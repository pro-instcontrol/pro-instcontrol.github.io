# -*- coding: utf-8 -*-
"""Shared vector-figure helpers for PPIC Chapter 9 (predictive maintenance).

Mirrors `ppicfig8_common.py` but numbers captions and bottom strips as ``9.n``
on a 680 x 300 canvas. Supplier modules register evaluated 5-tuples in a
local registry via ``make_registry()``.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path,
                  _poly, _rect, _txt, svg)

W, H = 680, 300


def make_registry():
    """Return (FIGS, _reg) for one figure supplier module."""
    figs = {}

    def _reg(f):
        figs[f.__name__] = f()
        return f

    return figs, _reg


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.0, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _mk(n, o, title, cvi, cen, avi, aen, h=H):
    """Close a figure with a bilingual 9.n strip and build the 5-tuple."""
    o.append(T(W / 2.0, h - 5, "Hình 9.%d   ·   Figure 9.%d" % (n, n),
               6.4, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 9.%d · %s" % (n, cvi),
        "Figure 9.%d · %s" % (n, cen),
        avi, aen)


def _b(x, y, w, h, label, fill="#eef3fb", size=7.8, color=INK):
    """A compact labelled block; ``\n`` starts a new line."""
    lines = str(label).split("\n")
    o = [_rect(x, y, w, h, fill)]
    y0 = y + h / 2.0 - (len(lines) - 1) * size * 0.55 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * size * 1.15, ln, size, color=color))
    return "".join(o)


def _ar(x1, y1, x2, y2, color=BLUE, sw=1.6):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color)


def _frame(x0, y0, w, h, xr, yr, xt, yt, xlab, ylab, logy=False):
    """Axes box, grid, ticks and titles; returns (markup, mx, my)."""
    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * w

    if logy:
        la, lb = math.log10(yr[0]), math.log10(yr[1])

        def my(v):
            return y0 + h - (math.log10(v) - la) / (lb - la) * h
    else:
        def my(v):
            return y0 + h - (v - yr[0]) / (yr[1] - yr[0]) * h

    o = [_rect(x0, y0, w, h, fill="#fbfaf7", sw=1.0)]
    for v, lab in yt:
        py = my(v)
        o.append(_line(x0, py, x0 + w, py, sw=0.5, color="#dcdcdc"))
        o.append(_line(x0 - 3, py, x0, py, sw=0.7))
        o.append(T(x0 - 6, py + 2.3, lab, 6.4, anchor="end", color=GREY))
    for v, lab in xt:
        px = mx(v)
        o.append(_line(px, y0 + h, px, y0 + h + 3, sw=0.7))
        o.append(T(px, y0 + h + 11, lab, 6.4, color=GREY))
    o.append(T(x0 + w / 2.0, y0 + h + 23, xlab, 7.4, color=INK))
    o.append('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
             'style="font:7.4px Inter,Helvetica,sans-serif;fill:%s">%s</text>'
             % (x0 - 30, y0 + h / 2.0, x0 - 30, y0 + h / 2.0, INK, esc(ylab)))
    return "".join(o), mx, my


def _series(points, mx, my, color, dot=1.9, dash=""):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=1.7, color=color, dash=dash)]
    for px, py in pts:
        o.append(_circle(px, py, dot, fill=color, sw=0))
    return "".join(o)


def _legend(items, x, y, w=76, lh=13, size=7.0):
    h = 11 + len(items) * lh
    o = [_rect(x, y, w, h, fill="#ffffff", sw=0.9)]
    for i, (col, lab) in enumerate(items):
        yy = y + 13 + i * lh
        o.append(_line(x + 5, yy - 2, x + 20, yy - 2, sw=2.0, color=col))
        o.append(T(x + 24, yy, lab, size, anchor="start"))
    return "".join(o)


def _wavey(x, y0, amp, n, step=9, phase=0):
    """A small corrugation/coil line, useful in mechanical cross-sections."""
    return [(x + i * step, y0 + (amp if i % 2 else -amp) * (1 if phase == 0 else -1))
            for i in range(n + 1)]
