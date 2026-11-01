# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 28 — Flow Measurement (Richard Thorn et al.).

The source chapter is by far the largest in the handbook: 132 pages, eleven
sections, 92 figures (28.1–28.92) and 23 tables. FIGS is built up section by
section; the module is written so that figures can be appended in batches
without touching the ones already done.

Geometry, labels and curve shapes are read off the rendered pages in
work/ch28img. Where the original is a product photograph (meter bodies,
rotors, probes) it is redrawn here as a line illustration of the same object,
which is the convention used throughout this handbook.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig, Box

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"
BLUE = "#1f4e79"
DARK = "#3a3a3a"


# ---------------------------------------------------------------- primitives

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
            '<marker id="ah28" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah28g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah28s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah28b" markerWidth="9" markerHeight="9" refX="2" refY="3" '
            'orient="auto"><path d="M7,0 L0,3 L7,6 z" fill="%s"/></marker>'
            '<marker id="ah28w" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="#ffffff"/></marker>'
            '<pattern id="hatch28" width="5" height="5" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" '
            'stroke="#9aa4b2" stroke-width="1.1"/></pattern>'
            '<pattern id="hatch28b" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="6" '
            'stroke="#b8c0cb" stroke-width="1"/></pattern>'
            '</defs>' % (E, G, S, E))


def _arr(x1, y1, x2, y2, col=E, marker="ah28", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah28b)" marker-end="url(#ah28)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _line(x1, y1, x2, y2, col=E, sw=1.4, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _rect(x, y, w, h, fill="none", col=E, sw=1.3, dash=None, rx=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    r = ' rx="%s"' % _f(rx) if rx else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, sw, d, r))


def _path(d, col=E, sw=1.4, fill="none", dash=None, cap="round"):
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" '
            'stroke-linejoin="round" stroke-linecap="%s"%s/>' % (d, fill, col, sw, cap, ds))


def _poly(pts, fill="none", col=E, sw=1.3, dash=None):
    d = "M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in pts) + " Z"
    return _path(d, col, sw, fill, dash)


def _circ(cx, cy, r, fill="none", col=E, sw=1.3):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy), _f(r), fill, col, sw))


def _ell(cx, cy, rx, ry, fill="none", col=E, sw=1.3):
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (_f(cx), _f(cy), _f(rx), _f(ry), fill, col, sw))


# ---------------------------------------------------- flow-specific primitives

def _pipe(x1, x2, yc, r, wall=1.6, ends=True):
    """A horizontal pipe seen from the side: two walls plus optional end ellipses."""
    o = [_line(x1, yc - r, x2, yc - r, E, wall),
         _line(x1, yc + r, x2, yc + r, E, wall)]
    if ends:
        o.append(_ell(x1, yc, 7, r, P, E, wall))
        o.append(_ell(x2, yc, 7, r, P, E, wall))
    return "".join(o)


def _tap(x, ytop, ywall, r=7):
    """A pressure tapping: a short stub with a small circle on top."""
    return (_line(x, ywall, x, ytop + r, E, 1.4) + _circ(x, ytop, r, P, E, 1.4))


def _profile(x0, yc, r, L, kind="lam", n=40):
    """Velocity profile: x as a function of y inside the pipe."""
    pts = []
    for i in range(n + 1):
        t = -1.0 + 2.0 * i / n
        if kind == "lam":
            f = 1 - t * t
        elif kind == "turb":
            f = (1 - t * t) ** (1.0 / 7.0)
        else:
            f = 1 - t * t
        pts.append((x0 + L * f, yc + r * t))
    return pts


def _flowarrow(x, y, w=46, col=E, sw=1.5):
    return _arr(x, y, x + w, y, col, "ah28", sw)


# ================================================================ 28.1

