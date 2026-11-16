# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 8 — Manual Valves IV: Plug Valves
(book ch. 3, Figures 3-49 … 3-59).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology and the variant features named in the original caption;
a numbered bilingual legend carries the feature names.  Figure 3-59 is an
editorial schematic of the multiport/transflow sequences described in the
source text (the source caption credits Serck Audco for the configuration).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _arrow, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, DISC_F, PACK_F, RING_F, _ell, _emit,
                     _emit_legend)

FIGS5 = {}


def _reg5(f):
    FIGS5[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
SEAT_F = "#e2e2dc"
PLUG_F = "#d9d9d2"
PTFE_F = "#dfe8dd"
GREASE_F = "#f2ecd9"


# ------------------------------------------------------------ frame builder
def _plug_ops(plug="cylindrical", seal="lubricated", closed=False,
              ports=2, lift=False, balance=False, sleeve=False,
              split=False, eccentric=False, o_ring_seats=False):
    """Plug-valve cross-section ops; centre of plug at local (0, 0)."""
    o = []
    # ------------------------------------------------------------ body shell
    body = [(-88, 76), (-62, 58), (-30, 50), (0, 50), (30, 50),
            (62, 58), (88, 76), (88, 114), (62, 132), (30, 140),
            (-30, 140), (-62, 132), (-88, 114)]
    o.append(("poly", body, BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 96, 72), (sx * 88, 72), (sx * 88, 118),
                           (sx * 96, 118)], RING_F, 1.2, INK, "", True))
    # bore and seat bores
    for sx in (-1, 1):
        o.append(("line", sx * 88, 88, sx * 30, 88, 1.2, INK, ""))
        o.append(("line", sx * 88, 112, sx * 30, 112, 1.2, INK, ""))
    # seat rings / spigots
    if o_ring_seats:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 34, 84), (sx * 24, 84),
                               (sx * 24, 116), (sx * 34, 116)],
                      SEAT_F, 1.1, INK, "", True))
            o.append(("circ", sx * 28, 88, 3.4, 1.0, INK, "#ffffff"))
            o.append(("circ", sx * 28, 112, 3.4, 1.0, INK, "#ffffff"))
    else:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 30, 84), (sx * 24, 84),
                               (sx * 24, 116), (sx * 30, 116)],
                      SEAT_F, 1.1, INK, "", True))
    # ------------------------------------------------------------- the plug
    if plug == "taper":
        pts = [(-22, -66), (22, -66), (30, 70), (-30, 70)]
    elif plug == "inverted":
        pts = [(-30, -70), (30, -70), (22, 66), (-22, 66)]
    elif plug == "eccentric":
        pts = [(-26, -62), (18, -62), (26, 68), (-18, 68)]
    else:
        pts = [(-26, -68), (26, -68), (26, 70), (-26, 70)]
    o.append(("poly", pts, PLUG_F, 1.3, INK, "", True))
    if sleeve:
        o.append(("poly", [(-34, -72), (34, -72), (38, 74), (-38, 74)],
                  PTFE_F, 1.1, INK, "", False))
        for k in range(3):
            yy = -50 + k * 46
            o.append(("line", -35, yy, -31, yy, 0.8, INK, ""))
            o.append(("line", 31, yy, 35, yy, 0.8, INK, ""))
    if split:
        o.append(("line", 0, -67, 0, 69, 1.1, INK, ""))
        o.append(("poly", [(-4, -18), (4, -18), (4, 20), (-4, 20)],
                  RING_F, 1.1, INK, "", True))
        for sx in (-1, 1):
            o.append(("poly", [(sx * 22, 84), (sx * 27, 84),
                               (sx * 27, 116), (sx * 22, 116)],
                      PTFE_F, 1.0, INK, "", True))
    # through port — open = aligned with the bore; closed = turned 90°
    if closed:
        o.append(("poly", [(-8, -54), (8, -54), (8, 54), (-8, 54)],
                  "#ffffff", 1.0, INK, "", True))
    else:
        o.append(("poly", [(-34, 92), (34, 92), (34, 108), (-34, 108)],
                  "#ffffff", 1.0, INK, "", True))
    if ports == 3:
        # second port at right angle, shown for the multiport lift type
        o.append(("poly", [(-8, -54), (8, -54), (8, 54), (-8, 54)],
                  "#ffffff", 1.0, INK, "", True))
    # ------------------------------------------------------------ seal types
    if seal == "lubricated":
        for yy in (-56, -44, 60, 72):
            o.append(("line", -26, yy, 26, yy, 0.9, INK, "3 2"))
        o.append(("line", 0, -68, 0, -24, 1.0, INK, ""))
        o.append(("circ", 0, -30, 3, 1.0, INK, GREASE_F))
    elif seal == "packing":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 26, -70), (sx * 34, -70),
                               (sx * 34, 70), (sx * 26, 70)],
                      PACK_F, 1.0, INK, "", True))
        o.append(("poly", [(-34, 70), (34, 70), (34, 80), (-34, 80)],
                  RING_F, 1.1, INK, "", True))
        o.append(("poly", [(-38, 80), (38, 80), (38, 88), (-38, 88)],
                  RING_F, 1.1, INK, "", True))
    elif seal == "metal":
        for sx in (-1, 1):
            o.append(("line", sx * 24, 86, sx * 30, 86, 1.3, INK, ""))
    elif seal == "ptfe":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 24, 80), (sx * 32, 80),
                               (sx * 32, 120), (sx * 24, 120)],
                      PTFE_F, 1.1, INK, "", True))
    if balance:
        for yy in (-52, 52):
            o.append(("circ", 0, yy, 3.2, 1.0, INK, "#ffffff"))
    # ------------------------------------------------------------ stem / gear
    if lift:
        # hinged lever lifts the plug clear before rotation
        o.append(("line", -46, -76, 46, -76, 1.6, INK, ""))
        o.append(("circ", 0, -76, 4, 1.2, INK, RING_F))
        o.append(("line", 0, -76, 0, -66, 1.6, INK, ""))
    else:
        o.append(("line", 0, -68, 0, -136, 2.2, INK, ""))
        if eccentric:
            o.append(("poly", _ell(6, -148, 28, 7), "#e8e8e2", 1.2, INK,
                      "", True))
            o.append(("circ", 6, -148, 5, 1.2, INK, RING_F))
        else:
            o.append(("poly", _ell(0, -150, 28, 7), "#e8e8e2", 1.2, INK,
                      "", True))
            o.append(("circ", 0, -150, 5, 1.2, INK, RING_F))
        # gland at the top of the body
        o.append(("poly", [(-14, -76), (14, -76), (14, -66), (-14, -66)],
                  PACK_F, 1.0, INK, "", True))
    return o


