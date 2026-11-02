# -*- coding: utf-8 -*-
"""Figures 89.1–89.5 for Handbook Chapter 89 — Electromagnetic Compatibility.

89.1  the source–path–receptor model
89.2  a typical industrial grounding situation, showing a ground loop
89.3  shielding effectiveness curves for copper
89.4  two high-frequency shielding failure modes
89.5  an open-field test site

89.3 is measured data and was digitised from the printed page, not modelled:
the 400 dpi page raster gave the plot box (left axis x=642, 300 dB at y=426,
0 dB at y=1794) and the nine decade lines (x=642…2453 for 0.1 kHz…10 GHz).
Each curve was then sampled column-wise with the grid lines and the four
in-figure labels masked out. The four curves are: E-field reflection (275 dB
at 0.1 kHz), plane-wave reflection (150 dB), H-field reflection (24 dB),
and absorption (about 5 dB until 1 MHz, then rising to 265 dB at 10 GHz).
The three reflection curves converge onto the plane-wave value near 300 MHz,
exactly as the printed figure shows, so E and H terminate where they merge.

89.1 and 89.4 were read off the page in the same way. 89.2 and 89.5 are
line drawings rebuilt from the printed originals.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content.
"""
import math

from hbfig import svg, _fig
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, _defs, _lbl, _r,
                      _line, _arr, _rect, _poly, _path, _dot, _circ, _hatch, Frame)

GREY = "#8a8a8a"
PALE = "#c9c9c9"


# ================================================================ 89.1
_SRC = [(0, "Vi xử lý"), (0, "Mạch lái video"), (0, "ESD"), (0, "Máy phát"),
        (0, "Máy tạo RF"), (0, "Nhiễu nguồn"), (0, "Sét")]
_PAT = [(0, "Bức xạ"), (1, "Trường điện từ"),
        (1, "Nhiễu chéo: điện dung,"), (1, "cảm ứng"),
        (0, "Dẫn"), (1, "Tín hiệu"), (1, "Nguồn"), (1, "Đất")]
_RCP = [(0, "Kỹ thuật số"), (0, "Vi xử lý"), (0, "Reset"), (0, "Logic khác"),
        (0, "Tương tự mức thấp"), (0, "Máy thu")]


def fig_89_1():
    tag = "891"
    o = [_defs(tag)]
    o.append(_lbl(340, 18, "Mọi vấn đề nhiễu đều có thể tách thành", "tm", "middle"))
    o.append(_lbl(206, 40, "•  NGUỒN gây nhiễu", "ts", "start"))
    o.append(_lbl(206, 58, "•  ĐỐI TƯỢNG THU bị nhiễu", "ts", "start"))
    o.append(_lbl(206, 76, "•  ĐƯỜNG dẫn nhiễu từ nguồn tới đối tượng thu", "ts", "start"))

    cols = [(14, "NGUỒN", _SRC, GOLD), (250, "ĐƯỜNG", _PAT, BLUE), (486, "THU", _RCP, TEAL)]
    w, h = 180, 200
    for x, head, items, col in cols:
        o.append(_rect(x, 98, w, h, 1.2, "#fff"))
        o.append(_rect(x, 98, w, 24, 1.2, "#f2f2f2"))
        o.append(_lbl(x + w / 2.0, 115, head, "tm", "middle"))
        o.append(_line(x, 122, x + w, 122, 1.0, col))
        for i, (lvl, it) in enumerate(items):
            if lvl == 0:
                o.append(_lbl(x + 9, 144 + i * 19, "• " + it, "ts", "start"))
            else:
                o.append(_lbl(x + 22, 144 + i * 19, it, "ts", "start"))
    o.append(_arr(198, 198, 246, 198, tag))
    o.append(_arr(434, 198, 482, 198, tag))
    return _fig(
        svg(680, 316, "".join(o), "Mô hình nguồn–đường–đối tượng thu"),
        "Hình 89.1 · Mô hình nguồn–đường–đối tượng thu để đánh giá các vấn đề nhiễu điện từ. "
        "Cả ba thành phần đều phải cùng tồn tại thì nhiễu mới xảy ra.",
        "Figure 89.1 · The source–path–receptor model for assessing EMI problems. All three "
        "elements must be present for an EMI problem to occur.",
        "Sơ đồ ba cột: nguồn gây nhiễu, đường dẫn nhiễu và đối tượng thu bị nhiễu",
        "Three-column model: interference sources, coupling paths and receptors")


