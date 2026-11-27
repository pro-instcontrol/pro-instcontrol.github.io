# -*- coding: utf-8 -*-
"""Vector redraws of Figures 5.1-5.10 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 5 "Area classification practice for gases,
vapours and mists in areas which are not freely ventilated".

All ten figures are unhatched line technical drawings with single diagonal
hatching for the hazardous zone. Dashed outlines are the unmodified / unroofed
extent `E`; solid outlines are the adjusted extent. Plan/elevation pairs are
used for Figs. 5.1, 5.2, 5.6, 5.8, 5.9 and 5.10; plan views for Figs. 5.3,
5.4 and 5.5; an elevation for Fig. 5.7. No axes or scale bars appear.

Architecture mirrors `mcmillanfig04_a.py`: every figure returns the standard
five-tuple through `vfig._fig()` and is registered in `FIGS` by the `_reg`
decorator, while the named callables `fig_f501()` ... `fig_f510()` remain the
public API.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _defs, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape XML-significant characters in displayed text."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.0, **kw):
    """Plain text: escape first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


def TM(x, y, s, size=8.0, **kw):
    """Markup text: allow <sup>/<sub> tags, escape bare ampersands."""
    return _txt(x, y, str(s).replace("&", "&amp;"), size, **kw)


def _dimh(x1, x2, y, label, size=7.2, color=GREY, lab_dy=-4):
    """Horizontal dimension between two witness marks, arrowheads outward."""
    return "".join([
        _line(x1, y - 4, x1, y + 4, sw=0.7, color=color),
        _line(x2, y - 4, x2, y + 4, sw=0.7, color=color),
        _arrow(x1 + 1, y, x2 - 1, y, sw=0.8, color=color, head="a7"),
        _arrow(x2 - 1, y, x1 + 1, y, sw=0.8, color=color, head="a7"),
        T((x1 + x2) / 2.0, y + lab_dy, label, size, color=INK),
    ])


def _dimv(y1, y2, x, label, size=7.2, color=GREY, lab_dx=6, anchor="start"):
    """Vertical dimension between two witness marks, arrowheads outward."""
    return "".join([
        _line(x - 4, y1, x + 4, y1, sw=0.7, color=color),
        _line(x - 4, y2, x + 4, y2, sw=0.7, color=color),
        _arrow(x, y1 + 1, x, y2 - 1, sw=0.8, color=color, head="a7"),
        _arrow(x, y2 - 1, x, y1 + 1, sw=0.8, color=color, head="a7"),
        T(x + lab_dx, (y1 + y2) / 2.0 + 2.4, label, size,
          anchor=anchor, color=INK),
    ])


def _lead(x1, y1, x2, y2):
    """Thin grey leader arrow for a printed callout."""
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a7")


def _legend(o, lines, y, size=6.2, step=10.4):
    for i, line in enumerate(lines):
        o.append(T(96, y + i * step, line, size, anchor="start", color=INK))


def _strip(o, h, n, vi, en, note, size=6.2):
    """Small bilingual caption strip at the foot of every SVG."""
    o.append(T(340, h - 42,
               "Hình 5.%d · %s / Figure 5.%d · %s" % (n, vi, n, en),
               size, color=INK))
    o.append(T(340, h - 18, note, 5.9, color=GREY))


def _note_text():
    return ("Gạch chéo đơn = vùng nguy hiểm; nét đứt = phạm vi chưa điều chỉnh / "
            "Single hatch = hazardous zone; dashed = unmodified extent")


