# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 10 — Feedforward Control."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- helpers
def _sim_pi(ts, dt, dist, kp, ti, tau=1.2, dead=0.3, ff=False, ff_gain=1.0):
    """A first-order process under a PI controller, with or without feedforward."""
    n = len(ts)
    y = [0.0] * n
    u = 0.0
    integ = 0.0
    buf = [0.0] * int(dead / dt + 1)
    for i, t in enumerate(ts):
        d = dist(t)
        # the compensator acts at the process input, alongside the disturbance
        ffd = ff_gain * d if ff else 0.0
        ud = buf.pop(0)
        buf.append(u)
        y[i] = y[i - 1] + dt * ((ud + d + ffd - y[i - 1]) / tau) if i else 0.0
        e = 0.0 - y[i]
        integ += e * dt
        u = kp * (e + integ / ti)
    return y


# ---------------------------------------------------------------- 10.1
def fig_10_2():
    """Manual feedforward: a human closes the loop."""
    o = [_txt(153, 22, "nhiễu", 8.5),
         _arrow(153, 30, 153, 38)]
    o.append(_box(98, 40, 110, 36, "QUÁ TRÌNH", size=8.5))
    o.append(_arrow(208, 58, 262, 58))
    o.append(_txt(266, 62, "PV", 8.5, anchor="start"))

    # the operator watches PV and acts on the MV
    o.append(_arrow(230, 58, 230, 118))
    o.append(_txt(236, 92, "quan sát", 7, anchor="start", color=GREY))
    o.append(_box(196, 120, 96, 40, "NGƯỜI\nVẬN HÀNH", size=7.4, fill="#f6efe0"))
    o.append(_line(196, 140, 44, 140))
    o.append(_line(44, 140, 44, 58))
    o.append(_arrow(44, 58, 96, 58))
    o.append(_txt(14, 144, "MV", 8.5, anchor="start"))
    o.append(_txt(90, 154, "điều chỉnh MV bằng tay", 7.2, anchor="start", color=GREY))

    o.append(_txt(300, 62, "không có vòng phản hồi nào", 7.4, anchor="start", color=GREY))
    o.append(_txt(300, 76, "sai số do người gây ra sẽ tồn tại", 7.4, anchor="start", color=GREY))
    return _finish(o, 660, 172,
                   "Hình 10-2. Điều khiển theo hướng bằng tay: người vận hành đo nhiễu, dựa vào hiểu "
                   "biết quá trình để chỉnh biến điều khiển.",
                   "Figure 10-2. Manual feedforward: the operator measures the disturbance and adjusts "
                   "the manipulated variable from process knowledge.",
                   "Sơ đồ: nhiễu vào quá trình, PV ra; người vận hành quan sát PV và tự chỉnh MV; không "
                   "có vòng phản hồi tự động.",
                   "Diagram: the disturbance enters the process and PV leaves it; the operator watches "
                   "PV and adjusts MV by hand; there is no automatic feedback loop.")


# ---------------------------------------------------------------- 10.2
def fig_10_3():
    """Automatic feedforward: the disturbance is measured before it arrives."""
    o = [_txt(14, 52, "nhiễu đo được", 8, anchor="start")]
    o.append(_arrow(96, 48, 150, 48))
    o.append(_circle(162, 48, 2.8, fill=INK, color=INK))
    o.append(_line(162, 48, 162, 120))
    o.append(_arrow(162, 120, 196, 120))
    o.append(_box(198, 102, 128, 36, "BỘ ĐIỀU KHIỂN FF", size=7.6, fill="#eef3fb"))
    o.append(_arrow(326, 120, 372, 120))
    o.append(_node(388, 120, "Σ", r=13))
    o.append(_arrow(401, 120, 440, 120))
    o.append(_box(442, 102, 110, 36, "QUÁ TRÌNH", size=8.2))
    o.append(_arrow(552, 120, 600, 120))
    o.append(_txt(604, 124, "PV", 8.5, anchor="start"))

    # the disturbance continues into the process
    o.append(_line(162, 48, 162, 78))
    o.append(_line(162, 78, 497, 78))
    o.append(_arrow(497, 78, 497, 100))
    o.append(_txt(300, 70, "nhiễu vẫn đi vào quá trình", 7, color=GREY))

    o.append(_txt(198, 156, "đo nhiễu trước khi nó tác động, tính bù ngay từ đầu", 7.4,
                  anchor="start", color=GREY))
    o.append(_txt(198, 170, "không dùng PV trong phép tính", 7.4, anchor="start", color=GREY))
    return _finish(o, 660, 186,
                   "Hình 10-3. Điều khiển theo hướng tự động: nhiễu được đo và bù trước khi vào vòng, "
                   "bộ điều khiển FF không dùng PV.",
                   "Figure 10-3. Automatic feedforward: the disturbance is measured and compensated "
                   "before it enters the loop; the FF controller does not use PV.",
                   "Sơ đồ: nhiễu đo được rẽ hai nhánh, một nhánh vào bộ điều khiển FF rồi cộng với đầu "
                   "ra, nhánh kia đi thẳng vào quá trình.",
                   "Diagram: the measured disturbance splits in two — one branch through the FF "
                   "controller into the summing node, the other straight into the process.")


