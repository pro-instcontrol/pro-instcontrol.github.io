# -*- coding: utf-8 -*-
"""Vector redraws of Figures 10.11-10.20 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 10 "Protection concept flameproof
enclosure 'd'".

Every drawing is a simplified vector redraw of the printed page image
(pdf pp.267, 271, 274-276, 280-283), with the printed letter legends and
dimensions transcribed from the pages.  Architecture mirrors the other
McMillan figure suppliers: each function returns the standard five-tuple
through `vfig._fig()` on a 680 x 300 canvas and is registered in `FIGS` by
the `_reg` decorator, while the named callables `fig_f1011()` .. `fig_f1020()`
remain the public API.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _f, _fig, _line, _path,
                  _poly, _rect, _txt, svg)

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

def _defs10():
    """Arrow markers and the 45-degree section hatching used throughout."""
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" '
            'refY="2.5" orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" '
            'fill="%s"/></marker>'
            '<marker id="a7" markerWidth="6" markerHeight="6" refX="5" '
            'refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" '
            'fill="%s"/></marker>'
            '<pattern id="sect" width="6" height="6" '
            'patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#5f6b73" '
            'stroke-width="0.7"/></pattern>'
            '</defs>' % (INK, INK))


def _title(o, n, vi, en, size=8.0):
    o.append(T(340, 15, "Hình 10.%d · %s / Figure 10.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, y=29, size=6.4):
    o.append(T(340, y, s, size, color=GREY))


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a7")


def _dimh(x1, x2, y, label, size=6.5, lab_dy=-4):
    return "".join([
        _line(x1, y - 4, x1, y + 4, sw=0.7, color=GREY),
        _line(x2, y - 4, x2, y + 4, sw=0.7, color=GREY),
        _arrow(x1 + 1, y, x2 - 1, y, sw=0.8, color=GREY, head="a7"),
        _arrow(x2 - 1, y, x1 + 1, y, sw=0.8, color=GREY, head="a7"),
        T((x1 + x2) / 2.0, y + lab_dy, label, size, color=INK),
    ])


def _dimv(y1, y2, x, label, size=6.5, lab_dx=6, anchor="start"):
    return "".join([
        _line(x - 4, y1, x + 4, y1, sw=0.7, color=GREY),
        _line(x - 4, y2, x + 4, y2, sw=0.7, color=GREY),
        _arrow(x, y1 + 1, x, y2 - 1, sw=0.8, color=GREY, head="a7"),
        _arrow(x, y2 - 1, x, y1 + 1, sw=0.8, color=GREY, head="a7"),
        T(x + lab_dx, (y1 + y2) / 2.0 + 2.4, label, size,
          anchor=anchor, color=INK),
    ])


def _rtext(x, y, s, size=7.0, color=INK):
    """Rotated axis title (kept clear of the plot area)."""
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (_f(x), _f(y), _f(x), _f(y), size, color, esc(s)))


def _arc_pts(cx, cy, r, a0, a1, step=5):
    return [(cx + r * math.cos(math.radians(a)),
             cy - r * math.sin(math.radians(a)))
            for a in range(int(a0), int(a1) + 1, step)]


def _band(cx, cy, r_in, r_out, a0, a1, fill, step=5):
    outer = _arc_pts(cx, cy, r_out, a0, a1, step)
    inner = list(reversed(_arc_pts(cx, cy, r_in, a0, a1, step)))
    return _poly(outer + inner, fill=fill, sw=1.0, close=True)


def _break(x, y, n=4):
    """Small wavy broken-end mark for a bar or wall drawn in section."""
    d = "M %s %s " % (_f(x), _f(y))
    for k in range(n):
        d += "q 3 -4 6 0 q 3 4 6 0 "
    return _path(d, sw=0.9, color=INK)


# ------------------------------------------------------------------ 10.11

@_reg
def fig_f1011():
    """Figure 10.11 - partial cylindrical joint: section and face view."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 11, "Khớp nối hình trụ một phần", "Partial cylindrical joint")
    _sub(o, "Mặt cắt qua thành vỏ / Face view of cover plate")

    # upper view - arch-shaped cross-section through the cylindrical wall
    cx, cy = 175, 150
    o.append(_band(cx, cy, 74, 90, 4, 176, PAPER))              # body
    o.append(_band(cx, cy, 86, 101, 18, 166, "url(#sect)"))     # cover plate
    o.append(T(175, 76, "Section", 6.2, color=GREY))
    o.append(T(175, 125, "Interior of", 6.6, color=INK))
    o.append(T(175, 137, "enclosure", 6.6, color=INK))
    o.append(_dimh(80, 98, 108, "L"))
    o.append(_line(80, 112, 80, 130, sw=0.7, color=GREY))
    o.append(_line(98, 112, 98, 124, sw=0.7, color=GREY))
    o.append(T(250, 60, "Cover plate", 6.6, anchor="end"))
    o.append(_lead(245, 62, 238, 81))
    o.append(T(38, 195, "Body", 6.6, anchor="start"))
    o.append(_lead(72, 192, 85, 153))

    # lower view - wavy body outline with cover plate and dashed opening
    o.append(_path(
        "M 350 150 C 350 122 364 105 385 108 C 405 111 412 96 436 100 "
        "C 460 104 470 92 496 98 C 522 104 540 94 561 104 "
        "C 582 114 602 110 610 128 C 618 146 612 164 605 178 "
        "C 598 192 584 194 569 201 C 550 209 531 200 511 205 "
        "C 491 210 470 202 450 206 C 430 210 410 200 390 198 "
        "C 370 196 352 180 350 150 Z", sw=1.2))
    o.append(_rect(410, 115, 140, 55, fill=PAPER, sw=1.3))
    o.append(_rect(430, 125, 100, 35, fill=PAPER, sw=1.0, dash="4 3"))
    o.append(_poly([(544, 115), (552, 115), (552, 123)],
                   fill=INK, sw=0.6, close=True))
    o.append(T(330, 92, "Body", 6.6, anchor="start"))
    o.append(_lead(366, 94, 382, 112))
    o.append(T(650, 92, "Cover plate", 6.6, anchor="end"))
    o.append(_lead(644, 94, 548, 117))
    o.append(_dimv(130, 152, 335, "L", lab_dx=-9, anchor="end"))
    o.append(_dimh(410, 430, 222, "L"))
    o.append(T(480, 252, "L = Joint width", 7.0, color=INK))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.11")),
                "Hình 10.11 · Khớp nối hình trụ một phần",
                "Figure 10.11 · Partial cylindrical joint",
                "Mặt cắt vòm qua thành vỏ cho thấy bản che có gạch chéo chồng lên "
                "thân vỏ, bên trong là khoang vỏ; hình chiếu mặt có đường viền "
                "lượn sóng, bản che và lỗ mở nét đứt, các kí hiệu L",
                "Arched section through the wall showing the hatched cover plate "
                "overlapping the body and the enclosure interior; face view with "
                "a wavy body outline, solid cover plate, dashed opening and "
                "joint-width L dimensions")


