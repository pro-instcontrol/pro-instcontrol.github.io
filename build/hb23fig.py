# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 23 — Force Measurement
(M. A. Elbestawi, McMaster University).

The source chapter contains exactly seventeen figures (23.1–23.17).
FIGS is a 17-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _subs(x, y, parts, anchor="start", cls="t"):
    """Text with real subscripts: parts is [(txt, is_subscript), ...].

    Unicode subscript *letters* (ᵢ, ₛ, ᵣ) are missing from the sans-serif
    stack, so they render as blanks; a tspan with an explicit dy is used
    instead.  The dy is undone on the following normal run.
    """
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
            '<marker id="ah23" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah23g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah23", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=5):
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


def _dim(x1, y1, x2, y2, col=S):
    """Dimension line with end ticks."""
    o = [_line(x1, y1, x2, y2, col, 1.0)]
    if abs(y2 - y1) < 0.5:
        o.append(_line(x1, y1 - 4, x1, y1 + 4, col, 1.0))
        o.append(_line(x2, y2 - 4, x2, y2 + 4, col, 1.0))
    else:
        o.append(_line(x1 - 4, y1, x1 + 4, y1, col, 1.0))
        o.append(_line(x2 - 4, y2, x2 + 4, y2, col, 1.0))
    return "".join(o)


def _poly(pts, fill=FILL, col=E, sw=1.5):
    d = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (d, fill, col, _f(sw)))


def _path(d, col=E, sw=1.4, fill="none", dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, col, _f(sw), ds))


def _grid_h(x, y, w, h, n=6, sw=2.2, col=E):
    """Serpentine horizontal gage grid."""
    dy = h / float(n - 1) if n > 1 else 0
    pts = []
    for i in range(n):
        yy = y + i * dy
        if i % 2 == 0:
            pts += [(x, yy), (x + w, yy)]
        else:
            pts += [(x + w, yy), (x, yy)]
    d = "M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linejoin="round" stroke-linecap="round"/>' % (d, col, _f(sw)))


# ---------------------------------------------------------------- 23.1
def fig_23_1():
    o = [_defs()]
    # (a) uniaxial tension
    o.append(_rect(72, 100, 100, 66, "#ffffff", S, 1.1, "5 4"))
    o.append(_rect(62, 110, 120, 46, FILL, E, 1.6))
    o.append(_arr(62, 122, 32, 122))
    o.append(_arr(182, 122, 212, 122))
    o.append(_lbl(34, 115, "p"))
    o.append(_lbl(204, 115, "p"))
    o.append(_arr(172, 133, 172, 116))
    o.append(_arr(172, 133, 172, 150))
    o.append(_lbl(166, 137, "Δt", "t", "end"))
    o.append(_dim(72, 180, 172, 180))
    o.append(_lbl(122, 196, "l₀", "t", "middle"))
    o.append(_lbl(122, 80, "(a) kéo một trục", "ts", "middle"))

    # (b) uniaxial compression
    o.append(_rect(290, 100, 100, 66, "#ffffff", S, 1.1, "5 4"))
    o.append(_rect(308, 96, 64, 74, FILL, E, 1.6))
    o.append(_arr(270, 122, 308, 122))
    o.append(_arr(410, 122, 372, 122))
    o.append(_lbl(270, 115, "p", "t", "end"))
    o.append(_lbl(412, 115, "p"))
    o.append(_arr(362, 133, 362, 106))
    o.append(_arr(362, 133, 362, 160))
    o.append(_lbl(356, 137, "Δt", "t", "end"))
    o.append(_dim(290, 180, 390, 180))
    o.append(_lbl(340, 196, "l₀", "t", "middle"))
    o.append(_lbl(340, 80, "(b) nén một trục", "ts", "middle"))

    # (c) simple shear
    o.append(_poly([(486, 168), (586, 168), (610, 104), (510, 104)], FILL, E, 1.6))
    o.append(_arr(556, 88, 600, 88))
    o.append(_lbl(604, 92, "F"))
    o.append(_arr(536, 184, 492, 184))
    o.append(_lbl(488, 188, "F", "t", "end"))
    o.append(_lbl(560, 126, "A₀", "t", "middle"))
    o.append(_path("M486,142 A26,26 0 0 1 495.5,143.6", S, 1.1))
    o.append(_lbl(496, 158, "γ"))
    o.append(_lbl(614, 128, "Δx"))
    o.append(_lbl(476, 128, "y", "t", "end"))
    o.append(_lbl(548, 80, "(c) trượt đơn", "ts", "middle"))

    return _fig(svg(680, 212, "".join(o),
                    "Ba cách đặt tải lên kim loại: kéo, nén và trượt"),
                "Hình 23.1 · Khi kim loại chịu kéo một trục (a), nén một trục (b) hoặc trượt đơn (c), "
                "nó biến dạng đàn hồi cho tới khi ứng suất pháp hoặc ứng suất tiếp đạt một giá trị tới hạn.",
                "Figure 23.1 · When a metal is loaded in uniaxial tension (a), uniaxial compression (b), "
                "or simple shear (c), it behaves elastically until a critical normal or shear stress "
                "is reached.",
                "Ba khối kim loại chịu kéo, nén và trượt với các mũi tên lực và kích thước",
                "Three metal blocks under tension, compression and shear with force arrows")


