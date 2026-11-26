# -*- coding: utf-8 -*-
"""Chapter 7 figure supplier B: programmable recorders and LED displays
(figures 7.12-7.22, printed pages 325-332).
"""
from ipcfig7_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def unicode_sub(n):
    """Unicode subscript digit for short matrix axis labels."""
    return u"\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089"[n]


# ----------------------------------------------------------------- helpers
def _ticks(x, y, w, h, step=10, color=INK):
    """Vertical division strokes of a touch-button strip."""
    o = []
    xx = x + step
    while xx < x + w - 1:
        o.append(_line(xx, y, xx, y + h, sw=0.7, color=color))
        xx += step
    return "".join(o)


def _led_h(cx, cy, color=INK, fill="#ffffff"):
    """Horizontal diode glyph (triangle pointing right) centred on (cx, cy)."""
    return (_poly([(cx - 9, cy - 7), (cx - 9, cy + 7), (cx + 3, cy)],
                  fill=fill, sw=1.1, color=color, close=True)
            + _line(cx + 3, cy - 7, cx + 3, cy + 7, sw=1.2, color=color))


def _led_v(cx, cy, color=INK, fill="#ffffff", up=False):
    """Vertical diode glyph; default direction is downward."""
    if up:
        pts = [(cx - 7, cy + 9), (cx + 7, cy + 9), (cx, cy - 3)]
        by = cy - 3
    else:
        pts = [(cx - 7, cy - 9), (cx + 7, cy - 9), (cx, cy + 3)]
        by = cy + 3
    return (_poly(pts, fill=fill, sw=1.1, color=color, close=True)
            + _line(cx - 7, by, cx + 7, by, sw=1.2, color=color))


def _res_v(x, y1, y2, color=INK):
    n = 4
    h = (y2 - y1) / float(n)
    pts = [(x, y1)]
    for i in range(n):
        pts.append((x + (5 if i % 2 == 0 else -5), y1 + h * (i + 0.5)))
    pts.append((x, y2))
    return _poly(pts, sw=1.0, color=color)


def _res_h(x1, x2, y, color=INK):
    n = 4
    w = (x2 - x1) / float(n)
    pts = [(x1, y)]
    for i in range(n):
        pts.append((x1 + w * (i + 0.5), y + (5 if i % 2 == 0 else -5)))
    pts.append((x2, y))
    return _poly(pts, sw=1.0, color=color)


def _ground(x, y, color=INK):
    return (_line(x - 8, y, x + 8, y, sw=1.1, color=color)
            + _line(x - 5, y + 4, x + 5, y + 4, sw=1.1, color=color)
            + _line(x - 2, y + 8, x + 2, y + 8, sw=1.1, color=color))


