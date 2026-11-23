# -*- coding: utf-8 -*-
"""Vector figures for Chapter 4 "pH Measurement" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 143-180 (printed pp. 130-166).

The source figures are images with numbered captions.  They are redrawn here
as simplified vector schematics with descriptive bilingual captions.  Every
function returns the standard 5-tuple ``(svg, caption_vi, caption_en,
aria_vi, aria_en)`` through ``_finish()``.  All SVG text is XML-escaped with
``esc()``/``T()``.  The printed chapter skips Figure 21; this module keeps the
source numbering (fig_f20, then fig_f22, fig_f23).
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
    """The mV/pH relation at two different temperatures."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Quan he mV/pH o hai nhiet do / mV/pH at two temperatures",
               9.0, color=INK, weight="600"))
    x0, y0, W, H = 92, 72, 452, 246

    def px(p):
        return x0 + p / 14.0 * W

    def py(e):
        return y0 + (600.0 - e) / 1200.0 * H

    for pv in (0, 7, 14):
        o.append(_line(px(pv), y0, px(pv), y0 + H, sw=0.6, color="#d5dbe0"))
        o.append(T(px(pv), y0 + H + 15, str(pv), 7.8, color=GREY))
    for ev in (400, 0, -400):
        o.append(_line(x0, py(ev), x0 + W, py(ev), sw=0.6, color="#d5dbe0"))
        o.append(T(x0 - 6, py(ev) + 3, str(ev), 7.2, color=GREY, anchor="end"))
    o.append(_line(x0, y0 + H, x0 + W + 10, y0 + H, sw=1.3))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.3))
    o.append(T(x0 + W + 22, y0 + H + 15, "pH", 8.4, color=INK, anchor="end"))
    o.append(T(x0 + 4, y0 - 14, "E (mV)", 8.4, color=INK))
    # E = -59.16(pH-7) at 25 C; E = -74.04(pH-7.5) at 100 C.
    o.append(_line(px(0), py(414.12), px(14), py(-414.12), sw=2.2, color=BLUE))
    o.append(_line(px(0), py(555.3), px(14), py(-481.26), sw=2.2, color=RED))
    o.append(_line(410, 96, 436, 96, sw=2.4, color=BLUE))
    o.append(T(442, 100, "25 C: -59.16 mV/pH", 7.6, color=BLUE, anchor="start"))
    o.append(_line(410, 114, 436, 114, sw=2.4, color=RED))
    o.append(T(442, 118, "100 C: -74.04 mV/pH", 7.6, color=RED, anchor="start"))
    o.append(_circle(px(7), py(0), 4, fill=BLUE))
    o.append(_circle(px(7.5), py(0), 4, fill=RED))
    o.append(_arrow(px(7.05), 202, px(7.45), 202, sw=1.0, color=GREEN))
    o.append(T(326, 220, "pH° dich / shifts", 7.2, color=GREEN))
    o.append(T(330, 298, "he so doc / slope coefficient = 0.1984 mV/(K.pH)",
               8.0, color=INK))
    o.append(_foot(680, 360, "Nhiet do tang lam tang do doc va dich diem dang the pH° / "
                             "Rising temperature steepens the slope and shifts the isopotential pH°"))
    return _finish(o, w, h, "mV/pH relation at two temperatures",
        "Hình 4.1 · Quan hệ mV/pH ở hai nhiệt độ: đường dốc hơn ứng với nhiệt độ cao hơn "
        "(-74,04 mV/pH ở 100 C, so với -59,16 mV/pH ở 25 C). Điểm đẳng thế pH° dịch chuyển "
        "theo nhiệt độ; hệ số dốc là 0,1984 mV/(K.pH).",
        "Figure 4.1 · The mV/pH relation at two temperatures: the steeper line corresponds to "
        "the higher temperature (-74.04 mV/pH at 100 C versus -59.16 mV/pH at 25 C). The "
        "isopotential pH value shifts with temperature; the slope coefficient is 0.1984 mV/(K.pH).",
        "Biểu đồ E theo pH với hai đường thẳng ở 25 và 100 độ C, điểm đẳng thế dịch theo nhiệt độ",
        "Plot of E against pH with two straight lines at 25 and 100 degrees C, isopotential shift")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Typical glass indicator and calomel reference electrode constructions."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Cau tao dien cuc thuong gap / Typical electrode constructions",
               9.0, color=INK, weight="600"))
    o.append(_panel(24, 44, 300, 290, "Dien cuc thuỷ tinh / Glass indicator electrode"))
    o.append(_panel(356, 44, 300, 290, "Dien cuc tham chieu calomel / Calomel reference electrode"))
    # Glass indicator electrode.
    o.append(_rect(150, 74, 48, 130, fill="#eef3fb", sw=1.5))
    o.append(_rect(154, 96, 40, 106, fill="#dfeaf4", sw=0))
    o.append(_ellipse(174, 212, 30, 30, fill="#f6e6c8", sw=1.6))
    o.append(_ellipse(174, 212, 23, 23, fill="#dfeaf4", sw=1.0))
    o.append(_line(174, 78, 174, 198, sw=2.0, color=GREY))
    o.append(_rect(168, 196, 12, 16, fill="#4b4b4b", sw=0))
    o.append(_line(174, 58, 174, 74, sw=2.2, color=INK))
    o.append(T(174, 51, "day dan / lead", 7.0, color=GREY))
    # Calomel reference electrode.
    o.append(_rect(482, 74, 48, 130, fill="#eef3fb", sw=1.5))
    o.append(_rect(486, 96, 40, 106, fill="#dfeaf4", sw=0))
    o.append(_rect(494, 154, 24, 38, fill="#7d6b52", sw=1.0))
    o.append(_line(506, 78, 506, 154, sw=2.0, color=GREY))
    o.append(_ellipse(506, 212, 27, 27, fill="#f6e6c8", sw=1.5))
    o.append(_rect(498, 232, 16, 10, fill="#9a9a9a", sw=1.0))
    o.append(_line(506, 58, 506, 74, sw=2.2, color=INK))
    o.append(T(506, 51, "day dan / lead", 7.0, color=GREY))
    for args in [(150, 112, 1), (140, 186, 2), (208, 214, 3),
                 (478, 172, 4), (478, 122, 5), (534, 237, 6)]:
        o.append(_num(*args))
    o.append(_legend(["Dung dich trong pH 7 / internal solution",
                      "Ag/AgCl trong / internal element",
                      "Mang thuy tinh nhay pH / pH glass bulb",
                      "Calomel Hg/Hg2Cl2 / reference element",
                      "Dung dich KCl / KCl electrolyte",
                      "Cau muoi xop / porous salt bridge"], 40, 262, lh=11, size=7.1))
    o.append(_legend(["Bien / Variable", "Dien cuc / Electrode",
                      "Theo doi / Track", "Tham chieu / Reference",
                      "on dinh / Stable", "Dan ion / Ion path"],
                     372, 262, lh=11, size=7.1))
    o.append(_foot(680, 366, "Dien the sinh ra ty le voi chenh pH giua dung dich trong va mau / "
                             "The voltage is proportional to the pH difference across the membrane"))
    return _finish(o, w, h, "Typical electrode constructions",
        "Hình 4.2 · Cấu tạo điện cực thường gặp: (trái) điện cực thuỷ tinh chỉ thị gồm điện cực "
        "Ag/AgCl trong, dung dịch trong pH 7 và màng thuỷ tinh nhạy pH; (phải) điện cực tham chiếu "
        "calomel gồm cặp calomel, dung dịch KCl và cầu muối xốp.",
        "Figure 4.2 · Typical electrode constructions: (left) a glass indicator electrode with an "
        "internal Ag/AgCl element, pH 7 internal solution and pH-sensitive glass bulb; (right) a "
        "calomel reference electrode with a calomel element, KCl electrolyte and porous salt bridge.",
        "Điện cực thuỷ tinh và điện cực tham chiếu calomel với các bộ phận chính",
        "Glass indicator and calomel reference electrodes with their labelled parts")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Different glass electrodes for different applications."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Bon loai dien cuc thuỷ tinh / Glass electrodes for different uses",
               9.0, color=INK, weight="600"))
    specs = [
        (24, "Bong tron tieu chuan", "Standard rounded bulb", "rounded"),
        (194, "Kim nho / Slim needle", "Slim needle tip", "needle"),
        (364, "Mat phang / Flat", "Flat surface tip", "flat"),
        (534, "Dau ben / Rugged", "Rugged red tip", "rugged"),
    ]
    for x, vi, en, kind in specs:
        o.append(_panel(x, 44, 150, 266, vi))
        cx = x + 75
        o.append(_rect(cx - 12, 80, 24, 96, fill="#eef3fb", sw=1.4))
        o.append(_line(cx, 66, cx, 80, sw=2.0, color=INK))
        if kind == "rounded":
            o.append(_ellipse(cx, 188, 22, 24, fill="#f6e6c8", sw=1.5))
        elif kind == "needle":
            o.append(_poly([(cx - 12, 176), (cx + 12, 176), (cx + 4, 226), (cx - 4, 226)],
                           fill="#f6e6c8", sw=1.4, close=True))
        elif kind == "flat":
            o.append(_rect(cx - 22, 176, 44, 40, fill="#f6e6c8", sw=1.5))
            o.append(_line(cx - 22, 216, cx + 22, 216, sw=2.2, color=RED))
        else:
            o.append(_ellipse(cx, 190, 26, 28, fill="#e7938a", sw=1.6, color=RED))
            o.append(_rect(cx - 14, 80, 28, 12, fill="#c0392b", sw=0))
        o.append(T(cx, 242, vi, 7.6, color=INK))
        o.append(T(cx, 256, en, 7.0, color=GREY))
        o.append(T(cx, 288, "mau / sample", 6.8, color=BLUE))
    o.append(_foot(680, 340, "Chon hinh dang dau do theo mau: long, hat, be mat phang hoac "
                             "dieu kien co hoc khac nghiệt / Choose the tip shape to suit the sample"))
    return _finish(o, w, h, "Different glass electrodes for different applications",
        "Hình 4.3 · Bốn loại điện cực thuỷ tinh cho các ứng dụng khác nhau: bong tròn tiêu chuẩn, "
        "đầu kim nhỏ, đầu mặt phẳng để đo trực tiếp trên bề mặt và đầu bền mẫu đo trong điều kiện "
        "cơ học khắc nghiệt.",
        "Figure 4.3 · Four glass electrodes for different applications: a standard rounded bulb, "
        "a slim needle tip, a flat tip for direct surface measurement and a rugged red tip for "
        "mechanically harsh conditions.",
        "Bốn đầu đo thuỷ tinh: bong tròn, kim nhỏ, mặt phẳng và đầu bền",
        "Four glass tips: rounded bulb, slim needle, flat surface and rugged tip")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Liquid junction constructions with typical KCl outflow."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Cau tao moi chat long va luong KCl ra / Liquid junctions and KCl outflow",
               8.8, color=INK, weight="600"))
    items = [
        (60, "Chan xop", "Porous pin", "10 ul/h", "pin"),
        (180, "Hai cap", "Double junction", "10 ul/h", "double"),
        (300, "Vanh", "Annular", "10-100 ul/h", "annular"),
        (420, "Tay dao nguoc", "Reversed sleeve", "1 ml/h", "sleeve"),
        (540, "Soi", "Fibre", "<10 ul/h", "fibre"),
    ]
    for cx, vi, en, rate, kind in items:
        o.append(_rect(cx - 30, 90, 60, 118, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx - 26, 108, 52, 96, fill="#dfeaf4", sw=0))
        o.append(_line(cx, 74, cx, 90, sw=2.0, color=INK))
        if kind == "pin":
            o.append(_rect(cx - 10, 208, 20, 26, fill="#9a9a9a", sw=1.0))
        elif kind == "double":
            o.append(_rect(cx - 14, 196, 28, 20, fill="#f6e6c8", sw=1.0))
            o.append(_rect(cx - 10, 218, 20, 16, fill="#cfe0cf", sw=1.0))
        elif kind == "annular":
            o.append(_rect(cx - 16, 208, 32, 26, fill="#f6e6c8", sw=1.0))
            o.append(_line(cx - 20, 214, cx - 16, 230, sw=2.0, color=GREEN))
            o.append(_line(cx + 20, 214, cx + 16, 230, sw=2.0, color=GREEN))
        elif kind == "sleeve":
            o.append(_rect(cx - 18, 208, 36, 30, fill="#f6e6c8", sw=1.0))
            o.append(_line(cx - 18, 232, cx + 18, 232, sw=1.6, color=GREEN))
        else:
            o.append(_line(cx, 208, cx, 242, sw=3.0, color="#c08a2e"))
        o.append(_arrow(cx, 238, cx + 8, 266, sw=1.0, color=BLUE))
        o.append(T(cx, 292, vi, 7.8, color=INK, weight="600"))
        o.append(T(cx, 306, en, 7.0, color=GREY))
        o.append(T(cx, 326, "KCl: " + rate, 7.4, color=BLUE, weight="600"))
    o.append(_foot(680, 356, "Luong KCl ra nho giu cau muoi on dinh nhung van du dan ion / "
                             "A small KCl outflow keeps the junction stable yet conductive"))
    return _finish(o, w, h, "Liquid junction constructions with typical KCl outflow",
        "Hình 4.4 · Năm cấu tạo mối chất lỏng chân xốp, hai cấp, vành, tay đảo ngược và sợi, "
        "kèm lượng dung dịch KCl ra tiêu biểu: 10 ul/h, 10 ul/h, 10-100 ul/h, 1 ml/h và "
        "dưới 10 ul/h.",
        "Figure 4.4 · Five liquid junction constructions: porous pin, double junction, annular, "
        "reversed sleeve and fibre, with typical KCl outflows of 10 ul/h, 10 ul/h, 10-100 ul/h, "
        "1 ml/h and below 10 ul/h.",
        "Năm loại cầu muối và lượng KCl ra tương ứng",
        "Five liquid junction types and their typical KCl outflows")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Selection of the correct reference electrode for measuring conditions."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Chon dung dien cuc tham chieu / Selecting the reference electrode",
               9.0, color=INK, weight="600"))
    o.append(_rect(250, 44, 180, 46, fill="#e7eef7", sw=1.4))
    o.append(T(340, 64, "Mau va dieu kien / Sample", 8.8, color=INK, weight="600"))
    o.append(T(340, 80, "and measuring conditions", 7.4, color=BLUE))
    for tx in (124, 340, 556):
        o.append(_arrow(340, 90, tx, 122, sw=1.2, color=BLUE))
    panels = [
        (24, "Binh mau nho / Small vessel", "slim", "Dang nho de vao binh mau nho",
         "Slim stem for small sample vessels"),
        (240, "Dieu kien khac nghiệt / Harsh", "cap", "Than nhua va nap bao ve",
         "Plastic stem and protection cap"),
        (456, "Do tren be mat phang / Flat", "flat", "Dau phang ap len be mat",
         "Flat tip pressed onto a surface"),
    ]
    for x, title, kind, vi, en in panels:
        o.append(_panel(x, 124, 200, 200, title))
        cx = x + 100
        if kind == "slim":
            o.append(_rect(cx - 8, 158, 16, 96, fill="#eef3fb", sw=1.3))
            o.append(_ellipse(cx, 258, 14, 14, fill="#f6e6c8", sw=1.3))
        elif kind == "cap":
            o.append(_rect(cx - 16, 158, 32, 96, fill="#e6e8ea", sw=1.3))
            o.append(_rect(cx - 20, 250, 40, 20, fill="#9aa4ad", sw=1.2))
            o.append(_poly([(cx - 16, 158), (cx + 16, 158), (cx + 10, 146), (cx - 10, 146)],
                           fill="#cdd2d6", sw=1.0, close=True))
        else:
            o.append(_rect(cx - 14, 158, 28, 96, fill="#eef3fb", sw=1.3))
            o.append(_rect(cx - 26, 254, 52, 18, fill="#f6e6c8", sw=1.3))
        o.append(T(cx, 292, vi, 7.0, color=INK))
        o.append(T(cx, 306, en, 6.8, color=GREY))
    o.append(_rect(24, 338, 632, 44, fill="#fdf1e3", sw=1.0))
    o.append(T(340, 354, "Nhiet do cao: calomel chi den 60 C; dung Ag/AgCl thay the / "
                         "High temperature: calomel stops at 60 C, use Ag/AgCl instead",
               7.8, color=INK))
    o.append(T(340, 370, "pH cao va muoi cao can mang thuỷ tinh chong kiem / "
                         "High pH and high salt need alkali-resistant glass",
               7.4, color=GREY))
    o.append(_foot(680, 398, "Kich thuoc va binh mau quyet dinh kieu dien cuc; dieu kien dac biet "
                             "quyet dinh vat lieu va cau muoi / Vessel and conditions decide the type"))
    return _finish(o, w, h, "Selection of the correct reference electrode",
        "Hình 4.5 · Chọn điện cực theo điều kiện đo: bình mẫu nhỏ dùng điện cực dạng nhỏ; "
        "điều kiện khắc nghiệt dùng thân nhựa và nắp bảo vệ; đo trên bề mặt phẳng dùng đầu phẳng. "
        "Nhiệt độ trên 60 C không dùng calomel mà dùng Ag/AgCl.",
        "Figure 4.5 · Choosing a reference electrode: small vessels need a slim stem, harsh "
        "conditions need a plastic stem and protection cap, and flat surfaces need a flat tip. "
        "Above 60 C calomel is replaced by Ag/AgCl.",
        "Sơ đồ chọn điện cực theo bình mẫu, điều kiện khắc nghiệt và bề mặt phẳng",
        "Choice chart for sample vessels, harsh conditions and flat surfaces")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Double junction reference electrode, cutaway view."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dien cuc tham chieu hai cap / Double junction reference electrode",
               9.0, color=INK, weight="600"))
    o.append(_rect(236, 60, 128, 250, fill="#eef3fb", sw=1.8))
    o.append(_rect(240, 84, 120, 130, fill="#dfeaf4", sw=0))
    o.append(_rect(248, 104, 28, 92, fill="#cfe0cf", sw=1.0))
    o.append(_line(262, 66, 262, 104, sw=2.0, color=GREY))
    o.append(_rect(256, 100, 12, 14, fill="#4b4b4b", sw=0))
    o.append(_rect(240, 216, 120, 54, fill="#f6e6c8", sw=0))
    o.append(_rect(248, 270, 104, 26, fill="#e8dcc0", sw=1.0))
    o.append(_rect(276, 296, 48, 14, fill="#9a9a9a", sw=1.0))
    o.append(_line(300, 44, 300, 60, sw=2.2, color=INK))
    for args in [(290, 120, 1), (290, 236, 2), (290, 278, 3), (330, 304, 4)]:
        o.append(_num(*args))
    o.append(_bl(384, 108, "1. Dien tham chieu trong", "Inner reference element"))
    o.append(_bl(384, 162, "2. Cau muoi thu nhat (KCl)", "First salt bridge (KCl)"))
    o.append(_bl(384, 232, "3. Cau muoi thu hai", "Second salt bridge"))
    o.append(_bl(384, 288, "4. Moi chat long ngoai", "Outer liquid junction"))
    o.append(T(670, 338, "Cap hai khong chua KCl khi KCl can tro mau / "
                         "The second bridge avoids KCl when it interferes",
               7.2, color=GREEN, anchor="end"))
    o.append(_foot(680, 374, "Dung cau muoi thu hai de tranh tuy va nhieu voi mau / "
                             "A second bridge avoids precipitation and sample interference"))
    return _finish(o, w, h, "Double junction reference electrode",
        "Hình 4.6 · Điện cực tham chiếu hai cấp, cắt ngang: điện tham chiếu bên trong, cầu muối "
        "thứ nhất chứa KCl, cầu muối thứ hai không chứa KCl và mối chất lỏng ngoài. Cấp hai tránh "
        "tủy và cản trở khi KCl không dùng cho mẫu.",
        "Figure 4.6 · Cutaway of a double junction reference electrode: the inner reference "
        "element, a first KCl salt bridge, a second salt bridge without KCl and the outer liquid "
        "junction. The second bridge avoids precipitation and interference with the sample.",
        "Cắt ngang điện cực hai cấp với hai buồng cầu muối và mối ngoài",
        "Cutaway of a double junction electrode with two bridges and outer junction")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Simplified pH meter diagram."""
    w, h = 680, 360
    o = [_defs()]
    o.append(T(340, 26, "So do don gian cua may do pH / Simplified pH meter diagram",
               9.0, color=INK, weight="600"))
    o.append(_rect(40, 130, 128, 50, fill="#dfeaf4", sw=1.4))
    o.append(T(104, 150, "Dien cuc thuỷ tinh", 8.0, color=INK))
    o.append(T(104, 168, "Glass electrode", 7.6, color=BLUE))
    o.append(_rect(40, 212, 128, 50, fill="#f6e6c8", sw=1.4))
    o.append(T(104, 232, "Dien cuc tham chieu", 8.0, color=INK))
    o.append(T(104, 250, "Reference electrode", 7.6, color=GREEN))
    o.append(_arrow(168, 155, 212, 180, sw=1.3, color=BLUE))
    o.append(_arrow(168, 237, 212, 212, sw=1.3, color=GREEN))
    o.append(_rect(214, 162, 150, 66, fill="#eef3fb", sw=1.6))
    o.append(T(289, 186, "Khuếch dai mV", 8.6, color=INK, weight="600"))
    o.append(T(289, 204, "mV amplifier", 7.8, color=BLUE))
    o.append(T(289, 220, "Zin > 10^12 ohm", 7.0, color=GREY))
    o.append(_arrow(364, 195, 398, 195, sw=1.3, color=INK))
    o.append(_rect(400, 172, 84, 46, fill="#fdf3e6", sw=1.4))
    o.append(T(442, 194, "A/D", 10, color=INK, weight="600"))
    o.append(T(442, 210, "do chuyen doi", 6.8, color=GREY))
    o.append(_arrow(484, 195, 520, 195, sw=1.3, color=INK))
    o.append(_rect(522, 166, 118, 58, fill="#e6f4ee", sw=1.4))
    o.append(T(581, 189, "Man hinh / Display", 8.2, color=INK, weight="600"))
    o.append(T(581, 208, "pH 7.00", 9.0, color=GREEN))
    o.append(T(40, 100, "Tin hieu cao ap, dong rat nho / High-impedance, tiny signal",
               7.4, color=RED, anchor="start"))
    o.append(_line(104, 108, 104, 128, sw=1.0, color=RED))
    o.append(_foot(680, 290, "Dat may va vỏ kim loai cung mot diem; day guard bao ve duong tin "
                             "hieu / Earth the meter and guard the high-impedance input"))
    o.append(_foot(680, 312, "Tro khang dau vao lon tranh tai dien tich va nhieu / "
                             "High input impedance avoids loading the electrode"))
    return _finish(o, w, h, "Simplified pH meter diagram",
        "Hình 4.7 · Sơ đồ máy đo pH đơn giản: điện cực thuỷ tinh và điện cực tham chiếu đưa tín "
        "hiệu vào bộ khuếch đại mV có trở kháng đầu vào rất lớn, qua bộ A/D đến màn hình. Cần nối "
        "đất và dây guard cho đường tín hiệu.",
        "Figure 4.7 · A simplified pH meter: the glass and reference electrodes feed a mV "
        "amplifier with very high input impedance, then an A/D converter and a display. Proper "
        "earthing and a guard trace protect the high-impedance signal.",
        "Luồng tín hiệu từ điện cực qua khuếch đại, A/D đến màn hình",
        "Signal path from electrodes through amplifier and A/D to the display")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """PHM240 pH/Ion Meter for high-precision pH measurements."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "May do pH/Ion PHM240 / PHM240 pH/Ion Meter",
               9.0, color=INK, weight="600"))
    o.append(_rect(56, 56, 568, 254, fill="#eceff2", sw=2.0, stroke="#7f8a94"))
    o.append(_rect(68, 68, 544, 230, fill="#f8f9fa", sw=1.0))
    o.append(T(96, 92, "PHM240", 12, color=INK, weight="600", anchor="start"))
    o.append(T(180, 92, "pH / Ion Meter - do chinh xac cao / high precision",
               7.6, color=GREY, anchor="start"))
    o.append(_rect(92, 108, 236, 92, fill="#0f2418", sw=1.2))
    o.append(T(210, 140, "pH  7.00", 18, color="#9fe870", anchor="middle"))
    o.append(T(210, 168, "25.0 C   mV  0.02", 9.0, color="#7fc98a"))
    o.append(T(210, 188, "AUTO CAL / auto calibration", 7.0, color="#7fc98a"))
    for r in range(3):
        for c in range(4):
            o.append(_rect(96 + c * 56, 218 + r * 22, 46, 16,
                           fill="#dfe3e6", sw=0.8))
    o.append(T(210, 292, "Ban phim / keypad", 7.0, color=GREY))
    o.append(T(372, 118, "Cong ket noi / Connectors", 8.2, color=INK, weight="600",
               anchor="start"))
    conns = [(384, 150, "pH / BNC"), (384, 196, "REF"), (384, 242, "TEMP")]
    for cx, cy, lab in conns:
        o.append(_circle(cx, cy, 15, fill="#3a3f44", sw=1.2))
        o.append(_circle(cx, cy, 6, fill="#c9ced2", sw=0.8))
        o.append(T(cx + 26, cy + 3, lab, 7.6, color=INK, anchor="start"))
    o.append(_rect(470, 132, 120, 132, fill="#eef3fb", sw=1.0))
    o.append(T(530, 152, "RS-232 / USB", 7.6, color=INK, weight="600"))
    o.append(T(530, 172, "may tinh / PC", 7.0, color=GREY))
    o.append(_line(486, 190, 574, 190, sw=1.0, color=GREY))
    o.append(T(530, 208, "dau ra / output", 7.0, color=GREY))
    o.append(T(530, 232, "Calibration", 7.4, color=BLUE))
    o.append(T(530, 248, "1 / 2 / 3 points", 7.0, color=GREY))
    o.append(_foot(680, 350, "So do mat truoc don gian, khong phai ban sao logo / "
                             "Simplified front panel, not a logo copy"))
    o.append(_foot(680, 372, "May de ban dung do pH va nong do ion voi do phan giai cao / "
                             "Benchtop meter for high-resolution pH and ion measurement"))
    return _finish(o, w, h, "PHM240 pH/Ion Meter for high-precision pH measurements",
        "Hình 4.8 · Mặt trước máy đo pH/Ion PHM240 dạng để bàn: màn hình hiển thị giá trị pH và "
        "nhiệt độ, bàn phím hiệu chuẩn, các cổng BNC pH, tham chiếu, đầu đo nhiệt độ và cổng "
        "máy tính. Đây là sơ đồ đơn giản, không phải bản sao logo.",
        "Figure 4.8 · Schematic front panel of the benchtop PHM240 pH/Ion Meter: a display of pH "
        "and temperature, a calibration keypad and connectors for pH/BNC, reference, temperature "
        "probe and a PC port. This is a simplified diagram, not a logo copy.",
        "Mặt trước máy đo pH với màn hình, bàn phím và các cổng kết nối",
        "Front panel of a pH meter with display, keypad and connectors")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """IUPAC Series certified standards in bottles placed in tins."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Chuan IUPAC hop cứng / IUPAC standards in tins",
               9.0, color=INK, weight="600"))
    vals = ["1.68", "4.01", "7.00", "10.01"]
    for i, val in enumerate(vals):
        x = 50 + i * 150
        o.append(_rect(x, 120, 112, 150, fill="#c9d2d9", sw=1.6))
        o.append(_line(x, 142, x + 112, 142, sw=1.0, color="#7f8a94"))
        o.append(_rect(x + 8, 154, 96, 106, fill="#eef3fb", sw=1.0))
        o.append(_rect(x + 40, 168, 32, 78, fill="#fbfaf7", sw=1.3))
        o.append(_rect(x + 45, 154, 22, 14, fill="#b45309", sw=1.0))
        o.append(_line(x + 56, 154, x + 56, 142, sw=1.0, color=GREY))
        o.append(T(x + 56, 214, val, 11, color=INK, weight="600"))
        o.append(T(x + 56, 230, "pH", 8.0, color=BLUE))
        o.append(T(x + 56, 290, "hop / tin", 7.6, color=INK))
        o.append(T(x + 56, 304, "chuan / standard", 7.0, color=GREY))
    o.append(T(340, 332, "Chai nhua day hop kim loai giu tuoi tho cao / "
                         "Thick plastic dropper bottles in tins assure long shelf life",
               8.0, color=INK))
    o.append(T(340, 350, "Dung dich dem chuẩn according to IUPAC Series / "
                         "IUPAC Series certified buffer standards",
               7.6, color=GREY))
    o.append(_foot(680, 370, "Hieu chuan may bang it nhat hai dung dich dem bao phu khoang do / "
                             "Calibrate with at least two buffers bracketing the sample pH"))
    return _finish(o, w, h, "IUPAC Series certified standards in bottles placed in tins",
        "Hình 4.9 · Bốn chuẩn đệm IUPAC trong chai nhựa dày có nút nhã giác, đặt trong hộp "
        "cứng: pH 1,68; 4,01; 7,00 và 10,01. Hộp và chai dày giữ tuổi thọ và ổn định dung dịch.",
        "Figure 4.9 · IUPAC Series certified buffer standards in thick plastic dropper bottles "
        "placed in tins, labelled pH 1.68, 4.01, 7.00 and 10.01. The thick bottles and tins assure "
        "a long shelf life.",
        "Bốn chai chuẩn đệm pH trong hộp cứng",
        "Four buffer standard bottles in tins labelled pH values")


# ---------------------------------------------------------------------------
@_reg
def fig_f10():
    """Typical pH glass electrode with ion exchange at the membrane."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Dien cuc thuỷ tinh pH va trao doi ion / Typical pH glass electrode",
               9.0, color=INK, weight="600"))
    o.append(_rect(70, 70, 46, 180, fill="#eef3fb", sw=1.5))
    o.append(_rect(74, 92, 38, 156, fill="#dfeaf4", sw=0))
    o.append(_line(93, 74, 93, 196, sw=2.0, color=GREY))
    o.append(_rect(87, 194, 12, 16, fill="#4b4b4b", sw=0))
    o.append(_ellipse(93, 252, 32, 34, fill="#f6e6c8", sw=1.6))
    o.append(_ellipse(93, 252, 24, 26, fill="#dfeaf4", sw=1.0))
    o.append(_line(93, 54, 93, 70, sw=2.2, color=INK))
    for args in [(50, 120, 1), (50, 196, 2), (132, 250, 3), (140, 300, 4)]:
        o.append(_num(*args))
    o.append(_bl(160, 104, "1. Dien Ag/AgCl trong", "Internal Ag/AgCl element"))
    o.append(_bl(160, 166, "2. Dung dich dem pH 7", "pH 7 fill solution"))
    o.append(_bl(160, 228, "3. Mang thuỷ tinh", "Glass membrane"))
    o.append(_bl(160, 288, "4. Mau can do", "Sample side"))
    o.append(_panel(360, 60, 296, 300, "Phat lon mang / Magnified membrane"))
    o.append(_rect(392, 108, 232, 44, fill="#e6f4ee", sw=1.0))
    o.append(_rect(392, 152, 232, 44, fill="#f6e6c8", sw=1.0))
    o.append(_rect(392, 196, 232, 44, fill="#dfeaf4", sw=1.0))
    o.append(T(508, 132, "lớp gel trong / inner gel layer", 7.4, color=GREEN))
    o.append(T(508, 176, "mang thuỷ tinh / glass membrane", 7.4, color=INK))
    o.append(T(508, 220, "lớp gel ngoai / outer gel layer", 7.4, color=BLUE))
    o.append(_arrow(430, 178, 430, 208, sw=1.4, color=RED))
    o.append(_arrow(586, 208, 586, 178, sw=1.4, color=RED))
    o.append(T(508, 264, "H+ doi ion giua hai mat / H+ ion exchange at both faces",
               7.6, color=RED))
    o.append(T(508, 290, "E ty le chenh pH / E depends on the pH difference", 7.4, color=GREY))
    o.append(T(508, 318, "Asymmetry co the xuat hien / asymmetry may appear",
               7.0, color=GREY))
    o.append(_foot(680, 384, "Lop gel ngam nuoc trao doi H+ voi dung dich; ion kiem cua thuy tinh "
                             "gioi han do doc / The hydrated gel exchanges H+ with the solution"))
    return _finish(o, w, h, "Typical pH Glass Electrode",
        "Hình 4.10 · Điện cực thuỷ tinh pH tiêu biểu: bộ phận Ag/AgCl trong, dung dịch đệm pH 7, "
        "màng thuỷ tinh và phía mẫu. Phóng to màng cho thấy lớp gel ngậm nước trao đổi ion H+ ở "
        "hai mặt, tạo điện thế tỷ lệ chênh pH.",
        "Figure 4.10 · A typical pH glass electrode: internal Ag/AgCl element, pH 7 fill solution, "
        "glass membrane and sample side. The magnified inset shows hydrated gel layers exchanging "
        "H+ ions at both faces, producing a voltage proportional to the pH difference.",
        "Điện cực thuỷ tinh và phóng to màng trao đổi ion H+",
        "Glass electrode and magnified membrane with H+ ion exchange")