# ------------------------------------------------------------------ 10.12

@_reg
def fig_f1012():
    """Figure 10.12 - labyrinth joint around a rotating shaft."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 12, "Hình học của khớp nối mê cung",
           "Geometry of a labyrinth joint")
    _sub(o, "Đường dẫn ngọn lửa qua các răng xen kẽ / Tortuous flamepath through interleaved teeth")

    o.append(_rect(80, 150, 520, 42, fill="url(#sect)"))          # shaft
    o.append(_rect(300, 55, 42, 95, fill="url(#sect)"))           # casing, upper
    o.append(_rect(300, 192, 42, 68, fill="url(#sect)"))          # casing, lower
    o.append(_rect(342, 100, 95, 50, fill=PAPER))                 # bearing, upper
    o.append(_rect(342, 192, 95, 48, fill=PAPER))                 # bearing, lower
    for y0 in (110, 194):
        o.append(_rect(268, y0, 74, 38, fill=PAPER, sw=1.0))
    for i in range(3):
        o.append(_rect(272 + i * 24, 112, 12, 11, fill=PAPER, sw=0.9))
        o.append(_rect(284 + i * 24, 128, 12, 11, fill="url(#sect)", sw=0.9))
        o.append(_rect(272 + i * 24, 196, 12, 11, fill=PAPER, sw=0.9))
        o.append(_rect(284 + i * 24, 212, 12, 11, fill="url(#sect)", sw=0.9))

    o.append(T(470, 62, "Body of machine", 6.6, anchor="start"))
    o.append(_lead(466, 64, 332, 80))
    o.append(T(165, 105, "Labyrinth joint", 6.6, anchor="start"))
    o.append(_lead(223, 107, 285, 120))
    o.append(T(480, 120, "Bearing assembly", 6.6, anchor="start"))
    o.append(_lead(476, 122, 432, 128))
    o.append(T(92, 218, "Machine interior", 6.6, anchor="start"))
    o.append(_lead(152, 216, 182, 200))
    o.append(T(92, 252, "Shaft", 6.6, anchor="start"))
    o.append(_lead(122, 250, 200, 176))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.12")),
                "Hình 10.12 · Hình học của khớp nối mê cung",
                "Figure 10.12 · Geometry of a labyrinth joint",
                "Trục quay nằm ngang đi qua thân máy có gạch chéo; hai bộ răng "
                "mê cung xen kẽ ở trên và dưới trục, cụm ổ bi ở bên phải; các "
                "nhãn gọi tên thân máy, trục, khoang máy và cụm ổ bi",
                "Horizontal hatched shaft through a hatched machine casing, with "
                "interleaved labyrinth teeth above and below the shaft and a "
                "stepped bearing assembly at the right; leaders name the casing, "
                "shaft, machine interior, labyrinth joint and bearing assembly")


# ------------------------------------------------------------------ 10.13

@_reg
def fig_f1013():
    """Figure 10.13 - shaft joint geometry, D, d, k, m legend."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 13, "Hình học của khớp nối trục", "Geometry of a shaft joint",
           size=7.8)

    o.append(_path(
        "M 250 52 C 285 50 306 65 321 80 C 336 96 331 119 325 140 "
        "C 319 166 299 186 270 200 C 240 212 205 205 185 188 "
        "C 165 170 160 145 165 120 C 170 95 181 69 206 58 "
        "C 221 52 235 52 250 52 Z", fill="url(#sect)", sw=1.2))
    o.append(_circle(250, 135, 50, fill=PAPER, sw=1.2))
    o.append(_circle(250, 135, 35, fill="url(#sect)", sw=1.2))
    o.append(_dimh(200, 300, 42, "D", size=7.0))
    o.append(_line(200, 46, 200, 86, sw=0.7, color=GREY))
    o.append(_line(300, 46, 300, 86, sw=0.7, color=GREY))
    o.append(_dimh(215, 285, 220, "d", size=7.0))
    o.append(_line(215, 216, 215, 168, sw=0.7, color=GREY))
    o.append(_line(285, 216, 285, 168, sw=0.7, color=GREY))
    o.append(_lead(216, 171, 226, 161))
    o.append(T(203, 177, "k", 6.8, anchor="end"))
    o.append(_lead(284, 171, 274, 161))
    o.append(T(297, 177, "m", 6.8, anchor="start"))
    o.append(T(92, 110, "Shaft", 6.6, anchor="start"))
    o.append(_lead(132, 112, 222, 126))
    o.append(T(360, 100, "Static part of joint", 6.6, anchor="start"))
    o.append(_lead(356, 102, 306, 106))
    o.append(T(30, 238, "d = Shaft diameter", 6.2, anchor="start", color=INK))
    o.append(T(30, 250, "k = Minimum acceptable radial clearance",
               6.2, anchor="start", color=INK))
    o.append(T(350, 238, "m = Maximum permissible gap for a cylindrical joint",
               6.2, anchor="start", color=INK))
    o.append(T(350, 250, "D = d + m + k", 6.2, anchor="start", color=INK))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.13")),
                "Hình 10.13 · Hình học của khớp nối trục",
                "Figure 10.13 · Geometry of a shaft joint",
                "Mặt cắt vành: trục gạch chéo nằm trong lỗ của khối vỏ tĩnh gạch "
                "chéo; các mũi tên D, d, k, m với bảng giải thích ở dưới",
                "Annular section with a hatched shaft inside the bore of a "
                "hatched static joint part; dimension arrows D, d, k and m with "
                "the printed four-line legend below")