def fig_28_1():
    o = [_defs()]
    # ---- laminar panel
    x0, yc, r = 66, 150, 48
    o.append(_pipe(x0 - 10, 300, yc, r))
    o.append(_lbl(183, 62, "Chảy tầng", "tb", "middle"))
    o.append(_lbl(183, 76, "Laminar flow", "ts", "middle"))
    for i in range(6):
        t = -0.86 + 1.72 * i / 5
        f = 1 - t * t
        y = yc + r * t
        o.append(_flowarrow(x0, y, 8 + 96 * f, S, 1.1))
    o.append(_path("M" + " L".join("%s,%s" % (_f(a), _f(b))
                                   for a, b in _profile(x0, yc, r, 104, "lam")), E, 1.8))
    # v_avg / v_max markers, staggered so the two captions cannot collide
    o.append(_line(x0 + 52, yc - r, x0 + 52, yc + r + 6, S, 1.0, "3 3"))
    o.append(_line(x0 + 104, yc - r, x0 + 104, yc + r + 6, S, 1.0, "3 3"))
    o.append(_subs(x0 + 52, yc + r + 34, [("v", False), ("avg", True)], "middle", "ts"))
    o.append(_subs(x0 + 104, yc + r + 50,
                   [("v", False), ("max", True), (" = 2v", False), ("avg", True)],
                   "middle", "ts"))
    # ---- turbulent panel
    x0b, ycb = 396, 150
    o.append(_pipe(x0b - 10, 630, ycb, r))
    o.append(_lbl(513, 62, "Chảy rối", "tb", "middle"))
    o.append(_lbl(513, 76, "Turbulent flow", "ts", "middle"))
    # wavy streamlines, kept to the upstream half of the pipe
    for k in range(5):
        yy = ycb - 30 + 15 * k
        d = "M%s,%s" % (_f(x0b + 8), _f(yy))
        for j in range(1, 7):
            d += " Q%s,%s %s,%s" % (_f(x0b + 8 + j * 16 - 8), _f(yy + (6 if j % 2 else -6)),
                                    _f(x0b + 8 + j * 16), _f(yy))
        o.append(_path(d, S, 1.1))
    for i in range(6):
        t = -0.86 + 1.72 * i / 5
        f = (1 - t * t) ** (1.0 / 7.0)
        o.append(_flowarrow(x0b, ycb + r * t, 6 + 98 * f, E, 1.2))
    o.append(_path("M" + " L".join("%s,%s" % (_f(a), _f(b))
                                   for a, b in _profile(x0b, ycb, r, 104, "turb")), E, 1.8))
    o.append(_line(x0b + 86, ycb - r, x0b + 86, ycb + r + 6, S, 1.0, "3 3"))
    o.append(_line(x0b + 104, ycb - r, x0b + 104, ycb + r + 6, S, 1.0, "3 3"))
    o.append(_subs(x0b + 78, ycb + r + 34, [("v", False), ("avg", True)], "middle", "ts"))
    o.append(_subs(x0b + 128, ycb + r + 50,
                   [("v", False), ("max", True), (" ≈ 1,2v", False), ("avg", True)],
                   "middle", "ts"))
    return _fig(svg(680, 300, "".join(o), "Phân bố vận tốc trong chảy tầng và chảy rối"),
                "Hình 28.1 · Phân bố vận tốc trong chảy tầng và chảy rối. Chảy tầng cho mặt "
                "parabol với vận tốc đỉnh gấp đôi vận tốc trung bình; chảy rối cho mặt phẳng "
                "hơn, đỉnh chỉ khoảng 1,2 lần.",
                "Figure 28.1 · Velocity profiles in laminar and turbulent flow. Laminar flow "
                "gives a parabola with a peak twice the mean; turbulent flow gives a flatter "
                "profile, peaking at about 1.2 times the mean.",
                "Hai mặt cắt ống cạnh nhau: mặt parabol của chảy tầng và mặt phẳng hơn của chảy rối",
                "Two pipe sections side by side: the parabolic laminar profile and the flatter turbulent one")


