# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 27 — Acoustic Measurement (Per Rasmussen,
G.R.A.S. Sound and Vibration).

The source chapter contains exactly twenty-one figures (27.1–27.21) and
five tables. FIGS is a 21-figure set — nothing is padded.

Every drawing was reconstructed against the rendered PDF pages in
work/ch27img (the geometry, the labels and the curve shapes were read off
the page images, not guessed from the captions). Four of the originals are
photographs (27.1, 27.8, 27.11, 27.13, 27.20); those are redrawn here as
line illustrations of the same object, which is the convention used
throughout this handbook.
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
            '<marker id="ah27" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah27g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah27s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah27r" markerWidth="9" markerHeight="9" refX="2" refY="3" '
            'orient="auto"><path d="M7,0 L0,3 L7,6 z" fill="%s"/></marker>'
            '<marker id="ah27b" markerWidth="9" markerHeight="9" refX="2" refY="3" '
            'orient="auto"><path d="M7,0 L0,3 L7,6 z" fill="%s"/></marker>'
            '<pattern id="hatch27" width="5" height="5" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" '
            'stroke="#9aa4b2" stroke-width="1.1"/></pattern>'
            '</defs>' % (E, G, S, S, E))


def _arr(x1, y1, x2, y2, col=E, marker="ah27", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _darr(x1, y1, x2, y2, col=E, sw=1.4):
    """Double-headed arrow."""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-start="url(#ah27b)" marker-end="url(#ah27)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=4):
    if isinstance(t, (list, tuple)):
        t = "\n".join(t)
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 2) + fs * 0.36
        o.append('<text class="t" x="%s" y="%s" text-anchor="middle" '
                 'font-size="%s">%s</text>' % (_f(x + w / 2.0), _f(yy), fs, ln))
    return "".join(o)


def _rect(x, y, w, h, fill=FILL, col=E, sw=1.4, dash=None, rx=0):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col,
                                       _f(sw), d))


def _dot(x, y, r=3.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _line(x1, y1, x2, y2, col=S, sw=1.0, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, _f(sw), d))


def _path(d, col=E, sw=1.4, fill="none", dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, col, _f(sw), ds))


def _circ(cx, cy, r, fill="none", col=E, sw=1.4, dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, _f(sw), ds))


def _poly(pts, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    p = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (p, fill, col, _f(sw), d))


def _mic(cx, top, d, h, grid=True):
    """A measurement microphone seen from the side: body + slotted cap."""
    o = [_rect(cx - d / 2.0, top, d, h, "#f4f6f9", E, 1.3, rx=2)]
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#e7ebf1" stroke="%s" '
             'stroke-width="1.2"/>' % (_f(cx), _f(top), _f(d / 2.0), _f(d * 0.20), E))
    if grid:
        n = max(5, int(d / 6))
        for i in range(n):
            a = _m.pi * (i + 0.5) / n
            o.append(_line(cx, top, cx + (d / 2.0 - 1) * _m.cos(a),
                           top - d * 0.20 * _m.sin(a), "#8c96a4", 0.8))
    o.append(_line(cx - d / 2.0, top + h * 0.62, cx + d / 2.0, top + h * 0.62, E, 0.9))
    return "".join(o)


# ================================================================ 27.1
def fig_27_1():
    o = [_defs()]
    # the set of the photograph: two ½" capsules and two ¼" capsules
    specs = [(110, 96, 62, 118, "½″", "1/2 in"),
             (255, 74, 58, 140, "½″", "1/2 in"),
             (370, 150, 30, 66, "¼″", "1/4 in"),
             (520, 118, 40, 84, "¼″", "1/4 in")]
    for cx, top, d, h, vi, en in specs:
        o.append(_mic(cx, top, d, h))
        o.append(_lbl(cx, top + h + 18, vi, "tb", "middle"))
        o.append(_lbl(cx, top + h + 31, en, "ts", "middle"))
    o.append(_lbl(340, 24, "Micro đo (condenser) — cỡ màng khác nhau", "ts", "middle"))
    return _fig(svg(680, 300, "".join(o), "Bốn micro đo kiểu condenser"),
                "Hình 27.1 · Micro đo: loại ½″ và ¼″. Micro condenser là đầu dò chuẩn cho mọi "
                "phép đo âm học; đường kính màng quyết định độ nhạy và dải tần sử dụng được.",
                "Figure 27.1 · Measurement microphones: ½″ and ¼″. The condenser microphone is the "
                "standard transducer for acoustic measurement; diaphragm diameter sets the "
                "sensitivity and the usable frequency range.",
                "Bốn micro đo kích cỡ khác nhau, mỗi chiếc có lưới bảo vệ ở đầu",
                "Four measurement microphones of different sizes, each with a slotted protection grid")


# ================================================================ 27.2
def fig_27_2():
    o = [_defs()]
    cx = 250
    # protection grid (cap, lifted)
    o.append(_path("M%s,96 q0,-34 62,-34 q62,0 62,34" % (_f(cx - 62), ), E, 1.6, "#e7ebf1"))
    o.append(_line(cx - 62, 96, cx + 62, 96, E, 1.4))
    for i in range(9):
        x = cx - 54 + i * 13.5
        o.append(_line(x, 96, x, 96 - 22 - 8 * _m.sin(_m.pi * (i + 0.5) / 9), "#8c96a4", 0.9))
    # diaphragm
    o.append('<ellipse cx="%s" cy="128" rx="58" ry="9" fill="#dfe7f2" stroke="%s" '
             'stroke-width="1.5"/>' % (_f(cx), E))
    # backplate
    o.append(_rect(cx - 54, 150, 108, 20, "#cfd8e6", E, 1.5, rx=3))
    for i in range(5):
        o.append(_circ(cx - 34 + i * 17, 160, 2.4, "#ffffff", E, 0.9))
    # casing (cup)
    o.append(_path("M%s,110 V232 H%s V110" % (_f(cx - 74), _f(cx + 74)), E, 1.7))
    # insulator
    o.append(_rect(cx + 40, 214, 30, 14, WARM, E, 1.2, rx=2))
    # leaders
    o.append(_line(cx - 40, 74, 120, 56, S, 1.0))
    o.append(_lbl(114, 52, "Lưới bảo vệ", "ts", "end"))
    o.append(_line(cx + 30, 124, 420, 108, S, 1.0))
    o.append(_lbl(426, 104, "Màng (diaphragm)", "ts", "start"))
    o.append(_line(cx + 54, 156, 420, 168, S, 1.0))
    o.append(_lbl(426, 172, "Bản cực (backplate)", "ts", "start"))
    o.append(_line(cx - 74, 214, 120, 226, S, 1.0))
    o.append(_lbl(114, 232, "Vỏ (casing)", "ts", "end"))
    o.append(_line(cx + 70, 220, 420, 214, S, 1.0))
    o.append(_lbl(426, 218, "Cách điện", "ts", "start"))
    return _fig(svg(680, 270, "".join(o), "Các phần tử cơ bản của micro đo"),
                "Hình 27.2 · Các phần tử cơ bản của micro đo: lưới bảo vệ, vỏ, màng, bản cực và "
                "cách điện. Màng và bản cực tạo thành hai bản của một tụ điện không khí.",
                "Figure 27.2 · Basic elements of a measurement microphone: protection grid, casing, "
                "diaphragm, backplate and insulator. Diaphragm and backplate form the two plates of "
                "an air capacitor.",
                "Sơ đồ tháo rời micro: lưới, màng, bản cực, vỏ và cách điện có chú thích",
                "Exploded view of a microphone: grid, diaphragm, backplate, casing and insulator")