# ------------------------------------------------------------------ 10.14

@_reg
def fig_f1014():
    """Figure 10.14 - limiting dimensions L1 and L2 of a floating shaft joint."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 14, "Kích thước giới hạn của khớp nối trục",
           "Limiting dimensions for shaft joint of rotating machines", size=7.4)

    o.append(_rect(80, 132, 520, 22, fill="url(#sect)"))           # shaft
    o.append(_rect(300, 45, 80, 87, fill="url(#sect)"))            # fixed part, top
    o.append(_rect(315, 62, 53, 68, fill=PAPER, sw=1.0))
    o.append(_rect(320, 72, 40, 56, fill="url(#sect)"))            # floating part
    o.append(_rect(312, 124, 53, 8, fill=PAPER, sw=0.9))           # flanged joint
    o.append(_rect(300, 154, 80, 81, fill="url(#sect)"))           # fixed part, bottom
    o.append(_rect(315, 156, 53, 64, fill=PAPER, sw=1.0))
    o.append(_rect(320, 160, 40, 55, fill="url(#sect)"))            # floating part
    o.append(_rect(430, 110, 60, 44, fill="url(#sect)"))            # bearing
    o.append(_rect(430, 175, 50, 40, fill="url(#sect)"))            # stop
    o.append(_dimh(300, 380, 40, "L<sub>1</sub>", size=7.0))
    o.append(_line(300, 44, 300, 62, sw=0.7, color=GREY))
    o.append(_line(380, 44, 380, 62, sw=0.7, color=GREY))
    o.append(_dimv(160, 220, 275, "L<sub>2</sub>", size=7.0, lab_dx=-8,
                   anchor="end"))

    o.append(T(150, 58, "Cylindrical joint", 6.4, anchor="start"))
    o.append(_lead(224, 60, 358, 95))
    o.append(T(150, 85, "Floating part", 6.4, anchor="start"))
    o.append(_lead(206, 87, 334, 100))
    o.append(T(150, 115, "Shaft", 6.4, anchor="start"))
    o.append(_lead(182, 117, 250, 143))
    o.append(T(85, 205, "Machine interior", 6.4, anchor="start"))
    o.append(_lead(152, 202, 180, 158))
    o.append(T(400, 50, "Fixed part", 6.4, anchor="start"))
    o.append(_lead(396, 52, 376, 62))
    o.append(T(400, 80, "Flanged joint", 6.4, anchor="start"))
    o.append(_lead(440, 82, 366, 127))
    o.append(T(520, 100, "Shaft bearing in fixed", 6.3, anchor="start"))
    o.append(T(520, 110, "part of enclosure", 6.3, anchor="start"))
    o.append(_lead(516, 106, 480, 130))
    o.append(T(520, 195, "Stop preventing", 6.3, anchor="start"))
    o.append(T(520, 205, "rotation", 6.3, anchor="start"))
    o.append(_lead(516, 200, 476, 195))
    o.append(T(340, 250, "L<sub>1</sub> = Cylindrical joint", 6.2, color=INK))
    o.append(T(340, 263,
               "L<sub>2</sub> = Flange joint allowing cylindrical joint assembly to float",
               6.2, color=INK))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.14")),
                "Hình 10.14 · Kích thước giới hạn của khớp nối trục trên máy quay",
                "Figure 10.14 · Limiting dimensions for shaft joint of rotating machines",
                "Mặt cắt dọc qua trục máy quay: chi tiết cố định và chi tiết nổi "
                "bao quanh trục, khớp trụ ở giữa, khớp bích cho phép nổi, ổ bi và "
                "chặn quay; kích thước L₁ và L₂ kèm ghi chú",
                "Axial section through a rotating-machine shaft with fixed and "
                "floating parts, the cylindrical joint between them, a flanged "
                "joint allowing float, a bearing and a stop preventing rotation; "
                "dimensions L1 and L2 with the printed notes")


# ------------------------------------------------------------------ 10.15

@_reg
def fig_f1015():
    """Figure 10.15 - cylindrical joint with grease retaining rings."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 15, "Khớp nối hình trụ có vòng giữ mỡ",
           "Cylindrical joint with grease retaining rings", size=7.8)

    o.append(_rect(80, 120, 520, 45, fill="url(#sect)"))            # shaft
    o.append(_rect(330, 55, 38, 65, fill="url(#sect)"))             # machine body
    o.append(_rect(368, 90, 60, 30, fill="url(#sect)"))
    o.append(_rect(300, 104, 14, 20, fill="url(#sect)", sw=0.9))    # rings
    o.append(_rect(314, 104, 14, 20, fill="url(#sect)", sw=0.9))
    o.append(_rect(330, 170, 40, 18, fill="url(#sect)"))            # flamepath ledge
    o.append(_rect(390, 165, 70, 40, fill="url(#sect)"))            # bearing
    o.append(_rect(405, 205, 30, 40, fill="url(#sect)"))
    o.append(_dimh(330, 370, 200, "L"))

    o.append(T(160, 68, "Grease retaining rings", 6.4, anchor="start"))
    o.append(_lead(228, 70, 306, 116))
    o.append(_lead(238, 78, 322, 116))
    o.append(T(440, 60, "Machine body", 6.4, anchor="start"))
    o.append(_lead(436, 62, 350, 76))
    o.append(T(520, 108, "Shaft", 6.4, anchor="start"))
    o.append(_lead(516, 110, 480, 140))
    o.append(T(85, 200, "Machine interior", 6.4, anchor="start"))
    o.append(_lead(152, 198, 180, 175))
    o.append(T(200, 212, "Flamepath", 6.4, anchor="start"))
    o.append(_lead(244, 210, 338, 176))
    o.append(T(500, 225, "Bearing assembly", 6.4, anchor="start"))
    o.append(_lead(496, 227, 440, 190))
    o.append(T(340, 258, "L = Length of flameproof joint.", 6.2, color=INK))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.15")),
                "Hình 10.15 · Khớp nối hình trụ có vòng giữ mỡ",
                "Figure 10.15 · Cylindrical joint with grease retaining rings",
                "Mặt cắt trục ngang có thân máy gạch chéo, hai vòng giữ mỡ nhỏ "
                "trên trục, khe dẫn ngọn lửa dưới thân máy đo bằng L và cụm ổ bi "
                "bên dưới; các nhãn theo bản in",
                "Axial section of a hatched shaft and machine body with two small "
                "grease retaining rings, the flamepath beneath the body measured "
                "by L, and a bearing assembly below; printed leaders retained")


