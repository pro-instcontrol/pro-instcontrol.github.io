# -*- coding: utf-8 -*-
"""Vector redraws of Figures 8.1-8.9 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 8 "Apparatus to European Standards".

All nine drawings are simplified sectional / elevation redraws of the printed
page images.  Captions follow the printed wording with a bilingual prefix;
letter legends and numeric values are transcribed from the pages.  Architecture
mirrors `mcmillanfig06.py`: every figure returns the standard five-tuple through
`vfig._fig()` and is registered in `FIGS` by the `_reg` decorator, while the
named callables `fig_f801()` ... `fig_f809()` remain the public API.
"""
import sys
import os
import math

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, BLUE, RED, GREEN, _arrow, _circle, _ellipse,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Displayed strings are pre-vetted Unicode with no XML special chars."""
    return str(s)


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _defs8():
    """Arrow markers plus the hatch / stipple fills used by the sections."""
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a7" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="sect" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#5f6b73" stroke-width="0.7"/>'
            '</pattern>'
            '<pattern id="comp" width="7" height="7" patternUnits="userSpaceOnUse">'
            '<circle cx="2" cy="2" r="0.8" fill="#5f6b73"/>'
            '<circle cx="5" cy="5" r="0.8" fill="#5f6b73"/>'
            '</pattern>'
            '</defs>' % (INK, INK))


def _title(o, n, vi, en, size=8.4):
    o.append(T(340, 15, "Hình 8.%d · %s / Figure 8.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, y=29, size=6.4):
    o.append(T(340, y, s, size, color=GREY))


def _wrap(s, n):
    out, cur = [], ""
    for w in str(s).split():
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= n:
            cur += " " + w
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def _para(o, x, y, s, size=6.4, maxchars=60, lh=11.0, anchor="start",
          color=INK):
    lines = _wrap(s, maxchars)
    for i, ln in enumerate(lines):
        o.append(T(x, y + i * lh, ln, size, anchor=anchor, color=color))
    return y + lh * len(lines)


def _legend_col(o, pairs, x, y0, size=5.7, maxchars=60, gap=2.6):
    """Render one column of letter legends; returns the next free y."""
    lh = size + 1.5
    yy = y0
    for letter, text in pairs:
        lines = _wrap(text, maxchars)
        o.append(T(x, yy, "%s = %s" % (letter, lines[0]), size,
                   anchor="start", color=INK))
        for j, ln in enumerate(lines[1:], 1):
            o.append(T(x + 7, yy + j * lh, ln, size,
                       anchor="start", color=INK))
        yy += lh * len(lines) + gap
    return yy


def _dimh(x1, x2, y, label, size=6.4, color=GREY, lab_dy=-4):
    return "".join([
        _line(x1, y - 4, x1, y + 4, sw=0.7, color=color),
        _line(x2, y - 4, x2, y + 4, sw=0.7, color=color),
        _arrow(x1 + 1, y, x2 - 1, y, sw=0.8, color=color, head="a7"),
        _arrow(x2 - 1, y, x1 + 1, y, sw=0.8, color=color, head="a7"),
        T((x1 + x2) / 2.0, y + lab_dy, label, size, color=INK),
    ])


def _dimv(y1, y2, x, label, size=6.4, color=GREY, lab_dx=6, anchor="start"):
    return "".join([
        _line(x - 4, y1, x + 4, y1, sw=0.7, color=color),
        _line(x - 4, y2, x + 4, y2, sw=0.7, color=color),
        _arrow(x, y1 + 1, x, y2 - 1, sw=0.8, color=color, head="a7"),
        _arrow(x, y2 - 1, x, y1 + 1, sw=0.8, color=color, head="a7"),
        T(x + lab_dx, (y1 + y2) / 2.0 + 2.4, label, size,
          anchor=anchor, color=INK),
    ])


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a7")


def _arcpts(cx, cy, r, a0, a1, step=8):
    return [(cx + r * math.cos(math.radians(a)),
             cy - r * math.sin(math.radians(a)))
            for a in range(int(a0), int(a1) + 1, step)]


def _cube8(cx, cy, bold=False):
    """Isometric cube: thin wireframe or bold conducting framework."""
    sw = 3.0 if bold else 1.1
    L, Tp, R, F = (cx - 72, cy - 18), (cx, cy - 36), (cx + 72, cy - 18), (cx, cy)
    BL, BF, BR, B = (cx - 72, cy + 50), (cx, cy + 68), (cx + 72, cy + 50), (cx, cy + 32)
    o = []
    for a, b in ((L, Tp), (Tp, R), (R, F), (F, L),
                 (L, BL), (BL, BF), (BF, F), (F, BR), (BR, R)):
        o.append(_line(a[0], a[1], b[0], b[1], sw=sw, color=INK))
    for a, b in ((Tp, B), (B, BL), (B, BR)):
        o.append(_line(a[0], a[1], b[0], b[1], sw=1.0 if not bold else 2.4,
                       dash="4 3", color=INK))
    return "".join(o)


# ------------------------------------------------------------------ 8.1

@_reg
def fig_f801():
    """Figure 8.1 - MESG test vessel with flange-gap adjuster."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Bình thử khe hở an toàn lớn nhất",
           "MESG test vessel")
    _sub(o, "Chỉnh khe hở tấm bích · bầu chứa hỗn hợp tính toán / "
            "Adjustable flange gap · stoichiometric test mixture", 29)

    # gas chamber and sphere
    o.append(_rect(40, 52, 250, 156, fill=PAPER, sw=1.3))
    o.append(_circle(165, 130, 60, fill=PAPER, sw=1.5))
    # calibrated flange-gap adjuster
    o.append(_line(165, 70, 165, 44, sw=2.2))
    o.append(_rect(155, 40, 20, 14, fill=INK, sw=0.8))
    for k in range(4):
        o.append(_line(158 + k * 5, 41, 158 + k * 5, 53, sw=0.7, color=PAPER))
    # flange lugs and stem
    o.append(_rect(97, 126, 9, 8, fill=PAPER, sw=1.1))
    o.append(_rect(224, 126, 9, 8, fill=PAPER, sw=1.1))
    for x0 in (97, 224):
        o.append(_line(x0 + 4.5, 122, x0 + 4.5, 138, sw=0.9))
    o.append(_rect(160, 190, 10, 18, fill=PAPER, sw=1.2))
    # sphere contents
    for i, ln in enumerate(("Sphere containing", "stoichiometric mixture",
                            "of test gas and air", "spark ignition source")):
        o.append(T(165, 112 + i * 10, ln, 6.2, color=INK))
    o.append(_path("M 165 156 L 165 168 M 159 162 L 171 162 "
                   "M 161 158 L 169 166 M 169 158 L 161 166",
                   fill="none", sw=0.9, color=INK))

    # printed callouts, re-positioned to the right of the chamber
    o.append(T(340, 52, "Calibrated flange gap adjuster", 6.8, anchor="start"))
    o.append(_lead(336, 54, 176, 46))
    o.append(T(340, 96, "Flange width = 25 mm", 6.8, anchor="start"))
    o.append(T(340, 108, "Flange gap = adjustable", 6.8, anchor="start"))
    o.append(_lead(336, 106, 234, 130))
    o.append(T(340, 152, "Gas surrounding sphere is the most easily", 6.8,
               anchor="start"))
    o.append(T(340, 164, "ignitable mixture of the test gas and air", 6.8,
               anchor="start"))
    o.append(_lead(336, 166, 286, 190))
    o.append(T(340, 250, "For full details see IEC 79-1A (1975), Appendix D",
               7.0, color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Fig 8.1")),
                "Hình 8.1 · Phương pháp xác định khe hở an toàn lớn nhất thử "
                "nghiệm. (Để biết chi tiết xem IEC 79-1A (1975), Phụ lục D)",
                "Figure 8.1 · Method of determination of maximum experimental "
                "safe gap. (For full details see IEC 79-1A (1975), Appendix D)",
                "Bình thử hình hộp chứa khí bao quanh một quả cầu; đầu điều chỉnh "
                "khe hở tấm bích có ren ở đỉnh, hai tai bích ở hai bên, thân dẫn "
                "xuống đáy; bên trong quả cầu ghi hỗn hợp tính toán của khí thử và "
                "không khí cùng nguồn đánh lửa; chú thích chiều rộng bích 25 mm",
                "Box-shaped test vessel enclosing a sphere, with a calibrated "
                "threaded flange-gap adjuster at the top, two flange lugs at the "
                "sides and a stem to the base; the sphere contains the "
                "stoichiometric test-gas and air mixture with spark ignition "
                "source; callouts give a 25 mm flange width and adjustable gap")


# ------------------------------------------------------------------ 8.2

@_reg
def fig_f802():
    """Figure 8.2 - Insulating plastics enclosures, two panels."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Vỏ bọc bằng nhựa cách điện",
           "Insulating plastics enclosures")

    o.append(T(172, 34, "Không có khung dẫn điện / No conducting framework",
               6.8, color=INK, weight="600"))
    o.append(_cube8(172, 100, bold=False))
    o.append(T(512, 34, "Có khung dẫn điện tiếp địa hở / "
                        "Conducting exposed earthed framework",
               6.3, color=INK, weight="600"))
    o.append(_cube8(512, 100, bold=True))

    left = ("Maximum area of each of six external surfaces",
            "IIA and IIB = 100 cm²", "IIC = 20 cm²", "Maximum volume",
            "IIA and IIB = 1000 cm³", "IIC = 90 cm³")
    right = ("Maximum area of each of six external surfaces",
             "IIA and IIB = 400 cm²", "IIC = 100 cm²", "Maximum volume",
             "IIA and IIB = 8000 cm³", "IIC = 1000 cm³")
    for i in range(6):
        o.append(T(20, 185 + i * 12, left[i], 6.6, anchor="start", color=INK))
        o.append(T(360, 185 + i * 12, right[i], 6.6, anchor="start", color=INK))
    o.append(T(340, 266, "Diện tích cm² · thể tích cm³ / "
                         "Area cm² · volume cm³", 6.4, color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Fig 8.2")),
                "Hình 8.2 · Vỏ bọc bằng nhựa cách điện. Không có khung dẫn điện: "
                "diện tích mỗi bề mặt IIA và IIB 100 cm², IIC 20 cm²; thể tích "
                "IIA và IIB 1000 cm³, IIC 90 cm³. Có khung tiếp địa: 400 cm², "
                "100 cm²; 8000 cm³, 1000 cm³",
                "Figure 8.2 · Insulating plastics enclosures. No conducting "
                "framework: area of each surface IIA and IIB 100 cm², IIC 20 cm²; "
                "volume IIA and IIB 1000 cm³, IIC 90 cm³. With earthed framework: "
                "400 cm², 100 cm²; 8000 cm³, 1000 cm³",
                "Hai hình lập phương đường nét mỏng và đường nét dày; bên trái "
                "không có khung dẫn điện với diện tích 100 cm² và 20 cm², thể "
                "tích 1000 cm³ và 90 cm³; bên phải có khung dẫn điện tiếp địa hở "
                "với diện tích 400 cm² và 100 cm², thể tích 8000 cm³ và 1000 cm³",
                "Two isometric cubes, thin wireframe at left and bold conducting "
                "framework at right; the left panel lists 100 cm² and 20 cm² "
                "surface area with 1000 cm³ and 90 cm³ volume, the right panel "
                "lists 400 cm² and 100 cm² with 8000 cm³ and 1000 cm³")


# ------------------------------------------------------------------ 8.3

@_reg
def fig_f803():
    """Figure 8.3 - Typical shrouds for fasteners, with height table."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Mũ che điển hình cho bộ phận giữ chặt",
           "Typical shrouds for fasteners")

    # circular shroud with a 120 deg opening
    o.append(_poly(_arcpts(100, 88, 32, 60, 300, 6), fill="none", sw=3.0))
    o.append(_circle(100, 88, 8, fill=PAPER, sw=1.2))
    o.append(_circle(100, 88, 4.5, fill=PAPER, sw=0.8))
    o.append(_line(100, 88, 116, 60, sw=0.9, color=GREY))
    o.append(_line(100, 88, 116, 116, sw=0.9, color=GREY))
    o.append(_poly(_arcpts(100, 88, 22, -60, 60, 10), fill="none",
                   sw=0.9, color=GREY))
    o.append(T(128, 88, "120° max", 6.6, anchor="start"))
    o.append(_dimv(56, 72, 52, "A", lab_dx=-7, anchor="end"))

    # flat-bottomed shroud
    o.append(_path("M 210 112 L 210 88 A 30 30 0 0 1 270 88 L 270 112 Z",
                   fill="none", sw=3.0))
    o.append(_circle(240, 90, 8, fill=PAPER, sw=1.2))
    o.append(_poly(_arcpts(240, 90, 21, -60, 60, 10), fill="none",
                   sw=0.9, color=GREY))
    o.append(T(268, 90, "120° max", 6.6, anchor="start"))
    o.append(_dimv(58, 74, 192, "A", lab_dx=-7, anchor="end"))

    _para(o, 340, 136,
          "Shroud height at least equal to thickness of bolt head, "
          "screwhead or nut", 6.4, maxchars=48, lh=10, anchor="middle")

    o.append(T(180, 162, "Thread size", 6.6, weight="600"))
    o.append(T(420, 162, "A in mm (normal)", 6.6, weight="600"))
    o.append(_line(120, 166, 560, 166, sw=1.0))
    rows = (("M5", "9.0"), ("M6", "9.5"), ("M8", "12.0"), ("M10", "14.0"),
            ("M12", "17.0"), ("M14", "19.0"), ("M16", "21.0"),
            ("M20", "24.0"), ("M24", "30.0"))
    for i, (t, v) in enumerate(rows):
        y = 178 + i * 10.4
        o.append(T(180, y, t, 6.4))
        o.append(T(420, y, v, 6.4))
    o.append(_line(120, 265, 560, 265, sw=1.0))
    return _fig(svg(w, h, "".join(o), esc("Fig 8.3")),
                "Hình 8.3 · Mũ che điển hình cho bộ phận giữ chặt. Chiều cao A "
                "tối thiểu bằng chiều dày đầu bulông, đầu vít hoặc đai ốc; M5 9.0, "
                "M6 9.5, M8 12.0, M10 14.0, M12 17.0, M14 19.0, M16 21.0, M20 "
                "24.0, M24 30.0 mm",
                "Figure 8.3 · Typical shrouds for fasteners. Shroud height A at "
                "least equal to bolt head, screwhead or nut thickness; M5 9.0, "
                "M6 9.5, M8 12.0, M10 14.0, M12 17.0, M14 19.0, M16 21.0, M20 "
                "24.0, M24 30.0 mm",
                "Hai dạng mũ che: một vòng tròn có cửa mở 120°, một dạng đáy "
                "phẳng, đều có bulông ở giữa và kích thước chiều cao A; bảng "
                "chín giá trị chiều cao theo cỡ ren từ M5 đến M24",
                "Two shroud forms, a circular ring with a 120 degree opening and "
                "a flat-bottomed form, each with a central bolt and height "
                "dimension A; a nine-row table of heights for threads M5 to M24")


