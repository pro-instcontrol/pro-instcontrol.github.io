# -*- coding: utf-8 -*-
"""Figures 3.1-3.18 for IPC Chapter 3 (temperature transducer figures)."""
import math

from ipcfig3_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def _zig(p1, p2, n=5, amp=3.0, color=INK, sw=1.1):
    """Zig-zag resistor drawn between two end points."""
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / length, dx / length
    pts = []
    for i in range(2 * n + 1):
        t = i / float(2 * n)
        off = amp if i % 2 else -amp
        pts.append((x1 + dx * t + nx * off, y1 + dy * t + ny * off))
    return _poly(pts, sw=sw, color=color)


def _ticks(cx, cy, r0, r1, a0, a1, n, color=GREY, sw=0.7):
    """Radial graduation marks on a round dial."""
    o = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / float(n))
        c, s = math.cos(a), math.sin(a)
        o.append(_line(cx + r0 * c, cy + r0 * s,
                       cx + r1 * c, cy + r1 * s, sw=sw, color=color))
    return "".join(o)


def _bridge_base(nterm):
    """Common Wheatstone bridge, supply, output and terminal strip."""
    o = [_defs()]
    o.append(_b(140, 16, 120, 26, "D.C. supply to\nbridge network", size=6.4))
    top, left, bot, right = (200, 54), (130, 112), (200, 170), (270, 112)
    o.append(_poly([top, left, bot, right, top], sw=1.3))
    o.append(_poly([(165, 42), (118, 42), (118, 112), left], sw=1.2, color=BLUE))
    o.append(_poly([(235, 42), (322, 42), (322, 112), right], sw=1.2, color=BLUE))
    o.append(_line(top[0], top[1], bot[0], bot[1], sw=1.1, color=GREY))
    o.append(_rect(180, 103, 40, 18, fill="#ffffff", sw=1.0))
    o.append(T(200, 115, "output", 7.0))
    o.append(_zig((193, 62), (137, 105), n=4, amp=3.2))
    o.append(T(157, 74, "Ra", 7.6))
    o.append(_zig((207, 62), (263, 105), n=4, amp=3.2))
    o.append(T(248, 74, "Rb", 7.6))
    o.append(_zig((137, 119), (193, 163), n=4, amp=3.2))
    o.append(T(157, 150, "Rc", 7.6))
    o.append(_line(332, 64, 332, 180, dash="4,4", color=GREY))
    o.append(_rect(350, 76, 28, 88, fill="#fbfaf7", sw=1.2))
    o.append(T(364, 70, "Terminal strip", 7.2))
    if nterm == 4:
        ys = [90, 108, 126, 144]
    elif nterm == 3:
        ys = [96, 118, 140]
    else:
        ys = [104, 134]
    for i, yy in enumerate(ys):
        o.append(_rect(354, yy - 7, 20, 14, fill="#eef3fb", sw=1.0))
        o.append(T(364, yy + 2.5, str(i + 1), 7.0))
    o.append(T(230, 205, "Control room side", 7.2))
    o.append(T(490, 205, "Field side", 7.2))
    return "".join(o), ys


# ---------------------------------------------------------------- 3.1
@_reg
def fig_f01():
    """Fig. 3.1 - liquid-in-glass thermometer."""
    o = [_defs()]
    o.append(_path("M414,178 L414,40 A16,12 0 0 1 446,40 L446,178 Z",
                   fill="#ffffff", sw=1.4))
    o.append(_line(427, 36, 427, 178, sw=0.8, color=GREY))
    o.append(_line(433, 36, 433, 178, sw=0.8, color=GREY))
    o.append(_rect(428.5, 100, 3, 80, fill=RED, sw=0))
    o.append(_circle(430, 190, 13, fill=RED, sw=1.3))
    for yy, lab in [(48, "120 °C"), (78, "90 °C"), (108, "60 °C"),
                    (138, "30 °C"), (168, "0 °C")]:
        o.append(_line(372, yy, 408, yy, dash="4,3", color=GREY))
        o.append(T(366, yy + 2.8, lab, 7.8, anchor="end"))
    o.append(T(520, 60, "Glass capillary", 7.6, anchor="start"))
    o.append(_ar(516, 63, 446, 62))
    o.append(T(520, 120, "Liquid", 7.8, anchor="start"))
    o.append(_ar(516, 117, 434, 118))
    o.append(T(520, 190, "Bulb", 7.8, anchor="start"))
    o.append(_ar(516, 187, 444, 188))
    return _mk(1, o, "Liquid-in-glass thermometer",
               "Nhiet ke chat long trong ong thuong co bulb va thang do",
               "Liquid-in-glass thermometer with bulb, capillary and scale",
               "So do nhiet ke co bulb o duoi, mao quan va thang do nhiet do",
               "Liquid-in-glass thermometer with a reservoir bulb, a narrow capillary and a temperature scale")