@_reg
def fig_f501():
    """Figure 5.1 - Effect of single walls within 1.5-3 m of sources of hazard."""
    w, h = 680, 650
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.1 · Ảnh hưởng của tường đơn trong khoảng 1,5–3 m từ nguồn nguy hiểm / "
               "Figure 5.1 · Effect of single walls within 1.5–3 m of sources of hazard",
               8.4, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt cắt đứng · Dưới: mặt bằng / Top: elevation · Bottom: plan",
               6.6, color=GREY))

    # ---- elevation -------------------------------------------------------
    o.append(_line(60, 250, 620, 250, sw=1.2, color=INK))
    o.append(T(618, 264, "Ground", 7.2, anchor="end", color=INK))
    # unmodified dome
    o.append(_path("M 96 250 C 96 120 176 70 270 72 C 370 74 455 120 470 206",
                   fill="none", sw=1.0, dash="4 3", color=GREY))
    # adjusted, hatched hazardous area
    o.append(_path("M 100 248 L 100 168 C 100 115 195 96 285 100 "
                   "C 375 104 452 126 472 168 C 492 205 466 232 432 226 "
                   "C 408 222 396 204 396 182 L 396 248 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    # wall
    o.append(_rect(356, 140, 8, 110, fill=INK, sw=0))
    o.append(T(372, 240, "Wall", 7.4, anchor="start", color=INK))
    # source
    o.append(_circle(150, 220, 3.0, fill=INK))
    o.append(T(62, 205, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(62, 214, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(112, 211, 146, 219))
    # dimensions
    o.append(_lead(150, 220, 108, 132))
    o.append(T(126, 170, "Z", 8.0, color=INK))
    o.append(_dimh(150, 356, 220, "X", lab_dy=-5))
    o.append(_dimv(220, 250, 150, "Y", lab_dx=-7, anchor="end"))
    o.append(_dimv(100, 118, 402, "a", lab_dx=6))
    o.append(_dimv(205, 228, 512, "b", lab_dx=6))
    o.append(_dimv(94, 120, 512, "c", lab_dx=6))

    # ---- plan ------------------------------------------------------------
    o.append(_circle(340, 385, 105, fill="url(#h6)", sw=1.3, color=INK))
    o.append(_path("M 268 312 C 300 292 380 292 412 312",
                   fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_rect(252, 316, 178, 7, fill=INK, sw=0))
    o.append(T(438, 326, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(340, 360, 3.0, fill=INK))
    o.append(T(340, 288, "Note", 7.6, color=INK))
    o.append(_lead(338, 292, 258, 311))
    o.append(_dimv(300, 316, 248, "a", lab_dx=-7, anchor="end"))
    o.append(_dimh(252, 430, 309, "d", lab_dy=-5))
    o.append(_dimh(252, 430, 330, "L", lab_dy=-5))
    o.append(_dimv(326, 360, 340, "X", lab_dx=6))
    o.append(_lead(340, 360, 250, 455))
    o.append(T(288, 418, "Z", 8.0, color=INK))
    o.append(T(470, 440, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(470, 449, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(466, 445, 344, 362))

    # ---- verbatim printed legend ----------------------------------------
    _legend(o, [
        "X = Distance wall/source of release (1.5–3 m)",
        "Y = Distance source to ground (Z − Y = 1.5–3 m)",
        "Z = Extent of hazardous area",
        "a = Z − X (vertical) or Z − L (horizontal)",
        "b = 0.5 Z (for densities greater than 1.3 only)",
        "c = 0.5 Z (for densities less than 0.7 only)",
        "d = wall length from edges of hazardous area",
        "Note: Where d is less than Z it is prudent to continue the hazardous",
        "      area across the rear face of the wall as shown",
    ], 484, step=10.2)

    _strip(o, h, 1,
           "Ảnh hưởng của tường đơn trong khoảng 1,5–3 m từ nguồn nguy hiểm",
           "Effect of single walls within 1.5–3 m of sources of hazard",
           _note_text())
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt đứng và mặt bằng: tường đơn cách nguồn 1,5–3 m, "
                        "vùng nguy hiểm gạch chéo quấn qua đầu tường, đường nét đứt "
                        "là phạm vi chưa điều chỉnh, các kích thước a b c d X Y Z L")),
                "Hình 5.1 · Ảnh hưởng của tường đơn trong khoảng 1,5–3 m từ nguồn "
                "nguy hiểm. Chú thích in trên hình được sao chép nguyên văn.",
                "Figure 5.1 · Effect of single walls within 1.5–3 m of sources of "
                "hazard. The printed legend is transcribed verbatim.",
                "Mặt cắt đứng có đường mặt đất, tường đứng màu đen, nguồn phát thải "
                "bên trái và vùng nguy hiểm gạch chéo quấn qua đầu tường với đường "
                "vòm nét đứt phía trên; mặt bằng là vùng gạch chéo gần tròn với thanh "
                "tường ngang ở phía trên và các mũi tên kích thước a, d, L, X, Z.",
                "Elevation with a ground line, a solid vertical wall, a source at "
                "left and a hatched hazardous zone wrapping over the wall beneath a "
                "dashed dome; plan view is a near-circular hatched zone with a thick "
                "horizontal wall bar near the top and dimensions a, d, L, X, Z.")


@_reg
def fig_f502():
    """Figure 5.2 - Effect of single walls within 1.5 m of source of hazard."""
    w, h = 680, 600
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.2 · Ảnh hưởng của tường đơn trong vòng 1,5 m từ nguồn nguy hiểm / "
               "Figure 5.2 · Effect of single walls within 1.5 m of source of hazard",
               8.4, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt cắt đứng · Dưới: mặt bằng / Top: elevation · Bottom: plan",
               6.6, color=GREY))

    # ---- elevation -------------------------------------------------------
    o.append(_line(60, 232, 600, 232, sw=1.2, color=INK))
    o.append(T(598, 246, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 94 232 C 94 105 180 62 265 68 C 350 74 390 120 392 200",
                   fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_path("M 98 230 L 98 155 C 98 110 180 90 260 95 "
                   "C 330 100 380 125 385 165 C 390 195 370 215 345 210 "
                   "C 325 206 315 190 315 175 L 315 230 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_rect(246, 120, 8, 112, fill=INK, sw=0))
    o.append(T(261, 224, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(150, 205, 3.0, fill=INK))
    o.append(T(62, 188, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(62, 197, "hazard", 7.0, anchor="start", color=INK))
    o.append(_lead(112, 194, 147, 204))
    o.append(_lead(150, 205, 106, 143))
    o.append(T(120, 170, "1.5 Z", 7.4, color=INK))
    o.append(_dimh(150, 250, 205, "X", lab_dy=-5))
    o.append(_dimv(68, 94, 400, "c", lab_dx=6))
    o.append(_dimv(190, 212, 400, "b", lab_dx=6))
    o.append(_dimv(95, 114, 280, "a", lab_dx=6))

    # ---- plan ------------------------------------------------------------
    o.append(_circle(340, 350, 100, fill="url(#h6)", sw=1.3, color=INK))
    o.append(_path("M 292 300 C 310 288 370 288 388 300",
                   fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_rect(286, 298, 110, 7, fill=INK, sw=0))
    o.append(T(402, 308, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(340, 350, 3.0, fill=INK))
    o.append(_lead(340, 350, 252, 425))
    o.append(T(286, 400, "1.5 Z", 7.4, color=INK))
    o.append(_dimh(286, 396, 316, "L", lab_dy=-5))
    o.append(_dimv(305, 350, 340, "X", lab_dx=6))
    o.append(T(160, 372, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(160, 381, "hazard", 7.0, anchor="start", color=INK))
    o.append(_lead(212, 378, 337, 352))

    # ---- verbatim printed legend ----------------------------------------
    _legend(o, [
        "X = Distance wall/source of hazard (< 1.5 m)",
        "Y = Distance source to ground (Z − Y = < 1.5 m)",
        "Z = Extent of hazardous area (unmodified)",
        "a = 1.5 Z − X",
        "b = Distortion of hazardous area (densities greater than 1.3 only)",
        "c = 0.75 Z (Densities less than 0.7 only)",
    ], 432, step=10.6)

    _strip(o, h, 2,
           "Ảnh hưởng của tường đơn trong vòng 1,5 m từ nguồn nguy hiểm",
           "Effect of single walls within 1.5 m of source of hazard",
           _note_text())
    return _fig(svg(w, h, "".join(o),
                    esc("Tường đơn đặt rất gần nguồn (dưới 1,5 m); mặt cắt đứng và "
                        "mặt bằng đều có vùng gạch chéo quấn qua tường, bán kính 1,5 Z "
                        "và các kích thước a, b, c, L, X")),
                "Hình 5.2 · Ảnh hưởng của tường đơn trong vòng 1,5 m từ nguồn nguy "
                "hiểm. Dấu `< 1,5 m` được giữ nguyên theo bản in.",
                "Figure 5.2 · Effect of single walls within 1.5 m of source of "
                "hazard. The printed `< 1.5 m` glyph is preserved verbatim.",
                "Mặt cắt đứng: tường đen gần nguồn, vùng gạch chéo quấn qua đầu tường, "
                "đường vòm nét đứt phía trên, mũi tên bán kính 1,5 Z và các kích thước "
                "a, b, c, X; mặt bằng: vùng tròn gạch chéo có thanh tường phía trên, "
                "bán kính 1,5 Z và kích thước L, X.",
                "Elevation: a solid wall close to the source, a hatched zone wrapping "
                "over it, a dashed dome above, a 1.5 Z radius arrow and dimensions a, "
                "b, c, X; plan: a hatched circular zone with a wall bar near the top, "
                "a 1.5 Z radius and dimensions L, X.")


@_reg
def fig_f503():
    """Figure 5.3 - Typical two-wall effect (a)."""
    w, h = 680, 440
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.3 · Ảnh hưởng điển hình của hai bức tường (a) / "
               "Figure 5.3 · Typical two-wall effect (a)",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32, "Mặt bằng / Plan view", 6.6, color=GREY))

    o.append(_path("M 250 330 C 185 330 160 265 165 205 "
                   "C 170 135 235 92 315 90 L 470 90 L 470 330 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(245, 340, 17, fill="url(#h6)", sw=0))
    # walls on top of the hatch
    o.append(_rect(466, 90, 8, 240, fill=INK, sw=0))
    o.append(_rect(250, 326, 224, 8, fill=INK, sw=0))
    o.append(T(482, 210, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(350, 347, "Wall", 7.4, color=INK))
    o.append(_circle(360, 275, 3.0, fill=INK))
    o.append(T(366, 264, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(366, 273, "hazard", 7.0, anchor="start", color=INK))
    o.append(_lead(360, 275, 182, 175))
    o.append(T(258, 217, "E", 8.0, color=INK))
    o.append(_dimh(255, 360, 275, "C", lab_dy=-5))
    o.append(_dimh(234, 254, 350, "a", lab_dy=10))

    _legend(o, [
        "E = Extent of hazard taking account of wall proximity,",
        "C = Distance source of hazard/wall end",
        "a = E − C",
    ], 360, step=11.2)
    _strip(o, h, 3,
           "Ảnh hưởng điển hình của hai bức tường (a)",
           "Typical two-wall effect (a)",
           "Mặt bằng: vùng nguy hiểm gạch chéo bao quanh góc hai tường / "
           "Plan: hatched hazardous area wrapping around a two-wall corner")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng gồm hai tường vuông góc, vùng nguy hiểm gạch chéo "
                        "bọc quanh đầu tường ngang, nguồn ở góc trong và các kích "
                        "thước E, C, a")),
                "Hình 5.3 · Ảnh hưởng điển hình của hai bức tường (a).",
                "Figure 5.3 · Typical two-wall effect (a).",
                "Mặt bằng có tường đứng bên phải và tường ngang bên dưới tạo góc vuông; "
                "vùng nguy hiểm gạch chéo chiếm phía trong góc và quấn tròn qua đầu "
                "tường ngang; mũi tên E, C, a chỉ từ nguồn ra.",
                "Plan view with a vertical wall at right and a horizontal wall at the "
                "bottom forming a corner; the hatched hazardous area fills the inside "
                "and rounds past the free end of the horizontal wall; arrows E, C and a.")


@_reg
def fig_f504():
    """Figure 5.4 - Typical two-wall effect (b)."""
    w, h = 680, 440
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.4 · Ảnh hưởng điển hình của hai bức tường (b) / "
               "Figure 5.4 · Typical two-wall effect (b)",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32, "Mặt bằng / Plan view", 6.6, color=GREY))

    o.append(_path("M 285 320 C 215 318 180 255 185 195 "
                   "C 190 135 255 92 335 92 C 415 92 470 108 470 120 L 470 320 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(472, 116, 20, fill="url(#h6)", sw=0))
    o.append(_circle(278, 322, 20, fill="url(#h6)", sw=0))
    o.append(_rect(466, 116, 8, 204, fill=INK, sw=0))
    o.append(_rect(280, 316, 194, 8, fill=INK, sw=0))
    o.append(T(482, 220, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(370, 339, "Wall", 7.4, color=INK))
    o.append(_circle(400, 270, 3.0, fill=INK))
    o.append(T(332, 254, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(332, 263, "hazard", 7.0, anchor="start", color=INK))
    o.append(_lead(396, 267, 202, 160))
    o.append(T(268, 206, "E", 8.0, color=INK))
    o.append(_dimv(150, 270, 400, "C", lab_dx=6))
    o.append(_dimv(94, 114, 496, "a", lab_dx=6))
    o.append(_dimv(300, 320, 258, "a", lab_dx=-7, anchor="end"))

    _legend(o, [
        "E = Extent of hazardous area with adjustments for wall proximity,",
        "C = Distance source of hazard/wall end",
        "a = E − C",
    ], 360, step=11.2)
    _strip(o, h, 4,
           "Ảnh hưởng điển hình của hai bức tường (b)",
           "Typical two-wall effect (b)",
           "Mặt bằng: vùng gạch chéo quấn tròn qua cả hai đầu tường tự do / "
           "Plan: hatched area wraps around both free wall ends")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng hai tường chữ L, vùng nguy hiểm gạch chéo bọc "
                        "quanh cả hai đầu tường với các thùy tròn, nguồn gần góc "
                        "trong và các kích thước E, C, a")),
                "Hình 5.4 · Ảnh hưởng điển hình của hai bức tường (b).",
                "Figure 5.4 · Typical two-wall effect (b).",
                "Mặt bằng có hai tường chữ L; vùng gạch chéo quấn tròn qua cả đầu tường "
                "đứng và đầu tường ngang; nguồn nằm gần góc trong, với mũi tên E, C và "
                "a ở hai đầu tường.",
                "Plan view with two L-shaped walls; the hatched area forms rounded "
                "lobes past both free wall ends; the source sits near the inner corner "
                "with arrows E, C and a at the wall ends.")


@_reg
def fig_f505():
    """Figure 5.5 - Typical three-wall effect."""
    w, h = 680, 440
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.5 · Ảnh hưởng điển hình của ba bức tường / "
               "Figure 5.5 · Typical three-wall effect",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32, "Mặt bằng / Plan view", 6.6, color=GREY))

    o.append(_path("M 270 330 L 270 182 C 245 178 235 140 270 132 "
                   "L 470 132 C 505 140 495 178 470 182 L 470 330 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_rect(266, 180, 8, 150, fill=INK, sw=0))
    o.append(_rect(466, 180, 8, 150, fill=INK, sw=0))
    o.append(_rect(270, 326, 204, 8, fill=INK, sw=0))
    o.append(_circle(322, 292, 3.0, fill=INK))
    o.append(T(334, 282, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(334, 291, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(332, 289, 324, 292))
    o.append(_dimv(140, 164, 244, "a", lab_dx=-7, anchor="end"))
    o.append(_dimv(140, 164, 492, "a", lab_dx=6))

    _legend(o, [
        "a = Taken from Table 3.2 on the basis of maximum release with",
        "      a minimum of 0.5 m",
    ], 356, step=11.2)
    _strip(o, h, 5,
           "Ảnh hưởng điển hình của ba bức tường",
           "Typical three-wall effect",
           "Mặt bằng: ba tường hình chữ U, vùng gạch chéo lấp đầy và quấn qua hai đầu tường / "
           "Plan: three U-shaped walls, hatched zone fills and rounds past both wall ends")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng ba tường hình chữ U hở phía trên, vùng nguy hiểm "
                        "gạch chéo lấp kín bên trong và bo tròn qua hai đầu tường, "
                        "nguồn ở gần đáy, kích thước a ở hai đầu")),
                "Hình 5.5 · Ảnh hưởng điển hình của ba bức tường.",
                "Figure 5.5 · Typical three-wall effect.",
                "Mặt bằng ba tường hình chữ U hở phía trên; vùng gạch chéo lấp đầy bên "
                "trong và quấn bo qua hai đầu tường; nguồn phát thải nằm gần đáy và kích "
                "thước a được ghi ở mỗi đầu tường.",
                "Plan view with three walls forming a U open at the top; the hatched "
                "hazardous zone fills the enclosure and rounds over both wall ends; "
                "the source lies near the bottom and a is marked at each wall end.")


@_reg
def fig_f506():
    """Figure 5.6 - Effect of flat roof within 5 m of free ventilation limit."""
    w, h = 680, 620
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.6 · Ảnh hưởng của mái phẳng trong vòng 5 m từ giới hạn thông gió tự do / "
               "Figure 5.6 · Effect of flat roof within 5 m of free ventilation limit",
               8.0, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt bằng · Dưới: mặt cắt đứng / Top: plan · Bottom: elevation",
               6.6, color=GREY))

    # ---- plan ------------------------------------------------------------
    o.append(_rect(230, 90, 240, 160, fill="none", sw=1.3, stroke=INK))
    o.append(T(240, 84, "Roof", 7.4, anchor="start", color=INK))
    o.append(_circle(400, 180, 85, fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_path("M 462 118 C 520 120 555 145 555 180 "
                   "C 555 215 520 240 462 242 C 480 215 480 145 462 118 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(400, 180, 3.0, fill=INK))
    o.append(_lead(400, 180, 340, 116))
    o.append(T(360, 148, "E", 8.0, color=INK))
    o.append(_dimh(400, 470, 76, "X", lab_dy=-5))
    o.append(_dimh(470, 520, 76, "a", lab_dy=-5))
    o.append(T(120, 205, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(120, 214, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(170, 211, 397, 182))

    # ---- elevation -------------------------------------------------------
    o.append(_line(200, 322, 560, 322, sw=2.4, color=INK))
    o.append(T(208, 314, "Roof", 7.4, anchor="start", color=INK))
    o.append(_line(120, 490, 600, 490, sw=1.2, color=INK))
    o.append(T(598, 504, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 200 486 L 200 326 C 200 323 205 322 210 322 "
                   "L 495 322 C 495 305 500 285 520 285 "
                   "C 540 285 545 305 545 322 L 560 322 L 560 486 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(400, 400, 110, fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_circle(400, 400, 3.0, fill=INK))
    o.append(_lead(400, 400, 322, 322))
    o.append(T(348, 360, "E", 8.0, color=INK))
    o.append(_dimh(400, 560, 400, "X", lab_dy=-5))
    o.append(_dimv(285, 320, 522, "a", lab_dx=6))

    _legend(o, [
        "E = Extent of hazardous area neglecting effect of roof,",
        "X = Distance source of release/wall,",
        "a = E − X",
    ], 512, step=11.0)
    _strip(o, h, 6,
           "Ảnh hưởng của mái phẳng trong vòng 5 m từ giới hạn thông gió tự do",
           "Effect of flat roof within 5 m of free ventilation limit of explosive atmosphere",
           _note_text(), size=5.9)
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng: mái phẳng hình chữ nhật, đường tròn nét đứt E và "
                        "vùng gạch chéo tràn qua cạnh phải; mặt cắt: mái nằm ngang, "
                        "vùng gạch chéo chạm mái và bo cao thêm a")),
                "Hình 5.6 · Ảnh hưởng của mái phẳng trong vòng 5 m từ giới hạn thông "
                "gió tự do của hỗn hợp có khả năng nổ.",
                "Figure 5.6 · Effect of flat roof within 5 m of free ventilation limit "
                "of explosive atmosphere.",
                "Mặt bằng có hình chữ nhật nhãn Roof, đường tròn đứt nét E quanh nguồn "
                "và thùy gạch chéo tràn qua cạnh phải; mặt cắt có thanh mái đen, đường "
                "mặt đất, vùng gạch chéo chạm mái và bo lên trên mái một đoạn a.",
                "Plan shows a rectangular Roof outline, a dashed circle E around the "
                "source and a hatched lobe spilling past the right edge; elevation has "
                "a thick Roof line, a ground line and a hatched zone reaching the roof "
                "and rounding above it by a.")


@_reg
def fig_f507():
    """Figure 5.7 - Effect of hip roof within 5 m of E."""
    w, h = 680, 480
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.7 · Ảnh hưởng của mái hồi trong vòng 5 m từ E / "
               "Figure 5.7 · Effect of hip roof within 5 m of E",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32, "Mặt cắt đứng / Elevation cross-section", 6.6, color=GREY))

    o.append(_line(150, 360, 560, 360, sw=1.2, color=INK))
    o.append(T(558, 374, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 260 358 L 260 240 L 340 150 L 330 132 "
                   "L 350 132 L 420 240 L 420 358 Z",
                   fill="url(#h6)", sw=1.4, color=INK))
    o.append(_rect(331, 120, 18, 15, fill=PAPER, sw=1.0))
    o.append(_dimv(120, 138, 368, "a", lab_dx=6))
    o.append(_circle(340, 300, 75, fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_circle(340, 300, 3.0, fill=INK))
    o.append(T(140, 215, "Hip roof", 7.4, anchor="start", color=INK))
    o.append(_lead(206, 212, 258, 224))
    o.append(T(148, 320, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(148, 329, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(208, 326, 337, 302))
    o.append(_lead(340, 300, 292, 252))
    o.append(T(300, 268, "E", 8.0, color=INK))

    _legend(o, [
        "E = Extent of hazardous area neglecting roof,",
        "a = 1 m",
    ], 392, step=11.6)
    _strip(o, h, 7,
           "Ảnh hưởng của mái hồi trong vòng 5 m từ E",
           "Effect of hip roof within 5 m of E",
           "Mặt cắt: toàn bộ không gian dưới mái hồi được gạch chéo, lỗ thông hơi ở đỉnh có a = 1 m / "
           "Elevation: hatched roof volume, a = 1 m band at the apex vent")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt mái hồi hình ngũ giác có lỗ thông hơi ở đỉnh, "
                        "toàn bộ bên trong được gạch chéo, nguồn và đường tròn đứt "
                        "E bên dưới, dải kích thước a quanh lỗ thông hơi")),
                "Hình 5.7 · Ảnh hưởng của mái hồi trong vòng 5 m từ E.",
                "Figure 5.7 · Effect of hip roof within 5 m of E.",
                "Mặt cắt ngang mái hồi kiểu chuồng Hà Lan có lỗ thông hơi nhỏ ở đỉnh; "
                "toàn bộ thể tích dưới mái được gạch chéo; nguồn phát thải và đường tròn "
                "đứt nét E nằm bên dưới; dải a = 1 m quanh lỗ thông hơi.",
                "Cross-section of a hipped (dutch-barn) roof with a small apex vent; "
                "the whole roof volume is hatched; the source and dashed extent E lie "
                "below; an a = 1 m band surrounds the apex vent.")


@_reg
def fig_f508():
    """Figure 5.8 - Effects of roof over single wall."""
    w, h = 680, 660
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.8 · Ảnh hưởng của mái phủ trên một bức tường / "
               "Figure 5.8 · Effects of roof over single wall",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt cắt đứng · Dưới: mặt bằng / Top: elevation · Bottom: plan",
               6.6, color=GREY))

    # ---- elevation -------------------------------------------------------
    o.append(_line(120, 255, 620, 255, sw=1.2, color=INK))
    o.append(T(618, 269, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 172 242 C 175 130 240 68 320 70 C 390 72 445 120 455 200",
                   fill="none", sw=1.0, dash="4 3", color=GREY))
    o.append(_path("M 170 255 L 170 120 C 170 92 230 78 300 78 "
                   "C 380 78 460 94 470 125 L 470 255 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_line(170, 110, 520, 110, sw=2.4, color=INK))
    o.append(T(180, 102, "Roof", 7.4, anchor="start", color=INK))
    o.append(_rect(416, 110, 8, 145, fill=INK, sw=0))
    o.append(T(430, 245, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(250, 200, 3.0, fill=INK))
    o.append(T(120, 192, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(120, 201, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(172, 198, 247, 202))
    o.append(_dimv(78, 108, 480, "a", lab_dx=6))
    o.append(_dimv(200, 255, 250, "V", lab_dx=-7, anchor="end"))
    o.append(_dimh(250, 420, 200, "X", lab_dy=-5))

    # ---- plan ------------------------------------------------------------
    o.append(_path("M 270 470 C 240 470 235 420 245 380 "
                   "C 255 335 300 312 360 312 C 420 312 480 330 495 365 "
                   "C 510 400 500 455 470 468 L 270 470 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_rect(290, 360, 160, 95, fill=PAPER, sw=1.2, stroke=INK))
    o.append(T(370, 483, "Roof", 7.4, color=INK))
    o.append(_rect(290, 348, 160, 7, fill=INK, sw=0))
    o.append(T(456, 347, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(370, 410, 3.0, fill=INK))
    o.append(_line(370, 410, 370, 300, sw=0.9, dash="2 3", color=GREY))
    o.append(T(370, 295, "F", 8.0, color=INK))
    o.append(_dimh(300, 440, 324, "b", lab_dy=-5))
    o.append(_dimv(328, 348, 482, "a", lab_dx=6))
    o.append(T(160, 414, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(160, 423, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(212, 420, 367, 412))

    # ---- verbatim printed legend ----------------------------------------
    _legend(o, [
        "E = Extent of hazardous area taking account of wall",
        "      proximity but in absence of roof",
        "V = Height of source of release",
        "X = Distance source/wall",
        "a = E − Y (with a minimum of 0.5 m over roof)",
        "b = 2y − 2a",
        "Note: Where b is less than E hazardous area extends",
        "      behind and over roof to F",
    ], 534, step=10.4)

    _strip(o, h, 8,
           "Ảnh hưởng của mái phủ trên một bức tường",
           "Effects of roof over single wall",
           "Ký hiệu E − Y và 2y − 2a được giữ nguyên dù Y/y không được định nghĩa / "
           "E − Y and 2y − 2a preserved although Y/y are undefined")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt đứng: mái nằm ngang, tường đứng, vùng gạch chéo "
                        "qua mái một đoạn a và đường đứt nét E; mặt bằng: hình chữ "
                        "nhật Roof trong vùng gạch chéo, thanh tường, các kích thước "
                        "a, b và đường chấm dẫn tới F")),
                "Hình 5.8 · Ảnh hưởng của mái phủ trên một bức tường. Chú thích in "
                "dùng E − Y và 2y − 2a dù V mới là ký hiệu được định nghĩa.",
                "Figure 5.8 · Effects of roof over single wall. The printed legend "
                "uses E − Y and 2y − 2a although V is the defined symbol.",
                "Mặt cắt đứng có mái ngang, tường đứng, nguồn bên trái, vùng gạch chéo "
                "bo cao quá mái một đoạn a và đường đứt nét E; mặt bằng có hình chữ "
                "nhật Roof trong vùng gạch chéo, thanh tường ngang, đường chấm tới F, "
                "kích thước a, b.",
                "Elevation with a horizontal Roof line, a solid Wall, a source at left, "
                "a hatched zone rounding above the roof by a and a dashed extent E; "
                "plan with a rectangular Roof inside a hatched wrap, a wall bar, a "
                "dotted line to F and dimensions a, b.")


@_reg
def fig_f509():
    """Figure 5.9 - Effect of roof over two walls."""
    w, h = 680, 640
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.9 · Ảnh hưởng của mái phủ trên hai bức tường / "
               "Figure 5.9 · Effect of roof over two walls",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt bằng · Dưới: mặt cắt đứng / Top: plan · Bottom: elevation",
               6.6, color=GREY))

    # ---- plan ------------------------------------------------------------
    o.append(_path("M 320 230 C 255 230 235 175 250 125 "
                   "C 265 80 330 72 390 78 C 460 84 520 100 520 150 "
                   "C 520 195 485 225 455 230 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(490, 108, 17, fill="url(#h6)", sw=0))
    o.append(_circle(315, 232, 17, fill="url(#h6)", sw=0))
    o.append(_rect(330, 100, 130, 130, fill=PAPER, sw=1.2, stroke=INK))
    o.append(T(344, 92, "Roof", 7.4, anchor="start", color=INK))
    o.append(_rect(456, 100, 8, 150, fill=INK, sw=0))
    o.append(_rect(320, 226, 144, 8, fill=INK, sw=0))
    o.append(T(472, 178, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(372, 247, "Wall", 7.4, color=INK))
    o.append(_circle(440, 215, 3.0, fill=INK))
    o.append(T(468, 262, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(468, 271, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(464, 260, 442, 216))
    o.append(_lead(440, 215, 258, 106))
    o.append(T(336, 152, "E", 8.0, color=INK))
    o.append(_dimv(110, 215, 440, "C", lab_dx=6))
    o.append(_lead(440, 215, 330, 100))
    o.append(T(372, 158, "D", 8.0, color=INK))
    o.append(_dimv(88, 104, 498, "a", lab_dx=6))

    # ---- elevation -------------------------------------------------------
    o.append(_line(250, 340, 500, 340, sw=2.4, color=INK))
    o.append(T(260, 332, "Roof", 7.4, anchor="start", color=INK))
    o.append(_rect(476, 340, 8, 150, fill=INK, sw=0))
    o.append(T(492, 466, "Wall", 7.4, anchor="start", color=INK))
    o.append(_line(140, 490, 600, 490, sw=1.2, color=INK))
    o.append(T(598, 504, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 202 486 L 202 350 C 205 327 250 318 320 318 "
                   "L 480 318 C 520 318 540 335 540 360 "
                   "L 540 486 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_circle(400, 420, 3.0, fill=INK))
    o.append(T(150, 334, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(150, 343, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(216, 340, 398, 421))
    o.append(_lead(400, 420, 252, 342))
    o.append(T(312, 380, "E", 8.0, color=INK))
    o.append(_dimh(200, 250, 512, "F", lab_dy=10))
    o.append(_dimh(250, 400, 512, "C", lab_dy=10))
    o.append(_dimv(318, 338, 512, "a", lab_dx=6))

    _legend(o, [
        "E = Extent of hazardous area taking account of walls if roof is not present",
        "C = Distance from source to end wall",
        "D = Distance from source to furthest corner of roof",
        "F = E − D",
        "a = E − C",
    ], 540, step=10.8)

    _strip(o, h, 9,
           "Ảnh hưởng của mái phủ trên hai bức tường",
           "Effect of roof over two walls",
           _note_text(), size=6.0)
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng có mái chữ nhật trong hai tường chữ L, vùng gạch "
                        "chéo quấn quanh, nguồn góc dưới phải, các kích thước E, C, D "
                        "và a; mặt cắt có mái đen, tường đứng, vùng gạch chéo và F, C")),
                "Hình 5.9 · Ảnh hưởng của mái phủ trên hai bức tường.",
                "Figure 5.9 · Effect of roof over two walls.",
                "Mặt bằng có mái hình chữ nhật nằm trong hai tường chữ L, vùng gạch "
                "chéo quấn quanh và nguồn gần góc dưới phải, với các mũi tên E, C, D, a; "
                "mặt cắt có thanh mái đen, tường đứng, vùng gạch chéo và các kích thước "
                "F, C, a.",
                "Plan shows a rectangular Roof inside two L-shaped walls, a hatched "
                "wrap-around and a source near the lower-right corner with arrows E, C, "
                "D and a; elevation has a thick Roof line, a vertical Wall, the hatched "
                "zone and dimensions F, C, a.")


@_reg
def fig_f510():
    """Figure 5.10 - Effect of roof on three-wall system."""
    w, h = 680, 600
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 5.10 · Ảnh hưởng của mái lên hệ thống ba bức tường / "
               "Figure 5.10 · Effect of roof on three-wall system",
               8.4, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trên: mặt bằng · Dưới: mặt cắt đứng / Top: plan · Bottom: elevation",
               6.6, color=GREY))

    # ---- plan ------------------------------------------------------------
    o.append(_path("M 280 240 L 280 182 C 252 176 242 138 278 130 "
                   "L 462 130 C 498 138 488 176 460 182 L 460 240 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(_rect(292, 158, 156, 74, fill=PAPER, sw=1.2, stroke=INK))
    o.append(T(474, 172, "Roof", 7.4, anchor="start", color=INK))
    o.append(_lead(472, 176, 446, 194))
    o.append(_rect(276, 182, 8, 58, fill=INK, sw=0))
    o.append(_rect(456, 182, 8, 58, fill=INK, sw=0))
    o.append(_rect(280, 236, 184, 8, fill=INK, sw=0))
    o.append(T(266, 200, "Wall", 7.4, anchor="end", color=INK))
    o.append(T(472, 200, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(372, 257, "Wall", 7.4, color=INK))
    o.append(T(370, 124, "Open end", 7.4, color=INK))
    o.append(_circle(315, 226, 3.0, fill=INK))
    o.append(T(170, 230, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(170, 239, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(222, 236, 313, 227))
    o.append(_dimv(130, 148, 482, "a", lab_dx=6))

    # ---- elevation -------------------------------------------------------
    o.append(_line(250, 310, 470, 310, sw=2.4, color=INK))
    o.append(T(260, 302, "Roof", 7.4, anchor="start", color=INK))
    o.append(_rect(266, 310, 8, 140, fill=INK, sw=0))
    o.append(_rect(446, 310, 8, 140, fill=INK, sw=0))
    o.append(_line(140, 450, 600, 450, sw=1.2, color=INK))
    o.append(T(598, 464, "Ground", 7.2, anchor="end", color=INK))
    o.append(_path("M 250 446 L 250 330 C 250 305 285 286 320 286 "
                   "L 410 286 C 455 286 470 305 470 330 L 470 446 Z",
                   fill="url(#h6)", sw=1.3, color=INK))
    o.append(T(256, 382, "Wall", 7.4, anchor="end", color=INK))
    o.append(T(462, 382, "Wall", 7.4, anchor="start", color=INK))
    o.append(_circle(390, 415, 3.0, fill=INK))
    o.append(T(490, 420, "Source of", 7.0, anchor="start", color=INK))
    o.append(T(490, 429, "release", 7.0, anchor="start", color=INK))
    o.append(_lead(486, 423, 392, 416))
    o.append(_dimv(286, 308, 238, "a", lab_dx=-7, anchor="end"))

    _legend(o, [
        "a = Taken from Table 3.2 on the basis of maximum release",
        "      (minimum figure 0.5 m)",
    ], 482, step=11.2)
    _strip(o, h, 10,
           "Ảnh hưởng của mái lên hệ thống ba bức tường",
           "Effect of roof on three-wall system",
           _note_text())
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt bằng có ba tường hình chữ U với đầu hở ở phía trên, "
                        "mái chữ nhật bên trong, vùng gạch chéo tràn qua đầu hở và "
                        "đầu tường, kích thước a; mặt cắt có mái ngang và vùng gạch "
                        "chéo bo cao hơn mái")),
                "Hình 5.10 · Ảnh hưởng của mái lên hệ thống ba bức tường.",
                "Figure 5.10 · Effect of roof on three-wall system.",
                "Mặt bằng có ba tường hình chữ U hở phía trên, mái hình chữ nhật nằm "
                "trong, vùng gạch chéo tràn qua đầu hở và quấn qua đầu tường với kích "
                "thước a; mặt cắt có thanh mái ngang và vùng gạch chéo bo cao hơn mái.",
                "Plan has three walls forming a U with an open end at the top, a "
                "rectangular Roof inside and a hatched zone spilling through the open "
                "end and past the wall ends with dimension a; elevation shows a "
                "horizontal Roof line and a hatched zone rounding above it.")
