# -*- coding: utf-8 -*-
"""Vector figures for Emerson, *Control Valve Handbook*, 6th ed. (2020),
Chapter 1 "Introduction to Control Valves" (printed pp. 16-33).

The source has nineteen numbered figures (1.1-1.19).  Each is redrawn here
as a simplified but faithful vector schematic that keeps the topology and
the numbered callouts of the original.  Every function returns the standard
5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)`` via ``_fig()``;
all SVG text is XML-escaped with ``esc()``/``T()`` before it reaches a tag.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    # Register the evaluated 5-tuple: `fig(num, key)` consumes the tuple, and
    # the XML validation import does `ET.fromstring(s[0])` on every FIG value.
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _spring(cx, y0, y1, width=26, turns=6, color=GREY):
    pts = [(cx, y0)]
    n = turns * 2
    for i in range(1, n):
        yy = y0 + (y1 - y0) * i / float(n)
        pts.append((cx + (width / 2.0 if i % 2 else -width / 2.0), yy))
    pts.append((cx, y1))
    return _poly(pts, sw=1.4, color=color)


def _num(cx, cy, n):
    """A numbered callout bubble."""
    return (_circle(cx, cy, 8, fill="#fdf3e6", sw=1.1, color=INK)
            + T(cx, cy + 3, str(n), 8.0, color=INK, weight="600"))


def _legend(items, x, y, lh=15, size=7.6):
    """Numbered parts list rendered as plain text lines."""
    return "".join(T(x, y + i * lh, "%d. %s" % (i + 1, lab), size,
                     anchor="start") for i, lab in enumerate(items))


def _bbody(cx, top, bw=150, bh=104, plug=True, seat=True):
    """A simplified globe-style valve body cross-section (linear valve)."""
    o = []
    o.append(_rect(cx - bw / 2, top, bw, bh, fill="#f4f7fb", sw=1.6))
    # flanged pipe ends
    o.append(_rect(cx - bw / 2 - 20, top + bh / 2 - 13, 22, 26,
                   fill="#e9eef4", sw=1.3))
    o.append(_rect(cx + bw / 2 - 2, top + bh / 2 - 13, 22, 26,
                   fill="#e9eef4", sw=1.3))
    # vertical bore
    o.append(_rect(cx - 15, top, 30, bh, fill="#ffffff", sw=1.0))
    if seat:
        o.append(_rect(cx - 26, top + bh / 2 - 5, 52, 10,
                       fill="#dfe7ef", sw=1.2))
    if plug:
        o.append(_poly([(cx - 12, top + bh / 2 - 6), (cx + 12, top + bh / 2 - 6),
                        (cx + 6, top + bh / 2 - 30), (cx - 6, top + bh / 2 - 30)],
                       fill="#fdf3e6", sw=1.4, close=True))
    return "".join(o)


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """Figure 1.1 (p. 17) - Feedback Control Loop."""
    w, h = 680, 300
    o = [_defs()]
    boxes = [(250, 56, 128, 42, "Process"), (470, 126, 108, 42, "Sensor"),
             (470, 206, 118, 42, "Transmitter"), (276, 206, 128, 42, "Controller"),
             (56, 126, 126, 42, "Control Valve")]
    for x, y, bw, bh, lab in boxes:
        o.append(_rect(x, y, bw, bh, fill="#e9edf2", sw=1.2))
        o.append(T(x + bw / 2, y + bh / 2 + 4, lab, 9.2, color=INK, weight="600"))
    # manipulated variable: valve -> up -> right into process
    o.append(_line(119, 126, 119, 77, sw=1.6, color=BLUE))
    o.append(_arrow(119, 77, 250, 77, sw=1.6, color=BLUE))
    o.append(T(157, 70, "Manipulated Variable", 8.4, color=BLUE, anchor="start"))
    # controlled variable: process -> right -> down into sensor
    o.append(_line(378, 77, 524, 77, sw=1.6, color=BLUE))
    o.append(_arrow(524, 77, 524, 126, sw=1.6, color=BLUE))
    o.append(T(432, 70, "Controlled Variable", 8.4, color=BLUE, anchor="start"))
    o.append(_arrow(524, 168, 524, 206, sw=1.4, color=GREY))
    o.append(_arrow(470, 227, 404, 227, sw=1.4, color=GREY))
    o.append(_arrow(276, 227, 182, 227, sw=1.4, color=GREY))
    o.append(_arrow(119, 206, 119, 180, sw=1.4, color=GREY))
    o.append(T(340, 278,
               "Hình 1.1 (tr. 17) · Vòng điều khiển phản hồi: van điều khiển là phần tử điều khiển cuối cùng",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.1 - Feedback control loop"))
    return _fig(s,
                "Hình 1.1 (nguyên bản tr. 17) · Vòng điều khiển phản hồi: cảm biến và bộ phát "
                "thu thông tin về biến quá trình (PV), bộ điều khiển so sánh với điểm đặt và "
                "ra lệnh cho van điều khiển — phần tử điều khiển cuối cùng thường gặp nhất — "
                "điều chỉnh biến thao tác để đưa PV về giá trị mong muốn.",
                "Figure 1.1 (source p. 17) · Feedback control loop: sensors and transmitters "
                "collect information about the process variable (PV), a controller compares it "
                "with the set point and commands the control valve - the most common final "
                "control element - which manipulates the manipulated variable to bring the PV "
                "back to the desired value.",
                "Sơ đồ vòng điều khiển phản hồi gồm van, quá trình, cảm biến, bộ phát và bộ điều khiển",
                "Feedback control loop diagram with valve, process, sensor, transmitter and controller")


@_reg
def fig_f02():
    """Figure 1.2 (p. 18) - Sliding-Stem Control Valve, assembled cutaway."""
    w, h = 640, 440
    o = [_defs()]
    # actuator / bonnet / body stacked on centre line
    o.append(_ellipse(210, 48, 92, 22, fill="#eef3fb", sw=1.5))
    o.append(_line(118, 48, 302, 48, sw=2.0, color=BLUE))
    o.append(_line(210, 48, 210, 120, sw=2.4, color=INK))
    o.append(_spring(210, 60, 112, width=34))
    o.append(_rect(194, 112, 32, 58, fill="#e9eef4", sw=1.2))     # yoke/bonnet
    o.append(_rect(188, 158, 44, 18, fill="#dfe7ef", sw=1.2))     # bonnet flange
    o.append(_bbody(210, 176, bw=168, bh=112))
    o.append(_line(150, 300, 270, 300, sw=2.0, color=GREEN))      # flow passage hint
    o.append(T(210, 318, "Flow", 7.4, color=GREEN))
    callouts = [
        (110, 48, 1, 300, 48), (110, 132, 2, 200, 132), (110, 170, 3, 210, 96),
        (110, 200, 4, 210, 168), (320, 196, 5, 232, 166), (320, 236, 6, 236, 200),
        (110, 252, 7, 210, 240), (320, 268, 8, 238, 238), (320, 288, 9, 236, 256),
        (110, 290, 10, 168, 272), (110, 320, 11, 210, 272),
    ]
    for lx, ly, n, tx, ty in callouts:
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        o.append(_num(lx - 12 if lx < 200 else lx + 12, ly, n))
    o.append(_legend(["Stem", "Packing Flange", "Actuator Locknut", "Bonnet",
                      "Bonnet Gasket", "Piston Ring", "Plug", "Cage", "Seat Ring",
                      "Body/Bonnet Bolting", "Body"], 388, 46, lh=17, size=8.0))
    o.append(T(320, 424, "Hình 1.2 (tr. 18) · Van điều khiển thân trục trượt, mặt cắt lắp ráp",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.2 - Sliding-stem control valve, assembled"))
    return _fig(s,
                "Hình 1.2 (tr. 18) · Van điều khiển kiểu thân trục trượt, mặt cắt lắp ráp: "
                "cơ cấu chấp hành màng/piston ở trên, thân van, nắp và thân van có đường dòng "
                "và chỗ ngồi ở dưới. Các số 1-11 chỉ: 1. Thân van; 2. Bích đệm; 3. Đai ốc khóa "
                "cơ cấu chấp hành; 4. Nắp van; 5. Gioăng nắp; 6. Vòng piston; 7. Nút van; "
                "8. Lồng; 9. Vòng chỗ ngồi; 10. Bulông nắp/thân; 11. Thân van (body).",
                "Figure 1.2 (p. 18) · Sliding-stem control valve, assembled cutaway: diaphragm/"
                "piston actuator above, stem, bonnet and valve body with flow passage and seat "
                "below. Key: 1. Stem; 2. Packing Flange; 3. Actuator Locknut; 4. Bonnet; "
                "5. Bonnet Gasket; 6. Piston Ring; 7. Plug; 8. Cage; 9. Seat Ring; "
                "10. Body/Bonnet Bolting; 11. Body.",
                "Mặt cắt lắp ráp van điều khiển thân trục trượt với các số gọi chi tiết 1-11",
                "Assembled cutaway of a sliding-stem control valve with numbered callouts 1-11")


@_reg
def fig_f03():
    """Figure 1.3 (p. 18) - Sliding-Stem Control Valve, exploded view."""
    w, h = 560, 470
    o = [_defs()]
    # exploded vertical stack
    parts = [(150, "1. Stem", "Thân van"),
             (196, "2. Packing Flange", "Bích đệm"),
             (242, "3. Actuator Locknut", "Đai ốc khóa"),
             (288, "4. Bonnet", "Nắp van"),
             (334, "5. Bonnet Gasket", "Gioăng nắp"),
             (380, "6. Piston Ring", "Vòng piston"),
             (416, "7. Plug", "Nút van"),
             (450, "8. Cage", "Lồng"),
             (480, "9. Seat Ring", "Vòng chỗ ngồi"),
             (504, "10. Body/Bonnet Bolting", "Bulông nắp/thân"),
             (524, "11. Body", "Thân van")]
    for i, (yy, en, vi) in enumerate(parts):
        o.append(_rect(150, yy, 180, 12 if i < 9 else 16,
                       fill="#f4f7fb" if i % 2 == 0 else "#eef3fb", sw=1.1))
        o.append(_num(132, yy + 7, i + 1))
        o.append(T(348, yy + 10, en, 7.6, anchor="start"))
    o.append(T(340, 460, "Hình 1.3 (tr. 18) · Van điều khiển thân trục trượt, dạng tách chi tiết",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.3 - Sliding-stem control valve, exploded view"))
    return _fig(s,
                "Hình 1.3 (tr. 18) · Van điều khiển kiểu thân trục trượt ở dạng tách chi tiết, "
                "cho thấy thứ tự xếp từ trên xuống: thân van, bích đệm, đai ốc khóa cơ cấu "
                "chấp hành, nắp van, gioăng nắp, vòng piston, nút van, lồng, vòng chỗ ngồi, "
                "bulông nắp/thân và thân van.",
                "Figure 1.3 (p. 18) · Sliding-stem control valve in exploded view, showing the "
                "top-to-bottom stack: stem, packing flange, actuator locknut, bonnet, bonnet "
                "gasket, piston ring, plug, cage, seat ring, body/bonnet bolting and body.",
                "Sơ đồ tách chi tiết van điều khiển thân trục trượt với 11 bộ phận",
                "Exploded view of a sliding-stem control valve with eleven components")


@_reg
def fig_f04():
    """Figure 1.4 (p. 18) - Angle Valve."""
    w, h = 520, 360
    o = [_defs()]
    # inlet from left, outlet down, perpendicular ports
    o.append(_rect(120, 130, 150, 74, fill="#f4f7fb", sw=1.6))
    o.append(_rect(100, 146, 22, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(258, 200, 46, 100, fill="#e9eef4", sw=1.3))
    o.append(_rect(168, 100, 30, 30, fill="#e9eef4", sw=1.2))
    o.append(_line(183, 100, 183, 64, sw=2.4, color=INK))
    o.append(_poly([(172, 152), (194, 152), (188, 176), (178, 176)],
                   fill="#fdf3e6", sw=1.3, close=True))
    o.append(_arrow(110, 167, 168, 167, sw=1.8, color=GREEN))
    o.append(_arrow(281, 210, 281, 286, sw=1.8, color=GREEN))
    o.append(T(196, 62, "Stem / Actuator", 8.4, color=INK))
    o.append(T(150, 126, "Inlet", 7.6, color=GREEN))
    o.append(T(298, 300, "Outlet", 7.6, color=GREEN))
    o.append(T(260, 344, "Hình 1.4 (tr. 18) · Van góc: cổng vào và ra vuông góc với nhau",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.4 - Angle valve, perpendicular inlet and outlet"))
    return _fig(s,
                "Hình 1.4 (tr. 18) · Van góc (Angle Valve): kiểu van có cổng vào và cổng ra "
                "vuông góc với nhau; còn được phân loại là van cầu kiểu góc.",
                "Figure 1.4 (p. 18) · Angle valve: a valve design in which the inlet and outlet "
                "ports are perpendicular to each other; it is also classed as an angle-style "
                "globe valve.",
                "Van góc với cổng vào và cổng ra vuông góc",
                "Angle valve with perpendicular inlet and outlet ports")


@_reg
def fig_f05():
    """Figure 1.5 (p. 19) - Bellows Seal Bonnet."""
    w, h = 540, 420
    o = [_defs()]
    o.append(_rect(210, 60, 36, 250, fill="#e9eef4", sw=1.4))     # bonnet
    o.append(_line(228, 40, 228, 330, sw=2.4, color=INK))          # valve stem
    o.append(_rect(206, 92, 44, 44, fill="#f7f9fb", sw=1.2))       # packing box
    for i in range(6):
        y = 148 + i * 14
        o.append(_line(206, y, 250, y + 7, sw=1.2, color=BLUE))
        o.append(_line(250, y + 7, 206, y + 14, sw=1.2, color=BLUE))
    o.append(T(280, 190, "Bellows / Ống mềm", 8.0, color=BLUE, anchor="start"))
    for i, lab in enumerate(["Bonnet", "Packing", "Packing Box", "Bellows", "Valve Stem"]):
        o.append(_num(120, 100 + i * 46, i + 1))
        o.append(T(70, 104 + i * 46, lab, 7.8, anchor="start"))
    o.append(T(270, 404, "Hình 1.5 (tr. 19) · Nắp kín bằng ống mềm (bellows seal bonnet)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.5 - Bellows seal bonnet"))
    return _fig(s,
                "Hình 1.5 (tr. 19) · Nắp van kín bằng ống mềm: dùng một ống mềm (bellows) để "
                "làm kín chống rò rỉ quanh thân phần đóng. Các số 1-5: 1. Nắp van; 2. Gioăng "
                "đệm; 3. Hộp đệm; 4. Ống mềm; 5. Thân van.",
                "Figure 1.5 (p. 19) · Bellows seal bonnet: a bonnet that uses a bellows for "
                "sealing against leakage around the closure-member stem. Key 1-5: "
                "1. Bonnet; 2. Packing; 3. Packing Box; 4. Bellows; 5. Valve Stem.",
                "Nắp van kín bằng ống mềm, mặt cắt có gioăng đệm và quy chiếu số 1-5",
                "Bellows seal bonnet cross-section with packing and numbered callouts 1-5")


@_reg
def fig_f06():
    """Figure 1.6 (p. 19) - Bonnet Assembly."""
    w, h = 500, 400
    o = [_defs()]
    o.append(_rect(200, 70, 40, 240, fill="#e9eef4", sw=1.4))
    o.append(_line(220, 50, 220, 330, sw=2.4, color=INK))
    o.append(_rect(196, 120, 48, 60, fill="#f7f9fb", sw=1.2))
    for i in range(4):
        o.append(_rect(200, 128 + i * 13, 40, 8, fill="#dfe7ef", sw=0.9))
    for i, lab in enumerate(["Bonnet", "Packing", "Packing Box", "Valve Stem"]):
        o.append(_num(130, 110 + i * 56, i + 1))
        o.append(T(80, 114 + i * 56, lab, 7.8, anchor="start"))
    o.append(T(250, 384, "Hình 1.6 (tr. 19) · Cụm nắp van (bonnet assembly)", 7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.6 - Bonnet assembly"))
    return _fig(s,
                "Hình 1.6 (tr. 19) · Cụm nắp van: cụm gồm chi tiết mà thân van đi xuyên qua "
                "và cơ cấu làm kín chống rò rỉ dọc thân; thường dùng để lắp cơ cấu chấp hành "
                "và nén bộ gioăng. Các số 1-4: 1. Nắp van; 2. Gioăng đệm; 3. Hộp đệm; "
                "4. Thân van.",
                "Figure 1.6 (p. 19) · Bonnet assembly: the part through which the valve stem "
                "moves together with the seal against leakage along the stem; it normally "
                "carries the actuator mounting and loads the packing. Key 1-4: 1. Bonnet; "
                "2. Packing; 3. Packing Box; 4. Valve Stem.",
                "Cụm nắp van gồm nắp, gioăng đệm, hộp đệm và thân van",
                "Bonnet assembly with bonnet, packing, packing box and valve stem")


@_reg
def fig_f07():
    """Figure 1.7 (p. 19) - Cages: Linear, Equal-Percentage, Quick-Opening."""
    w, h = 680, 300
    o = [_defs()]
    titles = ["Linear / Tuyến tính", "Equal-Percentage / Phần trăm bằng nhau",
              "Quick-Opening / Mở nhanh"]
    for k, title in enumerate(titles):
        x = 30 + k * 220
        o.append(T(x + 88, 30, title, 9.0, color=INK, weight="600"))
        o.append(_rect(x, 52, 176, 196, fill="#f4f7fb", sw=1.4))
        for g in range(1, 4):
            o.append(_line(x + g * 44, 52, x + g * 44, 248, sw=0.6, color="#d8dde3"))
        for g in range(1, 4):
            o.append(_line(x, 52 + g * 49, x + 176, 52 + g * 49, sw=0.6, color="#d8dde3"))
        # cage window cut-outs
        if k == 0:                      # linear: equal-width rectangular slots
            for wy in (92, 150, 208):
                o.append(_rect(x + 54, wy, 68, 22, fill="#ffffff", sw=1.2))
        elif k == 1:                    # equal-%: V notches widening upward
            for wy in (150, 190):
                o.append(_poly([(x + 54, wy + 26), (x + 88, wy),
                                (x + 122, wy + 26)], fill="#ffffff", sw=1.2, close=True))
        else:                           # quick-opening: large lower windows
            for wy in (170, 214):
                o.append(_rect(x + 50, wy, 76, 24, fill="#ffffff", sw=1.2))
    o.append(T(340, 282, "Hình 1.7 (tr. 19) · Lồng (cage) trái sang phải: tuyến tính, phần trăm bằng nhau, mở nhanh",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.7 - Cage window shapes: linear, equal-percentage, quick-opening"))
    return _fig(s,
                "Hình 1.7 (tr. 19) · Ba dạng lồng (cage) từ trái sang phải: tuyến tính "
                "(Linear), phần trăm bằng nhau (Equal-Percentage) và mở nhanh (Quick-Opening). "
                "Các cửa sở trên thành lồng quyết định đặc tính dòng của van.",
                "Figure 1.7 (p. 19) · Cages left to right: Linear, Equal-Percentage and "
                "Quick-Opening. The openings in the cage walls determine the flow "
                "characteristic of the control valve.",
                "Ba dạng lồng với cửa sở khác nhau quyết định đặc tính dòng của van",
                "Three cage window patterns that determine the valve flow characteristic")


@_reg
def fig_f08():
    """Figure 1.8 (p. 20) - Three-Way Globe Valve."""
    w, h = 520, 380
    o = [_defs()]
    o.append(_rect(150, 120, 180, 110, fill="#f4f7fb", sw=1.6))
    o.append(_rect(130, 146, 22, 30, fill="#e9eef4", sw=1.3))      # inlet A
    o.append(_rect(328, 146, 22, 30, fill="#e9eef4", sw=1.3))      # outlet B
    o.append(_rect(228, 228, 34, 60, fill="#e9eef4", sw=1.3))      # port C
    o.append(_line(240, 100, 240, 60, sw=2.4, color=INK))
    o.append(_poly([(228, 176), (252, 176), (246, 200), (234, 200)],
                   fill="#fdf3e6", sw=1.3, close=True))
    o.append(_arrow(150, 161, 200, 161, sw=1.6, color=GREEN))
    o.append(_arrow(280, 161, 340, 161, sw=1.6, color=GREEN))
    o.append(_arrow(245, 230, 245, 282, sw=1.6, color=GREEN))
    o.append(T(128, 136, "A", 8.6, color=GREEN))
    o.append(T(352, 136, "B", 8.6, color=GREEN))
    o.append(T(272, 300, "C", 8.6, color=GREEN))
    o.append(T(260, 362, "Hình 1.8 (tr. 20) · Van cầu ba cổng (three-way globe valve)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.8 - Three-way globe valve"))
    return _fig(s,
                "Hình 1.8 (tr. 20) · Van cầu ba cổng: van có một phần đóng chuyển động tuyến "
                "tính và ba kết nối dòng, dùng để gộp (hội tụ) hoặc tách (phân luồng) dòng.",
                "Figure 1.8 (p. 20) · Three-way globe valve: a valve with a linear-motion "
                "closure member and three flow connections, used for converging (mixing) or "
                "diverging (diverting) flows.",
                "Van cầu ba cổng dùng để gộp hoặc tách dòng",
                "Three-way globe valve used for mixing or diverting flow")


@_reg
def fig_f09():
    """Figure 1.9 (p. 20) - Direct-Acting Actuator."""
    w, h = 600, 460
    o = [_defs()]
    o.append(_ellipse(250, 60, 120, 26, fill="#eef3fb", sw=1.6))
    o.append(_line(130, 60, 370, 60, sw=2.2, color=BLUE))
    o.append(_line(250, 60, 250, 312, sw=2.6, color=INK))
    o.append(_spring(250, 76, 178, width=56))
    o.append(_rect(214, 178, 72, 20, fill="#dfe7ef", sw=1.2))
    o.append(_rect(196, 196, 108, 116, fill="none", sw=1.6))         # yoke
    o.append(_line(196, 312, 304, 312, sw=1.4, color=GREY))
    o.append(_rect(240, 312, 20, 32, fill="#e9eef4", sw=1.2))        # stem connector
    legend = ["Diaphragm Casing", "Diaphragm", "Diaphragm Plate", "Actuator Spring",
              "Actuator Stem", "Spring Seat", "Spring Adjuster", "Yoke",
              "Stem Connector", "Valve Stem", "Travel Indicator Disk", "Travel Scale"]
    for i, lab in enumerate(legend):
        o.append(_num(452, 44 + i * 32, i + 1))
        o.append(T(470, 48 + i * 32, lab, 7.6, anchor="start"))
    o.append(_arrow(360, 60, 300, 60, sw=1.0, color=GREY))
    o.append(T(250, 446, "Hình 1.9 (tr. 20) · Cơ cấu chấp hành màng tác động trực tiếp (direct-acting)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.9 - Direct-acting diaphragm actuator"))
    return _fig(s,
                "Hình 1.9 (tr. 20) · Cơ cấu chấp hành màng tác động trực tiếp: thân cơ cấu "
                "chấp hành dịch ra khi áp suất nạp tăng. Gồm vỏ màng, màng, đĩa màng, lò xo, "
                "thân, đế lò xo, vít chỉnh lò xo, ách (yoke), đầu nối thân, thân van, đĩa "
                "chỉ thị hành trình và thang đo hành trình (1-12).",
                "Figure 1.9 (p. 20) · Direct-acting diaphragm actuator: the actuator stem "
                "extends with increasing loading pressure. Shows diaphragm casing, diaphragm, "
                "diaphragm plate, spring, stem, spring seat, spring adjuster, yoke, stem "
                "connector, valve stem, travel indicator disk and travel scale (1-12).",
                "Cơ cấu chấp hành màng tác động trực tiếp với 12 chi tiết được quy chiếu",
                "Direct-acting diaphragm actuator with twelve numbered components")


@_reg
def fig_f10():
    """Figure 1.10 (p. 21) - Piston-Type Actuator."""
    w, h = 500, 380
    o = [_defs()]
    o.append(_rect(180, 50, 140, 170, fill="#eef3fb", sw=1.6))
    o.append(_rect(186, 120, 128, 24, fill="#dfe7ef", sw=1.4))       # piston
    o.append(_line(250, 120, 250, 300, sw=2.6, color=INK))
    o.append(_rect(238, 64, 24, 20, fill="#fdf3e6", sw=1.2))         # pressure conn.
    o.append(_rect(180, 220, 40, 14, fill="#dfe7ef", sw=1.2))
    o.append(_rect(280, 220, 40, 14, fill="#dfe7ef", sw=1.2))
    legend = ["Loading Pressure Connection", "Piston", "Piston Seal", "Cylinder",
              "Cylinder Closure Seal", "Seal Bushing", "Stem Connector"]
    for i, lab in enumerate(legend):
        o.append(_num(390, 62 + i * 38, i + 1))
        o.append(T(410, 66 + i * 38, lab, 7.6, anchor="start"))
    o.append(T(250, 364, "Hình 1.10 (tr. 21) · Cơ cấu chấp hành kiểu piston (piston-type actuator)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.10 - Piston-type actuator"))
    return _fig(s,
                "Hình 1.10 (tr. 21) · Cơ cấu chấp hành kiểu piston: chất lỏng (thường là khí nén) "
                "tác dụng lên piston di động để tạo chuyển động cho thân và lực đóng. Có thể là "
                "tác động kép hoặc kiểu lò xo an toàn (spring-fail). Các số 1-7 quy chiếu các "
                "bộ phận chính.",
                "Figure 1.10 (p. 21) · Piston-type actuator: fluid, usually compressed air, acts "
                "on a movable piston to produce actuator-stem motion and seating force; it may "
                "be double-acting or spring-fail. Numbers 1-7 call out the main parts.",
                "Cơ cấu chấp hành kiểu piston với piston trong xi lanh",
                "Piston-type actuator with a piston inside a cylinder")


@_reg
def fig_f11():
    """Figure 1.11 (p. 21) - Packing (PTFE and graphite)."""
    w, h = 680, 330
    o = [_defs()]
    o.append(T(170, 30, "PTFE Packing / Gioăng PTFE", 9.0, color=INK, weight="600"))
    o.append(T(510, 30, "Graphite Packing / Gioăng than chì", 9.0, color=INK, weight="600"))
    o.append(_rect(120, 56, 100, 210, fill="#f7f9fb", sw=1.3))
    o.append(_line(170, 48, 170, 280, sw=2.2, color=INK))
    for i in range(6):
        o.append(_poly([(132, 90 + i * 26), (208, 90 + i * 26),
                        (198, 108 + i * 26), (142, 108 + i * 26)],
                       fill="#eef3fb", sw=0.9, close=True))
    o.append(_rect(150, 150, 40, 18, fill="#dfe7ef", sw=1.1))
    ptfe = ["Upper Wiper", "Packing Follower", "Female Adaptor", "V-Ring",
            "Male Adaptor", "Lantern Ring", "Washer", "Spring", "Box Ring/Lower Wiper"]
    o.append(_legend(ptfe, 236, 70, lh=21, size=7.2))
    o.append(_rect(460, 56, 100, 210, fill="#f7f9fb", sw=1.3))
    o.append(_line(510, 48, 510, 280, sw=2.2, color=INK))
    for i in range(5):
        o.append(_rect(468, 84 + i * 32, 84, 14, fill="#e9eef4", sw=0.9))
    graph = ["Filament Ring", "Laminated Ring", "Lantern Ring", "Zinc Washer"]
    o.append(_legend(graph, 576, 88, lh=34, size=7.2))
    o.append(T(340, 314, "Hình 1.11 (tr. 21) · Bộ gioăng đệm: PTFE (trái) và than chì (phải)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.11 - Packing: PTFE and graphite arrangements"))
    return _fig(s,
                "Hình 1.11 (tr. 21) · Các kiểu gioăng đệm: PTFE gồm gờ lau trên, đĩa ép, "
                "đầu nối cái, vòng V, đầu nối đực, vòng lantern, vòng đệm, lò xo và vòng đáy; "
                "than chì gồm vòng sợi, vòng many lớp, vòng lantern và vòng kẽm.",
                "Figure 1.11 (p. 21) · Packing arrangements: PTFE packing with upper wiper, "
                "follower, female adaptor, V-ring, male adaptor, lantern ring, washer, spring "
                "and box ring; graphite packing with filament ring, laminated ring, lantern "
                "ring and zinc washer.",
                "Hai kiểu bộ gioăng đệm PTFE và than chì",
                "Two packing arrangements: PTFE and graphite")


@_reg
def fig_f12():
    """Figure 1.12 (p. 22) - Reverse-Acting Actuator."""
    w, h = 600, 460
    o = [_defs()]
    o.append(_ellipse(250, 60, 120, 26, fill="#eef3fb", sw=1.6))
    o.append(_line(130, 60, 370, 60, sw=2.2, color=BLUE))
    o.append(_line(250, 60, 250, 312, sw=2.6, color=INK))
    o.append(_rect(236, 60, 28, 44, fill="#dfe7ef", sw=1.2))          # seal bushing
    o.append(_spring(250, 110, 190, width=56))
    o.append(_rect(196, 190, 108, 122, fill="none", sw=1.6))
    o.append(_arrow(360, 60, 300, 60, sw=1.0, color=GREY))
    legend = ["Diaphragm Casing", "Diaphragm", "Diaphragm Plate", "Seal Bushing and O-rings",
              "Actuator Spring", "Actuator Stem", "Spring Seat", "Spring Adjuster",
              "Yoke", "Stem Connector", "Travel Indicator Disk", "Valve Stem",
              "Integrated Handwheel Mounting Bosses", "Integral Air Passage",
              "Integral DVC6200 Mounting Pad", "Travel Scale"]
    for i, lab in enumerate(legend):
        yy = 40 + i * 25
        o.append(_num(452, yy, i + 1))
        o.append(T(470, yy + 4, lab, 7.0, anchor="start"))
    o.append(T(250, 448, "Hình 1.12 (tr. 22) · Cơ cấu chấp hành tác động ngược (reverse-acting)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.12 - Reverse-acting diaphragm actuator"))
    return _fig(s,
                "Hình 1.12 (tr. 22) · Cơ cấu chấp hành tác động ngược: thân cơ cấu chấp hành "
                "thu vào khi áp suất nạp tăng; có vòng đệm kiểu seal bushing lắp ở đầu trên của "
                "ách (yoke) để chống rò áp nạp dọc thân. Hình cũng cho thấy các bửng lắp bánh "
                "tay, đường dẫn khí tích hợp và bệ lắp bộ định vị DVC6200.",
                "Figure 1.12 (p. 22) · Reverse-acting actuator: the actuator stem retracts with "
                "increasing loading pressure; a seal bushing is installed in the upper end of "
                "the yoke to prevent leakage of loading pressure along the stem. Integrated "
                "handwheel bosses, air passage and DVC6200 mounting pad are also shown.",
                "Cơ cấu chấp hành tác động ngược với vòng đệm seal bushing ở đầu trên",
                "Reverse-acting actuator with a seal bushing at the top of the yoke")


@_reg
def fig_f13():
    """Figure 1.13 (p. 23) - Rotary Control Valve."""
    w, h = 540, 380
    o = [_defs()]
    o.append(_circle(210, 200, 84, fill="#eef3fb", sw=2.0))
    o.append(_circle(210, 200, 52, fill="#ffffff", sw=1.4))
    o.append(_circle(210, 200, 30, fill="#f4f7fb", sw=1.2))
    o.append(_line(210, 200, 292, 200, sw=3.0, color=INK))
    o.append(_rect(330, 120, 120, 160, fill="#eef3fb", sw=1.6))
    o.append(_spring(390, 140, 230, width=40))
    o.append(_line(390, 200, 330, 200, sw=2.2, color=INK))
    o.append(_ellipse(390, 118, 56, 14, fill="#dfe7ef", sw=1.2))
    o.append(T(116, 304, "Flanged body & ball / Vòng bi & bi", 7.8))
    o.append(T(390, 106, "Actuator / Cơ cấu chấp hành", 7.8))
    o.append(T(270, 364, "Hình 1.13 (tr. 23) · Van điều khiển quay (rotary control valve)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.13 - Rotary control valve"))
    return _fig(s,
                "Hình 1.13 (tr. 23) · Van điều khiển quay: phần đóng (bi, đĩa hoặc nút lệch) "
                "quay trong dòng để điều chỉnh lưu lượng; ở đây là van bi với thân van có "
                "bích và cơ cấu chấp hành tác động qua cần quay.",
                "Figure 1.13 (p. 23) · Rotary control valve: the closure member (ball, disk or "
                "eccentric plug) rotates in the flow stream to control capacity; shown here as "
                "a ball valve with flanged body and an actuator working through a lever.",
                "Van điều khiển quay kiểu bi với thân có bích và cơ cấu chấp hành",
                "Rotary ball control valve with flanged body and actuator")


@_reg
def fig_f14():
    """Figure 1.14 (p. 24) - Segmented Ball."""
    w, h = 360, 320
    o = [_defs()]
    o.append(_path("M 70 170 A 110 110 0 0 1 290 170 L 290 170 "
                   "A 110 110 0 0 1 70 170 Z", fill="#f4f7fb", sw=1.6))
    o.append(_circle(180, 130, 76, fill="#eef3fb", sw=1.5))
    o.append(_path("M 180 130 L 180 54 A 76 76 0 0 1 248 182 Z",
                   fill="#dfe7ef", sw=1.2))
    o.append(_line(40, 170, 320, 170, sw=2.4, color=INK))
    o.append(T(180, 250, "Partial sphere with flow passage", 8.0))
    o.append(T(180, 300, "Hình 1.14 (tr. 24) · Bi phân đoạn (segmented ball)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.14 - Segmented ball"))
    return _fig(s,
                "Hình 1.14 (tr. 24) · Bi phân đoạn: phần đóng của van quay dùng một hình cầu "
                "một phần có lỗ dòng chảy xuyên qua.",
                "Figure 1.14 (p. 24) · Segmented ball: the flow closure member of a rotary "
                "control valve using a partial sphere with a flow passage through it.",
                "Bi phân đoạn dùng làm phần đóng trong van quay",
                "Segmented ball used as the closure member of a rotary valve")


@_reg
def fig_f15():
    """Figure 1.15 (p. 24) - V-Notch Ball."""
    w, h = 460, 320
    o = [_defs()]
    o.append(_circle(230, 150, 88, fill="#eef3fb", sw=1.8))
    o.append(_poly([(230, 150), (230, 66), (296, 196), (230, 196)],
                   fill="#dfe7ef", sw=1.2, close=True))
    o.append(_line(40, 150, 420, 150, sw=3.0, color=INK))
    o.append(_poly([(230, 150), (286, 150), (230, 106)], fill="#ffffff", sw=1.3, close=True))
    o.append(T(230, 270, "V-notch / Rãnh chữ V - wide rangeability", 8.2, color=BLUE))
    o.append(T(230, 306, "Hình 1.15 (tr. 24) · Bi rãnh V (V-notch ball)", 7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.15 - V-notch ball"))
    return _fig(s,
                "Hình 1.15 (tr. 24) · Bi rãnh V: dạng bi phân đoạn phổ biến nhất, có bề mặt "
                "cầu được đánh bóng hoặc mạ và rãnh hình chữ V cho dải điều chỉnh rộng, tạo "
                "đặc tính dòng phần trăm bằng nhau.",
                "Figure 1.15 (p. 24) · V-notch ball: the most common segmented-ball type, with "
                "a polished or plated partial-sphere surface and a V-shaped notch that permits "
                "wide rangeability and an equal-percentage flow characteristic.",
                "Bi có rãnh hình chữ V tạo dải điều chỉnh rộng và đặc tính phần trăm bằng nhau",
                "V-notch ball giving wide rangeability and an equal-percentage characteristic")


@_reg
def fig_f16():
    """Figure 1.16 (p. 24) - Eccentric Disk Valve."""
    w, h = 500, 360
    o = [_defs()]
    o.append(_circle(180, 180, 100, fill="#eef3fb", sw=2.0))
    for i in range(12):
        a = 2 * math.pi * i / 12
        o.append(_circle(180 + 100 * math.cos(a), 180 + 100 * math.sin(a), 5,
                         fill="#dfe7ef", sw=0.8))
    o.append(_ellipse(180, 180, 66, 78, fill="#f4f7fb", sw=1.4))
    o.append(_line(180, 180, 292, 180, sw=3.0, color=INK))          # offset shaft
    o.append(_rect(320, 120, 110, 120, fill="#eef3fb", sw=1.6))
    o.append(_spring(375, 138, 214, width=36))
    o.append(T(150, 304, "Offset shaft / Trục lệch tâm", 7.8))
    o.append(T(250, 344, "Hình 1.16 (tr. 24) · Van đĩa lệch tâm (eccentric disk valve)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.16 - Eccentric disk valve"))
    return _fig(s,
                "Hình 1.16 (tr. 24) · Van đĩa lệch tâm: vị trí lệch tâm của điểm nối trục/đĩa "
                "khiến đĩa đi theo đường cong cam khi mở, nhờ đó đĩa thoát khỏi chỗ kín ngay "
                "khi mở, giảm ma sát và mòn.",
                "Figure 1.16 (p. 24) · Eccentric disk valve: off-centre shaft/disk positioning "
                "makes the disk follow a cammed path on opening, swinging it out of contact "
                "with the seal as soon as it opens and reducing friction and wear.",
                "Van đĩa lệch tâm với trục lệch làm đĩa thoát chỗ kín khi mở",
                "Eccentric disk valve whose offset shaft lifts the disk off the seal on opening")


@_reg
def fig_f17():
    """Figure 1.17 (p. 25) - Rotary Control Valve, cross-section."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_ellipse(300, 60, 78, 20, fill="#eef3fb", sw=1.5))
    o.append(_line(222, 60, 378, 60, sw=2.0, color=BLUE))
    o.append(_spring(300, 76, 150, width=44))
    o.append(_rect(264, 150, 72, 84, fill="none", sw=1.5))
    o.append(_line(300, 150, 300, 250, sw=2.4, color=INK))
    o.append(_line(300, 250, 372, 250, sw=2.4, color=INK))          # lever
    o.append(_line(372, 250, 372, 280, sw=2.4, color=INK))
    o.append(_line(150, 280, 372, 280, sw=3.0, color=INK))          # shaft
    o.append(_circle(210, 280, 58, fill="#eef3fb", sw=1.8))
    o.append(_ellipse(210, 280, 20, 56, fill="#f4f7fb", sw=1.4))    # disk
    o.append(_rect(160, 336, 100, 14, fill="#dfe7ef", sw=1.0))      # seal
    legend = ["Loading Pressure Connection", "Diaphragm Case", "Diaphragm",
              "Diaphragm Plate", "Spring", "Actuator Stem", "Lever", "Shaft",
              "Travel Stop", "Packing", "Disk", "Body", "Seal", "Seal Retainer"]
    for i, lab in enumerate(legend):
        yy = 36 + i * 26
        o.append(_num(520, yy, i + 1))
        o.append(T(538, yy + 4, lab, 7.2, anchor="start"))
    o.append(T(250, 414, "Hình 1.17 (tr. 25) · Van điều khiển quay, mặt cắt (1-14)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.17 - Rotary control valve cross-section"))
    return _fig(s,
                "Hình 1.17 (tr. 25) · Van điều khiển quay, mặt cắt: cơ cấu chấp hành màng "
                "ở trên, cần quay nối thân với đĩa, thân van có đĩa, chỗ kín và vòng giữ chỗ "
                "kín. Các số 1-14 quy chiếu: đầu nối áp nạp, vỏ màng, màng, đĩa màng, lò xo, "
                "thân cơ cấu, cần, trục, chặn hành trình, gioăng đệm, đĩa, thân van, chỗ kín "
                "và vòng giữ chỗ kín.",
                "Figure 1.17 (p. 25) · Rotary control valve cross-section: diaphragm actuator "
                "above, lever linking stem to disk, and a body carrying the disk, seal and seal "
                "retainer. Numbers 1-14 call out loading-pressure connection, diaphragm case, "
                "diaphragm, diaphragm plate, spring, actuator stem, lever, shaft, travel stop, "
                "packing, disk, body, seal and seal retainer.",
                "Mặt cắt van điều khiển quay với 14 chi tiết được quy chiếu",
                "Cross-section of a rotary control valve with fourteen numbered parts")


