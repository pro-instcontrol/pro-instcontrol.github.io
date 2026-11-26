# -*- coding: utf-8 -*-
"""Vector figures 5-8 for PPIC Chapter 9 (predictive maintenance).

Figure 5 redraws the two-branch algorithm flow printed on p231, Figure 6 the
Q-Q plot of T2 quantiles against chi-squared quantiles on p232, and Figures
7 and 8 the Hotelling T2 control charts for signals recorded 2 and 5 weeks
after grinding-table replacement on p233.  Each figure is registered in
``FIGS`` by ``@_reg`` and returns the standard five-tuple from ``_mk``.
"""
import math
import random

from ppicfig9_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _box(x, y, w, lines, size=6.0, fill="#eef3fb"):
    """Centred flow-chart box; returns (markup, height)."""
    h = 6.0 + 7.0 * len(lines)
    o = [_rect(x, y, w, h, fill, sw=0.9)]
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y + 8.0 + i * 7.0, ln, size))
    return "".join(o), h


def _down(x, y1, y2, color=INK):
    return _ar(x, y1, x, y2, sw=1.0, color=color)


def _star(cx, cy, r, color):
    """Five-point star as a vector polygon (used for chart markers)."""
    pts = []
    for k in range(10):
        a = -math.pi / 2.0 + k * math.pi / 5.0
        rr = r if k % 2 == 0 else r * 0.43
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return _poly(pts, fill=color, sw=0.25, color=color, close=True)


