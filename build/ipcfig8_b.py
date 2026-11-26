# -*- coding: utf-8 -*-
"""Figure supplier B for IPC Chapter 8: figures 8.10-8.18 (PDF pp. 361-369).

Each figure is a simplified vector redraw of the printed raster diagram:
analogue signal conditioning, display and control interfaces, the interrupt
bus and the three common network topologies.
"""
from ipcfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def _blk(x, y, w, h, label, size=7.4, fill="#eef3fb"):
    """Compact labelled block; newlines start further text lines."""
    lines = str(label).split("\n")
    o = [_rect(x, y, w, h, fill)]
    step = size * 1.15
    top = y + h / 2.0 - (len(lines) - 1) * step / 2.0 + size * 0.32
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, top + i * step, ln, size))
    return "".join(o)


def _res_h(x1, x2, y, amp=4.0, n=8):
    """Horizontal zig-zag resistor between x1 and x2 on rail y."""
    pts = [(x1, y), (x1 + 5, y)]
    span = (x2 - x1 - 10) / float(n)
    for i in range(n):
        pts.append((x1 + 5 + (i + 0.5) * span,
                    y + (-amp if i % 2 == 0 else amp)))
    pts.append((x2 - 5, y))
    pts.append((x2, y))
    return _poly(pts, sw=1.1)


def _res_v(x, y1, y2, amp=4.0, n=8):
    """Vertical zig-zag resistor between y1 (top) and y2 (bottom)."""
    pts = [(x, y1), (x, y1 + 5)]
    span = (y2 - y1 - 10) / float(n)
    for i in range(n):
        pts.append((x + (-amp if i % 2 == 0 else amp),
                    y1 + 5 + (i + 0.5) * span))
    pts.append((x, y2 - 5))
    pts.append((x, y2))
    return _poly(pts, sw=1.1)


def _cap_v(x, y0, y1):
    """Capacitor shunt between the top rail y0 and the bottom rail y1."""
    yc = (y0 + y1) / 2.0
    return "".join((_line(x, y0, x, yc - 3, sw=1.0),
                    _line(x - 7, yc - 3, x + 7, yc - 3, sw=1.3),
                    _line(x - 7, yc + 3, x + 7, yc + 3, sw=1.3),
                    _line(x, yc + 3, x, y1, sw=1.0)))


def _diode_v(x, y0, y1, up=False):
    """Vertical clamp diode between rails y0 (top) and y1 (bottom).

    ``up=True`` reverses the symbol, giving the oppositely connected diode.
    """
    yc = (y0 + y1) / 2.0
    s = 5.5
    if up:
        tri = [(x - s, yc + 5), (x + s, yc + 5), (x, yc - 2)]
        bar_y = yc - 3
        return "".join((_line(x, y0, x, bar_y, sw=1.0),
                        _poly(tri, fill="#eef3fb", close=True),
                        _line(x - s, bar_y, x + s, bar_y, sw=1.3),
                        _line(x, yc + 5, x, y1, sw=1.0)))
    tri = [(x - s, yc - 5), (x + s, yc - 5), (x, yc + 2)]
    bar_y = yc + 3
    return "".join((_line(x, y0, x, yc - 5, sw=1.0),
                    _poly(tri, fill="#eef3fb", close=True),
                    _line(x - s, bar_y, x + s, bar_y, sw=1.3),
                    _line(x, bar_y, x, y1, sw=1.0)))


def _ground(x, y):
    """A small earth symbol hanging below a block."""
    return "".join((_line(x, y - 14, x, y, sw=1.0),
                    _line(x - 7, y, x + 7, y, sw=1.2),
                    _line(x - 4.5, y + 3.5, x + 4.5, y + 3.5, sw=1.0),
                    _line(x - 2, y + 7, x + 2, y + 7, sw=0.9)))


def _and_gate(x, y, w=36, h=34):
    """Flat-left, rounded-right AND gate centred vertically at y."""
    top, bot = y - h / 2.0, y + h / 2.0
    d = "M %s %s L %s %s Q %s %s %s %s Q %s %s %s %s Z" % (
        x, top, x, bot, x + w, bot, x + w, y, x + w, top, x, top)
    return _path(d, fill="#eef3fb")