# ------------------------------------------------------------------ 8.4

@_reg
def fig_f804():
    """Figure 8.4 - Typical recesses for shrouding purposes."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Hốc lõm điển hình để che chắn",
           "Typical recesses for shrouding purposes")

    # section through a counterbored recess
    o.append(_poly([(80, 44), (170, 44), (170, 72), (196, 72),
                    (196, 120), (80, 120)], fill="url(#sect)", sw=1.1, close=True))
    o.append(_poly([(250, 44), (340, 44), (340, 120), (224, 120),
                    (224, 72), (250, 72)], fill="url(#sect)", sw=1.1, close=True))
    o.append(_rect(198, 76, 24, 44, fill=PAPER, sw=1.1))
    for i in range(5):
        o.append(_line(198, 82 + i * 7, 222, 82 + i * 7, sw=0.7, color=GREY))
    o.append(_rect(196, 60, 28, 14, fill=PAPER, sw=1.1))
    o.append(_dimh(170, 250, 36, "B"))
    o.append(_dimv(44, 72, 360, "C"))
    o.append(T(150, 132, "Thread", 6.4, anchor="end"))
    o.append(_lead(154, 130, 205, 100))
    o.append(T(280, 132, "Clearance hole", 6.4, anchor="start"))
    o.append(_lead(276, 130, 222, 102))

    o.append(T(140, 146, "Thread size", 6.4, weight="600"))
    o.append(T(280, 146, "Clearance hole size (mm)", 6.4, weight="600"))
    o.append(T(460, 146, "B (mm)", 6.4, weight="600"))
    o.append(_line(110, 150, 560, 150, sw=1.0))
    rows = (("M5", "5.5", "18"), ("M6", "6.6", "19"), ("M8", "9.0", "24"),
            ("M10", "11.0", "28"), ("M12", "14.0", "34"),
            ("M14", "16.0", "38"), ("M16", "18.0", "42"),
            ("M20", "22.0", "48"), ("M24", "26.0", "60"))
    for i, (t, c, b) in enumerate(rows):
        y = 162 + i * 9.6
        o.append(T(140, y, t, 6.2))
        o.append(T(280, y, c, 6.2))
        o.append(T(460, y, b, 6.2))
    o.append(_line(110, 244, 560, 244, sw=1.0))
    o.append(T(340, 258, "C = at least height of bolthead, screwhead or nut",
               6.6))
    return _fig(svg(w, h, "".join(o), esc("Fig 8.4")),
                "Hình 8.4 · Hốc lõm điển hình để che chắn. Bảng kích thước ren "
                "M5 đến M24 với đường kính lỗ lọt 5.5 đến 26.0 mm và B từ 18 đến "
                "60 mm; C tối thiểu bằng chiều cao đầu bulông",
                "Figure 8.4 · Typical recesses for shrouding purposes. Table of "
                "threads M5 to M24 with clearance holes 5.5 to 26.0 mm and B from "
                "18 to 60 mm; C at least the height of a bolt head",
                "Mặt cắt có hốc lõm ở thân trên với chiều rộng B và chiều sâu C, "
                "bulông đi qua lỗ lọt; bảng chín dòng giá trị ren, lỗ lọt và B "
                "cùng ghi chú chiều cao C",
                "Section with a counterbored recess of width B and depth C, a "
                "bolt passing through a clearance hole; a nine-row table of "
                "thread size, clearance hole and B, with the note on height C")


# ------------------------------------------------------------------ 8.5

@_reg
def fig_f805():
    """Figure 8.5 - Typical compression gland for armoured cable, A-L."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Đầu nối ép điển hình cho cáp bọc thép",
           "Typical compression gland for armoured cable", size=8.2)

    # longitudinal section of the gland
    o.append(_rect(50, 82, 420, 16, fill=PAPER, sw=1.2))          # inner sheath
    o.append(_rect(50, 74, 250, 32, fill="none", sw=1.8))         # outer sheath
    o.append(_rect(300, 74, 120, 6, fill="url(#sect)", sw=0.8))   # armour
    o.append(_rect(300, 100, 120, 6, fill="url(#sect)", sw=0.8))
    o.append(_rect(270, 54, 170, 20, fill="url(#sect)", sw=1.3))  # body top
    o.append(_rect(270, 106, 170, 20, fill="url(#sect)", sw=1.3)) # body bottom
    o.append(_path("M 270 54 l 6 -5 l 6 5 l 6 -5 l 6 5 l 6 -5 l 6 5",
                   fill="none", sw=0.9))
    o.append(_rect(262, 50, 8, 80, fill=INK, sw=0))               # washer A
    o.append(_rect(302, 80, 10, 20, fill=INK, sw=0))              # ring B
    o.append(_poly([(385, 74), (415, 54), (427, 54), (405, 82)],
                   fill="url(#sect)", sw=1.1, close=True))        # element E
    o.append(_poly([(385, 106), (415, 126), (427, 126), (405, 98)],
                   fill="url(#sect)", sw=1.1, close=True))
    o.append(_rect(425, 74, 15, 32, fill="url(#sect)", sw=1.1))   # clamp G
    o.append(_rect(465, 76, 8, 28, fill=INK, sw=0))               # weather ring H
    o.append(_rect(473, 58, 57, 64, fill="url(#sect)", sw=1.3))   # element J
    for k in range(4):
        o.append(_line(478 + k * 14, 58, 478 + k * 14, 122,
                       sw=0.7, color=PAPER))

    letters = (("A", 266, 46, 266, 50), ("B", 307, 138, 307, 100),
               ("C", 240, 46, 262, 54), ("D", 330, 46, 330, 54),
               ("E", 400, 46, 400, 54), ("F", 360, 68, 360, 75),
               ("G", 432, 138, 432, 106), ("H", 469, 46, 469, 76),
               ("J", 500, 46, 500, 58), ("K", 200, 76, 200, 82),
               ("L", 180, 112, 180, 106))
    for letter, tx, ty, lx, ly in letters:
        o.append(T(tx, ty, letter, 7.0, color=INK))
        o.append(_lead(tx, ty + 2, lx, ly))

    left = (("A", "Sealing washer between enclosure and gland"),
            ("B", "Sealing ring on cable inner sheath of armoured cable "
                  "is also weatherseal for non armoured cable where items "
                  "F, G, H, and L are not present"),
            ("C", "Thread for fixing gland to enclosure"),
            ("D", "Gland body (entry element)"),
            ("E", "Cable seal compression element"))
    right = (("F", "Cable armour"), ("G", "Armour clamping"),
             ("H", "Weather sealing ring"),
             ("J", "Weather seal compression element"),
             ("K", "Cable inner sheath or outer sheath for "
                   "non-armoured cables"),
             ("L", "Outer sheath of armoured cables"))
    _legend_col(o, left, 20, 150, size=5.7, maxchars=60)
    _legend_col(o, right, 350, 150, size=5.7, maxchars=60)
    return _fig(svg(w, h, "".join(o), esc("Fig 8.5")),
                "Hình 8.5 · Đầu nối ép điển hình cho cáp bọc thép, ký hiệu A đến "
                "L gồm vòng đệm, vòng làm kín, thân đầu nối, phần ép làm kín, "
                "lớp bọc thép, kẹp giữ, vòng chắn thời tiết và lớp vỏ",
                "Figure 8.5 · Typical compression gland for armoured cable, "
                "letters A to L covering washer, sealing ring, gland body, "
                "compression element, armour, armour clamp, weather seal and "
                "cable sheaths",
                "Mặt cắt ngang đầu nối cáp có các ký hiệu A đến L chỉ vòng đệm "
                "giữa vỏ bọc và đầu nối, vòng làm kín trên vỏ trong, ren bắt, "
                "thân đầu nối, phần ép, lớp giáp, kẹp giáp, vòng chắn thời tiết "
                "và các lớp vỏ cáp; chú thích đầy đủ bên dưới",
                "Longitudinal section of a cable gland with letters A to L "
                "marking the enclosure washer, inner-sheath sealing ring, "
                "fixing thread, gland body, compression element, armour, "
                "armour clamp, weather ring and cable sheaths, with full legends")


