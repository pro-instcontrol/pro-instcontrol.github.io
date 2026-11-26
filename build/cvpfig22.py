# -*- coding: utf-8 -*-
"""Vector redraws of the five figures in Baumann Chapter 22,
*Control Valve Primer*, 5th ed. -- "Graphical Estimation of Noise Produced
by Turbulence and Cavitation of Liquids".

Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` and is registered in
:data:`FIGS` through :func:`_reg`, following ``build/cvpfig19.py``.

Figures 22-1 and 22-2 are computed from logarithmic families read off the
printed graphs; Figure 22-3 uses computed turbulence and cavitation curves;
Figures 22-4 and 22-5 plot the printed data-point series explicitly.  All
axes, gridlines, legends, circled panel marks and bilingual caption strips
are genuine SVG primitives.  Text is escaped, with literal Unicode for
multiplication, subtraction and subscript characters; no CJK and no bare
'&' is emitted.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (GREY, INK, _circle, _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


def _num(v):
    """Format a number using the literal Unicode minus sign."""
    return str(v).replace("-", "\u2212")


def _frame(o, L, T, R, B, ymin, ymax, yticks, xticks, ylab, xlab, sub=None):
    """Plot frame, gridlines, ticks and axis titles; return (px, py) mappers."""
    pw, ph = R - L, B - T
    xlo, xhi = xticks[0][0], xticks[-1][0]

    def px(v):
        return L + (v - xlo) / (xhi - xlo) * pw

    def py(v):
        return B - (v - ymin) / (ymax - ymin) * ph

    o.append(_rect(L, T, pw, ph, fill="#fdfcf9", sw=1.1))
    for v in yticks:
        o.append(_line(L, py(v), R, py(v), sw=0.7, color="#ccd0d4"))
        o.append(_txt(L - 8, py(v) + 2.6, _num(v), 7.0,
                      anchor="end", color=GREY))
    for v, lab in xticks:
        o.append(_line(px(v), T, px(v), B, sw=0.6, color="#e0e2e5"))
        o.append(_txt(px(v), B + 14, lab, 7.0, color=GREY))
    if sub:
        for v, lab in sub:
            o.append(_txt(px(v), B + 28, lab, 6.5, color=GREY))
    o.append(_txt(L - 30, T - 8, ylab, 7.6, anchor="start", color=INK))
    o.append(_txt((L + R) / 2.0, B + 42, xlab, 7.6, color=INK))
    return px, py


def _minor_y(o, L, R, T, B, py, ymin, ymax, step, majors):
    """Fine horizontal gridlines between the labelled major ticks."""
    v = ymin + step
    while v < ymax:
        if all(abs(v - m) > 1e-6 for m in majors):
            o.append(_line(L, py(v), R, py(v), sw=0.4, color="#eceef0"))
        v += step


def _curve(o, fn, xlo, xhi, px, py, ymin, ymax, n=241, sw=1.35,
           color="#7a7f86", dash=""):
    """Sample fn over [xlo, xhi]; skip points outside the plotted y range."""
    pts = []
    for i in range(n):
        x = xlo + (xhi - xlo) * i / (n - 1.0)
        y = fn(x)
        if y is None or not (ymin - 0.02 <= y <= ymax + 0.02):
            continue
        pts.append((px(x), py(y)))
    if len(pts) > 1:
        o.append(_poly(pts, sw=sw, color=color, dash=dash))


def _mark(o, cx, cy, letter):
    """Circled A/B/C mark at the right edge of the plot."""
    o.append(_circle(cx, cy, 13, fill="#ffffff", sw=1.3, color=INK))
    o.append(_txt(cx, cy + 5, letter, 12, color=INK, weight="600"))


def _strip(o, vi, en):
    """Bilingual caption strip drawn inside the SVG."""
    o.append(_txt(340, 322, esc(vi), 7.3, color=INK))
    o.append(_txt(340, 336, esc(en), 7.3, color=GREY))


def _marker(o, cx, cy, shape, r=3.0, fill=INK, sw=1.0, color=None):
    """A data-point marker: square, diamond, triangle or dot."""
    color = color or fill
    if shape == "square":
        o.append(_rect(cx - r, cy - r, 2 * r, 2 * r,
                       fill=fill, sw=sw, stroke=color))
    elif shape == "diamond":
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        o.append(_poly(pts, fill=fill, sw=sw, color=color, close=True))
    elif shape == "triangle":
        pts = [(cx, cy - r), (cx + r * 0.9, cy + r * 0.8),
               (cx - r * 0.9, cy + r * 0.8)]
        o.append(_poly(pts, fill=fill, sw=sw, color=color, close=True))
    else:
        o.append(_circle(cx, cy, r, fill=fill, sw=sw, color=color))


def _series(o, xs, ys, px, py, color, shape, dash="", sw=1.3, r=3.0):
    """Connect a printed data series and draw each explicit data point."""
    o.append(_poly([(px(x), py(y)) for x, y in zip(xs, ys)],
                   sw=sw, color=color, dash=dash))
    for x, y in zip(xs, ys):
        _marker(o, px(x), py(y), shape, r=r, fill=color, sw=0.9)


def _legend(o, x, y, w, h, rows):
    """Legend box; rows are (label, colour, dash, marker shape or '')."""
    o.append(_rect(x, y, w, h, fill="#ffffff", sw=0.9, stroke=GREY))
    for i, (label, color, dash, shape) in enumerate(rows):
        yy = y + (i + 1) * h / (len(rows) + 1.0)
        o.append(_line(x + 7, yy, x + 25, yy, sw=1.2, dash=dash, color=color))
        if shape:
            _marker(o, x + 16, yy, shape, r=2.3, fill=color, sw=0.8)
        o.append(_txt(x + 29, yy + 2.6, esc(label), 6.8,
                      anchor="start", color=INK))


@_reg
def fig_f221():
    """Figure 22-1 -- Graph A: base level A from Cv per D squared."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Graph A · Base sound level from Cv / D² and pipe diameter"),
                  10.2, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("Seven families Cv = k × D²   ·   1 in = 25 mm"),
                  7.8, color=GREY))

    xt = [(d, str(d)) for d in range(0, 15, 2)]
    sub = [(d, str(25 * d)) for d in range(1, 15)]
    px, py = _frame(o, L, T, R, B, 10, 30,
                    [10, 15, 20, 25, 30], xt, "dB(A)",
                    "Downstream pipe diameter D, in  (1 in = 25 mm)", sub)
    _minor_y(o, L, R, T, B, py, 10, 30, 1, (10, 15, 20, 25, 30))

    # Logarithmic family read from the printed spacing: every doubling of
    # Cv / D² adds about 3.3 dB, and A grows as 10 log10(D).
    for k in (15, 10, 7, 5, 3, 2, 1):
        def f(D, k=k):
            return 10.0 * math.log10(D) + 11.0 * math.log10(k) + 2.0
        _curve(o, f, 0.2, 14.0, px, py, 10, 30, sw=1.3)

    for k in (15, 10, 7, 5, 3, 2, 1):
        a = 10.0 * math.log10(12.6) + 11.0 * math.log10(k) + 2.0
        o.append(_txt(px(13.4), py(a) - 4.0,
                      esc("Cv = %g×D²" % k), 7.2,
                      anchor="end", color=INK, weight="600"))

    _mark(o, 634, 151, "A")
    _strip(o,
           "Hình 22-1 · Đồ thị A: mức ồn cơ bản theo Cv / D² và đường kính ống.",
           "Figure 22-1 · Graph A: base level from Cv / D² and pipe diameter.")

    title = "Baumann Figure 22-1: Graph A, base level from Cv per D squared and pipe diameter"
    caption_vi = ("Hình 22-1 · Đồ thị A: mức ồn cơ bản theo Cv / D² "
                  "và đường kính ống.")
    caption_en = ("Figure 22-1 · Graph A: base level from Cv / D² "
                  "and pipe diameter.")
    aria_vi = (
        "Đồ thị A: mức ồn cơ bản từ 10 đến 30 dB(A) theo đường kính ống D "
        "từ 0 đến 14 inch, với thang phụ 25 đến 350 mm; bảy đường cong "
        "logarithmic ứng với Cv bằng 1, 2, 3, 5, 7, 10 và 15 nhân D bình "
        "phương, tăng nhanh rồi phẳng dần; có nhãn A được khoanh tròn ở bên phải.")
    aria_en = (
        "Graph A: base sound level from 10 to 30 dB(A) against downstream "
        "pipe diameter D from 0 to 14 in, with a secondary scale from 25 to "
        "350 mm; seven logarithmic curves for Cv = 1, 2, 3, 5, 7, 10 and 15 "
        "times D squared, rising steeply then flattening; circled A mark at "
        "the right edge.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f222():
    """Figure 22-2 -- Graph B: pressure factor from absolute inlet pressure."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Graph B · Sound level from absolute inlet pressure"),
                  10.5, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("B = 35 log10(P₁ psia) − 35   ·   example: 145 psia → 40.5 dBA"),
                  7.8, color=GREY))

    xt = [(p, str(p)) for p in range(0, 351, 50)]
    sub = [(i * 2.5 / 22.5 * 350.0, "%g" % (i * 2.5)) for i in range(10)]
    px, py = _frame(o, L, T, R, B, 0, 55,
                    list(range(0, 56, 5)), xt, "LP [dB(A)]",
                    "Absolute inlet pressure P₁, psia / bar(a)", sub)

    def fb(P):
        if P <= 0:
            return None
        return 35.0 * math.log10(P) - 35.0

    _curve(o, fb, 10.0, 350.0, px, py, 0, 55, n=241, sw=1.6, color=INK)

    mx, my = px(145.0), py(40.5)
    o.append(_line(L, my, mx, my, sw=0.8, dash="3,3", color=GREY))
    o.append(_line(mx, B, mx, my, sw=0.8, dash="3,3", color=GREY))
    o.append(_circle(mx, my, 3.5, fill=INK, sw=1.0, color="#ffffff"))

    o.append(_rect(344, 104, 150, 24, fill="#ffffff", sw=1.0, stroke=GREY))
    o.append(_line(354, 116, 372, 116, sw=1.5, color=INK))
    o.append(_txt(376, 119, esc("35 log(P₁ psia) − 35"), 7.5, color=INK))

    _mark(o, 634, 151, "B")
    _strip(o,
           "Hình 22-2 · Đồ thị B: mức ồn theo áp suất đầu vào tuyệt đối.",
           "Figure 22-2 · Graph B: sound level from absolute inlet pressure.")

    title = "Baumann Figure 22-2: Graph B, sound level from absolute inlet pressure"
    caption_vi = "Hình 22-2 · Đồ thị B: mức ồn theo áp suất đầu vào tuyệt đối."
    caption_en = "Figure 22-2 · Graph B: sound level from absolute inlet pressure."
    aria_vi = (
        "Đồ thị B: mức ồn LP từ 0 đến 55 dB(A) theo áp suất đầu vào tuyệt đối "
        "P₁ từ 0 đến 350 psia, thang phụ 0 đến 22,5 bar(a); một đường cong theo "
        "B = 35 log10(P₁ psia) − 35, có điểm đánh dấu tại 145 psia và 40,5 dBA, "
        "ô chú thích công thức và nhãn B được khoanh tròn ở bên phải.")
    aria_en = (
        "Graph B: sound level LP from 0 to 55 dB(A) against absolute inlet "
        "pressure P₁ from 0 to 350 psia, secondary scale 0 to 22.5 bar(a); "
        "one curve following B = 35 log10(P₁ psia) − 35, a marker at 145 psia "
        "and 40.5 dBA, a formula legend box and a circled B mark at the right "
        "edge.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f223():
    """Figure 22-3 -- turbulence and cavitation components of water noise."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Turbulence and cavitation components of water noise"),
                  10.4, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("Lx dBA versus 10X   ·   grey: turbulence, black: cavitation"),
                  7.8, color=GREY))

    xt = [(t, str(t)) for t in range(0, 11)]
    px, py = _frame(o, L, T, R, B, 0, 55,
                    list(range(0, 56, 5)), xt, "Lx dBA", "10X")
    _minor_y(o, L, R, T, B, py, 0, 55, 2.5, list(range(0, 56, 5)))

    def turb(t):
        if t <= 1.0:
            return None
        return 20.0 * (1.0 - math.exp(-(t - 1.0) / 1.35))

    _curve(o, turb, 1.0, 10.0, px, py, 0, 55,
           n=241, sw=1.4, color="#9a9a9a", dash="4,3")

    # Each cavitation curve rises to a peak, then falls back toward the
    # turbulence plateau; higher XFz means a lower peak.
    families = [
        (0.2, 1.8, 9.0, 6.0, 49.0),
        (0.3, 2.6, 10.0, 6.5, 40.0),
        (0.4, 3.6, 15.0, 7.0, 35.0),
        (0.5, 3.8, 18.0, 7.2, 30.0),
    ]
    end = 9.5

    def cav(t, t0=0.0, y0=0.0, tp=0.0, yp=0.0):
        if t < t0 or t > end:
            return None
        if t <= tp:
            u = (t - t0) / (tp - t0)
            return y0 + (yp - y0) * (u ** 0.85)
        u = (end - t) / (end - tp)
        return 20.0 + (yp - 20.0) * (u ** 1.1)

    for xfz, t0, y0, tp, yp in families:
        _curve(o, lambda t, t0=t0, y0=y0, tp=tp, yp=yp: cav(t, t0, y0, tp, yp),
               t0, end, px, py, 0, 55, n=241, sw=1.35, color=INK)

    for xfz, tx, ty in ((0.2, 2.3, 8.5), (0.3, 3.2, 11.0),
                        (0.4, 4.4, 14.0), (0.5, 5.2, 16.0)):
        o.append(_txt(px(tx), py(ty),
                      esc("X_Fz = %s" % _num(xfz)), 7.0,
                      anchor="end", color=INK, weight="600"))
    o.append(_txt(px(6.7), py(15.5), esc("For FL = 0.7"), 7.0,
                  anchor="start", color=INK))

    _legend(o, px(6.6), 47, 166, 32,
            [("Turbulence", "#9a9a9a", "4,3", ""),
             ("Cavitation", INK, "", "")])

    _mark(o, 634, 151, "C")
    _strip(o,
           "Hình 22-3 · Thành phần tiếng ồn do nhiễu loạn và xâm thực của nước.",
           "Figure 22-3 · Turbulence and cavitation sound components of water.")

    title = "Baumann Figure 22-3: turbulence and cavitation sound level components of water"
    caption_vi = ("Hình 22-3 · Thành phần tiếng ồn do nhiễu loạn và "
                  "xâm thực của nước.")
    caption_en = "Figure 22-3 · Turbulence and cavitation sound components of water."
    aria_vi = (
        "Đồ thị thành phần tiếng ồn Lx từ 0 đến 55 dBA theo 10X từ 0 đến 10: "
        "đường đứt nét màu xám tăng từ 1.0 lên khoảng 20 dBA; bốn đường đậm "
        "màu đen cho X_Fz bằng 0,2; 0,3; 0,4 và 0,5, đỉnh lần lượt khoảng "
        "49, 40, 35 và 30 dBA rồi giảm về 20 dBA; ghi chú For FL = 0.7, "
        "chú giải và nhãn C được khoanh tròn.")
    aria_en = (
        "Sound level components Lx from 0 to 55 dBA against 10X from 0 to 10: "
        "a grey dashed turbulence curve rising from 1.0 to about 20 dBA; "
        "four solid black cavitation curves for XFz = 0.2, 0.3, 0.4 and 0.5 "
        "peaking near 49, 40, 35 and 30 dBA before falling to about 20 dBA; "
        "labelled For FL = 0.7, with legend and a circled C mark.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f224():
    """Figure 22-4 -- printed test data for a 0.100 m rotary plug valve."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 14,
                  esc("Sound Levels of 0.100 m Rotary Plug Valve: Cv = 18, FL = 0.9, "
                      "Fd = 0.25, P1 = 1000 kPa"),
                  8.9, color=INK, weight="600"))
    o.append(_txt(340, 30,
                  esc("Test data, calculated data and turbulent trend"),
                  7.6, color=GREY))

    xt = [(t, str(t)) for t in range(1, 11)]
    px, py = _frame(o, L, T, R, B, 0, 120,
                    list(range(0, 121, 20)), xt, "Sound Level in dB(A)", "X × 10")
    _minor_y(o, L, R, T, B, py, 0, 120, 10, list(range(0, 121, 20)))

    xs = list(range(1, 11))
    test = [59, 63, 66, 78, 93, 92, 86, 84, 80, 79]
    calc = [60, 63, 66, 88, 92, 98, 88, 85, 83, 79]
    turb = [58, 62, 66, 70, 72, 73, 74, 76, 78, 80]

    _series(o, xs, turb, px, py, INK, "triangle", dash="1,2.5", sw=1.3, r=2.9)
    _series(o, xs, test, px, py, "#9a9a9a", "diamond", sw=1.2, r=3.1)
    _series(o, xs, calc, px, py, INK, "square", sw=1.4, r=2.8)

    _legend(o, 455, 176, 135, 52,
            [("Test Data", "#9a9a9a", "", "diamond"),
             ("Calculated Data", INK, "", "square"),
             ("Turbulent Trend", INK, "1,2.5", "triangle")])

    _strip(o,
           "Hình 22-4 · Số liệu thử nghiệm và tính toán của van cắm quay 4 inch.",
           "Figure 22-4 · Test and calculated data for a 4-inch rotary plug valve.")

    title = ("Baumann Figure 22-4: test data of a 4-inch rotary plug valve, "
             "Cv 18, FL 0.9")
    caption_vi = ("Hình 22-4 · Số liệu thử nghiệm và tính toán của "
                  "van cắm quay 4 inch.")
    caption_en = "Figure 22-4 · Test and calculated data for a 4-inch rotary plug valve."
    aria_vi = (
        "Biểu đồ mức ồn từ 0 đến 120 dB(A) theo X nhân 10 từ 1 đến 10 cho van "
        "cắm quay 0,100 m: Cv bằng 18, FL bằng 0,9, Fd bằng 0,25, P1 bằng "
        "1000 kPa. Ba chuỗi điểm: số liệu thử nghiệm hình thoi màu xám, số liệu "
        "tính toán hình vuông màu đen và xu hướng nhiễu loạn hình tam giác màu đen "
        "tăng chậm; chú giải ở góc dưới bên phải.")
    aria_en = (
        "Sound level from 0 to 120 dB(A) against X times 10 from 1 to 10 for "
        "a 0.100 m rotary plug valve: Cv = 18, FL = 0.9, Fd = 0.25, "
        "P1 = 1000 kPa. Three explicit point series: grey diamond test data, "
        "black square calculated data and slowly rising black triangle "
        "turbulent trend; legend at the lower right.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f225():
    """Figure 22-5 -- printed data for multi-stage noise reducing trim."""
    w, h = 680, 360
    L, T, R, B = 74, 46, 600, 258
    o = []

    o.append(_txt(340, 12,
                  esc('3" Globe Valve with Multi-Stage Noise Reducing Trim'),
                  9.8, color=INK, weight="600"))
    o.append(_txt(340, 27,
                  esc("FL last stage = 0.8, P1 = 480 psig, Cv = 13. Area ratio = 4:1."),
                  8.4, color=GREY))

    xt = [(t, str(t)) for t in range(1, 10)]
    px, py = _frame(o, L, T, R, B, 0, 70,
                    list(range(0, 71, 10)), xt, "Sound Level in dB(A)",
                    "Pressure Ratio X × 10")
    _minor_y(o, L, R, T, B, py, 0, 70, 5, list(range(0, 71, 10)))

    xs = list(range(1, 10))
    s1 = [39, 50, 52, 56, 59, 61, 63, 65, 65]
    s2 = [37, 43, 50, 56, 59, 61, 64, 64, 64]

    _series(o, xs, s2, px, py, "#9a9a9a", "diamond", dash="2,2", sw=1.1, r=2.8)
    _series(o, xs, s1, px, py, INK, "square", sw=1.4, r=2.8)

    o.append(_line(px(4.2), py(37), px(4.7), py(37),
                   sw=0.9, dash="2,2", color=GREY))
    o.append(_txt(px(4.8), py(37) + 2.6, esc("est"), 6.4,
                  anchor="start", color=GREY))

    _legend(o, 470, 178, 120, 44,
            [("Series 2", "#9a9a9a", "2,2", "diamond"),
             ("Series 1", INK, "", "square")])

    _strip(o,
           "Hình 22-5 · Số liệu thử nghiệm van cầu 3 inch có van lọc nhiều tầng.",
           "Figure 22-5 · Test data for a 3-inch globe valve with multi-stage trim.")

    title = ("Baumann Figure 22-5: 3-inch globe valve with multi-stage "
             "noise reducing trim test data")
    caption_vi = ("Hình 22-5 · Số liệu thử nghiệm van cầu 3 inch có "
                  "van lọc nhiều tầng.")
    caption_en = ("Figure 22-5 · Test data for a 3-inch globe valve with "
                  "multi-stage trim.")
    aria_vi = (
        "Biểu đồ mức ồn từ 0 đến 70 dB(A) theo tỉ lệ áp suất X nhân 10 từ 1 đến "
        "9 cho van cầu 3 inch có van lọc giảm ồn nhiều tầng: FL tầng cuối bằng 0,8, "
        "P1 bằng 480 psig, Cv bằng 13, tỉ lệ diện tích 4:1. Hai chuỗi điểm: Series 1 "
        "hình vuông đậm tăng từ 39 lên 65 dBA và Series 2 hình thoi xám đứt nét "
        "tăng từ 37 lên 64 dBA; chú giải ở góc dưới bên phải.")
    aria_en = (
        "Sound level from 0 to 70 dB(A) against pressure ratio X times 10 from "
        "1 to 9 for a 3-inch globe valve with multi-stage noise reducing trim: "
        "FL of last stage = 0.8, P1 = 480 psig, Cv = 13, area ratio 4:1. Two "
        "explicit point series: Series 1 black squares rising from 39 to 65 dBA "
        "and Series 2 grey dotted diamonds rising from 37 to 64 dBA; legend at "
        "the lower right.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)
