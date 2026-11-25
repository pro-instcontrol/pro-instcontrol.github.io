# -*- coding: utf-8 -*-
from ipcfig6_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)
import math

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _gnd(x, y, color=INK):
    """Standard ground symbol with its connection point at (x, y)."""
    return (_line(x, y - 7, x, y, sw=1.0, color=color)
            + _line(x - 7, y, x + 7, y, sw=1.1, color=color)
            + _line(x - 4.5, y + 3, x + 4.5, y + 3, sw=0.9, color=color)
            + _line(x - 2, y + 6, x + 2, y + 6, sw=0.8, color=color))


def _hatch(x, y, color=INK):
    """Grounded mechanical support for a pneumatic flapper."""
    o = [_line(x, y - 6, x, y, sw=1.0, color=color),
         _line(x - 9, y, x + 9, y, sw=1.1, color=color)]
    for dx in (-7, -4, -1, 2, 5, 8):
        o.append(_line(x + dx, y, x + dx - 5, y + 5, sw=0.8, color=color))
    return "".join(o)


def _cap_h(x, y, color=INK):
    return (_line(x - 4, y - 7, x - 4, y + 7, sw=1.2, color=color)
            + _line(x + 4, y - 7, x + 4, y + 7, sw=1.2, color=color))


def _zig_h(x1, x2, y, n=5, amp=3.2, color=INK):
    pts = [(x1 + (x2 - x1) * i / float(2 * n),
            y + (amp if i % 2 else -amp)) for i in range(2 * n + 1)]
    return _poly(pts, sw=1.1, color=color)


def _zig_v(x, y1, y2, n=5, amp=3.2, color=INK):
    pts = [(x + (amp if i % 2 else -amp),
            y1 + (y2 - y1) * i / float(2 * n)) for i in range(2 * n + 1)]
    return _poly(pts, sw=1.1, color=color)


def _oa(x, y, w, h, label="OA"):
    """Op-amp triangle; inverting terminal near y+0.32h, non-inverting near y+0.70h."""
    o = [_poly([(x, y), (x, y + h), (x + w, y + h / 2.0)],
               fill="#ffffff", sw=1.3, close=True)]
    o.append(T(x + 9, y + 0.32 * h + 2.8, "-", 8.4, anchor="start"))
    o.append(T(x + 9, y + 0.70 * h + 2.8, "+", 8.4, anchor="start"))
    o.append(T(x + w * 0.6, y + h / 2.0 + 2.6, label, 7.0))
    return "".join(o)


def _contact(x, y, color=INK):
    """Normally open relay contact: two terminals 26 px apart with an open blade."""
    return (_circle(x, y, 2.4, fill="#ffffff", sw=1.1, color=color)
            + _circle(x, y + 26, 2.4, fill="#ffffff", sw=1.1, color=color)
            + _line(x, y, x + 11, y + 24, sw=1.2, color=color))


def _vtxt(x, y, s, size=7.4, color=INK):
    """Vertical (rotated -90) axis title."""
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, x, y, size, color, s))


def _darrow(x, y1, y2, color=GREY):
    return (_ar(x, y1, x, y2, color=color, sw=1.0)
            + _ar(x, y2, x, y1, color=color, sw=1.0))


def _bellows(x, y, w, h, color=INK):
    o = [_rect(x, y, w, h, fill="#ffffff", sw=1.1)]
    pts = [(x + i * w / 8.0, y + h / 2.0 + (3 if i % 2 else -3))
           for i in range(9)]
    o.append(_poly(pts, sw=1.0, color=color))
    return "".join(o)