def _plug_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
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
    return _plug_fig(num, ten, tvi, marks, _plug_ops(**kw),
                     courtesy=courtesy, sub=sub)


# ----------------------------------------------------- cylindrical plug valves
@_reg5
def fig_vsh_3_49():
    cfg = (49,
           "Lubricated cylindrical plug valve",
           "Van phích trụ bôi trơn",
           [(("đường dẫn chất làm kín qua cán phích",
             "sealant passage through the plug shank"), (200, 100)),
            (("rãnh phân bổ chất bôi trơn", "lubricant distributing grooves"),
             (168, 244)),
            (("phích trụ, cổng vuông", "cylindrical plug, rectangular port"),
             (200, 280)),
            (("có thể bơm lại khi vận hành",
             "seal can be restored in service"), (180, 322))],
           "Pegler Hattersley Limited.")
    return _m(cfg, plug="cylindrical", seal="lubricated")


@_reg5
def fig_vsh_3_50():
    cfg = (50,
           "Cylindrical plug valve with packing sleeve",
           "Van phích trụ có ống bọc đệm",
           [(("ống bọc đệm (packing sleeve)", "packing sleeve"), (168, 100)),
            (("đai ốc ép (follower nut)", "follower nut"), (200, 266)),
            (("đệm nén amiang hoặc PTFE đặc", "compressed asbestos or solid "
             "PTFE packing"), (232, 250)),
            (("thắt lại khi van đóng", "retighten only when closed"),
             (176, 320))],
           "Rich. Klinger AG.")
    return _m(cfg, plug="cylindrical", seal="packing",
              sub="Cỡ nhỏ, áp suất và nhiệt độ cao / Small sizes, fairly high "
              "pressure and temperature")


@_reg5
def fig_vsh_3_51():
    cfg = (51,
           "Cylindrical plug valve with expandable split plug",
           "Van phích trụ có phích tách đôi nở ra được",
           [(("phích tách làm hai nửa", "plug split into two halves"),
             (200, 252)),
            (("nêm chỉnh được từ ngoài", "wedge adjusted from outside"),
             (200, 214)),
            (("vòng PTFE hẹp trên mặt nửa phích",
             "narrow PTFE rings in the plug faces"), (168, 250)),
            (("chặn kép xả trung gian", "double block and bleed"),
             (236, 286))],
           "Langley Alloys Limited.")
    return _m(cfg, plug="cylindrical", seal="metal", split=True,
              sub="Cho dịch vụ thép không gỉ và hợp kim / For stainless and "
              "expensive-alloy duties")


