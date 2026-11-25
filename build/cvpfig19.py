# -*- coding: utf-8 -*-
"""Vector redraws of printed Graphs A, B and C in Baumann Chapter 19,
*Control Valve Primer*, 5th ed. — "The Graphical ABC Method for Gases".

Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` and is registered in
:data:`FIGS` through :func:`_reg`, mirroring ``build/cvpfig18.py``.

All curves are computed from the printed equations, never approximated with
straight lines::

    A = 25 log10(D) − 10 + 20 log10(Cv/D²)     (Graph A, seven Cv/D² curves)
    B = 35 log10(P₁ psia) − 35                 (Graph B, one curve)
    C = 27 + 30 log10(10X) + 20 log10(Fd)      (Graph C, six Fd curves)

Dual-unit axes, gridlines, curve labels, circled A/B/C marks and bilingual
bottom caption strips are genuine SVG primitives (no raster).  All text is
escaped; × and − are literal Unicode; no CJK and no bare '&' is emitted.
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
    """Format a number using the literal Unicode minus sign U+2212."""
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


def _curve(o, fn, xlo, xhi, px, py, ymin, ymax, n=241, sw=1.35, color="#7a7f86"):
    """Sample fn over [xlo, xhi]; skip points outside the plotted y range."""
    pts = []
    for i in range(n):
        x = xlo + (xhi - xlo) * i / (n - 1.0)
        y = fn(x)
        if y is None or not (ymin - 0.02 <= y <= ymax + 0.02):
            continue
        pts.append((px(x), py(y)))
    if len(pts) > 1:
        o.append(_poly(pts, sw=sw, color=color))


def _mark(o, cx, cy, letter):
    """Circled A/B/C mark at the right edge of the plot."""
    o.append(_circle(cx, cy, 13, fill="#ffffff", sw=1.3, color=INK))
    o.append(_txt(cx, cy + 5, letter, 12, color=INK, weight="600"))


def _strip(o, vi, en):
    """Bilingual caption strip drawn inside the SVG."""
    o.append(_txt(340, 322, esc(vi), 7.3, color=INK))
    o.append(_txt(340, 336, esc(en), 7.3, color=GREY))


@_reg
def fig_f191():
    """Figure 19-1 — Graph A: seven Cv/D² curves against pipe diameter."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Graph A · Sound level from Cv and pipe diameter"),
                  10.5, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("A = 25 log10(D) − 10 + 20 log10(Cv/D²)"),
                  7.8, color=GREY))

    xt = [(d, str(d)) for d in range(2, 19, 2)]
    sub = [(d, str(d * 25)) for d in range(2, 19, 2)]  # 1 in = 25 mm
    px, py = _frame(o, L, T, R, B, -10, 45,
                    list(range(-10, 46, 5)), xt, "dB(A)",
                    "Pipe diameter D, in  (1 in = 25 mm)", sub)

    for k in (15, 10, 5, 3.5, 2, 1, 0.5):
        def f(D, k=k):
            return 25.0 * math.log10(D) - 10.0 + 20.0 * math.log10(k)
        _curve(o, f, 2.0, 18.0, px, py, -10, 45)

    # labels at D = 11; the 5 and 3.5 curves are only ~12 px apart, so nudge
    labs = [(15, 0), (10, 0), (5, -3), (3.5, 3), (2, 0), (1, 0), (0.5, 0)]
    for k, dy in labs:
        a = 25.0 * math.log10(11.0) - 10.0 + 20.0 * math.log10(k)
        o.append(_txt(px(11.0), py(a) - 4 + dy,
                      esc("Cv = %s×D²" % _num(k)), 7.2,
                      color=INK, weight="600"))

    _mark(o, 634, 151, "A")
    _strip(o,
           "Hình 19-1 · Đồ thị A. Lưu ý: inch = 0,04 × mm.",
           "Figure 19-1 · Graph A. Note: Inch = 0.04 × mm.")

    title = "Baumann Figure 19-1: Graph A, sound level from Cv and pipe diameter"
    caption_vi = "Hình 19-1 · Đồ thị A. Lưu ý: inch = 0,04 × mm."
    caption_en = "Figure 19-1 · Graph A. Note: Inch = 0.04 × mm."
    aria_vi = (
        "Đồ thị A: mức ồn dB(A) theo đường kính ống D từ 2 đến 18 inch, "
        "với bảy đường cong Cv bằng 15, 10, 5, 3,5, 2, 1 và 0,5 nhân D bình "
        "phương; công thức A = 25 log10(D) − 10 + 20 log10(Cv/D²); "
        "thang phụ tính bằng mm với 1 inch bằng 25 mm (25 đến 450 mm); "
        "có nhãn A được khoanh tròn ở bên phải.")
    aria_en = (
        "Graph A: sound level in dB(A) from −10 to 45 plotted against pipe "
        "diameter D from 2 to 18 in, with seven curves for Cv = 15, 10, 5, "
        "3.5, 2, 1 and 0.5 times D squared; formula A = 25 log10(D) − 10 + "
        "20 log10(Cv/D²); secondary millimetre scale from 25 to 450 mm "
        "(1 in = 25 mm); circled A mark at the right edge.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f192():
    """Figure 19-2 — Graph B: sound level from inlet pressure."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Graph B · Sound level from inlet pressure"),
                  10.5, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("B = 35 log10(P₁ psia) − 35"),
                  7.8, color=GREY))

    xt = [(p, str(p)) for p in range(0, 351, 50)]
    sub = [(i * 2.5 / 22.5 * 350.0, "%g" % (i * 2.5)) for i in range(10)]
    px, py = _frame(o, L, T, R, B, 0, 55,
                    list(range(0, 56, 5)), xt, "dB(A)",
                    "Inlet pressure P₁, psia / bar(a)", sub)

    def fb(P):
        if P <= 0:
            return None
        return 35.0 * math.log10(P) - 35.0

    _curve(o, fb, 10.0, 350.0, px, py, 0, 55, n=241, sw=1.6, color=INK)

    # small legend box, set below the curve so it does not mask it
    o.append(_rect(300, 104, 150, 24, fill="#ffffff", sw=1.0, stroke=GREY))
    o.append(_txt(375, 119, esc("B = 35 log(P₁ psia) − 35"), 7.6, color=INK))

    _mark(o, 634, 151, "B")
    _strip(o,
           "Hình 19-2 · Đồ thị B.",
           "Figure 19-2 · Graph B.")

    title = "Baumann Figure 19-2: Graph B, sound level from inlet pressure"
    caption_vi = "Hình 19-2 · Đồ thị B."
    caption_en = "Figure 19-2 · Graph B."
    aria_vi = (
        "Đồ thị B: mức ồn dB(A) từ 0 đến 55 theo áp suất đầu vào P₁ từ 0 đến "
        "350 psia (thang phụ 0 đến 22,5 bar(a)); một đường cong duy nhất theo "
        "công thức B = 35 log10(P₁ psia) − 35, có ô chú thích công thức và "
        "nhãn B được khoanh tròn ở bên phải.")
    aria_en = (
        "Graph B: sound level in dB(A) from 0 to 55 plotted against inlet "
        "pressure P₁ from 0 to 350 psia (secondary scale 0 to 22.5 bar(a)); "
        "a single curve following B = 35 log10(P₁ psia) − 35, with a small "
        "legend box carrying the formula and a circled B mark at the right "
        "edge.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f193():
    """Figure 19-3 — Graph C: six Fd curves against 10X."""
    w, h = 680, 360
    L, T, R, B = 74, 44, 600, 258
    o = []

    o.append(_txt(340, 15,
                  esc("Graph C · Sound level from pressure drop and Fd"),
                  10.5, color=INK, weight="600"))
    o.append(_txt(340, 32,
                  esc("C = 27 + 30 log10(10X) + 20 log10(Fd)   ·   "
                      "10X = 10(P₁ − P₂)/P₁"),
                  7.8, color=GREY))

    xt = [(t, str(t)) for t in range(0, 11)]
    px, py = _frame(o, L, T, R, B, 0, 60,
                    list(range(0, 61, 5)), xt, "dB(A)",
                    "10X, pressure-drop ratio")

    for fd in (1.0, 0.5, 0.2, 0.1, 0.07, 0.01):
        def f(t, fd=fd):
            return 27.0 + 30.0 * math.log10(t) + 20.0 * math.log10(fd)
        _curve(o, f, 0.1, 10.0, px, py, 0, 60)

    # staggered label positions keep the six curves' labels clear of each other
    labs = [(1.0, 2.5, -4), (0.5, 3.0, -1), (0.2, 3.5, -4),
            (0.1, 4.0, -4), (0.07, 3.0, -4), (0.01, 5.0, -4)]
    for fd, t, dy in labs:
        c = 27.0 + 30.0 * math.log10(t) + 20.0 * math.log10(fd)
        o.append(_txt(px(t), py(c) + dy,
                      esc("Fd = %s" % _num(fd)), 7.2,
                      color=INK, weight="600"))

    _mark(o, 634, 151, "C")
    _strip(o,
           "Hình 19-3 · Đồ thị C.",
           "Figure 19-3 · Graph C.")

    title = "Baumann Figure 19-3: Graph C, sound level from pressure drop and Fd"
    caption_vi = "Hình 19-3 · Đồ thị C."
    caption_en = "Figure 19-3 · Graph C."
    aria_vi = (
        "Đồ thị C: mức ồn dB(A) từ 0 đến 60 theo 10X từ 0 đến 10, với sáu "
        "đường cong ứng với Fd bằng 1,0; 0,5; 0,2; 0,1; 0,07 và 0,01; "
        "công thức C = 27 + 30 log10(10X) + 20 log10(Fd), trong đó "
        "X = (P₁ − P₂)/P₁; có nhãn C được khoanh tròn ở bên phải.")
    aria_en = (
        "Graph C: sound level in dB(A) from 0 to 60 plotted against 10X from "
        "0 to 10, with six curves for Fd = 1.0, 0.5, 0.2, 0.1, 0.07 and "
        "0.01; formula C = 27 + 30 log10(10X) + 20 log10(Fd), where "
        "X = (P₁ − P₂)/P₁; circled C mark at the right edge.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)
