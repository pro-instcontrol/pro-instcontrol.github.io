# -*- coding: utf-8 -*-
"""Figures 5.23-5.33 for IPC Chapter 5 (signal conditioning and DAQ).

Supplier module ``_c``: voltage to frequency conversion, potentiometer
slide wire coupling, successive approximation comparison, digital meter
quantization error, the weighted resistor DAC and the five steps of R-2R
ladder reduction.  Every figure is a simplified vector redraw of the
printed diagram; all labels stay inside the 680 x 250 canvas and above
y = 232.
"""
from ipcfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _res_h(x1, x2, y, label="", n=4, amp=2.4, ly=None, size=7.0):
    """Horizontal zigzag resistor between (x1,y) and (x2,y)."""
    pts = [(x1, y)]
    for i in range(1, 2 * n):
        pts.append((x1 + (x2 - x1) * i / float(2 * n),
                    y + (amp if i % 2 else -amp)))
    pts.append((x2, y))
    o = [_poly(pts, sw=1.0)]
    if label:
        o.append(T((x1 + x2) / 2.0, y - 8.0 if ly is None else ly,
                   label, size))
    return "".join(o)


def _res_v(x, y1, y2, label="", n=4, amp=2.4, lx=None, size=7.0):
    """Vertical zigzag resistor between (x,y1) and (x,y2)."""
    pts = [(x, y1)]
    for i in range(1, 2 * n):
        pts.append((x + (amp if i % 2 else -amp),
                    y1 + (y2 - y1) * i / float(2 * n)))
    pts.append((x, y2))
    o = [_poly(pts, sw=1.0)]
    if label:
        o.append(T(x + 9 if lx is None else lx, (y1 + y2) / 2.0 + 2.4,
                   label, size, anchor="start"))
    return "".join(o)


def _gnd(x, y):
    """Ground symbol with three shrinking bars."""
    return (_line(x, y, x, y + 5, sw=1.0)
            + _line(x - 6, y + 5, x + 6, y + 5, sw=1.0)
            + _line(x - 4, y + 9, x + 4, y + 9, sw=0.9)
            + _line(x - 2, y + 13, x + 2, y + 13, sw=0.8))


def _gate_r(x, y, r=11, color=INK):
    """AND gate, flat side on the left and output at the right."""
    return _path("M%d,%d A%d,%d 0 0 1 %d,%d Z" %
                 (x, y - r, r, r, x, y + r), sw=1.0, color=color)


def _gate_l(x, y, r=11, color=INK):
    """AND gate, flat side on the right and output at the left."""
    return _path("M%d,%d A%d,%d 0 0 1 %d,%d Z" %
                 (x, y + r, r, r, x, y - r), sw=1.0, color=color)


def _opamp(x, y, w=48, h=42, color=INK):
    """Op amp triangle with upper plus input and lower minus input."""
    o = [_poly([(x, y - h / 2.0), (x, y + h / 2.0), (x + w, y)],
               fill="#ffffff", sw=1.2, color=color)]
    o.append(T(x + 8, y - h / 2.0 + 9, "+", 8.0, anchor="start"))
    o.append(T(x + 8, y + h / 2.0 - 7, "-", 8.0, anchor="start"))
    return "".join(o)


def _sw(x, y1, y2, color=INK):
    """Open knife switch from a top contact to a lower contact."""
    return (_circle(x, y1, 1.5, fill="#ffffff", sw=0.9)
            + _circle(x + 8, y2, 1.5, fill="#ffffff", sw=0.9)
            + _line(x, y1, x + 8, y2 - 2, sw=1.0, color=color))


def _rung(x, y, drop, lab, ground=True):
    o = [_res_v(x, y, y + drop, lab, lx=x + 9)]
    if ground:
        o.append(_gnd(x, y + drop))
    return "".join(o)