# ---------------------------------------------------------------- 10.3
def fig_10_1():
    """What feedforward buys: the same disturbance, with and without it."""
    x0, y0, W, H = 66, 46, 516, 126
    dt = 0.02
    ts = [i * dt for i in range(301)]

    def dist(t):
        return -0.55 if t > 1.0 else 0.0

    fb = _sim_pi(ts, dt, dist, 1.2, 3.2, ff=False)
    both = _sim_pi(ts, dt, dist, 1.2, 3.2, ff=True, ff_gain=1.0)

    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_line(x0, y0 + H * 0.5, x0 + W, y0 + H * 0.5, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 8, y0 + H * 0.5 - 9, "SP", 7, anchor="start", color=GREY))

    def tr(ys):
        return _poly([(x0 + W * t / 6.0, y0 + H * (0.5 - v / 2.0)) for t, v in zip(ts, ys)],
                     sw=2.0, color=None)

    o.append(_poly([(x0 + W * t / 6.0, y0 + H * (0.5 - v / 2.0)) for t, v in zip(ts, fb)],
                   sw=2.0, color=RED))
    o.append(_poly([(x0 + W * t / 6.0, y0 + H * (0.5 - v / 2.0)) for t, v in zip(ts, both)],
                   sw=2.0, color=BLUE))
    o.append(_legend_h(x0 + 10, y0 + H + 44,
                       [(RED, "chỉ phản hồi: sai lệch lớn rồi mới sửa", ""),
                        (BLUE, "có theo hướng: gần như không lệch", "")], gap=24))
    o.append(_txt(x0 + W * 0.02, y0 + H * 0.93, "nhiễu bậc thang xuất hiện ở đây", 7.2,
                  anchor="start", color=GREY))
    o.append(_arrow(x0 + W * 0.24, y0 + H * 0.80, x0 + W * 0.24, y0 + H * 0.52, sw=0.8,
                    color=GREY, head="a5"))
    return _finish(o, 660, 232,
                   "Hình 10-1. Cùng một nhiễu bậc thang: chỉ có phản hồi thì PV lệch sâu rồi mới hồi, có "
                   "thêm theo hướng thì gần như không lệch.",
                   "Figure 10-1. The same step disturbance: with feedback alone PV deviates deeply before "
                   "recovering; with feedforward added it barely moves.",
                   "Hai đường PV: đường đỏ tụt xuống rồi bò về điểm đặt, đường xanh gần như nằm trên "
                   "điểm đặt suốt thời gian.",
                   "Two PV traces: the red one drops and then creeps back to the set point, the blue one "
                   "stays almost on the set point throughout.")


