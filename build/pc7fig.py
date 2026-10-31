# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 7 — Real and Ideal P.I.D. Controllers."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- 7.1
def fig_7_1():
    """The ideal (non-interactive) controller: three terms that add."""
    o = [_node(88, 96, "Σ", r=14)]
    o.append(_txt(14, 100, "SP", 8.5, anchor="start"))
    o.append(_arrow(42, 96, 71, 96))
    o.append(_txt(14, 188, "PV", 8.5, anchor="start"))
    o.append(_arrow(88, 184, 88, 113))
    o.append(_txt(72, 172, "−", 12, color=INK))
    o.append(_txt(108, 88, "ERR", 7.5, anchor="start", color=GREY))

    o.append(_line(102, 96, 160, 96))
    o.append(_line(160, 54, 160, 138))
    for y in (54, 96, 138):
        o.append(_arrow(160, y, 168, y, sw=1))

    o.append(_box(170, 37, 186, 34, "P:   K_c", size=8.5))
    o.append(_box(170, 79, 186, 34, "I:   K_c / (T_int·s)", size=8.5))
    o.append(_box(170, 121, 186, 34, "D:   K_c · T_der·s", size=8.5))

    for y in (54, 96, 138):
        o.append(_line(356, y, 388, y))
    o.append(_line(388, 54, 388, 138))
    o.append(_node(408, 96, "Σ", r=14))
    o.append(_arrow(422, 96, 574, 96))
    o.append(_txt(580, 100, "OP", 8.5, anchor="start"))

    o.append(_txt(170, 178, "ba khâu độc lập — xem được riêng từng khâu", 7.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 200,
                   "Hình 7-1. Bộ điều khiển PID lý tưởng (không tương tác): ba khâu P, I, D tính độc "
                   "lập rồi cộng lại.",
                   "Figure 7-1. The ideal (non-interactive) PID controller: three independent terms "
                   "that are summed.",
                   "Sơ đồ khối: sai lệch ERR rẽ vào ba nhánh song song P, I, D tính riêng, ba đầu ra "
                   "cộng lại thành OP.",
                   "Block diagram: the error fans into three parallel P, I and D branches computed "
                   "separately; their outputs sum to OP.")


# ---------------------------------------------------------------- 7.2
def fig_7_2():
    """The ideal algorithm, as the source prints it."""
    o = [_rect(24, 20, 612, 104, "#fbfaf6", sw=0.8, stroke="#ddd7c8")]
    o.append(_txt(330, 52, "OP  =  Gain · (D-Control + I-Control + P-Control)", 11.5))
    o.append(_txt(330, 82, "OP  =  K_c · (1 + 1/(T_int·s) + T_der·s) · ERR", 11.5))
    o.append(_txt(330, 108, "không tương tác: đạo hàm là vi phân lý tưởng, không lọc", 8, color=GREY))
    return _finish(o, 660, 140,
                   "Hình 7-2. Công thức bộ điều khiển PID lý tưởng.",
                   "Figure 7-2. The ideal PID algorithm.",
                   "Khung công thức: OP bằng Gain nhân tổng ba khâu D, I, P; viết đầy đủ là K_c nhân "
                   "một cộng một chia T tích phân nhân s, cộng T vi phân nhân s, tất cả nhân sai lệch.",
                   "A formula panel: OP equals gain times the sum of the D, I and P terms; written out, "
                   "K-sub-c times one plus one over T-integral times s plus T-derivative times s, times "
                   "the error.")


# ---------------------------------------------------------------- 7.3
def fig_7_3():
    """The real (interactive) controller: PI in series with a lead."""
    o = [_node(78, 92, "Σ", r=14)]
    o.append(_txt(14, 96, "SP", 8.5, anchor="start"))
    o.append(_arrow(42, 92, 61, 92))
    o.append(_txt(14, 184, "PV", 8.5, anchor="start"))
    o.append(_arrow(78, 180, 78, 109))
    o.append(_txt(62, 168, "−", 12, color=INK))

    o.append(_arrow(92, 92, 134, 92))
    o.append(_box(136, 76, 196, 32, "PI:  K_c · (1 + 1/(T_int·s))", size=7.8))
    o.append(_arrow(332, 92, 368, 92))
    o.append(_box(370, 76, 198, 32, "LEAD:  (1 + T_der·s)/(1 + α·T_der·s)", size=7.4))
    o.append(_arrow(568, 92, 606, 92))
    o.append(_txt(612, 96, "OP", 8.5, anchor="start"))

    o.append(_txt(136, 138, "mắc nối tiếp — đầu ra không phải tổng của ba khâu độc lập", 7.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 168,
                   "Hình 7-3. Bộ điều khiển PID thực (tương tác): khâu PI mắc nối tiếp với khâu LEAD.",
                   "Figure 7-3. The real (interactive) PID controller: PI in series with a lead.",
                   "Sơ đồ khối: sai lệch qua khâu PI rồi qua khâu lead; hai khối nối tiếp nhau chứ "
                   "không song song.",
                   "Block diagram: the error passes through a PI block and then a lead block; the two "
                   "are in series, not parallel.")


# ---------------------------------------------------------------- 7.4
def fig_7_4():
    """The real algorithm, as the source prints it."""
    o = [_rect(24, 20, 612, 116, "#fbfaf6", sw=0.8, stroke="#ddd7c8")]
    o.append(_txt(330, 50, "OP  =  K_c ·", 12.5))
    o.append(_txt(330, 76, "(T_int·s + 1) / (T_int·s)", 12.5))
    o.append(_txt(330, 102, "·  (T_der·s + 1) / (α·T_der·s + 1)", 12.5))
    o.append(_txt(330, 124, "=  K_c · PI · LEAD", 8.5, color=GREY))
    return _finish(o, 660, 152,
                   "Hình 7-4. Công thức bộ điều khiển PID thực (tương tác).",
                   "Figure 7-4. The real (interactive) PID algorithm.",
                   "Khung công thức: OP bằng K_c nhân phân số T tích phân nhân s cộng một trên T tích "
                   "phân nhân s, nhân với phân số T vi phân nhân s cộng một trên alpha T vi phân nhân "
                   "s cộng một.",
                   "A formula panel: OP equals K-sub-c times T-integral times s plus one over "
                   "T-integral times s, times T-derivative times s plus one over alpha T-derivative "
                   "times s plus one.")


# ---------------------------------------------------------------- 7.5
def fig_7_5():
    """Lead = derivative followed by a first-order lag."""
    o = [_txt(18, 62, "ERR", 8.5, anchor="start")]
    o.append(_arrow(50, 58, 140, 58))
    o.append(_box(142, 43, 168, 30, "T_der · s", size=9.5))
    o.append(_arrow(310, 58, 368, 58))
    o.append(_box(370, 43, 178, 30, "1 / (1 + T_lag·s)", size=9.5))
    o.append(_arrow(548, 58, 596, 58))
    o.append(_txt(602, 62, "ra", 8.5, anchor="start"))

    o.append(_txt(18, 102, "α = T_der / T_lag", 9.5, anchor="start"))
    o.append(_txt(18, 122, "trích từ Chương 6: khâu vi phân mạnh gấp α lần bộ lọc đi kèm", 7.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 142,
                   "Hình 7-5. Sơ đồ khối khâu LEAD dùng làm điều khiển vi phân.",
                   "Figure 7-5. Block diagram of the lead used for derivative action.",
                   "Sơ đồ nối tiếp: tín hiệu qua khâu T vi phân nhân s, rồi qua bộ lọc thông thấp một "
                   "chia một cộng T trễ nhân s.",
                   "Series diagram: the signal passes through T-derivative times s, then a first-order "
                   "low-pass filter.")


# ---------------------------------------------------------------- 7.6
def fig_7_6():
    """Why the lead stops differentiating: gain against frequency, log-log."""
    x0, y0, W, H = 74, 46, 512, 150
    Td, a = 10.0, 8.0
    Tl = Td / a

    def ideal(x):
        return x                                   # |jω| = ω, on a log10 axis

    def lead(x):
        w = 10.0 ** x
        return math.log10(Td * w / math.sqrt(1.0 + (Tl * w) ** 2))

    o = [_axes(x0, y0, W, H, "", "",
               xt=[(0, "0,01"), (0.25, "0,1"), (0.5, "1"), (0.75, "10"), (1, "100")],
               yt=[(0, "0,01"), (0.3, "0,1"), (0.6, "1"), (0.9, "10")])]
    o.append(_txt(x0 + W, y0 + H + 26, "tần số ω (rad/s)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 + 5, y0 - 10, "hệ số khuếch đại", 7.6, color=GREY))
    # y axis spans 10^-2 … 10^1.3
    lo, hi = -2.0, 1.3

    def ymap(v):
        return y0 + H - (v - lo) / (hi - lo) * H

    o.append(_curve(ideal, x0, y0, W, H, n=201, xr=(-2, 2), yr=(lo, hi), color=GREY, sw=1.3,
                    dash="4 3"))
    o.append(_curve(lead, x0, y0, W, H, n=241, xr=(-2, 2), yr=(lo, hi), color=BLUE, sw=2.0))

    # the plateau at alpha
    ya = ymap(math.log10(a))
    o.append(_line(x0 + W * 0.72, ya, x0 + W, ya, sw=0.8, dash="2 3", color=RED))
    o.append(_txt(x0 + W - 4, ya - 7, "α = 8  (≈ 18 dB)", 7.5, anchor="end", color=RED))

    o.append(_txt(x0 + 12, y0 + 18, "vi phân lý tưởng", 7.5, anchor="start", color=GREY))
    o.append(_txt(x0 + 12, y0 + 30, "20 dB / thập kỷ", 7.5, anchor="start", color=GREY))
    o.append(_txt(x0 + W * 0.55, ymap(-0.42), "khâu lead", 8.5, anchor="start", color=BLUE))
    o.append(_txt(x0 + W * 0.55, ymap(-0.72), "ngừng vi phân ở tần số cao", 7,
                  anchor="start", color=BLUE))
    return _finish(o, 660, 236,
                   "Hình 7-6. Đáp ứng tần số của khâu vi phân lý tưởng và của khâu lead: lead dừng "
                   "khuếch đại ở α.",
                   "Figure 7-6. Frequency response of ideal differentiation and of the lead: the lead "
                   "stops amplifying at α.",
                   "Đồ thị log-log: đường nét đứt là vi phân lý tưởng tăng đều 20 dB mỗi thập kỷ; "
                   "đường liền là khâu lead, ban đầu bám theo rồi nằm ngang ở mức alpha bằng 8.",
                   "Log-log plot: the dashed line is ideal differentiation rising 20 dB per decade; "
                   "the solid lead follows it at first, then flattens at alpha equal to eight.")


# ---------------------------------------------------------------- 7.7
def fig_7_7():
    """Noise and instability look alike on a trend and are not the same problem."""
    W, H = 246, 118

    def noise(t):
        return 0.5 + 0.055 * math.sin(2 * math.pi * 7.3 * t) + \
            0.035 * math.sin(2 * math.pi * 13.1 * t + 1.1) + \
            0.022 * math.sin(2 * math.pi * 21.7 * t + 2.4)

    def unstable(t):
        return 0.5 + 0.075 * math.exp(0.42 * t) * math.sin(2 * math.pi * 1.15 * t)

    o = []
    for i, (x0, fn, title, col) in enumerate([
            (54, noise, "nhiễu (noise)", GREY),
            (368, unstable, "mất ổn định (instability)", RED)]):
        o.append(_txt(x0 + W / 2.0, 24, title, 8.5, color=INK))
        o.append(_axes(x0, 36, W, H, "thời gian", "PV",
                       xt=[(0, "0"), (0.5, "t"), (1, "")],
                       yt=[(0, ""), (0.5, "50"), (1, "")]))
        o.append(_line(x0, 36 + H * 0.5, x0 + W, 36 + H * 0.5, sw=0.7, dash="3 3", color=GREY))
        o.append(_curve(fn, x0, 36, W, H, n=321, xr=(0, 1), yr=(0.2, 0.8), color=col, sw=1.5))

    o.append(_txt(54 + W / 2.0, 186, "biên độ không đổi · tần số cao · do dây và cảm biến", 7.2,
                  color=GREY))
    o.append(_txt(368 + W / 2.0, 186, "biên độ tăng dần · tần số thấp · do vòng kín", 7.2,
                  color=GREY))
    o.append(_txt(330, 212, "cùng nhìn giống nhau trên trend, nhưng phải xử lý khác nhau: "
                            "lọc cho nhiễu, chỉnh định cho mất ổn định", 7.6, color=INK))
    return _finish(o, 660, 228,
                   "Hình 7-7. Hai hiện tượng trông giống nhau trên trend nhưng khác bản chất: nhiễu và "
                   "mất ổn định.",
                   "Figure 7-7. Two phenomena that look alike on a trend but are different problems: "
                   "noise and instability.",
                   "Hai đồ thị cạnh nhau: bên trái là tín hiệu nhiễu biên độ không đổi tần số cao; bên "
                   "phải là dao động có biên độ tăng dần, tức vòng kín đã mất ổn định.",
                   "Two panels side by side: on the left a high-frequency signal of constant "
                   "amplitude; on the right an oscillation whose amplitude grows, meaning the loop has "
                   "gone unstable.")


# ---------------------------------------------------------------- 7.8
def fig_7_8():
    """The PV filter buys noise rejection with lag."""
    x0, y0, W, H = 66, 44, 520, 132
    o = [_axes(x0, y0, W, H, "", "PV sau lọc",
               xt=[(0, "0"), (0.25, "2"), (0.5, "4"), (0.75, "6"), (1, "8")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_txt(x0 + W, y0 + H + 26, "thời gian (s)", 7.4, anchor="end", color=GREY))
    o.append(_line(x0, y0, x0 + W, y0, sw=1.0, dash="4 3", color=INK))
    o.append(_txt(x0 + W - 4, y0 - 6, "bậc thang PV", 7, anchor="end", color=GREY))
    for T, col, lab in ((0.35, BLUE, "T_f = 0,35 s"),
                        (1.2, GOLD, "T_f = 1,2 s"),
                        (3.0, RED, "T_f = 3 s")):
        o.append(_curve(lambda t, T=T: 1.0 - math.exp(-t / T), x0, y0, W, H, n=201,
                        xr=(0, 8), yr=(0, 1), color=col, sw=1.8))
    o.append(_legend_h(x0 + 8, y0 + H + 44,
                       [(BLUE, "lọc nhẹ  T_f = 0,35 s", ""),
                        (GOLD, "vừa  T_f = 1,2 s", ""),
                        (RED, "lọc mạnh  T_f = 3 s", "")], gap=30))
    o.append(_txt(x0 + W - 4, y0 + H * 0.62, "lọc mạnh: nhiễu ít, nhưng thêm trễ", 7.5,
                  anchor="end", color=GREY))
    return _finish(o, 660, 246,
                   "Hình 7-8. Bộ lọc biến đoạn nhiễu bằng thời gian trễ: ba hằng số lọc khác nhau cho "
                   "ba mức trễ khác nhau.",
                   "Figure 7-8. The PV filter trades noise for lag: three filter time constants give "
                   "three different lags.",
                   "Ba đường đáp ứng bậc thang với hằng số lọc 0,35 giây, 1,2 giây và 3 giây; hằng số "
                   "càng lớn đường càng bò chậm, tức trễ càng nhiều.",
                   "Three step responses with filter time constants of 0.35, 1.2 and 3 seconds; the "
                   "larger the constant the slower the rise, that is the more lag.")


# ---------------------------------------------------------------- 7.9
def fig_7_9():
    """The KENT K90 discrete implementation."""
    o = [_txt(24, 34, "PB = dải tỉ lệ (%),  IAT và DAT tính bằng giây,  quét tính bằng giây", 8,
              anchor="start", color=GREY)]

    o.append(_box(24, 50, 190, 40, "K1 = 100 / PB", size=9))
    o.append(_box(24, 100, 190, 40, "K2 = (100/PB) · (quét / IAT)", size=7.8))
    o.append(_box(24, 150, 190, 40, "K3 = (100/PB) · (DAT / quét)", size=7.8))

    o.append(_line(214, 70, 250, 70))
    o.append(_line(214, 120, 250, 120))
    o.append(_line(214, 170, 250, 170))
    o.append(_line(250, 70, 250, 170))
    o.append(_node(268, 120, "Σ", r=14))
    o.append(_arrow(282, 120, 320, 120))
    o.append(_txt(326, 124, "kết quả", 9, anchor="start"))

    o.append(_txt(24, 208, "P  =  K1 · ERR", 8.5, anchor="start"))
    o.append(_txt(150, 208, "I  =  K2 · Σ ERR · quét", 8.5, anchor="start"))
    o.append(_txt(340, 208, "D  =  K3 · (PV_K − PV_K−1)", 8.5, anchor="start"))

    o.append(_txt(24, 236, "OP = (100/PB) · [ ERR + (1/IAT)∫ERR dt + DAT · dPV/dt ]", 9.5,
                  anchor="start", color=INK))
    return _finish(o, 660, 250,
                   "Hình 7-9. Ví dụ bộ điều khiển KENT K90: ba hệ số rời rạc K1, K2, K3 tính từ dải tỉ "
                   "lệ PB và chu kỳ quét.",
                   "Figure 7-9. The KENT K90 example: three discrete gains K1, K2, K3 derived from the "
                   "proportional band and the scan period.",
                   "Sơ đồ: ba hệ số K1, K2, K3 tính từ dải tỉ lệ và chu kỳ quét, mỗi hệ số nhân một "
                   "thành phần P, I, D rồi cộng lại; bên dưới là công thức gộp.",
                   "Diagram: three gains K1, K2, K3 derived from the proportional band and scan "
                   "period, each scaling a P, I or D component before they sum; the combined formula "
                   "is printed below.")
