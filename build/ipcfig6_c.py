# -*- coding: utf-8 -*-
"""Vector figure supplier for IPC Chapter 6, figures 6.19 - 6.26.

Registered through ``ipcfig6_common.make_registry()``; the aggregate module
``ipcfig6`` merges this registry with the other two suppliers.
"""
from ipcfig6_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ------------------------------------------------------------------ helpers
def _res_v(cx, y0, y1, n=5, amp=3.6):
    """Zigzag resistor drawn vertically between y0 and y1."""
    pts = [(cx, y0)]
    step = (y1 - y0) / float(n)
    for i in range(n):
        pts.append((cx + (amp if i % 2 else -amp), y0 + step * (i + 0.5)))
    pts.append((cx, y1))
    return _poly(pts, sw=1.2)


def _res_h(y, x0, x1, n=6, amp=3.2):
    """Zigzag resistor drawn horizontally between x0 and x1."""
    pts = [(x0, y)]
    step = (x1 - x0) / float(n)
    for i in range(n):
        pts.append((x0 + step * (i + 0.5), y + (amp if i % 2 else -amp)))
    pts.append((x1, y))
    return _poly(pts, sw=1.2)


def _bell(cx, cy, lab):
    """Small pneumatic bellows (coil) with its two-letter designation."""
    o = [_rect(cx - 13, cy - 8, 26, 16, fill="#fbfaf7", sw=1.0)]
    pts = [(cx - 10 + i * 5, cy + (-3 if i % 2 else 3)) for i in range(5)]
    o.append(_poly(pts, sw=1.0))
    if lab:
        o.append(T(cx + 19, cy + 3, lab, 7.6))
    return "".join(o)


def _valve(cx, cy, r=8):
    """Bow-tie control valve symbol on a process line."""
    return _poly([(cx - r, cy - r), (cx + r, cy + r),
                  (cx + r, cy - r), (cx - r, cy + r)],
                 fill="#eef3fb", close=True, sw=1.2)


def _ft(cx, cy, r=7):
    """Flow / level transmitter: circled cross."""
    return (_circle(cx, cy, r, fill="#ffffff", sw=1.1)
            + _line(cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6, sw=0.9)
            + _line(cx - r * 0.6, cy + r * 0.6, cx + r * 0.6, cy - r * 0.6, sw=0.9))


def _ground(cx, y):
    """Ground symbol hanging below a common line."""
    return (_line(cx, y, cx, y + 4, sw=1.0)
            + _line(cx - 9, y + 4, cx + 9, y + 4, sw=1.0)
            + _line(cx - 6, y + 8, cx + 6, y + 8, sw=1.0)
            + _line(cx - 3, y + 12, cx + 3, y + 12, sw=1.0))


def _drum(cx, cy, rx=38, ry=15):
    """Boiler drum with a dashed water level inside."""
    o = [_ellipse(cx, cy, rx, ry, fill="#fbfaf7", sw=1.3)]
    o.append(_line(cx - rx + 5, cy + 2, cx + rx - 5, cy + 2,
                   sw=1.0, dash="4 3"))
    for xx in (cx - 22, cx - 8, cx + 8, cx + 22):
        o.append(_line(xx, cy + 3, xx, cy + 9, sw=0.6, color=GREY))
    return "".join(o)


