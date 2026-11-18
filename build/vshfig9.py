# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 12 — Check Valves (book ch. 4,
Figures 4-1 … 4-15).  Each function returns the standard 5-tuple
(svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology and variant features named in the original captions; a
numbered bilingual legend carries the feature names.  Open-position flow
arrows are editorial additions showing the direction that operates the
valve; they are not part of the original photographs.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, PACK_F, RING_F, _ell, _emit, _emit_legend)

FIGS9 = {}


def _reg9(f):
    FIGS9[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
DISC_F = "#d9d9d2"
RUBBER_F = "#c9d5c9"
PTFE_F = "#dfe8dd"


def _fig9(num, ten, tvi, marks, ops, courtesy="", sub="", rot=0.0,
          w=560, h=380, xleg=402, extra=()):
    o2 = []
    _emit(o2, ops, rot=rot, cx=0.0, cy=100.0, dx=200, dy=180)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "Hình 4-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 4-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _flow(o, x1, y1, x2, y2):
    """Rightward blue flow arrow."""
    o.append(("line", x1, y1, x2, y2, 1.6, BLUE, ""))
    o.append(("poly", [(x2, y2), (x2 - 8, y2 - 3.5), (x2 - 8, y2 + 3.5)],
              BLUE, 0, BLUE, "", True))


def _upflow(o, x, y1, y2):
    o.append(("line", x, y1, x, y2, 1.6, BLUE, ""))
    o.append(("poly", [(x, y2), (x - 3.5, y2 + 8), (x + 3.5, y2 + 8)],
              BLUE, 0, BLUE, "", True))


def _spring(o, x, y1, y2, turns=5):
    pts = [(x, y1)]
    for i in range(turns * 2):
        pts.append((x + (-6 if i % 2 else 6), y1 + (y2 - y1) * (i + 1) / (turns * 2.0)))
    pts.append((x, y2))
    o.append(("poly", pts, "none", 1.0, INK, "", False))


# ------------------------------------------------------------- lift check
def _lift_ops(pattern="standard", disc="piston", dashpot=False,
              spring=False, gas=False, combined=False, lift=0.0):
    """Lift check valve; seat plane at local y=110, flow left to right."""
    o = []
    if pattern == "angle":
        body = [(-96, 66), (-70, 58), (-36, 40), (-20, 30), (20, 30),
                (36, 40), (36, 8), (-36, 8), (-70, 58), (-96, 134),
                (-70, 142), (-30, 148), (30, 148), (70, 142), (96, 134),
                (96, 66), (70, 58)]
        o.append(("poly", body, BODY_F, 1.3, INK, "", True))
        o.append(("poly", [(-28, 8), (28, 8), (28, 0), (-28, 0)],
                  RING_F, 1.2, INK, "", True))
        o.append(("poly", [(-18, 24), (18, 24), (18, 112), (-18, 112)],
                  "#ffffff", 1.0, INK, "", True))
        out_y = None
    elif pattern == "oblique":
        body = [(-96, 78), (-70, 68), (-36, 50), (-18, 44), (18, 34),
                (60, 34), (96, 52), (96, 112), (70, 128), (30, 142),
                (-30, 152), (-70, 142), (-96, 128)]
        o.append(("poly", body, BODY_F, 1.3, INK, "", True))
        o.append(("poly", [(96, 48), (104, 48), (104, 86), (96, 86)],
                  RING_F, 1.2, INK, "", True))
        out_y = 67
    else:
        body = [(-96, 66), (-70, 58), (-34, 38), (-18, 32), (18, 32),
                (34, 38), (70, 58), (96, 66), (96, 134), (70, 142),
                (34, 148), (-34, 148), (-70, 142), (-96, 134)]
        o.append(("poly", body, BODY_F, 1.3, INK, "", True))
        o.append(("poly", [(96, 52), (104, 52), (104, 90), (96, 90)],
                  RING_F, 1.2, INK, "", True))
        out_y = 71

    # ports and throat
    o.append(("poly", [(-104, 86), (-96, 86), (-96, 122), (-104, 122)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-84, 90), (-18, 90), (-18, 116), (-84, 116)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-18, 56), (18, 56), (18, 116), (-18, 116)],
              "#ffffff", 1.0, INK, "", True))
    if out_y is not None:
        o.append(("poly", [(18, out_y - 14), (84, out_y - 14),
                           (84, out_y + 14), (18, out_y + 14)],
                  "#ffffff", 1.0, INK, "", True))
    # seat
    o.append(("poly", [(-24, 110), (-18, 110), (-18, 118), (-24, 118)],
              RING_F, 1.1, INK, "", True))
    o.append(("poly", [(18, 110), (24, 110), (24, 118), (18, 118)],
              RING_F, 1.1, INK, "", True))

    # closure member
    y = 98.0 - lift
    if disc == "ball":
        o.append(("circ", 0, y - 4, 14, 1.3, INK, DISC_F))
    elif disc == "ring" or gas:
        for r in (5.5, 9.5, 13.0):
            o.append(("circ", 0, y - 4, r, 1.0, INK, "none"))
        o.append(("poly", [(-16, y - 16), (16, y - 16),
                           (16, y - 10), (-16, y - 10)],
                  DISC_F, 1.2, INK, "", True))
    else:
        o.append(("poly", [(-16, y - 12), (16, y - 12),
                           (16, y), (-16, y)],
                  DISC_F, 1.3, INK, "", True))
        if disc == "cone":
            o.append(("poly", [(-5, y - 2), (5, y - 2),
                               (14, y - 30), (-14, y - 30)],
                      DISC_F, 1.1, INK, "", True))

    if disc != "ball" and not gas:
        o.append(("line", -14, 30, -14, y - 12, 1.1, INK, ""))
        o.append(("line", 14, 30, 14, y - 12, 1.1, INK, ""))
        o.append(("line", -20, 30, 20, 30, 1.2, INK, ""))
    if disc != "ball":
        o.append(("line", 0, y - 12, 0, 12, 1.8, INK, ""))
    if spring:
        _spring(o, 0, 16, max(34, y - 20))
    if dashpot:
        o.append(("poly", [(-12, -18), (12, -18), (12, 22), (-12, 22)],
                  RING_F, 1.2, INK, "", True))
        o.append(("poly", [(-7, -8), (7, -8), (7, 22), (-7, 22)],
                  "#ffffff", 0.9, INK, "", True))
        o.append(("line", -7, 4, 7, 4, 0.9, INK, "2 2"))
    if combined:
        o.append(("line", 0, 12, 0, -94, 2.2, INK, ""))
        o.append(("poly", _ell(0, -100, 26, 6), "#e8e8e2", 1.2, INK, "", True))
        o.append(("poly", [(-11, -12), (11, -12), (11, 0), (-11, 0)],
                  PACK_F, 1.0, INK, "", True))

    # operating flow
    _flow(o, -78, 103, -38, 103)
    if pattern == "angle":
        o.append(("line", 0, 104, 0, 34, 1.6, BLUE, ""))
        o.append(("poly", [(0, 34), (-3.5, 42), (3.5, 42)],
                  BLUE, 0, BLUE, "", True))
    else:
        _upflow(o, 0, 96, 74)
        if out_y is not None:
            _flow(o, 32, out_y, 76, out_y)
    return o


