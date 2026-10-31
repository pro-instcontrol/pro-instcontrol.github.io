# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 14 — Self-Tuning Control and SPC."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h

# ---------------------------------------------------------------- table 14.1
DATA = [
    [1, 4, 6, 4], [3, 7, 5, 5], [4, 5, 5, 7], [6, 2, 4, 5], [1, 6, 7, 3],
    [8, 3, 6, 4], [7, 5, 6, 6], [5, 3, 4, 6], [4, 5, 9, 2], [7, 5, 6, 5],
    [4, 5, 6, 5], [6, 7, 8, 5], [3, 3, 7, 3], [6, 3, 2, 9], [7, 3, 4, 3],
    [6, 4, 6, 5], [5, 5, 0, 5], [6, 4, 6, 3], [6, 4, 4, 0], [6, 2, 5, 4]]
AVGS = [sum(r) / 4.0 for r in DATA]
RNGS = [max(r) - min(r) for r in DATA]
XBAR = sum(AVGS) / len(AVGS)          # 4.7625
RBAR = sum(RNGS) / len(RNGS)          # 4.05
SDX = RBAR / 2.059                    # sigma estimated from the mean range
SD_XBAR = SDX / 2.0                   # sigma / sqrt(n), n = 4
SD_R = 0.88 * SDX
UCL_X, LCL_X = XBAR + 3 * SD_XBAR, XBAR - 3 * SD_XBAR
UCL_R, LCL_R = RBAR + 3 * SD_R, max(0.0, RBAR - 3 * SD_R)


def _mk(x0, y0, W, H, xr, yr):
    def X(v):
        return x0 + (v - xr[0]) / float(xr[1] - xr[0]) * W

    def Y(v):
        return y0 + H - (v - yr[0]) / float(yr[1] - yr[0]) * H
    return X, Y


def _gauss(x, mu, sd):
    return math.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))


# ---------------------------------------------------------------- 14.1
def fig_14_1():
    """The three components of a self-tuning controller."""
    o = [_txt(330, 20, "Hai vòng lồng nhau: vòng trong điều khiển, vòng ngoài chỉnh tham số",
              8.2, weight="600")]
    o.append(_circle(80, 82, 13, fill="#fff", sw=1.2))
    o.append(_txt(80, 85, "Σ", 9))
    o.append(_box(112, 56, 96, 52, "BỘ ĐIỀU KHIỂN", fill="#e8eef6", size=6.8,
                  sub="Kc, Ti, Td"))
    o.append(_box(336, 56, 104, 52, "QUÁ TRÌNH", fill="#f6ecd8", size=7.6))
    o.append(_arrow(48, 82, 65, 82, sw=1.1))
    o.append(_txt(40, 78, "SP", 7.4, anchor="end"))
    o.append(_arrow(93, 82, 110, 82, sw=1.1))
    o.append(_arrow(208, 82, 334, 82, sw=1.1))
    o.append(_txt(270, 74, "MV", 7.0))
    o.append(_arrow(440, 82, 492, 82, sw=1.1))
    o.append(_txt(500, 86, "PV", 7.4, anchor="start"))

    o.append(_poly([(492, 82), (522, 82), (522, 132), (80, 132), (80, 95)], sw=1.1))
    o.append(_arrow(80, 132, 80, 96, sw=1.1))

    o.append(_box(112, 186, 118, 44, "BỘ TỔNG HỢP", fill="#e6f0e8", size=6.8,
                  sub="controller synthesizer"))
    o.append(_box(300, 186, 122, 44, "BỘ NHẬN DẠNG", fill="#e6f0e8", size=6.8,
                  sub="system identifier"))
    o.append(_arrow(175, 186, 175, 110, sw=1.0, dash="5 3", color=GREEN))
    o.append(_txt(181, 150, "đổi Kc, Ti, Td", 6.2, anchor="start", color=GREEN))
    o.append(_arrow(300, 208, 232, 208, sw=1.1))
    o.append(_arrow(175, 186, 175, 110, sw=1.0, dash="5 3", color=GREEN))
    o.append(_txt(181, 150, "đổi Kc, Ti, Td", 6.2, anchor="start", color=GREEN))

    o.append(_circle(272, 82, 2.4, fill=INK, sw=0))
    o.append(_line(272, 82, 272, 168, sw=1.0, color=GREY))
    o.append(_line(272, 168, 340, 168, sw=1.0, color=GREY))
    o.append(_arrow(340, 168, 340, 184, sw=1.0, color=GREY))
    o.append(_txt(276, 164, "MV", 6.4, anchor="start", color=GREY))
    o.append(_circle(522, 132, 2.4, fill=INK, sw=0))
    o.append(_line(522, 132, 522, 208, sw=1.0, color=GREY))
    o.append(_arrow(522, 208, 426, 208, sw=1.0, color=GREY))
    o.append(_txt(500, 200, "PV", 6.4, anchor="end", color=GREY))
    return _finish(o, 660, 250,
                   "Hình 14-1. Ba khối của một hệ tự chỉnh định. Vòng trong là vòng điều khiển quen "
                   "thuộc, chỉ khác là các tham số của nó thay đổi được. Vòng ngoài lấy MV và PV, "
                   "nhận dạng quá trình rồi tổng hợp bộ tham số mới — và vòng ngoài chạy chậm hơn "
                   "vòng trong rất nhiều.",
                   "Figure 14-1. The three blocks of a self-tuning system. The inner loop is the "
                   "familiar control loop, except that its parameters can change. The outer loop takes "
                   "the MV and the PV, identifies the process and synthesises a new parameter set — and "
                   "it runs far more slowly than the inner loop.",
                   "Sơ đồ khối: điểm đặt vào bộ điều khiển, ra van và quá trình, PV quay về; phía dưới "
                   "là bộ nhận dạng và bộ tổng hợp nối ngược lên bộ điều khiển bằng nét đứt.",
                   "A block diagram: set point into the controller, out to the process, PV returning; "
                   "below it an identifier and a synthesiser connected back up to the controller by a "
                   "dashed line.")