# ---------------------------------------------------------------------------
@_reg
def fig_f11():
    """pH-electrode transfer function."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Ham truyen cua dien cuc pH / pH-electrode transfer function",
               9.0, color=INK, weight="600"))
    x0, y0, W, H = 96, 66, 456, 236

    def px(p):
        return x0 + p / 14.0 * W

    def py(e):
        return y0 + (550.0 - e) / 900.0 * H

    for pv in (0, 7, 14):
        o.append(_line(px(pv), y0, px(pv), y0 + H, sw=0.6, color="#d5dbe0"))
        o.append(T(px(pv), y0 + H + 15, str(pv), 7.8, color=GREY))
    for ev in (500, 0, -300):
        o.append(_line(x0, py(ev), x0 + W, py(ev), sw=0.6, color="#d5dbe0"))
        o.append(T(x0 - 6, py(ev) + 3, str(ev), 7.2, color=GREY, anchor="end"))
    o.append(_line(x0, y0 + H, x0 + W + 10, y0 + H, sw=1.3))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.3))
    o.append(T(x0 + W + 22, y0 + H + 15, "pH", 8.4, color=INK, anchor="end"))
    o.append(T(x0 + 4, y0 - 14, "E (mV)", 8.4, color=INK))
    o.append(_line(px(0), py(512), px(14), py(512 - 59.16 * 14), sw=2.4, color=BLUE))
    o.append(_circle(px(0), py(512), 4, fill=RED))
    o.append(T(px(0) + 10, py(512) - 4, "512 mV bias", 7.6, color=RED, anchor="start"))
    o.append(T(400, 150, "do doc / slope = -59.16 mV/pH at 25 C",
               7.8, color=BLUE))
    o.append(T(400, 172, "E = 512 - 59.16 x pH", 8.6, color=INK, weight="600"))
    o.append(T(400, 194, "dien the giam khi pH tang / voltage falls as pH rises",
               7.2, color=GREY))
    o.append(_foot(680, 330, "Dien cuc ly tuong cho 0 mV o pH 7; thuc te co sai so lech va do "
                             "doc can hieu chuan / Ideal gives 0 mV at pH 7; real offset and span "
                             "errors need calibration"))
    o.append(_foot(680, 352, "Do doc tang theo nhiet do nen can bu nhiet / "
                             "Slope rises with temperature, so compensation is required"))
    return _finish(o, w, h, "pH-Electrode Transfer Function",
        "Hình 4.11 · Hàm truyền của điện cực pH: đường thẳng giảm, độ dốc khoảng -59,16 mV/pH "
        "ở 25 C. Điện thế giảm khi pH tăng, bắt đầu khoảng 512 mV (điện áp lệch trong mạch) và "
        "cần bù nhiệt vì độ dốc đổi theo nhiệt độ.",
        "Figure 4.11 · The pH-electrode transfer function: a falling straight line with a slope "
        "of about -59.16 mV/pH at 25 C. Voltage decreases as pH rises, starting near the 512 mV "
        "bias used in the circuit; temperature compensation is needed because the slope varies.",
        "Đường thẳng giảm của điện thế theo pH, dốc -59 mV/pH",
        "Falling straight line of voltage versus pH with -59 mV/pH slope")


# ---------------------------------------------------------------------------
@_reg
def fig_f12():
    """pH scale 0-14 with the tenfold-per-unit annotation."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 26, "Thang pH 0-14 / The pH scale 0-14",
               9.0, color=INK, weight="600"))
    cols = ["#c0392b", "#cb4335", "#d35400", "#e67e22", "#d4ac0d", "#b8b31a", "#8bb615",
            "#27ae60", "#1abc9c", "#16a085", "#2980b9", "#2471a3", "#6c3483", "#8e44ad"]
    x0, bw = 28, 44
    for i in range(14):
        o.append(_rect(x0 + i * bw, 110, bw, 48, fill=cols[i], sw=0.6, stroke="#ffffff"))
        o.append(T(x0 + i * bw + bw / 2, 176, str(i), 8.0, color=INK))
    o.append(_line(x0 - 6, 158, x0 + 14 * bw + 6, 158, sw=0))
    o.append(T(x0 + 7 * bw, 96, "7 = trung tính / neutral", 8.6, color=INK, weight="600"))
    o.append(_arrow(x0 + 7 * bw, 100, x0 + 7 * bw, 108, sw=1.2, color=INK))
    o.append(T(x0 + 3 * bw, 200, "Chua / Acidic (H+ cao)", 8.0, color=RED, weight="600"))
    o.append(T(x0 + 11 * bw, 200, "Kiem / Alkaline (OH- cao)", 8.0, color=BLUE, weight="600"))
    o.append(_rect(150, 224, 380, 56, fill="#eef3fb", sw=1.2))
    o.append(T(340, 244, "Moi don vi pH doi nong do H+ mot lan 10x / "
                         "Each pH unit changes [H+] by a factor of 10",
               8.0, color=INK, weight="600"))
    o.append(T(340, 266, "pH = -log10[H+]; [H+] tang 10 lan khi pH giam 1 / "
                         "tenfold per unit step", 7.4, color=GREY))
    o.append(_foot(680, 310, "pH 0 = acid manh, pH 14 = base manh, pH 7 = trung tính / "
                             "0 strong acid, 14 strong base, 7 neutral"))
    return _finish(o, w, h, "pH Scale",
        "Hình 4.12 · Thang pH từ 0 đến 14: bên trái là chua (H+ cao), bên phải là kiềm "
        "(OH- cao), pH 7 là trung tính. Mỗi đơn vị thay đổi nồng độ H+ một lần 10 theo "
        "pH = -log10[H+].",
        "Figure 4.12 · The pH scale runs from 0 to 14: acidic (high H+) on the left, alkaline "
        "(high OH-) on the right, with pH 7 neutral. Each unit changes the H+ concentration "
        "tenfold according to pH = -log10[H+].",
        "Thang màu pH 0 đến 14 với pH 7 ở giữa và các bước 10 lần",
        "Colour band pH 0 to 14 with neutral 7 and tenfold steps")


