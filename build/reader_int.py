# -*- coding: utf-8 -*-
"""CSIA Integrator Guide, Volume 1 (2000) — reader pages for translated chapters.

Run:  python build/reader_int.py          # every chapter that has a module
      python build/reader_int.py 3        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import int_common as C  # noqa: E402

# Chapter number -> module name.
MODULES = {
    1: "int_ch01", 2: "int_ch02", 3: "int_ch03",
    4: "int_ch04", 5: "int_ch05", 6: "int_ch06",
    7: "int_ch07", 8: "int_ch08", 9: "int_ch09",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("int", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
