# -*- coding: utf-8 -*-
"""Runner for the Alan McMillan hazardous-area installations reader."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mcmillan_common as C  # noqa: E402

MODULES = {
    1: "mcmillan_ch01",
    2: "mcmillan_ch02",
    3: "mcmillan_ch03",
    4: "mcmillan_ch04",
    5: "mcmillan_ch05",
    6: "mcmillan_ch06",
    7: "mcmillan_ch07",
    8: "mcmillan_ch08",
    9: "mcmillan_ch09",
    10: "mcmillan_ch10",
    11: "mcmillan_ch11",
    12: "mcmillan_ch12",
    13: "mcmillan_ch13",
    14: "mcmillan_ch14",
    15: "mcmillan_ch15",
    16: "mcmillan_ch16",
    17: "mcmillan_ch17",
    18: "mcmillan_ch18",
    19: "mcmillan_ch19",
    20: "mcmillan_ch20",
    21: "mcmillan_ch21",
    22: "mcmillan_ch22",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("mcmillan", num, mod)
        except ImportError:
            print("  (unit %d has no module yet — skipped)" % num)
            continue
        print("  unit %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
