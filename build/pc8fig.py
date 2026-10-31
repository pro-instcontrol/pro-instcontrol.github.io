# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 8 — Tuning of PID Controllers."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- helpers
def _shade(x0, y0, W, H, fn_hi, fn_lo, t0, t1, fill="#f6e7c8", n=121):
    """Fill the band between two functions of t over [t0, t1]."""
    top, bot = [], []
    for i in range(n):
        t = t0 + (t1 - t0) * i / (n - 1.0)
        px = x0 + W * t
        top.append((px, y0 + H * (1 - fn_hi(t))))
        bot.append((px, y0 + H * (1 - fn_lo(t))))
    pts = top + bot[::-1]
    d = "M " + " L ".join("%s %s" % (round(a, 1), round(b, 1)) for a, b in pts) + " Z"
    return _path(d, fill=fill, sw=0, color=fill)


def _second_order(t, w=4.0):
    """Critically damped unit step response."""
    if t <= 0:
        return 0.0
    return 1.0 - (1.0 + w * t) * math.exp(-w * t)


def _lag(t, L, T):
    """Dead time then first-order rise."""
    if t <= L:
        return 0.0
    return 1.0 - math.exp(-(t - L) / T)


# ---------------------------------------------------------------- 8.1
def fig_8_1():
    """IAE: the area between the SP and PV trends is what ZN minimises."""
    x0, y0, W, H = 66, 46, 520, 128
    t0 = 0.12
    o = [_axes(x0, y0, W, H, "thời gian", "PV / SP",
               xt=[(0, "0"), (0.5, ""), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_shade(x0, y0, W, H, lambda t: 1.0, lambda t: _second_order(t - t0),
                    t0, 1.0, fill="#f3e4c4"))
    # the SP step itself: flat at zero, up at t0, flat at 100 %
    o.append(_line(x0, y0 + H, x0 + W * t0, y0 + H, sw=1.5, color=INK))
    o.append(_line(x0 + W * t0, y0 + H, x0 + W * t0, y0, sw=1.5, color=INK))
    o.append(_line(x0 + W * t0, y0, x0 + W, y0, sw=1.5, color=INK, dash="4 3"))
    o.append(_curve(lambda t: _second_order(t - t0), x0, y0, W, H, n=241,
                    xr=(0, 1), yr=(0, 1), color=BLUE, sw=2.0))
    o.append(_txt(x0 + W * t0 + 8, y0 - 7, "SP", 8, anchor="start", color=GREY))
    o.append(_txt(x0 + W * 0.30, y0 + H * 0.72, "diện tích sai lệch", 8.5,
                  anchor="start", color="#8a6a1e"))
    o.append(_txt(x0 + W * 0.30, y0 + H * 0.84, "IAE = ∫|ERR| dt  →  cực tiểu", 8,
                  anchor="start", color="#8a6a1e"))
    o.append(_txt(x0 + W * 0.58, y0 + H * 0.30, "PV", 8.5, anchor="start", color=BLUE))
    return _finish(o, 660, 214,
                   "Hình 8-1. Tích phân sai lệch (IAE): mục tiêu của chỉnh định Ziegler-Nichols là làm "
                   "diện tích giữa đường SP và đường PV nhỏ nhất.",
                   "Figure 8-1. Integral of the error: the Ziegler-Nichols objective is to minimise the "
                   "area between the SP and PV trends.",
                   "Đồ thị bậc thang điểm đặt và đáp ứng của PV; vùng giữa hai đường được tô để chỉ "
                   "diện tích sai lệch cần cực tiểu.",
                   "A set-point step with the PV response; the band between the two traces is shaded to "
                   "show the error area to be minimised.")


# ---------------------------------------------------------------- 8.2
def fig_8_2():
    """ISE weights the large early error far more heavily."""
    x0, y0, W, H = 66, 46, 520, 128
    t0 = 0.10
    o = [_axes(x0, y0, W, H, "thời gian", "|ERR| và ERR²",
               xt=[(0, "0"), (0.5, ""), (1, "")],
               yt=[(0, "0"), (0.5, "0,5"), (1, "1")])]
    o.append(_curve(lambda t: abs(1.0 - _second_order(t - t0)) if t >= t0 else 0.0,
                    x0, y0, W, H, n=241, xr=(0, 1), yr=(0, 1), color=BLUE, sw=2.0))
    o.append(_curve(lambda t: (1.0 - _second_order(t - t0)) ** 2 if t >= t0 else 0.0,
                    x0, y0, W, H, n=241, xr=(0, 1), yr=(0, 1), color=RED, sw=2.0))
    o.append(_legend_h(x0 + 10, y0 + H + 44,
                       [(BLUE, "|ERR| — IAE cân đều", ""),
                        (RED, "ERR² — ISE dồn trọng số về sai lệch lớn", "")], gap=34))
    o.append(_txt(x0 + W * 0.40, y0 + H * 0.92, "vùng này bị ISE phạt nặng", 8,
                  anchor="start", color=RED))
    return _finish(o, 660, 232,
                   "Hình 8-2. Tích phân sai lệch bình phương (ISE): cùng một sai lệch nhưng sai lệch lớn "
                   "bị phạt nặng hơn nhiều.",
                   "Figure 8-2. Integral of the error squared: the same error history, but large "
                   "deviations are punished far more heavily.",
                   "Hai đường trên cùng đồ thị: đường xanh là độ lớn sai lệch, đường đỏ là bình phương "
                   "sai lệch; đường đỏ dốc mạnh ở vùng sai lệch lớn rồi tắt rất nhanh.",
                   "Two curves on one plot: the blue is the magnitude of the error, the red its square; "
                   "the red rises steeply where the error is large and dies away quickly.")


# ---------------------------------------------------------------- 8.3
def fig_8_3():
    """The open-loop reaction curve and the three numbers read off it."""
    x0, y0, W, H = 78, 50, 494, 122
    L, T = 0.15, 0.19
    o = [_axes(x0, y0, W, H, "thời gian (phút)", "PV (%)",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.632, "63,2"), (1, "100")])]
    o.append(_curve(lambda t: _lag(t, L, T), x0, y0, W, H, n=301, xr=(0, 1), yr=(0, 1),
                    color=BLUE, sw=2.0))

    # the point of inflection, with the tangent that carries the slope N
    t_in = L + T
    y_in = _lag(t_in, L, T)
    slope = math.exp(-1.0) / T
    o.append(_line(x0 + W * (t_in - 0.13), y0 + H * (1 - (y_in - slope * 0.13)),
                   x0 + W * (t_in + 0.17), y0 + H * (1 - (y_in + slope * 0.17)),
                   sw=1.3, color=RED))
    o.append(_circle(x0 + W * t_in, y0 + H * (1 - y_in), 2.8, fill=RED, color=RED))
    o.append(_txt(x0 + W * t_in - 8, y0 + H * (1 - y_in) - 9, "điểm uốn", 7,
                  anchor="end", color=RED))
    o.append(_txt(x0 + W * (t_in + 0.17) + 5, y0 + H * (1 - (y_in + slope * 0.17)) - 3,
                  "N (%/phút)", 7.5, anchor="start", color=RED))

    # 63.2 % of the final value, measured from the end of L
    y63 = y0 + H * (1 - 0.632)
    o.append(_line(x0, y63, x0 + W * (L + T), y63, sw=0.7, dash="2 3", color=GREY))
    o.append(_line(x0 + W * (L + T), y63, x0 + W * (L + T), y0 + H, sw=0.7, dash="2 3",
                   color=GREY))
    o.append(_arrow(x0 + W * L, y63 + 11, x0 + W * (L + T), y63 + 11, sw=0.9,
                    color=GOLD, head="a5"))
    o.append(_arrow(x0 + W * (L + T), y63 + 11, x0 + W * L, y63 + 11, sw=0.9,
                    color=GOLD, head="a5"))
    o.append(_txt(x0 + W * (L + T / 2.0), y63 + 5, "LTC", 7.5, color=GOLD))

    # L bracket under the axis
    o.append(_line(x0, y0 + H + 18, x0 + W * L, y0 + H + 18, sw=1.0, color=INK))
    o.append(_line(x0, y0 + H + 14, x0, y0 + H + 22, sw=0.8))
    o.append(_line(x0 + W * L, y0 + H + 14, x0 + W * L, y0 + H + 22, sw=0.8))
    o.append(_txt(x0 + W * L / 2.0, y0 + H + 32, "L", 8.5, color=INK))
    o.append(_txt(x0 + W * L + 8, y0 + H - 14, "chưa thấy thay đổi", 7, anchor="start",
                  color=GREY))
    return _finish(o, 660, 226,
                   "Hình 8-3. Đường cong phản ứng vòng hở: độ trễ hiệu dụng L, độ dốc cực đại N và hằng "
                   "số thời gian vòng LTC.",
                   "Figure 8-3. The open-loop reaction curve: effective lag L, maximum slope N and the "
                   "loop time constant.",
                   "Đồ thị đáp ứng bậc thang: PV phẳng trong khoảng L rồi tăng theo hàm mũ; tiếp tuyến "
                   "tại điểm uốn cho độ dốc N, đường 63,2 phần trăm cho hằng số thời gian vòng.",
                   "Step response plot: PV is flat for L then rises exponentially; the tangent at the "
                   "inflection gives the slope N, and the 63.2 per cent line gives the loop time "
                   "constant.")


