# -*- coding: utf-8 -*-
"""Figures 5.12-5.22 for IPC Chapter 5 (signal conditioning and data acquisition).

Supplier module ``_b``: instrumentation amplifier, multiplexing, sample and
hold, and the first data-conversion circuits.  Each figure is a simplified
vector redraw of the printed diagram; all artwork stays above y = 232 of the
680 x 250 canvas so the bilingual 5.n strip added by ``_mk`` remains clear.
"""
from ipcfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ---------------------------------------------------------------- helpers
def _res_h(x1, x2, y, n=4, amp=3.0):
    """Horizontal zig-zag resistor between two wire ends."""
    pts = [(x1, y)]
    for i in range(1, 2 * n):
        pts.append((x1 + (x2 - x1) * i / float(2 * n),
                    y + (amp if i % 2 else -amp)))
    pts.append((x2, y))
    return _poly(pts, sw=1.1, color=INK)


def _res_v(x, y1, y2, n=4, amp=3.0):
    """Vertical zig-zag resistor between two wire ends."""
    pts = [(x, y1)]
    for i in range(1, 2 * n):
        pts.append((x + (amp if i % 2 else -amp),
                    y1 + (y2 - y1) * i / float(2 * n)))
    pts.append((x, y2))
    return _poly(pts, sw=1.1, color=INK)


def _gnd(x, y):
    """Ground symbol with its top lead at (x, y)."""
    return (_line(x, y, x, y + 4, sw=1.0)
            + _line(x - 6, y + 4, x + 6, y + 4, sw=1.0)
            + _line(x - 4, y + 7, x + 4, y + 7, sw=0.9)
            + _line(x - 2, y + 10, x + 2, y + 10, sw=0.8))


def _cap(x, y, lab=""):
    """Two horizontal capacitor plates at (x, y) with a short lead above."""
    o = [_line(x - 9, y, x + 9, y, sw=1.3),
         _line(x - 9, y + 4, x + 9, y + 4, sw=1.3)]
    if lab:
        o.append(T(x + 14, y + 5, lab, 7.6, anchor="start"))
    return "".join(o)


def _op(xl, yc, w=46, h=38, lab="", plus="lower"):
    """Right-pointing op-amp triangle, left edge x=xl and centre y=yc."""
    yt, yb = yc - h * 0.28, yc + h * 0.28
    o = [_poly([(xl, yc - h / 2.0), (xl, yc + h / 2.0), (xl + w, yc)],
               fill="#ffffff", sw=1.2)]
    if plus == "upper":
        o += [T(xl + 7, yt + 2.4, "+", 8.0),
              T(xl + 7, yb + 2.2, "−", 8.0)]
    else:
        o += [T(xl + 7, yt + 2.2, "−", 8.0),
              T(xl + 7, yb + 2.4, "+", 8.0)]
    if lab:
        o.append(T(xl + w * 0.46, yc + 2.6, lab, 7.2))
    return "".join(o)


def _and(x, y, w=24, h=13, pins=2):
    """D-shaped AND gate: flat left edge at (x, y-h/2), output at (x+w, y)."""
    r = h / 2.0
    o = [_path("M%.1f,%.1f H%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f Z"
               % (x, y - r, x + w - r, r, r, x + w - r, y + r),
               fill="#ffffff", sw=1.15)]
    for i in range(pins):
        py = y - r + h * (i + 1.0) / (pins + 1.0)
        o.append(_line(x, py, x + 3, py, sw=0.9))
    o.append(_circle(x + w, y, 1.8, fill="#ffffff", sw=0.9))
    return "".join(o)


def _or(x, y, w=52, h=56):
    """OR gate with concave input edge and pointed output."""
    d = ("M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f "
         "Q%.1f,%.1f %.1f,%.1f Z"
         % (x, y - h / 2.0, x + 12, y - h / 2.0, x + w, y,
            x + 12, y + h / 2.0, x, y + h / 2.0,
            x + 9, y, x, y - h / 2.0))
    return _path(d, fill="#ffffff", sw=1.2)


def _star(x, y, r=4.2, color=RED):
    """Cross marker used for waveform coincidence points."""
    return (_line(x - r, y, x + r, y, sw=1.1, color=color)
            + _line(x, y - r, x, y + r, sw=1.1, color=color))