# ---------------------------------------------------------------------- 6.19
@_reg
def fig_f19():
    """Fig. 6.19 - electronic error detector with zener stabilised supply."""
    o = [_defs()]
    yc, yb = 110.0, 200.0
    o.append(_line(70, yb, 520, yb, sw=1.2))
    o.append(T(40, 78, "Signal input", 7.4, anchor="start"))
    o.append(T(40, 90, "4 to 20 mA DC", 7.0, anchor="start"))
    o.append(T(66, 102, "+", 10, color=RED))
    o.append(T(66, 212, "-", 10, color=RED))
    o.append(_ar(70, yc, 246, yc, sw=1.4))

    o.append(_res_v(250, 118, 194))
    o.append(T(266, 148, "Precision resistor", 7.2, anchor="start"))
    o.append(T(266, 160, "62.5 ohms \u00b10.1%", 7.0, anchor="start"))

    o.append(_line(250, yc, 250, 52))
    o.append(_line(250, 52, 410, 52))
    o.append(_line(410, 52, 410, yc))
    o.append(T(252, 46, "+", 10, color=RED, anchor="start"))
    o.append(T(408, 46, "-", 10, color=RED, anchor="end"))
    o.append(T(330, 30, "Zener stabilised power unit (1.25 volt)", 7.4))

    o.append(_res_h(yc, 258, 402))
    o.append(T(330, 92, "Set value adj.", 7.4))
    o.append(_ar(350, 128, 350, 114, sw=1.2))
    o.append(_line(350, 128, 520, 128))

    o.append(_line(520, 128, 520, 200, sw=0.9))
    o.append(_ar(520, 148, 520, 132, sw=1.2))
    o.append(_ar(520, 176, 520, 196, sw=1.2))
    o.append(T(510, 134, "+", 10, color=RED, anchor="end"))
    o.append(T(510, 196, "-", 10, color=RED, anchor="end"))
    o.append(T(532, 150, "Output error", 7.2, anchor="start"))
    o.append(T(532, 162, "voltage", 7.2, anchor="start"))
    o.append(T(532, 174, "-1 to +1 volt", 7.0, anchor="start"))
    return _mk(19, o, "Electronic error detector with zener supply",
               "Mạch phát hiện sai số điện tử có nguồn ổn áp zener 1,25 V và điện trở chính xác 62,5 ôm",
               "Electronic error detector with a 1.25 V zener supply and a 62.5 ohm precision resistor",
               "Sơ đồ mạch so sánh tín hiệu đầu vào 4 đến 20 mA với điện áp đặt trị; nguồn zener ổn định 1,25 V cấp cho chiết áp chỉnh trị số đặt, điện trở chính xác 62,5 ôm nối về đường chung và đầu ra là điện áp sai số từ -1 đến +1 V.",
               "Circuit comparing a 4 to 20 mA input signal with an adjustable set value; a 1.25 V zener supply feeds the set-value potentiometer, a 62.5 ohm precision resistor returns to the common line, and the output is an error voltage from -1 to +1 V.")


# ---------------------------------------------------------------------- 6.20
@_reg
def fig_f20():
    """Fig. 6.20 - op-amp input and feedback capacitor network."""
    o = [_defs()]
    yc, yb = 120.0, 200.0
    o.append(_line(90, yb, 510, yb, sw=1.2))
    o.append(_line(115, yb, 115, yc, sw=1.0))
    o.append(_ar(115, 150, 115, 126, sw=1.2))
    o.append(T(104, 110, "+", 10, color=RED, anchor="end"))
    o.append(T(104, 206, "-", 10, color=RED, anchor="end"))
    o.append(T(100, 122, "Ein", 8.0, anchor="end"))
    o.append(T(92, 160, "Input error", 7.0, anchor="end"))
    o.append(T(92, 172, "signal", 7.0, anchor="end"))

    o.append(_line(115, yc, 154, yc))
    o.append(_line(154, yc - 9, 154, yc + 9, sw=1.4))
    o.append(_line(164, yc - 9, 164, yc + 9, sw=1.4))
    o.append(_line(164, yc, 270, yc))
    o.append(T(159, 96, "Cin", 7.6))
    o.append(T(150, 78, "Input capacitor", 7.0))

    o.append(_poly([(270, 92), (270, 148), (340, yc)],
                   fill="#eef3fb", close=True, sw=1.4))
    o.append(T(302, 116, "Op.", 7.6))
    o.append(T(302, 128, "Amp.", 7.6))
    o.append(_line(270, 140, 250, 140))
    o.append(_line(250, 140, 250, yb))
    o.append(_ground(250, yb))

    o.append(_line(340, yc, 430, yc))
    o.append(_line(430, yc, 430, 70))
    o.append(_line(430, 70, 348, 70))
    o.append(_line(348, 61, 348, 79, sw=1.4))
    o.append(_line(338, 61, 338, 79, sw=1.4))
    o.append(_line(338, 70, 250, 70))
    o.append(_line(250, 70, 250, yc))
    o.append(T(343, 56, "Cfb", 7.6))
    o.append(T(420, 56, "Feedback capacitor", 7.0))

    o.append(_line(340, yc, 510, yc))
    o.append(_line(510, yb, 510, yc, sw=0.9))
    o.append(_ar(510, 150, 510, 128, sw=1.2))
    o.append(_ar(510, 176, 510, 196, sw=1.2))
    o.append(T(500, 112, "+", 10, color=RED, anchor="end"))
    o.append(T(500, 206, "-", 10, color=RED, anchor="end"))
    o.append(T(522, 114, "E0", 8.0, anchor="start"))
    o.append(T(526, 158, "Controller", 7.0, anchor="start"))
    o.append(T(526, 170, "output signal", 7.0, anchor="start"))
    return _mk(20, o, "Op-amp input and feedback network",
               "Mạch khuếch đại thu toán có tụ đầu vào Cin và tụ phản hồi Cfb",
               "Operational amplifier circuit with input capacitor Cin and feedback capacitor Cfb",
               "Sơ đồ khuếch đại thu toán: tín hiệu sai số Ein đi qua tụ đầu vào Cin tới ngõ vào đảo, tụ phản hồi Cfb nối ngõ ra E0 trở lại ngõ vào, ngõ còn lại nối đất; dòng phản hồi bám theo dòng tín hiệu sai số.",
               "Operational amplifier circuit: the error signal Ein passes through input capacitor Cin to the inverting input, feedback capacitor Cfb returns output E0 to that input, and the other input is grounded; the feedback current tracks the error-signal current.")


