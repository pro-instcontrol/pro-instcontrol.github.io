# -*- coding: utf-8 -*-
"""Runner for Instrumentation and Process Control reader pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ipc_common as C  # noqa: E402

MODULES = {
    1: "ipc_ch01",
    2: "ipc_ch02",
    3: "ipc_ch03",
    4: "ipc_ch04",
    5: "ipc_ch05",
    6: "ipc_ch06",
    7: "ipc_ch07",
    8: "ipc_ch08",
}


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for num, mod in sorted(MODULES.items()):
        if only is not None and num != only:
            continue
        try:
            m = C.build("ipc", num, mod)
        except ImportError:
            print("  (chapter %d has no module yet — skipped)" % num)
            continue
        print("  chapter %d: %d pages source, figures %d"
              % (num, m.PAGES_SRC, m.body_vi().count('class="figure"')))


if __name__ == "__main__":
    main()
