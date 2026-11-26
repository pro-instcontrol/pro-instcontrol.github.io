# -*- coding: utf-8 -*-
"""Runner for the R. STAHL ExProtection Global-America-Basics reader."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expb_common as C  # noqa: E402

MODULES = {
    1: "expb_ch01",
    2: "expb_ch02",
    3: "expb_ch03",
    4: "expb_ch04",
    5: "expb_ch05",
    6: "expb_ch06",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("expb", num, mod)
        except ImportError:
            print("  (unit %d has no module yet — skipped)" % num)
            continue
        print("  unit %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
