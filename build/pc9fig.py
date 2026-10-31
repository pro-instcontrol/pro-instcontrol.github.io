# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 9 — Output Modes, Equations, Cascade Control."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- 9.1
def fig_9_1():
    """The output section of a controller: calculation, mode, limit, real OP."""
    o = [_txt(16, 66, "CV", 8.5, anchor="start"),
         _txt(16, 78, "từ khối PID", 6.8, anchor="start", color=GREY)]
    o.append(_arrow(46, 62, 76, 62))
    o.append(_node(90, 62, "Σ", r=13))

    o.append(_arrow(103, 62, 132, 62))
    o.append(_box(134, 46, 118, 32, "ĐẦU RA ẢO", size=7.8))
    o.append(_arrow(252, 62, 282, 62))
    o.append(_box(284, 46, 130, 32, "GIỚI HẠN 0–100 %", size=7.4))
    o.append(_arrow(414, 62, 444, 62))
    o.append(_box(446, 46, 118, 32, "ĐẦU RA THẬT", size=7.8))
    o.append(_arrow(564, 62, 606, 62))
    o.append(_txt(612, 66, "OP", 8.5, anchor="start"))

    # the manual value that the PID increments
    o.append(_txt(90, 132, "giá trị MANUAL", 7.5, color=GREY))
    o.append(_txt(90, 144, "(live zero)", 6.8, color=GREY))
    o.append(_arrow(90, 122, 90, 77))

    # mode annotation
    o.append(_rect(134, 96, 278, 26, "#fbfaf6", sw=0.7, stroke="#ddd7c8"))
    o.append(_txt(273, 113, "chế độ: MANUAL · AUTO · CASCADE", 7.6, color=INK))
    o.append(_txt(134, 152, "chỉ ở AUTO hay CASCADE thì phép tính PID mới tác động lên đầu ra",
                  7.2, anchor="start", color=GREY))
    return _finish(o, 660, 168,
                   "Hình 9-1. Khối đầu ra của một bộ điều khiển PID: giá trị CV từ khối tính toán, giá "
                   "trị MANUAL, chế độ, giới hạn và đầu ra thật.",
                   "Figure 9-1. The output section of a PID controller: the CV from the calculation "
                   "block, the manual value, the mode, the limit and the real output.",
                   "Sơ đồ khối: CV và giá trị MANUAL cộng lại thành đầu ra ảo, qua khối giới hạn 0 đến "
                   "100 phần trăm thành đầu ra thật; nhãn chế độ nằm dưới khối giới hạn.",
                   "Block diagram: CV and the manual value sum into a virtual output, which passes a "
                   "0 to 100 per cent limiter to become the real output; the mode label sits under the "
                   "limiter.")


# ---------------------------------------------------------------- 9.2
def fig_9_2():
    """Two output blocks on one controller, each with its own mode."""
    o = [_box(20, 74, 96, 34, "PID", size=9)]
    o.append(_arrow(116, 91, 146, 91))
    o.append(_node(160, 91, "Σ", r=13))
    o.append(_line(173, 91, 196, 91))
    o.append(_line(196, 44, 196, 138))
    for y in (44, 138):
        o.append(_arrow(196, y, 214, y, sw=1))

    o.append(_box(216, 26, 120, 36, "KHỐI RA 1", size=7.8))
    o.append(_box(216, 120, 120, 36, "KHỐI RA 2", size=7.8))
    o.append(_arrow(336, 44, 380, 44))
    o.append(_arrow(336, 138, 380, 138))
    o.append(_txt(386, 48, "OP1  (CASCADE)", 8, anchor="start"))
    o.append(_txt(386, 142, "OP2  (AUTO)", 8, anchor="start"))

    o.append(_txt(276, 78, "cùng một lượng tăng ∆CV", 7.4, color=GREY))
    o.append(_txt(276, 96, "cộng vào cả hai khối", 7.4, color=GREY))
    o.append(_txt(276, 114, "nhưng giá trị tuyệt đối khác nhau", 7.4, color=GREY))
    return _finish(o, 660, 176,
                   "Hình 9-2. Hai khối đầu ra độc lập trên cùng một bộ điều khiển: cùng nhận một lượng "
                   "tăng nhưng giữ giá trị tuyệt đối riêng.",
                   "Figure 9-2. Two independent output blocks on one controller: both take the same "
                   "increment but keep their own absolute values.",
                   "Sơ đồ: khối PID cộng vào một điểm rồi rẽ thành hai nhánh, mỗi nhánh qua một khối "
                   "đầu ra riêng cho ra OP1 và OP2.",
                   "Diagram: the PID block sums into one point that splits into two branches, each "
                   "through its own output block to give OP1 and OP2.")