# ---------------------------------------------------------------- 10.4
def fig_10_5():
    """Time matching: heating is fast, cooling is slow, and the command must be asymmetric."""
    x0, y0, W, H = 66, 46, 516, 126
    th, tc = 0.45, 1.55

    def heat(t):
        return 1 - math.exp(-t / th) if t >= 0 else 0.0

    def cool(t):
        return math.exp(-t / tc) if t >= 0 else 1.0

    o = [_axes(x0, y0, W, H, "thời gian (phút)", "nhiệt độ",
               xt=[(0, "0"), (0.5, ""), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_curve(heat, x0, y0, W, H, n=241, xr=(0, 3), yr=(0, 1), color=RED, sw=2.0))
    o.append(_curve(lambda t: cool(t - 1.5), x0, y0, W, H, n=241, xr=(0, 3), yr=(0, 1),
                    color=BLUE, sw=2.0))
    o.append(_txt(x0 + W * 0.14, y0 + H * 0.74, "cấp nhiệt: nhanh", 7.5,
                  anchor="start", color=RED))
    o.append(_txt(x0 + W * 0.60, y0 + H * 0.62, "ngừng cấp nhiệt: chậm", 7.5,
                  anchor="start", color=BLUE))
    o.append(_line(x0 + W * 0.5, y0, x0 + W * 0.5, y0 + H, sw=0.7, dash="3 3", color=GREY))
    o.append(_txt(x0 + W * 0.5, y0 - 7, "đảo chiều", 7, color=GREY))
    return _finish(o, 660, 214,
                   "Hình 10-5. Khớp thời gian: quá trình cấp nhiệt nhanh hơn nhiều so với quá trình "
                   "nguội, nên một lệnh đối xứng sẽ cho một đáp ứng không đối xứng.",
                   "Figure 10-5. Time matching: heating is much faster than cooling, so a symmetric "
                   "command produces an asymmetric response.",
                   "Đồ thị: nhiệt độ tăng nhanh theo hàm mũ khi cấp nhiệt, rồi giảm chậm hơn hẳn sau khi "
                   "đảo chiều; hai hằng số thời gian khác nhau rõ rệt.",
                   "A plot: temperature rises quickly while heating and falls much more slowly after "
                   "the reversal; the two time constants differ visibly.")


# ---------------------------------------------------------------- 10.5
def fig_10_4():
    """The four parts every feedforward block must have."""
    o = [_box(24, 60, 96, 34, "ĐẦU VÀO\n(nhiễu đo)", size=7.4)]
    o.append(_arrow(120, 77, 152, 77))
    o.append(_box(154, 60, 110, 34, "HÀM TOÁN", size=8.5))
    o.append(_arrow(264, 77, 296, 77))
    o.append(_box(298, 60, 100, 34, "ĐẦU RA", size=8.5))
    o.append(_arrow(398, 77, 440, 77))
    o.append(_txt(446, 81, "tới MV", 8.5, anchor="start"))

    o.append(_box(154, 12, 110, 26, "ĐIỂM ĐẶT", size=7.4, fill="#f6efe0"))
    o.append(_arrow(209, 38, 209, 58))

    o.append(_txt(24, 128, "bốn thành phần bắt buộc của một khối theo hướng:", 8,
                  anchor="start", color=INK))
    for i, s in enumerate(["đầu vào nhận diện được, lấy từ nhiễu đã đo",
                           "một điểm đặt hay điểm gốc và điểm điều khiển",
                           "một hàm toán tác động lên đầu vào và điểm đặt",
                           "một đầu ra là kết quả của hàm toán đó"]):
        o.append(_txt(34, 146 + i * 13, "•  " + s, 7.4, anchor="start", color=GREY))
    return _finish(o, 660, 208,
                   "Hình 10-4. Bốn thành phần của một bộ điều khiển theo hướng; toàn bộ tác động của nó "
                   "được mô tả bằng chính hàm toán mà nó thực hiện.",
                   "Figure 10-4. The four parts of a feedforward controller; its whole action is "
                   "described by the mathematical function it performs.",
                   "Sơ đồ: đầu vào từ nhiễu đo qua khối hàm toán ra đầu ra; điểm đặt cũng đi vào khối "
                   "hàm toán; bên dưới liệt kê bốn thành phần bắt buộc.",
                   "Diagram: the input from the measured disturbance passes through a maths block to "
                   "the output; a set point also enters the block; the four required parts are listed "
                   "below.")


# ---------------------------------------------------------------- 10.6
def fig_10_6():
    """A lead/lag compensator: the same step, seen through (1+Ts)/(1+αTs)."""
    x0, y0, W, H = 66, 46, 516, 126
    Tl, a = 1.0, 0.4           # lead time constant, lag/lead ratio

    def step(t):
        return 1.0 if t > 0.6 else 0.0

    def leadlag(t):
        if t <= 0.6:
            return 0.0
        u = t - 0.6
        # step response of (1 + Tl s)/(1 + a Tl s)
        return 1.0 + (1.0 / a - 1.0) * math.exp(-u / (a * Tl))

    o = [_axes(x0, y0, W, H, "thời gian", "tín hiệu",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (1.0 / 3.0, "1"), (2.5 / 3.0, "2,5")])]
    o.append(_curve(step, x0, y0, W, H, n=241, xr=(0, 4), yr=(0, 3.0), color=GREY, sw=1.6,
                    dash="4 3"))
    o.append(_curve(leadlag, x0, y0, W, H, n=241, xr=(0, 4), yr=(0, 3.0), color=BLUE, sw=2.0))
    o.append(_txt(x0 + W * 0.14, y0 + H * 0.86, "bậc thang vào", 7.4,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W * 0.30, y0 + H * 0.30, "ra của khâu lead/lag", 7.6,
                  anchor="start", color=BLUE))
    o.append(_txt(x0 + W * 0.30, y0 + H * 0.42, "đỉnh rồi tự tắt về 1", 7.2,
                  anchor="start", color=BLUE))
    o.append(_txt(x0 + W * 0.62, y0 + H * 0.16, "(1 + T_lead·s) / (1 + α·T_lead·s)", 8.5,
                  anchor="start", color=INK))
    return _finish(o, 660, 214,
                   "Hình 10-6. Khâu bù lead/lag: một bước nhảy vào cho ra một đỉnh rồi tự tắt dần về "
                   "mức một — đúng lượng bù cần để khớp hai tốc độ phản ứng khác nhau.",
                   "Figure 10-6. The lead/lag compensator: a step in gives a spike that decays back to "
                   "one — the extra push needed to match two different reaction speeds.",
                   "Đồ thị: đường nét đứt là bậc thang vào; đường liền vọt lên khoảng 2,5 rồi tắt dần "
                   "về mức 1.",
                   "A plot: the dashed line is the input step; the solid line overshoots to about 2.5 "
                   "and then decays back to 1.")


# ---------------------------------------------------------------- 10.7
def fig_10_7():
    """The feed heater with mass-flow feedforward and a fuel flow loop."""
    o = [_txt(12, 44, "lưu lượng vào", 7.2, anchor="start", color=GREY)]
    o.append(_arrow(12, 52, 62, 52))
    o.append(_box(64, 34, 62, 36, "FT\nđo lưu lượng", size=7.2))
    o.append(_arrow(126, 52, 154, 52))
    o.append(_box(156, 34, 96, 36, "TÍNH NHIỆT LƯỢNG\nCẦN CẤP", size=6.9, fill="#eef3fb"))
    o.append(_arrow(252, 52, 280, 52))
    o.append(_node(294, 52, "Σ", r=12, size=8.5))
    o.append(_arrow(306, 52, 334, 52))
    o.append(_box(336, 34, 76, 36, "FC\nnhiên liệu", size=7.4))
    o.append(_arrow(412, 52, 440, 52))
    o.append(_box(442, 38, 36, 28, "van", size=7.4))
    o.append(_arrow(478, 52, 508, 52))
    o.append(_box(510, 26, 124, 52, "LÒ GIA NHIỆT", size=7.4, sub="dòng ra đã gia nhiệt"))

    # the temperature transmitter on the outlet, and its trim back to the sum
    o.append(_arrow(572, 78, 572, 106))
    o.append(_box(538, 106, 68, 28, "TT\nnhiệt độ ra", size=6.8))
    o.append(_arrow(538, 120, 294, 120))
    o.append(_arrow(294, 120, 294, 64))
    o.append(_txt(312, 112, "phản hồi nhiệt độ — chỉ hiệu chỉnh phần dư", 7.2,
                  anchor="start", color=RED))

    o.append(_txt(64, 156, "đo lưu lượng vào → tính ngay lượng nhiệt cần", 7.2,
                  anchor="start", color=GREY))
    o.append(_txt(64, 170, "nên nhiễu lưu lượng bị bù trước khi tới nhiệt độ", 7.2,
                  anchor="start", color=GREY))
    return _finish(o, 660, 186,
                   "Hình 10-7. Điều khiển theo hướng cho bộ gia nhiệt dòng liệu: lưu lượng vào được đo "
                   "và quy đổi ngay thành nhiệt lượng cần cấp, cộng với một vòng lưu lượng nhiên liệu.",
                   "Figure 10-7. Feedforward for the feed heater: the inlet flow is measured and "
                   "converted straight into the heat required, on top of a fuel flow loop.",
                   "Sơ đồ: lưu lượng vào qua cảm biến FT, vào khối tính nhiệt lượng, cộng với tín hiệu "
                   "phản hồi nhiệt độ từ TT ở đầu ra lò, rồi tới bộ điều khiển lưu lượng nhiên liệu, "
                   "qua van và vào lò gia nhiệt.",
                   "Diagram: the inlet flow passes an FT into a heat-demand block, sums with the "
                   "temperature feedback from the TT on the heater outlet, and drives the fuel flow "
                   "controller, through the valve, into the feed heater.")


# ---------------------------------------------------------------- 10.8
def fig_10_8():
    """Feedforward alone leaves a drift; only feedback removes it."""
    x0, y0, W, H = 66, 46, 516, 126
    dt = 0.02
    ts = [i * dt for i in range(301)]

    def dist(t):
        return -0.5 if t > 1.0 else 0.0

    ff_only = _sim_pi(ts, dt, dist, 0.0, 2.0, ff=True, ff_gain=0.82)
    ff_fb = _sim_pi(ts, dt, dist, 1.6, 2.6, ff=True, ff_gain=0.82)

    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_line(x0, y0 + H * 0.5, x0 + W, y0 + H * 0.5, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 6, y0 + H * 0.5 - 5, "SP", 7, anchor="start", color=GREY))
    o.append(_poly([(x0 + W * t / 6.0, y0 + H * (0.5 - v / 2.0)) for t, v in zip(ts, ff_only)],
                   sw=2.0, color=RED))
    o.append(_poly([(x0 + W * t / 6.0, y0 + H * (0.5 - v / 2.0)) for t, v in zip(ts, ff_fb)],
                   sw=2.0, color=BLUE))
    o.append(_legend_h(x0 + 10, y0 + H + 44,
                       [(RED, "chỉ theo hướng: còn dư một khoảng lệch", ""),
                        (BLUE, "theo hướng + phản hồi: dư được xoá", "")], gap=24))
    o.append(_txt(x0 + W * 0.72, y0 + H * 0.77, "phần dư", 7.2, anchor="start", color=RED))
    return _finish(o, 660, 232,
                   "Hình 10-8. Chỉ có theo hướng thì luôn còn một khoảng lệch dư, vì mô hình bù không "
                   "bao giờ hoàn hảo; thêm phản hồi thì khoảng dư đó bị xoá.",
                   "Figure 10-8. Feedforward alone always leaves a residual offset, because the "
                   "compensation model is never perfect; adding feedback removes it.",
                   "Hai đường PV sau cùng một nhiễu: đường đỏ ổn định ở một mức thấp hơn điểm đặt, "
                   "đường xanh quay về đúng điểm đặt.",
                   "Two PV traces after the same disturbance: the red settles below the set point, the "
                   "blue returns to it.")


