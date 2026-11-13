# -*- coding: utf-8 -*-
"""Upload every catalogue PDF not yet on its target release, via curl.

GitHub caps 1,000 assets per release, so new (id >= 220) PDFs are split across
library-pdfs-2 / library-pdfs-3 (the routing is defined once in
build/lib_release.py and replayed here, in build/make_links.py and in
build/books_site.py so all three agree on where each file lives).

The token is taken from the GH_TOKEN environment variable -- never written to
disk. Idempotent: existing release assets are skipped. Missing source files
(orphaned catalogue entries) are skipped with no retries.
"""

import json
import os
import subprocess
import sys
import time
from urllib.parse import quote

import lib_release

OWNER = "pro-instcontrol"
REPO = "pro-instcontrol.github.io"


def curl(args, tok, timeout=60):
    cmd = ["curl", "-s", "--max-time", str(timeout), "-H",
           "Authorization: Bearer " + tok] + args
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 30)


def get_release(tok, tag):
    """Return (id, name) for an existing release, creating it if absent."""
    r = curl(["-H", "Accept: application/vnd.github+json",
              "https://api.github.com/repos/%s/%s/releases/tags/%s"
              % (OWNER, REPO, tag)], tok)
    if r.returncode == 0 and r.stdout.lstrip().startswith("{"):
        try:
            d = json.loads(r.stdout)
            if "id" in d:
                return d["id"], d.get("name", tag)
        except ValueError:
            pass
    body = json.dumps({"tag_name": tag, "name": tag, "draft": False,
                       "prerelease": False, "target_commitish": "main"})
    r2 = curl(["-X", "POST", "-H", "Accept: application/vnd.github+json",
               "-H", "Content-Type: application/json", "-d", body,
               "https://api.github.com/repos/%s/%s/releases" % (OWNER, REPO)],
              tok)
    try:
        d = json.loads(r2.stdout)
        if "id" in d:
            return d["id"], d.get("name", tag)
    except ValueError:
        pass
    raise SystemExit("create release %s failed: %s" % (tag, r2.stdout[:200]))


def existing_assets(tok, rid):
    names = set()
    page = 1
    while True:
        r = curl(["-H", "Accept: application/vnd.github+json",
                  "https://api.github.com/repos/%s/%s/releases/%d/assets"
                  "?per_page=100&page=%d" % (OWNER, REPO, rid, page)], tok)
        if r.returncode != 0 or not r.stdout.strip():
            break
        try:
            a = json.loads(r.stdout)
        except ValueError:
            break
        if not a:
            break
        names.update(x["name"] for x in a)
        if len(a) < 100:
            break
        page += 1
    return names


def upload(name, path, rid, tok):
    # Git Bash curl wants forward slashes; the catalogue already stores them.
    full = path
    url = ("https://uploads.github.com/repos/%s/%s/releases/%d/assets?name=%s"
           % (OWNER, REPO, rid, quote(name)))
    for attempt in range(4):
        try:
            r = curl(["-X", "POST", "-H", "Content-Type: application/pdf",
                      "--data-binary", "@" + full, url], tok, timeout=600)
            if r.returncode == 0 and '"id"' in r.stdout:
                return True, None
            if "already_exists" in r.stdout:
                return True, "exists"
            if "file_count limited" in r.stdout:
                # Hard 1,000-asset cap -- retrying cannot help this file.
                return False, "file_count_limit"
            msg = (r.stdout.strip() or r.stderr.strip())[:160]
        except subprocess.TimeoutExpired:
            msg = "timeout"
        except Exception as exc:                          # noqa: BLE001
            msg = str(exc)[:160]
        if attempt < 3:
            time.sleep(3)
    return False, msg


def main():
    tok = os.environ["GH_TOKEN"]
    cat = json.load(open(lib_release.CAT, encoding="utf-8"))

    rid_cache = {}
    have_cache = {}

    def rid_for(tag):
        if tag not in rid_cache:
            rid_cache[tag], _ = get_release(tok, tag)
            have_cache[tag] = existing_assets(tok, rid_cache[tag])
        return rid_cache[tag]

    print("resolving release ids ...", flush=True)
    for tag in ("library-pdfs", "library-pdfs-2", "library-pdfs-3"):
        rid = rid_for(tag)
        print("  %s -> release %d (%d assets present)"
              % (tag, rid, len(have_cache[tag])), flush=True)

    up = skip = fail = miss = 0
    total = 0
    for w in sorted(cat["works"], key=lambda x: x["id"]):
        for d in (w.get("docs") or []):
            p = d.get("path") or ""
            if not p.lower().endswith(".pdf"):
                continue
            total += 1
            tag = lib_release.release_tag(p)
            name = lib_release.asset_name(p)
            rid = rid_for(tag)
            if name in have_cache[tag]:
                skip += 1
                continue
            if not os.path.exists(p):          # source file gone; skip (no retries)
                miss += 1
                continue
            ok, err = upload(name, p, rid, tok)
            if ok:
                up += 1
                have_cache[tag].add(name)
                if err != "exists":
                    print("  + [%d/%d] %s -> %s" % (up, total, name[:50], tag),
                          flush=True)
            else:
                fail += 1
                print("  ! FAIL %s -> %s" % (name, err), flush=True)

    print("\nuploaded %d, skipped %d (present), missing %d (no source), "
          "failed %d  (scanned %d docs)" % (up, skip, miss, fail, total),
          flush=True)


if __name__ == "__main__":
    main()