# ---------------------------------------------------------------------------
@_reg
def fig_f13():
    """Optimum pH-electrode circuit with a 512 mV bias."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Mach dien cuc pH toi uu / Optimum pH-electrode circuit",
               9.0, color=INK, weight="600"))
    o.append(_rect(40, 96, 92, 40, fill="#fdf3e6", sw=1.4))
    o.append(T(86, 112, "1.024 V", 8.6, color=INK, weight="600"))
    o.append(T(86, 128, "ref LM4140", 6.8, color=GREY))
    o.append(_line(86, 136, 86, 150, sw=1.2, color=INK))
    o.append(_rect(74, 150, 24, 22, fill="#eef3fb", sw=1.0))
    o.append(T(86, 165, "10k", 6.8, color=INK))
    o.append(_rect(74, 176, 24, 22, fill="#eef3fb", sw=1.0))
    o.append(T(86, 191, "10k", 6.8, color=INK))
    o.append(_line(86, 198, 86, 214, sw=1.2, color=INK))
    o.append(T(120, 182, "512 mV", 7.6, color=RED, anchor="start"))
    o.append(_poly([(214, 108), (214, 188), (292, 148)],
                   fill="#e6f4ee", sw=1.6, close=True))
    o.append(T(250, 140, "U1", 9.0, color=INK, weight="600"))
    o.append(T(250, 158, "buffer", 6.8, color=GREY))
    o.append(_line(86, 214, 214, 214, sw=1.2, color=RED))
    o.append(_line(86, 214, 214, 170, sw=1.2, color=RED))
    o.append(_arrow(292, 148, 340, 148, sw=1.2, color=RED))
    o.append(T(318, 138, "REF", 7.0, color=RED))
    o.append(_rect(40, 250, 110, 44, fill="#dfeaf4", sw=1.4))
    o.append(T(95, 268, "Dien cuc pH", 8.0, color=INK))
    o.append(T(95, 284, "pH electrode", 7.0, color=BLUE))
    o.append(_arrow(150, 272, 396, 272, sw=1.4, color=BLUE))
    o.append(_poly([(398, 234), (398, 314), (476, 274)],
                   fill="#dfeaf4", sw=1.6, close=True))
    o.append(T(434, 266, "U2", 9.0, color=INK, weight="600"))
    o.append(T(434, 284, "buffer", 6.8, color=GREY))
    o.append(_arrow(476, 274, 528, 274, sw=1.4, color=BLUE))
    o.append(_rect(530, 250, 124, 48, fill="#e6f4ee", sw=1.4))
    o.append(T(592, 270, "VOUT", 8.6, color=INK, weight="600"))
    o.append(T(592, 288, "VpH + 512 mV", 8.0, color=GREEN))
    o.append(_line(526, 274, 526, 320, sw=0))
    o.append(_path("M470,274 L470,336 L434,336 L434,314", sw=1.0, color=GREY))
    o.append(_path("M250,188 L250,206 L292,206 L292,158", sw=1.0, color=GREY))
    o.append(T(340, 360, "U1 offset 512 mV; U2 buffer unity-gain; Zin rat lon / "
                         "U1 biases by 512 mV, U2 buffers at unity gain, high Zin",
               7.8, color=INK))
    o.append(_foot(680, 392, "Chuyen tinh hieu hai cuc thanh don cuc dung cho nguon mot chieu / "
                             "Level-shifts the bipolar sensor signal for a single supply"))
    return _finish(o, w, h, "pH-Electrode Circuit",
        "Hình 4.13 · Mạch điện cực pH: bộ đệm 1,024 V chia đôi bằng hai điện trở 10k tạo "
        "512 mV, bộ đệm U1 (theo dõi đơn vị) phân cực tham chiếu; U2 cũng là bộ đệm đơn vị "
        "đọc đầu ra. Kết quả VOUT = VpH + 512 mV, trở kháng đầu vào rất lớn.",
        "Figure 4.13 · The pH-electrode circuit: a 1.024 V reference divided by two 10 kohm "
        "resistors gives 512 mV; unity-gain buffer U1 biases the reference electrode and U2 "
        "buffers the output, so VOUT = VpH + 512 mV with a very high input impedance.",
        "Mach U1 lech 512 mV va U2 dem don vi ra VOUT",
        "Circuit with U1 512 mV bias and unity-gain U2 output buffer")


# ---------------------------------------------------------------------------
@_reg
def fig_f14():
    """Circuit board guard layout around the op-amp input pins."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Bố trí guard tren ban mach / Circuit board guard layout",
               9.0, color=INK, weight="600"))
    o.append(_rect(224, 70, 232, 232, fill="#e9e3d6", sw=1.8))
    o.append(_poly([(292, 104), (292, 196), (388, 150)],
                   fill="#dfeaf4", sw=1.6, close=True))
    o.append(T(340, 146, "op-amp", 8.4, color=INK, weight="600"))
    for i in range(4):
        px = 244 + i * 56
        o.append(_rect(px, 46, 22, 24, fill="#c08a2e", sw=1.0))
        o.append(_rect(px, 302, 22, 24, fill="#c08a2e", sw=1.0))
        o.append(T(px + 11, 40, "P%d" % (i + 1), 6.8, color=GREY))
        o.append(T(px + 11, 340, "P%d" % (i + 5), 6.8, color=GREY))
    o.append(_path("M250,92 L250,282 L430,282 L430,92 Z",
                   sw=1.8, color=GREEN, dash="6 4"))
    o.append(_rect(250, 92, 44, 60, fill="none", sw=2.0, stroke=GREEN))
    o.append(_line(244, 190, 268, 190, sw=2.0, color=GREEN))
    o.append(_line(244, 214, 292, 214, sw=2.0, color=GREEN))
    o.append(T(340, 372, "Vong guard bao quanh chan vao, cach chan nguon va chan ra / "
                         "The guard ring surrounds the input pins, away from supply and output",
               7.8, color=INK))
    o.append(T(488, 110, "Vong guard / Guard ring", 7.8, color=GREEN, anchor="start"))
    o.append(T(488, 130, "dat dien the bang tin hieu /", 7.0, color=GREY, anchor="start"))
    o.append(T(488, 142, "driven at signal potential", 7.0, color=GREY, anchor="start"))
    o.append(T(488, 166, "Chan vao / Input pins P2-P3", 7.8, color=GREEN, anchor="start"))
    o.append(T(488, 186, "giam rò va nhieu / minimise leakage", 7.0, color=GREY,
               anchor="start"))
    o.append(T(488, 222, "Chan nguon / Supply pins", 7.8, color=RED, anchor="start"))
    o.append(T(488, 242, "nam ngoai vong guard / kept outside the ring",
               7.0, color=GREY, anchor="start"))
    o.append(T(488, 278, "Chan ra / Output pin", 7.8, color=BLUE, anchor="start"))
    o.append(T(488, 298, "khong di qua vung input /", 7.0, color=GREY, anchor="start"))
    o.append(T(488, 310, "not routed through input area", 7.0, color=GREY, anchor="start"))
    return _finish(o, w, h, "Circuit Board Guard Layout",
        "Hình 4.14 · Bo tri guard tren ban mach: mot vong/dường guard dat quanh chan vao cua "
        "op-amp, o dien the tin hieu de chong ro va nhieu; chan nguon va chan ra dat ben ngoai "
        "vung guard.",
        "Figure 4.14 · Circuit board guard layout: a guard ring and trace surround the op-amp "
        "input pins and are driven at the signal potential to reduce leakage and noise; supply and "
        "output pins are kept outside the guarded area.",
        "So chan op-amp co vong guard quanh chan vao",
        "Op-amp pinout with a guard ring around the input pins")


