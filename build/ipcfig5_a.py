# -*- coding: utf-8 -*-
"""Figures 5.1-5.11 for IPC Chapter 5 (signal conditioning and DAQ).

Supplier module ``_a``: DAQ block schemes, power pack, chopper amplifier and
the basic operational-amplifier arithmetic circuits.  Every figure is a
simplified vector redraw of the printed original; all labels stay inside the
680 x 250 canvas and above y = 232 (the 5.n strip sits at y = 245).
"""
from ipcfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _zig_h(x1, x2, y, n=5, amp=3.0, color=INK):
    """Horizontal zig-zag resistor between two end points."""
    pts = []
    for i in range(2 * n + 1):
        pts.append((x1 + (x2 - x1) * i / float(2 * n),
                    y + (amp if i % 2 else -amp)))
    return _poly(pts, sw=1.1, color=color)


def _zig_v(x, y1, y2, n=5, amp=3.0, color=INK):
    """Vertical zig-zag resistor between two end points."""
    pts = []
    for i in range(2 * n + 1):
        pts.append((x + (amp if i % 2 else -amp),
                    y1 + (y2 - y1) * i / float(2 * n)))
    return _poly(pts, sw=1.1, color=color)


def _cap_h(x, y, color=INK):
    """Capacitor inserted in a horizontal wire (two vertical plates)."""
    return (_line(x - 4, y - 7, x - 4, y + 7, sw=1.2, color=color)
            + _line(x + 4, y - 7, x + 4, y + 7, sw=1.2, color=color))


def _cap_v(x, y, color=INK):
    """Capacitor inserted in a vertical wire (two horizontal plates)."""
    return (_line(x - 7, y - 4, x + 7, y - 4, sw=1.2, color=color)
            + _line(x - 7, y + 4, x + 7, y + 4, sw=1.2, color=color))


def _coil_v(x, y1, y2, n=8, amp=5.0, color=INK):
    """Transformer winding drawn as a stack of small semicircular bumps."""
    seg = (y2 - y1) / float(n)
    d = "M%.1f,%.1f" % (x, y1)
    for i in range(n):
        d += " A%.1f,%.1f 0 0 0 %.1f,%.1f" % (
            amp, seg / 2.0, x, y1 + seg * (i + 1))
    return _path(d, sw=1.1, color=color)


def _diode_h(x, y, direction=1, color=INK):
    """Diode in a horizontal wire; direction 1 points right, -1 points left."""
    if direction > 0:
        tri = [(x - 6, y - 5), (x - 6, y + 5), (x + 3, y)]
        bx = x + 4
    else:
        tri = [(x + 6, y - 5), (x + 6, y + 5), (x - 3, y)]
        bx = x - 4
    return (_poly(tri, fill="#ffffff", sw=1.1, color=color, close=True)
            + _line(bx, y - 6, bx, y + 6, sw=1.2, color=color))


def _zener_v(x, y, color=INK):
    """Zener diode pointing upward with a bent cathode bar."""
    return (_poly([(x - 5, y + 5), (x + 5, y + 5), (x, y - 4)],
                  fill="#ffffff", sw=1.1, color=color, close=True)
            + _poly([(x - 9, y - 3), (x - 6, y - 6),
                     (x + 6, y - 6), (x + 9, y - 3)], sw=1.1, color=color))


def _gnd(x, y, color=INK):
    """Standard ground symbol, with the connection point at (x, y)."""
    return (_line(x, y - 7, x, y, sw=1.0, color=color)
            + _line(x - 7, y, x + 7, y, sw=1.1, color=color)
            + _line(x - 4.5, y + 3, x + 4.5, y + 3, sw=0.9, color=color)
            + _line(x - 2, y + 6, x + 2, y + 6, sw=0.8, color=color))


def _oa(x, y, w, h, label="OA"):
    """Op-amp triangle: left edge x..x+w, tip at (x+w, y+h/2).

    Inverting terminal sits at (x, y+0.3h), non-inverting at (x, y+0.7h).
    """
    o = [_poly([(x, y), (x, y + h), (x + w, y + h / 2.0)],
               fill="#ffffff", sw=1.3, close=True)]
    o.append(T(x + 11, y + 0.3 * h + 2.8, "-", 8.6, anchor="start"))
    o.append(T(x + 11, y + 0.7 * h + 2.8, "+", 8.6, anchor="start"))
    o.append(T(x + w * 0.62, y + h / 2.0 + 2.8, label, 7.2))
    return "".join(o)