# ----------------------------------------------------------------- 7.12
@_reg
def fig_f12():
    """Fig. 7.12 - multifunction programmable recorder communication link."""
    o = [_defs()]
    # physical communication bus, drawn as the large rectangle in the print
    o.append(_line(60, 62, 455, 62, sw=1.6, color=BLUE))
    o.append(_line(455, 62, 455, 200, sw=1.6, color=BLUE))
    o.append(_line(60, 200, 455, 200, sw=1.6, color=BLUE))
    o.append(_rect(56, 58, 8, 8, fill=INK, sw=0))
    o.append(_rect(56, 196, 8, 8, fill=INK, sw=0))
    # PC-based operator interface
    o.append(_b(270, 12, 140, 34, "PC-based\noperator interface", size=7.6))
    o.append(_line(340, 46, 340, 62, sw=1.3, color=BLUE))
    # upper recorder: display screen and touch programming strip
    o.append(_rect(130, 72, 140, 54, fill="#fbfaf7", sw=1.3))
    o.append(_rect(150, 78, 100, 34, fill="#ffffff", sw=1.1))
    o.append(_rect(130, 112, 140, 14, fill="#eef3fb", sw=1.1))
    o.append(_ticks(130, 112, 140, 14, 10))
    o.append(T(200, 68, "Recorder", 7.6))
    o.append(T(78, 97, "Display screen", 7.2))
    o.append(_ar(113, 96, 151, 96, sw=1.1))
    o.append(_line(270, 95, 455, 95, sw=1.2, color=BLUE))
    o.append(T(360, 88, "Touch push button for programming", 7.0))
    o.append(_ar(330, 91, 242, 118, color=GREY, sw=1.0))
    # lower recorder: chart and touch programming strip
    o.append(_rect(130, 140, 140, 54, fill="#fbfaf7", sw=1.3))
    o.append(_rect(150, 146, 100, 34, fill="#ffffff", sw=1.1))
    o.append(_rect(130, 180, 140, 14, fill="#eef3fb", sw=1.1))
    o.append(_ticks(130, 180, 140, 14, 10))
    o.append(T(200, 136, "Recorder", 7.6))
    o.append(T(82, 165, "Chart", 7.4))
    o.append(_ar(109, 164, 151, 164, sw=1.1))
    o.append(_line(270, 152, 455, 152, sw=1.2, color=BLUE))
    o.append(T(360, 145, "Touch push button for programming", 7.0))
    o.append(_ar(330, 148, 242, 186, color=GREY, sw=1.0))
    # local I/O stations
    for yy, num in ((70, "01"), (116, "02"), (162, "03")):
        o.append(_b(490, yy, 160, 34, "Local I/O station\n" + num, size=7.4))
        o.append(_line(455, yy + 17, 490, yy + 17, sw=1.2, color=BLUE))
    o.append(_ar(628, 213, 462, 201, color=BLUE, sw=1.3))
    o.append(T(555, 222, "Communication channel physical link", 7.0))
    return _mk(12, o, "Programmable recorder communication network",
               "Mạng máy ghi lập trình được với bảng cảm ứng và đường truyền thông",
               "Programmable recorder network with touch panel and communication link",
               "Sơ đồ mạng nhiều máy ghi lập trình được: bảng điều khiển PC, hai máy ghi có bảng cảm ứng và màn hình hoặc biểu đồ, ba trạm I/O cục bộ cùng đường truyền thông vật lý chung.",
               "Network of multifunction programmable recorders: a PC-based operator interface, two recorders with display screen or chart and touch push buttons for programming, three local I/O stations and the physical communication channel linking them.")


# ----------------------------------------------------------------- 7.13
@_reg
def fig_f13():
    """Fig. 7.13 - magnetostrictive pen-position sensing elements."""
    o = [_defs()]
    o.append(_rect(60, 118, 560, 40, fill="#fbfaf7", sw=1.3))
    for xx in range(72, 620, 12):
        o.append(_line(xx, 118, xx, 158, sw=0.6, color="#9a9a9a"))
    # piezoelectric transducer (white case with shaded base)
    o.append(_rect(120, 80, 125, 38, fill="#ffffff", sw=1.3))
    o.append(_rect(120, 106, 125, 12, fill="#bcbcbc", sw=0))
    o.append(T(182, 68, "Piezoelectric transducer", 7.8))
    o.append(_ar(232, 74, 226, 86, sw=1.1))
    # detecting coil
    o.append(_rect(455, 84, 125, 34, fill="#9a9a9a", sw=1.3))
    o.append(T(518, 70, "Detecting coil", 7.8))
    o.append(_ar(548, 76, 540, 88, sw=1.1))
    # magnetostrictive element is the long hatched strip
    o.append(T(470, 186, "Magnetostrictive element", 7.8))
    o.append(_ar(470, 178, 462, 158, sw=1.1))
    return _mk(13, o, "Magnetostrictive pen-position sensor",
               "Cảm biến vị trí bút dùng phần tử từ giảo",
               "Magnetostrictive element, piezoelectric transducer and detecting coil",
               "Sơ đồ cảm biến vị trí bút: bộ chuyển đổi áp điện phát xung siêu âm vào thanh từ giảo có vạch chia, cuộn dò ở đầu kia nhận tín hiệu để xác định vị trí.",
               "Pen-position sensing arrangement: a piezoelectric transducer launches an ultrasonic pulse along the hatched magnetostrictive element while the detecting coil at the far end receives the return signal used to determine pen position.")


