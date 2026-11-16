# -*- coding: utf-8 -*-
"""Peter Smith & R. W. Zappe, *Valve Selection Handbook*, 5th ed. (Gulf
Professional Publishing / Elsevier, 2004) — reader pages.

Run:  python build/reader_vsh.py          # every unit that has a module
      python build/reader_vsh.py 1        # one unit
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vsh_common as C  # noqa: E402

# Unit number -> module name.
MODULES = {
    1: "vsh_ch01",
    2: "vsh_ch02",
    3: "vsh_ch03",
    4: "vsh_ch04",
    5: "vsh_ch05",
    6: "vsh_ch06",
    7: "vsh_ch07",
    8: "vsh_ch08",
    9: "vsh_ch09",
    10: "vsh_ch10",
    11: "vsh_ch11",
    12: "vsh_ch12",
    13: "vsh_ch13",
    14: "vsh_ch14",
    15: "vsh_ch15",
    16: "vsh_ch16",
    17: "vsh_ch17",
    18: "vsh_ch18",
    19: "vsh_ch19",
    20: "vsh_ch20",
    21: "vsh_ch21",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("vsh", num, mod)
        except ImportError:
            print("  (unit %d has no module yet — skipped)" % num)
            continue
        print("  unit %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
