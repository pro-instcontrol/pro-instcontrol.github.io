# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 32 — Temperature.

§32.1–32.3 are complete: figures 32.1–32.22.  §32.4 is in progress — 32.24 is drawn,
32.25–32.31 remain.  The book has no figure 32.23 (see FIG_NO at the foot of the file).
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


def _therm(cx, cy, r=16.0, horiz=False):
    """The thermistor symbol §32.3 uses everywhere: a circle holding a zigzag
    with a small T beside it. The zigzag follows the lead direction — the book
    turns it horizontal when the leads run sideways (fig 32.21a). Leads are
    drawn by the caller, because every figure enters the symbol differently."""
    o = [_circ(cx, cy, r, "#fff", E, 1.3)]
    n = 8
    if horiz:
        x0, x1 = cx - r * 0.66, cx + r * 0.66
        o.append(_pl([(x0 + (x1 - x0) * i / n, cy - 4.2 + (7.0 if i % 2 else 0.0))
                      for i in range(n + 1)], E, 1.05))
        o.append(_lbl(cx, cy - 5.0, "T", "ts", "middle", _fs(8)))
    else:
        y0, y1 = cy - r * 0.66, cy + r * 0.66
        o.append(_pl([(cx - 4.2 + (7.0 if i % 2 else 0.0), y0 + (y1 - y0) * i / n)
                      for i in range(n + 1)], E, 1.05))
        o.append(_lbl(cx + 2.6, cy + 3.2, "T", "ts", "start", _fs(8)))
    return "".join(o)


def _zz(x1, y1, x2, y2, amp=5.0, n=6, col=E, sw=1.3):
    """A zigzag resistor between two points. Drawn along the segment, so the
    same helper covers the vertical and the horizontal case — which matters
    because §32.3 uses both orientations side by side."""
    dx, dy = x2 - x1, y2 - y1
    L = _m.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    pts = [(x1, y1)]
    for i in range(1, 2 * n):
        t = i / float(2 * n)
        s = amp if i % 2 else -amp
        pts.append((x1 + dx * t + nx * s, y1 + dy * t + ny * s))
    pts.append((x2, y2))
    return _pl(pts, col, sw)


def _batt(cx, cy, lbl="", side="right"):
    """A single cell, + up. The caller draws the leads down to cy-4 and up from
    cy+4."""
    o = [_line(cx - 11, cy - 4, cx + 11, cy - 4, E, 1.5),
         _line(cx - 5.5, cy + 4, cx + 5.5, cy + 4, E, 3.2),
         _lbl(cx + 10, cy - 7, "+", "ts", "middle", _fs(9))]
    if lbl:
        if side == "right":
            o.append(_mix(cx + 16, cy + 4, [(lbl, ""), ], "start", "ts"))
        else:
            o.append(_mix(cx - 16, cy + 4, [(lbl, ""), ], "end", "ts"))
    return "".join(o)


def _res_h(cx, cy, w=34.0, h=9.0):
    """A resistor in a horizontal lead, drawn as the book draws it in 32.19 — a
    plain open box, not the ANSI zigzag."""
    return _rect(cx - w / 2.0, cy - h / 2.0, w, h, "#fff", E, 1.3)


def _res_v(cx, cy, w=9.0, h=34.0):
    return _rect(cx - w / 2.0, cy - h / 2.0, w, h, "#fff", E, 1.3)


# ---------------------------------------------------------------- 32.16
def fig_32_16():
    """R against T for a switching-type PTC thermistor. The interest is the
    shape: a shallow negative slope, then a wall, then a peak and a negative
    tail — so the axes are bare and there is no scale to speak of."""
    o = [_defs()]
    AX, AY = 170.0, 330.0
    o.append(_arr(AX, AY + 12, AX, 44, E, sw=1.5))
    o.append(_arr(AX - 16, AY, 616, AY, E, sw=1.5))
    o.append(_lbl(148, 56, "R", "t", "end"))
    o.append(_lbl(624, 352, "T", "t", "start"))
    o.append(_path("M 246,286 Q 322,302 402,308 "
                   "C 434,309 460,268 474,190 "
                   "C 484,138 492,100 502,84 "
                   "C 510,72 528,70 540,80 "
                   "C 550,90 556,104 562,124", E, 1.9))
    o.append(_line(412, 311, 498, 311, S, 1.1, "7 5"))
    o.append(_mix(506, 315, [("R", ""), ("min", "sub")], "start"))
    o.append(_line(432, 88, 534, 88, S, 1.1, "7 5"))
    o.append(_mix(424, 92, [("R", ""), ("max", "sub")], "end"))
    return _fig(svg(660, 380, "".join(o),
                    "Đặc tính điện trở theo nhiệt độ của nhiệt điện trở PTC kiểu chuyển mạch"),
                "Hình 32.16 · Đặc tính điện trở – nhiệt độ của một nhiệt điện trở PTC kiểu "
                "chuyển mạch thông dụng. Ở nhiệt độ thấp, từ dưới 0 °C đến R<sub>min</sub>, giá trị "
                "điện trở nhỏ và R<sub>T</sub> theo T có hệ số nhiệt độ của điện trở âm nhỏ, cỡ "
                "−1% °C<sup>−1</sup>. Khi nhiệt độ tăng, hệ số nhiệt độ của điện trở trở thành dương "
                "và điện trở bắt đầu tăng. Tại một nhiệt độ ngưỡng hay nhiệt độ chuyển mạch, tốc độ "
                "tăng trở nên rất nhanh và đặc tính PTC trở nên rất dốc. Trong dải chuyển mạch của "
                "nó, linh kiện có giá trị điện trở cao. Ở nhiệt độ trên dải chuyển mạch, điện trở "
                "đạt giá trị cực đại, vượt qua đó hệ số nhiệt độ lại trở thành âm.",
                "Hình 32.16 · Resistance–temperature characteristic of a typical switching-type "
                "PTC thermistor. At low temperatures, from below 0 °C to R<sub>min</sub>, the "
                "resistance value is low and R<sub>T</sub> vs. T exhibits a small negative "
                "temperature coefficient of resistance on the order of −1% °C<sup>−1</sup>. As the "
                "temperature increases, the temperature coefficient of resistance becomes positive "
                "and the resistance begins to rise. At a threshold or switching temperature, the "
                "rate of rise becomes very rapid and the PTC characteristic becomes very steep. "
                "Within its switching range, the device exhibits a high resistance value. At "
                "temperatures above the switching range, the resistance reaches a maximum value "
                "beyond which the temperature coefficient becomes negative again.",
                "Đường cong điện trở theo nhiệt độ: một đoạn thoải hơi dốc xuống, rồi dựng đứng "
                "thành vách, vượt qua mức R max, đạt đỉnh và hạ xuống ở cuối; hai đường gạch ngang "
                "đánh dấu mức R min và R max",
                "A resistance-versus-temperature curve that slopes gently down, rises almost "
                "vertically, overshoots the R max level to a peak and then falls; dashed level "
                "lines mark R min and R max")


# ---------------------------------------------------------------- 32.19
def _source(cx, cy, r=21.0):
    """An alternating source: a circle with one cycle of sine inside."""
    o = [_circ(cx, cy, r, "#fff", E, 1.3)]
    o.append(_pl([(cx - r * 0.50 + i * r / 20.0,
                   cy - 5.0 * _m.sin(2 * _m.pi * i / 20.0)) for i in range(21)], E, 1.1))
    return "".join(o)


def _term(x, y):
    """An open output terminal — a small white circle."""
    return _circ(x, y, 3.4, "#fff", E, 1.2)


def fig_32_19():
    """(a) the thermistor divider and (b) the S-shaped output it produces."""
    o = [_defs()]
    # ---- (a) the divider
    o.append(_source(96, 158))
    o.append(_pl([(96, 137), (96, 78), (222, 78)], E, 1.3))
    o.append(_therm(222, 110, 17))
    o.append(_pl([(222, 93), (222, 78)], E, 1.3))
    o.append(_pl([(222, 127), (222, 186)], E, 1.3))
    o.append(_res_v(222, 206, 26, 40))
    o.append(_pl([(222, 226), (222, 246), (96, 246), (96, 179)], E, 1.3))
    # taps
    o.append(_pl([(222, 160), (272, 160)], E, 1.3))
    o.append(_term(272, 160))
    o.append(_pl([(222, 246), (272, 246)], E, 1.3))
    o.append(_term(272, 246))

    o.append(_mix(244, 100, [("R", ""), ("T", "sub")], "start", "ts"))
    o.append(_lbl(250, 210, "R", "ts", "start"))
    o.append(_mix(64, 196, [("e", "i"), ("s", "sub")], "end", "ts"))
    o.append(_mix(280, 184, [("e", "i"), ("0", "sub"), ("(T)", "")], "start", "ts"))
    o.append(_lbl(160, 292, "(a)", "ts", "middle"))

    # ---- (b) the S-curve the divider produces
    o.append(_arr(380, 292, 380, 56, E, sw=1.4))
    o.append(_arr(368, 280, 654, 280, E, sw=1.4))
    o.append(_mix(372, 50, [("e", "i"), ("0", "sub"), ("(T)", "")], "end", "ts"))
    o.append(_lbl(0, 0, "TEMPERATURE", "ts", "middle",
                  ' transform="translate(516,306)"'))
    # the level the curve runs into
    o.append(_line(404, 102, 646, 102, S, 1.1, "7 5"))
    o.append(_mix(396, 106, [("e", "i"), ("s", "sub")], "end", "ts"))
    # a logistic, so the foot and shoulder are both genuinely flat — a straight
    # line from the axis to the first sample leaves a kink at the left end
    o.append(_pl([(x, 275 - 172.0 / (1 + _m.exp(-(x - 500) / 38.0)))
                  for x in range(382, 646, 4)], E, 1.8))
    o.append(_lbl(508, 330, "(b)", "ts", "middle"))

    return _fig(svg(680, 340, "".join(o),
                    "Cầu phân áp dùng nhiệt điện trở và đường cong đầu ra hình chữ S"),
                "Hình 32.19 · (a) Cầu phân áp dùng nhiệt điện trở. Điện trở R biểu diễn tổ hợp song "
                "song của điện trở tải và điện trở phân áp cố định. (b) Đầu ra, e<sub>0</sub> theo "
                "T, là một đường cong hình chữ S, tuyến tính trên một phần của dải nhiệt độ.",
                "Hình 32.19 · (a) Thermistor voltage divider. The resistor R represents the parallel "
                "combination of the load resistance and the fixed divider resistor. (b) The output, "
                "e<sub>0</sub> vs. T, is an S-shaped curve that is linear over a portion of the "
                "temperature range.",
                "Hình (a) một nguồn xoay chiều e s nối tiếp với nhiệt điện trở R T ở nhánh trên và "
                "điện trở R ở nhánh dưới, hai cực ra lấy ở giữa và ở đáy; hình (b) đường cong chữ S "
                "của đầu ra e 0 theo nhiệt độ, tiệm cận mức e s",
                "Panel (a) an alternating source in series with a thermistor and a fixed resistor, "
                "with two output terminals; panel (b) an S-shaped output curve rising towards the "
                "level e s")