# ---------------------------------------------------------------------------
@_reg
def fig_f15():
    """System for defining Newtonian viscosity."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dinh nghia do nhot Newton / Defining Newtonian viscosity",
               9.0, color=INK, weight="600"))
    o.append(_rect(110, 276, 460, 16, fill="#9aa4ad", sw=1.2))
    o.append(_rect(110, 104, 460, 16, fill="#9aa4ad", sw=1.2))
    o.append(_rect(112, 120, 456, 156, fill="#dfeaf4", sw=0))
    o.append(T(340, 308, "Ban duoi co dinh / lower plate fixed", 7.8, color=GREY))
    o.append(_arrow(456, 92, 596, 92, sw=2.0, color=RED))
    o.append(T(526, 82, "Luc F / Force F", 8.0, color=RED))
    o.append(_arrow(456, 116, 596, 116, sw=1.8, color=BLUE))
    o.append(T(526, 130, "Van toc U / velocity U", 7.8, color=BLUE))
    for k in range(6):
        yy = 258 - k * 26
        frac = k / 5.0
        ln = 20 + frac * 150
        xx = 130
        o.append(_line(xx, yy, xx, yy, sw=0))
        o.append(_arrow(xx, yy, xx + ln, yy, sw=1.2, color=GREEN))
    o.append(_circle(130, 258, 3, fill=INK))
    o.append(T(292, 190, "phan bo van toc tuyen tinh / linear velocity profile",
               7.6, color=GREEN))
    o.append(_line(110, 120, 110, 276, sw=1.2, color=INK))
    o.append(_arrow(96, 276, 96, 120, sw=1.0, color=GREY))
    o.append(T(86, 198, "z", 8.0, color=GREY))
    o.append(T(340, 350, "dUx/dz = U/h ;  tau = mu x dUx/dz", 9.0, color=INK, weight="600"))
    o.append(_foot(680, 382, "Luc keo mat tren tao gradient van toc; ung suat ty le gradient / "
                             "Force on the upper plate sets the gradient; shear stress is proportional"))
    return _finish(o, w, h, "System for defining Newtonian viscosity",
        "Hình 4.15 · He thong dinh nghia do nhot Newton: hai ban song song, ban duoi co dinh, "
        "ban tren chiu luc F va chuyen dong voi van toc U. Phan bo van toc trong chat long la "
        "tuyen tinh, gradient dUx/dz va ung suat tau = mu.dUx/dz.",
        "Figure 4.15 · The system defining Newtonian viscosity: two parallel plates, the lower "
        "one fixed and the upper dragged by force F at velocity U. The velocity profile is linear; "
        "the shear stress is tau = mu times dUx/dz.",
        "Hai ban song song voi phan bo van toc tuyen tinh",
        "Two parallel plates with a linear velocity profile")


# ---------------------------------------------------------------------------
@_reg
def fig_f16():
    """Rotating cylinder viscometer nomenclature."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Nhom danh phap do nhot quay / Rotating cylinder viscometer",
               8.8, color=INK, weight="600"))
    o.append(_rect(170, 80, 250, 250, fill="#fbfaf7", sw=2.0))
    o.append(_rect(176, 118, 238, 206, fill="#dfeaf4", sw=0))
    o.append(_rect(246, 96, 98, 200, fill="#eef3fb", sw=1.8))
    o.append(_line(295, 60, 295, 96, sw=2.2, color=GREY))
    o.append(_path("M150,96 A150,150 0 0 1 210,72", sw=1.6, color=RED))
    o.append(_arrow(210, 72, 224, 84, sw=1.6, color=RED))
    o.append(T(160, 78, "co quay / cup rotates", 7.4, color=RED, anchor="start"))
    o.append(_arrow(360, 130, 360, 220, sw=1.6, color=GREEN))
    o.append(T(372, 176, "mo-men xoay / torque", 7.2, color=GREEN, anchor="start"))
    o.append(_line(246, 214, 246, 250, sw=1.2, color=BLUE))
    o.append(_line(344, 214, 344, 250, sw=1.2, color=BLUE))
    o.append(T(470, 122, "R2: ban kinh coc ngoai / outer cup radius", 7.4, color=INK,
               anchor="start"))
    o.append(T(470, 150, "R1: ban kinh trong / inner radius", 7.4, color=INK, anchor="start"))
    o.append(T(470, 178, "L: chieu dai hinh tru / cylinder length", 7.4, color=INK,
               anchor="start"))
    o.append(T(470, 206, "d = R2 - R1: khe chat long / fluid gap", 7.4, color=INK,
               anchor="start"))
    o.append(T(470, 246, "tau = M / (2.pi.R1^2.L)", 8.4, color=GREEN, anchor="start"))
    o.append(T(470, 268, "do nhot tu mo-men va toc do /", 7.0, color=GREY, anchor="start"))
    o.append(T(470, 280, "viscosity from torque and speed", 7.0, color=GREY, anchor="start"))
    o.append(T(470, 314, "Chat long nam trong khe /", 7.4, color=BLUE, anchor="start"))
    o.append(T(470, 326, "fluid in the annular gap", 7.4, color=BLUE, anchor="start"))
    o.append(_foot(680, 374, "Hinh tru trong duoc treo, coc ngoai quay deo chat long / "
                             "Inner cylinder suspended, outer cup rotated to shear the fluid"))
    return _finish(o, w, h, "Schematic nomenclature of a rotating cylinder viscometer",
        "Hình 4.16 · So danh phap may do nhot hinh tru quay: coc ngoai quay quanh hinh tru "
        "trong duoc treo, chat long nam trong khe d = R2 - R1. Ghi ban kinh R1, R2, chieu dai "
        "L, mo-men xoay va cong thuc tau = M/(2.pi.R1^2.L).",
        "Figure 4.16 · Nomenclature of a rotating cylinder viscometer: the outer cup rotates "
        "around a suspended inner cylinder with fluid in the gap d = R2 - R1. Radii R1 and R2, "
        "length L, applied torque and tau = M/(2*pi*R1^2*L) are indicated.",
        "Coc ngoai quay quanh tru trong voi khe chat long",
        "Outer cup rotating around an inner cylinder with a fluid gap")