# ---------------------------------------------------------------- 23.2
def fig_23_2():
    o = [_defs()]
    # (a) tension
    o.append(_rect(70, 100, 80, 56, "#ffffff", S, 1.1, "5 4"))
    o.append(_rect(70, 106, 100, 44, FILL, E, 1.6))
    o.append(_dim(70, 172, 150, 172))
    o.append(_dim(150, 172, 170, 172))
    o.append(_lbl(106, 188, "l₀", "t", "middle"))
    o.append(_lbl(164, 188, "Δl", "t", "middle"))
    o.append(_lbl(122, 212, "S = p / A₀", "t", "middle"))
    o.append(_lbl(122, 230, "e = Δl / l₀", "t", "middle"))
    o.append(_lbl(122, 84, "(a)", "ts", "middle"))

    # (b) compression
    o.append(_rect(296, 100, 80, 56, "#ffffff", S, 1.1, "5 4"))
    o.append(_rect(308, 98, 56, 60, FILL, E, 1.6))
    o.append(_dim(296, 172, 376, 172))
    o.append(_dim(364, 172, 376, 172))
    o.append(_lbl(330, 188, "l₀", "t", "middle"))
    o.append(_lbl(372, 188, "Δl", "t", "middle"))
    o.append(_lbl(340, 212, "S = p / A₀", "t", "middle"))
    o.append(_lbl(340, 230, "e = Δl / l₀", "t", "middle"))
    o.append(_lbl(340, 84, "(b)", "ts", "middle"))

    # (c) shear
    o.append(_poly([(486, 156), (586, 156), (610, 100), (510, 100)], FILL, E, 1.6))
    o.append(_path("M486,132 A24,24 0 0 1 495.5,134", S, 1.1))
    o.append(_lbl(496, 148, "γ"))
    o.append(_lbl(614, 120, "Δx"))
    o.append(_lbl(476, 126, "y", "t", "end"))
    o.append(_lbl(548, 212, "τ = F / A₀", "t", "middle"))
    o.append(_lbl(548, 230, "γ = Δx / y", "t", "middle"))
    o.append(_lbl(548, 84, "(c)", "ts", "middle"))

    return _fig(svg(680, 244, "".join(o),
                    "Định nghĩa ứng suất và biến dạng đàn hồi cho kéo, nén và trượt"),
                "Hình 23.2 · Ứng suất và biến dạng đàn hồi cho: (a) kéo một trục; (b) nén một trục; "
                "(c) trượt đơn.",
                "Figure 23.2 · Elastic stress and strain for: (a) uniaxial tension; (b) uniaxial "
                "compression; (c) simple shear.",
                "Ba hình vẽ định nghĩa ứng suất và biến dạng kèm công thức",
                "Three diagrams defining stress and strain with formulas")


