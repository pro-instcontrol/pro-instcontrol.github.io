# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — reader pages for the translated chapters.

Run:  python build/reader_sis.py          # every chapter that has a module
      python build/reader_sis.py 3        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pcsis_common as C   # noqa: E402

MODULES = {3: "sis_ch03", 4: "sis_ch04", 5: "sis_ch05", 6: "sis_ch06",
           7: "sis_ch07", 8: "sis_ch08", 9: "sis_ch09", 10: "sis_ch10",
           11: "sis_ch11",
           12: "sis_ch12",
           13: "sis_ch13", 14: "sis_ch14", 15: "sis_ch15",
           16: "sis_ch16"}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("sis", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
