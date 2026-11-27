# -*- coding: utf-8 -*-
"""Vector redraws of Figures 9.1-9.2 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 9 "Protection concepts 'm', 'o' and 'q'".

Both drawings are simplified vector redraws of the printed page images
(pdf pp.238 and 241).  Captions follow the printed wording with a bilingual
prefix; letter legends and numeric values are transcribed from the pages.
Architecture mirrors `mcmillanfig08.py`: each figure returns the standard
five-tuple through `vfig._fig()` and is registered in `FIGS` by the `_reg`
decorator, while the named callables `fig_f901()` and `fig_f902()` remain the
public API.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, BLUE, RED, GREEN, _arrow, _circle, _ellipse,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

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

def _defs9():
    """Arrow markers plus the hatch and pellet fills used by the sections."""
    return ('<defs>'
            '<marker id="a9" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a9s" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="hatch9" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#5f6b73" stroke-width="0.7"/>'
            '</pattern>'
            '<pattern id="pel9" width="7" height="7" patternUnits="userSpaceOnUse">'
            '<circle cx="2" cy="2" r="0.9" fill="#5f6b73"/>'
            '<circle cx="5" cy="5" r="0.9" fill="#5f6b73"/>'
            '</pattern>'
            '</defs>' % (INK, INK))


def _title9(o, n, vi, en, size=8.0):
    o.append(T(340, 15, "Hình 9.%d · %s / Figure 9.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub9(o, s, y=29, size=6.2):
    o.append(T(340, y, s, size, color=GREY))


def _wrap(s, n):
    out, cur = [], ""
    for w in str(s).split():
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= n:
            cur += " " + w
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def _legend_col(o, pairs, x, y0, size=5.8, maxchars=54, gap=2.6):
    """Render one column of letter legends; returns the next free y."""
    lh = size + 1.5
    yy = y0
    for letter, text in pairs:
        lines = _wrap(text, maxchars)
        o.append(T(x, yy, "%s = %s" % (letter, lines[0]), size,
                   anchor="start", color=INK))
        for j, ln in enumerate(lines[1:], 1):
            o.append(T(x + 7, yy + j * lh, ln, size,
                       anchor="start", color=INK))
        yy += lh * len(lines) + gap
    return yy


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a9s")


# ------------------------------------------------------------------ 9.1

@_reg
def fig_f901():
    """Figure 9.1 - breathing device to exclude water, letters A-E."""
    w, h = 680, 300
    o = [_defs9(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title9(o, 1, "Thiết bị thở loại trừ nước",
            "Breathing device to exclude water")
    _sub9(o, "Mặt cắt đứng · Vertical section · ký hiệu A–E / letters A–E", 29)

    # Enclosure wall A: two hatched segments with an opening for the device.
    o.append(_rect(64, 50, 40, 90, fill="url(#hatch9)", sw=1.2))
    o.append(_rect(64, 176, 40, 72, fill="url(#hatch9)", sw=1.2))
    # Gasket C between the wall edge and the holder flange at the top.
    o.append(_rect(104, 84, 8, 14, fill=INK, sw=0))
    # Desiccant holder D: side rails, top flange and bottom cap.
    o.append(_rect(112, 92, 6, 142, fill=PAPER, sw=1.1))
    o.append(_rect(146, 92, 6, 142, fill=PAPER, sw=1.1))
    o.append(_rect(108, 86, 48, 8, fill=PAPER, sw=1.1))
    o.append(_rect(108, 230, 48, 8, fill=PAPER, sw=1.1))
    # Desiccant column B, shown as a pellet-filled column.
    o.append(_rect(118, 96, 28, 134, fill="url(#pel9)", sw=0.9))

    # Downward-facing vent E: hollow tube turning down at the right.
    o.append(_path("M 152 100 L 244 100 Q 264 100 264 120 L 264 210",
                   fill="none", sw=1.8))
    o.append(_path("M 152 108 L 244 108 Q 256 108 256 120 L 256 204",
                   fill="none", sw=1.2))
    o.append(_line(256, 204, 264, 210, sw=1.2))

    # Printed letter callouts, kept clear of one another and of the legend.
    for letter, tx, ty, lx, ly in (
            ("A", 44, 70, 64, 74),
            ("B", 44, 168, 118, 164),
            ("C", 128, 62, 108, 88)):
        o.append(T(tx, ty, letter, 7.0, color=INK))
        o.append(_lead(tx + 4, ty + 2, lx, ly))
    o.append(T(188, 92, "D", 7.0, color=INK))
    o.append(_lead(192, 94, 152, 100))
    o.append(_lead(192, 94, 152, 214))
    o.append(T(300, 160, "E", 7.0, color=INK))
    o.append(_lead(296, 162, 264, 160))

    left = (("A", "Enclosure Wall"),
            ("B", "Desiccant"),
            ("C", "Gasket"),
            ("D", "Desiccant holder where all three parts are secured together "
                  "by welding, soldering, cementing or have interposing gaskets "
                  "to prevent moisture entry"),
            ("E", "Downward facing vent secured to desiccant holder by welding, "
                  "soldering or screwing"))
    _legend_col(o, left, 340, 58, size=5.8, maxchars=54)
    o.append(T(340, 158, "Note: The desiccant Holder is fixed to the enclosure",
               6.0, anchor="start", color=GREY))
    o.append(T(340, 170, "in a manner acceptable to BS/EN 50015 (1994)",
               6.0, anchor="start", color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Fig 9.1")),
                "Hình 9.1 · Ví dụ về thiết bị thở dùng để loại trừ nước. "
                "A = Thành vỏ bọc, B = Chất hút ẩm, C = Vòng đệm, "
                "D = Giá đỡ chất hút ẩm, trong đó cả ba phần được gắn kết với "
                "nhau bằng hàn, hàn thiếc, xi măng hoặc có các vòng đệm xen kẽ "
                "để ngăn hơi ẩm xâm nhập. E = Cửa thông hơi hướng xuống, được "
                "gắn vào giá đỡ chất hút ẩm bằng hàn, hàn thiếc hoặc vặn vít. "
                "Lưu ý: Giá đỡ chất hút ẩm được cố định vào vỏ bọc theo cách "
                "được BS/EN 50015 (1994) chấp nhận",
                "Figure 9.1 · Example of breathing device to exclude Water. "
                "A = Enclosure Wall, B = Desiccant, C = Gasket, D = Desiccant "
                "holder where all three parts are secured together by welding, "
                "soldering, cementing or have interposing gaskets to prevent "
                "moisture entry. E = Downward facing vent secured to desiccant "
                "holder by welding, soldering or screwing. Note: The desiccant "
                "Holder is fixed to the enclosure in a manner acceptable to "
                "BS/EN 50015 (1994)",
                "Mặt cắt đứng của thiết bị thở: thành vỏ bọc gạch chéo có chỗ "
                "hở giữa, cột chất hút ẩm nằm trong giá đỡ đi qua chỗ hở, vòng "
                "đệm ở đỉnh và ống thông hơi hình chữ J quay xuống ở bên phải; "
                "các ký hiệu A đến E được giải nghĩa trong chú thích",
                "Vertical section of the breathing device: the hatched "
                "enclosure wall is interrupted at the centre, a pellet-filled "
                "desiccant column in its holder passes through the opening, a "
                "gasket sits at the top and a J-shaped vent turns downward at "
                "the right; letters A to E are defined in the caption")


# ------------------------------------------------------------------ 9.2

@_reg
def fig_f902():
    """Figure 9.2 - leakage measuring technique with brass electrodes."""
    w, h = 680, 300
    o = [_defs9(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title9(o, 2, "Kỹ thuật đo rò rỉ", "Leakage measuring technique")
    _sub9(o, "Hai thanh dẫn cách điện · điện cực đồng thau / "
             "Two insulated bars · brass electrodes", 29)

    # Base slab in perspective beneath the two bars.
    o.append(_poly([(70, 214), (330, 126), (420, 166), (160, 254)],
                   fill="#f0ede5", sw=1.0, close=True))

    # Bar 1: front face, top face and right side (1 cm x 1 cm, 5 cm long).
    b1 = [(96, 180), (128, 190), (128, 214), (96, 204)]
    b1b = [(236, 118), (268, 128), (268, 152), (236, 142)]
    o.append(_poly([b1[0], b1[1], b1b[1], b1b[0]],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(_poly([b1[1], b1[2], b1b[2], b1b[1]],
                   fill="#f2f0ea", sw=1.2, close=True))
    o.append(_poly(b1, fill="#e8e4da", sw=1.2, close=True))

    # Bar 2, offset across the base.
    b2 = [(156, 202), (188, 212), (188, 236), (156, 226)]
    b2b = [(296, 140), (328, 150), (328, 174), (296, 164)]
    o.append(_poly([b2[0], b2[1], b2b[1], b2b[0]],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(_poly([b2[1], b2[2], b2b[2], b2b[1]],
                   fill="#f2f0ea", sw=1.2, close=True))
    o.append(_poly(b2, fill="#e8e4da", sw=1.2, close=True))

    # Brass electrode bands at the far ends, with the 0.5 cm gap between them.
    o.append(_poly([(208, 130), (240, 140), (268, 128), (236, 118)],
                   fill="#d9c48a", sw=1.0, close=True))
    o.append(_poly([(268, 152), (300, 162), (328, 150), (296, 140)],
                   fill="#d9c48a", sw=1.0, close=True))
    o.append(_line(270, 130, 270, 150, sw=0.7, color=GREY))
    o.append(_arrow(272, 132, 272, 148, sw=0.8, color=GREY, head="a9s"))
    o.append(_arrow(272, 148, 272, 132, sw=0.8, color=GREY, head="a9s"))

    # Upright electrode leads rising toward the measuring instrument.
    o.append(_rect(248, 56, 8, 78, fill="#e8e4da", sw=1.0))
    o.append(_rect(308, 78, 8, 78, fill="#e8e4da", sw=1.0))
    o.append(T(280, 42, "To measuring instrument", 6.8, weight="600"))
    o.append(_arrow(252, 54, 266, 48, sw=1.0, head="a9"))
    o.append(_arrow(312, 76, 298, 48, sw=1.0, head="a9"))

    # Printed callouts and dimensions.
    o.append(T(46, 142, "Insulated conductors", 6.4, anchor="start"))
    o.append(_lead(114, 146, 120, 184))
    o.append(_lead(114, 146, 176, 206))
    o.append(T(282, 118, "0.5 cm", 6.4))
    o.append(T(372, 170, "Brass electrodes", 6.4, anchor="start"))
    o.append(_lead(368, 172, 272, 134))
    o.append(_lead(368, 172, 306, 156))

    # 1 cm height and 1 cm width at the front end of bar 1.
    o.append(_line(82, 180, 82, 204, sw=0.8, color=GREY))
    o.append(_line(78, 180, 86, 180, sw=0.8, color=GREY))
    o.append(_line(78, 204, 86, 204, sw=0.8, color=GREY))
    o.append(T(76, 196, "1 cm", 6.4, anchor="end"))
    o.append(_line(96, 212, 128, 222, sw=0.8, color=GREY))
    o.append(_line(96, 208, 96, 216, sw=0.8, color=GREY))
    o.append(_line(128, 218, 128, 226, sw=0.8, color=GREY))
    o.append(T(112, 234, "1 cm", 6.4))

    # 5 cm length dimension below the bars.
    o.append(_line(158, 252, 158, 260, sw=0.8, color=GREY))
    o.append(_line(234, 252, 234, 260, sw=0.8, color=GREY))
    o.append(_arrow(160, 256, 232, 256, sw=0.8, color=GREY, head="a9s"))
    o.append(_arrow(232, 256, 160, 256, sw=0.8, color=GREY, head="a9s"))
    o.append(T(196, 248, "5 cm", 6.4))

    o.append(T(360, 206, "Notes: (1) Electrodes surrounded by filling material",
               6.0, anchor="start", color=GREY))
    o.append(T(360, 218, "to a depth of at least 1 cm in all directions",
               6.0, anchor="start", color=GREY))
    o.append(T(360, 230, "(2) Measuring instrument should apply 1000V dc.",
               6.0, anchor="start", color=GREY))
    o.append(T(360, 242, "to electrodes", 6.0, anchor="start", color=GREY))
    return _fig(svg(w, h, "".join(o), esc("Fig 9.2")),
                "Hình 9.2 · Kỹ thuật đo rò rỉ. Ghi chú: (1) Điện cực phải được "
                "bao quanh bởi vật liệu điền đầy có độ sâu ít nhất 1 cm theo mọi "
                "hướng. (2) Dụng cụ đo phải áp 1000V dc. vào các điện cực",
                "Figure 9.2 · Leakage Measuring Technique. Notes: (1) Electrodes "
                "should be surrounded by filling material with a depth of at "
                "least 1 cm in all directions. (2) Measuring instrument should "
                "apply 1000V dc. to electrodes",
                "Hình phối cảnh của hai thanh dẫn cách điện tiết diện 1 cm × 1 cm, "
                "dài 5 cm, đặt trên đế; ở đầu sau là hai điện cực đồng thau cách "
                "nhau 0,5 cm, hai cọc dẫn đứng lên trên có mũi tên hướng tới dụng "
                "cụ đo; các kích thước 1 cm, 5 cm và 0,5 cm được ghi rõ",
                "Perspective view of two insulated conducting bars of 1 cm × 1 cm "
                "section and 5 cm length resting on a base; brass electrodes at "
                "the far ends with a 0.5 cm gap, two upright posts carrying "
                "arrows towards the measuring instrument; dimensions 1 cm, 5 cm "
                "and 0.5 cm are shown")