# ================================================================ 27.3
def fig_27_3():
    o = [_defs()]
    # left: diaphragm in section
    o.append(_line(80, 60, 80, 190, E, 1.4))
    o.append(_line(230, 60, 230, 190, E, 1.4))
    o.append(_line(80, 60, 230, 60, E, 1.4))
    o.append(_line(80, 190, 230, 190, E, 1.4))
    o.append(_line(80, 120, 230, 120, E, 1.0, "5 4"))
    o.append(_path("M110,120 q40,-26 80,0", G, 1.8))
    o.append(_darr(150, 120, 150, 88, G, 1.3))
    o.append(_lbl(150, 210, "màng + độ căng", "ts", "middle"))
    # right: mass-spring-dashpot
    o.append(_rect(360, 46, 66, 34, "#dfe7f2", E, 1.5))
    o.append(_lbl(393, 68, "M", "tb", "middle"))
    o.append(_line(393, 80, 393, 96, E, 1.2))
    xs = []
    for i in range(9):
        y = 96 + i * 8
        xs.append((393 + (16 if i % 2 == 0 else -16), y))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in xs), G, 1.6))
    o.append(_line(393, 160, 393, 182, E, 1.2))
    o.append(_rect(340, 182, 106, 10, "#cfd8e6", E, 1.4))
    # dashpot
    o.append(_rect(470, 96, 46, 86, "#ffffff", E, 1.4))
    o.append(_rect(474, 130, 38, 40, "#dfe7f2", E, 0.0))
    o.append(_line(452, 150, 470, 150, E, 1.3))
    o.append(_line(452, 150, 452, 96, E, 1.0))
    o.append(_line(452, 96, 393, 96, E, 1.0))
    o.append(_lbl(516, 112, "D", "tb", "start"))
    o.append(_lbl(410, 130, "S", "tb", "middle"))
    o.append(_lbl(393, 40, "Khối lượng màng", "ts", "middle"))
    o.append(_lbl(300, 232, "Độ căng màng", "ts", "middle"))
    o.append(_arr(300, 222, 300, 196, S, "ah27s", 1.0))
    o.append(_lbl(520, 208, "Cản hệ thống", "ts", "middle"))
    o.append(_arr(520, 198, 500, 180, S, "ah27s", 1.0))
    return _fig(svg(680, 250, "".join(o), "Tương tự cơ học của micro"),
                "Hình 27.3 · Tương tự cơ học của micro: màng có khối lượng M, độ căng (lò xo S) và "
                "cản D. Ba tham số này quyết định đáp tuyến tần số của micro.",
                "Figure 27.3 · Mechanical analogy of a microphone: the diaphragm has mass M, tension "
                "(spring S) and damping D. These three parameters set the frequency response.",
                "Bên trái là mặt cắt màng, bên phải là hệ khối lượng–lò xo–cản tương đương",
                "Left: diaphragm section; right: equivalent mass-spring-damper system")


# ================================================================ 27.4
def fig_27_4():
    b = Box(560, 250, (0, 10), (0, 10), pad=(52, 22, 22, 44))
    body = b.axes("Tần số", "Mức",
                  xt=[(2.2, ""), (4.6, ""), (6.8, "")], yt=[], grid=False)
    # nominal response: flat then roll-off
    pts = []
    for i in range(0, 141):
        u = i / 140.0 * 10
        v = 8.0 / (1 + _m.exp((u - 6.6) * 1.6))
        pts.append((u, v))
    body += b.curve(pts, "c1")
    # resonance bump variant (decreased damping)
    pts2 = []
    for i in range(0, 141):
        u = i / 140.0 * 10
        v = 8.0 / (1 + _m.exp((u - 7.0) * 1.4)) + 2.0 * _m.exp(-((u - 6.5) ** 2) / 0.30)
        pts2.append((u, v))
    body += b.curve(pts2, "c3")
    # decreased mass -> knee moves right
    pts3 = []
    for i in range(0, 141):
        u = i / 140.0 * 10
        v = 8.0 / (1 + _m.exp((u - 7.6) * 1.7))
        pts3.append((u, v))
    body += b.curve(pts3, "c2")
    body += b.label(0.4, 8.6, "Độ căng màng giảm →", "ts")
    body += _arr(b.x(2.6), b.y(8.45), b.x(3.9), b.y(8.45), S, "ah27s", 1.0)
    body += b.label(4.5, 9.4, "Cản hệ thống giảm", "ts")
    body += _arr(b.x(5.6), b.y(9.15), b.x(5.6), b.y(8.3), S, "ah27s", 1.0)
    body += b.label(7.2, 6.2, "Khối lượng", "ts")
    body += b.label(7.2, 5.4, "màng giảm →", "ts")
    body += _arr(b.x(7.1), b.y(6.9), b.x(8.2), b.y(6.9), S, "ah27s", 1.0)
    body += b.label(2.0, 3.0, "Độ căng màng giảm ←", "ts")
    body += _arr(b.x(4.0), b.y(2.6), b.x(2.7), b.y(2.6), S, "ah27s", 1.0)
    return _fig(svg(560, 250, body, "Ảnh hưởng của tham số micro tới đáp tuyến"),
                "Hình 27.4 · Ảnh hưởng của các tham số micro tới đáp tuyến tần số. Giảm độ căng "
                "màng làm tần số cộng hưởng hạ xuống; giảm cản làm đỉnh cộng hưởng cao lên; giảm "
                "khối lượng màng đẩy điểm gãy lên cao.",
                "Figure 27.4 · Influence of microphone parameters on frequency response. Lower "
                "diaphragm tension drops the resonance; lower damping raises the resonance peak; "
                "lower diaphragm mass pushes the break point higher.",
                "Ba đường đáp tuyến: phẳng rồi gãy xuống, một đường có đỉnh cộng hưởng",
                "Three response curves: flat then rolling off, one with a resonance peak")


