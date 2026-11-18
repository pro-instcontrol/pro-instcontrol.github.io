# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 17 — Sizing Pressure Relief Devices
(book ch. 7, Figures 7-1 … 7-9).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

The source charts are engineering nomograms.  They are redrawn as clean
qualitative vector charts with the same axes, ranges and curve families;
no new numeric data are invented.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _txt, svg)
from vshfig3 import _emit_legend

FIGS14 = {}


def _reg14(f):
    FIGS14[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
PANEL_F = "#d9d9d2"
HOT_F = "#b5533d"
COOL_F = "#9bbfd1"
XLEG = 402
X0, X1, Y0, Y1 = 56, 360, 54, 300


def _chart(xticks, yticks, xlab, ylab, logx=False, right=()):
    """Grid/axes plus linear-or-log x and linear y mapping functions."""
    e = []

    def X(v):
        if logx:
            lo, hi = math.log10(xticks[0][0]), math.log10(xticks[-1][0])
            return X0 + (math.log10(v) - lo) / (hi - lo) * (X1 - X0)
        lo, hi = xticks[0][0], xticks[-1][0]
        return X0 + (v - lo) / (hi - lo) * (X1 - X0)

    def Y(v):
        lo, hi = yticks[0][0], yticks[-1][0]
        return Y1 - (v - lo) / (hi - lo) * (Y1 - Y0)

    e.append(_line(X0, Y1, X1, Y1, 1.3, color=INK))
    e.append(_line(X0, Y1, X0, Y0, 1.3, color=INK))
    for v, lab in xticks:
        xx = X(v)
        e.append(_line(xx, Y0, xx, Y1, 0.6, color=GREY))
        e.append(_txt(xx, Y1 + 13, lab, 6.0))
    for v, lab in yticks:
        yy = Y(v)
        e.append(_line(X0, yy, X1, yy, 0.6, color=GREY))
        e.append(_txt(X0 - 6, yy, lab, 6.0, anchor="end"))
    e.append(_txt((X0 + X1) / 2, Y1 + 30, xlab, 7.0, color=INK))
    e.append(_txt(16, (Y0 + Y1) / 2, ylab, 7.0, color=INK))
    for yy, lab in right:
        e.append(_txt(X1 + 6, yy, lab, 5.8, anchor="start", color=GREY))
    return e, X, Y


def _curve(e, pts, color=BLUE, sw=1.8, dash=""):
    e.append(_poly(pts, "none", sw=sw, color=color, dash=dash, close=False))


def _fig7(num, ten, tvi, marks, extra=(), courtesy="", sub=""):
    o2 = list(extra)
    if sub:
        o2.append(_txt(200, 350, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(548, 366, courtesy, 6.0, anchor="end", color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 7-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 7-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _install_ops():
    e = []
    # vessel and nozzle
    e.append(_poly([(20, 300), (62, 256), (126, 234), (190, 236),
                    (254, 234), (318, 256), (360, 300)],
                   BODY_F, 1.4, INK, "", True))
    e.append(_poly([(158, 236), (158, 158), (182, 158), (182, 236)],
                   "#ffffff", 1.2, INK, "", True))
    e.append(_line(152, 158, 188, 158, 1.4, INK))
    e.append(_line(152, 150, 188, 150, 1.4, INK))
    # valve body, seat and bonnet
    e.append(_poly([(136, 150), (204, 150), (194, 106), (146, 106)],
                   PANEL_F, 1.4, INK, "", True))
    e.append(_line(150, 128, 190, 128, 1.4, INK))
    e.append(_poly([(138, 66), (202, 66), (202, 106), (138, 106)],
                   "#ffffff", 1.2, INK, "", True))
    e.append(_line(170, 66, 170, 128, 1.4, INK))
    sp = [(170, 72)]
    for i in range(12):
        sp.append((170 + (-8 if i % 2 else 8), 74 + i * 2.6))
    sp.append((170, 105))
    e.append(_poly(sp, "none", 1.1, INK, "", False))
    # outlet and rising discharge pipe
    e.append(_poly([(204, 126), (246, 126), (246, 138), (204, 138)],
                   "#ffffff", 1.2, INK, "", True))
    e.append(_line(246, 120, 246, 144, 1.4, INK))
    e.append(_line(252, 120, 252, 144, 1.4, INK))
    e.append(_poly([(252, 126), (312, 126), (330, 108), (338, 74),
                    (338, 52), (322, 52), (322, 100), (306, 114),
                    (252, 114)],
                   "#ffffff", 1.2, INK, "", True))
    e.append(_line(318, 52, 342, 52, 1.4, INK))
    e.append(_txt(336, 44, "T", 8.0, color=INK, weight="bold"))
    e.append(_txt(190, 320, "1", 10, color=INK, weight="bold"))
    return e


# ------------------------------------------------------------------- figures
@_reg14
def fig_vsh_7_1():
    return _fig7(
        1, "Typical pressure relief valve installation and flow-equation "
           "subscripts",
        "Lắp đặt van an toàn điển hình và ký hiệu chỉ số trong phương trình lưu lượng",
        [(("bình / nguồn áp (1)", "source vessel (1)"), (190, 272)),
         (("cổng vào bình (E)", "vessel nozzle (E)"), (170, 152)),
         (("vào van (N)", "valve inlet (N)"), (150, 124)),
         (("ra van (2)", "valve outlet (2)"), (232, 132)),
         (("đầu ống xả (3)", "discharge outlet (3)"), (330, 60)),
         (("nhiệt độ dòng (T)", "stream temperature (T)"), (312, 96))],
        extra=_install_ops(),
        sub="Các chỉ số được dùng cho điều kiện tại các vị trí đánh dấu / subscripts for conditions at the marked points")


@_reg14
def fig_vsh_7_2():
    xs = [1.00 - 0.05 * i for i in range(13)]
    xt = [(v, "%.2f" % v if v == 1.00 else "%.2f" % v) for v in xs]
    yt = [(0.25 + 0.05 * i, "%.2f" % (0.25 + 0.05 * i)) for i in range(16)]
    right = []
    for f, lab in [(0.25, "100"), (0.33, "150"), (0.41, "200"),
                   (0.49, "250"), (0.57, "300"), (0.65, "350"),
                   (0.73, "400"), (0.81, "450"), (0.89, "500"),
                   (1.00, "560")]:
        right.append((Y1 - (f - 0.25) / 0.75 * (Y1 - Y0), lab))
    e, X, Y = _chart(
        xt, yt,
        "Tỷ lệ áp P2'/P1 hoặc P2/P1 / pressure ratio",
        "Hệ số dòng F / flow factor F",
        right=right)
    for i, k in enumerate((1.00, 1.30, 1.60, 1.90)):
        pts = []
        for j, r in enumerate((1.00, 0.995, 0.99, 0.985, 0.98, 0.975, 0.97)):
            f = 0.27 + (0.73 / 6) * j * (0.72 + 0.09 * i)
            pts.append((X(r), Y(min(1.0, f))))
        _curve(e, pts, GREY, 1.1)
    for i, k in enumerate((1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9)):
        fmax = 0.64 + 0.025 * i
        pts = []
        for j in range(11):
            r = 0.92 - 0.052 * j
            f = 0.30 + (fmax - 0.30) * (1 - math.exp(-3.0 * (0.94 - r)))
            pts.append((X(max(0.40, r)), Y(f)))
        _curve(e, pts, BLUE if i in (0, 4, 9) else GREY,
               1.6 if i in (0, 4, 9) else 0.8)
    e.append(_txt(X(0.62), Y(0.83) - 8, "k = 1.90", 6.0, color=BLUE))
    e.append(_txt(X(0.68), Y(0.70) + 8, "k = 1.30", 6.0, color=GREY))
    e.append(_txt(X(0.74), Y(0.58) + 8, "k = 1.00", 6.0, color=GREY))
    return _fig7(
        2, "Flow correction factor F for subsonic nozzle flow",
        "Hệ số hiệu chỉnh dòng F cho dòng qua miệng phụ âm",
        [(("họ đường k = 1.00…1.90", "k curves 1.00…1.90"), (300, 150)),
         (("thang F trái", "left F scale"), (52, 100)),
         (("thang F phải", "right F scale"), (366, 100)),
         (("tỷ lệ áp suất", "pressure ratio"), (210, 314))],
        extra=e,
        courtesy="Anderson, Greenwood &amp; Co., Catalog 90/9000-US.96")


@_reg14
def fig_vsh_7_3():
    xt = [(v, str(v)) for v in range(0, 51, 5)]
    yt = [(0.50 + 0.05 * i, "%.2f" % (0.50 + 0.05 * i)) for i in range(11)]
    e, X, Y = _chart(xt, yt, "Phần trăm áp ngược / percent back pressure",
                     "Hệ số Kb / back-pressure factor Kb")
    _curve(e, [(X(v), Y(1.0 if v <= 30 else 1.0 - 0.0016 * (v - 30) ** 1.25))
               for v in range(0, 51, 2)], GREEN, 2.0)
    _curve(e, [(X(v), Y(1.0 if v <= 30 else 1.0 - 0.0052 * (v - 30) ** 1.25))
               for v in range(0, 51, 2)], HOT_F, 2.0)
    e.append(_txt(X(39), Y(0.94) - 8, "20% overpressure", 6.2, color=GREEN))
    e.append(_txt(X(42), Y(0.80) + 6, "10% overpressure", 6.2, color=HOT_F))
    return _fig7(
        3, "Back-pressure correction Kb for bellows-balanced gas valves",
        "Hệ số hiệu chỉnh áp ngược Kb cho van khí cân bằng bellows",
        [(("vùng Kb = 1", "Kb = 1 plateau"), (150, 60)),
         (("đường quá áp 20%", "20% overpressure curve"), (312, 70)),
         (("đường quá áp 10%", "10% overpressure curve"), (330, 130))],
        extra=e,
        courtesy="API RP 520 Part I, December 1976, American Petroleum Institute",
        sub="Áp ngược tích lũy và áp ngược chồng lên / built-up and superimposed back pressure")


@_reg14
def fig_vsh_7_4():
    xt = [(0.95 + 0.05 * i, "%.2f" % (0.95 + 0.05 * i)) for i in range(6)]
    ps = list(range(1500, 3201, 100))
    yt = [(p, str(p)) for p in ps]
    yf = lambda p: Y1 - (p - 1500) / 1700 * (Y1 - Y0)
    right = [(yf(p), "%d / %.1f" % (round(p * 6.895, -1), p / 14.504))
             for p in (1500, 2000, 2500, 3000, 3200)]
    e, X, Y = _chart(xt, yt, "Hệ số hiệu chỉnh KN / correction factor KN",
                     "Áp suất psia / pressure, psia", right=right)
    _curve(e, [(X(k), Y(p)) for k, p in
               [(1.00, 1500), (1.03, 2000), (1.055, 2300), (1.08, 2600),
                (1.11, 2850), (1.15, 3050), (1.20, 3200)]], BLUE, 2.2)
    e.append(_txt(372, 40, "kPaa / bara", 5.8, color=GREY, anchor="start"))
    return _fig7(
        4, "Napier correction KN for high-pressure saturated steam",
        "Hệ số hiệu chỉnh Napier KN cho hơi bão hòa áp cao",
        [(("KN = 1 dưới 105 bara", "KN = 1 below 105 bara"), (150, 280)),
         (("vùng áp cao", "high-pressure range"), (250, 100)),
         (("thang psia / kPaa / bara", "psia / kPaa / bara scales"), (360, 60))],
        extra=e,
        courtesy="Crosby Engineering Handbook, TP-V300, Crosby Valve &amp; Gage Company")


@_reg14
def fig_vsh_7_5():
    xt = [(v, str(v)) for v in range(10, 51, 5)]
    yt = [(v / 10.0, "%.1f" % (v / 10.0)) for v in range(0, 12)]
    e, X, Y = _chart(xt, yt, "Phần trăm quá áp / percent overpressure",
                     "Hệ số Kp / capacity factor Kp")
    pts = [(10, 0.61), (15, 0.80), (20, 0.91), (25, 0.995),
           (30, 1.02), (35, 1.045), (40, 1.06), (45, 1.075), (50, 1.09)]
    _curve(e, [(X(a), Y(b)) for a, b in pts], BLUE, 2.2)
    e.append(_line(X(25), Y0, X(25), Y(0.995), 0.9, GREY, "4 3"))
    e.append(_txt(X(25) + 5, Y(0.995) - 8, "mở hoàn toàn / full lift", 6.0,
                  color=GREY))
    return _fig7(
        5, "Liquid-service overpressure factor Kp",
        "Hệ số quá áp Kp cho van dùng cho chất lỏng",
        [(("Kp tăng tới 25%", "Kp rises to 25%"), (112, 98)),
         (("trên 25% chỉ đổi theo quá áp", "above 25% only overpressure changes"),
          (270, 66)),
         (("dưới 10% dễ rung van", "below 10% chatter risk"), (66, 164))],
        extra=e,
        courtesy="API RP 520 Part I, 6th Edition, March 1993, American Petroleum Institute",
        sub="Van cần 25% quá áp để mở hoàn toàn / valve needs 25% overpressure for full lift")


@_reg14
def fig_vsh_7_6():
    xt = [(v, str(v)) for v in range(0, 51, 10)]
    yt = [(0.50 + 0.05 * i, "%.2f" % (0.50 + 0.05 * i)) for i in range(11)]
    e, X, Y = _chart(xt, yt, "Phần trăm áp ngược / percent back pressure",
                     "Hệ số Kw / back-pressure factor Kw")
    pts = [(0, 1.0), (10, 1.0), (12, 1.0), (20, 0.95), (30, 0.86),
           (40, 0.77), (50, 0.68)]
    _curve(e, [(X(a), Y(b)) for a, b in pts], BLUE, 2.2)
    e.append(_txt(X(29), Y(0.86) + 10, "bellows balanced", 6.0, color=GREY))
    return _fig7(
        6, "Back-pressure factor Kw for bellows-balanced liquid valves",
        "Hệ số áp ngược Kw cho van chất lỏng cân bằng bellows",
        [(("vùng không hiệu chỉnh", "no correction region"), (105, 62)),
         (("giảm dần theo áp ngược", "falls with back pressure"), (269, 142)),
         (("10% mở hoàn toàn", "10% full-lift valves"), (440, 330))],
        extra=e,
        courtesy="API RP 520 Part I, December 1976, American Petroleum Institute",
        sub="Van 25% quá áp; loại mở đầy trong 10% hỏi nhà chế tạo / 25% valves; 10% types: consult maker")


@_reg14
def fig_vsh_7_7():
    xs = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000, 100000]
    xt = [(v, str(v)) for v in xs]
    yt = [(0.30 + 0.10 * i, "%.1f" % (0.30 + 0.10 * i)) for i in range(8)]
    e, X, Y = _chart(xt, yt, "Reynolds, Re (thang log) / Reynolds number (log scale)",
                     "Hệ số độ nhớt Kv / viscosity factor Kv", logx=True)
    pts = [(30, 0.30), (50, 0.45), (100, 0.60), (200, 0.75),
           (400, 0.84), (1000, 0.91), (4000, 0.96), (20000, 0.985),
           (100000, 0.995)]
    _curve(e, [(X(a), Y(b)) for a, b in pts], BLUE, 2.2)
    return _fig7(
        7, "Viscosity correction Kv versus Reynolds number",
        "Hệ số hiệu chỉnh độ nhớt Kv theo số Reynolds",
        [(("đầu vào lặp Re", "Re enters the iteration"), (112, 276)),
         (("Kv áp vào diện tích ban đầu", "Kv applied to initial area"), (230, 108)),
         (("Kv tiến về 1", "Kv approaches 1"), (320, 64))],
        extra=e,
        courtesy="API RP 520 Part I, December 1976, American Petroleum Institute",
        sub="Lặp: diện tích không nhớt → Re → Kv → diện tích hiệu chỉnh / iterate non-viscous area → Re → Kv → corrected area")


@_reg14
def fig_vsh_7_8():
    xs = [1, 10, 100]
    xt = [(v, str(v)) for v in xs]
    yt = [(0.1, "0.1"), (1, "1"), (10, "10"), (30, "30")]
    e, X, Y = _chart(xt, yt,
                     "0.9 Ae / (An K)  (log)",
                     "Hệ số trở lực ζ / resistance coefficient ζ",
                     logx=True)
    for i, base in enumerate((0.10, 0.13, 0.17, 0.22, 0.28)):
        pts = [(X(v), Y(base * v)) for v in (1, 3, 10, 30, 100)
               if base * v <= 30]
        _curve(e, pts, BLUE if i == 4 else GREY, 1.5 if i == 4 else 1.0)
        xx = X(min(100, 27 / base))
        e.append(_txt(xx - 6, Y(27) - 8,
                      ("0", "0.02", "0.04", "0.08", "1.0")[i],
                      5.8, color=GREY))
    pts = [(X(v), Y(0.075 * v)) for v in (1, 3, 10, 30, 100)]
    _curve(e, pts, HOT_F, 1.6, "5 3")
    e.append(_txt(X(45), Y(3.4) - 8, "chất lỏng / liquids", 6.0, color=HOT_F))
    return _fig7(
        8, "Inlet-line resistance coefficient for 3% inlet loss",
        "Hệ số trở lực ống vào tương ứng tổn thất 3%",
        [(("đường tỷ lệ áp", "pressure-ratio lines"), (250, 118)),
         (("đường gạch đứt: chất lỏng", "dashed: liquids"), (208, 213)),
         (("ζ = 1 mốc tham chiếu", "ζ = 1 reference"), (70, 201))],
        extra=e,
        courtesy="AD-Merkblatt A2, Verband der Technischen Uberwachungs-Vereine e.V., Essen",
        sub="Áp dụng khí/hơi với k = 1.3; đường gạch đứt cho chất lỏng / gas and vapor k = 1.3; dashed line for liquids")


@_reg14
def fig_vsh_7_9():
    xt = [(v, str(v)) for v in range(0, 11, 1)]
    yt = [(v, str(v)) for v in range(1, 7)]
    e, X, Y = _chart(xt, yt, "Giá trị zeta / zeta value",
                     "Pae / P'' tại đầu ống / Pae / P'' at pipe end")
    for i, k in enumerate((1.0, 1.2, 1.4, 1.6, 1.8, 2.0)):
        a = 0.88 + 0.15 * i
        pts = [(X(v), Y(min(6.0, 1 + a * math.sqrt(v))))
               for v in [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        _curve(e, pts, HOT_F if i in (0, 5) else GREY,
               1.8 if i in (0, 5) else 0.9)
        e.append(_txt(X(9.2), Y(min(6.0, 1 + a * 3)) - 2,
                      "k = %.1f" % k, 5.8, color=GREY, anchor="start"))
    return _fig7(
        9, "Discharge-line resistance coefficient for gas or vapor",
        "Hệ số trở lực ống xả cho khí hoặc hơi",
        [(("họ đường k = 1.0…2.0", "k curves 1.0…2.0"), (280, 108)),
         (("Pae áp ngược tích lũy", "Pae built-up back pressure"), (150, 231)),
         (("P'' áp tới hạn ở đầu ống", "P'' critical at pipe end"), (330, 66))],
        extra=e,
        courtesy="Bopp &amp; Reuther, Safety Valves — Handbook for System Planners and Operators")