# ------------------------------------------------------------------ 10.16

@_reg
def fig_f1016():
    """Figure 10.16 - explosion pressure profile (P, t, maximum rate of rise)."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 16, "Biểu đồ áp suất trong vỏ chống cháy",
           "Profile of pressure inside a flameproof enclosure", size=7.8)
    _sub(o, "resulting form an internal explosion / do một vụ nổ bên trong", 29, 6.2)

    o.append(_arrow(60, 230, 610, 230, sw=1.2))
    o.append(_arrow(60, 230, 60, 55, sw=1.2))
    o.append(_rtext(20, 150, "Differential pressure (N/m²)", 7.0))
    o.append(T(610, 247, "Time", 6.8, anchor="end"))
    o.append(T(610, 258, "(seconds)", 6.8, anchor="end"))
    o.append(T(52, 244, "0", 6.8, anchor="end"))
    o.append(_path("M 60 230 C 120 228 160 210 200 165 "
                   "C 230 125 260 102 300 100 C 360 98 450 130 590 170",
                   sw=1.6))
    o.append(_line(60, 150, 236, 150, sw=0.9, dash="4 3", color=GREY))
    o.append(T(52, 153, "p", 7.0, anchor="end"))
    o.append(_line(200, 175, 322, 68, sw=0.9, dash="4 3", color=GREY))
    o.append(T(330, 62, "Maximum rate", 6.6, anchor="start"))
    o.append(T(330, 72, "of rise", 6.6, anchor="start"))
    o.append(_line(240, 135, 240, 230, sw=0.9, dash="4 3", color=GREY))
    o.append(_line(60, 240, 60, 245, sw=0.8, color=GREY))
    o.append(_line(240, 240, 240, 245, sw=0.8, color=GREY))
    o.append(_line(60, 242, 240, 242, sw=0.8, color=GREY))
    o.append(T(150, 255, "t", 6.8))
    o.append(T(340, 267, "P = Maximum explosion pressure; t = Pressure rise time",
               6.4, color=INK))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.16")),
                "Hình 10.16 · Biểu đồ áp suất trong vỏ chống cháy do một vụ nổ bên trong",
                "Figure 10.16 · Profile of pressure inside a flameproof enclosure resulting form an internal explosion",
                "Đồ thị áp suất vi phân theo thời gian: đường cong tăng dạng "
                "chữ S tới đỉnh rồi giảm, đường ngang đứt nét ở mức p, tiếp "
                "tuyến đứt nét chỉ tốc độ tăng lớn nhất và đoạn ngang chỉ t",
                "Differential-pressure against time graph with a sigmoidal rise "
                "to a peak and slow decay, a dashed level p, a dashed tangent "
                "labelled maximum rate of rise and a time bracket t")


# ------------------------------------------------------------------ 10.17

@_reg
def fig_f1017():
    """Figure 10.17 - two enclosures showing pressure piling."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 17, "Ảnh hưởng của hiện tượng tích áp",
           "Effects of pressure piling")

    o.append(_rect(170, 60, 400, 12, fill="url(#sect)"))            # top wall
    o.append(_rect(170, 203, 400, 12, fill="url(#sect)"))           # bottom wall
    o.append(_rect(170, 60, 14, 155, fill="url(#sect)"))            # left wall
    o.append(_rect(556, 60, 14, 155, fill="url(#sect)"))            # right wall
    o.append(_rect(360, 72, 14, 58, fill="url(#sect)"))             # partition
    o.append(_rect(360, 142, 14, 61, fill="url(#sect)"))
    o.append(_poly([(238, 100), (268, 118), (306, 110), (318, 140),
                    (298, 162), (276, 154), (252, 176), (230, 158),
                    (222, 132)], fill=PAPER, sw=1.3, close=True))
    o.append(T(270, 143, "Explosion", 6.8, color=INK))
    o.append(_arrow(325, 135, 400, 135, sw=1.1))
    o.append(_arrow(325, 145, 400, 145, sw=1.1))
    o.append(T(405, 128, "Shock", 6.6, anchor="start"))
    o.append(T(405, 138, "fronts", 6.6, anchor="start"))

    o.append(T(170, 52, "Pressure = p initially", 6.6, anchor="start"))
    o.append(_lead(220, 54, 240, 90))
    o.append(T(430, 52, "Pressure = p + δp initially", 6.6, anchor="start"))
    o.append(_lead(480, 54, 490, 90))
    o.append(T(90, 232, "Maximum explosion", 6.2, anchor="start"))
    o.append(T(90, 242, "pressure = P", 6.2, anchor="start"))
    o.append(_lead(190, 230, 205, 207))
    o.append(T(250, 232, "Small hole to allow", 6.2, anchor="start"))
    o.append(T(250, 242, "passage of wires between", 6.2, anchor="start"))
    o.append(T(250, 252, "enclosures", 6.2, anchor="start"))
    o.append(_lead(340, 229, 367, 138))
    o.append(T(430, 232, "Maximum explosion pressure", 6.2, anchor="start"))
    o.append(T(430, 242, "typically approaches (p + δp) × P/p", 6.2,
               anchor="start"))
    o.append(_lead(470, 229, 505, 207))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.17")),
                "Hình 10.17 · Ảnh hưởng của hiện tượng tích áp",
                "Figure 10.17 · Effects of pressure piling",
                "Hai buồng kề nhau có vách gạch chéo và lỗ nhỏ ở vách ngăn; "
                "buồng trái có chùm nổ, mũi tên sóng xung kích đi sang buồng "
                "phải; các nhãn áp suất ban đầu, áp suất nổ lớn nhất và công thức",
                "Two adjoining hatched chambers with a small hole in the "
                "partition; a starburst explosion in the left chamber and shock "
                "fronts crossing to the right, with initial pressure labels, "
                "maximum explosion pressure and the printed formula")


