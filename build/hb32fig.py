# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 32 — Temperature.

Only §32.1 is implemented so far: figures 32.1–32.6 (bimetallic thermometers).
Geometry is read off the 140 dpi page images in work/ch32img.

House rules carried over from chapters 29–31:
  * never write <sub>/<sup> inside SVG <text> — use _mix() tspans;
  * a font-size attribute on <text class="t|ts"> is ignored, because the class
    rule sets the `font` shorthand — use _fs() for an inline style;
  * _arr()'s sixth positional argument is the *marker*, not the stroke width.
    Always pass sw= by keyword, or the arrowhead silently disappears.
"""
import math as _m

from hbfig import INK, GOLD, MUTED, TXT, STYLE, _f, svg, _fig

E = INK
G = GOLD
S = MUTED
FILL = "#eef1f5"
DARK = "#cfd6de"


# ------------------------------------------------------------------ primitives
def _lbl(x, y, t, cls="t", anchor="start", extra=""):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s"%s>%s</text>'
            % (cls, _f(x), _f(y), anchor, extra, t))


def _fs(n):
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


def _defs():
    return ('<defs>'
            '<marker id="ah32" viewBox="0 0 10 10" refX="8.4" refY="5" '
            'markerWidth="6.4" markerHeight="6.4" orient="auto-start-reverse">'
            '<path d="M0,1.6 L9,5 L0,8.4 z" fill="%s"/></marker>'
            '<pattern id="h32" width="6" height="6" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#c9ced6" stroke-width="1"/></pattern>'
            '<pattern id="w32" width="5" height="5" patternTransform="rotate(45)" '
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


def _arr(x1, y1, x2, y2, col=E, marker="ah32", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.0):
    """A dimension line with arrowheads at both ends."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah32)" marker-end="url(#ah32)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _band(x0, x1, y, bow, thick, fill=DARK):
    """A curved two-layer strip: an arc from (x0,y) to (x1,y) bulging up by bow,
    closed off to give it thickness."""
    cy = y - bow
    d = ("M %s,%s Q %s,%s %s,%s L %s,%s Q %s,%s %s,%s Z"
         % (_f(x0), _f(y), _f((x0 + x1) / 2.0), _f(cy), _f(x1), _f(y),
            _f(x1), _f(y + thick), _f((x0 + x1) / 2.0), _f(cy + thick),
            _f(x0), _f(y + thick)))
    return _path(d, E, 1.3, fill)