# ---------------------------------------------------------------- 3.2
@_reg
def fig_f02():
    """Fig. 3.2 - mercury-in-steel thermometer."""
    o = [_defs()]
    o.append(_path("M56,96 H108 A12,12 0 0 1 108,120 H56 A12,12 0 0 1 56,96 Z",
                   fill="#eef3fb", sw=1.4))
    o.append(_rect(108, 103, 16, 10, fill="#eef3fb", sw=1.2))
    o.append(_line(124, 108, 232, 108, sw=1.8, color=BLUE))
    o.append(_ellipse(252, 108, 11, 14, fill="none", sw=1.6, color=BLUE))
    o.append(_ellipse(282, 108, 11, 14, fill="none", sw=1.6, color=BLUE))
    o.append(_line(263, 108, 271, 108, sw=1.6, color=BLUE))
    o.append(_line(293, 108, 420, 108, sw=1.8, color=BLUE))
    o.append(_poly([(420, 108), (436, 70), (442, 72)], sw=1.3))
    o.append(_circle(470, 104, 68, fill="#fbfaf7", sw=1.2))
    o.append(_ticks(470, 104, 58, 64, -55, 235, 20))
    arc1 = [(470 + 50 * math.cos(math.radians(a)),
             104 + 50 * math.sin(math.radians(a)))
            for a in range(-50, 231, 5)]
    arc2 = [(470 + 45 * math.cos(math.radians(a)),
             104 + 45 * math.sin(math.radians(a)))
            for a in range(-50, 231, 5)]
    o.append(_poly(arc1, sw=2.3, color=INK))
    o.append(_poly(arc2, sw=0.8, color=GREY))
    o.append(_line(470, 104, 508, 122, sw=2.2, color=RED))
    o.append(_circle(470, 104, 3.2, fill=INK, sw=0))
    o.append(T(84, 72, "Steel bulb with mercury", 7.6))
    o.append(_ar(84, 78, 84, 96))
    o.append(T(266, 72, "Capillary tube", 7.6))
    o.append(_ar(266, 78, 266, 94))
    o.append(T(470, 24, "Bourdon tube", 7.6))
    o.append(_ar(470, 30, 494, 54))
    o.append(T(596, 168, "Pointer and dial", 7.6, anchor="start"))
    o.append(_ar(592, 165, 512, 128))
    return _mk(2, o, "Mercury-in-steel thermometer",
               "Nhiet ke thuong-tep co bulb thep, mao quan va ong bourdon chi thang",
               "Mercury-in-steel thermometer with bulb, capillary and Bourdon dial",
               "So do nhiet ke co bulb bang thep, mao quan cuon va ong bourdon quan dong ho chi",
               "Mercury-in-steel thermometer: a steel bulb and coiled capillary drive a Bourdon tube and dial pointer")


# ---------------------------------------------------------------- 3.3
@_reg
def fig_f03():
    """Fig. 3.3 - bimetallic strip, straight (low temperature)."""
    o = [_defs()]
    o.append(_line(140, 60, 140, 164, sw=2.0))
    for yy in range(64, 164, 12):
        o.append(_line(132, yy, 140, yy - 8, sw=0.7, color=GREY))
    o.append(_rect(140, 94, 18, 28, fill="#d9dde2", sw=1.2))
    o.append(_rect(158, 96, 324, 7, fill="#cdd9e8", sw=1.1))
    o.append(_rect(158, 103, 324, 7, fill="url(#h7)", sw=1.1))
    o.append(T(300, 72, "High-expansion metal", 7.6))
    o.append(_ar(300, 78, 300, 96))
    o.append(T(300, 146, "Low-expansion metal", 7.6))
    o.append(_ar(300, 140, 300, 111))
    o.append(T(150, 182, "Fixed end", 7.6))
    o.append(_ar(150, 176, 150, 123))
    o.append(T(540, 104, "Free end", 7.6, anchor="start"))
    o.append(_ar(536, 104, 484, 104))
    o.append(T(330, 212, "Straight at low temperature", 7.8))
    return _mk(3, o, "Bimetallic strip, straight",
               "Hai kim loai dan nhiep khac nhau được lien ket va thang khi lanh",
               "Bimetallic strip straight at low temperature",
               "So do hai ban kim loai dan nhiep kep voi nhau, dang thang o nhiet do thap",
               "Two welded metal strips of different expansion rates held straight at low temperature")


