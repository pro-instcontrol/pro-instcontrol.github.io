# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 30 — Viscosity Measurement.

24 source pages, one section, 12 figures (30.1–30.12) and four tables.
Geometry is read off the 140 dpi page images in work/ch30img.

House rules that bit us in chapter 29 and apply here:
  * never write <sub>/<sup> inside SVG <text> — use _mix()/_subs() tspans;
  * escape "<" as &lt; anywhere in SVG text;
  * a font-size attribute on <text class="t|ts"> is ignored, because the class
    rule sets the `font` shorthand — use _fs() for an inline style instead;
  * a label rotated to a line's angle needs a perpendicular offset, not a
    vertical one.
"""
import math as _m

from hbfig import INK, GOLD, MUTED, TXT, STYLE, _f, svg, _fig

E = INK
G = GOLD
S = MUTED
P = "#ffffff"
FILL = "#f4f6f9"
DARK = "#111111"


# ------------------------------------------------------------------ primitives
def _lbl(x, y, t, cls="t", anchor="start", extra=""):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s"%s>%s</text>'
            % (cls, _f(x), _f(y), anchor, extra, t))


def _fs(n):
    """An inline font size for a <text> element.

    A presentation attribute is not enough: .t and .ts set the `font` shorthand
    through a class rule, and a class rule beats a presentation attribute, so
    font-size="8" on a <text class="ts"> is silently ignored. An inline style
    wins. On a <tspan> there is no matching rule, so the attribute does work.
    """
    return ' style="font-size:%spx"' % n


def _mix(x, y, parts, anchor="start", cls="t", extra=""):
    """One <text> assembled from parts, so a subscript cannot drift away from
    the symbol it belongs to.

    parts is a list of (text, kind) with kind 'n', 'sub', 'sup' or 'i'. Each
    tspan carries the net dy, so the baseline is restored without the filler
    space that _subs() uses.
    """
    out, pend = [], 0
    for t, k in parts:
        dy = -pend
        pend = 0
        fs = ""
        if k == "sub":
            dy += 3
            pend = 3
            fs = ' font-size="8"'
        elif k == "sup":
            dy -= 4
            pend = -4
            fs = ' font-size="8"'
        it = ' font-style="italic"' if k == "i" else ""
        a = (' dy="%d"' % dy if dy else "") + fs + it
        out.append('<tspan%s>%s</tspan>' % (a, t))
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s"%s>%s</text>'
            % (cls, _f(x), _f(y), anchor, extra, "".join(out)))


def _rot(x, y, parts, ang, anchor="middle", cls="t", fs=None):
    """_mix rotated about its own anchor, for text that follows a sloping line."""
    extra = ' transform="rotate(%s %s %s)"' % (_f(ang), _f(x), _f(y))
    if fs:
        extra += _fs(fs)
    return _mix(x, y, parts, anchor, cls, extra)


def _defs():
    return ('<defs>'
            '<marker id="ah30" viewBox="0 0 10 10" refX="8.4" refY="5" '
            'markerWidth="6.4" markerHeight="6.4" orient="auto-start-reverse">'
            '<path d="M0,1.6 L9,5 L0,8.4 z" fill="%s"/></marker>'
            '<pattern id="h30" width="6" height="6" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#c9ced6" stroke-width="1"/></pattern>'
            '<pattern id="w30" width="5" height="5" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="5" stroke="#8b93a1" stroke-width="1"/></pattern>'
            '<pattern id="d30" width="7" height="7" patternUnits="userSpaceOnUse">'
            '<circle cx="2" cy="2" r="1" fill="#aab2bf"/></pattern>'
            '</defs>' % E)


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


def _pl(pts, col=E, sw=1.3, dash=None):
    d = "M " + " L ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts)
    return _path(d, col, sw, "none", dash)


def _circ(cx, cy, r, fill="none", col=E, sw=1.3, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, sw, d))


def _ell(cx, cy, rx, ry, fill="none", col=E, sw=1.3, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(cx), _f(cy), _f(rx), _f(ry), fill, col, sw, d))


def _arr(x1, y1, x2, y2, col=E, marker="ah30", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _carr(d, col=E, sw=1.4, marker="ah30"):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" marker-end="url(#%s)"/>' % (d, col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.0):
    """A dimension line with arrowheads at both ends."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah30)" marker-end="url(#ah30)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _dot(x, y, r=2.4, fill=DARK):
    return _circ(x, y, r, fill, fill, 0.6)


def _shaft(cx, y1, y2, w=26, fill="url(#h30)"):
    """The driving shaft, drawn as a hatched bar centred on cx."""
    return _rect(cx - w / 2.0, y1, w, y2 - y1, fill, E, 1.2)


def _triad(x, y, size=34, labels=True):
    """x right, z up, y into the page."""
    o = [_arr(x, y, x + size, y), _arr(x, y, x, y - size)]
    o.append(_arr(x, y, x + size * 0.62, y - size * 0.62, sw=1.1))
    if labels:
        o.append(_lbl(x + size + 4, y + 4, "x", "ts", "start"))
        o.append(_lbl(x + 2, y - size - 6, "z", "ts", "middle"))
        o.append(_lbl(x + size * 0.62 + 4, y - size * 0.62 - 2, "y", "ts", "start"))
    return "".join(o)


