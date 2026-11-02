# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 29 — Point Velocity Measurement.

55 source pages, three sections, 31 figures (29.1–29.31) and three tables.
Figures are appended section by section, so a later session can add §29.2 and
§29.3 without touching what is already here.

Geometry is read off the 140 dpi page images in work/ch29img. Where the source
is a photograph or a vendor drawing it is redrawn as a line illustration of the
same object, which is the convention used throughout this handbook.
"""
import math as _m

from hbfig import INK, GOLD, MUTED, TXT, STYLE, _f, svg, _fig

E = INK
G = GOLD
S = MUTED
P = "#ffffff"
FILL = "#f4f6f9"
WARM = "#fdf6ec"
BLUE = "#eef2f7"
DARK = "#111111"


# ------------------------------------------------------------------ primitives
def _lbl(x, y, t, cls="t", anchor="start", extra=""):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s"%s>%s</text>'
            % (cls, _f(x), _f(y), anchor, extra, t))


def _subs(x, y, parts, anchor="start", cls="t"):
    """A label with real subscripts. parts is [(text, is_sub), ...].

    Never write <sub> inside SVG <text>: the HTML parser treats it as a breakout
    from foreign content and the rest of the figure collapses.
    """
    out = []
    for t, is_sub in parts:
        if is_sub:
            out.append('<tspan font-size="8" dy="3">%s</tspan><tspan dy="-3"> </tspan>' % t)
        else:
            out.append(t)
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, "".join(out)))


def _defs():
    return ('<defs>'
            '<marker id="ah29" viewBox="0 0 10 10" refX="8.4" refY="5" '
            'markerWidth="6.4" markerHeight="6.4" orient="auto-start-reverse">'
            '<path d="M0,1.6 L9,5 L0,8.4 z" fill="%s"/></marker>'
            '<marker id="ah29o" viewBox="0 0 10 10" refX="8.4" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M1,5 L8.2,1.6 L8.2,8.4 z" fill="none" stroke="%s" stroke-width="1.1"/>'
            '</marker>'
            '<pattern id="h29" width="7" height="7" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="#c9ced6" stroke-width="1"/></pattern>'
            '<pattern id="w29" width="6" height="6" patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="6" x2="6" y2="0" stroke="#c9ced6" stroke-width=".8"/></pattern>'
            '</defs>' % (E, E))


def _line(x1, y1, x2, y2, col=E, sw=1.4, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _rect(x, y, w, h, fill="none", col=E, sw=1.3, dash=None, rx=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    r = ' rx="%s"' % rx if rx else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, sw, d, r))


def _path(d, col=E, sw=1.4, fill="none", dash=None, cap="round"):
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" '
            'stroke-linecap="%s" stroke-linejoin="round"%s/>' % (d, fill, col, sw, cap, ds))


def _poly(pts, fill="none", col=E, sw=1.3, dash=None):
    d = "M " + " L ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts) + " Z"
    return _path(d, col, sw, fill, dash)


def _circ(cx, cy, r, fill="none", col=E, sw=1.3, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, sw, d))


def _ell(cx, cy, rx, ry, fill="none", col=E, sw=1.3, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(cx), _f(cy), _f(rx), _f(ry), fill, col, sw, d))


def _arr(x1, y1, x2, y2, col=E, marker="ah29", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _carr(d, col=E, sw=1.5, marker="ah29"):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" marker-end="url(#%s)"/>' % (d, col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.1):
    """A dimension line with arrowheads at both ends."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah29)" marker-end="url(#ah29)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _tube(d, w=15, fill=P, col=E):
    """A flow tube drawn from its centreline."""
    return _path(d, col, w) + _path(d, fill, w - 2.6)


def _wall(x, y, w, h, pat="url(#h29)"):
    return _rect(x, y, w, h, pat, E, 1.2)


def _dot(x, y, r=2.6, fill=DARK):
    return _circ(x, y, r, fill, fill, 0.8)


# ------------------------------------------------------------------ 29.1
def fig_29_1():
    """Bernoulli device: inlet, outlet, heat in, shaft work out, two elevations."""
    o = [_defs()]
    # the device
    o.append(_rect(250, 70, 200, 150, P, E, 1.5))
    o.append(_lbl(300, 120, "Any device", "t", "start"))
    o.append(_lbl(300, 134, "through which", "t", "start"))
    o.append(_lbl(300, 148, "a steady flow", "t", "start"))
    o.append(_lbl(300, 162, "exists", "t", "start"))
    # inlet pipe, left
    o.append(_line(120, 152, 250, 152, E, 1.4))
    o.append(_line(120, 176, 250, 176, E, 1.4))
    o.append(_arr(128, 164, 176, 164, E))
    o.append(_lbl(120, 150, "V₁", "t", "start"))
    o.append(_dot(212, 164))
    o.append(_lbl(212, 148, "P₁", "t", "middle"))
    # outlet pipe, top right
    o.append(_line(450, 82, 600, 82, E, 1.4))
    o.append(_line(450, 106, 600, 106, E, 1.4))
    o.append(_arr(470, 94, 520, 94, E))
    o.append(_lbl(452, 76, "P₂", "t", "start"))
    o.append(_lbl(536, 88, "V₂", "t", "start"))
    o.append(_line(450, 70, 450, 82, E, 1.4, dash="4 3"))
    # shaft work out: a pulley with a weight
    o.append(_circ(498, 140, 20, P, E, 1.3))
    o.append(_circ(498, 140, 4, P, E, 1.1))
    o.append(_line(478, 140, 518, 140, E, 1.1))
    o.append(_line(498, 120, 498, 106, E, 1.1))
    o.append(_line(518, 140, 518, 168, E, 1.0))
    o.append(_rect(510, 168, 16, 13, "url(#w29)", E, 1.0))
    o.append(_lbl(524, 138, "Shaft work", "ts", "start"))
    o.append(_lbl(524, 150, "output", "ts", "start"))
    # heat input: a burner under the device
    o.append(_line(350, 220, 350, 268, E, 1.6))
    o.append(_line(336, 268, 364, 268, E, 1.6))
    o.append(_line(336, 276, 364, 276, E, 1.2))
    o.append(_path("M 350,220 q -10,-10 -4,-20 q 8,-8 2,-16", E, 1.2))
    o.append(_path("M 350,220 q 10,-10 4,-20 q -8,-8 -2,-16", E, 1.2))
    o.append(_arr(366, 214, 366, 178, G))
    o.append(_lbl(372, 196, "Net heat", "ts", "start"))
    o.append(_lbl(372, 208, "input", "ts", "start"))
    # elevations
    o.append(_line(110, 300, 620, 300, E, 1.0))
    o.append(_lbl(596, 316, "Datum level", "ts", "start"))
    o.append(_darr(150, 300, 150, 164, E, 1.0))
    o.append(_lbl(140, 236, "Z₁", "t", "end"))
    o.append(_darr(636, 300, 636, 94, E, 1.0))
    o.append(_lbl(646, 200, "Z₂", "t", "start"))
    return _fig(svg(720, 330, "".join(o), "Thiết bị minh hoạ phương trình Bernoulli"),
                "Hình 29.1 · Một thiết bị minh hoạ phương trình Bernoulli cho dòng chảy ổn định, "
                "bỏ qua tổn thất. (Theo [1].)",
                "Figure 29.1 · A device demonstrating Bernoulli’s equation for steady flow, "
                "neglecting losses. (From [1].)",
                "Hộp thiết bị có dòng vào bên trái, dòng ra phía trên bên phải, cấp nhiệt từ dưới "
                "và trục công suất, với hai cao độ Z1 và Z2 so với mặt chuẩn",
                "A device box with an inlet on the left, an outlet at top right, heat input from "
                "below and a shaft output, with elevations Z1 and Z2 above a datum")


def fig_29_2():
    """A Pitot-static assembly read by a mercury U-tube manometer."""
    o = [_defs()]
    cy, r = 100, 36
    # pipe: two walls plus elliptical ends
    o.append(_line(90, cy - r, 620, cy - r, E, 1.4))
    o.append(_line(90, cy + r, 620, cy + r, E, 1.4))
    o.append(_ell(90, cy, 12, r, P, E, 1.2))
    o.append(_ell(620, cy, 12, r, P, E, 1.2))
    o.append(_arr(500, cy, 560, cy, E))
    o.append(_lbl(566, cy - 6, "V", "t", "start"))
    # flow centreline
    o.append(_line(110, cy, 600, cy, S, 0.8, dash="7 5"))
    # point 1: a plain static tap
    o.append(_dot(250, cy))
    o.append(_lbl(250, cy - 12, "1", "t", "middle"))
    o.append(_line(250, cy + r, 250, 262, E, 1.4))
    o.append(_line(250, cy + r, 250, cy + r, E, 1.4))
    # point 2: a Pitot facing the flow, then down
    o.append(_dot(330, cy))
    o.append(_lbl(330, cy - 12, "2", "t", "middle"))
    o.append(_path("M 296,%d L 340,%d L 340,262" % (cy, cy), E, 1.4))
    o.append(_lbl(300, cy - 12, "Pitot", "ts", "middle"))
    o.append(_line(310, cy - 10, 318, cy - 2, S, 0.8))
    # U-tube
    o.append(_path("M 250,262 L 250,300 Q 250,318 268,318 L 322,318 Q 340,318 340,300 L 340,262",
                   E, 1.4))
    # mercury: left column higher than right
    o.append(_rect(244, 236, 12, 76, "url(#h29)", E, 1.0))
    o.append(_rect(334, 268, 12, 44, "url(#h29)", E, 1.0))
    o.append(_path("M 244,312 Q 250,318 262,318 L 328,318 Q 340,318 340,312 L 340,306 "
                   "L 244,306 Z", "url(#h29)", E, 1.0))
    # datum and dimensions
    o.append(_line(200, 318, 420, 318, S, 0.9, dash="5 4"))
    o.append(_darr(216, 318, 216, 236, E, 1.0))
    o.append(_lbl(210, 282, "h₁", "t", "end"))
    o.append(_darr(392, 318, 392, 268, E, 1.0))
    o.append(_lbl(398, 296, "h₂", "t", "start"))
    o.append(_darr(180, 318, 180, cy, E, 1.0))
    o.append(_lbl(174, 214, "h₃", "t", "end"))
    o.append(_darr(372, 236, 372, 268, G, 1.0))
    o.append(_lbl(378, 256, "∆h = 2,5 cm", "ts", "start"))
    o.append(_darr(660, cy - r, 660, cy + r, E, 1.0))
    o.append(_lbl(668, cy + 4, "h = 7,6 cm", "ts", "start"))
    o.append(_line(628, cy - r, 660, cy - r, S, 0.9))
    o.append(_line(628, cy + r, 660, cy + r, S, 0.9))
    o.append(_arr(300, 338, 300, 326, E))
    o.append(_lbl(310, 338, "3", "t", "start"))
    return _fig(svg(720, 360, "".join(o), "Áp kế đo một cụm ống Pitot-tĩnh"),
                "Hình 29.2 · Dùng áp kế để đo một cụm ống Pitot-tĩnh — ví dụ (1).",
                "Figure 29.2 · Using a manometer to measure a Pitot-static tube assembly — "
                "Example (1).",
                "Ống dẫn nằm ngang có hai điểm lấy áp nối xuống một áp kế chữ U thuỷ ngân, "
                "với các độ cao h1, h2, h3 và ∆h",
                "A horizontal pipe with two pressure taps leading down to a mercury U-tube "
                "manometer, with heights h1, h2, h3 and delta h")


def fig_29_3():
    """Flow around a nonrotating body, with the stagnation point marked X."""
    o = [_defs()]
    o.append(_line(60, 58, 660, 58, E, 1.3))
    o.append(_line(60, 262, 660, 262, E, 1.3))
    # the body: a teardrop, nose at x=262, tail at x=512
    o.append(_path("M 262,160 C 276,112 330,104 380,108 C 460,114 500,138 512,160 "
                   "C 500,182 460,206 380,212 C 330,216 276,208 262,160 Z",
                   E, 1.4, "url(#h29)"))
    # streamlines: one continuous path each, bulging over the body
    for y0, peak in ((52, 84), (80, 106), (240, 214), (268, 238)):
        o.append(_path("M 62,%s C 180,%s 250,%s 360,%s C 470,%s 560,%s 658,%s"
                       % (_f(y0), _f(y0), _f(peak - 6), _f(peak), _f(peak),
                          _f(y0), _f(y0)), E, 1.0))
        o.append(_arr(240, y0 + 2, 290, y0 + 4, E))
        o.append(_arr(430, peak + 1, 470, peak + 2, E))
    o.append(_line(62, 160, 258, 160, E, 1.0))
    o.append(_arr(180, 160, 216, 160, E))
    o.append(_lbl(238, 148, "X", "tb", "end"))
    o.append(_dot(258, 160, 2.2))
    return _fig(svg(720, 300, "".join(o), "Dòng chảy quanh một vật rắn không quay"),
                "Hình 29.3 · Dòng chảy quanh một vật rắn không quay.",
                "Figure 29.3 · Flow around a nonrotating solid body.",
                "Vật dạng giọt nước đặt trong ống, các đường dòng tách ra vòng qua vật, "
                "điểm X đánh dấu điểm tới hạn ở mũi vật",
                "A teardrop-shaped body in a duct, streamlines splitting around it, with the "
                "stagnation point X marked at its nose")


def fig_29_4():
    """A right-angle tube dipped into a free stream."""
    o = [_defs()]
    # water body, from the free surface down to the bed
    o.append(_rect(60, 150, 580, 110, "url(#w29)", "none", 0))
    o.append(_line(60, 150, 640, 150, E, 1.2))
    o.append(_line(60, 260, 640, 260, E, 1.2))
    # the tube: vertical run with a 90 degree bend, open end facing left
    o.append(_path("M 366,56 L 366,232 Q 366,244 354,244 L 300,244", E, 16))
    o.append(_path("M 366,56 L 366,232 Q 366,244 354,244 L 300,244", P, 13.4))
    # the liquid column standing above the free surface
    o.append(_rect(359, 58, 14, 92, "url(#h29)", E, 1.0))
    o.append(_darr(404, 62, 404, 150, E, 1.0))
    o.append(_lbl(412, 110, "∆h", "t", "start"))
    o.append(_line(370, 62, 404, 62, S, 0.9))
    # flow in the water
    o.append(_arr(80, 196, 146, 196, E))
    o.append(_lbl(82, 188, "V", "t", "start"))
    o.append(_path("M 70,212 C 180,212 250,212 296,212", E, 1.0))
    o.append(_arr(248, 212, 292, 212, E))
    o.append(_path("M 70,232 C 170,232 236,234 294,236", E, 1.0))
    o.append(_arr(240, 233, 290, 235, E))
    o.append(_lbl(296, 226, "A", "t", "start"))
    o.append(_lbl(120, 246, "dòng chảy", "ts", "start"))
    return _fig(svg(720, 290, "".join(o), "Ống vuông góc trong hệ dòng chảy"),
                "Hình 29.4 · Ống vuông góc trong một hệ dòng chảy.",
                "Figure 29.4 · Right-angle tube in a flow system.",
                "Ống chữ L nhúng trong dòng chảy, đầu hở A hướng vào dòng, cột chất lỏng "
                "dâng cao hơn mặt thoáng một đoạn ∆h",
                "An L-shaped tube dipped into a flow, its open end A facing the stream, with "
                "the liquid column standing a height delta h above the free surface")


def fig_29_5():
    """Pitot’s two-tube method: static, dynamic and total pressure."""
    o = [_defs()]
    o.append(_rect(70, 172, 580, 116, "url(#w29)", "none", 0))
    o.append(_line(70, 172, 650, 172, E, 1.3))
    o.append(_line(70, 288, 650, 288, E, 1.3))
    o.append(_lbl(566, 262, "Water", "ts", "start"))
    # tube 1: static, open at the side
    o.append(_rect(272, 92, 18, 186, P, E, 1.3))
    o.append(_rect(272, 128, 18, 44, "url(#h29)", "none", 0))
    o.append(_line(272, 214, 290, 214, E, 1.3))
    o.append(_lbl(281, 84, "Tube 1", "ts", "middle"))
    # tube 2: total pressure, open at the bottom facing the flow
    o.append(_rect(392, 84, 18, 194, P, E, 1.3))
    o.append(_rect(392, 84, 18, 88, "url(#h29)", "none", 0))
    o.append(_lbl(401, 76, "Tube 2", "ts", "middle"))
    o.append(_line(262, 240, 350, 240, S, 0.9, dash="4 3"))
    o.append(_lbl(356, 244, "Sensing level", "ts", "start"))
    # the three pressure columns
    o.append(_darr(232, 128, 232, 172, E, 1.0))
    o.append(_lbl(226, 154, "Indicated", "ts", "end"))
    o.append(_lbl(226, 166, "static", "ts", "end"))
    o.append(_lbl(226, 178, "pressure", "ts", "end"))
    o.append(_darr(340, 84, 340, 128, G, 1.0))
    o.append(_lbl(266, 104, "Indicated", "ts", "end"))
    o.append(_lbl(266, 116, "dynamic", "ts", "end"))
    o.append(_lbl(266, 128, "pressure", "ts", "end"))
    o.append(_line(270, 110, 336, 110, S, 0.8))
    o.append(_darr(470, 84, 470, 172, E, 1.0))
    o.append(_lbl(478, 132, "Total pressure", "ts", "start"))
    o.append(_arr(88, 250, 148, 250, E))
    o.append(_lbl(90, 242, "FLOW", "ts", "start"))
    return _fig(svg(720, 310, "".join(o), "Phương pháp ống Pitot cơ bản"),
                "Hình 29.5 · Phương pháp ống Pitot cơ bản để cảm nhận áp suất tĩnh, động và toàn phần. "
                "(Theo R. P. Benedict, Fundamentals of Temperature, Pressure and Flow Measurements, "
                "3rd ed., New York: John Wiley & Sons, 1984. With permission.)",
                "Figure 29.5 · Basic Pitot tube method of sensing static, dynamic, and total "
                "pressure. (From R. P. Benedict, Fundamentals of Temperature, Pressure and Flow "
                "Measurements, 3rd ed., New York: John Wiley & Sons, 1984. With permission.)",
                "Hai ống thẳng đứng nhúng trong nước: ống 1 lấy áp tĩnh ở thành bên, ống 2 hướng "
                "vào dòng; mực nước trong hai ống chênh nhau cho biết áp suất động",
                "Two vertical tubes dipped in water: tube 1 senses static pressure at its side, "
                "tube 2 faces the flow; the difference in levels gives the dynamic pressure")


