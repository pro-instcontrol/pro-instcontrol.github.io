# -*- coding: utf-8 -*-
"""PPIC Chapter 8 figure supplier C: figures 15-21 (coal-bucket dampers).

All figures are vector redraws of the printed charts in work/ppic8_pages.
"""
import math

from ppicfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()

PALETTE = (BLUE, GREEN, RED, "#7d3c98", "#d68910", "#0e6655", "#154360",
           "#a93226", "#148f77", "#8e44ad", "#ca6f1e", "#1a5276", "#6e2c00")


# ----------------------------------------------------------------- helpers
def _rng(seed):
    s = (seed & 0x7fffffff) or 1

    def nxt():
        nonlocal s
        s = (1103515245 * s + 12345) & 0x7fffffff
        return s / 2147483647.0
    return nxt


def _mark(x, y, kind, r, color):
    if kind == "diamond":
        return _poly([(x, y - r), (x + r * 0.78, y), (x, y + r),
                      (x - r * 0.78, y)], fill=color, sw=0.5, color=color,
                     close=True)
    if kind == "tri":
        return _poly([(x, y - r), (x + r * 0.92, y + r * 0.8),
                      (x - r * 0.92, y + r * 0.8)], fill=color, sw=0.5,
                     color=color, close=True)
    return _circle(x, y, r, fill=color, sw=0.5, color=color)


def _mseries(points, mx, my, color, kind, r=2.6, sw=1.5, dash=""):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=sw, color=color, dash=dash)]
    o += [_mark(px, py, kind, r, color) for px, py in pts]
    return "".join(o)


def _ticks(lo, hi, step, fmt="%d"):
    return [(v, fmt % v) for v in range(lo, hi + 1, step)]


def _fade(t, t0, f, dec, amp, phase, f2=2.15, a2=0.16):
    if t < t0:
        return 0.0
    s = t - t0
    e = math.exp(-dec * s)
    return amp * e * math.sin(2 * math.pi * f * s + phase) \
        + a2 * amp * e * math.sin(2 * math.pi * f2 * s + 0.6)


# ------------------------------------------------------------------- 15
@_reg
def fig_f15():
    """Acceleration reduction rates: four line-chart panels (a)-(d)."""
    o = []
    # shared legend
    o.append(_mark(226, 10, "diamond", 3.0, INK))
    o.append(T(235, 12, "El Centro", 7.0, anchor="start"))
    o.append(_mark(326, 10, "tri", 3.1, BLUE))
    o.append(T(335, 12, "Impvall", 7.0, anchor="start"))
    o.append(_mark(406, 10, "dot", 2.9, RED))
    o.append(T(415, 12, "RGB", 7.0, anchor="start"))

    panels = [
        (50, 28, (-40, 30),
         [(-11, -13, 6, 2), (-21, -11.5, -1.5, -6), (7, -15, 16, 5)],
         "(a) Peak / frequent"),
        (362, 28, (-20, 30),
         [(-6, -6.5, 10, 7), (-6.5, -11, 9.5, 4.5), (0.5, -1, 21, 16.5)],
         "(b) RMS / frequent"),
        (50, 156, (-40, 30),
         [(-9, -3, 18, 12), (-30, -19, 5, 0), (0, 6, 17.5, 17)],
         "(c) Peak / moderate"),
        (362, 156, (-20, 30),
         [(-5.5, 0, 20, 20), (-9, -7, 11.5, 13), (6, 5, 20.5, 27.5)],
         "(d) RMS / moderate"),
    ]
    kinds = ("diamond", "tri", "dot")
    colors = (INK, BLUE, RED)
    for x0, y0, yr, data, title in panels:
        o.append(T(x0, y0 - 5, title, 7.2, color=INK, weight="bold"))
        fr, mx, my = _frame(x0, y0, 248, 78, (1, 4), yr,
                            [(v, str(v)) for v in (1, 2, 3, 4)],
                            _ticks(yr[0], yr[1], 10), xlab="Story",
                            ylab="Rate (%)")
        o.append(fr)
        for vals, kind, col in zip(data, kinds, colors):
            pts = [(s, v) for s, v in zip((1, 2, 3, 4), vals)]
            o.append(_mseries(pts, mx, my, col, kind, r=2.8))
    return _mk(15, o, "Acceleration reduction rates, four panels",
               "Tỷ lệ giảm gia tốc theo bốn điều kiện",
               "Acceleration reduction rates under frequent and moderate earthquakes",
               "Bốn biểu đồ đường: đỉnh và RMS dưới động đất thường gặp và trung bình; "
               "ba đường El Centro, Impvall và RGB.",
               "Four line-chart panels: peak and RMS reduction under frequent and "
               "moderate earthquakes, with El Centro, Impvall and RGB records.")


