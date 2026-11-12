# -*- coding: utf-8 -*-
"""Upload every catalogue PDF that is not yet on the library-pdfs release.

Idempotent: it lists existing release assets once and skips any already there,
so it is safe to re-run and to use for the whole library, not just one batch.

    TOKEN=... python build/upload_library.py

Writes work/library_links.json with per-work reader / download URLs.
"""

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")

OWNER = "pro-instcontrol"
REPO = "pro-instcontrol.github.io"
TAG = "library-pdfs"
RELEASE_BASE = "https://github.com/%s/%s/releases/download/%s/" % (OWNER, REPO, TAG)
SITE = "https://pro-instcontrol.github.io"


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

    up = skip = fail = 0
    for w in sorted(cat["works"], key=lambda x: x["id"]):
        for d in (w.get("docs") or []):
            p = d.get("path") or ""
            if not p.lower().endswith(".pdf"):
                continue
            name = pdf_asset_name(p)
            if name in have:
                skip += 1
                continue
            ok, size, err = upload(tok, rel_id, name, p)
            if ok:
                up += 1
                have.add(name)
                if err != "exists":
                    print("  + %-55s %6.1f MB"
                          % (name[:55], size / 1048576.0))
            else:
                fail += 1
                print("  ! %s -> %s" % (name, err))
    print("\nuploaded %d, skipped %d (already present), failed %d"
          % (up, skip, fail))


if __name__ == "__main__":
    main()