# ---------------------------------------------------------------------- 6.21
@_reg
def fig_f21():
    """Fig. 6.21 - old-model pneumatic controller with four bellows."""
    o = [_defs()]
    o.append(T(170, 12, "Air supply 1.4 kg/cm\u00b2", 7.0))
    o.append(_b(125, 20, 90, 26, "Set value\nregulation unit", size=7.0))
    o.append(_ar(170, 46, 170, 64, sw=1.2))
    for cy, lab in ((76, "SV"), (108, "RA"), (142, "PV"), (174, "FB")):
        o.append(_bell(170, cy, lab))

    o.append(_line(156, 125, 232, 125, sw=2.0))
    for xx in (166, 176, 186, 196, 206, 216, 226):
        o.append(_line(xx, 121, xx - 4, 129, sw=0.6, color=GREY))
    o.append(_ar(232, 125, 258, 125, sw=1.2))
    o.append(T(266, 128, "Proportional band adjustment", 7.0, anchor="start"))

    o.append(T(76, 205, "Process variable", 7.0, anchor="start"))
    o.append(T(76, 217, "from transmitter", 7.0, anchor="start"))
    o.append(_ar(145, 198, 145, 142, sw=1.2))
    o.append(_line(145, 142, 158, 142))

    o.append(_line(182, 108, 300, 108))
    o.append(_line(300, 108, 300, 62))
    o.append(_line(300, 62, 318, 62))
    o.append(_b(320, 50, 80, 24, "Reset restrictor unit", size=6.8))
    o.append(_line(400, 62, 450, 62))
    o.append(_line(450, 62, 450, 145))

    o.append(_line(182, 142, 448, 142))
    o.append(_poly([(400, 150), (426, 136)], sw=1.6))
    o.append(_circle(400, 150, 2, fill=INK, sw=0))
    o.append(T(414, 130, "Flapper", 7.0))
    o.append(_rect(450, 140, 30, 20, fill="#fbfaf7", sw=1.1))
    o.append(T(490, 142, "Booster relay-cum-", 7.0, anchor="start"))
    o.append(T(490, 154, "nozzle assembly", 7.0, anchor="start"))

    o.append(_ar(465, 188, 465, 162, sw=1.2))
    o.append(T(465, 202, "Air supply 1.4 kg/cm\u00b2", 7.0))
    o.append(_line(480, 160, 560, 160))
    o.append(_ar(560, 160, 560, 190, sw=1.4))
    o.append(T(560, 204, "Output to final", 7.0))
    o.append(T(560, 216, "control element", 7.0))

    o.append(_line(182, 174, 240, 174))
    o.append(_line(240, 174, 240, 193))
    o.append(_line(240, 193, 280, 193))
    o.append(_b(280, 182, 70, 22, "Derivative unit", size=6.8))
    o.append(_line(350, 193, 450, 193))
    o.append(_line(450, 193, 450, 145))
    return _mk(21, o, "Old-model pneumatic controller",
               "Mẫu cũ của bộ điều khiển khí nén với bốn ống màng SV, PV, RA và FB",
               "Old-model pneumatic controller with four SV, PV, RA and FB bellows",
               "Sơ đồ bộ điều khiển khí nén kiểu cũ: tín hiệu đặt và tín hiệu quá trình tác động lên các ống màng SV và PV, cần đòn bẩy chỉnh dải tỷ lệ, cánh baffle và bộ khuếch đại vòi phun tạo ngõ ra; đường ngược qua tiết lưu đặt lại và bộ vi phân tới các ống màng RA và FB.",
               "Old pneumatic controller: set value and process variable act on the SV and PV bellows, a lever sets the proportional band, and a flapper with booster relay and nozzle generates the output; feedback returns through a reset restrictor and a derivative unit to the RA and FB bellows.")


