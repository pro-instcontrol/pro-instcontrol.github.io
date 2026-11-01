# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 25 — Tactile Sensing
(R. E. Saad, A. Bonen, K. C. Smith, B. Benhabib — University of Toronto).

The source chapter contains exactly twelve figures (25.1–25.12).
FIGS is a 12-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"
BLUE = "#1f4e79"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _subs(x, y, parts, anchor="start", cls="t"):
    """Text with real subscripts: parts is [(txt, is_subscript), ...]."""
    s = ""
    prev = False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="8" dy="3">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-3">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs():
    return ('<defs>'
            '<marker id="ah25" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah25g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah25s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah25b" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah25r" markerWidth="9" markerHeight="9" refX="2" refY="3" '
            'orient="auto"><path d="M7,0 L0,3 L7,6 z" fill="%s"/></marker>'
            '<pattern id="hatch25" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" '
            'stroke="#9aa4b2" stroke-width="1"/></pattern>'
            '</defs>' % (E, G, S, BLUE, S))


def _arr(x1, y1, x2, y2, col=E, marker="ah25", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _dim(x1, y1, x2, y2, txt="", off=0, vertical=True, col=S):
    """Dimension line with tick ends and a label."""
    o = [_line(x1, y1, x2, y2, col, 1.0)]
    if vertical:
        o.append(_line(x1 - 4, y1, x1 + 4, y1, col, 1.0))
        o.append(_line(x2 - 4, y2, x2 + 4, y2, col, 1.0))
    else:
        o.append(_line(x1, y1 - 4, x1, y1 + 4, col, 1.0))
        o.append(_line(x2, y2 - 4, x2, y2 + 4, col, 1.0))
    if txt:
        if vertical:
            o.append(_lbl(x1 + off, (y1 + y2) / 2.0 + 4, txt, "ts", "middle"))
        else:
            o.append(_lbl((x1 + x2) / 2.0, y1 + off, txt, "ts", "middle"))
    return "".join(o)


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=4):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _rect(x, y, w, h, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, _f(sw), d))


def _dot(x, y, r=3.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _line(x1, y1, x2, y2, col=S, sw=1.0, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, _f(sw), d))


def _path(d, col=E, sw=1.4, fill="none", dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, col, _f(sw), ds))


def _circ(cx, cy, r, fill="none", col=E, sw=1.4, dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, _f(sw), ds))


def _poly(pts, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    p = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (p, fill, col, _f(sw), d))


def _opamp(x, y, w=46, h=42, inv_top=True):
    """Op-amp triangle with input stubs; x,y is the top-left of the bounding box."""
    o = [_path("M%s,%s L%s,%s L%s,%s z" % (_f(x), _f(y), _f(x), _f(y + h), _f(x + w), _f(y + h / 2.0)),
               E, 1.4, "#ffffff")]
    o.append(_lbl(x + 9, y + h * 0.35 + 4, "−", "t", "middle"))
    o.append(_lbl(x + 9, y + h * 0.72 + 4, "+", "t", "middle"))
    return "".join(o)


def _res(x1, y1, x2, y2, n=6, amp=4):
    """Zig-zag resistor between two points (horizontal or vertical)."""
    dx, dy = x2 - x1, y2 - y1
    L = _m.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    pts = [(x1, y1)]
    lead = L * 0.18
    body = L - 2 * lead
    pts.append((x1 + ux * lead, y1 + uy * lead))
    for i in range(n):
        t = (i + 0.5) / n
        s = 1 if i % 2 == 0 else -1
        px = x1 + ux * (lead + body * t) + nx * amp * s
        py = y1 + uy * (lead + body * t) + ny * amp * s
        pts.append((px, py))
    pts.append((x1 + ux * (lead + body), y1 + uy * (lead + body)))
    pts.append((x2, y2))
    p = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="1.3"/>' % (p, E)


def _cap(x, y, gap=7, w=20, vert=True):
    """Capacitor centred at x,y."""
    if vert:
        return (_line(x - w / 2, y - gap / 2, x + w / 2, y - gap / 2, E, 1.6)
                + _line(x - w / 2, y + gap / 2, x + w / 2, y + gap / 2, E, 1.6))
    return (_line(x - gap / 2, y - w / 2, x - gap / 2, y + w / 2, E, 1.6)
            + _line(x + gap / 2, y - w / 2, x + gap / 2, y + w / 2, E, 1.6))


def _arc(cx, cy, r, a0, a1, col=S, sw=0.9, n=16):
    """Arc sampled as a polyline; angles in radians, y axis pointing down."""
    pts = []
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / float(n)
        pts.append((cx + r * _m.cos(a), cy + r * _m.sin(a)))
    d = "M%s,%s " % (_f(pts[0][0]), _f(pts[0][1])) + " ".join(
        "L%s,%s" % (_f(p[0]), _f(p[1])) for p in pts[1:])
    return _path(d, col, sw)


def _wavy(x1, y1, x2, y2, n=4, amp=2.6, col=E, sw=1.0):
    """Zig-zag (wavy) arrow — used for light travelling in a fibre."""
    L = _m.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    pts = [(x1, y1)]
    for k in range(n):
        t = (k + 1) / float(n + 1)
        s = 1 if k % 2 == 0 else -1
        pts.append((x1 + ux * L * t + nx * amp * s, y1 + uy * L * t + ny * amp * s))
    pts.append((x2, y2))
    d = "M%s,%s " % (_f(pts[0][0]), _f(pts[0][1])) + " ".join(
        "L%s,%s" % (_f(p[0]), _f(p[1])) for p in pts[1:])
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'marker-end="url(#ah25)"/>' % (d, col, _f(sw)))


def _bar(x1, y1, x2, y2, col, w=7.0):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, _f(w)))


