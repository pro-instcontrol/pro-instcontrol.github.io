# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 14 — Pilot-Operated Pressure Relief Valves
(book ch. 5, Figures 5-35 … 5-44).  Each function returns the standard
5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified bilingual vector
schematics.  The source gives no dimensioned drawings, so no numerical
scales are invented; control-piping layouts are editorial schematics.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, _circle, _defs, _fig, _line,
                  _poly, _txt, svg)
from vshfig3 import (RING_F, _emit, _emit_legend)

FIGS11 = {}


def _reg11(f):
    FIGS11[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
DISC_F = "#d9d9d2"
RUBBER_F = "#c9d5c9"
SPRING_F = "#dcdcd6"
DOME_F = "#eef3f8"
DX, DY = 170, 185
XLEG = 402


def _spring(o, x, y1, y2, turns=5, width=7):
    pts = [(x, y1)]
    for i in range(turns * 2):
        pts.append((x + (-width if i % 2 else width),
                    y1 + (y2 - y1) * (i + 1) / (turns * 2.0)))
    pts.append((x, y2))
    o.append(("poly", pts, "none", 1.2, INK, "", False))


def _arrow(o, x1, y1, x2, y2, color=BLUE, sw=1.6):
    o.append(("line", x1, y1, x2, y2, sw, color, ""))
    a = math.atan2(y2 - y1, x2 - x1)
    for d in (2.55, -2.55):
        o.append(("line", x2, y2,
                  x2 + 8 * math.cos(a + d), y2 + 8 * math.sin(a + d),
                  sw, color, ""))


def _pop_fig(num, ten, tvi, marks, panels=(), extra=(), courtesy="", sub=""):
    o2 = []
    for ops, dx, dy in panels:
        _emit(o2, ops, dx=dx, dy=dy)
    o2.extend(extra)
    if sub:
        o2.append(_txt(200, 356, sub, 6.8, color=GREY))
    _emit_legend(o2, XLEG, marks)
    if courtesy:
        o2.append(_txt(476, 366, courtesy, 6.4, color=GREY))
    return _fig(svg(560, 380, _defs() + "".join(o2), ten),
                "Hình 5-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 5-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


def _system_ops(kind="piston", flowing=False, balanced=False, snap=False,
                modulating=False, drag=False, adjust=False, reverse=False,
                deenergize=False, energize=False, check=False, silencer=False,
                bellows_pilot=False, solenoid=False, bleed=False):
    """Pilot-operated relief valve in a local frame: main valve at x=0,
    pilot at x=145, dome above the closure member."""
    o = []

    # ---- main valve body, inlet and outlet -------------------------------
    o.append(("poly", [(-62, 100), (-62, 38), (-46, 18), (-46, -28),
                       (-30, -44), (30, -44), (46, -28), (46, 18),
                       (62, 38), (62, 100)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-22, 100), (22, 100), (22, 112), (-22, 112)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-30, 112), (30, 112), (30, 120), (-30, 120)],
              BODY_F, 1.2, INK, "", True))
    o.append(("poly", [(62, 18), (86, 18), (86, 50), (62, 50)],
              BODY_F, 1.2, INK, "", True))
    o.append(("poly", [(86, 14), (96, 14), (96, 54), (86, 54)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(-18, 108), (18, 108), (18, 48), (-18, 48)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-18, 48), (88, 48), (88, 18), (-18, 18)],
              "#ffffff", 1.0, INK, "", True))
    o.append(("poly", [(-27, 42), (27, 42), (27, 52), (-27, 52)],
              RING_F, 1.1, INK, "", True))

    # ---- closure member --------------------------------------------------
    if kind == "diaphragm":
        o.append(("poly", [(-40, 30), (-20, 20), (20, 20), (40, 30),
                           (20, 40), (-20, 40)],
                  RUBBER_F, 1.4, INK, "", True))
        o.append(("line", 0, 22, 0, -44, 2.0, INK, ""))
    elif kind == "cylinder":
        o.append(("poly", [(-25, 12), (25, 12), (25, 50), (-25, 50)],
                  DISC_F, 1.3, INK, "", True))
        o.append(("poly", [(-13, -22), (13, -22), (13, 12), (-13, 12)],
                  "#ffffff", 1.1, INK, "", True))
        o.append(("line", 0, -22, 0, -72, 2.0, INK, ""))
    else:
        o.append(("poly", [(-30, -44), (-30, 16), (30, 16), (30, -44)],
                  "none", 1.0, INK, "", True))
        o.append(("poly", [(-24, 14), (24, 14), (24, 48), (-24, 48)],
                  DISC_F, 1.3, INK, "", True))
        o.append(("line", 0, 14, 0, -72, 2.0, INK, ""))
        if drag:
            o.append(("poly", [(-30, 0), (-22, 0), (-22, 10), (-30, 10)],
                      RUBBER_F, 1.0, INK, "", True))
            o.append(("poly", [(30, 0), (22, 0), (22, 10), (30, 10)],
                      RUBBER_F, 1.0, INK, "", True))

    # ---- dome / pressure chamber -----------------------------------------
    o.append(("poly", [(-44, -44), (44, -44), (44, -92), (-44, -92)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(-34, -84), (34, -84), (34, -52), (-34, -52)],
              DOME_F, 0.8, GREY, "", True))
    if adjust:
        o.append(("line", 18, -92, 18, -112, 1.6, INK, ""))
        o.append(("poly", [(10, -112), (26, -112), (26, -106), (10, -106)],
                  RING_F, 1.0, INK, "", True))
    if energize:
        o.append(("line", 0, -72, 0, -96, 1.2, BLUE, ""))
        _arrow(o, 0, -96, 0, -72, BLUE, 1.2)

    # ---- pilot ------------------------------------------------------------
    o.append(("poly", [(112, -96), (178, -96), (178, -28), (112, -28)],
              BODY_F, 1.3, INK, "", True))
    o.append(("line", 124, -88, 124, -36, 1.0, INK, ""))
    o.append(("line", 166, -88, 166, -36, 1.0, INK, ""))
    if bellows_pilot:
        for i in range(4):
            yy = -86 + i * 8
            o.append(("line", 138, yy, 152, yy + 4, 1.0, INK, ""))
            o.append(("line", 152, yy, 138, yy + 4, 1.0, INK, ""))
    else:
        _spring(o, 145, -90, -58, 5, 7)
    o.append(("poly", [(134, -56), (156, -56), (156, -48), (134, -48)],
              DISC_F, 1.1, INK, "", True))
    if solenoid:
        o.append(("poly", [(132, -116), (158, -116), (158, -96), (132, -96)],
                  RING_F, 1.0, INK, "", True))
        o.append(("line", 145, -116, 145, -128, 1.0, GREY, ""))
    if snap:
        o.append(("poly", [(118, -70), (128, -70), (128, -60), (118, -60)],
                  GREEN, 0.8, INK, "", True))
    if modulating:
        o.append(("line", 118, -66, 128, -66, 2.2, GREEN, ""))

    # ---- sense line, vent and flow ---------------------------------------
    o.append(("line", 44, -76, 112, -76, 1.2, INK, ""))
    o.append(("line", 166, -76, 198, -76, 1.2, INK, ""))
    if check:
        o.append(("poly", [(178, -84), (190, -76), (178, -68)],
                  DISC_F, 1.0, INK, "", True))
        o.append(("line", 190, -76, 198, -76, 1.2, INK, ""))
    if flowing:
        _arrow(o, 198, -76, 214, -76, GREY, 1.2)
    else:
        o.append(("line", 198, -84, 198, -68, 1.6, INK, ""))
        o.append(("line", 206, -84, 206, -68, 1.6, INK, ""))
    if bleed:
        o.append(("poly", [(70, -72), (78, -72), (78, -64), (70, -64)],
                  GREEN, 0.8, INK, "", True))
        o.append(("line", 78, -68, 88, -68, 1.0, GREY, "3 2"))

    if reverse:
        _arrow(o, 118, 34, 74, 34, BLUE)
        _arrow(o, 0, 96, 0, 128, BLUE)
    else:
        _arrow(o, 0, 126, 0, 86, BLUE)
        _arrow(o, 66, 34, 104, 34, BLUE)
    if silencer:
        for xx in (84, 88, 92):
            o.append(("line", xx, 20, xx, 48, 1.0, GREY, ""))
    if deenergize:
        o.append(("circ", 198, -104, 7, 1.0, INK, "#ffffff"))
        o.append(("line", 194, -108, 202, -100, 1.0, GREY, ""))
        o.append(("line", 202, -108, 194, -100, 1.0, GREY, ""))
    if energize:
        o.append(("circ", 198, -104, 7, 1.0, INK, DOME_F))
        o.append(("line", 198, -108, 198, -100, 1.0, INK, ""))
        o.append(("line", 194, -104, 202, -104, 1.0, INK, ""))
    if balanced:
        o.append(("line", 178, -88, 190, -88, 1.0, GREY, "4 3"))
        o.append(("line", 190, -88, 190, -76, 1.0, GREY, "4 3"))
    return o