# ================================================================ 89.2
def _gnd_diag(x, y):
    """Earth symbol: stub, bar, and diagonal hatching below it."""
    o = [_line(x, y, x, y + 11, 1.5), _line(x - 23, y + 11, x + 23, y + 11, 1.5)]
    for i in range(5):
        o.append(_line(x - 20 + i * 9, y + 11, x - 11 + i * 9, y + 25, 1.0, GREY))
    return "".join(o)


def _gnd_cross(x, y):
    """Chassis/signal symbol: stub, bar, and cross-hatching below it."""
    o = [_line(x, y, x, y + 11, 1.5), _line(x - 23, y + 11, x + 23, y + 11, 1.5)]
    for i in range(5):
        o.append(_line(x - 20 + i * 9, y + 11, x - 11 + i * 9, y + 25, 1.0, GREY))
        o.append(_line(x + 20 - i * 9, y + 11, x + 11 - i * 9, y + 25, 1.0, GREY))
    return "".join(o)


def fig_89_2():
    tag = "892"
    o = [_defs(tag)]
    # two pieces of equipment
    o.append(_rect(52, 52, 116, 92, 1.3, "#fff"))
    o.append(_rect(512, 52, 116, 92, 1.3, "#fff"))
    # signal pair between them
    o.append(_line(168, 80, 512, 80, 1.3))
    o.append(_line(168, 104, 512, 104, 1.3))
    o.append(_lbl(340, 70, "Tín hiệu", "tm", "middle"))
    # drops from the return conductor
    o.append(_line(206, 104, 206, 252, 1.3))
    o.append(_line(474, 104, 474, 252, 1.3))
    # common ground impedance, with the noise voltage across it
    o.append(_line(206, 252, 322, 252, 1.3))
    o.append(_line(358, 252, 474, 252, 1.3))
    o.append(_circ(340, 252, 17, E, "#fff", 1.2))
    o.append(_r(340, 257, [("V", False), ("n", True)], "middle", "ts"))
    # loop current: an almost-complete circle, with a tangential arrowhead
    cx, cy, r = 340, 176, 32
    arc = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in range(300, 29, -4)]
    o.append(_path(arc, 1.4, RED))
    a = math.radians(30)
    ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
    tx, ty = math.sin(a), -math.cos(a)          # direction of travel
    nx, ny = math.cos(a), math.sin(a)           # outward normal
    o.append(_poly([(ex + tx * 13, ey + ty * 13),
                    (ex + nx * 6.5, ey + ny * 6.5),
                    (ex - nx * 6.5, ey - ny * 6.5)], 1.0, RED, RED))
    o.append(_lbl(cx, cy + 4, "A", "tm", "middle"))
    # ground symbols
    o.append(_gnd_diag(206, 252))
    o.append(_gnd_cross(474, 252))
    return _fig(
        svg(680, 306, "".join(o), "Sơ đồ nối đất công nghiệp và vòng đất"),
        "Hình 89.2 · Tình huống nối đất công nghiệp điển hình, đồng thời minh hoạ một vòng đất. "
        "Dòng nhiễu chạy vòng qua trở kháng đất chung, sinh ra điện áp nhiễu V(n).",
        "Figure 89.2 · A typical industrial grounding situation, which also illustrates a ground "
        "loop. The circulating current develops a noise voltage V(n) across the common ground "
        "impedance.",
        "Hai thiết bị nối với nhau bằng cặp dây tín hiệu và một đường đất chung, với dòng điện "
        "chạy vòng và điện áp nhiễu trên trở kháng đất chung",
        "Two units joined by a signal pair and a shared ground return, with a circulating loop "
        "current and a noise voltage across the common ground impedance")


# ================================================================ 89.3
# Digitised from the printed plot: (frequency in kHz, shielding loss in dB).
_C_E = [(0.126, 275), (0.201, 265), (0.32, 257), (0.81, 242), (1.292, 236),
        (2.064, 229), (3.3, 224), (5.275, 218), (8.432, 213), (48.279, 193),
        (74.438, 188), (115.478, 183), (181.522, 177), (285.336, 172),
        (448.524, 167), (705.041, 162), (1107.757, 156), (2726.186, 144),
        (4276.723, 139), (6709.137, 132), (16332.154, 120), (25371.598, 114),
        (39414.151, 108), (61228.909, 101), (150408.62, 89), (238381.598, 82),
        (377809.372, 80)]

