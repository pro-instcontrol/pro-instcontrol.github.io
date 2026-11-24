# -*- coding: utf-8 -*-
"""Vector figures 3.19-3.36 for the IPC Chapter 3 bilingual reader."""
from ipcfig3_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series, _wavey,
                            make_registry)
import math

FIGS, _reg = make_registry()


def _res(x1, y1, x2, y2, n=5, amp=3.0, color=INK, sw=1.0):
    """Zig-zag resistor between two points."""
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


def _wire(pts, color=INK, sw=1.1):
    return _poly(pts, sw=sw, color=color)


def _dot(x, y, r=2.0, color=INK):
    return _circle(x, y, r, fill=color, sw=0)


def _tip(x, y, color=INK):
    """Chevron symbol for a thermocouple measuring junction."""
    return _poly([(x - 16, y), (x, y - 9), (x, y + 9)],
                 fill="#ffffff", sw=1.2, color=color, close=True)


def _hatchv(x, y, w, h, step=6, color=GREY):
    o = []
    for yy in range(int(y), int(y + h), step):
        o.append(_line(x, yy, x + w, min(y + h, yy + 5), sw=0.5, color=color))
    return "".join(o)


# ---------------------------------------------------------------- 3.19
@_reg
def fig_f19():
    """Fig. 3.19 - Gasifier thermocouple: assembly and cut view of the tip."""
    o = [_defs()]
    # complete assembly
    o.append(_rect(35, 78, 360, 10, "#eef3fb", sw=1.0))
    o.append(_rect(35, 78, 24, 10, "#e9e3d6", sw=1.0))
    o.append(_line(35, 83, 395, 83, sw=0.6, dash="4,3", color=GREY))
    o.append(_rect(400, 48, 15, 64, "#e9e3d6", sw=1.0))
    o.append(_hatchv(400, 48, 15, 64))
    o.append(_rect(415, 78, 52, 10, "#eef3fb", sw=1.0))
    o.append(_line(415, 83, 467, 83, sw=0.6, dash="4,3", color=GREY))
    # expansion hole
    o.append(_rect(372, 80, 6, 6, "#ffffff", sw=0.9))
    o.append(_ar(375, 66, 375, 80, color=RED, sw=1.0))
    o.append(T(375, 60, "Expansion hole", 7.0, color=RED))
    # vessel wall / tightening screw / seal
    o.append(_rect(446, 61, 9, 15, "#ffffff", sw=1.0))
    o.append(_line(445, 61, 456, 61, sw=1.4))
    o.append(_ar(451, 50, 451, 60, color=RED, sw=1.0))
    o.append(T(451, 44, "Tightening screw", 7.0, color=RED))
    o.append(_rect(462, 70, 27, 26, "#e9e3d6", sw=1.0))
    o.append(_hatchv(462, 70, 27, 26, step=5))
    o.append(_wire([(489, 83), (520, 83), (540, 75)]))
    o.append(_rect(552, 58, 22, 8, "#ffffff", sw=1.0))
    o.append(_ar(573, 60, 565, 64, color=RED, sw=1.0))
    o.append(T(596, 58, "Rubber gasket", 7.0, color=RED))
    # thermocouple head
    o.append(_poly([(540, 75), (575, 66), (606, 84), (575, 100)],
                   fill="#f4f6fa", sw=1.2, close=True))
    o.append(_circle(590, 84, 5, fill="#ffffff", sw=1.0))
    o.append(_ar(604, 108, 590, 94, color=RED, sw=1.0))
    o.append(T(608, 114, "Thermo couple head", 7.0, color=RED))
    o.append(T(340, 128, "Complete assembly", 8.0, weight="bold"))
    # labels of the main assembly
    o.append(T(63, 101, "Ceramic part", 7.0))
    o.append(T(63, 110, "Protection tube", 7.0))
    o.append(T(300, 110, "Metal part SS316", 7.0))
    o.append(_ar(480, 119, 476, 96, color=RED, sw=1.0))
    o.append(T(480, 124, "High pressure seal", 7.0, color=RED))
    # cut view of the tip
    o.append(_circle(170, 178, 32, fill="#fbfaf7", sw=1.3))
    o.append(_circle(170, 178, 24, fill="none", sw=1.0, color=GREY))
    o.append(_circle(170, 178, 14, fill="#f4f6fa", sw=1.0))
    o.append(_dot(165, 174, 2.2, color=RED))
    o.append(_dot(175, 182, 2.2, color=BLUE))
    o.append(_ar(96, 156, 143, 165, color=RED, sw=1.0))
    o.append(T(88, 150, "Thermocouple tip", 7.0, color=RED))
    o.append(_ar(268, 156, 190, 170, color=BLUE, sw=1.0))
    o.append(T(272, 150, "Internal ceramic tube", 7.0, color=BLUE))
    o.append(_ar(107, 207, 149, 191, color=GREY, sw=1.0))
    o.append(T(52, 215, "Inner ceramic sheath", 7.0))
    o.append(_ar(266, 205, 191, 190, color=GREY, sw=1.0))
    o.append(T(268, 212, "Outer ceramic sheath", 7.0))
    o.append(T(170, 228, "Cut view", 7.0, color=GREY))
    return _mk(19, o, "Figure 3.19 - Gasifier thermocouple",
               "Cặp nhiệt điện dùng trong lò khí hóa: cụm hoàn chỉnh và mặt cắt đầu đo",
               "Gasifier thermocouple: complete assembly and cut view of the measuring tip",
               "Sơ đồ cấu tạo cặp nhiệt điện lò khí hóa với đầu đo, vỏ bảo vệ và gioăng làm kín",
               "Construction of a gasifier thermocouple showing the sealed head, protection tube and cut view of the tip")


