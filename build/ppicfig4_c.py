# -*- coding: utf-8 -*-
"""Vector figures 9-11 for PPIC chapter 4 (instrument calibration monitoring)."""
import math
from ppicfig4_common import (BLUE, GREEN, GREY, INK, RED, W, H, T, _ar, _b,
                             _circle, _fig, _frame, _legend, _line, _path,
                             _poly, _rect, _series, _tri_membership, _mk,
                             make_registry)

FIGS, _reg = make_registry()

ORANGE = "#d9792b"  # Signal 4 trace of the printed pressurizer plot


@_reg
def fig_f09():
    """Universe of discourse of the frequency-of-occurrence fuzzy input."""
    o = []
    fr, mx, my = _frame(105, 42, 500, 200, (0, 100), (0, 1),
                        [(0, "0"), (20, "20"), (40, "40"), (60, "60"),
                         (80, "80"), (100, "100")],
                        [(0, "0"), (1, "1")],
                        "Frequency (%)", "")
    o.append(fr)

    # Expected: dotted left shoulder.  Its right plateau runs beneath the
    # solid Frequent plateau, exactly as on the printed page.
    o.append(_poly([(mx(8), my(0)), (mx(20), my(1)), (mx(100), my(1))],
                   color=RED, dash="2 3"))
    # Frequent: solid right shoulder rising from 50 to 70 percent.
    o.append(_poly([(mx(50), my(0)), (mx(70), my(1)), (mx(100), my(1))],
                   color=BLUE))
    # Rare: dashed left triangle falling from 0 to 10 percent.
    o.append(_poly([(mx(0), my(1)), (mx(10), my(0))],
                   color=GREEN, dash="5 3"))

    o.append(T(mx(8), my(0.74), "Rare", 8.0, color=GREEN))
    o.append(T(mx(40), my(0.55), "Expected", 8.0, color=RED))
    o.append(T(mx(84), my(0.62), "Frequent", 8.0, color=BLUE))

    return _mk(9, o,
               "Universe of discourse for the frequency of occurrence (τ) fuzzy input variable",
               "Vũ trụ thảo luận cho biến đầu vào mờ tần suất xuất hiện (τ)",
               "Universe of discourse for the frequency of occurrence (τ) fuzzy input variable",
               "Ba hàm thuộc mờ chồng lấp Hiếm, Dự kiến và Thường xuyên trên trục tần suất từ 0 đến 100 phần trăm.",
               "Three overlapping membership functions Rare, Expected and Frequent on a frequency axis from 0 to 100 percent.")


@_reg
def fig_f10():
    """Universe of discourse of the status fuzzy output: C, P and I sets."""
    o = []
    fr, mx, my = _frame(110, 58, 480, 185, (0, 1), (0, 1),
                        [(0, "0"), (0.25, "0.25"), (0.5, "0.5"),
                         (0.75, "0.75"), (1, "1")],
                        [(0, "0"), (1, "1")],
                        "Status", "")
    o.append(fr)

    # C(consistent) = [0, 0, 0.5]
    o.append(_poly([(mx(0), my(1)), (mx(0.25), my(1)), (mx(0.5), my(0))],
                   color=GREEN, dash="5 3"))
    # P(partially consistent) = [0.25, 0.5, 0.75]
    o.append(_poly([(mx(0.25), my(0)), (mx(0.5), my(1)), (mx(0.75), my(0))],
                   color=RED, dash="2 3"))
    # I(inconsistent) = [0.5, 1, 1]
    o.append(_poly([(mx(0.5), my(0)), (mx(0.75), my(1)), (mx(1), my(1))],
                   color=BLUE))

    o.append(T(mx(0.1), my(0.68), "Consistent", 8.0, color=GREEN))
    o.append(T(mx(0.5), 32, "Partially", 7.6, color=RED))
    o.append(T(mx(0.5), 43, "consistent", 7.6, color=RED))
    o.append(T(mx(0.86), my(0.68), "Inconsistent", 8.0, color=BLUE))

    return _mk(10, o,
               "Universe of discourse for the status (s) fuzzy output variable",
               "Vũ trụ thảo luận cho biến đầu ra mờ trạng thái (s)",
               "Universe of discourse for the status (s) fuzzy output variable",
               "Ba hàm thuộc mờ Nhất quán, Nhất quán một phần và Không nhất quán trên trục trạng thái từ 0 đến 1.",
               "Three overlapping membership functions Consistent, Partially consistent and Inconsistent on a status axis from 0 to 1.")


