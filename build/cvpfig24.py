# -*- coding: utf-8 -*-
"""Vector redraw of Figure 24-1 in Baumann Chapter 24, *Control Valve Primer*.

The printed figure is an unlabelled cross-section of a typical bellows seal with
internal pressurization. This module redraws it as a labelled schematic: bonnet,
stem, bellows, backup packing, telltale connection, gasket and valve plug.
Bilingual callouts are derived from the chapter text, not from printed labels.
"""
from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _circle, _defs, _fig,
                  _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


@_reg
def fig_f241():
    """Figure 24-1 -- typical bellows seal with internal pressurization."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Đệm màng của van điều khiển / Valve bellows seal with internal pressurization",
               10.0, color=INK, weight="600"))

    # Bonnet cross-section: two hatched walls around a central stem.
    o.append(_poly([(286, 72), (292, 62), (372, 62), (378, 72),
                    (392, 226), (414, 258), (414, 284), (266, 284),
                    (266, 258), (288, 226)], fill="#eef1f5", sw=1.4, close=True))
    for x in (266, 414):
        o.append(_line(x, 258, x + (12 if x == 266 else -12), 226,
                       sw=1.0, color="#9aa4ae"))
    o.append(_rect(250, 284, 180, 12, fill="#d8e0e8", sw=1.2))
    o.append(_rect(262, 296, 156, 8, fill="#f2e5cf", sw=1.0))

    # Stem and plug.
    o.append(_rect(328, 42, 16, 250, fill="#fbfaf7", sw=1.4))
    o.append(_rect(320, 282, 32, 16, fill="#dfe7f0", sw=1.2))
    o.append(_poly([(320, 298), (336, 312), (352, 298)],
                   fill="#d7e3f1", sw=1.2, close=True))
    o.append(_rect(332, 312, 8, 14, fill="#fbfaf7", sw=1.0))

    # Backup packing and follower above the bellows.
    for y in (70, 80, 90):
        o.append(_rect(302, y, 26, 7, fill="#e6d7bd", sw=0.9))
        o.append(_rect(344, y, 26, 7, fill="#e6d7bd", sw=0.9))
    o.append(_rect(296, 62, 80, 6, fill="#cbd5df", sw=1.0))

    # Bellows: zigzag convolutions between stem and bonnet wall.
    left, right = [(292 + (i % 2) * 8, 108 + i * 10) for i in range(9)], \
                  [(372 - (i % 2) * 8, 108 + i * 10) for i in range(9)]
    o.append(_poly(left, sw=1.5, color=BLUE))
    o.append(_poly(right, sw=1.5, color=BLUE))
    for i in range(9):
        o.append(_line(left[i][0], left[i][1], right[i][0], right[i][1],
                       sw=1.0, color="#8fb0c8"))
    o.append(_rect(290, 100, 84, 6, fill="#cbd5df", sw=1.0))
    o.append(_rect(290, 188, 84, 6, fill="#cbd5df", sw=1.0))

    # Telltale connection between bellows and backup packing, to a gauge.
    o.append(_line(378, 102, 504, 102, sw=2.0, color=GREEN))
    o.append(_circle(520, 102, 16, fill="#fbfaf7", sw=1.4, color=GREEN))
    o.append(_txt(520, 106, "P", 10, color=GREEN, weight="600"))
    o.append(_arrow(410, 102, 470, 102, sw=1.0, color=GREEN))
    o.append(T(520, 72, "Kết nối báo động / Telltale connection", 8.0,
               anchor="middle", color=GREEN))

    # Bilingual callouts with leaders.
    def label(x, y, text, tx, ty, color=INK, anchor="end"):
        o.append(_line(x, y, tx, ty, sw=0.9, color=GREY))
        o.append(T(tx + (-4 if anchor == "end" else 4), ty + 2.5, text,
                   8.0, anchor=anchor, color=color))

    label(316, 76, "Đệm dự phòng / Backup packing", 210, 76)
    label(330, 140, "Thân van / Valve stem", 210, 140)
    label(300, 158, "Ống màng / Bellows", 210, 158, color=BLUE)
    label(268, 292, "Gioăng / Gasket", 210, 292, color=RED)
    o.append(_line(414, 258, 616, 246, sw=0.9, color=GREY))
    o.append(T(620, 249, "Nắp van / Bonnet", 8.0, anchor="end"))

    # Bilingual strip inside the SVG.
    o.append(T(340, 352, "Hình 24-1 · Đệm màng điển hình với áp suất cấp bên trong",
               7.2, color=INK))
    o.append(T(340, 368, "Figure 24-1 · Typical bellows seal with internal pressurization",
               7.2, color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Sơ đồ cắt đệm màng van điều khiển")),
                "Hình 24-1 · Đệm màng điển hình với áp suất cấp bên trong.",
                "Figure 24-1 · Typical bellows seal with internal pressurization.",
                "Sơ đồ cắt đệm màng, đệm dự phòng, kết nối báo động và nắp van",
                "Cutaway of a bellows seal with backup packing, telltale connection and bonnet")
