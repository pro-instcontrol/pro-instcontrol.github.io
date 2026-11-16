# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 9 — Manual Valves V: Ball Valves
(book ch. 3, Figures 3-60 … 3-68).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology and the variant features named in the original caption;
a numbered bilingual legend carries the feature names.  Figure 3-68 is a
redrawn editorial arrangement of the body-construction variants listed in
BS 5159:1974 (not a reproduction of the standard's drawing).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _arrow, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, PACK_F, RING_F, _ell, _emit, _emit_legend)

FIGS6 = {}


def _reg6(f):
    FIGS6[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
SEAT_F = "#e2e2dc"
BALL_F = "#d9d9d2"
PTFE_F = "#dfe8dd"


# ------------------------------------------------------------ frame builder
def _ball_ops(seats="torsion", entry="split", ball="floating",
              slots=False, diaphragm=False, wedge=False,
              spring_top=False, trunnion=False, bonnet_wedge=False,
              cam=False, sealed=False, one_piece=False):
    """Ball-valve cross-section ops; ball centre at local (0, 0)."""
    o = []
    # body shell — the bore band runs y 88..114 in the local frame
    body = [(-88, 76), (-62, 58), (-34, 52), (0, 52), (34, 52),
            (62, 58), (88, 76), (88, 114), (62, 132), (34, 140),
            (-34, 140), (-62, 132), (-88, 114)]
    o.append(("poly", body, BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 96, 72), (sx * 88, 72), (sx * 88, 118),
                           (sx * 96, 118)], RING_F, 1.2, INK, "", True))
        o.append(("line", sx * 88, 88, sx * 36, 88, 1.2, INK, ""))
        o.append(("line", sx * 88, 112, sx * 36, 112, 1.2, INK, ""))
    if entry == "axial":
        # bolted axial-entry cover on the upstream side
        o.append(("poly", [(-104, 76), (-88, 76), (-88, 114), (-104, 114)],
                  RING_F, 1.2, INK, "", True))
        for yy in (82, 108):
            o.append(("line", -104, yy, -96, yy, 0.9, INK, ""))
    elif entry == "sandwich":
        for sx in (-1, 1):
            o.append(("line", sx * 58, 54, sx * 58, 138, 1.2, INK, ""))
    elif entry == "top":
        o.append(("poly", [(-38, -62), (38, -62), (38, -48), (-38, -48)],
                  RING_F, 1.2, INK, "", True))
        for bx in (-30, -10, 10, 30):
            o.append(("line", bx, -64, bx, -46, 0.9, INK, ""))
    elif sealed:
        for sx in (-1, 1):
            o.append(("circ", sx * 74, 132, 2.6, 0.9, INK, "#ffffff"))
    # ------------------------------------------------------------- ball
    c = []
    for i in range(29):
        t = 2 * math.pi * i / 28.0
        c.append((34 * math.cos(t), 100 + 34 * math.sin(t)))
    o.append(("poly", c, BALL_F, 1.3, INK, "", False))
    if cam:
        # ball lifted clear of the seat by the cam mechanism
        o.append(("poly", [(-36, 90), (36, 90), (36, 106), (-36, 106)],
                  "#ffffff", 1.0, INK, "", True))
    else:
        o.append(("poly", [(-36, 92), (36, 92), (36, 110), (-36, 110)],
                  "#ffffff", 1.0, INK, "", True))
    if trunnion:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 34 - 4, 97), (sx * 34 + 4, 97),
                               (sx * 34 + 4, 105), (sx * 34 - 4, 105)],
                      RING_F, 1.0, INK, "", True))
    if ball == "floating":
        o.append(("line", 0, 66, 0, 92, 0.8, INK, "3 2"))
    # ------------------------------------------------------------ seats
    for sx in (-1, 1):
        if diaphragm:
            # seat ring carried on a metal diaphragm acting as a spring
            o.append(("poly", [(sx * 36, 80), (sx * 46, 80),
                               (sx * 46, 120), (sx * 36, 120)],
                      PTFE_F, 1.1, INK, "", True))
            o.append(("poly", [(sx * 46, 74), (sx * 52, 74),
                               (sx * 52, 126), (sx * 46, 126)],
                      "none", 1.0, INK, "", False))
        elif wedge or bonnet_wedge:
            o.append(("poly", [(sx * 36, 84), (sx * 46, 78),
                               (sx * 46, 122), (sx * 36, 116)],
                      PTFE_F, 1.1, INK, "", True))
        else:
            o.append(("poly", [(sx * 36, 84), (sx * 44, 84),
                               (sx * 44, 116), (sx * 36, 116)],
                      PTFE_F, 1.1, INK, "", True))
        if seats == "torsion":
            # cantilevered lip: ball first touches only the tip
            o.append(("poly", [(sx * 36, 84), (sx * 32, 88),
                               (sx * 32, 112), (sx * 36, 116)],
                      "none", 1.1, INK, "", False))
        if slots:
            for yy in (90, 110):
                o.append(("line", sx * 44, yy, sx * 50, yy, 0.8, INK, ""))
    if spring_top:
        o.append(("poly", [(-14, -46), (14, -46), (14, -36), (-14, -36)],
                  RING_F, 1.0, INK, "", True))
        for k in range(3):
            zz = [((-4 if k % 2 else 4), -36 + k * 5)]
            o.append(("line", -4, -34 + k * 6, 4, -31 + k * 6, 0.9, INK, ""))
    if bonnet_wedge:
        o.append(("poly", [(-42, -56), (42, -56), (42, -42), (-42, -42)],
                  RING_F, 1.1, INK, "", True))
        for bx in (-34, -12, 12, 34):
            o.append(("line", bx, -58, bx, -42, 0.9, INK, ""))
    # -------------------------------------------------------- stem / drive
    if cam:
        o.append(("poly", [(-46, -58), (46, -58), (46, -46), (-46, -46)],
                  RING_F, 1.2, INK, "", True))
        o.append(("circ", 0, -52, 6, 1.1, INK, RING_F))
        o.append(("line", -30, -58, 0, -34, 1.2, INK, ""))
    else:
        o.append(("line", 0, 66, 0, -138, 2.2, INK, ""))
        o.append(("poly", [(-12, -70), (12, -70), (12, -58), (-12, -58)],
                  PACK_F, 1.0, INK, "", True))
        o.append(("poly", _ell(0, -150, 28, 7), "#e8e8e2", 1.2, INK,
                  "", True))
        o.append(("circ", 0, -150, 5, 1.2, INK, RING_F))
    return o


