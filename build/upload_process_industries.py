# -*- coding: utf-8 -*-
"""Upload only the Process Industries PDFs that are not yet on the release.

Scoped deliberately: it touches works 100, 149 (the Process Industries single
file only) and 214-219. Every other work in the catalogue is left alone.

For each document it computes the release-asset name with the same function
books_site.py uses (so the page links resolve), skips assets that already exist,
and uploads the rest. Writes /tmp/pi_links.json with the reader / download URLs.

    TOKEN=... python build/upload_process_industries.py
"""

import hashlib
import json
import os
import re
import sys
import urllib.request
import urllib.error
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")

OWNER = "pro-instcontrol"
REPO = "pro-instcontrol.github.io"
TAG = "library-pdfs"
RELEASE_BASE = ("https://github.com/%s/%s/releases/download/%s/" % (OWNER, REPO, TAG))
SITE = "https://pro-instcontrol.github.io"
TARGET_IDS = {100, 149, 214, 215, 216, 217, 218, 219}


def pdf_asset_name(path):
    """Must match books_site.pdf_asset_name byte for byte."""
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]
    base = os.path.basename(path).rsplit(".", 1)[0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")[:40] or "doc"
    return "%s__%s.pdf" % (slug, h)


def api(url, tok, method="GET", data=None, ctype=None):
    headers = {"Authorization": "Bearer " + tok,
               "Accept": "application/vnd.github+json",
               "User-Agent": "wb-uploader"}
    if ctype:
        headers["Content-Type"] = ctype
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    return json.load(urllib.request.urlopen(req, timeout=300))


def existing_assets(tok, rel_id):
    names = set()
    page = 1
    while True:
        a = api("https://api.github.com/repos/%s/%s/releases/%d/assets"
                "?per_page=100&page=%d" % (OWNER, REPO, rel_id, page), tok)
        if not a:
            break
        for x in a:
            names.add(x["name"])
        if len(a) < 100:
            break
        page += 1
    return names


def upload(tok, rel_id, name, path):
    full = path.replace("/", os.sep)
    size = os.path.getsize(full)
    with open(full, "rb") as fh:
        data = fh.read()
    url = ("https://uploads.github.com/repos/%s/%s/releases/%d/assets?name=%s"
           % (OWNER, REPO, rel_id, quote(name)))
    try:
        api(url, tok, method="POST", data=data, ctype="application/pdf")
        return True, size, None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:200]
        if exc.code == 422 and "already_exists" in body:
            return True, size, "exists"
        return False, size, "HTTP %s %s" % (exc.code, body)
    except Exception as exc:                       # noqa: BLE001
        return False, size, str(exc)[:200]


def main():
    tok = os.environ["TOKEN"]
    cat = json.load(open(CAT, encoding="utf-8"))
    rel = api("https://api.github.com/repos/%s/%s/releases/tags/%s"
              % (OWNER, REPO, TAG), tok)
    rel_id = rel["id"]
    have = existing_assets(tok, rel_id)
    print("release %s has %d assets already" % (rel_id, len(have)))

    targets = [w for w in cat["works"] if w["id"] in TARGET_IDS]
    targets.sort(key=lambda w: w["id"])

    links = []
    up = skip = fail = 0
    for w in targets:
        docs = w.get("docs") or []
        if w["id"] == 149:
            docs = [d for d in docs if (d.get("path") or "").startswith("D:/Process Industries")]
        wdocs = []
        for d in docs:
            p = d.get("path") or ""
            if not p.lower().endswith(".pdf"):
                continue
            name = pdf_asset_name(p)
            dl = RELEASE_BASE + name
            if name in have:
                skip += 1
                status = "skip"
            else:
                ok, size, err = upload(tok, rel_id, name, p)
                if ok:
                    up += 1
                    have.add(name)
                    status = "up" if err != "exists" else "exists"
                    print("  + %-55s %6.1f MB" % (name[:55], size / 1048576.0))
                else:
                    fail += 1
                    status = "FAIL"
                    print("  ! %s -> %s" % (name, err))
            wdocs.append({
                "title": d.get("title") or os.path.basename(p),
                "download": dl,
                "reader": SITE + "/books/reader/?u=" + quote(dl, safe=""),
                "status": status,
            })
        first = wdocs[0] if wdocs else None
        links.append({
            "id": w["id"], "title": w["title"],
            "work_page": SITE + "/books/work/%d/" % w["id"],
            "vi_work_page": SITE + "/vi/books/work/%d/" % w["id"],
            "docs": wdocs,
            "reader": first["reader"] if first else None,
            "download": first["download"] if first else None,
        })

    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    out = os.path.join(ROOT, "work", "pi_links.json")
    json.dump(links, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\nuploaded %d, skipped %d (already present), failed %d" % (up, skip, fail))
    print("links written to %s" % os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
