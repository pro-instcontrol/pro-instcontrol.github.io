# -*- coding: utf-8 -*-
"""Vector figures 4.1-4.4 for PPIC chapter 4 (fuzzy fault detection).

The diagrams redraw the printed figures with simplified geometry but keep
the printed labels, percentages, axes and rule structure.
"""
import math

from ppicfig4_common import (BLUE, GREEN, GREY, INK, RED, W, H, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend, _line,
                             _path, _poly, _rect, _series, _tri_membership,
                             _mk, make_registry)

FIGS, _reg = make_registry()


@_reg
def fig_f01():
    """Figure 4.1 - maintenance approach tree with the printed percentages."""
    o = [_defs()]

    o.append(_rect(272, 14, 136, 26, "#eef3fb", sw=1.2))
    o.append(T(340, 31, "Maintenance programs", 8.6, color=INK,
               weight="600"))

    o.append(_ar(340, 40, 170, 76, color=BLUE, sw=1.5))
    o.append(_ar(340, 40, 500, 76, color=BLUE, sw=1.5))
    o.append(T(252, 61, ">55%", 8.0, color=RED, weight="600"))

    o.append(_rect(72, 78, 196, 40, "#fdeceb", sw=1.2))
    o.append(T(170, 95, "Reactive/corrective", 8.2, color=INK,
               weight="600"))
    o.append(T(170, 108, "(repair upon failure)", 7.6, color=INK))

    o.append(_rect(444, 78, 112, 28, "#eef3fb", sw=1.2))
    o.append(T(500, 96, "Preventive", 8.4, color=INK, weight="600"))

    o.append(_ar(500, 106, 465, 142, color=BLUE, sw=1.5))
    o.append(_ar(500, 106, 610, 142, color=BLUE, sw=1.5))
    o.append(T(473, 130, "31%", 7.8, color=GREEN, weight="600"))
    o.append(T(605, 130, "12%", 7.8, color=BLUE, weight="600"))

    o.append(_rect(392, 142, 146, 38, "#e7f2ec", sw=1.2))
    o.append(T(465, 159, "Scheduled", 8.2, color=INK, weight="600"))
    o.append(T(465, 172, "(time driven)", 7.6, color=INK))

    o.append(_rect(548, 142, 124, 38, "#eaf1f8", sw=1.2))
    o.append(T(610, 159, "Predictive", 8.2, color=INK, weight="600"))
    o.append(T(610, 172, "(condition driven)", 7.4, color=INK))

    o.append(_line(34, 196, 646, 196, sw=0.8, color="#dcdcdc"))
    o.append(T(340, 204, "USA maintenance program survey, 2000", 7.2,
               color=GREY))

    bars = [
        (212, "Reactive/corrective", 55, ">55%", RED, "#fdeceb"),
        (240, "Scheduled (time driven)", 31, "31%", GREEN, "#e7f2ec"),
        (268, "Predictive (condition driven)", 12, "12%", BLUE, "#eaf1f8"),
    ]
    for y, label, val, shown, col, fill in bars:
        o.append(T(196, y + 12, label, 7.6, color=INK, anchor="end"))
        o.append(_rect(210, y, 5.0 * val, 16, fill, sw=1.0))
        o.append(T(216 + 5.0 * val, y + 12, shown, 7.8, color=col,
                   anchor="start", weight="600"))

    return _mk(1, o, "Equipment maintenance approaches",
               "Các cách tiếp cận bảo trì thiết bị",
               "Equipment maintenance approaches",
               "Sơ đồ ba cách tiếp cận bảo trì thiết bị",
               "Diagram of three equipment maintenance approaches")