# ---------------------------------------------------------------- 9.3
def fig_9_3():
    """Single loop temperature control — the reference case."""
    o = [_box(24, 62, 92, 34, "TC", size=9.5)]
    o.append(_txt(24, 52, "SP nhiệt độ", 7.4, anchor="start", color=GREY))
    o.append(_arrow(70, 40, 70, 60, sw=1))
    o.append(_arrow(116, 79, 176, 79))
    o.append(_box(178, 62, 84, 34, "VAN", size=9))
    o.append(_arrow(262, 79, 316, 79))
    o.append(_txt(318, 74, "nhiên liệu", 7.4, anchor="start", color=GREY))

    # the heater as a box with a coil
    o.append(_rect(318, 44, 130, 74, "#eef3fb", sw=1.1, stroke=INK))
    o.append(_txt(383, 68, "LÒ", 9))
    o.append(_txt(383, 82, "nhiệt", 7, color=GREY))
    o.append(_path("M 336 100 q 12 -14 24 0 q 12 14 24 0 q 12 -14 24 0", fill="none", sw=1.2,
                   color=RED))

    o.append(_arrow(448, 79, 508, 79))
    o.append(_txt(510, 74, "T2 ra", 7.4, anchor="start", color=GREY))

    # the measurement loop back to the controller
    o.append(_line(470, 79, 470, 150))
    o.append(_line(470, 150, 70, 150))
    o.append(_arrow(70, 150, 70, 98))
    o.append(_box(430, 132, 44, 24, "TT", size=8.5))
    o.append(_txt(200, 164, "một vòng, một bộ điều khiển, nhiễu áp suất nhiên liệu đi thẳng vào T2",
                  7.2, color=GREY))
    return _finish(o, 660, 186,
                   "Hình 9-3. Điều khiển nhiệt độ một vòng: bộ điều khiển TC lái trực tiếp vị trí van "
                   "nhiên liệu.",
                   "Figure 9-3. Single-loop temperature control: the TC drives the fuel valve position "
                   "directly.",
                   "Sơ đồ vòng: điểm đặt vào bộ điều khiển TC, đầu ra tới van nhiên liệu, lò gia nhiệt, "
                   "cảm biến TT đưa nhiệt độ ra về bộ điều khiển.",
                   "A loop diagram: the set point enters TC, its output drives the fuel valve, the "
                   "heater, and a TT returns the outlet temperature to the controller.")