# ---------------------------------------------------------------- 5.23
@_reg
def fig_f23():
    """Fig. 5.23 - voltage to frequency conversion circuit."""
    o = [_defs()]
    o.append(T(340, 40, "Voltage to frequency conversion circuit", 7.8))

    # Input, integrator and level detector.
    o.append(T(42, 56, "Ei", 8.0, anchor="start"))
    o.append(_ar(56, 62, 94, 62))
    o.append(_b(96, 46, 92, 32, "Integrator"))
    o.append(T(204, 56, "Eo", 8.0, anchor="start"))
    o.append(_ar(220, 62, 254, 62))
    o.append(_b(256, 46, 108, 32, "Level detector"))

    # Feedback loop: level detector, gate, clock and pulse generator.
    o.append(_ar(310, 78, 310, 114))
    o.append(_gate_l(310, 128, r=12))
    o.append(_b(404, 113, 102, 30, "Clock\nosillator"))
    o.append(_ar(404, 128, 324, 128))
    o.append(_b(158, 113, 104, 30, "Pulse\ngenerator"))
    o.append(_ar(298, 128, 262, 128))
    o.append(T(304, 152, "Pulse generator gate", 6.6))
    o.append(_poly([(158, 128), (70, 128), (70, 186)], sw=1.1))
    o.append(_ar(120, 128, 96, 128))
    o.append(_circle(70, 128, 1.8, fill=INK, sw=0))

    # Time base and counting chain.
    o.append(_poly([(455, 143), (455, 166), (472, 166)], sw=1.1))
    o.append(_b(474, 150, 116, 32, "Time base\nselection"))
    o.append(_b(326, 150, 108, 32, "Start/stop\ngate"))
    o.append(_ar(474, 166, 436, 166))

    # Main gate and output.
    o.append(_path("M56,186 A14,14 0 0 0 84,186 Z", sw=1.1))
    o.append(_poly([(326, 166), (84, 166), (84, 186)], sw=1.1))
    o.append(_poly([(70, 200), (70, 214)], sw=1.1))
    o.append(T(46, 200, "Main gate", 6.4, anchor="end"))
    o.append(_b(148, 200, 92, 28, "Counter"))
    o.append(_b(272, 200, 92, 28, "Indicator"))
    o.append(_ar(70, 214, 146, 214))
    o.append(_ar(240, 214, 270, 214))
    return _mk(23, o, "Voltage to frequency conversion circuit",
               "Mạch chuyển đổi điện áp sang tần số gồm tích phân, đầu dò mức, bộ phát xung và bộ đếm",
               "Voltage to frequency converter with integrator, level detector, pulse generator and counter",
               "Sơ đồ khối mạch chuyển đổi điện áp sang tần số: Ei qua tích phân tới đầu dò mức, đầu dò điều khiển cổng phát xung nhận xung từ dao động, xung phản hồi về tích phân; dao động cũng cấp cho chọn cơ sở thời gian, cổng start stop, cổng chính, bộ đếm và chỉ thị.",
               "Block diagram of the voltage to frequency converter: Ei passes through an integrator to a level detector which gates clock pulses to a pulse generator whose output feeds back to the integrator; the clock also drives the time base selector, start stop gate, main gate, counter and indicator.")