@_reg
def fig_f02():
    """Figure 4.2 - two-stage fuzzy logic diagnostic monitoring scheme."""
    o = [_defs()]

    for x, name in ((56, "System 1"), (280, "System 2"), (500, "System N")):
        o.append(_rect(x, 16, 120, 32, "#eef3fb", sw=1.2))
        o.append(T(x + 60, 29, name, 8.2, color=INK, weight="600"))
        o.append(T(x + 60, 41, "signals", 8.2, color=INK))
    o.append(T(430, 34, "...", 9.0, color=GREY))

    o.append(_ar(116, 48, 230, 86, color=BLUE, sw=1.5))
    o.append(_ar(340, 48, 340, 86, color=BLUE, sw=1.5))
    o.append(_ar(560, 48, 450, 86, color=BLUE, sw=1.5))

    o.append(_rect(170, 88, 340, 44, "#eaf1f8", sw=1.3))
    o.append(T(340, 106, "Fault detection and isolation (FDI) with", 8.0,
               color=INK, weight="600"))
    o.append(T(340, 120, "general-purpose signal processing modules", 8.0,
               color=INK))

    o.append(_rect(18, 96, 124, 38, "#e7f2ec", sw=1.2))
    o.append(T(80, 112, "Plant systems", 7.8, color=INK, weight="600"))
    o.append(T(80, 125, "database", 7.8, color=INK))
    o.append(_ar(142, 123, 170, 123, color=GREEN, sw=1.4))

    o.append(_ar(230, 132, 120, 143, color=BLUE, sw=1.4))
    o.append(_ar(340, 132, 340, 143, color=BLUE, sw=1.4))
    o.append(_ar(450, 132, 560, 143, color=BLUE, sw=1.4))

    for cx, name in ((120, "System 1 status"),
                     (340, "System 2 status"),
                     (560, "System N status")):
        o.append(_ellipse(cx, 158, 46, 15, fill="#fbfaf7", sw=1.2))
        o.append(T(cx, 161, name, 7.6, color=INK))
    o.append(T(230, 162, "...", 9.0, color=GREY))
    o.append(T(450, 162, "...", 9.0, color=GREY))

    o.append(_ar(120, 173, 220, 204, color=BLUE, sw=1.4))
    o.append(_ar(340, 173, 340, 204, color=BLUE, sw=1.4))
    o.append(_ar(560, 173, 460, 204, color=BLUE, sw=1.4))
    o.append(_line(18, 122, 10, 122, sw=1.3, color=GREEN))
    o.append(_line(10, 122, 10, 225, sw=1.3, color=GREEN))
    o.append(_ar(10, 225, 170, 225, color=GREEN, sw=1.4))

    o.append(_rect(170, 204, 340, 44, "#e7f2ec", sw=1.3))
    o.append(T(340, 222, "System-specific signal processing", 8.0,
               color=INK, weight="600"))
    o.append(T(340, 236, "techniques for anomaly characterization", 8.0,
               color=INK))

    o.append(_ar(340, 248, 340, 263, color=BLUE, sw=1.4))
    o.append(_ellipse(340, 280, 74, 17, fill="#fbfaf7", sw=1.2))
    o.append(T(340, 283, "Overall system health", 8.0, color=INK))

    return _mk(2, o, "Overall scheme of fuzzy logic diagnostic monitoring",
               "Sơ đồ tổng thể giám sát chẩn đoán bằng logic mờ",
               "Overall scheme of fuzzy logic diagnostic monitoring",
               "Sơ đồ tổng thể giám sát chẩn đoán logic mờ",
               "Flow diagram of the overall fuzzy logic diagnostic monitoring scheme")


@_reg
def fig_f03():
    """Figure 4.3 - four temperature signals with increasing noise."""
    o = []
    ctrl = [(0, 705), (50, 710), (80, 760), (100, 750), (120, 775),
            (160, 775), (200, 805), (220, 805), (240, 825), (290, 825),
            (310, 875), (350, 875)]
    panels = [
        (62, 16, "Uniform noise", "(a) Little change in noise", 0.8, 1.0, 1.0),
        (380, 16, "Slight noise", "(b) Slight increase in noise",
         1.3, 0.4, 0.6),
        (62, 140, "Noisy", "(c) Significant increase in noise",
         2.8, 0.25, 0.75),
        (380, 140, "Very noisy", "(d) Considerable increase in noise",
         5.0, 0.15, 0.85),
    ]

    for x0, y0, leg, sub, amp, f0, f1 in panels:
        w, h = 250, 76
        fr, mx, my = _frame(x0, y0, w, h, (0, 350), (700, 900),
                            [(0, "0"), (100, "100"), (200, "200"),
                             (300, "300")],
                            [(700, "700"), (750, "750"), (800, "800"),
                             (850, "850"), (900, "900")],
                            "Time (min)", "°F")
        o.append(fr)
        pts = []
        for k in range(0, 351, 5):
            t = k
            base = ctrl[-1][1]
            for i in range(len(ctrl) - 1):
                xa, ya = ctrl[i]
                xb, yb = ctrl[i + 1]
                if xa <= t <= xb:
                    base = ya + (yb - ya) * (t - xa) / float(xb - xa)
                    break
            fac = f0 + (f1 - f0) * t / 350.0
            noise = amp * fac * (0.55 * math.sin(0.85 * t)
                                 + 0.30 * math.sin(2.7 * t + 1.1)
                                 + 0.15 * math.sin(6.3 * t + 2.2))
            pts.append((t, base + noise))
        o.append(_series(pts, mx, my, BLUE, dot=0.9))
        o.append(_line(x0 + 12, y0 + 14, x0 + 30, y0 + 14, sw=1.6,
                       color=BLUE))
        o.append(T(x0 + 34, y0 + 16, leg, 6.8, color=BLUE, anchor="start"))
        o.append(T(x0 + w / 2.0, y0 + h + 34, sub, 7.4, color=INK))

    o.append(T(340, 274,
               "Upper plenum, Experimental Breeder Reactor II; "
               "startup from 0% to 100% power", 7.0, color=GREY))

    return _mk(3, o, "Four temperature sensors with varying amounts of signal noise",
               "Bốn cảm biến nhiệt độ với các mức nhiễu tín hiệu khác nhau",
               "Four temperature sensors with varying amounts of signal noise",
               "Bốn tín hiệu nhiệt độ với mức nhiễu tăng dần khi công suất lò tăng",
               "Four temperature signals with noise increasing as reactor power rises")