# ---------------------------------------------------------------- 3.4
@_reg
def fig_f04():
    """Fig. 3.4 - bimetallic strip, bent (heated)."""
    o = [_defs()]
    o.append(_line(140, 60, 140, 164, sw=2.0))
    for yy in range(64, 164, 12):
        o.append(_line(132, yy, 140, yy - 8, sw=0.7, color=GREY))
    o.append(_rect(140, 94, 18, 28, fill="#d9dde2", sw=1.2))
    o.append(_path("M158,100 C270,100 380,98 480,68 L480,75 C380,105 270,107 158,107 Z",
                   fill="#cdd9e8", sw=1.1))
    o.append(_path("M158,107 C270,107 380,105 480,75 L480,82 C380,112 270,114 158,114 Z",
                   fill="url(#h7)", sw=1.1))
    o.append(T(300, 52, "High-expansion metal", 7.6))
    o.append(_ar(300, 58, 300, 99))
    o.append(T(300, 150, "Low-expansion metal", 7.6))
    o.append(_ar(300, 144, 300, 111))
    o.append(T(150, 182, "Fixed end", 7.6))
    o.append(_ar(150, 176, 150, 114))
    o.append(T(546, 70, "Free end", 7.6, anchor="start"))
    o.append(_ar(542, 73, 482, 74))
    o.append(T(340, 212, "Heated: the strip bends upward", 7.8))
    return _mk(4, o, "Bimetallic strip, bent",
               "Hai kim loai dan nhiep cong len khi nhiet do tang",
               "Heated bimetallic strip bent upward",
               "So do hai ban kim loai dan nhiep cong len o dau tu do khi duoc nong len",
               "The same bonded strips curving upward at the free end as temperature rises")


# ---------------------------------------------------------------- 3.5
@_reg
def fig_f05():
    """Fig. 3.5 - helical bimetallic thermometer."""
    o = [_defs()]
    o.append(_circle(340, 70, 48, fill="#fbfaf7", sw=1.4))
    o.append(_ticks(340, 70, 36, 43, -150, -30, 12))
    o.append(_line(340, 70, 366, 52, sw=2.2, color=RED))
    o.append(_circle(340, 70, 3.2, fill=INK, sw=0))
    o.append(_path("M330,114 H350 V192 A10,10 0 0 1 330,192 Z",
                   fill="#eef3fb", sw=1.3))
    o.append(_line(340, 118, 340, 188, dash="3,3", color=GREY))
    coil = [(340 + 9 * math.sin(i * 0.95), 134 + i * 5.2) for i in range(10)]
    o.append(_poly(coil, sw=1.7, color=BLUE))
    coil2 = [(340 + 7 * math.sin(i * 0.95 + 0.8), 134 + i * 5.2)
             for i in range(10)]
    o.append(_poly(coil2, sw=1.1, color=GREY))
    o.append(T(250, 128, "Free end", 7.8, anchor="start"))
    o.append(_ar(246, 126, 332, 136))
    o.append(T(420, 132, "Uncoiling spindle", 7.8, anchor="start"))
    o.append(_ar(416, 130, 348, 140))
    o.append(T(210, 172, "Immersion length", 7.8, anchor="start"))
    o.append(_ar(206, 169, 328, 169))
    o.append(T(420, 192, "Fixed end", 7.8, anchor="start"))
    o.append(_ar(416, 190, 350, 186))
    return _mk(5, o, "Helical bimetallic thermometer",
               "Nhiet ke song kim loai dang xoan oc co dau quay va dau co dinh",
               "Helical bimetallic thermometer with dial and spindle",
               "So do nhiet ke co thanh xoan oc bang hai kim loai, dau tren quay kim chi va dau duoi co dinh",
               "Industrial helical bimetallic thermometer showing the coiled element, free end, spindle and fixed end")


