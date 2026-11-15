# -*- coding: utf-8 -*-
"""Anna-Mari Heikkilä, *Inherent Safety in Process Plant Design* (VTT 384,
1999) — reader pages.

Run:  python build/reader_isd.py          # every chapter that has a module
      python build/reader_isd.py 1        # one chapter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import isd_common as C  # noqa: E402

# Chapter number -> module name.
MODULES = {
    1: "isd_ch01",
    2: "isd_ch02",
    3: "isd_ch03",
    4: "isd_ch04",
    5: "isd_ch05",
    6: "isd_ch06",
    7: "isd_ch07",
    8: "isd_ch08",
    9: "isd_ch09",
    10: "isd_ch10",
    11: "isd_ch11",
    12: "isd_ch12",
    13: "isd_ch13",
    14: "isd_ch14",
    15: "isd_ch15",
    16: "isd_ch16",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("isd", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