# ---------------------------------------------------------------- 3.20
@_reg
def fig_f20():
    """Fig. 3.20 - Surface (skin) temperature thermocouple held by magnets."""
    o = [_defs()]
    # inclined reactor vessel wall
    o.append(_poly([(90, 72), (520, 150), (505, 176), (75, 98)],
                   fill="#eef3fb", sw=1.3, close=True))
    o.append(_line(86, 85, 512, 163, sw=0.6, dash="5,3", color=GREY))
    # two hollow cylindrical magnets
    for mx, my in ((185, 140), (385, 175)):
        o.append(_rect(mx, my, 30, 44, "#ffffff", sw=1.1))
        o.append(_ellipse(mx + 15, my, 15, 5, fill="#f4f6fa", sw=1.0))
        o.append(_ellipse(mx + 15, my + 44, 15, 5, fill="none", sw=1.0))
        o.append(_line(mx + 15, my - 12, mx + 15, my + 56,
                       sw=0.6, dash="4,3", color=GREY))
    o.append(_ar(155, 158, 185, 158, color=GREY, sw=1.0))
    o.append(T(143, 162, "d", 8.0, color=GREY))
    o.append(_ar(355, 193, 385, 193, color=GREY, sw=1.0))
    o.append(T(343, 197, "d", 8.0, color=GREY))
    # steel flat and housing
    o.append(_wire([(200, 118), (455, 155)], sw=2.0))
    o.append(_rect(452, 132, 44, 32, "#f4f6fa", sw=1.2))
    o.append(_circle(450, 158, 4, fill=RED, sw=0))
    o.append(_ar(478, 128, 590, 46, color=BLUE, sw=1.0))
    o.append(_ar(486, 132, 600, 50, color=BLUE, sw=1.0))
    o.append(_circle(590, 46, 2.4, fill=INK, sw=0))
    o.append(_circle(600, 50, 2.4, fill=INK, sw=0))
    o.append(T(596, 38, "Thermocouple extension wire", 7.0, color=BLUE))
    # callouts
    o.append(_ar(250, 205, 200, 184, color=RED, sw=1.0))
    o.append(T(252, 210, "Magnets", 7.5, color=RED))
    o.append(_ar(500, 207, 451, 162, color=RED, sw=1.0))
    o.append(T(502, 212, "Thermocouple tip", 7.5, color=RED))
    o.append(T(270, 65, "Reactor vessel surface", 7.0, color=GREY))
    return _mk(20, o, "Figure 3.20 - Surface temperature thermocouple",
               "Cặp nhiệt điện đo nhiệt độ bề mặt, giữ bằng nam châm hình trụ",
               "Surface temperature thermocouple held against a vessel by cylinder magnets",
               "Sơ đồ cặp nhiệt điện đo nhiệt độ mặt ngoài thành bình với hai nam châm và dây nối dài",
               "Skin temperature thermocouple: magnets, steel flat, tip on the vessel wall and extension wires")


# ---------------------------------------------------------------- 3.21
@_reg
def fig_f21():
    """Fig. 3.21 - Superheater metal thermocouple with curved grip."""
    o = [_defs()]
    # curved metal grip (two arc bands)
    def arc(cx, cy, r, a0, a1, n=16):
        pts = []
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        return pts
    o.append(_poly(arc(150, 125, 62, -108, 108), sw=3.0, color=INK))
    o.append(_poly(arc(150, 125, 50, -108, 108), sw=3.0, color=INK))
    a0 = arc(150, 125, 62, -108, 108)[0]
    b0 = arc(150, 125, 50, -108, 108)[0]
    a1 = arc(150, 125, 62, 108, 108)[-1]
    b1 = arc(150, 125, 50, 108, 108)[-1]
    o.append(_line(a0[0], a0[1], b0[0], b0[1], sw=1.2))
    o.append(_line(a1[0], a1[1], b1[0], b1[1], sw=1.2))
    # measuring junction fixed to the grip
    o.append(_rect(186, 115, 18, 20, "#ffffff", sw=1.0))
    o.append(_line(191, 125, 199, 125, sw=1.6, color=RED))
    o.append(_ar(120, 72, 190, 116, color=RED, sw=1.0))
    o.append(T(110, 68, "Thermocouple tip", 7.2, color=RED))
    o.append(_ar(160, 204, 158, 186, color=GREY, sw=1.0))
    o.append(T(160, 212, "Metal grip", 7.2, color=GREY))
    # long mineral-insulated inset
    def wave(x0, x1, yc, amp, n=140):
        pts = []
        for i in range(n + 1):
            t = i / float(n)
            x = x0 + (x1 - x0) * t
            pts.append((x, yc + amp * math.sin(5.0 * math.pi * t)))
        return pts
    o.append(_poly(wave(200, 460, 125, 12), sw=1.2))
    o.append(_poly(wave(200, 460, 125, 9), sw=1.0, color=GREY))
    o.append(_ar(350, 80, 350, 111, color=GREY, sw=1.0))
    o.append(T(350, 74, "Mineral insulated thermocouple inset", 7.2, color=GREY))
    # head
    o.append(_wire([(460, 125), (485, 125), (485, 105)]))
    o.append(_rect(472, 72, 34, 34, "#f4f6fa", sw=1.1))
    o.append(_circle(489, 89, 7, fill="#ffffff", sw=1.0))
    o.append(_poly([(482, 106), (496, 106), (492, 122), (486, 122)],
                   fill="#e9e3d6", sw=1.0, close=True))
    o.append(_ar(540, 158, 493, 118, color=RED, sw=1.0))
    o.append(T(542, 163, "Thermocouple head", 7.2, color=RED))
    return _mk(21, o, "Figure 3.21 - Superheater metal thermocouple",
               "Cặp nhiệt điện đo nhiệt độ kim loại ống quá nhiệt, đầu đo dạng cung",
               "Superheater metal thermocouple with an arc-shaped grip",
               "Sơ đồ cặp nhiệt điện quá nhiệt với đầu kẹp cong và đoạn dây cách điện khoáng dài",
               "Superheater thermocouple: curved metal grip, junction and long mineral-insulated inset")


# ---------------------------------------------------------------- 3.22
@_reg
def fig_f22():
    """Fig. 3.22 - Parallel thermocouples for average temperature."""
    o = [_defs()]
    for y in (78, 148):
        o.append(_tip(62, y))
        o.append(_wire([(62, y - 9), (110, y - 9)]))
        o.append(_wire([(62, y + 9), (110, y + 9)]))
        o.append(_rect(110, y - 20, 132, 40, "#ffffff", sw=1.1))
        o.append(_res(128, y, 218, y))
        o.append(T(236, y - 5, "+", 8.0))
        o.append(T(236, y + 11, "−", 8.0))
        o.append(_wire([(242, y - 9), (300, y - 9)]))
        o.append(_wire([(242, y + 9), (300, y + 9)]))
    o.append(_rect(300, 52, 56, 122, "#f4f6fa", sw=1.2))
    o.append(_line(320, 52, 320, 174, sw=0.9, color=GREY))
    o.append(_dot(320, 69)); o.append(_dot(320, 87))
    o.append(_dot(320, 139)); o.append(_dot(320, 157))
    o.append(_wire([(356, 69), (520, 92)]))
    o.append(_wire([(356, 157), (520, 116)]))
    o.append(_rect(520, 76, 108, 56, "#ffffff", sw=1.2))
    o.append(T(536, 98, "+", 8.0))
    o.append(T(536, 120, "−", 8.0))
    o.append(_ar(628, 104, 654, 104, color=BLUE, sw=1.0))
    # callouts
    o.append(_ar(70, 178, 60, 157, color=RED, sw=1.0))
    o.append(T(72, 196, "Thermocouple tips", 7.2, color=RED))
    o.append(_ar(172, 190, 172, 130, color=GREY, sw=1.0))
    o.append(T(172, 207, "Swamping resistance box", 7.2, color=GREY))
    o.append(T(328, 207, "Terminal strip", 7.2))
    o.append(T(574, 150, "Measurement circuit", 7.2))
    return _mk(22, o, "Figure 3.22 - Average temperature circuit",
               "Mắc song song nhiều cặp nhiệt điện qua điện trở dập để đo nhiệt độ trung bình",
               "Parallel thermocouples with swamping resistors for average temperature",
               "Sơ đồ nối song song các cặp nhiệt điện có điện trở dập và bảng cực tới mạch đo",
               "Average-temperature measurement: parallel thermocouples, swamping resistors and terminal strip")


