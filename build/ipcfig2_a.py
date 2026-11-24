# -*- coding: utf-8 -*-
from ipcfig2_common import (make_registry, T, _b, _ar, _frame, _series,
                            _legend, _wavey, _mk, _defs, _line, _circle,
                            _rect, _ellipse, _path, _poly, BLUE, GREEN, GREY, INK, RED)
FIGS, _reg = make_registry()

import math


def _zig(x1, y1, x2, y2, n=6, amp=3.0, color=INK, sw=1.0):
    """A zig-zag resistor or spring segment between two points."""
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / length, dx / length
    pts = [(x1, y1)]
    for i in range(1, 2 * n):
        t = i / (2.0 * n)
        s = amp if i % 2 else -amp
        pts.append((x1 + dx * t + nx * s, y1 + dy * t + ny * s))
    pts.append((x2, y2))
    return _poly(pts, sw=sw, color=color)


def _dial(cx, cy, r, labels, vmax=100.0, pointer=None):
    """A round gage dial with a 270-degree scale."""
    o = [_circle(cx, cy, r, fill="#fbfaf7", sw=1.4),
         _circle(cx, cy, r * 0.87, fill="none", sw=0.6, color=GREY)]
    for i in range(51):
        a = math.radians(225 - 270 * i / 50.0)
        r1 = r * (0.70 if i % 5 == 0 else 0.76)
        r2 = r * 0.84
        o.append(_line(cx + r1 * math.cos(a), cy - r1 * math.sin(a),
                       cx + r2 * math.cos(a), cy - r2 * math.sin(a),
                       sw=1.0 if i % 5 == 0 else 0.5))
    for text, val in labels:
        a = math.radians(225 - 270 * val / vmax)
        o.append(T(cx + r * 0.56 * math.cos(a),
                   cy - r * 0.56 * math.sin(a) + r * 0.07,
                   text, r * 0.17))
    if pointer is not None:
        a = math.radians(225 - 270 * pointer / vmax)
        o.append(_line(cx, cy, cx + r * 0.63 * math.cos(a),
                       cy - r * 0.63 * math.sin(a), sw=2.2, color=RED))
        o.append(_circle(cx, cy, 3.0, fill=INK, sw=0))
    return "".join(o)


# ---------------------------------------------------------------- 2.1
@_reg
def fig_f01():
    """Fig. 2.1 - Basic instrumentation system."""
    o = [_defs()]
    o.append(_b(92, 62, 64, 40, "Final\ncontrol\nelement", size=6.8))
    o.append(_b(250, 62, 80, 40, "Process", size=8.0))
    o.append(_b(430, 62, 80, 40, "Transmitter", size=7.6))
    o.append(T(52, 76, "Process", 6.8))
    o.append(T(52, 86, "flow in", 6.8))
    o.append(_ar(70, 82, 92, 82))
    o.append(_ar(156, 82, 250, 82))
    o.append(_ar(330, 82, 430, 82))
    o.append(_ar(510, 82, 568, 82))
    o.append(T(610, 78, "Process flow out", 6.8))
    o.append(T(290, 28, "Process disturbances", 7.2))
    o.append(_ar(290, 32, 290, 62))
    o.append(_ar(470, 102, 470, 130))
    o.append(_line(290, 130, 520, 130, sw=1.2))
    o.append(_ar(290, 130, 290, 152))
    o.append(_ar(520, 130, 520, 152))
    o.append(_b(250, 152, 80, 38, "Controller", size=7.8))
    o.append(_b(466, 152, 108, 38, "Indicator/Recorder", size=7.4))
    o.append(T(290, 210, "Set value of the process", 7.0))
    o.append(_ar(290, 206, 290, 190))
    o.append(_line(250, 171, 124, 171, sw=1.3))
    o.append(_ar(124, 171, 124, 102))
    return _mk(1, o, "Figure 2.1 - Basic instrumentation system",
               "So do khong che co ban: dau vao di qua phan tu dieu khiet cuoi, qua trinh, bo phat tin hien thi/ ghi va bo dieu khien co phan hoi",
               "Basic instrumentation system: process flow through final control element, process, transmitter, indicator/recorder and feedback controller",
               "So do khoi he thong dieu khiet co ban voi duong phan hoi tu bo phat tin den bo dieu khien",
               "Block diagram of a basic instrumentation loop with transmitter, controller and feedback path")


# ---------------------------------------------------------------- 2.2
@_reg
def fig_f02():
    """Fig. 2.2 - Quarter amplitude decay response."""
    o = [_defs()]
    fr, mx, my = _frame(96, 32, 430, 158, (0, 10), (0, 10),
                        [(0, "0"), (5, "5"), (10, "10")],
                        [(0, "0"), (5, "5"), (10, "10")],
                        "Time", "Controlled variable")
    o.append(fr)
    o.append(_line(96, my(5), 526, my(5), dash="5,3", color=GREY))
    pts = []
    for i in range(301):
        t = 10.0 * i / 300.0
        v = 5.0 + 3.0 * math.exp(-0.308 * t) * math.sin(2 * math.pi * t / 4.5)
        pts.append((t, v))
    o.append(_series(pts, mx, my, BLUE, dot=0))
    t1 = 1.125
    t2 = t1 + 4.5
    v1 = 5.0 + 3.0 * math.exp(-0.308 * t1)
    v2 = 5.0 + 3.0 * math.exp(-0.308 * t2)
    o.append(_line(mx(t1), my(5), mx(t1), my(v1), dash="3,2", color=GREY))
    o.append(_line(mx(t2), my(5), mx(t2), my(v2), dash="3,2", color=GREY))
    o.append(T(mx(t1) + 6, my((5 + v1) / 2.0), "x", 8.0, color=RED))
    o.append(T(mx(t2) + 6, my((5 + v2) / 2.0), "y", 8.0, color=RED))
    o.append(T(mx(7.1), my(1.9), "x / y = 1/4", 8.0, color=INK))
    return _mk(2, o, "Figure 2.2 - Amplitude decay response",
               "Dap ung phan rong bien do mot phan tu: dao dong gat dan ve gia tri dat",
               "Quarter-amplitude decay response: a damped oscillation settling at the set value",
               "Bieu do dao dong gat dan theo thoi gian voi ty le bien do x/y bang 1/4",
               "Damped oscillation curve with two successive peak amplitudes in ratio one to four")


