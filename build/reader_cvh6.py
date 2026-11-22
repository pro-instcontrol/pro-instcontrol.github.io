# -*- coding: utf-8 -*-
"""Runner for Emerson Control Valve Handbook 6th ed reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cvh6_common as C  # noqa: E402

MODULES = {
    1: "cvh6_ch01",
    2: "cvh6_ch02",
    3: "cvh6_ch03",
    4: "cvh6_ch04",
    5: "cvh6_ch05",
    6: "cvh6_ch06",
    7: "cvh6_ch07",
    8: "cvh6_ch08",
    9: "cvh6_ch09",
    10: "cvh6_ch10",
    11: "cvh6_ch11",
    12: "cvh6_ch12",
    13: "cvh6_ch13",
    14: "cvh6_ch14",
    15: "cvh6_ch15",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("cvh6", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
