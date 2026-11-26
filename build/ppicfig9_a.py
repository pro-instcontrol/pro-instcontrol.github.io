# -*- coding: utf-8 -*-
"""Vector figures 9.1-9.4 for PPIC chapter 9 (predictive maintenance).

Genuine vector redraws of the printed diagrams on PDF pages 221, 222, 225 and
230: the coal-grinding subsystem configuration, a simplified section of a new
and a worn grinding table, an acoustic spectrogram with dominant frequency
bands, and the three-state hidden Markov model with transition/emission arrows.
"""
import math

from ppicfig9_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()


# ------------------------------------------------------------------- fig 9.1
@_reg
def fig_f01():
    o = [_defs()]
    o.append(T(340, 13, "Coal-grinding subsystem configuration",
               9.0, color=INK, weight="600"))

    # raw-coal feed hopper and central chute
    o.append(_poly([(328, 34), (352, 34), (347, 66), (333, 66)],
                   fill="#eef3fb", sw=1.1, close=True))
    o.append(T(340, 26, "Coal feed", 7.0, color=INK))
    o.append(_ar(340, 40, 340, 118, color=GREY, sw=1.2))

    # mill shell in simplified vertical section
    o.append(_path("M220,255 L220,120 C220,96 470,96 470,120 L470,255 Z",
                   fill="#fbfaf7", sw=1.5))
    o.append(_rect(333, 66, 14, 66, fill="#e8eef7", sw=1.0))

    # classifier deflector plates in the upper part of the mill
    for yy in (118, 132, 146):
        o.append(_line(236, yy, 264, yy + 12, sw=1.0, color=GREY))
        o.append(_line(426, yy, 454, yy - 12, sw=1.0, color=GREY))

    # fine-powder outlet duct
    o.append(_path("M455,116 C495,104 520,92 600,92",
                   fill="none", sw=2.2, color=GREY))
    o.append(_ar(598, 92, 622, 92, color=GREY, sw=2.0))

    # coarse particle recirculation back onto the grinding table
    o.append(_path("M430,150 C438,172 431,188 416,202",
                   fill="none", sw=1.2, color=BLUE, dash="4 3"))
    o.append(_ar(419, 197, 414, 205, color=BLUE, sw=1.2))

    # grinding table with hub and three rollers
    o.append(_ellipse(345, 213, 92, 13, fill="#dfe5ec", sw=1.2))
    o.append(_ellipse(345, 213, 16, 5, fill="#c3ccd8", sw=1.0))
    for cx in (296, 345, 394):
        o.append(_circle(cx, 191, 18, fill="#c9d2dc", sw=1.1))
        o.append(_circle(cx, 191, 5, fill="#aeb9c6", sw=0.8))

    # rotating central shaft and its direction of rotation
    o.append(_line(345, 132, 345, 200, sw=1.4, color=INK))
    o.append(_path("M330,170 C330,158 360,158 360,170",
                   fill="none", sw=1.1, color=BLUE))
    o.append(_ar(360, 168, 358, 163, color=BLUE, sw=1.1))

    # primary-air inlet and upward air flow through the table
    o.append(_ar(548, 260, 442, 238, color=GREEN, sw=1.8))
    for xx in (285, 345, 405):
        o.append(_ar(xx, 246, xx, 231, color=GREEN, sw=1.2))

    # base and ground line
    o.append(_line(205, 258, 486, 258, sw=1.3))
    x = 205
    while x <= 486:
        o.append(_line(x, 258, x - 5, 264, sw=0.6, color=GREY))
        x += 9

    # component labels with leader lines
    o.append(T(150, 126, "Classifier / deflector plates", 7.0, color=BLUE))
    o.append(_line(207, 126, 236, 128, sw=0.8, color=GREY))
    o.append(T(150, 190, "Grinding rollers", 7.0, color=INK))
    o.append(_line(181, 190, 278, 191, sw=0.8, color=GREY))
    o.append(T(150, 225, "Mill body", 7.0, color=INK))
    o.append(_line(168, 223, 220, 220, sw=0.8, color=GREY))
    o.append(T(345, 248, "Grinding table", 7.0, color=INK))
    o.append(T(575, 82, "Fine powder to burners", 7.0, color=INK))
    o.append(T(545, 150, "Coarse particles", 7.0, color=INK))
    o.append(_line(513, 150, 452, 156, sw=0.8, color=GREY, dash="3 2"))
    o.append(T(520, 270, "Primary air", 7.0, color=GREEN))

    return _mk(1, o, "Coal-grinding subsystem configuration",
               "Cấu hình hệ thống nghiền than",
               "Coal-grinding subsystem configuration",
               "Sơ đồ cắt ngang hệ thống nghiền than: than đầu vào, thân máy, bàn nghiền, con lăn, bộ phân loại và ống dẫn.",
               "Cross-section of the coal-grinding subsystem: coal feed, mill body, grinding table, rollers, classifier and ducts.")


