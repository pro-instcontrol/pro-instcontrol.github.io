# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 12 — Long Dead Time and the Smith Predictor."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- helpers
def _shift(buf, val):
    buf.append(val)
    return buf.pop(0)


def _plain(ts, dt, kp, ti, tau=1.5, L=3.0, sp=50.0):
    """A plain PI loop on a first-order-plus-dead-time process."""
    n = len(ts)
    y = [0.0] * n
    us = [0.0] * n
    u = 0.0
    integ = 0.0
    buf = [0.0] * int(L / dt + 1)
    for i, t in enumerate(ts):
        ud = _shift(buf, u)
        if i:
            y[i] = y[i - 1] + dt * ((ud - y[i - 1]) / tau)
        e = sp - y[i]
        integ += e * dt
        u = kp * (e + integ / ti)
        us[i] = u
    return y, us


def _smith(ts, dt, kp, ti, Lp=4.0, Lm=4.0, tau=1.5, taum=1.5, sp=50.0):
    """The Smith predictor, with the model's dead time free to be wrong."""
    n = len(ts)
    y = [0.0] * n
    u = 0.0
    integ = 0.0
    ym = 0.0
    bp = [0.0] * int(Lp / dt + 1)
    bm = [0.0] * int(Lm / dt + 1)
    for i, t in enumerate(ts):
        ud = _shift(bp, u)
        ymd = _shift(bm, ym)
        if i:
            y[i] = y[i - 1] + dt * ((ud - y[i - 1]) / tau)
        ym = ym + dt * ((u - ym) / taum)
        e = sp - (y[i] + ym - ymd)
        integ += e * dt
        u = kp * (e + integ / ti)
    return y


# ---------------------------------------------------------------- 12.1
def fig_12_1():
    """Three reaction curves: short, medium and long dead time."""
    x0, y0, W, H = 72, 46, 476, 128

    def resp(L):
        def f(t):
            if t <= L:
                return 0.0
            return 1.0 - math.exp(-(t - L) / 1.0)
        return f

    o = [_axes(x0, y0, W, H, "thời gian", "PV (% thang)",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.632, "63 %"), (1, "100")])]
    o.append(_line(x0, y0 + H * (1 - 0.632), x0 + W, y0 + H * (1 - 0.632),
                   sw=0.8, dash="4 3", color=GREY))
    for L, col, lab, lvl in [(0.3, BLUE, "L ngắn", 4), (1.8, GREEN, "L vừa", 14),
                             (4.0, RED, "L dài", 24)]:
        o.append(_curve(resp(L), x0, y0, W, H, n=321, xr=(0, 10), yr=(0, 1.0),
                        color=col, sw=2.0))
        # the dead-time span, drawn as a bar under the axis, one row per curve
        o.append(_line(x0, y0 + H + lvl, x0 + W * L / 10.0, y0 + H + lvl, sw=1.2, color=col))
        o.append(_txt(x0 + W * L / 10.0 + 6, y0 + H + lvl + 3, lab, 6.6,
                      anchor="start", color=col))
    o.append(_txt(x0 + W * 0.46, y0 + H * 0.20, "cùng một hằng số thời gian, ba thời gian chết",
                  6.8, anchor="start", color=GREY))
    return _finish(o, 660, 208,
                   "Hình 12-1. Ba đường cong phản ứng với cùng một hằng số thời gian nhưng thời gian "
                   "chết khác nhau. Thời gian chết chỉ làm đường cong dịch sang phải, nhưng chính độ "
                   "dịch đó phá vỡ vòng điều khiển.",
                   "Figure 12-1. Three reaction curves with the same time constant but different dead "
                   "times. Dead time only shifts the curve to the right — but that shift is what breaks "
                   "the control loop.",
                   "Đồ thị ba đường cong phản ứng bậc một: đường xanh dịch ít nhất, đường đỏ dịch nhiều "
                   "nhất; các đoạn gạch dưới trục đánh dấu độ dài thời gian chết của từng đường.",
                   "Three first-order reaction curves: the blue shifts least, the red most; the bars "
                   "under the axis mark each curve's dead time.")