@_reg
def fig_f11():
    """Four redundant pressurizer pressure traces with the spurious sensor."""
    o = []
    fr, mx, my = _frame(80, 30, 500, 220, (0, 250), (2234, 2250),
                        [(v, str(v)) for v in range(0, 251, 50)],
                        [(v, str(v)) for v in range(2234, 2251, 2)],
                        "Day", "psia")
    o.append(fr)

    def _trace(waypoints, amp, phase):
        pts = []
        for i in range(161):
            day = 250.0 * i / 160.0
            val = waypoints[-1][1]
            for (xa, ya), (xb, yb) in zip(waypoints, waypoints[1:]):
                if xa <= day <= xb:
                    f = (day - xa) / (xb - xa) if xb > xa else 0.0
                    val = ya + (yb - ya) * f
                    break
            val += amp * math.sin(day / 13.0 + phase)
            val += 0.35 * amp * math.sin(day / 4.7 + 2.0 * phase)
            pts.append((day, val))
        return pts

    traces = [
        (BLUE, "6 3 1 3", 0.14, 0.4,
         [(0, 2247.2), (30, 2248.0), (55, 2247.3), (85, 2247.4),
          (96, 2247.2), (100, 2243.6), (104, 2245.0), (112, 2246.7),
          (135, 2247.4), (170, 2247.3), (195, 2247.0), (200, 2246.6),
          (203, 2239.5), (207, 2241.2), (230, 2241.4), (250, 2241.0)]),
        (RED, "6 4", 0.11, 1.7,
         [(0, 2240.6), (30, 2240.9), (55, 2240.7), (90, 2240.8),
          (98, 2240.6), (101, 2238.9), (105, 2240.3), (120, 2240.9),
          (160, 2240.7), (185, 2240.4), (198, 2240.4), (202, 2238.8),
          (206, 2239.5), (230, 2239.5), (250, 2239.7)]),
        (GREY, "1 3", 0.09, 2.9,
         [(0, 2239.0), (30, 2238.8), (60, 2238.8), (90, 2238.9),
          (100, 2238.3), (110, 2238.9), (140, 2239.4), (170, 2239.5),
          (195, 2239.4), (202, 2238.2), (208, 2239.0), (230, 2239.3),
          (250, 2239.4)]),
        (ORANGE, "", 0.10, 4.1,
         [(0, 2239.5), (30, 2240.0), (60, 2239.9), (90, 2240.0),
          (98, 2239.8), (101, 2238.0), (105, 2239.2), (115, 2238.6),
          (140, 2238.5), (190, 2238.5), (200, 2238.4), (203, 2236.7),
          (208, 2237.8), (225, 2237.6), (240, 2237.9), (250, 2238.1)]),
    ]
    for col, dash, amp, phase, waypoints in traces:
        o.append(_series(_trace(waypoints, amp, phase), mx, my, col,
                         dot=0, dash=dash))

    legend = [(BLUE, "6 3 1 3", "Signal 1"), (RED, "6 4", "Signal 2"),
              (GREY, "1 3", "Signal 3"), (ORANGE, "", "Signal 4")]
    for i, (col, dash, lab) in enumerate(legend):
        lx = 175 if i < 2 else 405
        ly = 288 if i % 2 == 0 else 302
        o.append(_line(lx, ly - 2.5, lx + 18, ly - 2.5,
                       sw=1.7, color=col, dash=dash))
        o.append(T(lx + 23, ly, lab, 7.6, anchor="start"))

    return _mk(11, o,
               "Pressurizer pressure measurements from four redundant sensors",
               "Đo áp suất bình tạo áp từ bốn cảm biến dự phòng",
               "Pressurizer pressure measurements from four redundant sensors",
               "Áp suất đo được theo thời gian từ bốn cảm biến dự phòng; tín hiệu 1 lệch rõ khỏi ba tín hiệu còn lại trước khoảng ngày 200.",
               "Pressure traces from four redundant sensors; signal 1 is visibly offset from the other three until recalibration near day 200.")