# ------------------------------------------------------------------- fig 9.2
@_reg
def fig_f02():
    o = [_defs()]
    o.append(T(340, 13, "New and worn grinding tables - simplified section",
               9.0, color=INK, weight="600"))
    o.append(_line(340, 46, 340, 265, sw=0.8, color=GREY, dash="4 4"))

    # (a) new table: a smooth, even wear track under the grinding roller
    o.append(T(175, 32, "New grinding table", 8.2, color=BLUE, weight="600"))
    o.append(_rect(80, 185, 190, 32, fill="#d9dee4", sw=1.1))
    o.append(_line(80, 185, 270, 185, sw=2.0, color=INK))
    o.append(_circle(175, 160, 24, fill="#c9d2dc", sw=1.2))
    o.append(_circle(175, 160, 6, fill="#aeb9c6", sw=0.9))
    o.append(_path("M149,166 C148,146 202,146 201,166",
                   fill="none", sw=1.0, color=BLUE))
    o.append(_ar(201, 164, 200, 159, color=BLUE, sw=1.0))
    o.append(T(90, 108, "Roller", 6.8, color=GREY, anchor="start"))
    o.append(_line(115, 105, 158, 146, sw=0.8, color=GREY))
    o.append(T(175, 240, "Smooth, even surface", 7.0, color=INK))

    # (b) worn table: a deeply grooved, uneven track with material loss
    o.append(T(505, 32, "Worn grinding table", 8.2, color=RED, weight="600"))
    o.append(_rect(410, 185, 190, 32, fill="#d9dee4", sw=1.1))
    ridge = [(410, 185), (422, 177), (434, 190), (446, 173), (458, 192),
             (470, 176), (482, 189), (494, 172), (506, 193), (518, 175),
             (530, 190), (542, 174), (554, 191), (566, 176), (578, 188),
             (590, 181), (600, 185), (600, 217), (410, 217)]
    o.append(_poly(ridge, fill="#c8b49c", sw=1.0, color="#8c6f5a", close=True))
    o.append(_circle(505, 150, 24, fill="#c9d2dc", sw=1.2))
    o.append(_circle(505, 150, 6, fill="#aeb9c6", sw=0.9))
    o.append(_path("M479,156 C478,136 532,136 531,156",
                   fill="none", sw=1.0, color=BLUE))
    o.append(_ar(531, 154, 530, 149, color=BLUE, sw=1.0))
    o.append(T(610, 108, "Roller", 6.8, color=GREY, anchor="end"))
    o.append(_line(587, 105, 535, 142, sw=0.8, color=GREY))
    o.append(T(505, 240, "Grooved, uneven surface", 7.0, color=INK))
    o.append(T(505, 255, "Material loss", 6.6, color=RED))

    return _mk(2, o, "New grinding table versus worn grinding table",
               "Bàn nghiền mới và bàn nghiền mòn",
               "New grinding table versus worn grinding table",
               "So sánh bàn nghiền mới (trái, bề mặt nhẵn) và bàn nghiền mòn (phải, bề mặt rãnh sâu).",
               "Simplified section of a new grinding table (left) and a worn grinding table (right) with grooves and material loss.")


