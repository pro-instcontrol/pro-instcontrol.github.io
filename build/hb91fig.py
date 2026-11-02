# -*- coding: utf-8 -*-
"""Figures 91.1–91.2 for Handbook Chapter 91 — Cathode Ray Tube Displays.

91.1 a typical CRT with electromagnetic focus and electromagnetic deflection
91.2 spectral profiles of two representative phosphors

Chapter 91 has only two figures, so both live here and there is no separate
base module: everything is imported straight from `hb93base.py`, which is the
oldest of the shared primitive modules and therefore the one all later
chapters chain from.

91.1 is traced from the printed cut-away: the tube is drawn in section, neck at
the left, faceplate at the right, with the four stages of image formation
(beam generation, focusing, deflection, energy conversion) each sitting in its
own labelled region of the tube.

91.2 is not computed from a formula — a phosphor emission spectrum is measured
data, so the two curves are rebuilt from the printed graph by digitising it.
The blue band peaks at 452 nm and the red line at 612 nm, as the source caption
states; every other point is read off the printed curve. The two monotone
flanks of the 612 nm line were enforced after digitising because a 4 px pen on
a near-vertical stroke makes the column-wise trace jitter by a couple of
percent.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _r().
"""
import math

from hbfig import svg, _fig, _f
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, Frame)

COIL = "#e9e9e9"          # coil bodies: light fill, dark outline
GLASSIN = "#fbfbfb"       # tube interior
PHOS = "#d8d8d8"          # phosphor coating


# ---------------------------------------------------------------- helpers
def _bez(p0, p1, p2, p3, n=28):
    """Sample a cubic Bezier into a point list, endpoints included."""
    out = []
    for i in range(n + 1):
        t = i / float(n)
        u = 1.0 - t
        x = (u * u * u * p0[0] + 3 * u * u * t * p1[0]
             + 3 * u * t * t * p2[0] + t * t * t * p3[0])
        y = (u * u * u * p0[1] + 3 * u * u * t * p1[1]
             + 3 * u * t * t * p2[1] + t * t * t * p3[1])
        out.append((x, y))
    return out


def _wall_at(pts, x):
    """y of a sampled wall at a given x (linear interpolation)."""
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        if (a[0] - x) * (b[0] - x) <= 0 and abs(b[0] - a[0]) > 1e-9:
            t = (x - a[0]) / (b[0] - a[0])
            return a[1] + t * (b[1] - a[1])
    return pts[-1][1]


def _brace(x0, x1, y, depth=6.0, sw=1.0):
    """A wide horizontal curly brace pointing down."""
    xm = (x0 + x1) / 2.0
    return _path([(x0, y - depth), (x0, y), (xm - 3, y), (xm, y + depth),
                  (xm + 3, y), (x1, y), (x1, y - depth)], sw, E)


def _off(pts, d):
    """Offset a polyline along its outward normal by d (sign carries direction)."""
    out = []
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        if i == 0:
            a, b = pts[0], pts[1]
        elif i == n - 1:
            a, b = pts[n - 2], pts[n - 1]
        else:
            a, b = pts[i - 1], pts[i + 1]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1.0
        out.append((x + dy / L * d, y - dx / L * d))
    return out


