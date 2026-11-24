# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 13 "How Good Is the Valve I Purchased?": simplified vector redrawings
of source Figures 13-1 (closed-loop differentiation test) and 13-2 (static
open-loop step response). Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _circle, _defs, _f,
                  _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


def _steps(segments):
    """[(t0, t1, value), ...] -> polyline points with vertical step jumps."""
    pts = []
    for i, (t0, t1, v) in enumerate(segments):
        pts.append((t0, v))
        pts.append((t1, v))
        if i + 1 < len(segments):
            pts.append((t1, segments[i + 1][2]))
    return pts


@_reg
def fig_f131():
    """Figure 13-1 - closed-loop differentiation, variability vs loop time constant."""
    w, h = 680, 420
    L, T, R, B = 74, 52, 636, 348
    PW, PH = R - L, B - T
    o = [_defs()]
    o.append(_txt(340, 18, esc("Closed-loop differentiation: variability vs loop speed"),
                  11.0, color=INK, weight="600"))
    o.append(_txt(340, 32, esc("Simplified redrawing of Baumann Fig. 13-1; source: Emerson Process Control"),
                  7.4, color=GREY))

    def px(t):
        return L + (math.log10(t) + 1.0) / 3.0 * PW

    def py(v):
        return B - v / 5.0 * PH

    # graticule
    for v in range(6):
        y = py(v)
        o.append(_line(L, y, R, y, sw=0.8, dash="2 3" if v else "0",
                       color="#b9bec4" if v else INK))
        o.append(_txt(L - 8, y + 2.6, str(v), 7.2, anchor="end", color=GREY))
    for decade in (0.1, 1, 10, 100):
        x = px(decade)
        o.append(_line(x, T, x, B, sw=0.8, dash="2 3", color="#b9bec4"))
        o.append(_txt(x, B + 13, esc("%g" % decade), 7.6, color=GREY))
    for base in (0.1, 1, 10):
        for k in range(2, 10):
            t = base * k
            if t <= 100:
                o.append(_line(px(t), B - 4, px(t), B, sw=0.6, color="#b9bec4"))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.1))

    # top axis: controller gain inversely related to time constant
    o.append(_txt(340, 45, esc("CONTROLLER GAIN, Kc"), 7.6, color=GREY, weight="600"))
    for t, lab in ((1, "1"), (10, "0.1")):
        x = px(t)
        o.append(_line(x, T - 9, x, T, sw=1.0, color=INK))
        o.append(_txt(x, T - 12, lab, 7.4, color=INK, weight="600"))

    # manual line and its callout
    o.append(_line(L, py(4.45), R, py(4.45), sw=1.2, dash="5 4", color=GREY))
    o.append(_txt(L + 18, py(4.45) - 14, esc("MANUAL"), 7.6, color=GREY, weight="600"))
    o.append(_line(L + 88, py(4.45) - 12, L + 112, py(4.45) - 3,
                   sw=0.9, color=GREY))
    o.append(_arrow(L + 112, py(4.45) - 3, px(0.28), py(4.45) + 1,
                    sw=0.9, color=GREY))

    # the "ideal" rising reference curve
    ideal = [(0.1, 0.85), (0.3, 1.15), (1, 1.40), (3, 1.65),
             (10, 1.95), (30, 2.15), (100, 2.35)]
    o.append(_poly([(px(t), py(v)) for t, v in ideal], sw=1.4, color=GREY))

    # three valve curves, with the marker shapes used in the source
    cA = [(0.1, 2.42), (0.3, 2.33), (1, 2.25), (3, 2.20),
          (10, 2.24), (30, 2.35), (100, 2.42)]
    cB = [(0.1, 1.80), (0.3, 1.90), (1, 2.02), (3, 2.18),
          (10, 2.31), (30, 2.40), (100, 2.43)]
    cC = [(0.1, 1.44), (0.3, 1.53), (1, 1.66), (3, 1.83),
          (10, 2.00), (30, 2.14), (100, 2.30)]
    o.append(_poly([(px(t), py(v)) for t, v in cA], sw=1.7, color=INK))
    o.append(_poly([(px(t), py(v)) for t, v in cB], sw=1.7, color=BLUE))
    o.append(_poly([(px(t), py(v)) for t, v in cC], sw=1.7, color=GREEN))
    for t, v in cA:
        x, y = px(t), py(v)
        o.append(_line(x - 3, y - 3, x + 3, y + 3, sw=1.1, color=INK))
        o.append(_line(x - 3, y + 3, x + 3, y - 3, sw=1.1, color=INK))
    for t, v in cB:
        o.append(_circle(px(t), py(v), 3.2, fill="#ffffff", sw=1.1, color=BLUE))
    for t, v in cC:
        x, y = px(t), py(v)
        o.append(_poly([(x, y - 3.4), (x + 3.4, y + 2.6), (x - 3.4, y + 2.6)],
                       sw=1.1, color=GREEN, close=True))

    for lab, t, v, col in (("A", 0.12, 2.45, INK), ("B", 0.12, 1.82, BLUE),
                           ("C", 0.12, 1.46, GREEN)):
        o.append(_txt(px(t) - 12, py(v) + 2.6, lab, 8.2, color=col, weight="600"))
        o.append(_arrow(px(t) - 8, py(v) + 1, px(t) + 2, py(v), sw=0.8, color=col))

    # minimum variability callout
    o.append(_txt(px(16), py(1.42), esc("MINIMUM"), 7.2, color=GREY, weight="600"))
    o.append(_txt(px(16), py(1.22), esc("VARIABILITY"), 7.2, color=GREY, weight="600"))
    o.append(_arrow(px(16), py(1.55), px(12), py(2.08), sw=0.9, color=GREY))

    # tuning direction arrows
    o.append(_txt(L + 12, B - 10, esc("FASTER TUNING"), 7.4, color=GREY, weight="600"))
    o.append(_arrow(L + 150, B - 12, L + 22, B - 12, sw=1.0, color=INK))
    o.append(_arrow(L + 150, B - 12, R - 94, B - 12, sw=1.0, color=INK))
    o.append(_txt(R - 12, B - 10, esc("SLOWER TUNING"), 7.4, color=GREY,
                  anchor="end", weight="600"))

    # rotated y title and x title
    o.append('<text x="%s" y="%s" text-anchor="middle" '
             'style="font:7.8px Inter,Helvetica,sans-serif;fill:%s;font-weight:600" '
             'transform="rotate(-90,%s,%s)">%s</text>'
             % (_f(22), _f((T + B) / 2.0), INK, _f(22), _f((T + B) / 2.0),
                esc("VARIABILITY 2σ/μ (%)")))
    o.append(_txt(R, B + 31, esc("CLOSED-LOOP TIME CONSTANT, τ (SECONDS)"),
                  8.0, anchor="end", color=INK, weight="600"))

    s = svg(w, h, "".join(o), esc("Closed-loop valve variability chart"))
    return _fig(s,
                "Hình 13.1 · Bản vẽ lại đơn giản hóa kết quả thử phân biệt vòng kín cho ba loại van: trục hoành là hằng số thời gian vòng kín τ (giây, thang log 0,1–100), trục tung là độ biến thiên 2σ/μ (%). Đường A (dấu ×) gần như phẳng quanh 2,2–2,4%; đường B (vòng tròn) tăng từ khoảng 1,8 lên 2,4%; đường C (tam giác) tăng từ khoảng 1,4 lên 2,3% và tiệm cận đường “lý tưởng” dốc lên từ 0,85%. Đường ngang đứt nét ở 4,45% là chế độ MANUAL; mũi tên “MINIMUM VARIABILITY” chỉ mức biến thiên nhỏ nhất. Trục trên cho thấy hệ số khuếch đại bộ điều khiển Kc giảm từ 1 xuống 0,1 khi τ tăng; mũi tên dưới chỉ chiều chỉnh nhanh hơn/chậm hơn. Nguồn: Emerson Process Control. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 13.1 · Simplified redrawing of closed-loop differentiation results for three valve types: x is closed-loop time constant τ (seconds, log 0.1–100), y is variability 2σ/μ (%). Curve A (crosses) stays near 2.2–2.4%, curve B (circles) rises from about 1.8 to 2.4%, and curve C (triangles) rises from about 1.4 to 2.3%, tracking the rising “ideal” line. The dashed line at 4.45% marks MANUAL operation; the “MINIMUM VARIABILITY” arrow marks the lowest variability. The top axis shows controller gain Kc falling from 1 to 0.1 as τ increases; the lower arrows indicate faster/slower tuning. Source: Emerson Process Control. This is a simplified vector redrawing.",
                "Đồ thị độ biến thiên vòng kín theo hằng số thời gian: van A gần phẳng, van B và C tăng dần, C tiệm cận đường lý tưởng; có đường MANUAL và mũi tên độ biến thiên nhỏ nhất.",
                "Semi-log chart of valve variability versus closed-loop time constant with curves A, B and C, an ideal reference line, a manual-mode line and tuning-direction arrows")


