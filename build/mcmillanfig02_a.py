# -*- coding: utf-8 -*-
"""Vector redraw of Figure 2.1 in A. McMillan, *Electrical Installations in
Hazardous Areas*, Chapter 2 "Area classification".

Fig. 2.1 is the "Typical ignition characteristics" chart: ignition energy
(mJ, logarithmic ordinate) against percentage gas in air, with the narrow
propane U-curve (minimum a = 260 uJ) and the broad hydrogen U-curve
(minimum b = 20 uJ), followed by a small explosive-limit table.

Simplified bilingual VI/EN SVG vector; no raster art is used. Architecture
mirrors `mcmillanfig01_a.py`: the function returns the standard five-tuple
through `vfig._fig()` and is registered in `FIGS` by the `_reg` decorator.
"""
import sys
import os
import math

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, PAPER, _arrow, _circle, _defs, _fig,
                  _line, _poly, _rect, _txt, svg)

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
    """Figure 2.1 - Typical ignition characteristics."""
    w, h = 680, 470
    o = [_defs()]
    o.append(_rect(0, 0, w, h, fill=PAPER, sw=0))

    # Headings.
    o.append(T(340, 20,
               "Hình 2.1 · Đặc tính đánh lửa điển hình / "
               "Figure 2.1 · Typical ignition characteristics",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34,
               "Năng lượng đánh lửa nhỏ nhất tại các điểm a và b / "
               "Minimum ignition energy at points a and b",
               6.8, color=GREY))

    # Plot geometry.  The ordinate is log10(energy in mJ) from -2 to +1,
    # i.e. 0.01 to 10 mJ; the abscissa is 0-100 percent gas in air.
    x0, ytop, W, Hplot = 92.0, 58.0, 524.0, 226.0
    ybot = ytop + Hplot

    def X(p):
        return x0 + p / 100.0 * W

    def Y(loge):
        return ytop + (1.0 - loge) / 3.0 * Hplot

    o.append(T(x0, 46, "Ignition energy (mJ) / Năng lượng đánh lửa (mJ)",
               7.6, anchor="start", color=GREY))

    # Decade grid and tick labels.
    for le, lab in ((1.0, "10"), (0.0, "1"), (-1.0, "0.1"), (-2.0, "0.01")):
        yy = Y(le)
        o.append(_line(x0, yy, x0 + W, yy, sw=0.6, dash="3 3",
                       color="#d7d2c6"))
        o.append(_line(x0 - 4, yy, x0, yy, sw=0.9, color=INK))
        o.append(T(x0 - 8, yy + 2.4, lab, 7.0, anchor="end", color=GREY))

    # Axes: horizontal 0-100, vertical 0.01-10 mJ (logarithmic).
    o.append(_line(x0, ybot, x0 + W + 8, ybot, sw=1.2, color=INK))
    o.append(_line(x0, ybot, x0, ytop - 6, sw=1.2, color=INK))
    for p in range(0, 101, 10):
        xx = X(p)
        major = (p % 20 == 0)
        o.append(_line(xx, ybot, xx, ybot + (4 if major else 2),
                       sw=0.9 if major else 0.6, color=INK))
        if major:
            o.append(T(xx, ybot + 14, str(p), 7.0, color=GREY))
    o.append(T(x0 + W / 2, ybot + 30,
               "Percentage gas in air / Phần trăm khí trong không khí",
               7.8, color=INK))

    def curve(L, U, pmin, emin, rise, exp, color):
        """U-shaped ignition-energy curve in log-energy space."""
        lemin = math.log10(emin)
        pts = []
        n = 260
        for i in range(n + 1):
            p = L + (U - L) * i / n
            if p <= pmin:
                t = (pmin - p) / (pmin - L)
            else:
                t = (p - pmin) / (U - pmin)
            le = lemin + rise * (t ** exp)
            if le > 1.0:            # above 10 mJ: outside the plotted range
                continue
            pts.append((X(p), Y(le)))
        return _poly(pts, fill="none", sw=1.9, color=color)

    # Broad hydrogen U (4.1-74.2 %, minimum 0.02 mJ near point b).
    o.append(curve(4.1, 74.2, 25.0, 0.02, 2.70, 1.6, BLUE))
    # Narrow propane U (about 2-9 %, minimum 0.26 mJ near point a).
    o.append(curve(2.1, 9.5, 5.5, 0.26, 2.00, 1.6, INK))

    # Curve labels: Vietnamese first, English in parentheses.
    o.append(T(140, 88, "Propan (Propane)", 7.4,
               anchor="start", color=INK, weight="600"))
    o.append(T(492, 94, "Hydro (Hydrogen)", 7.4,
               anchor="start", color=BLUE, weight="600"))

    # Marked minima a and b.
    xa, ya = X(5.5), Y(math.log10(0.26))
    xb, yb = X(25.0), Y(math.log10(0.02))
    o.append(_circle(xa, ya, 2.6, fill=INK, sw=0.8, color=PAPER))
    o.append(T(xa - 9, ya + 2, "a", 7.6, anchor="end",
               color=INK, weight="600"))
    o.append(_circle(xb, yb, 2.6, fill=BLUE, sw=0.8, color=PAPER))
    o.append(T(xb + 9, yb + 3, "b", 7.6, anchor="start",
               color=BLUE, weight="600"))

    # Explosive-limit table.
    tx0, ty0, tw, th = 150.0, 334.0, 380.0, 76.0
    o.append(_rect(tx0, ty0, tw, th, fill=PAPER, sw=1.0, stroke=GREY))
    o.append(_line(270, ty0, 270, ty0 + th, sw=0.8, color=GREY))
    o.append(_line(400, ty0, 400, ty0 + th, sw=0.8, color=GREY))
    o.append(_line(tx0, ty0 + 34, tx0 + tw, ty0 + 34, sw=0.9, color=GREY))
    o.append(_line(tx0, ty0 + 55, tx0 + tw, ty0 + 55, sw=0.7, color=GREY))
    o.append(T(210, ty0 + 14, "Khí / Gas", 7.6, color=INK, weight="600"))
    o.append(T(335, ty0 + 13, "Giới hạn nổ dưới (%)", 7.0,
               color=INK, weight="600"))
    o.append(T(335, ty0 + 25, "Lower explosive limit (%)", 7.0, color=GREY))
    o.append(T(465, ty0 + 13, "Giới hạn nổ trên (%)", 7.0,
               color=INK, weight="600"))
    o.append(T(465, ty0 + 25, "Upper explosive limit (%)", 7.0, color=GREY))
    o.append(T(210, ty0 + 48, "Hydro / Hydrogen", 7.4, color=INK))
    o.append(T(335, ty0 + 48, "4.1", 7.6, color=BLUE, weight="600"))
    o.append(T(465, ty0 + 48, "74.2", 7.6, color=BLUE, weight="600"))
    o.append(T(210, ty0 + 69, "Propan / Propane", 7.4, color=INK))
    o.append(T(335, ty0 + 69, "2.1", 7.6, color=INK, weight="600"))
    o.append(T(465, ty0 + 69, "9.5", 7.6, color=INK, weight="600"))

    o.append(T(340, ty0 + 90, "Min. ignition energy a = 260 µJ, b = 20 µJ",
               7.6, color=INK))
    o.append(T(340, 452,
               "Hình 2.1 · Đặc tính đánh lửa điển hình / "
               "Figure 2.1 · Typical ignition characteristics",
               7.0, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Đồ thị năng lượng đánh lửa theo phần trăm khí trong không khí "
                        "với đường propan hẹp và đường hydro rộng, có các điểm a và b "
                        "và bảng giới hạn nổ")),
                "Hình 2-1 · Đặc tính đánh lửa điển hình.",
                "Figure 2-1 · Typical ignition characteristics.",
                "Đồ thị năng lượng đánh lửa theo phần trăm khí trong không khí với hai "
                "đường hình chữ U cho propan và hydro; điểm a 260 µJ, điểm b 20 µJ; "
                "bảng giới hạn nổ dưới và trên.",
                "Ignition-energy versus percent-gas-in-air chart with U-shaped propane "
                "and hydrogen curves, point a 260 µJ, point b 20 µJ, and lower/upper "
                "explosive-limit table.")