# ------------------------------------------------------------------- fig 9.3
@_reg
def fig_f03():
    o = [_defs()]
    o.append(T(340, 13, "Spectrogram of an acoustic signal",
               9.0, color=INK, weight="600"))
    x0, y0, pw, ph = 95.0, 40.0, 515.0, 180.0
    xr, yr = (0.0, 40.0), (0.0, 2100.0)

    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * pw

    def my(v):
        return y0 + ph - (v - yr[0]) / (yr[1] - yr[0]) * ph

    # colour-coded spectral intensity: strong low-frequency energy plus bands
    rows, cols = 14, 34
    for r in range(rows):
        fm = yr[0] + (yr[1] - yr[0]) * (r + 0.5) / rows
        ya = my(yr[0] + (yr[1] - yr[0]) * (r + 1) / rows)
        yb = my(yr[0] + (yr[1] - yr[0]) * r / rows)
        for c in range(cols):
            tm = xr[0] + (xr[1] - xr[0]) * (c + 0.5) / cols
            base = math.exp(-fm / 520.0)
            band1 = 0.34 * math.exp(-((fm - 430.0) / 230.0) ** 2)
            band2 = 0.17 * math.exp(-((fm - 1250.0) / 260.0) ** 2)
            v = 0.30 + 0.62 * base + band1 + band2
            v *= 0.88 + 0.12 * math.sin(tm * 0.9 + fm * 0.02)
            v = max(0.0, min(1.0, v))
            col = ("#b03a2e" if v > 0.82 else "#cf5b25" if v > 0.66
                   else "#e08a1e" if v > 0.50 else "#d9b81e" if v > 0.38
                   else "#e8dd6b")
            xa, xb = mx(xr[0] + (xr[1] - xr[0]) * c / cols), \
                     mx(xr[0] + (xr[1] - xr[0]) * (c + 1) / cols)
            o.append(_rect(xa, ya, xb - xa + 0.4, yb - ya + 0.4,
                           fill=col, sw=0))

    # frame, grid lines, ticks and axis titles
    o.append(_rect(x0, y0, pw, ph, fill="none", sw=1.2))
    for v in (500, 1000, 1500, 2000):
        yy = my(v)
        o.append(_line(x0, yy, x0 + pw, yy, sw=0.5, color="#ffffff"))
        o.append(_line(x0 - 3, yy, x0, yy, sw=0.8))
        o.append(T(x0 - 6, yy + 2.3, str(v), 6.4, anchor="end", color=GREY))
    o.append(_line(x0 - 3, y0 + ph, x0, y0 + ph, sw=0.8))
    o.append(T(x0 - 6, y0 + ph + 2.3, "0", 6.4, anchor="end", color=GREY))
    for v in range(5, 41, 5):
        xx = mx(v)
        o.append(_line(xx, y0 + ph, xx, y0 + ph + 3, sw=0.8))
        o.append(T(xx, y0 + ph + 11, str(v), 6.4, color=GREY))
    o.append(T(x0 + pw / 2.0, y0 + ph + 23, "Time", 7.4, color=INK))
    o.append(T(x0 - 50, y0 - 8, "Frequency", 7.4, color=INK, anchor="start"))

    # dominant frequency bands
    for freq, lab in ((600, "Dominant band 0-600 Hz"),
                      (1250, "Band ~1.2 kHz")):
        yy = my(freq)
        o.append(_line(x0, yy, x0 + pw, yy, sw=1.0,
                       color="#ffffff", dash="6 4"))
        wlab = 7.0 * 0.56 * len(lab)
        o.append(_rect(x0 + 5, yy - 13, wlab + 10, 13,
                       fill="#ffffff", sw=0.8, stroke=INK))
        o.append(T(x0 + 10 + wlab / 2.0, yy - 3, lab, 7.0, color=INK))

    # amplitude colour scale
    sx = 628.0
    for i, cc in enumerate(("#b03a2e", "#cf5b25", "#e08a1e",
                            "#d9b81e", "#e8dd6b")):
        o.append(_rect(sx, 60 + i * 18, 12, 18, fill=cc, sw=0))
    o.append(T(sx + 6, 54, "High", 6.4, color=INK))
    o.append(T(sx + 6, 160, "Low", 6.4, color=INK))
    o.append(T(sx + 6, 172, "Amp.", 6.4, color=GREY))

    return _mk(3, o, "Spectrogram of an acoustic signal",
               "Phổ âm thanh của tín hiệu âm thanh",
               "Spectrogram of an acoustic signal",
               "Phổ âm thanh với trục thời gian, trục tần số, cường độ màu và các dải tần chiếm ưu thế.",
               "Acoustic spectrogram with time and frequency axes, colour-coded amplitude and marked dominant frequency bands.")