# ================================================================ 27.5
def fig_27_5():
    o = [_defs()]
    # rigid wall
    o.append(_line(330, 96, 330, 250, E, 2.2))
    o.append(_line(330, 46, 330, 92, E, 2.2, "2 5"))
    o.append(_line(330, 254, 330, 292, E, 2.2, "2 5"))
    # incident plane waves
    for i, y in enumerate((86, 120, 154, 188, 222)):
        o.append(_arr(120, y, 300, y, E, "ah27", 1.3))
    o.append(_lbl(58, 154, "Sóng tới", "ts", "middle"))
    # microphone flush in the wall
    o.append(_rect(330, 176, 74, 26, "#f4f6f9", E, 1.4, rx=3))
    o.append(_line(404, 189, 470, 189, E, 1.3))
    o.append(_path("M470,189 q26,0 34,22", E, 1.3))
    o.append(_lbl(424, 168, "Micro áp suất", "ts", "middle"))
    o.append(_lbl(344, 268, "Tường cứng", "ts", "start"))
    return _fig(svg(680, 320, "".join(o), "Ứng dụng của micro áp suất"),
                "Hình 27.5 · Ứng dụng của micro áp suất. Micro được gắn phẳng vào một tường cứng để "
                "đo đúng áp suất tại bề mặt, ví dụ trên thành của một hộp kín.",
                "Figure 27.5 · Application of pressure microphones. The microphone is mounted flush "
                "in a rigid wall so that it measures the pressure at the surface itself, for example "
                "on the wall of a closed coupler.",
                "Sóng phẳng tới đập vào tường cứng, micro gắn xuyên qua tường",
                "Plane waves arriving at a rigid wall with a microphone mounted through it")


# ================================================================ 27.6
def fig_27_6():
    o = [_defs()]
    sx, sy = 190, 170
    o.append(_dot(sx, sy, 7))
    o.append(_lbl(sx, sy + 84, "Nguồn âm", "ts", "middle"))
    for a in (150, 180, 210, 240, 270, 300, 330, 20, 340):
        r = _m.radians(a)
        o.append(_arr(sx + 12 * _m.cos(r), sy - 12 * _m.sin(r),
                      sx + 62 * _m.cos(r), sy - 62 * _m.sin(r), E, "ah27", 1.2))
    # free-field microphone aimed at the source
    o.append(_line(sx + 6, sy - 2, 430, 150, S, 0.9, "4 4"))
    o.append(_rect(430, 138, 76, 24, "#f4f6f9", E, 1.4, rx=3))
    o.append(_line(506, 150, 560, 150, E, 1.3))
    o.append(_path("M560,150 q26,0 34,20", E, 1.3))
    o.append(_lbl(468, 128, "Micro trường tự do", "ts", "middle"))
    o.append(_lbl(430, 240, "Hướng 0° tới nguồn", "ts", "middle"))
    return _fig(svg(680, 270, "".join(o), "Ứng dụng của micro trường tự do"),
                "Hình 27.6 · Ứng dụng của micro trường tự do. Micro phải hướng thẳng về nguồn "
                "(góc tới 0°) để đo áp suất như nó tồn tại trước khi đưa micro vào trường âm.",
                "Figure 27.6 · Application of a free-field microphone. The microphone is aimed "
                "straight at the source (0° incidence) so that it measures the pressure as it "
                "existed before the microphone entered the sound field.",
                "Nguồn điểm phát sóng mọi hướng, micro hướng về nguồn",
                "A point source radiating in all directions with a microphone aimed at it")


# ================================================================ 27.7
def _mini(y0, kind):
    """One panel of figure 27.7, drawn at an explicit vertical offset."""
    o = []
    X0, X1 = 76, 330
    YB = y0 + 74
    o.append(_line(X0, YB, X1, YB, E, 1.3))
    o.append(_line(X0, YB, X0, y0 + 18, E, 1.3))
    pts = []
    for i in range(0, 121):
        u = i / 120.0
        if kind == "a":                      # pressure build-up in front of diaphragm
            v = 0.30 + 0.62 * _m.exp(-((u - 0.72) ** 2) / 0.045)
        elif kind == "b":                    # pressure response of the microphone
            v = 0.78 / (1 + _m.exp((u - 0.62) * 12))
        else:                                # resulting free-field response
            v = 0.78 / (1 + _m.exp((u - 0.78) * 14))
        pts.append((X0 + u * (X1 - X0), YB - v * 54))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts), E, 1.6))
    o.append(_lbl(X0 + 4, y0 + 22, "Level", "ts"))
    o.append(_lbl(X1 - 8, YB + 14, "Freq.", "ts", "end"))
    return "".join(o)


def fig_27_7():
    o = [_defs()]
    y = 16
    for lab, kind, cap in (("(A)", "a", "Tăng áp trước màng"),
                           ("(B)", "b", "Đáp tuyến áp của micro"),
                           ("(C)", "c", "Đáp tuyến trường tự do")):
        o.append(_mini(y, kind))
        o.append(_lbl(24, y + 44, lab, "tb", "start"))
        o.append(_lbl(320, y + 104, cap, "ts", "middle"))
        y += 112
    return _fig(svg(560, 370, "".join(o), "Đáp tuyến của micro trường tự do"),
                "Hình 27.7 · Đáp tuyến tần số của micro trường tự do: (A) mức tăng áp trước màng; "
                "(B) đáp tuyến áp của micro (giảm ở tần số cao); (C) đáp tuyến tổng hợp — tích của "
                "hai đường trên, phẳng tới tần số danh định.",
                "Figure 27.7 · Frequency response of a free-field microphone: (A) pressure increase "
                "in front of the diaphragm; (B) microphone pressure response, falling at high "
                "frequency; (C) resulting free-field response — the product of the two, flat up to "
                "the rated frequency.",
                "Ba ô xếp dọc, mỗi ô một đường đáp tuyến: tăng, giảm, rồi phẳng",
                "Three stacked panels, each with one response curve: rising, falling, then flat")


# ================================================================ 27.8
def fig_27_8():
    o = [_defs()]
    # body
    o.append(_path("M250,120 q0,-26 30,-26 h60 q30,0 30,26 v150 q0,20 -20,20 h-80 q-20,0 -20,-20 z",
                   E, 1.7, "#f7f9fc"))
    # microphone stalk
    o.append(_rect(296, 40, 18, 56, "#e7ebf1", E, 1.4, rx=2))
    for i in range(6):
        o.append(_line(298 + i * 3, 44, 298 + i * 3, 92, "#8c96a4", 0.7))
    o.append(_line(305, 96, 305, 120, E, 1.3))
    # display
    o.append(_rect(266, 132, 92, 56, "#ffffff", E, 1.5, rx=3))
    o.append(_lbl(312, 164, "dB", "tb", "middle"))
    # keypad
    for r in range(4):
        for c in range(4):
            o.append(_rect(268 + c * 22, 200 + r * 17, 16, 12, "#eef2f7", E, 0.9, rx=2))
    o.append(_lbl(312, 314, "Máy đo mức âm", "ts", "middle"))
    o.append(_lbl(340, 60, "micro", "ts", "start"))
    return _fig(svg(680, 336, "".join(o), "Máy đo mức âm kiểu 1"),
                "Hình 27.8 · Máy đo mức âm kiểu 1 hiện đại có bộ phân tích tần số tích hợp: micro ở "
                "đầu, hiển thị số và bàn phím chọn chức năng.",
                "Figure 27.8 · Modern Type 1 sound level meter with built-in frequency analyser: "
                "microphone at the tip, numeric display and a keypad for function selection.",
                "Máy đo mức âm cầm tay có micro ở đỉnh, màn hình và bàn phím",
                "A handheld sound level meter with a microphone at the tip, display and keypad")