# ---------------------------------------------------------------- 2.3
@_reg
def fig_f03():
    """Fig. 2.3 - Control valve characteristics."""
    o = [_defs()]
    fr, mx, my = _frame(96, 28, 420, 160, (0, 100), (0, 100),
                        [(0, "0"), (70, "70%"), (100, "100%")],
                        [(0, "0"), (70, "70%"), (100, "100%")],
                        "% Opening", "% Flow")
    o.append(fr)
    o.append(_line(96, my(70), 516, my(70), dash="5,3", color=GREY))
    xs = [i * 2.0 for i in range(51)]
    linear = [(x, x) for x in xs]
    quick = [(x, 100.0 * (1.0 - (1.0 - x / 100.0) ** 4)) for x in xs]
    equal = [(x, 100.0 * (math.exp(3.0 * x / 100.0) - 1.0) /
              (math.exp(3.0) - 1.0)) for x in xs]
    o.append(_series(quick, mx, my, RED, dot=0))
    o.append(_series(linear, mx, my, BLUE, dot=0))
    o.append(_series(equal, mx, my, GREEN, dot=0))
    o.append(_legend([(RED, "Quick opening valve"),
                      (BLUE, "Linear valve"),
                      (GREEN, "Equal percentage valve")], 534, 54, w=136))
    return _mk(3, o, "Figure 2.3 - Control valve characteristics",
               "Dac tinh van dieu khiet: luong chay phan tram theo do mo van cho ba loai van",
               "Control valve characteristics: percent flow versus percent opening for three valve types",
               "Do thi ba duong dac tinh luong chay theo do mo cua van thang, van mo nhanh va van ty le bang",
               "Chart with linear, quick-opening and equal-percentage flow curves on percent axes")


# ---------------------------------------------------------------- 2.4
@_reg
def fig_f04():
    """Fig. 2.4 - Four auto/manual loading stations."""
    o = [_defs()]
    o.append(T(340, 22, "Set value", 7.2))
    o.append(_ar(340, 26, 340, 46))
    o.append(T(228, 68, "Process", 7.0))
    o.append(T(228, 78, "variable", 7.0))
    o.append(_ar(276, 74, 314, 74))
    o.append(_circle(340, 74, 26, fill="#eef3fb", sw=1.3))
    o.append(T(340, 77, "Controller", 7.2))
    o.append(T(396, 66, "Controller", 7.0))
    o.append(T(340, 106, "Output", 7.2))
    o.append(_ar(340, 100, 340, 120))
    o.append(_line(124, 120, 574, 120, sw=1.3))
    for x in (124, 274, 424, 574):
        o.append(_line(x, 120, x, 136, sw=1.2))
        o.append(_rect(x - 24, 136, 48, 48, fill="#eef3fb", sw=1.2))
        o.append(_line(x - 24, 136, x + 24, 184, sw=0.8, color=GREY))
        o.append(T(x - 14, 152, "A", 8.0))
        o.append(T(x + 14, 174, "M", 8.0))
    o.append(T(636, 152, "Auto/Manual", 6.8))
    o.append(T(636, 162, "loading station", 6.8))
    o.append(_ar(124, 184, 124, 210))
    o.append(T(100, 222, "To final control element 1", 6.6))
    for i, x in enumerate((274, 424, 574), start=2):
        o.append(_line(x, 184, x, 204, dash="3,3", color=GREY))
        o.append(_ar(x, 200, x, 208, color=GREY, sw=1.2))
        o.append(T(x, 220, str(i), 7.2))
    return _mk(4, o, "Figure 2.4 - Four auto/manual loading stations",
               "Bon tram tai tu dong/ thu cong duoc noi chung de dieu khien bon phan tu cuoi doc lap",
               "Four auto/manual loading stations linked to operate four independent final control elements",
               "So do bo dieu khien chia tin hieu xuong bon tram tu dong thu cong va bon phan tu dieu khiet cuoi",
               "Controller output bus feeding four A/M stations and four numbered final control elements")


# ---------------------------------------------------------------- 2.5
@_reg
def fig_f05():
    """Fig. 2.5 - Air set (air filter/regulator)."""
    o = [_defs()]
    o.append(_poly([(256, 72), (424, 72), (372, 190), (308, 190)],
                   fill="#eef3fb", sw=1.5, close=True))
    o.append(_ellipse(340, 64, 22, 6, fill="#dbe6f3", sw=1.2))
    o.append(_line(340, 70, 340, 72, sw=1.0))
    o.append(T(398, 58, "Regulating knob", 7.0))
    o.append(_line(398, 60, 362, 64, sw=0.8, color=GREY))
    o.append(_circle(340, 118, 24, fill="#ffffff", sw=1.2))
    for i in range(13):
        a = math.radians(200 - 220 * i / 12.0)
        o.append(_line(340 + 17 * math.cos(a), 118 - 17 * math.sin(a),
                       340 + 21 * math.cos(a), 118 - 21 * math.sin(a),
                       sw=0.6, color=GREY))
    o.append(_ar(340, 118, 354, 106, color=RED, sw=1.4))
    o.append(T(246, 108, "Output pressure", 6.8))
    o.append(T(246, 118, "gage", 6.8))
    o.append(_ar(294, 114, 316, 114))
    o.append(_rect(330, 190, 20, 12, fill="#dbe6f3", sw=1.2))
    o.append(_line(330, 202, 350, 202, sw=1.2))
    o.append(T(400, 200, "Drain cock", 7.0))
    o.append(_line(398, 197, 352, 196, sw=0.8, color=GREY))
    o.append(_ar(256, 92, 224, 92, color=GREEN))
    o.append(T(204, 94, "Air in", 6.6))
    return _mk(5, o, "Figure 2.5 - Air set (air filter/regulator)",
               "Bo loc va dieu ap khi: nut chinh ap, dong ho ap suat dau ra va van xa",
               "Air set combining a filter and regulator, with regulating knob, output gage and drain cock",
               "So do bo loc dieu ap khi co nut dieu chinh, dong ho ap suat dau ra va van xa day",
               "Trapezoidal air filter-regulator body with top knob, face gage and bottom drain")


