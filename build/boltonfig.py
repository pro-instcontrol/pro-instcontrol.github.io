# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 1.

Every figure is redrawn as a clean vector so it stays legible on a phone,
matching the standard used for the Practical Process Control and SIS readers.
Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).

The module re-uses the shared primitives in `vfig` and adds a small
block-diagram composer used by many of the control-system figures.
"""
import math

from vfig import (BLUE, GOLD, GREY, INK, PAPER, RED, GREEN, _arrow, _axes,
                  _box, _circle, _curve, _defs, _ellipse, _f, _fig, _hatch,
                  _label, _line, _path, _poly, _rect, _ring, _txt, svg)


# ----------------------------------------------------------------- helpers
def _svg(w, h, objs, title=""):
    return svg(w, h, _defs() + "".join(objs), title)


def _finish(o, w, h, vi, en, aria_vi="", aria_en=""):
    return _fig(_svg(w, h, o, vi), vi, en, aria_vi or vi, aria_en or en)


def bx(x, y, w, h, label, fill="#eef3fb", size=8):
    """A labelled block."""
    return _box(x, y, w, h, label, fill=fill, size=size)


def ar(x1, y1, x2, y2, dash="", color=INK, sw=1.2):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def ln(x1, y1, x2, y2, dash="", color=INK, sw=0.9):
    return _line(x1, y1, x2, y2, sw=sw, dash=dash, color=color)


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


def sumj(x, y, signs, r=11):
    """Summing junction: signs is e.g. ['+','','-'] placed around the circle."""
    o = [_circle(x, y, r, fill="#fff")]
    pos = [(x, y - r - 4), (x + r + 5, y + 3), (x, y + r + 5), (x - r - 5, y + 3)]
    for i, s in enumerate(signs[:4]):
        if s:
            o.append(_txt(pos[i][0], pos[i][1], s, 8, anchor="middle", color=INK))
    return "".join(o)


def tap(x, y):
    """Take-off point: a small filled dot."""
    return _circle(x, y, 2.6, fill=INK)


def wire(o, pts, dash="", color=INK):
    for i in range(len(pts) - 1):
        o.append(ln(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], dash=dash, color=color))


# =====================================================================
# Figure 1.1 — Systems: gear box, amplifier, formal system boundary
# =====================================================================
def fig_1_1():
    o = []
    # (a) gear box
    o.append(bx(20, 20, 70, 46, "Gear box"))
    o.append(tx(55, 14, "(a)"))
    o.append(ar(8, 43, 20, 43))
    o.append(ar(90, 43, 102, 43))
    o.append(tx(6, 50, "Rotation", 6.5))
    o.append(tx(6, 58, "of input", 6.5))
    o.append(tx(96, 50, "Rotation", 6.5))
    o.append(tx(96, 58, "of output", 6.5))
    # (b) amplifier
    o.append(bx(150, 20, 70, 46, "Amplifier"))
    o.append(tx(185, 14, "(b)"))
    o.append(ar(138, 43, 150, 43))
    o.append(ar(220, 43, 232, 43))
    o.append(tx(132, 50, "Input", 6.5))
    o.append(tx(132, 58, "signal", 6.5))
    o.append(tx(226, 50, "Output", 6.5))
    o.append(tx(226, 58, "signal", 6.5))
    # (c) formal system
    o.append(_rect(300, 18, 90, 56, "#fff", sw=1.2))
    o.append(tx(345, 47, "System"))
    o.append(tx(345, 14, "(c)"))
    o.append(ar(280, 46, 300, 46))
    o.append(ar(390, 46, 410, 46))
    o.append(tx(268, 52, "Inputs", 6.5))
    o.append(tx(404, 52, "Outputs", 6.5))
    o.append(_line(345, 74, 345, 92, color=GREY))
    o.append(_line(255, 92, 435, 92, color=GREY))
    o.append(_line(255, 92, 255, 74, color=GREY))
    o.append(_line(435, 92, 435, 74, color=GREY))
    o.append(tx(345, 100, "System boundary", 6.5, color=GREY))
    o.append(tx(345, 110, "Environment", 6.5, color=GREY))
    return _finish(o, 420, 120,
                   "Hệ thống: (a) hộp bánh răng, (b) bộ khuếch đại, (c) cách biểu diễn hình thức xác định một hệ thống.",
                   "Systems: (a) a gear box, (b) an amplifier, (c) the formal picture defining a system.")


# =====================================================================
# Figure 1.2 — Control system: required value in, variable at desired out
# =====================================================================
def fig_1_2():
    o = []
    o.append(bx(60, 30, 110, 50, "Control\nsystem", fill="#eef3fb"))
    o.append(ar(20, 55, 60, 55))
    o.append(ar(170, 55, 210, 55))
    o.append(tx(14, 50, "Input:", 7))
    o.append(tx(14, 62, "required", 7, anchor="start"))
    o.append(tx(14, 72, "value of a", 7, anchor="start"))
    o.append(tx(14, 82, "variable", 7, anchor="start"))
    o.append(tx(216, 50, "Output:", 7, anchor="start"))
    o.append(tx(216, 62, "variable", 7, anchor="start"))
    o.append(tx(216, 72, "at desired", 7, anchor="start"))
    o.append(tx(216, 82, "value", 7, anchor="start"))
    return _finish(o, 300, 110,
                   "Hệ thống điều khiển: đầu vào là giá trị yêu cầu của một biến và đầu ra là biến đó ở giá trị mong muốn.",
                   "Control system: an input of the required value of some variable and an output of the variable at the desired value.")


# =====================================================================
# Figure 1.3 — Block diagrams: (a) electric motor (b) car driving system
# =====================================================================
def fig_1_3():
    o = []
    # (a)
    o.append(tx(70, 16, "(a)"))
    o.append(bx(30, 30, 90, 46, "Electric\nmotor"))
    o.append(ar(8, 53, 30, 53))
    o.append(ar(120, 53, 142, 53))
    o.append(tx(2, 60, "Electrical", 6.5))
    o.append(tx(2, 68, "energy", 6.5))
    o.append(tx(134, 60, "Mechanical", 6.5))
    o.append(tx(134, 68, "energy", 6.5))
    # (b)
    o.append(tx(270, 16, "(b)"))
    o.append(bx(190, 30, 80, 38, "Driver"))
    o.append(bx(300, 30, 90, 38, "Car steering\nunit"))
    o.append(bx(300, 84, 90, 38, "Car on road"))
    o.append(ar(270, 49, 300, 49))
    o.append(ar(345, 68, 345, 84))
    o.append(ar(300, 103, 270, 103, dash="4 3"))
    o.append(ar(270, 68, 270, 49))
    o.append(tx(178, 26, "Required", 6.3))
    o.append(tx(178, 34, "position", 6.3))
    o.append(tx(396, 90, "Position", 6.3, anchor="start"))
    o.append(tx(396, 98, "on road", 6.3, anchor="start"))
    return _finish(o, 460, 130,
                   "Ví dụ về sơ đồ khối biểu diễn hệ thống: (a) động cơ điện, (b) hệ thống lái xe ô tô gồm nhiều khối.",
                   "Examples of block diagrams to represent systems: (a) an electric motor, (b) a car driving system involving a number of blocks.")


# =====================================================================
# Figure 1.4 — Block diagram elements: element, information paths,
#             summing junction, take-off point
# =====================================================================
def fig_1_4():
    o = []
    o.append(tx(60, 16, "(a)"))
    o.append(bx(25, 30, 70, 40, "System\nelement"))
    o.append(ar(5, 50, 25, 50))
    o.append(ar(95, 50, 115, 50))
    o.append(tx(2, 64, "input", 6.3))
    o.append(tx(112, 64, "output", 6.3))
    o.append(tx(170, 16, "(b)"))
    o.append(bx(140, 30, 60, 36, "A"))
    o.append(bx(225, 30, 60, 36, "B"))
    o.append(ar(200, 48, 225, 48))
    o.append(tx(205, 56, "signal", 6.3))
    o.append(tx(300, 16, "(c)"))
    o.append(sumj(300, 50, ["+", "", "-"]))
    o.append(ar(272, 50, 289, 50))
    o.append(ar(328, 50, 356, 50))
    o.append(ar(300, 28, 300, 39))
    o.append(tx(262, 46, "+", 7))
    o.append(tx(360, 54, "sum", 6.3, anchor="start"))
    o.append(tx(300, 78, "(d)"))
    o.append(ar(300, 95, 300, 118))
    o.append(tap(300, 95))
    return _finish(o, 420, 130,
                   "Các thành phần sơ đồ khối: (a) phần tử hệ thống, (b) đường truyền tín hiệu, (c) nút tổng, (d) điểm lấy tín hiệu.",
                   "Block diagram elements: (a) system element, (b) information paths, (c) summing junction, (d) take-off point.")


# =====================================================================
# Figure 1.5 — Central heating system with negative feedback
# =====================================================================
def fig_1_5():
    o = []
    o.append(bx(20, 25, 95, 40, "Thermostat", fill="#eef3fb"))
    o.append(bx(20, 85, 95, 40, "Furnace", fill="#eef3fb"))
    o.append(bx(165, 55, 80, 40, "Room", fill="#eef3fb"))
    o.append(sumj(150, 45, ["+", "", "-"]))
    o.append(ar(115, 45, 139, 45))
    o.append(ar(161, 45, 165, 65))
    o.append(ar(245, 75, 280, 75))
    o.append(ar(280, 75, 280, 105, dash="4 3"))
    o.append(ar(280, 105, 245, 105))
    o.append(ar(115, 105, 70, 105))
    o.append(ar(70, 105, 70, 25, dash="4 3"))
    o.append(ar(70, 25, 62, 25))
    o.append(tx(8, 19, "Required", 6.3))
    o.append(tx(8, 27, "temp.", 6.3))
    o.append(tx(150, 18, "Comparator", 6.3))
    o.append(tx(150, 130, "Actual room temperature (fed back)", 6.3, color=GREY))
    o.append(tx(290, 78, "Heat", 6.3, anchor="start"))
    return _finish(o, 360, 145,
                   "Sơ đồ khối hệ thống sưởi trung tâm dùng phản hồi âm: bộ so sánh nhiệt độ yêu cầu và thực tế để bật/tắt lò.",
                   "Block diagram for a central heating system employing negative feedback.")


# =====================================================================
# Figure 1.6 — Open-loop system (no feedback)
# =====================================================================
def fig_1_6():
    o = []
    o.append(bx(20, 35, 95, 42, "Heating\nselection", fill="#eef3fb"))
    o.append(bx(170, 35, 95, 42, "Room\nprocess", fill="#eef3fb"))
    o.append(ar(115, 56, 170, 56))
    o.append(ar(5, 56, 20, 56))
    o.append(ar(265, 56, 300, 56))
    o.append(tx(2, 44, "Input", 6.3))
    o.append(tx(2, 52, "of required", 6.3))
    o.append(tx(2, 60, "temp.", 6.3))
    o.append(tx(304, 50, "Output:", 6.3, anchor="start"))
    o.append(tx(304, 60, "room temp.", 6.3, anchor="start"))
    return _finish(o, 380, 95,
                   "Hệ thống vòng hở: đầu ra không tác động ngược lại để hiệu chỉnh đầu vào khi có nhiễu.",
                   "Open-loop system with no feedback of output to modify the input if there are any extraneous disturbances.")


# =====================================================================
# Figure 1.7 — Closed-loop system (feedback)
# =====================================================================
def fig_1_7():
    o = []
    o.append(bx(20, 30, 90, 42, "Controller", fill="#eef3fb"))
    o.append(bx(165, 30, 90, 42, "Process", fill="#eef3fb"))
    o.append(sumj(140, 51, ["+", "", "-"]))
    o.append(ar(5, 51, 20, 51))
    o.append(ar(110, 51, 130, 51))
    o.append(ar(150, 51, 165, 51))
    o.append(ar(255, 51, 290, 51, dash="4 3"))
    o.append(ar(290, 51, 290, 92))
    o.append(ar(290, 92, 140, 92))
    o.append(ar(140, 92, 140, 62))
    o.append(tx(2, 40, "Input", 6.3))
    o.append(tx(2, 48, "required", 6.3))
    o.append(tx(2, 56, "value", 6.3))
    o.append(tx(296, 46, "Output", 6.3, anchor="start"))
    o.append(tx(296, 56, "variable", 6.3, anchor="start"))
    o.append(tx(150, 108, "Feedback of output", 6.3, color=GREY))
    return _finish(o, 380, 120,
                   "Hệ thống vòng kín: tín hiệu phản hồi được so sánh với giá trị yêu cầu để hiệu chỉnh đầu ra.",
                   "Closed-loop system with feedback of output to modify the input and so adjust for any extraneous disturbances.")


# =====================================================================
# Figure 1.8 — Closed-loop with feedback modifying controller input
# =====================================================================
def fig_1_8():
    o = []
    o.append(bx(15, 25, 90, 38, "Comparison\nelement", fill="#eef3fb"))
    o.append(bx(15, 85, 90, 38, "Correction\nelement", fill="#eef3fb"))
    o.append(bx(160, 85, 90, 38, "Room", fill="#eef3fb"))
    o.append(sumj(135, 44, ["+", "", "-"]))
    o.append(ar(105, 44, 124, 44))
    o.append(ar(146, 44, 160, 85, dash="4 3"))
    o.append(ar(105, 104, 60, 104))
    o.append(ar(60, 104, 60, 85, dash="4 3"))
    o.append(ar(60, 85, 55, 85))
    o.append(ar(160, 104, 250, 104, dash="4 3"))
    o.append(ar(250, 104, 250, 25))
    o.append(ar(250, 25, 146, 25))
    o.append(ar(146, 25, 146, 34))
    o.append(tx(6, 18, "Set value", 6.3))
    o.append(tx(170, 18, "Temperature", 6.3))
    o.append(tx(170, 26, "measurement", 6.3))
    o.append(tx(256, 96, "Temperature", 6.3, anchor="start"))
    return _finish(o, 330, 120,
                   "Hệ thống vòng kín với phản hồi dùng để hiệu chỉnh đầu vào bộ điều khiển, giúp tự điều chỉnh khi có nhiễu.",
                   "Closed-loop system with feedback being used to modify the input to the controller and so enable the control system to adjust when there are extraneous disturbances.")


# =====================================================================
# Figure 1.9 — Basic elements of an open-loop control system
# =====================================================================
def fig_1_9():
    o = []
    o.append(bx(15, 40, 80, 36, "Control"))
    o.append(bx(120, 40, 80, 36, "Correction"))
    o.append(bx(225, 40, 80, 36, "Process"))
    o.append(ar(95, 58, 120, 58))
    o.append(ar(200, 58, 225, 58))
    o.append(ar(5, 58, 15, 58))
    o.append(ar(305, 58, 330, 58))
    o.append(tx(2, 46, "Input", 6.3))
    o.append(tx(330, 52, "Output", 6.3, anchor="start"))
    o.append(tx(330, 60, "variable", 6.3, anchor="start"))
    return _finish(o, 380, 90,
                   "Các thành phần cơ bản của hệ thống điều khiển vòng hở: điều khiển, hiệu chỉnh và quá trình.",
                   "Basic elements of an open-loop control system.")


# =====================================================================
# Figure 1.10 — Basic elements of a closed-loop system
# =====================================================================
def fig_1_10():
    o = []
    o.append(sumj(40, 40, ["+", "", "-"]))
    o.append(bx(70, 22, 90, 36, "Control law\nelement", fill="#eef3fb"))
    o.append(bx(70, 80, 90, 36, "Correction\nelement", fill="#eef3fb"))
    o.append(bx(215, 51, 85, 36, "Process", fill="#eef3fb"))
    o.append(ar(5, 40, 29, 40))
    o.append(ar(51, 40, 70, 40))
    o.append(ar(160, 40, 160, 80, dash="4 3"))
    o.append(ar(160, 98, 160, 69))
    o.append(ar(160, 69, 215, 69))
    o.append(ar(300, 69, 340, 69, dash="4 3"))
    o.append(ar(340, 69, 340, 110))
    o.append(ar(340, 110, 40, 110))
    o.append(ar(40, 110, 40, 51))
    o.append(tx(2, 30, "Required\nvalue", 6.3))
    o.append(tx(346, 62, "Output\nY", 6.3, anchor="start"))
    o.append(tx(150, 130, "Measurement of variable being controlled", 6.3, color=GREY))
    return _finish(o, 400, 145,
                   "Các thành phần cơ bản của hệ thống vòng kín: nút so sánh, luật điều khiển, phần tử hiệu chỉnh, quá trình và đo lường.",
                   "Basic elements of a closed-loop control system.")


# =====================================================================
# Figure 1.11 — Actuator examples: (a) motor, (b) cylinder
# =====================================================================
def fig_1_11():
    o = []
    o.append(tx(70, 16, "(a)"))
    o.append(bx(30, 30, 80, 38, "Motor"))
    o.append(ar(8, 49, 30, 49))
    o.append(ar(110, 49, 132, 49))
    o.append(tx(2, 56, "From", 6.3))
    o.append(tx(2, 64, "controller", 6.3))
    o.append(tx(134, 56, "Load", 6.3, anchor="start"))
    o.append(tx(270, 16, "(b)"))
    o.append(bx(220, 25, 100, 44, "Cylinder\nwith piston", fill="#eef3fb"))
    o.append(ar(200, 47, 220, 47))
    o.append(tx(196, 54, "Pressure\nfrom\ncontroller", 6.3, anchor="end"))
    return _finish(o, 360, 90,
                   "Ví dụ về cơ cấu chấp hành: (a) động cơ, (b) xi lanh.",
                   "Actuator examples: (a) motor, (b) cylinder.")


# =====================================================================
# Figure 1.12 — Discrete-event control with on-off valve
# =====================================================================
def fig_1_12():
    o = []
    o.append(bx(20, 30, 80, 38, "Controller", fill="#eef3fb"))
    o.append(bx(160, 30, 70, 38, "Valve", fill="#eef3fb"))
    o.append(bx(160, 90, 70, 38, "Tank", fill="#eef3fb"))
    o.append(ar(100, 49, 160, 49))
    o.append(ar(230, 49, 270, 49, dash="4 3"))
    o.append(ar(270, 49, 270, 90, dash="4 3"))
    o.append(ar(270, 90, 230, 90))
    o.append(ar(195, 90, 195, 70, dash="4 3"))
    o.append(tx(8, 24, "On-off", 6.3))
    o.append(tx(8, 32, "inputs", 6.3))
    o.append(tx(276, 44, "Full", 6.3, anchor="start"))
    o.append(tx(276, 52, "signal", 6.3, anchor="start"))
    o.append(tx(195, 110, "Empty signal", 6.3, color=GREY))
    return _finish(o, 330, 125,
                   "Điều khiển theo sự kiện rời rạc: bộ điều khiển chuyển van mở khi nhận tín hiệu rỗng và đóng khi đầy.",
                   "Discrete-event control with the controller switching the valve open when empty signal received and closed when the full signal.")


# =====================================================================
# Figure 1.13 — Potentiometer as a position sensor
# =====================================================================
def fig_1_13():
    o = []
    o.append(_rect(30, 50, 150, 14, "#ddd", sw=1))
    o.append(_circle(30, 57, 4, fill="#fff"))
    o.append(_circle(180, 57, 4, fill="#fff"))
    o.append(_line(30, 57, 105, 35, color=INK, sw=1.4))
    o.append(_circle(105, 35, 5, fill=GOLD))
    o.append(ar(180, 57, 215, 57))
    o.append(tx(220, 54, "Vout", 7, anchor="start"))
    o.append(tx(105, 26, "Slider", 6.3))
    o.append(tx(2, 64, "1", 7))
    o.append(tx(184, 64, "2", 7))
    o.append(tx(95, 80, "Track", 6.3, color=GREY))
    return _finish(o, 300, 95,
                   "Potentiometer dùng làm cảm biến vị trí: điện áp ra tỉ lệ với vị trí con trượt.",
                   "Potentiometer as a sensor of position.")


# =====================================================================
# Figure 1.14 — (a) Strain gauge, (b) use on a cantilever
# =====================================================================
def fig_1_14():
    o = []
    o.append(tx(70, 16, "(a)"))
    o.append(_rect(30, 30, 80, 14, "#cdd", sw=1))
    o.append(tx(70, 22, "Wire / foil", 6))
    o.append(tx(70, 60, "Strain gauge", 6.3))
    o.append(tx(250, 16, "(b)"))
    o.append(_poly([(210, 95), (290, 95), (290, 35), (210, 35)], fill="#eee", sw=1.2))
    o.append(_line(250, 35, 250, 95, color=RED, sw=1.4))
    o.append(tx(255, 60, "Gauge", 6))
    o.append(tx(250, 110, "Cantilever", 6.3, color=GREY))
    return _finish(o, 330, 125,
                   "(a) Cảm biến biến dạng (strain gauge), (b) dùng trên một thanh công xôn để đo chuyển vị.",
                   "(a) Strain gauge, (b) example of use on a cantilever to provide a displacement sensor.")


# =====================================================================
# Figure 1.15 — LVDT
# =====================================================================
def fig_1_15():
    o = []
    o.append(_rect(30, 35, 50, 44, "#eee", sw=1.1))
    o.append(_rect(95, 35, 50, 44, "#eee", sw=1.1))
    o.append(_rect(160, 35, 50, 44, "#eee", sw=1.1))
    o.append(_line(55, 57, 95, 57, color=GREY, sw=1.4))
    o.append(_line(120, 57, 160, 57, color=GREY, sw=1.4))
    o.append(_line(185, 57, 225, 57, color=INK, sw=1.6))
    o.append(tx(55, 28, "Prim.", 6))
    o.append(tx(120, 28, "Sec.", 6))
    o.append(tx(185, 28, "Sec.", 6))
    o.append(tx(40, 92, "a.c. in", 6.3))
    o.append(ar(40, 98, 40, 79))
    o.append(tx(230, 54, "p.d. out", 6.3, anchor="start"))
    return _finish(o, 290, 110,
                   "LVDT (máy biến áp vi phân từ tính tuyến tính): điện áp ra tỉ lệ với vị trí của lõi từ.",
                   "LVDT: giving an output p.d. related to the position of the plunger.")


# =====================================================================
# Figure 1.16 — Incremental encoder
# =====================================================================
def fig_1_16():
    o = []
    o.append(_circle(80, 60, 42, fill="#f3f3f3", sw=1.2))
    for i in range(12):
        a = i * 30 * math.pi / 180
        o.append(_line(80 + 30 * math.cos(a), 60 + 30 * math.sin(a),
                       80 + 40 * math.cos(a), 60 + 40 * math.sin(a), color=INK, sw=1.4))
    o.append(_line(80, 60, 130, 60, color=GREY, sw=1.2, dash="3 3"))
    o.append(tx(80, 110, "Disc rotates with shaft", 6.3, color=GREY))
    o.append(ar(50, 60, 20, 60))
    o.append(tx(2, 56, "Light", 6.3))
    o.append(tx(135, 56, "Detector", 6.3, anchor="start"))
    return _finish(o, 230, 125,
                   "Bộ mã hóa gia tăng: đĩa quay tạo xung, số xung tỉ lệ với góc quay.",
                   "Incremental encoder: angular displacement results in pulses being detected, the number of pulses being proportional to the angular displacement.")


# =====================================================================
# Figure 1.17 — Absolute encoder wheel (binary word)
# =====================================================================
def fig_1_17():
    o = []
    o.append(_circle(80, 60, 46, fill="#f3f3f3", sw=1.2))
    o.append(_circle(80, 60, 26, fill="#fff", sw=1))
    # concentric tracks with slots
    for r in (30, 36, 42):
        n = 16
        for i in range(n):
            a = i * 2 * math.pi / n
            o.append(_line(80 + (r - 3) * math.cos(a), 60 + (r - 3) * math.sin(a),
                           80 + (r + 3) * math.cos(a), 60 + (r + 3) * math.sin(a),
                           color=INK, sw=1.2))
    o.append(tx(80, 116, "Each arc has a unique set of apertures", 6, color=GREY))
    return _finish(o, 180, 130,
                   "Bánh xe của bộ mã hóa tuyệt đối: từng cung cho một từ nhị phân riêng biệt chỉ vị trí góc.",
                   "The rotating wheel of the absolute encoder: the binary word output indicates the angular position.")


# =====================================================================
# Figure 1.18 — Limit switches: (a) lever, (b) roller, (c) cam
# =====================================================================
def fig_1_18():
    o = []
    o.append(tx(40, 16, "(a)"))
    o.append(_rect(20, 35, 30, 22, "#eef3fb", sw=1.1))
    o.append(_line(50, 46, 78, 30, color=INK, sw=1.6))
    o.append(tx(120, 16, "(b)"))
    o.append(_rect(100, 35, 30, 22, "#eef3fb", sw=1.1))
    o.append(_circle(146, 38, 7, fill="#fff", sw=1.2))
    o.append(ar(146, 38, 175, 38))
    o.append(tx(210, 16, "(c)"))
    o.append(_rect(190, 35, 30, 22, "#eef3fb", sw=1.1))
    o.append(_ellipse(240, 40, 14, 7, fill="#fff", sw=1.2))
    return _finish(o, 290, 70,
                   "Công tắc giới hạn: (a) cần gạt, (b) con lăn, (c) cam.",
                   "Limit switches: (a) Lever, (b) roller, (c) cam.")


# =====================================================================
# Figure 1.19 — Tachogenerator
# =====================================================================
def fig_1_19():
    o = []
    o.append(_rect(40, 30, 60, 44, "#eef3fb", sw=1.1))
    o.append(_circle(70, 52, 16, fill="#fff", sw=1.2))
    o.append(tx(70, 56, "coil", 6))
    o.append(ar(100, 52, 130, 52))
    o.append(tx(135, 49, "e.m.f. out", 6.3, anchor="start"))
    o.append(tx(70, 90, "Rotates in magnetic field", 6.3, color=GREY))
    o.append(ar(70, 84, 70, 74))
    return _finish(o, 230, 100,
                   "Máy phát tốc (tachogenerator): điện áp xoay chiều cảm ứng tỉ lệ với tốc độ góc.",
                   "The tachogenerator.")


# =====================================================================
# Figure 1.20 — Diaphragm sensors (a) plain (b) corrugated
# =====================================================================
def fig_1_20():
    o = []
    o.append(tx(80, 16, "(a)"))
    o.append(_line(30, 40, 130, 40, color=INK, sw=2))
    o.append(ar(30, 40, 15, 60))
    o.append(ar(130, 40, 145, 60))
    o.append(tx(20, 66, "Pressure", 6.3))
    o.append(tx(20, 74, "difference", 6.3))
    o.append(tx(240, 16, "(b)"))
    o.append(_path("M210 40 q10 -12 20 0 q10 12 20 0 q10 -12 20 0 q10 12 20 0",
                   fill="none", sw=2, color=INK))
    return _finish(o, 360, 85,
                   "Cảm biến màng: (a) mặt phẳng, (b) có gân để tăng biên độ chuyển động.",
                   "Diaphragm sensors (a) plain, (b) corrugated for greater movement.")


# =====================================================================
# Figure 1.21 — Pressure gauge with strain gauges on diaphragm
# =====================================================================
def fig_1_21():
    o = []
    o.append(_ellipse(80, 50, 50, 18, fill="#eef3fb", sw=1.3))
    o.append(_line(40, 50, 120, 50, color=INK, sw=1.4))
    o.append(_line(80, 32, 80, 50, color=RED, sw=1.6))
    o.append(_line(80, 68, 80, 50, color=RED, sw=1.6))
    o.append(tx(80, 90, "Strain gauges on diaphragm", 6.3, color=GREY))
    o.append(tx(20, 46, "Pressure", 6.3))
    return _finish(o, 200, 105,
                   "Áp kế dùng strain gauge gắn trên màng để cảm nhận chuyển động.",
                   "Pressure gauge with strain gauges to sense movement of the diaphragm.")


# =====================================================================
# Figure 1.22 — Piezo-electric sensor
# =====================================================================
def fig_1_22():
    o = []
    o.append(_ellipse(80, 45, 48, 16, fill="#eef3fb", sw=1.3))
    o.append(_rect(72, 22, 16, 16, "#f7e9c8", sw=1.1))
    o.append(tx(80, 16, "Crystal", 6))
    o.append(tx(80, 80, "Diaphragm presses crystal", 6.3, color=GREY))
    return _finish(o, 180, 95,
                   "Cảm biến áp điện: màng ép tinh thể sinh điện tích trên bề mặt.",
                   "Basic form of a piezo-electric sensor.")


# =====================================================================
# Figure 1.23 — Venturi tube
# =====================================================================
def fig_1_23():
    o = []
    o.append(_path("M20 30 L60 30 L95 70 L135 70 L170 30 L210 30", fill="none", sw=2, color=INK))
    o.append(_path("M20 80 L60 80 L95 40 L135 40 L170 80 L210 80", fill="none", sw=2, color=INK))
    o.append(ar(20, 55, 8, 55))
    o.append(tx(2, 52, "Flow", 6.3))
    o.append(tx(95, 100, "Pressure diff. measured at constriction", 6, color=GREY))
    return _finish(o, 230, 115,
                   "Ống Venturi: hiệu áp suất tại chỗ thắt tỉ lệ với lưu lượng.",
                   "Venturi tube: pressure difference is a measure of the flow rate.")


# =====================================================================
# Figure 1.24 — Orifice plate
# =====================================================================
def fig_1_24():
    o = []
    o.append(_path("M20 30 L200 30", fill="none", sw=2, color=INK))
    o.append(_path("M20 80 L90 80 L90 35 L110 35 L110 80 L200 80", fill="none", sw=2, color=INK))
    o.append(_circle(100, 55, 4, fill=INK))
    o.append(tx(100, 100, "Orifice plate in pipe", 6.3, color=GREY))
    return _finish(o, 220, 115,
                   "Đĩa lỗ (orifice plate): đo hiệu áp suất qua lỗ để tính lưu lượng.",
                   "Orifice plate.")


# =====================================================================
# Figure 1.25 — Turbine flowmeter
# =====================================================================
def fig_1_25():
    o = []
    o.append(_path("M20 30 L200 30", fill="none", sw=2, color=INK))
    o.append(_path("M20 80 L200 80", fill="none", sw=2, color=INK))
    for i in range(6):
        o.append(_line(70 + i * 16, 30, 78 + i * 16, 80, color=BLUE, sw=1.6))
    o.append(_circle(150, 55, 5, fill=INK))
    o.append(ar(150, 55, 175, 55))
    o.append(tx(180, 52, "Pulse", 6.3, anchor="start"))
    return _finish(o, 230, 95,
                   "Lưu lượng kế tuabin: số xung mỗi giây tỉ lệ với lưu lượng.",
                   "Basic principle of the turbine flowmeter: number of pulses picked-up per second is a measure of flow rate.")


# =====================================================================
# Figure 1.26 — Potentiometer float gauge
# =====================================================================
def fig_1_26():
    o = []
    o.append(_rect(30, 40, 80, 44, "#eef3fb", sw=1.1))
    o.append(_line(40, 84, 40, 60, color=INK, sw=2))
    o.append(_line(40, 60, 100, 60, color=INK, sw=1.4))
    o.append(_circle(100, 60, 5, fill=GOLD))
    o.append(tx(100, 90, "Float", 6.3))
    o.append(ar(110, 60, 140, 60))
    o.append(tx(145, 57, "Vout", 6.3, anchor="start"))
    return _finish(o, 210, 100,
                   "Cảm biến mức chất lỏng bằng phao và potentiometer: điện áp ra giảm khi phao dâng.",
                   "Potentiometer float gauge: as the float rises the output p.d. decreases.")


# =====================================================================
# Figure 1.27 — Bimetallic strip bends with temperature
# =====================================================================
def fig_1_27():
    o = []
    o.append(_path("M30 70 Q80 70 130 40", fill="none", sw=6, color="#b0894a"))
    o.append(_path("M30 78 Q80 78 130 48", fill="none", sw=6, color="#7a8a99"))
    o.append(tx(60, 100, "Bends upward when heated", 6.3, color=GREY))
    return _finish(o, 180, 115,
                   "Dải kép kim loại (bimetallic): khi nhiệt độ tăng, dải cong về phía vật liệu hệ số nở lớn hơn.",
                   "Bimetallic strip; as the temperature increases it bends upwards with the higher coefficient material extending more.")


# =====================================================================
# Figure 1.28 — Thermistor resistance vs temperature
# =====================================================================
def fig_1_28():
    o = []
    o.append(_axes(40, 30, 130, 70, "Temperature / °C", "R", xt=[(0, "0"), (1, "100")], yt=[(0, "0"), (1, "R")]))
    o.append(_curve(lambda t: math.exp(-3 * t), 40, 30, 130, 70, xr=(0, 1), yr=(0, 1), sw=1.6, color=RED))
    return _finish(o, 200, 120,
                   "Điện trở của thermistor giảm phi tuyến khi nhiệt độ tăng.",
                   "Variation of resistance with temperature for thermistors.")


# =====================================================================
# Figure 1.29 — Thermistors: (a) rod, (b) disc, (c) bead
# =====================================================================
def fig_1_29():
    o = []
    o.append(tx(45, 16, "(a)"))
    o.append(_rect(30, 30, 16, 44, "#caa", sw=1.1))
    o.append(tx(130, 16, "(b)"))
    o.append(_ellipse(130, 50, 22, 10, fill="#caa", sw=1.1))
    o.append(tx(230, 16, "(c)"))
    o.append(_circle(230, 50, 12, fill="#caa", sw=1.1))
    return _finish(o, 270, 75,
                   "Thermistor: (a) thanh, (b) đĩa, (c) hạt.",
                   "Thermistors: (a) rod, (b) disc, (c) bead.")


# =====================================================================
# Figure 1.30 — Thermocouple
# =====================================================================
def fig_1_30():
    o = []
    o.append(_rect(20, 40, 30, 30, "#c90", sw=1.1))
    o.append(_rect(120, 40, 30, 30, "#099", sw=1.1))
    o.append(_line(50, 55, 120, 55, color=INK, sw=2))
    o.append(_circle(85, 55, 4, fill=INK))
    o.append(tx(85, 75, "Junction", 6.3))
    o.append(tx(2, 36, "Metal A", 6))
    o.append(tx(122, 36, "Metal B", 6))
    o.append(tx(60, 95, "p.d. between junctions", 6.3, color=GREY))
    return _finish(o, 175, 110,
                   "Cặp nhiệt điện (thermocouple): hiệu điện thế giữa hai mối nối phụ thuộc vào nhiệt độ.",
                   "Thermocouple: a temperature difference between the junctions gives a p.d. between them.")


# =====================================================================
# Figure 1.31 — Thermocouple e.m.f. vs temperature (common types)
# =====================================================================
def fig_1_31():
    o = []
    o.append(_axes(40, 25, 140, 75, "Temperature / °C", "E", xt=[(0, "0"), (1, "400")], yt=[(0, "0"), (1, "E")]))
    o.append(_curve(lambda t: t, 40, 25, 140, 75, xr=(0, 1), yr=(0, 1), sw=1.5, color=RED))
    o.append(_curve(lambda t: 0.7 * t, 40, 25, 140, 75, xr=(0, 1), yr=(0, 1), sw=1.5, color=BLUE, dash="4 3"))
    return _finish(o, 210, 120,
                   "Suất điện động của các cặp nhiệt điện phổ biến (E, J, K, T) thay đổi theo nhiệt độ.",
                   "Thermocouples: chromel-constantan (E), chromel-alumel (K), copper-constantan (T).")


# =====================================================================
# Figure 1.32 — Cold junction compensation
# =====================================================================
def fig_1_32():
    o = []
    o.append(bx(20, 30, 70, 36, "Thermo-\ncouple", fill="#eef3fb"))
    o.append(bx(120, 30, 80, 36, "Compensation\ncircuit", fill="#eef3fb"))
    o.append(bx(120, 90, 80, 36, "Display", fill="#eef3fb"))
    o.append(ar(90, 48, 120, 48))
    o.append(ar(200, 48, 230, 48, dash="4 3"))
    o.append(ar(160, 66, 160, 90))
    o.append(tx(8, 24, "At 0°C", 6.3))
    o.append(tx(235, 44, "Signal", 6.3, anchor="start"))
    return _finish(o, 290, 140,
                   "Bù mối nối lạnh: mạch bù tạo suất điện động bù để mô phỏng mối nối ở 0°C.",
                   "Cold junction compensation to compensate for the cold junction not being at 0°C.")


# =====================================================================
# Figure 1.33 — LM35 connections
# =====================================================================
def fig_1_33():
    o = []
    o.append(tx(70, 16, "(a)"))
    o.append(_rect(30, 30, 40, 70, "#eef3fb", sw=1.1))
    o.append(tx(50, 26, "LM35"))
    o.append(tx(50, 60, "+5V", 6))
    o.append(tx(50, 78, "GND", 6))
    o.append(tx(50, 96, "Vout", 6))
    o.append(tx(190, 16, "(b)"))
    o.append(_rect(170, 30, 40, 70, "#eef3fb", sw=1.1))
    o.append(tx(190, 26, "LM35"))
    o.append(tx(190, 60, "+5V", 6))
    o.append(tx(190, 78, "-V", 6))
    o.append(tx(190, 96, "Vout", 6))
    return _finish(o, 250, 110,
                   "Kết nối LM35: (a) dải 12–110°C, (b) dải -40–110°C.",
                   "LM35 connections (a) 12°C to 110°C, (b) -40°C to 110°C.")


# =====================================================================
# Figure 1.34 — Resistance to voltage conversion (potential divider)
# =====================================================================
def fig_1_34():
    o = []
    o.append(tx(100, 18, "Thermistor"))
    o.append(_rect(40, 30, 40, 56, "#eef3fb", sw=1.1))
    o.append(_rect(120, 30, 40, 56, "#eef3fb", sw=1.1))
    o.append(_line(80, 40, 120, 40, color=INK, sw=1.4))
    o.append(_line(80, 76, 120, 76, color=INK, sw=1.4))
    o.append(_line(80, 40, 80, 20, color=INK, sw=1.4))
    o.append(_line(120, 40, 120, 20, color=INK, sw=1.4))
    o.append(_line(80, 20, 120, 20, color=INK, sw=1.4))
    o.append(ar(100, 20, 100, 8))
    o.append(tx(100, 4, "+6 V", 6.3))
    o.append(ar(80, 76, 60, 76))
    o.append(tx(40, 92, "Output", 6.3))
    return _finish(o, 200, 105,
                   "Chuyển đổi trở → điện áp bằng mạch phân áp cho thermistor.",
                   "Resistance to voltage conversion for a thermistor.")


# =====================================================================
# Figure 1.35 — Protection against high currents
# =====================================================================
def fig_1_35():
    o = []
    o.append(_line(30, 50, 70, 50, color=INK, sw=1.4))
    o.append(_rect(70, 38, 26, 24, "#eef3fb", sw=1.1))
    o.append(tx(83, 54, "R", 8))
    o.append(_line(96, 50, 130, 50, color=INK, sw=1.4))
    o.append(_rect(130, 38, 30, 24, fill="#fff", sw=1.4))
    o.append(tx(145, 33, "Fuse", 6))
    o.append(ar(30, 50, 14, 50))
    o.append(ar(160, 50, 185, 50))
    o.append(tx(2, 46, "In", 6.3))
    o.append(tx(190, 46, "Out", 6.3, anchor="start"))
    return _finish(o, 220, 75,
                   "Bảo vệ chống dòng quá lớn bằng điện trở nối tiếp và cầu chì.",
                   "Protection against high currents.")


# =====================================================================
# Figure 1.36 — Optoisolator
# =====================================================================
def fig_1_36():
    o = []
    o.append(bx(15, 30, 70, 36, "LED\n(infrared)", fill="#eef3fb"))
    o.append(bx(135, 30, 80, 36, "Photo-\ntransistor", fill="#eef3fb"))
    o.append(_line(85, 48, 135, 48, color=INK, sw=1.4, dash="3 3"))
    o.append(tx(100, 42, "IR", 6.5))
    o.append(ar(5, 48, 15, 48))
    o.append(ar(215, 48, 235, 48))
    o.append(tx(2, 44, "In", 6.3))
    o.append(tx(238, 44, "Out", 6.3, anchor="start"))
    return _finish(o, 260, 75,
                   "Bộ cách ly quang (optoisolator): dùng bức xạ hồng ngoại truyền tín hiệu giữa hai mạch cách ly.",
                   "Optoisolator: infrared radiation is used to transmit signal from input to output circuits.")


# =====================================================================
# Figure 1.37 — Signals: (a) analogue, (b) digital
# =====================================================================
def fig_1_37():
    o = []
    o.append(tx(60, 16, "(a)"))
    o.append(_axes(20, 40, 100, 50, "Time", "Signal"))
    o.append(_curve(lambda t: 0.5 + 0.4 * math.sin(6 * t), 20, 40, 100, 50, xr=(0, 1), yr=(0, 1), sw=1.5, color=BLUE))
    o.append(tx(220, 16, "(b)"))
    o.append(_axes(160, 40, 100, 50, "Time", "Signal"))
    o.append(_poly([(160, 70), (180, 70), (180, 45), (200, 45), (200, 70), (220, 70), (220, 45), (240, 45), (240, 70)],
                   sw=1.5, color=RED))
    return _finish(o, 300, 105,
                   "Tín hiệu: (a) tương tự (biến liên tục), (b) số (từng bước, xung bật/tắt).",
                   "Signals: (a) analogue, (b) digital.")


# =====================================================================
# Figure 1.38 — Sampling, sampling pulse, sampled, held
# =====================================================================
def fig_1_38():
    o = []
    o.append(_axes(15, 30, 90, 40, "Time", "a)", xt=[], yt=[]))
    o.append(_curve(lambda t: 0.5 + 0.35 * math.sin(7 * t), 15, 30, 90, 40, xr=(0, 1), yr=(0, 1), sw=1.4, color=BLUE))
    o.append(_axes(125, 30, 90, 40, "Time", "b)", xt=[], yt=[]))
    o.append(_poly([(125, 60), (135, 60), (135, 42), (143, 42), (143, 60), (153, 60), (153, 42), (161, 42), (161, 60), (171, 60), (171, 42), (179, 42), (179, 60), (189, 60), (189, 42), (197, 42), (197, 60), (205, 60), (205, 42), (213, 42), (213, 60)], sw=1.3, color=GREY))
    o.append(_axes(15, 90, 90, 40, "Time", "c)", xt=[], yt=[]))
    o.append(_poly([(15, 116), (25, 116), (25, 104), (45, 104), (45, 98), (70, 98), (70, 90), (95, 90), (95, 84), (105, 84)], sw=1.4, color=BLUE))
    o.append(_axes(125, 90, 90, 40, "Time", "d)", xt=[], yt=[]))
    o.append(_poly([(125, 116), (25 + 100, 116), (25 + 100, 116)], sw=1))
    # held: step signal
    o.append(_poly([(125, 116), (135, 116), (135, 106), (160, 106), (160, 98), (190, 98), (190, 90), (215, 90)], sw=1.4, color=BLUE))
    return _finish(o, 230, 140,
                   "Chuyển đổi số: (a) tín hiệu tương tự, (b) xung lấy mẫu, (c) tín hiệu đã lấy mẫu, (d) tín hiệu giữ.",
                   "(a) Analogue signal, (b) time signal, (c) sampled signal, (d) sampled and held signal.")


# =====================================================================
# Figure 1.39 — Analogue-to-digital conversion block diagram
# =====================================================================
def fig_1_39():
    o = []
    o.append(bx(15, 40, 70, 36, "Sample &\nhold", fill="#eef3fb"))
    o.append(bx(130, 40, 85, 36, "Analogue-to-\ndigital conv.", fill="#eef3fb"))
    o.append(ar(5, 58, 15, 58))
    o.append(ar(85, 58, 130, 58))
    o.append(ar(215, 58, 250, 58))
    o.append(tx(2, 54, "Analogue", 6))
    o.append(tx(2, 62, "input", 6))
    o.append(tx(255, 54, "Digital", 6, anchor="start"))
    o.append(tx(255, 62, "signal", 6, anchor="start"))
    return _finish(o, 320, 80,
                   "Chuyển đổi tương tự–số: khối lấy mẫu–giữ theo sau là bộ chuyển đổi ADC.",
                   "Analogue-to-digital conversion.")


# =====================================================================
# Figure 1.40 — Digital output from a 3-bit ADC
# =====================================================================
def fig_1_40():
    o = []
    o.append(_axes(35, 30, 150, 70, "Analogue input (frac. of max)", "Digital"))
    steps = ["000", "001", "010", "011", "100", "101", "110", "111"]
    for i, s in enumerate(steps):
        x = 35 + i * 150 / 8.0
        o.append(_line(x, 100, x, 32, color=GREY, sw=0.6))
    o.append(_poly([(35, 100), (35 + 150 / 8, 100), (35 + 150 / 8, 100 - 70 / 8),
                    (35 + 300 / 8, 100 - 70 / 8), (35 + 300 / 8, 100 - 140 / 8),
                    (35 + 450 / 8, 100 - 140 / 8), (35 + 450 / 8, 100 - 210 / 8),
                    (35 + 600 / 8, 100 - 210 / 8), (35 + 600 / 8, 100 - 280 / 8),
                    (35 + 750 / 8, 100 - 280 / 8), (35 + 750 / 8, 100 - 350 / 8),
                    (35 + 900 / 8, 100 - 350 / 8), (35 + 900 / 8, 100 - 420 / 8),
                    (35 + 1050 / 8, 100 - 420 / 8), (35 + 1050 / 8, 100 - 490 / 8),
                    (35 + 1200 / 8, 100 - 490 / 8)], sw=1.5, color=BLUE))
    return _finish(o, 210, 120,
                   "Đầu ra số của ADC 3 bit: 8 từ mã hóa điện áp tương tự thành 8 mức.",
                   "Digital output from an ADC (3-bit example).")


# =====================================================================
# Figure 1.41 — Digital-to-analogue conversion
# =====================================================================
def fig_1_41():
    o = []
    o.append(_axes(35, 30, 150, 70, "Digital word input", "Analogue"))
    o.append(_poly([(35, 100), (35 + 150 / 8, 100), (35 + 150 / 8, 100 - 70 / 8),
                    (35 + 300 / 8, 100 - 70 / 8), (35 + 300 / 8, 100 - 140 / 8),
                    (35 + 450 / 8, 100 - 140 / 8), (35 + 450 / 8, 100 - 210 / 8),
                    (35 + 600 / 8, 100 - 210 / 8), (35 + 600 / 8, 100 - 280 / 8),
                    (35 + 750 / 8, 100 - 280 / 8), (35 + 750 / 8, 100 - 350 / 8),
                    (35 + 900 / 8, 100 - 350 / 8), (35 + 900 / 8, 100 - 420 / 8),
                    (35 + 1050 / 8, 100 - 420 / 8), (35 + 1050 / 8, 100 - 490 / 8),
                    (35 + 1200 / 8, 100 - 490 / 8)], sw=1.5, color=RED))
    return _finish(o, 210, 120,
                   "Chuyển đổi số–tương tự: từ mã nhị phân thành giá trị tương tự tương đương.",
                   "Digital-to-analogue conversion.")


# =====================================================================
# Figure 1.42 — 741 operational amplifier pinout
# =====================================================================
def fig_1_42():
    o = []
    o.append(_rect(60, 25, 80, 90, "#eef3fb", sw=1.2))
    o.append(tx(100, 20, "741 op-amp", 7))
    pins = {1: "Offset null", 2: "Inverting", 3: "Non-inv.", 4: "-V",
            5: "Offset null", 6: "Output", 7: "+V", 8: "N/C"}
    for p in range(1, 9):
        a = (p - 1) * 45 * math.pi / 180
        x = 100 + 44 * math.cos(a)
        y = 70 + 44 * math.sin(a)
        o.append(_circle(x, y, 3, fill="#fff", sw=1))
        o.append(tx(x, y - 7, str(p), 6.5))
        o.append(tx(x + (8 if math.cos(a) >= 0 else -8), y + 3, pins[p], 5.6,
                    anchor="start" if math.cos(a) >= 0 else "end"))
    return _finish(o, 220, 130,
                   "Sơ đồ chân của op-amp 741: chân 2 vào đảo, 3 không đảo, 6 ra, 4 và 7 cấp nguồn.",
                   "The 741 operational amplifier pin connections.")


# =====================================================================
# Figure 1.43 — Inverting amplifier
# =====================================================================
def fig_1_43():
    o = []
    o.append(_circle(100, 55, 22, fill="#eef3fb", sw=1.2))
    o.append(tx(100, 59, "−", 14))
    o.append(tx(100, 30, "+", 11))
    o.append(_line(62, 55, 40, 55, color=INK, sw=1.4))
    o.append(_line(78, 55, 62, 55, color=INK, sw=1.4))
    o.append(_line(40, 55, 40, 95, color=INK, sw=1.4))
    o.append(_line(40, 95, 80, 95, color=INK, sw=1.4))
    o.append(_line(80, 95, 80, 77, color=INK, sw=1.4))
    o.append(_line(80, 77, 100, 77, color=INK, sw=1.4))
    o.append(_line(122, 55, 160, 55, color=INK, sw=1.4))
    o.append(tx(28, 50, "Vin", 7))
    o.append(tx(165, 50, "Vout", 7, anchor="start"))
    o.append(tx(55, 90, "R1", 7))
    o.append(tx(92, 90, "R2", 7))
    return _finish(o, 210, 110,
                   "Bộ khuếch đại đảo: Vout/Vin = −R2/R1.",
                   "Inverting amplifier.")


# =====================================================================
# Figure 1.44 — Differential amplifier
# =====================================================================
def fig_1_44():
    o = []
    o.append(_circle(100, 55, 22, fill="#eef3fb", sw=1.2))
    o.append(tx(100, 59, "−", 14))
    o.append(tx(100, 30, "+", 11))
    o.append(_line(40, 40, 78, 40, color=INK, sw=1.4))
    o.append(_line(78, 40, 78, 55, color=INK, sw=1.4))
    o.append(_line(40, 70, 78, 70, color=INK, sw=1.4))
    o.append(_line(78, 70, 78, 55, color=INK, sw=1.4))
    o.append(_line(122, 55, 160, 55, color=INK, sw=1.4))
    o.append(_line(40, 40, 40, 90, color=INK, sw=1.4))
    o.append(_line(40, 90, 72, 90, color=INK, sw=1.4))
    o.append(_line(72, 90, 72, 77, color=INK, sw=1.4))
    o.append(tx(20, 36, "V1", 7, anchor="end"))
    o.append(tx(20, 66, "V2", 7, anchor="end"))
    o.append(tx(165, 50, "Vout", 7, anchor="start"))
    return _finish(o, 210, 110,
                   "Bộ khuếch đại vi sai: khuếch đại hiệu giữa hai điện áp vào V1 và V2.",
                   "Differential amplifier.")


# =====================================================================
# Figure 1.45 — (a) Two-position, (b) three-position valves
# =====================================================================
def fig_1_45():
    o = []
    o.append(tx(55, 16, "(a)"))
    o.append(_rect(20, 30, 34, 34, "#fff", sw=1.3))
    o.append(_line(37, 30, 37, 64, color=INK, sw=1.2))
    o.append(tx(110, 16, "(b)"))
    o.append(_rect(90, 30, 50, 34, "#fff", sw=1.3))
    o.append(_line(107, 30, 107, 64, color=INK, sw=1))
    o.append(_line(123, 30, 123, 64, color=INK, sw=1))
    return _finish(o, 170, 70,
                   "Van điều hướng: (a) hai vị trí, (b) ba vị trí.",
                   "(a) Two position, (b) three position valves.")


# =====================================================================
# Figure 1.46 — (a) Flow path, (b) shut-off, (c) initial connections
# =====================================================================
def fig_1_46():
    o = []
    o.append(tx(55, 16, "(a)"))
    o.append(_rect(20, 30, 34, 30, "#fff", sw=1.3))
    o.append(_line(37, 30, 37, 60, color=INK, sw=1))
    o.append(_line(22, 45, 52, 45, color=BLUE, sw=1.4))
    o.append(_poly([(44, 41), (50, 45), (44, 49)], fill=BLUE, sw=0))
    o.append(tx(120, 16, "(b)"))
    o.append(_rect(95, 30, 34, 30, "#fff", sw=1.3))
    o.append(_line(112, 30, 112, 60, color=INK, sw=1))
    o.append(_line(105, 45, 119, 45, color=INK, sw=1.4))
    o.append(tx(200, 16, "(c)"))
    o.append(_rect(180, 30, 34, 30, "#fff", sw=1.3))
    o.append(_line(197, 30, 197, 60, color=INK, sw=1))
    o.append(tx(186, 70, "ports", 6))
    return _finish(o, 250, 80,
                   "Ký hiệu van: (a) đường chảy, (b) đóng, (c) nối ban đầu.",
                   "(a) Flow path, (b) shut-off, (c) initial connections.")


# =====================================================================
# Figure 1.47 — Commonly used directional valves (simplified)
# =====================================================================
def fig_1_47():
    o = []
    labels = ["2/2", "2/2", "3/2", "3/2", "4/2", "5/2", "5/3"]
    for i, lab in enumerate(labels):
        x = 15 + i * 62
        o.append(_rect(x, 30, 44, 40, "#fff", sw=1.2))
        o.append(_line(x + 22, 30, x + 22, 70, color=INK, sw=0.9))
        o.append(tx(x + 22, 22, lab, 6.5))
    o.append(tx(220, 95, "P pressure, R/S exhaust, A/B signal ports", 6, color=GREY))
    return _finish(o, 460, 110,
                   "Các van điều hướng thường dùng: 2/2, 3/2, 4/2, 5/2, 5/3 (số cổng/số vị trí).",
                   "Commonly used direction valves: P or 1 = pressure, R/S or 3/5 = exhaust, A/B or 2/4 = signal.")


# =====================================================================
# Figure 1.48 — Valve actuation methods (simplified icons)
# =====================================================================
def fig_1_48():
    o = []
    meth = ["Push", "Plunger", "Lever", "Spring", "Pedal", "Roller", "Solenoid", "Pneum."]
    for i, m in enumerate(meth):
        x = 15 + i * 52
        o.append(_rect(x, 35, 40, 30, "#eef3fb", sw=1.1))
        o.append(tx(x + 20, 55, m, 5.8))
    return _finish(o, 440, 80,
                   "Các cách tác động van: nút bấm, cần gạt, đòn bẩy, lò xo, bàn đạp, con lăn, solenoid, khí nén.",
                   "Examples of valve actuation methods.")


# =====================================================================
# Figure 1.49 — Solenoid-activated 3/2 valve with return spring
# =====================================================================
def fig_1_49():
    o = []
    o.append(_rect(40, 30, 50, 44, "#fff", sw=1.3))
    o.append(_line(65, 30, 65, 74, color=INK, sw=1))
    o.append(tx(65, 22, "3/2", 6.5))
    o.append(_rect(15, 35, 14, 30, "#eef3fb", sw=1))
    o.append(tx(22, 55, "S", 6))  # solenoid
    o.append(_line(100, 52, 130, 52, color=INK, sw=1.3))
    o.append(_line(100, 52, 100, 30, color=INK, sw=1.3))
    o.append(tx(134, 48, "to cylinder", 6, anchor="start"))
    return _finish(o, 200, 90,
                   "Van 3/2 tác động bằng solenoid và hoàn vị bằng lò xo.",
                   "Symbol for a solenoid-activated valve with return spring.")


# =====================================================================
# Figure 1.50 — Control of a single-acting cylinder
# =====================================================================
def fig_1_50():
    o = []
    o.append(tx(120, 16, "(a) before"))
    o.append(_rect(20, 35, 40, 28, "#fff", sw=1.2))
    o.append(_line(40, 35, 40, 63, color=INK, sw=0.9))
    o.append(_rect(150, 35, 90, 28, "#eef3fb", sw=1.1))
    o.append(_line(195, 49, 240, 49, color=INK, sw=1.4))
    o.append(_rect(240, 43, 20, 12, "#ddd", sw=1))
    o.append(tx(120, 90, "(b) when activated"))
    o.append(_rect(20, 100, 40, 28, "#fff", sw=1.2))
    o.append(_line(40, 100, 40, 128, color=INK, sw=0.9))
    o.append(_rect(150, 100, 90, 28, "#eef3fb", sw=1.1))
    o.append(_line(195, 114, 245, 114, color=INK, sw=1.4))
    o.append(_rect(245, 108, 20, 12, "#ddd", sw=1))
    return _finish(o, 290, 145,
                   "Điều khiển xi lanh tác động đơn: van đổi vị trí khi solenoid được kích, piston dịch chuyển.",
                   "Control of a single-acting cylinder: (a) before solenoid activated, (b) when solenoid activated.")


# =====================================================================
# Figure 1.51 — Control of a double-acting cylinder
# =====================================================================
def fig_1_51():
    o = []
    o.append(_rect(20, 40, 40, 30, "#fff", sw=1.2))
    o.append(_line(40, 40, 40, 70, color=INK, sw=0.9))
    o.append(_rect(140, 40, 110, 30, "#eef3fb", sw=1.1))
    o.append(_line(195, 55, 250, 55, color=INK, sw=1.4))
    o.append(_rect(250, 49, 22, 12, "#ddd", sw=1))
    o.append(_line(250, 55, 280, 55, color=INK, sw=1.2, dash="4 3"))
    o.append(tx(2, 36, "S1", 6))
    o.append(tx(2, 76, "S2", 6))
    return _finish(o, 300, 90,
                   "Điều khiển xi lanh tác động kép bằng van hai solenoid.",
                   "Control of a double-acting cylinder.")


# =====================================================================
# Figure 1.52 — Flow controlled by movement of a plug
# =====================================================================
def fig_1_52():
    o = []
    o.append(_path("M20 40 L120 40", fill="none", sw=2, color=INK))
    o.append(_path("M20 70 L120 70", fill="none", sw=2, color=INK))
    o.append(_poly([(120, 40), (120, 70), (150, 55)], fill="#eef3fb", sw=1.2))
    o.append(_line(150, 55, 150, 95, color=INK, sw=1.4))
    o.append(_circle(150, 100, 7, fill="#fff", sw=1.2))
    o.append(tx(155, 96, "plug", 6))
    return _finish(o, 210, 115,
                   "Lưu lượng được điều khiển bởi sự dịch chuyển của côn (plug) trong đường chảy.",
                   "Flow controlled by movement of a plug.")


# =====================================================================
# Figure 1.53 — (a) Direct action, (b) reverse action diaphragm valve
# =====================================================================
def fig_1_53():
    o = []
    o.append(tx(70, 16, "(a)"))
    o.append(_ellipse(40, 45, 26, 12, fill="#eef3fb", sw=1.2))
    o.append(_line(40, 33, 40, 14, color=INK, sw=1.4))
    o.append(_path("M60 14 q15 15 0 30", fill="none", sw=2, color="#888"))
    o.append(tx(40, 70, "Air pressure\nincreases → close", 6))
    o.append(tx(230, 16, "(b)"))
    o.append(_ellipse(200, 45, 26, 12, fill="#eef3fb", sw=1.2))
    o.append(_line(200, 57, 200, 76, color=INK, sw=1.4))
    o.append(_path("M180 76 q15 -15 0 -30", fill="none", sw=2, color="#888"))
    o.append(tx(200, 92, "Air pressure\nincreases → open", 6))
    return _finish(o, 300, 110,
                   "Van màng: (a) tác động thuận (áp tăng → đóng), (b) tác động nghịch (áp tăng → mở).",
                   "(a) Direct action, (b) reverse action.")


# =====================================================================
# Figure 1.54 — Direct action plug: (a) close, (b) open
# =====================================================================
def fig_1_54():
    o = []
    o.append(tx(90, 16, "(a) air ↑ → close"))
    o.append(_poly([(40, 40), (90, 40), (90, 70), (130, 55)], fill="#eef3fb", sw=1.2))
    o.append(_line(90, 55, 90, 95, color=INK, sw=1.3))
    o.append(_circle(90, 100, 7, fill="#fff", sw=1.1))
    o.append(tx(230, 16, "(b) air ↑ → open"))
    o.append(_poly([(180, 40), (230, 40), (230, 70), (270, 55)], fill="#eef3fb", sw=1.2))
    o.append(_line(230, 55, 230, 95, color=INK, sw=1.3))
    o.append(_circle(230, 100, 7, fill="#fff", sw=1.1))
    return _finish(o, 310, 115,
                   "Dạng côn: (a) áp tăng thì đóng, (b) áp tăng thì mở, tùy vị trí lò xo.",
                   "Direct action: (a) air pressure increase to close, (b) air pressure increase to open.")


# =====================================================================
# Figure 1.55 — Effect of plug shape on flow
# =====================================================================
def fig_1_55():
    o = []
    o.append(_axes(40, 30, 130, 70, "% stem displacement", "Flow %"))
    o.append(_poly([(40, 100), (170, 40)], sw=1.5, color=BLUE))
    o.append(_poly([(40, 100), (70, 60), (100, 48), (130, 44), (170, 42)], sw=1.5, color=RED))
    o.append(_poly([(40, 100), (60, 55), (80, 45), (100, 42), (170, 40)], sw=1.5, color=GREEN))
    o.append(tx(40, 116, "Linear / Equal % / Quick opening", 6, color=GREY))
    return _finish(o, 210, 130,
                   "Ảnh hưởng của dạng côn đến lưu lượng: tuyến tính, phần trăm đều, mở nhanh.",
                   "Effect of plug shape on flow.")


# =====================================================================
# Figure 1.56 — (a) Series, (b) shunt, (c) compound, (d) separate DC motors
# =====================================================================
def fig_1_56():
    o = []
    def motor(x, y, label):
        o.append(_circle(x, y, 18, fill="#eef3fb", sw=1.2))
        o.append(_circle(x, y, 4, fill="#fff", sw=1))
        o.append(tx(x, y + 30, label, 6.3))
    motor(35, 35, "(a) series")
    o.append(_line(17, 43, 35, 43, color=INK, sw=1.4))
    o.append(_line(35, 43, 53, 43, color=INK, sw=1.4))
    motor(130, 35, "(b) shunt")
    o.append(_line(112, 35, 148, 35, color=INK, sw=1.4))
    motor(225, 35, "(c) compound")
    o.append(_line(207, 43, 225, 43, color=INK, sw=1.4))
    o.append(_line(225, 27, 225, 17, color=INK, sw=1.4))
    o.append(_line(207, 27, 243, 27, color=INK, sw=1.4))
    motor(320, 35, "(d) separate")
    o.append(_line(302, 27, 338, 27, color=INK, sw=1.4))
    o.append(_line(302, 43, 338, 43, color=INK, sw=1.4))
    return _finish(o, 380, 75,
                   "Động cơ DC: (a) nối tiếp, (b) song song, (c) hỗn hợp, (d) kích từ riêng.",
                   "(a) Series, (b) shunt, (c) compound, (d) separately wound.")


# =====================================================================
# Figure 1.57 — Torque-speed characteristics of DC motors
# =====================================================================
def fig_1_57():
    o = []
    o.append(_axes(40, 25, 140, 80, "Angular speed", "Torque"))
    o.append(_poly([(40, 30), (180, 100)], sw=1.5, color=RED))
    o.append(_poly([(40, 45), (180, 95)], sw=1.5, color=BLUE, dash="4 3"))
    o.append(_poly([(40, 60), (180, 90)], sw=1.5, color=GREEN, dash="2 2"))
    o.append(tx(40, 120, "Series / shunt / compound", 6, color=GREY))
    return _finish(o, 220, 135,
                   "Đặc tuyến mô-men/tốc độ của các loại động cơ DC.",
                   "Torque-speed characteristics of d.c. motors.")


# =====================================================================
# Figure 1.58 — Permanent-magnet stepper motor (2-phase)
# =====================================================================
def fig_1_58():
    o = []
    o.append(_circle(80, 60, 46, fill="#f3f3f3", sw=1.2))
    for i, a in enumerate([0, 90, 180, 270]):
        rad = a * math.pi / 180
        o.append(_rect(80 + 38 * math.cos(rad) - 7, 60 + 38 * math.sin(rad) - 7, 14, 14, "#eef3fb", sw=1))
    o.append(_circle(80, 60, 12, fill="#fff", sw=1.4))
    o.append(tx(80, 130, "Rotor steps 90° between poles", 6.3, color=GREY))
    return _finish(o, 175, 145,
                   "Động cơ bước nam châm vĩnh cửu (2 pha): rô-to bước 90° giữa các cực.",
                   "The basic principles of the permanent magnet stepper motor (2-phase) with a rotor giving 90° steps.")


# =====================================================================
# Figure 1.59 — 3-phase variable reluctance stepper motor
# =====================================================================
def fig_1_59():
    o = []
    o.append(_circle(80, 60, 46, fill="#f3f3f3", sw=1.2))
    for i in range(6):
        a = i * 60 * math.pi / 180
        o.append(_rect(80 + 38 * math.cos(a) - 7, 60 + 38 * math.sin(a) - 7, 14, 14, "#eef3fb", sw=1))
    o.append(_circle(80, 60, 14, fill="#fff", sw=1.4))
    o.append(_path("M80 46 q14 14 0 28 q-14 -14 0 -28", fill="none", sw=1, color=GREY))
    o.append(tx(80, 130, "Soft-steel toothed rotor aligns to min. reluctance", 6, color=GREY))
    return _finish(o, 175, 145,
                   "Động cơ bước tựa từ biến thiên 3 pha: rô-to thép mềm căn chỉnh vào vị trí từ kháng nhỏ nhất.",
                   "Basic principles of a 3-phase variable reluctance stepper motor.")


# =====================================================================
# Figure 1.60 — Stepper driver circuit SAA 1027
# =====================================================================
def fig_1_60():
    o = []
    o.append(_rect(60, 25, 90, 70, "#eef3fb", sw=1.2))
    o.append(tx(105, 20, "SAA1027", 7))
    for i, (px, py, lab) in enumerate([(60, 35, "Trig"), (60, 50, "Rot"), (60, 65, "Set"), (150, 35, "Coil A"), (150, 50, "Coil B"), (150, 65, "Coil C")]):
        o.append(tx(px - 4, py + 3, lab, 6, anchor="end" if px < 105 else "start"))
        o.append(_line(px, py, 105 if px < 105 else 105, py, color=INK, sw=1.2))
    o.append(tx(105, 110, "+12 V supply; 4-phase motor", 6.3, color=GREY))
    return _finish(o, 230, 125,
                   "Mạch điều khiển SAA1027 cho động cơ bước 4 pha 12 V.",
                   "Driver circuit SAA 1027 for a 12 V 4-phase stepper motor.")


# =====================================================================
# Figure 1.61 — Control of motor shaft speed (pictorial)
# =====================================================================
def fig_1_61():
    o = []
    o.append(bx(15, 25, 80, 34, "Potentiometer\nset value", fill="#eef3fb"))
    o.append(bx(15, 80, 80, 34, "Differential\namplifier", fill="#eef3fb"))
    o.append(bx(150, 52, 80, 34, "Motor", fill="#eef3fb"))
    o.append(bx(150, 105, 80, 34, "Tachogenerator", fill="#eef3fb"))
    o.append(ar(95, 42, 150, 60, dash="4 3"))
    o.append(ar(150, 69, 95, 80))
    o.append(ar(95, 97, 60, 97, dash="4 3"))
    o.append(ar(60, 97, 60, 114))
    o.append(ar(60, 114, 150, 114))
    o.append(ar(190, 122, 230, 122))
    o.append(tx(235, 118, "Output: shaft", 6, anchor="start"))
    return _finish(o, 320, 160,
                   "Điều khiển tốc độ trục động cơ: potentiometer đặt giá trị, op-amp so sánh, tachogenerator phản hồi.",
                   "Control of the speed of rotation of a shaft.")


# =====================================================================
# Figure 1.62 — Block diagram of motor speed control
# =====================================================================
def fig_1_62():
    o = []
    o.append(bx(15, 30, 80, 34, "Controller:\ndiff. amplifier", fill="#eef3fb"))
    o.append(bx(140, 30, 80, 34, "Motor", fill="#eef3fb"))
    o.append(sumj(115, 47, ["+", "", "-"]))
    o.append(ar(5, 47, 15, 47))
    o.append(ar(95, 47, 104, 47))
    o.append(ar(126, 47, 140, 47))
    o.append(ar(220, 47, 255, 47, dash="4 3"))
    o.append(ar(255, 47, 255, 88))
    o.append(ar(255, 88, 115, 88))
    o.append(ar(115, 88, 115, 58))
    o.append(bx(200, 105, 90, 30, "Tachogenerator", fill="#eef3fb"))
    o.append(ar(245, 105, 255, 88, dash="4 3"))
    o.append(tx(2, 43, "Set value", 6))
    o.append(tx(260, 42, "Output", 6, anchor="start"))
    return _finish(o, 330, 150,
                   "Sơ đồ khối điều khiển tốc độ động cơ: so sánh, luật điều khiển, động cơ, đo bằng tachogenerator.",
                   "Control of the speed of rotation of a shaft (block diagram).")


# =====================================================================
# Figure 1.63 — Position control system (pictorial)
# =====================================================================
def fig_1_63():
    o = []
    o.append(bx(15, 25, 80, 32, "Potentiometer\nset value", fill="#eef3fb"))
    o.append(bx(15, 80, 80, 32, "Comparison +\nADC", fill="#eef3fb"))
    o.append(bx(150, 52, 80, 32, "Stepper\nmotor", fill="#eef3fb"))
    o.append(bx(150, 105, 80, 32, "Tool +\nbelt", fill="#eef3fb"))
    o.append(ar(95, 41, 150, 60, dash="4 3"))
    o.append(ar(150, 68, 95, 80))
    o.append(ar(95, 96, 60, 96, dash="4 3"))
    o.append(ar(60, 96, 60, 113))
    o.append(ar(60, 113, 150, 113))
    o.append(tx(235, 109, "Position", 6, anchor="start"))
    return _finish(o, 320, 155,
                   "Hệ thống điều khiển vị trí: động cơ bước qua dây đai dịch chuyển dụng cụ; potentiometer đo vị trí.",
                   "Position control system.")


# =====================================================================
# Figure 1.64 — Block diagram of position control
# =====================================================================
def fig_1_64():
    o = []
    o.append(bx(15, 30, 80, 32, "Controller:\nmicroproc. + ADC", fill="#eef3fb"))
    o.append(bx(140, 30, 80, 32, "Driver +\nstepper", fill="#eef3fb"))
    o.append(sumj(115, 46, ["+", "", "-"]))
    o.append(ar(5, 46, 15, 46))
    o.append(ar(95, 46, 104, 46))
    o.append(ar(126, 46, 140, 46))
    o.append(ar(220, 46, 255, 46, dash="4 3"))
    o.append(ar(255, 46, 255, 88))
    o.append(ar(255, 88, 115, 88))
    o.append(ar(115, 88, 115, 58))
    o.append(bx(200, 103, 90, 30, "Tool + belt", fill="#eef3fb"))
    o.append(tx(2, 42, "Set value", 6))
    o.append(tx(260, 42, "Position", 6, anchor="start"))
    return _finish(o, 330, 150,
                   "Sơ đồ khối điều khiển vị trí dụng cụ.",
                   "Position control system (block diagram).")


# =====================================================================
# Figure 1.65 — Power assisted steering
# =====================================================================
def fig_1_65():
    o = []
    o.append(bx(15, 30, 80, 30, "Controller", fill="#eef3fb"))
    o.append(bx(120, 30, 80, 30, "Control\nvalve", fill="#eef3fb"))
    o.append(bx(120, 85, 80, 30, "Cylinder", fill="#eef3fb"))
    o.append(bx(120, 135, 80, 30, "Wheels", fill="#eef3fb"))
    o.append(sumj(95, 45, ["+", "", "-"]))
    o.append(ar(5, 45, 15, 45))
    o.append(ar(95, 45, 120, 45))
    o.append(ar(200, 45, 235, 45, dash="4 3"))
    o.append(ar(160, 60, 160, 85))
    o.append(ar(160, 115, 160, 135))
    o.append(ar(160, 150, 95, 150, dash="4 3"))
    o.append(ar(95, 150, 95, 56))
    o.append(tx(2, 41, "Steering\nangle", 6))
    o.append(tx(240, 41, "Wheels", 6, anchor="start"))
    return _finish(o, 320, 185,
                   "Trợ lái: góc lái được thu nhỏ bằng bánh răng, phản hồi cơ khí từ bánh xe qua van thủy lực.",
                   "Power assisted steering.")


# =====================================================================
# Figure 1.66 — (a) Fuel supply system, (b) fuel pressure regulator
# =====================================================================
def fig_1_66():
    o = []
    o.append(tx(120, 16, "(a)"))
    o.append(bx(20, 30, 50, 28, "Tank", fill="#eef3fb"))
    o.append(bx(85, 30, 50, 28, "Pump", fill="#eef3fb"))
    o.append(bx(150, 30, 50, 28, "Filter", fill="#eef3fb"))
    o.append(bx(215, 30, 60, 28, "Regulator", fill="#eef3fb"))
    o.append(bx(215, 75, 60, 28, "Injectors", fill="#eef3fb"))
    o.append(ar(70, 44, 85, 44))
    o.append(ar(135, 44, 150, 44))
    o.append(ar(200, 44, 215, 44))
    o.append(ar(245, 58, 245, 75))
    o.append(tx(230, 95, "(b) regulator: diaphragm + ball + spring", 6, color=GREY))
    return _finish(o, 300, 110,
                   "Hệ thống cấp nhiên liệu: (a) bơm, lọc, van điều áp, vòi phun; (b) van điều áp bằng màng và lò xo.",
                   "(a) Fuel supply system, (b) fuel pressure regulator.")


# =====================================================================
# Figure 1.67 — Fuel supply control system (block diagram)
# =====================================================================
def fig_1_67():
    o = []
    o.append(sumj(40, 45, ["+", "", "-"]))
    o.append(bx(70, 28, 80, 30, "Control law\nspring", fill="#eef3fb"))
    o.append(bx(70, 82, 80, 30, "Correction\n(ball)", fill="#eef3fb"))
    o.append(bx(200, 55, 80, 30, "Process", fill="#eef3fb"))
    o.append(ar(5, 45, 29, 45))
    o.append(ar(51, 45, 70, 45))
    o.append(ar(150, 45, 150, 82, dash="4 3"))
    o.append(ar(150, 97, 150, 68))
    o.append(ar(150, 68, 200, 68))
    o.append(ar(280, 68, 320, 68, dash="4 3"))
    o.append(ar(320, 68, 320, 110))
    o.append(ar(320, 110, 40, 110))
    o.append(ar(40, 110, 40, 56))
    o.append(tx(2, 41, "Set value\n(spring)", 6))
    o.append(tx(326, 63, "Pressure", 6, anchor="start"))
    return _finish(o, 380, 130,
                   "Hệ thống điều khiển áp suất nhiên liệu: lò xo đặt giá trị, màng so sánh, bi hiệu chỉnh, đo bằng màng.",
                   "Fuel supply control system.")


# =====================================================================
# Figure 1.68 — Antilock brakes: (a) schematic, (b) block form
# =====================================================================
def fig_1_68():
    o = []
    o.append(tx(110, 16, "(a)"))
    o.append(bx(20, 30, 70, 30, "Master\ncylinder", fill="#eef3fb"))
    o.append(bx(120, 30, 70, 30, "Modulator\n(valves)", fill="#eef3fb"))
    o.append(bx(120, 85, 70, 30, "Wheel +\nsensor", fill="#eef3fb"))
    o.append(bx(20, 85, 70, 30, "Controller", fill="#eef3fb"))
    o.append(ar(90, 45, 120, 45))
    o.append(ar(155, 60, 155, 85))
    o.append(ar(120, 100, 90, 100, dash="4 3"))
    o.append(ar(90, 100, 90, 72))
    o.append(tx(240, 16, "(b) block form"))
    o.append(bx(220, 40, 90, 30, "Controller", fill="#eef3fb"))
    o.append(sumj(300, 95, ["+", "", "-"]))
    o.append(tx(240, 100, "Wheel\nspeed", 6))
    return _finish(o, 360, 145,
                   "Hệ thống chống bó cứng phanh (ABS): đo tốc độ bánh, so sánh với dữ liệu, điều chỉnh áp suất van.",
                   "Antilock brakes: (a) schematic diagram, (b) block form of the control system.")


# =====================================================================
# Figure 1.69 / 1.70 — Sheet thickness control system
# =====================================================================
def fig_1_69():
    o = []
    o.append(bx(15, 30, 90, 30, "LVDT +\nconverter", fill="#eef3fb"))
    o.append(bx(140, 30, 80, 30, "Amplifier", fill="#eef3fb"))
    o.append(bx(140, 85, 80, 30, "D.C. motor\n(armature)", fill="#eef3fb"))
    o.append(bx(140, 140, 80, 30, "Rolls", fill="#eef3fb"))
    o.append(ar(105, 45, 140, 45))
    o.append(ar(180, 60, 180, 85))
    o.append(ar(180, 115, 180, 140))
    o.append(tx(2, 26, "Thickness", 6))
    o.append(tx(225, 155, "Sheet", 6, anchor="start"))
    return _finish(o, 320, 185,
                   "Điều khiển độ dày tấm: LVDT đo sai lệch, khuếch đại, động cơ chỉnh vị trí rulo trên.",
                   "Sheet thickness control system.")


def fig_1_70():
    o = []
    o.append(bx(15, 30, 80, 30, "LVDT is sensor\n+ comparator", fill="#eef3fb"))
    o.append(bx(130, 30, 80, 30, "Amplifier +\ncorrection", fill="#eef3fb"))
    o.append(bx(130, 85, 80, 30, "Screw +\nroll", fill="#eef3fb"))
    o.append(sumj(105, 47, ["+", "", "-"]))
    o.append(ar(5, 47, 15, 47))
    o.append(ar(95, 47, 130, 47))
    o.append(ar(210, 47, 245, 47, dash="4 3"))
    o.append(ar(170, 60, 170, 85))
    o.append(ar(170, 115, 105, 115, dash="4 3"))
    o.append(ar(105, 115, 105, 58))
    o.append(tx(2, 43, "Thickness", 6))
    o.append(tx(250, 43, "Thickness", 6, anchor="start"))
    return _finish(o, 330, 150,
                   "Sơ đồ khối điều khiển độ dày tấm.",
                   "Sheet thickness control system (block diagram).")


# =====================================================================
# Figure 1.71 / 1.72 — Liquid level control
# =====================================================================
def fig_1_71():
    o = []
    o.append(_rect(120, 40, 90, 70, "#eef3fb", sw=1.2))
    o.append(_line(120, 70, 210, 70, color=BLUE, sw=2))
    o.append(_circle(165, 40, 5, fill=INK))
    o.append(_line(165, 40, 165, 25, color=INK, sw=1.4))
    o.append(_ellipse(60, 55, 26, 12, fill="#eef3fb", sw=1.2))
    o.append(tx(40, 100, "Pneumatic controller (bellows + diaphragm)", 6, color=GREY))
    o.append(tx(225, 64, "Inflow / Outflow", 6, anchor="start"))
    return _finish(o, 320, 120,
                   "Điều khiển mức chất lỏng bằng bộ điều khiển khí nén vận hành bằng phao.",
                   "Level control system.")


def fig_1_72():
    o = []
    o.append(sumj(40, 45, ["+", "", "-"]))
    o.append(bx(70, 28, 90, 30, "Pneumatic\ncontroller", fill="#eef3fb"))
    o.append(bx(70, 82, 90, 30, "Valves +\ntank", fill="#eef3fb"))
    o.append(ar(5, 45, 29, 45))
    o.append(ar(51, 45, 70, 45))
    o.append(ar(160, 45, 195, 45, dash="4 3"))
    o.append(ar(115, 60, 115, 82))
    o.append(ar(115, 112, 40, 112, dash="4 3"))
    o.append(ar(40, 112, 40, 56))
    o.append(tx(2, 41, "Set level", 6))
    o.append(tx(200, 41, "Level", 6, anchor="start"))
    return _finish(o, 300, 140,
                   "Sơ đồ khối điều khiển mức chất lỏng: phao đặt giá trị, bộ điều khiển khí nén, van, bể.",
                   "Level control system (block diagram).")


# =====================================================================
# Figure 1.73 — Robot gripper
# =====================================================================
def fig_1_73():
    o = []
    o.append(_line(80, 30, 50, 90, color=INK, sw=2))
    o.append(_line(80, 30, 110, 90, color=INK, sw=2))
    o.append(_circle(50, 90, 6, fill="#fff", sw=1.2))
    o.append(_circle(110, 90, 6, fill="#fff", sw=1.2))
    o.append(_circle(80, 30, 5, fill=INK))
    o.append(_line(80, 30, 80, 14, color=INK, sw=1.4))
    o.append(tx(80, 105, "Fingers pivot to grip", 6, color=GREY))
    return _finish(o, 180, 120,
                   "Cơ cấu kẹp của robot: các ngón gập lại để giữ vật.",
                   "Robot gripper.")


# =====================================================================
# Figure 1.74 — Gripper control system
# =====================================================================
def fig_1_74():
    o = []
    o.append(sumj(40, 45, ["+", "", "-"]))
    o.append(bx(70, 28, 80, 30, "Controller +\namplifier", fill="#eef3fb"))
    o.append(bx(70, 82, 80, 30, "Servovalve +\ngripper", fill="#eef3fb"))
    o.append(ar(5, 45, 29, 45))
    o.append(ar(51, 45, 70, 45))
    o.append(ar(150, 45, 185, 45, dash="4 3"))
    o.append(ar(115, 60, 115, 82))
    o.append(ar(115, 112, 40, 112, dash="4 3"))
    o.append(ar(40, 112, 40, 56))
    o.append(tx(2, 41, "Force\nrequired", 6))
    o.append(tx(190, 41, "Object", 6, anchor="start"))
    return _finish(o, 290, 140,
                   "Hệ thống điều khiển kẹp: cảm biến lực phản hồi để giữ vật với lực vừa đủ.",
                   "Gripper control system.")


# =====================================================================
# Figure 1.75 — Closed loop machine tool control
# =====================================================================
def fig_1_75():
    o = []
    o.append(bx(15, 30, 80, 30, "Memory\n(program)", fill="#eef3fb"))
    o.append(bx(140, 30, 80, 30, "Controller +\ndrive", fill="#eef3fb"))
    o.append(bx(140, 85, 80, 30, "Tool +\nwork table", fill="#eef3fb"))
    o.append(sumj(115, 47, ["+", "", "-"]))
    o.append(ar(5, 47, 15, 47))
    o.append(ar(95, 47, 104, 47))
    o.append(ar(126, 47, 140, 47))
    o.append(ar(220, 47, 255, 47, dash="4 3"))
    o.append(ar(180, 62, 180, 85))
    o.append(ar(180, 115, 115, 115, dash="4 3"))
    o.append(ar(115, 115, 115, 58))
    o.append(tx(2, 43, "Required\npositions", 6))
    o.append(tx(260, 43, "Workpiece", 6, anchor="start"))
    return _finish(o, 340, 150,
                   "Điều khiển máy công cụ vòng kín: bộ nhớ cung cấp chương trình, đo vị trí bàn máy.",
                   "Closed loop machine tool control system.")


# =====================================================================
# Figure 1.76 — Automatic drill
# =====================================================================
def fig_1_76():
    o = []
    o.append(bx(20, 30, 90, 30, "Switch\nsensor", fill="#eef3fb"))
    o.append(bx(150, 30, 80, 30, "Controller", fill="#eef3fb"))
    o.append(bx(150, 85, 80, 30, "Motor +\ndrill", fill="#eef3fb"))
    o.append(ar(110, 45, 150, 45))
    o.append(ar(190, 60, 190, 85))
    o.append(tx(2, 26, "Workpiece\npresent", 6))
    o.append(tx(235, 100, "Drill down /\nretract", 6, anchor="start"))
    return _finish(o, 300, 145,
                   "Máy khoan tự động: công tắc cảm biến phát hiện chi tiết, bộ điều khiển hạ/khoan/rút mũi khoan.",
                   "An automatic drill.")


# =====================================================================
# Figure 1.77 — Microprocessor-based controller
# =====================================================================
def fig_1_77():
    o = []
    o.append(bx(20, 30, 80, 32, "Inputs from\nsensors", fill="#eef3fb"))
    o.append(bx(130, 30, 90, 32, "Micro-\nprocessor", fill="#eef3fb"))
    o.append(bx(130, 85, 90, 32, "Output to\ncorrection", fill="#eef3fb"))
    o.append(bx(130, 140, 90, 28, "Power\nsupply", fill="#eef3fb"))
    o.append(ar(100, 46, 130, 46))
    o.append(ar(175, 62, 175, 85))
    o.append(ar(20, 110, 175, 110, dash="4 3"))
    o.append(ar(175, 156, 175, 140, dash="4 3"))
    o.append(tx(2, 26, "Measure-\nment", 6))
    o.append(tx(225, 100, "Correction\nelement", 6, anchor="start"))
    return _finish(o, 300, 185,
                   "Bộ điều khiển dựa trên vi xử lý: so sánh đầu vào cảm biến với giá trị yêu cầu, xuất tín hiệu hiệu chỉnh.",
                   "Microprocessor-based controller.")


# ---------------------------------------------------------------------
# Aliases so every figure referenced in the chapter exists.
# ---------------------------------------------------------------------
FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