# ---------------------------------------------------------------- 25.1
def fig_25_1():
    o = [_defs()]
    # block in 3/4 view: front face + top face + left face
    o.append(_poly([(96, 128), (556, 128), (600, 158), (140, 158)], "#f7f9fc", E, 1.4))
    o.append(_rect(140, 158, 460, 92, FILL, E, 1.4))
    o.append(_poly([(96, 128), (140, 158), (140, 250), (96, 220)], "#e6ebf2", E, 1.4))
    # sensing element row at depth d (front face) + on the left face
    for i in range(9):
        xx = 168 + i * 49
        o.append(_rect(xx, 206, 18, 11, "#2a2a2a", E, 0.8))
    o.append(_line(150, 196, 590, 196, S, 0.9, "4 3"))
    # indentor
    o.append(_circ(348, 96, 30, "#ffffff", E, 1.6))
    o.append(_path("M318,96 A30,30 0 0 0 378,96", S, 1.0))
    o.append(_arr(348, 30, 348, 62))
    o.append(_lbl(356, 44, "F"))
    # stress spreading under the indentor
    for dx in (-52, -30, 30, 52):
        o.append(_path("M%s,%s Q%s,%s %s,%s"
                       % (_f(348 + dx * 0.45), _f(126), _f(348 + dx * 0.8), _f(160),
                          _f(348 + dx), _f(196)), S, 0.9, "none", "3 3"))
    # depth dimension
    o.append(_dim(624, 158, 624, 206, "d", off=14))
    o.append(_line(600, 158, 628, 158, S, 0.8))
    o.append(_line(600, 206, 628, 206, S, 0.8))
    # labels
    o.append(_lbl(150, 120, "lớp mềm dẻo", "ts", "start"))
    o.append(_lbl(196, 240, "phần tử cảm nhận lực", "ts", "start"))
    o.append(_line(196, 228, 196, 218, S, 0.9))
    o.append(_lbl(392, 82, "vật ấn", "ts", "start"))
    o.append(_line(388, 84, 378, 92, S, 0.9))

    return _fig(svg(680, 268, "".join(o),
                    "Vật rắn ấn lõm lớp mềm dẻo phía trên một dãy phần tử cảm nhận lực"),
                "Hình 25.1 · Một vật ấn lõm lớp phủ mềm dẻo của dãy cảm biến xúc giác, trong đó một "
                "dãy phần tử cảm nhận lực được đặt cách mặt trên một khoảng d.",
                "Figure 25.1 · An object indenting a compliant layer, where an array of force-sensing "
                "elements is placed at a distance d from the surface.",
                "Vật rắn ấn xuống lớp mềm dẻo; dãy phần tử cảm nhận lực nằm ở độ sâu d",
                "A rigid object indenting a compliant layer; force-sensing elements at depth d")


# ---------------------------------------------------------------- 25.2
def fig_25_2():
    o = [_defs()]
    x0, x1 = 150, 560
    ytop, ybot = 170, 244
    o.append(_rect(x0, ytop, x1 - x0, ybot - ytop, FILL, E, 1.4))
    # pressure distribution: filled area above the surface
    xm0, xm1 = 196, 514
    curve = []
    n = 26
    for i in range(n + 1):
        xx = xm0 + (xm1 - xm0) * i / float(n)
        u = (xx - (xm0 + xm1) / 2.0) / ((xm1 - xm0) / 2.0)
        hgt = 54 * (1 - u * u) ** 0.55 + 7
        curve.append((xx, ytop - hgt))
    poly = [(xm0, ytop)] + curve + [(xm1, ytop)]
    o.append('<polygon points="%s" fill="url(#hatch25)" stroke="none"/>'
             % " ".join("%s,%s" % (_f(a), _f(b)) for a, b in poly))
    o.append(_path("M%s,%s " % (_f(curve[0][0]), _f(curve[0][1]))
                   + " ".join("L%s,%s" % (_f(a), _f(b)) for a, b in curve[1:]), E, 1.3))
    o.append(_line(xm0, curve[0][1], xm0, ytop, E, 1.3))
    o.append(_line(xm1, curve[-1][1], xm1, ytop, E, 1.3))
    o.append(_line(xm0, ytop, xm1, ytop, E, 1.4))
    # x_min / x_max just under the surface
    o.append(_subs(xm0, ytop + 15, [("x", False), ("min", True)], "middle", "ts"))
    o.append(_subs(xm1, ytop + 15, [("x", False), ("max", True)], "middle", "ts"))
    # q_v label on the curve
    o.append(_subs(238, 118, [("q", False), ("v", True), ("(x)", False)], "start", "t"))
    # x axis (left, clear of the curve)
    o.append(_arr(96, 128, 140, 128))
    o.append(_lbl(146, 132, "x"))
    # z axis
    o.append(_arr(355, ybot, 355, ybot + 30))
    o.append(_lbl(346, ybot + 28, "z", "t", "end"))
    # depth d
    o.append(_dim(600, ytop, 600, ybot, "d", off=14))
    o.append(_line(x1, ytop, 604, ytop, S, 0.8))
    o.append(_line(x1, ybot, 604, ybot, S, 0.8))
    o.append(_lbl(355, 296, "lớp mềm dẻo, đồng nhất, đẳng hướng", "ts", "middle"))

    return _fig(svg(680, 312, "".join(o),
                    "Đầu đo một chiều lý tưởng chịu ứng suất pháp q_v(x)"),
                "Hình 25.2 · Đầu đo một chiều lý tưởng chịu một ứng suất pháp.",
                "Figure 25.2 · Ideal one-dimensional transducer subjected to a normal stress.",
                "Lớp mềm dẻo chịu phân bố ứng suất pháp q_v(x) giữa x_min và x_max",
                "A compliant layer under a normal stress distribution q_v(x) from x_min to x_max")


# ---------------------------------------------------------------- 25.3
def fig_25_3():
    o = [_defs()]
    x0, x1 = 120, 560
    ytop, ybot = 160, 240
    o.append(_rect(x0, ytop, x1 - x0, ybot - ytop, FILL, E, 1.4))
    # discrete force arrows
    n = 9
    xs = [150 + i * (500.0 / (n - 1)) for i in range(n)]
    for xx in xs:
        o.append(_arr(xx, 104, xx, ytop - 2, E, "ah25", 1.2))
    o.append(_subs(xs[0], 98, [("f", False), ("1", True)], "middle", "ts"))
    o.append(_subs(xs[1], 98, [("f", False), ("2", True)], "middle", "ts"))
    o.append(_lbl((xs[3] + xs[4]) / 2.0, 98, "…", "t", "middle"))
    o.append(_subs(xs[5], 98, [("f", False), ("j", True)], "middle", "ts"))
    o.append(_lbl((xs[6] + xs[7]) / 2.0, 98, "…", "t", "middle"))
    o.append(_subs(xs[8], 98, [("f", False), ("n", True)], "middle", "ts"))
    # x_min / x_max at the surface
    o.append(_subs(x0 - 4, ytop + 13, [("x", False), ("min", True)], "end", "ts"))
    o.append(_subs(x1 + 4, ytop + 13, [("x", False), ("max", True)], "start", "ts"))
    # spacing dimensions, above the surface, clear of the arrows
    ya, yb = 122, 140
    o.append(_dim(xs[2], ya, xs[3], ya, "", vertical=False))
    o.append(_subs((xs[2] + xs[3]) / 2.0, ya - 5, [("Δx", False), ("q", True)], "middle", "ts"))
    o.append(_dim(xs[3] + 14, yb, xs[4] + 14, yb, "", vertical=False))
    o.append(_subs((xs[3] + xs[4]) / 2.0 + 14, yb - 5,
                   [("Δx", False), ("p", True)], "middle", "ts"))
    # sensing cells inside
    for i in range(8):
        xx = 148 + i * 50
        o.append(_rect(xx, 198, 26, 12, "#2a2a2a", E, 0.8))
    o.append(_subs(150, 230, [("ζ", False), ("1", True)], "start", "ts"))
    o.append(_subs(200, 230, [("ζ", False), ("2", True)], "start", "ts"))
    o.append(_lbl(270, 230, "…", "ts"))
    o.append(_subs(348, 230, [("ζ", False), ("i", True)], "start", "ts"))
    o.append(_lbl(420, 230, "…", "ts"))
    o.append(_subs(498, 230, [("ζ", False), ("n", True)], "start", "ts"))
    # z axis
    o.append(_arr(340, ybot, 340, ybot + 26))
    o.append(_lbl(332, ybot + 24, "z", "t", "end"))
    # depth
    o.append(_dim(600, ytop, 600, 204, "d", off=14))
    o.append(_line(x1, ytop, 604, ytop, S, 0.8))
    o.append(_line(578, 204, 604, 204, S, 0.8))
    o.append(_lbl(340, 296, "phần tử cảm nhận đặt cách nhau Δx", "ts", "middle"))

    return _fig(svg(680, 310, "".join(o),
                    "Đầu đo một chiều với các phần tử cảm nhận rời rạc đặt tại z bằng d"),
                "Hình 25.3 · Đầu đo một chiều với các phần tử cảm nhận rời rạc đặt tại z = d.",
                "Figure 25.3 · One-dimensional transducer with discrete sensing elements located at "
                "z = d.",
                "Các lực rời rạc f1 đến fn tác dụng lên lớp; các ô cảm nhận ζ nằm ở độ sâu d",
                "Discrete forces f1 to fn on the layer; sensing cells zeta at depth d")


