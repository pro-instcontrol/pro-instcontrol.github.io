# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 11 — Diaphragm and Stainless Steel Valves
(book ch. 3, Figures 3-93 … 3-99).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology named in the original captions; a numbered bilingual
legend carries the feature names.  Figures 3-97 … 3-99 are editorial
schematic charts: the source text gives no numeric scales and warns that
allowable pressure/temperature depends on the construction material, so no
invented numbers are shown.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, INK, _circle, _defs, _ellipse, _fig,
                  _line, _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, PACK_F, RING_F, _ell, _emit, _emit_legend)

FIGS8 = {}


def _reg8(f):
    FIGS8[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
BONNET_F = "#ece9df"
MEMBRANE_F = "#c9d5c9"
DISC_F = "#d9d9d2"
PTFE_F = "#dfe8dd"


# ------------------------------------------------------- diaphragm geometry
def _dia_ops(weir=True, double_bonnet=False, tbranch=False,
             shroud=True, o_ring=False):
    """Cross-section ops; flow axis at local y=104, stem rises to y<0."""
    o = []
    half = 52.0
    crest = 110.0 if weir else 124.0
    centre = 96.0 if weir else 100.0
    closed_centre = crest - 2.0

    def under(x):
        return centre - (centre - 72.0) * (abs(x) / half) ** 2

    def above(x):
        return under(x) - 5.0

    xs = [-half + 2 * half * i / 12.0 for i in range(13)]

    # ---- body and flanges -------------------------------------------------
    o.append(("poly", [(-96, 68), (-68, 62), (68, 62), (96, 68),
                       (96, 140), (68, 146), (-68, 146), (-96, 140)],
              BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 104, 80), (sx * 96, 80),
                           (sx * 96, 132), (sx * 104, 132)],
                  RING_F, 1.2, INK, "", True))
        for yy in (88, 106, 124):
            o.append(("circ", sx * 100, yy, 1.8, 0.8, INK, ""))

    # ---- flow passage (white) following diaphragm and weir ----------------
    bore = [(-84, 84), (-52, 84)]
    bore += [(x, under(x)) for x in xs]
    bore += [(52, 84), (84, 84), (84, 124)]
    if weir:
        bore += [(52, 124), (20, crest), (-20, crest), (-52, 124),
                 (-84, 124)]
    else:
        bore += [(-84, 124)]
    o.append(("poly", bore, "#ffffff", 1.0, INK, "", True))

    # ---- bonnet(s) --------------------------------------------------------
    if double_bonnet:
        o.append(("poly", [(-60, 70), (-60, 48), (-50, 34), (50, 34),
                           (60, 48), (60, 70)],
                  BONNET_F, 1.2, INK, "", True))
        o.append(("poly", [(-50, 34), (-48, 10), (-30, -8), (30, -8),
                           (48, 10), (50, 34)],
                  BONNET_F, 1.2, INK, "", True))
        o.append(("line", -54, 34, 54, 34, 1.4, INK, ""))
        for xx in (-46, -24, 24, 46):
            o.append(("circ", xx, 34, 2.4, 0.8, INK, RING_F))
        top_y, hand_y, tip_y = -8.0, -140.0, -156.0
    else:
        o.append(("poly", [(-60, 70), (-60, 42), (-48, 18), (-24, 2),
                           (24, 2), (48, 18), (60, 42), (60, 70)],
                  BONNET_F, 1.2, INK, "", True))
        o.append(("line", -58, 70, 58, 70, 1.5, INK, ""))
        for xx in (-46, -26, 26, 46):
            o.append(("circ", xx, 70, 2.4, 0.8, INK, RING_F))
        top_y, hand_y, tip_y = 2.0, -126.0, -142.0

    # ---- diaphragm, compressed between body and bonnet -------------------
    band = [(x, above(x)) for x in xs]
    band += [(x, under(x)) for x in reversed(xs)]
    o.append(("poly", band, MEMBRANE_F, 1.2, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 46, 68), (sx * 58, 68),
                           (sx * 58, 80), (sx * 46, 80)],
                  MEMBRANE_F, 1.0, INK, "", True))
    # rubber backing on a PTFE face, as described for weir-type valves
    o.append(("poly", [(x, above(x) - 3.0) for x in xs[1:-1]]
              + [(xs[-2], above(xs[-2])), (xs[1], above(xs[1]))],
              "none", 0.9, "#6f8f6f", "2 2", True))
    # dashed closed position on the straight-through variant
    if not weir:
        o.append(("poly", [(x, closed_centre
                            - (closed_centre - 74.0) * (abs(x) / half) ** 2)
                           for x in xs],
                  "none", 1.0, GREY, "3 2", False))

    # ---- compressor plate, rising stem, packing, handwheel ---------------
    comp = [(x, above(x) - 3.0) for x in xs]
    o.append(("poly", comp, "none", 1.2, INK, "", False))
    o.append(("line", 0, above(0) - 3.0, 0, tip_y, 2.2, INK, ""))
    o.append(("poly", [(-11, top_y - 8), (11, top_y - 8),
                       (11, top_y + 6), (-11, top_y + 6)],
              PACK_F, 1.0, INK, "", True))
    o.append(("line", -14, top_y + 6, 14, top_y + 6, 1.2, INK, ""))
    if o_ring:
        o.append(("circ", 0, top_y + 12, 3.4, 0.9, INK, RING_F))
    if shroud:
        o.append(("poly", [(-6, hand_y + 12), (6, hand_y + 12),
                           (6, top_y + 7), (-6, top_y + 7)],
                  "#ffffff", 0.9, GREY, "", True))
        o.append(("poly", [(-6, hand_y + 14), (6, hand_y + 14),
                           (6, hand_y + 24), (-6, hand_y + 24)],
                  GOLD, 0.9, INK, "", True))
        o.append(("line", -18, hand_y + 30, -12, hand_y + 30, 1.0, INK, ""))
        o.append(("line", 12, hand_y + 30, 18, hand_y + 30, 1.0, INK, ""))
    o.append(("poly", _ell(0, hand_y, 28, 6), "#e8e8e2", 1.2, INK, "", True))
    o.append(("poly", _ell(0, hand_y, 22, 3.6), "none", 0.9, INK, "", True))
    o.append(("line", 0, tip_y, 0, hand_y - 6, 1.6, INK, ""))

    # ---- T-branch for true sampling --------------------------------------
    if tbranch:
        o.append(("poly", [(-20, 124), (20, 124), (20, 164), (-20, 164)],
                  BODY_F, 1.2, INK, "", True))
        o.append(("poly", [(-13, 112), (13, 112), (13, 164), (-13, 164)],
                  "#ffffff", 0.9, INK, "", True))
        o.append(("poly", [(-28, 164), (28, 164), (28, 172), (-28, 172)],
                  RING_F, 1.1, INK, "", True))
        o.append(("poly", [(-9, 144), (9, 144), (9, 152), (-9, 152)],
                  DISC_F, 1.0, INK, "", True))
        o.append(("line", 0, 152, 0, 180, 1.4, INK, ""))
        o.append(("line", -10, 180, 10, 180, 1.4, INK, ""))
        o.append(("line", 0, 102, 0, 128, 1.4, BLUE, ""))
        o.append(("poly", [(0, 132), (-3.2, 124), (3.2, 124)],
                  BLUE, 0, BLUE, "", True))

    # ---- flow direction ---------------------------------------------------
    o.append(("line", -78, 104, -58, 104, 1.6, BLUE, ""))
    o.append(("poly", [(-58, 104), (-66, 100.5), (-66, 107.5)],
              BLUE, 0, BLUE, "", True))
    o.append(("line", 58, 104, 78, 104, 1.6, BLUE, ""))
    o.append(("poly", [(78, 104), (70, 100.5), (70, 107.5)],
              BLUE, 0, BLUE, "", True))
    return o


