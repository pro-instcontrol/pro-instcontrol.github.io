# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 13 — Direct-Loaded Pressure Relief Valves
(book ch. 5, Figures 5-1 … 5-34).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections;
numbered bilingual legends name the features.  Force/lift diagrams and
control-piping layouts are editorial schematics: the source provides no
numeric scales, so none are invented.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, PACK_F, RING_F, _ell, _emit, _emit_legend)

FIGS10 = {}


def _reg10(f):
    FIGS10[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
DISC_F = "#d9d9d2"
RUBBER_F = "#c9d5c9"
SPRING_F = "#dcdcd6"


def _prv_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
             extra=(), w=560, h=380, xleg=402):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0.0, cy=0.0, dx=200, dy=180)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "Hình 5-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 5-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _spring(o, x, y1, y2, turns=6, width=8):
    pts = [(x, y1)]
    for i in range(turns * 2):
        pts.append((x + (-width if i % 2 else width),
                    y1 + (y2 - y1) * (i + 1) / (turns * 2.0)))
    pts.append((x, y2))
    o.append(("poly", pts, "none", 1.3, INK, "", False))


def _prv_ops(open_bonnet=False, cooling=False, eductor=False,
             vent_bonnet=False, bellows=False, piston_seal=False, spool=False,
             guide_ring=False, nozzle_ring=False, friction_ring=False,
             proportional=False, belleville=False, actuator=False,
             dry_damper=False, viscous_damper=False, pop=True):
    """Spring-loaded PRV; vertical inlet below, horizontal outlet right."""
    o = []
    o.append(("poly", [(-56, 162), (-56, 96), (-78, 70), (-78, 44),
                       (-40, 26), (40, 26), (78, 44), (78, 70),
                       (100, 70), (100, 100), (56, 100), (56, 162)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-42, 162), (42, 162), (42, 172), (-42, 172)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(100, 62), (108, 62), (108, 108), (100, 108)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-22, 96), (22, 96), (22, 166), (-22, 166)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-40, 62), (94, 62), (94, 90), (-40, 90)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-30, 90), (-22, 90), (-22, 100), (-30, 100)],
              RING_F, 1.1, INK, "", True))
    o.append(("poly", [(22, 90), (30, 90), (30, 100), (22, 100)],
              RING_F, 1.1, INK, "", True))
    dy = -4 if pop else 4
    o.append(("poly", [(-28, 82 + dy), (28, 82 + dy),
                       (28, 90 + dy), (-28, 90 + dy)],
              DISC_F, 1.3, INK, "", True))
    if proportional:
        o.append(("poly", [(28, 76), (46, 66), (46, 94), (28, 84)],
                  DISC_F, 1.1, INK, "", True))
    o.append(("line", 0, 82 + dy, 0, -52, 2.0, INK, ""))

    # bonnet and spring enclosure
    if open_bonnet:
        o.append(("line", -44, 26, -44, -34, 1.6, INK, ""))
        o.append(("line", 44, 26, 44, -34, 1.6, INK, ""))
        o.append(("line", -30, 26, -30, -34, 1.0, GREY, ""))
        o.append(("line", 30, 26, 30, -34, 1.0, GREY, ""))
    else:
        o.append(("poly", [(-48, 26), (-48, -16), (-32, -50),
                           (32, -50), (48, -16), (48, 26)],
                  BODY_F, 1.3, INK, "", True))
        if vent_bonnet:
            o.append(("line", 48, -8, 88, -8, 1.0, GREY, "4 3"))
            o.append(("line", 88, -8, 88, 62, 1.0, GREY, "4 3"))
    if cooling:
        o.append(("poly", [(-46, 26), (46, 26), (46, 40), (-46, 40)],
                  PACK_F, 1.0, INK, "", True))
    if spool:
        o.append(("poly", [(-30, 78), (-30, -12), (30, -12), (30, 78)],
                  "none", 1.0, GREY, "3 2", True))

    if belleville:
        for i in range(5):
            yy = -34 + i * 11
            o.append(("poly", [(-28, yy), (28, yy), (18, yy + 7), (-18, yy + 7)],
                      SPRING_F, 1.1, INK, "", True))
    else:
        _spring(o, 0, -40, 74 + dy)
    o.append(("poly", [(-16, -54), (16, -54), (16, -46), (-16, -46)],
              RING_F, 1.1, INK, "", True))
    o.append(("line", 0, -54, 0, -68, 1.4, INK, ""))

    if bellows:
        for sx in (-1, 1):
            pts = []
            for i in range(11):
                pts.append((sx * (16 + (6 if i % 2 else 0)), -10 + i * 8))
            o.append(("poly", pts, "none", 1.1, INK, "", False))
    if piston_seal:
        o.append(("poly", [(-16, 40), (16, 40), (16, 52), (-16, 52)],
                  RING_F, 1.0, INK, "", True))
        o.append(("line", -14, 46, 14, 46, 1.2, BLUE, ""))
    if guide_ring:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 30, 70), (sx * 38, 70),
                               (sx * 38, 84), (sx * 30, 84)],
                      RING_F, 1.0, INK, "", True))
    if nozzle_ring:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 30, 96), (sx * 38, 96),
                               (sx * 38, 106), (sx * 30, 106)],
                      RING_F, 1.0, INK, "", True))
    if friction_ring:
        for yy in (28, 60):
            o.append(("circ", 0, yy, 6, 1.1, INK, RUBBER_F))
    if eductor:
        for sx in (-1, 1):
            o.append(("line", sx * 34, 76, sx * 34, 26, 1.2, BLUE, ""))
            o.append(("poly", [(sx * 34, 26), (sx * 30, 34), (sx * 38, 34)],
                      BLUE, 0, BLUE, "", True))
    if dry_damper:
        for yy in (18, 30, 42, 54):
            o.append(("poly", [(-20, yy), (0, yy + 4), (20, yy),
                               (0, yy - 4)], "#6f6f6f", 1.0, INK, "", True))
    if viscous_damper:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 12, 14), (sx * 26, 14),
                               (sx * 26, 58), (sx * 12, 58)],
                      "#e5eee4", 1.0, INK, "", True))
            o.append(("line", sx * 19, 16, sx * 19, 56, 0.8, GREY, ""))
    if actuator:
        o.append(("poly", [(-32, -118), (32, -118), (32, -68), (-32, -68)],
                  RING_F, 1.2, INK, "", True))
        o.append(("line", -32, -92, 32, -92, 1.2, INK, ""))
        o.append(("line", 0, -68, 0, -54, 1.6, INK, ""))
        o.append(("poly", [(-22, -110), (22, -110), (22, -96), (-22, -96)],
                  "#dbe6f0", 1.0, INK, "", True))

    # flow arrows
    o.append(("line", 0, 158, 0, 112, 1.6, BLUE, ""))
    o.append(("poly", [(0, 112), (-3.5, 120), (3.5, 120)],
              BLUE, 0, BLUE, "", True))
    o.append(("line", 36, 76, 88, 76, 1.6, BLUE, ""))
    o.append(("poly", [(88, 76), (80, 72.5), (80, 79.5)],
              BLUE, 0, BLUE, "", True))
    return o


