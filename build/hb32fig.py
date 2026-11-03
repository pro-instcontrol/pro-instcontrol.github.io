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


# ------------------------------------------------------------------ 32.7
def fig_32_7():
    """R/R0 against temperature for the four common RTD metals."""
    o = [_defs()]
    L, Rr, T, B = 140.0, 520.0, 50.0, 350.0

    def px(t):
        return L + (t + 200.0) / 1000.0 * (Rr - L)

    def py(v):
        return B - v / 4.0 * (B - T)

    # frame, grid, ticks
    o.append(_rect(L, T, Rr - L, B - T, "#fff", E, 1.3))
    for t, lab in ((-200, "\u2212200"), (0, "0"), (200, "200"),
                   (400, "400"), (600, "600"), (800, "800")):
        if 0 < t < 800:
            o.append(_line(px(t), T, px(t), B, "#ccd2da", 1.0))
        o.append(_line(px(t), B, px(t), B + 4, E, 1.1))
        o.append(_lbl(px(t), B + 18, lab, "ts", "middle"))
    for v in (1, 2, 3, 4):
        if v < 4:
            o.append(_line(L, py(v), Rr, py(v), "#ccd2da", 1.0))
        o.append(_line(L - 4, py(v), L, py(v), E, 1.1))
        o.append(_lbl(L - 8, py(v) + 4, str(v), "ts", "end"))
    o.append(_mix(66, (T + B) / 2.0, [("R", "i"), ("/", ""), ("R", "i"), ("0", "sub")],
                  "middle", "tb", ' transform="rotate(-90 66 %s)"' % _f((T + B) / 2.0)))
    o.append(_lbl((L + Rr) / 2.0, B + 44, "Temperature \u00b0C", "t", "middle"))

    # the metals, steepest first.  Platinum's coefficient is the real one —
    # the others are scaled so the fan closes inside the frame, as it does in
    # the original, whose curves are drawn well off scale.
    metals = ((0.01150, 2.0e-6), (0.00860, 1.5e-6),
              (0.00591, 1.0e-6), (0.003945, -0.4e-6))

    def r_of(t, a, b):
        return 1.0 + a * t + b * t * t

    # below 0 °C the four curves are indistinguishable at this scale, so the
    # original draws one shared branch — so do we
    o.append(_pl([(px(-200), py(0.45)), (px(-150), py(0.62)),
                  (px(-80), py(0.85)), (px(0), py(1.0))], E, 1.7))
    for a, b in metals:
        pts, t = [], 0.0
        while t <= 800.0:
            v = r_of(t, a, b)
            if v > 4.0:
                break
            pts.append((px(t), py(v)))
            t += 4.0
        o.append(_pl(pts, E, 1.7))

    # the open circles the original marks the curves with, and their leaders
    lab = ((90, "Platinum", 670, 0.003945, -0.4e-6),
           (141, "Nickel alloy", 200, 0.00860, 1.5e-6),
           (214, "Copper", 135, 0.00591, 1.0e-6))
    for ly, name, t, a, b in lab:
        mx, my = px(t), py(r_of(t, a, b))
        o.append(_circ(mx, my, 3.2, "#fff", E, 1.3))
        o.append(_line(mx + 4, my, 594, ly, S, 0.9))
        o.append(_lbl(598, ly + 4, name, "t", "start"))
    # Nickel's curve leaves the top of the frame at 250 °C, so its label is
    # carried over the top edge — a straight leader from the curve would have
    # to cut across all three of the others.
    o.append(_line(311, 32, 594, 32, S, 0.9))
    o.append(_arr(311, 32, 311, 50, E, sw=0.9))
    o.append(_lbl(598, 36, "Nickel", "t", "start"))
    return _fig(svg(720, 410, "".join(o),
                    "Đồ thị R trên R₀ theo nhiệt độ của bốn kim loại làm cảm biến RTD"),
                "Hình 32.7 · Trong các kim loại thông dụng, niken có độ nhạy cao nhất. Cả bốn "
                "đường cùng đi qua điểm (0 °C; 1) rồi tách ra; đường càng dốc thì độ nhạy càng lớn.",
                "Figure 32.7 · Of the common metals, nickel has the highest sensitivity. All four "
                "curves pass through (0 °C; 1) and then fan out; the steeper the curve, the greater "
                "the sensitivity.",
                "Đồ thị có trục hoành là nhiệt độ từ âm 200 đến 800 độ C và trục tung là R trên R₀ "
                "từ 0 đến 4. Bốn đường cùng xuất phát từ điểm 0 độ C, R trên R₀ bằng 1 rồi tỏa lên; "
                "đường niken dốc nhất thoát khỏi đỉnh khung ở khoảng 250 độ C, đường bạch kim "
                "thoải nhất và đạt khoảng 3,9 ở 800 độ C",
                "A chart with temperature on the horizontal axis from minus 200 to 800 degrees C "
                "and R over R0 on the vertical axis from 0 to 4. Four curves leave the point at "
                "0 degrees C, R over R0 equal to 1, and fan upward; nickel is steepest and leaves "
                "the top of the frame near 250 degrees C, platinum is shallowest and reaches about "
                "3.9 at 800 degrees C")


