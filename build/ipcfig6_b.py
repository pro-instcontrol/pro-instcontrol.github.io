# -*- coding: utf-8 -*-
from ipcfig6_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)
import math

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _gnd(x, y, color=INK):
    return (_line(x, y - 7, x, y, sw=1.0, color=color)
            + _line(x - 7, y, x + 7, y, sw=1.1, color=color)
            + _line(x - 4.5, y + 3, x + 4.5, y + 3, sw=0.9, color=color)
            + _line(x - 2, y + 6, x + 2, y + 6, sw=0.8, color=color))


def _hatch(x, y, color=INK):
    o = [_line(x, y - 6, x, y, sw=1.0, color=color),
         _line(x - 9, y, x + 9, y, sw=1.1, color=color)]
    for dx in (-7, -4, -1, 2, 5, 8):
        o.append(_line(x + dx, y, x + dx - 5, y + 5, sw=0.8, color=color))
    return "".join(o)


def _cap_h(x, y, color=INK):
    return (_line(x - 4, y - 7, x - 4, y + 7, sw=1.2, color=color)
            + _line(x + 4, y - 7, x + 4, y + 7, sw=1.2, color=color))


def _cap_v(x, y, color=INK):
    return (_line(x - 7, y - 4, x + 7, y - 4, sw=1.2, color=color)
            + _line(x - 7, y + 4, x + 7, y + 4, sw=1.2, color=color))


def _zig_h(x1, x2, y, n=5, amp=3.2, color=INK):
    pts = [(x1 + (x2 - x1) * i / float(2 * n),
            y + (amp if i % 2 else -amp)) for i in range(2 * n + 1)]
    return _poly(pts, sw=1.1, color=color)


def _zig_v(x, y1, y2, n=5, amp=3.2, color=INK):
    pts = [(x + (amp if i % 2 else -amp),
            y1 + (y2 - y1) * i / float(2 * n)) for i in range(2 * n + 1)]
    return _poly(pts, sw=1.1, color=color)


def _oa(x, y, w, h, label="OA"):
    o = [_poly([(x, y), (x, y + h), (x + w, y + h / 2.0)],
               fill="#ffffff", sw=1.3, close=True)]
    o.append(T(x + 9, y + 0.32 * h + 2.8, "-", 8.4, anchor="start"))
    o.append(T(x + 9, y + 0.70 * h + 2.8, "+", 8.4, anchor="start"))
    o.append(T(x + w * 0.62, y + h / 2.0 + 2.6, label, 7.0))
    return "".join(o)


def _bellows(x, y, w, h, color=INK):
    o = [_rect(x, y, w, h, fill="#ffffff", sw=1.1)]
    pts = [(x + i * w / 8.0, y + h / 2.0 + (3 if i % 2 else -3))
           for i in range(9)]
    o.append(_poly(pts, sw=1.0, color=color))
    return "".join(o)


def _darrow(x, y1, y2, color=GREY):
    return (_ar(x, y1, x, y2, color=color, sw=1.0)
            + _ar(x, y2, x, y1, color=color, sw=1.0))


def _hbar(x, y, w=12, h=8):
    """Black restriction / needle-valve symbol on a horizontal line."""
    return _rect(x, y - h / 2.0, w, h, fill=INK, sw=0)


def _vbar(x, y, w=8, h=12):
    return _rect(x - w / 2.0, y - h / 2.0, w, h, fill=INK, sw=0)


def _terminal(x, y):
    return _circle(x, y, 2.8, fill="#ffffff", sw=1.1)