# ---------------------------------------------------------------------------
@_reg
def fig_f17():
    """Falling sphere viscometer in a constant-temperature bath."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "May do nhot qua cau roi / Falling sphere viscometer",
               9.0, color=INK, weight="600"))
    o.append(_rect(180, 52, 240, 314, fill="#e6f4ee", sw=1.6))
    o.append(_rect(250, 68, 100, 282, fill="#dfeaf4", sw=1.4))
    o.append(T(300, 62, "bon on nhiet / constant-T bath 25 C", 7.4, color=GREEN))
    o.append(_circle(300, 172, 14, fill="#c08a2e", sw=1.2))
    o.append(_arrow(300, 196, 300, 244, sw=1.6, color=RED))
    o.append(T(316, 222, "v", 9.0, color=RED, anchor="start"))
    o.append(_line(286, 158, 314, 158, sw=1.0, color=INK))
    o.append(T(322, 152, "d", 8.0, color=INK, anchor="start"))
    o.append(_line(252, 110, 348, 110, sw=1.0, color=BLUE))
    o.append(T(360, 114, "D", 8.0, color=BLUE, anchor="start"))
    o.append(_line(244, 120, 244, 316, sw=1.0, color=GREY))
    o.append(_arrow(232, 316, 232, 120, sw=1.0, color=GREY))
    o.append(T(226, 218, "L", 8.0, color=GREY))
    o.append(_bl(448, 112, "Ong tiet dien khong doi", "Constant-area tube"))
    o.append(_bl(448, 170, "Qua cau roi voi van toc v", "Sphere falling at velocity v"))
    o.append(_bl(448, 228, "D: duong kính ong, d: duong kính cau", "Tube and sphere diameters"))
    o.append(_bl(448, 286, "L: quang duong roi; bon on nhiet", "Fall length; temperature bath"))
    o.append(T(448, 344, "mu = (g L (rho_s - rho_f) d^2) / (18 v)",
               8.0, color=GREEN, anchor="start"))
    o.append(_foot(680, 386, "Van toc cuoi cua qua cau cho biet do nhot theo dinh luat Stokes / "
                             "The terminal sphere velocity gives viscosity by Stokes' law"))
    return _finish(o, w, h, "Schematic diagram of a falling sphere viscometer",
        "Hình 4.17 · So do may do nhot qua cau roi: ong tiet dien dat trong bon on nhiet, "
        "qua cau duong kính roi voi van toc cuoi v. Ghi duong kính ong D, duong kính cau d "
        "va quang duong L; do nhot tinh theo dinh luat Stokes.",
        "Figure 4.17 · A falling sphere viscometer: a constant-area tube sits in a "
        "constant-temperature bath and a sphere of diameter d falls at terminal velocity v. Tube "
        "diameter D and fall distance L are marked; viscosity follows Stokes' law.",
        "Ong trong bon on nhiet voi qua cau roi va cac kich thuoc",
        "Tube in a temperature bath with a falling sphere and dimensions")


# ---------------------------------------------------------------------------
@_reg
def fig_f18():
    """Capillary tube viscometer."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "May do nhot ong mao dan / Capillary tube viscometer",
               9.0, color=INK, weight="600"))
    o.append(_rect(70, 88, 130, 140, fill="#eef3fb", sw=1.6))
    o.append(_rect(74, 150, 122, 74, fill="#dfeaf4", sw=0))
    o.append(T(152, 122, "bo chua / reservoir", 7.6, color=INK))
    o.append(_rect(200, 160, 300, 22, fill="#fbfaf7", sw=1.6))
    o.append(_rect(204, 164, 292, 14, fill="#dfeaf4", sw=0))
    o.append(_arrow(120, 180, 196, 180, sw=1.4, color=BLUE))
    o.append(T(158, 172, "Q", 8.4, color=BLUE))
    o.append(_arrow(76, 130, 122, 130, sw=1.4, color=RED))
    o.append(T(96, 118, "P1", 7.4, color=RED))
    o.append(_arrow(516, 171, 556, 171, sw=1.4, color=GREEN))
    o.append(T(538, 160, "P2", 7.4, color=GREEN))
    o.append(_path("M520,164 Q540,148 560,164", sw=1.4, color=BLUE))
    o.append(_path("M520,178 Q540,194 560,178", sw=1.4, color=BLUE))
    o.append(T(540, 214, "phan bo parabon / parabolic profile", 7.2, color=BLUE))
    o.append(_line(230, 196, 230, 226, sw=1.0, color=INK))
    o.append(_line(470, 196, 470, 226, sw=1.0, color=INK))
    o.append(_arrow(230, 222, 470, 222, sw=1.0, color=GREY))
    o.append(T(350, 240, "l (chieu dai ong / tube length)", 7.2, color=GREY))
    o.append(T(350, 282, "r = ban kinh ong / tube radius", 7.8, color=INK))
    o.append(T(350, 310, "Q = pi.P.r^4 / (8.mu.l)", 9.0, color=GREEN, weight="600"))
    o.append(T(350, 332, "P = P1 - P2: chenh ap suat / pressure difference",
               7.4, color=GREY))
    o.append(_foot(680, 372, "Dong chay tang lam trong ong nho, tiet dien parabon va Q ty le r^4 / "
                             "Laminar flow in a narrow tube gives a parabolic profile and Q prop r^4"))
    return _finish(o, w, h, "Schematic diagram of a capillary tube viscometer",
        "Hình 4.18 · So do may do nhot ong mao dan: bo chua dua chat long qua ong nho co "
        "tiet dien chay tang lam (phan bo parabon), luong Q, chenh ap P = P1 - P2, ban kinh r "
        "va chieu dai l. Cong thuc Q = pi.P.r^4/(8.mu.l).",
        "Figure 4.18 · A capillary tube viscometer: a reservoir drives liquid through a narrow "
        "tube with a laminar parabolic profile, flow Q and pressure difference P = P1 - P2. Tube "
        "radius r and length l are marked, and Q = pi*P*r^4/(8*mu*l).",
        "Ong mao dan voi dong chay tang lam va cong thuc Q",
        "Capillary tube with laminar flow and the flow-rate formula")