# ------------------------------------------------------------------ 10.18

@_reg
def fig_f1018():
    """Figure 10.18 - indirect entry enclosure with separate terminal box."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 18, "Vỏ chống cháy vào gián tiếp",
           "Indirect entry flameproof enclosure", size=7.8)
    _sub(o, "Vỏ chính và hộp đấu dây là hai vỏ riêng biệt / Main enclosure and terminal box are separate", 29, 6.2)

    o.append(_rect(90, 75, 14, 140, fill="url(#sect)"))             # main walls
    o.append(_rect(90, 75, 380, 13, fill="url(#sect)"))
    o.append(_rect(90, 202, 380, 13, fill="url(#sect)"))
    o.append(_rect(490, 75, 14, 140, fill="url(#sect)"))            # terminal walls
    o.append(_rect(490, 75, 70, 13, fill="url(#sect)"))
    o.append(_rect(490, 202, 70, 13, fill="url(#sect)"))
    o.append(_rect(546, 75, 14, 140, fill="url(#sect)"))
    o.append(_rect(150, 120, 130, 55, fill=PAPER, sw=1.2))          # equipment
    o.append(_rect(452, 128, 38, 13, fill=INK, sw=0.8))             # bushings
    o.append(_rect(452, 164, 38, 13, fill=INK, sw=0.8))
    o.append(_path("M 280 138 C 310 134 330 132 452 134", sw=1.1))
    o.append(_path("M 280 162 C 310 168 330 170 452 170", sw=1.1))
    o.append(_path("M 490 134 C 520 136 528 160 525 208", sw=1.1))
    o.append(_path("M 490 170 C 510 174 520 190 525 208", sw=1.1))
    o.append(_circle(525, 220, 7, fill=PAPER, sw=1.1))              # gland
    o.append(_line(525, 227, 525, 250, sw=1.1))
    o.append(_line(529, 227, 529, 250, sw=1.1))
    o.append(_path("M 523 256 q 3 -4 6 0 q 3 4 6 0", sw=0.9))

    o.append(T(200, 60, "Main enclosure", 6.6, anchor="start"))
    o.append(_lead(266, 62, 300, 78))
    o.append(T(370, 60, "Bushings", 6.6, anchor="start"))
    o.append(_lead(420, 62, 468, 132))
    o.append(T(570, 60, "Terminal box", 6.6, anchor="end"))
    o.append(_lead(554, 62, 522, 100))
    o.append(T(215, 143, "Electrical", 6.6, color=INK))
    o.append(T(215, 155, "equipment", 6.6, color=INK))
    o.append(T(430, 250, "Cable gland", 6.6, anchor="end"))
    o.append(_lead(432, 248, 520, 224))
    o.append(T(560, 258, "Cable", 6.6, anchor="start"))
    o.append(_lead(556, 256, 530, 248))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.18")),
                "Hình 10.18 · Vỏ chống cháy vào gián tiếp. Lưu ý: Vỏ chính và hộp đấu dây là các vỏ hoàn toàn riêng biệt",
                "Figure 10.18 · Indirect entry flameproof enclosure. Note: The main enclosure and terminal box are entirely separate enclosures",
                "Vỏ chính và hộp đấu dây là hai vỏ riêng biệt nối với nhau qua "
                "hai thông đạo; bên trong vỏ chính có thiết bị điện, dây dẫn "
                "chạy qua thông đạo tới hộp và đi ra qua cổng cáp và cáp",
                "A main enclosure and a physically separate terminal box joined "
                "by two bushings, with electrical equipment inside the main "
                "enclosure, wires running through the bushings and out through "
                "a cable gland and cable")


# ------------------------------------------------------------------ 10.19

@_reg
def fig_f1019():
    """Figure 10.19 - direct entry enclosure with terminals inside."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 19, "Vỏ chống cháy vào trực tiếp",
           "Direct entry flameproof enclosure")

    o.append(_rect(110, 70, 14, 140, fill="url(#sect)"))            # enclosure walls
    o.append(_rect(110, 70, 410, 13, fill="url(#sect)"))
    o.append(_rect(110, 197, 410, 13, fill="url(#sect)"))
    o.append(_rect(520, 70, 18, 140, fill="url(#sect)"))            # separate right wall
    o.append(_rect(180, 115, 150, 60, fill=PAPER, sw=1.2))          # components
    o.append(_circle(330, 130, 4, fill=INK))
    o.append(_circle(330, 155, 4, fill=INK))
    o.append(_path("M 330 130 C 360 140 390 180 420 200", sw=1.1))
    o.append(_path("M 330 155 C 360 165 390 190 420 200", sw=1.1))
    o.append(_rect(412, 200, 26, 20, fill=PAPER, sw=1.1))           # gland boss
    o.append(_poly([(412, 220), (438, 220), (432, 232), (418, 232)],
                   fill=PAPER, sw=1.1, close=True))
    o.append(_line(425, 232, 425, 258, sw=1.1))
    o.append(_path("M 423 264 q 3 -4 6 0 q 3 4 6 0", sw=0.9))

    o.append(T(200, 58, "Enclosure", 6.6, anchor="start"))
    o.append(_lead(262, 60, 300, 74))
    o.append(T(400, 58, "Terminals", 6.6, anchor="start"))
    o.append(_lead(396, 60, 332, 128))
    o.append(T(255, 140, "Electrical", 6.6, color=INK))
    o.append(T(255, 152, "components", 6.6, color=INK))
    o.append(T(470, 224, "Gland", 6.6, anchor="start"))
    o.append(_lead(466, 226, 438, 218))
    o.append(T(470, 256, "Cable", 6.6, anchor="start"))
    o.append(_lead(466, 258, 428, 248))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.19")),
                "Hình 10.19 · Vỏ chống cháy vào trực tiếp",
                "Figure 10.19 · Direct entry flameproof enclosure",
                "Vỏ có thành gạch chéo, thiết bị điện và các cực đấu nối nằm "
                "trong cùng một buồng; dây dẫn chạy xuống cổng cáp ở đáy và cáp "
                "đi ra ngoài",
                "Hatched-wall enclosure with the electrical components and "
                "terminals inside the same chamber, conductors sweeping down to "
                "the gland in the bottom wall and a cable exiting below")


