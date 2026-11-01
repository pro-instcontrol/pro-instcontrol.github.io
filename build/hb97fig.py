# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 97 — PID Control (F. Greg Shinskey, Process
Control Consultant).

Four figures (97.1–97.4). 97.1 and 97.4 are loop / controller block diagrams
redrawn block for block; 97.2 and 97.3 are response plots redrawn from the
source curves.

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
BLUE = "#1d4ed8"
TEAL = "#0f766e"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="t"):
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="8.2" dy="2.4">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.4">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _vlab(x, y, txt, cls="t"):
    """Axis title rotated 90° counter-clockwise about (x, y)."""
    return ('<text class="%s" x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>'
            % (cls, _f(x), _f(y), _f(x), _f(y), txt))


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="s%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<style>.tl{font:9.5px Inter,Helvetica,sans-serif;fill:#555}'
            '.tm{font:9px Inter,Helvetica,sans-serif;fill:#333}'
            '.tf{font:11.5px "Cambria Math",Georgia,serif;fill:#111}'
            '.tb{font:10px Inter,Helvetica,sans-serif;fill:#111;font-weight:700}'
            '.tcap{font:9px Inter,Helvetica,sans-serif;fill:#555}'
            '</style></defs>' % (tag, E, tag, S))


def _line(x1, y1, x2, y2, sw=1.3, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="97", sw=1.25, col=E):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, tag))


def _rect(x, y, w, h, sw=1.25, fill="#fff", dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, E, sw, d))


def _blk(x, y, w, h, parts, cls="tf"):
    """Box with one or more centred lines; parts may be str or [(txt, is_sub)]."""
    o = [_rect(x, y, w, h)]
    n = len(parts)
    for i, ln in enumerate(parts):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 13 + 3.6
        if isinstance(ln, list):
            o.append(_rich(x + w / 2.0, cy, ln, "middle", cls))
        else:
            o.append(_lbl(x + w / 2.0, cy, ln, cls, "middle"))
    return "".join(o)


def _frac(cx, cy, num, den, w=44, cls="tf"):
    """Fraction with a rule; num/den are str or [(txt, is_sub)]."""
    o = [_line(cx - w / 2.0, cy, cx + w / 2.0, cy, 1.0)]
    if isinstance(num, list):
        o.append(_rich(cx, cy - 5, num, "middle", cls))
    else:
        o.append(_lbl(cx, cy - 5, num, cls, "middle"))
    if isinstance(den, list):
        o.append(_rich(cx, cy + 13, den, "middle", cls))
    else:
        o.append(_lbl(cx, cy + 13, den, cls, "middle"))
    return "".join(o)


def _sum(cx, cy, r=10, signs=None, tag="97"):
    o = ['<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="1.25"/>'
         % (_f(cx), _f(cy), _f(r), E)]
    if signs:
        pos = {"l": (cx - r - 13, cy - 6), "r": (cx + r + 3, cy - 5),
               "t": (cx + 4, cy - r - 4), "b": (cx - 9, cy + r + 11)}
        for k, s in signs.items():
            x, y = pos[k]
            o.append(_lbl(x, y, s, "tm"))
    return "".join(o)