# ---------------------------------------------------------------- 23.3
def fig_23_3():
    o = [_defs()]
    # (a) thin diaphragm load cell
    o.append(_rect(32, 96, 160, 86, "#ffffff", E, 1.5))
    o.append(_rect(46, 114, 132, 54, WARM, S, 1.0))
    o.append(_rect(46, 104, 132, 9, FILL, E, 1.5))
    o.append(_arr(112, 58, 112, 100))
    o.append(_lbl(118, 64, "F"))
    o.append(_lbl(60, 140, "Kd"))
    o.append(_lbl(160, 132, "X", "t", "end"))
    o.append(_lbl(112, 204, "(a) màng mỏng", "ts", "middle"))

    # (b) hydraulic load cell
    o.append(_rect(270, 96, 150, 86, "#ffffff", E, 1.5))
    o.append(_rect(284, 112, 122, 56, WARM, S, 1.0))
    o.append(_rect(320, 84, 50, 14, FILL, E, 1.5))
    o.append(_arr(345, 56, 345, 80))
    o.append(_lbl(351, 62, "F"))
    o.append(_lbl(352, 108, "A", "t", "middle"))
    o.append('<circle cx="246" cy="132" r="15" fill="#ffffff" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_line(261, 132, 284, 132, E, 1.2))
    o.append(_line(246, 132, 254, 124, G, 1.3))
    o.append(_lbl(246, 158, "p", "t", "middle"))
    o.append(_lbl(345, 204, "(b) thủy lực", "ts", "middle"))

    # (c) pneumatic load cell
    o.append(_arr(470, 116, 500, 116))
    o.append(_subs(470, 108, [("P", False), ("s", True)]))
    o.append(_rect(500, 108, 10, 7, E, E, 1.0))
    o.append(_rect(500, 121, 10, 7, E, E, 1.0))
    o.append(_rect(514, 104, 92, 52, WARM, E, 1.4))
    o.append(_rect(556, 156, 8, 10, "#ffffff", E, 1.2))
    o.append(_rect(532, 168, 56, 6, FILL, E, 1.4))
    o.append(_rect(516, 174, 88, 7, FILL, E, 1.4))
    o.append(_arr(560, 208, 560, 182))
    o.append(_lbl(566, 202, "F"))
    o.append(_lbl(520, 196, "Kd"))
    o.append('<circle cx="632" cy="126" r="13" fill="#ffffff" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_line(606, 126, 619, 126, E, 1.2))
    o.append(_line(632, 126, 638, 118, G, 1.3))
    o.append(_subs(632, 110, [("P", False), ("0", True)], "middle"))
    o.append(_lbl(596, 152, "Fp", "t", "end"))
    o.append(_lbl(560, 84, "(c) khí nén", "ts", "middle"))

    return _fig(svg(680, 220, "".join(o),
                    "Ba loại load cell: màng mỏng, thủy lực và khí nén"),
                "Hình 23.3 · Các loại load cell khác nhau.",
                "Figure 23.3 · Different types of load cells.",
                "Ba sơ đồ load cell màng mỏng, thủy lực và khí nén",
                "Three load cell schematics: thin diaphragm, hydraulic and pneumatic")


# ---------------------------------------------------------------- 23.4
def fig_23_4():
    o = [_defs()]

    def panel(x0, grids, lab):
        o.append(_rect(x0, 88, 180, 96, "#ffffff", S, 1.2))
        y = 100
        for ang, n in grids:
            o.append(_grid_h(x0 + 14, y, 96, 18, n))
            ax, ay = x0 + 134, y + 9
            dx = 17 * _m.cos(_m.radians(ang))
            dy = -17 * _m.sin(_m.radians(ang))
            o.append(_arr(ax - dx / 2.0, ay - dy / 2.0, ax + dx / 2.0, ay + dy / 2.0))
            o.append(_lbl(x0 + 156, ay + 4, "%d°" % ang, "ts"))
            y += 30
        o.append(_lbl(x0 + 90, 200, lab, "ts", "middle"))

    panel(44, [(0, 5)], "(a) một phần tử")
    panel(250, [(0, 3), (90, 3)], "(b) hai phần tử")
    panel(456, [(0, 3), (45, 3), (90, 3)], "(c) ba phần tử")

    return _fig(svg(680, 212, "".join(o),
                    "Cấu hình gage điện trở lá kim loại: một, hai và ba phần tử"),
                "Hình 23.4 · Cấu hình của gage điện trở lá kim loại: (a) một phần tử; (b) hai phần tử; "
                "và (c) ba phần tử.",
                "Figure 23.4 · Configuration of metal-foil resistance strain gages: (a) single element; "
                "(b) two element; (c) three element.",
                "Ba kiểu lưới gage điện trở: một, hai và ba phần tử, kèm hướng đặt",
                "Three foil gage grid configurations: single, two and three element with orientation")


# ---------------------------------------------------------------- 23.5
def fig_23_5():
    o = [_defs()]
    T = (340, 52)
    B = (340, 216)
    L = (218, 134)
    R = (462, 134)
    # arms
    o.append(_line(T[0], T[1], L[0], L[1], E, 1.5))
    o.append(_line(L[0], L[1], B[0], B[1], E, 1.5))
    o.append(_line(T[0], T[1], R[0], R[1], E, 1.5))
    o.append(_line(R[0], R[1], B[0], B[1], E, 1.5))
    # resistor marks
    def res(p, q, lab, dx, dy):
        mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
        return _lbl(mx + dx, my + dy, lab, "tb", "middle")
    o.append(res(T, L, "R₁", -14, -4))
    o.append(res(T, R, "R₂", 14, -4))
    o.append(res(L, B, "R₃", -14, 8))
    o.append(res(R, B, "R₄", 14, 8))
    # nodes
    for pt in (T, B, L, R):
        o.append(_dot(pt[0], pt[1], 3.6))
    # source across top-bottom
    o.append(_line(340, 26, 340, 48, E, 1.3))
    o.append(_subs(348, 24, [("E", False), ("i", True)]))
    o.append(_line(340, 220, 340, 238, E, 1.3))
    # galvanometer across left-right
    o.append(_line(222, 134, 252, 134, E, 1.2))
    o.append(_line(428, 134, 458, 134, E, 1.2))
    o.append('<circle cx="340" cy="134" r="15" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(340, 139, "G", "tb", "middle"))
    o.append(_line(255, 134, 325, 134, E, 1.2, "4 4"))
    o.append(_line(355, 134, 425, 134, E, 1.2, "4 4"))
    o.append(_lbl(232, 126, "D", "tb", "middle"))
    o.append(_lbl(448, 126, "C", "tb", "middle"))

    return _fig(svg(680, 246, "".join(o), "Cầu Wheatstone bốn nhánh"),
                "Hình 23.5 · Cầu Wheatstone.",
                "Figure 23.5 · The Wheatstone bridge.",
                "Sơ đồ cầu Wheatstone với bốn điện trở, nguồn và điện kế",
                "Wheatstone bridge schematic with four resistors, source and galvanometer")


# ---------------------------------------------------------------- 23.6
def fig_23_6():
    o = [_defs()]
    # (a) cantilever beam
    o.append(_rect(96, 84, 20, 90, "#ffffff", E, 1.4))
    for i in range(6):
        yy = 88 + i * 15
        o.append(_line(96, yy, 86, yy + 10, S, 1.0))
    o.append(_rect(116, 110, 300, 26, FILL, E, 1.6))
    o.append(_arr(380, 78, 380, 106))
    o.append(_lbl(386, 84, "P"))
    o.append(_dim(116, 158, 380, 158))
    o.append(_lbl(248, 174, "x", "t", "middle"))
    o.append(_lbl(424, 124, "h", "t", "middle"))
    o.append(_lbl(250, 102, "b", "t", "middle"))
    # gages on top
    o.append(_rect(180, 106, 26, 5, G, G, 1.0))
    o.append(_rect(250, 106, 26, 5, G, G, 1.0))
    # gages on bottom
    o.append(_rect(180, 135, 26, 5, "#ffffff", E, 1.1))
    o.append(_rect(250, 135, 26, 5, "#ffffff", E, 1.1))
    o.append(_lbl(120, 96, "gage 1 và 3 (mặt trên)", "ts"))
    o.append(_lbl(120, 152, "gage 2 và 4 (mặt dưới)", "ts"))
    o.append(_lbl(248, 200, "(a) dầm công xôn với bốn gage", "ts", "middle"))

    # (b) bridge with gage positions
    T, B, L, R = (340, 246), (340, 330), (270, 288), (410, 288)
    o.append(_line(T[0], T[1], L[0], L[1], E, 1.4))
    o.append(_line(L[0], L[1], B[0], B[1], E, 1.4))
    o.append(_line(T[0], T[1], R[0], R[1], E, 1.4))
    o.append(_line(R[0], R[1], B[0], B[1], E, 1.4))
    o.append(_lbl(300, 262, "1", "tb", "middle"))
    o.append(_lbl(380, 262, "4", "tb", "middle"))
    o.append(_lbl(300, 318, "3", "tb", "middle"))
    o.append(_lbl(380, 318, "2", "tb", "middle"))
    for pt in (T, B, L, R):
        o.append(_dot(pt[0], pt[1], 3.4))
    o.append(_line(340, 228, 340, 242, E, 1.2))
    o.append(_subs(348, 226, [("E", False), ("i", True)]))
    o.append(_line(340, 334, 340, 348, E, 1.2))
    o.append(_line(274, 288, 300, 288, E, 1.1))
    o.append(_line(380, 288, 406, 288, E, 1.1))
    o.append(_subs(352, 302, [("E", False), ("0", True)], "middle", "tb"))
    o.append(_lbl(340, 368, "(b) vị trí gage trong cầu Wheatstone", "ts", "middle"))

    return _fig(svg(680, 380, "".join(o), "Load cell kiểu dầm và vị trí gage trong cầu"),
                "Hình 23.6 · Load cell kiểu dầm: (a) một số load cell kiểu dầm (phần tử đàn hồi có gage); "
                "và (b) vị trí gage trong cầu Wheatstone.",
                "Figure 23.6 · Beam-type load cells: (a) a selection of beam-type load cells (elastic "
                "element with strain gages); and (b) gage positions in the Wheatstone bridge.",
                "Dầm công xôn có bốn gage và sơ đồ cầu với vị trí các gage",
                "Cantilever beam with four gages and the bridge with gage positions")


# ---------------------------------------------------------------- 23.7
def fig_23_7():
    o = [_defs()]
    cx, cy = 118, 132
    ro, ri = 54, 40
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.6"/>'
             % (_f(cx), _f(cy), _f(ro), FILL, E))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
             % (_f(cx), _f(cy), _f(ri), E))
    o.append(_arr(cx, 56, cx, 76))
    o.append(_lbl(cx + 6, 62, "P"))
    o.append(_arr(cx, 208, cx, 188))
    o.append(_lbl(cx + 6, 202, "P"))
    o.append(_rect(cx - 8, cy - ro - 1, 16, 6, G, G, 1.0))
    o.append(_rect(cx - 8, cy + ro - 5, 16, 6, G, G, 1.0))
    o.append(_rect(cx - ri - 6, cy - 4, 6, 9, "#ffffff", E, 1.1))
    o.append(_rect(cx + ri, cy - 4, 6, 9, "#ffffff", E, 1.1))
    o.append(_dim(cx - ro, cy, cx + ro, cy))
    o.append(_lbl(cx, cy - 8, "D = 2R", "t", "middle"))
    o.append(_lbl(cx + 66, cy - 40, "gage 2", "ts"))
    o.append(_lbl(cx + 66, cy - 28, "ngoài", "ts"))
    o.append(_lbl(cx - 62, cy + 34, "gage 3", "ts", "end"))
    o.append(_lbl(cx - 62, cy + 46, "trong", "ts", "end"))
    o.append(_lbl(cx, 226, "(a) vòng đo với gage", "ts", "middle"))

    # (b) bridge
    T, B, L, R = (340, 76), (340, 176), (272, 126), (408, 126)
    o.append(_line(T[0], T[1], L[0], L[1], E, 1.4))
    o.append(_line(L[0], L[1], B[0], B[1], E, 1.4))
    o.append(_line(T[0], T[1], R[0], R[1], E, 1.4))
    o.append(_line(R[0], R[1], B[0], B[1], E, 1.4))
    o.append(_lbl(300, 96, "1", "tb", "middle"))
    o.append(_lbl(380, 96, "4", "tb", "middle"))
    o.append(_lbl(300, 164, "3", "tb", "middle"))
    o.append(_lbl(380, 164, "2", "tb", "middle"))
    for pt in (T, B, L, R):
        o.append(_dot(pt[0], pt[1], 3.4))
    o.append(_line(340, 60, 340, 72, E, 1.2))
    o.append(_subs(348, 58, [("E", False), ("i", True)]))
    o.append(_line(340, 180, 340, 194, E, 1.2))
    o.append(_line(276, 126, 300, 126, E, 1.1))
    o.append(_line(380, 126, 404, 126, E, 1.1))
    o.append(_subs(340, 130, [("E", False), ("0", True)], "middle", "tb"))
    o.append(_lbl(340, 214, "(b) vị trí gage trong cầu", "ts", "middle"))

    # (c) ring with LVDT
    cx2 = 556
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.6"/>'
             % (_f(cx2), _f(cy), _f(48), FILL, E))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
             % (_f(cx2), _f(cy), _f(35), E))
    o.append(_arr(cx2, 56, cx2, 78))
    o.append(_lbl(cx2 + 6, 62, "P"))
    o.append(_arr(cx2, 208, cx2, 186))
    o.append(_lbl(cx2 + 6, 202, "P"))
    o.append(_rect(cx2 - 7, cy - 26, 14, 52, WARM, E, 1.3))
    o.append(_lbl(cx2 + 12, cy - 4, "lõi", "ts"))
    o.append(_lbl(cx2 + 12, cy + 10, "LVDT", "ts"))
    o.append(_lbl(cx2, 226, "(c) vòng đo với LVDT", "ts", "middle"))

    return _fig(svg(680, 240, "".join(o), "Load cell kiểu vòng với gage và với LVDT"),
                "Hình 23.7 · Load cell kiểu vòng: (a) phần tử đàn hồi với cảm biến gage; (b) vị trí gage "
                "trong cầu Wheatstone; và (c) phần tử đàn hồi với cảm biến LVDT.",
                "Figure 23.7 · Ring-type load cells: (a) elastic element with strain-gage sensors; "
                "(b) gage positions in the Wheatstone bridge; and (c) elastic element with an LVDT sensor.",
                "Vòng đo có gage, sơ đồ cầu và vòng đo có LVDT",
                "Proving ring with gages, the bridge, and a proving ring with an LVDT")