# ---------------------------------------------------------------- 5.24
@_reg
def fig_f24():
    """Fig. 5.24 - potentiometer type ADC with mechanical slide wire."""
    o = [_defs()]
    o.append(T(340, 40, "Potentiometer type ADC, slide wire coupling", 7.8))

    # Upper chain from error voltage to the servo system.
    o.append(_b(70, 106, 98, 34, "Converter\nDC to AC"))
    o.append(_b(196, 106, 88, 34, "Preamplifier"))
    o.append(_b(312, 106, 104, 34, "Servo-amplifier"))
    o.append(_b(452, 106, 112, 34, "Servo balancing\nsystem"))
    o.append(_ar(168, 123, 194, 123))
    o.append(_ar(284, 123, 310, 123))
    o.append(_ar(416, 123, 450, 123))

    # Electromechanical display above the servo system.
    o.append(_b(470, 34, 164, 44,
                "24 volt DC\nElectromechanical counter\nfor digital display"))
    o.append(_line(508, 106, 508, 80, sw=1.1, dash="4,3", color=INK))

    # Error voltage and precision potentiometer below.
    o.append(_b(70, 158, 98, 30, "Error\nvoltage"))
    o.append(_ar(119, 158, 119, 142))
    o.append(_b(70, 200, 150, 30, "Precision potentiometer\ncircuit"))
    o.append(_ar(119, 200, 119, 190))

    # Input brackets.
    o.append(_poly([(70, 204), (44, 204), (44, 226), (70, 226)], sw=1.0))
    o.append(T(40, 211, "Unknown", 7.0, anchor="end"))
    o.append(T(40, 221, "voltage", 7.0, anchor="end"))
    o.append(_poly([(220, 204), (240, 204), (240, 226), (220, 226)], sw=1.0))
    o.append(T(246, 215, "Reference voltage", 7.0, anchor="start"))

    # Mechanical feedback of the slide wire.
    o.append(_poly([(508, 140), (508, 176), (220, 176), (220, 215)],
                   sw=1.0, dash="4,3", color=INK))
    o.append(T(360, 170, "Mechanical coupling with slide-wire", 6.6))
    return _mk(24, o, "Mechanical slide wire coupling",
               "Mạch potentiometer tự cân bằng với khớp nối cơ khí và bộ đếm điện cơ",
               "Self balancing potentiometer circuit with mechanical slide wire coupling",
               "Sơ đồ mạch potentiometer tự cân bằng: điện áp chưa biết và điện áp chuẩn vào mạch potentiometer chính xác, sai số được đổi DC sang AC rồi khuếch đại qua tiền khuếch đại và servo, cơ cấu cân bằng servo điều khiển bộ đếm điện cơ qua khớp nối cơ khí với dây trượt.",
               "Diagram of the self balancing potentiometer: unknown and reference voltages feed the precision potentiometer, the error voltage is converted from DC to AC and amplified through a preamplifier and servo amplifier, and the servo balancing system drives an electromechanical counter through a mechanical slide wire coupling.")


# ---------------------------------------------------------------- 5.25
@_reg
def fig_f25():
    """Fig. 5.25 - successive approximation comparison tree."""
    o = [_defs()]
    o.append(T(340, 16, "Successive approximation comparator", 7.8))

    def node(x, y, lab=""):
        return (_rect(x - 15, y - 7, 30, 14, fill="#ffffff", sw=1.0)
                + (T(x, y + 2.7, lab, 7.0) if lab else ""))

    def link(x1, y1, x2, y2, lab, lx, ly):
        return _ar(x1, y1, x2, y2, color=BLUE) + T(lx, ly, lab, 6.4)

    c1 = (72, 124)
    c2 = [(220, 80), (220, 164)]
    c3 = [(368, 56), (368, 102), (368, 146), (368, 192)]
    c4 = [(524, 38 + 24 * i) for i in range(8)]

    # Comparison headings and their downward arrows.
    o.append(T(72, 34, "First comparison", 7.0))
    o.append(_ar(72, 40, 72, 114))
    o.append(T(220, 34, "Second comparison", 7.0))
    o.append(_ar(220, 40, 220, 72))
    o.append(T(368, 34, "Third comparison", 7.0))
    o.append(_ar(368, 40, 368, 48))
    o.append(T(524, 22, "Final comparison", 7.0))
    o.append(_ar(524, 28, 524, 31))

    # Input fraction.
    o.append(link(16, 124, 55, 124, "1/2 Er", 36, 116))

    # First approximation.
    o.append(node(c1[0], c1[1], "100"))
    o.append(link(88, 124, 203, 80, "3/4 Er", 140, 112))
    o.append(link(88, 124, 203, 164, "1/4 Er", 140, 156))

    # Second approximation.
    for (x, y), lab in zip(c2, ("110", "010")):
        o.append(node(x, y, lab))
    o.append(link(236, 80, 351, 56, "7/8 Er", 272, 72))
    o.append(link(236, 80, 351, 102, "5/8 Er", 272, 94))
    o.append(link(236, 164, 351, 146, "3/8 Er", 272, 152))
    o.append(link(236, 164, 351, 192, "1/8 Er", 272, 184))

    # Third approximation.
    for (x, y), lab in zip(c3, ("111", "101", "011", "001")):
        o.append(node(x, y, lab))
    pairs = [(c3[0], c4[0], "7/8 Er", 42), (c3[0], c4[1], "3/4 Er", 66),
             (c3[1], c4[2], "5/8 Er", 90), (c3[1], c4[3], "1/2 Er", 114),
             (c3[2], c4[4], "3/8 Er", 138), (c3[2], c4[5], "1/4 Er", 162),
             (c3[3], c4[6], "1/8 Er", 186), (c3[3], c4[7], "Er", 210)]
    for (sx, sy), (tx, ty), lab, ly in pairs:
        o.append(link(sx + 16, sy, tx - 17, ty, lab, 448, ly))

    # Final codes.
    for lab, (x, y) in zip(("111", "110", "101", "100",
                            "011", "010", "001", "000"), c4):
        o.append(node(x, y, lab))
    return _mk(25, o, "Successive approximation comparator",
               "Cây so sánh xấp xỉ liên tiếp với các mã nhị phân từ 000 đến 111",
               "Successive approximation comparison tree with binary codes from 000 to 111",
               "Sơ đồ cây so sánh xấp xỉ liên tiếp: mã 100 được so sánh với một phần hai Er, sau đó mỗi nhánh cộng thêm một phần tư và một phần tám Er để chọn 110 hoặc 010, rồi 111, 101, 011, 001 và cuối cùng là một trong tám mã từ 111 đến 000.",
               "Successive approximation comparison tree: code 100 is compared with half of Er, then each branch adds a quarter and an eighth of Er to select 110 or 010, then 111, 101, 011 or 001, and finally one of eight codes from 111 down to 000.")