def _rot_ylabel(x, y, s, size=6.8, color=INK):
    return ('<text x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, x, y, size, color, s))


def _rand(seed, n):
    """Deterministic uniform samples in [0, 1)."""
    x = seed
    out = []
    for _ in range(n):
        x = (1103515245 * x + 12345) % 2147483648
        out.append(x / float(0x7fffffff))
    return out


# ------------------------------------------------------------------- 9.5
@_reg
def fig_f05():
    """Two-branch algorithm flow: offline training and online updating."""
    o = [_defs()]
    o.append(T(340, 12, "Flow diagram of the proposed algorithm",
               8.6, color=INK, weight="600"))
    o.append(T(155, 24, "Offline procedure", 7.2, color=BLUE, weight="600"))
    o.append(T(507, 24, "Online procedure", 7.2, color=BLUE, weight="600"))

    left = [
        ["Acquisition of the acoustic", "signals for training",
         "y[i], i = 0,1,2,..."],
        ["Computing of spectrogram", "sequence",
         "S_p[f,n], f ∈ {f_1,...,f_p}", "n = 0,1,...,N−1 (Eq.1)"],
        ["Calculation of observations", "X[n], n = 0,1,...,N−1", "(Eq.3, 4)"],
        ["Computing of T² statistics", "X̄, S, T² (Eq.5, 6, 7)"],
        ["Calculation of observations", "O[n] (Eq.10)"],
        ["K-means clustering", "Calculation of C_j, j = 1,...,4", "(Eq.11)"],
        ["Forming of HMM observations", "Ô[n], n = 0,1,...,N−1", "(Eq.11)"],
        ["HMM training, determining", "of parameters", "A, B, π"],
    ]
    y = 30.0
    for k, lines in enumerate(left):
        box, h = _box(30, y, 250, lines)
        o.append(box)
        y += h
        if k < len(left) - 1:
            o.append(_down(155, y, y + 5))
            y += 5

    # Online branch: initialization, decision diamond, sliding-window steps.
    online = [
        (30.0, ["Initialization of sequence", "number of window data", "n ← 0"]),
        (88.0, ["Acquisition of data from", "sliding window",
                "y[0],...,y[Lw−1]"]),
        (120.0, ["Computing of spectrogram", "S_p[f,n] (Eq.1)"]),
        (145.0, ["Calculation of vector", "X[n] (Eq.3, 4)"]),
        (170.0, ["Calculation of observations", "O[n] (Eq.10)"]),
        (195.0, ["Calculation of HMM", "observations", "Ô[n] (Eq.11)"]),
        (227.0, ["HMM updating"]),
    ]
    for y, lines in online:
        box, h = _box(395, y, 225, lines)
        o.append(box)
    o.append(_down(507, 57, 60, BLUE))
    o.append(_poly([(459, 72), (507, 61), (555, 72), (507, 83)],
                   fill="#fff8e8", sw=0.9, color=INK, close=True))
    o.append(T(507, 75, "Time counter", 6.4))
    o.append(_down(507, 83, 87, BLUE))
    for y1, y2 in ((115, 119), (140, 144), (165, 169), (190, 194), (222, 226)):
        o.append(_down(507, y1, y2, BLUE))
    o.append(_down(507, 240, 244, BLUE))
    o.append(_poly([(470, 245), (544, 245), (566, 270), (448, 270)],
                   fill="#fff4e0", sw=0.9, color=INK, close=True))
    o.append(T(507, 255, "ESTIMATED", 6.4, weight="600"))
    o.append(T(507, 264, "STATE", 6.4, weight="600"))

    # Feedback loop from HMM updating to the time counter.
    o.append(_line(620, 234, 648, 234, sw=1.0, color=BLUE))
    o.append(_line(648, 234, 648, 72, sw=1.0, color=BLUE))
    o.append(_ar(648, 72, 557, 72, sw=1.0, color=BLUE))
    o.append(_rect(622, 150, 54, 16, fill="#ffffff", sw=0.8))
    o.append(T(649, 161, "n ← n + 1", 5.8, color=BLUE))

    return _mk(5, o,
               "Flow diagram of the proposed algorithm",
               "Sơ đồ thuật toán đề xuất: quy trình ngoại tuyến và trực tuyến",
               "Flow diagram of the proposed algorithm: offline and online procedure",
               "Quy trình ngoại tuyến gồm thu tín hiệu, phổ, thống kê T² và huấn luyện HMM; quy trình trực tuyến cập nhật trạng thái HMM.",
               "The offline branch acquires signals and builds the spectrogram, T² chart and HMM; the online branch extracts features and updates the estimated state.")


# ------------------------------------------------------------------- 9.6
@_reg
def fig_f06():
    """Q-Q plot of T² quantiles versus chi-squared quantiles (6 days)."""
    o = [T(340, 12, "Q-Q plot", 8.6, color=INK, weight="600")]
    fr, mx, my = _frame(90, 32, 520, 196, (0.0, 28.0), (0.0, 28.0),
                        [(v, "%g" % v) for v in range(0, 28, 5)],
                        [(v, "%g" % v) for v in range(0, 28, 5)],
                        "χ² quantiles", "")
    o.append(fr)
    o.append(_rot_ylabel(44, 130, "T² quantiles"))
    o.append(_line(mx(0), my(0), mx(28), my(28), sw=2.0, color=RED))
    for i in range(64):
        q = 0.35 + 27.4 * i / 63.0
        dev = 0.18 * math.sin(i * 1.7) + 0.12 * math.cos(i * 0.9)
        if i > 54:
            dev += 0.11 * (i - 54)
        v = min(27.8, q + dev)
        o.append(_star(mx(q), my(v), 1.6, BLUE))
    return _mk(6, o,
               "Q-Q plot for the recorded acoustic signal",
               "Đồ thị Q-Q cho tín hiệu âm thanh ghi nhận 6 ngày sau khi thay bàn nghiền",
               "Q-Q plot for the acoustic signal recorded 6 days after grinding-table replacement",
               "Các điểm nằm gần đường 45°, phù hợp với phân phối chi bình phương của thống kê T².",
               "The points follow the 45 degree reference line, supporting a chi-squared distribution for the T² statistic.")


def _t2_chart(o, x0, y0, w, h, xmax, ymax, yt, title, npts, seed,
              high, outliers):
    """Shared Hotelling T² chart frame, UCL line and star markers."""
    o.append(T(340, 12, title, 8.2, color=INK, weight="600"))
    fr, mx, my = _frame(x0, y0, w, h, (0.0, xmax), (0.0, ymax),
                        [(v, "%g" % v) for v in range(0, int(xmax) + 1, 100)],
                        [(v, "%g" % v) for v in yt], "Samples", "")
    o.append(fr)
    o.append(_rot_ylabel(x0 - 46, y0 + h / 2.0, "T² statistics"))
    ucl = 36.12
    o.append(_line(mx(0), my(ucl), mx(xmax), my(ucl), sw=2.0, color=BLUE))
    o.append(T(x0 + w - 4, my(ucl) - 4, "UCL = 36.12", 6.4,
               anchor="end", color=BLUE))
    u = _rand(seed, npts * 2)
    for i in range(npts):
        x = 4.0 + (xmax - 8.0) * u[2 * i]
        y = 2.0 + (high - 2.0) * u[2 * i + 1]
        if u[2 * i + 1] > 0.88:
            y += 5.0
        o.append(_star(mx(x), my(min(ymax - 1.0, y)), 2.6, RED))
    for x, y in outliers:
        o.append(_star(mx(x), my(y), 2.9, RED))
    return o


# ------------------------------------------------------------------- 9.7
@_reg
def fig_f07():
    """T² control chart, signal recorded 2 weeks after replacement."""
    o = _t2_chart([], 90, 32, 520, 196, 600.0, 80.0,
                  range(0, 81, 10),
                  "T² control chart for acoustic signal recorded on 02 02 2012",
                  240, 20120202, 27.0,
                  [(45, 38), (120, 43), (170, 41), (355, 40),
                   (382, 71), (440, 39), (475, 37), (515, 44)])
    return _mk(7, o,
               "T² control chart, 2 weeks after replacement",
               "Biểu đồ kiểm soát T² cho tín hiệu ghi nhận 2 tuần sau khi thay bàn nghiền",
               "T² control chart for the signal recorded 2 weeks after replacement",
               "Hầu hết các điểm nằm dưới UCL = 36,12; chỉ một số ít vượt giới hạn.",
               "Most points remain below UCL = 36.12; only a few exceed the limit.")


# ------------------------------------------------------------------- 9.8
@_reg
def fig_f08():
    """T² control chart, signal recorded 5 weeks after replacement."""
    o = _t2_chart([], 90, 32, 520, 196, 600.0, 120.0,
                  range(0, 121, 20),
                  "T² control chart for acoustic signal recorded on 24 02 2012",
                  300, 20240224, 45.0,
                  [(32, 120), (48, 116), (96, 112), (150, 105),
                   (215, 107), (300, 100), (420, 101), (505, 96)])
    # Extra high band: wear pushes a large share of points above the UCL.
    u = _rand(773, 150)
    for i in range(75):
        x = 6.0 + 588.0 * u[2 * i]
        y = 48.0 + 67.0 * u[2 * i + 1]
        o.append(_star(90 + x / 600.0 * 520,
                       32 + 196 - y / 120.0 * 196, 2.6, RED))
    return _mk(8, o,
               "T² control chart, 5 weeks after replacement",
               "Biểu đồ kiểm soát T² cho tín hiệu ghi nhận 5 tuần sau khi thay bàn nghiền",
               "T² control chart for the signal recorded 5 weeks after replacement",
               "Nhiều điểm nằm trên UCL = 36,12, cho thấy bàn nghiền đang mòn dần.",
               "Many points now lie above UCL = 36.12, indicating progressive wear of the grinding table.")
