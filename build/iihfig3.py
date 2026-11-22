# -*- coding: utf-8 -*-
"""Vector figures for Chapter 3 "Measurement of Level" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 97-142 (printed pp. 83-128).

The source figures are UNNUMBERED images, each marked only by a ``Citation:``
line (an image credit, not prose).  Their subjects are inferred from the
surrounding prose and the citation URL.  They are redrawn here as simplified
vector schematics with descriptive bilingual captions.  Every function
returns the standard 5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)``
through ``_fig()``.  All SVG text is XML-escaped with ``esc()``/``T()``.
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
    """Intro: the four levels/scales of measurement, increasing detail."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 28, "Các mức và thang đo của một biến / Levels and scales of a variable",
               9.2, color=INK, weight="600"))
    o.append(_rect(34, 152, 128, 52, fill="#e7eef7", sw=1.4))
    o.append(T(98, 175, "Biến", 10, color=INK, weight="600"))
    o.append(T(98, 192, "Variable", 8.4, color=BLUE))
    bands = [
        (66, 208, "Danh nghĩa / Nominal", "chỉ phân loại - classify only", "#f3f0fa"),
        (136, 268, "Thứ tự / Ordinal", "có thứ tự - ordered ranks", "#eaf1fb"),
        (206, 328, "Khoảng / Interval", "khoảng cách bằng nhau - equal intervals", "#e6f4ee"),
        (276, 388, "Tỷ lệ / Ratio", "điểm zero thật - true zero point", "#fdf1e3"),
    ]
    for i, (y, bw, name, desc, fill) in enumerate(bands):
        o.append(_rect(206, y, bw, 48, fill=fill, sw=1.2))
        o.append(T(216, y + 20, name, 9.0, color=INK, weight="600", anchor="start"))
        o.append(T(216, y + 37, desc, 7.8, color=GREY, anchor="start"))
        o.append(_arrow(162, 178, 204, y + 24, sw=1.0, color=BLUE))
    o.append(_arrow(640, 340, 640, 76, sw=1.2, color=RED))
    o.append(T(640, 70, "độ chi tiết tăng", 7.6, color=RED, anchor="end"))
    o.append(T(640, 62, "increasing detail", 7.6, color=RED, anchor="end"))
    o.append(_foot(680, 362, "Mức cao hơn bao hàm mức thấp hơn va them thuộc tính moi / "
                             "Each higher level includes the lower one and adds something new"))
    return _finish(o, w, h, "Levels and scales of measurement",
        "Hình 3.1 · Ảnh gốc không đánh số — Một biến có thể ở một trong bốn mức đo: danh nghĩa, "
        "thứ tự, khoảng và tỷ lệ. Độ chi tiết tăng dần từ trên xuống; mức cao hơn bao hàm mức thấp "
        "hơn và thêm một thuộc tính mới.",
        "Figure 3.1 · Source image unnumbered — A variable has one of four measurement levels: "
        "nominal, ordinal, interval and ratio. Detail increases downwards; each higher level "
        "includes the lower one and adds a new property.",
        "Bốn mức đo danh nghĩa, thứ tự, khoảng, tỷ lệ xếp theo độ chi tiết tăng dần",
        "Four measurement levels nominal, ordinal, interval, ratio stacked by increasing detail")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """measlevl.gif: comparison grid of the four levels of measurement."""
    w, h = 680, 430
    o = [_defs()]
    o.append(T(340, 26, "Bốn mức đo: thuộc tính va vi du / Four levels: properties and examples",
               9.0, color=INK, weight="600"))
    xs = [40, 160, 280, 400, 520, 640]   # label column + four data columns
    heads = ["Danh nghĩa\nNominal", "Thứ tự\nOrdinal", "Khoảng\nInterval", "Tỷ lệ\nRatio"]
    o.append(_rect(40, 46, 600, 40, fill="#e7eef7", sw=1.2))
    for i, hd in enumerate(heads):
        for j, ln in enumerate(hd.split("\n")):
            o.append(T((xs[i + 1] + xs[i + 2]) / 2, 62 + j * 14, ln, 8.6,
                       color=INK, weight="600"))
    for xb in xs[1:-1]:
        o.append(_line(xb, 46, xb, 362, sw=0.6, color="#cfd5db"))
    rows = [
        ("Phân loại / Categories", ["+", "+", "+", "+"]),
        ("Thứ tự / Order", ["-", "+", "+", "+"]),
        ("Khoảng bằng nhau / Equal intervals", ["-", "-", "+", "+"]),
        ("Điểm zero thật / True zero", ["-", "-", "-", "+"]),
    ]
    y = 86
    rh = 44
    for label, cells in rows:
        o.append(_rect(40, y, 120, rh, fill="#f5f6f8", sw=0.8))
        o.append(T(46, y + 27, label, 7.2, color=INK, anchor="start"))
        for i, c in enumerate(cells):
            o.append(T((xs[i + 1] + xs[i + 2]) / 2, y + 29,
                       "co/yes" if c == "+" else "khong/no",
                       8.0, color=GREEN if c == "+" else GREY, weight="600"))
        o.append(_line(40, y + rh, 640, y + rh, sw=0.6, color="#cfd5db"))
        y += rh
    o.append(_rect(40, y, 600, 38, fill="#fdf1e3", sw=1.0))
    o.append(T(46, y + 24, "Vi du / Example", 7.6, color=INK, anchor="start"))
    ex = ["Gioi tinh / Gender", "Xep hang / Ranks",
          "Nhiet do F / Temp F", "Can nang / Weight"]
    for i, e in enumerate(ex):
        o.append(T((xs[i + 1] + xs[i + 2]) / 2, y + 24, e, 7.4, color=INK))
    o.append(_foot(680, 400, "Nominal it nhat, ordinal them thu tu, interval them khoang cach, "
                             "ratio them zero that / Nominal least, ordinal adds order, "
                             "interval adds equal gaps, ratio adds true zero"))
    o.append(_foot(680, 418, "Ke hieu: + = co/yes; - = khong/no ; F = Fahrenheit"))
    return _finish(o, w, h, "Comparison of the four measurement levels",
        "Hình 3.2 · Ảnh gốc không đánh số — Bảng so sánh bốn mức đo: danh nghĩa chỉ phân loại; "
        "thứ tự thêm thứ tự; khoảng thêm khoảng cách bằng nhau; tỷ lệ thêm điểm zero thật. Ví dụ "
        "tương ứng: giới tính, xếp hạng, nhiệt độ độ F, cân nặng.",
        "Figure 3.2 · Source image unnumbered — Comparison grid of the four levels: nominal only "
        "classifies; ordinal adds order; interval adds equal intervals; ratio adds a true zero. "
        "Examples: gender, ranks, temperature in Fahrenheit, weight.",
        "Bảng so sánh bốn mức đo theo thuộc tính và ví dụ",
        "Comparison grid of the four measurement levels by property and example")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """YouTube thumbnail: why knowing the level of measurement matters."""
    w, h = 680, 360
    o = [_defs()]
    o.append(T(340, 26, "Tai sao can biet muc do / Why the level of measurement matters",
               9.0, color=INK, weight="600"))
    o.append(_rect(260, 46, 160, 48, fill="#e7eef7", sw=1.4))
    o.append(T(340, 66, "Bien / Variable", 9.4, color=INK, weight="600"))
    o.append(T(340, 83, " gia tri thay doi / values vary", 7.4, color=GREY))
    o.append(_arrow(340, 94, 340, 120, sw=1.3, color=BLUE))
    o.append(_rect(230, 120, 220, 50, fill="#dfeaf4", sw=1.4))
    o.append(T(340, 141, "Muc do cua bien", 9.4, color=INK, weight="600"))
    o.append(T(340, 158, "Level of measurement", 8.6, color=BLUE))
    o.append(_arrow(300, 170, 170, 214, sw=1.2, color=BLUE))
    o.append(_arrow(380, 170, 510, 214, sw=1.2, color=BLUE))
    o.append(_panel(40, 216, 260, 92, "1. Giai thich du lieu / Interpret data"))
    o.append(T(170, 258, "Gia tri la ma ngan cho ten dai", 8.0, color=INK))
    o.append(T(170, 277, "Values are short codes for longer names", 7.4, color=GREY))
    o.append(T(170, 296, "danh nghia = khong lay trung binh", 7.4, color=RED))
    o.append(_panel(380, 216, 260, 92, "2. Chon phep kiem dinh / Choose test"))
    o.append(T(510, 258, "Phep kiem phu hop voi muc do", 8.0, color=INK))
    o.append(T(510, 277, "Test depends on the level of measurement", 7.4, color=GREY))
    o.append(T(510, 296, "danh nghia -> khong t-test", 7.4, color=RED))
    o.append(_foot(680, 336, "Biet muc do -> hien du lieu dung va chon thong ke dung / "
                             "Know the level -> interpret data and choose statistics correctly"))
    return _finish(o, w, h, "Why the level of measurement matters",
        "Hình 3.3 · Ảnh gốc không đánh số — Biết mức đo của biến giúp (1) giải thích dữ liệu "
        "đúng — giá trị số chỉ là mã ngắn của tên dài; và (2) chọn đúng phép kiểm định thống kê "
        "— dữ liệu danh nghĩa không bao giờ được lấy trung bình hay dùng t-test.",
        "Figure 3.3 · Source image unnumbered — Knowing a variable's level of measurement helps "
        "(1) interpret data correctly — numeric values are short codes for longer names; and "
        "(2) choose the right statistical test — nominal data is never averaged or given a t-test.",
        "Luong trinh: bien -> muc do -> giai thich du lieu va chon phep kiem dinh",
        "Flow: variable -> level -> interpret data and choose statistical test")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """measlev2.gif: ordinal educational attainment with unequal gaps."""
    w, h = 680, 360
    o = [_defs()]
    o.append(T(340, 26, "Muc thu tu: trinh do hoc van / Ordinal level: educational attainment",
               9.0, color=INK, weight="600"))
    ticks = [60, 120, 210, 330, 480, 640]
    o.append(_line(50, 150, 660, 150, sw=1.4, color=INK))
    for i, x in enumerate(ticks):
        o.append(_line(x, 142, x, 158, sw=1.4, color=INK))
        o.append(_circle(x, 150, 4, fill="#fdf3e6", sw=1.2))
        o.append(T(x, 134, str(i), 9.0, color=INK, weight="600"))
    o.append(_arrow(52, 112, 658, 112, sw=1.0, color=RED))
    o.append(T(356, 104, "thu tang / increasing", 7.6, color=RED))
    o.append(_line(ticks[0], 176, ticks[1], 176, sw=1.0, color=BLUE))
    o.append(T((ticks[0] + ticks[1]) / 2, 192, "0-1", 7.4, color=BLUE))
    o.append(_line(ticks[3], 176, ticks[4], 176, sw=1.0, color=RED))
    o.append(T((ticks[3] + ticks[4]) / 2, 192, "3-4", 7.4, color=RED))
    o.append(T(350, 210, "Khoang 0-1 khong bang khoang 3-4 / The 0-1 gap is not the 3-4 gap",
               8.0, color=INK))
    labels = ["0 = duoi THPT / < high school", "1 = mot phan THPT / some high school",
              "2 = tot nghiep THPT / high school degree", "3 = mot phan DH / some college",
              "4 = bang DH / college degree", "5 = sau DH / post college"]
    for i, lab in enumerate(labels):
        col, row = i % 2, i // 2
        o.append(T(40 + col * 330, 244 + row * 22, lab, 7.8, color=INK, anchor="start"))
    o.append(_foot(680, 326, "Gia tri cao hon nghia la hoc van nhieu hon, nhung khoang cach "
                             "giua cac gia tri khong co nghia / Higher = more education, but "
                             "intervals between values are not interpretable"))
    o.append(_foot(680, 344, "THPT = trung hoc pho thong (high school); DH = dai hoc (college)"))
    return _finish(o, w, h, "Ordinal level with unequal intervals",
        "Hình 3.4 · Ảnh gốc không đánh số — Mức thứ tự: các hạng được xếp thứ tự "
        "(0 = dưới THPT ... 5 = sau ĐH), nhưng khoảng cách giữa các hạng không bằng nhau và "
        "không có nghĩa; ví dụ khoảng 0–1 khác khoảng 3–4.",
        "Figure 3.4 · Source image unnumbered — Ordinal level: categories are rank-ordered "
        "(0 = less than high school ... 5 = post college), but the distances between ranks are "
        "neither equal nor interpretable; e.g. the 0-1 gap differs from the 3-4 gap.",
        "Thang trinh do hoc van 0 den 5 voi cac khoang cach khong deu",
        "Educational attainment scale 0 to 5 with unequal intervals")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Area marking in a factory, plus keyboard visual-indicator rectangles."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Chi thi truc quan: danh dau khu vuc / Visual indicators: area marking",
               9.0, color=INK, weight="600"))
    o.append(_panel(30, 44, 360, 300, "San xuat / Factory floor"))
    o.append(_rect(48, 70, 324, 258, fill="#f8f9fa", sw=1.0, stroke="#cfd5db"))
    zones = [(66, 92, 120, 74, "Khu A / Zone A"), (208, 92, 146, 74, "Khu B / Zone B"),
             (66, 186, 100, 60, "Khu C / Zone C"), (186, 186, 168, 60, "Khu D / Zone D"),
             (66, 266, 288, 46, "Duong di / Walkway")]
    for x, y, zw, zh, lab in zones:
        o.append(_rect(x, y, zw, zh, fill="#e3f0fb", sw=1.6, stroke=BLUE))
        o.append(T(x + zw / 2, y + zh / 2 + 3, lab, 7.6, color=BLUE))
    o.append(_panel(410, 44, 240, 300, "Ban phim / Keyboard focus"))
    o.append(_rect(438, 76, 184, 110, fill="#f8f9fa", sw=1.0, stroke="#cfd5db"))
    for r in range(3):
        for c in range(4):
            o.append(_rect(450 + c * 42, 88 + r * 32, 34, 24,
                           fill="#fdf3e6", sw=0.8, stroke="#cfd5db"))
    o.append(_rect(492, 88, 34, 24, fill="none", sw=2.4, stroke=BLUE))
    o.append(T(530, 100, "<- o nhan / focus", 7.2, color=BLUE, anchor="start"))
    o.append(T(530, 152, "hinh chu nhat xanh", 7.2, color=INK, anchor="start"))
    o.append(T(530, 168, "blue rectangle", 7.2, color=INK, anchor="start"))
    o.append(T(528, 214, "dieu huong bang ban phim", 7.4, color=GREY, anchor="start"))
    o.append(T(528, 230, "keyboard navigation", 7.4, color=GREY, anchor="start"))
    o.append(T(528, 252, "cho thay vi tri / shows", 7.4, color=GREY, anchor="start"))
    o.append(T(528, 268, "vi tri hien tai / location", 7.4, color=GREY, anchor="start"))
    o.append(_foot(680, 372, "O nhan mau xanh hien ra khi dieu huong bang ban phim; trong nha may "
                             "la cac vung danh dau mau / Blue boxes appear on keyboard "
                             "navigation; in a factory they are painted area markings"))
    return _finish(o, w, h, "Visual indicators and factory area marking",
        "Hình 3.5 · Ảnh gốc không đánh số — (trái) Các khu vực được đánh dấu bằng ô màu xanh "
        "trên sàn nhà máy; (phải) các hình chữ nhật xanh hiện ra khi dùng bàn phím để điều hướng, "
        "cho người dùng thấy vị trí của họ.",
        "Figure 3.5 · Source image unnumbered — (left) blue-painted zone markings on a factory "
        "floor; (right) blue rectangles that appear when a visitor uses keyboard navigation, "
        "letting them see their location.",
        "San nha may voi cac khu danh dau xanh va o nhan ban phim",
        "Factory floor with blue zone markings and keyboard focus boxes")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Electrical resistance and conductance - the water pipe analogy."""
    w, h = 680, 370
    o = [_defs()]
    o.append(T(340, 26, "Dien tro va do dan: so sanh ong nuoc / Resistance and conductance: "
                        "water-pipe analogy", 8.8, color=INK, weight="600"))
    o.append(_panel(30, 44, 290, 210, "Ong nuoc / Water pipe"))
    o.append(_rect(56, 116, 238, 40, fill="#dfeaf4", sw=1.4))
    o.append(_arrow(70, 136, 280, 136, sw=2.0, color=BLUE))
    o.append(T(86, 108, "P1 cao / high", 7.4, color=RED))
    o.append(T(250, 108, "P2 thap / low", 7.4, color=GREY))
    o.append(_arrow(96, 118, 96, 78, sw=1.2, color=RED))
    o.append(_arrow(256, 118, 256, 78, sw=1.2, color=GREY))
    o.append(T(176, 182, "Luong Q / Flow Q ~ (P1 - P2)", 8.0, color=INK))
    o.append(T(176, 206, "do dan G ~ luong / conductance ~ flow", 7.4, color=GREY))
    o.append(T(176, 230, "dien tro ~ ap suat can / R ~ pressure needed", 7.4, color=GREY))
    o.append(_panel(360, 44, 290, 210, "Day dan / Wire"))
    o.append(_rect(386, 132, 238, 12, fill="#e3eef7", sw=1.2))
    o.append(_rect(470, 122, 40, 32, fill="#fdf3e6", sw=1.4, stroke=RED))
    o.append(T(490, 116, "R", 8.6, color=RED))
    o.append(_arrow(400, 138, 462, 138, sw=1.8, color=BLUE))
    o.append(_arrow(518, 138, 610, 138, sw=1.8, color=BLUE))
    o.append(T(420, 168, "V", 9.0, color=INK))
    o.append(T(566, 168, "I", 9.0, color=INK))
    o.append(T(505, 202, "Dong I / Current I", 8.0, color=INK))
    o.append(T(505, 226, "R = V/I ; G = I/V = 1/R", 8.0, color=GREEN))
    o.append(_rect(150, 276, 380, 44, fill="#e6f4ee", sw=1.2, stroke=GREEN))
    o.append(T(340, 295, "R = V/I (ohm, Ω) ; G = 1/R (siemens, S)", 9.0, color=INK, weight="600"))
    o.append(T(340, 312, "Dinh luat Ohm: V ti le thuc voi I / Ohm's law: V is proportional to I",
               7.6, color=GREY))
    o.append(_foot(680, 348, "Giam ap toc dung luc day / Voltage drop (not voltage itself) "
                             "drives the current, like pressure difference drives water"))
    return _finish(o, w, h, "Electrical resistance and conductance",
        "Hình 3.6 · Ảnh gốc không đánh số — So sánh dòng điện trong dây dẫn với dòng nước "
        "trong ống: điện trở R = V/I (đơn vị ohm), độ dẫn G = 1/R (siemens). Sụt áp cũng như chênh "
        "áp lực — chứ không phải giá trị tuyệt đối — tạo ra dòng chảy.",
        "Figure 3.6 · Source image unnumbered — Current in a wire compared with water in a pipe: "
        "resistance R = V/I (ohm), conductance G = 1/R (siemens). Voltage drop, like pressure "
        "difference, drives the flow.",
        "Ong nuoc va day dan minh hoa R = V/I va G = 1/R",
        "Water pipe and wire illustrating R = V/I and G = 1/R")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Static (hydrostatic) pressure, pressure head and P = gamma h."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Ap suat tinh (thuyet tinh) va cot ap / Static pressure and pressure head",
               8.8, color=INK, weight="600"))
    o.append(_rect(80, 60, 300, 290, fill="#fbfaf7", sw=1.6))
    o.append(_rect(82, 100, 296, 248, fill="#dfeaf4", sw=0))
    o.append(_line(82, 100, 378, 100, sw=1.6, color=BLUE))
    o.append(T(230, 92, "mat chat long / fluid surface", 7.6, color=BLUE))
    o.append(_line(226, 100, 226, 286, sw=1.2, color=RED, dash="5 3"))
    o.append(_arrow(214, 104, 214, 282, sw=1.2, color=RED))
    o.append(_arrow(238, 282, 238, 104, sw=1.2, color=RED))
    o.append(T(250, 196, "h", 10, color=RED))
    o.append(T(250, 212, "do sau / depth", 7.4, color=RED))
    o.append(_rect(206, 286, 40, 20, fill="#fdf3e6", sw=1.2))
    o.append(_arrow(226, 300, 226, 336, sw=1.8, color=INK))
    o.append(T(270, 318, "F = P x A", 8.4, color=INK))
    for i, yy in enumerate((140, 190, 240, 290)):
        o.append(_arrow(392, yy, 330, yy, sw=1.0 + i * 0.4, color=BLUE))
    o.append(T(366, 120, "ap suat tang theo do sau", 7.4, color=BLUE, anchor="end"))
    o.append(T(366, 134, "pressure grows with depth", 7.4, color=BLUE, anchor="end"))
    o.append(_panel(410, 74, 240, 220, "Phuong trinh / Equations"))
    o.append(T(530, 118, "P = F / A", 10, color=INK, weight="600"))
    o.append(T(530, 138, "F = P x A", 9.0, color=GREY))
    o.append(T(530, 176, "P = gamma x h", 10, color=INK, weight="600"))
    o.append(T(530, 196, "h = P / gamma", 9.0, color=GREY))
    o.append(T(530, 230, "gamma = trong luong rieng", 7.6, color=GREY))
    o.append(T(530, 246, "specific weight of fluid", 7.6, color=GREY))
    o.append(T(530, 272, "P = ap suat / pressure", 7.2, color=GREY))
    o.append(_foot(680, 386, "Cot ap la chieu cao chat long se dat duoc neu bo cac luc giam giu; "
                             "cong thuc chi dung cho chat long khong nen / Pressure head is the "
                             "height fluid would reach if confining forces were removed; valid "
                             "for incompressible fluids"))
    return _finish(o, w, h, "Static pressure and pressure head",
        "Hình 3.7 · Ảnh gốc không đánh số — Áp suất tĩnh do trọng lượng chất lỏng gây ra, "
        "tăng theo độ sâu. Các phương trình: P = F/A; P = γ·h (γ là trọng lượng riêng); "
        "cot ap h = P/γ là chiều cao chất lỏng nếu bỏ lực giam giữ.",
        "Figure 3.7 · Source image unnumbered — Static pressure is due to fluid weight and grows "
        "with depth. Equations: P = F/A; P = gamma*h (gamma = specific weight); pressure head "
        "h = P/gamma is the height the fluid would reach if confining forces were removed.",
        "Bonh chua chat long voi do sau h va cac phuong trinh ap suat",
        "Tank of fluid with depth h and the pressure equations")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """Omron fig1: level control principle with ground and elevated tanks."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Nguyen ly dieu khien muc: be chua va be tang cao / Level control principle",
               8.8, color=INK, weight="600"))
    o.append(_panel(28, 44, 190, 130, "Be duoi dat / Ground tank"))
    o.append(_rect(56, 84, 134, 76, fill="#fbfaf7", sw=1.4))
    o.append(_rect(58, 118, 130, 40, fill="#dfeaf4", sw=0))
    o.append(T(123, 168, "nuoc cap tu nguon / water mains", 6.6, color=GREY))
    o.append(_arrow(210, 110, 250, 110, sw=1.2, color=BLUE))
    o.append(_circle(300, 262, 30, fill="#fdf3e6", sw=1.6))
    o.append(_poly([(288, 246), (288, 278), (314, 262)], fill=BLUE, close=True))
    o.append(T(300, 306, "May bom / Pump", 8.0, color=INK))
    o.append(_arrow(300, 232, 300, 180, sw=1.8, color=BLUE))
    o.append(_arrow(300, 180, 470, 180, sw=1.8, color=BLUE))
    o.append(_arrow(470, 180, 470, 150, sw=1.8, color=BLUE))
    o.append(_panel(410, 44, 240, 200, "Be tang cao / Elevated tank"))
    o.append(_rect(440, 76, 180, 150, fill="#fbfaf7", sw=1.4))
    o.append(_rect(442, 116, 176, 108, fill="#dfeaf4", sw=0))
    o.append(_line(442, 116, 618, 116, sw=1.4, color=BLUE))
    o.append(_line(442, 146, 618, 146, sw=1.0, color=RED, dash="5 3"))
    o.append(_line(442, 176, 618, 176, sw=1.0, color=GREEN, dash="5 3"))
    o.append(T(624, 118, "cao / high", 6.8, color=BLUE, anchor="start"))
    o.append(T(624, 148, "E1", 6.8, color=RED, anchor="start"))
    o.append(T(624, 178, "E2", 6.8, color=GREEN, anchor="start"))
    o.append(_line(500, 84, 500, 200, sw=1.0, color=GREY))
    o.append(T(494, 82, "E3", 6.8, color=GREY, anchor="end"))
    o.append(_rect(60, 300, 560, 60, fill="#f5f6f8", sw=1.0))
    o.append(T(340, 322, "Khi muc thap -> bom chay; khi muc dat E1 -> bom dung", 8.4,
               color=INK, weight="600"))
    o.append(T(340, 342, "Low level -> pump on; reaching high level E1 -> pump off", 8.0,
               color=GREY))
    o.append(_foot(680, 388, "E1 = dien cuoc muc cao, E2 = muc thap, E3 = dien cuoc chung / "
                             "E1 high-level electrode, E2 low-level, E3 common electrode"))
    return _finish(o, w, h, "Level control principle",
        "Hình 3.8 · Ảnh gốc không đánh số — Nguyên lý điều khiển mức nước tòa nhà: nước từ "
        "nguồn chảy vào bể dưới đất, được bơm lên bể trên cao và phân phối các tầng. Khi mức "
        "thấp thì bơm chạy (điện cực E1/E2/E3), khi đạt mức cao E1 thì bơm dừng.",
        "Figure 3.8 · Source image unnumbered — Building water-level control principle: mains "
        "water fills the ground tank, a pump lifts it to the elevated tank, and distribution "
        "follows. The pump runs at low level (electrodes E1/E2/E3) and stops at high level E1.",
        "So do be duoi dat, may bom va be tang cao voi dien cuoc muc",
        "Diagram of ground tank, pump and elevated tank with level electrodes")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """Omron principles: conductive electrode detection at low and high level."""
    w, h = 680, 430
    o = [_defs()]
    o.append(T(340, 26, "Phat hien muc bang dien cuoc dan / Conductive electrode level detection",
               8.8, color=INK, weight="600"))
    for k, (x, title, lvl, closed) in enumerate([
            (24, "Muc nuoc thap / Low water level", 158, False),
            (352, "Muc nuoc cao / High water level", 106, True)]):
        o.append(_panel(x, 44, 304, 300, title))
        o.append(_rect(x + 22, 82, 180, 170, fill="#fbfaf7", sw=1.4))
        o.append(_rect(x + 24, lvl, 176, 250 - lvl, fill="#dfeaf4", sw=0))
        o.append(_line(x + 24, lvl, x + 200, lvl, sw=1.4, color=BLUE))
        for j, (ex, name, col) in enumerate([(x + 60, "E1", RED),
                                             (x + 110, "E2", GREEN),
                                             (x + 160, "E3", INK)]):
            o.append(_line(ex, 86, ex, 242 if j > 0 else 150, sw=2.0, color=col))
            o.append(T(ex, 80, name, 8.0, color=col))
        o.append(_rect(x + 218, 120, 62, 60, fill="#fdf3e6", sw=1.2))
        o.append(T(x + 249, 140, "Relay", 8.0, color=INK))
        o.append(T(x + 249, 156, "X", 10, color=RED, weight="600"))
        o.append(_line(x + 200, 196, x + 218, 170, sw=0.9, color=GREY))
        if closed:
            o.append(_line(x + 249, 180, x + 249, 200, sw=1.8, color=GREEN))
            o.append(T(x + 249, 214, "a side", 7.4, color=GREEN))
            o.append(T(x + 130, 274, "Mach dong / circuit closed", 7.6, color=GREEN))
            o.append(T(x + 130, 292, "Relay X honored -> switch to a", 6.8, color=GREY))
        else:
            o.append(_line(x + 249, 180, x + 266, 200, sw=1.8, color=RED))
            o.append(T(x + 249, 214, "b side", 7.4, color=RED))
            o.append(T(x + 130, 274, "Mach ho / circuit open", 7.6, color=RED))
            o.append(T(x + 130, 292, "No current E1-E3 -> relay stays at b", 6.8, color=GREY))
        o.append(T(x + 152, 328, "chat long dan / conductive liquid", 7.0, color=GREY))
    o.append(_foot(680, 370, "E1/E2/E3 la cac dien cuoc; chat long dan dong mach giua E1 va E3. "
                             "E2 them vao de tao mach tu giu / E1/E2/E3 electrodes; conductive "
                             "liquid closes the circuit between E1 and E3; E2 forms a "
                             "self-holding circuit"))
    o.append(_foot(680, 388, "Khi muc roi duoi E2, relay X mat dien va tiep diem NC dong lai / "
                             "When level falls below E2, relay X drops out and its NC contact "
                             "closes"))
    o.append(_foot(680, 406, "NC = normally closed (tiep diem thuong dong)"))
    return _finish(o, w, h, "Conductive electrode level detection",
        "Hình 3.9 · Ảnh gốc không đánh số — Phát hiện mức bằng điện cực dẫn: (trái) E1 không "
        "chạm chất lỏng nên mạch hở, relay X không tác động, tiếp điểm ở phía b; (phải) chất lỏng "
        "chạm E1 làm mạch đóng qua E1–E3, relay chuyển sang phía a. E2 tạo mạch tự giữ.",
        "Figure 3.9 · Source image unnumbered — Conductive electrode detection: (left) E1 is out "
        "of the liquid, the circuit is open and relay X stays at the b side; (right) liquid "
        "reaching E1 closes the circuit via E1-E3 and the relay switches to the a side. E2 "
        "forms a self-holding circuit.",
        "Hai binh chua thap va cao voi dien cuoc E1 E2 E3 va relay X",
        "Two tanks at low and high level with electrodes E1 E2 E3 and relay X")