# ---------------------------------------------------------------- 3.23
@_reg
def fig_f23():
    """Fig. 3.23 - Two opposed thermocouples for differential temperature."""
    o = [_defs()]
    for y in (78, 150):
        o.append(_tip(62, y))
        o.append(_wire([(62, y - 9), (110, y - 9)]))
        o.append(_wire([(62, y + 9), (110, y + 9)]))
        o.append(_rect(110, y - 20, 118, 40, "#ffffff", sw=1.1))
    o.append(T(220, 73, "+", 8.0)); o.append(T(220, 89, "−", 8.0))
    o.append(T(220, 145, "+", 8.0)); o.append(T(220, 161, "−", 8.0))
    # opposed connection on the terminal strip
    o.append(_wire([(228, 69), (300, 69)]))
    o.append(_wire([(228, 87), (300, 87)]))
    o.append(_wire([(228, 141), (300, 141)]))
    o.append(_wire([(228, 159), (300, 159)]))
    o.append(_rect(300, 55, 60, 118, "#f4f6fa", sw=1.2))
    o.append(_line(318, 55, 318, 173, sw=0.8, color=GREY))
    o.append(_dot(318, 69)); o.append(_dot(318, 87))
    o.append(_dot(318, 141)); o.append(_dot(318, 159))
    o.append(_wire([(318, 87), (318, 141)]))
    o.append(_wire([(360, 69), (520, 92)]))
    o.append(_wire([(360, 159), (520, 120)]))
    o.append(_rect(520, 76, 108, 58, "#ffffff", sw=1.2))
    o.append(T(536, 99, "+", 8.0)); o.append(T(536, 121, "−", 8.0))
    o.append(_ar(628, 105, 654, 105, color=BLUE, sw=1.0))
    o.append(_ar(70, 180, 60, 159, color=RED, sw=1.0))
    o.append(T(72, 198, "Thermocouple tips", 7.2, color=RED))
    o.append(T(330, 198, "Terminal strip", 7.2))
    o.append(T(574, 154, "Measurement circuit", 7.2))
    o.append(T(340, 135, "Opposed emf", 7.0, color=RED))
    return _mk(23, o, "Figure 3.23 - Differential temperature circuit",
               "Hai cặp nhiệt điện mắc ngược nhau để đo chênh nhiệt độ giữa hai môi trường",
               "Two opposed thermocouples for differential temperature measurement",
               "Sơ đồ nối ngược hai cặp nhiệt điện để suất điện động hiệu ứng bằng không khi hai nhiệt độ bằng nhau",
               "Differential-temperature circuit: two opposing thermocouples, terminal strip and measurement circuit")


# ---------------------------------------------------------------- 3.24
@_reg
def fig_f24():
    """Fig. 3.24 - Thermistor voltage divider linearising circuit."""
    o = [_defs()]
    o.append(_wire([(190, 52), (400, 52)]))
    o.append(_wire([(190, 52), (190, 190)]))
    o.append(_wire([(190, 190), (520, 190)]))
    # thermistor in a circle
    o.append(_circle(400, 82, 30, fill="#fbfaf7", sw=1.2))
    o.append(_wire([(400, 52), (400, 58)]))
    o.append(_res(400, 58, 400, 106, n=6, amp=4.0))
    o.append(_dot(400, 112))
    o.append(_res(400, 112, 400, 190, n=6, amp=4.0))
    # output branch
    o.append(_wire([(400, 112), (520, 112)]))
    o.append(_dot(400, 52)); o.append(_dot(400, 190)); o.append(_dot(520, 190))
    o.append(_dot(520, 112))
    o.append(_ar(172, 190, 172, 52, color=BLUE, sw=1.2))
    o.append(T(160, 122, "e_in", 7.6, color=BLUE))
    o.append(_ar(542, 190, 542, 112, color=GREEN, sw=1.2))
    o.append(T(550, 154, "e_out", 7.6, color=GREEN))
    o.append(T(414, 160, "R", 8.0))
    o.append(_ar(452, 82, 428, 82, color=GREY, sw=1.0))
    o.append(T(454, 86, "NTC thermistor", 7.2, color=GREY))
    o.append(T(350, 214, "Voltage divider linearises voltage versus temperature", 7.0, color=GREY))
    return _mk(24, o, "Figure 3.24 - Thermistor voltage divider",
               "Mạch chia áp dùng thermistor để tuyến tính hóa quan hệ điện áp nhiệt độ",
               "Voltage divider that linearises the thermistor voltage-temperature relation",
               "Sơ đồ mạch chia áp có thermistor NTC ở nhánh trên và điện trở R ở nhánh dưới",
               "Thermistor divider: supply e_in, NTC element, fixed resistor R and output e_out")


