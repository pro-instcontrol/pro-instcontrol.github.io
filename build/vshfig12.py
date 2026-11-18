# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 15 — Rupture Discs: Construction
(book ch. 6, Figures 6-1 … 6-33).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

The source photographs are redrawn as simplified bilingual vector
cross-sections.  Qualitative charts carry no invented numeric scale.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import RING_F, _emit, _emit_legend

FIGS12 = {}


def _reg12(f):
    FIGS12[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
METAL_F = "#d9d9d2"
GRAPHITE_F = "#6f6f6f"
SEAL_F = "#c9d5c9"
WOOL_F = "#e8e2d0"
SCORE_F = "#8b3a32"
DX, DY = 200, 170
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
        elif k == "dot":
            _, cx, cy, n = op
            out.append(("dot", cx * s + dx, cy * s + dy, n))
        else:
            out.append(op)
    return out


def _arrow(o, x1, y1, x2, y2, color=BLUE, sw=1.6):
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


def _holder_ops(conical=False, exploded=False):
    o = []
    off = -26 if exploded else 0
    o.append(("poly", [(-78, 74 + off), (-78, 104 + off), (78, 104 + off),
                       (78, 74 + off), (34, 74 + off), (34, 58 + off),
                       (-34, 58 + off), (-34, 74 + off)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-78, 18), (-78, 50), (78, 50), (78, 18),
                       (34, 18), (34, 34), (-34, 34), (-34, 18)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-30, 104 + off), (30, 104 + off),
                       (30, 58 + off), (-30, 58 + off)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-30, 34), (30, 34), (30, 18), (-30, 18)],
              "#ffffff", 1.0, INK, "", True))
    for x in (-60, 60):
        o.append(("line", x, 18, x, 104 + off, 1.0, GREY, ""))
        o.append(("circ", x, 18, 3, 0.8, INK, ""))
        o.append(("circ", x, 104 + off, 3, 0.8, INK, ""))
    if conical:
        o.append(("line", -34, 50, -22, 58, 1.3, INK, ""))
        o.append(("line", 34, 50, 22, 58, 1.3, INK, ""))
    return o


def _dome_pts(dome="forward", burst=False, graphite=False):
    if burst:
        return [(-40, 54), (-32, 48), (-20, 42), (-10, 54),
                (0, 34), (10, 54), (20, 42), (32, 48),
                (40, 54), (40, 58), (-40, 58)]
    if dome == "reverse":
        return [(-40, 54), (-30, 62), (-14, 72), (0, 76),
                (14, 72), (30, 62), (40, 54), (40, 58), (-40, 58)]
    if dome == "flat":
        return [(-40, 52), (40, 52), (40, 58), (-40, 58)]
    return [(-40, 54), (-30, 46), (-14, 36), (0, 32),
            (14, 36), (30, 46), (40, 54), (40, 58), (-40, 58)]