def _pneumatic_head(o):
    """Air supply, restriction, nozzle and flapper, relay; returns relay base y."""
    o.append(_ar(38, 52, 58, 52, sw=1.3))
    o.append(_line(58, 52, 330, 52, sw=1.2))
    o.append(T(34, 66, "Air supply", 7.0, anchor="start"))
    o.append(T(34, 78, "1.4 kg/cm²", 7.0, anchor="start"))
    o.append(_hbar(272, 52))
    o.append(T(278, 40, "Restriction", 7.0))
    o.append(_poly([(330, 47), (330, 57), (354, 52)],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(T(342, 40, "Nozzle", 7.0))
    o.append(_circle(368, 44, 2.8, fill="#ffffff", sw=1.1))
    o.append(_line(368, 46, 368, 148, sw=1.4))
    o.append(_hatch(368, 148))
    o.append(T(378, 64, "Flapper operated by", 7.0, anchor="start"))
    o.append(T(378, 75, "process variable", 7.0, anchor="start"))
    o.append(_ar(374, 78, 370, 82, color=GREY, sw=1.0))
    o.append(_poly([(316, 57), (316, 104), (272, 104)], sw=1.2))
    o.append(_poly([(110, 52), (110, 104), (160, 104)], sw=1.2))
    o.append(_rect(160, 104, 112, 38, fill="#eef3fb", sw=1.2))
    o.append(T(216, 127, "Pneumatic relay", 7.6))
    return 142


# ---------------------------------------------------------------- 6.10
@_reg
def fig_f10():
    """Fig. 6.10 - Pneumatic integral controller with integral restriction."""
    o = [_defs()]
    _pneumatic_head(o)
    o.append(_line(216, 142, 216, 204, sw=1.2))
    o.append(_ar(216, 204, 158, 204, sw=1.3))
    o.append(T(150, 208, "Output", 7.2, anchor="end"))
    o.append(_line(250, 204, 446, 204, sw=1.2))
    o.append(_bellows(290, 166, 44, 28))
    o.append(_zig_h(344, 390, 180, n=8, amp=4))
    o.append(_hatch(367, 194))
    o.append(_bellows(396, 166, 44, 28))
    o.append(_line(290, 180, 440, 180, sw=1.1))
    o.append(T(367, 158, "Spring (Kp)", 7.0))
    o.append(T(404, 154, "Proportional bellows", 7.0, anchor="start"))
    o.append(_ar(400, 148, 418, 164, color=GREY, sw=1.0))
    o.append(_poly([(440, 194), (440, 220), (252, 220), (252, 204)], sw=1.1))
    o.append(_hbar(280, 220))
    o.append(T(272, 234, "Integral restriction", 7.0, anchor="start"))
    o.append(_ar(286, 228, 280, 222, color=GREY, sw=1.0))
    return _mk(10, o, "Pneumatic integral controller",
               "Sơ đồ khí nén có tiết lưu tích phân và ống nhồi bổ sung",
               "Pneumatic controller with an integral restriction and extra bellows",
               "Sơ đồ khí nén: áp suất cấp qua tiết lưu tới vòi phun và cánh chắn, áp suất ngược điều khiển rơ le; đầu ra tác động qua tiết lưu tích phân tới ống nhồi tích phân cân bằng với ống nhồi tỷ lệ và lò xo, nhờ đó triệt tiêu sai lệch tĩnh.",
               "Pneumatic circuit: supply air passes a restriction to the nozzle and process-driven flapper, and back pressure drives the relay. The output reaches an integral bellows through an integral restriction and balances a proportional bellows and spring, eliminating proportional offset.")


# ---------------------------------------------------------------- 6.11
@_reg
def fig_f11():
    """Fig. 6.11 - Response of derivative control action."""
    o = [_defs()]
    o.append(_ar(100, 196, 100, 38, sw=1.2))
    o.append(_ar(100, 196, 628, 196, sw=1.2))
    o.append(T(638, 200, "Time", 7.4, anchor="start"))
    o.append(_line(100, 104, 570, 104, sw=1.0, dash="7 4"))
    o.append(T(578, 100, "Set value", 7.0, anchor="start"))
    o.append(_line(250, 58, 250, 176, sw=0.9, dash="4 4", color=GREY))
    meas = [(100, 104), (250, 104), (250, 60), (530, 60)]
    o.append(_poly(meas, sw=1.8, color=BLUE))
    o.append(T(540, 54, "Measurement input change", 7.0, anchor="start"))
    o.append(_ar(536, 58, 512, 58, color=GREY, sw=1.0))
    out = [(100, 142), (250, 142), (250, 174), (270, 174),
           (270, 130), (520, 130)]
    o.append(_poly(out, sw=1.9, color=RED))
    o.append(T(532, 134, "Output", 7.2, anchor="start"))
    o.append(_ar(528, 134, 510, 134, color=GREY, sw=1.0))
    o.append(T(262, 186, "Derivative kick", 6.8, anchor="start", color=GREY))
    return _mk(11, o, "Derivative control response",
               "Đáp ứng đạo hàm với xung đầu vào và đầu ra nhảy tức thời",
               "Derivative response to a step measurement input",
               "Đồ thị đường giá trị cài đặt đứt nét, đầu vào đo lường nhảy lên và đầu ra có một xung đẩy xuống ngắn trước khi nhảy lên mức mới; điều này thể hiện tác dụng dự báo của vi phân.",
               "Graph with a dashed set value, a step increase in the measurement input, and an output that makes a brief downward kick before stepping to a new level, illustrating anticipatory derivative action.")


# ---------------------------------------------------------------- 6.12
@_reg
def fig_f12():
    """Fig. 6.12 - Electronic differentiator (derivative plus proportional)."""
    o = [_defs()]
    o.append(_terminal(62, 84))
    o.append(_terminal(62, 190))
    o.append(_darrow(44, 90, 184))
    o.append(T(32, 140, "Ein", 7.4))
    o.append(_line(64, 84, 210, 84, sw=1.2))
    o.append(_cap_h(112, 84))
    o.append(T(112, 72, "Cin", 7.2))
    o.append(_poly([(150, 84), (150, 38), (330, 38), (330, 84)], sw=1.2))
    o.append(_cap_h(244, 38))
    o.append(T(244, 26, "Cfd", 7.2))
    o.append(_oa(210, 56, 70, 60, "OA"))
    o.append(_line(210, 98, 210, 190, sw=1.1))
    o.append(_gnd(210, 190))
    o.append(_line(280, 86, 470, 86, sw=1.2))
    o.append(_terminal(470, 86))
    o.append(_terminal(470, 190))
    o.append(_line(64, 190, 470, 190, sw=1.2))
    o.append(_darrow(486, 90, 186))
    o.append(T(498, 140, "E0", 7.4, anchor="start"))
    o.append(_zig_v(330, 94, 120, n=4, amp=3.0))
    o.append(T(314, 108, "R", 7.0, anchor="end"))
    o.append(_ar(352, 112, 334, 108, color=GREY, sw=1.0))
    o.append(T(360, 106, "Derivative adjustment", 7.0, anchor="start"))
    o.append(_line(330, 124, 330, 130, sw=1.1))
    o.append(_cap_v(330, 134))
    o.append(T(314, 138, "Cd", 7.0, anchor="end"))
    o.append(_line(330, 142, 330, 150, sw=1.1))
    o.append(_line(330, 150, 380, 150, sw=1.1))
    o.append(_zig_v(380, 150, 170, n=3, amp=3.0))
    o.append(T(366, 162, "R3", 7.0, anchor="end"))
    o.append(_line(380, 170, 380, 190, sw=1.1))
    o.append(_zig_v(424, 150, 170, n=3, amp=3.0))
    o.append(T(434, 162, "R4", 7.0, anchor="start"))
    o.append(_line(424, 170, 424, 190, sw=1.1))
    o.append(_line(424, 150, 470, 150, sw=1.1))
    o.append(_ar(400, 158, 380, 158, color=GREY, sw=1.0))
    o.append(_zig_v(444, 96, 190, n=6, amp=3.0))
    o.append(T(444, 88, "Rp", 7.0))
    o.append(_ar(414, 124, 442, 124, color=GREY, sw=1.0))
    o.append(T(360, 210, "Proportional band adjustment", 7.0, anchor="start"))
    return _mk(12, o, "Electronic differentiator circuit",
               "Mạch vi phân điện tử với tụ sai số và chiết áp chỉnh thời gian",
               "Electronic derivative circuit with adjustable derivative time",
               "Sơ đồ mạch: tín hiệu sai số qua tụ Cin tới bộ khuếch đại, tụ Cfd phản hồi; mạng đầu ra gồm biến trở chỉnh vi phân, tụ Cd và chiết áp Rp chỉnh dải tỷ lệ, tạo đầu ra E0 có thành phần vi phân tạm thời.",
               "Circuit in which the error signal passes through capacitor Cin to the amplifier with capacitor Cfd feedback; an adjustable resistor, capacitor Cd and potentiometer Rp set derivative time and proportional band, producing the temporary derivative contribution in E0.")


# ---------------------------------------------------------------- 6.13
@_reg
def fig_f13():
    """Fig. 6.13 - Pneumatic derivative controller."""
    o = [_defs()]
    _pneumatic_head(o)
    o.append(_line(216, 142, 216, 204, sw=1.2))
    o.append(_ar(216, 204, 158, 204, sw=1.3))
    o.append(T(150, 208, "Output", 7.2, anchor="end"))
    o.append(_zig_h(330, 374, 180, n=8, amp=4))
    o.append(_hatch(352, 194))
    o.append(_bellows(388, 166, 44, 28))
    o.append(_line(330, 180, 432, 180, sw=1.1))
    o.append(_poly([(326, 180), (326, 204), (216, 204)], sw=1.1))
    o.append(T(352, 158, "Spring (Kp)", 7.0))
    o.append(T(396, 154, "Proportional bellows", 7.0, anchor="start"))
    o.append(_ar(392, 148, 410, 164, color=GREY, sw=1.0))
    o.append(_poly([(432, 194), (432, 220), (250, 220), (250, 204)], sw=1.1))
    o.append(_vbar(462, 206))
    o.append(_line(432, 194, 462, 194, sw=1.1))
    o.append(_line(462, 194, 462, 220, sw=1.1))
    o.append(T(470, 202, "Derivative", 7.0, anchor="start"))
    o.append(T(470, 212, "restriction", 7.0, anchor="start"))
    o.append(_ar(468, 208, 464, 206, color=GREY, sw=1.0))
    return _mk(13, o, "Pneumatic derivative controller",
               "Sơ đồ khí nén có tiết lưu đạo hàm trước ống nhồi tỷ lệ",
               "Pneumatic controller with a derivative restriction",
               "Sơ đồ khí nén: vòi phun và cánh chắn tạo áp suất ngược điều khiển rơ le; tiết lưu đạo hàm đặt trên đường dẫn tới ống nhồi tỷ lệ, tạo hiệu ứng khuếch đại tạm thời khi tải thay đổi.",
               "Pneumatic circuit with nozzle, flapper and relay; a derivative restriction in the line to the proportional bellows produces a temporary gain boost whenever the load changes, improving stability.")


# ---------------------------------------------------------------- 6.14
@_reg
def fig_f14():
    """Fig. 6.14 - Proportional plus integral response diagram."""
    o = [_defs()]
    o.append(_ar(88, 68, 88, 16, sw=1.1))
    o.append(_ar(88, 68, 632, 68, sw=1.1))
    o.append(T(82, 16, "Process variable", 7.0, anchor="end"))
    o.append(T(642, 72, "Time", 7.0, anchor="start"))
    o.append(_poly([(88, 56), (170, 56), (170, 26), (430, 26)], sw=1.5))
    o.append(T(440, 30, "Set value", 7.0, anchor="start"))
    o.append(_ar(88, 108, 88, 80, sw=1.1))
    o.append(T(82, 100, "Output", 7.0, anchor="end"))
    o.append(_poly([(88, 140), (200, 140), (200, 92), (470, 92)], sw=1.6))
    o.append(T(400, 86, "Proportional action", 7.0))
    o.append(_poly([(200, 140), (510, 106)], sw=1.7, color=BLUE))
    o.append(T(520, 110, "PI action", 7.0, anchor="start", color=BLUE))
    o.append(_line(200, 126, 560, 126, sw=1.0, dash="7 4"))
    o.append(T(566, 130, "Proportional action", 7.0, anchor="start"))
    o.append(_line(200, 88, 200, 148, sw=0.9, dash="4 4", color=GREY))
    o.append(_line(430, 106, 430, 148, sw=0.9, dash="4 4", color=GREY))
    o.append(_darrow(174, 140, 126))
    o.append(T(166, 138, "Es", 7.0, anchor="end"))
    o.append(_darrow(446, 126, 106))
    o.append(T(452, 118, "Es", 7.0, anchor="start"))
    o.append(_ar(200, 152, 430, 152, color=GREY, sw=1.0))
    o.append(_ar(430, 152, 200, 152, color=GREY, sw=1.0))
    o.append(T(315, 168, "Time for one repeat", 7.0))
    o.append(_line(88, 178, 632, 178, sw=1.0))
    o.append(_line(88, 224, 632, 224, sw=1.1))
    o.append(_ar(632, 224, 620, 224, sw=1.1))
    o.append(T(642, 228, "Time", 7.0, anchor="start"))
    o.append(_ar(88, 186, 88, 178, sw=1.1))
    o.append(T(82, 196, "Output", 7.0, anchor="end"))
    decay = [(200 + i * 12, 188 + 26 * (1 - math.exp(-i / 7.0)))
             for i in range(27)]
    o.append(_poly(decay, sw=1.7, color=BLUE))
    o.append(_line(88, 214, 520, 214, sw=1.1))
    o.append(T(528, 218, "Proportional action", 7.0, anchor="start"))
    o.append(_line(88, 198, 284, 198, sw=1.0, dash="6 4"))
    o.append(T(96, 194, "63.2% of drop", 7.0, anchor="start"))
    o.append(_line(284, 198, 284, 220, sw=0.9, dash="4 4", color=GREY))
    o.append(_ar(200, 220, 284, 220, color=GREY, sw=1.0))
    o.append(_ar(284, 220, 200, 220, color=GREY, sw=1.0))
    o.append(T(300, 220, "Rate time", 7.0, anchor="start"))
    return _mk(14, o, "PI control response chart",
               "Đồ thị đáp ứng tỷ lệ cộng tích phân với thời gian lặp và thời gian tốc độ",
               "PI response with proportional step, integral ramp and reset time",
               "Đồ thị ba phần: đầu vào giá trị cài đặt dạng bước, đầu ra gồm bước tỷ lệ cộng đường tăng tuyến tính của tích phân trong thời gian lặp, và đường suy giảm 63,2% dùng để xác định thời gian tốc độ.",
               "Three-panel chart: a set-value step, an output made of a proportional step plus a linear integral ramp repeated each reset time, and a decaying curve whose 63.2% point defines the rate time.")


# ---------------------------------------------------------------- 6.15
@_reg
def fig_f15():
    """Fig. 6.15 - Electronic PI controller circuit."""
    o = [_defs()]
    o.append(_terminal(62, 76))
    o.append(_terminal(62, 190))
    o.append(_darrow(44, 82, 184))
    o.append(T(32, 136, "Ein", 7.4))
    o.append(_zig_v(118, 80, 116, n=4, amp=3.0))
    o.append(_zig_v(118, 120, 154, n=4, amp=3.0))
    o.append(T(104, 100, "R1", 7.0, anchor="end"))
    o.append(T(104, 140, "R2", 7.0, anchor="end"))
    o.append(_zig_v(118, 158, 186, n=4, amp=3.0))
    o.append(_line(118, 116, 168, 116, sw=1.1))
    o.append(_zig_h(122, 162, 116, n=4, amp=3.0))
    o.append(T(142, 106, "Ri", 7.0))
    o.append(_ar(142, 138, 142, 122, color=GREY, sw=1.0))
    o.append(T(96, 210, "Integral adjustment", 7.0, anchor="start"))
    o.append(_line(62, 76, 210, 76, sw=1.2))
    o.append(_cap_h(182, 76))
    o.append(T(182, 64, "Cin", 7.2))
    o.append(_poly([(168, 76), (168, 32), (340, 32), (340, 76)], sw=1.2))
    o.append(_cap_h(246, 32))
    o.append(T(246, 20, "Cfb", 7.2))
    o.append(_oa(210, 54, 70, 60, "OA"))
    o.append(_line(210, 96, 210, 190, sw=1.1))
    o.append(_gnd(210, 190))
    o.append(_line(280, 84, 470, 84, sw=1.2))
    o.append(_terminal(470, 84))
    o.append(_terminal(470, 190))
    o.append(_line(62, 190, 470, 190, sw=1.2))
    o.append(_darrow(486, 88, 186))
    o.append(T(498, 140, "E0", 7.4, anchor="start"))
    o.append(_line(340, 84, 340, 122, sw=1.1))
    o.append(_ar(366, 122, 344, 122, color=GREY, sw=1.0))
    o.append(_zig_v(402, 100, 190, n=6, amp=3.0))
    o.append(T(402, 92, "Rp", 7.0))
    o.append(T(340, 210, "Proportional band adjustment", 7.0, anchor="start"))
    return _mk(15, o, "Electronic PI controller",
               "Mạch điều khiển tỷ lệ cộng tích phân với chiết áp Ri và Rp",
               "Electronic PI circuit with integral and proportional-band controls",
               "Sơ đồ mạch PI: tín hiệu sai số qua mạng R1, Ri, R2 và tụ Cin tới bộ khuếch đại có phản hồi Cfb; chiết áp Ri chỉnh tốc độ tích phân, còn Rp chỉnh dải tỷ lệ để đầu ra E0 triệt tiêu sai lệch tĩnh.",
               "PI circuit: the error signal passes the R1-Ri-R2 network and capacitor Cin to an amplifier with Cfb feedback; Ri sets integral rate and Rp sets proportional band so that output E0 removes steady-state offset.")


# ---------------------------------------------------------------- 6.16
@_reg
def fig_f16():
    """Fig. 6.16 - Electronic PID controller circuit."""
    o = [_defs()]
    o.append(_terminal(62, 76))
    o.append(_terminal(62, 190))
    o.append(_darrow(44, 82, 184))
    o.append(T(32, 136, "Ein", 7.4))
    o.append(_zig_v(118, 80, 116, n=4, amp=3.0))
    o.append(_zig_v(118, 120, 154, n=4, amp=3.0))
    o.append(T(104, 100, "R1", 7.0, anchor="end"))
    o.append(T(104, 140, "R2", 7.0, anchor="end"))
    o.append(_zig_v(118, 158, 186, n=4, amp=3.0))
    o.append(_line(118, 116, 168, 116, sw=1.1))
    o.append(_zig_h(122, 162, 116, n=4, amp=3.0))
    o.append(T(142, 106, "Ri", 7.0))
    o.append(_ar(142, 138, 142, 122, color=GREY, sw=1.0))
    o.append(T(96, 210, "Integral adjustment", 7.0, anchor="start"))
    o.append(_line(62, 76, 210, 76, sw=1.2))
    o.append(_cap_h(182, 76))
    o.append(T(182, 64, "Cin", 7.2))
    o.append(_poly([(168, 76), (168, 32), (352, 32), (352, 76)], sw=1.2))
    o.append(_cap_h(248, 32))
    o.append(T(248, 20, "Cfb", 7.2))
    o.append(_oa(210, 54, 70, 60, "OA"))
    o.append(_line(210, 96, 210, 190, sw=1.1))
    o.append(_gnd(210, 190))
    o.append(_line(280, 86, 570, 86, sw=1.2))
    o.append(_terminal(570, 86))
    o.append(_terminal(570, 190))
    o.append(_line(62, 190, 570, 190, sw=1.2))
    o.append(_darrow(586, 90, 186))
    o.append(T(598, 140, "E0", 7.4, anchor="start"))
    o.append(_line(316, 116, 372, 116, sw=1.1))
    o.append(_zig_h(320, 368, 116, n=5, amp=3.0))
    o.append(T(344, 106, "Rd", 7.0))
    o.append(_ar(344, 134, 344, 122, color=GREY, sw=1.0))
    o.append(T(316, 142, "Derivative adjustment", 7.0, anchor="start"))
    o.append(_line(316, 116, 330, 116, sw=1.1))
    o.append(_line(330, 122, 330, 130, sw=1.1))
    o.append(_cap_v(330, 134))
    o.append(T(314, 138, "Cd", 7.0, anchor="end"))
    o.append(_line(330, 142, 330, 150, sw=1.1))
    o.append(_line(330, 150, 420, 150, sw=1.1))
    o.append(_zig_v(420, 150, 170, n=3, amp=3.0))
    o.append(T(430, 162, "R3", 7.0, anchor="start"))
    o.append(_line(420, 170, 420, 190, sw=1.1))
    o.append(_zig_v(470, 150, 170, n=3, amp=3.0))
    o.append(T(480, 162, "R4", 7.0, anchor="start"))
    o.append(_line(470, 170, 470, 190, sw=1.1))
    o.append(_ar(396, 158, 418, 158, color=GREY, sw=1.0))
    o.append(_zig_v(526, 100, 190, n=6, amp=3.0))
    o.append(T(526, 92, "Rp", 7.0))
    o.append(_ar(496, 122, 524, 122, color=GREY, sw=1.0))
    o.append(T(404, 210, "Proportional band adjustment", 7.0, anchor="start"))
    return _mk(16, o, "Electronic PID controller",
               "Mạch điều khiển PID điện tử gồm chỉnh tích phân, vi phân và dải tỷ lệ",
               "Electronic PID circuit with integral, derivative and band controls",
               "Sơ đồ mạch PID: mạng đầu vào R1, Ri, R2 và tụ Cin tới bộ khuếch đại phản hồi Cfb; Rd với tụ Cd tạo vi phân, Ri tạo tích phân và Rp chỉnh dải tỷ lệ cho tín hiệu đầu ra E0.",
               "PID circuit: the input network R1-Ri-R2 and capacitor Cin feed an amplifier with Cfb feedback; Rd with capacitor Cd supplies derivative action, Ri supplies integral action and Rp sets the proportional band of output E0.")


# ---------------------------------------------------------------- 6.17
@_reg
def fig_f17():
    """Fig. 6.17 - Pneumatic PID controller with two restrictors."""
    o = [_defs()]
    _pneumatic_head(o)
    o.append(_line(216, 142, 216, 204, sw=1.2))
    o.append(_ar(216, 204, 158, 204, sw=1.3))
    o.append(T(150, 208, "Output", 7.2, anchor="end"))
    o.append(_vbar(286, 192))
    o.append(_line(216, 204, 286, 204, sw=1.1))
    o.append(_line(286, 204, 286, 180, sw=1.1))
    o.append(_bellows(300, 166, 44, 28))
    o.append(_zig_h(354, 398, 180, n=8, amp=4))
    o.append(_hatch(376, 194))
    o.append(_bellows(404, 166, 44, 28))
    o.append(_line(300, 180, 448, 180, sw=1.1))
    o.append(T(376, 158, "Spring (Kp)", 7.0))
    o.append(T(412, 154, "Proportional bellows", 7.0, anchor="start"))
    o.append(_ar(408, 148, 426, 164, color=GREY, sw=1.0))
    o.append(T(196, 194, "Derivative restrictor", 7.0, anchor="start"))
    o.append(_ar(280, 200, 286, 196, color=GREY, sw=1.0))
    o.append(_poly([(448, 194), (448, 224), (256, 224), (256, 204)], sw=1.1))
    o.append(_hbar(292, 224))
    o.append(T(284, 236, "Integral restrictor", 7.0, anchor="start"))
    o.append(_ar(298, 230, 292, 226, color=GREY, sw=1.0))
    return _mk(17, o, "Pneumatic PID controller",
               "Sơ đồ khí nén PID với tiết lưu vi phân và tiết lưu tích phân",
               "Pneumatic PID circuit with derivative and integral restrictors",
               "Sơ đồ khí nén: rơ le nhận áp suất ngược từ vòi phun và cánh chắn; tiết lưu vi phân nằm trên đường tới ống nhồi, tiết lưu tích phân nằm trên đường phản hồi, tạo đồng thời ba tác vụ PID.",
               "Pneumatic PID circuit: the relay responds to nozzle back pressure; a derivative restrictor sits in the line to the bellows and an integral restrictor in the feedback line, producing proportional, integral and derivative action together.")


# ---------------------------------------------------------------- 6.18
@_reg
def fig_f18():
    """Fig. 6.18 - Integral-windup limiter circuit."""
    o = [_defs()]
    o.append(_circle(210, 50, 11, fill="#ffffff", sw=1.2))
    o.append(_ar(72, 50, 199, 50, sw=1.3))
    o.append(T(72, 70, "Proportional action", 7.0, anchor="start"))
    o.append(T(196, 38, "+", 8.4, anchor="start"))
    o.append(_rect(90, 150, 100, 36, fill="#eef3fb", sw=1.2))
    o.append(T(140, 172, "Integral unit", 7.8))
    o.append(_ar(170, 150, 170, 61, sw=1.3))
    o.append(T(180, 122, "Integral action", 7.0, anchor="start"))
    o.append(T(176, 66, "+", 8.4, anchor="start"))
    o.append(_ar(221, 50, 620, 50, sw=1.3))
    o.append(T(628, 54, "Output", 7.2, anchor="start"))
    o.append(_poly([(400, 50), (400, 112), (240, 112), (240, 154)], sw=1.1))
    o.append(_ar(240, 132, 240, 152, sw=1.2))
    o.append(_poly([(400, 112), (520, 112), (520, 156)], sw=1.1))
    o.append(_ar(520, 134, 520, 156, sw=1.2))
    o.append(_rect(220, 154, 40, 28, fill="#ffffff", sw=1.2))
    o.append(T(240, 173, "<", 10.0))
    o.append(_ar(220, 168, 190, 168, sw=1.2))
    o.append(_rect(300, 154, 40, 28, fill="#ffffff", sw=1.2))
    o.append(T(320, 173, ">", 10.0))
    o.append(_ar(300, 168, 260, 168, sw=1.2))
    o.append(_poly([(496, 154), (496, 182), (456, 168)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_ar(456, 168, 340, 168, sw=1.2))
    o.append(_circle(520, 168, 11, fill="#ffffff", sw=1.2))
    o.append(_ar(509, 168, 498, 168, sw=1.2))
    o.append(T(506, 158, "-", 8.4, anchor="end"))
    o.append(T(508, 186, "+", 8.4, anchor="start"))
    o.append(_ar(520, 202, 520, 179, sw=1.2))
    o.append(T(534, 202, "Bias", 7.0, anchor="start"))
    o.append(_ar(320, 200, 320, 182, sw=1.2))
    o.append(T(324, 200, "Preload", 7.0, anchor="start"))
    o.append(T(462, 200, "Amplifier", 7.0, anchor="start"))
    o.append(T(200, 194, "(Preferential)", 6.4, anchor="start", color=GREY))
    o.append(T(200, 204, "Low limit switch", 7.0, anchor="start"))
    o.append(T(300, 214, "(Preferential)", 6.4, anchor="start", color=GREY))
    o.append(T(300, 224, "High limit switch", 7.0, anchor="start"))
    return _mk(18, o, "Integral-windup limiter circuit",
               "Sơ đồ hạn chế tích phân bão hòa với công tắc giới hạn và bộ khuếch đại",
               "Limiter circuit that prevents integral windup",
               "Sơ đồ khối: tác vụ tỷ lệ và tích phân cộng tại đầu ra; đầu ra được đưa qua công tắc giới hạn thấp và cao cùng bộ khuếch đại và tín hiệu lệch, để khóa vòng tích phân khi đầu ra tiến tới bão hòa và giữ preload tránh bão hòa dưới.",
               "Block diagram: proportional and integral actions are summed at the output; the output passes low and high limit switches with an amplifier and bias signal, disabling the integral path near saturation while a preload avoids lower-limit saturation.")