# ================================================================ 27.9
def fig_27_9():
    o = [_defs()]
    y = 96
    # mic capsule
    o.append('<ellipse cx="70" cy="%s" rx="15" ry="9" fill="#e7ebf1" stroke="%s" '
             'stroke-width="1.4"/>' % (_f(y), E))
    o.append(_line(85, y, 108, y, E, 1.2))
    # preamplifier triangle
    o.append(_poly([(110, y - 20), (110, y + 20), (152, y)], "#ffffff", E, 1.5))
    o.append(_line(152, y, 190, y, E, 1.2))
    # weighting box
    o.append(_rect(190, y - 22, 74, 44, "#ffffff", E, 1.5, rx=3))
    o.append(_path("M198,%s q14,-12 28,0 q10,8 18,-6" % _f(y + 6), G, 1.4))
    o.append(_lbl(227, y - 4, "A", "ts", "middle"))
    o.append(_line(264, y, 300, y, E, 1.2))
    # RMS box
    o.append(_rect(300, y - 22, 74, 44, "#ffffff", E, 1.5, rx=3))
    o.append(_path("M308,%s q10,-12 20,0 q10,12 20,0" % _f(y + 4), G, 1.4))
    o.append(_lbl(337, y - 4, "RMS", "ts", "middle"))
    o.append(_line(374, y, 410, y, E, 1.2))
    # meter box
    o.append(_rect(410, y - 22, 74, 44, "#ffffff", E, 1.5, rx=3))
    o.append(_line(424, y + 14, 470, y + 14, E, 1.2))
    o.append(_line(447, y + 14, 466, y - 10, G, 1.6))
    o.append(_line(447, y + 14, 447, y - 12, E, 0.8, "3 3"))
    # labels
    o.append(_lbl(70, y + 44, "Mic.", "ts", "middle"))
    o.append(_lbl(131, y + 44, "Tiền khuếch đại", "ts", "middle"))
    o.append(_lbl(227, y + 44, "Cân tần số", "ts", "middle"))
    o.append(_lbl(337, y + 44, "Tách sóng RMS", "ts", "middle"))
    o.append(_lbl(447, y + 44, "Chỉ thị", "ts", "middle"))
    return _fig(svg(680, 190, "".join(o), "Các khối chức năng của máy đo mức âm"),
                "Hình 27.9 · Các khối chức năng của máy đo mức âm: micro → tiền khuếch đại → bộ "
                "cân tần số (A) → tách sóng RMS → chỉ thị.",
                "Figure 27.9 · Functional parts of a sound level meter: microphone → preamplifier → "
                "A-weighting filter → RMS detector → display.",
                "Chuỗi khối: micro, tiền khuếch đại, cân tần số, RMS, chỉ thị",
                "Block chain: microphone, preamplifier, weighting, RMS detector, meter")


# ================================================================ 27.10
def _a_weight(f):
    """IEC 61672 A-weighting, in dB."""
    f2 = f * f
    ra = (12194.0 ** 2 * f2 ** 2) / ((f2 + 20.6 ** 2) *
                                    _m.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) *
                                    (f2 + 12194.0 ** 2))
    return 20.0 * _m.log10(ra) + 2.00


def fig_27_10():
    b = Box(620, 300, (0, 1), (-70, 20), pad=(56, 22, 22, 46))
    # log axis 10 Hz .. 20 kHz
    def lx(f):
        return _m.log10(f / 10.0) / _m.log10(2000.0)
    ticks = [(10, "10"), (20, "20"), (50, "50"), (100, "100"), (200, "200"),
             (500, "500"), (1000, "1k"), (2000, "2k"), (5000, "5k"),
             (10000, "10k"), (20000, "20k")]
    xt = [(lx(f), lab) for f, lab in ticks]
    yt = [(-70, "−70"), (-60, "−60"), (-50, "−50"), (-40, "−40"), (-30, "−30"),
          (-20, "−20"), (-10, "−10"), (0, "0"), (10, "10"), (20, "20")]
    body = b.axes("Tần số (Hz)", "dB", xt=xt, yt=yt, grid=True)
    pts = []
    for i in range(0, 201):
        u = i / 200.0
        f = 10.0 * (2000.0 ** u)
        pts.append((u, _a_weight(f)))
    body += b.curve(pts, "c1")
    body += b.label(lx(1000), 6, "0 dB tại 1 kHz", "ts", "middle")
    return _fig(svg(620, 300, body, "Đường cong cân tần số A"),
                "Hình 27.10 · Đường cong cân tần số A. Bộ lọc A làm suy giảm mạnh tần số thấp và "
                "tần số rất cao, chỉ hơi nhấn vùng 1–5 kHz, nhằm mô phỏng độ nhạy của tai người.",
                "Figure 27.10 · A-weighting curve. The A-filter strongly attenuates low and very "
                "high frequencies and slightly lifts the 1–5 kHz region, approximating the "
                "sensitivity of the human ear.",
                "Đường cong A trên trục tần số logarit, từ âm 70 dB ở 10 Hz lên 0 dB ở 1 kHz",
                "The A-weighting curve on a logarithmic frequency axis, from −70 dB at 10 Hz to 0 dB at 1 kHz")


