# -*- coding: utf-8 -*-
"""Vector figures for Chapter 8 "Installation and Maintenance" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 176-191.

Eleven simplified but faithful figures ``fig_f8_01`` ... ``fig_f8_11``.
Every function is registered with :func:`_reg` and returns the standard
5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through
:func:`_finish`. All text is XML-escaped with :func:`T` / :func:`esc`.

Source quirk: in the text dump the caption for Figure 8.7 precedes that of
Figure 8.6 on printed p. 184, and the caption for Figure 8.9 precedes that
of Figure 8.8 on printed p. 185. Figure 8.4 is captioned inside section
8.3.5 although it illustrates 8.5.1, and Figure 8.5 is captioned at the end
of 8.4.2. The functions here are numbered and placed in logical prose order;
see ``source_notes`` in the prose module.
"""
import math

from cvh6fig import (_reg, _finish, _leader, _labels, _c4_labels, esc, T,
                     _defs, _rect, _line, _circle, _ellipse, _poly, _path,
                     _arrow, _spring, _num, svg, _legend,
                     INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not re-exported by `cvh6fig`.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# small local helpers
# ---------------------------------------------------------------------------
def _pipe_h(o, x0, x1, y, ht=44, arrows=3):
    """A horizontal pipe section with flow arrows."""
    o.append(_rect(x0, y, x1 - x0, ht, fill="#eef3fb", sw=1.5))
    o.append(_line(x0, y, x1, y, sw=1.7, color=INK))
    o.append(_line(x0, y + ht, x1, y + ht, sw=1.7, color=INK))
    for i in range(arrows):
        ax = x0 + (i + 0.5) * (x1 - x0) / arrows
        o.append(_arrow(ax - 13, y + ht / 2.0, ax + 13, y + ht / 2.0,
                        sw=1.2, color=GREEN))


def _bub(o, cx, cy, tag, r=11):
    """An instrument bubble (DVC, TE, SV ...)."""
    o.append(_circle(cx, cy, r, fill="#ffffff", sw=1.3, color=INK))
    o.append(T(cx, cy + 3, tag, 7.0, weight="600"))


def _hex(o, cx, cy, r, hole=10):
    """A hexagonal nut in face view."""
    pts = [(cx + r * math.cos(math.radians(a)),
            cy + r * math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]
    o.append(_poly(pts, fill="#e9eef4", sw=1.4, close=True))
    o.append(_circle(cx, cy, hole, fill="#ffffff", sw=1.1))


def _ring(o, cx, cy, ro, ri, fill=FILL):
    """A flat gasket / washer in face view."""
    o.append(_circle(cx, cy, ro, fill=fill, sw=1.3, color=GOLD))
    o.append(_circle(cx, cy, ri, fill="#ffffff", sw=1.1))


def _stack_rings(o, cx, cy, ro, ri, n=3, step=6):
    """A short stack of packing rings drawn as offset ellipses."""
    for i in range(n):
        yy = cy - (n - 1) * step / 2.0 + i * step
        o.append(_ellipse(cx, yy, ro, 7, fill=FILL, sw=1.1, color=GOLD))
        o.append(_ellipse(cx, yy, ri, 4, fill="#ffffff", sw=0.8, color=GOLD))


# ---------------------------------------------------------------------------
# Figure 8.1 - Flow direction arrow on a valve body
# ---------------------------------------------------------------------------
@_reg
def fig_f8_01():
    """Figure 8.1 (p. 178) - Flow-direction arrow on a metal-seated ball valve."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 28,
               "Mũi tên chỉ chiều dòng chảy trên thân van / Flow-Direction Arrow on a Valve Body",
               8.8, weight="600"))
    _pipe_h(o, 60, 620, 150, 50, arrows=4)
    # flanged ball valve body
    o.append(_rect(268, 132, 14, 86, fill="#e9eef4", sw=1.4))
    o.append(_rect(398, 132, 14, 86, fill="#e9eef4", sw=1.4))
    o.append(_rect(282, 132, 116, 86, fill="#f4f7fb", sw=1.8))
    o.append(_circle(340, 175, 32, fill=FILL, sw=1.6, color=GOLD))
    o.append(_circle(340, 175, 17, fill="#ffffff", sw=1.2, color=GOLD))
    o.append(_arrow(310, 175, 370, 175, sw=2.0, color=GREEN))
    # cast arrow detail above the body
    o.append(_arrow(322, 108, 358, 108, sw=1.8, color=GREEN))
    o.append(_leader(340, 114, 340, 130))
    o.append(T(340, 98, "Mũi tên trên thân / Cast arrow", 7.4, color=GREEN))
    o.append(T(340, 258, "Van bi đế kim loại / Metal-seated ball valve", 8.0, weight="600"))
    o.append(T(340, 288,
               "Lắp thân van để dòng chảy đi theo mũi tên hoặc sổ hướng dẫn / "
               "Install the body so flow follows the arrow or the instruction manual",
               7.0, color=GREY))
    o.append(_legend([
        "Dòng chất lưu / Fluid flow",
        "Mũi tên chỉ chiều dòng chảy / Flow-direction arrow",
        "Thân van và đế kim loại / Valve body and metal seat",
    ], 60, 322, lh=18))
    return _finish(w, h, o,
                   "Figure 8.1 (p. 178) - Flow-direction arrow on a valve body",
                   "Hình 8.1 (tr. 178) · Mũi tên chỉ chiều dòng chảy trên thân van",
                   "Hình 8.1 (tr. 178) · Mũi tên đúc trên thân van bi đế kim loại cho biết chiều "
                   "dòng chảy; phải lắp thân van sao cho chất lưu đi đúng chiều mũi tên hoặc theo "
                   "sổ hướng dẫn của nhà sản xuất.",
                   "Figure 8.1 (p. 178) · The arrow cast on a metal-seated ball valve body shows "
                   "the intended flow direction; the body must be installed so fluid follows the "
                   "arrow or the manufacturer's instruction manual.",
                   "Sơ đồ Hình 8.1 (tr. 178) mũi tên chiều dòng chảy trên thân van",
                   "Schematic of Figure 8.1 (p. 178) flow-direction arrow on a valve body")


# ---------------------------------------------------------------------------
# Figure 8.2 - Criss-cross bolt tightening
# ---------------------------------------------------------------------------
@_reg
def fig_f8_02():
    """Figure 8.2 (p. 178) - Tighten flange bolts in a criss-cross pattern."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 28,
               "Siết bulông theo kiểu chéo đối xứng / Tighten Bolts in a Criss-Cross Pattern",
               8.8, weight="600"))
    cx, cy = 250, 208
    o.append(_circle(cx, cy, 120, fill="#eef3fb", sw=1.8))
    o.append(_circle(cx, cy, 78, fill="#ffffff", sw=1.4, color=GREY))
    o.append(_circle(cx, cy, 44, fill="#e9eef4", sw=1.4, color=GREY))
    # opposite-pair guide lines
    for ang in (0, 45):
        r = math.radians(ang)
        o.append(_line(cx - 100 * math.cos(r), cy - 100 * math.sin(r),
                       cx + 100 * math.cos(r), cy + 100 * math.sin(r),
                       sw=0.7, dash="4 4", color=GREY))
    r = math.radians(90)
    o.append(_line(cx, cy - 100, cx, cy + 100, sw=0.7, dash="4 4", color=GREY))
    r = math.radians(-90)
    o.append(_line(cx, cy + 100, cx, cy - 100, sw=0.7, dash="4 4", color=GREY))
    # numerals as printed in the dump, clockwise from the top
    labs = [(90, 1), (45, 2), (0, 3), (-45, 8), (-90, 5),
            (-135, 6), (180, 4), (135, 7)]
    for ang, n in labs:
        r = math.radians(ang)
        bx = cx + 100 * math.cos(r)
        by = cy - 100 * math.sin(r)
        o.append(_circle(bx, by, 13, fill="#ffffff", sw=1.2, color=INK))
        o.append(T(bx, by + 3, str(n), 8.0, weight="600"))
    o.append(T(540, 100, "Trình tự siết / Tightening sequence", 8.0, weight="600"))
    for i, s in enumerate([
            "Siết nhẹ trước / Snug up gently",
            "1–5 · 2–6 · 3–4 · 8–7",
            "Siết dần từng cặp đối diện / Tighten opposite pairs progressively",
            "Tránh ép gioăng không đều / Avoid uneven gasket loading",
            "Tránh rò rỉ và hỏng bích / Prevent leaks and flange damage"]):
        o.append(T(420, 130 + i * 26, s, 7.2, anchor="start",
                   color=GREY if i in (0, 2, 3, 4) else INK))
    o.append(_legend([
        "Mặt bích / Flange face",
        "Bulông được đánh số / Numbered bolts",
        "Cặp bulông đối diện / Opposite bolt pair",
    ], 420, 300, lh=18))
    return _finish(w, h, o,
                   "Figure 8.2 (p. 178) - Tighten bolts in a criss-cross pattern",
                   "Hình 8.2 (tr. 178) · Siết bulông theo kiểu chéo đối xứng",
                   "Hình 8.2 (tr. 178) · Sau khi căn chỉnh bích và siết nhẹ các bulông, tiến hành "
                   "siết chéo theo từng cặp đối diện để ép gioăng đều, tránh rò rỉ và tránh làm "
                   "hỏng hoặc gãy bích, nhất là khi bích khác vật liệu với bích van.",
                   "Figure 8.2 (p. 178) · After aligning the flanges and snugging the bolts, tighten "
                   "opposite pairs progressively in a criss-cross pattern for even gasket loading, "
                   "preventing leaks and flange damage, especially with dissimilar flange materials.",
                   "Sơ đồ Hình 8.2 (tr. 178) trình tự siết bulông chéo đối xứng",
                   "Schematic of Figure 8.2 (p. 178) criss-cross bolt tightening")