# ---------------------------------------------------------------- 6.1
@_reg
def fig_f01():
    """Fig. 6.1 - ON-OFF control: measurement and valve output waveforms."""
    o = [_defs()]
    o.append(_ar(110, 196, 110, 48, sw=1.1))
    o.append(_ar(110, 196, 644, 196, sw=1.1))
    o.append(T(652, 200, "Time", 7.4, anchor="start"))
    o.append(_line(110, 88, 620, 88, sw=1.1, dash="6 4"))
    o.append(T(62, 92, "Set value", 7.2, anchor="end"))
    meas = [(112, 88), (137, 102), (162, 108), (187, 102), (212, 88),
            (237, 74), (262, 68), (287, 74), (312, 88), (337, 102),
            (362, 108), (387, 102), (412, 88), (437, 74), (462, 68),
            (487, 74), (512, 88), (537, 102), (562, 108), (587, 102),
            (612, 88)]
    o.append(_poly(meas, sw=1.8, color=BLUE))
    o.append(T(566, 62, "Measurement", 7.2, anchor="start"))
    o.append(_ar(562, 66, 528, 82, color=GREY, sw=1.0))
    for xx in (212, 312, 412, 512):
        o.append(_line(xx, 90, xx, 148, sw=0.9, dash="4 3", color=GREY))
    steps = [(112, 150), (212, 150), (212, 190), (312, 190), (312, 150),
             (412, 150), (412, 190), (512, 190), (512, 150), (612, 150)]
    o.append(_poly(steps, sw=1.9, color=RED))
    o.append(_line(62, 150, 110, 150, sw=1.0, dash="4 3", color=GREY))
    o.append(_line(62, 190, 110, 190, sw=1.0, dash="4 3", color=GREY))
    o.append(T(58, 154, "100%", 7.2, anchor="end"))
    o.append(T(58, 194, "0%", 7.2, anchor="end"))
    o.append(T(20, 222, "Output signal to control valve", 7.0, anchor="start"))
    o.append(_ar(152, 218, 116, 192, color=GREY, sw=1.0))
    return _mk(1, o, "ON-OFF control action",
               "Dao động đo lường và tín hiệu đầu ra đóng cắt theo giá trị cài đặt",
               "Measurement oscillation and ON-OFF valve output around the set value",
               "Đồ thị gồm đường đo lường dao động quanh giá trị cài đặt và tín hiệu đầu ra đóng cắt ở mức 100% hoặc 0%; các đường đứt nét đánh dấu thời điểm đo lường vượt qua giá trị cài đặt.",
               "Graph of a measurement oscillating around the set value with a valve output switching between 100% and 0%; dashed lines mark the instants when the measurement crosses the set value.")


# ---------------------------------------------------------------- 6.2
@_reg
def fig_f02():
    """Fig. 6.2 - Electrical ON-OFF implementation with a thermostatic relay."""
    o = [_defs()]
    o.append(_line(60, 55, 520, 55, sw=1.2))
    o.append(_line(60, 180, 520, 180, sw=1.2))
    o.append(_ar(45, 178, 45, 57, sw=1.2))
    o.append(_ar(45, 57, 45, 178, sw=1.2))
    o.append(T(34, 112, "Control", 7.0, anchor="end"))
    o.append(T(34, 122, "supply", 7.0, anchor="end"))
    o.append(_rect(100, 70, 60, 52, fill="#fbfaf7", sw=0.9, dash="4 3"))
    o.append(_line(130, 55, 130, 85, sw=1.1))
    o.append(_contact(130, 85))
    o.append(_line(130, 111, 130, 140, sw=1.1))
    o.append(T(150, 98, "TS", 7.4, anchor="start"))
    o.append(T(28, 158, "Thermostat", 7.0, anchor="start"))
    o.append(_ar(82, 154, 112, 108, color=GREY, sw=1.0))
    o.append(_rect(108, 140, 44, 26, fill="#eef3fb", sw=1.2))
    o.append(T(130, 157, "R1", 7.8))
    o.append(_line(130, 166, 130, 180, sw=1.1))
    o.append(_line(300, 55, 300, 85, sw=1.1))
    o.append(_contact(300, 85))
    o.append(_line(300, 111, 300, 140, sw=1.1))
    o.append(T(320, 98, "1R1", 7.4, anchor="start"))
    o.append(_rect(278, 140, 44, 26, fill="#eef3fb", sw=1.2))
    o.append(T(300, 157, "R2", 7.8))
    o.append(_line(300, 166, 300, 180, sw=1.1))
    o.append(_line(470, 55, 470, 85, sw=1.1))
    o.append(_contact(470, 85))
    o.append(_line(470, 111, 470, 140, sw=1.1))
    o.append(T(490, 98, "1R2", 7.4, anchor="start"))
    o.append(_rect(430, 140, 80, 28, fill="#eef3fb", sw=1.2))
    o.append(_ar(528, 156, 512, 156, color=GREY, sw=1.0))
    o.append(T(534, 152, "Supply to", 7.0, anchor="start"))
    o.append(T(534, 162, "ON-OFF action.", 7.0, anchor="start"))
    return _mk(2, o, "Electrical ON-OFF control circuit",
               "Mạch điều khiển đóng cắt dùng công tắc nhiệt và hai rơ le",
               "Electrical ON-OFF control circuit with a thermostatic switch and two relays",
               "Sơ đồ mạch điện: công tắc nhiệt TS đóng sẽ cấp điện cho rơ le R1; tiếp điểm thường mở 1R1 đóng cấp điện cho rơ le R2; tiếp điểm 1R2 đóng cấp nguồn cho cơ cấu đóng cắt.",
               "Circuit diagram: closing the thermostatic switch TS energises relay R1; its normally open contact 1R1 closes and energises relay R2; contact 1R2 then supplies the ON-OFF actuator.")