# ---------------------------------------------------------------- 14.2
def fig_14_2():
    """Gain scheduling: a table of gains approximating the required curve."""
    x0, y0, W, H = 76, 48, 448, 124
    X, Y = _mk(x0, y0, W, H, (0.0, 100.0), (0.0, 3.0))
    o = [_axes(x0, y0, W, H, "biến phụ (tải, % công suất)", "độ lợi Kc",
               xt=[(0.0, "0"), (0.5, "50"), (1.0, "100")],
               yt=[(0.0, "0"), (1.0 / 3.0, "1"), (2.0 / 3.0, "2"), (1.0, "3")])]

    def need(v):
        return 2.55 * math.exp(-v / 62.0) + 0.28

    o.append(_curve(need, x0, y0, W, H, n=161, xr=(0.0, 100.0), yr=(0.0, 3.0),
                    sw=1.8, color=BLUE))

    breaks = [0, 25, 50, 75, 100]
    for i in range(4):
        a, b = breaks[i], breaks[i + 1]
        kc = need((a + b) / 2.0)
        o.append(_line(X(a), Y(kc), X(b), Y(kc), sw=2.2, color=GOLD))
        for xb in (a, b):
            if 0 < xb < 100:
                o.append(_line(X(xb), Y(kc), X(xb), Y(0.0), sw=0.8, dash="3 3", color=GREY))

    for i, (a, b) in enumerate(zip(breaks[:-1], breaks[1:])):
        o.append(_txt(X((a + b) / 2.0), Y(need((a + b) / 2.0)) - 8, "K%d" % (i + 1), 6.4,
                      color=GOLD, weight="600"))
    o.append(_legend_h(x0 + 4, y0 + H + 34,
                       [(BLUE, "độ lợi cần có", ""),
                        (GOLD, "bảng độ lợi đang dùng", "")], gap=20))
    return _finish(o, 660, 226,
                   "Hình 14-2. Điều khiển theo lịch trình độ lợi: độ lợi cần có thay đổi liên tục "
                   "theo tải, nhưng bộ điều khiển chỉ chứa một bảng bốn mức. Giữa hai mốc, độ lợi "
                   "được giữ cố định — đó chính là chỗ mất mát của phương pháp, và cũng là chỗ nó "
                   "đơn giản.",
                   "Figure 14-2. Gain scheduling: the required gain changes continuously with load, but "
                   "the controller only holds a table of four levels. Between breakpoints the gain is "
                   "held constant — that is exactly where the method loses accuracy, and exactly what "
                   "makes it simple.",
                   "Đồ thị độ lợi theo tải: một đường cong giảm dần màu xanh, và bốn đoạn bậc thang màu "
                   "vàng bám theo đường cong ấy.",
                   "A gain-versus-load plot: a decreasing blue curve with four gold step segments "
                   "following it.")


