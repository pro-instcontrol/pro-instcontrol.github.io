# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 7.

Every figure is redrawn as a clean vector. Chapter 7 is Controllers and has 51
figures spanning mechanical thermostats, electronic switches (thyristor /
transistor / H-bridge), PID mode graphs, controller block diagrams, Bode plots,
PLC ladder diagrams and embedded-system examples.
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


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


def ln2(x1, y1, x2, y2, color=INK, sw=0.9, dash=""):
    return _line(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def ar(x1, y1, x2, y2, color=INK, sw=1.1, dash=""):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def blk(x, y, w, h, label, fill="#eef3fb", size=8, color=INK):
    return _box(x, y, w, h, label, fill=fill, size=size, color=color)


def sumj(x, y, r=11, label="\u03a3"):
    return _circle(x, y, r, fill="#eef3fb") + _txt(x, y + 3.6, label, 11)


def gax(x0, y0, W, H, xlab="", ylab=""):
    return _axes(x0, y0, W, H, xlab, ylab, xt=[], yt=[])


def gmap(x0, y0, W, H):
    def m(t, v):  # t,v normalised 0..1
        return (x0 + t * W, y0 + H - v * H)
    return m


# =====================================================================
# Figure 7.1 - Bimetallic thermostat
# =====================================================================
def fig_7_1():
    o = []
    o.append(_rect(50, 70, 170, 13, fill=RED))          # high expansivity
    o.append(_rect(50, 83, 170, 13, fill=BLUE))         # low expansivity
    o.append(tx(135, 67, "Vật liệu giãn nở lớn", 6.8))
    o.append(tx(135, 106, "Vật liệu giãn nở nhỏ", 6.8))
    o.append(_rect(44, 64, 8, 32, fill=INK))            # clamp
    o.append(_circle(228, 76, 4, fill=INK))             # fixed contact
    o.append(_circle(228, 83, 4, fill="#888"))          # moving (soft iron)
    o.append(_rect(238, 70, 12, 17, fill=GOLD))         # small magnet
    o.append(tx(244, 104, "Nam châm", 6.2, color=GREY))
    o.append(ln2(228, 87, 228, 138, color=GREY))
    o.append(ln2(244, 87, 244, 138, color=GREY))
    o.append(tx(150, 128, "Các điểm nối điện", 6.5, color=GREY))
    o.append(_arrow(16, 76, 44, 76, sw=1, color=GREY, dash="2 2"))
    o.append(tx(30, 66, "Chỉnh\ntemp.", 6.2, anchor="start", color=GREY))
    o.append(tx(135, 152, "Dải kép kim loại (bimetallic strip)", 7, color=GREY))
    return _f(o, 300, 165,
              "Cảm biến nhiệt dải kép kim loại: hai lớp vật liệu giãn nở khác nhau, tiếp điểm đóng/mở nhờ nam châm nhỏ và mạch điện.",
              "Bimetallic thermostat: two bonded strips of different expansivity, with a contact opened/closed by a small magnet and the electrical connections.")


# =====================================================================
# Figure 7.2 - Temperature controller switch point
# =====================================================================
def fig_7_2():
    o = []
    x0, y0, W, H = 50, 40, 250, 150
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Nhiệt độ", "Đầu ra"))
    o.append(tx(x0 + W / 2.0, y0 + H + 26, "Nhiệt độ", 7, color=GREY))
    o.append(tx(x0 - 8, y0 - 8, "Đầu ra", 7, color=GREY))
    # set value line
    sx = 0.5
    px, _ = m(sx, 0)
    o.append(ln2(px, y0, px, y0 + H, color=GOLD, dash="3 3"))
    o.append(tx(px, y0 - 4, "Giá trị đặt", 6.5, color=GOLD))
    # on-off step at set value
    o.append(_poly([m(0, 0.05), m(sx, 0.05), m(sx, 0.95), m(1, 0.95)], color=BLUE, sw=1.6))
    o.append(tx(x0 + 30, y0 + 30, "Off", 7, color=GREY))
    o.append(tx(x0 + W - 30, y0 + 30, "On", 7, color=GREY))
    return _f(o, 360, 230,
              "Điểm chuyển mạch của bộ điều khiển nhiệt độ: đầu ra chỉ có hai mức On/Off tại giá trị đặt.",
              "Temperature controller switch point: the output is just on or off at the set value.")


# =====================================================================
# Figure 7.3 - Fluctuation of temperature about set value
# =====================================================================
def fig_7_3():
    o = []
    x0, y0, W, H = 50, 50, 270, 150
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian", "Nhiệt độ"))
    sv = 0.6
    # set value line
    _, py = m(0, sv)
    o.append(ln2(x0, py, x0 + W, py, color=GOLD, dash="3 3"))
    o.append(tx(x0 + W - 2, py - 4, "Giá trị đặt", 6.5, anchor="end", color=GOLD))
    # oscillating temperature
    pts = []
    for i in range(0, 101):
        t = i / 100.0
        env = 0.12 * (1 - t)
        v = sv + env * math.sin(t * 22)
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.6))
    o.append(tx(x0 + 40, y0 + 20, "Temp. dưới giá trị đặt \u2192 bật", 6.2, color=GREY))
    o.append(tx(x0 + 40, y0 + 34, "Temp. tiếp tục tăng sau khi tắt", 6.2, color=GREY))
    return _f(o, 370, 230,
              "Nhiệt độ dao động quanh giá trị đặt do độ trễ: khi dưới giá trị đặt thì bật, nhưng nhiệt độ tiếp tục tăng một lúc sau khi tắt.",
              "Fluctuation of temperature about the set value because of time lags: the heater is switched on below set value yet temperature keeps rising after switch-off.")


# =====================================================================
# Figure 7.4 - On-off controller with a dead band
# =====================================================================
def fig_7_4():
    o = []
    x0, y0, W, H = 50, 50, 270, 150
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian", "Nhiệt độ / Đầu ra"))
    sv = 0.55
    _, py = m(0, sv)
    o.append(ln2(x0, py, x0 + W, py, color=GOLD, dash="3 3"))
    o.append(tx(x0 + W - 2, py - 4, "Giá trị đặt", 6.5, anchor="end", color=GOLD))
    top = sv + 0.08
    bot = sv - 0.08
    _, pto = m(0, top)
    _, pbo = m(0, bot)
    o.append(ln2(x0, pto, x0 + W, pto, color=RED, dash="4 3"))
    o.append(ln2(x0, pbo, x0 + W, pbo, color=RED, dash="4 3"))
    o.append(tx(x0 + 10, pto - 3, "trần dải chết", 6.2, color=RED))
    o.append(tx(x0 + 10, pbo + 8, "đáy dải chết", 6.2, color=RED))
    # controller off when temp reaches top, on when reaches bottom
    for k in range(3):
        a = 0.12 + k * 0.28
        b = a + 0.16
        o.append(_poly([m(a, 0.05), m(a, 0.95), m(b, 0.95), m(b, 0.05)], color=BLUE, sw=1.5))
    o.append(tx(x0 + 30, y0 + 28, "Tắt", 7, color=GREY))
    o.append(tx(x0 + 40, y0 + 44, "Bật", 7, color=GREY))
    return _f(o, 370, 230,
              "Bộ điều khiển On/Off có dải chết (dead band): tắt khi nhiệt độ chạm trần dải chết, bật khi chạm đáy — giảm tần số chuyển mạch.",
              "On-off controller with a dead band: it switches off when temperature reaches the top of the band and on at the bottom, reducing switching frequency.")


# =====================================================================
# Figure 7.5 - Thyristor circuit
# =====================================================================
def fig_7_5():
    o = []
    # 300 V source
    o.append(_rect(40, 60, 16, 80, fill="#eee"))
    o.append(tx(48, 50, "300 V", 7))
    o.append(ln2(48, 60, 48, 40, color=INK))
    o.append(ln2(48, 140, 48, 160, color=INK))
    # 30 ohm resistor
    o.append(_rect(120, 95, 60, 10, fill="#eee"))
    o.append(tx(150, 90, "30 \u03a9", 7))
    o.append(ln2(48, 40, 120, 40, color=INK))
    o.append(ln2(120, 40, 120, 95, color=INK))
    o.append(ln2(180, 40, 230, 40, color=INK))
    o.append(ln2(230, 40, 230, 95, color=INK))
    # thyristor symbol
    o.append(_circle(230, 110, 18, fill="#eef3fb"))
    o.append(tx(230, 113, "SCR", 7))
    o.append(ln2(230, 128, 230, 160, color=INK))
    o.append(ln2(48, 160, 230, 160, color=INK))
    # gate
    o.append(ln2(248, 110, 270, 110, color=INK))
    o.append(tx(278, 110, "Gate", 7))
    return _f(o, 320, 190,
              "Mạch thyristor: thyristor mắc nối tiếp với điện trở 30 Ω dưới nguồn 300 V; cổng (gate) điều khiển điện áp đánh thủng.",
              "Thyristor circuit: the SCR is in series with a 30 \u03a9 resistor across 300 V; the gate controls the breakdown voltage.")


