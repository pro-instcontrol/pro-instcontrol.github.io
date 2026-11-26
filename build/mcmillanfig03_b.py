# -*- coding: utf-8 -*-
"""Vector redraws of Figures 3.9, 3.10 and 3.11 in A. McMillan,
*Electrical Installations in Hazardous Areas*, Chapter 3
"Area classification practice for gases, vapours and mists in freely
ventilated situations".

The three figures are area-classification cross-sections.  Printed hatch
conventions are preserved: square grid = Zone 0, crosshatch = Zone 1 and
single diagonal = Zone 2; liquid is drawn as short horizontal dashes.
Captions and dimension letters are taken from the page renders, since the
PDF text layer garbles them.

Architecture mirrors `mcmillanfig02_a.py`: each function returns the
standard five-tuple through `vfig._fig()` and is registered in `FIGS` by
the `_reg` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, PAPER, _arrow, _circle, _defs, _fig,
                  _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _grid(x, y, w, h, step=8, color="#9a9a9a", sw=0.6):
    """Zone 0: printed square-grid hatch, drawn as crossing straight lines."""
    o = []
    xx = x + step
    while xx < x + w:
        o.append(_line(xx, y, xx, y + h, sw=sw, color=color))
        xx += step
    yy = y + step
    while yy < y + h:
        o.append(_line(x, yy, x + w, yy, sw=sw, color=color))
        yy += step
    return "".join(o)


def _liquid(x, y, w, h, step=13, dash=7, sw=0.7):
    """Liquid: short horizontal dashes in evenly spaced rows."""
    o = []
    yy = y + 4
    while yy < y + h - 2:
        xx = x + 3
        while xx + dash < x + w - 2:
            o.append(_line(xx, yy, xx + dash, yy, sw=sw, color=INK))
            xx += step
        yy += 9
    return "".join(o)


def _hatch_fill(d, patterns, outline=True, sw=1.3):
    """Opaque base plus one or more overlay hatch patterns on a path."""
    o = [_path(d, fill=PAPER, sw=0)]
    for p in patterns:
        o.append(_path(d, fill=p, sw=0))
    if outline:
        o.append(_path(d, fill="none", sw=sw))
    return "".join(o)


_LEGEND = ("Vùng 0 = lưới ô vuông / Zone 0 = square grid;  "
           "Vùng 1 = ô chéo chữ X / Zone 1 = crosshatch;  "
           "Vùng 2 = gạch chéo đơn / Zone 2 = single diagonal")


def _legend(y):
    return T(340, y, _LEGEND, 6.6, color=GREY)


@_reg
def fig_f309():
    """Figure 3.9 - Fixed roof stock tank."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_rect(0, 0, w, h, fill=PAPER, sw=0))
    o.append(T(340, 20, "Hình 3.9 · Bể chứa mái cố định / "
                        "Figure 3.9 · Fixed roof stock tank",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34, "a = 3 m, b = 1.5 m, c = 2.5 m", 7.4, color=GREY))

    # Zone 2: single-diagonal band wrapped around the tank and bund, with a
    # notch occupied by the tank itself and rounded outside shoulders.
    outer = ("M270,190 L222,190 L222,258 Q222,288 192,300 L156,300 "
             "Q130,300 130,326 L130,350 L550,350 L550,326 "
             "Q550,300 524,300 L488,300 Q458,288 458,258 "
             "L458,190 L410,190 L410,350 L270,350 Z")
    o.append(_hatch_fill(outer, ("url(#h6)",), sw=1.4))

    # Tank in section: Zone 0 square-grid vapour space over dashed liquid.
    o.append(_rect(270, 190, 140, 160, fill=PAPER, sw=1.5))
    o.append(_grid(271, 191, 138, 60, step=8))
    o.append(_liquid(271, 253, 138, 96))

    # Zone 1: crosshatched dome around the roof vent.
    dome = "M286,205 L286,170 A69,62 0 0 1 424,170 L424,205 Z"
    o.append(_hatch_fill(dome, ("url(#h6)", "url(#h7)"), sw=1.4))

    # Zone 1: bund interior either side of the tank.
    o.append(_hatch_fill("M230,312 H270 V350 H230 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.1))
    o.append(_hatch_fill("M410,312 H450 V350 H410 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.1))
    o.append(_rect(226, 300, 4, 50, fill=PAPER, sw=1.2))
    o.append(_rect(450, 300, 4, 50, fill=PAPER, sw=1.2))

    # Short vent pipe on the roof.
    o.append(_rect(349, 170, 9, 20, fill=PAPER, sw=1.2))
    o.append(_line(346, 170, 361, 170, sw=1.6))

    o.append(_line(126, 350, 554, 350, sw=1.8))

    # Printed dimension arrows.
    o.append(_arrow(352, 190, 388, 152, sw=1.0))
    o.append(T(346, 194, "a", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(196, 246, 226, 214, sw=1.0))
    o.append(T(192, 250, "b", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(500, 334, 538, 298, sw=1.0))
    o.append(T(496, 340, "c", 8.4, anchor="end", color=INK, weight="600"))

    o.append(_line(452, 318, 492, 304, sw=0.9))
    o.append(T(496, 307, "Bund / Bể chắn", 7.4, anchor="start", color=INK))

    o.append(_legend(388))
    o.append(T(340, 412,
               "Hình 3.9 · Bể chứa mái cố định. a = 3 m, b = 1.5 m, c = 2.5 m / "
               "Figure 3.9 · Fixed roof stock tank. a = 3 m, b = 1.5 m, c = 2.5 m",
               7.0, color=INK))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt bể chứa mái cố định: không gian hơi Vùng 0 dạng lưới ô "
                    "vuông, nắp Vùng 1 ô chéo chữ X quanh ống thông hơi và trong bể "
                    "chắn, vùng Vùng 2 gạch chéo đơn bao quanh")),
                "Hình 3.9 · Bể chứa mái cố định. a = 3 m, b = 1.5 m, c = 2.5 m",
                "Figure 3.9 · Fixed roof stock tank. a = 3 m, b = 1.5 m, c = 2.5 m",
                "Mặt cắt bể chứa mái cố định: không gian hơi Vùng 0 dạng lưới ô vuông, "
                "nắp Vùng 1 ô chéo chữ X quanh ống thông hơi và bên trong bể chắn, "
                "vùng Vùng 2 gạch chéo đơn bao quanh; a = 3 m, b = 1.5 m, c = 2.5 m.",
                "Cross-section of a fixed roof stock tank: square-grid Zone 0 vapour "
                "space, crosshatched Zone 1 cap around the vent and inside the bund, "
                "single-diagonal Zone 2 outside; a = 3 m, b = 1.5 m, c = 2.5 m.")


@_reg
def fig_f310():
    """Figure 3.10 - Floating roof stock tank."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_rect(0, 0, w, h, fill=PAPER, sw=0))
    o.append(T(340, 20, "Hình 3.10 · Bể chứa mái nổi / "
                        "Figure 3.10 · Floating roof stock tank",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34, "A = 1.5 m, B = 2.5 m", 7.4, color=GREY))

    # Zone 2: single-diagonal lobes outside the tank and bund.
    outer = ("M270,205 L222,205 L222,262 Q222,288 192,300 L156,300 "
             "Q130,300 130,326 L130,330 L550,330 L550,326 "
             "Q550,300 524,300 L488,300 Q458,288 458,262 "
             "L458,205 L410,205 L410,330 L270,330 Z")
    o.append(_hatch_fill(outer, ("url(#h6)",), sw=1.4))

    # Tank body with dashed liquid; there is no Zone 0 hatch.
    o.append(_rect(270, 205, 140, 125, fill=PAPER, sw=1.5))
    o.append(_liquid(271, 212, 138, 116))

    # Zone 1: crosshatched space above the floating roof.
    cap = ("M250,205 L250,142 Q250,120 272,120 L408,120 "
           "Q430,120 430,142 L430,205 Z")
    o.append(_hatch_fill(cap, ("url(#h6)", "url(#h7)"), sw=1.4))

    # Zone 1: bund interior either side of the tank.
    o.append(_hatch_fill("M230,298 H270 V330 H230 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.1))
    o.append(_hatch_fill("M410,298 H450 V330 H410 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.1))
    o.append(_rect(226, 286, 4, 44, fill=PAPER, sw=1.2))
    o.append(_rect(450, 286, 4, 44, fill=PAPER, sw=1.2))

    # Floating roof at the liquid surface, its thin rim and the seals.
    o.append(_line(268, 205, 412, 205, sw=2.4))
    o.append(_line(270, 198, 270, 212, sw=1.2))
    o.append(_line(410, 198, 410, 212, sw=1.2))
    o.append(_line(272, 202, 272, 208, sw=1.0))
    o.append(_line(408, 202, 408, 208, sw=1.0))

    o.append(_line(126, 330, 554, 330, sw=1.8))

    # Bilingual leaders.
    o.append(_line(230, 184, 272, 204, sw=0.9))
    o.append(T(226, 187, "Seal / Phớt làm kín", 7.4,
               anchor="end", color=INK))
    o.append(_line(466, 162, 412, 203, sw=0.9))
    o.append(T(470, 165, "Floating roof / Mái nổi", 7.4,
               anchor="start", color=INK))
    o.append(_line(452, 318, 490, 306, sw=0.9))
    o.append(T(494, 309, "Bund / Bể chắn", 7.4, anchor="start", color=INK))
    o.append(T(340, 258, "Chất lỏng / Liquid", 7.2, color=GREY))

    # Printed dimension arrows.
    o.append(_arrow(394, 158, 420, 130, sw=1.0))
    o.append(T(390, 162, "A", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(500, 300, 534, 268, sw=1.0))
    o.append(T(496, 306, "B", 8.4, anchor="end", color=INK, weight="600"))

    o.append(_legend(388))
    o.append(T(340, 412,
               "Hình 3.10 · Bể chứa mái nổi. A = 1.5 m, B = 2.5 m / "
               "Figure 3.10 · Floating roof stock tank. A = 1.5 m, B = 2.5 m",
               7.0, color=INK))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt bể chứa mái nổi: chất lỏng có nét gạch ngang, mái nổi "
                    "và phớt làm kín; Vùng 1 ô chéo chữ X phía trên mái và trong bể "
                    "chắn, không có Vùng 0; Vùng 2 gạch chéo đơn bên ngoài")),
                "Hình 3.10 · Bể chứa mái nổi. A = 1.5 m, B = 2.5 m",
                "Figure 3.10 · Floating roof stock tank. A = 1.5 m, B = 2.5 m",
                "Mặt cắt bể chứa mái nổi: chất lỏng dạng nét gạch ngang, mái nổi và "
                "phớt làm kín ở hai bên; Vùng 1 ô chéo chữ X phía trên mái và trong "
                "bể chắn, không có Vùng 0; Vùng 2 gạch chéo đơn bao quanh; "
                "A = 1.5 m, B = 2.5 m.",
                "Cross-section of a floating roof stock tank: dash-hatched liquid, "
                "floating roof and side seals; crosshatched Zone 1 above the roof "
                "and inside the bund with no Zone 0; single-diagonal Zone 2 outside; "
                "A = 1.5 m, B = 2.5 m.")


@_reg
def fig_f311():
    """Figure 3.11 - Water sealed gas storage tank."""
    w, h = 680, 500
    o = [_defs()]
    o.append(_rect(0, 0, w, h, fill=PAPER, sw=0))
    o.append(T(340, 20, "Hình 3.11 · Bể chứa khí bịt kín bằng nước / "
                        "Figure 3.11 · Water sealed gas storage tank",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34, "A = 3 m, B = 10 m, C = 7 m", 7.4, color=GREY))

    # Outer Zone 2: large dome with rounded side flares, single diagonal.
    big = ("M230,360 L230,300 Q230,270 258,258 "
           "Q272,175 340,146 Q408,116 476,146 "
           "Q544,175 558,258 Q586,270 586,300 "
           "L586,360 Z")
    o.append(_hatch_fill(big, ("url(#h6)",), sw=1.4))

    # Gas-holder body sitting in the water basin.
    o.append(_rect(340, 278, 136, 82, fill=PAPER, sw=1.6))
    o.append(_line(340, 278, 476, 278, sw=2.0))

    # Nested inner hazard zone around the relief valve: opposite diagonal.
    cap = "M358,278 A50,52 0 0 1 458,278 Z"
    o.append(_hatch_fill(cap, ("url(#h7)",), sw=1.3))

    # Water basin with dash-hatched water and side water seals.
    o.append(_rect(330, 360, 156, 80, fill=PAPER, sw=1.2))
    o.append(_liquid(336, 366, 144, 70))
    o.append(_line(330, 440, 486, 440, sw=1.6))

    # Pressure relief valve symbol at the top centre.
    o.append(_line(408, 278, 408, 254, sw=1.4))
    o.append(_poly([(398, 254), (418, 254), (408, 244)],
                   fill=PAPER, sw=1.2, close=True))
    o.append(_line(396, 254, 420, 254, sw=1.2))

    # Bilingual leaders.
    o.append(_line(348, 184, 402, 250, sw=0.9))
    o.append(T(344, 187, "Pressure relief valve / Van xả áp", 7.4,
               anchor="end", color=INK))
    o.append(_line(320, 376, 342, 362, sw=0.9))
    o.append(T(316, 379, "Water seal / Gioăng nước", 7.2,
               anchor="end", color=INK))
    o.append(_line(492, 376, 474, 362, sw=0.9))
    o.append(T(496, 379, "Water seal / Gioăng nước", 7.2,
               anchor="start", color=INK))
    o.append(T(408, 412, "Nước / Water", 8.0, color=INK))

    # Printed dimension arrows.
    o.append(_arrow(360, 180, 338, 150, sw=1.0))
    o.append(T(364, 184, "C", 8.4, anchor="start", color=INK, weight="600"))
    o.append(_arrow(398, 244, 420, 232, sw=1.0))
    o.append(T(394, 248, "A", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(516, 330, 550, 298, sw=1.0))
    o.append(T(512, 336, "B", 8.4, anchor="end", color=INK, weight="600"))

    o.append(_legend(464))
    o.append(T(340, 484,
               "Hình 3.11 · Bể chứa khí bịt kín bằng nước. A = 3 m, B = 10 m, C = 7 m / "
               "Figure 3.11 · Water sealed gas storage tank. A = 3 m, B = 10 m, C = 7 m",
               7.0, color=INK))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt bể chứa khí bịt kín bằng nước: thân bể đặt trong bể nước "
                    "có nét gạch ngang, van xả áp ở đỉnh, gioăng nước ở hai bên, "
                    "hai vùng gạch chéo đơn xếp chồng")),
                "Hình 3.11 · Bể chứa khí bịt kín bằng nước. A = 3 m, B = 10 m, C = 7 m",
                "Figure 3.11 · Water sealed gas storage tank. A = 3 m, B = 10 m, C = 7 m",
                "Mặt cắt bể chứa khí bịt kín bằng nước: thân bể đặt trong bể nước có "
                "nét gạch ngang, van xả áp ở đỉnh, gioăng nước ở chân hai bên, hai "
                "vùng nguy hiểm gạch chéo đơn xếp chồng quanh van và toàn bể; "
                "A = 3 m, B = 10 m, C = 7 m.",
                "Cross-section of a water-sealed gas holder: holder body standing in "
                "a dash-hatched water basin, pressure relief valve at the top, water "
                "seals at both sides and nested single-diagonal hazard zones; "
                "A = 3 m, B = 10 m, C = 7 m.")