# ---------------------------------------------------------------------------
@_reg
def fig_f19():
    """(a) Saybolt and (b) Redwood orifice viscometers."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "(a) Saybolt; (b) Redwood / hai loai do nhot lo / two orifice viscometers",
               8.4, color=INK, weight="600"))
    o.append(_panel(24, 44, 300, 316, "(a) May Saybolt / Saybolt viscometer"))
    o.append(_panel(356, 44, 300, 316, "(b) May Redwood / Redwood viscometer"))
    for ox, kind in [(174, "saybolt"), (506, "redwood")]:
        o.append(_rect(ox - 46, 92, 92, 96, fill="#eef3fb", sw=1.6))
        o.append(_rect(ox - 42, 140, 84, 44, fill="#dfeaf4", sw=0))
        o.append(T(ox, 116, " coc / cup", 7.4, color=INK))
        if kind == "saybolt":
            o.append(_poly([(ox - 10, 188), (ox + 10, 188), (ox + 3, 210), (ox - 3, 210)],
                           fill="#f6e6c8", sw=1.2, close=True))
        else:
            o.append(_line(ox, 188, ox, 216, sw=4.0, color="#c08a2e"))
        o.append(_arrow(ox, 214, ox, 252, sw=1.2, color=BLUE))
        o.append(_ellipse(ox, 292, 40, 24, fill="#fbfaf7", sw=1.4))
        o.append(_rect(ox - 12, 268, 24, 12, fill="#fbfaf7", sw=1.4))
        o.append(_line(ox - 30, 292, ox + 30, 292, sw=0.8, color=GREY))
        o.append(_line(ox - 22, 300, ox + 22, 300, sw=0.8, color=GREY))
        o.append(T(ox, 332, "binh nhan / receiving flask", 7.0, color=GREY))
    o.append(T(174, 140, "nhiet do / T", 7.0, color=GREEN, anchor="start"))
    o.append(T(506, 140, "nhiet do / T", 7.0, color=GREEN, anchor="start"))
    o.append(_rect(70, 374, 540, 30, fill="#fdf1e3", sw=1.0))
    o.append(T(340, 393, "Thoi gian chay het mot the tich cho biet do nhot / "
                         "Efflux time for a fixed volume gives viscosity",
               7.8, color=INK))
    return _finish(o, w, h, "Saybolt and Redwood orifice viscometers",
        "Hình 4.19 · So do (a) may Saybolt va (b) may Redwood: chat long chay qua lo nho "
        "xuong binh nhan co vach chia; ghi nhiet do va thoi gian chay het mot the tich, tu "
        "do suy do nhot.",
        "Figure 4.19 · Schematics of (a) a Saybolt viscometer and (b) a Redwood viscometer: "
        "liquid flows through a small orifice into a graduated receiving flask. Temperature and "
        "the efflux time for a fixed volume give the viscosity.",
        "Hai may do nhot lo Saybolt va Redwood voi binh nhan",
        "Saybolt and Redwood orifice viscometers with receiving flasks")


# ---------------------------------------------------------------------------
@_reg
def fig_f20():
    """Parabolic laminar velocity profile in a circular tube (inferred)."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Phan bo van toc parabon trong ong tron / Parabolic tube profile",
               9.0, color=INK, weight="600"))
    o.append(T(340, 46, "Source caption blank; diagram inferred from the surrounding derivation",
               7.4, color=RED))
    x0, ytop, ybot = 140, 96, 300
    o.append(_line(x0, ytop, 556, ytop, sw=2.0, color=INK))
    o.append(_line(x0, ybot, 556, ybot, sw=2.0, color=INK))
    o.append(T(348, 86, "v = 0 o thanh / no slip at wall", 7.6, color=GREY))
    o.append(T(348, 318, "v = 0 o thanh / no slip at wall", 7.6, color=GREY))
    mid = (ytop + ybot) / 2.0
    for k in range(-5, 6):
        yy = mid + k * 18.0
        vmax = 1.0 - (yy - mid) ** 2 / ((ybot - ytop) / 2.0) ** 2
        ln = 6 + vmax * 120
        o.append(_line(x0 + 26, yy, x0 + 26, yy, sw=0))
        o.append(_arrow(x0 + 26, yy, x0 + 26 + ln, yy, sw=1.2, color=BLUE))
    o.append(_arrow(x0 + 26, mid, x0 + 26 + 126, mid, sw=2.0, color=RED))
    o.append(T(x0 + 26 + 130, mid + 3, "v max", 8.0, color=RED, anchor="start"))
    o.append(_line(x0 + 250, mid, x0 + 250, ybot, sw=1.0, color=GREEN))
    o.append(T(x0 + 258, (mid + ybot) / 2, "r", 8.0, color=GREEN, anchor="start"))
    o.append(_line(x0 + 350, mid, x0 + 350, ybot, sw=1.0, color=GREEN))
    o.append(T(x0 + 358, (mid + ybot) / 2, "R", 8.0, color=GREEN, anchor="start"))
    o.append(_rect(x0 + 368, mid - 8, 26, 16, fill="#f6e6c8", sw=1.0))
    o.append(T(x0 + 381, mid - 14, "dr", 7.0, color=INK))
    o.append(T(348, 348, "v(r) = (P / (4.mu.l)) x (R^2 - r^2)", 8.8,
               color=INK, weight="600"))
    o.append(T(348, 372, "Q = pi.P.R^4 / (8.mu.l) - tich phan theo vong tron dr / "
                         "integrate the annular element dr",
               7.4, color=GREY))
    o.append(_foot(680, 402, "Nhan de so day o thanh, lon nhat o tam; Q ti le R^4 / "
                             "Zero at the wall, maximum at the centre; Q proportional to R^4"))
    return _finish(o, w, h, "Parabolic laminar profile in a circular tube",
        "Hình 4.20 · Nhãn nguồn để trống; sơ đồ được suy ra từ phép tính bao quanh. "
        "Trong ong tron, dong chay tang lam co phan bo van toc parabon: van toc bang 0 o "
        "thanh ong, lon nhat o tam, v(r) = P(R^2 - r^2)/(4.mu.l), suy ra Q = pi.P.R^4/(8.mu.l).",
        "Figure 4.20 · Source caption blank; diagram inferred from the surrounding derivation. "
        "In a circular tube, laminar flow has a parabolic velocity profile: zero at the wall and "
        "maximum at the centre, v(r) = P(R^2 - r^2)/(4*mu*l), giving Q = pi*P*R^4/(8*mu*l).",
        "Phan bo van toc parabon trong ong, bang 0 o thanh",
        "Parabolic velocity profile in a tube, zero at the wall")