def fig_25_4():
    o = [_defs()]
    rowy = [112, 150, 188]
    colx = [300, 400, 500]
    # Vcc + decoder
    o.append(_subs(46, 62, [("V", False), ("cc", True)], "middle", "ts"))
    o.append(_line(46, 68, 46, 86, E, 1.2))
    o.append(_rect(30, 86, 34, 118, "#e6ebf2", E, 1.2))
    for i in range(3):
        o.append(_rect(38, 100 + i * 32, 18, 14, "#ffffff", E, 1.0))
    o.append(_lbl(47, 218, "bộ giải mã", "ts", "middle"))
    # rows
    for i, yy in enumerate(rowy):
        o.append(_line(64, yy, 296, yy, E, 1.2))
        o.append(_lbl(88, yy - 6, "hàng %d" % (i + 1), "ts", "start"))
    # columns (segmented so the resistor bodies are not overdrawn)
    for xx in colx:
        segs = [(100, 112), (136, 150), (174, 188), (212, 226)]
        for y1, y2 in segs:
            o.append(_line(xx, y1, xx, y2, E, 1.2))
    # resistors
    for j, xx in enumerate(colx):
        for i, yy in enumerate(rowy):
            o.append(_res(xx, yy, xx, yy + 24))
            o.append(_subs(xx - 7, yy + 17,
                           [("R", False), ("%d%d" % (i + 1, j + 1), True)], "end", "ts"))
    # forces at the top
    for j, xx in enumerate(colx):
        o.append(_arr(xx, 54, xx, 96))
        o.append(_subs(xx + 6, 66, [("f", False), ("%d" % (j + 1), True)], "start", "ts"))
    # multiplexer
    o.append(_rect(296, 230, 240, 22, "#e6ebf2", E, 1.2))
    o.append(_lbl(416, 245, "bộ dồn kênh", "ts", "middle"))
    for xx in colx:
        o.append(_line(xx, 226, xx, 230, E, 1.2))
        o.append(_lbl(xx + 5, 224, "cột %d" % (colx.index(xx) + 1), "ts", "start"))
    # output from multiplexer to the inverting input
    o.append(_line(416, 252, 416, 266, E, 1.2))
    o.append(_line(416, 266, 404, 266, E, 1.2))
    o.append(_line(404, 266, 404, 292, E, 1.2))
    o.append(_line(404, 292, 430, 292, E, 1.2))
    # op-amp
    o.append(_opamp(430, 278, 44, 40))
    o.append(_line(430, 307, 412, 307, E, 1.2))
    o.append(_line(412, 307, 412, 330, E, 1.2))
    o.append(_line(400, 330, 424, 330, E, 1.6))
    for i in range(3):
        o.append(_line(404 + i * 6, 330, 404 + i * 6 - 3, 336, S, 1.0))
    o.append(_line(474, 298, 512, 298, E, 1.2))
    o.append(_subs(518, 302, [("V", False), ("o", True)], "start", "t"))
    # feedback resistor
    o.append(_line(420, 292, 420, 268, E, 1.2))
    o.append(_line(420, 268, 462, 268, E, 1.2))
    o.append(_dot(420, 292, 2.6))
    o.append(_res(462, 268, 508, 268))
    o.append(_subs(485, 260, [("R", False), ("f", True)], "middle", "ts"))
    o.append(_line(508, 268, 512, 268, E, 1.2))
    o.append(_line(512, 268, 512, 298, E, 1.2))
    o.append(_dot(512, 298, 2.6))

    return _fig(svg(680, 350, "".join(o),
                    "Sơ đồ nguyên lý đầu đo điện trở: ma trận 3 nhân 3 phần tử, bộ giải mã, bộ dồn kênh và khuếch đại"),
                "Hình 25.4 · Cấu hình chung của một đầu đo kiểu điện trở.",
                "Figure 25.4 · General configuration of a resistive transducer.",
                "Ma trận điện trở 3x3 quét theo hàng và cột, qua bộ dồn kênh tới khuếch đại thuật toán",
                "A 3x3 resistor matrix scanned by rows and columns through a multiplexer to an op-amp")