# ---------------------------------------------------------------- 8.4
def fig_8_4():
    """Method (1): only N and L are needed, and they enter every formula."""
    o = [_rect(24, 20, 612, 96, "#fbfaf6", sw=0.8, stroke="#ddd7c8")]
    o.append(_txt(330, 46, "P:    K_c = (OP% / (N%·min⁻¹ × L min))", 11))
    o.append(_txt(330, 72, "PI:   K_c = 0,9 × (OP% / (N × L)),   T_int = 3 · L", 11))
    o.append(_txt(330, 98, "PID:  K_c = 1,2 × (OP% / (N × L)),   T_int = 2 · L,   T_der = 0,5 · L",
                  11))
    return _finish(o, 660, 132,
                   "Hình 8-4. Ba bộ công thức của phương pháp Ziegler-Nichols vòng hở (1), chỉ dùng N và L.",
                   "Figure 8-4. The three formula sets of Ziegler-Nichols open-loop method (1), which "
                   "need only N and L.",
                   "Khung công thức: hệ số khuếch đại bằng OP phần trăm chia tích N nhân L, nhân thêm "
                   "0,9 cho PI và 1,2 cho PID; thời gian tích phân bằng 3L hoặc 2L, thời gian vi phân "
                   "bằng 0,5L.",
                   "A formula panel: the gain is OP per cent divided by N times L, scaled by 0.9 for PI "
                   "and 1.2 for PID; the integral time is 3L or 2L and the derivative time 0.5L.")


