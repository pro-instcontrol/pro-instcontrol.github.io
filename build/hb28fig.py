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


# ================================================================ 28.2

def fig_28_7():
    o = [_defs()]
    # tapered vertical tube, wider at the top
    o.append(_line(250, 320, 272, 66, E, 1.8))
    o.append(_line(404, 320, 428, 66, E, 1.8))
    o.append(_line(272, 66, 428, 66, E, 1.8))
    o.append(_line(250, 320, 404, 320, E, 1.8))
    # flanges
    o.append(_rect(232, 40, 236, 16, "#e8ecf2", E, 1.4, rx=2))
    o.append(_rect(226, 320, 248, 16, "#e8ecf2", E, 1.4, rx=2))
    # scale ticks along the left wall
    for i in range(13):
        y = 96 + i * 17
        t = 0.55 + i * 0.035
        x = 250 + (y - 320) * (272 - 250) / (66 - 320)
        o.append(_line(x + 6, y, x + 6 + 9 * t, y, S, 1.0))
    # bob
    o.append(_path("M325,196 L341,196 L341,214 L333,226 L325,214 Z", E, 1.5, "#cfd8e6"))
    o.append(_line(333, 196, 333, 214, E, 1.0))
    # flow arrows
    for x in (300, 333, 366):
        o.append(_arr(x, 296, x, 246, S, "ah28s", 1.2))
    o.append(_lbl(446, 120, "Ống thuỷ tinh hình côn", "t"))
    o.append(_lbl(446, 134, "conical glass tube", "ts"))
    o.append(_arr(440, 128, 424, 118, S, "ah28s", 1.0))
    o.append(_lbl(446, 210, "Phao (bob)", "t"))
    o.append(_lbl(446, 224, "float", "ts"))
    o.append(_arr(440, 214, 346, 212, S, "ah28s", 1.0))
    o.append(_lbl(446, 300, "Thang chia trên ống", "t"))
    o.append(_lbl(446, 314, "scale engraved on the tube", "ts"))
    o.append(_arr(440, 300, 286, 250, S, "ah28s", 1.0))
    o.append(_lbl(120, 200, "Dòng đi lên", "ts", "middle"))
    o.append(_arr(120, 292, 120, 240, S, "ah28s", 1.3))
    return _fig(svg(680, 366, "".join(o), "Mặt cắt ống đo lưu lượng kiểu rotameter"),
                "Hình 28.7 · Mặt cắt một rotameter. Mức phao dâng tuyến tính theo lưu lượng tăng. "
                "Ống hình côn nên tiết diện vành khuyên quanh phao tăng dần theo chiều cao — đó "
                "chính là “diện tích biến thiên”.",
                "Figure 28.7 · Cross-section of a rotameter. The level of the bob rises linearly with "
                "increasing flow rate. The conical tube makes the annular area around the bob grow "
                "with height — this is the “variable area”.",
                "Mặt cắt dọc ống côn thuỷ tinh có phao và thang chia, mũi tên dòng đi lên",
                "Section through a conical glass tube with a bob and scale, flow arrow upward")


def fig_28_8():
    o = [_defs()]
    yc = 130
    # reading line
    o.append(_line(66, yc, 640, yc, E, 1.0, "6 4"))
    o.append('<path d="M66,%s l12,-4 l0,8 z" fill="%s"/>' % (_f(yc), E))
    o.append(_lbl(72, yc - 7, "Reading line", "ts", "start"))
    o.append(_lbl(300, 56, "guided", "ts", "middle"))
    # six bob shapes
    shapes = [
        ("M150,96 L150,140 L166,166 L182,140 L182,96 Z", "trụ + mũi côn"),
        ("M228,96 L228,140 L244,166 L260,140 L260,96 Z", "có thanh dẫn"),
        ("circle", "cầu"),
        ("M368,96 L368,150 L384,150 L384,96 Z", "trụ có rãnh"),
        ("M446,96 L446,150 L462,150 L462,96 Z", "trụ có rãnh"),
        ("M524,96 L524,136 L540,162 L556,136 L556,96 Z", "côn"),
    ]
    xs = [166, 244, 316, 376, 454, 540]
    for (d, name), cx in zip(shapes, xs):
        if d == "circle":
            o.append(_circ(cx, 120, 26, "#eef2f7", E, 1.6))
        else:
            o.append(_path(d, E, 1.6, "#eef2f7"))
    # guide rod on the second bob
    o.append(_line(244, 62, 244, 166, E, 1.3))
    # slots on the ribbed bobs
    for cx in (376, 454):
        for i in range(3):
            o.append(_line(cx + 4, 108 + i * 14, cx + 12, 112 + i * 14, S, 1.2))
    for cx, name in zip(xs, [s[1] for s in shapes]):
        o.append(_lbl(cx, 196, name, "ts", "middle"))
    return _fig(svg(680, 230, "".join(o), "Các dạng phao rotameter thường gặp"),
                "Hình 28.8 · Các dạng phao rotameter thường gặp. Hình dạng phao quyết định mức độ "
                "phụ thuộc độ nhớt; phao cầu dùng trong ống nhỏ, phao có rãnh nghiêng làm phao tự "
                "quay chậm để giữ vị trí ổn định.",
                "Figure 28.8 · Typical rotameter bob geometries. The shape sets how strongly the "
                "reading depends on viscosity; spherical bobs suit small tubes, and inclined grooves "
                "make the bob spin slowly to hold a stable position.",
                "Sáu dạng phao khác nhau đặt trên một đường đọc chung",
                "Six bob shapes arranged along a common reading line")


def fig_28_9():
    o = [_defs()]
    # duct
    o.append(_line(60, 250, 600, 250, E, 1.7))
    o.append(_line(60, 300, 600, 300, E, 1.7))
    # hinge and flap
    o.append(_circ(330, 232, 5, E, E, 1.2))
    o.append(_path("M330,232 L392,282 L404,268 L342,218 Z", E, 1.6, "#cfd8e6"))
    # magnet block above the duct
    o.append(_rect(316, 150, 30, 56, "#eef2f7", E, 1.5, rx=3))
    o.append(_lbl(331, 172, "N", "tb", "middle"))
    o.append(_lbl(331, 198, "S", "tb", "middle"))
    o.append(_line(331, 206, 331, 228, E, 1.4))
    # indicator
    o.append(_rect(232, 150, 66, 46, P, E, 1.5, rx=3))
    o.append(_path("M240,188 A24,24 0 0 1 288,188", E, 1.2))
    o.append(_line(264, 188, 276, 166, E, 1.6))
    o.append(_lbl(265, 148, "chỉ thị", "ts", "middle"))
    o.append(_line(298, 172, 316, 172, S, 1.2))
    # spring
    d = "M392,268"
    for i in range(5):
        d += " l8,-9 l8,9"
    o.append(_path(d, E, 1.2))
    o.append(_line(472, 264, 472, 300, E, 1.2))
    # flow arrow
    o.append(_arr(470, 275, 540, 275, S, "ah28s", 1.3))
    o.append(_lbl(504, 292, "dòng", "ts", "middle"))
    o.append(_lbl(331, 132, "nam châm vĩnh cửu truyền vị trí lá chắn", "ts", "middle"))
    return _fig(svg(680, 330, "".join(o), "Lưu lượng kế lá chắn di động"),
                "Hình 28.9 · Lưu lượng kế lá chắn di động. Nam châm (N, S) truyền vị trí lá chắn tới "
                "bộ chỉ thị. Lá chắn mở cho tới khi lực động học của dòng cân bằng với lực hồi phục "
                "của lò xo hoặc đối trọng.",
                "Figure 28.9 · Movable vane meter. The magnet (N, S) transmits the vane position to an "
                "indicator. The vane opens until the dynamic force of the flow balances the restoring "
                "force of a spring or weight.",
                "Lá chắn bản lề trong ống, nam châm và bộ chỉ thị kim",
                "A hinged vane in a duct, a magnet and a pointer indicator")


def fig_28_10():
    o = [_defs()]
    o.append(_rect(180, 70, 320, 190, P, E, 1.8, rx=4))
    o.append(_rect(192, 82, 296, 166, "#f6f8fa", "#b8c0cb", 1.0, rx=2))
    # flap seen through the window
    o.append(_circ(300, 96, 5, E, E, 1.2))
    o.append(_path("M300,96 L372,158 L384,146 L312,84 Z", E, 1.6, "#cfd8e6"))
    # scale arc
    o.append(_path("M300,96 m-70,0 a70,70 0 0 1 40,-62", S, 1.0, "none", "4 3"))
    for a in range(0, 5):
        ang = _m.radians(-18 - a * 11)
        o.append(_line(300 + 70 * _m.cos(ang), 96 + 70 * _m.sin(ang),
                       300 + 60 * _m.cos(ang), 96 + 60 * _m.sin(ang), S, 1.1))
    o.append(_lbl(300, 236, "cửa sổ thuỷ tinh / nhựa", "ts", "middle"))
    o.append(_lbl(300, 282, "Góc của lá chắn là thước đo lưu lượng", "t", "middle"))
    o.append(_lbl(300, 298, "The angle of the vane provides a measure of the flow rate", "ts", "middle"))
    o.append(_lbl(540, 160, "thang chia", "ts"))
    return _fig(svg(680, 320, "".join(o), "Bộ chỉ thị lưu lượng kiểu cửa sổ"),
                "Hình 28.10 · Bộ chỉ thị lưu lượng. Góc của lá chắn là thước đo lưu lượng; loại rẻ "
                "tiền dùng cửa sổ thuỷ tinh hoặc nhựa để nhìn trực tiếp lá chắn.",
                "Figure 28.10 · Flow indicator. The angle of the vane provides a measure of the flow "
                "rate; low-cost units use a glass or plastic window for a direct view of the flap.",
                "Cửa sổ trong suốt nhìn thấy lá chắn nghiêng và thang chia",
                "A transparent window showing the inclined flap and a scale")


def _weir_crest(o, x1, x2, ybase, h, label=""):
    """Channel floor plus a weir plate standing h above it."""
    o.append(_line(x1, ybase, x2, ybase, E, 1.6))
    o.append(_line(x1, ybase - h, x2, ybase - h, E, 1.6))


def fig_28_11():
    o = [_defs()]
    # side elevation of the channel with the weir plate
    yb = 300
    o.append(_line(60, yb, 250, yb, E, 1.7))
    o.append(_line(250, yb, 250, yb - 120, E, 1.7))
    o.append(_line(250, yb - 120, 262, yb - 120, E, 1.7))
    o.append(_line(262, yb - 120, 262, yb, E, 1.7))
    o.append(_line(262, yb, 620, yb, E, 1.7))
    # water surface upstream and the nappe falling over the crest
    o.append(_line(60, 150, 250, 150, "#7aa7c7", 1.6))
    o.append(_path("M250,150 C286,152 300,196 316,238 C330,274 356,290 392,292", "#7aa7c7", 1.8))
    o.append(_path("M250,150 C290,154 306,200 322,240", "#7aa7c7", 1.0, "none", "5 4"))
    o.append(_lbl(268, 168, "màng nước", "ts"))
    o.append(_lbl(268, 182, "nappe", "ts"))
    o.append(_lbl(150, 142, "mặt nước thượng lưu", "ts", "middle"))
    # ventilation hole under the nappe
    o.append(_circ(284, 258, 8, P, E, 1.3))
    o.append(_lbl(300, 274, "lỗ thông hơi", "ts"))
    # dimensions
    o.append(_darr(200, 150, 200, 180, S, 1.0))
    o.append(_lbl(192, 172, "h", "tb", "end"))
    o.append(_darr(214, 180, 214, yb, S, 1.0))
    o.append(_lbl(206, 250, "P", "tb", "end"))
    o.append(_darr(250, 330, 262, 330, S, 1.0))
    o.append(_lbl(256, 348, "b", "tb", "middle"))
    # inset: crest bevel
    o.append(_circ(556, 96, 52, P, E, 1.2))
    o.append(_path("M520,72 L592,72 L592,86 L520,86 Z", E, 1.3, "#eef2f7"))
    o.append(_line(592, 72, 570, 100, E, 1.3))
    o.append(_lbl(600, 96, "45°", "ts"))
    o.append(_lbl(556, 168, "cạnh đỉnh vát 45°", "ts", "middle"))
    o.append(_lbl(556, 182, "45° bevel", "ts", "middle"))
    return _fig(svg(680, 366, "".join(o), "Đập tràn thành mỏng toàn chiều rộng"),
                "Hình 28.11 · Đập tràn thành mỏng toàn chiều rộng. Lưu lượng Q biến thiên theo mức "
                "nước h trên đỉnh tràn (Q ~ h^(3/2)) và theo hệ số lưu lượng C_d phụ thuộc lưu lượng.",
                "Figure 28.11 · Full-width thin plate weir. Flow rate Q varies with water level h "
                "above the weir crest (Q ~ h^(3/2)) and with a flow-dependent discharge coefficient.",
                "Mặt cắt đập tràn thành mỏng với màng nước đổ, kích thước h và P, và hình phóng to cạnh vát",
                "Side view of a thin plate weir with the falling nappe, the h and P dimensions, and a bevel inset")


def fig_28_12():
    o = [_defs()]
    yb = 300
    # front elevation: channel B with a rectangular notch b
    o.append(_line(90, yb, 90, 120, E, 1.7))
    o.append(_line(90, 120, 250, 120, E, 1.7))
    o.append(_line(250, 120, 250, 190, E, 1.7))
    o.append(_line(250, 190, 430, 190, E, 1.7))
    o.append(_line(430, 190, 430, 120, E, 1.7))
    o.append(_line(430, 120, 590, 120, E, 1.7))
    o.append(_line(590, 120, 590, yb, E, 1.7))
    # water surface
    o.append(_line(96, 158, 424, 158, "#7aa7c7", 1.4))
    o.append(_lbl(260, 176, "màng nước / nappe", "ts", "middle"))
    # dimensions
    o.append(_darr(90, 336, 590, 336, S, 1.0))
    o.append(_lbl(340, 354, "B — chiều rộng kênh", "ts", "middle"))
    o.append(_darr(250, 214, 430, 214, S, 1.0))
    o.append(_lbl(340, 232, "b — chiều rộng cửa tràn", "ts", "middle"))
    o.append(_darr(466, 158, 466, 190, S, 1.0))
    o.append(_lbl(476, 178, "h", "tb"))
    o.append(_darr(466, 190, 466, yb, S, 1.0))
    o.append(_lbl(476, 250, "p", "tb"))
    return _fig(svg(680, 372, "".join(o), "Đập tràn thành mỏng hình chữ nhật"),
                "Hình 28.12 · Đập tràn thành mỏng hình chữ nhật (cửa tràn hẹp hơn kênh). Hệ số lưu "
                "lượng C_d phụ thuộc lưu lượng, nên phải hiệu chuẩn hoặc dùng công thức thực nghiệm.",
                "Figure 28.12 · Thin plate rectangular notch weir — the notch is narrower than the "
                "channel. The discharge coefficient depends on flow, so calibration or an empirical "
                "correction is needed.",
                "Mặt đứng đập tràn chữ nhật với kích thước B, b, h và p",
                "Front elevation of a rectangular notch weir with the B, b, h and p dimensions")