@_reg5
def fig_vsh_3_52():
    cfg = (52,
           "Cylindrical plug valve with O-ring seat seal, shown closed",
           "Van phích trụ chỗ kín O-ring, thể hiện ở vị trí đóng",
           [(("O-ring trên mỏm cổng", "O-rings on the port spigots"),
             (168, 264)),
            (("phích ở vị trí đóng", "plug in the closed position"),
             (200, 240)),
            (("áp chất lỏng ép O-ring hạ lưu",
             "fluid pressure forces the downstream O-ring onto the plug"),
             (236, 282)),
            (("chủ yếu cho hệ thủy lực áp cao",
             "mainly for high-pressure hydraulic systems"), (168, 322))],
           "Orseal Limited.")
    return _m(cfg, plug="cylindrical", seal="metal", closed=True,
              o_ring_seats=True)


@_reg5
def fig_vsh_3_53():
    cfg = (53,
           "Cylindrical plug valve with eccentric semi-plug",
           "Van phích trụ có bán phích lệch tâm",
           [(("phích lệch tâm", "eccentric semi-plug"), (200, 252)),
            (("mặt nổi trong thân ăn khớp phích",
             "plug matches a raised face in the body"), (168, 282)),
            (("momen quyết định khả năng làm kín",
             "sealing capacity controlled by applied torque"), (234, 100)),
            (("xử lý chất dính", "handles sticky substances"), (180, 322))],
           "DeZurik.")
    return _m(cfg, plug="eccentric", seal="metal", eccentric=True,
              sub="Mặt kín có thể bọc ê-lô-me hoặc nhựa / Seating faces may "
              "be elastomer- or plastic-lined")


# --------------------------------------------------------- taper plug valves
@_reg5
def fig_vsh_3_54():
    cfg = (54,
           "Taper plug valve with unlubricated metal seatings",
           "Van phích côn chỗ kín kim loại không bôi trơn",
           [(("phích hình nón", "tapered plug"), (200, 252)),
            (("chỗ kín kim loại không bôi trơn",
             "unlubricated metal seatings"), (168, 282)),
            (("khe hở tương đối rộng", "relatively wide leakage gap"),
             (236, 296)),
            (("kín tốt với chất lỏng nhớt hoặc sức căng bề mặt cao",
             "seals liquids of high viscosity or surface tension"),
             (176, 324))],
           "Pegler Hattersley Limited.")
    return _m(cfg, plug="taper", seal="metal")


@_reg5
def fig_vsh_3_55():
    cfg = (55,
           "Lubricated taper plug valve",
           "Van phích côn bôi trơn",
           [(("phích côn bôi trơn", "lubricated taper plug"), (200, 252)),
            (("bơm thêm chất làm kín nhấc phích khỏi chỗ kín",
             "extra sealant lifts the plug off its seat"), (168, 282)),
            (("không nới lỏng ty ren khi giải phóng phích",
             "do not slacken the gland to free the plug"), (236, 110)),
            (("có thể tự kẹt nếu siết quá tay",
             "manual overtightening can seize the plug"), (176, 324))],
           "Serck Audco Pty. Ltd.")
    return _m(cfg, plug="taper", seal="lubricated")


@_reg5
def fig_vsh_3_56():
    cfg = (56,
           "Lubricated taper plug valve with inverted, pressure-balanced plug",
           "Van phích côn bôi trơn, phích lật ngược cân bằng áp",
           [(("phích lật ngược, tách khỏi trục",
             "inverted plug divorced from the stem"), (200, 252)),
            (("lỗ cân bằng áp ở hai đầu phích",
             "balance holes at both plug ends"), (168, 282)),
            (("vít trong nắp chỉnh vị trí phích",
             "screw in the cover adjusts the plug"), (200, 106)),
            (("bơm chất làm kín từ đầu trục",
             "sealant injected at the stem end"), (236, 116))],
           "Nordstrom.")
    return _m(cfg, plug="inverted", seal="lubricated", balance=True,
              sub="Dùng cho áp suất rất cao / For very high pressures")


