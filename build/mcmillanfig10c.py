# -*- coding: utf-8 -*-
"""Vector redraws of Figures 10.21-10.25 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 10 "Flameproof enclosure 'd'".

Every drawing is a simplified vector redraw of the rendered page images
(p284, p288, p289, p290).  All letter legends, printed labels and dimensions
are transcribed from those pages; Fig. 10.22 keeps the lowercase `outside`,
Fig. 10.24 keeps the one-word `Weatherseal`, and the figure dimensions keep
the printed `8mm min` spelling (no space).  Each public callable returns the
standard five-tuple through `vfig._fig()` on a 680 x 300 canvas and is
registered in `FIGS` by the `_reg` decorator.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _fig, _line, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Displayed strings are pre-vetted Unicode; escape a stray ampersand."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=6.5, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _defs10():
    """Leader markers plus the section hatch fills used by the drawings."""
    return ('<defs>'
            '<marker id="a10" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a10s" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="hatch10" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#6f777d" stroke-width="0.7"/>'
            '</pattern>'
            '<pattern id="vhatch10" width="6" height="6" patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#6f777d" stroke-width="0.7"/>'
            '</pattern>'
            '</defs>' % (INK, INK))


def _title10(o, n, vi, en, size=6.9):
    o.append(T(340, 14, "Hình 10.%d · %s / Figure 10.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub10(o, s, y=27, size=5.8):
    o.append(T(340, y, s, size, color=GREY))


def _ml(o, x, y0, lines, size=6.4, anchor="middle", color=INK, lh=None):
    """Stack one or more label lines; `lines` may be a plain string."""
    if isinstance(lines, str):
        lines = [lines]
    lh = lh or (size + 2.0)
    for i, s in enumerate(lines):
        o.append(T(x, y0 + i * lh, s, size, anchor=anchor, color=color))


def _lead(o, x1, y1, x2, y2):
    o.append(_arrow(x1, y1, x2, y2, sw=0.7, color=GREY, head="a10s"))


def _break(o, x, y0, y1):
    """Small hand-drawn break zigzag on a sectioned member."""
    pts = []
    y = y0
    while y < y1:
        pts.extend([(x, y), (x + 4, y + 3), (x, y + 6)])
        y += 6
    o.append(_poly(pts, sw=0.8, color=INK))


def _dim(o, x0, x1, y, text, ty=None):
    """A horizontal dimension with inward-facing arrows and printed text."""
    o.append(_line(x0, y + 2, x0, y + 26, sw=0.8, color=INK))
    o.append(_line(x1, y + 2, x1, y + 26, sw=0.8, color=INK))
    o.append(_arrow(x0 + 14, y + 8, x0 + 1, y + 8, sw=0.7, color=INK, head="a10s"))
    o.append(_arrow(x1 - 14, y + 8, x1 - 1, y + 8, sw=0.7, color=INK, head="a10s"))
    o.append(T((x0 + x1) / 2.0, ty if ty is not None else y + 4, text, 6.2))


# ------------------------------------------------------------------ 10.21

@_reg
def fig_f1021():
    """Figure 10.21 - closing device with hexagon key type control."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title10(o, 21, "Thiết bị đóng với điều khiển kiểu lục giác",
             "Closing device with hexagon key type control")
    _sub10(o, "Mặt cắt vách vỏ · Enclosure wall in section")

    # Hatched enclosure wall, broken at both ends.
    o.append(_rect(80, 150, 520, 26, fill="url(#hatch10)", sw=1.2))
    _break(o, 80, 150, 176)
    _break(o, 596, 150, 176)

    # Low, wide plug head with a dashed hexagonal socket.
    o.append(_rect(330, 112, 80, 38, fill="#fff", sw=1.3))
    o.append(_poly([(360, 120), (380, 120), (390, 129), (380, 138),
                    (360, 138), (350, 129)],
                   sw=0.9, color=INK, dash="3 2", close=True))
    # Shank with chamfered lower end; thread marks at the wall.
    o.append(_poly([(348, 150), (392, 150), (392, 198), (385, 206),
                    (355, 206), (348, 198)],
                   fill="#fff", sw=1.3, close=True))
    for yy in (158, 165, 172):
        o.append(_line(348, yy, 392, yy, sw=0.5, color=GREY))

    _ml(o, 465, 56, ["Hexagon socket as per", "special fasteners"], 6.5)
    _lead(o, 452, 60, 380, 122)
    _ml(o, 560, 88, ["Narrow shaped head", "to prevent use of pliers"], 6.5)
    _lead(o, 505, 102, 404, 132)
    _ml(o, 175, 96, ["Engaged threads and", "length for threaded", "joint"], 6.6)
    o.append(_line(215, 118, 300, 118, sw=0.7, color=GREY))
    _lead(o, 300, 118, 342, 166)
    o.append(T(285, 145, "Outside", 6.6))
    _ml(o, 630, 156, ["Enclosure", "wall"], 6.6, anchor="start")
    _lead(o, 618, 162, 565, 163)
    o.append(T(370, 226, "Inside", 6.8))

    return _fig(svg(w, h, "".join(o),
                    "Mặt cắt thiết bị đóng đầu lục giác / Hexagon-key closing device in section"),
                "Hình 10.21 · Thiết bị đóng với điều khiển kiểu lục giác",
                "Figure 10.21 · Closing device with hexagon key type control",
                "Mặt cắt vách vỏ có lỗ ren, nút bịt đầu lục giác lõm và thân ren ăn khớp",
                "Sectioned enclosure wall with threaded plug, recessed hexagon socket and engaged threads")