# ---------------------------------------------------------------- 5.26
@_reg
def fig_f26():
    """Fig. 5.26 - start and flip flop sequence of the SAR ADC."""
    o = [_defs()]
    o.append(T(340, 18, "Successive approximation ADC timing", 7.8))
    o.append(T(40, 32, "Analog voltage", 7.0, anchor="start"))
    o.append(T(40, 42, "measurement input", 7.0, anchor="start"))

    # Comparator and DAC.
    o.append(_poly([(150, 64), (190, 64), (170, 96)],
                   fill="#ffffff", sw=1.1))
    o.append(_line(40, 50, 302, 50, sw=1.1))
    o.append(_ar(170, 50, 170, 62))
    o.append(T(214, 68, "Comparator", 7.0, anchor="start"))
    o.append(T(214, 78, "circuit", 7.0, anchor="start"))
    o.append(_b(300, 44, 134, 36, "Digital to analog\nconverter circuit"))
    o.append(_b(490, 44, 110, 36, "Reference\nvoltage supply"))
    o.append(_ar(490, 62, 436, 62))

    # Four bit bus between DAC and control register.
    o.append(_b(300, 118, 134, 34, "Control register\ncircuit"))
    for x in (320, 344, 368, 392):
        o.append(_ar(x, 118, x, 82))
        o.append(_circle(x, 100, 1.8, fill=INK, sw=0))
    o.append(_line(312, 100, 498, 100, sw=1.0))
    o.append(_ar(498, 100, 508, 100))
    o.append(T(512, 96, "Output voltage in", 7.0, anchor="start"))
    o.append(T(512, 106, "digital form", 7.0, anchor="start"))

    # Comparator and delayed pulse into the AND gate.
    o.append(_gate_r(210, 132, r=11))
    o.append(_poly([(170, 96), (170, 126), (208, 126)], sw=1.1))
    o.append(_ar(208, 126, 212, 126))
    o.append(_b(96, 130, 80, 34, "Time\ndelay"))
    o.append(_ar(176, 147, 208, 137))
    o.append(_ar(221, 132, 298, 132))

    # Distribution register and its four bit path.
    o.append(_b(300, 176, 134, 34, "Distribution\nregister circuit"))
    for x in (320, 344, 368, 392):
        o.append(_ar(x, 176, x, 154))

    # Start stop flip flop, Set MSB and start line.
    o.append(_b(96, 180, 80, 34, "Start/stop\nflip-flop"))
    o.append(_ar(136, 180, 136, 166))
    o.append(_ar(176, 190, 298, 190))
    o.append(T(238, 184, "Set MSB", 7.0))
    o.append(_circle(40, 220, 2.2, fill="#ffffff", sw=1.0))
    o.append(_line(40, 220, 136, 220, sw=1.1))
    o.append(_ar(136, 220, 136, 216))
    o.append(T(40, 231, "Start", 7.0))
    o.append(_poly([(434, 140), (460, 140), (460, 224), (160, 224), (160, 216)],
                   sw=1.1))
    return _mk(26, o, "Start and flip flop sequence",
               "Hệ thống ADC xấp xỉ liên tiếp với trigger start stop và thanh ghi điều khiển",
               "Successive approximation ADC system with start stop flip flop",
               "Sơ đồ khối ADC xấp xỉ liên tiếp: đầu vào tương tự vào bộ so sánh, nguồn chuẩn vào DAC, DAC và thanh ghi điều khiển trao đổi bốn bit, đầu ra chữ số nằm trên bus, cổng AND nhận tín hiệu so sánh và trễ, trigger start stop khởi động và đặt MSB cho thanh ghi phân phối.",
               "Block diagram of the successive approximation ADC: the analog input enters the comparator, the reference supply feeds the DAC, the DAC and control register exchange four bits, the digital output is tapped from the bus, an AND gate combines the comparator and delayed signals, and the start stop flip flop sets the MSB in the distribution register.")