def fig_28_2():
    o = [_defs()]
    # pipe drawn in oblique view: left end low and wide, right end high and narrow
    lx, ly, lrx, lry = 120, 226, 26, 50
    rx, ry, rrx, rry = 556, 118, 19, 36
    o.append(_ell(lx, ly, lrx, lry, WARM, E, 1.6))
    o.append(_ell(rx, ry, rrx, rry, WARM, E, 1.6))
    o.append(_line(lx, ly - lry, rx, ry - rry, E, 1.6))
    o.append(_line(lx, ly + lry, rx, ry + rry, E, 1.6))
    # the tapering is in the section, so add a faint mid line
    o.append(_line(lx, ly, rx, ry, "#d6dde6", 1.0, "4 4"))
    o.append(_lbl(200, 130, "chất lưu, khối lượng riêng ρ", "t"))
    o.append(_lbl(200, 144, "fluid density ρ", "ts"))
    o.append(_flowarrow(168, 196, 54))
    o.append(_subs(176, 186, [("v", False), ("1", True)], "start", "tb"))
    o.append(_flowarrow(404, 152, 56))
    o.append(_subs(412, 142, [("v", False), ("2", True)], "start", "tb"))
    # height references
    o.append(_line(60, 330, 590, 330, E, 1.2))
    for xx, ytop, lab in ((172, ly + lry, "h₁"), (452, 138, "h₂")):
        o.append(_line(xx, ytop, xx, 330, S, 1.0, "3 3"))
        o.append(_arr(xx, 330, xx, ytop + 2, S, "ah28s", 1.0))
        o.append(_lbl(xx - 8, (ytop + 330) / 2, lab, "tb", "end"))
    return _fig(svg(680, 350, "".join(o), "Dòng chảy trong ống thuôn nghiêng"),
                "Hình 28.2 · Dòng chảy qua một ống thuôn, đặt nghiêng. Đầu vào lớn, đầu ra nhỏ nên "
                "vận tốc tăng từ v₁ lên v₂; h₁ và h₂ là độ cao so với một mốc cố định.",
                "Figure 28.2 · Flow through an inclined, tapered pipe. The inlet is large and the "
                "outlet small, so the velocity rises from v₁ to v₂; h₁ and h₂ are heights above a "
                "fixed datum.",
                "Ống thuôn đặt nghiêng với hai mặt cắt elip, mũi tên vận tốc và hai độ cao h",
                "A tapered inclined pipe with two elliptical sections, velocity arrows and two heights")