# ---------------------------------------------------------------- 2.6
@_reg
def fig_f06():
    """Fig. 2.6 - U-tube manometer."""
    o = [_defs()]
    o.append(_path("M 286 58 L 286 150 A 54 54 0 0 0 394 150 L 394 58", sw=1.4))
    o.append(_path("M 298 58 L 298 150 A 42 42 0 0 0 382 150 L 382 58", sw=1.0))
    o.append(_path("M 292 128 L 292 150 A 48 48 0 0 0 388 150 L 388 92",
                   sw=10, color="#bcd8ee"))
    for yy in range(132, 151, 8):
        o.append(_line(287, yy, 297, yy, sw=0.5, color=BLUE))
    for yy in range(96, 151, 8):
        o.append(_line(383, yy, 393, yy, sw=0.5, color=BLUE))
    o.append(_line(286, 128, 298, 128, sw=1.4, color=BLUE))
    o.append(_line(382, 92, 394, 92, sw=1.4, color=BLUE))
    o.append(_line(248, 128, 286, 128, dash="4,3", color=GREY))
    o.append(_line(248, 92, 382, 92, dash="4,3", color=GREY))
    o.append(_ar(258, 124, 258, 96, color=GREY, sw=1.2))
    o.append(_ar(258, 96, 258, 124, color=GREY, sw=1.2))
    o.append(T(246, 112, "h", 8.0))
    o.append(T(292, 28, "Pressure", 7.0))
    o.append(T(292, 38, "P1", 7.0))
    o.append(_ar(292, 42, 292, 58))
    o.append(T(470, 72, "Open to atmosphere", 7.0))
    o.append(T(470, 82, "(P2)", 7.0))
    o.append(_line(398, 62, 462, 70, sw=0.8, color=GREY))
    o.append(_ar(388, 50, 388, 58))
    o.append(T(488, 140, "Manometer liquid (rho)", 7.0))
    o.append(_line(398, 136, 480, 137, sw=0.8, color=GREY))
    o.append(T(340, 212, "P = rho*h", 8.2))
    o.append(T(340, 228, "(P1 - P2) = rho*h", 8.2))
    return _mk(6, o, "Figure 2.6 - U-tube manometer",
               "Ong chinh U: chenh lech muc chat long h cho biet ap suat P1 tru P2",
               "U-tube manometer: the difference in liquid levels h measures the pressure difference P1 - P2",
               "Ong U hai canh co chat long, canh trai chiu ap suat P1, canh phai mo tuong dung P2",
               "U-tube with two liquid levels, pressure input on one leg and atmosphere on the other")


# ---------------------------------------------------------------- 2.7
@_reg
def fig_f07():
    """Fig. 2.7 - Well-type manometer."""
    o = [_defs()]
    o.append(_rect(150, 90, 180, 80, fill="#ffffff", sw=1.4))
    o.append(_rect(152, 140, 176, 28, fill="#dbe8f5", sw=0))
    for yy in (145, 152, 159, 166):
        o.append(_line(154, yy, 326, yy, sw=0.6, color=BLUE))
    o.append(_rect(330, 160, 80, 10, fill="#dbe8f5", sw=0.8, stroke=BLUE))
    o.append(_rect(410, 56, 20, 114, fill="#ffffff", sw=1.3))
    o.append(_rect(412, 82, 16, 88, fill="#dbe8f5", sw=0))
    for yy in range(88, 170, 8):
        o.append(_line(412, yy, 428, yy, sw=0.5, color=BLUE))
    o.append(T(240, 54, "Pressure", 7.0))
    o.append(T(240, 64, "P1", 7.0))
    o.append(_ar(240, 68, 240, 90))
    o.append(T(452, 48, "P2", 7.2))
    o.append(_ar(420, 42, 420, 56))
    o.append(T(104, 112, "Well", 7.2))
    o.append(_ar(134, 114, 148, 114))
    o.append(T(94, 190, "Manometer liquid", 7.0))
    o.append(_line(160, 186, 220, 152, sw=0.8, color=GREY))
    o.append(_rect(438, 58, 14, 110, fill="#ffffff", sw=1.0))
    for i in range(12):
        yy = 64 + i * 9
        o.append(_line(438, yy, 447 if i % 2 == 0 else 443, yy, sw=0.6, color=GREY))
    o.append(T(556, 100, "Direct", 7.0))
    o.append(T(556, 110, "measurement", 7.0))
    o.append(T(556, 120, "scale", 7.0))
    o.append(_line(452, 100, 518, 105, sw=0.8, color=GREY))
    return _mk(7, o, "Figure 2.7 - Well-type manometer",
               "Ong do kieu be chua: ap suat tac dung len be chua, muc doc tren canh do duoc doc truc tiep",
               "Well-type manometer: pressure applied to a large well, with a direct reading scale on the narrow leg",
               "Be chua lon va ong do hep co thang doc truc tiep, ap suat P1 vao be chua va P2 o dau ong",
               "Large well connected to a narrow graduated leg with direct measurement scale")


