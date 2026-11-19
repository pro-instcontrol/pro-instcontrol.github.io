# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 21 — Appendices
(Appendix B, Figures B-1 … B-3 compressibility factor charts).  The
full-page source charts are redrawn as one simplified editorial chart
that preserves the working principle: Z as a function of reduced
pressure Pr for a family of reduced temperatures Tr.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _defs, _fig, _line, _poly,
                  _txt, svg)
from vshfig3 import _emit, _emit_legend

FIGS18 = {}


def _reg18(f):
    FIGS18[f.__name__] = f
    return f


INKC = "#1a1a1a"
XLEG = 402
CURVE = ["#1f5fa8", "#2f8f5b", "#a8642f", "#7a3fa8", "#a82f4f", "#5c6b7a"]


def _path(pts):
    """Dashed-capable polyline as a poly op with close=False."""
    return ("poly", pts, "none", 1.4, INK, "", False)


@_reg18
def fig_vsh_b_1():
    """Figure B-1 — compressibility factor Z versus reduced pressure."""
    ten = ("Compressibility factor Z as a function of reduced pressure "
           "Pr for a family of reduced temperatures Tr (simplified from "
           "Appendix B charts)")
    tvi = ("Hệ số nén Z theo áp suất quy đổi Pr cho họ nhiệt độ quy đổi "
           "Tr (vẽ rút gọn từ các biểu đồ phụ lục B)")
    ops = []
    # plot frame: origin (70,300), x to 380 (Pr 0..10), y up to 40 (Z 1.1..0)
    x0, y0, x1, y1 = 70, 300, 380, 44
    ops.append(("poly", [(x0, y1), (x1, y1), (x1, y0), (x0, y0)],
                "#fbfbf8", 1.4, INKC, "", True))
    # gridlines + ticks
    for z in (0.2, 0.4, 0.6, 0.8, 1.0):
        yy = y0 - (y0 - y1) * z / 1.1
        ops.append(("line", x0, yy, x1, yy, 0.6, "#cccccc", ""))
        ops.append(_txt(x0 - 8, yy + 3, "%.1f" % z, 7.0, color=GREY,
                        anchor="end"))
    for pr in range(1, 11):
        xx = x0 + (x1 - x0) * pr / 10.0
        ops.append(("line", xx, y0, xx, y0 - 5, 0.8, INKC, ""))
        if pr % 2 == 0 or pr == 1:
            ops.append(_txt(xx, y0 + 14, str(pr), 7.0, color=GREY))
    # Z = 1 ideal line
    z1 = y0 - (y0 - y1) * 1.0 / 1.1
    ops.append(("line", x0, z1, x1, z1, 1.0, GREY, "6,4"))
    ops.append(_txt(x1 - 6, z1 - 6, "Z = 1 (khí lý tưởng / ideal gas)",
                    6.8, color=GREY, anchor="end"))
    # Tr family curves (qualitative, generalized compressibility shape)
    def curve(tr, peak_pr, peak_z, end_z, shade=0.0):
        pts = []
        n = 40
        for i in range(n + 1):
            pr = 10.0 * i / n
            # logistic dip then recovery, tuned per Tr
            t = pr / 10.0
            dip = (peak_z - end_z) * (1.0 - math.exp(-3.0 * t / (peak_pr / 10.0)))
            base = 1.0 + (peak_z - 1.0) * math.exp(-((t - peak_pr / 10.0)
                                                     * 3.0) ** 2)
            z = base - dip * t
            z = min(max(z, 0.05), 1.08)
            xx = x0 + (x1 - x0) * pr / 10.0
            yy = y0 - (y0 - y1) * z / 1.1
            pts.append((xx, yy))
        return pts
    fam = [(1.05, 0.55, 0.22, 0.85), (1.1, 0.6, 0.30, 0.92),
           (1.2, 0.75, 0.45, 1.00), (1.4, 0.9, 0.62, 1.04),
           (2.0, 1.4, 0.86, 1.04), (5.0, 3.0, 1.00, 1.05)]
    for i, (tr, pp, pz, ez) in enumerate(fam):
        ops.append(_path(curve(tr, pp, pz, ez)))
        lx = x1 - 14
        ly = y0 - (y0 - y1) * (pz + 0.05) / 1.1 - i * 0
        ops.append(_txt(lx, y0 - (y0 - y1) * min(pz + 0.09, 1.05) / 1.1,
                        "Tr = %s" % ("%.2f" % tr).rstrip("0").rstrip("."),
                        6.8, color=CURVE[i % len(CURVE)], anchor="end"))
    # axis labels
    ops.append(_txt((x0 + x1) / 2, y0 + 30, "Pr — áp suất quy đổi / "
                    "reduced pressure", 7.6, weight="bold"))
    ops.append(_txt(x0 - 46, (y0 + y1) / 2, "Z", 8.0, weight="bold"))
    extra = [
        _txt(70, 336, "Pr = P / Pc,  Tr = T / Tc  (Pc, Tc — áp suất và "
             "nhiệt độ tới hạn của lưu chất, xem Bảng B-1)", 6.8,
             color=GREY),
    ]
    marks = [
        (("họ đường Tr", "family of Tr curves"), (330, 120)),
        (("đường Z = 1", "ideal-gas line"), (330, 176)),
        (("cực đại gần Pr ≈ 1", "peak near Pr ≈ 1"), (150, 210)),
        (("giá trị Z tối thiểu", "minimum Z"), (200, 262)),
    ]
    o2 = []
    _emit(o2, ops)
    o2.extend(extra)
    _emit_legend(o2, XLEG, marks)
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình B-1 · %s (vẽ lại, rút gọn)." % tvi,
                "Figure B-1 · %s — redrawn, simplified." % ten,
                tvi, ten)
