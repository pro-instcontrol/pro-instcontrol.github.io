# -*- coding: utf-8 -*-
"""Vector redraw of Figure 23-1 in Baumann Chapter 23, *Control Valve Primer*.

The printed figure is a photograph of a water jet leaving a control valve
outlet, with undissolved vapour mixed into the water. This module redraws it
as a labelled schematic: valve body and seat, the two-phase jet, entrained
vapour bubbles, and the open-air region where the vapour redissolves.
Every function returns the standard 5-tuple via ``_fig()`` from ``vfig``.
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
def fig_f231():
    """Figure 23-1 -- liquid flashing in a control valve without choked flow."""
    w, h = 680, 330
    o = [_defs()]
    o.append(T(340, 24, "Hóa hơi chất lỏng trong van điều khiển / Liquid flashing in a control valve",
               10.2, color=INK, weight="600"))

    # Inlet pipe and simplified valve body with a plug against the seat.
    o.append(_rect(28, 132, 42, 66, fill="#e9eef5", sw=1.2))
    o.append(_rect(70, 104, 154, 122, fill="#e4ebf4", sw=1.4))
    o.append(_path("M96,142 L96,188 L154,188 L154,142 Z", fill="#fbfaf7", sw=1.1))
    o.append(_poly([(154, 142), (184, 160), (154, 178)], fill="#e9dcc5", sw=1.2, close=True))
    o.append(_line(184, 116, 184, 206, sw=3.0, color=INK))
    o.append(_line(184, 116, 184, 206, sw=1.0, color="#fbfaf7"))
    o.append(_poly([(140, 100), (174, 100), (174, 116), (140, 116)],
                   fill="#d7e3f1", sw=1.1, close=True))
    o.append(_line(157, 100, 157, 88, sw=1.4))
    o.append(_arrow(12, 165, 68, 165, sw=1.8, color=BLUE))

    # Two-phase jet leaving the outlet: water plume plus entrained vapour.
    plume = [(224, 150), (224, 180), (286, 214), (350, 232),
             (420, 238), (420, 92), (350, 98), (286, 116)]
    o.append(_poly(plume, fill="#dbeaf5", sw=1.5, color=BLUE, close=True))
    o.append(_path("M240,165 C286,158 330,170 410,165", fill="none", sw=1.5, color=BLUE))
    o.append(_path("M246,183 C294,194 340,190 414,196", fill="none", sw=1.1,
                   color="#8bb4cf", dash="4 3"))
    for cx, cy, r in [(266, 148, 7), (292, 176, 9), (318, 136, 6),
                      (336, 188, 11), (362, 154, 8), (382, 206, 6),
                      (398, 122, 9), (352, 112, 5), (276, 200, 5)]:
        o.append(_circle(cx, cy, r, fill="#ffffff", sw=1.0, color=GREY))

    # Open atmosphere to the right, where the vapour redissolves harmlessly.
    o.append(_rect(436, 70, 216, 194, fill="#fbfaf7", sw=1.1,
                   stroke="#b7bec6", dash="5 4"))
    o.append(T(544, 90, "Không khí tự do / Open air", 8.6, color=GREY))
    o.append(_arrow(420, 162, 470, 162, sw=1.6, color=BLUE))
    o.append(_path("M472,150 C486,142 496,150 508,144", fill="none", sw=1.1,
                   color="#9ab6c8", dash="3 3"))
    o.append(_path("M474,176 C488,186 500,176 514,184", fill="none", sw=1.1,
                   color="#9ab6c8", dash="3 3"))
    o.append(_circle(492, 164, 4, fill="#ffffff", sw=0.9, color=GREY))
    o.append(T(544, 232, "Hơi hòa tan lại / Vapor redissolves", 8.2, color=GREEN))

    # Callouts.
    o.append(T(49, 118, "Đầu vào P₁ / Inlet P₁", 8.0, anchor="start", color=BLUE))
    o.append(_line(180, 108, 180, 62, sw=0.9, color=GREY))
    o.append(T(188, 58, "Đế van / Seat", 8.0, anchor="start"))
    o.append(_line(318, 116, 388, 90, sw=0.9, color=GREY))
    o.append(T(428, 86, "Hơi chưa hòa tan / Undissolved vapor", 8.0,
               anchor="end", color=RED))
    o.append(_line(324, 244, 324, 262, sw=0.9, color=GREY))
    o.append(T(324, 272, "Tia nước + hơi / Water + vapor jet", 8.2, anchor="middle"))

    # Bilingual strip inside the SVG (present in both language pages).
    o.append(T(340, 300, "Hình 23-1 · Hóa hơi chất lỏng trong van điều khiển, không có dòng nghẽn",
               7.0, color=INK))
    o.append(T(340, 316, "Figure 23-1 · Liquid flashing in a control valve without choked flow",
               7.0, color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Sơ đồ hóa hơi chất lỏng ở cửa ra van")),
                "Hình 23-1 · Hóa hơi chất lỏng trong van điều khiển, không có dòng nghẽn.",
                "Figure 23-1 · Liquid flashing in a control valve without choked flow.",
                "Sơ đồ tia nước và hơi thoát ra từ cửa van, hơi hòa tan lại trong không khí",
                "Schematic water-and-vapor jet leaving a valve outlet, with vapor redissolving in air")
