# -*- coding: utf-8 -*-
"""Shared vector-figure helpers for PPIC Chapter 5 (thorium/uranium HTRs).

Mirrors `ppicfig4_common.py` but numbers captions and the bottom strip as
``5.n``. Figure supplier modules import these helpers and register their
evaluated 5-tuples in a local registry via ``make_registry()``.
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

W, H = 680, 330


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
    """Close a figure with a bilingual 5.n strip and build the 5-tuple."""
    o.append(T(W / 2.0, h - 6, "Hình 5.%d   ·   Figure 5.%d" % (n, n),
               6.6, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 5.%d · %s" % (n, cvi),
        "Figure 5.%d · %s" % (n, cen),
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


def _frame(x0, y0, w, h, xr, yr, xt, yt, xlab, ylab):
    """Axes box, grid, ticks and titles; returns (markup, mx, my)."""
    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * w

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
    o.append(T(x0 + w / 2.0, y0 + h + 22, xlab, 7.4, color=INK))
    o.append('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
             'style="font:7.4px Inter,Helvetica,sans-serif;fill:%s">%s</text>'
             % (x0 - 31, y0 + h / 2.0, x0 - 31, y0 + h / 2.0, INK, esc(ylab)))
    return "".join(o), mx, my


def _series(points, mx, my, color, dot=1.9, dash="", fill="none"):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=1.7, color=color, dash=dash, fill=fill)]
    for px, py in pts:
        o.append(_circle(px, py, dot, fill=color, sw=0))
    return "".join(o)


def _legend(items, x, y, w=92, lh=13, size=7.0):
    h = 11 + len(items) * lh
    o = [_rect(x, y, w, h, fill="#ffffff", sw=0.9)]
    for i, (col, lab) in enumerate(items):
        yy = y + 13 + i * lh
        o.append(_line(x + 5, yy - 2, x + 20, yy - 2, sw=2.0, color=col))
        o.append(T(x + 24, yy, lab, size, anchor="start"))
    return "".join(o)


def _tri_membership(x0, x1, peak, color, y0, y1, label, dashed=False):
    """A triangular fuzzy membership function with a label."""
    o = [_poly([(x0, y1), (peak, y0), (x1, y1)], sw=1.4, color=color,
               dash="4 3" if dashed else "", fill="none")]
    o.append(T(peak, (y0 + y1) / 2.0 - 8, label, 7.0, color=color))
    return "".join(o)