# ----------------------------------------------------------------- 7.14
@_reg
def fig_f14():
    """Fig. 7.14 - solid-state input scanner."""
    o = [_defs()]
    # input, output terminals and the common left rail
    o.append(T(45, 46, "Input", 7.6))
    o.append(_circle(52, 58, 3.2, fill="#ffffff"))
    o.append(_line(55, 58, 120, 58, sw=1.2))
    o.append(_line(120, 58, 120, 200, sw=1.2))
    o.append(_circle(52, 200, 3.2, fill="#ffffff"))
    o.append(_line(55, 200, 120, 200, sw=1.2))
    o.append(T(45, 217, "Output", 7.6))
    # two photo couplers (nested squares)
    for yy in (74, 148):
        o.append(_rect(104, yy, 60, 32, fill="#fbfaf7", sw=1.2))
        o.append(_rect(113, yy + 7, 42, 18, fill="#ffffff", sw=1.1))
    # upper and lower rails of the solid-state switch
    o.append(_line(120, 90, 400, 90, sw=1.2))
    o.append(_line(120, 135, 400, 135, sw=1.2))
    o.append(_line(164, 164, 205, 164, sw=1.2))
    o.append(_line(205, 164, 205, 90, sw=1.2))
    o.append(_circle(205, 135, 2.2, fill=INK, sw=0))
    o.append(_res_v(330, 90, 135))
    # opto-isolated switch block and its control loop
    o.append(_rect(400, 78, 70, 70, fill="#fbfaf7", sw=1.2))
    o.append(_led_v(420, 112, color=GREEN))
    o.append(_led_v(452, 112, color=BLUE))
    o.append(_line(427, 107, 445, 103, sw=0.9, dash="3 3", color=GREY))
    o.append(_line(427, 117, 445, 121, sw=0.9, dash="3 3", color=GREY))
    o.append(_line(470, 95, 545, 95, sw=1.1))
    o.append(_line(545, 95, 545, 90, sw=1.1))
    o.append(_circle(600, 90, 3.2, fill="#ffffff"))
    o.append(_line(548, 90, 597, 90, sw=1.1))
    o.append(_line(470, 130, 545, 130, sw=1.1))
    o.append(_line(545, 130, 545, 135, sw=1.1))
    o.append(_circle(600, 135, 3.2, fill="#ffffff"))
    o.append(_line(548, 135, 597, 135, sw=1.1))
    o.append(T(550, 160, "Controlling signal", 7.4))
    return _mk(14, o, "Solid-state input scanner",
               "Bộ quét đầu vào bán dẫn",
               "Input scanner block with photo couplers and controlling signal",
               "Sơ đồ bộ quét đầu vào: tín hiệu vào đi qua các bộ ghép quang, mạch transistor chịu áp cao và điện trở; tín hiệu điều khiển cách ly quang chọn kênh cần quét trước khi đưa ra đầu ra.",
               "Simplified input scanner: the input passes through photo couplers and a high-voltage solid-state switch with a bias resistor; an optically isolated controlling signal selects the channel before the signal reaches the output.")