@_reg
def fig_f04():
    """Figure 4.4 - fuzzy noise detector output for the third signal."""
    o = [_defs()]

    o.append(T(152, 15, "RMS = 1.69", 8.6, color=RED, weight="600"))
    o.append(T(337, 15, "ZCR = 5.22", 8.6, color=RED, weight="600"))
    o.append(T(532, 15, "Sensor status", 8.6, color=BLUE, weight="600"))
    o.append(T(152, 30, "zero   low   ordinary   elevated", 6.6, color=GREY))
    o.append(T(337, 30, "infrequent   regular   frequent", 6.6, color=GREY))
    o.append(T(30, 30, "Rule", 7.2, color=GREY))

    peaks = [70, 92, 38, 52, 104]
    zcr_high = [True, True, False, False, True]
    marker_rms = 72 + 1.69 / 4.0 * 160
    marker_zcr = 250 + 5.22 / 6.0 * 174

    for i in range(5):
        top = 40 + 29 * i
        o.append(T(30, top + 15, str(i + 1), 7.8, color=INK))

        o.append(_rect(72, top, 160, 22, "#ffffff", sw=0.9))
        pk = 72 + peaks[i]
        o.append(_poly([(80, top + 19), (pk, top + 3), (224, top + 19)],
                       fill="#d9c4e8", sw=1.1, color="#7d4f9c"))
        o.append(_line(marker_rms, top + 2, marker_rms, top + 20,
                       sw=1.0, color=RED, dash="3 2"))

        o.append(_rect(250, top, 174, 22, "#ffffff", sw=0.9))
        if zcr_high[i]:
            o.append(_poly([(258, top + 19), (282, top + 3),
                            (412, top + 3), (416, top + 19)],
                           fill="#a9d9ba", sw=1.1, color=GREEN))
        else:
            o.append(_poly([(258, top + 19), (290, top + 3),
                            (322, top + 19)],
                           fill="#a9d9ba", sw=1.1, color=GREEN))
        o.append(_line(marker_zcr, top + 2, marker_zcr, top + 20,
                       sw=1.0, color=RED, dash="3 2"))

        o.append(_rect(444, top, 166, 22, "#ffffff", sw=0.9))
        o.append(_poly([(462, top + 19), (527, top + 3), (592, top + 19)],
                       fill="#bcd8ed", sw=1.1, color=BLUE))
        o.append(_line(536, top + 2, 536, top + 20, sw=1.0, color=RED,
                       dash="3 2"))

    o.append(T(340, 198, "Defuzzification (centroid)", 7.6, color=GREY,
               weight="600"))
    o.append(_poly([(452, 274), (536, 214), (620, 274)],
                   fill="#a9cbe6", sw=1.3, color=BLUE))
    o.append(_line(536, 214, 536, 274, sw=1.2, color=RED, dash="3 2"))
    o.append(T(452, 286, "0", 6.8, color=GREY))
    o.append(T(620, 286, "1", 6.8, color=GREY))
    o.append(T(300, 238, "Sensor status = 0.557", 9.0, color=RED,
               anchor="end", weight="600"))
    o.append(_ar(310, 235, 444, 235, color=RED, sw=1.4))
    o.append(T(536, 301, "Third signal: noisy", 8.2, color=BLUE,
               weight="600"))

    return _mk(4, o, "Application of fuzzy noise detector to the third temperature signal",
               "Áp dụng bộ phát hiện nhiễu mờ cho tín hiệu nhiệt độ thứ ba",
               "Application of fuzzy noise detector to the third temperature signal",
               "Kết quả giải mờ cho tín hiệu nhiệt độ thứ ba: RMS = 1.69, ZCR = 5.22, trạng thái = 0.557",
               "Defuzzification result for the third temperature signal: RMS = 1.69, ZCR = 5.22, sensor status = 0.557")