# ------------------------------------------------------------------ 30.1
def fig_30_1():
    """Newtonian viscosity: two plates, a linear velocity profile between them."""
    o = [_defs()]
    x0, x1 = 250, 560
    ytop, ybot = 88, 208          # inner faces of the two plates
    # the plates
    o.append(_rect(x0, 78, x1 - x0, 10, DARK, E, 1.0))
    o.append(_rect(x0, ybot, x1 - x0, 10, DARK, E, 1.0))
    # the applied force
    o.append(_arr(150, 60, 246, 60, E, sw=1.6))
    o.append(_mix(198, 50, [("F", "i")], anchor="middle"))
    # fluid layers: each starts at x0 and ends on the profile
    n = 7
    for i in range(n + 1):
        y = ytop + (ybot - ytop) * i / float(n)
        xr = x0 + (x1 - x0) * (1 - i / float(n))
        o.append(_line(x0, y, xr, y, E, 1.0))
    # the profile itself
    o.append(_line(x0, ybot, x1, ytop, E, 1.4, dash="5 4"))
    o.append(_rot(492, 150, [("dU", "n"), ("x", "sub"), ("/dz", "n")], -20.4, "middle", "ts"))
    o.append(_mix(x0 - 8, 104, [("U", "n"), ("s", "sub")], anchor="end"))
    o.append(_triad(180, 250, 30))
    return _fig(svg(720, 290, "".join(o), "Hệ hai bản phẳng định nghĩa độ nhớt Newton"),
                "Hình 30.1 · Hệ quy chiếu để định nghĩa độ nhớt Newton. Khi bản trên chịu một lực, "
                "chất lỏng giữa hai bản bị kéo theo phương của lực, vận tốc mỗi lớp giảm dần khi "
                "ra xa bản trên và cuối cùng bằng không tại mặt bản dưới.",
                "Figure 30.1 · System for defining Newtonian viscosity. When the upper plate is "
                "subjected to a force, the fluid between the plates is dragged in the direction of "
                "the force, the velocity of each layer diminishing away from the upper plate and "
                "reaching zero at the lower plate.",
                "Hai bản phẳng nằm ngang, bản trên chịu lực F; giữa hai bản là các lớp chất lỏng "
                "dài ngắn khác nhau, đầu mút phải của chúng nằm trên một đường bao nghiêng, kèm "
                "hệ trục toạ độ x, y, z",
                "Two horizontal plates, the upper one loaded by a force F, with fluid layers of "
                "decreasing length between them whose right-hand ends lie on a sloping envelope, "
                "and an x, y, z triad")


# ------------------------------------------------------------------ 30.2
def fig_30_2():
    """Flow curves: Newtonian straight, pseudo-plastic and dilatant curved."""
    o = [_defs()]
    ox, oy = 150, 330
    xr, yt = 640, 70
    o.append(_arr(ox, oy, xr, oy, E, sw=1.4))
    o.append(_arr(ox, oy, ox, yt, E, sw=1.4))
    o.append(_lbl((ox + xr) / 2.0, oy + 26, "strain rate", "t", "middle"))
    o.append(_lbl(ox - 22, (oy + yt) / 2.0, "shear stress", "t", "middle",
                  ' transform="rotate(-90 %s %s)"' % (_f(ox - 22), _f((oy + yt) / 2.0))))

    # Newtonian: a straight line through the origin, slope eta
    o.append(_line(ox, oy, 600, 250, E, 1.6))
    o.append(_rot(470, 306, [("Newtonian liquids", "n")], -9.5, "middle", "ts"))
    # The slope label belongs just above the line, not on the axis: at y = oy its
    # descender was drawn straight through the strain-rate axis. x = 380 keeps it
    # clear of both "Newtonian liquids" (which starts around x = 425) and the
    # dilatant curve above.
    o.append(_lbl(380, 277, "slope η", "ts", "middle", ' font-style="italic"'))

    # pseudo-plastic: steep then flattening
    ps = [(ox, oy), (205, 248), (265, 200), (340, 168), (430, 148), (540, 136)]
    o.append(_pl(ps, E, 1.6, dash="8 3 2 3"))
    o.append(_lbl(300, 136, "pseudo-plastic materials", "ts", "start",
                  ' font-style="italic"'))
    o.append(_line(298, 132, 268, 194, E, 0.8))

    # dilatant: shallow then steepening, crossing the pseudo-plastic curve
    dl = [(ox, oy), (250, 306), (330, 272), (400, 222), (455, 165), (500, 112)]
    o.append(_pl(dl, E, 1.6, dash="6 4"))
    o.append(_lbl(470, 232, "dilatant materials", "ts", "start", ' font-style="italic"'))
    o.append(_line(468, 228, 452, 174, E, 0.8))

    # legend
    o.append(_rect(330, 78, 150, 44, P, E, 1.0))
    o.append(_lbl(405, 96, "non-Newtonian", "ts", "middle"))
    o.append(_line(344, 108, 380, 108, E, 1.6, dash="8 3 2 3"))
    o.append(_line(392, 108, 428, 108, E, 1.6, dash="6 4"))
    return _fig(svg(720, 372, "".join(o), "Các đường cong chảy của chất lỏng Newton và phi Newton"),
                "Hình 30.2 · Các đường cong chảy minh hoạ ứng xử của chất lỏng Newton và phi Newton.",
                "Figure 30.2 · Flow curves illustrating Newtonian and non-Newtonian fluid behaviour.",
                "Đồ thị ứng suất trượt theo tốc độ biến dạng: một đường thẳng qua gốc có độ dốc "
                "eta, một đường chấm gạch cong lõm xuống và một đường gạch đứt cong lõm lên, hai "
                "đường này cắt nhau",
                "A shear-stress against strain-rate graph: a straight line through the origin with "
                "slope eta, a dash-dot curve concave down and a dashed curve concave up, the two "
                "curves crossing")