# =====================================================================
# Figure 7.6 - Thyristor d.c. control
# =====================================================================
def fig_7_6():
    o = []
    x0, y0, W, H = 40, 30, 280, 80
    m = gmap(x0, y0, W, H)
    # gate AC signal
    o.append(tx(x0, y0 - 6, "Tín hiệu cổng (xác lập)", 6.5, color=GREY))
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        v = 0.5 + 0.45 * math.sin(t * 22)
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.4))
    # chopped output below
    y1 = 130
    m2 = gmap(x0, y1, W, 80)
    o.append(tx(x0, y1 - 6, "Điện áp ra bị chóp (chopped)", 6.5, color=GREY))
    out = []
    for i in range(0, 121):
        t = i / 120.0
        # on when sin positive
        on = math.sin(t * 22) > 0
        out.append(m2(t, 0.85 if on else 0.1))
    o.append(_poly(out, color=RED, sw=1.4))
    return _f(o, 360, 240,
              "Điều khiển dòng một chiều bằng thyristor: tín hiệu xoay chiều vào cổng chóp điện áp cấp cho tải, trị trung bình thay đổi được.",
              "Thyristor d.c. control: an a.c. gate signal chops the d.c. supply to the load, giving a controllable average voltage.")


# =====================================================================
# Figure 7.7 - Thyristor control for a.c. power to a load
# =====================================================================
def fig_7_7():
    o = []
    # a.c. source
    o.append(_circle(40, 100, 14, fill="#eef3fb"))
    o.append(tx(40, 103, "~", 12))
    o.append(ln2(54, 100, 90, 100, color=INK))
    # load
    o.append(_rect(150, 92, 44, 16, fill="#eee"))
    o.append(tx(172, 87, "Tải", 7))
    o.append(ln2(90, 100, 150, 100, color=INK))
    o.append(ln2(194, 100, 250, 100, color=INK))
    # thyristor
    o.append(_circle(250, 100, 16, fill="#eef3fb"))
    o.append(tx(250, 103, "SCR", 7))
    o.append(ln2(250, 116, 250, 150, color=INK))
    o.append(ln2(40, 114, 250, 114, color=INK))
    # R1, R2 pot, diode on gate
    o.append(_rect(250, 70, 10, 30, fill="#eee"))
    o.append(tx(255, 64, "R1", 7))
    o.append(_rect(285, 60, 24, 12, fill="#eee"))
    o.append(tx(297, 55, "R2", 7))
    o.append(ln2(260, 70, 260, 50, color=INK))
    o.append(_circle(260, 50, 4, fill=INK))  # diode
    o.append(ln2(260, 46, 297, 46, color=INK))
    o.append(ln2(297, 46, 297, 72, color=INK))
    o.append(tx(310, 100, "Điốt", 6.5, color=GREY))
    return _f(o, 340, 175,
              "Điều khiển a.c. bằng thyristor: tải mắc nối tiếp thyristor; biến trở R2 đặt mức kích, điốt bảo vệ cổng; trễ góc kích đổi công suất.",
              "Thyristor a.c. control: the load is in series with the SCR; R2 sets the trigger level, a diode protects the gate, and trigger delay varies the power.")


