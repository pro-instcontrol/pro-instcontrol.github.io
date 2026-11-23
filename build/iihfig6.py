# -*- coding: utf-8 -*-
"""Vector figures for Chapter 6 "Mechanical Flow Meters" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 217-256 (printed pp. 203-242).

The nine source figures are photographs or line drawings with short numbered
captions (source Fig. 7 has only a bare caption; it is the bypass-line
installation for oval gear meters described in the adjacent text).  They are
redrawn here as simplified bilingual vector schematics.  Every function
returns the standard 5-tuple ``(svg, caption_vi, caption_en, aria_vi,
aria_en)`` through ``_finish()``.  All SVG text is XML-escaped with ``esc()``
and kept romanized (unaccented) Vietnamese; the bilingual captions use full
Vietnamese diacritics.  Source figure order 1 through 9 is preserved.
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
    figs = f()
    FIGS[f.__name__] = figs
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"\x26(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _bl(x, y, vi, en, size=7.4, color=INK, anchor="start", dy=11):
    """Two-line bilingual label (Vietnamese over English)."""
    return (T(x, y, vi, size, color=color, anchor=anchor)
            + T(x, y + dy, en, size - 0.7, color=GREY, anchor=anchor))


def _num(cx, cy, n):
    """A numbered callout bubble."""
    return (_circle(cx, cy, 8, fill="#fdf3e6", sw=1.1, color=INK)
            + T(cx, cy + 3, str(n), 8.0, color=INK, weight="600"))


def _legend(items, x, y, lh=15, size=7.6):
    """Numbered parts list rendered as plain text lines."""
    return "".join(T(x, y + i * lh, "%d. %s" % (i + 1, lab), size,
                     anchor="start") for i, lab in enumerate(items))


def _callouts(items):
    """Draw connector lines and numbered bubbles from (lx,ly) to (tx,ty)."""
    o = []
    for i, (lx, ly, tx, ty) in enumerate(items):
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        dy = 12 if ly < 200 else -12
        o.append(_num(lx, ly + dy, i + 1))
    return "".join(o)


def _foot(w, y, text):
    # Auto-shrink long bilingual notes so they stay inside the canvas.
    size = min(7.6, max(4.4, 640.0 / (len(text) * 0.52)))
    return T(w / 2.0, y, text, size, color=GREY)


def _panel(x, y, w, h, label):
    o = [_rect(x, y, w, h, fill="#fbfaf7", sw=1.3, stroke=GREY)]
    o.append(T(x + w / 2.0, y + 16, label, 8.6, color=INK, weight="600"))
    return "".join(o)


def _finish(o, w, h, title, cap_vi, cap_en, aria_vi, aria_en):
    s = svg(w, h, "".join(o), esc(title))
    return _fig(s, cap_vi, cap_en, aria_vi, aria_en)


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """One-dimensional flow system with a restriction (source Figure 1)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "He thong dong 1 chieu voi doan thu hep / "
                        "One-dimensional flow system with a restriction",
               8.6, color=INK, weight="600"))
    # Pipe wall, centre line and the restriction at x = 340.
    o.append(_rect(60, 118, 560, 112, fill="#eef3fb", sw=1.8))
    o.append(_line(60, 174, 620, 174, sw=0.9, color=GREY, dash="6 5"))
    o.append(_rect(330, 118, 20, 38, fill="#9aa4ad", sw=1.2))
    o.append(_rect(330, 194, 20, 36, fill="#9aa4ad", sw=1.2))
    # Converging / diverging streamlines through the gap.
    for k in (0, 1, 2, 3, 4, 5):
        yy = 128 + k * 18
        o.append(_path("M64,%d L300,%d Q330,%d 352,168 Q374,%d 616,%d"
                       % (yy, yy, 150 + k * 5, 150 + k * 5, yy),
                       sw=1.0, color=BLUE))
    o.append(_arrow(96, 174, 176, 174, sw=2.2, color=BLUE))
    o.append(T(136, 110, "Chay / Flow", 7.4, color=BLUE))
    # Upstream (Section 1) and downstream (Section 2) reference stations.
    o.append(_line(170, 230, 170, 250, sw=1.0, color=INK))
    o.append(_line(500, 230, 500, 250, sw=1.0, color=INK))
    o.append(T(170, 262, "Mat cat 1 / Section 1", 7.6, color=INK, weight="600"))
    o.append(T(500, 262, "Mat cat 2 / Section 2", 7.6, color=INK, weight="600"))
    o.append(T(170, 276, "T1 A1 rho1 V1 P1 Z1", 7.0, color=GREY))
    o.append(T(500, 276, "T2 A2 rho2 V2 P2 Z2", 7.0, color=GREY))
    # Restriction label and the head difference h.
    o.append(T(340, 152, "Thu hep / Restriction", 7.0, color=INK, weight="600"))
    o.append(_line(250, 118, 250, 92, sw=1.2, color=RED))
    o.append(_circle(250, 88, 3.5, fill=RED))
    o.append(_line(430, 118, 430, 92, sw=1.2, color=GREEN))
    o.append(_circle(430, 88, 3.5, fill=GREEN))
    o.append(T(340, 80, "h = P1/(rho g) - P2/(rho g)", 7.6, color=INK))
    o.append(_foot(680, 320, "Gia su dong nhat chieu, chat long khong nen, khong ma sat / "
                             "One-dimensional, incompressible, frictionless flow is assumed"))
    o.append(_foot(680, 346, "Su thu hep lam tang van toc va giam ap suat; do giam ap suat cho biet luong "
                             "chay / The restriction raises velocity and lowers pressure; the drop indicates flow"))
    return _finish(o, w, h, "One-dimensional flow system with a restriction",
        "Hình 6.1 · Hệ thống dòng một chiều có đoạn thu hẹt trong đường ống: chất lỏng chảy từ mặt cắt 1 "
        "(thượng lưu) qua đoạn thu hẹt tới mặt cắt 2 (hạ lưu). Các thông số T, A, ρ, V, P, Z lần lượt là "
        "nhiệt độ, tiết diện, mật độ, vận tốc, áp suất và độ cao đường tâm; chênh cột áp h phản ánh lưu lượng.",
        "Figure 6.1 · A one-dimensional flow system with a restriction in the pipeline: fluid passes from "
        "section 1 (upstream) through the restriction to section 2 (downstream). T, A, ρ, V, P and Z are "
        "temperature, area, density, stream velocity, pressure and centre-line elevation; the head difference h "
        "indicates the flow rate.",
        "Sơ đồ dòng một chiều có đoạn thu hẹt trong ống",
        "Schematic of a one-dimensional flow system with a pipe restriction")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Orifice and differential-pressure measurement (source Figure 2)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dia lo va do chenh ap / Orifice and pressure-differential measurement",
               8.8, color=INK, weight="600"))
    o.append(_rect(60, 88, 560, 62, fill="#eef3fb", sw=1.8))
    o.append(_arrow(98, 119, 186, 119, sw=2.0, color=BLUE))
    o.append(T(142, 104, "Chat long / Fluid", 7.2, color=BLUE))
    # Orifice plate split by the bore.
    o.append(_rect(334, 88, 9, 25, fill="#9aa4ad", sw=1.0))
    o.append(_rect(334, 125, 9, 25, fill="#9aa4ad", sw=1.0))
    o.append(_path("M343,113 L360,119 L343,125 Z", fill="#f6e6c8", sw=1.0))
    # Pressure legs to the U-tube manometer.
    o.append(_line(272, 150, 272, 212, sw=1.4, color=INK))
    o.append(_line(272, 212, 306, 212, sw=1.4, color=INK))
    o.append(_line(414, 150, 414, 212, sw=1.4, color=INK))
    o.append(_line(414, 212, 378, 212, sw=1.4, color=INK))
    o.append(_rect(302, 212, 9, 108, fill="#fbfaf7", sw=1.6))
    o.append(_rect(370, 212, 9, 108, fill="#fbfaf7", sw=1.6))
    o.append(_path("M306,320 A34,34 0 0 0 374,320", sw=1.6, color=INK))
    o.append(_rect(302, 258, 9, 62, fill="#bcd3e6", sw=0))
    o.append(_rect(370, 288, 9, 32, fill="#bcd3e6", sw=0))
    o.append(_path("M302,288 A34,34 0 0 0 370,318 L370,320 A34,34 0 0 1 302,290 Z",
                   fill="#9bbedd", sw=0))
    o.append(_line(306, 258, 352, 258, sw=0.9, color=RED, dash="4 3"))
    o.append(_line(374, 288, 328, 288, sw=0.9, color=RED, dash="4 3"))
    o.append(T(340, 252, "h", 9.0, color=RED))
    o.append(T(272, 168, "Tap thuong / Upstream tap", 6.8, color=INK, anchor="end"))
    o.append(T(414, 168, "Tap ha / Downstream tap", 6.8, color=INK))
    o.append(T(340, 334, "Chat do: rho_m / Manometer fluid: rho_m", 7.2, color=INK))
    o.append(T(340, 350, "rho_f = weight density of the measured fluid", 6.8, color=GREY))
    o.append(_foot(680, 374, "Q = K A sqrt(2 g h (rho_m - rho_f) / rho_f); "
                             "K = Cd / sqrt(1 - beta^4)"))
    return _finish(o, w, h, "Orifice and pressure-differential measurement",
        "Hình 6.2 · Đo lưu lượng bằng tấm lỗ và đồng hồ chênh áp: dòng chất lỏng qua tấm lỗ, hai đường dẫn "
        "áp thượng lưu và hạ lưu nối tới ống chữ U. Chênh cột chất lỏng h, cùng mật độ chất đo ρf và mật độ "
        "chất áp kế ρm, được dùng để tính lưu lượng.",
        "Figure 6.2 · Flow measurement with an orifice and a differential manometer: upstream and downstream "
        "pressure legs feed a U-tube. The liquid-column difference h, together with the fluid density ρf and "
        "manometer-fluid density ρm, gives the flow rate.",
        "Tấm lỗ và đồng hồ đo chênh áp chữ U",
        "Orifice plate and a U-tube differential manometer")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Reciprocating piston meter (source Figure 3)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Dong ho piston qua lai / Reciprocating piston meter",
               9.0, color=INK, weight="600"))
    # Cylinder and piston.
    o.append(_rect(120, 132, 420, 108, fill="#eef3fb", sw=1.8))
    o.append(_rect(300, 138, 32, 96, fill="#c9d2d9", sw=1.4))
    o.append(_line(332, 186, 500, 186, sw=3.0, color=INK))
    o.append(_arrow(60, 186, 150, 186, sw=2.0, color=BLUE))
    o.append(_arrow(500, 186, 620, 186, sw=2.0, color=RED))
    # Two slide valves at the inlet and outlet ports.
    o.append(_rect(156, 108, 56, 24, fill="#f6e6c8", sw=1.2))
    o.append(_rect(468, 108, 56, 24, fill="#f6e6c8", sw=1.2))
    o.append(_line(184, 132, 184, 150, sw=1.2, color=GREY))
    o.append(_line(496, 132, 496, 150, sw=1.2, color=GREY))
    # External arm drives the counter.
    o.append(_line(500, 186, 500, 268, sw=1.4, color=GREY))
    o.append(_line(500, 268, 568, 268, sw=1.4, color=GREY))
    o.append(_circle(596, 268, 26, fill="#fdf3e6", sw=1.4))
    o.append(T(596, 264, "Bo dem", 7.2, color=INK))
    o.append(T(596, 274, "Counter", 6.6, color=GREY))
    # Labels.
    o.append(_bl(178, 92, "1. Van truot vao", "inlet slide valve", 7.0))
    o.append(_bl(496, 92, "2. Van truot ra", "outlet slide valve", 7.0))
    o.append(T(316, 252, "3. Piston", 7.4, color=INK, weight="600"))
    o.append(T(320, 264, "xi lanh gang / cast-iron cylinder", 6.6, color=GREY))
    o.append(T(84, 172, "Dau vao / Inlet", 6.8, color=BLUE))
    o.append(T(586, 172, "Dau ra / Outlet", 6.8, color=RED))
    o.append(_foot(680, 326, "Chat long day piston sang trai roi sang phai; hai van truot doi chieu "
                             "va canh tay ngoai cho bo dem / Fluid drives the piston left then right; the slide "
                             "valves reverse and the external arm drives the counter"))
    o.append(_foot(680, 352, "Do chinh xac tu ±0.2 den ±0.3% / Accuracy from ±0.2 to ±0.3%"))
    return _finish(o, w, h, "Reciprocating piston meter",
        "Hình 6.3 · Đồng hồ piston qua lại: xi lanh gang chứa piston, hai van trượt ở cổng vào và cổng ra. "
        "Chất lỏng đẩy piston từ cực trái sang cực phải, van trượt đổi chiều và cánh tay ngoài dẫn động bộ "
        "đếm; độ chính xác ±0,2 đến ±0,3%.",
        "Figure 6.3 · A reciprocating piston meter: a cast-iron cylinder holds a piston, with two slide valves "
        "at the inlet and outlet ports. Fluid drives the piston from one extreme to the other, the slide valves "
        "reverse, and an external arm drives the counter; accuracy is ±0.2 to ±0.3%.",
        "Đồng hồ đo piston qua lại gồm xi lanh, piston và hai van trượt",
        "Reciprocating piston meter with cylinder, piston and two slide valves")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Operating principle of the piston meter (source Figure 4)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Nguyen ly hoat dong cua dong ho piston / Operating principle of the piston meter",
               8.8, color=INK, weight="600"))
    # Cylinder with the piston shown in two extreme positions.
    o.append(_rect(110, 136, 460, 96, fill="#eef3fb", sw=1.8))
    o.append(_rect(210, 142, 28, 84, fill="#dbe4ea", sw=1.0, dash="4 3"))
    o.append(_rect(442, 142, 28, 84, fill="#dbe4ea", sw=1.0, dash="4 3"))
    o.append(_rect(324, 142, 30, 84, fill="#c9d2d9", sw=1.4))
    # Alternate flow arrows through each end of the cylinder.
    o.append(_arrow(140, 184, 300, 184, sw=1.8, color=BLUE))
    o.append(_arrow(372, 184, 540, 184, sw=1.8, color=RED))
    o.append(_arrow(300, 214, 150, 214, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_arrow(540, 214, 380, 214, sw=1.2, color=RED, dash="4 3"))
    # Slide valve above the ports, linked to the counter.
    o.append(_rect(300, 100, 80, 24, fill="#f6e6c8", sw=1.2))
    o.append(_line(340, 124, 340, 142, sw=1.2, color=GREY))
    o.append(_line(340, 100, 340, 76, sw=1.2, color=GREY))
    o.append(_circle(340, 72, 16, fill="#fdf3e6", sw=1.2))
    o.append(T(340, 76, "Dem", 7.0, color=INK))
    # Numbered callouts with a compact legend.
    o.append(_num(150, 250, 1))
    o.append(_num(500, 250, 2))
    o.append(_num(340, 300, 3))
    o.append(_legend(["Xi lanh / cylinder", "Van truot / slide valve",
                      "Co cau dem / counting mechanism"], 174, 268, lh=14, size=7.2))
    o.append(_foot(680, 332, "Piston cho chat long chay xen ke qua moi dau xi lanh tu dau vao den dau ra / "
                             "The piston passes liquid alternately through each end of the cylinder, inlet to outlet"))
    o.append(_foot(680, 358, "Van truot dieu khien cong vao/ra va cho bo dem; do chinh xac trong 0.5% / "
                             "The slide valve controls the ports and the counter; accuracy within 0.5%"))
    return _finish(o, w, h, "Operating principle of the piston meter",
        "Hình 6.4 · Nguyên lý hoạt động của đồng hồ piston: piston qua lại đẩy chất lỏng xen kẽ qua hai đầu "
        "xi lanh từ cổng vào tới cổng ra; van trượt điều khiển hai cổng và dẫn động bộ đếm. Với lưu lượng "
        "nhỏ dùng piston đường kính lớn, hành trình ngắn, độ chính xác trong 0,5%.",
        "Figure 6.4 · Operating principle of the piston meter: the reciprocating piston passes liquid "
        "alternately through each end of the cylinder from inlet to outlet, while the slide valve controls the "
        "ports and drives the counter. Low flows use large-diameter pistons with short strokes; accuracy is "
        "within 0.5%.",
        "Nguyên lý piston đẩy chất lỏng xen kẽ qua hai đầu xi lanh",
        "Piston principle passing liquid alternately through each cylinder end")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Nutating disk meter (source Fig. 5)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dong ho dia dao dong / Nutating disk meter",
               9.0, color=INK, weight="600"))
    # Precision-machined chamber.
    o.append(_rect(120, 110, 380, 170, fill="#eef3fb", sw=1.8))
    o.append(_ellipse(310, 194, 132, 52, fill="#fbfaf7", sw=1.2))
    # Central ball and the slotted, tilting disk.
    o.append(_circle(310, 194, 20, fill="#c9d2d9", sw=1.4))
    o.append(_ellipse(310, 178, 104, 26, fill="#f6e6c8", sw=1.4, color=BLUE))
    o.append(_ellipse(310, 210, 104, 26, fill="#f6e6c8", sw=1.4, color=BLUE))
    o.append(_line(310, 178, 310, 210, sw=0.9, color=GREY, dash="3 3"))
    # Axial pin, cam and gear train to the totalizer.
    o.append(_line(330, 194, 402, 194, sw=2.0, color=INK))
    o.append(_circle(408, 194, 12, fill="#fdf3e6", sw=1.2))
    o.append(_line(420, 194, 470, 194, sw=1.4, color=INK))
    o.append(_rect(500, 160, 80, 68, fill="#fbfaf7", sw=1.4))
    o.append(T(540, 186, "Bo dem", 7.4, color=INK, weight="600"))
    o.append(T(540, 202, "Totalizer /", 6.6, color=GREY))
    o.append(T(540, 214, "pulse output", 6.6, color=GREY))
    # Flow in and out.
    o.append(_arrow(60, 250, 130, 250, sw=2.0, color=BLUE))
    o.append(_arrow(500, 250, 620, 250, sw=2.0, color=RED))
    o.append(T(88, 238, "Dau vao / Inlet", 6.8, color=BLUE))
    o.append(T(560, 238, "Dau ra / Outlet", 6.8, color=RED))
    # Numbered callouts.
    o.append(_num(180, 128, 1))
    o.append(_num(310, 152, 2))
    o.append(_num(240, 226, 3))
    o.append(_num(444, 168, 4))
    o.append(_num(540, 150, 5))
    o.append(_legend(["Buong / chamber", "Bi tam / centre ball", "Dia / disk",
                      "Chan + cam / pin and cam", "Bo dem / totalizer"], 60, 284,
                     lh=14, size=7.2))
    o.append(_foot(680, 358, "Moi chu ky dao dong tuong ung mot the tich chat long co dinh / "
                             "Each nutation cycle corresponds to one fixed volume of liquid"))
    o.append(_foot(680, 382, "Sai so ±1 den 2%; nhiet do -150 den 120 do C; ap suat lam viec toi da 10 kg/cm2 / "
                             "Inaccuracy ±1 to 2%; temperature -150 to 120 deg C; max working pressure 10 kg/cm2"))
    return _finish(o, w, h, "Nutating disk meter",
        "Hình 6.5 · Đồng hồ đĩa dao động (nutating disk / disk meter): buồng gia công chính xác chứa bi tâm, "
        "đĩa có khe và chốt trục. Áp suất chất lỏng làm đĩa và bi dao động, chốt truyền chuyển động qua cam và "
        "bộ bánh răng tới bộ đếm; mỗi chu kỳ tương ứng một thể tích cố định.",
        "Figure 6.5 · A nutating disk meter: a precision-machined chamber contains a centre ball, a slotted disk "
        "and an axial pin. Liquid pressure makes the disk and ball nutate; the pin transmits motion through a cam "
        "and gear train to the totalizer, one fixed volume per cycle.",
        "Đồng hồ đĩa dao động với bi tâm, đĩa và chốt dẫn động bộ đếm",
        "Nutating disk meter with centre ball, disk and pin driving the totalizer")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Oscillating piston meter (source Figure 6)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dong ho piston dao dong / Oscillating piston meter",
               9.0, color=INK, weight="600"))
    positions = [(24, "Vi tri 1 / Position 1", "trung tinh / neutral"),
                 (238, "Vi tri 2 / Position 2", "lan trai / rolls left"),
                 (452, "Vi tri 3 / Position 3", "di xuong / driven down")]
    for ox, lab, sub in positions:
        cx = ox + 102
        o.append(_panel(ox, 44, 204, 256, lab))
        o.append(_circle(cx, 158, 52, fill="#eef3fb", sw=1.6))
        # Dividing bridge separating inlet from outlet.
        o.append(_rect(cx - 6, 116, 12, 84, fill="#9aa4ad", sw=1.0))
        # Slotted ring (split piston) in three angular states.
        if "1" in lab:
            pts = [(cx - 44, 138), (cx - 12, 116), (cx + 44, 138)]
        elif "2" in lab:
            pts = [(cx - 46, 156), (cx - 12, 122), (cx + 40, 148)]
        else:
            pts = [(cx - 42, 178), (cx - 8, 200), (cx + 46, 168)]
        o.append(_poly(pts, fill="none", sw=4.0, color=BLUE))
        o.append(_circle(cx, 158, 10, fill="#f6e6c8", sw=1.2))
        o.append(T(cx, 224, sub, 7.2, color=GREY))
        o.append(_arrow(cx - 70, 158, cx - 30, 158, sw=1.2, color=BLUE))
        o.append(_arrow(cx + 30, 158, cx + 70, 158, sw=1.2, color=RED))
        o.append(T(cx, 270, "vong chia / split ring", 7.0, color=INK))
    o.append(_foot(680, 326, "Vong chia dao dong trong mot mat phang quon cau noi; chuyen dong truyen qua mang "
                             "den bo dem / A split ring oscillates in one plane about the bridge; motion passes "
                             "through a diaphragm to the register"))
    o.append(_foot(680, 352, "Dung cho ong nho 50 mm hoac nho hon; do chinh xac ±1% / Used on pipes of 50 mm or "
                             "less; accuracy around ±1%"))
    return _finish(o, w, h, "Oscillating piston meter",
        "Hình 6.6 · Đồng hồ piston dao động gồm vòng chia (piston dạng vòng rãnh) dao động trong một mặt phẳng "
        "quanh cầu ngăn giữa cổng vào và cổng ra. Hình cho thấy chu kỳ ba vị trí: trung tính, lăn sang trái và "
        "bị đẩy xuống; chuyển động truyền qua màng tới bộ bánh răng và bộ đếm, độ chính xác khoảng ±1%.",
        "Figure 6.6 · An oscillating piston meter uses a split ring oscillating in one plane about the bridge "
        "between inlet and outlet. The three-position cycle is shown: neutral, rolling left and driven down; "
        "motion passes through a diaphragm to the gear train and register, with accuracy around ±1%.",
        "Chu kỳ ba vị trí của đồng hồ piston dao động",
        "Three-position cycle of an oscillating piston meter")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Bypass-line installation for oval gear meters (source Figure 7)."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Lap dat duong bang pass cho dong ho banh rang oval / "
                        "Bypass-line installation for oval gear meters", 8.4,
               color=INK, weight="600"))
    # Main process line with shut-off valves, strainer and meter.
    o.append(_line(60, 172, 620, 172, sw=2.4, color=INK))
    o.append(_poly([(126, 160), (126, 184), (146, 172)], fill="#f6e6c8", sw=1.2, close=True))
    o.append(_poly([(146, 160), (146, 184), (126, 172)], fill="#f6e6c8", sw=1.2, close=True))
    o.append(_poly([(556, 160), (556, 184), (576, 172)], fill="#f6e6c8", sw=1.2, close=True))
    o.append(_poly([(576, 160), (576, 184), (556, 172)], fill="#f6e6c8", sw=1.2, close=True))
    # Y-strainer.
    o.append(_path("M236,172 L262,196 L262,172 Z", fill="#dfeaf4", sw=1.2))
    o.append(_line(262, 196, 276, 196, sw=1.2, color=GREY))
    # Oval gear meter body with two meshing oval rotors.
    o.append(_rect(344, 146, 104, 52, fill="#eef3fb", sw=1.6))
    o.append(_ellipse(370, 172, 18, 13, fill="#f6e6c8", sw=1.2, color=BLUE))
    o.append(_ellipse(422, 172, 18, 13, fill="#f6e6c8", sw=1.2, color=GREEN))
    # Bypass branch below, with its own valve.
    o.append(_line(196, 172, 196, 300, sw=1.6, color=INK))
    o.append(_line(196, 300, 486, 300, sw=1.6, color=INK))
    o.append(_line(486, 300, 486, 172, sw=1.6, color=INK))
    o.append(_poly([(326, 288), (326, 312), (346, 300)], fill="#f6e6c8", sw=1.2, close=True))
    o.append(_poly([(346, 288), (346, 312), (326, 300)], fill="#f6e6c8", sw=1.2, close=True))
    # Flow direction and notes.
    o.append(_arrow(88, 172, 152, 172, sw=1.8, color=BLUE))
    o.append(T(96, 154, "Chay / Flow", 6.8, color=BLUE))
    o.append(T(136, 212, "Van cau / Shutoff", 6.6, color=INK, anchor="end"))
    o.append(T(566, 212, "Van cau / Shutoff", 6.6, color=INK))
    o.append(T(256, 214, "Luoc Y / Y-strainer", 6.6, color=INK))
    o.append(T(396, 138, "Dong ho / Meter", 7.2, color=INK, weight="600"))
    o.append(T(336, 330, "Van bang pass / Bypass valve", 7.0, color=INK))
    o.append(T(336, 344, "Duong bang pass / Bypass line", 6.8, color=GREY))
    o.append(_foot(680, 374, "Bang pass cho phep cach ly dong ho va luoc khoi duong chinh de ve sinh va sua chua "
                             "nhanh / The bypass isolates meter and strainer from the main line for quick cleaning "
                             "and repair"))
    o.append(_foot(680, 398, "Lap luoc phia truoc; lap van dieu tiet/ngat o phia sau; dong thang chay tu duoi "
                             "len tren / Strainer upstream; control valve downstream; vertical flow bottom to top"))
    return _finish(o, w, h, "Bypass-line installation for oval gear meters",
        "Hình 6.7 · Sơ đồ lắp đặt đường ống có đường vòng bypass cho đồng hồ bánh răng oval: đường chính gồm "
        "van ngắt, lưới lọc kiểu Y, đồng hồ và van ngắt; nhánh bypass có riêng một van. Đường vòng cho phép "
        "cách ly đồng hồ và lưới lọc để vệ sinh, bảo trì mà không ngừng dây chuyền.",
        "Figure 6.7 · Piping with a bypass line for oval gear meters: the main run carries shut-off valves, a "
        "Y-strainer, the meter and a control/shut-off valve, while the lower branch has its own bypass valve. The "
        "bypass allows the meter and strainer to be isolated for cleaning and repair.",
        "Lắp đặt đường vòng bypass cho đồng hồ bánh răng oval",
        "Bypass-line piping installation for an oval gear meter")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """A simple turbine flow meter (source Figure 8)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Dong ho tuabin don gian / A simple turbine flow meter",
               9.0, color=INK, weight="600"))
    # Flow tube and supports acting as straighteners.
    o.append(_rect(80, 142, 520, 96, fill="#eef3fb", sw=1.8))
    o.append(_rect(200, 150, 14, 80, fill="#c9d2d9", sw=1.0))
    o.append(_rect(466, 150, 14, 80, fill="#c9d2d9", sw=1.0))
    o.append(_arrow(114, 190, 184, 190, sw=2.0, color=BLUE))
    o.append(_arrow(496, 190, 574, 190, sw=1.6, color=RED))
    # Multi-bladed free-spinning rotor on a shaft.
    o.append(_line(240, 190, 460, 190, sw=2.0, color=INK))
    o.append(_ellipse(350, 190, 26, 44, fill="#f6e6c8", sw=1.4, color=BLUE))
    for k in range(6):
        yy = 160 + k * 12
        o.append(_line(336, yy, 364, yy, sw=0.9, color=GREY))
    # Pickup coil outside the tube, above the rotor.
    o.append(_rect(330, 96, 40, 24, fill="#fdf3e6", sw=1.2))
    o.append(_line(350, 120, 350, 142, sw=1.2, color=RED))
    o.append(T(350, 88, "Cuon cam bien / Pickup coil", 7.0, color=INK))
    # Numbered callouts.
    o.append(_num(132, 160, 1))
    o.append(_num(350, 250, 2))
    o.append(_num(207, 250, 3))
    o.append(_num(468, 250, 4))
    o.append(_legend(["Than ong / flow tube", "Rotor canh / bladed rotor",
                      "Gia do / supports", "Cuon cam bien / pickup coil"], 60, 286,
                     lh=14, size=7.2))
    o.append(_foot(680, 358, "Van toc quay cua rotor ti le voi van toc chat long; tan so tin hieu ti le voi luong "
                             "the tich / Rotor angular velocity is proportional to fluid velocity; signal "
                             "frequency is linear with volumetric flow"))
    return _finish(o, w, h, "A simple turbine flow meter",
        "Hình 6.8 · Đồng hồ tuabin đơn giản: toàn bộ chất lỏng đi qua ống và làm quay rôto nhiều cánh; tốc độ "
        "quay tỉ lệ với vận tốc dòng, tín hiệu tần số đầu ra tỉ lệ tuyến tính với lưu lượng thể tích. Giá đỡ "
        "đồng thời làm bộ chỉnh thẳng dòng và chứa ổ mở tự bôi trơn.",
        "Figure 6.8 · A simple turbine flow meter: all the fluid passes through the tube and spins a bladed "
        "rotor; rotational speed is proportional to fluid velocity and the frequency output varies linearly with "
        "volumetric flow. The supports also act as flow straighteners and house open, self-lubricating bearings.",
        "Đồng hồ tuabin đơn giản với rôto cánh và cuộn cảm biến",
        "Simple turbine meter with a bladed rotor and pickup coil")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """Turbine flow meter, detailed view (source Figure 9)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dong ho tuabin / Turbine flow meter",
               9.0, color=INK, weight="600"))
    # Housing and flow axis.
    o.append(_rect(80, 148, 520, 84, fill="#eef3fb", sw=1.8))
    o.append(_line(100, 190, 580, 190, sw=0.9, color=GREY, dash="6 5"))
    o.append(_arrow(118, 190, 196, 190, sw=2.0, color=BLUE))
    o.append(_arrow(484, 190, 562, 190, sw=1.6, color=RED))
    # Multibladed rotor mounted at right angles to the flow axis.
    o.append(_circle(340, 190, 46, fill="#fbfaf7", sw=1.4))
    for k in range(12):
        a = 2 * math.pi * k / 12.0
        o.append(_line(340 + 12 * math.cos(a), 190 + 12 * math.sin(a),
                       340 + 42 * math.cos(a), 190 + 42 * math.sin(a),
                       sw=1.6, color=BLUE))
    o.append(_circle(340, 190, 9, fill="#c9d2d9", sw=1.2))
    # Shaft retained in the housing by a shaft-support; bearings.
    o.append(_line(340, 190, 500, 190, sw=2.2, color=INK))
    o.append(_rect(470, 166, 14, 48, fill="#c9d2d9", sw=1.2))
    o.append(T(476, 234, "Gia truc / Shaft-support", 7.0, color=INK))
    o.append(T(476, 246, "o bi / ball or sleeve bearing", 6.6, color=GREY))
    # Magnetic pickup coil outside the fluid channel.
    o.append(_rect(322, 94, 36, 24, fill="#fdf3e6", sw=1.2))
    o.append(_line(340, 118, 340, 144, sw=1.2, color=RED))
    o.append(T(340, 86, "Cuon tu / Magnetic pickup coil", 7.0, color=INK))
    o.append(T(340, 280, "Moi canh di qua cuon tao mot xung dien ap / Each blade generates a voltage pulse",
               7.2, color=INK))
    o.append(_foot(680, 322, "Rotor quay tu do quanh truc; toc do do cuon tu giam sat ben ngoai vo dong ho / "
                             "The rotor spins freely about its shaft; speed is monitored by a magnetic pickup "
                             "coil fitted outside the meter housing"))
    o.append(_foot(680, 348, "So xung cho biet tong luong; tan so cho biet luong; f = np Q / Tp / "
                             "Pulse count gives total flow, frequency gives flow rate: f = np Q / Tp"))
    o.append(_foot(680, 374, "Co san 6.35 den 650 mm; luong chat long 100 cm3 den hon 50 m3 / "
                             "Sizes 6.35 to 650 mm; liquid range 100 cubic cm to over 50 cubic m"))
    return _finish(o, w, h, "Turbine flow meter",
        "Hình 6.9 · Đồng hồ tuabin điển hình: rôto nhiều cánh đặt vuông góc với trục dòng, được đỡ bằng "
        "ổ bi hoặc ổ bạc trên trục giữ bằng giá trong thân đồng hồ. Mỗi cánh đi qua cuộn cảm biến từ tính tạo "
        "một xung điện áp; tổng số xung cho tổng lưu lượng, tần số cho lưu lượng, f = np·Q/Tp.",
        "Figure 6.9 · A typical turbine flow meter: a multibladed rotor mounted at right angles to the flow "
        "axis, carried on ball or sleeve bearings on a shaft held by a support in the housing. Each blade passing "
        "the magnetic pickup generates a voltage pulse; total pulses give total flow and frequency gives flow "
        "rate, f = np·Q/Tp.",
        "Rôto nhiều cánh và cuộn cảm biến từ tính của đồng hồ tuabin",
        "Multibladed rotor and magnetic pickup of a turbine flow meter")