# ---------------------------------------------------------------------- 6.22
@_reg
def fig_f22():
    """Fig. 6.22 - miniature pneumatic controller block diagram."""
    o = [_defs()]
    o.append(T(340, 16, "Twin indicator", 7.0))
    o.append(T(340, 28, "(process variable and set value)", 7.0))
    o.append(_ar(340, 32, 340, 48, sw=1.2))
    o.append(_rect(250, 50, 90, 40, fill="#eef3fb", sw=1.2))
    o.append(T(295, 75, "PV / SV", 8.5))

    o.append(_b(40, 60, 90, 40, "Process\nvariable input", size=7.4))
    o.append(_ar(130, 80, 248, 80, sw=1.3))
    o.append(_b(380, 52, 90, 30, "Set value\nmechanism", size=7.0))
    o.append(_ar(378, 67, 342, 67, sw=1.3))

    o.append(_line(85, 100, 85, 155))
    o.append(_ar(85, 155, 168, 155, sw=1.2))
    o.append(_b(170, 140, 90, 30, "Derivative unit", size=7.0))
    o.append(_ar(260, 155, 298, 155, sw=1.2))
    o.append(_b(300, 140, 90, 40, "Control\nmodule", size=7.4))
    o.append(_ar(390, 160, 428, 160, sw=1.2))
    o.append(_b(430, 140, 90, 40, "Auto-\nbalance unit", size=7.4))
    o.append(_ar(558, 160, 522, 160, sw=1.2))
    o.append(_b(560, 140, 90, 40, "Manual\nloading station", size=7.4))

    o.append(_b(560, 60, 90, 34, "Output\nindicator", size=7.4))
    o.append(_ar(605, 138, 605, 96, sw=1.3))
    o.append(_line(345, 140, 345, 105))
    o.append(_line(345, 105, 575, 105))
    o.append(_ar(575, 105, 575, 96, sw=1.2))
    return _mk(22, o, "Miniature pneumatic controller",
               "Sơ đồ khối bộ điều khiển khí nén thu nhỏ gồm sáu thành phần chức năng",
               "Block diagram of the miniature pneumatic controller with six functional components",
               "Sơ đồ khối bộ điều khiển khí nén thu nhỏ: tín hiệu quá trình đi qua bộ vi phân tới mô-đun điều khiển, bộ cân bằng tự động và trạm nạp tay đổi chế độ không giật, bộ chỉ thị ngõ ra và bộ chỉ thị kép cho trị số đặt và trị số quá trình.",
               "Block diagram of the miniature pneumatic controller: the process variable passes through a derivative unit to the control module, an auto-balance unit and manual loading station allow bumpless transfer, and indicators show the output and the twin set-value and process-variable readings.")


