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


FIGS = [fig_28_1(), fig_28_2(), fig_28_3(), fig_28_4(), fig_28_5(), fig_28_6(),
        fig_28_7(), fig_28_8(), fig_28_9(), fig_28_10(), fig_28_11(), fig_28_12(),
        fig_28_13(), fig_28_14(), fig_28_15(), fig_28_16(), fig_28_17(), fig_28_18(),
        fig_28_19(), fig_28_20()]


def fig(n):
    return FIGS[n - 1]
