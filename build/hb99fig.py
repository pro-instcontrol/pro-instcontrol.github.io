# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 99 — Electropneumatic and Electrohydraulic
Instruments: Modeling of Electrohydraulic and Electrohydrostatic Actuators
(M. Pachter and C. H. Houpis, Air Force Institute of Technology).

The source has ten figures (99.1–99.10). 99.1, 99.5, 99.6 and 99.7 are
mechanical drawings and are redrawn here as schematics that keep every
labelled quantity; the block diagrams are redrawn block for block.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _rich().
"""
import math

from hbfig import _f, svg, _fig

E = "#2a2a2a"
S = "#888888"
GRID = "#e4e4e4"
GOLD = "#b45309"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="t"):
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7" dy="2.4">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.4">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="s%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<style>.tl{font:9.5px Inter,Helvetica,sans-serif;fill:#555}'
            '.tm{font:9px Inter,Helvetica,sans-serif;fill:#333}'
            '.tf{font:9.5px Inter,Helvetica,sans-serif;fill:#555;font-style:italic}'
            '</style></defs>' % (tag, E, tag, S))


def _line(x1, y1, x2, y2, sw=1.4, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="99", sw=1.3, col=E):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, tag))


def _sarr(x1, y1, x2, y2, tag="99", sw=1.1):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#s%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), S, sw, tag))


def _rect(x, y, w, h, sw=1.3, fill="#fff", dash="", rx=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    r = ' rx="%s"' % _f(rx) if rx else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), r, fill, E, sw, d))


def _blk(x, y, w, h, parts, fs=None, dash=""):
    """Block with centred text. parts is a list of lines, each a str or a
    list of (txt, is_sub) tuples."""
    o = [_rect(x, y, w, h, 1.3, "#fff", dash)]
    n = len(parts)
    for i, ln in enumerate(parts):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 13 + 3.6
        if isinstance(ln, list):
            if all(isinstance(t, str) for t in ln):
                ln = " ".join(ln)
                o.append(_lbl(x + w / 2.0, cy, ln, "tm", "middle"))
            else:
                o.append(_rich(x + w / 2.0, cy, ln, "middle", "tm"))
        else:
            o.append(_lbl(x + w / 2.0, cy, ln, "tm", "middle"))
    return "".join(o)


def _frac(x, y, w, h, num, den, fs=None):
    """Block showing num/den with a rule between them."""
    o = [_rect(x, y, w, h, 1.3)]
    my = y + h / 2.0
    o.append(_line(x + 4, my, x + w - 4, my, 1.1))
    if isinstance(num, list):
        o.append(_rich(x + w / 2.0, my - 4, num, "middle", "tm"))
    else:
        o.append(_lbl(x + w / 2.0, my - 4, num, "tm", "middle"))
    if isinstance(den, list):
        o.append(_rich(x + w / 2.0, my + 11, den, "middle", "tm"))
    else:
        o.append(_lbl(x + w / 2.0, my + 11, den, "tm", "middle"))
    return "".join(o)


def _sum(cx, cy, r=9, signs=None, tag="99"):
    """Summing junction; signs is a dict like {'l':'+','b':'-','t':'+'}."""
    o = ['<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="1.3"/>'
         % (_f(cx), _f(cy), _f(r), E)]
    if signs:
        pos = {"l": (cx - r - 10, cy - 5), "r": (cx + r + 3, cy - 5),
               "t": (cx - 2.5, cy - r - 5), "b": (cx + 5, cy + r + 11)}
        for k, s in signs.items():
            x, y = pos[k]
            o.append(_lbl(x, y, s, "tm"))
    return "".join(o)


def _hatch(x1, y1, x2, y2, n=7):
    """Hatching for a fixed support / ground line."""
    o = [_line(x1, y1, x2, y1, 1.4)]
    step = (x2 - x1) / float(n)
    for i in range(n):
        xa = x1 + i * step + step * 0.25
        o.append(_line(xa, y1, xa - step * 0.5, y1 + 9, 1.0, S))
    return "".join(o)


def _bode(x, y, w, h, xr, xt, xtl, y1r, y1t, y2r, y2t,
          xlab, y1lab, y2lab, curves):
    """Two-panel Bode plot.  x is a log axis in rad/s: xr = (log10 fmin,
    log10 fmax).  Magnitude panel sits at (x, y, w, h); the phase panel sits
    h + GAP below it.  curves = [(f(s), dash, label), ...]; dash "+" draws
    sampled markers instead of a line."""
    GAP = 62
    o = []
    x0, x1 = xr
    span = float(x1 - x0)

    def X(f):
        return x + (math.log10(f) - x0) * w / span

    def Y1(v):
        return y + h - (v - y1r[0]) * h / float(y1r[1] - y1r[0])

    def Y2(v):
        return y + h + GAP + h - (v - y2r[0]) * h / float(y2r[1] - y2r[0])

    def xname(d):
        if d >= 0:
            return str(10 ** d)
        return "0," + "0" * (-d - 1) + "1"

    # decade grid + tick labels
    for d in range(int(math.floor(x0)), int(math.ceil(x1)) + 1):
        xx = X(10 ** d)
        if not (x - 0.5 <= xx <= x + w + 0.5):
            continue
        o.append(_line(xx, y, xx, y + h, 0.8, GRID))
        o.append(_line(xx, y + h + GAP, xx, y + 2 * h + GAP, 0.8, GRID))
        o.append(_lbl(xx, y + h + 13, xname(d), "tm", "middle"))
        o.append(_lbl(xx, y + 2 * h + GAP + 13, xname(d), "tm", "middle"))

    # horizontal grids + value labels
    for v in y1t:
        yy = Y1(v)
        o.append(_line(x, yy, x + w, yy, 0.8, GRID))
        o.append(_lbl(x - 7, yy + 3.4, str(v), "tm", "end"))
    for v in y2t:
        yy = Y2(v)
        o.append(_line(x, yy, x + w, yy, 0.8, GRID))
        o.append(_lbl(x - 7, yy + 3.4, str(v), "tm", "end"))

    # frames
    for top in (y, y + h + GAP):
        o.append(_line(x, top, x, top + h, 1.2))
        o.append(_line(x, top + h, x + w, top + h, 1.2))

    # axis titles
    o.append(_lbl(x + w / 2.0, y + 2 * h + GAP + 30, xlab, "tm", "middle"))
    for ty, lab in ((y + h / 2.0, y1lab), (y + h + GAP + h / 2.0, y2lab)):
        o.append('<text class="tm" x="%s" y="%s" text-anchor="middle" '
                 'transform="rotate(-90 %s %s)">%s</text>'
                 % (_f(x - 42), _f(ty), _f(x - 42), _f(ty), lab))

    # curves
    N = 260
    for fn, dash, _lab in curves:
        if dash == "+":
            continue
        seg = []
        for i in range(N + 1):
            f = 10 ** (x0 + span * i / float(N))
            g = fn(1j * f)
            seg.append((f, 20 * math.log10(max(1e-6, abs(g))),
                        math.degrees(math.atan2(g.imag, g.real))))
        # unwrap phase so it descends monotonically across the sweep
        ph, out = [seg[0][2]], []
        for _f_, _m_, _p in seg[1:]:
            p = _p
            while p - ph[-1] > 180:
                p -= 360
            while p - ph[-1] < -180:
                p += 360
            ph.append(p)
        for (f, m, _p), p in zip(seg, ph):
            out.append((X(f), Y1(max(y1r[0], min(y1r[1], m))),
                        Y2(max(y2r[0], min(y2r[1], p)))))
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        for k in (1, 2):
            pts = " ".join("%s,%s" % (_f(p[0]), _f(p[k])) for p in out)
            o.append('<polyline points="%s" fill="none" stroke="%s" '
                     'stroke-width="1.5"%s/>' % (pts, E, d))
    return "".join(o)


# ---------------------------------------------------------------- 99.1
def fig_99_1():
    o = [_defs("99")]
    # fixed pivot, top left
    o.append(_hatch(34, 66, 96, 66, 6))
    o.append(_line(96, 66, 96, 210, 2.2))
    o.append('<circle cx="96" cy="66" r="3" fill="%s"/>' % E)
    o.append('<circle cx="96" cy="120" r="2.6" fill="%s"/>' % E)
    o.append('<circle cx="96" cy="150" r="2.6" fill="%s"/>' % E)
    o.append('<circle cx="96" cy="210" r="2.6" fill="%s"/>' % E)
    # input
    o.append(_arr(48, 30, 84, 54))
    o.append(_rich(90, 34, [("δ", False), ("ec", True)], "start", "tm"))
    o.append(_lbl(78, 124, "a", "tm", "end"))
    o.append(_lbl(78, 214, "b", "tm", "end"))
    # servo valve
    o.append(_rect(250, 92, 184, 60, 1.4))
    o.append(_rect(300, 100, 18, 44, 1.2, "#e8e8e8"))
    o.append(_rect(370, 100, 18, 44, 1.2, "#e8e8e8"))
    o.append(_line(318, 122, 370, 122, 1.4))
    o.append(_lbl(342, 84, "Van servo", "tm", "middle"))
    o.append(_arr(300, 62, 300, 100))
    o.append(_lbl(304, 74, "Q", "tm"))
    o.append(_arr(406, 62, 406, 100))
    o.append(_lbl(410, 74, "Hồi", "tm"))
    # spool link
    o.append(_line(96, 120, 250, 120, 1.4))
    o.append(_rich(200, 114, [("x", False), ("v", True)], "middle", "tm"))
    # ports down to the cylinder
    o.append(_line(300, 152, 300, 178, 1.4))
    o.append(_line(406, 152, 406, 178, 1.4))
    o.append(_lbl(286, 172, "A", "tm", "end"))
    o.append(_lbl(420, 172, "B", "tm"))
    # cylinder
    o.append(_rect(250, 178, 230, 60, 1.5))
    o.append(_rect(300, 182, 22, 52, 1.3, "#e8e8e8"))
    o.append(_line(322, 208, 480, 208, 2.2))
    o.append(_rich(400, 200, [("x", False), ("p", True)], "middle", "tm"))
    o.append(_arr(430, 226, 470, 226))
    # feedback link below the cylinder
    o.append(_line(540, 300, 540, 336, 1.4))
    o.append(_line(540, 336, 56, 336, 1.4))
    o.append(_line(56, 336, 56, 150, 1.4))
    o.append(_arr(56, 150, 92, 150))
    o.append(_lbl(46, 146, "c", "tm", "end"))
    o.append(_rich(150, 214, [("x", False), ("1", True)], "middle", "tm"))
    o.append(_arr(120, 232, 156, 232))
    # output arm d, e
    o.append(_line(480, 208, 480, 300, 1.4))
    o.append(_line(480, 300, 570, 300, 1.4))
    o.append(_lbl(524, 294, "d", "tm", "middle"))
    o.append('<circle cx="570" cy="300" r="3" fill="%s"/>' % E)
    o.append(_hatch(552, 312, 588, 312, 3))
    o.append(_line(570, 300, 570, 312, 1.2))
    o.append(_line(570, 300, 660, 268, 1.4))
    o.append(_lbl(610, 278, "e", "tm", "middle"))
    # control surface
    o.append('<path d="M660 268 L758 246 L760 262 L664 284 Z" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.3"/>' % E)
    o.append(_line(660, 276, 760, 254, 0.9, S, "4 3"))
    o.append('<path d="M700 300 A 44 44 0 0 0 716 272" fill="none" stroke="%s" '
             'stroke-width="1.0" marker-end="url(#a99)"/>' % E)
    o.append(_rich(722, 296, [("δ", False), ("e", True)], "start", "tm"))
    o.append(_lbl(300, 356, "Liên kết phản hồi", "tf", "middle"))
    return _fig(svg(800, 380, "".join(o),
                    "Sơ đồ hệ điều khiển không hồi tiếp: cần vào, van servo, xi lanh thuỷ lực và tay đòn ra"),
                "Hình 99.1 · Hệ điều khiển không hồi tiếp. Cần vào quay quanh điểm tựa, dịch van servo một đoạn "
                "x<sub>v</sub>; pittông chạy x<sub>p</sub>; liên kết phản hồi dài c đưa x<sub>f</sub> về cần, "
                "còn tay đòn d–e biến chuyển vị thành góc lái δ<sub>e</sub>.",
                "Figure 99.1 · Irreversible control system. The input lever turns about its pivot and "
                "displaces the servo valve by x<sub>v</sub>; the piston moves x<sub>p</sub>; the feedback "
                "linkage of length c returns x<sub>f</sub> to the lever, and the d–e arm turns the "
                "displacement into the surface angle δ<sub>e</sub>.",
                "Sơ đồ cơ khí của hệ điều khiển không hồi tiếp: cần vào, van servo, xi lanh và tay đòn",
                "Mechanical schematic: input lever, servo valve, cylinder and output arm")


# ---------------------------------------------------------------- 99.2
def _sig(x, y, parts, anchor="start"):
    return _rich(x, y, parts, anchor, "tm")


def fig_99_2():
    o = [_defs("99")]

    # ---------------- (a) actuator block diagram
    y = 56
    o.append(_sig(22, y + 4, [("δ", False), ("ec", True), ("(s)", False)]))
    o.append(_arr(92, y, 116, y))
    o.append(_blk(116, y - 14, 36, 28, ["a"]))
    o.append(_arr(152, y, 186, y))
    o.append(_sig(160, y - 8, [("x", False), ("1", True)]))
    o.append(_blk(186, y - 18, 66, 36, [["b + c"], ["b"]]))
    o.append(_arr(252, y, 292, y))
    o.append(_sum(302, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(312, y, 372, y))
    o.append(_sig(378, y + 4, [("x", False), ("v", True)]))
    # feedback: x_f -> c/b -> up into the junction
    o.append(_blk(272, y + 30, 60, 32, [["c"], ["b"]]))
    o.append(_arr(302, y + 30, 302, y + 12))
    o.append(_sig(352, y + 38, [("x", False), ("f", True)]))
    o.append(_arr(400, y + 46, 334, y + 46))
    o.append(_lbl(560, y + 4, "(a)", "tb"))

    # ---------------- (b) feedback control system
    y = 176
    o.append(_sig(22, y + 4, [("δ", False), ("ec", True), ("(s)", False)]))
    o.append(_arr(92, y, 112, y))
    o.append(_blk(112, y - 14, 34, 28, ["a"]))
    o.append(_arr(146, y, 180, y))
    o.append(_sig(150, y - 8, [("x", False), ("1", True)]))
    o.append(_blk(180, y - 18, 66, 36, [["b + c"], ["b"]]))
    o.append(_arr(246, y, 284, y))
    o.append(_sum(294, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(304, y, 330, y))
    o.append(_sig(306, y - 9, [("x", False), ("v", True)]))
    o.append(_blk(330, y - 14, 32, 28, ["K"]))
    o.append(_arr(362, y, 388, y))
    o.append(_sig(364, y - 9, [("Q", False)]))
    o.append(_blk(388, y - 18, 40, 36, [["1"], ["As"]]))
    o.append(_arr(428, y, 454, y))
    o.append(_sig(430, y - 9, [("x", False), ("p", True)]))
    o.append(_blk(454, y - 18, 64, 36, [["1"], ["d + e"]]))
    o.append(_arr(518, y, 580, y))
    o.append(_sig(588, y + 4, [("δ", False), ("e", True), ("(s)", False)]))
    # feedback: delta_e -> e -> x_f -> c/b -> up into the junction
    o.append(_line(548, y, 548, y + 70, 1.3))
    o.append(_line(548, y + 70, 494, y + 70, 1.3))
    o.append(_blk(442, y + 54, 52, 32, ["e"]))
    o.append(_arr(442, y + 70, 414, y + 70))
    o.append(_sig(420, y + 60, [("x", False), ("f", True)]))
    o.append(_blk(328, y + 54, 60, 32, [["c"], ["b"]]))
    o.append(_arr(328, y + 70, 300, y + 70))
    o.append(_line(294, y + 70, 294, y + 10, 1.3))
    o.append(_lbl(620, y + 4, "(b)", "tb"))

    # ---------------- (c) simplified
    y = 312
    o.append(_sig(22, y + 4, [("δ", False), ("ec", True), ("(s)", False)]))
    o.append(_arr(92, y, 112, y))
    o.append(_blk(112, y - 18, 176, 36, []))
    o.append(_sig(118, y + 4, [("F", False), ("A", True), ("(s) = (b + c)", False)]))
    o.append(_lbl(262, y - 2, "a", "tm", "middle"))
    o.append(_lbl(262, y + 14, "b", "tm", "middle"))
    o.append(_line(252, y + 2, 272, y + 2, 1.0))
    o.append(_arr(288, y, 320, y))
    o.append(_sum(330, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(340, y, 366, y))
    o.append(_rect(366, y - 42, 190, 84, 1.1, "none", "5 4"))
    o.append(_blk(374, y - 26, 82, 52, [["K"], ["A(d + e)"]]))
    o.append(_arr(456, y, 486, y))
    o.append(_blk(486, y - 20, 46, 40, [["1"], ["s"]]))
    o.append(_arr(532, y, 590, y))
    o.append(_sig(598, y + 4, [("δ", False), ("e", True), ("(s)", False)]))
    o.append(_lbl(568, y - 52, "G(s)", "tb"))
    o.append(_sarr(560, y - 48, 540, y - 43))
    # H(s) = ce/b
    o.append(_line(560, y, 560, y + 74, 1.3))
    o.append(_line(560, y + 74, 492, y + 74, 1.3))
    o.append(_blk(366, y + 56, 126, 36, []))
    o.append(_lbl(374, y + 80, "H(s) =", "tm"))
    o.append(_lbl(452, y + 74, "ce", "tm", "middle"))
    o.append(_line(438, y + 78, 466, y + 78, 1.1))
    o.append(_lbl(452, y + 90, "b", "tm", "middle"))
    o.append(_arr(366, y + 74, 336, y + 74))
    o.append(_line(330, y + 74, 330, y + 10, 1.3))
    o.append(_lbl(640, y + 4, "(c)", "tb"))

    return _fig(svg(700, 440, "".join(o),
                    "Ba sơ đồ khối của cơ cấu chấp hành: sơ đồ khối, sơ đồ có vòng phản hồi và sơ đồ rút gọn"),
                "Hình 99.2 · (a) Sơ đồ khối của cơ cấu chấp hành; (b) sơ đồ khối của hệ điều khiển phản hồi "
                "cơ cấu chấp hành; (c) sơ đồ khối rút gọn, trong đó G(s) = K/[A(d + e)s] và "
                "H(s) = ce/b.",
                "Figure 99.2 · (a) Actuator block diagram; (b) block diagram of the actuator feedback "
                "control system; (c) simplified block diagram, in which G(s) = K/[A(d + e)s] and "
                "H(s) = ce/b.",
                "Ba sơ đồ khối xếp chồng: sơ đồ ban đầu, sơ đồ có vòng phản hồi, và sơ đồ rút gọn",
                "Three stacked block diagrams: open diagram, feedback diagram and simplified diagram")



# ---------------------------------------------------------------- 99.3
def fig_99_3():
    o = [_defs("99")]
    ax, ay, w, h = 110, 62, 420, 200
    o.append(_arr(ax, ay + h, ax, ay - 16))
    o.append(_line(ax, ay + h, ax + w + 40, ay + h, 1.4))
    o.append(_arr(ax + w + 40, ay + h, ax + w + 62, ay + h))
    o.append(_lbl(ax + w + 66, ay + h + 4, "t, s", "t"))
    o.append(_lbl(ax - 6, ay + h + 34, "0", "t", "end"))
    ycmd = ay + h - 62
    o.append(_line(ax, ycmd, ax + w, ycmd, 1.5, E))
    o.append(_rich(ax + w - 26, ycmd - 10, [("δ", False), ("ec", True), ("(t)", False)], "start", "tm"))
    tau, ytop = 62.0, ay + 34
    pts = []
    for i in range(0, 121):
        t = i / 120.0 * 5.0
        pts.append((ax + t * tau, ycmd - (ycmd - ytop) * (1.0 - math.exp(-t))))
    d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.9"/>' % (d, E))
    o.append(_line(ax, ytop, ax + w, ytop, 0.9, S, "5 4"))
    o.append(_rich(ax + w - 26, ytop - 8, [("δ", False), ("e", True), ("(t)", False)], "start", "tm"))
    o.append(_line(ax + tau, ay + h, ax + tau, ytop, 0.9, S, "4 3"))
    o.append(_rich(ax + tau + 6, ay + h + 18, [("τ", False)], "start", "t"))
    return _fig(svg(680, 310, "".join(o),
                    "Đáp ứng bậc thang của cơ cấu chấp hành: tín hiệu ra tiến tới giá trị xác lập theo hàm mũ"),
                "Hình 99.3 · Đáp ứng thời gian của một cơ cấu chấp hành. Với lệnh bậc thang δ<sub>ec</sub>(t), "
                "đầu ra δ<sub>e</sub>(t) tiến tới giá trị xác lập theo quy luật hàm mũ với hằng số thời gian τ.",
                "Figure 99.3 · Time response of an actuator. For a step command δ<sub>ec</sub>(t) the output "
                "δ<sub>e</sub>(t) approaches its steady value exponentially with time constant τ.",
                "Đồ thị đáp ứng bậc thang: tín hiệu vào là bậc thang, tín hiệu ra tăng theo hàm mũ",
                "Step response: step command and exponential output")


# ---------------------------------------------------------------- 99.4
def fig_99_4():
    o = [_defs("99")]
    tau = 0.05
    p4 = [0.05, 0.016, 0.013, 0.011]

    def first(s):
        return 1.0 / (1.0 + tau * s)

    def fourth(s):
        g = 1.0
        for t in p4:
            g /= (1.0 + t * s)
        return g

    o.append(_bode(110, 52, 400, 150, (0, 2), None, None,
                   (-26, 2), [0, -5, -10, -15, -20, -25],
                   (-280, 5), [0, -50, -100, -150, -200, -250],
                   "Tần số (rad/giây)", "Biên độ (dB)", "Pha (độ)",
                   [(first, "6 4", "1st"), (fourth, "", "4th")]))
    o.append(_lbl(352, 112, "bậc 1", "tm"))
    o.append(_lbl(352, 150, "bậc 4", "tm"))
    return _fig(svg(620, 470, "".join(o),
                    "So sánh đáp ứng tần số của mô hình cơ cấu chấp hành bậc một và bậc bốn"),
                "Hình 99.4 · So sánh mô hình cơ cấu chấp hành bậc một và bậc bốn. Mô hình bậc một (nét đứt) "
                "bám sát mô hình bậc bốn ở dải tần thấp, nhưng lệch pha đáng kể ở dải tần cao — đúng dải "
                "tần mà các bộ bù điều khiển bền vững hiện đại làm việc.",
                "Figure 99.4 · Comparison of first- and fourth-order actuator models. The first-order model "
                "(dashed) tracks the fourth-order one at low frequency but departs sharply in phase at the "
                "higher frequencies, which lie inside the bandwidth of modern robust compensators.",
                "Hai đồ thị Bode: biên độ và pha theo tần số, so sánh mô hình bậc một và bậc bốn",
                "Two Bode panels comparing first- and fourth-order models")


# ---------------------------------------------------------------- 99.5
def fig_99_5():
    o = [_defs("99")]
    y = 120
    o.append(_sig(20, y + 4, [("δ", False), ("ec", True)]))
    o.append(_arr(66, y, 96, y))
    o.append(_sum(106, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(116, y, 150, y))
    # ram (power cylinder)
    o.append(_rect(150, y - 24, 140, 48, 1.5))
    o.append(_lbl(220, y + 6, "Ram", "tb", "middle"))
    # electrical valve riding on the ram
    o.append(_rect(168, y - 58, 84, 24, 1.3, "#f7f7f7"))
    o.append(_lbl(210, y - 64, "Van điện", "tm", "middle"))
    o.append(_line(210, y - 34, 210, y - 24, 1.2))
    # output rod
    o.append(_line(290, y, 372, y, 2.4))
    o.append(_arr(330, y, 372, y))
    o.append(_rich(296, y - 12, [("x", False), ("p", True)], "start", "tm"))
    # control surface (airfoil) with pivot
    o.append('<path d="M372 %s C 392 %s, 448 %s, 470 %s L 424 %s Z" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.3"/>'
             % (y + 2, y - 20, y - 20, y + 4, y + 30, E))
    o.append(_line(374, y + 1, 462, y + 2, 0.9, S, "4 3"))
    o.append(_line(424, y + 30, 424, y + 44, 1.2))
    o.append(_hatch(408, y + 44, 440, y + 44, 3))
    o.append(_rich(470, y + 22, [("δ", False), ("e", True)], "start", "tm"))
    # potentiometer
    o.append(_rect(500, y - 56, 84, 32, 1.3, "#f7f7f7"))
    o.append(_lbl(542, y - 62, "Chiết áp", "tm", "middle"))
    zz, xa, xb = [], 512, 572
    step = (xb - xa) / 6.0
    zz.append("M%s %s" % (_f(xa), _f(y - 40)))
    for i in range(6):
        zz.append("L%s %s" % (_f(xa + step * (i + 0.5)), _f(y - 40 + (4 if i % 2 == 0 else -4))))
    zz.append("L%s %s" % (_f(xb), _f(y - 40)))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.2"/>' % (" ".join(zz), E))
    o.append(_arr(452, y + 2, 496, y - 34))
    # feedback loop
    o.append(_line(512, y - 24, 512, y + 96, 1.3))
    o.append(_line(512, y + 96, 106, y + 96, 1.3))
    o.append(_line(106, y + 96, 106, y + 10, 1.3))
    return _fig(svg(620, 270, "".join(o),
                    "Sơ đồ cơ cấu chấp hành điện – thuỷ lực: van điện, xi lanh thuỷ lực, cánh lái và chiết áp phản hồi"),
                "Hình 99.5 · Cơ cấu chấp hành điện – thuỷ lực. Vòng phản hồi được cơ giới hoá bằng điện: van "
                "điều khiển bằng nam châm điện, chiết áp đo góc lái của cánh, còn phần tử công suất là một xi "
                "lanh thuỷ lực.",
                "Figure 99.5 · Electrohydraulic actuator. The feedback loop is mechanised electrically: a "
                "solenoid-controlled valve, a potentiometer measuring the surface deflection, and a "
                "hydraulic cylinder as the power element.",
                "Sơ đồ khối cơ cấu chấp hành điện – thuỷ lực có vòng phản hồi bằng chiết áp",
                "Electrohydraulic actuator with potentiometer feedback")


# ---------------------------------------------------------------- 99.6
def fig_99_6():
    o = [_defs("99")]
    # damping block, hatched
    o.append(_rect(96, 152, 180, 44, 1.4, "#f7f7f7"))
    for i in range(20):
        xa = 84 + i * 11
        x1 = max(xa, 96.0)
        x2 = min(xa + 44, 276.0)
        if x2 <= x1:
            continue
        o.append(_line(x1, 196 - (x1 - xa), x2, 196 - (x2 - xa), 0.7, S))
    # stator
    o.append(_hatch(74, 216, 302, 216, 11))
    o.append(_lbl(186, 240, "Stato", "tm", "middle"))
    # rotor
    o.append(_rect(126, 64, 120, 90, 1.5))
    o.append(_lbl(186, 114, "Rôto", "tb", "middle"))
    o.append(_rich(186, 52, [("Rôto: quán tính J", False), ("m", True)], "middle", "tm"))
    # shaft
    o.append(_rect(66, 94, 60, 26, 1.3))
    o.append(_rect(246, 94, 96, 26, 1.3))
    o.append(_line(246, 107, 342, 107, 1.4))
    # opposed torque arrows on the shaft
    o.append('<path d="M254 88 Q 270 70, 288 88" fill="none" stroke="%s" '
             'stroke-width="1.2" marker-end="url(#a99)"/>' % E)
    o.append(_rich(252, 64, [("τ", False), ("cmd", True)], "start", "tm"))
    o.append('<path d="M340 88 Q 324 70, 306 88" fill="none" stroke="%s" '
             'stroke-width="1.2" marker-end="url(#a99)"/>' % E)
    o.append(_rich(302, 64, [("τ", False), ("load", True)], "start", "tm"))
    o.append(_rich(288, 176, [("Giảm chấn động cơ B", False), ("m", True)], "start", "tm"))
    return _fig(svg(520, 260, "".join(o),
                    "Mô hình động cơ: rôto có quán tính và giảm chấn, trục nhận mômen lệnh và mômen tải"),
                "Hình 99.6 · Mô hình động cơ. Rôto có mômen quán tính J<sub>m</sub> và giảm chấn cơ điện "
                "B<sub>m</sub>; trục chịu mômen lệnh τ<sub>cmd</sub> và mômen tải τ<sub>load</sub> ngược chiều.",
                "Figure 99.6 · Motor model. The rotor has moment of inertia J<sub>m</sub> and "
                "electromechanical damping B<sub>m</sub>; the shaft carries the command torque "
                "τ<sub>cmd</sub> and the opposing load torque τ<sub>load</sub>.",
                "Sơ đồ động cơ: rôto trên stato, trục có hai mômen ngược chiều",
                "Motor model: rotor on a stator, shaft with opposed torques")


# ---------------------------------------------------------------- 99.7
def fig_99_7():
    o = [_defs("99")]
    o.append(_rect(40, 108, 112, 56, 1.5))
    o.append(_lbl(96, 140, "Động cơ/Bơm", "tm", "middle"))
    # pressure line to the right chamber
    o.append(_line(152, 118, 196, 118, 1.3))
    o.append(_line(196, 118, 196, 66, 1.3))
    o.append(_line(196, 66, 430, 66, 1.3))
    o.append(_arr(430, 66, 430, 100, 1.3))
    # return line to the left chamber
    o.append(_line(152, 154, 196, 154, 1.3))
    o.append(_line(196, 154, 196, 214, 1.3))
    o.append(_line(196, 214, 286, 214, 1.3))
    o.append(_line(286, 214, 286, 186, 1.3))
    o.append(_arr(286, 214, 286, 182, 1.3))
    o.append(_lbl(206, 202, "Q", "tm", "middle"))
    # cylinder
    o.append(_rect(240, 104, 240, 78, 1.5))
    o.append(_rect(286, 108, 20, 70, 1.3, "#e8e8e8"))
    o.append(_line(306, 143, 560, 143, 2.2))
    o.append(_rich(316, 132, [("F", False), ("A", True)], "start", "tm"))
    o.append(_arr(320, 124, 356, 124))
    o.append(_rich(404, 132, [("F", False), ("P", True)], "start", "tm"))
    o.append(_arr(412, 124, 376, 124))
    o.append(_rich(320, 168, [("M", False), ("p", True)], "start", "tm"))
    o.append(_rich(320, 200, [("x", False), ("p", True)], "start", "tm"))
    o.append(_arr(346, 196, 388, 196))
    # hinge and arm
    o.append('<circle cx="560" cy="143" r="6" fill="#fff" stroke="%s" stroke-width="1.3"/>' % E)
    o.append(_line(566, 143, 594, 164, 1.3))
    # control surface hanging from the hinge
    o.append('<path d="M592 156 C 620 170, 652 182, 670 198 C 638 206, 606 192, 592 176 Z" '
             'fill="#f2f2f2" stroke="%s" stroke-width="1.3"/>' % E)
    # moment arm R_h
    o.append(_line(578, 145, 578, 166, 1.0, S))
    o.append('<path d="M578 145 L574.6 152 L581.4 152 Z" fill="%s"/>' % S)
    o.append('<path d="M578 166 L574.6 159 L581.4 159 Z" fill="%s"/>' % S)
    o.append(_rich(578, 140, [("R", False), ("h", True)], "middle", "tm"))
    # surface travel
    o.append(_arr(628, 122, 578, 122))
    o.append(_rich(634, 126, [("X", False), ("L", True)], "start", "tm"))
    # hinge and aerodynamic moments
    o.append('<path d="M584 200 A 11 11 0 1 1 594 209" fill="none" stroke="%s" '
             'stroke-width="1.1" marker-end="url(#a99)"/>' % E)
    o.append(_rich(572, 200, [("τ", False), ("R", True)], "end", "tm"))
    o.append('<path d="M678 188 A 11 11 0 1 1 674 208" fill="none" stroke="%s" '
             'stroke-width="1.1" marker-end="url(#a99)"/>' % E)
    o.append(_rich(682, 194, [("τ", False), ("L", True)], "start", "tm"))
    # surface angle to the free stream
    o.append(_line(706, 152, 776, 152, 1.2))
    o.append(_line(706, 152, 776, 124, 1.2))
    o.append('<path d="M744 152 A 38 38 0 0 0 752 133" fill="none" stroke="%s" stroke-width="1.0"/>' % E)
    o.append(_rich(750, 150, [("Θ", False), ("L", True)], "start", "tm"))
    return _fig(svg(800, 250, "".join(o),
                    "Sơ đồ điều khiển cơ cấu chấp hành rút gọn: động cơ/bơm, xi lanh, tay đòn và cánh lái"),
                "Hình 99.7 · Điều khiển cơ cấu chấp hành rút gọn (không vẽ theo tỉ lệ). Bơm đẩy lưu lượng Q "
                "vào xi lanh; chênh áp tạo lực F<sub>A</sub> − F<sub>P</sub>; pittông chạy x<sub>p</sub>; tay "
                "đòn dài R<sub>h</sub> biến chuyển vị thành mômen quay cánh lái Θ<sub>L</sub>.",
                "Figure 99.7 · Simplified actuator control (not drawn to scale). The pump drives flow Q into "
                "the cylinder; the pressure difference produces F<sub>A</sub> − F<sub>P</sub>; the piston "
                "moves x<sub>p</sub>; the arm of length R<sub>h</sub> turns the displacement into the surface "
                "moment Θ<sub>L</sub>.",
                "Sơ đồ rút gọn: bơm, xi lanh, pittông, tay đòn và cánh lái",
                "Simplified schematic: pump, cylinder, piston, arm and control surface")


# ---------------------------------------------------------------- 99.8
def fig_99_8():
    o = [_defs("99")]
    y = 150
    o.append(_rich(12, y + 4, [("τ", False), ("cmd", True)], "start", "tm"))
    o.append(_arr(60, y, 84, y))
    o.append(_sum(96, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_rich(110, y - 9, [("τ", False), ("e", True)], "start", "tm"))
    o.append(_arr(106, y, 132, y))
    o.append(_frac(132, y - 20, 74, 40, "1",
                   [("J", False), ("m", True), ("s + b", False), ("m", True)]))
    o.append(_arr(206, y, 228, y))
    o.append(_rich(210, y - 9, [("Ω", False), ("m", True)], "start", "tm"))
    o.append(_frac(228, y - 20, 50, 40, [("D", False), ("m", True)], "2\u03c0"))
    o.append(_arr(278, y, 300, y))
    o.append(_rich(276, y - 16, [("Q", False), ("m", True)], "start", "tm"))
    o.append(_sum(312, y, 10, {"l": "+", "t": "\u2212"}))
    o.append(_rich(324, y - 9, [("\u03b4Q", False)], "start", "tm"))
    o.append(_arr(322, y, 348, y))
    o.append(_frac(348, y - 20, 76, 40, "1",
                   [("K", False), ("s", True), ("s + C", False), ("t", True)]))
    o.append(_arr(424, y, 448, y))
    o.append(_rich(428, y - 12, [("P", False)], "start", "tm"))
    o.append(_line(427, y - 16, 437, y - 16, 0.9))
    o.append(_blk(448, y - 14, 30, 28, ["A"]))
    o.append(_arr(478, y, 502, y))
    o.append(_rich(480, y - 14, [("F", False), ("A", True)], "start", "tm"))
    o.append(_sum(514, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_rich(530, y - 9, [("F", False), ("e", True)], "start", "tm"))
    o.append(_arr(524, y, 550, y))
    # piston / load dynamics: wide fraction block, short rule
    o.append(_rect(550, y - 30, 172, 60, 1.3))
    o.append(_lbl(636, y - 8, "1", "tm", "middle"))
    o.append(_line(598, y - 2, 674, y - 2, 1.0))
    o.append(_rich(636, y + 16,
                   [("(M", False), ("p", True), (" + J", False), ("L", True), ("/R", False),
                    ("h", True), ("\u00b2)s + B", False), ("p", True), (" + B", False),
                    ("L", True), ("/R", False), ("h", True), ("\u00b2", False)], "middle", "tm"))
    o.append(_arr(722, y, 746, y))
    o.append(_rich(724, y + 20, [("sX", False), ("p", True)], "start", "tm"))
    o.append(_frac(746, y - 20, 36, 40, "1", "s"))
    o.append(_arr(782, y, 806, y))
    o.append(_rich(786, y - 9, [("X", False), ("p", True)], "start", "tm"))
    o.append(_frac(806, y - 20, 48, 40, "1", [("R", False), ("h", True)]))
    o.append(_arr(854, y, 884, y))
    o.append(_rich(890, y + 4, [("\u03b8", False), ("L", True)], "start", "tm"))
    # top feedback: sX_p -> A -> dQ junction
    o.append(_line(734, y, 734, 70, 1.3))
    o.append(_line(734, 70, 660, 70, 1.3))
    o.append(_blk(628, 56, 32, 28, ["A"]))
    o.append(_line(628, 70, 312, 70, 1.3))
    o.append(_arr(312, 70, 312, y - 10, "99"))
    # bottom right: theta_L -> Load_aero -> tau_L -> 1/R_h -> F_e junction
    o.append(_line(866, y, 866, y + 84, 1.3))
    o.append(_line(866, y + 84, 786, y + 84, 1.3))
    o.append(_blk(660, y + 68, 126, 32, []))
    o.append(_lbl(668, y + 92, "Load", "tm"))
    o.append(_lbl(700, y + 92, "aero", "tm"))
    o.append(_arr(660, y + 84, 620, y + 84))
    o.append(_rich(628, y + 78, [("\u03c4", False), ("L", True)], "start", "tm"))
    o.append(_frac(584, y + 68, 36, 32, "1", [("R", False), ("h", True)]))
    o.append(_arr(584, y + 84, 552, y + 84))
    o.append(_line(552, y + 84, 552, y + 10, 1.3))
    o.append(_arr(552, y + 10, 518, y + 10, "99"))
    # bottom left: P -> D_m/2pi -> tau_load -> tau_e junction
    o.append(_line(440, y, 440, y + 112, 1.3))
    o.append(_line(440, y + 112, 300, y + 112, 1.3))
    o.append(_frac(250, y + 98, 50, 28, [("D", False), ("m", True)], "2\u03c0"))
    o.append(_arr(250, y + 112, 214, y + 112))
    o.append(_rich(150, y + 106, [("\u03c4", False), ("load", True)], "start", "tm"))
    o.append(_line(120, y + 112, 96, y + 112, 1.3))
    o.append(_line(96, y + 112, 96, y + 10, 1.3))
    o.append(_arr(96, y + 10, 96, y + 4, "99"))
    o.append(_lbl(120, 44, "Động lực học động cơ", "tm", "middle"))
    o.append(_lbl(320, 44, "Động lực học bơm/chất lỏng", "tm", "middle"))
    o.append(_lbl(650, 44, "Động lực học pittông/tải", "tm", "middle"))
    return _fig(svg(940, 300, "".join(o),
                    "Sơ đồ khối của EHA thuần: ba nhóm động lực học và ba vòng phản hồi"),
                "Hình 99.8 · Sơ đồ khối của EHA thuần (không có bộ điều khiển). Ba nhóm động lực học nối "
                "tiếp — động cơ, bơm/chất lỏng, pittông/tải — với ba vòng phản hồi: lưu lượng A·sX<sub>p</sub>, "
                "mômen tải τ<sub>L</sub>/R<sub>h</sub> và mômen τ<sub>load</sub> do chênh áp bơm gây ra.",
                "Figure 99.8 · Bare EHA block diagram. Three dynamics groups in cascade — motor, pump/fluid, "
                "piston/load — with three feedback paths: the flow A·sX<sub>p</sub>, the load moment "
                "τ<sub>L</sub>/R<sub>h</sub>, and the torque τ<sub>load</sub> produced by the pump pressure.",
                "Sơ đồ khối EHA với ba nhóm khối và ba vòng phản hồi",
                "EHA block diagram: three block groups and three feedback paths")


# ---------------------------------------------------------------- 99.9
def fig_99_9():
    o = [_defs("99")]

    def sp(s):
        return 10.0 * (s + 2.0) / ((s + 1.2) * (s + 6.0))

    def full(s):
        return sp(s) / (s + 0.05)

    o.append(_bode(110, 52, 420, 150, (-2, 3), None, None,
                   (-40, 40), [40, 20, 0, -20, -40],
                   (-180, 0), [0, -45, -90, -135, -180],
                   "Tần số (rad/giây)", "Biên độ (dB)", "Pha (độ)",
                   [(full, "", "full"), (sp, "+", "sp")]))

    def X(f):
        return 110 + (math.log10(f) + 2) * 420 / 5.0

    def YM(v):
        return 52 + 150 - (v + 40) * 150 / 80.0

    def YP(v):
        return 52 + 150 + 62 + 150 - (v + 180) * 150 / 180.0

    prev = None
    for i in range(0, 161):
        f = 10 ** (-2 + 5 * i / 160.0)
        g = sp(1j * f)
        mdb = max(-40, min(40, 20 * math.log10(abs(g))))
        phd = math.degrees(math.atan2(g.imag, g.real))
        if prev is not None:
            while phd - prev > 180:
                phd -= 360
            while phd - prev < -180:
                phd += 360
        prev = phd
        o.append('<circle cx="%s" cy="%s" r="1.7" fill="%s"/>'
                 % (_f(X(f)), _f(YM(mdb)), GOLD))
        o.append('<circle cx="%s" cy="%s" r="1.7" fill="%s"/>'
                 % (_f(X(f)), _f(YP(max(-180, min(0, phd)))), GOLD))
    o.append(_lbl(520, 72, "mô hình đầy đủ", "tm", "end"))
    o.append(_lbl(520, 88, "xấp xỉ chu kỳ ngắn", "tm", "end"))
    return _fig(svg(640, 470, "".join(o),
                    "So sánh đáp ứng tần số của mô hình đầy đủ và xấp xỉ chu kỳ ngắn của chuyển động dọc"),
                "Hình 99.9 · So sánh mô hình đầy đủ (nét liền) và xấp xỉ chu kỳ ngắn (dấu chấm) cho phương trình "
                "chuyển động dọc của máy bay. Hai mô hình bám sát nhau ở dải tần trên 0,5 rad/giây; dưới tần số "
                "ấy xấp xỉ không còn đúng vì chế độ dọc chậm — gọi là phugoid — bắt đầu có tác dụng.",
                "Figure 99.9 · Comparison of the full state model (solid) and the short-period approximation "
                "(dots) for the longitudinal equations of motion. The two agree above about 0.5 rad/s; below "
                "that the approximation fails because the slow longitudinal mode, the phugoid, takes over.",
                "Hai đồ thị Bode so sánh mô hình đầy đủ và xấp xỉ chu kỳ ngắn",
                "Two Bode panels comparing the full and short-period models")


# ---------------------------------------------------------------- 99.10
def fig_99_10():
    o = [_defs("99")]
    y = 160
    o.append(_rich(12, y + 4, [("θ", False), ("cmd", True)], "start", "tm"))
    o.append(_arr(58, y, 82, y))
    o.append(_blk(82, y - 16, 76, 32, []))
    o.append(_rich(90, y + 4, [("F", False), ("\u0398", True), ("(s)", False)], "start", "tm"))
    o.append(_arr(158, y, 186, y))
    o.append(_sum(196, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(206, y, 232, y))
    o.append(_blk(232, y - 16, 76, 32, []))
    o.append(_rich(240, y + 4, [("G", False), ("\u0398", True), ("(s)", False)], "start", "tm"))
    o.append(_arr(308, y, 336, y))
    # inner loop box
    o.append(_rect(334, y - 50, 310, 100, 1.1, "none", "4 3"))
    o.append(_lbl(346, y - 56, "Vòng trong QFT", "tm"))
    o.append(_rich(340, y - 8, [("\u03c9", False), ("cmd", True)], "start", "tm"))
    o.append(_sum(366, y, 10, {"l": "+", "b": "\u2212"}))
    o.append(_arr(376, y, 402, y))
    o.append(_blk(402, y - 16, 76, 32, []))
    o.append(_rich(410, y + 4, [("G", False), ("m", True), ("(s)", False)], "start", "tm"))
    o.append(_arr(478, y, 506, y))
    o.append(_sum(516, y, 10, {"l": "+", "t": "+"}))
    o.append(_sarr(516, y - 28, 516, y - 12))
    o.append(_rich(524, y - 32, [("d", False), ("1", True), ("(t)", False)], "start", "tm"))
    o.append(_arr(526, y, 552, y))
    o.append(_blk(552, y - 16, 70, 32, []))
    o.append(_rich(560, y + 4, [("P", False), ("1", True), ("(s)", False)], "start", "tm"))
    o.append(_arr(622, y, 648, y))
    o.append(_rich(626, y - 9, [("\u03c9", False), ("m", True)], "start", "tm"))
    # outer plant box
    o.append(_rect(650, y - 66, 172, 132, 1.1, "none", "2 3"))
    o.append(_lbl(660, y - 72, "P", "tm"))
    o.append(_rich(672, y - 72, [("\u0398", True), (" của vòng ngoài", False)], "start", "tm"))
    o.append(_blk(668, y - 16, 76, 32, []))
    o.append(_rich(676, y + 4, [("P", False), ("\u0398", True), ("(s)", False)], "start", "tm"))
    o.append(_arr(744, y, 772, y))
    o.append(_sum(782, y, 10, {"l": "+", "t": "\u2212"}))
    o.append(_sarr(782, y - 28, 782, y - 12))
    o.append(_rich(790, y - 32, [("d", False), ("2", True), ("(t)", False)], "start", "tm"))
    o.append(_arr(792, y, 858, y))
    o.append(_lbl(866, y + 5, "L", "tb"))
    # inner feedback
    o.append(_line(636, y, 636, y + 72, 1.3))
    o.append(_line(636, y + 72, 366, y + 72, 1.3))
    o.append(_line(366, y + 72, 366, y + 10, 1.3))
    # outer feedback
    o.append(_line(842, y, 842, y + 106, 1.3))
    o.append(_line(842, y + 106, 196, y + 106, 1.3))
    o.append(_line(196, y + 106, 196, y + 10, 1.3))
    return _fig(svg(900, 300, "".join(o),
                    "Hai vòng phản hồi trong cấu trúc QFT hai bậc tự do: vòng trong điều khiển tốc độ góc, vòng ngoài điều khiển góc lái"),
                "Hình 99.10 · Hai vòng phản hồi trong cấu trúc QFT hai bậc tự do. Vòng trong điều khiển tốc độ "
                "góc của động cơ, vòng ngoài điều khiển góc lái của cánh; bộ lọc trước F<sub>Θ</sub> của vòng "
                "ngoài gánh toàn bộ yêu cầu bám.",
                "Figure 99.10 · Two feedback loops in the QFT two-degrees-of-freedom structure. The inner loop "
                "controls the motor's angular rate, the outer loop the surface deflection; the outer "
                "prefilter F<sub>Θ</sub> carries the whole tracking requirement.",
                "Sơ đồ hai vòng phản hồi lồng nhau với bộ lọc trước và hai nhiễu",
                "Two nested feedback loops with a prefilter and two disturbances")


FIGS = [fig_99_1, fig_99_2, fig_99_3, fig_99_4, fig_99_5,
        fig_99_6, fig_99_7, fig_99_8, fig_99_9, fig_99_10]


def fig(n):
    return FIGS[n - 1]()
