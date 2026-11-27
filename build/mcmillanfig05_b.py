# -*- coding: utf-8 -*-
"""Vector redraws of Figures 5.11-5.15 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 5 "Area classification practice
for gases, vapours and mists in areas which are not freely ventilated".

Fig. 5.11 is a plan of a room with four vent openings; Figs. 5.12-5.14 are
building cross-sections showing forced/extract/local ventilation; Fig. 5.15
is the paint-spray booth.  Single diagonal hatching marks a Zone 2-type
hazardous halo, cross-hatching marks the more severe Zone 1 interior in
Figs. 5.13-5.15.  No axes or scale bars are drawn.

Architecture mirrors `mcmillanfig04_a.py`: every figure returns the standard
five-tuple through `vfig._fig()` and is registered in `FIGS` by the `_reg`
decorator.  Printed legends and caption notes are preserved verbatim.
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


def TP(x, y, s, size=8.0, **kw):
    """Plain text with preserved runs of spaces for aligned legend columns."""
    return _txt(x, y, esc(s), size, **kw).replace(
        "<text ", '<text xml:space="preserve" ', 1)


def _cross_defs():
    """vfig._defs() plus a cross-hatch pattern for Zone 1 interiors."""
    xh = ('<pattern id="xh" width="7" height="7" patternUnits="userSpaceOnUse" '
          'patternTransform="rotate(45)">'
          '<line x1="0" y1="0" x2="0" y2="7" stroke="#6f6a5f" stroke-width="0.7"/>'
          '<line x1="0" y1="0" x2="7" y2="0" stroke="#6f6a5f" stroke-width="0.7"/>'
          '</pattern>')
    return _defs().replace("</defs>", xh + "</defs>")


def _dim(x1, y1, x2, y2, color=GREY):
    """Double-headed dimension line."""
    return (_arrow(x1, y1, x2, y2, sw=0.8, color=color, head="a7")
            + _arrow(x2, y2, x1, y1, sw=0.8, color=color, head="a7"))


def _fan(cx, cy):
    """Fan symbol: a circle crossed by an X."""
    return (_circle(cx, cy, 7, fill=PAPER, sw=1.1)
            + _line(cx - 4, cy - 4, cx + 4, cy + 4, sw=0.9)
            + _line(cx - 4, cy + 4, cx + 4, cy - 4, sw=0.9))


def _lobe(cx, cy, r, cross=False):
    """Hatched hazardous lobe (single hatch = Zone 2, cross = Zone 1)."""
    return _circle(cx, cy, r, fill="url(#xh)" if cross else "url(#h6)", sw=1.0)


def _head(o, w, n, vi, en, sub):
    o.append(T(w / 2.0, 18,
               "Hình 5.%d · %s / Figure 5.%d · %s" % (n, vi, n, en),
               8.8, color=INK, weight="600"))
    o.append(T(w / 2.0, 32, sub, 6.6, color=GREY))


def _strip(o, w, h, n, vi, en, note=None):
    y = h - 24 if note else h - 16
    o.append(T(w / 2.0, y,
               "Hình 5.%d · %s / Figure 5.%d · %s" % (n, vi, n, en),
               7.0, color=INK))
    if note:
        o.append(T(w / 2.0, h - 8, note, 6.2, color=GREY))


@_reg
def fig_f511():
    """Figure 5.11 - Hazardous area is a room with openings."""
    w, h = 680, 480
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, w, 11, "Khu vực nguy hiểm trong phòng có lỗ mở",
          "Hazardous area is a room with openings",
          "Mặt bằng; một nét gạch chéo = khu vực nguy hiểm / "
          "Plan view; single hatching = hazardous area")

    o.append(_line(120, 330, 500, 330, sw=1.2))
    o.append(T(500, 344, "Ground", 6.8, anchor="end", color=INK))

    # Hazardous lobes at the four vent positions (drawn behind the walls).
    o.append(_lobe(250, 130, 40))
    o.append(_lobe(410, 130, 40))
    o.append(_path("M 210 330 A 40 40 0 0 1 290 330 Z",
                   fill="url(#h6)", sw=1.0))
    o.append(_path("M 370 330 A 40 40 0 0 1 450 330 Z",
                   fill="url(#h6)", sw=1.0))

    # Building interior and thick walls.
    o.append(_rect(250, 130, 160, 200, fill="url(#h6)", sw=0))
    o.append(_line(250, 130, 410, 130, sw=2.4))
    o.append(_line(250, 130, 250, 330, sw=2.4))
    o.append(_line(410, 130, 410, 330, sw=2.4))

    # Vent markers.
    for vx, vy in ((258, 145), (402, 145), (258, 316), (402, 316)):
        o.append(T(vx, vy, "V", 7.0, color=INK))

    # Extent dimensions at the openings.
    for x1, y1, x2, y2, lx, ly in (
            (250, 130, 222, 102, 232, 106),
            (250, 130, 220, 156, 226, 163),
            (410, 130, 438, 102, 432, 100),
            (250, 330, 222, 302, 224, 296),
            (410, 330, 438, 302, 436, 296)):
        o.append(_dim(x1, y1, x2, y2))
        o.append(T(lx, ly, "a", 7.0, color=INK))

    o.append(_circle(330, 228, 3, fill=INK, sw=0))
    o.append(T(330, 206, "Source of", 7.2, color=INK))
    o.append(T(330, 216, "release", 7.2, color=INK))
    o.append(T(424, 232, "Building", 7.2, anchor="start", color=INK))

    legend = [
        "V = Vents (louvres or otherwise)",
        "a = Extent of hazardous area (Table 3.2) with a minimum of 0.5 m",
        "Hazardous area        Source of release",
        "Not acceptable        – Continuous grade",
        "Zone 1                – Primary grade",
        "Zone 2                – Secondary grade",
    ]
    for i, line in enumerate(legend):
        o.append(TP(120, 374 + i * 13, line, 6.6, anchor="start", color=INK))

    _strip(o, w, h, 11, "Khu vực nguy hiểm trong phòng có lỗ mở",
           "Hazardous area is a room with openings (with or without louvres)",
           "Chú thích in được giữ nguyên / Printed legend reproduced verbatim")

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt bằng tòa nhà có bốn lỗ thông hơi V ở bốn góc, mỗi lỗ có "
                    "thùy nguy hiểm gạch chéo đơn phía ngoài và kích thước a; "
                    "bên trong có nguồn phát thải và bảng chú thích in")),
                "Hình 5.11 Khu vực nguy hiểm trong một phòng có các lỗ mở "
                "(có hoặc không có cửa chớp).",
                "Figure 5.11 Hazardous area is a room with openings "
                "(with or without louvres)",
                "Mặt bằng tòa nhà có bốn lỗ thông hơi đánh dấu V tại bốn góc; "
                "phía ngoài mỗi lỗ là thùy khu vực nguy hiểm gạch chéo đơn "
                "với kích thước a. Nguồn phát thải nằm trong tòa nhà, có nhãn "
                "Building và Ground, kèm bảng chú thích in gồm sáu dòng.",
                "Plan view of a building with four vents marked V at the corners; "
                "outside each vent is a single-hatched hazardous lobe with "
                "dimension a. A source of release dot sits inside, with "
                "Building and Ground labels and a six-line printed legend.")


@_reg
def fig_f512():
    """Figure 5.12 - Secondary grade source with forced ventilation."""
    w, h = 680, 440
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, w, 12, "Nguồn phát thải cấp phụ với thông gió cưỡng bức",
          "Secondary grade source of release with forced ventilation",
          "Mặt cắt; gạch chéo đơn = bên trong tòa nhà / "
          "Elevation; single hatching = building interior")

    o.append(_line(150, 350, 480, 350, sw=1.2))
    o.append(T(480, 364, "Ground", 6.8, anchor="end", color=INK))

    o.append(_rect(210, 120, 220, 230, fill="url(#h6)", sw=0))
    o.append(_line(210, 120, 430, 120, sw=2.4))
    o.append(_line(210, 120, 210, 300, sw=2.4))
    o.append(_line(430, 120, 430, 350, sw=2.4))
    # Door leaf at the lower left.
    o.append(_line(210, 300, 188, 318, sw=1.4))

    # Extract duct rising through the roof.
    o.append(_path("M 350 120 L 350 92 Q 350 78 364 78 L 558 78",
                   fill="none", sw=1.4))
    o.append(_fan(500, 78))
    o.append(T(500, 96, "Fan", 6.6, color=INK))
    o.append(_arrow(562, 78, 606, 78, sw=1.1))
    o.append(T(608, 72, "Extract airflow", 6.0, anchor="start", color=INK))
    o.append(T(608, 82, "(Note 2)", 6.0, anchor="start", color=INK))

    # All aperture arrows point INTO the building.
    o.append(_arrow(172, 190, 206, 190, sw=1.0, head="a7"))
    o.append(T(166, 184, "(Note 1)", 6.4, anchor="end", color=INK))
    o.append(_arrow(466, 175, 434, 175, sw=1.0, head="a7"))
    o.append(T(470, 169, "Crack (Note 1)", 6.4, anchor="start", color=INK))
    o.append(_arrow(466, 295, 434, 295, sw=1.0, head="a7"))
    o.append(T(470, 289, "Air inlet (Note 1)", 6.4, anchor="start", color=INK))
    o.append(_arrow(172, 322, 206, 322, sw=1.0, head="a7"))
    o.append(T(166, 316, "Door", 6.4, anchor="end", color=INK))

    o.append(_circle(320, 245, 3, fill=INK, sw=0))
    o.append(T(320, 225, "Source of", 7.2, color=INK))
    o.append(T(320, 235, "hazard", 7.2, color=INK))
    o.append(T(230, 108, "Building", 7.2, anchor="start", color=INK))

    _strip(o, w, h, 12, "Nguồn cấp phụ với thông gió cưỡng bức",
           "Secondary grade source with forced ventilation",
           "Mũi tên tại mọi lỗ mở hướng vào trong / "
           "Arrows at all apertures point inward")

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt tòa nhà có bên trong gạch chéo đơn, nguồn phát thải, "
                    "ống dẫn mái với quạt và mũi tên thoát khí sang phải; các mũi "
                    "tên tại khe hở, cửa vào khí và cửa đi đều hướng vào trong")),
                "Hình 5.12 Nguồn phát thải cấp phụ với thông gió cưỡng bức. "
                "Ghi chú: (1) Thông gió hút đảm bảo luồng khí tại mọi lỗ mở "
                "đều hướng vào trong tòa nhà. (2) Lưu lượng khí hút đủ để pha "
                "loãng nguồn phát thải cấp phụ lớn nhất đến tỷ lệ yêu cầu của LEL.",
                "Figure 5.12 Secondary grade source of release with forced "
                "ventilation. Notes: (1) Extract ventilation ensures that airflow "
                "at all apertures will be into building. (2) Extract airflow "
                "sufficient to dilute maximum secondary grade source of release "
                "to required fraction of LEL",
                "Mặt cắt tòa nhà có bên trong gạch chéo đơn, một nguồn phát thải, "
                "ống dẫn qua mái với quạt và mũi tên Extract airflow hướng sang "
                "phải. Nhãn Crack, Air inlet, Door và (Note 1) ở các lỗ mở; mọi "
                "mũi tên ở lỗ mở đều hướng vào trong. Đường nét Ground ở dưới cùng.",
                "Elevation of a single-hatched building with a source of release, "
                "a roof duct, fan and rightward Extract airflow arrow. Crack, "
                "Air inlet and Door are labelled with (Note 1); every aperture "
                "arrow points inward. Ground runs along the base.")


@_reg
def fig_f513():
    """Figure 5.13 - Primary grade source with extract ventilation."""
    w, h = 680, 470
    o = [_cross_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, w, 13, "Nguồn phát thải cấp chính với thông gió hút",
          "Primary grade source of release with extract ventilation",
          "Mặt cắt; ô chéo chữ thập = Vùng 1 bên trong, gạch chéo đơn = Vùng 2 / "
          "Elevation; cross-hatched interior = Zone 1, single hatch = Zone 2")

    o.append(_line(150, 365, 470, 365, sw=1.2))
    o.append(T(470, 379, "Ground", 6.8, anchor="end", color=INK))

    o.append(_rect(200, 150, 240, 215, fill="url(#xh)", sw=0))
    o.append(_line(200, 150, 440, 150, sw=2.4))
    o.append(_line(200, 150, 200, 320, sw=2.4))
    o.append(_line(440, 150, 440, 365, sw=2.4))
    o.append(_line(200, 320, 178, 338, sw=1.4))

    # Extract duct, fan and discharge lobe.
    o.append(_path("M 360 150 L 360 122 Q 360 100 382 100 L 517 100",
                   fill="none", sw=1.4))
    o.append(_fan(505, 100))
    o.append(T(505, 116, "Fan", 6.6, color=INK))
    o.append(_lobe(545, 100, 28))
    o.append(T(552, 94, "a", 6.6, color=INK))
    o.append(_arrow(574, 100, 630, 100, sw=1.1))
    o.append(T(602, 92, "Extract air", 6.6, color=INK))
    o.append(T(578, 136, "(Note 2)", 6.4, color=INK))

    # Air inlets with inward arrows and hatched lobes.
    for cx, cy, ax, ay, lx, ly in (
            (200, 270, 160, 156, 154, 250),
            (440, 250, 480, 444, 486, 244),
            (440, 325, 480, 444, 486, 319)):
        o.append(_lobe(cx, cy, 26))
        o.append(T(cx - 12, cy - 4, "a", 6.6, color=INK))
        o.append(_arrow(ax, ay, ax + (36 if ax < cx else -36), ay,
                        sw=1.0, head="a7"))
        o.append(T(lx, ly, "Air inlet (Note 1)", 6.4,
                   anchor="end" if ax < cx else "start", color=INK))

    o.append(T(168, 350, "Door", 6.4, anchor="end", color=INK))
    o.append(T(190, 140, "Building", 7.0, anchor="end", color=INK))
    o.append(_circle(320, 260, 3, fill=INK, sw=0))
    o.append(T(320, 238, "Source of", 7.2, color=INK))
    o.append(T(320, 248, "release", 7.2, color=INK))

    o.append(TP(340, 404, "a = Table 3.2 but 0.5 m minimum", 7.0, color=INK))

    _strip(o, w, h, 13, "Nguồn cấp chính với thông gió hút",
           "Primary grade source with extract ventilation",
           "Bên trong là Vùng 1; thùy tại cửa xả và lỗ vào là Vùng 2 / "
           "Zone 1 inside; discharge and inlet lobes are Zone 2")

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt tòa nhà có bên trong ô chéo chữ thập là Vùng 1, "
                    "ống dẫn mái với quạt, thùy gạch chéo đơn tại cửa xả mang "
                    "kích thước a và các thùy tương tự tại cửa vào khí; mũi tên "
                    "hướng vào trong, có nhãn Door và Ground")),
                "Hình 5.13 Nguồn phát thải cấp chính với thông gió hút. "
                "Ghi chú: (1) Thông gió đảm bảo luồng khí hướng vào tòa nhà trong "
                "điều kiện vận hành bình thường, giới hạn Vùng 1 bên trong tòa nhà. "
                "(2) Trong điều kiện bất thường, hỗn hợp có khả năng nổ có thể thoát "
                "ra từ cửa xả ngoài các lỗ mở của tòa nhà.",
                "Figure 5.13 Primary grade source of release with extract "
                "ventilation. Notes: (1) Ventilation ensures airflow is into the "
                "building in normal operation restricting Zone 1 to inside "
                "building. (2) In abnormal circumstances explosive atmosphere may "
                "leak from extract vent in addition to building openings",
                "Mặt cắt tòa nhà có bên trong ô chéo chữ thập (Vùng 1) và nguồn "
                "phát thải. Ống dẫn mái có quạt, mũi tên Extract air và thùy "
                "gạch chéo đơn mang kích thước a tại cửa xả (Note 2). Ba cửa vào "
                "khí có thùy a và mũi tên hướng vào trong; có Door, Building, "
                "Ground và dòng chú thích a = Table 3.2 but 0.5 m minimum.",
                "Elevation with a cross-hatched (Zone 1) interior and a source dot. "
                "The roof duct carries a fan, an Extract air arrow and a "
                "single-hatched discharge lobe marked a (Note 2). Three air inlets "
                "have hatched lobes marked a with inward arrows; Door, Building, "
                "Ground and the legend a = Table 3.2 but 0.5 m minimum are shown.")


@_reg
def fig_f514():
    """Figure 5.14 - Effects of point source ventilation."""
    w, h = 680, 470
    o = [_cross_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, w, 14, "Ảnh hưởng của thông gió tại chỗ đối với nguồn điểm",
          "Effects of point source ventilation",
          "Mặt cắt; gạch chéo đơn = Vùng 2, ô chéo chữ thập = Vùng 0 (Vùng 1) / "
          "Elevation; single hatch = Zone 2, cross hatch = Zone 0 (Zone 1)")

    o.append(_line(170, 355, 500, 355, sw=1.2))
    o.append(T(500, 369, "Ground", 6.8, anchor="end", color=INK))

    o.append(_rect(210, 140, 240, 215, fill="url(#h6)", sw=0))
    o.append(_line(210, 140, 450, 140, sw=2.4))
    o.append(_line(210, 140, 210, 355, sw=2.4))
    o.append(_line(450, 140, 450, 355, sw=2.4))

    # Extract duct, fan and discharge lobe.
    o.append(_path("M 360 140 L 360 112 Q 360 85 387 85 L 497 85",
                   fill="none", sw=1.4))
    o.append(_fan(490, 85))
    o.append(T(405, 175, "Extract ventilation", 6.4, color=INK))
    o.append(_lobe(525, 85, 28))
    o.append(T(560, 112, "(Note 1)", 6.4, anchor="start", color=INK))

    # Hood over the cross-hatched liquid source.
    o.append(_path("M 300 278 L 370 278 L 358 252 L 312 252 Z",
                   fill=PAPER, sw=1.2))
    o.append(_rect(315, 280, 40, 40, fill="url(#xh)", sw=1.0))
    o.append(T(335, 307, "Liquid", 6.0, color=INK))
    o.append(T(292, 268, "Hood", 6.6, anchor="end", color=INK))
    o.append(T(378, 292, "(Note 2)", 6.4, anchor="start", color=INK))
    o.append(_arrow(340, 378, 340, 324, sw=0.8, color=GREY, head="a7"))

    # Hazardous lobes at wall openings.
    for cx, cy, lx, ly, anc in (
            (210, 285, 172, 278, "end"),
            (450, 245, 482, 239, "start"),
            (450, 320, 482, 314, "start")):
        o.append(_lobe(cx, cy, 24))
        o.append(T(lx, ly, "(Note 1)", 6.4, anchor=anc, color=INK))

    o.append(T(340, 385, "Continuous grade", 6.4, color=INK))
    o.append(T(340, 395, "source of release", 6.4, color=INK))

    _strip(o, w, h, 14, "Ảnh hưởng của thông gió điểm",
           "Effects of point source ventilation",
           "Chú thích (3) in: \"is restricted Table 3.2\" / "
           "Printed note (3) reads: \"is restricted Table 3.2\"")

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt tòa nhà có bên trong gạch chéo đơn, ống dẫn mái với "
                    "quạt và thùy nguy hiểm tại cửa xả; giữa nhà có chụp hút trên "
                    "ô vuông chất lỏng ô chéo chữ thập, các thùy (Note 1) ở lỗ mở "
                    "hai bên và nhãn Continuous grade source of release")),
                "Hình 5.14 Ảnh hưởng của thông gió tại chỗ đối với nguồn điểm. "
                "Ghi chú: (1) Bên trong tòa nhà và bên ngoài quanh các lỗ mở là "
                "Vùng 2 để tính đến trường hợp mất thông gió. (2) Khu vực ngay "
                "quanh nguồn phát thải cấp liên tục (hoặc cấp chính) là Vùng 0 "
                "(Vùng 1). (3) Khi nguồn là nguồn điểm và vận tốc thông gió tại "
                "chỗ là 2 m/s, Vùng 0 (Vùng 1) bị giới hạn Table 3.2 với giá trị "
                "nhỏ nhất 0.5 m",
                "Figure 5.14 Effects of point source ventilation. Notes: (1) "
                "Interior of building and exterior around openings are Zone 2 "
                "to take account of ventilation failure. (2) Immediate area around "
                "continuous (or primary) grade source of release is Zone 0 "
                "(Zone 1). (3) Where source is a point source and ventilation "
                "velocity local to it is 2 m/s Zone 0 (Zone 1) is restricted "
                "Table 3.2 with a minimum of 0.5 m",
                "Mặt cắt tòa nhà có bên trong gạch chéo đơn, ống dẫn mái với quạt "
                "và thùy nguy hiểm mang nhãn (Note 1). Chụp hút Hood nằm trên ô "
                "vuông Liquid ô chéo chữ thập, có nhãn (Note 2); các thùy (Note 1) "
                "ở lỗ mở hai bên. Nhãn Continuous grade source of release nằm dưới "
                "đường Ground.",
                "Elevation of a single-hatched building with a roof extract duct, "
                "fan and hatched discharge lobe (Note 1). A hood sits over a "
                "cross-hatched Liquid square labelled (Note 2); hatched lobes "
                "marked (Note 1) lie at the side openings. Continuous grade "
                "source of release is labelled below the Ground line.")


@_reg
def fig_f515():
    """Figure 5.15 - The paint-spray booth."""
    w, h = 680, 440
    o = [_cross_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, w, 15, "Buồng phun sơn", "The paint-spray booth",
          "Mặt cắt; thùy ngoài gạch chéo đơn = Vùng 2, bên trong ô chéo chữ thập "
          "= Vùng 1 / Elevation; outer single hatch = Zone 2, cross hatch = Zone 1")

    o.append(_line(110, 340, 610, 340, sw=1.2))
    o.append(T(610, 354, "Ground", 6.8, anchor="end", color=INK))

    # Zone 2 halo (3 m) and inner Zone 1 lobe (1 m) at the opening.
    o.append(_lobe(200, 150, 88))
    o.append(_lobe(200, 150, 30, cross=True))
    o.append(_dim(200, 150, 132, 102))
    o.append(T(156, 118, "3 m", 6.6, color=INK))
    o.append(_dim(200, 150, 174, 130))
    o.append(T(176, 108, "1 m", 6.6, color=INK))

    # Booth interior and rear grid A.
    o.append(_poly([(200, 150), (430, 150), (510, 340), (200, 340)],
                   fill="url(#xh)", sw=1.4, close=True))
    o.append(_line(430, 150, 430, 340, sw=1.2, dash="3 2"))
    o.append(T(430, 142, "A", 7.0, color=INK))
    o.append(T(430, 354, "A", 7.0, color=INK))

    # Duct rising from the rear to a fan and hatched outlet lobe.
    o.append(_path("M 470 250 L 470 122 Q 470 95 497 95 L 530 95",
                   fill="none", sw=1.4))
    o.append(_fan(515, 95))
    o.append(T(515, 116, "Fan", 6.6, color=INK))
    o.append(_lobe(560, 95, 30))
    o.append(_dim(560, 95, 586, 95))
    o.append(T(573, 86, "1 m", 6.4, color=INK))

    o.append(T(330, 356, "Spray booth", 7.0, color=INK))
    o.append(TP(340, 382, "A = Grid or mesh to increase eveness of airflow",
                7.0, color=INK))

    _strip(o, w, h, 15, "Buồng phun sơn", "The paint-spray booth",
           "Chú thích in giữ nguyên chữ \"eveness\" / Printed \"eveness\" retained")

    return _fig(svg(w, h, "".join(o), esc(
                    "Mặt cắt buồng phun sơn có bên trong ô chéo chữ thập, lưới "
                    "dọc phía sau đánh dấu A, thùy gạch chéo đơn 3 m và thùy nhỏ "
                    "1 m trước cửa mở, ống dẫn ra quạt và thùy gạch chéo 1 m ở "
                    "đầu ra, có nhãn Spray booth, Ground và chú thích A")),
                "Hình 5.15 Buồng phun sơn.",
                "Figure 5.15 The paint-spray booth",
                "Mặt cắt buồng phun sơn có bên trong ô chéo chữ thập và lưới dọc "
                "phía sau đánh dấu A ở đầu trên và đầu dưới. Trước cửa mở là thùy "
                "nguy hiểm gạch chéo đơn 3 m chứa thùy nhỏ 1 m. Ống dẫn từ phía "
                "sau đi lên qua quạt tới thùy tròn gạch chéo có kích thước 1 m; "
                "có nhãn Spray booth, Ground và chú thích A.",
                "Elevation of a paint-spray booth with a cross-hatched interior "
                "and a vertical rear grid marked A at top and bottom. Outside the "
                "opening is a single-hatched 3 m lobe containing a smaller 1 m "
                "lobe. A duct rises from the rear through a fan to a hatched "
                "circular outlet lobe marked 1 m; Spray booth, Ground and the "
                "grid legend A are shown.")