# ------------------------------------------------------------------ 10.22

@_reg
def fig_f1022():
    """Figure 10.22 - closing device with shearing head (lowercase outside)."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title10(o, 22, "Thiết bị đóng với đầu cắt đứt",
             "Closing device with shearing head")
    _sub10(o, "Mặt cắt vách vỏ · Enclosure wall in section")

    o.append(_rect(80, 155, 520, 26, fill="url(#hatch10)", sw=1.2))
    _break(o, 80, 155, 181)
    _break(o, 596, 155, 181)

    # Long shank, slender neck and hexagonal head; residual flange above wall.
    o.append(_rect(345, 155, 48, 72, fill="#fff", sw=1.3))
    o.append(_rect(338, 150, 62, 8, fill="#fff", sw=1.2))
    o.append(_rect(360, 132, 18, 23, fill="#fff", sw=1.2))
    o.append(_poly([(352, 112), (369, 104), (386, 112), (386, 124),
                    (369, 132), (352, 124)],
                   fill="#fff", sw=1.3, close=True))
    o.append(_line(352, 118, 386, 118, sw=0.7, color=GREY))
    # Intended shear plane: short dash below the head.
    o.append(_line(346, 136, 392, 136, sw=0.9, color=INK, dash="4 2"))

    _ml(o, 150, 70, ["This part shears", "on", "tightening"], 6.6)
    _lead(o, 205, 88, 355, 136)
    o.append(T(295, 148, "outside", 6.6))  # lowercase as printed
    _ml(o, 555, 84, ["Residual head narrow", "and shaped to prevent",
                     "use of pliers"], 6.5)
    _lead(o, 500, 104, 398, 155)
    _ml(o, 165, 214, ["Engaged threads", "and length for",
                      "threaded joint"], 6.6)
    _lead(o, 230, 205, 348, 183)
    _ml(o, 630, 161, ["Enclosure", "wall"], 6.6, anchor="start")
    _lead(o, 618, 168, 565, 168)
    o.append(T(370, 250, "Inside", 6.8))

    return _fig(svg(w, h, "".join(o),
                    "Mặt cắt thiết bị đóng đầu cắt / Shearing-head closing device in section"),
                "Hình 10.22 · Thiết bị đóng với đầu cắt đứt",
                "Figure 10.22 · Closing device with shearing head",
                "Đầu lục giác nằm trên cổ mảnh có vệt cắt, thân ren đi xuyên vách vỏ",
                "Hexagon head on a slender neck at the shear plane, shank through the wall")


# ------------------------------------------------------------------ 10.23

@_reg
def fig_f1023():
    """Figure 10.23 - flameproof compression gland."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title10(o, 23, "Tiếp hợp cáp nén chống cháy",
             "Flameproof compression gland")
    _sub10(o, "Mặt cắt dọc · Longitudinal half-section")

    o.append(_line(85, 150, 595, 150, sw=0.7, color=GREY, dash="10 3 2 3"))

    # Incoming cable and bedding/inner-sheath layers.
    o.append(_rect(95, 132, 150, 36, fill="#fff", sw=1.2))
    o.append(_line(102, 141, 240, 141, sw=0.6, color=GREY))
    o.append(_line(102, 159, 240, 159, sw=0.6, color=GREY))
    _break(o, 95, 132, 168)
    o.append(_rect(228, 120, 58, 12, fill="url(#hatch10)", sw=1.0))
    o.append(_rect(228, 168, 58, 12, fill="url(#hatch10)", sw=1.0))

    # Stepped hatched gland body, mirrored about the cable axis.
    for x, y, ww, hh in ((286, 108, 44, 24), (330, 102, 58, 30),
                         (388, 112, 26, 20), (286, 168, 44, 24),
                         (330, 168, 58, 30), (388, 168, 26, 20)):
        o.append(_rect(x, y, ww, hh, fill="url(#hatch10)", sw=1.1))
    # External thread serrations on the shoulder.
    tz = []
    for i in range(9):
        xx = 288 + i * 5
        tz.extend([(xx, 108), (xx + 2.5, 104)])
    o.append(_poly(tz, sw=0.7, color=INK))
    # Annular sealing rings at two stations and the tapering inner cone.
    for x, y in ((322, 110), (322, 180), (386, 112), (386, 179)):
        o.append(_rect(x, y, 10, 9, fill=INK, sw=0))
    o.append(_poly([(300, 134), (348, 122), (348, 140), (300, 148)],
                   fill="#eef3fb", sw=0.9, close=True))
    o.append(_poly([(300, 166), (348, 178), (348, 160), (300, 152)],
                   fill="#eef3fb", sw=0.9, close=True))

    # Outgoing cable, outer sheath, armour clamp and weather seal.
    o.append(_rect(420, 132, 165, 36, fill="#fff", sw=1.2))
    o.append(_rect(420, 124, 165, 52, fill="none", sw=1.0))
    o.append(_line(425, 141, 580, 141, sw=0.6, color=GREY))
    o.append(_line(425, 159, 580, 159, sw=0.6, color=GREY))
    o.append(_poly([(404, 126), (420, 132), (420, 140), (404, 136)],
                   fill="url(#hatch10)", sw=0.9, close=True))
    o.append(_poly([(404, 174), (420, 168), (420, 160), (404, 164)],
                   fill="url(#hatch10)", sw=0.9, close=True))
    o.append(_rect(540, 124, 10, 10, fill=INK, sw=0))
    o.append(_rect(540, 166, 10, 10, fill=INK, sw=0))
    _break(o, 585, 130, 170)

    _dim(o, 248, 292, 84, "8mm min", ty=76)

    _ml(o, 100, 218, ["Cable bedding", "and inner sheath", "(or outer sheath",
                      "if cable not", "armoured)"], 6.2, lh=8.2)
    _lead(o, 150, 208, 205, 168)
    o.append(T(215, 240, "Thread", 6.4))
    _lead(o, 215, 232, 300, 124)
    _ml(o, 305, 224, ["Armour clamp", "(if armoured", "cable)"], 6.2)
    _lead(o, 305, 216, 412, 172)
    _ml(o, 400, 216, ["Exd seal (and", "weather seal", "for unarmoured",
                      "cable)"], 6.2)
    _lead(o, 400, 208, 326, 192)
    _ml(o, 495, 224, ["Weather seal", "(if armoured", "cable)"], 6.2)
    _lead(o, 495, 216, 392, 192)
    _ml(o, 595, 224, ["Cable outer sheath", "(if armoured", "cable)"], 6.2)
    _lead(o, 580, 216, 548, 174)

    return _fig(svg(w, h, "".join(o),
                    "Mặt cắt tiếp hợp cáp nén chống cháy / Compression gland section"),
                "Hình 10.23 · Tiếp hợp cáp nén chống cháy",
                "Figure 10.23 · Flameproof compression gland",
                "Mặt cắt dài đầu nối cáp nén có vòng đệm, kẹp giáp và khe ren 8mm min",
                "Longitudinal section of a compression cable gland with sealing rings and armour clamp")