# ---------------------------------------------------------------- 23.8
def fig_23_8():
    o = [_defs()]

    def plate(cx, y0, label, arrows, txt):
        o.append(_rect(cx - 54, y0, 108, 34, FILL, E, 1.5))
        for a in arrows:
            o.append(a)
        o.append(_lbl(cx, y0 + 22, "P", "ts", "middle"))
        o.append(_lbl(cx, y0 + 56, label, "ts", "middle"))
        o.append(_lbl(cx, y0 + 70, txt, "ts", "middle"))

    # (a) longitudinal / thickness mode
    plate(122, 84, "(a) d₃₃", [_arr(122, 56, 122, 80), _arr(122, 146, 122, 122)],
          "nén theo trục phân cực")
    # (b) transverse mode
    plate(340, 84, "(b) d₃₁", [_arr(272, 101, 282, 101), _arr(408, 101, 398, 101)],
          "nén ngang trục phân cực")
    # (c) shear mode
    plate(558, 84, "(c) d₁₅", [_arr(500, 70, 546, 70), _arr(616, 132, 570, 132)],
          "trượt trên mặt bản")

    return _fig(svg(680, 176, "".join(o), "Ba chế độ hoạt động của bản áp điện phẳng"),
                "Hình 23.8 · Các chế độ hoạt động của một bản phẳng dùng làm phần tử áp điện.",
                "Figure 23.8 · Modes of operation for a simple plate as a piezoelectric device.",
                "Ba chế độ: nén dọc trục phân cực, nén ngang và trượt",
                "Three modes: longitudinal, transverse and shear")