@_reg9
def fig_vsh_4_1():
    return _fig9(
        1, "Lift check valve with piston-type disc, standard pattern",
        "Van một chiều kiểu nâng có đĩa piston, kiểu tiêu chuẩn",
        [(("đĩa piston nâng thẳng đứng", "piston disc lifting vertically"),
          (200, 268)),
         (("chỗ kín nằm ngang", "horizontal seat"), (226, 298)),
         (("dẫn hướng đĩa", "disc guide"), (174, 210)),
         (("thân và hai bích", "body and flanges"), (106, 286))],
        _lift_ops(pattern="standard", lift=12.0),
        "Edward Valves Inc.")


@_reg9
def fig_vsh_4_2():
    return _fig9(
        2, "Angle-pattern lift check valve with built-in dashpot acting "
        "during the final closing movement",
        "Van một chiều kiểu nâng dạng góc có bộ giảm chấn tác dụng ở cuối "
        "hành trình đóng",
        [(("đường ra thẳng đứng", "vertical outlet"), (200, 182)),
         (("bộ giảm chấn cuối hành trình", "dashpot in final closing stage"),
          (200, 166)),
         (("đuôi hình nón tiết lưu dần", "conical extension throttling flow"),
          (226, 262)),
         (("không có lò xo đóng", "no closing spring"), (174, 210))],
        _lift_ops(pattern="angle", disc="cone", dashpot=True, lift=10.0),
        "Sempell A.G.")