# ---------------------------------------------------------------------------
# Figure 8.3 - Non-intrusive diagnostics program
# ---------------------------------------------------------------------------
@_reg
def fig_f8_03():
    """Figure 8.3 (p. 181) - Non-intrusive diagnostics for predictive maintenance."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Chương trình chẩn đoán không xâm lấn cho bảo trì dự báo / "
               "Non-Intrusive Diagnostics for Predictive Maintenance", 8.0, weight="600"))
    # valve assembly with digital controller
    o.append(_rect(65, 205, 170, 76, fill="#eef3fb", sw=1.7))
    o.append(_rect(52, 219, 16, 48, fill="#e9eef4", sw=1.3))
    o.append(_rect(232, 219, 16, 48, fill="#e9eef4", sw=1.3))
    o.append(_line(150, 205, 150, 150, sw=3.0, color=INK))
    o.append(_rect(105, 100, 90, 50, fill="#f4f7fb", sw=1.6))
    o.append(_spring(150, 103, 147, width=26, turns=4))
    o.append(_rect(88, 54, 124, 40, fill="#fdf3e6", sw=1.6))
    o.append(T(150, 79, "Bộ điều khiển van số", 7.6, weight="600"))
    _bub(o, 150, 122, "DVC", r=13)
    o.append(_line(40, 112, 105, 112, sw=1.7, color=BLUE))
    o.append(_arrow(60, 112, 96, 112, sw=1.3, color=BLUE))
    o.append(T(42, 102, "Khí nén / Air", 7.2, anchor="start"))
    o.append(_line(150, 190, 150, 150, sw=1.0, dash="4 3", color=GREY))
    o.append(T(150, 310, "Van đang vận hành / Valve in service", 7.4))
    # diagnostics panel
    o.append(_rect(330, 60, 312, 250, fill="#fafbfd", sw=1.7))
    o.append(T(486, 88, "Chẩn đoán khi đang vận hành / In-Service Diagnostics", 8.0, weight="600"))
    rows = [
        (GREEN, "Không lỗi — tiếp tục vận hành / No fault detected"),
        (GOLD, "Cảnh báo — lên kế hoạch bảo trì / Warning — plan maintenance"),
        (RED, "Lỗi — cần xử lý ngay / Error — immediate attention"),
    ]
    for i, (col, txt) in enumerate(rows):
        yy = 140 + i * 56
        o.append(_circle(364, yy, 11, fill=col, sw=0))
        o.append(T(386, yy + 3, txt, 7.1, anchor="start"))
    o.append(T(486, 330,
               "Chất lượng khí · rò rỉ · áp suất cấp · ma sát · độ lệch hành trình",
               6.9, color=GREY))
    o.append(T(486, 344,
               "Air quality · leakage · supply pressure · friction · travel deviation",
               6.9, color=GREY))
    o.append(_legend([
        "Cảm biến không xâm lấn / Non-intrusive sensing",
        "Cảnh báo sớm / Predictive warning",
        "Hành động khắc phục / Corrective action",
    ], 60, 372, lh=18))
    return _finish(w, h, o,
                   "Figure 8.3 (p. 181) - Non-intrusive diagnostics program",
                   "Hình 8.3 (tr. 181) · Chẩn đoán không xâm lấn cho bảo trì dự báo",
                   "Hình 8.3 (tr. 181) · Chương trình chẩn đoán không xâm lấn dùng bộ điều khiển "
                   "van số để theo dõi van đang vận hành, báo cáo mức độ lỗi và đưa ra khuyến nghị "
                   "xanh, vàng hoặc đỏ.",
                   "Figure 8.3 (p. 181) · A non-intrusive diagnostics program uses a digital valve "
                   "controller to monitor a valve in service, reporting fault severity and giving "
                   "green, yellow or red recommendations.",
                   "Sơ đồ Hình 8.3 (tr. 181) chẩn đoán không xâm lấn cho bảo trì dự báo",
                   "Schematic of Figure 8.3 (p. 181) non-intrusive predictive diagnostics")


# ---------------------------------------------------------------------------
# Figure 8.4 - Typical spring-and-diaphragm actuator
# ---------------------------------------------------------------------------
@_reg
def fig_f8_04():
    """Figure 8.4 (p. 182) - Typical spring-and-diaphragm actuator."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Cơ cấu chấp hành lò xo - màng điển hình / Typical Spring-and-Diaphragm Actuator",
               8.6, weight="600"))
    # upper diaphragm casing and molded diaphragm
    o.append(_ellipse(340, 150, 130, 48, fill="#eef3fb", sw=1.8, color=INK))
    o.append(_line(210, 150, 470, 150, sw=2.2, color=GOLD))
    o.append(_rect(200, 148, 280, 14, fill="#e9eef4", sw=1.4))
    # spring and stem
    o.append(_line(340, 150, 340, 372, sw=3.0, color=INK))
    o.append(_spring(340, 172, 296, width=40, turns=6))
    o.append(_rect(252, 296, 176, 26, fill="#f4f7fb", sw=1.6))
    o.append(_rect(262, 350, 156, 52, fill="#eef3fb", sw=1.7))
    o.append(_rect(246, 362, 18, 28, fill="#e9eef4", sw=1.3))
    o.append(_rect(416, 362, 18, 28, fill="#e9eef4", sw=1.3))
    o.append(_arrow(50, 132, 196, 132, sw=1.6, color=RED))
    o.append(T(52, 122, "Áp suất khí / Air pressure", 7.4, anchor="start"))
    # callouts
    o.append(_leader(256, 148, 190, 100))
    o.append(T(186, 96, "Màng ép khuôn / Molded diaphragm", 7.4, anchor="end"))
    o.append(_leader(365, 232, 470, 214))
    o.append(T(476, 218, "Lò xo / Spring", 7.4, anchor="start"))
    o.append(_leader(420, 374, 500, 356))
    o.append(T(506, 360, "Thân van / Valve body", 7.4, anchor="start"))
    o.append(_leader(340, 320, 220, 320))
    o.append(T(214, 324, "Ty / Stem", 7.4, anchor="end"))
    o.append(T(340, 408,
               "Khí tạo lực một chiều, lò xo tạo lực chiều ngược lại — cơ cấu tác động đơn / "
               "Air supplies force in one direction and the spring in the other: single-acting",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 8.4 (p. 182) - Typical spring-and-diaphragm actuator",
                   "Hình 8.4 (tr. 182) · Cơ cấu chấp hành lò xo - màng điển hình",
                   "Hình 8.4 (tr. 182) · Mặt cắt cơ cấu lò xo - màng điển hình: màng ép khuôn nhận "
                   "áp suất khí tạo lực một chiều, lò xo tạo lực chiều ngược lại, nên đây là cơ cấu "
                   "tác động đơn.",
                   "Figure 8.4 (p. 182) · Cross-section of a typical spring-and-diaphragm actuator: "
                   "a molded diaphragm takes air pressure for force in one direction and a spring "
                   "supplies force in the other, making it single-acting.",
                   "Sơ đồ Hình 8.4 (tr. 182) cơ cấu chấp hành lò xo - màng",
                   "Schematic of Figure 8.4 (p. 182) spring-and-diaphragm actuator")


# ---------------------------------------------------------------------------
# Figure 8.5 - Control disk
# ---------------------------------------------------------------------------
@_reg
def fig_f8_05():
    """Figure 8.5 (p. 183) - Control disk."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 28, "Đĩa điều khiển / Control Disk", 9.0, weight="600"))
    o.append(_rect(60, 140, 560, 100, fill="#eef3fb", sw=1.6))
    o.append(_line(60, 140, 620, 140, sw=1.7, color=INK))
    o.append(_line(60, 240, 620, 240, sw=1.7, color=INK))
    o.append(_rect(266, 132, 14, 116, fill="#e9eef4", sw=1.4))
    o.append(_rect(400, 132, 14, 116, fill="#e9eef4", sw=1.4))
    o.append(_arrow(90, 190, 248, 190, sw=1.5, color=GREEN))
    o.append(_arrow(430, 190, 590, 190, sw=1.5, color=GREEN))
    # disk and shaft
    o.append(_ellipse(340, 190, 24, 50, fill=FILL, sw=1.8, color=GOLD))
    o.append(_line(340, 96, 340, 284, sw=2.4, color=INK))
    o.append(_rect(300, 168, 14, 44, fill="#dfe7ef", sw=1.2))
    o.append(_rect(366, 168, 14, 44, fill="#dfe7ef", sw=1.2))
    o.append(T(340, 84, "Đĩa điều khiển / Control disk", 8.0, weight="600"))
    o.append(_leader(340, 116, 430, 116))
    o.append(T(436, 120, "Trục / Shaft", 7.4, anchor="start"))
    o.append(_leader(372, 208, 450, 262))
    o.append(T(456, 266, "Vòng đế / Seat ring", 7.4, anchor="start"))
    o.append(T(340, 306,
               "Đĩa là phần tử điều khiển và là chi tiết hao mòn trong danh sách phụ tùng dự phòng",
               6.9, color=GREY))
    o.append(T(340, 320,
               "The disk is a controlling element and a wear part in the spare-parts list",
               6.9, color=GREY))
    o.append(_legend([
        "Dòng chất lưu / Fluid flow",
        "Đĩa điều khiển / Control disk",
        "Vòng đế / Seat ring",
    ], 60, 340, lh=18))
    return _finish(w, h, o,
                   "Figure 8.5 (p. 183) - Control disk",
                   "Hình 8.5 (tr. 183) · Đĩa điều khiển",
                   "Hình 8.5 (tr. 183) · Đĩa điều khiển là phần tử làm việc của van quay, nằm trong "
                   "danh sách phụ tùng dự phòng cùng với nút, ty, cage, bi và trục.",
                   "Figure 8.5 (p. 183) · The control disk is the working element of a rotary valve "
                   "and appears in the recommended spare-parts list alongside the plug, stem, cage, "
                   "ball and shaft.",
                   "Sơ đồ Hình 8.5 (tr. 183) đĩa điều khiển",
                   "Schematic of Figure 8.5 (p. 183) control disk")


# ---------------------------------------------------------------------------
# Figure 8.6 - Stud, washer and nut
# ---------------------------------------------------------------------------
@_reg
def fig_f8_06():
    """Figure 8.6 (p. 184) - Stud, washer and nut."""
    w, h = 680, 390
    o = [_defs()]
    o.append(T(340, 28, "Chốt ren, vòng đệm và đai ốc / Stud, Washer, and Nut", 9.0, weight="600"))
    o.append(_line(60, 190, 620, 190, sw=0.7, dash="6 4", color=GREY))
    # stud with thread ticks
    o.append(_rect(90, 174, 300, 32, fill="#e9eef4", sw=1.5))
    for x in range(300, 388, 10):
        o.append(_line(x, 174, x + 6, 206, sw=0.8, color=GREY))
    # washer and nut in face view
    _ring(o, 452, 190, 30, 12)
    _hex(o, 558, 190, 34, hole=12)
    o.append(T(240, 148, "Chốt ren / Stud", 8.0, weight="600"))
    o.append(_leader(452, 156, 452, 128))
    o.append(T(452, 124, "Vòng đệm / Washer", 7.6))
    o.append(_leader(558, 152, 558, 124))
    o.append(T(558, 120, "Đai ốc / Nut", 7.6))
    o.append(T(340, 272,
               "Các chi tiết này thường có trong bộ phụ tùng dùng để thay thế khi đại tu van / "
               "These parts are commonly supplied in the kits used to overhaul a valve",
               7.0, color=GREY))
    o.append(_legend([
        "Chốt ren có ren ở đầu / Threaded stud",
        "Vòng đệm phân bổ tải trọng / Load-spreading washer",
        "Đai ốc siết / Tightening nut",
    ], 60, 306, lh=18))
    return _finish(w, h, o,
                   "Figure 8.6 (p. 184) - Stud, washer, and nut",
                   "Hình 8.6 (tr. 184) · Chốt ren, vòng đệm và đai ốc",
                   "Hình 8.6 (tr. 184) · Ba chi tiết cơ bản của mối lắp bắt bích: chốt ren, vòng đệm "
                   "và đai ốc, thường được gộp trong bộ phụ tùng thay thế.",
                   "Figure 8.6 (p. 184) · The three basic fastener parts of a bolted joint: stud, "
                   "washer and nut, commonly grouped together in a replacement parts kit.",
                   "Sơ đồ Hình 8.6 (tr. 184) chốt ren, vòng đệm và đai ốc",
                   "Schematic of Figure 8.6 (p. 184) stud, washer and nut")


# ---------------------------------------------------------------------------
# Figure 8.7 - Gasket kit
# ---------------------------------------------------------------------------
@_reg
def fig_f8_07():
    """Figure 8.7 (p. 184) - Gasket kit."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 28, "Bộ gioăng / Gasket Kit", 9.0, weight="600"))
    o.append(T(340, 74, "Bộ phụ tùng cho một lần sửa cụ thể / Parts for a specific repair", 7.2,
               color=GREY))
    o.append(_rect(70, 100, 540, 200, fill="#fafbfd", sw=1.7))
    o.append(_rect(84, 114, 512, 172, fill="none", sw=0.7, dash="5 4", stroke=GREY))
    # ring gasket
    _ring(o, 180, 190, 54, 28)
    # flat gasket with bore
    o.append(_rect(288, 158, 120, 64, fill=FILL, sw=1.4, stroke=GOLD))
    o.append(_rect(302, 172, 92, 36, fill="#ffffff", sw=1.1))
    # spiral-wound style gasket
    o.append(_circle(500, 190, 46, fill=FILL, sw=1.4, color=GOLD))
    o.append(_circle(500, 190, 22, fill="#ffffff", sw=1.1))
    for i in range(10):
        a = i * 36
        r = math.radians(a)
        o.append(_line(500 + 24 * math.cos(r), 190 + 24 * math.sin(r),
                       500 + 44 * math.cos(r), 190 + 44 * math.sin(r),
                       sw=0.7, color=GOLD))
    o.append(T(180, 270, "Gioăng vòng / Ring gasket", 7.4))
    o.append(T(348, 270, "Gioăng phẳng / Flat gasket", 7.4))
    o.append(T(500, 270, "Gioăng xoắn / Spiral-wound gasket", 7.4))
    o.append(T(340, 334,
               "Dùng đúng bộ gioăng giúp đảm bảo kín khít và rút ngắn thời gian chờ linh kiện / "
               "The correct gasket kit ensures a tight seal and shortens the wait for parts",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 8.7 (p. 184) - Gasket kit",
                   "Hình 8.7 (tr. 184) · Bộ gioăng",
                   "Hình 8.7 (tr. 184) · Bộ gioăng gồm các chi tiết làm kín cần thiết cho một lần "
                   "sửa cụ thể, giúp kiểm soát tồn kho và đảm bảo có đủ phụ tùng khi tháo van.",
                   "Figure 8.7 (p. 184) · A gasket kit groups the sealing parts needed for a "
                   "specific repair, improving inventory control and assuring that all required "
                   "parts arrive together.",
                   "Sơ đồ Hình 8.7 (tr. 184) bộ gioăng",
                   "Schematic of Figure 8.7 (p. 184) gasket kit")


# ---------------------------------------------------------------------------
# Figure 8.8 - Packing kit
# ---------------------------------------------------------------------------
@_reg
def fig_f8_08():
    """Figure 8.8 (p. 185) - Packing kit."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 28, "Bộ đệm kín / Packing Kit", 9.0, weight="600"))
    o.append(T(340, 74, "Bộ vòng đệm thay thế cho thân hoặc trục van / Replacement rings for the stem",
               7.2, color=GREY))
    o.append(_rect(70, 100, 540, 200, fill="#fafbfd", sw=1.7))
    o.append(_rect(84, 114, 512, 172, fill="none", sw=0.7, dash="5 4", stroke=GREY))
    for cx, ro, ri, n, lab in [
            (160, 34, 13, 3, "Vòng nhỏ / Small rings"),
            (280, 42, 18, 4, "Vòng trung bình / Medium rings"),
            (406, 50, 24, 4, "Vòng lớn / Large rings"),
            (540, 38, 15, 3, "Vòng đế / Backing rings")]:
        _stack_rings(o, cx, 190, ro, ri, n=n)
        o.append(T(cx, 272, lab, 7.0))
    o.append(T(340, 334,
               "Thay đúng bộ đệm khi có rò rỉ quanh thân hoặc khi tháo van hoàn toàn / "
               "Replace the packing when leakage develops or when the valve is fully disassembled",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 8.8 (p. 185) - Packing kit",
                   "Hình 8.8 (tr. 185) · Bộ đệm kín",
                   "Hình 8.8 (tr. 185) · Bộ đệm kín chứa các vòng có kích thước khác nhau để thay "
                   "thay thế khi rò rỉ quanh thân hoặc khi tháo van để bảo trì, kiểm tra.",
                   "Figure 8.8 (p. 185) · A packing kit holds rings of several sizes for replacement "
                   "when leakage develops around the stem or when the valve is disassembled for "
                   "maintenance or inspection.",
                   "Sơ đồ Hình 8.8 (tr. 185) bộ đệm kín",
                   "Schematic of Figure 8.8 (p. 185) packing kit")


# ---------------------------------------------------------------------------
# Figure 8.9 - Typical valve stem packing assemblies
# ---------------------------------------------------------------------------
@_reg
def fig_f8_09():
    """Figure 8.9 (p. 185) - Typical valve stem packing assemblies."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Cụm đệm kín thân van điển hình / Typical Valve Stem Packing Assemblies",
               8.8, weight="600"))
    # bonnet cross-section
    o.append(_rect(220, 110, 240, 240, fill="#f4f7fb", sw=1.8))
    o.append(_rect(302, 110, 76, 240, fill="#ffffff", sw=1.2))
    o.append(_line(340, 86, 340, 382, sw=3.4, color=INK))
    # packing nut and rings
    o.append(_rect(294, 110, 92, 24, fill="#e9eef4", sw=1.4))
    for yy in (154, 174, 194, 214, 234, 254):
        o.append(_rect(308, yy, 64, 14, fill=FILL, sw=1.1, stroke=GOLD))
    o.append(_circle(398, 204, 7, fill="#ffffff", sw=1.1, color=BLUE))
    o.append(_line(408, 204, 462, 186, sw=0.7, color=GREY))
    o.append(T(468, 184, "Lỗ bôi trơn / Lubricator hole", 7.2, anchor="start"))
    o.append(_leader(294, 122, 176, 126))
    o.append(T(170, 130, "Đai ốc đệm / Packing nut", 7.2, anchor="end"))
    o.append(_leader(308, 224, 180, 212))
    o.append(T(174, 216, "Các vòng đệm / Packing rings", 7.2, anchor="end"))
    o.append(_leader(372, 320, 470, 300))
    o.append(T(476, 304, "Thân van / Valve stem", 7.2, anchor="start"))
    o.append(T(340, 386,
               "Khoảng một nửa số vòng nằm dưới lỗ bôi trơn — không nên thổi cũ bằng áp suất / "
               "About half the rings lie below the lubricator hole — do not blow them out with pressure",
               6.9, color=GREY))
    o.append(T(340, 414,
               "Tháo cơ cấu chấp hành và nắp van, kéo thân ra rồi đẩy vòng cũ ra từ đỉnh nắp / "
               "Remove the actuator and bonnet, pull the stem and drive the old rings out from the top",
               6.9, color=GREY))
    return _finish(w, h, o,
                   "Figure 8.9 (p. 185) - Typical valve stem packing assemblies",
                   "Hình 8.9 (tr. 185) · Cụm đệm kín thân van điển hình",
                   "Hình 8.9 (tr. 185) · Mặt cắt cụm đệm kín quanh thân van: đai ốc, các vòng đệm "
                   "xếp chồng và lỗ bôi trơn; khoảng một nửa số vòng nằm dưới lỗ này.",
                   "Figure 8.9 (p. 185) · Cross-section of a stem packing assembly: packing nut, "
                   "stacked rings and the lubricator hole, with about half the rings below the hole.",
                   "Sơ đồ Hình 8.9 (tr. 185) cụm đệm kín thân van",
                   "Schematic of Figure 8.9 (p. 185) typical stem packing assembly")