# ---------------------------------------------------------------- 9.4
def fig_9_4():
    """Cascade: TC drives the FC set point; both loops have their own transmitter."""
    o = [_box(24, 52, 84, 30, "TC", size=9.5),
         _box(24, 140, 84, 30, "FC", size=9.5)]
    o.append(_txt(44, 30, "SP nhiệt độ", 7.2, anchor="middle", color=GREY))
    o.append(_arrow(44, 36, 44, 50))

    # TC output becomes the FC set point
    o.append(_arrow(108, 67, 152, 67))
    o.append(_line(152, 67, 152, 122))
    o.append(_line(152, 122, 66, 122))
    o.append(_arrow(66, 122, 66, 138))
    o.append(_txt(160, 90, "OP của TC", 7.2, anchor="start", color=RED))
    o.append(_txt(160, 102, "= SP của FC", 7.2, anchor="start", color=RED))

    o.append(_arrow(108, 155, 196, 155))
    o.append(_box(198, 140, 66, 30, "VAN", size=9))
    o.append(_arrow(264, 155, 312, 155))
    o.append(_rect(314, 116, 118, 78, "#eef3fb", sw=1.1, stroke=INK))
    o.append(_txt(373, 140, "LÒ", 9))
    o.append(_path("M 334 172 q 12 -12 24 0 q 12 12 24 0", fill="none", sw=1.2, color=RED))
    o.append(_arrow(432, 155, 486, 155))
    o.append(_txt(492, 172, "T2", 8.5, anchor="start"))

    # TT on the outlet, feeding the primary
    o.append(_box(446, 143, 40, 24, "TT", size=8.2))
    o.append(_line(466, 143, 466, 20))
    o.append(_line(466, 20, 88, 20))
    o.append(_arrow(88, 20, 88, 50))
    o.append(_txt(300, 15, "nhiệt độ ra hồi tiếp về TC", 7, color=GREY))

    # FT on the fuel line, feeding the secondary
    o.append(_line(288, 155, 288, 182))
    o.append(_box(266, 182, 44, 22, "FT", size=8.2))
    o.append(_line(266, 193, 66, 193))
    o.append(_arrow(66, 193, 66, 172))
    o.append(_txt(330, 208, "lưu lượng nhiên liệu hồi tiếp về FC", 7, anchor="start", color=GREY))
    return _finish(o, 660, 220,
                   "Hình 9-4. Cascade hai bộ điều khiển: đầu ra của TC trở thành điểm đặt của FC, nên "
                   "nhiễu áp suất nhiên liệu bị chặn trước khi tới nhiệt độ.",
                   "Figure 9-4. Two-controller cascade: the TC output becomes the FC set point, so fuel "
                   "pressure disturbances are stopped before they reach the temperature.",
                   "Sơ đồ: TC ở trên, FC ở dưới; đầu ra TC đi vào điểm đặt của FC, FC lái van, van cấp "
                   "nhiên liệu cho lò; cảm biến nhiệt độ TT hồi tiếp về TC và cảm biến lưu lượng FT hồi "
                   "tiếp về FC.",
                   "Diagram: TC above, FC below; the TC output feeds the FC set point, FC drives the "
                   "valve, the valve feeds the heater; a TT feeds back to TC and an FT feeds back to "
                   "FC.")