@_reg
def fig_f10():
    """Fig 8.10: thermocouple filter and opposite clamp diodes."""
    o = [_defs()]
    o.append(T(340, 22, "Thermocouple input: filter capacitor and clamp diodes", 8.8))
    # thermocouple junction feeding the terminal strip
    o.append(_circle(40, 120, 3.2, fill=INK, sw=0))
    o.append(_line(40, 120, 95, 90, sw=1.1))
    o.append(_line(40, 120, 95, 150, sw=1.1))
    o.append(T(42, 112, "Thermocouple", 6.8, anchor="end"))
    o.append(_rect(95, 78, 26, 84))
    o.append(_circle(108, 90, 2.8, fill=INK, sw=0))
    o.append(_circle(108, 150, 2.8, fill=INK, sw=0))
    o.append(T(108, 174, "Terminal strip", 6.4))
    # two rails with series resistors
    o.append(_line(121, 90, 155, 90, sw=1.1))
    o.append(_res_h(155, 215, 90))
    o.append(_line(215, 90, 570, 90, sw=1.1))
    o.append(_line(121, 150, 155, 150, sw=1.1))
    o.append(_res_h(155, 215, 150))
    o.append(_line(215, 150, 570, 150, sw=1.1))
    o.append(T(185, 82, "R1", 6.4))
    o.append(T(185, 162, "R2", 6.4))
    # filter and opposite polarity clamps
    o.append(_cap_v(280, 90, 150))
    o.append(T(292, 125, "C", 6.6, anchor="start"))
    o.append(_diode_v(380, 90, 150, up=True))
    o.append(T(392, 125, "D1", 6.6, anchor="start"))
    o.append(_diode_v(470, 90, 150, up=False))
    o.append(T(482, 125, "D2", 6.6, anchor="start"))
    o.append(_circle(570, 90, 2.8, fill="#ffffff", sw=1.1))
    o.append(_circle(570, 150, 2.8, fill="#ffffff", sw=1.1))
    for i, ln in enumerate(("Thermocouple output", "to be connected to",
                            "ADC interface of", "microprocessor")):
        o.append(T(580, 92 + i * 12, ln, 6.6, anchor="start"))
    return _mk(
        10, o, "Thermocouple signal conditioning with filter and clamp diodes",
        "Sơ đồ điều hòa tín hiệu nhiệt điện: điện trở R1, R2, tụ lọc C và hai diode kẹp ngược chiều",
        "Thermocouple interface with series resistors, a filter capacitor and opposite clamp diodes",
        "Sơ đồ cảm biến nhiệt điện qua dải cọc, điện trở R1 R2, tụ C và hai diode ngược chiều tới ADC",
        "Thermocouple connected through a terminal strip, resistors R1 and R2, a capacitor and two opposite diodes to the ADC interface")


@_reg
def fig_f11():
    """Fig 8.11: process analyzer signal tapped in parallel with a display."""
    o = [_defs()]
    o.append(T(340, 18, "Process analyzer tapped in parallel with its display instrument", 8.4))
    o.append(_blk(30, 26, 110, 28, "Process\nanalyzer", 7.0))
    o.append(_blk(250, 26, 110, 28, "Display\ninstrument", 7.0))
    o.append(_line(140, 34, 250, 34, sw=1.1))
    o.append(_line(140, 46, 250, 46, sw=1.1))
    # terminal strip tapped from the two signal leads
    o.append(_rect(170, 88, 44, 84))
    o.append(_circle(186, 100, 2.8, fill=INK, sw=0))
    o.append(_circle(202, 160, 2.8, fill=INK, sw=0))
    o.append(_line(186, 34, 186, 100, sw=1.0))
    o.append(_line(202, 46, 202, 160, sw=1.0))
    o.append(T(192, 184, "Terminal strip", 6.4))
    # rails through R1 and R2
    o.append(_line(186, 100, 240, 100, sw=1.1))
    o.append(_res_h(240, 290, 100))
    o.append(_line(290, 100, 610, 100, sw=1.1))
    o.append(_line(202, 160, 240, 160, sw=1.1))
    o.append(_res_h(240, 290, 160))
    o.append(_line(290, 160, 610, 160, sw=1.1))
    o.append(T(265, 92, "R1", 6.4))
    o.append(T(265, 169, "R2", 6.4))
    o.append(_cap_v(350, 100, 160))
    o.append(T(362, 133, "C", 6.6, anchor="start"))
    o.append(_diode_v(450, 100, 160, up=True))
    o.append(T(462, 133, "D1", 6.6, anchor="start"))
    o.append(_diode_v(530, 100, 160, up=False))
    o.append(T(542, 133, "D2", 6.6, anchor="start"))
    o.append(_circle(610, 100, 2.8, fill="#ffffff", sw=1.1))
    o.append(_circle(610, 160, 2.8, fill="#ffffff", sw=1.1))
    o.append(T(620, 136, "To ADC", 7.0, anchor="start"))
    return _mk(
        11, o, "Process analyzer signal tapped in parallel with the display",
        "Sơ đồ lấy tín hiệu bộ phân tích song song với máy hiển thị để tránh quá tải cảm biến",
        "Analyzer output tapped in parallel with the display instrument before the ADC interface",
        "Sơ đồ tín hiệu analyzer được lấy song song với máy hiển thị qua dải cọc và mạch lọc",
        "Process analyzer output tapped in parallel with its display instrument, filtered and sent to the ADC")


