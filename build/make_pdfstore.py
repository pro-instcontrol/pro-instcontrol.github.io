"""Publish the library's PDF bytes so the reader can stream them.

Why this exists
---------------
The reader used to hand a URL to docs.google.com/gview, which refuses anything
much over 30 MB ("This file is too large to preview").  Two books are 111 MB
and 147 MB, so those works could not be opened at all.  The replacement is
pdf.js, running on the site itself, fetching the file over HTTP range requests.

Where the bytes live is the whole problem.  Measured, not assumed:

  * GitHub Release assets — `Content-Disposition: attachment`, no
    `Access-Control-Allow-Origin`; `fetch()` dies with "Failed to fetch", and
    the native viewer downloads instead of rendering.
  * raw.githubusercontent.com — sends `Access-Control-Allow-Origin: *` and
    honours Range, but answers the CORS preflight for a `Range` header with
    403, and starts returning 404 for large files.  Unusable.
  * cdn.jsdelivr.net — correct preflight, but 404s any file over 20 MB.
  * **GitHub Pages — same origin as the site, `Content-Type: application/pdf`,
    `Accept-Ranges: bytes`, 206 Partial Content, no attachment header.**  No
    CORS, no preflight, CDN-backed.  This is the one that works.

So the PDFs live in companion repositories with Pages enabled.  The library is
~1.5 GB and a Pages site is capped at 1 GB, so it is spread over two of them,
filled greedily by size.

Rules
-----
* Names are content-addressed (``name__sha1-16.pdf``) and never change, which
  is what makes long-lived caching safe.
* GitHub refuses a file over 100 MB, so anything above ~90 MB is split into
  page-range parts.  ``pypdf``'s ``append(src, pages=(a, b))`` is the only sane
  way: it copies page objects without decoding their image streams.  (A
  per-page ``add_page`` loop rewrote a 40-page slice as 53 MB because it kept
  the whole cross-reference table.)
* ``library/pdfindex.json`` is the contract with ``books_site.py``; the site
  never guesses a filename, and never guesses a repository either.
* A path already in the index keeps its repository, so adding a book never
  moves an existing one.

Usage
-----
    python build/make_pdfstore.py --index          # metadata only
    python build/make_pdfstore.py --stage          # + copy/split the files
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

PDF_ROOT = "D:/Process Control and Automation"
CAT = os.path.join(ROOT, "library", "catalog.json")
INDEX = os.path.join(ROOT, "library", "pdfindex.json")

# Two Pages sites, each capped at 1 GB by GitHub.  The library is ~1.5 GB.
STORES = [("pdf-store", "D:/pdf-store"), ("pdf-store-b", "D:/pdf-store-b")]
STORE_CAP = 760 * 1024 * 1024

# GitHub's hard per-file ceiling is 100 MB; stay clear of it.
SPLIT_AT = 90 * 1024 * 1024


def asset_name(path):
    """Deterministic, collision-safe filename for a catalogue PDF path."""
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]
    base = os.path.basename(path).rsplit(".", 1)[0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")[:40] or "doc"
    return "%s__%s.pdf" % (slug, h)


def resolve(path):
    """Catalogue paths are absolute for most works, relative to PDF_ROOT for the rest."""
    if os.path.exists(path):
        return path
    cand = os.path.join(PDF_ROOT, path.replace("/", os.sep))
    return cand if os.path.exists(cand) else None


def catalogue_paths():
    cat = json.load(open(CAT, encoding="utf-8"))
    works = cat["works"] if isinstance(cat, dict) else cat
    seen = []
    for w in works:
        for d in (w.get("docs") or []):
            p = d.get("path") or ""
            if p.lower().endswith(".pdf") and p not in seen:
                seen.append(p)
    return seen


SCRATCH = os.path.join(ROOT, "work", "pdfsplit")


def _write_part(src, a, b, path):
    import pypdf

    w = pypdf.PdfWriter()
    w.append(src, pages=(a, b))
    with open(path, "wb") as fh:
        w.write(fh)
    return os.path.getsize(path)


def _leaves(src, a, b, limit, stem, depth=0):
    """Split [a, b) until every part is under `limit`, by measured size.

    Splitting evenly by page count does not work: in one 147 MB scan nearly all
    of the imagery sits in one half, so a 50/50 page split produced 142 MB and
    5 MB. The only reliable measure is the file that comes out.
    """
    tmp = os.path.join(SCRATCH, "%s_%d_%d.pdf" % (stem, a, b))
    size = _write_part(src, a, b, tmp)
    if size <= limit or b - a <= 1 or depth > 6:
        return [(a, b, tmp, size)]
    os.remove(tmp)
    mid = (a + b) // 2
    return (_leaves(src, a, mid, limit, stem, depth + 1)
            + _leaves(src, mid, b, limit, stem, depth + 1))


def plan(path):
    """Decide how one PDF is published: a single file, or page-range parts."""
    src = resolve(path)
    if not src:
        return None
    size = os.path.getsize(src)
    name = asset_name(path)
    if size <= SPLIT_AT:
        return {"f": name, "n": 1, "parts": [], "bytes": size}

    import pypdf

    os.makedirs(SCRATCH, exist_ok=True)
    total = len(pypdf.PdfReader(src).pages)
    stem = name[:-4]
    leaves = _leaves(src, 0, total, SPLIT_AT, stem)
    n = len(leaves)
    parts, ranges = [], []
    for i, (a, b, tmp, _sz) in enumerate(leaves):
        final = os.path.join(SCRATCH, "%s__p%dof%d.pdf" % (stem, i + 1, n))
        if os.path.exists(final):
            os.remove(final)
        os.replace(tmp, final)
        parts.append("%s__p%dof%d.pdf" % (stem, i + 1, n))
        ranges.append("%d-%d" % (a + 1, b))
    return {"f": parts[0], "n": n, "parts": parts, "r": "|".join(ranges),
            "bytes": size, "pages": total}


def build_index():
    try:
        old = json.load(open(INDEX, encoding="utf-8"))
    except (OSError, ValueError):
        old = {}

    planned = []
    for p in catalogue_paths():
        info = plan(p)
        if info:
            planned.append((p, info))

    # Fill each store greedily, biggest first.  A path that already has a home
    # keeps it: moving one would break every link pointing at it.
    used = {name: 0 for name, _ in STORES}
    home = {}
    for p, info in planned:
        prev = (old.get(p) or {}).get("s")
        if prev in used:
            home[p] = prev
            used[prev] += info["bytes"]
    for p, info in sorted(planned, key=lambda t: -t[1]["bytes"]):
        if p in home:
            continue
        room = [n for n, _ in STORES if used[n] + info["bytes"] <= STORE_CAP]
        pick = min(room, key=lambda n: used[n]) if room else min(used, key=used.get)
        home[p] = pick
        used[pick] += info["bytes"]

    out = {}
    for p, info in planned:
        store = home[p]
        entry = dict(info)
        entry["s"] = store
        entry["u"] = "/%s/pdfs/%s" % (store, info["f"])
        if info["n"] > 1:
            entry["parts"] = ["/%s/pdfs/%s" % (store, f) for f in info["parts"]]
        out[p] = entry

    json.dump(out, open(INDEX, "w", encoding="utf-8"), ensure_ascii=False,
              indent=1, sort_keys=True)
    total = sum(v["bytes"] for v in out.values())
    print("index: %d PDFs, %.0f MB, %d split" % (len(out), total / 1048576,
                                                 sum(1 for v in out.values() if v["n"] > 1)))
    for name, _ in STORES:
        n = sum(1 for v in out.values() if v["s"] == name)
        print("  %-12s %4d files  %.0f MB" % (name, n, used[name] / 1048576))
    return out


def stage(index):
    """Materialise the two repositories that Pages will publish."""
    import shutil

    for name, root in STORES:
        os.makedirs(os.path.join(root, "pdfs"), exist_ok=True)
        with open(os.path.join(root, ".nojekyll"), "w") as fh:
            fh.write("")
        with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as fh:
            fh.write("<!doctype html><meta charset=utf-8><title>PDF store</title>"
                     "<p>PDF bytes for the Pro InstControl library. "
                     "Served to <a href='https://pro-instcontrol.github.io/books/'>"
                     "the reader</a>.</p>\n")

    done = 0
    for path, info in sorted(index.items()):
        src = resolve(path)
        if not src:
            continue
        dest = dict(STORES)[info["s"]]
        if info["n"] == 1:
            target = os.path.join(dest, "pdfs", info["f"])
            if not (os.path.exists(target) and os.path.getsize(target) == info["bytes"]):
                try:
                    os.link(src, target)
                except OSError:
                    shutil.copy2(src, target)
        else:
            for i in range(info["n"]):
                base = os.path.basename(info["parts"][i])
                target = os.path.join(dest, "pdfs", base)
                if os.path.exists(target):
                    continue
                piece = os.path.join(SCRATCH, base)
                if not os.path.exists(piece):
                    raise SystemExit("missing split part %s — rerun --index" % base)
                try:
                    os.link(piece, target)
                except OSError:
                    shutil.copy2(piece, target)
        done += 1
        if done % 100 == 0:
            print("  staged %d/%d" % (done, len(index)))

    for name, root in STORES:
        d = os.path.join(root, "pdfs")
        files = os.listdir(d)
        total = sum(os.path.getsize(os.path.join(d, f)) for f in files)
        print("staged %-12s %4d files  %.0f MB" % (name, len(files), total / 1048576))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", action="store_true", help="write the PDF trees")
    ap.add_argument("--index", action="store_true", help="rebuild pdfindex.json only")
    args = ap.parse_args()
    index = build_index()
    if args.stage:
        stage(index)


if __name__ == "__main__":
    main()
