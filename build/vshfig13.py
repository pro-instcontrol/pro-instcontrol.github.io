# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 16 — Rupture Discs: Selection
(book ch. 6, Figures 6-34 … 6-38).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Pressure-level and explosion charts are editorial schematics redrawn from
the source explanations; no numeric scales are invented where the source
gives none.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _txt, svg)
from vshfig3 import RING_F, _emit, _emit_legend

FIGS13 = {}


def _reg13(f):
    FIGS13[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
PANEL_F = "#d9d9d2"
FLAME_F = "#d98b4a"
HOT_F = "#b5533d"
COOL_F = "#9bbfd1"
XLEG = 402


def _scale_ops(ops, s=1.0, dx=0.0, dy=0.0):
    out = []
    for op in ops:
        k = op[0]
        if k == "poly":
            _, pts, fill, sw, color, dash, close = op
            out.append(("poly", [(x * s + dx, y * s + dy) for x, y in pts],
                        fill, sw, color, dash, close))
        elif k == "line":
            _, x1, y1, x2, y2, sw, color, dash = op
            out.append(("line", x1 * s + dx, y1 * s + dy,
                        x2 * s + dx, y2 * s + dy, sw, color, dash))
        elif k == "circ":
            _, cx, cy, r, sw, color, fill = op
            out.append(("circ", cx * s + dx, cy * s + dy, r * s,
                        sw, color, fill))
        else:
            out.append(op)
    return out


def _arrow(o, x1, y1, x2, y2, color=BLUE, sw=1.5):
    o.append(("line", x1, y1, x2, y2, sw, color, ""))
    a = math.atan2(y2 - y1, x2 - x1)
    for d in (2.55, -2.55):
        o.append(("line", x2, y2,
                  x2 + 7 * math.cos(a + d), y2 + 7 * math.sin(a + d),
                  sw, color, ""))


def _rd_fig(num, ten, tvi, marks, panels=(), extra=(), courtesy="", sub=""):
    o2 = []
    for ops, dx, dy in panels:
        _emit(o2, ops, dx=dx, dy=dy)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, 350, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(476, 366, courtesy, 6.4, color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 6-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 6-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _chart_6_34():
    e = []
    e.append(_line(70, 316, 358, 316, 1.4, color=INK))
    e.append(_line(70, 316, 70, 62, 1.4, color=INK))
    e.append(_txt(214, 340, "Mức áp suất / pressure level →",
                  7.8, color=INK))
    e.append(_txt(38, 190, "Áp suất", 7.8, color=INK))
    levels = [
        (106, "MAWP áp làm việc tối đa cho phép", "MAWP", INK),
        (146, "Áp vỡ định mức cộng sai số", "rated + tolerance", HOT_F),
        (186, "Áp vỡ định mức", "rated burst", BLUE),
        (226, "Áp vỡ nhỏ nhất ~82% MAWP", "minimum burst ~82%", GREEN),
        (276, "Áp vận hành ≤57% MAWP", "operating ≤57%", GREY),
    ]
    for y, vi, en, col in levels:
        e.append(_line(82, y, 350, y, 1.2, color=col,
                       dash="4 3" if col in (INK, GREY) else ""))
        e.append(_txt(86, y - 5, vi, 6.8, anchor="start", color=col))
        e.append(_txt(86, y + 7, en, 6.2, anchor="start", color=col))
    e.append(_poly([(120, 134), (120, 158), (318, 158), (318, 134)],
                   "none", sw=1.2, color=HOT_F, close=False))
    e.append(_txt(220, 128, "sai số áp vỡ ±5% / burst tolerance ±5%",
                  6.4, color=HOT_F))
    e.append(_poly([(150, 178), (150, 194), (300, 194), (300, 178)],
                   "none", sw=1.2, color=BLUE, close=False))
    e.append(_txt(225, 210, "phạm vi chế tạo +10%/−5% / manufacturing range",
                  6.4, color=BLUE))
    e.append(_txt(214, 46, "Sơ đồ điển hình, không có thang số / typical only, no numeric scale",
                  6.6, color=GREY))
    return e


def _vent_panel_ops(state="intact"):
    o = []
    o.append(("poly", [(-64, 30), (64, 30), (64, 54), (-64, 54)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-54, 30), (54, 30), (54, 46), (-54, 46)],
              "#ffffff", 1.0, INK, "", True))
    if state == "intact":
        o.append(("poly", [(-48, 46), (48, 46), (48, 6), (-48, 6)],
                  PANEL_F, 1.3, INK, "", True))
        o.append(("circ", 0, 26, 18, 1.0, GREY, ""))
        o.append(("line", -34, 14, 34, 14, 0.8, GREY, "4 3"))
    else:
        o.append(("poly", [(-48, 46), (-12, 46), (-22, -8), (-44, 30)],
                  PANEL_F, 1.2, INK, "", True))
        o.append(("poly", [(12, 46), (48, 46), (44, 30), (22, -12)],
                  PANEL_F, 1.2, INK, "", True))
        o.append(("poly", [(-10, 46), (10, 46), (0, 4)],
                  PANEL_F, 1.2, INK, "", True))
        _arrow(o, 0, -24, 0, 4, BLUE)
    return o


def _chart_6_36():
    e = []
    e.append(_line(80, 306, 360, 306, 1.4, color=INK))
    e.append(_line(80, 306, 80, 62, 1.4, color=INK))
    e.append(_txt(220, 330, "Thời gian / time →", 7.8, color=INK))
    e.append(_txt(40, 186, "Áp suất", 7.8, color=INK))
    e.append(_line(88, 106, 352, 106, 1.0, GREY, "4 3"))
    e.append(_txt(300, 98, "Pmax không thông hơi / unvented", 6.2, color=GREY))
    e.append(_line(88, 152, 352, 152, 1.0, GREEN, "4 3"))
    e.append(_txt(302, 144, "Pult bình / enclosure", 6.2, color=GREEN))
    e.append(_line(88, 212, 352, 212, 1.0, BLUE, "4 3"))
    e.append(_txt(302, 204, "Pred đã giảm / reduced", 6.2, color=BLUE))
    unvented = [(90, 296), (130, 240), (170, 180), (210, 130),
                (250, 104), (300, 96)]
    vented = [(90, 296), (130, 248), (170, 218), (210, 208),
              (250, 206), (300, 205)]
    e.append(_poly(unvented, "none", sw=2.0, color=HOT_F, close=False))
    e.append(_poly(vented, "none", sw=2.0, color=BLUE, close=False))
    e.append(_circle(170, 218, 6, sw=1.2, color=INK))
    e.append(_txt(170, 238, "Pstat mở tấm thông / vent opens",
                  6.4, color=INK))
    e.append(_txt(214, 48, "Đường xuân theo lời giải thích nguồn / qualitative from the source",
                  6.6, color=GREY))
    return e


def _flame_test_ops():
    o = []
    # protected vessel and vent duct
    o.append(("poly", [(20, 120), (20, 260), (150, 260), (150, 210),
                       (220, 210), (220, 170), (150, 170), (150, 120)],
              BODY_F, 1.4, INK, "", True))
    o.append(("poly", [(20, 136), (150, 136), (150, 244), (20, 244)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(220, 170), (320, 170), (320, 206), (220, 206)],
              "#ffffff", 1.0, INK, "", True))
    # fireball below and horizontally from the vent
    o.append(("poly", [(238, 206), (268, 246), (322, 272), (368, 260),
                       (340, 222), (306, 206), (270, 198)],
              FLAME_F, 0.9, HOT_F, "", True))
    o.append(("poly", [(286, 206), (326, 224), (370, 222), (344, 198),
                       (310, 190)],
              HOT_F, 0.8, HOT_F, "", True))
    # flame travelling inside the duct
    for x in (244, 268, 292, 316):
        o.append(("poly", [(x, 176), (x + 9, 188), (x + 18, 176)],
                  HOT_F, 0.8, HOT_F, "", True))
    _arrow(o, 240, 188, 330, 188, HOT_F, 1.4)
    return o


def _vent_system_ops():
    o = []
    # vessel and short duct toward exterior wall
    o.append(("poly", [(16, 132), (16, 258), (140, 258), (140, 214),
                       (196, 214), (196, 172), (140, 172), (140, 132)],
              BODY_F, 1.4, INK, "", True))
    o.append(("poly", [(16, 148), (140, 148), (140, 244), (16, 244)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(140, 42), (204, 42), (204, 172), (140, 172)],
              BODY_F, 1.2, INK, "", True))
    o.append(("poly", [(150, 42), (194, 42), (194, 172), (150, 172)],
              "#ffffff", 1.0, INK, "", True))
    # vent panel at the duct entrance
    o.append(("poly", [(140, 120), (204, 120), (204, 132), (140, 132)],
              PANEL_F, 1.2, INK, "", True))
    # flame trap tube and ceramic filter mat
    o.append(("poly", [(156, 60), (188, 60), (188, 112), (156, 112)],
              RING_F, 1.1, INK, "", True))
    for yy in (70, 82, 94):
        o.append(("line", 156, yy, 188, yy + 4, 1.0, GREY, ""))
        o.append(("line", 188, yy, 156, yy + 4, 1.0, GREY, ""))
    o.append(("poly", [(156, 52), (188, 52), (188, 58), (156, 58)],
              "#8c887c", 1.0, INK, "", True))
    # hot inlet and cool outlet arrows
    _arrow(o, 172, 158, 172, 116, HOT_F, 1.4)
    _arrow(o, 172, 52, 172, 18, COOL_F, 1.4)
    return o


# ------------------------------------------------------------------- figures
@_reg13
def fig_vsh_6_34():
    return _rd_fig(
        34, "Typical pressure-level relationships for an installed "
           "rupture disc as the sole relief device",
        "Quan hệ mức áp điển hình khi đĩa vỡ là thiết bị giảm áp duy nhất",
        [(("MAWP", "MAWP"), (300, 106)),
         (("đỉnh sai số áp vỡ", "upper burst tolerance"), (300, 146)),
         (("áp vỡ nhỏ nhất ~82%", "minimum burst ~82%"), (300, 226)),
         (("áp vận hành ≤57%", "operating ≤57%"), (300, 276))],
        extra=_chart_6_34(),
        courtesy="Fike Metal Products")


@_reg13
def fig_vsh_6_35():
    return _rd_fig(
        35, "Composite explosion vent panel before and after bursting",
        "Tấm thông nổ composite trước và sau khi vỡ",
        [(("tấm composite", "composite panel"), (110, 202)),
         (("cánh vỡ mở ra", "opened petals"), (295, 196)),
         (("dòng xả qua cửa thông", "discharge through vent"), (295, 148))],
        panels=[(_vent_panel_ops("intact"), 110, 185),
                (_vent_panel_ops("burst"), 295, 185)],
        extra=(_txt(110, 138, "trước / before", 7.2, color=GREY),
               _txt(295, 138, "sau / after", 7.2, color=GREY)),
        courtesy="Continental Disc Corporation")


@_reg13
def fig_vsh_6_36():
    return _rd_fig(
        36, "Comparison of vented and unvented explosion pressures",
        "So sánh áp suất nổ khi có và không có cửa thông",
        [(("Pmax không thông hơi", "unvented Pmax"), (300, 96)),
         (("Pult của bình", "enclosure Pult"), (300, 152)),
         (("Pred đã giảm", "reduced Pred"), (300, 212)),
         (("Pstat mở cửa thông", "vent opens at Pstat"), (170, 218))],
        extra=_chart_6_36(),
        courtesy="Fike Metal Products")


@_reg13
def fig_vsh_6_37():
    return _rd_fig(
        37, "Dust-explosion test showing flame propagation through piping",
        "Thử nghiệm nổ bụi cho thấy ngọn lửa lan qua đường ống",
        [(("đám cháy lan ra", "expanding fireball"), (310, 246)),
         (("bụi chưa cháy gặp không khí", "unburned dust meets air"),
          (338, 220)),
         (("ngọn lửa lan trong ống", "flame travels in the duct"),
          (286, 188))],
        panels=[(_flame_test_ops(), 0, 0)],
        sub="Fireball có thể vượt ~4 m xuống dưới và ~15 m ngang / about 4 m down and 15 m across",
        courtesy="Fike Metal Products")


@_reg13
def fig_vsh_6_38():
    return _rd_fig(
        38, "Tubular flame-quenching vent system for flameless dust "
           "explosion pressure relief",
        "Hệ thống thông hơi dạng ống dập ngọn lửa, xả nổ bụi không có lửa",
        [(("tấm thông nổ", "explosion vent panel"), (172, 126)),
         (("ống bẫy lửa", "tubular flame trap"), (172, 86)),
         (("tấm lọc gốm", "ceramic filter mat"), (172, 55)),
         (("khí ra dưới 100 °C", "outlet gas below 100 °C"), (172, 28))],
        panels=[(_vent_system_ops(), 0, 0)],
        sub="1500 °C vào → dưới 100 °C ra; ống dẫn ≤3 m / inlet to outlet; duct no more than 3 m",
        courtesy="Rembe GmbH.")