# ---------------------------------------------------------------- 5.1
@_reg
def fig_f01():
    """Fig. 5.1 - DAQ blocks: transducers, conditioner, multiplexer, ADC."""
    o = [_defs()]
    # three tall channel blocks
    o.append(_rect(24, 52, 96, 136, fill="#eef3fb", sw=1.3))
    for i, ln in enumerate(("Analog", "signals from", "transducers")):
        o.append(T(72, 65 + i * 11, ln, 7.2))
    for i, lab in enumerate(("1", "2", "3", "...", "...", "n")):
        o.append(T(72, 106 + i * 14, lab, 7.2))

    o.append(_rect(176, 52, 96, 136, fill="#eef3fb", sw=1.3))
    for i, ln in enumerate(("Signals", "conditioner", "unit")):
        o.append(T(224, 65 + i * 11, ln, 7.2))
    for i, lab in enumerate(("1", "2", "3", "...", "...", "n")):
        o.append(T(224, 106 + i * 14, lab, 7.2))

    o.append(_rect(330, 72, 80, 96, fill="#fbfaf7", sw=1.3))
    for i, ln in enumerate(("Multi-", "plexing", "unit")):
        o.append(T(370, 112 + i * 13, ln, 7.6))

    # parallel signal paths between the channel blocks
    for yy in (96, 110, 124, 138, 152):
        o.append(_ar(120, yy, 174, yy, sw=1.3))
        o.append(_ar(272, yy, 328, yy, sw=1.3))

    o.append(_rect(466, 104, 64, 44, fill="#eef3fb", sw=1.3))
    o.append(T(498, 131, "ADC", 8.6))
    o.append(_ar(410, 126, 464, 126, sw=1.4))
    o.append(_ar(530, 126, 542, 126, sw=1.4))
    o.append(T(548, 130, "To PC", 7.6, anchor="start"))
    return _mk(1, o, "Data acquisition block diagram",
               "Sơ đồ khối hệ thống thu thập dữ liệu từ cảm biến tới máy tính",
               "Block diagram of a data acquisition system from transducers to a PC",
               "Sơ đồ gồm bốn khối theo thứ tự: tín hiệu tương tự từ cảm biến, bộ điều chỉnh tín hiệu, bộ ghép kênh và bộ ADC, sau đó tín hiệu số được đưa tới máy tính. Các đường song song biểu thị nhiều kênh đầu vào đánh số từ 1 tới n.",
               "Diagram with four blocks in order: analog signals from transducers, a signal conditioner unit, a multiplexing unit and an ADC, with the digital output fed to a PC. Parallel lines represent the numbered input channels from 1 to n.")


# ---------------------------------------------------------------- 5.2
@_reg
def fig_f02():
    """Fig. 5.2 - data logging scheme with electronic transmitters."""
    o = [_defs()]
    o.append(_rect(250, 24, 180, 32, fill="#eef3fb", sw=1.3))
    o.append(T(340, 44, "Unit operation process", 7.8))

    o.append(_rect(160, 30, 44, 22, fill="#fbfaf7", sw=1.1))
    o.append(T(182, 45, "Tx5", 7.2))
    o.append(_ar(250, 41, 204, 41, sw=1.2))

    o.append(_rect(476, 30, 44, 22, fill="#fbfaf7", sw=1.1))
    o.append(T(498, 45, "Tx6", 7.2))
    o.append(_ar(430, 41, 476, 41, sw=1.2))

    # Tx1 fed from the left side of the process
    o.append(_line(250, 30, 110, 30, sw=1.0))
    o.append(_ar(110, 30, 110, 66, sw=1.2))
    o.append(_rect(88, 66, 44, 22, fill="#fbfaf7", sw=1.1))
    o.append(T(110, 81, "Tx1", 7.2))

    for xx, lab in ((250, "Tx2"), (310, "Tx3"), (370, "Tx4")):
        o.append(_rect(xx, 66, 44, 22, fill="#fbfaf7", sw=1.1))
        o.append(T(xx + 22, 81, lab, 7.2))
        o.append(_ar(xx + 22, 56, xx + 22, 66, sw=1.1))

    # multiplexer and all transmitter feeds
    o.append(_rect(196, 100, 288, 28, fill="#eef3fb", sw=1.3))
    o.append(T(340, 118, "Multiplexing unit", 7.8))
    o.append(_poly([(110, 88), (110, 114), (194, 114)], sw=1.1))
    o.append(_ar(180, 114, 196, 114, sw=1.1))
    o.append(_poly([(182, 52), (182, 108), (194, 108)], sw=1.1))
    o.append(_ar(180, 108, 196, 108, sw=1.1))
    o.append(_poly([(498, 52), (530, 52), (530, 104), (484, 104)], sw=1.1))
    o.append(_ar(500, 104, 484, 104, sw=1.1))
    for xx in (272, 332, 392):
        o.append(_ar(xx, 88, xx, 100, sw=1.1))

    # A/D converter and computer
    o.append(_rect(310, 138, 60, 24, fill="#eef3fb", sw=1.2))
    o.append(T(340, 148, "A/D", 7.4))
    o.append(T(340, 158, "convertor", 6.8))
    o.append(_ar(340, 128, 340, 138, sw=1.2))
    o.append(_rect(285, 172, 110, 26, fill="#eef3fb", sw=1.3))
    o.append(T(340, 188, "Computer system", 7.8))
    o.append(_ar(340, 162, 340, 172, sw=1.2))

    # address lines from the computer back to the multiplexer
    o.append(_poly([(380, 198), (380, 202), (505, 202), (505, 124)], sw=1.0,
                   color=GREY))
    o.append(_ar(505, 124, 484, 124, sw=1.1, color=GREY))
    o.append(T(511, 128, "Address", 7.0, anchor="start", color=GREY))
    o.append(T(511, 138, "lines", 7.0, anchor="start", color=GREY))

    o.append(_rect(100, 176, 100, 22, fill="#fbfaf7", sw=1.1))
    o.append(T(150, 190, "Generation of alarms", 7.0))
    o.append(_ar(285, 183, 200, 183, sw=1.2))
    o.append(_rect(420, 176, 80, 22, fill="#fbfaf7", sw=1.1))
    o.append(T(460, 190, "Hard copier", 7.4))
    o.append(_ar(395, 183, 420, 183, sw=1.2))

    o.append(_rect(290, 208, 100, 20, fill="#fbfaf7", sw=1.1))
    o.append(T(340, 221, "Operator station", 7.2))
    o.append(_ar(335, 198, 335, 208, sw=1.0))
    o.append(_ar(345, 208, 345, 198, sw=1.0))
    o.append(_rect(140, 208, 100, 20, fill="#fbfaf7", sw=1.1))
    o.append(T(190, 221, "Auxiliary storage", 7.2))
    o.append(_ar(290, 218, 240, 218, sw=1.2))
    return _mk(2, o, "Data acquisition scheme",
               "Sơ đồ thu thập dữ liệu với các bộ phát và máy tính điều khiển",
               "Data acquisition scheme using field transmitters and a computer system",
               "Sơ đồ hệ thống ghi dữ liệu: các bộ phát Tx1 tới Tx6 từ quá trình công nghệ đi vào bộ ghép kênh, qua bộ chuyển đổi A/D tới máy tính; máy tính điều khiển địa chỉ và nối tới bảng cảnh báo, máy in, bộ nhớ phụ và trạm người vận hành.",
               "Data logging scheme: transmitters Tx1 to Tx6 from the unit operation process feed a multiplexing unit, then an A/D convertor and a computer system; the computer drives the address lines and links to alarm generation, a hard copier, auxiliary storage and an operator station.")


