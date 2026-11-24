# -*- coding: utf-8 -*-
"""Vector figures for Chapter 6 "Special and Severe Service Control Valves"
of Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 150-161.

Nine simplified but faithful figures ``fig_f6_01`` ... ``fig_f6_09``.
Every function is registered with :func:`_reg` and returns the standard
5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through
:func:`_finish`.  All text is XML-escaped with :func:`T` / :func:`esc`.

Source quirk: in the text dump the caption for Figure 6.4 appears before
that of Figure 6.3 on printed p. 152.  The functions here are numbered and
placed in logical order (6.3 before 6.4); see ``source_notes`` in the prose
module.
"""
import math

from cvh6fig import (_reg, _finish, _leader, _labels, _c4_labels, esc, T,
                     _defs, _rect, _line, _circle, _ellipse, _poly, _path,
                     _arrow, _spring, _num, svg, _legend, _curve,
                     INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not in `cvh6fig` (imported there only
# for shape helpers); import them from their real home.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# small local helpers
# ---------------------------------------------------------------------------
def _chart_axes(o, x, y, W, H, xlab, ylab, xt, yt, fs=7.0):
    """Manual axes with real-value ticks ``[(value, label), ...]``."""
    def px(v):
        return x + v / 100.0 * W

    def py(v):
        return y + H - v / 100.0 * H

    o.append(_line(x, y + H, x + W, y + H, sw=1.2, color=INK))
    o.append(_line(x, y, x, y + H, sw=1.2, color=INK))
    o.append(T(x + W / 2.0, y + H + 32, xlab, 7.4, color=INK))
    o.append(T(x - 4, y - 12, ylab, 7.4, color=INK, anchor="start"))
    for v, lab in xt:
        o.append(_line(px(v), y + H, px(v), y + H + 3, sw=0.8))
        o.append(T(px(v), y + H + 13, lab, fs, color=GREY))
    for v, lab in yt:
        o.append(_line(x - 3, py(v), x, py(v), sw=0.8))
        o.append(T(x - 5, py(v) + 2.4, lab, fs, color=GREY, anchor="end"))
    return px, py


def _bolt_row(o, x0, x1, y, step=12):
    for bx in range(int(x0), int(x1), step):
        o.append(_circle(bx, y, 1.5, fill=GREY, sw=0))


# ---------------------------------------------------------------------------
# Chapter 6 figures
# ---------------------------------------------------------------------------
@_reg
def fig_f6_01():
    """Figure 6.1 (p. 151) - High-performance butterfly valve."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(250, 30, "Van bướm hiệu năng cao / High-Performance Butterfly Valve",
               9.0, weight="600"))
    o.append(_line(60, 180, 440, 180, sw=1.8, color=INK))
    o.append(_line(60, 240, 440, 240, sw=1.8, color=INK))
    o.append(_rect(60, 168, 16, 84, fill="#e9eef4", sw=1.4))
    o.append(_rect(424, 168, 16, 84, fill="#e9eef4", sw=1.4))
    _bolt_row(o, 68, 76, 186); _bolt_row(o, 432, 440, 186)
    o.append(_ellipse(250, 210, 56, 62, fill="#eef3fb", sw=1.6, color=BLUE))
    o.append(_poly([(212, 180), (288, 240), (282, 248), (206, 188)],
                   fill=GOLD, sw=1.5, close=True))
    o.append(_line(250, 210, 250, 100, sw=3.0, color=INK))
    o.append(_rect(214, 56, 72, 44, fill="#f4f7fb", sw=1.6))
    o.append(_ellipse(250, 56, 44, 11, fill="#e9eef4", sw=1.4))
    o.append(_spring(250, 60, 94, width=26))
    for cx, cy, n in [(110, 210, 1), (250, 210, 2), (250, 132, 3),
                      (250, 78, 4), (250, 276, 5), (432, 210, 6)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Thân van / Body",
        "Đĩa bướm / Butterfly disc",
        "Trục then / Splined shaft",
        "Cơ cấu chấp hành / Actuator",
        "Gioăng hỗ trợ áp suất / Pressure-assisted seal",
        "Đầu nối bích / Flanged ends",
    ], 470, 104, lh=25))
    o.append(T(250, 336,
               "Bịt kín chặt, chịu áp suất và nhiệt độ cực đoan / "
               "Tight shutoff across extreme pressure and temperature", 7.2, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.1 (p. 151) - High-performance butterfly valve",
                   "Hình 6.1 (tr. 151) · Van bướm hiệu năng cao",
                   "Hình 6.1 (tr. 151) · Sơ đồ van bướm hiệu năng cao: đĩa bướm quay trên trục then, "
                   "kết hợp với cơ cấu màng-lò xo hoặc piston khí nén và gioăng hỗ trợ áp suất để "
                   "đóng kín trong điều kiện áp suất và nhiệt độ cực đoan.",
                   "Figure 6.1 (p. 151) · Schematic of a high-performance butterfly valve: a disc "
                   "rotates on a splined shaft driven by a spring-and-diaphragm or pneumatic piston "
                   "actuator, with a pressure-assisted seal for tight shutoff at extreme pressure "
                   "and temperature.",
                   "Sơ đồ van bướm hiệu năng cao với trục then và cơ cấu chấp hành",
                   "Schematic of a high-performance butterfly valve with splined shaft and actuator")


@_reg
def fig_f6_02():
    """Figure 6.2 (p. 152) - Large-flow valve body for noise attenuation."""
    w, h = 680, 430
    o = [_defs()]
    o.append(T(250, 30, "Thân van lưu lượng lớn để giảm ồn / Large-Flow Body for Noise Attenuation",
               9.0, weight="600"))
    o.append(_line(50, 190, 120, 190, sw=1.8, color=INK))
    o.append(_line(50, 250, 120, 250, sw=1.8, color=INK))
    o.append(_rect(120, 150, 360, 140, fill="#f4f7fb", sw=1.8))
    o.append(_rect(104, 186, 16, 68, fill="#e9eef4", sw=1.4))
    o.append(_line(480, 170, 630, 170, sw=1.8, color=INK))
    o.append(_line(480, 270, 630, 270, sw=1.8, color=INK))
    o.append(_rect(480, 166, 16, 108, fill="#e9eef4", sw=1.4))
    o.append(_rect(210, 176, 170, 88, fill="#e9eef4", sw=1.4, stroke=BLUE))
    for gx in range(222, 372, 16):
        for gy in range(188, 256, 14):
            o.append(_circle(gx, gy, 2.6, fill="#ffffff", sw=0.8, color=GREY))
    o.append(_poly([(262, 182), (328, 182), (320, 214), (270, 214)],
                   fill=GOLD, sw=1.5, close=True))
    o.append(_line(295, 182, 295, 96, sw=3.0, color=INK))
    o.append(_rect(255, 52, 80, 44, fill="#f4f7fb", sw=1.6))
    o.append(_line(275, 52, 275, 30, sw=1.0, color=GREY))
    o.append(_line(315, 52, 315, 30, sw=1.0, color=GREY))
    o.append(_arrow(60, 220, 108, 220, sw=1.6, color=GREEN))
    o.append(_arrow(496, 220, 620, 220, sw=1.6, color=GREEN))
    for cx, cy, n in [(160, 160, 1), (250, 222, 2), (295, 130, 3),
                      (560, 174, 4), (295, 74, 5)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Thân đúc/chế tạo lớn / Large cast/fabricated body",
        "Cage nhiều lỗ nhỏ / Cage with many small holes",
        "Hành trình nút rất dài / Very long plug travel",
        "Đầu ra mở rộng / Expanded outlet connection",
        "Piston tác động kép / Double-acting piston",
    ], 470, 76, lh=22, size=7.0))
    o.append(T(340, 344,
               "Nhiều lỗ nhỏ, đầu ra mở rộng giảm ồn / Many small holes, expanded outlet cut noise",
               7.2, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.2 (p. 152) - Large-flow valve body for noise attenuation",
                   "Hình 6.2 (tr. 152) · Thân van lưu lượng lớn giảm ồn",
                   "Hình 6.2 (tr. 152) · Thân van đúc hoặc chế tạo lớn dạng cage, có hành trình nút "
                   "rất dài, nhiều lỗ nhỏ trên thành cage và đầu ra mở rộng nhằm giảm vận tốc "
                   "chất lỏng và mức ồn phát sinh.",
                   "Figure 6.2 (p. 152) · A large cast or fabricated cage-style body with very long "
                   "plug travel, many small holes through the cage wall and an expanded outlet "
                   "connection, all used to lower fluid velocity and noise output.",
                   "Sơ đồ thân van cage lưu lượng lớn với đầu ra mở rộng",
                   "Schematic of a large-flow cage body with an expanded outlet")


@_reg
def fig_f6_03():
    """Figure 6.3 (p. 152) - Black forged body for high capacity."""
    w, h = 660, 380
    o = [_defs()]
    o.append(T(330, 30, "Thân rèn đen cho công suất lớn / Black Forged Body for High Capacity",
               9.0, weight="600"))
    # globe-style forged block
    o.append(_rect(80, 130, 190, 110, fill="#3a4049", sw=1.8, stroke=INK))
    o.append(_rect(66, 162, 16, 46, fill="#3a4049", sw=1.4))
    o.append(_rect(268, 162, 16, 46, fill="#3a4049", sw=1.4))
    o.append(_rect(162, 130, 26, 110, fill="#ffffff", sw=1.0))
    o.append(_poly([(152, 186), (198, 186), (190, 210), (160, 210)],
                   fill=GOLD, sw=1.3, close=True))
    o.append(_line(175, 130, 175, 88, sw=2.6, color=INK))
    o.append(T(175, 274, "Kiểu cầu / Globe design", 8.0))
    # angle-style forged block
    o.append(_rect(390, 130, 120, 110, fill="#3a4049", sw=1.8, stroke=INK))
    o.append(_rect(366, 162, 26, 46, fill="#3a4049", sw=1.4))
    o.append(_rect(390, 238, 46, 18, fill="#3a4049", sw=1.4))
    o.append(_rect(430, 168, 24, 72, fill="#ffffff", sw=1.0))
    o.append(_line(430, 168, 430, 124, sw=2.6, color=INK))
    o.append(T(450, 274, "Kiểu góc / Angle design", 8.0))
    for cx, cy, n in [(98, 140, 1), (290, 140, 2), (175, 106, 3)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Thân rèn khối / Block forged body",
        "Bích tích hợp / Integral flanges",
        "Thiết kế theo ASME B16.34 / Designed to ASME B16.34",
    ], 360, 306, lh=21))
    o.append(T(60, 344,
               "Đáp ứng cấp trung gian, công suất cao / Intermediate ratings, high capacity",
               7.0, color=GREY, anchor="start"))
    return _finish(w, h, o,
                   "Figure 6.3 (p. 152) - Black forged body for high capacity",
                   "Hình 6.3 (tr. 152) · Thân rèn đen công suất lớn",
                   "Hình 6.3 (tr. 152) · Thân van rèn khối, có thể chế tạo dạng cầu hoặc dạng góc, "
                   "với bích tích hợp theo ASME B16.34 để đáp ứng các cấp áp suất trung gian và "
                   "năng lực lưu lượng lớn.",
                   "Figure 6.3 (p. 152) · A block-forged body that can be built in globe or angle "
                   "form, with integral flanges to ASME B16.34, covering intermediate ratings and "
                   "high flow capacity.",
                   "Sơ đồ thân rèn khối dạng cầu và dạng góc có bích tích hợp",
                   "Schematic of block forged bodies in globe and angle form with integral flanges")


@_reg
def fig_f6_04():
    """Figure 6.4 (p. 152) - Special control valve for very low Cv / flow."""
    w, h = 640, 380
    o = [_defs()]
    o.append(T(320, 30, "Van điều khiển đặc biệt cho lưu lượng rất nhỏ / Very-Low-Flow Valve",
               9.0, weight="600"))
    # compact valve
    o.append(_line(50, 178, 96, 178, sw=1.6, color=INK))
    o.append(_line(50, 212, 96, 212, sw=1.6, color=INK))
    o.append(_rect(96, 150, 150, 90, fill="#f4f7fb", sw=1.7))
    o.append(_line(246, 162, 320, 162, sw=1.6, color=INK))
    o.append(_line(246, 228, 320, 228, sw=1.6, color=INK))
    o.append(_rect(170, 150, 20, 90, fill="#ffffff", sw=1.0))
    o.append(_circle(180, 195, 4, fill=GOLD, sw=1.2))
    o.append(_line(180, 150, 180, 104, sw=2.4, color=INK))
    o.append(_rect(158, 76, 44, 28, fill="#e9eef4", sw=1.4))
    # magnified inset
    o.append(_circle(470, 200, 92, fill="#fbfcfd", sw=1.4, color=GREY))
    o.append(_rect(426, 150, 88, 100, fill="#eef3fb", sw=1.2))
    o.append(_rect(462, 150, 16, 100, fill="#ffffff", sw=1.0))
    o.append(_poly([(452, 168), (488, 168), (480, 196), (460, 196)],
                   fill=GOLD, sw=1.3, close=True))
    o.append(_rect(450, 202, 40, 8, fill="#dfe7ef", sw=1.2))
    o.append(_line(470, 168, 470, 118, sw=2.0, color=INK))
    o.append(_leader(512, 230, 560, 272))
    o.append(T(470, 306, "Khe hở dung sai chặt / Close-tolerance clearance",
               7.2, anchor="middle"))
    o.append(_num(120, 160, 1))
    o.append(_num(470, 128, 2))
    o.append(T(60, 300, "Cv thấp tới 0,000001 / Cv down to 0.000001",
               7.6, color=BLUE, anchor="start"))
    o.append(T(60, 324, "Thân nhỏ gọn, nhẹ / Compact, lightweight body",
               7.0, anchor="start"))
    return _finish(w, h, o,
                   "Figure 6.4 (p. 152) - Special control valve designed for very low flow rates",
                   "Hình 6.4 (tr. 152) · Van cho lưu lượng rất nhỏ",
                   "Hình 6.4 (tr. 152) · Van điều khiển đặc biệt, nhỏ gọn và nhẹ, dùng vòng đế van "
                   "và nút gia công với dung sai rất chặt để điều khiển chính xác lưu lượng chất lỏng "
                   "hoặc khí cực nhỏ, có thể tới Cv = 0,000001.",
                   "Figure 6.4 (p. 152) · A compact, lightweight special control valve using a "
                   "seat ring and plug machined to very close tolerances for accurate control of "
                   "extremely small liquid or gas flows, down to Cv = 0.000001.",
                   "Sơ đồ van điều khiển nhỏ gọn cho lưu lượng cực thấp",
                   "Schematic of a compact control valve for extremely low flow")


@_reg
def fig_f6_05():
    """Figure 6.5 (p. 154) - Typical extension bonnet."""
    w, h = 660, 420
    o = [_defs()]
    o.append(_line(60, 330, 600, 330, sw=1.8, color=INK))
    o.append(_line(60, 390, 600, 390, sw=1.8, color=INK))
    o.append(_rect(250, 320, 160, 80, fill="#f4f7fb", sw=1.8))
    o.append(_rect(234, 340, 18, 40, fill="#e9eef4", sw=1.3))
    o.append(_rect(408, 340, 18, 40, fill="#e9eef4", sw=1.3))
    o.append(_rect(226, 300, 208, 96, fill="#eaf2fb", sw=0.8, stroke=BLUE))
    o.append(_rect(288, 140, 84, 160, fill="#eef3fb", sw=1.6))
    o.append(_rect(276, 104, 108, 40, fill="#fdf3e6", sw=1.6))
    o.append(_line(330, 110, 330, 356, sw=2.6, color=INK))
    o.append(_rect(316, 68, 28, 36, fill="#e9eef4", sw=1.4))
    for fy in (336, 348, 360, 372):
        o.append(_line(322, fy, 338, fy, sw=0.9, color=BLUE))
        o.append(_line(330, fy - 6, 330, fy + 6, sw=0.9, color=BLUE))
    for cx, cy, n in [(330, 124, 1), (330, 220, 2), (330, 366, 3), (330, 86, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_leader(396, 220, 470, 200))
    o.append(T(476, 204, "Nắp kéo dài / Extension bonnet", 7.4, anchor="start"))
    o.append(_leader(384, 124, 462, 148))
    o.append(T(468, 152, "Hộp đệm làm ấm / Packing box warmed by ambient",
               7.2, anchor="start"))
    o.append(T(476, 248, "Càng lạnh, nắp càng dài", 7.4, anchor="start"))
    o.append(T(476, 268, "Colder service needs a longer bonnet", 7.4, anchor="start", color=GREY))
    o.append(T(330, 32, "Nắp kéo dài điển hình / Typical Extension Bonnet", 9.0, weight="600"))
    return _finish(w, h, o,
                   "Figure 6.5 (p. 154) - Typical extension bonnet",
                   "Hình 6.5 (tr. 154) · Nắp kéo dài điển hình",
                   "Hình 6.5 (tr. 154) · Nắp kéo dài đưa hộp đệm và thân van ra khỏi vùng đông lạnh, "
                   "được làm ấm bằng nhiệt độ môi trường để ngăn sương giá đóng trên thân và làm rách "
                   "đệm; nhiệt độ càng thấp thì nắp càng dài.",
                   "Figure 6.5 (p. 154) · An extension bonnet lifts the packing box and stem out of "
                   "the cold zone so ambient heat prevents frost from forming on the stem and "
                   "tearing the packing; colder service requires a longer bonnet.",
                   "Sơ đồ nắp kéo dài cách nhiệt hộp đệm khỏi vùng đông lạnh",
                   "Schematic of an extension bonnet keeping packing out of the cold zone")


@_reg
def fig_f6_06():
    """Figure 6.6 (p. 154) - Trim to handle cavitation."""
    w, h = 660, 400
    o = [_defs()]
    o.append(T(330, 30, "Trim chống xâm thực / Trim to Handle Cavitation", 9.0, weight="600"))
    o.append(_line(60, 180, 130, 180, sw=1.8, color=INK))
    o.append(_line(60, 260, 130, 260, sw=1.8, color=INK))
    o.append(_rect(130, 140, 400, 160, fill="#f4f7fb", sw=1.8))
    o.append(_line(530, 180, 610, 180, sw=1.8, color=INK))
    o.append(_line(530, 260, 610, 260, sw=1.8, color=INK))
    o.append(_rect(220, 156, 220, 128, fill="#eef3fb", sw=1.4, stroke=BLUE))
    for i in range(5):
        dy = 164 + i * 24
        o.append(_rect(232, dy, 196, 12, fill="#dfe7ef", sw=1.1))
        for hx in range(250, 414, 22):
            o.append(_circle(hx, dy + 6, 3.2, fill="#ffffff", sw=0.8, color=GREY))
    o.append(_line(330, 156, 330, 96, sw=2.8, color=INK))
    o.append(_rect(296, 58, 68, 38, fill="#e9eef4", sw=1.5))
    o.append(_arrow(70, 220, 124, 220, sw=1.6, color=GREEN))
    o.append(_arrow(536, 220, 600, 220, sw=1.6, color=GREEN))
    o.append(_num(330, 78, 1))
    o.append(_num(330, 300, 2))
    o.append(_leader(448, 200, 486, 294))
    o.append(T(492, 298, "Đĩa xếp chồng DST / Stacked DST disks", 7.2, anchor="start"))
    o.append(T(330, 352,
               "Chịu chênh áp trên 6000 psig, cho hạt tới 1,27 cm (1/2 in) lọt qua / "
               "Handles over 6000 psig drop while passing particulate up to 1.27 cm (1/2 in)",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.6 (p. 154) - Trim to handle cavitation",
                   "Hình 6.6 (tr. 154) · Trim xử lý xâm thực",
                   "Hình 6.6 (tr. 154) · Trim chống xâm thực nhiều tầng gồm các đĩa xếp chồng DST "
                   "có lỗ nhỏ, chia tổng chênh áp thành nhiều cấp nhưng vẫn cho chất rắn kích thước "
                   "đến 1,27 cm (1/2 in) đi qua, dùng đến trên 6000 psig.",
                   "Figure 6.6 (p. 154) · A multi-stage anti-cavitation trim of stacked DST disks "
                   "with small holes that split the total drop into steps yet pass particulate up "
                   "to 1.27 cm (1/2 in); used above 6000 psig.",
                   "Sơ đồ trim nhiều tầng chống xâm thực dạng đĩa xếp",
                   "Schematic of a multi-stage stacked-disk anti-cavitation trim")


@_reg
def fig_f6_07():
    """Figure 6.7 (p. 155) - Trim to handle particles."""
    w, h = 660, 400
    o = [_defs()]
    o.append(T(330, 30, "Trim xử lý hạt rắn / Trim to Handle Particles", 9.0, weight="600"))
    o.append(_line(60, 180, 130, 180, sw=1.8, color=INK))
    o.append(_line(60, 250, 130, 250, sw=1.8, color=INK))
    o.append(_rect(130, 150, 400, 130, fill="#f4f7fb", sw=1.8))
    o.append(_line(530, 180, 610, 180, sw=1.8, color=INK))
    o.append(_line(530, 250, 610, 250, sw=1.8, color=INK))
    o.append(_rect(116, 178, 16, 44, fill="#e9eef4", sw=1.3))
    o.append(_rect(514, 178, 16, 44, fill="#e9eef4", sw=1.3))
    o.append(_circle(330, 215, 60, fill="none", sw=1.6, color=BLUE))
    o.append(_circle(348, 215, 52, fill=GOLD, sw=1.6))
    o.append(_line(330, 215, 330, 100, sw=2.8, color=INK))
    o.append(_rect(300, 64, 60, 36, fill="#e9eef4", sw=1.4))
    o.append(_path("M 330 100 C 360 104 372 118 372 134", sw=1.0, dash="3 3", color=GREY))
    o.append(_arrow(70, 215, 124, 215, sw=1.6, color=GREEN))
    o.append(_arrow(536, 215, 600, 215, sw=1.6, color=GREEN))
    o.append(_num(330, 82, 1))
    o.append(_num(348, 215, 2))
    o.append(_num(330, 155, 3))
    o.append(_leader(348, 215, 470, 310))
    o.append(T(476, 314, "Nút lệch tâm / Eccentric plug", 7.4, anchor="start"))
    o.append(T(476, 336, "Đường dòng suôi / Streamlined passages",
               7.0, anchor="start"))
    o.append(T(330, 372,
               "Vòng đế van tự căn giữa; điều tiết hoặc đóng/mở / "
               "Self-centering seat ring; throttling or on-off operation", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.7 (p. 155) - Trim to handle particles",
                   "Hình 6.7 (tr. 155) · Trim xử lý hạt rắn",
                   "Hình 6.7 (tr. 155) · Van quay nút lệch tâm với đường dòng suôi, trim kim loại bền "
                   "và vòng đế van tự căn giữa, dùng cho chất lưu xói mòn, đóng cặn và khó xử lý, "
                   "vận hành điều tiết hoặc đóng/mở.",
                   "Figure 6.7 (p. 155) · An eccentric plug rotary valve with streamlined flow "
                   "passages, rugged metal trim and a self-centering seat ring, for erosive, coking "
                   "and other difficult fluids in throttling or on-off service.",
                   "Sơ đồ van quay nút lệch tâm cho chất lưu có hạt rắn",
                   "Schematic of an eccentric plug rotary valve for particulate service")


@_reg
def fig_f6_08():
    """Figure 6.8 (p. 156) - Inherent valve characteristic."""
    w, h = 640, 390
    o = [_defs()]
    x0, y0, W, H = 88, 56, 352, 222
    _chart_axes(o, x0, y0, W, H,
                "Hành trình định mức (%) / Rated Travel (%)",
                "Hệ số dòng định mức (%) / Rated Flow Coefficient (%)",
                [(0, "0"), (50, "50"), (100, "100")],
                [(0, "0"), (50, "50"), (100, "100")], fs=7.0)
    o.append(_curve(lambda t: t, x0, y0, W, H, sw=1.9, color=BLUE))
    o.append(_curve(lambda t: (math.exp(2.6 * t) - 1.0) / (math.exp(2.6) - 1.0),
                    x0, y0, W, H, sw=1.9, color=GREEN))
    o.append(_curve(lambda t: t ** 0.34, x0, y0, W, H, sw=1.9, color=RED))
    for yy, col, lab in [(96, BLUE, "Tuyến tính / Linear"),
                         (132, GREEN, "Phần trăm bằng / Equal-Percentage"),
                         (168, RED, "Mở nhanh / Quick-Opening")]:
        o.append(_line(462, yy, 478, yy, sw=2.2, color=col))
        o.append(T(484, yy + 3, lab, 7.0, anchor="start"))
    o.append(T(320, 356,
               "Đặc tính vốn có của van tiêu chuẩn / Inherent characteristics of standard valves",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.8 (p. 156) - Inherent valve characteristic",
                   "Hình 6.8 (tr. 156) · Đặc tính vốn có của van",
                   "Hình 6.8 (tr. 156) · Ba đường đặc tính dòng vốn có của van tiêu chuẩn — tuyến "
                   "tính, phần trăm bằng và mở nhanh — thể hiện quan hệ giữa hệ số dòng định mức và "
                   "hành trình định mức; trim đặc biệt có thể tạo đường cong riêng.",
                   "Figure 6.8 (p. 156) · Three inherent flow characteristics of standard valves - "
                   "linear, equal-percentage and quick-opening - relating rated flow coefficient to "
                   "rated travel; special trims can generate custom curves.",
                   "Biểu đồ ba đường đặc tính dòng vốn có theo hành trình",
                   "Chart of three inherent flow characteristic curves versus travel")


@_reg
def fig_f6_09():
    """Figure 6.9 (p. 157) - Pressurizer spray valve."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 30, "Van phun bình áp lực / Pressurizer Spray Valve", 9.0, weight="600"))
    # primary loop
    o.append(_line(60, 110, 620, 110, sw=2.0, color=INK))
    o.append(_line(60, 132, 360, 132, sw=2.0, color=INK))
    o.append(_circle(150, 121, 20, fill="#eef3fb", sw=1.6))
    o.append(T(150, 125, "P", 9.0, weight="600"))
    o.append(_rect(250, 104, 90, 34, fill="#f4f7fb", sw=1.6))
    o.append(T(295, 126, "Lò phản ứng / Core", 7.2))
    # spray branch and valve
    o.append(_line(400, 110, 400, 158, sw=1.8, color=INK))
    o.append(_rect(372, 158, 56, 42, fill="#f4f7fb", sw=1.7))
    o.append(_line(400, 158, 400, 120, sw=2.4, color=INK))
    o.append(_rect(388, 96, 24, 24, fill="#e9eef4", sw=1.4))
    o.append(_line(400, 200, 400, 226, sw=1.6, color=INK))
    o.append(_circle(400, 230, 5, fill=GOLD, sw=1.0))
    # pressurizer vessel
    o.append(_ellipse(520, 280, 58, 84, fill="#eef3fb", sw=1.8))
    o.append(_line(462, 280, 578, 280, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(400, 226, 462, 226, sw=1.6, color=INK))
    o.append(_arrow(404, 226, 458, 226, sw=1.4, color=GREEN))
    o.append(_num(400, 180, 1))
    o.append(_leader(428, 180, 486, 172))
    o.append(T(492, 176, "Van phun / Spray valve", 7.4, anchor="start"))
    o.append(_leader(520, 200, 520, 312))
    o.append(T(520, 330, "Bình áp lực / Pressurizer", 7.4))
    o.append(T(604, 120, "Nước làm mát sơ cấp / Primary coolant", 7.4, anchor="end"))
    o.append(T(340, 372,
               "Cấp nước làm mát vào bình áp lực để điều khiển áp suất trong lò phản ứng PWR / "
               "Feeds coolant to the pressurizer that controls reactor coolant pressure in a PWR",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 6.9 (p. 157) - Pressurizer spray valve",
                   "Hình 6.9 (tr. 157) · Van phun bình áp lực",
                   "Hình 6.9 (tr. 157) · Van phun bình áp lực trong nhà máy PWR cấp nước làm mát sơ "
                   "chính vào bình áp lực, từ đó điều khiển áp suất nước làm mát trong lò phản ứng.",
                   "Figure 6.9 (p. 157) · The pressurizer spray valve in a PWR supplies primary "
                   "coolant to the pressurizer, which in turn controls reactor coolant pressure.",
                   "Sơ đồ van phun bình áp lực trong hệ thống PWR",
                   "Schematic of a pressurizer spray valve in a PWR")
