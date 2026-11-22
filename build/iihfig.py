# -*- coding: utf-8 -*-
"""Vector figures for Chapter 1 "Measurement of Temperature" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation &
Control* (2018), printed pp. 2-45 (PDF pp. 16-59).

The source carries six numbered figures (Figure 1 - Figure 6).  All are
redrawn here as simplified vector schematics that keep the topology and the
labels of the originals; numbered callouts are used where a components list
is appropriate.  Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through ``_fig()``.
All SVG text is XML-escaped with ``esc()``/``T()`` before it reaches a tag.
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
    # the XML validation import does ET.fromstring(s[0]) on every FIG value.
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


def _num(cx, cy, n):
    """A numbered callout bubble."""
    return (_circle(cx, cy, 8, fill="#fdf3e6", sw=1.1, color=INK)
            + T(cx, cy + 3, str(n), 8.0, color=INK, weight="600"))


def _legend(items, x, y, lh=15, size=7.6):
    """Numbered parts list rendered as plain text lines."""
    return "".join(T(x, y + i * lh, "%d. %s" % (i + 1, lab), size,
                     anchor="start") for i, lab in enumerate(items))


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """Figure 1 (source PDF p.19, printed p.5) - Thermowell."""
    w, h = 680, 330
    o = [_defs()]
    # process vessel wall, fluid to the right
    o.append(_rect(300, 36, 34, 250, fill="url(#h6)", sw=1.4))
    o.append(T(317, 30, "Vách bình / vessel wall", 8, color=GREY))
    o.append(T(470, 46, "Chất lỏng quá trình / process fluid", 8.4,
              color=BLUE, anchor="middle"))
    # a few fluid wavy hints
    for yy in (86, 118, 150, 182, 214, 246):
        o.append(_line(360, yy, 580, yy, sw=0.7, color="#bcd7e6", dash="4 5"))
    # thermowell: closed-end metal tube inserted from the left into the fluid
    o.append(_rect(150, 130, 380, 34, fill="#e8edf2", sw=1.6))
    o.append(_poly([(530, 130), (546, 134), (556, 147), (546, 160), (530, 164)],
                   fill="#e8edf2", sw=1.6, close=True))
    o.append(_line(150, 130, 150, 164, sw=1.6))
    # thermometer stem and bulb inside the well, scale on the left
    o.append(_rect(86, 141, 350, 12, fill="#fdf3e6", sw=1.1))
    o.append(_ellipse(444, 147, 13, 8, fill=RED, sw=1.0))
    for i in range(9):
        xx = 100 + i * 34
        o.append(_line(xx, 138, xx, 145 if i % 2 else 133, sw=0.8))
        o.append(T(xx, 127, str(i), 6.4, color=GREY))
    o.append(T(120, 190, "Nhiệt kế / thermometer", 8.4, color=INK, anchor="start"))
    # callouts
    for lx, ly, n, tx, ty in [
        (96, 110, 1, 175, 137), (200, 210, 2, 300, 147),
        (317, 90, 3, 317, 100), (600, 190, 4, 540, 150),
    ]:
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        o.append(_num(lx, ly - 12, n))
    o.append(T(317, 312,
               "Hình 1.1 (nguyên bản tr. 5) · Giê-cheo-nhiệt (thermowell): ống kim loại bịt kín một đầu",
               7.8, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.1 - Thermowell"))
    return _fig(s,
                "Hình 1.1 (nguyên bản Hình 1, tr. 5) · Giê-cheo-nhiệt (thermowell): ống kim loại "
                "bịt kín một đầu được đưa vào buồng hoặc chất lỏng; nhiệt kế nằm bên trong ống và "
                "tiếp xúc với thành ống. Các số chỉ: 1. Nhiệt kế; 2. Thân giê-cheo-nhiệt; "
                "3. Vách bình; 4. Chất lỏng quá trình.",
                "Figure 1.1 (source Figure 1, p. 5) · Thermowell: a closed-end metal tube that "
                "sticks into the chamber or fluid, with the thermometer sitting inside the well "
                "and making contact with its sides. Callouts: 1. Thermometer; 2. Thermowell tube; "
                "3. Vessel wall; 4. Process fluid.",
                "Mặt cắt giê-cheo-nhiệt với nhiệt kế đặt trong ống kim loại bịt kín xuyên qua vách bình",
                "Thermowell cross-section with a thermometer inside a closed-end tube through a vessel wall")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Figure 2 (source PDF p.23, printed p.9) - Bimetal strip."""
    w, h = 680, 330
    o = [_defs()]
    # fixed clamp at the left
    o.append(_rect(70, 110, 40, 110, fill="#d9dee4", sw=1.3))
    for xx in (78, 90, 102):
        o.append(_circle(xx, 120, 3, fill=INK))
        o.append(_circle(xx, 210, 3, fill=INK))
    o.append(T(90, 96, "Đầu cố định", 8, color=GREY))
    # strip at ambient: two bonded layers, straight
    o.append(_rect(110, 152, 250, 12, fill=BLUE, sw=1.0))
    o.append(_rect(110, 164, 250, 12, fill="#c8d9e4", sw=1.0))
    o.append(T(235, 146, "Kim loại giãn nở nhiều", 7.6, color=BLUE))
    o.append(T(235, 190, "Kim loại giãn nở ít", 7.6, color="#3f6a86"))
    # heated state: the strip curls upward, ending at a contact
    pts_a = [(110, 240), (180, 240), (240, 236), (300, 220), (350, 192), (380, 158)]
    pts_b = [(110, 252), (180, 252), (240, 248), (300, 232), (350, 204), (380, 170)]
    o.append(_poly(pts_a, sw=3.2, color=BLUE))
    o.append(_poly(pts_b, sw=3.2, color="#3f6a86"))
    # fixed contact above the free end
    o.append(_line(374, 126, 374, 142, sw=2.4, color=INK))
    o.append(_circle(374, 146, 4, fill=GREEN))
    o.append(T(400, 138, "Tiếp điểm / contact", 8, color=GREEN, anchor="start"))
    # heat arrows
    for xx in (170, 230, 290):
        o.append(_arrow(xx, 296, xx, 268, sw=1.2, color=RED))
    o.append(T(230, 312, "Nhiệt độ tăng / rising temperature", 8, color=RED))
    # callouts
    for lx, ly, n, tx, ty in [
        (140, 112, 1, 170, 154), (140, 282, 2, 165, 246),
        (430, 196, 3, 375, 175), (90, 232, 4, 112, 232),
    ]:
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        o.append(_num(lx, ly + (12 if ly < 200 else -12), n))
    o.append(T(340, 326, "Hình 1.2 (nguyên bản tr. 9) · Thanh hai kim loại uốn cong khi nóng",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.2 - Bimetal strip"))
    return _fig(s,
                "Hình 1.2 (nguyên bản Hình 2, tr. 9) · Thanh hai kim loại: hai vật liệu khác nhau "
                "được ép với nhau; khi nhiệt độ tăng chúng giãn nở với tốc độ khác nhau nên tạo "
                "ứng suất làm thanh cuộn lại. Các số chỉ: 1. Lớp kim loại giãn nở nhiều; "
                "2. Lớp kim loại giãn nở ít; 3. Đầu tự do / tiếp điểm; 4. Đầu cố định.",
                "Figure 1.2 (source Figure 2, p. 9) · Bimetal strip: two different metals sandwiched "
                "together expand at different rates, generating a stress that makes the element curl "
                "when heated. Callouts: 1. High-expansion metal layer; 2. Low-expansion metal layer; "
                "3. Free end / contact; 4. Fixed end.",
                "Thanh hai kim loại ở trạng thái nguội và khi bị nóng, uốn về phía tiếp điểm",
                "Bimetal strip shown cold and heated, curling toward a switch contact")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Figure 3 (source PDF p.31, printed p.17) - Three-wire RTD cross section."""
    w, h = 680, 350
    o = [_defs()]
    cx = 250
    # stainless steel sheath, closed at the bottom
    o.append(_rect(cx - 44, 60, 88, 220, fill="#e4e9ee", sw=1.8))
    o.append(_poly([(cx - 44, 280), (cx - 36, 292), (cx, 298), (cx + 36, 292), (cx + 44, 280)],
                   fill="#e4e9ee", sw=1.8, close=True))
    o.append(_line(cx - 44, 70, cx + 44, 70, sw=1.2))
    # ceramic powder fill
    o.append(_rect(cx - 34, 78, 68, 196, fill="#f7f0df", sw=1.0))
    for yy in range(88, 272, 16):
        o.append(_line(cx - 30, yy, cx + 30, yy, sw=0.5, color="#d4c8a8", dash="2 3"))
    # non-inductively wound resistance coil (zig-zag folded back on itself)
    coil = []
    for i in range(16):
        yy = 92 + i * 11
        coil.append((cx - 18 if i % 2 else cx + 18, yy))
    o.append(_poly(coil, sw=2.2, color=RED))
    o.append(_line(cx + 18, 92, cx + 18, 267, sw=0.8, color=RED, dash="2 4"))
    o.append(_line(cx - 18, 92, cx - 18, 267, sw=0.8, color=RED, dash="2 4"))
    # three lead wires leaving the top
    for i, col in enumerate((BLUE, GREEN, INK)):
        x0 = cx - 16 + i * 16
        o.append(_line(x0, 92, x0, 34, sw=1.6, color=col))
        o.append(T(x0, 26, str(i + 1), 7.6, color=col))
    o.append(T(cx, 18, "Ba dây dẫn / three leads", 8.2, color=GREY))
    # callouts and legend
    for lx, ly, n, tx, ty in [
        (110, 96, 1, cx - 44, 110), (110, 160, 2, cx - 34, 160),
        (110, 230, 3, cx - 18, 220), (400, 60, 4, cx + 10, 60),
    ]:
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        o.append(_num(lx, ly + 12, n))
    o.append(_legend([
        "Vỏ thép không gỉ / stainless-steel sheath",
        "Bột gốm dẫn nhiệt / ceramic powder fill",
        "Cuộn điện trở không cảm ứng / non-inductive coil",
        "Ba dây dẫn, hiệu chỉnh sụt áp / three leads",
    ], 405, 116, lh=28, size=8.0))
    o.append(T(340, 336, "Hình 1.3 (nguyên bản tr. 17) · Mặt cắt RTD ba dây điển hình",
               7.8, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.3 - Three-wire RTD cross section"))
    return _fig(s,
                "Hình 1.3 (nguyên bản Hình 3, tr. 17) · Mặt cắt của RTD ba dây điển hình: cuộn dây "
                "được quấn không cảm ứng trong vỏ thép không gỉ, khe hở giữa phần tử và vỏ được "
                "lấp bằng bột gốm để dẫn nhiệt tốt; có ba dây dẫn để hiệu chỉnh sụt áp. Các số chỉ: "
                "1. Vỏ thép; 2. Bột gốm; 3. Cuộn điện trở; 4. Ba dây dẫn.",
                "Figure 1.3 (source Figure 3, p. 17) · Cross section of a typical three-wire RTD: a "
                "non-inductively wound coil inside a stainless-steel sheath, the space filled with "
                "ceramic powder for good thermal conduction, and three leads for lead-wire voltage "
                "drop correction. Callouts: 1. Steel sheath; 2. Ceramic powder; 3. Resistance coil; "
                "4. Three leads.",
                "Mặt cắt đầu dò RTD ba dây gồm vỏ thép, bột gốm, cuộn điện trở và ba dây dẫn",
                "Cross-section of a three-wire RTD showing sheath, ceramic fill, coil and three leads")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Figure 4 (source PDF p.33, printed p.19) - Thermopile in a hair drier."""
    w, h = 680, 320
    o = [_defs()]
    # barrel of the hair drier
    o.append(_rect(150, 90, 330, 140, fill="#eef2f6", sw=1.8))
    o.append(_poly([(480, 90), (520, 104), (520, 216), (480, 230)],
                   fill="#e4eaf0", sw=1.8, close=True))
    # handle
    o.append(_rect(250, 230, 52, 60, fill="#dfe5ec", sw=1.5))
    o.append(T(276, 306, "Tay cầm / handle", 7.6, color=GREY))
    # heating coil (hot) and fan (cool end)
    o.append(_circle(210, 160, 40, fill="none", sw=1.4))
    for k in range(6):
        o.append(_line(210, 160, 210 + 38 * math.cos(k * 1.047),
                       160 + 38 * math.sin(k * 1.047), sw=1.2, color=BLUE))
    o.append(T(210, 222, "Quạt / fan", 7.6, color=BLUE))
    heat = []
    for i in range(9):
        xx = 285 + i * 20
        heat.append((xx, 140 - 12 * (1 if i % 2 else -1)))
    o.append(_poly(heat, sw=3.0, color=RED))
    o.append(T(370, 122, "Cuộn gia nhiệt / heater coil", 7.8, color=RED))
    # thermopile sensor facing the heater
    o.append(_rect(430, 148, 30, 26, fill="#fdf3e6", sw=1.5))
    o.append(T(445, 138, "Thermopile", 7.6, color=INK))
    for k in range(3):
        o.append(_arrow(415 - k * 14, 156 + k * 5, 463, 156 + k * 5,
                        sw=1.0, color=RED))
    o.append(T(500, 170, "Bức xạ IR", 7.6, color=RED, anchor="start"))
    # wires to control
    o.append(_line(445, 174, 445, 210, sw=1.2, color=GREY))
    o.append(_rect(410, 210, 70, 18, fill="#e9edf2", sw=1.1))
    o.append(T(445, 223, "Điều khiển", 7.2))
    # air flow
    for yy in (250, 268):
        o.append(_arrow(300, yy, 540, yy, sw=1.2, color=BLUE))
    o.append(T(420, 284, "Luồng khí / airflow", 7.6, color=BLUE))
    o.append(T(340, 316, "Hình 1.4 (nguyên bản tr. 19) · Thermopile trong máy sấy tóc",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.4 - Thermopile in a hair drier"))
    return _fig(s,
                "Hình 1.4 (nguyên bản Hình 4, tr. 19) · Thermopile được dùng trong máy sấy tóc: "
                "cảm biến hướng vào cuộn gia nhiệt, hấp thụ bức xạ hồng ngoại từ bề mặt nóng và "
                "tạo tín hiệu điện tỉ lệ với nhiệt độ, dùng để điều khiển gia nhiệt và luồng khí.",
                "Figure 1.4 (source Figure 4, p. 19) · Thermopiles are used in hair driers: the "
                "sensor faces the heater coil, absorbs the infrared radiation emitted by the hot "
                "surface and produces an electrical signal proportional to temperature for control.",
                "Sơ đồ máy sấy tóc với cảm biến thermopile hướng vào cuộn gia nhiệt",
                "Hair drier schematic with a thermopile sensor facing the heater coil")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Figure 5 (source PDF p.33, printed p.19) - Ear thermometer thermopile."""
    w, h = 680, 330
    o = [_defs()]
    # head outline (simplified) and ear canal
    o.append(_ellipse(250, 165, 130, 120, fill="#f7efe6", sw=1.6))
    o.append(_path("M330,125 C370,130 400,145 430,160 L430,188 C400,198 370,205 330,210",
                   fill="#efe2d2", sw=1.4))
    o.append(_ellipse(428, 174, 16, 26, fill="#e8d3bd", sw=1.2))
    o.append(T(433, 218, "Màng nhĩ / eardrum", 7.8, color=GREY, anchor="start"))
    o.append(T(250, 52, "Đầu nhiệt kế nhét vào ống tai", 8.6, color=INK))
    # thermometer probe with lens and thermopile
    o.append(_rect(452, 158, 130, 32, fill="#eaf0f6", sw=1.6))
    o.append(_poly([(452, 158), (436, 164), (436, 184), (452, 190)],
                   fill="#dfe8f0", sw=1.6, close=True))
    o.append(_line(446, 164, 446, 184, sw=2.2, color=BLUE))     # lens
    o.append(_rect(470, 162, 26, 24, fill="#fdf3e6", sw=1.2))  # thermopile
    o.append(T(483, 154, "Thermopile", 7.6))
    o.append(T(446, 208, "Thấu kính / lens", 7.4, color=BLUE))
    # handle and display
    o.append(_rect(548, 190, 46, 100, fill="#dfe5ec", sw=1.5))
    o.append(_rect(540, 196, 62, 30, fill="#fbfaf7", sw=1.2))
    o.append(T(571, 215, "37.0 °C", 9.0, color=INK, weight="600"))
    o.append(T(571, 306, "Thân máy / handle", 7.4, color=GREY))
    # IR rays from eardrum to sensor
    for k in range(3):
        o.append(_arrow(420, 164 + k * 10, 448, 166 + k * 8, sw=1.1, color=RED))
    o.append(T(400, 142, "Bức xạ IR", 7.6, color=RED, anchor="start"))
    o.append(T(340, 326, "Hình 1.5 (nguyên bản tr. 19) · Nhiệt kế tai dùng cảm biến thermopile",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.5 - Ear thermometer uses a thermopile"))
    return _fig(s,
                "Hình 1.5 (nguyên bản Hình 5, tr. 19) · Nhiệt kế tai dùng thermopile: đầu dò hướng "
                "vào màng nhĩ, thấu kính tập trung bức xạ hồng ngoại từ màng nhĩ tới cảm biến "
                "thermopile, cho kết đọc nhanh không cần chạm vào màng nhĩ.",
                "Figure 1.5 (source Figure 5, p. 19) · Ear thermometers use thermopiles: the probe "
                "is aimed at the eardrum and a lens focuses the infrared radiation onto the "
                "thermopile detector, giving a fast reading without touching the eardrum.",
                "Nhiệt kế tai với đầu dò thermopile hướng bức xạ hồng ngoại từ màng nhĩ",
                "Ear thermometer with a thermopile probe aimed at the eardrum")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Figure 6 (source PDF p.34, printed p.20) - Thermocouple assembly."""
    w, h = 680, 330
    o = [_defs()]
    # protective sheath with closed (measuring) tip
    o.append(_rect(120, 140, 300, 40, fill="#e6ebf0", sw=1.6))
    o.append(_poly([(420, 140), (444, 146), (456, 160), (444, 174), (420, 180)],
                   fill="#e6ebf0", sw=1.6, close=True))
    # two dissimilar metal wires joined at the measuring junction
    o.append(_line(130, 152, 430, 152, sw=2.4, color=BLUE))
    o.append(_line(130, 168, 430, 168, sw=2.4, color=RED))
    o.append(_circle(438, 160, 9, fill="#f6d9a8", sw=1.4))
    o.append(T(438, 136, "Mối nối đo", 7.6, color=INK))
    # extension leads to the readout at the cold junction
    o.append(_line(120, 152, 60, 152, sw=1.8, color=BLUE))
    o.append(_line(120, 168, 60, 168, sw=1.8, color=RED))
    o.append(_line(60, 152, 60, 120, sw=1.6, color=BLUE))
    o.append(_line(60, 168, 60, 120, sw=1.6, color=RED))
    o.append(_rect(30, 78, 60, 42, fill="#eef3fb", sw=1.4))
    o.append(T(60, 96, "Nhiệt kế", 8.0))
    o.append(T(60, 110, "hoặc bộ đọc", 7.4))
    o.append(T(60, 136, "Mối nối tham chiếu", 7.4, color=GREY))
    # numbered callouts + legend
    for lx, ly, n, tx, ty in [
        (200, 110, 1, 210, 152), (200, 200, 2, 210, 168),
        (474, 120, 3, 440, 152), (300, 220, 4, 300, 180),
        (96, 60, 5, 60, 80),
    ]:
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        o.append(_num(lx, ly + (12 if ly < 190 else -12), n))
    o.append(_legend([
        "Dây kim loại A / metal A wire",
        "Dây kim loại B / metal B wire",
        "Mối nối nóng (đo) / measuring junction",
        "Vỏ bảo vệ, cách điện / sheath and insulation",
        "Mối nối lạnh tới bộ đọc / reference junction",
    ], 500, 110, lh=30, size=7.8))
    o.append(T(360, 322, "Hình 1.6 (nguyên bản tr. 20) · Cụm cặp nhiệt điện",
               7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.6 - Thermocouple assembly"))
    return _fig(s,
                "Hình 1.6 (nguyên bản Hình 6, tr. 20) · Cụm cặp nhiệt điện: hai dây kim loại khác "
                "nhau được nối ở một đầu (mối nối đo/nóng), đầu kia nối tới nhiệt kế hoặc thiết bị "
                "đọc có khả năng đo cặp nhiệt điện (mối nối tham chiếu/lạnh). Các số chỉ: "
                "1. Dây kim loại A; 2. Dây kim loại B; 3. Mối nối đo; 4. Vỏ bảo vệ; 5. Mối nối tham chiếu.",
                "Figure 1.6 (source Figure 6, p. 20) · Thermocouple assembly: two dissimilar metal "
                "wires joined at one end (the measuring/hot junction) and connected at the other end "
                "to a thermocouple thermometer or capable device (the reference/cold junction). "
                "Callouts: 1. Metal A wire; 2. Metal B wire; 3. Measuring junction; 4. Protective "
                "sheath; 5. Reference junction.",
                "Cụm cặp nhiệt điện gồm hai dây kim loại khác nhau nối ở đầu đo và nối tới bộ đọc",
                "Thermocouple assembly with two dissimilar wires joined at the measuring end")