# ---------------------------------------------------------------- 5.3
@_reg
def fig_f03():
    """Fig. 5.3 - power pack unit and its application blocks."""
    o = [_defs()]
    o.append(_rect(250, 32, 120, 30, fill="#eef3fb", sw=1.2))
    o.append(T(310, 51, "Power pack unit", 7.4))
    o.append(_ar(310, 62, 310, 80, sw=1.3))

    o.append(_rect(250, 82, 120, 34, fill="#fbfaf7", sw=1.2))
    o.append(T(310, 96, "Measurement", 7.6))
    o.append(T(310, 107, "circuit", 7.6))
    o.append(T(146, 96, "Sensor", 7.4, anchor="end"))
    o.append(T(146, 107, "signal", 7.4, anchor="end"))
    o.append(_ar(150, 101, 250, 101, sw=1.3))

    o.append(_rect(250, 138, 120, 30, fill="#fbfaf7", sw=1.2))
    o.append(T(310, 157, "Calibration adjustment", 7.2))
    o.append(_ar(310, 138, 310, 117, sw=1.3))

    o.append(_rect(410, 82, 150, 34, fill="#eef3fb", sw=1.2))
    o.append(T(485, 96, "Instrumentation", 7.6))
    o.append(T(485, 107, "amplifier", 7.6))
    o.append(_ar(370, 99, 410, 99, sw=1.3))

    o.append(_rect(440, 138, 90, 30, fill="#fbfaf7", sw=1.2))
    o.append(T(485, 157, "Filter", 7.6))
    o.append(_ar(485, 116, 485, 138, sw=1.3))
    o.append(_rect(570, 138, 80, 30, fill="#eef3fb", sw=1.2))
    o.append(T(610, 157, "Output", 7.6))
    o.append(_ar(530, 153, 570, 153, sw=1.3))
    return _mk(3, o, "Power pack unit block diagram",
               "Sơ đồ khối nguồn nuôi cho mạch đo và bộ khuếch đại",
               "Block diagram of a power pack unit supplying the measurement circuit and amplifier",
               "Sơ đồ khối thể hiện nguồn nuôi cấp điện cho mạch đo; tín hiệu cảm biến và bộ chỉnh chu đi vào mạch đo, đầu ra mạch đo được khuếch đại, lọc rồi đưa tới đầu ra.",
               "Block diagram of a power pack supplying the measurement circuit: the sensor signal and calibration adjustment feed the measurement circuit, whose output passes through an instrumentation amplifier and a filter to the output.")