# ---------------------------------------------------------------------------
@_reg
def fig_f10():
    """Closed tank with a dry reference leg for a d/p cell."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Be kin voi chan tham chieu kho / Closed tank with dry reference leg",
               9.0, color=INK, weight="600"))
    o.append(_rect(180, 56, 260, 264, fill="#fbfaf7", sw=1.6))
    o.append(_rect(182, 106, 256, 212, fill="#dfeaf4", sw=0))
    o.append(_line(182, 106, 438, 106, sw=1.4, color=BLUE))
    o.append(T(310, 96, "vung hoi / vapor space", 7.8, color=GREY))
    o.append(T(310, 218, "chat long / liquid", 8.6, color=BLUE))
    o.append(_line(180, 322, 440, 322, sw=1.6, color=INK))
    o.append(_rect(150, 334, 58, 42, fill="#fdf3e6", sw=1.6))
    o.append(T(179, 354, "d/p", 10, color=INK, weight="600"))
    o.append(T(179, 369, "cell", 7.4, color=GREY))
    o.append(_line(200, 322, 200, 334, sw=1.8, color=BLUE))
    o.append(_arrow(208, 324, 208, 338, sw=1.4, color=BLUE))
    o.append(T(222, 350, "HP", 8.2, color=BLUE, anchor="start"))
    o.append(_path("M150,346 L118,346 L118,90 L180,90", sw=2.0, color=GREEN))
    o.append(T(70, 214, "chan kho", 8.0, color=GREEN, anchor="start"))
    o.append(T(70, 230, "dry leg", 8.0, color=GREEN, anchor="start"))
    o.append(_arrow(120, 120, 120, 150, sw=1.2, color=GREEN))
    o.append(T(330, 344, "P hoi / vapor pressure = P v", 7.8, color=GREY))
    o.append(_rect(448, 70, 200, 210, fill="#f5f6f8", sw=1.0))
    o.append(T(548, 92, "Nguon tham chieu / Reference", 8.4, color=INK, weight="600"))
    o.append(T(548, 122, "Chan kho dan ap suat hoi", 7.6, color=GREY))
    o.append(T(548, 138, "toi dau thap cua d/p cell", 7.6, color=GREY))
    o.append(T(548, 168, "Dry leg sends vapor pressure to", 7.6, color=GREY))
    o.append(T(548, 184, "the low-pressure side of the cell", 7.6, color=GREY))
    o.append(T(548, 214, "dung khi hoi khong an mon,", 7.6, color=GREY))
    o.append(T(548, 230, "khong tuy va it ngung tu", 7.6, color=GREY))
    o.append(T(548, 246, "Use when vapor is non-corrosive,", 7.6, color=GREY))
    o.append(T(548, 262, "non-plugging, low condensation", 7.6, color=GREY))
    o.append(_foot(680, 390, "Chan kho giu ap suat tham chieu khong doi, de dang bu ap suat "
                             "tren mat chat long / The dry leg keeps a constant reference "
                             "pressure, compensating for pressure on the liquid surface"))
    return _finish(o, w, h, "Closed tank dry reference leg",
        "Hình 3.10 · Ảnh gốc không đánh số — Bể kín với chân tham chieu khô (dry leg): áp suất "
        "hơi trong vùng hơi được dẫn tới đầu áp suất thấp (LP) của cảm biến d/p, đầu áp suất cao "
        "(HP) nối đáy bể. Dùng khi hơi không ăn mòn, không tắc và ít ngưng tụ.",
        "Figure 3.10 · Source image unnumbered — Closed tank with a dry reference leg: vapor "
        "pressure in the headspace is sent to the low-pressure (LP) side of the d/p cell, while "
        "the high-pressure (HP) side connects to the tank bottom. Used when vapor is "
        "non-corrosive, non-plugging and condenses little.",
        "Be kin voi dau do HP day be va chan tham chieu kho LP",
        "Closed tank with HP bottom connection and dry LP reference leg")


# ---------------------------------------------------------------------------
@_reg
def fig_f11():
    """Closed tank with a wet reference leg for a d/p cell."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Be kin voi chan tham chieu uot / Closed tank with wet reference leg",
               9.0, color=INK, weight="600"))
    o.append(_rect(180, 56, 260, 264, fill="#fbfaf7", sw=1.6))
    o.append(_rect(182, 106, 256, 212, fill="#dfeaf4", sw=0))
    o.append(_line(182, 106, 438, 106, sw=1.4, color=BLUE))
    o.append(T(310, 96, "vung hoi / vapor space", 7.8, color=GREY))
    o.append(T(310, 218, "chat long / liquid", 8.6, color=BLUE))
    o.append(_line(180, 322, 440, 322, sw=1.6, color=INK))
    o.append(_rect(150, 334, 58, 42, fill="#fdf3e6", sw=1.6))
    o.append(T(179, 354, "d/p", 10, color=INK, weight="600"))
    o.append(T(179, 369, "cell", 7.4, color=GREY))
    o.append(_line(200, 322, 200, 334, sw=1.8, color=BLUE))
    o.append(_arrow(208, 324, 208, 338, sw=1.4, color=BLUE))
    o.append(T(222, 350, "HP", 8.2, color=BLUE, anchor="start"))
    o.append(_path("M150,346 L118,346 L118,90 L180,90", sw=2.0, color=GREEN))
    o.append(_line(120, 100, 120, 336, sw=6.0, color="#bfe0cf"))
    o.append(_line(120, 100, 120, 336, sw=1.0, color=GREEN))
    o.append(T(62, 210, "chan uot", 8.0, color=GREEN, anchor="start"))
    o.append(T(62, 226, "wet leg", 8.0, color=GREEN, anchor="start"))
    o.append(T(62, 242, "chat long tro", 7.0, color=GREY, anchor="start"))
    o.append(_rect(104, 58, 32, 28, fill="#fdf3e6", sw=1.2))
    o.append(T(120, 76, "FI", 7.6, color=RED))
    o.append(T(150, 70, "chi thi luu luong / sight indicator", 6.8, color=GREY, anchor="start"))
    o.append(_rect(448, 70, 200, 220, fill="#f5f6f8", sw=1.0))
    o.append(T(548, 92, "Chan uot / Wet leg", 8.4, color=INK, weight="600"))
    o.append(T(548, 122, "Hoi de ngung tu hoac an mon", 7.4, color=GREY))
    o.append(T(548, 138, "nen chan duoc nap chat long tro", 7.4, color=GREY))
    o.append(T(548, 164, "When vapor condenses or is", 7.4, color=GREY))
    o.append(T(548, 180, "corrosive, fill the leg with an", 7.4, color=GREY))
    o.append(T(548, 196, "inert liquid of low expansion", 7.4, color=GREY))
    o.append(T(548, 224, "canh dien SG va chieu cao cot", 7.4, color=GREY))
    o.append(T(548, 240, "tham chieu phai duoc tinh dung", 7.4, color=GREY))
    o.append(T(548, 258, "Cell duoc ha theo hydrostatic", 7.4, color=GREY))
    o.append(T(548, 274, "head; mount a sight indicator", 7.4, color=GREY))
    o.append(_foot(680, 390, "Kho hay uot: chan tham chieu khong doi, chi bien doi la muc trong be / "
                             "Wet or dry: the reference leg stays constant, so only the tank "
                             "level varies"))
    return _finish(o, w, h, "Closed tank wet reference leg",
        "Hình 3.11 · Ảnh gốc không đánh số — Bể kín với chân tham chieu ướt (wet leg): khi hơi "
        "dễ ngưng tụ hoặc ăn mòn, chân tham chieu được đầy chất lỏng trơ giãn nở thấp; có chỉ thị "
        "lưu lượng (FI) ở đỉnh và cảm biến d/p được hạ theo cột thủy tĩnh.",
        "Figure 3.11 · Source image unnumbered — Closed tank with a wet reference leg: when vapor "
        "condenses or is corrosive, the reference leg is filled with an inert low-expansion "
        "liquid; a sight flow indicator (FI) sits at the top and the d/p cell is lowered by the "
        "hydrostatic head.",
        "Be kin voi chan tham chieu uot co chi thi luu luong va dau do HP",
        "Closed tank with wet reference leg, sight indicator and HP connection")