# ---------------------------------------------------------------- 14.3
def fig_14_3():
    """The three features a self-tuner measures on the response."""
    x0, y0, W, H = 74, 46, 462, 132
    X, Y = _mk(x0, y0, W, H, (0.0, 12.0), (0.0, 1.6))
    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0.0, "0"), (1.0, "")],
               yt=[(0.0, "0"), (1.0 / 1.6, "1,0")])]

    zeta, wn = 0.22, 1.35

    def resp(t):
        wd = wn * math.sqrt(1 - zeta * zeta)
        return 1.0 - math.exp(-zeta * wn * t) * (
            math.cos(wd * t) + zeta / math.sqrt(1 - zeta * zeta) * math.sin(wd * t))

    o.append(_curve(resp, x0, y0, W, H, n=361, xr=(0.0, 12.0), yr=(0.0, 1.6),
                    sw=2.0, color=BLUE))
    o.append(_line(x0, Y(1.0), x0 + W, Y(1.0), sw=0.9, dash="4 3", color=GREY))
    o.append(_txt(x0 + 6, Y(1.0) - 5, "điểm đặt", 6.2, anchor="start", color=GREY))

    wd = wn * math.sqrt(1 - zeta * zeta)
    tp = math.pi / wd
    peak = resp(tp)
    o.append(_line(X(tp), Y(1.0), X(tp), Y(peak), sw=1.0, color=RED))
    o.append(_txt(X(tp) + 5, Y((1.0 + peak) / 2.0), "độ vọt lố", 6.4, anchor="start",
                  color=RED))

    t2 = 3 * math.pi / wd
    p2 = resp(t2)
    o.append(_line(X(tp), Y(peak), X(t2), Y(peak), sw=0.9, dash="2 3", color=GOLD))
    o.append(_line(X(t2), Y(1.0), X(t2), Y(peak), sw=1.0, color=GOLD))
    o.append(_txt(X(t2) + 5, Y(peak) - 4, "đỉnh sau", 6.2, anchor="start", color=GOLD))
    o.append(_arrow(X(tp), Y(0.28), X(t2), Y(0.28), sw=0.9, color=GOLD))
    o.append(_arrow(X(t2), Y(0.28), X(tp), Y(0.28), sw=0.9, color=GOLD))
    o.append(_line(X(tp), Y(0.24), X(tp), Y(0.32), sw=0.8, color=GOLD))
    o.append(_line(X(t2), Y(0.24), X(t2), Y(0.32), sw=0.8, color=GOLD))
    o.append(_txt((X(tp) + X(t2)) / 2.0, Y(0.22), "chu kỳ dao động", 6.4, color=GOLD))
    o.append(_txt(X(4.0), Y(1.24), "tỉ số hai đỉnh = mức tắt dần", 6.4, anchor="start",
                  color=INK))
    return _finish(o, 660, 224,
                   "Hình 14-3. Ba đại lượng mà bộ tự chỉnh định đo trên đáp ứng: độ vọt lố (đỉnh cao "
                   "hơn điểm đặt bao nhiêu), chu kỳ dao động (khoảng cách giữa hai đỉnh) và mức tắt "
                   "dần (tỉ số giữa hai đỉnh liên tiếp). Từ ba số này suy ngược ra độ lợi và thời "
                   "gian tích phân.",
                   "Figure 14-3. The three quantities a self-tuner measures on the response: overshoot "
                   "(how far the peak rises above set point), period of oscillation (peak to peak) and "
                   "damping (the ratio of successive peaks). From these three numbers it infers the gain "
                   "and the integral time.",
                   "Đồ thị đáp ứng bậc thang dao động tắt dần, có đánh dấu đỉnh thứ nhất, đỉnh thứ ba "
                   "và khoảng cách giữa chúng.",
                   "A damped oscillatory step response with the first peak, the third peak and the "
                   "spacing between them marked.")