def _disc_ops(dome="forward", burst=False, graphite=False, score=None,
              slotted=False, lined=False, cap=False, support=None,
              cut=None, armor=False, bars=False, conical=False,
              exploded=False, flat=False):
    o = _holder_ops(conical=conical, exploded=exploded)
    fill = GRAPHITE_F if graphite else METAL_F
    o.append(("poly", _dome_pts(dome, burst, graphite),
              fill, 1.4, INK, "", True))
    base = 62 if dome == "reverse" else 64
    if burst:
        o.append(("line", 0, 34 if dome != "reverse" else 76,
                  0, 82, 1.0, GREY, "4 3"))
    if score == "cross":
        col = "#ffffff" if graphite else SCORE_F
        if dome == "reverse":
            o.append(("line", -22, 62, 22, 72, 1.4, col, ""))
            o.append(("line", -22, 72, 22, 62, 1.4, col, ""))
        else:
            o.append(("line", -22, 42, 22, 52, 1.4, col, ""))
            o.append(("line", -22, 52, 22, 42, 1.4, col, ""))
    elif score in ("partial", "perforated"):
        col = "#ffffff" if graphite else SCORE_F
        yy = 68 if dome == "reverse" else 48
        o.append(("poly", [(18, yy), (28, yy + 2), (36, yy + 6),
                           (38, yy + 10)], "none", 1.3, col, "", False))
        if score == "perforated":
            for xx in (22, 28, 34):
                o.append(("circ", xx, yy + 3, 1.6, 0.8, col, ""))
    if slotted:
        yy = 52 if dome != "reverse" else 58
        for xx in (-30, 30):
            o.append(("circ", xx, yy, 2.4, 0.9, INK, "#ffffff"))
    if lined:
        o.append(("poly", [(-38, base), (38, base), (38, base + 5),
                           (-38, base + 5)], SEAL_F, 1.0, INK, "", True))
    if cap:
        o.append(("poly", [(-44, 30), (44, 30), (34, 20), (-34, 20)],
                  RING_F, 1.0, INK, "", True))
    if support == "vacuum":
        o.append(("poly", [(-38, base + 8), (38, base + 8),
                           (38, base + 15), (-38, base + 15)],
                  RING_F, 1.0, INK, "", True))
        for xx in (-24, -8, 8, 24):
            o.append(("line", xx, base + 9, xx, base + 14, 1.0, GREY, ""))
    if support == "backpressure":
        o.append(("poly", [(-38, 24), (38, 24), (38, 30), (-38, 30)],
                  RING_F, 1.0, INK, "", True))
        for xx in (-24, -8, 8, 24):
            o.append(("line", xx, 24, xx, 30, 1.0, GREY, ""))
    if cut == "knife":
        for x in (-18, 18):
            o.append(("poly", [(x - 8, 78), (x + 8, 78), (x, 68)],
                      METAL_F, 1.0, INK, "", True))
    if cut == "teeth":
        pts = [(-34, 80)]
        for i in range(9):
            x = -34 + i * 8
            pts.extend([(x + 4, 72), (x + 8, 80)])
        o.append(("poly", pts + [(34, 86), (-34, 86)],
                  METAL_F, 1.0, INK, "", True))
    if bars:
        for x in (-28, 28):
            o.append(("poly", [(x - 5, 56), (x + 5, 56),
                               (x + 5, 70), (x - 5, 70)],
                      METAL_F, 1.0, INK, "", True))
    if armor:
        o.append(("poly", [(-48, 50), (-40, 50), (-40, 62), (-48, 62)],
                  METAL_F, 1.1, INK, "", True))
        o.append(("poly", [(40, 50), (48, 50), (48, 62), (40, 62)],
                  METAL_F, 1.1, INK, "", True))
    if flat:
        o.append(("line", -40, 54, 40, 54, 1.0, GREY, "4 3"))
    o.append(("line", -78, 110, 78, 110, 0.9, GREY, ""))
    _arrow(o, 0, 132, 0, 112)
    return o


def _before_after(before, after):
    return [(_scale_ops(before, 0.55), 105, 185),
            (_scale_ops(after, 0.55), 295, 185)]


def _chart_6_1():
    e = []
    e.append(_line(86, 306, 350, 306, 1.5, color=INK))
    e.append(_line(86, 306, 86, 66, 1.5, color=INK))
    e.append(_txt(218, 334, "Nhiệt độ / temperature →", 8.0, color=INK))
    e.append(_txt(42, 186, "Áp vượt", 8.0, color=INK))
    e.append(_txt(42, 198, "Burst pressure", 6.6, color=GREY))
    curves = [
        ([(96, 268), (140, 250), (190, 220), (240, 176), (300, 112), (338, 78)],
         "#4c6fa8", "Inconel"),
        ([(96, 282), (140, 264), (190, 236), (240, 198), (300, 150), (338, 122)],
         "#8b6f3a", "Stainless steel"),
        ([(96, 292), (140, 280), (190, 262), (240, 238), (300, 208), (338, 186)],
         "#67936a", "Nickel / Monel"),
        ([(96, 298), (140, 292), (190, 284), (240, 272), (300, 252), (338, 236)],
         "#9a5f8c", "Aluminum"),
    ]
    for pts, color, label in curves:
        e.append(_poly(pts, "none", sw=1.8, color=color, close=False))
        e.append(_txt(pts[-1][0] + 6, pts[-1][1], label, 6.6,
                      anchor="start", color=color))
    e.append(_txt(218, 48, "Đường xuân theo vật liệu / qualitative by material",
                  6.8, color=GREY))
    return e