def _ball_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
              w=560, h=380, xleg=402):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=200, dy=180)
    ay = 180 + 100
    o2.append(_line(82, ay, 104, ay, 1.6, color=BLUE))
    o2.append(_poly([(104, ay), (96, ay - 3.5), (96, ay + 3.5)],
                    fill=BLUE, sw=0, close=True))
    o2.append(_line(296, ay, 318, ay, 1.6, color=BLUE))
    o2.append(_poly([(296, ay), (304, ay - 3.5), (304, ay + 3.5)],
                    fill=BLUE, sw=0, close=True))
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


def _m(cfg, sub="", **kw):
    num, ten, tvi, marks, courtesy = cfg
    return _ball_fig(num, ten, tvi, marks, _ball_ops(**kw),
                     courtesy=courtesy, sub=sub)


# --------------------------------------------------------- floating ball
@_reg6
def fig_vsh_3_60():
    cfg = (60,
           "Schematic view of ball valve with floating ball and torsion "
           "seats, showing the function of pressure-equalizing slots in the "
           "periphery of the seats",
           "Sơ đồ van bi có bi nổi và chỗ kín xoắn, thể hiện tác dụng của "
           "rãnh cân bằng áp ở chu vi chỗ kín",
           [(("bi nổi", "floating ball"), (200, 264)),
            (("chỗ kín môi công đòn (torsion seat)", "cantilevered-lip "
             "torsion seat"), (166, 280)),
            (("rãnh cân bằng áp chu vi", "peripheral pressure-equalizing "
             "slots"), (234, 288)),
            (("cân bằng áp làm giảm momen van", "balanced upstream seat "
             "reduces valve torque"), (176, 326))],
           "Worcester Valve Co., Ltd.")
    return _m(cfg, seats="torsion", slots=True)


@_reg6
def fig_vsh_3_61():
    cfg = (61,
           "Ball valve with floating ball and torsion seats, with "
           "axial-entry body",
           "Van bi có bi nổi và chỗ kín xoắn, thân vào theo hướng trục",
           [(("thân vào theo hướng trục", "axial-entry body"), (152, 106)),
            (("bi nổi", "floating ball"), (200, 264)),
            (("chỗ kín xoắn có môi công đòn", "torsion seats with "
             "cantilevered lips"), (166, 280)),
            (("đệm kín cổng", "port sealing lip"), (234, 288))],
           "Jamesbury International Corp.")
    return _m(cfg, seats="torsion", entry="axial")


@_reg6
def fig_vsh_3_62():
    cfg = (62,
           "Ball valve with floating ball and diaphragm-supported seats, "
           "with sandwich-split body",
           "Van bi có bi nổi và chỗ kín do màng đỡ, thân ghép kẹp",
           [(("chỗ kín đỡ bằng màng kim loại", "seat rings supported on "
             "metal diaphragms"), (166, 280)),
            (("màng đóng vai trò lò xo", "diaphragms act as springs"),
             (234, 288)),
            (("thân ghép kẹp (sandwich-split)", "sandwich-split body"),
             (234, 140)),
            (("bi nổi", "floating ball"), (200, 264))],
           "Rich. Klinger AG.")
    return _m(cfg, entry="sandwich", diaphragm=True)