def _installation_ops():
    """Three pilot control lines interlocked around one main valve."""
    o = []

    # main valve at the foot of the control lines
    o.append(("poly", [(100, 262), (240, 262), (240, 320), (100, 320)],
              BODY_F, 1.3, INK, "", True))
    o.append(("poly", [(132, 320), (208, 320), (208, 334), (132, 334)],
              RING_F, 1.2, INK, "", True))
    o.append(("poly", [(150, 280), (190, 280), (190, 306), (150, 306)],
              DISC_F, 1.2, INK, "", True))
    o.append(("line", 170, 280, 170, 262, 2.0, INK, ""))
    _arrow(o, 170, 342, 170, 324, BLUE)

    xs = (74, 170, 266)
    labels = (("P1", "indirect"), ("P2", "indirect"), ("SOL", "solenoid"))
    for x, (tag, kind) in zip(xs, labels):
        o.append(("line", x, 246, x, 132, 1.3, INK, ""))
        o.append(("poly", [(x - 26, 132), (x + 26, 132),
                           (x + 26, 72), (x - 26, 72)],
                  BODY_F, 1.2, INK, "", True))
        o.append(("txt", x, 96, tag, 9.0, INK, "bold"))
        o.append(("txt", x, 112, kind, 6.4, GREY, ""))
        o.append(("line", x - 9, 186, x + 9, 174, 1.4, INK, ""))
        o.append(("line", x + 9, 186, x - 9, 174, 1.4, INK, ""))
        o.append(("line", x, 246, 170, 246, 1.0, GREY, "4 3"))
    o.append(("line", 74, 198, 266, 198, 1.0, GREY, "4 3"))
    return o