def _clock(x1, x2, y, hi=12, count=4):
    """A short gated train of square clock pulses."""
    o = [_line(x1, y + hi, x2, y + hi, sw=1.0)]
    span = (x2 - x1) / float(count)
    for i in range(count):
        a = x1 + i * span + span * 0.16
        b = a + span * 0.52
        o.append(_poly([(a, y + hi), (a, y), (b, y), (b, y + hi)],
                       sw=1.0, color=BLUE))
    return "".join(o)


# ---------------------------------------------------------------- 5.12
@_reg
def fig_f12():
    """Fig. 5.12 - basic three-op-amp instrumentation amplifier."""
    o = []
    # Input terminals and their reference grounds (upper stage).
    o.append(_circle(108, 62, 2.6, fill="#ffffff", sw=1.1))
    o.append(_line(108, 62, 170, 62, sw=1.1))
    o.append(T(106, 47, "(e_n + e_1)", 7.6))
    o.append(_circle(108, 82, 2.2, fill=INK, sw=0))
    o.append(_gnd(108, 82))
    # OA1: plus upper, minus lower.
    o.append(_op(170, 62, w=52, h=36, lab="OA1", plus="upper"))
    o.append(_line(222, 62, 330, 62, sw=1.1))
    o.append(T(284, 53, "eg1", 7.4))
    # Feedback ladder R1 - RX - R2 on the vertical spine.
    o.append(_line(330, 62, 330, 68, sw=1.1))
    o.append(_res_v(330, 68, 100))
    o.append(T(342, 86, "R1", 7.6, anchor="start"))
    o.append(_line(330, 100, 330, 106, sw=1.1))
    o.append(_res_v(330, 106, 138))
    o.append(T(342, 124, "RX", 7.6, anchor="start"))
    o.append(_poly([(310, 119), (327, 119), (323, 116.5)],
                   fill="#ffffff", sw=1.0))
    o.append(_line(310, 119, 310, 100, sw=1.0))
    o.append(_line(330, 138, 330, 144, sw=1.1))
    o.append(_res_v(330, 144, 174))
    o.append(T(342, 158, "R2", 7.6, anchor="start"))
    # OA1 inverting feedback node.
    o.append(_poly([(330, 100), (140, 100), (140, 73), (170, 73)], sw=1.1))
    # Lower source and its reference.
    o.append(_circle(108, 184, 2.6, fill="#ffffff", sw=1.1))
    o.append(_line(108, 184, 170, 184, sw=1.1))
    o.append(T(106, 170, "(e_n + e_2)", 7.6))
    o.append(_circle(108, 200, 2.2, fill=INK, sw=0))
    o.append(_gnd(108, 200))
    # OA2: as printed, plus upper at the resistor junction, minus lower.
    o.append(_op(170, 174, w=52, h=36, lab="OA2", plus="upper"))
    o.append(_poly([(330, 138), (140, 138), (140, 164), (170, 164)], sw=1.1))
    o.append(_line(222, 174, 330, 174, sw=1.1))
    o.append(T(284, 165, "eg2", 7.4))
    # Output differential amplifier OA3.
    o.append(_res_h(330, 440, 62, n=4))
    o.append(T(385, 53, "R", 7.4))
    o.append(_poly([(440, 62), (440, 107), (460, 107)], sw=1.1))
    o.append(_res_h(440, 530, 62, n=4))
    o.append(T(485, 53, "R", 7.4))
    o.append(_poly([(530, 62), (530, 118), (512, 118)], sw=1.1))
    o.append(_res_h(330, 440, 174, n=4))
    o.append(T(385, 165, "R", 7.4))
    o.append(_poly([(440, 174), (440, 129), (460, 129)], sw=1.1))
    o.append(_res_h(440, 530, 174, n=4))
    o.append(T(485, 165, "R", 7.4))
    o.append(_line(530, 174, 530, 186, sw=1.1))
    o.append(_gnd(530, 186))
    o.append(_op(460, 118, w=52, h=40, lab="OA3", plus="lower"))
    o.append(_line(512, 118, 600, 118, sw=1.1))
    o.append(_circle(600, 118, 2.6, fill="#ffffff", sw=1.1))
    o.append(T(612, 122, "eo", 7.8, anchor="start"))
    return _mk(12, o, "Instrumentation amplifier",
               "Bộ khuếch đại đo lường ba op-amp",
               "Three-op-amp instrumentation amplifier",
               "Sơ đồ bộ khuếch đại đo lường: OA1 và OA2 khuếch đại tín hiệu vi sai qua R1, RX và R2; OA3 tạo điện áp ra eo.",
               "Diagram of the instrumentation amplifier: OA1 and OA2 form the input stage with R1, RX and R2, and OA3 produces the output eo.")


