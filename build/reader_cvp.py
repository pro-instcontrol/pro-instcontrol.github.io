# -*- coding: utf-8 -*-
"""Runner for Baumann Control Valve Primer reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cvp_common as C  # noqa: E402

MODULES = {
    1: "cvp_ch01",
    2: "cvp_ch02",
    3: "cvp_ch03",
    4: "cvp_ch04",
    5: "cvp_ch05",
    6: "cvp_ch06",
    7: "cvp_ch07",
    8: "cvp_ch08",
    9: "cvp_ch09",
    10: "cvp_ch10",
    11: "cvp_ch11",
    12: "cvp_ch12",
    13: "cvp_ch13",
    14: "cvp_ch14",
    15: "cvp_ch15",
    16: "cvp_ch16",
    17: "cvp_ch17",
    18: "cvp_ch18",
    19: "cvp_ch19",
    20: "cvp_ch20",
    21: "cvp_ch21",
    22: "cvp_ch22",
    23: "cvp_ch23",
    24: "cvp_ch24",
    25: "cvp_ch25",
    26: "cvp_ch26",
    27: "cvp_ch27",
    28: "cvp_ch28",
    29: "cvp_ch29",
    30: "cvp_ch30",
    31: "cvp_ch31",
    32: "cvp_ch32",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("cvp", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