def _dia_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
             w=560, h=380, xleg=402):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=200, dy=180)
    if sub:
        o2.append(_txt(200, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "Hình 3-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 3-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


COURTESY = "Saunders Valve Company Limited."


@_reg8
def fig_vsh_3_93():
    return _dia_fig(
        93, "Diaphragm valve, weir type",
        "Van màng kiểu đập (weir)",
        [(("đập trong đường dòng", "weir in the flow passage"), (224, 290)),
         (("màng và đệm cao su", "diaphragm with elastomer backing"),
          (200, 272)),
         (("bản ép (compressor)", "compressor plate"), (176, 264)),
         (("bọc tay quay, ống chỉ báo, buồng mỡ",
           "shroud, lift sleeve, grease chamber"),
          (200, 78)),
         (("thân van, hai bích đường ống", "valve body and pipeline flanges"),
          (106, 280))],
        _dia_ops(weir=True, shroud=True), courtesy=COURTESY)


@_reg8
def fig_vsh_3_94():
    return _dia_fig(
        94, "Diaphragm valve, straight-through type",
        "Van màng kiểu đường thẳng",
        [(("đường dòng thẳng, không có đập", "straight passage without a weir"),
          (224, 304)),
         (("màng uốn nhiều hơn", "more highly flexed diaphragm"),
          (200, 272)),
         (("vị trí đóng (nét đứt)", "closed position (dashed)"), (176, 284)),
         (("bulông nắp van", "bonnet bolting"), (200, 210)),
         (("thân van, hai bích đường ống", "valve body and pipeline flanges"),
          (106, 280))],
        _dia_ops(weir=False, shroud=True), courtesy=COURTESY)


@_reg8
def fig_vsh_3_95():
    return _dia_fig(
        95, "Diaphragm valve, weir type, with double-bonnet assembly for "
        "large valve sizes",
        "Van màng kiểu đập có cụm nắp kép cho cỡ van lớn",
        [(("cụm nắp kép, hai nửa bắt bulông", "double bonnet, bolted together"),
          (200, 214)),
         (("màng và đệm cao su", "diaphragm with elastomer backing"),
          (200, 272)),
         (("đập trong đường dòng", "weir in the flow passage"), (224, 290)),
         (("thân và bích cỡ lớn", "larger body and flanges"), (106, 280)),
         (("tay quay và cần van", "handwheel and rising stem"),
          (200, 44))],
        _dia_ops(weir=True, double_bonnet=True, shroud=False),
        courtesy=COURTESY)


@_reg8
def fig_vsh_3_96():
    return _dia_fig(
        96, "Diaphragm valve, weir type, with T-branch for sampling duty",
        "Van màng kiểu đập có nhánh chữ T để lấy mẫu",
        [(("đập trong đường dòng", "weir in the flow passage"), (224, 290)),
         (("nhánh lấy mẫu chữ T", "T-branch for true sampling"),
          (200, 330)),
         (("dòng chính không bị cản", "main flow is not impeded"),
          (150, 280)),
         (("màng và bản ép", "diaphragm and compressor"), (200, 268)),
         (("nắp van", "bonnet"), (200, 210))],
        _dia_ops(weir=True, tbranch=True, shroud=False), courtesy=COURTESY)


# ------------------------------------------------------------ schematic charts
def _chart_base(ten, xlabel, ylabel, y0=46.0, ph=268.0):
    x0, pw = 62.0, 372.0
    o = []
    for i in range(5):
        yy = y0 + i * ph / 4.0
        o.append(_line(x0, yy, x0 + pw, yy, 0.5, color="#d8d5cc"))
        xx = x0 + i * pw / 4.0
        o.append(_line(xx, y0, xx, y0 + ph, 0.5, color="#d8d5cc"))
    o.append(_rect(x0, y0, pw, ph, "none", 1.2, stroke=INK))
    o.append(_txt(x0, y0 - 12, ylabel, 7.6, anchor="start", color=INK,
                  weight="bold"))
    o.append(_txt(x0 + pw / 2.0, y0 + ph + 28, xlabel, 8.2, color=INK,
                  weight="bold"))
    return o, x0, y0, pw, ph


def _pt_chart(num, ten, tvi, straight, source):
    """Qualitative pressure/temperature envelope — no invented scale."""
    o, x0, y0, pw, ph = _chart_base(
        ten, "Nhiệt độ / Temperature (°C)",
        "Áp suất làm việc / Working pressure (bar)")
    hi = [0.86, 0.90, 0.86, 0.72, 0.50, 0.26] if not straight else \
         [0.66, 0.70, 0.64, 0.50, 0.32, 0.16]
    lo = [0.72, 0.76, 0.70, 0.54, 0.34, 0.14] if not straight else \
         [0.52, 0.54, 0.48, 0.36, 0.22, 0.08]
    pts = [(x0 + i * pw / 5.0, y0 + ph * (1.0 - hi[i])) for i in range(6)]
    band = pts + [(x0 + i * pw / 5.0, y0 + ph * (1.0 - lo[i]))
                  for i in reversed(range(6))]
    o.append(_poly(band, "#e5eee4", 0.0, GREY, "", True))
    o.append(_poly(pts, "none", 1.8, INK))
    o.append(_poly([(x0 + i * pw / 5.0, y0 + ph * (1.0 - lo[i]))
                    for i in range(6)], "none", 1.4, BLUE, "4 3"))
    o.append(_txt(x0 + 10, y0 + 16,
                  "Miền áp suất/nhiệt độ điển hình / typical envelope",
                  7.0, anchor="start", color=GREY))
    for i, (vi, en) in enumerate([
            ("giới hạn theo vật liệu", "limit depends on material"),
            ("cấu hình khác", "other construction")]):
        yy = y0 + 16 + i * 20
        o.append(_line(444, yy - 3, 458, yy - 3, 1.6,
                       INK if i == 0 else BLUE, "" if i == 0 else "4 3"))
        o.append(_txt(462, yy, vi, 6.4, anchor="start"))
        o.append(_txt(462, yy + 8, en, 5.8, anchor="start", color=GREY))
    o.append(_txt(x0 + pw / 2.0, y0 + ph + 38,
                  "Sơ đồ biên tập, không theo tỉ lệ — xem catalog / "
                  "editorial, not to scale — see catalogue",
                  6.8, color=GREY))
    o.append(_txt(476, 372, source, 6.4, color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o), ten),
                "Hình 3-%d · %s (sơ đồ biên tập, vẽ lại; không theo tỉ lệ). "
                "Nguồn: %s" % (num, tvi, source),
                "Figure 3-%d · %s (editorial schematic, redrawn; not to "
                "scale). Courtesy of %s" % (num, ten, source.rstrip(".") + "."),
                tvi, ten)


@_reg8
def fig_vsh_3_97():
    return _pt_chart(
        97, "Pressure/temperature relationship of weir-type diaphragm valves",
        "Quan hệ áp suất/nhiệt độ của van màng kiểu đập",
        straight=False, source=COURTESY)


@_reg8
def fig_vsh_3_98():
    return _pt_chart(
        98, "Pressure/temperature relationship of straight-through "
        "diaphragm valves",
        "Quan hệ áp suất/nhiệt độ của van màng kiểu đường thẳng",
        straight=True, source=COURTESY)


@_reg8
def fig_vsh_3_99():
    ten = "Inherent and installed flow characteristics of weir-type " \
          "diaphragm valves"
    tvi = "Đặc tính dòng vốn có và sau lắp đặt của van màng kiểu đập"
    o, x0, y0, pw, ph = _chart_base(
        ten, "Độ mở van / Valve opening (%)",
        "Lưu lượng tương đối / Relative flow")
    for i in range(5):
        o.append(_txt(x0 + i * pw / 4.0, y0 + ph + 14,
                      ["0", "25", "50", "75", "100"][i], 7.0, color=INK))
    inherent = [0.03, 0.14, 0.32, 0.56, 0.80, 0.93]
    installed = [0.02, 0.10, 0.22, 0.36, 0.50, 0.60]
    for vals, col in ((inherent, INK), (installed, BLUE)):
        pts = [(x0 + i * pw / 5.0, y0 + ph * (1.0 - vals[i]))
               for i in range(6)]
        o.append(_poly(pts, "none", 1.8, col))
    for i, (vi, en) in enumerate([
            ("đặc tính vốn có", "inherent characteristic"),
            ("đặc tính sau lắp đặt", "installed characteristic")]):
        yy = y0 + 20 + i * 22
        o.append(_line(444, yy - 3, 458, yy - 3, 1.8,
                       INK if i == 0 else BLUE))
        o.append(_txt(462, yy, vi, 6.6, anchor="start"))
        o.append(_txt(462, yy + 8, en, 5.8, anchor="start", color=GREY))
    o.append(_txt(x0 + pw / 2.0, y0 + ph + 38,
                  "Dạng đường đổi theo cỡ van; cam biến đổi được / curves "
                  "vary with size; variable cam available", 6.6, color=GREY))
    o.append(_txt(476, 372, COURTESY, 6.4, color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o), ten),
                "Hình 3-99 · %s (sơ đồ biên tập, vẽ lại; không theo tỉ lệ). "
                "Nguồn: %s" % (tvi, COURTESY),
                "Figure 3-99 · %s (editorial schematic, redrawn; not to "
                "scale). Courtesy of %s" % (ten, COURTESY.rstrip(".") + "."),
                tvi, ten)