# ---------------------------------------------------------------- 23.9
def fig_23_9():
    o = [_defs()]
    # twister: two crystals with perpendicular electrical axes
    o.append(_rect(92, 92, 110, 22, FILL, E, 1.4))
    o.append(_rect(92, 116, 110, 22, WARM, E, 1.4))
    o.append(_arr(78, 103, 60, 103))
    o.append(_arr(216, 127, 234, 127))
    o.append(_lbl(56, 96, "V", "t", "end"))
    o.append(_lbl(238, 131, "V"))
    o.append(_lbl(147, 74, "trục điện vuông góc", "ts", "middle"))
    o.append(_lbl(147, 158, "(a) twister — xoắn", "ts", "middle"))

    # bender: bimorph
    o.append(_path("M400,120 q70,-26 140,0", E, 1.6, "none"))
    o.append(_path("M400,132 q70,-26 140,0", G, 1.6, "none"))
    o.append(_lbl(470, 88, "hai phiến dán ghép", "ts", "middle"))
    o.append(_lbl(470, 158, "(b) bender — uốn", "ts", "middle"))
    o.append(_arr(400, 108, 382, 108))
    o.append(_arr(540, 108, 558, 108))
    o.append(_lbl(378, 112, "V", "t", "end"))
    o.append(_lbl(562, 112, "V"))

    return _fig(svg(680, 190, "".join(o),
                    "Biến dạng của đầu đo áp điện kiểu twister và bender khi đặt điện áp"),
                "Hình 23.9 · Độ cong của các đầu đo áp điện “twister” và “bender” khi đặt điện áp.",
                "Figure 23.9 · Curvature of “twister” and “bender” piezoelectric transducers when "
                "voltage is applied.",
                "Hai đầu đo áp điện: một xoắn và một uốn khi có điện áp",
                "Two piezoelectric transducers, one twisting and one bending under voltage")


# ---------------------------------------------------------------- 23.10
def fig_23_10():
    o = [_defs()]
    # exploded stack of the three-component transducer
    o.append(_rect(60, 74, 150, 14, FILL, E, 1.4))
    o.append(_lbl(216, 70, "nắp trên", "ts"))
    o.append(_rect(60, 96, 150, 16, WARM, E, 1.4))
    o.append(_lbl(135, 107, "X-cut (Fz)", "ts", "middle"))
    o.append(_rect(60, 120, 150, 16, "#ffffff", E, 1.4))
    o.append(_lbl(135, 131, "Y-cut (Fx)", "ts", "middle"))
    o.append(_rect(60, 144, 150, 16, "#ffffff", E, 1.4))
    o.append(_lbl(135, 155, "Y-cut (Fy)", "ts", "middle"))
    o.append(_rect(60, 168, 150, 14, FILL, E, 1.4))
    o.append(_lbl(216, 192, "đế", "ts"))
    o.append(_arr(135, 44, 135, 70))
    o.append(_lbl(141, 50, "F"))
    o.append(_lbl(135, 214, "(a) đầu đo ba thành phần", "ts", "middle"))

    # four transducers between base and top plate
    o.append(_rect(300, 74, 300, 16, FILL, E, 1.4))
    o.append(_lbl(306, 66, "bản trên", "ts"))
    for i in range(4):
        xx = 320 + i * 70
        o.append(_rect(xx, 96, 44, 44, WARM, E, 1.3))
        o.append(_lbl(xx + 22, 122, "3", "tb", "middle"))
    o.append(_rect(300, 146, 300, 16, FILL, E, 1.4))
    o.append(_lbl(450, 176, "bản đế", "ts", "middle"))
    o.append(_arr(450, 44, 450, 70))
    o.append(_lbl(456, 50, "F"))
    o.append(_lbl(450, 214, "(b) bốn đầu đo kẹp giữa hai bản", "ts", "middle"))

    return _fig(svg(680, 228, "".join(o),
                    "Đầu đo lực ba thành phần và cách bố trí bốn đầu đo trong dynamometer"),
                "Hình 23.10 · Đầu đo lực ba thành phần.",
                "Figure 23.10 · Three-component force transducer.",
                "Cấu tạo đầu đo ba thành phần và bốn đầu đo kẹp giữa hai bản",
                "Three-component transducer construction and four transducers clamped between plates")