# ---------------------------------------------------------------- 5.27
@_reg
def fig_f27():
    """Fig. 5.27 - quantization error of a digital meter."""
    o = [_defs()]
    o.append(T(340, 46, "Quantization error", 8.0))
    o.append(_line(80, 68, 80, 166, sw=1.1))
    o.append(_ar(80, 120, 610, 120))
    o.append(_line(80, 88, 540, 88, sw=0.8, color=GREY, dash="4,3"))
    o.append(_line(80, 152, 540, 152, sw=0.8, color=GREY, dash="4,3"))

    pts = []
    for i in range(6):
        a = 100 + i * 72
        pts.append((a, 88))
        pts.append((a + 72, 152))
        if i < 5:
            pts.append((a + 72, 88))
    o.append(_poly(pts, sw=1.7, color=BLUE))

    o.append(T(72, 66, "Error", 7.0, anchor="end"))
    o.append(T(72, 92, "+C/2", 7.0, anchor="end"))
    o.append(T(72, 124, "O", 7.0, anchor="end"))
    o.append(T(72, 156, "-C/2", 7.0, anchor="end"))
    o.append(_ar(560, 90, 560, 150))
    o.append(T(572, 124, "C", 7.6, anchor="start"))
    o.append(T(340, 190, "Input signal", 7.4))
    return _mk(27, o, "Digital meter quantization error",
               "Sai số lượng tử hóa của đồng hồ số dạng đường răng cưa",
               "Quantization error of a digital meter shown as a sawtooth",
               "Đồ thị sai số lượng tử hóa: trục ngang là tín hiệu vào, trục dọc là sai số, đường răng cưa giảm từ cộng C chia hai xuống trừ C chia hai rồi nhảy lên, hai đường đứt nét giới hạn vùng sai số và mũi tên bên phải chỉ độ rộng đỉnh đến đỉnh C.",
               "Plot of quantization error: the horizontal axis is the input signal and the vertical axis is error, a sawtooth ramps from plus C over two down to minus C over two then jumps back, two dashed lines mark the error limits and a right hand arrow marks the peak to peak value C.")