def fig_29_6():
    """A modern Pitot-static probe, sectioned to show the two passages."""
    o = [_defs()]
    o.append(_path("M 556,84 L 444,84 Q 430,84 430,98 L 430,150", E, 22))
    o.append(_path("M 556,84 L 444,84 Q 430,84 430,98 L 430,150", P, 18))
    o.append(_path("M 548,84 L 446,84 Q 438,84 438,98 L 438,168", E, 6))
    o.append(_path("M 548,84 L 446,84 Q 438,84 438,98 L 438,168", P, 3.4))
    # impact hole at the nose
    o.append(_path("M 552,75 L 562,75 L 562,93 L 552,93", E, 1.4))
    o.append(_line(544, 75, 552, 75, E, 1.4))
    o.append(_line(544, 93, 552, 93, E, 1.4))
    o.append(_lbl(566, 62, "IMPACT HOLE", "ts", "start"))
    o.append(_line(566, 66, 560, 78, S, 0.8))
    # static holes on the top surface
    for x in (468, 484, 500, 516):
        o.append(_line(x, 73, x + 7, 73, P, 3.2))
        o.append(_line(x, 73, x + 7, 73, E, 1.6))
    o.append(_lbl(462, 52, "STATIC HOLES", "ts", "start"))
    o.append(_line(478, 56, 478, 70, S, 0.8))
    # flow direction, below the impact hole label
    o.append(_arr(660, 108, 604, 108, E))
    o.append(_lbl(664, 98, "FLOW", "ts", "end"))
    o.append(_lbl(664, 122, "DIRECTION", "ts", "end"))
    # mounting boss on the vertical run
    o.append(_rect(410, 146, 40, 14, "url(#h29)", E, 1.2))
    o.append(_rect(406, 160, 48, 22, P, E, 1.2))
    o.append(_rect(414, 166, 32, 10, "url(#h29)", E, 0.9))
    # static connection, branching left
    o.append(_path("M 430,186 L 430,212 L 384,212 L 384,238", E, 12))
    o.append(_path("M 430,186 L 430,212 L 384,212 L 384,238", P, 9.4))
    o.append(_lbl(376, 244, "STATIC", "ts", "end"))
    o.append(_lbl(376, 256, "CONNECTION", "ts", "end"))
    # impact connection, straight down
    o.append(_path("M 438,186 L 438,250", E, 7))
    o.append(_path("M 438,186 L 438,250", P, 4.2))
    o.append(_lbl(450, 244, "IMPACT", "ts", "start"))
    o.append(_lbl(450, 256, "CONNECTION", "ts", "start"))
    return _fig(svg(720, 290, "".join(o), "Cụm ống Pitot-tĩnh hiện đại"),
                "Hình 29.6 · Một cụm ống Pitot-tĩnh hiện đại. (Theo ASME/ANSI PTC 19.2-1987, "
                "Instruments and Apparatus, Part 2, Pressure Measurements, 1987. With permission.)",
                "Figure 29.6 · A modern Pitot-static tube assembly. (From ASME/ANSI PTC 19.2-1987, "
                "Instruments and Apparatus, Part 2, Pressure Measurements, 1987. With permission.)",
                "Đầu dò chữ L có lỗ động ở mũi và hàng lỗ tĩnh trên mặt trên, hai đường dẫn "
                "áp riêng biệt dẫn xuống hai đầu nối",
                "An L-shaped probe with an impact hole at the nose and a row of static holes on "
                "top, the two pressure passages leading to separate connections")


def fig_29_7():
    """The flow field at a pressure tap: deflection, curvature and an eddy."""
    o = [_defs()]
    o.append(_wall(110, 110, 190, 120))
    o.append(_wall(350, 110, 190, 120))
    o.append(_path("M 60,52 L 250,52 C 300,52 302,68 302,82", E, 1.0))
    o.append(_arr(232, 52, 270, 52, E))
    o.append(_path("M 60,74 L 250,74 C 310,74 314,90 314,98", E, 1.0))
    o.append(_arr(240, 74, 278, 74, E))
    o.append(_path("M 60,96 L 246,96 C 296,96 326,102 326,106", E, 1.0))
    o.append(_arr(234, 96, 272, 96, E))
    o.append(_path("M 660,52 L 420,52 C 370,52 368,68 368,82", E, 1.0))
    o.append(_arr(500, 52, 548, 52, E))
    o.append(_path("M 660,74 L 420,74 C 360,74 356,90 356,98", E, 1.0))
    o.append(_arr(496, 74, 544, 74, E))
    # the eddy, sized to sit inside the 50 px wide hole
    o.append(_carr("M 326,128 a 21,21 0 1 1 2,42", E, 1.2))
    o.append(_carr("M 344,170 a 21,21 0 1 1 -2,-42", E, 1.2))
    return _fig(svg(720, 260, "".join(o), "Trường dòng tại một điểm lấy áp"),
                "Hình 29.7 · Trường dòng tại một điểm lấy áp.",
                "Figure 29.7 · Pressure tap flow field.",
                "Thành ống có lỗ khoan, các đường dòng phía trên bị lệch xuống miệng lỗ và "
                "một xoáy hình thành trong lỗ",
                "A drilled wall with the streamlines above it deflected into the mouth of the "
                "hole and an eddy forming inside it")


def fig_29_8():
    """Total-pressure error against angle of attack for four probe geometries."""
    o = [_defs()]
    x0, y0, w, h = 96, 34, 396, 226

    def mx(v):
        return x0 + w * (v + 40) / 80.0

    def my(v):
        return y0 + h - h * v / 0.7

    o.append(_rect(x0, y0, w, h, P, E, 1.2))
    for v in (-40, -30, -20, -10, 0, 10, 20, 30, 40):
        px = mx(v)
        o.append(_line(px, y0 + h, px, y0 + h + 4, E, 1.0))
        o.append(_lbl(px, y0 + h + 15, "%d" % v, "ts", "middle"))
    for v in (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7):
        py = my(v)
        o.append(_line(x0 - 4, py, x0, py, E, 1.0))
        o.append(_lbl(x0 - 7, py + 3, ("%.1f" % v).replace(".", ","), "ts", "end"))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 32, "Angle of attack, deg", "ts", "middle"))
    o.append('<text class="ts" transform="translate(%s,%s) rotate(-90)" text-anchor="middle">'
             '∆p/q</text>' % (_f(x0 - 42), _f(y0 + h / 2.0)))

    # Four curves, each symmetric in the angle of attack: the error grows with
    # |angle| on both sides, so the plot is a gull wing, not a single ramp.
    amp = [(0.58, "o"), (0.54, "s"), (0.495, "t"), (0.455, "x")]
    for scale, kind in amp:
        pts = []
        for a in (-40, -30, -20, -10, 0, 10, 20, 30, 40):
            f = (abs(a) / 40.0) ** 1.7
            pts.append((a, scale * f))
        d = "M " + " L ".join("%s,%s" % (_f(mx(a)), _f(my(b))) for a, b in pts)
        o.append(_path(d, E, 1.2))
        for a, b in pts:
            if a == 0:
                continue
            px, py = mx(a), my(b)
            if kind == "o":
                o.append(_circ(px, py, 2.8, P, E, 1.0))
            elif kind == "s":
                o.append(_rect(px - 2.6, py - 2.6, 5.2, 5.2, P, E, 1.0))
            elif kind == "t":
                o.append(_poly([(px, py - 3.2), (px + 3, py + 2.2), (px - 3, py + 2.2)], P, E, 1.0))
            else:
                o.append(_line(px - 2.8, py - 2.8, px + 2.8, py + 2.8, E, 1.1))
                o.append(_line(px - 2.8, py + 2.8, px + 2.8, py - 2.8, E, 1.1))
    # legend: the four probe noses, one per row, caption underneath
    lx = 528
    for k, kind in enumerate(("o", "s", "t", "x")):
        yy = 52 + k * 40
        o.append(_path("M %d,%d L %d,%d" % (lx, yy + 12, lx + 22, yy + 12), E, 3.0))
        if kind == "o":
            o.append(_ell(lx + 32, yy + 12, 9, 9, P, E, 1.2))
        elif kind == "s":
            o.append(_poly([(lx + 23, yy + 3), (lx + 41, yy + 3), (lx + 41, yy + 21),
                            (lx + 23, yy + 21)], P, E, 1.2))
        elif kind == "t":
            o.append(_poly([(lx + 23, yy + 3), (lx + 41, yy + 3), (lx + 32, yy + 21)], P, E, 1.2))
        else:
            o.append(_line(lx + 24, yy + 4, lx + 40, yy + 20, E, 1.2))
            o.append(_line(lx + 24, yy + 20, lx + 40, yy + 4, E, 1.2))
    o.append(_lbl(lx + 12, 226, "bốn dạng", "ts", "middle"))
    o.append(_lbl(lx + 12, 238, "đầu dò", "ts", "middle"))
    return _fig(svg(720, 300, "".join(o), "Sai số chỉ thị áp suất toàn phần theo góc tới"),
                "Hình 29.8 · Sự biến thiên của chỉ thị áp suất toàn phần theo góc tới và theo hình học "
                "đầu dò. (Theo ASME/ANSI PTC 19.2-1987, Instruments and Apparatus, Part 2, Pressure "
                "Measurements, 1987. With permission.)",
                "Figure 29.8 · Variation of total pressure indication with angle of attack and "
                "geometry for Pitot tubes. (From ASME/ANSI PTC 19.2-1987, Instruments and "
                "Apparatus, Part 2, Pressure Measurements, 1987. With permission.)",
                "Đồ thị ∆p/q theo góc tới từ −40 đến +40 độ với bốn đường cong đối xứng ứng với "
                "bốn dạng đầu dò khác nhau",
                "A plot of delta p over q against angle of attack from minus 40 to plus 40 "
                "degrees, with four symmetric curves for four probe shapes")


def fig_29_9():
    """The type S Pitot tube: assembly, side view and end view."""
    o = [_defs()]
    # two barrels, bent in opposite directions at the tip
    o.append(_path("M 236,56 L 236,150", E, 13))
    o.append(_path("M 236,56 L 236,150", P, 10.4))
    o.append(_path("M 254,56 L 254,150", E, 13))
    o.append(_path("M 254,56 L 254,150", P, 10.4))
    o.append(_path("M 236,60 L 236,40 Q 236,32 244,32 L 258,32", E, 13))
    o.append(_path("M 236,60 L 236,40 Q 236,32 244,32 L 258,32", P, 10.4))
    o.append(_path("M 254,60 L 254,40 Q 254,32 246,32 L 232,32", E, 13))
    o.append(_path("M 254,60 L 254,40 Q 254,32 246,32 L 232,32", P, 10.4))
    o.append(_lbl(272, 28, "PITOT", "ts", "start"))
    o.append(_line(268, 30, 262, 34, S, 0.8))
    # flange
    o.append(_rect(212, 150, 66, 12, "url(#h29)", E, 1.2))
    o.append(_lbl(206, 158, "FLANGE", "ts", "end"))
    # lower barrels and fittings
    o.append(_path("M 236,162 L 236,240", E, 13))
    o.append(_path("M 236,162 L 236,240", P, 10.4))
    o.append(_path("M 254,162 L 254,240", E, 13))
    o.append(_path("M 254,162 L 254,240", P, 10.4))
    for x in (236, 254):
        o.append(_rect(x - 7, 240, 14, 12, "url(#h29)", E, 1.0))
        o.append(_rect(x - 5, 252, 10, 16, P, E, 1.0))
    o.append(_lbl(280, 206, '3/8" FITTINGS WITH', "ts", "start"))
    o.append(_lbl(280, 218, "TEFLON FERRULES", "ts", "start"))
    o.append(_lbl(280, 258, '3/8" TO 1/4"', "ts", "start"))
    o.append(_lbl(280, 270, "HOSE CONNECTORS", "ts", "start"))
    # side view
    o.append(_lbl(486, 86, "Side View", "ts", "middle"))
    o.append(_path("M 452,110 L 452,180", E, 11))
    o.append(_path("M 452,110 L 452,180", P, 8.4))
    o.append(_path("M 482,110 L 482,180", E, 11))
    o.append(_path("M 482,110 L 482,180", P, 8.4))
    o.append(_line(444, 110, 490, 110, S, 0.9, dash="4 3"))
    o.append(_line(444, 180, 490, 180, S, 0.9, dash="4 3"))
    o.append(_darr(420, 110, 420, 180, E, 0.9))
    o.append(_lbl(414, 148, "d₁, d₂", "ts", "end"))
    o.append(_lbl(496, 114, "A-SIDE PLANE", "ts", "start"))
    o.append(_lbl(496, 180, "B-SIDE PLANE", "ts", "start"))
    # end view
    o.append(_lbl(486, 216, "End View", "ts", "middle"))
    o.append(_path("M 458,230 L 496,230 A 11,11 0 0 1 496,252 L 458,252 Z", P, E, 1.2))
    o.append(_path("M 458,230 L 442,230 A 11,11 0 0 0 442,252 L 458,252", P, E, 1.2))
    o.append(_lbl(478, 244, "A", "ts", "middle"))
    o.append(_lbl(434, 244, "B", "ts", "middle"))
    o.append(_lbl(486, 274, "FACE OPENING PLANES", "ts", "middle"))
    return _fig(svg(720, 300, "".join(o), "Ống Pitot kiểu S"),
                "Hình 29.9 · Ống Pitot kiểu S dùng cho đo dòng khí có các thông số thiết kế đặc thù. "
                "Ví dụ, đường kính ống Dt của đầu dò khí nằm trong khoảng 0,48 đến 0,95 cm. Khoảng "
                "cách từ đáy mỗi nhánh tới mặt phẳng miệng mở, kích thước d₁, d₂, phải bằng nhau và "
                "nằm trong khoảng 1,05 đến 1,50 lần đường kính ngoài Dt. Các miệng mở phải thẳng hàng "
                "như hình vẽ; cấu hình này cho hệ số hiệu chỉnh xấp xỉ 0,84. (Theo EPA, CFR 40 "
                "Part 60, Appendix A — Test Methods, 1 July 1995.)",
                "Figure 29.9 · An S type Pitot tube for use in gas flow measurement will have "
                "specific design parameters. For example, the diameter of the tubing Dt of a gas "
                "probe will be between 0.48 and 0.95 cm. There should be equal distances from the "
                "base of each leg of the Pitot tube to its face opening plane, dimensions d1, d2. "
                "This distance should be between 1.05 and 1.50 times the external tubing diameter, "
                "Dt. The face openings of the Pitot tube should be aligned as shown. This "
                "configuration of the type S Pitot tube results in a correction coefficient of "
                "approximately 0.84. (From EPA, CFR 40 Part 60, Appendix A — Test Methods, "
                "1 July 1995.)",
                "Ống Pitot kiểu S với hai nhánh song song có miệng mở ngược chiều nhau, mặt bích "
                "và các đầu nối, kèm hình chiếu cạnh và hình chiếu đầu",
                "A type S Pitot tube with two parallel legs whose openings face opposite ways, a "
                "flange and hose connectors, with side and end views")