# ---------------------------------------------------------------------- 6.23
@_reg
def fig_f23():
    """Fig. 6.23 - pneumatic control module with four bellows and floating disc."""
    o = [_defs()]
    o.append(T(560, 12, "Air supply 1.4 kg/cm\u00b2", 7.0, anchor="end"))
    o.append(_ar(600, 18, 470, 18, sw=1.2))
    o.append(_rect(140, 30, 80, 60, fill="#eef3fb", sw=1.2))
    o.append(T(180, 58, "Pneumatic", 7.6))
    o.append(T(180, 72, "relay", 7.6))
    o.append(_line(220, 50, 258, 50))
    o.append(_b(260, 40, 70, 22, "Restriction", size=6.8))
    o.append(_line(330, 50, 450, 50))
    o.append(_line(450, 50, 450, 82))

    o.append(_ellipse(420, 100, 95, 20, fill="#fbfaf7", sw=1.3))
    o.append(_ar(365, 72, 392, 87, sw=1.1))
    o.append(T(355, 68, "Fulcrum", 7.0))
    o.append(_ar(500, 82, 490, 92, sw=1.1))
    o.append(T(500, 78, "Floating disc", 7.0))
    o.append(_poly([(392, 118), (408, 118), (400, 128)],
                   fill="#eef3fb", close=True, sw=1.1))
    o.append(T(352, 122, "Nozzle", 7.0, anchor="end"))

    for cx, lab in ((300, "FB"), (375, "PV"), (450, "SV"), (525, "RA")):
        o.append(_line(cx, 118, cx, 142, sw=1.0, dash="3 3"))
        o.append(_bell(cx, 150, lab))

    o.append(_ar(375, 158, 375, 168, sw=1.2))
    o.append(_b(355, 170, 72, 22, "Derivative unit", size=6.8))
    o.append(_ar(375, 208, 375, 194, sw=1.2))
    o.append(T(415, 214, "From transmitter", 7.0, anchor="start"))
    o.append(T(415, 226, "(process variable)", 7.0, anchor="start"))
    o.append(_ar(450, 190, 450, 160, sw=1.2))
    o.append(T(468, 182, "Set value", 7.0, anchor="start"))
    o.append(_b(493, 180, 64, 22, "Reset unit", size=6.8))
    o.append(_ar(525, 178, 525, 160, sw=1.2))

    o.append(_line(190, 90, 190, 205))
    o.append(_line(190, 150, 288, 150))
    o.append(_line(190, 205, 525, 205))
    o.append(_ar(525, 205, 525, 202, sw=1.1))
    o.append(_ar(190, 208, 190, 216, sw=1.4))
    o.append(T(190, 230, "Output to final control element", 7.0))

    o.append(T(566, 126, "FB - Feedback bellows", 6.5, anchor="start"))
    o.append(T(566, 138, "PV - Process variable bellows", 6.5, anchor="start"))
    o.append(T(566, 150, "SV - Set value bellows", 6.5, anchor="start"))
    o.append(T(566, 162, "RA - Reset action bellows", 6.5, anchor="start"))
    return _mk(23, o, "Pneumatic control module with floating disc",
               "Mô-đun điều khiển khí nén có bốn ống màng và đĩa nổi tự cân bằng",
               "Pneumatic control module with four bellows and a floating disc",
               "Cận cảnh mô-đun điều khiển: bốn ống màng FB, PV, SV và RA tác động lên đĩa nổi tựa trên điểm tựa; vòi phun và rơ le khí nén tạo ngõ ra tới phần tử điều khiển cuối, với bộ vi phân trên đường đầu vào và bộ đặt lại trên đường ngược.",
               "Close-up of the control module: four bellows FB, PV, SV and RA bear on a floating disc about a fulcrum; a nozzle and pneumatic relay generate the output to the final control element, with a derivative unit in the input line and a reset unit in the feedback line.")


