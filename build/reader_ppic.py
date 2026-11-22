# -*- coding: utf-8 -*-
"""Runner for L. N. Jalali (ed.) Handbook on Power Plant Instrumentation
and Control reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ppic_common as C  # noqa: E402

MODULES = {
    1: "ppic_ch01",
    2: "ppic_ch02",
    3: "ppic_ch03",
    4: "ppic_ch04",
    5: "ppic_ch05",
    6: "ppic_ch06",
    7: "ppic_ch07",
    8: "ppic_ch08",
    9: "ppic_ch09",
    10: "ppic_ch10",
    11: "ppic_ch11",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("ppic", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