def fig_29_10():
    """A Pitot-static tube in uniform subsonic flow."""
    o = [_defs()]
    o.append(_path("M 330,96 Q 330,86 344,86 L 660,86 L 660,150 L 344,150 Q 330,150 330,140 Z",
                   DARK, DARK, 1.0))
    o.append(_line(330, 118, 660, 118, P, 1.6))
    o.append(_arr(70, 118, 120, 118, E))
    o.append(_lbl(70, 110, "V", "t", "start"))
    o.append(_path("M 60,66 C 200,66 260,74 316,96", E, 1.0))
    o.append(_arr(214, 68, 252, 71, E))
    o.append(_path("M 60,170 C 200,170 260,162 316,140", E, 1.0))
    o.append(_arr(214, 168, 252, 165, E))
    o.append(_dot(150, 118))
    o.append(_lbl(150, 136, "P₁, v₁, T₁", "ts", "middle"))
    o.append(_dot(322, 118, 2.4))
    o.append(_lbl(292, 178, "P₀, v₀, T₀", "ts", "middle"))
    o.append(_line(300, 170, 320, 128, S, 0.8))
    return _fig(svg(720, 200, "".join(o), "Ống Pitot-tĩnh trong dòng dưới âm đều"),
                "Hình 29.10 · Ống Pitot-tĩnh trong dòng dưới âm đều.",
                "Figure 29.10 · Pitot-static tube in uniform subsonic flow.",
                "Đầu dò tù hướng vào dòng, điểm 1 ở thượng nguồn với P1, v1, T1 và điểm 0 tại "
                "mũi với P0, v0, T0",
                "A blunt probe facing the stream, station 1 upstream with P1, v1, T1 and station "
                "0 at the nose with P0, v0, T0")


def fig_29_11():
    """A detached bow shock ahead of the probe in supersonic flow."""
    o = [_defs()]
    o.append(_path("M 360,92 Q 360,82 374,82 L 660,82 L 660,146 L 374,146 Q 360,146 360,136 Z",
                   DARK, DARK, 1.0))
    o.append(_line(360, 114, 660, 114, P, 1.6))
    o.append(_path("M 300,30 C 330,70 336,96 336,114 C 336,132 330,158 300,198", E, 1.8))
    o.append(_lbl(262, 100, "Normal", "ts", "end"))
    o.append(_lbl(262, 112, "shock", "ts", "end"))
    o.append(_line(266, 106, 328, 112, S, 0.8))
    o.append(_lbl(352, 214, "Shock wave", "ts", "start"))
    o.append(_line(346, 208, 330, 180, S, 0.8))
    o.append(_arr(80, 114, 130, 114, E))
    o.append(_lbl(80, 104, "V₁", "t", "start"))
    o.append(_lbl(80, 132, "P₁, M₁", "ts", "start"))
    o.append(_dot(346, 114, 2.4))
    o.append(_lbl(368, 42, "P₂", "ts", "start"))
    o.append(_lbl(368, 54, "M₂", "ts", "start"))
    o.append(_line(370, 46, 350, 110, S, 0.8))
    o.append(_lbl(398, 180, "P₀, T₀", "ts", "start"))
    o.append(_line(402, 172, 376, 148, S, 0.8))
    return _fig(svg(720, 240, "".join(o), "Sóng xung kích tách rời trước ống Pitot"),
                "Hình 29.11 · Sóng xung kích tách rời trước ống Pitot trong dòng trên âm.",
                "Figure 29.11 · Detached bow shock ahead of the Pitot tube in supersonic flow.",
                "Đầu dò tù trong dòng trên âm, một sóng xung kích cong tách rời phía trước mũi, "
                "với các trạng thái P1, M1 và P2, M2",
                "A blunt probe in supersonic flow with a detached curved bow shock ahead of the "
                "nose, showing states P1, M1 and P2, M2")


def fig_29_12():
    """A circular duct section divided into twelve equal areas."""
    o = [_defs()]
    cx, cy, R = 250, 190, 112
    o.append(_circ(cx, cy, R, P, E, 1.3))
    o.append(_circ(cx, cy, R * 0.64, P, E, 1.1))
    o.append(_circ(cx, cy, R * 0.30, P, E, 1.1))
    d = R * 0.7071
    o.append(_line(cx - d, cy - d, cx + d, cy + d, E, 1.0))
    o.append(_line(cx - d, cy + d, cx + d, cy - d, E, 1.0))
    # The distances in the table are measured from one wall, as a percentage of
    # the diameter: x = -R + 2R*pct/100. Measuring them from the centre instead
    # bunches all six points around the middle.
    for pct in (4.4, 14.6, 29.6, 70.4, 85.4, 95.6):
        off = -R + 2 * R * pct / 100.0
        o.append(_dot(cx + off, cy, 2.2))
        o.append(_dot(cx, cy + off, 2.2))
    # the table of traverse points
    tx, ty = 400, 118
    o.append(_line(tx, ty, tx + 190, ty, E, 1.0))
    o.append(_line(tx, ty + 18, tx + 190, ty + 18, E, 1.0))
    o.append(_line(tx, ty + 18 + 6 * 17, tx + 190, ty + 18 + 6 * 17, E, 1.0))
    o.append(_lbl(tx + 6, ty + 12, "Traverse point", "ts", "start"))
    o.append(_lbl(tx + 184, ty + 12, "% of diameter", "ts", "end"))
    for k, pct in enumerate((4.4, 14.6, 29.6, 70.4, 85.4, 95.6)):
        yy = ty + 34 + k * 17
        o.append(_lbl(tx + 30, yy, "%d" % (k + 1), "ts", "middle"))
        o.append(_lbl(tx + 184, yy, ("%.1f" % pct).replace(".", ","), "ts", "end"))
    return _fig(svg(720, 340, "".join(o), "Tiết diện ống tròn chia thành 12 phần bằng nhau"),
                "Hình 29.12 · Ví dụ tiết diện ống khói tròn chia thành 12 phần bằng nhau, có đánh dấu "
                "vị trí các điểm đo.",
                "Figure 29.12 · Example showing circular stack cross-section divided into 12 equal "
                "areas, with location of traverse points indicated.",
                "Mặt cắt tròn có hai vòng tròn đồng tâm và hai đường chéo chia thành 12 phần bằng "
                "nhau, sáu điểm đo trên mỗi đường kính, kèm bảng khoảng cách theo phần trăm "
                "đường kính",
                "A circular section divided into twelve equal areas by two concentric circles and "
                "two diagonals, six traverse points on each diameter, with a table of distances as "
                "a percentage of the diameter")


def fig_29_13():
    """The automated probe and its control case."""
    o = [_defs()]
    # the probe, clear of the case so the two halves do not overlap
    o.append(_path("M 120,150 L 296,150", E, 12))
    o.append(_path("M 120,150 L 296,150", P, 9.4))
    o.append(_path("M 296,150 L 296,110 Q 296,102 304,102 L 322,102", E, 12))
    o.append(_path("M 296,150 L 296,110 Q 296,102 304,102 L 322,102", P, 9.4))
    o.append(_lbl(326, 72, "Type S pitot tube + platinum RTD", "ts", "start"))
    o.append(_line(338, 76, 322, 100, S, 0.8))
    o.append(_dot(320, 102, 3.0))
    o.append(_rect(150, 132, 40, 36, "url(#h29)", E, 1.2))
    o.append(_lbl(170, 186, "Mounting port", "ts", "middle"))
    o.append(_rect(92, 128, 44, 44, P, E, 1.3))
    o.append(_lbl(114, 120, "Longitudinal", "ts", "middle"))
    o.append(_lbl(114, 108, "stepper motor", "ts", "middle"))
    o.append(_rect(150, 196, 44, 34, P, E, 1.3))
    o.append(_lbl(172, 244, "Rotational", "ts", "middle"))
    o.append(_lbl(172, 256, "stepper motor", "ts", "middle"))
    o.append(_circ(252, 150, 7, P, E, 1.1))
    o.append(_lbl(252, 192, "Encoder roller", "ts", "middle"))
    o.append(_path("M 214,150 q 8,-14 16,0 q 8,14 16,0 q 8,-14 16,0", E, 1.2))
    o.append(_lbl(222, 132, "Bellows", "ts", "middle"))
    o.append(_path("M 214,178 C 214,216 280,222 340,222", E, 1.4))
    o.append(_lbl(266, 218, "Data/motor cable", "ts", "middle"))
    # the case
    o.append(_rect(340, 96, 250, 190, P, E, 1.5, rx=10))
    o.append(_lbl(465, 88, "Case assembly", "ts", "middle"))
    boxes = [("Interface", "electronics", "assembly", 356, 112),
             ("High-range", "transducer", "", 436, 112),
             ("Low-range", "transducer", "", 516, 112),
             ("Barometric", "pressure", "sensor", 436, 186),
             ("Vent", "solenoid", "", 516, 186),
             ("Case", "temperature", "sensor", 356, 232),
             ("Case", "heater", "", 466, 240)]
    for a, b, c, bx, by in boxes:
        o.append(_rect(bx, by, 74, 44, BLUE, E, 1.1))
        o.append(_lbl(bx + 37, by + 16, a, "ts", "middle"))
        o.append(_lbl(bx + 37, by + 28, b, "ts", "middle"))
        if c:
            o.append(_lbl(bx + 37, by + 40, c, "ts", "middle"))
    o.append(_rect(340, 200, 22, 16, "url(#h29)", E, 1.0))
    o.append(_lbl(340, 300, "Quick-connect pneumatic couplers", "ts", "start"))
    o.append(_path("M 250,270 C 300,270 320,274 360,274", E, 1.4))
    o.append(_lbl(256, 320, "Stack temperature cable", "ts", "start"))
    return _fig(svg(720, 336, "".join(o), "Đầu dò tự động gồm ống Pitot kiểu S và cảm biến RTD"),
                "Hình 29.13 · Đầu dò tự động gồm một ống Pitot kiểu S và một cảm biến RTD bạch kim "
                "gắn trên một ống thép không gỉ loại 319. (Theo T. C. Elliott, CEM System: Lynchpin "
                "Holding CAA Compliance Together, Power, May 1995, 31–40. With permission.)",
                "Figure 29.13 · Automated probe consists of a type S Pitot tube and a platinum RTD "
                "mounted onto a type 319 stainless steel probe. (From T. C. Elliott, CEM System: "
                "Lynchpin Holding CAA Compliance Together, Power, May 1995, 31–40. With permission.)",
                "Đầu dò dài có ống Pitot kiểu S, hai động cơ bước, cảm biến bạch kim và con lăn "
                "mã hoá, nối cáp tới một hộp điều khiển chứa các bộ chuyển đổi và cảm biến",
                "A long probe with a type S Pitot tube, two stepper motors, a platinum sensor and "
                "an encoder roller, cabled to a control case holding the transducers and sensors")


def fig_29_14():
    """The hybrid acoustic-plus-Pitot system on a stack."""
    o = [_defs()]
    o.append(_path("M 230,64 L 230,296", E, 1.4))
    o.append(_path("M 420,64 L 420,296", E, 1.4))
    o.append(_ell(325, 64, 95, 18, P, E, 1.3))
    o.append(_path("M 230,296 Q 325,314 420,296", E, 1.3, dash="5 4"))
    o.append(_lbl(434, 60, "Stack", "ts", "start"))
    # two transceiver ports on opposite walls
    o.append(_rect(216, 150, 16, 10, "url(#h29)", E, 1.0))
    o.append(_rect(418, 170, 16, 10, "url(#h29)", E, 1.0))
    o.append(_line(232, 155, 270, 178, E, 1.2))
    o.append(_line(418, 175, 380, 198, E, 1.2))
    o.append(_lbl(250, 120, "Transceiver/sensor", "ts", "start"))
    o.append(_lbl(250, 108, "assemblies", "ts", "start"))
    o.append(_line(252, 112, 232, 146, S, 0.8))
    # the acoustic path and the angle it makes
    o.append(_path("M 270,178 L 380,198", E, 1.0, dash="4 3"))
    o.append(_line(270, 178, 270, 212, S, 0.8, dash="4 3"))
    o.append(_path("M 270,198 a 20,20 0 0 1 14,7", E, 1.0))
    o.append(_lbl(292, 204, "θ", "t", "start"))
    # the span
    o.append(_darr(452, 160, 452, 180, E, 1.0))
    o.append(_lbl(460, 174, "Approximate", "ts", "start"))
    o.append(_lbl(460, 186, "one stack", "ts", "start"))
    o.append(_lbl(460, 198, "diameter", "ts", "start"))
    # plant air into the stack
    o.append(_arr(478, 250, 424, 250, E))
    o.append(_lbl(482, 246, "Plant air", "ts", "start"))
    o.append(_lbl(482, 258, "(90–150 psig)", "ts", "start"))
    # signal cable down to the processor
    o.append(_path("M 232,196 C 180,196 168,238 168,262", E, 1.4))
    o.append(_lbl(96, 214, "Signal and", "ts", "start"))
    o.append(_lbl(96, 226, "power cable", "ts", "start"))
    o.append(_rect(470, 268, 78, 42, P, E, 1.3))
    o.append(_lbl(509, 286, "Processor", "ts", "middle"))
    o.append(_lbl(509, 298, "control", "ts", "middle"))
    o.append(_lbl(509, 310, "unit", "ts", "middle"))
    o.append(_path("M 470,289 L 430,289", E, 1.2))
    # outputs leave the processor, not the stack
    o.append(_path("M 509,310 L 509,346", E, 1.2))
    o.append(_path("M 509,346 L 300,346", E, 1.2))
    o.append(_arr(348, 346, 300, 346, E))
    o.append(_lbl(296, 340, "4–20 mA analog", "ts", "end"))
    o.append(_path("M 300,346 L 300,368", E, 1.2))
    o.append(_arr(300, 376, 300, 368, E))
    o.append(_lbl(296, 390, "RS422/485 digital", "ts", "end"))
    o.append(_lbl(308, 390, "To CEM data-logging/computer system", "ts", "start"))
    return _fig(svg(720, 408, "".join(o), "Sơ đồ khối của hệ lai"),
                "Hình 29.14 · Sơ đồ khối của hệ lai.",
                "Figure 29.14 · Block diagram of the hybrid system.",
                "Ống khói mặt cắt có hai cụm đầu dò thu phát đặt đối diện theo một góc θ, nối "
                "tới bộ xử lý và các đầu ra tương tự và số",
                "A sectioned stack with two transceiver assemblies mounted opposite each other at "
                "an angle theta, cabled to a processor with analogue and digital outputs")


def fig_29_15():
    """The acoustic probe: Pitot, static port and acoustic sensor on one shaft."""
    o = [_defs()]
    o.append(_rect(120, 110, 52, 76, P, E, 1.3))
    o.append(_rect(110, 118, 10, 60, "url(#h29)", E, 1.1))
    o.append(_path("M 172,140 L 540,140", E, 13))
    o.append(_path("M 172,140 L 540,140", P, 10.4))
    # the Pitot inside the shaft
    o.append(_path("M 300,150 L 420,150", E, 6))
    o.append(_path("M 300,150 L 420,150", P, 3.4))
    o.append(_path("M 420,144 L 428,144 L 428,156 L 420,156", E, 1.2))
    o.append(_lbl(360, 172, "PITOT TUBE", "ts", "middle"))
    # acoustic sensor at the tip
    o.append(_rect(540, 128, 30, 24, "url(#h29)", E, 1.2))
    o.append(_lbl(556, 112, "HASTALLOY", "ts", "middle"))
    o.append(_lbl(556, 100, "ACOUSTIC SENSOR", "ts", "middle"))
    o.append(_line(556, 104, 556, 126, S, 0.8))
    # static port, in the right order top to bottom
    o.append(_lbl(104, 72, "STATIC", "ts", "end"))
    o.append(_lbl(104, 84, "PRESSURE", "ts", "end"))
    o.append(_lbl(104, 96, "PORT", "ts", "end"))
    o.append(_line(108, 90, 140, 112, S, 0.8))
    # temperature sensor inside the shaft
    o.append(_lbl(300, 96, "TEMPERATURE", "ts", "start"))
    o.append(_lbl(300, 108, "SENSOR INSIDE", "ts", "start"))
    o.append(_line(330, 100, 352, 134, S, 0.8))
    o.append(_lbl(470, 196, "AIR BLAST", "ts", "start"))
    o.append(_line(468, 190, 500, 154, S, 0.8))
    return _fig(svg(720, 230, "".join(o), "Đầu dò âm học chứa cảm biến âm, ống Pitot và cảm biến nhiệt"),
                "Hình 29.15 · Đầu dò âm học chứa cảm biến âm, ống Pitot và cảm biến nhiệt.",
                "Figure 29.15 · Acoustic probe contains acoustic, Pitot, and temperature sensors.",
                "Trục đầu dò xuyên qua thành ống khói, mang theo ống Pitot, cảm biến nhiệt bên "
                "trong và cảm biến âm học hợp kim Hastalloy ở đầu mút",
                "A probe shaft passing through the stack wall, carrying a Pitot tube, an internal "
                "temperature sensor and a Hastalloy acoustic sensor at its tip")