# ------------------------------------------------------------------ 30.3
def fig_30_3():
    """Concentric cylinders: outer cup, inner bob, the annulus of fluid."""
    o = [_defs()]
    cx = 360
    # outer cylinder: two walls and a base, hatched
    o.append(_rect(244, 96, 26, 196, "url(#h30)", E, 1.2))
    o.append(_rect(450, 96, 26, 196, "url(#h30)", E, 1.2))
    o.append(_rect(244, 268, 232, 24, "url(#h30)", E, 1.2))
    # the fluid in the annulus
    o.append(_rect(270, 96, 180, 172, "url(#d30)", E, 0.0))
    # inner cylinder (the bob): a cup with a bevelled foot
    o.append(_poly([(304, 112), (416, 112), (416, 246), (392, 262), (328, 262), (304, 246)],
                   P, E, 1.4))
    # shafts
    o.append(_shaft(cx, 52, 112))
    o.append(_shaft(cx, 262, 330))
    # torque at the top, rotation at the bottom
    o.append(_carr("M 392,102 q 26,-10 28,12", E, 1.3))
    o.append(_mix(428, 96, [("T", "i")], anchor="end"))
    o.append(_carr("M 330,318 q -34,6 -40,-20", E, 1.3))
    o.append(_mix(300, 322, [("ω", "i"), ("2", "sub")], anchor="end"))
    # dimensions
    o.append(_line(244, 60, 244, 68, E, 0.8))
    o.append(_line(476, 60, 476, 68, E, 0.8))
    o.append(_darr(244, 64, 340, 64, E, 1.0))
    o.append(_darr(380, 64, 476, 64, E, 1.0))
    o.append(_mix(312, 58, [("D", "i"), ("2", "sub"), (" = 2R", "i"), ("2", "sub")],
                  anchor="middle", cls="ts"))
    o.append(_line(304, 140, 304, 148, E, 0.8))
    o.append(_line(416, 140, 416, 148, E, 0.8))
    o.append(_darr(304, 144, 416, 144, E, 1.0))
    o.append(_mix(360, 138, [("D", "i"), ("1", "sub"), (" = 2R", "i"), ("1", "sub")],
                  anchor="middle", cls="ts"))
    o.append(_line(228, 112, 240, 112, E, 0.8))
    o.append(_line(228, 262, 240, 262, E, 0.8))
    o.append(_darr(232, 112, 232, 262, E, 1.0))
    o.append(_lbl(224, 191, "L", "t", "middle"))
    # axes at the centre
    o.append(_arr(cx, 196, cx, 150, E, sw=1.1))
    o.append(_lbl(cx + 4, 148, "z", "ts", "start"))
    o.append(_arr(cx, 196, cx + 40, 196, E, sw=1.1))
    o.append(_lbl(cx + 44, 200, "r", "ts", "start"))
    # leaders on the right
    for ty, tx, label in ((120, 492, "Outer cylinder"), (196, 492, "Fluid sample"),
                          (250, 492, "Inner cylinder")):
        o.append(_lbl(496, ty, label, "ts", "start", ' font-style="italic"'))
        o.append(_line(492, ty - 4, 478 if ty == 120 else (440 if ty == 196 else 412),
                       ty - 4, E, 0.8))
    return _fig(svg(720, 350, "".join(o), "Hình học nhớt kế hai trụ đồng tâm"),
                "Hình 30.3 · Hình học của nhớt kế hai trụ đồng tâm.",
                "Figure 30.3 · Concentric cylinders viscometer geometry.",
                "Mặt cắt nhớt kế: trụ ngoài dạng cốc có thành dày, trụ trong hình cốc úp, chất lỏng "
                "ở vành khuyên giữa hai trụ; trục trên chịu mômen T, trục dưới quay với tốc độ góc "
                "omega hai",
                "A viscometer section: a thick-walled outer cup, an inner bob, fluid in the annulus "
                "between them; the upper shaft carries torque T and the lower one rotates at omega 2")


# ------------------------------------------------------------------ 30.4
def fig_30_4():
    """Cone and plate: the cone above, the fluid wedge, the plate below."""
    o = [_defs()]
    cx = 360
    yrim, yapex, yplate = 138, 176, 176
    # cone body
    o.append(_poly([(272, yrim), (448, yrim), (cx, yapex)], "url(#h30)", E, 1.3))
    # the fluid: two thin wedges, zero at the apex
    o.append(_poly([(272, yrim), (272, yplate), (cx, yapex)], "url(#w30)", E, 1.1))
    o.append(_poly([(448, yrim), (448, yplate), (cx, yapex)], "url(#w30)", E, 1.1))
    # the plate
    o.append(_rect(264, yplate, 192, 9, DARK, E, 1.0))
    # shafts
    o.append(_shaft(cx, 84, yrim))
    o.append(_shaft(cx, yplate + 9, 238))
    # rotation and torque
    o.append(_carr("M 378,92 q 16,-8 22,6", E, 1.3))
    o.append(_mix(404, 88, [("Ω", "i"), (", ", "n"), ("φ", "i")], anchor="start"))
    o.append(_carr("M 328,222 q -30,4 -34,-18", E, 1.3))
    o.append(_mix(286, 226, [("T", "i")], anchor="end"))
    # the cone half-angle theta, measured from the axis
    o.append(_line(cx, 62, cx, yapex, E, 0.8, dash="5 4"))
    arc = []
    for i in range(0, 9):
        a = _m.radians(-90 + 66.6 * i / 8.0)
        arc.append((cx + 100 * _m.cos(a), yapex + 100 * _m.sin(a)))
    o.append(_pl(arc, E, 1.0))
    o.append(_lbl(424, 70, "θ", "t", "middle"))
    # the small gap angle at the rim
    arc2 = []
    for i in range(0, 7):
        a = _m.radians(180 - 13.0 * i / 6.0)
        arc2.append((448 + 26 * _m.cos(a), yplate + 26 * _m.sin(a)))
    o.append(_pl(arc2, E, 1.0))
    o.append(_mix(482, 168, [("θ", "i"), ("0", "sub")], anchor="start"))
    # the radius
    o.append(_line(448, yrim - 4, 448, 116, E, 0.8))
    o.append(_darr(376, 112, 448, 112, E, 1.0))
    o.append(_lbl(414, 106, "R", "t", "middle"))
    # leaders on the left
    o.append(_lbl(258, 108, "Cone", "ts", "end", ' font-style="italic"'))
    o.append(_line(262, 112, 320, 128, E, 0.8))
    o.append(_lbl(258, 170, "Fluid", "ts", "end", ' font-style="italic"'))
    o.append(_lbl(258, 182, "Sample", "ts", "end", ' font-style="italic"'))
    o.append(_line(262, 172, 286, 166, E, 0.8))
    o.append(_lbl(258, 216, "Plate", "ts", "end", ' font-style="italic"'))
    o.append(_line(262, 212, 292, 186, E, 0.8))
    return _fig(svg(720, 256, "".join(o), "Hình học nhớt kế nón – bản phẳng"),
                "Hình 30.4 · Hình học của nhớt kế nón – bản phẳng.",
                "Figure 30.4 · Cone-and-plate viscometer geometry.",
                "Mặt cắt nhớt kế nón – bản: nón có đỉnh chạm bản phẳng, chất lỏng lấp đầy khe "
                "hình nêm dày dần ra mép, trục trên quay với tốc độ góc omega, trục dưới chịu mômen T",
                "A cone-and-plate section: the cone apex touches the plate, fluid fills the wedge "
                "that widens towards the rim, the upper shaft rotates at omega and the lower one "
                "carries torque T")