@_reg
def fig_f18():
    """Figure 1.18 (p. 29) - Deadband."""
    w, h = 560, 340
    o = [_defs()]
    x0, y0, W, H = 90, 40, 400, 240
    o.append(_arrow(x0, y0 + H, x0 + W + 20, y0 + H, sw=1.3))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1.3))
    o.append(T(x0 - 8, y0 - 18, "100%", 7.4, anchor="end", color=GREY))
    o.append(T(x0 + W + 14, y0 + H + 16, "100%", 7.4, anchor="end", color=GREY))
    o.append(T(x0 + W / 2, y0 + H + 34, "Controller Output / Đầu ra bộ điều khiển", 8.4))
    o.append(T(x0 - 58, 24, "Process Variable", 8.4, anchor="start"))
    o.append(T(x0 - 58, 36, "Biến quá trình", 8.4, anchor="start"))
    o.append(_line(x0, y0 + 6, x0 + W, y0 + 6, sw=1.0, dash="6 4", color=GREY))
    # blue response: low flat, then sharp rise at full output
    o.append(_line(x0 + 4, y0 + H - 6, x0 + W - 14, y0 + H - 6, sw=2.6, color=BLUE))
    o.append(_arrow(x0 + W - 6, y0 + H - 8, x0 + W - 6, y0 + 12, sw=2.6, color=BLUE))
    # the deadband loop in the middle
    o.append(_line(x0 + 150, y0 + 118, x0 + 250, y0 + 118, sw=1.0, dash="5 4", color=INK))
    o.append(_arrow(x0 + 220, y0 + 112, x0 + 160, y0 + 112, sw=1.0, color=INK))
    o.append(_arrow(x0 + 180, y0 + 126, x0 + 240, y0 + 126, sw=1.0, color=INK))
    o.append(T(x0 + 200, y0 + 104, "Deadband / Vùng chết", 8.0, color=INK))
    o.append(T(280, 326, "Hình 1.18 (tr. 29) · Vùng chết (deadband) của van điều khiển",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.18 - Deadband"))
    return _fig(s,
                "Hình 1.18 (tr. 29) · Vùng chết (deadband): miền đầu ra mà trong đó đổi chiều "
                "tín hiệu đầu vào không gây ra thay đổi observable ở đầu ra. Với van điều "
                "khiển, đầu vào là đầu ra bộ điều khiển (CO) và đầu ra là biến quá trình (PV); "
                "deadband thường được thể hiện bằng phần trăm dải đầu vào.",
                "Figure 1.18 (p. 29) · Deadband: the range through which an input signal can be "
                "varied, upon reversal of direction, without an observable change in output. "
                "For control valves the input is controller output (CO) and the output is the "
                "process variable (PV); deadband is typically expressed as a percent of input span.",
                "Đồ thị vùng chết với đầu ra bộ điều khiển và biến quá trình",
                "Deadband plot with controller output and process variable axes")


@_reg
def fig_f19():
    """Figure 1.19 (p. 30) - Inherent Valve Characteristics."""
    w, h = 560, 400
    o = [_defs()]
    x0, y0, W, H = 80, 40, 400, 300
    for g in range(1, 5):
        o.append(_line(x0 + g * W / 5, y0, x0 + g * W / 5, y0 + H,
                       sw=0.7, color="#d8dde3"))
        o.append(_line(x0, y0 + g * H / 5, x0 + W, y0 + g * H / 5,
                       sw=0.7, color="#d8dde3"))
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1.3))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1.3))
    o.append(T(x0 - 10, y0 - 18, "100", 7.4, anchor="end", color=GREY))
    o.append(T(x0 + W + 12, y0 + H + 16, "100", 7.4, anchor="end", color=GREY))
    o.append(T(x0, y0 + H + 32, "0", 7.4, color=GREY))
    o.append(T(x0 + W / 2, y0 + H + 48, "Rated Travel (%) / Hành trình định mức (%)", 8.4))
    o.append(T(x0 - 56, 24, "Rated Flow Coefficient (%)", 8.2, anchor="start"))
    o.append(T(x0 - 56, 36, "Hệ số dòng định mức (%)", 8.2, anchor="start"))
    # curves
    n = 60
    quick = [(x0 + W * i / n, y0 + H - H * (1 - (1 - i / n) ** 3)) for i in range(n + 1)]
    linear = [(x0 + W * i / n, y0 + H - H * i / n) for i in range(n + 1)]
    k = 3.0
    eq = [(x0 + W * i / n, y0 + H - H * (math.exp(k * i / n) - 1) / (math.exp(k) - 1))
          for i in range(n + 1)]
    o.append(_poly(quick, sw=2.2, color=BLUE))
    o.append(_poly(linear, sw=2.2, color=INK))
    o.append(_poly(eq, sw=2.2, color=RED))
    o.append(T(x0 + 70, y0 + 44, "Quick-Opening / Mở nhanh", 8.0, color=BLUE))
    o.append(T(x0 + 214, y0 + 176, "Linear / Tuyến tính", 8.0, color=INK))
    o.append(T(x0 + 250, y0 + 274, "Equal-Percentage / Phần trăm bằng nhau", 8.0, color=RED))
    o.append(T(280, 392, "Hình 1.19 (tr. 30) · Đặc tính van vốn có: mở nhanh, tuyến tính, phần trăm bằng nhau",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.19 - Inherent valve characteristics"))
    return _fig(s,
                "Hình 1.19 (tr. 30) · Đặc tính dòng vốn có của van: quan hệ giữa hệ số dòng "
                "(Cv) và phần trăm hành trình định mức ở áp suất không đổi gồm ba dạng: mở "
                "nhanh (đạt Cv lớn nhất với hành trình rất nhỏ), tuyến tính (Cv tăng đều theo "
                "hành trình) và phần trăm bằng nhau (mỗi bước hành trình tăng Cv lên một tỉ "
                "lệ phần trăm bằng nhau).",
                "Figure 1.19 (p. 30) · Inherent valve flow characteristics: the relation between "
                "flow coefficient (Cv) and percent rated travel at constant pressure drop comes "
                "in three forms - quick-opening (maximum Cv at minimal travel), linear (equal "
                "increments of Cv per travel increment) and equal-percentage (equal-percentage "
                "change of Cv per travel increment).",
                "Ba đường đặc tính van vốn có: mở nhanh, tuyến tính và phần trăm bằng nhau",
                "Three inherent valve characteristic curves: quick-opening, linear and equal-percentage")


# ===========================================================================
# Chapter 2 - Control Valve Performance (source printed pp. 34-53)
# Figures 2.1-2.10. All are redrawn as clean simplified vector schematics.
# ===========================================================================

@_reg
def fig_f21():
    """Figure 2.1 (p. 35) - Process Variability."""
    w, h = 640, 300
    o = [_defs()]
    x0, y0, W, H = 70, 34, 520, 170
    for g in range(1, 5):
        o.append(_line(x0, y0 + H * g / 5.0, x0 + W, y0 + H * g / 5.0,
                       sw=0.6, color="#d8dde3"))
    o.append(_arrow(x0, y0 + H, x0 + W + 18, y0 + H, sw=1.2))
    o.append(_arrow(x0, y0 + H, x0, y0 - 12, sw=1.2))
    cy = y0 + H / 2.0
    band = 30
    o.append(_rect(x0, cy - band, W, 2 * band, fill="#e8f1f7", sw=0))
    o.append(_line(x0, cy, x0 + W, cy, sw=1.1, dash="5 4", color=BLUE))
    o.append(_line(x0, y0 + H - 12, x0 + W, y0 + H - 12,
                   sw=1.1, dash="4 3", color=RED))
    pts = []
    for i in range(121):
        x = x0 + W * i / 120.0
        y = cy + 9 * math.sin(i * 0.55) + 5 * math.sin(i * 1.7) + 3 * math.sin(i * 3.1)
        pts.append((x, y))
    o.append(_poly(pts, sw=1.8, color=INK))
    o.append(T(x0 + W + 5, cy + 3, "Set Point", 7.5, color=BLUE, anchor="start"))
    o.append(T(x0 + W + 5, cy - band + 3, "+2 sigma", 7.3, color=BLUE, anchor="start"))
    o.append(T(x0 + W + 5, cy + band + 3, "-2 sigma", 7.3, color=BLUE, anchor="start"))
    o.append(T(x0 + 6, y0 + H - 18, "Lower specification limit", 7.3,
               color=RED, anchor="start"))
    o.append(T(x0 + W / 2, y0 + H + 18, "Time", 8.2))
    o.append(T(x0 - 12, y0 - 17, "Process Variable (PV)", 8.0,
               color=INK, anchor="start"))
    o.append(T(320, 280,
               "Hình 2.1 (tr. 35) · Biến thiên quá trình quanh điểm đặt trong dải +/-2 sigma",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.1 - Process variability"))
    return _fig(s,
                "Hình 2.1 (tr. 35) · Biến thiên quá trình: đường biến quá trình (PV) dao động "
                "quanh điểm đặt; dải +/-2 sigma mô tả độ phân tán của sai lệch so với điểm đặt "
                "và là thước đo mức độ chặt chẽ của điều khiển. Giới hạn đặc tính dưới nằm "
                "thấp hơn dải này; dùng van có sigma nhỏ hơn sẽ thu hẹp dải phân tán.",
                "Figure 2.1 (p. 35) · Process variability: the process variable (PV) fluctuates "
                "about the set point; the +/-2 sigma band describes the spread of deviations "
                "from the set point and measures how tightly the process is controlled. The "
                "lower specification limit lies below the band; a valve with a smaller sigma "
                "narrows the spread.",
                "Đường biến quá trình nhiễu quanh điểm đặt, có dải +/-2 sigma và giới hạn đặc tính dưới",
                "Noisy process variable trace about a set point with a +/-2 sigma band and lower specification limit")


@_reg
def fig_f22():
    """Figure 2.2 (p. 36) - Performance Test Loop."""
    w, h = 640, 290
    o = [_defs()]
    boxes = [(36, 54, 124, 46, "Controller"), (228, 54, 132, 46, "Control Valve"),
             (432, 54, 132, 46, "Process"), (432, 190, 132, 46, "Sensor / Transmitter")]
    for x, y, bw, bh, lab in boxes:
        o.append(_rect(x, y, bw, bh, fill="#e9edf2", sw=1.2))
        o.append(T(x + bw / 2, y + bh / 2 + 3, lab, 8.6, weight="600"))
    o.append(_arrow(160, 77, 228, 77, sw=1.5, color=BLUE))
    o.append(T(194, 69, "CO", 7.6, color=BLUE))
    o.append(_arrow(360, 77, 432, 77, sw=1.5, color=BLUE))
    o.append(T(396, 69, "Flow", 7.6, color=BLUE))
    o.append(_arrow(498, 28, 498, 54, sw=1.4, color=RED))
    o.append(T(508, 40, "Load disturbance", 7.4, color=RED, anchor="start"))
    o.append(_line(498, 100, 498, 190, sw=1.4, color=GREY))
    o.append(_arrow(498, 166, 498, 190, sw=1.4, color=GREY))
    o.append(T(508, 148, "PV", 7.4, color=GREY, anchor="start"))
    o.append(_line(432, 213, 98, 213, sw=1.4, color=GREY))
    o.append(_arrow(98, 213, 98, 104, sw=1.4, color=GREY))
    o.append(T(254, 205, "Feedback signal", 7.4, color=GREY))
    o.append(T(320, 262, "Hình 2.2 (tr. 36) · Vòng thử nghiệm hiệu năng trong điều khiển vòng kín",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.2 - Performance test loop"))
    return _fig(s,
                "Hình 2.2 (tr. 36) · Vòng thử nghiệm hiệu năng: bộ điều khiển gửi tín hiệu đầu "
                "ra (CO) tới van điều khiển, van điều chỉnh lưu lượng qua quá trình, cảm biến "
                "và bộ phát đo biến quá trình (PV) rồi phản hồi về bộ điều khiển. Nhiễu tải "
                "tác động vào quá trình; thử nghiệm vòng kín là cách duy nhất đo đúng hiệu "
                "năng biến thiên của cụm van.",
                "Figure 2.2 (p. 36) · Performance test loop: a controller sends its output (CO) "
                "to the control valve, the valve manipulates flow through the process, and a "
                "sensor and transmitter measure the process variable (PV) and feed it back to "
                "the controller. A load disturbance enters the process; closed-loop testing is "
                "the only true measure of valve variability performance.",
                "Sơ đồ vòng thử nghiệm vòng kín gồm bộ điều khiển, van, quá trình, cảm biến và phản hồi",
                "Closed-loop test block diagram with controller, valve, process, sensor and feedback")


@_reg
def fig_f23():
    """Figure 2.3 (p. 37) - Effect of Deadband on Valve Performance."""
    w, h = 660, 430
    o = [_defs()]
    o.append(T(330, 18, "Step inputs: 0.5%, 1%, 2%, 5%, 10% (increasing step size)",
               8.4))
    o.append(T(126, 34, "Dashed = controller output (CO)", 7.4,
               color=BLUE, anchor="start"))
    o.append(T(386, 34, "Solid = flow response (PV)", 7.4, color=RED, anchor="start"))
    x0, W = 96, 520
    amps = [0.5, 1.0, 2.0, 5.0, 10.0]
    cum = [0.0]
    for a in amps:
        cum.append(cum[-1] + a)
    tt = [0, 20, 36, 52, 68, 84, 100]
    lev = cum + [cum[-1]]

    def step_poly(levels, ymap):
        pts = []
        for i, t in enumerate(tt):
            px = x0 + W * t / 100.0
            if i > 0:
                pts.append((px, ymap(levels[i - 1])))
            pts.append((px, ymap(levels[i])))
        return pts

    rows = [(52, "Valve A - responds to steps as small as 0.5%", 0.5),
            (182, "Valve B - responds only to 5% and 10% steps", 5.0),
            (312, "Valve C - responds only to the 10% step", 10.0)]
    for yt, lab, th in rows:
        yb = yt + 62
        o.append(_line(x0, yb, x0 + W, yb, sw=0.9, color="#c8ced6"))
        ymap = lambda v, yb=yb: yb - 56 * v / 20.0
        o.append(T(x0, yt - 8, lab, 8.4, color=INK, anchor="start"))
        o.append(_poly(step_poly(lev, ymap), sw=1.4, color=BLUE, dash="4 3"))
        rl = [0.0]
        for a in amps:
            rl.append(rl[-1] + (a if a >= th else 0.0))
        rl.append(rl[-1])
        o.append(_poly(step_poly(rl, ymap), sw=1.9, color=RED))
    o.append(T(330, 418,
               "Hình 2.3 (tr. 37) · Ảnh hưởng của vùng chết: đáp ứng lưu lượng của ba van với cùng chuỗi bước đầu vào",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.3 - Effect of deadband on valve performance"))
    return _fig(s,
                "Hình 2.3 (tr. 37) · Ảnh hưởng của vùng chết tới hiệu năng van: thí nghiệm vòng "
                "hở với chuỗi bước đầu vào 0,5% đến 10%. Chuyển động thân cơ cấu chấp hành của "
                "cả ba van đều bám tín hiệu, nhưng lưu lượng chỉ đáp ứng đúng với van A (0,5%); "
                "van B cần 5% và van C cần 10% mới bắt đầu đáp ứng.",
                "Figure 2.3 (p. 37) · Effect of deadband on valve performance: an open-loop test "
                "with input steps from 0.5% to 10%. Actuator stem motion tracks the input in all "
                "three valves, but flow responds faithfully only for Valve A (0.5%); Valve B "
                "needs 5% and Valve C needs 10% before responding.",
                "Ba bộ đồ thị so sánh tín hiệu đầu vào và đáp ứng lưu lượng của van A, B, C",
                "Three trace panels comparing input signal and flow response for valves A, B and C")


@_reg
def fig_f24():
    """Figure 2.4 (p. 41) - Valve Response Time Summary."""
    w, h = 660, 430
    o = [_defs()]
    x0, y0, W, H = 80, 32, 250, 140
    o.append(_rect(x0, y0, W, H, fill="#fbfcfd", sw=0.9))
    o.append(_line(x0, y0 + H, x0 + W, y0 + H, sw=1.0))
    o.append(_line(x0, y0, x0, y0 + H, sw=1.0))
    o.append(_poly([(x0 + 20, y0 + H - 6), (x0 + 30, y0 + H - 6),
                    (x0 + 30, y0 + 12), (x0 + W - 8, y0 + 12)],
                   sw=1.3, color=BLUE, dash="4 3"))
    td_x, t63_x = x0 + 58, x0 + 120
    pts = [(x0 + 20, y0 + H - 6), (td_x, y0 + H - 6)]
    for i in range(41):
        xx = td_x + 132 * i / 40.0
        frac = 1 - math.exp(-(xx - td_x) / 52.0)
        pts.append((xx, y0 + H - 6 - (H - 30) * frac))
    o.append(_poly(pts, sw=2.0, color=INK))
    y63 = y0 + H - 6 - (H - 30) * 0.63
    o.append(_line(x0, y63, x0 + W, y63, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(td_x, y0 + H, td_x, y0 + 8, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(t63_x, y0 + H, t63_x, y0 + 8, sw=0.8, dash="3 3", color=GREY))
    o.append(T(td_x + 3, y0 + 20, "T(d)", 7.4, color=GREY, anchor="start"))
    o.append(T(t63_x + 3, y0 + 20, "T63", 7.4, color=GREY, anchor="start"))
    o.append(T(x0 + 3, y63 - 4, "63%", 7.2, color=GREY, anchor="start"))
    o.append(T(x0 + W / 2, y0 - 10, "Step response: dead time plus dynamic time", 8.4))
    bx, by, bW, bH = 110, 214, 500, 120
    o.append(_line(bx, by + bH, bx + bW, by + bH, sw=1.0))
    o.append(_line(bx, by, bx, by + bH, sw=1.0))
    for v in (0, 2, 4, 6, 8):
        yy = by + bH - bH * v / 8.0
        o.append(_line(bx - 4, yy, bx, yy, sw=0.8))
        o.append(T(bx - 8, yy + 3, str(v), 7.2, color=GREY, anchor="end"))
    o.append(T(bx - 34, by - 8, "T63 (s)", 7.6, color=GREY, anchor="start"))
    vals = [(0.34, "A open", "#cddce8"), (0.74, "A close", "#cddce8"),
            (7.74, "B open", "#e6d4c2"), (1.67, "B close", "#e6d4c2"),
            (5.49, "C open", "#d8e6d2"), (3.90, "C close", "#d8e6d2")]
    for i, (v, lab, fill) in enumerate(vals):
        x = bx + 25 + i * 82
        bh = bH * v / 8.0
        o.append(_rect(x, by + bH - bh, 44, bh, fill=fill, sw=1.0))
        o.append(T(x + 22, by + bH - bh - 4, "%.2f" % v, 7.2))
        o.append(T(x + 22, by + bH + 16, lab, 7.4))
    o.append(T(330, 414,
               "Hình 2.4 (tr. 41) · Tóm tắt thời gian đáp ứng: T(d), T63 và so sánh ba van theo số liệu thử nghiệm",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.4 - Valve response time summary"))
    return _fig(s,
                "Hình 2.4 (tr. 41) · Tóm tắt thời gian đáp ứng của van: T63 đo từ lúc đầu vào "
                "thay đổi đến lúc đầu ra đạt 63% giá trị thay đổi, gồm thời gian chết T(d) và "
                "thời gian động. Biểu đồ cột so sánh T63 theo số liệu bảng nguồn cho van A, B, "
                "C ở chiều mở và đóng.",
                "Figure 2.4 (p. 41) · Valve response time summary: T63 is measured from the "
                "input change until the output reaches 63% of the change, including dead time "
                "T(d) and dynamic time. The bars compare source-table T63 values for Valves A, "
                "B and C in the opening and closing directions.",
                "Đồ thị thời gian đáp ứng T63 gồm đoạn chết và đoạn động, kèm biểu đồ cột so sánh ba van",
                "Step response showing dead time and dynamic time plus a bar chart comparing three valves")


@_reg
def fig_f25():
    """Figure 2.5 (p. 44) - Installed Flow Characteristic and Gain."""
    w, h = 660, 430
    o = [_defs()]
    x0, y0, W, H = 76, 30, 520, 150
    for g in range(1, 5):
        o.append(_line(x0 + W * g / 5.0, y0, x0 + W * g / 5.0, y0 + H,
                       sw=0.6, color="#d8dde3"))
        o.append(_line(x0, y0 + H * g / 5.0, x0 + W, y0 + H * g / 5.0,
                       sw=0.6, color="#d8dde3"))
    o.append(_rect(x0 + W * 0.25, y0, W * 0.40, H, fill="#eef5ee", sw=0))
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1.1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.1))
    flow = [1000.0 / (1 + math.exp(-(t - 45) / 11.0)) for t in range(101)]
    fp = [(x0 + W * t / 100.0, y0 + H - H * flow[t] / 1000.0) for t in range(101)]
    o.append(_poly(fp, sw=2.1, color=BLUE))
    o.append(T(x0 + 8, y0 + 14, "Flow (gpm)", 7.6, color=BLUE, anchor="start"))
    o.append(T(x0 + W * 0.45, y0 + 44, "Installed Characteristic", 8.0, color=BLUE))
    y0b, Hb = 214, 118
    o.append(_rect(x0 + W * 0.25, y0b, W * 0.40, Hb, fill="#eef5ee", sw=0))
    for g in range(1, 4):
        o.append(_line(x0, y0b + Hb * g / 4.0, x0 + W, y0b + Hb * g / 4.0,
                       sw=0.6, color="#d8dde3"))
    o.append(_arrow(x0, y0b + Hb, x0 + W + 16, y0b + Hb, sw=1.1))
    o.append(_arrow(x0, y0b + Hb, x0, y0b - 10, sw=1.1))
    for v in (0.5, 2.0):
        yy = y0b + Hb - Hb * v / 3.2
        o.append(_line(x0, yy, x0 + W, yy, sw=0.9, dash="4 3", color=RED))
        o.append(T(x0 + W + 4, yy + 3, "%.1f" % v, 7.2, color=RED, anchor="start"))
    gp = []
    for t in range(101):
        g = 3.0 * math.exp(-((t - 45) / 22.0) ** 2)
        gp.append((x0 + W * t / 100.0, y0b + Hb - Hb * g / 3.2))
    o.append(_poly(gp, sw=2.1, color=INK))
    o.append(T(x0 + 8, y0b + 14, "Gain (% Flow / % Input)", 7.6,
               color=INK, anchor="start"))
    o.append(T(x0 + W * 0.40, y0b + 34, "Installed Gain", 8.0, color=INK))
    o.append(T(x0 + W * 0.26, y0b + Hb - 12, "Control Range", 7.6,
               color=GREEN, anchor="start"))
    for t in (0, 20, 40, 60, 80, 100):
        o.append(T(x0 + W * t / 100.0, y0b + Hb + 16, str(t), 7.4, color=GREY))
    o.append(T(x0 + W / 2, y0b + Hb + 32, "Valve Travel (%)", 8.2))
    o.append(T(330, 414,
               "Hình 2.5 (tr. 44) · Đặc tính dòng lắp đặt và hệ số khuếch đại: đường trên là lưu lượng, đường dưới là độ dốc (installed gain)",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.5 - Installed flow characteristic and gain"))
    return _fig(s,
                "Hình 2.5 (tr. 44) · Đặc tính dòng lắp đặt và hệ số khuếch đại: đường trên cho "
                "lưu lượng theo hành trình van khi độ chụt áp thay đổi tự nhiên; đường dưới là "
                "độ dốc của đường trên, tức installed gain. Vùng giữa hai giới hạn 0,5 và 2,0 "
                "là dải điều khiển.",
                "Figure 2.5 (p. 44) · Installed flow characteristic and gain: the upper curve is "
                "flow versus valve travel with the pressure drop free to change; the lower curve "
                "is its slope, the installed gain. The region between the 0.5 and 2.0 limits is "
                "the control range.",
                "Hai đồ thị xếp chồng: đặc tính dòng lắp đặt ở trên và độ dốc installed gain ở dưới",
                "Two stacked plots: installed flow characteristic above and its installed gain below")


@_reg
def fig_f26():
    """Figure 2.6 (p. 46) - Effect of Valve Style on Control Range."""
    w, h = 660, 400
    o = [_defs()]
    x0, y0, W, H = 80, 34, 520, 240

    def Y(v):
        return y0 + H - H * v / 3.2

    for g in range(1, 5):
        o.append(_line(x0 + W * g / 5.0, y0, x0 + W * g / 5.0, y0 + H,
                       sw=0.6, color="#d8dde3"))
        o.append(_line(x0, y0 + H * g / 5.0, x0 + W, y0 + H * g / 5.0,
                       sw=0.6, color="#d8dde3"))
    o.append(_rect(x0, Y(2.0), W, Y(0.5) - Y(2.0), fill="#eef5ee", sw=0))
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1.1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.1))
    for v in (0.5, 1.0, 2.0):
        o.append(_line(x0, Y(v), x0 + W, Y(v), sw=0.8, dash="4 3", color=RED))
        o.append(T(x0 + W + 4, Y(v) + 3, "%.1f" % v, 7.2, color=RED, anchor="start"))
    globe = [(x0 + W * t / 100.0, Y(1.0 + 0.12 * math.sin(t / 16.0)))
             for t in range(5, 96)]
    butte = [(x0 + W * t / 100.0, Y(2.5 * math.exp(-((t - 48) / 6.0) ** 2)))
             for t in range(101)]
    o.append(_poly(globe, sw=2.2, color=BLUE))
    o.append(_poly(butte, sw=2.2, color=RED))
    o.append(T(x0 + W * 0.72, Y(1.3) - 8, "Globe - wide control range", 8.0,
               color=BLUE, anchor="start"))
    o.append(T(x0 + W * 0.53, Y(2.6) - 6, "Butterfly", 8.0, color=RED))
    o.append(T(x0 + 8, y0 + 14, "Installed Gain (% Flow / % Input)", 7.8,
               color=INK, anchor="start"))
    for t in (0, 20, 40, 60, 80, 100):
        o.append(T(x0 + W * t / 100.0, y0 + H + 16, str(t), 7.4, color=GREY))
    o.append(T(x0 + W / 2, y0 + H + 32, "Valve Travel (%)", 8.2))
    o.append(T(330, 380,
               "Hình 2.6 (tr. 46) · Ảnh hưởng của kiểu van tới dải điều khiển: van cầu có dải rộng hơn bướm",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.6 - Effect of valve style on control range"))
    return _fig(s,
                "Hình 2.6 (tr. 46) · Ảnh hưởng của kiểu van tới dải điều khiển. So sánh van bướm "
                "và van cầu cùng cỡ đường ống: với van cầu, hệ số khuếch đại lắp đặt nằm trong "
                "giới hạn EnTech 0,5 đến 2,0 trên dải hành trình rộng; van bướm chỉ đạt được "
                "điều đó trong một dải hẹp.",
                "Figure 2.6 (p. 46) · Effect of valve style on control range. A line-size butterfly "
                "valve is compared with a line-size globe valve: the globe valve keeps its "
                "installed gain within the EnTech 0.5 to 2.0 limits over a much wider travel "
                "range, while the butterfly valve meets them only in a narrow band.",
                "Đồ thị hệ số khuếch đại lắp đặt so sánh dải điều khiển của van cầu và van bướm",
                "Installed gain chart comparing the control ranges of globe and butterfly valves")


@_reg
def fig_f27():
    """Figure 2.7 (p. 49) - Closed Loop Random Load Disturbance Summary."""
    w, h = 640, 380
    o = [_defs()]
    x0, y0, W, H = 80, 34, 500, 250
    for v in range(0, 7):
        yy = y0 + H - H * v / 6.0
        o.append(_line(x0, yy, x0 + W, yy, sw=0.6, color="#d8dde3"))
        o.append(T(x0 - 8, yy + 3, str(v), 7.2, color=GREY, anchor="end"))
    for t in (1, 2, 5, 10):
        xx = x0 + W * math.log(t) / math.log(10.0)
        o.append(_line(xx, y0, xx, y0 + H, sw=0.6, color="#d8dde3"))
        o.append(T(xx, y0 + H + 16, str(t), 7.4, color=GREY))
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1.1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.1))
    o.append(T(x0 + W / 2, y0 + H + 34, "Closed-Loop Time Constant (seconds)", 8.2))
    o.append(T(x0 - 14, y0 - 18, "Variability, sigma (% of set point)", 7.8,
               color=INK, anchor="start"))
    o.append(_line(x0, y0 + H - H * 5.5 / 6.0, x0 + W, y0 + H - H * 5.5 / 6.0,
                   sw=1.3, dash="5 4", color=GREY))
    o.append(T(x0 + 6, y0 + H - H * 5.5 / 6.0 - 6, "Manual (open loop)", 7.4,
               color=GREY, anchor="start"))

    def X(t):
        return x0 + W * math.log(t) / math.log(10.0)

    def Y(v):
        return y0 + H - H * v / 6.0

    minp = [(X(1 + 9 * i / 60.0), Y(3.0 - 2.5 * i / 60.0)) for i in range(61)]
    ap = [(X(1 + 9 * i / 60.0), Y(3.3 - 2.5 * i / 60.0)) for i in range(61)]
    bp = [(X(1 + 9 * i / 60.0), Y(5.3 - 3.9 * i / 60.0)) for i in range(61)]
    cp = [(X(1 + 9 * i / 60.0), Y(5.7 - 3.9 * i / 60.0)) for i in range(61)]
    o.append(_poly(minp, sw=1.6, color="#999", dash="4 3"))
    o.append(_poly(bp, sw=2.0, color="#b06b3a"))
    o.append(_poly(cp, sw=2.0, color=RED))
    o.append(_poly(ap, sw=2.2, color=BLUE))
    o.append(T(X(3.2), Y(2.25) - 8, "Minimum Variability", 7.6, color="#777"))
    o.append(T(X(6.0), Y(1.7) - 10, "Valve A", 7.8, color=BLUE))
    o.append(T(X(6.6), Y(2.3) - 10, "Valve B", 7.8, color="#b06b3a"))
    o.append(T(X(7.2), Y(2.9) - 10, "Valve C", 7.8, color=RED))
    o.append(T(x0 + 10, y0 + H - 16, "Faster Tuning", 7.6, color=GREY, anchor="start"))
    o.append(T(x0 + W - 8, y0 + H - 16, "Slower Tuning", 7.6, color=GREY, anchor="end"))
    o.append(T(320, 362,
               "Hình 2.7 (tr. 49) · Tóm tắt nhiễu tải ngẫu nhiên vòng kín: biến thiên theo hằng số thời gian vòng kín",
               7.6, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Figure 2.7 - Closed-loop random load disturbance summary"))
    return _fig(s,
                "Hình 2.7 (tr. 49) · Tóm tắt nhiễu tải ngẫu nhiên vòng kín: biến thiên (phần trăm "
                "của điểm đặt) được vẽ theo hằng số thời gian vòng kín. Đường Manual là mức "
                "biến thiên khi không điều khiển; đường Minimum Variability là hiệu năng của "
                "van lý tưởng. Van A bám sát đường lý tưởng, trong khi van B và C làm biến "
                "thiên tăng khi chỉnh nhanh hơn.",
                "Figure 2.7 (p. 49) · Closed-loop random load disturbance summary: variability "
                "(percent of set point) is plotted against closed-loop time constant. The Manual "
                "line is the variability with no control, and the Minimum Variability line is "
                "the performance of an ideal valve. Valve A tracks the ideal line while Valves "
                "B and C show rising variability with faster tuning.",
                "Đồ thị biến thiên theo hằng số thời gian vòng kín có đường Manual và ba đường van",
                "Variability versus closed-loop time constant chart with a Manual line and three valve curves")


@_reg
def fig_f28():
    """Figure 2.8 (p. 50) - Effect of Valve Style on Control Range."""
    w, h = 620, 340
    o = [_defs()]
    o.append(T(310, 20, "Installed gain within the 0.5 - 2.0 specification limits",
               8.4))
    x0, W = 152, 380
    rows = [("Globe", 82, "#cddce8"), ("V-notch ball", 62, "#d8e6d2"),
            ("Eccentric plug", 50, "#e6d4c2"), ("Butterfly", 25, "#eadbd5")]
    for i, (lab, v, fill) in enumerate(rows):
        y = 52 + i * 56
        o.append(T(x0 - 10, y + 19, lab, 8.6, color=INK, anchor="end"))
        o.append(_rect(x0, y, W * v / 100.0, 30, fill=fill, sw=1.0))
        o.append(T(x0 + W * v / 100.0 + 8, y + 19, "%d%% of travel" % v,
                   8.0, color=INK, anchor="start"))
    o.append(_line(x0, 268, x0 + W, 268, sw=0.9, color="#c8ced6"))
    o.append(T(x0 + W / 2, 286, "Relative control range (wider is better)", 8.2))
    o.append(T(310, 318,
               "Hình 2.8 (tr. 50) · Ảnh hưởng của kiểu van tới dải điều khiển: van cầu rộng nhất, van bướm hẹp nhất",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.8 - Effect of valve style on control range"))
    return _fig(s,
                "Hình 2.8 (tr. 50) · Ảnh hưởng của kiểu van tới dải điều khiển, biểu diễn bằng "
                "thanh so sánh: van cầu có dải điều khiển rộng nhất; van bi rãnh V và van nút "
                "lệch tâm nằm trung gian; van bướm hẹp nhất và thường chỉ phù hợp cho ứng "
                "dụng tải cố định.",
                "Figure 2.8 (p. 50) · Effect of valve style on control range, shown as comparison "
                "bars: the globe valve has the widest control range; V-notch ball and eccentric "
                "plug valves fall in between; the butterfly valve has the narrowest range and "
                "is generally best suited to fixed-load applications.",
                "Biểu đồ thanh so sánh dải điều khiển của van cầu, van bi, van nút lệch tâm và van bướm",
                "Bar chart comparing control ranges of globe, V-notch ball, eccentric plug and butterfly valves")


@_reg
def fig_f29():
    """Figure 2.9 (p. 51) - Data Comparision [sic]."""
    w, h = 620, 380
    o = [_defs()]
    x0, y0, W, H = 56, 40, 262, 196
    for g in range(1, 4):
        o.append(_line(x0, y0 + H * g / 4.0, x0 + W, y0 + H * g / 4.0,
                       sw=0.6, color="#d8dde3"))
    o.append(_arrow(x0, y0 + H, x0 + W + 14, y0 + H, sw=1.1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.1))
    o.append(T(x0 + 6, y0 + 12, "Valve Signature (%)", 7.4,
               color=INK, anchor="start"))
    base = []
    curr = []
    for t in range(101):
        p = t / 100.0
        s = 100.0 / (1 + math.exp(-(t - 48) / 10.0))
        base.append((x0 + W * p, y0 + H - H * s / 100.0))
        sc = s + 7 * math.sin(t / 9.0) * math.exp(-((t - 50) / 34.0) ** 2)
        curr.append((x0 + W * p, y0 + H - H * max(0, min(100, sc)) / 100.0))
    o.append(_poly(base, sw=2.0, color=BLUE))
    o.append(_poly(curr, sw=1.8, color=RED, dash="5 3"))
    o.append(T(x0 + 8, y0 + H - 14, "Baseline: as shipped", 7.4,
               color=BLUE, anchor="start"))
    o.append(T(x0 + 8, y0 + H - 26, "Current: in service", 7.4,
               color=RED, anchor="start"))
    o.append(T(x0 + W / 2, y0 + H + 16, "Input Signal (%)", 7.8))
    tx, ty, tw = 356, 42, 240
    o.append(_rect(tx, ty, tw, 198, fill="#fbfcfd", sw=1.0))
    cw = [104, 68, 68]
    heads = ["Parameter", "Shipped", "Current"]
    xx = tx
    for cwv, hd in zip(cw, heads):
        o.append(_rect(xx, ty, cwv, 26, fill="#e9edf2", sw=0.8))
        o.append(T(xx + cwv / 2, ty + 17, hd, 7.6, weight="600"))
        xx += cwv
    tab = [("Deadband", "0.25%", "1.80%"), ("T63 (s)", "0.34", "0.91"),
           ("Travel range", "0-100%", "0-100%"), ("Signature", "Pass", "Deviation")]
    for r, row in enumerate(tab):
        xx = tx
        yy = ty + 26 + r * 43
        for ci, (cwv, cell) in enumerate(zip(cw, row)):
            o.append(_rect(xx, yy, cwv, 43, fill="#ffffff" if r % 2 == 0 else "#f5f7fa",
                           sw=0.8))
            o.append(T(xx + cwv / 2, yy + 26, cell, 7.6,
                       color=RED if (ci == 2 and r in (0, 1, 3)) else INK))
            xx += cwv
    o.append(T(310, 360,
               "Hình 2.9 (tr. 51) · So sánh dữ liệu: đường chuẩn lúc xuất xưởng và dữ liệu hiện tại",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.9 - Data Comparision"))
    return _fig(s,
                "Hình 2.9 (tr. 51) · So sánh dữ liệu (nguyên bản viết là Data Comparision): sau "
                "khi đưa van vào vận hành, ValveLink chạy lại các phép thử như lúc xuất xưởng "
                "và đối chiếu dữ liệu hiện tại với dữ liệu chuẩn để nhanh chóng xác định vấn đề.",
                "Figure 2.9 (p. 51) · Data comparison (the source caption reads Data Comparision): "
                "after the valve is in service, ValveLink reruns the factory tests and compares "
                "current data with the as-shipped baseline to pinpoint issues quickly.",
                "Đồ thị đường chữ ký van so sánh đường chuẩn và dữ liệu hiện tại kèm bảng thông số",
                "Valve signature plot comparing the as-shipped baseline with current data and a parameter table")


@_reg
def fig_f2_10():
    """Figure 2.10 (p. 51) - ValveLink Software."""
    w, h = 660, 420
    o = [_defs()]
    o.append(_rect(30, 20, 600, 360, fill="#f7f8fa", sw=1.2))
    o.append(_rect(30, 20, 600, 28, fill="#dce6f0", sw=1.0))
    o.append(T(42, 38, "ValveLink Software - Performance Diagnostics", 8.6,
               color=INK, anchor="start"))
    o.append(T(604, 38, "_   []   X", 8.0, color=INK, anchor="end"))
    o.append(T(42, 66, "File   Edit   View   Diagnostics   Help", 7.6,
               color=GREY, anchor="start"))
    cx, cy, cW, cH = 48, 80, 330, 190
    o.append(_rect(cx, cy, cW, cH, fill="#ffffff", sw=0.9))
    for i in range(1, 4):
        o.append(_line(cx, cy + cH * i / 4.0, cx + cW, cy + cH * i / 4.0,
                       sw=0.6, color="#e2e6ea"))
    o.append(T(cx + 8, cy + 16, "Trend: travel and drive signal", 7.6,
               color=GREY, anchor="start"))
    tr1 = [(cx + 12 + 300 * i / 80.0,
            cy + 30 + 120 * (1 - (i / 80.0 + 0.06 * math.sin(i / 5.0))))
           for i in range(81)]
    tr2 = [(cx + 12 + 300 * i / 80.0,
            cy + 30 + 120 * (1 - (0.85 * i / 80.0 + 0.04 * math.cos(i / 6.0))))
           for i in range(81)]
    o.append(_poly(tr1, sw=1.7, color=BLUE))
    o.append(_poly(tr2, sw=1.7, color=RED, dash="4 3"))
    px, py, pw, ph = 396, 80, 216, 190
    o.append(_rect(px, py, pw, ph, fill="#ffffff", sw=0.9))
    o.append(T(px + 8, py + 18, "Diagnostic Summary", 8.2,
               color=INK, anchor="start", weight="600"))
    lines = ["Status        OK", "Deadband      0.25%", "T63           0.34 s",
             "Travel        50%", "Seat load     Nominal", "Signature     Pass"]
    for i, ln in enumerate(lines):
        o.append(T(px + 10, py + 42 + i * 24, ln, 7.8,
                   color=INK if i != 5 else GREEN, anchor="start"))
    for bx, lab in ((50, "Run Signature Test"), (250, "Compare Data"),
                    (440, "Export Report")):
        o.append(_rect(bx, 296, 170, 30, fill="#e9edf2", sw=1.0))
        o.append(T(bx + 85, 315, lab, 7.8))
    o.append(T(330, 402,
               "Hình 2.10 (tr. 51) · Phần mềm ValveLink: xu hướng và chẩn đoán hiệu năng van",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 2.10 - ValveLink software"))
    return _fig(s,
                "Hình 2.10 (tr. 51) · Phần mềm ValveLink: bảng điều khiển đơn giản với biểu đồ "
                "xu hướng hành trình và tín hiệu lái cùng khu vực chẩn đoán liệt kê trạng thái, "
                "vùng chết, T63, hành trình, tải chỗ ngồi và kết quả đường chữ ký.",
                "Figure 2.10 (p. 51) · ValveLink software: a simplified panel with trend charts "
                "for travel and drive signal, plus a diagnostics area listing status, deadband, "
                "T63, travel, seat load and signature results.",
                "Giao diện phần mềm ValveLink gồm biểu đồ xu hướng và bảng chẩn đoán",
                "Simplified ValveLink software interface with trend charts and a diagnostics panel")