# ----------------------------------------------------------------- 7.15
@_reg
def fig_f15():
    """Fig. 7.15 - paperless recording system."""
    o = [_defs()]
    # input terminal board
    o.append(_rect(28, 42, 38, 150, fill="#fbfaf7", sw=1.2))
    o.append(T(47, 26, "Input terminal", 7.2))
    o.append(T(47, 35, "board", 7.2))
    for yy, num in ((62, "1"), (96, "2"), (130, "3"), (178, "n")):
        o.append(T(38, yy + 2.5, num, 7.0))
        o.append(_circle(59, yy, 2.8, fill="#ffffff"))
    # signal conditioners
    for yy, num in ((46, "1"), (80, "2"), (114, "3"), (162, "n")):
        o.append(_b(88, yy, 92, 32, "Signal\nconditioner " + num, size=7.0))
        o.append(_line(62, yy + 16, 88, yy + 16, sw=1.1))
    # conditioned inputs enter the recording control circuit
    for xa, yb, xc, yc in ((285, 62, 300, 136), (292, 96, 300, 148),
                           (298, 130, 300, 160), (290, 178, 300, 172)):
        o.append(_line(180, yb, xa, yb, sw=1.1))
        o.append(_line(xa, yb, xa, yc, sw=1.1))
        o.append(_line(xa, yc, xc, yc, sw=1.1))
    # recording control circuit
    o.append(_rect(300, 130, 180, 66, fill="#fbfaf7", sw=1.3))
    o.append(T(390, 164, "Recording control circuit", 8.4))
    # memory bank
    o.append(_rect(395, 80, 165, 42, fill="none", sw=1.1,
                   dash="6 4", stroke=GREY))
    o.append(T(477, 92, "Memory bank", 7.6))
    for xx, lab in ((405, "M1"), (447, "M2"), (489, "M3"), (531, "Mn")):
        o.append(_rect(xx, 98, 24, 18, fill="#eef3fb", sw=1.0))
        o.append(T(xx + 12, 111, lab, 6.8))
        o.append(_line(xx + 12, 116, xx + 12, 130, sw=0.9, color=GREY))
    # output controlling circuit, DAC and output paths
    o.append(_rect(405, 48, 150, 24, fill="#eef3fb", sw=1.2))
    o.append(T(480, 64, "Output controlling circuit", 7.6))
    for xx in (417, 459, 501, 543):
        o.append(_line(xx, 72, xx, 80, sw=0.9, dash="3 3", color=GREY))
    o.append(_line(508, 48, 508, 36, sw=1.1))
    o.append(_b(350, 10, 82, 26, "Digital output", size=7.2))
    o.append(_rect(475, 12, 66, 24, fill="#fbfaf7", sw=1.2))
    o.append(T(508, 28, "DAC", 8.0))
    o.append(_b(565, 10, 95, 26, "Analog output", size=7.2))
    o.append(_ar(475, 23, 434, 23, color=BLUE, sw=1.3))
    o.append(_ar(541, 23, 563, 23, color=BLUE, sw=1.3))
    # triggering and logic control
    o.append(_b(235, 205, 100, 26, "Triggering\ncircuit", size=7.2))
    o.append(_b(365, 205, 170, 26, "Logic and training\ncontrol circuit", size=7.2))
    o.append(_line(335, 218, 363, 218, sw=1.1))
    o.append(_circle(210, 218, 3, fill="#ffffff"))
    o.append(_line(213, 218, 233, 218, sw=1.1))
    o.append(T(145, 221, "External triggering input", 6.8))
    o.append(_ar(340, 196, 300, 205, color=GREY, sw=1.0))
    o.append(T(345, 202, "Internal triggering input", 6.6, anchor="start"))
    o.append(_ar(455, 196, 455, 205, color=GREY, sw=1.0))
    o.append(_line(130, 146, 130, 194, sw=0.9, dash="4 4", color=GREY))
    o.append(_line(130, 194, 255, 194, sw=0.9, dash="4 4", color=GREY))
    return _mk(15, o, "Paperless recorder block diagram",
               "Sơ đồ hệ thống ghi không giấy",
               "Paperless recorder with signal conditioners, trigger logic, memory bank and DAC",
               "Sơ đồ máy ghi không giấy: tín hiệu từ bảng đầu vào qua các bộ điều chỉnh tới mạch điều khiển ghi, lưu vào ngân hàng nhớ M1…Mn; mạch điều khiển đầu ra chọn DAC xuất tín hiệu tương tự hoặc xuất số, còn mạch kích hoạt trong và ngoài điều khiển logic ghi.",
               "Block diagram of the paperless recorder: input channels pass through signal conditioners to the recording control circuit and the M1…Mn memory bank; the output controlling circuit feeds the DAC for analog output or a digital output, while internal and external triggering drive the trigger and logic control circuits.")


# ----------------------------------------------------------------- 7.16
@_reg
def fig_f16():
    """Fig. 7.16 - measurement, display and control device relationship."""
    o = [_defs()]
    o.append(_b(70, 95, 150, 52, "Measurement\ndevice", size=8.2))
    o.append(_b(265, 95, 150, 52, "Display\ndevice", size=8.2))
    o.append(_b(460, 95, 150, 52, "Control\ndevice", size=8.2))
    o.append(_ar(222, 121, 263, 121, color=BLUE, sw=1.6))
    o.append(_ar(417, 121, 458, 121, color=BLUE, sw=1.6))
    return _mk(16, o, "Instrumentation device relationship",
               "Quan hệ giữa các thiết bị trong hệ thống đo",
               "Relationship among measurement, display and control devices",
               "Sơ đồ hệ thống kín: tín hiệu từ thiết bị đo truyền tới thiết bị hiển thị rồi tới thiết bị điều khiển; phạm vi thảo luận ở đây tập trung vào thiết bị hiển thị số.",
               "Block diagram of a closed instrumentation system: the measurement device feeds the display device, which in turn feeds the control device; the present discussion concentrates on the digital display device.")