# ================================================================ 91.1
def fig_91_1():
    tag = "911"
    o = [_defs(tag)]

    AX = 240.0                    # tube axis
    NX0, NX1 = 56.0, 250.0        # neck
    NH = 26.0                     # neck half-height
    FX = 548.0                    # faceplate x at the corners
    FT, FB = 92.0, 388.0          # faceplate top / bottom

    # ---- wall curves -----------------------------------------------------
    # The funnel is steep just aft of the neck and shallows as it approaches
    # the faceplate corner, which is the widest point of the tube.
    t1 = _bez((NX1, AX - NH), (312, AX - NH), (352, 188), (394, 146))
    t2 = _bez((394, 146), (444, 100), (500, 88), (FX, FT))
    b1 = _bez((NX1, AX + NH), (312, AX + NH), (352, 292), (394, 334))
    b2 = _bez((394, 334), (444, 380), (500, 392), (FX, FB))
    face = _bez((FX, FT), (592, 128), (592, 352), (FX, FB))

    wall_t = [(NX1, AX - NH)] + t1 + t2[1:] + [(FX, FT)]
    wall_b = [(NX1, AX + NH)] + b1 + b2[1:] + [(FX, FB)]

    # ---- tube outline ----------------------------------------------------
    o.append(_path(wall_t + face[1:] + wall_b[::-1][1:] + [(NX0, AX + NH),
                                                           (NX0, AX - NH)],
                   1.5, E, fill=GLASSIN, close=True))

    # ---- phosphor coating on the inner face ------------------------------
    phos = _bez((FX, FT + 10), (583, 136), (583, 344), (FX, FB - 10))
    o.append(_path(phos, 2.0, "#9e9e9e"))
    o.append(_line(FX, FT, FX, FT + 10, 1.0, E))
    o.append(_line(FX, FB - 10, FX, FB, 1.0, E))

    # ---- beam: a thin wedge converging on the spot -----------------------
    o.append(_line(124, AX - 7, FX - 4, AX - 1.5, 1.0, "#8a8a8a"))
    o.append(_line(124, AX + 7, FX - 4, AX + 1.5, 1.0, "#8a8a8a"))
    o.append(_dot(FX + 2, AX, 2.8, E))
    o.append(_circ(FX + 2, AX, 5.2, E, "none", 0.9))

    # ---- electron gun internals -----------------------------------------
    # heater: a wound filament in a small can
    o.append(_rect(66, AX - 13, 32, 26, 1.0, "#fff", "", E))
    zz = []
    for i in range(15):
        zz.append((70 + i * 1.85, AX - 5 if i % 2 == 0 else AX + 5))
    o.append(_path(zz, 1.1, E))
    # cathode: a cup opening toward the beam
    o.append(_path([(120, AX - 16), (104, AX - 16), (104, AX + 16),
                    (120, AX + 16)], 1.4, E))
    o.append(_line(112, AX - 16, 112, AX + 16, 0.8, "#a8a8a8"))
    o.append(_line(120, AX - 16, 120, AX + 16, 1.6, E))
    # G1 and G2: apertured plates
    for gx in (138, 160):
        o.append(_line(gx, AX - 24, gx, AX - 5, 1.7, E))
        o.append(_line(gx, AX + 5, gx, AX + 24, 1.7, E))

    # ---- focusing lenses -------------------------------------------------
    for (y0, y1) in ((AX - NH - 24, AX - NH), (AX + NH, AX + NH + 24)):
        o.append(_rect(186, y0, 46, 24, 1.1, COIL, "", E))
        o.append(_line(198, y0 + 3, 198, y1 - 3, 0.7, "#b4b4b4"))
        o.append(_line(220, y0 + 3, 220, y1 - 3, 0.7, "#b4b4b4"))

    # ---- deflection coils: bands wrapped on the cone ---------------------
    for (wall, sgn) in ((wall_t, 1.0), (wall_b, -1.0)):
        seg = [p for p in wall if 264 <= p[0] <= 350]
        if not seg:
            continue
        inner = _off(seg, sgn * 1.0)
        outer = _off(seg, sgn * 25.0)
        o.append(_poly(inner + outer[::-1], 1.1, COIL, E))
        for i in range(1, 5):
            k = min(int(len(seg) * i / 5.0), len(seg) - 1)
            a, b = inner[k], outer[k]
            o.append(_line(a[0], a[1], b[0], b[1], 0.7, "#b4b4b4"))

    # ---- anode stud ------------------------------------------------------
    ay = _wall_at(wall_t, 426)
    o.append(_line(426, ay, 426, ay - 8, 2.6, E))
    o.append(_dot(426, ay - 10, 3.2, E))

    # ---- labels ----------------------------------------------------------
    o.append(_lbl(48, 152, "Cuộn gia nhiệt", "tm"))
    o.append(_line(80, 156, 80, AX - 15, 0.8, S))
    o.append(_lbl(100, 118, "Catôt", "tm"))
    o.append(_line(116, 122, 112, AX - 18, 0.8, S))
    o.append(_lbl(150, 84, "Thấu kính hội tụ", "tm"))
    o.append(_lbl(150, 96, "điện từ", "tm"))
    o.append(_line(198, 100, 208, AX - NH - 25, 0.8, S))
    o.append(_lbl(386, 50, "Anôt", "tm"))
    o.append(_line(408, 54, 424, ay - 14, 0.8, S))
    o.append(_lbl(398, 176, "Lớp phủ", "tm"))
    o.append(_lbl(398, 188, "huỳnh quang", "tm"))
    o.append(_line(452, 192, 570, 212, 0.8, S))
    o.append(_lbl(614, 100, "Màn hình", "tm"))
    o.append(_line(612, 104, 598, 140, 0.8, S))
    o.append(_lbl(614, AX + 4, "Điểm sáng", "tm"))
    o.append(_line(612, AX + 2, 586, AX + 1, 0.8, S))
    o.append(_lbl(138, 292, "G1", "ts", "middle"))
    o.append(_line(138, 288, 138, AX + 25, 0.8, S))
    o.append(_lbl(160, 292, "G2", "ts", "middle"))
    o.append(_line(160, 288, 160, AX + 25, 0.8, S))
    o.append(_brace(60, 172, 316, 7.0, 0.9))
    o.append(_lbl(116, 342, "Súng điện tử", "tm", "middle"))
    o.append(_lbl(296, 352, "Cuộn lệch ngang", "tm"))
    o.append(_lbl(296, 364, "và dọc", "tm"))
    o.append(_line(330, 348, 330, 312, 0.8, S))

    return _fig(
        svg(700, 412, "".join(o),
            "Sơ đồ cắt dọc một ống phóng tia điện tử điển hình"),
        "Hình 91.1 · Ví dụ một ống phóng tia điện tử (CRT) điển hình, hội tụ điện từ và lệch "
        "điện từ. Kiểu ống này thường dùng cho các ứng dụng khắt khe như chiếu ảnh độ sáng cao, "
        "độ phân giải cao. Ống loại này có sẵn từ nhiều nhà sản xuất như Sony, Matsushita và "
        "Thomson.",
        "Figure 91.1 · Example of a typical CRT with electromagnetic focus and electromagnetic "
        "deflection. This type of tube design is usually used for demanding applications such as "
        "bright, high-resolution image projection. Tubes like this are available from a number of "
        "manufacturers such as Sony, Matsushita and Thomson.",
        "Mặt cắt dọc ống CRT: cổ ống bên trái chứa súng điện tử với cuộn gia nhiệt, catôt và "
        "hai lưới G1, G2; thấu kính hội tụ điện từ và cuộn lệch ngang dọc bọc quanh cổ; vỏ ống "
        "loe ra thành bầu; mặt trước phủ lớp huỳnh quang, nơi chùm tia hội tụ thành điểm sáng",
        "Longitudinal section of a CRT: the neck at the left holds the electron gun with heater "
        "coils, cathode and grids G1 and G2; electromagnetic focusing lenses and the horizontal "
        "and vertical deflection coils surround the neck; the envelope flares into the bulb; the "
        "faceplate carries the phosphor coating where the beam converges to a spot")