# ------------------------------------------------------------------- fig 9.4
@_reg
def fig_f04():
    o = [_defs()]
    o.append(T(340, 13, "Hidden Markov model with three states",
               9.0, color=INK, weight="600"))
    xs = (160.0, 340.0, 520.0)
    sy = 80.0

    # state-transition arcs above the state circles
    o.append(_path("M170,55 C250,18 430,18 510,55",
                   fill="none", sw=1.2, color=BLUE))
    o.append(_ar(500, 46, 510, 55, color=BLUE, sw=1.2))
    o.append(T(340, 26, "a13", 6.4, color=BLUE))

    for i, x in enumerate(xs, 1):
        o.append(_circle(x, sy, 25, fill="#eef3fb", sw=1.3))
        o.append(T(x, sy + 4, "S%d" % i, 10.0, color=INK))
        o.append(_path("M%s,%s C%s,%s %s,%s %s,%s"
                       % (x - 15, sy - 19, x - 32, sy - 56,
                          x + 32, sy - 56, x + 15, sy - 19),
                       fill="none", sw=1.1, color=BLUE))
        o.append(_ar(x + 14, sy - 22, x + 12, sy - 29,
                     color=BLUE, sw=1.1))
        o.append(T(x, 43, "a%d%d" % (i, i), 6.4, color=BLUE))

    for xa, xb, lab in ((184, 316, "a12"), (364, 496, "a23")):
        o.append(_path("M%d,72 C%d,50 %d,50 %d,72"
                       % (xa, xa + 46, xb - 46, xb),
                       fill="none", sw=1.2, color=BLUE))
        o.append(_ar(xb - 8, 65, xb, 72, color=BLUE, sw=1.2))
        o.append(T((xa + xb) / 2.0, 60, lab, 6.4, color=BLUE))
    for xa, xb, lab in ((316, 184, "a21"), (496, 364, "a32")):
        o.append(_path("M%d,90 C%d,112 %d,112 %d,90"
                       % (xa, xa - 46, xb + 46, xb),
                       fill="none", sw=1.2, color=BLUE))
        o.append(_ar(xb + 8, 97, xb, 90, color=BLUE, sw=1.2))
        o.append(T((xa + xb) / 2.0, 116, lab, 6.4, color=BLUE))

    o.append(_path("M510,100 C430,150 250,150 170,100",
                   fill="none", sw=1.2, color=BLUE))
    o.append(_ar(180, 106, 170, 100, color=BLUE, sw=1.2))
    o.append(T(340, 140, "a31", 6.4, color=BLUE))

    # emission arrows from each state to each observation symbol
    ems = [
        (160, 105, 172, 205, 172, "b11"),
        (330, 105, 190, 205, 190, "b21"),
        (510, 105, 208, 205, 208, "b31"),
        (170, 105, 322, 205, 322, "b12"),
        (340, 105, 340, 205, 340, "b22"),
        (510, 105, 358, 205, 358, "b32"),
        (175, 105, 502, 205, 502, "b13"),
        (350, 105, 520, 205, 520, "b23"),
        (520, 105, 538, 205, 538, "b33"),
    ]
    for x1, y1, x2, y2, lx, lab in ems:
        own = (lab[0] == lab[1])
        o.append(_ar(x1, y1, x2, y2, color=BLUE if own else GREY,
                     sw=1.3 if own else 0.9))
        o.append(T(lx, 196, lab, 6.0, color=INK))

    for i, x in enumerate(xs, 1):
        o.append(_rect(x - 30, 205, 60, 38, fill="#f4f4f0", sw=1.2))
        o.append(T(x, 229, "v%d" % i, 10.0, color=INK))

    o.append(T(340, 268, "λ = (A, B, π)", 7.4, color=INK))

    return _mk(4, o, "Hidden Markov model with three states",
               "Mô hình Markov ẩn với ba trạng thái",
               "Hidden Markov model with three states",
               "Mô hình Markov ẩn với ba trạng thái S1, S2, S3; mũi tên chuyển trạng thái và xác suất phát xạ tới các quan sát v1, v2, v3.",
               "Hidden Markov model with three states S1, S2, S3, transition arrows and emission arrows to observations v1, v2, v3.")