# ---------------------------------------------------------------- 32.20
def _dot(x, y):
    return _circ(x, y, 2.7, E, E, 1.0)


def fig_32_20():
    """Four circuits: the two non-standard-source networks the book converts
    from (left) and the standard-source equivalents it converts to (right)."""
    o = [_defs()]

    # ---- (a) left: E1 driving R_T, R4, R3
    o.append(_batt(105, 160))
    o.append(_pl([(105, 156), (105, 70), (250, 70)], E, 1.3))
    o.append(_therm(250, 100, 18))
    o.append(_pl([(250, 70), (250, 82)], E, 1.3))
    o.append(_pl([(250, 118), (250, 130)], E, 1.3))
    o.append(_zz(250, 130, 250, 180))
    o.append(_pl([(250, 180), (250, 204)], E, 1.3))
    o.append(_zz(250, 204, 250, 244))
    o.append(_pl([(250, 244), (250, 250), (105, 250), (105, 164)], E, 1.3))
    o.append(_pl([(250, 192), (302, 192)], E, 1.3))
    o.append(_term(302, 192))
    o.append(_pl([(250, 250), (302, 250)], E, 1.3))
    o.append(_term(302, 250))
    o.append(_dot(250, 192))
    o.append(_dot(250, 250))
    o.append(_mix(122, 164, [("E", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(274, 92, [("R", ""), ("T", "sub")], "start", "ts"))
    o.append(_mix(274, 156, [("R", ""), ("4", "sub")], "start", "ts"))
    o.append(_mix(274, 226, [("R", ""), ("3", "sub")], "start", "ts"))
    o.append(_mix(310, 226, [("e", "i"), ("0", "sub")], "start", "ts"))
    # the conversion runs left to right
    o.append(_arr(330, 182, 370, 182, E, sw=1.3))

    # ---- (a) right: the standard-source equivalent
    o.append(_batt(410, 160))
    o.append(_pl([(410, 156), (410, 70), (470, 70)], E, 1.3))
    o.append(_zz(470, 70, 470, 118))
    o.append(_pl([(470, 118), (470, 162)], E, 1.3))
    o.append(_zz(470, 162, 470, 240))
    o.append(_pl([(470, 240), (470, 250), (410, 250), (410, 164)], E, 1.3))
    o.append(_pl([(470, 150), (520, 150), (520, 70), (590, 70)], E, 1.3))
    o.append(_therm(590, 100, 18))
    o.append(_pl([(590, 70), (590, 82)], E, 1.3))
    o.append(_pl([(590, 118), (590, 162)], E, 1.3))
    o.append(_zz(590, 162, 590, 240))
    o.append(_pl([(590, 240), (590, 250), (646, 250)], E, 1.3))
    o.append(_pl([(590, 150), (646, 150)], E, 1.3))
    o.append(_term(646, 150))
    o.append(_term(646, 250))
    o.append(_dot(470, 150))
    o.append(_dot(590, 150))
    o.append(_mix(392, 164, [("E", ""), ("2", "sub")], "end", "ts"))
    o.append(_mix(492, 96, [("R", ""), ("2", "sub")], "start", "ts"))
    o.append(_mix(492, 206, [("R", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(614, 92, [("R", ""), ("T", "sub")], "start", "ts"))
    o.append(_mix(614, 206, [("R", ""), ("3", "sub")], "start", "ts"))
    o.append(_mix(654, 206, [("e", "i"), ("0", "sub")], "start", "ts"))
    o.append(_lbl(350, 284, "(a)", "ts", "middle"))

    # ---- (b) left: E1 driving R_T and R only
    o.append(_batt(105, 450))
    o.append(_pl([(105, 446), (105, 360), (250, 360)], E, 1.3))
    o.append(_therm(250, 390, 18))
    o.append(_pl([(250, 360), (250, 372)], E, 1.3))
    o.append(_pl([(250, 408), (250, 444)], E, 1.3))
    o.append(_zz(250, 444, 250, 500))
    o.append(_pl([(250, 500), (250, 506), (105, 506), (105, 454)], E, 1.3))
    o.append(_pl([(250, 432), (302, 432)], E, 1.3))
    o.append(_term(302, 432))
    o.append(_pl([(250, 506), (302, 506)], E, 1.3))
    o.append(_term(302, 506))
    o.append(_dot(250, 432))
    o.append(_dot(250, 506))
    o.append(_mix(122, 454, [("E", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(274, 382, [("R", ""), ("T", "sub")], "start", "ts"))
    o.append(_lbl(274, 476, "R", "ts", "start"))
    o.append(_mix(310, 466, [("e", "i"), ("01", "sub")], "start", "ts"))

    # ---- (b) right: R2 in parallel with R_T, feeding R1
    o.append(_batt(410, 450))
    o.append(_pl([(410, 446), (410, 360), (470, 360)], E, 1.3))
    o.append(_zz(470, 360, 470, 408))
    o.append(_pl([(470, 408), (470, 442)], E, 1.3))
    o.append(_pl([(470, 360), (560, 360), (560, 372)], E, 1.3))
    o.append(_therm(560, 390, 18))
    o.append(_pl([(560, 408), (560, 430), (470, 430)], E, 1.3))
    o.append(_zz(470, 442, 470, 500))
    o.append(_pl([(470, 500), (470, 506), (410, 506), (410, 454)], E, 1.3))
    o.append(_pl([(470, 430), (646, 430)], E, 1.3))
    o.append(_pl([(470, 506), (646, 506)], E, 1.3))
    o.append(_term(646, 430))
    o.append(_term(646, 506))
    o.append(_dot(470, 360))
    o.append(_dot(470, 430))
    o.append(_dot(560, 430))
    o.append(_mix(392, 454, [("E", ""), ("2", "sub")], "end", "ts"))
    o.append(_mix(492, 390, [("R", ""), ("2", "sub")], "start", "ts"))
    o.append(_mix(584, 382, [("R", ""), ("T", "sub")], "start", "ts"))
    o.append(_mix(492, 478, [("R", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(654, 486, [("e", "i"), ("02", "sub")], "start", "ts"))
    o.append(_lbl(350, 574, "(b)", "ts", "middle"))

    return _fig(svg(700, 620, "".join(o),
                    "Bốn sơ đồ mạch tương đương của cầu phân áp nhiệt điện trở"),
                "Hình 32.20 · Các mạch tương đương của cầu phân áp nhiệt điện trở, dùng để chuyển "
                "một mạng có nguồn điện áp không chuẩn thành mạng dùng nguồn điện áp chuẩn. Ở (a) "
                "chỉ một phần điện áp ra là khả dụng. Các nhiệt kế kiểu ôm kế dùng những mạch này. "
                "Mạch chuyển đổi ở (b) cho toàn bộ điện áp ra khả dụng, nhưng mắc nối tiếp với một "
                "điện áp phân cực. (b) được dùng với các nhiệt kế kiểu mạch cầu.",
                "Hình 32.20 · Equivalent thermistor voltage divider circuits for converting a "
                "network with a nonstandard voltage source to a network that uses a standard "
                "voltage source. Only a portion of the output is available in (a). Ohmmeter-type "
                "thermometers use such circuits. The conversion circuit of (b) provides the full "
                "available output voltage in a series with a bias voltage. (b) is used with bridge "
                "circuit-type thermometers.",
                "Bốn sơ đồ mạch điện: hàng (a) gồm mạch dùng nguồn E 1 với nhiệt điện trở R T, R 4 "
                "và R 3, và mạch tương đương dùng nguồn E 2 với R 2, R 1, R T và R 3; hàng (b) gồm "
                "mạch dùng E 1 với R T và R, và mạch dùng E 2 với R 2 song song R T rồi nối tiếp "
                "R 1",
                "Four circuit diagrams: row (a) an E 1 network with a thermistor, R 4 and R 3 and "
                "its E 2 equivalent with R 2, R 1, the thermistor and R 3; row (b) an E 1 network "
                "with the thermistor and R, and an E 2 network with R 2 in parallel with the "
                "thermistor feeding R 1")


# ---------------------------------------------------------------- 32.21
def fig_32_21():
    """Three ways to reach a standard R_T0: the plain parallel network, the same
    with an insertion resistor, and the two-thermistor conversion."""
    o = [_defs()]

    def net(l, r, top, bot, lead_l, lead_r):
        """The common skeleton: a rectangle between terminals 1 and 2."""
        g = [_term(lead_l[0], 110), _pl([(lead_l[0], 110), (lead_l[1], 110)], E, 1.3)]
        g.append(_pl([(l, top), (l, 110), (l, bot)], E, 1.3))
        g.append(_pl([(r, top), (r, 110), (r, bot)], E, 1.3))
        g.append(_dot(l, 110))
        g.append(_dot(r, 110))
        g.append(_term(lead_r[0], 110))
        g.append(_pl([(lead_r[1], 110), (r, 110)], E, 1.3))
        return "".join(g)

    # (a) the basic parallel network
    o.append(net(60, 180, 55, 165, (35, 60), (205, 180)))
    o.append(_pl([(60, 55), (96, 55)], E, 1.3))
    o.append(_therm(120, 55, 16, horiz=True))
    o.append(_pl([(144, 55), (180, 55)], E, 1.3))
    o.append(_pl([(60, 165), (96, 165)], E, 1.3))
    o.append(_zz(96, 165, 144, 165))
    o.append(_pl([(144, 165), (180, 165)], E, 1.3))
    o.append(_mix(120, 26, [("R", ""), ("T", "sub"), (" = R", ""), ("T0", "sub"),
                            (" r(T)", "")], "middle", "ts"))
    o.append(_lbl(120, 152, "R", "ts", "middle"))
    o.append(_lbl(120, 206, "(a)", "ts", "middle"))

    # (b) the same, with the insertion resistor R1
    o.append(net(300, 420, 55, 165, (250, 262), (445, 420)))
    o.append(_zz(262, 110, 296, 110))
    o.append(_pl([(296, 110), (300, 110)], E, 1.3))
    o.append(_pl([(300, 55), (336, 55)], E, 1.3))
    o.append(_therm(360, 55, 16, horiz=True))
    o.append(_pl([(384, 55), (420, 55)], E, 1.3))
    o.append(_pl([(300, 165), (336, 165)], E, 1.3))
    o.append(_zz(336, 165, 384, 165))
    o.append(_pl([(384, 165), (420, 165)], E, 1.3))
    o.append(_mix(279, 96, [("R", ""), ("1", "sub")], "middle", "ts"))
    o.append(_mix(360, 26, [("R", ""), ("T", "sub"), (" = R", ""), ("T0", "sub"),
                            (" r(T)", "")], "middle", "ts"))
    o.append(_lbl(360, 152, "R", "ts", "middle"))
    o.append(_lbl(360, 206, "(b)", "ts", "middle"))

    # (c) the conversion, with R_E, R_A and R_B
    o.append(net(530, 680, 55, 165, (470, 482), (705, 680)))
    o.append(_zz(482, 110, 520, 110))
    o.append(_pl([(520, 110), (530, 110)], E, 1.3))
    o.append(_pl([(530, 55), (556, 55)], E, 1.3))
    o.append(_therm(580, 55, 16, horiz=True))
    o.append(_pl([(604, 55), (626, 55)], E, 1.3))
    o.append(_zz(626, 55, 662, 55))
    o.append(_pl([(662, 55), (680, 55)], E, 1.3))
    o.append(_pl([(530, 165), (590, 165)], E, 1.3))
    o.append(_zz(590, 165, 620, 165))
    o.append(_pl([(620, 165), (680, 165)], E, 1.3))
    o.append(_mix(501, 96, [("R", ""), ("E", "sub")], "middle", "ts"))
    o.append(_mix(578, 24, [("R", ""), ("T", "sub"), (" = R\u2032", ""), ("T0", "sub"),
                            (" r(T)", "")], "middle", "ts"))
    o.append(_mix(644, 42, [("R", ""), ("A", "sub")], "middle", "ts"))
    o.append(_mix(605, 152, [("R", ""), ("B", "sub")], "middle", "ts"))
    o.append(_lbl(605, 206, "(c)", "ts", "middle"))

    return _fig(svg(740, 250, "".join(o),
                    "Ba mạng nhiệt điện trở tuyến tính tương đương, nối song song giữa hai cực"),
                "Hình 32.21 · Các mạng nhiệt điện trở tuyến tính tương đương, dùng để chuyển một "
                "mạng có R<sub>T0</sub> không chuẩn thành mạng có giá trị R′<sub>T0</sub> chuẩn theo "
                "catalog. Yêu cầu là cả hai nhiệt điện trở phải có cùng đặc tính tỉ số điện trở – "
                "nhiệt độ.",
                "Hình 32.21 · Equivalent linear thermistor networks for converting a network with a "
                "nonstandard R<sub>T0</sub> to a network with a standard catalog value for "
                "R′<sub>T0</sub>. A requirement is that both thermistors have the same resistance "
                "ratio–temperature characteristic.",
                "Ba mạng song song giữa hai cực 1 và 2: (a) nhiệt điện trở song song với R, (b) "
                "thêm R 1 nối tiếp ở nhánh vào, (c) thêm R E nối tiếp cùng nhiệt điện trở mắc nối "
                "tiếp R A song song với R B",
                "Three parallel networks between terminals 1 and 2: (a) a thermistor in parallel "
                "with R, (b) the same with a series insertion resistor R 1, (c) a series R E with "
                "the thermistor plus R A in parallel with R B")


# ---------------------------------------------------------------- 32.22
def fig_32_22():
    """The two- and three-thermistor dividers. Both are the same skeleton — R1
    from terminal 1 to the output node, then n parallel thermistor branches to
    the bottom rail — so one routine draws both."""
    o = [_defs()]

    def net(xr, br, terms):
        """xr is the R1 column, br the x positions of the thermistor branches,
        terms the four terminal points. Both networks are the same skeleton, so
        the branch count is the only thing that differs."""
        t1, t2, t3, t4 = terms
        g = []
        # top rail and R1
        g.append(_pl([(t1[0], t1[1]), (xr, t1[1])], E, 1.3))
        g.append(_zz(xr, t1[1], xr, t1[1] + 55))
        g.append(_pl([(xr, t1[1] + 55), (xr, 130)], E, 1.3))
        g.append(_dot(xr, 130))
        g.append(_pl([(xr, 130), (t3[0], t3[1])], E, 1.3))
        # the branch bus
        g.append(_pl([(xr, 130), (br[0], 130)], E, 1.3))
        for bx in br:
            g.append(_dot(bx, 130))
            g.append(_zz(bx, 130, bx, 185))
            g.append(_pl([(bx, 185), (bx, 208)], E, 1.3))
            g.append(_therm(bx, 225, 17))
            g.append(_pl([(bx, 242), (bx, 320)], E, 1.3))
        # T1 hangs straight off the output node, on the R1 column — it is the
        # one branch that is not inside a series pair
        g.append(_pl([(xr, 130), (xr, 208)], E, 1.3))
        g.append(_therm(xr, 225, 17))
        g.append(_pl([(xr, 242), (xr, 320)], E, 1.3))
        # the bottom rail and the terminal pair
        g.append(_pl([(t2[0], t2[1]), (t4[0], t4[1])], E, 1.3))
        for bx in br:
            g.append(_dot(bx, 320))
        # E_in and E_0
        g.append(_darr(t1[0], t1[1] + 12, t2[0], t2[1] - 12))
        g.append(_darr(t3[0], t3[1] + 12, t4[0], t4[1] - 12))
        # the matched set — the box takes in T1 as well as the R/T branch pairs,
        # which is what the book's dashed outline does
        g.append(_rect(br[0] - 20, 112, (xr + 40) - (br[0] - 20), 190, "none", S, 1.2, "6 4"))
        g.append(_mix(xr + 46, 300, [("R", ""), ("T", "sub")], "start", "ts"))
        return "".join(g)

    # ---- two-thermistor network
    o.append(net(250, (150,), ((70, 50), (70, 320), (330, 130), (330, 320))))
    o.append(_mix(272, 80, [("R", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(172, 160, [("R", ""), ("2", "sub")], "start", "ts"))
    o.append(_mix(272, 232, [("T", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(172, 274, [("T", ""), ("2", "sub")], "start", "ts"))
    o.append(_term(70, 50))
    o.append(_term(70, 320))
    o.append(_term(330, 130))
    o.append(_term(330, 320))
    o.append(_lbl(56, 44, "1", "ts", "end"))
    o.append(_lbl(56, 334, "2", "ts", "end"))
    o.append(_lbl(340, 124, "3", "ts", "start"))
    o.append(_lbl(340, 334, "4", "ts", "start"))
    o.append(_mix(0, 0, [("E", ""), ("in", "sub")], "middle", "ts",
                  ' transform="translate(58,185) rotate(-90)"'))
    o.append(_mix(0, 0, [("E", ""), ("0", "sub")], "middle", "ts",
                  ' transform="translate(346,225) rotate(-90)"'))

    # ---- three-thermistor network
    o.append(net(580, (450, 515), ((410, 50), (410, 320), (670, 130), (670, 320))))
    o.append(_mix(602, 80, [("R", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(472, 160, [("R", ""), ("3", "sub")], "start", "ts"))
    o.append(_mix(537, 160, [("R", ""), ("2", "sub")], "start", "ts"))
    o.append(_mix(602, 232, [("T", ""), ("1", "sub")], "start", "ts"))
    o.append(_mix(472, 274, [("T", ""), ("3", "sub")], "start", "ts"))
    o.append(_mix(537, 274, [("T", ""), ("2", "sub")], "start", "ts"))
    o.append(_term(410, 50))
    o.append(_term(410, 320))
    o.append(_term(670, 130))
    o.append(_term(670, 320))
    o.append(_lbl(396, 44, "1", "ts", "end"))
    o.append(_lbl(396, 334, "2", "ts", "end"))
    o.append(_lbl(680, 124, "3", "ts", "start"))
    o.append(_lbl(680, 334, "4", "ts", "start"))
    o.append(_mix(0, 0, [("E", ""), ("in", "sub")], "middle", "ts",
                  ' transform="translate(398,185) rotate(-90)"'))
    o.append(_mix(0, 0, [("E", ""), ("0", "sub")], "middle", "ts",
                  ' transform="translate(686,225) rotate(-90)"'))

    return _fig(svg(720, 360, "".join(o),
                    "Cầu phân áp tuyến tính hai và ba nhiệt điện trở"),
                "Hình 32.22 · Cầu phân áp tuyến tính hai nhiệt điện trở và ba nhiệt điện trở, cho độ "
                "tuyến tính tốt hơn. Mắc các điện trở R<sub>1</sub> song song qua hai cực ra 3–4 sẽ "
                "biến các mạng này thành mạng điện trở tuyến tính.",
                "Hình 32.22 · Two-thermistor and three-thermistor linear voltage dividers that "
                "provide improved linearity. Placing the resistors R<sub>1</sub> across the output "
                "terminals 3–4 converts the networks to linear resistance networks.",
                "Hai mạng cầu phân áp có bốn cực 1, 2, 3, 4; mạng trái có một nhánh nhiệt điện trở "
                "T 2 mắc nối tiếp R 2 song song với T 1, mạng phải có thêm nhánh R 3 và T 3; đường "
                "gạch đứt bao quanh bộ nhiệt điện trở",
                "Two four-terminal divider networks; the left has one branch of R 2 in series with "
                "T 2 in parallel with T 1, the right adds an R 3 / T 3 branch; a dashed box encloses "
                "the matched thermistor set")


# ---------------------------------------------------------------- 32.18
def fig_32_18():
    """Current against time for three chip thermistors driven from a step in
    voltage. Three exponentials with different asymptotes, drawn on the book's
    ruled grid — the grid is what makes the millisecond detail readable."""
    o = [_defs()]
    L, R, T, B = 150.0, 600.0, 60.0, 340.0
    TMAX, IMAX = 28.0, 22.5

    def px(t):
        return L + t / TMAX * (R - L)

    def py(i):
        return B - i / IMAX * (B - T)

    # ruled grid, drawn first so the curves sit on top of it
    for i in (5, 10, 15, 20):
        o.append(_line(L, py(i), R, py(i), "#e3e7ec", 0.9))
    for t in (5, 10, 15, 20, 25):
        o.append(_line(px(t), B, px(t), T, "#e3e7ec", 0.9))
    o.append(_line(L, T, L, B + 8, E, 1.4))
    o.append(_line(L - 8, B, R + 8, B, E, 1.4))

    for i in (5, 10, 15, 20):
        o.append(_line(L - 5, py(i), L, py(i), E, 1.2))
        o.append(_lbl(L - 10, py(i) + 4, "%d" % i, "ts", "end"))
    for t in (0, 5, 10, 15, 20, 25):
        o.append(_line(px(t), B, px(t), B + 5, E, 1.2))
        o.append(_lbl(px(t), B + 19, "%d" % t, "ts", "middle"))

    o.append(_lbl(0, 0, "Current (mA)", "ts", "middle",
                  ' transform="translate(108,%d) rotate(-90)"' % int((T + B) / 2)))
    o.append(_lbl(0, 0, "Time (seconds)", "ts", "middle",
                  ' transform="translate(%d,%d)"' % (int((L + R) / 2), B + 40)))

    # I(t) = I0 + (Iinf - I0)(1 - exp(-t/tau)) for each of the three curves
    for i0, iinf, tau, name in ((5.0, 15.0, 6.0, "A"), (5.0, 17.5, 3.4, "B"),
                                (5.0, 20.0, 2.4, "C")):
        pts = [(px(t / 4.0), py(i0 + (iinf - i0) * (1 - _m.exp(-(t / 4.0) / tau))))
               for t in range(0, 101)]
        o.append(_pl(pts, E, 1.5))
        o.append(_lbl(px(TMAX) + 10, pts[-1][1] + 4, name, "t", "start"))

    # inset: the test circuit, on a white patch so the grid does not run through it
    o.append(_rect(404, 218, 194, 116, "#fff", E, 1.0))
    o.append(_pl([(424, 242), (568, 242)], E, 1.2))
    o.append(_pl([(424, 242), (424, 316)], E, 1.2))
    o.append(_pl([(424, 316), (568, 316)], E, 1.2))
    o.append(_pl([(568, 242), (568, 316)], E, 1.2))
    o.append(_therm(496, 242, 14))
    o.append(_res_v(568, 280, 9, 30))
    o.append(_mix(582, 284, [("R", ""), ("L", "sub")], "start", "ts"))
    o.append(_line(424, 266, 424, 292, "#fff", 3.4))
    o.append(_line(414, 272, 434, 272, E, 1.4))
    o.append(_line(419, 280, 429, 280, E, 2.6))
    o.append(_line(424, 280, 424, 316, E, 1.2))
    o.append(_mix(418, 268, [("E", "")], "end", "ts"))
    # the switch, open at rest
    o.append(_circ(478, 316, 2.4, E, E, 1.0))
    o.append(_circ(504, 316, 2.4, E, E, 1.0))
    o.append(_line(480, 315, 502, 304, E, 1.3))

    return _fig(svg(680, 420, "".join(o),
                    "Đặc tính dòng theo thời gian của ba nhiệt điện trở chip, có lưới chia độ"),
                "Hình 32.18 · Đặc tính dòng – thời gian của các nhiệt điện trở chip phủ epoxy của "
                "Thermometrics, Inc. Đường A và C ứng với một chiếc DC95F402 có điện trở ở công "
                "suất không tại 25 °C là 4 kΩ. Đường B ứng với một chiếc DC9F802 có điện trở ở công "
                "suất không tại 25 °C là 8 kΩ. Kích thích là một bước nhảy điện áp qua một nguồn "
                "tương đương Thevenin. Với đường A, điện áp nguồn là 24 V và điện trở nguồn là 1 kΩ. "
                "Với đường B và C, điện áp nguồn là 48 V và điện trở nguồn là 2 kΩ.",
                "Hình 32.18 · Current–time characteristics of Thermometrics, Inc. epoxy-coated chip "
                "thermistors. Curves A and C are for a DC95F402 having a zero-power resistance at "
                "25 °C of 4 kΩ. Curve B is for a DC9F802 having a zero-power resistance at 25 °C of "
                "8 kΩ. The excitation is a step function in voltage through a Thevenin equivalent "
                "source. The source voltage and resistance values for curve A are 24 V and 1 kΩ, "
                "respectively. For curves B and C, the source voltage is 48 V and source resistance "
                "is 2 kΩ.",
                "Ba đường cong dòng theo thời gian cùng xuất phát từ 5 mA và tiến dần tới các giá "
                "trị 15, 17,5 và 20 mA, trên một lưới chia độ; góc dưới bên phải có sơ đồ mạch thử "
                "gồm nguồn E, nhiệt điện trở, điện trở tải R L và một công tắc",
                "Three current-versus-time curves starting together at 5 mA and levelling off at "
                "15, 17.5 and 20 mA on a ruled grid, with a small test circuit inset at lower right")


# ---------------------------------------------------------------- 32.17
def fig_32_17():
    """Voltage against current for a self-heated NTC thermistor, with the
    Thevenin load line and the operating point where it cuts the curve."""
    o = [_defs()]
    AX, AY = 118.0, 350.0
    o.append(_arr(AX, AY + 10, AX, 40, E, sw=1.5))
    o.append(_arr(AX - 14, AY, 622, AY, E, sw=1.5))
    o.append(_mix(104, 50, [("E", ""), ("T", "sub")], "end"))
    o.append(_mix(630, 368, [("I", ""), ("T", "sub")], "start"))

    # the V-I curve: steep rise, a maximum, then a slow negative-resistance fall
    o.append(_pl([(120, 350), (123, 300), (128, 268), (136, 238), (148, 212),
                  (165, 190), (186, 173), (210, 160), (238, 152), (268, 149),
                  (300, 152), (340, 162), (390, 176), (450, 190), (520, 203),
                  (590, 212), (622, 217)], E, 1.9))
    # The load line is chosen so that it really does cut the curve: above the
    # peak at 268, level with it at 450.  Drawing the dot at a fixed point and
    # hoping the line passes through it is how fig 32.17 went wrong first time.
    o.append(_line(150, 82, 622, 252, E, 1.5))
    o.append(_circ(450, 190, 3.6, E, E, 1.0))
    o.append(_on_line(150, 82, 622, 252, [("LOAD LINE", "")], off=-13, frac=0.34, cls="ts"))

    # inset: the Thevenin equivalent looking into the thermistor terminals
    o.append(_pl([(415, 68), (605, 68)], E, 1.2))
    o.append(_pl([(415, 68), (415, 140)], E, 1.2))
    o.append(_pl([(415, 140), (605, 140)], E, 1.2))
    o.append(_pl([(605, 68), (605, 140)], E, 1.2))
    o.append(_res_h(462, 68, 34, 9))
    o.append(_mix(462, 56, [("R", ""), ("THEV", "sub")], "middle", "ts"))
    # battery on the left leg
    o.append(_line(415, 92, 415, 118, "#fff", 3.2))
    o.append(_line(405, 96, 425, 96, E, 1.4))
    o.append(_line(410, 104, 420, 104, E, 2.6))
    o.append(_line(415, 104, 415, 140, E, 1.2))
    o.append(_mix(430, 100, [("E", ""), ("THEV", "sub")], "start", "ts"))
    o.append(_therm(605, 104, 15))
    # the terminals the equivalent is taken with respect to
    for y in (68, 140):
        o.append(_circ(540, y, 3.2, "#fff", E, 1.1))
        o.append(_arr(560, y, 545, y, E, sw=1.0))
    o.append(_arcarr(508, 104, 31, 72, 224, E, 1.1))
    o.append(_mix(474, 132, [("I", ""), ("T", "sub")], "middle", "ts"))

    o.append(_mix(470, 170, [("OPERATING POINT", "")], "start", "ts"))
    o.append(_arr(466, 174, 456, 187, E, sw=0.9))
    return _fig(svg(680, 400, "".join(o),
                    "Đặc tính dòng – áp của nhiệt điện trở NTC tự đốt nóng, kèm đường tải và điểm làm việc"),
                "Hình 32.17 · Đặc tính dòng – áp điển hình của một nhiệt điện trở NTC. Do hiện tượng "
                "tự đốt nóng, độ dốc của đường E<sub>T</sub> theo I<sub>T</sub> giảm khi dòng tăng. "
                "Điều này tiếp diễn cho đến khi E<sub>T</sub> đạt cực đại, tại đó độ dốc bằng không. "
                "Vượt qua giá trị này, độ dốc tiếp tục giảm và nhiệt điện trở thể hiện đặc tính điện "
                "trở âm. Mạch tương đương Thevenin nhìn từ hai cực của nhiệt điện trở cho một quan "
                "hệ tuyến tính giữa E<sub>T</sub> và I<sub>T</sub>, vẽ được thành đường tải. Giao "
                "điểm của đường tải với đường E<sub>T</sub> theo I<sub>T</sub> là điểm làm việc.",
                "Hình 32.17 · Typical voltage–current characteristic of an NTC thermistor. Due to "
                "self-heating of the thermistor, the slope of the E<sub>T</sub> vs. I<sub>T</sub> "
                "curve decreases with increasing current. This continues until a maximum value of "
                "E<sub>T</sub> is reached for which the slope is equal to zero. Beyond this value, "
                "the slope continues to decrease and the thermistor exhibits a negative resistance "
                "characteristic. The Thevenin equivalent circuit with respect to the thermistor "
                "terminals provides a straight-line relationship between E<sub>T</sub> and "
                "I<sub>T</sub> that can be plotted as a load line. The intersection of the load "
                "line with the E<sub>T</sub> vs. I<sub>T</sub> curve is the operating point.",
                "Đường đặc tính dòng – áp dốc lên từ gốc, đạt đỉnh rồi hạ thoải; một đường thẳng "
                "gọi là đường tải cắt nó tại điểm làm việc; góc trên bên phải có sơ đồ mạch tương "
                "đương Thevenin gồm R THEV, nguồn E THEV và nhiệt điện trở",
                "A current–voltage characteristic rising from the origin to a peak then falling "
                "slowly, cut by a straight load line at the operating point, with a Thevenin "
                "equivalent inset at upper right")


# ---- 32.24
def fig_32_24():
    """The modern digital thermocouple thermometer: a hand-held indicator with the
    probe plugged into its jack.  The book's photograph is redrawn as line art —
    LCD, type-selector pills, the probe loop and the measuring junction inside its
    dashed circle."""
    o = [_defs()]
    # body of the indicator
    o.append(_rect(40, 46, 212, 168, "#fff", E, 1.6, rx=14))
    # LCD
    o.append(_rect(58, 62, 176, 46, "#fff", E, 1.4, rx=4))
    o.append(_lbl(146, 94, "19.9 °C", "t", "middle", _fs(17)))
    # thermocouple-type selector: four pills under a shared frame
    o.append(_rect(66, 120, 140, 28, "none", E, 1.1, rx=6))
    for i, k in enumerate("EJKT"):
        x = 74 + i * 33
        o.append(_rect(x, 124, 26, 20, "#fff", E, 1.0, rx=3))
        o.append(_lbl(x + 13, 138, k, "ts", "middle", _fs(9)))
    o.append(_lbl(136, 162, "TC TYPE", "ts", "middle", _fs(8)))
    # the ON key
    o.append(_rect(190, 176, 50, 24, "#fff", E, 1.1, rx=11))
    o.append(_lbl(215, 192, "ON", "ts", "middle", _fs(8)))
    # jack on the right edge, with the reference temperature beside it
    o.append(_rect(252, 112, 26, 30, "#fff", E, 1.3, rx=3))
    o.append(_lbl(265, 131, "T", "ts", "middle", _fs(9)))
    o.append(_mix(284, 156, [("T", ""), ("r", "sub")], "start", "ts"))
    o.append(_line(279, 146, 284, 152, E, 0.9))
    # the probe: a loop of cable from the jack up to the plug, sampled from a cubic
    # so it sags the way the lead does in the photograph instead of kinking
    def _cubic(p0, p1, p2, p3, n=26):
        out = []
        for i in range(n + 1):
            t = i / float(n)
            u = 1 - t
            out.append((u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0],
                        u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]))
        return out

    o.append(_pl(_cubic((278, 127), (316, 133), (296, 58), (352, 74)), E, 1.4))
    o.append(_rect(352, 62, 34, 24, "#fff", E, 1.3, rx=3))
    o.append(_lbl(369, 79, "K", "ts", "middle", _fs(9)))
    # the measuring junction, in its dashed circle
    o.append(_pl([(386, 74), (430, 74)], E, 1.4))
    o.append(_circ(430, 74, 3.2, E, E, 1.0))
    o.append(_circ(430, 74, 25, "none", S, 1.1, dash="4 3"))
    # inside the circle, above the junction: outside it the subscript ran through
    # the ring
    o.append(_mix(430, 60, [("T", ""), ("m", "sub")], "middle", "ts"))
    o.append(_lbl(430, 128, "measuring junction", "ts", "middle", _fs(8)))
    o.append(_lbl(369, 44, "plug", "ts", "middle", _fs(8)))
    return _fig(svg(680, 240, "".join(o),
                    "Máy đo nhiệt độ cặp nhiệt điện kỹ thuật số cầm tay với đầu dò"),
                "Hình 32.24 · Máy đo nhiệt độ cặp nhiệt điện kỹ thuật số hiện đại. Điện tử số "
                "đã làm cho việc đo nhiệt độ thông thường trở nên rất dễ dàng, nhưng cũng che "
                "khuất nhu cầu thường trực về một hiểu biết đúng đắn các nguyên lý nhiệt điện, "
                "nhằm đạt độ chính xác với những mạch phức tạp hơn và những phép đo quan "
                "trọng hơn.",
                "Figure 32.24 · The simple modern digital thermocouple thermometer. Modern "
                "digital electronics has made casual thermometry very easy, but has obscured "
                "the continuing need to have an authentic understanding of thermoelectric "
                "principles for accurate thermometry with more complicated circuits and more "
                "important measurements.",
                "Máy đo cầm tay có màn hình hiển thị 19,9 °C, hàng nút chọn loại cặp nhiệt "
                "điện E J K T, phích cắm đầu dò và mối nối đo trong vòng tròn nét đứt",
                "Hand-held indicator showing 19.9 °C with E J K T type buttons, a probe plug "
                "and the measuring junction inside a dashed circle")


def _rot(t, x, y):
    """Lay a label out vertically (bottom-up), the way the book marks the
    narrow isothermal zones.  _mix() output is injected with a transform."""
    return t.replace('<text ', '<text transform="rotate(-90 %d %d)" ' % (x, y), 1)


# ---- 32.25
def fig_32_25():
    """The basic thermocouple circuit with a single temperature reference
    junction e: measuring junction b at T_m, reference junction e at T_r,
    intermediate material C between junctions c and d, and the ice bath at
    T_i carrying the open-circuit terminals a and f."""
    o = []
    B = ' style="font-weight:700"'
    # ice bath: drop shadow, box, dashed inner isothermal zone
    o.append(_rect(224, 138, 190, 98, "#d9dee4", "none", 0, rx=10))
    o.append(_rect(217, 131, 190, 98, "#fff", E, 1.3, rx=10))
    o.append(_rect(254, 149, 135, 68, "none", S, 1.1, dash="4 3", rx=6))
    # upper leg e - d - (material C) - c - b ; lower legs e-A'-f and b-A-a
    o.append(_pl([(78, 84), (153, 42), (282, 44), (370, 44), (501, 42), (574, 84)], E, 1.4))
    o.append(_pl([(78, 84), (149, 126), (278, 126), (278, 182)], E, 1.4))
    o.append(_pl([(574, 84), (495, 126), (357, 126), (357, 182)], E, 1.4))
    # isothermal-zone outlines: T_r at left, the C link, T_m at right
    o.append(_ell(81, 85, 62, 28, "none", S, 1.1, dash="4 3"))
    o.append(_ell(326, 42, 68, 20, "none", S, 1.1, dash="4 3"))
    o.append(_ell(560, 85, 62, 28, "none", S, 1.1, dash="4 3"))
    # junction dots
    for x, y in ((78, 84), (282, 44), (370, 44), (574, 84), (278, 182), (357, 182)):
        o.append(_circ(x, y, 3, E, E, 1))
    # labels
    o.append(_mix(44, 88, [("T", "i"), ("r", "sub")]))
    o.append(_mix(94, 88, [("e", "i")], "middle"))
    o.append(_lbl(234, 26, "B′", "t", "middle", B))
    o.append(_lbl(234, 148, "A′", "t", "middle", B))
    o.append(_lbl(476, 26, "B", "t", "middle", B))
    o.append(_lbl(476, 148, "A", "t", "middle", B))
    o.append(_lbl(326, 34, "C", "t", "middle", B))
    o.append(_lbl(296, 58, "d", "t", "middle"))
    o.append(_lbl(356, 58, "c", "t", "middle"))
    o.append(_lbl(560, 88, "b", "t", "middle"))
    o.append(_mix(602, 88, [("T", "i"), ("m", "sub")], "middle"))
    o.append(_lbl(292, 176, "f", "t", "middle"))
    o.append(_lbl(348, 176, "a", "t", "middle"))
    o.append(_mix(321, 202, [("T", "i"), ("i", "sub")], "middle"))
    return _fig(svg(680, 250, "".join(o),
                    "Mạch cặp nhiệt điện cơ bản với một mối nối chuẩn nhiệt độ duy nhất e"),
                "Hình 32.25 · Mạch cặp nhiệt điện cơ bản với một mối nối chuẩn nhiệt độ duy nhất, "
                "e. Điện áp Seebeck đo ở chế độ hở mạch tại hai cực a và f tỉ lệ với chênh lệch "
                "nhiệt độ giữa mối nối đo b của cặp nhiệt điện và mối nối chuẩn cần thiết e. Để "
                "thuận tiện, T<sub>r</sub> thường được giữ ở 0 °C. Để đo nhiệt độ, các vùng ở "
                "nhiệt độ T<sub>r</sub> và T<sub>i</sub> phải đẳng nhiệt.",
                "Figure 32.25 · The basic thermocouple circuit with a single temperature "
                "reference junction, e. The Seebeck voltage measured in open-circuit mode at "
                "terminals a and f is proportional to the temperature difference between "
                "thermocouple measuring junction b and the necessary temperature reference "
                "junction e. For convenience, T<sub>r</sub> is usually made to be 0 °C. For "
                "thermometry, the zones at temperatures T<sub>r</sub> and T<sub>i</sub> must "
                "be isothermal.",
                "Sơ đồ mạch cặp nhiệt điện một mối nối chuẩn: mối nối đo b ở T_m bên phải, mối "
                "nối chuẩn e ở T_r bên trái, vật liệu trung gian C giữa hai mối nối c và d trên "
                "dây trên, và bình đá T_i ở giữa dưới với hai cực a và f",
                "Single-reference thermocouple circuit diagram: measuring junction b at T_m at "
                "right, reference junction e at T_r at left, intermediate material C between "
                "junctions c and d on the upper leg, and the T_i ice bath at bottom center "
                "with terminals a and f")


# ---- 32.26
def fig_32_26():
    """The basic thermocouple circuit with dual temperature reference junctions:
    principal pair A-B joined at the measuring junction d, extension leads C-D,
    input terminals b-f on the isothermal block (zone T_i) with the dashed
    internal compensation pair A'-B' referencing T_0, and the alternative
    reference zone T_s around junctions c and e."""
    o = []
    B = ' style="font-weight:700"'
    # isothermal block with its dashed boundary
    o.append(_rect(20, 30, 222, 196, "none", S, 1.1, dash="5 3", rx=12))
    o.append(_rect(35, 41, 185, 172, FILL, E, 1.3, rx=8))
    # the two dashed junction zones on the block, and the T_s terminal zone
    o.append(_ell(93, 129, 15, 56, "none", S, 1.1, dash="4 3"))
    o.append(_ell(184, 129, 15, 56, "none", S, 1.1, dash="4 3"))
    o.append(_rect(290, 57, 82, 147, "none", S, 1.1, dash="4 3", rx=10))
    # internal circuit g-a and the dashed compensation pair A'-B'
    o.append(_line(93, 85, 93, 174, E, 1.2))
    o.append(_line(93, 85, 185, 85, E, 1.3, dash="5 3"))
    o.append(_line(93, 174, 184, 174, E, 1.3, dash="5 3"))
    # extension leads D (upper) and C (lower), principal legs B and A
    o.append(_pl([(185, 85), (490, 85), (545, 125)], E, 1.4))
    o.append(_pl([(184, 174), (490, 174), (545, 131)], E, 1.4))
    # measuring-junction lozenge, bead, then dots
    o.append(_ell(570, 128, 66, 32, "none", S, 1.1, dash="4 3"))
    o.append(_ell(556, 128, 17, 9, DARK, E, 1.2))
    for x, y in ((93, 85), (93, 174), (185, 85), (184, 174),
                 (346, 85), (345, 174), (556, 128)):
        o.append(_circ(x, y, 3, E, E, 1))
    # zone temperatures, rotated inside the narrow capsules
    o.append(_rot(_mix(84, 129, [("T", "i"), ("0", "sub")], "middle"), 84, 129))
    o.append(_rot(_mix(184, 129, [("T", "i"), ("i", "sub")], "middle"), 184, 129))
    # wire labels
    o.append(_lbl(138, 64, "B′", "t", "middle", B))
    o.append(_lbl(139, 191, "A′", "t", "middle", B))
    o.append(_lbl(254, 63, "+", "t", "middle"))
    o.append(_lbl(254, 197, "−", "t", "middle"))
    o.append(_lbl(276, 63, "D", "t", "middle", B))
    o.append(_lbl(276, 197, "C", "t", "middle", B))
    o.append(_lbl(476, 64, "B", "t", "middle", B))
    o.append(_lbl(476, 197, "A", "t", "middle", B))
    # T_s zone label, then the terminals e and c
    o.append(_mix(331, 48, [("T", "i"), ("s", "sub")], "middle"))
    o.append(_lbl(346, 104, "e", "t", "middle"))
    o.append(_mix(346, 126, [("T", "i"), ("e", "sub")], "middle"))
    o.append(_lbl(346, 148, "c", "t", "middle"))
    o.append(_mix(346, 196, [("T", "i"), ("c", "sub")], "middle"))
    # measuring junction d, terminal m, temperature T_m
    o.append(_lbl(556, 150, "d", "t", "middle"))
    o.append(_lbl(588, 122, "m", "t", "middle"))
    o.append(_mix(616, 131, [("T", "i"), ("m", "sub")], "middle"))
    return _fig(svg(680, 240, "".join(o),
                    "Mạch cặp nhiệt điện cơ bản với hai mối nối chuẩn nhiệt độ"),
                "Hình 32.26 · Mạch cặp nhiệt điện cơ bản với hai mối nối chuẩn nhiệt độ. Cặp "
                "nhiệt điện chính là cặp AB; cặp CD là dây dẫn nối dài. Điện áp Seebeck đo ở "
                "chế độ hở mạch giữa hai cực b và f tỉ lệ với chênh lệch nhiệt độ giữa mối nối "
                "đo d của cặp nhiệt điện và các mối nối chuẩn cần thiết. Tùy theo loại dây nối "
                "dài, các mối nối chuẩn có thể là c và e, hoặc là b và f. Để đo nhiệt độ, các "
                "vùng ở nhiệt độ T<sub>s</sub> và T<sub>i</sub> phải đẳng nhiệt.",
                "Figure 32.26 · The basic thermocouple circuit with dual temperature reference "
                "junctions. The principal thermocouple is the AB pair. Pair CD is the extension "
                "lead. The Seebeck voltage measured in open-circuit mode between terminals b "
                "and f is proportional to the temperature difference between thermocouple "
                "measuring junction d and the necessary temperature reference junctions. "
                "Depending on the type of extension leads, the reference junctions might be "
                "either c and e, or else b and f. For thermometry, the zones at temperatures "
                "T<sub>s</sub> and T<sub>i</sub> must be isothermal.",
                "Mạch cặp nhiệt điện hai mối nối chuẩn: mối nối đo d bên phải, hai dây chính B "
                "và A chạy về hai cực e và c trong vùng T_s, dây nối dài D và C tới hai cực "
                "đầu vào f và b trên khối đẳng nhiệt T_i, bên trong có cặp bù nét đứt A′-B′ "
                "nối tới vùng chuẩn T_0",
                "Dual-reference thermocouple circuit: measuring junction d at right, principal "
                "legs B and A running to terminals e and c in the T_s zone, extension leads D "
                "and C to input terminals f and b on the T_i isothermal block, with the dashed "
                "internal compensation pair A′-B′ referencing T_0 inside")


# ---- 32.27  (grounding / shielding, sub-figures a–g)
def _twpair(x0, x1, y, n=4, col=E, sw=1.3):
    """A twisted-pair segment: two wires that cross n times."""
    seg = (x1 - x0) / (2 * n)
    pts_top, pts_bot = [], []
    for i in range(2 * n + 1):
        x = x0 + i * seg
        if i % 2 == 0:
            pts_top.append((x, y - 7)); pts_bot.append((x, y + 7))
        else:
            pts_top.append((x, y + 7)); pts_bot.append((x, y - 7))
    return _pl(pts_top, col, sw) + _pl(pts_bot, col, sw)


def _tblock(x, yc):
    """3-terminal input block; returns svg + the three terminal y coords."""
    w, h = 40, 34
    out = [_rect(x, yc - h / 2, w, h, "#fff", E, 1.3, rx=3)]
    ys = [yc - 9, yc, yc + 9]
    for yy in ys:
        out.append(_line(x + w, yy, x + w + 6, yy, E, 1.1))
    out.append(_lbl(x + w / 2, yc - 15, "+", "ts", "middle", _fs(9)))
    out.append(_lbl(x + w / 2, yc + 3, "−", "ts", "middle", _fs(9)))
    out.append(_lbl(x + w / 2, yc + 21, "o", "ts", "middle", _fs(9)))
    return "".join(out), ys


def _gnd(x, y, label, col=E):
    out = [_line(x, y, x, y + 12, col, 1.2),
           _line(x - 9, y + 12, x + 9, y + 12, col, 1.2),
           _line(x - 6, y + 16, x + 6, y + 16, col, 1.2),
           _line(x - 3, y + 20, x + 3, y + 20, col, 1.2),
           _lbl(x, y + 30, label, "ts", "middle", _fs(8))]
    return "".join(out)


def fig_32_27():
    """Preferred grounding and shielding for several thermometry situations
    (sub-figures a–g).  EM and ES noise are controlled by different means."""
    o = [_defs()]
    W, H = 780, 762
    N = 7
    top = 28
    rh = (H - top - 44) / N
    subj_x0, subj_x1 = 40, 60
    # test-subject bar (hatched), with a rotated label
    o.append(_rect(subj_x0, top, subj_x1 - subj_x0, N * rh, "url(#w32)", E, 1.2))
    o.append(_rot(_lbl((subj_x0 + subj_x1) / 2 + 2, top + N * rh / 2,
                        "Test Subject", "ts", "middle", _fs(9)),
                   (subj_x0 + subj_x1) / 2 + 2, top + N * rh / 2))
    # right rails
    rail_out, rail_in = 672, 652
    o.append(_line(rail_out, top, rail_out, top + N * rh, E, 1.3))
    o.append(_line(rail_in, top, rail_in, top + N * rh, E, 1.3))
    o.append(_lbl(rail_out + 4, top - 6, "+", "ts", "start", _fs(9)))
    o.append(_lbl(rail_in + 4, top - 6, "−", "ts", "start", _fs(9)))
    # grounds at the bottom
    gy = top + N * rh + 16
    o.append(_line(rail_out, top + N * rh, rail_out, gy, E, 1.2))
    o.append(_gnd(rail_out, gy, "Guard Power Gnd"))
    o.append(_line(subj_x1, top + N * rh, subj_x1, gy, E, 1.2))
    o.append(_gnd(subj_x1, gy, "Subject Gnd"))
    block_x = 560
    for i in range(N):
        yc = top + i * rh + rh / 2
        iz_x = subj_x1 + 8
        o.append(_rect(iz_x, yc - 13, 10, 26, "url(#h32)", E, 1.0))  # isolation/coupling
        tp0 = iz_x + 16
        tp1 = block_x - 14
        o.append(_line(tp0, yc - 7, tp1, yc - 7, E, 1.3))
        o.append(_line(tp0, yc + 7, tp1, yc + 7, E, 1.3))
        o.append(_twpair(tp0, tp1, yc, n=4))
        svg_b, ys = _tblock(block_x, yc)
        o.append(svg_b)
        o.append(_line(block_x + 40, ys[0], rail_out, ys[0], E, 1.1))
        o.append(_line(block_x + 40, ys[1], rail_in, ys[1], E, 1.1))
        # guard return: drop clear of the lower signal wire before running left
        o.append(_pl([(block_x + 40, ys[2]), (block_x + 40, yc + 24),
                      (tp0 - 4, yc + 24)], E, 1.1, "3 3"))
        if i == 0:
            o.append(_circ(tp0 + 7, yc - 7, 2.4, "none", E, 1.0))
            o.append(_lbl(block_x + 50, ys[0] - 2, "Tr", "ts", "start", _fs(8)))
            o.append(_mix(iz_x + 7, yc - 20, [("T", "i"), ("m", "sub")], "middle", "ts", _fs(8)))
            o.append(_mix(iz_x + 7, yc + 22, [("T", "i"), ("s", "sub")], "middle", "ts", _fs(8)))
            o.append(_lbl(iz_x + 20, top + 2, "Electrical Isolation", "ts", "start", _fs(8)))
            o.append(_lbl(iz_x + 20, top + 12, "Thermal Coupling", "ts", "start", _fs(8)))
        elif i == 1:
            o.append(_circ(subj_x1 + 13, yc, 2.6, E, E, 1.0))
            o.append(_circ(tp0 + 5, yc - 7, 2.2, "none", E, 1.0))
            o.append(_circ(tp0 + 5, yc + 7, 2.2, "none", E, 1.0))
        else:  # 2..6: oval coupling element with open-circle marks + dashed links
            oval_x = (tp0 + tp1) / 2
            o.append(_ell(oval_x, yc, 14, 20, "none", S, 1.1, dash="4 3"))
            o.append(_circ(oval_x, yc - 8, 2.0, "none", E, 1.0))
            o.append(_circ(oval_x, yc + 8, 2.0, "none", E, 1.0))
            o.append(_line(oval_x - 16, yc, oval_x - 2, yc, E, 1.0, dash="4 3"))
            o.append(_line(oval_x + 2, yc, oval_x + 16, yc, E, 1.0, dash="4 3"))
            if i == 2:
                o.append(_path("M %d,%d q -16,0 -16,16 q 0,16 16,16" % (subj_x1 + 8, yc - 7), E, 1.2))
            elif i == 3:
                o.append(_path("M %d,%d h -14 v 14 h 14 v -10" % (subj_x1 + 8, yc - 7), E, 1.2))
            elif i == 4:
                o.append(_path("M %d,%d q -18,-12 -18,4 q 0,18 18,4" % (subj_x1 + 8, yc - 7), E, 1.2))
            elif i == 5:
                o.append(_path("M %d,%d q -22,-4 -22,8 q 0,18 22,6" % (subj_x1 + 8, yc - 7), E, 1.2))
            else:
                o.append(_path("M %d,%d l -14,-8 M %d,%d l -14,8"
                               % (subj_x1 + 8, yc - 7, subj_x1 + 8, yc + 7), E, 1.2))
        o.append(_lbl(subj_x1 + 3, yc - rh / 2 + 11, "(%s)" % chr(97 + i), "ts", "start", _fs(9)))
    return _fig(svg(W, H, "".join(o),
                    "Nối đất và che chắn ưu tiên cho một số tình huống đo nhiệt độ"),
                "Hình 32.27 · Nối đất và che chắn ưu tiên cho một số tình huống đo nhiệt độ. Nhiễu "
                "điện từ (EM) và tĩnh điện (ES) phải được khống chế bằng những biện pháp khác nhau. "
                "Thiết kế của bộ theo dõi cặp nhiệt điện có thể quy định sẵn cách nối đất và che "
                "chắn được dùng.",
                "Figure 32.27 · Preferred grounding and shielding for several thermometry "
                "situations. Electromagnetic (EM) and electrostatic (ES) noise must be controlled "
                "by different means. The design of the thermocouple monitoring instrument may "
                "dictate the grounding and shielding scheme that can be used.",
                "Bảy sơ đồ con (a)–(g): thanh sọc chéo bên trái là vật thể thử, mỗi hàng nối qua "
                "cặp xoắn và khối đầu vào ba cực (+ − o) tới hai thanh ray + và − bên phải, tiếp "
                "đất Guard Power Gnd và Subject Gnd ở đáy",
                "Seven sub-figures (a)–(g): hatched bar at left is the test subject, each row runs "
                "through a twisted pair and a three-terminal input block (+ − o) to the + and − "
                "rails at right, grounded at Guard Power Gnd and Subject Gnd at the bottom")


# ---- 32.28  (balanced input recorder)
def _z(zx, zy, w, vert=False, n=6, amp=6, col=E, sw=1.3):
    """A zigzag resistor between (zx,zy) and (zx+w,zy) (or vertical)."""
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        if vert:
            y = zy + t * w
            x = zx + (amp if (i % 2 == 1) else -amp) * (1 if (i not in (0, n)) else 0)
        else:
            x = zx + t * w
            y = zy + (amp if (i % 2 == 1) else -amp) * (1 if (i not in (0, n)) else 0)
        pts.append((x, y))
    return _pl(pts, col, sw)


def fig_32_28():
    """Balanced input recorder circuit for improved common-mode noise rejection."""
    o = [_defs()]
    W, H = 680, 300
    # measuring junction Tm, with a dashed shield arc hugging it on the right
    o.append(_circ(60, 150, 3, E, E, 1.2))
    o.append(_circ(60, 150, 22, "none", S, 1.1, dash="4 3"))
    o.append(_mix(60, 104, [("T", "i"), ("m", "sub")], "middle", "ts", _fs(9)))
    o.append(_path("M 60,116 A 34,34 0 1 1 60,184", E, 1.2, "none", "2 3"))
    # emf sources + resistors on the two legs
    for yi, tag in ((132, "a"), (168, "b")):
        o.append(_line(84, yi, 110, yi, E, 1.4))
        o.append(_circ(136, yi, 14, "none", E, 1.2))
        o.append(_mix(136, yi - 20, [("E", "i"), (tag, "sub")], "middle", "ts", _fs(8)))
        o.append(_line(150, yi, 214, yi, E, 1.4))
        o.append(_z(214, yi, 42, False, 6, 6))
        o.append(_mix(235, yi - 16, [("R", ""), (tag, "sub")], "middle", "ts", _fs(9)))
        o.append(_line(256, yi, 320, yi, E, 1.4))
    # T_r reference box, with conductors carried through to the diamond nodes
    o.append(_rect(320, 110, 110, 80, "#fff", E, 1.4, rx=4))
    o.append(_mix(375, 102, [("T", "i"), ("r", "sub")], "middle", "ts", _fs(9)))
    for yd in (132, 168):
        o.append(_line(320, yd, 367, yd, E, 1.3))
        o.append(_poly([(372, yd - 5), (377, yd), (372, yd + 5), (367, yd)], "none", E, 1.2))
    # R_c balancing resistor on the lower reference path, in its own dashed zone
    o.append(_z(436, 168, 42, False, 6, 6))
    o.append(_mix(457, 148, [("R", ""), ("c", "sub")], "middle", "ts", _fs(9)))
    o.append(_rect(432, 152, 54, 28, "none", S, 1.1, dash="4 3", rx=6))
    # upper signal line steps up to the top of the upper R_s
    o.append(_pl([(430, 132), (470, 132), (470, 120), (514, 120)], E, 1.3))
    o.append(_line(478, 168, 514, 168, E, 1.3))
    # two matched R_s (vertical)
    o.append(_z(520, 120, 30, True, 6, 6))
    o.append(_z(520, 168, 30, True, 6, 6))
    o.append(_mix(496, 162, [("R", ""), ("s", "sub")], "end", "ts", _fs(9)))
    o.append(_rect(505, 108, 46, 100, "none", S, 1.1, dash="4 3", rx=6))
    # guard enclosure + instrument block; wires land on the terminals
    o.append(_rect(560, 70, 92, 162, "none", S, 1.1, dash="4 3", rx=8))
    o.append(_rect(576, 95, 38, 112, "#fff", E, 1.3, rx=4))
    for yy in (115, 150, 185):
        o.append(_circ(595, yy, 3, E, E, 1.1))
    o.append(_pl([(520, 120), (545, 120), (545, 115), (576, 115)], E, 1.3))
    o.append(_line(520, 150, 576, 150, E, 1.3))
    o.append(_pl([(520, 198), (545, 198), (545, 185), (576, 185)], E, 1.3))
    o.append(_lbl(622, 119, "+", "ts", "start", _fs(9)))
    o.append(_lbl(622, 189, "−", "ts", "start", _fs(9)))
    o.append(_mix(595, 84, [("T", "i"), ("i", "sub")], "middle", "ts", _fs(9)))
    o.append(_lbl(595, 226, "Guard", "ts", "middle", _fs(8)))
    return _fig(svg(W, H, "".join(o),
                    "Sơ đồ mạch đầu vào cân bằng để cải thiện khử nhiễu chế độ chung"),
                "Hình 32.28 · Sơ đồ mạch đầu vào cân bằng cho máy ghi nhằm cải thiện khử nhiễu "
                "chế độ chung. Điện trở cân bằng nhiệt kế R<sub>c</sub> = R<sub>a</sub> − "
                "R<sub>b</sub> và cặp điện trở đầu vào trở cao chuẩn khớp R<sub>s</sub> phải "
                "được giữ đẳng nhiệt.",
                "Figure 32.28 · A circuit arrangement for balanced input recorders to improve "
                "common-mode noise rejection. The thermometer balancing resistor, "
                "R<sub>c</sub> = R<sub>a</sub> − R<sub>b</sub>, and the matched pair of "
                "high-resistance input resistors R<sub>s</sub> must be held isothermal.",
                "Mạch đầu vào cân bằng: mối nối đo T_m trái, nguồn E_a/E_b và điện trở R_a/R_b "
                "trên hai nhánh vào hộp chuẩn T_r, điện trở cân bằng R_c và cặp R_s, khối dụng "
                "cụ ba cực +/−/Guard trong vùng che chắn bên phải",
                "Balanced input circuit: measuring junction T_m at left, emf sources E_a/E_b and "
                "resistors R_a/R_b on the two legs feeding the T_r reference box, balancing "
                "resistor R_c and the matched R_s pair, three-terminal +/−/Guard instrument "
                "block inside the guarded region at right")


# ---- 32.29  (the Seebeck emf cell)
def fig_32_29():
    """The Seebeck emf cell: a homogeneous nonisothermal segment of material M
    with end-points 1 and 2, modelled as a nonideal voltage source E_M(T) with
    internal resistance R(T), observed open-circuit."""
    o = [_defs()]
    W, H = 680, 232
    # physical segment of material M
    o.append(_rect(60, 100, 240, 30, FILL, E, 1.4))
    o.append(_lbl(180, 120, "M", "t", "middle", ' style="font-weight:700;font-size:12px"'))
    for x, n in ((60, "1"), (300, "2")):
        o.append(_circ(x, 115, 3, E, E, 1))
        o.append(_lbl(x, 90, n, "t", "middle"))
    o.append(_mix(56, 154, [("T", "i"), ("1", "sub")], "middle"))
    o.append(_mix(304, 154, [("T", "i"), ("2", "sub")], "middle"))
    o.append(_mix(180, 154, [("σ", "i"), ("M", "sub"), ("(", ""), ("T", "i"), (")", "")], "middle"))
    o.append(_lbl(180, 186, "đoạn vật liệu / segment", "ts", "middle", _fs(8)))
    # arrow between the two views
    o.append(_lbl(352, 121, "→", "t", "middle", _fs(15)))
    # equivalent circuit: terminal 1 - R(T) - source E_M(T) - terminal 2
    o.append(_circ(420, 115, 3.4, "#fff", E, 1.3))
    o.append(_lbl(420, 90, "1", "t", "middle"))
    o.append(_line(424, 115, 470, 115, E, 1.4))
    o.append(_z(470, 115, 44, False, 6, 6))
    o.append(_mix(492, 95, [("R", ""), ("(", ""), ("T", "i"), (")", "")], "middle"))
    o.append(_line(514, 115, 540, 115, E, 1.4))
    o.append(_circ(566, 115, 16, "#fff", E, 1.4))
    o.append(_mix(566, 87, [("E", "i"), ("M", "sub"), ("(", ""), ("T", "i"), (")", "")], "middle"))
    o.append(_line(582, 115, 636, 115, E, 1.4))
    o.append(_circ(640, 115, 3.4, "#fff", E, 1.3))
    o.append(_lbl(640, 90, "2", "t", "middle"))
    # open-circuit measurement path
    o.append(_path("M 420,105 A 112,58 0 0 1 640,105", S, 1.1, "none", "4 3"))
    o.append(_lbl(530, 44, "i = 0", "ts", "middle", _fs(9)))
    o.append(_lbl(530, 152, "hở mạch / open circuit", "ts", "middle", _fs(8)))
    o.append(_lbl(530, 186, "nguồn áp không lý tưởng / nonideal source", "ts", "middle", _fs(8)))
    return _fig(svg(W, H, "".join(o),
                    "Phần tử suất điện động Seebeck với nguồn áp không lý tưởng"),
                "Hình 32.29 · Phần tử suất điện động Seebeck. Mọi vật liệu dẫn điện, đẳng hướng "
                "nhiệt điện và không đẳng nhiệt đều là một nguồn suất điện động Seebeck. Phần tử "
                "cơ bản, một nguồn áp không lý tưởng có điện trở nội, góp một suất điện động "
                "Seebeck chỉ phụ thuộc vật liệu M và nhiệt độ tại hai điểm cuối 1 và 2 của đoạn.",
                "Figure 32.29 · The Seebeck emf cell. Every homogeneous, nonisothermal, "
                "electrically conducting material is a source of Seebeck emf. The basic cell, a "
                "nonideal voltage source with internal resistance, contributes a Seebeck emf that "
                "depends only on the material M and the temperatures at the segment end-points "
                "1 and 2.",
                "Bên trái là đoạn vật liệu M với hai điểm cuối 1 và 2 ở nhiệt độ T1 và T2, hệ số "
                "σ_M(T); bên phải là mạch tương đương: nguồn áp E_M(T) nối tiếp điện trở nội "
                "R(T), đo ở chế độ hở mạch i = 0",
                "Left: a segment of material M with end-points 1 and 2 at temperatures T1 and T2 "
                "and coefficient sigma_M(T); right: the equivalent circuit, source E_M(T) in "
                "series with internal resistance R(T), measured open-circuit at i = 0")


# ---- 32.30  (the T/X sketch)
def fig_32_30():
    """The T/X sketch for the Figure 32.26 circuit: real junctions b,c,d,e,f as
    closed circles joined by thermoelements C,A,B,D; dashed isotherms through c
    and e meeting the opposite legs at virtual junctions c' and e' (tics); the
    shaded zone between Tc and Te; dashed virtual thermoelements down to the
    designated reference temperature T0."""
    o = [_defs()]
    W, H = 680, 356
    ax, ay = 70, 282          # axis origin
    # axes
    o.append(_arr(ax, ay, 628, ay, E, sw=1.3))
    o.append(_arr(ax, ay, ax, 40, E, sw=1.3))
    o.append(_lbl(634, 286, "X", "t", "start", _fs(10)))
    o.append(_lbl(64, 42, "T", "t", "end", _fs(10)))
    yT0, yTi, yTc, yTe, yTm = 250, 215, 150, 120, 60
    # shaded zone between Tc and Te (behind everything else)
    o.append(_rect(220, yTe, 272, yTc - yTe, FILL, "none", 0))
    # thermoelements: b-c (C), c-d (A), d-e (B), e-f (D)
    o.append(_pl([(120, yTi), (220, yTc)], E, 1.5))
    o.append(_pl([(220, yTc), (340, yTm)], E, 1.5))
    o.append(_pl([(340, yTm), (460, yTe)], E, 1.5))
    o.append(_pl([(460, yTe), (560, yTi)], E, 1.5))
    # isotherms through c and e, meeting the opposite legs at c' and e'
    o.append(_line(74, yTc, 491, yTc, S, 1.0, "5 4"))
    o.append(_line(74, yTe, 260, yTe, S, 1.0, "5 4"))
    # virtual junction tics
    o.append(_line(487, yTc - 4, 495, yTc + 4, E, 1.6))
    o.append(_line(256, yTe - 4, 264, yTe + 4, E, 1.6))
    o.append(_lbl(500, yTc + 6, "c′", "t", "start", _fs(9)))
    o.append(_lbl(250, yTe - 8, "e′", "t", "end", _fs(9)))
    # virtual thermoelements down to the designated reference T0
    o.append(_line(74, yT0, 620, yT0, S, 1.0, "5 4"))
    o.append(_pl([(120, yTi), (120, yT0)], E, 1.3, "3 3"))
    o.append(_pl([(560, yTi), (560, yT0)], E, 1.3, "3 3"))
    o.append(_lbl(340, 268, "thân nhiệt điện ảo / virtual thermoelements", "ts", "middle", _fs(8)))
    # junction dots + letters
    for x, y in ((120, yTi), (220, yTc), (340, yTm), (460, yTe), (560, yTi)):
        o.append(_circ(x, y, 3.2, E, E, 1))
    o.append(_lbl(110, 208, "b", "t", "middle"))
    o.append(_lbl(212, 142, "c", "t", "middle"))
    o.append(_lbl(340, 48, "d", "t", "middle"))
    o.append(_lbl(468, 112, "e", "t", "middle"))
    o.append(_lbl(570, 208, "f", "t", "middle"))
    # segment labels
    B = ' style="font-weight:700"'
    o.append(_lbl(166, 174, "C", "t", "middle", B))
    o.append(_lbl(280, 98, "A", "t", "middle", B))
    o.append(_lbl(400, 98, "B", "t", "middle", B))
    o.append(_lbl(516, 152, "D", "t", "middle", B))
    # temperature labels on the axis and at the junctions
    o.append(_mix(60, yTm + 4, [("T", "i"), ("m", "sub")], "end"))
    o.append(_mix(60, yTc + 4, [("T", "i"), ("c", "sub")], "end"))
    o.append(_mix(60, yTe + 4, [("T", "i"), ("e", "sub")], "end"))
    o.append(_mix(60, yTi + 4, [("T", "i"), ("i", "sub")], "end"))
    o.append(_mix(60, yT0 + 4, [("T", "i"), ("0", "sub")], "end"))
    o.append(_mix(104, 236, [("T", "i"), ("b", "sub")], "end", "ts", _fs(8)))
    o.append(_mix(576, 236, [("T", "i"), ("f", "sub")], "start", "ts", _fs(8)))
    o.append(_lbl(620, 300, "không theo tỉ lệ / not to scale", "ts", "end", _fs(8)))
    o.append(_lbl(618, 274, "X (vị trí quanh mạch)", "ts", "end", _fs(8)))
    return _fig(svg(W, H, "".join(o),
                    "Bản phác T/X để trực quan hóa mạch nhiệt điện"),
                "Hình 32.30 · Bản phác T/X để trực quan hóa mạch nhiệt điện. Nhiệt độ của mối nối "
                "chuẩn và quan hệ giữa (không nhất thiết là giá trị cụ thể của) nhiệt độ của mọi "
                "mối nối thực phụ trong mạch phải được biết để đo chính xác — cũng như khi dùng "
                "bản phác T/X. Bản phác đơn giản này giúp nhận ra những mối nối phụ phải được "
                "khống chế cùng một nhiệt độ, và cho thấy rõ những thân nhiệt điện nào được ghép "
                "nhiệt theo cặp, dù không được nối trực tiếp trong mạch nối tiếp.",
                "Figure 32.30 · The T/X sketch for thermoelectric circuit visualization. The "
                "temperature of the reference junction(s) and the relation between (not "
                "necessarily the specific values of) the temperatures of all incidental real "
                "junctions in a circuit must be known for accurate thermometry, just as for the "
                "use of the T/X sketch. The simple sketch is an aid in recognizing temperatures "
                "of incidental junctions that must be controlled to the same temperature. It "
                "also makes clear which thermoelements are thermally paired, even if not "
                "directly joined in the series circuit.",
                "Bản phác nhiệt độ theo vị trí: trục T thẳng đứng, trục X ngang; năm mối nối "
                "thực b c d e f đánh dấu bằng chấm đặc, nối bởi các thân nhiệt điện C A B D; "
                "đường đẳng nhiệt nét đứt qua c và e cắt chân đối diện tại mối nối ảo c′ và e′ "
                "đánh dấu bằng vạch; vùng gạch bóng giữa Tc và Te; hai thân nhiệt điện ảo nét "
                "đứt kéo xuống đường đẳng nhiệt T0",
                "Temperature-versus-position sketch: vertical T axis, horizontal X axis; five "
                "real junctions b c d e f marked by filled dots joined by thermoelements C A B D; "
                "dashed isotherms through c and e meeting the opposite legs at virtual junctions "
                "c′ and e′ marked by tics; shaded zone between Tc and Te; two dashed virtual "
                "thermoelements dropping to the T0 isotherm")


FIGS = [fig_32_1, fig_32_2, fig_32_3, fig_32_4, fig_32_5, fig_32_6,
        fig_32_7, fig_32_8, fig_32_9, fig_32_10, fig_32_11, fig_32_12,
        fig_32_13, fig_32_14, fig_32_15, fig_32_16, fig_32_17, fig_32_18,
        fig_32_19, fig_32_20, fig_32_21, fig_32_22,         fig_32_24,
        fig_32_25, fig_32_26, fig_32_27, fig_32_28, fig_32_29, fig_32_30]

# The book has no figure 32.23: the numbering runs 32.22 -> 32.24 and nothing in
# the PDF ever mentions a 32.23.  FIGS is positional, so the printed number of
# each slot lives here; fig() refuses a number that is not in the list rather
# than quietly handing back the figure next door.
FIG_NO = list(range(1, 23)) + [24, 25, 26, 27, 28, 29, 30]


def fig(n):
    if n not in FIG_NO:
        raise KeyError("no figure 32.%d in this chapter" % n)
    return FIGS[FIG_NO.index(n)]()