def fig_29_16():
    """The velocity profile across a stack and the path average."""
    o = [_defs()]
    base, top = 246, 90
    x0, x1 = 140, 580
    o.append(_path("M 140,246 A 220,84 0 0 0 580,246", E, 1.3))
    o.append(_line(x0, base, x1, base, E, 1.4))
    prof = [(140, 0.03), (170, 0.42), (200, 0.66), (230, 0.72), (260, 0.60), (290, 0.70),
            (320, 0.78), (350, 0.72), (380, 0.84), (410, 0.90), (440, 0.86), (470, 0.78),
            (500, 0.68), (530, 0.56), (560, 0.40), (580, 0.03)]
    for x, frac in prof:
        y = base - frac * (base - top)
        o.append(_line(x, base, x, y, E, 0.9))
        o.append(_arr(x, y + 8, x, y, E))
    d = "M " + " L ".join("%s,%s" % (_f(x), _f(base - f * (base - top))) for x, f in prof)
    o.append(_path(d, E, 1.5))
    o.append(_line(x0, 132, x1, 132, E, 1.0, dash="7 5"))
    o.append(_lbl(148, 124, "PATH AVERAGE VELOCITY", "ts", "start"))
    o.append(_line(286, 126, 306, 132, S, 0.8))
    o.append(_path("M 148,244 C 240,196 480,196 572,244", S, 1.1, dash="6 5"))
    o.append(_lbl(360, 72, "ACTUAL VELOCITY", "ts", "middle"))
    o.append(_lbl(360, 84, "PROFILE", "ts", "middle"))
    o.append(_line(392, 76, 408, 96, S, 0.8))
    o.append(_lbl(132, 262, "V₁", "t", "end"))
    o.append(_lbl(186, 196, "V₂", "t", "start"))
    o.append(_lbl(536, 196, "V₃", "t", "start"))
    o.append(_lbl(590, 262, "V₄", "t", "start"))
    # legend, below the duct section so it does not sit on the arc
    o.append(_lbl(140, 348, "V₁ = V₄ = 0 at walls", "ts", "start"))
    o.append(_lbl(140, 364, "V₂ = velocity at point, measured by Pitot tube", "ts", "start"))
    o.append(_lbl(140, 380, "V₃ = velocity at diametric point, measured by Pitot tube", "ts", "start"))
    return _fig(svg(720, 396, "".join(o), "Prôfin vận tốc trong một ống khói lớn"),
                "Hình 29.16 · Prôfin vận tốc trong một ống dẫn hoặc ống khói lớn điển hình có thể thay "
                "đổi rất nhiều, do đó làm thay đổi tổng lưu lượng thể tích. Hệ lai giả thiết V₁ và V₄ "
                "bằng không; đo V₂ và V₃ bằng các ống Pitot; và cho giá trị trung bình theo đường đi "
                "(diện tích dưới đường cong) nhờ phần âm học của đầu dò.",
                "Figure 29.16 · The velocity profile in a typical large duct or stack can vary "
                "greatly, thus changing the total volumetric flow. The hybrid system assumes V1 and "
                "V4 to be zero; measures V2 and V3 using the Pitot tubes; and provides the path "
                "average (area under the curve) using the acoustic portions of this sensor.",
                "Prôfin vận tốc dạng răng cưa trên tiết diện ống khói, các mũi tên vận tốc từ đáy "
                "lên đường cong, đường trung bình theo đường đi nằm ngang và cung diện tích dưới "
                "đường cong",
                "A jagged velocity profile across a stack section, velocity arrows from the base up "
                "to the curve, a horizontal path-average line and an arc marking the area under the "
                "curve")


def _pl(pts, col=E, sw=1.4, fill="none", dash=None):
    """Open polyline. _poly closes the path with Z, which is wrong for a
    resistor zigzag or a streamline."""
    d = "M " + " L ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts)
    return _path(d, col, sw, fill, dash)