# ---------------------------------------------------------------- 8.5
def fig_8_5():
    """Method (2): the tangent through the point of inflection, and PGU."""
    x0, y0, W, H = 78, 52, 470, 120
    L, T = 0.20, 0.22
    t_in = L + T
    y_in = _lag(t_in, L, T)
    slope = math.exp(-1.0) / T

    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (1, "100")])]
    o.append(_curve(lambda t: _lag(t, L, T), x0, y0, W, H, n=301, xr=(0, 1), yr=(0, 1),
                    color=BLUE, sw=2.0))
    # the tangent continued back to t = 0
    xa = 0.0
    ya = y_in - slope * (t_in - xa)
    o.append(_line(x0, y0 + H * (1 - ya), x0 + W * (t_in + 0.18),
                   y0 + H * (1 - (y_in + slope * 0.18)), sw=1.2, color=RED, dash="5 3"))
    o.append(_circle(x0 + W * t_in, y0 + H * (1 - y_in), 2.6, fill=RED, color=RED))
    o.append(_txt(x0 + W * t_in + 6, y0 + H * (1 - y_in) - 6, "POI", 7.5, anchor="start",
                  color=RED))

    # delta C on the y axis and delta V as a label
    o.append(_line(x0 - 6, y0 + H * (1 - ya), x0 + 6, y0 + H * (1 - ya), sw=1.2, color=RED))
    o.append(_txt(x0 - 8, y0 + H * (1 - ya) - 4, "∆C", 8.5, anchor="end", color=RED))
    o.append(_txt(x0 + W * 0.50, y0 + H * 0.50, "∆V = độ dịch van (%)", 8,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W * 0.50, y0 + H * 0.66, "PG_u = 2 · ∆V / ∆C", 9,
                  anchor="start", color=INK))
    o.append(_txt(x0 + W * 0.50, y0 + H * 0.82, "T_u = 4 · L", 9, anchor="start", color=INK))

    # L bracket
    o.append(_line(x0, y0 + H + 16, x0 + W * L, y0 + H + 16, sw=1.0))
    o.append(_txt(x0 + W * L / 2.0, y0 + H + 30, "L", 8.5, color=INK))
    return _finish(o, 660, 232,
                   "Hình 8-5. Phương pháp vòng hở (2): tiếp tuyến qua điểm uốn cắt trục tung cho ∆C, từ "
                   "đó tính PG_u và T_u.",
                   "Figure 8-5. Open-loop method (2): the tangent through the point of inflection meets "
                   "the vertical axis at delta-C, giving PG-u and T-u.",
                   "Đồ thị đáp ứng và một tiếp tuyến nét đứt kéo ngược về trục tung; giao điểm với trục "
                   "tung đánh dấu delta C, khoảng phẳng ban đầu đánh dấu L.",
                   "A response curve with a dashed tangent extended back to the vertical axis; its "
                   "intercept is delta-C and the initial flat interval is L.")


