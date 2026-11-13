# -*- coding: utf-8 -*-
"""Emit a reader / download links manifest for the catalogue.

By default it covers the 71 PCA + BCIT works added in this batch (id >= 220);
pass --all to cover every work. The URLs are deterministic (they depend only on
the catalogue paths and the release asset naming), so the manifest is correct
whether or not the PDFs have finished uploading yet.

    python build/make_links.py [--all]
"""

import hashlib
import json
import os
import re
import sys
from urllib.parse import quote

import lib_release  # noqa: E402  (release-bucket routing for PDF URLs)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")
INDEX = os.path.join(ROOT, "library", "pdfindex.json")
OWNER = "pro-instcontrol"
REPO = "pro-instcontrol.github.io"
TAG = "library-pdfs"
RELEASE_BASE = "https://github.com/%s/%s/releases/download/%s/" % (OWNER, REPO, TAG)
SITE = "https://pro-instcontrol.github.io"

# Catalogue path -> {u: same-origin pdf-store path, ...}, built by
# build/make_pdfstore.py. The reader page only honours the `f` parameter
# (a same-origin pdf-store URL it can read with range requests); a release
# URL cannot be rendered (CORS + Content-Disposition: attachment). So the
# manifest must carry the pdf-store `f` link, never the release `u`.
_INDEX = {}
try:
    _INDEX.update(json.load(open(INDEX, encoding="utf-8")))
except (OSError, ValueError):
    pass


def pdf_asset_name(path):
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]
    base = os.path.basename(path).rsplit(".", 1)[0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")[:40] or "doc"
    return "%s__%s.pdf" % (slug, h)


def reader_link(path, title):
    """Same-origin pdf-store reader URL (renders inline), mirroring
    books_site.reader_href. Falls back to the release URL only if the path
    is absent from the index (so the link is never dead)."""
    info = _INDEX.get(path) or {}
    if info.get("u"):
        q = [("f", info["u"]), ("t", title)]
    else:
        q = [("f", lib_release.asset_url(path)), ("t", title)]
    return (SITE + "/books/reader/?" +
            "&".join("%s=%s" % (k, quote(v, safe="")) for k, v in q))


def main():
    only_new = "--all" not in sys.argv
    cat = json.load(open(CAT, encoding="utf-8"))
    out = []
    for w in sorted(cat["works"], key=lambda x: x["id"]):
        if only_new and w["id"] < 220:
            continue
        docs = []
        for d in (w.get("docs") or []):
            p = d.get("path") or ""
            if not p.lower().endswith(".pdf"):
                continue
            u = lib_release.asset_url(p)
            docs.append({
                "title": d.get("title") or os.path.basename(p),
                "download": u,
                "reader": reader_link(p, d.get("title") or os.path.basename(p)),
            })
        if not docs:
            continue
        out.append({
            "id": w["id"], "title": w["title"],
            "domain": w.get("domain"), "n_docs": len(docs),
            "work_page": SITE + "/books/work/%d/" % w["id"],
            "vi_work_page": SITE + "/vi/books/work/%d/" % w["id"],
            "docs": docs,
        })
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    path = os.path.join(ROOT, "work", "library_new_links.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nd = sum(o["n_docs"] for o in out)
    print("wrote %s : %d works, %d docs" % (os.path.relpath(path, ROOT), len(out), nd))


if __name__ == "__main__":
    main()