# ------------------------------------------------------------------- 16
@_reg
def fig_f16():
    """Finite-element model of the four-storey CBD-equipped test structure."""
    o = [_defs()]
    ox, oy, dj, di, dk = 250.0, 244.0, 42.0, 20.0, 28.0

    def P(i, j, k):
        return ox + dj * j + di * i, oy - dk * k - 8.0 * i - 2.0 * j

    def top(i, j):
        return 6 if (i == 2 and j >= 2) else 4

    o.append(_poly([P(0, 0, 0), P(0, 3, 0), P(2, 3, 0), P(2, 0, 0)],
                   fill="#f2efe7", sw=0.8, color="#c3bdb0", close=True))
    # floor beams
    for k in range(5):
        for i in range(3):
            a, b = P(i, 0, k), P(i, 3, k)
            o.append(_line(a[0], a[1], b[0], b[1], color=BLUE, sw=1.7))
        for j in range(4):
            a, b = P(0, j, k), P(2, j, k)
            o.append(_line(a[0], a[1], b[0], b[1], color=BLUE, sw=1.7))
    # raised rear tower beams
    for k in (5, 6):
        a, b = P(2, 2, k), P(2, 3, k)
        o.append(_line(a[0], a[1], b[0], b[1], color=BLUE, sw=1.7))
    # columns
    for i in range(3):
        for j in range(4):
            a, b = P(i, j, 0), P(i, j, top(i, j))
            o.append(_line(a[0], a[1], b[0], b[1], color=BLUE, sw=2.4))
    # green joint markers at the base
    for i in range(3):
        for j in range(4):
            x, y = P(i, j, 0)
            o.append(_rect(x - 2.2, y - 2.2, 4.4, 4.4, fill=GREEN, sw=0))
    # LINK elements (the three coal-bucket dampers) on the front lower storey
    for j in range(3):
        a, b = P(0, j, 0.75), P(0, j + 1, 0.75)
        o.append(_line(a[0], a[1], b[0], b[1], color=RED, sw=3.4))
        for x, y in (a, b):
            o.append(_circle(x, y, 2.4, fill=GREEN, sw=0))
        o.append(T((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 11,
                   "CBD%d" % (3 - j), 6.8, color=RED))
    # key
    o.append(_line(60, 260, 78, 260, color=BLUE, sw=2.6))
    o.append(T(84, 262, "Frame", 7.0, anchor="start"))
    o.append(_line(150, 260, 168, 260, color=RED, sw=3.4))
    o.append(T(174, 262, "LINK (CBD)", 7.0, anchor="start"))
    o.append(_circle(286, 260, 2.8, fill=GREEN, sw=0))
    o.append(T(294, 262, "Node", 7.0, anchor="start"))
    return _mk(16, o, "Finite-element model with coal-bucket dampers",
               "Mô hình phần tử hữu hạn của kết cấu",
               "Finite-element model of the subject structure",
               "Mô hình khung không gian bốn tầng trong SAP2000, có ba phần tử LINK "
               "mô phỏng các bộ giảm chấn phễu than CBD1-CBD3.",
               "SAP2000 space-frame model of the four-storey test structure; three "
               "LINK elements represent coal-bucket dampers CBD1-CBD3.")


# ------------------------------------------------------------------- 17
@_reg
def fig_f17():
    """Test-versus-FEA time-history comparison, three panels."""
    o = []
    panels = [
        (50, "(a) El Centro drift", 2.0,
         [(INK, "Test", "dot", 1.55, 0.0), (RED, "FEA", "dot", 1.42, 0.12)],
         [(v, "%g" % v) for v in (-2, -1, 0, 1, 2)]),
        (260, "(b) Impvall drift", 2.0,
         [(INK, "Test", "dot", 1.5, 0.0), (RED, "FEA", "dot", 1.4, 0.15)],
         [(v, "%g" % v) for v in (-2, -1, 0, 1, 2)]),
        (470, "(c) CBD3 displacement", 5.0,
         [(INK, "El Centro", "dot", 4.1, 0.0), (RED, "Impvall", "dot", 3.7, 0.2)],
         [(v, "%g" % v) for v in (-5, 0, 5)]),
    ]
    for x0, title, ymax, series, yt in panels:
        o.append(T(x0, 26, title, 7.2, color=INK, weight="bold"))
        fr, mx, my = _frame(x0, 40, 170, 190, (0, 5), (-ymax, ymax),
                            [(v, str(v)) for v in (0, 1, 2, 3, 4, 5)],
                            yt, xlab="Time (s)", ylab="u (mm)")
        o.append(fr)
        ts = [5.0 * i / 110 for i in range(111)]
        for col, lab, kind, amp, ph in series:
            pts = [(t, _fade(t, 1.25, 3.1, 0.85, amp, ph)) for t in ts]
            o.append(_poly([(mx(a), my(b)) for a, b in pts], sw=1.4, color=col,
                           dash="4 2" if lab in ("FEA", "Impvall") else ""))
        for i, (col, lab, kind, amp, ph) in enumerate(series):
            yy = 53 + i * 11
            o.append(_line(x0 + 116, yy - 2, x0 + 130, yy - 2, sw=1.6,
                           color=col, dash="4 2" if i else ""))
            o.append(T(x0 + 134, yy, lab, 6.4, anchor="end"))
    return _mk(17, o, "Test versus FEA response comparison",
               "So sánh đáp ứng thí nghiệm và mô phỏng FEA",
               "Test-versus-FEA response comparison under three cases",
               "Ba bảng so sánh thời gian: (a) trượt tầng El Centro, (b) trượt tầng "
               "Impvall giữa thí nghiệm và FEA, (c) chuyển vị của CBD3.",
               "Three time-history panels: (a) El Centro and (b) Impvall story drift "
               "from test and FEA, and (c) CBD3 displacement under both records.")


# ------------------------------------------------------------------- 18
@_reg
def fig_f18():
    """(a) far-field and (b) near-field response spectra (53 records)."""
    o = []

    def mean_curve(t):
        if t < 1.5:
            return 1.0 + 1.6 * (1.0 - math.exp(-t / 0.7))
        return 2.6 * math.exp(-0.40 * (t - 1.5)) + 0.28

    specs = []
    for pi, (x0, title, seed, n) in enumerate(
            [(56, "(a) Far-field", 1201, 22), (360, "(b) Near-field", 2401, 28)]):
        o.append(T(x0, 26, title, 7.2, color=INK, weight="bold"))
        fr, mx, my = _frame(x0, 34, 262, 192, (0, 6), (0, 5),
                            [(v, str(v)) for v in range(7)],
                            [(v, str(v)) for v in range(6)],
                            xlab="T (s)", ylab="Accel (g)")
        o.append(fr)
        r = _rng(seed)
        for c in range(n):
            tp = 0.08 + 0.55 * r()
            hp = 1.5 + 3.0 * r()
            wp = 0.08 + 0.24 * r()
            t2 = 0.9 + 1.9 * r()
            h2 = 0.4 + 1.0 * r()
            pts = []
            for i in range(141):
                t = 6.0 * i / 140
                v = (hp * math.exp(-((t - tp) / wp) ** 2)
                     + h2 * math.exp(-((t - t2) / (0.4 + 0.5 * r())) ** 2)
                     + 0.12 + 0.22 * r()
                     + 0.16 * math.exp(-((t - 0.3) / 0.9) ** 2))
                pts.append((mx(t), my(max(0.0, min(v, 4.95)))))
            o.append(_poly(pts, sw=0.65, color=PALETTE[c % len(PALETTE)]))
        o.append(_poly([(mx(6.0 * i / 140), my(mean_curve(6.0 * i / 140)))
                        for i in range(141)], sw=1.8, color=RED, dash="5 3"))
        specs.append(x0)
    o.append(_line(318, 264, 332, 264, color=RED, sw=1.8, dash="5 3"))
    o.append(T(338, 266, "Mean", 7.0, anchor="start"))
    return _mk(18, o, "Far-field and near-field response spectra",
               "Phổ phản ứng động đất trường xa và trường gần",
               "Far-field and near-field seismic response spectra",
               "Phổ gia tốc phản ứng của 22 động đất trường xa và 28 động đất trường gần, "
               "có đường trung bình màu đỏ.",
               "Acceleration response spectra of 22 far-field and 28 near-field records "
               "with the red dashed mean spectrum.")


# ------------------------------------------------------------------- 19
@_reg
def fig_f19():
    """Reduction rates over 53 excitations, displacement and acceleration."""
    o = []
    cfg = [
        (56, "(a) Displacement", (-10, 45), 17.2, 9.6, -8, 40, 23, 38, 991),
        (360, "(b) Acceleration", (-15, 30), 2.1, -1.9, -12, 14, 23, 9, 992),
    ]
    for x0, title, yr, mrms, mpeak, lo, hi, hi_id, lo_id, seed in cfg:
        o.append(T(x0, 26, title, 7.2, color=INK, weight="bold"))
        fr, mx, my = _frame(x0, 34, 262, 192, (0, 53), yr,
                            [(v, str(v)) for v in (0, 10, 20, 30, 40, 50)],
                            _ticks(yr[0], yr[1], 10),
                            xlab="Seismic wave number", ylab="Rate (%)")
        o.append(fr)
        r = _rng(seed)

        def spread():
            return r() + r() + r() - 1.5

        rms = [max(lo, min(hi, mrms + 6.6 * spread())) for _ in range(54)]
        peak = [max(lo, min(hi, mpeak + 7.4 * spread())) for _ in range(54)]
        if title.startswith("(a)"):
            rms[hi_id], rms[lo_id], peak[lo_id] = 39.8, -7.7, -6.0
        else:
            rms[hi_id], peak[lo_id] = 24.0, -11.0
        for n in range(1, 54):
            o.append(_mark(mx(n), my(peak[n]), "dot", 2.5, RED))
            o.append(_mark(mx(n), my(rms[n]), "tri", 2.9, BLUE))
        for val, lab in ((mrms, "Mean (RMS)"), (mpeak, "Mean (peak)")):
            yy = my(val)
            o.append(_line(x0, yy, x0 + 262, yy, color=GREY, sw=0.9, dash="4 3"))
            o.append(T(x0 + 16, yy - 4, lab, 6.4, anchor="start", color=GREY))
        hi_y = my(rms[hi_id]) - 5
        o.append(T(mx(hi_id) + 5, hi_y, "No. 23", 6.4, anchor="start"))
        lo_y = my(rms[lo_id] if title.startswith("(a)") else peak[lo_id]) - 4
        o.append(T(mx(lo_id) + 5, lo_y, "No. %d" % lo_id, 6.4, anchor="start"))
    o.append(_mark(244, 270, "dot", 2.5, RED))
    o.append(T(253, 272, "Peak", 7.0, anchor="start"))
    o.append(_mark(330, 270, "tri", 2.9, BLUE))
    o.append(T(339, 272, "RMS", 7.0, anchor="start"))
    return _mk(19, o, "Reduction rates over 53 excitations",
               "Tỷ lệ giảm qua 53 bộ dao động động đất",
               "Displacement and acceleration reduction rates over 53 excitations",
               "Đồ thị phân tán tỷ lệ giảm của 53 dao động: chuyển vị và gia tốc, "
               "với giá trị đỉnh và RMS cùng đường trung bình.",
               "Scatter of peak and RMS reduction rates over 53 excitations: "
               "(a) displacement and (b) acceleration, with dashed mean levels.")


# ------------------------------------------------------------------- 20
@_reg
def fig_f20():
    """(a) Fourier amplitude spectra with CBD band, (b) drift response."""
    o = [_defs()]

    def g(f, c, w, a=1.0):
        return a * math.exp(-((f - c) / w) ** 2)

    # ---- (a) Fourier amplitude spectra
    o.append(T(52, 24, "(a) Fourier amplitude", 7.2, color=INK, weight="bold"))
    fr, mx, my = _frame(52, 32, 272, 182, (10, 30), (0, 2.5),
                        [(v, str(v)) for v in (10, 15, 20, 25, 30)],
                        [(0, "0"), (0.5, "0.5"), (1, "1.0"),
                         (1.5, "1.5"), (2, "2.0"), (2.5, "2.5")],
                        xlab="Frequency (Hz)", ylab="Amplitude")
    o.append(fr)
    bx, bw = mx(18), mx(22) - mx(18)
    o.append(_rect(bx, 32, bw, 182, fill="#e6e6e6", sw=0))
    o.append(_line(bx, 32, bx, 214, color=GREY, sw=0.9, dash="3 2"))
    o.append(_line(bx + bw, 32, bx + bw, 214, color=GREY, sw=0.9, dash="3 2"))
    r = _rng(7301)
    p23, p38 = [], []
    for i in range(301):
        f = 10 + 20 * i / 300
        n = r()
        v23 = (0.16 + 0.20 * n + 1.45 * g(f, 12.55, 0.20)
               + 1.82 * g(f, 14.25, 0.17) + 1.18 * g(f, 16.55, 0.24)
               + 1.85 * g(f, 18.70, 0.32) + 0.62 * g(f, 19.75, 0.22)
               + 0.35 * g(f, 11.3, 0.18))
        v38 = (0.12 + 0.15 * n + 0.42 * g(f, 10.5, 0.22)
               + 0.48 * g(f, 12.3, 0.26) + 0.56 * g(f, 18.4, 0.42)
               + 0.34 * g(f, 22.2, 0.55) + 0.28 * g(f, 15.6, 0.30))
        p23.append((mx(f), my(max(0, min(v23, 2.48)))))
        p38.append((mx(f), my(max(0, min(v38, 1.05)))))
    o.append(_poly(p38, sw=1.3, color=BLUE))
    o.append(_poly(p23, sw=1.3, color=RED, dash="4 2"))
    o.append(_ar(146, 60, 158, 60, color=GREY, sw=1.0))
    o.append(_ar(226, 60, 214, 60, color=GREY, sw=1.0))
    o.append(T(222, 52, "Operating range", 6.4, anchor="start", color=INK))
    o.append(_line(150, 262, 168, 262, color=RED, sw=1.6, dash="4 2"))
    o.append(T(173, 264, "No. 23", 7.0, anchor="start"))
    o.append(_line(224, 262, 242, 262, color=BLUE, sw=1.6))
    o.append(T(247, 264, "No. 38", 7.0, anchor="start"))

    # ---- (b) displacement response, two records
    o.append(T(378, 24, "(b) Interstory drift", 7.2, color=INK, weight="bold"))
    for y0, yr, aw, ao, lab in (
            (32, (-1, 1), 0.30, 0.95, "No. 23"),
            (148, (-0.2, 0.2), 0.045, 0.115, "No. 38")):
        fr, mx, my = _frame(378, y0, 250, 74, (0, 6), yr,
                            [(v, str(v)) for v in range(7)],
                            [(yr[0], "%g" % yr[0]), (0, "0"),
                             (yr[1], "%g" % yr[1])],
                            xlab="Time (s)", ylab="u (mm)")
        o.append(fr)
        ts = [6.0 * i / 180 for i in range(181)]
        p_out = [(mx(t), my(_fade(t, 0.55, 6.2, 0.95, ao, 0.25)))
                 for t in ts]
        p_with = [(mx(t), my(_fade(t, 0.55, 6.2, 2.6, aw, 0.0)))
                  for t in ts]
        o.append(_poly(p_out, sw=1.3, color=BLUE, dash="4 2"))
        o.append(_poly(p_with, sw=1.4, color=RED))
        o.append(_rect(mx(0.25), y0 + 5, 34, 11, fill="#e8f4e0", sw=0.6,
                       stroke="#7aa86a"))
        o.append(T(mx(0.25) + 17, y0 + 13, lab, 6.4, color="#1e5b28"))
    o.append(_line(420, 140, 438, 140, color=RED, sw=1.6))
    o.append(T(443, 142, "With CBDs", 6.4, anchor="start"))
    o.append(_line(510, 140, 528, 140, color=BLUE, sw=1.6, dash="4 2"))
    o.append(T(533, 142, "Without CBDs", 6.4, anchor="start"))
    return _mk(20, o, "Fourier spectra and drift reduction",
               "Phổ Fourier và giảm trượt tầng giữa hai dao động",
               "Fourier spectra of excitations 23 and 38 and drift reduction",
               "Phổ biên độ Fourier của dao động 23 và 38 với dải tần hoạt động của CBD; "
               "so sánh đáp ứng chuyển vị có và không có CBD.",
               "Fourier amplitude spectra of excitations 23 and 38 with the CBD "
               "operating band, and drift response with and without CBDs.")


# ------------------------------------------------------------------- 21
@_reg
def fig_f21():
    """Reduction rates versus structural frequency, displacement/acceleration."""
    o = []
    x0, w = 64.0, 560.0
    specs = [
        (28, 94, (0, 20), 0, "(a) Displacement",
         [(0.85, 15.0), (0.9, 16.5), (1.0, 17.4), (1.1, 17.6), (1.2, 17.5),
          (1.3, 17.2), (1.4, 16.5), (1.6, 15.6), (1.8, 14.2), (2.0, 12.8),
          (2.2, 11.2)],
         [(0.85, 9.0), (0.9, 9.7), (1.0, 9.3), (1.1, 9.6), (1.2, 9.6),
          (1.3, 9.3), (1.4, 9.4), (1.6, 8.6), (1.8, 7.6), (2.0, 6.8),
          (2.2, 5.9)]),
        (166, 90, (-10, 10), 1, "(b) Acceleration",
         [(0.85, -0.5), (0.9, 1.0), (1.0, 2.0), (1.1, 1.9), (1.2, 1.4),
          (1.3, 1.3), (1.4, 1.6), (1.5, 2.0), (1.6, 2.1), (1.8, 1.4),
          (2.0, 0.4), (2.2, -0.8)],
         [(0.85, -5.5), (0.9, -3.0), (1.0, -1.9), (1.1, -1.5), (1.2, -1.5),
          (1.3, -2.2), (1.4, -2.8), (1.5, -2.6), (1.6, -1.2), (1.8, -0.8),
          (2.0, -1.6), (2.2, -3.0)]),
    ]
    for y0, h, yr, idx, title, rms, peak in specs:
        o.append(T(x0, y0 - 8, title, 7.2, color=INK, weight="bold"))
        fr, mx, my = _frame(x0, y0, w, h, (0.8, 2.2), yr,
                            [(v, "%g" % v) for v in
                             (0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2)],
                            _ticks(yr[0], yr[1], 2),
                            xlab="Structure frequency (T/T1)", ylab="Rate (%)")
        o.append(fr)
        for xv in (0.85, 1.4):
            o.append(_line(mx(xv), y0, mx(xv), y0 + h, color=GREY, sw=0.7,
                           dash="3 2"))
        o.append(_mseries(rms, mx, my, BLUE, "dot", r=2.4))
        o.append(_mseries(peak, mx, my, RED, "dot", r=2.4))
        lab_y = my(11 if idx == 0 else 4.2)
        o.append(T(mx(0.85) + 4, lab_y, "← 0.85T₁", 6.4, anchor="start"))
        o.append(T(mx(1.4) + 4, lab_y, "← 1.4T₁", 6.4, anchor="start"))
        o.append(T(mx(1.22), my(rms[6][1]) - 4, "← RMS", 6.4, anchor="start"))
        o.append(T(mx(1.22), my(peak[6][1]) - 4, "← Peak", 6.4,
                   anchor="start"))
    return _mk(21, o, "Reduction rates versus structural frequency",
               "Tỷ lệ giảm theo tần số kết cấu",
               "Reduction rates versus structural frequency",
               "Tỷ lệ giảm chuyển vị và gia tốc khi thay đổi tần số kết cấu "
               "T/T1, với các mốc 0,85T1 và 1,4T1.",
               "Displacement and acceleration reduction rates versus structural "
               "frequency ratio T/T1, marked at 0.85T1 and 1.4T1.")
