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
                  _arrow, _axes, _circle, _curve, _defs, _ellipse, _fig, _hatch,
                  _line, _path, _poly, _rect, _txt, svg)

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
    o.append(T(x0 + 8, y0 + 32, "Baseline: as shipped", 7.4,
               color=BLUE, anchor="start"))
    o.append(T(x0 + 8, y0 + 46, "Current: in service", 7.4,
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

# ---------------------------------------------------------------------------
# Chapter 3 figures (3.1-3.52).  Each redraws a source figure as a simplified
# vector schematic and returns the standard 5-tuple via _fig().
# ---------------------------------------------------------------------------

def _finish(w, h, o, title, cap_short, cap_vi, cap_en, aria_vi, aria_en):
    """Append the in-SVG caption line and wrap the figure as a 5-tuple."""
    o.append(T(w / 2.0, h - 10, cap_short, 7.4, color=GREY))
    return _fig(svg(w, h, "".join(o), esc(title)), cap_vi, cap_en, aria_vi, aria_en)


def _leader(x1, y1, x2, y2):
    return _line(x1, y1, x2, y2, sw=0.7, color=GREY)


def _labels(items, x, y, lh=24):
    """Bilingual label column with a small dot marker."""
    o = []
    for i, (vi, en) in enumerate(items):
        yy = y + i * lh
        o.append(_circle(x, yy - 2.5, 1.8, fill=BLUE, sw=0))
        o.append(T(x + 9, yy, vi + " / " + en, 7.5, anchor="start"))
    return "".join(o)


@_reg
def fig_f31():
    """Figure 3.1 (p. 55) - Flanged Angle-Style Control Valve Body."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(150, 120, 170, 84, fill="#f4f7fb", sw=1.6))
    o.append(_rect(76, 138, 76, 48, fill="#e9eef4", sw=1.4))
    o.append(_rect(62, 128, 18, 68, fill="#dfe7ef", sw=1.3))
    o.append(_rect(286, 204, 56, 76, fill="#e9eef4", sw=1.4))
    o.append(_rect(276, 274, 76, 18, fill="#dfe7ef", sw=1.3))
    o.append(_rect(198, 76, 52, 44, fill="#e9eef4", sw=1.3))
    o.append(_line(224, 44, 224, 172, sw=2.4, color=INK))
    o.append(_rect(206, 148, 36, 28, fill="#fdf3e6", sw=1.3))
    o.append(_rect(204, 176, 40, 9, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(96, 162, 154, 162, sw=1.8, color=GREEN))
    o.append(_arrow(314, 214, 314, 268, sw=1.8, color=GREEN))
    for yy, tx, ty in ((92, 250, 92), (120, 258, 120), (152, 248, 160),
                       (180, 246, 180), (208, 322, 214)):
        o.append(_leader(tx, ty, 384, yy))
    o.append(_labels([("Thân van", "Body"), ("Nắp van", "Bonnet"),
                      ("Thân", "Stem"), ("Lồng", "Cage"),
                      ("Vòng chỗ ngồi", "Seat ring")], 396, 92))
    return _finish(w, h, o, "Figure 3.1 - Flanged angle-style control valve body",
                   "Hình 3.1 (tr. 55) · Thân van điều khiển kiểu góc có bích",
                   "Hình 3.1 (tr. 55) · Thân van điều khiển kiểu góc có bích: cổng vào nằm ngang, "
                   "cổng ra thẳng đứng, thân van kiểu lồng; thường dùng cho nước cấp lò hơi và "
                   "thoát nước gia nhiệt, nơi van cũng đóng vai trò như một khúc khuỷu.",
                   "Figure 3.1 (p. 55) · Flanged angle-style control valve body: horizontal inlet "
                   "and vertical outlet with cage-style construction; common in boiler feedwater "
                   "and heater drain service where space is limited and the valve also serves as "
                   "an elbow.",
                   "Thân van góc có bích: cổng vào ngang, cổng ra xuống dưới, nút van dẫn hướng bằng lồng",
                   "Flanged angle valve body with horizontal inlet, downward outlet and cage-guided plug")


@_reg
def fig_f32():
    """Figure 3.2 (p. 56) - Bar Stock Valve Body."""
    w, h = 600, 320
    o = [_defs()]
    o.append(_rect(140, 110, 250, 100, fill="#f4f7fb", sw=1.7))
    o.append(_hatch(144, 114, 242, 92))
    o.append(_rect(96, 138, 46, 44, fill="#e9eef4", sw=1.3))
    o.append(_rect(84, 130, 14, 60, fill="#dfe7ef", sw=1.2))
    o.append(_rect(388, 138, 46, 44, fill="#e9eef4", sw=1.3))
    o.append(_rect(432, 130, 14, 60, fill="#dfe7ef", sw=1.2))
    o.append(_rect(236, 64, 58, 46, fill="#e9eef4", sw=1.3))
    o.append(_line(265, 34, 265, 168, sw=2.4, color=INK))
    o.append(_rect(246, 150, 38, 26, fill="#fdf3e6", sw=1.3))
    o.append(_rect(244, 176, 42, 8, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(120, 160, 198, 160, sw=1.8, color=GREEN))
    o.append(_arrow(400, 160, 428, 160, sw=1.8, color=GREEN))
    o.append(T(30, 92, "Thanh phôi gia công / Machined bar stock", 7.2,
               color=INK, anchor="start"))
    o.append(T(300, 284, "Thân bằng hợp kim chống ăn mòn / Alloy body for corrosive service",
               7.6, color=GREY))
    return _finish(w, h, o, "Figure 3.2 - Bar stock valve body",
                   "Hình 3.2 (tr. 56) · Thân van chế tạo từ thanh phôi",
                   "Hình 3.2 (tr. 56) · Thân van chế tạo từ thanh phôi: thân đặc được gia công "
                   "lỗ dẫn và bề mặt làm kín, thường chọn cho ứng dụng ăn mòn khi cần hợp kim "
                   "đặc biệt; đôi khi rẻ hơn thân đúc và có thể dùng lót polyme.",
                   "Figure 3.2 (p. 56) · Bar stock valve body: a solid billet machined with a flow "
                   "passage and sealing surfaces, often specified for corrosive service when "
                   "exotic alloys are needed; it can be less expensive than a casting, and a "
                   "polymer liner may also be used.",
                   "Mặt cắt thân van gia công từ thanh phôi đặc với lỗ dẫn và gioăng chỗ ngồi",
                   "Cross-section of a bar stock valve body machined from solid stock")


@_reg
def fig_f33():
    """Figure 3.3 (p. 56) - Single-Ported Globe-Style Valve Body."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(200, 96, 190, 170, fill="#f4f7fb", sw=1.7))
    o.append(_rect(132, 150, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(118, 140, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(388, 150, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(456, 140, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(262, 48, 66, 48, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 20, 295, 196, sw=2.4, color=INK))
    o.append(_rect(276, 180, 38, 30, fill="#fdf3e6", sw=1.3))
    o.append(_rect(272, 210, 46, 10, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(154, 176, 232, 176, sw=1.8, color=GREEN))
    o.append(_arrow(295, 246, 295, 272, sw=1.8, color=GREEN))
    o.append(_arrow(350, 176, 430, 176, sw=1.8, color=GREEN))
    o.append(T(152, 132, "Đầu vào / Inlet", 7.6, color=GREEN))
    o.append(T(430, 132, "Đầu ra / Outlet", 7.6, color=GREEN))
    o.append(T(330, 40, "Dẫn hướng bằng thân / Stem guiding", 7.6,
               color=INK, anchor="start"))
    o.append(T(310, 310, "Dòng chảy thường đi lên qua vòng chỗ ngồi / Flow normally up through the seat ring",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.3 - Single-ported globe-style valve body",
                   "Hình 3.3 (tr. 56) · Thân van cầu một cổng",
                   "Hình 3.3 (tr. 56) · Thân van cầu một cổng: kiểu thân phổ biến nhất, kết cấu "
                   "đơn giản, dẫn hướng nút van bằng thân; dòng chảy thường đi lên qua vòng chỗ "
                   "ngồi, dùng rộng rãi trong điều khiển quá trình cỡ NPS 1-4.",
                   "Figure 3.3 (p. 56) · Single-ported globe-style valve body: the most common and "
                   "simplest body style, with stem-guided plug; flow normally passes upward through "
                   "the seat ring, widely used in process control at NPS 1-4.",
                   "Thân van cầu một cổng với nút van dẫn hướng bằng thân, dòng đi lên qua chỗ ngồi",
                   "Single-ported globe body with stem-guided plug and upward flow through the seat")


@_reg
def fig_f34():
    """Figure 3.4 (p. 57) - Valve Body with Cage-Style Trim, Balanced."""
    w, h = 620, 380
    o = [_defs()]
    o.append(_rect(196, 90, 198, 178, fill="#f4f7fb", sw=1.7))
    o.append(_rect(128, 146, 70, 54, fill="#e9eef4", sw=1.4))
    o.append(_rect(114, 136, 18, 74, fill="#dfe7ef", sw=1.3))
    o.append(_rect(392, 146, 70, 54, fill="#e9eef4", sw=1.4))
    o.append(_rect(460, 136, 18, 74, fill="#dfe7ef", sw=1.3))
    o.append(_rect(258, 40, 74, 50, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 12, 295, 200, sw=2.4, color=INK))
    # cage: two walls with window openings
    o.append(_rect(252, 118, 18, 120, fill="#dfe7ef", sw=1.2))
    o.append(_rect(320, 118, 18, 120, fill="#dfe7ef", sw=1.2))
    for k in range(4):
        o.append(_rect(252, 136 + k * 24, 18, 10, fill="#ffffff", sw=0.7))
        o.append(_rect(320, 136 + k * 24, 18, 10, fill="#ffffff", sw=0.7))
    o.append(_rect(272, 176, 46, 46, fill="#fdf3e6", sw=1.4))
    o.append(_rect(268, 222, 54, 10, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(160, 172, 246, 172, sw=1.7, color=GREEN))
    o.append(_arrow(344, 200, 344, 250, sw=1.7, color=GREEN))
    o.append(_leader(262, 150, 406, 96))
    o.append(T(414, 100, "Lồng / Cage", 7.5, anchor="start", color=BLUE))
    o.append(_leader(318, 196, 406, 128))
    o.append(T(414, 132, "Nút cân bằng / Balanced plug", 7.5, anchor="start"))
    o.append(T(300, 330, "Áp suất hạ lưu tác động lên cả hai mặt nút / Downstream pressure on both plug faces",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.4 - Valve body with cage-style trim, balanced plug and soft seat",
                   "Hình 3.4 (tr. 57) · Thân van có lồng dẫn, nút cân bằng",
                   "Hình 3.4 (tr. 57) · Thân van có Trim dạng lồng: lồng vừa dẫn hướng nút van, giữ "
                   "vòng chỗ ngồi vừa tạo đặc tính dòng. Ở kiểu cân bằng, áp suất hạ lưu tác động "
                   "lên cả mặt trên và mặt dưới của nút, triệt tiêu phần lớn lực mất cân bằng tĩnh.",
                   "Figure 3.4 (p. 57) · Valve body with cage-style trim and balanced plug: the cage "
                   "guides the plug, retains the seat ring and characterizes flow. In balanced "
                   "designs downstream pressure acts on both plug faces, nullifying most static "
                   "unbalanced force and allowing a smaller actuator.",
                   "Mặt cắt thân van có lồng dẫn với các cửa sổ và nút van cân bằng",
                   "Cutaway of a cage-guided body with windows and a balanced valve plug")


@_reg
def fig_f35():
    """Figure 3.5 (p. 57) - Reverse-Acting Double-Ported Globe-Style Valve Body."""
    w, h = 620, 380
    o = [_defs()]
    o.append(_rect(196, 86, 198, 196, fill="#f4f7fb", sw=1.7))
    o.append(_rect(128, 140, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(114, 130, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(392, 140, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(460, 130, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(258, 36, 74, 50, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 8, 295, 250, sw=2.4, color=INK))
    # two seat rings and a two-faced plug
    o.append(_rect(240, 148, 110, 9, fill="#dfe7ef", sw=1.2))
    o.append(_rect(240, 218, 110, 9, fill="#dfe7ef", sw=1.2))
    o.append(_poly([(272, 154), (318, 154), (326, 216), (264, 216)],
                   fill="#fdf3e6", sw=1.4, close=True))
    o.append(_arrow(160, 166, 236, 166, sw=1.6, color=GREEN))
    o.append(_arrow(354, 166, 430, 166, sw=1.6, color=GREEN))
    o.append(_arrow(160, 234, 236, 234, sw=1.6, color=GREEN))
    o.append(_arrow(354, 234, 430, 234, sw=1.6, color=GREEN))
    o.append(T(300, 300, "Lực động trên hai cổng tự cân bằng / Forces on the two ports tend to balance",
               7.4, color=GREY))
    o.append(T(300, 322, "Lắp được cả hai chiều: đẩy xuống mở hoặc đẩy xuống đóng / Reversible: push-down-to-open or push-down-to-close",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.5 - Reverse-acting double-ported globe-style valve body",
                   "Hình 3.5 (tr. 57) · Thân van cầu hai cổng kiểu đảo chiều",
                   "Hình 3.5 (tr. 57) · Thân van cầu hai cổng kiểu đảo chiều: dòng có xu hướng mở "
                   "một cổng và đóng cổng kia nên lực động trên nút tự cân bằng; thân van thường "
                   "lắp được cả hai chiều, đẩy xuống để mở hoặc để đóng.",
                   "Figure 3.5 (p. 57) · Reverse-acting double-ported globe-style valve body: flow "
                   "tends to open one port and close the other, so the dynamic force on the plug "
                   "tends to balance; the body is often reversible, allowing push-down-to-open or "
                   "push-down-to-close plug action.",
                   "Thân van hai cổng có hai vòng chỗ ngồi và nút van hai mặt tự cân bằng",
                   "Double-ported body with two seat rings and a self-balancing two-faced plug")


@_reg
def fig_f36():
    """Figure 3.6 (p. 58) - Three-Way Globe Valve."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(210, 112, 180, 136, fill="#f4f7fb", sw=1.7))
    o.append(_rect(130, 148, 82, 46, fill="#e9eef4", sw=1.4))
    o.append(_rect(116, 138, 18, 66, fill="#dfe7ef", sw=1.3))
    o.append(_rect(388, 148, 82, 46, fill="#e9eef4", sw=1.4))
    o.append(_rect(468, 138, 18, 66, fill="#dfe7ef", sw=1.3))
    o.append(_rect(262, 246, 74, 56, fill="#e9eef4", sw=1.4))
    o.append(_rect(252, 298, 94, 16, fill="#dfe7ef", sw=1.3))
    o.append(_rect(272, 62, 56, 50, fill="#e9eef4", sw=1.3))
    o.append(_line(300, 32, 300, 196, sw=2.4, color=INK))
    o.append(_rect(280, 176, 40, 58, fill="#fdf3e6", sw=1.4))
    o.append(_arrow(152, 171, 214, 171, sw=1.7, color=GREEN))
    o.append(_arrow(386, 171, 448, 171, sw=1.7, color=GREEN))
    o.append(_arrow(300, 236, 300, 288, sw=1.7, color=GREEN))
    o.append(T(150, 132, "Cổng trái / Left port", 7.4, color=GREEN))
    o.append(T(448, 132, "Cổng phải / Right port", 7.4, color=GREEN))
    o.append(T(300, 330, "Cổng chung dưới / Bottom common port", 7.4, color=GREEN))
    o.append(T(170, 44, "Nút trụ ở vị trí giữa hành trình", 7.0,
               color=INK, anchor="start"))
    o.append(T(170, 56, "Cylindrical plug at mid-travel", 7.0,
               color=INK, anchor="start"))
    return _finish(w, h, o, "Figure 3.6 - Three-way globe valve",
                   "Hình 3.6 (tr. 58) · Van cầu ba chiều",
                   "Hình 3.6 (tr. 58) · Van cầu ba chiều có nút cân bằng, nút trụ ở vị trí giữa "
                   "hành trình: cổng chung dưới thông sang cả cổng trái và cổng phải. Dùng cho "
                   "điều khiển tại vị trí giữa theo kiểu gộp dòng hoặc tách dòng.",
                   "Figure 3.6 (p. 58) · Three-way globe valve with a balanced plug shown at "
                   "mid-travel: the bottom common port is open to both the right-hand and "
                   "left-hand ports. Used for mid-travel throttling of converging or diverging "
                   "fluids.",
                   "Van cầu ba cổng với nút trụ ở vị trí giữa, thông cổng chung sang hai cổng bên",
                   "Three-port globe valve with cylindrical plug at mid-travel")


@_reg
def fig_f37():
    """Figure 3.7 (p. 59) - Shaft Center Line Offset with Disc Center."""
    w, h = 600, 320
    o = [_defs()]
    # disc seen edge-on, shaft passing behind with an offset
    o.append(_ellipse(300, 160, 96, 30, fill="#fdf3e6", sw=1.6))
    o.append(_line(300, 130, 300, 190, sw=1.8, color=BLUE))
    o.append(_circle(300, 160, 6, fill=BLUE, sw=0))
    o.append(_line(150, 160, 452, 160, sw=2.2, color=INK))
    o.append(_circle(300, 160, 5, fill=RED, sw=0))
    o.append(_line(300, 160, 300, 250, sw=0.9, color=GREY, dash="3 3"))
    o.append(_line(336, 160, 336, 250, sw=0.9, color=GREY, dash="3 3"))
    o.append(_arrow(300, 240, 336, 240, sw=1.1, color=RED))
    o.append(T(318, 232, "e", 8.5, color=RED))
    o.append(T(300, 108, "Tâm đĩa / Disc center", 7.6, color=BLUE))
    o.append(T(300, 276, "Trục lệch / Offset shaft center line", 7.6, color=INK))
    o.append(T(300, 300, "Đĩa rời khỏi gioăng sau 15 độ quay / Disc lifts off the seal after 15 degrees",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 3.7 - Shaft center line offset with disc center",
                   "Hình 3.7 (tr. 59) · Đường tâm trục lệch với tâm đĩa",
                   "Hình 3.7 (tr. 59) · Đường tâm trục lệch với tâm đĩa: thiết kế lệch một hay hai "
                   "lần giúp đĩa rời khỏi gioăng ngay sau khi bắt đầu quay, giảm mòn gioăng và "
                   "cho phép mô-men nhỏ hơn với độ kín chặt hơn.",
                   "Figure 3.7 (p. 59) · Shaft center line offset with disc center: single or double "
                   "offset lifts the disc away from the seal just after rotation begins, reducing "
                   "seal wear and allowing lower torque with tighter shutoff.",
                   "Đĩa bướm với trục lệch tâm và khoảng lệch e giữa tâm trục và tâm đĩa",
                   "Butterfly disc with an offset shaft and the eccentricity e between centers")


@_reg
def fig_f38():
    """Figure 3.8 (p. 59) - Segmented V-Notch Ball."""
    w, h = 600, 320
    o = [_defs()]
    o.append(_circle(268, 160, 92, fill="#f4f7fb", sw=1.7))
    o.append(_path("M268,160 L268,68 A92,92 0 0,1 340,90 Z",
                   fill="#e9eef4", sw=1.3))
    o.append(_path("M268,160 L196,128 L268,68 Z", fill="#fdf3e6", sw=1.3))
    o.append(_line(268, 160, 360, 160, sw=2.4, color=INK))
    o.append(_line(268, 160, 268, 68, sw=1.1, color=GREY, dash="3 3"))
    o.append(_arrow(214, 182, 250, 160, sw=1.4, color=GREEN))
    o.append(_circle(268, 160, 5, fill=BLUE, sw=0))
    o.append(_leader(232, 122, 392, 96))
    o.append(T(400, 100, "Rãnh V / V-notch", 7.6, anchor="start", color=BLUE))
    o.append(_leader(330, 96, 392, 132))
    o.append(T(400, 136, "Đoạn cầu / Ball segment", 7.6, anchor="start"))
    o.append(T(300, 288, "Rãnh V tạo đặc tính dòng phần trăm bằng / V-notch gives equal-percentage flow",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.8 - Segmented V-notch ball",
                   "Hình 3.8 (tr. 59) · Quả cầu có rãnh V dạng đoạn",
                   "Hình 3.8 (tr. 59) · Quả cầu đoạn có rãnh V định hình: rãnh V tạo đặc tính "
                   "dòng phần trăm bằng, còn quả cầu luôn tiếp xúc gioăng khi quay nên có tác "
                   "dụng cắt, hạn chế tắc nghẽn với bùn, giấy và chất lỏng có sợi.",
                   "Figure 3.8 (p. 59) · Segmented ball with a contoured V-notch: the notch produces "
                   "an equal-percentage flow characteristic, while the ball stays in contact with "
                   "the seal for a shearing action that minimizes clogging on slurries and fibrous "
                   "fluids.",
                   "Quả cầu đoạn có rãnh V và gioăng tiếp xúc liên tục",
                   "Segmented ball with a contoured V-notch and continuous seal contact")


@_reg
def fig_f39():
    """Figure 3.9 (p. 60) - Butterfly Control Valve."""
    w, h = 620, 340
    o = [_defs()]
    o.append(_rect(120, 110, 360, 120, fill="#f4f7fb", sw=1.7))
    o.append(_rect(96, 96, 26, 148, fill="#dfe7ef", sw=1.3))
    o.append(_rect(478, 96, 26, 148, fill="#dfe7ef", sw=1.3))
    o.append(_ellipse(300, 170, 54, 104, fill="#fdf3e6", sw=1.6))
    o.append(_line(300, 66, 300, 274, sw=2.6, color=INK))
    o.append(_circle(300, 170, 6, fill=BLUE, sw=0))
    o.append(_arrow(150, 130, 240, 130, sw=1.6, color=GREEN))
    o.append(_arrow(360, 210, 450, 210, sw=1.6, color=GREEN))
    o.append(T(150, 96, "Thân van / Body", 7.6, color=INK))
    o.append(T(440, 96, "Gioăng / Seal", 7.6, color=INK))
    o.append(T(300, 300, "Đĩa quay 90 độ để điều tiết / Disc rotates 90 degrees to throttle",
               7.4, color=GREY))
    o.append(T(300, 322, "Đặc tính gần phần trăm bằng / Approximately equal-percentage characteristic",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.9 - Butterfly control valve",
                   "Hình 3.9 (tr. 60) · Van điều khiển bướm",
                   "Hình 3.9 (tr. 60) · Van điều khiển bướm: chiếm ít không gian lắp đặt, tổn thất "
                   "áp suất thấp, đặc tính gần phần trăm bằng; dùng được cho điều tiết hoặc đóng "
                   "mở, với kích cỡ tới NPS 72.",
                   "Figure 3.9 (p. 60) · Butterfly control valve: minimal installation space, low "
                   "pressure loss and an approximately equal-percentage characteristic; suitable "
                   "for throttling or on/off control in sizes through NPS 72.",
                   "Van bướm với đĩa quay giữa hai bích và trục thẳng đứng",
                   "Butterfly valve with a rotating disc between two flanges")


@_reg
def fig_f3_10():
    """Figure 3.10 (p. 60) - Ball Valve Options."""
    w, h = 660, 320
    o = [_defs()]
    specs = [(140, "Cổng đầy / Full port", "fit"),
             (330, "Rãnh V / V-notch", "vnotch"),
             (520, "Giảm chấn / Anti-cavitation", "cav")]
    for cx, lab, kind in specs:
        o.append(_rect(cx - 78, 108, 156, 104, fill="#f4f7fb", sw=1.5))
        o.append(_rect(cx - 96, 134, 20, 52, fill="#dfe7ef", sw=1.2))
        o.append(_rect(cx + 76, 134, 20, 52, fill="#dfe7ef", sw=1.2))
        o.append(_circle(cx, 160, 42, fill="#e9eef4", sw=1.4))
        if kind == "fit":
            o.append(_circle(cx, 160, 24, fill="#ffffff", sw=1.1))
        elif kind == "vnotch":
            o.append(_path("M%x,%d L%x,%d L%x,%d Z" % (cx - 22, 160, cx - 22, 138, cx + 6, 138),
                           fill="#ffffff", sw=1.0))
            o.append(_circle(cx, 160, 24, fill="#ffffff", sw=1.1))
        else:
            for k in range(3):
                o.append(_circle(cx - 20 + k * 20, 160, 6, fill="#ffffff", sw=0.9))
        o.append(_arrow(cx - 92, 160, cx - 52, 160, sw=1.5, color=GREEN))
        o.append(T(cx, 248, lab, 7.8, color=INK))
    o.append(T(330, 292, "Tùy chọn van bi để giảm tiếng ồn và chống xói mòn / Ball valve options for noise and cavitation",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.10 - Ball valve options",
                   "Hình 3.10 (tr. 60) · Các tùy chọn van bi",
                   "Hình 3.10 (tr. 60) · Các tùy chọn van bi: cổng đầy, rãnh V và cấu hình chống "
                   "xói mòn, giảm tiếng ồn; Emerson cung cấp các tùy chọn này cho mức tiếng ồn và "
                   "xói mòn trung bình.",
                   "Figure 3.10 (p. 60) · Ball valve options: full port, V-notch and anti-cavitation "
                   "configurations; Emerson offers such options for moderate noise and cavitation "
                   "protection.",
                   "Ba cấu hình van bi: cổng đầy, rãnh V và giảm xói mòn",
                   "Three ball valve configurations: full port, V-notch and anti-cavitation")


@_reg
def fig_f3_11():
    """Figure 3.11 (p. 61) - High-Performance Butterfly Control Valve."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(130, 108, 340, 124, fill="#f4f7fb", sw=1.7))
    o.append(_rect(106, 92, 26, 156, fill="#dfe7ef", sw=1.3))
    o.append(_rect(468, 92, 26, 156, fill="#dfe7ef", sw=1.3))
    o.append(_ellipse(300, 170, 60, 100, fill="#fdf3e6", sw=1.6))
    o.append(_line(300, 66, 300, 274, sw=2.6, color=INK))
    o.append(_circle(300, 170, 6, fill=BLUE, sw=0))
    o.append(_path("M300,66 A104,104 0 0,1 392,140", fill="none", sw=1.1,
                   color=RED, dash="4 3"))
    o.append(_arrow(392, 140, 300, 170, sw=1.1, color=RED, dash="4 3"))
    o.append(T(404, 96, "90 độ / 90 degrees", 7.4, color=RED, anchor="start"))
    o.append(_arrow(150, 132, 236, 132, sw=1.6, color=GREEN))
    o.append(_arrow(364, 208, 450, 208, sw=1.6, color=GREEN))
    o.append(T(300, 306, "Lắp lệch đôi giúp đĩa rời gioăng sau khi bắt đầu mở / Double offset lifts the disc off the seal",
               7.4, color=GREY))
    o.append(T(300, 328, "Đặc tính dòng tuyến tính / Linear flow characteristic through 90 degrees",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.11 - High-performance butterfly control valve",
                   "Hình 3.11 (tr. 61) · Van bướm điều khiển hiệu năng cao",
                   "Hình 3.11 (tr. 61) · Van bướm điều khiển hiệu năng cao: cho đặc tính dòng "
                   "tuyến tính qua 90 độ quay đĩa; lắp lệch đôi kéo đĩa ra khỏi gioăng sau khi bắt "
                   "đầu mở, giảm mòn và cho phép điều tiết hiệu quả.",
                   "Figure 3.11 (p. 61) · High-performance butterfly control valve: linear flow "
                   "characteristic through 90 degrees of disc rotation; double-offset mounting "
                   "pulls the disc away from the seal after it begins to open, minimizing wear.",
                   "Van bướm hiệu năng cao với đĩa lệch đôi và cung quay 90 độ",
                   "High-performance butterfly valve with double-offset disc and a 90-degree arc")


@_reg
def fig_f3_12():
    """Figure 3.12 (p. 61) - Pressure Assisted Seal Configuration."""
    w, h = 600, 320
    o = [_defs()]
    o.append(_rect(150, 96, 300, 136, fill="#f4f7fb", sw=1.6))
    o.append(_rect(196, 96, 26, 136, fill="#dfe7ef", sw=1.2))
    o.append(_rect(378, 96, 26, 136, fill="#dfe7ef", sw=1.2))
    o.append(_ellipse(300, 164, 72, 44, fill="#fdf3e6", sw=1.5))
    o.append(_circle(300, 164, 7, fill=BLUE, sw=0))
    o.append(_arrow(300, 60, 300, 118, sw=2.0, color=RED))
    o.append(_arrow(172, 164, 200, 164, sw=1.7, color=GREEN))
    o.append(_arrow(400, 164, 428, 164, sw=1.7, color=GREEN))
    o.append(_leader(344, 140, 440, 88))
    o.append(T(448, 92, "Vòng làm kín / Seal ring", 7.5, anchor="start", color=BLUE))
    o.append(T(300, 280, "Áp suất quá trình ép vòng làm kín vào chỗ ngồi / Process pressure assists the seal",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.12 - Pressure assisted seal configuration",
                   "Hình 3.12 (tr. 61) · Cấu hình làm kín hỗ trợ bằng áp suất",
                   "Hình 3.12 (tr. 61) · Cấu hình làm kín hỗ trợ bằng áp suất: áp suất quá trình "
                   "được dùng để ép vòng làm kín vào chỗ ngồi, cho độ kín chặt đặc biệt ở cả hai "
                   "chiều dòng, đặc biệt với nút lệch tâm và chất lỏng khó xử lý.",
                   "Figure 3.12 (p. 61) · Pressure assisted seal configuration: process pressure is "
                   "used to push the seal ring into its seat, giving exceptional tight shutoff in "
                   "both flow directions, especially with eccentric-plug designs on difficult fluids.",
                   "Vòng làm kín được áp suất ép vào chỗ ngồi, dòng qua hai phía",
                   "Seal ring pressed into its seat by process pressure")


@_reg
def fig_f3_13():
    """Figure 3.13 (p. 62) - Eccentric Plug Control Valve Body."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(180, 110, 240, 130, fill="#f4f7fb", sw=1.7))
    o.append(_rect(120, 148, 62, 48, fill="#e9eef4", sw=1.3))
    o.append(_rect(106, 138, 18, 68, fill="#dfe7ef", sw=1.2))
    o.append(_rect(418, 148, 62, 48, fill="#e9eef4", sw=1.3))
    o.append(_rect(478, 138, 18, 68, fill="#dfe7ef", sw=1.2))
    o.append(_rect(258, 58, 74, 52, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 28, 295, 200, sw=2.4, color=INK))
    o.append(_ellipse(292, 196, 58, 40, fill="#fdf3e6", sw=1.5))
    o.append(_circle(268, 196, 6, fill=BLUE, sw=0))
    o.append(_rect(322, 178, 12, 42, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(152, 172, 226, 172, sw=1.7, color=GREEN))
    o.append(_arrow(366, 172, 442, 172, sw=1.7, color=GREEN))
    o.append(_leader(280, 196, 412, 96))
    o.append(T(420, 100, "Nút lệch tâm / Eccentric plug", 7.5, anchor="start"))
    o.append(T(300, 300, "Đường đi của nút giảm tiếp xúc với vòng chỗ ngồi khi mở / Plug path minimizes seat contact",
               7.4, color=GREY))
    o.append(T(300, 322, "Chịu mòn, chịu nhiệt tới 427 độ C / Erosion resistant, to 427 deg C",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.13 - Eccentric plug control valve body",
                   "Hình 3.13 (tr. 62) · Thân van điều khiển nút lệch tâm",
                   "Hình 3.13 (tr. 62) · Thân van điều khiển nút lệch tâm: đường đi của đĩa lệch "
                   "giảm tiếp xúc với vòng chỗ ngồi khi mở, giảm mòn và ma sát; thân và Trim chịu "
                   "nhiệt tới 427 độ C và chênh áp đóng tới 1500 psi, hợp cho bùn và chất coking.",
                   "Figure 3.13 (p. 62) · Eccentric plug control valve body: the plug path minimizes "
                   "contact with the seat ring when opening, reducing wear and friction; the rugged "
                   "body and trim handle 427 deg C and 1500 psi shutoff on slurries and coking fluids.",
                   "Thân van nút lệch tâm với vòng chỗ ngồi tự định tâm",
                   "Eccentric plug valve body with a self-centering seat ring")


@_reg
def fig_f3_14():
    """Figure 3.14 (p. 62) - Full-Port Ball Control Valve."""
    w, h = 620, 340
    o = [_defs()]
    o.append(_rect(120, 110, 360, 110, fill="#f4f7fb", sw=1.7))
    o.append(_rect(96, 96, 26, 138, fill="#dfe7ef", sw=1.3))
    o.append(_rect(478, 96, 26, 138, fill="#dfe7ef", sw=1.3))
    o.append(_circle(300, 165, 58, fill="#e9eef4", sw=1.5))
    o.append(_circle(300, 165, 40, fill="#ffffff", sw=1.2))
    o.append(_line(300, 107, 300, 60, sw=2.4, color=INK))
    o.append(_arrow(150, 165, 236, 165, sw=1.8, color=GREEN))
    o.append(_arrow(364, 165, 450, 165, sw=1.8, color=GREEN))
    o.append(T(300, 272, "Đường kính lỗ bằng đường kính ống / Bore equals pipe diameter", 7.6, color=BLUE))
    o.append(T(300, 296, "Ít hoặc không hạn chế dòng, cho phép thông tẩy / Little restriction; allows pigging",
               7.4, color=GREY))
    o.append(T(300, 318, "Thử lửa theo API 6 và 6FA / Fire tested to API 6 and 6FA", 7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.14 - Full-Port Ball Control Valve",
                   "Hình 3.14 (tr. 62) · Van bi điều khiển cổng đầy",
                   "Hình 3.14 (tr. 62) · Van bi điều khiển cổng đầy: lỗ trong bằng đường kính "
                   "ống nên gần như không hạn chế dòng và cho phép thông tẩy; thiết kế ba mảnh, "
                   "gắn trục chốt, đã thử lửa theo API 6 và 6FA.",
                   "Figure 3.14 (p. 62) · Full-port ball control valve: the bore matches the pipe "
                   "diameter, presenting little or no flow restriction and allowing pigging; a "
                   "three-piece trunnion-mounted design, fire tested to API 6 and 6FA.",
                   "Van bi cổng đầy với lỗ dẫn bằng đường kính ống",
                   "Full-port ball valve with a bore equal to the pipe diameter")


@_reg
def fig_f3_15():
    """Figure 3.15 (p. 62) - Full-Port Ball Valve."""
    w, h = 620, 340
    o = [_defs()]
    o.append(_rect(120, 108, 360, 114, fill="#f4f7fb", sw=1.7))
    o.append(_rect(96, 94, 26, 142, fill="#dfe7ef", sw=1.3))
    o.append(_rect(478, 94, 26, 142, fill="#dfe7ef", sw=1.3))
    o.append(_circle(300, 166, 58, fill="#e9eef4", sw=1.5))
    o.append(_circle(300, 166, 40, fill="#ffffff", sw=1.2))
    o.append(_line(300, 108, 300, 58, sw=2.4, color=INK))
    o.append(_line(198, 108, 198, 222, sw=1.1, color=GREY, dash="3 3"))
    o.append(_line(402, 108, 402, 222, sw=1.1, color=GREY, dash="3 3"))
    o.append(T(198, 246, "Mảnh 1", 7.4, color=GREY))
    o.append(T(300, 246, "Mảnh 2 / thân giữa", 7.4, color=GREY))
    o.append(T(402, 246, "Mảnh 3", 7.4, color=GREY))
    o.append(_arrow(150, 166, 236, 166, sw=1.7, color=GREEN))
    o.append(_arrow(364, 166, 450, 166, sw=1.7, color=GREEN))
    o.append(T(300, 288, "Ba mảnh, gắn trục chốt / Three-piece trunnion-mounted construction", 7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.15 - Full-Port Ball Valve",
                   "Hình 3.15 (tr. 62) · Van bi cổng đầy ba mảnh",
                   "Hình 3.15 (tr. 62) · Van bi cổng đầy dạng ba mảnh, gắn trục chốt: thân giữa "
                   "chứa quả cầu và gioăng, hai đầu nối vào đường ống; thiết kế tối ưu cho điều "
                   "khiển tự động trong bypass, mẻ, giám sát và đóng khẩn cấp.",
                   "Figure 3.15 (p. 62) · Full-port ball valve: a three-piece, trunnion-mounted "
                   "construction with a centre section carrying the ball and seals between the two "
                   "pipe-end pieces, optimized for bypass, batch, monitor and emergency shutoff service.",
                   "Van bi cổng đầy ba mảnh có quả cầu gắn trục chốt",
                   "Three-piece full-port ball valve with a trunnion-mounted ball")


@_reg
def fig_f3_16():
    """Figure 3.16 (p. 63) - Multi-Port Flow Selector Valve."""
    w, h = 560, 400
    o = [_defs()]
    o.append(_circle(280, 186, 84, fill="#f4f7fb", sw=1.7))
    o.append(_circle(280, 186, 26, fill="#fdf3e6", sw=1.4))
    o.append(_circle(280, 186, 6, fill=BLUE, sw=0))
    for i in range(8):
        import math as _m
        a = 2 * _m.pi * i / 8.0
        x1 = 280 + 84 * _m.cos(a)
        y1 = 186 + 84 * _m.sin(a)
        x2 = 280 + 132 * _m.cos(a)
        y2 = 186 + 132 * _m.sin(a)
        o.append(_line(x1, y1, x2, y2, sw=5, color="#dfe7ef"))
        o.append(_line(x1, y1, x2, y2, sw=1.1, color=INK))
        o.append(_arrow(x2 - 16 * _m.cos(a), y2 - 16 * _m.sin(a), x1, y1,
                        sw=1.2, color=GREEN))
    o.append(_line(280, 102, 280, 54, sw=6, color="#dfe7ef"))
    o.append(_arrow(280, 78, 280, 108, sw=1.4, color=RED))
    o.append(T(280, 44, "Đầu ra thử / Test outlet", 7.6, color=RED))
    o.append(_line(280, 270, 280, 322, sw=6, color="#dfe7ef"))
    o.append(_arrow(280, 290, 280, 318, sw=1.4, color=GREEN))
    o.append(T(280, 344, "Đầu ra chung / Common group outlet", 7.6, color=GREEN))
    o.append(T(280, 378, "Tám đầu vào được chọn luân phiên qua rô-to / Eight inlets selected by a rotor",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 3.16 - Multi-port flow selector valve",
                   "Hình 3.16 (tr. 63) · Van chọn dòng đa cổng",
                   "Hình 3.16 (tr. 63) · Van chọn dòng đa cổng nối với tám đường vào: rô-to cô "
                   "lập, chuyển hướng hoặc thử một đường riêng trong khi bảy đường còn lại vẫn "
                   "chảy tới cổng ra chung. Gồm thân, nắp, nút rô-to và cơ cấu chấp hành.",
                   "Figure 3.16 (p. 63) · Multi-port flow selector valve connected to eight inlet "
                   "lines: a rotor isolates, diverts or tests an individual line while the remaining "
                   "seven continue to a common outlet. It consists of body, bonnet, rotor plug and "
                   "actuator.",
                   "Van đa cổng với tám đường vào, một đầu ra thử và một đầu ra chung",
                   "Multi-port valve with eight inlets, one test outlet and a common outlet")


@_reg
def fig_f3_17():
    """Figure 3.17 (p. 64) - Popular Varieties of Bolted Flange Connections."""
    w, h = 660, 320
    o = [_defs()]
    kinds = [(140, "Bích mặt phẳng / Flat-face"),
             (330, "Bích mặt nổi / Raised-face"),
             (520, "Mối nối kiểu vòng / Ring-type joint")]
    for cx, lab in kinds:
        o.append(_rect(cx - 90, 122, 72, 76, fill="#e9eef4", sw=1.4))
        o.append(_rect(cx + 18, 122, 72, 76, fill="#e9eef4", sw=1.4))
        o.append(_rect(cx - 18, 140, 36, 40, fill="#f4f7fb", sw=1.2))
        o.append(_line(cx - 96, 160, cx + 96, 160, sw=1.0, color=GREY, dash="3 3"))
    # flat face: gasket over whole face
    o.append(_rect(50, 160, 180, 8, fill="#fdf3e6", sw=0.8))
    # raised face
    o.append(_rect(240, 152, 180, 8, fill="#fdf3e6", sw=0.8))
    o.append(_rect(276, 144, 108, 8, fill="#dfe7ef", sw=0.9))
    # RTJ: groove with ring
    o.append(_rect(430, 152, 180, 8, fill="#fdf3e6", sw=0.8))
    o.append(_ellipse(520, 160, 24, 12, fill="#fdf3e6", sw=1.2))
    for cx in (140, 330, 520):
        o.append(_circle(cx - 60, 112, 5, fill=BLUE, sw=0))
        o.append(_circle(cx + 60, 112, 5, fill=BLUE, sw=0))
    for cx, lab in kinds:
        o.append(T(cx, 250, lab, 7.8, color=INK))
    o.append(T(330, 292, "Ba loại bích bắt bulông thông dụng / Three popular bolted-flange varieties",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.17 - Popular varieties of bolted flange connections",
                   "Hình 3.17 (tr. 64) · Các loại nối bích bắt bulông thông dụng",
                   "Hình 3.17 (tr. 64) · Các loại nối bích bắt bulông thông dụng: mặt phẳng, mặt "
                   "nổi và mối nối kiểu vòng. Mặt phẳng ép toàn bộ bề mặt qua gioăng; mặt nổi có "
                   "vòng nổi và rãnh đồng tâm; kiểu vòng dùng gioăng kim loại dạng vòng trong rãnh "
                   "chữ U, dùng được đến 15.000 psig.",
                   "Figure 3.17 (p. 64) · Popular bolted-flange connections: flat-face, raised-face "
                   "and ring-type joint. Flat-face clamps the gasket over the full face; raised-face "
                   "has concentric grooves; the ring-type joint wedges a metal ring into a U-groove "
                   "and is used up to 15,000 psig.",
                   "So sánh ba dạng mặt bích: phẳng, nổi và rãnh vòng",
                   "Comparison of flat-face, raised-face and ring-type-joint flanges")


@_reg
def fig_f3_18():
    """Figure 3.18 (p. 64) - Common Welded End Connections."""
    w, h = 640, 320
    o = [_defs()]
    # socket weld
    o.append(_rect(110, 104, 180, 96, fill="#f4f7fb", sw=1.6))
    o.append(_rect(110, 128, 44, 48, fill="#dfe7ef", sw=1.2))
    o.append(_rect(154, 140, 56, 24, fill="#ffffff", sw=1.2))
    o.append(_rect(60, 140, 94, 24, fill="#e9eef4", sw=1.2))
    o.append(_poly([(150, 140), (162, 152), (150, 164)], fill="#fdf3e6", sw=1.1, close=True))
    o.append(T(200, 226, "Hàn lổ / Socket weld", 7.8, color=INK))
    # butt weld
    o.append(_rect(370, 104, 180, 96, fill="#f4f7fb", sw=1.6))
    o.append(_rect(300, 140, 70, 24, fill="#e9eef4", sw=1.2))
    o.append(_poly([(366, 134), (378, 152), (366, 170)], fill="#ffffff", sw=1.1, close=True))
    o.append(_poly([(382, 134), (370, 152), (382, 170)], fill="#ffffff", sw=1.1, close=True))
    o.append(_rect(374, 140, 176, 24, fill="#e9eef4", sw=1.2))
    o.append(T(460, 226, "Hàn đối đầu / Butt weld", 7.8, color=INK))
    o.append(T(320, 280, "Đầu hàn kín ở mọi áp suất và nhiệt độ / Welded ends are leak-tight at all pressures",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.18 - Common welded end connections",
                   "Hình 3.18 (tr. 64) · Các kiểu đầu nối hàn thông dụng",
                   "Hình 3.18 (tr. 64) · Các kiểu đầu nối hàn thông dụng: hàn lổ và hàn đối đầu. "
                   "Đầu hàn kín ở mọi áp suất, nhiệt độ và có chi phí ban đầu thấp, nhưng khó tháo "
                   "khỏi đường ống và chỉ dùng cho vật liệu hàn được.",
                   "Figure 3.18 (p. 64) · Common welded end connections: socket weld and butt weld. "
                   "Welded ends are leak-tight at all pressures and temperatures and economical in "
                   "first cost, but are harder to remove and limited to weldable materials.",
                   "Mặt cắt đầu hàn lổ và đầu hàn đối đầu",
                   "Cross-sections of socket-weld and butt-weld end connections")


@_reg
def fig_f3_19():
    """Figure 3.19 (p. 65) - Typical Bonnet, Flange, and Stud Bolts."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(244, 150, 132, 150, fill="#e9eef4", sw=1.6))   # bonnet
    o.append(_rect(228, 138, 164, 16, fill="#dfe7ef", sw=1.3))    # bonnet flange
    o.append(_rect(228, 296, 164, 16, fill="#dfe7ef", sw=1.3))    # body flange
    o.append(_rect(214, 312, 192, 46, fill="#f4f7fb", sw=1.4))    # body top
    o.append(_rect(288, 96, 44, 54, fill="#f7f9fb", sw=1.2))      # packing box
    for i in range(4):
        o.append(_rect(292, 102 + i * 12, 36, 8, fill="#fdf3e6", sw=0.8))
    o.append(_line(310, 44, 310, 250, sw=2.4, color=INK))
    for x in (236, 384):
        o.append(_line(x, 138, x, 316, sw=2.2, color=INK))
        o.append(_rect(x - 9, 128, 18, 10, fill="#dfe7ef", sw=1.1))
        o.append(_rect(x - 9, 312, 18, 10, fill="#dfe7ef", sw=1.1))
    o.append(_leader(392, 108, 452, 88))
    o.append(T(460, 92, "Hộp đệm / Packing box", 7.5, anchor="start"))
    o.append(_leader(390, 146, 452, 132))
    o.append(T(460, 136, "Bích nắp / Bonnet flange", 7.5, anchor="start"))
    o.append(_leader(392, 160, 452, 176))
    o.append(T(460, 180, "Bulông chốt / Stud bolt", 7.5, anchor="start"))
    o.append(_leader(390, 304, 452, 224))
    o.append(T(460, 228, "Gioăng nắp / Bonnet gasket", 7.5, anchor="start"))
    o.append(T(310, 380, "Bulông nắp nén gioăng và giữ nắp vào thân / Stud bolts load the gasket and hold the bonnet",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.19 - Typical bonnet, flange, and stud bolts",
                   "Hình 3.19 (tr. 65) · Nắp, bích và bulông chốt điển hình",
                   "Hình 3.19 (tr. 65) · Nắp, bích và bulông chốt điển hình: nắp có bích liền, "
                   "đặt gioăng giữa bích nắp và bích thân, gioăng nén qua bulông chốt; hộp đệm "
                   "ở trên chứa bộ đệm được giữ bằng bích đệm.",
                   "Figure 3.19 (p. 65) · Typical bonnet, flange and stud bolts: an integral-flange "
                   "bonnet with a gasket between the bonnet and body flanges compressed by studs; "
                   "the packing box above holds the packing set with a packing follower.",
                   "Mặt cắt nắp van có bích liền, bulông chốt và hộp đệm",
                   "Cutaway of an integral-flange bonnet with studs and packing box")


@_reg
def fig_f3_20():
    """Figure 3.20 (p. 66) - Bonnet Variations."""
    w, h = 640, 320
    o = [_defs()]
    kinds = [(140, "Nắp thường / Standard"),
             (320, "Nắp kéo dài / Extension"),
             (500, "Nắp ống mềm / Bellows seal")]
    for cx, lab in kinds:
        o.append(_rect(cx - 60, 116, 120, 132, fill="#f4f7fb", sw=1.5))
        o.append(_rect(cx - 72, 104, 144, 14, fill="#dfe7ef", sw=1.2))
        o.append(_line(cx, 52, cx, 200, sw=2.2, color=INK))
    # standard: short packing
    o.append(_rect(118, 132, 44, 40, fill="#fdf3e6", sw=1.0))
    # extension: tall narrow neck
    o.append(_rect(296, 60, 48, 88, fill="#e9eef4", sw=1.2))
    # bellows: accordion folds
    for i in range(5):
        y = 130 + i * 12
        o.append(_line(476, y, 524, y + 8, sw=1.2, color=BLUE))
        o.append(_line(524, y + 8, 476, y + 16, sw=1.2, color=BLUE))
    for cx, lab in kinds:
        o.append(T(cx, 276, lab, 7.8, color=INK))
    o.append(T(320, 302, "Nắp van có thể thay đổi để phù hợp nhiệt độ, áp suất và yêu cầu kín / Bonnets vary with temperature and sealing duty",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.20 - Bonnet variations",
                   "Hình 3.20 (tr. 66) · Các biến thể nắp van",
                   "Hình 3.20 (tr. 66) · Các biến thể nắp van: nắp thường, nắp kéo dài cho nhiệt độ "
                   "cao hoặc thấp và nắp kín bằng ống mềm khi không được phép rò rỉ. Nắp cùng vật "
                   "liệu thân van vì là chi tiết chịu áp cùng điều kiện nhiệt và ăn mòn.",
                   "Figure 3.20 (p. 66) · Bonnet variations: standard, extension for high or low "
                   "temperature, and bellows seal where no leakage can be tolerated. The bonnet is "
                   "made of the same material as the body because it is a pressure-containing member.",
                   "Ba dạng nắp van: thường, kéo dài và kín bằng ống mềm",
                   "Three bonnet styles: standard, extension and bellows seal")


def _tbl(x, y, widths, headers, rows, rh=22, fs=7.2):
    """A compact bilingual table; returns (markup, bottom_y)."""
    total = sum(widths)
    o = [_rect(x, y, total, rh, fill="#dfe7ef", sw=1.0)]
    xx = x
    for wd, hd in zip(widths, headers):
        o.append(T(xx + wd / 2.0, y + rh / 2.0 + 2.6, hd, fs,
                   color=INK, weight="600"))
        xx += wd
    yy = y + rh
    for i, row in enumerate(rows):
        o.append(_rect(x, yy, total, rh,
                       fill="#ffffff" if i % 2 else "#f7f9fb", sw=0.9))
        xx = x
        for wd, cell in zip(widths, row):
            o.append(T(xx + wd / 2.0, yy + rh / 2.0 + 2.6, str(cell), fs))
            xx += wd
        yy += rh
    return "".join(o), yy


@_reg
def fig_f3_21():
    """Figure 3.21 (p. 66) - Valve Body with Fabricated Extension Bonnet."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(206, 250, 208, 96, fill="#f4f7fb", sw=1.7))    # body
    o.append(_rect(140, 278, 68, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(126, 268, 18, 62, fill="#dfe7ef", sw=1.2))
    o.append(_rect(410, 278, 68, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(476, 268, 18, 62, fill="#dfe7ef", sw=1.2))
    o.append(_rect(268, 100, 84, 150, fill="#eef3fb", sw=1.5))    # extension neck
    for i in range(5):
        o.append(_line(268, 120 + i * 26, 352, 120 + i * 26, sw=0.6, color="#9a9a9a"))
    o.append(_rect(288, 54, 44, 46, fill="#f7f9fb", sw=1.2))      # packing box
    o.append(_line(310, 24, 310, 300, sw=2.4, color=INK))
    o.append(_arrow(164, 298, 232, 298, sw=1.6, color=GREEN))
    o.append(_arrow(388, 298, 454, 298, sw=1.6, color=GREEN))
    o.append(_leader(354, 170, 452, 140))
    o.append(T(444, 138, "Nắp kéo dài chế tạo", 7.2, anchor="start"))
    o.append(T(444, 150, "Fabricated extension bonnet", 7.2, anchor="start"))
    o.append(T(310, 374, "Dời hộp đệm xa nhiệt độ quá trình / Moves packing away from process temperature",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.21 - Valve body with fabricated extension bonnet",
                   "Hình 3.21 (tr. 66) · Thân van có nắp kéo dài chế tạo",
                   "Hình 3.21 (tr. 66) · Thân van có nắp kéo dài chế tạo từ ống: nắp kéo dài đưa "
                   "hộp đệm ra xa nhiệt độ cực đoan của quá trình. Bề mặt nhẵn của ống inox được "
                   "ưu tiên cho dịch vụ lạnh; thành mỏng giúp giảm truyền nhiệt.",
                   "Figure 3.21 (p. 66) · Valve body with a fabricated extension bonnet: the "
                   "extension moves the packing box far enough from extreme process temperature. "
                   "Smooth stainless tubing is preferred for cold service; thin walls reduce heat "
                   "transfer.",
                   "Thân van với nắp kéo dài bằng ống inox và hộp đệm ở xa",
                   "Valve body with a fabricated tubular extension bonnet")


@_reg
def fig_f3_22():
    """Figure 3.22 (p. 67) - ENVIRO-SEAL Bellows Seal Bonnet."""
    w, h = 620, 410
    o = [_defs()]
    o.append(_rect(220, 246, 180, 104, fill="#f4f7fb", sw=1.7))
    o.append(_rect(156, 272, 66, 44, fill="#e9eef4", sw=1.3))
    o.append(_rect(142, 262, 18, 64, fill="#dfe7ef", sw=1.2))
    o.append(_rect(392, 272, 66, 44, fill="#e9eef4", sw=1.3))
    o.append(_rect(456, 262, 18, 64, fill="#dfe7ef", sw=1.2))
    o.append(_rect(268, 66, 84, 180, fill="#eef3fb", sw=1.5))     # bonnet
    o.append(_line(310, 30, 310, 300, sw=2.4, color=INK))
    for i in range(7):
        y = 120 + i * 14
        o.append(_line(272, y, 348, y + 7, sw=1.3, color=BLUE))
        o.append(_line(348, y + 7, 272, y + 14, sw=1.3, color=BLUE))
    o.append(_rect(288, 74, 44, 40, fill="#f7f9fb", sw=1.2))
    o.append(T(366, 170, "Ống mềm / Bellows", 7.6, anchor="start", color=BLUE))
    o.append(T(366, 196, "Đệm dự phòng / Back-up packing", 7.6, anchor="start"))
    o.append(T(310, 386, "Không rò rỉ dọc thân, dùng cho chất độc, dễ bay hơi hoặc phóng xạ",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.22 - ENVIRO-SEAL bellows seal bonnet",
                   "Hình 3.22 (tr. 67) · Nắp kín ống mềm ENVIRO-SEAL",
                   "Hình 3.22 (tr. 67) · Nắp kín bằng ống mềm ENVIRO-SEAL: dùng khi không cho "
                   "phép rò rỉ dọc thân (dưới 1x10-6 cc/giây helium), thường với chất lỏng độc, "
                   "dễ bay hơi, phóng xạ hoặc đắt giá. Bộ đệm dự phòng ngăn hỏng sự cố nếu ống vỡ.",
                   "Figure 3.22 (p. 67) · ENVIRO-SEAL bellows seal bonnet: used when no leakage "
                   "(less than 1x10-6 cc/sec helium) along the stem can be tolerated, often with "
                   "toxic, volatile, radioactive or expensive fluids. Back-up packing prevents "
                   "catastrophic failure if the bellows ruptures.",
                   "Nắp van có ống mềm kín và bộ đệm dự phòng phía trên",
                   "Bellows-sealed bonnet with back-up packing above the bellows")


@_reg
def fig_f3_23():
    """Figure 3.23 (p. 67) - Welded-Leaf and Mechanically-Formed Bellows."""
    w, h = 620, 320
    o = [_defs()]
    # welded leaf: stacked short leaves
    o.append(_rect(110, 104, 180, 130, fill="#f7f9fb", sw=1.3))
    for i in range(6):
        y = 116 + i * 18
        o.append(_rect(132, y, 136, 6, fill="#e9eef4", sw=0.9))
        if i < 5:
            o.append(_line(132, y + 6, 158, y + 18, sw=1.0, color=BLUE))
            o.append(_line(268, y + 6, 242, y + 18, sw=1.0, color=BLUE))
    o.append(T(200, 264, "Ống mềm lá hàn / Welded-leaf", 7.8, color=INK))
    o.append(T(200, 284, "Chiều cao thấp hơn / Shorter package height", 7.2, color=GREY))
    # mechanically formed: deep convolutions
    o.append(_rect(360, 104, 180, 130, fill="#f7f9fb", sw=1.3))
    for i in range(5):
        y = 112 + i * 24
        o.append(_path("M378,%d C396,%d 402,%d 420,%d C438,%d 444,%d 462,%d"
                       % (y, y - 8, y + 8, y, y - 8, y + 8, y),
                       fill="none", sw=1.2, color=BLUE))
    o.append(T(450, 264, "Ống mềm tạo hình cơ khí / Mechanically-formed", 7.8, color=INK))
    o.append(T(450, 284, "Độ tin cậy cao hơn / Higher reliability", 7.2, color=GREY))
    return _finish(w, h, o, "Figure 3.23 - Welded-leaf and mechanically-formed bellows",
                   "Hình 3.23 (tr. 67) · Ống mềm lá hàn và ống mềm tạo hình cơ khí",
                   "Hình 3.23 (tr. 67) · Hai loại ống mềm: lá hàn có chiều cao tổng ngắn hơn nhưng "
                   "tuổi thọ có thể hạn chế do cách chế tạo; loại tạo hình cơ khí cao hơn nhưng "
                   "quy trình chế tạo lặp lại tốt nên độ tin cậy cao hơn.",
                   "Figure 3.23 (p. 67) · Two bellows designs: welded-leaf has a shorter total "
                   "height but service life may be limited by its manufacture; mechanically-formed "
                   "bellows is taller but produced by a more repeatable process and therefore more "
                   "reliable.",
                   "So sánh ống mềm lá hàn và ống mềm tạo hình cơ khí",
                   "Comparison of welded-leaf and mechanically-formed bellows")


@_reg
def fig_f3_24():
    """Figure 3.24 (p. 68) - Packing Material Arrangements for Globe-Style Bodies."""
    w, h = 660, 420
    o = [_defs()]
    o.append(_rect(230, 84, 60, 240, fill="#e9eef4", sw=1.5))     # packing box wall
    o.append(_rect(350, 84, 60, 240, fill="#e9eef4", sw=1.5))
    o.append(_line(320, 56, 320, 356, sw=2.6, color=INK))         # stem
    items = [("Upper wiper", "Gạt trên"), ("Packing follower", "Bích ép"),
             ("Female adapter", "Đầu cái"), ("V-Ring", "Vòng V"),
             ("Male adapter", "Đầu đực"), ("Washer", "Vòng đệm"),
             ("Spring", "Lò xo"), ("Packing box", "Hộp đệm"),
             ("Lower wiper", "Gạt dưới")]
    for i, (en, vi) in enumerate(items):
        yy = 100 + i * 25
        o.append(_rect(294, yy, 52, 12, fill="#fdf3e6", sw=0.9))
        o.append(_num(206, yy + 6, i + 1))
        o.append(T(196, yy + 9, vi + " / " + en, 6.4, anchor="end"))
    o.append(_leader(206, 124, 160, 124))
    o.append(_leader(410, 124, 540, 110))
    o.append(T(548, 110, "Gioăng TFE V-Ring", 7.0, anchor="start"))
    o.append(T(548, 121, "TFE V-Ring packing", 7.0, anchor="start"))
    o.append(_leader(410, 150, 540, 141))
    o.append(T(548, 141, "Lá than chì / Laminated", 7.0, anchor="start"))
    o.append(T(548, 152, "graphite", 7.0, anchor="start"))
    o.append(_leader(410, 176, 540, 172))
    o.append(T(548, 172, "Sợi than chì / Filament", 7.0, anchor="start"))
    o.append(T(548, 183, "graphite", 7.0, anchor="start"))
    o.append(T(330, 392, "Bố trí vật liệu đệm điển hình cho thân van kiểu cầu / Typical packing arrangements",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.24 - Packing material arrangements for globe-style valve bodies",
                   "Hình 3.24 (tr. 68) · Bố trí vật liệu đệm cho thân van kiểu cầu",
                   "Hình 3.24 (tr. 68) · Bố trí vật liệu đệm cho thân van kiểu cầu: gạt trên, bích "
                   "ép đệm, đầu nối cái, vòng V, đầu nối đực, vòng đệm, lò xo, hộp đệm và gạt dưới "
                   "(1-9). Các cấu hình TFE V-Ring đơn, đôi và có cổng xả được mô tả.",
                   "Figure 3.24 (p. 68) · Packing material arrangements for globe-style valve "
                   "bodies: upper wiper, packing follower, female adapter, V-ring, male adapter, "
                   "washer, spring, packing box and lower wiper (1-9), with single, double and "
                   "leak-off TFE V-ring arrangements.",
                   "Mặt cắt hộp đệm với chín chi tiết được đánh số",
                   "Packing box cutaway with nine numbered components")


@_reg
def fig_f3_25():
    """Figure 3.25 (p. 69) - Measurement Frequency for VOC Valves."""
    w, h = 660, 360
    o = [_defs()]
    o.append(T(330, 40, "Tỷ lệ van rò ở 500 ppm / Leaking valves at 500 ppm",
               9.0, weight="600"))
    steps = [("< 0.5%", "Hàng năm / Annual", GREEN),
             ("0.5% - 1%", "Nửa năm / Semi-annual", "#6a9e3f"),
             ("1% - 2%", "Hàng quý / Quarterly", "#b8860b"),
             ("> 2%", "Hàng tháng / Monthly", RED)]
    for i, (thr, freq, col) in enumerate(steps):
        y = 74 + i * 58
        o.append(_rect(120, y, 150, 40, fill="#eef3fb", sw=1.3))
        o.append(T(195, y + 25, thr, 8.6, color=col, weight="600"))
        o.append(_arrow(272, y + 20, 356, y + 20, sw=1.6, color=col))
        o.append(_rect(360, y, 220, 40, fill="#f7f9fb", sw=1.3))
        o.append(T(470, y + 25, freq, 8.4))
    o.append(T(330, 330, "Giám sát LDAR thưa hơn khi tỷ lệ rò thấp / LDAR interval lengthens as leak rate falls",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.25 - Measurement frequency for valves controlling VOC",
                   "Hình 3.25 (tr. 69) · Tần suất đo cho van điều khiển VOC",
                   "Hình 3.25 (tr. 69) · Tần suất đo cho van điều khiển hợp chất hữu cơ dễ bay hơi: "
                   "tỷ lệ van rò dưới 0,5% cho phép giám sát hàng năm, cao hơn 2% phải giám sát "
                   "hàng tháng kèm kế hoạch cải thiện chất lượng.",
                   "Figure 3.25 (p. 69) · Measurement frequency for valves controlling volatile "
                   "organic chemicals: below 0.5% leaking valves permits annual monitoring, while "
                   "above 2% requires monthly LDAR with a quality improvement plan.",
                   "Thang tần suất LDAR từ hàng năm đến hàng tháng theo tỷ lệ rò",
                   "LDAR frequency ladder from annual to monthly by leak percentage")


@_reg
def fig_f3_26():
    """Figure 3.26 (p. 70) - ISO 15848-1 Qualification Requirements."""
    w, h = 620, 340
    o = [_defs()]
    o.append(T(310, 40, "Yêu cầu thử nghiệm ISO 15848-1 / ISO 15848-1 qualification",
               9.0, weight="600"))
    t, bot = _tbl(70, 62, [110, 130, 150, 90],
                  ["Kiểu van / Valve", "Cấp chu trình cơ khí / Class",
                   "Số chu trình / Cycles", "Chu trình nhiệt / Temp"],
                  [("Điều khiển / Control", "CC1", "20,000", "2"),
                   ("Điều khiển / Control", "CC2", "60,000", "3"),
                   ("Điều khiển / Control", "CC3", "100,000", "4"),
                   ("Cô lập / Isolation", "CO1", "205", "2"),
                   ("Cô lập / Isolation", "CO2", "1,500", "3"),
                   ("Cô lập / Isolation", "CO3", "2,500", "4")], rh=30, fs=7.6)
    o.append(t)
    o.append(T(310, bot + 24, "Van điều khiển thử ở 10% hành trình hai phía vị trí 50%; van cô lập thử full stroke",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.26 - ISO 15848-1 qualification requirements",
                   "Hình 3.26 (tr. 70) · Yêu cầu thử nghiệm ISO 15848-1",
                   "Hình 3.26 (tr. 70) · Yêu cầu thử nghiệm ISO 15848-1: bảng cấp chu trình cơ khí "
                   "CC1-CC3 cho van điều khiển (20.000-100.000 chu trình) và CO1-CO3 cho van cô "
                   "lập (205-2.500 chu trình), kèm số chu trình nhiệt tương ứng.",
                   "Figure 3.26 (p. 70) · ISO 15848-1 qualification requirements: mechanical cycle "
                   "classes CC1-CC3 for control valves (20,000-100,000 cycles) and CO1-CO3 for "
                   "isolation valves (205-2,500 cycles), with matching thermal cycles.",
                   "Bảng cấp chu trình cơ khí và nhiệt theo ISO 15848-1",
                   "ISO 15848-1 table of mechanical and thermal cycle classes")


@_reg
def fig_f3_27():
    """Figure 3.27 (p. 70) - ISO 15848-1 Measured Leak Rate."""
    w, h = 620, 330
    o = [_defs()]
    o.append(T(310, 40, "Tỷ lệ rò đo được ISO 15848-1 / Measured leak rate",
               9.0, weight="600"))
    t, bot = _tbl(48, 62, [110, 160, 160],
                  ["Cấp kín / Class", "mg/s/m chu vi thân", "atm cm3/s/mm thân"],
                  [("AH", "< 10^-5", "< 1.76x10^-7"),
                   ("BH", "< 10^-4", "< 1.76x10^-6"),
                   ("CH", "< 10^-2", "< 1.76x10^-4")], rh=34, fs=8.0)
    o.append(t)
    o.append(T(310, bot + 22, "H = helium theo phương pháp tỷ lệ rò; M = methane theo EPA Method 21",
               7.4, color=GREY))
    o.append(T(310, bot + 42, "Cấp A thường chỉ đạt được với thiết kế ống mềm / Class A typically only with bellows",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.27 - ISO 15848-1 measured leak rate",
                   "Hình 3.27 (tr. 70) · Tỷ lệ rò đo được theo ISO 15848-1",
                   "Hình 3.27 (tr. 70) · Tỷ lệ rò đo được theo ISO 15848-1 (Phụ lục A): các cấp "
                   "AH, BH, CH với giới hạn tính theo chu vi và đường kính thân; H là thử bằng "
                   "helium, M là thử bằng methane theo EPA Method 21.",
                   "Figure 3.27 (p. 70) · ISO 15848-1 measured leak rate (Annex A): tightness classes "
                   "AH, BH and CH with limits per stem perimeter and diameter; H denotes helium "
                   "testing and M methane testing per EPA Method 21.",
                   "Bảng tỷ lệ rò AH, BH, CH theo ISO 15848-1",
                   "ISO 15848-1 leak rate table for classes AH, BH and CH")


@_reg
def fig_f3_28():
    """Figure 3.28 (p. 70) - ISO 15848-1 Measured Leak Concentration."""
    w, h = 620, 320
    o = [_defs()]
    o.append(T(310, 40, "Nồng độ rò đo được ISO 15848-1 / Measured leak concentration",
               9.0, weight="600"))
    t, bot = _tbl(80, 62, [140, 240],
                  ["Cấp kín / Class", "Nồng độ đo (Phụ lục B) / Measured concentration"],
                  [("AM", "< 50 ppm"),
                   ("BM", "< 100 ppm"),
                   ("CM", "< 500 ppm")], rh=34, fs=8.0)
    o.append(t)
    o.append(T(310, bot + 22, "Phương pháp ngửi theo EPA Method 21 / Sniffing method per EPA Method 21",
               7.4, color=GREY))
    o.append(T(310, bot + 42, "Cấp A thường chỉ đạt được với thiết kế ống mềm / Class A typically only with bellows",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.28 - ISO 15848-1 measured leak concentration",
                   "Hình 3.28 (tr. 70) · Nồng độ rò đo được theo ISO 15848-1",
                   "Hình 3.28 (tr. 70) · Nồng độ rò đo được theo ISO 15848-1 (Phụ lục B, phương "
                   "pháp ngửi EPA Method 21): các cấp AM dưới 50 ppm, BM dưới 100 ppm và CM dưới "
                   "500 ppm.",
                   "Figure 3.28 (p. 70) · ISO 15848-1 measured leak concentration (Annex B, sniffing "
                   "method per EPA Method 21): classes AM below 50 ppm, BM below 100 ppm and CM "
                   "below 500 ppm.",
                   "Bảng nồng độ rò AM, BM, CM theo ISO 15848-1",
                   "ISO 15848-1 leak concentration table for classes AM, BM and CM")


@_reg
def fig_f3_29():
    """Figure 3.29 (p. 71) - FCI 91-1 Leakage Class Summary."""
    w, h = 620, 320
    o = [_defs()]
    o.append(T(310, 40, "Tóm tắt cấp rò FCI 91-1 / FCI 91-1 leakage classes",
               9.0, weight="600"))
    t, bot = _tbl(44, 62, [90, 130, 110, 150],
                  ["Cấp / Class", "Chu trình cơ khí / Mech. cycles",
                   "Chu trình nhiệt / Thermal", "Rò tối đa EPA 21",
                   ],
                  [("A1", "100,000", "3", "100 ppm"),
                   ("A2", "100,000", "3", "500 ppm"),
                   ("B1", "25,000", "3", "100 ppm"),
                   ("B2", "25,000", "3", "500 ppm")], rh=32, fs=7.0)
    o.append(t)
    o.append(T(310, bot + 22, "ANSI/FCI 91-1 dùng phương pháp ngửi EPA Method 21 / Uses EPA Method 21 sniffing",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.29 - FCI 91-1 leakage class summary",
                   "Hình 3.29 (tr. 71) · Tóm tắt cấp rò FCI 91-1",
                   "Hình 3.29 (tr. 71) · Tóm tắt cấp rò FCI 91-1: các cấp A1, A2, B1, B2 với "
                   "100.000 hoặc 25.000 chu trình cơ khí, ba chu trình nhiệt và rò tối đa 100 hoặc "
                   "500 ppm theo EPA Method 21.",
                   "Figure 3.29 (p. 71) · FCI 91-1 leakage class summary: classes A1, A2, B1 and B2 "
                   "with 100,000 or 25,000 mechanical cycles, three thermal cycles and maximum "
                   "leakage of 100 or 500 ppm per EPA Method 21.",
                   "Bảng cấp rò A1, A2, B1, B2 của FCI 91-1",
                   "FCI 91-1 leakage class table A1, A2, B1 and B2")


@_reg
def fig_f3_30():
    """Figure 3.30 (p. 71) - Single PTFE V-Ring Packing."""
    w, h = 600, 340
    o = [_defs()]
    o.append(_rect(214, 76, 56, 210, fill="#e9eef4", sw=1.4))
    o.append(_rect(330, 76, 56, 210, fill="#e9eef4", sw=1.4))
    o.append(_line(300, 52, 300, 306, sw=2.6, color=INK))
    for i in range(3):
        y = 108 + i * 24
        o.append(_poly([(270, y), (330, y), (318, y + 14), (282, y + 14)],
                       fill="#fdf3e6", sw=1.1, close=True))
    o.append(_spring(300, 186, 228, width=40))
    o.append(_leader(336, 120, 428, 96))
    o.append(T(436, 100, "Vòng V PTFE / PTFE V-ring", 7.6, anchor="start"))
    o.append(_leader(336, 204, 428, 148))
    o.append(T(436, 152, "Lò xo / Coil spring", 7.6, anchor="start"))
    o.append(T(300, 320, "Đạt 100 ppmv ở van thân trượt, dưới 300 psi và -18 đến 93 độ C",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.30 - Single PTFE V-ring packing",
                   "Hình 3.30 (tr. 71) · Bộ đệm V-Ring PTFE đơn",
                   "Hình 3.30 (tr. 71) · Bộ đệm V-Ring PTFE đơn dùng lò xo giữa bộ đệm và vòng hộp "
                   "đệm, đạt tiêu chí 100 ppmv cho van thân trượt khi áp suất không quá 300 psi và "
                   "nhiệt độ -18 đến 93 độ C; ma sát vận hành rất thấp.",
                   "Figure 3.30 (p. 71) · Single PTFE V-ring packing uses a coil spring between the "
                   "packing and packing box ring; it meets the 100 ppmv criterion for sliding-stem "
                   "valves below 300 psi and -18 to 93 deg C, with very low operating friction.",
                   "Mặt cắt bộ đệm V-ring PTFE đơn có lò xo",
                   "Cutaway of single PTFE V-ring packing with a coil spring")


@_reg
def fig_f3_31():
    """Figure 3.31 (p. 72) - ENVIRO-SEAL PTFE Packing System."""
    w, h = 620, 356
    o = [_defs()]
    o.append(_rect(210, 72, 58, 214, fill="#e9eef4", sw=1.4))
    o.append(_rect(348, 72, 58, 214, fill="#e9eef4", sw=1.4))
    o.append(_line(308, 48, 308, 308, sw=2.6, color=INK))
    # Belleville spring stack
    for i in range(3):
        y = 84 + i * 12
        o.append(_line(276, y, 340, y + 6, sw=1.3, color=RED))
        o.append(_line(340, y + 6, 276, y + 12, sw=1.3, color=RED))
    # PTFE/carbon packing rings
    for i in range(3):
        y = 134 + i * 26
        o.append(_rect(272, y, 72, 16, fill="#fdf3e6", sw=1.1))
    o.append(_rect(272, 216, 72, 14, fill="#dfe7ef", sw=1.1))
    o.append(_leader(344, 100, 438, 88))
    o.append(T(438, 88, "Bộ lò xo Belleville", 7.2, anchor="start"))
    o.append(T(438, 99, "Belleville springs", 7.2, anchor="start"))
    o.append(_leader(346, 160, 438, 140))
    o.append(T(438, 140, "Vòng đệm PTFE-carbon", 7.2, anchor="start"))
    o.append(T(438, 151, "PTFE-carbon rings", 7.2, anchor="start"))
    o.append(T(308, 324, "Tải không đổi, chống ép ra, căn chỉnh thân / Constant load, anti-extrusion, alignment",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.31 - ENVIRO-SEAL PTFE packing system",
                   "Hình 3.31 (tr. 72) · Hệ thống đệm PTFE ENVIRO-SEAL",
                   "Hình 3.31 (tr. 72) · Hệ thống đệm PTFE ENVIRO-SEAL dùng lò xo Belleville tạo "
                   "tải không đổi, chống ép vật liệu mềm, căn chỉnh thân trong lỗ nắp và giảm số "
                   "vòng đệm; dùng tới 750 psi và 232 độ C cho cả van trượt lẫn van quay.",
                   "Figure 3.31 (p. 72) · ENVIRO-SEAL PTFE packing system with Belleville springs "
                   "for constant load, anti-extrusion containment, stem alignment and fewer seal "
                   "rings; suited to 750 psi and 232 deg C in both sliding-stem and rotary valves.",
                   "Mặt cắt hệ thống đệm PTFE có lò xo Belleville và vòng chống ép",
                   "Cutaway of ENVIRO-SEAL PTFE packing with Belleville springs")


@_reg
def fig_f3_32():
    """Figure 3.32 (p. 72) - ENVIRO-SEAL Duplex Packing System."""
    w, h = 620, 356
    o = [_defs()]
    o.append(_rect(208, 72, 58, 214, fill="#e9eef4", sw=1.4))
    o.append(_rect(348, 72, 58, 214, fill="#e9eef4", sw=1.4))
    o.append(_line(306, 48, 306, 308, sw=2.6, color=INK))
    for i in range(3):
        y = 84 + i * 12
        o.append(_line(274, y, 338, y + 6, sw=1.3, color=RED))
        o.append(_line(338, y + 6, 274, y + 12, sw=1.3, color=RED))
    for i in range(3):
        y = 134 + i * 26
        o.append(_rect(270, y, 72, 16, fill="#fdf3e6", sw=1.1))       # PTFE
        o.append(_rect(270, y + 16, 72, 10, fill="#b9b0a0", sw=1.1))  # graphite
    o.append(_leader(344, 150, 436, 100))
    o.append(T(444, 104, "PTFE / PTFE", 7.4, anchor="start"))
    o.append(_leader(344, 168, 436, 136))
    o.append(T(444, 140, "Than chì / Graphite", 7.4, anchor="start"))
    o.append(T(306, 324, "Giải pháp ma sát thấp, rò thấp, thử lửa API 589 / Low friction, low emission, fire-tested",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.32 - ENVIRO-SEAL Duplex packing system",
                   "Hình 3.32 (tr. 72) · Hệ thống đệm kép ENVIRO-SEAL",
                   "Hình 3.32 (tr. 72) · Hệ thống đệm kép ENVIRO-SEAL kết hợp PTFE và than chì, "
                   "cho giải pháp ma sát thấp, rò thấp, đã thử lửa theo API 589 cho van thân trượt "
                   "với nhiệt độ quá trình tới 232 độ C; không dùng cho van quay.",
                   "Figure 3.32 (p. 72) · ENVIRO-SEAL Duplex packing combines PTFE and graphite for "
                   "a low-friction, low-emission, fire-tested solution (API 589) on sliding-stem "
                   "valves to 232 deg C; not offered on rotary valves.",
                   "Mặt cắt hệ thống đệm kép PTFE và than chì",
                   "Cutaway of duplex PTFE and graphite packing")


@_reg
def fig_f3_33():
    """Figure 3.33 (p. 72) - ENVIRO-SEAL Graphite ULF Packing System."""
    w, h = 620, 376
    o = [_defs()]
    o.append(_rect(206, 72, 60, 226, fill="#e9eef4", sw=1.4))
    o.append(_rect(352, 72, 60, 226, fill="#e9eef4", sw=1.4))
    o.append(_line(306, 46, 306, 314, sw=2.6, color=INK))
    for i in range(3):
        y = 84 + i * 12
        o.append(_line(272, y, 340, y + 6, sw=1.3, color=RED))
        o.append(_line(340, y + 6, 272, y + 12, sw=1.3, color=RED))
    for i in range(4):
        y = 132 + i * 30
        o.append(_rect(268, y, 76, 20, fill="#b9b0a0", sw=1.1))
        o.append(_rect(268, y + 7, 76, 4, fill="#fdf3e6", sw=0.6))
        o.append(_rect(262, y + 4, 6, 12, fill="#fdf3e6", sw=0.6))
        o.append(_rect(344, y + 4, 6, 12, fill="#fdf3e6", sw=0.6))
    o.append(_leader(350, 160, 442, 104))
    o.append(T(450, 108, "Lớp PTFE mỏng / Thin PTFE layers", 7.4, anchor="start"))
    o.append(_leader(350, 210, 442, 152))
    o.append(T(450, 156, "Vòng than chì / Graphite rings", 7.4, anchor="start"))
    o.append(T(306, 344, "ULF giảm ma sát, tăng làm kín và kéo dài tuổi thọ / ULF reduces friction and extends life",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.33 - ENVIRO-SEAL Graphite ULF packing system",
                   "Hình 3.33 (tr. 72) · Hệ thống đệm than chì ULF ENVIRO-SEAL",
                   "Hình 3.33 (tr. 72) · Hệ thống đệm than chì ULF ENVIRO-SEAL dùng cho nhiệt độ "
                   "trên 232 độ C, gồm các lớp PTFE rất mỏng bên trong vòng đệm và vòng đệm PTFE "
                   "mỏng hai bên; cách bố trí này giảm ma sát, hỗ trợ làm kín và kéo dài tuổi thọ.",
                   "Figure 3.33 (p. 72) · ENVIRO-SEAL Graphite ULF packing for temperatures above "
                   "232 deg C, with very thin PTFE layers inside the rings and thin PTFE washers on "
                   "each side; the placement reduces friction, promotes sealing and extends cycle life.",
                   "Mặt cắt bộ đệm than chì ULF có các lớp PTFE mỏng",
                   "Cutaway of graphite ULF packing with thin PTFE layers")


@_reg
def fig_f3_34():
    """Figure 3.34 (p. 73) - ENVIRO-SEAL Graphite Packing for Rotary Valves."""
    w, h = 620, 376
    o = [_defs()]
    o.append(_rect(206, 74, 60, 224, fill="#e9eef4", sw=1.4))
    o.append(_rect(352, 74, 60, 224, fill="#e9eef4", sw=1.4))
    o.append(_circle(306, 168, 16, fill="#f4f7fb", sw=1.4))        # rotary shaft
    o.append(_line(306, 46, 306, 312, sw=2.6, color=INK))
    for i in range(4):
        y = 120 + i * 32
        o.append(_rect(268, y, 76, 18, fill="#b9b0a0", sw=1.1))
    o.append(_rect(266, 84, 80, 12, fill="#fdf3e6", sw=1.1))
    o.append(_rect(266, 290, 80, 12, fill="#fdf3e6", sw=1.1))
    o.append(_leader(352, 140, 442, 100))
    o.append(T(450, 104, "Bích đệm / Packing flange", 7.4, anchor="start"))
    o.append(_leader(352, 188, 442, 148))
    o.append(T(450, 152, "Vòng than chì / Graphite rings", 7.4, anchor="start"))
    o.append(T(306, 344, "Độ kín 100 ppmv tới 1500 psi, -6 đến 316 độ C / 100 ppmv to 1500 psi",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.34 - ENVIRO-SEAL graphite packing system for rotary valves",
                   "Hình 3.34 (tr. 73) · Hệ thống đệm than chì ENVIRO-SEAL cho van quay",
                   "Hình 3.34 (tr. 73) · Hệ thống đệm than chì ENVIRO-SEAL cho van quay: dùng cho "
                   "ứng dụng môi trường từ -6 đến 316 độ C hoặc nơi cần an toàn cháy; chịu áp tới "
                   "1500 psi mà vẫn đạt 100 ppmv theo EPA, có thể dùng tới 371 độ C ngoài môi trường.",
                   "Figure 3.34 (p. 73) · ENVIRO-SEAL graphite packing for rotary valves: for "
                   "environmental service from -6 to 316 deg C or where fire safety matters; it "
                   "withstands 1500 psi while meeting 100 ppmv EPA criteria and can reach 371 deg C "
                   "in non-environmental service.",
                   "Mặt cắt bộ đệm than chì cho van quay có trục và bích đệm",
                   "Cutaway of graphite packing for a rotary valve with shaft and flange")


@_reg
def fig_f3_35():
    """Figure 3.35 (p. 74) - Sliding-Stem Environmental Packing Selection."""
    w, h = 660, 420
    o = [_defs()]
    o.append(T(330, 34, "Lựa chọn đệm môi trường cho van thân trượt / Sliding-stem packing selection",
               9.0, weight="600"))
    t, bot = _tbl(24, 52, [150, 196, 92, 92, 76],
                  ["Hệ đệm / Packing", "Giới hạn P và T", "Làm kín / Seal",
                   "Tuổi thọ / Life", "Ma sát / Friction"],
                  [("PTFE V-Ring đơn", "300 psi, -18-93 C", "Better", "Long", "Very low"),
                   ("ENVIRO-SEAL PTFE", "750 psi, -46-232 C", "Superior", "Very long", "Low"),
                   ("ISO-Seal PTFE", "6000 psi, -46-232 C", "Superior", "Very long", "Low"),
                   ("ENVIRO-SEAL Duplex", "750 psi, -46-232 C", "Superior", "Very long", "Low"),
                   ("ENVIRO-SEAL Graphite ULF", "1500 psi, -7-315 C", "Superior", "Very long", "Moderate"),
                   ("ISO-Seal Graphite", "3365 psi, -46-400 C", "Superior", "Very long", "Moderate")],
                  rh=33, fs=7.0)
    o.append(t)
    o.append(T(330, bot + 22, "Sợi than chì bện và PTFE kép không đạt yêu cầu làm kín môi trường",
               7.4, color=RED))
    return _finish(w, h, o, "Figure 3.35 - Sliding-stem environmental packing selection",
                   "Hình 3.35 (tr. 74) · Lựa chọn đệm môi trường cho van thân trượt",
                   "Hình 3.35 (tr. 74) · Bảng so sánh các lựa chọn đệm thân trượt theo áp suất, "
                   "nhiệt độ, hiệu năng làm kín, tuổi thọ và ma sát. Sợi than chì bện và PTFE kép "
                   "không được chấp nhận làm giải pháp làm kín môi trường.",
                   "Figure 3.35 (p. 74) · Table comparing sliding-stem packing choices by pressure, "
                   "temperature, seal performance, service life and friction. Braided graphite "
                   "filament and double PTFE are not acceptable environmental sealing solutions.",
                   "Bảng lựa chọn đệm van thân trượt theo hiệu năng và tuổi thọ",
                   "Sliding-stem packing selection table by seal performance and life")


@_reg
def fig_f3_36():
    """Figure 3.36 (p. 74) - Rotary Environmental Packing Selection."""
    w, h = 660, 340
    o = [_defs()]
    o.append(T(330, 34, "Lựa chọn đệm môi trường cho van quay / Rotary packing selection",
               9.0, weight="600"))
    t, bot = _tbl(34, 52, [170, 206, 96, 96],
                  ["Hệ đệm / Packing", "Giới hạn P và T", "Làm kín / Seal",
                   "Ma sát / Friction"],
                  [("ENVIRO-SEAL PTFE", "750 psi, -46-232 C", "Superior", "Low"),
                   ("ENVIRO-SEAL Graphite", "1500 psi, -18-315 C", "Superior", "Moderate"),
                   ("ISO-Seal Graphite", "1500 psi, -46-400 C", "Superior", "Moderate")],
                  rh=36, fs=7.6)
    o.append(t)
    o.append(T(330, bot + 24, "PTFE đơn và đệm băng than chì không đạt cho van quay",
               7.4, color=RED))
    o.append(T(330, bot + 46, "Single PTFE and graphite ribbon are poor fugitive seals on rotary valves",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 3.36 - Rotary environmental packing selection",
                   "Hình 3.36 (tr. 74) · Lựa chọn đệm môi trường cho van quay",
                   "Hình 3.36 (tr. 74) · Bảng so sánh các lựa chọn đệm cho van quay. PTFE đơn và "
                   "bố trí đệm băng than chì không đạt yêu cầu làm kín khí thải bay hơi; ENVIRO-SEAL "
                   "PTFE và than chì cho hiệu năng vượt trội.",
                   "Figure 3.36 (p. 74) · Table comparing packing choices for rotary valves. Single "
                   "PTFE and graphite ribbon arrangements perform poorly as fugitive-emission seals; "
                   "ENVIRO-SEAL PTFE and graphite give superior performance.",
                   "Bảng lựa chọn đệm van quay theo áp suất và nhiệt độ",
                   "Rotary packing selection table by pressure and temperature")


@_reg
def fig_f3_37():
    """Figure 3.37 (p. 74) - Characterized Cages for Globe-Style Bodies."""
    w, h = 620, 340
    o = [_defs()]
    shapes = [(140, "Mở nhanh / Quick-opening"),
              (310, "Tuyến tính / Linear"),
              (480, "Phần trăm bằng / Equal-percentage")]
    for cx, lab in shapes:
        o.append(_rect(cx - 46, 88, 92, 168, fill="#eef3fb", sw=1.5))
        o.append(_rect(cx - 46, 88, 14, 168, fill="#dfe7ef", sw=1.1))
        o.append(_rect(cx + 32, 88, 14, 168, fill="#dfe7ef", sw=1.1))
    # window shapes on front wall
    o.append(_rect(116, 176, 48, 72, fill="#ffffff", sw=1.0))         # quick
    o.append(_poly([(286, 232), (334, 232), (334, 152)],
                   fill="#ffffff", sw=1.0, close=True))              # linear
    pts = [(456, 232)]
    for k in range(9):
        t = k / 8.0
        pts.append((456 + 48 * (1 - (1 - t) ** 2), 232 - 80 * t))
    pts.append((456, 152))
    o.append(_poly(pts, fill="#ffffff", sw=1.0, close=True))         # equal %
    for cx, lab in shapes:
        o.append(T(cx, 286, lab, 7.8, color=INK))
    o.append(T(310, 320, "Hình dạng cửa sổ lồng quyết định đặc tính dòng vốn có / Cage window shape sets inherent characteristic",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.37 - Characterized cages for globe-style valve bodies",
                   "Hình 3.37 (tr. 74) · Lồng định hình cho thân van kiểu cầu",
                   "Hình 3.37 (tr. 74) · Lồng định hình: hình dạng cửa sổ trên thành lồng quyết định "
                   "đặc tính dòng — mở nhanh, tuyến tính hoặc phần trăm bằng. Thay lồng để đổi đặc "
                   "tính không cần thay nút van hay vòng chỗ ngồi.",
                   "Figure 3.37 (p. 74) · Characterized cages: the shape of the cage windows sets "
                   "the inherent flow characteristic - quick-opening, linear or equal-percentage. "
                   "Changing cages does not require changing the plug or seat ring.",
                   "Ba dạng cửa sổ lồng: mở nhanh, tuyến tính, phần trăm bằng",
                   "Three cage window shapes: quick-opening, linear and equal-percentage")


@_reg
def fig_f3_38():
    """Figure 3.38 (p. 75) - Inherent Flow Characteristics Curves."""
    w, h = 620, 360
    o = [_defs()]
    x0, y0, W, H = 110, 60, 360, 220
    o.append(_axes(x0, y0, W, H, "Hành trình định mức (%) / Rated travel (%)",
                   "Lưu lượng định mức (%)",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda t: t, x0, y0, W, H, sw=1.8, color=BLUE))
    o.append(_curve(lambda t: (math.exp(t) - 1) / (math.e - 1),
                    x0, y0, W, H, sw=1.8, color=GREEN))
    o.append(_curve(lambda t: math.sqrt(t), x0, y0, W, H, sw=1.8, color=RED))
    o.append(_line(500, 96, 512, 96, sw=2.0, color=BLUE))
    o.append(T(518, 100, "Tuyến tính / Linear", 7.0, anchor="start"))
    o.append(_line(500, 128, 512, 128, sw=2.0, color=GREEN))
    o.append(T(518, 132, "Phần trăm bằng", 7.0, anchor="start"))
    o.append(T(518, 142, "Equal-percentage", 7.0, anchor="start"))
    o.append(_line(500, 168, 512, 168, sw=2.0, color=RED))
    o.append(T(518, 168, "Mở nhanh", 7.0, anchor="start"))
    o.append(T(518, 178, "Quick-opening", 7.0, anchor="start"))
    o.append(T(310, 326, "Đặc tính vốn có tại áp suất chênh không đổi / Inherent curves at constant differential",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.38 - Inherent flow characteristics curves",
                   "Hình 3.38 (tr. 75) · Đường đặc tính dòng vốn có",
                   "Hình 3.38 (tr. 75) · Đường đặc tính dòng vốn có: tuyến tính, phần trăm bằng và "
                   "mở nhanh, biểu diễn quan hệ giữa phần trăm lưu lượng lớn nhất và phần trăm "
                   "hành trình khi giữ chênh áp không đổi qua van.",
                   "Figure 3.38 (p. 75) · Inherent flow characteristic curves: linear, "
                   "equal-percentage and quick-opening, relating percentage of maximum flow to "
                   "percentage of travel at a constant differential pressure across the valve.",
                   "Ba đường cong đặc tính dòng vốn có trên cùng một trục",
                   "Three inherent flow characteristic curves on one axes")


@_reg
def fig_f3_39():
    """Figure 3.39 (p. 75) - Various Plug Contours for Flow Characterization."""
    w, h = 620, 340
    o = [_defs()]
    kinds = [(140, "Mở nhanh / Quick-opening"),
             (310, "Tuyến tính / Linear"),
             (480, "Phần trăm bằng / Equal-percentage")]
    for cx, lab in kinds:
        o.append(_line(cx - 60, 236, cx + 60, 236, sw=2.0, color=INK))  # seat
        o.append(_line(cx, 78, cx, 210, sw=2.2, color=INK))              # stem
    o.append(_poly([(96, 210), (184, 210), (160, 150), (120, 150)],
                   fill="#fdf3e6", sw=1.3, close=True))
    o.append(_poly([(266, 210), (354, 210), (330, 128), (290, 128)],
                   fill="#fdf3e6", sw=1.3, close=True))
    pts = [(436, 210), (524, 210), (500, 120), (486, 146), (476, 172), (460, 192)]
    o.append(_poly(pts, fill="#fdf3e6", sw=1.3, close=True))
    for cx, lab in kinds:
        o.append(T(cx, 268, lab, 7.8, color=INK))
    o.append(T(310, 312, "Đường bao nút cạnh vòng chỗ ngồi quyết định đặc tính / Plug contour at the seat sets the characteristic",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.39 - Various plug contours for different flow characterization",
                   "Hình 3.39 (tr. 75) · Các dạng đường bao nút van cho đặc tính dòng",
                   "Hình 3.39 (tr. 75) · Các dạng đường bao nút van: hình dạng bề mặt nút cạnh "
                   "vòng chỗ ngồi quyết định đặc tính dòng vốn có; khi nút dịch chuyển, diện tích "
                   "dòng không bị cản thay đổi theo đường bao của nút.",
                   "Figure 3.39 (p. 75) · Various plug contours for flow characterization: the plug "
                   "surface next to the seat ring determines the inherent characteristic; as the "
                   "plug moves, the unobstructed flow area changes with the plug contour.",
                   "Ba dạng đường bao nút van cạnh chỗ ngồi",
                   "Three plug contours at the seat ring")


@_reg
def fig_f3_40():
    """Figure 3.40 (p. 76) - Quick-Opening Flow Characteristic Construction."""
    w, h = 600, 360
    o = [_defs()]
    o.append(_rect(180, 100, 200, 148, fill="#f4f7fb", sw=1.7))
    o.append(_rect(120, 138, 62, 46, fill="#e9eef4", sw=1.3))
    o.append(_rect(106, 128, 18, 66, fill="#dfe7ef", sw=1.2))
    o.append(_rect(378, 138, 62, 46, fill="#e9eef4", sw=1.3))
    o.append(_rect(438, 128, 18, 66, fill="#dfe7ef", sw=1.2))
    o.append(_rect(248, 52, 64, 48, fill="#e9eef4", sw=1.3))
    o.append(_line(280, 24, 280, 190, sw=2.4, color=INK))
    o.append(_poly([(252, 156), (308, 156), (296, 118), (264, 118)],
                   fill="#fdf3e6", sw=1.3, close=True))
    o.append(_rect(248, 202, 64, 10, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(150, 160, 214, 160, sw=1.6, color=GREEN))
    o.append(_arrow(346, 160, 412, 160, sw=1.6, color=GREEN))
    o.append(_leader(286, 138, 424, 92))
    o.append(T(432, 96, "Tiết diện dòng / Flow area", 7.5, anchor="start"))
    o.append(T(300, 300, "Đường kính cổng, nút van, thân, vòng chỗ ngồi / Port diameter, plug, stem, seat ring",
               7.4, color=GREY))
    o.append(T(300, 322, "Cấu hình điển hình cho đặc tính mở nhanh / Typical quick-opening construction",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.40 - Typical construction for quick-opening flow",
                   "Hình 3.40 (tr. 76) · Cấu hình điển hình cho dòng mở nhanh",
                   "Hình 3.40 (tr. 76) · Cấu hình điển hình cho đặc tính mở nhanh: đường kính cổng, "
                   "nút van, diện tích dòng, thân và vòng chỗ ngồi được bố trí để diện tích dòng "
                   "tăng nhanh ngay ở đoạn đầu hành trình.",
                   "Figure 3.40 (p. 76) · Typical construction for quick-opening flow: port "
                   "diameter, plug, flow area, stem and seat ring arranged so that flow area "
                   "increases rapidly in the first part of travel.",
                   "Mặt cắt van với nhãn đường kính cổng và diện tích dòng",
                   "Valve cutaway labelled with port diameter and flow area")


@_reg
def fig_f3_41():
    """Figure 3.41 (p. 76) - Cross Section of Cage Guiding and Plug Guiding."""
    w, h = 620, 380
    o = [_defs()]
    o.append(_rect(198, 90, 200, 178, fill="#f4f7fb", sw=1.7))
    o.append(_rect(130, 146, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(116, 136, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(396, 146, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(464, 136, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(258, 42, 74, 48, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 14, 295, 200, sw=2.4, color=INK))
    o.append(_rect(252, 118, 18, 122, fill="#dfe7ef", sw=1.2))
    o.append(_rect(320, 118, 18, 122, fill="#dfe7ef", sw=1.2))
    o.append(_rect(272, 176, 46, 48, fill="#fdf3e6", sw=1.4))
    o.append(_rect(268, 224, 54, 10, fill="#dfe7ef", sw=1.2))
    o.append(_leader(256, 140, 410, 96))
    o.append(T(418, 100, "Dẫn hướng bằng lồng / Cage guiding", 7.4, anchor="start"))
    o.append(_leader(316, 196, 410, 140))
    o.append(T(418, 144, "Dẫn hướng bằng nút / Plug guiding", 7.4, anchor="start"))
    o.append(T(298, 320, "Đường kính ngoài nút sát thành trong lồng suốt hành trình / Plug OD close to cage ID over full travel",
               7.4, color=GREY))
    o.append(T(298, 342, "Nắp, lồng và chỗ ngồi tự căn chỉnh / Bonnet, cage and seat are self-aligning",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.41 - Cross-sectional view of cage guiding",
                   "Hình 3.41 (tr. 76) · Mặt cắt dẫn hướng bằng lồng",
                   "Hình 3.41 (tr. 76) · Mặt cắt dẫn hướng bằng lồng: đường kính ngoài của nút van "
                   "sát thành trong lồng suốt hành trình; nắp, lồng và vòng chỗ ngồi tự căn chỉnh "
                   "nên đảm bảo nút van khớp chỗ ngồi và bộ đệm khi đóng.",
                   "Figure 3.41 (p. 76) · Cross-section of cage guiding: the plug outside diameter "
                   "stays close to the cage inside wall throughout travel; bonnet, cage and seat "
                   "ring are self-aligning, ensuring correct plug, packing and seating alignment.",
                   "Mặt cắt van cầu có lồng dẫn và nút van được dẫn hướng",
                   "Globe valve cutaway showing cage and plug guiding")


@_reg
def fig_f3_42():
    """Figure 3.42 (p. 77) - Adapter Method for Reduced Flow Capacity."""
    w, h = 620, 380
    o = [_defs()]
    o.append(_rect(198, 90, 200, 178, fill="#f4f7fb", sw=1.7))
    o.append(_rect(130, 146, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(116, 136, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(396, 146, 70, 52, fill="#e9eef4", sw=1.4))
    o.append(_rect(464, 136, 18, 72, fill="#dfe7ef", sw=1.3))
    o.append(_rect(258, 42, 74, 48, fill="#e9eef4", sw=1.3))
    o.append(_line(295, 14, 295, 190, sw=2.4, color=INK))
    o.append(_rect(262, 112, 16, 104, fill="#dfe7ef", sw=1.2))
    o.append(_rect(312, 112, 16, 104, fill="#dfe7ef", sw=1.2))
    o.append(_rect(276, 164, 36, 40, fill="#fdf3e6", sw=1.3))
    o.append(_rect(272, 204, 44, 9, fill="#dfe7ef", sw=1.2))
    o.append(_rect(258, 92, 74, 14, fill="#fdf3e6", sw=1.2))       # upper adapter
    o.append(_rect(258, 250, 74, 14, fill="#fdf3e6", sw=1.2))      # lower adapter
    o.append(_leader(334, 100, 412, 92))
    o.append(T(420, 96, "Đoạn chuyển tiếp trên / Upper adapter", 7.4, anchor="start"))
    o.append(_leader(334, 258, 412, 140))
    o.append(T(420, 144, "Đoạn chuyển tiếp dưới / Lower adapter", 7.4, anchor="start"))
    o.append(T(298, 322, "Trim cỡ nhỏ hơn ghép vào thân lớn / Smaller trim fitted into a larger body",
               7.4, color=GREY))
    o.append(T(298, 344, "Giảm lưu lượng, giảm vận tốc đầu ra, sửa lỗi chọn quá cỡ",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.42 - Adapter method for reduced flow capacity",
                   "Hình 3.42 (tr. 77) · Phương pháp đoạn chuyển tiếp giảm lưu lượng",
                   "Hình 3.42 (tr. 77) · Phương pháp đoạn chuyển tiếp: dùng nút, lồng và vòng chỗ "
                   "ngồi từ cỡ van nhỏ hơn cùng kiểu, cùng đoạn nối phía trên lồng và dưới chỗ ngồi "
                   "để ghép vào thân lớn; giúp giảm lưu lượng, giảm vận tốc và sửa lỗi chọn van quá cỡ.",
                   "Figure 3.42 (p. 77) · Adapter method: plug, cage and seat ring from a smaller "
                   "valve of similar construction are fitted with adapters above the cage and below "
                   "the seat into a larger body, reducing capacity and velocity and correcting "
                   "over-sizing errors.",
                   "Thân van lớn chứa trim cỡ nhỏ qua hai đoạn chuyển tiếp",
                   "Large body holding smaller trim via upper and lower adapters")


@_reg
def fig_f3_43():
    """Figure 3.43 (p. 77) - Diaphragm Actuators, direct and reverse acting."""
    w, h = 640, 360
    o = [_defs()]
    for cx, lab, up in ((180, "Tác động trực tiếp / Direct-acting", False),
                        (460, "Tác động ngược / Reverse-acting", True)):
        o.append(_ellipse(cx, 176, 110, 30, fill="#eef3fb", sw=1.6))    # diaphragm
        o.append(_rect(cx - 108, 96, 216, 80, fill="#f7f9fb", sw=1.4))  # upper case
        o.append(_rect(cx - 108, 176, 216, 80, fill="#f7f9fb", sw=1.4)) # lower case
        o.append(_line(cx, 176, cx, 316, sw=2.4, color=INK))
        o.append(_spring(cx, 112, 168, width=40))
        o.append(_arrow(cx, 74, cx, 108, sw=1.7, color=RED))
        direction = "lên / up" if up else "xuống / down"
        o.append(_arrow(cx - 20, 300, cx - 20, 332 if not up else 276,
                        sw=1.6, color=GREEN))
        o.append(T(cx, 356, lab, 7.8, color=INK))
    o.append(T(320, 40, "Áp suất cấp tăng đẩy màng và dịch chuyển thân / Increasing air pressure moves the diaphragm and stem",
               8.4, weight="600"))
    o.append(T(320, 60, "Lực đầu ra ròng = lực màng trừ lực lò xo / Net thrust = diaphragm force minus spring force",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.43 - Diaphragm actuators",
                   "Hình 3.43 (tr. 77) · Cơ cấu chấp hành màng",
                   "Hình 3.43 (tr. 77) · Cơ cấu chấp hành màng khí nén: tác động trực tiếp (áp suất "
                   "tăng đẩy màng xuống, thân dãn ra) và tác động ngược (đẩy màng lên, thân co lại). "
                   "Lực đầu ra ròng là hiệu giữa lực màng và lực lò xo.",
                   "Figure 3.43 (p. 77) · Pneumatic diaphragm actuators: direct-acting (increasing "
                   "pressure pushes the diaphragm down and extends the stem) and reverse-acting "
                   "(pushes it up and retracts the stem). Net output thrust is diaphragm force minus "
                   "spring force.",
                   "Cơ cấu màng tác động trực tiếp và tác động ngược",
                   "Direct-acting and reverse-acting diaphragm actuators")


@_reg
def fig_f3_44():
    """Figure 3.44 (p. 78) - Field-Reversible Multi-Spring Actuator."""
    w, h = 600, 376
    o = [_defs()]
    o.append(_rect(180, 80, 240, 76, fill="#f7f9fb", sw=1.5))
    o.append(_ellipse(300, 156, 114, 26, fill="#eef3fb", sw=1.5))
    o.append(_rect(180, 156, 240, 96, fill="#f7f9fb", sw=1.5))
    o.append(_line(300, 156, 300, 320, sw=2.6, color=INK))
    for dx in (-56, 56):
        o.append(_spring(300 + dx, 96, 150, width=34))
    o.append(_arrow(300, 42, 300, 80, sw=1.8, color=RED))
    o.append(_leader(360, 118, 452, 92))
    o.append(T(460, 96, "Nhiều lò xo / Multi-spring", 7.5, anchor="start"))
    o.append(_leader(358, 196, 452, 152))
    o.append(T(444, 152, "Đảo chiều tại hiện trường", 7.2, anchor="start"))
    o.append(T(444, 163, "Field-reversible", 7.2, anchor="start"))
    o.append(T(300, 344, "Có thể lắp tác động trực tiếp hoặc ngược / Assembled for either action",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.44 - Field-reversible multi-spring actuator",
                   "Hình 3.44 (tr. 78) · Cơ cấu nhiều lò xo đảo chiều tại hiện trường",
                   "Hình 3.44 (tr. 78) · Cơ cấu nhiều lò xo có thể đảo chiều tại hiện trường: dùng "
                   "nhiều lò xo nhỏ trong vỏ, cho phép lắp thành tác động trực tiếp hoặc ngược mà "
                   "không cần thay đổi chi tiết, linh hoạt khi cấu hình tại công trường.",
                   "Figure 3.44 (p. 78) · Field-reversible multi-spring actuator: several small "
                   "springs in the case allow assembly for direct or reverse action without changing "
                   "parts, giving flexibility during field configuration.",
                   "Cơ cấu màng nhiều lò xo có thể đổi chiều tác động",
                   "Multi-spring diaphragm actuator with reversible action")


@_reg
def fig_f3_45():
    """Figure 3.45 (p. 78) - Diaphragm Actuator for Rotary Valve."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(180, 74, 210, 72, fill="#f7f9fb", sw=1.5))
    o.append(_ellipse(285, 146, 100, 24, fill="#eef3fb", sw=1.5))
    o.append(_rect(180, 146, 210, 84, fill="#f7f9fb", sw=1.5))
    o.append(_line(285, 146, 285, 250, sw=2.4, color=INK))
    o.append(_spring(285, 92, 140, width=36))
    o.append(_arrow(285, 42, 285, 76, sw=1.7, color=RED))
    o.append(_circle(285, 264, 16, fill="#fdf3e6", sw=1.4))
    o.append(_line(285, 264, 380, 264, sw=3.0, color=INK))          # lever
    o.append(_line(380, 264, 380, 300, sw=2.4, color=INK))          # shaft
    o.append(_path("M380,232 A32,32 0 0,1 408,264", fill="none",
                   sw=1.0, color=RED, dash="4 3"))
    o.append(T(420, 250, "Cần đẩy / Actuator lever", 7.5, anchor="start"))
    o.append(T(310, 334, "Tùy hướng cần mà áp suất tăng mở hoặc đóng van / Lever orientation decides open or close",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.45 - Diaphragm actuator for rotary valve",
                   "Hình 3.45 (tr. 78) · Cơ cấu màng cho van quay",
                   "Hình 3.45 (tr. 78) · Cơ cấu màng tác động trực tiếp cho van quay: áp suất tăng "
                   "đẩy màng xuống, truyền qua cần gắn trên trục van; tùy hướng cần mà van mở hoặc "
                   "đóng.",
                   "Figure 3.45 (p. 78) · Direct-acting diaphragm actuator for rotary valves: "
                   "increasing air pressure pushes the diaphragm down, driving a lever on the valve "
                   "shaft; depending on lever orientation the valve opens or closes.",
                   "Cơ cấu màng nối cần đẩy lên trục van quay",
                   "Diaphragm actuator driving a lever on a rotary valve shaft")


@_reg
def fig_f3_46():
    """Figure 3.46 (p. 78) - Control Valve with Double-Acting Piston Actuator."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(210, 62, 180, 130, fill="#f7f9fb", sw=1.6))     # cylinder
    o.append(_rect(214, 116, 172, 20, fill="#dfe7ef", sw=1.2))     # piston
    o.append(_line(300, 126, 300, 316, sw=2.6, color=INK))
    o.append(_arrow(260, 90, 260, 112, sw=1.5, color=RED))
    o.append(_arrow(340, 180, 340, 158, sw=1.5, color=RED))
    o.append(_rect(262, 192, 76, 66, fill="#e9eef4", sw=1.4))      # bonnet
    o.append(_rect(226, 258, 148, 92, fill="#f4f7fb", sw=1.6))     # body
    o.append(_rect(162, 284, 66, 40, fill="#e9eef4", sw=1.3))
    o.append(_rect(148, 274, 18, 60, fill="#dfe7ef", sw=1.2))
    o.append(_rect(372, 284, 66, 40, fill="#e9eef4", sw=1.3))
    o.append(_rect(436, 274, 18, 60, fill="#dfe7ef", sw=1.2))
    o.append(_leader(392, 100, 446, 84))
    o.append(T(454, 88, "Xi lanh piston / Piston cylinder", 7.4, anchor="start"))
    o.append(T(300, 380, "Tác động kép cho lực lớn cả hai chiều / Double acting gives maximum force in both directions",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.46 - Control valve with double-acting piston actuator",
                   "Hình 3.46 (tr. 78) · Van điều khiển có cơ cấu piston tác động kép",
                   "Hình 3.46 (tr. 78) · Van điều khiển có cơ cấu piston tác động kép: dùng khí "
                   "áp suất cao tới 150 psig, cho lực đẩy cực đại và tốc độ hành trình nhanh ở cả "
                   "hai chiều; có thể lắp van trip khí nén và hệ thống khóa khi mất áp cấp.",
                   "Figure 3.46 (p. 78) · Control valve with double-acting piston actuator: uses "
                   "high-pressure plant air up to 150 psig, giving maximum thrust and fast stroking "
                   "in both directions, with pneumatic trip valves and lock-up systems available.",
                   "Van điều khiển với xi lanh piston tác động kép",
                   "Control valve with a double-acting piston cylinder")


@_reg
def fig_f3_47():
    """Figure 3.47 (p. 79) - Control Valve with Scotch-Yoke Piston Actuator."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(190, 58, 220, 150, fill="#f7f9fb", sw=1.6))
    o.append(_rect(196, 122, 208, 20, fill="#dfe7ef", sw=1.2))
    o.append(_line(300, 132, 300, 244, sw=2.6, color=INK))
    o.append(_rect(258, 244, 84, 44, fill="#eef3fb", sw=1.4))       # yoke
    o.append(_circle(300, 266, 12, fill="#fdf3e6", sw=1.3))
    o.append(_line(300, 266, 300, 292, sw=2.2, color=INK))
    o.append(_rect(226, 292, 148, 60, fill="#f4f7fb", sw=1.6))      # body
    o.append(_rect(164, 306, 64, 34, fill="#e9eef4", sw=1.3))
    o.append(_rect(150, 296, 18, 54, fill="#dfe7ef", sw=1.2))
    o.append(_rect(372, 306, 64, 34, fill="#e9eef4", sw=1.3))
    o.append(_rect(434, 296, 18, 54, fill="#dfe7ef", sw=1.2))
    o.append(_arrow(254, 88, 254, 118, sw=1.5, color=RED))
    o.append(_leader(410, 80, 462, 84))
    o.append(T(468, 88, "Cơ cấu kiểu Scotch-yoke", 7.4, anchor="start"))
    o.append(T(300, 380, "Chuyển chuyển động thẳng của piston sang chuyển động quay / Converts piston linear motion to rotary output",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.47 - Control valve with Scotch-Yoke piston actuator",
                   "Hình 3.47 (tr. 79) · Van điều khiển có cơ cấu piston Scotch-yoke",
                   "Hình 3.47 (tr. 79) · Van điều khiển có cơ cấu piston Scotch-yoke: chuyển chuyển "
                   "động thẳng của piston sang mô-men quay qua ách và chốt trượt, cho mô-men lớn ở "
                   "vị trí đầu và cuối hành trình của van quay.",
                   "Figure 3.47 (p. 79) · Control valve with Scotch-yoke piston actuator: converts "
                   "the piston's linear motion into rotary torque through a yoke and pin, delivering "
                   "high torque at the beginning and end of a rotary valve's travel.",
                   "Van điều khiển với cơ cấu piston và ách Scotch-yoke",
                   "Control valve with a piston and Scotch-yoke mechanism")


@_reg
def fig_f3_48():
    """Figure 3.48 (p. 79) - Manual Actuator for Sliding-Stem Valves."""
    w, h = 600, 400
    o = [_defs()]
    o.append(_circle(300, 92, 58, fill="#f7f9fb", sw=2.0))
    o.append(_circle(300, 92, 8, fill="#dfe7ef", sw=1.0))
    for i in range(8):
        import math as _m
        a = 2 * _m.pi * i / 8.0
        o.append(_line(300 + 50 * _m.cos(a), 92 + 50 * _m.sin(a),
                       300 + 64 * _m.cos(a), 92 + 64 * _m.sin(a),
                       sw=3.0, color=INK))
    o.append(_line(300, 150, 300, 268, sw=3.0, color=INK))
    o.append(_rect(272, 200, 56, 58, fill="#e9eef4", sw=1.4))       # yoke/nut
    o.append(_rect(240, 258, 120, 92, fill="#f4f7fb", sw=1.6))
    o.append(_rect(180, 280, 62, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(166, 270, 18, 62, fill="#dfe7ef", sw=1.2))
    o.append(_rect(358, 280, 62, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(418, 270, 18, 62, fill="#dfe7ef", sw=1.2))
    o.append(T(300, 376, "Vặn tay quay để định vị nút van / Handwheel positions the valve plug",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.48 - Manual actuator for sliding-stem valves",
                   "Hình 3.48 (tr. 79) · Cơ cấu chấp hành tay cho van thân trượt",
                   "Hình 3.48 (tr. 79) · Cơ cấu chấp hành tay cho van thân trượt: vặn tay quay qua "
                   "vít/đai ốc để định vị nút van; dùng khi không cần điều khiển tự động, có sẵn "
                   "cỡ cho van cầu và van quay, rẻ hơn nhiều cơ cấu tự động.",
                   "Figure 3.48 (p. 79) · Manual actuator for sliding-stem valves: a handwheel "
                   "positions the plug through a screw and nut; used where automatic control is not "
                   "required, available in sizes for globe and rotary valves and far less expensive "
                   "than automatic actuators.",
                   "Van thân trượt có tay quay và cơ cấu vít điều chỉnh",
                   "Sliding-stem valve with a handwheel and screw mechanism")


@_reg
def fig_f3_49():
    """Figure 3.49 (p. 79) - Manual Actuator for Rotary Valves."""
    w, h = 600, 380
    o = [_defs()]
    o.append(_circle(300, 96, 56, fill="#f7f9fb", sw=2.0))
    o.append(_circle(300, 96, 8, fill="#dfe7ef", sw=1.0))
    for i in range(8):
        import math as _m
        a = 2 * _m.pi * i / 8.0
        o.append(_line(300 + 48 * _m.cos(a), 96 + 48 * _m.sin(a),
                       300 + 62 * _m.cos(a), 96 + 62 * _m.sin(a),
                       sw=3.0, color=INK))
    o.append(_rect(268, 152, 64, 44, fill="#e9eef4", sw=1.4))
    o.append(_circle(300, 174, 12, fill="#fdf3e6", sw=1.3))         # gear
    o.append(_line(300, 196, 300, 240, sw=3.0, color=INK))
    o.append(_circle(300, 250, 20, fill="#fdf3e6", sw=1.4))
    o.append(_rect(240, 270, 120, 58, fill="#f4f7fb", sw=1.6))
    o.append(_rect(180, 284, 62, 32, fill="#e9eef4", sw=1.3))
    o.append(_rect(166, 274, 18, 52, fill="#dfe7ef", sw=1.2))
    o.append(_rect(358, 284, 62, 32, fill="#e9eef4", sw=1.3))
    o.append(_rect(418, 274, 18, 52, fill="#dfe7ef", sw=1.2))
    o.append(T(300, 354, "Tay quay qua bộ bánh răng quay trục van / Handwheel turns the shaft through gears",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.49 - Manual actuator for rotary valves",
                   "Hình 3.49 (tr. 79) · Cơ cấu chấp hành tay cho van quay",
                   "Hình 3.49 (tr. 79) · Cơ cấu chấp hành tay cho van quay: tay quay truyền qua bộ "
                   "bánh răng để quay trục van; một số kiểu có chỉ thị số để định vị lại chính xác "
                   "nút hoặc đĩa van.",
                   "Figure 3.49 (p. 79) · Manual actuator for rotary valves: a handwheel drives a "
                   "gear train that turns the valve shaft; some models offer dial indicators for "
                   "accurate repositioning of the plug or disc.",
                   "Van quay có tay quay và bộ bánh răng",
                   "Rotary valve with a handwheel and gear train")


@_reg
def fig_f3_50():
    """Figure 3.50 (p. 79) - Rack-and-Pinion Actuator."""
    w, h = 620, 356
    o = [_defs()]
    o.append(_rect(130, 96, 360, 148, fill="#f7f9fb", sw=1.6))
    o.append(_rect(150, 124, 320, 22, fill="#e9eef4", sw=1.2))
    o.append(_rect(150, 194, 320, 22, fill="#e9eef4", sw=1.2))
    for i in range(11):
        x = 168 + i * 28
        o.append(_line(x, 124, x + 10, 146, sw=1.2, color=INK))
        o.append(_line(x, 194, x + 10, 216, sw=1.2, color=INK))
    o.append(_circle(310, 170, 44, fill="#fdf3e6", sw=1.7))
    o.append(_circle(310, 170, 8, fill=BLUE, sw=0))
    o.append(_line(310, 170, 310, 274, sw=2.6, color=INK))
    o.append(_arrow(196, 170, 250, 170, sw=1.6, color=GREEN))
    o.append(T(310, 306, "Răng cưa đẩy bánh răng quay / Rack drives the pinion", 7.6, color=INK))
    o.append(T(310, 326, "Gọn, rẻ; thường dùng cho đóng mở / Compact and economical for on-off service",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.50 - Rack-and-pinion actuator",
                   "Hình 3.50 (tr. 79) · Cơ cấu chấp hành răng cưa - bánh răng",
                   "Hình 3.50 (tr. 79) · Cơ cấu răng cưa - bánh răng: giải pháp gọn và kinh tế cho "
                   "van quay. Do có độ hở răng, thường dùng cho ứng dụng đóng mở hoặc nơi biến thiên "
                   "quá trình không đáng lo ngại.",
                   "Figure 3.50 (p. 79) · Rack-and-pinion actuator: a compact, economical solution "
                   "for rotary valves; because of backlash it is typically used for on-off "
                   "applications or where process variability is not a concern.",
                   "Cơ cấu răng cưa truyền động cho bánh răng và trục van",
                   "Rack-and-pinion actuator driving a rotary shaft")


@_reg
def fig_f3_51():
    """Figure 3.51 (p. 80) - Electric Actuator for Sliding-Stem Valve."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(196, 62, 208, 122, fill="#eef3fb", sw=1.6))      # motor housing
    o.append(_circle(300, 122, 38, fill="#f7f9fb", sw=1.5))
    o.append(_circle(300, 122, 8, fill=BLUE, sw=0))
    o.append(_rect(250, 184, 100, 54, fill="#f4f7fb", sw=1.4))      # gear reduction
    o.append(_line(300, 238, 300, 300, sw=3.0, color=INK))
    o.append(_rect(268, 262, 64, 42, fill="#e9eef4", sw=1.3))
    o.append(_rect(228, 300, 144, 58, fill="#f4f7fb", sw=1.6))
    o.append(_rect(166, 314, 64, 32, fill="#e9eef4", sw=1.3))
    o.append(_rect(152, 304, 18, 52, fill="#dfe7ef", sw=1.2))
    o.append(_rect(370, 314, 64, 32, fill="#e9eef4", sw=1.3))
    o.append(_rect(432, 304, 18, 52, fill="#dfe7ef", sw=1.2))
    o.append(_leader(406, 92, 452, 84))
    o.append(T(460, 88, "Động cơ điện / Electric motor", 7.4, anchor="start"))
    o.append(_leader(352, 206, 452, 136))
    o.append(T(460, 140, "Giảm tốc / Gear reduction", 7.4, anchor="start"))
    o.append(T(300, 380, "Động cơ không chổi than giảm cháy khi đóng cắt nhanh / Brushless motors reduce burnout",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.51 - Electric actuator for sliding-stem valve",
                   "Hình 3.51 (tr. 80) · Cơ cấu chấp hành điện cho van thân trượt",
                   "Hình 3.51 (tr. 80) · Cơ cấu chấp hành điện cho van thân trượt: dùng động cơ điện "
                   "và bộ giảm tốc để dịch chuyển nút van; truyền thống chỉ đóng mở, nay có kiểu "
                   "điều khiển liên tục, đặc biệt nơi không có khí dụng cụ.",
                   "Figure 3.51 (p. 80) · Electric actuator for sliding-stem valves: an electric "
                   "motor and gear reduction move the plug; traditionally limited to on-off duty, "
                   "some now provide continuous control, especially where instrument air is scarce.",
                   "Van thân trượt có động cơ điện và bộ giảm tốc",
                   "Sliding-stem valve with electric motor and gearbox")


@_reg
def fig_f3_52():
    """Figure 3.52 (p. 80) - Electric Actuator for Rotary Valve."""
    w, h = 620, 396
    o = [_defs()]
    o.append(_rect(196, 62, 208, 118, fill="#eef3fb", sw=1.6))
    o.append(_circle(300, 120, 36, fill="#f7f9fb", sw=1.5))
    o.append(_circle(300, 120, 8, fill=BLUE, sw=0))
    o.append(_rect(250, 180, 100, 52, fill="#f4f7fb", sw=1.4))
    o.append(_line(300, 232, 300, 272, sw=3.0, color=INK))
    o.append(_circle(300, 282, 18, fill="#fdf3e6", sw=1.4))
    o.append(_rect(240, 300, 120, 44, fill="#f4f7fb", sw=1.6))
    o.append(_rect(180, 312, 62, 26, fill="#e9eef4", sw=1.3))
    o.append(_rect(166, 302, 18, 46, fill="#dfe7ef", sw=1.2))
    o.append(_rect(358, 312, 62, 26, fill="#e9eef4", sw=1.3))
    o.append(_rect(418, 302, 18, 46, fill="#dfe7ef", sw=1.2))
    o.append(_leader(406, 88, 452, 80))
    o.append(T(460, 84, "Động cơ / Motor", 7.4, anchor="start"))
    o.append(_leader(352, 204, 452, 130))
    o.append(T(460, 134, "Bộ giảm tốc / Gearbox", 7.4, anchor="start"))
    o.append(T(300, 364, "Đầu ra quay 90 độ cho van bi và van bướm / 90-degree rotary output for ball and butterfly valves",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 3.52 - Electric actuator for rotary valve",
                   "Hình 3.52 (tr. 80) · Cơ cấu chấp hành điện cho van quay",
                   "Hình 3.52 (tr. 80) · Cơ cấu chấp hành điện cho van quay: động cơ qua bộ giảm "
                   "tốc tạo đầu ra quay 90 độ cho van bi, van bướm; dùng ở nơi không sẵn khí dụng "
                   "cụ hoặc số lượng van quá ít để biện minh cho hệ thống máy nén.",
                   "Figure 3.52 (p. 80) · Electric actuator for rotary valves: a motor through a "
                   "gearbox provides 90-degree rotary output for ball and butterfly valves; used "
                   "where instrument air is unavailable or too few valves justify a compressor.",
                   "Van quay có động cơ điện và đầu ra quay 90 độ",
                   "Rotary valve with an electric motor and 90-degree output")

# ---------------------------------------------------------------------------
# Chapter 4 figures (4.1-4.27).  The source mis-numbers the solenoid-valve
# figures of section 4.10 as 14.14-14.23; here they are 4.14-4.23.
# Each redraws a source figure as a simplified vector schematic and returns
# the standard 5-tuple via _finish().
# ---------------------------------------------------------------------------

def _c4_box(x, y, w, h, label, size=8.2, fill="#eef3fb"):
    """Labelled block used by the Chapter 4 schematics."""
    return (_rect(x, y, w, h, fill, 1.3)
            + T(x + w / 2.0, y + h / 2.0 + size * 0.35, label, size, weight="600"))


def _c4_dia(cx, top, w=88, h=34):
    """Simplified diaphragm actuator: spring, diaphragm casing and stem."""
    o = [_rect(cx - w / 2, top, w, h, fill="#f4f7fb", sw=1.4),
         _ellipse(cx, top, w / 2, 8, fill="#e9eef4", sw=1.3),
         _line(cx, top + h, cx, top + h + 24, sw=2.6, color=INK),
         _spring(cx, top - 32, top - 2, width=20, turns=5),
         _rect(cx - 18, top - 40, 36, 8, fill="#dfe7ef", sw=1.2)]
    return "".join(o)


def _c4_sov(x, y, ports=3, size=36):
    """Two-square solenoid valve symbol with coil, return spring and ports."""
    o = [_rect(x, y, size, size, fill="#f4f7fb", sw=1.4),
         _rect(x + size, y, size, size, fill="#eef3fb", sw=1.4),
         _rect(x - 28, y + 7, 22, size - 14, fill="#fdf3e6", sw=1.2),
         T(x - 17, y + size / 2 + 3, "S", 9, weight="600"),
         _line(x - 6, y + size / 2, x, y + size / 2, sw=1)]
    zx = x + 2 * size + 3
    o.append(_poly([(zx, y + 5), (zx + 6, y + 11), (zx, y + 17),
                    (zx + 6, y + 23), (zx, y + 29), (zx + 6, y + 35)], sw=1.1))
    labs = ("1", "2", "3") if ports == 3 else ("1", "2", "3", "4")
    for bx in (x, x + size):
        for i, lab in enumerate(labs):
            px = bx + 5 + i * (size - 10) / (len(labs) - 1.0)
            o.append(_line(px, y + size, px, y + size + 8, sw=1))
            o.append(T(px, y + size + 17, lab, 7.4))
    return "".join(o)


def _c4_handwheel(cx, cy, r):
    """A handwheel rim with six spokes and a hub."""
    o = [_circle(cx, cy, r, fill="#fdf3e6", sw=2.2)]
    for a in range(0, 360, 60):
        rad = math.radians(a)
        o.append(_line(cx, cy, cx + r * math.cos(rad),
                       cy + r * math.sin(rad), sw=1.4))
    o.append(_circle(cx, cy, 6, fill=BLUE, sw=0))
    return "".join(o)


def _c4_labels(items, x, y, lh=14, size=7.4):
    """Legend column for pre-joined 'VI / EN' label strings."""
    return "".join(_circle(x, y + i * lh - 2.5, 1.8, fill=BLUE, sw=0)
                   + T(x + 9, y + i * lh, s, size, anchor="start")
                   for i, s in enumerate(items))


def _c4_mounted(cx, top, label, sub=""):
    """A positioner/controller housing mounted on a sliding-stem valve."""
    o = [_rect(cx - 48, top, 96, 56, fill="#eef3fb", sw=1.5),
         T(cx, top + 25, label, 8.4, weight="600")]
    if sub:
        o.append(T(cx, top + 41, sub, 7.4, color=GREY))
    o.append(_line(cx, top + 56, cx, top + 88, sw=3, color=INK))
    o.append(_c4_dia(cx, top + 88, w=78, h=28))
    o.append(_bbody(cx, top + 150, bw=126, bh=72))
    return "".join(o)


@_reg
def fig_f4_01():
    """Figure 4.1 (p. 84) - Typical Pneumatic, Single-Acting Positioner."""
    w, h = 660, 440
    o = [_defs()]
    o.append(_c4_box(40, 40, 100, 34, "Supply / Cấp khí", size=8.4))
    o.append(_rect(56, 124, 64, 36, fill="#f7f9fb", sw=1.3))
    o.append(T(88, 146, "In / Đầu vào", 7.8))
    o.append(_poly([(110, 170), (430, 132)], sw=3.0, color=INK))
    o.append(_circle(184, 159, 6, fill="#fdf3e6", sw=1.4))
    o.append(T(184, 180, "Input axis", 7.2, color=GREY))
    o.append(_circle(330, 146, 6, fill="#fdf3e6", sw=1.4))
    o.append(T(330, 167, "Feedback axis", 7.2, color=GREY))
    o.append(_ellipse(330, 180, 30, 10, fill="#dfe7ef", sw=1.2))
    o.append(_line(430, 114, 430, 156, sw=2.2, color=RED))
    o.append(_rect(438, 130, 14, 18, fill="#eef3fb", sw=1.3))
    o.append(_c4_box(486, 84, 126, 42, "Relay / Rơ-le", size=8.4))
    o.append(_arrow(140, 57, 490, 100, sw=1.3, color=GREEN))
    o.append(_arrow(452, 139, 490, 120, sw=1.3, color=BLUE))
    o.append(_arrow(549, 126, 549, 188, sw=1.6, color=BLUE))
    o.append(_c4_dia(549, 192, w=82, h=30))
    o.append(_c4_box(476, 286, 146, 46, "Output to diaphragm / Đầu ra tới màng", size=7.6))
    o.append(_arrow(549, 246, 549, 286, sw=1.6, color=INK))
    o.append(_path("M 476 312 C 404 312 364 252 330 190", sw=1.0, dash="4 3", color=GREY))
    o.append(_path("M 150 132 A 40 40 0 0 1 190 172", sw=1.0, dash="3 3", color=GREY))
    o.append(_path("M 300 112 A 44 44 0 0 1 344 156", sw=1.0, dash="3 3", color=GREY))
    o.append(_c4_labels(["Ống mềm tín hiệu / Instrument bellows",
                         "Trục đầu vào / Input axis",
                         "Thanh đòn / Beam",
                         "Cam / Feedback cam",
                         "Trục phản hồi / Feedback axis"], 44, 350, lh=15))
    o.append(_c4_labels(["Cánh chắn / Flapper",
                         "Vòi phun / Nozzle",
                         "Rơ-le khuếch đại / Amplifier relay",
                         "Đầu ra tới màng / Output to diaphragm",
                         "Cấp khí / Supply"], 356, 350, lh=15))
    return _finish(w, h, o, "Figure 4.1 - Typical pneumatic single-acting positioner",
                   "Hình 4.1 (tr. 84) · Bộ định vị khí nén, tác động đơn điển hình",
                   "Hình 4.1 (tr. 84) · Bộ định vị khí nén, tác động đơn điển hình: tín hiệu vào "
                   "làm ống mềm đẩy thanh đòn quanh trục đầu vào, cánh chắn tiến gần vòi phun; "
                   "rơ-le tăng áp suất đầu ra tới màng và chuyển động thân van được cam phản hồi "
                   "về thanh đòn cho tới khi cân bằng.",
                   "Figure 4.1 (p. 84) · Typical pneumatic, single-acting positioner: the input "
                   "signal expands a bellows that pivots a beam about the input axis, moving a "
                   "flapper toward the nozzle; a relay raises actuator output pressure while a "
                   "cam feeds stem motion back until equilibrium is reached.",
                   "Sơ đồ bộ định vị khí nén với ống mềm, thanh đòn, cam và cánh chắn",
                   "Pneumatic positioner diagram with bellows, beam, cam and flapper")


@_reg
def fig_f4_02():
    """Figure 4.2 (p. 85) - Typical Single-Acting Analog I/P Positioner."""
    w, h = 660, 440
    o = [_defs()]
    o.append(_c4_box(34, 56, 116, 40, "4-20 mA DC / Input", size=8.2))
    o.append(_c4_box(180, 56, 124, 40, "I/P Converter / Bộ chuyển đổi", size=8.0))
    o.append(_arrow(150, 76, 180, 76, sw=1.6, color=GREEN))
    o.append(_arrow(304, 76, 360, 76, sw=1.6, color=GREEN))
    o.append(T(334, 68, "Pneumatic", 7.0, color=GREY))
    o.append(_rect(360, 60, 58, 32, fill="#f7f9fb", sw=1.3))
    o.append(T(389, 80, "Bellows", 7.6))
    o.append(_poly([(412, 132), (520, 112)], sw=3.0, color=INK))
    o.append(_circle(452, 124, 6, fill="#fdf3e6", sw=1.4))
    o.append(_ellipse(452, 152, 26, 9, fill="#dfe7ef", sw=1.2))
    o.append(_line(520, 96, 520, 136, sw=2.2, color=RED))
    o.append(_rect(528, 110, 12, 18, fill="#eef3fb", sw=1.3))
    o.append(_c4_box(424, 178, 120, 38, "Relay / Rơ-le", size=8.2))
    o.append(_arrow(534, 119, 486, 178, sw=1.3, color=BLUE))
    o.append(_arrow(484, 216, 484, 254, sw=1.6, color=BLUE))
    o.append(_c4_dia(484, 258, w=80, h=28))
    o.append(_c4_box(410, 320, 150, 44, "Actuator stem / Thân cơ cấu", size=7.8))
    o.append(_arrow(484, 310, 484, 320, sw=1.6))
    o.append(_path("M 410 342 C 356 342 330 240 452 160", sw=1.0, dash="4 3", color=GREY))
    o.append(_c4_box(40, 180, 136, 38, "Supply / Cấp khí", size=8.2))
    o.append(_arrow(176, 199, 424, 199, sw=1.2, color=GREEN))
    o.append(_c4_labels(["Đầu vào 4-20 mA / DC input",
                         "Bộ chuyển đổi I/P / I/P converter",
                         "Tín hiệu khí nén / Pneumatic signal",
                         "Cánh chắn / Flapper",
                         "Vòi phun / Nozzle"], 40, 376, lh=13))
    o.append(_c4_labels(["Ống mềm / Bellows",
                         "Thanh đòn / Beam",
                         "Cam / Cam",
                         "Rơ-le / Relay",
                         "Đầu ra tới cơ cấu / Output to actuator"], 350, 376, lh=13))
    return _finish(w, h, o, "Figure 4.2 - Typical single-acting analog I/P positioner",
                   "Hình 4.2 (tr. 85) · Bộ định vị I/P tương tự, tác động đơn",
                   "Hình 4.2 (tr. 85) · Bộ định vị I/P tương tự, tác động đơn: tín hiệu 4-20 mA được "
                   "đổi thành áp suất khí nén tỷ lệ, rồi điều khiển cụm cánh chắn-vòi phun và rơ-le "
                   "như bộ định vị khí nén; ống mềm nhận tín hiệu khí nén từ bộ chuyển đổi.",
                   "Figure 4.2 (p. 85) · Typical single-acting analog I/P positioner: a 4-20 mA "
                   "signal is converted to a proportional pneumatic pressure that drives the "
                   "nozzle/flapper and relay much as in a pneumatic positioner; the bellows "
                   "receives the converter's pneumatic output.",
                   "Sơ đồ bộ định vị I/P tương tự với bộ chuyển đổi và cánh chắn",
                   "Analog I/P positioner diagram with converter and flapper")


@_reg
def fig_f4_03():
    """Figure 4.3 (p. 85) - I/P Positioner."""
    w, h = 620, 350
    o = [_defs()]
    o.append(_rect(196, 64, 228, 150, fill="#eef3fb", sw=1.8))
    o.append(_rect(214, 84, 96, 74, fill="#f7f9fb", sw=1.3))
    o.append(T(262, 126, "I/P", 16, weight="600", color=BLUE))
    o.append(_circle(382, 118, 28, fill="#fdf3e6", sw=1.5))
    o.append(_circle(382, 118, 20, fill="#ffffff", sw=1.0))
    o.append(_line(382, 118, 396, 106, sw=2, color=RED))
    o.append(T(382, 160, "Gauge / Đồng hồ", 7.6, color=GREY))
    o.append(_rect(240, 214, 140, 26, fill="#dfe7ef", sw=1.3))
    o.append(T(310, 231, "Mounting bracket / Giá lắp", 7.6))
    o.append(_line(310, 240, 310, 278, sw=3, color=INK))
    o.append(_leader(214, 150, 112, 196))
    o.append(T(108, 200, "4-20 mA input / Đầu vào", 7.6, anchor="end"))
    o.append(_leader(424, 150, 500, 196))
    o.append(T(504, 200, "Pneumatic output / Đầu ra khí", 7.6, anchor="start"))
    o.append(T(310, 312, "Thiết bị điện-khí nén tích hợp trên thân van / Integral electro-pneumatic device",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 4.3 - I/P positioner",
                   "Hình 4.3 (tr. 85) · Bộ định vị I/P",
                   "Hình 4.3 (tr. 85) · Bộ định vị I/P: vỏ thiết bị có đầu vào dòng 4-20 mA, đồng hồ "
                   "áp suất và đầu ra khí nén, lắp trực tiếp lên cụm van điều khiển.",
                   "Figure 4.3 (p. 85) · I/P positioner: a housing with 4-20 mA input, pressure "
                   "gauge and pneumatic output, mounted directly on the control valve assembly.",
                   "Bộ định vị I/P có đồng hồ áp suất và giá lắp",
                   "I/P positioner with pressure gauge and mounting bracket")


@_reg
def fig_f4_04():
    """Figure 4.4 (p. 86) - Digital Valve Controller Mounted on a Control Valve."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(188, 46, 244, 112, fill="#eef3fb", sw=1.8))
    o.append(T(310, 74, "Digital Valve Controller", 9.2, weight="600"))
    o.append(T(310, 94, "Bộ điều khiển van số / DVC", 8.0, color=GREY))
    o.append(_circle(228, 132, 14, fill="#fdf3e6", sw=1.2))
    o.append(_circle(264, 132, 14, fill="#fdf3e6", sw=1.2))
    o.append(_rect(330, 116, 78, 32, fill="#f7f9fb", sw=1.2))
    o.append(T(369, 136, "µP / Vi xử lý", 7.6))
    o.append(_line(310, 158, 310, 186, sw=3, color=INK))
    o.append(_c4_dia(310, 190, w=84, h=30))
    o.append(_arrow(346, 220, 420, 220, sw=1.4, color=BLUE))
    o.append(_arrow(274, 220, 200, 220, sw=1.4, color=BLUE))
    o.append(T(430, 224, "Out 1", 7.4, anchor="start", color=BLUE))
    o.append(T(190, 224, "Out 2", 7.4, anchor="end", color=BLUE))
    o.append(_bbody(310, 254, bw=130, bh=74))
    o.append(_leader(432, 90, 520, 84))
    o.append(T(524, 88, "HART / Fieldbus / Wireless", 7.4, anchor="start"))
    o.append(T(310, 366, "Phản hồi không liên kết, chẩn đoán và truyền thông hai chiều / Linkage-less feedback, diagnostics and two-way communication",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.4 - Digital valve controller on a control valve",
                   "Hình 4.4 (tr. 86) · Bộ điều khiển van số lắp trên van điều khiển",
                   "Hình 4.4 (tr. 86) · Bộ điều khiển van số lắp trên van điều khiển: vi xử lý đọc tín "
                   "hiểu, điều khiển I/P và cấp hai áp suất đầu ra cho cơ cấu chấp hành; phản hồi "
                   "không liên kết, chẩn đoán và truyền thông HART, fieldbus hoặc không dây.",
                   "Figure 4.4 (p. 86) · Digital valve controller mounted on a control valve: the "
                   "microprocessor reads the signal, drives the I/P converter and supplies two "
                   "output pressures to the actuator, with linkage-less feedback, diagnostics and "
                   "HART, fieldbus or wireless communication.",
                   "Bộ điều khiển van số trên cơ cấu màng và thân van",
                   "Digital valve controller on a diaphragm actuator and valve body")


@_reg
def fig_f4_05():
    """Figure 4.5 (p. 87) - Detail of Deflector / Nozzle Pilot Stage."""
    w, h = 640, 330
    o = [_defs()]
    o.append(_rect(120, 92, 150, 46, fill="#eef3fb", sw=1.5))
    o.append(T(195, 120, "Supply nozzle / Vòi cấp", 8.0))
    o.append(_rect(370, 92, 150, 46, fill="#eef3fb", sw=1.5))
    o.append(T(445, 120, "Receiver / Vòi nhận", 8.0))
    o.append(_poly([(270, 108), (370, 108)], sw=1.2, color=GREEN))
    o.append(_poly([(270, 122), (370, 122)], sw=1.2, color=GREEN))
    o.append(_arrow(272, 115, 364, 115, sw=1.6, color=GREEN))
    o.append(_line(320, 80, 320, 152, sw=4, color=RED))
    o.append(_circle(320, 78, 5, fill=RED, sw=0))
    o.append(_leader(320, 78, 320, 48))
    o.append(T(320, 44, "Deflector bar / Thanh chắn", 7.8))
    o.append(_arrow(520, 115, 592, 115, sw=1.8, color=BLUE))
    o.append(T(592, 108, "Pilot pressure", 7.4, anchor="end", color=BLUE))
    o.append(_leader(232, 138, 196, 196))
    o.append(T(196, 212, "Constant air flow / Dòng khí không đổi", 7.6, anchor="end"))
    o.append(_leader(445, 138, 470, 196))
    o.append(T(474, 212, "To booster stage / Tới cấp khuếch đại", 7.6, anchor="start"))
    o.append(T(320, 282, "Tín hiệu dòng định vị thanh chắn, làm đổi dòng tới vòi nhận / Input current positions the deflector in the flow stream",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.5 - Deflector / nozzle pilot stage detail",
                   "Hình 4.5 (tr. 87) · Chi tiết cấp thử thanh chắn / vòi phun",
                   "Hình 4.5 (tr. 87) · Chi tiết cấp thử thanh chắn/vòi phun: dòng khí không đổi từ "
                   "vòi cấp hướng vào vòi nhận; thanh chắn do tín hiệu dòng điều khiển làm đổi dòng, "
                   "thiết lập áp suất thử điều khiển cấp khuếch đại.",
                   "Figure 4.5 (p. 87) · Detail of the deflector/nozzle pilot stage: constant flow "
                   "from the supply nozzle is aimed at the receiver nozzle; a current-positioned "
                   "deflector alters the stream and sets the pilot pressure for the booster stage.",
                   "Cặp vòi phun với thanh chắn ở giữa dòng khí",
                   "Paired nozzles with a deflector bar in the air stream")


@_reg
def fig_f4_06():
    """Figure 4.6 (p. 88) - Transducer Mounted on a Control Valve."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(206, 56, 208, 96, fill="#eef3fb", sw=1.8))
    o.append(T(310, 84, "I/P Transducer", 9.0, weight="600"))
    o.append(T(310, 104, "Bộ chuyển đổi I/P", 7.8, color=GREY))
    o.append(_rect(232, 122, 156, 20, fill="#f7f9fb", sw=1.2))
    o.append(T(310, 136, "Converter + booster relay", 7.2))
    o.append(_line(310, 152, 310, 182, sw=3, color=INK))
    o.append(_c4_dia(310, 186, w=82, h=28))
    o.append(_bbody(310, 250, bw=128, bh=72))
    o.append(_leader(206, 96, 116, 92))
    o.append(T(112, 96, "4-20 mA in", 7.6, anchor="end"))
    o.append(_leader(414, 96, 506, 92))
    o.append(T(510, 96, "No feedback", 7.6, anchor="start"))
    o.append(T(310, 356, "Đáp ứng rất nhanh, không có phản hồi vị trí van / Very fast response with no valve position feedback",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 4.6 - Transducer mounted on a control valve",
                   "Hình 4.6 (tr. 88) · Bộ chuyển đổi lắp trên van điều khiển",
                   "Hình 4.6 (tr. 88) · Bộ chuyển đổi I/P lắp trên van điều khiển: mô-đun đổi dòng "
                   "4-20 mA thành áp suất tỷ lệ, rơ-le khuếch đại bên trong cấp khí cho cơ cấu chấp "
                   "hành; không có phản hồi vị trí nên đáp ứng rất nhanh.",
                   "Figure 4.6 (p. 88) · Transducer mounted on a control valve: a module converts "
                   "4-20 mA into proportional pressure and an internal amplifier relay supplies "
                   "the actuator; with no position feedback, response is very quick.",
                   "Bộ chuyển đổi I/P lắp trên cơ cấu chấp hành",
                   "I/P transducer mounted on an actuator")


@_reg
def fig_f4_07():
    """Figure 4.7 (p. 88) - Volume Booster Sectional View."""
    w, h = 660, 420
    o = [_defs()]
    o.append(_rect(150, 96, 360, 190, fill="#f4f7fb", sw=1.8))
    o.append(_rect(150, 104, 168, 78, fill="#ffffff", sw=1.3))
    o.append(_rect(318, 104, 192, 78, fill="#ffffff", sw=1.3))
    o.append(_ellipse(234, 143, 60, 22, fill="#e9eef4", sw=1.3))
    o.append(_ellipse(414, 143, 62, 22, fill="#e9eef4", sw=1.3))
    o.append(_line(234, 165, 234, 210, sw=2, color=INK))
    o.append(_line(414, 165, 414, 210, sw=2, color=INK))
    o.append(_rect(206, 210, 56, 22, fill="#fdf3e6", sw=1.3))
    o.append(_rect(388, 210, 56, 22, fill="#fdf3e6", sw=1.3))
    o.append(_line(150, 221, 66, 221, sw=4, color=GREEN))
    o.append(T(66, 214, "Supply / Cấp", 7.6, anchor="start", color=GREEN))
    o.append(_line(510, 221, 596, 221, sw=4, color=BLUE))
    o.append(T(596, 214, "Output / Đầu ra", 7.6, anchor="end", color=BLUE))
    o.append(_line(150, 268, 66, 268, sw=3, color=RED))
    o.append(T(66, 284, "Exhaust / Xả", 7.6, anchor="start", color=RED))
    o.append(_line(330, 286, 330, 326, sw=1.6, color=GREY))
    o.append(_rect(306, 326, 48, 20, fill="#eef3fb", sw=1.2))
    o.append(T(330, 340, "Signal in", 7.0))
    o.append(_rect(196, 70, 76, 24, fill="#eef3fb", sw=1.2))
    o.append(T(234, 86, "Bypass + screw", 7.0))
    o.append(_line(234, 94, 234, 104, sw=1.0, dash="3 3"))
    o.append(_leader(234, 143, 96, 152))
    o.append(T(92, 156, "Diaphragms / Màng", 7.4, anchor="end"))
    o.append(_c4_labels(["Cổng cấp / Supply port",
                         "Cổng xả / Exhaust port",
                         "Màng / Diaphragms",
                         "Tiết lưu bypass / Bypass restriction"], 60, 362, lh=13))
    o.append(_c4_labels(["Vít chỉnh / Adjusting screw",
                         "Đầu ra tới cơ cấu / Output to actuator",
                         "Tín hiệu vào / Signal input",
                         "Vùng chết cố định / Fixed deadband"], 350, 362, lh=13))
    return _finish(w, h, o, "Figure 4.7 - Volume booster sectional view",
                   "Hình 4.7 (tr. 88) · Mặt cắt bộ tăng thể tích",
                   "Hình 4.7 (tr. 88) · Mặt cắt bộ tăng thể tích: chênh áp giữa tín hiệu vào và đầu "
                   "ra làm màng dịch chuyển, mở cổng cấp hoặc cổng xả cho tới khi chênh áp nằm trong "
                   "vùng chết; tiết lưu bypass và vít chỉnh cho tín hiệu nhỏ đi thẳng qua.",
                   "Figure 4.7 (p. 88) · Volume booster sectional view: a differential between "
                   "signal and output moves the diaphragms to open the supply or exhaust port "
                   "until the difference is within the deadband; a bypass restriction and "
                   "adjusting screw let small signals pass through.",
                   "Mặt cắt bộ tăng thể tích với hai màng và cổng cấp, xả",
                   "Sectioned volume booster with two diaphragms and supply and exhaust ports")


@_reg
def fig_f4_08():
    """Figure 4.8 (p. 89) - Typical Boosters Installation, Double-Acting Actuator."""
    w, h = 660, 390
    o = [_defs()]
    o.append(_c4_box(36, 48, 128, 42, "Positioner / Bộ định vị", size=8.2))
    o.append(_c4_box(224, 48, 100, 42, "Booster 1", size=8.4))
    o.append(_c4_box(352, 48, 100, 42, "Booster 2", size=8.4))
    o.append(_arrow(164, 69, 224, 69, sw=1.4, color=GREEN))
    o.append(_arrow(324, 69, 352, 69, sw=1.4, color=GREEN))
    o.append(_line(274, 90, 274, 132, sw=2, color=BLUE))
    o.append(_line(402, 90, 402, 150, sw=2, color=BLUE))
    o.append(_rect(250, 132, 360, 176, fill="#f4f7fb", sw=1.8))
    o.append(_rect(272, 148, 316, 52, fill="#e9eef4", sw=1.4))
    o.append(T(430, 178, "Upper cylinder / Xi lanh trên", 8.0))
    o.append(_rect(272, 216, 316, 52, fill="#e9eef4", sw=1.4))
    o.append(T(430, 246, "Lower cylinder / Xi lanh dưới", 8.0))
    o.append(_line(430, 200, 430, 216, sw=4, color=INK))
    o.append(_line(430, 308, 430, 336, sw=3, color=INK))
    o.append(_bbody(430, 336, bw=120, bh=44))
    o.append(T(274, 282, "Piston / Piston", 7.6, color=GREY))
    o.append(T(330, 364, "Ít nhất hai bộ tăng, một cho mỗi phía piston / At least two boosters, one per piston side",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 4.8 - Typical boosters installation with double-acting actuator",
                   "Hình 4.8 (tr. 89) · Bố trí bộ tăng điển hình với cơ cấu tác động kép",
                   "Hình 4.8 (tr. 89) · Bố trí bộ tăng điển hình với cơ cấu tác động kép: hai bộ tăng "
                   "nhận đầu ra từ bộ định vị và cấp khí riêng cho xi lanh trên và xi lanh dưới, "
                   "đẩy piston và thân van nhanh hơn.",
                   "Figure 4.8 (p. 89) · Typical boosters installation with a double-acting "
                   "actuator: two boosters take the positioner output and feed the upper and lower "
                   "cylinders separately for faster piston and stem movement.",
                   "Hai bộ tăng cấp khí cho xi lanh trên và dưới",
                   "Two boosters feeding the upper and lower actuator cylinders")


@_reg
def fig_f4_09():
    """Figure 4.9 (p. 89) - SIS Digital Valve Controller on a Safety Valve."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_c4_box(30, 52, 132, 44, "Logic solver / Bộ giải logic", size=7.8))
    o.append(_arrow(162, 74, 218, 74, sw=1.5, color=GREEN))
    o.append(_c4_box(218, 52, 146, 44, "DVC + SOV", size=8.6))
    o.append(_line(291, 96, 291, 130, sw=3, color=INK))
    o.append(_c4_dia(291, 134, w=90, h=34))
    o.append(_line(291, 192, 291, 222, sw=3, color=INK))
    o.append(_bbody(291, 222, bw=132, bh=76))
    o.append(_leader(364, 74, 458, 68))
    o.append(T(462, 72, "Emergency vent / block", 7.4, anchor="start"))
    o.append(_leader(364, 152, 458, 140))
    o.append(T(462, 144, "Spring-return fail mode", 7.4, anchor="start"))
    o.append(_c4_box(180, 330, 260, 40, "Safe state on demand / Trạng thái an toàn khi có yêu cầu", size=7.8))
    o.append(_arrow(291, 298, 291, 330, sw=1.2, dash="4 3", color=GREY))
    return _finish(w, h, o, "Figure 4.9 - SIS digital valve controller on a safety valve",
                   "Hình 4.9 (tr. 89) · Bộ điều khiển van số SIS trên van an toàn",
                   "Hình 4.9 (tr. 89) · Bộ điều khiển van số SIS trên van an toàn: bộ giải logic điều "
                   "khiển DVC và van điện từ; cơ cấu hồi vị lò xo đưa van về trạng thái an toàn khi "
                   "có yêu cầu ngắt khẩn cấp.",
                   "Figure 4.9 (p. 89) · SIS digital valve controller on a safety valve: a logic "
                   "solver commands the DVC and solenoid valve, while a spring-return actuator "
                   "drives the valve to its safe state on an emergency demand.",
                   "Van an toàn do DVC và van điện từ điều khiển",
                   "Safety valve controlled by a DVC and solenoid valve")


@_reg
def fig_f4_10():
    """Figure 4.10 (p. 90) - Pneumatic Controller on a Control Valve."""
    w, h = 620, 400
    o = [_defs()]
    o.append(_rect(170, 50, 280, 130, fill="#eef3fb", sw=1.8))
    o.append(T(310, 76, "Pneumatic Controller / Bộ điều khiển khí nén", 8.6, weight="600"))
    o.append(_circle(222, 134, 26, fill="#fdf3e6", sw=1.4))
    o.append(_path("M 208 134 A 14 14 0 1 1 236 134 A 14 14 0 1 1 208 134", sw=1.2))
    o.append(T(222, 174, "Bourdon tube", 7.2, color=GREY))
    o.append(_circle(310, 130, 16, fill="#f7f9fb", sw=1.3))
    o.append(T(310, 166, "Set point / Điểm đặt", 7.2, color=GREY))
    o.append(_rect(376, 112, 56, 36, fill="#f7f9fb", sw=1.2))
    o.append(T(404, 134, "Relay", 7.6))
    o.append(_line(310, 180, 310, 210, sw=3, color=INK))
    o.append(_c4_dia(310, 214, w=82, h=28))
    o.append(_bbody(310, 278, bw=130, bh=72))
    o.append(_leader(170, 104, 96, 96))
    o.append(T(92, 100, "Process input / Đầu vào quá trình", 7.4, anchor="end"))
    o.append(_leader(432, 130, 498, 124))
    o.append(T(502, 128, "Pneumatic output", 7.4, anchor="start"))
    o.append(T(310, 372, "Đo tại chỗ và trực tiếp dẫn áp suất tới van / Measures locally and drives valve pressure directly",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.10 - Pneumatic controller on a control valve",
                   "Hình 4.10 (tr. 90) · Bộ điều khiển khí nén lắp trên van điều khiển",
                   "Hình 4.10 (tr. 90) · Bộ điều khiển khí nén lắp trên van điều khiển: phần tử đầu "
                   "vào (ví dụ ống Bourdon) đo áp suất, nhiệt độ hoặc mức tại chỗ và trực tiếp dẫn "
                   "áp suất khí nén đầu ra tới cơ cấu chấp hành.",
                   "Figure 4.10 (p. 90) · Pneumatic controller on a control valve: an input element "
                   "such as a Bourdon tube measures pressure, temperature or level locally and "
                   "directly drives pneumatic output pressure to the actuator.",
                   "Bộ điều khiển khí nén có ống Bourdon lắp trên van",
                   "Pneumatic controller with Bourdon tube mounted on a valve")


def _c4_ctrl(o, cx, reset=False, rate=False):
    """Shared beam-flapper pneumatic controller schematic."""
    o.append(_rect(64, 92, 132, 74, fill="#f7f9fb", sw=1.4))
    o.append(T(130, 122, "Input element", 8.2, weight="600"))
    o.append(T(130, 143, "Bourdon / bellows", 7.2, color=GREY))
    o.append(_path("M 92 152 A 22 22 0 0 1 136 152", sw=1.2))
    o.append(_circle(130, 78, 13, fill="#fdf3e6", sw=1.3))
    o.append(T(130, 82, "SP", 7.4))
    o.append(T(130, 60, "Set point", 7.2, color=GREY))
    o.append(_line(196, 128, 258, 170, sw=1.2, color=GREY))
    o.append(_poly([(250, 206), (478, 182)], sw=3.0, color=INK))
    o.append(_circle(330, 197, 6, fill="#fdf3e6", sw=1.4))
    o.append(T(330, 218, "Flapper pivot", 7.0, color=GREY))
    o.append(_line(478, 166, 478, 206, sw=2.4, color=RED))
    o.append(_rect(486, 178, 14, 20, fill="#eef3fb", sw=1.3))
    o.append(_c4_box(518, 120, 126, 40, "Relay / Rơ-le", size=8.2))
    o.append(_arrow(500, 188, 522, 152, sw=1.3, color=BLUE))
    o.append(_rect(300, 240, 66, 22, fill="#fdf3e6", sw=1.2))
    o.append(T(333, 254, "Proportional bellows", 6.8))
    if reset:
        o.append(_rect(212, 240, 66, 22, fill="#eef3fb", sw=1.2))
        o.append(T(245, 254, "Reset bellows", 7.0))
        o.append(T(245, 274, "vented / thông hơi", 6.6, color=GREY))
    if rate:
        o.append(_rect(390, 240, 56, 22, fill="#eef3fb", sw=1.2))
        o.append(T(418, 254, "Rate valve", 7.2))
        o.append(_rect(458, 240, 56, 22, fill="#eef3fb", sw=1.2))
        o.append(T(486, 254, "Relief", 7.2))
    o.append(_path("M 518 160 C 560 160 580 300 366 300 C 340 300 336 270 333 262",
                   sw=1.0, dash="4 3", color=GREY))
    o.append(_arrow(581, 140, 581, 190, sw=1.5, color=BLUE))
    o.append(T(585, 196, "To final control", 7.0, anchor="end", color=BLUE))
    o.append(_line(64, 178, 64, 214, sw=1.3, color=GREEN))
    o.append(T(64, 226, "Supply", 7.0, color=GREEN))
    o.append(_path("M 150 206 A 34 34 0 0 1 184 240", sw=1.0, dash="3 3", color=GREY))
    o.append(_path("M 300 178 A 34 34 0 0 1 334 212", sw=1.0, dash="3 3", color=GREY))
    o.append(_leader(130, 92, 130, 46))
    o.append(T(130, 42, "Process pointer / Kim quá trình", 7.2))
    o.append(T(300, 318, "Đường nét đứt: phản hồi đầu ra / Dashed line: output feedback", 7.0, color=GREY))
    return o


@_reg
def fig_f4_11():
    """Figure 4.11 (p. 91) - Pneumatic Controller Schematic, proportional-only."""
    w, h = 680, 450
    o = [_defs()]
    o = _c4_ctrl(o, 330, reset=False, rate=False)
    o.append(_c4_labels(["Kim quá trình / Process pointer",
                         "Phần tử đầu vào / Input element",
                         "Liên kết / Connecting link",
                         "Áp suất cấp / Supply pressure",
                         "Cánh chắn / Flapper",
                         "Vòi phun / Nozzle",
                        "Beam / Thanh đòn"], 44, 344, lh=14))
    o.append(_c4_labels(["Rơ-le / Relay",
                         "Áp suất vòi phun / Nozzle pressure",
                         "Ống mềm tỷ lệ / Proportional bellows",
                         "Dải tỷ lệ / Proportional band",
                         "Đầu ra tới phần tử cuối / Output to final element",
                         "Tác động trực tiếp / Direct action",
                         "Tác động ngược / Reverse action"], 356, 344, lh=14))
    return _finish(w, h, o, "Figure 4.11 - Pneumatic controller schematic, proportional-only",
                   "Hình 4.11 (tr. 91) · Sơ đồ bộ điều khiển khí nén (chỉ tỷ lệ)",
                   "Hình 4.11 (tr. 91) · Sơ đồ bộ điều khiển khí nén — <i>Pneumatic Controller "
                   "Schematic</i> trong nguyên bản — dạng chỉ tỷ lệ (proportional-only): đầu vào "
                   "dời cánh chắn, áp suất vòi phun tác động lên rơ-le và ống mềm tỷ lệ phản hồi "
                   "để đạt cân bằng; núm dải tỷ lệ định vị vòi phun trên cánh chắn.",
                   "Figure 4.11 (p. 91) · Pneumatic controller schematic (also captioned "
                   "<i>Pneumatic Controller Schematic</i> in the source), proportional-only: input "
                   "moves the flapper, nozzle pressure acts on the relay and a proportional "
                   "bellows feeds output back to equilibrium; the band knob positions the nozzle.",
                   "Sơ đồ bộ điều khiển khí nén chỉ tỷ lệ",
                   "Pneumatic controller schematic, proportional-only control")


@_reg
def fig_f4_12():
    """Figure 4.12 (p. 92) - Pneumatic Controller Schematic, PID."""
    w, h = 680, 450
    o = [_defs()]
    o = _c4_ctrl(o, 330, reset=True, rate=True)
    o.append(_c4_labels(["Ống mềm tích phân / Reset bellows",
                         "Ống mềm tỷ lệ / Proportional bellows",
                         "Van tốc độ / Rate valve",
                         "Van xả chênh áp / Differential relief",
                         "Áp suất tích phân / Reset pressure",
                        "Phản hồi / Feedback link"], 44, 344, lh=14))
    o.append(_c4_labels(["Cánh chắn / Flapper",
                         "Vòi phun / Nozzle",
                         "Rơ-le / Relay",
                         "Áp suất đầu ra / Output pressure",
                         "Tác động tỷ lệ + tích phân + vi phân",
                        "Proportional + reset + rate"], 356, 344, lh=14))
    return _finish(w, h, o, "Figure 4.12 - Pneumatic controller schematic, PID",
                   "Hình 4.12 (tr. 92) · Sơ đồ bộ điều khiển khí nén (tỷ lệ + tích phân + vi phân)",
                   "Hình 4.12 (tr. 92) · Sơ đồ bộ điều khiển khí nén — cùng mang chú thích "
                   "<i>Pneumatic Controller Schematic</i> như Hình 4.11 trong nguyên bản — dạng tỷ "
                   "lệ cộng tích phân cộng vi phân: thêm ống mềm tích phân, van tốc độ và van xả "
                   "chênh áp để giảm độ lệch và tăng tốc hiệu chỉnh cho hệ thống chậm.",
                   "Figure 4.12 (p. 92) · Pneumatic controller schematic - identically captioned "
                   "<i>Pneumatic Controller Schematic</i> in the source - with proportional, reset "
                   "and rate action: reset and proportional bellows, a rate valve and a "
                   "differential relief valve reduce offset and speed correction on slow systems.",
                   "Sơ đồ bộ điều khiển khí nén có tích phân và vi phân",
                   "Pneumatic controller schematic with reset and rate action")


@_reg
def fig_f4_13():
    """Figure 4.13 (p. 93) - Wireless Position Monitor Mounted on an Actuator."""
    w, h = 620, 390
    o = [_defs()]
    o.append(_rect(210, 60, 200, 96, fill="#eef3fb", sw=1.7))
    o.append(T(310, 88, "Wireless Position Monitor", 8.4, weight="600"))
    o.append(T(310, 106, "Bộ giám sát vị trí không dây", 7.6, color=GREY))
    o.append(_line(310, 60, 310, 34, sw=2, color=INK))
    o.append(_circle(310, 30, 4, fill=INK, sw=0))
    o.append(_path("M 296 24 A 20 20 0 0 1 324 24", sw=1.0, color=GREEN))
    o.append(_path("M 288 16 A 32 32 0 0 1 332 16", sw=1.0, color=GREEN))
    o.append(_line(310, 156, 310, 186, sw=3, color=INK))
    o.append(_c4_dia(310, 190, w=84, h=30))
    o.append(_bbody(310, 254, bw=128, bh=72))
    o.append(_leader(410, 108, 494, 100))
    o.append(T(498, 104, "0-100% digital", 7.4, anchor="start"))
    o.append(T(310, 354, "Phản hồi vị trí độc lập, không cần dây tín hiệu / Independent position feedback without signal wiring",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.13 - Wireless position monitor on an actuator",
                   "Hình 4.13 (tr. 93) · Bộ giám sát vị trí không dây lắp trên cơ cấu chấp hành",
                   "Hình 4.13 (tr. 93) · Bộ giám sát vị trí không dây lắp trên cơ cấu chấp hành: "
                   "thiết bị đo thân van và gửi tín hiệu số 0-100% độc lập với dây dẫn hệ thống "
                   "điều khiển; bản lắp có dây cho tín hiệu 4-20 mA.",
                   "Figure 4.13 (p. 93) · Wireless position monitor mounted on an actuator: the "
                   "device measures stem position and sends a 0-100% digital signal independent of "
                   "control-system wiring; a wired version supplies 4-20 mA.",
                   "Bộ giám sát vị trí không dây có ăn-ten trên thân van",
                   "Wireless position monitor with antenna on the valve actuator")


@_reg
def fig_f4_14():
    """Figure 4.14 (p. 93) - Spring-Return Actuator Diagram (source Fig 14.14)."""
    w, h = 640, 350
    o = [_defs()]
    o.append(_c4_box(30, 48, 104, 34, "IA Supply", size=8.4))
    o.append(_c4_sov(164, 40, ports=3))
    o.append(_arrow(134, 65, 164, 65, sw=1.5, color=GREEN))
    o.append(_line(200, 112, 200, 142, sw=2, color=BLUE))
    o.append(_c4_dia(200, 146, w=86, h=32))
    o.append(_line(200, 202, 200, 228, sw=3, color=INK))
    o.append(_bbody(200, 228, bw=118, bh=62))
    o.append(_leader(236, 146, 330, 132))
    o.append(T(334, 136, "Spring-return actuator / Cơ cấu hồi lò xo", 7.4, anchor="start"))
    o.append(T(200, 316, "Van ba chiều dùng cho cơ cấu hồi vị lò xo / Three-way SOV for spring-return actuators",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.14 - Spring-return actuator diagram",
                   "Hình 4.14 (tr. 93) · Sơ đồ cơ cấu chấp hành hồi vị bằng lò xo",
                   "Hình 4.14 (tr. 93) — đánh số 14.14 trong nguyên bản — sơ đồ cơ cấu chấp hành "
                   "hồi vị bằng lò xo: van điện từ ba chiều cấp hoặc xả khí cho buồng màng; khi mất "
                   "khí, lò xo đưa van về trạng thái an toàn.",
                   "Figure 4.14 (p. 93) - numbered 14.14 in the source - spring-return actuator "
                   "diagram: a three-way solenoid valve supplies or vents the diaphragm casing, "
                   "and on loss of air the spring drives the valve to its safe state.",
                   "Van điện từ ba chiều cấp khí cho cơ cấu màng có lò xo",
                   "Three-way solenoid valve feeding a spring-return diaphragm actuator")


@_reg
def fig_f4_15():
    """Figure 4.15 (p. 93) - Double-Acting Actuator Diagram (source Fig 14.15)."""
    w, h = 640, 370
    o = [_defs()]
    o.append(_c4_box(26, 44, 100, 34, "IA Supply", size=8.4))
    o.append(_c4_sov(156, 36, ports=4, size=38))
    o.append(_arrow(126, 61, 156, 61, sw=1.5, color=GREEN))
    o.append(_line(196, 108, 196, 130, sw=2, color=BLUE))
    o.append(_line(270, 108, 270, 130, sw=2, color=BLUE))
    o.append(_rect(160, 130, 320, 140, fill="#f4f7fb", sw=1.8))
    o.append(_rect(182, 146, 276, 46, fill="#e9eef4", sw=1.4))
    o.append(T(320, 174, "Upper side / Phía trên", 8.0))
    o.append(_rect(182, 208, 276, 46, fill="#e9eef4", sw=1.4))
    o.append(T(320, 236, "Lower side / Phía dưới", 8.0))
    o.append(_line(320, 192, 320, 208, sw=4, color=INK))
    o.append(_line(320, 270, 320, 296, sw=3, color=INK))
    o.append(_bbody(320, 296, bw=110, bh=42))
    o.append(T(320, 340, "Van bốn chiều cho cơ cấu tác động kép / Four-way SOV for double-acting actuators",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.15 - Double-acting actuator diagram",
                   "Hình 4.15 (tr. 93) · Sơ đồ cơ cấu chấp hành tác động kép",
                   "Hình 4.15 (tr. 93) — đánh số 14.15 trong nguyên bản — sơ đồ cơ cấu chấp hành "
                   "tác động kép: van điện từ bốn chiều cấp khí cho một phía piston và xả phía kia, "
                   "tạo chuyển động hai hướng không có lò xo hồi vị.",
                   "Figure 4.15 (p. 93) - numbered 14.15 in the source - double-acting actuator "
                   "diagram: a four-way solenoid valve pressurizes one side of the piston and vents "
                   "the other for two-direction travel without a return spring.",
                   "Van điện từ bốn chiều điều khiển piston hai chiều",
                   "Four-way solenoid valve controlling a two-direction piston")


@_reg
def fig_f4_16():
    """Figure 4.16 (p. 94) - SOV and DVC in a 1oo2 Configuration (source 14.16)."""
    w, h = 660, 370
    o = [_defs()]
    o.append(_c4_box(28, 54, 132, 42, "Logic solver", size=8.2))
    o.append(_c4_box(190, 54, 138, 42, "DVC / Bộ điều khiển số", size=7.8))
    o.append(_c4_sov(374, 46, ports=3, size=36))
    o.append(_arrow(160, 75, 190, 75, sw=1.4, color=GREEN))
    o.append(_arrow(328, 75, 374, 75, sw=1.4, color=GREEN))
    o.append(_line(410, 108, 410, 138, sw=2, color=BLUE))
    o.append(_c4_dia(410, 142, w=84, h=30))
    o.append(_line(410, 196, 410, 222, sw=3, color=INK))
    o.append(_bbody(410, 222, bw=118, bh=62))
    o.append(_c4_box(52, 190, 156, 40, "1oo2: either device trips", size=7.6))
    o.append(_arrow(208, 210, 374, 190, sw=1.0, dash="4 3", color=GREY))
    o.append(T(330, 316, "SOV và DVC: bất kỳ một trong hai thiết bị đều đưa van về trạng thái an toàn",
               7.4, color=GREY))
    return _finish(w, h, o, "Figure 4.16 - Solenoid valve and DVC in a 1oo2 configuration",
                   "Hình 4.16 (tr. 94) · Van điện từ và DVC trong cấu hình 1oo2",
                   "Hình 4.16 (tr. 94) — đánh số 14.16 trong nguyên bản — van điện từ đặt giữa bộ "
                   "điều khiển van số và van điều khiển; SOV luôn được cấp điện khi DVC đang điều "
                   "khiển, và hoặc SOV hoặc DVC đều có thể đưa van về trạng thái đóng/an toàn "
                   "(cấu hình 1-out-of-2).",
                   "Figure 4.16 (p. 94) - numbered 14.16 in the source - solenoid valve and DVC in "
                   "a 1oo2 configuration: the SOV sits between the controller and the valve and "
                   "stays energized during normal control; either the SOV or the DVC can drive the "
                   "valve to the closed or safe state.",
                   "Cấu hình 1oo2 gồm DVC và van điện từ trước cơ cấu chấp hành",
                   "1oo2 arrangement of a DVC and solenoid valve ahead of the actuator")


@_reg
def fig_f4_17():
    """Figure 4.17 (p. 94) - Direct-Acting Solenoid Valve Assembly (source 14.17)."""
    w, h = 620, 330
    o = [_defs()]
    o.append(_c4_box(30, 54, 100, 34, "IA Supply", size=8.4))
    o.append(_c4_sov(166, 46, ports=3, size=40))
    o.append(_arrow(130, 71, 166, 71, sw=1.5, color=GREEN))
    o.append(_leader(166, 60, 100, 118))
    o.append(T(96, 122, "Coil / Cuộn dây", 7.4, anchor="end"))
    o.append(_leader(206, 60, 300, 118))
    o.append(T(304, 122, "Direct electromagnetic force", 7.4, anchor="start"))
    o.append(_line(206, 126, 206, 158, sw=2, color=BLUE))
    o.append(_c4_dia(206, 162, w=80, h=28))
    o.append(T(206, 244, "Tác động trực tiếp chỉ bằng lực điện từ / Operated solely by solenoid force",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.17 - Direct-acting solenoid valve assembly",
                   "Hình 4.17 (tr. 94) · Cụm van điện từ tác động trực tiếp",
                   "Hình 4.17 (tr. 94) — đánh số 14.17 trong nguyên bản — cụm van điện từ tác động "
                   "trực tiếp: lực điện từ của cuộn dây trực tiếp đổi trạng thái van, phù hợp toàn "
                   "dải áp suất 0-150 psi của cơ cấu chấp hành.",
                   "Figure 4.17 (p. 94) - numbered 14.17 in the source - direct-acting solenoid "
                   "valve assembly: solenoid electromagnetic force alone changes valve state, "
                   "suited to the full 0-150 psi actuator pressure range.",
                   "Van điện từ tác động trực tiếp có cuộn dây và lò xo",
                   "Direct-acting solenoid valve with coil and return spring")


@_reg
def fig_f4_18():
    """Figure 4.18 (p. 94) - Pilot-Operated Solenoid Valve (source 14.18)."""
    w, h = 640, 350
    o = [_defs()]
    o.append(_c4_box(24, 46, 96, 32, "External air", size=8.0))
    o.append(_c4_sov(148, 42, ports=3, size=34))
    o.append(_c4_sov(148, 190, ports=3, size=34))
    o.append(_arrow(120, 62, 148, 62, sw=1.4, color=GREEN))
    o.append(T(230, 56, "Pilot SOV / Van thử", 7.6, anchor="start"))
    o.append(T(230, 204, "Main SOV / Van chính", 7.6, anchor="start"))
    o.append(_line(216, 76, 216, 118, sw=1.4, color=GREEN))
    o.append(_arrow(216, 118, 216, 190, sw=1.4, color=GREEN))
    o.append(_line(216, 260, 216, 292, sw=2, color=BLUE))
    o.append(T(216, 310, "Đổi trạng thái bằng áp suất khí ngoài / State changed by external air pressure",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.18 - Pilot-operated solenoid valve",
                   "Hình 4.18 (tr. 94) · Van điện từ dẫn khí ngoài",
                   "Hình 4.18 (tr. 94) — đánh số 14.18 trong nguyên bản — van điện từ dẫn khí ngoài: "
                   "một mẫu điện từ tác động trực tiếp bật/tắt áp suất khí ngoài để đổi trạng thái "
                   "van chính, ngay cả khi thân van chính không có áp suất.",
                   "Figure 4.18 (p. 94) - numbered 14.18 in the source - externally-piloted solenoid "
                   "valve: a direct-acting solenoid pilot switches external air to change the main "
                   "valve state even with no pressure in the main valve body.",
                   "Van chính và van thử dẫn khí ngoài",
                   "Main solenoid valve with an external-air pilot valve")


@_reg
def fig_f4_19():
    """Figure 4.19 (p. 95) - 1oo2 SOV Architecture (source Fig 14.19)."""
    w, h = 660, 370
    o = [_defs()]
    o.append(_c4_box(24, 50, 104, 34, "IA Supply", size=8.4))
    o.append(_c4_sov(158, 42, ports=3, size=34))
    o.append(_c4_sov(158, 152, ports=3, size=34))
    o.append(_arrow(128, 67, 158, 67, sw=1.4, color=GREEN))
    o.append(_line(128, 67, 128, 169, sw=1.4, color=GREEN))
    o.append(_arrow(128, 169, 158, 169, sw=1.4, color=GREEN))
    o.append(_line(226, 76, 286, 76, sw=1.6, color=BLUE))
    o.append(_line(226, 186, 286, 186, sw=1.6, color=BLUE))
    o.append(_line(286, 76, 286, 186, sw=1.6, color=BLUE))
    o.append(_arrow(286, 186, 286, 226, sw=1.8, color=BLUE))
    o.append(_c4_dia(286, 230, w=82, h=28))
    o.append(_bbody(286, 292, bw=112, bh=46))
    o.append(_c4_box(396, 78, 232, 52, "1oo2: any 1 of 2 SOVs trips / bất kỳ 1 trong 2", size=7.8))
    o.append(T(286, 356, "Kiến trúc song song: một van đủ đưa phần tử điều khiển cuối về an toàn / Parallel: one SOV suffices",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.19 - 1oo2 solenoid-operated valve architecture",
                   "Hình 4.19 (tr. 95) · Kiến trúc van điện từ 1oo2",
                   "Hình 4.19 (tr. 95) — đánh số 14.19 trong nguyên bản — kiến trúc van điện từ 1oo2: "
                   "hai SOV mắc song song trước phần tử điều khiển cuối; chỉ cần một trong hai đổi "
                   "trạng thái khi có yêu cầu là van về trạng thái an toàn.",
                   "Figure 4.19 (p. 95) - numbered 14.19 in the source - 1oo2 solenoid-operated "
                   "valve architecture: two SOVs in parallel ahead of the final control element, "
                   "where any one changing state puts the valve in its safe state.",
                   "Hai van điện từ song song trong kiến trúc 1oo2",
                   "Two parallel solenoid valves in a 1oo2 architecture")


@_reg
def fig_f4_20():
    """Figure 4.20 (p. 95) - 2oo2 SOV Architecture (source Fig 14.20)."""
    w, h = 660, 370
    o = [_defs()]
    o.append(_c4_box(24, 50, 104, 34, "IA Supply", size=8.4))
    o.append(_c4_sov(158, 42, ports=3, size=34))
    o.append(_c4_sov(296, 152, ports=3, size=34))
    o.append(_arrow(128, 67, 158, 67, sw=1.4, color=GREEN))
    o.append(_line(226, 76, 296, 76, sw=1.6, color=BLUE))
    o.append(_line(296, 76, 296, 152, sw=1.6, color=BLUE))
    o.append(_line(364, 186, 418, 186, sw=1.6, color=BLUE))
    o.append(_arrow(418, 186, 418, 226, sw=1.8, color=BLUE))
    o.append(_c4_dia(418, 230, w=82, h=28))
    o.append(_bbody(418, 292, bw=112, bh=46))
    o.append(_c4_box(56, 178, 214, 48, "2oo2: both SOVs must trip / cả hai phải đổi", size=7.6))
    o.append(T(330, 356, "Kiến trúc nối tiếp: phải cả hai van đổi trạng thái mới ngắt / Series: both SOVs must change state",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.20 - 2oo2 solenoid-operated valve architecture",
                   "Hình 4.20 (tr. 95) · Kiến trúc van điện từ 2oo2",
                   "Hình 4.20 (tr. 95) — đánh số 14.20 trong nguyên bản — kiến trúc van điện từ 2oo2: "
                   "hai SOV mắc nối tiếp; phải cả hai cùng đổi trạng thái khi có yêu cầu mới đưa "
                   "phần tử điều khiển cuối về trạng thái an toàn.",
                   "Figure 4.20 (p. 95) - numbered 14.20 in the source - 2oo2 solenoid-operated "
                   "valve architecture: two SOVs in series, where both must change state on demand "
                   "to put the final control element in its safe state.",
                   "Hai van điện từ nối tiếp trong kiến trúc 2oo2",
                   "Two series solenoid valves in a 2oo2 architecture")


@_reg
def fig_f4_21():
    """Figure 4.21 (p. 95) - Redundant SOV (source Fig 14.21)."""
    w, h = 640, 340
    o = [_defs()]
    o.append(_c4_box(24, 48, 96, 32, "IA Supply", size=8.0))
    o.append(_c4_sov(152, 42, ports=3, size=34))
    o.append(_c4_sov(152, 150, ports=3, size=34))
    o.append(_line(120, 64, 152, 64, sw=1.4, color=GREEN))
    o.append(_line(120, 64, 120, 172, sw=1.4, color=GREEN))
    o.append(_arrow(120, 172, 152, 172, sw=1.4, color=GREEN))
    o.append(_line(220, 76, 300, 76, sw=1.6, color=BLUE))
    o.append(_line(220, 184, 300, 184, sw=1.6, color=BLUE))
    o.append(_line(300, 76, 300, 184, sw=1.6, color=BLUE))
    o.append(_arrow(300, 184, 380, 184, sw=1.6, color=BLUE))
    o.append(_c4_box(388, 128, 210, 70, "Final control element / Phần tử điều khiển cuối", size=7.8))
    o.append(_c4_box(78, 228, 300, 40, "Avoid spurious trips / Tránh ngắt giả", size=7.8))
    o.append(T(320, 308, "Giảm ngắt giả và bảo đảm ngắt khi có yêu cầu / Reduce spurious trips and ensure shutdown on demand",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.21 - Redundant solenoid valve",
                   "Hình 4.21 (tr. 95) · Hệ thống van điện từ dự phòng",
                   "Hình 4.21 (tr. 95) — đánh số 14.21 trong nguyên bản — hệ thống van điện từ dự "
                   "phòng dùng cho ứng dụng trọng yếu: hai SOV song song giúp tránh ngắt giả và "
                   "đồng thời bảo đảm cụm van vẫn đóng khi có yêu cầu.",
                   "Figure 4.21 (p. 95) - numbered 14.21 in the source - redundant solenoid valve "
                   "system for critical service: parallel SOVs help avoid spurious trips while "
                   "helping ensure shutdown still occurs when demanded.",
                   "Hai van điện từ dự phòng song song",
                   "Two parallel redundant solenoid valves")


@_reg
def fig_f4_22():
    """Figure 4.22 (p. 95) - Three-Way Manual Reset SOV (source Fig 14.22)."""
    w, h = 620, 340
    o = [_defs()]
    o.append(_c4_box(28, 50, 96, 32, "IA Supply", size=8.0))
    o.append(_c4_sov(154, 44, ports=3, size=40))
    o.append(_arrow(124, 66, 154, 66, sw=1.4, color=GREEN))
    o.append(_line(194, 124, 194, 158, sw=2, color=BLUE))
    o.append(_c4_dia(194, 162, w=80, h=28))
    o.append(_line(234, 88, 286, 88, sw=2, color=RED))
    o.append(_rect(286, 74, 20, 28, fill="#fdf3e6", sw=1.4))
    o.append(_line(296, 74, 296, 48, sw=2.2, color=RED))
    o.append(_circle(296, 44, 9, fill="#fdf3e6", sw=1.4))
    o.append(_leader(296, 44, 366, 40))
    o.append(T(370, 44, "Manual reset lever / Cần đặt lại bằng tay", 7.6, anchor="start"))
    o.append(T(310, 300, "Cấp điện nhưng chưa tác động cho tới khi người vận hành nâng cần / Energized but inert until an operator lifts the lever",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.22 - Three-way manual reset solenoid valve",
                   "Hình 4.22 (tr. 95) · Van điện từ ba chiều đặt lại bằng tay",
                   "Hình 4.22 (tr. 95) — đánh số 14.22 trong nguyên bản — van điện từ ba chiều đặt "
                   "lại bằng tay: SOV được cấp điện nhưng không tác động cho tới khi người vận hành "
                   "nâng cần cơ khí vào vị trí, dùng khi cần xác nhận trước khi đưa vào vận hành.",
                   "Figure 4.22 (p. 95) - numbered 14.22 in the source - three-way manual reset SOV: "
                   "the valve is energized but will not operate until an operator lifts a lever, "
                   "used when verification is needed before putting the SOV in service.",
                   "Van điện từ ba chiều có cần đặt lại bằng tay",
                   "Three-way solenoid valve with a manual reset lever")


@_reg
def fig_f4_23():
    """Figure 4.23 (p. 95) - SOV Manifold Assembly (source Fig 14.23)."""
    w, h = 640, 340
    o = [_defs()]
    o.append(_rect(120, 120, 400, 110, fill="#eef3fb", sw=1.8))
    o.append(T(320, 142, "Manifold block / Khối phân phối", 8.6, weight="600"))
    for i, cx in enumerate((190, 320, 450)):
        o.append(_c4_sov(cx - 22, 170, ports=3, size=34))
        o.append(T(cx, 234, "SOV %d" % (i + 1), 7.4))
    o.append(_line(120, 175, 74, 175, sw=4, color=GREEN))
    o.append(T(70, 168, "IA", 7.6, anchor="end", color=GREEN))
    o.append(_line(520, 175, 566, 175, sw=4, color=BLUE))
    o.append(T(570, 168, "To actuator", 7.6, anchor="start", color=BLUE))
    o.append(T(320, 278, "Nhiều phụ kiện nối trực tiếp vào manifold, gọn sơ đồ đấu dây / Accessories connect directly, simplifying hookup",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.23 - SOV manifold assembly",
                   "Hình 4.23 (tr. 95) · Cụm manifold van điện từ",
                   "Hình 4.23 (tr. 95) — đánh số 14.23 trong nguyên bản — cụm manifold van điện từ: "
                   "nhiều SOV được lắp trên một khối phân phối chung, nối trực tiếp để loại bỏ đoạn "
                   "ống dài và đơn giản hóa sơ đồ đấu dây tại hiện trường.",
                   "Figure 4.23 (p. 95) - numbered 14.23 in the source - SOV manifold assembly: "
                   "several SOVs mounted on one common block, connected directly to eliminate long "
                   "tubing runs and simplify the field hookup schematic.",
                   "Khối manifold mang ba van điện từ",
                   "Manifold block carrying three solenoid valves")


@_reg
def fig_f4_24():
    """Figure 4.24 (p. 96) - Trip Valve Shown in Tripped Condition."""
    w, h = 680, 440
    o = [_defs()]
    o.append(_c4_box(30, 46, 118, 34, "Supply pressure", size=8.0))
    o.append(_line(148, 63, 214, 63, sw=2, color=GREEN))
    o.append(_poly([(214, 55), (230, 63), (214, 71)], fill="#fdf3e6", sw=1.2, close=True))
    o.append(T(222, 46, "Check valve", 7.0))
    o.append(_line(230, 63, 276, 63, sw=2, color=GREEN))
    o.append(_rect(276, 34, 46, 116, fill="#e9eef4", sw=1.5))
    o.append(T(299, 98, "Volume", 7.4))
    o.append(T(299, 112, "tank", 7.4))
    o.append(_rect(360, 120, 180, 100, fill="#f4f7fb", sw=1.8))
    o.append(T(450, 140, "Trip valve / Van ngắt", 8.4, weight="600"))
    o.append(T(450, 160, "TRIPPED / ĐÃ NGẮT", 7.4, color=RED, weight="600"))
    for i, lab in enumerate(("A", "B", "C", "D", "E", "F")):
        px = 382 + i * 28
        o.append(_circle(px, 200, 8, fill="#fdf3e6", sw=1.0))
        o.append(T(px, 203, lab, 7.0))
    o.append(_line(322, 170, 360, 170, sw=2, color=GREEN))
    o.append(_c4_box(30, 200, 118, 36, "Positioner / Bộ định vị", size=7.4))
    o.append(_arrow(148, 218, 360, 214, sw=1.4, color=BLUE))
    o.append(_line(450, 220, 450, 262, sw=2, color=BLUE))
    o.append(_rect(392, 262, 216, 84, fill="#f4f7fb", sw=1.6))
    o.append(_rect(410, 272, 180, 28, fill="#e9eef4", sw=1.3))
    o.append(T(500, 290, "Upper cylinder / Xi lanh trên", 7.4))
    o.append(_rect(410, 308, 180, 28, fill="#e9eef4", sw=1.3))
    o.append(T(500, 326, "Lower cylinder / Xi lanh dưới", 7.4))
    o.append(_line(500, 300, 500, 308, sw=3, color=INK))
    o.append(_c4_labels(["Cấp vào bình / Supply to charge tank",
                         "Van một chiều / Check valve",
                         "Bình chứa / Volume tank",
                         "Cổng A-F / Ports A-F",
                        "Áp suất xi lanh trên / Upper cylinder pressure"], 40, 370, lh=13))
    o.append(_c4_labels(["Áp suất xi lanh dưới / Lower cylinder pressure",
                         "Bộ định vị / Positioner",
                         "Trạng thái đã ngắt / Tripped condition",
                        "Khóa ở vị trí cuối / Lock in last position"], 356, 370, lh=13))
    return _finish(w, h, o, "Figure 4.24 - Trip valve shown in tripped condition",
                   "Hình 4.24 (tr. 96) · Van ngắt trong trạng thái đã ngắt",
                   "Hình 4.24 (tr. 96) · Van ngắt trong trạng thái đã ngắt: khi áp suất cấp xuống "
                   "dưới điểm ngắt, van ngắt dùng khí dự phòng từ bình chứa qua van một chiều để "
                   "đưa cơ cấu chấp hành về trạng thái an toàn; các cổng A–F nối bộ định vị và hai "
                   "phía xi lanh.",
                   "Figure 4.24 (p. 96) · Trip valve shown in tripped condition: when supply falls "
                   "below the trip point, the valve uses reserve air from a volume tank through a "
                   "check valve to drive the actuator to its safe state; ports A-F link the "
                   "positioner and both cylinder sides.",
                   "Sơ đồ van ngắt có bình chứa và cổng A đến F",
                   "Trip valve diagram with volume tank and ports A through F")


@_reg
def fig_f4_25():
    """Figure 4.25 (p. 96) - Typical 3-Way Switching Valve."""
    w, h = 620, 350
    o = [_defs()]
    o.append(_line(310, 40, 310, 62, sw=2, color=INK))
    o.append(_rect(292, 24, 36, 16, fill="#eef3fb", sw=1.3))
    o.append(T(310, 18, "Adjusting screw", 7.2))
    o.append(_spring(310, 40, 92, width=24, turns=5))
    o.append(_rect(248, 92, 124, 62, fill="#eef3fb", sw=1.5))
    o.append(T(310, 116, "Spring case", 8.0))
    o.append(T(310, 136, "Vỏ lò xo", 7.4, color=GREY))
    o.append(_ellipse(310, 168, 56, 14, fill="#f7f9fb", sw=1.3))
    o.append(_rect(248, 182, 124, 66, fill="#f4f7fb", sw=1.5))
    o.append(T(310, 216, "3-way switching", 8.0, weight="600"))
    o.append(T(310, 234, "valve / van chuyển mạch", 7.2, color=GREY))
    for i, lab in enumerate(("A", "B", "C")):
        px = 270 + i * 40
        o.append(_line(px, 248, px, 274, sw=1.6, color=GREY))
        o.append(T(px, 286, "Port " + lab, 7.2))
    o.append(T(310, 320, "Áp suất giảm không đổi; Lock in Last / Constant reduced pressure; lock in last position",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.25 - Typical 3-way switching valve",
                   "Hình 4.25 (tr. 96) · Van chuyển mạch ba chiều điển hình",
                   "Hình 4.25 (tr. 96) · Van chuyển mạch ba chiều điển hình: vít chỉnh trên vỏ lò xo "
                   "đặt điểm chuyển mạch theo yêu cầu, cung cấp áp suất khí giảm không đổi cho bộ "
                   "điều khiển dẫn khí; dùng để đạt tác động an toàn «Khóa ở vị trí cuối cùng».",
                   "Figure 4.25 (p. 96) · Typical three-way switching valve: an adjusting screw on "
                   "the spring case sets the switching point, delivering constant reduced pressure "
                   "to pilot-operated controllers and providing a lock-in-last fail action.",
                   "Van chuyển mạch ba chiều có vít chỉnh và vỏ lò xo",
                   "Three-way switching valve with adjusting screw and spring case")


@_reg
def fig_f4_26():
    """Figure 4.26 (p. 97) - Actuator with Side-Mounted Handwheel."""
    w, h = 620, 410
    o = [_defs()]
    o.append(_c4_dia(310, 90, w=110, h=46))
    o.append(_line(310, 160, 310, 194, sw=3, color=INK))
    o.append(_bbody(310, 194, bw=124, bh=72))
    o.append(_line(365, 112, 424, 112, sw=2, color=INK))
    o.append(_rect(418, 102, 18, 20, fill="#fdf3e6", sw=1.3))
    o.append(_line(436, 112, 470, 112, sw=2, color=INK))
    o.append(_c4_handwheel(498, 112, 38))
    o.append(_leader(498, 74, 498, 48))
    o.append(T(498, 44, "Side handwheel / Tay quay bên hông", 7.6))
    o.append(_leader(365, 112, 300, 60))
    o.append(T(296, 56, "Bevel gear / Bánh răng côn", 7.4, anchor="end"))
    o.append(T(310, 298, "Giới hạn hành trình một hướng; vị trí trung tính cho phép vận hành tự động toàn hành trình",
               7.2, color=GREY))
    o.append(T(310, 320, "Limits travel in one direction; neutral allows full automatic travel",
               7.0, color=GREY))
    return _finish(w, h, o, "Figure 4.26 - Actuator with side-mounted handwheel",
                   "Hình 4.26 (tr. 97) · Cơ cấu chấp hành có tay quay lắp bên hông",
                   "Hình 4.26 (tr. 97) · Cơ cấu chấp hành có tay quay lắp bên hông: qua bánh răng côn, "
                   "tay quay đi van được theo một hướng tại bất kỳ điểm nào của hành trình thân; có "
                   "thể giới hạn một hướng, còn vị trí trung tính cho vận hành tự động toàn hành trình.",
                   "Figure 4.26 (p. 97) · Actuator with a side-mounted handwheel: through a bevel "
                   "gear the wheel strokes the valve in either direction at any point in stem "
                   "travel; it can limit one direction, while neutral permits full automatic travel.",
                   "Tay quay lắp bên hông qua bánh răng côn trên cơ cấu màng",
                   "Side handwheel through a bevel gear on a diaphragm actuator")


@_reg
def fig_f4_27():
    """Figure 4.27 (p. 97) - Actuator with Top-Mounted Handwheel."""
    w, h = 620, 410
    o = [_defs()]
    o.append(_c4_handwheel(310, 74, 40))
    o.append(_line(310, 114, 310, 138, sw=3, color=INK))
    o.append(_c4_dia(310, 142, w=112, h=46))
    o.append(_line(310, 212, 310, 244, sw=3, color=INK))
    o.append(_bbody(310, 244, bw=124, bh=72))
    o.append(_leader(350, 74, 440, 66))
    o.append(T(444, 70, "Top handwheel / Tay quay trên đỉnh", 7.6, anchor="start"))
    o.append(_leader(310, 142, 200, 132))
    o.append(T(196, 136, "Diaphragm actuator / Cơ cấu màng", 7.4, anchor="end"))
    o.append(T(310, 344, "Dùng cho dịch vụ không thường xuyên để đi van bằng tay / For infrequent manual stroking service",
               7.2, color=GREY))
    return _finish(w, h, o, "Figure 4.27 - Actuator with top-mounted handwheel",
                   "Hình 4.27 (tr. 97) · Cơ cấu chấp hành có tay quay lắp trên đỉnh",
                   "Hình 4.27 (tr. 97) · Cơ cấu chấp hành có tay quay lắp trên đỉnh: tay quay nằm "
                   "trục trên cơ cấu màng, dùng cho dịch vụ không thường xuyên để đi van bằng tay "
                   "khi cần định vị van trong trường hợp khẩn cấp.",
                   "Figure 4.27 (p. 97) · Actuator with a top-mounted handwheel: the wheel sits on "
                   "the axis of the diaphragm actuator and is used for infrequent service to "
                   "manually stroke or position the valve in an emergency.",
                   "Tay quay lắp trên đỉnh cơ cấu màng",
                   "Handwheel mounted on top of the diaphragm actuator")