def fig_28_3():
    o = [_defs()]
    # pipe with a step reduction: wide on the left, narrow on the right
    yc = 196
    o.append(_line(60, yc - 56, 300, yc - 56, E, 1.7))
    o.append(_line(300, yc - 56, 300, yc - 26, E, 1.7))
    o.append(_line(300, yc - 26, 610, yc - 26, E, 1.7))
    o.append(_line(60, yc + 56, 300, yc + 56, E, 1.7))
    o.append(_line(300, yc + 56, 300, yc + 26, E, 1.7))
    o.append(_line(300, yc + 26, 610, yc + 26, E, 1.7))
    o.append(_ell(60, yc, 8, 56, P, E, 1.7))
    o.append(_ell(610, yc, 8, 26, P, E, 1.7))
    # pressure capsules
    o.append(_tap(190, 96, yc - 56, 22))
    o.append(_subs(190, 101, [("p", False), ("1", True)], "middle", "tb"))
    o.append(_tap(452, 112, yc - 26, 22))
    o.append(_subs(452, 117, [("p", False), ("2", True)], "middle", "tb"))
    # velocities
    o.append(_flowarrow(126, yc, 52))
    o.append(_subs(132, yc - 10, [("v", False), ("1", True)], "start", "tb"))
    o.append(_flowarrow(390, yc, 52))
    o.append(_subs(396, yc - 10, [("v", False), ("2", True)], "start", "tb"))
    # area annotations, below the pipe, arrows up to the two end faces
    o.append(_lbl(66, 300, "diện tích mặt cắt ống A₁", "t"))
    o.append(_lbl(66, 314, "cross-sectional area of pipe A₁", "ts"))
    o.append(_arr(96, 292, 66, 258, S, "ah28s", 1.1))
    o.append(_lbl(614, 300, "diện tích mặt cắt ống A₂", "t", "end"))
    o.append(_lbl(614, 314, "cross-sectional area of pipe A₂", "ts", "end"))
    o.append(_arr(586, 292, 612, 228, S, "ah28s", 1.1))
    o.append(_lbl(214, 176, "khối lượng riêng ρ", "t"))
    return _fig(svg(680, 330, "".join(o), "Dùng một chỗ thắt trong ống để đo lưu lượng"),
                "Hình 28.3 · Dùng một chỗ thắt trong ống để đo lưu lượng. Ống thu từ tiết diện A₁ "
                "xuống A₂ nên vận tốc tăng từ v₁ lên v₂ và áp suất giảm từ p₁ xuống p₂; chênh áp "
                "đo được chính là thước đo lưu lượng.",
                "Figure 28.3 · Using a restriction in a pipe to measure fluid flow rate. The bore "
                "narrows from A₁ to A₂, so velocity rises from v₁ to v₂ and pressure falls from p₁ "
                "to p₂; the measured drop is the measure of flow rate.",
                "Ống có một bậc thu tiết diện, hai đầu dò áp suất p1 và p2, mũi tên vận tốc",
                "A pipe with a step restriction, two pressure tappings p1 and p2, velocity arrows")


def fig_28_4():
    o = [_defs()]
    # ---- plate face, top left
    px, py = 250, 82
    o.append(_ell(px, py, 46, 58, P, E, 1.7))
    o.append(_ell(px, py, 21, 26, "#f2f4f7", E, 1.5))
    o.append(_rect(px - 9, py - 74, 18, 18, P, E, 1.5, rx=2))
    o.append(_lbl(px + 56, py - 66, "Tấm orifice", "tb"))
    o.append(_lbl(px + 56, py - 52, "Orifice Plate", "ts"))
    # leaders from the plate down to the two section views
    o.append(_line(px + 40, py + 44, 344, 232, S, 1.0))
    o.append(_line(px + 34, py + 50, 344, 336, S, 1.0))
    # ---- upper section view
    yc1 = 262
    o.append(_pipe(90, 620, yc1, 26, 1.7, ends=False))
    o.append(_rect(338, yc1 - 34, 9, 68, "#ffffff", E, 1.6))
    o.append(_tap(310, 214, yc1 - 26, 6))
    o.append(_tap(372, 214, yc1 - 26, 6))
    # ---- lower section view with the vena contracta
    yc2 = 366
    o.append(_pipe(90, 620, yc2, 26, 1.7, ends=False))
    o.append(_rect(338, yc2 - 34, 9, 68, "#ffffff", E, 1.6))
    o.append(_path("M%s,%s C%s,%s %s,%s %s,%s" % (
        _f(347), _f(yc2 - 9), _f(368), _f(yc2 - 9), _f(386), _f(yc2 - 14),
        _f(410), _f(yc2 - 18)), E, 1.3, "none", "4 3"))
    o.append(_path("M%s,%s C%s,%s %s,%s %s,%s" % (
        _f(347), _f(yc2 + 9), _f(368), _f(yc2 + 9), _f(386), _f(yc2 + 14),
        _f(410), _f(yc2 + 18)), E, 1.3, "none", "4 3"))
    # ---- annotations
    o.append(_lbl(44, 196, "Chiều dòng chảy", "t"))
    o.append(_lbl(44, 210, "Flow Direction", "ts"))
    o.append(_flowarrow(44, 220, 52))
    o.append(_lbl(430, 168, "Điểm lấy áp", "tb"))
    o.append(_lbl(430, 182, "(chênh áp qua lưu lượng kế đo tại đây)", "ts"))
    o.append(_lbl(430, 196, "Pressure tappings", "ts"))
    o.append(_arr(486, 200, 372, 208, S, "ah28s", 1.0))
    o.append(_arr(470, 200, 310, 208, S, "ah28s", 1.0))
    o.append(_lbl(596, 352, "vena contracta", "ts", "end"))
    return _fig(svg(680, 410, "".join(o), "Lưu lượng kế tấm orifice cạnh vát vuông"),
                "Hình 28.4 · Lưu lượng kế tấm orifice cạnh vuông. Tấm khoan lỗ đặt kẹp giữa hai "
                "mặt bích; dòng sau khi qua lỗ còn co tiếp tới mặt cắt nhỏ nhất gọi là vena "
                "contracta, rồi mới bung ra chạm thành ống.",
                "Figure 28.4 · A square-edged orifice plate flowmeter. The drilled plate is clamped "
                "between flanges; downstream of the hole the jet keeps contracting to a minimum "
                "section, the vena contracta, before spreading to the pipe wall.",
                "Tấm orifice nhìn chính diện, hai mặt cắt ống có tấm chắn và điểm lấy áp",
                "The orifice plate face-on, and two pipe sections showing the plate and tappings")


