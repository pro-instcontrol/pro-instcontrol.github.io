# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 31 — Surface Tension Measurement.

14 source pages, three sections, 5 figures (31.1–31.5) and two tables.
Geometry is read off the 140 dpi page images in work/ch31img.

House rules carried over from chapters 29 and 30:
  * never write <sub>/<sup> inside SVG <text> — use _mix() tspans;
  * escape "<" as &lt; anywhere in SVG text;
  * a font-size attribute on <text class="t|ts"> is ignored, because the class
    rule sets the `font` shorthand — use _fs() for an inline style instead;
  * a label rotated to a line's angle needs a perpendicular offset, not a
    vertical one.

Chapter-specific note: a drop resting on a plane with contact angle theta is a
spherical cap whose centre sits *below* the plane, at depth R cos(theta). Getting
that sign wrong turns a flat wetting drop into a tall dome — see _cap().
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
    """An inline font size for a <text> element (a presentation attribute loses
    to the class rule that sets the `font` shorthand)."""
    return ' style="font-size:%spx"' % n


def _mix(x, y, parts, anchor="start", cls="t", extra=""):
    """One <text> assembled from parts, so a subscript cannot drift away from
    the symbol it belongs to."""
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
    extra = ' transform="rotate(%s %s %s)"' % (_f(ang), _f(x), _f(y))
    if fs:
        extra += _fs(fs)
    return _mix(x, y, parts, anchor, cls, extra)