# ------------------------------------------------------------------ 10.24

@_reg
def fig_f1024():
    """Figure 10.24 - compound filled gland."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title10(o, 24, "Tiếp hợp cáp nhồi hợp chất",
             "Compound filled gland")
    _sub10(o, "Mặt cắt dọc · Longitudinal section")

    o.append(_line(85, 150, 595, 150, sw=0.8, color=GREY, dash="12 3 2 3"))

    # Separated conductor cores at the left.
    for k, yy in enumerate((138, 148, 158)):
        pts = [(105 + i * 6, yy + 3 * math.sin(i * 0.8 + k)) for i in range(25)]
        o.append(_poly(pts, sw=1.0, color=INK))

    # Stepped hatched gland body around the cylindrical flamepath.
    for x, y, ww, hh in ((210, 124, 40, 12), (250, 114, 70, 22),
                         (320, 108, 60, 28), (380, 118, 35, 18),
                         (210, 164, 40, 12), (250, 164, 70, 22),
                         (320, 164, 60, 28), (380, 164, 35, 18)):
        o.append(_rect(x, y, ww, hh, fill="url(#hatch10)", sw=1.1))
    for y0, y1 in ((108, 108), (164, 164)):
        tz = []
        for i in range(12):
            xx = 322 + i * 5
            tz.extend([(xx, y0), (xx + 2.5, y1 - 4 if y0 == 108 else y1 + 4)])
        o.append(_poly(tz, sw=0.6, color=INK))
    o.append(_rect(300, 116, 12, 9, fill=INK, sw=0))
    o.append(_rect(300, 175, 12, 9, fill=INK, sw=0))

    # Conical ferrule containing the compound into which the cores pass.
    o.append(_poly([(372, 130), (446, 120), (446, 140), (372, 140)],
                   fill="#f3eee2", sw=1.1, close=True))
    o.append(_poly([(372, 170), (446, 160), (446, 180), (372, 180)],
                   fill="#f3eee2", sw=1.1, close=True))

    # Cable sheath at the right with inner sheath, O-ring and armour clamp.
    o.append(_rect(444, 124, 151, 52, fill="#fff", sw=1.2))
    o.append(_line(450, 132, 590, 132, sw=0.7, color=GREY))
    o.append(_line(450, 168, 590, 168, sw=0.7, color=GREY))
    _circle(452, 150, 4, fill="#fff", sw=1.0)
    o.append(_poly([(424, 172), (444, 166), (444, 176), (424, 182)],
                   fill="url(#hatch10)", sw=0.9, close=True))
    o.append(_rect(438, 180, 10, 9, fill=INK, sw=0))
    o.append(T(522, 150, "Cable sheath", 6.6))
    _break(o, 595, 130, 170)

    _dim(o, 180, 224, 84, "8mm min", ty=76)

    _ml(o, 330, 62, ["Cylindrical", "flamepath"], 6.3)
    _lead(o, 330, 70, 345, 110)
    _ml(o, 440, 62, ["Ferrule to contain", "compound"], 6.3)
    _lead(o, 440, 70, 410, 124)
    _ml(o, 565, 62, ["Inner sheath", "(if armoured cable)"], 6.3)
    _lead(o, 555, 70, 505, 128)

    o.append(T(140, 232, "Conductors", 6.4))
    _lead(o, 155, 224, 205, 148)
    _ml(o, 285, 230, ["'O' ring", "weather seal"], 6.3)
    _lead(o, 285, 222, 452, 158)
    _ml(o, 400, 230, ["Armour clamp", "(if armoured cable)"], 6.3)
    _lead(o, 400, 222, 435, 186)
    o.append(T(560, 232, "Weatherseal", 6.4))
    _lead(o, 555, 224, 445, 188)

    return _fig(svg(w, h, "".join(o),
                    "Mặt cắt tiếp hợp cáp nhồi hợp chất / Compound gland section"),
                "Hình 10.24 · Tiếp hợp cáp nhồi hợp chất",
                "Figure 10.24 · Compound filled gland",
                "Mặt cắt dài đầu nối cáp nhồi hợp chất có mục chống cháy dạng trụ và ferrule",
                "Longitudinal section of a compound gland with cylindrical flamepath and ferrule")


# ------------------------------------------------------------------ 10.25

@_reg
def fig_f1025():
    """Figure 10.25 - conduit stopping box."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title10(o, 25, "Hộp chặn ống dẫn", "Conduit stopping box")
    _sub10(o, "Mặt cắt ngang · Horizontal section")

    # Hatched enclosure wall with a threaded hole for the conductors.
    o.append(_rect(180, 70, 34, 160, fill="url(#hatch10)", sw=1.2))
    _break(o, 180, 74, 96)
    _break(o, 180, 204, 226)

    # Insulated conductors run through the wall, box and conduit.
    for k, yy in enumerate((142, 150, 158)):
        pts = [(155 + i * 10, yy + 3 * math.sin(i * 0.8 + k)) for i in range(47)]
        o.append(_poly(pts, sw=0.9, color=INK))

    # Stopper box: hatched top/bottom walls and dark sealing blocks at ends.
    o.append(_rect(214, 126, 186, 52, fill="#fff", sw=1.2))
    o.append(_rect(214, 126, 186, 8, fill="url(#hatch10)", sw=1.1))
    o.append(_rect(214, 170, 186, 8, fill="url(#hatch10)", sw=1.1))
    o.append(_rect(214, 134, 9, 36, fill=INK, sw=0))
    o.append(_rect(391, 134, 9, 36, fill=INK, sw=0))

    # Angled filling boss and its slanted hexagon cap screw.
    o.append(_poly([(296, 126), (312, 126), (358, 84), (342, 84)],
                   fill="url(#vhatch10)", sw=1.1, close=True))
    o.append(_poly([(338, 80), (352, 72), (368, 80), (366, 92),
                    (350, 100), (336, 92)],
                   fill="#fff", sw=1.2, close=True))

    # Seamless / seam-welded conduit, double-walled.
    o.append(_rect(400, 130, 215, 44, fill="#fff", sw=1.2))
    o.append(_line(400, 136, 615, 136, sw=0.8, color=GREY))
    o.append(_line(400, 168, 615, 168, sw=0.8, color=GREY))
    _break(o, 613, 134, 170)

    _ml(o, 197, 46, ["Enclosure", "wall"], 6.4)
    _lead(o, 197, 54, 197, 68)
    _ml(o, 105, 118, ["Insulated", "conductors"], 6.4)
    _lead(o, 140, 124, 175, 143)
    o.append(T(150, 200, "Inside", 6.5))
    _ml(o, 105, 236, ["Threaded", "flameproof", "joint"], 6.4)
    _lead(o, 145, 228, 210, 150)
    _ml(o, 295, 54, ["Threaded", "flameproof", "joint"], 6.4)
    _lead(o, 295, 62, 286, 126)
    _ml(o, 455, 54, ["Hexagon cap screw", "(to seal filling point)"], 6.4)
    _lead(o, 430, 62, 362, 82)
    _ml(o, 255, 112, ["Stopper", "box"], 6.4)
    _lead(o, 268, 120, 250, 130)
    _ml(o, 575, 100, ["Seamless or", "seam welded", "conduit"], 6.4)
    _lead(o, 545, 108, 505, 136)
    _ml(o, 530, 214, ["Threaded", "flameproof", "joint"], 6.4)
    _lead(o, 515, 206, 402, 166)
    _ml(o, 310, 246, ["Sealing washers", "or packing",
                      "(to retain compound)"], 6.4)
    _lead(o, 275, 238, 220, 168)
    _lead(o, 345, 238, 395, 168)

    return _fig(svg(w, h, "".join(o),
                    "Mặt cắt hộp chặn ống dẫn / Conduit stopping box section"),
                "Hình 10.25 · Hộp chặn ống dẫn",
                "Figure 10.25 · Conduit stopping box",
                "Mặt cắt hộp chặn có vách vỏ, hộp nhồi hợp chất, nắp vít lục giác và ống dẫn",
                "Section of a stopping box with enclosure wall, compound box, hexagon cap screw and conduit")