# ---------------------------------------------------------------- 25.5
def fig_25_5():
    o = [_defs()]
    # ---- (a) single cell, elevation with the unloaded plate shown dashed
    o.append(_rect(70, 96, 142, 14, "none", S, 1.1, "5 4"))
    o.append(_rect(70, 118, 142, 14, "#dfe5ee", E, 1.3))
    o.append(_rect(70, 132, 142, 44, "#f6f2e8", E, 1.3))
    o.append(_rect(70, 176, 142, 10, "#dfe5ee", E, 1.3))
    o.append(_arr(141, 50, 141, 92))
    o.append(_lbl(149, 64, "F"))
    o.append(_lbl(141, 160, "điện môi", "ts", "middle"))
    o.append(_lbl(64, 90, "điện cực", "ts", "end"))
    o.append(_line(66, 88, 66, 96, S, 0.9))
    # h : compressed dielectric thickness
    o.append(_dim(44, 132, 44, 176, "", off=0))
    o.append(_line(40, 132, 74, 132, S, 0.7))
    o.append(_line(40, 176, 74, 176, S, 0.7))
    o.append(_lbl(34, 158, "h", "ts", "end"))
    # h0 : unloaded gap
    o.append(_dim(232, 110, 232, 176, "", off=0))
    o.append(_line(212, 110, 236, 110, S, 0.7))
    o.append(_line(212, 176, 236, 176, S, 0.7))
    o.append(_subs(242, 148, [("h", False), ("0", True)], "start", "ts"))
    o.append(_dim(70, 202, 212, 202, "l", off=15, vertical=False))
    o.append(_lbl(141, 238, "(a)", "tb", "middle"))

    # ---- (b) array with multiplexers
    gx0, gx1, gy0, gy1 = 296, 442, 100, 188
    for i in range(4):
        yy = gy0 + i * (gy1 - gy0) / 3.0
        o.append(_line(gx0, yy, gx1, yy, S, 1.0))
    for j in range(5):
        xx = gx0 + j * (gx1 - gx0) / 4.0
        o.append(_line(xx, gy0, xx, gy1, S, 1.0))
        o.append(_line(xx, gy0 - 10, xx, gy0, E, 1.0))
        o.append(_line(xx, gy1, xx, gy1 + 10, E, 1.0))
    for i in range(4):
        for j in range(5):
            o.append(_dot(gx0 + j * (gx1 - gx0) / 4.0, gy0 + i * (gy1 - gy0) / 3.0, 2.2, "#2a2a2a"))
    o.append(_rect(gx0 - 8, 70, gx1 - gx0 + 16, 20, "#e6ebf2", E, 1.1))
    o.append(_lbl((gx0 + gx1) / 2.0, 84, "bộ dồn kênh", "ts", "middle"))
    o.append(_rect(gx0 - 8, 198, gx1 - gx0 + 16, 20, "#e6ebf2", E, 1.1))
    o.append(_lbl((gx0 + gx1) / 2.0, 212, "bộ dồn kênh", "ts", "middle"))
    # source + detector
    o.append(_circ(258, 144, 13, "#ffffff", E, 1.3))
    o.append(_lbl(258, 149, "~", "t", "middle"))
    o.append(_subs(258, 174, [("V", False), ("s", True)], "middle", "ts"))
    o.append(_line(271, 144, gx0, 144, E, 1.1))
    o.append(_lbl((gx0 + gx1) / 2.0, 232, "bộ phát hiện", "ts", "middle"))
    o.append(_line((gx0 + gx1) / 2.0, 218, (gx0 + gx1) / 2.0, 220, E, 1.1))
    o.append(_lbl(369, 250, "(b)", "tb", "middle"))

    # ---- (c) equivalent circuit
    o.append(_circ(486, 152, 13, "#ffffff", E, 1.3))
    o.append(_lbl(486, 157, "~", "t", "middle"))
    o.append(_subs(470, 156, [("V", False), ("s", True)], "end", "ts"))
    o.append(_line(486, 139, 486, 112, E, 1.2))
    o.append(_line(486, 112, 536, 112, E, 1.2))
    o.append(_res(536, 112, 536, 144))
    o.append(_subs(544, 132, [("R", False), ("d", True)], "start", "ts"))
    o.append(_line(536, 144, 536, 162, E, 1.2))
    o.append(_line(486, 165, 486, 196, E, 1.2))
    o.append(_line(536, 162, 648, 162, E, 1.2))
    o.append(_cap(578, 174, 7, 24, True))
    o.append(_line(578, 162, 578, 170.5, E, 1.2))
    o.append(_line(578, 177.5, 578, 196, E, 1.2))
    o.append(_subs(596, 176, [("C", False), ("ij", True)], "start", "ts"))
    o.append(_cap(626, 174, 7, 24, True))
    o.append(_line(626, 162, 626, 170.5, E, 1.2))
    o.append(_line(626, 177.5, 626, 196, E, 1.2))
    o.append(_subs(644, 176, [("C", False), ("d", True)], "start", "ts"))
    o.append(_line(478, 196, 648, 196, E, 1.6))
    o.append(_line(486, 196, 486, 196, E, 1.2))
    o.append(_subs(556, 152, [("V", False), ("d", True)], "middle", "ts"))
    o.append(_lbl(592, 238, "(c)", "tb", "middle"))

    return _fig(svg(680, 256, "".join(o),
                    "Ô cơ bản của cảm biến xúc giác điện dung, cấu hình dãy và mạch tương đương"),
                "Hình 25.5 · (a) Ô cơ bản của một cảm biến xúc giác kiểu tụ điện. (b) Cấu hình điển hình "
                "của một cảm biến xúc giác điện dung. (c) Mạch tương đương để đo điện dung C<sub>ij</sub>.",
                "Figure 25.5 · (a) Basic cell of a capacitive tactile sensor. (b) Typical configuration of "
                "a capacitive tactile sensor. (c) Equivalent circuit for the measurement of the "
                "capacitance C<sub>ij</sub>.",
                "Ba hình: ô tụ điện có hai điện cực và lớp điện môi; dãy cảm biến quét hàng cột; mạch tương đương",
                "Three panels: a capacitor cell with electrodes and dielectric; a scanned array; the equivalent circuit")


