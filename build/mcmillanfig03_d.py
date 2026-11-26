# -*- coding: utf-8 -*-
"""Vector redraws of Figures 3.15-3.19 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 3 "Area classification practice
for gases, vapours and mists in freely ventilated situations".

Fig. 3.15 shows liquid sampling (normal and abnormal operation), Fig. 3.16
the closed in-line gas-sampling loop, Figs. 3.17 and 3.18 the effect of a
doorway and of a short wall on the extent of a hazardous area, and Fig. 3.19
a release at a vent.  Printed hatch conventions are preserved: square grid
= Zone 0, crosshatch = Zone 1 and single diagonal = Zone 2; liquid is drawn
as short horizontal dashes.  Captions, keys and notes follow the page
renders, since the PDF text layer garbles them (in particular the printed
"value stems" typo in Fig. 3.16 is kept).

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
def _hatch_fill(d, patterns, outline=True, sw=1.3):
    """Opaque base plus one or more overlay hatch patterns on a path."""
    o = [_path(d, fill=PAPER, sw=0)]
    for p in patterns:
        o.append(_path(d, fill=p, sw=0))
    if outline:
        o.append(_path(d, fill="none", sw=sw))
    return "".join(o)


def _hr(x, y, w, h, patterns, sw=1.1):
    """Hatched rectangle, used for the walls in Figs. 3.17 and 3.18."""
    d = "M%s,%s H%s V%s H%s Z" % (x, y, x + w, y + h, x)
    return _hatch_fill(d, patterns, sw=sw)


def _ground(cx, y, half=120):
    """Horizontal ground/base line with short diagonal hatching beneath."""
    o = [_line(cx - half, y, cx + half, y, sw=1.3)]
    x = int(cx - half)
    while x < cx + half - 6:
        o.append(_line(x + 6, y + 6, x, y, sw=0.6, color=GREY))
        x += 9
    return "".join(o)


def _dome(cx, ground, width, height_to_dome, fill="url(#h6)", sw=1.3):
    """Dome-topped area standing on a ground line."""
    r = width / 2.0
    dy = ground - height_to_dome
    d = ("M %s %s L %s %s A %s %s 0 0 1 %s %s L %s %s Z"
         % (cx - r, ground, cx - r, dy, r, r, cx + r, dy, cx + r, ground))
    return _path(d, fill=fill, sw=sw)


def _valve(cx, cy, r=7, cross=False):
    """Bowtie valve symbol, or a circle with an X (cross=True)."""
    o = []
    if cross:
        o.append(_circle(cx, cy, r, fill=PAPER, sw=1.1))
        o.append(_line(cx - r + 1, cy - r + 1, cx + r - 1, cy + r - 1, sw=0.9))
        o.append(_line(cx - r + 1, cy + r - 1, cx + r - 1, cy - r + 1, sw=0.9))
    else:
        o.append(_poly([(cx - r, cy - r), (cx - r, cy + r), (cx, cy)],
                       close=True, fill=PAPER, sw=1.0))
        o.append(_poly([(cx + r, cy - r), (cx + r, cy + r), (cx, cy)],
                       close=True, fill=PAPER, sw=1.0))
    return "".join(o)


def _dv(x, y1, y2, label, size=7.2, color=INK):
    """Vertical double-headed dimension with a label at left."""
    return "".join([
        _line(x - 3, y1, x + 3, y1, sw=0.7, color=GREY),
        _line(x - 3, y2, x + 3, y2, sw=0.7, color=GREY),
        _arrow(x, y1 + 3, x, y2 - 3, sw=0.9, color=GREY, head="a7"),
        _arrow(x, y2 - 3, x, y1 + 3, sw=0.9, color=GREY, head="a7"),
        T(x - 6, (y1 + y2) / 2.0 + 2.4, label, size, anchor="end",
          color=color),
    ])


def _dh(x1, x2, y, label, size=7.4, color=INK):
    """Horizontal double-headed dimension with the label above the line."""
    return "".join([
        _line(x1, y - 3, x1, y + 3, sw=0.7, color=GREY),
        _line(x2, y - 3, x2, y + 3, sw=0.7, color=GREY),
        _arrow(x1 + 3, y, x2 - 3, y, sw=0.9, color=GREY, head="a7"),
        _arrow(x2 - 3, y, x1 + 3, y, sw=0.9, color=GREY, head="a7"),
        T((x1 + x2) / 2.0, y - 5, label, size, color=color, weight="600"),
    ])


_LEGEND = ("Vùng 0 = lưới ô vuông / Zone 0 = square grid;  "
           "Vùng 1 = ô chéo chữ X / Zone 1 = crosshatch;  "
           "Vùng 2 = gạch chéo đơn / Zone 2 = single diagonal")


def _legend(y):
    return T(340, y, _LEGEND, 6.6, color=GREY)


# ------------------------------------------------------------------- figures
@_reg
def fig_f315():
    """Figure 3.15 - Liquid sampling (normal and abnormal operation)."""
    w, h = 680, 560
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.15 · Lấy mẫu chất lỏng / Figure 3.15 · Liquid sampling",
               9.2, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = 1 m, b = vũng chất lỏng, c = Bảng 3.7 / "
               "a = 1 m, b = pool, c = Table 3.7",
               6.8, color=GREY))

    # ---- Upper panel: normal operation, narrow Zone 2 capsule on ground.
    o.append(_dome(250, 250, 80, 135, fill="url(#h6)"))
    o.append(_ground(250, 250, 150))
    o.append(_dv(232, 100, 126, "a"))
    o.append(T(170, 150, "a = 1 m", 7.4, anchor="start", color=INK))
    # Sampling pipe, valve, sample arrow and tundish.
    o.append(_line(250, 92, 250, 166, sw=1.2))
    o.append(_valve(250, 128, r=7))
    o.append(T(264, 132, "Valve", 7.2, anchor="start", color=INK))
    o.append(_arrow(340, 95, 272, 95, sw=1.0))
    o.append(T(346, 99, "Sample", 7.2, anchor="start", color=INK))
    o.append(_poly([(232, 164), (268, 164), (250, 184)],
                   close=True, fill=PAPER, sw=1.1))
    o.append(_line(230, 162, 270, 162, sw=1.0))
    o.append(_path("M250,184 Q250,206 272,206 L344,206",
                   fill="none", sw=1.0))
    o.append(_arrow(344, 206, 372, 206, sw=1.0))
    o.append(T(378, 210, "To collector", 7.0, anchor="start", color=INK))
    o.append(T(250, 272, "Mặt cắt · Thường / Normal operation", 7.0,
               color=GREY))

    # ---- Lower panel: abnormal operation, wide Zone 2 zone down to ground.
    zone = "M150,470 L200,350 A50,50 0 0 1 300,350 L440,470 Z"
    o.append(_hatch_fill(zone, ("url(#h6)",), sw=1.4))
    o.append(_ground(295, 470, 165))
    o.append(_arrow(232, 316, 232, 338, sw=0.9, color=GREY, head="a7"))
    o.append(T(224, 332, "a", 8.0, anchor="end", color=INK, weight="600"))
    o.append(_line(250, 322, 250, 384, sw=1.2))
    o.append(_valve(250, 356, r=7))
    o.append(T(264, 360, "Valve", 7.2, anchor="start", color=INK))
    o.append(_arrow(350, 332, 272, 332, sw=1.0))
    o.append(T(356, 336, "Sample", 7.2, anchor="start", color=INK))
    o.append(_poly([(232, 384), (268, 384), (250, 404)],
                   close=True, fill=PAPER, sw=1.1))
    o.append(_line(230, 382, 270, 382, sw=1.0))
    o.append(_path("M250,404 Q250,426 276,426 L394,426",
                   fill="none", sw=1.0))
    o.append(_arrow(394, 426, 422, 426, sw=1.0))
    o.append(T(428, 430, "To collector", 7.0, anchor="start", color=INK))
    # Printed key beside the lower panel.
    o.append(T(66, 340, "a = 1 m", 7.4, anchor="start", color=INK))
    o.append(T(66, 354, "b = pool", 7.4, anchor="start", color=INK))
    o.append(T(66, 368, "c = Table 3.7", 7.4, anchor="start", color=INK))
    o.append(_dh(150, 394, 496, "b"))
    o.append(_arrow(418, 466, 438, 466, sw=0.9, color=GREY, head="a7"))
    o.append(T(444, 470, "c", 8.0, anchor="start", color=INK, weight="600"))
    o.append(T(340, 518, "Mặt cắt · Bất thường / Abnormal operation", 7.0,
               color=GREY))
    o.append(T(340, 546,
               "Hình 3.15 · Lấy mẫu chất lỏng. a = 1 m, "
               "b = vũng chất lỏng, c = Bảng 3.7 / Figure 3.15 · Liquid "
               "sampling. a = 1 m, b = pool, c = Table 3.7", 6.4,
               color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Sơ đồ lấy mẫu chất lỏng: panel trên vùng Vùng 2 gạch chéo "
                    "đơn quanh van và phễu rót vào dây dẫn tới bình thu mẫu; "
                    "panel dưới vùng gạch chéo đơn rộng ra đến mặt đất với "
                    "các kích thước a, b, c")),
                "Hình 3.15 · Lấy mẫu chất lỏng. a = 1 m, "
                "b = vũng chất lỏng, c = Bảng 3.7",
                "Figure 3.15 · Liquid sampling. a = 1 m, b = pool, "
                "c = Table 3.7",
                "Panel trên: ống lấy mẫu đứng đứng có van và phễu, dòng Sample "
                "từ bên phải, đường dẫn To collector, vùng Vùng 2 gạch chéo đơn "
                "hình nang đứng trên mặt đất, a = 1 m. Panel dưới: vùng Vùng 2 "
                "hình thang xảy ra bất thường, kích thước b dưới mặt đất và c ở "
                "cạnh phải; chú thích a = 1 m, b = pool, c = Table 3.7.",
                "Upper panel: a vertical sample pipe with a valve and tundish, "
                "a Sample arrow from the right, a bent line to the collector "
                "and a narrow single-diagonal Zone 2 capsule on the ground; "
                "a = 1 m. Lower panel: a wider single-diagonal Zone 2 area "
                "reaching the ground, with b along the ground and c at the "
                "right edge; key a = 1 m, b = pool, c = Table 3.7.")


@_reg
def fig_f316():
    """Figure 3.16 - Gas sampling (closed in-line sampling system)."""
    w, h = 680, 468
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.16 · Lấy mẫu khí / Figure 3.16 · Gas sampling",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = Bảng 3.2 cho các mối nối thích hợp / "
               "a = Table 3.2 for appropriate joints",
               6.8, color=GREY))

    # Single-diagonal Zone 2 band enclosing the whole sampling system.
    outer = ("M155,95 H525 Q570,95 570,140 V265 Q570,310 525,310 "
             "H155 Q110,310 110,265 V140 Q110,95 155,95 Z")
    o.append(_hatch_fill(outer, ("url(#h6)",), sw=1.4))

    # Horizontal process line with joint ticks and inline valve symbols.
    o.append(_rect(155, 186, 370, 10, fill=PAPER, sw=1.1))
    for jx in (210, 285, 430, 505):
        o.append(_rect(jx - 2, 181, 4, 20, fill=PAPER, sw=1.0))
    o.append(_valve(350, 191, r=8, cross=True))
    o.append(_valve(455, 191, r=7))
    o.append(T(330, 78, "Fixed valves", 7.2, color=INK))
    o.append(_line(330, 82, 348, 170, sw=0.8, color=GREY))
    o.append(T(520, 78, "Joints", 7.2, color=INK))
    o.append(_line(518, 82, 505, 178, sw=0.8, color=GREY))

    # Closed loops at both ends, down through valve pairs to the bottle.
    o.append(_path("M155,196 L155,250 Q155,268 176,272 L250,284",
                   fill="none", sw=1.1))
    o.append(_path("M525,196 L525,250 Q525,268 504,272 L430,284",
                   fill="none", sw=1.1))
    for vx in (215, 238):
        o.append(_valve(155, vx, r=6))
        o.append(_valve(525, vx, r=6))
    o.append(_rect(250, 282, 180, 30, fill=PAPER, sw=1.2))
    o.append(T(340, 326, "Sample bottle / Chai mẫu", 7.0, color=INK))
    o.append(_line(525, 238, 568, 246, sw=0.8, color=GREY))
    o.append(T(574, 250, "Sample bottle", 7.0, anchor="start", color=INK))
    o.append(T(574, 261, "valves", 7.0, anchor="start", color=INK))

    # Printed a arrows at the left end, right end and lower left.
    o.append(_arrow(118, 191, 140, 191, sw=1.0, head="a7"))
    o.append(T(110, 195, "a", 8.2, anchor="end", color=INK, weight="600"))
    o.append(_arrow(562, 191, 540, 191, sw=1.0, head="a7"))
    o.append(T(570, 195, "a", 8.2, anchor="start", color=INK, weight="600"))
    o.append(_arrow(118, 280, 140, 290, sw=1.0, head="a7"))
    o.append(T(110, 292, "a", 8.2, anchor="end", color=INK, weight="600"))

    o.append(_legend(348))
    # Printed note, kept verbatim (including the "value stems" typo).
    o.append(T(60, 370, "Note: Release from value stems assumed less than "
                        "joints. If this is not so", 6.6,
               anchor="start", color=INK))
    o.append(T(60, 382, "the hazardous area should be adjusted to take "
                        "account of hazardous areas", 6.6,
               anchor="start", color=INK))
    o.append(T(60, 394, "from column 3 of Table 3.2", 6.6,
               anchor="start", color=INK))
    o.append(T(60, 410, "Lưu ý: Giả thiết rò rỉ từ thân van nhỏ hơn mối nối; "
                        "nếu không, điều chỉnh khu vực nguy hiểm", 6.4,
               anchor="start", color=GREY))
    o.append(T(60, 422, "để tính đến các khu vực nguy hiểm từ cột 3 của "
                        "Bảng 3.2", 6.4, anchor="start", color=GREY))
    o.append(T(340, 454,
               "Hình 3.16 · Lấy mẫu khí. a = Bảng 3.2 cho các mối nối thích "
               "hợp / Figure 3.16 · Gas sampling. a = Table 3.2 for "
               "appropriate joints", 6.2, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Sơ đồ mặt bằng hệ thống lấy mẫu khí kín: đường ống ngang "
                    "có các van và mối nối, hai vòng ống ở hai đầu đi qua cặp "
                    "van xuống chai mẫu, toàn bộ nằm trong dải Vùng 2 gạch "
                    "chéo đơn với các mũi tên a")),
                "Hình 3.16 · Lấy mẫu khí. a = Bảng 3.2 cho các mối nối "
                "thích hợp. Lưu ý: Giả thiết sự rò rỉ từ thân van nhỏ hơn mối "
                "nối. Nếu không đúng như vậy, khu vực nguy hiểm phải được "
                "điều chỉnh để tính đến các khu vực nguy hiểm từ cột 3 của "
                "Bảng 3.2",
                "Figure 3.16 · Gas sampling. a = Table 3.2 for appropriate "
                "joints. Note: Release from value stems assumed less than "
                "joints. If this is not so the hazardous area should be "
                "adjusted to take account of hazardous areas from column 3 "
                "of Table 3.2",
                "Mặt bằng: đường ống ngang có các van và các vết mối nối, có "
                "nhãn Fixed valves và Joints; hai vòng ống đầu xuống qua cặp "
                "van đến chai mẫu có nhãn Sample bottle valves; dải Vùng 2 "
                "gạch chéo đơn bao quanh, có mũi tên a ở đầu trái, đầu phải "
                "và góc trái dưới.",
                "Plan: a horizontal process line with valve symbols and joint "
                "ticks labelled Fixed valves and Joints; closed loops at both "
                "ends descend through valve pairs to a Sample bottle; "
                "everything sits in a single-diagonal Zone 2 band with a "
                "arrows at the left end, right end and lower left.")


@_reg
def fig_f317():
    """Figure 3.17 - Openings between spaces (wall with a door)."""
    w, h = 680, 580
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.17 · Lỗ hổng giữa các không gian / "
               "Figure 3.17 · Openings between spaces",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = Khoảng cách từ tường đến nguồn nguy hiểm, "
               "b = Phạm vi không có tường, c = b - a / "
               "a = Distance of wall from source of hazard, "
               "b = Extent of hazardous area ignoring wall, c = b - a",
               6.2, color=GREY))

    # ---- Upper plan view: the zone pushes through the door in the wall.
    lower = ("M205,182 L205,238 Q205,268 250,266 Q300,264 340,268 "
             "Q380,264 430,266 Q475,268 475,238 L475,182 Z")
    o.append(_hatch_fill(lower, ("url(#h6)",), sw=1.4))
    cap = ("M282,182 L282,152 Q282,112 340,112 Q398,112 398,152 "
           "L398,182 Z")
    o.append(_hatch_fill(cap, ("url(#h6)",), sw=1.4))
    o.append(_hr(170, 170, 148, 12, ("url(#h7)",), sw=1.0))
    o.append(_hr(362, 170, 148, 12, ("url(#h7)",), sw=1.0))
    o.append(T(520, 166, "Wall / Tường", 7.0, anchor="start", color=INK))
    o.append(_line(510, 174, 516, 171, sw=0.8, color=GREY))
    o.append(_line(340, 188, 340, 182, sw=0.8, color=GREY))
    o.append(T(340, 200, "Door / Cửa", 7.0, color=INK))
    o.append(_circle(340, 235, 2.8, fill=INK, sw=0))
    o.append(T(352, 232, "Source of", 6.8, anchor="start", color=INK))
    o.append(T(352, 241, "hazard", 6.8, anchor="start", color=INK))
    o.append(_arrow(300, 126, 272, 148, sw=1.0, head="a7"))
    o.append(T(264, 142, "c", 8.2, anchor="end", color=INK, weight="600"))
    o.append(_arrow(340, 230, 340, 186, sw=1.0, head="a7"))
    o.append(T(334, 212, "a", 8.2, anchor="end", color=INK, weight="600"))
    o.append(_arrow(336, 239, 228, 258, sw=1.0, head="a7"))
    o.append(T(276, 260, "b", 8.2, color=INK, weight="600"))
    o.append(T(340, 292, "Mặt bằng / Plan", 7.2, color=GREY))

    # ---- Lower elevation view: the zone wraps over the wall top.
    dome = ("M180,460 L180,405 Q180,345 320,342 Q430,340 455,380 "
            "L475,460 Z")
    o.append(_hatch_fill(dome, ("url(#h6)",), sw=1.4))
    o.append(_line(140, 460, 540, 460, sw=1.5))
    o.append(_hr(430, 358, 10, 40, ("url(#h7)",), sw=1.0))
    o.append(_hr(430, 424, 10, 36, ("url(#h7)",), sw=1.0))
    o.append(T(446, 352, "Wall / Tường", 6.8, anchor="start", color=INK))
    o.append(_line(428, 410, 416, 414, sw=0.8, color=GREY))
    o.append(T(410, 418, "Door", 7.0, anchor="end", color=INK))
    o.append(_circle(300, 425, 2.8, fill=INK, sw=0))
    o.append(T(270, 408, "Source of", 6.8, anchor="end", color=INK))
    o.append(T(270, 417, "hazard", 6.8, anchor="end", color=INK))
    o.append(_arrow(298, 422, 225, 362, sw=1.0, head="a7"))
    o.append(T(248, 386, "b", 8.2, color=INK, weight="600"))
    o.append(_arrow(446, 372, 468, 352, sw=1.0, head="a7"))
    o.append(T(474, 348, "c", 8.2, anchor="start", color=INK, weight="600"))
    o.append(_dh(300, 430, 448, "a"))
    o.append(T(340, 480, "Mặt cắt / Elevation", 7.2, color=GREY))
    o.append(T(80, 502, "a = Distance of wall from source of hazard", 7.2,
               anchor="start", color=INK))
    o.append(T(80, 514, "b = Extent of hazardous area ignoring wall", 7.2,
               anchor="start", color=INK))
    o.append(T(80, 526, "c = b - a", 7.2, anchor="start", color=INK))
    o.append(_legend(548))
    o.append(T(340, 568,
               "Hình 3.17 · Lỗ hổng giữa các không gian / "
               "Figure 3.17 · Openings between spaces", 6.6, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt bằng và mặt cắt của tường có cửa: vùng Vùng 2 gạch "
                    "chéo đơn quanh nguồn nguy hiểm và chui qua cửa, tường "
                    "được gạch chéo, các kích thước a, b, c và đường mặt đất")),
                "Hình 3.17 · Lỗ hổng giữa các không gian. "
                "a = Khoảng cách từ tường đến nguồn nguy hiểm, "
                "b = Phạm vi không có tường, c = b - a",
                "Figure 3.17 · Openings between spaces. a = Distance of wall "
                "from source of hazard, b = Extent of hazardous area ignoring "
                "wall, c = b - a",
                "Mặt bằng: tường ngang có khe cửa, dấu nguồn nguy hiểm ở dưới, "
                "vùng gạch chéo đơn quanh nguồn và chui qua cửa thành mũ vòm "
                "tròn; mũi tên c ở góc trái trên, a từ nguồn đến tường, b về "
                "phía trái dưới. Mặt cắt: tường đứng có cửa, vùng gạch chéo "
                "đơn bao quanh và đi qua đỉnh tường, có các kích thước a, b, c.",
                "Plan: a hatched horizontal wall with a Door gap, a source dot "
                "below, and a single-diagonal hazardous area around the source "
                "pushing through the door as a rounded cap; arrows c at upper "
                "left, a from source to wall and b to the lower-left boundary. "
                "Elevation: a hatched wall with a door gap, the hatched area "
                "wrapping over its top, ground line and dimensions a, b and c.")


@_reg
def fig_f318():
    """Figure 3.18 - Hazardous areas due to short walls."""
    w, h = 680, 580
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.18 · Khu vực nguy hiểm do tường ngắn / "
               "Figure 3.18 · Hazardous areas due to short walls",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "a = Khoảng cách từ tường đến nguồn nguy hiểm, "
               "b = Phạm vi không có tường, c = b - a / "
               "a = Distance of wall from source of hazard, "
               "b = Extent of hazardous area ignoring wall, c = b - a",
               6.2, color=GREY))

    # ---- Upper plan view: a short wall floating above the source.
    blob = ("M205,150 Q205,110 280,108 L400,108 Q475,110 475,150 "
            "Q505,200 475,258 Q400,282 340,280 Q280,282 205,258 "
            "Q175,200 205,150 Z")
    o.append(_hatch_fill(blob, ("url(#h6)",), sw=1.4))
    o.append(_hr(260, 150, 160, 10, ("url(#h7)",), sw=1.0))
    o.append(T(430, 157, "Wall / Tường", 7.0, anchor="start", color=INK))
    o.append(_circle(340, 220, 2.8, fill=INK, sw=0))
    o.append(T(352, 218, "Source of", 6.8, anchor="start", color=INK))
    o.append(T(352, 227, "hazard", 6.8, anchor="start", color=INK))
    o.append(_arrow(280, 126, 240, 146, sw=1.0, head="a7"))
    o.append(T(232, 142, "c", 8.2, anchor="end", color=INK, weight="600"))
    o.append(_arrow(340, 216, 340, 164, sw=1.0, head="a7"))
    o.append(T(334, 192, "a", 8.2, anchor="end", color=INK, weight="600"))
    o.append(_arrow(336, 225, 230, 255, sw=1.0, head="a7"))
    o.append(T(276, 252, "b", 8.2, color=INK, weight="600"))
    o.append(T(340, 292, "Mặt bằng / Plan", 7.2, color=GREY))

    # ---- Lower elevation view: the zone rises over the short wall top.
    dome = ("M180,460 L180,405 Q180,345 320,340 Q440,338 458,375 "
            "L498,460 Z")
    o.append(_hatch_fill(dome, ("url(#h6)",), sw=1.4))
    o.append(_line(140, 460, 540, 460, sw=1.5))
    o.append(_hr(438, 355, 10, 105, ("url(#h7)",), sw=1.0))
    o.append(T(456, 350, "Wall / Tường", 6.8, anchor="start", color=INK))
    o.append(_circle(300, 430, 2.8, fill=INK, sw=0))
    o.append(T(270, 412, "Source of", 6.8, anchor="end", color=INK))
    o.append(T(270, 421, "hazard", 6.8, anchor="end", color=INK))
    o.append(_arrow(298, 426, 225, 362, sw=1.0, head="a7"))
    o.append(T(248, 388, "b", 8.2, color=INK, weight="600"))
    o.append(_arrow(448, 365, 470, 345, sw=1.0, head="a7"))
    o.append(T(476, 342, "c", 8.2, anchor="start", color=INK, weight="600"))
    o.append(_dh(300, 438, 448, "a"))
    o.append(T(340, 480, "Mặt cắt / Elevation", 7.2, color=GREY))
    o.append(T(80, 502, "a = Distance of wall from source of hazard", 7.2,
               anchor="start", color=INK))
    o.append(T(80, 514, "b = Extent of hazardous area ignoring wall", 7.2,
               anchor="start", color=INK))
    o.append(T(80, 526, "c = b - a", 7.2, anchor="start", color=INK))
    o.append(_legend(548))
    o.append(T(340, 568,
               "Hình 3.18 · Khu vực nguy hiểm do tường ngắn / "
               "Figure 3.18 · Hazardous areas due to short walls",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt bằng và mặt cắt của tường ngắn: đoạn tường ngắn "
                    "được gạch chéo, dấu nguồn nguy hiểm ở dưới, vùng Vùng 2 "
                    "gạch chéo đơn quanh cả hai đầu tường và đi qua đỉnh "
                    "tường, có các kích thước a, b, c")),
                "Hình 3.18 · Khu vực nguy hiểm do tường ngắn. "
                "a = Khoảng cách từ tường đến nguồn nguy hiểm, "
                "b = Phạm vi không có tường, c = b - a",
                "Figure 3.18 · Hazardous areas due to short walls. "
                "a = Distance of wall from source of hazard, "
                "b = Extent of hazardous area ignoring wall, c = b - a",
                "Mặt bằng: đoạn tường ngắn nằm trên dấu nguồn nguy hiểm, "
                "vùng gạch chéo đơn bao quanh cả hai đầu tường, mũi tên c ở "
                "góc trái trên, a từ nguồn đến tường, b về phía trái dưới. "
                "Mặt cắt: tường ngắn đứng bên phải trên mặt đất, vùng gạch "
                "chéo đơn vượt qua đỉnh tường, có các kích thước a, b, c.",
                "Plan: a short hatched wall segment above a source dot, with "
                "a single-diagonal area wrapping around both wall ends; "
                "arrows c at upper left, a from source to wall and b to the "
                "lower-left boundary. Elevation: a short hatched wall at "
                "right, the hatched area rising over its top, a ground line "
                "and dimensions a, b and c.")


@_reg
def fig_f319():
    """Figure 3.19 - Release at a vent."""
    w, h = 680, 522
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.19 · Xì thải tại miệng thông hơi / "
               "Figure 3.19 · Release at vent",
               9.4, color=INK, weight="600"))
    o.append(T(340, 34, "a = 1 m, b = ...", 6.8, color=GREY))

    # Large single-diagonal Zone 2 hemisphere on the base line.
    hemi = "M90,370 A250,250 0 0 1 590,370 Z"
    o.append(_hatch_fill(hemi, ("url(#h6)",), sw=1.4))
    o.append(_line(80, 370, 600, 370, sw=1.5))

    # Vent stack below the base line, with brick-like horizontal divisions.
    o.append(_rect(332, 370, 16, 50, fill=PAPER, sw=1.2))
    yy = 377
    while yy < 419:
        o.append(_line(332, yy, 348, yy, sw=0.7, color=GREY))
        yy += 7

    # Crosshatched Zone 1 circle a around the outlet.
    o.append(_circle(340, 370, 16, fill=PAPER, sw=0))
    o.append(_circle(340, 370, 16, fill="url(#h6)", sw=0))
    o.append(_circle(340, 370, 16, fill="url(#h7)", sw=0))
    o.append(_circle(340, 370, 16, fill="none", sw=1.3))
    o.append(T(362, 362, "a", 8.4, anchor="start", color=INK, weight="600"))

    # Radial b arrow to the upper-left arc and a small curved arrow at base.
    o.append(_arrow(340, 366, 180, 232, sw=1.1))
    o.append(T(246, 292, "b", 8.4, color=INK, weight="600"))
    o.append(_path("M326,424 Q312,432 326,438", fill="none", sw=0.9))
    o.append(_arrow(326, 438, 330, 433, sw=0.9, color=INK, head="a7"))

    o.append(_legend(442))
    o.append(T(60, 462, "a = 1 m, b = Calculated from Chapter 4 based on "
                        "jet-release extent equation", 6.6,
               anchor="start", color=INK))
    o.append(T(60, 474, "and volume of gas/vapour released.", 6.6,
               anchor="start", color=INK))
    o.append(T(60, 490, "Note: Where release is from a bursting disc Zone 0 "
                        "inside vent and Zone 1", 6.4,
               anchor="start", color=INK))
    o.append(T(60, 502, "immediately surrounding the vent, both become "
                        "Zone 2", 6.4, anchor="start", color=INK))
    o.append(T(340, 516,
               "Hình 3.19 · Xì thải tại miệng thông hơi / "
               "Figure 3.19 · Release at vent", 6.4, color=GREY))

    return _fig(svg(w, h, "".join(o), esc(
                    "Ống thông hơi đứng đứng có các vách ngang, vòng tròn "
                    "ô chéo chứa X Vùng 1 quanh miệng và bán cầu Vùng 2 gạch "
                    "chéo đơn lớn trên đường cơ sở, mũi tên bán kính b và "
                    "mũi tên cong nhỏ tại chân ống")),
                "Hình 3.19 · Xì thải tại miệng thông hơi. a = 1 m, "
                "b = Tính theo Chương 4 dựa trên phương trình độ phạm vi "
                "phun và thể tích khí/hơi thoát ra. Lưu ý: Khi xảy ra từ "
                "đĩa vỡ, Vùng 0 bên trong ống và Vùng 1 ngay quanh ống "
                "đều trở thành Vùng 2",
                "Figure 3.19 · Release at vent. a = 1 m, b = Calculated "
                "from Chapter 4 based on jet-release extent equation and "
                "volume of gas/vapour released. Note: Where release is from "
                "a bursting disc Zone 0 inside vent and Zone 1 immediately "
                "surrounding the vent, both become Zone 2",
                "Ống thông hơi hẹp có các vách ngang như gạch xây, vòng tròn "
                "nhỏ ô chéo chứa X quanh miệng đánh dấu a, bán cầu Vùng 2 "
                "gạch chéo đơn rất lớn nằm trên đường cơ sở, mũi tên bán "
                "kính b từ miệng đến cung trái trên và mũi tên cong nhỏ "
                "tại chân ống.",
                "A narrow vent stack with brick-like horizontal divisions, a "
                "small crosshatched Zone 1 circle a around the outlet and a "
                "very large single-diagonal Zone 2 hemisphere on the base "
                "line; a radial arrow b runs from the outlet to the upper-left "
                "arc, with a small curved arrow at the stack base.")