# ---------------------------------------------------------------- 3.6
@_reg
def fig_f06():
    """Fig. 3.6 - RTD internal view."""
    o = [_defs()]
    o.append(_path("M64,110 A14,14 0 0 1 78,96 H340 V124 H78 A14,14 0 0 1 64,110 Z",
                   fill="#eef3fb", sw=1.4))
    o.append(_rect(76, 101, 150, 18, fill="#fdf6e3", sw=0.9))
    o.append(_zig((80, 110), (222, 110), n=16, amp=5.0, color=RED, sw=1.0))
    for xx in (240, 258, 276, 294, 312, 330):
        o.append(_circle(xx, 104, 1.2, fill=GREY, sw=0))
        o.append(_circle(xx, 116, 1.2, fill=GREY, sw=0))
    o.append(_rect(340, 84, 66, 52, fill="url(#h6)", sw=1.2))
    for i in range(5):
        o.append(_line(344 + i * 13, 84, 350 + i * 13, 136,
                       sw=0.8, color=GREY))
    o.append(_poly([(406, 74), (424, 86), (424, 134), (406, 146),
                    (388, 134), (388, 86)], fill="#dfe5ec", sw=1.2, close=True))
    o.append(_line(424, 104, 566, 104, sw=1.6, color=BLUE))
    o.append(_line(424, 116, 566, 116, sw=1.6, color=RED))
    o.append(T(150, 64, "RTD element", 8.0))
    o.append(_ar(150, 68, 150, 101))
    o.append(T(270, 64, "Sheath", 8.0))
    o.append(_ar(270, 68, 270, 97))
    o.append(T(380, 64, "Mounting threads", 8.0))
    o.append(_ar(380, 68, 380, 85))
    o.append(T(600, 110, "Lead wires", 8.0, anchor="start"))
    o.append(_ar(596, 110, 568, 110))
    o.append(T(252, 146, "MgO packing", 7.0, anchor="start"))
    o.append(_ar(248, 142, 252, 125))
    return _mk(6, o, "RTD internal view",
               "Mat cat ben trong cua RTD co cuon day, vo bao ve, ren lap va day dan",
               "Internal view of a resistance temperature detector",
               "So do mat cat RTD thay cuon day platin, bot magnesium oxit, vo bao ve va day dan dau ra",
               "Cutaway of an RTD showing the platinum coil, MgO packing, sheath, mounting threads and lead wires")


# ---------------------------------------------------------------- 3.7
@_reg
def fig_f07():
    """Fig. 3.7 - assembled RTD."""
    o = [_defs()]
    o.append(_line(56, 114, 72, 114, sw=1.6, color=BLUE))
    o.append(_rect(72, 104, 16, 20, fill="#dde4ee", sw=1.1))
    o.append(_ellipse(112, 114, 32, 44, fill="#eef3fb", sw=1.4))
    o.append(_ellipse(112, 114, 20, 32, fill="#ffffff", sw=0.9))
    o.append(_rect(144, 108, 52, 12, fill="#eef3fb", sw=1.2))
    o.append(_poly([(196, 96), (212, 104), (212, 124), (196, 132),
                    (180, 124), (180, 104)], fill="#dfe5ec", sw=1.2, close=True))
    o.append(_poly([(244, 94), (260, 102), (260, 126), (244, 134),
                    (228, 126), (228, 102)], fill="#dfe5ec", sw=1.2, close=True))
    o.append(_rect(212, 106, 32, 8, fill="#eef3fb", sw=1.0))
    o.append(_rect(260, 109, 270, 11, fill="#f3f6fa", sw=1.2))
    o.append(_path("M530,109 H548 L568,114 L548,120 H530 Z",
                   fill="#f3f6fa", sw=1.2))
    o.append(_line(300, 114, 520, 114, sw=0.5, color=GREY))
    o.append(T(112, 58, "RTD head", 8.0))
    o.append(_ar(112, 62, 112, 72))
    o.append(T(238, 58, "Adjustable coupling", 8.0))
    o.append(_ar(238, 62, 238, 95))
    o.append(T(440, 58, "RTD inset", 8.0))
    o.append(_ar(440, 62, 440, 109))
    return _mk(7, o, "Assembled RTD",
               "RTD hoan chinh san sang lap dat gom dau, khop dieu chinh va ong inset",
               "Assembled RTD ready for installation",
               "So do RTD hoan chinh voi dau dau day, khop noi dieu chinh va ong bao ve inset",
               "Complete assembled resistance thermometer with connection head, adjustable coupling and protective inset")


# ---------------------------------------------------------------- 3.8
@_reg
def fig_f08():
    """Fig. 3.8 - two-wire RTD bridge scheme."""
    base, ys = _bridge_base(3)
    o = [base]
    o.append(_poly([(270, 112), (320, 112), (320, ys[0]), (350, ys[0])],
                   sw=1.3, color=BLUE))
    o.append(_poly([(200, 170), (300, 170), (300, ys[1]), (350, ys[1])],
                   sw=1.3, color=BLUE))
    o.append(_line(378, ys[0], 540, 96, sw=1.4, color=BLUE))
    o.append(_poly([(378, ys[1]), (500, ys[1]), (500, 144), (540, 144)],
                   sw=1.4, color=RED))
    o.append(_zig((540, 96), (540, 144), n=5, amp=4.0, color=INK, sw=1.3))
    o.append(T(580, 120, "Rx (RTD)", 7.6, anchor="start"))
    o.append(T(340, 222, "2-wire: lead resistance adds to the RTD resistance",
               7.0))
    return _mk(8, o, "Two-wire RTD measurement scheme",
               "So do cau 2 day: dien tro day dan cong vao dien tro RTD",
               "Two-wire Wheatstone bridge scheme for RTD readout",
               "So do mang cau Wheatstone 2 day noi RTD qua bang dau cuoi, co ba cuc dau cuoi 1 2 3",
               "Two-wire bridge readout: two lead wires run from the bridge through the terminal strip to the RTD")