# ------------------------------------------------------------------ 30.5
def fig_30_5():
    """Parallel disks: two plates, a fluid slab, gap h, radius R."""
    o = [_defs()]
    cx = 330
    ytop, ybot = 148, 196
    o.append(_rect(232, ytop - 10, 196, 10, DARK, E, 1.0))
    o.append(_rect(232, ybot, 196, 10, DARK, E, 1.0))
    o.append(_rect(232, ytop, 196, ybot - ytop, "url(#w30)", E, 1.1))
    o.append(_shaft(cx, 78, ytop - 10))
    o.append(_shaft(cx, ybot + 10, 262))
    o.append(_carr("M 358,100 q 30,-2 34,20", E, 1.3))
    o.append(_mix(398, 108, [("Ω", "i"), (", θ", "n")], anchor="start"))
    o.append(_carr("M 300,238 q -28,4 -32,-16", E, 1.3))
    o.append(_mix(264, 218, [("T", "i")], anchor="end"))
    # R, from the axis to the rim
    o.append(_line(232, ytop - 16, 232, ytop - 4, E, 0.8))
    o.append(_line(cx, ytop - 34, cx, ytop - 10, E, 0.8, dash="4 3"))
    o.append(_darr(348, ytop - 28, 428, ytop - 28, E, 1.0))
    o.append(_lbl(380, ytop - 34, "R", "t", "middle"))
    # h, the gap
    o.append(_line(436, ytop, 448, ytop, E, 0.8))
    o.append(_line(436, ybot, 448, ybot, E, 0.8))
    o.append(_darr(444, ytop, 444, ybot, E, 1.0))
    o.append(_lbl(456, 175, "h", "t", "start"))
    # leaders
    o.append(_lbl(224, 120, "Upper", "ts", "end", ' font-style="italic"'))
    o.append(_lbl(224, 132, "Plate", "ts", "end", ' font-style="italic"'))
    o.append(_line(228, 124, 268, 138, E, 0.8))
    o.append(_lbl(224, 172, "Fluid", "ts", "end", ' font-style="italic"'))
    o.append(_lbl(224, 184, "Sample", "ts", "end", ' font-style="italic"'))
    o.append(_line(228, 176, 250, 176, E, 0.8))
    o.append(_lbl(224, 222, "Lower", "ts", "end", ' font-style="italic"'))
    o.append(_lbl(224, 234, "Plate", "ts", "end", ' font-style="italic"'))
    o.append(_line(228, 226, 268, 206, E, 0.8))
    o.append(_triad(292, 292, 26))
    return _fig(svg(720, 300, "".join(o), "Hình học nhớt kế hai đĩa song song"),
                "Hình 30.5 · Hình học của nhớt kế hai đĩa song song.",
                "Figure 30.5 · Parallel disks viscometer geometry.",
                "Mặt cắt nhớt kế hai đĩa: hai bản tròn song song kẹp lớp chất lỏng dày h, bán "
                "kính R, trục trên quay, trục dưới chịu mômen",
                "A parallel-disk viscometer section: two parallel disks clamp a fluid layer of "
                "thickness h and radius R, the upper shaft rotates and the lower carries torque")


