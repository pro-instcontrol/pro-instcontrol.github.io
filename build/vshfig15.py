# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 18 — Actuators
(book ch. 8, Figures 8-1 … 8-5).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

The source figures are photographs and mechanical drawings.  They are
redrawn as clean editorial schematics that preserve the working
principle shown in each source figure.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _txt, svg)
from vshfig3 import _emit, _emit_legend

FIGS15 = {}


def _reg15(f):
    FIGS15[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
PANEL_F = "#d9d9d2"
RING_F = "#e6e0d2"
SHAFT_F = "#8c887c"
GREEN_F = "#9bbfd1"
XLEG = 402


def _ell_pts(cx, cy, rx, ry, n=32):
    return [(cx + rx * math.cos(2 * math.pi * i / n),
             cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def _upper_arc(cx, cy, r, a0, a1, n=24):
    """Arc points in screen coordinates; 90 deg is straight up."""
    return [(cx + r * math.cos(math.radians(a)),
             cy - r * math.sin(math.radians(a)))
            for a in (a0 + (a1 - a0) * i / (n - 1) for i in range(n))]


def _fig8(num, ten, tvi, marks, ops=(), panels=(), extra=(), courtesy="", sub=""):
    o2 = []
    _emit(o2, ops)
    for pop, dx, dy in panels:
        _emit(o2, pop, dx=dx, dy=dy)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, 350, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(548, 366, courtesy, 6.2, anchor="end", color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 8-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 8-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _electric_ops():
    o = []
    # control box
    o.append(("poly", [(62, 132), (132, 132), (132, 206), (62, 206)],
              PANEL_F, 1.3, INK, "", True))
    for i, xx in enumerate((78, 94, 110)):
        o.append(("circ", xx, 160, 6, 1.0, INK, "#ffffff"))
        o.append(("line", xx, 166, xx, 184, 1.0, INK, ""))
    o.append(("line", 72, 196, 124, 196, 1.0, GREY, ""))
    # motor body and end cover
    o.append(("poly", [(132, 124), (236, 124), (252, 140), (252, 198),
                       (236, 214), (132, 214)], BODY_F, 1.4, INK, "", True))
    o.append(("poly", [(252, 136), (282, 136), (282, 202), (252, 202)],
              RING_F, 1.2, INK, "", True))
    for yy in (150, 170, 190):
        o.append(("line", 258, yy, 276, yy, 0.9, GREY, ""))
    # handwheel and stem
    o.append(("poly", _ell_pts(186, 70, 78, 20), "none", 2.0, INK, "", False))
    o.append(("poly", _ell_pts(186, 70, 12, 8), RING_F, 1.2, INK, "", True))
    for dx, dy in ((70, 0), (-70, 0), (38, 16), (-38, 16), (38, -16), (-38, -16)):
        o.append(("line", 186, 70, 186 + dx, 70 + dy, 1.0, INK, ""))
    o.append(("line", 186, 78, 186, 126, 3.0, SHAFT_F, ""))
    # gear housing and output
    o.append(("poly", [(146, 214), (226, 214), (214, 258), (158, 258)],
              RING_F, 1.3, INK, "", True))
    o.append(("circ", 186, 236, 20, 1.2, INK, "#ffffff"))
    o.append(("line", 186, 258, 186, 300, 3.2, SHAFT_F, ""))
    o.append(("poly", [(164, 300), (208, 300), (208, 312), (164, 312)],
              PANEL_F, 1.2, INK, "", True))
    o.append(("line", 186, 312, 186, 330, 2.2, SHAFT_F, ""))
    return o


def _scotch_section_ops():
    o = []
    o.append(("poly", [(-72, -46), (72, -46), (72, 46), (-72, 46)],
              BODY_F, 1.3, INK, "", True))
    o.append(("line", -72, -28, 72, -28, 0.8, GREY, ""))
    o.append(("line", -72, 28, 72, 28, 0.8, GREY, ""))
    o.append(("poly", [(-34, -40), (18, -40), (18, 40), (-34, 40)],
              RING_F, 1.2, INK, "", True))
    o.append(("line", 18, 0, 44, 0, 2.0, SHAFT_F, ""))
    o.append(("poly", [(44, -58), (86, -58), (86, 58), (44, 58)],
              PANEL_F, 1.2, INK, "", True))
    o.append(("poly", [(58, -38), (72, -38), (72, 38), (58, 38)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("circ", 65, 0, 10, 1.3, BLUE, "#ffffff"))
    o.append(("line", 65, 0, 100, 0, 2.2, SHAFT_F, ""))
    o.append(("line", -72, -58, -72, 58, 1.3, INK, ""))
    o.append(("line", 72, -58, 72, 58, 1.3, INK, ""))
    return o


def _scotch_exterior_ops():
    o = []
    o.append(("poly", [(-78, -52), (54, -52), (78, -30), (78, 30),
                       (54, 52), (-78, 52)], BODY_F, 1.4, INK, "", True))
    o.append(("poly", [(-54, -38), (36, -38), (54, -18), (54, 18),
                       (36, 38), (-54, 38)], "#ffffff", 0.9, GREY, "", True))
    o.append(("line", 78, 0, 112, 0, 3.0, SHAFT_F, ""))
    o.append(("poly", [(-96, 52), (48, 52), (36, 72), (-84, 72)],
              PANEL_F, 1.2, INK, "", True))
    o.append(("circ", -64, -52, 7, 1.0, INK, "#ffffff"))
    o.append(("circ", 40, -52, 7, 1.0, INK, "#ffffff"))
    return o


def _rack_ops(kind):
    o = []
    o.append(("poly", [(-48, -42), (48, -42), (48, 42), (-48, 42)],
              BODY_F, 1.3, INK, "", True))
    o.append(("circ", 0, 0, 16, 1.3, BLUE, "#ffffff"))
    for i in range(8):
        a = 2 * math.pi * i / 8
        x1, y1 = 13 * math.cos(a), 13 * math.sin(a)
        x2, y2 = 19 * math.cos(a), 19 * math.sin(a)
        o.append(("line", x1, y1, x2, y2, 0.9, INK, ""))
    if kind == "single":
        o.append(("poly", [(-40, -34), (22, -34), (22, -20), (-40, -20)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(-48, -40), (-40, -40), (-40, -14), (-48, -14)],
                  PANEL_F, 1.0, INK, "", True))
    elif kind == "tandem":
        for yy in (-32, 20):
            o.append(("poly", [(-40, yy), (24, yy), (24, yy + 12), (-40, yy + 12)],
                      RING_F, 1.0, INK, "", True))
        o.append(("line", -48, -26, -48, 26, 1.2, GREY, ""))
    else:
        o.append(("poly", [(-40, -34), (24, -34), (24, -20), (-40, -20)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(-24, 20), (40, 20), (40, 34), (-24, 34)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(-48, -40), (-40, -40), (-40, -14), (-48, -14)],
                  PANEL_F, 1.0, INK, "", True))
        o.append(("poly", [(40, 14), (48, 14), (48, 40), (40, 40)],
                  PANEL_F, 1.0, INK, "", True))
    return o


def _cam_ops(flip=False):
    o = []
    o.append(("poly", [(-74, -38), (74, -38), (74, 38), (-74, 38)],
              BODY_F, 1.3, INK, "", True))
    sx = -1 if flip else 1
    o.append(("poly", [(sx * 30 - 24, -32), (sx * 30 + 24, -32),
                       (sx * 30 + 24, 32), (sx * 30 - 24, 32)],
              RING_F, 1.2, INK, "", True))
    o.append(("line", sx * 30, 0, 0, 0, 2.4, SHAFT_F, ""))
    o.append(("circ", 0, 0, 19, 1.3, BLUE, "#ffffff"))
    o.append(("circ", 0, 0, 6, 1.0, INK, "#ffffff"))
    o.append(("line", 0, -38, 0, -54, 1.2, INK, ""))
    o.append(("line", -74, -20, 74, -20, 0.8, GREY, ""))
    o.append(("line", -74, 20, 74, 20, 0.8, GREY, ""))
    return o


def _vane_ops():
    o = []
    cx, cy, r = 190, 270, 128
    arc = _upper_arc(cx, cy, r, 158, 22)
    o.append(("poly", [(cx, cy)] + arc, BODY_F, 1.5, INK, "", True))
    inner = _upper_arc(cx, cy, r - 18, 150, 30)
    o.append(("poly", [(cx, cy)] + inner, "#ffffff", 1.0, GREY, "", True))
    vane = _upper_arc(cx, cy, r - 16, 96, 76)
    o.append(("poly", [(cx, cy)] + vane + [(cx, cy)], GREEN_F,
              1.3, GREEN, "", True))
    o.append(("circ", cx, cy, 18, 1.4, INK, "#ffffff"))
    o.append(("circ", cx, cy, 7, 1.0, INK, "#ffffff"))
    left = _upper_arc(cx, cy, r, 158, 150)
    right = _upper_arc(cx, cy, r, 30, 22)
    o.append(("poly", [(left[0][0] - 12, left[0][1] - 4),
                       (left[0][0] + 12, left[0][1] - 4),
                       (left[-1][0] + 12, left[-1][1] + 4),
                       (left[-1][0] - 12, left[-1][1] + 4)],
              PANEL_F, 1.1, INK, "", True))
    o.append(("poly", [(right[0][0] - 12, right[0][1] - 4),
                       (right[0][0] + 12, right[0][1] - 4),
                       (right[-1][0] + 12, right[-1][1] + 4),
                       (right[-1][0] - 12, right[-1][1] + 4)],
              PANEL_F, 1.1, INK, "", True))
    return o


# ------------------------------------------------------------------- figures
@_reg15
def fig_vsh_8_1():
    return _fig8(
        1, "Three-phase electric actuator with handwheel and output drive",
        "Bộ chấp hành điện ba pha với tay quay và đầu ra truyền động",
        [(("tủ điều khiển", "control box"), (98, 166)),
         (("mô tơ và hộp số", "motor and gearing"), (194, 168)),
         (("tay quay dự phòng", "handwheel for manual operation"), (186, 70)),
         (("trục ra vào van", "output drive to valve"), (186, 278))],
        ops=_electric_ops(),
        courtesy="Rotork, UK")


@_reg15
def fig_vsh_8_2():
    e = [
        _txt(115, 84, "(a) mặt cắt / section", 7.4, color=GREY),
        _txt(280, 84, "(b) dạng ngoài / exterior", 7.4, color=GREY),
    ]
    return _fig8(
        2, "Scotch yoke actuator: section and exterior view",
        "Bộ chấp hành yoke Scotch: mặt cắt và dạng bên ngoài",
        [(("piston", "piston"), (100, 150)),
         (("rãnh yoke", "yoke slot"), (162, 130)),
         (("chốt quay", "rotary pin"), (180, 160)),
         (("thân xi lanh", "cylinder housing"), (305, 162)),
         (("trục ra", "output shaft"), (382, 150))],
        ops=[],
        panels=[(_scotch_section_ops(), 115, 160),
                (_scotch_exterior_ops(), 285, 160)],
        extra=e, courtesy="Rotork, UK",
        sub="Chuyển động tịnh tiến của piston thành quay qua rãnh yoke / piston travel becomes rotation through the yoke slot")


@_reg15
def fig_vsh_8_3():
    extra = [
        _txt(88, 246, "single / đơn", 7.0),
        _txt(190, 246, "tandem / song song", 7.0),
        _txt(292, 246, "dual-opposed / đối lập kép", 6.6),
    ]
    return _fig8(
        3, "Single, tandem and dual-opposed rack-and-pinion actuators",
        "Bộ chấp hành bánh răng–thanh răng: đơn, song song và đối lập kép",
        [(("bánh răng ra", "output pinion"), (88, 162)),
         (("thanh răng", "rack"), (88, 136)),
         (("piston đơn", "single piston"), (52, 136)),
         (("piston đối lập", "opposed pistons"), (330, 136))],
        extra=extra,
        panels=[(_rack_ops("single"), 88, 162),
                (_rack_ops("tandem"), 190, 162),
                (_rack_ops("dual"), 292, 162)],
        sub="Piston hoặc nhiều piston dẫn thanh răng quay bánh răng / one or more pistons drive a rack that turns the pinion")


@_reg15
def fig_vsh_8_4():
    extra = [
        _txt(120, 244, "vị trí 1 / position 1", 6.8, color=GREY),
        _txt(288, 244, "vị trí 2 / position 2", 6.8, color=GREY),
    ]
    return _fig8(
        4, "Double-acting cam actuator with connected pistons",
        "Bộ chấp hành cam tác động kép với các piston liên kết",
        [(("piston", "piston"), (165, 164)),
         (("thanh liên kết", "connecting bars"), (140, 164)),
         (("cam", "cam"), (120, 164)),
         (("trục ra", "output shaft"), (120, 104))],
        extra=extra,
        panels=[(_cam_ops(False), 120, 164),
                (_cam_ops(True), 288, 164)],
        sub="Hai piston liên kết qua cam và trục, tạo mô-men hai chiều / two pistons linked through a cam and shaft")


@_reg15
def fig_vsh_8_5():
    return _fig8(
        5, "Vane actuator for quarter-turn valves",
        "Bộ chấp hành cánh vane cho van quay 90 độ",
        [(("buồng kín", "airtight chamber"), (190, 136)),
         (("cánh vane", "plate vane"), (196, 198)),
         (("trục quay", "rotary shaft"), (190, 270)),
         (("cổng khí", "air ports"), (82, 208))],
        ops=_vane_ops(),
        sub="Khí vào một buồng, thoát buồng kia làm cánh và trục quay 90° / air enters one chamber and exhausts the other to rotate the shaft 90°")