# ---------------------------------------------------------------- 3.9
@_reg
def fig_f09():
    """Fig. 3.9 - three-wire RTD bridge scheme."""
    base, ys = _bridge_base(4)
    o = [base]
    o.append(_poly([(270, 112), (312, 112), (312, ys[0]), (350, ys[0])],
                   sw=1.3, color=BLUE))
    o.append(_poly([(200, 170), (292, 170), (292, ys[1]), (350, ys[1])],
                   sw=1.3, color=BLUE))
    o.append(_poly([(130, 112), (108, 112), (108, 182), (272, 182),
                    (272, ys[2]), (350, ys[2])], sw=1.2, color=GREEN))
    o.append(_poly([(378, ys[0]), (500, ys[0]), (500, 90), (540, 90)],
                   sw=1.4, color=BLUE))
    o.append(_poly([(378, ys[1]), (500, ys[1]), (500, 144), (540, 144)],
                   sw=1.4, color=RED))
    o.append(_poly([(378, ys[2]), (524, ys[2]), (524, 90), (540, 90)],
                   sw=1.3, color=GREEN))
    o.append(_zig((540, 90), (540, 144), n=5, amp=4.0, color=INK, sw=1.3))
    o.append(T(580, 117, "Rx (RTD)", 7.6, anchor="start"))
    o.append(T(340, 222, "3-wire (Siemens): the third lead balances lead resistance",
               7.0))
    return _mk(9, o, "Three-wire RTD measurement scheme",
               "So do cau 3 day Siemens: day th ba bù dien tro day dan",
               "Three-wire Siemens bridge scheme for RTD readout",
               "So do mang cau 3 day voi bon cuc dau cuoi, ba day noi toi RTD de tru dien tro day dan",
               "Three-wire Siemens compensation scheme with three leads between the bridge and the RTD")


# ---------------------------------------------------------------- 3.10
@_reg
def fig_f10():
    """Fig. 3.10 - four-wire RTD bridge scheme."""
    base, ys = _bridge_base(2)
    o = [base]
    o.append(_poly([(270, 112), (320, 112), (320, ys[0]), (350, ys[0])],
                   sw=1.3, color=BLUE))
    o.append(_poly([(200, 170), (320, 170), (320, ys[1]), (350, ys[1])],
                   sw=1.3, color=BLUE))
    for yy in (98, 102):
        o.append(_poly([(378, ys[0]), (390, ys[0]), (390, yy), (540, yy)],
                       sw=1.3, color=BLUE))
    for yy in (138, 142):
        o.append(_poly([(378, ys[1]), (390, ys[1]), (390, yy), (540, yy)],
                       sw=1.3, color=RED))
    o.append(_line(540, 98, 540, 102, sw=1.3, color=BLUE))
    o.append(_line(540, 138, 540, 142, sw=1.3, color=RED))
    o.append(_zig((540, 102), (540, 138), n=4, amp=4.0, color=INK, sw=1.3))
    o.append(T(580, 120, "Rx (RTD)", 7.6, anchor="start"))
    o.append(T(340, 222, "4-wire (Callender): current and potential leads separate",
               7.0))
    return _mk(10, o, "Four-wire RTD measurement scheme",
               "So do cau 4 day Callender: tach day dong va day do dien ap",
               "Four-wire Callender bridge scheme for RTD readout",
               "So do mang cau 4 day voi hai cuc dau cuoi, moi cuc co hai day rieng dan toi RTD",
               "Four-wire Callender scheme with separate current and potential leads to the RTD element")