# ---------------------------------------------------------------- 14.4
def fig_14_4():
    """Four subgroups drawn from a stable process."""
    o = []
    hours = ["08:00", "09:00", "10:00", "11:00"]
    samples = [[3.9, 5.6, 4.4, 5.1], [4.2, 5.0, 5.8, 4.5],
               [4.6, 5.4, 4.1, 5.2], [5.0, 4.3, 5.5, 4.7]]
    for i, (h, vals) in enumerate(zip(hours, samples)):
        yb = 34 + i * 46
        X, Y = _mk(96, yb, 380, 40, (2.0, 8.0), (0.0, 1.0))
        o.append(_txt(88, yb + 26, h, 6.6, anchor="end", color=GREY))
        o.append(_line(96, yb + 40, 476, yb + 40, sw=0.7, color="#d8d3c8"))
        pts = [(X(v), Y(_gauss(v, 4.8, 0.62) / 0.66)) for v in
               [2.0 + 0.05 * k for k in range(121)]]
        o.append(_poly(pts, sw=1.3, color=GREY))
        for v in vals:
            o.append(_circle(X(v), Y(0.06), 2.6, fill=BLUE, sw=0))
    o.append(_txt(300, 22, "Bốn nhóm lấy từ một quá trình ổn định", 8.0, weight="600"))
    o.append(_txt(96, 226, "giá trị đo", 6.6, anchor="start", color=GREY))
    return _finish(o, 660, 240,
                   "Hình 14-4. Bốn nhóm con lấy từ một quá trình ổn định, mỗi giờ một nhóm. Đường "
                   "cong chuông là phân bố đầu ra của quá trình trong giờ đó; các chấm là những giá "
                   "trị thực sự đo được. Cả bốn đường cong trùng nhau — đó là định nghĩa của ổn định.",
                   "Figure 14-4. Four subgroups from a stable process, one per hour. The bell curve is "
                   "the distribution of the process output during that hour; the dots are the values "
                   "actually measured. All four curves coincide — that is the definition of stable.",
                   "Bốn hàng, mỗi hàng một đường cong chuông giống nhau đặt trên một trục giá trị, với "
                   "bốn chấm đo rải rác quanh đỉnh.",
                   "Four rows, each with an identical bell curve on a value axis and four measured dots "
                   "scattered around its peak.")