def _path(pts, col=E, sw=1.7, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
            % (" ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts), col, sw, d))


def _frame(x, y, w, h):
    """Plot frame with small inward ticks, no tick labels (as in the source)."""
    o = [_rect(x, y, w, h, 0.9, "#fff")]
    for i in (1, 2, 3):
        xx = x + w * i / 4.0
        o.append(_line(xx, y + h, xx, y + h - 5, 0.8, S))
        o.append(_line(xx, y, xx, y + 5, 0.8, S))
    for i in (1, 2, 3):
        yy = y + h * i / 4.0
        o.append(_line(x, yy, x + 5, yy, 0.8, S))
        o.append(_line(x + w, yy, x + w - 5, yy, 0.8, S))
    return "".join(o)


# ---------------------------------------------------------------- 97.1
def fig_97_1():
    o = [_defs("97")]
    DIV = 202                                     # dashed process/controller divider

    # ---- process (above the divider)
    o.append(_lbl(150, 36, "q", "tf"))
    o.append(_lbl(136, 60, "Load", "tcap"))
    o.append(_arr(158, 44, 206, 44))
    o.append(_blk(206, 24, 74, 42, [[("g", False), ("q", True)]]))
    # load enters Kp from above with a minus sign
    o.append(_arr(243, 66, 243, 82))
    o.append(_lbl(234, 78, "\u2212", "tm", "end"))

    o.append(_blk(108, 92, 74, 46, [[("g", False), ("m", True)]]))
    o.append(_arr(182, 115, 224, 115))
    o.append(_lbl(202, 109, "+", "tm", "middle"))
    o.append(_blk(224, 82, 80, 66, [[("K", False), ("p", True)]]))

    o.append(_arr(304, 115, 372, 115))
    o.append(_sum(384, 115, 10, {"l": "+", "t": "\u2212"}))
    # noise enters the summing junction from above
    o.append(_lbl(396, 44, "u", "tf"))
    o.append(_lbl(408, 58, "Noise", "tcap"))
    o.append(_arr(384, 64, 384, 103))

    o.append(_arr(394, 115, 470, 115))
    o.append(_lbl(408, 109, "c", "tf"))
    o.append(_lbl(428, 132, "Controlled var.", "tcap"))

    o.append(_line(40, DIV, 660, DIV, 1.0, E, "6 4"))
    o.append(_lbl(44, DIV - 8, "Process", "tcap"))
    o.append(_lbl(44, DIV + 16, "Controller", "tcap"))

    # ---- controller (below the divider)
    o.append(_line(384, 125, 384, 288, 1.3))
    o.append(_sum(384, 300, 10, {"t": "\u2212", "r": "+"}))
    o.append(_blk(470, 277, 74, 46, [[("g", False), ("r", True)]]))
    o.append(_arr(470, 300, 396, 300))
    o.append(_lbl(584, 296, "f", "tf"))
    o.append(_lbl(556, 318, "Set point", "tcap"))
    o.append(_arr(584, 300, 546, 300))

    o.append(_lbl(348, 294, "e", "tf"))
    o.append(_lbl(338, 314, "Dev.", "tcap"))
    o.append(_blk(250, 277, 84, 46, [[("K", False), ("c", True), (" g", False), ("c", True)]]))
    o.append(_line(250, 300, 145, 300, 1.3))
    o.append(_lbl(212, 294, "m", "tf"))
    o.append(_lbl(158, 322, "Manipulated var.", "tcap"))
    o.append(_arr(145, 300, 145, 146))
    return _fig(svg(720, 350, "".join(o),
                    "S\u01a1 \u0111\u1ed3 v\u00f2ng k\u00edn: \u0111\u1ed1i t\u01b0\u1ee3ng \u1edf tr\u00ean, b\u1ed9 \u0111i\u1ec1u khi\u1ec3n \u1edf d\u01b0\u1edbi, "
                    "v\u1edbi nhi\u1ec5u u, t\u1ea3i q, bi\u1ebfn \u0111i\u1ec1u khi\u1ec3n m v\u00e0 bi\u1ebfn \u0111\u01b0\u1ee3c \u0111i\u1ec1u khi\u1ec3n c"),
                "H\u00ecnh 97.1 \u00b7 \u0110\u1ed1i t\u01b0\u1ee3ng v\u00e0 b\u1ed9 \u0111i\u1ec1u khi\u1ec3n m\u1eafc th\u00e0nh m\u1ed9t v\u00f2ng. Ph\u1ea7n tr\u00ean \u0111\u01b0\u1eddng "
                "g\u1ea1ch n\u1eb1m ngang l\u00e0 \u0111\u1ed1i t\u01b0\u1ee3ng: t\u1ea3i q \u0111i qua h\u00e0m \u0111\u1ed9ng h\u1ecdc g<sub>q</sub> v\u00e0 tr\u1eeb v\u00e0o "
                "\u0111\u1ea7u ra c\u1ee7a K<sub>p</sub>, c\u00f2n bi\u1ebfn \u0111i\u1ec1u khi\u1ec3n m \u0111i qua g<sub>m</sub> r\u1ed3i c\u1ed9ng v\u00e0o. Nhi\u1ec5u u "
                "c\u1ed9ng tr\u1ef1c ti\u1ebfp v\u00e0o bi\u1ebfn \u0111\u01b0\u1ee3c \u0111i\u1ec1u khi\u1ec3n c. Ph\u1ea7n d\u01b0\u1edbi l\u00e0 b\u1ed9 \u0111i\u1ec1u khi\u1ec3n: "
                "l\u1ec7nh \u0111\u1eb7t f qua b\u1ed9 l\u1ecdc g<sub>r</sub> tr\u1eeb \u0111i c \u0111\u1ec3 t\u1ea1o \u0111\u1ed9 l\u1ec7ch e, r\u1ed3i qua K<sub>c</sub>g<sub>c</sub> "
                "th\u00e0nh t\u00edn hi\u1ec7u \u0111i\u1ec1u khi\u1ec3n m.",
                "Figure 97.1 \u00b7 Process and controller connected in a loop. Above the dashed divider "
                "is the process: the load q passes through the dynamic gain g<sub>q</sub> and is "
                "subtracted at the output of K<sub>p</sub>, while the manipulated variable m passes "
                "through g<sub>m</sub> and is added. Noise u adds directly to the controlled variable "
                "c. Below the divider is the controller: set point f passes through the filter "
                "g<sub>r</sub> and has c subtracted from it to form the deviation e, which becomes "
                "the manipulated variable m through K<sub>c</sub>g<sub>c</sub>.",
                "\u0110\u1ed3 th\u1ecb v\u00f2ng \u0111i\u1ec1u khi\u1ec3n c\u00f3 \u0111\u1ed1i t\u01b0\u1ee3ng v\u00e0 b\u1ed9 \u0111i\u1ec1u khi\u1ec3n",
                "Loop diagram with process and controller")


# ---------------------------------------------------------------- 97.2
def fig_97_2():
    o = [_defs("97")]
    x0, y0, w, h = 95, 55, 505, 245
    YR = 245                       # steady value of c = set point r
    T = 8.0

    def X(t):
        return x0 + t / T * w

    def opn(t):
        return YR - 150.0 * (1 - math.exp(-t / 3.0))

    def cls(t):
        return YR - 45.0 * (1 - math.exp(-t / 0.55)) * math.exp(-t / 1.9) \
            + 4.0 * math.exp(-t / 0.7)

    o.append(_frame(x0, y0, w, h))
    o.append(_vlab(70, y0 + h / 2.0, "Controlled variable"))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 32, "Time", "t", "middle"))

    o.append(_line(x0, YR, x0 + w, YR, 0.9, S))

    ts = [T * i / 200.0 for i in range(201)]
    o.append(_path([(X(t), opn(t)) for t in ts], E, 1.7, "7 4"))
    o.append(_path([(X(t), cls(t)) for t in ts], E, 1.9))

    o.append(_lbl(340, 150, "Open-loop", "tcap"))
    o.append(_lbl(400, 232, "Closed-loop", "tcap"))
    o.append(_lbl(X(0) + 6, YR - 14, "c", "tf"))
    o.append(_lbl(X(1.1), YR + 16, "r", "tf"))
    return _fig(svg(640, 350, "".join(o),
                    "\u0110\u00e1p \u1ee9ng v\u00f2ng h\u1edf t\u0103ng theo h\u00e0m m\u0169 (n\u00e9t g\u1ea1ch) v\u00e0 \u0111\u00e1p \u1ee9ng v\u00f2ng k\u00edn "
                    "quay v\u1ec1 gi\u00e1 tr\u1ecb \u0111\u1eb7t (n\u00e9t li\u1ec1n)"),
                "H\u00ecnh 97.2 \u00b7 \u0110i\u1ec1u khi\u1ec3n v\u00f2ng k\u00edn l\u00e0m sai s\u1ed1 nh\u1ecf nh\u1ea5t. Khi v\u00f2ng h\u1edf, sau m\u1ed9t "
                "b\u01b0\u1edbc nh\u1ea3y t\u1ea3i th\u00ec c \u0111i theo \u0111\u01b0\u1eddng h\u00e0m m\u0169 (n\u00e9t g\u1ea1ch). Khi v\u00f2ng k\u00edn, b\u1ed9 \u0111i\u1ec1u "
                "khi\u1ec3n t\u00e1c \u0111\u1ed9ng l\u00ean m \u0111\u1ec3 \u0111\u01b0a c v\u1ec1 r theo n\u00e9t li\u1ec1n \u2014 qu\u1ef9 \u0111\u1ea1o t\u1ed1i \u01b0u c\u00f3 t\u00edch "
                "ph\u00e2n tr\u1ecb tuy\u1ec7t \u0111\u1ed1i c\u1ee7a sai s\u1ed1 (IAE) gi\u1eefa c v\u00e0 r l\u00e0 nh\u1ecf nh\u1ea5t.",
                "Figure 97.2 \u00b7 Closed-loop control minimizes error. In the open loop, c takes an "
                "exponential path after a load step (dashed). With the loop closed the controller "
                "moves m to return c to r along the solid curve, an optimum trajectory having a "
                "minimum integrated absolute error (IAE) between c and r.",
                "\u0110\u1ed3 th\u1ecb \u0111\u00e1p \u1ee9ng v\u00f2ng h\u1edf v\u00e0 v\u00f2ng k\u00edn theo th\u1eddi gian",
                "Open-loop and closed-loop responses versus time")