# ---------------------------------------------------------------------------
@_reg
def fig_f12():
    """Overview: contact and non-contact level measurement technologies."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Tong quan cong nghe do muc / Overview of level technologies",
               9.0, color=INK, weight="600"))
    o.append(_rect(250, 44, 180, 46, fill="#e7eef7", sw=1.4))
    o.append(T(340, 65, "Do muc / Level", 9.4, color=INK, weight="600"))
    o.append(T(340, 81, "measurement", 8.0, color=BLUE))
    o.append(_arrow(300, 90, 190, 120, sw=1.2, color=BLUE))
    o.append(_arrow(380, 90, 490, 120, sw=1.2, color=BLUE))
    o.append(_panel(28, 122, 300, 250, "Cam bien tiep xuc / Contact sensors"))
    contact = ["Level sight gauge / Ong nhin", "Float / Phao", "Displacer / Phao chiem",
               "Bubble tube / Ong bat bot", "RF capacitance / Dien dung RF",
               "Resistance tape / Bang dien tro", "Contacting ultrasonic / Sieu am tiep xuc"]
    for i, t in enumerate(contact):
        o.append(T(44, 158 + i * 28, "- " + t, 8.0, color=INK, anchor="start"))
    o.append(_panel(352, 122, 300, 250, "Cam bien khong tiep xuc / Non-contact"))
    noncontact = ["Radar / Radar", "Non-contact ultrasonic / Sieu am",
                  "Load cells / Canh dien tu", "Nuclear / Phong xa",
                  "Guided radar / Radar dan song", "3D solids scanner / Quet 3D"]
    for i, t in enumerate(noncontact):
        o.append(T(368, 158 + i * 30, "- " + t, 8.0, color=INK, anchor="start"))
    o.append(_foot(680, 398, "Moi thiet bi co cach dung rieng; tham khao tai lieu nha san xuat "
                             "truoc khi mua / Every device uses the method differently; consult "
                             "the manufacturer before purchase"))
    return _finish(o, w, h, "Overview of level measurement technologies",
        "Hình 3.12 · Ảnh gốc không đánh số — Phân loại công nghệ đo mức thành cảm biến tiếp "
        "xúc (ống nhìn, phao, phao chìm, ống bọt, điện dung RF, băng điện trở, siêu âm tiếp xúc) "
        "và cảm biến không tiếp xúc (radar, siêu âm, cân điện tử, phóng xạ, radar dẫn sóng, quét 3D).",
        "Figure 3.12 · Source image unnumbered — Level technologies split into contact sensors "
        "(sight gauge, float, displacer, bubble tube, RF capacitance, resistance tape, "
        "contacting ultrasonic) and non-contact sensors (radar, ultrasonic, load cells, "
        "nuclear, guided radar, 3D scanning).",
        "Cay phan loai cam bien do muc tiep xuc va khong tiep xuc",
        "Tree of contact and non-contact level sensor categories")


# ---------------------------------------------------------------------------
@_reg
def fig_f13():
    """Radar blips: reflected pulses on a radar scope."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Tiec hieu radar: xung phan xa / Radar blips: reflected pulses",
               9.0, color=INK, weight="600"))
    cx, cy = 190, 206
    o.append(_circle(cx, cy, 128, fill="#0f2418", sw=1.6))
    for r in (42, 84, 124):
        o.append(_circle(cx, cy, r, fill="none", sw=0.8, color="#3c7a55"))
    o.append(_line(cx - 128, cy, cx + 128, cy, sw=0.6, color="#3c7a55"))
    o.append(_line(cx, cy - 128, cx, cy + 128, sw=0.6, color="#3c7a55"))
    import math as _m
    for a in range(0, 360, 30):
        rad = _m.radians(a)
        o.append(_line(cx + 92 * _m.cos(rad), cy + 92 * _m.sin(rad),
                       cx + 124 * _m.cos(rad), cy + 124 * _m.sin(rad),
                       sw=0.5, color="#3c7a55"))
    o.append(_poly([(cx, cy), (cx + 108 * _m.cos(_m.radians(-58)),
                              cy + 108 * _m.sin(_m.radians(-58))),
                    (cx + 108 * _m.cos(_m.radians(-40)),
                     cy + 108 * _m.sin(_m.radians(-40)))],
                   fill="#1d6b3f", sw=0))
    for bx, by in [(250, 150), (120, 130), (230, 262), (150, 270)]:
        o.append(_circle(bx, by, 5, fill="#9fe870", sw=0))
        o.append(_circle(bx, by, 9, fill="none", sw=0.8, color="#4fbf6a"))
    o.append(T(cx, 352, "man hinh radar / radar screen", 7.6, color=GREY))
    o.append(_panel(360, 56, 288, 280, "Thoi gian bay / Time of flight"))
    o.append(_rect(386, 110, 64, 34, fill="#dfeaf4", sw=1.2))
    o.append(T(418, 131, "Phat", 8.6, color=BLUE))
    o.append(_arrow(452, 126, 560, 126, sw=1.6, color=BLUE))
    o.append(T(506, 118, "xung / pulse", 7.4, color=BLUE))
    o.append(_rect(560, 106, 54, 40, fill="#fdf3e6", sw=1.2))
    o.append(T(587, 131, "Vat", 8.4, color=INK))
    o.append(_arrow(560, 146, 452, 146, sw=1.6, color=RED))
    o.append(T(506, 162, "phan xa / echo", 7.4, color=RED))
    o.append(T(504, 206, "d = (c x t) / 2", 11, color=INK, weight="600"))
    o.append(T(504, 230, "c = toc do anh sang / speed of light", 7.6, color=GREY))
    o.append(T(504, 254, "t = thoi gian bay / time of flight", 7.6, color=GREY))
    o.append(T(504, 286, "Chat dan dien phan xa tot hon", 7.6, color=GREY))
    o.append(T(504, 302, "Conductive materials reflect better", 7.6, color=GREY))
    return _finish(o, w, h, "Radar blips and time of flight",
        "Hình 3.13 · Ảnh gốc không đánh số — (trái) Màn hình radar với các chấm sáng (blips) "
        "là tín hiệu phản xạ; (phải) radar phát xung điện từ tới vật rồi nhận xung phản hồi, "
        "khoảng cách d = c·t/2. Vật dẫn điện phản xạ tốt hơn.",
        "Figure 3.13 · Source image unnumbered — (left) a radar screen with blips showing "
        "reflected signals; (right) radar emits an electromagnetic pulse and receives the echo, "
        "with distance d = c*t/2. Conductive materials reflect the signal better.",
        "Man hinh radar voi cac cham sang va so do thoi gian bay",
        "Radar screen with blips and a time-of-flight diagram")