# ---------------------------------------------------------------- 25.6
def fig_25_6():
    o = [_defs()]
    # ---- (a) piezoelectric cell
    o.append(_poly([(86, 92), (216, 92), (232, 106), (102, 106)], "#dfe5ee", E, 1.3))
    o.append(_poly([(102, 106), (232, 106), (232, 114), (102, 114)], "#c9d2df", E, 1.1))
    o.append(_poly([(102, 114), (232, 114), (232, 172), (102, 172)], "#f6f2e8", E, 1.3))
    o.append(_poly([(102, 172), (232, 172), (232, 180), (102, 180)], "#c9d2df", E, 1.1))
    o.append(_poly([(102, 180), (232, 180), (216, 166), (86, 166)], "#dfe5ee", E, 1.2))
    o.append(_arr(162, 52, 162, 88))
    o.append(_lbl(170, 66, "F"))
    o.append(_lbl(160, 146, "vật liệu áp điện", "ts", "middle"))
    # axes
    o.append(_arr(70, 140, 44, 140))
    o.append(_lbl(38, 144, "1", "t", "end"))
    o.append(_arr(216, 74, 242, 62))
    o.append(_lbl(248, 60, "2", "t"))
    o.append(_arr(176, 194, 176, 220))
    o.append(_lbl(184, 214, "3", "t"))
    # thickness
    o.append(_dim(248, 114, 248, 172, "h", off=13))
    o.append(_line(232, 114, 252, 114, S, 0.7))
    o.append(_line(232, 172, 252, 172, S, 0.7))
    # voltage terminals
    o.append(_line(232, 110, 274, 110, E, 1.1))
    o.append(_line(232, 176, 274, 176, E, 1.1))
    o.append(_line(274, 110, 274, 124, E, 1.1))
    o.append(_line(274, 162, 274, 176, E, 1.1))
    o.append(_lbl(282, 147, "V", "t"))
    o.append(_lbl(145, 240, "(a)", "tb", "middle"))

    # ---- (b) charge amplifier
    # transducer capacitor in series into the inverting node, far side grounded
    o.append(_line(316, 174, 330, 174, E, 1.2))
    o.append(_cap(340, 174, 8, 26, False))
    o.append(_line(348, 174, 440, 174, E, 1.2))
    o.append(_line(316, 174, 316, 200, E, 1.2))
    o.append(_line(304, 200, 328, 200, E, 1.6))
    for i in range(3):
        o.append(_line(308 + i * 6, 200, 308 + i * 6 - 3, 206, S, 1.0))
    o.append(_subs(340, 158, [("C", False), ("s", True)], "middle", "ts"))
    o.append(_opamp(440, 160, 46, 42))
    o.append(_line(486, 181, 524, 181, E, 1.2))
    o.append(_subs(530, 185, [("V", False), ("o", True)], "start", "t"))
    o.append(_line(392, 174, 392, 142, E, 1.2))
    o.append(_dot(392, 174, 2.6))
    o.append(_line(392, 142, 468, 142, E, 1.2))
    o.append(_cap(476, 142, 8, 26, False))
    o.append(_line(484, 142, 520, 142, E, 1.2))
    o.append(_subs(476, 126, [("C", False), ("f", True)], "middle", "ts"))
    o.append(_line(520, 142, 524, 142, E, 1.2))
    o.append(_line(524, 142, 524, 181, E, 1.2))
    o.append(_dot(524, 181, 2.6))
    o.append(_line(440, 192, 424, 192, E, 1.2))
    o.append(_line(424, 192, 424, 212, E, 1.2))
    o.append(_line(412, 212, 436, 212, E, 1.6))
    for i in range(3):
        o.append(_line(416 + i * 6, 212, 416 + i * 6 - 3, 218, S, 1.0))
    o.append(_lbl(340, 238, "(b)", "tb", "middle"))

    return _fig(svg(680, 256, "".join(o),
                    "Ô cơ bản của đầu đo áp điện và bộ khuếch đại điện tích"),
                "Hình 25.6 · (a) Ô cơ bản của một đầu đo áp điện. (b) Bộ khuếch đại điện tích dùng để đo "
                "lực tác dụng.",
                "Figure 25.6 · (a) Basic cell of a piezoelectric transducer. (b) Charge amplifier utilized "
                "for the measurement of the applied force.",
                "Ô áp điện có ba trục và hai điện cực; bộ khuếch đại điện tích với tụ hồi tiếp",
                "A piezoelectric cell with three axes; a charge amplifier with feedback capacitor")


# ---------------------------------------------------------------- 25.7
def fig_25_7():
    o = [_defs()]
    # transducer capacitance on the input node
    o.append(_line(110, 92, 110, 126, E, 1.2))
    o.append(_cap(110, 130, 8, 26, True))
    o.append(_line(110, 92, 168, 92, E, 1.2))
    o.append(_line(110, 134, 110, 164, E, 1.2))
    o.append(_line(102, 164, 122, 164, E, 1.6))
    for i in range(3):
        o.append(_line(105 + i * 6, 164, 105 + i * 6 - 3, 170, S, 1.0))
    o.append(_lbl(110, 80, "C", "ts", "middle"))
    # inverting node and feedback resistor
    o.append(_line(168, 92, 168, 153, E, 1.2))
    o.append(_dot(168, 153, 2.6))
    o.append(_line(168, 153, 208, 153, E, 1.2))
    o.append(_line(168, 108, 200, 108, E, 1.2))
    o.append(_res(200, 108, 246, 108))
    o.append(_subs(223, 100, [("R", False), ("f", True)], "middle", "ts"))
    o.append(_line(246, 108, 252, 108, E, 1.2))
    o.append(_line(252, 108, 252, 159, E, 1.2))
    o.append(_opamp(208, 138, 46, 42))
    o.append(_line(254, 159, 292, 159, E, 1.2))
    o.append(_dot(252, 159, 2.6))
    o.append(_subs(298, 163, [("V", False), ("o", True)], "start", "t"))
    o.append(_line(208, 168, 192, 168, E, 1.2))
    o.append(_line(192, 168, 192, 190, E, 1.2))
    o.append(_line(180, 190, 204, 190, E, 1.6))
    for i in range(3):
        o.append(_line(184 + i * 6, 190, 184 + i * 6 - 3, 196, S, 1.0))
    # annotation
    o.append(_subs(336, 130, [("V", False), ("o", True), (" = ", False), ("R", False),
                              ("f", True), (" · dQ/dt = ", False), ("R", False),
                              ("f", True), (" · i", False)], "start", "ts"))

    return _fig(svg(680, 220, "".join(o),
                    "Bộ chuyển đổi dòng điện sang điện áp dùng khuếch đại thuật toán"),
                "Hình 25.7 · Bộ chuyển đổi dòng điện sang điện áp.",
                "Figure 25.7 · Current-to-voltage converter.",
                "Khuếch đại thuật toán có điện trở hồi tiếp biến dòng điện tích thành điện áp ra",
                "An op-amp with feedback resistor converting charge current into an output voltage")


