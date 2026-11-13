# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — reader pages for translated chapters.

Run:  python build/reader_bolton.py          # every chapter that has a module
      python build/reader_bolton.py 1        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as C   # noqa: E402

# Chapter number -> module name. Add a module here as each chapter is translated.
MODULES = {1: "bolton_ch01", 2: "bolton_ch02", 3: "bolton_ch03", 4: "bolton_ch04", 5: "bolton_ch05", 6: "bolton_ch06", 7: "bolton_ch07"}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("bolton", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