_C_P = [(0.201, 146), (0.32, 143), (0.509, 140), (0.81, 138), (5.275, 129),
        (8.432, 126), (13.172, 124), (20.309, 122), (31.313, 120),
        (48.279, 118), (74.438, 117), (115.478, 115), (181.522, 113),
        (285.336, 112), (448.524, 110), (1107.757, 107), (1737.801, 105),
        (2726.186, 103), (4276.723, 101), (6709.137, 99), (16332.154, 95),
        (25371.598, 93), (39414.151, 91), (61228.909, 89), (150408.62, 85),
        (238381.598, 81), (377809.372, 80), (598787.502, 78), (949014.236, 76),
        (1444894.259, 74), (2188587.601, 72), (3315063.13, 70),
        (5021340.5, 68), (7605846.232, 67)]

_C_H = [(0.126, 24), (0.201, 26), (0.32, 28), (0.509, 30), (0.81, 32),
        (1.292, 34), (2.064, 36), (3.3, 38), (5.275, 40), (74.438, 55),
        (115.478, 57), (181.522, 60), (285.336, 62), (448.524, 64),
        (705.041, 67), (1107.757, 68), (1737.801, 70), (4276.723, 73),
        (6709.137, 74), (16332.154, 76), (39414.151, 78), (61228.909, 78),
        (150408.62, 80), (238381.598, 80), (377809.372, 80)]

_C_A = [(1.292, 5), (2.064, 5), (5.275, 5), (8.432, 5), (13.172, 5),
        (20.309, 5), (31.313, 5), (48.279, 5), (74.438, 5), (115.478, 5),
        (181.522, 5), (285.336, 6), (448.524, 5), (705.041, 6), (1107.757, 6),
        (1737.801, 6), (2726.186, 6), (4276.723, 6), (6709.137, 7),
        (16332.154, 13), (25371.598, 16), (39414.151, 21), (61228.909, 25),
        (150408.62, 39), (238381.598, 48), (377809.372, 60), (598787.502, 73),
        (1444894.259, 110), (2188587.601, 136), (3315063.13, 172),
        (5021340.5, 209), (7605846.232, 265)]


def fig_89_3():
    tag = "893"
    o = [_defs(tag)]
    F = Frame(104, 34, 512, 300, (0.1, 1e7), (0, 300), xlog=True)
    o.append(F.hgrid([50, 100, 150, 200, 250], GRID, 0.9))
    o.append(F.vgrid([1, 10, 100, 1e3, 1e4, 1e5, 1e6], GRID, 0.9))
    o.append(F.frame())
    o.append(F.yticks([(0, "0"), (50, "50"), (100, "100"), (150, "150"),
                       (200, "200"), (250, "250"), (300, "300")], dx=8, cls="ts"))
    o.append(F.xticks([(0.1, "0,1"), (1, "1"), (10, "10"), (100, "100"),
                       (1e3, "1"), (1e4, "10"), (1e5, "100"),
                       (1e6, "1"), (1e7, "10")], dy=14, cls="ts"))
    # unit row under the decade labels, centred on each decade group
    o.append(_lbl(F.X(3.16), 372, "kHz", "ts", "middle"))
    o.append(_lbl(F.X(1e4), 372, "MHz", "ts", "middle"))
    o.append(_lbl(F.X(3.16e6), 372, "GHz", "ts", "middle"))
    o.append(_lbl(340, 396, "Tần số", "tm", "middle"))
    o.append(_lbl(44, 178, "SE", "tm", "middle"))
    o.append(_lbl(44, 194, "dB", "tm", "middle"))
    for data in (_C_E, _C_P, _C_H, _C_A):
        o.append(_path([(F.X(f), F.Y(v)) for f, v in data], 1.5, E))
    o.append(_lbl(F.X(1.0), 150, "Suy hao phản xạ", "ts", "start"))
    o.append(_lbl(F.X(1.0), 164, "trường điện (E)", "ts", "start"))
    o.append(_lbl(F.X(0.13), 214, "Suy hao phản xạ", "ts", "start"))
    o.append(_lbl(F.X(0.13), 228, "sóng phẳng", "ts", "start"))
    o.append(_lbl(F.X(3.2), 250, "Suy hao phản xạ", "ts", "start"))
    o.append(_lbl(F.X(3.2), 264, "trường từ (H)", "ts", "start"))
    o.append(_lbl(F.X(1.1e5), 74, "Suy hao hấp thụ,", "ts", "start"))
    o.append(_lbl(F.X(1.1e5), 88, "dB trên mil", "ts", "start"))
    return _fig(
        svg(680, 412, "".join(o), "Hiệu quả che chắn của đồng theo tần số"),
        "Hình 89.3 · Đường cong hiệu quả che chắn điển hình của đồng. Hai cơ chế (phản xạ và hấp "
        "thụ) và ba loại trường (điện, từ và sóng phẳng) cùng thể hiện trên một đồ thị; che chắn "
        "bằng nhôm gần như giống hệt đồng.",
        "Figure 89.3 · Typical shielding effectiveness curves for copper. Note two mechanisms "
        "(reflection and absorption) and three types of fields (electric, magnetic, and plane "
        "wave). Shielding for aluminum is almost the same as for copper.",
        "Đồ thị hiệu quả che chắn theo tần số, từ 0,1 kHz đến 10 GHz, với bốn đường cong",
        "Shielding effectiveness against frequency from 0.1 kHz to 10 GHz, four curves")