@_reg
def fig_f12():
    """Fig 8.12: 4-20 mA through a 62.5 ohm precision resistor."""
    o = [_defs()]
    o.append(T(340, 30, "Current-to-voltage conversion with a 62.5 ohm precision resistor", 8.8))
    o.append(_line(110, 80, 570, 80, sw=1.2))
    o.append(_line(110, 180, 570, 180, sw=1.2))
    for x, y in ((110, 80), (110, 180), (570, 80), (570, 180)):
        o.append(_circle(x, y, 3.0, fill="#ffffff", sw=1.1))
    o.append(_res_v(340, 80, 180))
    o.append(T(352, 134, "62.5 ohm", 7.0, anchor="start"))
    for i, ln in enumerate(("4 to 20 mAmp.", "current input", "signal")):
        o.append(T(180, 118 + i * 12, ln, 7.0))
    for i, ln in enumerate(("0.25 to 1.25 volt", "voltage signal")):
        o.append(T(500, 124 + i * 12, ln, 7.0))
    return _mk(
        12, o, "Current signal converted to voltage by a 62.5 ohm resistor",
        "Sơ đồ đổi tín hiệu dòng 4 đến 20 mA thành điện áp 0,25 đến 1,25 V qua điện trở 62,5 ôm",
        "A 4-20 mA current signal develops 0.25-1.25 V across a 62.5 ohm precision resistor",
        "Sơ đồ dòng 4 đến 20 mA chạy qua điện trở 62,5 ôm tạo điện áp 0,25 đến 1,25 V",
        "Current input of 4 to 20 mA flowing through a 62.5 ohm resistor produces a 0.25 to 1.25 V signal")