# ---------------------------------------------------------------- 3.25
@_reg
def fig_f25():
    """Fig. 3.25 - Four standard thermistor constructions."""
    o = [_defs()]
    # bead type
    o.append(_rect(82, 100, 48, 52, "#ffffff", sw=1.1))
    o.append(_hatchv(86, 104, 40, 44, step=5))
    o.append(_ellipse(106, 126, 13, 8, fill="#f4f6fa", sw=1.0))
    o.append(_wire([(96, 100), (96, 76)]))
    o.append(_wire([(116, 100), (116, 76)]))
    o.append(_dot(96, 76, 1.8)); o.append(_dot(116, 76, 1.8))
    o.append(T(106, 68, "Leads", 7.0))
    # disc type
    o.append(_ellipse(255, 126, 32, 13, fill=INK, sw=1.0))
    o.append(_wire([(242, 116), (242, 84)]))
    o.append(_wire([(268, 116), (268, 84)]))
    o.append(_dot(242, 84, 1.8)); o.append(_dot(268, 84, 1.8))
    o.append(T(255, 76, "Leads", 7.0))
    # washer type
    o.append(_ellipse(420, 126, 44, 22, fill="#e9e3d6", sw=1.2))
    o.append(_ellipse(420, 126, 21, 9, fill="#fbfaf7", sw=1.1))
    o.append(_line(384, 115, 456, 115, sw=2.0, color=GREY))
    o.append(_line(384, 137, 456, 137, sw=2.0, color=GREY))
    o.append(_ar(378, 96, 400, 112, color=GREY, sw=1.0))
    o.append(_ar(462, 96, 440, 112, color=GREY, sw=1.0))
    o.append(T(420, 88, "Connections", 7.0, color=GREY))
    # rod type
    o.append(_rect(568, 104, 20, 44, "#e9e3d6", sw=1.1))
    o.append(_hatchv(568, 104, 20, 44, step=5))
    o.append(_wire([(578, 104), (578, 78)]))
    o.append(_wire([(578, 148), (578, 174)]))
    o.append(_dot(578, 78, 1.8)); o.append(_dot(578, 174, 1.8))
    o.append(T(616, 88, "Leads", 7.0))
    for x, label in ((106, "Beads type"), (255, "Disc type"),
                     (420, "Washer type"), (578, "Rod type")):
        o.append(T(x, 196, label, 7.6, weight="bold"))
    return _mk(25, o, "Figure 3.25 - Thermistor constructions",
               "Bốn dạng chế tạo thermistor: hạt, đĩa, vòng đệm và thanh",
               "Four thermistor constructions: bead, disc, washer and rod",
               "Sơ đồ bốn dạng thermistor kèm dây dẫn và bề mặt tiếp xúc mạ kim loại",
               "Bead, disc, washer and rod thermistors with their leads and plated connections")


# ---------------------------------------------------------------- 3.26
@_reg
def fig_f26():
    """Fig. 3.26 - Thermistor interchangeability tolerance curve."""
    o = [_defs()]
    fr, mx, my = _frame(128, 42, 420, 150, (-80, 160), (0, 0.8),
                        [(-80, "−80"), (-20, "−20"), (80, "80"), (160, "+160")],
                        [(0, "0"), (0.8, "0.8")],
                        "Measured temperature °C", "Tolerance °C")
    o.append(fr)
    pts = []
    for i in range(61):
        t = -80.0 + 240.0 * i / 60.0
        if t < 20.0:
            v = 0.8 * (1.0 - (t + 80.0) / 100.0) ** 1.6 + 0.03
        elif t < 80.0:
            v = 0.03 + 0.01 * math.sin((t - 20.0) / 60.0 * math.pi)
        else:
            v = 0.03 + 0.22 * ((t - 80.0) / 80.0) ** 1.5
        pts.append((t, v))
    o.append(_series(pts, mx, my, BLUE, dot=0))
    o.append(_line(mx(20), my(0), mx(20), my(0.8), sw=0.7, dash="4,3", color=GREEN))
    o.append(_line(mx(85), my(0), mx(85), my(0.8), sw=0.7, dash="4,3", color=GREEN))
    o.append(T(448, 62, "Stable range 20 °C to 85 °C", 7.0, color=GREEN))
    o.append(T(112, 202, "O", 7.2))
    return _mk(26, o, "Figure 3.26 - Thermistor tolerance curve",
               "Đường cong sai số thermistor theo nhiệt độ đo, vùng ổn định 20 °C đến 85 °C",
               "Thermistor tolerance against measured temperature, stable from 20 °C to 85 °C",
               "Đồ thị sai số thay đổi lớn ở nhiệt độ thấp và thấp nhất trong khoảng 20 đến 85 độ C",
               "Tolerance curve falling steeply at low temperature and nearly flat over 20 °C to 85 °C")


# ---------------------------------------------------------------- 3.27
@_reg
def fig_f27():
    """Fig. 3.27 - Potentiometric temperature recording scheme."""
    o = [_defs()]
    o.append(_poly([(105, 190), (125, 174), (105, 158), (85, 174)],
                   fill="#f4f6fa", sw=1.1, close=True))
    o.append(_rect(68, 132, 74, 26, "#ffffff", sw=1.1))
    o.append(_wire([(105, 158), (105, 158)]))
    o.append(_wire([(85, 174), (78, 158)]))
    o.append(_wire([(125, 174), (132, 158)]))
    o.append(_wire([(78, 132), (78, 70)]))
    o.append(_wire([(132, 132), (132, 92)]))
    o.append(_rect(62, 48, 122, 44, "#f4f6fa", sw=1.2))
    o.append(_poly([(78, 78), (96, 60), (120, 64), (146, 58), (168, 66)],
                   sw=1.4))
    o.append(_dot(120, 64, 2.6, color=RED))
    o.append(_wire([(120, 64), (120, 102)]))
    o.append(_wire([(120, 102), (96, 102)]))
    o.append(_wire([(96, 102), (96, 132)]))
    o.append(_wire([(168, 66), (168, 132)]))
    o.append(_poly([(120, 64), (232, 76)], sw=0.9, dash="6,3", color=GREY))
    # signal chain
    o.append(_b(226, 92, 92, 30, "DC to AC\nConvertor", size=7.0))
    o.append(_b(226, 137, 92, 30, "Pre-Amplifier", size=7.6))
    o.append(_b(226, 182, 92, 30, "Servo-Amplifier", size=7.4))
    o.append(_wire([(168, 108), (226, 108)]))
    o.append(_wire([(318, 108), (346, 108)]))
    o.append(_wire([(346, 108), (346, 152)]))
    o.append(_wire([(346, 152), (226, 152)]))
    o.append(_wire([(346, 152), (346, 197)]))
    o.append(_wire([(346, 197), (226, 197)]))
    # servomotor and windings
    o.append(_circle(490, 76, 24, fill="#fbfaf7", sw=1.3))
    o.append(_dot(490, 76, 3.0))
    o.append(_res(540, 56, 540, 96, n=4, amp=5.0))
    o.append(_wire([(514, 62), (540, 56)]))
    o.append(_wire([(514, 90), (540, 96)]))
    o.append(_res(470, 140, 510, 140, n=4, amp=5.0))
    o.append(_wire([(470, 140), (446, 140)]))
    o.append(_wire([(510, 140), (540, 140)]))
    o.append(_wire([(318, 197), (446, 197)]))
    o.append(_wire([(446, 197), (446, 140)]))
    o.append(_wire([(540, 140), (540, 96)]))
    # labels
    o.append(T(122, 42, "Potentiometric circuit", 7.2))
    o.append(T(105, 208, "Thermocouple", 7.2))
    o.append(T(105, 128, "Terminal strip", 7.2))
    o.append(T(310, 70, "Mechanical coupling", 7.2, color=GREY))
    o.append(T(490, 42, "A.C. Servomotor", 7.4))
    o.append(T(584, 76, "Reference winding", 7.2))
    o.append(T(556, 152, "Control winding", 7.2))
    return _mk(27, o, "Figure 3.27 - Potentiometric recording system",
               "Sơ đồ hệ thống ghi nhiệt độ tự cân bằng dùng servo cơ khí",
               "Self-balancing potentiometric temperature recording scheme",
               "Sơ đồ mạch đo thế, bộ chuyển đổi một chiều sang xoay chiều, khuếch đại và cơ cấu servo",
               "Potentiometric recorder: thermocouple, converter, amplifiers, servomotor and mechanical coupling")