@_reg
def fig_f132():
    """Figure 13-2 - static open-loop step response of a rotary valve."""
    w, h = 680, 410
    L, T, R, B = 62, 46, 620, 330
    PW, PH = R - L, B - T
    o = [_defs()]
    o.append(_txt(340, 16, esc("Static (open-loop) step response of a rotary valve with positioner"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 30, esc("Simplified redrawing of Baumann Fig. 13-2; source: Emerson Process Control"),
                  7.4, color=GREY))

    def px(t):
        return L + t / 450.0 * PW

    def py(v):
        """v is on the left signal/travel scale (45-75); right flow scale is v-5."""
        return B - (v - 45.0) / 30.0 * PH

    # graticule
    for v in range(45, 76, 5):
        y = py(v)
        o.append(_line(L, y, R, y, sw=0.8, dash="2 3", color="#b9bec4"))
        o.append(_txt(L - 7, y + 2.6, str(v), 7.0, anchor="end", color=GREY))
        o.append(_txt(R + 7, y + 2.6, str(v - 5), 7.0, color=GREY))
    for t in range(0, 451, 50):
        x = px(t)
        o.append(_line(x, T, x, B, sw=0.7, dash="2 3", color="#c9cdd2"))
        o.append(_txt(x, B + 13, str(t), 7.0, color=GREY))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.1))

    # step-size bands along the bottom of the plot
    bands = ((0, 100, "0.5% STEPS"), (100, 165, "1% STEPS"),
             (165, 230, "2% STEPS"), (230, 300, "5% STEPS"),
             (300, 420, "10% STEPS"))
    for t0, t1, lab in bands:
        o.append(_txt((px(t0) + px(t1)) / 2.0, B - 12, lab, 6.8,
                      color=GREY, weight="600"))

    # I/P input signal: dash-dot stepped trace
    ip = [(0, 22, 60.2), (22, 60, 60.0), (60, 110, 59.6),
          (110, 150, 59.9), (150, 175, 59.1), (175, 205, 58.8),
          (205, 230, 59.4), (230, 255, 58.7), (255, 270, 59.8),
          (270, 300, 58.6), (300, 320, 54.6), (320, 350, 55.3),
          (350, 390, 49.4), (390, 410, 48.5), (410, 450, 54.0)]
    o.append(_poly([(px(t), py(v)) for t, v in _steps(ip)],
                   sw=1.4, dash="6 3 1 3", color=GREY))

    # actuator travel: solid stepped trace (left scale)
    trav = [(0, 20, 63.2), (20, 60, 62.9), (60, 110, 62.5),
            (110, 150, 63.0), (150, 175, 61.6), (175, 200, 62.3),
            (200, 230, 60.3), (230, 250, 62.2), (250, 265, 66.3),
            (265, 300, 60.9), (300, 320, 57.3), (320, 350, 62.4),
            (350, 365, 60.1), (365, 400, 53.3), (400, 450, 62.6)]
    o.append(_poly([(px(t), py(v)) for t, v in _steps(trav)],
                   sw=1.7, color=BLUE))

    # flow rate: solid trace (right scale = left scale minus 5)
    flow = [(0, 20, 65.0), (20, 60, 64.9), (60, 110, 64.8),
            (110, 150, 65.0), (150, 175, 65.6), (175, 200, 64.3),
            (200, 230, 64.4), (230, 250, 66.3), (250, 265, 66.4),
            (265, 300, 64.2), (300, 320, 64.3), (320, 350, 68.1),
            (350, 365, 64.0), (365, 400, 60.2), (400, 450, 65.2)]
    o.append(_poly([(px(t), py(v)) for t, v in _steps(flow)],
                   sw=1.7, color=INK))

    # labels with leader arrows
    o.append(_txt(px(130), py(70.5), esc("FLOW-RATE"), 7.6,
                  color=INK, weight="600"))
    o.append(_arrow(px(145), py(70.0), px(168), py(65.5), sw=0.9, color=INK))
    o.append(_txt(px(70), py(66.8), esc("ACTUATOR-TRAVEL"), 7.6,
                  color=BLUE, weight="600"))
    o.append(_arrow(px(105), py(66.4), px(115), py(62.4), sw=0.9, color=BLUE))
    o.append(_txt(px(175), py(50.5), esc("I/P INPUT SIGNAL"), 7.6,
                  color=GREY, weight="600"))
    o.append(_arrow(px(190), py(51.5), px(197), py(58.7), sw=0.9, color=GREY))

    o.append(_txt(L + 2, T - 9, esc("(%) SIGNAL-TRAVEL"), 7.8,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(R - 2, T - 9, esc("(%) FLOW"), 7.8,
                  anchor="end", color=INK, weight="600"))
    o.append(_txt(R, B + 29, esc("TIME (SECONDS)"), 8.0,
                  anchor="end", color=INK, weight="600"))

    s = svg(w, h, "".join(o), esc("Static open-loop valve step-response chart"))
    return _fig(s,
                "Hình 13.2 · Bản vẽ lại đơn giản hóa phép thử tĩnh (vòng hở) của một van quay có bộ định vị: trục hoành là thời gian (giây, 0–450), trục trái là phần trăm tín hiệu/hành trình (45–75%), trục phải là phần trăm lưu lượng (40–70%). Đường đứt chấm là tín hiệu vào I/P, với các bước 0,5%, 1%, 2%, 5% và 10% (ghi ở dưới); đường xanh là hành trình bộ truyền động còn đường đen là lưu lượng. Ở các bước nhỏ, hành trình thay đổi nhưng lưu lượng hầu như không đổi — bằng chứng có khe hở/chuyển động mất (lost motion) giữa thân van và phần tử đóng. Ở bước 10%, cả ba đường đều thay đổi rõ. Nguồn: Emerson Process Control. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 13.2 · Simplified redrawing of the static open-loop step test of a rotary valve with positioner: x is time (seconds, 0–450), left axis is signal/travel (45–75%), right axis is flow (40–70%). The dash-dot trace is the I/P input signal with 0.5%, 1%, 2%, 5% and 10% steps (labelled along the bottom); the blue trace is actuator travel and the black trace is flow rate. At the small steps the travel changes but flow scarcely does — evidence of lost motion between the stem and the closure member. At the 10% steps all three traces change clearly. Source: Emerson Process Control. This is a simplified vector redrawing.",
                "Đồ thị đáp ứng bước vòng hở: tín hiệu I/P dạng bước, hành trình bộ truyền động phản ứng sớm nhưng lưu lượng chỉ đổi rõ ở bước lớn, cho thấy chuyển động mất giữa thân van và phần tử đóng.",
                "Time-series chart of I/P input steps, actuator travel and flow rate, with the flow lagging the travel at small step sizes")