# ---------------------------------------------------------------- 10.9
def fig_10_9():
    """The comparison the chapter keeps making."""
    o = [_rect(24, 22, 300, 118, "#f6efe0", sw=1.0, stroke="#d9cdb2")]
    o.append(_txt(174, 42, "PHẢN HỒI", 9, color=INK))
    o.append(_txt(174, 62, "sửa cái đã sai", 8, color=GREY))
    o.append(_txt(174, 82, "chờ sai lệch xuất hiện", 7.4, color=GREY))
    o.append(_txt(174, 96, "luôn ổn định được nếu đủ chậm", 7.4, color=GREY))
    o.append(_txt(174, 118, "không cần biết nhiễu là gì", 7.4, color=INK))

    o.append(_rect(344, 22, 300, 118, "#eef3fb", sw=1.0, stroke="#b9cbe6"))
    o.append(_txt(494, 42, "THEO HƯỚNG", 9, color=INK))
    o.append(_txt(494, 62, "ngăn cái sắp sai", 8, color=GREY))
    o.append(_txt(494, 82, "hành động trước khi lệch", 7.4, color=GREY))
    o.append(_txt(494, 96, "cần mô hình chính xác của nhiễu", 7.4, color=GREY))
    o.append(_txt(494, 118, "sai mô hình thì để lại dư", 7.4, color=INK))

    o.append(_txt(330, 164, "hai cơ chế không thay thế nhau: theo hướng giảm biên độ sai lệch, "
                            "phản hồi xoá phần dư", 7.6, color=GREY))
    return _finish(o, 660, 180,
                   "Hình 10-9. Đối chiếu hai cơ chế: phản hồi sửa cái đã sai, theo hướng ngăn cái sắp sai.",
                   "Figure 10-9. The two mechanisms side by side: feedback corrects what has already "
                   "gone wrong, feedforward prevents what is about to.",
                   "Hai khung cạnh nhau liệt kê đặc điểm của phản hồi và của theo hướng, cùng một dòng "
                   "kết luận rằng hai cơ chế bổ sung cho nhau.",
                   "Two panels listing the properties of feedback and of feedforward, with a line "
                   "below saying the two complement each other.")
