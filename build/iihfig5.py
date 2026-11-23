# -*- coding: utf-8 -*-
"""Vector figures for Chapter 5 "Measurement of Flow Rate" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 181-216 (printed pp. 167-202).

The ten source figures are photographic or line drawings with short numbered
captions.  They are redrawn here as simplified bilingual vector schematics.
Every function returns the standard 5-tuple ``(svg, caption_vi, caption_en,
aria_vi, aria_en)`` through ``_finish()``.  All SVG text is XML-escaped with
``esc()``/``T()``.  Captions keep the source figure order 1 through 10.
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
    """Orifice plate with a differential-pressure manometer."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Do luong bang lo va dong ho chenh ap / "
                        "Orifice and pressure-differential measurement",
               8.6, color=INK, weight="600"))
    # Pipe cross-section (top) with the orifice plate at x = 340.
    o.append(_rect(60, 90, 560, 60, fill="#eef3fb", sw=1.8))
    o.append(_line(60, 120, 330, 120, sw=0, color=BLUE))
    o.append(_arrow(96, 120, 178, 120, sw=2.0, color=BLUE))
    o.append(T(120, 108, "Chay / Flow", 7.2, color=BLUE))
    o.append(_rect(336, 90, 8, 25, fill="#9aa4ad", sw=1.0))
    o.append(_rect(336, 125, 8, 25, fill="#9aa4ad", sw=1.0))
    # Pressure legs down to the U-tube manometer.
    o.append(_line(276, 150, 276, 210, sw=1.5, color=INK))
    o.append(_line(276, 210, 306, 210, sw=1.5, color=INK))
    o.append(_line(404, 150, 404, 210, sw=1.5, color=INK))
    o.append(_line(404, 210, 374, 210, sw=1.5, color=INK))
    o.append(_rect(302, 210, 8, 96, fill="#fbfaf7", sw=1.6))
    o.append(_rect(370, 210, 8, 96, fill="#fbfaf7", sw=1.6))
    o.append(_path("M306,306 A34,34 0 0 0 374,306", sw=1.6, color=INK))
    o.append(_rect(302, 252, 8, 54, fill="#d9e6f2", sw=0))
    o.append(_rect(370, 282, 8, 24, fill="#d9e6f2", sw=0))
    o.append(_path("M302,282 A34,34 0 0 0 370,312 L370,306 A34,34 0 0 1 302,276 Z",
                   fill="#bcd3e6", sw=0))
    o.append(_line(306, 252, 348, 252, sw=0.9, color=BLUE, dash="4 3"))
    o.append(_line(374, 282, 332, 282, sw=0.9, color=BLUE, dash="4 3"))
    o.append(T(340, 246, "h", 9.0, color=RED))
    # Numbered callouts.
    for args in [(92, 120, 1), (340, 78, 2), (276, 172, 3), (404, 172, 4),
                 (340, 330, 5)]:
        o.append(_num(*args))
    o.append(_foot(680, 358, "1. Dong chay / Flow - 2. Dia lo / Orifice plate - "
                             "3. Tap thuong / Upstream tap - 4. Tap xuong / Downstream tap - "
                             "5. Dong ho chenh ap / DP manometer"))
    o.append(_foot(680, 382, "Chenh ap h cho biet luong Q theo quan he can bac hai / "
                             "The head difference h gives Q through a square-root relation"))
    return _finish(o, w, h, "Orifice and pressure-differential measurement",
        "Hình 5.1 · Đo lưu lượng bằng tấm lỗ và đồng hồ chênh áp: chất lỏng chảy trong ống qua tấm "
        "lỗ, hai đường dẫn áp ở thượng lưu và hạ lưu nối tới ống chữ U. Chênh áp cột chất lỏng h "
        "dùng để suy ra lưu lượng.",
        "Figure 5.1 · Flow measurement with an orifice plate and a differential manometer: fluid "
        "flows through the plate, and upstream and downstream pressure legs feed a U-tube. The "
        "liquid-column difference h gives the flow rate.",
        "Ống dẫn có tấm lỗ và đồng hồ chênh áp chữ U",
        "Pipe with an orifice plate and a U-tube differential manometer")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Flow pattern and vena contracta downstream of an orifice plate."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Dong chay qua dia lo / Flow pattern with orifice plate",
               9.0, color=INK, weight="600"))
    o.append(_line(56, 90, 624, 90, sw=2.0, color=INK))
    o.append(_line(56, 290, 624, 290, sw=2.0, color=INK))
    # Orifice plate with a sharp upstream edge.
    o.append(_rect(246, 90, 8, 82, fill="#9aa4ad", sw=1.2))
    o.append(_rect(246, 208, 8, 82, fill="#9aa4ad", sw=1.2))
    o.append(_poly([(246, 172), (258, 190), (246, 208)],
                   fill="#f6e6c8", sw=1.2, close=True))
    # Streamlines converge to the vena contracta then diverge again.
    o.append(_path("M60,102 L196,102 Q246,102 312,176 Q410,102 620,102", sw=1.3, color=BLUE))
    o.append(_path("M60,128 L196,128 Q246,128 312,182 Q410,128 620,128", sw=1.3, color=BLUE))
    o.append(_path("M60,152 L196,152 Q246,152 312,187 Q410,152 620,152", sw=1.3, color=BLUE))
    o.append(_line(60, 190, 620, 190, sw=0.9, color=GREY, dash="6 5"))
    o.append(_path("M60,228 L196,228 Q246,228 312,193 Q410,228 620,228", sw=1.3, color=BLUE))
    o.append(_path("M60,252 L196,252 Q246,252 312,198 Q410,252 620,252", sw=1.3, color=BLUE))
    o.append(_path("M60,278 L196,278 Q246,278 312,204 Q410,278 620,278", sw=1.3, color=BLUE))
    o.append(_arrow(270, 190, 350, 190, sw=2.4, color=RED))
    o.append(_arrow(410, 190, 470, 190, sw=1.6, color=RED))
    # Labels and callouts.
    o.append(_bl(130, 72, "1. Dau vao / inlet", "Flow approaches the sharp edge", 7.0))
    o.append(_bl(420, 74, "4. Phuc hoi / recovery", "Velocity falls, pressure rises", 7.0))
    for args in [(250, 76, 1), (312, 244, 2), (246, 232, 3), (486, 250, 4)]:
        o.append(_num(*args))
    o.append(T(312, 262, "2. Vena contracta", 7.6, color=RED, weight="600"))
    o.append(T(312, 274, "V max, P min / max velocity, min pressure", 7.0, color=GREY))
    o.append(_bl(150, 322, "Mat cat chay co hieu qua / Effective flow section",
                 "giam sau dia lo / reduced downstream of the plate", 7.2))
    o.append(_foot(680, 372, "Canh sac dau vao tao tiep xuc gan nhu thuan tuy giua chat long va ban / "
                             "The sharp leading edge gives almost pure line contact with the fluid"))
    return _finish(o, w, h, "Flow pattern with orifice plate",
        "Hình 5.2 · Dòng chảy qua tấm lỗ: các đường dòng hội tụ sau tấm lỗ, đạt tiết diện nhỏ nhất "
        "tại vena contracta, ở đó vận tốc lớn nhất và áp suất nhỏ nhất; sau đó dòng giãn ra và áp "
        "suất phục hồi một phần.",
        "Figure 5.2 · Flow pattern through an orifice plate: the streamlines converge just after "
        "the plate and reach their smallest section at the vena contracta, where velocity is "
        "maximum and pressure minimum; the flow then expands and pressure partly recovers.",
        "Các đường dòng hội tụ tại vena contracta sau tấm lỗ",
        "Streamlines converging at the vena contracta behind an orifice plate")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Three orifice plate types, front and side views."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Ba loai dia lo / Three types of orifice plate",
               9.0, color=INK, weight="600"))
    specs = [
        (24, "Dong tam / Concentric", "con"),
        (238, "Lech tam / Eccentric", "ecc"),
        (452, "Doan / Segmental", "seg"),
    ]
    for x, label, kind in specs:
        cx = x + 102
        o.append(_panel(x, 44, 204, 276, label))
        o.append(_circle(cx, 132, 44, fill="#fbfaf7", sw=1.6))
        if kind == "con":
            o.append(_circle(cx, 132, 18, fill="#dfeaf4", sw=1.3))
        elif kind == "ecc":
            o.append(_circle(cx + 12, 144, 18, fill="#dfeaf4", sw=1.3))
        else:
            o.append(_poly([(cx - 32, 152), (cx + 32, 152), (cx + 26, 160),
                            (cx - 26, 160)], fill="#dfeaf4", sw=1.3, close=True))
        o.append(T(cx, 192, "Mat truoc / Front view", 7.2, color=GREY))
        # Side view: plate in cross-section with the bore as a gap.
        o.append(_rect(cx - 60, 226, 120, 12, fill="#9aa4ad", sw=1.2))
        if kind == "con":
            o.append(_rect(cx - 18, 226, 36, 12, fill="#dfeaf4", sw=0))
        elif kind == "ecc":
            o.append(_rect(cx - 4, 226, 36, 12, fill="#dfeaf4", sw=0))
        else:
            o.append(_rect(cx - 30, 226, 60, 12, fill="#dfeaf4", sw=0))
        o.append(T(cx, 262, "Mat cat / Side view", 7.2, color=GREY))
        o.append(T(cx, 294, "chat sach / clean fluid" if kind == "con" else
                   "chat co ran / with solids", 7.0,
                   color=GREEN if kind == "con" else RED))
    o.append(_foot(680, 350, "Lo dong tam cho chat sach; lo lech tam va lo doan cho chat chua ran, "
                             "bun hoac khi co hat / Concentric for clean fluids; eccentric and "
                             "segmental for solids and slurries"))
    return _finish(o, w, h, "Sketch of orifices of different types",
        "Hình 5.3 · Ba loại tấm lỗ, mỗi loại xem ở mặt trước và mặt cắt: đồng tâm (lỗ ở giữa, dùng "
        "cho chất sạch), lệch tâm (lỗ dịch khỏi tâm) và dạng đoạn (lỗ là một đoạn của đường tròn).",
        "Figure 5.3 · Three orifice plate types, each in front and side view: concentric (central "
        "bore, for clean fluids), eccentric (offset bore) and segmental (a circular segment).",
        "Ba loại tấm lỗ: đồng tâm, lệch tâm và dạng đoạn",
        "Three orifice plate types: concentric, eccentric and segmental")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Three machining methods for the orifice edge."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Gia cong lo / Machining methods of orifices",
               9.0, color=INK, weight="600"))
    specs = [
        (24, "Loai 1 / Type 1", "bevel"),
        (238, "Loai 2 / Type 2", "square"),
        (452, "Loai 3 / Type 3", "quadrant"),
    ]
    for x, label, kind in specs:
        cx = x + 102
        o.append(_panel(x, 44, 204, 272, label))
        o.append(_line(cx - 78, 120, cx + 78, 120, sw=1.6, color=GREY))
        o.append(_line(cx - 78, 152, cx + 78, 152, sw=1.6, color=GREY))
        o.append(_rect(cx - 70, 120, 52, 32, fill="#c9d2d9", sw=1.2))
        o.append(_rect(cx + 18, 120, 52, 32, fill="#c9d2d9", sw=1.2))
        if kind == "bevel":
            o.append(_poly([(cx - 18, 120), (cx - 18, 128), (cx, 152),
                            (cx + 18, 152), (cx + 18, 128), (cx + 18, 120)],
                           fill="#f6e6c8", sw=1.2, close=True))
        elif kind == "square":
            o.append(_rect(cx - 18, 120, 36, 32, fill="#f6e6c8", sw=1.2))
        else:
            o.append(_path("M%d,120 Q%d,140 %d,140 L%d,152 L%d,152 L%d,120 Z"
                           % (cx - 20, cx - 20, cx, cx, cx + 20, cx + 20),
                           fill="#f6e6c8", sw=1.2))
        o.append(_arrow(cx, 98, cx, 116, sw=1.4, color=BLUE))
        o.append(T(cx, 90, "dau vao / inlet", 7.0, color=BLUE))
        o.append(_bl(cx, 188, "canh sac / sharp edge", "bevel sau / downstream bevel"
                     if kind == "bevel" else
                     ("canh vuong / square edge" if kind == "square" else
                      "canh goc tu / quadrant edge"), 7.2))
        o.append(T(cx, 238, "t = chieu day ban / plate thickness", 6.8, color=GREY))
        o.append(T(cx, 272, "D / d = ti le duong kinh", 7.0, color=INK))
        o.append(T(cx, 286, "diameter ratio beta", 6.6, color=GREY))
    o.append(_foot(680, 350, "Loai 1 va 2 de che tao va lap lai; F duoc goi la 'plater' trong nguon. "
                             "Loai 3 (canh goc tu) dung cho chat nhot cao / Types 1 and 2 are "
                             "easy to reproduce; type 3 suits viscous fluids"))
    return _finish(o, w, h, "Machining methods of orifices",
        "Hình 5.4 · Ba phương pháp gia công mép lỗ: loại 1 có vát ở phía sau, loại 2 có mép vuông "
        "hai mặt và loại 3 có mép góc tư (quadrant edge) dùng cho chất lỏng nhớt cao. F được nguồn "
        "gọi là 'plater'.",
        "Figure 5.4 · Three machining methods for the orifice edge: type 1 has a downstream "
        "bevel, type 2 a square edge and type 3 a quadrant edge used for viscous fluids. F is "
        "called the 'plater' in the source.",
        "Ba cách gia công mép lỗ tấm lỗ",
        "Three machining methods for the orifice edge")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Five standard pressure-tap locations on an orifice plate."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 26, "Vi tri cac diem lay ap / Location of pressure taps",
               9.0, color=INK, weight="600"))
    rows = [
        (94, "Mat bich / Flange", "25 mm / 25 mm", 356, 364),
        (146, "Vena contracta", "1D / venacontracta", 258, 384),
        (198, "Ban kinh / Radius", "1D / 0.5D", 258, 390),
        (250, "Ong / Pipe", "2.5D / 8D", 206, 480),
        (302, "Goc / Corner", "tai goc / at corner", 356, 364),
    ]
    for yy, name, dist, x1, x2 in rows:
        o.append(_rect(150, yy, 420, 26, fill="#eef3fb", sw=1.3))
        o.append(_rect(358, yy, 4, 26, fill="#9aa4ad", sw=1.0))
        o.append(T(244, yy + 17, name, 7.6, color=INK, weight="600"))
        o.append(T(468, yy + 17, dist, 7.2, color=BLUE))
        o.append(_poly([(x1 - 5, yy), (x1 + 5, yy), (x1, yy - 8)],
                       fill=RED, sw=0.8, close=True))
        o.append(_poly([(x2 - 5, yy), (x2 + 5, yy), (x2, yy - 8)],
                       fill=GREEN, sw=0.8, close=True))
    o.append(T(340, 348, "d1 = tap thuong luu / upstream - d2 = tap ha luu / downstream",
               7.6, color=INK))
    o.append(_foot(680, 374, "Mat bich 25 mm; vena contracta = ap suat nho nhat; radius = D/2; "
                             "ong = 2.5D va 8D; goc dung cho ong nho hon 50 mm / "
                             "Flange 25 mm; radius D/2; pipe 2.5D and 8D; corner below 50 mm"))
    o.append(T(340, 400, "D = duong kính ong, beta = d/D / pipe diameter, beta = d/D",
               7.0, color=GREY))
    return _finish(o, w, h, "Location of pressure taps with orifice plate",
        "Hình 5.5 · Năm vị trí lấy áp thông thường với tấm lỗ: mặt bích (25 mm), vena contracta, "
        "bán kính (0,5D), ống (2,5D thượng lưu và 8D hạ lưu) và góc (ống dưới 50 mm).",
        "Figure 5.5 · Five common pressure-tap locations with an orifice plate: flange (25 mm), "
        "vena contracta, radius (0.5D), pipe (2.5D upstream and 8D downstream) and corner (pipes "
        "under 50 mm).",
        "Năm vị trí lấy áp trên đường ống có tấm lỗ",
        "Five pressure-tap locations on a pipe with an orifice plate")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Classic long-form Venturi tube with an annular throat chamber."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Venturi dai kinh dien / Classic long form Venturi",
               9.0, color=INK, weight="600"))
    body = [(60, 120), (180, 120), (300, 160), (400, 160), (600, 120),
            (600, 240), (400, 200), (300, 200), (180, 240), (60, 240)]
    o.append(_poly(body, fill="#eef3fb", sw=1.8, close=True))
    o.append(_line(60, 180, 600, 180, sw=0.9, color=GREY, dash="6 5"))
    # Annular chamber above the throat with internal and external taps.
    o.append(_rect(320, 138, 60, 22, fill="#fdf3e6", sw=1.4))
    for tx in (330, 342, 354, 366, 378):
        o.append(_line(tx, 160, tx, 168, sw=1.0, color=GREY))
    o.append(_line(350, 138, 350, 108, sw=1.6, color=BLUE))
    o.append(_circle(350, 104, 5, fill=BLUE))
    o.append(_line(140, 120, 140, 96, sw=1.6, color=RED))
    o.append(_circle(140, 92, 5, fill=RED))
    # Top labels.
    o.append(_bl(120, 70, "1. Doan vao / inlet", "straight pipe section", 7.0))
    o.append(_bl(240, 70, "2. Cone hoi tu", "converging cone", 7.0))
    o.append(_bl(350, 88, "3. Co hong / throat", "constant velocity", 7.0))
    o.append(_bl(520, 70, "4. Cone phuc hoi", "diverging recovery cone", 7.0))
    o.append(T(470, 150, "5. Buong nhan / annular chamber", 7.2, color=INK,
               anchor="start"))
    o.append(T(470, 164, "6-8 taps, 4 external", 6.8, color=GREY, anchor="start"))
    o.append(_arrow(120, 180, 180, 180, sw=1.4, color=BLUE))
    o.append(_foot(680, 352, "1. Inlet - 2. Converging cone - 3. Throat - 4. Recovery cone - "
                             "5. Annular chamber (6-8 internal taps averaged)"))
    o.append(_foot(680, 378, "Goc phuc hoi nho giup gan nhu phuc hoi toan bo ap suat dau vao / "
                             "The small recovery angle recovers nearly all the inlet head"))
    return _finish(o, w, h, "Classic long form Venturi",
        "Hình 5.6 · Venturi dạng dài kinh điển: đoạn vào thẳng, côn hội tụ, cổ họng hình trụ có "
        "buồng nhận áp vòng (6–8 lỗ trong, 4 lỗ ngoài) và côn phục hồi dài lấy lại gần như toàn bộ "
        "cột áp ban đầu.",
        "Figure 5.6 · Classic long-form Venturi: a straight inlet, a converging cone, a cylindrical "
        "throat with an annular averaging chamber (6-8 internal and 4 external taps), and a long "
        "recovery cone that recovers nearly all of the inlet head.",
        "Ống Venturi dạng dài với buồng nhận áp vòng ở cổ họng",
        "Long-form Venturi with an annular pressure chamber at the throat")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Short-form Venturi tube with a single throat tap."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Venturi dang ngan / Short form Venturi",
               9.0, color=INK, weight="600"))
    body = [(80, 120), (200, 120), (280, 160), (360, 160), (540, 120),
            (600, 120), (600, 240), (540, 240), (360, 200), (280, 200),
            (200, 240), (80, 240)]
    o.append(_poly(body, fill="#eef3fb", sw=1.8, close=True))
    o.append(_line(80, 180, 600, 180, sw=0.9, color=GREY, dash="6 5"))
    # One throat tap (no annular chamber) and the inlet tap.
    o.append(_line(320, 160, 320, 116, sw=1.6, color=BLUE))
    o.append(_circle(320, 112, 5, fill=BLUE))
    o.append(_line(150, 120, 150, 96, sw=1.6, color=RED))
    o.append(_circle(150, 92, 5, fill=RED))
    o.append(_bl(140, 70, "1. Doan vao / inlet", "high-pressure tap", 7.0))
    o.append(_bl(320, 72, "2. Co hong / throat", "single pressure tap", 7.0))
    o.append(_bl(510, 70, "3. Cone ra 21 do", "21 degree recovery cone", 7.0))
    o.append(_bl(430, 280, "Khong buong nhan / no annular chamber",
                 "or an external averaging chamber may be used", 7.2))
    o.append(_arrow(110, 180, 180, 180, sw=1.4, color=BLUE))
    o.append(_foot(680, 352, "The he so ngan va re hon / A shorter, lower-cost second generation "
                             "of Venturi tubes, welded from compatible materials"))
    o.append(_foot(680, 378, "Goc cone phuc hoi tang tu 7 do len 21 do so voi dang dai / "
                             "The recovery angle increased from 7 to 21 degrees"))
    return _finish(o, w, h, "Short form Venturi",
        "Hình 5.7 · Venturi dạng ngắn: thay buồng nhận áp vòng bằng một lỗ đo duy nhất (hoặc buồng "
        "nhận áp ngoài), đồng thời tăng góc côn phục hồi từ 7° lên 21° nhằm giảm chiều dài và chi phí.",
        "Figure 5.7 · Short-form Venturi: the internal annular chamber is replaced by a single "
        "pressure tap (or an external averaging chamber), and the recovery cone angle is increased "
        "from 7 to 21 degrees to reduce cost and laying length.",
        "Ống Venturi dạng ngắn với một lỗ lấy áp ở cổ họng",
        "Short-form Venturi with a single throat pressure tap")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """Flange-type flow nozzle between pipe flanges."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 26, "Voi phun_loai mat bich / Flange type flow nozzle",
               9.0, color=INK, weight="600"))
    o.append(_rect(70, 120, 540, 120, fill="#eef3fb", sw=1.8))
    o.append(_poly([(300, 120), (370, 120), (378, 162), (378, 198),
                    (370, 240), (300, 240), (322, 190), (322, 170)],
                   fill="#f6e6c8", sw=1.6, close=True))
    # Flanges and bolts.
    o.append(_rect(292, 100, 10, 160, fill="#c9d2d9", sw=1.2))
    o.append(_rect(378, 100, 10, 160, fill="#c9d2d9", sw=1.2))
    for by in (112, 140, 220, 248):
        o.append(_line(290, by, 304, by, sw=1.0, color=GREY))
        o.append(_line(376, by, 390, by, sw=1.0, color=GREY))
    o.append(_arrow(120, 180, 220, 180, sw=1.8, color=BLUE))
    o.append(_arrow(400, 180, 470, 180, sw=1.4, color=RED))
    o.append(_line(270, 120, 270, 88, sw=1.6, color=RED))
    o.append(_circle(270, 84, 5, fill=RED))
    o.append(_line(420, 120, 420, 88, sw=1.6, color=GREEN))
    o.append(_circle(420, 84, 5, fill=GREEN))
    o.append(_bl(170, 72, "1. Mat bich / flange", "bolted between pipe flanges", 7.0))
    o.append(_bl(345, 288, "2. Voi phun / nozzle", "smooth convergent section", 7.2))
    o.append(_bl(510, 288, "3. Tap ap / pressure taps", "upstream and downstream", 7.2))
    o.append(_foot(680, 352, "Dau ra song song voi truc ong, duong kính bang vena contracta "
                             "cua lo tuong duong / Discharge parallel to the pipe axis with the "
                             "diameter of an equal-capacity orifice vena contracta"))
    return _finish(o, w, h, "Flow nozzle",
        "Hình 5.8 · Vòi phun lưu lượng dạng mặt bích: đoạn hội tụ nhẵn được kẹp giữa hai mặt bích, "
        "đầu ra song song với trục ống và có đường kính bằng vena contracta của tấm lỗ tương "
        "đương; áp suất thượng lưu và hạ lưu được đo bằng cảm biến chênh áp.",
        "Figure 5.8 · A flange-type flow nozzle: a smooth convergent section clamped between pipe "
        "flanges, discharging parallel to the pipe axis with the diameter of an equal-capacity "
        "orifice vena contracta; upstream and downstream pressures feed a DP sensor.",
        "Vòi phun dạng mặt bích kẹp giữa hai mặt bích ống",
        "Flange-type flow nozzle clamped between pipe flanges")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """(a) ASME long-radius and (b) Simplex flow nozzles."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "(a) ASME long-radius (b) Simplex - hai kieu voi phun / "
                        "two nozzle designs", 8.8, color=INK, weight="600"))
    o.append(_panel(24, 44, 308, 288, "(a) ASME long-radius / ban kinh dai"))
    o.append(_panel(348, 44, 308, 288, "(b) Simplex / loai Simplex"))
    for ox, kind in [(178, "asme"), (502, "simplex")]:
        o.append(_rect(ox - 110, 150, 220, 96, fill="#eef3fb", sw=1.4))
        if kind == "asme":
            o.append(_path("M%d,150 Q%d,150 %d,178 L%d,178 L%d,150 Z"
                           % (ox - 92, ox - 30, ox + 20, ox + 78, ox + 92),
                           fill="#f6e6c8", sw=1.4))
            o.append(_path("M%d,246 Q%d,246 %d,218 L%d,218 L%d,246 Z"
                           % (ox - 92, ox - 30, ox + 20, ox + 78, ox + 92),
                           fill="#f6e6c8", sw=1.4))
        else:
            o.append(_path("M%d,150 Q%d,164 %d,180 L%d,180 L%d,150 Z"
                           % (ox - 92, ox - 20, ox + 30, ox + 78, ox + 92),
                           fill="#f6e6c8", sw=1.4))
            o.append(_path("M%d,246 Q%d,232 %d,216 L%d,216 L%d,246 Z"
                           % (ox - 92, ox - 20, ox + 30, ox + 78, ox + 92),
                           fill="#f6e6c8", sw=1.4))
        o.append(_arrow(ox - 96, 198, ox - 40, 198, sw=1.6, color=BLUE))
        o.append(_arrow(ox + 40, 198, ox + 96, 198, sw=1.4, color=RED))
        o.append(T(ox, 274, "mat cat / section", 7.2, color=GREY))
        o.append(T(ox, 300, "gang / gun metal, inox, bronze, monel", 6.8, color=INK))
    o.append(_foot(680, 360, "Vat lieu thuong dung: gang, thep khong g, dong thanh va monel; "
                             "co the ma crom hoac phu stellite chong mon / Common materials are "
                             "gun metal, stainless steel, bronze and monel, often chromium plated"))
    o.append(_foot(680, 386, "Chu thich nguon cho hinh 9 ket thuc bang 'tg' (OCR) - giu nguyen "
                             "trong ban Anh / The source caption ends with 'tg' (OCR)"))
    return _finish(o, w, h, "ASME long-radius and Simplex flow nozzles",
        "Hình 5.9 · (a) Vòi phun ASME bán kính dài và (b) vòi phun loại Simplex. Cả hai được chế "
        "tạo từ gang, thép không gỉ, đồng thanh hoặc monel, thường mạ crom; chú thích nguồn kết "
        "thúc bằng 'tg' (lỗi OCR).",
        "Figure 5.9 · (a) The ASME long-radius and (b) the Simplex flow nozzles. Both are made of "
        "gun metal, stainless steel, bronze or monel and are often chromium plated. The source "
        "caption ends with 'tg' (an OCR artifact).",
        "Hai kiểu vòi phun ASME bán kính dài và Simplex",
        "Two flow nozzle designs: ASME long-radius and Simplex")