# ----------------------------------------------------------------- 7.17
@_reg
def fig_f17():
    """Fig. 7.17 - LED P/N junction layers with emitted light."""
    o = [_defs()]
    o.append(_rect(180, 86, 250, 90, fill="#fbfaf7", sw=1.4))
    o.append(_line(180, 132, 430, 132, sw=1.1))
    o.append(_rect(180, 78, 34, 8, fill=INK, sw=0))
    o.append(_rect(386, 78, 44, 8, fill=INK, sw=0))
    o.append(_rect(180, 176, 250, 8, fill=INK, sw=0))
    o.append(T(305, 114, "P – type", 9.2))
    o.append(T(305, 160, "N – type", 9.2))
    o.append(T(305, 40, "Emitted light", 8.4))
    for xx in (240, 270, 300, 330, 360):
        o.append(_ar(xx, 78, xx, 50, color=GREEN, sw=1.5))
    o.append(T(480, 62, "Anode", 8.0, anchor="start"))
    o.append(_ar(472, 66, 420, 80, sw=1.0))
    # bias source E_b
    o.append(_line(430, 82, 520, 82, sw=1.2))
    o.append(_line(520, 82, 520, 118, sw=1.2))
    o.append(_line(506, 118, 534, 118, sw=1.4))
    o.append(_line(511, 127, 529, 127, sw=1.4))
    o.append(_line(520, 127, 520, 180, sw=1.2))
    o.append(_line(430, 180, 520, 180, sw=1.2))
    o.append(T(542, 126, "E_b", 8.0, anchor="start"))
    o.append(T(130, 212, "Cathode", 8.0))
    o.append(_ar(160, 206, 205, 183, sw=1.0))
    return _mk(17, o, "LED P-N junction construction",
               "Cấu trúc tiếp xúc P-N của LED",
               "LED P/N layers with emitted light, anode and cathode",
               "Sơ đồ cắt ngang LED: lớp P ở trên, lớp N ở dưới, cực dương và cực âm tiếp xúc với nguồn E_b; khi phân cực thuận, ánh sáng phát ra qua bề mặt lớp P.",
               "Cross-section of an LED: the P-type layer sits above the N-type layer, with anode and cathode contacts connected to the bias source E_b; under forward bias photons escape upward from the junction region.")


# ----------------------------------------------------------------- 7.18
@_reg
def fig_f18():
    """Fig. 7.18 - phosphor-coated LED construction (a) and symbol (b)."""
    o = [_defs()]
    # (a) internal construction
    o.append(_rect(45, 60, 290, 75, fill="#fbfaf7", sw=1.3))
    o.append(_path("M 80,135 L 80,75 L 300,75 L 300,135"))
    o.append(_rect(155, 92, 65, 43, fill="#ffffff", sw=1.2))
    o.append(_rect(220, 92, 65, 43, fill="#ffffff", sw=1.2))
    o.append(T(187, 117, "P", 8.6))
    o.append(T(252, 117, "N", 8.6))
    o.append(_rect(172, 135, 14, 7, fill=INK, sw=0))
    o.append(_rect(245, 135, 14, 7, fill=INK, sw=0))
    o.append(_line(179, 142, 179, 172, sw=1.1))
    o.append(_line(179, 172, 208, 172, sw=1.1))
    o.append(_line(208, 164, 208, 180, sw=1.4))
    o.append(_line(216, 167, 216, 177, sw=1.4))
    o.append(_line(216, 172, 252, 172, sw=1.1))
    o.append(_line(252, 172, 252, 142, sw=1.1))
    o.append(T(232, 190, "E_b", 7.6))
    o.append(T(112, 48, "Phosphor layer", 7.6))
    o.append(_ar(142, 52, 150, 63, sw=1.0))
    o.append(T(78, 160, "Diode", 7.6))
    o.append(_ar(101, 157, 108, 134, sw=1.0))
    o.append(T(190, 211, "(a)", 7.8, color=GREY))
    # (b) representative circuit symbol
    o.append(T(535, 50, "(b)", 7.8, color=GREY))
    o.append(_circle(430, 112, 3.2, fill="#ffffff"))
    o.append(_line(433, 112, 512, 112, sw=1.2))
    o.append(_poly([(512, 96), (512, 128), (544, 112)],
                   fill="#fbfaf7", sw=1.3, close=True))
    o.append(_line(544, 92, 544, 132, sw=1.5))
    o.append(_line(547, 112, 637, 112, sw=1.2))
    o.append(_circle(640, 112, 3.2, fill="#ffffff"))
    for x1, y1, x2, y2 in ((528, 92, 552, 72), (540, 90, 564, 70),
                           (552, 90, 576, 72)):
        o.append(_ar(x1, y1, x2, y2, color=GREEN, sw=1.2))
    o.append(T(535, 154, "Representation of LED", 7.6))
    return _mk(18, o, "LED construction and circuit symbol",
               "Cấu trúc và ký hiệu mạch của LED",
               "LED PN diode with phosphor layer (a) and LED symbol (b)",
               "Hai bảng: (a) cấu trúc bên trong gồm lớp phốt pho bao bọc tiếp xúc P-N và nguồn phân cực E_b; (b) ký hiệu mạch của LED với hai mũi tên chỉ ánh sáng phát ra.",
               "Two panels: (a) internal construction with a phosphor layer enclosing the P-N diode and its bias source E_b; (b) the representative circuit symbol of an LED, with two arrows denoting emitted light.")