def fig_28_5():
    o = [_defs()]
    yc = 150
    # profile radii along the Venturi: inlet, converging, throat, diverging, outlet
    seg = [(70, 60, 54), (200, 60, 54), (330, 60, 28), (430, 60, 28), (560, 60, 46), (620, 60, 46)]
    top = [(70, yc - 54), (200, yc - 54)]
    # build a smooth upper wall
    d = ("M70,%s L200,%s Q%s,%s %s,%s L430,%s Q%s,%s %s,%s L620,%s"
         % (_f(yc - 54), _f(yc - 54), _f(268), _f(yc - 54), _f(330), _f(yc - 28),
            _f(yc - 28), _f(496), _f(yc - 28), _f(560), _f(yc - 46), _f(yc - 46)))
    o.append(_path(d, E, 1.7))
    d2 = ("M70,%s L200,%s Q%s,%s %s,%s L430,%s Q%s,%s %s,%s L620,%s"
          % (_f(yc + 54), _f(yc + 54), _f(268), _f(yc + 54), _f(330), _f(yc + 28),
             _f(yc + 28), _f(496), _f(yc + 28), _f(560), _f(yc + 46), _f(yc + 46)))
    o.append(_path(d2, E, 1.7))
    o.append(_ell(70, yc, 9, 54, P, E, 1.7))
    o.append(_ell(620, yc, 9, 46, P, E, 1.7))
    # section rings
    for xx, rr in ((200, 54), (330, 28), (430, 28), (560, 46)):
        o.append(_ell(xx, yc, 5, rr, "none", "#9aa4b2", 1.0))
    # tappings
    o.append(_tap(300, yc + 54 + 34, yc + 54, 6))
    o.append(_tap(470, yc + 28 + 46, yc + 28, 6))
    o.append(_line(300, yc + 94, 372, yc + 104, S, 1.0))
    o.append(_line(470, yc + 80, 452, yc + 104, S, 1.0))
    o.append(_lbl(378, yc + 108, "Điểm lấy áp", "ts"))
    o.append(_lbl(378, yc + 121, "Pressure tappings", "ts"))
    o.append(_lbl(96, yc - 74, "Chiều dòng chảy", "ts"))
    o.append(_flowarrow(48, yc - 40, 54))
    o.append(_lbl(330, yc - 44, "họng", "ts", "middle"))
    return _fig(svg(680, 310, "".join(o), "Lưu lượng kế ống Venturi"),
                "Hình 28.5 · Lưu lượng kế ống Venturi. Ống thu dần, một đoạn họng trụ rồi loe dần; "
                "độ thu hẹp diễn ra từ từ nên hệ số lưu lượng C gần 1 và tổn thất áp suất vĩnh "
                "viễn nhỏ hơn nhiều so với tấm orifice.",
                "Figure 28.5 · A Venturi tube flowmeter. A converging inlet, a cylindrical throat "
                "and a diverging outlet; because the contraction is gradual the discharge "
                "coefficient is close to unity and the permanent pressure loss is much lower "
                "than an orifice plate.",
                "Mặt cắt ống Venturi với đoạn thu, họng và đoạn loe, kèm hai điểm lấy áp",
                "Venturi tube section with converging inlet, throat and diverging outlet, plus two tappings")