# ---------------------------------------------------------------- 5.13
@_reg
def fig_f13():
    """Fig. 5.13 - multiplexed data acquisition chain."""
    o = []
    o.append(_b(40, 72, 92, 112,
                "Signal\nconditioning\nunit\n1\n2\n3\n...\nn", size=7.2))
    o.append(_b(172, 72, 92, 112,
                "Sample and\nhold unit\n1\n2\n3\n...\nn", size=7.2))
    o.append(_b(304, 72, 104, 112, "Analog\nmultiplexing\nunit", size=7.6))
    o.append(_ar(132, 100, 172, 100))
    o.append(_ar(264, 100, 304, 100))
    o.append(_b(452, 92, 68, 30, "ADC", size=8.0))
    o.append(_ar(408, 107, 452, 107))
    o.append(T(556, 99, "Output", 7.8, anchor="start"))
    o.append(T(556, 111, "1, 2, 3 ... n", 7.2, anchor="start"))
    o.append(_ar(520, 107, 548, 107))
    o.append(_b(360, 20, 272, 36,
                "Computer generated\naddress lines/decoder  1, 2, 3 ... n",
                size=7.0, fill="#f4f6fa"))
    o.append(_ar(420, 56, 392, 72))
    o.append(_ar(470, 56, 356, 80))
    o.append(_b(424, 166, 150, 38, "Control unit", size=8.0,
                fill="#f4f6fa"))
    o.append(_ar(424, 182, 410, 182))
    o.append(_poly([(410, 182), (410, 166)], sw=1.1))
    o.append(_ar(500, 166, 500, 122))
    o.append(T(340, 190, "Control", 7.0, anchor="end"))
    return _mk(13, o, "Multiplexed data acquisition chain",
               "Chuỗi thu thập số liệu ghép kênh",
               "Multiplexed data acquisition chain",
               "Sơ đồ khối: tín hiệu đã điều hòa đi qua bộ giữ mẫu, bộ ghép kênh tương tự và ADC tới đầu ra; đường địa chỉ và bộ điều khiển chọn kênh.",
               "Block diagram of conditioned signals passing through sample and hold, an analogue multiplexer and an ADC to the output, with address and control lines.")


# ---------------------------------------------------------------- 5.14
@_reg
def fig_f14():
    """Fig. 5.14 - two-to-four decoder built from AND gates."""
    o = []
    xs = [180, 240, 300, 360]
    labs = ["x", "x̄", "y", "ȳ"]
    for x, lab in zip(xs, labs):
        o.append(_line(x, 32, x, 196, sw=1.1))
        o.append(T(x, 26, lab, 8.2))
    # Gate inputs: pairs of (vertical line index, offset from gate centre).
    pairs = [(0, 0, 2, -6), (0, 0, 3, 6),
             (1, 1, 2, 7), (1, 1, 3, -7)]
    gys = [60, 100, 140, 180]
    for i, (a, da, b, db) in enumerate(pairs):
        gy = gys[i]
        for li, off in ((a, da), (b, db)):
            o.append(_line(xs[li], gy + off, 420, gy + off, sw=1.0))
        o.append(_and(420, gy, w=24, h=13, pins=2))
        o.append(T(456, gy + 3, str(i), 8.0, anchor="start"))
    o.append(T(120, 114, "Select inputs", 7.4, anchor="end"))
    return _mk(14, o, "Two-to-four decoder",
               "Bộ giải mã hai thành bốn",
               "Two-to-four decoder",
               "Mạch giải mã gồm bốn cổng AND nhận x, x bar, y và y bar để tạo bốn đầu ra từ 0 đến 3.",
               "Decoder built from four AND gates combining x, x bar, y and y bar to produce four outputs from 0 to 3.")