def _arc(cx, cy, r, a0, a1, col=E, sw=1.0, dash=None):
    """Arc from angle a0 to a1 (degrees, 0 = +x, positive = counter-clockwise on
    screen, i.e. upward)."""
    x0 = cx + r * _m.cos(_m.radians(a0))
    y0 = cy - r * _m.sin(_m.radians(a0))
    x1 = cx + r * _m.cos(_m.radians(a1))
    y1 = cy - r * _m.sin(_m.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    d = ("M %s,%s A %s,%s 0 %d %d %s,%s"
         % (_f(x0), _f(y0), _f(r), _f(r), large, sweep, _f(x1), _f(y1)))
    return _path(d, col, sw, "none", dash)


def _arcarr(cx, cy, r, a0, a1, col=E, sw=1.2):
    """A curved arrow — used for the bending moments, which act about a point
    rather than along a line."""
    x0 = cx + r * _m.cos(_m.radians(a0))
    y0 = cy - r * _m.sin(_m.radians(a0))
    x1 = cx + r * _m.cos(_m.radians(a1))
    y1 = cy - r * _m.sin(_m.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    d = ("M %s,%s A %s,%s 0 %d %d %s,%s"
         % (_f(x0), _f(y0), _f(r), _f(r), large, sweep, _f(x1), _f(y1)))
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'marker-end="url(#ah32)"/>' % (d, col, sw))


def _on_line(x1, y1, x2, y2, parts, off=11, frac=0.5, cls="ts"):
    """A label riding along a line: rotated to the line's angle (kept upright)
    and pushed off it perpendicular. Getting the angle from atan2 rather than
    hard-coding it is the only way these stay on their lines when the geometry
    is tweaked."""
    ang = _m.degrees(_m.atan2(y2 - y1, x2 - x1))
    if ang > 90:
        ang -= 180
    elif ang < -90:
        ang += 180
    mx = x1 + (x2 - x1) * frac
    my = y1 + (y2 - y1) * frac
    a = _m.radians(ang + 90)
    px, py = mx + off * _m.cos(a), my + off * _m.sin(a)
    extra = ' transform="rotate(%s %s %s)"' % (_f(ang), _f(px), _f(py))
    return _mix(px, py, parts, "middle", cls, extra)


def _spiral(cx, cy, r0, r1, turns, col=E, sw=1.3):
    """An Archimedean spiral. Concentric circles read as a bullseye, not a coil —
    the growing radius is what makes it a spiral."""
    pts = []
    n = 240
    for i in range(n + 1):
        t = i / float(n)
        a = 2 * _m.pi * turns * t
        r = r0 + (r1 - r0) * t
        pts.append((cx + r * _m.cos(a), cy + r * _m.sin(a)))
    d = "M " + " L ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts)
    return _path(d, col, sw)


# ------------------------------------------------------------------ 32.1
def fig_32_1():
    """The strip flat at T0, and the same strip bent once heated to T."""
    o = [_defs()]
    x0, x1 = 215, 505
    h = 19

    # (1) flat, at T0 — shaded, with the ghost outline it will occupy when hot
    o.append(_rect(x0, 42, x1 - x0, h, DARK, E, 1.2))
    o.append(_rect(x0 - 28, 42, x1 - x0 + 56, h, "none", E, 0.9, "5 4"))
    o.append(_mix(x1 + 44, 56, [("T", "i"), ("0", "sub")], "start", "ts"))

    # (2) flat, the two layers separated so the interface is visible
    o.append(_rect(x0, 112, x1 - x0, h, "#fff", E, 1.2))
    o.append(_line(x0, 112 + h / 2.0, x1, 112 + h / 2.0, E, 0.9))
    o.append(_rect(x0 - 28, 112, x1 - x0 + 56, h, "none", E, 0.9, "5 4"))
    o.append(_mix(x1 + 44, 126, [("T", "i"), ("0", "sub")], "start", "ts"))

    # (3) the same strip, now bent — the ghost shows where it started
    o.append(_line(x0 - 28, 246, x1 + 28, 246, E, 0.9, "5 4"))
    o.append(_band(x0, x1, 246, 62, 20))
    o.append(_mix(x1 + 44, 214, [("T", "i"), (" > ", ""), ("T", "i"), ("0", "sub")],
                  "start", "ts"))
    o.append(_lbl(360, 292, "convex up (α₂ > α₁)", "ts", "middle"))
    return _fig(svg(720, 310, "".join(o),
                    "Dải kim loại kép phẳng ở T0 và cong khi bị đốt nóng"),
                "Hình 32.1 · Dải kim loại kép. Dải phẳng ở nhiệt độ T₀; khi nung nóng, lớp có "
                "hệ số giãn nở lớn hơn giãn nhiều hơn nên dải cong lồi lên trên.",
                "Figure 32.1 · Linear bimetallic strip. Flat at T₀; once heated, the layer with "
                "the larger expansion coefficient grows more and the strip bows convex upward.",
                "Ba hình xếp dọc: dải phẳng có viền đứt nét, dải phẳng hai lớp, và dải cong lồi "
                "lên trên với đường đứt nét đánh dấu vị trí ban đầu",
                "Three stacked views of a flat strip: one shaded with a dashed ghost outline, one "
                "plain showing the two bonded layers, and one bowed convex upward with a dashed "
                "line marking its original flat position")


# ------------------------------------------------------------------ 32.2
def fig_32_2():
    """Bending of a bimetallic strip: the element, the bent element and the
    resulting internal stress distribution."""
    o = [_defs()]

    # ---- (a) the element cut out of the strip
    bx0, bx1, by, bh = 120, 600, 58, 40
    o.append(_rect(bx0, by, bx1 - bx0, bh, "#fff", E, 1.3))
    o.append(_line(bx0, by + bh / 2.0, bx1, by + bh / 2.0, E, 1.3))
    o.append(_mix((bx0 + bx1) / 2.0, by + 15, [("(2) ", ""), ("E", "i"), ("2", "sub"),
                                              (", α", ""), ("2", "sub")], "middle", "ts"))
    o.append(_mix((bx0 + bx1) / 2.0, by + 33, [("(1) ", ""), ("E", "i"), ("1", "sub"),
                                              (", α", ""), ("1", "sub")], "middle", "ts"))
    for xx, idx in ((150, "1"), (470, "2")):
        o.append(_line(xx, by - 26, xx, by, E, 1.0, "4 3"))
        o.append(_line(xx, by + bh, xx, by + bh + 24, E, 1.0, "4 3"))
        o.append(_mix(xx, by - 32, [("A", "i"), (idx, "sub")], "middle", "ts"))
        o.append(_mix(xx, by + bh + 38, [("B", "i"), (idx, "sub")], "middle", "ts"))
    # thicknesses at the right-hand end
    o.append(_darr(628, by, 628, by + bh / 2.0, S, 0.9))
    o.append(_darr(628, by + bh / 2.0, 628, by + bh, S, 0.9))
    o.append(_darr(660, by, 660, by + bh, S, 0.9))
    o.append(_mix(636, by + 13, [("t", "i"), ("1", "sub")], "start", "ts"))
    o.append(_mix(636, by + 36, [("t", "i"), ("2", "sub")], "start", "ts"))
    o.append(_mix(668, by + 26, [("t", "i")], "start", "ts"))
    o.append(_lbl((bx0 + bx1) / 2.0, by + bh + 68, "(a)", "ts", "middle"))

    # ---- (b) the element, bent. The two cut sections carry a force P along the
    # axis and a moment M about it; they are drawn separately because they are
    # separate quantities and one arrow labelled with both reads as neither.
    y = 210
    o.append(_band(150, 470, y, 52, 15, DARK))
    o.append(_band(150, 470, y + 15, 52, 15, "#fff"))
    o.append(_mix(310, y - 46, [("(2)", "")], "middle", "ts"))
    o.append(_mix(310, y + 26, [("(1)", "")], "middle", "ts"))
    # right-hand section: moment (curved) and axial force (straight)
    o.append(_arcarr(480, y + 2, 15, 300, 60, E, 1.2))
    o.append(_arr(474, y + 2, 506, y - 14, E, sw=1.2))
    o.append(_mix(506, y - 16, [("P", "i"), ("1", "sub")], "start", "ts"))
    o.append(_mix(486, y - 30, [("M", "i"), ("1", "sub")], "start", "ts"))
    o.append(_arcarr(140, y + 2, 15, 240, 0, E, 1.2))
    o.append(_arr(146, y + 2, 114, y - 14, E, sw=1.2))
    o.append(_mix(96, y - 16, [("P", "i"), ("2", "sub")], "end", "ts"))
    o.append(_mix(104, y - 30, [("M", "i"), ("2", "sub")], "end", "ts"))
    o.append(_lbl(310, y + 96, "(b)", "ts", "middle"))

    # ---- (c) stress across the section, and shear at the ends
    cx, top, bot = 300, 340, 430
    o.append(_rect(cx - 26, top, 52, bot - top, "#fff", E, 1.2))
    o.append(_line(cx, top, cx, bot, E, 0.8, "4 3"))
    # linear bending stress: tension at the top fibre, compression at the bottom
    o.append(_line(cx + 34, top + 4, cx - 34, bot - 4, G, 1.4))
    for yy in (top + 12, top + 30, bot - 30, bot - 12):
        xx = cx + 34 * (1 - 2 * (yy - top) / float(bot - top))
        o.append(_arr(cx, yy, xx, yy, G, sw=1.0))
    o.append(_mix(cx - 34, top - 10, [("σ", "i")], "middle", "ts"))

    # shear at the ends: a section carrying a set of small horizontal arrows
    sx = 430
    o.append(_rect(sx - 24, top, 48, bot - top, "#fff", E, 1.2))
    for yy in (top + 16, top + 34, top + 52, top + 70):
        o.append(_arr(sx - 16, yy, sx + 16, yy, E, sw=0.9))
    o.append(_mix(sx, top - 10, [("τ", "i")], "middle", "ts"))
    o.append(_lbl(365, bot + 32, "(c)", "ts", "middle"))
    return _fig(svg(720, 500, "".join(o),
                    "Uốn của dải kim loại kép và phân bố ứng suất bên trong"),
                "Hình 32.2 · Uốn của dải kim loại kép khi nung nóng đều, với α₂ ≥ α₁. (a) Dải và "
                "phân tố A₁B₁–A₂B₂ cắt ra từ dải. (b) Phân tố bị uốn cong. (c) Phân bố ứng suất: "
                "bên trái là ứng suất pháp trên tiết diện, bên phải là ứng suất cắt ở hai đầu.",
                "Figure 32.2 · Bending of a bimetallic strip uniformly heated with α₂ ≥ α₁. "
                "(a) The strip and the element A₁B₁–A₂B₂ cut out of it. (b) The element bent. "
                "(c) Internal stress: normal stress across the section on the left, shearing "
                "stress at the ends on the right.",
                "Ba phần: dải phẳng hai lớp có tiết diện A1B1 và A2B2 cùng chiều dày t1, t2; phân "
                "tố bị uốn cong với mômen và lực ở hai đầu; và hai tiết diện nhỏ thể hiện ứng "
                "suất pháp và ứng suất cắt",
                "Three parts: a flat two-layer strip with sections A1B1 and A2B2 and thicknesses "
                "t1 and t2; the same element bent with moments and forces at both ends; and two "
                "small sections showing normal and shearing stress")


def fig_32_3():
    """A strip simply supported at its ends, with the radius construction."""
    o = [_defs()]
    y = 250
    xa, xb = 200, 520
    cx = (xa + xb) / 2.0
    bow, thick = 40, 11
    for x in (xa, xb):
        o.append(_poly([(x - 20, y + 46), (x + 20, y + 46), (x, y + 8)], FILL, E, 1.2))
        o.append(_line(x - 26, y + 46, x + 26, y + 46, E, 1.4))
    o.append(_band(xa, xb, y, bow, thick, DARK))
    # span
    o.append(_darr(xa, y - 62, xb, y - 62, S, 0.9))
    o.append(_line(xa, y - 68, xa, y - 52, S, 0.8))
    o.append(_line(xb, y - 68, xb, y - 52, S, 0.8))
    o.append(_mix(cx, y - 70, [("L", "i")], "middle", "ts"))
    # mid-span deflection: from the line through the supports up to the *under*
    # side of the strip, so the arrow does not vanish inside the band
    # The mid-span deflection is only ~35 px tall, so dimensioning it in place
    # jams the arrow into the strip. Carry the two levels out to the right with
    # thin extension lines and dimension between them where there is room.
    ytop = y - bow + thick
    o.append(_line(cx, ytop, cx + 74, ytop, S, 0.7, "3 3"))
    o.append(_line(cx, y, cx + 74, y, S, 0.7, "3 3"))
    o.append(_darr(cx + 62, y, cx + 62, ytop, S, 0.9))
    o.append(_mix(cx + 70, (y + ytop) / 2.0 + 4, [("d", "i")], "start", "ts"))
    # radius construction: centre well below, R out to the end, R-t2 vertically
    oy = y + 300
    o.append(_line(cx, y + 6, cx, oy, E, 1.0, "5 4"))
    o.append(_line(cx, oy, xb, y + 6, E, 1.0))
    o.append(_circ(cx, oy, 3, E, E, 1.0))
    o.append(_on_line(cx, oy, xb, y + 6, [("R", "i")], off=12))
    o.append(_on_line(cx, y + 6, cx, oy, [("R", "i"), (" − ", ""), ("t", "i"), ("2", "sub")],
                      off=14))
    o.append(_mix(xb + 12, y + 4, [("t", "i"), ("2", "sub")], "start", "ts"))
    return _fig(svg(720, 600, "".join(o),
                    "Dải đặt trên hai gối tựa đơn giản, với cấu trúc bán kính cong"),
                "Hình 32.3 · Uốn của dải đặt trên hai gối tựa đơn giản ở hai đầu. Độ võng d ở "
                "giữa nhịp liên hệ với bán kính cong R qua hình học của cung.",
                "Figure 32.3 · Bending of a strip simply supported at its ends. The mid-span "
                "deflection d is related to the radius of curvature R through the geometry of "
                "the arc.",
                "Dải cong đặt trên hai gối hình tam giác, có kích thước nhịp L ở trên, độ võng d "
                "ở giữa, và hai đường bán kính R và R trừ t2 kéo xuống tâm cong ở phía dưới",
                "A bowed strip resting on two triangular supports, with span L dimensioned above, "
                "mid-span deflection d, and radius lines R and R minus t2 running down to the "
                "centre of curvature below")


def fig_32_4():
    """The same strip clamped at one end — the cantilever case."""
    o = [_defs()]
    xa, xb = 150, 500
    ya, yb = 96, 156
    o.append(_rect(xa - 34, ya - 16, 34, 62, "url(#w32)", E, 1.2))
    o.append(_line(xa - 34, ya - 16, xa - 34, ya + 46, E, 1.4))
    o.append(_path("M %s,%s C %s,%s %s,%s %s,%s L %s,%s C %s,%s %s,%s %s,%s Z"
                   % (_f(xa), _f(ya), _f(xa + 130), _f(ya), _f(xb - 90), _f(yb - 8), _f(xb), _f(yb),
                      _f(xb), _f(yb + 10), _f(xb - 90), _f(yb + 2), _f(xa + 130), _f(ya + 10),
                      _f(xa), _f(ya + 10)), E, 1.3, DARK))
    # span
    o.append(_darr(xa, ya - 40, xb, ya - 40, S, 0.9))
    o.append(_line(xa, ya - 46, xa, ya - 30, S, 0.8))
    o.append(_line(xb, ya - 46, xb, ya - 30, S, 0.8))
    o.append(_mix((xa + xb) / 2.0, ya - 48, [("L", "i")], "middle", "ts"))
    # deflection at the free end, measured from the strip's original line
    o.append(_darr(xb, ya, xb, yb, S, 0.9))
    o.append(_mix(xb + 10, (ya + yb) / 2.0, [("d", "i")], "start", "ts"))
    o.append(_mix(xb + 12, yb + 16, [("t", "i"), ("1", "sub")], "start", "ts"))
    # radius construction
    oy = yb + 300
    o.append(_line(xa + 10, ya + 10, xa + 10, oy, E, 1.0, "5 4"))
    o.append(_line(xa + 10, oy, xb, yb + 6, E, 1.0))
    o.append(_circ(xa + 10, oy, 3, E, E, 1.0))
    o.append(_on_line(xa + 10, oy, xb, yb + 6, [("R", "i")], off=12))
    o.append(_on_line(xa + 10, ya + 10, xa + 10, oy,
                      [("R", "i"), (" + ", ""), ("t", "i"), ("1", "sub"), (" − ", ""), ("d", "i")],
                      off=14))
    return _fig(svg(720, 560, "".join(o),
                    "Dải bị kẹp chặt một đầu, đầu kia tự do cong xuống"),
                "Hình 32.4 · Uốn của dải kẹp chặt ở một đầu. Đầu tự do võng xuống một đoạn d so "
                "với phương ban đầu.",
                "Figure 32.4 · Bending of a strip fixed at one end. The free end drops by d from "
                "its original line.",
                "Dải kim loại kẹp vào tường gạch chéo ở bên trái, cong xuống về phía đầu tự do; "
                "có kích thước chiều dài L, độ võng d và các đường bán kính R",
                "A strip clamped into a hatched wall on the left, curving down toward its free "
                "end, with span L, deflection d and radius lines R")


def fig_32_5():
    """A coiled bimetal element: the spiral with its pointer, and the helix."""
    o = [_defs()]
    cx, cy = 210, 150
    o.append(_spiral(cx, cy, 13, 68, 2.6))
    o.append(_circ(cx, cy, 4, E, E, 1.0))
    # radius, out to the rim and labelled beyond it
    ax, ay = cx + 68 * _m.cos(_m.radians(40)), cy - 68 * _m.sin(_m.radians(40))
    o.append(_arr(cx, cy, ax, ay, E, sw=1.0))
    o.append(_mix(cx + 88 * _m.cos(_m.radians(40)),
                  cy - 88 * _m.sin(_m.radians(40)) - 4, [("R", "i")], "start", "ts"))
    # thickness of the coil, dimensioned clear of the rim
    o.append(_darr(cx - 92, cy - 68, cx - 92, cy + 68, S, 0.9))
    o.append(_line(cx - 98, cy - 68, cx - 74, cy - 68, S, 0.8))
    o.append(_line(cx - 98, cy + 68, cx - 74, cy + 68, S, 0.8))
    o.append(_mix(cx - 92, cy - 76, [("t", "i")], "middle", "ts"))
    # the pointer and the force applied at its end
    px, py = cx + 96, cy + 96
    o.append(_line(cx, cy, px, py, E, 1.6))
    o.append(_arr(px - 6, py - 6, px + 12, py + 12, E, sw=1.2))
    o.append(_mix(px + 18, py + 14, [("F", "i")], "start", "ts"))
    # rotation angle, measured from the vertical to the pointer
    o.append(_line(cx, cy, cx, cy + 92, E, 0.9, "4 3"))
    o.append(_arc(cx, cy, 78, -90, -45, E, 1.0))
    o.append(_mix(cx + 40, cy + 86, [("θ", "i")], "start", "ts"))

    # the helix: the same strip wound as a screw, drawn as a zigzag with a
    # parallel second edge so it reads as a strip and not as a bare line
    hx, hy = 400, 74
    pts = [(hx + i * 44, hy + (0 if i % 2 == 0 else 78)) for i in range(5)]
    o.append(_pl(pts, E, 1.6))
    for i in range(len(pts) - 1):
        o.append(_line(pts[i][0], pts[i][1] + 9, pts[i + 1][0], pts[i + 1][1] + 9, E, 1.0))
    o.append(_lbl(hx + 88, hy + 112, "helical coil", "ts", "middle"))
    return _fig(svg(720, 300, "".join(o),
                    "Phần tử lưỡng kim dạng cuộn xoắn ốc và dạng lò xo xoắn"),
                "Hình 32.5 · Phần tử lưỡng kim dạng cuộn. Bên trái là cuộn xoắn ốc có kim chỉ và "
                "lực F tác dụng ở đầu kim, với góc quay θ; bên phải là dạng xoắn ốc (lò xo).",
                "Figure 32.5 · Helical coiled bimetal element. On the left the spiral coil with "
                "its pointer and a force F applied at its end, giving a rotation θ; on the right "
                "the same strip wound as a helix.",
                "Bên trái là cuộn xoắn ốc nhiều vòng có bán kính R, chiều dày t, kim chỉ quay góc "
                "theta dưới lực F; bên phải là dải xếp thành hình lò xo xoắn",
                "Left: a multi-turn spiral coil with radius R, strip thickness t and a pointer "
                "rotated by theta under a force F. Right: the same strip wound into a helix")


def fig_32_6():
    """A snap-action disc, shown in both of its stable positions."""
    o = [_defs()]
    x0, x1 = 170, 470
    cy = 120
    # the mounts the disc sits in
    o.append(_rect(x0 - 30, cy - 34, 30, 68, "url(#w32)", E, 1.2))
    o.append(_rect(x1, cy - 34, 30, 68, "url(#w32)", E, 1.2))
    # position A: bowed upward (solid).  Position B: bowed downward (dashed).
    # The dash has to go through dash=, not the fill slot — see the note at the
    # top of this file.
    o.append(_path("M %s,%s Q %s,%s %s,%s"
                   % (_f(x0), _f(cy), _f((x0 + x1) / 2.0), _f(cy - 46), _f(x1), _f(cy)),
                   E, 2.0))
    o.append(_path("M %s,%s Q %s,%s %s,%s"
                   % (_f(x0), _f(cy), _f((x0 + x1) / 2.0), _f(cy + 46), _f(x1), _f(cy)),
                   E, 1.2, "none", "5 4"))
    # travel between the two positions
    o.append(_darr(310, cy - 42, 310, cy + 42, E, 1.0))
    o.append(_mix(x1 + 40, cy - 40, [("A", "i")], "start", "ts"))
    o.append(_mix(x1 + 40, cy + 46, [("B", "i")], "start", "ts"))
    # the two fixed contacts and the lever the disc pushes when it snaps down
    o.append(_circ(104, cy - 16, 4, E, E, 1.0))
    o.append(_circ(104, cy + 38, 4, E, E, 1.0))
    o.append(_line(104, cy - 16, x0 - 30, cy - 16, E, 1.2))
    o.append(_line(104, cy + 38, 196, cy + 38, E, 1.2))
    o.append(_rect(196, cy + 32, 150, 12, "#fff", E, 1.2))
    o.append(_path("M %s,%s Q %s,%s %s,%s"
                   % (_f(346), _f(cy + 32), _f(358), _f(cy + 20), _f(370), _f(cy + 32)),
                   E, 1.2))
    o.append(_lbl(96, cy - 22, "Contact", "ts", "end"))
    o.append(_lbl(96, cy + 44, "Contact", "ts", "end"))
    return _fig(svg(720, 250, "".join(o),
                    "Phần tử lưỡng kim tác động tức thời ở hai vị trí ổn định A và B"),
                "Hình 32.6 · Phần tử lưỡng kim tác động tức thời. Đĩa bật từ vị trí A sang vị trí "
                "B khi vượt qua nhiệt độ ngưỡng, đóng hoặc mở tiếp điểm.",
                "Figure 32.6 · Snap-action bimetallic element. The disc jumps from position A to "
                "position B once the threshold temperature is crossed, making or breaking the "
                "contact.",
                "Đĩa lưỡng kim gắn giữa hai khối gạch chéo, có vị trí lồi lên A và vị trí lõm "
                "xuống B, mũi tên hai chiều chỉ khoảng dịch chuyển, hai tiếp điểm ở bên trái",
                "A bimetallic disc mounted between two hatched blocks, with a raised position A "
                "and a lowered position B, a double arrow showing the travel, and two contacts "
                "on the left")


FIGS = [fig_32_1, fig_32_2, fig_32_3, fig_32_4, fig_32_5, fig_32_6]


def fig(n):
    return FIGS[n - 1]()