# ---------------------------------------------------------------------------
# Figure 8.10 - Bench set seating force
# ---------------------------------------------------------------------------
@_reg
def fig_f8_10():
    """Figure 8.10 (p. 187) - Bench set seating force."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Lực ép đế và giá trị bench set / Bench Set Seating Force", 8.8, weight="600"))
    x0, x1 = 130, 610
    yt, yb = 96, 306
    o.append(_line(x0, yb, x1, yb, sw=1.4, color=INK))
    o.append(_line(x0, yt - 14, x0, yb, sw=1.4, color=INK))
    for psig in (0, 3, 6, 9, 12, 15):
        xx = x0 + psig / 15.0 * (x1 - x0)
        o.append(_line(xx, yb, xx, yb + 4, sw=0.9, color=INK))
        o.append(T(xx, yb + 16, str(psig), 7.2, color=GREY))
    o.append(T(370, 348,
               "Áp suất màng cơ cấu chấp hành (psig) / Actuator Diaphragm Pressure (psig)",
               7.4))
    o.append(T(140, 62, "Hành trình cơ cấu / Actuator Travel", 7.4, anchor="start"))
    # two sloping lines: bench set and bench set plus deadband
    o.append(_line(226, yt, 514, yb, sw=2.2, color=BLUE))
    o.append(_line(266, yt, 554, yb, sw=2.2, color=RED))
    o.append(T(300, 80, "Bench set (3–11 psig) / Bàn đặt ban đầu", 7.2, anchor="start",
               color=BLUE))
    o.append(T(486, 80, "Bench set + deadband / + Vùng chết", 7.2, anchor="start",
               color=RED))
    o.append(T(438, 202, "Vùng chết / Deadband", 7.0, anchor="start", color=GREY))
    o.append(T(140, 112, "0% hành trình (chặn trên) / 0% Travel (upper stop)", 7.0,
               anchor="start"))
    o.append(T(140, 292, "100% hành trình định mức (chặn dưới, nút ép đế) / "
               "100% Rated travel (lower stop, plug-seated)", 7.0, anchor="start"))
    o.append(T(340, 388,
               "*Cơ cấu nối với van, có vùng chết / *Actuator connected to valve, deadband present",
               7.0, color=GREY))
    o.append(T(340, 416,
               "Lực ép đế = áp suất áp dụng − bench set − độ nén lò xo do hành trình / "
               "Seating force = applied pressure - bench set - spring compression from travel",
               6.8, color=GREY))
    return _finish(w, h, o,
                   "Figure 8.10 (p. 187) - Bench set seating force",
                   "Hình 8.10 (tr. 187) · Lực ép đế và bench set",
                   "Hình 8.10 (tr. 187) · Đồ thị áp suất màng và hành trình: bench set 3–11 psig "
                   "cộng vùng chết xác định áp suất bắt đầu mở và lực ép đế khi nút đã ngồi.",
                   "Figure 8.10 (p. 187) · A diaphragm-pressure versus travel plot: the 3-11 psig "
                   "bench set together with deadband defines the pressure that starts travel and "
                   "the seating force when the plug is seated.",
                   "Sơ đồ Hình 8.10 (tr. 187) lực ép đế và bench set",
                   "Schematic of Figure 8.10 (p. 187) bench set seating force")


# ---------------------------------------------------------------------------
# Figure 8.11 - STO planning process
# ---------------------------------------------------------------------------
@_reg
def fig_f8_11():
    """Figure 8.11 (p. 191) - STO planning process, seven steps."""
    w, h = 680, 470
    o = [_defs()]
    o.append(T(340, 28,
               "Quy trình lập kế hoạch STO / STO Planning Process", 9.0, weight="600"))
    steps = [
        ("OPERATIONAL\nPLANNING", "24–60 tháng"),
        ("ALIGNMENT", "12–24 tháng"),
        ("WORK SCOPE\nDEFINITION", "12–18 tháng"),
        ("DETAILED\nPLANNING", "4–6 tháng"),
        ("PRE-STO\nPLANNING", "2–6 tháng"),
        ("EXECUTION", "tại chỗ"),
        ("POST STO\nEVALUATION", "2–4 tháng sau"),
    ]
    centers = [64, 156, 248, 340, 432, 524, 616]
    for i, ((label, when), cx) in enumerate(zip(steps, centers)):
        o.append(_rect(cx - 39, 120, 78, 64, fill="#eef3fb", sw=1.5))
        lines = label.split("\n")
        o.append(T(cx, 142, lines[0], 6.6, weight="600"))
        if len(lines) > 1:
            o.append(T(cx, 154, lines[1], 6.6, weight="600"))
        o.append(_circle(cx, 104, 11, fill="#fdf3e6", sw=1.1, color=INK))
        o.append(T(cx, 107, str(i + 1), 8.0, weight="600"))
        if i < len(steps) - 1:
            o.append(_arrow(cx + 41, 152, centers[i + 1] - 41, 152,
                            sw=1.3, color=GREEN))
        o.append(T(cx, 202, when, 6.8, color=GREY))
    o.append(T(340, 240,
               "Năm chữ P: Lập kế hoạch đúng đắn ngăn ngừa hiệu quả kém / "
               "The Five P's: Proper Planning Prevents Poor Performance",
               7.4, weight="600"))
    o.append(T(340, 274,
               "Công cụ số và chẩn đoán (AMS, ValveLink, FlowScanner) xác nhận phạm vi cuối / "
               "Digital and diagnostic tools (AMS, ValveLink, FlowScanner) validate the final scope",
               6.9, color=GREY))
    o.append(T(340, 302,
               "Chẩn đoán giúp xác định van cần sửa và van còn tốt trước khi dừng máy / "
               "Diagnostics pinpoint valves needing repair and valves that are healthy",
               6.9, color=GREY))
    o.append(_legend([
        "Lập kế hoạch vận hành / Operational planning",
        "Thống nhất và xác định phạm vi / Alignment and scope definition",
        "Thực hiện và đánh giá sau STO / Execution and post-evaluation",
    ], 60, 338, lh=18))
    return _finish(w, h, o,
                   "Figure 8.11 (p. 191) - STO planning process",
                   "Hình 8.11 (tr. 191) · Quy trình lập kế hoạch STO",
                   "Hình 8.11 (tr. 191) · Quy trình STO bảy bước từ lập kế hoạch vận hành, thống "
                   "nhất, xác định phạm vi, lập kế hoạch chi tiết, trước-STO, thực hiện đến đánh giá "
                   "sau dừng máy.",
                   "Figure 8.11 (p. 191) · The seven-step STO process from operational planning, "
                   "alignment, scope definition and detailed planning through pre-STO preparation, "
                   "execution and post-outage evaluation.",
                   "Sơ đồ Hình 8.11 (tr. 191) quy trình bảy bước lập kế hoạch STO",
                   "Schematic of Figure 8.11 (p. 191) seven-step STO planning process")