# ---------------------------------------------------------------- 3.28
@_reg
def fig_f28():
    """Fig. 3.28 - Potentiometer slide-wire circuit with cold-junction compensation."""
    o = [_defs()]
    # main measurement chain P - Q
    o.append(_wire([(100, 96), (580, 96)]))
    o.append(_dot(100, 96, 2.6)); o.append(_dot(580, 96, 2.6))
    o.append(_res(128, 96, 168, 96))
    o.append(_dot(190, 96, 2.6))
    o.append(_line(190, 92, 190, 100, sw=2.0, color=BLUE))
    o.append(_line(410, 92, 410, 100, sw=2.0, color=BLUE))
    o.append(_dot(410, 96, 2.6))
    o.append(_res(442, 96, 482, 96))
    # standard cell loop
    o.append(_wire([(100, 96), (100, 52)]))
    o.append(_wire([(100, 52), (322, 52)]))
    o.append(_circle(340, 52, 18, fill="#fbfaf7", sw=1.2))
    o.append(T(340, 48, "Eb", 7.4))
    o.append(_wire([(358, 52), (580, 52)]))
    o.append(_wire([(580, 52), (580, 96)]))
    # nickel compensation resistor across the slide wire
    o.append(_wire([(190, 96), (190, 74)]))
    o.append(_res(230, 74, 370, 74, n=6, amp=3.0))
    o.append(_wire([(370, 74), (410, 74)]))
    o.append(_wire([(410, 74), (410, 96)]))
    o.append(T(300, 68, "R4 (Ni)", 7.0, color=RED))
    # lower detector and thermocouple circuit
    o.append(_wire([(100, 96), (100, 148)]))
    o.append(_wire([(100, 148), (112, 148)]))
    o.append(_res(112, 148, 152, 148))
    o.append(_wire([(152, 148), (232, 148)]))
    o.append(_dot(202, 148, 2.4))
    o.append(_circle(248, 148, 16, fill="#ffffff", sw=1.1))
    o.append(_wire([(264, 148), (304, 148)]))
    o.append(_rect(304, 138, 34, 20, "#e9e3d6", sw=1.0))
    o.append(_line(310, 143, 330, 153, sw=1.0, color=RED))
    o.append(_line(310, 153, 330, 143, sw=1.0, color=BLUE))
    o.append(_wire([(338, 148), (410, 148)]))
    o.append(_wire([(410, 96), (410, 148)]))
    o.append(_res(450, 148, 486, 148))
    o.append(_wire([(410, 148), (450, 148)]))
    o.append(_wire([(486, 148), (580, 148)]))
    o.append(_wire([(580, 148), (580, 96)]))
    # node letters and component labels
    for x, y, lab in ((88, 92, "P"), (586, 92, "Q"), (184, 112, "L"),
                      (414, 112, "M"), (198, 166, "X"), (394, 88, "Y")):
        o.append(T(x, y, lab, 7.6, color=RED))
    o.append(T(148, 90, "R2", 7.0)); o.append(T(462, 90, "R3", 7.0))
    o.append(T(130, 166, "R1", 7.0)); o.append(T(468, 166, "R5", 7.0))
    o.append(T(520, 166, "Rs", 7.0))
    o.append(T(300, 114, "Slide-wire", 7.4, color=BLUE))
    o.append(T(322, 182, "Thermocouple", 7.2))
    o.append(T(248, 180, "Null detector", 7.0, color=GREY))
    return _mk(28, o, "Figure 3.28 - Potentiometer slide-wire circuit",
               "Mạch potentiometer dây trượt có bù nhiệt độ mối nối lạnh bằng điện trở niken",
               "Potentiometer slide-wire circuit with cold-junction compensation",
               "Sơ đồ mạch gồm nguồn chuẩn Eb, dây trượt LM, điện trở niken R4 và cặp nhiệt điện",
               "Slide-wire potentiometer: standard source Eb, slide wire L-M, nickel resistor R4 and thermocouple")