# ================================================================ 91.2
# Digitised from the printed graph: (wavelength nm, normalised output %).
_BLUE = [
    (380, 0.0), (389.4, 0.7), (396.3, 2.4), (402.1, 6.4), (407, 12.3), (411.5, 20.1),
    (415.4, 28.8), (430.5, 70.0), (433.5, 77.8), (436.9, 85.1), (440, 90.3),
    (444.5, 96.2), (447.9, 99.0), (451.2, 100.0), (454, 99.8), (457, 98.3),
    (460.6, 95.0), (464.5, 90.1), (468.6, 83.4), (478.5, 63.7), (489.9, 43.2),
    (499.6, 28.4), (506.5, 21.1), (515.8, 13.6), (526.7, 7.6), (535.1, 5.0),
    (544.2, 3.1), (555.8, 1.8),
]
_RED = [
    (556, 1.8), (562.5, 1.0), (571.7, 0.8), (574.3, 1.2), (577.3, 3.2), (587, 11.4),
    (591.3, 14.1), (593.3, 14.7), (595.6, 14.5), (599.9, 12.0), (601.2, 13.0),
    (603, 15.4), (604, 20.6), (605.3, 42.2), (606.2, 57.4), (607, 69.7),
    (608.3, 83.6), (608.6, 85.3), (609.4, 85.9), (610.3, 97.6), (612, 99.3),
    (613.1, 94.1), (614.6, 83.1), (615, 82.6), (616.5, 61.2), (616.7, 50.5),
    (617.2, 47.8), (618.2, 36.2), (619.3, 27.5), (621.5, 17.4), (623.8, 14.5),
    (624.7, 14.3), (625.3, 14.8), (628.1, 18.3), (629.9, 17.9), (632.5, 15.0),
    (636.8, 6.8), (638.7, 4.8), (641.5, 3.3), (643.4, 3.2), (648.6, 4.7),
    (651.8, 4.8), (656.8, 3.3), (663.2, 2.9), (670.1, 1.4), (675.9, 0.9),
    (680.5, 1.1), (681.1, 1.3), (688.6, 3.1), (691.7, 2.9), (696.2, 1.7),
    (699.2, 2.0), (701.4, 3.4), (707.4, 10.6), (708.9, 11.1), (711.7, 9.1),
    (716.9, 3.1), (720.3, 1.1), (738.8, 0.6), (740, 0.0),
]


