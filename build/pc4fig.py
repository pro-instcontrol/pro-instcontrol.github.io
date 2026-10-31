# -*- coding: utf-8 -*-
"""Vector figures for Practical Process Control, Chapter 4 (control fundamentals).

Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
Every trace is computed from the function it illustrates, not sketched.
"""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _defs, _ellipse, _f, _fig, _label, _line,
                  _path, _poly, _rect, _txt, svg)
from pcfig import _finish, _legend, _spring


# ---------------------------------------------------------------- 4.1
def fig_4_1():
    o = [_txt(330, 16, "Bộ điều khiển hai vị trí với đầu vào hình sin", 8.6, weight="600")]
    x0, y0, W, H = 84, 40, 500, 120
    o.append(_axes(x0, y0, W, H, "thời gian", "% thang đo",
                   xt=[(0, "0"), (0.5, "1"), (1, "2")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    # set point and the measured variable
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=1.0, color=GREY, dash="5 4"))
    o.append(_curve(lambda t: 0.5 + 0.34 * math.sin(2 * math.pi * t), x0, y0, W, H,
                    n=241, xr=(0, 2), color=BLUE, sw=1.9))
    # two-position output: on below the set point, off above it
    pts = []
    n = 480
    for i in range(n + 1):
        t = 2.0 * i / n
        v = 0.5 + 0.34 * math.sin(2 * math.pi * t)
        pts.append((x0 + t / 2.0 * W, y0 + H - (0.13 if v < 0.5 else 0.0) * H))
    o.append(_poly(pts, color=GOLD, sw=1.6))
    o.append(_txt(x0 + 6, y0 + H / 2.0 - 5, "SP", 6.8, color=GREY, anchor="start"))
    o.append(_legend(x0 + W - 168, y0 + 6,
                     [(BLUE, "PV đo được", ""),
                      (GOLD, "OP: đóng / ngắt", "")], w=166))
    return _finish(o, 660, 186,
                   "Hình 4-1 · Đáp ứng của bộ điều khiển hai vị trí với đầu vào hình sin. Đầu ra chỉ có "
                   "hai mức: bật khi PV dưới điểm đặt và tắt khi PV trên điểm đặt.",
                   "Figure 4.1 · Response of a two-position controller to a sinusoidal input. The output "
                   "has only two states: on while the PV is below the set point, off while it is above.")

# ---------------------------------------------------------------- 4.2
def fig_4_2():
    o = [_txt(330, 16, "Ví dụ đồ thị về điều khiển đóng – ngắt", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 104
    o.append(_axes(x0, y0, W, H, "thời gian", "nhiệt độ (°C)",
                   xt=[(0, "0"), (0.5, "1,5"), (1, "3")],
                   yt=[(0, "46"), (0.5, "52"), (1, "58")]))

    def py(v):
        return y0 + H - (v - 46.0) / 12.0 * H

    # dead band straddling the set point
    o.append(_rect(x0, py(53.0), W, py(51.0) - py(53.0), "#fdf3dd", sw=0))
    o.append(_line(x0, py(52.0), x0 + W, py(52.0), sw=1.0, color=GREY, dash="5 4"))
    o.append(_txt(x0 + 4, py(52.0) - 5, "SP", 6.8, color=GREY, anchor="start"))
    o.append(_txt(x0 + W - 4, py(53.0) - 5, "vùng chết", 6.6, color=GOLD, anchor="end"))
    # the temperature ramps up while the burner is on and decays while it is off
    up, down, dt = 6.0, -3.6, 0.002
    pts, seg = [], []
    t, temp = 0.0, 51.0
    yb = y0 + H + 30
    on = True
    while t <= 3.0001:
        # the burner latches off at the top of the band and on at the bottom
        if on and temp >= 53.0:
            on = False
        elif (not on) and temp <= 51.0:
            on = True
        pts.append((x0 + t / 3.0 * W, py(temp)))
        seg.append((x0 + t / 3.0 * W, yb - (12 if on else 0)))
        temp += (up if on else down) * dt
        t += dt
    o.append(_poly(pts, color=RED, sw=1.7))
    o.append(_line(x0, yb, x0 + W, yb, sw=0.8, color=GREY))
    o.append(_poly(seg, color=GOLD, sw=1.5))
    o.append(_txt(x0 - 6, yb - 2, "đốt", 6.4, color=GOLD, anchor="end"))
    return _finish(o, 660, 214,
                   "Hình 4-2 · Ví dụ đồ thị về điều khiển đóng – ngắt trên một nồi hơi gia nhiệt: nhiệt độ "
                   "dao động quanh điểm đặt trong vùng chết, còn đầu ra chỉ chuyển giữa hai trạng thái.",
                   "Figure 4.2 · Graphical example of on-off control on a fired boiler: the temperature "
                   "oscillates about the set point inside the dead band while the output switches between "
                   "two states.")


# ---------------------------------------------------------------- 4.3
def fig_4_3():
    o = [_txt(330, 18, "Khái niệm điều khiển theo mô hình (feedforward)", 8.6, weight="600")]
    y = 74
    o.append(_box(40, y, 120, 44, "Nhiễu\n(tải thay đổi)", fill="#fdeccf"))
    o.append(_box(210, y, 130, 44, "Bộ bù\ntheo mô hình", fill="#eef3fb"))
    o.append(_box(390, y, 110, 44, "Van", fill="#eef3fb"))
    o.append(_box(540, y, 90, 44, "Quá trình", fill="#eef3fb"))
    for a, b in ((160, 210), (340, 390), (500, 540)):
        o.append(_arrow(a, y + 22, b, y + 22, sw=1.2))
    o.append(_arrow(586, y + 44, 586, y + 74, sw=1.2))
    o.append(_txt(586, y + 90, "PV", 7.2, color=GREY))
    o.append(_txt(330, y - 12, "không có đường phản hồi: đầu ra không ảnh hưởng tới tác động điều khiển",
                  6.8, color=GREY))
    return _finish(o, 660, 186,
                   "Hình 4-3 · Khái niệm điều khiển theo mô hình: tác động điều khiển dựa trên trạng thái "
                   "của nhiễu đầu vào mà không xét tới tình trạng thực của hệ.",
                   "Figure 4.3 · The concept of feedforward control: the control action is based on the "
                   "state of a disturbance input without reference to the actual condition of the system.")

# ---------------------------------------------------------------- 4.4
def fig_4_4():
    o = [_txt(330, 18, "Sơ đồ khối điều khiển theo mô hình", 8.6, weight="600")]
    y = 76
    o.append(_box(26, y, 104, 42, "Nhiễu", fill="#fdeccf"))
    o.append(_box(158, y, 104, 42, "Phần tử đo\nnhiễu", fill="#eef3fb"))
    o.append(_box(290, y, 104, 42, "Bộ bù FF", fill="#eef3fb"))
    o.append(_circle(452, y + 21, 13))
    o.append(_box(478, y, 84, 42, "Van", fill="#eef3fb"))
    o.append(_box(478, y + 84, 84, 42, "Quá trình", fill="#eef3fb"))
    o.append(_arrow(130, y + 21, 158, y + 21, sw=1.2))
    o.append(_arrow(262, y + 21, 290, y + 21, sw=1.2))
    o.append(_arrow(394, y + 21, 439, y + 21, sw=1.2))
    o.append(_arrow(465, y + 21, 478, y + 21, sw=1.2))
    o.append(_arrow(520, y + 42, 520, y + 84, sw=1.2))
    o.append(_arrow(562, y + 105, 600, y + 105, sw=1.2))
    o.append(_txt(604, y + 108, "PV", 7.2, color=GREY, anchor="start"))
    # bias from the operator into the summing junction
    o.append(_arrow(452, y + 60, 452, y + 36, sw=1.0, color=GREY, dash="4 3"))
    o.append(_txt(452, y + 74, "điểm đặt tay", 6.4, color=GREY))
    o.append(_txt(452, y + 21 - 18, "+", 7.4, color=INK))
    return _finish(o, 660, 210,
                   "Hình 4-4 · Sơ đồ khối của điều khiển theo mô hình. Bộ bù tính trước lượng bù cho nhiễu "
                   "đo được rồi cộng vào tín hiệu đặt trước khi tới van.",
                   "Figure 4.4 · Feedforward block diagram. The compensator calculates the correction for "
                   "the measured disturbance and adds it to the set signal ahead of the valve.")

# ---------------------------------------------------------------- 4.5
def fig_4_5():
    o = [_txt(330, 18, "Bộ điều khiển tác động thuận và tác động nghịch", 8.6, weight="600")]
    # tank
    o.append(_rect(120, 60, 170, 110, "#eef3fb"))
    o.append(_rect(120, 148, 170, 22, "#dfe7f2"))
    # inlet line with V1
    o.append(_line(60, 76, 120, 76, sw=1.6))
    o.append(_poly([(84, 66), (104, 76), (84, 86)], fill=PAPER, sw=1.2, close=True))
    o.append(_txt(108, 56, "V1", 7.2, color=BLUE, anchor="start"))
    o.append(_arrow(38, 76, 58, 76, sw=1.2, color=BLUE))
    o.append(_txt(20, 80, "vào", 6.6, color=BLUE, anchor="start"))
    # outlet line with V2
    o.append(_line(290, 158, 360, 158, sw=1.6))
    o.append(_poly([(306, 148), (326, 158), (306, 168)], fill=PAPER, sw=1.2, close=True))
    o.append(_txt(316, 142, "V2", 7.2, color=GOLD))
    o.append(_arrow(360, 158, 382, 158, sw=1.2, color=GOLD))
    o.append(_txt(386, 162, "ra", 6.6, color=GOLD, anchor="start"))
    # level transmitter and controller
    o.append(_circle(205, 118, 11, fill=PAPER))
    o.append(_txt(205, 121, "LT", 6.4, color=GREY))
    o.append(_box(430, 96, 104, 44, "Bộ điều khiển\nmức LC", fill="#eef3fb", size=7))
    o.append(_line(216, 118, 430, 118, sw=1.0, color=GREY, dash="4 3"))
    # signal paths to the two valves
    o.append(_path("M 430 106 L 400 106 L 400 48 L 94 48 L 94 62", sw=1.2, color=BLUE, dash="4 3"))
    o.append(_path("M 430 130 L 400 130 L 400 186 L 316 186 L 316 168", sw=1.2, color=GOLD, dash="4 3"))
    o.append(_legend(430, 20,
                     [(BLUE, "V1 vào: tác động nghịch", ""),
                      (GOLD, "V2 ra: tác động thuận", "")], w=200))
    return _finish(o, 660, 202,
                   "Hình 4-5 · Bộ điều khiển tác động thuận và tác động nghịch. Điều khiển van ra V2 là tác "
                   "động thuận (PV tăng thì OP tăng); điều khiển van vào V1 là tác động nghịch (PV tăng thì "
                   "OP giảm).",
                   "Figure 4.5 · Direct and reverse acting controllers. Manipulating the outlet valve V2 is "
                   "direct action (PV up, OP up); manipulating the inlet valve V1 is reverse action (PV up, "
                   "OP down).")

# ---------------------------------------------------------------- 4.6
def fig_4_6():
    o = [_txt(330, 18, "Điều khiển phản hồi bằng tay", 8.6, weight="600")]
    y = 76
    o.append(_box(40, y, 110, 52, "Người\nvận hành", fill="#fdeccf"))
    o.append(_box(200, y, 100, 52, "Nhiệt kế", fill="#eef3fb"))
    o.append(_box(350, y, 100, 52, "Van hơi", fill="#eef3fb"))
    o.append(_box(500, y, 110, 52, "Bình gia\nnhiệt", fill="#eef3fb"))
    o.append(_arrow(150, y + 16, 200, y + 16, sw=1.2, color=BLUE))
    o.append(_txt(175, y + 10, "nhìn", 6.4, color=BLUE))
    o.append(_arrow(300, y + 16, 350, y + 16, sw=1.2))
    o.append(_arrow(450, y + 16, 500, y + 16, sw=1.2))
    o.append(_arrow(555, y + 52, 555, y + 86, sw=1.2))
    o.append(_line(555, y + 86, 95, y + 86, sw=1.2))
    o.append(_arrow(95, y + 86, 95, y + 28, sw=1.2, color=BLUE))
    o.append(_txt(325, y + 100, "so sánh với nhiệt độ mong muốn rồi quay van", 6.6, color=GREY))
    return _finish(o, 660, 190,
                   "Hình 4-6 · Điều khiển phản hồi bằng tay: người vận hành đọc nhiệt kế, so với giá trị "
                   "mong muốn rồi chỉnh van. Vòng kín nằm ở chỗ người, không nằm ở thiết bị.",
                   "Figure 4.6 · Manual feedback control: the operator reads the thermometer, compares it "
                   "with the desired value and moves the valve. The loop is closed by the person, not by an "
                   "instrument.")

# ---------------------------------------------------------------- 4.7
def fig_4_7():
    o = [_txt(330, 18, "Sơ đồ khối vòng điều khiển kín", 8.6, weight="600")]
    y = 84
    o.append(_txt(22, y + 26, "SP", 8.0, color=GREY, anchor="start"))
    o.append(_arrow(46, y + 22, 74, y + 22, sw=1.2))
    o.append(_circle(88, y + 22, 13))
    o.append(_txt(88, y + 12, "+", 7.0))
    o.append(_txt(82, y + 31, "−", 8.4))
    o.append(_box(130, y, 108, 44, "Bộ điều khiển\n(P, I, D)", fill="#eef3fb", size=7))
    o.append(_box(268, y, 84, 44, "Van", fill="#eef3fb"))
    o.append(_box(382, y, 104, 44, "Quá trình", fill="#eef3fb"))
    o.append(_box(516, y, 100, 44, "Cảm biến", fill="#eef3fb"))
    for a, b in ((101, 130), (238, 268), (352, 382), (486, 516)):
        o.append(_arrow(a, y + 22, b, y + 22, sw=1.2))
    o.append(_txt(249, y + 14, "MV", 6.4, color=GREY))
    o.append(_txt(500, y + 14, "PV", 6.4, color=GREY))
    o.append(_arrow(616, y + 22, 640, y + 22, sw=1.2))
    o.append(_arrow(566, y + 44, 566, y + 84, sw=1.2))
    o.append(_line(566, y + 84, 88, y + 84, sw=1.2))
    o.append(_arrow(88, y + 84, 88, y + 36, sw=1.2))
    o.append(_txt(330, y + 98, "tín hiệu phản hồi", 6.8, color=GREY))
    return _finish(o, 660, 210,
                   "Hình 4-7 · Sơ đồ khối vòng điều khiển kín. Sai lệch Err = SP − PV được đưa vào bộ điều "
                   "khiển, đầu ra đi qua van tới quá trình rồi được đo và quay lại điểm so sánh.",
                   "Figure 4.7 · Closed-loop block diagram. The error Err = SP − PV enters the controller, "
                   "whose output passes through the valve and the process, is measured and returns to the "
                   "comparison point.")

# ---------------------------------------------------------------- 4.8
def fig_4_8():
    o = [_txt(330, 18, "Kết hợp điều khiển theo mô hình và phản hồi", 8.6, weight="600")]
    y = 96
    o.append(_box(24, 40, 96, 38, "Nhiễu", fill="#fdeccf", size=7.4))
    o.append(_box(148, 40, 96, 38, "Bộ bù FF", fill="#eef3fb", size=7.4))
    o.append(_circle(286, 59, 12))
    o.append(_box(324, y, 84, 40, "Van", fill="#eef3fb", size=7.4))
    o.append(_box(430, y, 96, 40, "Quá trình", fill="#eef3fb", size=7.4))
    o.append(_box(324, 40, 84, 38, "Bộ điều khiển\nPI", fill="#eef3fb", size=6.6))
    o.append(_box(560, y, 78, 40, "Cảm biến", fill="#eef3fb", size=6.8))
    o.append(_arrow(120, 59, 148, 59, sw=1.2))
    o.append(_arrow(244, 59, 274, 59, sw=1.2))
    o.append(_arrow(298, 59, 324, 59, sw=1.2))
    o.append(_arrow(408, 59, 408, 96, sw=1.2))
    o.append(_arrow(408, y + 20, 430, y + 20, sw=1.2))
    o.append(_arrow(526, y + 20, 560, y + 20, sw=1.2))
    o.append(_arrow(599, y + 40, 599, y + 74, sw=1.2))
    o.append(_line(599, y + 74, 286, y + 74, sw=1.2))
    o.append(_arrow(286, y + 74, 286, 71, sw=1.2))
    o.append(_txt(442, y + 88, "phản hồi", 6.6, color=GREY))
    o.append(_txt(268, 34, "SP", 7.0, color=GREY, anchor="end"))
    return _finish(o, 660, 200,
                   "Hình 4-8 · Sơ đồ khối kết hợp cả hai: nhánh theo mô hình bù phần lớn nhiễu ngay khi nó "
                   "xuất hiện, vòng phản hồi chỉ còn phải sửa phần sai số còn lại.",
                   "Figure 4.8 · Block diagram of the combination: the feedforward branch corrects most of "
                   "the upset as it occurs, leaving only the residual error for the feedback loop.")

# ---------------------------------------------------------------- 4.9
def fig_4_9():
    o = [_txt(330, 16, "Đường đáp ứng quá trình: thời gian chết và hằng số thời gian", 8.6,
              weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "PV",
                   yt=[(0, "0"), (0.632, "63,2 %"), (1, "100 %")]))
    L, T = 0.18, 0.30

    def resp(t):
        if t < L:
            return 0.0
        return 1.0 - math.exp(-(t - L) / T)

    o.append(_curve(resp, x0, y0, W, H, n=241, xr=(0, 1), color=INK, sw=1.9))
    # step in the manipulated variable
    o.append(_poly([(x0, y0 + H), (x0 + 0.04 * W, y0 + H), (x0 + 0.04 * W, y0 + 0.10 * H),
                    (x0 + W, y0 + 0.10 * H)], color=GREY, sw=1.3, dash="5 4"))
    # dead time
    o.append(_line(x0 + 0.04 * W, y0 + H, x0 + (0.04 + L) * W, y0 + H, sw=0))
    o.append(_arrow(x0 + 0.04 * W, y0 + H + 14, x0 + (0.04 + L) * W, y0 + H + 14, sw=0.9, color=GOLD))
    o.append(_arrow(x0 + (0.04 + L) * W, y0 + H + 14, x0 + 0.04 * W, y0 + H + 14, sw=0.9, color=GOLD))
    o.append(_txt(x0 + (0.04 + L / 2) * W, y0 + H + 26, "L: thời gian chết", 6.6, color=GOLD))
    # time constant: 63.2 % of the final change after one T
    xT = x0 + (0.04 + L + T) * W
    yT = y0 + H - 0.632 * H
    o.append(_line(xT, yT, xT, y0 + H, sw=0.8, color=BLUE, dash="3 3"))
    o.append(_line(x0, yT, xT, yT, sw=0.8, color=BLUE, dash="3 3"))
    o.append(_txt(xT + 5, y0 + H - 8, "T", 7.2, color=BLUE, anchor="start"))
    o.append(_circle(xT, yT, 2.6, fill=BLUE))
    o.append(_legend(x0 + W - 176, y0 + H - 40,
                     [(INK, "PV", ""), (GREY, "MV (bậc thang)", "5 4")], w=174))
    return _finish(o, 660, 216,
                   "Hình 4-9 · Đường đáp ứng của quá trình sau một bậc thang ở biến điều khiển, thể hiện cả "
                   "thời gian chết L và hằng số thời gian T (thời điểm đạt 63,2 % mức thay đổi cuối cùng).",
                   "Figure 4.9 · Process reaction curve after a step in the manipulated variable, showing "
                   "both the dead time L and the time constant T (the point at which 63.2 % of the final "
                   "change is reached).")

# ---------------------------------------------------------------- 4.10
def fig_4_10():
    o = [_txt(330, 16, "Thuật toán lấy mẫu – giữ khi thời gian chết lớn", 8.6, weight="600")]
    x0, y0, W, H = 84, 40, 500, 96
    o.append(_axes(x0, y0, W, H, "thời gian", "PV"))
    L, T = 0.10, 0.22

    def pv(t):
        if t < L:
            return 0.0
        return 1.0 - math.exp(-(t - L) / T)

    o.append(_curve(pv, x0, y0, W, H, n=241, xr=(0, 1), color=INK, sw=1.8))
    # controller enabled in short windows, held in between
    yb = y0 + H + 30
    o.append(_line(x0, yb, x0 + W, yb, sw=0.8, color=GREY))
    windows = [(0.12, 0.20), (0.34, 0.42), (0.56, 0.64), (0.78, 0.86)]
    for a, b in windows:
        o.append(_rect(x0 + a * W, yb - 14, (b - a) * W, 14, "#fdeccf", sw=0.9, stroke=GOLD))
        o.append(_txt(x0 + (a + b) / 2 * W, yb - 4, "ON", 5.8, color=GOLD))
    o.append(_txt(x0 - 6, yb - 4, "điều khiển", 6.4, color=GOLD, anchor="end"))
    o.append(_txt(x0 + W / 2, yb + 14, "giữ (hold) giữa các cửa sổ", 6.6, color=GREY))
    return _finish(o, 660, 200,
                   "Hình 4-10 · Thuật toán lấy mẫu – giữ: bộ điều khiển chỉ được bật trong những khoảng ngắn "
                   "rồi chuyển sang trạng thái giữ, chờ hết thời gian chết của quá trình trước khi bật lại.",
                   "Figure 4.10 · Sample-and-hold: the controller is enabled for short periods, then its "
                   "output is held while the process dead time elapses before it is enabled again.")

# ---------------------------------------------------------------- 4.11
def fig_4_11():
    o = [_txt(330, 16, "Đáp ứng quá trình với một thay đổi bậc thang ở đầu vào", 8.6, weight="600")]
    x0, y0, W, H = 84, 44, 500, 116
    o.append(_axes(x0, y0, W, H, "thời gian", "PV",
                   yt=[(0, "PV₁"), (1, "PV₂")]))
    L, T = 0.16, 0.26

    def resp(t):
        if t < L:
            return 0.0
        return 1.0 - math.exp(-(t - L) / T)

    o.append(_curve(resp, x0, y0, W, H, n=241, xr=(0, 1), color=INK, sw=1.9))
    # the gain triangle: ΔPV over ΔMV
    o.append(_line(x0, y0 + H, x0, y0, sw=0, color=GREY))
    o.append(_arrow(x0 - 40, y0 + H, x0 - 40, y0, sw=0.9, color=GOLD))
    o.append(_arrow(x0 - 40, y0, x0 - 40, y0 + H, sw=0.9, color=GOLD))
    o.append(_txt(x0 - 46, y0 + H / 2, "ΔPV", 6.8, color=GOLD, anchor="end"))
    o.append(_arrow(x0, y0 + H + 16, x0 + 0.10 * W, y0 + H + 16, sw=0.9, color=BLUE))
    o.append(_arrow(x0 + 0.10 * W, y0 + H + 16, x0, y0 + H + 16, sw=0.9, color=BLUE))
    o.append(_txt(x0 + 0.05 * W, y0 + H + 28, "ΔMV", 6.8, color=BLUE))
    o.append(_txt(x0 + W - 8, y0 + 16, "K = ΔPV / ΔMV", 7.4, color=INK, anchor="end"))
    o.append(_txt(x0 + 0.04 * W, y0 + H - 6, "L", 6.8, color=GREY, anchor="start"))
    return _finish(o, 660, 210,
                   "Hình 4-11 · Ví dụ đáp ứng của quá trình với một thay đổi bậc thang ở đầu vào: hệ số "
                   "khuếch đại K là tỉ số giữa mức thay đổi đầu ra và mức thay đổi đầu vào sau khi đã ổn định.",
                   "Figure 4.11 · Example of a process response to a step change in the input: the process "
                   "gain K is the ratio of the settled output change to the input change.")

FIGURES = [fig_4_1, fig_4_2, fig_4_3, fig_4_4, fig_4_5, fig_4_6, fig_4_7, fig_4_8,
           fig_4_9, fig_4_10, fig_4_11]
