# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 19 — Double Block and Bleed Ball
Valves (book ch. 9, Figures 9-1 … 9-2).  Each function returns the
standard 5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

The source figures are photographs and engineering drawings.  They are
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

FIGS16 = {}


def _reg16(f):
    FIGS16[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
PANEL_F = "#d9d9d2"
RING_F = "#e6e0d2"
SHAFT_F = "#8c887c"
FLOW_F = "#9bbfd1"
XLEG = 402


def _ell_pts(cx, cy, rx, ry, n=32):
    return [(cx + rx * math.cos(2 * math.pi * i / n),
             cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def _fig9(num, ten, tvi, marks, ops=(), extra=(), courtesy="", sub=""):
    o2 = []
    _emit(o2, ops)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, 350, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(548, 366, courtesy, 6.2, anchor="end", color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 9-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 9-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _ball_valve_body(cx, cy, w=64, h=44, open_=True):
    """One inline ball symbol: body with ball and bore."""
    o = []
    o.append(("poly", [(cx - w, cy - h), (cx + w, cy - h), (cx + w, cy + h),
                       (cx - w, cy + h)], BODY_F, 1.3, INK, "", True))
    o.append(("circ", cx, cy, 20, 1.3, INK, "#ffffff"))
    if open_:
        o.append(("poly", [(cx - 14, cy - 7), (cx + 14, cy - 7),
                           (cx + 14, cy + 7), (cx - 14, cy + 7)],
                  FLOW_F, 1.0, INK, "", True))
    else:
        o.append(("line", cx - 14, cy, cx + 14, cy, 1.4, INK, ""))
    return o


def _lever(cx, cy, ang=30, ln=34):
    """Lever handle from valve stem; ang in degrees, 0 = horizontal."""
    x2 = cx + ln * math.cos(math.radians(ang))
    y2 = cy - ln * math.sin(math.radians(ang))
    return [("circ", cx, cy, 5, 1.2, INK, "#ffffff"),
            ("line", cx, cy, x2, y2, 2.4, SHAFT_F, ""),
            ("circ", x2, y2, 3.4, 1.1, INK, "#ffffff")]


@_reg16
def fig_vsh_9_1():
    """Figure 9-1 — instrument DBB, top entry (exterior + section)."""
    ten = ("Instrument double block and bleed ball valve, top entry — "
           "exterior and section")
    tvi = ("Van bi chặn kép và xả dùng cho thiết bị đo, entry phía trên — "
           "ngoại hình và mặt cắt")
    ops = []
    # ---- exterior view (upper) -------------------------------------
    ex, ey = 190, 110
    # body barrel
    ops.append(("poly", _ell_pts(ex, ey, 92, 34), BODY_F, 1.5, INK, "", True))
    ops.append(("poly", _ell_pts(ex - 92, ey, 16, 34), RING_F, 1.3, INK, "",
                True))
    ops.append(("poly", _ell_pts(ex + 92, ey, 16, 34), RING_F, 1.3, INK, "",
                True))
    ops.append(("line", ex - 108, ey - 26, ex - 108, ey + 26, 1.6, INK, ""))
    ops.append(("line", ex + 108, ey - 26, ex + 108, ey + 26, 1.6, INK, ""))
    # top-entry bleed needle valve with handwheel
    ops.append(("line", ex - 20, ey - 34, ex - 20, ey - 58, 2.0, SHAFT_F, ""))
    ops.append(("poly", _ell_pts(ex - 20, ey - 66, 22, 7), "none", 1.6, INK,
                "", False))
    ops.append(("line", ex - 20, ey - 58, ex - 20, ey - 66, 1.4, INK, ""))
    ops.append(("poly", [(ex - 26, ey - 34), (ex - 14, ey - 34),
                         (ex - 10, ey - 46), (ex - 30, ey - 46)],
                RING_F, 1.1, INK, "", True))
    # two lever handles (isolation balls)
    ops.extend(_lever(ex - 58, ey - 12, 40))
    ops.extend(_lever(ex + 64, ey - 12, -20))
    # drain connection below
    ops.append(("line", ex + 20, ey + 34, ex + 20, ey + 52, 1.6, INK, ""))
    ops.append(("poly", [(ex + 14, ey + 52), (ex + 26, ey + 52)],
                "none", 1.2, INK, "", False))
    # ---- section view (lower) --------------------------------------
    sy = 258
    for dx in (-78, 78):
        ops.extend(_ball_valve_body(200 + dx, sy, w=52, h=36, open_=True))
    # flow bore
    ops.append(("line", 30, sy, 148, sy, 1.6, GREY, ""))
    ops.append(("line", 252, sy, 370, sy, 1.6, GREY, ""))
    # central bleed tee up to needle valve
    ops.append(("line", 200, sy, 200, sy - 44, 1.6, INK, ""))
    ops.append(("poly", [(186, sy - 44), (214, sy - 44), (206, sy - 62),
                         (194, sy - 62)], RING_F, 1.2, INK, "", True))
    ops.append(("line", 200, sy - 62, 200, sy - 78, 1.6, INK, ""))
    ops.append(("line", 188, sy - 78, 212, sy - 78, 2.0, SHAFT_F, ""))
    # interconnecting channel between the two balls
    ops.append(("line", 148, sy + 16, 252, sy + 16, 1.0, GREY, "4,4"))
    ops.append(("line", 148, sy + 22, 252, sy + 22, 1.0, GREY, "4,4"))
    extra = [
        _txt(58, 30, "Ngoại hình / exterior", 7.0, color=GREY),
        _txt(30, 190, "Mặt cắt / section", 7.0, color=GREY),
        _txt(30, sy - 16, "từ quá trình", 6.5, color=GREY),
        _txt(370, sy - 16, "từ quá trình", 6.5, color=GREY, anchor="end"),
    ]
    marks = [
        (("hai bi cách ly", "two isolation balls"), (252, 258)),
        (("van xả kim", "bleed needle valve"), (200, 204)),
        (("tay nắm bán nguyệt", "quarter-turn levers"), (132, 82)),
        (("bánh tay van xả", "bleed handwheel"), (140, 44)),
        (("kênh xả giữa hai bi", "interball bleed channel"), (252, 282)),
    ]
    return _fig9(1, ten, tvi, marks, ops=ops, extra=extra,
                 courtesy="Orsenigo, Italy")


@_reg16
def fig_vsh_9_2():
    """Figure 9-2 — in-line DBB, trunnion mounted side entry."""
    ten = ("In-line double block and bleed ball valve, 4 in 900 class, "
           "trunnion mounted side entry — section")
    tvi = ("Van bi chặn kép và xả đặt trong đường ống, 4 in lớp 900, "
           "bi gắn trục quay (trunnion), entry bên — mặt cắt")
    ops = []
    sy = 210
    # flow bore through the body
    ops.append(("poly", [(30, sy - 46), (368, sy - 46), (368, sy + 46),
                         (30, sy + 46)], BODY_F, 1.6, INK, "", True))
    ops.append(("line", 30, sy - 30, 368, sy - 30, 0.8, GREY, ""))
    ops.append(("line", 30, sy + 30, 368, sy + 30, 0.8, GREY, ""))
    # flanges
    for fx in (34, 364):
        ops.append(("poly", [(fx - 8, sy - 62), (fx + 8, sy - 62),
                             (fx + 8, sy + 62), (fx - 8, sy + 62)],
                    RING_F, 1.4, INK, "", True))
    # two trunnion balls in series
    for cx in (136, 264):
        ops.append(("circ", cx, sy, 26, 1.5, INK, "#ffffff"))
        ops.append(("poly", [(cx - 17, sy - 8), (cx + 17, sy - 8),
                             (cx + 17, sy + 8), (cx - 17, sy + 8)],
                    FLOW_F, 1.0, INK, "", True))
        # side-entry stem
        ops.append(("line", cx, sy - 26, cx, sy - 62, 2.4, SHAFT_F, ""))
        ops.append(("poly", [(cx - 15, sy - 62), (cx + 15, sy - 62),
                             (cx + 15, sy - 76), (cx - 15, sy - 76)],
                    PANEL_F, 1.2, INK, "", True))
        # trunnions below
        ops.append(("line", cx - 10, sy + 26, cx - 10, sy + 36, 1.6, INK, ""))
        ops.append(("line", cx + 10, sy + 26, cx + 10, sy + 36, 1.6, INK, ""))
    # bleed valve between the two balls, from the interball cavity
    ops.append(("line", 200, sy + 30, 200, sy + 74, 1.8, INK, ""))
    ops.append(("poly", [(188, sy + 74), (212, sy + 74), (206, sy + 92),
                         (194, sy + 92)], RING_F, 1.2, INK, "", True))
    ops.append(("line", 200, sy + 92, 200, sy + 106, 1.6, INK, ""))
    ops.append(("line", 190, sy + 106, 210, sy + 106, 2.0, SHAFT_F, ""))
    # interball cavity hatch
    ops.append(("line", 168, sy + 38, 188, sy + 38, 0.9, GREY, "4,4"))
    ops.append(("line", 212, sy + 38, 232, sy + 38, 0.9, GREY, "4,4"))
    extra = [
        _txt(34, sy - 60, "áp vào", 7.0, color=GREY),
        _txt(364, sy - 60, "áp ra", 7.0, color=GREY, anchor="end"),
        _txt(200, 374, "điểm xả giữa hai bi có thể kiểm tra độ kín từng bi",
             6.8, color=GREY),
    ]
    marks = [
        (("bi 1 gắn trunnion", "trunnion ball 1"), (136, 210)),
        (("bi 2 gắn trunnion", "trunnion ball 2"), (264, 210)),
        (("cavity giữa hai bi", "interball cavity"), (200, 250)),
        (("van xả kim", "bleed needle valve"), (200, 300)),
        (("trục entry bên", "side-entry stems"), (136, 140)),
        (("mặt bích ANSI B16.5", "ANSI B16.5 flanges"), (30, 148)),
    ]
    return _fig9(2, ten, tvi, marks, ops=ops, extra=extra,
                 courtesy="Orsenigo, Italy")


@_reg16
def fig_vsh_9_3():
    """Figure 9-3 — DBB functions: injection quill and sampling."""
    ten = "DBB service functions — chemical injection and sampling quill"
    tvi = ("Các chức năng phục vụ của DBB — phun hóa chất và lấy mẫu "
           "bằng ống quill")
    ops = []
    sy = 170
    # process pipe
    ops.append(("poly", [(30, sy - 26), (360, sy - 26), (360, sy + 26),
                         (30, sy + 26)], BODY_F, 1.5, INK, "", True))
    ops.append(("line", 30, sy, 360, sy, 1.0, GREY, ""))
    # mating flange with quill entering the flow
    ops.append(("poly", [(200, sy - 40), (216, sy - 40), (216, sy + 40),
                         (200, sy + 40)], RING_F, 1.3, INK, "", True))
    # vertical quill tube
    ops.append(("line", 208, sy - 26, 208, sy - 70, 1.6, INK, ""))
    # compact DBB valve on top of the quill
    ops.append(("poly", [(178, sy - 70), (238, sy - 70), (238, sy - 108),
                         (178, sy - 108)], PANEL_F, 1.4, INK, "", True))
    ops.extend(_ball_valve_body(194, sy - 89, w=18, h=14, open_=True))
    ops.extend(_ball_valve_body(222, sy - 89, w=18, h=14, open_=True))
    ops.append(("circ", 208, sy - 116, 8, 1.3, INK, "#ffffff"))
    # chemical source with in-line poppet check
    ops.append(("line", 208, sy - 140, 208, sy - 124, 1.4, INK, ""))
    ops.append(("line", 198, sy - 132, 218, sy - 132, 1.2, BLUE, ""))
    ops.append(("poly", [(202, sy - 124), (214, sy - 124), (208, sy - 118)],
                INK, 1.0, INK, "", True))
    # sample bottle at the side outlet
    ops.append(("line", 238, sy - 89, 282, sy - 89, 1.6, INK, ""))
    ops.append(("line", 282, sy - 89, 282, sy - 64, 1.6, INK, ""))
    ops.append(("poly", [(270, sy - 64), (294, sy - 64), (294, sy - 38),
                         (270, sy - 38)], "none", 1.4, INK, "", False))
    extra = [
        _txt(318, 60, "chai lấy mẫu / sample bottle", 6.8, color=GREY),
        _txt(330, 208, "mặt bích ghép + ống quill vào dòng chảy", 6.8,
             color=GREY, anchor="end"),
    ]
    marks = [
        (("DBB cỡ nhỏ", "compact DBB"), (170, 66)),
        (("hai bi cách ly", "two isolation balls"), (222, 81)),
        (("van một chiều poppet", "in-line poppet check"), (244, 38)),
        (("nguồn hóa chất", "chemical source"), (168, 28)),
        (("ống quill vào quá trình", "quill into the process"), (152, 144)),
    ]
    return _fig9(3, ten, tvi, marks, ops=ops, extra=extra)