# ---------------------------------------------------------------- 8.6
def fig_8_6():
    """A first-order lag: 63.2 % per time constant, never quite 100 %."""
    x0, y0, W, H = 70, 50, 500, 126
    T = 0.18
    o = [_axes(x0, y0, W, H, "thời gian (số hằng số thời gian τ)", "PV (%)",
               xt=[(0, "0"), (T, "1τ"), (2 * T, "2τ"), (3 * T, "3τ"), (4 * T, "4τ"), (5 * T, "5τ")],
               yt=[(0, "0"), (0.632, "63,2"), (0.865, "86,5"), (1, "100")])]
    o.append(_curve(lambda t: 1 - math.exp(-t / T), x0, y0, W, H, n=241, xr=(0, 0.95), yr=(0, 1),
                    color=BLUE, sw=2.0))
    # tangent at the origin reaches 100 % at one time constant
    o.append(_line(x0, y0 + H, x0 + W * T, y0, sw=1.2, color=RED, dash="5 3"))
    o.append(_txt(x0 + W * T + 6, y0 + 22, "tiếp tuyến tại gốc", 7.5, anchor="start", color=RED))
    for frac, lab in ((0.632, "63,2 %"), (0.865, "86,5 %"), (0.95, "95 %")):
        o.append(_line(x0, y0 + H * (1 - frac), x0 + W * T * (-math.log(1 - frac)),
                       y0 + H * (1 - frac), sw=0.7, dash="2 3", color=GREY))
    o.append(_txt(x0 + W * 0.42, y0 + H * 0.52, "mỗi khoảng τ lấy đi 63,2 %", 8,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W * 0.42, y0 + H * 0.62, "phần còn lại — không bao giờ tới 100 %", 8,
                  anchor="start", color=GREY))
    return _finish(o, 660, 224,
                   "Hình 8-6. Đáp ứng của khâu trễ bậc một với đầu vào bậc thang: sau một hằng số thời "
                   "gian đạt 63,2 %, sau hai đạt 86,5 %, sau ba đạt 95 %.",
                   "Figure 8-6. First-order lag response to a step: 63.2 % after one time constant, "
                   "86.5 % after two, 95 % after three.",
                   "Đồ thị hàm mũ tiến dần tới 100 phần trăm; các đường chấm đánh dấu mức 63,2, 86,5 "
                   "và 95 phần trăm tại một, hai và ba hằng số thời gian.",
                   "An exponential curve approaching 100 per cent; dotted lines mark the 63.2, 86.5 and "
                   "95 per cent levels at one, two and three time constants.")