# ---------------------------------------------------------------- 9.5
def fig_9_5():
    """Equation type A: every action is computed from the error."""
    o = [_node(72, 92, "Σ", r=13)]
    o.append(_txt(14, 88, "SP", 8.5, anchor="start"))
    o.append(_txt(14, 130, "PV", 8.5, anchor="start"))
    o.append(_arrow(40, 92, 58, 92))
    o.append(_arrow(40, 126, 72, 126))
    o.append(_arrow(72, 126, 72, 106))
    o.append(_txt(86, 84, "ERR", 7.5, anchor="start", color=GREY))

    o.append(_line(85, 92, 132, 92))
    o.append(_line(132, 42, 132, 142))
    for y in (42, 92, 142):
        o.append(_arrow(132, y, 146, y, sw=1))
    o.append(_box(148, 28, 150, 28, "P:  K_c · ERR", size=7.8))
    o.append(_box(148, 78, 150, 28, "I:  K_c/T_int ∫ERR", size=7.8))
    o.append(_box(148, 128, 150, 28, "D:  K_c·T_der dERR/dt", size=7.4))
    for y in (42, 92, 142):
        o.append(_line(298, y, 330, y))
    o.append(_line(330, 42, 330, 142))
    o.append(_node(350, 92, "Σ", r=13))
    o.append(_arrow(364, 92, 420, 92))
    o.append(_txt(426, 96, "OP", 8.5, anchor="start"))

    o.append(_rect(452, 30, 184, 118, "#fbfaf6", sw=0.8, stroke="#ddd7c8"))
    o.append(_txt(544, 54, "loại A", 9.5))
    o.append(_txt(544, 76, "P, I, D đều tính từ ERR", 7.4, color=GREY))
    o.append(_txt(544, 94, "một bước nhảy SP", 7.4, color=GREY))
    o.append(_txt(544, 108, "đi thẳng vào cả ba khâu", 7.4, color=GREY))
    o.append(_txt(544, 132, "bộ điều khiển tiêu chuẩn", 7.4, color=INK))
    return _finish(o, 660, 164,
                   "Hình 9-5. Phương trình loại A: cả ba khâu P, I, D đều lấy sai lệch ERR làm đầu vào.",
                   "Figure 9-5. Equation type A: all three actions take the error as their input.",
                   "Sơ đồ khối: sai lệch rẽ vào ba nhánh P, I, D rồi cộng lại; bên phải là khung ghi "
                   "chú loại A dùng cho bộ điều khiển tiêu chuẩn.",
                   "Block diagram: the error fans into three branches P, I and D that sum; a note box "
                   "on the right says type A is the standard controller.")


# ---------------------------------------------------------------- 9.6
def fig_9_6():
    """Equation type C: P and D act on PV only; the error feeds only the integral."""
    o = [_txt(14, 96, "PV", 8.5, anchor="start")]
    o.append(_arrow(46, 92, 58, 92))
    o.append(_circle(72, 92, 2.6, fill=INK, color=INK))
    o.append(_line(72, 40, 72, 138))
    o.append(_arrow(72, 40, 156, 40, sw=1))
    o.append(_arrow(72, 138, 156, 138, sw=1))
    o.append(_arrow(72, 92, 103, 92))

    o.append(_node(118, 92, "Σ", r=13))
    o.append(_txt(118, 152, "SP", 8.5))
    o.append(_arrow(118, 142, 118, 106))
    o.append(_arrow(131, 92, 156, 92))
    o.append(_txt(96, 74, "ERR", 7, anchor="middle", color=GREY))

    o.append(_box(158, 26, 152, 28, "P:  K_c · PV", size=8))
    o.append(_box(158, 78, 152, 28, "I:  K_c/T_int ∫ERR", size=8))
    o.append(_box(158, 124, 152, 28, "D:  T_der · dPV/dt", size=8))

    for y in (40, 92, 138):
        o.append(_line(310, y, 342, y))
    o.append(_line(342, 40, 342, 138))
    o.append(_node(362, 89, "Σ", r=13))
    o.append(_arrow(376, 89, 428, 89))
    o.append(_txt(434, 93, "OP", 8.5, anchor="start"))

    o.append(_rect(452, 26, 184, 126, "#fbfaf6", sw=0.8, stroke="#ddd7c8"))
    o.append(_txt(544, 50, "loại C", 9.5))
    o.append(_txt(544, 72, "P và D chỉ thấy PV", 7.4, color=GREY))
    o.append(_txt(544, 90, "chỉ khâu I thấy ERR", 7.4, color=GREY))
    o.append(_txt(544, 112, "bước nhảy SP", 7.4, color=RED))
    o.append(_txt(544, 126, "→ đầu ra tăng dần", 7.4, color=RED))
    o.append(_txt(544, 142, "không có cú đập", 7.4, color=RED))
    return _finish(o, 660, 176,
                   "Hình 9-6. Phương trình loại C: khâu P và D lấy trực tiếp PV, chỉ khâu I lấy sai lệch, "
                   "nên bước nhảy điểm đặt trở thành một đoạn dốc.",
                   "Figure 9-6. Equation type C: P and D take PV directly, only the integral sees the "
                   "error, so a set-point step becomes a ramp.",
                   "Sơ đồ khối: PV rẽ vào ba nhánh P, I, D; SP chỉ đi vào bộ cộng tạo sai lệch cho "
                   "nhánh I; ba nhánh cộng lại thành đầu ra.",
                   "Block diagram: PV fans into the P, I and D branches; SP enters only the summing "
                   "node that feeds the I branch; the three sum to the output.")