@_reg9
def fig_vsh_4_3():
    return _fig9(
        3, "Lift check valve with piston-type disc, oblique pattern",
        "Van một chiều kiểu nâng có đĩa piston, kiểu xiên",
        [(("thân kiểu xiên", "oblique-pattern body"), (236, 218)),
         (("đĩa piston", "piston disc"), (200, 268)),
         (("chỗ kín và dẫn hướng", "seat and guide"), (174, 298)),
         (("lắp ngang hoặc thẳng đứng chiều lên", "horizontal or vertical "
           "upflow mounting"), (124, 286))],
        _lift_ops(pattern="oblique", lift=12.0),
        "Edward Valves Inc.")


@_reg9
def fig_vsh_4_4():
    return _fig9(
        4, "Lift check valve with spring-loaded ring-shaped disc",
        "Van một chiều kiểu nâng có đĩa dạng vòng nén bằng lò xo",
        [(("đĩa dạng vòng", "ring-shaped disc"), (200, 262)),
         (("lò xo hỗ trợ đóng", "closing spring"), (200, 198)),
         (("lối dòng hình vòng tại chỗ kín", "ring-shaped seat orifice"),
          (228, 298)),
         (("hành trình nâng ngắn", "short lift"), (172, 210))],
        _lift_ops(pattern="standard", disc="ring", spring=True, lift=9.0),
        "Mannesmann-Meer AG.")


@_reg9
def fig_vsh_4_5():
    return _fig9(
        5, "Lift check valve with ball-type disc, standard pattern",
        "Van một chiều kiểu nâng có đĩa dạng bi, kiểu tiêu chuẩn",
        [(("bi lăn vào chỗ kín", "ball rolls into the seat"), (200, 272)),
         (("không dẫn hướng sát", "no close guidance"), (174, 210)),
         (("tự chỉnh khi đóng", "self-aligning on closing"), (228, 298)),
         (("chỉ lắp ngang", "horizontal mounting only"), (110, 286))],
        _lift_ops(pattern="standard", disc="ball", lift=14.0),
        "Crane Co.")


@_reg9
def fig_vsh_4_6():
    return _fig9(
        6, "Lift check valve for pulsating gas flow, with minimum lift, "
        "low inertia and frictionless guiding",
        "Van một chiều kiểu nâng cho dòng khí xung, hành trình nhỏ nhất, "
        "quán tính thấp và dẫn hướng không ma sát",
        [(("nhiều lỗ chỗ kín hình vòng", "multiple ring-shaped seat orifices"),
          (200, 272)),
         (("đĩa mỏng quán tính thấp", "thin low-inertia plate"), (174, 248)),
         (("lò xo chọn theo chế độ", "spring selected for the duty"),
          (200, 216)),
         (("lắp được mọi chiều, kể cả chiều xuống",
           "any position, including vertical downflow"), (112, 286))],
        _lift_ops(pattern="standard", disc="ring", gas=True, lift=6.0),
        "Hoerbiger Corporation of America.")


@_reg9
def fig_vsh_4_7():
    return _fig9(
        7, "Combined lift check and stop valve with piston-type disc, "
        "oblique pattern",
        "Van kết hợp một chiều kiểu nâng và van chặn, đĩa piston, kiểu xiên",
        [(("cần van tách rời đĩa", "stem detached from the disc"),
          (200, 88)),
         (("nâng cần: làm việc như van một chiều", "stem raised: lift check"),
          (200, 162)),
         (("hạ cần ép đĩa: làm việc như van chặn", "stem down: stop valve"),
          (226, 262)),
         (("thân dạng van cầu xiên", "oblique globe-shaped body"),
          (236, 218))],
        _lift_ops(pattern="oblique", lift=10.0, combined=True),
        "Edward Valves Inc.")