# ------------------------------------------------------------------ 10.20

@_reg
def fig_f1020():
    """Figure 10.20 - internally secured closing device."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 20, "Thiết bị đóng cố định từ bên trong",
           "Internally secured closing device")

    o.append(_rect(90, 120, 500, 50, fill="url(#sect)"))            # wall
    o.append(_break(92, 120) + _break(92, 170))
    o.append(_break(574, 120) + _break(574, 170))
    o.append(_rect(320, 95, 50, 130, fill=PAPER, sw=1.2))           # plug shank
    o.append(_path("M 316 95 Q 345 68 374 95 Z", fill=PAPER, sw=1.2))
    o.append(_rect(337, 82, 14, 6, fill=PAPER, sw=0.9))             # slot
    o.append(_path("M 320 186 q -12 6 -6 14 q 8 6 6 -6", sw=1.0))
    o.append(_path("M 370 186 q 12 6 6 14 q -8 6 -6 -6", sw=1.0))
    o.append(_path("M 320 196 q -12 6 -6 14 q 8 6 6 -6", sw=1.0))
    o.append(_path("M 370 196 q 12 6 6 14 q -8 6 -6 -6", sw=1.0))

    o.append(T(430, 60, "Closing device", 6.5, anchor="start"))
    o.append(T(430, 70, "(no specific head precautions)", 6.5,
               anchor="start"))
    o.append(_lead(426, 66, 360, 90))
    o.append(T(180, 86, "Engaged threads", 6.4, anchor="start"))
    o.append(T(180, 97, "and length for", 6.4, anchor="start"))
    o.append(T(180, 108, "threaded joint", 6.4, anchor="start"))
    o.append(_lead(272, 106, 322, 140))
    o.append(T(285, 112, "Outside", 6.4, anchor="end"))
    o.append(T(345, 220, "Inside", 6.4, color=INK))
    o.append(T(600, 143, "Enclosure wall", 6.5, anchor="end"))
    o.append(_lead(596, 146, 500, 145))
    o.append(T(430, 198, "Retaining", 6.4, anchor="start"))
    o.append(T(430, 208, "device", 6.4, anchor="start"))
    o.append(_lead(426, 204, 380, 195))
    return _fig(svg(w, h, "".join(o), esc("Fig 10.20")),
                "Hình 10.20 · Thiết bị đóng được cố định từ bên trong",
                "Figure 10.20 · Internally secured closing device",
                "Mặt cắt thành vỏ gạch chéo với nút đóng luồn từ ngoài vào, đầu "
                "vòm có khe, thân có ren ăn khớp và hai vòng giữ ở bên trong; "
                "các nhãn Outside, Inside và Enclosure wall",
                "Section through a hatched enclosure wall with a plug fitted "
                "from outside, a domed slotted head, engaged threads and "
                "internal retaining coils; leaders mark Outside, Inside and "
                "Enclosure wall")