# --------------------------------------------------------------- 5-35 … 5-41
@_reg11
def fig_vsh_5_35():
    return _pop_fig(
        35, "Basic layout of a pilot-operated pressure relief valve with "
            "direct-acting pilot",
        "Bố trí cơ bản của van an toàn xả điều khiển bằng pilot tác động trực tiếp",
        [(("buồng áp / dome", "dome chamber"), (170, 115)),
         (("pilot tác động trực tiếp", "direct-acting pilot"), (315, 123)),
         (("đường cảm áp", "pressure sense line"), (248, 109)),
         (("piston đóng", "main piston closure"), (170, 217)),
         (("thông hơi ra khí quyển", "vent to atmosphere"), (375, 109))],
        panels=[(_system_ops(), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_36():
    return _pop_fig(
        36, "Full-bore flanged steel main valve with adjustable stroke bolt "
            "and pressure-actuated drag ring",
        "Van chính thép mặt bích đường kính đầy đủ, bulông chỉnh hành trình "
        "và vòng cản áp",
        [(("béc đường kính đầy đủ", "full-bore nozzle"), (170, 255)),
         (("bulông chỉnh hành trình", "adjustable stroke bolt"), (188, 73)),
         (("vòng cản áp", "pressure-actuated drag ring"), (170, 193)),
         (("mặt bích đầu vào", "flanged inlet"), (170, 301))],
        panels=[(_system_ops(kind="piston", drag=True, adjust=True), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_37():
    return _pop_fig(
        37, "Diaphragm-type main valve with unbalanced flowing pilot; snap or "
            "modulating action, for overpressure or vacuum relief",
        "Van chính kiểu màng với pilot chảy không cân bằng; tác động bật hoặc "
        "điều tiết, dùng xả áp hoặc xả chân không",
        [(("màng làm cơ cấu đóng", "diaphragm closure"), (170, 215)),
         (("pilot chảy không cân bằng", "unbalanced flowing pilot"), (315, 123)),
         (("bật hoặc điều tiết", "snap or modulating action"), (315, 95)),
         (("có thể đấu cho chân không", "piped for vacuum relief"), (170, 255))],
        panels=[(_system_ops(kind="diaphragm", flowing=True, snap=True),
                 DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_38():
    return _pop_fig(
        38, "Diaphragm-type pilot-operated valve for overpressure and vacuum "
            "relief; balanced non-flowing pilot, modulating action",
        "Van điều khiển bằng pilot kiểu màng cho xả áp và xả chân không; "
        "pilot cân bằng không chảy, tác động điều tiết",
        [(("màng làm cơ cấu đóng", "diaphragm closure"), (170, 215)),
         (("pilot cân bằng không chảy", "balanced non-flowing pilot"),
          (315, 123)),
         (("điều tiết theo nhu cầu", "modulating action"), (315, 95)),
         (("khí áp thấp", "low-pressure gas duty"), (170, 301))],
        panels=[(_system_ops(kind="diaphragm", flowing=False, balanced=True,
                             modulating=True), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_39():
    return _pop_fig(
        39, "Piston-type main valve with pilot-balanced non-flowing modulating "
            "pilot for gas, liquid and two-phase fluids",
        "Van chính kiểu piston với pilot điều tiết không chảy, cân bằng cho "
        "khí, chất lỏng và lưu chất hai pha",
        [(("van chính kiểu piston", "piston-type main valve"), (170, 215)),
         (("pilot cân bằng", "pilot-balanced pilot"), (315, 123)),
         (("không chảy, điều tiết", "non-flowing modulating"), (315, 95)),
         (("khí / lỏng / hai pha", "gas / liquid / two-phase"), (170, 301))],
        panels=[(_system_ops(kind="piston", flowing=False, balanced=True,
                             modulating=True), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_40():
    return _pop_fig(
        40, "Pilot non-flowing snap-action valve for gas and steam service, "
            "including dirt, hydrates and high moisture",
        "Van pilot không chảy tác động bật cho khí và hơi, kể cả môi trường "
        "có bụi bẩn, hydrat và độ ẩm cao",
        [(("pilot tác động bật", "snap-action pilot"), (315, 123)),
         (("không chảy", "non-flowing pilot"), (315, 95)),
         (("chịu bẩn và hydrat", "dirt / hydrate service"), (260, 219)),
         (("dải áp và nhiệt rộng", "wide pressure and temperature range"),
          (170, 115))],
        panels=[(_system_ops(kind="piston", flowing=False, snap=True),
                 DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


@_reg11
def fig_vsh_5_41():
    return _pop_fig(
        41, "Pilot non-flowing snap-action valve with reversed flow through "
            "the main valve, built-in damper and dual-pilot option",
        "Van pilot không chảy tác động bật, dòng chảy đảo qua van chính, "
        "có bộ giảm chấn và tùy chọn hai pilot",
        [(("dòng chảy đảo", "reversed main-valve flow"), (260, 219)),
         (("piston nằm trong vùng áp", "piston in the pressure zone"),
          (170, 215)),
         (("bộ giảm chấn tích hợp", "built-in piston damper"), (170, 145)),
         (("điều khiển từ xa / hai pilot", "remote or dual-pilot option"),
          (315, 95))],
        panels=[(_system_ops(kind="piston", flowing=False, snap=True,
                             reverse=True, drag=True), DX, DY)],
        courtesy="Anderson, Greenwood &amp; Co.")


# --------------------------------------------------------------- 5-42 … 5-44
@_reg11
def fig_vsh_5_42():
    return _pop_fig(
        42, "Main valve designed to open on being deenergized, with its "
            "associated pilot, check valve and diffuser silencer",
        "Van chính mở khi mất điện, cùng pilot, van một chiều và bộ "
        "giảm thanh kiểu khuếch tán",
        [(("van một chiều thông buồng áp", "dome-vent check valve"),
          (350, 109)),
         (("pilot lò xo xả ra", "discharging spring-loaded pilot"), (315, 123)),
         (("mở khi mất điện", "deenergize-to-open main valve"), (170, 217)),
         (("bộ giảm thanh khuếch tán", "diffuser-type silencer"), (260, 219))],
        panels=[(_system_ops(kind="piston", check=True, deenergize=True,
                             silencer=True, flowing=True), DX, DY)],
        courtesy="Sempell A.G.")


@_reg11
def fig_vsh_5_43():
    return _pop_fig(
        43, "Typical installation diagram: one main valve with two "
            "indirect-acting pilots and one solenoid control line",
        "Sơ đồ lắp đặt điển hình: một van chính với hai pilot tác động "
        "gián tiếp và một đường điều khiển bằng solenoid",
        [(("van chính", "main valve"), (170, 292)),
         (("pilot tác động gián tiếp", "indirect-acting pilots"), (92, 82)),
         (("van điều khiển solenoid", "solenoid control valve"), (284, 82)),
         (("van cô lập liên khóa", "interlocked isolation valves"),
          (170, 180))],
        panels=[(_installation_ops(), 0, 0)],
        extra=(_txt(74, 96, "P1", 9.0, weight="bold"),
               _txt(74, 112, "indirect", 6.4, color=GREY),
               _txt(170, 96, "P2", 9.0, weight="bold"),
               _txt(170, 112, "indirect", 6.4, color=GREY),
               _txt(266, 96, "SOL", 9.0, weight="bold"),
               _txt(266, 112, "solenoid", 6.4, color=GREY),
               _txt(170, 206, "khóa liên động / interlocked isolation",
                    7.0, color=GREY),
               _txt(170, 46,
                    "Một đường điều khiển cô lập tại một thời điểm / "
                    "one control line isolated at a time", 6.8, color=GREY)),
        courtesy="Sempell A.G.")


@_reg11
def fig_vsh_5_44():
    return _pop_fig(
        44, "Energize-to-open main valve with bellows-sealed pilot, "
            "solenoid assistance and bleed to outlet",
        "Van chính mở khi có điện, pilot kín bằng ống màng, hỗ trợ "
        "bằng solenoid và xì sang đầu ra",
        [(("pilot kín bằng ống màng", "bellows-sealed pilot"), (315, 123)),
         (("thân đóng dạng trụ", "cylindrical closure member"), (170, 215)),
         (("piston trung tâm", "central piston"), (170, 155)),
         (("lỗ xì sang đầu ra", "bleed to outlet"), (260, 219)),
         (("hỗ trợ bằng solenoid", "solenoid assistance"), (315, 90))],
        panels=[(_system_ops(kind="cylinder", energize=True,
                             bellows_pilot=True, solenoid=True,
                             bleed=True), DX, DY)],
        courtesy="Bopp &amp; Reuther.")
