# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 11 — Combined Feedback and Feedforward."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h


# ---------------------------------------------------------------- helpers
def _sim_pct(ts, dt, dist, kp, ti, ff_gain=0.0, tau=1.5, dead=1.0):
    """First-order plant on a 0-100 % scale, PI feedback, optional feedforward."""
    n = len(ts)
    y = [0.0] * n
    y[0] = 50.0
    u = 0.0
    integ = 0.0
    buf = [0.0] * max(1, int(dead / dt + 1))
    for i, t in enumerate(ts):
        d = dist(t)
        ffd = -ff_gain * d if ff_gain else 0.0
        ud = buf.pop(0)
        buf.append(u)
        if i:
            y[i] = y[i - 1] + dt * ((ud + d + ffd + 50.0 - y[i - 1]) / tau)
        e = 50.0 - y[i]
        integ += e * dt
        u = kp * (e + integ / ti)
    return y


# ---------------------------------------------------------------- 11.1
def fig_11_1():
    """Two kinds of disturbance: the magnitude changes, or the speed changes."""
    def mag(t):
        return 50.0 if t <= 1.2 else 50.0 + 40.0 * math.exp(-(t - 1.2) / 0.70)

    def fast(t):
        return 50.0 if t <= 1.2 else 50.0 + 40.0 * math.exp(-(t - 1.2) / 0.35)

    def slow(t):
        return 50.0 if t <= 1.2 else 50.0 + 40.0 * math.exp(-(t - 1.2) / 1.50)

    o = []
    # left panel: the magnitude of the disturbance changes
    o.append(_axes(50, 48, 244, 116, "thời gian", "PV",
                   xt=[(0, "0"), (1, "")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(mag, 50, 48, 244, 116, n=241, xr=(0, 5), yr=(0, 100), color=RED, sw=2.0))
    o.append(_txt(56, 42, "biên độ nhiễu thay đổi", 7.2, anchor="start", color=RED))

    # right panel: the speed of the process response changes
    o.append(_axes(392, 48, 244, 116, "thời gian", "PV",
                   xt=[(0, "0"), (1, "")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(fast, 392, 48, 244, 116, n=241, xr=(0, 5), yr=(0, 100), color=BLUE, sw=2.0))
    o.append(_curve(slow, 392, 48, 244, 116, n=241, xr=(0, 5), yr=(0, 100), color=GOLD, sw=2.0))
    o.append(_txt(398, 42, "tốc độ phản ứng thay đổi", 7.2, anchor="start", color=GREY))

    o.append(_legend_h(398, 196, [(BLUE, "hằng số thời gian ngắn", ""),
                                  (GOLD, "hằng số thời gian dài", "")], gap=20))
    return _finish(o, 660, 222,
                   "Hình 11-1. Hai loại nhiễu mà điều khiển theo hướng phải xử lý: bên trái là biên độ "
                   "thay đổi, bên phải là tốc độ phản ứng của quá trình thay đổi — cùng một nhiễu, hai "
                   "hằng số thời gian khác nhau.",
                   "Figure 11-1. The two kinds of disturbance feedforward must handle: on the left the "
                   "magnitude changes, on the right the process response speed changes — same "
                   "disturbance, two different time constants.",
                   "Hai đồ thị PV theo thời gian: bên trái một đường vọt lên rồi tắt dần; bên phải hai "
                   "đường cùng độ cao nhưng tắt nhanh và tắt chậm.",
                   "Two PV-versus-time plots: on the left one curve rises and decays; on the right two "
                   "curves reach the same height but decay at different rates.")


# ---------------------------------------------------------------- 11.2
def fig_11_2():
    """The combined scheme: one valve, two mechanisms."""
    o = []
    # feed and the feedforward chain
    o.append(_txt(10, 34, "F1, T1", 7.0, anchor="start", color=GREY))
    o.append(_arrow(10, 48, 38, 48))
    o.append(_box(40, 30, 52, 36, "FT", size=7.6))
    o.append(_arrow(92, 48, 118, 48))
    o.append(_box(120, 30, 86, 36, "TÍNH NHIỆT\nLƯỢNG", size=6.6))
    o.append(_arrow(206, 48, 232, 48))
    o.append(_box(234, 30, 68, 36, "LEAD/LAG", size=6.9))
    o.append(_arrow(302, 48, 326, 48))
    o.append(_txt(314, 40, "FF", 6.8, anchor="middle", color=RED))
    o.append(_node(338, 48, "Σ", r=12, size=8.5))
    o.append(_arrow(350, 48, 376, 48))
    o.append(_box(378, 30, 66, 36, "FC\nnhiên liệu", size=6.9))
    o.append(_arrow(444, 48, 468, 48))
    o.append(_box(470, 34, 30, 28, "van", size=7.2))
    o.append(_arrow(500, 48, 528, 48))
    o.append(_arrow(528, 48, 528, 104))
    o.append(_txt(536, 88, "MV duy nhất", 6.8, anchor="start", color=GOLD))

    # the plant
    o.append(_box(430, 104, 150, 48, "LÒ GIA NHIỆT", size=7.4, sub="gia nhiệt dòng liệu"))
    o.append(_arrow(405, 128, 430, 128))
    o.append(_txt(401, 121, "dòng liệu F1", 6.8, anchor="end", color=GREY))
    o.append(_arrow(580, 128, 640, 128))
    o.append(_txt(588, 120, "T2", 7.2))

    # the temperature transmitter and the primary controller
    o.append(_arrow(625, 128, 625, 150))
    o.append(_box(596, 150, 58, 28, "TT\nT2", size=6.6))
    o.append(_arrow(596, 164, 386, 164))
    o.append(_box(290, 150, 96, 40, "TC\nnhiệt độ ra", size=7.0))
    o.append(_arrow(338, 150, 338, 60))
    o.append(_txt(346, 74, "TC", 6.8, anchor="start", color=BLUE))

    return _finish(o, 660, 206,
                   "Hình 11-2. Sơ đồ kết hợp: chuỗi theo hướng (FT → tính nhiệt lượng → lead/lag) và "
                   "vòng phản hồi (TT → TC) cùng tác động lên một biến điều khiển duy nhất là lưu lượng "
                   "nhiên liệu.",
                   "Figure 11-2. The combined scheme: the feedforward chain (FT → heat demand → "
                   "lead/lag) and the feedback loop (TT → TC) both act on one manipulated variable, the "
                   "fuel flow.",
                   "Sơ đồ khối: lưu lượng vào qua FT, qua khối tính nhiệt lượng và lead/lag tới bộ cộng; "
                   "TT ở đầu ra qua TC cũng tới bộ cộng; bộ cộng đặt điểm đặt cho FC điều khiển van cấp "
                   "nhiên liệu cho lò.",
                   "Block diagram: the inlet flow passes FT, a heat-demand block and lead/lag into a "
                   "summer; the outlet TT feeds a TC into the same summer; the summer sets the set point "
                   "of the FC that drives the fuel valve.")


# ---------------------------------------------------------------- 11.3
def fig_11_3():
    """Absolute versus incremental: why the summer adds increments, not positions."""
    o = [_txt(20, 24, "NẾU MỖI BỘ ĐIỀU KHIỂN ĐÒI MỘT VỊ TRÍ VAN", 7.4, anchor="start", color=GREY)]

    # panel A: two masters each claim the whole valve
    o.append(_box(20, 42, 96, 34, "TC", size=7.6, fill="#f6efe0"))
    o.append(_box(20, 96, 96, 34, "FF", size=7.6, fill="#f6efe0"))
    o.append(_arrow(116, 59, 168, 59))
    o.append(_arrow(116, 113, 168, 113))
    o.append(_box(170, 50, 84, 70, "VAN", size=7.6))
    o.append(_txt(140, 50, "0…100 %", 6.4, anchor="middle", color=GREY))
    o.append(_txt(140, 104, "0…100 %", 6.4, anchor="middle", color=GREY))
    o.append(_txt(212, 136, "xung đột", 7.0, anchor="middle", color=RED))

    # panel B: one baseline, one correction
    o.append(_txt(352, 24, "NẾU MỘT BÊN ĐẶT GỐC, MỘT BÊN THÊM HIỆU CHỈNH", 7.4,
                  anchor="start", color=GREY))
    o.append(_box(352, 42, 96, 34, "FF\ngốc", size=7.2, fill="#f6efe0"))
    o.append(_box(352, 96, 96, 34, "TC\n± nhỏ", size=7.2, fill="#f6efe0"))
    o.append(_arrow(448, 59, 476, 59))
    o.append(_arrow(448, 113, 476, 113))
    o.append(_node(490, 86, "Σ", r=12, size=8.5))
    o.append(_arrow(502, 86, 528, 86))
    o.append(_box(530, 64, 78, 44, "FC\n→ VAN", size=7.2))
    o.append(_txt(490, 136, "một lệnh duy nhất", 7.0, anchor="middle", color=GREEN))

    return _finish(o, 660, 152,
                   "Hình 11-3. Vì sao bộ cộng phải cộng các lượng tăng dần: nếu cả hai bộ điều khiển cùng "
                   "đòi một vị trí van tuyệt đối thì chúng tranh nhau; nếu một bên đặt giá trị gốc và "
                   "bên kia chỉ thêm hiệu chỉnh thì chỉ còn một lệnh duy nhất.",
                   "Figure 11-3. Why the summer adds increments: if both controllers claim an absolute "
                   "valve position they compete; if one supplies the baseline and the other only a "
                   "correction, there is a single command.",
                   "Hai sơ đồ so sánh: bên trái TC và FF cùng đòi vị trí van tuyệt đối nên xung đột; bên "
                   "phải FF đặt giá trị gốc, TC thêm hiệu chỉnh nhỏ, cộng lại thành một lệnh duy nhất "
                   "cho FC.",
                   "Two diagrams compared: on the left the TC and the FF both claim an absolute valve "
                   "position, so they conflict; on the right the FF supplies the baseline and the TC a "
                   "small correction, summing to one command for the FC.")


# ---------------------------------------------------------------- 11.4
def fig_11_4():
    """The heat balance: required fuel flow against inlet flow, at three temperature rises."""
    x0, y0, W, H = 74, 44, 480, 132

    def fuel(f1, dt):
        # F = F1 · C · (T2 − T1) / h, normalised so 100 % flow at dT = 40 gives 100 % fuel
        return min(108.0, f1 * dt / 40.0)

    o = [_axes(x0, y0, W, H, "lưu lượng vào F1 (% thang)", "nhiên liệu F (% thang)",
               xt=[(0, "0"), (0.25, "25"), (0.5, "50"), (0.75, "75"), (1, "100")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    for dt, col in [(20.0, BLUE), (40.0, GREEN), (60.0, RED)]:
        o.append(_curve(lambda x, dt=dt: fuel(x, dt), x0, y0, W, H, n=201,
                        xr=(0, 100), yr=(0, 108), color=col, sw=2.0))
    o.append(_line(x0, y0 + H * (1 - 100.0 / 108.0), x0 + W, y0 + H * (1 - 100.0 / 108.0),
                   sw=0.9, dash="5 3", color=GREY))
    o.append(_txt(x0 + 4, y0 + H * (1 - 100.0 / 108.0) - 5, "trần 100 %", 6.6,
                  anchor="start", color=GREY))
    o.append(_legend(x0 + 16, y0 + 12,
                     [(BLUE, "ΔT = 20 °C", ""),
                      (GREEN, "ΔT = 40 °C", ""),
                      (RED, "ΔT = 60 °C", "")], w=112))
    o.append(_txt(x0 + 16, y0 + 72, "bão hoà ở F1 ≈ 67 %", 6.8,
                  anchor="start", color=RED))
    return _finish(o, 660, 208,
                   "Hình 11-4. Cân bằng nhiệt của bộ gia nhiệt: nhiên liệu cần cấp tỉ lệ với lưu lượng vào "
                   "và với độ tăng nhiệt độ. Khi ΔT = 60 °C, dòng vào chỉ cần đạt 67 % là van nhiên liệu "
                   "đã hết dư địa.",
                   "Figure 11-4. The heater's heat balance: fuel demand is proportional to inlet flow and "
                   "to the temperature rise. At ΔT = 60 °C the valve runs out of range once the inlet flow "
                   "reaches 67 per cent.",
                   "Đồ thị ba đường thẳng qua gốc: nhiên liệu cần cấp theo lưu lượng vào, ứng với ba độ "
                   "tăng nhiệt độ 20, 40 và 60 °C; đường 60 °C cắt mức 100 % ở khoảng 67 % lưu lượng.",
                   "Three straight lines through the origin: fuel demand against inlet flow for "
                   "temperature rises of 20, 40 and 60 °C; the 60 °C line crosses the 100 per cent level "
                   "at about 67 per cent flow.")


# ---------------------------------------------------------------- 11.5
def fig_11_5():
    """Initialisation: the bump when the primary's output starts from the wrong value."""
    dt = 0.02
    ts = [i * dt for i in range(601)]
    tau, kp, ti = 1.5, 1.2, 2.0
    sp = 40.0

    def run(op0):
        y = [0.0] * len(ts)
        y[0] = sp                             # the loop is already holding at SP
        u = sp                                # in manual, the operator holds the output at 40
        integ = 0.0
        for i, t in enumerate(ts):
            if i:
                y[i] = y[i - 1] + dt * ((u - y[i - 1]) / tau)
            if t > 2.0:                       # the switch to automatic
                e = sp - y[i]
                integ += e * dt
                u = op0 + kp * (e + integ / ti)
            else:
                u = sp
        return y

    good = run(sp)                            # initialised at the value already in use
    bad = run(0.0)                            # initialised at zero

    x0, y0, W, H = 70, 46, 484, 130
    o = [_axes(x0, y0, W, H, "thời gian", "PV",
               xt=[(0, "0"), (2 / 12.0, "2"), (1, "")],
               yt=[(0, "0"), (40 / 100.0, "40"), (1, "100")])]
    o.append(_line(x0, y0 + H * (1 - 40 / 100.0), x0 + W, y0 + H * (1 - 40 / 100.0),
                   sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 6, y0 + H * (1 - 40 / 100.0) - 5, "SP", 6.8, anchor="start", color=GREY))
    o.append(_poly([(x0 + W * t / 12.0, y0 + H * (1 - v / 100.0)) for t, v in zip(ts, bad)],
                   sw=2.0, color=RED))
    o.append(_poly([(x0 + W * t / 12.0, y0 + H * (1 - v / 100.0)) for t, v in zip(ts, good)],
                   sw=2.0, color=BLUE))
    o.append(_line(x0 + W * 2 / 12.0, y0, x0 + W * 2 / 12.0, y0 + H, sw=0.9, dash="3 3", color=GREY))
    o.append(_txt(x0 + W * 2 / 12.0 + 5, y0 + 10, "chuyển sang AUTO", 6.8, anchor="start", color=GREY))
    o.append(_legend_h(x0 + 8, y0 + H + 40,
                       [(BLUE, "khởi tạo đúng: OP = FF + SP", ""),
                        (RED, "khởi tạo bằng 0: cú giật", "")], gap=20))
    return _finish(o, 660, 232,
                   "Hình 11-5. Khởi tạo: nếu đầu ra của TC được nạp đúng bằng tổng tín hiệu theo hướng và "
                   "điểm đặt của FC thì việc chuyển sang AUTO không gây giật; nếu nạp bằng 0 thì PV tụt "
                   "xuống rồi mới hồi.",
                   "Figure 11-5. Initialisation: if the TC's output is pre-loaded with the feedforward "
                   "signal plus the FC's set point, switching to AUTO causes no bump; if it is loaded "
                   "with zero, the PV drops before recovering.",
                   "Đồ thị PV theo thời gian: đường xanh phẳng ở mức 40; đường đỏ tụt xuống khoảng 26 sau "
                   "khi chuyển sang AUTO rồi hồi dần về 40.",
                   "A PV-versus-time plot: the blue trace stays flat at 40; the red trace falls to about "
                   "26 after the switch to AUTO and then recovers to 40.")


# ---------------------------------------------------------------- 11.6
def fig_11_6():
    """The tuning order the chapter prescribes."""
    o = []
    labels = [("1", "chỉnh vòng\nthứ cấp FC"),
              ("2", "chỉnh khối\ntheo hướng"),
              ("3", "chỉnh TC theo\nZiegler–Nichols"),
              ("4", "đánh giá tốc độ\ntrôi của PV")]
    xs = [10, 172, 334, 496]
    for (num, lab), x in zip(labels, xs):
        o.append(_box(x, 34, 138, 44, lab, size=7.0))
        o.append(_circle(x + 12, 34, 9, "#f6efe0", 1.0, INK))
        o.append(_txt(x + 12, 37, num, 7.6, color=INK))
    for i in range(3):
        o.append(_arrow(xs[i] + 138, 56, xs[i + 1], 56))

    # the branch off step four
    o.append(_arrow(565, 78, 565, 108))
    o.append(_box(334, 110, 300, 42,
                  "nếu trôi không đáng kể: giảm K của TC theo hiểu biết quá trình", size=6.9,
                  fill="#eaf3ea"))

    o.append(_txt(10, 180, "Phản hồi ở đây chỉ là phần bổ sung: nó phải không gây dao động và không "
                           "gây mất ổn định.", 7.2, anchor="start", color=GREY))
    return _finish(o, 660, 196,
                   "Hình 11-6. Trình tự chỉnh định: vòng thứ cấp trước, rồi khối theo hướng, rồi vòng sơ "
                   "cấp bằng công thức Ziegler–Nichols; cuối cùng đánh giá tốc độ trôi và giảm K nếu "
                   "phản hồi đang can thiệp quá mạnh.",
                   "Figure 11-6. The tuning order: secondary loop first, then the feedforward block, then "
                   "the primary by the Ziegler–Nichols formulas; finally judge the drift rate and reduce K "
                   "if feedback is intervening too hard.",
                   "Lưu đồ bốn bước chỉnh định nối tiếp nhau, bước bốn rẽ nhánh sang một khối quyết định "
                   "giảm hệ số K của bộ điều khiển nhiệt độ.",
                   "A four-step tuning flow, with step four branching to a decision block that reduces the "
                   "temperature controller's gain.")


# ---------------------------------------------------------------- 11.7
def fig_11_7():
    """Three ways of combining: drift, oscillation, and the working compromise."""
    dt = 0.02
    ts = [i * dt for i in range(601)]

    def dist(t):
        return -50.0 if t > 1.0 else 0.0

    ff_only = _sim_pct(ts, dt, dist, 0.0, 2.0, 0.75)
    too_hot = _sim_pct(ts, dt, dist, 2.6, 2.4, 0.75)
    balanced = _sim_pct(ts, dt, dist, 1.0, 3.0, 0.75)

    x0, y0, W, H = 70, 46, 484, 130
    o = [_axes(x0, y0, W, H, "thời gian", "PV (%)",
               xt=[(0, "0"), (1, "")],
               yt=[(0, "0"), (0.5, "50"), (1, "100")])]
    o.append(_line(x0, y0 + H * 0.5, x0 + W, y0 + H * 0.5, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 6, y0 + H * 0.5 - 5, "SP", 6.8, anchor="start", color=GREY))
    for vals, col in [(ff_only, RED), (too_hot, GOLD), (balanced, BLUE)]:
        o.append(_poly([(x0 + W * t / 12.0, y0 + H * (1 - v / 100.0)) for t, v in zip(ts, vals)],
                       sw=1.9, color=col))
    o.append(_txt(x0 + W * 0.62, y0 + H * 0.72, "phần dư", 6.8, anchor="start", color=RED))
    o.append(_legend_h(x0 + 6, y0 + H + 40,
                       [(RED, "theo hướng đơn thuần: trôi", ""),
                        (GOLD, "phản hồi quá mạnh: dao động", ""),
                        (BLUE, "phản hồi vừa phải: ổn định", "")], gap=18))
    return _finish(o, 660, 236,
                   "Hình 11-7. Ba cách ghép: để theo hướng làm một mình thì PV trôi; tăng phản hồi quá "
                   "mạnh thì hệ dao động; giữ phản hồi vừa đủ thì PV về đúng điểm đặt mà không dao động.",
                   "Figure 11-7. Three ways of combining: feedforward alone lets the PV drift; turning "
                   "feedback up too hard makes the loop oscillate; keeping feedback just strong enough "
                   "brings the PV back to set point without oscillation.",
                   "Đồ thị PV theo thời gian với ba đường: đường đỏ trôi xuống và nằm lại; đường vàng dao "
                   "động tắt dần; đường xanh về lại điểm đặt êm.",
                   "A PV-versus-time plot with three traces: the red one drifts down and stays there; the "
                   "gold one oscillates as it decays; the blue one returns to set point smoothly.")