def _res(x1, y1, x2, y2, n=6, amp=5.5, col=E, sw=1.4):
    """A resistor zigzag along the line from (x1,y1) to (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    L = _m.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    lead = min(9.0, L * 0.16)
    sx, sy = x1 + ux * lead, y1 + uy * lead
    ex, ey = x2 - ux * lead, y2 - uy * lead
    span = L - 2 * lead
    pts = [(x1, y1), (sx, sy)]
    steps = n * 2
    for i in range(1, steps):
        t = i / float(steps)
        s = 1 if i % 2 else -1
        pts.append((sx + ux * span * t + px * amp * s,
                    sy + uy * span * t + py * amp * s))
    pts += [(ex, ey), (x2, y2)]
    return _pl(pts, col, sw)


def _wavy(x1, y1, x2, y2, amp=3.4, waves=4, col=E, sw=1.15):
    """A wavy (heat-flux) arrow. The wave is sampled ten times per period so it
    reads as a curve rather than a sawtooth, and the head is drawn as a triangle
    on the axis so it is not left hanging off the last crest."""
    dx, dy = x2 - x1, y2 - y1
    L = _m.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    body = L - 7.0
    steps = waves * 10
    pts = []
    for i in range(steps + 1):
        t = i / float(steps)
        s = _m.sin(t * _m.pi * 2 * waves) * amp * (1.0 - 0.55 * t)
        pts.append((x1 + ux * body * t + px * s, y1 + uy * body * t + py * s))
    out = _pl(pts, col, sw)
    bx, by = x1 + ux * body, y1 + uy * body
    out += _poly([(x2, y2), (bx + px * 3.2, by + py * 3.2),
                  (bx - px * 3.2, by - py * 3.2)], col, col, 1.0)
    return out


def _rod(x, y1, y2, w=13, coils=0, fill=P):
    """A sheathed sensor rod, optionally with a coil of windings."""
    out = [_rect(x - w / 2.0, y1, w, y2 - y1, fill, E, 1.2, rx=w / 2.0)]
    if coils:
        step = (y2 - y1 - 14) / float(coils)
        for i in range(coils):
            yy = y1 + 8 + i * step
            out.append(_line(x - w / 2.0 + 1.5, yy, x + w / 2.0 - 1.5, yy, E, 0.7))
    return "".join(out)


def _stem(cx, top, w=120, h=56, ry=16):
    """The cylindrical probe stem: an ellipse for the top face, two sides and a
    downward arc for the bottom."""
    r = w / 2.0
    out = [_path("M %s,%s L %s,%s A %s,%s 0 0 0 %s,%s L %s,%s"
                 % (_f(cx - r), _f(top), _f(cx - r), _f(top + h),
                    _f(r), _f(ry), _f(cx + r), _f(top + h), _f(cx + r), _f(top)),
                 E, 1.3, P)]
    out.append(_ell(cx, top, r, ry, P, E, 1.3))
    return "".join(out)


# ------------------------------------------------------------------ 29.2
def fig_29_17():
    """The dual-sensor industrial probe: a heated velocity rod and an unheated
    temperature rod side by side on a cylindrical stem."""
    o = [_defs()]
    o.append(_stem(360, 300, 124, 52, 17))
    o.append(_rod(330, 110, 302, 13, 14))
    o.append(_rod(392, 110, 302, 13, 14))
    # heat leaving the velocity sensor
    o.append(_wavy(334, 104, 372, 58, 2.6, 3))
    o.append(_subs(378, 54, [("q", 0), ("c", 1)]))
    # the two sensor labels, leaders landing on different rods
    o.append(_lbl(250, 56, "Velocity", "t", "start"))
    o.append(_lbl(250, 70, "sensor", "t", "start"))
    o.append(_line(300, 64, 326, 112, E, 0.9))
    o.append(_lbl(470, 56, "Temperature", "t", "start"))
    o.append(_lbl(470, 70, "sensor", "t", "start"))
    o.append(_line(466, 64, 396, 112, E, 0.9))
    o.append(_subs(344, 152, [("T", 0), ("v", 1)]))
    o.append(_subs(404, 152, [("T", 0), ("a", 1)]))
    # probe stem label
    o.append(_lbl(196, 300, "Probe", "t", "start"))
    o.append(_lbl(196, 314, "stem", "t", "start"))
    o.append(_line(244, 306, 296, 330, E, 0.9))
    # active length L
    o.append(_darr(292, 114, 292, 202))
    o.append(_line(292, 114, 322, 114, E, 0.7, dash="3 3"))
    o.append(_line(292, 202, 322, 202, E, 0.7, dash="3 3"))
    o.append(_lbl(284, 162, "L", "t", "end"))
    # mass velocity
    o.append(_arr(238, 262, 300, 224, E, "ah29", 1.6))
    o.append(_subs(232, 276, [("ρU", 0)], anchor="end"))
    return _fig(svg(720, 396, "".join(o), "Đầu dò nhiệt công nghiệp hai cảm biến"),
                "Hình 29.17 · Nguyên lý làm việc của một nhiệt kế gió công nghiệp điển hình. "
                "T<sub>v</sub> là nhiệt độ của cảm biến vận tốc được nung nóng; T<sub>a</sub> là nhiệt "
                "độ khí đo bởi cảm biến nhiệt độ; ρ là khối lượng riêng của khí; U là vận tốc khí; "
                "q<sub>c</sub> là nhiệt được dòng khí mang đi; và L là chiều dài phần đầu được nung "
                "nóng của cảm biến. (In lại theo sự cho phép của Sierra Instruments, Inc.)",
                "Figure 29.17 · The principle of operation of a typical industrial thermal anemometer. "
                "T<sub>v</sub> is the temperature of the heated velocity sensor; T<sub>a</sub> is the "
                "gas temperature measured by the temperature sensor; ρ is the gas mass density; U is "
                "the gas velocity; q<sub>c</sub> is the heat carried away by the flowing gas stream; "
                "and L is the length of the heated tip of the sensor. (Reprinted with permission of "
                "Sierra Instruments, Inc.)",
                "Hai thanh cảm biến thẳng đứng có quấn dây, dựng song song trên một thân trụ tròn; "
                "mũi tên nhiệt lượn sóng bay lên khỏi thanh bên trái, mũi tên ρU hướng vào hai thanh, "
                "kích thước L đánh dấu phần quấn dây",
                "Two vertical wound sensor rods standing side by side on a cylindrical stem; a wavy "
                "heat arrow rises from the left rod, a ρU arrow points at both rods, and an L "
                "dimension marks the wound length")


def fig_29_18():
    """The sensor catalogue: four industrial and four research probe types."""
    o = [_defs()]

    def cell(x, y, w, h):
        return _rect(x, y, w, h, P, "#c9ced6", 1.0)

    def title(y, txt):
        return (_rect(24, y, 672, 24, WARM, E, 1.1)
                + _lbl(360, y + 17, txt, "tb", "middle", ' font-size="10"'))

    # ---------------- industrial panel
    o.append(title(24, "INDUSTRIAL THERMAL SENSORS"))
    o.append(cell(24, 48, 336, 104))
    o.append(cell(360, 48, 336, 104))
    o.append(cell(24, 152, 336, 104))
    o.append(cell(360, 152, 336, 104))

    # A — dual sensor, sheathed
    o.append(_lbl(38, 70, "Dual Sensor,", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 83, "Sheathed", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 100, "Two platinum windings", "ts", "start", ' font-size="8"'))
    o.append(_lbl(38, 111, "in stainless steel sheaths", "ts", "start", ' font-size="8"'))
    o.append(_rod(252, 72, 128, 9, 9))
    o.append(_rod(276, 72, 128, 9, 9))
    o.append(_rect(228, 128, 72, 14, P, E, 1.1))
    o.append(_lbl(258, 68, "Ø3", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(292, 104, "50", "ts", "start", ' font-size="8"'))
    o.append(_lbl(304, 140, "Ø20", "ts", "start", ' font-size="8"'))

    # B — micro-machined / thin film
    o.append(_lbl(374, 70, "Micro-Machined or", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 83, "Thin-Film Sensor", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 100, "Two microelectronic RTDs on", "ts", "start", ' font-size="8"'))
    o.append(_lbl(374, 111, "silicon or alumina chip", "ts", "start", ' font-size="8"'))
    o.append(_rod(596, 92, 128, 6, 0))
    o.append(_rod(614, 92, 128, 6, 0))
    o.append(_rect(574, 128, 62, 12, P, E, 1.1))
    o.append(_lbl(588, 88, "Ø0.5", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(628, 116, "8", "ts", "start", ' font-size="8"'))
    o.append(_lbl(604, 150, "Ø6", "ts", "middle", ' font-size="8"'))

    # C — dual sensor, unsheathed
    o.append(_lbl(38, 174, "Dual Sensor,", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 187, "Unsheathed", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 204, "Two platinum windings,", "ts", "start", ' font-size="8"'))
    o.append(_lbl(38, 215, "glass coated", "ts", "start", ' font-size="8"'))
    o.append(_rod(252, 176, 232, 9, 9))
    o.append(_rod(276, 176, 232, 9, 9))
    o.append(_rect(228, 232, 72, 12, P, E, 1.1))
    o.append(_lbl(258, 172, "Ø1", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(292, 208, "20", "ts", "start", ' font-size="8"'))
    o.append(_lbl(304, 244, "Ø6", "ts", "start", ' font-size="8"'))

    # D — multipoint averaging array
    o.append(_lbl(374, 174, "Multi-Point Flow", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 187, "Averaging Array", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 204, "2 or 4 probes with 1 to 4 dual", "ts", "start", ' font-size="8"'))
    o.append(_lbl(374, 215, "sensors at equal-area centroids", "ts", "start", ' font-size="8"'))
    o.append(_circ(596, 202, 42, P, E, 1.2, dash="5 3"))
    for ang in (25, 65, 115, 155, 205, 245, 295, 335):
        rr = _m.radians(ang)
        o.append(_dot(596 + 26 * _m.cos(rr), 202 - 26 * _m.sin(rr), 1.9))
    o.append(_line(536, 202, 656, 202, E, 1.2))
    o.append(_lbl(536, 194, "U", "ts", "start", ' font-size="8"'))
    o.append(_lbl(500, 254, "Duct wall", "ts", "start", ' font-size="8"'))
    o.append(_line(556, 250, 578, 240, E, 0.8))

    # ---------------- research panel
    o.append(title(264, "RESEARCH THERMAL SENSORS"))
    o.append(cell(24, 288, 336, 100))
    o.append(cell(360, 288, 336, 100))
    o.append(cell(24, 388, 336, 100))
    o.append(cell(360, 388, 336, 100))

    # E — single normal hot-wire: two prongs pointing left, the wire spanning
    # their tips, the body to the right
    o.append(_lbl(38, 310, "Single Normal", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 323, "Hot-Wire Probe", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 340, "Single 5 µm tungsten wire,", "ts", "start", ' font-size="8"'))
    o.append(_lbl(38, 351, "plated at the ends", "ts", "start", ' font-size="8"'))
    o.append(_line(196, 334, 232, 334, E, 1.4))
    o.append(_line(196, 346, 232, 346, E, 1.4))
    o.append(_line(196, 334, 196, 346, E, 1.0))
    o.append(_rect(232, 330, 64, 20, P, E, 1.2))
    o.append(_lbl(206, 326, "2", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(250, 372, "5–8", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(302, 344, "Ø1.5", "ts", "start", ' font-size="8"'))

    # F — X hot-wire: the two wires cross between the prong tips
    o.append(_lbl(374, 310, "“X” Hot-Wire", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 323, "Probe", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 340, "Two perpendicular 5 µm", "ts", "start", ' font-size="8"'))
    o.append(_lbl(374, 351, "tungsten hot wires", "ts", "start", ' font-size="8"'))
    o.append(_line(520, 334, 556, 334, E, 1.4))
    o.append(_line(520, 350, 556, 350, E, 1.4))
    o.append(_line(556, 334, 556, 350, E, 1.0))
    o.append(_line(556, 334, 580, 350, E, 1.0))
    o.append(_line(556, 350, 580, 334, E, 1.0))
    o.append(_rect(580, 330, 42, 24, P, E, 1.2))
    o.append(_lbl(528, 330, "3", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(568, 372, "9", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(628, 346, "Ø2.5", "ts", "start", ' font-size="8"'))

    # G — single hot-film
    o.append(_lbl(38, 410, "Single", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 423, "Hot-Film Probe", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(38, 440, "Quartz-coated platinum film", "ts", "start", ' font-size="8"'))
    o.append(_lbl(38, 451, "0.1 µm thick × 1 mm long", "ts", "start", ' font-size="8"'))
    o.append(_pl([(196, 440), (224, 440), (224, 430), (300, 430)], E, 1.1))
    o.append(_pl([(196, 456), (224, 456), (224, 448), (300, 448)], E, 1.1))
    o.append(_line(300, 430, 300, 448, E, 1.1))
    o.append(_rect(232, 430, 34, 3.6, G, G, 0.6))
    o.append(_lbl(206, 424, "1.5–2", "ts", "start", ' font-size="8"'))
    o.append(_lbl(268, 472, "5", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(306, 442, "Ø2", "ts", "start", ' font-size="8"'))

    # H — 3-D hot-wire
    o.append(_lbl(374, 410, "3-D", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 423, "Hot-Wire Probe", "tb", "start", ' font-size="9.5"'))
    o.append(_lbl(374, 440, "Three orthogonal 5 µm", "ts", "start", ' font-size="8"'))
    o.append(_lbl(374, 451, "tungsten hot wires", "ts", "start", ' font-size="8"'))
    o.append(_pl([(520, 444), (552, 444), (552, 434), (612, 434)], E, 1.1))
    o.append(_pl([(520, 460), (552, 460), (552, 452), (612, 452)], E, 1.1))
    o.append(_line(552, 434, 552, 452, E, 1.1))
    o.append(_line(572, 434, 572, 452, E, 1.0))
    o.append(_line(592, 434, 592, 452, E, 1.0))
    o.append(_line(572, 443, 592, 443, E, 1.0))
    o.append(_lbl(520, 430, "3", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(572, 472, "9", "ts", "middle", ' font-size="8"'))
    o.append(_lbl(618, 446, "Ø4", "ts", "start", ' font-size="8"'))
    return _fig(svg(720, 500, "".join(o), "Các kiểu cảm biến nhiệt công nghiệp và nghiên cứu"),
                "Hình 29.18 · Các cảm biến nhiệt kế gió công nghiệp và nghiên cứu điển hình. Mọi "
                "kích thước tính bằng milimét. T<sub>v</sub> chỉ cảm biến vận tốc được nung nóng; "
                "T<sub>a</sub> chỉ cảm biến nhiệt độ; U là thành phần vận tốc chính theo phương x; "
                "V là thành phần vận tốc ngang theo phương y; và W là thành phần vận tốc ngang theo "
                "phương z.",
                "Figure 29.18 · Typical industrial and research thermal anemometer sensors. All "
                "dimensions are in millimetres. T<sub>v</sub> indicates the heated velocity sensor; "
                "T<sub>a</sub> indicates the temperature sensor; U is the major velocity component in "
                "the x-direction; V is the transverse velocity component in the y-direction; and W is "
                "the transverse velocity component in the z-direction.",
                "Bảng vẽ gồm hai khung, khung trên là bốn kiểu cảm biến công nghiệp và khung dưới là "
                "bốn kiểu cảm biến nghiên cứu, mỗi ô có hình phác đầu dò kèm kích thước",
                "A two-panel plate, four industrial sensor types above and four research types below, "
                "each cell holding a sketch of the probe with its dimensions")


def fig_29_19():
    """First law on the velocity sensor: a cylinder with electric power in,
    convection out, conduction out along the stem."""
    o = [_defs()]
    x1, x2, cy, ry = 200, 440, 180, 48
    o.append(_path("M %d,%d L %d,%d" % (x1, cy - ry, x2, cy - ry), E, 1.4))
    o.append(_path("M %d,%d L %d,%d" % (x1, cy + ry, x2, cy + ry), E, 1.4))
    o.append(_ell(x1, cy, 30, ry, P, E, 1.4))
    # the far end is drawn cut away, hatched to mark a sectioned face
    o.append(_ell(x2, cy, 30, ry, "url(#h29)", E, 1.4))
    # length L
    o.append(_darr(230, 104, 410, 104))
    o.append(_line(230, 104, 230, cy - ry, E, 0.7, dash="3 3"))
    o.append(_line(410, 104, 410, cy - ry, E, 0.7, dash="3 3"))
    o.append(_lbl(320, 98, "L", "t", "middle"))
    # diameter d — the label sits above the top arrowhead so it does not run
    # into the wavy arrow entering the left end
    o.append(_darr(160, cy - ry, 160, cy + ry))
    o.append(_lbl(160, 124, "d", "t", "middle"))
    # electric power in
    o.append(_wavy(84, cy, 142, cy, 3.0, 3))
    o.append(_lbl(76, cy + 4, "w", "t", "end"))
    # convection out of the top surface, clear of the L dimension
    o.append(_wavy(418, cy - 46, 450, 84, 3.0, 3))
    o.append(_subs(456, 80, [("q", 0), ("c", 1)]))
    # conduction out of the far end
    o.append(_wavy(472, cy, 526, cy, 3.0, 3))
    o.append(_subs(534, cy + 4, [("q", 0), ("L", 1)]))
    # surface temperature
    o.append(_subs(452, 116, [("T", 0), ("e", 1)]))
    o.append(_line(450, 120, 440, cy - ry + 4, E, 0.8))
    # flow arrow and gas temperature
    o.append(_arr(320, 292, 368, 250, E, "ah29", 2.0))
    o.append(_lbl(310, 302, "U", "tb", "end"))
    o.append(_subs(376, 262, [("T", 0), ("a", 1)]))
    # the coordinate triad, kept inside the cylinder outline
    o.append(_arr(380, 180, 402, 162, E, "ah29", 1.0))
    o.append(_lbl(406, 160, "x", "ts", "start", ' font-size="9"'))
    o.append(_arr(380, 180, 380, 156, E, "ah29", 1.0))
    o.append(_lbl(380, 150, "z", "ts", "middle", ' font-size="9"'))
    o.append(_arr(380, 180, 358, 188, E, "ah29", 1.0))
    o.append(_lbl(352, 194, "y", "ts", "end", ' font-size="9"'))
    # velocity-sensor leader
    o.append(_lbl(452, 268, "Velocity", "t", "start"))
    o.append(_lbl(452, 282, "sensor", "t", "start"))
    o.append(_line(448, 262, 442, cy + ry - 4, E, 0.8))
    return _fig(svg(720, 330, "".join(o), "Định luật thứ nhất áp dụng cho cảm biến vận tốc"),
                "Hình 29.19 · Định luật thứ nhất của nhiệt động học áp dụng cho cảm biến vận tốc của "
                "nhiệt kế gió. Số hạng w là công suất điện (watt) cấp cho cảm biến; q<sub>c</sub> là "
                "nhiệt đối lưu do dòng khí vận tốc U, nhiệt độ T<sub>a</sub> mang đi; q<sub>L</sub> là "
                "nhiệt dẫn bị mất; T<sub>e</sub> là nhiệt độ bề mặt trung bình của cảm biến trên chiều "
                "dài L; và d là đường kính ngoài của cảm biến.",
                "Figure 29.19 · First law of thermodynamics applied to a thermal anemometer velocity "
                "sensor. The term w is the electric power (watts) supplied to the sensor; "
                "q<sub>c</sub> is the heat convected away by the flowing fluid having a velocity U and "
                "temperature T<sub>a</sub>; q<sub>L</sub> is the conductive heat lost; T<sub>e</sub> is "
                "the average surface temperature of the sensor over its length L; and d is the "
                "sensor’s outside diameter.",
                "Một hình trụ nằm ngang có mặt cắt gạch chéo ở đầu phải; mũi tên nhiệt lượn sóng đi "
                "vào đầu trái, đi ra khỏi mặt trên và đi ra khỏi đầu phải; kích thước L và d được "
                "đánh dấu; mũi tên U hướng lên phía cảm biến",
                "A horizontal cylinder with a hatched section at its right end; wavy heat arrows enter "
                "at the left, leave through the top surface and leave at the right end; L and d are "
                "dimensioned; a U arrow points up at the sensor")


def fig_29_20():
    """Constant-temperature bridge. The two bridge output nodes are labelled and
    the error amplifier takes them as named inputs — routing both wires round a
    diamond bridge would need two crossings, which reads worse than the labels."""
    o = [_defs()]
    A = (340, 80)
    e2 = (250, 200)
    e1 = (430, 200)
    o.append(_res(*A, *e2, n=5, amp=4.5))
    o.append(_res(*A, *e1, n=5, amp=4.5))
    o.append(_res(250, 200, 250, 310, n=5, amp=4.5))
    o.append(_res(430, 200, 430, 310, n=5, amp=4.5))
    o.append(_line(*A, 340, 42, E, 1.3))
    o.append(_dot(*A, 2.4))
    o.append(_dot(*e2, 2.4))
    o.append(_dot(*e1, 2.4))
    # sensor rods
    o.append(_rod(250, 310, 400, 15, 5))
    o.append(_rod(430, 310, 400, 15, 5))
    o.append(_wall(130, 400, 440, 13))
    o.append(_lbl(122, 396, "Duct wall", "ts", "end", ' font-size="9"'))
    o.append(_line(126, 394, 152, 401, E, 0.8))
    # labels
    o.append(_subs(238, 196, [("e", 0), ("2", 1)], anchor="end"))
    o.append(_subs(442, 196, [("e", 0), ("1", 1)]))
    o.append(_subs(284, 136, [("R", 0), ("1", 1)], anchor="end"))
    o.append(_subs(396, 136, [("R", 0), ("2", 1)]))
    o.append(_subs(264, 258, [("R", 0), ("3", 1)]))
    o.append(_subs(416, 258, [("R", 0), ("4", 1)], anchor="end"))
    o.append(_subs(264, 352, [("R", 0), ("v", 1)]))
    o.append(_subs(416, 352, [("R", 0), ("T", 1)], anchor="end"))
    # voltage across the velocity sensor
    o.append(_darr(222, 318, 222, 386))
    o.append(_subs(214, 356, [("E", 0), ("v", 1)], anchor="end"))
    # error amplifier
    o.append(_poly([(580, 172), (580, 242), (646, 207)], P, E, 1.4))
    o.append(_line(552, 188, 580, 188, E, 1.3))
    o.append(_line(552, 226, 580, 226, E, 1.3))
    o.append(_subs(546, 184, [("e", 0), ("2", 1)], anchor="end"))
    o.append(_subs(546, 240, [("e", 0), ("1", 1)], anchor="end"))
    o.append(_lbl(592, 268, "Operational", "ts", "middle", ' font-size="9"'))
    o.append(_lbl(592, 280, "amplifier", "ts", "middle", ' font-size="9"'))
    # output and feedback
    o.append(_line(646, 207, 690, 207, E, 1.3))
    o.append(_line(690, 207, 690, 42, E, 1.3))
    o.append(_line(690, 42, 340, 42, E, 1.3))
    o.append(_lbl(700, 150, "E", "tb", "start"))
    o.append(_lbl(200, 434, "Velocity", "ts", "middle", ' font-size="9"'))
    o.append(_lbl(200, 446, "sensor", "ts", "middle", ' font-size="9"'))
    o.append(_lbl(480, 434, "Temperature", "ts", "middle", ' font-size="9"'))
    o.append(_lbl(480, 446, "sensor", "ts", "middle", ' font-size="9"'))
    return _fig(svg(720, 455, "".join(o), "Mạch cầu của nhiệt kế gió nhiệt độ không đổi"),
                "Hình 29.20 · Mạch cầu Wheatstone của nhiệt kế gió nhiệt độ không đổi, có bù nhiệt độ "
                "tự động. R₁, R₂ và R₄ là các điện trở cố định được chọn để đạt bù nhiệt độ; R₃ là "
                "điện trở đầu dò và cáp; R<sub>v</sub> là điện trở cảm biến vận tốc; R<sub>T</sub> là "
                "điện trở cảm biến nhiệt độ; và E là tín hiệu điện áp ra của cầu. Với nhiệt kế gió "
                "nghiên cứu làm việc trong dòng đẳng nhiệt, cảm biến nhiệt độ được bỏ và thay bằng "
                "một biến trở cầu. Một số mạch bù nhiệt có thêm một điện trở song song với "
                "R<sub>T</sub>.",
                "Figure 29.20 · Constant-temperature thermal anemometer bridge circuit with automatic "
                "temperature compensation. R₁, R₂ and R₄ are fixed resistors selected to achieve "
                "temperature compensation; R₃ is the probe and cable resistance; R<sub>v</sub> is the "
                "velocity sensor’s resistance; R<sub>T</sub> is the temperature sensor’s resistance; "
                "and E is the bridge voltage output signal. For research anemometers operating in "
                "isothermal flows, the temperature sensor is eliminated and replaced with a variable "
                "bridge resistor. Some temperature compensation circuits have an additional resistor "
                "in parallel with R<sub>T</sub>.",
                "Sơ đồ cầu Wheatstone hình thoi với bốn điện trở, hai nhánh cảm biến treo xuống qua "
                "thành ống, khuếch đại thuật toán bên phải và đường hồi tiếp vòng qua đỉnh cầu",
                "A diamond Wheatstone bridge with four resistors, two sensor arms hanging down through "
                "the duct wall, an operational amplifier on the right and a feedback wire running over "
                "the top of the bridge")


def fig_29_21():
    """PC-based research system: five stacked units above the probe."""
    o = [_defs()]
    boxes = [("Personal computer", 36), ("A/D", 100), ("Signal conditioner", 164),
             ("Low-pass filter", 228), ("Anemometer circuit", 292)]
    for name, y in boxes:
        o.append(_rect(260, y, 200, 42, P, E, 1.3))
        o.append(_lbl(360, y + 26, name, "t", "middle"))
    for i in range(len(boxes) - 1):
        o.append(_line(360, boxes[i][1] + 42, 360, boxes[i + 1][1], E, 1.3))
    # probe
    o.append(_rod(336, 334, 420, 14, 5))
    o.append(_rod(384, 334, 420, 14, 5))
    o.append(_wall(190, 420, 370, 13))
    o.append(_lbl(182, 416, "Duct wall", "ts", "end", ' font-size="9"'))
    o.append(_line(184, 414, 300, 421, E, 0.8))
    o.append(_arr(236, 392, 290, 392, E, "ah29", 1.8))
    o.append(_lbl(228, 396, "U", "tb", "end"))
    o.append(_subs(296, 396, [("T", 0), ("a", 1)]))
    o.append(_subs(330, 366, [("R", 0), ("v", 1)], anchor="end"))
    o.append(_subs(390, 366, [("R", 0), ("T", 1)]))
    o.append(_lbl(250, 448, "Velocity", "ts", "start", ' font-size="9"'))
    o.append(_lbl(250, 460, "sensor", "ts", "start", ' font-size="9"'))
    o.append(_line(300, 444, 334, 414, E, 0.8))
    o.append(_lbl(452, 448, "Temperature", "ts", "start", ' font-size="9"'))
    o.append(_lbl(452, 460, "sensor", "ts", "start", ' font-size="9"'))
    o.append(_line(448, 444, 388, 414, E, 0.8))
    return _fig(svg(720, 472, "".join(o), "Hệ nhiệt kế gió số điều khiển bằng máy tính"),
                "Hình 29.21 · Hệ nhiệt kế gió số điều khiển bằng máy vi tính cá nhân. Bộ điều hoà tín "
                "hiệu phối hợp đầu ra của mạch nhiệt kế gió với bộ chuyển đổi A/D. Với dòng đẳng "
                "nhiệt, cảm biến nhiệt độ được bỏ.",
                "Figure 29.21 · Personal computer-based digital thermal anemometer system. The signal "
                "conditioner matches the anemometer circuit’s output to the ADC. For isothermal flows, "
                "the temperature sensor is eliminated.",
                "Năm khối chữ nhật xếp dọc nối với nhau — máy tính, A/D, bộ điều hoà tín hiệu, lọc "
                "thông thấp, mạch nhiệt kế gió — phía dưới là hai thanh cảm biến cắm xuyên thành ống",
                "Five stacked rectangular blocks — computer, A/D, signal conditioner, low-pass filter, "
                "anemometer circuit — with two sensor rods below them passing through the duct wall")


def fig_29_22():
    """Microprocessor-based drive: the constant temperature difference is held
    digitally, so there is no analogue bridge."""
    o = [_defs()]
    o.append(_dot(360, 26, 2.6))
    o.append(_line(360, 26, 360, 44, E, 1.3))
    o.append(_lbl(370, 22, "E", "tb", "start"))
    o.append(_rect(260, 44, 200, 52, P, E, 1.3))
    o.append(_lbl(360, 76, "Microprocessor", "t", "middle"))
    o.append(_line(360, 96, 360, 128, E, 1.3))
    o.append(_rect(260, 128, 200, 46, P, E, 1.3))
    o.append(_lbl(360, 157, "A/D", "t", "middle"))
    o.append(_rod(336, 178, 290, 14, 5))
    o.append(_rod(384, 178, 290, 14, 5))
    o.append(_line(336, 174, 336, 290, E, 1.0))
    o.append(_line(384, 174, 384, 290, E, 1.0))
    o.append(_wall(190, 290, 370, 13))
    o.append(_lbl(182, 286, "Duct wall", "ts", "end", ' font-size="9"'))
    o.append(_line(184, 284, 300, 291, E, 0.8))
    o.append(_arr(236, 262, 290, 262, E, "ah29", 1.8))
    o.append(_lbl(228, 266, "U", "tb", "end"))
    o.append(_subs(296, 266, [("T", 0), ("a", 1)]))
    o.append(_subs(330, 232, [("R", 0), ("v", 1)], anchor="end"))
    o.append(_subs(390, 232, [("R", 0), ("T", 1)]))
    o.append(_lbl(250, 322, "Velocity", "ts", "start", ' font-size="9"'))
    o.append(_lbl(250, 334, "sensor", "ts", "start", ' font-size="9"'))
    o.append(_line(300, 318, 334, 284, E, 0.8))
    o.append(_lbl(452, 322, "Temperature", "ts", "start", ' font-size="9"'))
    o.append(_lbl(452, 334, "sensor", "ts", "start", ' font-size="9"'))
    o.append(_line(448, 318, 388, 284, E, 0.8))
    return _fig(svg(720, 348, "".join(o), "Hệ nhiệt kế gió số dùng vi xử lý"),
                "Hình 29.22 · Nhiệt kế gió số dùng vi xử lý. Hệ này duy trì bằng kỹ thuật số một chênh "
                "lệch nhiệt độ không đổi (T<sub>v</sub> − T<sub>T</sub>) và tự động hiệu chỉnh sự biến "
                "thiên tính chất chất lưu theo nhiệt độ. Nhà sản xuất cung cấp một gói điện tử gắn trên "
                "đầu dò, cho tín hiệu ra tương tự E và/hoặc tín hiệu số RS485 tỉ lệ tuyến tính với vận "
                "tốc khối của khí. (In lại theo sự cho phép của Sierra Instruments, Inc.)",
                "Figure 29.22 · Microprocessor-based digital thermal anemometer. This system digitally "
                "maintains a constant temperature difference (T<sub>v</sub> − T<sub>T</sub>) and "
                "automatically corrects for the variation in fluid properties with temperature. The "
                "manufacturer provides a probe-mounted electronics package delivering an analog output "
                "signal E and/or a digital RS485 signal linearly proportional to gas mass velocity. "
                "(Reprinted with permission of Sierra Instruments, Inc.)",
                "Hai khối chữ nhật — vi xử lý và A/D — nối thẳng đứng, tín hiệu E ở trên cùng, phía "
                "dưới là hai thanh cảm biến xuyên thành ống",
                "Two rectangular blocks — microprocessor and A/D — connected vertically, the output E "
                "at the top, and two sensor rods passing through the duct wall below")


def fig_29_23():
    """Flow calibration curve: bridge voltage against mass velocity. The curve
    is the fitted E = sqrt(A + B·sqrt(U)) through the calibration points."""
    o = [_defs()]
    L, R, T, B = 96, 660, 56, 320

    def X(v):
        return L + v / 140.0 * (R - L)

    def Y(e):
        return B - e / 5.0 * (B - T)

    o.append(_rect(L, T, R - L, B - T, P, E, 1.2))
    for v in range(0, 141, 5):
        o.append(_line(X(v), B, X(v), B - (7 if v % 20 == 0 else 4), E, 1.1))
    for v in range(0, 141, 20):
        o.append(_lbl(X(v), B + 16, str(v), "ts", "middle", ' font-size="9"'))
    for i in range(0, 11):
        e = i * 0.5
        o.append(_line(L, Y(e), L + (7 if i % 2 == 0 else 4), Y(e), E, 1.1))
    for i in range(0, 6):
        o.append(_lbl(L - 12, Y(i) + 4, str(i), "ts", "end", ' font-size="9"'))
    pts = []
    for k in range(0, 261):
        v = k * 0.5
        e = _m.sqrt(0.09 + 1.808 * _m.sqrt(v)) if v > 0 else 0.30
        pts.append((X(v), Y(e)))
    o.append(_pl(pts, E, 1.8))
    for v in range(0, 131, 10):
        e = _m.sqrt(0.09 + 1.808 * _m.sqrt(v)) if v > 0 else 0.30
        o.append(_rect(X(v) - 2.6, Y(e) - 2.6, 5.2, 5.2, E, E, 0.8))
    o.append('<text class="t" x="%s" y="%d" text-anchor="middle">Velocity, U'
             '<tspan font-size="8" dy="3">s</tspan>'
             '<tspan dy="-3"> (normal m/s)</tspan></text>'
             % (_f((L + R) / 2.0), B + 40))
    o.append('<text class="t" x="52" y="%d" text-anchor="middle" transform="rotate(-90 52 %d)">'
             'Bridge voltage, E (volts)</text>' % ((T + B) / 2, (T + B) / 2))
    return _fig(svg(720, 392, "".join(o), "Đường cong hiệu chuẩn lưu lượng điển hình"),
                "Hình 29.23 · Đường cong hiệu chuẩn lưu lượng điển hình của một nhiệt kế gió công "
                "nghiệp. Bộ điện tử điều khiển là bộ trên Hình 29.22. Chênh lệch nhiệt độ không đổi "
                "(T<sub>v</sub> − T<sub>T</sub>) là 50,0 °C. Điện trở nguội R<sub>v0</sub> và "
                "R<sub>T0</sub> của cảm biến vận tốc và cảm biến nhiệt độ ở 20 °C lần lượt khoảng "
                "20 Ω và 200 Ω. (In lại theo sự cho phép của Sierra Instruments, Inc.)",
                "Figure 29.23 · Typical flow calibration curve for an industrial thermal anemometer. "
                "The electronics drive is that shown in Figure 29.22. The constant temperature "
                "difference (T<sub>v</sub> − T<sub>T</sub>) is 50.0 °C. The cold resistances "
                "R<sub>v0</sub> and R<sub>T0</sub> of the velocity and temperature sensors at 20 °C are "
                "approximately 20 Ω and 200 Ω, respectively. (Reprinted with permission of Sierra "
                "Instruments, Inc.)",
                "Đồ thị điện áp cầu theo vận tốc khối, đường cong tăng chậm dần và bão hoà, có các "
                "điểm dấu vuông dọc theo đường cong",
                "A plot of bridge voltage against mass velocity, the curve rising steeply then "
                "flattening, with square markers along it")


# ------------------------------------------------------------------ 29.3
def _mix(x, y, parts, anchor="start", cls="t", extra=""):
    """One <text> element assembled from parts, so a subscript cannot drift away
    from the word it belongs to.

    parts is a list of (text, kind) with kind 'n', 'sub', 'sup' or 'i'. Each
    tspan carries the net dy, so the baseline is restored without the filler
    space that _subs() uses -- a space there leaves a gap before a closing
    bracket, which is visible in a label like "(u_max)".
    """
    out, pend = [], 0
    for t, k in parts:
        dy = -pend
        pend = 0
        fs = ""
        if k == "sub":
            dy += 3
            pend = 3
            fs = _fs(8)
        elif k == "sup":
            dy -= 4
            pend = -4
            fs = _fs(8)
        it = ' font-style="italic"' if k == "i" else ""
        a = (' dy="%d"' % dy if dy else "") + fs + it
        out.append('<tspan%s>%s</tspan>' % (a, t))
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s"%s>%s</text>'
            % (cls, _f(x), _f(y), anchor, extra, "".join(out)))


def _fs(n):
    """An inline font size for a <text> element.

    A presentation attribute is not enough: .t and .ts set the `font` shorthand
    through a class rule, and a class rule beats a presentation attribute, so
    font-size="8" on a <text class="ts"> is silently ignored. An inline style
    wins. On a <tspan> there is no matching rule, so the attribute does work --
    which is why only the element-level sizes need this.
    """
    return ' style="font-size:%spx"' % n


def _rot(x, y, parts, ang, anchor="middle", cls="t", fs=None):
    """_mix rotated about its own anchor, for text that follows a sloping line."""
    extra = ' transform="rotate(%s %s %s)"' % (_f(ang), _f(x), _f(y))
    if fs:
        extra += _fs(fs)
    return _mix(x, y, parts, anchor, cls, extra)


def _burst(x0, x1, base, cx, sigma, amp, period=7.0, step=1.2, col=E, sw=1.0):
    """A Doppler burst: a Gaussian envelope over a sine, drawn as a polyline.

    The sample step is fixed so the crests stay sharp, and the envelope is
    evaluated at every sample so the taper is smooth rather than a triangle.
    """
    pts = []
    x = x0
    while x <= x1:
        env = _m.exp(-((x - cx) / sigma) ** 2)
        pts.append((x, base - amp * env * _m.sin((x - cx) / period * 2 * _m.pi)))
        x += step
    return _pl(pts, col, sw)


def _rnd(n, seed=12345):
    """A deterministic pseudo-random sequence in [0,1).

    Figure 29.29 is a measured trace; a fixed seed keeps the drawing identical
    between builds, so a later screenshot comparison is meaningful.
    """
    out, s = [], seed
    for _ in range(n):
        s = (1103515245 * s + 12345) % 2147483648
        out.append(s / 2147483648.0)
    return out


def _cyl(x, y, w, h, r=6, fill=P, col=E, sw=1.3):
    """A horizontal barrel seen from the side: a capsule, used for the receiver
    and the probe bodies."""
    return ('<path d="M %s,%s L %s,%s A %s,%s 0 0 1 %s,%s L %s,%s A %s,%s 0 0 1 %s,%s Z" '
            'fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(x), _f(y), _f(x + w - h / 2.0), _f(y),
               _f(h / 2.0), _f(h / 2.0), _f(x + w - h / 2.0), _f(y + h),
               _f(x), _f(y + h), _f(h / 2.0), _f(h / 2.0), _f(x), _f(y),
               fill, col, sw))


def _barrel(x, y, w, h, ang, px, py, r=9):
    """A barrel rotated about (px,py), for the receivers that look at an angle."""
    return ('<g transform="rotate(%s %s %s)">%s</g>'
            % (_f(ang), _f(px), _f(py), _cyl(x, y, w, h, r)))


def fig_29_24():
    """The dual-beam LDV: beam splitter, transmitting lens, the crossing where
    the fringes live, receiving optics, and the electronics chain below."""
    o = [_defs()]
    yA, yB, yC = 150, 198, 174          # the two beams and the optical axis
    xc = 398                            # the crossing point

    # laser and beam splitter
    o.append(_line(24, yA - 6, 148, yA - 6, E, 1.5))
    o.append(_line(24, yA + 6, 148, yA + 6, E, 1.5))
    o.append(_lbl(30, yA - 18, "laser beam", "ts", "start", ' font-style="italic"'))
    o.append(_wall(148, 126, 34, 96))
    o.append(_line(182, yA, 286, yA, E, 1.5))
    o.append(_line(182, yB, 286, yB, E, 1.5))

    # beam diameter and beam separation
    o.append(_darr(206, yA - 12, 206, yA))
    o.append(_mix(206, yA - 18, [("D", "n"), ("e-2", "sub")], anchor="middle", cls="ts"))
    o.append(_darr(240, yA, 240, yB))
    o.append(_lbl(248, yC + 4, "d", "t", "start"))

    # transmitting lens and the converging beams
    o.append(_ell(286, yC, 15, 56, P, E, 1.4))
    o.append(_line(301, yA, xc, yC, E, 1.5))
    o.append(_line(301, yB, xc, yC, E, 1.5))
    o.append(_ell(xc, yC, 15, 6, P, E, 1.2))

    # the half-angle 2k, drawn as an arc bulging left from the crossing
    arc = []
    for i in range(0, 17):
        th = _m.radians(166.1 + (193.9 - 166.1) * i / 16.0)
        arc.append((xc + 38 * _m.cos(th), yC - 38 * _m.sin(th)))
    o.append(_pl(arc, E, 1.2))
    o.append('<text class="t" x="354" y="%d" text-anchor="middle">2κ</text>' % (yC + 26))

    # particles, scattered around the measuring volume
    for dx, dy, r in [(-52, -66, 2.4), (-14, -78, 2.0), (26, -62, 2.6),
                      (58, -44, 2.2), (-64, -30, 2.6), (-30, -40, 2.0),
                      (10, -34, 2.4), (46, -22, 2.0), (-58, 30, 2.2),
                      (-22, 44, 2.6), (18, 52, 2.0), (54, 36, 2.4),
                      (-40, 70, 2.2), (6, 76, 2.0), (40, 62, 2.6),
                      (74, 8, 2.2), (-78, 4, 2.0)]:
        o.append(_dot(xc + dx, yC + dy, r, "#555555"))
    o.append(_lbl(296, 268, "particles moving", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(296, 281, "with the fluid", "ts", "start", ' font-style="italic"'))
    o.append(_arr(356, 262, 370, 226, E, "ah29", 1.0))

    # the coordinate triad at the crossing
    o.append(_arr(xc, yC - 8, xc, 74, E, "ah29", 1.4))
    o.append(_lbl(xc + 6, 72, "Y", "t", "start"))
    o.append(_arr(xc + 10, yC, 470, yC, E, "ah29", 1.4))
    o.append(_lbl(474, yC - 6, "X", "t", "start"))

    # receiving optics and the receiver
    o.append(_line(xc + 14, yC - 5, 491, yC - 34, E, 0.8, dash="4 3"))
    o.append(_line(xc + 14, yC + 5, 491, yC + 34, E, 0.8, dash="4 3"))
    o.append(_ell(505, yC, 14, 46, P, E, 1.4))
    o.append(_ell(548, yC, 11, 40, P, E, 1.4))
    o.append(_rect(586, 152, 54, 42, P, E, 1.3))
    o.append(_lbl(613, 214, "Receiver", "ts", "middle"))

    # signal path down to the electronics
    o.append(_pl([(640, 173), (676, 173), (676, 346), (586, 346)], E, 1.3))
    o.append(_arr(520, 346, 492, 346, E, "ah29", 1.4))
    o.append(_arr(404, 346, 376, 346, E, "ah29", 1.4))
    for x, w, t in [(520, 66, "Photodetector"), (404, 84, "Signal processor"),
                    (288, 84, "Data processor")]:
        o.append(_rect(x, 326, w, 40, P, E, 1.3))
        o.append(_lbl(x + w / 2.0, 382, t, "ts", "middle"))

    # the burst and the fringe spacing it encodes
    o.append(_burst(40, 250, 404, 145, 40, 74, 6.6))
    o.append(_line(40, 404, 250, 404, E, 1.0))
    o.append(_mix(40, 316, [("d", "n"), ("f", "sub"), (" = λ ⁄ (2 sin κ)", "n")]))
    return _fig(svg(720, 440, "".join(o), "Sơ đồ hệ hai chùm tia"),
                "Hình 29.24 · Sơ đồ một hệ hai chùm tia. Hai chùm song song cách nhau một khoảng d "
                "được thấu kính hội tụ lại thành một điểm; tại vùng giao nhau chúng tạo thành hệ vân "
                "có khoảng vân d<sub>f</sub>. Ánh sáng tán xạ từ các hạt đi qua vùng đo được thu lại "
                "và đưa tới đầu dò quang.",
                "Figure 29.24 · Schematic of a dual-beam system. Two parallel beams separated by d are "
                "brought to a common focus; in the intersection region they form a fringe pattern of "
                "spacing d<sub>f</sub>. Light scattered by particles crossing the measuring volume is "
                "collected and taken to the photodetector.",
                "Sơ đồ quang học hệ hai chùm tia: chùm laser bị tách thành hai tia song song, qua thấu "
                "kính hội tụ tại một điểm, các hạt tán xạ ánh sáng về phía thấu kính thu, rồi tới bộ "
                "thu và chuỗi xử lý tín hiệu",
                "An optical schematic of a dual-beam system: a laser beam is split into two parallel "
                "beams, focused to a crossing point by a lens, particles scatter light toward a "
                "receiving lens and then a receiver and signal-processing chain")


def fig_29_25():
    """Details of the beam crossing: the optical train, the fringe pattern seen
    across section A-A, and the ellipsoidal measuring volume."""
    o = [_defs()]
    yc = 110

    # --- the optical train, drawn small
    o.append(_wall(40, 88, 26, 44))
    o.append(_line(66, 100, 196, yc, E, 1.2))
    o.append(_line(66, 120, 196, yc, E, 1.2))
    o.append(_ell(120, yc, 10, 34, P, E, 1.2))
    o.append(_ell(196, yc, 11, 5, P, E, 1.0))
    o.append(_line(204, yc - 2, 272, yc - 26, E, 0.8, dash="4 3"))
    o.append(_line(204, yc + 2, 272, yc + 26, E, 0.8, dash="4 3"))
    o.append(_ell(280, yc, 10, 30, P, E, 1.2))
    o.append(_ell(310, yc, 7, 24, P, E, 1.2))
    o.append(_rect(330, 100, 16, 20, P, E, 1.2))
    o.append(_lbl(348, 142, "photodetector", "ts", "middle", _fs(9)))
    for dx, dy in [(-30, -30), (4, -42), (34, -26), (-34, 24), (0, 40), (30, 30)]:
        o.append(_dot(196 + dx, yc + dy, 2.0, "#555555"))

    # section A-A
    o.append(_line(196, 40, 196, 196, E, 0.9, dash="6 4"))
    o.append(_lbl(196, 34, "A", "t", "middle"))
    o.append(_lbl(196, 210, "A", "t", "middle"))

    # coordinate triad
    o.append(_arr(400, 96, 400, 44, E, "ah29", 1.3))
    o.append(_lbl(404, 40, "y", "t", "start"))
    o.append(_arr(400, 96, 460, 96, E, "ah29", 1.3))
    o.append(_lbl(466, 100, "x", "t", "start"))

    # --- the fringe pattern across A-A
    cx, cy, r = 150, 306, 64
    o.append(_circ(cx, cy, r, P, E, 1.4))
    k = -4
    while k <= 4:
        yy = cy + k * 9.0
        half = _m.sqrt(max(r * r - (yy - cy) ** 2, 0))
        if half > 1:
            o.append(_line(cx - half, yy, cx + half, yy, E, 1.3))
        k += 1
    o.append(_darr(cx + r + 10, cy - 4.5, cx + r + 10, cy + 4.5))
    o.append(_mix(cx + r + 16, cy + 8,
                  [("d", "n"), ("f", "sub"), (" = λ ⁄ (2 sin κ)", "n")]))
    o.append(_lbl(cx, 396, "magnified cross", "ts", "middle", ' font-style="italic"'))
    o.append(_lbl(cx, 409, "sectional view at A–A", "ts", "middle", ' font-style="italic"'))

    # --- the measuring volume
    ex, ey = 540, 300
    o.append(_ell(ex, ey, 80, 30, P, E, 1.5))
    for k in range(-4, 5):
        xx = ex + k * 15.0
        half = 30 * _m.sqrt(max(1 - (k * 15.0 / 80) ** 2, 0))
        o.append(_line(xx, ey - half, xx, ey + half, "#9aa0a8", 0.9))
    o.append(_mix(586, 232, [("e", "n"), ("-2", "sup"), (" contour", "n")], cls="ts"))
    o.append(_line(590, 238, 584, 272, E, 0.8, dash="3 3"))
    o.append(_darr(ex - 80, ey + 44, ex + 80, ey + 44))
    o.append(_mix(ex, ey + 38, [("l", "n"), ("m", "sub")], anchor="middle"))
    o.append(_darr(ex + 96, ey - 12, ex + 96, ey + 12))
    o.append(_mix(ex + 102, ey + 4, [("d", "n"), ("m", "sub")]))
    o.append(_lbl(ex, 396, "magnified view of the", "ts", "middle", ' font-style="italic"'))
    o.append(_lbl(ex, 409, "beam intersection region", "ts", "middle", ' font-style="italic"'))

    # the relation between the two
    o.append(_mix(238, 336, [("u", "n"), ("y", "sub"), (" = f", "n"), ("D", "sub"),
                             (" d", "n"), ("f", "sub")], cls="ts"))
    return _fig(svg(720, 424, "".join(o), "Chi tiết vùng giao nhau của hai chùm tia"),
                "Hình 29.25 · Chi tiết vùng giao nhau của hai chùm tia. Hệ vân quan sát trên thiết "
                "diện A–A có khoảng vân d<sub>f</sub> = λ ⁄ (2 sin κ); vùng đo là một khối elipxoit "
                "có đường kính d<sub>m</sub> và chiều dài l<sub>m</sub> xác định theo tiêu chí 1/e². "
                "Vận tốc theo phương y bằng tích của tần số Doppler và khoảng vân.",
                "Figure 29.25 · Details of the beam crossing. The fringe pattern seen across section "
                "A–A has spacing d<sub>f</sub> = λ ⁄ (2 sin κ); the measuring volume is an ellipsoid of "
                "diameter d<sub>m</sub> and length l<sub>m</sub> defined by the 1/e² criterion. The "
                "velocity in the y direction is the product of the Doppler frequency and the fringe "
                "spacing.",
                "Ba phần: sơ đồ quang học nhỏ có thiết diện A–A, mặt cắt phóng to của hệ vân trong "
                "một vòng tròn, và khối elipxoit vùng đo với các kích thước l và d",
                "Three parts: a small optical schematic with a section line A–A, a magnified circular "
                "cross-section of the fringe pattern, and the ellipsoidal measuring volume with its "
                "l and d dimensions")


def fig_29_26():
    """(a) the Bragg cell that imposes the frequency shift; (b) why the shift
    removes the directional ambiguity."""
    o = [_defs()]

    # --- (a) Bragg cell
    o.append(_line(28, 96, 150, 132, E, 1.5))
    o.append(_lbl(24, 88, "laser beam", "ts", "start", ' font-style="italic"'))
    o.append(_rect(150, 60, 86, 150, P, E, 1.4))
    # 12 px between wavefronts, not 7: the acoustic wavelength has to be
    # dimensioned below, and a 7 px span cannot hold two arrowheads without
    # collapsing into a single blob.
    k = 66
    while k < 206:
        o.append(_line(151, k, 235, k, E, 0.9))
        k += 12
    o.append(_rect(150, 50, 86, 11, "url(#h29)", E, 1.2))
    o.append(_lbl(266, 44, "acoustic absorber", "ts", "start", ' font-style="italic"'))
    o.append(_line(262, 50, 240, 56, E, 0.8))

    # acoustic wavelength inside the cell: extension ticks on two neighbouring
    # wavefronts and a dimension between them, so the arrowheads land on the
    # lines the dimension is actually measuring
    o.append(_line(140, 138, 150, 138, E, 0.7))
    o.append(_line(140, 150, 150, 150, E, 0.7))
    o.append(_line(145, 141, 145, 147, E, 0.9))
    o.append('<path d="M145,138 L142.6,141.4 L147.4,141.4 z" fill="%s"/>' % E)
    o.append('<path d="M145,150 L142.6,146.6 L147.4,146.6 z" fill="%s"/>' % E)
    o.append(_lbl(138, 147, "Λ", "t", "end"))

    # the two emergent beams
    o.append(_line(236, 132, 330, 166, E, 1.5))
    o.append(_line(236, 132, 330, 98, E, 1.5))
    o.append(_mix(336, 172, [("ν", "n"), ("0", "sub")]))
    o.append(_mix(336, 94, [("ν", "n"), ("0", "sub"), (" + 40 MHz", "n")]))
    o.append(_pl([(273.6, 118.4), (276.4, 124.0), (277.6, 132.0),
                  (276.4, 140.0), (273.6, 145.6)], E, 1.0))
    o.append(_lbl(284, 136, "2α = λ ⁄ Λ", "ts", "start"))

    # the incident angle
    o.append(_line(116, 132, 152, 132, E, 0.8, dash="4 3"))
    arc = []
    for i in range(0, 9):
        th = _m.radians(180.0 + 16.4 * i / 8.0)
        arc.append((150 + 44 * _m.cos(th), 132 + 44 * _m.sin(th)))
    o.append(_pl(arc, E, 1.0))
    o.append(_lbl(118, 114, "α", "t", "middle"))

    # drive electronics
    o.append(_rect(176, 210, 34, 10, "url(#h29)", E, 1.1))
    o.append(_lbl(218, 222, "transducer", "ts", "start", ' font-style="italic"'))
    o.append(_arr(193, 240, 193, 220, E, "ah29", 1.2))
    o.append(_rect(158, 240, 74, 28, P, E, 1.2))
    o.append(_lbl(195, 252, "Power", "ts", "middle", ' font-style="italic"'))
    o.append(_lbl(195, 264, "amplifier", "ts", "middle", ' font-style="italic"'))
    o.append(_arr(195, 300, 195, 268, E, "ah29", 1.2))
    o.append(_rect(158, 300, 74, 28, P, E, 1.2))
    o.append(_lbl(195, 312, "Local", "ts", "middle", ' font-style="italic"'))
    o.append(_lbl(195, 324, "oscillator", "ts", "middle", ' font-style="italic"'))
    o.append(_lbl(240, 320, "40 MHz", "ts", "start"))
    o.append(_lbl(24, 268, "Λ – wavelength of travelling", "ts", "start", _fs(9)))
    o.append(_lbl(24, 280, "acoustic wave in the cell", "ts", "start", _fs(9)))
    o.append(_lbl(24, 292, "medium", "ts", "start", _fs(9)))
    o.append(_lbl(186, 356, "(a)", "t", "middle"))

    # --- (b) velocity against frequency
    ox, oy, x1 = 480, 300, 706
    sl = 150.0 / 220.0
    o.append(_arr(344, oy, x1, oy, E, "ah29", 1.3))
    o.append(_arr(ox, oy, ox, 60, E, "ah29", 1.3))
    o.append(_lbl(ox, 50, "Frequency", "t", "middle"))
    o.append(_lbl(640, 322, "Velocity", "t", "middle"))
    o.append(_lbl(354, 318, "(–ve)", "ts", "start", ' font-weight="600"'))
    o.append(_mix(440, 318, [("(–u", "n"), ("max", "sub"), (")", "n")],
                  anchor="middle", cls="ts", extra=' font-weight="600"'))
    o.append(_lbl(478, 318, "0", "ts", "end", ' font-weight="600"'))
    o.append(_lbl(662, 318, "(+ve)", "ts", "start", ' font-weight="600"'))

    # the unshifted characteristic: a V through the origin
    o.append(_line(ox, oy, 356, oy - sl * (ox - 356), E, 1.5))
    o.append(_line(ox, oy, x1, oy - sl * (x1 - ox), E, 1.5))
    o.append(_rot(394, 237, [("freq. shift = 0", "n")], 34.3, "middle", "t", "9"))
    o.append(_rot(608, 230, [("freq. shift = 0", "n")], -34.3, "middle", "t", "9"))

    # the shifted characteristic: the same V translated up by f_s
    xv = 420
    o.append(_line(xv, oy, 352, oy - sl * (xv - 352), E, 1.5))
    o.append(_line(xv, oy, x1, oy - sl * (x1 - xv), E, 1.5))
    o.append(_rot(380, 268, [("freq. shift = f", "n"), ("s", "sub")], 34.3, "middle", "t", "9"))
    o.append(_rot(604, 162, [("freq. shift = f", "n"), ("s", "sub")], -34.3, "middle", "t", "9"))

    # the shift itself, and the crossing that sets the rule of thumb
    o.append(_darr(ox, oy, ox, oy - sl * (ox - xv)))
    o.append(_line(450, oy, 450, oy - sl * 30, E, 0.8, dash="4 3"))
    o.append(_lbl(398, 172, "frequency shift", "ts", "start", ' font-style="italic"'))
    o.append(_mix(398, 186, [("(f", "n"), ("s", "sub"), (" ~ 2u", "n"), ("max", "sub"),
                             (" ⁄ d", "n"), ("f", "sub"), (")", "n")],
                  cls="ts", extra=' font-style="italic"'))
    o.append(_carr("M 462,192 Q 476,238 472,272", E, 1.0))
    o.append(_lbl(560, 356, "(b)", "t", "middle"))
    return _fig(svg(720, 372, "".join(o), "Tế bào Bragg và đồ thị vận tốc theo tần số"),
                "Hình 29.26 · (a) Bố trí tế bào Bragg. Sóng âm lan truyền trong tế bào làm lệch một "
                "phần chùm tia và dịch tần số của nó đi 40 MHz. (b) Vận tốc theo tần số: khi chưa "
                "dịch tần, đường đặc trưng là một chữ V qua gốc toạ độ nên không phân biệt được "
                "chiều; dịch tần f<sub>s</sub> nâng đường đặc trưng lên và cho phép đo cả vận tốc âm.",
                "Figure 29.26 · (a) Bragg cell arrangement. An acoustic wave travelling in the cell "
                "deflects part of the beam and shifts its frequency by 40 MHz. (b) Velocity against "
                "frequency: without a shift the characteristic is a V through the origin, so the "
                "direction is ambiguous; a shift f<sub>s</sub> raises the characteristic and makes "
                "negative velocities measurable.",
                "Bên trái là tế bào Bragg với chùm tia tới, hai chùm ra lệch nhau góc 2α, bộ chuyển "
                "đổi và dao động 40 MHz; bên phải là đồ thị có hai đường chữ V, một qua gốc và một "
                "dịch lên trên",
                "On the left a Bragg cell with an incident beam, two emergent beams separated by 2α, "
                "a transducer and a 40 MHz oscillator; on the right a graph with two V-shaped "
                "characteristics, one through the origin and one shifted upward")


def fig_29_27():
    """A fibre-optic LDV probe: two fibres carry the beams to the head, a third
    carries the scattered light back."""
    o = [_defs()]
    yc = 200

    o.append(_rect(24, 250, 62, 30, P, E, 1.3))
    o.append(_lbl(55, 269, "laser", "ts", "middle"))
    o.append(_rect(104, 250, 54, 30, P, E, 1.3))
    o.append(_lbl(131, 269, "couplers", "ts", "middle"))
    o.append(_rect(24, 330, 74, 30, P, E, 1.3))
    o.append(_lbl(61, 349, "photodetector", "ts", "middle", _fs(8)))

    # the probe body
    o.append(_cyl(186, yc - 30, 300, 60, 10, P, E, 1.4))
    o.append(_line(470, yc - 30, 470, yc + 30, E, 1.2))
    o.append(_ell(470, yc, 7, 22, P, E, 1.2))
    o.append(_ell(438, yc, 6, 15, P, E, 1.2))

    # the two delivery fibres and their collimating lenses
    o.append(_rect(196, yc - 18, 12, 9, E, E, 0.8))
    o.append(_rect(196, yc + 9, 12, 9, E, E, 0.8))
    o.append(_ell(238, yc - 13, 4, 9, P, E, 1.1))
    o.append(_ell(238, yc + 13, 4, 9, P, E, 1.1))

    # the beams run collimated to the front lens and are focused after it
    o.append(_line(242, yc - 13, 470, yc - 13, E, 1.4))
    o.append(_line(242, yc + 13, 470, yc + 13, E, 1.4))
    o.append(_line(470, yc - 13, 566, yc, E, 1.4))
    o.append(_line(470, yc + 13, 566, yc, E, 1.4))
    o.append(_ell(566, yc, 12, 5, P, E, 1.1))
    for dx, dy in [(-18, -28), (12, -32), (30, 12), (-8, 28), (26, -8)]:
        o.append(_dot(566 + dx, yc + dy, 2.0, "#555555"))

    # scattered light back through the front lens onto the receiving fibre
    o.append(_line(562, yc - 6, 478, yc - 19, E, 0.9, dash="4 3"))
    o.append(_line(562, yc + 6, 478, yc + 19, E, 0.9, dash="4 3"))
    o.append(_line(462, yc - 15, 446, yc - 7, E, 0.9, dash="4 3"))
    o.append(_line(462, yc + 15, 446, yc + 7, E, 0.9, dash="4 3"))
    o.append(_lbl(606, 158, "scattered light", "ts", "start", ' font-style="italic"'))
    o.append(_line(602, 162, 574, 186, E, 0.8))

    # the fibre runs: two out to the probe, one back to the detector
    o.append(_pl([(158, 258), (172, 258), (172, yc - 13), (192, yc - 13)], E, 1.6))
    o.append(_pl([(158, 272), (180, 272), (180, yc + 13), (192, yc + 13)], E, 1.6))
    o.append(_pl([(446, yc), (446, 300), (160, 300), (160, 345), (100, 345)], E, 1.6))
    o.append(_lbl(156, 326, "to photodetector", "ts", "end", ' font-style="italic"'))

    # leaders
    o.append(_lbl(196, 88, "transmitting fibres", "ts", "start", ' font-style="italic"'))
    o.append(_line(248, 92, 202, yc - 16, E, 0.8, dash="3 3"))
    o.append(_lbl(282, 132, "collimating", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(282, 145, "lenses", "ts", "start", ' font-style="italic"'))
    o.append(_line(294, 150, 242, yc - 7, E, 0.8))
    o.append(_lbl(404, 88, "receiving", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(404, 101, "lens", "ts", "start", ' font-style="italic"'))
    o.append(_line(412, 106, 464, yc - 17, E, 0.8))
    o.append(_lbl(330, 274, "receiving fibre", "ts", "start", ' font-style="italic"'))
    o.append(_line(384, 268, 434, yc + 17, E, 0.8, dash="3 3"))
    return _fig(svg(720, 392, "".join(o), "Sơ đồ bố trí một hệ sợi quang"),
                "Hình 29.27 · Sơ đồ bố trí một hệ sợi quang để đo một thành phần vận tốc. Hai sợi "
                "quang đơn mẫu giữ phân cực dẫn hai chùm tia laser tới đầu dò, nơi chúng được chuẩn "
                "trực và hội tụ; một sợi đa mẫu thu ánh sáng tán xạ ngược và dẫn về đầu dò quang.",
                "Figure 29.27 · Schematic arrangement of a fibre-optic system for measuring one "
                "velocity component. Two single-mode, polarisation-preserving fibres carry the laser "
                "beams to the probe, where they are collimated and focused; a multimode fibre "
                "collects the back-scattered light and carries it to the photodetector.",
                "Sơ đồ hệ sợi quang: hộp laser và bộ ghép nối, các sợi quang dẫn tới một đầu dò hình "
                "trụ nằm ngang có thấu kính chuẩn trực và thấu kính thu, hai chùm tia giao nhau ngoài "
                "đầu dò",
                "A fibre-optic schematic: a laser box and couplers, fibres leading to a horizontal "
                "cylindrical probe containing collimating and receiving lenses, with two beams "
                "crossing outside the probe")


def fig_29_28():
    """Three components from two probes: neither probe is normal to the third
    component, so the two must be set at an angle to each other."""
    o = [_defs()]

    # the duct, with a port in the near wall where the probes come through
    o.append(_wall(140, 46, 460, 9))
    o.append(_wall(140, 228, 130, 9))
    o.append(_wall(470, 228, 130, 9))
    for y in (92, 122, 176, 206):
        o.append(_arr(168, y, 214, y, E, "ah29", 1.0))
        o.append(_arr(526, y, 572, y, E, "ah29", 1.0))
    o.append(_lbl(370, 34, "flow", "ts", "middle", ' font-style="italic"'))

    px, py = 370, 145
    o.append(_ell(px, py, 12, 6, P, E, 1.1))

    # probe 1, entering from the lower left
    o.append('<g transform="rotate(-42.5 300 250)">%s%s</g>'
             % (_cyl(137, 234, 163, 32, 10), _line(287, 238, 287, 262, E, 1.2)))
    o.append(_line(300, 242, px - 4, py + 4, E, 1.2))
    o.append(_line(300, 258, px - 4, py - 4, E, 1.2))
    # probe 2, entering from the lower right
    o.append('<g transform="rotate(42.5 440 250)">%s%s</g>'
             % (_cyl(440, 234, 163, 32, 10), _line(453, 238, 453, 262, E, 1.2)))
    o.append(_line(440, 242, px + 4, py + 4, E, 1.2))
    o.append(_line(440, 258, px + 4, py - 4, E, 1.2))

    # the angle between the two optical axes
    arc = []
    for i in range(0, 13):
        th = _m.radians(56.3 + (123.7 - 56.3) * i / 12.0)
        arc.append((px + 48 * _m.cos(th), py + 48 * _m.sin(th)))
    o.append(_pl(arc, E, 1.1))
    # a raw "<" is not legal in XML text and collapses the whole figure
    o.append(_lbl(px, 214, "θ &lt; 90°", "t", "middle"))

    # the fibres and the electronics they run to
    for x, w, t in [(250, 110, "signal processor"), (380, 96, "computer")]:
        o.append(_rect(x, 390, w, 28, P, E, 1.3))
        o.append(_lbl(x + w / 2.0, 408, t, "ts", "middle"))
    o.append(_arr(360, 404, 380, 404, E, "ah29", 1.2))
    o.append(_pl([(180, 362), (196, 382), (196, 404), (250, 404)], E, 1.5))
    o.append(_pl([(560, 362), (544, 382), (544, 404), (476, 404)], E, 1.5))
    o.append(_lbl(96, 356, "fibres", "ts", "start", ' font-style="italic"'))
    o.append(_line(140, 356, 178, 362, E, 0.8))
    return _fig(svg(720, 430, "".join(o), "Hệ LDV ba thành phần với hai đầu dò sợi quang"),
                "Hình 29.28 · Hệ LDV ba thành phần dùng hai đầu dò sợi quang. Hai đầu dò đặt nghiêng "
                "nhau một góc nhỏ hơn 90° và cùng hướng vào một điểm đo; mỗi đầu dò đo hai thành phần "
                "vận tốc trong mặt phẳng vuông góc với trục quang của nó, và thành phần thứ ba suy ra "
                "từ hình học của cặp đầu dò.",
                "Figure 29.28 · A three-component LDV system using two fibre-optic probes. The two "
                "probes are set at an angle of less than 90° to each other and both look at the same "
                "measuring point; each measures two velocity components in the plane normal to its "
                "optical axis, and the third follows from the geometry of the pair.",
                "Hai đầu dò hình trụ đặt nghiêng vào một ống dẫn có dòng chảy, chùm tia của chúng giao "
                "nhau tại một điểm, góc giữa hai trục quang được đánh dấu, và các sợi quang dẫn xuống "
                "bộ xử lý tín hiệu và máy tính",
                "Two cylindrical probes angled into a duct with a flowing stream, their beams crossing "
                "at one point, the angle between the optical axes marked, and fibres running down to "
                "a signal processor and a computer")


def fig_29_29():
    """The photodetector output: a noisy baseline punctuated by short bursts of
    varying amplitude."""
    o = [_defs()]
    ox, oy, x1, ytop = 80, 250, 580, 44
    base = 196
    o.append(_arr(ox, oy, x1, oy, E, "ah29", 1.3))
    o.append(_arr(ox, oy, ox, ytop, E, "ah29", 1.3))
    o.append(_lbl((ox + x1) / 2.0, 288, "time (millisecs)", "t", "middle",
                  ' font-style="italic"'))
    o.append(_lbl(52, (oy + ytop) / 2.0, "Photodetector output (millivolts)", "ts", "middle",
                  ' font-style="italic" transform="rotate(-90 52 %d)"' % ((oy + ytop) / 2.0)))

    n = _rnd(560, 20240607)
    bursts = [(150, 9, 14), (205, 7, 22), (258, 6, 11), (306, 6, 8),
              (366, 9, 20), (408, 12, 42), (452, 8, 26), (492, 7, 16), (530, 6, 10)]
    pts = []
    for i in range(0, 480):
        x = ox + 8 + i
        y = base - 3.0 * (n[i] - 0.5)
        for c, s, a in bursts:
            env = _m.exp(-((x - c) / s) ** 2)
            y -= a * env * _m.sin((x - c) / 3.0 * 2 * _m.pi)
        pts.append((x, y))
    o.append(_pl(pts, E, 1.0))

    o.append(_lbl(392, 112, "signal bursts", "ts", "start", ' font-style="italic"'))
    o.append(_line(390, 118, 410, 142, E, 0.8, dash="4 3"))
    o.append(_arr(410, 142, 407, 158, E, "ah29", 1.0))
    return _fig(svg(640, 306, "".join(o), "Diễn biến thời gian của tín hiệu đầu dò quang"),
                "Hình 29.29 · Diễn biến thời gian của tín hiệu đầu dò quang. Mỗi lần một hạt đi qua "
                "vùng đo, mức tín hiệu tăng vọt thành một chùm (burst) ngắn; biên độ thay đổi tuỳ theo "
                "quỹ đạo của hạt và tín hiệu chỉ tồn tại gián đoạn, khi có hạt.",
                "Figure 29.29 · Time history of the photodetector signal. Each time a particle passes "
                "through the measuring volume the signal level jumps into a short burst; the amplitude "
                "varies with the particle trajectory, and the signal exists only intermittently, "
                "whenever a particle is present.",
                "Đường tín hiệu nhiễu quanh một mức nền thấp, thỉnh thoảng bật lên thành những chùm "
                "dao động ngắn có biên độ khác nhau",
                "A signal trace noisy about a low baseline, occasionally jumping into short "
                "oscillatory bursts of differing amplitude")


def fig_29_30():
    """(a) the phase Doppler system; (b) the fringe model that explains the
    phase difference between two apertures."""
    o = [_defs()]

    # --- (a) the system
    o.append(_rect(36, 160, 64, 24, P, E, 1.2))
    o.append(_lbl(68, 175, "Power supply", "ts", "middle", _fs(8)))
    o.append(_rect(36, 200, 64, 26, P, E, 1.2))
    o.append(_lbl(68, 217, "Laser", "ts", "middle", _fs(9)))
    o.append(_arr(68, 184, 68, 198, E, "ah29", 1.1))
    o.append(_rect(116, 200, 100, 26, P, E, 1.2))
    o.append(_lbl(166, 217, "Transmitting optics", "ts", "middle", _fs(8)))
    o.append(_line(100, 213, 116, 213, E, 1.2))

    # the probe, fed by a fibre
    o.append(_cyl(224, 186, 150, 26, 8, P, E, 1.3))
    o.append(_wall(224, 186, 24, 26))
    # the fibre that feeds the probe: a single diagonal, because a stepped
    # run under the box reads as a second, stray box at this size
    o.append(_line(216, 214, 226, 204, E, 1.3))
    o.append(_line(374, 192, 418, 196, E, 1.2))
    o.append(_line(374, 206, 418, 200, E, 1.2))
    o.append(_ell(422, 198, 11, 5, P, E, 1.0))
    for dx, dy in [(-18, -24), (12, -30), (28, 10), (-6, 26), (22, -8), (-26, 6)]:
        o.append(_dot(422 + dx, 198 + dy, 2.0, "#555555"))

    # the receiver barrel, aimed at the volume
    o.append(_line(424, 196, 468, 156, E, 0.9, dash="4 3"))
    o.append(_barrel(470, 134, 96, 32, -40, 470, 150))
    o.append(_lbl(560, 116, "scattered light", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(560, 129, "collection system", "ts", "start", ' font-style="italic"'))
    o.append(_line(556, 134, 524, 128, E, 0.8))

    # the electronics chain
    for x, w, t in [(238, 74, "computer"), (324, 92, "signal processor"),
                    (430, 92, "photodetector")]:
        o.append(_rect(x, 44, w, 28, P, E, 1.2))
        o.append(_lbl(x + w / 2.0, 62, t, "ts", "middle", _fs(9)))
    o.append(_arr(430, 58, 416, 58, E, "ah29", 1.1))
    o.append(_arr(324, 58, 312, 58, E, "ah29", 1.1))
    o.append(_pl([(543, 90), (543, 58), (522, 58)], E, 1.2))

    # the burst the detector sees
    o.append(_burst(576, 686, 244, 626, 12, 22, 3.2, 0.8, E, 0.9))
    o.append(_line(576, 244, 686, 244, E, 0.9))
    o.append(_lbl(631, 270, "photodetector output", "ts", "middle", _fs(8)))
    o.append(_lbl(200, 250, "(a)", "t", "middle"))

    # --- (b) the fringe model
    y0, y1 = 300, 372
    o.append(_rect(180, y0, 340, y1 - y0, P, E, 1.3))
    k = y0 + 7
    while k < y1:
        o.append(_line(181, k, 519, k, E, 1.2))
        k += 12
    o.append(_ell(352, (y0 + y1) / 2.0, 20, 15, P, E, 1.3))
    o.append(_dot(352, (y0 + y1) / 2.0, 3.0))
    o.append(_darr(400, y0 + 31, 400, y0 + 43))
    o.append(_mix(406, y0 + 41, [("s", "n"), ("f", "sub")]))
    o.append(_darr(212, y0 + 13, 212, y0 + 61))
    o.append(_mix(218, y0 + 41, [("s", "n"), ("r", "sub")]))
    o.append(_pl([(528, y0), (536, y0), (536, y1), (528, y1)], E, 1.2))
    o.append(_lbl(542, (y0 + y1) / 2.0 - 6, "scattered", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(542, (y0 + y1) / 2.0 + 7, "fringe", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(542, (y0 + y1) / 2.0 + 20, "pattern", "ts", "start", ' font-style="italic"'))

    # the measuring volume that projects the pattern
    vx, vy = 210, 424
    o.append(_ell(vx, vy, 46, 17, P, E, 1.3))
    for k in range(-2, 3):
        o.append(_line(vx + k * 15.0, vy - 13, vx + k * 15.0, vy + 13, "#9aa0a8", 0.9))
    o.append(_line(vx - 44, vy - 15, 184, y1, E, 0.7, dash="4 3"))
    o.append(_line(vx + 44, vy - 15, 300, y1, E, 0.7, dash="4 3"))
    o.append(_lbl(268, 424, "fringe pattern in", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(268, 437, "the measuring volume", "ts", "start", ' font-style="italic"'))
    o.append(_arr(264, 420, 244, 412, E, "ah29", 0.9))
    return _fig(svg(720, 452, "".join(o), "Sơ đồ hệ pha/Doppler và mô hình vân"),
                "Hình 29.30 · (a) Sơ đồ hệ pha/Doppler: hệ thu đặt nghiêng thu ánh sáng tán xạ và "
                "đưa tới nhiều đầu dò quang đặt ở các vị trí khác nhau. (b) Mô hình vân: hạt đi qua "
                "vùng đo chiếu hệ vân ra không gian thành các dải sáng tối có khoảng cách s<sub>f</sub> "
                "trên mặt phẳng thu; hai khe thu cách nhau s<sub>r</sub> nhận hai tín hiệu lệch pha "
                "nhau một góc s<sub>r</sub>⁄s<sub>f</sub> × 360°.",
                "Figure 29.30 · (a) Phase/Doppler system: schematic. The receiver is set at an angle "
                "and delivers the scattered light to several photodetectors at different positions. "
                "(b) The fringe model: a particle crossing the measuring volume projects the fringe "
                "pattern into space as bright and dark bands of spacing s<sub>f</sub> at the receiver "
                "plane; two apertures separated by s<sub>r</sub> receive signals differing in phase by "
                "s<sub>r</sub>⁄s<sub>f</sub> × 360°.",
                "Hai phần: sơ đồ hệ pha Doppler với hộp laser, bộ phát quang, đầu dò, bộ thu nghiêng "
                "và chuỗi điện tử; mô hình vân với dải vân ngang, hạt ở giữa và khối vùng đo chiếu vân "
                "lên trên",
                "Two parts: a phase Doppler schematic with a laser box, transmitting optics, a probe, "
                "an angled receiver and the electronics chain; and a fringe model with a band of "
                "horizontal fringes, a particle inside, and the measuring volume projecting the "
                "fringes upward")


def fig_29_31():
    """(a) the three-aperture receiver that resolves the 2π ambiguity; (b) why
    the wide pair carries the fine count and the narrow pair the coarse one."""
    o = [_defs()]
    cx, cy, r = 150, 150, 100
    o.append(_circ(cx, cy, r, P, E, 1.5))
    # the third aperture, hatched: the circular segment right of the second chord
    o.append(_path("M %s,%s A 100,100 0 0 1 %s,%s L %s,%s Z"
                   % (_f(cx + 42), _f(cy - 90.7), _f(cx + 42), _f(cy + 90.7),
                      _f(cx + 42), _f(cy - 90.7)),
                   E, 1.2, "url(#h29)"))
    o.append(_line(cx - 42, cy - 90.7, cx - 42, cy + 90.7, E, 1.4))
    o.append(_line(cx + 42, cy - 90.7, cx + 42, cy + 90.7, E, 1.4))
    o.append(_lbl(cx - 66, cy + 6, "1", "t", "middle"))
    o.append(_lbl(cx, cy + 6, "2", "t", "middle"))
    o.append(_lbl(cx + 70, cy + 6, "3", "t", "middle"))
    o.append(_lbl(cx, cy + 132, "(a)", "t", "middle"))

    # --- (b) phase against diameter
    ox, oy, x1, ytop = 400, 276, 700, 76
    xr = 680                             # both characteristics end on a wrap
    o.append(_arr(ox - 40, oy, x1, oy, E, "ah29", 1.3))
    o.append(_arr(ox, oy, ox, ytop - 16, E, "ah29", 1.3))
    o.append(_lbl((ox + x1) / 2.0, oy + 30, "Diameter", "t", "middle"))
    o.append(_lbl(356, (oy + ytop) / 2.0, "Phase", "t", "middle",
                  ' transform="rotate(-90 356 %d)"' % ((oy + ytop) / 2.0)))
    o.append(_lbl(ox - 8, ytop + 4, "360", "ts", "end", ' font-weight="600"'))
    o.append(_lbl(ox - 8, oy + 4, "0", "ts", "end", ' font-weight="600"'))
    o.append(_line(ox, ytop, x1, ytop, E, 0.9, dash="3 3"))

    # the fine characteristic, Phi-13: one wrap every 70 px
    x = ox
    while x < xr:
        o.append(_line(x, oy, x + 70, oy - (oy - ytop), E, 1.6))
        if x + 70 < xr:
            o.append(_line(x + 70, oy, x + 70, ytop, E, 0.8, dash="4 3"))
        x += 70
    # the coarse characteristic, Phi-12: one wrap every 140 px
    x = ox
    while x < xr:
        o.append(_line(x, oy, x + 140, oy - (oy - ytop), E, 1.5, dash="7 3 2 3"))
        x += 140

    o.append(_mix(432, 108, [("Φ", "n"), ("13", "sub")], anchor="middle"))
    o.append(_carr("M 436,114 Q 446,150 430,182", E, 1.0))
    # the coarse label has to sit clear of the solid ramps, which cross the
    # whole upper half of the plot
    o.append(_mix(616, 108, [("Φ", "n"), ("12", "sub")], anchor="middle"))
    o.append(_carr("M 622,114 Q 634,118 644,124", E, 1.0))
    o.append(_lbl(560, 324, "(b)", "t", "middle"))
    return _fig(svg(720, 340, "".join(o), "Cấu hình ba đầu dò và quan hệ pha – đường kính"),
                "Hình 29.31 · (a) Cấu hình ba đầu dò: chùm sáng tán xạ được chia qua ba khe 1, 2, 3 "
                "rồi hội tụ vào ba đầu dò quang. (b) Quan hệ pha – đường kính: cặp khe 1–3 có khoảng "
                "cách lớn nên pha Φ<sub>13</sub> biến thiên nhanh theo đường kính và cho độ phân giải "
                "cao, nhưng bị nhập nhằng sau mỗi 2π; cặp 1–2 có pha Φ<sub>12</sub> biến thiên chậm "
                "hơn và được dùng để theo dõi số vòng của Φ<sub>13</sub>.",
                "Figure 29.31 · (a) Three-detector configuration: the scattered light is divided "
                "through three apertures 1, 2, 3 and focused onto three photodetectors. (b) "
                "Phase–diameter relationship: the widely spaced pair 1–3 gives a phase Φ<sub>13</sub> "
                "that changes quickly with diameter and therefore a high resolution, but it is "
                "ambiguous beyond each 2π; the closely spaced pair 1–2 gives a slower Φ<sub>12</sub> "
                "that is used to keep track of the number of wraps of Φ<sub>13</sub>.",
                "Bên trái là mặt thu hình tròn chia thành ba dải đánh số 1, 2, 3; bên phải là đồ thị "
                "pha theo đường kính với hai đường răng cưa có chu kỳ khác nhau và đường 360 độ",
                "On the left a circular receiver face divided into three numbered strips; on the "
                "right a phase-versus-diameter graph with two sawtooth characteristics of different "
                "period and a 360 degree line")


FIGS = [fig_29_1(), fig_29_2(), fig_29_3(), fig_29_4(),
        fig_29_5(), fig_29_6(), fig_29_7(), fig_29_8(),
        fig_29_9(), fig_29_10(), fig_29_11(), fig_29_12(),
        fig_29_13(), fig_29_14(), fig_29_15(), fig_29_16(),
        fig_29_17(), fig_29_18(), fig_29_19(), fig_29_20(),
        fig_29_21(), fig_29_22(), fig_29_23(),
        fig_29_24(), fig_29_25(), fig_29_26(), fig_29_27(),
        fig_29_28(), fig_29_29(), fig_29_30(), fig_29_31()]


def fig(n):
    return FIGS[n - 1]