# ---------------------------------------------------------------------------
@_reg
def fig_f22():
    """Turbidity meter with sample vial and detector geometry."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "May do do doc / Turbidity meter",
               9.0, color=INK, weight="600"))
    o.append(T(340, 42, "Hinh 21 khong co trong ban in; day la hinh 22 / "
                        "Figure 21 absent in print; this is figure 22", 7.2, color=RED))
    o.append(_rect(60, 64, 336, 280, fill="#eceff2", sw=2.0, stroke="#7f8a94"))
    o.append(_rect(74, 78, 308, 62, fill="#0f2418", sw=1.2))
    o.append(T(228, 104, "12.4 NTU", 18, color="#9fe870"))
    o.append(T(228, 126, "sample / mau", 7.6, color="#7fc98a"))
    o.append(T(228, 158, "May cam tay / Handheld meter", 8.4, color=INK, weight="600"))
    for r in range(2):
        for c in range(5):
            o.append(_rect(92 + c * 52, 184 + r * 26, 40, 18, fill="#dfe3e6", sw=0.8))
    o.append(T(228, 258, "ban phim / keypad", 7.4, color=GREY))
    o.append(T(228, 296, "hieu chuan / calibrate", 7.4, color=BLUE))
    o.append(_panel(420, 64, 236, 280, "Hinh hoc do / Detector geometry"))
    o.append(_rect(462, 120, 52, 150, fill="#eef3fb", sw=1.6))
    o.append(_rect(466, 156, 44, 78, fill="#dfeaf4", sw=0))
    o.append(T(488, 112, "vial mau / sample vial", 7.4, color=INK))
    o.append(_arrow(430, 196, 462, 196, sw=1.8, color="#b45309"))
    o.append(T(432, 184, "nguon / source", 6.8, color="#b45309", anchor="start"))
    o.append(_arrow(514, 196, 566, 156, sw=1.8, color=GREEN))
    o.append(T(566, 146, "detector 90°", 7.2, color=GREEN, anchor="start"))
    o.append(T(538, 226, "anh xa / scattered light", 6.8, color=GREY, anchor="start"))
    o.append(T(480, 268, "Do doc do anh xa 90° / measure 90° scatter",
               7.4, color=INK, anchor="start"))
    o.append(T(538, 288, "dong vi thuoc thu / nephelometric",
               7.0, color=GREY, anchor="start"))
    o.append(_foot(680, 372, "Dung vial sach, khong bot khí; hieu chuan bang chuan NTU / "
                             "Use a clean bubble-free vial and calibrate with NTU standards"))
    return _finish(o, w, h, "Turbidity meter",
        "Hình 4.22 · Hinh 21 khong co trong ban in; hinh 22 la may do do doc: may cam tay co "
        "manhinh hien thi NTU, ban phim hieu chuan, vial mau va hinh hoc detector dat 90° so "
        "voi nguon sang de do anh xa.",
        "Figure 4.22 · Source figure 21 is absent in the printed chapter; this Figure 22 shows a "
        "turbidity meter: a handheld body with an NTU display, calibration keypad, sample vial "
        "and a detector placed at 90 degrees to the light source to measure scattered light.",
        "May do do doc voi vial mau va detector 90 do",
        "Turbidity meter with a sample vial and 90 degree detector")


# ---------------------------------------------------------------------------
@_reg
def fig_f23():
    """A turbidity tube with a black target and reading scale."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Ong do do doc / A turbidity tube",
               9.0, color=INK, weight="600"))
    o.append(T(340, 42, "Hinh 21 khong co trong ban in; day la hinh 23 / "
                        "Figure 21 absent in print; this is figure 23", 7.2, color=RED))
    o.append(_rect(286, 60, 108, 300, fill="#fbfaf7", sw=2.0))
    o.append(_rect(290, 64, 100, 292, fill="#eaf2f8", sw=0))
    o.append(_rect(296, 324, 88, 30, fill="#2a2a2a", sw=1.0))
    o.append(_line(332, 326, 332, 352, sw=3.0, color="#fbfaf7"))
    o.append(_line(316, 338, 348, 338, sw=3.0, color="#fbfaf7"))
    o.append(T(340, 372, "dau muc tieu den / black target", 7.2, color=GREY))
    for i in range(11):
        yy = 80 + i * 24
        ln = 18 if i % 2 == 0 else 10
        o.append(_line(290, yy, 290 + ln, yy, sw=1.0, color=INK))
        o.append(T(316, yy + 3, str(i * 10), 6.6, color=INK, anchor="start"))
    o.append(_line(290, 152, 390, 152, sw=1.6, color=BLUE, dash="6 4"))
    o.append(T(396, 150, "muc nuoc / fill line", 7.4, color=BLUE, anchor="start"))
    o.append(T(396, 168, "doc gia tri / read scale", 7.0, color=GREY, anchor="start"))
    o.append(_bl(120, 120, "Ong nhua trong, co vach", "Clear graduated tube"))
    o.append(_bl(120, 178, "Dap nuoc mau den day", "Fill with sample to the mark"))
    o.append(_bl(120, 236, "Nhin qua cot nuoc", "Look down through the column"))
    o.append(_bl(120, 294, "Mat dau muc tieu: doc NTU", "Target vanishes: read NTU"))
    o.append(_foot(680, 400, "Cot nuoc cang doc, muc tieu mat som hon; gia tri doc bang don vi "
                             "NTU / A deeper column hides the target sooner; read in NTU units"))
    return _finish(o, w, h, "A turbidity tube",
        "Hình 4.23 · Hinh 21 khong co trong ban in; hinh 23 la ong do do doc: ong nhua "
        "trong co vach chia, day co dau muc tieu den. Dap mau den vach, nhin xuong va doc "
        "gia tri khi dau muc tieu bien mat, don vi NTU.",
        "Figure 4.23 · Source figure 21 is absent in the printed chapter; this Figure 23 is a "
        "turbidity tube: a clear graduated tube with a black target at the bottom. Fill with "
        "sample to the mark and read the NTU scale where the target just disappears.",
        "Ong do do doc co dau muc tieu den va thang chia",
        "Graduated turbidity tube with a black target and fill line")
