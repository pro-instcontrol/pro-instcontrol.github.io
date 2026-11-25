# -*- coding: utf-8 -*-
"""Vector figures 5.1-5.6 for PPIC chapter 5 (thorium/uranium block HTRs).

Each figure is a simplified vector redraw of the printed figure on PDF pages
99-107: the annular HTR core and hexagonal fuel block, the four spatial
separation levels, the one-sixth core model, the two-step calculation scheme,
the fuel-cycle cost time flow, and five compact configurations at 46% Th.
"""
import math

from ppicfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _tri_membership, make_registry)

FIGS, _reg = make_registry()

MOX = "#2e8b57"
ORANGE = "#d98416"
LIGHT = "#cfcfcf"


def _hexp(cx, cy, r, fill, sw=0.65, label=""):
    """Point-top hexagon, optionally lettered at its centre."""
    pts = [(cx + r * math.cos(math.radians(30 + 60 * k)),
            cy + r * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    o = [_poly(pts, fill=fill, sw=sw, color="#7a7a7a", close=True)]
    if label:
        o.append(T(cx, cy + 2.2, label, 6.2, color=INK))
    return "".join(o)


def _hexf(cx, cy, r, fill, sw=1.0, color=INK):
    """Flat-top hexagon (flat upper and lower edges)."""
    pts = [(cx + r * math.cos(math.radians(60 * k)),
            cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _hexfield(cx, cy, r, n, color_fn, sw=0.55):
    """Hexagonal cluster of small point-top cells in axial coordinates."""
    dx, dy = math.sqrt(3) * r, 1.5 * r
    o = []
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            hd = max(abs(a), abs(b), abs(a + b))
            if hd > n:
                continue
            px = cx + dx * (a + 0.5 * b)
            py = cy + dy * b
            col = color_fn(hd, px - cx, py - cy, a, b)
            if col is None:
                continue
            o.append(_hexp(px, py, r, col, sw=sw))
    return "".join(o)


def _disk(cx, cy, r, dots, fill="#d8d8d8"):
    """A fuel compact: grey binder disk with small TRISO dots."""
    o = [_circle(cx, cy, r, fill=fill, sw=0.9, color="#888888")]
    spots = [(0.0, 0.0)]
    for k in range(6):
        ang = math.radians(60 * k)
        spots.append((0.52 * r * math.cos(ang), 0.52 * r * math.sin(ang)))
    for k in range(6):
        ang = math.radians(30 + 60 * k)
        spots.append((0.80 * r * math.cos(ang), 0.80 * r * math.sin(ang)))
    for i, (dx0, dy0) in enumerate(spots):
        o.append(_circle(cx + dx0, cy + dy0, max(1.5, r * 0.115),
                         fill=dots[i % len(dots)], sw=0))
    return "".join(o)


def _triso(cx, cy, r, kernel, mid=None):
    """TRISO particle: binder shell, optional buffer, fuel kernel."""
    o = [_circle(cx, cy, r, fill="#cfcfcf", sw=0.8, color="#888888")]
    if mid is not None:
        o.append(_circle(cx, cy, r * 0.70, fill=mid, sw=0))
    o.append(_circle(cx, cy, r * 0.44, fill=kernel, sw=0))
    return "".join(o)


def _rot_text(x, y, s, size=7.0, color=INK):
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, x, y, size, color, s))


@_reg
def fig_f01():
    """Figure 5.1 - annular HTR core and hexagonal fuel block prism."""
    o = [_defs()]
    o.append(T(340, 14, "Thorium-fueled HTR reactor core and fuel block",
               8.8, color=INK, weight="600"))

    # (a) reactor core: annular hexagonal fuel zone inside two reflector rings
    o.append(T(160, 28, "(a) Reactor core", 7.6, color=INK))
    cx, cy = 165.0, 160.0
    o.append(_circle(cx, cy, 104, fill="#e2e2e2", sw=1.1, color=INK))
    o.append(_circle(cx, cy, 74, fill="none", sw=0.8, color="#666666"))

    def core_cell(hd, dx0, dy0, a, b):
        d = math.hypot(dx0, dy0)
        if d > 100:
            return None
        if d > 84:
            return "#cccccc"       # outer reflector
        if d > 74:
            return "#808080"       # inner reflector ring
        if d > 25:
            return RED             # annular fuel zone
        return "#b8b8b8"           # central reflector

    o.append(_hexfield(cx, cy, 10.5, 5, core_cell))
    o.append(T(22, 78, "Fuel zone", 7.0, color=INK, anchor="start"))
    o.append(_line(62, 81, 112, 115, sw=0.7, color=INK))
    o.append(T(22, 250, "Inner reflectors", 7.0, color=INK, anchor="start"))
    o.append(_line(82, 247, 110, 212, sw=0.7, color=INK))
    o.append(T(300, 80, "Outer reflectors", 7.0, color=INK, anchor="end"))
    o.append(_line(244, 83, 232, 108, sw=0.7, color=INK))

    # (b) hexagonal fuel block prism with axial channels
    o.append(T(515, 28, "(b) Fuel block", 7.6, color=INK))
    o.append(_line(459, 44, 571, 44, sw=0.8, color=INK))
    o.append(_line(459, 41, 459, 47, sw=0.8, color=INK))
    o.append(_line(571, 41, 571, 47, sw=0.8, color=INK))
    o.append(T(515, 41, "36 cm", 6.8, color=INK))
    o.append(_poly([(459, 95), (487, 143.5), (487, 258.5), (459, 210)],
                   fill="#b9d4e4", sw=0.9, color=INK, close=True))
    o.append(_poly([(487, 143.5), (543, 143.5), (543, 258.5), (487, 258.5)],
                   fill="#d3e6f1", sw=0.9, color=INK, close=True))
    o.append(_poly([(543, 143.5), (571, 95), (571, 210), (543, 258.5)],
                   fill="#a9c8dc", sw=0.9, color=INK, close=True))
    o.append(_hexf(515, 95, 56, "#dcecf6", sw=1.0))
    for i, xx in enumerate((494, 503, 512, 521, 530)):
        o.append(_line(xx, 146, xx, 256, sw=2.2,
                       color=RED if i % 2 == 0 else BLUE))
    for xx, y0, y1 in ((466, 105, 215), (474, 118, 228), (482, 131, 241)):
        o.append(_line(xx, y0, xx, y1, sw=1.9,
                       color=BLUE if xx == 474 else RED))
    for xx, y0, y1 in ((548, 131, 241), (556, 118, 228), (564, 105, 215)):
        o.append(_line(xx, y0, xx, y1, sw=1.9,
                       color=BLUE if xx == 556 else RED))
    o.append(_line(536, 147, 536, 255, sw=2.4, color="#555555", dash="4 2"))
    o.append(_ar(600, 52, 600, 254, color=INK, sw=0.8))
    o.append(_poly([(600, 46), (596, 55), (604, 55)],
                   fill=INK, sw=0, color=INK, close=True))
    o.append(_rot_text(613, 152, "80 cm", 7.0))
    o.append(_line(380, 279, 395, 279, sw=2.2, color=RED))
    o.append(T(399, 282, "Fuel rod", 6.4, color=INK, anchor="start"))
    o.append(_line(455, 279, 470, 279, sw=2.2, color=BLUE))
    o.append(T(474, 282, "Coolant channel", 6.4, color=INK, anchor="start"))
    o.append(_line(555, 279, 570, 279, sw=2.2, color="#555555", dash="4 2"))
    o.append(T(574, 282, "Burnable poison", 6.2, color=INK, anchor="start"))

    return _mk(1, o, "Thorium-fueled HTR core and fuel block",
               "Lõi lò HTR chạy bằng thori và khối nhiên liệu",
               "Thorium-fueled HTR core and fuel block",
               "Sơ đồ lõi lò phản ứng dạng vòng gồm vùng nhiên liệu hình lục giác màu đỏ, "
               "bộ phản xạ trong và ngoài màu xám, cùng khối nhiên liệu lục giác có kênh "
               "làm mát, than nhiên liệu và chất độc cháy cố định; kích thước 36 cm và 80 cm.",
               "Diagram of the annular reactor core with a red hexagonal fuel zone, inner "
               "and outer grey reflectors, and a hexagonal fuel block prism showing "
               "coolant channels, fuel rods and a fixed burnable poison; 36 cm across "
               "flats and 80 cm high.")


@_reg
def fig_f02():
    """Figure 5.2 - four levels of spatial separation of Th and U fuels."""
    o = [_defs()]
    o.append(T(340, 12, "red: uranium    blue: thorium    green: mixed fuel",
               6.4, color=GREY))
    for xx, lab in ((62, "TRISO"), (178, "Compact"), (330, "Block"),
                    (490, "Core"), (600, "Level")):
        o.append(T(xx, 24, lab, 6.6, color=GREY))

    def green_core(hd, dx0, dy0, a, b):
        if hd <= 1:
            return "#bdbdbd"
        if hd <= 3:
            return MOX
        return "#c9c9c9"

    def mixed_core(hd, dx0, dy0, a, b):
        if hd <= 1:
            return "#bdbdbd"
        if hd <= 3:
            return MOX
        return "#c9c9c9"

    def sb_core(hd, dx0, dy0, a, b):
        if hd <= 1:
            return MOX
        if hd == 2:
            return RED
        if hd == 3:
            return MOX
        return "#c9c9c9"

    def wasb_core(hd, dx0, dy0, a, b):
        if hd <= 2:
            return RED
        if hd <= 4:
            return BLUE
        return "#c9c9c9"

    def tiny_core(cx, cy, fn):
        return (_circle(cx, cy, 34, fill="#cfcfcf", sw=0.9, color="#888888")
                + _hexfield(cx, cy, 4.4, 4, fn, sw=0.4))

    def dashed(y):
        return "".join(_line(x0, y, x1, y, sw=0.8, color="#999999", dash="3 3")
                       for x0, x1 in ((82, 148), (206, 288), (370, 450)))

    # (a) no separation, Th/U MOX
    o.append(dashed(60))
    o.append(_triso(62, 60, 16, MOX, ORANGE))
    o.append(_disk(178, 60, 24, [MOX]))
    o.append(_hexf(330, 60, 34, "#e3e3e3", sw=0.9))
    o.append(_hexfield(330, 60, 4.4, 3,
                       lambda hd, dx0, dy0, a, b: MOX, sw=0.4))
    o.append(tiny_core(490, 60, green_core))
    o.append(T(600, 56, "(a) No separation", 7.2, color=INK, anchor="start"))
    o.append(T(600, 67, "(Th/U MOX)", 6.6, color=GREY, anchor="start"))

    # (b) TRISO-level separation
    o.append(dashed(130))
    o.append(_triso(62, 118, 13, RED, "#e6a08a"))
    o.append(_triso(62, 142, 13, BLUE, "#8fb2cc"))
    o.append(_disk(178, 118, 17, [RED]))
    o.append(_disk(178, 142, 17, [BLUE]))
    o.append(_hexf(330, 130, 34, "#e3e3e3", sw=0.9))
    o.append(_hexfield(330, 130, 4.4, 3,
                       lambda hd, dx0, dy0, a, b: RED if (a + b) % 2 == 0 else BLUE,
                       sw=0.4))
    o.append(tiny_core(490, 130, mixed_core))
    o.append(T(600, 126, "(b) TRISO level", 7.2, color=INK, anchor="start"))
    o.append(T(600, 137, "(SBT)", 6.6, color=GREY, anchor="start"))

    # (c) channel-level separation
    o.append(dashed(200))
    o.append(_triso(62, 188, 13, RED, "#e6a08a"))
    o.append(_triso(62, 212, 13, BLUE, "#8fb2cc"))
    o.append(_disk(178, 188, 17, [RED]))
    o.append(_disk(178, 212, 17, [BLUE]))

    def channel_block(hd, dx0, dy0, a, b):
        if hd <= 1:
            return "#999999"
        if hd <= 3:
            return RED
        return BLUE

    o.append(_hexf(330, 200, 34, "#e3e3e3", sw=0.9))
    o.append(_hexfield(330, 200, 3.8, 4, channel_block, sw=0.4))
    o.append(tiny_core(490, 200, sb_core))
    o.append(T(600, 196, "(c) Channel level", 7.2, color=INK, anchor="start"))
    o.append(T(600, 207, "(SBU)", 6.6, color=GREY, anchor="start"))

    # (d) block-level separation
    o.append(dashed(270))
    o.append(_triso(62, 258, 13, RED, "#e6a08a"))
    o.append(_triso(62, 282, 13, BLUE, "#8fb2cc"))
    o.append(_disk(178, 258, 17, [RED]))
    o.append(_disk(178, 282, 17, [BLUE]))
    o.append(_hexf(330, 255, 16, RED, sw=0.9))
    o.append(_hexfield(330, 255, 3.4, 2,
                       lambda hd, dx0, dy0, a, b: RED, sw=0.4))
    o.append(_hexf(330, 285, 16, BLUE, sw=0.9))
    o.append(_hexfield(330, 285, 3.4, 2,
                       lambda hd, dx0, dy0, a, b: BLUE, sw=0.4))
    o.append(tiny_core(490, 270, wasb_core))
    o.append(T(600, 266, "(d) Block level", 7.2, color=INK, anchor="start"))
    o.append(T(600, 277, "(WASB)", 6.6, color=GREY, anchor="start"))

    return _mk(2, o, "Four levels of spatial separation",
               "Bốn cấp độ tách biệt không gian",
               "Four levels of spatial separation",
               "Bốn hàng so sánh mức không tách biệt (Th/U MOX), tách biệt mức TRISO, "
               "tách biệt mức kênh và tách biệt mức khối; mỗi hàng thể hiện hạt TRISO, "
               "viên nhiên liệu, khối nhiên liệu và lõi, với uranium màu đỏ, thori màu "
               "xanh và nhiên liệu hỗn hợp màu xanh lá.",
               "Four rows compare no separation (Th/U MOX), TRISO-level, channel-level "
               "and block-level separation; each row traces TRISO particles, fuel "
               "compacts, fuel blocks and the core, with uranium in red, thorium in "
               "blue and mixed fuel in green.")


@_reg
def fig_f03():
    """Figure 5.3 - one-sixth core calculation model (triangular sector)."""
    o = [_defs()]
    o.append(T(340, 14, "Reactor core calculation model for 1/6 core",
               8.8, color=INK, weight="600"))
    o.append(_line(205, 22, 88, 240, sw=0.8, color=GREY, dash="4 3"))
    o.append(_line(205, 22, 322, 240, sw=0.8, color=GREY, dash="4 3"))

    def colour(j, i):
        k = j - 0.55 * i
        if k <= -4.2:
            return "#8a8a8a", "R"
        if k <= -3.4:
            return BLUE, "T"
        if k <= -2.4:
            return RED, "F"
        if k <= -1.3:
            return ORANGE, "O"
        return "#8a8a8a", "R"

    for i in range(9):
        y = 42 + i * 23.25
        for j in range(i + 1):
            x = 205 + (j - i / 2.0) * 26.8
            col, letter = colour(j, i)
            o.append(_hexp(x, y, 15.5, col, sw=0.7, label=letter))

    o.append(T(520, 56, "Legend", 7.6, color=INK, weight="600"))
    for y, col, lab in ((88, RED, "F Fuel"), (120, ORANGE, "O Fuel"),
                        (152, BLUE, "T Fuel"), (184, "#8a8a8a", "R Reflector")):
        o.append(_hexp(450, y, 12, col, sw=0.8))
        o.append(T(470, y + 2.5, lab, 7.0, color=INK, anchor="start"))
    o.append(T(520, 216, "One sixth of the annular core", 6.8, color=GREY))
    o.append(T(340, 268, "Diagonal bands: R reflector, O and F fuel, T fuel, R reflector",
               6.6, color=GREY))
    return _mk(3, o, "One-sixth core calculation model",
               "Mô hình tính toán lõi một phần sáu",
               "One-sixth core calculation model",
               "Mô hình tam giác gồm các khối nhiên liệu hình lục giác của một phần sáu lõi, "
               "với các dải chéo: bộ phản xạ xám R, nhiên liệu cam O, nhiên liệu đỏ F, "
               "nhiên liệu xanh T và bộ phản xạ xám; có chú giải màu bên phải.",
               "Triangular one-sixth core model of hexagonal blocks with diagonal bands "
               "of grey reflector R, orange fuel O, red fuel F, blue fuel T and grey "
               "reflector, with a colour legend at right.")


@_reg
def fig_f04():
    """Figure 5.4 - two-step calculation scheme flow."""
    o = [_defs()]
    o.append(T(340, 14, "Two-step calculation scheme", 9.0,
               color=INK, weight="600"))

    # (a) 2D fuel block lattice calculation
    o.append(_hexf(125, 115, 68, "#e8e8e8", sw=1.1))

    def block_cell(hd, dx0, dy0, a, b):
        return "#c4c4c4"

    o.append(_hexfield(125, 115, 5.2, 5, block_cell, sw=0.5))
    for a in range(-5, 6):
        for b in range(-5, 6):
            hd = max(abs(a), abs(b), abs(a + b))
            if hd > 5:
                continue
            px = 125 + math.sqrt(3) * 5.2 * (a + 0.5 * b)
            py = 115 + 1.5 * 5.2 * b
            if (a + b) % 3 == 0:
                o.append(_circle(px, py, 2.2, fill=RED, sw=0))
            elif (a - b) % 4 == 0:
                o.append(_circle(px, py, 2.2, fill=BLUE, sw=0))
    o.append(T(125, 205, "(a) Block calculation", 7.2, color=INK))
    o.append(T(125, 222, "red: fuel rod; blue: helium; grey: graphite",
               6.2, color=GREY))

    o.append(_ar(195, 115, 270, 115, color=BLUE, sw=1.4))
    o.append(T(232, 96, "few-group", 6.0, color=BLUE))
    o.append(T(232, 105, "cross sections", 6.0, color=BLUE))

    # (b) 1D annular reflector calculation
    o.append(_circle(335, 115, 55, fill="#bdbdbd", sw=1.0, color=INK))
    o.append(_circle(335, 115, 40, fill=RED, sw=0))
    o.append(_circle(335, 115, 17, fill="#bdbdbd", sw=0.8, color="#888888"))
    o.append(T(335, 205, "(b) Reflector calculation", 7.2, color=INK))
    o.append(T(335, 222, "inner reflector / fuel zone / outer reflector",
               6.2, color=GREY))

    o.append(_ar(395, 115, 470, 115, color=BLUE, sw=1.4))
    o.append(T(432, 96, "homogenized", 6.0, color=BLUE))
    o.append(T(432, 105, "cross sections", 6.0, color=BLUE))

    # (c) 2D full-core calculation with interface-current method
    o.append(_circle(560, 115, 68, fill="#c9c9c9", sw=1.0, color=INK))

    def full_core(hd, dx0, dy0, a, b):
        if hd <= 1:
            return "#bdbdbd"
        if hd <= 3:
            return RED
        return "#c9c9c9"

    o.append(_hexfield(560, 115, 8.0, 4, full_core, sw=0.6))
    o.append(T(560, 205, "(c) Full core calculation", 7.2, color=INK))
    o.append(T(560, 222, "1D annular data to 2D full core", 6.2, color=GREY))
    o.append(T(340, 264, "Lattice step (a), then core steps (b) and (c)",
               6.8, color=GREY))

    return _mk(4, o, "Two-step calculation scheme",
               "Sơ đồ tính toán hai bước",
               "Two-step calculation scheme",
               "Sơ đồ ba ô: (a) tính toán khối với các hạt nhiên liệu, heli và than chì; "
               "(b) tính toán bộ phản xạ với các vòng đồng tâm; (c) tính toán toàn lõi; "
               "mũi tên chuyển tiết diện nhóm ít giữa các bước.",
               "Flow of three panels: (a) block calculation with fuel rods, helium and "
               "graphite cells, (b) reflector calculation with concentric inner "
               "reflector, fuel zone and outer reflector, (c) full core calculation; "
               "arrows transfer few-group cross sections.")


@_reg
def fig_f05():
    """Figure 5.5 - time flow of fuel cycle cost, direct disposal option."""
    o = [_defs()]
    o.append(T(340, 14, "Time flow of nuclear fuel cycle cost (direct disposal)",
               8.8, color=INK, weight="600"))
    o.append(_ar(70, 200, 70, 52, color=INK, sw=1.0))
    o.append(_line(70, 200, 640, 200, sw=1.0, color=INK))
    o.append(_ar(640, 200, 654, 200, color=INK, sw=1.0))
    o.append(_rot_text(30, 130, "Relative cost", 7.0))
    o.append(T(650, 204, "Time", 7.0, color=INK, anchor="start"))

    bars = [(105, 88, "a", "#c9c9c9"), (160, 26, "b", "#c9c9c9"),
            (200, 24, "c", "#c9c9c9"), (250, 90, "d", "#c9c9c9"),
            (300, 46, "e", "#c9c9c9"), (430, 32, "g", "#c9c9c9"),
            (555, 60, "h", "#e8b4ae")]
    for xx, hh, letter, fill in bars:
        o.append(_rect(xx - 8, 200 - hh, 16, hh, fill, sw=0.8))
        o.append(T(xx, 195 - hh, letter, 7.0, color=INK, weight="600"))
        o.append(_line(xx, 202, xx, 240, sw=0.6, color="#bb6a5a", dash="2 2"))

    o.append(_line(350, 52, 350, 240, sw=1.0, color=RED, dash="4 3"))
    o.append(T(350, 46, "f", 7.0, color=RED, weight="600"))
    o.append(_ar(105, 234, 350, 234, color=RED, sw=1.0))
    o.append(T(227, 226, "Lead time", 6.8, color=RED))
    o.append(_ar(350, 250, 555, 250, color=RED, sw=1.0))
    o.append(T(452, 242, "Lag time", 6.8, color=RED))
    o.append(_line(350, 230, 350, 254, sw=1.0, color=RED))

    for xx, yy, lab in ((75, 266, "a  natural uranium purchase"),
                        (75, 276, "b  thorium purchase"),
                        (75, 286, "c  conversion"),
                        (75, 296, "d  enrichment"),
                        (360, 266, "e  fabrication"),
                        (360, 276, "f  commissioning date of reactor"),
                        (360, 286, "g  spent fuel storage"),
                        (360, 296, "h  spent fuel disposal")):
        o.append(T(xx, yy, lab, 6.2, color=INK, anchor="start"))

    return _mk(5, o, "Nuclear fuel cycle cost time flow",
               "Dòng thời gian chi phí chu trình nhiên liệu hạt nhân",
               "Nuclear fuel cycle cost time flow",
               "Trục thời gian với các cột chi phí tương đối cho mua urani tự nhiên, mua "
               "thori, chuyển đổi, làm giàu, chế tạo, ngày đưa lò vào hoạt động, lưu trữ "
               "và thải bỏ nhiên liệu đã dùng; mũi tên đỏ đánh dấu thời gian dẫn trước "
               "và thời gian trễ.",
               "Time axis with relative-cost bars for natural uranium purchase, thorium "
               "purchase, conversion, enrichment, fabrication, reactor commissioning, "
               "spent fuel storage and direct disposal; red arrows mark lead time and "
               "lag time.")


@_reg
def fig_f06():
    """Figure 5.6 - five compact configurations at 46 percent thorium."""
    o = []
    o.append(T(340, 14, "Five uranium/thorium configurations at 46% thorium",
               8.8, color=INK, weight="600"))

    def red_center(hd, a, b):
        return RED if hd <= 2 else BLUE

    def red_middle(hd, a, b):
        return RED if hd == 3 else BLUE

    def red_outer(hd, a, b):
        return RED if hd >= 4 else BLUE

    def red_checker(hd, a, b):
        return RED if (a + b) % 2 == 0 else BLUE

    def red_dispersed(hd, a, b):
        return RED if (2 * a + b) % 4 < 2 else BLUE

    configs = [
        (150, 86, red_center), (340, 86, red_middle), (530, 86, red_outer),
        (245, 216, red_checker), (435, 216, red_dispersed)]

    for idx, (cx, cy, rule) in enumerate(configs):
        o.append(_hexf(cx, cy, 54, "#e6e6e6", sw=1.0))
        for a in range(-5, 6):
            for b in range(-5, 6):
                hd = max(abs(a), abs(b), abs(a + b))
                if hd > 5:
                    continue
                px = cx + 9.0 * (a + 0.5 * b)
                py = cy + 9.0 * 0.866 * b
                o.append(_circle(px, py, 3.2, fill=rule(hd, a, b),
                                 sw=0.3, color="#777777"))

    for xx, yy, lab in ((150, 148, "(a) SBU 1#"), (340, 148, "(b) SBU 2#"),
                        (530, 148, "(c) SBU 3#"), (245, 278, "(d) SBU 4#"),
                        (435, 278, "(e) SBU 5#")):
        o.append(T(xx, yy, lab, 7.0, color=INK))

    o.append(_circle(180, 300, 4, fill=RED, sw=0))
    o.append(T(190, 303, "Uranium compact", 6.4, color=INK, anchor="start"))
    o.append(_circle(400, 300, 4, fill=BLUE, sw=0))
    o.append(T(410, 303, "Thorium compact", 6.4, color=INK, anchor="start"))

    return _mk(6, o, "Five uranium/thorium configurations at 46% thorium",
               "Năm cấu hình urani/thori ở 46% thori",
               "Five uranium/thorium configurations at 46% thorium",
               "Năm khối nhiên liệu lục giác với mạng viên nén: SBU 1 tập trung urani ở "
               "giữa, SBU 2 ở vòng giữa, SBU 3 ở vòng ngoài, SBU 4 và SBU 5 phân bố đều, "
               "ở hàm lượng thori 46%.",
               "Five hexagonal fuel blocks with compact lattices: SBU 1 has uranium in "
               "the centre, SBU 2 in a middle ring, SBU 3 in an outer ring, while SBU 4 "
               "and SBU 5 are dispersed, all at 46 percent thorium.")
