# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 6 — Digital Control Principles."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _rect, _txt)
from pcfig import _finish, _legend


# ---------------------------------------------------------------- 6.1
def fig_6_1():
    """Field (real) controller: P + I + filtered D, the form on the nameplate."""
    o = [_node(96, 96, "Σ", r=14)]
    o.append(_txt(16, 100, "SP", 8.5, anchor="start"))
    o.append(_arrow(44, 96, 79, 96))
    o.append(_txt(16, 190, "PV", 8.5, anchor="start"))
    o.append(_arrow(96, 186, 96, 113))
    o.append(_txt(80, 174, "−", 12, color=INK))
    o.append(_txt(116, 88, "ERR", 7.5, anchor="start", color=GREY))

    o.append(_line(110, 96, 172, 96))
    o.append(_line(172, 54, 172, 138))
    for y in (54, 96, 138):
        o.append(_arrow(172, y, 180, y, sw=1))

    o.append(_box(182, 37, 190, 34, "P:    K"))
    o.append(_box(182, 79, 190, 34, "I:    1 / (T_int·s)"))
    o.append(_box(182, 121, 190, 34, "D:    T_der·s\n/ (1 + α·T_der·s)"))

    for y in (54, 96, 138):
        o.append(_line(372, y, 404, y))
    o.append(_line(404, 54, 404, 138))
    o.append(_node(424, 96, "Σ", r=14))
    o.append(_arrow(438, 96, 588, 96))
    o.append(_txt(594, 100, "OP", 8.5, anchor="start"))

    o.append(_txt(182, 178, "α = 8 ÷ 12 trong thiết bị công nghiệp", 7.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 200,
                   "Hình 6-1. Sơ đồ khối bộ điều khiển thực (field controller): khâu P, I và một khâu "
                   "vi phân có lọc.",
                   "Figure 6-1. Block diagram of a field (real) controller: P, I and a filtered "
                   "derivative.",
                   "Sơ đồ khối: điểm đặt SP và giá trị đo PV vào bộ cộng, sai lệch ERR đi tới ba khâu "
                   "song song P, I và D có lọc, ba đầu ra cộng lại thành OP.",
                   "Block diagram: set point SP and measurement PV sum to an error, which fans into "
                   "three parallel P, I and filtered-D blocks whose outputs sum to OP.")


# ---------------------------------------------------------------- 6.2
def fig_6_2():
    """Ideal PID in parallel (non-interacting) form."""
    o = [_node(80, 92, "Σ", r=14)]
    o.append(_txt(14, 96, "SP", 8.5, anchor="start"))
    o.append(_arrow(42, 92, 63, 92))
    o.append(_txt(14, 184, "PV", 8.5, anchor="start"))
    o.append(_arrow(80, 180, 80, 109))
    o.append(_txt(64, 168, "−", 12, color=INK))

    o.append(_arrow(94, 92, 124, 92))
    o.append(_box(126, 78, 64, 28, "K", size=9))

    o.append(_line(190, 92, 214, 92))
    o.append(_line(214, 29, 214, 153))
    for y in (29, 91, 153):
        o.append(_arrow(214, y, 222, y, sw=1))

    o.append(_box(224, 14, 190, 30, "1", size=9))
    o.append(_box(224, 76, 190, 30, "1 / (T_int·s)", size=9))
    o.append(_box(224, 138, 190, 30, "T_der·s", size=9))

    for y in (29, 91, 153):
        o.append(_line(414, y, 446, y))
    o.append(_line(446, 29, 446, 153))
    o.append(_node(466, 91, "Σ", r=14))
    o.append(_arrow(480, 91, 600, 91))
    o.append(_txt(606, 95, "OP", 8.5, anchor="start"))

    o.append(_txt(224, 190, "dạng song song lý tưởng:   OP = K · (1 + 1/(T_int·s) + T_der·s) · ERR",
                  7.5, anchor="start", color=GREY))
    return _finish(o, 660, 204,
                   "Hình 6-2. Sơ đồ khối bộ điều khiển PID lý tưởng.",
                   "Figure 6-2. Block diagram of the ideal PID controller.",
                   "Sơ đồ: sai lệch qua khâu khuếch đại K rồi rẽ vào ba nhánh song song có hệ số 1, "
                   "một chia T tích phân nhân s, và T vi phân nhân s; ba nhánh cộng lại thành OP.",
                   "Diagram: the error passes through gain K then splits into three parallel branches "
                   "with factors 1, one over T-integral times s, and T-derivative times s; the three "
                   "sum to OP.")


# ---------------------------------------------------------------- 6.3
def fig_6_3():
    """Incremental form: only the change between scans is used."""
    x0, y0, W, H = 58, 40, 556, 128
    o = [_axes(x0, y0, W, H, "số lần quét (scan)", "ERR",
               xt=[(0, "0"), (1 / 6.0, "2"), (2 / 6.0, "4"), (3 / 6.0, "6"),
                   (4 / 6.0, "8"), (5 / 6.0, "10"), (1, "12")],
               yt=[(0, "0"), (0.25, "0,25"), (0.5, "0,5"), (0.75, "0,75"), (1, "1")])]
    o.append(_curve(lambda t: math.exp(-t / 3.2), x0, y0, W, H, n=241,
                    xr=(0.0, 12.0), yr=(0.0, 1.0), color=INK, sw=1.8))
    for k in range(1, 11):
        t = float(k)
        v = math.exp(-t / 3.2)
        o.append(_circle(x0 + W * t / 12.0, y0 + H * (1 - v), 2.8, fill=BLUE, color=BLUE))

    t1, t2 = 3.0, 4.0
    v1, v2 = math.exp(-t1 / 3.2), math.exp(-t2 / 3.2)
    x1, x2 = x0 + W * t1 / 12.0, x0 + W * t2 / 12.0
    y1, y2 = y0 + H * (1 - v1), y0 + H * (1 - v2)
    o.append(_line(x1, y1, x2, y1, sw=0.8, dash="3 3", color=RED))
    o.append(_line(x2, y1, x2, y2, sw=1.6, color=RED))
    o.append(_circle(x2, y1, 2.0, fill=RED, color=RED))
    o.append(_txt(x2 + 9, (y1 + y2) / 2.0 + 3, "ΔERR", 8.5, anchor="start", color=RED))
    o.append(_txt(x0 + W - 12, y0 + 22, "ΔOP = K · ΔERR", 9, anchor="end", color=INK))
    o.append(_txt(x0 + W - 12, y0 + 36, "chỉ số gia giữa hai lần quét, không phải giá trị tuyệt đối",
                  7, anchor="end", color=GREY))
    return _finish(o, 660, 210,
                   "Hình 6-3. Ví dụ đồ thị của ΔOP: mỗi lần quét chỉ tính số gia.",
                   "Figure 6-3. Graphical example of delta-OP: each scan computes only an increment.",
                   "Đồ thị sai lệch giảm dần theo hàm mũ, chấm xanh ở mỗi lần quét; hai lần quét liên "
                   "tiếp được nối bằng một đoạn đỏ ghi delta ERR, chính là lượng thay đổi của đầu ra.",
                   "An exponentially decaying error with a blue dot at each scan; two consecutive "
                   "scans are joined by a red segment labelled delta-ERR, which is the output change.")


# ---------------------------------------------------------------- 6.4
def fig_6_4():
    """The nameplate formula, rewritten in F(s)."""
    o = [_rect(24, 20, 612, 112, "#fbfaf6", sw=0.8, stroke="#ddd7c8")]
    o.append(_txt(330, 50, "OP  =  K ·", 13))
    o.append(_txt(330, 76, "(1 + T_int·s) / (T_int·s)", 13))
    o.append(_txt(330, 102, "·  (1 + T_der·s) / (1 + α·T_der·s)", 13))
    o.append(_txt(330, 122, "=  K · PI · LEAD", 8.5, color=GREY))
    return _finish(o, 660, 150,
                   "Hình 6-4. Công thức bộ điều khiển thực viết theo F(s), dùng khâu vi phân dạng LEAD.",
                   "Figure 6-4. The real controller in F(s), using a lead algorithm for derivative.",
                   "Khung công thức: OP bằng K nhân phân số một cộng T tích phân nhân s trên T tích "
                   "phân nhân s, nhân với phân số một cộng T vi phân nhân s trên một cộng alpha T vi "
                   "phân nhân s.",
                   "A formula panel: OP equals K times one plus T-integral times s over T-integral "
                   "times s, times one plus T-derivative times s over one plus alpha T-derivative "
                   "times s.")


# ---------------------------------------------------------------- 6.5
def fig_6_5():
    """The lead block: a derivative followed by a first-order lag."""
    o = [_txt(18, 66, "ERR", 8.5, anchor="start")]
    o.append(_arrow(50, 62, 138, 62))
    o.append(_box(140, 47, 170, 30, "T_der · s", size=9.5))
    o.append(_arrow(310, 62, 368, 62))
    o.append(_box(370, 47, 180, 30, "1 / (1 + T_lag·s)", size=9.5))
    o.append(_arrow(550, 62, 598, 62))
    o.append(_txt(604, 66, "ra", 8.5, anchor="start"))

    o.append(_txt(18, 106, "α = T_der / T_lag = 8", 9.5, anchor="start"))
    o.append(_txt(18, 126, "khâu vi phân mạnh gấp 8 lần bộ lọc thông thấp — đủ nhanh để bắt thay "
                           "đổi, đủ chậm để không khuếch đại nhiễu", 7.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 148,
                   "Hình 6-5. Sơ đồ khối khâu LEAD dùng làm điều khiển vi phân.",
                   "Figure 6-5. Block diagram of the lead algorithm used for derivative action.",
                   "Sơ đồ nối tiếp: tín hiệu sai lệch qua khâu vi phân T vi phân nhân s, rồi qua bộ "
                   "lọc thông thấp một chia một cộng T trễ nhân s.",
                   "Series diagram: the error passes through a derivative block T-derivative times s, "
                   "then a first-order low-pass filter.")


# ---------------------------------------------------------------- 6.6
def fig_6_6():
    """Siemens S5-100V incremental form, three branches plus the previous output."""
    o = [_txt(14, 114, "XW", 9, anchor="start")]
    o.append(_line(48, 38, 48, 182))
    for y in (38, 110, 182):
        o.append(_arrow(48, y, 66, y, sw=1))

    o.append(_box(68, 24, 140, 28, "XW_K − XW_K−1", size=8))
    o.append(_box(216, 24, 50, 28, "× R", size=8.5))
    o.append(_box(274, 24, 50, 28, "× K", size=8.5))

    o.append(_box(68, 96, 140, 28, "XW_K", size=8.5))
    o.append(_box(216, 96, 50, 28, "× T_INT", size=7.5))

    o.append(_box(68, 168, 190, 28, "XW_K − 2XW_K−1 + XW_K−2", size=7.5))
    o.append(_box(266, 168, 64, 28, "× T_DER", size=7.5))

    o.append(_line(324, 38, 386, 38))
    o.append(_line(266, 110, 386, 110))
    o.append(_line(330, 182, 386, 182))
    o.append(_line(386, 38, 386, 182))
    o.append(_node(404, 110, "Σ", r=14))

    o.append(_arrow(418, 110, 440, 110))
    o.append(_box(442, 96, 104, 28, "+ OP_K−1", size=8.5))
    o.append(_arrow(546, 110, 588, 110))
    o.append(_txt(594, 114, "OP_K", 9, anchor="start"))

    o.append(_txt(68, 226, "ΔOP = K [ (XW_K − XW_K−1)·R + T_INT·XW_K + T_DER·(XW_K − 2XW_K−1 + XW_K−2) ]",
                  7.5, anchor="start", color=GREY))
    return _finish(o, 660, 244,
                   "Hình 6-6. Ví dụ dạng số gia trên Siemens S5-100V.",
                   "Figure 6-6. Example of the incremental form (Siemens S5-100V).",
                   "Sơ đồ ba nhánh tính số gia: nhánh tỉ lệ lấy hiệu hai giá trị liên tiếp nhân R, "
                   "nhánh tích phân nhân T tích phân, nhánh vi phân lấy hiệu bậc hai nhân T vi phân; "
                   "ba nhánh cộng lại rồi cộng với OP trước đó để ra OP mới.",
                   "Three increment branches: proportional takes the difference of consecutive "
                   "samples times R, integral multiplies by T-integral, derivative takes the second "
                   "difference; the three sum and add to the previous OP.")