# ---------------------------------------------------------------- 14.5
def fig_14_5():
    """Average and range chart for a stable process."""
    avgs = [4.4, 5.1, 4.9, 4.2, 5.3, 4.7, 4.5, 5.0]
    rngs = [4, 3, 5, 4, 6, 3, 4, 5]
    o = []
    for k, (vals, cl, ucl, lcl, lab, yr) in enumerate([
            (avgs, XBAR, UCL_X, LCL_X, "trung bình nhóm", (0.0, 9.0)),
            (rngs, RBAR, UCL_R, LCL_R, "khoảng biến thiên R", (0.0, 10.0))]):
        x0, y0, W, H = 84, 40 + k * 116, 424, 92
        X, Y = _mk(x0, y0, W, H, (0.5, 8.5), yr)
        o.append(_axes(x0, y0, W, H, "", lab,
                       xt=[(0.5, "1"), (7.5, "8")] if k else [(0.5, ""), (7.5, "")],
                       yt=[(0.0, "%d" % yr[0]), (1.0, "%d" % yr[1])]))
        o.append(_line(x0, Y(ucl), x0 + W, Y(ucl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(lcl), x0 + W, Y(lcl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(cl), x0 + W, Y(cl), sw=0.9, color=GREEN))
        o.append(_txt(x0 + W + 4, Y(ucl) + 2.4, "UCL", 6.0, anchor="start", color=RED))
        o.append(_txt(x0 + W + 4, Y(lcl) + 2.4, "LCL", 6.0, anchor="start", color=RED))
        o.append(_txt(x0 + W + 4, Y(cl) + 2.4, "CL", 6.0, anchor="start", color=GREEN))
        o.append(_poly([(X(i + 1), Y(v)) for i, v in enumerate(vals)], sw=1.5, color=BLUE))
        for i, v in enumerate(vals):
            o.append(_circle(X(i + 1), Y(v), 2.5, fill=BLUE, sw=0))
    o.append(_txt(330, 22, "Biểu đồ trung bình và khoảng biến thiên — quá trình ổn định", 8.0,
                  weight="600"))
    return _finish(o, 660, 268,
                   "Hình 14-5. Biểu đồ trung bình và khoảng biến thiên của một quá trình ổn định. Mọi "
                   "điểm đều nằm trong giới hạn, và chúng dao động quanh đường tâm một cách ngẫu "
                   "nhiên — không có xu hướng, không có chuỗi điểm cùng phía.",
                   "Figure 14-5. The average and range chart for a stable process. Every point lies "
                   "inside the limits, and the points wander about the centre line at random — no "
                   "trend, no run of points on one side.",
                   "Hai biểu đồ xếp dọc: trung bình nhóm và khoảng biến thiên, mỗi biểu đồ có đường "
                   "giới hạn trên, giới hạn dưới và đường tâm, các điểm đều nằm trong giới hạn.",
                   "Two stacked charts — subgroup average and range — each with upper and lower "
                   "control limits and a centre line, all points inside the limits.")


# ---------------------------------------------------------------- 14.6
def fig_14_6():
    """Four subgroups from an unstable process."""
    o = []
    hours = ["08:00", "09:00", "10:00", "11:00"]
    bells = [(4.8, 0.62), (6.9, 0.62), (2.7, 0.62), (4.8, 0.95)]
    samples = [[3.9, 5.6, 4.4, 5.1], [6.2, 7.6, 6.5, 7.1],
               [2.0, 3.4, 2.3, 3.1], [3.4, 6.1, 4.2, 6.4]]
    for i, (h, (mu, sd), vals) in enumerate(zip(hours, bells, samples)):
        yb = 34 + i * 46
        X, Y = _mk(96, yb, 380, 40, (0.0, 9.0), (0.0, 1.0))
        o.append(_txt(88, yb + 26, h, 6.6, anchor="end", color=GREY))
        o.append(_line(96, yb + 40, 476, yb + 40, sw=0.7, color="#d8d3c8"))
        pts = [(X(v), Y(_gauss(v, mu, sd) / 0.66)) for v in
               [0.0 + 0.05 * k for k in range(181)]]
        o.append(_poly(pts, sw=1.3, color=GREY))
        for v in vals:
            o.append(_circle(X(v), Y(0.06), 2.6, fill=BLUE, sw=0))
    o.append(_txt(300, 22, "Bốn nhóm lấy từ một quá trình KHÔNG ổn định", 8.0, weight="600"))
    o.append(_txt(96, 226, "giá trị đo", 6.6, anchor="start", color=GREY))
    return _finish(o, 660, 240,
                   "Hình 14-6. Cùng bốn giờ ấy nhưng quá trình đang thay đổi. Đường chuông lúc 09:00 "
                   "dịch sang phải, lúc 10:00 dịch mạnh sang trái, rồi 11:00 trở về nhưng rộng ra. "
                   "Trung bình và độ tán xạ thay đổi độc lập với nhau — đó là hai biến phải theo dõi "
                   "riêng.",
                   "Figure 14-6. The same four hours, but the process is moving. The bell shifts right "
                   "at 09:00, sharply left at 10:00, then returns at 11:00 but wider. Mean and spread "
                   "change independently — which is why they are tracked as two separate variables.",
                   "Bốn hàng đường cong chuông: hai hàng đầu dịch sang phải, hàng thứ ba dịch sang "
                   "trái, hàng thứ tư trở về giữa nhưng thấp và rộng hơn.",
                   "Four rows of bell curves: the first two shift right, the third shifts left, and "
                   "the fourth returns to the centre but lower and wider.")


# ---------------------------------------------------------------- 14.7
def fig_14_7():
    """Average and range chart for the unstable process."""
    avgs = [4.8, 8.2, 1.2, 5.0]
    rngs = [4.0, 4.0, 4.0, 9.6]
    o = []
    for k, (vals, cl, ucl, lcl, lab, yr) in enumerate([
            (avgs, XBAR, UCL_X, LCL_X, "trung bình nhóm", (0.0, 9.5)),
            (rngs, RBAR, UCL_R, LCL_R, "khoảng biến thiên R", (0.0, 10.5))]):
        x0, y0, W, H = 84, 40 + k * 116, 424, 92
        X, Y = _mk(x0, y0, W, H, (0.5, 4.5), yr)
        o.append(_axes(x0, y0, W, H, "giờ" if not k else "", lab,
                       xt=[(0.125, "08"), (0.375, "09"), (0.625, "10"), (0.875, "11")]
                       if not k else [(0.125, ""), (0.875, "")],
                       yt=[(0.0, "%d" % yr[0]), (1.0, "%d" % yr[1])]))
        o.append(_line(x0, Y(ucl), x0 + W, Y(ucl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(lcl), x0 + W, Y(lcl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(cl), x0 + W, Y(cl), sw=0.9, color=GREEN))
        o.append(_txt(x0 + W + 4, Y(ucl) + 2.4, "UCL", 6.0, anchor="start", color=RED))
        o.append(_txt(x0 + W + 4, Y(lcl) + 2.4, "LCL", 6.0, anchor="start", color=RED))
        o.append(_txt(x0 + W + 4, Y(cl) + 2.4, "CL", 6.0, anchor="start", color=GREEN))
        o.append(_poly([(X(i + 1), Y(v)) for i, v in enumerate(vals)], sw=1.5, color=BLUE))
        for i, v in enumerate(vals):
            out = v > ucl or v < lcl
            o.append(_circle(X(i + 1), Y(v), 3.2, fill=RED if out else BLUE, sw=0))
    o.append(_txt(330, 22, "Biểu đồ trung bình và khoảng biến thiên — quá trình KHÔNG ổn định",
                  8.0, weight="600"))
    return _finish(o, 660, 268,
                   "Hình 14-7. Cùng hai biểu đồ ấy cho quá trình đang thay đổi. 09:00 trung bình vượt "
                   "giới hạn trên; 10:00 tụt dưới giới hạn dưới; 11:00 trung bình trở lại bình thường "
                   "nhưng khoảng biến thiên vượt giới hạn trên. Ba giờ đầu độ tán xạ không đổi — nếu "
                   "chỉ nhìn khoảng biến thiên thì đã bỏ sót hai lần quá trình mất kiểm soát.",
                   "Figure 14-7. The same two charts for the moving process. At 09:00 the average "
                   "exceeds the upper limit; at 10:00 it falls below the lower one; at 11:00 the average "
                   "returns to normal but the range exceeds its upper limit. For the first three hours "
                   "the spread did not change — watching only the range would have missed two "
                   "excursions.",
                   "Hai biểu đồ: điểm trung bình thứ hai nằm trên giới hạn trên, điểm thứ ba dưới giới "
                   "hạn dưới, và điểm khoảng biến thiên thứ tư vượt giới hạn trên — cả ba đánh dấu đỏ.",
                   "Two charts: the second average point above the upper limit, the third below the "
                   "lower, and the fourth range point above its upper limit — all three marked in red.")


# ---------------------------------------------------------------- 14.8
def fig_14_8():
    """Histograms of the measurements, the averages and the ranges."""
    o = []
    flat = [v for r in DATA for v in r]
    panels = [
        ("80 giá trị đo", flat, [i + 0.5 for i in range(10)], 0.0, 10.0, BLUE),
        ("20 trung bình nhóm", AVGS, [3.5 + 0.5 * i for i in range(7)], 3.0, 7.0, GREEN),
        ("20 khoảng biến thiên", RNGS, [1.5 + i for i in range(7)], 1.0, 8.0, GOLD)]
    for k, (title, vals, centres, lo, hi, col) in enumerate(panels):
        x0, y0, W, H = 58 + k * 210, 52, 150, 88
        counts = []
        for c in centres:
            bw = (centres[1] - centres[0]) if len(centres) > 1 else 1.0
            counts.append(sum(1 for v in vals if abs(v - c) < bw / 2.0 + 1e-9))
        top = max(counts) * 1.12 or 1
        X, Y = _mk(x0, y0, W, H, (lo, hi), (0.0, top))
        o.append(_axes(x0, y0, W, H, title, "số lần",
                       xt=[(0.0, "%g" % lo), (1.0, "%g" % hi)],
                       yt=[(0.0, "0")]))
        bw = (hi - lo) / len(centres)
        for c, n in zip(centres, counts):
            if n:
                o.append(_rect(X(c - bw * 0.42), Y(n), X(c + bw * 0.42) - X(c - bw * 0.42),
                               Y(0) - Y(n), col, sw=0.8, stroke=INK))
    return _finish(o, 660, 206,
                   "Hình 14-8. Ba biểu đồ tần suất dựng từ chính bảng dữ liệu của ví dụ 14.7.5: 80 giá "
                   "trị đo, 20 trung bình nhóm và 20 khoảng biến thiên. Cả ba vẽ cùng tỉ lệ. Chúng có "
                   "hình dạng và độ tán xạ hoàn toàn khác nhau, nên không thể dùng lẫn các đại lượng "
                   "này cho nhau.",
                   "Figure 14-8. Three histograms built from the data table of example 14.7.5: the 80 "
                   "measurements, the 20 subgroup averages and the 20 ranges. All three are drawn to the "
                   "same scale. They have completely different shapes and spreads, so the three "
                   "quantities cannot be used interchangeably.",
                   "Ba biểu đồ cột cạnh nhau: biểu đồ giá trị đo rộng và thấp, biểu đồ trung bình hẹp "
                   "và cao, biểu đồ khoảng biến thiên lệch hẳn về phía phải.",
                   "Three bar charts side by side: the measurements wide and low, the averages narrow "
                   "and tall, the ranges skewed hard to the right.")


# ---------------------------------------------------------------- 14.9
def fig_14_9():
    """The three distributions and how their standard deviations relate."""
    x0, y0, W, H = 76, 50, 448, 122
    X, Y = _mk(x0, y0, W, H, (-1.0, 11.0), (0.0, 0.52))
    o = [_axes(x0, y0, W, H, "giá trị", "mật độ",
               xt=[(0.0, "0"), (1.0, "10")],
               yt=[(0.0, "0")])]
    for mu, sd, col, dash in ((XBAR, SDX, BLUE, ""),
                              (XBAR, SD_XBAR, GREEN, ""),
                              (RBAR, SD_R, GOLD, "5 3")):
        pts = [(X(v), Y(_gauss(v, mu, sd))) for v in [-1.0 + 0.02 * k for k in range(601)]]
        o.append(_poly(pts, sw=1.9, color=col, dash=dash))
        o.append(_line(X(mu), Y(0.0), X(mu), Y(_gauss(mu, mu, sd)), sw=0.8, dash="2 3",
                       color=col))
    o.append(_txt(X(XBAR), Y(0.50), "AVER(X) = AVER(x̄)", 6.6, color=INK))
    o.append(_legend(x0 + W - 152, y0 + 6,
                     [(BLUE, "X: SD = %.2f" % SDX, ""),
                      (GREEN, "x̄: SD = %.2f" % SD_XBAR, ""),
                      (GOLD, "R: SD = %.2f" % SD_R, "5 3")], w=148))
    o.append(_txt(x0 + 6, y0 + H + 34,
                  "SD(x̄) = SD(X)/√n  ·  AVER(R) = d₂·SD(X)  ·  SD(R) = d₃·SD(X)",
                  6.8, anchor="start", color=GREY))
    return _finish(o, 660, 226,
                   "Hình 14-9. Ba phân bố của ví dụ 14.7.5 vẽ trên cùng một trục. Phân bố của trung "
                   "bình nhóm hẹp hơn phân bố của từng giá trị đo đúng √n lần — đó là lý do biểu đồ "
                   "trung bình phát hiện được những dịch chuyển mà nhìn từng giá trị đo không thấy. "
                   "Phân bố của khoảng biến thiên lệch, nên chỉ dùng d₂ và d₃ để quy đổi.",
                   "Figure 14-9. The three distributions of example 14.7.5 on one axis. The distribution "
                   "of the subgroup average is narrower than that of a single measurement by exactly √n "
                   "— which is why the average chart detects shifts that looking at individual readings "
                   "would miss. The range distribution is skewed, so only d₂ and d₃ are used to convert "
                   "it.",
                   "Ba đường cong chuông trên một trục: đường xanh rộng nhất, đường xanh lá hẹp và cao "
                   "hơn ở cùng tâm, đường vàng nét đứt lệch sang trái và rộng.",
                   "Three bell curves on one axis: the widest in blue, a narrower and taller green one "
                   "at the same centre, and a dashed gold one shifted left and broad.")


# ---------------------------------------------------------------- 14.10
def fig_14_10():
    """The finished control chart for the worked example."""
    o = []
    for k, (vals, cl, ucl, lcl, lab, yr) in enumerate([
            (AVGS, XBAR, UCL_X, LCL_X, "trung bình nhóm x̄", (0.0, 9.0)),
            (RNGS, RBAR, UCL_R, LCL_R, "khoảng biến thiên R", (0.0, 10.5))]):
        x0, y0, W, H = 84, 44 + k * 118, 430, 94
        X, Y = _mk(x0, y0, W, H, (0.5, 20.5), yr)
        o.append(_axes(x0, y0, W, H, "số thứ tự nhóm" if not k else "", lab,
                       xt=[(0.5 / 20.0, "1"), (19.5 / 20.0, "20")] if not k
                       else [(0.5 / 20.0, ""), (19.5 / 20.0, "")],
                       yt=[(0.0, "%g" % yr[0]), (1.0, "%g" % yr[1])]))
        o.append(_line(x0, Y(ucl), x0 + W, Y(ucl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(lcl), x0 + W, Y(lcl), sw=1.0, dash="5 3", color=RED))
        o.append(_line(x0, Y(cl), x0 + W, Y(cl), sw=0.9, color=GREEN))
        o.append(_txt(x0 + W + 5, Y(ucl) + 2.4, "UCL %.3f" % ucl, 5.8, anchor="start",
                      color=RED))
        o.append(_txt(x0 + W + 5, Y(lcl) + 2.4, "LCL %.3f" % lcl, 5.8, anchor="start",
                      color=RED))
        o.append(_txt(x0 + W + 5, Y(cl) + 2.4, "CL %.2f" % cl, 5.8, anchor="start",
                      color=GREEN))
        o.append(_poly([(X(i + 1), Y(v)) for i, v in enumerate(vals)], sw=1.4, color=BLUE))
        for i, v in enumerate(vals):
            o.append(_circle(X(i + 1), Y(v), 2.3, fill=BLUE, sw=0))
    o.append(_txt(330, 22, "Biểu đồ kiểm soát của ví dụ 14.7.5 — dựng từ bảng 14.1", 8.0,
                  weight="600"))
    return _finish(o, 660, 272,
                   "Hình 14-10. Biểu đồ kiểm soát dựng từ đúng 20 nhóm của bảng 14.1, với giới hạn "
                   "tính theo cả hai cách. Cả 20 trung bình nằm trong khoảng 1,811 đến 7,715 và cả 20 "
                   "khoảng biến thiên nằm dưới 9,243, nên quá trình được coi là ổn định. Lưu ý giới "
                   "hạn dưới của khoảng biến thiên bằng 0 vì R không thể âm.",
                   "Figure 14-10. The control chart built from the twenty subgroups of table 14.1, with "
                   "limits computed both ways. All twenty averages fall between 1.811 and 7.715 and all "
                   "twenty ranges fall below 9.243, so the process is judged stable. Note that the lower "
                   "range limit is 0 because R cannot be negative.",
                   "Hai biểu đồ xếp dọc với 20 điểm mỗi biểu đồ, đường giới hạn trên và dưới màu đỏ, "
                   "đường tâm màu xanh lá, tất cả các điểm đều nằm trong giới hạn.",
                   "Two stacked charts with twenty points each, red upper and lower limits, a green "
                   "centre line, every point inside the limits.")


# ---------------------------------------------------------------- 14.11
def fig_14_11():
    """The decision logic behind a control chart."""
    o = [_txt(330, 20, "Lô-gic của một biểu đồ kiểm soát", 8.4, weight="600")]
    o.append(_box(232, 36, 196, 34, "lấy mẫu n giá trị, mỗi giờ một nhóm", fill="#eef3fb",
                  size=6.8))
    o.append(_box(232, 92, 196, 34, "tính trung bình x̄ và khoảng biến thiên R", fill="#eef3fb",
                  size=6.8))
    o.append(_arrow(330, 70, 330, 90, sw=1.1))
    o.append(_box(232, 148, 196, 34, "so với giới hạn đã tính trước", fill="#eef3fb", size=6.8))
    o.append(_arrow(330, 126, 330, 146, sw=1.1))
    o.append(_box(300, 204, 150, 34, "nằm trong giới hạn?", fill="#f6ecd8", size=7.0))
    o.append(_arrow(330, 182, 330, 202, sw=1.1))

    o.append(_poly([(300, 221), (150, 221), (150, 168)], sw=1.1))
    o.append(_arrow(150, 190, 150, 170, sw=1.1))
    o.append(_txt(158, 216, "có", 6.8, anchor="start", color=GREEN))
    o.append(_box(60, 110, 150, 56, "quá trình ổn định", fill="#e6f0e8", size=7.0,
                  sub="chỉ còn nguyên nhân ngẫu nhiên"))
    o.append(_txt(150, 240, "muốn giảm tán xạ: đổi quá trình", 6.2, color=GREY))

    o.append(_poly([(450, 221), (546, 221), (546, 168)], sw=1.1))
    o.append(_arrow(546, 190, 546, 170, sw=1.1))
    o.append(_txt(470, 216, "không", 6.8, anchor="start", color=RED))
    o.append(_box(470, 104, 156, 62, "tìm nguyên nhân gán được", fill="#f7e3e0", size=6.8,
                  sub="máy, vật liệu, phương pháp"))
    o.append(_txt(546, 240, "sửa nguyên nhân, không đổi quá trình", 6.2, color=GREY))
    return _finish(o, 660, 258,
                   "Hình 14-11. Lô-gic của biểu đồ kiểm soát. Mọi điểm nằm trong giới hạn nghĩa là "
                   "quá trình chỉ còn biến thiên ngẫu nhiên — muốn giảm nữa thì phải thay đổi chính "
                   "quá trình. Một điểm ra ngoài giới hạn nghĩa là có nguyên nhân gán được — phải tìm "
                   "và sửa nguyên nhân đó, không phải đổi quá trình. Hai việc này khác nhau về bản "
                   "chất và không thể thay thế nhau.",
                   "Figure 14-11. The logic of a control chart. Every point inside the limits means the "
                   "process carries only random variation — to reduce it further you must change the "
                   "process itself. A point outside the limits means an assignable cause — find it and "
                   "fix it, do not change the process. The two responses are different in kind and "
                   "cannot substitute for each other.",
                   "Lưu đồ quyết định từ lấy mẫu, tính trung bình và khoảng biến thiên, so với giới "
                   "hạn, rồi rẽ hai nhánh: trong giới hạn thì quá trình ổn định, ngoài giới hạn thì "
                   "tìm nguyên nhân gán được.",
                   "A decision flow from sampling, through computing the average and range and "
                   "comparing with the limits, branching into a stable process or an assignable cause.")


FIGURES = [fig_14_1, fig_14_2, fig_14_3, fig_14_4, fig_14_5, fig_14_6,
           fig_14_7, fig_14_8, fig_14_9, fig_14_10, fig_14_11]
