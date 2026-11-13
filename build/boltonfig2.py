# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 2.

Every figure is redrawn as a clean vector so it stays legible on a phone,
matching the standard used for the Practical Process Control and SIS readers.
Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).

Re-uses the shared primitives in `vfig`; the small block-diagram composer
helpers below mirror those in boltonfig.py.
"""
import math

from vfig import (BLUE, GOLD, GREY, INK, PAPER, RED, GREEN, _arrow, _axes,
                  _box, _circle, _curve, _defs, _ellipse, _f, _fig, _hatch,
                  _label, _line, _path, _poly, _rect, _ring, _txt, svg)


# ----------------------------------------------------------------- helpers
def _svg(w, h, objs, title=""):
    return svg(w, h, _defs() + "".join(objs), title)


def _f(o, w, h, vi, en, aria_vi="", aria_en=""):
    return _fig(_svg(w, h, o, vi), vi, en, aria_vi or vi, aria_en or en)


def bx(x, y, w, h, label, fill="#eef3fb", size=8):
    return _box(x, y, w, h, label, fill=fill, size=size)


def ar(x1, y1, x2, y2, dash="", color=INK, sw=1.2):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def ln(x1, y1, x2, y2, dash="", color=INK, sw=0.9):
    return _line(x1, y1, x2, y2, sw=sw, dash=dash, color=color)


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


def sumj(x, y, signs, r=11):
    o = [_circle(x, y, r, fill="#fff")]
    pos = [(x, y - r - 4), (x + r + 5, y + 3), (x, y + r + 5), (x - r - 5, y + 3)]
    for i, s in enumerate(signs[:4]):
        if s:
            o.append(_txt(pos[i][0], pos[i][1], s, 8, anchor="middle", color=INK))
    return "".join(o)


def tap(x, y):
    return _circle(x, y, 2.6, fill=INK)


def wire(o, pts, dash="", color=INK):
    for i in range(len(pts) - 1):
        o.append(ln(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], dash=dash, color=color))


# =====================================================================
# Figure 2.1 - Amplifier system with gain = 10
# =====================================================================
def fig_2_1():
    o = []
    o.append(bx(150, 38, 130, 52, "Gain = 10"))
    o.append(ar(40, 64, 150, 64))
    o.append(ar(280, 64, 400, 64))
    o.append(tx(28, 60, "Input", 7.5, anchor="start"))
    o.append(tx(28, 70, "signal", 7.5, anchor="start"))
    o.append(tx(390, 60, "Output", 7.5, anchor="start"))
    o.append(tx(390, 70, "signal", 7.5, anchor="start"))
    return _f(o, 440, 100,
              "Hệ khuếch đại với hệ số khuyếch đại bằng 10: đầu ra gấp mười lần đầu vào.",
              "Amplifier system with a gain of 10: the output is ten times the input.")


# =====================================================================
# Figure 2.2 - (a) spring system, (b) step input, (c) step response
# =====================================================================
def fig_2_2():
    o = []
    # (a) spring system
    ax, ay = 18, 30
    o.append(_rect(ax, ay, 110, 78, "#fff", sw=1.1))
    o.append(tx(ax + 55, ay - 6, "(a)"))
    o.append(tx(ax + 55, ay + 16, "Spring", 7.5))
    o.append(tx(ax + 55, ay + 27, "system", 7.5))
    # zigzag spring
    zx = ax + 55
    pts = [(zx - 18, ay + 46)]
    for i in range(6):
        pts.append((zx - 18 + (36 if i % 2 == 0 else 0), ay + 50 + i * 5))
    pts.append((zx + 18, ay + 76))
    o.append(_poly(pts, color=INK, sw=1))
    o.append(ar(ax + 4, ay + 46, ax + 30, ay + 46))
    o.append(tx(ax + 2, ay + 40, "Load", 6.5, anchor="start"))
    o.append(ar(ax + 30, ay + 76, ax + 4, ay + 76))
    o.append(tx(ax + 2, ay + 83, "Deflection", 6.5, anchor="start"))
    # (b) step input
    bx_, by = 160, 30
    o.append(tx(bx_ + 55, by - 6, "(b)"))
    o.append(_axes(bx_, by + 20, 110, 70, "Time", ""))
    # step at t=1
    o.append(_curve(lambda t: 0 if t < 1 else 1, bx_, by + 20, 110, 70, xr=(0, 4), yr=(0, 1.2)))
    o.append(tx(bx_ + 55, by + 100, "Input", 7))
    # (c) output
    cx, cy = 300, 30
    o.append(tx(cx + 55, cy - 6, "(c)"))
    o.append(_axes(cx, cy + 20, 110, 70, "Time", ""))
    o.append(_curve(lambda t: 1 - math.exp(-0.6 * t) * math.cos(2.2 * t), cx, cy + 20, 110, 70, xr=(0, 4), yr=(-0.15, 1.2)))
    o.append(tx(cx + 55, cy + 100, "Output", 7))
    return _f(o, 440, 120,
              "Hệ thống lò xo: (a) hệ lò xo với tải không đổi tác động tại một thời điểm, (b) tín hiệu đầu vào dạng bậc, (c) đầu ra biến thiên theo thời gian với đầu vào bậc.",
              "Spring system: (a) the spring system with a constant load applied at some instant, (b) the step input, (c) the output varying with time for the step input.")


# =====================================================================
# Figure 2.3 - Two systems in series and equivalent
# =====================================================================
def fig_2_3():
    o = []
    # (a)
    o.append(tx(70, 16, "(a)"))
    o.append(bx(20, 40, 80, 44, "G1"))
    o.append(bx(140, 40, 80, 44, "G2"))
    o.append(ar(8, 62, 20, 62))
    o.append(ar(100, 62, 140, 62))
    o.append(ar(220, 62, 250, 62))
    o.append(tx(2, 56, "Input", 6.5, anchor="start"))
    o.append(tx(232, 56, "Output", 6.5, anchor="start"))
    # (b)
    o.append(tx(330, 16, "(b)"))
    o.append(bx(300, 40, 100, 44, "G = G1 x G2"))
    o.append(ar(288, 62, 300, 62))
    o.append(ar(400, 62, 430, 62))
    o.append(tx(282, 56, "Input", 6.5, anchor="start"))
    o.append(tx(412, 56, "Output", 6.5, anchor="start"))
    return _f(o, 450, 90,
              "Hai hệ thống mắc nối tiếp (a) và hệ tương đương có hệ số khuyếch đại bằng tích các hệ số của hai hệ thành phần (b).",
              "Two systems in series (a) and the equivalent system with a gain equal to the product of the gains of the two constituent systems (b).")


# =====================================================================
# Figure 2.4 - Negative feedback
# =====================================================================
def fig_2_4():
    o = []
    o.append(sumj(70, 60, ["", "", "-"]))
    o.append(ar(20, 60, 59, 60))
    o.append(bx(95, 38, 80, 44, "G"))
    o.append(ar(175, 60, 250, 60))
    o.append(tx(14, 55, "Input", 6.5, anchor="start"))
    o.append(tx(244, 55, "Output", 6.5, anchor="start"))
    # feedback
    o.append(ln(215, 60, 215, 92, color=INK))
    o.append(ln(215, 92, 70, 92, color=INK))
    o.append(ar(70, 92, 70, 71))
    o.append(bx(225, 86, 40, 24, "H", size=7))
    o.append(tx(245, 104, "Feedback", 6.5))
    return _f(o, 300, 120,
              "Hệ thống có phản hồi âm: tín hiệu phản hồi trừ khỏi tín hiệu đầu vào.",
              "System with negative feedback: the fed-back signal subtracts from the input.")


# =====================================================================
# Figure 2.5 - Positive feedback
# =====================================================================
def fig_2_5():
    o = []
    o.append(sumj(70, 60, ["", "", "+"]))
    o.append(ar(20, 60, 59, 60))
    o.append(bx(95, 38, 80, 44, "G"))
    o.append(ar(175, 60, 250, 60))
    o.append(tx(14, 55, "Input", 6.5, anchor="start"))
    o.append(tx(244, 55, "Output", 6.5, anchor="start"))
    o.append(ln(215, 60, 215, 92, color=INK))
    o.append(ln(215, 92, 70, 92, color=INK))
    o.append(ar(70, 92, 70, 71))
    o.append(bx(225, 86, 40, 24, "H", size=7))
    o.append(tx(245, 104, "Feedback", 6.5))
    return _f(o, 300, 120,
              "Hệ thống có phản hồi dương: tín hiệu phản hồi cộng vào tín hiệu đầu vào.",
              "System with positive feedback: the fed-back signal adds to the input.")


# =====================================================================
# Figure 2.6 - Feedback amplifier circuit
# =====================================================================
def fig_2_6():
    o = []
    # op amp triangle
    o.append(_poly([(120, 30), (120, 100), (190, 65)], fill="#eef3fb", sw=1.2))
    o.append(tx(150, 90, "Op amp", 7))
    # input + at left
    o.append(ar(50, 65, 118, 65))
    o.append(tx(44, 60, "Input", 6.5, anchor="start"))
    # non-inverting + and inverting - markers
    o.append(tx(112, 50, "+", 9))
    o.append(tx(112, 84, "-", 9))
    # output
    o.append(ar(190, 65, 250, 65))
    o.append(tx(244, 60, "Output", 6.5, anchor="start"))
    # potential divider R1, R2 across output back to inverting input
    o.append(ln(250, 65, 300, 65, color=INK))
    o.append(ln(300, 65, 300, 110, color=INK))
    o.append(bx(280, 110, 40, 22, "R1", size=7))
    o.append(bx(280, 134, 40, 22, "R2", size=7))
    o.append(ln(300, 156, 150, 156, color=INK))
    o.append(ln(150, 156, 150, 84, color=INK))
    o.append(ar(150, 84, 122, 84))
    o.append(tx(160, 170, "Potential divider", 6.5))
    return _f(o, 350, 195,
              "Mạch khuếch đại phản hồi gồm bộ khuếch đại thuật toán với mạng phân áp gồm hai điện trở R1 và R2.",
              "Feedback amplifier circuit: an operational amplifier with a potential divider of two resistors R1 and R2.")


# =====================================================================
# Figure 2.7 - Mechanical building blocks: (a) spring (b) dashpot (c) mass
# =====================================================================
def fig_2_7():
    o = []
    # (a) spring
    o.append(tx(45, 14, "(a)"))
    o.append(tx(45, 30, "Spring", 7))
    pts = [(30, 55)]
    for i in range(5):
        pts.append((30 + (24 if i % 2 == 0 else 0), 60 + i * 8))
    pts.append((54, 100))
    o.append(_poly(pts, color=INK, sw=1.2))
    o.append(ar(14, 55, 30, 55))
    o.append(ar(54, 100, 70, 100))
    o.append(tx(10, 50, "F", 7, anchor="start"))
    o.append(tx(10, 108, "y", 7, anchor="start"))
    # (b) dashpot
    o.append(tx(160, 14, "(b)"))
    o.append(tx(160, 30, "Dashpot", 7))
    o.append(_rect(150, 55, 40, 50, "#eef3fb", sw=1.2))
    o.append(_poly([(160, 30), (160, 55), (180, 55), (180, 30)], color=INK, sw=1, close=True))
    o.append(_line(170, 30, 170, 18, sw=1))
    o.append(ar(140, 18, 170, 18))
    o.append(tx(134, 13, "F", 7, anchor="start"))
    o.append(tx(184, 85, "y", 7))
    # (c) mass
    o.append(tx(290, 14, "(c)"))
    o.append(tx(290, 30, "Mass", 7))
    o.append(_rect(270, 45, 46, 40, "#eef3fb", sw=1.2))
    o.append(tx(293, 67, "m", 8))
    o.append(ar(250, 65, 270, 65))
    o.append(tx(244, 60, "F", 7, anchor="start"))
    return _f(o, 360, 120,
              "Các khối cấu tạo của hệ cơ: (a) lò xo, (b) giảm chấn (dashpot), (c) khối lượng.",
              "Mechanical system building blocks: (a) spring, (b) dashpot, (c) mass.")


# =====================================================================
# Figure 2.8 - (a) mechanical system (b) free-body diagram
# =====================================================================
def fig_2_8():
    o = []
    # (a)
    o.append(tx(80, 14, "(a)"))
    o.append(tx(80, 30, "Mechanical", 7))
    o.append(tx(80, 40, "system", 7))
    o.append(_rect(60, 60, 50, 36, "#eef3fb", sw=1.2))
    o.append(tx(85, 80, "m", 8))
    # spring to left
    pts = [(20, 78)]
    for i in range(4):
        pts.append((20 + (18 if i % 2 == 0 else 0), 80 + i * 6))
    pts.append((60, 96))
    o.append(_poly(pts, color=INK, sw=1))
    o.append(ar(8, 78, 20, 78))
    o.append(tx(2, 73, "F", 7, anchor="start"))
    # dashpot to right
    o.append(_rect(130, 60, 26, 36, "#eef3fb", sw=1.2))
    o.append(_line(143, 60, 143, 44, sw=1))
    o.append(tx(150, 78, "c", 7))
    # (b) free body
    o.append(tx(270, 14, "(b)"))
    o.append(tx(260, 30, "Free-body", 7))
    o.append(tx(260, 40, "diagram", 7))
    o.append(_rect(240, 60, 50, 36, "#eef3fb", sw=1.2))
    o.append(tx(265, 80, "m", 8))
    o.append(ar(220, 80, 240, 80))
    o.append(tx(214, 75, "F", 7, anchor="start"))
    o.append(ar(290, 70, 270, 72, color=RED))
    o.append(tx(292, 64, "ky", 7, color=RED))
    o.append(ar(290, 92, 270, 90, color=RED))
    o.append(tx(292, 96, "c dy/dt", 6.5, color=RED))
    return _f(o, 360, 120,
              "Hệ cơ gồm khối lượng, giảm chấn và độ cứng (a) cùng biểu đồ lực tác dụng lên khối lượng (b).",
              "Mechanical system with mass, damping and stiffness (a) and the free-body diagram of the forces acting on the mass (b).")


# =====================================================================
# Figure 2.9 - Rotational elements: (a) torsional spring (b) dashpot (c) inertia
# =====================================================================
def fig_2_9():
    o = []
    # (a) torsional spring - shaft coil
    o.append(tx(50, 14, "(a)"))
    o.append(tx(45, 28, "Torsional", 6.5))
    o.append(tx(45, 37, "spring", 6.5))
    o.append(_line(20, 70, 30, 70, sw=1.4))
    pts = [(30, 70)]
    for i in range(7):
        pts.append((30 + (22 if i % 2 == 0 else 0), 64 - i * 4))
    pts.append((52, 50))
    o.append(_poly(pts, color=INK, sw=1.1))
    o.append(ar(20, 78, 30, 70))
    o.append(tx(14, 82, "T", 7, anchor="start"))
    # (b) rotational dashpot
    o.append(tx(165, 14, "(b)"))
    o.append(tx(160, 28, "Rotational", 6.5))
    o.append(tx(160, 37, "dashpot", 6.5))
    o.append(_circle(170, 70, 20, fill="#eef3fb"))
    o.append(_line(170, 50, 170, 40, sw=1.2))
    o.append(tx(176, 66, "c", 7))
    # (c) moment of inertia - disk
    o.append(tx(290, 14, "(c)"))
    o.append(tx(280, 28, "Moment of", 6.5))
    o.append(tx(280, 37, "inertia", 6.5))
    o.append(_ellipse(290, 70, 26, 10, fill="#eef3fb"))
    o.append(_line(290, 70, 290, 40, sw=1.2))
    o.append(tx(296, 66, "I", 7))
    return _f(o, 340, 110,
              "Các phần tử quay: (a) lò xo xoắn, (b) giảm chấn quay, (c) mô-men quán tính.",
              "Rotational system elements: (a) torsional spring, (b) rotational dashpot, (c) moment of inertia.")


# =====================================================================
# Figure 2.10 - (a) rotational example (b) free-body diagram
# =====================================================================
def fig_2_10():
    o = []
    # (a) disk twisted by shaft
    o.append(tx(70, 14, "(a)"))
    o.append(tx(60, 30, "Rotation", 7))
    o.append(tx(60, 40, "of disk", 7))
    o.append(_ellipse(70, 70, 28, 11, fill="#eef3fb"))
    o.append(_line(70, 70, 70, 40, sw=1.2))
    o.append(_poly([(20, 78), (20, 62), (40, 62), (40, 78)], color=INK, sw=1, close=True))
    o.append(tx(16, 92, "Shaft", 6.5))
    o.append(tx(40, 60, "T", 7))
    # (b) free body
    o.append(tx(250, 14, "(b)"))
    o.append(tx(240, 30, "Free-body", 7))
    o.append(tx(240, 40, "diagram", 7))
    o.append(_ellipse(250, 70, 28, 11, fill="#eef3fb"))
    o.append(_line(250, 70, 250, 40, sw=1.2))
    o.append(ar(220, 70, 232, 70))
    o.append(tx(214, 65, "T", 7, anchor="start"))
    o.append(ar(280, 62, 262, 66, color=RED))
    o.append(tx(282, 56, "kθ", 6.5, color=RED))
    o.append(ar(280, 80, 262, 76, color=RED))
    o.append(tx(282, 84, "c dθ/dt", 6.5, color=RED))
    return _f(o, 330, 110,
              "Ví dụ hệ quay: (a) sự xoắn đĩa do trục, (b) biểu đồ lực (mô-men) tác dụng lên đĩa.",
              "Example rotational system: (a) rotation of a disk by twisting a shaft, (b) the free-body diagram.")


# =====================================================================
# Figure 2.11 - Electrical building blocks: resistor, inductor, capacitor
# =====================================================================
def fig_2_11():
    o = []
    # resistor
    o.append(tx(40, 14, "Resistor", 7))
    o.append(_poly([(20, 50), (30, 40), (40, 60), (50, 40), (60, 60), (70, 40), (80, 50)], color=INK, sw=1.2))
    o.append(_line(20, 50, 12, 50, sw=1.2))
    o.append(_line(80, 50, 88, 50, sw=1.2))
    o.append(tx(45, 70, "i", 7))
    o.append(tx(45, 82, "v", 7))
    # inductor
    o.append(tx(150, 14, "Inductor", 7))
    pts = [(130, 50)]
    for i in range(4):
        pts.append((130 + 10, 45 - i * 2))
        pts.append((142, 45 - i * 2))
    o.append(_poly(pts + [(170, 50)], color=INK, sw=1.2))
    o.append(_line(130, 50, 120, 50, sw=1.2))
    o.append(tx(140, 70, "i", 7))
    o.append(tx(140, 82, "v", 7))
    # capacitor
    o.append(tx(255, 14, "Capacitor", 7))
    o.append(_line(235, 50, 257, 50, sw=1.4))
    o.append(_line(263, 50, 285, 50, sw=1.4))
    o.append(_line(235, 50, 228, 50, sw=1.2))
    o.append(_line(285, 50, 292, 50, sw=1.2))
    o.append(tx(255, 70, "i", 7))
    o.append(tx(255, 82, "v", 7))
    return _f(o, 320, 100,
              "Các khối cấu tạo của hệ điện: điện trở, cuộn cảm và tụ điện.",
              "Electrical system building blocks: resistor, inductor and capacitor.")


# =====================================================================
# Figure 2.12 - Electrical RC system
# =====================================================================
def fig_2_12():
    o = []
    o.append(tx(20, 20, "v", 8))
    o.append(_line(20, 30, 20, 60, sw=1.2))
    o.append(_line(20, 60, 70, 60, sw=1.2))
    # resistor R
    o.append(_poly([(70, 60), (80, 50), (90, 70), (100, 50), (110, 70), (120, 50), (130, 60)], color=INK, sw=1.2))
    o.append(_line(130, 60, 180, 60, sw=1.2))
    # capacitor C
    o.append(_line(180, 60, 200, 60, sw=1.4))
    o.append(_line(206, 60, 230, 60, sw=1.4))
    o.append(_line(230, 60, 230, 40, sw=1.2))
    o.append(_line(20, 40, 230, 40, sw=1.2))
    o.append(tx(95, 80, "R", 7))
    o.append(tx(203, 80, "C", 7))
    o.append(tx(225, 52, "vc", 7))
    return _f(o, 270, 100,
              "Hệ điện gồm điện trở và tụ điện; đầu ra là điện áp vc trên tụ.",
              "Electrical system with resistance and capacitance; the output is the voltage vc across the capacitor.")


# =====================================================================
# Figure 2.13 - Electrical RLC system
# =====================================================================
def fig_2_13():
    o = []
    o.append(tx(20, 20, "v", 8))
    o.append(_line(20, 30, 20, 60, sw=1.2))
    o.append(_line(20, 60, 70, 60, sw=1.2))
    o.append(_poly([(70, 60), (80, 50), (90, 70), (100, 50), (110, 70), (120, 50), (130, 60)], color=INK, sw=1.2))
    o.append(_line(130, 60, 175, 60, sw=1.2))
    # inductor
    lp = [(175, 60)]
    for i in range(3):
        lp.append((185, 56 - i * 1))
        lp.append((195, 56 - i * 1))
    o.append(_poly(lp + [(205, 60)], color=INK, sw=1.2))
    o.append(_line(205, 60, 250, 60, sw=1.2))
    o.append(_line(250, 60, 270, 60, sw=1.4))
    o.append(_line(276, 60, 300, 60, sw=1.4))
    o.append(_line(300, 60, 300, 40, sw=1.2))
    o.append(_line(20, 40, 300, 40, sw=1.2))
    o.append(tx(98, 80, "R", 7))
    o.append(tx(190, 80, "L", 7))
    o.append(tx(283, 80, "C", 7))
    o.append(tx(295, 52, "vc", 7))
    return _f(o, 340, 100,
              "Hệ điện gồm điện trở, cuộn cảm và tụ điện.",
              "Electrical system with resistance, inductance and capacitance.")


# =====================================================================
# Figure 2.14 - (a) thermal resistance (b) thermal capacitance
# =====================================================================
def fig_2_14():
    o = []
    # (a)
    o.append(tx(80, 14, "(a)"))
    o.append(tx(70, 28, "Thermal", 6.5))
    o.append(tx(70, 37, "resistance", 6.5))
    o.append(_rect(40, 50, 70, 40, "#eef3fb", sw=1.2))
    o.append(tx(75, 72, "wall", 7))
    o.append(ar(20, 70, 40, 70))
    o.append(tx(14, 65, "T1", 7, anchor="start"))
    o.append(ar(110, 70, 130, 70))
    o.append(tx(134, 65, "T2", 7, anchor="start"))
    o.append(tx(75, 100, "q", 7))
    # (b)
    o.append(tx(250, 14, "(b)"))
    o.append(tx(240, 28, "Thermal", 6.5))
    o.append(tx(240, 37, "capacitance", 6.5))
    o.append(_rect(220, 55, 70, 50, "#eef3fb", sw=1.2))
    o.append(tx(255, 82, "mass m", 7))
    o.append(ar(200, 72, 220, 72, color=RED))
    o.append(tx(194, 67, "q1", 6.5, color=RED, anchor="start"))
    o.append(ar(290, 72, 310, 72))
    o.append(tx(314, 67, "q2", 6.5, anchor="start"))
    o.append(tx(255, 120, "T", 7))
    return _f(o, 340, 140,
              "Các khối cấu tạo nhiệt: (a) điện trở nhiệt, (b) điện dung nhiệt.",
              "Thermal building blocks: (a) thermal resistance, (b) thermal capacitance.")


# =====================================================================
# Figure 2.15 - Thermal example: thermometer in liquid
# =====================================================================
def fig_2_15():
    o = []
    o.append(_rect(40, 50, 90, 70, "#eef3fb", sw=1.2))
    o.append(tx(85, 90, "Liquid", 7))
    o.append(tx(85, 100, "TL", 7))
    # thermometer
    o.append(_line(150, 30, 150, 60, sw=2, color=RED))
    o.append(_circle(150, 70, 14, fill="#fdeaea", color=RED))
    o.append(ar(150, 40, 150, 30, color=RED))
    o.append(tx(160, 50, "T", 7))
    o.append(_line(150, 30, 120, 30, color=RED, sw=1, dash=""))
    return _f(o, 220, 140,
              "Nhiệt kế ở nhiệt độ T đo nhiệt độ chất lỏng thay đổi đột ngột lên TL.",
              "A thermometer at temperature T used to measure the temperature of a liquid that suddenly changes to TL.")


# =====================================================================
# Figure 2.16 - Room temperature example
# =====================================================================
def fig_2_16():
    o = []
    o.append(_rect(40, 45, 120, 80, "#eef3fb", sw=1.2))
    o.append(tx(100, 75, "Room", 7))
    o.append(tx(100, 86, "T", 7))
    # heater in
    o.append(ar(15, 60, 40, 60, color=RED))
    o.append(tx(8, 55, "q1", 6.5, color=RED, anchor="start"))
    # heat out
    o.append(ar(160, 100, 185, 100))
    o.append(tx(189, 95, "q2", 6.5, anchor="start"))
    o.append(tx(100, 140, "Heater q1, loss q2", 6.5))
    return _f(o, 220, 155,
              "Mô hình nhiệt phòng: lò sưởi cung cấp nhiệt q1, phòng tỏa nhiệt q2.",
              "Model of a room: a heater supplies heat at rate q1 and the room loses heat at rate q2.")


# =====================================================================
# Figure 2.17 - Hydraulic building blocks (a) resistance (b) capacitance (c) inertance
# =====================================================================
def fig_2_17():
    o = []
    # (a) resistance - two pipe diameters
    o.append(tx(70, 14, "(a)"))
    o.append(tx(55, 28, "Resistance", 6.5))
    o.append(_poly([(30, 45), (50, 45), (40, 60), (60, 60), (50, 75), (70, 75)], color=INK, sw=1.1))
    o.append(_line(20, 45, 30, 45, sw=1.2))
    o.append(_line(70, 75, 90, 75, sw=1.2))
    o.append(tx(45, 92, "p1   p2", 6.5))
    # (b) capacitance - tank
    o.append(tx(190, 14, "(b)"))
    o.append(tx(185, 28, "Capacitance", 6.5))
    o.append(_poly([(160, 50), (160, 95), (210, 95), (210, 50)], color=INK, sw=1.2))
    o.append(_line(160, 70, 210, 70, color=BLUE, sw=1))
    o.append(ar(140, 50, 160, 50))
    o.append(tx(134, 45, "q1", 6.5, anchor="start"))
    o.append(ar(210, 75, 230, 75))
    o.append(tx(234, 70, "q2", 6.5, anchor="start"))
    # (c) inertance - accelerating fluid
    o.append(tx(310, 14, "(c)"))
    o.append(tx(300, 28, "Inertance", 6.5))
    o.append(_poly([(290, 95), (290, 50), (340, 50), (340, 95)], color=INK, sw=1.2))
    o.append(ar(265, 72, 290, 72, color=BLUE))
    o.append(tx(258, 67, "p1", 6.5, anchor="start"))
    o.append(ar(340, 72, 365, 72, color=BLUE))
    o.append(tx(350, 67, "p2", 6.5, anchor="start"))
    return _f(o, 400, 115,
              "Các khối cấu tạo thủy lực: (a) điện trở, (b) điện dung, (c) quán tính (inertance).",
              "Hydraulic building blocks: (a) resistance, (b) capacitance, (c) inertance.")


# =====================================================================
# Figure 2.18 - Hydraulic example: container with valve
# =====================================================================
def fig_2_18():
    o = []
    o.append(_poly([(60, 50), (60, 110), (150, 110), (150, 50)], color=INK, sw=1.2))
    o.append(_line(60, 80, 150, 80, color=BLUE, sw=1))
    o.append(ar(35, 65, 60, 65, color=BLUE))
    o.append(tx(28, 60, "q1", 6.5, color=BLUE, anchor="start"))
    # valve
    o.append(_rect(150, 72, 22, 18, "#eef3fb", sw=1.1))
    o.append(tx(161, 120, "Valve", 6.5))
    o.append(ar(172, 81, 200, 81, color=BLUE))
    o.append(tx(204, 76, "q2", 6.5, color=BLUE, anchor="start"))
    o.append(tx(105, 130, "Cross-section A, height h", 6.5))
    return _f(o, 240, 145,
              "Hệ thủy lực: chất lỏng vào bồn với lưu lượng q1 và ra qua van với lưu lượng q2.",
              "Hydraulic system: liquid enters a container at rate q1 and leaves through a valve at rate q2.")


# =====================================================================
# Figure 2.19 - First-order step response
# =====================================================================
def fig_2_19():
    o = []
    x0, y0, W, H = 45, 30, 300, 150
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: 1 - math.exp(-t), x0, y0, W, H, xr=(0, 4), yr=(0, 1.1), color=BLUE, sw=1.4))
    marks = [(1, 0.632, "0.63k"), (2, 0.865, "0.86k"), (3, 0.95, "0.95k"), (4, 0.982, "0.98k")]
    for t, y, lab in marks:
        px = x0 + t / 4.0 * W
        py = y0 + H - y / 1.1 * H
        o.append(_circle(px, py, 2.4, fill=RED))
        o.append(_line(px, py, px, y0 + H, color=GREY, sw=0.6, dash="2 3"))
        o.append(_txt(px - 4, py - 6, lab, 6.5, anchor="end", color=RED))
    o.append(_txt(x0 + W, y0 - 14, "1k", 6.8, anchor="end", color=GREY))
    return _f(o, 400, 200,
              "Đáp ứng của hệ bậc nhất với đầu vào bậc đơn vị: sau 1τ đạt 0,63k, 2τ đạt 0,86k, 3τ đạt 0,95k, 4τ đạt 0,98k.",
              "Behaviour of a first-order system subject to a unit step input: after 1τ it reaches 0.63k, 2τ 0.86k, 3τ 0.95k, 4τ 0.98k.")


# =====================================================================
# Figure 2.20 - Second-order step response for various damping ratios
# =====================================================================
def _y2(t, zeta):
    if zeta == 0:
        return 1 - math.cos(t)
    if zeta >= 1:
        if zeta == 1:
            return 1 - math.exp(-t) * (1 + t)
        sd = math.sqrt(zeta * zeta - 1)
        return 1 - math.exp(-zeta * t) * (math.cosh(sd * t) + zeta / sd * math.sinh(sd * t))
    wd = math.sqrt(1 - zeta * zeta)
    return 1 - math.exp(-zeta * t) * (math.cos(wd * t) + zeta / wd * math.sin(wd * t))


def fig_2_20():
    o = []
    x0, y0, W, H = 45, 30, 310, 160
    o.append(_axes(x0, y0, W, H, "Time x natural angular frequency", "Output"))
    for z in [0.0, 0.25, 0.5, 1.0, 2.0]:
        o.append(_curve(lambda t, z=z: _y2(t, z), x0, y0, W, H, xr=(0, 10), yr=(-0.1, 2.0), color=BLUE, sw=1.1))
    o.append(_txt(x0 + 6, y0 + 12, "ζ = 0 (undamped)", 6.5, anchor="start", color=INK))
    o.append(_txt(x0 + 6, y0 + 26, "ζ = 1 (critical)", 6.5, anchor="start", color=INK))
    o.append(_txt(x0 + 6, y0 + 40, "ζ > 1 (overdamped)", 6.5, anchor="start", color=INK))
    return _f(o, 400, 210,
              "Đáp ứng bậc hai với các tỷ số giảm chấn khác nhau: không giảm chấn, giảm chấn nhỏ, tới hạn và quá giảm chấn.",
              "Behaviour of a second-order system for different damping ratios: undamped, underdamped, critically damped and overdamped.")


# =====================================================================
# Figure 2.21 - Transfer function as a block
# =====================================================================
def fig_2_21():
    o = []
    o.append(bx(120, 40, 130, 50, "G(s)"))
    o.append(ar(30, 65, 120, 65))
    o.append(ar(250, 65, 360, 65))
    o.append(tx(20, 60, "X(s)", 7.5, anchor="start"))
    o.append(tx(300, 60, "Y(s)", 7.5, anchor="start"))
    o.append(tx(180, 105, "Transfer function multiplies input to give output", 6.5))
    return _f(o, 380, 130,
              "Hàm truyền G(s) được biểu diễn như một khối: đầu vào X(s), đầu ra Y(s), toán tử G(s) trong khối.",
              "The transfer function as the factor that multiplies the input to give the output.")


# =====================================================================
# Figure 2.22 - Speed-control block diagram
# =====================================================================
def fig_2_22():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "Input", 6.5, anchor="start"))
    o.append(bx(90, 38, 80, 44, "Amplifier\nK"))
    o.append(bx(200, 38, 90, 44, "Motor\n1/(sL+R)"))
    o.append(bx(330, 38, 80, 44, "Gears\nN"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(170, 60, 200, 60))
    o.append(ar(290, 60, 330, 60))
    o.append(ar(410, 60, 460, 60))
    o.append(tx(420, 54, "Output", 6.5, anchor="start"))
    # feedback
    o.append(ln(370, 60, 370, 95, color=INK))
    o.append(ln(370, 95, 60, 95, color=INK))
    o.append(ar(60, 95, 60, 71))
    o.append(bx(250, 95, 90, 24, "Tachogenerator H", size=6.5))
    return _f(o, 500, 130,
              "Sơ đồ khối hệ điều khiển tốc độ trục: bộ khuếch đại K, động cơ 1/(sL+R), bộ truyền N, phản hồi qua tachogenerator H.",
              "Block diagram for the speed-control system: amplifier K, motor 1/(sL+R), gears N, with feedback via a tachogenerator H.")


# =====================================================================
# Figure 2.23 - Systems in series
# =====================================================================
def fig_2_23():
    o = []
    o.append(bx(40, 40, 90, 44, "G1(s)"))
    o.append(bx(190, 40, 90, 44, "G2(s)"))
    o.append(ar(20, 62, 40, 62))
    o.append(ar(130, 62, 190, 62))
    o.append(ar(280, 62, 330, 62))
    o.append(tx(10, 56, "X(s)", 7, anchor="start"))
    o.append(tx(150, 50, "Y1(s)", 7))
    o.append(tx(285, 56, "Y(s)", 7, anchor="start"))
    return _f(o, 350, 90,
              "Hai hệ mắc nối tiếp: đầu ra tổng cộng là tích các hàm truyền G1(s)·G2(s).",
              "Systems in series: the overall transfer function is the product G1(s)·G2(s).")


# =====================================================================
# Figure 2.24 - Negative feedback block
# =====================================================================
def fig_2_24():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(bx(90, 38, 90, 44, "G(s)"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(180, 60, 260, 60))
    o.append(tx(195, 54, "Y(s)", 7, anchor="start"))
    o.append(ln(225, 60, 225, 92, color=INK))
    o.append(ln(225, 92, 60, 92, color=INK))
    o.append(ar(60, 92, 60, 71))
    o.append(bx(180, 92, 90, 24, "H(s)", size=7))
    return _f(o, 290, 130,
              "Hệ có phản hồi âm: hàm truyền tổng cộng G(s)/[1+G(s)H(s)].",
              "System with negative feedback: overall transfer function G(s)/[1+G(s)H(s)].")


# =====================================================================
# Figure 2.25 - Positive feedback block
# =====================================================================
def fig_2_25():
    o = []
    o.append(sumj(60, 60, ["", "", "+"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(bx(90, 38, 90, 44, "G(s)"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(180, 60, 260, 60))
    o.append(tx(195, 54, "Y(s)", 7, anchor="start"))
    o.append(ln(225, 60, 225, 92, color=INK))
    o.append(ln(225, 92, 60, 92, color=INK))
    o.append(ar(60, 92, 60, 71))
    o.append(bx(180, 92, 90, 24, "H(s)", size=7))
    return _f(o, 290, 130,
              "Hệ có phản hồi dương: hàm truyền tổng cộng G(s)/[1−G(s)H(s)].",
              "System with positive feedback: overall transfer function G(s)/[1−G(s)H(s)].")


# =====================================================================
# Figure 2.26 - Example negative feedback
# =====================================================================
def fig_2_26():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(bx(90, 38, 110, 44, "2/(s+2)"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(200, 60, 270, 60))
    o.append(tx(210, 54, "Y(s)", 7, anchor="start"))
    o.append(ln(255, 60, 255, 92, color=INK))
    o.append(ln(255, 92, 60, 92, color=INK))
    o.append(ar(60, 92, 60, 71))
    o.append(bx(195, 92, 60, 24, "H = 4", size=7))
    return _f(o, 300, 130,
              "Ví dụ phản hồi âm: đường thẳng G(s)=2/(s+2), phản hồi H=4.",
              "Example negative-feedback system with forward path 2/(s+2) and feedback H = 4.")


# =====================================================================
# Figure 2.27 - Example positive feedback
# =====================================================================
def fig_2_27():
    o = []
    o.append(sumj(60, 60, ["", "", "+"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(bx(90, 38, 110, 44, "2/(s+2)"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(200, 60, 270, 60))
    o.append(tx(210, 54, "Y(s)", 7, anchor="start"))
    o.append(ln(255, 60, 255, 92, color=INK))
    o.append(ln(255, 92, 60, 92, color=INK))
    o.append(ar(60, 92, 60, 71))
    o.append(bx(195, 92, 60, 24, "H = 4", size=7))
    return _f(o, 300, 130,
              "Ví dụ phản hồi dương: đường thẳng G(s)=2/(s+2), phản hồi H=4.",
              "Example positive-feedback system with forward path 2/(s+2) and feedback H = 4.")


# =====================================================================
# Figure 2.28 - System with negative feedback (sensitivity)
# =====================================================================
def fig_2_28():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(bx(90, 38, 90, 44, "G(s)"))
    o.append(ar(49, 60, 90, 60))
    o.append(ar(180, 60, 260, 60))
    o.append(tx(195, 54, "Y(s)", 7, anchor="start"))
    o.append(ln(225, 60, 225, 92, color=INK))
    o.append(ln(225, 92, 60, 92, color=INK))
    o.append(ar(60, 92, 60, 71))
    o.append(bx(180, 92, 90, 24, "H(s)", size=7))
    return _f(o, 290, 130,
              "Hệ kín có phản hồi âm dùng để phân tích độ nhạy với thay đổi tham số.",
              "Closed-loop system with negative feedback, used to analyse sensitivity to parameter changes.")


# =====================================================================
# Figure 2.29 - Disturbance with open-loop system
# =====================================================================
def fig_2_29():
    o = []
    o.append(bx(60, 38, 90, 44, "G1(s)"))
    o.append(sumj(190, 60, ["", "", "+"]))
    o.append(bx(250, 38, 90, 44, "G2(s)"))
    o.append(ar(20, 60, 60, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(ar(150, 60, 190, 60))
    o.append(ar(280, 60, 360, 60))
    o.append(tx(290, 54, "Y(s)", 7, anchor="start"))
    o.append(ar(190, 20, 190, 49))
    o.append(tx(196, 14, "D(s)", 7, anchor="start"))
    return _f(o, 390, 110,
              "Nhiễu với hệ vòng hở: nhiễu D(s) được cộng vào giữa hai khối G1 và G2.",
              "Disturbance with an open-loop system: the disturbance D(s) is added between two elements G1 and G2.")


# =====================================================================
# Figure 2.30 - Disturbance with closed-loop system
# =====================================================================
def fig_2_30():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(bx(100, 38, 90, 44, "G1(s)"))
    o.append(sumj(230, 60, ["", "", "+"]))
    o.append(bx(290, 38, 90, 44, "G2(s)"))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 7, anchor="start"))
    o.append(ar(49, 60, 100, 60))
    o.append(ar(190, 60, 230, 60))
    o.append(ar(320, 60, 400, 60))
    o.append(tx(330, 54, "Y(s)", 7, anchor="start"))
    o.append(ar(230, 20, 230, 49))
    o.append(tx(236, 14, "D(s)", 7, anchor="start"))
    o.append(ln(335, 60, 335, 95, color=INK))
    o.append(ln(335, 95, 60, 95, color=INK))
    o.append(ar(60, 95, 60, 71))
    o.append(bx(270, 95, 60, 24, "H(s)", size=7))
    return _f(o, 430, 120,
              "Nhiễu với hệ vòng kín: tác động nhiễu được giảm bởi hệ số [1+G1G2H].",
              "Disturbance with a closed-loop system: the effect of the disturbance is reduced by the factor [1+G1G2H].")


# =====================================================================
# Figure 2.31 - Blocks in series equivalence
# =====================================================================
def fig_2_31():
    o = []
    o.append(tx(60, 16, "X", 7))
    o.append(bx(40, 35, 70, 40, "G1"))
    o.append(bx(150, 35, 70, 40, "G2"))
    o.append(ar(20, 55, 40, 55))
    o.append(ar(110, 55, 150, 55))
    o.append(ar(220, 55, 260, 55))
    o.append(tx(244, 50, "Y", 7))
    o.append(tx(135, 80, "Equivalent to", 6.5))
    o.append(tx(330, 16, "X", 7))
    o.append(bx(310, 35, 90, 40, "G1 G2"))
    o.append(ar(290, 55, 310, 55))
    o.append(ar(400, 55, 440, 55))
    o.append(tx(424, 50, "Y", 7))
    return _f(o, 460, 100,
              "Rút gọn khối nối tiếp: X → G1 → G2 → Y tương đương X → G1G2 → Y.",
              "Blocks in series: X → G1 → G2 → Y is equivalent to X → G1G2 → Y.")


# =====================================================================
# Figure 2.32 - Moving a take-off point beyond a block
# =====================================================================
def fig_2_32():
    o = []
    o.append(tx(60, 16, "y", 7))
    o.append(bx(40, 35, 80, 40, "G"))
    o.append(ar(20, 55, 40, 55))
    o.append(ar(120, 55, 170, 55))
    o.append(tap(40, 55))
    o.append(tx(150, 50, "y", 7))
    o.append(tx(110, 75, "Equivalent to", 6.5))
    o.append(tx(330, 16, "y", 7))
    o.append(bx(300, 35, 80, 40, "G"))
    o.append(ar(280, 55, 300, 55))
    o.append(ar(380, 55, 430, 55))
    o.append(tap(380, 55))
    o.append(bx(390, 70, 50, 24, "1/G", size=7))
    return _f(o, 450, 110,
              "Chuyển điểm lấy tín hiệu ra sau khối: thêm khối 1/G trên nhánh lấy tín hiệu.",
              "Moving a take-off point to beyond a block: insert a 1/G block on the take-off branch.")


# =====================================================================
# Figure 2.33 - Moving a take-off point ahead of a block
# =====================================================================
def fig_2_33():
    o = []
    o.append(tx(60, 16, "y", 7))
    o.append(bx(40, 35, 80, 40, "G"))
    o.append(ar(20, 55, 40, 55))
    o.append(ar(120, 55, 170, 55))
    o.append(tap(120, 55))
    o.append(tx(150, 50, "y", 7))
    o.append(tx(110, 75, "Equivalent to", 6.5))
    o.append(tx(330, 16, "y", 7))
    o.append(bx(300, 35, 80, 40, "G"))
    o.append(ar(280, 55, 300, 55))
    o.append(ar(380, 55, 430, 55))
    o.append(tap(300, 55))
    o.append(bx(255, 70, 50, 24, "G", size=7))
    return _f(o, 450, 110,
              "Chuyển điểm lấy tín hiệu ra trước khối: thêm khối G trên nhánh lấy tín hiệu.",
              "Moving a take-off point to ahead of a block: insert a G block on the take-off branch.")


# =====================================================================
# Figure 2.34 - Rearrangement of summing points
# =====================================================================
def fig_2_34():
    o = []
    o.append(sumj(70, 55, ["", "", "+", "+"]))
    o.append(ar(20, 55, 59, 55))
    o.append(tx(14, 50, "x1", 7, anchor="start"))
    o.append(ar(81, 40, 95, 40))
    o.append(tx(84, 34, "x2", 7))
    o.append(ar(81, 70, 95, 70))
    o.append(tx(84, 78, "x3", 7))
    o.append(ar(95, 55, 160, 55))
    o.append(tx(150, 50, "y", 7))
    o.append(tx(95, 95, "Equivalent to", 6.5))
    o.append(sumj(280, 40, ["", "", "+"]))
    o.append(sumj(280, 70, ["", "", "+"]))
    o.append(ar(230, 40, 269, 40))
    o.append(tx(224, 35, "x1", 7))
    o.append(ar(291, 40, 330, 40))
    o.append(tx(300, 34, "x2", 7))
    o.append(ar(230, 70, 269, 70))
    o.append(tx(224, 76, "x3", 7))
    o.append(ar(291, 70, 330, 70))
    o.append(ar(330, 40, 330, 58, color=INK))
    o.append(ar(330, 58, 330, 70))
    o.append(ar(330, 55, 380, 55))
    o.append(tx(370, 50, "y", 7))
    return _f(o, 400, 120,
              "Sắp xếp lại các điểm cộng: tách một điểm cộng thành hai điểm cộng nối tiếp.",
              "Rearrangement of summing points: a single summing point split into two in series.")


# =====================================================================
# Figure 2.35 - Interchange of summing points
# =====================================================================
def fig_2_35():
    o = []
    o.append(sumj(70, 55, ["", "", "+"]))
    o.append(ar(20, 55, 59, 55))
    o.append(tx(14, 50, "x1", 7, anchor="start"))
    o.append(ar(81, 40, 95, 40))
    o.append(tx(84, 34, "x2", 7))
    o.append(ar(95, 55, 150, 55))
    o.append(tx(140, 50, "y", 7))
    o.append(tx(95, 90, "Equivalent to", 6.5))
    o.append(sumj(290, 55, ["", "", "+"]))
    o.append(ar(240, 55, 279, 55))
    o.append(tx(234, 50, "x2", 7))
    o.append(ar(301, 40, 315, 40))
    o.append(tx(304, 34, "x1", 7))
    o.append(ar(315, 55, 370, 55))
    o.append(tx(360, 50, "y", 7))
    return _f(o, 390, 120,
              "Hoán đổi hai điểm cộng nối tiếp: thứ tự cộng không làm thay đổi tổng.",
              "Interchange of summing points: the order of summation does not change the result.")


# =====================================================================
# Figure 2.36 - Moving a summing point ahead of a block
# =====================================================================
def fig_2_36():
    o = []
    o.append(tx(70, 14, "Before", 6.5))
    o.append(sumj(60, 55, ["", "", "+"]))
    o.append(bx(120, 33, 70, 44, "G"))
    o.append(ar(20, 55, 49, 55))
    o.append(tx(14, 50, "x1", 7, anchor="start"))
    o.append(ar(71, 40, 85, 40))
    o.append(tx(74, 34, "x2", 7))
    o.append(ar(85, 55, 120, 55))
    o.append(ar(190, 55, 240, 55))
    o.append(tx(220, 50, "y", 7))
    o.append(tx(155, 85, "Equivalent to", 6.5))
    o.append(tx(330, 14, "After", 6.5))
    o.append(bx(300, 33, 70, 44, "G"))
    o.append(sumj(400, 55, ["", "", "+"]))
    o.append(ar(260, 55, 300, 55))
    o.append(ar(370, 55, 400, 55))
    o.append(ar(411, 40, 440, 40))
    o.append(tx(414, 34, "x2", 7))
    o.append(bx(420, 70, 40, 24, "1/G", size=7))
    o.append(ar(440, 40, 440, 49))
    o.append(ln(440, 49, 411, 49, color=INK))
    o.append(ar(400, 55, 470, 55))
    o.append(tx(450, 50, "y", 7))
    return _f(o, 490, 110,
              "Chuyển điểm cộng ra trước khối: thêm khối 1/G trên nhánh đưa x2 vào.",
              "Moving a summing point ahead of a block: insert a 1/G block on the branch carrying x2.")


# =====================================================================
# Figure 2.37 - Moving a summing point beyond a block
# =====================================================================
def fig_2_37():
    o = []
    o.append(tx(70, 14, "Before", 6.5))
    o.append(bx(40, 33, 70, 44, "G"))
    o.append(sumj(150, 55, ["", "", "+"]))
    o.append(ar(20, 55, 40, 55))
    o.append(tx(14, 50, "x1", 7, anchor="start"))
    o.append(ar(110, 55, 150, 55))
    o.append(ar(161, 40, 175, 40))
    o.append(tx(164, 34, "x2", 7))
    o.append(ar(175, 55, 240, 55))
    o.append(tx(220, 50, "y", 7))
    o.append(tx(155, 85, "Equivalent to", 6.5))
    o.append(tx(340, 14, "After", 6.5))
    o.append(sumj(300, 55, ["", "", "+"]))
    o.append(bx(360, 33, 70, 44, "G"))
    o.append(ar(260, 55, 300, 55))
    o.append(tx(254, 50, "x1", 7, anchor="start"))
    o.append(ar(311, 40, 340, 40))
    o.append(tx(314, 34, "x2", 7))
    o.append(bx(320, 70, 40, 24, "G", size=7))
    o.append(ar(340, 40, 340, 49))
    o.append(ln(340, 49, 311, 49, color=INK))
    o.append(ar(300, 55, 360, 55))
    o.append(ar(430, 55, 480, 55))
    o.append(tx(460, 50, "y", 7))
    return _f(o, 500, 110,
              "Chuyển điểm cộng ra sau khối: thêm khối G trên nhánh đưa x2 vào.",
              "Moving a summing point beyond a block: insert a G block on the branch carrying x2.")


# =====================================================================
# Figure 2.38 - Removing a block from a feedback path
# =====================================================================
def fig_2_38():
    o = []
    o.append(tx(90, 14, "Before", 6.5))
    o.append(bx(60, 33, 80, 44, "G"))
    o.append(ar(20, 55, 60, 55))
    o.append(ar(140, 55, 210, 55))
    o.append(tx(180, 50, "y", 7))
    o.append(ln(180, 55, 180, 80, color=INK))
    o.append(ln(180, 80, 100, 80, color=INK))
    o.append(ar(100, 80, 100, 55))
    o.append(bx(120, 80, 40, 22, "H", size=7))
    o.append(tx(155, 95, "Equivalent to", 6.5))
    o.append(tx(330, 14, "After", 6.5))
    o.append(bx(310, 33, 110, 44, "G/(1+GH)"))
    o.append(ar(270, 55, 310, 55))
    o.append(ar(420, 55, 490, 55))
    o.append(tx(460, 50, "y", 7))
    return _f(o, 510, 125,
              "Loại bỏ khối khỏi đường phản hồi: hệ tương đương có hàm truyền G/(1+GH).",
              "Removing a block from a feedback path: the equivalent system has transfer function G/(1+GH).")


# =====================================================================
# Figure 2.39 - Removing a block from a forward path
# =====================================================================
def fig_2_39():
    o = []
    o.append(tx(90, 14, "Before", 6.5))
    o.append(bx(60, 33, 80, 44, "G"))
    o.append(ar(20, 55, 60, 55))
    o.append(ar(140, 55, 210, 55))
    o.append(tx(180, 50, "y", 7))
    o.append(ln(180, 55, 180, 80, color=INK))
    o.append(ln(180, 80, 100, 80, color=INK))
    o.append(ar(100, 80, 100, 55))
    o.append(bx(120, 80, 40, 22, "H", size=7))
    o.append(ln(140, 91, 140, 105, color=INK))
    o.append(ln(140, 105, 60, 105, color=INK))
    o.append(ar(60, 105, 60, 79))
    o.append(tx(155, 120, "Equivalent to", 6.5))
    o.append(tx(330, 14, "After", 6.5))
    o.append(bx(310, 33, 110, 44, "G/(1+GH)"))
    o.append(ar(270, 55, 310, 55))
    o.append(ar(420, 55, 490, 55))
    o.append(tx(460, 50, "y", 7))
    return _f(o, 510, 135,
              "Loại bỏ khối khỏi đường thẳng: hệ tương đương có hàm truyền G/(1+GH).",
              "Removing a block from a forward path: the equivalent system has transfer function G/(1+GH).")


# =====================================================================
# Figure 2.40 - The circuit to be simplified
# =====================================================================
def fig_2_40():
    o = []
    o.append(sumj(50, 60, ["", "", "-"]))
    o.append(bx(100, 38, 80, 44, "G1"))
    o.append(sumj(230, 60, ["", "", "-"]))
    o.append(bx(280, 38, 80, 44, "G2"))
    o.append(ar(20, 60, 39, 60))
    o.append(tx(14, 54, "X(s)", 6.5, anchor="start"))
    o.append(ar(39, 60, 100, 60))
    o.append(ar(180, 60, 230, 60))
    o.append(ar(360, 60, 430, 60))
    o.append(tx(395, 54, "Y(s)", 6.5, anchor="start"))
    # feedforward 1
    o.append(ar(140, 38, 140, 20, color=INK))
    o.append(ar(140, 20, 230, 20, color=INK))
    o.append(ar(230, 20, 230, 49))
    o.append(tx(146, 14, "1", 7))
    # inner feedback G3
    o.append(ln(320, 60, 320, 95, color=INK))
    o.append(ln(320, 95, 230, 95, color=INK))
    o.append(ar(230, 95, 230, 71))
    o.append(bx(270, 95, 40, 22, "G3", size=7))
    # outer feedback H
    o.append(ln(395, 60, 395, 120, color=INK))
    o.append(ln(395, 120, 50, 120, color=INK))
    o.append(ar(50, 120, 50, 71))
    o.append(bx(310, 120, 40, 22, "H", size=7))
    return _f(o, 450, 150,
              "Mạng khối cần rút gọn: G1, G2 nối tiếp, vòng phản hồi trong G3 và vòng ngoài H.",
              "The circuit to be simplified: G1 and G2 in series with an inner feedback loop G3 and an outer loop H.")


# =====================================================================
# Figure 2.41 - Stage 1: moving a take-off point
# =====================================================================
def fig_2_41():
    o = []
    o.append(bx(60, 38, 80, 44, "G1"))
    o.append(sumj(200, 60, ["", "", "-"]))
    o.append(bx(250, 38, 80, 44, "G2"))
    o.append(ar(20, 60, 60, 60))
    o.append(ar(140, 60, 200, 60))
    o.append(ar(280, 60, 360, 60))
    o.append(tx(320, 54, "Y(s)", 6.5, anchor="start"))
    o.append(tap(140, 60))
    o.append(ar(140, 60, 140, 95, color=INK))
    o.append(ln(140, 95, 200, 95, color=INK))
    o.append(ar(200, 95, 200, 71))
    o.append(bx(160, 95, 40, 22, "G3", size=7))
    o.append(ln(320, 60, 320, 110, color=INK))
    o.append(ln(320, 110, 20, 110, color=INK))
    o.append(ar(20, 110, 20, 71))
    o.append(bx(250, 110, 40, 22, "H", size=7))
    return _f(o, 400, 140,
              "Bước 1: chuyển điểm lấy tín hiệu để tách riêng vòng phản hồi trong.",
              "Stage 1: moving the take-off point to expose the inner feedback loop clearly.")


# =====================================================================
# Figure 2.42 - Stage 2: eliminating a feedforward loop
# =====================================================================
def fig_2_42():
    o = []
    o.append(bx(60, 38, 80, 44, "G1"))
    o.append(sumj(200, 60, ["", "", "+"]))
    o.append(bx(250, 38, 80, 44, "G2"))
    o.append(ar(20, 60, 60, 60))
    o.append(ar(140, 60, 200, 60))
    o.append(ar(280, 60, 360, 60))
    o.append(tx(320, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ar(140, 60, 140, 30, color=INK))
    o.append(ar(140, 30, 200, 30, color=INK))
    o.append(ar(200, 30, 200, 49))
    o.append(tx(146, 24, "1", 7))
    o.append(ln(320, 60, 320, 95, color=INK))
    o.append(ln(320, 95, 200, 95, color=INK))
    o.append(ar(200, 95, 200, 71))
    o.append(bx(260, 95, 50, 22, "1+1/G2", size=6.5))
    o.append(ln(320, 60, 320, 110, color=INK))
    o.append(ln(320, 110, 20, 110, color=INK))
    o.append(ar(20, 110, 20, 71))
    o.append(bx(250, 110, 40, 22, "H", size=7))
    return _f(o, 400, 140,
              "Bước 2: khử vòng feedforward, gộp nhánh 1 vào tổng thành 1+1/G2.",
              "Stage 2: eliminating the feedforward loop, combining the unity path into 1+1/G2.")


# =====================================================================
# Figure 2.43 - Stage 3: simplifying series elements
# =====================================================================
def fig_2_43():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(bx(120, 38, 110, 44, "G1 G2"))
    o.append(ar(20, 60, 49, 60))
    o.append(ar(49, 60, 120, 60))
    o.append(ar(230, 60, 320, 60))
    o.append(tx(280, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ln(275, 60, 275, 95, color=INK))
    o.append(ln(275, 95, 60, 95, color=INK))
    o.append(ar(60, 95, 60, 71))
    o.append(bx(215, 95, 60, 22, "1+1/G2", size=6.5))
    o.append(ln(275, 60, 275, 110, color=INK))
    o.append(ln(275, 110, 20, 110, color=INK))
    o.append(ar(20, 110, 20, 71))
    o.append(bx(215, 110, 40, 22, "H", size=7))
    return _f(o, 360, 140,
              "Bước 3: gộp hai khối nối tiếp G1 và G2 thành G1G2.",
              "Stage 3: simplifying the series elements G1 and G2 into G1G2.")


# =====================================================================
# Figure 2.44 - Stage 4: simplifying a feedback element
# =====================================================================
def fig_2_44():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(bx(120, 38, 110, 44, "G1 G2"))
    o.append(ar(20, 60, 49, 60))
    o.append(ar(49, 60, 120, 60))
    o.append(ar(230, 60, 320, 60))
    o.append(tx(280, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ln(275, 60, 275, 95, color=INK))
    o.append(ln(275, 95, 60, 95, color=INK))
    o.append(ar(60, 95, 60, 71))
    o.append(bx(200, 95, 70, 22, "1+G1G2G3", size=6.5))
    o.append(ln(275, 60, 275, 110, color=INK))
    o.append(ln(275, 110, 20, 110, color=INK))
    o.append(ar(20, 110, 20, 71))
    o.append(bx(200, 110, 40, 22, "H", size=7))
    return _f(o, 360, 140,
              "Bước 4: rút gọn vòng phản hồi trong thành một khối 1+G1G2G3.",
              "Stage 4: simplifying the inner feedback element into 1+G1G2G3.")


# =====================================================================
# Figure 2.45 - Stage 5: simplifying series elements again
# =====================================================================
def fig_2_45():
    o = []
    o.append(sumj(60, 60, ["", "", "-"]))
    o.append(bx(130, 38, 130, 44, "G1G2(1+1/G2)"))
    o.append(ar(20, 60, 49, 60))
    o.append(ar(49, 60, 130, 60))
    o.append(ar(260, 60, 350, 60))
    o.append(tx(310, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ln(300, 60, 300, 95, color=INK))
    o.append(ln(300, 95, 60, 95, color=INK))
    o.append(ar(60, 95, 60, 71))
    o.append(bx(220, 95, 70, 22, "1+G1G2G3", size=6.5))
    o.append(ln(300, 60, 300, 110, color=INK))
    o.append(ln(300, 110, 20, 110, color=INK))
    o.append(ar(20, 110, 20, 71))
    o.append(bx(220, 110, 40, 22, "H", size=7))
    return _f(o, 390, 140,
              "Bước 5: gộp khối thẳng và nhánh đưa vào thành G1G2(1+1/G2).",
              "Stage 5: simplifying the series elements into G1G2(1+1/G2).")


# =====================================================================
# Figure 2.46 - Stage 6: final negative feedback reduction
# =====================================================================
def fig_2_46():
    o = []
    o.append(bx(120, 38, 170, 44, "G1(G1+1)"))
    o.append(ar(20, 60, 120, 60))
    o.append(ar(290, 60, 380, 60))
    o.append(tx(340, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ln(330, 60, 330, 95, color=INK))
    o.append(ln(330, 95, 120, 95, color=INK))
    o.append(ar(120, 95, 120, 60))
    o.append(bx(190, 95, 100, 22, "1+G1G2G3+G1(G1+1)", size=6))
    return _f(o, 410, 130,
              "Bước 6: rút gọn phản hồi âm cuối cùng thành G1(G1+1)/[1+G1G2G3+G1(G1+1)].",
              "Stage 6: final negative-feedback reduction to G1(G1+1)/[1+G1G2G3+G1(G1+1)].")


# =====================================================================
# Figure 2.47 - System with a disturbance input
# =====================================================================
def fig_2_47():
    o = []
    o.append(sumj(60, 60, ["", "", "+"]))
    o.append(bx(120, 38, 90, 44, "2/s"))
    o.append(sumj(260, 60, ["", "", "+"]))
    o.append(bx(310, 38, 90, 44, "1/(s+1)"))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 6.5, anchor="start"))
    o.append(ar(49, 60, 120, 60))
    o.append(ar(210, 60, 260, 60))
    o.append(ar(400, 60, 460, 60))
    o.append(tx(415, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ar(260, 20, 260, 49))
    o.append(tx(266, 14, "D(s)", 6.5, anchor="start"))
    o.append(ln(400, 60, 400, 95, color=INK))
    o.append(ln(400, 95, 260, 95, color=INK))
    o.append(ar(260, 95, 260, 71))
    o.append(bx(320, 95, 60, 22, "-(s+1)", size=6.5))
    o.append(ln(400, 60, 400, 115, color=INK))
    o.append(ln(400, 115, 60, 115, color=INK))
    o.append(ar(60, 115, 60, 71))
    o.append(bx(310, 115, 60, 22, "s+3", size=7))
    return _f(o, 480, 145,
              "Hệ có hai đầu vào X(s) và nhiễu D(s); dùng nguyên lý xếp chồng để tính Y(s).",
              "System with a disturbance input D(s) as well as X(s); use superposition to find Y(s).")


# =====================================================================
# Figure 2.48 - System with disturbance set to zero
# =====================================================================
def fig_2_48():
    o = []
    o.append(sumj(60, 60, ["", "", "+"]))
    o.append(bx(120, 38, 90, 44, "2/s"))
    o.append(sumj(260, 60, ["", "", "+"]))
    o.append(bx(310, 38, 90, 44, "1/(s+1)"))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "X(s)", 6.5, anchor="start"))
    o.append(ar(49, 60, 120, 60))
    o.append(ar(210, 60, 260, 60))
    o.append(ar(400, 60, 460, 60))
    o.append(tx(415, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ln(400, 60, 400, 95, color=INK))
    o.append(ln(400, 95, 260, 95, color=INK))
    o.append(ar(260, 95, 260, 71))
    o.append(bx(320, 95, 60, 22, "-(s+1)", size=6.5))
    o.append(ln(400, 60, 400, 115, color=INK))
    o.append(ln(400, 115, 60, 115, color=INK))
    o.append(ar(60, 115, 60, 71))
    o.append(bx(310, 115, 60, 22, "s+3", size=7))
    return _f(o, 480, 145,
              "Khi đặt D(s)=0, hệ chỉ còn đáp ứng với X(s).",
              "With the disturbance set to zero, the system responds only to X(s).")


# =====================================================================
# Figure 2.49 - System with input set to zero
# =====================================================================
def fig_2_49():
    o = []
    o.append(sumj(60, 60, ["", "", "+"]))
    o.append(bx(120, 38, 90, 44, "2/s"))
    o.append(sumj(260, 60, ["", "", "+"]))
    o.append(bx(310, 38, 90, 44, "1/(s+1)"))
    o.append(ar(20, 60, 49, 60))
    o.append(tx(14, 54, "0", 6.5, anchor="start"))
    o.append(ar(49, 60, 120, 60))
    o.append(ar(210, 60, 260, 60))
    o.append(ar(400, 60, 460, 60))
    o.append(tx(415, 54, "Y(s)", 6.5, anchor="start"))
    o.append(ar(260, 20, 260, 49))
    o.append(tx(266, 14, "D(s)", 6.5, anchor="start"))
    o.append(ln(400, 60, 400, 95, color=INK))
    o.append(ln(400, 95, 260, 95, color=INK))
    o.append(ar(260, 95, 260, 71))
    o.append(bx(320, 95, 60, 22, "-(s+1)", size=6.5))
    o.append(ln(400, 60, 400, 115, color=INK))
    o.append(ln(400, 115, 60, 115, color=INK))
    o.append(ar(60, 115, 60, 71))
    o.append(bx(310, 115, 60, 22, "s+3", size=7))
    return _f(o, 480, 145,
              "Khi đặt X(s)=0, đầu ra chỉ do nhiễu D(s) gây ra.",
              "With the input set to zero, the output is due only to the disturbance D(s).")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
