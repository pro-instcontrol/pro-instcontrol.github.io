# -*- coding: utf-8 -*-
"""Vector figures for Practical Process Control, Chapter 5 (stability and modes).

Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _defs, _ellipse, _f, _fig, _label, _line,
                  _path, _poly, _rect, _txt, svg)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- 5.1
def fig_5_1():
    o = [_txt(330, 18, "Điều khiển nhiệt độ lò gia nhiệt nguyên liệu", 8.6, weight="600")]
    # feed line into the heater
    o.append(_line(40, 96, 150, 96, sw=1.6))
    o.append(_arrow(24, 96, 38, 96, sw=1.2, color=BLUE))
    o.append(_txt(26, 86, "nguyên liệu vào", 6.4, color=BLUE, anchor="start"))
    # heater shell
    o.append(_rect(150, 66, 180, 76, "#eef3fb"))
    o.append(_txt(240, 110, "Lò gia nhiệt", 7.2, color=INK))
    # burner at the bottom
    o.append(_poly([(214, 142), (266, 142), (252, 160), (228, 160)], fill="#fdeccf", sw=1.0, close=True))
    o.append(_txt(272, 156, "đốt", 6.4, color=GOLD, anchor="start"))
    # fuel line with the control valve
    o.append(_line(240, 160, 240, 186, sw=1.6))
    o.append(_line(120, 186, 240, 186, sw=1.6))
    o.append(_poly([(160, 176), (180, 186), (160, 196)], fill=PAPER, sw=1.2, close=True))
    o.append(_txt(170, 172, "FV", 7.0, color=GOLD))
    o.append(_arrow(96, 186, 118, 186, sw=1.2, color=GOLD))
    o.append(_txt(92, 190, "nhiên liệu", 6.4, color=GOLD, anchor="end"))
    # outlet and temperature transmitter
    o.append(_line(330, 96, 470, 96, sw=1.6))
    o.append(_arrow(470, 96, 496, 96, sw=1.2, color=BLUE))
    o.append(_txt(474, 86, "T₂ ra", 6.6, color=BLUE, anchor="start"))
    o.append(_circle(392, 96, 11, fill=PAPER))
    o.append(_txt(392, 99, "TT", 6.4, color=GREY))
    # controller
    o.append(_box(360, 130, 110, 42, "Bộ điều khiển\nnhiệt độ TC", fill="#eef3fb", size=6.8))
    o.append(_line(392, 107, 392, 130, sw=1.0, color=GREY, dash="4 3"))
    o.append(_path("M 360 151 L 320 151 L 320 206 L 170 206 L 170 196", sw=1.2,
                   color=GOLD, dash="4 3"))
    o.append(_txt(268, 218, "tín hiệu ra điều khiển van nhiên liệu", 6.4, color=GOLD))
    return _finish(o, 660, 236,
                   "Hình 5-1 · Điều khiển nhiệt độ của một lò gia nhiệt nguyên liệu trước khi vào tháp chưng "
                   "cất. Biến được điều khiển là nhiệt độ ra T₂, biến điều khiển là vị trí van nhiên liệu.",
                   "Figure 5.1 · Temperature control of a feed heater ahead of a distillation column. The "
                   "controlled variable is the outlet temperature T2 and the manipulated variable is the "
                   "fuel valve position.")

# ---------------------------------------------------------------- 5.2
def fig_5_2():
    o = [_txt(330, 16, "Mất ổn định khi lệch pha 180° và hệ số khuếch đại lớn hơn 1", 8.6,
              weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "biên độ"))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.8, color=GREY, dash="3 3"))

    def wave(k, amp=0.20):
        def f(t):
            return 0.5 + amp * math.exp(k * t) * math.sin(2 * math.pi * 2.2 * t)
        return f

    o.append(_curve(wave(-1.5), x0, y0, W, H, n=361, color=GREEN, sw=1.5))
    o.append(_curve(wave(0.0, 0.16), x0, y0, W, H, n=361, color=GREY, sw=1.5))
    o.append(_curve(wave(1.6, 0.10), x0, y0, W, H, n=361, color=RED, sw=1.8))
    o.append(_legend(x0 + W - 190, y0 + 6,
                     [(GREEN, "K vòng &lt; 1: tắt dần", ""),
                      (GREY, "K vòng = 1: dao động đều", ""),
                      (RED, "K vòng &gt; 1: tăng dần", "")], w=188))
    return _finish(o, 660, 186,
                   "Hình 5-2 · Mất ổn định tăng dần khi tín hiệu có độ lệch pha 180° và hệ số khuếch đại vòng "
                   "lớn hơn 1. Với cùng độ lệch pha, K vòng nhỏ hơn 1 cho dao động tắt dần, bằng 1 cho dao "
                   "động đều.",
                   "Figure 5.2 · Increasing instability when a signal returns with 180° of phase shift and a "
                   "loop gain above 1. At the same phase shift, a loop gain below 1 decays and a gain of "
                   "exactly 1 sustains a steady oscillation.")

# ---------------------------------------------------------------- 5.3
def fig_5_3():
    o = [_txt(330, 16, "Quan hệ giữa dải tỉ lệ và hành trình van", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "PV (% dải đo)", "MV (% hành trình)",
                   xt=[(0, "0"), (0.4, "40"), (0.5, "50"), (0.6, "60"), (1, "100")],
                   yt=[(0, "0"), (0.4, "40"), (0.6, "60"), (1, "100")]))
    # MV = K (PV - PV0) + 50 for each band; the middle of the band sits at MV = 50
    def band(k):
        # None outside the axes, so the steep line is clipped at the frame
        def f(v):
            y = 0.5 + k * (v - 0.5)
            return None if (y < -0.01 or y > 1.01) else y
        return f

    o.append(_curve(band(5.0), x0, y0, W, H, n=241, color=GOLD, sw=1.8))
    o.append(_curve(band(1.0), x0, y0, W, H, n=61, color=INK, sw=1.8))
    o.append(_curve(band(0.2), x0, y0, W, H, n=61, color=GREY, sw=1.8))
    # the legend goes in the empty upper-left corner: the lower right is crossed
    # by the K = 0,2 line and the upper right by the K = 1 line
    o.append(_legend(x0 + 12, y0 + 6,
                     [(GOLD, "PB 20 % (K = 5)", ""),
                      (INK, "PB 100 % (K = 1)", ""),
                      (GREY, "PB 500 % (K = 0,2)", "")], w=176))
    return _finish(o, 660, 186,
                   "Hình 5-3 · Quan hệ giữa dải tỉ lệ và hành trình van. Với PB = 20 % (K = 5), PV đi từ 40 % "
                   "tới 60 % đã đưa van hết hành trình; với PB = 500 % (K = 0,2), PV đi hết dải cũng chỉ làm "
                   "van dịch từ 40 % lên 60 %.",
                   "Figure 5.3 · Proportional band against valve travel. At PB = 20 % (K = 5) a PV move from "
                   "40 % to 60 % takes the valve through its whole stroke; at PB = 500 % (K = 0.2) the full "
                   "PV range moves the valve only from 40 % to 60 %.")


# ---------------------------------------------------------------- 5.4
def fig_5_4():
    o = [_txt(330, 16, "Độ lệch pha do tác động tích phân", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "góc (độ)", "biên độ"))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.8, color=GREY, dash="3 3"))
    o.append(_curve(lambda t: 0.5 + 0.30 * math.sin(2 * math.pi * t), x0, y0, W, H,
                    n=241, xr=(0, 1.5), color=INK, sw=1.7))
    o.append(_curve(lambda t: 0.5 - 0.30 * math.cos(2 * math.pi * t), x0, y0, W, H,
                    n=241, xr=(0, 1.5), color=GOLD, sw=1.7))
    # mark one peak and the lagging peak
    o.append(_line(x0 + 0.25 / 1.5 * W, y0 + H * 0.16, x0 + 0.25 / 1.5 * W, y0 + H, sw=0.8,
                   color=INK, dash="3 3"))
    o.append(_line(x0 + 0.5 / 1.5 * W, y0 + H * 0.16, x0 + 0.5 / 1.5 * W, y0 + H, sw=0.8,
                   color=GOLD, dash="3 3"))
    o.append(_arrow(x0 + 0.25 / 1.5 * W, y0 + 16, x0 + 0.5 / 1.5 * W, y0 + 16, sw=0.9, color=BLUE))
    o.append(_arrow(x0 + 0.5 / 1.5 * W, y0 + 16, x0 + 0.25 / 1.5 * W, y0 + 16, sw=0.9, color=BLUE))
    o.append(_txt(x0 + 0.375 / 1.5 * W, y0 + 9, "lệch 90°", 6.8, color=BLUE))
    o.append(_legend_h(x0, y0 + H + 16,
                       [(INK, "tín hiệu vào", ""), (GOLD, "tích phân", "")]))
    return _finish(o, 660, 192,
                   "Hình 5-4 · Độ lệch pha của phép tích phân trên một sóng sin. Tác động tích phân luôn làm "
                   "chậm pha 90°, và độ trễ này có tác dụng làm mất ổn định vòng kín.",
                   "Figure 5.4 · The phase shift introduced by integration of a sine wave. Integral action "
                   "always lags by 90°, and that lag is destabilising in a closed loop.")

# ---------------------------------------------------------------- 5.5
def fig_5_5():
    o = [_txt(330, 16, "Quan hệ tích phân và đầu ra khi sai lệch không đổi", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "OP"))
    o.append(_curve(lambda t: 0.06 + 0.62 * t, x0, y0, W, H, n=61, color=GOLD, sw=1.9))
    for i in range(1, 4):
        x = x0 + i / 4.0 * W
        o.append(_line(x, y0 + H, x, y0 + H - 0.06 * H, sw=0.8, color=GREY))
        o.append(_txt(x, y0 + H + 12, "T", 6.8, color=GREY))
    o.append(_txt(x0 + 4, y0 + H + 12, "0", 6.8, color=GREY))
    o.append(_label(x0 + W - 8, y0 + 26, "mỗi T: OP tăng thêm ERR × K", 6.8, GOLD, anchor="end"))
    return _finish(o, 660, 186,
                   "Hình 5-5 · Quan hệ tích phân và đầu ra khi sai lệch giữ nguyên: sau mỗi hằng số thời gian "
                   "tích phân T, đầu ra lại tăng thêm một lượng ERR × K, tạo thành một đường dốc.",
                   "Figure 5.5 · Integral relationships with a constant error: at the completion of each "
                   "integral time constant T the output rises by another ERR × K, producing a ramp.")

# ---------------------------------------------------------------- 5.6
def fig_5_6():
    o = [_txt(330, 16, "Tác động tích phân trong thực tế", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "OP / PV"))
    o.append(_curve(lambda t: 0.06 + 0.80 * (1 - math.exp(-3.0 * t)), x0, y0, W, H,
                    n=241, color=GOLD, sw=1.9))
    o.append(_curve(lambda t: 1.0 - 0.94 * math.exp(-3.0 * t), x0, y0, W, H,
                    n=241, color=INK, sw=1.5, dash="5 4"))
    o.append(_legend_h(x0, y0 + H + 16,
                       [(INK, "PV tiến về SP", "5 4"), (GOLD, "OP tích phân", "")]))
    # the annotation sits in the empty lower band: at the left it would land on
    # the start of the curve it describes
    o.append(_label(x0 + 0.40 * W, y0 + H - 12, "ERR giảm dần nên đường dốc bị bẻ cong", 6.8, GREY,
                    anchor="start"))
    return _finish(o, 660, 192,
                   "Hình 5-6 · Tác động tích phân trong thực tế: khi OP tăng và đi qua quá trình, PV tiến về "
                   "SP, sai lệch giảm, nên tốc độ thay đổi giảm theo — đường dốc biến thành đường cong bậc "
                   "một quen thuộc.",
                   "Figure 5.6 · Integral action in practice: as the output rises and passes through the "
                   "process, the PV moves towards the set point, the error shrinks and the rate of change "
                   "falls, turning the ramp into the familiar first-order curve.")

# ---------------------------------------------------------------- 5.7
def fig_5_7():
    o = [_txt(330, 16, "Độ vượt pha do phép vi phân", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "góc (độ)", "biên độ"))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.8, color=GREY, dash="3 3"))
    o.append(_curve(lambda t: 0.5 + 0.30 * math.sin(2 * math.pi * t), x0, y0, W, H,
                    n=241, xr=(0, 1.5), color=INK, sw=1.7))
    o.append(_curve(lambda t: 0.5 + 0.30 * math.cos(2 * math.pi * t), x0, y0, W, H,
                    n=241, xr=(0, 1.5), color=GOLD, sw=1.7))
    o.append(_line(x0 + 0.25 / 1.5 * W, y0 + H * 0.16, x0 + 0.25 / 1.5 * W, y0 + H, sw=0.8,
                   color=INK, dash="3 3"))
    o.append(_line(x0, y0 + H * 0.16, x0, y0 + H, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_arrow(x0, y0 + 16, x0 + 0.25 / 1.5 * W, y0 + 16, sw=0.9, color=BLUE))
    o.append(_arrow(x0 + 0.25 / 1.5 * W, y0 + 16, x0, y0 + 16, sw=0.9, color=BLUE))
    o.append(_txt(x0 + 0.125 / 1.5 * W, y0 + 9, "vượt 90°", 6.8, color=BLUE))
    o.append(_legend_h(x0, y0 + H + 16,
                       [(INK, "tín hiệu vào", ""), (GOLD, "vi phân", "")]))
    return _finish(o, 660, 192,
                   "Hình 5-7 · Độ vượt pha của phép vi phân trên một sóng sin. Tác động vi phân đẩy pha lên "
                   "trước 90°, và có thể bù lại một phần hoặc toàn bộ độ trễ pha đang có.",
                   "Figure 5.7 · The phase lead introduced by differentiation of a sine wave. Derivative "
                   "action advances the phase by 90° and can cancel part or all of an existing lag.")

# ---------------------------------------------------------------- 5.8
def fig_5_8():
    o = [_txt(330, 16, "Quan hệ vi phân và đầu ra khi sai lệch thay đổi bậc thang", 8.6,
              weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "OP"))
    t0 = 0.16

    def op(t):
        if t < t0:
            return 0.05
        return 0.05 + 0.80 * math.exp(-(t - t0) / 0.16)

    o.append(_curve(op, x0, y0, W, H, n=241, xr=(0, 1), color=GOLD, sw=1.9))
    o.append(_line(x0 + t0 * W, y0 + H, x0 + t0 * W, y0 + H - 0.85 * H, sw=0.8, color=GREY,
                   dash="3 3"))
    o.append(_txt(x0 + t0 * W - 6, y0 + H - 0.88 * H, "bậc thang ở ERR", 6.6, color=GREY,
                  anchor="end"))
    for i, frac in enumerate((0.632, 0.864)):
        yy = y0 + H - (0.05 + 0.80 * frac) * H
        o.append(_line(x0 + t0 * W, yy, x0 + (t0 + 0.16 * (i + 1)) * W, yy, sw=0.7, color=BLUE,
                       dash="2 3"))
        o.append(_txt(x0 + (t0 + 0.16 * (i + 1)) * W + 4, yy + 3, "%d %%" % (63 if i == 0 else 86),
                      6.2, color=BLUE, anchor="start"))
    return _finish(o, 660, 186,
                   "Hình 5-8 · Quan hệ vi phân và đầu ra khi ERR thay đổi bậc thang: đầu ra nhảy ngay lên một "
                   "giá trị lớn rồi giảm dần, mỗi hằng số thời gian vi phân giảm 63,2 % quãng đường còn lại.",
                   "Figure 5.8 · Derivative relationships for a step change in the error: the output jumps "
                   "immediately to a large value and then decays, losing 63.2 % of the remaining distance in "
                   "each derivative time constant.")

# ---------------------------------------------------------------- 5.9
def fig_5_9():
    o = [_txt(330, 16, "Vi phân không có chức năng khi đứng một mình", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "ERR / OP"))
    t0 = 0.2
    o.append(_poly([(x0, y0 + H - 0.10 * H), (x0 + t0 * W, y0 + H - 0.10 * H),
                    (x0 + t0 * W, y0 + H - 0.45 * H), (x0 + W, y0 + H - 0.45 * H)],
                   color=INK, sw=1.6, dash="5 4"))

    def d(t):
        if t < t0:
            return 0.05
        return 0.05 + 0.42 * math.exp(-(t - t0) / 0.10)

    o.append(_curve(d, x0, y0, W, H, n=241, xr=(0, 1), color=GOLD, sw=1.8))
    o.append(_legend_h(x0, y0 + H + 16,
                       [(INK, "ERR (bậc thang)", "5 4"), (GOLD, "OP vi phân", "")]))
    o.append(_label(x0 + 0.55 * W, y0 + H - 0.12 * H, "OP trở về 0: không giữ được giá trị hiệu chỉnh",
                    6.8, RED, anchor="start"))
    return _finish(o, 660, 192,
                   "Hình 5-9 · Vi phân không có chức năng khi đứng một mình: sau khi sai lệch đã ổn định, đầu "
                   "ra vi phân trở về 0 và không còn giữ được bất kỳ giá trị hiệu chỉnh nào.",
                   "Figure 5.9 · Derivative control has no functionality on its own: once the error has "
                   "settled, the derivative output returns to zero and holds no correction at all.")

# ---------------------------------------------------------------- 5.10
def fig_5_10():
    o = [_txt(330, 18, "Sơ đồ khối bộ điều khiển PID lý tưởng", 8.6, weight="600")]
    cy = 100
    o.append(_txt(24, cy + 4, "SP", 8.0, color=GREY, anchor="start"))
    o.append(_arrow(46, cy, 72, cy, sw=1.2))
    o.append(_circle(86, cy, 13))
    o.append(_txt(86, cy - 10, "+", 7.2))
    o.append(_txt(78, cy + 12, "−", 8.4))
    # one bus feeds all three branches
    o.append(_line(99, cy, 108, cy, sw=1.1))
    o.append(_line(108, 57, 108, 143, sw=1.1))
    for yy in (57, 100, 143):
        o.append(_arrow(108, yy, 122, yy, sw=1.1))
    o.append(_box(122, 40, 96, 34, "P\nK·ERR", fill="#eef3fb", size=7.2))
    o.append(_box(122, 83, 96, 34, "I\n1/T<sub>I</sub>∫ERR", fill="#fdeccf", size=7.2))
    o.append(_box(122, 126, 96, 34, "D\nT<sub>D</sub>·d/dt", fill="#e6f0e6", size=7.2))
    # and one bus collects them again
    for yy in (57, 100, 143):
        o.append(_line(218, yy, 238, yy, sw=1.1))
    o.append(_line(238, 57, 238, 143, sw=1.1))
    o.append(_arrow(238, cy, 249, cy, sw=1.1))
    o.append(_circle(262, cy, 13))
    o.append(_txt(262, cy + 4, "Σ", 8.0))
    o.append(_arrow(275, cy, 300, cy, sw=1.2))
    o.append(_box(300, 78, 104, 44, "Van + quá\ntrình", fill="#eef3fb", size=6.8))
    o.append(_arrow(404, cy, 440, cy, sw=1.2))
    o.append(_txt(444, cy + 4, "PV", 7.4, color=GREY, anchor="start"))
    # feedback runs below the whole branch stack
    o.append(_arrow(352, 122, 352, 200, sw=1.1))
    o.append(_line(352, 200, 86, 200, sw=1.1))
    o.append(_arrow(86, 200, 86, 113, sw=1.1))
    o.append(_txt(360, 214, "ba nhánh làm việc song song trên cùng một sai lệch", 6.6, color=GREY))
    return _finish(o, 660, 232,
                   "Hình 5-10 · Sơ đồ khối của một bộ điều khiển PID lý tưởng: ba nhánh P, I, D cùng nhận "
                   "một sai lệch và cộng lại ở đầu ra.",
                   "Figure 5.10 · Block diagram of an ideal PID controller: the P, I and D branches all act "
                   "on the same error and are summed at the output.")


# ---------------------------------------------------------------- 5.11
def fig_5_11():
    o = [_txt(330, 16, "Đáp ứng điển hình của bộ điều khiển P, PI và PID", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "PV"))
    t0 = 0.12
    SP = 0.80
    ysp = y0 + H * (1 - SP)
    # the set point is drawn through the same value mapping as the curves, so
    # "reaches the set point" means exactly that
    o.append(_curve(lambda t: SP, x0, y0, W, H, n=2, xr=(0, 1), color=GREY, dash="5 4", sw=1.0))
    o.append(_txt(x0 + W - 4, ysp - 6, "SP", 6.8, color=GREY, anchor="end"))

    def p_only(t):
        if t < t0:
            return 0.20
        return 0.20 + 0.45 * (1 - math.exp(-(t - t0) / 0.30))

    def pi(t):
        if t < t0:
            return 0.20
        return 0.20 + 0.60 * (1 - math.exp(-(t - t0) / 0.16))

    def pid(t):
        if t < t0:
            return 0.20
        u = t - t0
        return 0.20 + 0.60 * (1 - math.exp(-u / 0.10) * math.cos(4.4 * u))

    o.append(_curve(p_only, x0, y0, W, H, n=241, xr=(0, 1), color=GREY, sw=1.5))
    o.append(_curve(pi, x0, y0, W, H, n=241, xr=(0, 1), color=GOLD, sw=1.5))
    o.append(_curve(pid, x0, y0, W, H, n=361, xr=(0, 1), color=INK, sw=1.8))
    # the standing offset: the gap between the P plateau and the set point,
    # dimensioned at the right where both are flat and nothing else crosses
    ypl = y0 + H * (1 - 0.65)
    xd = x0 + 0.74 * W
    o.append(_arrow(xd, ypl, xd, ysp + 2, sw=0.9, color=BLUE))
    o.append(_arrow(xd, ysp, xd, ypl - 2, sw=0.9, color=BLUE))
    o.append(_txt(xd + 6, ysp - 5, "sai lệch tĩnh", 6.4, color=BLUE, anchor="start"))
    o.append(_legend(x0 + W - 132, y0 + H - 44,
                     [(GREY, "P", ""), (GOLD, "PI", ""), (INK, "PID", "")], w=130))
    return _finish(o, 660, 186,
                   "Hình 5-11 · Đáp ứng điển hình của bộ điều khiển P, PI và PID với cùng một bậc thang ở "
                   "điểm đặt: P dừng lại ở một sai lệch tĩnh, PI khử được sai lệch nhưng chậm, PID nhanh hơn "
                   "nhờ tác động vi phân.",
                   "Figure 5.11 · Typical P, PI and PID responses to the same set-point step: P settles with "
                   "a standing offset, PI removes the offset but slowly, and PID gets there faster because of "
                   "the derivative term.")

FIGURES = [fig_5_1, fig_5_2, fig_5_3, fig_5_4, fig_5_5, fig_5_6, fig_5_7, fig_5_8,
           fig_5_9, fig_5_10, fig_5_11]