# ---------------------------------------------------------------- 97.3
def fig_97_3():
    o = [_defs("97")]
    x0, y0, w, h = 95, 55, 505, 245
    YR = 140
    YC = 280
    T = 8.0

    def X(t):
        return x0 + t / T * w

    def step(t, zeta, om):
        wd = om * math.sqrt(1 - zeta * zeta)
        e = math.exp(-zeta * om * t)
        return YR + (YC - YR) * e * (math.cos(wd * t)
                                     + (zeta / math.sqrt(1 - zeta * zeta))
                                     * math.sin(wd * t))

    o.append(_frame(x0, y0, w, h))
    o.append(_vlab(70, y0 + h / 2.0, "Controlled variable"))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 32, "Time", "t", "middle"))
    o.append(_line(x0, YR, x0 + w, YR, 0.9, S))

    ts = [T * i / 200.0 for i in range(201)]
    o.append(_path([(X(t), step(t, 0.35, 1.5)) for t in ts], E, 1.6, "7 4"))
    o.append(_path([(X(t), step(t, 0.70, 1.2)) for t in ts], E, 1.9))

    o.append(_lbl(252, 90, "No filter", "tcap"))
    o.append(_lbl(252, 174, "Set-point filter", "tcap"))
    o.append(_lbl(x0 + 8, YC - 6, "c", "tf"))
    o.append(_lbl(x0 + 8, YR - 7, "r", "tf"))
    return _fig(svg(640, 350, "".join(o),
                    "\u0110\u00e1p \u1ee9ng v\u1edbi b\u1ed9 l\u1ecdc ch\u1ec9nh \u0111\u1ecbnh (n\u00e9t li\u1ec1n) v\u00e0 kh\u00f4ng c\u00f3 b\u1ed9 l\u1ecdc (n\u00e9t g\u1ea1ch)"),
                "H\u00ecnh 97.3 \u00b7 B\u1ed9 l\u1ecdc l\u1ec7nh \u0111\u1eb7t l\u00e0m gi\u1ea3m \u0111\u1ed9 v\u1ecdt. N\u1ebfu ch\u1ec9nh \u0111\u1ecbnh PID theo \u0111\u00e1p \u1ee9ng t\u1ea3i "
                "th\u00ec c th\u01b0\u1eddng v\u01b0\u1ee3t qu\u00e1 gi\u00e1 tr\u1ecb \u0111\u1eb7t khi l\u1ec7nh \u0111\u1eb7t thay \u0111\u1ed5i (n\u00e9t g\u1ea1ch). Ch\u00e8n "
                "m\u1ed9t b\u1ed9 l\u1ecdc tr\u1ec5\u2013s\u1edbm v\u00e0o \u0111\u01b0\u1eddng l\u1ec7nh \u0111\u1eb7t s\u1ebd cho n\u00e9t li\u1ec1n, c\u00f3 \u0111\u1ed9 v\u1ecdt nh\u1ecf h\u01a1n "
                "nhi\u1ec1u.",
                "Figure 97.3 \u00b7 A lead\u2013lag filter reduces overshoot. If the PID settings are optimized "
                "for load response they usually cause c to overshoot a change in set point r "
                "(dashed). Inserting a lead\u2013lag filter in the set-point path produces the solid "
                "curve.",
                "\u0110\u1ed3 th\u1ecb \u0111\u1ed9 v\u1ecdt c\u00f3 v\u00e0 kh\u00f4ng c\u00f3 b\u1ed9 l\u1ecdc ch\u1ec9nh \u0111\u1ecbnh",
                "Overshoot with and without a set-point filter")