@_reg5
def fig_vsh_3_57():
    cfg = (57,
           "Taper plug valve with PTFE body sleeve",
           "Van phích côn có ống lót thân PTFE",
           [(("ống lót PTFE trong thân", "PTFE body sleeve"), (168, 250)),
            (("phích không bị dính", "sleeve keeps the plug from sticking"),
             (200, 282)),
            (("diện tích kín lớn, chịu hư hỏng bề mặt",
             "large seating area tolerates surface damage"), (236, 296)),
            (("sửa tại hiện trường, không cần xát phích",
             "field repairable, no lapping required"), (176, 324))],
           'Xomox Corporation, "Tupline".')
    return _m(cfg, plug="taper", seal="ptfe", sleeve=True)


@_reg5
def fig_vsh_3_58():
    cfg = (58,
           "Multiport taper plug valve with lift plug",
           "Van phích côn đa cổng có phích nâng",
           [(("cơ cấu bản lề nâng phích trước khi quay",
             "hinged lever lifts the plug before rotation"), (200, 106)),
            (("phích có mặt bọc cao su", "plug may be rubber faced"),
             (200, 252)),
            (("tự khóa nhờ độ côn", "self-locking by its taper"),
             (168, 282)),
            (("dùng cho nhiều cổng, đồng hành van 3-53",
             "multiport companion to the valve of Fig. 3-53"), (176, 324))],
           "DeZurik.")
    return _m(cfg, plug="taper", seal="metal", ports=3, lift=True)


# ------------------------------------------------------------ multiport scheme
@_reg5
def fig_vsh_3_59():
    """Editorial top-view schematic of transflow / non-transflow sequences."""
    w, h = 560, 380
    o = [_defs()]

    def port_row(x, y, label, trans):
        # body circle and three ports: left, right, bottom
        o.append(_circle(x, y, 52, fill=BODY_F, sw=1.3))
        o.append(_rect(x - 78, y - 9, 26, 18, fill=RING_F, sw=1.1))
        o.append(_rect(x + 52, y - 9, 26, 18, fill=RING_F, sw=1.1))
        o.append(_rect(x - 9, y + 52, 18, 26, fill=RING_F, sw=1.1))
        o.append(_txt(x, y - 72, label, 8.0, color=INK, weight="bold"))
        if trans:
            # transflow: the new passage opens while the first is still open
            o.append(_poly([(x - 44, y - 6), (x + 44, y - 6),
                            (x + 44, y + 6), (x - 44, y + 6)],
                           fill="#ffffff", sw=1.1, close=True))
            o.append(_poly([(x - 6, y), (x + 6, y), (x + 6, y + 44),
                            (x - 6, y + 44)], fill="#ffffff", sw=1.1,
                           close=True))
            o.append(_txt(x, y + 86, "cổng mới mở trước / opens first",
                          6.8, color=GREY))
        else:
            o.append(_poly([(x - 44, y - 6), (x + 44, y - 6),
                            (x + 44, y + 6), (x - 44, y + 6)],
                           fill="#ffffff", sw=1.1, close=True))
            o.append(_txt(x, y + 86, "cổng cũ đóng trước / closes first",
                          6.8, color=GREY))

    port_row(130, 150, "Dòng chuyển tiếp · Transflow", True)
    port_row(300, 150, "Không chuyển tiếp · Non-transflow", False)
    for i, (vi, en) in enumerate([
            ("thân van ba cổng", "three-port valve body"),
            ("cổng vào / ra", "inlet / outlet ports"),
            ("cổng chuyển hướng", "diverted port"),
            ("thứ tự đóng – mở", "close / open sequence")]):
        yy = 62 + i * 40
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(130, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(130, 150.5, "1", 8.0, weight="bold"))
    o.append(_circle(78, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(78, 150.5, "2", 8.0, weight="bold"))
    o.append(_circle(300, 202, 7.5, sw=1.2, color=INK))
    o.append(_txt(300, 202.5, "3", 8.0, weight="bold"))
    o.append(_circle(248, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(248, 150.5, "4", 8.0, weight="bold"))
    o.append(_txt(476, h - 14, "Serck Audco Pty. Ltd.", 6.6, color=GREY))
    return _fig(svg(w, h, "".join(o), "Plug valve multiport configurations"),
                "Hình 3-59 · Cấu hình đa cổng của van phích: dòng chuyển tiếp "
                "và không chuyển tiếp (sơ đồ biên tập, vẽ lại). Nguồn: Serck "
                "Audco Pty. Ltd.",
                "Figure 3-59 · Multiport configurations of plug valves — "
                "transflow and non-transflow sequences (editorial schematic, "
                "redrawn). (Courtesy of Serck Audco Pty. Ltd.)",
                "Cấu hình đa cổng: dòng chuyển tiếp và không chuyển tiếp.",
                "Multiport configurations: transflow and non-transflow.")