# ---------------------------------------------------------------- 3.29
@_reg
def fig_f29():
    """Fig. 3.29 - Linear servomotor arrangement."""
    o = [_defs()]
    o.append(_rect(140, 62, 400, 16, "#e9e3d6", sw=1.1))
    o.append(_hatchv(140, 62, 400, 16, step=6))
    o.append(_rect(130, 52, 14, 36, "#e9e3d6", sw=1.1))
    o.append(_hatchv(130, 52, 14, 36, step=6))
    o.append(_rect(536, 52, 14, 36, "#e9e3d6", sw=1.1))
    o.append(_hatchv(536, 52, 14, 36, step=6))
    o.append(_rect(322, 50, 58, 40, "#f4f6fa", sw=1.2))
    o.append(_res(330, 70, 372, 70, n=5, amp=6.0))
    # magnet blocks
    for mx in (210, 488):
        o.append(_rect(mx, 112, 24, 44, "#ffffff", sw=1.1))
        o.append(T(mx + 12, 108, "N", 8.0, color=RED))
        o.append(T(mx + 12, 140, "S", 8.0, color=BLUE))
    for xx in (170, 260, 350, 440, 520):
        o.append(_ar(xx, 82, xx, 164, color=GREY, sw=1.1))
    o.append(_rect(166, 166, 364, 18, "#f4f6fa", sw=1.2))
    o.append(_ar(456, 202, 480, 170, color=GREY, sw=1.0))
    o.append(T(460, 210, "Magnetic lines of force", 7.0, color=GREY))
    o.append(T(258, 200, "Flat iron piece", 7.4))
    o.append(T(351, 42, "Control coil", 7.4, color=RED))
    o.append(_ar(480, 44, 450, 62, color=GREY, sw=1.0))
    o.append(T(484, 40, "Iron rod", 7.2))
    o.append(_ar(604, 48, 550, 48, color=GREY, sw=1.0))
    o.append(T(606, 44, "Pole piece", 7.2))
    o.append(_ar(420, 82, 398, 82, color=RED, sw=1.0))
    o.append(_ar(280, 82, 302, 82, color=RED, sw=1.0))
    return _mk(29, o, "Figure 3.29 - Linear servomotor",
               "Động cơ servo tuyến tính với cuộn điều khiển di chuyển trên thanh sắt",
               "Linear servomotor with a moving control coil on an iron rod",
               "Sơ đồ cuộn điều khiển, thanh sắt, nam châm vĩnh cửu và mảnh sắt phẳng dưới tác dụng của từ trường",
               "Linear motor: control coil, iron rod, pole pieces, N/S magnets and downward magnetic flux")


# ---------------------------------------------------------------- 3.30
@_reg
def fig_f30():
    """Fig. 3.30 - Optical (brightness) pyrometer."""
    o = [_defs()]
    o.append(_rect(42, 88, 26, 26, "#f4f6fa", sw=1.1))
    o.append(_ar(20, 101, 40, 101, color=RED, sw=1.2))
    o.append(T(55, 78, "Hot body", 7.2, color=RED))
    # optical elements
    o.append(_ellipse(150, 101, 6, 24, fill="#eef3fb", sw=1.1))
    o.append(_line(182, 86, 182, 116, sw=1.4))
    o.append(_circle(244, 101, 8, fill="#ffffff", sw=1.1))
    o.append(_line(292, 86, 292, 116, sw=1.4, color=RED))
    o.append(_ellipse(348, 101, 6, 24, fill="#eef3fb", sw=1.1))
    o.append(_ellipse(472, 101, 6, 24, fill="#eef3fb", sw=1.1))
    # ray bundle
    for dy in (-16, 0, 16):
        o.append(_line(68, 101 + dy, 144, 101 + dy * 0.4, sw=0.6, color=GREY))
        o.append(_line(156, 101 + dy * 0.4, 242, 101, sw=0.6, color=GREY))
        o.append(_line(252, 101, 290, 101 + dy * 0.5, sw=0.6, color=GREY))
        o.append(_line(298, 101 + dy * 0.5, 342, 101 + dy, sw=0.6, color=GREY))
        o.append(_line(354, 101 + dy, 466, 101 - dy * 0.7, sw=0.6, color=GREY))
        o.append(_line(478, 101 - dy * 0.7, 540, 101, sw=0.6, color=GREY))
    o.append(_poly([(540, 92), (566, 101), (540, 110)], fill="#ffffff", sw=1.1, close=True))
    o.append(_poly([(566, 101), (582, 92), (582, 110)], sw=1.0, close=True))
    # measuring circuit
    o.append(_wire([(244, 109), (244, 152)]))
    o.append(_rect(196, 152, 96, 30, "#f4f6fa", sw=1.1))
    o.append(T(244, 170, "Measuring circuit", 7.0))
    o.append(_wire([(196, 167), (160, 167)]))
    o.append(_res(160, 182, 196, 182))
    o.append(_wire([(160, 182), (160, 167)]))
    o.append(_wire([(196, 182), (196, 167)]))
    o.append(T(122, 192, "Eb", 7.4))
    o.append(T(326, 198, "Variable resistance to adjust lamp current", 6.8, color=GREY))
    o.append(T(150, 66, "Object lens", 7.0)); o.append(T(184, 76, "Screen", 7.0))
    o.append(T(292, 66, "Filter", 7.0, color=RED))
    o.append(T(244, 136, "Lamp", 7.2, color=RED))
    o.append(T(472, 66, "Microscopic lens", 7.0))
    o.append(T(560, 132, "Human eye", 7.2))
    return _mk(30, o, "Figure 3.30 - Optical pyrometer",
               "Quang học kế đo nhiệt độ: thấu kính vật, đèn chuẩn, kính lọc và mắt người",
               "Optical brightness pyrometer with object lens, comparison lamp and red filter",
               "Sơ đồ đường quang từ vật nóng qua thấu kính, đèn, kính lọc tới mắt và mạch chỉnh dòng đèn",
               "Brightness pyrometer: hot body, object lens, lamp, filter, microscopic lens and eye")


# ---------------------------------------------------------------- 3.31
@_reg
def fig_f31():
    """Fig. 3.31 - Primary flow element in a pipe: pressure and velocity."""
    o = [_defs()]
    top = [(70, 100), (290, 110), (326, 122), (356, 122), (392, 110), (620, 86)]
    bot = [(70, 166), (290, 172), (326, 158), (356, 158), (392, 168), (620, 142)]
    o.append(_poly(top + list(reversed(bot)), fill="#f7f9fc", sw=1.3, close=True))
    for f in (0.15, 0.34, 0.5, 0.68, 0.86):
        o.append(_line(70 + 550 * f, 100 + 10 * f, 70 + 550 * f, 166 + 6 * f,
                       sw=0.5, color="#c8d3e0"))
    o.append(_line(70, 133, 620, 114, sw=0.6, dash="6,4", color=GREY))
    # restriction plates
    o.append(_line(324, 122, 324, 158, sw=2.0, color=INK))
    o.append(_line(358, 122, 358, 158, sw=2.0, color=INK))
    o.append(_ar(180, 125, 260, 128, color=BLUE, sw=1.4))
    o.append(_ar(328, 140, 354, 140, color=RED, sw=1.5))
    o.append(_line(70, 202, 620, 202, sw=1.0))
    o.append(T(600, 214, "Reference", 7.0, color=GREY))
    # elevation and pressure taps
    for x, py, lab in ((202, 130, "P1 (HP)"), (480, 120, "P2 (LP)")):
        o.append(_ar(x, py + 8, x, 194, color=GREY, sw=1.0))
        o.append(T(x, lab and (182 if x < 300 else 176), lab, 7.2, color=GREY))
    o.append(_line(138, 138, 138, 202, sw=0.6, dash="4,3", color=GREY))
    o.append(_ar(148, 202, 148, 138, color=GREY, sw=1.0))
    o.append(T(126, 176, "Z1", 7.2))
    o.append(_line(430, 128, 430, 202, sw=0.6, dash="4,3", color=GREY))
    o.append(_ar(440, 202, 440, 128, color=GREY, sw=1.0))
    o.append(T(418, 172, "Z2", 7.2))
    o.append(T(170, 96, "V1", 7.4, color=BLUE)); o.append(T(170, 112, "A1", 7.4))
    o.append(T(334, 108, "V2", 7.4, color=RED)); o.append(T(366, 114, "A2", 7.4))
    o.append(T(340, 66, "Restriction", 7.0, color=GREY))
    o.append(T(304, 186, "Flow", 7.0, color=BLUE))
    return _mk(31, o, "Figure 3.31 - Flow primary element in a pipe",
               "Phần tử chính trong ống dẫn: vận tốc tăng và áp suất giảm tại chỗ thu hẹp",
               "Flow primary element in a pipe: velocity rises and pressure falls at the restriction",
               "Sơ đồ dòng chất lỏng qua chỗ thu hẹp với các thông số P1, P2, V1, V2, A1, A2 và Z1, Z2",
               "Pipe restriction showing upstream high pressure P1, downstream low pressure P2 and elevations Z1, Z2")


