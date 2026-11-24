# -*- coding: utf-8 -*-
"""Vector figures for Book 7 — Baumann, *Control Valve Primer*, 5th ed.

Chapter 5 "Valve Sizing Made Easy": simplified vector re-drawings of
source Figures 5-1 and 5-2.  Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _box, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f51():
    """Figure 5-1 — pressure drop vs specific valve flow capacity, water at 15 ft/s."""
    w, h = 680, 410
    o = [_defs()]
    o.append(_txt(340, 20, esc("Quan he giam ap van va nang luong luong dac thu"),
                  10.4, color=INK, weight="600"))
    o.append(_txt(340, 38,
                  esc("Nuoc o 15 ft/s trong ong · d = duong kinh van (inch) "
                      "· ap dung cho khi/hoi o 150 ft/s"),
                  7.6, color=GREY))

    L, T, R, B = 72, 64, 620, 318
    PW, PH = R - L, B - T

    def px(v):
        return L + v / 40.0 * PW

    def py(v):
        return B - v / 60.0 * PH

    # grid and axes
    for gx in range(0, 41, 10):
        o.append(_line(px(gx), T, px(gx), B, sw=0.8, color="#e6e6e6"))
        o.append(_txt(px(gx), B + 13, str(gx), 6.8, color=GREY))
    for gy in range(0, 61, 10):
        o.append(_line(L, py(gy), R, py(gy), sw=0.8, color="#e6e6e6"))
        o.append(_txt(L - 6, py(gy) + 2.4, str(gy), 6.8, anchor="end", color=GREY))
    o.append(_line(L, B, R, B, sw=1.3, color=INK))
    o.append(_line(L, T, L, B, sw=1.3, color=INK))
    o.append(_txt(L, T - 9, esc("ΔP (psi)"), 8.4, anchor="start",
                  color=INK, weight="600"))
    o.append(_txt((L + R) / 2, B + 28, esc("Nang luong luong dac thu Cv/d²"),
                  8.4, color=INK, weight="600"))

    # Q = 2.45 * V * d^2 (gpm), Cv = Q / sqrt(dP)  ->  dP = (2.45 V / (Cv/d^2))^2
    # with V = 15 ft/s:  dP = 1350 / (Cv/d^2)^2  (psi)
    xs = [4.75 + (40.0 - 4.75) * i / 120.0 for i in range(121)]
    curve = [(px(x), py(1350.0 / (x * x))) for x in xs]

    # shade the region above the limit curve (higher drop than a line-size valve)
    d = "M%.2f %.2f " % (curve[0][0], T)
    d += " ".join("L%.2f %.2f" % (a, b) for a, b in curve)
    d += " L%.2f %.2f Z" % (curve[-1][0], T)
    o.append(_path(d, fill="#fdf0ee", sw=0, color="none"))

    o.append(_line(L, py(5), R, py(5), sw=1.0, dash="4 3", color=RED))
    o.append(_txt(R - 6, py(5) - 7, esc("5 psi - van bang ong"),
                  7.2, anchor="end", color=RED))
    o.append(_poly(curve, sw=2.2, color=BLUE))

    # reference point: Cv/d^2 ~ 17 gives about 5 psi at 15 ft/s
    rx, ry = px(17.0), py(1350.0 / (17.0 ** 2))
    o.append(_line(rx, ry, rx, B, sw=1.0, dash="3 3", color=RED))
    o.append(_line(L, ry, rx, ry, sw=1.0, dash="3 3", color=RED))
    o.append(_circle(rx, ry, 4, fill="#ffffff", sw=1.6, color=RED))
    o.append(_txt(rx + 8, ry - 12, esc("Cv/d²=17, ΔP~5 psi"),
                  7.6, anchor="start", color=RED, weight="600"))
    o.append(_txt(483, 303, esc("gioi han 15 ft/s (nuoc)"),
                  7.4, anchor="end", color=BLUE, weight="600"))

    o.append(_txt(40, 368, esc("duong xanh / blue: gioi han 15 ft/s"),
                  7.4, anchor="start", color=INK))
    o.append(_txt(258, 368, esc("diem do / red: Cv/d²=17, ΔP~5 psi"),
                  7.4, anchor="start", color=INK))
    o.append(_txt(478, 368, esc("vung nhat / shade: ΔP > 5 psi"),
                  7.4, anchor="start", color=INK))
    o.append(_txt(340, 392,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(du lieu tu Fig. 5-1)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Pressure drop versus specific valve flow capacity, water at 15 ft/s"))
    return _fig(s,
                "Hình 5.1 · Đồ thị đơn giản hóa quan hệ giữa độ giảm áp van ΔP và năng lực lưu "
                "lượng riêng Cv/d² cho nước ở vận tốc 15 ft/s trong ống; d là đường kính van "
                "(inch). Tại Cv/d² ≈ 17 thì ΔP ≈ 5 psi; ΔP lớn hơn đòi hỏi van nhỏ hơn ống, "
                "dùng reducer hoặc trim giảm. Đồ thị cũng áp dụng cho khí và hơi ở 150 ft/s. "
                "Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 5.1 · Simplified redrawing of the chart relating valve pressure drop ΔP "
                "to specific flow capacity Cv/d² for water at 15 ft/s pipe velocity; d is valve "
                "diameter (inches). At Cv/d² ≈ 17, ΔP ≈ 5 psi; a higher ΔP calls for a valve "
                "smaller than the pipe, with reducers or reduced trim. The chart also applies to "
                "gas or steam at 150 ft/s. This is a simplified vector redrawing.",
                "Đồ thị độ giảm áp van theo năng lực lưu lượng riêng, đường cong giảm với mốc 17 và 5 psi",
                "Chart of valve pressure drop versus specific flow capacity, falling curve with a 17 and 5 psi reference")


@_reg
def fig_f52():
    """Figure 5-2 — valve Reynolds number factor F_R versus valve Reynolds number Re_v."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_txt(340, 20, esc("He so Reynolds van F_R theo so Reynolds van Re_v"),
                  10.4, color=INK, weight="600"))
    o.append(_txt(340, 38,
                  esc("Bon duong cong theo kieu van va Cd = Cv/d² · "
                      "FR tien ve 1 khi Re_v > 10000"),
                  7.6, color=GREY))

    L, T, R, B = 76, 64, 628, 316
    PW, PH = R - L, B - T

    def px(lg):
        return L + (lg - 1.0) / 4.0 * PW

    def py(fr):
        return B - fr * PH

    def fr(lg, m):
        return 1.0 / (1.0 + 10 ** (-(lg - m) / 1.3))

    # grid and axes (log x, linear y)
    for lg, lab in ((1, "10"), (2, "100"), (3, "1k"), (4, "10k"), (5, "100k")):
        o.append(_line(px(lg), T, px(lg), B, sw=0.8, color="#e6e6e6"))
        o.append(_txt(px(lg), B + 13, lab, 6.8, color=GREY))
    for fv, lab in ((0.0, "0"), (0.2, "0,2"), (0.4, "0,4"), (0.6, "0,6"),
                    (0.8, "0,8"), (1.0, "1,0")):
        o.append(_line(L, py(fv), R, py(fv), sw=0.8, color="#e6e6e6"))
        o.append(_txt(L - 6, py(fv) + 2.4, lab, 6.8, anchor="end", color=GREY))
    o.append(_line(L, B, R, B, sw=1.3, color=INK))
    o.append(_line(L, T, L, B, sw=1.3, color=INK))
    o.append(_txt(L, T - 9, esc("He so Reynolds van F_R"), 8.4,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt((L + R) / 2, B + 34, esc("So Reynolds van Re_v (thang log)"),
                  8.4, color=INK, weight="600"))

    # above Re_v = 10,000 the viscosity correction can be ignored
    o.append(_line(px(4), T, px(4), B, sw=1.0, dash="4 3", color=GREY))
    o.append(_txt(px(4) - 6, T - 8, esc("Re_v=10k: FR ~ 1"),
                  7.2, anchor="end", color=GREY))

    curves = [(2.7, BLUE), (2.4, GREEN), (2.1, RED), (1.8, INK)]
    for m, color in curves:
        pts = [(px(1.0 + 4.0 * i / 120.0), py(fr(1.0 + 4.0 * i / 120.0, m)))
               for i in range(121)]
        o.append(_poly(pts, sw=2.0, color=color))

    for idx, (m, color) in enumerate(curves, start=1):
        o.append(_txt(px(2.5) + 6, py(fr(2.5, m)) - 3, str(idx),
                      7.6, anchor="start", color=color, weight="600"))

    leg = [
        (48, 372, BLUE, "1 · van cau / globe, Cd<10"),
        (48, 390, GREEN, "2 · van cau, cam lech / globe, eccentric, Cd 10-15"),
        (360, 372, RED, "3 · van canh / butterfly, Cd 15-25"),
        (360, 390, INK, "4 · van bi / ball, Cd>25 / small flow Cd<1"),
    ]
    for x, y, color, label in leg:
        o.append(_line(x, y - 3, x + 14, y - 3, sw=2.2, color=color))
        o.append(_txt(x + 20, y, esc(label), 7.4, anchor="start", color=INK))
    o.append(_txt(340, 412,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(F_R theo [7,8])"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Valve Reynolds number factor FR versus valve Reynolds number Re_v"))
    return _fig(s,
                "Hình 5.2 · Đồ thị đơn giản hóa hệ số Reynolds van F_R theo số Reynolds van "
                "Re_v (thang log) với bốn đường cong 1–4 tùy kiểu van và năng lực lưu lượng "
                "tương đối Cd = Cv/d²: 1 van cầu Cd<10; 2 van cầu và van cắm lệch Cd 10–15; "
                "3 van cánh bướm Cd 15–25; 4 van bi Cd>25 và van lưu lượng nhỏ Cd<1. F_R tiến "
                "về 1 khi Re_v lớn hơn 10.000, khi đó bỏ qua hoàn toàn hiệu chỉnh độ nhớt. "
                "Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 5.2 · Simplified redrawing of the graph of valve Reynolds number factor "
                "F_R versus valve Reynolds number Re_v (log scale), with curves 1–4 by valve "
                "style and relative flow capacity Cd = Cv/d²: 1 globe Cd<10; 2 globe and "
                "eccentric rotary plug Cd 10–15; 3 butterfly Cd 15–25; 4 ball Cd>25 and "
                "small-flow valves Cd<1. F_R approaches 1 above Re_v = 10,000, where the "
                "viscosity correction can be ignored. This is a simplified vector redrawing.",
                "Bốn đường cong F_R tăng dần theo Re_v và tiến về 1 ở mười nghìn, kèm chú thích bốn kiểu van",
                "Four rising F_R curves versus Re_v approaching 1 at ten thousand, with four valve-style legend entries")