# ------------------------------------------------------------- swing check
def _swing_ops(kind="single", spring=False):
    o = []
    o.append(("poly", [(-96, 72), (-70, 62), (70, 62), (96, 72),
                       (96, 136), (70, 146), (-70, 146), (-96, 136)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-104, 82), (-96, 82), (-96, 126), (-104, 126)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(96, 82), (104, 82), (104, 126), (96, 126)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-84, 86), (84, 86), (84, 124), (-84, 124)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(34, 86), (42, 86), (42, 124), (34, 124)],
              RING_F, 1.1, INK, "", True))
    o.append(("circ", 38, 66, 5, 1.1, INK, RING_F))
    if kind == "double":
        o.append(("line", 0, 88, 0, 122, 1.2, INK, ""))
        for sy in (-1, 1):
            yy = 105 + sy * 15
            o.append(("poly", [(2, yy), (34, yy - 24),
                               (34, yy - 16), (2, yy + 8)],
                      DISC_F, 1.2, INK, "", True))
            _spring(o, 20, yy - 34, yy - 20, 3)
    else:
        o.append(("poly", [(38, 64), (76, 98), (72, 106), (34, 72)],
                  RUBBER_F if kind == "rubber" else DISC_F, 1.3, INK, "", True))
        o.append(("line", 38, 70, 38, 122, 1.0, GREY, "3 2"))
        if kind == "rubber":
            o.append(("line", 38, 66, 38, 148, 2.0, RUBBER_F, ""))
            o.append(("line", 38, 130, 38, 146, 1.0, INK, "3 2"))
            o.append(("line", 38, 74, 38, 118, 0.8, INK, ""))
        if spring:
            _spring(o, 62, 68, 92, 4)
    _flow(o, -76, 105, -8, 105)
    _flow(o, 50, 105, 76, 105)
    return o


@_reg9
def fig_vsh_4_8():
    return _fig9(
        8, "Swing check valve", "Van một chiều kiểu đĩa quay bản lề",
        [(("đĩa quay quanh bản lề ngoài chỗ kín",
           "disc swings about a hinge outside the seat"), (244, 232)),
         (("vị trí đóng (nét đứt)", "closed position (dashed)"), (238, 300)),
         (("chỗ kín", "seat"), (238, 286)),
         (("thân và bích", "body and flanges"), (106, 286))],
        _swing_ops(), "Velan Engineering, Limited.")


@_reg9
def fig_vsh_4_9():
    return _fig9(
        9, "Swing check valve with steel-reinforced rubber disc integral "
        "with the body gasket",
        "Van một chiều kiểu đĩa quay có đĩa cao su gia cố thép, một khối "
        "với gioăng thân",
        [(("đĩa là một phần của gioăng thân",
           "disc integral with the body gasket"), (244, 230)),
         (("dải cao su uốn để mở/đóng", "bending rubber strip"), (238, 314)),
         (("cốt thép gia cố", "steel reinforcement"), (268, 246)),
         (("thân chia đôi", "split body"), (124, 286))],
        _swing_ops(kind="rubber"),
        "Saunders Valve Company Limited.")


@_reg9
def fig_vsh_4_10():
    return _fig9(
        10, "Double-disc swing check valve with two spring-loaded "
        "D-shaped discs on a rib",
        "Van một chiều kiểu đĩa quay kép có hai đĩa chữ D nén lò xo trên một gân",
        [(("hai đĩa chữ D", "two D-shaped discs"), (244, 230)),
         (("gân giữa thân", "rib across the bore"), (200, 286)),
         (("nén lò xo, đáp ứng nhanh", "spring loaded, fast response"),
          (268, 268)),
         (("đường đi ngắn hơn, nhẹ hơn khoảng 50%",
           "shorter travel, about 50% lighter"), (110, 286))],
        _swing_ops(kind="double", spring=True),
        "Mission Manufacturing Co.")