@_reg6
def fig_vsh_3_63():
    cfg = (63,
           "Ball valve with wedge seats spring-loaded from the top, with "
           "one-piece top-entry body",
           "Van bi có chỗ kín dạng nêm nén bằng lò xo từ trên, thân một "
           "mảnh vào từ trên",
           [(("lò xo nén từ trên", "spring loading from the top"),
             (200, 118)),
            (("chỗ kín dạng nêm", "wedge-shaped seats"), (166, 280)),
            (("thân một mảnh vào từ trên", "one-piece top-entry body"),
             (234, 128)),
            (("bi nổi", "floating ball"), (200, 264))],
           "McCanna")
    return _m(cfg, entry="top", wedge=True, spring_top=True)


# ------------------------------------------------------ trunnion mounted
@_reg6
def fig_vsh_3_64():
    cfg = (64,
           "Ball valve with trunnion-supported ball and floating seats, "
           "with one-piece sealed body",
           "Van bi có bi đỡ bằng chốt và chỗ kín phao, thân một mảnh kín",
           [(("bi đỡ bằng chốt (trunnion)", "trunnion-supported ball"),
             (200, 264)),
            (("chỗ kín phao, kín chu vi bằng O-ring", "floating seat ring "
             "sealed by a peripheral O-ring"), (166, 280)),
            (("tự quay nhẹ chỗ kín mỗi lần thao tác", "seat rings rotated "
             "slightly on each operation"), (234, 288)),
            (("thân kín một mảnh", "one-piece sealed body"), (176, 326))],
           "Cameron Iron Works, Inc.")
    return _m(cfg, seats="metal", ball="trunnion", trunnion=True,
              sealed=True, one_piece=True,
              sub="Dùng cho áp suất chất lỏng cao / For high fluid pressures")


@_reg6
def fig_vsh_3_65():
    cfg = (65,
           "Ball valve with trunnion-supported ball and wedge seats forced "
           "into the valve body by the bonnet, with one-piece top-entry body",
           "Van bi có bi đỡ chốt và chỗ kín nêm do nắp ép vào thân, thân một "
           "mảnh vào từ trên",
           [(("nắp ép chỗ kín vào thân", "bonnet forces the seats into "
             "the body"), (200, 116)),
            (("chỗ kín nêm", "wedge seats"), (166, 280)),
            (("bi đỡ bằng chốt", "trunnion-supported ball"), (200, 264)),
            (("môi chỗ kín bo tròn để giảm momen", "radiused seat lips "
             "reduce torque"), (234, 288))],
           "Truflo Limited.")
    return _m(cfg, entry="top", wedge=True, bonnet_wedge=True,
              trunnion=True, ball="trunnion")


@_reg6
def fig_vsh_3_66():
    cfg = (66,
           "Ball valve with cam mechanism to seat and unseat the ball",
           "Van bi có cơ cấu cam đưa bi vào và ra khỏi chỗ kín",
           [(("cơ cấu cam", "cam mechanism"), (200, 112)),
            (("nâng bi ra khỏi chỗ kín trước khi mở", "ball lifted clear "
             "of the seat before opening"), (166, 280)),
            (("ép bi lại sau khi đóng", "ball forced back after closing"),
             (234, 288)),
            (("loại bỏ phần lớn trượt giữa mặt kín", "avoids most sliding "
             "between seatings"), (176, 326))],
           "Orbit Valve Company.")
    return _m(cfg, cam=True, seats="metal")


