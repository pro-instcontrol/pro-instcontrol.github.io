# -*- coding: utf-8 -*-
"""Vector figures 9-11 for PPIC chapter 9 (control charts and HMM)."""
import math

from ppicfig9_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()


def _rnd(seed):
    """Deterministic uniform generator, kept local to each figure."""
    s = [seed]

    def u():
        s[0] = (1103515245 * s[0] + 12345) % 2147483648
        return s[0] / 2147483648.0

    return u


def _star(cx, cy, r=2.5, color=RED):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return _poly(pts, fill=color, sw=0, color=color, close=True)


@_reg
def fig_f09():
    """T² chart eight weeks after replacement, nearly all points beyond UCL."""
    o = [T(340, 14, "T² control chart for acoustic signal recorded on 15 03 2012",
           8.6, weight="bold")]
    fr, mx, my = _frame(70, 26, 578, 202, (0, 600), (0, 180),
                        [(v, str(v)) for v in range(0, 601, 100)],
                        [(v, str(v)) for v in range(0, 181, 20)],
                        "Samples", "T² statistics")
    o.append(fr)
    ucl = 36.0
    o.append(_line(mx(0), my(ucl), mx(600), my(ucl), sw=2.2, color=BLUE))
    o.append(T(656, my(ucl) + 2.4, "UCL", 6.2, color=BLUE, anchor="start"))

    u = _rnd(15032012)
    for i in range(470):
        x = 3 + 554 * u()
        r = u()
        if r < 0.11:
            y = 12 + 24 * u()
        elif r < 0.84:
            y = 38 + 52 * (u() ** 1.6)
        elif r < 0.97:
            y = 92 + 55 * u()
        else:
            y = 148 + 28 * u()
        if x < 300 and r > 0.97:
            y = min(176.0, y + 10 * u())
        o.append(_star(mx(x), my(y), 2.4))

    return _mk(9, o, "T² control chart eight weeks after replacement",
               "Biểu đồ kiểm soát T² cho tín hiệu âm thanh ghi nhận 8 tuần sau khi thay bàn nghiền",
               "T² control chart for acoustic signal recorded 8 weeks after grinding table replacement",
               "Nhiều điểm nằm trên đường giới hạn kiểm soát UCL sau 8 tuần.",
               "Many plotted points lie above the UCL line eight weeks after replacement.")


@_reg
def fig_f10():
    """Estimated densities for signals at two, five and eight weeks."""
    o = [T(340, 14, "Estimated probability density function", 8.8,
           weight="bold")]
    fr, mx, my = _frame(70, 30, 556, 188, (-50, 200), (0, 0.08),
                        [(v, str(v)) for v in (-50, 0, 50, 100, 150, 200)],
                        [(0.01 * i, "0" if i == 0 else "0.%02d" % i)
                         for i in range(9)],
                        "Data", "Density")
    o.append(fr)

    def red_f(x):
        if x <= 0:
            return 0.0006 if 38 <= x <= 72 else 0.0
        t = x / 3.6
        v = 0.0528 * (t ** 3) * math.exp(-t)
        if 38 <= x <= 72:
            v += 0.0006
        return v

    def green_f(x):
        t = (x - 5) / 9.0
        if t <= 0:
            return 0.0
        return 0.00426 * (t ** 4) * math.exp(-t)

    def black_f(x):
        t = (x - 8) / 13.0
        if t <= 0:
            return 0.0
        return 0.0092 * (t ** 3.2) * math.exp(-t)

    for fn, col in ((red_f, RED), (green_f, GREEN), (black_f, INK)):
        pts = []
        for i in range(251):
            xv = -50 + 250 * i / 250.0
            pts.append((mx(xv), my(min(fn(xv), 0.08))))
        o.append(_poly(pts, sw=2.0, color=col))

    o.append(_legend([(RED, "Two weeks after grinding table replacement"),
                      (GREEN, "Five weeks after grinding table replacement"),
                      (INK, "Eight weeks after grinding table replacement")],
                     318, 36, w=302, lh=15, size=6.8))

    return _mk(10, o, "Estimated probability density functions",
               "Ước tính hàm mật độ xác suất cho tín hiệu ghi nhận sau 2, 5 và 8 tuần",
               "Estimated probability density functions for signals recorded 2, 5 and 8 weeks after grinding table replacement",
               "Ba đường mật độ màu đỏ, xanh lục và đen dịch chuyển dần sang phải khi bàn nghiền mòn.",
               "Three density curves shift to the right and broaden as the grinding table wears.")


@_reg
def fig_f11():
    """Observation sequence and inferred HMM states, entering the worn state."""
    o = [T(352, 13, "Sequence of observations", 8.4, weight="bold")]
    fr1, mx1, my1 = _frame(72, 20, 560, 86, (0, 1800), (0, 80),
                           [(v, str(v)) for v in (0, 400, 800, 1200, 1600)],
                           [(v, str(v)) for v in (0, 20, 40, 60, 80)],
                           "Number of samples", "Observations")
    o.append(fr1)

    u = _rnd(11092012)

    def band(x1, x2, lev, jitter=1.2):
        x = float(x1)
        while x < x2:
            seg = min(3.0 + 3.0 * u(), x2 - x)
            yy = lev + (u() - 0.5) * jitter
            o.append(_line(mx1(x), my1(yy), mx1(x + seg), my1(yy),
                           sw=2.6, color=BLUE))
            x += seg + 0.7

    band(0, 560, 14.0)
    band(565, 1080, 47.0)
    band(1330, 1665, 47.5)
    band(600, 1000, 66.0)
    band(1150, 1660, 66.5)
    for xv, yv in ((800, 67), (880, 64), (960, 65), (1120, 48), (1250, 48)):
        o.append(_star(mx1(xv), my1(yv), 2.1, color=BLUE))

    o.append(T(352, 145, "HMM states", 8.4, weight="bold"))
    fr2, mx2, my2 = _frame(72, 152, 560, 86, (0, 1800), (1, 3),
                           [(v, str(v)) for v in (0, 400, 800, 1200, 1600)],
                           [(1, "1"), (1.5, "1.5"), (2, "2"),
                            (2.5, "2.5"), (3, "3")],
                           "Number of samples", "States")
    o.append(fr2)
    for xa, xb, st in ((0, 560, 1), (560, 1080, 2), (1100, 1680, 3)):
        o.append(_line(mx2(xa), my2(st), mx2(xb), my2(st), sw=4.6, color=RED))
        o.append(_circle(mx2(xa), my2(st), 2.0, fill=RED, sw=0))
        o.append(_circle(mx2(xb), my2(st), 2.0, fill=RED, sw=0))

    return _mk(11, o, "HMM states inferred over time",
               "Các trạng thái HMM theo thời gian",
               "HMM states inferred over time",
               "Biểu đồ gồm chuỗi quan sát và ba trạng thái HMM; trạng thái 3 tương ứng bàn nghiền mòn.",
               "Two-panel chart of observations and HMM states; state 3 marks the worn grinding table.")