# ---------------------------------------------------------------------- 6.24
@_reg
def fig_f24():
    """Fig. 6.24 - automatic process control closed loop."""
    o = [_defs()]
    o.append(T(40, 79, "Process input", 7.5, anchor="start"))
    o.append(_ar(105, 75, 133, 75, sw=1.3))
    o.append(_b(135, 50, 95, 50, "Final\ncontrol\nelement", size=7.4))
    o.append(T(262, 44, "Manipulated variable", 6.8))
    o.append(_ar(230, 75, 300, 75, sw=1.3))
    o.append(_b(330, 52, 80, 46, "Process", size=8.5))
    o.append(T(340, 18, "Process disturbance", 6.8))
    o.append(_ar(340, 24, 340, 48, sw=1.2))
    o.append(T(440, 48, "Controlled variable", 6.8))
    o.append(_ar(410, 75, 468, 75, sw=1.3))
    o.append(T(505, 26, "Primary sensing", 6.8))
    o.append(T(505, 36, "element", 6.8))
    o.append(_ar(505, 40, 505, 50, sw=1.1))
    o.append(_b(470, 52, 70, 46, "PSE", size=8.5))
    o.append(_ar(540, 75, 558, 75, sw=1.3))
    o.append(T(560, 79, "Process output", 7.5, anchor="start"))

    o.append(_ar(505, 98, 505, 148, sw=1.3))
    o.append(_b(470, 150, 70, 40, "Transmitter", size=7.5))
    o.append(T(420, 160, "Process variable", 6.8))
    o.append(_ar(468, 170, 372, 170, sw=1.3))
    o.append(_b(280, 150, 90, 40, "Error\ndetector", size=7.4))
    o.append(T(325, 208, "Set value", 7.0))
    o.append(_ar(325, 200, 325, 192, sw=1.2))
    o.append(_poly([(250, 145), (250, 195), (175, 170)],
                   fill="#eef3fb", close=True, sw=1.4))
    o.append(T(212, 158, "Control", 6.8))
    o.append(T(212, 172, "amplifier", 6.8))
    o.append(_ar(280, 170, 252, 170, sw=1.3))
    o.append(_ar(175, 168, 175, 102, sw=1.3))
    return _mk(24, o, "Automatic process control loop",
               "Sơ đồ khối hệ thống điều khiển quá trình tự động hồi tiếp",
               "Block diagram of a closed-loop automatic process control system",
               "Sơ đồ khối vòng điều khiển tự động: tín hiệu đặt và tín hiệu đo từ cảm biến và bộ phát được so sánh tại bộ phát hiện sai số, khuếch đại để điều khiển phần tử cuối, tác động lên quá trình; đầu ra quá trình được đo ngược lại và nhiễu đi vào trực tiếp tại quá trình.",
               "Closed control loop: set value and the measured signal from the primary sensing element and transmitter are compared in the error detector, amplified to drive the final control element and the process; the process output is fed back for measurement while a disturbance enters the process directly.")


# ---------------------------------------------------------------------- 6.25
@_reg
def fig_f25():
    """Fig. 6.25 - three-element boiler drum level with feed forward."""
    o = [_defs()]
    o.append(_drum(95, 85, 40, 16))
    o.append(T(95, 118, "Boiler drum", 7.5))
    o.append(_line(95, 69, 95, 45))
    o.append(_ar(95, 45, 640, 45, sw=1.3))
    o.append(T(620, 32, "Steam out", 7.0, anchor="start"))
    o.append(_ft(440, 45, 7))
    o.append(T(440, 62, "Steam flow transmitter", 6.8))
    o.append(_line(440, 52, 440, 76))
    o.append(_b(430, 78, 85, 20, "Square-root extractor", size=6.4))
    o.append(_line(480, 98, 480, 105))
    o.append(_ar(480, 105, 522, 110, sw=1.2))
    o.append(_b(450, 112, 95, 32, "Feed flow\ncomputer", size=7.0))
    o.append(_ar(545, 128, 558, 128, sw=1.2))
    o.append(T(560, 128, "Remote set point", 6.8, anchor="start"))
    o.append(_ar(497, 144, 497, 158, sw=1.2))
    o.append(_b(470, 160, 50, 28, "SC", size=9.0))
    o.append(T(530, 176, "Secondary controller", 6.8, anchor="start"))

    o.append(_line(135, 85, 183, 95))
    o.append(_ft(190, 95, 7))
    o.append(T(190, 72, "Drum level transmitter", 6.8))
    o.append(_ar(190, 103, 190, 148, sw=1.2))
    o.append(T(205, 132, "Independent set point", 6.8))
    o.append(_ar(205, 138, 205, 148, sw=1.1))
    o.append(_b(180, 150, 50, 28, "PC", size=9.0))
    o.append(_line(230, 164, 270, 164))
    o.append(_line(270, 164, 270, 128))
    o.append(_ar(270, 128, 448, 128, sw=1.2))

    o.append(_ar(620, 205, 140, 205, sw=1.3))
    o.append(_line(140, 205, 140, 101))
    o.append(_line(140, 101, 120, 101))
    o.append(T(620, 218, "From feed-water heater", 6.8, anchor="end"))
    o.append(_ft(360, 205, 7))
    o.append(T(360, 222, "Feed-water flow transmitter", 6.5))
    o.append(_line(360, 198, 360, 195))
    o.append(_b(330, 175, 85, 20, "Square-root extractor", size=6.4))
    o.append(_line(415, 185, 470, 185))
    o.append(_valve(430, 205, 8))
    o.append(T(500, 212, "Feed water control valve", 6.5, anchor="start"))
    o.append(_ar(495, 208, 445, 206, sw=1.1))
    o.append(_line(495, 188, 495, 196))
    o.append(_line(495, 196, 430, 196))
    o.append(_ar(430, 196, 430, 199, sw=1.1))
    return _mk(25, o, "Three-element boiler drum level scheme",
               "Sơ đồ điều khiển mức nước lò hơi ba thành phần có vòng đầu vào",
               "Three-element boiler drum level control scheme with feed-forward",
               "Sơ đồ điều khiển mức lò hơi ba thành phần: mức nước, lưu lượng hơi và lưu lượng nước cấp. Tín hiệu lưu lượng hơi và nước cấp được khai căn bậc hai, bộ tính toán lưu lượng nước lập trị số đặt từ xa cho bộ điều khiển phụ, trong khi bộ điều khiển chính PC nhận mức nước và trị số đặt độc lập để điều khiển van nước cấp.",
               "Three-element drum level scheme using drum level, steam flow and feed-water flow. Both flow signals are square-rooted, the feed-water flow computer forms the remote set point for the secondary controller, and the primary controller PC compares drum level with its independent set point to actuate the feed-water valve.")