# -------------------------------------------------- historical disc elements
def _disc_element(turn_deg=90, lip=True):
    o = []
    o.append(("poly", [(-84, 128), (84, 128), (84, 158), (-84, 158)],
              BODY_F, 1.2, INK, "", True))
    o.append(("poly", [(-30, 78), (30, 78), (30, 128), (-30, 128)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-44, 118), (-30, 118), (-30, 130), (-44, 130)],
              RING_F, 1.1, INK, "", True))
    o.append(("poly", [(30, 118), (44, 118), (44, 130), (30, 130)],
              RING_F, 1.1, INK, "", True))
    o.append(("poly", [(-36, 88), (36, 88), (36, 100), (-36, 100)],
              DISC_F, 1.3, INK, "", True))
    if lip:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 36, 88), (sx * 52, 82),
                               (sx * 52, 92), (sx * 36, 100)],
                      DISC_F, 1.1, INK, "", True))
    o.append(("line", 0, 88, 0, 40, 2.0, INK, ""))
    for sx in (-1, 1):
        o.append(("line", sx * 46, 100, sx * 62, 100 - 24, 1.2, BLUE, ""))
        o.append(("poly", [(sx * 62, 100 - 24), (sx * 54, 100 - 20),
                           (sx * 60, 100 - 16)], BLUE, 0, BLUE, "", True))
    o.append(("poly", [(-50, 112), (50, 112), (50, 124), (-50, 124)],
              "none", 1.0, GREY, "3 2", True))
    o.append(("line", 0, 158, 0, 130, 1.6, BLUE, ""))
    return o


@_reg10
def fig_vsh_5_1():
    return _prv_fig(
        1, "Valve elements of a Ritchie-type pressure relief valve: annular "
        "huddling chamber and secondary orifice",
        "Các phần tử của van an toàn kiểu Ritchie: buồng tụ áp hình vòng "
        "và lỗ phụ",
        [(("vành deflector và môi quanh đĩa", "peripheral deflector and lip"),
          (240, 262)),
         (("buồng tụ áp hình vòng", "annular huddling chamber"),
          (200, 290)),
         (("lỗ phụ quanh chỗ kín", "secondary orifice around the seat"),
          (162, 304)),
         (("dòng chỉ đổi hướng khoảng 90°", "flow deflected only about 90°"),
          (158, 262))],
        _disc_element(turn_deg=90),
        "Editorial schematic / sơ đồ biên tập")


@_reg10
def fig_vsh_5_2():
    return _prv_fig(
        2, "Naylor-type pressure relief valve: lip turns the discharge "
        "through 180° for maximum lift",
        "Van an toàn kiểu Naylor: môi dẫn dòng quay 180° để nâng đĩa tối đa",
        [(("môi quanh đĩa", "lip around the disc"), (240, 262)),
         (("dòng đổi hướng 180°", "flow turned through 180°"), (200, 214)),
         (("lực nâng cực đại từ động lượng", "maximum lift from momentum"),
          (162, 304)),
         (("độ mở tỉ lệ với áp suất vượt", "lift proportional to overpressure"),
          (158, 262))],
        _disc_element(turn_deg=180),
        "Editorial schematic / sơ đồ biên tập")


# -------------------------------------------------------------- safety valves
@_reg10
def fig_vsh_5_3():
    return _prv_fig(
        3, "Safety valve with open bonnet", "Van an toàn có nắp hở",
        [(("nắp hở để hơi thoát ra", "open bonnet vents leaking steam"),
          (156, 180)),
         (("lò xo và vít chỉnh", "spring and adjusting screw"), (200, 118)),
         (("đĩa và chỗ kín", "disc and seat"), (200, 270)),
         (("đường ra", "outlet"), (288, 258))],
        _prv_ops(open_bonnet=True), "Dresser Industries.")