# ---------------------------------------------------------------------------
@_reg
def fig_f14():
    """Point level versus continuous level measurement."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Do muc diem va lien tuc / Point and continuous level measurement",
               8.8, color=INK, weight="600"))
    for x, title in [(24, "Do muc diem / Point level"), (352, "Do muc lien tuc / Continuous level")]:
        o.append(_panel(x, 44, 300, 260, title))
        o.append(_rect(x + 40, 84, 150, 180, fill="#fbfaf7", sw=1.4))
        o.append(_rect(x + 42, 150, 146, 112, fill="#dfeaf4", sw=0))
        o.append(_line(x + 42, 150, x + 188, 150, sw=1.4, color=BLUE))
    o.append(_line(64, 116, 166, 116, sw=2.0, color=RED))
    o.append(_circle(115, 116, 5, fill=RED))
    o.append(T(115, 108, "cong tac bao cao", 7.0, color=RED))
    o.append(T(115, 200, "chi mot diem / single point", 7.2, color=GREY))
    o.append(T(174, 130, " relay", 7.0, color=RED, anchor="start"))
    o.append(T(174, 146, " ON/OFF", 7.0, color=RED, anchor="start"))
    o.append(_line(392, 96, 392, 250, sw=3.0, color=BLUE))
    for yy in (120, 150, 180, 210, 240):
        o.append(_line(386, yy, 398, yy, sw=1.0, color=BLUE))
    o.append(T(402, 178, "dau do / probe", 7.2, color=BLUE, anchor="start"))
    o.append(T(402, 200, "4-20 mA", 7.6, color=GREEN, anchor="start"))
    o.append(T(402, 216, "ti le voi muc", 7.2, color=GREEN, anchor="start"))
    o.append(_rect(30, 320, 620, 44, fill="#f5f6f8", sw=1.0))
    o.append(T(340, 338, "Diem = mot manh cung (bao cao/dat); Lien tuc = dau ra tuong tu "
                          "cho toan bo dải muc", 8.0, color=INK, weight="600"))
    o.append(T(340, 356, "Point = one discrete height (high/low alarm); Continuous = analog "
                          "output over the whole range", 7.6, color=GREY))
    o.append(_foot(680, 386, "Tin hieu dau ra duoc noi vong dieu khien va chi thi truc quan / "
                             "The output signal links to a control loop and a visual indicator"))
    return _finish(o, w, h, "Point and continuous level measurement",
        "Hình 3.14 · Ảnh gốc không đánh số — (trái) Cảm biến mức điểm đánh dấu một độ cao rời "
        "rạc, thường là báo cao hoặc báo thấp, với relay ON/OFF; (phải) cảm biến liên tục cho "
        "tín hiệu tương tự 4–20 mA tỉ lệ với mức trong toàn dải.",
        "Figure 3.14 · Source image unnumbered — (left) a point sensor marks one discrete height, "
        "usually a high or low alarm, with an ON/OFF relay; (right) a continuous sensor gives a "
        "4-20 mA analog output proportional to level across the whole range.",
        "So sanh cam bien muc diem va cam bien muc lien tuc",
        "Comparison of point and continuous level sensors")


# ---------------------------------------------------------------------------
@_reg
def fig_f15():
    """RF capacitance level sensor: probe and vessel wall as capacitor plates."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Cam bien dien dung: dau do va thanh be la hai ban cuc / "
                        "Capacitance sensor: probe and vessel as plates", 8.6,
               color=INK, weight="600"))
    o.append(_rect(120, 56, 300, 272, fill="#fbfaf7", sw=4.0, stroke="#9aa4ad"))
    o.append(_rect(124, 130, 292, 196, fill="#dfeaf4", sw=0))
    o.append(_line(124, 130, 416, 130, sw=1.4, color=BLUE))
    o.append(_rect(256, 50, 28, 150, fill="#e6c98f", sw=1.4, stroke=RED))
    o.append(T(270, 46, "dau do / probe", 7.4, color=RED))
    o.append(_rect(244, 38, 52, 20, fill="#fdf3e6", sw=1.2))
    o.append(T(270, 52, "RF", 8.4, color=RED))
    o.append(_arrow(430, 150, 420, 150, sw=1.0, color=INK))
    o.append(T(436, 154, "ban cuc 1: dau do / plate 1: probe", 7.6, color=INK, anchor="start"))
    o.append(_arrow(430, 96, 420, 96, sw=1.0, color=INK))
    o.append(T(436, 100, "ban cuc 2: thanh be / plate 2: vessel", 7.6, color=INK, anchor="start"))
    o.append(_arrow(430, 260, 420, 260, sw=1.0, color=INK))
    o.append(T(436, 264, "dien moi: chat long / dielectric: liquid", 7.6, color=INK,
               anchor="start"))
    o.append(_rect(440, 300, 210, 36, fill="#e6f4ee", sw=1.0, stroke=GREEN))
    o.append(T(545, 324, "C tang khi muc tang / C rises with level", 8.2, color=GREEN))
    o.append(_foot(680, 364, "Vat lieu khong dan: chat long lam dien moi, thanh be lam ban cuc; "
                             "vat lieu dan: dau do duoc boc cach dien / Non-conductive material: "
                             "liquid acts as dielectric and wall as plate; conductive material: "
                             "the probe is insulated"))
    o.append(_foot(680, 384, "Dung cho do diem hoac do lien tuc; chat long, bot, bun va be mat "
                             "phan chia / Usable for point or continuous measurement of liquids, "
                             "granules, slurries and interfaces"))
    return _finish(o, w, h, "RF capacitance level sensor",
        "Hình 3.15 · Ảnh gốc không đánh số — Cảm biến điện dung dùng đầu dò và thành bể như "
        "hai bản tụ điện, chất lỏng là điện môi. Khi mức tăng, phần đầu dò bị ngập tăng làm điện "
        "dung tăng; dùng được cho đo điểm hoặc đo liên tục.",
        "Figure 3.15 · Source image unnumbered — A capacitance sensor uses the probe and the "
        "vessel wall as the two capacitor plates, with the liquid as dielectric. As level rises, "
        "more of the probe is covered and capacitance increases; usable for point or continuous "
        "measurement.",
        "Be chua voi dau do dien dung, thanh be va chat long lam dien moi",
        "Tank with capacitance probe, vessel wall and liquid dielectric")