# ---------------------------------------------------------------- 3.32
@_reg
def fig_f32():
    """Fig. 3.32 - Continuity derivation control volume."""
    o = [_defs()]
    o.append(_line(210, 58, 210, 178, sw=1.0, dash="5,4", color=GREY))
    o.append(_line(500, 84, 500, 160, sw=1.0, dash="5,4", color=GREY))
    o.append(_line(210, 58, 500, 84, sw=1.5))
    o.append(_line(210, 178, 500, 160, sw=1.5))
    o.append(_ar(96, 118, 202, 118, color=BLUE, sw=1.4))
    o.append(_ar(504, 122, 612, 122, color=BLUE, sw=1.4))
    o.append(T(112, 104, "Flow in", 7.6, color=BLUE))
    o.append(T(560, 108, "Flow out", 7.6, color=BLUE))
    o.append(T(210, 196, "Inlet end", 7.4))
    o.append(T(500, 184, "Outlet end", 7.4))
    o.append(T(258, 50, "Section 1: A1, V1, p1", 7.0, color=GREY))
    o.append(T(450, 74, "Section 2: A2, V2, p2", 7.0, color=GREY))
    o.append(T(350, 216, "p / ρ + v² / 2 + g z = constant  (ideal, incompressible flow)",
               7.4, color=INK))
    o.append(_ar(350, 206, 350, 150, color=GREY, sw=0.9))
    return _mk(32, o, "Figure 3.32 - Derivation of the flow formula",
               "Thể tích kiểm soát giữa hai mặt cắt để suy ra phương trình lưu lượng",
               "Control volume between inlet and outlet sections for the flow derivation",
               "Sơ đồ thể tích kiểm soát có dòng vào, dòng ra và hai mặt cắt 1, 2 dùng trong suy diễn Bernoulli",
               "Control volume with flow in and flow out, used for the continuity and Bernoulli derivation")


# ---------------------------------------------------------------- 3.33
@_reg
def fig_f33():
    """Fig. 3.33 - Different shapes of orifice plates."""
    o = [_defs()]
    for cx in (150, 340, 530):
        o.append(_circle(cx, 112, 52, fill="#f7f9fc", sw=1.4))
        o.append(_poly([(cx - 12, 62), (cx - 8, 44), (cx + 8, 44), (cx + 12, 62)],
                       fill="#e9e3d6", sw=1.0, close=True))
    # concentric bore
    o.append(_circle(150, 112, 14, fill="#ffffff", sw=1.2))
    # eccentric bore, tangent to pipe wall
    o.append(_circle(340, 146, 14, fill="#ffffff", sw=1.2))
    # segmental opening
    o.append(_path("M 490 132 Q 530 168 570 132 L 490 132 Z",
                   fill="#ffffff", sw=1.2))
    # flow direction
    o.append(_ar(74, 42, 120, 42, color=BLUE, sw=1.2))
    o.append(T(97, 34, "Flow", 7.0, color=BLUE))
    for x, lab in ((150, "Concentric"), (340, "Eccentric"), (530, "Segmental")):
        o.append(T(x, 190, lab, 8.0, weight="bold"))
    o.append(T(340, 214, "Off-centre and segmental bores avoid damming of solids",
               7.0, color=GREY))
    return _mk(33, o, "Figure 3.33 - Different shapes of orifice plates",
               "Ba dạng tấm chắn lỗ: đồng tâm, lệch tâm và dạng đoạn cung",
               "Three orifice plate shapes: concentric, eccentric and segmental",
               "Sơ đồ ba dạng tấm chắn lỗ với lỗ ở giữa, lỗ lệch tâm và lỗ dạng đoạn cung",
               "Concentric, eccentric and segmental orifice plates for clean, dirty and mixed-phase service")


# ---------------------------------------------------------------- 3.34
@_reg
def fig_f34():
    """Fig. 3.34 - Pitot tube for velocity distribution."""
    o = [_defs()]
    o.append(_rect(70, 168, 540, 4, "#e9e3d6", sw=0.8))
    o.append(_line(70, 62, 610, 62, sw=0.8, color=GREY))
    o.append(_ar(96, 120, 196, 120, color=BLUE, sw=1.4))
    o.append(T(146, 108, "Flow", 7.4, color=BLUE))
    # bent pitot tube, double line for the tube wall
    o.append(_poly([(250, 90), (330, 90), (330, 168)], sw=1.4, color=INK))
    o.append(_poly([(250, 104), (316, 104), (316, 168)], sw=1.4, color=INK))
    o.append(_line(250, 90, 250, 104, sw=1.4))
    o.append(_ar(226, 97, 248, 97, color=RED, sw=1.2))
    # stagnation opening and static opening
    o.append(_rect(248, 90, 4, 14, "#ffffff", sw=0.9))
    o.append(_dot(322, 130, 2.0, color=BLUE))
    o.append(_ar(400, 142, 324, 132, color=BLUE, sw=1.0))
    o.append(T(404, 146, "Static opening", 7.2, color=BLUE))
    o.append(T(232, 78, "Impact opening", 7.2, color=RED))
    o.append(T(518, 174, "Pipe wall", 7.0, color=GREY))
    # cross-section view below the wall
    o.append(_circle(330, 206, 18, fill="#f7f9fc", sw=1.1))
    o.append(_circle(330, 206, 12, fill="none", sw=0.9, color=GREY))
    o.append(_circle(330, 206, 5, fill="none", sw=0.9, color=BLUE))
    o.append(T(392, 210, "Pitot tube", 7.4))
    o.append(_ar(376, 208, 350, 208, color=GREY, sw=1.0))
    return _mk(34, o, "Figure 3.34 - Pitot tube",
               "Ống Pitot có lỗ hứng dòng chính và lỗ đo tĩnh áp",
               "Pitot tube with an impact opening and a static pressure opening",
               "Sơ đồ ống Pitot đặt trong ống dẫn, đầu hứng hướng về dòng chảy và mặt cắt ngang của ống",
               "Pitot tube inserted through the pipe wall: impact opening facing the flow, static opening and end view")