@_reg10
def fig_vsh_5_4():
    return _prv_fig(
        4, "Safety valve with cooling spool between body and bonnet",
        "Van an toàn có vòng làm mát giữa thân và nắp",
        [(("vòng làm mát (lantern ring)", "cooling (lantern) spool"),
          (200, 206)),
         (("lò xo được bảo vệ khỏi quá nhiệt", "spring protected from overheating"),
          (200, 130)),
         (("đĩa và chỗ kín", "disc and seat"), (200, 270)),
         (("đường ra", "outlet"), (288, 258))],
        _prv_ops(open_bonnet=True, cooling=True),
        "Crosby Valve &amp; Gage Company, Wrentham, MA.")


@_reg10
def fig_vsh_5_5():
    return _prv_fig(
        5, "Safety valve with no nozzle ring; secondary orifice fixed by "
        "seat and disc geometry",
        "Van an toàn không có vòng béc; lỗ phụ do hình học chỗ kín và đĩa quyết định",
        [(("không có vòng béc", "no nozzle ring"), (200, 298)),
         (("hình học cố định của lỗ phụ", "fixed secondary-orifice geometry"),
          (236, 276)),
         (("đĩa dẫn trong bạc", "disc guided in sleeve"), (168, 244)),
         (("lò xo", "spring"), (200, 134))],
        _prv_ops(open_bonnet=True, guide_ring=True),
        "Sempell A.G.")


@_reg10
def fig_vsh_5_6():
    return _prv_fig(
        6, "Safety valve with eductor lift assistance",
        "Van an toàn có cơ cấu hút hỗ trợ nâng đĩa",
        [(("kênh hút quanh đĩa", "eductor channels around the disc"),
          (236, 254)),
         (("hút sạch buồng phía trên đĩa", "evacuates chamber above the disc"),
          (200, 200)),
         (("đóng mở sắc dọn", "sharp opening and closing"), (200, 130)),
         (("lò xo", "spring"), (168, 166))],
        _prv_ops(eductor=True),
        "Crosby Valve &amp; Gage Company, Wrentham, MA.")