# ------------------------------------------------------------------ 32.8
def fig_32_8():
    """The standard platinum resistance thermometer, in section."""
    o = [_defs()]
    o.append(_rect(150, 86, 420, 66, "#fff", E, 1.5, rx=33))
    # leadwires run right through the seal and on to the element
    for i in range(4):
        y = 108 + i * 8
        o.append(_line(104, y, 322, y, E, 1.1))
    o.append(_rect(150, 90, 30, 58, "url(#w32)", E, 1.1))
    # the support plate and the drilled mandrel the coils sit in
    o.append(_rect(212, 100, 300, 38, FILL, E, 1.2))
    o.append(_rect(300, 104, 196, 30, "#fff", E, 1.2))
    for i in range(5):
        cx = 316 + i * 36
        o.append(_rect(cx - 9, 106, 18, 26, "#fff", E, 1.0))
        o.append(_pl([(cx - 6 if j % 2 == 0 else cx + 6, 108 + j * 2.6)
                      for j in range(9)], E, 1.1)
                 )
    o.append(_lbl(84, 46, "LEADWIRES", "ts", "start"))
    o.append(_arr(126, 52, 112, 100, E, sw=0.9))
    o.append(_lbl(310, 44, "PLATINUM COILS", "ts", "start"))
    o.append(_arr(346, 50, 346, 100, E, sw=0.9))
    o.append(_lbl(214, 196, "ELEMENT SUPPORT", "ts", "start"))
    o.append(_arr(258, 190, 266, 140, E, sw=0.9))
    o.append(_lbl(440, 196, "QUARTZ SHEATH", "ts", "start"))
    o.append(_arr(474, 190, 504, 154, E, sw=0.9))
    return _fig(svg(720, 215, "".join(o),
                    "Mặt cắt nhiệt kế điện trở bạch kim chuẩn"),
                "Hình 32.8 · Nhiệt kế điện trở bạch kim chuẩn (SPRT) dễ vỡ và chỉ dùng trong "
                "môi trường phòng thí nghiệm.",
                "Figure 32.8 · The Standard Platinum Resistance Thermometer is fragile and used "
                "only in laboratory environments.",
                "Mặt cắt ngang một ống vỏ thạch anh thuôn hai đầu, bên trong có tấm đỡ phần tử "
                "khoan lỗ chứa các cuộn dây bạch kim, bốn dây dẫn đi ra phía trái",
                "A cross-section of a rounded quartz tube containing a support plate drilled with "
                "holes that hold platinum coils, with four leadwires leaving to the left")