# ---------------------------------------------------------------- 9.7
def fig_9_7():
    """Saturation versus non-saturation: windup, and the recovery that comes too late."""
    x0, y0, W, H = 70, 48, 500, 128
    dt, ki, base = 0.02, 34.0, 60.0

    def err(t):
        return 1.0 if t < 2.2 else -0.6

    sat, non = [], []
    vi = 0.0          # the virtual integrator of a saturating controller: never clamped
    ni = 0.0          # the integral of a non-saturating controller: reset each scan
    for i in range(0, 201):
        t = i * dt
        vi += ki * err(t) * dt
        sat.append((t, min(100.0, max(0.0, base + vi))))
        ni += ki * err(t) * dt
        out = min(100.0, max(0.0, base + ni))
        ni = out - base
        non.append((t, out))

    o = [_axes(x0, y0, W, H, "thời gian", "đầu ra (%)",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_line(x0, y0, x0 + W, y0, sw=1.1, dash="4 3", color=RED))
    o.append(_txt(x0 + 6, y0 + 12, "trần 100 %", 7, anchor="start", color=RED))

    def trace(pts):
        return _poly([(x0 + W * t / 4.0, y0 + H * (1 - v / 100.0)) for t, v in pts],
                     sw=2.0, color=None)

    o.append(_poly([(x0 + W * t / 4.0, y0 + H * (1 - v / 100.0)) for t, v in non],
                   sw=2.0, color=BLUE))
    o.append(_poly([(x0 + W * t / 4.0, y0 + H * (1 - v / 100.0)) for t, v in sat],
                   sw=2.0, color=GOLD))
    o.append(_legend_h(x0 + 10, y0 + H + 44,
                       [(BLUE, "không bão hoà — hồi phục ngay", ""),
                        (GOLD, "bão hoà — cuộn tích phân rồi mới hồi phục", "")], gap=24))
    o.append(_txt(x0 + W * 0.56, y0 + H * 0.16, "bão hoà vẫn giữ 100 %", 7.5,
                  anchor="start", color=GOLD))
    o.append(_txt(x0 + W * 0.56, y0 + H * 0.28, "dù nhiễu đã đảo chiều", 7.2,
                  anchor="start", color=GOLD))

    return _finish(o, 660, 232,
                   "Hình 9-7. Bão hoà và không bão hoà: bộ điều khiển bão hoà giữ đầu ra ở 100 % lâu hơn "
                   "sau khi nhiễu đã đảo chiều.",
                   "Figure 9-7. Saturation against non-saturation: the saturating controller holds the "
                   "output at 100 per cent long after the disturbance has reversed.",
                   "Hai đường đầu ra theo thời gian: cả hai cùng chạm trần 100 phần trăm, nhưng đường "
                   "bão hoà ở lại trên trần lâu hơn hẳn rồi mới đi xuống.",
                   "Two output traces over time: both reach the 100 per cent ceiling, but the "
                   "saturating one stays there much longer before coming down.")


# ---------------------------------------------------------------- 9.8
def fig_9_8():
    """Cascade tuning order: inside out, treating each tuned loop as part of the process."""
    o = [_rect(20, 22, 300, 120, "#f6efe0", sw=1.0, stroke="#d9cdb2")]
    o.append(_txt(170, 40, "1. chỉnh FC trước", 8.5, color=INK))
    o.append(_box(40, 56, 90, 30, "TC", size=9))
    o.append(_box(40, 96, 90, 30, "FC", size=9))
    o.append(_arrow(130, 111, 176, 111))
    o.append(_box(178, 96, 60, 30, "VAN", size=8.5))
    o.append(_arrow(85, 86, 85, 96))
    o.append(_txt(170, 136, "TC còn để nguyên", 7, color=GREY))

    o.append(_rect(344, 22, 300, 120, "#eef3fb", sw=1.0, stroke="#b9cbe6"))
    o.append(_txt(494, 40, "2. rồi chỉnh TC", 8.5, color=INK))
    o.append(_box(364, 56, 90, 30, "TC", size=9))
    o.append(_box(364, 96, 90, 30, "FC", size=9))
    o.append(_arrow(454, 111, 500, 111))
    o.append(_box(502, 96, 60, 30, "VAN", size=8.5))
    o.append(_arrow(409, 86, 409, 96))
    o.append(_txt(494, 136, "FC đã chỉnh = một khâu của quá trình", 7, color=GREY))

    o.append(_txt(20, 164, "Vòng trong (secondary) chỉnh trước vì nó nhanh; vòng ngoài (primary) "
                           "chỉnh sau, coi vòng trong là một khâu của quá trình.", 7.6,
                  anchor="start", color=GREY))
    return _finish(o, 660, 180,
                   "Hình 9-8. Thứ tự chỉnh định cascade: vòng trong trước, rồi coi vòng đã chỉnh là một "
                   "phần của quá trình để chỉnh vòng ngoài.",
                   "Figure 9-8. Cascade tuning order: the inner loop first, then treat the tuned loop "
                   "as part of the process and tune the outer one.",
                   "Hai khung cạnh nhau: khung trái đánh dấu bước một chỉnh bộ điều khiển lưu lượng; "
                   "khung phải đánh dấu bước hai chỉnh bộ điều khiển nhiệt độ.",
                   "Two panels: the left marks step one, tuning the flow controller; the right marks "
                   "step two, tuning the temperature controller.")


# ---------------------------------------------------------------- 9.9
def fig_9_9():
    """One primary with three secondaries."""
    o = [_box(20, 96, 86, 32, "TC", size=9.5)]
    o.append(_txt(20, 86, "primary", 7, anchor="start", color=GREY))
    o.append(_line(106, 112, 146, 112))
    o.append(_line(146, 40, 146, 184))
    for y, lab in ((40, "FC-1"), (112, "FC-2"), (184, "FC-3")):
        o.append(_arrow(146, y, 168, y, sw=1))
        o.append(_box(170, y - 16, 74, 32, lab, size=8.5))
        o.append(_arrow(244, y, 292, y))
        o.append(_box(294, y - 14, 62, 28, "VAN", size=8))
        o.append(_arrow(356, y, 404, y))
        o.append(_txt(410, y + 4, "lưu lượng " + lab[-1], 7.4, anchor="start", color=GREY))

    o.append(_txt(24, 206, "một phép tính PID  ·  ba khối đầu ra riêng  ·  ba điểm khởi tạo riêng  ·  "
                           "ba bộ xử lý giới hạn riêng", 7.6, anchor="start", color=GREY))
    return _finish(o, 660, 214,
                   "Hình 9-9. Cascade với nhiều vòng thứ cấp: một bộ điều khiển sơ cấp có nhiều khối đầu "
                   "ra, mỗi khối lái một vòng thứ cấp riêng.",
                   "Figure 9-9. Cascade with multiple secondaries: one primary controller with several "
                   "output blocks, each driving its own secondary loop.",
                   "Sơ đồ: một bộ điều khiển TC duy nhất rẽ ra ba nhánh, mỗi nhánh qua một bộ điều "
                   "khiển lưu lượng và một van riêng.",
                   "Diagram: a single TC fans out into three branches, each through its own flow "
                   "controller and valve.")
