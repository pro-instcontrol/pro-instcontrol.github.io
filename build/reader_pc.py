# -*- coding: utf-8 -*-
"""Practical Process Control — reader pages for the translated chapters.

Run:  python build/reader_pc.py          # every chapter that has a module
      python build/reader_pc.py 3        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pcsis_common as C   # noqa: E402

MODULES = {3: "pc_ch03", 4: "pc_ch04", 5: "pc_ch05", 6: "pc_ch06", 7: "pc_ch07", 8: "pc_ch08", 9: "pc_ch09", 10: "pc_ch10", 11: "pc_ch11", 12: "pc_ch12"}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("pc", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