# ---------------------------------------------------------------- 6.3
@_reg
def fig_f03():
    """Fig. 6.3 - Pneumatic ON-OFF nozzle and flapper circuit."""
    o = [_defs()]
    o.append(_ar(55, 90, 72, 90, sw=1.3))
    o.append(_line(72, 90, 300, 90, sw=1.2))
    o.append(T(30, 112, "Pneumatic supply", 7.0, anchor="start"))
    o.append(T(30, 122, "(1.4 kg/cm²)", 7.0, anchor="start"))
    o.append(_rect(250, 86, 12, 8, fill=INK, sw=0))
    o.append(T(256, 76, "Restriction", 7.0))
    o.append(_poly([(300, 84), (300, 96), (326, 91), (326, 89)],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(T(316, 76, "Nozzle", 7.0))
    o.append(_circle(340, 68, 2.8, fill="#ffffff", sw=1.1))
    o.append(_line(340, 70, 340, 150, sw=1.4))
    o.append(_hatch(340, 150))
    o.append(T(348, 80, "Flapper operated by", 7.0, anchor="start"))
    o.append(T(348, 90, "process variable", 7.0, anchor="start"))
    o.append(_ar(345, 86, 342, 88, color=GREY, sw=1.0))
    o.append(_poly([(310, 96), (310, 118), (206, 118)], sw=1.2))
    o.append(_rect(150, 118, 112, 36, fill="#eef3fb", sw=1.2))
    o.append(T(206, 140, "Pneumatic relay", 7.6))
    o.append(_ar(206, 154, 206, 196, sw=1.3))
    o.append(T(206, 208, "Output", 7.4))
    return _mk(3, o, "Pneumatic ON-OFF nozzle-flapper circuit",
               "Sơ đồ khí nén đóng cắt với vòi phun và cánh chắn",
               "Pneumatic ON-OFF circuit with a restriction, nozzle and flapper",
               "Sơ đồ khí nén: nguồn khí 1.4 kg/cm² đi qua tiết lưu và vòi phun tới cánh chắn do biến số quá trình điều khiển; áp suất ngược điều khiển rơ le khí nén cho đầu ra đóng cắt.",
               "Pneumatic diagram: a 1.4 kg/cm² supply passes through a restriction and nozzle toward a flapper moved by the process variable; the back pressure drives a pneumatic relay that produces the ON-OFF output.")


# ---------------------------------------------------------------- 6.4
@_reg
def fig_f04():
    """Fig. 6.4 - Quarter amplitude decay response."""
    o = [_defs()]
    o.append(_ar(92, 192, 92, 44, sw=1.2))
    o.append(_ar(92, 192, 626, 192, sw=1.2))
    o.append(_vtxt(26, 120, "Controlled variable", 7.4))
    o.append(T(634, 196, "Time", 7.4, anchor="start"))
    o.append(_line(92, 120, 600, 120, sw=1.2))
    decay = [(92, 120), (110, 104), (130, 82), (150, 66), (170, 62),
             (190, 70), (210, 92), (230, 118), (250, 145), (270, 158),
             (290, 156), (310, 140), (330, 122), (350, 108), (370, 104),
             (390, 110), (410, 120), (430, 126), (450, 126), (470, 122),
             (490, 119), (520, 120), (560, 120)]
    o.append(_poly(decay, sw=1.8, color=BLUE))
    o.append(_darrow(170, 64, 118))
    o.append(T(180, 94, "y", 7.6, anchor="start"))
    o.append(_darrow(378, 105, 118))
    o.append(T(388, 114, "x", 7.6, anchor="start"))
    o.append(T(505, 100, "x/y = 1/4", 7.4, anchor="start"))
    return _mk(4, o, "Quarter amplitude decay",
               "Đáp ứng suy giảm biên độ một phần tư",
               "Quarter amplitude decay of a proportional-control response",
               "Đồ thị biến số điều khiển dao động suy dần quanh giá trị ổn định, với biên độ đầu là y và biên độ sau là x, tỷ lệ x trên y bằng một phần tư.",
               "Response curve of the controlled variable decaying toward the steady value; the first peak amplitude y and the second peak amplitude x satisfy x/y = 1/4.")


# ---------------------------------------------------------------- 6.5
@_reg
def fig_f05():
    """Fig. 6.5 - Sustained cycling from high proportional gain."""
    o = [_defs()]
    o.append(_ar(92, 196, 92, 44, sw=1.2))
    o.append(_ar(92, 196, 626, 196, sw=1.2))
    o.append(_vtxt(26, 124, "Controlled variable", 7.4))
    o.append(T(634, 200, "Time", 7.4, anchor="start"))
    o.append(_line(92, 120, 610, 120, sw=1.0, dash="6 4"))
    cyc = [(92, 120), (110, 95), (130, 68), (150, 58), (170, 62),
           (190, 82), (210, 112), (230, 150), (250, 176), (270, 172),
           (290, 145), (310, 112), (330, 90), (350, 88), (370, 102),
           (390, 120)]
    for xx in range(395, 611, 5):
        cyc.append((xx, 120 - 10 * math.sin(2 * math.pi * (xx - 390) / 40.0)))
    o.append(_poly(cyc, sw=1.8, color=BLUE))
    o.append(T(520, 88, "Set value", 7.0, anchor="start"))
    o.append(_ar(516, 92, 586, 118, color=GREY, sw=1.0))
    return _mk(5, o, "Sustained oscillation at high gain",
               "Dao động duy trì khi hệ số khuếch đại quá lớn",
               "Sustained oscillation of the controlled variable at high controller gain",
               "Đồ thị biến số điều khiển dao động lớn rồi duy trì thành chu kỳ nhỏ quanh giá trị cài đặt, minh họa hiện tượng chu kỳ do hệ số khuếch đại quá cao.",
               "Controlled variable swings widely and then settles into small sustained cycles about the set value, illustrating cycling caused by excessive controller gain.")


# ---------------------------------------------------------------- 6.6
@_reg
def fig_f06():
    """Fig. 6.6 - Electronic implementation of proportional action."""
    o = [_defs()]
    o.append(_circle(70, 80, 2.8, fill="#ffffff", sw=1.1))
    o.append(_circle(70, 170, 2.8, fill="#ffffff", sw=1.1))
    o.append(T(56, 76, "Ein", 7.2, anchor="end"))
    o.append(T(56, 86, "(error signal)", 7.0, anchor="end"))
    o.append(_line(72, 80, 116, 80, sw=1.2))
    o.append(_cap_h(120, 80))
    o.append(_line(124, 80, 200, 80, sw=1.2))
    o.append(T(120, 64, "Cin", 7.4))
    o.append(T(120, 50, "Input capacitor", 7.0))
    o.append(_oa(200, 60, 70, 60, "OA"))
    o.append(_line(200, 112, 200, 145, sw=1.1))
    o.append(_gnd(200, 145))
    o.append(_poly([(160, 80), (160, 42), (270, 42), (270, 90)], sw=1.2))
    o.append(_cap_h(214, 42))
    o.append(T(214, 30, "Cfb", 7.4))
    o.append(T(330, 30, "Feedback capacitor", 7.0, anchor="start"))
    o.append(_ar(326, 33, 226, 34, color=GREY, sw=1.0))
    o.append(_line(270, 90, 430, 90, sw=1.2))
    o.append(_circle(430, 90, 2.8, fill="#ffffff", sw=1.1))
    o.append(T(440, 86, "E0 (Controller output)", 7.2, anchor="start"))
    o.append(_line(400, 90, 400, 100, sw=1.1))
    o.append(_zig_v(400, 100, 158, n=6, amp=3.2))
    o.append(_line(400, 158, 400, 170, sw=1.1))
    o.append(_line(70, 170, 430, 170, sw=1.2))
    o.append(_ar(432, 128, 405, 128, color=GREY, sw=1.0))
    o.append(T(440, 146, "Proportional band", 7.0, anchor="start"))
    o.append(T(440, 156, "adjustment potentiometer", 7.0, anchor="start"))
    return _mk(6, o, "Electronic proportional controller",
               "Mạch điện tử thực hiện tác vụ tỷ lệ với tụ đầu vào và tụ phản hồi",
               "Electronic proportional controller with input and feedback capacitors",
               "Sơ đồ mạch khuếch đại thu toán: tín hiệu sai số Ein qua tụ Cin tới chân vào đảo, tụ Cfb phản hồi từ đầu ra E0; chiết áp giữa đầu ra và đường tham chiếu chỉnh dải tỷ lệ.",
               "Op-amp circuit: the error signal Ein passes through capacitor Cin to the inverting input while capacitor Cfb feeds the output E0 back; a potentiometer between the output and the reference rail adjusts the proportional band.")


# ---------------------------------------------------------------- 6.7
@_reg
def fig_f07():
    """Fig. 6.7 - Pneumatic implementation of proportional action."""
    o = [_defs()]
    o.append(_ar(55, 80, 72, 80, sw=1.3))
    o.append(_line(72, 80, 306, 80, sw=1.2))
    o.append(T(30, 102, "Air supply", 7.0, anchor="start"))
    o.append(T(30, 112, "1.4 kg/cm²", 7.0, anchor="start"))
    o.append(_rect(242, 76, 12, 8, fill=INK, sw=0))
    o.append(T(248, 66, "Restriction", 7.0))
    o.append(_poly([(306, 74), (306, 86), (330, 81), (330, 79)],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(T(320, 66, "Nozzle", 7.0))
    o.append(_circle(344, 58, 2.8, fill="#ffffff", sw=1.1))
    o.append(_line(344, 60, 344, 164, sw=1.4))
    o.append(_hatch(344, 164))
    o.append(T(352, 72, "Flapper operated by", 7.0, anchor="start"))
    o.append(T(352, 82, "process variable", 7.0, anchor="start"))
    o.append(_ar(348, 78, 346, 80, color=GREY, sw=1.0))
    o.append(_poly([(316, 86), (316, 108), (206, 108)], sw=1.2))
    o.append(_rect(150, 108, 112, 38, fill="#eef3fb", sw=1.2))
    o.append(T(206, 131, "Pneumatic relay", 7.6))
    o.append(_line(206, 146, 206, 198, sw=1.2))
    o.append(_ar(206, 198, 156, 198, sw=1.3))
    o.append(T(148, 202, "Output", 7.2, anchor="end"))
    o.append(_poly([(206, 180), (470, 180), (470, 168)], sw=1.1))
    o.append(T(382, 118, "Spring", 7.0))
    o.append(_zig_v(382, 132, 160, n=6, amp=3.5))
    o.append(_bellows(432, 138, 44, 30))
    o.append(T(476, 110, "Proportional bellows", 7.0))
    o.append(_ar(380, 116, 382, 130, color=GREY, sw=1.0))
    o.append(_ar(448, 116, 448, 136, color=GREY, sw=1.0))
    return _mk(7, o, "Pneumatic proportional controller",
               "Sơ đồ khí nén thực hiện tác vụ tỷ lệ với ống nhồi và lò xo",
               "Pneumatic proportional controller with nozzle, bellows and spring",
               "Sơ đồ khí nén: vòi phun và cánh chắn tạo áp suất ngược cho rơ le; đầu ra cấp cho ống nhồi tỷ lệ cân bằng với lò xo, tỷ lệ cánh chắn trên dưới vòi phun quyết định hệ số khuếch đại.",
               "Pneumatic circuit: the nozzle and flapper develop back pressure for the relay; the output acts on a proportional bellows balanced by a spring, and the flapper lever ratio sets the proportional gain.")


# ---------------------------------------------------------------- 6.8
@_reg
def fig_f08():
    """Fig. 6.8 - Electronic integrator circuit."""
    o = [_defs()]
    o.append(_circle(70, 90, 2.8, fill="#ffffff", sw=1.1))
    o.append(_circle(70, 180, 2.8, fill="#ffffff", sw=1.1))
    o.append(_darrow(52, 94, 176))
    o.append(T(40, 137, "Ein", 7.4))
    o.append(T(20, 198, "Error signal", 7.0, anchor="start"))
    o.append(_line(72, 90, 120, 90, sw=1.2))
    o.append(_zig_v(120, 94, 114, n=4, amp=3.0))
    o.append(_zig_v(120, 118, 138, n=4, amp=3.0))
    o.append(T(136, 104, "R1", 7.2, anchor="start"))
    o.append(T(136, 128, "R2", 7.2, anchor="start"))
    o.append(_zig_v(120, 142, 168, n=5, amp=3.0))
    o.append(_ar(136, 160, 123, 154, color=GREY, sw=1.0))
    o.append(T(140, 172, "Integral adjustment", 7.0, anchor="start"))
    o.append(_line(120, 168, 120, 180, sw=1.1))
    o.append(_line(72, 180, 440, 180, sw=1.2))
    o.append(_line(120, 116, 180, 116, sw=1.2))
    o.append(_cap_h(160, 116))
    o.append(T(160, 104, "Cin", 7.4))
    o.append(_oa(210, 96, 70, 60, "Op. Amp."))
    o.append(_line(210, 138, 210, 160, sw=1.1))
    o.append(_gnd(210, 160))
    o.append(_poly([(160, 116), (160, 60), (280, 60), (280, 126)], sw=1.2))
    o.append(_cap_h(214, 60))
    o.append(T(214, 48, "Cfb", 7.4))
    o.append(_line(280, 126, 440, 126, sw=1.2))
    o.append(_circle(440, 126, 2.8, fill="#ffffff", sw=1.1))
    o.append(_darrow(456, 130, 176))
    o.append(T(468, 154, "E0", 7.4, anchor="start"))
    return _mk(8, o, "Electronic integrator controller",
               "Mạch tích phân điện tử với chiết áp chỉnh thời gian tích phân",
               "Electronic integrator circuit with an adjustable integral resistor",
               "Sơ đồ mạch tích phân: tín hiệu sai số Ein qua bộ chia R1, R2 và biến trở Rv tới tụ Cin và bộ khuếch đại; tụ Cfb phản hồi từ đầu ra E0, tạo đầu ra thay đổi liên tục khi còn sai số.",
               "Integrator circuit: the error signal Ein passes through divider resistors R1, R2 and variable resistor Rv to capacitor Cin and the amplifier; capacitor Cfb feeds back the output E0, producing a continuous change while an error persists.")


# ---------------------------------------------------------------- 6.9
@_reg
def fig_f09():
    """Fig. 6.9 - Integral action response to a measurement input change."""
    o = [_defs()]
    o.append(_ar(100, 192, 100, 44, sw=1.2))
    o.append(_ar(100, 192, 626, 192, sw=1.2))
    o.append(T(634, 196, "Time", 7.4, anchor="start"))
    o.append(_line(100, 110, 590, 110, sw=1.1, dash="7 3"))
    o.append(_ar(590, 110, 568, 110, sw=1.1))
    o.append(T(598, 106, "Set value", 7.0, anchor="start"))
    for xx in (250, 400):
        o.append(_line(xx, 62, xx, 186, sw=0.9, dash="4 4", color=GREY))
    pulse = [(100, 110), (250, 110), (250, 70), (400, 70),
             (400, 140), (560, 140)]
    o.append(_poly(pulse, sw=1.8, color=BLUE))
    o.append(T(430, 54, "Measurement input change", 7.0, anchor="start"))
    o.append(_ar(428, 58, 370, 68, color=GREY, sw=1.0))
    out = [(100, 150), (250, 150), (400, 172), (560, 172)]
    o.append(_poly(out, sw=1.8, color=RED))
    o.append(T(580, 176, "Output", 7.2, anchor="start"))
    o.append(_ar(576, 178, 548, 178, color=GREY, sw=1.0))
    return _mk(9, o, "Integral action response",
               "Đáp ứng tích phân khi đầu vào đo lường thay đổi",
               "Integral-action output ramping during a measurement input change",
               "Đồ thị thể hiện đầu vào đo lường dạng xung chữ nhật quanh giá trị cài đặt và đầu ra tăng tuyến tính trong thời gian sai số tồn tại, rồi giữ giá trị mới.",
               "Graph of a rectangular measurement input pulse about the set value and a controller output that ramps linearly while the deviation persists, then holds at a new level.")