# ---------------------------------------------------------------- 25.8
def fig_25_8():
    o = [_defs()]
    # ---- (a) reflective transducer, side elevation
    o.append(_rect(84, 88, 250, 20, "#f6f2e8", E, 1.3))
    o.append(_line(84, 108, 334, 108, E, 1.6))
    o.append(_lbl(209, 80, "màng đàn hồi có mặt phản xạ", "ts", "middle"))
    o.append(_arr(209, 40, 209, 84))
    o.append(_lbl(217, 54, "F"))
    # fibers
    o.append(_rect(150, 150, 16, 84, "#dfe5ee", E, 1.2))
    o.append(_rect(228, 150, 16, 84, "#dfe5ee", E, 1.2))
    o.append(_lbl(158, 248, "sợi phát", "ts", "middle"))
    o.append(_lbl(236, 248, "sợi thu", "ts", "middle"))
    # light cone: out of the emitter, off the membrane, back into the receiver
    o.append(_line(158, 150, 116, 108, S, 0.9, "3 3"))
    o.append(_line(158, 150, 214, 108, S, 0.9, "3 3"))
    o.append(_line(214, 108, 236, 150, S, 0.9, "3 3"))
    o.append(_line(158, 132, 158, 112, G, 1.2))
    o.append(_arr(158, 118, 158, 110, G, "ah25g", 1.2))
    o.append(_arr(200, 118, 232, 144, G, "ah25g", 1.2))
    # angle theta at the emitter mouth
    o.append(_path("M158,132 A18,18 0 0 0 168,136", S, 0.9))
    o.append(_lbl(172, 132, "θ", "ts"))
    # gap h
    o.append(_dim(300, 108, 300, 150, "", off=0))
    o.append(_line(236, 108, 304, 108, S, 0.7))
    o.append(_line(244, 150, 304, 150, S, 0.7))
    o.append(_lbl(310, 132, "h", "t"))
    o.append(_lbl(209, 268, "(a)", "tb", "middle"))

    # ---- (b) intensity curve
    ax, ay = 430, 210
    o.append(_arr(ax, ay, ax + 212, ay))
    o.append(_arr(ax, ay, ax, ay - 112))
    o.append(_lbl(ax + 218, ay + 4, "h", "t"))
    o.append(_lbl(ax - 10, ay - 116, "I", "t", "middle"))
    pts = []
    for i in range(41):
        t = i / 40.0
        xx = ax + 6 + t * 196
        u = (xx - ax - 6) / 196.0
        yy = ay - 96 * (u / 0.22) * _m.exp(1 - u / 0.22) if u > 0 else ay
        pts.append((xx, max(yy, ay - 96)))
    o.append(_path("M%s,%s " % (_f(pts[0][0]), _f(pts[0][1]))
                   + " ".join("L%s,%s" % (_f(a), _f(b)) for a, b in pts[1:]), E, 1.5))
    xh = ax + 6 + 0.22 * 196
    o.append(_line(xh, ay, xh, ay - 100, S, 1.0, "4 3"))
    o.append(_subs(xh, ay + 16, [("h", False), ("min", True)], "middle", "ts"))
    o.append(_arr(xh + 26, ay - 66, xh + 82, ay - 66))
    o.append(_lbl(xh + 54, ay - 72, "dải làm việc", "ts", "middle"))
    o.append(_lbl(536, 268, "(b)", "tb", "middle"))

    return _fig(svg(680, 282, "".join(o),
                    "Đầu đo phản xạ quang và cường độ sáng theo khoảng cách h"),
                "Hình 25.8 · (a) Đầu đo kiểu phản xạ. (b) Cường độ sáng như một hàm của khoảng cách h.",
                "Figure 25.8 · (a) Reflective transducer. (b) Light-intensity as a function of the "
                "distance h.",
                "Màng phản xạ trên hai sợi quang, và đường cong cường độ sáng theo khoảng cách",
                "A reflective membrane over two fibers, and the intensity-versus-distance curve")


# ---------------------------------------------------------------- 25.9
def fig_25_9():
    o = [_defs()]
    GT, GB = 150, 226          # glass top / bottom surface

    # ---- glass waveguide
    o.append(_rect(170, GT, 450, GB - GT, "#f3f7fb", E, 1.4))
    o.append(_subs(596, 212, [("n", False), ("2", True)], "end", "ts"))
    o.append(_subs(596, 248, [("n", False), ("1", True)], "end", "ts"))

    # ---- elastic membrane: one profile — a web whose underside swells into
    #      five hemispherical bumps resting on the top surface of the glass
    o.append(_path("M158,110 L628,110 L628,124 L578,124"
                   "A26,26 0 0 1 526,124 L490,124"
                   "A26,26 0 0 1 438,124 L402,124"
                   "A26,26 0 0 1 350,124 L314,124"
                   "A26,26 0 0 1 262,124 L226,124"
                   "A26,26 0 0 1 174,124 L158,124 Z", E, 1.3, "#e7e2d8"))
    o.append(_lbl(176, 98, "màng đàn hồi", "ts"))
    o.append(_line(180, 101, 186, 110, S, 0.9))

    # ---- object pressing on the membrane
    o.append(_rect(300, 54, 150, 56, "#3a3a3a", E, 1.3))
    o.append(_arr(375, 20, 375, 50))
    o.append(_lbl(383, 38, "F"))
    o.append(_lbl(294, 46, "vật ấn", "ts", "end"))

    # ---- light source and mirror
    o.append(_box(40, 250, 62, 38, "Nguồn\nsáng", E, "#efe6d4", 9))
    o.append(_line(104, 110, 146, 130, "#c9ced6", 5.0))
    o.append(_line(104, 110, 146, 130, E, 1.0))
    o.append(_line(71, 250, 122, 120, S, 0.9))
    o.append(_line(74, 250, 128, 122, S, 0.9, "3 3"))
    o.append(_line(122, 120, 170, 194, E, 1.1))
    o.append(_line(128, 122, 170, 206, E, 1.1, "4 3"))

    # ---- ray zig-zag inside the waveguide
    seg = [((170, 198), (288, GT), None),
           ((288, GT), (376, GB), "4 3"),
           ((376, GB), (464, GT), None),
           ((464, GT), (552, GB), "4 3"),
           ((552, GB), (620, 167), None)]
    for (x1, y1), (x2, y2), dsh in seg:
        o.append(_line(x1, y1, x2, y2, E, 1.2, dsh))
        o.append(_arr(x1 + (x2 - x1) * 0.52, y1 + (y2 - y1) * 0.52,
                      x1 + (x2 - x1) * 0.62, y1 + (y2 - y1) * 0.62, E, "ah25", 0.9))

    # ---- scattering at the two contact points
    for fx in (288, 464):
        for ang in (0.78, 2.36):
            dx, dy = _m.cos(ang) * 34, _m.sin(ang) * 34
            o.append(_arr(fx + dx * 0.32, GT + dy * 0.32, fx + dx, GT + dy,
                          G, "ah25g", 1.0))
        o.append(_arr(fx, GT + 5, fx, 262))

    # ---- detecting element
    o.append(_rect(238, 268, 364, 26, "#e7e2d8", E, 1.3))
    o.append(_lbl(420, 286, "phần tử phát hiện", "tb", "middle"))

    # ---- angle of incidence alpha at the glass-air interface
    o.append(_line(552, 198, 552, 254, S, 0.9, "4 3"))
    o.append(_arc(552, 226, 26, -_m.pi / 2, -_m.pi / 2 - 0.86))
    o.append(_arc(552, 226, 26, -_m.pi / 2, -_m.pi / 2 + 0.86))
    o.append(_lbl(522, 188, "α", "ts", "end"))
    o.append(_lbl(582, 188, "α", "ts", "start"))

    return _fig(svg(680, 310, "".join(o),
                    "Đầu đo xúc giác dựa trên nguyên lý phản xạ toàn phần bị phá vỡ"),
                "Hình 25.9 · Đầu đo xúc giác dựa trên nguyên lý phản xạ toàn phần bị phá vỡ.",
                "Figure 25.9 · Tactile transducer based on the principle of internal reflection.",
                "Màng đàn hồi có các gờ tiếp xúc với tấm dẫn sáng; ánh sáng tán xạ tại chỗ tiếp xúc "
                "và rọi xuống phần tử phát hiện",
                "An elastic membrane whose ridges touch the waveguide; light scatters at the contact "
                "points and falls on the detecting element")