# ---------------------------------------------------------------- 12.2
def fig_12_2():
    """The conveyor: dead time is distance divided by belt speed."""
    o = []
    # the hopper
    o.append(_box(28, 34, 82, 44, "PHỄU CHỨA", size=7.0))
    o.append(_path("M 56 78 L 82 78 L 76 96 L 62 96 Z", fill="#e8e2d4", sw=1.0, color=INK))
    o.append(_arrow(69, 96, 69, 112))

    # the belt
    o.append(_line(40, 112, 470, 112, sw=1.4, color=INK))
    o.append(_line(40, 126, 470, 126, sw=1.4, color=INK))
    for cx in range(52, 470, 34):
        o.append(_circle(cx, 119, 3.2, "#fff", 0.9, INK))
    # material riding the belt
    for cx in range(90, 380, 26):
        o.append(_line(cx, 113, cx, 125, sw=1.6, color=GOLD))

    # the belt weigher
    o.append(_box(378, 92, 66, 44, "CÂN BĂNG", size=6.8))
    o.append(_arrow(411, 136, 411, 158))
    o.append(_txt(415, 152, "PV", 6.8, anchor="start", color=BLUE))

    # the receiving process
    o.append(_box(508, 96, 108, 46, "QUÁ TRÌNH", size=7.2))
    o.append(_arrow(470, 119, 508, 119))

    # belt speed and the distance
    o.append(_arrow(196, 92, 268, 92))
    o.append(_txt(232, 86, "tốc độ băng v", 6.8, anchor="middle", color=GREY))
    o.append(_arrow(190, 176, 44, 176))
    o.append(_arrow(190, 176, 378, 176))
    o.append(_txt(284, 172, "khoảng cách d", 6.8, anchor="middle", color=GREY))
    o.append(_line(44, 168, 44, 180, sw=1.0, color=GREY))
    o.append(_line(378, 168, 378, 180, sw=1.0, color=GREY))
    o.append(_txt(284, 196, "L = d / v ≈ 10 phút", 7.2, anchor="middle", color=RED))

    o.append(_txt(96, 148, "thất thoát do rơi vãi dọc đường", 6.6, anchor="start", color=GREY))
    return _finish(o, 660, 214,
                   "Hình 12-2. Băng tải dài: thời gian chết bằng khoảng cách chia cho tốc độ băng. Bộ "
                   "điều khiển thay đổi lưu lượng ở phễu nhưng phải chờ khoảng mười phút mới thấy tác "
                   "động ở đầu cân.",
                   "Figure 12-2. A long conveyor: dead time is distance divided by belt speed. The "
                   "controller changes the hopper feed but waits about ten minutes before the weigher at "
                   "the far end sees any effect.",
                   "Sơ đồ băng tải: phễu chứa đổ liệu xuống băng, băng chạy qua cân băng rồi vào quá "
                   "trình; bên dưới ghi khoảng cách d và công thức thời gian chết L = d/v.",
                   "A conveyor diagram: the hopper feeds the belt, the belt passes a weigher and enters "
                   "the process; below, the distance d and the dead-time formula L = d/v are marked.")