# ---------------------------------------------------------------- 8.7
def fig_8_7():
    """The LTC method reads three numbers straight off the curve."""
    o = [_rect(24, 20, 612, 92, "#fbfaf6", sw=0.8, stroke="#ddd7c8")]
    o.append(_txt(150, 46, "PG = 1 / K_process", 12))
    o.append(_txt(390, 46, "IG = LTC", 12))
    o.append(_txt(520, 46, "DG = 0,25 · IG", 12))
    o.append(_txt(330, 72, "K_process lấy từ độ cao cuối cùng chia cho bước thay đổi đầu vào", 8.5,
                  color=GREY))
    o.append(_txt(330, 96, "LTC đo từ lúc PV bắt đầu đổi tới mức 63,2 % của độ thay đổi tổng", 8.5,
                  color=GREY))
    return _finish(o, 660, 130,
                   "Hình 8-7. Phương pháp hằng số thời gian vòng: ba tham số PG, IG, DG đọc trực tiếp "
                   "trên đường cong.",
                   "Figure 8-7. The loop time constant method: PG, IG and DG are read straight off the "
                   "curve.",
                   "Khung công thức: hệ số tỉ lệ bằng nghịch đảo hệ số khuếch đại quá trình, hệ số tích "
                   "phân bằng hằng số thời gian vòng, hệ số vi phân bằng một phần tư hệ số tích phân.",
                   "A formula panel: the proportional gain is the reciprocal of the process gain, the "
                   "integral gain equals the loop time constant, and the derivative gain is a quarter "
                   "of the integral gain.")


# ---------------------------------------------------------------- 8.8
def fig_8_8():
    """Damped cycling: the decay ratio between the first two overshoots."""
    x0, y0, W, H = 66, 48, 520, 126
    d, wn = 0.16, 2 * math.pi * 1.55

    def resp(t):
        if t < 0:
            return 0.0
        wd = wn * math.sqrt(1 - d * d)
        return 1 - math.exp(-d * wn * t) * (math.cos(wd * t) + d / math.sqrt(1 - d * d)
                                            * math.sin(wd * t))

    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (1, "100")])]
    o.append(_line(x0, y0 + H, x0 + W, y0 + H, sw=1.4, color=INK))
    o.append(_curve(resp, x0, y0, W, H, n=361, xr=(0, 1), yr=(0, 1.55), color=BLUE, sw=2.0))
    o.append(_line(x0, y0, x0 + W, y0, sw=1.1, color=GREY, dash="4 3"))

    # first and second peak
    wd = wn * math.sqrt(1 - d * d)
    t1 = math.pi / wd
    t2 = 3 * math.pi / wd
    for t, lab in ((t1, "đỉnh 1"), (t2, "đỉnh 2")):
        v = resp(t)
        o.append(_circle(x0 + W * t, y0 + H * (1 - v / 1.55), 2.8, fill=RED, color=RED))
        o.append(_txt(x0 + W * t, y0 + H * (1 - v / 1.55) - 8, lab, 7.5, color=RED))
    o.append(_line(x0 + W * t1, y0 + H * 0.86, x0 + W * t2, y0 + H * 0.86, sw=1.0,
                   color=GOLD))
    o.append(_txt(x0 + W * (t1 + t2) / 2.0, y0 + H * 0.86 + 13, "P_d", 8.5, color=GOLD))
    o.append(_txt(x0 + W * 0.66, y0 + H * 0.24, "P = đỉnh 1 / đỉnh 2", 8.5,
                  anchor="start", color=INK))
    return _finish(o, 660, 226,
                   "Hình 8-8. Dao động tắt dần: tỉ số tắt P là tỉ số giữa biên độ đỉnh thứ nhất và đỉnh "
                   "thứ hai, P_d là chu kỳ tắt dần.",
                   "Figure 8-8. Damped oscillation: the decay ratio P is the first peak divided by the "
                   "second, and P-d is the damped period.",
                   "Đồ thị dao động tắt dần quanh giá trị cuối; hai đỉnh đầu được đánh dấu, khoảng cách "
                   "giữa chúng là chu kỳ tắt dần, tỉ số độ cao hai đỉnh là tỉ số tắt.",
                   "A decaying oscillation about its final value; the first two peaks are marked, the "
                   "distance between them is the damped period and the ratio of their heights is the "
                   "decay ratio.")