# ---------------------------------------------------------------- 3.11
@_reg
def fig_f11():
    """Fig. 3.11 - thermocouple beads and head."""
    o = [_defs()]
    o.append(_circle(48, 123, 4, fill=RED, sw=0))
    o.append(_line(52, 120, 440, 120, sw=1.5, color=BLUE))
    o.append(_line(52, 126, 440, 126, sw=1.5, color=RED))
    for xx in (110, 190, 270, 350):
        o.append(_rect(xx, 114, 60, 18, fill="#eef3fb", sw=1.2))
        o.append(_line(xx + 4, 120, xx + 56, 120, dash="4,3", color=GREY))
        o.append(_line(xx + 4, 126, xx + 56, 126, dash="4,3", color=GREY))
    o.append(_poly([(430, 106), (500, 110), (500, 140), (430, 134)],
                   fill="url(#h6)", sw=1.3, close=True))
    o.append(_rect(440, 114, 50, 18, fill="#fbfaf7", sw=1.0))
    o.append(_path("M500,120 H560 Q572,120 572,134 V156",
                   fill="none", sw=1.6, color=BLUE))
    o.append(_path("M500,126 H552 Q566,126 566,138 V156",
                   fill="none", sw=1.6, color=RED))
    o.append(T(150, 88, "Thermocouple element", 7.6))
    o.append(_ar(150, 92, 150, 114))
    o.append(T(280, 88, "Thermocouple beads", 7.6))
    o.append(_ar(280, 92, 280, 114))
    o.append(T(468, 176, "Thermocouple head", 7.6))
    o.append(_ar(468, 170, 468, 140))
    o.append(T(588, 88, "Extension cable", 7.6, anchor="start"))
    o.append(_ar(584, 91, 550, 120))
    o.append(T(76, 166, "Fused junction", 7.2))
    o.append(_ar(76, 162, 50, 128))
    return _mk(11, o, "Thermocouple beads and head",
               "Hat nhiet dien va dau noi day nhiet ou",
               "Thermocouple elements, insulator beads and head",
               "So do hai day nhiet ou di qua bon hat gioi tu roi vao dau dau day va cap noi dai",
               "Thermocouple wires pass through refractory insulator beads before terminating in the connection head")


# ---------------------------------------------------------------- 3.12
@_reg
def fig_f12():
    """Fig. 3.12 - complete thermocouple assembly."""
    o = [_defs()]
    o.append(_line(56, 114, 72, 114, sw=1.6, color=BLUE))
    o.append(_rect(72, 104, 16, 20, fill="#dde4ee", sw=1.1))
    o.append(_ellipse(112, 114, 32, 44, fill="#eef3fb", sw=1.4))
    o.append(_ellipse(112, 114, 20, 32, fill="#ffffff", sw=0.9))
    o.append(_rect(144, 108, 52, 12, fill="#eef3fb", sw=1.2))
    o.append(_poly([(196, 96), (212, 104), (212, 124), (196, 132),
                    (180, 124), (180, 104)], fill="#dfe5ec", sw=1.2, close=True))
    o.append(_poly([(244, 94), (260, 102), (260, 126), (244, 134),
                    (228, 126), (228, 102)], fill="#dfe5ec", sw=1.2, close=True))
    o.append(_rect(212, 106, 32, 8, fill="#eef3fb", sw=1.0))
    o.append(_rect(260, 109, 250, 11, fill="#f3f6fa", sw=1.2))
    o.append(_path("M510,109 H534 L560,114 L534,120 H510 Z",
                   fill="#f3f6fa", sw=1.2))
    o.append(_line(300, 114, 510, 114, sw=0.5, color=GREY))
    o.append(T(112, 58, "Thermocouple head", 8.0))
    o.append(_ar(112, 62, 112, 72))
    o.append(T(238, 58, "Adjustable coupling", 8.0))
    o.append(_ar(238, 62, 238, 95))
    o.append(T(440, 58, "Thermowell", 8.0))
    o.append(_ar(440, 62, 440, 109))
    return _mk(12, o, "Complete thermocouple assembly",
               "Cap nhiet ou hoan chinh gom dau, khop dieu chinh va ong bao ve",
               "Complete thermocouple ready for installation",
               "So do cap nhiet ou hoan chinh voi dau dau day, khop dieu chinh va ong thermowell",
               "Complete thermocouple assembly with head, adjustable coupling and thermowell")


# ---------------------------------------------------------------- 3.13
@_reg
def fig_f13():
    """Fig. 3.13 - taper shank threaded thermowell."""
    o = [_defs()]
    o.append(_path("M300,60 H360 V178 Q360,186 352,186 H308 Q300,186 300,178 Z",
                   fill="url(#h6)", sw=1.4))
    for yy in (70, 78, 86, 94, 158, 166, 174):
        o.append(_line(300, yy, 360, yy, sw=0.8, color=GREY))
    o.append(_path("M360,96 C440,101 500,109 552,116 Q564,118 552,120 "
                   "C500,128 440,140 360,144 Z", fill="#eef3fb", sw=1.4))
    o.append(_line(360, 48, 360, 192, dash="5,4", color=GREY))
    o.append(T(330, 40, "Threaded shank", 7.8))
    o.append(_ar(330, 44, 330, 68))
    o.append(T(460, 74, "Tapered portion", 7.8))
    o.append(_ar(460, 78, 460, 108))
    o.append(T(476, 164, "Rounded tip", 7.8))
    o.append(_ar(476, 160, 546, 122))
    o.append(T(248, 142, "Mounting shoulder", 7.8, anchor="end"))
    o.append(_ar(252, 139, 302, 139))
    return _mk(13, o, "Taper shank threaded thermowell",
               "Ong bao ve nhiet ke co ren va phan thon dan den dau tron",
               "Taper shank threaded thermowell",
               "So do ong thermowell co doan ren va thanh thon dan ve phia dau tron",
               "Threaded thermowell with a tapered shank that provides strength against flow vibration")