# ---------------------------------------------------------------- 97.4
def fig_97_4():
    o = [_defs("97")]
    YM, YL = 108, 212

    o.append(_lbl(28, YM + 4, "r", "tf"))
    o.append(_arr(46, YM, 62, YM))
    # set-point filter
    o.append(_rect(62, 72, 100, 72))
    o.append(_frac(112, 96, [("1 + G", False), ("r", True), ("Is", False)],
                   "1 + Is", 56))
    o.append(_lbl(112, 160, "Filter", "tcap", "middle"))
    o.append(_arr(162, YM, 186, YM))

    # error and derivative summing junctions
    o.append(_sum(196, YM, 9, {"l": "+", "b": "\u2212"}))
    o.append(_arr(205, YM, 284, YM))
    o.append(_lbl(240, YM - 10, "e", "tf"))
    o.append(_sum(298, YM, 9, {"b": "\u2212"}))
    o.append(_arr(307, YM, 340, YM))

    o.append(_blk(340, 84, 72, 48, [[("K", False), ("c", True)]]))
    o.append(_lbl(376, 150, "Proportional", "tcap", "middle"))
    o.append(_arr(412, YM, 448, YM))

    o.append(_sum(460, YM, 9, {"l": "+", "b": "+"}))
    o.append(_arr(469, YM, 504, YM))
    # saturation limits symbol
    o.append(_rect(504, 84, 76, 48))
    o.append('<path d="M524,100 L524,116 L532,108 z" fill="%s"/>' % E)
    o.append('<path d="M560,100 L560,116 L552,108 z" fill="%s"/>' % E)
    o.append(_lbl(542, 150, "Limits", "tcap", "middle"))
    o.append(_arr(580, YM, 652, YM))
    o.append(_lbl(596, YM - 12, "m", "tf"))

    # derivative branch off c
    o.append(_lbl(28, YL + 4, "c", "tf"))
    o.append(_line(44, YL, 236, YL, 1.3))
    o.append(_arr(196, YL, 196, YM + 10))
    o.append(_arr(236, YL, 249, YL))
    o.append(_blk(250, 188, 96, 48, []))
    o.append(_frac(298, 205, "Ds", "1 + \u03b1Ds", 52))
    o.append(_lbl(298, 252, "Derivative", "tcap", "middle"))
    o.append(_arr(298, 188, 298, YM + 10))

    # integral loop: m -> f -> integral -> b -> summing junction
    o.append(_line(634, YM, 634, YL, 1.0, E, "5 4"))
    o.append(_line(634, YL, 522, YL, 1.0, E, "5 4"))
    o.append(_arr(522, YL, 509, YL))
    o.append(_lbl(548, YL - 8, "f", "tf"))
    o.append(_rect(412, 188, 96, 48))
    o.append(_frac(460, 205, "1", "1 + Is", 46))
    o.append(_lbl(460, 252, "Integral", "tcap", "middle"))
    o.append(_arr(460, 188, 460, YM + 10))
    o.append(_lbl(468, 162, "b", "tf"))
    return _fig(svg(720, 290, "".join(o),
                    "S\u01a1 \u0111\u1ed3 kh\u1ed1i b\u1ed9 \u0111i\u1ec1u khi\u1ec3n PID t\u01b0\u01a1ng t\u00e1c: b\u1ed9 l\u1ecdc l\u1ec7nh \u0111\u1eb7t, kh\u00e2u \u0111\u1ea1o h\u00e0m, "
                    "kh\u00e2u t\u1ec9 l\u1ec7, kh\u00e2u t\u00edch ph\u00e2n v\u00e0 kh\u1ed1i gi\u1edbi h\u1ea1n"),
                "H\u00ecnh 97.4 \u00b7 B\u1ed9 \u0111i\u1ec1u khi\u1ec3n PID t\u01b0\u01a1ng t\u00e1c th\u01b0\u01a1ng m\u1ea1i. Kh\u00e2u t\u00edch ph\u00e2n \u0111\u01b0\u1ee3c t\u1ea1o b\u1eb1ng "
                "ph\u1ea3n h\u1ed3i d\u01b0\u01a1ng \u0111\u1ea7u ra qua m\u1ed9t kh\u00e2u tr\u1ec5 b\u1eadc m\u1ed9t c\u00f3 h\u1eb1ng s\u1ed1 th\u1eddi gian b\u1eb1ng th\u1eddi "
                "gian t\u00edch ph\u00e2n I. T\u00edn hi\u1ec7u ph\u1ea3n h\u1ed3i f l\u1ea5y sau kh\u1ed1i gi\u1edbi h\u1ea1n, n\u00ean c\u00f3 th\u1ec3 thay b\u1eb1ng "
                "h\u1eb1ng s\u1ed1 \u0111\u1ec3 d\u1eebng t\u00edch ph\u00e2n v\u00e0 ch\u1ed1ng hi\u1ec7n t\u01b0\u1ee3ng d\u1ed3n t\u00edch ph\u00e2n.",
                "Figure 97.4 \u00b7 Commercial interacting PID controller. Integration is achieved by "
                "positive feedback of the output through a first-order lag set at the integral time "
                "I. The feedback signal f is taken downstream of the high and low limits, so it may "
                "be replaced with a constant to stop integration and prevent reset windup.",
                "S\u01a1 \u0111\u1ed3 kh\u1ed1i b\u1ed9 \u0111i\u1ec1u khi\u1ec3n PID t\u01b0\u01a1ng t\u00e1c",
                "Interacting PID controller block diagram")


FIGS = [fig_97_1, fig_97_2, fig_97_3, fig_97_4]


def fig(n):
    return FIGS[n - 1]()