# ---------------------------------------------------------------- 25.10
def fig_25_10():
    o = [_defs()]
    BT, BB = 100, 200
    for bx in (60, 206, 352, 498):
        o.append(_rect(bx, BT, 120, BB - BT, "#6e6e6e", E, 1.3))

    # membrane: web over the blocks, a dome over each slot
    top = [(60, 92), (153, 92), (177, 70), (209, 70), (233, 92), (299, 92),
           (323, 70), (355, 70), (379, 92), (445, 92), (469, 70), (501, 70),
           (525, 92), (618, 92)]
    bot = [(x, y + 8) for x, y in top]
    o.append(_poly(top + bot[::-1], "#dcd7cc", E, 1.3))
    o.append(_lbl(22, 62, "màng đàn hồi", "ts"))
    o.append(_line(58, 66, 70, 88, S, 0.9))

    # light paths across each slot, then the pins that interrupt them
    for sl in (180, 326, 472):
        for yy in (208, 214, 220):
            o.append(_arr(sl + 2, yy, sl + 24, yy, G, "ah25g", 0.9))
        o.append(_rect(sl - 26, 204, 26, 18, "#cfc6b4", E, 1.1))
        o.append(_rect(sl + 26, 204, 26, 18, "#cfc6b4", E, 1.1))
    for cx in (193, 339, 485):
        o.append(_rect(cx - 5, 78, 10, 126, "#1f1f1f", E, 1.0))
    for cx in (339, 485):
        o.append(_arr(cx, 34, cx, 64))

    o.append(_lbl(167, 252, "bộ phát", "ts", "middle"))
    o.append(_lbl(219, 252, "bộ thu", "ts", "middle"))

    return _fig(svg(680, 270, "".join(o),
                    "Nguyên lý hoạt động của đầu đo kiểu chắn sáng"),
                "Hình 25.10 · Nguyên lý hoạt động của đầu đo kiểu chắn sáng.",
                "Figure 25.10 · Principle of operation of an occluder transducer.",
                "Màng đàn hồi mang các chốt thẳng đứng; lực ấn làm chốt hạ xuống cắt chùm sáng "
                "giữa bộ phát và bộ thu",
                "An elastic membrane carrying vertical pins; an applied force drives a pin down "
                "across the light path between emitter and detector")


# ---------------------------------------------------------------- 25.11
def fig_25_11():
    o = [_defs()]
    cx0, cy0 = 340, 100

    def P(i, j, dy=0.0):
        return (cx0 + 150 * (i - j), cy0 + 75 * (i + j) + dy)

    # substrate
    o.append(_poly([P(0, 0, 8), P(1, 0, 8), P(1, 1, 8), P(0, 1, 8)], "#dfe3e9", E, 1.3))
    o.append(_poly([P(1, 0, 8), P(1, 1, 8), (340, 308), (490, 233)], "#ccd2da", E, 1.3))
    o.append(_poly([P(0, 1, 8), P(1, 1, 8), (340, 308), (190, 233)], "#d5dae1", E, 1.3))

    # layers, bottom to top
    lay = [(4, 0.0, "j", "#c6cbd3", 5.0), (3, -16.0, "i", "#aeb4bd", 6.0),
           (2, -32.0, "j", "#8d939c", 7.0), (1, -48.0, "i", "#1f1f1f", 8.0)]
    for _, dy, d, col, wd in lay:
        for t in (0.125, 0.375, 0.625, 0.875):
            if d == "i":
                a, b = P(0, t, dy), P(1, t, dy)
            else:
                a, b = P(t, 0, dy), P(t, 1, dy)
            o.append(_bar(a[0], a[1], b[0], b[1], col, wd))

    # light in / out at the fibre ends
    ux, uy = 0.894, 0.447
    for t in (0.125, 0.375, 0.625, 0.875):
        e = P(1, t, -48)
        o.append(_wavy(e[0] + 4, e[1] + 2, e[0] + 4 + ux * 26, e[1] + 2 + uy * 26))
        e = P(t, 1, -32)
        o.append(_wavy(e[0] - 4, e[1] + 2, e[0] - 4 - ux * 26, e[1] + 2 + uy * 26))

    o.append(_lbl(500, 96, "lớp 1", "ts"))
    o.append(_line(496, 100, 402, 100, S, 0.9))
    o.append(_lbl(176, 86, "lớp 2", "ts", "end"))
    o.append(_line(180, 90, 292, 108, S, 0.9))
    o.append(_lbl(150, 194, "lớp 3", "ts", "end"))
    o.append(_line(154, 190, 224, 156, S, 0.9))
    o.append(_lbl(150, 232, "lớp 4", "ts", "end"))
    o.append(_line(154, 228, 300, 214, S, 0.9))

    return _fig(svg(680, 330, "".join(o),
                    "Đầu đo xúc giác bốn lớp dùng sợi quang"),
                "Hình 25.11 · Đầu đo xúc giác bốn lớp.",
                "Figure 25.11 · A four-layer tactile transducer.",
                "Hai lớp sợi quang hoạt động vuông góc nhau, uốn vi mô do hai lớp sợi gợn sóng "
                "phía dưới gây ra",
                "Two orthogonal layers of active fibres, microbent by the two corrugation layers "
                "beneath them")


