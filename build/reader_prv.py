# -*- coding: utf-8 -*-
"""Crosby *Pressure Relief Valve Engineering Handbook* (TP-V300, 1997) — reader pages.

Run:  python build/reader_prv.py          # every chapter that has a module
      python build/reader_prv.py 1        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prv_common as C  # noqa: E402

# Chapter number -> module name.
MODULES = {
    1: "prv_ch01",
    2: "prv_ch02",
    3: "prv_ch03",
    4: "prv_ch04",
    5: "prv_ch05",
    6: "prv_ch06",
    7: "prv_ch07",
    8: "prv_ch08",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("prv", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