# ---------------------------------------------------------------- 23.11
def fig_23_11():
    o = [_defs()]
    # splash cover
    o.append(_rect(400, 56, 96, 40, "#ffffff", E, 1.4))
    o.append(_lbl(448, 74, "vỏ chắn", "ts", "middle"))
    o.append(_lbl(448, 88, "bàn phay", "ts", "middle"))
    # rotating body
    o.append(_rect(296, 96, 88, 96, FILL, E, 1.5))
    # taper socket
    o.append(_poly([(304, 192), (376, 192), (368, 216), (312, 216)], WARM, E, 1.4))
    # base ring
    o.append(_rect(300, 216, 80, 14, FILL, E, 1.4))
    # ring sensor
    o.append(_rect(288, 230, 104, 26, "#ffffff", E, 1.5))
    o.append(_lbl(340, 247, "vòng cảm biến", "ts", "middle"))
    # tool
    o.append(_poly([(330, 256), (350, 256), (346, 292), (334, 292)], "#ffffff", E, 1.4))
    o.append(_lbl(340, 306, "dụng cụ cắt", "ts", "middle"))
    # charge amplifiers
    o.append(_rect(384, 200, 22, 52, WARM, E, 1.2))
    o.append(_lbl(395, 266, "KĐ", "ts", "middle"))
    # antennas
    o.append(_line(340, 96, 340, 76, E, 1.4))
    o.append(_lbl(340, 70, "anten", "ts", "middle"))
    o.append(_line(428, 96, 428, 112, G, 1.4))
    o.append(_lbl(428, 126, "anten cố định", "ts", "middle"))
    # callouts
    for n, x, y in (("1", 276, 236), ("2", 288, 200), ("3", 290, 220), ("7", 414, 190),
                    ("8", 326, 84), ("9", 410, 106), ("10", 492, 62)):
        o.append('<circle cx="%s" cy="%s" r="9" fill="#ffffff" stroke="%s" stroke-width="1.2"/>'
                 % (_f(x), _f(y), E))
        o.append(_lbl(x, y + 3.5, n, "ts", "middle"))

    return _fig(svg(680, 316, "".join(o),
                    "Hệ đo lực quay gắn trên trục chính để đo lực cắt trong phay năm trục"),
                "Hình 23.11 · Hệ đo lực xác định lực cắt gắn với dụng cụ trong phay năm trục.",
                "Figure 23.11 · Force measuring system to determine the tool-related cutting forces in "
                "five-axis milling.",
                "Mặt cắt trục chính có vòng cảm biến, bộ khuếch đại và hai ăng ten",
                "Spindle section with sensing ring, amplifiers and two antennas")


# ---------------------------------------------------------------- 23.12
def fig_23_12():
    o = [_defs()]
    o.append(_rect(180, 96, 320, 14, FILL, E, 1.6))
    o.append(_rect(180, 158, 320, 14, FILL, E, 1.6))
    o.append(_dim(516, 112, 516, 156))
    o.append(_lbl(524, 138, "h"))
    o.append(_dim(180, 190, 500, 190))
    o.append(_lbl(340, 206, "A", "t", "middle"))
    o.append(_arr(340, 56, 340, 92))
    o.append(_lbl(346, 62, "F"))
    o.append(_lbl(150, 108, "+", "tb", "end"))
    o.append(_lbl(150, 170, "−", "tb", "end"))
    o.append(_subs(340, 138, [("ε", False), ("0", True), (" ε", False), ("r", True)], "middle"))
    o.append(_subs(340, 224, [("C = \u03b5", False), ("0", True), (" \u03b5", False), ("r", True),
                              (" A / h", False)], "middle"))
    o.append(_lbl(420, 84, "màng đàn hồi", "ts"))

    return _fig(svg(680, 238, "".join(o), "Đầu đo lực kiểu điện dung với hai bản cực và khe không khí"),
                "Hình 23.12 · Đầu đo lực kiểu điện dung.",
                "Figure 23.12 · Capacitive force transducer.",
                "Hai bản cực song song cách nhau một khe hở, có lực tác dụng lên màng",
                "Two parallel plates separated by an air gap with a force on the membrane")