# ------------------------------------------------------- antistatic detail
@_reg6
def fig_vsh_3_67():
    """Antistatic device: spring-loaded plungers earthing ball/stem/body."""
    w, h = 560, 340
    o = [_defs()]
    cx = 200
    # stem tongue and part of the ball
    o.append(_rect(cx - 10, 50, 20, 130, fill=BALL_F, sw=1.3))
    o.append(_poly([(cx - 46, 190), (cx - 30, 164), (cx + 30, 164),
                    (cx + 46, 190), (cx + 30, 250), (cx - 30, 250)],
                   fill=BALL_F, sw=1.3, close=True))
    # body boss around the stem
    o.append(_poly([(cx - 46, 40), (cx - 22, 40), (cx - 22, 150),
                    (cx - 46, 150)], fill=BODY_F, sw=1.2, close=True))
    o.append(_poly([(cx + 22, 40), (cx + 46, 40), (cx + 46, 150),
                    (cx + 22, 150)], fill=BODY_F, sw=1.2, close=True))
    # plunger 1: stem tongue to ball
    o.append(_rect(cx + 10, 168, 26, 10, fill=RING_F, sw=1.1))
    for k in range(3):
        o.append(_line(cx + 14 + k * 8, 170, cx + 18 + k * 8, 176,
                       0.8, INK))
    # plunger 2: stem to body
    o.append(_rect(cx - 40, 86, 22, 10, fill=RING_F, sw=1.1))
    for k in range(3):
        o.append(_line(cx - 38 + k * 7, 88, cx - 34 + k * 7, 94,
                       0.8, INK))
    for i, (vi, en) in enumerate([
            ("pít-tông lò xo giữa lưỡi trục và bi",
             "spring-loaded plunger, stem tongue to ball"),
            ("pít-tông lò xo giữa trục và thân",
             "spring-loaded plunger, stem to body"),
            ("đảm bảo thông mạch điện", "ensures electrical continuity"),
            ("tránh tia lửa gây cháy", "prevents incendiary sparks")]):
        yy = 62 + i * 40
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx + 28, 173, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx + 28, 173.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx - 30, 91, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 30, 91.5, "2", 8.0, weight="bold"))
    o.append(_txt(476, 320, "Worcester Valve Co., Ltd.", 6.6, color=GREY))
    return _fig(svg(w, h, "".join(o), "Ball valve antistatic device"),
                "Hình 3-67 · Thiết bị chống tĩnh điện nối trục với bi và "
                "trục với thân van bi (vẽ lại). Nguồn: Worcester Valve "
                "Co., Ltd.",
                "Figure 3-67 · Antistatic device grounding stem to ball and "
                "stem to body of a ball valve — redrawn. (Courtesy of "
                "Worcester Valve Co., Ltd.)",
                "Thiết bị chống tĩnh điện cho van bi.",
                "Antistatic device for a ball valve.")


# --------------------------------------------------- body construction map
@_reg6
def fig_vsh_3_68():
    """Editorial arrangement of the body-construction variants in BS 5159."""
    w, h = 560, 380
    o = [_defs()]

    def variant(x, y, label, split_line=False, top_entry=False,
                sealed=False, tapping=None):
        o.append(_rect(x - 46, y - 30, 92, 60, fill=BODY_F, sw=1.3))
        o.append(_rect(x - 58, y - 8, 12, 16, fill=RING_F, sw=1.1))
        o.append(_rect(x + 46, y - 8, 12, 16, fill=RING_F, sw=1.1))
        o.append(_circle(x, y, 17, fill="#ffffff", sw=1.1))
        if split_line:
            o.append(_line(x - 46, y + 14, x + 46, y + 14, 1.1, INK))
        if top_entry:
            o.append(_rect(x - 20, y - 42, 40, 12, fill=RING_F, sw=1.1))
            o.append(_line(x, y - 42, x, y - 17, 1.1, INK))
        if sealed:
            o.append(_circle(x - 40, y - 24, 2.4, sw=0.9, color=INK,
                             fill=GREY))
            o.append(_circle(x + 40, y - 24, 2.4, sw=0.9, color=INK,
                             fill=GREY))
        if tapping:
            o.append(_line(x, y - 30, x, y - 48, 1.0, INK))
            o.append(_txt(x, y - 52, tapping, 6.4, color=GREY))
        o.append(_txt(x, y + 48, label, 7.2, color=INK, weight="bold"))

    variant(100, 100, "Thân một mảnh / One-piece", sealed=True)
    variant(270, 100, "Thân ghép đôi / Split", split_line=True)
    variant(100, 230, "Vào từ trên / Top entry", top_entry=True)
    variant(270, 230, "Thân kín + vào trên / Sealed, top", top_entry=True,
            sealed=True, tapping="tap")
    for i, (vi, en) in enumerate([
            ("thân một mảnh: ít mối nối", "one-piece: fewest body joints"),
            ("thân kín: dùng khi chôn", "sealed body: buried service"),
            ("vào từ trên: sửa tại chỗ", "top entry: in-situ servicing"),
            ("vị trí lấy áp trên thân", "body tapping locations")]):
        yy = 62 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_txt(476, h - 14, "BS 5159:1974 (sơ đồ biên tập)", 6.6,
                  color=GREY))
    return _fig(svg(w, h, "".join(o), "Ball valve body constructions"),
                "Hình 3-68 · Các kiểu thân và vị trí lấy áp của van bi "
                "(sơ đồ biên tập, vẽ lại theo BS 5159:1974).",
                "Figure 3-68 · Ball valve body constructions and body "
                "tapping locations (editorial schematic redrawn from "
                "BS 5159:1974).",
                "Các kiểu thân van bi và vị trí lấy áp.",
                "Ball valve body constructions and tapping locations.")
