# -*- coding: utf-8 -*-
"""Shared SVG primitives for the Process Control and SIS reader figures.

Same conventions as `hb06fig`: every figure function returns
`(svg, caption_vi, caption_en, aria_vi, aria_en)` built through `_fig()`,
and every curve is computed from its governing formula.
"""
import math
import re

from hbfig import Box, STYLE, _f, _fig, svg   # noqa: F401  (re-exported)

INK = "#2a2a2a"
GOLD = "#b45309"
GREY = "#888"
BLUE = "#1f5f8b"
RED = "#b03a2e"
GREEN = "#2e7d4f"
FILL = "#f6e6c8"
PAPER = "#fbfaf7"


# ---------------------------------------------------------------- shapes
def _rect(x, y, w, h, fill="#fff", sw=1.1, dash="", stroke=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, stroke or INK, sw, d))


def _line(x1, y1, x2, y2, sw=1, dash="", color=INK):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _txt(x, y, s, size=8.5, anchor="middle", color="#111", weight=""):
    s = re.sub(r"<sub>(.*?)</sub>",
               r'<tspan baseline-shift="sub" font-size="0.72em">\1</tspan>', s)
    s = re.sub(r"<sup>(.*?)</sup>",
               r'<tspan baseline-shift="super" font-size="0.72em">\1</tspan>', s)
    w = ("font-weight:%s;" % weight) if weight else ""
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx Inter,Helvetica,sans-serif;'
            'fill:%s;%s">%s</text>' % (_f(x), _f(y), anchor, size, color, w, s))


def _arrow(x1, y1, x2, y2, sw=1.2, color=INK, dash="", head="a6"):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s '
            'marker-end="url(#%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d, head))


def _defs():
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a7" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="h6" width="7" height="7" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="#9a9a9a" stroke-width="0.7"/></pattern>'
            '<pattern id="h7" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(-45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#b9b0a0" stroke-width="0.6"/></pattern>'
            '</defs>' % (INK, INK))


def _hatch(x, y, w, h, step=7):
    o = []
    n = int((w + h) / step) + 1
    for i in range(n + 1):
        x1 = x + i * step
        o.append(_line(max(x, x1), y, max(x, x1 - h), y + h, sw=0.6, color="#9a9a9a"))
    return "".join(o)


def _poly(pts, fill="none", sw=1.4, color=INK, dash="", close=False):
    d = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    tag = "polygon" if close else "polyline"
    da = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<%s points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (tag, d, fill, color, sw, da))


def _path(d, fill="none", sw=1.4, color=INK, dash=""):
    da = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, color, sw, da))


def _circle(cx, cy, r, fill="none", sw=1.1, color=INK, dash=""):
    da = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, color, sw, da))


def _ellipse(cx, cy, rx, ry, fill="none", sw=1.1, color=INK):
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy), _f(rx), _f(ry), fill, color, sw))


def _ring(cx, cy, r_in, r_out, fill="#e9e3d6"):
    return (_circle(cx, cy, r_out, fill=fill)
            + _circle(cx, cy, r_in, fill="#fdfdfd"))


# ---------------------------------------------------------------- blocks
def _box(x, y, w, h, label, fill="#eef3fb", sw=1.1, size=8, sub="", color=INK):
    """A labelled block; `label` may contain a newline for a second line."""
    o = [_rect(x, y, w, h, fill, sw)]
    lines = label.split("\n")
    cy = y + h / 2.0 + (0 if len(lines) == 1 else -size * 0.42)
    for i, ln in enumerate(lines):
        o.append(_txt(x + w / 2.0, cy + i * (size + 1.4), ln, size, color=color))
    if sub:
        o.append(_txt(x + w / 2.0, y + h - 5, sub, size - 1.2, color=GREY))
    return "".join(o)


def _node(cx, cy, label, fill="#eef3fb", r=13, size=9):
    return _circle(cx, cy, r, fill=fill) + _txt(cx, cy + size * 0.36, label, size)


def _axes(x0, y0, W, H, xlab, ylab, xt=None, yt=None):
    """Cartesian axes with optional tick lists [(value, label), …] in data units."""
    # Both axis titles sit on the top row: the x title at the right end of the
    # abscissa, the y title above the ordinate. Keeping the x title out of the
    # tick row stops it colliding with the last tick label ("100").
    o = [_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1),
         _arrow(x0, y0 + H, x0, y0 - 12, sw=1),
         _txt(x0 + W, y0 - 16, xlab, 7.4, anchor="end", color=GREY),
         _txt(x0 + 5, y0 - 14, ylab, 7.6, color=GREY)]
    for v, lab in (xt or []):
        px = x0 + v * W
        o.append(_line(px, y0 + H, px, y0 + H + 3, sw=0.8))
        o.append(_txt(px, y0 + H + 12, lab, 6.8, color=GREY))
    for v, lab in (yt or []):
        py = y0 + H - v * H
        o.append(_line(x0 - 3, py, x0, py, sw=0.8))
        o.append(_txt(x0 - 5, py + 2.4, lab, 6.8, anchor="end", color=GREY))
    return "".join(o)


def _curve(fn, x0, y0, W, H, n=121, xr=(0.0, 1.0), yr=(0.0, 1.0), **kw):
    """Plot fn(t) for t in xr over a box, mapping yr onto the height."""
    lo, hi = xr
    a, b = yr
    pts = []
    for i in range(n):
        t = lo + (hi - lo) * i / (n - 1.0)
        v = fn(t)
        if v is None:
            continue
        pts.append((x0 + (t - lo) / (hi - lo) * W, y0 + H - (v - a) / (b - a) * H))
    return _poly(pts, **kw)


def _label(x, y, s, size=7, color=GREY, anchor="middle", weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)
