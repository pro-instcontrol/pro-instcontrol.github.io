"""One-off + reusable pass: de-duplicate inline-SVG <defs> IDs in published HTML.

The transform itself lives in svg_ids.namespace_svg_ids (also wired into
framework.write()). This script applies it to the already-built site so the
committed pages are valid HTML. Safe to re-run: idempotent.

Usage:
    python build/apply_svg_ids.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from svg_ids import namespace_svg_ids

ROOT = os.path.dirname(HERE)  # project root

# Where the published SVG-bearing pages live.
TREES = [
    ".",                      # root framework pages
    "books",
    "vi/books",
    "es",
]


def iter_html():
    for tree in TREES:
        base = os.path.join(ROOT, tree)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in files:
                if fn.endswith(".html"):
                    yield os.path.join(dirpath, fn)


def main():
    changed = 0
    total = 0
    for path in iter_html():
        total += 1
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        if "<svg" not in html:
            continue
        fixed = namespace_svg_ids(html)
        if fixed != html:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(fixed)
            changed += 1
    print("scanned %d html files, rewrote %d (svg defs namespaced)" % (total, changed))


if __name__ == "__main__":
    main()
