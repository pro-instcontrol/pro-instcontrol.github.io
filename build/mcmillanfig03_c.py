# -*- coding: utf-8 -*-
"""Vector redraws of Figures 3.12, 3.13 and 3.14 in A. McMillan,
*Electrical Installations in Hazardous Areas*, Chapter 3
"Area classification practice for gases, vapours and mists in freely
ventilated situations".

The printed hatch conventions are preserved: square grid = Zone 0,
crosshatch = Zone 1 and single diagonal = Zone 2; liquid is drawn as short
horizontal dashes.  Captions and dimension letters are taken from the page
renders, since the PDF text layer garbles them.

Architecture mirrors `mcmillanfig02_a.py`: each function returns the
standard five-tuple through `vfig._fig()` and is registered in `FIGS` by
the `_reg` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _defs, _fig,
                  _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape all XML-significant characters in displayed text."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.0, **kw):
    """Text helper: escape first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# --------------------------------------------------------------- primitives
def _grid(x, y, w, h, step=9, color="#9a9a9a", sw=0.6):
    """Zone 0: square-grid hatch drawn as crossing straight lines."""
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


def _capsule(cx, top, bottom, width, patterns, sw=1.3):
    """Vertically elongated capsule with semicircular ends."""
    r = width / 2.0
    ty, by = top + r, bottom - r
    d = ("M %s %s A %s %s 0 0 1 %s %s L %s %s A %s %s 0 0 1 %s %s Z"
         % (cx - r, ty, r, r, cx + r, ty, cx + r, by, r, r, cx - r, by))
    return _hatch_fill(d, patterns, sw=sw)


_LEGEND = ("Vùng 0 = lưới ô vuông / Zone 0 = square grid;  "
           "Vùng 1 = ô chéo chữ X / Zone 1 = crosshatch;  "
           "Vùng 2 = gạch chéo đơn / Zone 2 = single diagonal")


def _legend(y):
    return T(340, y, _LEGEND, 6.6, color=GREY)