# ================================================================ 27.11
def fig_27_11():
    o = [_defs()]
    # instrument body: a wedge with a raised screen
    o.append(_poly([(150, 150), (470, 150), (500, 250), (120, 250)], "#f7f9fc", E, 1.6))
    o.append(_poly([(160, 60), (462, 60), (470, 148), (150, 148)], "#eef2f7", E, 1.6))
    o.append(_rect(176, 72, 262, 66, "#ffffff", E, 1.3, rx=2))
    # bar spectrum on the screen
    for i in range(14):
        h = 8 + 40 * (0.35 + 0.65 * abs(_m.sin(i * 1.7)))
        o.append(_rect(184 + i * 18, 130 - h, 11, h, "#9aa4b2", E, 0.0))
    o.append(_line(184, 132, 430, 132, E, 1.0))
    # control panel
    for r in range(2):
        for c in range(9):
            o.append(_rect(150 + c * 38, 170 + r * 26, 26, 16, "#ffffff", E, 0.9, rx=2))
    # cable and probe
    o.append(_path("M120,240 q-50,10 -58,-26 q-8,-36 22,-40", E, 1.3))
    o.append(_line(500, 220, 560, 232, E, 1.6))
    o.append(_rect(560, 226, 46, 12, "#e7ebf1", E, 1.2, rx=2))
    o.append(_lbl(310, 286, "Máy phân tích tần số thời gian thực", "ts", "middle"))
    return _fig(svg(680, 310, "".join(o), "Máy phân tích tần số thời gian thực"),
                "Hình 27.11 · Máy phân tích tần số thời gian thực dùng cho đo âm học, hiển thị phổ "
                "dạng cột theo dải 1/3 octave cùng đầu dò và cáp nối.",
                "Figure 27.11 · Real-time frequency analyser for acoustic measurements, showing a "
                "bar spectrum in 1/3-octave bands together with its probe and cable.",
                "Thiết bị có màn hình phổ dạng cột, bàn phím điều khiển và đầu dò",
                "An instrument with a bar-spectrum screen, a control panel and a probe")


# ================================================================ 27.12
def fig_27_12():
    o = [_defs()]
    cx, cy = 340, 330
    RX, RY, ZX = 132, 46, 108
    # equator (back half dashed, front half solid)
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="%s" '
             'stroke-width="1.4" stroke-dasharray="5 4"/>'
             % (_f(cx), _f(cy), _f(RX), _f(RY), E))
    # dome
    o.append(_path("M%s,%s A%s,%s 0 0 1 %s,%s"
                   % (_f(cx - RX), _f(cy), _f(RX), _f(ZX), _f(cx + RX), _f(cy)), E, 1.6))
    # axes
    o.append(_arr(cx, cy, cx, cy - ZX - 40, E, "ah27", 1.2))
    o.append(_lbl(cx + 6, cy - ZX - 44, "z", "ts", "start"))
    o.append(_arr(cx, cy, cx + RX + 78, cy - 42, E, "ah27", 1.2))
    o.append(_lbl(cx + RX + 84, cy - 44, "y", "ts", "start"))
    o.append(_arr(cx, cy, cx - RX - 92, cy + 20, E, "ah27", 1.2))
    o.append(_lbl(cx - RX - 98, cy + 24, "x", "ts", "end"))
    # reference box
    o.append(_poly([(cx - 26, cy - 8), (cx + 14, cy - 22), (cx + 34, cy - 6),
                    (cx + 34, cy + 26), (cx - 6, cy + 40), (cx - 26, cy + 24)], "#ffffff", E, 1.3))
    o.append(_line(cx - 26, cy - 8, cx - 6, cy + 6, E, 1.0))
    o.append(_line(cx - 6, cy + 6, cx + 34, cy - 6, E, 1.0))
    o.append(_line(cx - 6, cy + 6, cx - 6, cy + 40, E, 1.0))
    o.append(_lbl(cx + 92, cy + 74, "Hộp quy chiếu", "ts", "start"))
    # measurement points (x/r, y/r, z/r) from table 27.3
    pts = [(1, -0.99, 0.00, 0.15), (2, 0.50, -0.86, 0.15), (3, 0.50, 0.86, 0.15),
           (4, -0.45, 0.77, 0.45), (5, -0.45, -0.77, 0.45), (6, 0.89, 0.00, 0.45),
           (7, 0.33, 0.57, 0.75), (8, -0.66, 0.00, 0.75), (9, 0.33, -0.57, 0.75),
           (10, 0.00, 0.00, 1.00)]
    for n, x, y, z in pts:
        px = cx + RX * x + 0.42 * RY * y
        py = cy - ZX * z - 0.62 * RY * y
        o.append(_dot(px, py, 3.0, "#ffffff"))
        o.append(_circ(px, py, 3.0, "none", E, 1.0))
        o.append(_lbl(px + 7, py - 5, str(n), "ts", "start"))
    o.append(_lbl(cx - RX - 40, cy - ZX + 8, "Mặt đo", "ts", "middle"))
    o.append(_arr(cx - RX - 40, cy - ZX + 16, cx - RX + 10, cy - ZX + 34, S, "ah27s", 1.0))
    return _fig(svg(680, 420, "".join(o), "Các điểm đo để xác định công suất âm"),
                "Hình 27.12 · Các điểm đo để xác định công suất âm. Mười điểm phân bố trên mặt bán "
                "cầu bán kính r quanh vật đo, toạ độ chuẩn hoá theo r như trong Bảng 27.3.",
                "Figure 27.12 · Measurement points for sound power determination. Ten points are "
                "spread over a hemisphere of radius r around the test object, with coordinates "
                "normalised to r as listed in Table 27.3.",
                "Bán cầu có trục x, y, z, hộp quy chiếu ở tâm và mười điểm đo được đánh số",
                "A hemisphere with x, y, z axes, a reference box at the centre and ten numbered points")