# ---------------------------------------------------------------- 5.28
@_reg
def fig_f28():
    """Fig. 5.28 - weighted resistor network DAC."""
    o = [_defs()]
    o.append(T(340, 38, "Weighted resistor network DAC", 7.8))
    o.append(T(46, 64, "+Vref", 7.6, anchor="start"))

    # Reference rail with a dashed section for the omitted middle bits.
    o.append(_line(40, 72, 166, 72, sw=1.1))
    o.append(_line(166, 72, 262, 72, sw=1.0, dash="4,3", color=GREY))
    o.append(_line(262, 72, 430, 72, sw=1.1))

    branches = [(80, "Dn-1", "R"), (150, "Dn-2", "2R"),
                (270, "D2", "2^(n-3)R"), (340, "D1", "2^(n-2)R"),
                (410, "D0", "2^(n-1)R")]
    for x, swlab, rlab in branches:
        o.append(_sw(x, 72, 96))
        o.append(T(x + 16, 90, swlab, 6.8, anchor="start"))
        o.append(_res_v(x + 8, 98, 154, rlab, lx=x + 20, size=6.8))

    # Summing bus with a matching dashed section.
    o.append(_line(80, 154, 166, 154, sw=1.1))
    o.append(_line(166, 154, 262, 154, sw=1.0, dash="4,3", color=GREY))
    o.append(_line(262, 154, 490, 154, sw=1.1))

    # Op amp, feedback resistor, ground and output.
    o.append(_poly([(478, 154), (478, 162), (490, 162)], sw=1.1))
    o.append(_opamp(490, 175, w=48, h=42))
    o.append(_line(490, 188, 490, 202, sw=1.1))
    o.append(_gnd(490, 202))
    o.append(_line(538, 175, 538, 130, sw=1.1))
    o.append(_res_h(478, 538, 130, "R0", ly=122))
    o.append(_poly([(478, 130), (478, 154)], sw=1.1))
    o.append(_line(538, 175, 600, 175, sw=1.1))
    o.append(T(604, 179, "Vo", 7.6, anchor="start"))
    return _mk(28, o, "Weighted resistor network DAC",
               "Mạch DAC dùng mạng điện trở trọng số với các nhánh chuyển mạch và op amp",
               "Weighted resistor DAC network with binary weighted switch branches",
               "Sơ đồ mạch DAC điện trở trọng số: nguồn Vref cấp cho các công tắc D n-1 đến D0, mỗi công tắc nối qua điện trở R, 2R đến 2 n-1 R tới thanh tổng, op amp OA có điện trở phản hồi R0 và đầu vào không đảo nối thanh tổng, đầu vào đảo nối đất, đầu ra Vo.",
               "Circuit of a weighted resistor DAC: the Vref rail feeds switches D n-1 down to D0, each switch connects through resistors R, 2R up to 2 n-1 R to the summing bus, op amp OA has feedback resistor R0, its non inverting input takes the bus, the inverting input is grounded and the output is Vo.")


# ---------------------------------------------------------------- 5.29
@_reg
def fig_f29():
    """Fig. 5.29 - the full R-2R ladder network."""
    o = [_defs()]
    o.append(T(340, 44, "R-2R ladder: full network", 7.8))
    y = 110
    xs = [170, 300, 430, 560]
    o.append(_ar(168, y, 118, y))
    for x, lab in zip(xs, ("D", "C", "B", "A")):
        o.append(T(x, y - 14, lab, 7.6))
    for i in range(3):
        o.append(_res_h(xs[i], xs[i + 1], y, "R", ly=y - 9, size=6.8))
    for x in xs:
        o.append(_rung(x, y, 58, "2R"))
    o.append(_line(560, y, 612, y, sw=1.0))
    o.append(_rung(612, y, 58, "2R"))
    o.append(T(340, 192, "Looking in from node D", 7.0))
    return _mk(29, o, "R-2R ladder full network",
               "Mạng thang R-2R đầy đủ với các nút D C B A và điện trở tận cùng",
               "Full R-2R ladder network with nodes D C B A and termination",
               "Sơ đồ mạng thang R-2R đầy đủ: bốn điện trở ngang R nối các nút D, C, B, A, mỗi nút có điện trở dọc 2R nối đất và một nhánh 2R tận cùng ở đầu phải, mũi tên chỉ hướng nhìn từ nút D.",
               "Full R-2R ladder: four horizontal R segments join nodes D, C, B and A, each node has a vertical 2R shunt to ground plus a terminating 2R branch at the right end, and an arrow shows the direction of looking in from node D.")


# ---------------------------------------------------------------- 5.30
@_reg
def fig_f30():
    """Fig. 5.30 - first reduction of the R-2R ladder."""
    o = [_defs()]
    o.append(T(340, 44, "R-2R ladder: first reduction", 7.8))
    y = 110
    xs = [170, 300, 430, 560]
    o.append(_ar(168, y, 118, y))
    for x, lab in zip(xs, ("D", "C", "B", "A")):
        o.append(T(x, y - 14, lab, 7.6))
    for i in range(3):
        o.append(_res_h(xs[i], xs[i + 1], y, "R", ly=y - 9, size=6.8))
    for x, lab in zip(xs, ("2R", "2R", "2R", "R")):
        o.append(_rung(x, y, 58, lab))
    o.append(T(340, 192, "The two end 2R branches become R", 7.0))
    return _mk(30, o, "R-2R ladder first reduction",
               "Bước giản lược đầu tiên của thang R-2R khi hai điện trở 2R cuối gộp thành R",
               "First reduction of the R-2R ladder, end 2R branches become R",
               "Sau bước giản lược đầu tiên, các nút D, C, B vẫn có điện trở dọc 2R còn nút A chỉ còn một điện trở R nối đất, ba đoạn ngang vẫn là R.",
               "After the first reduction, nodes D, C and B keep vertical 2R shunts while node A has a single R shunt to ground, and the three horizontal segments remain R.")