# =====================================================================
# Figure 7.8 - Transistor switch (a) and (b)
# =====================================================================
def fig_7_8():
    o = []
    # (a)
    o.append(tx(60, 20, "(a) Có đầu vào", 7))
    o.append(_rect(40, 40, 16, 60, fill="#eee"))
    o.append(tx(48, 110, "Rc", 7))
    o.append(ln2(48, 40, 48, 70, color=INK))
    o.append(ln2(48, 70, 90, 70, color=INK))
    # transistor triangle
    o.append(_poly([(90, 70), (110, 62), (110, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(110, 70, 130, 70, color=INK))
    o.append(ln2(100, 70, 100, 120, color=INK))  # base
    o.append(tx(104, 128, "Base", 6.5))
    o.append(ln2(130, 70, 130, 50, color=INK))
    o.append(ln2(48, 40, 130, 40, color=INK))
    o.append(tx(150, 44, "Vcc", 7))
    o.append(ln2(130, 70, 130, 110, color=INK))
    o.append(ln2(130, 110, 90, 110, color=INK))
    o.append(tx(70, 95, "Vin", 6.5))
    # (b)
    o.append(tx(230, 20, "(b) Không đầu vào", 7))
    o.append(_rect(210, 40, 16, 60, fill="#eee"))
    o.append(tx(218, 110, "Rc", 7))
    o.append(ln2(218, 40, 218, 70, color=INK))
    o.append(ln2(218, 70, 260, 70, color=INK))
    o.append(_poly([(260, 70), (280, 62), (280, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(280, 70, 300, 70, color=INK))
    o.append(ln2(270, 70, 270, 120, color=INK))
    o.append(tx(274, 128, "Base", 6.5))
    o.append(ln2(300, 70, 300, 50, color=INK))
    o.append(ln2(218, 40, 300, 40, color=INK))
    o.append(tx(320, 44, "Vcc", 7))
    o.append(ln2(300, 70, 300, 110, color=INK))
    o.append(ln2(300, 110, 260, 110, color=INK))
    o.append(tx(280, 95, "Vout = 0", 6.5))
    return _f(o, 370, 140,
              "Khoá transistor: (a) có Vin → collector-emitter thông dẫn thấp, Vout \u2248 0; (b) không có Vin → trở cao, toàn bộ Vcc ra ở Vout.",
              "Transistor switch: (a) with input the collector-emitter resistance drops and Vout is near 0; (b) with no input the resistance is high and Vcc appears at the output.")


# =====================================================================
# Figure 7.9 - Darlington pair
# =====================================================================
def fig_7_9():
    o = []
    o.append(tx(60, 20, "+V", 7))
    o.append(ln2(60, 26, 60, 60, color=INK))
    o.append(_poly([(60, 70), (85, 62), (85, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(85, 70, 130, 70, color=INK))
    # second transistor
    o.append(_poly([(130, 70), (155, 62), (155, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(155, 70, 200, 70, color=INK))
    o.append(ln2(100, 70, 100, 95, color=INK))
    o.append(tx(96, 105, "Input", 6.5))
    o.append(ln2(200, 70, 200, 45, color=INK))
    o.append(tx(210, 46, "Output", 7))
    o.append(ln2(85, 70, 85, 110, color=INK))
    o.append(ln2(155, 70, 155, 110, color=INK))
    o.append(_circle(120, 110, 4, fill=INK))  # protection diode
    o.append(ln2(85, 110, 155, 110, color=INK))
    o.append(ln2(120, 114, 120, 130, color=INK))
    o.append(tx(130, 130, "Diode bảo vệ", 6.2, color=GREY))
    return _f(o, 260, 150,
              "Cặp Darlington: hai transistor khuếch đại dòng base nhỏ thành dòng lớn để khoá tải, có diode bảo vệ khi tắt.",
              "Darlington pair: two transistors amplify a small base current to switch a larger load, with a protection diode across them.")


# =====================================================================
# Figure 7.10 - Pulse-width modulation
# =====================================================================
def fig_7_10():
    o = []
    # block diagram
    o.append(blk(30, 20, 90, 26, "PWM\nd.c. input"))
    o.append(ar(120, 33, 150, 33))
    o.append(blk(150, 20, 90, 26, "Hệ thống\nchóp"))
    o.append(ar(240, 33, 270, 33))
    o.append(blk(270, 20, 90, 26, "Đầu ra\nd.c. chóp"))
    # waveform
    x0, y0, W, H = 30, 90, 320, 90
    m = gmap(x0, y0, W, H)
    o.append(tx(x0, y0 - 6, "Điện áp trung bình thay đổi theo độ rộng xung", 6.5, color=GREY))
    on = [0.0, 0.5, 0.6, 1.0]
    segs = [(0.05, 0.25), (0.35, 0.6), (0.7, 0.92)]
    for (a, b) in segs:
        o.append(_poly([m(a, 0.9), m(a, 0.1), m(b, 0.1), m(b, 0.9)], color=BLUE, sw=1.4))
    return _f(o, 380, 200,
              "Điều chế độ rộng xung (PWM): khóa tắt/bật điện áp một chiều; phần trăm chu kỳ bật càng lớn thì trị trung bình càng gần điện áp vào.",
              "Pulse-width modulation: a d.c. voltage is switched on and off; the larger the fraction of the cycle that is on, the closer the average to the input.")


# =====================================================================
# Figure 7.11 - PNP/transistor control circuit
# =====================================================================
def fig_7_11():
    o = []
    o.append(tx(40, 20, "Nguồn nuôi", 6.5, color=GREY))
    o.append(ln2(50, 30, 50, 60, color=INK))
    o.append(_poly([(50, 70), (75, 62), (75, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(75, 70, 120, 70, color=INK))
    o.append(_poly([(120, 70), (145, 62), (145, 78)], fill="#eef3fb", color=INK))
    o.append(ln2(145, 70, 190, 70, color=INK))
    o.append(ln2(97, 70, 97, 110, color=INK))
    o.append(tx(93, 120, "Đầu vào PWM", 6.2))
    o.append(_circle(120, 95, 4, fill=INK))
    o.append(ln2(120, 95, 120, 130, color=INK))
    o.append(_circle(120, 95, 8, fill="none", color=INK))
    o.append(tx(132, 130, "Diode", 6.2, color=GREY))
    o.append(ln2(190, 70, 190, 45, color=INK))
    o.append(tx(200, 46, "Động cơ", 7))
    o.append(_rect(195, 35, 40, 14, fill="#eee"))
    return _f(o, 260, 150,
              "Mạch điều khiển transistor thực hiện PWM: tín hiệu xung từ vi xử lý khoá transistor, diode cho dòng cảm ứng khi tắt; điều khiển tốc độ động cơ.",
              "Transistor circuit for PWM: the pulsed signal switches the transistor and a diode provides a path for the motor inductive current when it is off.")


# =====================================================================
# Figure 7.12 - H circuit
# =====================================================================
def fig_7_12():
    o = []
    o.append(tx(60, 18, "+V", 7))
    o.append(ln2(60, 24, 60, 50, color=INK))
    # four transistors as switches
    for (x, y, lab) in [(60, 50, "1"), (60, 130, "2"), (210, 50, "4"), (210, 130, "3")]:
        o.append(_circle(x, y, 12, fill="#eef3fb"))
        o.append(tx(x, y + 3, lab, 9))
    o.append(ln2(60, 50, 60, 130, color=INK))
    o.append(ln2(210, 50, 210, 130, color=INK))
    o.append(ln2(60, 50, 210, 50, color=INK))
    o.append(ln2(60, 130, 210, 130, color=INK))
    # motor in middle
    o.append(_rect(125, 78, 36, 24, fill="#eee"))
    o.append(tx(143, 95, "M", 11))
    o.append(ln2(143, 78, 143, 50, color=INK))
    o.append(ln2(143, 130, 143, 102, color=INK))
    o.append(tx(30, 52, "A", 7))
    o.append(tx(30, 132, "B", 7))
    return _f(o, 260, 160,
              "Mạch H dùng 4 transistor: bật (1,4) chạy thuận, bật (2,3) chạy nghịch; tín hiệu PWM vào A hoặc B đổi hướng và tốc độ động cơ.",
              "H-circuit with four transistors: 1 and 4 on drives forward, 2 and 3 on drives reverse; the PWM signal on A or B sets direction and speed.")


# =====================================================================
# Figure 7.13 - Circuit for microprocessor control of a motor
# =====================================================================
def fig_7_13():
    o = []
    o.append(tx(20, 16, "Forward/\nreverse", 6.5, color=GREY))
    o.append(tx(20, 60, "PWM", 7))
    # AND gates 1-4 and inverter
    gxy = [(60, 40, "1"), (60, 90, "2"), (60, 140, "3"), (60, 190, "4")]
    for (x, y, lab) in gxy:
        o.append(_rect(x - 16, y - 12, 32, 24, fill="#eef3fb"))
        o.append(tx(x, y + 3, "AND " + lab, 6.5))
    o.append(_rect(150, 110, 30, 22, fill="#eef3fb"))
    o.append(tx(165, 123, "NOT", 7))
    # connections
    o.append(ln2(20, 40, 44, 40, color=INK))
    o.append(ln2(20, 90, 44, 90, color=INK))
    o.append(ln2(44, 40, 44, 140, color=INK))
    o.append(ln2(44, 140, 44, 190, color=INK))
    o.append(ln2(44, 40, 60, 40, color=INK))
    o.append(ln2(44, 90, 60, 90, color=INK))
    o.append(ln2(44, 140, 60, 140, color=INK))
    o.append(ln2(44, 190, 60, 190, color=INK))
    o.append(ln2(44, 90, 135, 121, color=INK))
    o.append(ln2(165, 121, 195, 121, color=INK))
    o.append(ln2(195, 121, 195, 90, color=INK))
    o.append(ln2(195, 90, 60, 90, color=INK))
    # transistors driven
    for y in [40, 90, 140, 190]:
        o.append(ln2(76, y, 110, y, color=INK))
        o.append(_circle(115, y, 9, fill="#eef3fb"))
        o.append(tx(115, y + 3, "T", 8))
    return _f(o, 230, 220,
              "Mạch điều khiển động cơ bằng vi xử lý: cổng AND + cổng NOT chọn transistor 1&4 (thuận) hoặc 2&3 (nghịch) theo tín hiệu forward/reverse và PWM.",
              "Microprocessor motor-control circuit: AND gates plus an inverter turn on transistors 1 and 4 (forward) or 2 and 3 (reverse) from the forward/reverse and PWM inputs.")


# =====================================================================
# Figure 7.14 - Microprocessor controller with feedback
# =====================================================================
def fig_7_14():
    o = []
    o.append(blk(20, 60, 80, 26, "Giá trị đặt"))
    o.append(ar(100, 73, 120, 73))
    o.append(sumj(130, 73))
    o.append(ar(141, 73, 175, 73))
    o.append(blk(175, 60, 80, 26, "Vi xử lý\n+ PWM"))
    o.append(ar(255, 73, 290, 73))
    o.append(blk(290, 60, 70, 26, "Động cơ"))
    o.append(ar(360, 73, 360, 140, color=INK))
    o.append(ar(360, 150, 250, 150, color=INK))
    o.append(blk(180, 137, 70, 26, "ADC"))
    o.append(ar(250, 150, 222, 150, color=INK))
    o.append(ar(180, 150, 150, 150, color=INK))
    o.append(blk(80, 137, 70, 26, "Tacho-\ngenerator"))
    o.append(ar(150, 150, 141, 150, color=INK))
    o.append(ar(130, 150, 130, 100, color=INK))
    o.append(tx(370, 110, "Phản hồi", 6.5, color=GREY, anchor="start"))
    return _f(o, 400, 190,
              "Điều khiển kín bằng vi xử lý: tín hiệu từ tachogenerator qua ADC thành số, vi xử lý so sánh với giá trị đặt và xuất PWM điều khiển động cơ.",
              "Microprocessor closed-loop controller: the tachogenerator output is digitised by an ADC, compared with the set value by the processor, and a PWM signal drives the motor.")


# =====================================================================
# Figure 7.15 - Proportional mode
# =====================================================================
def fig_7_15():
    o = []
    x0, y0, W, H = 50, 40, 250, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Sai lệch e", "Đầu ra"))
    o.append(_poly([m(0, 0.05), m(1, 0.95)], color=BLUE, sw=1.8))
    o.append(tx(x0 + 30, y0 + 140, "Đầu ra = Kp \u00b7 e", 7, color=GREY))
    return _f(o, 360, 230,
              "Chế độ tỉ lệ (P): đầu ra của bộ điều khiển tỉ lệ với sai lệch, tức đầu ra = Kp\u00b7e.",
              "Proportional mode: the controller output is proportional to the error, i.e. output = Kp\u00b7e.")


# =====================================================================
# Figure 7.16 - Derivative mode
# =====================================================================
def fig_7_16():
    o = []
    # error-time graph
    o.append(tx(20, 16, "Đồ thị sai lệch - thời gian", 6.5, color=GREY))
    m1 = gmap(20, 30, 150, 90)
    o.append(gax(20, 30, 150, 90, "t", "e"))
    o.append(_poly([m1(0, 0.1), m1(0.3, 0.85), m1(1, 0.85)], color=BLUE, sw=1.5))
    # derivative output
    o.append(tx(200, 16, "Đầu ra tỉ lệ độ dốc", 6.5, color=GREY))
    m2 = gmap(200, 30, 150, 90)
    o.append(gax(200, 30, 150, 90, "t", "đầu ra"))
    o.append(_poly([m2(0, 0.1), m2(0.3, 0.85), m2(0.3, 0.1), m2(1, 0.1)], color=RED, sw=1.5))
    return _f(o, 370, 150,
              "Chế độ đạo hàm (D): đầu ra tỉ lệ với tốc độ đổi của sai lệch — độ dốc của đồ thị sai lệch-thời gian.",
              "Derivative mode: the output is proportional to the rate of change of error, i.e. the slope of the error-time graph.")


# =====================================================================
# Figure 7.17 - Integral mode
# =====================================================================
def fig_7_17():
    o = []
    o.append(tx(20, 16, "Đồ thị sai lệch - thời gian", 6.5, color=GREY))
    m1 = gmap(20, 30, 150, 90)
    o.append(gax(20, 30, 150, 90, "t", "e"))
    o.append(_poly([m1(0, 0.1), m1(0.3, 0.85), m1(1, 0.85)], color=BLUE, sw=1.5))
    o.append(tx(200, 16, "Diện tích dưới đồ thị (tích phân)", 6.5, color=GREY))
    m2 = gmap(200, 30, 150, 90)
    o.append(gax(200, 30, 150, 90, "t", "đầu ra"))
    o.append(_poly([m2(0, 0.05), m2(0.3, 0.3), m2(1, 0.9)], color=GREEN, sw=1.5))
    o.append(tx(200, 132, "Đầu ra không về 0 khi e = 0", 6.2, color=GREY))
    return _f(o, 370, 150,
              "Chế độ tích phân (I): đầu ra tỉ lệ với diện tích dưới đồ thị sai lệch theo thời gian, nên vẫn có giá trị ngay cả khi sai lệch đã về 0.",
              "Integral mode: the output is proportional to the area under the error-time graph, so it can be non-zero even when the error has returned to zero.")


# =====================================================================
# Figure 7.18 - Proportional controller in control system
# =====================================================================
def fig_7_18():
    o = []
    o.append(blk(20, 70, 70, 26, "Giá trị đặt"))
    o.append(ar(90, 83, 110, 83))
    o.append(sumj(120, 83))
    o.append(ar(131, 83, 160, 83))
    o.append(blk(160, 70, 60, 26, "Kp"))
    o.append(ar(220, 83, 250, 83))
    o.append(blk(250, 70, 70, 26, "G(s)"))
    o.append(ar(320, 83, 370, 83))
    o.append(tx(380, 86, "Đầu ra", 7))
    o.append(ar(370, 96, 370, 150, color=INK))
    o.append(ar(370, 160, 230, 160, color=INK))
    o.append(blk(160, 147, 70, 26, "H(s)"))
    o.append(ar(230, 160, 131, 160, color=INK))
    o.append(ar(120, 160, 120, 96, color=INK))
    return _f(o, 410, 190,
              "Bộ điều khiển tỉ lệ trong hệ kín: sai lệch qua khối Kp rồi G(s), tín hiệu phản hồi qua H(s) trừ vào giá trị đặt.",
              "Proportional controller in a closed-loop system: the error passes through the Kp block then G(s), with feedback through H(s) subtracted at the summing junction.")


# =====================================================================
# Figure 7.19 - Step response of an under-damped system
# =====================================================================
def fig_7_19():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian", "Đầu ra"))
    ss = 0.8
    _, pys = m(0, ss)
    o.append(ln2(x0, pys, x0 + W, pys, color=GOLD, dash="3 3"))
    o.append(tx(x0 + W - 2, pys - 4, "Giá trị xác lập", 6.5, anchor="end", color=GOLD))
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        v = ss * (1 - math.exp(-3.2 * t) * math.cos(5.5 * t))
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    o.append(tx(x0 + 150, y0 + 70, "Overshoot", 7, color=RED))
    return _f(o, 370, 230,
              "Đáp ứng bậc của hệ dao động (under-damped): đầu ra vượt quá giá trị xác lập (overshoot) rồi dần hội tụ.",
              "Step response of an under-damped system: the output overshoots the steady-state value before settling.")


# =====================================================================
# Figure 7.20 - Water level control system
# =====================================================================
def fig_7_20():
    o = []
    o.append(blk(20, 40, 80, 26, "Giá trị đặt\nmức nước"))
    o.append(ar(100, 53, 130, 53))
    o.append(sumj(140, 53))
    o.append(ar(151, 53, 180, 53))
    o.append(blk(180, 40, 70, 26, "Bộ điều\nkhiển"))
    o.append(ar(250, 53, 285, 53))
    o.append(blk(285, 40, 70, 26, "Van"))
    o.append(ar(355, 53, 355, 95, color=INK))
    # tank
    o.append(_rect(315, 100, 80, 70, fill="#eef3fb"))
    o.append(tx(355, 175, "Bể chứa", 7, color=GREY))
    o.append(ln2(355, 170, 355, 200, color=INK))
    o.append(ar(355, 205, 250, 205, color=INK))
    o.append(blk(180, 192, 70, 26, "Đo lưu\nlượng ra"))
    o.append(ar(250, 205, 151, 205, color=INK))
    o.append(ar(140, 205, 140, 66, color=INK))
    return _f(o, 410, 230,
              "Điều khiển mức nước: bộ điều khiển chỉnh van theo sai lệch mức; nhưng với tỉ lệ, để giữ lưu lượng ra mới cần một sai lệch (offset).",
              "Water-level control: the controller adjusts the valve from the level error; with proportional control a steady error (offset) is needed to hold a new outflow.")


# =====================================================================
# Figure 7.21 - Steady-state error with a step input
# =====================================================================
def fig_7_21():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian", "Tín hiệu"))
    # input step
    o.append(_poly([m(0, 0.1), m(0.15, 0.1), m(0.15, 0.9), m(1, 0.9)], color=INK, sw=1.5))
    o.append(tx(x0 + 20, y0 + 30, "Đầu vào", 7, color=GREY))
    # output lags and stops short
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        v = 0.1 + 0.75 * (1 - math.exp(-3 * t))
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.6))
    o.append(tx(x0 + 60, y0 + 95, "Đầu ra", 7, color=GREY))
    _, pyi = m(0, 0.9)
    _, pyo = m(0, 0.85)
    o.append(ln2(x0 + W - 20, pyi, x0 + W - 20, pyo, color=RED, sw=1))
    o.append(tx(x0 + W - 18, (pyi + pyo) / 2, "offset", 6.5, anchor="start", color=RED))
    return _f(o, 370, 230,
              "Sai lệch xác lập (offset) với đầu vào bậc: đầu ra không đạt được giá trị đặt; hiệu số gọi là offset.",
              "Steady-state error with a step input: the output never reaches the input value, the difference being the offset.")


# =====================================================================
# Figure 7.22 - PD controller output to a ramp input
# =====================================================================
def fig_7_22():
    o = []
    x0, y0, W, H = 30, 30, 110, 80
    for i, (lab, col, fn) in enumerate([
        ("P only", BLUE, lambda t: 0.1 + 0.5 * t),
        ("D only", RED, lambda t: 0.85 if t < 0.15 else 0.1),
        ("P + D", GREEN, lambda t: min(0.95, 0.1 + 0.5 * t + (0.7 if t < 0.15 else 0))),
    ]):
        mx = gmap(x0 + i * 125, y0, W, H)
        o.append(gax(x0 + i * 125, y0, W, H, "t", ""))
        o.append(tx(x0 + i * 125 + W / 2.0, y0 + H + 16, lab, 6.8, color=col))
        pts = [mx(t, max(0.05, min(0.95, fn(t)))) for t in [j / 60.0 for j in range(61)]]
        o.append(_poly(pts, color=col, sw=1.4))
    return _f(o, 400, 140,
              "Đáp ứng bộ điều khiển PD với đầu vào dốc: thành phần đạo hàm lớn khi độ dốc sai lệch lớn, giúp đầu ra tăng nhanh hơn chỉ tỉ lệ.",
              "PD controller output to a ramp input: the derivative term is largest when the error slope is greatest, so the output rises faster than with proportional alone.")


# =====================================================================
# Figure 7.23 - PI controller output to a step input
# =====================================================================
def fig_7_23():
    o = []
    x0, y0, W, H = 30, 30, 110, 80
    for i, (lab, col, fn) in enumerate([
        ("P only", BLUE, lambda t: 0.1 + 0.6 if t > 0.15 else 0.1),
        ("I only", RED, lambda t: 0.1 + 0.8 * min(1.0, t)),
    ]):
        mx = gmap(x0 + i * 125, y0, W, H)
        o.append(gax(x0 + i * 125, y0, W, H, "t", ""))
        o.append(tx(x0 + i * 125 + W / 2.0, y0 + H + 16, lab, 6.8, color=col))
        pts = [mx(t, max(0.05, min(0.95, fn(t)))) for t in [j / 60.0 for j in range(61)]]
        o.append(_poly(pts, color=col, sw=1.4))
    return _f(o, 290, 140,
              "Đáp ứng bộ điều khiển PI với đầu vào bậc: thành phần tích phân loại bỏ offset, đưa giá trị xác lập bằng giá trị đặt.",
              "PI controller output to a step input: the integral term removes the offset, giving a steady-state value equal to the set value.")


# =====================================================================
# Figure 7.24 - Error-time graph used in examples
# =====================================================================
def fig_7_24():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (s)", "Sai lệch e"))
    o.append(_poly([m(0, 0.1), m(0.1, 0.5), m(0.33, 0.5), m(0.33, 0.85), m(1, 0.85)],
                    color=BLUE, sw=1.7))
    o.append(tx(x0 + 40, y0 + 40, "e tăng rồi\ngiữ không đổi", 6.5, color=GREY))
    return _f(o, 370, 230,
              "Đồ thị sai lệch-thời gian dùng trong ví dụ: sai lệch tăng rồi duy trì không đổi.",
              "The error-time graph used in the worked examples: the error rises then stays constant.")


# =====================================================================
# Figure 7.25 - Example (a) proportional
# =====================================================================
def fig_7_25():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (s)", "Đầu ra (%)"))
    # output = 50 + 5*e ; e as in 7.24 mapped 0..0.85 -> 50..92.5
    def out(t):
        if t < 0.1:
            e = 0.1 + (0.5 - 0.1) * (t / 0.1)
        elif t < 0.33:
            e = 0.5
        else:
            e = 0.85
        return 0.1 + (50 + 5 * (e * 0.85)) / 100.0 * 0.85
    # simpler: map 50..93 onto 0.1..0.9
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        if t < 0.1:
            e = 0.1 + (0.5 - 0.1) * (t / 0.1)
        elif t < 0.33:
            e = 0.5
        else:
            e = 0.85
        val = 50 + 5 * e
        pts.append(m(t, 0.1 + (val - 40) / 60.0 * 0.8))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    o.append(tx(x0 + 30, y0 + 25, "50% + 5e", 7, color=GREY))
    return _f(o, 370, 230,
              "Ví dụ (a) chỉ tỉ lệ Kp=5, bắt đầu tại 50%: đầu ra = 50% + 5 lần sai lệch.",
              "Example (a) proportional only, Kp=5, starting at 50%: output = 50% + 5 times the error.")


# =====================================================================
# Figure 7.26 - Example (b) PD
# =====================================================================
def fig_7_26():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (s)", "Đầu ra (%)"))
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        if t < 0.1:
            e = 0.1 + (0.5 - 0.1) * (t / 0.1)
        elif t < 0.33:
            e = 0.5
        else:
            e = 0.85
        slope = 4.0 if t < 0.1 else (0.0 if t < 1 else 0.0)
        val = 50 + 5 * e + 2.0 * slope
        pts.append(m(t, 0.1 + (val - 40) / 60.0 * 0.8))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    o.append(tx(x0 + 30, y0 + 25, "50% + 5e + 2,0\u00b7độ dốc", 7, color=GREY))
    return _f(o, 370, 230,
              "Ví dụ (b) tỉ lệ + đạo hàm Kp=5, Kd=2,0 s: phần đạo hàm lớn trong 0\u20131 s (độ dốc e), sau đó chỉ còn tỉ lệ.",
              "Example (b) proportional plus derivative, Kp=5, Kd=2.0 s: the derivative term is 2.0 times the error slope, large during 0\u20131 s.")


# =====================================================================
# Figure 7.27 - Example (c) PI
# =====================================================================
def fig_7_27():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (s)", "Đầu ra (%)"))
    area = 0.0
    pts = []
    dt = 1.0 / 120.0
    for i in range(0, 121):
        t = i / 120.0
        if t < 0.1:
            e = 0.1 + (0.5 - 0.1) * (t / 0.1)
        elif t < 0.33:
            e = 0.5
        else:
            e = 0.85
        if i > 0:
            area += e * dt
        val = 50 + 5 * e + 2.0 * area
        pts.append(m(t, 0.1 + (val - 40) / 80.0 * 0.8))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    o.append(tx(x0 + 30, y0 + 25, "50% + 5e + 2,0\u00b7diện tích", 7, color=GREY))
    return _f(o, 370, 230,
              "Ví dụ (c) tỉ lệ + tích phân Kp=5, Ki=2,0 s\u207b\u00b9: đầu ra tăng theo diện tích dưới đồ thị sai lệch, khử offset.",
              "Example (c) proportional plus integral, Kp=5, Ki=2.0 s\u207b\u00b9: the output rises with the area under the error graph and removes the offset.")


# =====================================================================
# Figure 7.28 - Proportional band
# =====================================================================
def fig_7_28():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Độ lệch (%)", "Đầu ra (%)"))
    # 50% PB: 50% deviation -> 100% output
    o.append(_poly([m(0, 0.05), m(0.5, 0.95), m(1, 0.95)], color=BLUE, sw=1.7))
    o.append(tx(x0 + 40, y0 + 40, "100% đổi đầu ra", 6.5, color=GREY))
    _, py = m(0.5, 0.95)
    o.append(ln2(x0, py, x0 + W * 0.5, py, color=GOLD, dash="3 3"))
    o.append(tx(x0 + W * 0.5 + 4, py - 4, "PB 50%", 6.5, anchor="start", color=GOLD))
    return _f(o, 370, 230,
              "Dải tỉ lệ (proportional band): phần trăm độ lệch tạo ra 100% đổi đầu ra; PB 50% nghĩa là lệch 50% đổi đầu ra 100%.",
              "Proportional band: the percentage deviation that produces a 100% change in controller output; a 50% PB means a 50% deviation gives 100% output change.")


# =====================================================================
# Figure 7.29 - Typical controller front panel
# =====================================================================
def fig_7_29():
    o = []
    o.append(_rect(20, 20, 330, 180, fill="#f3f1ea", sw=1))
    o.append(tx(185, 34, "Mặt trước bộ điều khiển ba số tử", 7.5, weight="bold"))
    # displays
    o.append(_rect(35, 50, 120, 30, fill="#dff0e0"))
    o.append(tx(95, 68, "Hiển thị biến\nquá trình", 6.5))
    o.append(_rect(170, 50, 120, 30, fill="#dff0e0"))
    o.append(tx(230, 68, "Hiển thị giá\ntrị đặt %", 6.5))
    # bar graph
    o.append(_rect(310, 50, 22, 110, fill="#eee"))
    o.append(_rect(312, 90, 18, 70, fill=BLUE))
    o.append(tx(321, 170, "Thanh", 6, color=GREY))
    # keys
    for i in range(5):
        o.append(_rect(45 + i * 30, 100, 24, 18, fill="#fff", sw=0.8))
    o.append(tx(185, 138, "Phím SP / M / A / Auto / Remote", 6.5, color=GREY))
    # digital display
    o.append(_rect(40, 145, 100, 22, fill="#1d1d1d"))
    o.append(tx(90, 160, "12.4 \u00b0C", 7, color="#fff"))
    o.append(tx(185, 162, "Hiển thị số", 6, color=GREY))
    return _f(o, 380, 220,
              "Mặt trước điển hình của bộ điều khiển quá trình ba số tử: màn hình biến quá trình, giá trị đặt, thanh đồ thị và các phím vận hành.",
              "Typical three-term process controller front panel: process-variable and set-point displays, a bar graph and the operating keys.")


# =====================================================================
# Figure 7.30 - Control system in manual mode
# =====================================================================
def fig_7_30():
    o = []
    o.append(blk(20, 60, 70, 26, "Giá trị đặt"))
    o.append(ar(90, 73, 110, 73))
    o.append(sumj(120, 73))
    o.append(ar(131, 73, 160, 73))
    o.append(blk(160, 60, 70, 26, "Bộ điều\nkhiển"))
    o.append(ar(230, 73, 265, 73))
    o.append(blk(265, 60, 70, 26, "Cơ cấu\nchỉnh"))
    o.append(ar(335, 73, 370, 73))
    o.append(blk(370, 60, 70, 26, "Thiết bị\nchấp hành"))
    o.append(ar(440, 73, 440, 140, color=INK))
    o.append(blk(370, 147, 70, 26, "Quá trình"))
    o.append(ar(370, 173, 290, 173, color=INK))
    o.append(blk(200, 160, 70, 26, "Đo lường"))
    o.append(ar(290, 173, 131, 173, color=INK))
    o.append(ar(120, 173, 120, 100, color=INK))
    # manual adjustment added into controller output
    o.append(blk(120, 20, 80, 22, "Chỉnh tay"))
    o.append(ar(160, 42, 195, 73, color=GOLD))
    return _f(o, 500, 200,
              "Hệ thống ở chế độ chỉnh tay: tín hiệu chỉnh tay được cộng vào đầu ra bộ điều khiển trước khi chuyển sang tự động (bumpless transfer).",
              "Control system in manual mode: a manually introduced signal is added to the controller output before switching to automatic control.")


# =====================================================================
# Figure 7.31 - Proportional controller
# =====================================================================
def fig_7_31():
    o = []
    o.append(blk(30, 70, 70, 26, "Sai lệch e"))
    o.append(ar(100, 83, 130, 83))
    o.append(blk(130, 70, 80, 26, "Kp"))
    o.append(ar(210, 83, 240, 83))
    o.append(blk(240, 70, 90, 26, "Đầu ra bộ\nđiều khiển"))
    return _f(o, 360, 130,
              "Bộ điều khiển tỉ lệ: đầu ra = Kp\u00b7e.",
              "Proportional controller: output = Kp\u00b7e.")


# =====================================================================
# Figure 7.32 - PD controller
# =====================================================================
def fig_7_32():
    o = []
    o.append(blk(30, 70, 70, 26, "Sai lệch e"))
    o.append(ar(100, 83, 130, 83))
    o.append(blk(130, 60, 70, 24, "Kp"))
    o.append(ar(200, 72, 240, 72))
    o.append(blk(240, 60, 70, 24, "Kd d/dt"))
    o.append(ar(310, 72, 345, 72))
    o.append(ar(100, 95, 130, 110, color=INK))
    o.append(blk(130, 100, 70, 24, "Kd d/dt"))
    o.append(ar(200, 112, 345, 112, color=INK))
    o.append(sumj(355, 90))
    o.append(ar(366, 90, 400, 90))
    o.append(blk(400, 77, 90, 26, "Đầu ra bộ\nđiều khiển"))
    return _f(o, 510, 150,
              "Bộ điều khiển tỉ lệ + đạo hàm: đầu ra = Kp\u00b7e + Kd\u00b7de/dt.",
              "Proportional plus derivative controller: output = Kp\u00b7e + Kd\u00b7de/dt.")


# =====================================================================
# Figure 7.33 - PI controller
# =====================================================================
def fig_7_33():
    o = []
    o.append(blk(30, 70, 70, 26, "Sai lệch e"))
    o.append(ar(100, 83, 130, 83))
    o.append(blk(130, 60, 70, 24, "Kp"))
    o.append(ar(200, 72, 240, 72))
    o.append(blk(240, 60, 70, 24, "Ki \u222b"))
    o.append(ar(310, 72, 345, 72))
    o.append(ar(100, 95, 130, 110, color=INK))
    o.append(blk(130, 100, 70, 24, "Ki \u222b"))
    o.append(ar(200, 112, 345, 112, color=INK))
    o.append(sumj(355, 90))
    o.append(ar(366, 90, 400, 90))
    o.append(blk(400, 77, 90, 26, "Đầu ra bộ\nđiều khiển"))
    return _f(o, 510, 150,
              "Bộ điều khiển tỉ lệ + tích phân: đầu ra = Kp\u00b7e + Ki\u222be dt.",
              "Proportional plus integral controller: output = Kp\u00b7e + Ki\u222be dt.")


# =====================================================================
# Figure 7.34 - PID controller
# =====================================================================
def fig_7_34():
    o = []
    o.append(blk(30, 80, 70, 24, "Sai lệch e"))
    o.append(ar(100, 92, 130, 92))
    o.append(blk(130, 50, 60, 22, "Kp"))
    o.append(blk(130, 80, 60, 22, "Kd d/dt"))
    o.append(blk(130, 110, 60, 22, "Ki \u222b"))
    o.append(ar(190, 61, 240, 61))
    o.append(ar(190, 91, 240, 91))
    o.append(ar(190, 121, 240, 121))
    o.append(sumj(250, 91))
    o.append(ar(261, 91, 300, 91))
    o.append(blk(300, 78, 80, 26, "Đầu ra bộ\nđiều khiển"))
    return _f(o, 410, 160,
              "Bộ điều khiển ba số tử (PID): đầu ra = Kp\u00b7e + Ki\u222be dt + Kd\u00b7de/dt.",
              "Three-term (PID) controller: output = Kp\u00b7e + Ki\u222be dt + Kd\u00b7de/dt.")


# =====================================================================
# Figure 7.35 - Example block diagram
# =====================================================================
def fig_7_35():
    o = []
    o.append(blk(20, 70, 80, 26, "Giá trị đặt"))
    o.append(ar(100, 83, 120, 83))
    o.append(sumj(130, 83))
    o.append(ar(141, 83, 170, 83))
    o.append(blk(170, 60, 90, 24, "Kp + Kd s"))
    o.append(ar(260, 72, 300, 72))
    o.append(blk(300, 60, 90, 24, "\u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9ns)"))
    o.append(ar(390, 72, 430, 72))
    o.append(tx(440, 75, "Đầu ra", 7))
    o.append(ar(430, 86, 430, 140, color=INK))
    o.append(ar(430, 150, 200, 150, color=INK))
    o.append(blk(130, 137, 70, 26, "H(s)"))
    o.append(ar(200, 150, 141, 150, color=INK))
    o.append(ar(130, 150, 130, 96, color=INK))
    return _f(o, 470, 180,
              "Ví dụ: hệ hở có bộ điều khiển PD (Kp+Kds) và quá trình G(s)=\u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9ns), có phản hồi H(s).",
              "Example: the open-loop system uses a PD controller Kp+Kd s and plant G(s)=\u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9ns) with feedback H(s).")


# =====================================================================
# Figure 7.36 - Bode gain plot for P, PI, PD, PID
# =====================================================================
def fig_7_36():
    o = []
    subs = [
        ("(a) P", BLUE, "flat", "20 lg Kp"),
        ("(b) PI", RED, "drop", "\u221220 dB/dec"),
        ("(c) PD", GREEN, "rise", "+20 dB/dec"),
        ("(d) PID", GOLD, "pid", None),
    ]
    for i, (lab, col, kind, note) in enumerate(subs):
        bx = 25 + (i % 2) * 175
        by = 25 + (i // 2) * 110
        m = gmap(bx, by, 150, 90)
        o.append(gax(bx, by, 150, 90, "lg f", "dB"))
        if kind == "flat":
            o.append(_poly([m(0, 0.5), m(1, 0.5)], color=col, sw=1.6))
        elif kind == "drop":
            o.append(_poly([m(0, 0.8), m(0.4, 0.8), m(1, 0.2)], color=col, sw=1.6))
        elif kind == "rise":
            o.append(_poly([m(0, 0.2), m(0.6, 0.2), m(1, 0.8)], color=col, sw=1.6))
        else:
            o.append(_poly([m(0, 0.7), m(0.35, 0.7), m(0.5, 0.4), m(1, 0.9)], color=col, sw=1.6))
        o.append(tx(bx + 75, by + 105, lab, 7, color=col))
    return _f(o, 380, 250,
              "Dạng cơ bản biểu đồ Bode lợi: (a) P tăng lợi hệ thống; (b) PI giảm lợi tần cao; (c) PD giảm lợi tần thấp và tăng; (d) PID phụ thuộc tỉ lệ \u03c4i/\u03c4d.",
              "Basic Bode gain plots: (a) P raises overall gain; (b) PI reduces high-frequency gain; (c) PD reduces low-frequency gain and raises it; (d) PID shape depends on \u03c4i/\u03c4d.")


# =====================================================================
# Figure 7.37 - Process reaction curve
# =====================================================================
def fig_7_37():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian", "Đầu ra (%)"))
    # S-shaped response to step
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        v = 0.1 + 0.8 / (1 + math.exp(-9 * (t - 0.5)))
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    # tangent at inflection
    _, pyi = m(0.5, 0.5)
    x1, y1 = m(0.30, 0.5 - 0.20)
    x2, y2 = m(0.70, 0.5 + 0.20)
    o.append(ln2(x1, y1, x2, y2, color=RED, dash="4 3"))
    # lag L intersection with axis
    xl, _ = m(0.30, 0)
    o.append(ln2(xl, y0, xl, pyi, color=GOLD, dash="3 3"))
    o.append(tx(xl - 4, y0 + H + 14, "L", 7, color=GOLD))
    o.append(tx(x0 + 120, y0 + 120, "R = M/T", 6.5, color=GREY))
    return _f(o, 370, 230,
              "Đường đặc tuyến quá trình (process reaction curve): tiếp tuyến tại điểm uốn cho độ dốc cực đại R = M/T; khoảng from test đến giao trục là độ trễ L.",
              "Process reaction curve: the tangent at the inflection gives the maximum gradient R = M/T; the time from the test to where the tangent meets the axis is the lag L.")


# =====================================================================
# Figure 7.38 - Direct digital control
# =====================================================================
def fig_7_38():
    o = []
    o.append(blk(20, 60, 90, 30, "Máy tính\n(DDC)"))
    o.append(ar(110, 75, 150, 75))
    o.append(blk(150, 60, 80, 30, "DAC"))
    o.append(ar(230, 75, 270, 75))
    o.append(blk(270, 60, 90, 30, "Cơ cấu\nchấp hành"))
    o.append(ar(360, 75, 360, 140, color=INK))
    o.append(blk(270, 147, 90, 30, "Quá trình"))
    o.append(ar(270, 162, 200, 162, color=INK))
    o.append(blk(120, 147, 80, 30, "ADC"))
    o.append(ar(200, 162, 110, 162, color=INK))
    o.append(ar(110, 162, 110, 90, color=INK))
    o.append(tx(20, 40, "Đo lường \u2192", 6.5, color=GREY))
    o.append(tx(150, 40, "Giá trị đặt", 6.5, color=GREY))
    return _f(o, 410, 200,
              "Điều khiển số trực tiếp (DDC): máy tính lấy mẫu đầu ra qua ADC, theo luật điều khiển tính tín hiệu hiệu chỉnh và xuất qua DAC tới cơ cấu chấp hành.",
              "Direct digital control: the computer samples the output via an ADC, computes the correction from the control law and sends it through a DAC to the actuator.")


# =====================================================================
# Figure 7.39 - The PLC system
# =====================================================================
def fig_7_39():
    o = []
    o.append(blk(20, 70, 90, 28, "Thiết bị\nlập trình"))
    o.append(ar(110, 84, 140, 84, color=INK))
    o.append(blk(140, 60, 90, 70, "PLC\nVi xử lý\nBộ nhớ\nNguồn\nGiao tiếp"))
    o.append(ar(230, 84, 270, 84, color=INK))
    o.append(blk(270, 60, 80, 28, "Đầu vào"))
    o.append(blk(270, 100, 80, 28, "Đầu ra"))
    o.append(tx(355, 74, "Cảm biến", 6.5, color=GREY))
    o.append(tx(355, 114, "Động cơ,\nvan", 6.5, color=GREY))
    return _f(o, 400, 160,
              "Hệ thống PLC: thiết bị lập trình nạp chương trình vào PLC (vi xử lý, bộ nhớ, nguồn, giao tiếp vào/ra) để giám sát cảm biến và điều khiển cơ cấu chấp hành.",
              "The PLC system: a programming device loads the program into the PLC (processor, memory, power supply, I/O interfaces) which monitors inputs and drives outputs.")


# =====================================================================
# Figure 7.40 - Hand-held programmer
# =====================================================================
def fig_7_40():
    o = []
    o.append(_rect(110, 30, 100, 150, fill="#e9e7df", sw=1))
    o.append(_rect(125, 45, 70, 45, fill="#1d1d1d"))
    o.append(tx(160, 70, "LCD", 7, color="#fff"))
    # keypad
    for r in range(3):
        for c in range(3):
            o.append(_circle(135 + c * 22, 110 + r * 20, 6, fill="#fff", color=INK))
    o.append(tx(160, 195, "Bàn phím & màn hình", 7, color=GREY))
    return _f(o, 320, 215,
              "Thiết bị lập trình cầm tay: bàn phím nhỏ và màn hình tinh thể lỏng để nhập chương trình PLC.",
              "Hand-held programmer: a small keyboard and liquid-crystal display for entering the PLC program.")


# =====================================================================
# Figure 7.41 - Motor switching circuit (a) conventional (b) ladder
# =====================================================================
def fig_7_41():
    o = []
    # (a)
    o.append(tx(40, 18, "(a) Mạch thường", 7))
    o.append(_rect(30, 40, 16, 50, fill="#eee"))
    o.append(tx(38, 100, "L1", 7))
    o.append(ln2(38, 40, 38, 70, color=INK))
    o.append(ln2(38, 70, 90, 70, color=INK))
    o.append(_circle(90, 70, 10, fill="#eef3fb"))
    o.append(tx(90, 73, "S", 8))
    o.append(ln2(100, 70, 150, 70, color=INK))
    o.append(_rect(150, 62, 40, 16, fill="#eee"))
    o.append(tx(170, 57, "Motor", 7))
    o.append(ln2(190, 70, 190, 110, color=INK))
    o.append(_rect(174, 110, 16, 40, fill="#eee"))
    o.append(tx(182, 160, "L2", 7))
    o.append(ln2(38, 110, 190, 110, color=INK))
    # (b) ladder
    o.append(tx(260, 18, "(b) Dạng thang", 7))
    o.append(ln2(250, 40, 250, 140, color=INK, sw=1.4))
    o.append(ln2(330, 40, 330, 140, color=INK, sw=1.4))
    o.append(ln2(250, 70, 330, 70, color=INK))
    o.append(_circle(290, 70, 9, fill="#eef3fb"))
    o.append(tx(290, 73, "S", 8))
    o.append(ln2(250, 110, 330, 110, color=INK))
    o.append(_rect(278, 102, 24, 16, fill="#eee"))
    o.append(tx(290, 132, "Motor", 6.5))
    o.append(tx(244, 35, "L1", 7))
    o.append(tx(334, 35, "L2", 7))
    return _f(o, 380, 180,
              "Mạch chuyển động cơ: (a) mạch nối tiếp công tắc và động cơ; (b) dạng thang (ladder) với hai thanh nguồn và một rung nối tiếp.",
              "Motor switching circuit: (a) the conventional series switch-and-motor circuit; (b) its ladder form with two power rails and one series rung.")


# =====================================================================
# Figure 7.42 - Basic symbols used with ladder programs
# =====================================================================
def fig_7_42():
    o = []
    o.append(tx(60, 20, "Đầu vào thường mở", 6.5, color=GREY))
    o.append(ln2(40, 60, 70, 60, color=INK))
    o.append(ln2(70, 50, 55, 70, color=INK))
    o.append(ln2(55, 50, 70, 70, color=INK))
    o.append(tx(60, 90, "||", 12, color=INK))
    o.append(tx(150, 20, "Đầu vào thường đóng", 6.5, color=GREY))
    o.append(ln2(130, 60, 160, 60, color=INK))
    o.append(_circle(145, 60, 9, fill="#eef3fb"))
    o.append(tx(150, 90, "|\u2502|", 12, color=INK))
    o.append(tx(250, 20, "Thiết bị ra", 6.5, color=GREY))
    o.append(_circle(260, 60, 11, fill="#eef3fb"))
    o.append(tx(260, 90, "O", 12, color=INK))
    o.append(tx(330, 20, "Cuối rung", 6.5, color=GREY))
    o.append(tx(340, 60, "END", 9, color=INK))
    return _f(o, 380, 110,
              "Ký hiệu cơ bản lập trình thang: tiếp điểm thường mở, thường đóng (đầu vào) và ký hiệu thiết bị ra, cùng END kết thúc rung.",
              "Basic ladder-program symbols: normally open and normally closed input contacts, the output-device symbol and the END rung marker.")


# =====================================================================
# Figure 7.43 - A ladder rung
# =====================================================================
def fig_7_43():
    o = []
    o.append(ln2(40, 40, 40, 120, color=INK, sw=1.4))
    o.append(ln2(180, 40, 180, 120, color=INK, sw=1.4))
    o.append(ln2(40, 70, 180, 70, color=INK))
    o.append(ln2(40, 70, 55, 70, color=INK))
    o.append(ln2(55, 60, 40, 80, color=INK))
    o.append(ln2(55, 60, 70, 80, color=INK))
    o.append(ln2(40, 100, 180, 100, color=INK))
    o.append(_circle(110, 100, 11, fill="#eef3fb"))
    o.append(tx(110, 130, "Khi công tắc đóng \u2192 ra bật", 6.5, color=GREY))
    return _f(o, 220, 150,
              "Một rung thang: đầu vào tiếp điểm thường mở nối với thiết bị ra; khi công tắc đóng (đầu vào mức cao) thì đầu ra kích hoạt.",
              "A ladder rung: a normally open input in series with the output symbol; when the switch closes the output is energised.")


# =====================================================================
# Figure 7.44 - Central heating system
# =====================================================================
def fig_7_44():
    o = []
    o.append(_rect(30, 60, 70, 50, fill="#eef3fb"))
    o.append(tx(65, 85, "Lò đun", 7))
    o.append(ar(100, 85, 140, 85, color=INK))
    o.append(_circle(150, 85, 11, fill="#eef3fb"))
    o.append(tx(150, 88, "Bơm", 6.5))
    o.append(ar(161, 85, 200, 85, color=INK))
    o.append(_rect(200, 65, 60, 40, fill="#eef3fb"))
    o.append(tx(230, 85, "Radiator", 6.5))
    o.append(ar(230, 105, 230, 150, color=INK))
    o.append(_rect(200, 150, 60, 40, fill="#eef3fb"))
    o.append(tx(230, 170, "Bồn nước\nnóng", 6.5))
    o.append(_circle(150, 150, 9, fill=RED))
    o.append(tx(150, 170, "Cảm biến\nnhiệt", 6))
    o.append(_rect(30, 20, 70, 24, fill="#eee"))
    o.append(tx(65, 36, "Công tắc\nStop/Run", 6))
    return _f(o, 300, 210,
              "Hệ thống sưởi trung tâm: lò đun, bơm, radiator và bồn nước nóng, với cảm biến nhiệt và công tắc Stop/Run theo đồng hồ.",
              "Central heating system: boiler, pump, radiators and hot-water tank, with temperature sensors and a Stop/Run clock switch.")


# =====================================================================
# Figure 7.45 - Central heating system with PLC controller
# =====================================================================
def fig_7_45():
    o = []
    o.append(ln2(30, 30, 30, 200, color=INK, sw=1.4))
    o.append(ln2(320, 30, 320, 200, color=INK, sw=1.4))
    o.append(tx(24, 22, "+24 V", 6.5))
    o.append(tx(322, 22, "0 V", 6.5))
    # rungs
    rows = [("X400", "Y430", 60), ("X401", "Y430", 90), ("X402", "Y430", 120),
            ("X403", "Y431", 150), ("X402", "Y432", 180)]
    for (inp, out, y) in rows:
        o.append(ln2(30, y, 320, y, color=INK))
        o.append(tx(60, y - 4, inp, 6.5, color=GREY))
        o.append(_circle(110, y, 8, fill="#eef3fb"))
        o.append(tx(200, y - 4, out, 6.5, color=GREY))
        o.append(_circle(250, y, 9, fill="#eef3fb"))
    o.append(tx(60, 215, "Đầu vào X400-X403, đầu ra Y430-Y432 (ladder PLC)", 6.5, color=GREY))
    return _f(o, 360, 230,
              "Hệ thống sưởi với bộ điều khiển PLC: các rung ladder với đầu vào X400\u2013X403 và đầu ra Y430\u2013Y432 điều khiển lò và van.",
              "Central heating with a PLC controller: ladder rungs with inputs X400\u2013X403 and outputs Y430\u2013Y432 switch the boiler and valves.")


# =====================================================================
# Figure 7.46 - Automatic focusing system
# =====================================================================
def fig_7_46():
    o = []
    o.append(blk(20, 70, 80, 26, "Cảm biến\nkhoảng cách"))
    o.append(ar(100, 83, 140, 83))
    o.append(blk(140, 60, 90, 30, "Vi xử lý"))
    o.append(ar(230, 75, 270, 75))
    o.append(blk(270, 60, 80, 26, "Lái ống\nkính"))
    o.append(ar(350, 73, 350, 140, color=INK))
    o.append(blk(300, 147, 90, 26, "Vị trí\nống kính"))
    o.append(ar(300, 160, 200, 160, color=INK))
    o.append(blk(140, 147, 70, 26, "So sánh"))
    o.append(ar(200, 160, 130, 160, color=INK))
    o.append(ar(140, 160, 140, 90, color=INK))
    return _f(o, 410, 190,
              "Hệ thống lấy nét tự động: cảm biến khoảng cách \u2192 vi xử lý \u2192 lái ống kính; vị trí ống kính phản hồi để so sánh đến khi không còn sai lệch.",
              "Automatic focusing system: the range sensor feeds the microprocessor which drives the lens; the lens position is fed back and compared until the error is zero.")


# =====================================================================
# Figure 7.47 - Washing machine system
# =====================================================================
def fig_7_47():
    o = []
    o.append(blk(20, 30, 80, 24, "Đồng hồ"))
    o.append(ar(100, 42, 130, 42))
    o.append(blk(20, 80, 80, 24, "Công tắc\ncửa"))
    o.append(ar(100, 92, 130, 92))
    o.append(blk(130, 50, 80, 40, "Vi xử lý\n+ chương trình"))
    o.append(ar(210, 70, 250, 70))
    o.append(blk(250, 57, 90, 26, "Cơ cấu\nchỉnh"))
    o.append(ar(340, 70, 370, 70))
    o.append(blk(370, 57, 80, 26, "Máy\ngiặt"))
    o.append(ar(360, 96, 280, 130, color=INK))
    o.append(blk(200, 130, 90, 40, "Cảm biến:\nmức / nhiệt\ntốc độ / cửa"))
    o.append(ar(200, 150, 130, 150, color=INK))
    o.append(ar(130, 150, 130, 90, color=INK))
    return _f(o, 470, 190,
              "Hệ thống máy giặt nhúng: vi xử lý theo chương trình điều khiển van, bơm, gia nhiệt, động cơ; các cảm biến mức/nhiệt/động cơ/cửa phản hồi.",
              "Embedded washing-machine system: a program-driven microprocessor controls valves, pump, heater and motor, with sensors for level, temperature, speed and door feeding back.")


# =====================================================================
# Figure 7.48 - Problem 5 (water level control block diagram)
# =====================================================================
def fig_7_48():
    o = []
    o.append(blk(20, 70, 80, 26, "Bộ điều\nkhiển Kp=10"))
    o.append(ar(100, 83, 140, 83))
    o.append(blk(140, 70, 80, 26, "Van (lưu\nlượng \u221d vào)"))
    o.append(ar(220, 83, 260, 83))
    o.append(blk(260, 70, 90, 26, "Bể chứa\nmức nước"))
    o.append(ar(350, 83, 350, 150, color=INK))
    o.append(blk(260, 147, 90, 26, "Đo mức"))
    o.append(ar(260, 160, 200, 160, color=INK))
    o.append(ar(200, 160, 141, 160, color=INK))
    o.append(ar(130, 160, 130, 96, color=INK))
    return _f(o, 410, 190,
              "Bài 5: hệ thống giữ mức nước không đổi bằng bộ điều khiển tỉ lệ Kp=10; van cho lưu lượng tỉ lệ với tín hiệu vào.",
              "Problem 5: a proportional controller Kp=10 holds the container level constant; the valve flow is proportional to the controller input.")


# =====================================================================
# Figure 7.49 - Problem 8 (error-time graph)
# =====================================================================
def fig_7_49():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (s)", "Sai lệch e"))
    o.append(_poly([m(0, 0.1), m(0.1, 0.6), m(0.45, 0.6), m(0.55, 0.2), m(0.9, 0.2), m(1, 0.5)],
                    color=BLUE, sw=1.7))
    o.append(tx(x0 + 40, y0 + 40, "Tín hiệu sai lệch\ncho bài 8", 6.5, color=GREY))
    return _f(o, 370, 230,
              "Bài 8: đồ thị sai lệch-thời gian cho trước, yêu cầu vẽ đồ thị đầu ra bộ điều khiển theo P, PD, PI.",
              "Problem 8: the given error-time graph for which the controller output is to be sketched for P, PD and PI modes.")


# =====================================================================
# Figure 7.50 - Problem 11 (process reaction curve)
# =====================================================================
def fig_7_50():
    o = []
    x0, y0, W, H = 50, 40, 270, 160
    m = gmap(x0, y0, W, H)
    o.append(gax(x0, y0, W, H, "Thời gian (phút)", "Đầu ra (%)"))
    pts = []
    for i in range(0, 121):
        t = i / 120.0
        v = 0.05 + 0.9 / (1 + math.exp(-7 * (t - 0.45)))
        pts.append(m(t, v))
    o.append(_poly(pts, color=BLUE, sw=1.7))
    x1, y1 = m(0.28, 0.05)
    x2, y2 = m(0.62, 0.05 + 0.9 * (1 / (1 + math.exp(-7 * (0.62 - 0.45))) - 1 / (1 + math.exp(-7 * (0.28 - 0.45)))))
    o.append(ln2(x1, y1, x2, y2, color=RED, dash="4 3"))
    o.append(tx(x0 + 60, y0 + 120, "Dốc R, độ trễ L", 6.5, color=GREY))
    return _f(o, 370, 230,
              "Bài 11: đáp ứng vòng hở với bậc đơn vị của quá trình; dùng đường đặc tuyến để tìm thiết lập PID (Ziegler-Nichols).",
              "Problem 11: the open-loop unit-step response; the process reaction curve is used to find the PID settings by Ziegler-Nichols.")


# =====================================================================
# Figure 7.51 - Problem 14 (liquid level control block diagram)
# =====================================================================
def fig_7_51():
    o = []
    o.append(blk(20, 70, 80, 26, "Giá trị đặt"))
    o.append(ar(100, 83, 120, 83))
    o.append(sumj(130, 83))
    o.append(ar(141, 83, 170, 83))
    o.append(blk(170, 60, 90, 24, "(s+0.5)/\n(0.2s+1)"))
    o.append(ar(260, 72, 300, 72))
    o.append(blk(300, 60, 90, 24, "1/s"))
    o.append(ar(390, 72, 430, 72))
    o.append(tx(440, 75, "Mức", 7))
    o.append(ar(430, 86, 430, 140, color=INK))
    o.append(ar(430, 150, 200, 150, color=INK))
    o.append(blk(130, 137, 70, 26, "Đo mức"))
    o.append(ar(200, 150, 141, 150, color=INK))
    o.append(ar(130, 150, 130, 96, color=INK))
    return _f(o, 470, 180,
              "Bài 14: điều khiển mức chất lỏng với bộ điều khiển (s+0.5)/(0.2s+1) và quá trình 1/s, phản hồi đo mức; tìm cách đầu ra biến thiên theo thời gian.",
              "Problem 14: liquid-level control with controller (s+0.5)/(0.2s+1) and plant 1/s, level feedback; determine how the output varies with time.")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
