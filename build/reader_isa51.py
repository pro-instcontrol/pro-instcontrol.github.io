# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1-1984 (R1992) — reader pages for translated chapters.

Run:  python build/reader_isa51.py          # every chapter that has a module
      python build/reader_isa51.py 3        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import isa51_common as C  # noqa: E402

# Chapter number -> module name. Add a module here as each chapter is translated.
MODULES = {
    1: "isa51_ch01", 2: "isa51_ch02", 3: "isa51_ch03",
    4: "isa51_ch04", 5: "isa51_ch05", 6: "isa51_ch06", 7: "isa51_ch07",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("isa51", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