# ---------------------------------------------------------------- 12.3
def fig_12_3():
    """What the controller does while it waits: it keeps ramping."""
    dt = 0.02
    ts = [i * dt for i in range(1001)]
    y, us = _plain(ts, dt, 1.0, 3.0)

    o = []
    # upper panel: the controller output
    o.append(_axes(72, 26, 476, 76, "", "OP (%)",
                   xt=[(0, "0"), (1, "")],
                   yt=[(0, "0"), (1, "100")]))
    o.append(_poly([(72 + 476 * t / 20.0, 26 + 76 * (1 - min(120.0, u) / 120.0))
                    for t, u in zip(ts, us)], sw=1.9, color=GOLD))
    o.append(_txt(80, 38, "đầu ra vẫn tăng trong suốt thời gian chết", 6.8,
                  anchor="start", color=GOLD))

    # lower panel: the PV
    o.append(_axes(72, 136, 476, 76, "thời gian", "PV (% thang)",
                   xt=[(0, "0"), (1, "")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_line(72, 136 + 76 * 0.5, 548, 136 + 76 * 0.5, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(78, 136 + 76 * 0.5 - 5, "SP", 6.6, anchor="start", color=GREY))
    o.append(_poly([(72 + 476 * t / 20.0, 136 + 76 * (1 - min(100.0, v) / 100.0))
                    for t, v in zip(ts, y)], sw=1.9, color=RED))
    o.append(_txt(78, 148, "PV vọt lố rồi mới quay lại", 6.8, anchor="start", color=RED))
    return _finish(o, 660, 226,
                   "Hình 12-3. Vì sao thời gian chết phá vỡ vòng kín: trong suốt thời gian chết bộ điều "
                   "khiển không thấy phản ứng nào nên vẫn tiếp tục tăng đầu ra; khi PV cuối cùng nhúc "
                   "nhích thì nó đã bù quá nhiều.",
                   "Figure 12-3. Why dead time breaks a closed loop: throughout the dead time the "
                   "controller sees no reaction, so it keeps raising its output; by the time the PV "
                   "finally moves it has over-compensated.",
                   "Hai đồ thị xếp trên dưới: phía trên là đầu ra bộ điều khiển tăng đều rồi mới hạ; phía "
                   "dưới là PV vọt lên trên điểm đặt rồi dao động trở lại.",
                   "Two stacked plots: above, the controller output ramps up before coming back; below, "
                   "the PV overshoots the set point and then oscillates back.")


# ---------------------------------------------------------------- 12.4
def fig_12_4():
    """The Smith predictor: an ordinary loop plus two extra terms in the feedback path."""
    o = []
    # the ordinary loop
    o.append(_txt(10, 44, "SP", 7.2, anchor="start"))
    o.append(_arrow(10, 56, 40, 56))
    o.append(_node(52, 56, "Σ", r=12, size=8.5))
    o.append(_arrow(64, 56, 90, 56))
    o.append(_box(92, 38, 66, 36, "BỘ ĐIỀU\nKHIỂN", size=6.8))
    o.append(_arrow(158, 56, 192, 56))
    o.append(_circle(176, 56, 2.6, INK, 0.8, INK))
    o.append(_box(194, 38, 62, 36, "QUÁ\nTRÌNH", size=6.8))
    o.append(_arrow(256, 56, 286, 56))
    o.append(_box(288, 38, 62, 36, "e<sup>−Ls</sup>", size=7.6))
    o.append(_arrow(350, 56, 386, 56))
    o.append(_txt(390, 60, "PV", 7.2, anchor="start"))

    # the two model terms
    o.append(_line(176, 56, 176, 176, sw=1.1))
    o.append(_arrow(176, 118, 196, 118))
    o.append(_box(198, 100, 84, 36, "MÔ HÌNH G", size=6.8))
    o.append(_arrow(176, 176, 196, 176))
    o.append(_box(198, 158, 84, 36, "G·e<sup>−Ls</sup>", size=7.0))

    # the summing point of the feedback path
    o.append(_node(330, 147, "Σ", r=12, size=8.5))
    o.append(_line(282, 118, 330, 118, sw=1.1))
    o.append(_arrow(330, 118, 330, 135))
    o.append(_line(282, 176, 330, 176, sw=1.1))
    o.append(_arrow(330, 176, 330, 159))
    o.append(_arrow(366, 56, 366, 147))
    o.append(_line(366, 147, 342, 147, sw=1.1))
    o.append(_txt(310, 112, "+", 7.0, anchor="end", color=GREEN))
    o.append(_txt(310, 184, "−", 7.6, anchor="end", color=RED))

    # the feedback bus back to the first summer
    o.append(_line(318, 147, 300, 147, sw=1.1))
    o.append(_line(300, 147, 300, 210, sw=1.1))
    o.append(_line(300, 210, 30, 210, sw=1.1))
    o.append(_arrow(30, 210, 30, 68))
    o.append(_arrow(30, 68, 40, 68))
    o.append(_txt(140, 204, "hai số hạng thêm vào đường phản hồi", 6.8,
                  anchor="start", color=BLUE))
    return _finish(o, 660, 226,
                   "Hình 12-4. Mô hình Smith Predictor: một vòng phản hồi thông thường, cộng thêm một "
                   "vòng trong đưa hai số hạng vào đường phản hồi — mô hình không trễ và mô hình có trễ.",
                   "Figure 12-4. The Smith predictor model: an ordinary feedback loop plus an inner loop "
                   "that introduces two extra terms into the feedback path — the undelayed model and the "
                   "delayed one.",
                   "Sơ đồ khối: điểm đặt vào bộ cộng, qua bộ điều khiển tới quá trình và khâu trễ ra PV; "
                   "tín hiệu sau bộ điều khiển còn rẽ xuống hai khối mô hình, một không trễ và một có "
                   "trễ, rồi cộng trừ vào đường phản hồi.",
                   "Block diagram: the set point enters a summer, passes the controller, the process and "
                   "a delay to the PV; the controller output also branches to two model blocks, one "
                   "undelayed and one delayed, which add and subtract into the feedback path.")


# ---------------------------------------------------------------- 12.5
def fig_12_5():
    """Two loops: the one that exists, and the one the controller is shown."""
    o = [_txt(18, 24, "VÒNG THẬT", 7.6, anchor="start", color=GREY)]
    o.append(_txt(10, 44, "SP", 6.8, anchor="start"))
    o.append(_arrow(10, 56, 34, 56))
    o.append(_node(46, 56, "Σ", r=11, size=8.0))
    o.append(_arrow(57, 56, 78, 56))
    o.append(_box(80, 40, 56, 32, "C", size=7.6))
    o.append(_arrow(136, 56, 158, 56))
    o.append(_box(160, 40, 60, 32, "QUÁ TRÌNH", size=6.4))
    o.append(_arrow(220, 56, 242, 56))
    o.append(_box(244, 40, 56, 32, "e<sup>−Ls</sup>", size=7.4))
    o.append(_arrow(300, 56, 326, 56))
    o.append(_txt(330, 60, "PV", 7.0, anchor="start"))
    o.append(_line(316, 56, 316, 118, sw=1.0))
    o.append(_line(316, 118, 24, 118, sw=1.0))
    o.append(_arrow(24, 118, 24, 68))
    o.append(_arrow(24, 68, 34, 68))
    o.append(_txt(96, 112, "vòng có thời gian chết L", 6.6, anchor="start", color=RED))

    o.append(_txt(372, 24, "VÒNG BỘ ĐIỀU KHIỂN NHÌN THẤY", 7.6, anchor="start", color=GREY))
    o.append(_txt(366, 44, "SP", 6.8, anchor="start"))
    o.append(_arrow(366, 56, 390, 56))
    o.append(_node(402, 56, "Σ", r=11, size=8.0))
    o.append(_arrow(413, 56, 434, 56))
    o.append(_box(436, 40, 56, 32, "C", size=7.6))
    o.append(_arrow(492, 56, 514, 56))
    o.append(_box(516, 40, 92, 32, "MÔ HÌNH G", size=6.6, sub="→ PV*"))
    o.append(_arrow(608, 56, 636, 56))
    o.append(_line(620, 56, 620, 118, sw=1.0))
    o.append(_line(620, 118, 380, 118, sw=1.0))
    o.append(_arrow(380, 118, 380, 68))
    o.append(_arrow(380, 68, 390, 68))
    o.append(_txt(440, 112, "vòng không có L", 6.6, anchor="start", color=GREEN))

    o.append(_arrow(330, 148, 420, 148))
    o.append(_txt(375, 143, "mô hình G, L", 6.6, anchor="middle", color=GREY))
    o.append(_txt(18, 168, "Bộ điều khiển điều khiển PV* chứ không điều khiển PV; nếu mô hình đúng thì "
                           "kéo PV theo là hệ quả.", 6.9, anchor="start", color=INK))
    return _finish(o, 660, 190,
                   "Hình 12-5. Hai vòng cùng tồn tại: vòng thật có thời gian chết, và vòng mà bộ điều "
                   "khiển thực sự nhìn thấy — không có thời gian chết, nhờ mô hình.",
                   "Figure 12-5. Two loops coexist: the real loop with its dead time, and the loop the "
                   "controller actually sees — no dead time, thanks to the model.",
                   "Hai sơ đồ cạnh nhau: bên trái vòng có khâu trễ trong đường phản hồi; bên phải vòng "
                   "chỉ có mô hình không trễ, với mũi tên mô hình nối hai bên.",
                   "Two diagrams side by side: on the left the loop with a delay in its feedback path; on "
                   "the right a loop containing only the undelayed model, joined by a model arrow.")


# ---------------------------------------------------------------- 12.6
def fig_12_6():
    """What a model mismatch does to the real PV."""
    dt = 0.02
    ts = [i * dt for i in range(1201)]
    good = _smith(ts, dt, 2.0, 1.5, Lm=4.0)
    short = _smith(ts, dt, 2.0, 1.5, Lm=2.0)
    long_ = _smith(ts, dt, 2.0, 1.5, Lm=5.5)

    x0, y0, W, H = 72, 46, 476, 130
    o = [_axes(x0, y0, W, H, "thời gian", "PV (% thang)",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_line(x0, y0 + H * 0.5, x0 + W, y0 + H * 0.5, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 6, y0 + H * 0.5 - 5, "SP", 6.6, anchor="start", color=GREY))
    for vals, col in [(short, GOLD), (long_, RED), (good, BLUE)]:
        o.append(_poly([(x0 + W * t / 24.0, y0 + H * (1 - max(0.0, min(100.0, v)) / 100.0))
                        for t, v in zip(ts, vals)], sw=1.9, color=col))
    o.append(_legend_h(x0 + 6, y0 + H + 40,
                       [(BLUE, "mô hình đúng: PV về SP", ""),
                        (GOLD, "L mô hình quá ngắn: PV đậu cao", ""),
                        (RED, "L mô hình quá dài: PV tụt", "")], gap=16))
    return _finish(o, 660, 232,
                   "Hình 12-6. Sai lệch mô hình: chỉ khi thời gian chết của mô hình đúng bằng của quá "
                   "trình thì PV mới về đúng điểm đặt. Mô hình ngắn quá thì PV đậu cao hơn, dài quá thì "
                   "PV tụt xuống — cả hai đều ổn định ở một giá trị sai.",
                   "Figure 12-6. Model mismatch: only when the model's dead time matches the process does "
                   "the PV reach set point. A model that is too short leaves the PV high, one that is too "
                   "long lets it fall — both settle at the wrong value.",
                   "Đồ thị PV theo thời gian với ba đường: đường xanh về đúng 50, đường vàng đậu quanh "
                   "66, đường đỏ tụt xuống khoảng 34.",
                   "A PV-versus-time plot with three traces: the blue settles at 50, the gold near 66, "
                   "and the red falls to about 34.")