# ---------------------------------------------------------------- 25.12
def fig_25_12():
    o = [_defs()]

    # ================= (a) photoelastic transducer
    FT, FB = 140, 250
    o.append(_poly([(150, FT), (560, FT), (500, 96), (90, 96)], "#f2f5f9", E, 1.3))
    o.append(_rect(150, FT, 410, 38, "#e9edf3", E, 1.3))
    o.append(_rect(150, 178, 410, 12, "#2f2f2f", E, 1.2))
    o.append(_rect(150, 190, 410, 60, "#dbe2ec", E, 1.3))
    o.append(_poly([(560, FT), (560, 178), (500, 134), (500, 96)], "#e9edf3", E, 1.2))
    o.append(_poly([(560, 178), (560, 190), (500, 146), (500, 134)], "#2f2f2f", E, 1.1))
    o.append(_poly([(560, 190), (560, FB), (500, 206), (500, 146)], "#dbe2ec", E, 1.2))
    o.append(_line(560, FT, 560, FB, E, 1.3))

    o.append(_lbl(355, 165, "lớp mềm dẻo", "tb", "middle"))
    o.append(_lbl(355, 226, "lớp quang đàn hồi", "tb", "middle"))
    o.append(_lbl(604, 200, "mặt phản xạ", "ts"))
    o.append(_line(600, 198, 566, 186, S, 0.9))

    # dimensions a, b, l, t
    o.append(_dim(132, FT, 132, 178, "a", off=-8))
    o.append(_dim(132, 190, 132, FB, "b", off=-8))
    o.append(_dim(150, 276, 560, 276, "l", off=13, vertical=False))
    o.append(_line(150, FB, 150, 280, S, 0.7))
    o.append(_line(560, FB, 560, 280, S, 0.7))
    o.append(_line(76, 94, 136, 138, S, 1.0))
    o.append(_line(71, 98, 81, 90, S, 1.0))
    o.append(_line(131, 142, 141, 134, S, 1.0))
    o.append(_lbl(86, 122, "t", "ts"))

    # axis triad
    o.append(_arr(600, 118, 632, 118))
    o.append(_arr(600, 118, 616, 104))
    o.append(_arr(600, 118, 600, 150))
    o.append(_lbl(636, 122, "x", "ts"))
    o.append(_lbl(620, 100, "y", "ts"))
    o.append(_lbl(604, 160, "z", "ts"))

    # force application region on the top surface
    o.append(_poly([(385, FT), (465, FT), (420, 107), (340, 107)],
                   "url(#hatch25)", E, 1.2))
    for fx in range(352, 418, 13):
        o.append(_arr(fx, 64, fx, 110, E, "ah25", 1.0))
    o.append(_subs(336, 60, [("F", False), ("y", True)], "end", "ts"))
    o.append(_lbl(336, 78, "vùng đặt lực", "ts", "end"))
    o.append(_line(340, 80, 392, 110, S, 0.9))

    # discrete tactels on the top surface, spacing s
    for tx in (150, 210, 270, 330):
        o.append(_line(tx, 112, tx, 124, E, 1.3))
    o.append(_dim(270, 106, 330, 106, "s", off=-5, vertical=False))
    o.append(_lbl(214, 116, "j−1", "ts", "middle"))
    o.append(_lbl(274, 116, "j", "ts", "middle"))
    o.append(_lbl(334, 116, "j+1", "ts", "middle"))

    # circularly polarised light below the beam
    o.append(_poly([(160, 356), (540, 356), (600, 326), (220, 326)], "#eef2f7", E, 1.2))
    for lx in range(200, 541, 30):
        o.append(_arr(lx, 352, lx, 300, G, "ah25g", 1.0))
    o.append(_lbl(350, 376, "ánh sáng phân cực tròn", "tb", "middle"))

    # ================= (b) circular reflective polariscope
    o.append(_lbl(40, 442, "phân bố lực", "ts", "middle"))
    for yy in (464, 476, 488):
        o.append(_arr(16, yy, 62, yy))
    o.append(_rect(70, 442, 10, 56, "#dfe5ee", E, 1.2))
    o.append(_lbl(75, 512, "đầu đo", "ts", "middle"))

    o.append(_rect(100, 424, 190, 100, "none", S, 1.1, "5 4"))
    o.append(_lbl(195, 558, "kính phân cực tròn", "ts", "middle"))

    o.append(_rect(120, 442, 8, 44, "#dfe5ee", E, 1.2))
    o.append(_lbl(124, 414, "bản λ/4", "ts", "middle"))
    o.append(_rect(180, 446, 40, 40, "#f4f7fa", E, 1.3))
    o.append(_line(180, 446, 220, 486, E, 1.2))
    o.append(_lbl(200, 414, "bộ tách chùm", "ts", "middle"))
    o.append(_rect(256, 442, 8, 56, "#dfe5ee", E, 1.2))
    o.append(_lbl(268, 418, "bộ phân tích", "ts"))

    # monochromatic source, polarizer and their beam into the splitter
    o.append(_arr(210, 506, 210, 486, E, "ah25", 1.0))
    o.append(_rect(188, 490, 44, 8, "#dfe5ee", E, 1.2))
    o.append(_rect(188, 506, 44, 10, "#efe6d4", E, 1.2))
    o.append(_lbl(186, 494, "bộ phân cực", "ts", "end"))
    o.append(_lbl(210, 532, "ánh sáng đơn sắc", "ts", "middle"))

    # beam: out to the transducer, back through the splitter to the camera
    o.append(_arr(180, 474, 132, 474, E, "ah25", 1.0))
    o.append(_arr(120, 474, 82, 474, E, "ah25", 1.0))
    o.append(_arr(82, 480, 120, 480, E, "ah25", 1.0))
    o.append(_arr(128, 480, 180, 480, E, "ah25", 1.0))
    o.append(_arr(220, 480, 256, 480, E, "ah25", 1.0))
    o.append(_arr(264, 480, 300, 480, E, "ah25", 1.0))

    o.append(_rect(300, 452, 52, 48, "#f4f7fa", E, 1.3))
    o.append(_lbl(326, 444, "camera CCD", "ts", "middle"))
    o.append(_line(352, 480, 390, 480, E, 1.2))
    o.append(_rect(390, 452, 44, 48, "#f4f7fa", E, 1.3))
    o.append(_lbl(412, 444, "máy tính", "ts", "middle"))

    o.append(_lbl(350, 392, "(a)", "tb", "middle"))
    o.append(_lbl(350, 578, "(b)", "tb", "middle"))

    return _fig(svg(680, 600, "".join(o),
                    "Đầu đo quang đàn hồi và kính phân cực phản xạ tròn"),
                "Hình 25.12 · (a) Đầu đo quang đàn hồi. (b) Kính phân cực phản xạ tròn.",
                "Figure 25.12 · (a) Photoelastic transducer. (b) Circular reflective polariscope.",
                "Dầm hai lớp có mặt phản xạ ở giữa, và sơ đồ chuỗi quang học của kính phân cực "
                "phản xạ tròn từ nguồn sáng tới máy tính",
                "A two-layer beam with a mirrored surface between the layers, and the optical chain "
                "of a circular reflective polariscope from light source to computer")

FIGS = [fig_25_1, fig_25_2, fig_25_3, fig_25_4,
        fig_25_5, fig_25_6, fig_25_7, fig_25_8,
        fig_25_9, fig_25_10, fig_25_11, fig_25_12]


def fig(n):
    return FIGS[n - 1]()