# ----------------------------------------------------------------- 7.19
@_reg
def fig_f19():
    """Fig. 7.19 - seven-segment LED with segment letters a-g."""
    o = [_defs()]
    o.append(_rect(150, 38, 340, 172, fill="none", sw=1.2,
                   dash="6 4", stroke=GREY))
    o.append(_rect(178, 46, 284, 156, fill="#fbfaf7", sw=1.3))
    # bias supply and ground on the left
    o.append(T(60, 102, "E_b", 7.4))
    o.append(_line(45, 110, 45, 172, sw=1.1))
    o.append(_ground(45, 172))
    o.append(_line(45, 110, 62, 110, sw=1.1))
    o.append(_line(62, 110, 62, 60, sw=1.1))
    o.append(_line(62, 110, 62, 192, sw=1.1))
    # the seven LED segments arranged in the printed cross layout
    specs = (("a", 260, 62, "h"), ("f", 205, 88, "v"),
             ("b", 320, 105, "v"), ("g", 260, 122, "h"),
             ("e", 205, 148, "v"), ("c", 320, 165, "v"),
             ("d", 260, 190, "h"))
    for lab, cx, cy, orient in specs:
        o.append(_led_h(cx, cy) if orient == "h" else _led_v(cx, cy))
        lx = cx - 18 if orient == "v" else cx
        ly = cy - 9 if orient == "v" else cy + 16
        o.append(T(lx, ly, lab, 7.2, color=INK))
        o.append(_line(cx + 12 if orient == "h" else cx,
                       cy, 455, cy, sw=0.9, dash="4 3", color=GREY))
        o.append(_line(455, cy, 478, cy, sw=1.0))
        o.append(T(474, cy + 2.5, lab, 7.2, anchor="end"))
        o.append(_line(480, cy, 495, cy, sw=1.0))
        o.append(_res_h(495, 525, cy))
        o.append(_line(525, cy, 540, cy, sw=1.0))
        o.append(_circle(544, cy, 2.2, fill="#ffffff"))
        o.append(_line(546, cy, 564, cy - 6, sw=1.1))
        o.append(_line(568, cy, 620, cy, sw=1.0))
    o.append(_line(620, 55, 620, 200, sw=1.2))
    o.append(_ground(620, 205))
    return _mk(19, o, "Seven-segment LED display",
               "Màn hình LED bảy đoạn",
               "Seven-segment LED with segment letters a-g",
               "Sơ đồ màn hình LED bảy đoạn: bảy diốt tương ứng các đoạn a, b, c, d, e, f, g được nối qua điện trở và công tắc tới nguồn E_b và đất; đóng công tắc đoạn nào thì đoạn đó sáng.",
               "Seven-segment LED circuit: the seven LEDs corresponding to segments a through g are wired through resistors and switches to the E_b supply and ground; closing a switch lights the corresponding segment to form a digit.")