# ------------------------------------------------------------------ 32.9
def fig_32_9():
    """The secondary standard PRT."""
    o = [_defs()]
    # flexible leadwires, drawn as a cable
    o.append(_pl([(58, 74), (96, 78), (128, 94), (150, 102)], E, 2.2))
    o.append(_pl([(58, 82), (94, 86), (126, 100), (150, 110)], E, 2.2))
    # transition fitting
    o.append(_rect(150, 90, 46, 32, "url(#w32)", E, 1.2))
    # sheath
    o.append(_rect(196, 96, 404, 20, "#fff", E, 1.4, rx=10))
    # hermetic seal at the entry
    o.append(_rect(196, 96, 14, 20, "url(#w32)", E, 1.0))
    # leadwires inside, with ceramic insulator beads threaded on them
    for y in (102, 110):
        o.append(_line(210, y, 508, y, E, 1.0))
    for x in range(240, 490, 34):
        o.append(_rect(x, 99, 9, 14, "#fff", E, 0.9))
    # coil-in-hole element and the potting behind it
    o.append(_rect(508, 98, 58, 16, "#fff", E, 1.1))
    o.append(_pl([(x, 100 if (x // 4) % 2 == 0 else 112)
                  for x in range(512, 563, 4)], E, 1.0))
    o.append(_rect(566, 98, 26, 16, "url(#h32)", E, 1.0))

    o.append(_lbl(56, 46, "FLEXIBLE EXTERNAL LEADWIRES", "ts", "start"))
    o.append(_arr(122, 52, 104, 74, E, sw=0.9))
    o.append(_lbl(150, 78, "TRANSITION FITTING", "ts", "start"))
    o.append(_arr(196, 84, 180, 90, E, sw=0.9))
    o.append(_lbl(320, 46, "HIGH TEMPERATURE METAL SHEATH", "ts", "start"))
    o.append(_arr(400, 52, 400, 96, E, sw=0.9))
    o.append(_lbl(470, 78, "HIGH TEMPERATURE LEADWIRES", "ts", "start"))
    o.append(_arr(494, 84, 460, 102, E, sw=0.9))

    o.append(_lbl(140, 180, "HERMETIC SEAL", "ts", "start"))
    o.append(_arr(196, 174, 202, 118, E, sw=0.9))
    o.append(_lbl(250, 180, "HIGH PURITY CERAMIC INSULATORS", "ts", "start"))
    o.append(_arr(340, 174, 340, 116, E, sw=0.9))
    o.append(_lbl(440, 180, "COIL-IN-HOLE ELEMENT", "ts", "start"))
    o.append(_arr(478, 174, 516, 116, E, sw=0.9))
    # the potting label sits on its own row, and its leader comes off the far
    # end of it, so it does not cut through the row above
    o.append(_lbl(440, 206, "HIGH PURITY CERAMIC POTTING MATERIAL", "ts", "start"))
    o.append(_arr(604, 200, 582, 116, E, sw=0.9))
    return _fig(svg(720, 225, "".join(o),
                    "Mặt cắt nhiệt kế điện trở bạch kim chuẩn thứ cấp"),
                "Hình 32.9 · Nhiệt kế điện trở bạch kim chuẩn thứ cấp cũng dành cho môi trường "
                "phòng thí nghiệm.",
                "Figure 32.9 · The Secondary Standard Platinum Resistance Thermometer is intended "
                "for laboratory environments.",
                "Một ống kim loại dài, đầu trái nối với cáp mềm qua khớp chuyển tiếp, bên trong "
                "có hai dây dẫn xuyên qua các hạt cách điện bằng gốm và phần tử cuộn dây đặt "
                "trong lỗ ở đầu phải",
                "A long metal sheath whose left end joins a flexible cable through a transition "
                "fitting, with two leadwires threaded through ceramic insulator beads and a "
                "coil-in-hole element at the right end")


# ------------------------------------------------------------------ 32.10
def fig_32_10():
    """The industrial PRT."""
    o = [_defs()]
    o.append(_pl([(58, 78), (96, 82), (128, 96), (150, 104)], E, 2.2))
    o.append(_pl([(58, 86), (94, 90), (126, 102), (150, 112)], E, 2.2))
    o.append(_rect(150, 92, 46, 32, "url(#w32)", E, 1.2))
    o.append(_rect(196, 96, 404, 22, "#fff", E, 1.6, rx=10))
    o.append(_rect(196, 96, 16, 22, "url(#w32)", E, 1.0))
    for y in (103, 111):
        o.append(_line(212, y, 496, y, E, 1.0))
    for x in range(244, 480, 36):
        o.append(_rect(x, 100, 10, 15, "#fff", E, 0.9))
    # the ruggedized element: a potted coil block
    o.append(_rect(496, 99, 62, 16, "url(#h32)", E, 1.2))
    o.append(_pl([(x, 101 if (x // 4) % 2 == 0 else 113)
                  for x in range(500, 555, 4)], E, 1.0))
    o.append(_rect(558, 99, 30, 16, "url(#w32)", E, 1.0))

    o.append(_lbl(56, 46, "FLEXIBLE EXTERNAL LEADWIRES", "ts", "start"))
    o.append(_arr(122, 52, 104, 78, E, sw=0.9))
    o.append(_lbl(150, 78, "TRANSITION FITTING", "ts", "start"))
    o.append(_arr(196, 84, 180, 92, E, sw=0.9))
    o.append(_lbl(320, 46, "STAINLESS STEEL SHEATH", "ts", "start"))
    o.append(_arr(392, 52, 392, 96, E, sw=0.9))

    o.append(_lbl(86, 186, "MOISTURE PROOF SEAL", "ts", "start"))
    o.append(_arr(196, 180, 204, 118, E, sw=0.9))
    o.append(_lbl(230, 186, "CERAMIC INSULATORS", "ts", "start"))
    o.append(_arr(300, 180, 320, 116, E, sw=0.9))
    o.append(_lbl(385, 186, "RUGGEDIZED ELEMENT", "ts", "start"))
    o.append(_arr(420, 180, 500, 118, E, sw=0.9))
    o.append(_lbl(540, 186, "CERAMIC POTTING MATERIAL", "ts", "start"))
    o.append(_arr(560, 180, 570, 118, E, sw=0.9))
    return _fig(svg(720, 215, "".join(o),
                    "Mặt cắt nhiệt kế điện trở bạch kim công nghiệp"),
                "Hình 32.10 · Nhiệt kế điện trở bạch kim công nghiệp bền gần như cặp nhiệt điện.",
                "Figure 32.10 · Industrial Platinum Resistance Thermometers are almost as durable "
                "as thermocouples.",
                "Một ống vỏ thép không gỉ dày, đầu trái nối cáp mềm qua khớp chuyển tiếp và mối "
                "hàn kín chống ẩm, bên trong có các hạt cách điện gốm và một khối phần tử được "
                "đúc kín ở đầu phải",
                "A thick stainless-steel sheath whose left end joins a flexible cable through a "
                "transition fitting and a moisture-proof seal, with ceramic insulator beads and a "
                "potted element block at the right end")


# ------------------------------------------------------------------ 32.11
def fig_32_11():
    """The wirewound RTD on its ceramic mandrel."""
    o = [_defs()]
    o.append(_rect(270, 84, 300, 64, "#fff", E, 1.5, rx=10))
    # ceramic cement seal closing the left end
    o.append(_rect(270, 86, 36, 60, "url(#w32)", E, 1.1))
    # the ceramic insulator the winding sits on, then the mica-insulated mandrel
    o.append(_rect(306, 90, 30, 52, "#f7f8fa", E, 1.1))
    o.append(_rect(336, 92, 204, 48, "url(#h32)", E, 1.2))
    # the platinum wire, seen side-on: one slanted pass per turn
    for x in range(344, 528, 16):
        o.append(_line(x, 98, x + 11, 134, E, 1.4))
    # leadwires entering through the seal
    o.append(_line(196, 104, 312, 104, E, 1.6))
    o.append(_line(196, 128, 312, 128, E, 1.6))

    o.append(_lbl(238, 46, "CERAMIC CEMENT SEAL", "ts", "start"))
    o.append(_arr(286, 52, 288, 86, E, sw=0.9))
    o.append(_lbl(380, 46, "PLATINUM WIRE", "ts", "start"))
    o.append(_arr(420, 52, 420, 96, E, sw=0.9))
    o.append(_lbl(530, 46, "S.S. TUBE", "ts", "start"))
    o.append(_arr(548, 52, 540, 84, E, sw=0.9))
    o.append(_lbl(600, 112, "MICA INSULATION", "ts", "start"))
    o.append(_arr(596, 112, 522, 138, E, sw=0.9))
    o.append(_lbl(176, 186, "PLATINUM ALLOY LEADWIRES", "ts", "start"))
    o.append(_arr(248, 180, 226, 130, E, sw=0.9))
    o.append(_lbl(360, 186, "CERAMIC INSULATOR", "ts", "start"))
    o.append(_arr(384, 180, 322, 142, E, sw=0.9))
    return _fig(svg(720, 205, "".join(o),
                    "Mặt cắt nhiệt kế điện trở dạng quấn dây trên lõi gốm"),
                "Hình 32.11 · Nhiệt kế điện trở quấn dây được quấn không cảm ứng quanh một lõi "
                "gốm hình trụ.",
                "Figure 32.11 · The wirewound RTD is noninductively wound around a cylindrical "
                "ceramic mandrel.",
                "Một ống thép không gỉ ngắn, đầu trái bịt bằng xi măng gốm, bên trong là lõi "
                "cách điện mica quấn dây bạch kim, hai dây dẫn hợp kim bạch kim đi vào từ bên trái",
                "A short stainless-steel tube sealed at the left with ceramic cement, containing "
                "a mica-insulated mandrel wound with platinum wire, with two platinum-alloy leads "
                "entering from the left")


# ------------------------------------------------------------------ 32.12
def fig_32_12():
    """The coil suspension RTD."""
    o = [_defs()]
    o.append(_rect(220, 86, 390, 64, "#fff", E, 1.5, rx=8))
    # powder packing filling the bore — jittered, or the regular grid reads as
    # a pattern rather than as loose powder
    for x in range(258, 576, 11):
        for y in range(94, 144, 10):
            o.append(_circ(x + ((x * 7 + y * 13) % 7) - 3,
                           y + ((x * 11 + y * 5) % 7) - 3,
                           1.1, "#9aa2ae", "none", 0))
    # the coil, drawn as the projection of a helix
    pts = []
    for i in range(0, 271):
        x = 292 + i
        pts.append((x, 118 - 15 * _m.sin(2 * _m.pi * (x - 292) / 24.0)))
    o.append(_pl(pts, E, 1.5))
    # glass seals at both ends
    o.append(_rect(220, 88, 34, 60, "url(#h32)", E, 1.1))
    o.append(_rect(576, 88, 34, 60, "url(#h32)", E, 1.1))
    o.append(_line(160, 106, 290, 106, E, 1.6))
    o.append(_line(160, 130, 290, 130, E, 1.6))

    o.append(_lbl(130, 44, "PLATINUM ALLOY LEAD WIRES", "ts", "start"))
    o.append(_arr(196, 50, 178, 106, E, sw=0.9))
    o.append(_lbl(340, 44, "HIGH PURITY POWDER PACKING", "ts", "start"))
    o.append(_arr(414, 50, 400, 94, E, sw=0.9))
    o.append(_lbl(214, 68, "GLASS SEAL", "ts", "start"))
    o.append(_arr(240, 72, 240, 88, E, sw=0.9))
    o.append(_lbl(534, 68, "GLASS SEAL", "ts", "start"))
    o.append(_arr(562, 72, 592, 88, E, sw=0.9))
    o.append(_lbl(330, 196, "PLATINUM COIL", "ts", "start"))
    o.append(_arr(392, 190, 392, 136, E, sw=0.9))
    o.append(_lbl(470, 196, "HIGH PURITY CERAMIC INSULATOR", "ts", "start"))
    o.append(_arr(520, 190, 548, 152, E, sw=0.9))
    return _fig(svg(720, 220, "".join(o),
                    "Mặt cắt nhiệt kế điện trở kiểu treo cuộn dây"),
                "Hình 32.12 · Nhiệt kế điện trở kiểu treo cuộn dây có cuộn dây được lắp vào các "
                "lỗ nhỏ.",
                "Figure 32.12 · The coil suspension RTD has a coil of wire assembled into small "
                "holes.",
                "Một ống trụ có hai đầu bịt kính, bên trong là lớp bột cách điện rải đều và một "
                "cuộn dây xoắn chạy dọc theo ống, hai dây dẫn đi vào từ bên trái",
                "A cylindrical tube sealed with glass at both ends, filled with insulating powder "
                "and containing a long helical coil, with two leads entering from the left")


# ------------------------------------------------------------------ 32.13
def fig_32_13():
    """The thin-film element, in isometric."""
    o = [_defs()]
    A = (250.0, 140.0)
    U = (210.0, -52.0)
    V = (46.0, 34.0)

    def P(u, v):
        return (A[0] + U[0] * u + V[0] * v, A[1] + U[1] * u + V[1] * v)

    top = [P(0, 0), P(1, 0), P(1, 1), P(0, 1)]
    o.append(_poly(top, "#fff", E, 1.5))
    # front and left faces, to give the plate its thickness
    o.append(_poly([P(0, 1), P(1, 1), (P(1, 1)[0], P(1, 1)[1] + 22),
                    (P(0, 1)[0], P(0, 1)[1] + 22)], FILL, E, 1.4))
    o.append(_poly([P(0, 0), P(0, 1), (P(0, 1)[0], P(0, 1)[1] + 22),
                    (P(0, 0)[0], P(0, 0)[1] + 22)], "#fff", E, 1.4))

    # the deposited film, a meander laid out in the plate's own plane
    vs = [0.30, 0.40, 0.50, 0.60, 0.70]
    pts = []
    for i, v in enumerate(vs):
        lo, hi = 0.32, 0.76
        if i % 2 == 0:
            pts += [P(lo, v), P(hi, v)]
            if i < len(vs) - 1:
                pts.append(P(hi, vs[i + 1]))
        else:
            pts += [P(hi, v), P(lo, v)]
            if i < len(vs) - 1:
                pts.append(P(lo, vs[i + 1]))
    o.append(_pl(pts, E, 2.6))

    # leadwires off the left face
    o.append(_line(250, 151, 196, 178, E, 1.6))
    o.append(_line(250, 158, 196, 194, E, 1.6))

    o.append(_lbl(90, 52, "GLASS (SUPPORT FOR LEADWIRES)", "ts", "start"))
    o.append(_arr(250, 58, 252, 137, E, sw=0.9))
    o.append(_lbl(330, 34, "DEPOSITED PLATINUM FILM", "ts", "start"))
    o.append(_arr(400, 40, 381, 118, E, sw=0.9))
    o.append(_lbl(516, 104, "PROTECTIVE GLASS COATING", "ts", "start"))
    o.append(_arr(512, 100, 476, 104, E, sw=0.9))
    o.append(_lbl(400, 216, "CERAMIC SUBSTRATE", "ts", "start"))
    o.append(_arr(452, 210, 470, 152, E, sw=0.9))
    o.append(_lbl(96, 216, "LEAD WIRES", "ts", "start"))
    o.append(_arr(170, 210, 198, 190, E, sw=0.9))
    return _fig(svg(720, 246, "".join(o),
                    "Phần tử màng mỏng bạch kim lắng trên đế gốm, nhìn theo hình chiếu trục đo"),
                "Hình 32.13 · Phần tử màng mỏng có một lớp bạch kim mỏng lắng trên đế gốm.",
                "Figure 32.13 · Thin-film elements have a thin film of platinum deposited onto a "
                "ceramic substrate.",
                "Một bản gốm mỏng nhìn nghiêng, mặt trên có đường dích dắc bằng bạch kim lắng "
                "đọng, phủ lớp thủy tinh bảo vệ, hai dây dẫn thoát ra ở góc dưới bên trái",
                "A thin ceramic plate seen at an angle, with a meandering deposited platinum track "
                "on its upper face under a protective glass coating, and two leads leaving at the "
                "lower left")


# ------------------------------------------------------------------ 32.14
def fig_32_14():
    """A fixed-point cell, in section, with its parts labelled."""
    o = [_defs()]
    # ---- borosilicate glass cell, open at the top
    o.append(_path("M 224,138 L 224,494 Q 224,536 300,536 Q 376,536 376,494 L 376,138",
                   E, 2.4))
    o.append(_path("M 232,146 L 232,492 Q 232,528 300,528 Q 368,528 368,492 L 368,146",
                   E, 1.1))
    # ---- thermal insulation filling the annulus
    o.append(_rect(234, 150, 132, 350, "url(#h32)", E, 0.8))
    # ---- graphite crucible, drawn over the insulation.  _path's argument order
    # is (d, col, sw, fill, dash) — the fill goes in the fourth slot.
    o.append(_path("M 254,312 L 254,470 Q 254,500 300,500 Q 346,500 346,470 L 346,312",
                   E, 1.6, "#fff"))
    # ---- the metal sample
    o.append(_rect(264, 340, 72, 136, "url(#h32)", E, 0.9))
    # ---- graphite thermometer well down the middle
    o.append(_rect(286, 320, 28, 152, "#fff", E, 1.2))
    # ---- graphite cap and the heat shunt above it
    o.append(_rect(246, 300, 108, 14, "#fff", E, 1.4))
    o.append(_rect(272, 286, 56, 14, "url(#w32)", E, 1.2))
    # ---- thermometer guide tube
    o.append(_rect(288, 146, 24, 142, "#fff", E, 1.2))
    # ---- stopper and gas seal
    o.append(_rect(234, 126, 132, 20, "url(#h32)", E, 1.2))
    o.append(_rect(264, 110, 72, 16, "url(#w32)", E, 1.2))
    # ---- the thermometer itself, with its lead
    o.append(_rect(250, 62, 100, 48, "#fff", E, 1.5, rx=4))
    o.append(_line(300, 62, 300, 34, E, 1.3))
    o.append(_line(300, 34, 388, 34, E, 1.3))
    # ---- shielding gas line and pressure gauge, clear of the thermometer body
    o.append(_pl([(352, 128), (352, 78), (372, 78)], E, 1.1))
    o.append(_circ(380, 78, 8, "#fff", E, 1.1))
    o.append(_line(380, 78, 386, 72, E, 0.9))

    lab = (
        (78, "platinum resistance thermometer", 352, 86),
        (114, "to shielding gas supply and pressure gauge", 384, 82),
        (150, "thermometer gas seal with silicone rubber", 334, 118),
        (186, "silicone rubber stopper", 366, 136),
        (222, "thermal insulation", 362, 210),
        (258, "thermometer guide tube [precision bore tube,", 312, 246),
        (294, "borosilicate glass cell [precision bore tube,", 374, 286),
        (330, "heat shunt (graphite)", 328, 293),
        (366, "graphite cap (lid) for the graphite crucible", 354, 307),
        (402, "graphite thermometer well", 314, 384),
        (438, "metal sample", 336, 424),
        (474, "graphite crucible", 346, 462),
        (510, "thermal insulation between the graphite", 368, 496),
    )
    for y, txt, tx, ty in lab:
        o.append(_lbl(420, y, txt, "ts", "start", _fs(9)))
        o.append(_arr(414, y - 3, tx, ty, E, sw=0.85))
    # the second lines of the three bracketed labels
    o.append(_lbl(420, 270, "ground to uniform outside diameter]", "ts", "start", _fs(9)))
    o.append(_lbl(420, 306, "ground to uniform outside diameter]", "ts", "start", _fs(9)))
    o.append(_lbl(420, 522, "crucible and the borosilicate glass cell", "ts", "start", _fs(9)))
    return _fig(svg(720, 552, "".join(o),
                    "Mặt cắt một tế bào điểm cố định dùng để hiệu chuẩn nhiệt kế chuẩn"),
                "Hình 32.14 · Hiệu chuẩn bằng điểm cố định dùng điểm ba, điểm đông đặc hoặc điểm "
                "nóng chảy của nước, kẽm, thiếc và agon.",
                "Figure 32.14 · Fixed point calibration uses the triple point, freezing point, or "
                "melting point of water, zinc, tin, and argon.",
                "Mặt cắt đứng của một ống thủy tinh borosilicat dài chứa lớp cách nhiệt, bên trong "
                "là nồi nấu graphit đựng mẫu kim loại, có giếng nhiệt kế graphit ở giữa; phía trên "
                "là nút cao su, mối hàn kín khí và nhiệt kế điện trở bạch kim, kèm đường dẫn khí "
                "và đồng hồ áp suất",
                "A vertical section through a tall borosilicate glass cell packed with thermal "
                "insulation, holding a graphite crucible of metal sample with a graphite "
                "thermometer well down the middle; above it sit a rubber stopper, a gas seal and "
                "the platinum resistance thermometer, with a gas line and pressure gauge")


# ------------------------------------------------------------------ 32.15
def fig_32_15():
    """An isothermal bath used for comparison calibration."""
    o = [_defs()]
    # outer tank, walls hatched
    o.append(_rect(140, 140, 440, 240, "url(#h32)", E, 1.6))
    o.append(_rect(170, 150, 400, 212, "#f7f8fa", E, 1.4))
    o.append(_rect(140, 118, 440, 22, "url(#h32)", E, 1.6))
    # the stabilization block
    o.append(_rect(280, 200, 220, 130, "#fff", E, 1.4))
    for x in range(300, 490, 26):
        o.append(_rect(x, 214, 10, 102, "#eef1f5", E, 0.8))
    # probes entering through the lid
    for x in (312, 412):
        o.append(_rect(x, 64, 12, 210, "#fff", E, 1.3))
        o.append(_rect(x - 4, 54, 20, 12, "#fff", E, 1.3))
    # measurement instrument
    o.append(_rect(86, 40, 128, 44, "#fff", E, 1.4, rx=4))
    o.append(_line(96, 58, 118, 58, "#8b93a1", 1.2))
    o.append(_line(96, 70, 132, 70, "#8b93a1", 1.2))
    o.append(_pl([(214, 62), (250, 62), (250, 70)], E, 1.2))
    o.append(_pl([(250, 70), (312, 70)], E, 1.2))
    o.append(_pl([(250, 70), (412, 70)], E, 1.2))
    # auto agitation
    o.append(_line(524, 356, 524, 316, E, 1.3))
    o.append(_ell(524, 310, 16, 5, "#fff", E, 1.2))
    o.append(_line(524, 312, 524, 300, E, 1.1))

    o.append(_lbl(64, 28, "MEASUREMENT INSTRUMENT", "ts", "start"))
    o.append(_arr(112, 34, 112, 40, E, sw=0.9))
    o.append(_lbl(596, 112, "HEATING OR", "ts", "start"))
    o.append(_lbl(596, 126, "COOLING", "ts", "start"))
    o.append(_arr(592, 122, 572, 190, E, sw=0.9))
    # the block label goes below the tank: inside the block the probe tubes
    # run straight through it and the text is unreadable
    o.append(_lbl(246, 398, "STABILIZATION BLOCK, 1\u201350 PROBES", "ts", "start", _fs(9)))
    o.append(_arr(300, 392, 330, 334, E, sw=0.9))
    o.append(_lbl(596, 330, "AUTO", "ts", "start"))
    o.append(_lbl(596, 344, "AGITATION", "ts", "start"))
    o.append(_arr(592, 338, 542, 310, E, sw=0.9))

    # the medium key, inside the vessel where the original puts it
    o.append(_lbl(184, 258, "MEDIUM", "tb", "start", _fs(9)))
    for i, t in enumerate(("1-ICE", "2-SILICON OIL", "3-HOT SALT BATH",
                           "4-O\u2082", "5-HEAVY SILICON OIL")):
        o.append(_lbl(184, 274 + i * 13, t, "ts", "start", _fs(9)))
    return _fig(svg(720, 412, "".join(o),
                    "Mặt cắt bể đẳng nhiệt dùng để hiệu chuẩn nhiệt kế điện trở công nghiệp"),
                "Hình 32.15 · Bể đẳng nhiệt cho phép hiệu chuẩn nhiệt kế điện trở công nghiệp "
                "bằng cách so sánh với một nhiệt kế chuẩn thứ cấp.",
                "Figure 32.15 · An isothermal bath permits calibration of industrial RTDs compared "
                "with a secondary standard.",
                "Mặt cắt một bể hai lớp có thành gạch chéo, bên trong là khối ổn định nhiệt khoan "
                "nhiều lỗ, hai que đo cắm từ trên xuống qua nắp, nối với một thiết bị đo ở góc "
                "trái; bên phải có cánh khuấy tự động",
                "A section through a double-walled bath with hatched walls, containing a drilled "
                "stabilization block with two probes inserted from above through the lid and "
                "wired to a measuring instrument at the left, with an agitator at the right")


FIGS = [fig_32_1, fig_32_2, fig_32_3, fig_32_4, fig_32_5, fig_32_6,
        fig_32_7, fig_32_8, fig_32_9, fig_32_10, fig_32_11, fig_32_12,
        fig_32_13, fig_32_14, fig_32_15]


def fig(n):
    return FIGS[n - 1]()
