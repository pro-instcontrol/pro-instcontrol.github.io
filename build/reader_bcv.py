# -*- coding: utf-8 -*-
"""Runner for Borden ISA Control Valves excerpt reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bcv_common as C  # noqa: E402

MODULES = {
    5: "bcv_ch05",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("bcv", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