# ---------------------------------------------------------------- 3.14
@_reg
def fig_f14():
    """Fig. 3.14 - thermonozzle construction."""
    o = [_defs()]
    o.append(_poly([(280, 55), (360, 55), (360, 155), (340, 175),
                    (300, 175), (280, 155)], fill="url(#h6)",
                   sw=1.4, close=True))
    o.append(_rect(302, 55, 36, 82, fill="#fbfaf7", sw=1.1))
    for yy in (72, 84, 96, 108):
        o.append(_zig((302, yy), (308, yy), n=2, amp=2.0, color=GREY, sw=0.7))
        o.append(_zig((332, yy), (338, yy), n=2, amp=2.0, color=GREY, sw=0.7))
    o.append(_line(320, 42, 320, 186, dash="5,4", color=GREY))
    o.append(T(450, 90, "Thermonozzle", 7.8, anchor="start"))
    o.append(_ar(446, 87, 362, 87))
    o.append(T(180, 100, "Threaded bore", 7.8, anchor="end"))
    o.append(_ar(184, 97, 302, 97))
    o.append(T(450, 160, "Chamfered end", 7.8, anchor="start"))
    o.append(_ar(446, 157, 344, 164))
    return _mk(14, o, "Thermonozzle construction",
               "Mat cat cau tao cua ong noi thermonozzle co ren trong",
               "Thermonozzle construction detail",
               "So do mat cat thermonozzle bang thep co ren ben trong va dau vat goc",
               "Section of a thermonozzle showing its threaded bore and chamfered lower end")


# ---------------------------------------------------------------- 3.15
@_reg
def fig_f15():
    """Fig. 3.15 - thermonozzle welded on a pipeline."""
    o = [_defs()]
    o.append(_rect(100, 124, 480, 52, fill="#f3f6fa", sw=1.2))
    o.append(_ellipse(100, 150, 12, 26, fill="url(#h6)", sw=1.2))
    o.append(_ellipse(580, 150, 12, 26, fill="url(#h6)", sw=1.2))
    o.append(_line(88, 150, 592, 150, dash="6,4", color=GREY))
    o.append(_poly([(320, 70), (370, 70), (370, 150), (320, 150)],
                   fill="url(#h6)", sw=1.3, close=True))
    o.append(_rect(332, 74, 26, 82, fill="#fbfaf7", sw=1.1))
    o.append(_poly([(320, 124), (332, 116), (344, 124)],
                   fill="#d9dde2", sw=0.8, close=True))
    o.append(_poly([(346, 124), (358, 116), (370, 124)],
                   fill="#d9dde2", sw=0.8, close=True))
    o.append(_line(345, 58, 345, 182, dash="5,4", color=GREY))
    o.append(T(180, 104, "Pipeline", 7.8, anchor="start"))
    o.append(_ar(196, 107, 224, 126))
    o.append(T(450, 86, "Thermowell", 7.8, anchor="start"))
    o.append(_ar(446, 83, 358, 80))
    o.append(T(450, 116, "Seal weld", 7.8, anchor="start"))
    o.append(_ar(446, 113, 372, 124))
    o.append(T(150, 200, "Centreline", 7.4))
    o.append(_ar(150, 194, 280, 153))
    return _mk(15, o, "Thermonozzle on a pipeline",
               "Lap dat ong noi nhiet ou len duong ong bang han kín",
               "Typical thermonozzle installation on a pipeline",
               "So do ong noi thermonozzle duoc han vao duong ong va ong bao ve chen vao ben trong",
               "Thermonozzle welded to a pipe with the thermowell inserted and seal-welded in place")