# ---------------------------------------------------------------- 23.13
def fig_23_13():
    o = [_defs()]
    # upper film with resistive material
    o.append(_rect(150, 84, 380, 34, "#ffffff", E, 1.4))
    o.append(_rect(230, 92, 220, 18, WARM, E, 1.3))
    o.append(_lbl(410, 74, "màng có vật liệu điện trở", "ts"))
    # lower film with interdigitating contacts
    o.append(_rect(150, 150, 380, 34, "#ffffff", E, 1.4))
    for i in range(6):
        xx = 230 + i * 38
        if i % 2 == 0:
            o.append(_rect(xx, 158, 22, 8, G, G, 1.0))
            o.append(_line(xx + 11, 158, xx + 11, 150, G, 1.2))
        else:
            o.append(_rect(xx, 168, 22, 8, E, E, 1.0))
            o.append(_line(xx + 11, 176, xx + 11, 184, E, 1.2))
    o.append(_lbl(340, 198, "màng có các điện cực đan răng lược", "ts", "middle"))
    # spacer
    o.append(_rect(150, 126, 60, 16, FILL, S, 1.1))
    o.append(_rect(470, 126, 60, 16, FILL, S, 1.1))
    o.append(_lbl(340, 138, "lớp đệm", "ts", "middle"))
    o.append(_arr(340, 48, 340, 80))
    o.append(_lbl(346, 54, "F"))

    return _fig(svg(680, 212, "".join(o), "Sơ đồ cấu tạo điện trở cảm nhận lực"),
                "Hình 23.13 · Sơ đồ một điện trở cảm nhận lực (FSR) điển hình.",
                "Figure 23.13 · Diagram of a typical force sensing resistor (FSR).",
                "Hai màng: một mang vật liệu điện trở, một mang điện cực đan răng lược",
                "Two films: one with resistive material, one with interdigitated contacts")


# ---------------------------------------------------------------- 23.14
def fig_23_14():
    o = [_defs()]
    x0, y0, x1, y1 = 96, 236, 600, 56

    def mx(v):
        return x0 + (_m.log10(v) - 0.0) * (x1 - x0) / 3.0

    def my(v):
        return y0 - (_m.log10(v) - 0.0) * (y0 - y1) / 3.6

    o.append(_line(x0, y0, x1, y0, E, 1.3))
    o.append(_line(x0, y0, x0, y1, E, 1.3))
    for v in (1, 10, 100, 1000):
        o.append(_line(mx(v), y0, mx(v), y0 + 5, E, 1.1))
        o.append(_lbl(mx(v), y0 + 18, str(v), "ts", "middle"))
    for v in (1, 10, 100, 1000):
        o.append(_line(x0 - 5, my(v), x0, my(v), E, 1.1))
        o.append(_lbl(x0 - 9, my(v) + 3.5, str(v), "ts", "end"))
    o.append(_lbl((x0 + x1) / 2.0, y0 + 36, "lực (g)", "ts", "middle"))
    o.append(_lbl(52, 146, "R (kΩ)", "ts", "middle"))

    pts = []
    f = 1.0
    while f <= 1000.0001:
        r = 300.0 * (10.0 / f) ** 2.2 if f < 10 else 300.0 * (10.0 / f)
        pts.append((mx(f), my(r)))
        f *= 1.08
    d = "M" + " L".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    o.append(_path(d, G, 2.2))

    o.append(_line(mx(10), y0, mx(10), my(300), G, 1.0, "4 4"))
    o.append(_lbl(mx(10) + 16, 96, "chuyển tiếp", "ts"))
    o.append(_lbl(mx(10) + 16, 110, "quanh 10 g", "ts"))
    o.append(_lbl(mx(400), 216, "vùng tuyến tính", "ts", "middle"))

    return _fig(svg(680, 286, "".join(o), "Đường cong điện trở theo lực của điện trở cảm nhận lực"),
                "Hình 23.14 · Điện trở theo lực của một điện trở cảm nhận lực điển hình.",
                "Figure 23.14 · Resistance as a function of force for a typical force sensing resistor.",
                "Đường cong giảm nhanh của điện trở khi lực tăng, có bước chuyển quanh 10 g",
                "Resistance falling steeply as force rises, with a transition near 10 g")


# ---------------------------------------------------------------- 23.15
def fig_23_15():
    o = [_defs()]
    # two crossed layers of copper strips
    for i in range(8):
        xx = 150 + i * 30
        o.append(_rect(xx, 76, 12, 130, "#e8eef5", E, 1.0))
    for j in range(8):
        yy = 86 + j * 15
        o.append(_rect(146, yy, 128, 6, WARM, S, 1.0))
    for i in range(8):
        for j in range(8):
            o.append('<rect x="%s" y="%s" width="12" height="6" fill="%s" stroke="%s" '
                     'stroke-width="0.8"/>' % (_f(150 + i * 30), _f(86 + j * 15), G, E))
    o.append(_lbl(210, 68, "64 phần tử, bước 2 mm", "ts", "middle"))
    o.append(_dim(150, 224, 360, 224))
    o.append(_lbl(255, 240, "8 × 8", "ts", "middle"))

    # section: two layers separated by silicone strips
    o.append(_rect(420, 76, 200, 18, "#e8eef5", E, 1.3))
    o.append(_lbl(520, 70, "lớp dây đồng 1", "ts", "middle"))
    for i in range(4):
        o.append(_rect(432 + i * 50, 106, 26, 14, FILL, S, 1.1))
    o.append(_lbl(520, 134, "đệm silicon", "ts", "middle"))
    o.append(_rect(420, 146, 200, 18, WARM, E, 1.3))
    o.append(_lbl(520, 178, "lớp dây đồng 2", "ts", "middle"))
    o.append(_lbl(520, 200, "lớp mỏng, mềm", "ts", "middle"))
    o.append(_lbl(520, 214, "dán được lên đầu ngón", "ts", "middle"))

    return _fig(svg(680, 252, "".join(o),
                    "Mảng xúc giác 8 nhân 8 với hai lớp dây đồng vuông góc"),
                "Hình 23.15 · Cảm biến mảng xúc giác.",
                "Figure 23.15 · Tactile array sensor.",
                "Lưới 8 nhân 8 phần tử cảm biến và mặt cắt hai lớp dây đồng",
                "8 by 8 sensing grid and a section through two crossed copper layers")