# ---------------------------------------------------------------- 8.9
def fig_8_9():
    """% overshoot against damping ratio — the second-order relation."""
    x0, y0, W, H = 72, 48, 500, 128

    def os_of(d):
        if d <= 0.0005:
            return 100.0
        if d >= 0.9995:
            return 0.0
        return 100.0 * math.exp(-math.pi * d / math.sqrt(1 - d * d))

    o = [_axes(x0, y0, W, H, "tỉ số tắt δ", "% quá điều chỉnh",
               xt=[(0, "0"), (0.2, "0,2"), (0.4, "0,4"), (0.6, "0,6"), (0.8, "0,8"), (1, "1,0")],
               yt=[(0, "0"), (0.2, "20"), (0.4, "40"), (0.6, "60"), (0.8, "80"), (1, "100")])]
    o.append(_curve(lambda d: os_of(d) / 100.0, x0, y0, W, H, n=241, xr=(0.001, 1.0),
                    yr=(0, 1), color=BLUE, sw=2.0))
    for d in (0.3, 0.5, 0.7):
        v = os_of(d)
        o.append(_line(x0 + W * d, y0 + H * (1 - v / 100.0), x0 + W * d, y0 + H, sw=0.7,
                       dash="2 3", color=GREY))
        o.append(_circle(x0 + W * d, y0 + H * (1 - v / 100.0), 2.4, fill=RED, color=RED))
        o.append(_txt(x0 + W * d + 5, y0 + H * (1 - v / 100.0) + 14,
                      "δ = %s → %.0f %%" % (("%.1f" % d).replace(".", ","), v), 7,
                      anchor="start", color=RED))
    o.append(_txt(x0 + W * 0.42, y0 + H * 0.30, "%OS = 100 · exp(−πδ / √(1−δ²))", 8.5,
                  anchor="start", color=GREY))
    return _finish(o, 660, 228,
                   "Hình 8-9. Quan hệ giữa phần trăm quá điều chỉnh và tỉ số tắt của một hệ bậc hai trội.",
                   "Figure 8-9. Percentage overshoot against damping ratio for a system with a dominant "
                   "second-order response.",
                   "Đường cong giảm từ 100 phần trăm quá điều chỉnh ở tỉ số tắt bằng 0 xuống 0 ở tỉ số "
                   "tắt bằng 1; ba điểm mẫu ở 0,3, 0,5 và 0,7 được đánh dấu.",
                   "A curve falling from 100 per cent overshoot at zero damping to zero at unit "
                   "damping; three sample points at 0.3, 0.5 and 0.7 are marked.")