def fig_28_13():
    o = [_defs()]
    yb = 300
    o.append(_line(90, yb, 90, 110, E, 1.7))
    o.append(_line(90, 110, 590, 110, E, 1.7))
    o.append(_line(590, 110, 590, yb, E, 1.7))
    # V notch
    o.append(_path("M250,110 L340,238 L430,110", E, 1.8))
    o.append(_line(90, yb, 250, yb, E, 1.7))
    o.append(_line(430, yb, 590, yb, E, 1.7))
    o.append(_line(250, yb, 250, 110, "#eef2f7", 0))
    # water surface
    o.append(_line(96, 160, 424, 160, "#7aa7c7", 1.4))
    # angle
    o.append(_path("M340,238 m0,-56 a56,56 0 0 0 -30,10", S, 1.0, "none", "4 3"))
    o.append(_lbl(348, 196, "θ", "tb"))
    o.append(_darr(466, 160, 466, 238, S, 1.0))
    o.append(_lbl(476, 204, "h", "tb"))
    o.append(_darr(466, 238, 466, yb, S, 1.0))
    o.append(_lbl(476, 276, "p", "tb"))
    o.append(_lbl(340, 278, "màng nước hình chữ V", "ts", "middle"))
    return _fig(svg(680, 372, "".join(o), "Đập tràn thành mỏng hình chữ V"),
                "Hình 28.13 · Đập tràn thành mỏng hình chữ V. Vì chiều dài mép ướt thay đổi theo mức "
                "nước nên hệ số lưu lượng gần như không đổi, và dải đo rộng hơn cửa tràn chữ nhật.",
                "Figure 28.13 · Thin plate V-notch weir. Because the wetted edge changes with head, "
                "the discharge coefficient is almost independent of flow, and the range is wider "
                "than a rectangular notch.",
                "Mặt đứng đập tràn chữ V với góc đỉnh và kích thước h, p",
                "Front elevation of a V-notch weir with the apex angle and h, p dimensions")


def fig_28_14():
    o = [_defs()]
    yb = 300
    # sill of length l standing above the floor
    o.append(_line(60, yb, 180, yb, E, 1.7))
    o.append(_line(180, yb, 180, 220, E, 1.7))
    o.append(_line(180, 220, 470, 220, E, 1.7))
    o.append(_line(470, 220, 470, yb, E, 1.7))
    o.append(_line(470, yb, 620, yb, E, 1.7))
    # water surfaces
    o.append(_line(60, 150, 180, 150, "#7aa7c7", 1.6))
    o.append(_path("M180,150 C210,152 224,164 250,166 L470,166", "#7aa7c7", 1.6))
    o.append(_path("M470,166 C500,190 512,244 528,286", "#7aa7c7", 1.6))
    o.append(_lbl(96, 142, "mặt nước thượng lưu", "ts", "middle"))
    o.append(_lbl(340, 158, "mặt nước trên đỉnh", "ts", "middle"))
    # dimensions
    o.append(_darr(140, 150, 140, 220, S, 1.0))
    o.append(_lbl(132, 190, "h₁", "tb", "end"))
    o.append(_darr(340, 166, 340, 220, S, 1.0))
    o.append(_lbl(332, 198, "h₂", "tb", "end"))
    o.append(_darr(180, 250, 470, 250, S, 1.0))
    o.append(_lbl(325, 268, "l — chiều dài đỉnh tràn", "ts", "middle"))
    o.append(_lbl(325, 336, "Lưu lượng cực đại khi h₂ = 2h₁/3", "t", "middle"))
    o.append(_lbl(325, 352, "Maximum discharge when h₂ = 2h₁/3", "ts", "middle"))
    return _fig(svg(680, 372, "".join(o), "Đập tràn đỉnh rộng"),
                "Hình 28.14 · Đập tràn đỉnh rộng. Đỉnh đủ dài để các đường dòng phía trên trở nên "
                "thẳng và song song; lưu lượng đạt cực đại khi độ sâu trên đỉnh bằng 2/3 cột nước "
                "tổng, và đây cũng là trạng thái ổn định của đập.",
                "Figure 28.14 · Broad-crested weir. The sill is long enough for straight, parallel "
                "streamlines to form above it; discharge peaks when the depth over the crest is "
                "two thirds of the total head, which is also the stable condition.",
                "Mặt cắt đập tràn đỉnh rộng với hai mức nước h1 và h2 và chiều dài đỉnh l",
                "Section through a broad-crested weir with h1, h2 and the sill length l")


def fig_28_15():
    o = [_defs()]
    # plan view: channel narrowing to a throat then widening
    o.append(_path("M60,110 L200,110 L300,150 L400,150 L500,110 L620,110", E, 1.7))
    o.append(_path("M60,230 L200,230 L300,190 L400,190 L500,230 L620,230", E, 1.7))
    o.append(_line(60, 110, 60, 230, E, 1.7))
    o.append(_line(620, 110, 620, 230, E, 1.7))
    o.append(_lbl(340, 92, "nhìn bằng / plan view", "ts", "middle"))
    o.append(_lbl(340, 172, "họng", "ts", "middle"))
    o.append(_darr(200, 262, 300, 262, S, 1.0))
    o.append(_lbl(250, 280, "2 h_max", "ts", "middle"))
    o.append(_darr(300, 262, 400, 262, S, 1.0))
    o.append(_lbl(350, 280, "L", "ts", "middle"))
    o.append(_darr(500, 262, 620, 262, S, 1.0))
    o.append(_lbl(560, 280, "≥ 3 (B − b)", "ts", "middle"))
    # section view
    o.append(_line(60, 400, 200, 400, E, 1.7))
    o.append(_path("M200,400 L300,360 L400,360 L500,400 L620,400", E, 1.7))
    o.append(_line(60, 340, 200, 340, "#7aa7c7", 1.6))
    o.append(_path("M200,340 L300,352 L400,352 L500,372", "#7aa7c7", 1.6))
    o.append(_lbl(130, 332, "mặt nước", "ts", "middle"))
    o.append(_darr(120, 340, 120, 400, S, 1.0))
    o.append(_lbl(112, 372, "P", "tb", "end"))
    o.append(_lbl(340, 430, "mặt cắt dọc / section", "ts", "middle"))
    return _fig(svg(680, 448, "".join(o), "Máng Venturi đo lưu lượng hở"),
                "Hình 28.15 · Máng Venturi. Thu hẹp chiều rộng kênh làm vận tốc trong đoạn hẹp tăng "
                "và mức nước hạ xuống; phần lớn cột nước được phục hồi ở đoạn loe. Lưu lượng cực đại "
                "khi độ sâu họng bằng 2/3 cột nước tổng.",
                "Figure 28.15 · Venturi flume. Narrowing the channel raises the velocity in the throat "
                "and lowers the water level; most of the head is recovered in the diverging section. "
                "Maximum discharge when the throat depth is 2/3 of the total head.",
                "Máng Venturi nhìn bằng và mặt cắt dọc, có kích thước họng và chiều dài",
                "Venturi flume in plan and section with the throat dimensions and lengths")


def _coef_axes(o, xlab, ylab, w=560, h=300):
    """Log–log axes for the two rotameter coefficient plots."""
    b = Box(w, h, (1, 100), (0.3, 10), pad=(56, 18, 18, 42))
    o.append(b.axes(xlab, ylab,
                    xt=[(1, "1"), (3, "3"), (10, "10"), (30, "30"), (100, "100")],
                    yt=[(0.3, "0,3"), (1, "1"), (3, "3"), (10, "10")]))
    return b


def fig_28_16():
    o = [_defs()]
    b = _coef_axes(o, "Ru", "α")
    for m, off in ((1.0, 0.0), (2.0, 0.55)):
        pts = []
        for i in range(60):
            ru = 1.0 * (100.0 ** (i / 59.0))
            val = (3.4 + off) / (1.0 + (ru / (14.0 - 4 * off)) ** 0.85)
            pts.append((ru, max(0.35, val)))
        o.append(b.curve(pts))
    o.append(b.label(2.0, 5.4, "m nhỏ", "ts"))
    o.append(b.label(2.0, 3.1, "m lớn", "ts"))
    return _fig(svg(560, 300, "".join(o), "Hệ số lưu lượng α theo số Ruppel"),
                "Hình 28.16 · Hệ số lưu lượng α của rotameter theo số Ruppel Ru và tỉ số diện tích mở "
                "m. Với hình học cho trước, α không đổi ở Ru thấp (chảy tầng) rồi giảm khi Ru tăng.",
                "Figure 28.16 · Rotameter flow coefficient α as a function of Ruppel number Ru and "
                "open area ratio m. For a given geometry α is constant at low Ru (laminar flow) and "
                "falls as Ru rises.",
                "Đồ thị log–log của α theo Ru với hai đường ứng với hai giá trị m",
                "Log–log plot of α against Ru with two curves for two values of m")


def fig_28_17():
    o = [_defs()]
    b = _coef_axes(o, "Ru", "β")
    for m, off in ((1.0, 0.0), (2.0, 0.5)):
        pts = []
        for i in range(60):
            ru = 1.0 * (100.0 ** (i / 59.0))
            val = (0.30 + off * 0.22) * (ru ** 0.42) / (1.0 + (ru / 9.0) ** 0.42 * 0.0)
            val = min(val, 3.2 + off * 1.1)
            pts.append((ru, max(0.32, val)))
        o.append(b.curve(pts))
    o.append(b.label(1.45, 4.4, "vùng tầng", "ts"))
    o.append(b.label(96, 4.4, "vùng rối", "ts", "end"))
    return _fig(svg(560, 300, "".join(o), "Hệ số lưu lượng β theo số Ruppel"),
                "Hình 28.17 · Hệ số lưu lượng β theo số Ruppel Ru và tỉ số diện tích mở m. Trong vùng "
                "tầng, log β tăng tuyến tính theo log Ru; sau đó chuyển dần sang đường nằm ngang khi "
                "dòng hoàn toàn rối.",
                "Figure 28.17 · Rotameter flow coefficient β against Ruppel number Ru and open area "
                "ratio m. In the laminar region log β rises linearly with log Ru, then turns over "
                "into a horizontal line once the flow is fully turbulent.",
                "Đồ thị log–log của β theo Ru với hai đường cong",
                "Log–log plot of β against Ru with two curves")


def fig_28_18():
    o = [_defs()]
    # half diametral plane: tube wall on the right, axis on the left
    o.append(_line(90, 60, 90, 330, S, 1.2, "6 4"))
    o.append(_path("M470,60 L470,150 Q470,196 452,236 L452,330", E, 1.7))
    # bob outline
    o.append(_path("M300,150 L360,150 L360,196 L330,222 L300,196 Z", E, 1.5, "#eef2f7"))
    o.append(_lbl(330, 240, "phao", "ts", "middle"))
    # vector field: strong near the wall gap, recirculation above the bob
    import random as _r
    _r.seed(7)
    for gy in range(80, 330, 26):
        for gx in range(110, 460, 30):
            if 290 < gx < 370 and 140 < gy < 230:
                continue
            ux = 0.55 + 0.9 * ((gx - 90) / 380.0)
            uy = 0.0
            if gy < 140:
                uy = -0.15
            elif 230 < gy < 300 and gx < 330:
                ux = -0.35
            o.append(_arr(gx, gy, gx + 18 * ux, gy + 18 * uy, "#5b6b7c", "ah28s", 0.9))
    o.append(_lbl(280, 46, "trục đối xứng", "ts", "middle"))
    o.append(_lbl(90, 348, "trục", "ts", "middle"))
    return _fig(svg(680, 366, "".join(o), "Vector vận tốc tính toán cho dòng tầng qua rotameter"),
                "Hình 28.18 · Vector vận tốc tính toán cho dòng tầng qua rotameter, trên nửa mặt phẳng "
                "đường kính, dòng đối xứng trục, Re = 220. (Hình gốc trong sách ghi “Figure not "
                "available”; hình này dựng lại theo mô tả trong mục “Computed Flow Field”.)",
                "Figure 28.18 · Computed velocity vectors for laminar flow through a rotameter, in a "
                "half diametral plane for axisymmetric flow at Reynolds number 220. (The original is "
                "marked “Figure not available”; this is redrawn from the description in “Computed "
                "Flow Field”.)",
                "Trường vector vận tốc quanh phao trong nửa mặt phẳng đường kính",
                "Velocity vector field around the bob in a half diametral plane")


def fig_28_19():
    o = [_defs()]
    o.append(_line(90, 60, 90, 330, S, 1.2, "6 4"))
    o.append(_path("M470,60 L470,150 Q470,196 452,236 L452,330", E, 1.7))
    o.append(_path("M300,150 L360,150 L360,196 L330,222 L300,196 Z", E, 1.5, "#eef2f7"))
    # streamlines: converging in the annulus, recirculating above the bob
    for i, x0 in enumerate(range(110, 470, 26)):
        d = "M%s,330 C%s,250 %s,180 %s,80" % (_f(x0), _f(x0 + 4), _f(x0 + 10), _f(x0 + 6))
        o.append(_path(d, "#5b6b7c", 1.1))
    for i in range(4):
        cy = 96 + i * 14
        o.append(_path("M120,%s C200,%s 260,%s 300,%s" % (_f(cy), _f(cy - 10), _f(cy + 12),
                                                          _f(cy + 4)), "#5b6b7c", 1.0))
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    for i, lab in enumerate(labels):
        x = 120 + i * 28
        o.append(_lbl(x, 74 + (i % 2) * 12, lab, "ts", "middle"))
    return _fig(svg(680, 366, "".join(o), "Đường dòng tính toán cho dòng tầng qua rotameter"),
                "Hình 28.19 · Đường dòng tính toán cho dòng tầng qua rotameter (Re = 220). Dòng bị ép "
                "qua vành khuyên hẹp giữa phao và thành ống, rồi tạo vùng hồi lưu ngay trên phao.",
                "Figure 28.19 · Computed streamlines for laminar flow through a rotameter "
                "(Reynolds number 220). The flow is forced through the narrow annulus between bob "
                "and wall, then forms a recirculation region just above the bob.",
                "Các đường dòng trong ống quanh phao, có nhãn a đến l",
                "Streamlines in the tube around the bob, labelled a to l")