# ================================================================ 89.4
def _fan(cx, cy, radii, a0, a1, n=11):
    """A fan of wavefront arcs centred on (cx, cy), from a0 to a1 degrees."""
    o = []
    for r in radii:
        p = []
        for k in range(n):
            a = math.radians(a0 + (a1 - a0) * k / (n - 1.0))
            p.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        o.append(_path(p, 1.1))
    return "".join(o)


def _dimv(y1, y2, x, tag, col=GREY):
    """A vertical double-headed dimension segment with witness ticks."""
    mid = (y1 + y2) / 2.0
    o = [_line(x, y1, x, y2, 0.8, col),
         _arr(x, mid, x, y1, tag, 1.0, col),
         _arr(x, mid, x, y2, tag, 1.0, col)]
    for y in (y1, y2):
        o.append(_line(x - 5, y, x + 5, y, 0.9, col))
    return "".join(o)


def fig_89_4():
    tag = "894"
    o = [_defs(tag)]

    # ---- left panel: a shield wall seen edge-on, broken by a slot
    o.append(_lbl(196, 22, "Rò rỉ ở khe", "tm", "middle"))
    o.append(_lbl(196, 38, "và mối nối", "tm", "middle"))
    o.append(_rect(192, 74, 9, 46, 1.0, "#dedede"))
    o.append(_rect(192, 160, 9, 46, 1.0, "#dedede"))
    o.append(_fan(196.5, 140, (16, 24, 32, 38), 160, 200))
    o.append(_fan(196.5, 140, (16, 24, 32, 38), 340, 380))
    o.append(_dimv(120, 160, 146, tag))
    o.append(_lbl(138, 143, "khe hở", "ts", "end"))

    # ---- right panel: a conductor passing through a shield plate
    o.append(_lbl(490, 22, "Dây dẫn", "tm", "middle"))
    o.append(_lbl(490, 38, "xuyên qua vách", "tm", "middle"))
    o.append(_rect(390, 136, 200, 6, 1.0, "#dedede"))
    o.append(_rect(485, 88, 9, 48, 1.0, "#dedede"))
    o.append(_rect(485, 142, 9, 64, 1.0, "#dedede"))
    o.append(_fan(489.5, 136, (15, 22, 29, 36), 186, 244))
    o.append(_fan(489.5, 136, (15, 22, 29, 36), 296, 354))
    o.append(_lbl(596, 144, "vách chắn", "ts", "start"))
    o.append(_lbl(505, 200, "dây dẫn", "ts", "start"))
    return _fig(
        svg(680, 246, "".join(o), "Hai kiểu hỏng che chắn ở tần số cao"),
        "Hình 89.4 · Hai kiểu hỏng che chắn: do khe/mối nối và do dây dẫn xuyên qua vách. Trong cả "
        "hai trường hợp, kích thước tới hạn là 1/20 bước sóng ở tần số cao nhất cần xét.",
        "Figure 89.4 · Two shielding failure modes, due to slots/seams and due to penetration of "
        "conductors. In both cases, the critical dimension is 1/20 wavelength for the highest "
        "frequency of concern.",
        "Hai sơ đồ nhỏ: rò rỉ qua khe trên vách chắn, và dây dẫn xuyên qua vách chắn, kèm các cung "
        "sóng thoát ra hai bên",
        "Two small diagrams: leakage through a slot in a shield wall, and a conductor passing "
        "through a shield, each with escaping wavefronts on both sides")