# ---------------------------------------------------------- tilting-disc
@_reg9
def fig_vsh_4_11():
    o = []
    o.append(("poly", [(-96, 72), (-70, 62), (70, 62), (96, 72),
                       (96, 136), (70, 146), (-70, 146), (-96, 136)],
              BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 96, 82), (sx * 104, 82),
                           (sx * 104, 126), (sx * 96, 126)],
                  RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-84, 86), (84, 86), (84, 124), (-84, 124)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(18, 86), (26, 86), (26, 124), (18, 124)],
              RING_F, 1.1, INK, "", True))
    o.append(("circ", 22, 70, 5, 1.1, INK, RING_F))
    o.append(("poly", [(22, 68), (70, 92), (66, 100), (18, 76)],
              DISC_F, 1.3, INK, "", True))
    o.append(("line", 22, 74, 22, 122, 1.0, GREY, "3 2"))
    _spring(o, 46, 66, 88, 4)
    _flow(o, -76, 105, -8, 105)
    _flow(o, 46, 105, 76, 105)
    return _fig9(
        11, "Tilting-disc check valve",
        "Van một chiều kiểu đĩa nghiêng",
        [(("trục quay gần tâm đĩa, lệch khỏi mặt chỗ kín",
           "pivot near disc centre, offset from the seat plane"),
          (222, 250)),
         (("đĩa rơi vào chỗ kín khi đóng", "disc drops into seat on closing"),
          (240, 300)),
         (("lò xo đáp ứng nhanh", "spring for quick response"),
          (246, 246)),
         (("đường đi ngắn của trọng tâm", "short centre-of-gravity travel"),
          (110, 286))],
        o, "Edward Valves Inc.")


# ------------------------------------------------------ diaphragm checks
def _dcheck_ops(kind="cone"):
    o = []
    o.append(("poly", [(-100, 68), (-70, 60), (70, 60), (100, 68),
                       (100, 140), (70, 148), (-70, 148), (-100, 140)],
              BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 108, 82), (sx * 100, 82),
                           (sx * 100, 126), (sx * 108, 126)],
                  RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-88, 84), (88, 84), (88, 126), (-88, 126)],
              "#ffffff", 1.0, INK, "", True))
    if kind == "cone":
        o.append(("poly", [(-46, 116), (48, 88), (48, 120), (-46, 120)],
                  RING_F, 1.1, INK, "", True))
        for x in (-30, -12, 6, 24, 40):
            yy = 112 - (x + 46) * 28.0 / 94.0
            o.append(("circ", x, yy, 2.0, 0.8, INK, "#ffffff"))
        o.append(("poly", [(-46, 110), (0, 78), (48, 84)],
                  RUBBER_F, 1.2, INK, "", True))
        o.append(("line", -46, 112, 48, 86, 1.0, GREY, "3 2"))
    elif kind == "pleat":
        o.append(("poly", [(-24, 92), (30, 92), (30, 120), (-24, 120)],
                  RING_F, 1.1, INK, "", True))
        pts = []
        for i in range(11):
            xx = -70 + i * 12
            pts.append((xx, 106 + (-7 if i % 2 else 7)))
        o.append(("poly", pts, "none", 1.2, INK, "", False))
        o.append(("poly", [(-70, 106), (-24, 106), (-24, 114), (-70, 114)],
                  RUBBER_F, 1.1, INK, "", True))
        o.append(("line", -24, 106, 30, 106, 1.0, GREY, "3 2"))
    else:
        o.append(("poly", [(-84, 90), (84, 90), (84, 120), (-84, 120)],
                  RUBBER_F, 1.2, INK, "", True))
        o.append(("poly", [(34, 90), (84, 90), (84, 104), (34, 104)],
                  "#ffffff", 1.0, INK, "", True))
        for yy in (94, 98, 102):
            o.append(("line", -84, yy, 30, yy, 0.7, "#7d9b7d", ""))
        for x, y in ((-50, 108), (-20, 112), (6, 106)):
            o.append(("circ", x, y, 2.4, 0.8, INK, RING_F))
        o.append(("line", 34, 90, 34, 120, 1.0, GREY, "3 2"))
    _flow(o, -76, 105, 4, 105)
    _flow(o, 40, 105, 76, 105)
    return o