# ---------------------------------------------------------------- 5.15
@_reg
def fig_f15():
    """Fig. 5.15 - four-channel analogue switch matrix."""
    o = []
    o.append(T(126, 34, "Computer generated", 7.2))
    o.append(T(126, 45, "address lines", 7.2))
    o.append(_ar(126, 52, 126, 100))
    o.append(_b(80, 100, 74, 72, "Decoder", size=8.2))
    o.append(_b(570, 30, 92, 32, "Analog\ninputs", size=7.2))
    fx = [220, 300, 380, 460]
    o.append(_line(570, 46, 247, 46, sw=1.1))
    for i, x in enumerate(fx):
        o.append(_b(x, 62, 54, 40, "FETS\n%d" % (i + 1), size=7.6))
        o.append(_line(x + 27, 46, x + 27, 62, sw=1.1))
        o.append(_line(x + 27, 102, x + 27, 124, sw=1.1))
        o.append(_poly([(154, 128 + i * 14), (x + 27, 128 + i * 14),
                        (x + 27, 102)], sw=1.0, color=BLUE))
    o.append(_line(247, 124, 540, 124, sw=1.1))
    o.append(_ar(540, 124, 582, 124))
    o.append(T(588, 128, "Analog output", 7.4, anchor="start"))
    return _mk(15, o, "Analogue switch matrix",
               "Ma trận khóa tương tự",
               "Analogue switch matrix",
               "Bộ giải mã chọn một trong bốn khóa FET để nối một ngõ vào tương tự với đường đầu ra chung.",
               "A decoder selects one of four FET switches that connect an analogue input to the common output line.")


# ---------------------------------------------------------------- 5.16
@_reg
def fig_f16():
    """Fig. 5.16 - four-to-one digital multiplexer."""
    o = []
    ys = [70, 100, 130, 160]
    o.append(T(82, 44, "Input lines", 7.6, anchor="start"))
    for i, y in enumerate(ys):
        o.append(_circle(52, y, 2.2, fill="#ffffff", sw=1.0))
        o.append(T(44, y + 3, str(i), 7.6, anchor="end"))
        o.append(_line(52, y, 300, y, sw=1.05))
    sx = [100, 140, 180, 220]
    sl = ["x", "x̄", "y", "ȳ"]
    for x, lab in zip(sx, sl):
        o.append(_line(x, 52, x, 176, sw=1.0))
        o.append(T(x, 46, lab, 8.0))
    o.append(T(282, 46, "Select lines", 7.4))
    o.append(_ar(276, 43, 226, 43))
    sel_pairs = [(0, 1), (0, 3), (1, 2), (1, 3)]
    for i, y in enumerate(ys):
        a, b = sel_pairs[i]
        for k, li in enumerate((a, b)):
            py = y - 6 + k * 12
            o.append(_line(sx[li], py, 300, py, sw=0.95, color=BLUE))
        o.append(_and(300, y, w=26, h=14, pins=3))
        o.append(_line(326, y, 380, (88, 101, 115, 128)[i], sw=1.0))
    o.append(_or(380, 108, w=58, h=62))
    o.append(_ar(438, 108, 566, 108))
    o.append(T(574, 112, "Output", 8.0, anchor="start"))
    return _mk(16, o, "Four-to-one digital multiplexer",
               "Bộ ghép kênh số bốn chọn một",
               "Four-to-one digital multiplexer",
               "Bốn ngõ vào 0 đến 3 được chọn qua các đường x, x bar, y và y bar; bốn cổng AND và một cổng OR tạo đầu ra.",
               "Four inputs 0 to 3 are selected by x, x bar, y and y bar; four AND gates feed one OR gate at the output.")


