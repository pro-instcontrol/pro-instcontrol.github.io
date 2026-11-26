# -*- coding: utf-8 -*-
"""Shared vector-figure helpers for PPIC Chapter 11 (adaptive power control).

Default canvas 680 x 360; the six-panel simulation figures pass ``h=520``.
Captions and bottom strips are numbered ``11.n``.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path,
                  _poly, _rect, _txt, svg)

W, H = 680, 360


def make_registry():
    """Return (FIGS, _reg) for one figure supplier module."""
    figs = {}

    def _reg(f):
        figs[f.__name__] = f()
        return f

    return figs, _reg


def esc(s):
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.0, **kw):
    return _txt(x, y, esc(s), size=size, **kw)


def _mk(n, o, title, cvi, cen, avi, aen, h=H):
    o.append(T(W / 2.0, h - 5, "Hình 11.%d   ·   Figure 11.%d" % (n, n),
               6.4, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 11.%d · %s" % (n, cvi),
        "Figure 11.%d · %s" % (n, cen),
        avi, aen)


def _b(x, y, w, h, label, fill="#eef3fb", size=7.6, color=INK):
    lines = str(label).split("\n")
    o = [_rect(x, y, w, h, fill)]
    y0 = y + h / 2.0 - (len(lines) - 1) * size * 0.55 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * size * 1.15, ln, size, color=color))
    return "".join(o)


def _ar(x1, y1, x2, y2, color=BLUE, sw=1.5, dash=""):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def _frame(x0, y0, w, h, xr, yr, xt, yt, xlab, ylab):
    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * w

    def my(v):
        return y0 + h - (v - yr[0]) / (yr[1] - yr[0]) * h

    o = [_rect(x0, y0, w, h, fill="#fbfaf7", sw=0.9)]
    for v, lab in yt:
        py = my(v)
        o.append(_line(x0, py, x0 + w, py, sw=0.45, color="#dcdcdc"))
        o.append(_line(x0 - 3, py, x0, py, sw=0.6))
        o.append(T(x0 - 5, py + 2.0, lab, 5.6, anchor="end", color=GREY))
    for v, lab in xt:
        px = mx(v)
        o.append(_line(px, y0 + h, px, y0 + h + 3, sw=0.6))
        o.append(T(px, y0 + h + 9, lab, 5.6, color=GREY))
    o.append(T(x0 + w / 2.0, y0 + h + 18, xlab, 6.4, color=INK))
    o.append('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
             'style="font:6.4px Inter,Helvetica,sans-serif;fill:%s">%s</text>'
             % (x0 - 24, y0 + h / 2.0, x0 - 24, y0 + h / 2.0, INK, esc(ylab)))
    return "".join(o), mx, my


def _series(points, mx, my, color, dot=0, dash=""):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=1.5, color=color, dash=dash)]
    for px, py in pts:
        if dot:
            o.append(_circle(px, py, dot, fill=color, sw=0))
    return "".join(o)