# ------------------------------------------------------------------ 30.6
def fig_30_6():
    """Capillary viscometer: reservoir above, tube below, L and D."""
    o = [_defs()]
    cx = 330
    # reservoir
    o.append(_rect(248, 70, 164, 120, "url(#d30)", E, 1.3))
    # fluid surface
    o.append(_line(252, 88, 408, 88, E, 1.0, dash="6 4"))
    # the tube: from the reservoir floor down
    o.append(_line(306, 190, 306, 330, E, 1.3))
    o.append(_line(354, 190, 354, 330, E, 1.3))
    o.append(_rect(306, 190, 48, 140, "url(#d30)", E, 0.0))
    # the junction: the reservoir floor with the bore
    o.append(_line(248, 190, 306, 190, E, 1.3))
    o.append(_line(354, 190, 412, 190, E, 1.3))
    # L, the tube length
    o.append(_line(354, 196, 372, 196, E, 0.8))
    o.append(_line(354, 324, 372, 324, E, 0.8))
    o.append(_darr(368, 196, 368, 324, E, 1.0))
    o.append(_lbl(380, 262, "L", "t", "start"))
    # D, the bore
    o.append(_darr(306, 316, 354, 316, E, 1.0))
    o.append(_lbl(330, 310, "D", "t", "middle"))
    # the axes and the mean velocity
    o.append(_arr(cx, 236, cx, 200, E, sw=1.0))
    o.append(_lbl(cx + 4, 200, "z", "ts", "start"))
    o.append(_arr(cx, 236, cx + 30, 236, E, sw=1.0))
    o.append(_lbl(cx + 34, 240, "r", "ts", "start"))
    o.append(_arr(cx, 248, cx, 282, E, sw=1.2))
    o.append(_lbl(cx + 6, 268, "V", "t", "start"))
    # leaders on the left
    o.append(_lbl(240, 196, "Inlet", "ts", "end", ' font-style="italic"'))
    o.append(_mix(240, 208, [("P", "i"), ("1", "sub"), (", z", "n"), ("1", "sub")],
                  anchor="end", cls="ts", extra=' font-style="italic"'))
    o.append(_line(244, 200, 302, 200, E, 0.8))
    o.append(_lbl(240, 240, "Capillary", "ts", "end", ' font-style="italic"'))
    o.append(_lbl(240, 252, "Tube", "ts", "end", ' font-style="italic"'))
    o.append(_line(244, 244, 302, 244, E, 0.8))
    o.append(_lbl(240, 300, "Outlet", "ts", "end", ' font-style="italic"'))
    o.append(_mix(240, 312, [("P", "i"), ("2", "sub"), (", z", "n"), ("2", "sub")],
                  anchor="end", cls="ts", extra=' font-style="italic"'))
    o.append(_line(244, 304, 302, 304, E, 0.8))
    # leaders on the right
    o.append(_lbl(420, 100, "Sample", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(420, 112, "Reservoir", "ts", "start", ' font-style="italic"'))
    o.append(_line(416, 96, 400, 104, E, 0.8))
    o.append(_lbl(420, 152, "Fluid", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(420, 164, "Sample", "ts", "start", ' font-style="italic"'))
    o.append(_line(416, 156, 392, 160, E, 0.8))
    return _fig(svg(720, 344, "".join(o), "Hình học nhớt kế mao quản"),
                "Hình 30.6 · Hình học của nhớt kế mao quản.",
                "Figure 30.6 · Capillary viscometer geometry.",
                "Bình chứa rộng phía trên nối xuống một ống mao quản hẹp; ghi chú lối vào, lối "
                "ra, chiều dài L và đường kính D của ống",
                "A wide reservoir above feeding a narrow capillary tube, annotated with inlet, "
                "outlet, tube length L and bore D")


# ------------------------------------------------------------------ 30.7
def fig_30_7():
    """Falling sphere: the tube, the ball, its radius, the timed interval."""
    o = [_defs()]
    x0, x1 = 270, 450
    y0, y1 = 60, 330
    o.append(_rect(x0, y0, x1 - x0, y1 - y0, "url(#d30)", E, 1.3))
    o.append(_mix(320, 92, [("ρ", "i"), ("1", "sub")], anchor="middle"))
    # the sphere
    cy, r = 140, 34
    o.append(_circ(378, cy, r, P, E, 1.4))
    o.append(_mix(358, cy + 4, [("ρ", "i"), ("2", "sub")], anchor="middle"))
    o.append(_line(378, cy, 412, cy, E, 1.0))
    o.append(_mix(414, cy + 4, [("r", "i"), ("s", "sub")], anchor="start", cls="ts"))
    # its velocity
    o.append(_arr(378, cy + r + 8, 378, cy + r + 48, E, sw=1.3))
    o.append(_mix(384, cy + r + 40, [("U", "i"), ("t", "sub")], anchor="start"))
    # the timed interval d
    o.append(_line(258, 120, 268, 120, E, 0.8))
    o.append(_line(258, 236, 268, 236, E, 0.8))
    o.append(_darr(262, 120, 262, 236, E, 1.0))
    o.append(_lbl(252, 182, "d", "t", "middle"))
    # H, the container height
    o.append(_line(x1, y0, 470, y0, E, 0.8))
    o.append(_line(x1, y1, 470, y1, E, 0.8))
    o.append(_darr(466, y0, 466, y1, E, 1.0))
    o.append(_lbl(478, 200, "H", "t", "start"))
    # the bore
    o.append(_darr(x0, y1 + 14, x1, y1 + 14, E, 1.0))
    o.append(_mix((x0 + x1) / 2.0, y1 + 32, [("2r", "i")], anchor="middle", cls="ts"))
    return _fig(svg(720, 360, "".join(o), "Sơ đồ nhớt kế bi rơi"),
                "Hình 30.7 · Sơ đồ nhớt kế bi rơi. Thời gian bi đi hết quãng đường d cho biết vận "
                "tốc của bi, và vận tốc đó được dùng để tính độ nhớt trượt.",
                "Figure 30.7 · Schematic diagram of the falling sphere viscometer. The time taken "
                "for the sphere to traverse the distance d gives its velocity, which is then used "
                "to calculate the shear viscosity.",
                "Ống trụ đứng chứa chất lỏng, một viên bi rơi xuống với vận tốc U; ghi chú bán "
                "kính bi, quãng đường d và chiều cao H của ống",
                "An upright cylindrical tube of fluid with a sphere falling at velocity U, "
                "annotated with the sphere radius, the interval d and the container height H")


# ------------------------------------------------------------------ 30.8
def fig_30_8():
    """Falling cylinder: a narrow rod inside the tube."""
    o = [_defs()]
    x0, x1 = 270, 450
    y0, y1 = 60, 330
    o.append(_rect(x0, y0, x1 - x0, y1 - y0, "url(#d30)", E, 1.3))
    # the cylinder
    cw = 34
    cy0, cy1 = 84, 200
    o.append(_rect(360 - cw / 2.0, cy0, cw, cy1 - cy0, P, E, 1.4))
    o.append(_mix(360, cy0 + 20, [("ρ", "i"), ("2", "sub")], anchor="middle"))
    o.append(_mix(318, cy0 + 18, [("ρ", "i"), ("1", "sub")], anchor="middle"))
    o.append(_line(360, cy0 + 44, 360 + cw / 2.0, cy0 + 44, E, 1.0))
    o.append(_mix(360 + cw / 2.0 + 3, cy0 + 48, [("r", "i"), ("c", "sub")],
                  anchor="start", cls="ts"))
    # its length L
    o.append(_line(330, cy0, 344, cy0, E, 0.8))
    o.append(_line(330, cy1, 344, cy1, E, 0.8))
    o.append(_darr(338, cy0, 338, cy1, E, 1.0))
    o.append(_lbl(332, 146, "L", "t", "end"))
    # velocity
    o.append(_arr(360, cy1 + 8, 360, cy1 + 44, E, sw=1.3))
    o.append(_mix(366, cy1 + 38, [("U", "i"), ("t", "sub")], anchor="start"))
    # d and 2r
    o.append(_line(258, 110, 268, 110, E, 0.8))
    o.append(_line(258, 230, 268, 230, E, 0.8))
    o.append(_darr(262, 110, 262, 230, E, 1.0))
    o.append(_lbl(252, 174, "d", "t", "middle"))
    o.append(_darr(x0, y1 + 14, x1, y1 + 14, E, 1.0))
    o.append(_mix((x0 + x1) / 2.0, y1 + 32, [("2r", "i")], anchor="middle", cls="ts"))
    return _fig(svg(720, 360, "".join(o), "Sơ đồ nhớt kế trụ rơi"),
                "Hình 30.8 · Sơ đồ nhớt kế trụ rơi. Nguyên lý giống nhớt kế bi rơi; vận tốc của "
                "trụ cho phép xác định độ nhớt trượt của chất lỏng.",
                "Figure 30.8 · Schematic diagram of the falling cylinder viscometer. Using the same "
                "principle as the falling sphere, the velocity of the cylinder gives the shear "
                "viscosity of the fluid.",
                "Ống trụ đứng chứa chất lỏng, một thanh trụ hẹp rơi thẳng đứng trong ống; ghi chú "
                "chiều dài thanh, bán kính thanh và quãng đường d",
                "An upright tube of fluid with a narrow rod falling axially inside it, annotated "
                "with the rod length, its radius and the interval d")


# ------------------------------------------------------------------ 30.9
def fig_30_9():
    """In-situ opaque-liquid method: electrodes across the vessel, two resistance peaks."""
    o = [_defs()]
    x0, x1 = 300, 430
    y0, y1 = 66, 210
    o.append(_rect(x0, y0, x1 - x0, y1 - y0, "url(#d30)", E, 1.3))
    # the sphere and its travel
    o.append(_circ(365, 96, 9, P, E, 1.2))
    o.append(_arr(365, 110, 365, 150, E, sw=1.1))
    # d between the two electrode planes
    o.append(_line(312, 88, 326, 88, E, 0.8))
    o.append(_line(312, 160, 326, 160, E, 0.8))
    o.append(_darr(319, 88, 319, 160, E, 1.0))
    o.append(_lbl(310, 128, "d", "t", "end"))
    # the two electrode leads
    o.append(_pl([(x0, 100), (252, 100), (252, 244), (330, 244)], E, 1.3))
    o.append(_pl([(x1, 100), (478, 100), (478, 244), (400, 244)], E, 1.3))
    o.append(_lbl(492, 88, "electrodes", "ts", "start", ' font-style="italic"'))
    o.append(_line(488, 92, 434, 100, E, 0.8))
    # the meter
    o.append(_rect(330, 232, 70, 34, P, E, 1.3))
    o.append(_path("M 336,258 q 8,-12 14,0 q 8,12 14,0 q 8,-12 14,0", E, 1.0))
    for k in range(3):
        o.append(_circ(378 + 8 * k, 240, 2.2, E, E, 0.5))
    # the trace
    o.append(_arr(330, 372, 330, 300, E, sw=1.2))
    o.append(_arr(330, 372, 500, 372, E, sw=1.2))
    o.append(_lbl(322, 330, "Resistance", "ts", "middle",
                  ' transform="rotate(-90 322 330)"'))
    o.append(_lbl(415, 388, "time", "ts", "middle"))
    trace = [(330, 366)]
    for cx0, h in ((372, 40), (438, 40)):
        for i in range(0, 13):
            x = cx0 - 26 + i * 4.3
            y = 366 - h * _m.exp(-((x - cx0) ** 2) / (2 * 9.0 ** 2))
            trace.append((x, y))
    trace.append((492, 366))
    o.append(_pl(trace, E, 1.4))
    # the two planes, projected onto the trace
    o.append(_line(372, 302, 372, 372, E, 0.8, dash="4 3"))
    o.append(_line(438, 302, 438, 372, E, 0.8, dash="4 3"))
    o.append(_lbl(405, 292, "Passage of sphere through", "ts", "middle"))
    o.append(_lbl(405, 304, "the electrode planes", "ts", "middle"))
    return _fig(svg(720, 400, "".join(o), "Thiết bị đo độ nhớt chất lỏng đục tại chỗ"),
                "Hình 30.9 · Một kiểu thiết bị đo độ nhớt của chất lỏng đục ngay tại chỗ. Tín hiệu "
                "điện khi bi rơi qua cho biết thời gian đi hết quãng đường d giữa hai mặt điện cực.",
                "Figure 30.9 · One type of apparatus used to determine the viscosity of opaque "
                "liquids in situ. The electrical signal from the passing sphere gives the time to "
                "traverse the known distance d between the two sensors.",
                "Bình chứa chất lỏng đục với viên bi rơi qua hai mặt điện cực; hai dây điện cực nối "
                "xuống một đồng hồ, phía dưới là đồ thị điện trở theo thời gian có hai đỉnh",
                "An opaque-liquid vessel with a sphere falling through two electrode planes; two "
                "leads run to a meter, and below is a resistance-against-time trace with two peaks")


# ------------------------------------------------------------------ 30.10
def fig_30_10():
    """Oscillating cup: fibre, mirror, rod, cup."""
    o = [_defs()]
    cx = 360
    # the ceiling
    for k in range(0, 9):
        o.append(_line(316 + k * 11, 40, 322 + k * 11, 50, E, 1.0))
    o.append(_line(312, 52, 408, 52, E, 1.4))
    # the fibre
    o.append(_line(cx, 52, cx, 96, E, 1.0))
    o.append(_lbl(392, 66, "Suspension", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(392, 78, "Fiber", "ts", "start", ' font-style="italic"'))
    o.append(_line(388, 70, cx + 2, 74, E, 0.8))
    # the mirror
    o.append(_circ(cx, 118, 20, P, E, 1.3))
    o.append(_lbl(cx, 122, "Mirror", "ts", "middle", _fs(9)))
    o.append(_line(cx, 96, cx, 98, E, 1.0))
    # the rod down to the cup
    o.append(_line(cx, 138, cx, 178, E, 1.6))
    # the cup
    o.append(_rect(300, 178, 120, 130, "url(#d30)", E, 1.4))
    o.append(_mix(cx, 250, [("ρ", "i")], anchor="middle"))
    o.append(_line(288, 178, 300, 178, E, 0.8))
    o.append(_line(288, 308, 300, 308, E, 0.8))
    o.append(_darr(292, 178, 292, 308, E, 1.0))
    o.append(_lbl(284, 246, "H", "t", "end"))
    o.append(_darr(300, 320, 420, 320, E, 1.0))
    o.append(_mix(cx, 338, [("2r", "i")], anchor="middle", cls="ts"))
    return _fig(svg(720, 350, "".join(o), "Sơ đồ nhớt kế cốc dao động"),
                "Hình 30.10 · Sơ đồ nhớt kế cốc dao động. Độ tắt dần lôga của biên độ và chu kỳ "
                "dao động của cốc được dùng để xác định độ nhớt trượt tuyệt đối của chất lỏng.",
                "Figure 30.10 · Schematic diagram of the oscillating cup viscometer. Measurement of "
                "the logarithmic damping of the amplitude and period of vessel oscillation gives "
                "the absolute shear viscosity of the liquid.",
                "Sợi treo gắn vào trần, phía dưới là một gương tròn, rồi một thanh nối xuống cốc "
                "hình hộp chứa chất lỏng",
                "A suspension fibre from the ceiling, a round mirror below it, then a rod down to a "
                "box-shaped cup of liquid")


# ------------------------------------------------------------------ 30.11
def fig_30_11():
    """Relaxation: relative viscosity step above, absorption peak below."""
    o = [_defs()]
    ox, xr = 250, 640
    ytop, ymid, ybot = 70, 190, 300
    # the shared frame: one axis line for the lower plot, a divider for the upper
    o.append(_arr(ox, ybot, xr, ybot, E, sw=1.3))
    o.append(_arr(ox, ybot, ox, ytop - 6, E, sw=1.3))
    o.append(_line(ox, ymid, xr, ymid, E, 0.8, dash="3 3"))
    # upper: eta/eta0 step
    step = [(ox, 150), (400, 150), (430, 148), (452, 132), (470, 104), (490, 96), (xr, 96)]
    o.append(_pl(step, E, 1.8))
    o.append(_line(ox, 150, 420, 150, E, 0.9, dash="6 4"))
    o.append(_lbl(300, 142, "relaxed state", "ts", "start", ' font-style="italic"'))
    o.append(_lbl(520, 88, "unrelaxed state", "ts", "start", ' font-style="italic"'))
    o.append(_mix(232, 124, [("η", "i"), ("/η", "n"), ("0", "sub")], anchor="middle",
                  extra=' transform="rotate(-90 232 124)"'))
    # lower: alpha lambda peak
    peak = []
    for i in range(0, 61):
        x = ox + i * (xr - ox) / 60.0
        y = 280 - 62 * _m.exp(-((x - 452) ** 2) / (2 * 22.0 ** 2))
        peak.append((x, y))
    o.append(_pl(peak, E, 1.8))
    o.append(_mix(232, 268, [("αλ", "i")], anchor="middle",
                  extra=' transform="rotate(-90 232 268)"'))
    # the relaxation frequency
    o.append(_line(452, 300, 452, 214, E, 0.8, dash="4 3"))
    o.append(_lbl(452, 316, "1", "ts", "middle"))
    o.append(_mix(560, 320, [("ωτ", "i")], anchor="start"))
    return _fig(svg(720, 340, "".join(o), "Ảnh hưởng của hiện tượng trễ lên độ nhớt và độ hấp thụ"),
                "Hình 30.11 · Ảnh hưởng của hiện tượng trễ trong chất lỏng (tần số trễ ứng với "
                "ωτ = 1, trong đó ω = 2πf) lên độ nhớt tương đối (trên) và độ hấp thụ trên một bước "
                "sóng (dưới), trong miền đàn hồi đã trễ (ωτ &lt; 1) và miền nhớt-đàn hồi chưa trễ "
                "(ωτ > 1).",
                "Figure 30.11 · Effects of liquid relaxation (relaxation frequency corresponds to "
                "ωτ = 1 where ω = 2πf) on relative viscosity (upper) and absorption per wavelength "
                "(lower) in the relaxed elastic (ωτ &lt; 1) and unrelaxed viscoelastic (ωτ > 1) "
                "regimes.",
                "Hai đồ thị xếp trên dưới dùng chung trục hoành: phía trên là bậc nhảy của độ nhớt "
                "tương đối từ trạng thái đã trễ sang chưa trễ, phía dưới là một đỉnh hấp thụ tại "
                "omega tau bằng một",
                "Two stacked plots sharing one horizontal axis: above, a step in relative viscosity "
                "from the relaxed to the unrelaxed state; below, an absorption peak at omega tau "
                "equal to one")


# ------------------------------------------------------------------ 30.12
def fig_30_12():
    """Ultrasonic apparatus: the pulse chain and its two displays."""
    o = [_defs()]
    yb = 78
    # the chain
    o.append(_rect(150, yb - 16, 96, 32, P, E, 1.2))
    o.append(_lbl(198, yb + 1, "Wave", "ts", "middle", _fs(9)))
    o.append(_lbl(198, yb + 13, "Generator", "ts", "middle", _fs(9)))
    o.append(_rect(266, yb - 14, 54, 28, P, E, 1.2))
    o.append(_lbl(293, yb + 4, "Gate", "ts", "middle", _fs(9)))
    o.append(_circ(360, yb, 20, P, E, 1.2))
    o.append(_path("M 348,%s q 6,-12 12,0 q 6,12 12,0" % _f(yb - 4), E, 1.0))
    # buffer rods with the sample between them
    o.append(_rect(392, yb - 12, 34, 24, P, E, 1.2))
    o.append(_lbl(409, yb + 4, "BR-1", "ts", "middle", _fs(8)))
    o.append(_rect(430, yb - 18, 34, 36, "url(#d30)", E, 1.2))
    o.append(_lbl(447, yb + 4, "Sample", "ts", "middle", _fs(7)))
    o.append(_rect(468, yb - 12, 34, 24, P, E, 1.2))
    o.append(_lbl(485, yb + 4, "BR-2", "ts", "middle", _fs(8)))
    for a, b in ((246, 266), (320, 340), (380, 392), (426, 430), (464, 468)):
        o.append(_line(a, yb, b, yb, E, 1.2))
    # down to the amplifier
    o.append(_pl([(502, yb), (534, yb), (534, 150), (400, 150)], E, 1.2))
    o.append(_rect(320, 136, 80, 28, P, E, 1.2))
    o.append(_lbl(360, 154, "Amplifier", "ts", "middle", _fs(9)))
    # the two displays
    o.append(_pl([(360, 164), (360, 190), (250, 190), (250, 206)], E, 1.2))
    o.append(_pl([(360, 190), (470, 190), (470, 206)], E, 1.2))
    # (a) the decay trace, in a circle
    o.append(_circ(250, 268, 62, P, E, 1.3))
    o.append(_lbl(250, 222, "a", "t", "middle"))
    o.append(_arr(206, 306, 206, 224, E, sw=1.0))
    o.append(_arr(206, 306, 296, 306, E, sw=1.0))
    o.append(_lbl(200, 262, "Amplitude", "ts", "middle",
                  ' transform="rotate(-90 200 262)"'))
    o.append(_lbl(252, 318, "Time", "ts", "middle"))
    o.append(_pl([(212, 238), (238, 238), (250, 240), (262, 256), (276, 268), (292, 272)],
                 E, 1.4))
    # (b) the interferogram, in a box
    o.append(_rect(400, 206, 152, 124, P, E, 1.3))
    o.append(_lbl(476, 222, "b", "t", "middle"))
    o.append(_arr(412, 318, 412, 216, E, sw=1.0))
    o.append(_arr(412, 318, 540, 318, E, sw=1.0))
    o.append(_lbl(406, 268, "Amplitude", "ts", "middle",
                  ' transform="rotate(-90 406 268)"'))
    o.append(_lbl(476, 326, "Melt Thickness", "ts", "middle", _fs(9)))
    # a decaying oscillation
    pts = []
    for i in range(0, 41):
        x = 418 + i * 2.9
        env = 46 * _m.exp(-(x - 418) / 96.0)
        pts.append((x, 268 - env * _m.cos((x - 418) / 7.2)))
    o.append(_pl(pts, E, 1.3))
    return _fig(svg(720, 348, "".join(o), "Sơ đồ thiết bị đo độ nhớt bằng sóng siêu âm"),
                "Hình 30.12 · Sơ đồ thiết bị xác định độ nhớt trượt và độ nhớt thể tích bằng cách "
                "đo suy giảm sóng siêu âm. Tín hiệu nhận được sau thanh đệm ra (BR-2) được hiển "
                "thị theo (a) cấu hình thanh đệm cố định và (b) kỹ thuật giao thoa với thanh đệm "
                "di động.",
                "Figure 30.12 · Schematic diagram of apparatus for liquid shear and volume viscosity "
                "determination by ultrasonic wave attenuation measurement, showing the received "
                "signal amplitude through the exit buffer rod (BR-2) using (a) a fixed buffer rod "
                "configuration and (b) an interferometric technique with a movable buffer rod.",
                "Sơ đồ khối: máy phát sóng, cổng, đầu biến năng, hai thanh đệm kẹp mẫu, bộ khuếch "
                "đại, rồi hai màn hiển thị — một vòng tròn vẽ đường suy giảm theo thời gian và một "
                "ô chữ nhật vẽ dao thoa theo bề dày mẫu nóng chảy",
                "A block diagram: wave generator, gate, transducer, two buffer rods clamping the "
                "sample, an amplifier, then two displays — a circle showing the decay against time "
                "and a box showing the interferogram against melt thickness")


FIGS = [fig_30_1, fig_30_2, fig_30_3, fig_30_4, fig_30_5, fig_30_6,
        fig_30_7, fig_30_8, fig_30_9, fig_30_10, fig_30_11, fig_30_12]


def fig(n):
    """Figure n (1-based), as the 5-tuple the reader helper expects."""
    return FIGS[n - 1]()