@_reg9
def fig_vsh_4_12():
    return _fig9(
        12, "Diaphragm check valve with cone-shaped diaphragm on a "
        "perforated basket",
        "Van một chiều màng có màng dạng nón trên rổ đục lỗ",
        [(("màng dạng nón", "cone-shaped diaphragm"), (200, 240)),
         (("rổ đỡ đục lỗ", "perforated supporting basket"), (236, 296)),
         (("dòng chảy nâng màng khỏi chỗ kín", "flow lifts diaphragm off seat"),
          (174, 290)),
         (("kẹp giữa hai bích", "clamped between flanges"), (106, 286))],
        _dcheck_ops("cone"), "Northvale Engineering.")


@_reg9
def fig_vsh_4_13():
    return _fig9(
        13, "Diaphragm check valve with ring-shaped pleated diaphragm",
        "Van một chiều màng có màng dạng vòng xếp nếp",
        [(("màng cao su xếp nếp dạng vòng", "pleated annular rubber diaphragm"),
          (172, 286)),
         (("môi tựa lên lõi khi đóng", "lip rests on core when closed"),
          (200, 296)),
         (("mở nếp và co môi, đóng rất nhanh", "pleats open, lip retracts, "
           "fast closing"), (236, 286)),
         (("giới hạn 10 bar và khoảng 74 °C",
           "limited to 10 bar and about 74 °C"), (110, 286))],
        _dcheck_ops("pleat"), "VAG-Armaturen GmbH.")


@_reg9
def fig_vsh_4_14():
    return _fig9(
        14, "Diaphragm check valve with flattened rubber sleeve closure member",
        "Van một chiều màng có cơ cấu đóng là ống cao su ép dẹt",
        [(("đầu ống ép dẹt mở khi có dòng xuôi",
           "flattened sleeve end opens on forward flow"), (240, 282)),
         (("ống cao su gia cố lớp nylon", "sleeve reinforced with nylon plies"),
          (172, 278)),
         (("mặt trong mềm, chịu được rắn lơ lửng",
           "soft bore embeds suspended solids"), (200, 304)),
         ((" DN 3 … DN 3000", "DN 3 … DN 3000"), (110, 286))],
        _dcheck_ops("sleeve"), "Red Valve Company Inc.")


@_reg9
def fig_vsh_4_15():
    o = _dcheck_ops("sleeve")
    # tide-gate context: two water levels and an outfall wall
    o.append(("poly", [(132, 148), (132, 178), (296, 178), (296, 148)],
              "#e8eef2", 0.9, GREY, "", True))
    o.append(("line", 116, 152, 180, 152, 1.6, BLUE, ""))
    o.append(("line", 250, 158, 312, 158, 1.6, BLUE, ""))
    o.append(("poly", [(300, 178), (300, 200), (312, 200), (312, 178)],
              "#d9d9d2", 1.0, INK, "", True))
    return _fig9(
        15, "Flattened-sleeve diaphragm check valve used as a tide gate",
        "Van một chiều ống cao su ép dẹt dùng làm cửa triều",
        [(("ống ép dẹt ngăn nước biển chảy ngược",
           "flattened sleeve blocks reverse tide"), (240, 282)),
         (("nước thượng lưu / xả", "upstream water / discharge"),
          (146, 334)),
         (("mực nước triều phía ngoài", "tidal level downstream"),
          (286, 342)),
         (("thân van trong cống xả", "valve body in the outfall"),
          (110, 286))],
        o, "Red Valve Company, Inc.",
        extra=(_line(296, 316, 382, 330, 1.0, GREY, "4 3"),
               _txt(414, 350, "Cống xả / outfall", 6.8, color=GREY)))