# ---------------------------------------------------------------------- 6.26
@_reg
def fig_f26():
    """Fig. 6.26 - feed-forward loop with multifunction dual controller."""
    o = [_defs()]
    o.append(_drum(95, 90, 38, 15))
    o.append(_line(95, 75, 95, 40))
    o.append(_ar(95, 40, 660, 40, sw=1.3))
    o.append(T(620, 28, "Steam out", 7.0, anchor="start"))
    o.append(_ft(480, 40, 7))
    o.append(T(480, 58, "Steam flow transmitter", 7.0))
    o.append(_line(480, 48, 480, 100))
    o.append(_line(480, 100, 385, 100))
    o.append(_ar(385, 100, 385, 108, sw=1.2))

    o.append(_line(133, 90, 183, 90))
    o.append(_ft(190, 90, 7))
    o.append(T(190, 68, "Drum level transmitter", 7.0))
    o.append(_line(190, 98, 190, 135))
    o.append(_ar(190, 135, 328, 135, sw=1.2))
    o.append(_rect(330, 110, 110, 50, fill="#eef3fb", sw=1.3))
    o.append(T(385, 139, "MPC", 11.0))
    for i, ln in enumerate(("Multifunction", "dual controller", "with independent",
                            "set point and", "manual operation", "arrangements")):
        o.append(T(452, 112 + i * 10, ln, 6.8, anchor="start"))

    o.append(_ar(620, 190, 140, 190, sw=1.3))
    o.append(T(660, 178, "Feed-water in", 7.0, anchor="end"))
    o.append(_line(140, 190, 140, 105))
    o.append(_line(140, 105, 120, 105))
    o.append(_valve(200, 190, 8))
    o.append(T(200, 208, "Feed-water", 6.8))
    o.append(T(200, 217, "control", 6.8))
    o.append(T(200, 226, "valve", 6.8))
    o.append(_ft(340, 190, 7))
    o.append(T(340, 208, "Feed-water transmitter", 7.0))
    o.append(_ar(340, 182, 340, 162, sw=1.2))
    o.append(_line(385, 160, 385, 175))
    o.append(_line(385, 175, 200, 175))
    o.append(_ar(200, 175, 200, 182, sw=1.2))
    return _mk(26, o, "Feed-forward loop with multifunction controller",
               "Vòng điều khiển ba thành phần dùng bộ điều khiển kép đa chức năng MPC",
               "Three-element feed-forward loop using a multifunction dual controller (MPC)",
               "Sơ đồ vòng điều khiển mức lò hơi dùng một bộ điều khiển kép đa chức năng MPC: tín hiệu mức nước, lưu lượng hơi và lưu lượng nước cấp đều vào bộ điều khiển, ngõ ra điều khiển van nước cấp; các phép khai căn và tính toán lưu lượng được lập trình bên trong thiết bị.",
               "Drum level loop built around one multifunction dual controller MPC: drum level, steam flow and feed-water flow signals all enter the controller, whose output drives the feed-water valve; square-root extraction and flow computation are programmed inside the instrument.")