# ------------------------------------------------------ safety relief valves
@_reg10
def fig_vsh_5_7():
    return _prv_fig(
        7, "Conventional safety relief valve with closed bonnet vented to outlet",
        "Van an toàn xả thông thường có nắp kín thông hơi sang đầu ra",
        [(("nắp kín thông sang đầu ra", "closed bonnet vented to outlet"),
          (200, 162)),
         (("vòng béc chỉnh blowdown", "nozzle blowdown ring"), (226, 300)),
         (("đĩa và chỗ kín", "disc and seat"), (200, 270)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, nozzle_ring=True),
        "Anderson, Greenwood &amp; Co.")


@_reg10
def fig_vsh_5_8():
    return _prv_fig(
        8, "Conventional safety relief valve with external blowdown screw",
        "Van an toàn xả thông thường có vít chỉnh blowdown bên ngoài",
        [(("vít chỉnh bên ngoài", "external adjusting screw"),
          (274, 216)),
         (("một lỗ dẫn bị tiết lưu một phần", "one guide hole partly restricted"),
          (226, 262)),
         (("ghế mềm cho xả nhiệt LPG/ammonia",
           "soft seatings for LPG/ammonia thermal relief"), (200, 300)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, nozzle_ring=True),
        "Anderson, Greenwood &amp; Co.",
        extra=(_line(468, 214, 494, 214, 1.2, INK, ""),
               _txt(498, 218, "vít / screw", 6.2, anchor="start",
                    color=GREY)))


@_reg10
def fig_vsh_5_9():
    return _prv_fig(
        9, "Safety relief valve converted to steam duty with open bonnet",
        "Van an toàn xả chuyển sang dịch vụ hơi có nắp hở",
        [(("nắp hở: cân bằng một phần", "open bonnet: partially balanced"),
          (200, 172)),
         (("không phù hợp áp suất ngược cộng thêm",
           "not for superimposed back pressure"), (244, 180)),
         (("đĩa và chỗ kín", "disc and seat"), (200, 270)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(open_bonnet=True, guide_ring=True),
        "Crosby Valve &amp; Gage Company, Wrentham, MA.")


@_reg10
def fig_vsh_5_10():
    return _prv_fig(
        10, "Bellows-balanced safety relief valve, bonnet vented",
        "Van an toàn xả cân bằng bằng ống màng, nắp thông hơi",
        [(("ống màng cân bằng", "balancing bellows"), (174, 216)),
         (("nắp thông hơi", "vented bonnet"), (200, 160)),
         (("diện tích đĩa không cân bằng nhỏ", "small unbalanced disc area"),
          (226, 276)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, bellows=True), "Sempell A.G.")


@_reg10
def fig_vsh_5_11():
    return _prv_fig(
        11, "Bellows-balanced safety relief valve with auxiliary piston seal",
        "Van an toàn xả cân bằng ống màng có thêm chỗ kín piston",
        [(("ống màng cân bằng", "balancing bellows"), (174, 216)),
         (("chỗ kín piston phụ", "auxiliary piston seal"), (200, 226)),
         (("lỗ thông hơi nắp", "bonnet vent"), (268, 168)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, bellows=True, piston_seal=True),
        "Dresser Industries.")


@_reg10
def fig_vsh_5_12():
    return _prv_fig(
        12, "Bellows-balanced safety relief valve with bellows in a "
        "protective spool, bonnet vented",
        "Van an toàn xả cân bằng ống màng đặt trong ống bảo vệ, nắp thông hơi",
        [(("ống màng trong ống bảo vệ", "bellows in protective spool"),
          (174, 216)),
         (("không có vòng béc", "no nozzle ring"), (226, 300)),
         (("nắp thông hơi", "vented bonnet"), (200, 160)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, bellows=True, spool=True),
        "Bopp &amp; Reuther.")


# ---------------------------------------------------------- liquid relief
@_reg10
def fig_vsh_5_13():
    return _prv_fig(
        13, "Liquid relief valve with adjustable nozzle ring, fully open "
        "within 10% overpressure",
        "Van xả chất lỏng có vòng béc chỉnh, mở hoàn toàn trong 10% áp vượt",
        [(("vòng béc chỉnh blowdown", "adjustable nozzle ring"), (226, 300)),
         (("mở hoàn toàn ở 10% áp vượt", "full lift at 10% overpressure"),
          (200, 270)),
         (("hoạt động ổn định dải rộng", "stable over a wide range"),
          (266, 300)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, nozzle_ring=True),
        "Crosby Valve &amp; Gage Company, Wrentham, MA.")


@_reg10
def fig_vsh_5_14():
    return _prv_fig(
        14, "Balanced liquid relief valve with friction ring to prevent chatter",
        "Van xả chất lỏng cân bằng có vòng ma sát chống rung",
        [(("O-ring dưới: vòng cản", "lower O-ring drag ring"), (200, 258)),
         (("O-ring trên: chỗ kín cân bằng", "upper O-ring balanced seal"),
          (200, 208)),
         (("lỗ dẫn áp qua đĩa và cần", "bore holes through disc and stem"),
          (236, 268)),
         (("lỗ thông hơi nắp", "bonnet vent"), (268, 168))],
        _prv_ops(vent_bonnet=True, friction_ring=True),
        "Anderson, Greenwood &amp; Co.")


@_reg10
def fig_vsh_5_15():
    return _prv_fig(
        15, "Proportional relief valve with linear opening characteristic",
        "Van xả tỉ lệ có đặc tính mở tuyến tính",
        [(("béc loe dần", "flared nozzle outlet"), (240, 292)),
         (("thay đổi lưu lượng chỉ dịch đĩa ít", "small disc motion per flow "
           "change"), (200, 270)),
         (("ma sát trong đủ để chặn dao động", "internal friction checks "
           "oscillation"), (168, 244)),
         (("lò xo", "spring"), (200, 126))],
        _prv_ops(vent_bonnet=True, proportional=True), "Sempell A.G.")


# ------------------------------------------------------------------- charts
def _chart(ten, tvi, curves, xlab, ylab, points=(), panel=False, note=""):
    """Editorial force/lift-type chart; curves are normalized, not data."""
    x0, y0, pw, ph = 68.0, 46.0, 360.0, 252.0
    o = [_rect(x0, y0, pw, ph, "#ffffff", 1.2, stroke=INK)]
    for i in range(5):
        xx = x0 + i * pw / 4.0
        yy = y0 + i * ph / 4.0
        o.append(_line(xx, y0, xx, y0 + ph, 0.5, color="#d8d5cc"))
        o.append(_line(x0, yy, x0 + pw, yy, 0.5, color="#d8d5cc"))
    o.append(_txt(x0, y0 - 10, ylab, 7.4, anchor="start", color=INK,
                  weight="bold"))
    o.append(_txt(x0 + pw / 2, y0 + ph + 26, xlab, 8.0, color=INK,
                  weight="bold"))
    for pts, col, dash in curves:
        p = [(x0 + a * pw, y0 + ph - b * ph) for a, b in pts]
        o.append(_poly(p, "none", 1.8, col, dash, False))
    for lab, ax, ay in points:
        cx, cy = x0 + ax * pw, y0 + ph - ay * ph
        o.append(_circle(cx, cy, 7.5, sw=1.0, color=INK))
        o.append(_txt(cx, cy - 0.5, lab, 8.0, weight="bold"))
    if panel:
        o.append(_txt(x0 + pw / 2, y0 + ph + 46, note, 6.8, color=GREY))
    else:
        o.append(_txt(476, 54, note, 6.4, color=GREY))
    return o


@_reg10
def fig_vsh_5_16():
    ten = "Opening and closing characteristic of a proportional relief valve"
    tvi = "Đặc tính mở và đóng của van xả tỉ lệ"
    o = _chart(ten, tvi,
               [([(0, .06), (.2, .22), (.5, .52), (.8, .8), (1, .94)], INK, ""),
                ([(0, .04), (.2, .18), (.5, .46), (.8, .74), (1, .90)], BLUE, "4 3")],
               "Nâng van / Valve lift", "Lưu lượng tương đối / Relative flow",
               note="Mở / opening")
    o += [_line(446, 80, 462, 80, 1.8, INK),
          _txt(466, 84, "mở / opening", 6.2, anchor="start"),
          _line(446, 102, 462, 102, 1.8, BLUE, "4 3"),
          _txt(466, 106, "đóng / closing", 6.2, anchor="start"),
          _txt(476, 366, "Sempell A.G.", 6.4, color=GREY)]
    return _prv_fig(16, ten, tvi, [], [], "Sempell A.G.", extra=o)


@_reg10
def fig_vsh_5_29():
    ten = "Force/lift diagram: decaying lifting force from inlet line loss"
    tvi = "Đồ thị lực/nâng: lực nâng suy giảm do tổn thất đường vào"
    o = _chart(ten, tvi,
               [([(0, .78), (.3, .70), (.6, .36), (1, .12)], INK, ""),
                ([(0, .64), (.3, .58), (.6, .29), (1, .08)], GREEN, ""),
                ([(0, .40), (.3, .35), (.6, .18), (1, .04)], "#b45309", ""),
                ([(0, .18), (1, .58)], GREY, "5 3")],
               "Nâng van / Valve lift", "Lực / Force",
               note="3% inlet loss: full lift in one stroke")
    o += [_line(446, 80, 462, 80, 1.6, INK),
          _txt(466, 84, "0% loss", 6.2, anchor="start"),
          _line(446, 100, 462, 100, 1.6, GREEN),
          _txt(466, 104, "1%", 6.2, anchor="start"),
          _line(446, 120, 462, 120, 1.6, "#b45309"),
          _txt(466, 124, "3%", 6.2, anchor="start"),
          _line(446, 140, 462, 140, 1.2, GREY, "5 3"),
          _txt(466, 144, "lò xo / spring", 6.2, anchor="start"),
          _txt(476, 366, "Sempell A.G.", 6.4, color=GREY)]
    return _prv_fig(29, ten, tvi, [], [], "Sempell A.G.", extra=o)


@_reg10
def fig_vsh_5_30():
    ten = "Force/lift diagram: built-up back pressure reduces lifting force"
    tvi = "Đồ thị lực/nâng: áp suất ngược tích tụ làm giảm lực nâng"
    o = _chart(ten, tvi,
               [([(0, .80), (.3, .72), (.6, .38), (1, .14)], INK, ""),
                ([(0, .68), (.3, .60), (.6, .30), (1, .10)], BLUE, ""),
                ([(0, .52), (.3, .44), (.6, .22), (1, .06)], "#b45309", ""),
                ([(0, .18), (1, .58)], GREY, "5 3")],
               "Nâng van / Valve lift", "Lực / Force",
               note="Zero inlet line loss")
    o += [_line(446, 80, 462, 80, 1.6, INK),
          _txt(466, 84, "0% back", 6.2, anchor="start"),
          _line(446, 100, 462, 100, 1.6, BLUE),
          _txt(466, 104, "medium", 6.2, anchor="start"),
          _line(446, 120, 462, 120, 1.6, "#b45309"),
          _txt(466, 124, "high", 6.2, anchor="start"),
          _txt(466, 148, "superimpose with 5-29", 6.0, anchor="start",
               color=GREY),
          _txt(476, 366, "Sempell A.G.", 6.4, color=GREY)]
    return _prv_fig(30, ten, tvi, [], [], "Sempell A.G.", extra=o)


@_reg10
def fig_vsh_5_31():
    ten = "Force/lift diagrams for two blowdown adjustment devices"
    tvi = "Đồ thị lực/nâng cho hai cơ cấu chỉnh blowdown"
    o = _chart(ten, tvi,
               [([(0, .76), (.3, .66), (.6, .32), (1, .16)], INK, ""),
                ([(0, .52), (.3, .46), (.6, .24), (1, .10)], BLUE, ""),
                ([(0, .18), (1, .58)], GREY, "5 3")],
               "Nâng van / Valve lift", "Lực / Force", panel=True,
               note="(a) guide ring — longer blowdown, lower popping pressure"
                    "    (b) nozzle ring — longer blowdown, higher popping "
                    "pressure")
    o += [_line(446, 82, 462, 82, 1.6, INK),
          _txt(466, 86, "(a) guide", 6.2, anchor="start"),
          _line(446, 104, 462, 104, 1.6, BLUE),
          _txt(466, 108, "(b) nozzle", 6.2, anchor="start"),
          _txt(476, 366, "Sempell A.G.", 6.4, color=GREY)]
    return _prv_fig(31, ten, tvi, [], [], "Sempell A.G.", extra=o)


@_reg10
def fig_vsh_5_32():
    ten = "Force/lift diagram: valves that pop fully open in one stroke"
    tvi = "Đồ thị lực/nâng: van mở bật hoàn toàn trong một nhịp"
    o = _chart(ten, tvi,
               [([(0, .14), (.10, .52), (.16, .72), (.5, .84), (1, .78)], INK, ""),
                ([(0, .18), (1, .58)], GREY, "5 3")],
               "Nâng van / Valve lift", "Lực / Force",
               points=[("A", .02, .20), ("B", .09, .48), ("C", .20, .74),
                       ("D", .62, .82), ("S", .78, .70), ("E", .16, .34)],
               note="Typical only — inlet loss 3%")
    o.append(_txt(476, 366, "Editorial / biên tập", 6.4, color=GREY))
    return _prv_fig(32, ten, tvi, [], [], "", extra=o)


@_reg10
def fig_vsh_5_33():
    ten = "Force/lift diagram: valves pop partly then modulate open"
    tvi = "Đồ thị lực/nâng: van mở bật một phần rồi tiếp tục mở điều tiết"
    o = _chart(ten, tvi,
               [([(0, .14), (.08, .44), (.22, .62), (.6, .78), (1, .80)], INK, ""),
                ([(0, .18), (1, .58)], GREY, "5 3")],
               "Nâng van / Valve lift", "Lực / Force",
               points=[("A", .02, .20), ("B", .09, .44), ("D", .70, .78),
                       ("S", .82, .68), ("E", .18, .34)],
               note="Typical only — lift/pressure per API RP 520 Fig. 22")
    o.append(_txt(476, 366, "Editorial / biên tập", 6.4, color=GREY))
    return _prv_fig(33, ten, tvi, [], [], "", extra=o)


# ---------------------------------------------------------- vacuum relief
def _vac_ops(kind="vacuum"):
    o = []
    o.append(("poly", [(-96, 84), (-70, 74), (70, 74), (96, 84),
                       (96, 136), (70, 146), (-70, 146), (-96, 136)],
              BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 96, 90), (sx * 104, 90),
                           (sx * 104, 130), (sx * 96, 130)],
                  RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-84, 96), (84, 96), (84, 126), (-84, 126)],
              "#ffffff", 1.0, INK, "", True))
    if kind == "breather":
        for sx in (-1, 1):
            o.append(("circ", sx * 22, 78, 4, 1.1, INK, RING_F))
            o.append(("poly", [(sx * 22, 76), (sx * 58, 52),
                               (sx * 62, 58), (sx * 26, 82)],
                      RUBBER_F, 1.2, INK, "", True))
            o.append(("line", sx * 22, 76, sx * 22, 96, 1.0, GREY, "3 2"))
        o.append(("poly", [(-14, 84), (14, 84), (14, 96), (-14, 96)],
                  RING_F, 1.0, INK, "", True))
    else:
        o.append(("poly", [(-26, 74), (26, 74), (26, 96), (-26, 96)],
                  BODY_F, 1.1, INK, "", True))
        o.append(("poly", [(-18, 84), (18, 84), (18, 96), (-18, 96)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(-24, 76), (24, 76), (24, 82), (-24, 82)],
                  RUBBER_F, 1.2, INK, "", True))
        o.append(("line", 0, 78, 0, 36, 1.8, INK, ""))
        o.append(("poly", [(-10, 36), (10, 36), (10, 42), (-10, 42)],
                  RING_F, 1.0, INK, "", True))
        if kind == "combo":
            o.append(("poly", [(-24, 56), (24, 56), (24, 62), (-24, 62)],
                      DISC_F, 1.2, INK, "", True))
            o.append(("line", 0, 58, 0, 20, 1.6, INK, ""))
            o.append(("poly", [(-9, 20), (9, 20), (9, 26), (-9, 26)],
                      RING_F, 1.0, INK, "", True))
    o.append(("line", -70, 110, -34, 110, 1.6, BLUE, ""))
    o.append(("poly", [(-34, 110), (-42, 106.5), (-42, 113.5)],
              BLUE, 0, BLUE, "", True))
    o.append(("line", 34, 110, 70, 110, 1.6, BLUE, ""))
    o.append(("poly", [(70, 110), (62, 106.5), (62, 113.5)],
              BLUE, 0, BLUE, "", True))
    return o


@_reg10
def fig_vsh_5_17():
    return _prv_fig(
        17, "Direct-loaded vacuum relief valve, disc loaded by its own light "
        "weight with sponge-rubber seat and PTFE-coated guide",
        "Van xả chân không trực tiếp, đĩa chỉ tải bằng trọng lượng nhẹ, "
        "chỗ kín cao su xốp và cần dẫn phủ PTFE",
        [(("đĩa nhẹ, chỉ tải bằng trọng lượng", "light disc, weight loaded"),
          (200, 256)),
         (("chỗ kín cao su xốp", "sponge-rubber seat seal"), (232, 274)),
         (("cần dẫn phủ PTFE", "PTFE-coated guide rod"), (200, 216)),
         (("thân ghép được với van xả áp dương", "body combinable with "
           "overpressure valve"), (110, 284))],
        _vac_ops("vacuum"), "Anderson, Greenwood &amp; Co.")


@_reg10
def fig_vsh_5_18():
    return _prv_fig(
        18, "Direct-loaded vacuum/pressure relief valve for sanitary service",
        "Van xả chân không/áp dương trực tiếp cho dịch vụ vệ sinh",
        [(("đĩa xả áp dương", "positive-pressure disc"), (200, 236)),
         (("đĩa xả chân không", "vacuum disc"), (200, 274)),
         (("thiết kế vệ sinh", "sanitary design"), (238, 300)),
         (("dùng cho đồ uống, thực phẩm, dược phẩm",
           "beverage, food and pharmaceutical service"), (110, 284))],
        _vac_ops("combo"), "Crosby Valve &amp; Gage Co.")


@_reg10
def fig_vsh_5_19():
    return _prv_fig(
        19, "Breather valve with separate vacuum and overpressure valves "
        "on point-contact hinges",
        "Van thông hơi có van chân không và van áp dương riêng, bản lề tiếp xúc điểm",
        [(("bản lề tiếp xúc điểm", "point-contact hinge"), (242, 246)),
         (("đĩa mở theo cung tròn", "disc swings in an arc"), (262, 256)),
         (("gioăng màng mềm, đóng lại gần áp cài đặt",
           "soft diaphragm seals, reseat near set pressure"), (160, 236)),
         (("cho bồn chứa áp thấp", "for low-pressure storage tanks"),
          (110, 284))],
        _vac_ops("breather"), "Shand &amp; Jurs.")


# ----------------------------------------------- auxiliary actuator layouts
def _piping_schematic(variant="assisted"):
    o = [_rect(96, 110, 116, 90, "#f5f5f1", 1.2),
         _txt(154, 138, "Van an toàn xả", 8.0, weight="bold"),
         _txt(154, 153, "PRV + lò xo", 7.0, color=GREY),
         _line(96, 155, 44, 155, 1.6, BLUE),
         _txt(44, 149, "áp hệ thống", 6.6, color=GREY)]
    if variant != "unrestricted":
        o += [_line(212, 128, 280, 128, 1.2, INK),
              _rect(280, 106, 74, 44, "#e5eee4", 1.1),
              _txt(317, 126, "Cơ cấu phụ", 7.2, weight="bold"),
              _txt(317, 140, "auxiliary device", 6.4, color=GREY)]
    else:
        o.append(_line(212, 128, 260, 128, 1.2, INK))
    if variant == "assisted":
        o += [_line(354, 128, 430, 128, 1.2, BLUE),
              _rect(430, 108, 84, 40, "#dbe6f0", 1.1),
              _txt(472, 126, "Khí nén", 7.2, weight="bold"),
              _txt(472, 140, "compressed air", 6.4, color=GREY),
              _txt(317, 184, "Mất điện → van làm việc bình thường",
                   7.0, color=GREY)]
    elif variant == "supplementary":
        o += [_line(354, 128, 430, 128, 1.2, BLUE),
              _rect(430, 108, 84, 40, "#dbe6f0", 1.1),
              _txt(472, 126, "Tải bổ sung", 7.2, weight="bold"),
              _txt(472, 140, "supplementary", 6.4, color=GREY),
              _txt(317, 184, "Tháo tải khi áp vượt; hỏng điện → vẫn xả đầy",
                   7.0, color=GREY)]
    else:
        for i, lab in enumerate(("M1", "M2", "M3")):
            yy = 92 + i * 34
            o += [_rect(302, yy, 46, 24, "#dbe6f0", 1.0),
                  _txt(325, yy + 15, lab, 7.4, weight="bold"),
                  _line(348, yy + 12, 392, yy + 12, 1.0, INK)]
        o += [_rect(392, 116, 52, 54, "#e5eee4", 1.1),
              _txt(418, 140, "B", 9.0, weight="bold"),
              _txt(418, 158, "buồng B", 6.2, color=GREY),
              _rect(392, 196, 52, 40, "#f6e6c8", 1.1),
              _txt(418, 216, "H", 9.0, weight="bold"),
              _rect(302, 196, 46, 24, "#dbe6f0", 1.0),
              _txt(325, 211, "M4", 7.4, weight="bold"),
              _line(348, 208, 392, 208, 1.0, INK),
              _txt(300, 256, "M1…M3 đóng, M4 xả H → B tạo tải ép; "
                    "khi xả: M1…M3 mở, M4 cấp H hỗ trợ nâng",
                   6.6, color=GREY)]
    o.append(_txt(300, 320, "Sơ đồ biên tập / editorial schematic",
                  6.6, color=GREY))
    return o


@_reg10
def fig_vsh_5_20():
    return _prv_fig(
        20, "Assisted (anti-chatter) safety relief valve",
        "Van an toàn xả có cơ cấu hỗ trợ chống rung",
        [(("cơ cấu hỗ trợ hở", "assist device deactivated normally"),
          (200, 62)),
         (("lực mở bổ sung không hạn chế", "unrestricted supplementary "
           "opening force"), (200, 116)),
         (("lò xo vẫn là tải chính", "spring remains the main load"),
          (200, 140)),
         (("mất khí nén → không cản trở", "air failure → no interference"),
          (160, 300))],
        _prv_ops(actuator=True), "Crosby Valve &amp; Gage Company, Wrentham, MA.")


@_reg10
def fig_vsh_5_21():
    ten = "Typical control piping of an assisted safety relief valve"
    tvi = "Sơ đồ đường điều khiển điển hình của van an toàn xả có hỗ trợ"
    return _prv_fig(21, ten, tvi, [], [],
                    "Crosby Valve &amp; Gage Company, Wrentham, MA.",
                    extra=_piping_schematic("assisted"))


@_reg10
def fig_vsh_5_22():
    return _prv_fig(
        22, "Supplementary-loaded safety relief valve with restricted load",
        "Van an toàn xả có tải bổ sung hạn chế",
        [(("cơ cấu tạo tải ép bổ sung", "restricted supplementary closing load"),
          (200, 62)),
         (("tải được tháo khi van mở", "load removed when valve opens"),
          (200, 118)),
         (("cơ cấu an toàn toàn cơ khí", "mechanical fail-safe device"),
          (242, 246)),
         (("cần tay nhả tải", "manual release lever"), (160, 216))],
        _prv_ops(actuator=True), "Crosby Valve &amp; Gage Company, Wrentham, MA.")


@_reg10
def fig_vsh_5_23():
    ten = "Typical control piping of a supplementary-loaded safety relief valve"
    tvi = "Sơ đồ đường điều khiển điển hình của van an toàn xả có tải bổ sung"
    return _prv_fig(23, ten, tvi, [], [],
                    "Crosby Valve &amp; Gage Company, Wrentham, MA.",
                    extra=_piping_schematic("supplementary"))


@_reg10
def fig_vsh_5_24():
    ten = ("Safety relief valve with unrestricted supplementary loading and "
           "lift assistance, with control system")
    tvi = "Van an toàn xả có tải bổ sung không hạn chế và hỗ trợ nâng, kèm hệ điều khiển"
    return _prv_fig(24, ten, tvi, [], [], "Sempell A.G.",
                    extra=_piping_schematic("unrestricted"))


@_reg10
def fig_vsh_5_25():
    ten = ("High-pressure, high-capacity safety valve with pneumatic "
           "supplementary loading and/or lift assistance")
    tvi = "Van an toàn áp suất cao, lưu lượng lớn có cơ cấu khí nén tạo tải bổ sung và/hoặc hỗ trợ nâng"
    return _prv_fig(
        25, ten, tvi,
        [(("bộ lò xo đĩa Belleville", "Belleville disc spring stack"),
          (200, 118)),
         (("cơ cấu khí nén phụ", "auxiliary pneumatic actuator"), (200, 60)),
         (("tải bổ sung / hỗ trợ nâng", "supplementary load / lift assist"),
          (200, 164)),
         (("dùng cho nhà máy nhiệt điện và hạt nhân",
           "conventional and nuclear power plants"), (160, 300))],
        _prv_ops(belleville=True, actuator=True), "Sempell AG.")


@_reg10
def fig_vsh_5_26():
    ten = ("High-pressure, high-capacity safety valve with pneumatic "
           "supplementary loading and/or lift assistance")
    tvi = "Van an toàn áp suất cao, lưu lượng lớn có cơ cấu khí nén tạo tải bổ sung và/hoặc hỗ trợ nâng"
    return _prv_fig(
        26, ten, tvi,
        [(("bộ lò xo đĩa Belleville", "Belleville disc spring stack"),
          (200, 118)),
         (("cơ cấu khí nén phụ", "auxiliary pneumatic actuator"), (200, 60)),
         (("đế lò xo chịu tải lớn", "heavy-duty spring stack"), (168, 140)),
         (("đĩa và chỗ kín", "disc and seat"), (200, 270))],
        _prv_ops(belleville=True, actuator=True), "Bopp &amp; Reuther.")


# ---------------------------------------------------------- oscillation dampers
@_reg10
def fig_vsh_5_27():
    return _prv_fig(
        27, "Pressure relief valve with dry-friction oscillation damper",
        "Van an toàn xả có bộ giảm dao động ma sát khô",
        [(("phần tử ma sát hình thấu kính", "lens-shaped friction elements"),
          (200, 220)),
         (("than chì điện cứng", "hard electro graphite"), (238, 236)),
         (("ma sát tĩnh thấp, lực gần đều", "low static friction, uniform "
           "force"), (200, 148)),
         (("lò xo nén các phần tử vào cần", "springs press elements onto "
           "stem"), (162, 244))],
        _prv_ops(dry_damper=True), "Bopp &amp; Reuther.")


@_reg10
def fig_vsh_5_28():
    return _prv_fig(
        28, "Pressure relief valve with viscous oscillation damper",
        "Van an toàn xả có bộ giảm dao động nhớt",
        [(("hai trục đồng tâm, khe hở nhỏ", "close-fitting concentric cylinders"),
          (232, 214)),
         (("mỡ nhớt đặc chủng", "special viscous grease"), (200, 236)),
         (("lực tỉ lệ vận tốc", "speed-dependent forces"), (200, 148)),
         (("tự thích ứng theo nhiễu động", "self-adjusting to disturbance"),
          (160, 300))],
        _prv_ops(viscous_damper=True), "Sempell A.G.")


# ----------------------------------------------------------- in-situ testing
@_reg10
def fig_vsh_5_34():
    ten = "Portable device for in-situ verification of valve operating data"
    tvi = "Thiết bị di động kiểm tra dữ liệu vận hành của van tại chỗ"
    extra = [
        _rect(92, 116, 106, 88, "#f5f5f1", 1.2),
        _txt(145, 142, "Van an toàn", 7.8, weight="bold"),
        _txt(145, 157, "PRV", 7.0, color=GREY),
        _line(198, 160, 262, 160, 1.6, INK),
        _rect(262, 126, 76, 70, "#dbe6f0", 1.2),
        _txt(300, 152, "Xi lanh", 7.6, weight="bold"),
        _txt(300, 168, "khí nén", 6.8, color=GREY),
        _line(338, 160, 392, 160, 1.4, BLUE),
        _rect(392, 128, 106, 64, "#e5eee4", 1.2),
        _txt(445, 152, "Máy tính + máy in", 7.4, weight="bold"),
        _txt(445, 168, "laptop + printer", 6.6, color=GREY),
        _line(145, 204, 145, 246, 1.2, INK, "4 3"),
        _txt(145, 260, "lực nâng đo được / measured lift force", 6.6,
             color=GREY),
        _txt(300, 300, "Không cần áp hệ thống; thử tại ≥ 80% áp cài đặt "
             "để đọc đặc tính", 6.8, color=GREY),
        _txt(300, 320, "Sơ đồ biên tập / editorial schematic", 6.6,
             color=GREY),
        _txt(476, 366, "Sempell A.G.", 6.4, color=GREY),
    ]
    return _prv_fig(34, ten, tvi, [], [], "Sempell A.G.", extra=extra)