# ================================================================ 27.13
def fig_27_13():
    o = [_defs()]
    # spacer rod with two capsules
    o.append(_line(120, 150, 470, 150, E, 3.0))
    o.append(_rect(150, 128, 44, 44, "#e7ebf1", E, 1.5, rx=4))
    o.append(_rect(300, 128, 44, 44, "#e7ebf1", E, 1.5, rx=4))
    for i in range(5):
        o.append(_line(156 + i * 8, 134, 156 + i * 8, 166, "#8c96a4", 0.8))
        o.append(_line(306 + i * 8, 134, 306 + i * 8, 166, "#8c96a4", 0.8))
    # dimension between capsules
    o.append(_line(194, 186, 194, 200, S, 1.0))
    o.append(_line(300, 186, 300, 200, S, 1.0))
    o.append(_line(194, 193, 300, 193, S, 1.0))
    o.append(_lbl(247, 212, "Δr", "ts", "middle"))
    # handle and cable
    o.append(_rect(470, 138, 70, 24, "#dfe7f2", E, 1.4, rx=3))
    o.append(_path("M540,150 q40,0 44,26 q4,26 -18,30", E, 1.3))
    o.append(_lbl(186, 110, "micro 1", "ts", "middle"))
    o.append(_lbl(322, 110, "micro 2", "ts", "middle"))
    o.append(_lbl(505, 130, "tay cầm", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Đầu dò cường độ hai micro"),
                "Hình 27.13 · Đầu dò cường độ âm hai micro: hai micro giống nhau đặt cách nhau một "
                "khoảng Δr cố định trên cùng một trục; hiệu áp giữa chúng cho phép tính vận tốc "
                "hạt theo phương của trục.",
                "Figure 27.13 · Two-microphone sound intensity probe: two matched microphones a "
                "fixed distance Δr apart on a common axis; the pressure difference between them "
                "yields the particle velocity along that axis.",
                "Hai micro cách nhau khoảng Δr trên một thanh, có tay cầm và cáp",
                "Two microphones spaced Δr apart on a rod, with a handle and cable")


# ================================================================ 27.14
def fig_27_14():
    o = [_defs()]
    for cx, tag, lab in ((170, "(a)", "v"), (470, "(b)", "v = 0")):
        o.append(_dot(cx, 120, 7))
        for r in (34, 50, 66, 82):
            a1, a2 = _m.radians(-52), _m.radians(52)
            o.append(_path("M%s,%s A%s,%s 0 0 1 %s,%s"
                           % (_f(cx + r * _m.cos(a1)), _f(120 + r * _m.sin(a1)),
                              _f(r), _f(r),
                              _f(cx + r * _m.cos(a2)), _f(120 + r * _m.sin(a2))), E, 1.1))
        if tag == "(a)":
            o.append(_darr(cx + 74, 120, cx + 124, 120, G, 1.6))
            o.append(_lbl(cx + 99, 108, "v", "tb", "middle"))
        else:
            o.append(_darr(cx + 92, 84, cx + 92, 156, G, 1.6))
            o.append(_lbl(cx + 104, 92, "v = 0", "tb", "start"))
        o.append(_lbl(cx + 40, 214, tag, "tb", "middle"))
    o.append(_lbl(320, 30, "Nguồn điểm", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Vận tốc hạt theo và vuông góc phương truyền"),
                "Hình 27.14 · Vận tốc hạt (a) dọc theo phương truyền — cho cường độ bức xạ ra xa "
                "nguồn; và (b) vuông góc với phương truyền — bằng không, nên cường độ tính theo "
                "hướng đó cũng bằng không.",
                "Figure 27.14 · Particle velocity (a) along the direction of propagation, giving "
                "intensity radiated away from the source; and (b) perpendicular to it, which is "
                "zero, so the intensity in that direction is zero too.",
                "Hai nguồn điểm phát sóng, một có mũi tên v dọc tia, một có mũi tên v bằng 0",
                "Two point sources radiating, one with v along the ray, one with v equal to zero")


# ================================================================ 27.15
def fig_27_15():
    o = [_defs()]
    # (a) temporal
    o.append(_lbl(120, 22, "Tần số thời gian", "tb", "middle"))
    o.append(_line(50, 96, 214, 96, E, 1.3))
    o.append(_line(50, 96, 50, 40, E, 1.3))
    pts = []
    for i in range(0, 121):
        u = i / 120.0
        pts.append((50 + u * 158, 68 - 20 * _m.sin(u * 4 * _m.pi)))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts), E, 1.5))
    o.append(_lbl(218, 100, "t", "ts", "start"))
    o.append(_arr(120, 110, 120, 136, S, "ah27s", 1.2))
    o.append(_lbl(132, 128, "ℱ", "tb", "start"))
    o.append(_line(50, 190, 214, 190, E, 1.3))
    o.append(_line(50, 190, 50, 140, E, 1.3))
    pk = [(50 + i, 190 - 46 * _m.exp(-((i - 78) ** 2) / 90.0)) for i in range(0, 165)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pk), E, 1.5))
    o.append(_lbl(218, 194, "f", "ts", "start"))
    o.append(_lbl(120, 214, "(a)", "tb", "middle"))
    # (b) spatial
    o.append(_lbl(470, 22, "Tần số không gian", "tb", "middle"))
    o.append(_lbl(470, 36, "(số sóng)", "ts", "middle"))
    o.append(_line(390, 96, 560, 96, E, 1.3))
    o.append(_line(390, 96, 390, 40, E, 1.3))
    for k in range(5):
        x0 = 396 + k * 36
        o.append(_path("M%s,60 L%s,60" % (_f(x0), _f(x0 + 28)), E, 1.2))
        o.append(_path("M%s,60 q7,-9 14,0 q7,9 14,0" % (_f(x0 + 4), ), E, 1.2))
    o.append(_lbl(566, 100, "l", "ts", "start"))
    o.append(_arr(470, 110, 470, 136, S, "ah27s", 1.2))
    o.append(_lbl(482, 128, "ℱ", "tb", "start"))
    o.append(_line(390, 190, 560, 190, E, 1.3))
    o.append(_line(390, 190, 390, 140, E, 1.3))
    pk2 = [(390 + i, 190 - 46 * _m.exp(-((i - 92) ** 2) / 90.0)) for i in range(0, 165)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pk2), E, 1.5))
    o.append(_lbl(566, 194, "k", "ts", "start"))
    o.append(_lbl(470, 214, "(b)", "tb", "middle"))
    return _fig(svg(680, 236, "".join(o), "Tần số thời gian và tần số không gian của sóng phẳng"),
                "Hình 27.15 · Tần số thời gian và tần số không gian của sóng phẳng: (a) biến thiên "
                "áp theo thời gian tại một điểm cho phổ theo f; (b) biến thiên áp theo vị trí dọc "
                "trục l tại một thời điểm cho phổ theo số sóng k.",
                "Figure 27.15 · Temporal and spatial frequency of a plane wave: (a) pressure against "
                "time at one point gives a spectrum in f; (b) pressure against position along an "
                "axis l at one instant gives a spectrum in wavenumber k.",
                "Bốn ô: dạng sóng theo thời gian, phổ theo f, mặt sóng theo l, phổ theo k",
                "Four panels: waveform vs time, spectrum vs f, wavefronts along l, spectrum vs k")


# ================================================================ 27.16
def fig_27_16():
    o = [_defs()]
    for cx, tag, slope in ((190, "(a)", 0.0), (490, "(b)", 0.42)):
        o.append(_line(cx - 110, 40, cx + 110, 40 + slope * 220, E, 1.2))
        for k in range(6):
            x0 = cx - 100 + k * 38
            y0 = 46 + slope * (k * 38)
            o.append(_path("M%s,%s q10,-14 20,0 q10,14 20,0" % (_f(x0), _f(y0)), E, 1.2))
        o.append(_arr(cx - 120, 96, cx - 120, 40, S, "ah27s", 1.1))
        o.append(_lbl(cx - 128, 92, "k", "ts", "end"))
        o.append(_arr(cx - 104, 40, cx + 96, 40 + slope * 200, S, "ah27s", 1.1))
        o.append(_lbl(cx + 100, 46 + slope * 200, "l", "ts", "start"))
        o.append(_lbl(cx, 190, tag, "tb", "middle"))
    # spectra underneath
    o.append(_line(80, 260, 300, 260, E, 1.2))
    o.append(_line(80, 260, 80, 214, E, 1.2))
    p1 = [(80 + i, 260 - 40 * _m.exp(-((i - 110) ** 2) / 70.0)) for i in range(0, 210)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in p1), E, 1.5))
    o.append(_lbl(306, 264, "k", "ts", "start"))
    o.append(_lbl(190, 288, "(a) một đỉnh tại k", "ts", "middle"))
    o.append(_line(380, 260, 600, 260, E, 1.2))
    o.append(_line(380, 260, 380, 214, E, 1.2))
    p2 = [(380 + i, 260 - 34 * _m.exp(-((i - 96) ** 2) / 110.0)) for i in range(0, 210)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in p2), E, 1.5))
    o.append(_lbl(606, 264, "k", "ts", "start"))
    o.append(_lbl(490, 288, "(b) đỉnh tại k·cos 45°", "ts", "middle"))
    return _fig(svg(680, 300, "".join(o), "Tần số không gian của sóng truyền theo hướng khác nhau"),
                "Hình 27.16 · Tần số không gian của sóng truyền theo các hướng khác nhau: (a) sóng "
                "truyền dọc trục đo cho đỉnh tại k; (b) sóng tới 45° cho đỉnh tại k·cos45°.",
                "Figure 27.16 · Spatial frequencies of waves propagating in different directions: "
                "(a) a wave along the measurement axis gives a peak at k; (b) a wave at 45° gives a "
                "peak at k·cos 45°.",
                "Hai cặp: mặt sóng và phổ không gian, đỉnh dịch khi sóng xiên",
                "Two pairs: wavefronts and spatial spectrum, the peak shifting for an oblique wave")


