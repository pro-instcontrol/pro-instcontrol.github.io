# -*- coding: utf-8 -*-
"""Vector figures 10.4 and 10.5 for PPIC chapter 10.

Both charts are redrawn from the printed pages: the top-event probability
chart (p.247) and the reliability chart (p.248).  All labels are emitted
through ``T()`` so the SVG stays XML-safe and bilingual.
"""
from ppicfig10_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar,
                              _circle, _defs, _ellipse, _fig, _frame, _legend,
                              _line, _path, _poly, _rect, _mk, _series,
                              make_registry)

FIGS, _reg = make_registry()


def _chart_legend(o, x, y, items, w=152, lh=15, size=7.0):
    """Two-entry legend with a valid dash pattern on the first sample."""
    h = 12 + len(items) * lh
    o.append(_rect(x, y, w, h, fill="#ffffff", sw=0.9))
    for i, (col, lab, dash) in enumerate(items):
        yy = y + 15 + i * lh
        o.append(_line(x + 6, yy - 4, x + 23, yy - 4,
                       sw=2.0, color=col, dash=dash))
        o.append(T(x + 28, yy, lab, size, anchor="start"))


@_reg
def fig_f04():
    """Top-event occurrence probability over 0-40 hours."""
    o = [T(W / 2.0, 16, "Probability of occurrence of a Top Event",
           9.0, weight="bold")]
    top = 2.8e-6
    step = 1.4e-7
    yt = [(step * i, "%.2E" % (step * i)) for i in range(21)]
    fr, mx, my = _frame(70, 28, 560, 206, (0, 40), (0, top),
                        [(v, str(v)) for v in (0, 10, 20, 30, 40)], yt,
                        "t (hours)", "")
    o.append(fr)
    o.append(T(70, 20, "TEP(t)", 7.4, color=INK, anchor="start"))

    low = [(0, 0.0), (10, 0.0), (20, 0.0),
           (30, 3.5e-8), (40, 2.7e-6)]
    high = [(0, 0.0), (10, 0.0), (20, 0.0),
            (30, 1.78955e-8), (40, 1.1427e-7)]
    o.append(_series(low, mx, my, BLUE, dot=2.2, dash="5 3"))
    o.append(_series(high, mx, my, INK, dot=2.2))
    _chart_legend(o, 88, 42,
                  [(BLUE, "Low Level Failure", "5 3"),
                   (INK, "High Level Failure", "")])

    return _mk(4, o,
               "Probability of occurrence of a Top Event",
               "Xác suất xuất hiện của sự kiện đỉnh",
               "Probability of occurrence of a Top Event",
               "Biểu đồ xác suất xuất hiện sự kiện đỉnh theo thời gian; "
               "đường đứt nét tăng mạnh sau 30 giờ.",
               "Chart of top-event probability versus time; the dashed low-level "
               "series rises steeply after 30 hours.",
               h=H)


@_reg
def fig_f05():
    """Reliability of the digital water level control system."""
    o = [T(W / 2.0, 16,
           "Reliability of the digital water level control system",
           9.0, weight="bold")]
    yt = [(0.999996 + 4e-7 * i, "%.7f" % (0.999996 + 4e-7 * i))
          for i in range(11)]
    fr, mx, my = _frame(80, 28, 540, 206, (0, 40), (0.999996, 1.0),
                        [(v, str(v)) for v in (0, 10, 20, 30, 40)], yt,
                        "t (hours)", "")
    o.append(fr)
    o.append(T(80, 20, "R(t)", 7.4, color=INK, anchor="start"))

    pts = [(0, 1.0), (10, 1.0), (20, 1.0),
           (30, 0.99999995), (40, 0.99999718)]
    o.append(_series(pts, mx, my, INK, dot=0))
    for xv, yv in pts:
        px, py = mx(xv), my(yv)
        o.append(_poly([(px, py - 3), (px + 3, py),
                        (px, py + 3), (px - 3, py)],
                       fill=INK, sw=0, color=INK, close=True))

    return _mk(5, o,
               "Reliability of the digital water level control system",
               "Độ tin cậy của hệ thống điều khiển mực nước số",
               "Reliability of the digital water level control system",
               "Biểu đồ độ tin cậy; giá trị giữ gần 1 đến 30 giờ rồi giảm mạnh ở 40 giờ.",
               "Reliability chart; values stay near 1 until 30 hours and then "
               "drop sharply at 40 hours.",
               h=H)