# ================================================================ 89.5
def _ellipse(cx, cy, rx, ry, n=72):
    return [(cx + rx * math.cos(2 * math.pi * i / n),
             cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]


def _dim(x1, x2, y, tag, col=GREY):
    """A double-headed dimension segment with witness ticks at both ends."""
    mid = (x1 + x2) / 2.0
    o = [_line(x1, y, x2, y, 0.8, col),
         _arr(mid, y, x1, y, tag, 1.0, col),
         _arr(mid, y, x2, y, tag, 1.0, col)]
    for x in (x1, x2):
        o.append(_line(x, y - 5, x, y + 5, 0.9, col))
    return "".join(o)


def fig_89_5():
    tag = "895"
    o = [_defs(tag)]
    # ground plane boundary
    o.append(_path(_ellipse(336, 196, 248, 62), 1.1, GREY, "5 5"))
    # turntable
    o.append(_path(_ellipse(140, 224, 46, 12), 1.2))
    o.append(_path(_ellipse(140, 218, 46, 12), 1.0))
    # table
    o.append(_line(106, 172, 178, 172, 1.4))
    o.append(_line(114, 172, 114, 220, 1.1, GREY))
    o.append(_line(170, 172, 170, 220, 1.1, GREY))
    # device under test: a monitor on the table
    o.append(_rect(120, 132, 40, 34, 1.3, "#fff"))
    o.append(_rect(125, 137, 30, 23, 1.0, "#e6e6e6"))
    o.append(_rect(116, 166, 48, 6, 1.3, "#fff"))
    # antenna mast and dipole
    o.append(_line(520, 54, 520, 246, 2.2))
    o.append(_line(527, 88, 527, 148, 1.3))
    o.append(_line(520, 118, 527, 118, 1.1))
    # leaders and labels
    o.append(_arr(150, 120, 140, 130, tag, 1.0))
    o.append(_lbl(150, 96, "Thiết bị cần đo", "ts", "middle"))
    o.append(_arr(470, 124, 512, 150, tag, 1.0))
    o.append(_lbl(430, 106, "Mặt phẳng đất ít nhất", "ts", "middle"))
    o.append(_lbl(430, 120, "bằng elip", "ts", "middle"))
    o.append(_arr(542, 74, 524, 88, tag, 1.0))
    o.append(_lbl(546, 70, "Anten", "ts", "start"))
    # minor axis of the ellipse
    o.append(_arr(336, 134, 336, 258, tag, 1.0, GREY))
    o.append(_arr(336, 258, 336, 134, tag, 1.0, GREY))
    o.append(_lbl(348, 200, "5,2 hoặc 17,3 m", "ts", "start"))
    # distances along the major axis
    o.append(_dim(90, 140, 286, tag))
    o.append(_dim(140, 520, 286, tag))
    o.append(_dim(520, 584, 286, tag))
    o.append(_lbl(115, 304, "1,5 hoặc 5 m", "ts", "middle"))
    o.append(_lbl(330, 304, "3 hoặc 10 m", "ts", "middle"))
    o.append(_lbl(552, 304, "1,5 hoặc 5 m", "ts", "middle"))
    # buried cables, entering from the sides
    o.append(_line(58, 200, 100, 218, 1.2))
    o.append(_lbl(24, 194, "Nguồn", "ts", "start"))
    o.append(_lbl(24, 208, "điện", "ts", "start"))
    o.append(_line(620, 200, 524, 242, 1.2))
    o.append(_lbl(668, 192, "Đầu vào", "ts", "end"))
    o.append(_lbl(668, 206, "máy thu", "ts", "end"))
    return _fig(
        svg(680, 320, "".join(o), "Bãi thử trường mở"),
        "Hình 89.5 · Một bãi thử trường mở. Cáp nguồn và cáp anten được đi ngầm dưới mặt phẳng đất "
        "để không ảnh hưởng tới trường đo được. Vùng giới hạn bởi elip phải trống mọi thứ trừ "
        "thiết bị cần đo, bàn đặt nó và anten đo. Thiết bị được đặt trên bàn xoay để đo bức xạ "
        "theo mọi hướng; xoay nó trong khi đo và đồng thời thay đổi độ cao anten thu sẽ tìm ra "
        "hướng bức xạ cực đại.",
        "Figure 89.5 · An open-field test site. Power and antenna cables are run under the ground "
        "plane so that they will not affect measured fields. The area outlined by the ellipse must "
        "be free of everything except the device under test, the table on which it rests, and the "
        "measuring antenna. To facilitate measuring radiation in all directions from the device, it "
        "is placed on a turntable. By rotating it during testing, and simultaneously varying the "
        "height of the receiving antenna, the direction of maximum radiation is found.",
        "Hình phối cảnh bãi thử trường mở: thiết bị cần đo trên bàn xoay, anten thu trên cột, mặt "
        "phẳng đất hình elip và các kích thước 1,5 hoặc 5 m, 3 hoặc 10 m, 5,2 hoặc 17,3 m",
        "Perspective view of an open-field test site: the device on a turntable, the receiving "
        "antenna on a mast, an elliptical ground plane and the 1.5 or 5 m, 3 or 10 m and 5.2 or "
        "17.3 m dimensions")