# ---------------------------------------------------------------- 5.4
@_reg
def fig_f04():
    """Fig. 5.4 - transformer, rectifier and regulated dual supply."""
    o = [_defs()]
    # transformer, primary with AC input and centre-tapped secondary
    o.append(_circle(70, 58, 2.8, fill="#ffffff", sw=1.1))
    o.append(_circle(70, 176, 2.8, fill="#ffffff", sw=1.1))
    o.append(_line(70, 61, 70, 68, sw=1.0))
    o.append(_line(70, 166, 70, 173, sw=1.0))
    o.append(_ar(52, 62, 52, 172, sw=1.0, color=GREY))
    o.append(_ar(52, 172, 52, 62, sw=1.0, color=GREY))
    o.append(T(42, 114, "A.C", 7.2, anchor="end"))
    o.append(T(42, 125, "supply", 7.2, anchor="end"))
    o.append(_coil_v(70, 68, 166))
    o.append(_line(88, 64, 88, 170, sw=2.0))
    o.append(_line(94, 64, 94, 170, sw=2.0))
    o.append(T(112, 48, "Transformer", 7.4))
    o.append(_coil_v(116, 68, 166))

    # full-wave rectifier using the two D1 diodes
    o.append(_line(116, 68, 160, 68, sw=1.1))
    o.append(_diode_h(168, 68))
    o.append(_line(176, 68, 250, 68, sw=1.1))
    o.append(_line(116, 166, 160, 166, sw=1.1))
    o.append(_diode_h(168, 166))
    o.append(_line(176, 166, 270, 166, sw=1.1))
    o.append(_line(270, 166, 270, 68, sw=1.1))
    o.append(T(168, 56, "D1", 7.2))
    o.append(T(168, 154, "D1", 7.2))
    # centre tap forms the negative rail
    o.append(_poly([(116, 117), (300, 117), (300, 160), (620, 160)], sw=1.1))

    # reservoir capacitor and series resistor
    o.append(_line(250, 68, 250, 93, sw=1.1))
    o.append(_cap_v(250, 97))
    o.append(_line(250, 101, 250, 117, sw=1.1))
    o.append(T(264, 101, "C", 7.2, anchor="start"))
    o.append(_line(270, 68, 290, 68, sw=1.1))
    o.append(_zig_h(290, 350, 68))
    o.append(T(320, 56, "R", 7.2))
    o.append(_line(350, 68, 620, 68, sw=1.1))

    # zener/resistor regulator ladder
    o.append(_line(450, 68, 450, 84, sw=1.1))
    o.append(_zener_v(450, 90))
    o.append(_line(450, 96, 450, 102, sw=1.1))
    o.append(_zig_v(450, 102, 124))
    o.append(T(464, 113, "R", 7.2, anchor="start"))
    o.append(_zener_v(450, 130))
    o.append(_line(450, 136, 450, 142, sw=1.1))
    o.append(_zig_v(450, 142, 160))
    o.append(T(464, 151, "R", 7.2, anchor="start"))
    o.append(T(464, 90, "D2", 7.2, anchor="start"))
    o.append(T(464, 130, "D2", 7.2, anchor="start"))

    # the two series transistors and the ground reference
    o.append(_circle(530, 96, 9, fill="#ffffff", sw=1.1))
    o.append(_line(524, 90, 524, 102, sw=1.1))
    o.append(_poly([(526, 91), (537, 78), (540, 68)], sw=1.1))
    o.append(_poly([(526, 101), (537, 108), (540, 116)], sw=1.1))
    o.append(_poly([(524, 96), (500, 116), (450, 116)], sw=1.0))
    o.append(T(546, 84, "Q1", 7.2, anchor="start"))
    o.append(_circle(530, 142, 9, fill="#ffffff", sw=1.1))
    o.append(_line(524, 136, 524, 148, sw=1.1))
    o.append(_poly([(526, 137), (537, 128), (540, 116)], sw=1.1))
    o.append(_poly([(526, 147), (537, 156), (540, 160)], sw=1.1))
    o.append(_poly([(524, 142), (500, 140), (450, 140)], sw=1.0))
    o.append(T(546, 156, "Q2", 7.2, anchor="start"))
    o.append(_line(540, 116, 566, 116, sw=1.1))
    o.append(_gnd(566, 116))

    # regulated output terminals
    o.append(_circle(620, 68, 2.8, fill="#ffffff", sw=1.1))
    o.append(T(632, 72, "+Vx", 7.4, anchor="start"))
    o.append(_circle(620, 160, 2.8, fill="#ffffff", sw=1.1))
    o.append(T(632, 164, "-Vx", 7.4, anchor="start"))
    return _mk(4, o, "Transformer and regulated filter circuit",
               "Mạch nguồn gồm máy biến áp, chỉnh lưu, tụ lọc và ổn áp hai cực",
               "Power supply with transformer, rectifier, filter capacitor and dual regulator",
               "Sơ đồ mạch nguồn: máy biến áp có cuộn giữa, hai diode D1 chỉnh lưu toàn sóng, tụ C và điện trở R lọc, sau đó mạch ổn áp gồm hai diode zener D2, hai điện trở R và hai transistor Q1, Q2 cho đầu ra +Vx và -Vx.",
               "Circuit diagram of the power pack: a centre-tapped transformer, two D1 rectifier diodes, a filter capacitor C and resistor R, followed by a regulator with two D2 zener diodes, two resistors and transistors Q1 and Q2 producing the +Vx and -Vx rails.")


