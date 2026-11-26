# -*- coding: utf-8 -*-
"""Vector redraw of Figure 2-1 in R. STAHL, *Basics of Explosion
Protection* -- the Fire Triangle (printed A4).

The printed triangle shows green Fuel at the apex, blue Oxygen at the
lower left, yellow Ignition at the lower right, and a red Combustion
disc where the three elements overlap. Redrawn as SVG with bilingual
VI/EN labels, never as raster art. Architecture mirrors `cvpfig26.py`.
"""
from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _circle, _defs, _fig,
                  _poly, _txt, svg)

YELLOW = "#f4d03f"

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
def fig_f201():
    """Figure 2-1 -- the Fire Triangle: fuel, oxygen, ignition, combustion."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 18,
               "Tam giác lửa / Fire Triangle — Nhiên liệu, Oxy, Nguồn đánh lửa / Fuel, Oxygen, Ignition",
               9.4, color=INK, weight="600"))

    # Triangle vertices and midpoints.
    apex = (340, 64)
    left = (190, 332)
    right = (490, 332)
    mid_l = (265, 198)
    mid_r = (415, 198)
    mid_b = (340, 332)

    # Three coloured corners of the triangle.
    o.append(_poly([apex, mid_l, mid_r], fill=GREEN, sw=1.2, close=True))
    o.append(_poly([left, mid_l, mid_b], fill=BLUE, sw=1.2, close=True))
    o.append(_poly([right, mid_r, mid_b], fill=YELLOW, sw=1.2, close=True))
    o.append(_poly([mid_l, mid_r, mid_b], fill=PAPER, sw=0.8, close=True))

    # Red combustion overlap disc.
    o.append(_circle(340, 250, 74, fill=RED, sw=1.4))

    # Bilingual corner labels (white on the coloured fields).
    o.append(T(340, 138, "Nhiên liệu", 11.0, color="#ffffff", weight="600"))
    o.append(T(340, 153, "Fuel", 11.0, color="#ffffff", weight="600"))
    o.append(T(230, 312, "Oxy", 9.0, color="#ffffff", weight="600"))
    o.append(T(230, 326, "Oxygen", 9.0, color="#ffffff", weight="600"))
    o.append(T(450, 312, "Đánh lửa", 9.0, color=INK, weight="600"))
    o.append(T(450, 326, "Ignition", 9.0, color=INK, weight="600"))

    # Centre label.
    o.append(T(340, 245, "Cháy", 13.0, color="#ffffff", weight="600"))
    o.append(T(340, 262, "Combustion", 13.0, color="#ffffff", weight="600"))

    # Explosive-limit note reproduced from the printed page.
    o.append(T(340, 360,
               "LEL / UEL — Giới hạn cháy dưới / trên · Lower / Upper Explosive Limit",
               7.2, color=GREY))

    # Bilingual caption strip inside the SVG.
    o.append(T(340, 384,
               "Hình 2-1 · Tam giác lửa / Figure 2-1 · Fire Triangle",
               7.2, color=INK))
    o.append(T(340, 402,
               "Nhiên liệu + Oxy + Nguồn đánh lửa = Cháy / Fuel + Oxygen + Ignition = Combustion",
               6.6, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Tam giác lửa với nhiên liệu màu xanh lá, oxy màu xanh dương, nguồn đánh lửa màu vàng và vùng cháy màu đỏ")),
                "Hình 2-1 · Tam giác lửa gồm nhiên liệu (xanh lá), oxy (xanh dương), nguồn đánh lửa (vàng); vùng cháy (đỏ) là sự chồng lấp của ba yếu tố",
                "Figure 2-1 · The Fire Triangle: green Fuel, blue Oxygen and yellow Ignition, with the red Combustion disc where the three elements overlap",
                "Tam giác lửa với đỉnh nhiên liệu màu xanh lá, góc trái oxy màu xanh dương, góc phải nguồn đánh lửa màu vàng và đĩa cháy màu đỏ ở giữa",
                "Fire triangle with green fuel at the apex, blue oxygen at lower left, yellow ignition at lower right and a red combustion disc in the overlap")