# ---------------------------------------------------------------------------
@_reg
def fig_f16():
    """Radar level transmitter: time-of-flight measurement."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "May phat radar do muc / Radar level transmitter", 9.0,
               color=INK, weight="600"))
    o.append(_rect(110, 56, 300, 280, fill="#fbfaf7", sw=1.6))
    o.append(_rect(112, 156, 296, 178, fill="#dfeaf4", sw=0))
    o.append(_line(112, 156, 408, 156, sw=1.6, color=BLUE))
    o.append(_poly([(238, 56), (282, 56), (274, 78), (246, 78)], fill="#9aa4ad", sw=1.2))
    o.append(T(260, 48, "anten", 7.6, color=GREY))
    o.append(_arrow(260, 82, 214, 156, sw=1.6, color=BLUE))
    o.append(_arrow(306, 82, 352, 156, sw=1.6, color=BLUE))
    o.append(_arrow(214, 152, 258, 86, sw=1.4, color=RED))
    o.append(_arrow(352, 152, 308, 86, sw=1.4, color=RED))
    o.append(_line(260, 78, 260, 156, sw=1.0, color=GREY, dash="4 3"))
    o.append(T(272, 118, "d", 9.0, color=INK))
    o.append(_line(424, 56, 424, 156, sw=1.0, color=GREY, dash="4 3"))
    o.append(T(436, 106, "H", 9.0, color=GREY))
    o.append(_panel(448, 70, 204, 232, "Tinh toan / Calculation"))
    o.append(T(550, 112, "d = c x t / 2", 10.0, color=INK, weight="600"))
    o.append(T(550, 138, "L = H - d", 10.0, color=INK, weight="600"))
    o.append(T(550, 172, "c = toc do song / wave speed", 7.4, color=GREY))
    o.append(T(550, 192, "t = thoi gian bay / flight time", 7.4, color=GREY))
    o.append(T(550, 222, "L = muc chat long", 7.6, color=BLUE))
    o.append(T(550, 238, "level of product", 7.6, color=BLUE))
    o.append(T(550, 266, "Khong anh huong boi khuay, an mon,", 7.2, color=GREY))
    o.append(T(550, 282, "nhiet do, ap suat / unaffected by", 7.2, color=GREY))
    o.append(_foot(680, 384, "Phat xung tan so cao, do thoi gian bay cua xung phan xa tu be mat "
                             "vat; can biet hinh hoc be tinh muc / Emits high-frequency pulses "
                             "and times the echo from the product surface; tank geometry is "
                             "needed to derive the level"))
    return _finish(o, w, h, "Radar level transmitter",
        "Hình 3.16 · Ảnh gốc không đánh số — Máy phát radar treo trên đỉnh bể phát xung xuống "
        "bề mặt vật liệu và nhận phản hồi. Khoảng cách d = c·t/2, mức L = H − d. Không bị ảnh "
        "hưởng bởi khuấy trộn, ăn mòn, nhiệt độ hay áp suất.",
        "Figure 3.16 · Source image unnumbered — A radar transmitter mounted at the tank top "
        "emits pulses toward the product surface and times the echo. Distance d = c*t/2 and "
        "level L = H - d. Unaffected by agitation, corrosion, temperature or pressure.",
        "Be chua voi anten radar phat va nhan xung phan xa",
        "Tank with radar antenna emitting and receiving pulses")


# ---------------------------------------------------------------------------
@_reg
def fig_f17():
    """Guided radar (guided wave radar) level transmitter."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Radar dan song / Guided radar level transmitter", 9.0,
               color=INK, weight="600"))
    o.append(_rect(110, 56, 300, 280, fill="#fbfaf7", sw=1.6))
    o.append(_rect(112, 156, 296, 178, fill="#dfeaf4", sw=0))
    o.append(_line(112, 156, 408, 156, sw=1.6, color=BLUE))
    o.append(_rect(244, 50, 32, 20, fill="#9aa4ad", sw=1.2))
    o.append(T(260, 44, "dau noi / process conn.", 7.2, color=GREY))
    o.append(_line(260, 70, 260, 300, sw=3.6, color="#9aa4ad"))
    o.append(_line(260, 70, 260, 156, sw=1.6, color=BLUE))
    o.append(_arrow(258, 92, 258, 146, sw=1.4, color=BLUE))
    o.append(_arrow(264, 146, 264, 92, sw=1.4, color=RED))
    o.append(_path("M246,156 Q260,168 274,156", sw=1.6, color=GREEN))
    o.append(T(282, 152, "phan xa / reflection", 7.4, color=GREEN, anchor="start"))
    o.append(T(282, 260, "dau do dan song / waveguide probe", 7.4, color=GREY, anchor="start"))
    o.append(_panel(448, 70, 204, 232, "Nguyen ly / Principle"))
    o.append(T(550, 112, "Xung dan theo dau do", 8.0, color=INK))
    o.append(T(550, 132, "Pulses travel along the probe", 7.4, color=GREY))
    o.append(T(550, 162, "Tro khang thay doi tai be mat", 7.8, color=INK))
    o.append(T(550, 180, "Impedance changes at the surface", 7.4, color=GREY))
    o.append(T(550, 212, "d = c x t / 2", 10.0, color=INK, weight="600"))
    o.append(T(550, 240, "Chịu it anh huong be mat ghet", 7.4, color=GREY))
    o.append(T(550, 256, "Less affected by uneven surfaces", 7.4, color=GREY))
    o.append(T(550, 284, "Do chinh xac ~ +/-0.2 mm", 7.4, color=GREEN))
    o.append(_foot(680, 384, "Radar dan song dan xung qua que/dau do; phan xa tai mat chat long "
                             "cho khoang cach truc tiep tu diem ket noi den be mat / Guided radar "
                             "guides pulses along a probe; the surface reflection gives the "
                             "distance from the process connection to the product"))
    return _finish(o, w, h, "Guided radar level transmitter",
        "Hình 3.17 · Ảnh gốc không đánh số — Radar dẫn sóng (guided wave radar) dẫn xung tần "
        "số cao theo đầu dò; khi gặp bề mặt vật liệu trở kháng thay đổi và một phần xung phản xạ. "
        "Thời gian phát–nhận cho khoảng cách trực tiếp tới bề mặt, ít bị ảnh hưởng bởi bề mặt gồ ghề.",
        "Figure 3.17 · Source image unnumbered — Guided wave radar guides high-frequency pulses "
        "along a probe; at the product surface the impedance changes and part of the pulse is "
        "reflected. The launch-to-receive time gives the distance to the surface, with little "
        "sensitivity to uneven surfaces.",
        "Be chua voi dau do radar dan song va phan xa tai mat chat long",
        "Tank with guided-wave radar probe and reflection at the surface")