# ---------------------------------------------------------------- 8.10
def fig_8_10():
    """Pu/P read from the overshoot: the Stiekema chart, computed."""
    x0, y0, W, H = 72, 48, 500, 128

    def rd_of_os(os_pct):
        """Rd = Pu/P = sqrt(1 - delta^2) with delta from the overshoot."""
        lnos = math.log(os_pct / 100.0)          # negative
        delta = -lnos / math.sqrt(math.pi ** 2 + lnos ** 2)
        return math.sqrt(1 - delta * delta)

    o = [_axes(x0, y0, W, H, "% quá điều chỉnh", "R_d = P_u / P",
               xt=[(0, "1"), (0.25, "3"), (0.5, "10"), (0.75, "30"), (1, "100")],
               yt=[(0, "0"), (0.25, "0,25"), (0.5, "0,50"), (0.75, "0,75"), (1, "1,00")])]
    # x is log10(OS) mapped from 0 (1 %) to 1 (100 %)
    o.append(_curve(lambda u: rd_of_os(10 ** u), x0, y0, W, H, n=241, xr=(0.0, 2.0),
                    yr=(0, 1), color=BLUE, sw=2.0))
    for u, lab in ((math.log10(5), "5 %"), (math.log10(10), "10 %"), (math.log10(25), "25 %")):
        v = rd_of_os(10 ** u)
        o.append(_circle(x0 + W * u / 2.0, y0 + H * (1 - v), 2.4, fill=RED, color=RED))
        o.append(_txt(x0 + W * u / 2.0 + 6, y0 + H * (1 - v) + 14,
                      "%s → %s" % (lab, ("%.2f" % v).replace(".", ",")), 7,
                      anchor="start", color=RED))
    o.append(_txt(x0 + 14, y0 + H * 0.86, "R_d = √(1 − δ²)", 9, anchor="start",
                  color=GREY))
    return _finish(o, 660, 228,
                   "Hình 8-10. Đọc chu kỳ tới hạn P_u từ chu kỳ tắt dần P thông qua R_d = P_u/P, tính từ "
                   "phần trăm quá điều chỉnh.",
                   "Figure 8-10. Reading the ultimate period from the damped period through R-d, "
                   "computed from the percentage overshoot.",
                   "Đường cong R_d giảm từ 1 ở 1 phần trăm quá điều chỉnh xuống khoảng 0,6 ở 25 phần "
                   "trăm; trục hoành theo thang logarit.",
                   "A curve of R-d falling from 1 at one per cent overshoot to about 0.6 at 25 per "
                   "cent; the horizontal axis is logarithmic.")


# ---------------------------------------------------------------- 8.11
def fig_8_11():
    """Dependent (ISA) and independent gains differ in what the gain multiplies."""
    o = [_txt(160, 26, "ISA — độ lợi phụ thuộc", 9, color=INK),
         _txt(496, 26, "độ lợi độc lập", 9, color=INK)]

    # ISA: Kc multiplies the whole bracket
    o.append(_box(24, 44, 60, 26, "E", size=8.5))
    o.append(_arrow(84, 57, 108, 57))
    o.append(_box(110, 38, 74, 38, "K_c", size=9))
    o.append(_arrow(184, 57, 208, 57))
    o.append(_box(210, 38, 108, 38, "P + I + D\n(bên trong ngoặc)", size=7.2))
    o.append(_arrow(318, 57, 336, 57))
    o.append(_txt(340, 61, "CV", 8.5, anchor="start"))

    # Independent: three separate gains
    o.append(_box(386, 44, 52, 26, "E", size=8.5))
    o.append(_line(438, 57, 458, 57))
    o.append(_line(458, 22, 458, 92))
    for y, lab in ((22, "K_p"), (57, "K_i"), (92, "K_d")):
        o.append(_arrow(458, y, 472, y, sw=1))
        o.append(_box(474, y - 13, 58, 26, lab, size=8.5))
        o.append(_line(532, y, 552, y))
    o.append(_line(552, 22, 552, 92))
    o.append(_node(570, 57, "Σ", r=13))
    o.append(_arrow(583, 57, 606, 57))
    o.append(_txt(610, 61, "CV", 8.5, anchor="start"))

    o.append(_txt(24, 122, "đổi K_c → đổi cả ba khâu", 7.5, anchor="start", color=GREY))
    o.append(_txt(386, 122, "đổi K_p, K_i, K_d riêng rẽ", 7.5, anchor="start", color=GREY))
    return _finish(o, 660, 140,
                   "Hình 8-11. So sánh phương trình ISA (độ lợi phụ thuộc) và phương trình độ lợi độc lập.",
                   "Figure 8-11. The ISA (dependent-gain) equation against the independent-gain "
                   "equation.",
                   "Hai sơ đồ cạnh nhau: bên trái một hệ số K_c nhân cả cụm P cộng I cộng D; bên phải "
                   "ba hệ số K_p, K_i, K_d riêng biệt cùng cộng vào một điểm.",
                   "Two diagrams side by side: on the left one gain K-sub-c multiplies the whole P plus "
                   "I plus D bracket; on the right three separate gains K-sub-p, K-sub-i and K-sub-d "
                   "sum into one point.")
