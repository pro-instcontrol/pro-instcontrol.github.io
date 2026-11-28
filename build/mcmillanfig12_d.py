# -*- coding: utf-8 -*-
"""Vector redraws of Figures 12.13-12.16 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 12 "increased safety 'e'".

Every drawing is a simplified vector redraw of the authoritative rendered
pages p344 (Fig. 12.13), p347 (Fig. 12.14), p348 (Fig. 12.15) and p349
(Fig. 12.16).  Printed English captions, notes and legend wording are kept
verbatim in the English captions; the captions are prefixed with a Vietnamese
translation.  Two printed OCR quirks are deliberately retained in the English
caption text and explained in the aria descriptions: Fig. 12.15 prints
"t, time determination" (intelligible as "te time determination") and
Fig. 12.16 prints "IJn ratios" and "5 second".  Each public callable returns
the standard five-tuple through ``vfig._fig()`` and is registered in ``FIGS``
by the ``_reg`` decorator.
"""
import sys
import os
import math

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, BLUE, RED, GREEN, _arrow, _circle, _defs,
                  _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.8):
    o.append(T(340, 16, "Hình 12.%d · %s / Figure 12.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, size=6.9):
    o.append(T(340, 29, s, size, color=GREY))


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.85, color=GREY, head="a7")


def _semi(cx, cy, r, n=28):
    """Upper semicircle whose flat side lies on y=cy."""
    pts = []
    for i in range(n + 1):
        a = math.pi - math.pi * i / float(n)
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    return _poly(pts, fill="none", sw=1.3, color=INK)


def _cross(cx, cy, d=10):
    return (_line(cx - d, cy, cx + d, cy, sw=0.9)
            + _line(cx, cy - d, cx, cy + d, sw=0.9))


def _polar_rect(cx, cy, r, a_deg, half_r, half_t, fill, sw=1.0, color=INK):
    """A small rectangle given by radial/tangential half-sizes and an angle."""
    a = math.radians(a_deg)
    ux, uy = math.cos(a), -math.sin(a)
    tx, ty = -uy, ux
    pts = []
    for sr, st in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        rr = r + sr * half_r
        pts.append((cx + rr * ux + st * half_t * tx,
                    cy + rr * uy + st * half_t * ty))
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _polar_dot(cx, cy, r, a_deg, dr, dt, rad=1.6):
    a = math.radians(a_deg)
    ux, uy = math.cos(a), -math.sin(a)
    tx, ty = -uy, ux
    return _circle(cx + r * ux + dr * ux + dt * tx,
                   cy + r * uy + dr * uy + dt * ty, rad, fill=INK, sw=0)


# ------------------------------------------------------------------ 12.13

@_reg
def fig_f1213():
    """Figure 12.13 - resistance heating device mandrel bend test."""
    w, h = 680, 320
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 13, "Thiết bị thử uốn thiết bị gia nhiệt điện trở",
           "Bend-test apparatus for resistance heat devices", 7.8)
    _sub(o, "Cáp hoặc băng mẫu uốn 90° trên trục gá thép · 90° bend on steel mandrels", 7.0)

    # Steel base and the two mandrels.
    o.append(_rect(110, 236, 460, 16, fill="#e9e9e9", sw=1.3))
    o.append(_semi(235, 236, 100))
    o.append(_semi(445, 236, 100))

    # Sample heating cable, tape or mantle: a narrow strip between mandrels.
    o.append(_rect(336, 52, 8, 210, fill="#fff", sw=1.2))
    o.append(_line(340, 54, 340, 264, sw=0.8, dash="4 5", color=GREY))
    o.append(_poly([(336, 52), (338, 49), (342, 49), (344, 52)],
                   fill="#fff", sw=1.0, close=True))
    o.append(_poly([(336, 262), (338, 265), (342, 265), (344, 262)],
                   fill="#fff", sw=1.0, close=True))

    # Minimum bending radius, shown on both mandrels as in the print.
    for cx in (235, 445):
        o.append(_cross(cx, 236))
        o.append(_arrow(cx + 5, 231, cx + 68, 168, sw=1.1, color=BLUE))
        o.append(T(cx + 31, 194, "R", 7.6, color=BLUE, weight="600"))

    # Printed leaders and bilingual labels.
    o.append(T(70, 86, "Cáp gia nhiệt mẫu / Sample heating cable,", 7.0, anchor="start"))
    o.append(T(70, 95, "băng hoặc lớp phủ / tape or mantle", 7.0, anchor="start"))
    o.append(_lead(252, 92, 334, 118))
    o.append(T(70, 126, "Trục gá thép / Steel mandrel", 7.0, anchor="start"))
    o.append(_lead(180, 132, 185, 148))
    o.append(T(150, 276, "Đế thép / Steel base", 7.0, anchor="start"))
    o.append(_lead(190, 270, 200, 246))

    # Printed note below the apparatus.
    o.append(T(340, 299, "R = Bán kính uốn nhỏ nhất do nhà sản xuất quy định", 7.0))
    o.append(T(340, 309, "R = Minimum bending radius specified by the manufacturer", 7.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.13")),
                "Hình 12.13 · Thiết bị thử nghiệm thiết bị gia nhiệt điện trở chịu "
                "ứng suất uốn khi sử dụng. R = Bán kính uốn nhỏ nhất do nhà sản xuất quy định",
                "Figure 12.13 · Test apparatus for resistance heat devices subject to "
                "bending stresses in service. R = Minimum bending radius specified by "
                "the manufacturer",
                "Cáp gia nhiệt mẫu, băng hoặc lớp phủ chạy thẳng đứng giữa hai trục gá "
                "thép bán tròn đặt trên đế thép. Mũi tên R từ tâm mỗi trục tới cung tròn "
                "cho biết bán kính uốn nhỏ nhất do nhà sản xuất quy định. Các nhãn "
                "Sample heating cable, tape or mantle, Steel mandrel và Steel base được "
                "chỉ bằng đường dẫn.",
                "A sample heating cable, tape or mantle runs vertically between two "
                "semicircular steel mandrels seated on a steel base. An R arrow from the "
                "centre cross of each mandrel to its arc marks the minimum bending radius "
                "specified by the manufacturer. Leader lines carry the printed labels "
                "Sample heating cable, tape or mantle, Steel mandrel and Steel base")


# ------------------------------------------------------------------ 12.14

@_reg
def fig_f1214():
    """Figure 12.14 - three-phase squirrel-cage machine cross-section."""
    w, h = 680, 380
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 14, "Máy lồng sóc ba pha điển hình",
           "Typical three-phase squirrel cage machine", 7.8)
    _sub(o, "Mặt cắt ngang · cách điện rãnh, thanh rôto và thiết bị hạn chế nhiệt / "
           "Cross-section with slot insulation and temperature limiting devices", 6.9)

    cx, cy = 340, 196
    o.append(_circle(cx, cy, 124, fill="#fff", sw=1.5))
    o.append(_circle(cx, cy, 88, fill="#f7f7f7", sw=1.3))
    o.append(_circle(cx, cy, 78, fill="#fff", sw=1.2))
    o.append(_circle(cx, cy, 30, fill="#fff", sw=1.2))

    # Stator teeth between the six slots.
    for a in (30, 90, 150, 210, 270, 330):
        rad = math.radians(a)
        ux, uy = math.cos(rad), -math.sin(rad)
        o.append(_line(cx + 88 * ux, cy + 88 * uy, cx + 123 * ux, cy + 123 * uy,
                       sw=0.8, color=GREY))

    # Six insulated stator slots with conductors; temperature-limiting devices
    # sit at the rear of the upper-left and lower-left slots.
    for a in (0, 60, 120, 180, 240, 300):
        o.append(_polar_rect(cx, cy, 104, a, 15, 13, fill="none", sw=0.8, color=GREY))
        o.append(_polar_rect(cx, cy, 104, a, 13, 11, fill="#eef3fb", sw=1.0))
        for dr in (-6, 0, 6):
            for dt in (-6, 0, 6):
                o.append(_polar_dot(cx, cy, 104, a, dr, dt, 1.6))
    o.append(_polar_rect(cx, cy, 116, 120, 4, 8, fill=GREEN, sw=0.8))
    o.append(_polar_rect(cx, cy, 116, 240, 4, 8, fill=GREEN, sw=0.8))

    # Squirrel-cage rotor bars in their slots.
    for a in range(0, 360, 30):
        o.append(_polar_rect(cx, cy, 68, a, 5, 5, fill="#dce6ee", sw=0.9))

    # Printed leader labels, translated first.
    o.append(T(60, 62, "Cách điện rãnh / Slot insulation", 6.8, anchor="start"))
    o.append(T(60, 71, "(Ghi chú 1 / Note 1)", 6.8, anchor="start"))
    o.append(_lead(180, 68, 270, 99))
    o.append(T(240, 50, "Răng stato / Stator tooth", 6.8, anchor="start"))
    o.append(_lead(330, 55, 340, 88))
    o.append(T(470, 60, "Stato / Stator", 6.8, anchor="start"))
    o.append(_lead(466, 66, 422, 98))
    o.append(T(30, 120, "Dây dẫn cách điện /", 6.8, anchor="start"))
    o.append(T(30, 129, "Insulated conductors", 6.8, anchor="start"))
    o.append(_lead(170, 128, 232, 190))
    o.append(T(20, 180, "Vật liệu chèn rãnh /", 6.8, anchor="start"))
    o.append(T(20, 189, "Slot packing securing", 6.8, anchor="start"))
    o.append(T(20, 198, "conductors", 6.8, anchor="start"))
    o.append(_lead(168, 192, 240, 196))
    o.append(T(490, 146, "Thanh rôto/rãnh /", 6.8, anchor="start"))
    o.append(T(490, 155, "Rotor bars/slots (Note 2)", 6.8, anchor="start"))
    o.append(_lead(486, 160, 412, 194))
    o.append(T(520, 270, "Rôto / Rotor", 6.8, anchor="start"))
    o.append(_lead(516, 268, 400, 246))
    o.append(T(60, 308, "Thiết bị hạn chế nhiệt /", 6.8, anchor="start"))
    o.append(T(60, 317, "Temperature-limiting device", 6.8, anchor="start"))
    o.append(_lead(200, 310, 284, 298))

    # Printed notes, condensed onto the drawing in two languages.
    o.append(T(340, 341, "Ghi chú: (1) cảm biến nhiệt trong cách điện rãnh, phía sau rãnh; "
                         "(2) thanh rôto giữ bằng vật liệu dẫn điện hoặc đúc nhôm", 6.8))
    o.append(T(340, 351, "Notes: (1) stator temperature limiting devices inside slot "
                         "insulation at rear of slot; (2) rotor bars secured by conductive "
                         "packing or aluminium casting", 6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.14")),
                "Hình 12.14 · Máy lồng sóc ba pha điển hình. Ghi chú: (1) Thiết bị hạn chế "
                "nhiệt độ stato được lắp bên trong lớp cách điện rãnh ở phía sau rãnh; các "
                "thiết bị này cũng cần được cách điện thỏa đáng. (2) Thanh rôto được giữ "
                "trong các rãnh bằng vật liệu dẫn điện hoặc đúc nhôm",
                "Figure 12.14 · Typical three-phase squirrel cage machine. Notes: (1) "
                "Stator temperature limiting devices fitted inside slot insulation at rear "
                "of slot. These need to be adequately insulated themselves. (2) Rotor bars "
                "secured in slots by conductive packing or aluminium casting",
                "Mặt cắt máy có vỏ stato tròn, sáu rãnh stato có dây dẫn và lớp cách điện, "
                "các răng stato giữa các rãnh, rôto với các thanh dẫn lồng sóc và lỗ trục. "
                "Hai thiết bị hạn chế nhiệt màu xanh nằm ở phía sau rãnh. Các nhãn "
                "Slot insulation (Note 1), Stator tooth, Stator, Insulated conductors, "
                "Slot packing securing conductors, Rotor bars/slots (Note 2) và Rotor đều "
                "có đường dẫn chỉ tới bộ phận tương ứng.",
                "Cross-section of a machine with a circular stator frame, six stator slots "
                "holding insulated conductors, stator teeth between the slots, a squirrel-"
                "cage rotor with its bars and a central shaft hole. Two green temperature "
                "limiting devices sit at the rear of slots. Leader labels mark Slot "
                "insulation (Note 1), Stator tooth, Stator, Insulated conductors, Slot "
                "packing securing conductors, Rotor bars/slots (Note 2) and Rotor")


# ------------------------------------------------------------------ 12.15

@_reg
def fig_f1215():
    """Figure 12.15 - te time determination chart."""
    w, h = 680, 330
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 15, "Xác định thời gian t<sub>e</sub>", "t, time determination", 7.8)
    _sub(o, "Nhiệt độ rôto kẹt · biểu đồ xác định thời gian te / Stalled-rotor temperature rise", 7.0)

    x0, ytop, W, H = 150, 70, 420, 170
    ybot = ytop + H
    yT2, yT1, yT0 = 80, 145, 205
    xX, xR = 430, 570

    # Frame, temperature levels and axis arrows.
    o.append(_rect(x0, ytop, W, H, fill="#fff", sw=1.1))
    for yy in (yT2, yT1, yT0):
        o.append(_line(x0, yy, x0 + W, yy, sw=0.9))
    o.append(_arrow(x0, ybot, x0 + W + 22, ybot, sw=1.0))
    o.append(_arrow(x0, ybot, x0, ytop - 16, sw=1.0))
    o.append(T(136, ytop - 18, "θ / Nhiệt độ", 6.8))
    o.append(T(142, yT2 + 3, "T<sub>2</sub>", 6.8, anchor="end"))
    o.append(T(142, yT1 + 3, "T<sub>1</sub>", 6.8, anchor="end"))
    o.append(T(142, yT0 + 3, "T<sub>0</sub>", 6.8, anchor="end"))
    o.append(T(142, ybot + 2, "0", 6.8, anchor="end"))

    # Dotted pre-stall rise approaching T1, then the X stall line.
    pts = []
    for i in range(15):
        u = (i + 0.5) / 15.0
        pts.append((x0 + 8 + (xX - x0 - 8) * u, yT0 - (yT0 - yT1) * (1 - (1 - u) ** 1.7)))
    for px, py in pts:
        o.append(_circle(px, py, 2.1, fill=INK, sw=0))
    o.append(_line(xX, ytop, xX, ybot, sw=2.4))
    o.append(T(xX, ytop - 9, "X", 7.4, weight="600"))

    # Solid post-stall curve rising towards T2.
    curve = []
    for i in range(29):
        u = i / 28.0
        curve.append((xX + (xR - xX) * u, yT1 - (yT1 - yT2) * (1 - (1 - u) ** 2.0)))
    o.append(_poly(curve, fill="none", sw=1.6))

    # Time arrow and the te interval under the plot.
    o.append(T(175, ybot + 16, "t / thời gian", 6.8))
    o.append(_line(xX, ybot, xX, ybot + 22, sw=0.8))
    o.append(_line(xR, ybot, xR, ybot + 22, sw=0.8))
    o.append(_arrow(xR, ybot + 15, xX + 5, ybot + 15, sw=0.8))
    o.append(_arrow(xX, ybot + 15, xR - 5, ybot + 15, sw=0.8))
    o.append(T((xX + xR) / 2.0, ybot + 33, "t<sub>e</sub>", 7.4, weight="600"))

    # Printed legend, translated first.
    o.append(T(340, 297, "T<sub>0</sub> = Nhiệt độ môi trường cao nhất quy định (thường 40 °C) / "
                         "T0 = Highest specified operating ambient temperature (normally 40 °C)", 6.8))
    o.append(T(340, 309, "T<sub>1</sub> = Nhiệt độ cao nhất ở chế độ định mức tại T0 / "
                         "T1 = Highest temperature reached by machines in rated service at T0", 6.8))
    o.append(T(340, 321, "T<sub>2</sub> = Nhiệt độ giới hạn / Limiting temperature; "
                         "θ = Nhiệt độ / Temperature; t = Thời gian / Time; "
                         "t<sub>e</sub> = te time; X = Điểm rôto kẹt / Rotor stall point", 6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.15")),
                "Hình 12.15 · Xác định thời gian tₑ",
                "Figure 12.15 · t, time determination",
                "Biểu đồ nhiệt độ theo thời gian có ba mức ngang T0, T1 và T2 cùng đường "
                "đáy 0. Đường chấm dần tiến từ T0 tới T1 tại điểm rôto kẹt X; sau X đường "
                "cong liền tăng lên T2. Phía dưới có mũi tên thời gian t và khoảng t<sub>e</sub> "
                "từ X tới cuối biểu đồ. Chú giải ghi T0 là nhiệt độ môi trường cao nhất "
                "quy định (thường 40 °C), T1 là nhiệt độ cao nhất ở chế độ định mức tại T0, "
                "T2 là nhiệt độ giới hạn, θ là nhiệt độ, t là thời gian và X là điểm rôto kẹt. "
                "EN caption retains the printed form 't, time determination', intelligible "
                "as 'te time determination'.",
                "Temperature-time chart with three horizontal levels T0, T1 and T2 above a "
                "zero baseline. A dotted curve rises from T0 towards T1 at the rotor stall "
                "point X; after X a solid curve climbs towards T2. Beneath the plot a time "
                "arrow t and a te interval run from X to the right edge. The legend gives "
                "T0 as highest specified operating ambient temperature (normally 40 °C), "
                "T1 as highest temperature reached by machines in rated service at T0, T2 "
                "as limiting temperature, theta as temperature, t as time and X as rotor "
                "stall point. The printed caption reads 't, time determination', an OCR "
                "form of 'te time determination', and is retained verbatim")


# ------------------------------------------------------------------ 12.16

@_reg
def fig_f1216():
    """Figure 12.16 - minimum permissible te time versus starting-current ratio."""
    w, h = 680, 330
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 16, "Thời gian t<sub>e</sub> tối thiểu cho phép theo tỷ lệ Ia/In",
           "Minimum permissible te times for IJn ratios", 7.8)
    _sub(o, "Đồ thị giới hạn · số giây tối thiểu theo dòng khởi động / Limit curve of minimum seconds", 7.0)

    x0, W = 130, 450
    ymap = [(40, 62), (30, 83), (20, 112), (10, 151), (8, 166), (6, 181),
            (5, 192), (4, 203), (3, 221), (2, 245), (1, 267)]
    xpos = lambda r: x0 + (r - 2) / 8.0 * W

    # Grid: vertical ratio lines and the non-uniform printed time lines.
    for r in range(2, 11):
        o.append(_line(xpos(r), 62, xpos(r), 267, sw=0.7, color=GREY))
    for val, yy in ymap:
        o.append(_line(x0, yy, x0 + W, yy, sw=0.7, color=GREY))
        o.append(T(x0 - 7, yy + 2.4, str(val), 6.8, anchor="end"))
    for r in range(2, 11):
        o.append(T(xpos(r), 281, str(r), 6.8))
    o.append(_rect(x0, 62, W, 205, fill="none", sw=1.1))

    # Minimum-time curve: (2.5, 30 s) down to (6.8, 5 s), then flat at 5 s.
    pts = []
    for i in range(19):
        r = 2.5 + (6.8 - 2.5) * i / 18.0
        yy = 83 + (192 - 83) * (r - 2.5) / (6.8 - 2.5)
        pts.append((xpos(r), yy))
    pts.append((xpos(10), 192))
    o.append(_poly(pts, fill="none", sw=1.8))

    # Axis titles and printed note.
    o.append(T(30, 49, "Thời gian t<sub>e</sub> tối thiểu", 6.8, anchor="start"))
    o.append(T(30, 59, "(Minimum te time, seconds)", 6.8, anchor="start"))
    o.append(T(355, 300, "Tỷ lệ dòng khởi động / Starting current ratio Ia/In", 7.0))
    o.append(T(340, 316, "Lưu ý: Trong mọi trường hợp, thời gian t<sub>e</sub> tối thiểu "
                         "được chấp nhận là 5 giây / Note: Minimum acceptable te time in any "
                         "case is 5 second", 6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.16")),
                "Hình 12.16 · Thời gian tₑ nhỏ nhất cho phép theo tỷ lệ Ia/In. Ghi chú: Trong "
                "mọi trường hợp, thời gian tₑ nhỏ nhất được chấp nhận là 5 giây",
                "Figure 12.16 · Minimum permissible te times for IJn ratios Note: Minimum "
                "acceptable te time in any case is 5 second",
                "Đồ thị có trục hoành là tỷ lệ dòng khởi động Ia/In từ 2 đến 10 và trục tung "
                "là thời gian t<sub>e</sub> tối thiểu tính bằng giây, các vạch 1, 2, 3, 4, 5, "
                "6, 8, 10, 20, 30, 40. Đường cong giảm từ khoảng 30 giây tại tỷ lệ 2,5 xuống "
                "5 giây tại tỷ lệ 6,8 rồi nằm ngang ở mức 5 giây. Ghi chú trong bản in nhấn "
                "mạnh mức tối thiểu 5 giây. EN caption keeps the printed OCR forms 'IJn "
                "ratios' and '5 second' (for Ia/In ratios and 5 seconds).",
                "Chart whose horizontal axis is the starting current ratio Ia/In from 2 to "
                "10 and whose vertical axis is minimum te time in seconds with ticks 1, 2, "
                "3, 4, 5, 6, 8, 10, 20, 30, 40. The curve falls from about 30 seconds at ratio "
                "2.5 to 5 seconds at ratio 6.8 and then runs flat at 5 seconds. The printed "
                "note insists on a 5-second minimum. The English caption deliberately keeps "
                "the printed OCR forms 'IJn ratios' and '5 second', intelligible as 'Ia/In "
                "ratios' and '5 seconds'")