# ------------------------------------------------------------------- figures
@_reg
def fig_f312():
    """Figure 3.12 - Loading and off-loading of road/rail tankers."""
    w, h = 680, 556
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.12 · Bốc và dỡ xe bồn đường bộ/đường sắt / "
               "Figure 3.12 · Loading and off-loading of road/rail tankers",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "Mặt bằng phía trên và mặt cắt phía dưới / "
               "Top plan above and bottom elevation below",
               6.8, color=GREY))

    # ---- Top plan: irregular single-diagonal Zone 2 boundary.
    outer = ("M180,150 C170,120 190,96 214,98 C228,68 262,62 282,74 "
             "C312,52 352,58 366,76 C402,54 442,58 458,82 "
             "C492,72 516,92 510,118 C532,140 528,172 506,184 "
             "C520,216 494,244 466,236 C442,256 404,254 388,236 "
             "C356,258 318,252 306,232 C274,248 238,236 232,212 "
             "C202,214 178,190 186,166 Z")
    o.append(_hatch_fill(outer, ("url(#h6)",), sw=1.4))

    # Cab at the left of the tanker.
    o.append(_rect(198, 120, 34, 42, fill=PAPER, sw=1.2))
    o.append(_path("M198,120 Q186,141 198,162", fill="none", sw=1.0))
    o.append(_line(216, 120, 216, 162, sw=1.0))

    # Tanker body: crosshatched Zone 1 with four vent circles.
    body = ("M250,96 H452 Q470,96 470,114 V164 Q470,182 452,182 "
            "H250 Q232,182 232,164 V114 Q232,96 250,96 Z")
    o.append(_hatch_fill(body, ("url(#h6)", "url(#h7)"), sw=1.4))
    for vx in (270, 332, 394, 446):
        o.append(_circle(vx, 124, 6, fill=PAPER, sw=1.0))

    # Dotted phi boundary: Zone 1 limit for the off-loading operation.
    o.append(_rect(352, 146, 118, 46, fill="none", sw=1.0,
                   dash="2 3", stroke=GREY))
    o.append(T(358, 142, "φ", 7.4, anchor="middle", color=GREY))
    o.append(T(462, 200, "φ", 7.4, anchor="middle", color=GREY))

    # Coupling and its bilingual leader.
    o.append(_rect(452, 160, 18, 12, fill=PAPER, sw=1.1))
    o.append(_line(470, 166, 506, 166, sw=0.9))
    o.append(T(510, 158, "Loading/", 7.2, anchor="start", color=INK))
    o.append(T(510, 170, "unloading", 7.2, anchor="start", color=INK))
    o.append(T(510, 182, "connections", 7.2, anchor="start", color=INK))

    # Flexible pipe below the connections, and the fixed pipes beneath.
    o.append(_hatch_fill("M438,182 H470 V232 H438 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.2))
    o.append(_poly([(454, 188), (448, 194), (460, 200), (448, 206),
                    (460, 212), (448, 218), (454, 226)],
                   fill="none", sw=0.9))
    o.append(T(478, 204, "Flexible", 7.2, anchor="start", color=INK))
    o.append(T(478, 216, "pipe / Ống mềm", 7.0, anchor="start", color=INK))
    o.append(_rect(418, 230, 52, 6, fill=PAPER, sw=1.0))
    o.append(_line(418, 233, 388, 246, sw=0.9))
    o.append(T(384, 250, "Fixed pipes / Ống cố định", 7.0,
               anchor="end", color=INK))

    # Dimension a at the top edge of the tanker.
    o.append(_arrow(254, 78, 254, 96, sw=1.0))
    o.append(T(260, 92, "a", 8.4, anchor="start", color=INK, weight="600"))
    o.append(T(340, 266, "Mặt bằng / Plan", 7.4, color=GREY))

    # ---- Bottom elevation: ground line, wavy Zone 2 band below it.
    band = ("M146,352 C180,348 210,354 240,352 C280,348 320,354 360,352 "
            "C400,348 440,354 474,350 L486,404 "
            "C452,412 420,404 392,410 C356,416 320,406 286,412 "
            "C250,418 216,406 182,410 C164,412 148,406 144,394 Z")
    o.append(_hatch_fill(band, ("url(#h6)",), sw=1.3))
    o.append(_line(120, 352, 560, 352, sw=1.5))

    # Crosshatched Zone 1 around the tank, coupling and the cab at left.
    halo = ("M262,352 L262,318 Q262,286 340,282 Q418,286 418,318 L418,352 Z")
    o.append(_hatch_fill(halo, ("url(#h6)",), sw=1.2))
    dome = ("M272,352 L272,320 Q272,294 340,290 Q408,294 408,320 L408,352 Z")
    o.append(_hatch_fill(dome, ("url(#h6)", "url(#h7)"), sw=1.3))
    o.append(_hatch_fill("M228,330 H412 V366 H228 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.3))
    o.append(_rect(186, 340, 42, 26, fill=PAPER, sw=1.2))
    o.append(_line(198, 340, 198, 366, sw=0.9))
    o.append(_hatch_fill("M320,366 H360 V392 H320 Z",
                         ("url(#h6)", "url(#h7)"), sw=1.2))
    o.append(_rect(300, 338, 80, 54, fill="none", sw=1.0,
                   dash="2 3", stroke=GREY))
    o.append(T(306, 334, "φ", 7.4, anchor="middle", color=GREY))
    o.append(T(374, 398, "φ", 7.4, anchor="middle", color=GREY))

    # Dimensions b and c.
    o.append(_arrow(500, 346, 500, 310, sw=1.0, head="a7"))
    o.append(_arrow(500, 310, 500, 346, sw=1.0, head="a7"))
    o.append(T(508, 334, "b", 8.4, anchor="start", color=INK, weight="600"))
    o.append(_line(340, 414, 340, 428, sw=0.8, color=GREY))
    o.append(_arrow(340, 424, 556, 424, sw=1.0))
    o.append(T(448, 419, "c", 8.4, color=INK, weight="600"))
    o.append(T(120, 440, "Mặt cắt / Elevation", 7.4,
               anchor="start", color=GREY))

    # Printed key, with a separate Vietnamese gloss for the grouped entries.
    o.append(T(92, 456, "a = 1.5 m", 7.6, anchor="start", color=INK))
    o.append(T(92, 468,
               "b = } These depend upon the characteristics of the pool formed by",
               7.2, anchor="start", color=INK))
    o.append(T(92, 480, "c = } any liquid release", 7.2,
               anchor="start", color=INK))
    o.append(T(92, 492, "φ = Limit of Zone 1 for off-loading operation", 7.2,
               anchor="start", color=INK))
    o.append(T(92, 504,
               "b, c = phụ thuộc vào đặc tính của vũng chất lỏng rò rỉ", 6.8,
               anchor="start", color=GREY))
    o.append(_legend(522))
    o.append(T(340, 542,
               "Hình 3.12 · Bốc và dỡ xe bồn đường bộ/đường sắt / "
               "Figure 3.12 · Loading and off-loading of road/rail tankers",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt bằng và mặt cắt xe bồn: thân xe ô chéo chữ X có bốn nắp "
                    "thông hơi, cabin bên trái, đầu nối và ống mềm/ống cố định, "
                    "đường chấm giới hạn Vùng 1 khi dỡ hàng, vùng Vùng 2 gạch "
                    "chéo đơn bao quanh và các kích thước a, b, c")),
                "Hình 3.12 · Bốc và dỡ xe bồn đường bộ/đường sắt",
                "Figure 3.12 · Loading and off-loading of road/rail tankers",
                "Mặt bằng: thân xe bồn ô chéo chữ X có bốn nắp thông hơi, cabin bên "
                "trái, đầu nối có nhãn Loading/unloading connections, ống mềm và "
                "ống cố định; đường chấm φ là giới hạn Vùng 1 khi dỡ hàng; a = 1.5 m; "
                "vùng Vùng 2 gạch chéo đơn bao quanh. Mặt cắt: Vùng 1 ô chéo quanh "
                "bình và đầu nối xuống mặt đất, vùng Vùng 2 gạch chéo đơn, b và c "
                "phụ thuộc vào đặc tính vũng chất lỏng rò rỉ.",
                "Plan: a crosshatched tanker body with four vents, a cab at left, "
                "loading/unloading connections, a flexible pipe and fixed pipes; "
                "the dotted phi line is the Zone 1 off-loading limit; a = 1.5 m; "
                "an irregular single-diagonal Zone 2 surrounds the tanker. "
                "Elevation: crosshatched Zone 1 around the tank and couplings down "
                "to ground inside Zone 2; b and c depend on the characteristics of "
                "the pool formed by any liquid release.")


@_reg
def fig_f313():
    """Figure 3.13 - Oil/water separator."""
    w, h = 680, 578
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.13 · Bể tách dầu/nước / Figure 3.13 · Oil/water separator",
               9.2, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = cột 50% của Bảng 3.7, b = cột >90% của Bảng 3.7 / "
               "a = 50% column of Table 3.7, b = >90% column of Table 3.7",
               6.8, color=GREY))

    # ---- Plan: three nested rounded squares.
    outer = ("M249,60 H431 Q465,60 465,94 V276 Q465,310 431,310 "
             "H249 Q215,310 215,276 V94 Q215,60 249,60 Z")
    o.append(_hatch_fill(outer, ("url(#h6)",), sw=1.4))
    inner = ("M262,85 H418 Q440,85 440,107 V263 Q440,285 418,285 "
             "H262 Q240,285 240,263 V107 Q240,85 262,85 Z")
    o.append(_hatch_fill(inner, ("url(#h6)", "url(#h7)"), sw=1.4))
    o.append(_rect(268, 112, 144, 146, fill=PAPER, sw=1.2))
    o.append(_grid(269, 113, 142, 144, step=9))

    # Printed corner arrows a and b.
    o.append(_arrow(255, 102, 228, 75, sw=1.0))
    o.append(T(220, 98, "b", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(414, 100, 436, 84, sw=1.0))
    o.append(T(442, 96, "a", 8.4, anchor="start", color=INK, weight="600"))
    o.append(T(340, 326, "Mặt bằng / Plan", 7.4, color=GREY))

    # ---- Elevation: domed Zone 2 above ground, nested bands at the rim.
    dome = ("M190,404 L190,382 Q190,352 340,348 Q490,352 490,382 L490,404 Z")
    o.append(_hatch_fill(dome, ("url(#h6)",), sw=1.4))
    cap = ("M262,404 L262,384 Q262,370 340,368 Q418,370 418,384 L418,404 Z")
    o.append(_hatch_fill(cap, ("url(#h6)", "url(#h7)"), sw=1.4))
    o.append(_line(140, 404, 540, 404, sw=1.5))

    # Separator body: Zone 0 grid above and below ground; liquid in the pit.
    o.append(_rect(284, 380, 112, 120, fill=PAPER, sw=1.2))
    o.append(_grid(285, 381, 110, 118, step=9))
    o.append(_liquid(286, 440, 108, 58))
    o.append(T(340, 470, "Liquid / Chất lỏng", 7.2, color=INK))

    o.append(_arrow(232, 382, 208, 360, sw=1.0))
    o.append(T(200, 382, "b", 8.4, anchor="end", color=INK, weight="600"))
    o.append(_arrow(396, 380, 414, 370, sw=1.0))
    o.append(T(422, 386, "a", 8.4, anchor="start", color=INK, weight="600"))
    o.append(T(340, 520, "Mặt cắt / Elevation", 7.4, color=GREY))
    o.append(_legend(540))
    o.append(T(340, 562,
               "Hình 3.13 · Bể tách dầu/nước. a = cột 50% của Bảng 3.7, "
               "b = cột >90% của Bảng 3.7 / Figure 3.13 · Oil/water separator. "
               "a = 50% column of Table 3.7, b = >90% column of Table 3.7",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt bằng và mặt cắt bể tách dầu/nước: lưới ô vuông Vùng 0 ở "
                    "giữa, dải ô chéo chữ X Vùng 1 quanh bể với mũi tên a, dải "
                    "gạch chéo đơn Vùng 2 ngoài cùng với mũi tên b, và hố chứa "
                    "chất lỏng có nét gạch ngang phía dưới mặt đất")),
                "Hình 3.13 · Bể tách dầu/nước. a = cột 50% của Bảng 3.7, "
                "b = cột >90% của Bảng 3.7",
                "Figure 3.13 · Oil/water separator. a = 50% column of Table 3.7, "
                "b = >90% column of Table 3.7",
                "Mặt bằng: ba hình vuông bo góc xếp lồng nhau; Vùng 0 lưới ô vuông "
                "ở giữa, Vùng 1 ô chéo chữ X có mũi tên a, Vùng 2 gạch chéo đơn có "
                "mũi tên b. Mặt cắt: cùng các vùng xếp lồng nhau trên mặt đất, với "
                "hố ngầm chứa chất lỏng có nét gạch ngang.",
                "Plan: three nested rounded squares; a square-grid Zone 0 centre, "
                "a crosshatched Zone 1 band marked a and an outer single-diagonal "
                "Zone 2 band marked b. Elevation: the same nested bands above "
                "ground with an underground pit containing dash-hatched liquid.")


@_reg
def fig_f314():
    """Figure 3.14 - Open drains."""
    w, h = 680, 580
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.14 · Cống hở / Figure 3.14 · Open drains",
               9.6, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = 1 m · Vùng 1 ô chéo chữ X quanh cống / "
               "a = 1 m · crosshatched Zone 1 around the drain",
               6.8, color=GREY))

    # ---- Section: crosshatched semicircular dome above the ground line.
    dome = ("M260,150 L260,124 Q260,70 340,70 Q420,70 420,124 L420,150 Z")
    o.append(_hatch_fill(dome, ("url(#h6)", "url(#h7)"), sw=1.4))
    o.append(_line(80, 150, 500, 150, sw=1.5))
    o.append(_rect(326, 150, 28, 28, fill=PAPER, sw=1.2))
    o.append(_liquid(327, 156, 26, 20, step=9, dash=5))
    o.append(_arrow(470, 76, 470, 144, sw=1.0, head="a7"))
    o.append(_arrow(470, 144, 470, 76, sw=1.0, head="a7"))
    o.append(_line(424, 70, 484, 70, sw=0.8, color=GREY))
    o.append(_line(424, 150, 484, 150, sw=0.8, color=GREY))
    o.append(T(482, 116, "a", 8.6, anchor="start", color=INK, weight="600"))
    o.append(T(340, 198, "Mặt cắt / Section", 7.4, color=GREY))

    # ---- Plan: crosshatched capsule around the square-grid drain strip.
    o.append(_capsule(340, 222, 474, 132,
                      ("url(#h6)", "url(#h7)"), sw=1.4))
    o.append(_rect(328, 252, 24, 192, fill=PAPER, sw=1.2))
    o.append(_grid(329, 253, 22, 190, step=9))
    o.append(_arrow(280, 502, 326, 502, sw=1.0, head="a7"))
    o.append(_arrow(326, 502, 280, 502, sw=1.0, head="a7"))
    o.append(_line(274, 496, 274, 508, sw=0.8, color=GREY))
    o.append(_line(328, 496, 328, 508, sw=0.8, color=GREY))
    o.append(T(302, 518, "a", 8.6, color=INK, weight="600"))
    o.append(_line(408, 446, 460, 446, sw=0.8, color=GREY))
    o.append(_line(408, 472, 460, 472, sw=0.8, color=GREY))
    o.append(_arrow(452, 446, 452, 472, sw=1.0, head="a7"))
    o.append(_arrow(452, 472, 452, 446, sw=1.0, head="a7"))
    o.append(T(462, 466, "a", 8.6, anchor="start", color=INK, weight="600"))
    o.append(T(340, 536, "Mặt bằng / Plan", 7.4, color=GREY))
    o.append(_legend(552))
    o.append(T(340, 570,
               "Hình 3.14 · Cống hở. a = 1 m / "
               "Figure 3.14 · Open drains. a = 1 m",
               7.0, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt và mặt bằng cống hở: mái vòm bán nguyệt ô chéo chữ X "
                    "trên mặt đất, cống nhỏ có nét gạch ngang bên dưới, mặt bằng "
                    "là dải cống lưới ô vuông nằm trong nang ô chéo chữ X, với "
                    "các kích thước a = 1 m")),
                "Hình 3.14 · Cống hở. a = 1 m",
                "Figure 3.14 · Open drains. a = 1 m",
                "Mặt cắt: mái vòm bán nguyệt ô chéo chữ X (Vùng 1) phía trên mặt "
                "đất, cống hở nhỏ có chất lỏng nét gạch ngang bên dưới, kích thước "
                "đứng a = 1 m. Mặt bằng: dải cống lưới ô vuông nằm trong nang ô chéo "
                "chữ X, có kích thước a ở cạnh và ở đầu.",
                "Section: a semicircular crosshatched Zone 1 dome above the ground "
                "line, a narrow drain with dash-hatched liquid below it, and the "
                "vertical dimension a = 1 m. Plan: a square-grid drain strip inside "
                "a crosshatched capsule, with the dimension a marked at the side "
                "and at the end.")