# ---------------------------------------------------------------- 3.16
@_reg
def fig_f16():
    """Fig. 3.16 - complete thermowell and thermonozzle installation."""
    o = [_defs()]
    o.append(_rect(80, 127, 520, 56, fill="#f3f6fa", sw=1.2))
    o.append(_ellipse(80, 155, 13, 28, fill="url(#h6)", sw=1.2))
    o.append(_ellipse(600, 155, 13, 28, fill="url(#h6)", sw=1.2))
    o.append(_line(70, 155, 610, 155, dash="6,4", color=GREY))
    o.append(_rect(310, 105, 60, 34, fill="url(#h6)", sw=1.3))
    o.append(_poly([(310, 127), (322, 119), (334, 127)],
                   fill="#d9dde2", sw=0.8, close=True))
    o.append(_poly([(346, 127), (358, 119), (370, 127)],
                   fill="#d9dde2", sw=0.8, close=True))
    o.append(_rect(295, 76, 90, 18, fill="#dfe5ec", sw=1.3))
    o.append(_rect(325, 94, 30, 82, fill="url(#h7)", sw=1.2))
    o.append(_path("M325,168 Q325,182 340,182 Q355,182 355,168 Z",
                   fill="#dfe5ec", sw=1.2))
    o.append(_line(340, 62, 340, 196, dash="5,4", color=GREY))
    o.append(T(200, 80, "Thermowell", 7.8, anchor="start"))
    o.append(_ar(196, 77, 294, 80))
    o.append(T(460, 100, "Thermonozzle", 7.8, anchor="start"))
    o.append(_ar(456, 97, 372, 110))
    o.append(T(460, 134, "Seal weld", 7.8, anchor="start"))
    o.append(_ar(456, 131, 372, 126))
    o.append(T(160, 118, "Main pipeline", 7.8, anchor="start"))
    o.append(_ar(176, 121, 210, 129))
    o.append(T(160, 206, "Centreline", 7.8, anchor="start"))
    o.append(_ar(156, 202, 300, 158))
    return _mk(16, o, "Thermowell and thermonozzle installation",
               "Lap dat day du ong bao ve, ong noi va duong ong chinh",
               "Complete thermowell and thermonozzle installation",
               "So toan bo ong bao ve nhiet ou duoc ren vao ong noi da han tren duong ong chinh",
               "Full installation with thermowell screwed into a thermonozzle on the main pipeline, tip below the centreline")


# ---------------------------------------------------------------- 3.17
@_reg
def fig_f17():
    """Fig. 3.17 - angled thermowell installation."""
    o = [_defs()]
    o.append(_rect(100, 124, 480, 52, fill="#f3f6fa", sw=1.2))
    o.append(_ellipse(100, 150, 12, 26, fill="url(#h6)", sw=1.2))
    o.append(_ellipse(580, 150, 12, 26, fill="url(#h6)", sw=1.2))
    o.append(_line(88, 150, 592, 150, dash="6,4", color=GREY))
    o.append(_poly([(299.3, 89.1), (346.3, 154.1), (357.7, 145.9),
                    (310.7, 80.9)], fill="#eef3fb", sw=1.3, close=True))
    o.append(_poly([(280, 70), (318, 85), (312, 98), (274, 83)],
                   fill="url(#h6)", sw=1.2, close=True))
    o.append(_line(296, 74, 353, 158, dash="5,4", color=GREY))
    o.append(T(250, 55, "Thermowell at an angle", 7.8))
    o.append(_ar(250, 59, 292, 76))
    o.append(T(450, 70, "Installation angle", 7.8, anchor="start"))
    o.append(_ar(446, 73, 334, 100))
    o.append(T(150, 202, "Pipe centreline", 7.6))
    o.append(_ar(150, 196, 280, 153))
    return _mk(17, o, "Angled thermowell installation",
               "Lap dat ong bao ve nghieng khi khong the dat vuong goc",
               "Thermowell installed at an angle on a pipeline",
               "So do ong bao ve nhiet ou dat nghieng tren duong ong khi khong lap vuong goc duoc",
               "Thermowell mounted at an inclined angle when perpendicular installation is not possible")


# ---------------------------------------------------------------- 3.18
@_reg
def fig_f18():
    """Fig. 3.18 - thermowell installed in an elbow."""
    o = [_defs()]
    d = "M100,160 L340,160 Q395,160 395,105 L395,72"
    o.append(_path(d, sw=54, color=INK))
    o.append(_path(d, sw=52, color="#f3f6fa"))
    o.append(_path(d, sw=1.0, dash="6,4", color=GREY))
    o.append(_rect(385, 40, 20, 90, fill="#eef3fb", sw=1.2))
    o.append(_rect(375, 30, 40, 12, fill="#dfe5ec", sw=1.2))
    o.append(_ar(150, 160, 230, 160, color=GREEN))
    o.append(T(190, 142, "Flow", 7.4, color=GREEN))
    o.append(T(236, 104, "Elbow", 7.8))
    o.append(_ar(240, 108, 350, 144))
    o.append(T(460, 62, "Thermowell", 7.8, anchor="start"))
    o.append(_ar(456, 65, 408, 66))
    o.append(T(460, 196, "In the elbow", 7.8, anchor="start"))
    o.append(_ar(456, 192, 400, 130))
    return _mk(18, o, "Thermowell in an elbow",
               "Lap dat ong bao ve nhiet ou tai khuyp cong cua duong ong",
               "Thermowell installed in a pipeline elbow",
               "So do ong bao ve nhiet ou dat thang dung tai dat cong ong",
               "Thermowell installed vertically in a pipe elbow to obtain a representative temperature reading")
