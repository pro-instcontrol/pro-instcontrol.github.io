# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 7 — Manual Valves III: Wedge Gate Valves
(book ch. 3, Figures 3-34 … 3-48).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology and the variant features named in the original caption;
a numbered bilingual legend carries the feature names.  Figures 3-46…3-48
document a photographed failure — here they are redrawn as labelled
schematics of the damaged parts (not photographic reproductions).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _arrow, _circle, _defs, _f as fmt,
                  _fig, _line, _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, DISC_F, PACK_F, RING_F, _ell, _emit,
                     _emit_legend)


FIGS4 = {}


def _reg4(f):
    FIGS4[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
SEAT_F = "#e2e2dc"
WEDGE_F = "#d9d9d2"
PTFE_F = "#dfe8dd"
RUBBER_F = "#c9d5c9"


# ------------------------------------------------------------ frame builder
def _wedge_ops(wedge="solid", bonnet="bolted", screw="internal",
               seal="packing", guides="ribs", tslot="flow",
               hollow=False, rubber=False, diaphragm=False,
               two_piece=False, flexible=False):
    """Wedge-valve cross-section ops.  Local frame: seat centre (0,0);
    horizontal bore band y 88..114; gate slot and bonnet above."""
    o = []
    # ---------------------------------------------------------- body shell
    top = 54
    body = [(-84, 82), (-60, 64), (-30, 52), (0, top), (30, 52),
            (60, 64), (84, 82), (84, 120), (60, 138), (30, 146),
            (-30, 146), (-60, 138), (-84, 120)]
    o.append(("poly", body, BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 92, 78), (sx * 84, 78), (sx * 84, 124),
                           (sx * 92, 124)], RING_F, 1.2, INK, "", True))
    # bore walls and the sloped metal seat faces
    for sx in (-1, 1):
        o.append(("line", sx * 84, 88, sx * 18, 88, 1.2, INK, ""))
        o.append(("line", sx * 84, 114, sx * 18, 114, 1.2, INK, ""))
        o.append(("poly", [(sx * 18, 85), (sx * 12, 85),
                           (sx * 12, 117), (sx * 18, 117)],
                  SEAT_F, 1.1, INK, "", True))
    # guide ribs / slots and the wedge travel path
    if guides in ("ribs", "machined"):
        for sx in (-1, 1):
            o.append(("line", sx * 32, 48, sx * 32, -36, 1.2, INK, ""))
    elif guides == "slots":
        for sx in (-1, 1):
            o.append(("line", sx * 26, 48, sx * 26, -36, 1.1, INK, "3 2"))
    # --------------------------------------------------------------- wedge
    wy0, wy1 = -66, 74
    if wedge == "solid" or wedge == "plain":
        o.append(("poly", [(-14, wy0), (14, wy0), (22, wy1), (-22, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        if hollow:
            o.append(("poly", [(-9, wy0 + 8), (9, wy0 + 8),
                               (15, wy1 - 10), (-15, wy1 - 10)],
                      BODY_F, 1.0, INK, "", True))
    elif wedge == "flexible":
        # two half-wedges with an integral boss at mid-height
        o.append(("poly", [(-14, wy0), (-2, wy0), (-2, wy1), (-22, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        o.append(("poly", [(2, wy0), (14, wy0), (22, wy1), (2, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        o.append(("poly", [(-12, -6), (12, -6), (12, 18), (-12, 18)],
                  SEAT_F, 1.1, INK, "", True))
    elif wedge == "two-piece":
        # two tapered plates rocking on a separate spacer ring
        o.append(("poly", [(-16, wy0), (-4, wy0), (-3, wy1), (-22, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        o.append(("poly", [(4, wy0), (16, wy0), (22, wy1), (3, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        o.append(("poly", [(-4, -4), (4, -4), (4, 20), (-4, 20)],
                  RING_F, 1.1, INK, "", True))
        o.append(("line", -4, 8, 4, 8, 0.9, INK, ""))
    elif wedge == "rubber":
        o.append(("poly", [(-15, wy0), (15, wy0), (23, wy1), (-23, wy1)],
                  WEDGE_F, 1.3, INK, "", True))
        # stirrup-shaped rubber rings around the rim
        o.append(("poly", [(-23, wy1), (-15, wy1), (-15, wy1 + 7),
                           (-27, wy1 + 7), (-27, wy0 + 16), (-20, wy0 + 16)],
                  RUBBER_F, 1.0, INK, "", False))
        o.append(("poly", [(23, wy1), (15, wy1), (15, wy1 + 7),
                           (27, wy1 + 7), (27, wy0 + 16), (20, wy0 + 16)],
                  RUBBER_F, 1.0, INK, "", False))
    elif wedge == "diaphragm":
        o.append(("poly", [(-15, wy0), (15, wy0), (23, wy1), (-23, wy1)],
                  RUBBER_F, 1.3, INK, "", True))
        # diaphragm separates the mechanism from the fluid
        o.append(("poly", [(-46, -36), (-15, -36), (-15, -26),
                           (15, -26), (15, -36), (46, -36)],
                  RUBBER_F, 1.2, INK, "", False))
    # ------------------------------------------------------- T-slot / stem
    if tslot == "cross":
        o.append(("poly", [(-12, wy0), (12, wy0), (12, wy0 + 9),
                           (-12, wy0 + 9)], "#eee9dd", 1.0, INK, "", True))
    elif tslot == "captured":
        o.append(("circ", 0, wy0 + 6, 5, 1.0, INK, RING_F))
    if diaphragm:
        o.append(("line", 0, wy0, 0, -76, 2.2, INK, ""))
    else:
        o.append(("line", 0, wy0, 0, -148, 2.2, INK, ""))
    # -------------------------------------------------------------- bonnet
    if bonnet not in ("diaphragm",):
        if bonnet == "screwed":
            o.append(("poly", [(-30, -100), (30, -100), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            for k in range(3):
                yy = -50 - k * 4
                o.append(("line", -30, yy, -24, yy, 0.8, INK, ""))
                o.append(("line", 24, yy, 30, yy, 0.8, INK, ""))
        elif bonnet == "bolted":
            o.append(("poly", [(-30, -96), (30, -96), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("poly", [(-38, -50), (38, -50), (38, -42), (-38, -42)],
                      RING_F, 1.1, INK, "", True))
            for bx in (-30, -10, 10, 30):
                o.append(("line", bx, -54, bx, -40, 1.0, INK, ""))
        elif bonnet == "union":
            o.append(("poly", [(-30, -92), (30, -92), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("poly", [(-36, -62), (36, -62), (36, -42), (-36, -42)],
                      RING_F, 1.2, INK, "", True))
            for bx in (-24, 0, 24):
                o.append(("line", bx, -62, bx, -44, 0.8, INK, ""))
        elif bonnet == "clamped":
            o.append(("poly", [(-30, -94), (30, -94), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("poly", [(-40, -58), (-30, -64), (30, -64),
                               (40, -58), (40, -44), (-40, -44)],
                      RING_F, 1.2, INK, "", True))
            for bx in (-34, 34):
                o.append(("line", bx, -70, bx, -40, 1.0, INK, ""))
        elif bonnet == "welded":
            o.append(("poly", [(-30, -96), (30, -96), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("line", -34, -44, -30, -50, 1.0, INK, ""))
            o.append(("line", 34, -44, 30, -50, 1.0, INK, ""))
        elif bonnet == "pressure-seal":
            o.append(("poly", [(-28, -104), (28, -104), (28, -40), (-28, -40)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("poly", [(-40, -56), (-28, -56), (-28, -40), (-40, -40)],
                      RING_F, 1.1, INK, "", True))
            o.append(("poly", [(28, -56), (40, -56), (40, -40), (28, -40)],
                      RING_F, 1.1, INK, "", True))
            for bx in (-34, -14, 14, 34):
                o.append(("line", bx, -60, bx, -36, 0.9, INK, ""))
        elif bonnet == "bolted-neck":
            o.append(("poly", [(-30, -98), (30, -98), (30, -44), (-30, -44)],
                      "#efefe9", 1.2, INK, "", True))
            o.append(("poly", [(-38, -52), (38, -52), (38, -42), (-38, -42)],
                      RING_F, 1.1, INK, "", True))
    # ------------------------------------------------------------- stem seal
    if seal == "packing" and bonnet not in ("diaphragm",):
        o.append(("poly", [(-12, -104), (12, -104), (12, -94), (-12, -94)],
                  PACK_F, 1.0, INK, "", True))
    elif seal == "bellows":
        zz = []
        for i in range(9):
            zz.append(((-6 if i % 2 else 6), -124 + i * 3.4))
        o.append(("poly", zz, "none", 1.1, INK, "", False))
        o.append(("poly", [(-12, -92), (12, -92), (12, -86), (-12, -86)],
                  PACK_F, 1.0, INK, "", True))
    # ------------------------------------------------------------- handwheel
    if screw == "internal":
        # non-rising stem: the thread runs inside the bonnet below the wheel
        zz = []
        for k in range(10):
            zz.append(((-5 if k % 2 else 5), -96 + k * 4.6))
        o.append(("poly", zz, "none", 0.9, INK, "", False))
        o.append(("poly", _ell(0, -154, 30, 7), "#e8e8e2", 1.2, INK, "", True))
        o.append(("circ", 0, -154, 5, 1.2, INK, RING_F))
    else:
        # external (rising) stem + yoke + threads above the bonnet
        o.append(("line", -28, -100, -28, -138, 1.5, INK, ""))
        o.append(("line", 28, -100, 28, -138, 1.5, INK, ""))
        for k in range(6):
            yy = -134 + k * 4
            o.append(("line", -6, yy, 6, yy + 2, 0.8, INK, ""))
        o.append(("poly", _ell(0, -152, 32, 7), "#e8e8e2", 1.2, INK, "", True))
        o.append(("circ", 0, -152, 5, 1.2, INK, RING_F))
    return o


def _wedge_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
               w=560, h=380, dx=200, dy=180, xleg=402):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=dx, dy=dy)
    ay = dy + 101
    o2.append(_line(dx - 118, ay, dx - 96, ay, 1.6, color=BLUE))
    o2.append(_poly([(dx - 96, ay), (dx - 104, ay - 3.5),
                     (dx - 104, ay + 3.5)], fill=BLUE, sw=0, close=True))
    o2.append(_line(dx + 96, ay, dx + 118, ay, 1.6, color=BLUE))
    o2.append(_poly([(dx + 118, ay), (dx + 110, ay - 3.5),
                     (dx + 110, ay + 3.5)], fill=BLUE, sw=0, close=True))
    if sub:
        o2.append(_txt(dx, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "H\u00ecnh 3-%d \u00b7 %s (v\u1ebd l\u1ea1i).%s"
                % (num, tvi, (" Ngu\u1ed3n: " + courtesy) if courtesy else ""),
                "Figure 3-%d \u00b7 %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _m(cfg, sub="", **kw):
    """Shorthand for a redrawn cutaway figure."""
    num, ten, tvi, marks, courtesy = cfg
    return _wedge_fig(num, ten, tvi, marks, _wedge_ops(**kw),
                      courtesy=courtesy, sub=sub)


CRANE = "Crane Co."


# ------------------------------------------------------- plain wedge gates
@_reg4
def fig_vsh_3_34():
    cfg = (34,
           "Wedge gate valve with plain hollow wedge, screwed-in bonnet and "
           "internal screw",
           "Van cửa nêm đĩa rỗng, nắp ren, trục vít trong",
           [(("thân đĩa rỗng", "plain hollow wedge"), (200, 228)),
            (("nắp ren vào thân", "screwed-in bonnet"), (176, 116)),
            (("trục vít trong", "internal screw"), (200, 100)),
            (("chỗ kín kim loại dạng nêm", "tapered metal seatings"),
             (226, 286))],
           CRANE)
    return _m(cfg, wedge="solid", hollow=True, bonnet="screwed",
              screw="internal", tslot="direct")


@_reg4
def fig_vsh_3_35():
    cfg = (35,
           "Wedge gate valve with plain hollow wedge, bolted bonnet and "
           "internal screw",
           "Van cửa nêm đĩa rỗng, nắp bắt bulông, trục vít trong",
           [(("đĩa rỗng", "hollow wedge"), (200, 228)),
            (("nắp bắt bulông", "bolted bonnet"), (176, 116)),
            (("cơ cấu vít trong", "internal screw"), (200, 100)),
            (("dẫn hướng bằng gờ thân", "body guide ribs"), (166, 250))],
           CRANE)
    return _m(cfg, wedge="solid", hollow=True, bonnet="bolted",
              screw="internal", guides="ribs", tslot="direct")


@_reg4
def fig_vsh_3_36():
    cfg = (36,
           "Wedge gate valve with plain solid wedge, union bonnet and "
           "internal screw",
           "Van cửa nêm đặc, nắp khớp nối, trục vít trong",
           [(("đĩa nêm đặc", "plain solid wedge"), (200, 228)),
            (("nắp khớp nối (union)", "union bonnet"), (176, 120)),
            (("rãnh chữ T ngang dòng", "T-slot across the flow"), (200, 116)),
            (("trục vít trong", "internal screw"), (200, 100))],
           CRANE)
    return _m(cfg, wedge="solid", bonnet="union", screw="internal",
              tslot="cross", guides="slots")


@_reg4
def fig_vsh_3_37():
    cfg = (37,
           "Wedge gate valve with clamped bonnet and internal screw",
           "Van cửa nêm với nắp kẹp, trục vít trong",
           [(("nắp kẹp (clamped bonnet)", "clamped bonnet"), (176, 118)),
            (("trục chịu toàn lực đẩy đĩa", "stem carries the full wedge thrust"),
             (200, 240)),
            (("chỉ dùng cho áp thấp", "low-pressure applications only"),
             (168, 288)),
            (("trục vít trong", "internal screw"), (200, 100))],
           CRANE)
    return _m(cfg, wedge="solid", bonnet="clamped", screw="internal",
              tslot="direct")


@_reg4
def fig_vsh_3_38():
    cfg = (38,
           "Wedge gate with plain solid wedge, bolted bonnet and external "
           "screw",
           "Van cửa nêm đặc, nắp bulông, trục vít ngoài",
           [(("đĩa nêm đặc", "plain solid wedge"), (200, 228)),
            (("rãnh chữ T theo dòng", "T-slot in line with flow"), (200, 116)),
            (("nắp bulông", "bolted bonnet"), (176, 120)),
            (("trục vít ngoài (rising stem)", "external (rising) screw"),
             (232, 82))],
           CRANE)
    return _m(cfg, wedge="solid", bonnet="bolted", screw="external",
              tslot="flow", guides="ribs")


@_reg4
def fig_vsh_3_39():
    cfg = (39,
           "Wedge gate with plain solid wedge, welded bonnet, external "
           "screw, bellows stem seal and auxiliary stuffing box seal",
           "Van cửa nêm đặc, nắp hàn, trục vít ngoài, gioăng ống sóng và "
           "hộp đón phụ",
           [(("nắp hàn kín", "welded bonnet"), (176, 116)),
            (("gioăng ống sóng", "bellows stem seal"), (232, 78)),
            (("hộp đón phụ", "auxiliary stuffing box"), (168, 82)),
            (("trục vít ngoài", "external screw"), (200, 238))],
           "Pegler Hattersley Limited.")
    return _m(cfg, wedge="solid", bonnet="welded", screw="external",
              seal="bellows", tslot="flow", guides="ribs")


# ------------------------------------------------------- seat / self-align
@_reg4
def fig_vsh_3_40():
    """Detail: PTFE sealing insert standing proud of the metal seat face."""
    w, h = 560, 340
    o = [_defs()]
    cx = 200
    o.append(_poly([(cx - 60, 60), (cx - 16, 60), (cx - 16, 250),
                    (cx - 60, 250)], fill=SEAT_F, sw=1.3, close=True))
    o.append(_poly([(cx - 16, 76), (cx - 10, 76), (cx - 10, 234),
                    (cx - 16, 234)], fill=PTFE_F, sw=1.0, close=True))
    # wedge face leaning on the insert
    o.append(_poly([(cx + 6, 52), (cx + 34, 52), (cx + 26, 258),
                    (cx + 2, 258)], fill=WEDGE_F, sw=1.3, close=True))
    o.append(_line(cx - 70, 155, cx - 44, 155, 1.4, color=BLUE))
    o.append(_poly([(cx - 44, 155), (cx - 52, 151.5), (cx - 52, 158.5)],
                   fill=BLUE, sw=0, close=True))
    o.append(_txt(cx - 20, 278, "đệm PTFE nhô nhẹ / PTFE insert stands proud",
                  7.0, color=GREY))
    for i, (vi, en) in enumerate([
            ("thân chỗ kín kim loại", "metal seat ring"),
            ("đệm kín PTFE", "PTFE sealing insert"),
            ("mặt nêm", "wedge face")]):
        yy = 70 + i * 40
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx - 38, 100, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 38, 100.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx - 13, 200, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 13, 200.5, "2", 8.0, weight="bold"))
    o.append(_circle(cx + 14, 130, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx + 14, 130.5, "3", 8.0, weight="bold"))
    o.append(_txt(476, 320, CRANE, 6.6, color=GREY))
    return _fig(svg(w, h, "".join(o), "PTFE seat insert detail"),
                "Hình 3-40 · Chỗ kín van cửa nêm với đệm làm kín PTFE "
                "(vẽ lại). Nguồn: Crane Co.",
                "Figure 3-40 · Wedge gate valve seat with PTFE sealing "
                "insert — redrawn. (Courtesy of Crane Co.)",
                "Đệm PTFE trong chỗ kín.", "PTFE sealing insert in the seat.")


@_reg4
def fig_vsh_3_41():
    cfg = (41,
           "Wedge gate valve with flexible wedge, pressure-sealed bonnet "
           "and external screw",
           "Van cửa nêm đĩa linh hoạt, nắp kín áp, trục vít ngoài",
           [(("đĩa nêm hai nửa, tự chỉnh", "flexible self-aligning wedge"),
             (200, 230)),
            (("nắp kín áp", "pressure-sealed bonnet"), (176, 116)),
            (("rãnh chữ T theo dòng", "T-slot in line with flow"), (200, 116)),
            (("trục vít ngoài", "external screw"), (232, 82))],
           CRANE)
    return _m(cfg, wedge="flexible", bonnet="pressure-seal",
              screw="external", tslot="flow", guides="ribs")


@_reg4
def fig_vsh_3_42():
    cfg = (42,
           "Forged wedge gate valve with pressure-sealed bonnet, flexible "
           "wedge with hard-faced grooves sliding on machined body ribs",
           "Van cửa nêm rèn, nắp kín áp, đĩa linh hoạt có rãnh phủ cứng "
           "trượt trên gờ thân gia công",
           [(("rãnh đĩa phủ cứng", "hard-faced wedge grooves"), (166, 234)),
            (("gờ dẫn gia công", "machined body guide ribs"), (166, 264)),
            (("nắp kín áp", "pressure-sealed bonnet"), (176, 116)),
            (("rãnh chữ T ngang dòng", "T-slot across the flow"), (200, 116))],
           "Velan Engineering Ltd.")
    return _m(cfg, wedge="flexible", bonnet="pressure-seal",
              screw="external", tslot="cross", guides="machined")


@_reg4
def fig_vsh_3_43():
    cfg = (43,
           "Wedge gate valve with two-piece wedge, pressure-sealed bonnet "
           "and external screw",
           "Van cửa nêm hai mảnh, nắp kín áp, trục vít ngoài",
           [(("hai mảnh nêm hình nón", "two tapered wedge plates"),
             (200, 230)),
            (("vòng đệm chỉnh mòn", "adjustable spacer ring"), (200, 190)),
            (("lưỡi phủ cứng trong rãnh thân", "hard-faced tongues in body "
             "grooves"), (166, 264)),
            (("nắp kín áp", "pressure-sealed bonnet"), (176, 116))],
           "Edward Valves Inc.")
    return _m(cfg, wedge="two-piece", bonnet="pressure-seal",
              screw="external", tslot="captured", guides="machined")


# ------------------------------------------------------------- rubber seats
@_reg4
def fig_vsh_3_44():
    cfg = (44,
           "Rubber-seated wedge gate valve without cavity in the bottom "
           "of the valve body",
           "Van cửa nêm chỗ kín cao su, không có khoang ở đáy thân",
           [(("vòng cao su hình yên cương", "stirrup-shaped rubber rings"),
             (166, 240)),
            (("không khoang đáy thân", "no bottom body cavity"), (200, 300)),
            (("kín đáy và thành hông", "seals on bottom and sidewalls"),
             (236, 286)),
            (("ép kín mặt chỗ kín phía trên", "wedges onto the upper seats"),
             (236, 262))],
           "VAG-Armaturen GmbH.")
    return _m(cfg, wedge="rubber", bonnet="bolted", screw="external",
              guides="slots", sub="Đáy thân phẳng — chất rắn không bị giam / "
              "Flat body bottom — no pocket for solids")


@_reg4
def fig_vsh_3_45():
    cfg = (45,
           "Rubber-seated wedge gate valve without cavity in the bottom "
           "of the valve body, wedge carried by a diaphragm",
           "Van cửa nêm chỗ kín cao su, không khoang đáy, đĩa do màng đỡ",
           [(("đĩa bọc cao su hoàn toàn", "fully rubber-lined wedge"),
             (200, 232)),
            (("màng ngăn cách cơ cấu và chất lỏng",
              "diaphragm separates mechanism from fluid"), (176, 106)),
            (("đáy đĩa kín vào đáy thân", "wedge bottom seals on body"),
             (236, 286)),
            (("dùng trong công nghiệp hóa chất",
              "widely used in the chemical industry"), (176, 302))],
           "Schmitz &amp; Schulte, D-5093 Burscheid.")
    return _m(cfg, wedge="diaphragm", bonnet="diaphragm", screw="external",
              seal="none", diaphragm=True, guides="none",
              sub="Có thể lót vật liệu chống ăn mòn / May be lined with "
              "corrosion-resistant materials")


# ------------------------------------------------------- failure case study
def _damage_fig(num, title_vi, title_en, parts, marks, courtesy="David Mair."):
    """Labelled schematic redraw of a photographed failure component."""
    w, h = 560, 340
    o = [_defs()]
    for pts, fill in parts:
        o.append(_poly(pts, fill=fill, sw=1.3, close=True))
    for i, (vi, en) in enumerate(marks):
        yy = 60 + i * 36
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_txt(200, 316, "Sơ đồ mô tả hư hỏng — không phải ảnh gốc / "
                  "Damage schematic — not a photographic reproduction",
                  6.8, color=GREY))
    o.append(_txt(476, 330, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, "".join(o), title_en),
                "Hình 3-%d · %s — sơ đồ hư hỏng (vẽ lại). Nguồn: %s"
                % (num, title_vi, courtesy),
                "Figure 3-%d · %s — damage schematic, redrawn. "
                "(Courtesy of %s)" % (num, title_en, courtesy),
                title_vi, title_en)


@_reg4
def fig_vsh_3_46():
    # guide slot of the flexible wedge, with rounded torn corners
    parts = [([(160, 44), (240, 44), (240, 116), (160, 116)], WEDGE_F),
             ([(180, 60), (220, 60), (220, 104), (180, 104)], "#faf9f5"),
             ([(176, 56), (186, 58), (184, 64), (174, 62)], RING_F),
             ([(216, 100), (224, 98), (226, 104), (218, 108)], RING_F)]
    o = [_defs()]
    for pts, fill in parts:
        o.append(_poly(pts, fill=fill, sw=1.3, close=True))
    o.append(_txt(200, 136, "rãnh dẫn bị mòn / worn guide slot", 7.0,
                  color=GREY))
    for i, (vi, en) in enumerate([
            ("cạnh sắc làm rách rãnh", "sharp slot edges tore"),
            ("mòn do cọ xát với gờ thân", "worn by sliding on body rib")]):
        yy = 70 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(180, 60, 7.5, sw=1.2, color=INK))
    o.append(_txt(180, 60.5, "1", 8.0, weight="bold"))
    o.append(_circle(220, 100, 7.5, sw=1.2, color=INK))
    o.append(_txt(220, 100.5, "2", 8.0, weight="bold"))
    o.append(_txt(200, 316, "Sơ đồ mô tả hư hỏng — không phải ảnh gốc / "
                  "Damage schematic — not a photographic reproduction",
                  6.8, color=GREY))
    o.append(_txt(476, 330, "David Mair.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Damaged flexible-wedge guide slots"),
                "Hình 3-46 · Hư hỏng rãnh dẫn của đĩa nêm linh hoạt khi đĩa "
                "xoay và kẹt trong thân van (DN 300 / NPS 12, class 150) "
                "(vẽ lại). Nguồn: David Mair.",
                "Figure 3-46 · Damage to guide slots of a flexible wedge "
                "after the wedge rotated and jammed in the body, DN 300 "
                "(NPS 12) class 150 — schematic redrawn. (Courtesy of "
                "David Mair)",
                "Hư hỏng rãnh dẫn đĩa nêm.",
                "Damaged wedge guide slots.")


@_reg4
def fig_vsh_3_47():
    o = [_defs()]
    o.append(_poly([(160, 56), (250, 56), (250, 76), (160, 76)],
                   fill=RING_F, sw=1.3, close=True))
    # scored / gouged rib surface
    for k in range(7):
        xx = 168 + k * 11
        o.append(_line(xx, 58, xx + 4, 74, 0.9, INK))
    o.append(_line(160, 58, 250, 58, 1.6, INK))
    o.append(_txt(205, 100, "gờ dẫn thân bị xước / scored body guide rib",
                  7.0, color=GREY))
    for i, (vi, en) in enumerate([
            ("bề mặt gờ thô", "rough unmachined rib surface"),
            ("vết xước do cạnh sắc của rãnh", "gouges from the sharp slot")]):
        yy = 145 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(178, 62, 7.5, sw=1.2, color=INK))
    o.append(_txt(178, 62.5, "1", 8.0, weight="bold"))
    o.append(_circle(224, 68, 7.5, sw=1.2, color=INK))
    o.append(_txt(224, 68.5, "2", 8.0, weight="bold"))
    o.append(_txt(200, 316, "Sơ đồ mô tả hư hỏng — không phải ảnh gốc / "
                  "Damage schematic — not a photographic reproduction",
                  6.8, color=GREY))
    o.append(_txt(476, 330, "David Mair.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Damaged body guide ribs"),
                "Hình 3-47 · Hư hỏng gờ dẫn thân van do đĩa nêm xoay và kẹt "
                "(DN 300 / NPS 12, class 150) (vẽ lại). Nguồn: David Mair.",
                "Figure 3-47 · Damage to body guide ribs after the wedge "
                "rotated and jammed, DN 300 (NPS 12) class 150 — schematic "
                "redrawn. (Courtesy of David Mair)",
                "Hư hỏng gờ dẫn thân.", "Damaged body guide ribs.")


@_reg4
def fig_vsh_3_48():
    o = [_defs()]
    # bent stem beside the guide bush
    o.append(_poly([(174, 40), (186, 40), (184, 150), (216, 250),
                    (206, 254), (172, 152)], fill=WEDGE_F, sw=1.3,
                   close=True))
    o.append(_poly([(160, 120), (210, 120), (210, 148), (160, 148)],
                   fill=RING_F, sw=1.2, close=True))
    for k in range(5):
        yy = 162 + k * 16
        o.append(_line(180 + k * 3, yy, 190 + k * 3, yy + 4, 0.9, INK))
    o.append(_txt(206, 286, "trục cong + xước mặt / bent and scored stem",
                  7.0, color=GREY))
    for i, (vi, en) in enumerate([
            ("trục bị uốn cong", "stem bent by the closing thrust"),
            ("xước quanh bạc dẫn", "surface damaged at the guide bush")]):
        yy = 80 + i * 46
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(184, 100, 7.5, sw=1.2, color=INK))
    o.append(_txt(184, 100.5, "1", 8.0, weight="bold"))
    o.append(_circle(190, 134, 7.5, sw=1.2, color=INK))
    o.append(_txt(190, 134.5, "2", 8.0, weight="bold"))
    o.append(_txt(200, 316, "Sơ đồ mô tả hư hỏng — không phải ảnh gốc / "
                  "Damage schematic — not a photographic reproduction",
                  6.8, color=GREY))
    o.append(_txt(476, 330, "David Mair.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Bent and scored valve stem"),
                "Hình 3-48 · Trục van bị cong và xước mặt do cố đóng khi "
                "đĩa nêm đã xoay và kẹt (DN 300 / NPS 12, class 150) "
                "(vẽ lại). Nguồn: David Mair.",
                "Figure 3-48 · Bent stem with surface damage after "
                "attempted closure with the wedge rotated and jammed, "
                "DN 300 (NPS 12) class 150 — schematic redrawn. "
                "(Courtesy of David Mair)",
                "Trục van bị cong và xước.", "Bent and scored valve stem.")