# ---------------------------------------------------------------- 5.31
@_reg
def fig_f31():
    """Fig. 5.31 - second reduction of the R-2R ladder."""
    o = [_defs()]
    o.append(T(340, 44, "R-2R ladder: second reduction", 7.8))
    y = 110
    xs = [200, 340, 480]
    o.append(_ar(198, y, 148, y))
    for x, lab in zip(xs, ("D", "C", "B")):
        o.append(T(x, y - 14, lab, 7.6))
    for i in range(2):
        o.append(_res_h(xs[i], xs[i + 1], y, "R", ly=y - 9, size=6.8))
    for x, lab in zip(xs, ("2R", "2R", "R")):
        o.append(_rung(x, y, 58, lab))
    o.append(T(340, 192, "One more section removed", 7.0))
    return _mk(31, o, "R-2R ladder second reduction",
               "Bước giản lược thứ hai của thang R-2R còn ba nút D C B",
               "Second reduction of the R-2R ladder with three nodes D C B",
               "Ở bước giản lược thứ hai, mạng còn ba nút D, C, B với hai đoạn ngang R, điện trở dọc 2R tại D và C, điện trở R tại B.",
               "In the second reduction the network has three nodes D, C and B with two horizontal R segments, vertical 2R shunts at D and C and a single R shunt at B.")


# ---------------------------------------------------------------- 5.32
@_reg
def fig_f32():
    """Fig. 5.32 - third reduction of the R-2R ladder."""
    o = [_defs()]
    o.append(T(340, 44, "R-2R ladder: third reduction", 7.8))
    y = 110
    xs = [250, 400]
    o.append(_ar(248, y, 198, y))
    for x, lab in zip(xs, ("D", "C")):
        o.append(T(x, y - 14, lab, 7.6))
    o.append(_res_h(xs[0], xs[1], y, "R", ly=y - 9, size=6.8))
    for x, lab in zip(xs, ("2R", "R")):
        o.append(_rung(x, y, 58, lab))
    o.append(T(340, 192, "Only two nodes remain", 7.0))
    return _mk(32, o, "R-2R ladder third reduction",
               "Bước giản lược thứ ba của thang R-2R còn hai nút D C",
               "Third reduction of the R-2R ladder with two nodes D C",
               "Ở bước giản lược thứ ba, mạng còn hai nút D và C nối nhau bằng một điện trở ngang R, D có điện trở dọc 2R và C có điện trở dọc R nối đất.",
               "In the third reduction the network has two nodes D and C joined by one horizontal R, with a vertical 2R shunt at D and a vertical R shunt at C.")


# ---------------------------------------------------------------- 5.33
@_reg
def fig_f33():
    """Fig. 5.33 - final equivalent resistance of the R-2R ladder."""
    o = [_defs()]
    o.append(T(340, 44, "R-2R ladder: final equivalent", 7.8))
    y = 110
    x = 340
    o.append(_ar(338, y, 288, y))
    o.append(T(x, y - 14, "D", 7.6))
    o.append(_rung(x, y, 58, "R"))
    o.append(T(340, 192, "Equivalent resistance looking in from D is R", 7.0))
    return _mk(33, o, "R-2R ladder final equivalent",
               "Bước giản lược cuối cùng của thang R-2R cho điện trở tương đương R tại nút D",
               "Final reduction of the R-2R ladder, equivalent resistance R",
               "Sau các bước giản lược, nhìn từ nút D mạng thang chỉ còn một điện trở R nối đất, chứng tỏ điện trở tương đương của thang là R.",
               "After all reductions, looking in from node D the ladder leaves a single resistor R to ground, showing that the equivalent resistance of the network is R.")
