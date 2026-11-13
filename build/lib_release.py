# -*- coding: utf-8 -*-
"""Deterministic mapping from a catalogue PDF path to its GitHub release bucket.

GitHub caps a single release at 1,000 assets, but a release has no total-size
cap. The library is ~2.4k PDFs / ~6.8 GB, so the assets are spread over several
releases:

  * ``library-pdfs``     -- legacy (catalogue id < 220) works, already uploaded.
  * ``library-pdfs-2``   -- the first 1,000 NEW (id >= 220) works' PDFs.
  * ``library-pdfs-3``   -- the remaining NEW PDFs.

The same ordering used here is replayed by build/make_links.py (page/download
URLs) and build/upload_curl.py (uploads), so the three never disagree about
which release a given file lives in.
"""

import hashlib
import json
import os
import re
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")
OWNER = "pro-instcontrol"
REPO = "pro-instcontrol.github.io"
SITE = "https://pro-instcontrol.github.io"

PER_RELEASE = 1000          # GitHub's hard asset-per-release ceiling
OLD_TAG = "library-pdfs"     # holds the legacy (id < 220) works
NEW_PREFIX = "library-pdfs-" # new works split into -2, -3, ... by global index
NEW_FROM_ID = 220           # catalogue works added in this batch

# cache: catalogue path -> release tag
_PATH_TAG = None


def asset_name(path):
    """Deterministic, collision-safe release-asset filename for a PDF path.

    Must match books_site.pdf_asset_name / make_pdfstore.asset_name byte for
    byte: slug(basename without ext)[:40] + "__" + sha1(path)[:16] + ".pdf".
    """
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]
    base = os.path.basename(path).rsplit(".", 1)[0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")[:40] or "doc"
    return "%s__%s.pdf" % (slug, h)


def _build():
    global _PATH_TAG
    if _PATH_TAG is not None:
        return _PATH_TAG
    cat = json.load(open(CAT, encoding="utf-8"))
    # Global ordering of NEW docs (id >= NEW_FROM_ID), works sorted by id,
    # docs in catalogue order. This is the single source of truth for bucketing.
    new_paths = []
    for w in sorted(cat["works"], key=lambda x: x["id"]):
        if w["id"] < NEW_FROM_ID:
            continue
        for d in (w.get("docs") or []):
            p = d.get("path") or ""
            if p.lower().endswith(".pdf"):
                new_paths.append(p)
    m = {}
    for i, p in enumerate(new_paths):
        tag = "%s%d" % (NEW_PREFIX, 2 + (i // PER_RELEASE))
        m[p] = tag
    # Legacy docs keep living in the original release.
    for w in cat["works"]:
        if w["id"] < NEW_FROM_ID:
            for d in (w.get("docs") or []):
                p = d.get("path") or ""
                if p.lower().endswith(".pdf"):
                    m.setdefault(p, OLD_TAG)
    _PATH_TAG = m
    return _PATH_TAG


def release_tag(path):
    return _build().get(path, OLD_TAG)


def asset_url(path):
    """Public download URL (Content-Disposition: attachment)."""
    tag = release_tag(path)
    return ("https://github.com/%s/%s/releases/download/%s/%s"
            % (OWNER, REPO, tag, asset_name(path)))


# books_site.py calls this by its old name.
pdf_url = asset_url


def reader_url(path):
    """Reader page URL; the reader itself resolves the inline (pdf-store) URL."""
    return SITE + "/books/reader/?u=" + quote(asset_url(path), safe="")


if __name__ == "__main__":
    import sys
    for p in sys.argv[1:]:
        print(p, "->", release_tag(p), asset_url(p))