def fig_28_20():
    o = [_defs()]
    # six small profile panels, one per axial station
    stations = ["45", "65", "88", "110", "135", "210"]
    import math as _mm
    for i, z in enumerate(stations):
        ox = 40 + i * 104
        oy = 200
        w, h = 84, 96
        o.append(_line(ox, oy, ox + w, oy, E, 1.1))
        o.append(_line(ox, oy, ox, oy - h, E, 1.1))
        for j in range(1, 4):
            o.append(_line(ox + j * w / 4.0, oy, ox + j * w / 4.0, oy - 3, S, 1.0))
        # computed profile (solid): peak in the annulus
        pts = []
        for k in range(25):
            r = k / 24.0
            u = (0.92 if z in ("65", "88") else 0.62) * (r ** 0.5) * _mm.exp(-((r - 0.78) ** 2) / 0.06)
            pts.append((ox + w * r, oy - h * min(1.0, u * 1.5)))
        o.append(_path("M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in pts), E, 1.6))
        # measured profile (dashed): slightly rounded, peak further out
        pts2 = []
        for k in range(25):
            r = k / 24.0
            u = (0.86 if z in ("65", "88") else 0.58) * (r ** 0.55) * _mm.exp(-((r - 0.84) ** 2) / 0.09)
            pts2.append((ox + w * r, oy - h * min(1.0, u * 1.5)))
        o.append(_path("M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in pts2), E, 1.3, "none", "4 3"))
        o.append(_lbl(ox + w / 2, oy + 18, "z = %s" % z, "ts", "middle"))
    o.append(_lbl(40, 44, "U_z — thành phần dọc trục (m/s)", "ts"))
    o.append(_lbl(40, 58, "nét liền: tính toán · nét đứt: đo được", "ts"))
    o.append(_lbl(340, 300, "r — vị trí hướng kính", "ts", "middle"))
    return _fig(svg(680, 320, "".join(o), "So sánh mặt cắt vận tốc đo được và tính toán"),
                "Hình 28.20 · So sánh mặt cắt vận tốc đo được (nét đứt) và tính toán (nét liền) cho "
                "dòng tầng qua rotameter, Re = 220, tại sáu vị trí dọc trục z. Đỉnh vận tốc nằm "
                "trong vành khuyên sát thành ống; trên phao xuất hiện vùng hồi lưu.",
                "Figure 28.20 · Measured (dashed) and computed (solid) velocity profiles for laminar "
                "flow through a rotameter at Re = 220, at six axial stations z. The peak sits in the "
                "annulus near the tube wall; a recirculation region appears above the bob.",
                "Sáu ô nhỏ, mỗi ô một mặt cắt vận tốc tại một vị trí z khác nhau",
                "Six small panels, each a velocity profile at a different axial station z")


# ================================================================ 28.3 PD meters

def _tip(a, R, d):
    """Radius from an offset rotor centre to the bore wall along angle a.

    The rotor centre sits d px from the bore centre on the +y (SVG downward)
    axis; a is measured from +x in radians. Used for the sliding-vane meter,
    where the vanes must reach the wall across the crescent."""
    uy = _m.sin(a)
    b = uy * d
    return -b + _m.sqrt(b * b + R * R - d * d)


def _thick(x1, y1, x2, y2, col=E, sw=6):
    return ('<path d="M%s,%s L%s,%s" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" fill="none"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _stub(cx, cy, R, side, y1, y2, ln=30):
    """A short pipe stub leaving the bore wall on one side, capped at the end."""
    sgn = -1 if side == "l" else 1
    xa = cx + sgn * _m.sqrt(max(1.0, R * R - (cy - y1) * (cy - y1)))
    xb = cx + sgn * (R + ln)
    o = [_line(xa, y1, xb, y1, E, 1.5), _line(xa, y2, xb, y2, E, 1.5),
         _line(xb, y1, xb, y2, E, 1.5)]
    return o


def _bellows(x, y, w, h, n=7):
    """Vertical accordion: zigzag left edge, mirrored right edge, closed box."""
    left, right = [], []
    for i in range(n + 1):
        yy = y + h * i / float(n)
        bulge = w * 0.30 if i % 2 else 0.0
        left.append((x + bulge, yy))
        right.append((x + w - bulge, yy))
    d = "M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in left)
    d += " L" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in reversed(right))
    d += " Z"
    return d


def _peanut(cx, cy, R, gap):
    """Union outline of two equal circles of radius R whose centres are gap apart."""
    h = _m.sqrt(R * R - (gap / 2.0) ** 2)
    return ("M%s,%s A%s,%s 0 1 0 %s,%s A%s,%s 0 1 0 %s,%s Z"
            % (_f(cx), _f(cy - h), _f(R), _f(R), _f(cx), _f(cy + h),
               _f(R), _f(R), _f(cx), _f(cy - h)))


def fig_28_21():
    o = [_defs()]
    cy, R, r, d = 128, 64, 40, -24
    for k, cx in enumerate((118, 340, 562)):
        o.append(_circ(cx, cy, R + 9, "none", E, 1.1))
        o.append(_circ(cx, cy, R, WARM, E, 2.4))
        o += _stub(cx, cy, R, "l", cy - 38, cy - 8, 26)
        o += _stub(cx, cy, R, "r", cy - 38, cy - 8, 26)
        o.append(_circ(cx, cy + d, r, P, E, 1.9))
        o.append(_circ(cx, cy + d, 7, E, E, 1.0))
        base = _m.radians(20 + 24 * k)
        for i in range(4):
            a = base + i * _m.pi / 2
            t = _tip(a, R, d) - 2
            o.append(_thick(cx, cy + d, cx + t * _m.cos(a), cy + d + t * _m.sin(a),
                            "#8fa3b8", 7))
        o.append(_lbl(cx, cy + R + 34, "vị trí %d" % (k + 1), "ts", "middle"))
    o.append(_arr(34, cy - 23, 54, cy - 23, S, "ah28s", 1.4))
    o.append(_lbl(28, cy - 50, "vào", "ts"))
    o.append(_arr(646, cy - 23, 626, cy - 23, S, "ah28s", 1.4))
    o.append(_lbl(652, cy - 50, "ra", "ts", "end"))
    return _fig(svg(680, 232, "".join(o), "Ba pha làm việc của lưu lượng kế thể tích kiểu cánh trượt"),
                "Hình 28.21 · Ba pha trong một vòng quay của lưu lượng kế thể tích kiểu cánh trượt. "
                "Rôto lệch tâm trong vỏ tròn; mỗi cánh trượt ra vào rãnh để luôn áp sát thành, nhốt "
                "một thể tích chất lưu ở vành khuyên rồi đẩy sang cửa ra.",
                "Figure 28.21 · Three phases of one revolution of a sliding-vane PD meter. The rotor "
                "is eccentric inside the round housing; each vane slides in and out of its slot to "
                "stay against the wall, trapping a volume in the crescent and sweeping it to the "
                "outlet.",
                "Ba vỏ tròn cạnh nhau, mỗi vỏ có rôto bốn cánh trượt ở một góc quay khác nhau",
                "Three round housings side by side, each with a four-vane rotor at a different angle")


def fig_28_22():
    o = [_defs()]
    cy, R = 128, 66
    for k, cx in enumerate((118, 340, 562)):
        o.append(_circ(cx, cy, R + 9, "none", E, 1.1))
        o.append(_circ(cx, cy, R, WARM, E, 2.4))
        o.append(_path("M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z" % (
            _f(cx), _f(cy - 26), _f(cx + 20), _f(cy - 26), _f(cx + 26), _f(cy - 2),
            _f(cx), _f(cy + 20), _f(cx - 26), _f(cy - 2), _f(cx - 20), _f(cy - 26),
            _f(cx), _f(cy - 26)), E, 1.8, P))
        base = _m.radians(15 + 22 * k)
        for i in range(3):
            a = base + i * 2 * _m.pi / 3
            a2 = a + 0.30
            o.append('<path d="M%s,%s Q%s,%s %s,%s" stroke="#8fa3b8" stroke-width="9" '
                     'fill="none" stroke-linecap="round"/>'
                     % (_f(cx + 24 * _m.cos(a)), _f(cy + 24 * _m.sin(a)),
                        _f(cx + 52 * _m.cos(a + 0.08)), _f(cy + 52 * _m.sin(a + 0.08)),
                        _f(cx + 60 * _m.cos(a2)), _f(cy + 60 * _m.sin(a2))))
        o.append(_lbl(cx, cy + R + 34, "vị trí %d" % (k + 1), "ts", "middle"))
    o.append(_arr(16, cy - 23, 48, cy - 23, S, "ah28s", 1.4))
    o.append(_lbl(14, cy - 52, "vào", "ts"))
    o.append(_arr(664, cy - 23, 632, cy - 23, S, "ah28s", 1.4))
    o.append(_lbl(666, cy - 52, "ra", "ts", "end"))
    return _fig(svg(680, 232, "".join(o), "Ba pha của lưu lượng kế thể tích kiểu ba rôto"),
                "Hình 28.22 · Nguyên lý lưu lượng kế ba rôto: ba cánh quay trong vỏ tròn, chất lưu bị "
                "nhốt giữa cánh và thành vỏ rồi được quét qua cửa ra. Một vòng của cơ cấu trên "
                "ứng với hai vòng của cánh, do bộ ba bánh răng định thời.",
                "Figure 28.22 · The trirotor principle: three blades turn inside a round housing, "
                "trapping liquid between blade and wall and sweeping it to the outlet. One turn of "
                "the top mechanism corresponds to two turns of the blades, set by a three-gear "
                "timing assembly.",
                "Ba vỏ tròn, mỗi vỏ có ba cánh quay quanh một cửa chắn hình tim ở giữa",
                "Three round housings, each with three blades sweeping past a heart-shaped gate")


def fig_28_23():
    o = [_defs()]
    o.append(_lbl(40, 24, "Nguyên lý BiRotor chuẩn — dòng vuông góc với trục rôto", "t"))
    for k, cx in enumerate((120, 340, 560)):
        x0, y0, w, h = cx - 92, 40, 184, 96
        o.append(_arr(x0 - 30, y0 + h / 2, x0 - 4, y0 + h / 2, S, "ah28s", 1.3))
        o.append(_arr(x0 + w + 4, y0 + h / 2, x0 + w + 30, y0 + h / 2, S, "ah28s", 1.3))
        o.append(_rect(x0, y0, w, h, WARM, E, 2.0, rx=4))
        for s in (-1, 1):
            ax, ay = cx + s * 40, y0 + h / 2
            rot = _m.radians(30 * k) + (0 if s < 0 else _m.pi / 2)
            for lobe in (-1, 1):
                lx = ax + lobe * 15 * _m.cos(rot + _m.pi / 2)
                ly = ay + lobe * 15 * _m.sin(rot + _m.pi / 2)
                o.append(_circ(lx, ly, 21, P, E, 1.8))
            o.append(_line(ax - 15 * _m.cos(rot + _m.pi / 2), ay - 15 * _m.sin(rot + _m.pi / 2),
                           ax + 15 * _m.cos(rot + _m.pi / 2), ay + 15 * _m.sin(rot + _m.pi / 2),
                           E, 1.2))
            o.append(_circ(ax, ay, 3.4, E, E, 0.8))
    for cx, txt in ((120, "dòng vào"), (340, "chuyển tiếp"), (560, "dòng ra")):
        o.append(_lbl(cx, 158, txt, "ts", "middle"))
    o.append(_lbl(40, 196, "Nguyên lý dòng hướng trục — trục rôto song song với dòng chảy", "t"))
    for k, cx in enumerate((120, 340, 560)):
        x0, y0, w, h = cx - 92, 212, 184, 76
        o.append(_arr(x0 - 30, y0 + h / 2, x0 - 4, y0 + h / 2, S, "ah28s", 1.3))
        o.append(_arr(x0 + w + 4, y0 + h / 2, x0 + w + 30, y0 + h / 2, S, "ah28s", 1.3))
        o.append(_rect(x0, y0, w, h, WARM, E, 2.0, rx=4))
        for s in (-1, 1):
            ax, ay = cx + s * 40, y0 + h / 2
            o.append(_circ(ax, ay, 26, P, E, 1.8))
            rot = _m.radians(30 * k) + (0 if s < 0 else _m.pi / 2)
            o.append(_thick(ax - 20 * _m.cos(rot), ay - 20 * _m.sin(rot),
                            ax + 20 * _m.cos(rot), ay + 20 * _m.sin(rot), "#8fa3b8", 10))
            o.append(_circ(ax, ay, 3.4, E, E, 0.9))
    o.append(_lbl(340, 314, "cụm đo đặt song song với dòng: lắp gọn hơn, chính xác hơn, tổn thất thấp hơn",
                  "ts", "middle"))
    return _fig(svg(680, 330, "".join(o), "Nguyên lý lưu lượng kế hai rôto kiểu BiRotor"),
                "Hình 28.23 · Lưu lượng kế hai rôto. Hàng trên: bản chuẩn, dòng chảy vuông góc với "
                "trục rôto. Hàng dưới: bản dòng hướng trục, cùng chi tiết và cùng nguyên lý nhưng "
                "cụm đo đặt song song với dòng — lắp gọn hơn, chính xác hơn và tổn thất thấp hơn.",
                "Figure 28.23 · The birotor meter. Top row: the standard version, with flow "
                "perpendicular to the rotor axes. Bottom row: the axial-flow version, identical in "
                "parts and principle but with the measuring unit parallel to the flow — more "
                "compact, more accurate and with lower loss.",
                "Hai hàng, mỗi hàng ba ô, mỗi ô hai rôto hình số tám trong vỏ chữ nhật",
                "Two rows of three panels, each panel showing two figure-eight rotors in a "
                "rectangular housing")


def fig_28_24():
    o = [_defs()]
    cx, cy = 340, 133
    o.append(_rect(110, 58, 460, 150, WARM, E, 2.2, rx=10))
    o.append(_circ(cx, cy, 26, P, E, 1.9))
    o.append(_circ(cx, cy, 6, E, E, 1.0))
    for a in (_m.radians(55), _m.radians(125), _m.radians(235), _m.radians(305)):
        bx, by = cx + 64 * _m.cos(a), cy + 64 * _m.sin(a)
        o.append(_line(cx + 24 * _m.cos(a), cy + 24 * _m.sin(a),
                       cx + 46 * _m.cos(a), cy + 46 * _m.sin(a), E, 3.0))
        o.append('<rect x="%s" y="%s" width="30" height="36" rx="4" fill="%s" stroke="%s" '
                 'stroke-width="1.8" transform="rotate(%s %s %s)"/>'
                 % (_f(bx - 15), _f(by - 18), P, E, _f(_m.degrees(a) + 90), _f(bx), _f(by)))
    o.append(_arr(44, cy, 104, cy, S, "ah28s", 1.5))
    o.append(_lbl(40, cy - 12, "vào", "ts"))
    o.append(_arr(636, cy, 576, cy, S, "ah28s", 1.5))
    o.append(_lbl(640, cy - 12, "ra", "ts"))
    o.append(_line(cx, cy + 26, cx, 232, S, 1.0, "3 3"))
    o.append(_lbl(cx, 246, "rôto lệch tâm (tay quay)", "ts", "middle"))
    o.append(_line(470, 240, 392, 100, S, 1.0, "3 3"))
    o.append(_lbl(474, 246, "pít-tông (4 chiếc)", "ts"))
    return _fig(svg(680, 268, "".join(o), "Lưu lượng kế thể tích kiểu pít-tông bốn xi-lanh"),
                "Hình 28.24 · Lưu lượng kế kiểu pít-tông. Một chi tiết quay ở giữa tạo chuyển động "
                "tịnh tiến cho cả bốn pít-tông; các pít-tông xả lệch pha nhau nên dòng ra gần như "
                "liên tục. Kiểu này chịu được chênh áp lớn nên đo được chất lỏng rất nhớt.",
                "Figure 28.24 · The piston meter. A central rotating part drives all four pistons; "
                "their discharges are phased so the outlet flow is nearly continuous. The "
                "piston-cylinder design withstands large differential pressures, so very viscous "
                "liquids can be metered.",
                "Một vỏ chữ nhật với rôto giữa và bốn pít-tông toả ra bốn phía",
                "A rectangular housing with a central rotor and four pistons radiating outwards")


def fig_28_25():
    o = [_defs()]
    cy = 118
    for k, cx in enumerate((120, 340, 560)):
        o.append(_rect(cx - 96, cy - 52, 192, 104, WARM, E, 2.2, rx=6))
        for s in (-1, 1):
            ax, ay = cx + s * 28, cy
            ang = 40 * k + (0 if s < 0 else 90)
            o.append('<ellipse cx="%s" cy="%s" rx="28" ry="21" fill="%s" stroke="%s" '
                     'stroke-width="1.9" transform="rotate(%s %s %s)"/>'
                     % (_f(ax), _f(ay), P, E, _f(ang), _f(ax), _f(ay)))
            o.append(_circ(ax, ay, 3.2, E, E, 0.8))
        o.append(_arr(cx - 122, cy, cx - 98, cy, S, "ah28s", 1.3))
        o.append(_arr(cx + 98, cy, cx + 122, cy, S, "ah28s", 1.3))
    o.append(_lbl(340, 200, "mỗi vòng quay chuyển bốn thể tích riêng phần", "ts", "middle"))
    return _fig(svg(680, 220, "".join(o), "Ba pha của lưu lượng kế bánh răng oval"),
                "Hình 28.25 · Lưu lượng kế bánh răng oval. Hai bánh răng oval ăn khớp, quay nhờ chênh "
                "áp; mỗi vòng quay chuyển bốn thể tích riêng phần giữa bánh răng và thành buồng đo. "
                "Truyền động ra trục ra qua kín cơ khí hoặc khớp từ.",
                "Figure 28.25 · The oval-gear meter. Two oval gears mesh and turn on the differential "
                "pressure; each revolution transfers four partial volumes between gear and chamber "
                "wall. Drive reaches the output shaft through a mechanical seal or a magnetic "
                "coupling.",
                "Ba ô, mỗi ô hai bánh răng oval ăn khớp trong vỏ chữ nhật",
                "Three panels, each with two meshing oval gears in a rectangular housing")


def fig_28_26():
    o = [_defs()]
    for k, (cx, cy) in enumerate(((112, 86), (282, 86), (112, 232), (282, 232))):
        o.append(_circ(cx, cy, 54, WARM, E, 2.2))
        o.append('<ellipse cx="%s" cy="%s" rx="44" ry="15" fill="%s" stroke="%s" '
                 'stroke-width="1.8" transform="rotate(%s %s %s)"/>'
                 % (_f(cx), _f(cy), P, E, _f(22 * k), _f(cx), _f(cy)))
        px = cx + 40 * _m.cos(_m.radians(22 * k))
        py = cy + 40 * _m.sin(_m.radians(22 * k))
        o.append(_circ(px, py, 4.5, E, E, 0.9))
        o.append(_lbl(cx, cy + 76, "pha %d" % (k + 1), "ts", "middle"))
    lx = 400
    o.append(_lbl(lx, 62, "Cấu tạo", "t"))
    for i, (name, note) in enumerate((
            ("Đĩa nghiêng (nutator)", "quay lắc trong buồng cầu"),
            ("Chốt dẫn", "truyền chuyển động ra bộ đếm"),
            ("Vách chia", "tách hai buồng thể tích"),
            ("Cửa vào / cửa ra", "lệch nhau nửa vòng"),
            ("Buồng đo", "một buồng đầy, một buồng xả"))):
        y = 92 + i * 34
        o.append(_lbl(lx, y, "• " + name, "t"))
        o.append(_lbl(lx + 12, y + 14, note, "ts"))
    return _fig(svg(680, 320, "".join(o), "Bốn pha của lưu lượng kế đĩa nghiêng"),
                "Hình 28.26 · Lưu lượng kế đĩa nghiêng. Đĩa đặt nghiêng trong buồng cầu lắc như con "
                "quay; mỗi pha nhốt đầy một buồng và xả buồng kia. Kết cấu rẻ, độ chính xác vừa "
                "phải, thường gặp trong đồng hồ nước.",
                "Figure 28.26 · The nutating-disk meter. A disk set at an angle inside a spherical "
                "chamber wobbles; each phase fills one chamber while emptying the other. Cheap and "
                "of moderate accuracy, it is common in water meters.",
                "Bốn vòng tròn thể hiện bốn pha lắc của đĩa, kèm danh sách chi tiết bên phải",
                "Four circles showing four phases of the disk, with a parts list at the right")


def fig_28_27():
    o = [_defs()]
    cx, cy, R, gap = 330, 132, 52, 76
    o.append(_path(_peanut(cx, cy, R, gap), E, 2.4, WARM))
    for s in (-1, 1):
        ax = cx + s * gap / 2
        for lobe in (-1, 1):
            o.append(_circ(ax, cy + lobe * 17, 25, P, E, 1.9))
        o.append(_line(ax, cy - 18, ax, cy + 18, E, 1.2))
        o.append(_circ(ax, cy, 3.6, E, E, 0.8))
        # rotation sense
        o.append('<path d="M%s,%s A26,14 0 0 %d %s,%s" stroke="%s" stroke-width="1.4" '
                 'fill="none" marker-end="url(#ah28s)"/>'
                 % (_f(ax - 16), _f(cy - 70), 1 if s < 0 else 0,
                    _f(ax + 16), _f(cy - 70), S))
    o.append(_arr(150, cy + 24, 258, cy + 24, S, "ah28s", 1.5))
    o.append(_lbl(146, cy + 34, "vào", "ts"))
    o.append(_arr(cx + 96, cy - 46, cx + 150, cy - 76, S, "ah28s", 1.5))
    o.append(_lbl(cx + 156, cy - 82, "ra", "ts"))
    o.append(_lbl(cx, cy + 96, "hai rôto hình số tám quay ngược chiều, không chạm nhau", "ts", "middle"))
    return _fig(svg(680, 260, "".join(o), "Sơ đồ lưu lượng kế kiểu Roots"),
                "Hình 28.27 · Sơ đồ lưu lượng kế Roots — loại thể tích phổ biến nhất để đo khí. Hai "
                "rôto hình số tám quay ngược chiều trong vỏ đôi; khe hở cơ khí rất nhỏ nên khí phải "
                "sạch, và dòng ra dao động theo chu kỳ.",
                "Figure 28.27 · Schematic of a Roots meter — the commonest PD meter for gas. Two "
                "figure-eight rotors turn in opposite directions inside a twin-bore housing; the "
                "mechanical clearance is very small, so the gas must be clean, and the outlet flow "
                "pulsates cyclically.",
                "Vỏ hình số tám với hai rôto, mũi tên dòng vào bên trái và dòng ra phía trên",
                "A figure-eight housing with two rotors, inlet arrow at the left and outlet above")


def fig_28_28():
    o = [_defs()]
    cy = 118
    for k, cx in enumerate((170, 470)):
        o.append(_circ(cx, cy, 62, WARM, E, 2.4))
        o.append(_path("M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z" % (
            _f(cx), _f(cy - 30), _f(cx + 18), _f(cy - 30), _f(cx + 26), _f(cy - 4),
            _f(cx), _f(cy + 18), _f(cx - 26), _f(cy - 4), _f(cx - 18), _f(cy - 30),
            _f(cx), _f(cy - 30)), E, 1.8, P))
        base = _m.radians(12 + 30 * k)
        for i in range(4):
            a = base + i * _m.pi / 2
            o.append(_thick(cx + 22 * _m.cos(a), cy + 22 * _m.sin(a),
                            cx + 54 * _m.cos(a), cy + 54 * _m.sin(a), "#8fa3b8", 9))
        o.append(_lbl(cx, cy + 82, "pha %d" % (k + 1), "ts", "middle"))
    o.append(_arr(40, cy, 100, cy, S, "ah28s", 1.5))
    o.append(_lbl(36, cy - 12, "vào", "ts"))
    o.append(_arr(580, cy, 640, cy, S, "ah28s", 1.5))
    o.append(_lbl(644, cy - 12, "ra", "ts"))
    o.append(_lbl(320, 232, "bốn cánh quay trong vành khuyên; cửa chắn cho cánh đi qua nhưng chặn khí",
                  "ts", "middle"))
    return _fig(svg(680, 252, "".join(o), "Hai pha làm việc của lưu lượng kế CVM"),
                "Hình 28.28 · Nguyên lý lưu lượng kế CVM. Bốn cánh quay trong vành khuyên quanh vỏ "
                "tròn; một cửa chắn giống chi tiết giữa của kiểu ba rôto cho cánh đi qua nhưng không "
                "cho khí lọt. Độ chính xác tương đương kiểu Roots nhưng dao động cửa ra nhỏ hơn.",
                "Figure 28.28 · The CVM principle. Four vanes rotate in an annulus around the round "
                "housing; a gate shaped like the centre piece of the trirotor lets the vanes pass "
                "but not the gas. Accuracy matches the Roots meter, with smaller outlet pulsation.",
                "Hai vỏ tròn, mỗi vỏ bốn cánh quay quanh một cửa chắn ở giữa",
                "Two round housings, each with four vanes rotating past a central gate")


def fig_28_29():
    o = [_defs()]
    for k, x0 in enumerate((70, 370)):
        y0, w, h = 78, 240, 150
        o.append(_rect(x0, y0, w, h, WARM, E, 2.2, rx=6))
        for j in range(2):
            bx = x0 + 34 + j * 96
            filled = (j == k)
            o.append(_path(_bellows(bx, y0 + 46, 76, 84, 7),
                           E, 1.7, P if not filled else "#dce6f2"))
        vx = x0 + 60 + (0 if k == 0 else 62)
        o.append(_rect(vx, y0 + 12, 60, 22, "#cfd8e6", E, 1.6, rx=3))
        o.append(_line(vx + 30, y0 + 12, vx + 30, y0 - 4, E, 1.6))
        o.append(_lbl(x0 + 18, y0 - 12, "vào", "ts"))
        o.append(_lbl(x0 + w - 18, y0 - 12, "ra", "ts", "end"))
        o.append(_arr(x0 + 30, y0 - 8, x0 + 30, y0 + 10, S, "ah28s", 1.2))
        o.append(_arr(x0 + w - 30, y0 + 10, x0 + w - 30, y0 - 8, S, "ah28s", 1.2))
        o.append(_lbl(x0 + w / 2, y0 + h + 22, "van trượt ở vị trí %d" % (k + 1), "ts", "middle"))
    o.append(_lbl(340, 274, "van trượt nối cửa vào với mặt trong của một ống xếp, mặt ngoài ống kia "
                            "thông cửa ra; chu kỳ sau đảo lại", "ts", "middle"))
    return _fig(svg(680, 288, "".join(o), "Hai pha của đồng hồ khí kiểu màng xếp"),
                "Hình 28.29 · Đồng hồ khí kiểu màng (ống xếp). Hai ống xếp đóng vai pít-tông, van "
                "trượt đôi đảo chiều nối luân phiên; nhờ vậy đo được lưu lượng rất nhỏ như bấc "
                "đánh lửa của bếp gas.",
                "Figure 28.29 · The diaphragm (bellows) gas meter. Two bellows act as pistons and a "
                "double slide valve alternates the connections; this design measures extremely low "
                "flow rates such as a gas burner pilot light.",
                "Hai vỏ chữ nhật, mỗi vỏ hai ống xếp và một van trượt ở hai vị trí khác nhau",
                "Two rectangular housings, each with two bellows and a slide valve in different "
                "positions")


# ================================================================ 28.4 turbines

def _num(x, y, n, tx, ty):
    """Circled callout number with a thin leader to the part it identifies."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.9" '
            'stroke-dasharray="2 2"/>' % (_f(x), _f(y), _f(tx), _f(ty), S)
            + _circ(x, y, 8, P, E, 1.1)
            + '<text class="ts" x="%s" y="%s" text-anchor="middle">%d</text>'
            % (_f(x), _f(y + 3.5), n))


def _blade_row(cx, cy, R, n=5, phase=0.0, col="#8fa3b8", sw=5):
    """A rotor seen end-on: hub plus n radial blades."""
    o = []
    for i in range(n):
        a = phase + i * 2 * _m.pi / n
        o.append(_thick(cx + 8 * _m.cos(a), cy + 8 * _m.sin(a),
                        cx + (R - 1) * _m.cos(a), cy + (R - 1) * _m.sin(a), col, sw))
    o.append(_circ(cx, cy, 8, E, E, 1.0))
    return o


def fig_28_30():
    o = [_defs()]
    yc = 185
    # ---- housing: bore is symmetric about the axis, 105..265
    o.append(_rect(86, 91, 508, 14, "url(#hatch28)", E, 1.6))
    o.append(_rect(86, 265, 508, 14, "url(#hatch28)", E, 1.6))
    for x in (72, 594):
        o.append(_rect(x, 55, 14, 36, "url(#hatch28)", E, 1.6))
        o.append(_rect(x, 279, 14, 36, "url(#hatch28)", E, 1.6))
    # ---- diffusers, with a support plate above and below each
    for cx in (200, 480):
        o.append(_ell(cx, yc, 74, 46, WARM, E, 1.8))
        o.append(_line(cx - 58, yc, cx + 58, yc, S, 0.9, "4 3"))
    for x in (144, 164, 516, 536):
        o.append(_rect(x, 105, 7, 34, "url(#hatch28b)", E, 1.0))
        o.append(_rect(x, 231, 7, 34, "url(#hatch28b)", E, 1.0))
    # ---- rotor: shaft, bearings, hub, two blades with tip clearance
    o.append(_line(296, yc, 384, yc, E, 2.6))
    o.append(_rect(331, 110, 18, 54, "url(#hatch28b)", E, 1.5))
    o.append(_rect(331, 206, 18, 54, "url(#hatch28b)", E, 1.5))
    o.append(_rect(324, 168, 32, 34, "#dce6f2", E, 1.8, rx=4))
    o.append(_rect(321, 172, 6, 26, "#9aa4b2", E, 1.1))
    o.append(_rect(353, 172, 6, 26, "#9aa4b2", E, 1.1))
    # ---- rotation pickup well
    o.append(_rect(334, 36, 28, 55, P, E, 1.6))
    o.append(_rect(338, 40, 20, 11, E, E, 1.0))
    o.append(_rect(338, 56, 20, 30, "url(#hatch28)", E, 1.3))
    o.append(_line(348, 36, 348, 22, E, 1.1))
    o.append('<polyline points="262,20 272,20 272,8 282,8 282,20 292,20 292,8 302,8 '
             '302,20 312,20 312,8 322,8 322,20" fill="none" stroke="%s" stroke-width="1.3"/>' % E)
    o.append(_lbl(256, 16, "1 V", "ts", "end"))
    # ---- flow through the annulus
    o.append(_arr(286, 122, 324, 122, S, "ah28s", 1.4))
    o.append(_arr(286, 248, 324, 248, S, "ah28s", 1.4))
    o.append(_line(26, yc, 104, yc, S, 0.9, "8 3 2 3"))
    o.append(_lbl(28, yc - 10, "trục đối xứng", "ts"))
    # ---- conditioning plate
    o.append(_line(110, 105, 110, 265, S, 1.4, "5 4"))
    # ---- numbered callouts
    o.append(_num(52, 66, 1, 72, 72))
    o.append(_num(210, 70, 2, 210, 91))
    o.append(_num(402, 36, 3, 362, 42))
    o.append(_num(402, 60, 4, 359, 46))
    o.append(_num(402, 84, 5, 359, 70))
    o.append(_num(626, 132, 6, 352, 120))
    o.append(_num(626, 164, 7, 356, 176))
    o.append(_num(626, 196, 8, 352, 200))
    o.append(_num(626, 228, 9, 384, 186))
    o.append(_num(170, 330, 10, 168, 250))
    o.append(_num(480, 330, 11, 480, 232))
    o.append(_num(96, 330, 12, 110, 250))
    return _fig(svg(680, 352, "".join(o), "Mặt cắt dọc lưu lượng kế tuabin hướng trục"),
                "Hình 28.30 · Mặt cắt dọc theo trục của một lưu lượng kế tuabin hướng trục, "
                "mô tả các bộ phận chính. Thân thường bằng thép không gỉ không từ tính như 304. "
                "Đầu nối thường là mặt bích (như hình), ren hoặc kiểu tri-clover. Hai bộ khuếch tán "
                "trước và sau giống nhau ở lưu lượng kế hai chiều, và thường được đỡ bằng ba tấm "
                "phẳng trở lên, hoặc bằng kết cấu ống, đặt dọc theo thân và đồng thời làm bộ nắn "
                "thẳng dòng. Tỷ lệ khe vành khuyên tại rôto khác nhau giữa các thiết kế. Ổ trượt "
                "thường dùng cho chất lỏng, ổ bi thường dùng cho khí. Đầu thu từ trở (như hình) rất "
                "phổ biến; ngoài ra còn loại cơ khí và loại sóng mang điều chế. (1) Đầu nối — vẽ "
                "kiểu mặt bích; (2) thân lưu lượng kế; (3) đầu thu tốc độ quay — vẽ kiểu từ trở; "
                "(4) nam châm vĩnh cửu; (5) cuộn dây quấn trên cực từ; (6) cánh rôto; (7) moay-ơ "
                "rôto; (8) ổ trục rôto — vẽ kiểu ổ trượt; (9) trục rôto; (10) gối đỡ và bộ nắn "
                "thẳng dòng của bộ khuếch tán; (11) bộ khuếch tán; (12) tấm xử lý dòng chảy (nét "
                "đứt) — tuỳ chọn ở một số lưu lượng kế.",
                "Figure 28.30 · Longitudinal section of an axial turbine flowmeter depicting the key "
                "components. The body is usually a magnetically transparent stainless steel such as "
                "304; end-fittings include face flanges (depicted), threaded fittings and tri-clover "
                "fittings. The diffusers are the same in bidirectional meters and are generally "
                "supported by three or more flat plates aligned with the body, which also act as flow "
                "straighteners. (1) end fitting — flange shown; (2) flowmeter body; (3) rotation "
                "pickup — magnetic, reluctance type shown; (4) permanent magnet; (5) pickup coil "
                "wound on pole piece; (6) rotor blade; (7) rotor hub; (8) rotor shaft bearing — "
                "journal type shown; (9) rotor shaft; (10) diffuser support and flow straightener; "
                "(11) diffuser; (12) flow conditioning plate (dotted) — optional with some meters.",
                "Mặt cắt dọc thân lưu lượng kế với hai bộ khuếch tán, rôto ở giữa và đầu thu từ "
                "trở phía trên",
                "Longitudinal section of the meter body with two diffusers, the central rotor and a "
                "magnetic reluctance pickup on top")


def fig_28_31():
    o = [_defs()]
    # ---- developed blade row
    o.append(_rect(90, 50, 160, 200, FILL, "none", 0))
    ang = _m.radians(32)
    for y0 in (60, 140):
        o.append(_thick(90, y0, 250, y0 + 160 * _m.tan(ang), E, 9))
    # chord, dimensioned just above the upper blade so it stays visible
    o.append(_darr(94, 53, 254, 153, S, 1.1))
    o.append(_line(94, 53, 90, 60, S, 0.9))
    o.append(_line(254, 153, 250, 160, S, 0.9))
    o.append(_lbl(178, 98, "c", "t", "middle"))
    o.append(_line(90, 60, 76, 60, S, 0.9, "3 3"))
    o.append(_line(90, 140, 76, 140, S, 0.9, "3 3"))
    o.append(_darr(80, 60, 80, 140, E, 1.2))
    o.append(_lbl(72, 104, "s", "t", "end"))
    o.append(_line(26, 185, 90, 185, S, 0.9, "8 3 2 3"))
    o.append(_lbl(28, 177, "Trục rôto", "ts"))
    o.append(_arr(34, 36, 104, 36, E, "ah28", 1.4))
    o.append(_lbl(69, 28, "V", "tb", "middle"))
    # ---- velocity triangle
    ox, oy = 330, 170
    o.append(_arr(ox, oy, 500, oy, E, "ah28", 1.6))
    o.append(_lbl(415, 162, "V", "tb", "middle"))
    o.append(_arr(ox, oy, 500, 222, E, "ah28", 1.6))
    o.append(_subs(496, 240, [("V", False), ("E", True)], "end", "tb"))
    o.append(_path("M390,170 A60,60 0 0 1 390,176", E, 1.1))
    o.append(_lbl(398, 184, "θ", "t"))
    o.append(_line(ox, oy, 455, 248, S, 1.1, "5 4"))
    o.append(_path("M440,170 A110,110 0 0 1 423,228", S, 1.0, "none", "4 3"))
    o.append(_lbl(438, 212, "β", "t"))
    # tangential velocity bars: actual and ideal
    o.append(_line(500, 170, 500, 222, E, 2.4))
    o.append(_line(494, 222, 506, 222, E, 1.6))
    o.append(_line(522, 170, 522, 240, E, 2.4))
    o.append(_line(516, 240, 528, 240, E, 1.6))
    o.append(_line(500, 222, 522, 222, S, 0.9, "3 3"))
    o.append(_subs(492, 198, [("r × ω", False)], "end", "t"))
    o.append(_subs(530, 188, [("r × ω", False), ("i", True)], "start", "t"))
    # force along the blade surface
    o.append(_arr(452, 262, 522, 306, G, "ah28g", 1.8))
    o.append(_lbl(530, 312, "F", "tb"))
    return _fig(svg(680, 330, "".join(o), "Giản đồ vectơ cho rôto tuabin hướng trục cánh phẳng"),
                "Hình 28.31 · Giản đồ vectơ cho rôto tuabin hướng trục cánh phẳng. Hiệu giữa vectơ "
                "vận tốc tiếp tuyến lý tưởng (chỉ số i) và thực là vận tốc trượt của rôto, gây ra "
                "bởi tác động tổng hợp của các mômen cản; chính hiệu này tạo nên sai số tuyến tính "
                "và dòng xoáy ở cửa ra. V — vectơ vận tốc dòng tới; V<sub>E</sub> — vectơ vận tốc "
                "dòng ra; θ — góc xoáy ở cửa ra do mômen cản của rôto; β — góc nghiêng cánh, cũng "
                "là góc tới khi dòng song song; ω — vectơ vận tốc góc của rôto; r — vectơ bán kính "
                "rôto; F — lực cản do dòng chảy tác dụng lên mỗi mặt cánh; c — dây cung cánh; "
                "s — bước cánh dọc theo moay-ơ; c/s — hệ số đặc của rôto.",
                "Figure 28.31 · Vector diagram for a flat-bladed axial turbine rotor. The difference "
                "between the ideal (subscript i) and actual tangential velocity vectors is the rotor "
                "slip velocity, caused by the net effect of the rotor retarding torques; it gives "
                "rise to linearity errors and creates swirl in the exit flow. V — incident fluid "
                "velocity vector; V<sub>E</sub> — exit fluid velocity vector; θ — exit flow swirl "
                "angle due to rotor retarding torques; β — blade pitch angle, the same as the angle "
                "of attack for parallel flow; ω — rotor angular velocity vector; r — rotor radius "
                "vector; F — flow-induced drag force on each blade surface; c — blade chord; s — "
                "blade spacing along the hub; c/s — rotor solidity factor.",
                "Bên trái là dãy cánh nghiêng góc beta với dây cung c và bước s; bên phải là tam "
                "giác vectơ V, V-E và các thanh vận tốc tiếp tuyến",
                "On the left a blade row inclined at beta with chord c and spacing s; on the right "
                "the vector triangle of V, V-E and the tangential velocity bars")


def fig_28_32():
    o = [_defs()]
    x0, x1, yt, yb = 190, 640, 56, 196
    # tolerance band
    for y in (92, 112, 132):
        o.append(_line(x0, y, x1, y, S, 0.9, "5 4"))
    # axes
    o.append(_line(x0, yt - 8, x0, yb, E, 1.4))
    for y in (92, 112, 132):
        o.append(_line(x0 - 4, y, x0, y, E, 1.2))
    # calibration curve
    o.append(_path("M236,196 C248,160 254,110 270,94 C282,82 292,100 302,114 "
                   "C316,132 340,122 390,117 C460,110 550,113 632,112", E, 2.2))
    for x in (236, 632):
        o.append(_line(x, yb, x, 250, S, 0.9, "5 4"))
    # range annotation
    o.append(_darr(246, 216, 622, 216, G, 1.3))
    o.append(_lbl(434, 208, "Dải lưu lượng cho một độ nhớt", "ts", "middle"))
    # three alternative horizontal axes
    rows = ((258, "Lưu lượng, thể tích/thời gian", "đo 1, 2 hoặc 3 theo",
             [("Q", False), ("min", True)], [("Q", False), ("max", True)]),
            (306, "Số Reynolds (Re)", "đo 1, 2 hoặc 3 theo",
             [("vài × 10⁴", False)], [("vài × 10⁶", False)]),
            (354, "Tần số xung / độ nhớt động học, f/ν", "đo 1 (UVC) hoặc 3 theo", None, None))
    for y, lab, pre, t1, t2 in rows:
        o.append(_line(x0, y, x1, y, E, 1.3))
        o.append(_lbl((x0 + x1) / 2, y - 8, lab, "tb", "middle"))
        o.append(_lbl(x0 - 6, y + 4, pre, "ts", "end"))
        if t1:
            # NB: never put <sub> inside SVG text — the HTML parser breaks out
            # of the SVG context there and the rest of the figure collapses.
            o.append(_subs(236, y + 16, t1, "middle", "ts"))
            o.append(_subs(632, y + 16, t2, "middle", "ts"))
    # the three vertical-axis titles
    for x, lab, n in ((36, "Hệ số K, xung/thể tích", "1"), (62, "% Đăng ký", "2"),
                      (88, "Sai số tuyến tính, %", "3")):
        o.append('<text class="ts" x="%s" y="126" text-anchor="middle" '
                 'transform="rotate(-90 %s 126)">%s</text>' % (_f(x), _f(x), lab))
        o.append(_lbl(x, 204, n, "ts", "middle"))
    # tick labels for the two families of scales
    for y, a, b in ((92, "100 + x", "+x"), (112, "100", "0"), (132, "100 − x", "−x")):
        o.append(_lbl(164, y + 4, a, "ts", "end"))
        o.append(_lbl(104, y + 4, b, "ts", "end"))
    return _fig(svg(680, 378, "".join(o), "Đường cong hiệu chuẩn điển hình của tuabin hướng trục một rôto"),
                "Hình 28.32 · Đường cong sai số tuyến tính — tức đường cong hiệu chuẩn — điển hình "
                "của một tuabin hướng trục một rôto với chất lưu độ nhớt thấp, vẽ theo các cách "
                "trình bày thay thế đang dùng. Đặc tả độ chính xác cao thường ứng với dải lưu lượng "
                "10:1 tính từ Q<sub>max</sub> xuống, còn dải làm việc mở rộng thường ứng với độ "
                "chính xác thấp hơn. Chỗ gồ trên đường cong là đặc điểm do biên dạng vận tốc thay "
                "đổi khi Re tiến tới miền chảy tầng; độ lớn của nó khác nhau giữa các lưu lượng kế. "
                "Độ nhạy và độ lặp lại suy giảm ở Re thấp. Phần trăm đăng ký chỉ dùng cho lưu lượng "
                "kế có đầu thu cơ khí; mọi lưu lượng kế khác dùng hệ số K. Đường cong độ nhớt phổ "
                "dụng (UVC) và hiệu chuẩn theo Re vẫn đúng ở các độ nhớt môi chất đã biết khác, "
                "miễn là Re hay f/v còn trong dải đã đặc tả. Re tính theo đường kính ống nối và nhỏ "
                "hơn bên trong lưu lượng kế, nên dải Re trên hình chỉ là gần đúng và có thể lệch "
                "một bậc tuỳ lưu lượng kế. Sai số tuyến tính cũng có thể biểu diễn theo số Strouhal "
                "(fD/V) phụ thuộc Re (VD/ν) hoặc theo số Roshko (fD²/ν), khi đó D là đường kính "
                "chuẩn của lưu lượng kế [4]. – – –, ảnh hưởng của vành bao rôto trong một lưu lượng "
                "kế có bù độ nhớt.",
                "Figure 28.32 · A typical single-rotor axial turbine linearity error, or calibration, "
                "curve for a low-viscosity fluid, showing the main alternative presentations in "
                "current use. Higher accuracy specifications usually correspond to a 10:1 flow range "
                "down from Q<sub>max</sub>, while extended operating ranges correspond to reduced "
                "accuracies. The hump is a characteristic feature caused by flow velocity profile "
                "changes as Re approaches the laminar region, and varies in magnitude between meters. "
                "Sensitivity and repeatability degrade at low Re. Percent registration is used only "
                "with meters that have mechanical pickups; all others have a K factor. Universal "
                "viscosity curve (UVC) and Re calibrations remain in effect at different known media "
                "viscosities provided Re or f/v stays within the specified range. Re is referenced to "
                "the connecting conduit diameter and is less within the flowmeter, so the Re range "
                "shown is approximate and can vary by an order of magnitude. Linearity error can also "
                "be expressed as Strouhal number (fD/V) versus Re (VD/ν) or Roshko number (fD²/ν), "
                "when D is a flowmeter reference diameter [4]. – – –, effect of a rotor shroud in a "
                "viscosity-compensated flowmeter.",
                "Đường cong hiệu chuẩn có chỗ gồ nhô lên khỏi dải dung sai rồi phẳng dần; ba trục "
                "hoành thay thế phía dưới",
                "A calibration curve with a hump above the tolerance band then flattening; three "
                "alternative horizontal axes below")


def fig_28_33():
    o = [_defs()]
    # pipe wall the stem passes through
    o.append(_line(250, 96, 660, 96, S, 1.6, "8 5"))
    o.append(_lbl(256, 88, "thành ống", "ts"))
    # stem and fork
    o.append(_rect(392, 30, 16, 66, "#dce6f2", E, 1.6))
    o.append(_rect(300, 96, 220, 12, "#dce6f2", E, 1.6))
    o.append(_rect(300, 108, 12, 144, "#dce6f2", E, 1.6))
    o.append(_rect(508, 108, 12, 144, "#dce6f2", E, 1.6))
    o.append(_line(312, 180, 508, 180, E, 2.4))
    # the two rotors, counter-rotating
    for cx, ph in ((368, 0.35), (452, 0.35)):
        o += _blade_row(cx, 180, 34, 5, ph)
        o.append(_circ(cx, 180, 34, "none", E, 1.3))
    o.append('<path d="M336,140 A36,36 0 0 1 400,140" fill="none" stroke="%s" '
             'stroke-width="1.4" marker-end="url(#ah28)"/>' % G)
    o.append('<path d="M484,140 A36,36 0 0 0 420,140" fill="none" stroke="%s" '
             'stroke-width="1.4" marker-end="url(#ah28)"/>' % G)
    # sensors in the stem
    for y, n in ((44, 1), (66, 2)):
        o.append(_rect(396, y, 8, 13, "url(#hatch28)", E, 1.1))
        o.append(_lbl(414, y + 10, "cảm biến %d" % n, "ts"))
    # flow
    o.append(_arr(240, 180, 296, 180, S, "ah28s", 1.5))
    o.append(_lbl(240, 172, "dòng chảy", "ts"))
    return _fig(svg(680, 300, "".join(o), "Cụm rôto của lưu lượng kế tuabin hướng trục hai rôto kiểu chèn"),
                "Hình 28.33 · Cụm rôto của một lưu lượng kế tuabin hướng trục hai rôto kiểu chèn dùng "
                "đo lưu lượng nước. Thiết kế đã được cấp bằng sáng chế này làm cho lưu lượng kế "
                "không nhạy với sai số do dòng xoáy — một nguồn sai số quan trọng ở lưu lượng kế "
                "tuabin hướng trục một rôto. Chuyển động quay được cảm nhận bởi hai cảm biến trở "
                "kháng điện riêng biệt. (Theo Onicon Incorporated.)",
                "Figure 28.33 · The rotor assembly of a dual-rotor insertion axial turbine flowmeter "
                "for water flow measurement. This patented design renders the meter insensitive to "
                "errors due to flow swirl, an important source of potential error in single-rotor "
                "axial turbine flowmeters. The rotations are sensed by two separate electric "
                "impedance sensors. (Courtesy of Onicon Incorporated.)",
                "Cán chèn qua thành ống, hai rôto quay ngược chiều trên một trục chung trong khung chữ U",
                "A stem through the pipe wall with two counter-rotating rotors on a common axle in a "
                "U-shaped fork")


# ================================================================ 28.5 impeller

def fig_28_34():
    o = [_defs()]
    o.append(_lbl(40, 24, "(a)", "tb"))
    # ---- panel (a) left: body cross-section, chamber and six-blade rotor
    o.append(_rect(115, 60, 190, 190, WARM, E, 1.8, rx=4))
    o.append(_circ(210, 155, 68, P, E, 1.6))
    o += _blade_row(210, 155, 60, 6, 0.35, "#8fa3b8", 4)
    o.append(_circ(210, 155, 5, E, E, 1.0))
    # pickup port above the chamber
    o.append(_rect(238, 20, 14, 40, "#dce6f2", E, 1.4))
    o.append(_rect(232, 6, 26, 14, "#dce6f2", E, 1.4))
    o.append(_lbl(264, 16, "đầu thu", "ts"))
    # jet orifice cut into the left wall, labelled outside the body
    o.append(_rect(115, 127, 11, 14, "#dce6f2", E, 1.2))
    o.append(_line(96, 134, 113, 134, S, 0.9, "3 3"))
    o.append(_lbl(92, 128, "lỗ phun", "ts", "end"))
    o.append(_lbl(92, 141, "hoặc cửa vào", "ts", "end"))
    # circulating flow inside the chamber, label above the rotor
    o.append('<path d="M176,192 A58,58 0 0 1 152,96" fill="none" stroke="%s" '
             'stroke-width="1.3" marker-end="url(#ah28s)"/>' % S)
    o.append(_lbl(118, 82, "dòng tuần hoàn", "ts"))
    # section plane A–A' through the chamber axis
    o.append(_line(210, 16, 210, 300, S, 1.0, "7 3 2 3"))
    o.append(_lbl(210, 12, "A", "ts", "middle"))
    o.append(_lbl(210, 310, "A\u2032", "ts", "middle"))
    # flow in and out
    o.append(_arr(70, 190, 108, 190, S, "ah28s", 1.5))
    o.append(_arr(335, 190, 312, 190, S, "ah28s", 1.5))
    # ---- panel (a) right: the two rotor profiles on section A–A'
    for y0, kind in ((56, "flat"), (186, "t")):
        o.append(_rect(345, y0, 80, 96, FILL, E, 1.6))
        o.append(_line(345, y0 + 48, 425, y0 + 48, S, 0.9, "4 3"))
        o.append(_rect(350, y0 + 43, 70, 10, "#9aa4b2", E, 1.2))
        if kind == "flat":
            o.append(_rect(378, y0 + 22, 14, 21, "#dce6f2", E, 1.2))
            o.append(_rect(378, y0 + 53, 14, 21, "#dce6f2", E, 1.2))
        else:
            o.append(_rect(368, y0 + 22, 34, 8, "#dce6f2", E, 1.2))
            o.append(_rect(380, y0 + 30, 10, 13, "#dce6f2", E, 1.2))
            o.append(_rect(380, y0 + 53, 10, 13, "#dce6f2", E, 1.2))
            o.append(_rect(368, y0 + 66, 34, 8, "#dce6f2", E, 1.2))
        o.append(_lbl(334, y0 + 2, "A", "ts", "end"))
        o.append(_lbl(334, y0 + 100, "A\u2032", "ts", "end"))
    o.append(_lbl(438, 84, "kiểu prôfin", "tb"))
    o.append(_lbl(438, 98, "phẳng", "tb"))
    o.append(_lbl(438, 214, "kiểu prôfin", "tb"))
    o.append(_lbl(438, 228, "chữ T", "tb"))
    o.append(_line(430, 124, 418, 116, S, 0.9, "3 3"))
    o.append(_lbl(438, 128, "khe hở lớn", "ts"))
    # ---- panel (b): insertion rotors, straight and angled
    o.append(_lbl(40, 322, "(b)", "tb"))
    o.append(_line(60, 344, 420, 344, S, 1.4, "8 5"))
    o.append(_lbl(64, 336, "thành ống", "ts"))
    for cx, kind in ((150, "straight"), (330, "angled")):
        o.append(_rect(cx - 6, 344, 12, 40, "#dce6f2", E, 1.4))
        o.append(_circ(cx, 396, 24, "none", E, 1.2))
        for i in range(6):
            a = i * _m.pi / 3 + (0.5 if kind == "angled" else 0.0)
            dx, dy = 20 * _m.cos(a), 20 * _m.sin(a)
            if kind == "straight":
                o.append(_thick(cx, 396, cx + dx, 396 + dy, "#8fa3b8", 4))
            else:
                o.append(_thick(cx - dy * 0.5, 396 + dx * 0.5,
                                cx + dx * 0.85, 396 + dy * 0.85, "#8fa3b8", 4))
        o.append(_circ(cx, 396, 4, E, E, 1.0))
        o.append(_lbl(cx, 442, "thẳng" if kind == "straight" else "nghiêng", "tb", "middle"))
    o.append(_arr(72, 396, 108, 396, S, "ah28s", 1.4))
    o.append(_arr(252, 396, 288, 396, S, "ah28s", 1.4))
    o.append(_lbl(72, 386, "dòng chảy", "ts"))
    o.append(_lbl(196, 378, "cán", "ts"))
    o.append(_line(192, 374, 158, 362, S, 0.9, "3 3"))
    o.append(_lbl(452, 400, "Số cánh điển hình = 6 hoặc 8", "ts"))
    return _fig(svg(680, 456, "".join(o), "Các kiểu rôto lưu lượng kế cánh guồng"),
                "Hình 28.34 · Các kiểu rôto của lưu lượng kế cánh guồng: (a) lưu lượng kế nối tiếp "
                "kiểu toàn phần — mặt cắt ngang thân (trái) và hai kiểu prôfin rôto theo mặt cắt "
                "A–A′ (phải); (b) lưu lượng kế kiểu chèn, với cánh thẳng và cánh nghiêng. Ở kiểu "
                "chèn, trục quay của cánh guồng vuông góc với dòng chảy — đây chính là điểm khác "
                "biệt so với lưu lượng kế tuabin, vốn có trục song song với dòng. Số cánh điển hình "
                "là 6 hoặc 8. (Theo David Wadlow.)",
                "Figure 28.34 · Impeller flowmeter rotor design variations: (a) in-line meters — body "
                "cross-section (left) and the two rotor profiles on section A–A′ (right); (b) "
                "insertion meters, with straight and angled blades. In the insertion type the "
                "impeller's rotary axis is transverse to the flow, which is what distinguishes it "
                "from the turbine meter. Typical number of blades is 6 or 8. (Courtesy of David "
                "Wadlow.)",
                "Hai pa-nen: mặt cắt thân lưu lượng kế nối tiếp với hai prôfin rôto, và hai kiểu "
                "cánh chèn thẳng và nghiêng",
                "Two panels: a body cross-section with two rotor profiles, and straight and angled "
                "insertion blades")


def fig_28_35():
    o = [_defs()]
    # pipe wall
    o.append(_rect(40, 210, 600, 14, "url(#hatch28)", E, 1.4))
    o.append(_lbl(46, 202, "thành ống", "ts"))
    # welded boss and fitting
    o.append(_path("M300,210 L300,176 L380,176 L380,210 Z", E, 1.6, FILL))
    o.append(_rect(312, 160, 56, 16, "#dce6f2", E, 1.5, rx=2))
    # threaded stem
    o.append(_rect(326, 60, 28, 100, "#dce6f2", E, 1.5))
    for i in range(6):
        y = 96 + i * 11
        o.append(_line(326, y, 354, y - 6, S, 0.8))
    # collar with flow arrow
    o.append(_rect(326, 66, 28, 22, P, E, 1.4))
    o.append(_arr(332, 77, 348, 77, G, "ah28g", 1.6))
    # top flange and rods
    o.append(_rect(302, 44, 76, 14, "#dce6f2", E, 1.5, rx=2))
    for x in (310, 366):
        o.append(_line(x, 30, x, 44, E, 2.2))
        o.append(_circ(x, 28, 3, E, E, 1.0))
    # cable lead and its label sit above the flange, clear of the two rods
    o.append(_line(340, 44, 340, 22, E, 2.2))
    o.append(_lbl(340, 14, "cáp tín hiệu", "ts", "middle"))
    # impeller inside the pipe
    o.append(_rect(326, 224, 28, 30, "#dce6f2", E, 1.4))
    o += _blade_row(340, 272, 30, 6, 0.5)
    o.append(_circ(340, 272, 30, "none", E, 1.2))
    # flow
    o.append(_arr(60, 272, 104, 272, S, "ah28s", 1.6))
    o.append(_arr(580, 272, 536, 272, S, "ah28s", 1.6))
    o.append(_lbl(62, 262, "dòng chảy", "ts"))
    # callout labels
    o.append(_line(354, 108, 392, 100, S, 0.9, "3 3"))
    o.append(_lbl(396, 98, "ren", "ts"))
    o.append(_line(368, 168, 400, 162, S, 0.9, "3 3"))
    o.append(_lbl(404, 160, "đai ốc", "ts"))
    o.append(_line(356, 78, 400, 70, S, 0.9, "3 3"))
    o.append(_lbl(404, 68, "mũi tên chỉ chiều dòng", "ts"))
    o.append(_line(370, 272, 408, 268, S, 0.9, "3 3"))
    o.append(_lbl(412, 266, "cánh guồng", "ts"))
    o.append(_line(300, 194, 268, 190, S, 0.9, "3 3"))
    o.append(_lbl(264, 188, "đế hàn", "ts", "end"))
    return _fig(svg(680, 322, "".join(o), "Cảm biến cánh guồng kiểu chèn"),
                "Hình 28.35 · Một cảm biến cánh guồng kiểu chèn điển hình. Cảm biến được lắp vào một "
                "lỗ trên thành ống qua đế hàn hoặc bộ nối kẹp; phần thân ren cho phép điều chỉnh độ "
                "sâu chèn, và mũi tên trên thân cho biết chiều dòng chảy. Cánh guồng nằm ở đầu dưới "
                "của cán chèn, quay quanh một trục vuông góc với dòng. Các kiểu “hot tap” cho phép "
                "lắp vào đường ống đang vận hành mà gần như không mất chất lưu.",
                "Figure 28.35 · A typical insertion type impeller flow sensor. The sensor enters the "
                "pipe through a welded boss or clamp-on fitting; the threaded body sets the insertion "
                "depth and the arrow on the body shows the flow direction. The impeller sits at the "
                "bottom of the stem and rotates about an axis transverse to the flow. “Hot tap” "
                "versions allow installation into a live pipeline with little or no loss of fluid.",
                "Cảm biến chèn qua thành ống với thân ren, đai ốc, mũi tên chiều dòng và cánh guồng ở đầu dưới",
                "An insertion sensor through the pipe wall with threaded body, hex nut, flow arrow and "
                "impeller at the bottom")


# ================================================================ 28.6 electromagnetic

def fig_28_36():
    o = [_defs()]
    # ---- the flow tube, drawn as a vertical cylinder
    o.append(_ell(340, 96, 96, 26, FILL, E, 1.5))
    o.append(_line(244, 96, 244, 292, E, 1.5))
    o.append(_line(436, 96, 436, 292, E, 1.5))
    o.append(_path("M244,292 A96,26 0 0 0 436,292", E, 1.5))
    o.append(_path("M244,292 A96,26 0 0 1 436,292", E, 1.0, "none", "5 4"))
    # flow entering from below
    o.append(_arr(340, 384, 340, 306, S, "ah28s", 1.6))
    o.append(_lbl(350, 378, "dòng chảy", "ts"))
    # axes through the centre of the tube
    o.append(_arr(340, 300, 340, 44, E, "ah28", 1.4))
    o.append(_lbl(348, 42, "Z", "tb"))
    o.append(_arr(340, 194, 486, 250, E, "ah28", 1.4))
    o.append(_lbl(492, 258, "X", "tb"))
    o.append(_arr(340, 194, 194, 250, E, "ah28", 1.4))
    o.append(_lbl(176, 258, "Y", "tb"))
    # the electrode pair, a virtual conductor across the tube
    o.append(_line(250, 236, 430, 152, S, 1.0, "4 3"))
    o.append(_circ(250, 236, 5, E, E, 1.2))
    o.append(_circ(430, 152, 5, E, E, 1.2))
    o.append(_lbl(238, 250, "S₁", "tb", "end"))
    o.append(_lbl(442, 148, "S₂", "tb"))
    o.append(_line(430, 138, 462, 108, S, 0.9, "3 3"))
    o.append(_lbl(466, 104, "cảm biến", "ts"))
    # magnetic field along Y
    o.append(_arr(392, 214, 330, 240, G, "ah28g", 1.5))
    o.append(_lbl(396, 226, "từ trường B", "ts"))
    return _fig(svg(680, 412, "".join(o), "Nguyên lý làm việc của lưu lượng kế điện từ"),
                "Hình 28.36 · Nguyên lý làm việc của lưu lượng kế điện từ. Định luật Faraday phát biểu "
                "rằng một điện áp được cảm ứng trong một vật dẫn chuyển động trong từ trường. Ở lưu "
                "lượng kế điện từ, chiều chuyển động của vật dẫn, từ trường và suất điện động cảm ứng "
                "vuông góc với nhau theo các trục x, y và z. Hai cảm biến S₁ và S₂ “nhìn thấy” một vật "
                "dẫn ảo chính là chất lưu trong ống.",
                "Figure 28.36 · Operational principle of electromagnetic flowmeters. Faraday's law "
                "states that a voltage is induced in a conductor moving in a magnetic field. In "
                "electromagnetic flowmeters, the direction of movement of the conductor, the magnetic "
                "field, and the induced emf are perpendicular to each other on x, y and z axes. "
                "Sensors S₁ and S₂ experience a virtual conductor due to liquid in the pipe.",
                "Ống trụ thẳng đứng có dòng chảy đi lên, ba trục toạ độ và hai điện cực S1, S2 đặt đối diện nhau",
                "A vertical flow tube with flow rising through it, three coordinate axes and two "
                "electrodes S1 and S2 on opposite walls")


def fig_28_37():
    o = [_defs()]
    # ---- flanges
    o.append(_ell(340, 84, 118, 24, FILL, E, 1.5))
    o.append(_ell(340, 336, 118, 24, FILL, E, 1.5))
    for a in range(8):
        ang = a * _m.pi / 4
        o.append(_circ(340 + 100 * _m.cos(ang), 84 + 20 * _m.sin(ang), 3, P, E, 1.0))
        o.append(_circ(340 + 100 * _m.cos(ang), 336 + 20 * _m.sin(ang), 3, P, E, 1.0))
    # ---- flow channel
    o.append(_rect(268, 84, 144, 252, P, E, 1.4))
    # ---- coils and laminated cores, mirrored about the bore axis
    for x in (196, 450):
        o.append(_rect(x, 116, 34, 190, "#dce6f2", E, 1.5, rx=6))
        for k in range(9):
            o.append(_line(x + 4, 130 + k * 20, x + 30, 130 + k * 20, S, 0.8))
    for x in (176, 488):
        o.append(_rect(x, 110, 16, 202, FILL, E, 1.5))
    # ---- flux across the bore
    for y in (176, 196, 216):
        o.append(_arr(238, y, 444, y, G, "ah28g", 1.3))
    o.append(_lbl(300, 168, "từ thông", "ts"))
    # ---- electrodes
    o.append(_rect(262, 190, 12, 12, P, E, 1.4))
    o.append(_rect(406, 190, 12, 12, P, E, 1.4))
    o.append(_line(274, 192, 286, 150, S, 0.9, "3 3"))
    o.append(_lbl(290, 146, "điện cực", "ts"))
    # ---- diameter dimension
    o.append(_darr(268, 292, 412, 292, E))
    o.append(_lbl(340, 286, "đường kính D", "ts", "middle"))
    # ---- callouts
    o.append(_line(286, 84, 248, 56, S, 0.9, "3 3"))
    o.append(_lbl(244, 52, "kênh dòng chảy", "ts", "end"))
    o.append(_line(470, 150, 512, 140, S, 0.9, "3 3"))
    o.append(_lbl(516, 138, "cuộn dây", "ts"))
    o.append(_lbl(516, 152, "nam châm", "ts"))
    o.append(_line(486, 240, 522, 232, S, 0.9, "3 3"))
    o.append(_lbl(526, 230, "lõi ghép", "ts"))
    o.append(_lbl(526, 244, "lá thép", "ts"))
    o.append(_line(430, 336, 486, 344, S, 0.9, "3 3"))
    o.append(_lbl(490, 348, "mặt bích", "ts"))
    o.append(_lbl(340, 76, "V", "tb", "middle"))
    return _fig(svg(680, 380, "".join(o), "Kết cấu của một lưu lượng kế điện từ thực tế"),
                "Hình 28.37 · Kết cấu của lưu lượng kế điện từ thực tế. Nam châm điện đặt bên ngoài tạo "
                "ra một từ trường đều xuyên qua ống và chất lưu bên trong. Các cảm biến được đặt lệch "
                "90° so với từ trường và so với chiều dòng chảy, và được cách điện với thành ống. Mặt "
                "bích dùng để bắt lưu lượng kế vào đường ống bên ngoài. Nhà chế tạo thường cung cấp "
                "thông tin về chiều dài tối thiểu của các đoạn ống thẳng phía trước và phía sau.",
                "Figure 28.37 · Construction of practical flowmeters. External electromagnets create a "
                "homogeneous magnetic field that passes through the pipe and the liquid inside. "
                "Sensors are located 90° to the magnetic field and the direction of the flow. Sensors "
                "are insulated from the pipe walls. Flanges are provided for fixing the flowmeter to "
                "external pipes. Usually, manufacturers supply information about the minimum lengths "
                "of the straight portions of external pipes.",
                "Mặt cắt ống có hai mặt bích, hai cuộn dây nam châm điện hai bên và cặp điện cực trên thành ống",
                "A pipe section with two flanges, two electromagnet coils either side and a pair of "
                "electrodes in the wall")


def fig_28_38():
    o = [_defs()]
    x0, x1, y0, y1 = 178, 566, 80, 440
    lo, hi = _m.log10(0.01), _m.log10(10000.0)

    def yq(q):
        return y1 - (_m.log10(q) - lo) / (hi - lo) * (y1 - y0)

    def xr(r):
        return x0 + (r - 0.01) / 0.99 * (x1 - x0)

    o.append(_rect(x0, y0, x1 - x0, y1 - y0, P, E, 1.4))
    # one gridline and one label per 1-2-5 step; a 5-7 pair would collide
    ticks = []
    for dec in range(-2, 5):
        for m in (1, 2, 5):
            q = m * 10.0 ** dec
            if 0.01 <= q <= 10000:
                ticks.append(q)
    for q in ticks:
        yy = yq(q)
        o.append(_line(x0, yy, x1, yy, "#cfcfcf", 1.0))
        o.append(_lbl(x0 - 7, yy + 3, "%g" % q, "ts", "end"))
    # meter-size lines: Q = A v, with v = 10 m/s at 100 % of range
    for d in (2.5, 4, 6, 10, 15, 25, 40, 50, 80, 100):
        a = _m.pi * (d / 2000.0) ** 2
        q100 = a * 10.0 * 60000.0
        o.append(_line(xr(0.01), yq(q100 / 100.0), xr(1.0), yq(q100), E, 1.3))
        xm, ym = xr(0.58), yq(q100 * 0.58)
        o.append(_rect(xm - 16, ym - 8, 32, 12, P, P, 0))
        o.append(_lbl(xm, ym + 2, "%g" % d, "ts", "middle"))
    # axis titles
    o.append(_lbl(172, 56, "lưu lượng", "ts", "end"))
    o.append(_lbl(172, 68, "(lít/phút)", "ts", "end"))
    o.append(_lbl(372, 52, "cỡ đồng hồ (mm)", "ts", "middle"))
    for xv, t in ((x0, "1 %"), (372, "50 %"), (x1, "100 %")):
        o.append(_line(xv, y1, xv, y1 + 6, E, 1.2))
        o.append(_lbl(xv, y1 + 18, t, "ts", "middle"))
    o.append(_lbl(372, y1 + 36, "dải đo", "ts", "middle"))
    # annotation, kept clear of the plot frame
    o.append(_rect(x0, y1 + 48, x1 - x0, 34, P, E, 1.0))
    o.append(_lbl(x0 + 10, y1 + 62, "có thể chọn bất kỳ dải làm việc 10:1 nào", "ts"))
    o.append(_lbl(x0 + 10, y1 + 75, "(trong giới hạn của đồng hồ)", "ts"))
    return _fig(svg(680, 530, "".join(o), "Biểu đồ chọn cỡ lưu lượng kế điện từ"),
                "Hình 28.38 · Chọn cỡ lưu lượng kế. Khi chọn một lưu lượng kế phù hợp cho một ứng dụng "
                "cụ thể, phải hết sức chú ý tới vận tốc chất lưu dự kiến: vận tốc phải nằm trong dải "
                "tuyến tính của thiết bị. Ví dụ, một lưu lượng kế đường kính trong 100 mm xử lý được "
                "lưu lượng từ 50 L/phút đến 4000 L/phút; chế độ làm việc tối ưu đạt được ở khoảng "
                "500 L/phút.",
                "Figure 28.38 · Selection of flowmeters. In the selection of a suitable flowmeter for a "
                "particular application, care must be exercised in handling the anticipated liquid "
                "velocities. The velocity of liquid must be within the linear range of the device. For "
                "example, a flowmeter with 100 mm internal diameter can handle flows between 50 L "
                "min⁻¹ and 4000 L min⁻¹. An optimum operation will be achieved at a flow rate of "
                "500 L min⁻¹.",
                "Biểu đồ logarit hai trục: lưu lượng theo dải đo, với mười đường chéo ứng với mười cỡ đồng hồ",
                "A log-log selection chart of flow rate against range, with ten diagonal lines, one "
                "per meter size")


def fig_28_39():
    o = [_defs()]
    o.append(_arr(150, 250, 150, 74, E, "ah28", 1.4))
    o.append(_arr(150, 250, 610, 250, E, "ah28", 1.4))
    o.append(_lbl(156, 72, "điện áp e", "ts"))
    o.append(_lbl(604, 264, "t", "tb"))
    # noise floor
    o.append(_line(150, 196, 600, 196, S, 0.9, "6 4"))
    o.append(_lbl(556, 190, "nhiễu", "ts"))
    # the sampled waveform: noise only, flow+noise, noise only, flow
    d = ("M156,196 L206,196 C216,196 216,120 232,120 L292,120 "
         "C306,120 306,196 320,196 L370,196 "
         "C380,196 380,148 396,148 L458,148 C472,148 472,196 486,196 L600,196")
    o.append(_path(d, E, 1.6))
    # the two signal spans
    o.append(_darr(262, 120, 262, 196, E))
    o.append(_lbl(268, 152, "tín hiệu dòng", "ts"))
    o.append(_lbl(268, 166, "+ nhiễu", "ts"))
    o.append(_darr(430, 148, 430, 196, E))
    o.append(_lbl(436, 166, "tín hiệu", "ts"))
    o.append(_lbl(436, 180, "dòng", "ts"))
    # sample instants and the magnet periods
    for x in (196, 292, 340, 458):
        o.append(_line(x, 196, x, 288, S, 0.9))
        o.append(_arr(x - 10, 268, x - 2, 262, S, "ah28s", 1.0))
        o.append(_lbl(x - 14, 282, "lấy mẫu", "ts", "end"))
    for a, b, t in ((150, 292, "nam châm BẬT"), (292, 396, "nam châm TẮT"),
                    (396, 600, "nam châm BẬT")):
        o.append(_line(a, 304, b, 304, E, 1.2))
        o.append(_line(a, 298, a, 310, E, 1.2))
        o.append(_line(b, 298, b, 310, E, 1.2))
        o.append(_lbl((a + b) / 2, 322, t, "ts", "middle"))
    return _fig(svg(680, 336, "".join(o), "Dạng sóng của lưu lượng kế điện từ một chiều xung"),
                "Hình 28.39 · Tín hiệu quan sát tại các điện cực là tổng của điện áp cảm ứng và nhiễu. "
                "Khi ngắt dòng điện trong cuộn dây nam châm, tín hiệu trên các điện cực chỉ còn là "
                "nhiễu. Lấy số đo khi không có dòng qua nam châm trừ đi số đo khi có dòng qua nam "
                "châm sẽ khử được ảnh hưởng của nhiễu một cách hiệu quả.",
                "Figure 28.39 · The signals observed at the electrodes represent the sum of the induced "
                "voltage and the noise. When the current in the magnetic coils is turned off, the "
                "signal across the electrodes represents only the noise. Subtracting the measurement "
                "of the flowmeter when no current flows through the magnet from the measurement when "
                "current flows through the magnet effectively cancels out the effect of noise.",
                "Giản đồ thời gian: mức nhiễu nằm ngang, hai xung tín hiệu dòng, các mốc lấy mẫu và chu kỳ nam châm bật tắt",
                "A timing diagram: a noise floor with two flow-signal pulses, sample instants and the "
                "magnet on/off periods")


def fig_28_40():
    o = [_defs()]
    cx, cy, r = 320, 196, 96
    o.append(_circ(cx, cy, r, "#3a3a3a", E, 1.6))
    # air pocket at the top of the pipe
    dy = 60.0
    hw = _m.sqrt(r * r - dy * dy)
    wave = []
    for k in range(17):
        x = cx + hw - k * (2 * hw / 16)
        y = cy - dy + 3.2 * _m.sin(k * 1.35)
        wave.append("%s,%s" % (_f(x), _f(y)))
    o.append(_path("M%s,%s A%s,%s 0 0 1 %s,%s L%s Z"
                   % (_f(cx - hw), _f(cy - dy), _f(r), _f(r), _f(cx + hw), _f(cy - dy),
                      " L".join(wave)), E, 1.3, P))
    # bubbles
    for bx, by, br in ((cx - 52, cy - 78, 6), (cx - 22, cy - 84, 4), (cx + 8, cy - 79, 5),
                       (cx + 40, cy - 86, 4), (cx + 62, cy - 76, 5)):
        o.append(_circ(bx, by, br, P, E, 1.1))
    # electrodes, top and bottom — the top one is in the air pocket
    o.append(_rect(cx - 7, cy - r - 4, 14, 12, P, E, 1.4))
    o.append(_rect(cx - 7, cy + r - 8, 14, 12, P, E, 1.4))
    o.append(_line(cx - 8, cy - r - 2, cx - 62, cy - r - 20, S, 0.9, "3 3"))
    o.append(_lbl(cx - 66, cy - r - 24, "điện cực 1", "ts", "end"))
    o.append(_line(cx - 8, cy + r - 2, cx - 62, cy + r + 18, S, 0.9, "3 3"))
    o.append(_lbl(cx - 66, cy + r + 26, "điện cực 2", "ts", "end"))
    o.append(_line(cx + 30, cy - 88, cx + 92, cy - 104, S, 0.9, "3 3"))
    o.append(_lbl(cx + 96, cy - 108, "bọt khí", "ts"))
    return _fig(svg(680, 400, "".join(o), "Ống không đầy chất lưu trong lưu lượng kế điện từ"),
                "Hình 28.40 · Ống của lưu lượng kế điện từ phải luôn đầy chất lưu thì phép đo mới chính "
                "xác. Nếu chất lưu không tiếp xúc đầy đủ với các điện cực, trở kháng cao sẽ chặn dòng "
                "điện nên không thể đo được. Ngoài ra, nếu ống không đầy, thì dù chất lưu vẫn tiếp xúc "
                "với điện cực, phần rỗng của ống cũng làm cho lưu lượng tính ra bị sai.",
                "Figure 28.40 · The pipes of electromagnetic flowmeters must be full of liquid at all "
                "times for accurate measurement. If the liquid does not make full contact with "
                "electrodes, the high impedance prevents the current flow; hence, measurements cannot "
                "be taken. Also, if the pipe is not full, even if contact is maintained between the "
                "liquid and electrodes, the empty portions of the pipe will lead to miscalculated flow "
                "rates.",
                "Mặt cắt ống chứa đầy chất lưu nhưng có túi khí ở phía trên, điện cực 1 nằm trong túi khí",
                "A pipe cross-section full of liquid but with an air pocket at the top, electrode 1 "
                "sitting inside the pocket")


def fig_28_41():
    o = [_defs()]
    ax, ay = 330, 292
    o.append(_arr(ax, ay, ax, 62, E, "ah28", 1.4))
    o.append(_arr(110, ay, 600, ay, E, "ah28", 1.4))
    o.append(_lbl(ax + 8, 60, "Y", "tb"))
    o.append(_lbl(608, ay + 4, "X", "tb"))
    # ideal profile: a tall parabola
    o.append(_path("M156,292 C196,120 244,84 330,84 C416,84 464,120 504,292", E, 1.7))
    # edge effect: steep at the walls, flat across the middle
    o.append(_path("M156,292 C168,150 196,116 244,116 L416,116 C464,116 492,150 504,292",
                   G, 1.5))
    # field effect: a lower parabola
    o.append(_path("M176,292 C216,176 254,150 330,150 C406,150 444,176 484,292", BLUE, 1.5))
    o.append(_line(156, 292, 156, 84, S, 0.8, "3 3"))
    o.append(_line(504, 292, 504, 84, S, 0.8, "3 3"))
    # callouts
    o.append(_line(340, 84, 372, 74, S, 0.9, "3 3"))
    o.append(_lbl(376, 72, "prôfin vận tốc lý tưởng", "ts"))
    o.append(_line(430, 116, 470, 100, S, 0.9, "3 3"))
    o.append(_lbl(474, 98, "hiệu ứng biên", "ts"))
    o.append(_line(300, 152, 262, 176, S, 0.9, "3 3"))
    o.append(_lbl(258, 180, "hiệu ứng", "ts", "end"))
    o.append(_lbl(258, 194, "từ trường", "ts", "end"))
    return _fig(svg(680, 312, "".join(o), "Prôfin vận tốc trong ống của lưu lượng kế điện từ"),
                "Hình 28.41 · Prôfin dòng chảy trong ống. Lưu lượng kế điện từ thể hiện một mức độ nhạy "
                "nhất định với prôfin dòng. Prôfin vận tốc lý tưởng có thể bị méo do hiệu ứng biên và "
                "do hiệu ứng từ trường, gọi là thuỷ động lực từ. Ở một số ứng dụng, nhiễu loạn vận tốc "
                "do hiệu ứng thuỷ động lực từ có thể đủ lớn để ảnh hưởng nghiêm trọng tới độ chính xác.",
                "Figure 28.41 · Flow profiles in the pipes. Magnetic flowmeters demonstrate a certain "
                "degree of sensitivity to flow profiles. The ideal velocity profile can be distorted "
                "due to edge effects and also field effects known as magneto-hydrodynamics. In some "
                "applications, the velocity perturbation due to the magnetohydrodynamic effect can be "
                "serious enough to severely influence the accuracy of operations.",
                "Ba đường cong prôfin vận tốc trên hệ trục: lý tưởng, hiệu ứng biên và hiệu ứng từ trường",
                "Three velocity-profile curves on a pair of axes: ideal, edge effect and field effect")


def fig_28_42():
    o = [_defs()]
    # ---- pipe and flanges
    o.append(_rect(52, 196, 116, 34, FILL, E, 1.5))
    o.append(_rect(512, 196, 116, 34, FILL, E, 1.5))
    for x in (168, 512):
        o.append(_rect(x - 10, 180, 20, 66, "#dce6f2", E, 1.5))
    # ---- meter body
    o.append(_rect(178, 158, 324, 110, WARM, E, 1.7, rx=4))
    o.append(_rect(216, 108, 248, 52, "#dce6f2", E, 1.6, rx=3))
    o.append(_rect(292, 118, 96, 30, P, E, 1.3))
    # ---- bore through the body, and the liner
    o.append(_rect(178, 200, 324, 26, P, E, 1.2))
    o.append(_line(178, 200, 502, 200, BLUE, 2.4))
    o.append(_line(178, 226, 502, 226, BLUE, 2.4))
    # ---- electrodes on top of the body
    for x in (262, 418):
        o.append(_rect(x - 6, 148, 12, 12, P, E, 1.3))
        o.append(_line(x, 148, x, 160, E, 1.2))
    # ---- ground straps: a short loop from the body top to each flange
    o.append(_path("M202,158 Q170,150 172,204", E, 2.4))
    o.append(_path("M478,158 Q510,150 508,204", E, 2.4))
    # ---- ground wire up to the earth symbol
    o.append(_path("M340,108 C340,80 372,72 392,64", E, 2.0))
    o.append(_line(392, 64, 470, 44, E, 2.0))
    for k, w in enumerate((30, 20, 12, 6)):
        o.append(_line(452 - w, 44 + k * 7, 452 + w, 44 + k * 7, E, 1.6))
    o.append(_lbl(486, 40, "về đất tốt", "ts"))
    # ---- labels
    o.append(_line(168, 176, 120, 152, S, 0.9, "3 3"))
    o.append(_lbl(116, 148, "dây nối đất", "ts", "end"))
    o.append(_lbl(116, 162, "(strap)", "ts", "end"))
    o.append(_line(470, 213, 540, 246, S, 0.9, "3 3"))
    o.append(_lbl(544, 250, "lớp lót ống", "ts"))
    o.append(_arr(60, 213, 104, 213, S, "ah28s", 1.6))
    o.append(_lbl(60, 250, "dòng chảy", "ts"))
    o.append(_lbl(262, 142, "điện cực", "ts", "middle"))
    return _fig(svg(680, 300, "".join(o), "Nối đất cho lưu lượng kế điện từ"),
                "Hình 28.42 · Nối đất cho lưu lượng kế điện từ. Nối đất tốt là điều kiện tuyệt đối cần "
                "thiết để cách ly nhiễu và điện thế đồng pha cao. Nếu ống dẫn điện và tiếp xúc với chất "
                "lưu thì phải nối đất lưu lượng kế vào chính ống. Nếu ống làm bằng vật liệu không dẫn "
                "điện thì phải lắp các vòng nối đất để duy trì tiếp xúc với chất lưu. Nối đất không đúng "
                "sẽ đặt lưu lượng kế dưới điện thế đồng pha quá lớn, làm giảm nghiêm trọng độ chính xác "
                "và có thể làm hỏng phần điện tử.",
                "Figure 28.42 · Grounding of electromagnetic flowmeters. A good grounding is absolutely "
                "essential to isolate noise and high common mode potential. If the pipe is conductive "
                "and makes contact with the liquid, the flowmeter should be grounded to the pipe. If "
                "the pipe is made from nonconductive materials, ground rings should be installed to "
                "maintain contact with the process liquid. Improper grounding results in excessive "
                "common mode voltages that can severely limit the accuracy and also damage the "
                "processing electronics.",
                "Thân lưu lượng kế giữa hai mặt bích, hai dây nối đất và dây dẫn về cọc tiếp địa",
                "A meter body between two flanges, with two ground straps and a lead to an earth "
                "symbol")


FIGS = [fig_28_1(), fig_28_2(), fig_28_3(), fig_28_4(), fig_28_5(), fig_28_6(),
        fig_28_7(), fig_28_8(), fig_28_9(), fig_28_10(), fig_28_11(), fig_28_12(),
        fig_28_13(), fig_28_14(), fig_28_15(), fig_28_16(), fig_28_17(), fig_28_18(),
        fig_28_19(), fig_28_20(), fig_28_21(), fig_28_22(), fig_28_23(),
        fig_28_24(), fig_28_25(), fig_28_26(), fig_28_27(), fig_28_28(),
        fig_28_29(), fig_28_30(), fig_28_31(), fig_28_32(),
        fig_28_33(), fig_28_34(), fig_28_35(),
        fig_28_36(), fig_28_37(), fig_28_38(), fig_28_39(), fig_28_40(),
        fig_28_41(), fig_28_42()]


def fig(n):
    return FIGS[n - 1]