# ================================================================ 27.17
def fig_27_17():
    o = [_defs()]
    # wave 1: oblique stripes with its own spectrum above
    o.append(_line(60, 130, 200, 130, E, 1.1))
    o.append(_line(60, 130, 60, 92, E, 1.1))
    p = [(60 + i, 130 - 26 * _m.exp(-((i - 62) ** 2) / 60.0)) for i in range(0, 140)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in p), E, 1.4))
    o.append(_lbl(206, 134, "k", "ts", "start"))
    for k in range(6):
        o.append(_line(60 + k * 22, 196, 104 + k * 22, 152, E, 1.2))
    # wave 2: zigzag with its own spectrum below
    o.append(_line(60, 330, 200, 330, E, 1.1))
    o.append(_line(60, 330, 60, 292, E, 1.1))
    p2 = [(60 + i, 330 - 26 * _m.exp(-((i - 88) ** 2) / 60.0)) for i in range(0, 140)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in p2), E, 1.4))
    o.append(_lbl(206, 334, "k", "ts", "start"))
    zz = []
    for i in range(0, 120, 12):
        zz.append((60 + i, 420 - (16 if (i // 12) % 2 == 0 else 0)))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in zz), E, 1.4))
    # arrows to the right: sum
    o.append(_arr(240, 250, 380, 250, E, "ah27", 1.4))
    o.append(_arr(240, 380, 380, 330, E, "ah27", 1.4))
    # combined spectrum
    o.append(_line(400, 250, 620, 250, E, 1.2))
    o.append(_line(400, 250, 400, 190, E, 1.2))
    c1 = [(400 + i, 250 - 34 * _m.exp(-((i - 62) ** 2) / 50.0)) for i in range(0, 210)]
    c2 = [(400 + i, 250 - 44 * _m.exp(-((i - 132) ** 2) / 50.0)) for i in range(0, 210)]
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in c1), E, 1.4))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in c2), E, 1.4))
    o.append(_lbl(626, 254, "k", "ts", "start"))
    # combined wave
    comb = []
    for i in range(0, 200):
        y = 380 - 18 * _m.sin(i / 9.0) - 12 * _m.sin(i / 4.2 + 1.0)
        comb.append((400 + i, y))
    o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in comb), E, 1.3))
    o.append(_lbl(510, 470, "tổng của hai sóng", "ts", "middle"))
    return _fig(svg(680, 490, "".join(o), "Phổ không gian của hai sóng truyền khác hướng"),
                "Hình 27.17 · Phổ không gian của hai sóng truyền theo hai hướng khác nhau. Mỗi sóng "
                "riêng lẻ cho một đỉnh; trường tổng cho phổ có hai đỉnh, mỗi đỉnh ứng với một hướng "
                "truyền.",
                "Figure 27.17 · Spatial spectrum of two waves propagating in different directions. "
                "Each wave alone gives one peak; the summed field gives a spectrum with two peaks, "
                "one per propagation direction.",
                "Hai sóng riêng với phổ một đỉnh, mũi tên dẫn tới phổ tổng hai đỉnh",
                "Two separate waves with single-peak spectra, arrows leading to a two-peak sum spectrum")


# ================================================================ 27.18
def fig_27_18():
    o = [_defs()]
    # hatched blocks at both ends
    o.append(_poly([(30, 120), (86, 120), (86, 300), (30, 320)], "url(#hatch27)", E, 1.4))
    o.append(_poly([(560, 120), (620, 120), (620, 320), (560, 300)], "url(#hatch27)", E, 1.4))
    # planes
    o.append(_line(250, 60, 250, 330, E, 2.0))
    o.append(_line(390, 60, 390, 330, E, 2.0, "6 5"))
    o.append(_lbl(250, 50, "Mặt quét", "ts", "middle"))
    o.append(_lbl(390, 50, "Mặt mới", "ts", "middle"))
    # three waves of different frequency crossing the planes
    for y, per, amp in ((140, 150, 16), (210, 74, 13), (285, 34, 11)):
        pts = []
        for i in range(0, 161):
            x = 96 + i * 1.0
            pts.append((x, y - amp * _m.sin((x - 96) / per * 2 * _m.pi)))
        o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts), E, 1.3))
    # transformation arrows
    o.append(_arr(96, 110, 150, 100, S, "ah27s", 1.1))
    o.append(_arr(500, 100, 556, 112, S, "ah27s", 1.1))
    o.append(_arr(96, 320, 150, 330, S, "ah27s", 1.1))
    o.append(_arr(500, 330, 556, 318, S, "ah27s", 1.1))
    return _fig(svg(680, 350, "".join(o), "Biến đổi các kiểu sóng trong phổ không gian"),
                "Hình 27.18 · Biến đổi các kiểu sóng đơn giản trong phổ không gian, từ mặt đo này "
                "sang mặt khác. Sóng phẳng chỉ dịch pha khi truyền, còn sóng tắt dần (evanescent) "
                "thì biên độ giảm dần theo khoảng cách.",
                "Figure 27.18 · Transformation of simple wave types in a spatial spectrum, from one "
                "measurement plane to another. Plane waves only shift phase in propagating, while "
                "evanescent waves decay in amplitude with distance.",
                "Hai mặt phẳng song song, ba sóng có tần số khác nhau băng qua",
                "Two parallel planes with three waves of different frequency crossing them")