# ------------------------------------------------------------------ 8.6

@_reg
def fig_f806():
    """Figure 8.6 - Detail of compound sealed gland, A-G."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 6, "Chi tiết đầu nối kín bằng hợp chất",
           "Detail of compound sealed gland")

    # section of the compound gland bolted to the enclosure wall
    o.append(_rect(400, 40, 46, 100, fill="url(#sect)", sw=1.4))   # enclosure
    o.append(_rect(180, 62, 220, 56, fill="url(#sect)", sw=1.4))   # gland body
    o.append(_rect(210, 68, 110, 44, fill="url(#comp)", sw=1.0))   # compound
    o.append(_rect(90, 74, 120, 30, fill=PAPER, sw=1.4))           # sheath
    for yy in (78, 88, 98):
        o.append(_line(90, yy, 210, yy, sw=1.4))                   # cores
    o.append(_rect(200, 56, 14, 68, fill=INK, sw=0))               # retainer
    o.append(_rect(250, 48, 16, 14, fill=PAPER, sw=1.1))           # fixing holes
    o.append(_rect(310, 48, 16, 14, fill=PAPER, sw=1.1))
    o.append(_rect(392, 58, 8, 64, fill=INK, sw=0))                # washer
    letters = (("A", 388, 50, 396, 58), ("B", 265, 72, 265, 90),
               ("C", 258, 38, 258, 48), ("D", 350, 50, 350, 62),
               ("E", 190, 48, 205, 58), ("F", 130, 66, 130, 78),
               ("G", 130, 114, 130, 104))
    for letter, tx, ty, lx, ly in letters:
        o.append(T(tx, ty, letter, 7.0, color=INK))
        o.append(_lead(tx, ty + 2, lx, ly))

    left = (("A", "Sealing washer between enclosure and gland"),
            ("B", "Filling compound"), ("C", "Gland fixing holes"),
            ("D", "Gland body"))
    right = (("E", "Compound retaining element"),
             ("F", "Insulated cable cores"),
             ("G", "Cable inner or outer sheath"))
    _legend_col(o, left, 20, 150, size=6.0, maxchars=58)
    _legend_col(o, right, 350, 150, size=6.0, maxchars=58)
    _para(o, 340, 232, "Armoured cables will additionally have an armour "
                       "clamp and outer weather seal", 6.4, maxchars=62,
          lh=11, anchor="middle")
    return _fig(svg(w, h, "".join(o), esc("Fig 8.6")),
                "Hình 8.6 · Chi tiết đầu nối kín bằng hợp chất, ký hiệu A đến G "
                "gồm vòng đệm, hợp chất độn, lỗ bắt, thân đầu nối, phần giữ hợp "
                "chất, lõi cáp cách điện và vỏ cáp; cáp bọc thép cần thêm kẹp "
                "giáp và vòng chắn thời tiết",
                "Figure 8.6 · Detail of compound sealed gland, letters A to G "
                "covering washer, filling compound, fixing holes, gland body, "
                "compound retainer, insulated cores and cable sheath; armoured "
                "cables also need an armour clamp and weather seal",
                "Mặt cắt đầu nối gắn vào thành vỏ bọc bên phải, có buồng chứa "
                "hợp chất và ba lõi dẫn đi vào từ bên trái; các ký hiệu A đến G "
                "và ghi chú cáp bọc thép cần kẹp giáp cùng vòng chắn thời tiết",
                "Section of a gland bolted into the enclosure wall at right, "
                "with a compound chamber and three cable cores entering from "
                "the left; letters A to G and a note that armoured cables add "
                "an armour clamp and weather seal")


# ------------------------------------------------------------------ 8.7

@_reg
def fig_f807():
    """Figure 8.7 - Entry protection for flexible (non-armoured) cables."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 7, "Bảo vệ cổng vào cho cáp mềm không bọc thép",
           "Entry protection for flexible cables", size=8.2)

    # gland section
    o.append(_rect(40, 76, 140, 30, fill=PAPER, sw=1.8))          # outer sheath
    o.append(_rect(160, 58, 120, 66, fill="url(#sect)", sw=1.4))  # gland body
    o.append(_poly([(180, 76), (200, 70), (200, 112), (180, 106)],
                   fill=INK, sw=0.8, close=True))                 # sealing ring
    o.append(_poly([(205, 70), (235, 58), (235, 114), (205, 112)],
                   fill="url(#sect)", sw=1.2, close=True))        # compression
    for yy in (86, 96):
        o.append(_line(40, yy, 280, yy, sw=1.2))
    o.append(_poly(_arcpts(200, 70, 12, 200, 340, 20), fill="none",
                   sw=0.8, color=GREY))
    o.append(T(196, 54, "r", 7.0))
    letters = (("A", 220, 48, 220, 58), ("B", 190, 132, 190, 106),
               ("C", 250, 48, 250, 58), ("D", 100, 68, 100, 76))
    for letter, tx, ty, lx, ly in letters:
        o.append(T(tx, ty, letter, 7.0))
        o.append(_lead(tx, ty + 2, lx, ly))

    # enlarged detail of the rear inner corner
    o.append(_circle(500, 105, 56, fill=PAPER, sw=1.4))
    o.append(_line(452, 70, 510, 70, sw=2.0))
    o.append(_line(510, 70, 510, 140, sw=2.0))
    o.append(_path("M 488 70 Q 510 70 510 96", fill="none", sw=1.6))
    o.append(_path("M 488 96 A 22 22 0 0 1 510 74",
                   fill="none", sw=0.9, color=GREY))
    o.append(T(520, 90, "75°", 7.0))
    o.append(T(500, 172, "Detail of rear inner corner of compression element",
               6.4, anchor="middle"))

    o.append(T(340, 196, "A = Gland body    B = Sealing ring    "
                         "C = Cable seal compression element    "
                         "D = Cable outer sheath", 6.2))
    o.append(T(340, 212, "r = 0.25 × maximum cable diameter or 3 mm "
                         "whichever is smaller", 6.6))
    o.append(T(340, 234, "Hình 8.7 · Cổng vào cáp mềm / "
                         "Figure 8.7 · Flexible cable entry", 6.4, color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Fig 8.7")),
                "Hình 8.7 · Bảo vệ cổng vào cho cáp mềm không bọc thép, ký hiệu "
                "A đến D và góc 75° ở góc trong của phần ép; r bằng 0,25 lần "
                "đường kính cáp lớn nhất hoặc 3 mm, lấy giá trị nhỏ hơn",
                "Figure 8.7 · Entry protection for flexible (non-armoured) "
                "cables, letters A to D and the 75 degree rear inner corner of "
                "the compression element; r = 0.25 x maximum cable diameter or "
                "3 mm whichever is smaller",
                "Mặt cắt đầu nối cáp mềm có ký hiệu A đến D, vòng làm kín và "
                "phần ép hình nêm; hình tròn phóng to bên phải góc trong 75° "
                "của phần ép cùng kích thước r",
                "Section of a flexible cable gland with letters A to D, a "
                "sealing ring and wedge compression element; an enlarged circle "
                "at right shows the 75 degree inner corner and the dimension r")


# ------------------------------------------------------------------ 8.8

@_reg
def fig_f808():
    """Figure 8.8 - Example of apparatus marking, A-J."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 8, "Ví dụ đánh dấu thiết bị",
           "Example of apparatus marking")

    o.append(_rect(110, 36, 460, 82, fill=PAPER, sw=1.4))
    o.append(_rect(126, 46, 44, 26, fill=INK, sw=0))
    o.append(T(400, 50, "SWITCH UNIT", 7.4, anchor="start"))
    o.append(T(400, 62, "TYPE TB 51", 7.4, anchor="start"))
    o.append(T(400, 74, "SERIAL NO 12345", 7.4, anchor="start"))
    o.append(T(340, 92, "EExde II T4 (Ta = −10 to +50°C)", 8.0,
               weight="600"))
    o.append(T(340, 110, "LCHE 95 4720 X", 8.0))
    for letter, tx, ty, lx, ly in (
            ("A", 148, 30, 148, 46), ("B", 470, 30, 490, 50),
            ("C", 560, 74, 492, 74), ("D", 120, 92, 270, 92),
            ("E", 200, 130, 290, 116), ("F", 260, 130, 320, 116),
            ("G", 320, 130, 350, 116), ("H", 380, 130, 380, 116),
            ("J", 440, 130, 410, 116)):
        o.append(T(tx, ty, letter, 6.8))
        o.append(_lead(tx, ty + 2, lx, ly))

    left = (("A", "Manufacturers logo for identification"),
            ("B", "Apparatus description and type no."),
            ("C", "Apparatus serial or batch no."),
            ("D", "Certification Code: note dual protection (EExd) switch "
                  "with EEx e connection facilities. Ta: ambient temperature "
                  "range. Marked only because it is not the normal one used "
                  "by the Standard."),
            ("E", "Identification of the certification body (test house)"))
    right = (("F", "Year of issue of certificate"),
             ("G", "Identification of Principal Protection Concept"),
             ("H", "Number of certificate within that year"),
             ("J", "X indicating special conditions for safe use; "
                   "certificate must be consulted for these"))
    _legend_col(o, left, 20, 146, size=5.6, maxchars=60)
    _legend_col(o, right, 350, 146, size=5.6, maxchars=60)
    return _fig(svg(w, h, "".join(o), esc("Fig 8.8")),
                "Hình 8.8 · Ví dụ đánh dấu thiết bị với nhãn EExde II T4 "
                "(Ta = −10 đến +50°C), ký hiệu A đến J chỉ logo, mô tả, số "
                "seri, mã chứng nhận, tổ chức thử nghiệm, năm, khái niệm bảo "
                "vệ chính, số chứng nhận và điều kiện đặc biệt X",
                "Figure 8.8 · Example of apparatus marking with EExde II T4 "
                "(Ta = −10 to +50°C), letters A to J for logo, description, "
                "serial number, certification code, test house, year, principal "
                "protection concept, certificate number and special condition X",
                "Nhãn thiết bị hình chữ nhật có ô logo đen, dòng SWITCH UNIT "
                "TYPE TB 51 SERIAL NO 12345, mã EExde II T4 với nhiệt độ môi "
                "trường và số chứng nhận LCHE 95 4720 X; chú thích A đến J",
                "Rectangular apparatus label with a black logo block, SWITCH "
                "UNIT TYPE TB 51 SERIAL NO 12345, the code EExde II T4 with "
                "ambient range and certificate number LCHE 95 4720 X, plus "
                "letter legend A to J")


# ------------------------------------------------------------------ 8.9

@_reg
def fig_f809():
    """Figure 8.9 - Example of component labelling, A-H."""
    w, h = 680, 300
    o = [_defs8(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 9, "Ví dụ ghi nhãn linh kiện",
           "Example of component labelling")

    o.append(_rect(110, 36, 460, 84, fill=PAPER, sw=1.4))
    o.append(T(340, 52, "G. WITHERSPOON plc", 8.6, weight="600"))
    o.append(T(340, 68, "RELAY TYPE E RLLI", 8.0))
    o.append(T(340, 88, "EEx II B", 8.0))
    o.append(_circle(150, 104, 12, fill=PAPER, sw=1.4))
    o.append(T(150, 108, "Ex", 7.0))
    o.append(T(230, 108, "96 1026 U", 8.0, anchor="start"))
    for letter, tx, ty, lx, ly in (
            ("A", 250, 30, 290, 44), ("B", 430, 68, 392, 68),
            ("C", 240, 88, 290, 88), ("D", 110, 104, 138, 104),
            ("E", 210, 132, 235, 116), ("F", 250, 132, 260, 116),
            ("G", 290, 132, 285, 116), ("H", 330, 132, 310, 116)):
        o.append(T(tx, ty, letter, 6.8))
        o.append(_lead(tx, ty + 2, lx, ly))

    left = (("A", "Manufacturers name"),
            ("B", "Manufacturers type no. (note serial no. not necessary)"),
            ("C", "Certification Code (note no temperature classification)"),
            ("D", "Certification body identification logo"))
    right = (("E", "Year of certificate issue"),
             ("F", "Identification of Principal Protection Concept"),
             ("G", "Number of certificate in year"),
             ("H", "U indicates a component"))
    _legend_col(o, left, 20, 146, size=6.0, maxchars=58)
    _legend_col(o, right, 350, 146, size=6.0, maxchars=58)
    return _fig(svg(w, h, "".join(o), esc("Fig 8.9")),
                "Hình 8.9 · Ví dụ ghi nhãn linh kiện có chữ U, với G. "
                "WITHERSPOON plc, RELAY TYPE E RLLI, EEx II B và số 96 1026 "
                "U; ký hiệu A đến H chỉ tên nhà sản xuất, loại, mã chứng nhận, "
                "logo, năm, khái niệm bảo vệ chính, số chứng nhận và U",
                "Figure 8.9 · Example of component labelling with U, showing "
                "G. WITHERSPOON plc, RELAY TYPE E RLLI, EEx II B and 96 1026 "
                "U; letters A to H for manufacturer, type, certification code, "
                "logo, year, protection concept, certificate number and U",
                "Nhãn linh kiện có tên G. WITHERSPOON plc, dòng RELAY TYPE E "
                "RLLI, mã EEx II B, biểu tượng Ex trong vòng tròn và số "
                "96 1026 U; chú thích A đến H, trong đó H là chữ U chỉ linh kiện",
                "Component label with G. WITHERSPOON plc, RELAY TYPE E RLLI, "
                "the code EEx II B, a circled Ex logo and the number 96 1026 "
                "U; letter legend A to H with H explaining U as a component")