# ---------------------------------------------------------------- 3.35
@_reg
def fig_f35():
    """Fig. 3.35 - Venturi tube with pressure taps."""
    o = [_defs()]
    top = [(60, 62), (232, 62), (304, 96), (382, 96), (476, 62), (620, 62)]
    bot = [(60, 170), (232, 170), (304, 136), (382, 136), (476, 170), (620, 170)]
    o.append(_poly(top + list(reversed(bot)), fill="#f7f9fc", sw=1.4, close=True))
    o.append(_line(60, 116, 620, 116, sw=0.6, dash="7,4", color=GREY))
    o.append(_line(60, 62, 60, 170, sw=1.0, dash="4,3", color=GREY))
    o.append(_line(620, 62, 620, 170, sw=1.0, dash="4,3", color=GREY))
    # pressure taps
    o.append(_line(198, 62, 198, 40, sw=1.2, color=RED))
    o.append(_dot(198, 62, 2.2, color=RED))
    o.append(T(198, 34, "High pressure tap", 7.0, color=RED))
    o.append(_line(340, 136, 340, 188, sw=1.2, color=BLUE))
    o.append(_dot(340, 136, 2.2, color=BLUE))
    o.append(T(340, 202, "Low pressure tap", 7.0, color=BLUE))
    # dimensions
    o.append(_ar(112, 62, 112, 170, color=GREY, sw=1.0))
    o.append(_ar(112, 170, 112, 62, color=GREY, sw=1.0))
    o.append(T(102, 118, "D", 8.0))
    o.append(_ar(400, 96, 400, 136, color=GREY, sw=1.0))
    o.append(_ar(400, 136, 400, 96, color=GREY, sw=1.0))
    o.append(T(412, 118, "d", 8.0))
    o.append(_ar(172, 174, 228, 174, color=GREY, sw=0.9))
    o.append(T(200, 188, "D/2", 7.0, color=GREY))
    o.append(_ar(310, 148, 342, 148, color=GREY, sw=0.9))
    o.append(T(324, 162, "d/2", 7.0, color=GREY))
    o.append(T(268, 76, "α ≈ 21°", 7.2, color=RED))
    o.append(T(432, 76, "β ≈ 5° to 8°", 7.2, color=RED))
    o.append(T(144, 214, "Approach section", 7.0, color=GREY))
    o.append(T(340, 156, "Throat", 7.0, color=GREY))
    o.append(T(536, 214, "Recovery section", 7.0, color=GREY))
    return _mk(35, o, "Figure 3.35 - Venturi tube",
               "Ống Venturi có đoạn hội tụ, cổ hẹp và đoạn khuếch tán thu hồi áp suất",
               "Venturi tube with converging approach, throat and diverging recovery section",
               "Sơ đồ ống Venturi với các góc α, β, đường kính D và d cùng vị trí lấy áp suất cao thấp",
               "Venturi tube: approach cone, throat of diameter d, recovery cone and high/low pressure taps")


# ---------------------------------------------------------------- 3.36
@_reg
def fig_f36():
    """Fig. 3.36 - Flow nozzle installed between flanges."""
    o = [_defs()]
    o.append(_line(60, 70, 620, 70, sw=1.1))
    o.append(_line(60, 162, 620, 162, sw=1.1))
    for fx in (190, 500):
        o.append(_rect(fx - 8, 54, 16, 124, "#e9e3d6", sw=1.1))
        o.append(_hatchv(fx - 8, 54, 16, 124, step=6))
    # nozzle profile: rounded entry tangent to the parallel throat
    o.append(_path("M 200 70 C 236 70 258 96 262 104 L 372 104 L 372 128 "
                   "L 262 128 C 258 136 236 162 200 162", sw=1.5))
    o.append(_line(372, 104, 372, 128, sw=2.0))
    o.append(_line(60, 116, 620, 116, sw=0.6, dash="7,4", color=GREY))
    o.append(_ar(180, 46, 510, 46, color=GREY, sw=1.0))
    o.append(_ar(510, 46, 180, 46, color=GREY, sw=1.0))
    o.append(T(345, 38, "D", 8.0))
    o.append(_ar(410, 104, 410, 128, color=GREY, sw=1.0))
    o.append(_ar(410, 128, 410, 104, color=GREY, sw=1.0))
    o.append(T(422, 120, "d", 8.0))
    o.append(_ar(270, 116, 356, 116, color=RED, sw=0.9))
    o.append(T(313, 152, "0.6d", 7.0, color=RED))
    o.append(_ar(226, 178, 374, 178, color=GREY, sw=1.0))
    o.append(_ar(374, 178, 226, 178, color=GREY, sw=1.0))
    o.append(T(300, 192, "1.5d", 7.0, color=GREY))
    o.append(_ar(150, 70, 184, 70, color=GREY, sw=0.9))
    o.append(T(118, 62, "0.1D", 7.0, color=GREY))
    o.append(_ar(560, 214, 440, 134, color=BLUE, sw=1.0))
    o.append(T(562, 218, "Flow nozzle", 7.4, color=BLUE))
    o.append(T(548, 150, "Pipe", 7.0, color=GREY))
    return _mk(36, o, "Figure 3.36 - Flow nozzle",
               "Vòi phun lưu lượng lắp giữa hai bích, đầu vào cong tiếp xúc với cổ hẹp song song",
               "Flow nozzle mounted between flanges with a curved entry and parallel throat",
               "Sơ đồ vòi phun lưu lượng với đầu vào cong, cổ hẹp song song và các kích thước D, d, 1.5d",
               "Flow nozzle: rounded inlet tangent to a short parallel throat, shown with pipe and flange dimensions")