@_reg
def fig_f13():
    """Fig 8.13: seven-segment LED display with address decoding."""
    o = [_defs()]
    o.append(T(340, 16, "Seven-segment LED display with output latch and address decoding", 8.8))
    # address decoder and its three low address lines
    o.append(_rect(40, 105, 100, 70))
    o.append(T(90, 136, "Address", 7.0))
    o.append(T(90, 148, "decoder", 7.0))
    for i, lab in enumerate(("A2", "A1", "A0")):
        yy = 120 + i * 20
        o.append(_line(35, yy, 40, yy, sw=1.0))
        o.append(T(32, yy + 2.2, lab, 6.6, anchor="end"))
    o.append(_line(140, 115, 162, 115, sw=1.0))
    o.append(_circle(165, 115, 2.4, fill="#ffffff", sw=1.0))
    o.append(T(149, 109, "O6", 6.2))
    # AND gate combines the decoded output with IOW
    o.append(_and_gate(168, 125, w=36, h=34))
    o.append(_line(140, 135, 162, 135, sw=1.0))
    o.append(_circle(165, 135, 2.4, fill="#ffffff", sw=1.0))
    o.append(T(137, 138, "IOW", 6.4, anchor="end"))
    o.append(_line(204, 125, 250, 125, sw=1.0))
    o.append(_line(250, 125, 250, 160, sw=1.0))
    o.append(_line(250, 160, 285, 160, sw=1.0))
    o.append(T(250, 175, "I/O select line", 6.6))
    # output latch with Vcc and ground
    o.append(_rect(285, 52, 110, 140))
    o.append(_line(340, 36, 340, 52, sw=1.0))
    o.append(T(350, 44, "Vcc", 6.6, anchor="start"))
    o.append(_ground(340, 206))
    o.append(T(340, 105, "Output", 7.2))
    o.append(T(340, 117, "latch", 7.2))
    ys = [64 + i * 11 for i in range(8)]
    for yy in ys:
        o.append(_line(240, yy, 285, yy, sw=1.0))
        o.append(_circle(240, yy, 1.7, fill=INK, sw=0))
        o.append(_circle(285, yy, 1.7, fill=INK, sw=0))
    o.append(T(240, 60, "Data lines", 6.6))
    # eight current-limiting resistors and LED segments to the common rail
    for yy in ys:
        o.append(_line(395, yy, 405, yy, sw=1.0))
        o.append(_res_h(405, 430, yy, amp=3.0, n=5))
        o.append(_line(430, yy, 452, yy, sw=1.0))
        o.append(_poly([(452, yy - 4), (452, yy + 4), (460, yy)],
                       fill="#eef3fb", close=True))
        o.append(_line(460, yy - 4, 460, yy + 4, sw=1.2))
        o.append(_line(460, yy, 490, yy, sw=1.0))
    o.append(_line(490, 58, 490, 148, sw=1.2))
    o.append(T(500, 62, "Vcc", 6.6, anchor="start"))
    return _mk(
        13, o, "Seven-segment LED display interface with address decoding",
        "Sơ đồ giao tiếp LED bảy đoạn: giải mã địa chỉ, cổng AND với IOW và cổng ra chốt",
        "Address decoder and IOW gate select an output latch driving a seven-segment LED display",
        "Sơ đồ các địa chỉ A0 A1 A2 giải mã cùng IOW để chọn cổng chốt, ra LED bảy đoạn qua điện trở",
        "Address lines decoded and combined with IOW to latch data into a seven-segment LED display through current-limiting resistors")


