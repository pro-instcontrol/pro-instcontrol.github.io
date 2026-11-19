# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 20 — Mechanical Locking Devices for
Valves (book ch. 10, Figures 10-1 … 10-8).  Each function returns the
standard 5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

The source figures are photographs and schematics.  They are redrawn as
clean editorial diagrams that preserve the working principle shown in
each source figure.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _txt, svg)
from vshfig3 import _emit, _emit_legend

FIGS17 = {}


def _reg17(f):
    FIGS17[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
PANEL_F = "#d9d9d2"
RING_F = "#e6e0d2"
SHAFT_F = "#8c887c"
LOCK_F = "#d9b23a"
XLEG = 402


def _fig10(num, ten, tvi, marks, ops=(), extra=(), courtesy="", sub=""):
    o2 = []
    _emit(o2, ops)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, 352, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(548, 366, courtesy, 6.2, anchor="end", color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 10-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 10-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _wire_seal(x1, y1, x2, y2, lead_x=None, lead_y=None):
    """Twisted wire through a bolt hole plus optional lead blob."""
    o = [("line", x1, y1, x2, y2, 1.2, INK, "")]
    if lead_x is not None:
        o.append(("circ", lead_x, lead_y, 3.2, 1.0, SHAFT_F, "#ffffff"))
    return o


def _padlock(cx, cy, s=10):
    """Padlock: shackle arc plus body."""
    o = []
    pts = [(cx - s * 0.55, cy),
           (cx - s * 0.55, cy - s * 0.9),
           (cx + s * 0.55, cy - s * 0.9),
           (cx + s * 0.55, cy)]
    o.append(("poly", pts, "none", 1.2, INK, "", False))
    o.append(("poly", [(cx - s, cy), (cx + s, cy), (cx + s, cy + s * 1.3),
                       (cx - s, cy + s * 1.3)], LOCK_F, 1.2, INK, "", True))
    o.append(("circ", cx, cy + s * 0.55, s * 0.22, 0.9, INK, "#ffffff"))
    return o


def _chain(x1, y1, x2, y2, n=7):
    o = []
    for i in range(n):
        t = (i + 0.5) / n
        cx = x1 + (x2 - x1) * t
        cy = y1 + (y2 - y1) * t
        o.append(("circ", cx, cy, 2.6, 1.0, SHAFT_F, "none"))
    o.append(("line", x1, y1, x2, y2, 0.7, GREY, ""))
    return o


def _handwheel(cx, cy, rx=40, ry=12):
    n = 28
    pts = [(cx - rx + 2 * rx * i / n, cy - ry * math.sin(math.pi * i / n))
           for i in range(n + 1)]
    pts += [(cx + rx - 2 * rx * i / n, cy + ry * math.sin(math.pi * i / n))
            for i in range(n + 1)]
    o = [("poly", pts, "none", 1.6, INK, "", False)]
    o.append(("circ", cx, cy, 5, 1.1, INK, "#ffffff"))
    return o


def _gearbox(cx, cy, w=44, h=30):
    o = [("poly", [(cx - w, cy - h), (cx + w, cy - h), (cx + w, cy + h),
                   (cx - w, cy + h)], PANEL_F, 1.3, INK, "", True)]
    o.append(("line", cx - w, cy, cx + w, cy, 0.8, GREY, ""))
    o.append(("circ", cx + w * 0.45, cy - h * 0.35, 4, 1.0, INK, "#ffffff"))
    return o


def _lock_house(cx, cy, w=56, h=30):
    """Mechanical locking device housing with two key slots."""
    o = [("poly", [(cx - w, cy - h), (cx + w, cy - h), (cx + w, cy + h),
                   (cx - w, cy + h)], LOCK_F, 1.4, INK, "", True)]
    o.append(("poly", [(cx - w * 0.55, cy - h * 0.45),
                       (cx - w * 0.15, cy - h * 0.45),
                       (cx - w * 0.15, cy + h * 0.45),
                       (cx - w * 0.55, cy + h * 0.45)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(cx + w * 0.15, cy - h * 0.45),
                       (cx + w * 0.55, cy - h * 0.45),
                       (cx + w * 0.55, cy + h * 0.45),
                       (cx + w * 0.15, cy + h * 0.45)],
              "#ffffff", 1.0, INK, "", True))
    return o


@_reg17
def fig_vsh_10_1():
    """Figure 10-1 — wire on gearbox handwheel with independent padlock."""
    ten = "Wire seal on gearbox handwheel with independent padlock"
    tvi = "Dây chì ở tay quay hộp số với khóa padlock độc lập"
    ops = []
    gx, gy = 200, 130
    ops.extend(_gearbox(gx, gy, 62, 36))
    ops.append(("line", gx, gy - 36, gx, gy - 66, 2.4, SHAFT_F, ""))
    ops.extend(_handwheel(gx, gy - 78, 58, 14))
    # wire through bolt hole on the gearbox and through handwheel spoke
    ops.extend(_wire_seal(gx - 40, gy + 8, gx - 88, gy - 66, gx - 88, gy - 66))
    ops.append(("circ", gx - 40, gy + 8, 3.4, 1.0, INK, "#ffffff"))
    # independent padlock hanging on the loop
    ops.extend(_padlock(gx - 88, gy - 46, 11))
    extra = [_txt(200, 320, "dây xoắn hai đầu, đầu chì chặn tay lười biếng",
                  6.8, color=GREY)]
    marks = [
        (("hộp số van", "valve gearbox"), (200, 130)),
        (("tay quay", "handwheel"), (200, 52)),
        (("lỗ bu-lông luồn dây", "bolt hole for wire"), (160, 138)),
        (("dây xoắn", "twisted wire"), (112, 92)),
        (("padlock độc lập", "independent padlock"), (112, 46)),
    ]
    return _fig10(1, ten, tvi, marks, ops=ops, extra=extra,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_2():
    """Figure 10-2 — wire on globe valve handwheel."""
    ten = "Wire seal on globe valve handwheel with independent padlock"
    tvi = "Dây chì ở tay quay van cầu với khóa padlock độc lập"
    ops = []
    # globe valve body
    ops.append(("poly", [(150, 190), (250, 190), (250, 262), (150, 262)],
                BODY_F, 1.4, INK, "", True))
    ops.append(("poly", [(150, 210), (120, 190), (120, 262), (150, 242)],
                RING_F, 1.2, INK, "", True))
    ops.append(("poly", [(250, 210), (280, 190), (280, 262), (250, 242)],
                RING_F, 1.2, INK, "", True))
    ops.append(("line", 60, 226, 120, 226, 1.6, GREY, ""))
    ops.append(("line", 280, 226, 340, 226, 1.6, GREY, ""))
    # bonnet and stem
    ops.append(("poly", [(184, 190), (216, 190), (216, 150), (184, 150)],
                PANEL_F, 1.3, INK, "", True))
    ops.append(("line", 200, 150, 200, 118, 2.2, SHAFT_F, ""))
    ops.extend(_handwheel(200, 106, 52, 12))
    # wire through the handwheel rim and a bolted eyelet on the bonnet
    ops.extend(_wire_seal(248, 106, 288, 60, 288, 60))
    ops.append(("circ", 252, 150, 3.2, 1.0, INK, "#ffffff"))
    ops.append(("line", 252, 150, 288, 60, 1.0, INK, ""))
    ops.extend(_padlock(288, 78, 11))
    extra = [_txt(200, 320, "dây luồn qua vành tay quay và mắt bu-lông trên "
                  "nắp van", 6.8, color=GREY)]
    marks = [
        (("tay quay van cầu", "globe handwheel"), (200, 106)),
        (("dây chì", "sealing wire"), (268, 84)),
        (("mắt bu-lông trên nắp", "eyelet on the bonnet"), (252, 150)),
        (("padlock độc lập", "independent padlock"), (288, 74)),
        (("thân van cầu", "globe body"), (200, 226)),
    ]
    return _fig10(2, ten, tvi, marks, ops=ops, extra=extra,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_3():
    """Figure 10-3 — key cabinet in the control room."""
    ten = "Key cabinet in the control room for spare interlock keys"
    tvi = "Tủ chìa khóa trong phòng điều khiển dùng cho các chìa dự phòng"
    ops = []
    # cabinet
    ops.append(("poly", [(70, 60), (330, 60), (330, 300), (70, 300)],
                PANEL_F, 1.5, INK, "", True))
    ops.append(("line", 200, 60, 200, 300, 1.2, INK, ""))
    # two doors with key boards
    for dx in (70, 200):
        cx = dx + 65
        ops.append(("poly", [(dx + 12, 84), (dx + 118, 84), (dx + 118, 200),
                             (dx + 12, 200)], "#ffffff", 1.0, GREY, "", True))
        for i, (kx, ky) in enumerate(((cx - 24, 110), (cx + 24, 110),
                                      (cx - 24, 150), (cx + 24, 150))):
            ops.append(("circ", kx, ky, 8, 1.1, INK, "#ffffff"))
            ops.append(("line", kx, ky + 8, kx, ky + 22, 1.6, SHAFT_F, ""))
        # key hanging below the board
        ops.append(("circ", cx, 238, 9, 1.2, LOCK_F, "#ffffff"))
        ops.append(("line", cx, 247, cx, 262, 1.8, SHAFT_F, ""))
        ops.append(("poly", [(cx - 7, 262), (cx + 7, 262), (cx + 5, 274),
                             (cx - 5, 274)], LOCK_F, 1.2, INK, "", True))
    extra = [_txt(200, 330, "chìa rỗi luôn nằm trong tủ hoặc trên một van",
                  6.8, color=GREY)]
    marks = [
        (("tủ chìa hai cửa", "two-door key cabinet"), (200, 90)),
        (("bảng treo chìa", "key board"), (135, 128)),
        (("chìa đồng bộ khóa", "dedicated lock keys"), (135, 240)),
        (("chìa dự phòng", "spare key retained"), (265, 240)),
        (("phòng điều khiển", "control room"), (330, 300)),
    ]
    return _fig10(3, ten, tvi, marks, ops=ops, extra=extra,
                  courtesy="Netherlocks, Holland")


def _locked_valve(kind):
    """Gate / ball / butterfly valve with a locking device on top works."""
    o = []
    cx, cy = 200, 236
    if kind == "gate":
        o.append(("poly", [(cx - 46, cy - 30), (cx + 46, cy - 30),
                           (cx + 46, cy + 30), (cx - 46, cy + 30)],
                  BODY_F, 1.4, INK, "", True))
        o.append(("poly", [(cx - 46, cy), (cx - 74, cy - 22), (cx - 74, cy + 22),
                           (cx - 46, cy)], RING_F, 1.2, INK, "", True))
        o.append(("poly", [(cx + 46, cy), (cx + 74, cy - 22), (cx + 74, cy + 22),
                           (cx + 46, cy)], RING_F, 1.2, INK, "", True))
        o.append(("line", 60, cy, cx - 74, cy, 1.5, GREY, ""))
        o.append(("line", cx + 74, cy, 340, cy, 1.5, GREY, ""))
        o.append(("line", cx, cy - 30, cx, cy - 78, 2.2, SHAFT_F, ""))
        o.extend(_handwheel(cx, cy - 92, 44, 11))
    elif kind == "ball":
        o.append(("poly", [(cx - 42, cy - 30), (cx + 42, cy - 30),
                           (cx + 42, cy + 30), (cx - 42, cy + 30)],
                  BODY_F, 1.4, INK, "", True))
        o.append(("circ", cx, cy, 18, 1.3, INK, "#ffffff"))
        o.append(("poly", [(cx - 12, cy - 6), (cx + 12, cy - 6),
                           (cx + 12, cy + 6), (cx - 12, cy + 6)],
                  "#9bbfd1", 1.0, INK, "", True))
        o.append(("line", 60, cy, cx - 42, cy, 1.5, GREY, ""))
        o.append(("line", cx + 42, cy, 340, cy, 1.5, GREY, ""))
        o.append(("line", cx, cy - 30, cx, cy - 66, 2.2, SHAFT_F, ""))
        o.append(("line", cx - 26, cy - 66, cx + 26, cy - 66, 3.0, SHAFT_F, ""))
    else:  # butterfly
        o.append(("poly", [(cx - 30, cy - 34), (cx + 30, cy - 34),
                           (cx + 30, cy + 34), (cx - 30, cy + 34)],
                  RING_F, 1.4, INK, "", True))
        o.append(("line", cx, cy - 34, cx, cy + 34, 2.0, SHAFT_F, ""))
        o.append(("poly", [(cx, cy - 24), (cx + 24, cy), (cx, cy + 24)],
                  "#9bbfd1", 1.2, INK, "", True))
        o.append(("line", 60, cy, cx - 30, cy, 1.5, GREY, ""))
        o.append(("line", cx + 30, cy, 340, cy, 1.5, GREY, ""))
        o.append(("line", cx, cy - 34, cx, cy - 66, 2.2, SHAFT_F, ""))
        o.append(("line", cx - 26, cy - 66, cx + 26, cy - 66, 3.0, SHAFT_F, ""))
    # locking housing bolted over the operator, chain + D-lock below
    o.extend(_lock_house(cx, cy - 92, 60, 26))
    o.extend(_chain(cx - 60, cy - 92, cx + 60, cy - 92, 9))
    o.extend(_padlock(cx + 60, cy - 74, 10))
    return o


@_reg17
def fig_vsh_10_4():
    """Figure 10-4 — gate valve with mechanical locking device."""
    ten = "Gate valve fitted with a mechanical locking device"
    tvi = "Van gate lắp thiết bị khóa cơ khí"
    ops = _locked_valve("gate")
    marks = [
        (("hộp khóa cơ khí", "locking device housing"), (200, 144)),
        (("hai khóa và chìa riêng", "two locks with dedicated keys"),
         (172, 144)),
        (("thân van gate", "gate body"), (200, 236)),
        (("khóa padlock / D-lock", "padlock / D-lock"), (260, 166)),
        (("dây xích", "chain"), (260, 144)),
    ]
    return _fig10(4, ten, tvi, marks, ops=ops,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_5():
    """Figure 10-5 — ball valve with mechanical locking device."""
    ten = "Ball valve fitted with a mechanical locking device"
    tvi = "Van bi lắp thiết bị khóa cơ khí"
    ops = _locked_valve("ball")
    marks = [
        (("hộp khóa trên trục", "housing on the stem"), (200, 144)),
        (("cần mở van 90°", "quarter-turn wrench"), (200, 170)),
        (("bi nổi", "floating ball"), (200, 236)),
        (("khóa padlock / D-lock", "padlock / D-lock"), (260, 166)),
        (("đế van bi", "ball seats"), (172, 236)),
    ]
    return _fig10(5, ten, tvi, marks, ops=ops,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_6():
    """Figure 10-6 — butterfly valve with mechanical locking device."""
    ten = "Butterfly valve fitted with a mechanical locking device"
    tvi = "Van bướm lắp thiết bị khóa cơ khí"
    ops = _locked_valve("butterfly")
    marks = [
        (("hộp khóa trên trục", "housing on the stem"), (200, 144)),
        (("cần mở van 90°", "quarter-turn wrench"), (200, 170)),
        (("đĩa bướm", "butterfly disc"), (200, 236)),
        (("khóa padlock / D-lock", "padlock / D-lock"), (260, 166)),
        (("thân van bướm wafer", "wafer body"), (170, 202)),
    ]
    return _fig10(6, ten, tvi, marks, ops=ops,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_7():
    """Figure 10-7 — double PRV interlock schematic."""
    ten = ("Mechanical interlocking of two PRVs: valve states and key "
           "paths between the control room and the isolating valves")
    tvi = ("Khóa cơ khí hai van an toàn PRV: trạng thái van và đường đi "
           "chìa giữa phòng điều khiển và các van cách ly")
    ops = []
    tx = []
    # blow-off header
    ops.append(("line", 40, 110, 320, 110, 1.8, INK, ""))
    ops.append(("poly", [(40, 110), (52, 106), (52, 114)], INK, 1.0, INK, "",
                True))
    tx.append(_txt(40, 100, "BLOW OFF", 7.0, color=GREY))
    # vessel feed at bottom
    ops.append(("line", 180, 330, 180, 296, 1.8, INK, ""))
    ops.append(("poly", [(174, 306), (186, 306), (180, 296)], INK, 1.0, INK,
                "", True))
    # PRV branches: left PRV1 (in service), right PRV2 (standby)
    for bx, tag in ((120, "PRV 1"), (250, "PRV 2")):
        ops.append(("line", bx, 296, bx, 234, 1.6, INK, ""))
        # PRV symbol (spring triangle)
        ops.append(("poly", [(bx - 10, 226), (bx + 10, 226), (bx, 212)],
                    "#ffffff", 1.3, INK, "", True))
        ops.append(("line", bx - 8, 208, bx + 8, 208, 1.4, INK, ""))
        ops.append(("line", bx - 6, 204, bx + 6, 204, 1.0, INK, ""))
        ops.append(("line", bx, 212, bx, 204, 1.2, INK, ""))
        tx.append(_txt(bx - 44, 222, tag, 7.4, weight="bold"))
        # riser into the header
        ops.append(("line", bx, 212, bx, 110, 1.6, INK, ""))
    # isolating valves: V4 above PRV1, V1 above PRV2, V3 / V2 below
    def bowtie(x, y, closed):
        if closed:
            ops.append(("poly", [(x - 9, y - 7), (x + 9, y + 7),
                                 (x + 9, y - 7), (x - 9, y + 7)],
                        INK, 1.0, INK, "", True))
        else:
            ops.append(("poly", [(x - 9, y - 7), (x - 9, y + 7), (x + 9, y)],
                        "none", 1.2, INK, "", False))
            ops.append(("poly", [(x + 9, y - 7), (x + 9, y + 7), (x - 9, y)],
                        "none", 1.2, INK, "", False))
    bowtie(120, 140, True)
    tx.append(_txt(96, 144, "V4", 7.4, weight="bold"))
    bowtie(250, 140, False)
    tx.append(_txt(226, 144, "V1", 7.4, weight="bold"))
    bowtie(120, 266, True)
    tx.append(_txt(96, 270, "V3", 7.4, weight="bold"))
    bowtie(250, 266, False)
    tx.append(_txt(226, 270, "V2", 7.4, weight="bold"))
    # key boxes with trapped/free keys
    def keybox(x, y, filled, letter):
        ops.append(("poly", [(x - 11, y - 9), (x + 11, y - 9), (x + 11, y + 9),
                             (x - 11, y + 9)],
                    "#ffffff" if not filled else LOCK_F, 1.2, INK, "", True))
        tx.append(_txt(x, y + 2, letter, 7.4,
                        weight="bold", color=GREY if not filled else INK))
    keybox(146, 140, True, "E")
    keybox(276, 140, False, "A")
    keybox(146, 266, True, "D")
    keybox(276, 266, False, "B")
    # control room box and key path (dashed)
    ops.append(("poly", [(150, 40), (300, 40), (300, 68), (150, 68)],
                "#ffffff", 1.3, INK, "", True))
    tx.append(_txt(225, 57, "CONTROL ROOM", 7.6, weight="bold"))
    ops.append(("line", 276, 68, 276, 131, 1.0, GREY, "5,4"))
    extra = [
        _txt(330, 96, "đường đi chìa (key path)", 6.8, color=GREY,
             anchor="end"),
        _txt(180, 352, "kịch bản: PRV 1 phục vụ, PRV 2 dự phòng",
             6.8, color=GREY),
        _txt(324, 352, "V1, V3, V4 — khóa mở", 6.8, color=GREY, anchor="end"),
    ]
    marks = [
        (("van an toàn PRV", "pressure relief valves"), (250, 218)),
        (("van cách ly V1…V4", "isolating valves V1…V4"), (185, 270)),
        (("hộp chìa trên van", "key boxes on the valves"), (302, 140)),
        (("chìa bị giữ / chìa rỗi", "trapped / free key"), (172, 266)),
        (("phòng điều khiển", "control room"), (160, 58)),
        (("đường ra khí thải", "blow-off header"), (70, 110)),
    ]
    extra.extend(tx)
    return _fig10(7, ten, tvi, marks, ops=ops, extra=extra,
                  courtesy="Netherlocks, Holland")


@_reg17
def fig_vsh_10_8():
    """Figure 10-8 — pig launcher interlock schematic."""
    ten = "Mechanical interlocking of a pipeline pig launcher"
    tvi = "Khóa cơ khí cho bệ phóng pig trên đường ống"
    ops = []
    tx = []
    # main supply line
    ops.append(("line", 40, 250, 106, 250, 1.7, INK, ""))
    tx.append(_txt(40, 264, "MAIN SUPPLY", 7.0, color=GREY))
    # V1 (throttle, locked closed in start scenario)
    ops.append(("poly", [(106, 243), (106, 257), (130, 250)], "none", 1.2,
                INK, "", False))
    ops.append(("poly", [(130, 243), (130, 257), (106, 250)], "none", 1.2,
                INK, "", False))
    tx.append(_txt(100, 234, "V1", 7.4, weight="bold"))
    # launcher barrel: wide door end tapering into the line bore
    ops.append(("poly", [(130, 206), (300, 224), (300, 276), (130, 294)],
                BODY_F, 1.5, INK, "", True))
    tx.append(_txt(215, 254, "PIG LAUNCHER", 7.6, weight="bold"))
    # closure door on the left end
    ops.append(("line", 130, 206, 130, 294, 2.2, SHAFT_F, ""))
    ops.append(("line", 124, 214, 124, 286, 1.6, INK, ""))
    # pig inside barrel
    ops.append(("poly", [(192, 242), (230, 250), (192, 258), (200, 250)],
                RING_F, 1.0, INK, "", True))
    # V3 after launcher, then V2 pipeline valve, then transport line
    ops.append(("line", 300, 250, 336, 250, 1.7, INK, ""))
    ops.append(("poly", [(336, 243), (336, 257), (360, 250)], "none", 1.2,
                INK, "", False))
    ops.append(("poly", [(360, 243), (360, 257), (336, 250)], "none", 1.2,
                INK, "", False))
    tx.append(_txt(338, 232, "V3", 7.4, weight="bold"))
    ops.append(("line", 360, 250, 396, 250, 1.7, INK, ""))
    ops.append(("poly", [(396, 241), (396, 259), (424, 250)], "none", 1.2,
                INK, "", False))
    ops.append(("poly", [(424, 241), (424, 259), (396, 250)], "none", 1.2,
                INK, "", False))
    tx.append(_txt(398, 232, "V2", 7.4, weight="bold"))
    ops.append(("line", 424, 250, 470, 250, 1.7, INK, ""))
    tx.append(_txt(470, 264, "MAIN TRANSPORT", 7.0, color=GREY,
                    anchor="end"))
    # vent valve V4 up from the launcher nose
    ops.append(("line", 300, 210, 300, 160, 1.6, INK, ""))
    ops.append(("poly", [(293, 160), (307, 160), (307, 146), (293, 146)],
                "none", 1.2, INK, "", False))
    ops.append(("poly", [(293, 146), (307, 146), (307, 132), (293, 132)],
                INK, 1.0, INK, "", True))
    tx.append(_txt(314, 140, "V4", 7.4, weight="bold"))
    ops.append(("line", 300, 132, 300, 100, 1.4, INK, ""))
    tx.append(_txt(308, 96, "VENT", 7.0, color=GREY))
    # key boxes
    def keybox(x, y, filled, letter):
        ops.append(("poly", [(x - 11, y - 9), (x + 11, y - 9), (x + 11, y + 9),
                             (x - 11, y + 9)],
                    "#ffffff" if not filled else LOCK_F, 1.2, INK, "", True))
        tx.append(_txt(x, y + 2, letter, 7.4,
                        weight="bold", color=GREY if not filled else INK))
    keybox(106, 218, True, "D")
    keybox(330, 214, False, "C")
    keybox(330, 176, True, "A")
    # control room
    ops.append(("poly", [(180, 40), (330, 40), (330, 68), (180, 68)],
                "#ffffff", 1.3, INK, "", True))
    tx.append(_txt(255, 57, "CONTROL ROOM", 7.6, weight="bold"))
    ops.append(("line", 330, 54, 352, 54, 1.0, GREY, "5,4"))
    ops.append(("line", 352, 54, 352, 176, 1.0, GREY, "5,4"))
    ops.append(("line", 352, 176, 341, 176, 1.0, GREY, "5,4"))
    extra = [
        _txt(240, 340, "kịch bản xuất phát: mọi van khóa đóng, cửa phóng "
             "khóa đóng, chìa A ở phòng điều khiển", 6.8, color=GREY),
        _txt(86, 122, "cửa đóng (closure door)", 6.8, color=GREY),
    ]
    marks = [
        (("bệ phóng pig", "pig launcher barrel"), (215, 230)),
        (("cửa kín barrel", "closure door"), (124, 200)),
        (("pig làm sạch", "cleaning pig"), (230, 276)),
        (("van thông V4", "vent valve V4"), (300, 146)),
        (("van V1…V3 khóa chìa", "interlocked valves V1…V3"), (396, 282)),
        (("phòng điều khiển", "control room"), (190, 58)),
    ]
    extra.extend(tx)
    return _fig10(8, ten, tvi, marks, ops=ops, extra=extra,
                  courtesy="Netherlocks, Holland")