# ---------------------------------------------------------------- 5.17
@_reg
def fig_f17():
    """Fig. 5.17 - relay operated sample and hold circuit."""
    o = []
    o.append(_circle(66, 60, 2.6, fill="#ffffff", sw=1.1))
    o.append(T(62, 56, "Vin", 7.8, anchor="end"))
    o.append(_line(66, 60, 180, 60, sw=1.1))
    o.append(_circle(180, 60, 2.4, fill="#ffffff", sw=1.1))
    o.append(_circle(202, 60, 2.4, fill="#ffffff", sw=1.1))
    o.append(_line(181, 59, 199, 49, sw=1.3, color=RED))
    o.append(T(222, 50, "Contact", 7.6, anchor="start"))
    o.append(_line(202, 60, 602, 60, sw=1.1))
    o.append(_circle(602, 60, 2.6, fill="#ffffff", sw=1.1))
    o.append(T(614, 64, "Vout", 7.8, anchor="start"))
    o.append(_line(440, 60, 440, 104, sw=1.1))
    o.append(_cap(440, 104, "Ch"))
    o.append(_line(440, 108, 440, 122, sw=1.1))
    o.append(_gnd(440, 122))
    # Relay coil and its mechanical link to the contact.
    o.append(_poly([(190, 56), (190, 86)], sw=1.0, color=GREY, dash="3,2"))
    for cy in (94, 102, 110, 118):
        o.append(_ellipse(190, cy, 7, 4.2, fill="#ffffff", sw=1.1))
    o.append(_line(190, 122, 190, 144, sw=1.0))
    o.append(T(214, 108, "Relay coil", 7.6, anchor="start"))
    o.append(_line(130, 144, 250, 144, sw=1.0))
    o.append(_line(130, 144, 130, 182, sw=1.0))
    o.append(_line(250, 144, 250, 182, sw=1.0))
    o.append(_circle(130, 184, 2.6, fill="#ffffff", sw=1.0))
    o.append(_circle(250, 184, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(190, 204, "Switching pulses", 7.8))
    return _mk(17, o, "Relay sample and hold circuit",
               "Mạch giữ mẫu dùng rơ le",
               "Relay sample and hold circuit",
               "Công tắc do rơ le điều khiển nạp tụ giữ Ch từ Vin trong kỳ lấy mẫu và giữ điện áp tại Vout.",
               "A relay operated contact charges the holding capacitor Ch from Vin during sampling and holds the voltage at Vout.")


# ---------------------------------------------------------------- 5.18
@_reg
def fig_f18():
    """Fig. 5.18 - FET switch sample and hold circuit."""
    o = []
    o.append(_circle(66, 100, 2.6, fill="#ffffff", sw=1.1))
    o.append(T(60, 96, "Vin", 7.8, anchor="end"))
    o.append(_line(66, 100, 177, 100, sw=1.1))
    o.append(_circle(190, 100, 13, fill="#ffffff", sw=1.2))
    o.append(_line(190, 88, 190, 112, sw=1.1))
    o.append(_poly([(185, 76), (195, 76), (190, 86)],
                   fill="#ffffff", sw=1.0, color=BLUE))
    o.append(T(190, 68, "FET switch", 7.6))
    o.append(_ar(190, 146, 190, 116, color=BLUE))
    o.append(T(190, 160, "Driver pulse", 7.6))
    o.append(_line(203, 100, 320, 100, sw=1.1))
    o.append(_line(320, 100, 320, 140, sw=1.1))
    o.append(_cap(320, 140, "Ch"))
    o.append(_line(320, 144, 320, 158, sw=1.1))
    o.append(_gnd(320, 158))
    o.append(_poly([(320, 100), (320, 112), (400, 112)], sw=1.1))
    o.append(_op(400, 100, w=54, h=44, lab="", plus="lower"))
    o.append(_poly([(454, 100), (472, 100), (472, 78),
                    (370, 78), (370, 88), (400, 88)], sw=1.1))
    o.append(_circle(472, 100, 2.2, fill=INK, sw=0))
    o.append(_line(472, 100, 602, 100, sw=1.1))
    o.append(_circle(602, 100, 2.6, fill="#ffffff", sw=1.1))
    o.append(T(614, 104, "Vout", 7.8, anchor="start"))
    o.append(T(464, 142, "Voltage follower", 7.6, anchor="start"))
    return _mk(18, o, "FET sample and hold circuit",
               "Mạch giữ mẫu dùng khóa FET",
               "FET sample and hold circuit",
               "Khóa FET điều khiển bằng xung nạp tụ Ch; bộ đệm hệ số một trở kháng cao đưa điện áp đã giữ ra Vout.",
               "A pulse driven FET switch charges Ch; a high impedance voltage follower buffers the held voltage to Vout.")


# ---------------------------------------------------------------- 5.19
@_reg
def fig_f19():
    """Fig. 5.19 - voltage to time conversion waveform diagram."""
    o = []
    x0, x1 = 150, 600
    # Reference levels.
    for y, lab in ((50, "+12V"), (82, "Unknown voltage"),
                   (112, "O"), (148, "−12V")):
        o.append(_line(120, y, x1, y, sw=0.8, color=GREY, dash="5,4"))
        o.append(T(114, y + 3, lab, 7.2, anchor="end"))
    o.append(T(114, 93, "to be measured", 7.2, anchor="end"))
    o.append(T(114, 184, "Time for gating", 7.2, anchor="end"))
    o.append(T(114, 214, "Clock pulse", 7.2, anchor="end"))
    # Ramp waveform from +12 V down to −12 V and back.
    o.append(_poly([(300, 50), (420, 148), (500, 50)], sw=2.0, color=BLUE))
    o.append(_ar(500, 50, 600, 50, color=GREY, sw=0.8))
    o.append(T(470, 126, "Ramp voltage", 7.6))
    o.append(_line(470, 130, 452, 135, sw=0.9, color=BLUE))
    # Start instant and crossing markers.
    o.append(_line(300, 38, 300, 224, sw=0.9, color=GREY, dash="4,4"))
    o.append(T(300, 32, "Start instant of measurement", 7.2))
    cx, cy = 339.2, 82.0
    o.append(_line(cx, cy, cx, 200, sw=0.9, color=GREY, dash="4,4"))
    o.append(_star(cx, cy))
    o.append(_star(376, 112))
    o.append(T(410, 76, "Point of coincidence", 7.2))
    o.append(_line(406, 79, 343, 82, sw=0.9, color=GREY))
    # Gating interval and gated clock pulses.
    o.append(_poly([(cx, 180), (cx + 3, 177), (cx - 3, 183)],
                   fill="none", sw=1.0, color=RED))
    o.append(_poly([(376, 180), (373, 177), (379, 183)],
                   fill="none", sw=1.0, color=RED))
    o.append(_line(cx + 3, 180, 373, 180, sw=1.2, color=RED))
    o.append(T(357, 198, "t", 8.0))
    o.append(_line(120, 224, 600, 224, sw=1.0))
    o.append(_clock(cx, 376, 208, hi=11, count=4))
    o.append(T(612, 228, "t", 7.6, anchor="start"))
    return _mk(19, o, "Voltage to time conversion",
               "Chuyển đổi điện áp sang thời gian",
               "Voltage to time conversion",
               "Đồ thị điện áp dốc cắt mức cần đo và mức zero; khoảng thời gian giữa hai điểm cắt quyết định số xung đồng hồ được đếm.",
               "Ramp waveform crossing the unknown level and zero; the interval between the crossings sets the number of clock pulses counted.")


# ---------------------------------------------------------------- 5.20
@_reg
def fig_f20():
    """Fig. 5.20 - ramp type ADC block diagram."""
    o = []
    o.append(T(46, 66, "Signal input", 7.4, anchor="start"))
    o.append(T(46, 78, "after conditioning", 7.4, anchor="start"))
    o.append(_ar(58, 82, 118, 82))
    o.append(_op(118, 82, w=70, h=44, plus="lower"))
    o.append(T(150, 84, "Input comparator", 6.4))
    o.append(_line(188, 82, 268, 82, sw=1.1))
    o.append(_ar(268, 82, 268, 112))
    o.append(T(274, 100, "Start pulse", 7.2, anchor="start"))
    o.append(_b(196, 132, 72, 34, "Clock\noscillator", size=7.0))
    o.append(_b(278, 112, 50, 34, "Gate", size=8.0))
    o.append(_ar(268, 149, 278, 132, color=BLUE))
    o.append(_b(350, 112, 60, 34, "Counter", size=7.8))
    o.append(_b(430, 112, 60, 34, "Output", size=7.8))
    o.append(_ar(328, 129, 350, 129))
    o.append(_ar(410, 129, 430, 129))
    o.append(_b(76, 172, 80, 34, "Ramp\ngenerator", size=7.2))
    o.append(_ar(156, 189, 196, 177))
    o.append(_ar(118, 172, 118, 94, color=BLUE))
    o.append(_op(196, 189, w=70, h=44, plus="lower"))
    o.append(T(226, 190, "Ground comparator", 6.4))
    o.append(_line(216, 213, 216, 218, sw=1.0))
    o.append(_gnd(216, 218))
    o.append(_poly([(266, 189), (292, 189), (292, 146)], sw=1.1))
    o.append(T(272, 174, "Stop pulse", 7.0, anchor="end"))
    o.append(_b(76, 202, 92, 26, "Sample rate\nmultivibrator", size=6.2))
    o.append(_ar(122, 202, 122, 206))
    o.append(_poly([(168, 215), (380, 215), (380, 146)], sw=1.0, color=BLUE))
    o.append(_ar(380, 152, 380, 146, color=BLUE))
    return _mk(20, o, "Ramp type ADC block diagram",
               "Sơ đồ khối ADC loại dốc",
               "Ramp type ADC block diagram",
               "Bộ so sánh đầu vào và bộ so sánh đất mở, đóng cổng; xung đồng hồ đi qua cổng tới bộ đếm và đầu ra.",
               "The input and ground comparators open and close the gate; clock pulses pass through to the counter and output.")


# ---------------------------------------------------------------- 5.21
@_reg
def fig_f21():
    """Fig. 5.21 - three constant input voltage levels."""
    o = []
    o.append(_ar(100, 202, 618, 202))
    o.append(_ar(100, 202, 100, 42))
    o.append(T(616, 214, "Time", 7.8, anchor="end"))
    for i, (yy, lab) in enumerate(((80, "Ei3"), (120, "Ei2"), (160, "Ei1"))):
        o.append(_line(100, yy, 520, yy, sw=1.3, color=BLUE))
        o.append(T(528, yy + 3, lab, 8.0, anchor="start"))
    o.append(T(88, 58, "Input", 7.4, anchor="end"))
    o.append(T(88, 70, "voltage", 7.4, anchor="end"))
    o.append(T(88, 82, "level", 7.4, anchor="end"))
    o.append(T(88, 216, "O", 7.6, anchor="end"))
    return _mk(21, o, "Input voltage levels",
               "Mức điện áp đầu vào",
               "Input voltage levels",
               "Đồ thị ba mức điện áp đầu vào không đổi Ei1, Ei2 và Ei3 theo thời gian.",
               "Graph of three constant input voltage levels Ei1, Ei2 and Ei3 versus time.")


# ---------------------------------------------------------------- 5.22
@_reg
def fig_f22():
    """Fig. 5.22 - integrator output ramps for three input levels."""
    o = []
    o.append(_ar(150, 54, 620, 54))
    o.append(_ar(150, 54, 150, 214))
    o.append(T(618, 48, "Time", 7.8, anchor="end"))
    o.append(T(138, 82, "Output", 7.4, anchor="end"))
    o.append(T(138, 94, "voltage", 7.4, anchor="end"))
    o.append(T(138, 106, "level", 7.4, anchor="end"))
    o.append(T(136, 50, "O", 7.6, anchor="end"))
    for ex, ey, lab in ((596, 122, "Eo3"), (430, 182, "Eo2"),
                        (302, 212, "Eo1")):
        o.append(_ar(150, 54, ex, ey, color=BLUE))
        o.append(T(ex + 6, ey + 4, lab, 8.0, anchor="start"))
    return _mk(22, o, "Integrator output ramps",
               "Đường dốc đầu ra bộ tích phân",
               "Integrator output ramps",
               "Đồ thị ba đường dốc đầu ra Eo1, Eo2 và Eo3; điện áp đầu vào càng lớn thì độ dốc càng dốc.",
               "Graph of three output ramps Eo1, Eo2 and Eo3; a higher input voltage gives a steeper slope.")