@_reg
def fig_f14():
    """Fig 8.14: latch, DAC and electro-pneumatic valve actuation."""
    o = [_defs()]
    o.append(T(340, 16, "Control output: DAC and electro-pneumatic converter", 9.0))
    # data bus into the latch
    ys = [62 + i * 12 for i in range(8)]
    for yy in ys:
        o.append(_line(20, yy, 70, yy, sw=1.0))
        o.append(_circle(20, yy, 1.7, fill=INK, sw=0))
        o.append(_circle(70, yy, 1.7, fill=INK, sw=0))
    o.append(T(45, 56, "Data lines", 6.6))
    o.append(_rect(70, 50, 80, 110))
    o.append(T(110, 101, "Latch", 7.4))
    o.append(_line(110, 36, 110, 50, sw=1.0))
    o.append(T(120, 44, "Vcc", 6.6, anchor="start"))
    o.append(_ground(90, 174))
    # latch to DAC
    for yy in ys:
        o.append(_line(150, yy, 180, yy, sw=1.0))
        o.append(_circle(150, yy, 1.7, fill=INK, sw=0))
        o.append(_circle(180, yy, 1.7, fill=INK, sw=0))
    o.append(_rect(180, 50, 80, 110))
    o.append(T(220, 101, "DAC", 7.6))
    o.append(_line(220, 36, 220, 50, sw=1.0))
    o.append(T(230, 44, "Vcc", 6.6, anchor="start"))
    # address decoder plus IOW enables the latch
    o.append(_blk(20, 178, 90, 34, "Address\ndecoder", 6.6))
    o.append(_line(110, 195, 128, 195, sw=1.0))
    o.append(_and_gate(132, 195, w=28, h=24))
    o.append(_line(122, 203, 132, 203, sw=1.0))
    o.append(T(120, 214, "IOW", 6.2, anchor="end"))
    o.append(_line(160, 195, 170, 195, sw=1.0))
    o.append(_line(170, 195, 170, 150, sw=1.0))
    o.append(_line(170, 150, 70, 150, sw=1.0))
    # DAC to electro-pneumatic converter
    o.append(_line(260, 100, 300, 100, sw=1.2))
    o.append(_line(260, 120, 300, 120, sw=1.2))
    o.append(_rect(300, 80, 160, 70))
    o.append(T(380, 105, "Electro-pneumatic", 7.2))
    o.append(T(380, 117, "converter", 7.2))
    # pneumatic supply into the top of the converter
    o.append(_ar(520, 62, 470, 62, color=BLUE, sw=1.1))
    o.append(_line(470, 62, 400, 62, sw=1.1))
    o.append(_line(400, 62, 400, 80, sw=1.1))
    o.append(T(525, 48, "Pneumatic supply", 6.6, anchor="start"))
    o.append(T(525, 60, "1.4 kg/cm2", 6.6, anchor="start"))
    # pneumatic output down to the control valve
    o.append(_line(460, 120, 490, 120, sw=1.1))
    o.append(_line(490, 120, 490, 192, sw=1.1))
    o.append(_line(490, 192, 545, 192, sw=1.1))
    o.append(T(500, 168, "Pneumatic output", 6.6, anchor="start"))
    o.append(T(500, 180, "0.2 to 1.0 kg/cm2", 6.6, anchor="start"))
    # process flow line with the pneumatic control valve
    o.append(_line(430, 195, 640, 195, sw=1.2))
    o.append(_ar(640, 195, 660, 195, color=INK, sw=1.2))
    o.append(_poly([(535, 188), (535, 202), (545, 195)],
                   fill="#eef3fb", close=True))
    o.append(_poly([(555, 188), (555, 202), (545, 195)],
                   fill="#eef3fb", close=True))
    o.append(_line(545, 188, 545, 192, sw=1.0))
    o.append(T(545, 223, "Pneumatic control valve", 6.6))
    o.append(T(640, 205, "Process flow line", 6.4, anchor="end"))
    return _mk(
        14, o, "DAC and electro-pneumatic converter driving a control valve",
        "Sơ đồ đầu ra điều khiển: chốt, DAC, bộ chuyển đổi điện-khí nén và van điều khiển trên đường ống",
        "Latch, DAC and electro-pneumatic converter drive a pneumatic control valve",
        "Sơ đồ dữ liệu qua chốt và DAC tới bộ chuyển đổi điện-khí nén, cấp khí 1.4 kg/cm2, ra 0.2 đến 1.0 kg/cm2",
        "Data is latched and converted by a DAC, then an electro-pneumatic converter drives a pneumatic control valve on the process flow line")


@_reg
def fig_f15():
    """Fig 8.15: interrupting devices sharing the IRQ and INTA lines."""
    o = [_defs()]
    o.append(T(340, 16, "Interrupt service: devices share IRQ and INTA lines", 9.0))
    o.append(_line(135, 72, 555, 72, sw=1.3))
    o.append(T(145, 64, "IRQ", 7.2, anchor="start"))
    o.append(_line(135, 203, 555, 203, sw=1.3))
    o.append(T(145, 216, "INTA", 7.2, anchor="start"))
    # microprocessor: receives IRQ, emits INTA
    o.append(_rect(85, 100, 100, 75))
    o.append(T(135, 132, "Micro-", 7.6))
    o.append(T(135, 144, "processor", 7.6))
    o.append(_ar(135, 72, 135, 100, color=RED, sw=1.2))
    o.append(_ar(135, 175, 135, 203, color=BLUE, sw=1.2))
    # three interrupting devices drive IRQ and listen on INTA
    for i, x in enumerate((275, 415, 555)):
        o.append(_rect(x - 50, 100, 100, 75))
        o.append(T(x, 128, "Interrupting", 7.2))
        o.append(T(x, 140, "device", 7.2))
        o.append(T(x, 153, "# %d" % (i + 1), 7.2))
        o.append(_ar(x, 100, x, 72, color=RED, sw=1.2))
        o.append(_ar(x, 203, x, 175, color=BLUE, sw=1.2))
    return _mk(
        15, o, "Interrupt service with shared IRQ and INTA lines",
        "Sơ đồ phục vụ ngắt: bộ vi xử lý và ba thiết bị sinh ngắt qua đường IRQ và INTA chung",
        "Microprocessor and three interrupting devices linked by IRQ and INTA lines",
        "Sơ đồ ba thiết bị sinh ngắt nối vào đường IRQ chung và đường INTA do bộ vi xử lý phát ra",
        "Block diagram of a microprocessor with three interrupting devices sharing an IRQ request line and an INTA acknowledge line")


