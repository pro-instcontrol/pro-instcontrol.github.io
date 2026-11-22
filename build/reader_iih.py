# -*- coding: utf-8 -*-
"""Runner for 3G E-learning Illustrated Handbook of Industrial
Instrumentation & Control reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iih_common as C  # noqa: E402

MODULES = {
    1: "iih_ch01",
    2: "iih_ch02",
    3: "iih_ch03",
    4: "iih_ch04",
    5: "iih_ch05",
    6: "iih_ch06",
    7: "iih_ch07",
    8: "iih_ch08",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("iih", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
