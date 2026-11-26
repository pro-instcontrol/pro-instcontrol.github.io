# -*- coding: utf-8 -*-
"""Vector redraws of Figures 2.5 and 2.6 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 2.

Fig. 2.5 is the area-classification decision procedure and Fig. 2.6 the
extent-of-hazardous-areas procedure. Both are simplified bilingual VI/EN
SVG vectors, no raster art. Architecture mirrors `mcmillanfig01_b.py`:
each function returns the standard five-tuple through `vfig._fig()` and
is registered in `FIGS` by `_reg`.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _defs, _fig, _line, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


DEC = "#fff5e6"
PROC = "#eef3fb"
TERM = "#eef6ee"
NOTE = "#f7f3e8"


def _bi(o, x, y, w, h, vi, en, fill=PROC, vs=7.2, es=6.8, paren=True):
    """A bilingual box: Vietnamese lines first, then English lines in
    parentheses, both vertically centred inside an explicitly filled box."""
    vi = [vi] if isinstance(vi, str) else list(vi)
    en = [en] if isinstance(en, str) else list(en)
    lines_en = []
    for i, t in enumerate(en):
        if paren:
            if i == 0:
                t = "(" + t
            if i == len(en) - 1:
                t = t + ")"
        lines_en.append(t)
    o.append(_rect(x, y, w, h, fill=fill, sw=1.0))
    rows = [(t, vs, INK) for t in vi] + [(t, es, GREY) for t in lines_en]
    step = 8.6
    cy = y + h / 2.0 - (len(rows) - 1) * step / 2.0 + 2.2
    for i, (t, sz, col) in enumerate(rows):
        o.append(T(x + w / 2.0, cy + i * step, t, sz, color=col))


@_reg
def fig_f205():
    """Figure 2.5 - Area classification procedure for explosive atmospheres."""
    w, h = 680, 568
    o = [_defs()]
    o.append(T(340, 18,
               "Hình 2.5 · Quy trình phân loại khu vực / Area classification procedure",
               8.8, color=INK, weight="600"))
    o.append(T(340, 30, "Chương 2 · McMillan, Electrical Installations in Hazardous Areas",
               6.8, color=GREY))

    # First decision and its two outcomes.
    _bi(o, 30, 54, 330, 56,
        ["Quá trình có chứa nhiều hơn mức tối thiểu quy định", "về chất dễ cháy?"],
        ["Does the process contain more than a specified minimum", "of flammable material?"],
        fill=DEC)
    _bi(o, 424, 54, 230, 56,
        ["Có thể không cần phân loại khu vực,", "nhưng cần biện pháp phòng ngừa đặc biệt"],
        ["Area classification may not be necessary", "but special precautions may be needed"])
    o.append(_arrow(360, 82, 424, 82, sw=1.1))
    o.append(T(392, 74, "NO", 6.8, color=GREY))

    # Second decision and its two outcomes.
    _bi(o, 30, 140, 190, 38,
        ["Quá trình có thể thoát ra chất đó?"],
        ["Can it release it?"], fill=DEC)
    _bi(o, 424, 140, 190, 38,
        ["Khu vực không nguy hiểm"],
        ["Non-hazardous area"], fill=TERM)
    o.append(_arrow(125, 110, 125, 140, sw=1.1))
    o.append(T(141, 128, "YES", 6.8, color=GREY, anchor="start"))
    o.append(_arrow(220, 159, 424, 159, sw=1.1))
    o.append(T(252, 151, "NO", 6.8, color=GREY))

    # Grade of release.
    _bi(o, 30, 206, 250, 38,
        ["Xác định cấp độ thoát ra"],
        ["Determine the grade of release"])
    o.append(_arrow(125, 178, 125, 206, sw=1.1))
    o.append(T(141, 195, "YES", 6.8, color=GREY, anchor="start"))

    # Three release grades in parallel.
    o.append(_line(125, 244, 125, 258, sw=1.0))
    o.append(_line(88, 258, 364, 258, sw=1.0))
    for cx in (88, 226, 364):
        o.append(_arrow(cx, 258, cx, 272, sw=1.0))
    _bi(o, 30, 272, 116, 42, ["Liên tục (Vùng 0)"],
        ["Continuous (Zone 0)"], vs=7.0, paren=False)
    _bi(o, 168, 272, 116, 42, ["Sơ cấp (Vùng 1)"],
        ["Primary (Zone 1)"], vs=7.0, paren=False)
    _bi(o, 306, 272, 116, 42, ["Thứ cấp (Vùng 2)"],
        ["Secondary (Zone 2)"], vs=7.0, paren=False)

    # Can the grade be lowered?
    _bi(o, 30, 344, 392, 48,
        ["Có thể sửa đổi quá trình để giảm cấp độ thoát ra?"],
        ["Can the process be modified to give a lower grade of release?"],
        fill=DEC)
    for cx in (88, 226, 364):
        o.append(_arrow(cx, 314, cx, 344, sw=1.0))

    # NO branch: determine the hazardous area extent.
    _bi(o, 140, 422, 240, 44,
        ["Cần xác định phạm vi khu vực nguy hiểm"],
        ["Hazardous area extent requires determination"])
    o.append(_arrow(226, 392, 226, 422, sw=1.1))
    o.append(T(242, 409, "NO", 6.8, color=GREY))
    _bi(o, 190, 496, 140, 32, ["xem Hình 2.6"], ["see Fig. 2.6"],
        fill=TERM, vs=7.0)
    o.append(_arrow(260, 466, 260, 496, sw=1.1))

    # YES branch: loop back to grade determination, and the possible
    # non-hazardous outcome shown in the source figure.
    o.append(_line(422, 368, 600, 368, sw=1.1))
    o.append(_line(478, 368, 478, 232, sw=1.1))
    o.append(_arrow(478, 232, 282, 232, sw=1.1))
    o.append(_line(600, 368, 600, 200, sw=1.0))
    o.append(_line(600, 200, 519, 200, sw=1.0))
    o.append(_arrow(519, 200, 519, 178, sw=1.0))
    o.append(T(432, 360, "YES", 6.8, color=GREY, anchor="start"))

    o.append(T(340, 550,
               "Hình 2.5 · Quy trình phân loại khu vực đối với khí quyển nổ / "
               "Figure 2.5 · Area classification procedure for explosive atmospheres",
               6.6, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Lưu đồ phân loại khu vực: chất dễ cháy, khả năng thoát ra, "
                        "cấp độ Vùng 0 Vùng 1 Vùng 2 và xác định phạm vi nguy hiểm")),
                "Hình 2-5 · Quy trình phân loại khu vực đối với khí quyển nổ.",
                "Figure 2-5 · Area classification procedure for explosive atmospheres.",
                "Lưu đồ: quá trình có chất dễ cháy tối thiểu, có thoát ra được không. "
                "Nếu có, xác định cấp độ thoát ra gồm Liên tục Vùng 0, Sơ cấp Vùng 1, "
                "Thứ cấp Vùng 2; có thể giảm cấp độ thì quay lại xác định, không thì "
                "xác định phạm vi khu vực nguy hiểm, xem Hình 2.6.",
                "Flowchart: is flammable material present above a minimum and can it "
                "be released. If yes, determine the grade of release as Continuous "
                "Zone 0, Primary Zone 1 or Secondary Zone 2; if the grade can be "
                "lowered the path loops back, otherwise determine the hazardous area "
                "extent and see Figure 2.6.")


@_reg
def fig_f206():
    """Figure 2.6 - Extent of hazardous areas."""
    w, h = 680, 434
    o = [_defs()]
    o.append(T(340, 18,
               "Hình 2.6 · Phạm vi của các khu vực nguy hiểm / Extent of hazardous areas",
               8.8, color=INK, weight="600"))
    o.append(T(340, 30, "Chương 2 · McMillan, Electrical Installations in Hazardous Areas",
               6.8, color=GREY))

    # Entry point.
    _bi(o, 250, 44, 180, 48,
        ["Xác định khu vực nguy hiểm", "(xem Hình 2.5)"],
        ["Determination of hazardous areas", "(see Fig. 2.5)"], paren=False)
    o.append(_arrow(340, 92, 340, 126, sw=1.1))

    # Normal-operation release rate.
    _bi(o, 150, 126, 270, 58,
        ["Xác định tốc độ thoát chất dễ cháy trong điều kiện",
         "bình thường. Có thể giảm tốc độ này?"],
        ["Determine the rate of release of flammable material",
         "during normal operation. Can it be reduced?"], fill=DEC)
    _bi(o, 440, 120, 158, 70,
        ["Xác định khoảng cách đến dưới LEL", "dựa trên tốc độ thoát và",
         "các đặc tính khác"],
        ["Determine the distance to below the LEL", "based upon release rate and other",
         "characteristics"], vs=7.0)
    _bi(o, 618, 141, 56, 30,
        ["Phạm vi vùng"], ["Extent of Zone"], fill=TERM, vs=6.8)
    o.append(_arrow(420, 155, 440, 155, sw=1.1))
    o.append(T(430, 147, "NO", 6.8, color=GREY))
    o.append(_arrow(598, 155, 618, 155, sw=1.1))

    # Abnormal-operation release rate.
    _bi(o, 150, 232, 270, 58,
        ["Xác định tốc độ thoát chất dễ cháy trong điều kiện",
         "bất thường. Có thể giảm tốc độ này?"],
        ["Determine the rate of release of flammable material",
         "during abnormal operation. Can it be reduced?"], fill=DEC)
    _bi(o, 440, 226, 158, 70,
        ["Xác định khoảng cách đến dưới LEL", "dựa trên tốc độ thoát và",
         "các đặc tính khác"],
        ["Determine the distance to below the LEL", "based upon release rate and other",
         "characteristics"], vs=7.0)
    _bi(o, 618, 247, 56, 30,
        ["Phạm vi vùng"], ["Extent of Zone"], fill=TERM, vs=6.8)
    o.append(_arrow(285, 184, 285, 232, sw=1.1))
    o.append(_arrow(420, 261, 440, 261, sw=1.1))
    o.append(T(430, 253, "NO", 6.8, color=GREY))
    o.append(_arrow(598, 261, 618, 261, sw=1.1))

    # YES loops back to the top of each release-rate question.
    o.append(_line(150, 155, 44, 155, sw=1.0))
    o.append(_line(44, 155, 44, 112, sw=1.0))
    o.append(_line(44, 112, 270, 112, sw=1.0))
    o.append(_arrow(270, 112, 270, 126, sw=1.0))
    o.append(T(64, 148, "YES", 6.8, color=GREY, anchor="start"))
    o.append(_line(150, 261, 44, 261, sw=1.0))
    o.append(_line(44, 261, 44, 218, sw=1.0))
    o.append(_line(44, 218, 270, 218, sw=1.0))
    o.append(_arrow(270, 218, 270, 232, sw=1.0))
    o.append(T(64, 254, "YES", 6.8, color=GREY, anchor="start"))

    # Note callout, the only dashed line in the figure.
    o.append(_rect(30, 322, 340, 76, fill=NOTE, sw=0.8, stroke="#b9b0a0"))
    o.append(T(44, 340, "Lưu ý: nếu tốc độ thoát bất thường bằng hoặc nhỏ hơn", 6.8,
               anchor="start", color=INK))
    o.append(T(44, 351, "tốc độ thoát bình thường thì không cần Vùng 2.", 6.8,
               anchor="start", color=INK))
    o.append(T(44, 366, "Note: if the release rate during abnormal operation is", 6.8,
               anchor="start", color=GREY))
    o.append(T(44, 377, "equal to or less than that in normal operation,", 6.8,
               anchor="start", color=GREY))
    o.append(T(44, 388, "no Zone 2 is required.", 6.8,
               anchor="start", color=GREY))
    o.append(_poly([(370, 322), (370, 308), (500, 308), (500, 298)],
                   fill="none", sw=0.9, color=GREY, dash="3 3"))

    o.append(T(340, 420,
               "Hình 2.6 · Phạm vi của các khu vực nguy hiểm / "
               "Figure 2.6 · Extent of hazardous areas",
               6.6, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Lưu đồ xác định phạm vi khu vực nguy hiểm theo tốc độ thoát "
                        "bình thường và bất thường, khoảng cách dưới LEL")),
                "Hình 2-6 · Phạm vi của các khu vực nguy hiểm.",
                "Figure 2-6 · Extent of hazardous areas.",
                "Lưu đồ: bắt đầu từ xác định khu vực nguy hiểm. Xét tốc độ thoát chất "
                "dễ cháy trong điều kiện bình thường, nếu giảm được thì quay lại, "
                "nếu không thì tính khoảng cách dưới LEL và ra phạm vi vùng. Lặp lại "
                "cho điều kiện bất thường. Ghi chú: không cần Vùng 2 nếu tốc độ thoát "
                "bất thường bằng hoặc nhỏ hơn tốc độ bình thường.",
                "Flowchart: start from determination of hazardous areas. For the "
                "normal-operation release rate, a reducible rate loops back; if not, "
                "determine the distance to below the LEL and the extent of zone. "
                "Repeat for abnormal operation. Note that no Zone 2 is required "
                "when the abnormal release rate is equal to or less than the normal one.")