# ------------------------------------------------------ terminology / heat / tension
@_reg12
def fig_vsh_6_1():
    return _rd_fig(
        1, "Temperature/burst-pressure relationship of solid-metal "
           "forward-domed rupture discs in several materials",
        "Quan hệ nhiệt độ/áp vượt của đĩa vòm thuận kim loại rắn ở nhiều vật liệu",
        [(("thép không gỉ", "stainless steel"), (300, 150)),
         (("Inconel", "Inconel"), (300, 112)),
         (("nickel / Monel", "nickel / Monel"), (300, 208)),
         (("nhôm", "aluminum"), (300, 252))],
        extra=_chart_6_1(),
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_2():
    o = _holder_ops()
    o.append(("poly", [(-34, 34), (34, 34), (34, 58), (-34, 58)],
              WOOL_F, 1.0, INK, "", True))
    for i in range(24):
        x = -30 + (i % 8) * 9
        y = 38 + (i // 8) * 7
        o.append(("line", x, y, x + 5, y + 2, 0.8, GREY, ""))
    o.append(("line", -20, 46, 20, 46, 1.2, SCORE_F, "4 3"))
    return _rd_fig(
        2, "Heat shield: holder packed with loose amorphous-silica wool "
           "for graphite rupture discs",
        "Tấm chắn nhiệt: giá đỡ chứa len sợi silica vô định hình rời cho đĩa vỡ graphite",
        [(("len silica rời", "loose silica wool"), (200, 214)),
         (("đĩa graphite", "graphite disc"), (200, 224)),
         (("vỡ sẽ phân mảnh", "fragments on burst"), (200, 238))],
        panels=[(o, DX, DY)],
        sub="Chỉ cho khí khô / dry gases only — không dùng với giá đỡ chân không bị tắc",
        courtesy="IMI Marston")


@_reg12
def fig_vsh_6_3():
    return _rd_fig(
        3, "Solid forward-domed rupture disc before and after bursting "
           "in gas service",
        "Đĩa vỡ vòm thuận kim loại rắn trước và sau khi vỡ trong dịch vụ khí",
        [(("vòm trước khi vỡ", "dome before burst"), (105, 208)),
         (("mỏng tại tâm vòm", "local thinning at dome centre"), (105, 196)),
         (("vỡ và phân mảnh", "burst with fragmentation"), (295, 205))],
        panels=_before_after(_disc_ops("forward"),
                             _disc_ops("forward", burst=True)),
        extra=(_txt(105, 150, "trước / before", 7.2, color=GREY),
               _txt(295, 150, "sau / after", 7.2, color=GREY)),
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_4():
    return _rd_fig(
        4, "Vacuum support for forward-domed discs, opening fully on burst",
        "Giá chống chân không cho đĩa vòm thuận, mở hoàn toàn khi vỡ",
        [(("đĩa vòm thuận", "forward-domed disc"), (200, 224)),
         (("giá chống chân không", "vacuum support"), (200, 275)),
         (("khe hở mở toàn lưu thông", "full opening after burst"), (200, 305))],
        panels=[(_disc_ops("forward", support="vacuum"), DX, DY)],
        courtesy="IMI Marston Ltd.")


@_reg12
def fig_vsh_6_5():
    return _rd_fig(
        5, "Permanent back-pressure support supplementing vacuum support",
        "Giá chống áp ngược cố định bổ sung cho giá chống chân không",
        [(("đĩa vòm thuận", "forward-domed disc"), (200, 224)),
         (("giá chống áp ngược", "permanent back-pressure support"),
          (200, 195)),
         (("giá chống chân không", "vacuum support"), (200, 275))],
        panels=[(_disc_ops("forward", support="backpressure"), DX, DY)],
        courtesy="IMI Palmer Ltd.")


@_reg12
def fig_vsh_6_6():
    o = []
    o.append(("circ", 0, 0, 62, 1.4, INK, METAL_F))
    for r in (18, 32, 46):
        pts = []
        for i in range(37):
            a = 2 * math.pi * i / 36
            rr = r + 4 * math.sin(5 * a)
            pts.append((rr * math.cos(a), rr * math.sin(a)))
        o.append(("poly", pts, "none", 1.0, SCORE_F, "", False))
    return _rd_fig(
        6, "Turtle-backing wrinkle pattern from alternate reverse flexing "
           "and stretch against inadequate support",
        "Vết nhăn lưng rùa do uốn ngược và kéo giãn luân phiên khi giá đỡ không đủ",
        [(("vết nhăn lưng rùa", "turtle-backing wrinkles"), (200, 170)),
         (("uốn ngược luân phiên", "alternate reverse flexing"), (200, 130)),
         (("giá đỡ không đủ", "inadequate support"), (200, 210))],
        panels=[(o, 200, 175)])


@_reg12
def fig_vsh_6_7():
    return _rd_fig(
        7, "Forward-domed rupture disc showing the burst pattern in a "
           "liquid-full system",
        "Đĩa vỡ vòm thuận với dạng vỡ trong hệ thống đầy chất lỏng",
        [(("vỡ ban đầu dạng khe", "initial slit pattern"), (200, 224)),
         (("mở thêm khi áp tăng", "opens further as pressure rises"),
          (200, 196)),
         (("dòng lỏng đầy", "liquid-full service"), (200, 300))],
        panels=[(_disc_ops("forward", burst=True), DX, DY)],
        courtesy="BS&amp;B.")


@_reg12
def fig_vsh_6_8():
    return _rd_fig(
        8, "Low-pressure forward-domed disc with vacuum support and "
           "protective cap",
        "Đĩa vòm thuận áp thấp có giá chống chân không và nắp bảo vệ",
        [(("đĩa mỏng áp thấp", "thin low-pressure disc"), (200, 224)),
         (("nắp bảo vệ", "protective cap"), (200, 190)),
         (("giá chống chân không", "vacuum support"), (200, 275))],
        panels=[(_disc_ops("forward", cap=True, support="vacuum"), DX, DY)],
        courtesy="Rembe GmbH.")


@_reg12
def fig_vsh_6_9():
    return _rd_fig(
        9, "Slotted and lined forward-domed rupture disc, three-layer "
           "construction",
        "Đĩa vỡ vòm thuận có khe và lớp lót, cấu trúc ba lớp",
        [(("lớp vòm có khe", "slotted dome layer"), (200, 220)),
         (("lớp làm kín", "seal layer"), (200, 274)),
         (("giá chống chân không", "vacuum support"), (200, 288))],
        panels=[(_disc_ops("forward", slotted=True, lined=True,
                           support="vacuum"), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Company")


@_reg12
def fig_vsh_6_10():
    return _rd_fig(
        10, "Cross-scored forward-acting rupture disc",
        "Đĩa vỡ tác động thuận có vạch cắt chéo",
        [(("vạch cắt chéo", "cross score"), (200, 218)),
         (("vật liệu dày hơn", "thicker material"), (200, 235)),
         (("mở không phân mảnh", "non-fragmenting opening"), (200, 196))],
        panels=[(_disc_ops("forward", score="cross"), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Company")


@_reg12
def fig_vsh_6_11():
    return _rd_fig(
        11, "Cross-scored forward-domed disc in a holder designed for "
           "polymerization service",
        "Đĩa vòm thuận vạch cắt chéo trong giá đỡ thiết kế cho dịch vụ trùng hợp",
        [(("vạch cắt chéo", "cross score"), (200, 218)),
         (("giá đỡ ít khe hở", "crevice-free holder"), (200, 190)),
         (("tránh tích tụ polymer", "avoids polymer build-up"), (200, 275))],
        panels=[(_disc_ops("forward", score="cross", conical=True), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Company")


@_reg12
def fig_vsh_6_12():
    return _rd_fig(
        12, "Slotted and lined flat rupture disc used as an environmental "
           "seal downstream of pressure relief valves",
        "Đĩa vỡ phẳng có khe và lớp lót dùng làm seal môi trường sau van an toàn xả",
        [(("đĩa phẳng có khe", "slotted flat disc"), (200, 224)),
         (("lớp làm kín", "seal layer"), (200, 272)),
         (("kẹp giữa hai mặt bích", "clamped between flanges"), (200, 190))],
        panels=[(_disc_ops("flat", slotted=True, lined=True), DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_13():
    return _rd_fig(
        13, "Slotted and lined flat rupture disc for overpressure protection "
           "of low-pressure systems",
        "Đĩa vỡ phẳng có khe và lớp lót bảo vệ quá áp cho hệ thống áp thấp",
        [(("đĩa phẳng có khe", "slotted flat disc"), (200, 224)),
         (("chịu chân không đầy đủ", "withstands full vacuum"), (200, 272)),
         (("hệ thống áp thấp", "low-pressure system"), (200, 190))],
        panels=[(_disc_ops("flat", slotted=True, lined=True,
                           support="backpressure"), DX, DY)],
        courtesy="BS&amp;B.")


@_reg12
def fig_vsh_6_14():
    return _rd_fig(
        14, "Exploded view of a reverse-buckling disc with knife blades",
        "Thể hiện tách của đĩa vỡ ngược có dao cắt",
        [(("đĩa vòm ngược", "reverse-buckling dome"), (200, 224)),
         (("dao cắt", "knife blades"), (200, 265)),
         (("chỉ dùng cho khí", "gas service only"), (200, 300))],
        panels=[(_disc_ops("reverse", exploded=True, cut="knife"), DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_15():
    return _rd_fig(
        15, "Reverse-buckling disc with a teeth ring",
        "Đĩa vỡ ngược có vòng răng cắt",
        [(("vòm ngược", "reverse dome"), (200, 224)),
         (("vòng răng cắt", "teeth ring"), (200, 268)),
         (("áp vỡ thấp hơn", "lower burst pressure"), (200, 300))],
        panels=[(_disc_ops("reverse", cut="teeth"), DX, DY)],
        courtesy="BS&amp;B.")


@_reg12
def fig_vsh_6_16():
    return _rd_fig(
        16, "Cross-scored annealed reverse-buckling disc in a prelocked "
           "holder, before and after rupture",
        "Đĩa vỡ ngược ủ mềm vạch cắt chéo trong giá khóa sẵn, trước và sau vỡ",
        [(("vạch cắt chéo mặt lõm", "cross score on concave side"),
          (105, 208)),
         (("cánh vỡ dạng quả cắt", "pie-shaped openings"), (295, 205)),
         (("đế vẫn kẹp chặt", "base held by holder"), (295, 225))],
        panels=_before_after(_disc_ops("reverse", score="cross"),
                             _disc_ops("reverse", score="cross", burst=True)),
        extra=(_txt(105, 150, "trước / before", 7.2, color=GREY),
               _txt(295, 150, "sau / after", 7.2, color=GREY)),
        courtesy="BS&amp;B.")


# --------------------------------------------------- reverse-buckling variants
@_reg12
def fig_vsh_6_17():
    return _rd_fig(
        17, "Reverse-buckling disc with a partial circumferential score line",
        "Đĩa vỡ ngược có vạch cắt ngoại vi một phần",
        [(("vạch cắt ngoại vi", "partial circumferential score"), (200, 216)),
         (("xé dọc vạch cắt", "shears along the score"), (200, 232)),
         (("gập quanh bản lề", "folds around a pivot"), (200, 198))],
        panels=[(_disc_ops("reverse", score="partial"), DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_18():
    return _rd_fig(
        18, "Low-pressure-series reverse-buckling disc with partial "
           "circumferential score",
        "Đĩa vỡ ngược dải áp thấp có vạch cắt ngoại vi một phần",
        [(("vòm mỏng áp thấp", "thin low-pressure dome"), (200, 220)),
         (("vạch cắt một phần", "partial score line"), (200, 214)),
         (("lớp làm kín", "seal layer"), (200, 274))],
        panels=[(_disc_ops("reverse", score="partial", lined=True), DX, DY)],
        courtesy="Fike Metal Products")


@_reg12
def fig_vsh_6_19():
    return _rd_fig(
        19, "Perforated partial score for the lowest burst pressures, "
           "sealed by an energised O-ring",
        "Vạch cắt một phần đục lỗ cho áp vỡ thấp nhất, làm kín bằng O-ring ép chặt",
        [(("vạch cắt đục lỗ", "perforated score"), (200, 214)),
         (("O-ring làm kín", "energised O-ring"), (200, 274)),
         (("áp vỡ cực thấp", "lowest burst pressure"), (200, 300))],
        panels=[(_disc_ops("reverse", score="perforated", lined=True),
                 DX, DY)],
        courtesy="BS&amp;B.")


@_reg12
def fig_vsh_6_20():
    o = _disc_ops("reverse", exploded=True)
    o.append(("poly", [(-38, -22), (-24, -34), (0, -40), (24, -34),
                       (38, -22), (38, -14), (-38, -14)],
              METAL_F, 1.3, INK, "", True))
    o.append(("line", -50, -8, -50, -30, 1.5, INK, ""))
    o.append(("line", 50, -8, 50, -30, 1.5, INK, ""))
    _arrow(o, 0, 12, 0, -12, BLUE)
    return _rd_fig(
        20, "Slip-away reverse-buckling disc expelled from the holder "
           "without rupturing",
        "Đĩa vỡ ngược kiểu trượt ra khỏi giá đỡ khi vòm ngược mà không xé toạc",
        [(("đĩa trượt ra", "slip-away disc"), (200, 138)),
         (("bộ chặn giữ đĩa", "arresting device"), (150, 150)),
         (("không cần mô-men siết đặc biệt", "no special torque"), (200, 290))],
        panels=[(o, DX, DY)],
        courtesy="IMI Marston Ltd.")


@_reg12
def fig_vsh_6_21():
    return _rd_fig(
        21, "Slotted and lined reverse-buckling disc with buckling bars "
           "as the burst-control element",
        "Đĩa vỡ ngược có khe và lớp lót, dùng thanh uốn làm phần tử điều khiển vỡ",
        [(("khe hình răng", "teeth-shaped slot"), (200, 216)),
         (("thanh uốn", "buckling bars"), (200, 240)),
         (("lớp làm kín", "seal layer"), (200, 274))],
        panels=[(_disc_ops("reverse", slotted=True, lined=True, bars=True),
                 DX, DY)],
        courtesy="Rembe GmbH.")


@_reg12
def fig_vsh_6_22():
    o = _disc_ops("forward", slotted=True, score="partial")
    o.append(("poly", [(-36, 82), (-26, 90), (0, 96), (26, 90), (36, 82),
                       (36, 88), (26, 96), (0, 102), (-26, 96), (-36, 88)],
              METAL_F, 1.2, INK, "", True))
    for x in (-18, 18):
        o.append(("poly", [(x - 7, 104), (x + 7, 104), (x, 96)],
                  METAL_F, 1.0, INK, "", True))
    return _rd_fig(
        22, "Two-way rupture disc incorporating buckling bars",
        "Đĩa vỡ hai chiều có thanh uốn",
        [(("đĩa thuận phía trên", "forward-acting upper disc"), (200, 220)),
         (("lớp làm kín PTFE", "PTFE seal layer"), (200, 274)),
         (("thanh uốn chiều ngược", "reverse buckling bars"), (200, 268))],
        panels=[(o, DX, DY)],
        courtesy="Rembe GmbH.")


@_reg12
def fig_vsh_6_23():
    o = _disc_ops("forward", slotted=True, lined=True)
    o.append(("line", -34, 88, 34, 88, 1.2, SCORE_F, ""))
    for x in (-20, 0, 20):
        o.append(("poly", [(x - 6, 96), (x + 6, 96), (x, 88)],
                  METAL_F, 1.0, INK, "", True))
    return _rd_fig(
        23, "Two-way disc with a reverse-acting PTFE member and knife blades",
        "Đĩa vỡ hai chiều có màng PTFE tác động ngược và dao cắt",
        [(("đĩa thuận đục lỗ", "perforated forward disc"), (200, 220)),
         (("màng PTFE tác động ngược", "reverse-acting PTFE disc"),
          (200, 264)),
         (("dao cắt", "knife blades"), (200, 282))],
        panels=[(o, DX, DY)],
        courtesy="Continental Disc Corporation")


# ------------------------------------------------------------- graphite discs
@_reg12
def fig_vsh_6_24():
    return _rd_fig(
        24, "Non-armoured monoblock rupture disc of brittle graphite",
        "Đĩa vỡ graphite giòn dạng khối đơn không gia cố",
        [(("màng graphite giòn", "brittle graphite membrane"), (200, 224)),
         (("không gia cố", "non-armoured"), (200, 190)),
         (("DN 25…DN 600", "DN 25…DN 600"), (200, 300))],
        panels=[(_disc_ops("flat", graphite=True), DX, DY)],
        courtesy="IMI Marston Ltd.")


@_reg12
def fig_vsh_6_25():
    return _rd_fig(
        25, "Monoblock brittle-graphite disc armoured by a bonded steel ring",
        "Đĩa graphite giòn dạng khối đơn được gia cố bằng vòng thép dán kết",
        [(("màng graphite", "graphite membrane"), (200, 224)),
         (("vòng thép gia cố", "bonded steel armor ring"), (160, 225)),
         (("cách ứng suất đường ống", "isolates piping stress"), (200, 190))],
        panels=[(_disc_ops("flat", graphite=True, armor=True), DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_26():
    o = _disc_ops("flat", graphite=True)
    o.append(("poly", [(-38, 82), (38, 82), (38, 90), (-38, 90)],
              GRAPHITE_F, 1.2, INK, "", True))
    return _rd_fig(
        26, "Two-way brittle-graphite rupture disc",
        "Đĩa vỡ graphite giòn hai chiều",
        [(("màng trên", "upper membrane"), (200, 224)),
         (("màng dưới", "lower membrane"), (200, 255)),
         (("tối đa 10 bar mỗi chiều", "10 bar maximum each way"), (200, 300))],
        panels=[(o, DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_27():
    o = _disc_ops("flat", graphite=True, support="backpressure")
    o.append(("poly", [(-44, 60), (-38, 60), (-38, 70), (-44, 70)],
              RING_F, 1.0, INK, "", True))
    o.append(("poly", [(38, 60), (44, 60), (44, 70), (38, 70)],
              RING_F, 1.0, INK, "", True))
    return _rd_fig(
        27, "Replaceable brittle-graphite membrane in a non-torque-"
           "sensitive recessed holder",
        "Màng graphite giòn thay thế được trong giá lõm không nhạy mô-men siết",
        [(("màng thay thế được", "replaceable membrane"), (200, 224)),
         (("lắp trong hốc định sâu", "controlled-depth recess"), (200, 258)),
         (("giá chống áp ngược", "reverse pressure supports"), (200, 192))],
        panels=[(o, DX, DY)],
        courtesy="IMI Marston Ltd.")


@_reg12
def fig_vsh_6_28():
    return _rd_fig(
        28, "Reverse-buckling rupture disc made of pure graphite",
        "Đĩa vỡ ngược làm bằng graphite nguyên chất",
        [(("graphite nguyên chất", "pure graphite"), (200, 224)),
         (("vòm ngược dày", "thick reverse dome"), (200, 200)),
         (("chịu ~550 °C", "about 550 °C service"), (200, 300))],
        panels=[(_disc_ops("reverse", graphite=True, score="cross"),
                 DX, DY)],
        courtesy="IMI Marston Ltd.")


# ------------------------------------------------------- holders and assemblies
@_reg12
def fig_vsh_6_29():
    o = _disc_ops("forward", exploded=True, conical=True)
    o.append(("line", -34, 50, -22, 58, 1.0, SCORE_F, ""))
    o.append(("line", 34, 50, 22, 58, 1.0, SCORE_F, ""))
    return _rd_fig(
        29, "Exploded holder for solid-metal forward-domed rupture discs "
           "with a 30-degree conical seat",
        "Thể hiện tách giá đỡ đĩa vòm thuận kim loại rắn với đế côn 30 độ",
        [(("đế côn 30°", "30-degree conical seat"), (200, 218)),
         (("vòng gia cố mép đĩa", "stiffening ring"), (200, 274)),
         (("tuân mô-men nhà chế tạo", "follow maker torque"), (200, 300))],
        panels=[(o, DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_30():
    o = []
    o.append(("poly", [(-90, 40), (-30, 40), (-30, 20), (30, 20),
                       (30, 40), (90, 40), (90, 90), (-90, 90)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-90, 52), (90, 52), (90, 78), (-90, 78)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-28, 20), (28, 20), (28, -46), (-28, -46)],
              BODY_F, 1.2, INK, "", True))
    o.append(("poly", [(-20, -46), (20, -46), (20, 20), (-20, 20)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-26, -20), (26, -20), (26, -12), (-26, -12)],
              METAL_F, 1.2, INK, "", True))
    _arrow(o, -86, 65, -52, 65)
    _arrow(o, 52, 65, 86, 65)
    _arrow(o, 0, -40, 0, -24, GREY)
    return _rd_fig(
        30, "Clean-sweep viscous-Tee assembly incorporating a forward-domed "
           "rupture disc",
        "Cụm quét sạch dạng T nhớt có đĩa vỡ vòm thuận",
        [(("đường quét ngang", "sweeping main passage"), (200, 235)),
         (("đĩa vỡ nhánh trên", "disc in upper branch"), (200, 150)),
         (("giảm tích tụ chất nhớt", "reduces viscous build-up"), (200, 295))],
        panels=[(o, DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_31():
    o = []
    o.append(("poly", [(-88, 20), (88, 20), (88, 100), (-88, 100)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-70, 100), (-30, 100), (-30, 40), (-70, 40)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(30, 100), (70, 100), (70, 40), (30, 40)],
              "#ffffff", 1.0, INK, "", True))
    for x in (-50, 50):
        o.append(("poly", [(x - 14, 68), (x + 14, 68),
                           (x + 14, 76), (x - 14, 76)],
                  METAL_F, 1.2, INK, "", True))
        o.append(("circ", x - 18, 72, 3, 0.9, INK, SEAL_F))
        o.append(("circ", x + 18, 72, 3, 0.9, INK, SEAL_F))
    o.append(("line", 0, 40, 0, 112, 2.0, INK, ""))
    o.append(("line", 0, 112, 44, 128, 2.0, INK, ""))
    _arrow(o, 0, 140, 0, 114, BLUE)
    return _rd_fig(
        31, "Manually changed quick-change rupture-disc housing",
        "Vỏ đĩa vỡ thay nhanh vận hành bằng tay",
        [(("hai vị trí đĩa", "two disc stations"), (150, 242)),
         (("O-ring làm kín", "O-ring seals"), (232, 242)),
         (("cần chuyển bằng tay", "manual change-over lever"), (244, 298))],
        panels=[(o, DX, DY)])


@_reg12
def fig_vsh_6_32():
    o = []
    o.append(("poly", [(-92, 24), (92, 24), (92, 104), (-92, 104)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-72, 104), (-28, 104), (-28, 44), (-72, 44)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(28, 104), (72, 104), (72, 44), (28, 44)],
              "#ffffff", 1.0, INK, "", True))
    for x in (-50, 50):
        o.append(("poly", [(x - 14, 70), (x + 14, 70),
                           (x + 14, 78), (x - 14, 78)],
                  METAL_F, 1.2, INK, "", True))
        o.append(("circ", x - 18, 74, 3, 0.9, INK, SEAL_F))
        o.append(("circ", x + 18, 74, 3, 0.9, INK, SEAL_F))
    o.append(("poly", [(-26, -18), (26, -18), (26, 16), (-26, 16)],
              RING_F, 1.1, INK, "", True))
    o.append(("line", -14, -18, 14, 16, 1.0, INK, ""))
    o.append(("line", 14, -18, -14, 16, 1.0, INK, ""))
    o.append(("line", 0, 16, 0, 24, 2.0, INK, ""))
    _arrow(o, 0, 140, 0, 112, BLUE)
    return _rd_fig(
        32, "Pneumatically operated sliding-gate quick-change housing",
        "Vỏ đĩa vỡ thay nhanh dạng cổng trượt điều khiển bằng khí nén",
        [(("cổng trượt", "sliding gate"), (200, 240)),
         (("cơ cấu khí nén", "pneumatic actuator"), (200, 182)),
         (("liên khóa bằng O-ring", "O-ring pressure interlock"), (268, 259))],
        panels=[(o, DX, DY)],
        courtesy="Continental Disc Corporation")


@_reg12
def fig_vsh_6_33():
    o = []
    o.append(("poly", [(-44, 24), (-44, 128), (44, 128), (44, 24),
                       (30, 24), (30, 36), (-30, 36), (-30, 24)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-30, 128), (30, 128), (30, 40), (-30, 40)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-34, 64), (34, 64), (34, 72), (-34, 72)],
              METAL_F, 1.2, INK, "", True))
    o.append(("poly", [(-34, 98), (34, 98), (34, 106), (-34, 106)],
              METAL_F, 1.2, INK, "", True))
    o.append(("poly", [(44, 76), (88, 76), (88, 92), (44, 92)],
              BODY_F, 1.1, INK, "", True))
    o.append(("circ", 104, 84, 14, 1.2, INK, "#ffffff"))
    o.append(("line", 104, 84, 110, 76, 1.0, INK, ""))
    o.append(("poly", [(70, 108), (90, 108), (90, 126), (50, 126)],
              METAL_F, 1.1, INK, "", True))
    _arrow(o, 0, 146, 0, 128)
    return _rd_fig(
        33, "Double disc assembly with pressure gauge and excess-flow "
           "valve as product-leakage warning devices",
        "Cụm hai đĩa có đồng hồ áp và van dòng vượt làm tín hiệu báo rò sản phẩm",
        [(("đĩa phía sản phẩm", "process-side disc"), (200, 268)),
         (("đĩa thứ hai", "second disc"), (200, 234)),
         (("đồng hồ áp", "pressure gauge"), (304, 254)),
         (("van dòng vượt", "excess-flow valve"), (260, 296))],
        panels=[(o, DX, DY)],
        courtesy="Sempell A.G.")