# ---------------------------------------------------------------- 23.16
def fig_23_16():
    o = [_defs()]
    # three-layer stack
    o.append(_rect(60, 70, 190, 16, FILL, E, 1.4))
    o.append(_lbl(155, 62, "lớp phủ bảo vệ", "ts", "middle"))
    o.append(_rect(60, 96, 190, 20, WARM, E, 1.4))
    o.append(_lbl(155, 110, "elastomer dẫn điện", "ts", "middle"))
    o.append(_rect(60, 126, 190, 20, "#ffffff", E, 1.4))
    o.append(_lbl(155, 140, "bản mạch in", "ts", "middle"))
    o.append(_arr(90, 40, 90, 66))
    o.append(_lbl(96, 46, "F"))

    # PCB with two rows of two bullseyes
    o.append(_rect(60, 168, 190, 66, "#ffffff", E, 1.4))
    for r in range(2):
        for c in range(2):
            cx = 92 + c * 62
            cy = 186 + r * 30
            o.append('<circle cx="%s" cy="%s" r="11" fill="none" stroke="%s" stroke-width="1.4"/>'
                     % (_f(cx), _f(cy), E))
            o.append('<circle cx="%s" cy="%s" r="5" fill="%s" stroke="%s" stroke-width="1.1"/>'
                     % (_f(cx), _f(cy), G, E))
    o.append(_lbl(155, 250, "(a) ba lớp và bốn taxel", "ts", "middle"))

    # taxel circuit
    o.append(_line(320, 96, 320, 116, E, 1.3))
    o.append(_lbl(320, 88, "đường cột", "ts", "middle"))
    o.append(_rect(310, 116, 20, 10, G, G, 1.0))
    o.append(_lbl(336, 108, "elastomer", "ts"))
    o.append(_line(330, 121, 372, 121, E, 1.2))
    o.append(_path("M372,121 L384,113 L396,129 L408,113 L420,129 L432,121", E, 1.4))
    o.append(_lbl(402, 146, "D", "tb", "middle"))
    o.append(_line(432, 121, 470, 121, E, 1.2))
    o.append(_line(470, 121, 470, 168, E, 1.2))
    o.append('<circle cx="470" cy="180" r="12" fill="#ffffff" stroke="%s" stroke-width="1.3"/>' % E)
    o.append(_lbl(470, 184, "T", "tb", "middle"))
    o.append(_line(470, 192, 470, 214, E, 1.2))
    o.append(_lbl(470, 228, "transistor chọn", "ts", "middle"))
    o.append(_lbl(400, 250, "(b) mạch một taxel", "ts", "middle"))

    return _fig(svg(680, 264, "".join(o),
                    "Cấu tạo ba lớp của mảng taxel và mạch của một taxel có diode chống nhiễu"),
                "Hình 23.16 · Mảng cảm biến taxel điển hình.",
                "Figure 23.16 · Typical taxel sensor array.",
                "Ba lớp của mảng taxel và sơ đồ mạch một taxel với diode",
                "Three-layer taxel array and the circuit of a single taxel with its diode")


# ---------------------------------------------------------------- 23.17
def fig_23_17():
    o = [_defs()]
    boxes = [(64, "Mảng\ncảm biến"), (196, "Dồn\nkênh"), (328, "ADC"),
             (460, "Bộ\nxử lý"), (592, "Đầu ra")]
    for x, t in boxes:
        o.append(_box(x - 44, 76, 88, 46, t, E, "#ffffff", 10))
    for i in range(4):
        x1 = boxes[i][0] + 44
        x2 = boxes[i + 1][0] - 44
        o.append(_arr(x1 + 3, 99, x2 - 3, 99))
    o.append(_lbl(340, 62, "bố trí chung của hệ mảng cảm biến thông minh", "ts", "middle"))

    # example: tactile finger
    o.append(_rect(140, 170, 90, 110, FILL, E, 1.5))
    for i in range(4):
        o.append(_rect(146, 180 + i * 24, 78, 10, G, G, 1.0))
    o.append(_lbl(185, 300, "bốn dải polymer áp điện", "ts", "middle"))
    o.append(_lbl(185, 314, "(tiếp xúc động)", "ts", "middle"))
    o.append(_rect(250, 200, 60, 26, "#ffffff", E, 1.4))
    o.append(_lbl(280, 217, "gage lực", "ts", "middle"))
    o.append(_lbl(280, 240, "lực nắm tĩnh", "ts", "middle"))
    o.append(_arr(236, 213, 246, 213))
    o.append(_lbl(400, 186, "ngón tay xúc giác", "ts"))
    o.append(_lbl(400, 202, "cảm biến tiếp xúc động", "ts"))
    o.append(_lbl(400, 218, "và cảm biến lực tĩnh", "ts"))
    o.append(_lbl(400, 234, "trên cùng một đầu ngón", "ts"))

    return _fig(svg(680, 324, "".join(o),
                    "Sơ đồ khối hệ mảng cảm biến thông minh và ví dụ ngón tay xúc giác"),
                "Hình 23.17 · Bố trí chung của một hệ mảng cảm biến thông minh.",
                "Figure 23.17 · General arrangement of an intelligent sensor array system.",
                "Sơ đồ khối từ mảng cảm biến tới bộ xử lý và ví dụ ngón tay xúc giác",
                "Block diagram from sensor array to processor, plus a tactile finger example")


FIGS = [fig_23_1, fig_23_2, fig_23_3, fig_23_4, fig_23_5, fig_23_6, fig_23_7, fig_23_8,
        fig_23_9, fig_23_10, fig_23_11, fig_23_12, fig_23_13, fig_23_14, fig_23_15,
        fig_23_16, fig_23_17]


def fig(n):
    return FIGS[n - 1]()