# ----------------------------------------------------------------- 7.20
@_reg
def fig_f20():
    """Fig. 7.20 - 5 x 7 dot-matrix X/Y wire arrangement."""
    o = [_defs()]
    xs = (180, 270, 360, 450, 540)
    ys = (45, 72, 99, 126, 153, 180, 207)
    for i, yy in enumerate(ys):
        o.append(_line(115, yy, 585, yy, sw=1.0))
        o.append(T(100, yy + 2.6, "X" + unicode_sub(i), 7.4, anchor="end"))
    for j, xx in enumerate(xs):
        o.append(_line(xx, 40, xx, 212, sw=1.0))
        o.append(T(xx, 225, "Y" + unicode_sub(j), 7.4))
    # every crossing carries an LED junction, drawn as a small node and slash
    for yy in ys:
        for xx in xs:
            o.append(_circle(xx, yy, 3.0, fill="#ffffff", sw=1.0))
            o.append(_line(xx - 5, yy + 5, xx + 5, yy - 5,
                           sw=0.9, color=GREEN))
    return _mk(20, o, "Dot-matrix X/Y wire arrangement",
               "Cấu trúc dây dẫn X-Y của ma trận chấm",
               "Dot-matrix LED with X and Y wire arrangement",
               "Sơ đồ ma trận chấm 5 cột, 7 dòng: bảy dây ngang X0…X6 cắt năm dây dọc Y0…Y4, mỗi điểm giao có một LED nối ở giữa hai dây để chọn điểm sáng.",
               "Dot-matrix wiring: seven horizontal X0…X6 lines cross five vertical Y0…Y4 lines and an LED is connected at every intersection, so selecting one X line and one Y line lights the corresponding dot.")


# ----------------------------------------------------------------- 7.21
@_reg
def fig_f21():
    """Fig. 7.21 - illuminated-dot selection matrix (digit 4)."""
    o = [_defs()]
    xs = (250, 320, 390, 460, 530)
    ys = (45, 72, 99, 126, 153, 180, 207)
    on = {(0, 3), (1, 2), (1, 3), (2, 1), (2, 3),
          (3, 0), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
          (5, 3), (6, 3)}
    for i, yy in enumerate(ys):
        for j, xx in enumerate(xs):
            lit = (i, j) in on
            o.append(_circle(xx, yy, 5.4, fill=INK if lit else "#ffffff",
                             sw=1.1, color=INK if lit else GREY))
    o.append(T(390, 226, "ON dots form the selected pattern", 7.0, color=GREY))
    return _mk(21, o, "Illuminated-dot selection matrix",
               "Chọn các chấm sáng trên ma trận LED",
               "Illuminated-dot selection on an LED dot matrix",
               "Ma trận 5 cột, 7 dòng với các chấm được tô đậm biểu thị LED ở trạng thái sáng; tổ hợp các chấm sáng tạo thành ký tự cần hiển thị.",
               "A 5-column by 7-row LED matrix in which filled dots mark the LEDs switched ON; the combined lit dots form the character to be displayed.")


# ----------------------------------------------------------------- 7.22
@_reg
def fig_f22():
    """Fig. 7.22 - ten-LED bar graph with process value and set point."""
    o = [_defs()]
    o.append(_rect(240, 30, 160, 185, fill="#fbfaf7", sw=1.3))
    levels = list(range(10, -1, -1))
    for idx, lev in enumerate(levels):
        yy = 45 + idx * 16
        lit = lev <= 6
        col = RED if lit else INK
        o.append(T(258, yy + 2.6, str(lev), 7.0, anchor="end"))
        o.append(_circle(270, yy, 2.4, fill="#ffffff"))
        o.append(_line(273, yy, 328, yy, sw=1.0, color=col))
        o.append(_poly([(328, yy), (345, yy - 7), (345, yy + 7)],
                       fill="#ffe9e5" if lit else "#ffffff",
                       sw=1.1, color=col, close=True))
        o.append(_line(328, yy - 7, 328, yy + 7, sw=1.3, color=col))
        o.append(_line(345, yy, 398, yy, sw=1.0, color=col))
    o.append(_ar(500, 109, 405, 109, color=RED, sw=1.3))
    o.append(T(538, 112, "Process value", 7.4, color=RED, anchor="start"))
    o.append(_ar(500, 77, 405, 77, color=BLUE, sw=1.3))
    o.append(T(538, 80, "Set point", 7.4, color=BLUE, anchor="start"))
    return _mk(22, o, "LED bar graph display",
               "Biểu đồ cột LED",
               "Ten-LED bar graph showing process value and set point",
               "Biểu đồ cột gồm 11 mức 0 đến 10, các LED từ 0 đến 6 được thắp sáng thể hiện giá trị quá trình; mũi tên màu xanh đánh dấu giá trị cài đặt tại mức 8.",
               "Vertical bar graph with levels 0 to 10: LEDs from 0 to 6 are lit to indicate the process value and a marker at level 8 indicates the set point.")