# ---------------------------------------------------------------------------
@_reg
def fig_f18():
    """Ultrasonic level transmitter: time of flight with sound speed."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "May phat sieu am do muc / Ultrasonic level transmitter", 9.0,
               color=INK, weight="600"))
    o.append(_rect(110, 56, 300, 280, fill="#fbfaf7", sw=1.6))
    o.append(_rect(112, 156, 296, 178, fill="#dfeaf4", sw=0))
    o.append(_line(112, 156, 408, 156, sw=1.6, color=BLUE))
    o.append(_path("M232,70 Q260,46 288,70 Z", fill="#9aa4ad", sw=1.2))
    o.append(T(260, 42, "cam bien / transducer", 7.2, color=GREY))
    o.append(_poly([(260, 74), (198, 156), (322, 156)], fill="#eaf4fb", sw=1.0, color=BLUE))
    o.append(_arrow(260, 80, 218, 152, sw=1.4, color=BLUE))
    o.append(_arrow(260, 80, 302, 152, sw=1.4, color=BLUE))
    o.append(_arrow(224, 150, 254, 84, sw=1.2, color=RED))
    o.append(_arrow(296, 150, 266, 84, sw=1.2, color=RED))
    o.append(_line(260, 72, 260, 156, sw=1.0, color=GREY, dash="4 3"))
    o.append(T(272, 118, "d", 9.0, color=INK))
    o.append(_panel(448, 70, 204, 232, "Tinh toan / Calculation"))
    o.append(T(550, 112, "d = v x t / 2", 10.0, color=INK, weight="600"))
    o.append(T(550, 138, "L = H - d", 10.0, color=INK, weight="600"))
    o.append(T(550, 170, "v = toc do am thanh", 7.6, color=GREY))
    o.append(T(550, 188, "speed of sound (temp. dependent)", 7.2, color=GREY))
    o.append(T(550, 218, "Khong tiep xuc, chi phi thap", 7.4, color=GREY))
    o.append(T(550, 236, "Non-contact, lowest cost", 7.4, color=GREY))
    o.append(T(550, 262, "Can do nhiet do be / measure tank", 7.4, color=GREY))
    o.append(T(550, 278, "temperature; khong co chan khong", 7.4, color=GREY))
    o.append(_foot(680, 384, "Sung phat xung am thanh va nhan tieng vong tu be mat; khac radar "
                             "oa toc do am phu thuoc nhiet do / Emits sound pulses and detects "
                             "the echo; unlike light, sound speed depends on temperature, which "
                             "must be measured"))
    return _finish(o, w, h, "Ultrasonic level transmitter",
        "Hình 3.18 · Ảnh gốc không đánh số — Cảm biến siêu âm phát xung âm thanh và nhận "
        "tiếng vọng từ bề mặt: d = v·t/2, mức L = H − d. Khác radar, tốc độ âm phụ thuộc nhiệt "
        "độ nên phải đo và bù nhiệt độ; không dùng được trong chân không hay áp suất cao.",
        "Figure 3.18 · Source image unnumbered — An ultrasonic sensor emits sound pulses and "
        "detects the echo: d = v*t/2 and level L = H - d. Unlike radar, sound speed depends on "
        "temperature, which must be measured; unsuitable for vacuum or high pressure.",
        "Be chua voi cam bien sieu am phat va nhan tieng vong",
        "Tank with ultrasonic transducer emitting and receiving an echo")


# ---------------------------------------------------------------------------
@_reg
def fig_f19():
    """Solids: uneven surface and acoustic phased-array averaging."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Be mat chat ran ghet va trung binh hoa / Uneven solids surface and "
                        "averaging", 8.6, color=INK, weight="600"))
    o.append(_rect(90, 56, 380, 290, fill="#fbfaf7", sw=1.6))
    surf = [(94, 180), (130, 160), (168, 196), (210, 152), (252, 188),
            (300, 150), (342, 194), (388, 158), (430, 190), (466, 172)]
    o.append(_poly(surf + [(466, 346), (94, 346)], fill="#efe2c4", sw=0))
    o.append(_poly(surf, sw=2.0, color="#b08d3f"))
    o.append(_rect(256, 48, 48, 18, fill="#9aa4ad", sw=1.2))
    o.append(T(280, 42, "phased array", 7.2, color=GREY))
    for ex in (132, 200, 280, 360, 430):
        o.append(_line(280, 70, ex, 170, sw=0.9, color=BLUE, dash="3 3"))
        o.append(_arrow(ex, 168, 280, 76, sw=0.8, color=RED))
    o.append(_line(94, 176, 466, 176, sw=1.4, color=GREEN, dash="6 4"))
    o.append(T(104, 204, "muc trung binh", 7.2, color=GREEN, anchor="start"))
    o.append(T(104, 216, "averaged level", 7.2, color=GREEN, anchor="start"))
    o.append(_panel(490, 80, 166, 210, "Ghi chu / Notes"))
    o.append(T(573, 112, "Radar khong tiep xuc", 7.2, color=GREY))
    o.append(T(573, 130, "bi anh huong be mat ghet", 7.2, color=GREY))
    o.append(T(573, 156, "Radar dan song it bi", 7.2, color=GREY))
    o.append(T(573, 174, "anh huong hon / less", 7.2, color=GREY))
    o.append(T(573, 200, "Am thanh pha mang do", 7.2, color=GREY))
    o.append(T(573, 218, "dien tich lon va lay TB", 7.2, color=GREY))
    o.append(T(573, 244, "Acoustic phased array", 7.2, color=GREY))
    o.append(T(573, 262, "averages a wide area", 7.2, color=GREY))
    o.append(_foot(680, 384, "Thiet bi tap nhieu tieng vong nho roi gop thanh mot tieng vong dai "
                             "dien cho khu vuc do / The device gathers several small echoes and "
                             "merges them into one representing the average of the measured area"))
    return _finish(o, w, h, "Uneven solids surface and averaging",
        "Hình 3.19 · Ảnh gốc không đánh số — Bề mặt chất rắn trong silo gồ ghề với các đỉnh và "
        "hố. Radar dẫn sóng ít bị ảnh hưởng; radar không tiếp xúc bị lệch hướng; công nghệ mảng "
        "pha âm thanh đo trên diện tích rộng và tính mức/trung bình thể tích.",
        "Figure 3.19 · Source image unnumbered — The solid surface in a silo is uneven with peaks "
        "and holes. Guided wave radar is less affected; non-contact radar can be deflected; "
        "acoustic phased-array measures over wide areas and computes an average level and volume.",
        "Silo chat ran voi be mat ghet va cac chum tia trung binh hoa",
        "Silo of solids with uneven surface and averaging beams")


