# -*- coding: utf-8 -*-
"""Site-wide local-link checker.

Walks every .html file under the project root (skipping build/, work/,
dist/, shots/ and dotted directories), resolves each href/src and reports
the ones that do not land on a file or a directory with an index.html.

Run:  python build/check_links.py
Exit code is 0 when nothing is broken, 1 otherwise.
"""
import html
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_ROOT = {"build", "work", "dist", "node_modules", "assets_tmp", "shots"}

# A word/hyphen boundary matters: without it, data-src="..." matches as src.
RX = re.compile(r'(?<![\w-])(?:href|src)="([^"]*)"')
EXTERNAL = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#", "//")


def pages():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT)
        if rel == ".":
            dn[:] = [d for d in dn if d not in SKIP_ROOT and not d.startswith(".")]
        else:
            dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return out


def resolves(base_dir, url):
    p = unquote(url.split("#")[0].split("?")[0])
    if not p:
        return True
    if p.startswith("/"):
        target = os.path.normpath(os.path.join(ROOT, p.lstrip("/")))
    else:
        target = os.path.normpath(os.path.join(base_dir, p))
    if os.path.isfile(target):
        return True
    return os.path.isdir(target) and os.path.isfile(os.path.join(target, "index.html"))


def main():
    broken, total = [], 0
    for pg in pages():
        base = os.path.dirname(pg)
        src = open(pg, encoding="utf-8", errors="replace").read()
        for m in RX.finditer(src):
            url = html.unescape(m.group(1))
            if url.startswith(EXTERNAL):
                continue
            total += 1
            if not resolves(base, url):
                broken.append((os.path.relpath(pg, ROOT), url))

    print("pages %d, local references %d, broken %d" % (len(pages()), total, len(broken)))
    for pg, url in broken[:40]:
        print("  %s -> %s" % (pg, url))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
