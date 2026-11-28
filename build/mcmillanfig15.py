# -*- coding: utf-8 -*-
"""Vector redraws of Figures 15.1-15.2 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 15 "Protection concepts for
apparatus for dust risks".

The two drawings are simplified vector redraws of the rendered pages
p484 and p485. Printed English captions (including the inline Note of
Fig. 15.2), in-figure labels and printed quirks are retained verbatim:
the six ungasketted joint sections and their `A ≥ 5 mm`, `(X + Y) ≥ 5 mm`,
`B ≥ 3 mm` and `≥ 5 mm` dimensions, the three Notes, the gasketed and
‘o’ ring sections of Fig. 15.2 with `(X+Y) ≥ 3 mm`, and the lowercase `o`
inside curly single quotes (never a zero). Every displayed string is
literal Unicode with raw ampersands escaped. Each public callable returns
the standard five-tuple through ``vfig._fig()`` and is registered in
``FIGS`` by the ``_reg`` decorator.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=7.6, **kw):
    """Plain text: clamp into the 6.8-9.5 px contract, vet, delegate to vfig."""
    size = min(9.5, max(6.8, float(size)))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _dim_h(o, x1, x2, y, label, above=True):
    """Horizontal dimension with end ticks, arrowheads and a T() label."""
    o.append(_line(x1, y, x2, y, sw=0.9, color=INK))
    o.append(_line(x1, y - 4, x1, y + 4, sw=0.9, color=INK))
    o.append(_line(x2, y - 4, x2, y + 4, sw=0.9, color=INK))
    o.append(_arrow(x1 + 9, y, x1, y, sw=0.9, color=INK, head="a7"))
    o.append(_arrow(x2 - 9, y, x2, y, sw=0.9, color=INK, head="a7"))
    o.append(T((x1 + x2) / 2.0, y - 7 if above else y + 11, label, 6.8,
               color=INK, weight="600"))


def _dim_v(o, x, y1, y2, label):
    """Vertical dimension with end ticks, arrowheads and a T() label."""
    o.append(_line(x, y1, x, y2, sw=0.9, color=INK))
    o.append(_line(x - 4, y1, x + 4, y1, sw=0.9, color=INK))
    o.append(_line(x - 4, y2, x + 4, y2, sw=0.9, color=INK))
    o.append(_arrow(x, y1 + 9, x, y1, sw=0.9, color=INK, head="a7"))
    o.append(_arrow(x, y2 - 9, x, y2, sw=0.9, color=INK, head="a7"))
    o.append(T(x - 7, (y1 + y2) / 2.0 + 2.4, label, 6.8,
               anchor="end", color=INK, weight="600"))


def _notes(o, y, vi, en):
    """Bilingual lead-in followed by the verbatim printed English note."""
    o.append(T(45, y, vi, 6.8, anchor="start", color=INK))
    o.append(T(45, y + 12, en, 6.8, anchor="start", color=INK))


# ------------------------------------------------------------------ 15.1

@_reg
def fig_f1501():
    """Figure 15.1 - six ungasketted joint sections in three tiers."""
    w, h = 680, 452
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 16,
               "Hình 15.1 · Kích thước tối thiểu của mối nối không có gioăng",
               7.6, color=INK, weight="600"))
    o.append(T(340, 28,
               "Figure 15.1 · Minimum dimensions for ungasketted joints",
               7.6, color=INK, weight="600"))
    o.append(T(340, 41,
               "Mặt cắt · mối nối mặt bích, mối nối chốt/trụ/nón và mối nối ren / "
               "Sections · flanged, spigot, cylindrical, conical and threaded joints",
               6.8, color=GREY))

    # Tier 1 - two flanged sections with A and X/Y dust paths.
    for cx, stepped in ((175, False), (500, True)):
        o.append(_rect(cx - 58, 76, 116, 14, fill="url(#h6)", sw=1.0))
        o.append(_rect(cx - 17, 90, 34, 42, fill="url(#h6)", sw=1.0))
        if stepped:
            o.append(_line(cx, 76, cx, 90, sw=0.9, color=INK))
            o.append(_rect(cx - 7, 84, 14, 12, fill="#ffffff", sw=1.0))
            _dim_h(o, cx - 58, cx, 68, "X")
            _dim_h(o, cx, cx + 58, 68, "Y")
            o.append(T(cx, 146, "(X + Y) ≥ 5 mm", 7.2, color=INK))
        else:
            _dim_h(o, cx - 58, cx + 18, 68, "A")
            o.append(T(cx, 146, "A ≥ 5 mm", 7.2, color=INK))
        o.append(T(cx + 70, 84, "(Note)", 6.8, anchor="start", color=GREY))

    _notes(o, 165, "Ghi chú / Note :",
           "Joint faces to be as close as possible (no deliberate gap).")
    o.append(T(340, 193, "Mối nối mặt bích / Flanged joints", 7.4,
               color=INK, weight="600"))

    # Tier 2 - spigot, cylindrical and conical joints, each B >= 3 mm.
    for cx, kind in ((140, "spigot"), (340, "cylindrical"), (540, "conical")):
        if kind == "spigot":
            o.append(_rect(cx - 30, 208, 60, 8, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx - 13, 216, 26, 52, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx - 25, 216, 9, 52, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx + 16, 216, 9, 52, fill="url(#h6)", sw=1.0))
        elif kind == "cylindrical":
            o.append(_rect(cx - 28, 208, 56, 8, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx - 26, 216, 8, 52, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx + 18, 216, 8, 52, fill="url(#h6)", sw=1.0))
            o.append(_rect(cx - 14, 222, 7, 46, fill="#ffffff", sw=1.0))
            o.append(_rect(cx + 7, 222, 7, 46, fill="#ffffff", sw=1.0))
        else:
            o.append(_poly([(cx - 30, 216), (cx + 30, 216),
                            (cx + 22, 268), (cx - 22, 268)],
                           fill="url(#h6)", sw=1.0, close=True))
            o.append(_poly([(cx - 17, 208), (cx + 17, 208),
                            (cx + 10, 260), (cx - 10, 260)],
                           fill="#ffffff", sw=1.0, close=True))
        _dim_v(o, cx - 44, 216, 268, "B")
        o.append(T(cx, 282, "B ≥ 3 mm", 7.2, color=INK))
    for cx, lab in ((140, "Mối nối chốt / Spigot joint"),
                    (340, "Mối nối trụ / Cylindrical joint"),
                    (540, "Mối nối nón / Conical joint")):
        o.append(T(cx, 294, lab, 6.8, color=INK))

    _notes(o, 312, "Ghi chú / Note :",
           "Joint faces to be as close fitting as possible (interference fit).")

    # Tier 3 - the threaded joint and its three-engaged-threads Note.
    cx = 340
    _dim_h(o, cx - 42, cx + 42, 344, "≥ 5 mm")
    o.append(_rect(cx - 100, 354, 200, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(cx - 100, 394, 200, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(cx - 42, 364, 84, 30, fill="#ffffff", sw=1.0))
    zig = [(cx - 42 + i * 10.5, 364 if i % 2 == 0 else 369)
           for i in range(9)]
    o.append(_poly(zig, fill="none", sw=1.0, color=INK))
    o.append(_poly([(x, 394 if i % 2 == 0 else 389) for i, (x, _) in enumerate(zig)],
                   fill="none", sw=1.0, color=INK))
    o.append(T(cx, 412, "Mối nối ren / Threaded joint", 7.4,
               color=INK, weight="600"))
    _notes(o, 428, "Ghi chú / Note :", "Three full threads must be engaged.")

    return _fig(svg(w, h, "".join(o), esc("Fig 15.1")),
                "Hình 15.1 · Kích thước tối thiểu của mối nối không có gioăng",
                "Figure 15.1 · Minimum dimensions for ungasketted joints",
                "Sáu mặt cắt mối nối không dùng gioăng xếp thành ba hàng. Hàng trên gồm hai "
                "mối nối mặt bích, một mặt có ký hiệu A với kích thước A ≥ 5 mm, mặt kia có "
                "ký hiệu X và Y với (X + Y) ≥ 5 mm, kèm chú thích (Note) và ghi chú yêu cầu "
                "hai mặt mối nối sát nhau nhất có thể, không có khe hở cố ý; nhóm được gắn "
                "nhãn Flanged joints. Hàng giữa là ba mối nối chốt, trụ và nón, mỗi mối có "
                "chiều dài đường đi bụi B ≥ 3 mm và ghi chú phải lắp khít chặt, ép chặt; "
                "hàng dưới là mối nối ren có kích thước ≥ 5 mm với ghi chú phải ăn khớp ít "
                "nhất ba ren đầy đủ",
                "Six ungasketted joint sections arranged in three tiers. The upper tier has "
                "two flanged sections, one marked A with A ≥ 5 mm and one marked X and Y with "
                "(X + Y) ≥ 5 mm, each with a (Note) callout and a note that joint faces are to "
                "be as close as possible with no deliberate gap, grouped under Flanged joints. "
                "The middle tier shows spigot, cylindrical and conical joints, each with a B "
                "dimension of B ≥ 3 mm and a note requiring the closest fitting, interference "
                "fit. The lower tier is a threaded joint with a ≥ 5 mm dimension and a note "
                "that three full threads must be engaged")


# ------------------------------------------------------------------ 15.2

@_reg
def fig_f1502():
    """Figure 15.2 - two gasketed sections and one ‘o’ ring sealed section."""
    w, h = 680, 356
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 16,
               "Hình 15.2 · Sử dụng gioăng và vòng ‘o’",
               7.6, color=INK, weight="600"))
    o.append(T(340, 28, "Figure 15.2 · Use of gaskets and ‘o’ rings.",
               7.6, color=INK, weight="600"))
    o.append(T(340, 41,
               "Mặt cắt · hai mối nối có gioăng phẳng và một mối nối kín bằng vòng ‘o’ / "
               "Sections · two flat-gasket joints and one ‘o’ ring sealed joint",
               6.8, color=GREY))

    # Upper tier - two gasketed flanged sections.
    for cx, two in ((180, False), (500, True)):
        o.append(_rect(cx - 58, 72, 116, 14, fill="url(#h6)", sw=1.0))
        o.append(_rect(cx - 17, 86, 34, 52, fill="url(#h6)", sw=1.0))
        o.append(_rect(cx - 25, 82, 50, 8, fill="#555555", sw=1.0))
        if two:
            o.append(_line(cx, 72, cx, 86, sw=0.9, color=INK))
            o.append(_rect(cx - 6, 88, 12, 12, fill="#ffffff", sw=1.0))
            _dim_h(o, cx - 58, cx, 64, "X")
            _dim_h(o, cx, cx + 58, 64, "Y")
            o.append(T(cx, 150, "(X+Y) ≥ 3 mm", 7.2, color=INK))
        else:
            _dim_h(o, cx - 58, cx + 18, 64, "A")
            o.append(T(cx, 150, "A ≥ 3 mm", 7.2, color=INK))
        o.append(T(cx + 45, 118, "Gioăng / Gasket", 6.8,
                   anchor="start", color=INK))
        o.append(_arrow(cx + 43, 114, cx + 20, 86, sw=0.9,
                        color=INK, head="a7"))
    o.append(T(340, 166, "Mối nối có gioăng / Gasketed joints", 7.4,
               color=INK, weight="600"))

    # Lower tier - the ‘o’ ring sealed joint in its recess.
    cx = 340
    o.append(_rect(cx - 105, 196, 210, 14, fill="url(#h6)", sw=1.0))
    o.append(_rect(cx - 105, 244, 210, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(cx - 16, 210, 32, 34, fill="url(#h6)", sw=1.0))
    o.append(_rect(cx + 8, 210, 24, 12, fill="#ffffff", sw=1.0))
    o.append(_circle(cx + 20, 216, 8, fill="#555555", sw=1.0))
    o.append(T(cx + 52, 212, "Vòng ‘o’ / ‘o’ ring", 6.8,
               anchor="start", color=INK))
    o.append(_arrow(cx + 50, 209, cx + 29, 214, sw=0.9,
                    color=INK, head="a7"))
    o.append(T(cx, 278, "(no defined minimum dimension)", 6.8, color=INK))
    o.append(T(cx, 296, "Mối nối kín bằng vòng ‘o’ / ‘o’ ring sealed joints",
               7.4, color=INK, weight="600"))
    o.append(T(45, 314, "Ghi chú in / Printed Note:", 6.8,
               anchor="start", color=GREY))
    o.append(T(45, 326,
               "Gaskets must be secured to one face of joint and ‘o’ rings in slots "
               "(by adhesive or other means", 6.8, anchor="start", color=GREY))
    o.append(T(45, 338,
               "which does not adversely affect sealing of joint)",
               6.8, anchor="start", color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 15.2")),
                "Hình 15.2 · Sử dụng gioăng và vòng ‘o’. Ghi chú: Gioăng phải được cố định vào "
                "một mặt của mối nối, còn vòng ‘o’ phải nằm trong rãnh (bằng keo dán hoặc biện "
                "pháp khác không làm ảnh hưởng xấu đến khả năng làm kín của mối nối)",
                "Figure 15.2 · Use of gaskets and ‘o’ rings. Note: Gaskets must be secured to "
                "one face of joint and ‘o’ rings in slots (by adhesive or other means which "
                "does not adversely affect sealing of joint)",
                "Ba mặt cắt mối nối. Hai mặt cắt ở hàng trên là mối nối mặt bích có gioăng "
                "phẳng: mặt trái có ký hiệu A với kích thước A ≥ 3 mm, mặt phải có ký hiệu X và "
                "Y với (X+Y) ≥ 3 mm; cả hai có mũi tên chỉ vào lớp gioăng tối màu và được gộp "
                "dưới nhãn Gasketed joints. Mặt cắt ở hàng dưới là mối nối dùng vòng ‘o’ đặt "
                "trong rãnh, có mũi tên chỉ vào vòng, được ghi là không có kích thước tối thiểu "
                "xác định và mang nhãn ‘o’ ring sealed joints; cuối bản vẽ là Ghi chú in về "
                "việc cố định gioăng vào một mặt và đặt vòng ‘o’ trong rãnh",
                "Three joint sections. The upper two are flanged joints with flat gaskets: the "
                "left one is marked A with A ≥ 3 mm, the right one is marked X and Y with "
                "(X+Y) ≥ 3 mm; leader lines on both point to the dark gasket layer, and the "
                "pair is grouped under Gasketed joints. The lower section is an ‘o’ ring "
                "sealed joint whose ring sits in a recess, identified by a leader and the "
                "words (no defined minimum dimension), grouped under ‘o’ ring sealed joints. "
                "A printed Note footer repeats that gaskets must be secured to one face and "
                "‘o’ rings fitted in slots")