@_reg
def fig_f16():
    """Fig 8.16: bus network topology with four devices."""
    o = [_defs()]
    o.append(T(340, 20, "Bus network topology", 9.2))
    o.append(_line(80, 125, 600, 125, sw=1.5))
    o.append(T(605, 129, "Bus", 7.2, anchor="start"))
    for x, y, lab in ((205, 70, "Device # 1"), (445, 70, "Device # 2"),
                      (205, 150, "Device # 3"), (445, 150, "Device # 4")):
        o.append(_rect(x - 55, y, 110, 30))
        o.append(T(x, y + 19, lab, 7.2))
    o.append(_line(205, 100, 205, 125, sw=1.1))
    o.append(_line(445, 100, 445, 125, sw=1.1))
    o.append(_line(205, 125, 205, 150, sw=1.1))
    o.append(_line(445, 125, 445, 150, sw=1.1))
    return _mk(
        16, o, "Bus network topology with four devices",
        "Sơ đồ mạng dạng bus: bốn thiết bị nối chung vào một đường bus",
        "Bus topology: four devices attached to a common bus line",
        "Sơ đồ mạng bus với bốn thiết bị nối vào một đường bus chung",
        "Bus topology with four devices sharing one bus; data is seen by all devices but acknowledged only by the addressed one")


@_reg
def fig_f17():
    """Fig 8.17: ring network topology with four devices."""
    o = [_defs()]
    o.append(T(340, 20, "Ring network topology", 9.2))
    for x, y, lab in ((235, 70, "Device # 1"), (445, 70, "Device # 2"),
                      (235, 155, "Device # 3"), (445, 155, "Device # 4")):
        o.append(_rect(x - 55, y, 110, 30))
        o.append(T(x, y + 19, lab, 7.2))
    o.append(_line(290, 85, 390, 85, sw=1.2))
    o.append(_line(290, 170, 390, 170, sw=1.2))
    o.append(_path("M 180 85 C 120 85 120 170 180 170", sw=1.2))
    o.append(_path("M 500 85 C 560 85 560 170 500 170", sw=1.2))
    o.append(T(565, 178, "Ring", 7.2, anchor="start"))
    return _mk(
        17, o, "Ring network topology with four devices",
        "Sơ đồ mạng dạng vòng: bốn thiết bị nối thành một vòng kín",
        "Ring topology: four devices connected in a closed loop",
        "Sơ đồ mạng vòng với bốn thiết bị nối thành vòng kín truyền tín hiệu từng chặng",
        "Ring topology with four devices on a closed loop; each device regenerates data not meant for it until the target device is reached")


@_reg
def fig_f18():
    """Fig 8.18: star network topology with a central master device."""
    o = [_defs()]
    o.append(T(340, 20, "Star network topology", 9.2))
    o.append(_line(170, 75, 285, 116, sw=1.2))
    o.append(_line(395, 116, 510, 75, sw=1.2))
    o.append(_line(170, 180, 285, 135, sw=1.2))
    o.append(_line(395, 135, 510, 180, sw=1.2))
    o.append(_rect(285, 105, 110, 40))
    o.append(T(340, 130, "Master device", 7.4))
    for x, y, lab in ((115, 60, "Device # 1"), (565, 60, "Device # 2"),
                      (115, 165, "Device # 3"), (565, 165, "Device # 4")):
        o.append(_rect(x - 55, y, 110, 30))
        o.append(T(x, y + 19, lab, 7.2))
    o.append(T(600, 210, "Star", 7.2, anchor="start"))
    return _mk(
        18, o, "Star network topology with a master device",
        "Sơ đồ mạng dạng sao: thiết bị chủ ở trung tâm điều khiển bốn thiết bị ngoại vi",
        "Star topology: four devices connected to a central master device",
        "Sơ đồ mạng sao với thiết bị chủ trung tâm và bốn thiết bị nối riêng lẻ",
        "Star topology with a central master device controlling all communication to four separately connected devices")