# ---------------------------------------------------------------- 2.8
@_reg
def fig_f08():
    """Fig. 2.8 - Inclined manometer."""
    o = [_defs()]
    o.append(_rect(170, 92, 150, 78, fill="#ffffff", sw=1.4))
    o.append(_rect(172, 136, 146, 32, fill="#dbe8f5", sw=0))
    for yy in (142, 150, 158, 166):
        o.append(_line(174, yy, 316, yy, sw=0.6, color=BLUE))
    o.append(T(244, 56, "Pressure", 7.0))
    o.append(T(244, 66, "P1", 7.0))
    o.append(_ar(244, 70, 244, 92))
    o.append(_poly([(318, 146), (498, 56), (502, 64), (322, 154)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_line(320, 152, 448, 90, sw=8, color="#bcd8ee"))
    o.append(_line(318, 146, 498, 56, sw=0.9))
    o.append(_line(322, 154, 502, 64, sw=0.9))
    o.append(T(520, 42, "P2", 7.2))
    o.append(_ar(506, 50, 496, 58))
    o.append(_line(170, 136, 450, 136, dash="4,3", color=GREY))
    o.append(_line(440, 90, 512, 90, dash="4,3", color=GREY))
    o.append(_ar(470, 132, 470, 94, color=GREY, sw=1.2))
    o.append(_ar(470, 94, 470, 132, color=GREY, sw=1.2))
    o.append(T(480, 116, "h", 8.0))
    o.append(_ar(326, 156, 440, 98, color=GREEN, sw=1.2))
    o.append(T(392, 130, "hx", 7.6, color=GREEN))
    o.append(_line(320, 168, 356, 168, dash="4,3", color=GREY))
    o.append(_path("M 320 168 A 34 34 0 0 0 350 153", sw=1.0, color=INK))
    o.append(T(352, 168, "theta", 7.4))
    o.append(T(340, 214, "h = hx sin(theta)", 8.2))
    return _mk(8, o, "Figure 2.8 - Inclined manometer",
               "Ong do nghieng: do dich chuyen thang dang h bang hx nhan sin theta, do ap thap chinh xac hon",
               "Inclined manometer: vertical displacement h equals hx times sin(theta), improving low-pressure resolution",
               "Be chua noi ong nghieng mot goc theta, h la do cao thang dang va hx la quang duong chat long di",
               "Reservoir and slanted tube with angle theta, travel hx and vertical rise h")


# ---------------------------------------------------------------- 2.9
@_reg
def fig_f09():
    """Fig. 2.9 - External view of pressure gage."""
    o = [_defs()]
    o.append(_dial(340, 112, 86,
                   [("0", 0), ("20", 20), ("40", 40),
                    ("60", 60), ("80", 80), ("100", 100)],
                   pointer=60))
    o.append(T(340, 154, "Kg/cm2", 8.0))
    o.append(T(340, 166, "Pressure", 7.4))
    o.append(_rect(330, 198, 20, 34, fill="#eef3fb", sw=1.2))
    for yy in (218, 222, 226):
        o.append(_line(330, yy, 350, yy, sw=0.5, color=GREY))
    o.append(T(148, 214, "External view", 6.8))
    o.append(T(148, 224, "of pressure gage", 6.8))
    o.append(_line(220, 216, 300, 190, sw=0.8, color=GREY))
    return _mk(9, o, "Figure 2.9 - External view of pressure gage",
               "Nhin ngoai cua dong ho ap suat: mat so 0 den 100 kg/cm2 va kim chi thi",
               "External view of a Bourdon pressure gage with a 0 to 100 kg/cm2 dial and pointer",
               "Mat dong ho ap suat tron co thang do 0-100 kg/cm2, kim va dau noi ren o phia duoi",
               "Circular pressure gage face marked 0 to 100 kg/cm2 with a pointer and threaded stem")


# ---------------------------------------------------------------- 2.10
@_reg
def fig_f10():
    """Fig. 2.10 - Internal view of pressure gage."""
    o = [_defs()]
    o.append(_path("M 250 192 A 90 90 0 1 1 430 192", sw=1.5))
    o.append(_path("M 402 158 A 66 66 0 1 1 393 72", sw=2.0, color=BLUE))
    o.append(_rect(388, 66, 12, 8, fill="#dbe6f3", sw=1.0))
    o.append(_line(393, 74, 378, 104, sw=1.4, color=INK))
    o.append(_poly([(362, 100), (386, 108), (372, 124)],
                   fill="#dbe6f3", sw=1.0, close=True))
    o.append(_circle(340, 116, 11, fill="#ffffff", sw=1.4))
    for i in range(12):
        a = 2 * math.pi * i / 12.0
        o.append(_line(340 + 11 * math.cos(a), 116 + 11 * math.sin(a),
                       340 + 13 * math.cos(a), 116 + 13 * math.sin(a),
                       sw=0.6, color=GREY))
    o.append(_ar(340, 116, 296, 76, color=RED, sw=1.6))
    o.append(_path("M 344 110 C 352 104 354 118 342 121 C 330 123 328 110 340 106",
                   sw=0.9, color=GREY))
    o.append(_path("M 252 178 A 84 84 0 0 1 300 132", sw=1.0, color=GREY))
    for i, val in enumerate(("0", "10", "20", "30")):
        a = math.radians(205 - 55 * i / 3.0)
        r1, r2 = 78, 86
        o.append(_line(340 + r1 * math.cos(a), 116 - r1 * math.sin(a),
                       340 + r2 * math.cos(a), 116 - r2 * math.sin(a), sw=0.8))
        o.append(T(340 + 70 * math.cos(a), 116 - 70 * math.sin(a) + 2,
                   val, 6.6, color=GREY))
    o.append(_rect(330, 192, 20, 40, fill="#eef3fb", sw=1.2))
    o.append(_line(320, 232, 360, 232, sw=1.4))
    for xx in range(322, 360, 6):
        o.append(_line(xx, 232, xx + 5, 237, sw=0.5, color=GREY))
    o.append(T(500, 50, "Free end", 6.8))
    o.append(T(500, 60, "of bourdon", 6.8))
    o.append(_line(498, 58, 402, 70, sw=0.8, color=GREY))
    o.append(T(498, 112, "Connecting link", 6.8))
    o.append(_line(496, 110, 384, 92, sw=0.8, color=GREY))
    o.append(T(484, 160, "Sector-Pinion", 6.8))
    o.append(T(484, 170, "assembly", 6.8))
    o.append(_line(482, 160, 382, 118, sw=0.8, color=GREY))
    o.append(T(404, 38, "Spring", 6.8))
    o.append(_line(402, 42, 348, 106, sw=0.8, color=GREY))
    return _mk(10, o, "Figure 2.10 - Internal view of pressure gage",
               "Ben trong dong ho: ong Bourdon hinh C, lien ket, bo banh rang va loxo can bang",
               "Internal view of a pressure gage showing the C-type Bourdon tube, link, sector-pinion and hairspring",
               "Ong Bourdon hinh C co dau tu do noi voi lien ket toi bo banh rang, kim chi thang do va loxo",
               "Cutaway mechanism with C-shaped Bourdon tube, connecting link, toothed sector and pointer")


# ---------------------------------------------------------------- 2.11
@_reg
def fig_f11():
    """Fig. 2.11 - Slack diaphragm low-range gage."""
    o = [_defs()]
    o.append(_rect(190, 82, 220, 78, fill="#ffffff", sw=1.3))
    o.append(T(300, 54, "Process pressure in", 7.0))
    o.append(_ar(300, 58, 300, 82))
    o.append(T(140, 98, "Restraining", 6.8))
    o.append(T(140, 108, "spring", 6.8))
    o.append(_line(206, 106, 292, 94, sw=0.8, color=GREY))
    o.append(_zig(300, 82, 300, 126, n=6, amp=5, color=BLUE))
    o.append(_poly(_wavey(196, 130, 4, 11, step=11), sw=1.2, color=BLUE))
    o.append(T(440, 116, "Slack diaphragm", 6.8))
    o.append(_line(438, 114, 332, 130, sw=0.8, color=GREY))
    o.append(_line(300, 130, 300, 178, sw=1.2))
    o.append(_circle(300, 178, 3, fill=INK, sw=0))
    o.append(_ar(300, 178, 252, 190, color=RED, sw=1.4))
    o.append(_path("M 226 200 A 46 46 0 0 1 252 176", sw=1.0, color=GREY))
    for i in range(7):
        a = math.radians(190 - 10 * i)
        o.append(_line(250 + 44 * math.cos(a), 190 - 44 * math.sin(a),
                       250 + 50 * math.cos(a), 190 - 50 * math.sin(a),
                       sw=0.6, color=GREY))
    o.append(T(160, 196, "Pointer", 6.6))
    o.append(T(160, 206, "and scale", 6.6))
    o.append(_line(216, 198, 244, 194, sw=0.8, color=GREY))
    return _mk(11, o, "Figure 2.11 - Slack diaphragm low-range gage",
               "Dong ho do ap thap dung mang chao long va loxo gioi han, co kim va thang do",
               "Low-range gage using a slack diaphragm balanced by a restraining spring, with pointer and scale",
               "Buong do co mang chao long o giua, loxo gioi han phia tren, kim chi thi va thang do cong",
               "Slack diaphragm separating two chambers with restraining spring, pointer and curved scale")


# ---------------------------------------------------------------- 2.12
@_reg
def fig_f12():
    """Fig. 2.12 - Absolute pressure gage with evacuated capsules."""
    o = [_defs()]
    o.append(_rect(180, 78, 240, 92, fill="#ffffff", sw=1.4))
    o.append(_ellipse(272, 100, 48, 8, fill="#eef3fb", sw=1.1))
    o.append(_ellipse(272, 122, 48, 8, fill="#eef3fb", sw=1.1))
    o.append(T(108, 88, "Evacuated", 6.8))
    o.append(T(108, 98, "capsules", 6.8))
    o.append(_line(164, 96, 224, 98, sw=0.8, color=GREY))
    o.append(T(108, 140, "Airtight", 6.8))
    o.append(T(108, 150, "chamber", 6.8))
    o.append(_line(164, 146, 180, 146, sw=0.8, color=GREY))
    o.append(_line(320, 110, 420, 110, sw=1.2))
    o.append(_zig(420, 110, 452, 110, n=5, amp=4, color=BLUE))
    o.append(_ar(452, 110, 486, 96, color=RED, sw=1.4))
    o.append(_path("M 484 90 A 44 44 0 0 1 500 132", sw=1.0, color=GREY))
    o.append(T(520, 150, "Pointer and", 6.6))
    o.append(T(520, 160, "scale", 6.6))
    o.append(T(300, 206, "Process pressure in", 7.0))
    o.append(_ar(300, 202, 300, 170))
    return _mk(12, o, "Figure 2.12 - Absolute pressure gage",
               "Hop kin va cac nang chua chan khong: ap suat do la ap suat tuyet doi cua chat long",
               "Absolute pressure gage with evacuated capsules sealed inside an airtight chamber",
               "Cac nang chua chan khong dat trong hop kin, chat long vao tu duoi va kim chi ap suat tuyet doi",
               "Airtight chamber containing evacuated capsules connected to a pointer and scale")


# ---------------------------------------------------------------- 2.13
@_reg
def fig_f13():
    """Fig. 2.13 - Twin-bellows absolute pressure gage."""
    o = [_defs()]
    o.append(T(178, 118, "Evacuated", 6.8))
    o.append(_ar(226, 120, 250, 120))
    o.append(_poly([(252, 82), (270, 88), (252, 94), (270, 100),
                    (252, 106), (270, 112), (252, 118), (270, 124),
                    (252, 130), (270, 136), (252, 142), (270, 148),
                    (252, 154), (270, 154)], sw=1.2, color=INK))
    o.append(_line(252, 82, 252, 154, sw=1.0))
    o.append(_poly([(404, 82), (388, 88), (404, 94), (388, 100),
                    (404, 106), (388, 112), (404, 118), (388, 124),
                    (404, 130), (388, 136), (404, 142), (388, 148),
                    (404, 154), (388, 154)], sw=1.2, color=INK))
    o.append(_line(404, 82, 404, 154, sw=1.0))
    o.append(T(396, 56, "Process", 6.8))
    o.append(T(396, 66, "pressure in", 6.8))
    o.append(_ar(396, 70, 396, 82))
    o.append(_line(262, 154, 262, 168, sw=1.1))
    o.append(_line(262, 168, 394, 168, sw=1.1))
    o.append(_line(394, 154, 394, 168, sw=1.1))
    o.append(_ar(328, 168, 280, 202, color=RED, sw=1.4))
    o.append(_path("M 254 212 A 46 46 0 0 1 282 194", sw=1.0, color=GREY))
    for i in range(7):
        a = math.radians(195 - 10 * i)
        o.append(_line(276 + 44 * math.cos(a), 208 - 44 * math.sin(a),
                       276 + 50 * math.cos(a), 208 - 50 * math.sin(a),
                       sw=0.6, color=GREY))
    o.append(T(330, 222, "Pointer and scale", 6.8))
    return _mk(13, o, "Figure 2.13 - Twin-bellows absolute pressure gage",
               "He thong hai ong phoi: mot ong chua chan khong, mot ong nhan ap suat, hieu chuyen dong cho ap tuyet doi",
               "Absolute pressure gage using twin bellows, one evacuated and one receiving process pressure",
               "Hai ong phoi dat canh nhau, mot ong chan khong va mot ong dap ap suat, kim chi ap suat tuyet doi",
               "Two opposed bellows, one evacuated and one pressurized, driving a differential pointer")


# ---------------------------------------------------------------- 2.14
@_reg
def fig_f14():
    """Fig. 2.14 - Diaphragm gage."""
    o = [_defs()]
    o.append(_dial(232, 92, 54, [], pointer=58))
    o.append(_rect(168, 158, 128, 7, fill="#eef3fb", sw=1.2))
    o.append(_rect(168, 170, 128, 7, fill="#eef3fb", sw=1.2))
    o.append(_line(168, 165, 296, 165, sw=1.4, color=BLUE))
    o.append(_line(232, 148, 232, 158, sw=1.1))
    for xx in (176, 288):
        o.append(_circle(xx, 161, 2.4, fill=INK, sw=0))
    o.append(_rect(224, 177, 16, 14, fill="#dbe6f3", sw=1.0))
    o.append(T(340, 154, "Flange", 6.8))
    o.append(T(340, 164, "connection", 6.8))
    o.append(_line(338, 158, 296, 161, sw=0.8, color=GREY))
    o.append(T(340, 184, "Diaphragm", 6.8))
    o.append(_line(338, 181, 296, 165, sw=0.8, color=GREY))
    o.append(T(334, 206, "Nipple for socket weld", 6.8))
    o.append(_line(332, 202, 242, 184, sw=0.8, color=GREY))
    o.append(T(232, 226, "Diaphragm gage", 7.4, color=INK))
    return _mk(14, o, "Figure 2.14 - Diaphragm gage",
               "Dong ho mang co ket noi mat bich: mang ngan cach chat long va bo phan cam nhan",
               "Diaphragm gage with flange connection and socket-weld nipple isolating the sensing element",
               "Dong ho co mang ngan cach dua giua mat bich va dau noi han o, day chat long truyen ap len ong Bourdon",
               "Gage above a flanged diaphragm seal with a socket-weld nipple underneath")


# ---------------------------------------------------------------- 2.15
@_reg
def fig_f15():
    """Fig. 2.15 - Volumetric seal gage."""
    o = [_defs()]
    o.append(_circle(452, 82, 5, fill="#ffffff", sw=1.0))
    o.append(_circle(396, 100, 4, fill="#ffffff", sw=1.0))
    o.append(_circle(508, 100, 4, fill="#ffffff", sw=1.0))
    o.append(_dial(452, 100, 46, [], pointer=70))
    o.append(_line(452, 146, 452, 158, sw=1.2))
    o.append(_path("M 452 158 C 430 150 410 172 388 160 C 370 150 356 166 342 158",
                   sw=1.4, color=BLUE))
    o.append(_rect(300, 134, 7, 48, fill="#eef3fb", sw=1.2))
    o.append(_rect(322, 134, 7, 48, fill="#eef3fb", sw=1.2))
    o.append(_line(307, 158, 322, 158, sw=1.6, color=BLUE))
    o.append(T(532, 122, "Fixing", 6.6))
    o.append(T(532, 132, "arrangement", 6.6))
    o.append(_line(530, 124, 510, 102, sw=0.8, color=GREY))
    o.append(T(390, 190, "Capillary", 6.8))
    o.append(T(268, 170, "Diaphragm", 6.8))
    o.append(_line(264, 168, 300, 160, sw=0.8, color=GREY))
    o.append(T(266, 200, "Flange", 6.8))
    o.append(_line(262, 196, 300, 178, sw=0.8, color=GREY))
    o.append(T(340, 226, "Volumetric seal gage", 7.4))
    return _mk(15, o, "Figure 2.15 - Volumetric seal gage",
               "Dong ho co day mao dan va mang ngan cach, cho phep dat xa diem do va giam rung",
               "Volumetric seal gage using a capillary tube between the diaphragm seal and the gage element",
               "Dong ho duoc noi voi mang ngan cach qua ong mao dan, co ba tai dinh vi va mat bich",
               "Remote gage connected by a coiled capillary to a flanged diaphragm seal")


# ---------------------------------------------------------------- 2.16
@_reg
def fig_f16():
    """Fig. 2.16 - Pneumatic pressure transmitter."""
    o = [_defs()]
    o.append(T(500, 30, "Air supply", 7.0))
    o.append(_ar(498, 34, 452, 34, color=GREEN))
    o.append(_rect(392, 28, 56, 11, fill="#eef3fb", sw=1.1))
    o.append(T(392, 20, "Restriction", 6.8))
    o.append(_rect(404, 50, 44, 40, fill="#eef3fb", sw=1.1))
    o.append(T(462, 62, "Relay", 7.0))
    o.append(_line(420, 39, 420, 50, sw=1.1))
    o.append(_line(448, 39, 448, 50, sw=1.1))
    o.append(_path("M 420 68 L 300 68 L 300 90", sw=1.2, color=GREEN))
    o.append(_rect(288, 90, 26, 8, fill="#dbe6f3", sw=1.0))
    o.append(T(206, 86, "Flapper", 6.8))
    o.append(T(206, 96, "nozzle system", 6.8))
    o.append(_line(264, 92, 288, 92, sw=0.8, color=GREY))
    o.append(_line(448, 70, 476, 70, sw=1.1))
    o.append(T(500, 70, "Output", 7.0))
    o.append(_line(476, 74, 476, 120, sw=1.1, color=BLUE))
    o.append(_line(476, 120, 448, 120, sw=1.1, color=BLUE))
    o.append(T(500, 132, "Calibration", 6.8))
    o.append(T(500, 142, "adjustment (span)", 6.8))
    o.append(_zig(414, 120, 448, 120, n=5, amp=4, color=BLUE))
    o.append(_line(448, 120, 452, 152, sw=1.0, color=BLUE))
    o.append(_zig(412, 154, 450, 154, n=5, amp=5, color=GREEN))
    o.append(T(494, 166, "Feedback", 6.8))
    o.append(T(494, 176, "bellows", 6.8))
    o.append(_line(490, 166, 452, 156, sw=0.8, color=GREY))
    o.append(_path("M 300 98 L 300 172", sw=1.2))
    o.append(T(208, 172, "Seal", 6.8))
    o.append(T(208, 182, "diaphragm", 6.8))
    o.append(_line(252, 176, 292, 168, sw=0.8, color=GREY))
    o.append(_rect(392, 162, 20, 34, fill="#dbe6f3", sw=1.1))
    o.append(T(452, 196, "Process", 6.8))
    o.append(T(452, 206, "diaphragm", 6.8))
    o.append(_line(450, 194, 414, 178, sw=0.8, color=GREY))
    o.append(T(112, 196, "Process", 6.8))
    o.append(T(112, 206, "pressure in", 6.8))
    o.append(_ar(180, 198, 288, 198, color=RED))
    return _mk(16, o, "Figure 2.16 - Pneumatic pressure transmitter",
               "Bo phat tin ap suat khi nen: he thong van/lo phun, bo khuyec dai, ong phoi va dieu chinh do dai",
               "Pneumatic pressure transmitter with flapper-nozzle, relay amplification and feedback bellows",
               "Ap suat chat long tac dung len mang ngăn, canh tay dat van phun, tin hieu duoc khuyec dai va phan hoi",
               "Flapper-nozzle transmitter with air supply, relay, output line, span adjustment and feedback bellows")


# ---------------------------------------------------------------- 2.17
@_reg
def fig_f17():
    """Fig. 2.17 - Pneumatic relay."""
    o = [_defs()]
    o.append(T(56, 34, "(a)", 7.2))
    o.append(T(200, 52, "Air supply", 6.8))
    o.append(_ar(198, 54, 152, 54, color=GREEN))
    o.append(_poly([(152, 48), (138, 60), (152, 72)],
                   fill="#dbe6f3", sw=1.0, close=True))
    o.append(T(148, 38, "AFR", 6.8))
    o.append(_line(152, 60, 320, 60, sw=1.2))
    o.append(T(300, 42, "Restriction", 6.8))
    o.append(_line(300, 46, 300, 58, sw=0.8, color=GREY))
    o.append(_rect(320, 46, 48, 60, fill="#eef3fb", sw=1.2))
    o.append(T(300, 124, "Pneumatic", 6.6))
    o.append(T(300, 134, "control relay", 6.6))
    o.append(_line(298, 122, 322, 96, sw=0.8, color=GREY))
    o.append(_circle(344, 84, 5, fill="#ffffff", sw=1.0))
    o.append(_line(344, 60, 344, 78, sw=1.0))
    o.append(_path("M 348 60 L 372 50", sw=1.2))
    o.append(T(392, 44, "Nozzle", 6.8))
    o.append(_line(390, 46, 374, 52, sw=0.8, color=GREY))
    o.append(_ar(344, 106, 344, 124, color=GREY, sw=1.0))
    o.append(T(350, 122, "Exhaust", 6.6))
    o.append(T(56, 152, "(b)", 7.2))
    for yy, lab in ((178, "Input"), (200, "Supply"), (224, "Output")):
        o.append(_rect(132, yy - 8, 94, 16, fill="#eef3fb", sw=1.0))
        o.append(T(128, yy + 2, lab, 6.6))
    o.append(_line(226, 178, 420, 178, sw=1.1))
    o.append(_line(226, 200, 404, 200, sw=1.1))
    o.append(_line(226, 224, 420, 224, sw=1.1))
    o.append(_circle(286, 200, 7, fill="#ffffff", sw=1.2))
    o.append(_rect(398, 164, 8, 72, fill="#dbe6f3", sw=1.1))
    o.append(_line(288, 200, 398, 190, sw=1.1))
    o.append(_circle(288, 200, 3, fill=INK, sw=0))
    o.append(_ar(226, 224, 194, 224, color=RED, sw=1.0))
    o.append(T(440, 178, "Diaphragm", 6.6))
    o.append(_line(438, 176, 408, 176, sw=0.8, color=GREY))
    o.append(T(440, 196, "Valve stem", 6.6))
    o.append(_line(438, 194, 360, 194, sw=0.8, color=GREY))
    o.append(T(440, 216, "Ball valve", 6.6))
    o.append(_line(438, 214, 300, 206, sw=0.8, color=GREY))
    return _mk(17, o, "Figure 2.17 - Pneumatic relay",
               "Bo khuyec dai khi nen: dau vao co chua, nguon cap, van ban va dau ra duoc dieu khien bang mang",
               "Pneumatic relay amplifying nozzle backpressure through a diaphragm, ball valve and exhaust",
               "So do nguyen ly va mat cat bo relay: dau vao AFR, nguon cap, dau ra, mang, than van va van ban",
               "Relay schematic with air filter regulator, restriction, nozzle, diaphragm and ball valve")


# ---------------------------------------------------------------- 2.18
@_reg
def fig_f18():
    """Fig. 2.18 - Calibration adjustment (Wheatstone bridge)."""
    o = [_defs()]
    o.append(_line(210, 70, 296, 70, sw=1.2))
    o.append(_zig(296, 70, 372, 70, n=5, amp=4))
    o.append(T(334, 56, "Rt", 7.0))
    o.append(_line(372, 70, 458, 70, sw=1.2))
    o.append(_line(210, 70, 210, 122, sw=1.2))
    o.append(_line(210, 122, 210, 186, sw=1.2))
    o.append(_line(180, 86, 180, 106, sw=1.6))
    o.append(_line(172, 96, 188, 96, sw=1.0))
    o.append(_line(174, 90, 186, 90, sw=0.7))
    o.append(_line(180, 86, 210, 86, sw=1.0))
    o.append(_line(180, 106, 210, 106, sw=1.0))
    o.append(T(156, 100, "Eb", 7.0))
    o.append(_zig(210, 106, 210, 150, n=5, amp=4))
    o.append(T(222, 130, "Rc", 7.0))
    o.append(_zig(210, 186, 296, 186, n=5, amp=4))
    o.append(T(252, 200, "Rc", 7.0))
    o.append(_line(296, 186, 458, 186, sw=1.2))
    o.append(_poly([(458, 70), (528, 116), (458, 186), (388, 116)],
                   fill="none", sw=1.2, close=True))
    o.append(_zig(398, 82, 448, 106, n=4, amp=3))
    o.append(T(410, 80, "R1", 6.8))
    o.append(_zig(468, 106, 518, 82, n=4, amp=3))
    o.append(T(498, 80, "R2", 6.8))
    o.append(_zig(398, 150, 448, 126, n=4, amp=3))
    o.append(T(410, 152, "R3", 6.8))
    o.append(_zig(468, 126, 518, 150, n=4, amp=3))
    o.append(T(498, 152, "R4", 6.8))
    o.append(_circle(458, 116, 13, fill="#ffffff", sw=1.1))
    o.append(T(458, 119, "V0", 6.8))
    o.append(T(458, 28, "Calibration adjustment", 7.6))
    return _mk(18, o, "Figure 2.18 - Calibration adjustment",
               "Mach cau Wheatstone co cac dien tro R1 den R4, Rt va Rc, nguon Eb va dau ra V0",
               "Wheatstone-bridge calibration circuit with R1 to R4, temperature and terminal compensation resistors",
               "So mach cau co bon nhanh dien tro cam ung, dien tro bu nhiet do Rt, bu dau cuoi Rc, nguon Eb va V0",
               "Bridge diamond of four resistors with supply battery, compensation resistors and detector")


# ---------------------------------------------------------------- 2.19
@_reg
def fig_f19():
    """Fig. 2.19 - Strain gage pressure transmitter."""
    o = [_defs()]
    o.append(_rect(388, 26, 74, 20, fill="#eef3fb", sw=1.1))
    o.append(T(425, 40, "Voltage", 6.6))
    o.append(T(425, 49, "regulator", 6.6))
    o.append(T(516, 34, "+", 8.0))
    o.append(_ar(514, 36, 462, 36, color=GREEN))
    o.append(_rect(218, 52, 72, 24, fill="#eef3fb", sw=1.1))
    o.append(T(254, 62, "Zero", 6.6))
    o.append(T(254, 71, "adjustment", 6.6))
    o.append(_line(254, 76, 254, 84, sw=0.8))
    o.append(_line(248, 84, 260, 84, sw=0.7))
    o.append(_line(250, 87, 258, 87, sw=0.6))
    o.append(_poly([(330, 90), (330, 122), (372, 106)],
                   fill="#eef3fb", sw=1.1, close=True))
    o.append(T(342, 102, "Input", 6.4))
    o.append(T(342, 112, "AMP", 6.4))
    o.append(_rect(408, 90, 74, 30, fill="#eef3fb", sw=1.1))
    o.append(T(445, 102, "Output current", 6.2))
    o.append(T(445, 112, "regulator", 6.6))
    o.append(_rect(408, 136, 74, 22, fill="#eef3fb", sw=1.1))
    o.append(T(445, 150, "Span adjustment", 6.2))
    o.append(T(516, 148, "-", 8.0))
    o.append(_line(482, 147, 512, 147, sw=1.0))
    o.append(_rect(136, 110, 74, 30, fill="#eef3fb", sw=1.1))
    o.append(T(173, 122, "Strain gage", 6.4))
    o.append(T(173, 132, "force unit", 6.4))
    o.append(_ar(210, 124, 268, 124))
    o.append(T(226, 140, "Connecting wire", 6.4))
    o.append(_line(254, 84, 254, 92, sw=1.0))
    o.append(_line(254, 92, 330, 92, sw=1.0))
    o.append(_line(330, 106, 408, 106, sw=1.0))
    o.append(_line(425, 46, 425, 90, sw=1.0))
    o.append(_line(445, 120, 445, 136, sw=1.0))
    o.append(_line(254, 92, 254, 124, sw=1.0))
    o.append(_line(173, 140, 173, 158, sw=0.8))
    o.append(T(560, 26, "Output", 6.6))
    o.append(T(560, 36, "signal", 6.6))
    o.append(_ar(560, 42, 560, 158, color=RED, sw=1.2))
    o.append(_line(300, 140, 300, 170, sw=1.2))
    o.append(T(316, 160, "Force beam", 6.4))
    o.append(_line(300, 170, 300, 178, sw=1.0))
    o.append(T(320, 178, "Thrust pivot and seal", 6.4))
    o.append(_rect(244, 182, 112, 44, fill="#ffffff", sw=1.2))
    o.append(_zig(268, 184, 268, 224, n=6, amp=4, color=BLUE))
    o.append(_zig(332, 184, 332, 224, n=6, amp=4, color=BLUE))
    o.append(T(362, 196, "Diaphragm", 6.4))
    o.append(_line(360, 194, 334, 200, sw=0.8, color=GREY))
    o.append(T(166, 190, "Vent plug", 6.4))
    o.append(_line(204, 190, 244, 190, sw=0.8, color=GREY))
    o.append(T(166, 224, "Open to atmosphere", 6.4))
    o.append(T(370, 222, "Process pressure", 6.4))
    o.append(_ar(300, 232, 300, 226, color=RED, sw=1.0))
    return _mk(19, o, "Figure 2.19 - Strain gage pressure transmitter",
               "Bo phat tin bien tro: co che dang va mang, mach dich ap, khuong dai vao va dieu chinh zero/span",
               "Strain gage pressure transmitter with force beam, Wheatstone bridge amplifier and 4-20 mA output",
               "Ap suat tac dung len mang lam bien dang thanh bien tro, tin hieu duoc khuech dai va chinh zero, span",
               "Force beam and diaphragm feeding a strain bridge, voltage regulator, amplifier and current regulator")


# ---------------------------------------------------------------- 2.20
@_reg
def fig_f20():
    """Fig. 2.20 - Capacitance pressure transmitter sensing element."""
    o = [_defs()]
    o.append(_path("M 196 62 A 62 78 0 0 0 196 198", sw=1.4))
    o.append(_path("M 208 74 A 50 66 0 0 0 208 186", sw=1.0, color=GREY))
    o.append(_path("M 220 86 A 38 54 0 0 0 220 174", sw=0.9, color=GREY))
    o.append(T(128, 208, "Isolating", 6.8))
    o.append(T(128, 218, "diaphragm", 6.8))
    o.append(_line(184, 206, 194, 190, sw=0.8, color=GREY))
    o.append(_rect(292, 62, 140, 132, fill="#eef3fb", sw=1.4))
    o.append(_line(334, 80, 334, 176, sw=2.0, color=BLUE))
    o.append(_line(390, 80, 390, 176, sw=2.0, color=BLUE))
    o.append(_zig(362, 82, 362, 174, n=9, amp=4, color=GREEN))
    o.append(_rect(336, 80, 52, 96, fill="#dbe8f5", sw=0))
    o.append(T(460, 96, "Capacitor", 6.6))
    o.append(T(460, 106, "plates", 6.6))
    o.append(_line(458, 100, 392, 100, sw=0.8, color=GREY))
    o.append(T(460, 138, "Diaphragm", 6.6))
    o.append(_line(458, 136, 366, 136, sw=0.8, color=GREY))
    o.append(T(460, 158, "Insulation", 6.6))
    o.append(_line(458, 156, 398, 156, sw=0.8, color=GREY))
    o.append(T(460, 178, "Silicone oil", 6.6))
    o.append(_line(458, 176, 382, 166, sw=0.8, color=GREY))
    o.append(_path("M 334 60 L 334 46 L 312 46", sw=1.0, color=INK))
    o.append(_path("M 390 60 L 390 46 L 368 46", sw=1.0, color=INK))
    o.append(T(242, 36, "Lead wires", 6.8))
    o.append(_line(296, 40, 312, 44, sw=0.8, color=GREY))
    o.append(_circle(332, 184, 2.4, fill=INK, sw=0))
    o.append(_circle(394, 184, 2.4, fill=INK, sw=0))
    o.append(T(462, 198, "Seal welds", 6.6))
    o.append(_line(460, 196, 396, 186, sw=0.8, color=GREY))
    o.append(T(340, 226, "Capacitance sensing element", 7.4))
    return _mk(20, o, "Figure 2.20 - Capacitance pressure transmitter sensing element",
               "Bo cam nhan dien dung: hai ban dien cuc, mang cam nhan, dau cach, dau Silicone va mang ngăn cach",
               "Capacitance transmitter sensing element with capacitor plates, sensing diaphragm, insulation and silicone oil",
               "Cau truc floating cell co hai ban cuc, mang giua, dau cach va mang ngăn cach bang dau silicone",
               "Cross-section of capacitor plates around a sensing diaphragm filled with silicone oil")