# ---------------------------------------------------------------------------
@_reg
def fig_f10():
    """Dall tube with inlet shoulder, annular slot and outlet cone."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 26, "Ong Dall / Dall tube",
               9.0, color=INK, weight="600"))
    body = [(80, 120), (220, 120), (220, 150), (300, 166), (320, 166),
            (320, 172), (520, 120), (600, 120), (600, 240), (520, 240),
            (320, 194), (320, 200), (300, 200), (220, 210), (220, 240),
            (80, 240)]
    o.append(_poly(body, fill="#eef3fb", sw=1.8, close=True))
    o.append(_line(80, 180, 600, 180, sw=0.9, color=GREY, dash="6 5"))
    # High-pressure tap at the inlet shoulder, low-pressure tap at the slot.
    o.append(_line(226, 150, 226, 88, sw=1.6, color=RED))
    o.append(_circle(226, 84, 5, fill=RED))
    o.append(_line(310, 166, 310, 96, sw=1.6, color=BLUE))
    o.append(_circle(310, 92, 5, fill=BLUE))
    o.append(_bl(160, 62, "1. Vai vao / inlet shoulder", "abrupt diameter decrease", 7.0))
    o.append(_bl(350, 62, "2. Khe hong / throat slot", "low pressure measured here", 7.0))
    o.append(_bl(520, 62, "3. Cone ra / outlet cone", "pressure recovery", 7.0))
    o.append(T(232, 282, "4. Tap cao / high-pressure tap", 7.2, color=RED,
               anchor="start"))
    o.append(T(430, 282, "5. Tap thap / low-pressure tap", 7.2, color=BLUE,
               anchor="start"))
    o.append(_arrow(110, 180, 180, 180, sw=1.4, color=GREEN))
    o.append(_foot(680, 330, "AP gan gap doi venturi cung duong kinh, ton that khoang 5%, "
                             "phuc hoi den 95% / DP is nearly double a comparable venturi with "
                             "about 5% loss and up to 95% recovery"))
    o.append(_foot(680, 360, "Khong dung cho chat long co ran co the lang dong trong khe hong / "
                             "Unsuitable for fluids with solids that settle in the throat slot"))
    o.append(_foot(680, 388, "Dung cho nuoc, nuoc thai, khong va hoi; vat lieu gang hoac gang "
                             "xam chat luong cao / Used for water, sewage, air and steam"))
    return _finish(o, w, h, "Dall tube",
        "Hình 5.10 · Ống Dall: thân có mặt bích với đoạn vào thẳng kết thúc bằng vai giảm đường "
        "kính đột ngột, côn vào và côn ra ngăn bằng khe hở hình vòng. Áp suất cao đo tại vai vào, "
        "áp suất thấp đo tại khe cổ họng.",
        "Figure 5.10 · A Dall tube: a flanged body with a short straight inlet ending in an abrupt "
        "inlet shoulder, an inlet cone and an outlet cone separated by a narrow annular slot. High "
        "pressure is measured at the shoulder and low pressure at the slotted throat.",
        "Ống Dall với vai vào, khe hở vòng và côn phục hồi",
        "Dall tube with inlet shoulder, annular slot and recovery cone")