def fig_28_6():
    o = [_defs()]
    yc1, yc2 = 250, 348
    # ---- upper view: pipe with the nozzle and both tappings
    o.append(_pipe(90, 620, yc1, 26, 1.7, ends=False))
    # nozzle body drawn in solid black section, like the original
    nd = ("M330,%s q0,-22 18,-26 L376,%s L376,%s L348,%s q-18,-4 -18,-26 Z"
          % (_f(yc1 - 26), _f(yc1 - 9), _f(yc1 + 9), _f(yc1 + 26)))
    o.append(_path(nd, DARK, 1.0, DARK))
    o.append(_rect(376, yc1 - 9, 26, 18, DARK, DARK, 1.0))
    o.append(_tap(310, 206, yc1 - 26, 6))
    o.append(_tap(408, 206, yc1 - 26, 6))
    # ---- lower view: same nozzle, no tappings
    o.append(_pipe(90, 620, yc2, 26, 1.7, ends=False))
    nd2 = ("M330,%s q0,-22 18,-26 L376,%s L376,%s L348,%s q-18,-4 -18,-26 Z"
           % (_f(yc2 - 26), _f(yc2 - 9), _f(yc2 + 9), _f(yc2 + 26)))
    o.append(_path(nd2, DARK, 1.0, DARK))
    o.append(_rect(376, yc2 - 9, 26, 18, DARK, DARK, 1.0))
    # ---- annotations
    o.append(_lbl(392, 156, "Điểm lấy áp", "tb"))
    o.append(_lbl(392, 170, "(chênh áp qua lưu lượng kế đo tại đây)", "ts"))
    o.append(_lbl(392, 184, "Pressure tappings", "ts"))
    o.append(_arr(430, 188, 408, 200, S, "ah28s", 1.0))
    o.append(_arr(452, 188, 310, 200, S, "ah28s", 1.0))
    o.append(_lbl(556, 214, "Vòi phun", "tb", "end"))
    o.append(_lbl(556, 228, "Nozzle", "ts", "end"))
    o.append(_line(548, 232, 400, 246, S, 1.0))
    o.append(_line(548, 306, 400, 348, S, 1.0))
    o.append(_lbl(44, 190, "Chiều dòng chảy", "t"))
    o.append(_lbl(44, 204, "Flow direction", "ts"))
    o.append(_flowarrow(44, 214, 52))
    return _fig(svg(680, 396, "".join(o), "Lưu lượng kế vòi phun"),
                "Hình 28.6 · Lưu lượng kế vòi phun. Miệng vào cong nên vòi phun vừa gọn vừa có hệ "
                "số lưu lượng gần 1; không có cạnh sắc để mòn nên dùng tốt với chất lưu bẩn và "
                "mài mòn, và với hơi quá nhiệt ở vận tốc cao.",
                "Figure 28.6 · A nozzle flowmeter. The curved inlet makes the nozzle both compact "
                "and close to unity discharge coefficient; with no sharp edge to erode it suits "
                "dirty and abrasive fluids, and high-velocity superheated steam.",
                "Hai mặt cắt ống có vòi phun tô đen, điểm lấy áp phía trên",
                "Two pipe sections with the nozzle in solid black and tappings above")


FIGS = [fig_28_1(), fig_28_2(), fig_28_3(), fig_28_4(), fig_28_5(), fig_28_6()]


def fig(n):
    return FIGS[n - 1]