# ---------------------------------------------------------------- 5.5
@_reg
def fig_f05():
    """Fig. 5.5 - chopper-modulated amplifier block scheme."""
    o = [_defs()]
    # upper row: DC input chopped into AC through a transformer
    o.append(T(90, 66, "Input", 7.2, anchor="end"))
    o.append(T(90, 76, "signal in", 7.2, anchor="end"))
    o.append(T(90, 86, "D.C.", 7.2, anchor="end"))
    o.append(_ar(92, 68, 110, 68, sw=1.1))
    o.append(_ar(92, 88, 110, 88, sw=1.1))
    o.append(_rect(110, 62, 18, 12, fill="#fbfaf7", sw=1.1))
    o.append(_rect(110, 82, 18, 12, fill="#fbfaf7", sw=1.1))
    o.append(T(119, 50, "Chopper", 7.0))
    o.append(_line(128, 68, 170, 68, sw=1.1))
    o.append(_line(128, 88, 170, 88, sw=1.1))
    o.append(_line(150, 68, 150, 100, sw=1.0))
    o.append(_gnd(150, 100))
    o.append(_coil_v(190, 62, 94, n=6, amp=4))
    o.append(_line(170, 68, 190, 62, sw=1.1))
    o.append(_line(170, 88, 190, 94, sw=1.1))
    o.append(_line(206, 58, 206, 98, sw=1.8))
    o.append(_line(212, 58, 212, 98, sw=1.8))
    o.append(_coil_v(230, 62, 94, n=6, amp=4))
    o.append(_line(230, 62, 290, 62, sw=1.1))
    o.append(_line(230, 94, 290, 94, sw=1.1))
    o.append(_circle(290, 62, 2.6, fill="#ffffff", sw=1.0))
    o.append(_circle(290, 94, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(304, 66, "A.C.", 7.4, anchor="start"))
    o.append(T(304, 77, "output", 7.4, anchor="start"))

    # lower row: amplifier, coupling transformer and rectifier/filter
    o.append(_line(43, 150, 70, 150, sw=1.1))
    o.append(_line(43, 190, 70, 190, sw=1.1))
    o.append(_circle(40, 150, 2.6, fill="#ffffff", sw=1.0))
    o.append(_circle(40, 190, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(28, 166, "A.C.", 7.2, anchor="end"))
    o.append(T(28, 177, "input", 7.2, anchor="end"))
    o.append(_rect(70, 135, 140, 70, fill="#eef3fb", sw=1.3))
    o.append(T(140, 173, "Amplifier", 8.0))
    o.append(_line(210, 150, 250, 150, sw=1.1))
    o.append(_line(210, 190, 250, 190, sw=1.1))
    o.append(_coil_v(250, 146, 194, n=7, amp=4))
    o.append(_line(266, 141, 266, 199, sw=1.8))
    o.append(_line(272, 141, 272, 199, sw=1.8))
    o.append(_coil_v(290, 146, 194, n=7, amp=4))
    o.append(_line(290, 150, 330, 150, sw=1.1))
    o.append(_line(290, 190, 330, 190, sw=1.1))
    o.append(_rect(330, 135, 120, 70, fill="#eef3fb", sw=1.3))
    o.append(T(390, 168, "Rectifier", 8.0))
    o.append(T(390, 180, "and filter", 8.0))
    o.append(_line(450, 150, 500, 150, sw=1.1))
    o.append(_line(450, 190, 500, 190, sw=1.1))
    o.append(_circle(500, 150, 2.6, fill="#ffffff", sw=1.0))
    o.append(_circle(500, 190, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(514, 166, "D.C.", 7.4, anchor="start"))
    o.append(T(514, 177, "output", 7.4, anchor="start"))
    return _mk(5, o, "Chopper-modulated amplifier",
               "Sơ đồ khuếch đại dùng bộ ngắt cơ học: DC sang AC, khuếch đại rồi chỉnh lưu",
               "Chopper-modulated amplifier converting DC to AC, amplifying and rectifying back",
               "Hình gồm hai phần: ở trên, tín hiệu DC được bộ ngắt cắt thành AC qua máy biến áp để lấy đầu ra AC; ở dưới, đầu vào AC qua bộ khuếch đại, máy biến áp ghép và mạch chỉnh lưu lọc cho đầu ra DC.",
               "Two parts: above, a DC input is chopped into AC through a transformer to give an AC output; below, an AC input passes through an amplifier, a coupling transformer and a rectifier and filter to give a DC output.")


# ---------------------------------------------------------------- 5.6
@_reg
def fig_f06():
    """Fig. 5.6 - basic inverting operational amplifier."""
    o = [_defs()]
    o.append(_circle(58, 114, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(44, 110, "ein", 7.4, anchor="end"))
    o.append(_line(61, 114, 100, 114, sw=1.1))
    o.append(_ar(76, 106, 104, 106, sw=1.0, color=GREY))
    o.append(T(90, 101, "I", 7.0))
    o.append(_zig_h(100, 160, 114))
    o.append(T(130, 102, "Ri", 7.4))
    o.append(_circle(170, 114, 2.6, fill="#ffffff", sw=1.0))
    o.append(_line(161, 114, 170, 114, sw=1.1))
    o.append(_line(170, 114, 230, 114, sw=1.1))

    o.append(_oa(230, 90, 110, 80))
    # feedback resistor R0 from summing node to output
    o.append(_line(170, 114, 170, 70, sw=1.1))
    o.append(_zig_h(170, 280, 70))
    o.append(T(225, 58, "R0", 7.4))
    o.append(_line(280, 70, 390, 70, sw=1.1))
    o.append(_line(390, 70, 390, 130, sw=1.1))
    # non-inverting terminal grounded
    o.append(_line(230, 146, 190, 146, sw=1.1))
    o.append(_gnd(190, 160))
    # output
    o.append(_line(340, 130, 510, 130, sw=1.1))
    o.append(_circle(510, 130, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(524, 134, "e0", 7.4, anchor="start"))
    return _mk(6, o, "Basic inverting operational amplifier",
               "Bộ khuếch đại thu toán cơ bản ở cấu hình đảo với Ri và R0",
               "Basic operational amplifier connected as an inverter with Ri and R0",
               "Sơ đồ bộ khuếch đại thu toán: tín hiệu ein qua điện trở Ri tới chân vào đảo, điện trở phản hồi R0 nối từ đầu ra e0 về điểm tổng, chân không đảo nối đất và dòng I chảy qua mạch.",
               "Diagram of an operational amplifier: the input ein passes through resistor Ri to the inverting terminal, feedback resistor R0 returns the output e0 to the summing node, the non-inverting terminal is grounded and the current I is indicated.")


# ---------------------------------------------------------------- 5.7
@_reg
def fig_f07():
    """Fig. 5.7 - inverter amplifier circuit."""
    o = [_defs()]
    o.append(_circle(70, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(56, 107, "ei", 7.4, anchor="end"))
    o.append(_line(73, 111, 110, 111, sw=1.1))
    o.append(_zig_h(110, 170, 111))
    o.append(T(140, 99, "R", 7.4))
    o.append(_circle(180, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(172, 102, "eg", 7.2, anchor="end"))
    o.append(_line(171, 111, 180, 111, sw=1.1))
    o.append(_line(180, 111, 250, 111, sw=1.1))

    o.append(_oa(250, 88, 110, 76))
    o.append(_line(180, 111, 180, 66, sw=1.1))
    o.append(_zig_h(180, 290, 66))
    o.append(T(235, 54, "R", 7.4))
    o.append(_line(290, 66, 400, 66, sw=1.1))
    o.append(_line(400, 66, 400, 126, sw=1.1))
    o.append(_line(250, 141, 210, 141, sw=1.1))
    o.append(_gnd(210, 155))
    o.append(_line(360, 126, 500, 126, sw=1.1))
    o.append(_circle(510, 126, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(524, 130, "e0", 7.4, anchor="start"))
    return _mk(7, o, "Inverter amplifier circuit",
               "Mạch đảo dùng bộ khuếch đại thu toán với điện trở đầu vào và phản hồi",
               "Inverting amplifier circuit with an op-amp, input resistor and feedback resistor",
               "Sơ đồ mạch đảo: tín hiệu ei đi qua điện trở R tới điểm tổng eg ở chân vào đảo; điện trở R nối từ đầu ra e0 về điểm này, chân không đảo nối đất.",
               "Circuit of the inverter: input ei passes through a resistor R to the summing node eg at the inverting input; a feedback resistor R returns the output e0 to that node while the non-inverting input is grounded.")


# ---------------------------------------------------------------- 5.8
@_reg
def fig_f08():
    """Fig. 5.8 - adder (summing amplifier)."""
    o = [_defs()]
    for yy, lab in ((100, "e1"), (134, "e2")):
        o.append(_circle(60, yy, 2.6, fill="#ffffff", sw=1.0))
        o.append(T(46, yy - 4, lab, 7.4, anchor="end"))
        o.append(_line(63, yy, 100, yy, sw=1.1))
        o.append(_zig_h(100, 160, yy))
        o.append(T(130, yy - 12, "R", 7.4))

    o.append(_line(160, 100, 220, 100, sw=1.1))
    o.append(_line(160, 134, 220, 134, sw=1.1))
    o.append(_line(220, 100, 220, 111, sw=1.1))
    o.append(_line(220, 134, 220, 111, sw=1.1))
    o.append(_circle(220, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(208, 102, "eg", 7.2, anchor="end"))
    o.append(_line(220, 111, 280, 111, sw=1.1))

    o.append(_oa(280, 88, 110, 76))
    o.append(_line(220, 111, 220, 66, sw=1.1))
    o.append(_zig_h(220, 330, 66))
    o.append(T(275, 54, "R", 7.4))
    o.append(_line(330, 66, 430, 66, sw=1.1))
    o.append(_line(430, 66, 430, 126, sw=1.1))
    o.append(_line(280, 141, 240, 141, sw=1.1))
    o.append(_gnd(240, 155))
    o.append(_line(390, 126, 500, 126, sw=1.1))
    o.append(_circle(510, 126, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(524, 130, "e0", 7.4, anchor="start"))
    return _mk(8, o, "Adder circuit",
               "Mạch cộng tín hiệu dùng bộ khuếch đại thu toán",
               "Adder circuit built with an operational amplifier",
               "Sơ đồ mạch cộng: hai đầu vào e1 và e2 mỗi đầu qua điện trở R tới điểm tổng tại chân vào đảo; điện trở phản hồi R nối từ đầu ra e0 về điểm tổng, chân không đảo nối đất.",
               "Adder circuit: two inputs e1 and e2 each pass through a resistor R to the summing junction at the inverting input; a feedback resistor R returns the output e0 to that junction and the non-inverting input is grounded.")


# ---------------------------------------------------------------- 5.9
@_reg
def fig_f09():
    """Fig. 5.9 - subtractor (two-stage difference amplifier)."""
    o = [_defs()]
    # first stage: e2 inverted to -e2
    o.append(_circle(40, 89, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(28, 85, "e2", 7.4, anchor="end"))
    o.append(_line(43, 89, 70, 89, sw=1.1))
    o.append(_zig_h(70, 120, 89))
    o.append(T(95, 77, "R", 7.4))
    o.append(_circle(130, 89, 2.6, fill="#ffffff", sw=1.0))
    o.append(_line(121, 89, 130, 89, sw=1.1))
    o.append(_line(130, 89, 160, 89, sw=1.1))
    o.append(_oa(160, 72, 80, 56))
    o.append(_line(130, 89, 130, 58, sw=1.1))
    o.append(_zig_h(130, 200, 58))
    o.append(T(165, 46, "R", 7.4))
    o.append(_line(200, 58, 240, 58, sw=1.1))
    o.append(_line(240, 58, 240, 100, sw=1.1))
    o.append(_line(160, 111, 120, 111, sw=1.1))
    o.append(_gnd(120, 124))
    o.append(_line(240, 100, 280, 100, sw=1.1))
    o.append(_line(280, 100, 280, 89, sw=1.1))
    o.append(T(268, 84, "-e2", 7.2, anchor="end"))

    # second stage: -e2 and e1 summed to give e2 - e1
    o.append(_line(280, 89, 330, 89, sw=1.1))
    o.append(_zig_h(330, 380, 89))
    o.append(T(355, 77, "R", 7.4))
    o.append(_circle(300, 140, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(288, 136, "e1", 7.4, anchor="end"))
    o.append(_line(303, 140, 330, 140, sw=1.1))
    o.append(_zig_h(330, 380, 140))
    o.append(T(355, 128, "R", 7.4))
    o.append(_line(380, 140, 380, 89, sw=1.1))
    o.append(_circle(390, 89, 2.6, fill="#ffffff", sw=1.0))
    o.append(_line(381, 89, 390, 89, sw=1.1))
    o.append(_line(390, 89, 420, 89, sw=1.1))

    o.append(_oa(420, 72, 90, 56))
    o.append(_line(390, 89, 390, 58, sw=1.1))
    o.append(_zig_h(390, 470, 58))
    o.append(T(430, 46, "R", 7.4))
    o.append(_line(470, 58, 520, 58, sw=1.1))
    o.append(_line(520, 58, 520, 100, sw=1.1))
    o.append(_line(420, 111, 390, 111, sw=1.1))
    o.append(_gnd(390, 124))
    o.append(_line(510, 100, 600, 100, sw=1.1))
    o.append(_circle(610, 100, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(624, 104, "e0", 7.4, anchor="start"))
    return _mk(9, o, "Subtractor circuit",
               "Mạch trừ tín hiệu gồm hai tầng khuếch đại thu toán",
               "Subtractor circuit using two operational amplifier stages",
               "Sơ đồ mạch trừ: tầng thứ nhất đảo e2 thành -e2; tầng thứ hai cộng -e2 với e1 và có điện trở phản hồi cho đầu ra e0 bằng e2 trừ e1.",
               "Subtractor circuit: the first stage inverts e2 to -e2; the second stage sums -e2 with e1 through equal resistors with feedback, giving an output e0 equal to e2 minus e1.")


# ---------------------------------------------------------------- 5.10
@_reg
def fig_f10():
    """Fig. 5.10 - integrator circuit."""
    o = [_defs()]
    o.append(_circle(70, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(56, 107, "ei", 7.4, anchor="end"))
    o.append(_line(73, 111, 110, 111, sw=1.1))
    o.append(_zig_h(110, 170, 111))
    o.append(T(140, 99, "R", 7.4))
    o.append(_circle(180, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(172, 102, "eg", 7.2, anchor="end"))
    o.append(_line(171, 111, 180, 111, sw=1.1))
    o.append(_line(180, 111, 260, 111, sw=1.1))

    o.append(_oa(260, 88, 110, 76))
    # capacitor in the feedback path
    o.append(_line(180, 111, 180, 66, sw=1.1))
    o.append(_line(180, 66, 226, 66, sw=1.1))
    o.append(_cap_h(230, 66))
    o.append(T(230, 52, "C", 7.4))
    o.append(_line(234, 66, 430, 66, sw=1.1))
    o.append(_line(430, 66, 430, 126, sw=1.1))
    o.append(_line(260, 141, 220, 141, sw=1.1))
    o.append(_gnd(220, 155))
    o.append(_line(370, 126, 500, 126, sw=1.1))
    o.append(_circle(510, 126, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(524, 130, "e0", 7.4, anchor="start"))
    return _mk(10, o, "Integrator circuit",
               "Mạch tích phân dùng tụ phản hồi và điện trở đầu vào",
               "Integrator circuit with an input resistor and a feedback capacitor",
               "Sơ đồ mạch tích phân: đầu vào ei qua điện trở R tới chân vào đảo, tụ C nối giữa đầu ra e0 và điểm tổng, chân không đảo nối đất; đầu ra tỷ lệ với tích phân của đầu vào.",
               "Integrator circuit: the input ei passes through resistor R to the inverting terminal while capacitor C provides feedback from the output e0 to the summing node; the non-inverting input is grounded and the output is proportional to the integral of the input.")


# ---------------------------------------------------------------- 5.11
@_reg
def fig_f11():
    """Fig. 5.11 - differentiator circuit."""
    o = [_defs()]
    o.append(_circle(70, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(56, 107, "ei", 7.4, anchor="end"))
    o.append(_line(73, 111, 116, 111, sw=1.1))
    o.append(_cap_h(120, 111))
    o.append(T(120, 97, "C", 7.4))
    o.append(_line(124, 111, 170, 111, sw=1.1))
    o.append(_circle(180, 111, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(172, 102, "eg", 7.2, anchor="end"))
    o.append(_line(171, 111, 180, 111, sw=1.1))
    o.append(_line(180, 111, 260, 111, sw=1.1))

    o.append(_oa(260, 88, 110, 76))
    o.append(_line(180, 111, 180, 66, sw=1.1))
    o.append(_zig_h(180, 290, 66))
    o.append(T(235, 54, "R", 7.4))
    o.append(_line(290, 66, 430, 66, sw=1.1))
    o.append(_line(430, 66, 430, 126, sw=1.1))
    o.append(_line(260, 141, 220, 141, sw=1.1))
    o.append(_gnd(220, 155))
    o.append(_line(370, 126, 500, 126, sw=1.1))
    o.append(_circle(510, 126, 2.6, fill="#ffffff", sw=1.0))
    o.append(T(524, 130, "e0", 7.4, anchor="start"))
    return _mk(11, o, "Differentiator circuit",
               "Mạch vi phân dùng tụ đầu vào và điện trở phản hồi",
               "Differentiator circuit with an input capacitor and a feedback resistor",
               "Sơ đồ mạch vi phân: đầu vào ei qua tụ C tới chân vào đảo, điện trở R nối giữa đầu ra e0 và điểm tổng, chân không đảo nối đất; đầu ra tỷ lệ với đạo hàm của đầu vào.",
               "Differentiator circuit: the input ei passes through capacitor C to the inverting terminal while resistor R provides feedback from the output e0 to the summing node; the non-inverting input is grounded and the output is proportional to the derivative of the input.")
