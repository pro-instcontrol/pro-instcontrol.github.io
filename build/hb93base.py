# -*- coding: utf-8 -*-
"""Shared drawing primitives for the Chapter 93 figures (93.1–93.20).

Split out because the chapter has twenty figures: `hb93fig.py` holds 93.1–93.10
and `hb93figb.py` holds 93.11–93.20, both importing from here.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _r().
"""
import math

from hbfig import _f

E = "#2a2a2a"
S = "#8a8a8a"
GRID = "#e2e2e2"
GOLD = "#b45309"
BLUE = "#1d4ed8"
TEAL = "#0f766e"
RED = "#b91c1c"
GREEN = "#15803d"
GLASS = "#f2f2f2"
DIELE = "#e4e4e4"
METAL = "#c4c4c4"


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="h%s" markerWidth="7" markerHeight="7" refX="5" refY="2.4" '
            'orient="auto"><path d="M0,0 L5,2.4 L0,4.8 z" fill="%s"/></marker>'
            '<style>.ts{font:9.5px Inter,Helvetica,sans-serif;fill:#666}'
            '.tm{font:9.5px Inter,Helvetica,sans-serif;fill:#222}'
            '.tb{font:9.5px Inter,Helvetica,sans-serif;fill:#111;font-weight:700}'
            '.txs{font:8px Inter,Helvetica,sans-serif;fill:#444}'
            '.tcap{font:8.6px Inter,Helvetica,sans-serif;fill:#555}'
            '.tf{font:11px "Cambria Math",Georgia,serif;fill:#111}'
            '</style></defs>' % (tag, E, tag, E))


def _lbl(x, y, txt, cls="tm", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _r(x, y, parts, anchor="start", cls="tm"):
    """parts = [(text, is_sub), ...] — subscript via tspan, never <sub>."""
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7.4" dy="2.2">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.2">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _line(x1, y1, x2, y2, sw=1.2, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="931", sw=1.15, col=E, head="a"):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, head, tag))


def _rect(x, y, w, h, sw=1.2, fill="#fff", dash="", col=E):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, col, sw, d))


def _poly(pts, sw=1.2, fill="#fff", col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (s, fill, col, sw, d))


def _path(pts, sw=1.5, col=E, dash="", fill="none", close=False):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    if close:
        s += " Z"
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (s, fill, col, sw, d))


def _dot(x, y, r=2.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _circ(x, y, r=4.4, col=E, fill="none", sw=1.1):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(x), _f(y), _f(r), fill, col, sw))


def _hatch(tag, x, y, w, h, step=9, col="#9a9a9a"):
    """Diagonal hatching clipped to a rectangle."""
    o = ['<clipPath id="c%s"><rect x="%s" y="%s" width="%s" height="%s"/></clipPath>'
         % (tag, _f(x), _f(y), _f(w), _f(h)),
         '<g clip-path="url(#c%s)">' % tag]
    k = -int(h)
    while k < w + h:
        o.append(_line(x + k, y + h, x + k + h, y, 0.7, col))
        k += step
    o.append("</g>")
    return "".join(o)


def _slab(x, y, w, d, t, dx=42, dy=24, fill=GLASS, col=E, sw=1.1):
    """An isometric plate: top face (w x d), front face and right face of height t."""
    right = [(x + w, y), (x + w + dx, y - dy), (x + w + dx, y - dy + t), (x + w, y + t)]
    front = [(x, y), (x + w, y), (x + w, y + t), (x, y + t)]
    top = [(x, y), (x + w, y), (x + w + dx, y - dy), (x + dx, y - dy)]
    return _poly(right, sw, fill, col) + _poly(front, sw, fill, col) + _poly(top, sw, fill, col)


def _isostrip(x, y, w, depth, t, dx, dy, fill=METAL, col=S, sw=0.7):
    """A strip lying on an isometric top face, running along the width."""
    yy = y - dy * depth
    xx = x + dx * depth
    return _poly([(xx, yy), (xx + w, yy), (xx + w + dx * t, yy - dy * t),
                  (xx + dx * t, yy - dy * t)], sw, fill, col)


def _isostrip_d(x, y, w, depth, dx, dy, fill=METAL, col=S, sw=0.7):
    """A strip lying on an isometric top face, running along the depth."""
    return _poly([(x, y), (x + w, y), (x + w + dx * depth, y - dy * depth),
                  (x + dx * depth, y - dy * depth)], sw, fill, col)


class Frame(object):
    """Linear or log mapping from data space to canvas space."""

    def __init__(self, x, y, w, h, xr, yr, xlog=False, ylog=False):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.xr, self.yr = xr, yr
        self.xlog, self.ylog = xlog, ylog

    def X(self, v):
        a, b = self.xr
        if self.xlog:
            t = (math.log10(max(v, 1e-9)) - math.log10(a)) / (math.log10(b) - math.log10(a))
        else:
            t = (v - a) / float(b - a)
        return self.x + t * self.w

    def Y(self, v):
        a, b = self.yr
        if self.ylog:
            t = (math.log10(max(v, 1e-9)) - math.log10(a)) / (math.log10(b) - math.log10(a))
        else:
            t = (v - a) / float(b - a)
        return self.y + self.h - t * self.h

    def frame(self, sw=1.2):
        return (_line(self.x, self.y + self.h, self.x + self.w, self.y + self.h, sw)
                + _line(self.x, self.y, self.x, self.y + self.h, sw))

    def vgrid(self, vs, col=GRID, sw=0.9):
        return "".join(_line(self.X(v), self.y, self.X(v), self.y + self.h, sw, col)
                       for v in vs)

    def hgrid(self, vs, col=GRID, sw=0.9):
        return "".join(_line(self.x, self.Y(v), self.x + self.w, self.Y(v), sw, col)
                       for v in vs)

    def xticks(self, pairs, len_=4, dy=14, cls="ts"):
        o = []
        for v, lab in pairs:
            px = self.X(v)
            o.append(_line(px, self.y + self.h, px, self.y + self.h + len_, 1.1))
            o.append(_lbl(px, self.y + self.h + dy, lab, cls, "middle"))
        return "".join(o)

    def yticks(self, pairs, len_=4, dx=6, cls="ts"):
        o = []
        for v, lab in pairs:
            py = self.Y(v)
            o.append(_line(self.x - len_, py, self.x, py, 1.1))
            o.append(_lbl(self.x - dx, py + 3.2, lab, cls, "end"))
        return "".join(o)

    def curve(self, pts, sw=1.7, col=E, dash=""):
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        s = "M" + " L".join("%s %s" % (_f(self.X(a)), _f(self.Y(b))) for a, b in pts)
        return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s/>' % (s, col, sw, d)

    def xlab(self, txt, dy=30, cls="ts"):
        return _lbl(self.x + self.w / 2.0, self.y + self.h + dy, txt, cls, "middle")

    def ylab(self, txt, dx=-42, cls="ts"):
        cy = self.y + self.h / 2.0
        return ('<text class="%s" x="%s" y="%s" text-anchor="middle" '
                'transform="rotate(-90 %s %s)">%s</text>'
                % (cls, _f(self.x + dx), _f(cy), _f(self.x + dx), _f(cy), txt))