def _defs():
    return ('<defs>'
            '<marker id="ah31" viewBox="0 0 10 10" refX="8.4" refY="5" '
            'markerWidth="6.4" markerHeight="6.4" orient="auto-start-reverse">'
            '<path d="M0,1.6 L9,5 L0,8.4 z" fill="%s"/></marker>'
            '<pattern id="h31" width="6" height="6" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#c9ced6" stroke-width="1"/></pattern>'
            '<pattern id="w31" width="5" height="5" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="5" stroke="#8b93a1" stroke-width="1"/></pattern>'
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


def _arr(x1, y1, x2, y2, col=E, marker="ah31", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.0):
    """A dimension line with arrowheads at both ends."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah31)" marker-end="url(#ah31)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _arc(cx, cy, r, a0, a1, col=E, sw=1.0, dash=None):
    """Arc from angle a0 to a1 (degrees, 0 = +x, positive = counter-clockwise on
    screen, i.e. upward). Used for contact-angle and azimuth indicators."""
    x0 = cx + r * _m.cos(_m.radians(a0))
    y0 = cy - r * _m.sin(_m.radians(a0))
    x1 = cx + r * _m.cos(_m.radians(a1))
    y1 = cy - r * _m.sin(_m.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    d = "M %s,%s A %s,%s 0 %d %d %s,%s" % (_f(x0), _f(y0), _f(r), _f(r),
                                           large, sweep, _f(x1), _f(y1))
    return _path(d, col, sw, "none", dash)


def _slab(x0, x1, y0, y1, fill="url(#h31)"):
    """A hatched solid body — the substrate every contact-line figure sits on."""
    return _rect(x0, y0, x1 - x0, y1 - y0, fill, E, 1.2)


def _cap(cx, y0, a, theta, col=E, sw=1.6):
    """A spherical cap sitting on the line y = y0.

    a is the contact radius, theta the contact angle in degrees. The centre of
    the generating sphere lies BELOW the plane at depth R*cos(theta), so the cap
    height is R - R*cos(theta): small theta gives a flat, wide drop (good
    wetting), large theta a tall one.
    """
    th = _m.radians(theta)
    R = a / _m.sin(th)
    x0, x1 = cx - a, cx + a
    return _path("M %s,%s A %s,%s 0 0 1 %s,%s"
                 % (_f(x0), _f(y0), _f(R), _f(R), _f(x1), _f(y0)), col, sw)


def _cap_R(cx, y0, a, theta):
    """Radius of the generating sphere, for callers that need to place labels."""
    return a / _m.sin(_m.radians(theta))


def _cap_top(cx, y0, a, theta):
    """y of the highest point of the cap, so labels can clear it."""
    R = _cap_R(cx, y0, a, theta)
    return y0 - R * (1 - _m.cos(_m.radians(theta)))


# ------------------------------------------------------------------ 31.1
def fig_31_1():
    """Contact angles and wetting: a flat drop in (a), a tall one in (b)."""
    o = [_defs()]
    y0 = 232
    # the two substrates
    o.append(_slab(60, 330, y0, y0 + 34))
    o.append(_slab(390, 660, y0, y0 + 34))

    for cx, a, th, letter, tx in ((195, 80, 34, "(a)", 195), (525, 62, 84, "(b)", 525)):
        o.append(_cap(cx, y0, a, th))
        xc = cx - a
        # Tangent to the cap at the left contact point, drawn as a dashed
        # construction line out into the gas. Without it the theta arc stops in
        # mid-air and reads as floating; the source marks the same tangent. The
        # line hugs the cap for its first few pixels — unavoidable, since the cap
        # *is* tangent there — so it is dashed to keep it distinct from the solid
        # liquid outline.
        ang = _m.radians(th)
        o.append(_line(xc, y0, xc + 54 * _m.cos(ang), y0 - 54 * _m.sin(ang),
                       E, 1.0, "4 3"))
        # contact-angle wedge between the slab and that tangent
        rr = 26
        o.append(_arc(xc, y0, rr, 0, th))
        am = _m.radians(th / 2.0)
        o.append(_mix(xc + (rr + 16) * _m.cos(am),
                      y0 - (rr + 16) * _m.sin(am) + 3,
                      [("θ", "i")], "middle", "ts"))
        o.append(_lbl(tx, y0 + 58, letter, "ts", "middle"))

    o.append(_lbl(300, y0 + 26, "solid", "ts", "middle"))
    o.append(_lbl(620, y0 + 26, "solid", "ts", "middle"))
    return _fig(svg(720, 330, "".join(o),
                    "Hai giọt chất lỏng trên mặt rắn, góc tiếp xúc nhỏ và lớn"),
                "Hình 31.1 · Minh hoạ góc tiếp xúc và sự làm ướt. Chất lỏng ở (a) làm ướt chất "
                "rắn tốt hơn ở (b).",
                "Figure 31.1 · Illustration of contact angles and wetting. The liquid in (a) wets "
                "the solid better than that in (b).",
                "Hai giọt chất lỏng nằm trên mặt rắn gạch chéo; giọt (a) dẹt và rộng với góc tiếp "
                "xúc nhỏ, giọt (b) cao và tròn với góc tiếp xúc lớn",
                "Two liquid drops resting on hatched solid surfaces: drop (a) is flat and wide "
                "with a small contact angle, drop (b) is tall and round with a large one")


# ------------------------------------------------------------------ 31.2
def fig_31_2():
    """The three surface tensions acting at a contact line, and theta."""
    o = [_defs()]
    y0 = 226
    o.append(_slab(110, 620, y0, y0 + 34))
    cx = 350
    th = 52.0

    # liquid surface leaving the contact point along the tangent, then flattening
    tx = cx + 78 * _m.cos(_m.radians(th))
    ty = y0 - 78 * _m.sin(_m.radians(th))
    o.append(_path("M %s,%s Q %s,%s 620,150" % (_f(cx), _f(y0), _f(tx), _f(ty)), E, 1.6))

    # the three tension vectors
    o.append(_arr(cx, y0, cx - 104, y0))          # gamma_SG, into the gas
    o.append(_arr(cx, y0, cx + 104, y0))          # gamma_SL, into the liquid
    o.append(_arr(cx, y0, tx, ty))                # gamma_LG, along the surface

    # Labels sit well out along each shaft: the contact point is where all three
    # vectors and the angle wedge converge, so anything placed near it collides
    # with something else.
    o.append(_mix(cx - 72, y0 - 10, [("γ", "n"), ("SG", "sub")], "middle", "ts"))
    o.append(_mix(cx + 74, y0 - 10, [("γ", "n"), ("SL", "sub")], "middle", "ts"))
    o.append(_mix(tx + 8, ty - 8, [("γ", "n"), ("LG", "sub")], "start", "ts"))

    # contact-angle wedge between the surface and gamma_LG. The label goes
    # *inside* the arc at r = 40: at r = 62 it landed on the liquid-surface curve.
    o.append(_arc(cx, y0, 46, 0, th))
    am = _m.radians(th / 2.0)
    o.append(_mix(cx + 40 * _m.cos(am), y0 - 40 * _m.sin(am) + 3,
                  [("θ", "i")], "middle", "ts"))

    o.append(_lbl(196, 128, "gas", "ts", "middle"))
    o.append(_lbl(520, 112, "liquid", "ts", "middle"))
    o.append(_lbl(300, y0 + 26, "solid", "ts", "middle"))
    return _fig(svg(720, 330, "".join(o),
                    "Ba lực căng bề mặt tác dụng tại đường tiếp xúc ba pha"),
                "Hình 31.2 · Các lực căng bề mặt tác dụng lên đường tiếp xúc.",
                "Figure 31.2 · Surface tension forces acting on the contact line.",
                "Sơ đồ đường tiếp xúc ba pha trên mặt rắn gạch chéo: vectơ gamma SG hướng sang "
                "trái, gamma SL hướng sang phải, gamma LG hướng lên theo tiếp tuyến mặt thoáng, "
                "kèm góc tiếp xúc theta",
                "A three-phase contact line on a hatched solid: gamma SG points left, gamma SL "
                "right, gamma LG up along the liquid surface, with the contact angle theta")


# ------------------------------------------------------------------ 31.3
def fig_31_3():
    """A surface element with (a) synclastic and (b) anticlastic curvature."""
    o = [_defs()]

    def patch(cx, cy, hsign, vsign, letter, top_a, bot_a, tip_a):
        """A surface element drawn as a 2x2 grid of curved lines.

        hsign and vsign are the signs of the two principal curvatures: equal
        signs give a dome, opposite signs a saddle. Only vsign changes between
        the two panels, so exactly one family of grid lines flips — which is the
        whole point of the figure.

        Every line is a quadratic Bezier between explicit end points. An earlier
        attempt used a parametric surface X(u,v)/Y(u,v); it looked right in the
        middle but the corners doubled back into little hooks, because at a
        corner both families of grid lines leave in nearly the same direction.
        Bezier edges cannot do that.

        The bow is large on purpose. The first version used +/-18 px on the
        outer edges only, which at page size reads as two identical rounded
        rectangles.
        """
        # A quadratic only reaches half its control offset at the midpoint, so
        # bow=34 buys a visible 17 px sagitta; 27 bought 13 and the panels
        # still looked alike.
        W, H, bow, sh = 116.0, 100.0, 34.0, -0.13
        hw, hh = W / 2.0, H / 2.0

        def sk(x, y):
            """Cheap perspective: tilt the whole patch so the right side sits
            higher, the way the source draws it."""
            return x, y + sh * (x - cx)

        TL, TR = sk(cx - hw, cy - hh), sk(cx + hw, cy - hh)
        BR, BL = sk(cx + hw, cy + hh), sk(cx - hw, cy + hh)

        def bez(P0, C, P1, t):
            u = 1 - t
            return (u * u * P0[0] + 2 * u * t * C[0] + t * t * P1[0],
                    u * u * P0[1] + 2 * u * t * C[1] + t * t * P1[1])

        def edge(A, B, dx, dy):
            """Bezier from A to B whose control is offset by (dx,dy) from the
            chord midpoint."""
            mx, my = (A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0
            return A, (mx + dx, my + dy), B

        top = edge(TL, TR, 0, vsign * bow)
        bot = edge(BL, BR, 0, vsign * bow)
        # The left edge is left straight and only the right edge bows. Bowing
        # both by the same amount is what a surface of translation really does,
        # but drawn flat it makes the left edge set off *rightward* from the
        # top-left corner while the top edge also sets off rightward, and the
        # corner folds into a hook. One straight edge, one bowed edge reads as
        # perspective instead.
        lef = edge(TL, BL, 0, 0)
        rig = edge(TR, BR, hsign * bow, 0)

        def d(P0, C, P1):
            return ("M %s,%s Q %s,%s %s,%s"
                    % (_f(P0[0]), _f(P0[1]), _f(C[0]), _f(C[1]), _f(P1[0]), _f(P1[1])))

        p = [_path(d(*e), E, 1.4) for e in (top, bot, lef, rig)]

        # the two interior curves, drawn between the midpoints of the edges so
        # the four quadrants close properly
        t05, b05 = bez(*top, 0.5), bez(*bot, 0.5)
        l05, r05 = bez(*lef, 0.5), bez(*rig, 0.5)
        p.append(_path(d(t05, (cx + hsign * bow, (t05[1] + b05[1]) / 2.0), b05), E, 1.1))
        p.append(_path(d(l05, ((l05[0] + r05[0]) / 2.0, (l05[1] + r05[1]) / 2.0 + vsign * bow),
                         r05), E, 1.1))

        def arrow(e, t, ang, ln, gap=8.0):
            """Tension on an edge, attached at parameter t rather than at the
            midpoint — at the midpoint the local slope is zero and every arrow
            would come out horizontal or vertical. The 8 px gap keeps the shaft
            from merging with the interior curve it is collinear with."""
            x, y = bez(*e, t)
            a = _m.radians(ang)
            dx, dy = _m.cos(a), -_m.sin(a)
            return _arr(x + gap * dx, y + gap * dy,
                        x + ln * dx, y + ln * dy, E, sw=1.5)

        p.append(arrow(top, 0.72, top_a, 70))
        p.append(arrow(bot, 0.72, bot_a, 70))
        p.append(arrow(lef, 0.55, 180, 76))
        p.append(arrow(rig, 0.42, tip_a, 38))
        p.append(_lbl(cx, 290, letter, "ts", "middle"))
        return "".join(p)

    # (a) dome: both families bow the same way; (b) saddle: they bow opposite ways
    o.append(patch(200, 150, +1, -1, "(a)", 104, 236, 34))
    o.append(patch(520, 150, +1, +1, "(b)", 56, 304, 58))
    return _fig(svg(720, 320, "".join(o),
                    "Phần tử mặt cong: hai bán kính cùng dấu và trái dấu"),
                "Hình 31.3 · Cơ học của mặt cong có các bán kính cong chính (a) cùng dấu và "
                "(b) trái dấu.",
                "Figure 31.3 · Mechanics of curved surfaces that have principal radii of "
                "curvature of (a) the same sign and (b) the opposite sign.",
                "Hai phần tử mặt cong vẽ dưới dạng lưới 2x2, mỗi cạnh có một mũi tên lực căng. "
                "Ở (a) hai họ đường lưới cong cùng chiều nên mặt lồi như vòm; ở (b) chúng cong "
                "ngược chiều nên mặt yên ngựa, và các lực ở hai cạnh đối diện triệt tiêu nhau",
                "Two surface elements drawn as 2x2 grids with a tension arrow on each edge. In "
                "(a) both families of grid lines bow the same way, giving a dome; in (b) they "
                "bow opposite ways, giving a saddle, and the forces on opposite edges cancel")


# ------------------------------------------------------------------ 31.4
def fig_31_4():
    """(a) a pendant drop with its coordinates, (b) a sessile drop."""
    o = [_defs()]

    # ---- (a) pendant drop hanging from a tube
    tube_l, tube_r = 148, 192
    o.append(_rect(tube_l - 14, 40, 14, 62, "url(#h31)", E, 1.2))
    o.append(_rect(tube_r, 40, 14, 62, "url(#h31)", E, 1.2))
    o.append(_path("M %d,102 C 138,134 110,174 118,212 C 128,250 150,262 170,262 "
                   "C 190,262 212,250 222,212 C 230,174 202,134 %d,102"
                   % (tube_l, tube_r), E, 1.6))

    # d_s across the neck, d_e across the equator. Both labels sit just left of
    # the z axis — centred, they were drawn straight through it.
    o.append(_darr(128, 140, 212, 140))
    o.append(_mix(166, 133, [("d", "i"), ("s", "sub")], "end", "ts"))
    o.append(_darr(118, 206, 222, 206))
    o.append(_mix(166, 199, [("d", "i"), ("e", "sub")], "end", "ts"))

    # axes: origin at the apex, z up, x to the right
    o.append(_line(170, 268, 170, 112, S, 0.9, dash="4 3"))
    o.append(_arr(170, 262, 170, 108, E, "ah31", 1.1))
    o.append(_lbl(176, 108, "z", "ts", "start"))
    o.append(_arr(170, 262, 224, 262, E, "ah31", 1.1))
    o.append(_lbl(230, 266, "x", "ts", "start"))

    # arc length s and the tangent angle phi, at a point low on the right flank
    o.append(_lbl(208, 252, "s", "ts", "start"))
    o.append(_line(204, 240, 236, 240, S, 0.9, dash="4 3"))
    o.append(_arc(204, 240, 26, 0, 40))
    o.append(_mix(236, 232, [("φ", "i")], "start", "ts"))

    o.append(_lbl(214, 116, "gas", "ts", "start"))
    o.append(_lbl(112, 300, "(a)", "ts", "middle"))

    # ---- (b) sessile drop on a plane
    y0 = 262
    cx = 540
    a, th = 74, 74
    o.append(_slab(410, 700, y0, y0 + 30))
    o.append(_cap(cx, y0, a, th))
    top = _cap_top(cx, y0, a, th)

    # R is the base radius, h the height above the plane
    o.append(_line(cx, y0 - 4, cx, top - 6, S, 0.9, dash="4 3"))
    o.append(_darr(cx, y0 - 26, cx + a, y0 - 26))
    o.append(_lbl(cx + a / 2.0, y0 - 32, "R", "ts", "middle"))
    o.append(_darr(cx + a + 26, y0, cx + a + 26, top))
    o.append(_lbl(cx + a + 32, (y0 + top) / 2.0 + 4, "h", "ts", "start"))
    o.append(_lbl(cx, y0 + 52, "(b)", "ts", "middle"))

    return _fig(svg(720, 360, "".join(o),
                    "Giọt treo và giọt nằm, kèm các kích thước đặc trưng"),
                "Hình 31.4 · (a) Giọt treo với các kích thước đặc trưng d<sub>e</sub> và "
                "d<sub>s</sub>, cùng các toạ độ dùng trong phương trình Young–Laplace. "
                "(b) Giọt nằm với các kích thước đặc trưng R và h.",
                "Figure 31.4 · (a) A pendant drop showing the characteristic dimensions d<sub>e</sub> "
                "and d<sub>s</sub>, and the coordinates used in the Young–Laplace equation. "
                "(b) A sessile drop showing the characteristic dimensions R and h.",
                "Bên trái là giọt treo dưới một ống nhỏ, có đường kính lớn nhất d_e và đường "
                "kính cổ d_s, trục z hướng lên từ đỉnh giọt, trục x sang phải, chiều dài cung s "
                "và góc nghiêng phi; bên phải là giọt nằm trên mặt phẳng với bán kính đáy R và "
                "chiều cao h",
                "Left, a pendant drop hanging from a tube with maximum diameter d_e and neck "
                "diameter d_s, a z axis up from the apex, an x axis to the right, arc length s and "
                "tangent angle phi; right, a sessile drop on a plane with base radius R and height h")


# ------------------------------------------------------------------ 31.5
def fig_31_5():
    """The four standard measurement geometries, one per panel."""
    o = [_defs()]

    # ---- (a) capillary rise
    yl = 250
    # The surface line is broken across the bore. Drawn straight through it, the
    # line at yl reads as a second meniscus and h stops meaning anything.
    o.append(_line(40, yl, 120, yl, E, 1.4))
    o.append(_line(200, yl, 330, yl, E, 1.4))
    # the walls run 30 px below the surface so the tube is visibly immersed
    o.append(_rect(120, 96, 14, yl + 30 - 96, "url(#h31)", E, 1.2))
    o.append(_rect(186, 96, 14, yl + 30 - 96, "url(#h31)", E, 1.2))
    o.append(_path("M 134,160 Q 160,176 186,160", E, 1.4))   # concave meniscus
    # the tube centreline, which gives the radius dimension a left-hand anchor
    o.append(_line(160, 100, 160, 160, S, 0.8, dash="4 3"))
    o.append(_darr(216, yl, 216, 160))
    o.append(_lbl(222, (yl + 160) / 2.0 + 4, "h", "ts", "start"))
    o.append(_darr(160, 132, 186, 132))
    o.append(_lbl(173, 126, "r", "ts", "middle"))
    o.append(_lbl(96, 196, "G", "ts", "middle"))
    o.append(_lbl(96, 272, "L", "ts", "middle"))
    o.append(_lbl(185, 300, "(a)", "ts", "middle"))

    # ---- (b) Wilhelmy plate
    xl = 372
    o.append(_line(352, yl, 700, yl, E, 1.4))
    o.append(_rect(xl, 104, 12, yl - 104, "url(#h31)", E, 1.2))
    o.append(_path("M 352,%d Q 360,%d 372,%d" % (yl, yl - 16, yl - 22), E, 1.4))
    o.append(_path("M 384,%d Q 396,%d 404,%d" % (yl - 22, yl - 16, yl), E, 1.4))
    o.append(_arr(xl + 6, 104, xl + 6, 62))
    o.append(_lbl(xl + 18, 70, "f", "ts", "start"))
    o.append(_lbl(352, 196, "G", "ts", "middle"))
    o.append(_lbl(440, 272, "L", "ts", "middle"))
    o.append(_lbl(420, 300, "(b)", "ts", "middle"))

    # ---- (c) du Nouy ring  (bottom row: everything shifted down by dy)
    dy = 310
    cy = 232 + dy
    o.append(_line(40, cy, 330, cy, E, 1.4))
    # The film the ring drags up. Straight sides plus a flat crown read as a
    # table; the S-curves are what make it a liquid sheet hanging off the wire.
    o.append(_path("M 96,%d C 104,%d 126,%d 158,%d L 242,%d C 274,%d 296,%d 304,%d"
                   % (cy - 9, cy - 34, cy - 44, cy - 44, cy - 44,
                      cy - 44, cy - 34, cy - 9), E, 1.4))
    o.append(_circ(96, cy, 9, P, E, 1.3))
    o.append(_circ(304, cy, 9, P, E, 1.3))
    o.append(_line(200, cy - 44, 200, 120 + dy, S, 0.9, dash="4 3"))
    o.append(_arr(200, cy - 44, 200, 104 + dy))
    o.append(_lbl(212, 112 + dy, "f", "ts", "start"))
    o.append(_darr(200, cy - 62, 304, cy - 62))
    o.append(_lbl(252, cy - 68, "R", "ts", "middle"))
    o.append(_lbl(322, cy + 4, "r", "ts", "start"))
    o.append(_lbl(60, 190 + dy, "G", "ts", "middle"))
    o.append(_lbl(60, 262 + dy, "L", "ts", "middle"))
    o.append(_lbl(185, 300 + dy, "(c)", "ts", "middle"))

    # ---- (d) maximum bubble pressure  (bottom row)
    ysurf = 150 + dy
    tip = 196 + dy
    # The surface line stops at the tube walls. It previously ran on to x = 660,
    # leaving a 160 px gap that read as a hole in the liquid.
    o.append(_line(352, ysurf, 552, ysurf, E, 1.4))
    o.append(_line(608, ysurf, 700, ysurf, E, 1.4))
    # the tube runs up out of the panel and is open at the top, so no cap
    o.append(_rect(552, 370, 12, tip - 370, "url(#h31)", E, 1.2))
    o.append(_rect(596, 370, 12, tip - 370, "url(#h31)", E, 1.2))
    o.append(_circ(580, 222 + dy, 26, P, E, 1.5))
    o.append(_darr(634, ysurf, 634, tip))
    o.append(_lbl(640, (ysurf + tip) / 2.0 + 4, "t", "ts", "start"))
    o.append(_darr(634, tip, 634, 248 + dy))
    o.append(_mix(640, 226 + dy, [("Z", "i"), ("B", "sub")], "start", "ts"))
    # stop 2 px short of the bubble wall: the head was landing on the circle
    o.append(_darr(580, 222 + dy, 604, 222 + dy))
    o.append(_lbl(592, 216 + dy, "r", "ts", "middle"))
    o.append(_lbl(532, 120 + dy, "G", "ts", "middle"))
    o.append(_lbl(520, 172 + dy, "L", "ts", "middle"))
    o.append(_lbl(580, 300 + dy, "(d)", "ts", "middle"))

    return _fig(svg(720, 640, "".join(o),
                    "Bốn hình học đo sức căng bề mặt"),
                "Hình 31.5 · Hình học của (a) phương pháp mao dẫn dâng, (b) phương pháp bản "
                "Wilhelmy, (c) phương pháp vòng du Noüy và (d) phương pháp áp suất bọt cực đại.",
                "Figure 31.5 · Geometries for (a) the capillary rise method, (b) the Wilhelmy "
                "plate method, (c) the du Noüy ring method and (d) the maximum bubble pressure "
                "method.",
                "Bốn sơ đồ nhỏ: (a) ống mao quản nhúng vào chất lỏng với cột chất lỏng dâng cao "
                "h và bán kính ống r; (b) bản phẳng mỏng treo thẳng đứng chịu lực kéo f; (c) vòng "
                "kim loại nâng màng chất lỏng, bán kính vòng R và bán kính dây r; (d) ống nhúng "
                "sâu t với bọt khí bán kính r ở đầu ống",
                "Four small diagrams: (a) a capillary tube dipped in liquid with a risen column of "
                "height h and bore radius r; (b) a thin vertical plate pulled by a force f; (c) a "
                "metal ring lifting a liquid film, ring radius R and wire radius r; (d) a tube "
                "immersed to depth t with a gas bubble of radius r at its tip")


FIGS = [fig_31_1, fig_31_2, fig_31_3, fig_31_4, fig_31_5]


def fig(n):
    return FIGS[n - 1]()