# ---------------------------------------------------------------------------
@_reg
def fig_f20():
    """Solids volume measurement using multiple points / 3D scanner."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 26, "Do the tich chat ran / Solids volume measurement", 9.0,
               color=INK, weight="600"))
    o.append(_rect(90, 56, 380, 290, fill="#fbfaf7", sw=1.6))
    surf = [(96, 176), (150, 158), (208, 190), (270, 156), (332, 188), (400, 160), (466, 184)]
    o.append(_poly(surf + [(466, 346), (96, 346)], fill="#efe2c4", sw=0))
    o.append(_poly(surf, sw=2.0, color="#b08d3f"))
    o.append(_circle(280, 48, 16, fill="#dfeaf4", sw=1.4))
    o.append(T(280, 52, "3D", 8.4, color=BLUE, weight="600"))
    o.append(_path("M306,56 A40,40 0 0 1 254,56", sw=1.2, color=BLUE))
    o.append(_arrow(254, 56, 246, 64, sw=1.2, color=BLUE))
    for px, py in [(140, 170), (200, 184), (260, 162), (320, 182), (390, 166),
                   (170, 200), (240, 196), (300, 204), (370, 200)]:
        o.append(_line(280, 64, px, py, sw=0.6, color=BLUE, dash="2 3"))
        o.append(_circle(px, py, 3, fill=RED, sw=0))
    o.append(T(282, 236, "nhieu diem do / multiple points", 7.4, color=RED))
    o.append(_panel(490, 80, 166, 210, "Ket qua / Output"))
    o.append(T(573, 114, "The tich tong hop", 7.4, color=GREY))
    o.append(T(573, 132, "combined volume", 7.4, color=GREY))
    o.append(T(573, 160, "5708V: silo nho-vua", 7.2, color=GREY))
    o.append(T(573, 178, "5708S: silo vua-lon", 7.2, color=GREY))
    o.append(T(573, 204, "Nhieu thiet bi co the", 7.4, color=GREY))
    o.append(T(573, 222, "noi thanh mot dau ra", 7.4, color=GREY))
    o.append(T(573, 248, "Multiple units combine", 7.4, color=GREY))
    o.append(T(573, 266, "into one volume output", 7.4, color=GREY))
    o.append(_foot(680, 384, "Do the tich yeu cau nhieu diem vi be mat ghet co dinh va ho sau; "
                             "mot thiet bi duy nhat cho ket qua the tich suy dien kem chinh xac / "
                             "Volume needs multiple points because surfaces have peaks and deep "
                             "holes; a single device gives a less accurate inferred volume"))
    return _finish(o, w, h, "Solids volume measurement",
        "Hình 3.20 · Ảnh gốc không đánh số — Đo thể tích chất rắn bằng nhiều điểm đo hoặc máy "
        "quét 3D (Rosemount 5708V/S): các tín hiệu được gộp thành một đầu ra thể tích tổng hợp. "
        "Bề mặt gồ ghề khiến một thiết bị đơn lẻ cho kết quả kém chính xác.",
        "Figure 3.20 · Source image unnumbered — Solids volume measured with multiple points or a "
        "3D scanner (Rosemount 5708V/S); the signals combine into one volume output. Peaks and "
        "holes make a single device give a less accurate inferred volume.",
        "Silo voi may quet 3D va nhieu diem do the tich",
        "Silo with a 3D scanner and multiple volume measurement points")


# ---------------------------------------------------------------------------
@_reg
def fig_f21():
    """Paddlewheel flowmeter: a wheel of paddles inside a pipe."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Dong ho luong luong canh quat / Paddlewheel flowmeter", 9.0,
               color=INK, weight="600"))
    o.append(_rect(70, 130, 460, 120, fill="#e7eef7", sw=1.8, stroke=BLUE))
    o.append(_line(70, 190, 530, 190, sw=0.8, color=BLUE, dash="4 4"))
    o.append(_arrow(84, 190, 178, 190, sw=2.0, color=BLUE))
    o.append(_arrow(422, 190, 516, 190, sw=2.0, color=BLUE))
    o.append(T(130, 168, "dong chay / flow", 7.8, color=BLUE))
    o.append(T(470, 168, "dong chay / flow", 7.8, color=BLUE))
    cx, cy, r = 300, 190, 56
    o.append(_circle(cx, cy, r, fill="#fbfaf7", sw=1.4))
    o.append(_circle(cx, cy, 10, fill="#9aa4ad", sw=1.2))
    for k in range(8):
        a = 2 * math.pi * k / 8
        x1 = cx + 14 * math.cos(a)
        y1 = cy + 14 * math.sin(a)
        x2 = cx + r * math.cos(a)
        y2 = cy + r * math.sin(a)
        o.append(_line(x1, y1, x2, y2, sw=3.0, color="#c08a2e"))
    o.append(_path("M330,150 A48,48 0 0 1 344,190", sw=1.4, color=RED))
    o.append(_arrow(344, 190, 336, 196, sw=1.4, color=RED))
    o.append(T(348, 146, "quay / rotates", 7.4, color=RED, anchor="start"))
    o.append(_rect(268, 88, 64, 30, fill="#fdf3e6", sw=1.2))
    o.append(T(300, 108, "cam bien / sensor", 7.0, color=INK))
    o.append(_line(300, 118, 300, 134, sw=1.2, color=GREY))
    o.append(_rect(562, 130, 96, 120, fill="#f5f6f8", sw=1.2))
    o.append(T(610, 158, "Hien thi", 8.0, color=INK))
    o.append(T(610, 176, "display", 7.6, color=GREY))
    o.append(T(610, 204, "xung / pulses", 7.4, color=GREEN))
    o.append(T(610, 224, "4-20 mA", 7.4, color=GREEN))
    o.append(_line(530, 190, 562, 190, sw=1.2, color=GREY))
    o.append(_foot(680, 296, "Canh quay voi van toc ti le luu luong; cam bien dem vong quay "
                             "va xuat tin hieu / Paddle spins at a speed proportional to flow; "
                             "the sensor counts rotation and outputs a signal"))
    o.append(_foot(680, 316, "Reynolds > 4000 dam bao chay roi loan hoan toan; khong anh huong "
                             "boi trong luong rieng / Reynolds > 4000 ensures fully turbulent "
                             "flow; unaffected by specific gravity"))
    o.append(_foot(680, 336, "Lap dat duoc ngang hoac doc, chay hai chieu; co the cap vanh yeu "
                             "hoac thanh ren / Mounts horizontally or vertically, either flow "
                             "direction; saddle or threaded mounts available"))
    return _finish(o, w, h, "Paddlewheel flowmeter",
        "Hình 3.21 · Ảnh gốc không đánh số — Đồng hồ lưu lượng cánh quạt: một bánh xe có "
        "nhiều cánh quay trong ống, tốc độ tỉ lệ với lưu lượng; cảm biến đếm vòng và cho đầu ra "
        "xung/4–20 mA. Lắp được ngang hoặc dọc, hai chiều dòng chảy; cần Reynolds > 4000.",
        "Figure 3.21 · Source image unnumbered — A paddlewheel flowmeter: a wheel with several "
        "paddles spins inside the pipe at a speed proportional to flow; the sensor counts "
        "rotation and gives a pulse/4-20 mA output. Mounts horizontally or vertically, either "
        "flow direction; requires Reynolds > 4000.",
        "Ong dan voi banh xe canh quay va cam bien dem vong",
        "Pipe with a rotating paddlewheel and a rotation sensor")