def fig_91_2():
    tag = "912"
    o = [_defs(tag)]
    F = Frame(78, 44, 528, 230, (380, 740), (0, 100))

    o.append(F.hgrid([10, 20, 30, 40, 50, 60, 70, 80, 90]))
    o.append(F.frame(1.2))

    xt = [(v, str(v)) for v in range(380, 741, 20)]
    yt = [(v, "%d%%" % v) for v in range(0, 101, 10)]
    o.append(F.xticks(xt, 4, 14))
    o.append(F.yticks(yt, 4, 6))

    o.append(F.xlab("Bước sóng (nm)", 32))
    o.append(F.ylab("Đầu ra huỳnh quang chuẩn hoá", -46))

    o.append(F.curve(_BLUE, 1.9, "#3a3a3a"))
    o.append(F.curve(_RED, 1.9, "#3a3a3a"))

    # peak markers
    for (lam, pct, tx, anchor) in ((452, 100.0, 452, "middle"), (612, 100.0, 612, "middle")):
        o.append(_line(F.X(lam), F.Y(pct) - 2, F.X(lam), F.Y(pct) - 16, 0.8, S, "3 3"))
        o.append(_lbl(F.X(lam) + (0 if anchor == "middle" else 0),
                      F.Y(pct) - 22, "λ = %d nm" % lam, "ts", anchor))
    o.append(_dot(F.X(452), F.Y(100), 2.6, E))
    o.append(_dot(F.X(612), F.Y(99.3), 2.6, E))

    return _fig(
        svg(640, 340, "".join(o),
            "Phổ phát xạ của hai loại huỳnh quang tiêu biểu"),
        "Hình 91.2 · Huỳnh quang có thể có phổ đặc trưng rất khác nhau. Đồ thị minh hoạ phổ của "
        "hai trường hợp tiêu biểu. Nguồn xanh là ví dụ về loại huỳnh quang có phổ rộng và trơn; "
        "đầu ra cực đại của nó nằm trong vùng xanh, ở bước sóng 452 nm. Loại huỳnh quang đỏ cho "
        "phổ nhọn hơn với vài đỉnh hẹp; đỉnh lớn nhất ở bước sóng 612 nm.",
        "Figure 91.2 · Phosphors can have a wide range of spectral characteristics. This graph "
        "illustrates the spectral profiles of two representative cases. The blue source is an "
        "example of a phosphor with a wide and smooth profile; its maximum output is in the blue "
        "at a wavelength of 452 nm. The red phosphor shows a sharper profile with several narrow "
        "peaks; its largest peak is at 612 nm.",
        "Đồ thị phổ phát xạ: một dải xanh rộng, trơn, đỉnh 100% tại 452 nm; và một phổ đỏ nhọn "
        "gồm đỉnh hẹp rất cao tại 612 nm cùng các đỉnh phụ ở 590, 600, 628, 648, 680 và 708 nm",
        "Emission spectra: a broad, smooth blue band peaking at 100% at 452 nm, and a sharp red "
        "spectrum with a very narrow main peak at 612 nm plus secondary peaks near 590, 600, "
        "628, 648, 680 and 708 nm")