# ================================================================ 27.19
def fig_27_19():
    o = [_defs()]
    o.append(_rect(30, 150, 62, 54, "#f4f6f9", E, 1.4, rx=3))
    o.append(_lbl(61, 224, "Nguồn ồn", "ts", "middle"))
    # (a) scan plane
    o.append(_poly([(140, 110), (196, 110), (196, 250), (140, 268)], "url(#hatch27)", E, 1.4))
    o.append(_lbl(168, 100, "(a)", "ts", "middle"))
    # (b) spectra
    for i, yy in enumerate((120, 168, 216)):
        o.append(_line(216, yy, 300, yy, E, 1.1))
        o.append(_line(216, yy, 216, yy - 26, E, 1.1))
        pk = [(216 + j, yy - 22 * _m.exp(-((j - 42) ** 2) / 40.0)) for j in range(0, 84)]
        o.append(_path("M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pk), E, 1.2))
        o.append(_arr(300, yy, 330, 168, S, "ah27s", 1.0))
    o.append(_lbl(258, 100, "(b)", "ts", "middle"))
    # (c) transform planes
    for i in range(3):
        o.append(_poly([(360 + i * 26, 140), (404 + i * 26, 140),
                        (404 + i * 26, 260), (360 + i * 26, 260)], "url(#hatch27)", E, 1.2))
    o.append(_arr(330, 200, 356, 200, S, "ah27s", 1.1))
    o.append(_lbl(420, 130, "2D-FFT", "tb", "middle"))
    o.append(_arr(470, 200, 520, 232, S, "ah27s", 1.1))
    o.append(_lbl(430, 288, "Các mặt biến đổi", "ts", "middle"))
    o.append(_lbl(462, 116, "(c)", "ts", "middle"))
    # (d) inverse transform
    o.append(_poly([(530, 232), (574, 232), (574, 320), (530, 336)], "url(#hatch27)", E, 1.4))
    o.append(_lbl(552, 356, "Kết quả", "ts", "middle"))
    o.append(_lbl(600, 226, "FFT⁻¹", "tb", "middle"))
    o.append(_lbl(600, 242, "(d)", "ts", "middle"))
    return _fig(svg(680, 380, "".join(o), "Nguyên lý tổng thể của NAH"),
                "Hình 27.19 · Nguyên lý tổng thể của NAH: (a) đo phổ chéo trên mặt quét; (b) tính "
                "cho từng tần số thời gian; (c) biến đổi Fourier không gian hai chiều; (d) biến đổi "
                "ngược để thu trường âm trên mặt mới.",
                "Figure 27.19 · Overall principle of NAH: (a) measurement of cross-spectra in the "
                "scan plane; (b) calculation for one temporal frequency at a time; (c) two-dimensional "
                "spatial Fourier transform; (d) inverse transform to obtain the sound field in the "
                "new plane.",
                "Sơ đồ khối: nguồn ồn, mặt quét, phổ, các mặt biến đổi, kết quả",
                "Block diagram: noise source, scan plane, spectra, transform planes, result")


# ================================================================ 27.20
def fig_27_20():
    o = [_defs()]
    o.append(_rect(240, 130, 120, 190, "#2a2a2a", E, 1.4, rx=6))
    o.append(_rect(268, 42, 64, 92, "#c9ced6", E, 1.4, rx=4))
    o.append('<ellipse cx="300" cy="42" rx="32" ry="8" fill="#e7ebf1" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append(_circ(300, 196, 7, "none", E, 1.2))
    o.append(_lbl(300, 220, "I / O", "ts", "middle"))
    o.append(_lbl(300, 348, "Pistonphone (nguồn âm chuẩn)", "ts", "middle"))
    o.append(_lbl(384, 90, "khoang chuẩn", "ts", "start"))
    o.append(_arr(384, 96, 340, 90, S, "ah27s", 1.0))
    return _fig(svg(680, 370, "".join(o), "Pistonphone dùng hiệu chuẩn micro"),
                "Hình 27.20 · Pistonphone dùng để hiệu chuẩn micro. Đây là nguồn âm rất ổn định, tạo "
                "mức áp suất xác định bên trong một khoang kín nhờ dịch chuyển thể tích của pit-tông.",
                "Figure 27.20 · Pistonphone for microphone calibration. It is a very stable sound "
                "source producing a well-defined sound pressure inside a closed cavity by piston "
                "volume displacement.",
                "Thiết bị hiệu chuẩn hình hộp đen có đầu xy-lanh bạc ở trên",
                "A black box-shaped calibrator with a silver cylinder on top")


# ================================================================ 27.21
def fig_27_21():
    o = [_defs()]
    # cavity
    o.append(_path("M180,110 H470 V210 H180", E, 1.6))
    o.append(_line(180, 110, 180, 210, E, 1.6))
    # test microphone inserted at the left
    o.append(_rect(96, 128, 84, 44, "#f4f6f9", E, 1.4, rx=3))
    o.append(_path("M96,150 q-30,0 -46,-14", E, 1.3))
    o.append(_lbl(138, 118, "Micro cần hiệu chuẩn", "ts", "middle"))
    # piston at the right
    o.append(_rect(470, 140, 46, 26, "#cfd8e6", E, 1.4, rx=2))
    o.append(_rect(516, 146, 60, 14, "#e7ebf1", E, 1.2, rx=2))
    o.append(_lbl(540, 182, "Pit-tông", "ts", "middle"))
    o.append(_darr(560, 128, 590, 128, G, 1.4))
    o.append(_lbl(575, 118, "X", "tb", "middle"))
    o.append(_lbl(470, 96, "ΔV", "tb", "middle"))
    o.append(_arr(470, 104, 448, 120, S, "ah27s", 1.0))
    o.append(_lbl(320, 238, "Thể tích thử", "ts", "middle"))
    o.append(_arr(320, 226, 320, 212, S, "ah27s", 1.0))
    return _fig(svg(680, 260, "".join(o), "Nguyên lý của pistonphone"),
                "Hình 27.21 · Nguyên lý của pistonphone: pit-tông dịch chuyển tuần hoàn một thể tích "
                "ΔV xác định trong khoang kín, làm thay đổi áp suất trong thể tích thử và tạo ra "
                "mức âm chuẩn tại micro cần hiệu chuẩn.",
                "Figure 27.21 · Principle of a pistonphone: the piston displaces a defined volume ΔV "
                "cyclically inside a closed cavity, changing the pressure in the test volume and so "
                "generating a reference sound level at the microphone under calibration.",
                "Micro gắn bên trái khoang, pit-tông bên phải với mũi tên ΔV và X",
                "Microphone at the left of the cavity, piston at the right with ΔV and X arrows")


# ================================================================ registry

FIGS = [fig_27_1(), fig_27_2(), fig_27_3(), fig_27_4(), fig_27_5(),
        fig_27_6(), fig_27_7(), fig_27_8(), fig_27_9(), fig_27_10(),
        fig_27_11(), fig_27_12(), fig_27_13(), fig_27_14(), fig_27_15(),
        fig_27_16(), fig_27_17(), fig_27_18(), fig_27_19(), fig_27_20(),
        fig_27_21()]


def fig(n):
    return FIGS[n - 1]
