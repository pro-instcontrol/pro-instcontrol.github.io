# -*- coding: utf-8 -*-
"""Vector redraws of Figures 10.1-10.10 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 10 "Apparatus using protection
concept flameproof enclosure 'd'".

All ten drawings are simplified vector redraws of the rendered page images
(p249, p252-p255, p258, p260, p263 and p264).  Captions use the printed
English wording with a bilingual prefix; printed letter legends, dimensions
and sub-captions are transcribed onto the drawings.  Architecture mirrors
`mcmillanfig08.py` / `mcmillanfig09.py`: each figure returns the standard
five-tuple through `vfig._fig()` and is registered in `FIGS` by the `_reg`
decorator, while the named callables `fig_f1001()` ... `fig_f1010()` remain
the public API.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (INK, GREY, PAPER, _arrow, _circle, _fig, _line, _path,
                  _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode; escape raw ampersands."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _defs10():
    """Arrow markers and the diagonal hatch used by all the sections."""
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a6s" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="hatch10" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#66707a" stroke-width="0.7"/>'
            '</pattern>'
            '</defs>' % (INK, INK))


def _title(o, n, vi, en):
    o.append(T(340, 15, "Hình 10.%d · %s / Figure 10.%d · %s" % (n, vi, n, en),
               8.0, color=INK, weight="600"))


def _sub(o, s, y=29, size=6.3):
    o.append(T(340, y, s, size, color=GREY))


def _hatch(x, y, w, h, sw=1.0):
    return _rect(x, y, w, h, fill="url(#hatch10)", sw=sw)


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a6s")


def _carrow(d, sw=1.0, color=INK):
    """Curved flame jet with an arrowhead."""
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a6)"/>' % (d, color, sw))


def _dimh(x1, x2, y, lab, ly=None, size=6.2):
    """Horizontal dimension with inward-facing arrowheads."""
    o = [_line(x1, y - 5, x1, y + 5, sw=0.7, color=GREY),
         _line(x2, y - 5, x2, y + 5, sw=0.7, color=GREY),
         _line(x1, y, x2, y, sw=0.8, color=GREY),
         _arrow(x1 + 1, y, x1 + 10, y, sw=0.8, color=GREY, head="a6s"),
         _arrow(x2 - 1, y, x2 - 10, y, sw=0.8, color=GREY, head="a6s")]
    o.append(T((x1 + x2) / 2.0, ly if ly is not None else y - 5, lab, size))
    return "".join(o)


def _dimv(x, y1, y2, lab, lx=None, size=6.2):
    """Vertical dimension with inward-facing arrowheads."""
    o = [_line(x - 5, y1, x + 5, y1, sw=0.7, color=GREY),
         _line(x - 5, y2, x + 5, y2, sw=0.7, color=GREY),
         _line(x, y1, x, y2, sw=0.8, color=GREY),
         _arrow(x, y1 + 1, x, y1 + 10, sw=0.8, color=GREY, head="a6s"),
         _arrow(x, y2 - 1, x, y2 - 10, sw=0.8, color=GREY, head="a6s")]
    o.append(T(lx if lx is not None else x - 8, (y1 + y2) / 2.0 + 2, lab,
               size, anchor="end"))
    return "".join(o)


def _wavy(x, y, w, n=3):
    """Wavy section-break along the bottom of a wall."""
    d = "M %s %s" % (x, y)
    seg = w / float(n)
    for i in range(n):
        yy = y - 5 if i % 2 == 0 else y + 5
        d += " Q %s %s %s %s" % (x + (i + 0.5) * seg, yy, x + (i + 1) * seg, y)
    return _path(d, sw=1.0)


# ------------------------------------------------------------------ 10.1

@_reg
def fig_f1001():
    """Figure 10.1 - principle of operation: explosion and flange cooling."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Nguyên lý hoạt động của vỏ chống cháy",
           "Principle of operation of flameproof enclosure")
    _sub(o, "Mặt cắt · các mũi tên chỉ ngọn lửa thoát qua khe / "
             "Section · arrows show flame escaping through the gaps")

    # Hatched enclosure band with a hollow centre.
    o.append(_hatch(250, 72, 180, 14))
    o.append(_hatch(250, 164, 180, 14))
    o.append(_hatch(250, 86, 14, 78))
    o.append(_hatch(416, 86, 14, 78))

    # Irregular internal-explosion burst.
    burst = [(302, 108), (314, 98), (328, 106), (340, 94), (352, 106),
             (366, 100), (382, 112), (372, 126), (384, 138), (366, 144),
             (354, 158), (340, 148), (324, 158), (312, 144), (298, 138),
             (306, 124)]
    o.append(_poly(burst, fill="#ffffff", sw=1.2, close=True))
    o.append(T(340, 123, "Internal", 6.2))
    o.append(T(340, 133, "explosion", 6.2))

    # Flange protrusions with the narrow vertical slit (the flame path).
    o.append(_rect(234, 112, 16, 24, fill="#ffffff", sw=1.1))
    o.append(_line(242, 112, 242, 136, sw=1.0))
    o.append(_rect(430, 112, 16, 24, fill="#ffffff", sw=1.1))
    o.append(_line(438, 112, 438, 136, sw=1.0))

    # Five curved flame jets fanning out of each slit.
    for d in ("M 240 116 Q 216 104 204 90",
              "M 238 120 Q 212 114 196 106",
              "M 236 124 Q 208 124 190 124",
              "M 238 128 Q 212 134 196 142",
              "M 240 132 Q 216 144 204 158",
              "M 440 116 Q 464 104 476 90",
              "M 442 120 Q 468 114 484 106",
              "M 444 124 Q 472 124 490 124",
              "M 442 128 Q 468 134 484 142",
              "M 440 132 Q 464 144 476 158"):
        o.append(_carrow(d))

    # Printed callouts, kept clear of the jets and of one another.
    o.append(T(140, 58, "Initial cooling", 6.0))
    o.append(T(140, 68, "in flanges", 6.0))
    o.append(_lead(146, 72, 240, 116))
    o.append(T(340, 196, "Enclosure", 6.4))
    o.append(_lead(340, 190, 340, 170))
    o.append(T(120, 200, "Further cooling", 6.0))
    o.append(T(120, 210, "due to turbulent", 6.0))
    o.append(T(120, 220, "mixing at exit", 6.0))
    o.append(T(120, 230, "from flanges", 6.0))
    o.append(_lead(150, 194, 210, 156))
    o.append(T(520, 200, "Flame paths", 6.0))
    o.append(T(520, 210, "(defined minimum", 6.0))
    o.append(T(520, 220, "length and maximum gap)", 6.0))
    o.append(_lead(514, 194, 436, 130))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.1")),
                "Hình 10.1 · Nguyên lý hoạt động của vỏ chống cháy",
                "Figure 10.1 · Principle of operation of flameproof enclosure",
                "Mặt cắt vỏ bọc thành dày gạch chéo, bên trong là vệt nổ "
                "hình ngôi sao có nhãn Internal explosion; hai tai bích ở "
                "hai bên có khe hở và năm mũi tên cong phun ra ngoài; các "
                "nhãn Initial cooling in flanges, Enclosure, Further cooling "
                "due to turbulent mixing at exit from flanges và Flame paths "
                "(defined minimum length and maximum gap) có mũi tên chỉ tới "
                "vị trí tương ứng",
                "Section of a thick hatched enclosure with a star-shaped "
                "internal explosion burst; flange lugs on both sides carry "
                "narrow slits with five curved flame jets escaping; callouts "
                "Initial cooling in flanges, Enclosure, Further cooling due "
                "to turbulent mixing at exit from flanges and Flame paths "
                "(defined minimum length and maximum gap) point to the "
                "relevant features")


# ------------------------------------------------------------------ 10.2

@_reg
def fig_f1002():
    """Figure 10.2 - stepped lid over two walls, the basic flange joint."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Các mối nối mặt bích điển hình",
           "Typical flanged joints")
    _sub(o, "Mặt cắt · nắp bậc tạo mê cung / Section · stepped lid forming a labyrinth")

    # Stepped lid: outer lands rest on the walls, centre drops between them.
    o.append(_path("M 160 92 L 160 68 L 440 68 L 440 92 L 420 92 "
                   "L 420 112 L 180 112 L 180 92 Z", fill="#ffffff", sw=1.3))
    o.append(_rect(160, 92, 20, 100, fill="#ffffff", sw=1.3))
    o.append(_rect(420, 92, 20, 100, fill="#ffffff", sw=1.3))
    o.append(_wavy(160, 192, 20))
    o.append(_wavy(420, 192, 20))

    o.append(T(300, 62, "Lid", 7.0, weight="600"))
    o.append(T(300, 150, "Interior of", 6.6))
    o.append(T(300, 162, "enclosure", 6.6))
    o.append(T(520, 98, "Flame path", 6.0, anchor="start"))
    o.append(T(520, 108, "(flange joint of", 6.0, anchor="start"))
    o.append(T(520, 118, "specified 'L' minimum", 6.0, anchor="start"))
    o.append(T(520, 128, "length and maximum", 6.0, anchor="start"))
    o.append(T(520, 138, "gap)", 6.0, anchor="start"))
    o.append(_lead(514, 112, 424, 102))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.2")),
                "Hình 10.2 · Các mối nối mặt bích điển hình",
                "Figure 10.2 · Typical flanged joints",
                "Mặt cắt hai thành vỏ đứng với nắp bậc nằm lên trên; phần "
                "giữa của nắp hạ xuống giữa hai thành tạo mối nối mê cung, "
                "hai đầu thành có đường gãy lượn sóng; nhãn Lid, Interior of "
                "enclosure và Flame path (flange joint of specified 'L' "
                "minimum length and maximum gap) với mũi tên chỉ vào bậc nắp "
                "bên phải",
                "Section of two upright walls with a stepped lid resting on "
                "them; the lid centre drops between the walls to form a "
                "labyrinth joint and both wall ends have wavy section breaks; "
                "labels Lid, Interior of enclosure and Flame path (flange "
                "joint of specified 'L' minimum length and maximum gap) with "
                "an arrow to the right-hand step")


# ------------------------------------------------------------------ 10.3

@_reg
def fig_f1003():
    """Figure 10.3 - gasket outside and inside the flamepath."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Lắp vòng đệm vào mối nối mặt bích",
           "Fitting of gaskets to flanged joints")
    _sub(o, "Hai mặt cắt góc L · vòng đệm đen / Two L-section details · solid gasket")

    # Left detail - gasket outboard of the vertical joint face.
    o.append(_hatch(120, 112, 100, 14))
    o.append(_hatch(196, 126, 16, 74))
    o.append(_wavy(196, 200, 16, 2))
    o.append(_rect(164, 118, 10, 8, fill=INK, sw=0))
    o.append(_dimh(166, 196, 98, "L", ly=91))
    o.append(_dimv(106, 112, 126, "α", lx=98))
    o.append(T(130, 170, "Gasket", 6.0))
    o.append(_lead(136, 166, 169, 122))
    o.append(T(270, 150, "Enclosure", 6.2))
    o.append(T(270, 161, "interior", 6.2))
    o.append(T(180, 220, "Gasket outside flamepath", 6.0))

    # Right detail - gasket inboard at the foot of the joint face.
    o.append(_hatch(440, 112, 100, 14))
    o.append(_hatch(516, 126, 16, 74))
    o.append(_wavy(516, 200, 16, 2))
    o.append(_rect(516, 128, 10, 12, fill=INK, sw=0))
    o.append(_dimh(486, 516, 98, "L", ly=91))
    o.append(_dimv(426, 112, 126, "α", lx=418))
    o.append(T(450, 170, "Gasket", 6.0))
    o.append(_lead(456, 166, 521, 134))
    o.append(T(590, 150, "Enclosure", 6.2))
    o.append(T(590, 161, "interior", 6.2))
    o.append(T(500, 220, "Gasket inside flamepath", 6.0))

    o.append(T(340, 244, "L = Flamepath (minimum length)", 6.0))
    o.append(T(340, 256, "α = Flamepath (maximum gap) Table 10.2", 6.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.3")),
                "Hình 10.3 · Lắp vòng đệm vào mối nối mặt bích",
                "Figure 10.3 · Fitting of gaskets to flanged joints",
                "Hai mặt cắt góc L gạch chéo với nắp ngang và thành vỏ đứng; "
                "bên trái vòng đệm đen nằm trong rãnh phía ngoài khe hở, bên "
                "phải vòng đệm nằm ở chân mặt nối phía trong; kích thước L và "
                "khe hở α được chỉ bằng mũi tên hai đầu; chú giải L = "
                "Flamepath (minimum length), α = Flamepath (maximum gap) "
                "Table 10.2",
                "Two hatched L-sections with a horizontal lid flange and a "
                "vertical wall; the left detail seats a solid black gasket "
                "outboard of the joint face, the right detail seats it "
                "inboard at the foot of the joint; dimensions L and gap α "
                "are shown with double arrows; legend L = Flamepath (minimum "
                "length), α = Flamepath (maximum gap) Table 10.2")


# ------------------------------------------------------------------ 10.4

@_reg
def fig_f1004():
    """Figure 10.4 - clearance holes through the flange, two examples."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Ảnh hưởng của lỗ bu lông xuyên qua mặt bích",
           "Effects of boltholes through flanges")
    _sub(o, "Hai mặt cắt · bu lông và lỗ hở / Two sections · bolt and clearance hole")

    # Upper: wall with a horizontal flange, bolt head above.
    o.append(_hatch(350, 60, 20, 85))
    o.append(_wavy(350, 145, 20, 2))
    o.append(_hatch(240, 96, 110, 14))
    o.append(_rect(292, 77, 22, 64, fill="#ffffff", sw=1.0))
    o.append(_rect(286, 68, 26, 9, fill="#ffffff", sw=1.1))
    o.append(_rect(296, 77, 14, 60, fill="#ffffff", sw=1.0))
    o.append(_rect(286, 132, 26, 9, fill="#ffffff", sw=1.1))
    o.append(_dimh(240, 370, 58, "L", ly=51))
    o.append(_dimh(310, 350, 126, "l", ly=119))
    o.append(T(150, 78, "Clearance hole", 6.0))
    o.append(T(150, 88, "(see Table 10.3)", 6.0))
    o.append(_lead(180, 92, 300, 105))
    o.append(T(430, 120, "Enclosure", 6.2))
    o.append(T(430, 131, "interior", 6.2))

    # Lower: flange on a hatched block, bolt head below.
    o.append(_hatch(240, 170, 150, 14))
    o.append(_hatch(300, 184, 60, 40))
    o.append(_rect(296, 164, 14, 50, fill="#ffffff", sw=1.0))
    o.append(_rect(286, 214, 26, 9, fill="#ffffff", sw=1.1))
    o.append(T(420, 166, "Clearance holes", 6.0, anchor="start"))
    o.append(T(420, 176, "(see Table 10.3)", 6.0, anchor="start"))
    o.append(_lead(414, 178, 305, 180))
    o.append(_lead(414, 178, 317, 180))
    o.append(T(430, 204, "Enclosure", 6.2))
    o.append(T(430, 215, "interior", 6.2))
    o.append(_dimh(296, 330, 236, "l", ly=229))
    o.append(_dimh(240, 360, 250, "L", ly=243))

    o.append(T(520, 252, "L = Overall flamepath length (Table 10.1)", 5.8))
    o.append(T(520, 264, "l = Length to Bolthole (Table 10.2)", 5.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.4")),
                "Hình 10.4 · Ảnh hưởng của lỗ bu lông xuyên qua mặt bích",
                "Figure 10.4 · Effects of boltholes through flanges",
                "Mặt cắt trên: thành vỏ gạch chéo với mặt bích ngang, bu lông "
                "có đầu ở trên xuyên qua lỗ hở; mặt cắt dưới: mặt bích nằm "
                "trên khối gạch chéo, bu lông có đầu ở dưới; hai mũi tên "
                "Clearance hole (see Table 10.3) chỉ vào khe hở quanh thân "
                "bu lông; kích thước L và l cùng chú giải L = Overall "
                "flamepath length (Table 10.1), l = Length to Bolthole "
                "(Table 10.2)",
                "Upper section: hatched wall with a horizontal flange and a "
                "bolt with head above passing through the clearance hole; "
                "lower section: flange on a hatched block with the bolt head "
                "below; Clearance hole (see Table 10.3) leaders point to the "
                "annular gaps around the shank; dimensions L and l with "
                "legend L = Overall flamepath length (Table 10.1), l = "
                "Length to Bolthole (Table 10.2)")


# ------------------------------------------------------------------ 10.5

@_reg
def fig_f1005():
    """Figure 10.5 - blind threaded holes, bolt from inside and outside."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Lỗ ren trong thành vỏ bọc",
           "Threaded holes in enclosures walls")
    _sub(o, "Hai mặt cắt · vách còn lại sau lỗ ren / Two sections · residual wall")

    # Upper: bolt inserted from inside, blind hole stops short of the surface.
    o.append(_hatch(200, 52, 220, 60))
    o.append(_hatch(200, 52, 18, 80))
    o.append(_wavy(200, 132, 18, 2))
    o.append(_rect(250, 58, 36, 40, fill="#ffffff", sw=1.0))
    o.append(_rect(258, 66, 20, 34, fill="#ffffff", sw=1.0))
    o.append(_rect(252, 104, 32, 10, fill="#ffffff", sw=1.1))
    o.append(_rect(246, 98, 44, 16, fill="#ffffff", sw=1.0))
    o.append(T(470, 58, "Material thickness", 6.0, anchor="start"))
    o.append(T(470, 68, "at least in accordance", 6.0, anchor="start"))
    o.append(T(470, 78, "with Table 10.4", 6.0, anchor="start"))
    o.append(_lead(464, 74, 274, 56))
    o.append(T(330, 124, "Inside of", 6.2))
    o.append(T(330, 135, "enclosure", 6.2))
    o.append(_dimh(258, 286, 122, "l", ly=115))
    o.append(_dimh(200, 286, 140, "L", ly=133))

    # Lower: bolt inserted from outside, residual triangular material.
    o.append(_hatch(200, 158, 220, 52))
    o.append(_hatch(200, 158, 18, 72))
    o.append(_wavy(200, 230, 18, 2))
    o.append(_rect(250, 158, 36, 40, fill="#ffffff", sw=1.0))
    o.append(_rect(258, 158, 20, 36, fill="#ffffff", sw=1.0))
    o.append(_rect(252, 148, 32, 10, fill="#ffffff", sw=1.1))
    o.append(_poly([(270, 198), (302, 198), (302, 212)],
                   fill="url(#hatch10)", sw=1.0, close=True))
    o.append(T(470, 170, "Material thickness", 6.0, anchor="start"))
    o.append(T(470, 180, "at least in accordance", 6.0, anchor="start"))
    o.append(T(470, 190, "with Table 10.4", 6.0, anchor="start"))
    o.append(_lead(464, 186, 292, 206))
    o.append(T(340, 222, "Inside of", 6.2))
    o.append(T(340, 233, "enclosure", 6.2))
    o.append(_dimh(258, 286, 224, "l", ly=217))
    o.append(_dimh(200, 286, 242, "L", ly=235))

    o.append(T(500, 256, "L = Overall flamepath length (Table 10.1)", 5.8))
    o.append(T(500, 266, "l = Length to bolthole (Table 10.2)", 5.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.5")),
                "Hình 10.5 · Lỗ ren trong thành vỏ bọc",
                "Figure 10.5 · Threaded holes in enclosures walls",
                "Hai mặt cắt vỏ bọc gạch chéo có lỗ ren mù: mặt cắt trên bu "
                "lông lắp từ bên trong, đầu bu lông ở dưới; mặt cắt dưới bu "
                "lông lắp từ bên ngoài, đầu bu lông ở trên và vùng vật liệu "
                "còn lại hình tam giác; mũi tên Material thickness at least "
                "in accordance with Table 10.4 chỉ vào vách còn lại; kích "
                "thước L và l ở dưới mỗi mặt cắt",
                "Two hatched enclosure sections with blind threaded holes: "
                "the upper bolt is inserted from inside with its head below; "
                "the lower bolt is inserted from outside with its head above "
                "and a triangular residual-material region; Material "
                "thickness at least in accordance with Table 10.4 leaders "
                "point to the remaining wall; dimensions L and l below each "
                "section")


# ------------------------------------------------------------------ 10.6

@_reg
def fig_f1006():
    """Figure 10.6 - internal and external spigot joints."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 6, "Mối nối mở rộng bên trong và bên ngoài",
           "Internal and external spigot joints")
    _sub(o, "Hai mặt cắt gạch chéo · a = chiều dài mở rộng, b = chiều dài mặt bích / "
             "a = spigot length, b = flange length")

    # Internal spigot.
    o.append(_hatch(170, 48, 280, 14))
    o.append(_hatch(170, 62, 14, 58))
    o.append(_wavy(170, 120, 14, 2))
    o.append(_hatch(228, 62, 50, 10))
    o.append(_hatch(266, 72, 12, 38))
    o.append(_hatch(266, 110, 40, 10))
    o.append(_dimh(170, 228, 46, "b", ly=39))
    o.append(_dimv(142, 62, 120, "a", lx=134))
    o.append(T(110, 60, "Flange", 6.0))
    o.append(_lead(116, 62, 196, 66))
    o.append(T(410, 60, "Spigot", 6.0))
    o.append(_lead(406, 62, 252, 54))
    o.append(T(350, 84, "Inside of", 6.0))
    o.append(T(350, 95, "enclosure", 6.0))
    o.append(_arrow(226, 68, 234, 68, sw=0.8, color=GREY, head="a6s"))
    o.append(_arrow(226, 82, 226, 74, sw=0.8, color=GREY, head="a6s"))
    o.append(T(340, 136, "Internal spigot", 6.4, weight="600"))

    # External spigot.
    o.append(_hatch(170, 150, 280, 14))
    o.append(_hatch(170, 164, 16, 36))
    o.append(_hatch(300, 164, 14, 58))
    o.append(_wavy(300, 222, 14, 2))
    o.append(_dimh(170, 300, 148, "b", ly=141))
    o.append(_dimv(142, 164, 200, "a", lx=134))
    o.append(T(410, 158, "Flange", 6.0))
    o.append(_lead(406, 160, 330, 156))
    o.append(T(110, 158, "Spigot", 6.0))
    o.append(_lead(116, 160, 178, 180))
    o.append(T(350, 190, "Inside of", 6.0))
    o.append(T(350, 201, "enclosure", 6.0))
    o.append(_arrow(298, 166, 306, 166, sw=0.8, color=GREY, head="a6s"))
    o.append(_arrow(306, 180, 306, 172, sw=0.8, color=GREY, head="a6s"))
    o.append(T(340, 238, "External spigot", 6.4, weight="600"))

    o.append(T(340, 254, "a = Length of spigot", 6.0))
    o.append(T(340, 266, "b = Length of flange", 6.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.6")),
                "Hình 10.6 · Mối nối mở rộng bên trong và bên ngoài",
                "Figure 10.6 · Internal and external spigot joints",
                "Hai mặt cắt gạch chéo xếp dọc: mặt cắt trên là mối nối mở "
                "rộng bên trong với chân mở rộng đi xuống ở trái, mặt cắt "
                "dưới là mối nối mở rộng bên ngoài với chân mở rộng ngắn ở "
                "trái và thành vỏ đứng ở giữa; mũi tên Flange và Spigot, "
                "kích thước a và b, nhãn Inside of enclosure; chú giải a = "
                "Length of spigot, b = Length of flange",
                "Two hatched sections stacked vertically: the upper internal "
                "spigot has a downward male leg at the left, the lower "
                "external spigot has a short male block at the left and a "
                "tall enclosure wall near the middle; Flange and Spigot "
                "leaders, dimensions a and b, Inside of enclosure labels; "
                "legend a = Length of spigot, b = Length of flange")


# ------------------------------------------------------------------ 10.7

@_reg
def fig_f1007():
    """Figure 10.7 - practical spigot joint with a chamfer or radius."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 7, "Thiết kế thực tế của mối nối mở rộng",
           "Practical execution of spigot joint")
    _sub(o, "Hai mặt cắt · góc vát hoặc bán kính trên phần male / "
             "chamfer or radius on the male right angle")

    # Internal spigot with chamfer.
    o.append(_hatch(170, 50, 280, 14))
    o.append(_hatch(170, 64, 14, 56))
    o.append(_wavy(170, 120, 14, 2))
    o.append(_hatch(228, 64, 50, 10))
    o.append(_hatch(266, 74, 12, 36))
    o.append(_hatch(266, 110, 40, 10))
    o.append(_line(228, 64, 236, 72, sw=1.2))
    o.append(_dimh(170, 228, 48, "b", ly=41))
    o.append(_dimv(142, 64, 120, "a", lx=134))
    o.append(T(105, 58, "Flange", 6.0))
    o.append(_lead(111, 60, 196, 68))
    o.append(T(420, 44, "Chamfer or radius", 6.0))
    o.append(_lead(416, 46, 234, 66))
    o.append(T(400, 108, "Spigot", 6.0))
    o.append(_lead(396, 110, 272, 94))
    o.append(T(108, 76, "f", 6.0))
    o.append(_lead(112, 78, 230, 70))
    o.append(T(300, 58, "f", 6.0))
    o.append(_lead(298, 60, 240, 76))
    o.append(T(350, 84, "Interior of", 6.0))
    o.append(T(350, 95, "enclosure", 6.0))
    o.append(T(340, 134, "Internal spigot", 6.2, weight="600"))

    # External spigot, mirror case.
    o.append(_hatch(170, 146, 280, 14))
    o.append(_hatch(170, 160, 16, 38))
    o.append(_hatch(300, 160, 14, 58))
    o.append(_wavy(300, 218, 14, 2))
    o.append(_line(300, 160, 292, 168, sw=1.2))
    o.append(_dimh(170, 300, 144, "b", ly=137))
    o.append(_dimv(142, 160, 218, "a", lx=134))
    o.append(T(410, 154, "Flange", 6.0))
    o.append(_lead(406, 156, 330, 152))
    o.append(T(420, 180, "Chamfer or radius", 6.0))
    o.append(_lead(416, 182, 296, 166))
    o.append(T(105, 178, "Spigot", 6.0))
    o.append(_lead(111, 180, 178, 186))
    o.append(T(108, 158, "f", 6.0))
    o.append(_lead(112, 160, 294, 164))
    o.append(T(250, 158, "f", 6.0))
    o.append(_lead(248, 160, 282, 170))
    o.append(T(350, 192, "Interior of", 6.0))
    o.append(T(350, 203, "enclosure", 6.0))
    o.append(T(340, 232, "External spigot", 6.2, weight="600"))

    o.append(T(80, 240, "a = Actual length of cylindrical part to chamfer or radius",
               5.4, anchor="start"))
    o.append(T(80, 247, "b = Actual length of plane part to chamfer or radius",
               5.4, anchor="start"))
    o.append(T(80, 254, "f = Maximum encroachment of chamfer or radius into plane and",
               5.4, anchor="start"))
    o.append(T(86, 261, "cylindrical part (1 mm max) (e.g., in these examples",
               5.4, anchor="start"))
    o.append(T(86, 268, "width of wall = b+f)", 5.4, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.7")),
                "Hình 10.7 · Thiết kế thực tế của mối nối mở rộng",
                "Figure 10.7 · Practical execution of spigot joint",
                "Hai mặt cắt gạch chéo giống Fig. 10.6 nhưng góc vuông của "
                "phần male được vát tròn; nhãn Flange, Chamfer or radius, "
                "Spigot, Interior of enclosure và hai ký hiệu f với mũi tên "
                "chỉ vào phần lấn của góc vát; kích thước a, b; chú giải a, "
                "b, f với f tối đa 1 mm và width of wall = b+f",
                "Two hatched sections like Fig. 10.6 but with the male right "
                "angle chamfered or rounded; labels Flange, Chamfer or "
                "radius, Spigot, Interior of enclosure and two f callouts "
                "pointing to the chamfer encroachment; dimensions a and b; "
                "legend a, b, f with f 1 mm max and width of wall = b+f")


# ------------------------------------------------------------------ 10.8

@_reg
def fig_f1008():
    """Figure 10.8 - three '0' ring gasket arrangements."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 8, "Bố trí vòng đệm kiểu '0' ring",
           "Arrangement of '0' ring type gasket")
    _sub(o, "Ba mặt cắt góc L · vòng tròn nhỏ trong rãnh / Three L-sections · small ring in a groove")

    # Left: '0' ring in the flange, outside the flamepath.
    o.append(_hatch(75, 68, 90, 12))
    o.append(_hatch(150, 80, 14, 70))
    o.append(_wavy(150, 150, 14, 2))
    o.append(_rect(105, 72, 12, 8, fill="#ffffff", sw=1.0))
    o.append(_circle(111, 76, 3.5, fill="#ffffff", sw=1.1))
    o.append(T(105, 52, "'0' ring", 6.0))
    o.append(_lead(109, 54, 111, 72))
    o.append(T(40, 96, "Flamepath", 6.0, anchor="start"))
    o.append(_lead(96, 98, 158, 100))
    o.append(T(230, 100, "Enclosure", 6.0))
    o.append(T(230, 111, "interior", 6.0))
    o.append(T(130, 170, "'0' ring in flange outside flamepath", 5.8))

    # Middle: '0' ring in the spigot, outside the flamepath.
    o.append(_hatch(285, 68, 90, 12))
    o.append(_hatch(360, 80, 14, 70))
    o.append(_wavy(360, 150, 14, 2))
    o.append(_rect(360, 100, 14, 14, fill="#ffffff", sw=1.0))
    o.append(_circle(367, 107, 3.5, fill="#ffffff", sw=1.1))
    o.append(T(330, 52, "'0' ring", 6.0))
    o.append(_lead(334, 54, 367, 103))
    o.append(T(250, 124, "Flamepath", 6.0, anchor="start"))
    o.append(_lead(306, 126, 368, 92))
    o.append(T(440, 100, "Enclosure", 6.0))
    o.append(T(440, 111, "interior", 6.0))
    o.append(T(340, 170, "'0' ring in spigot outside flamepath", 5.8))

    # Right: '0' ring in the spigot, inside the flamepath.
    o.append(_hatch(495, 68, 90, 12))
    o.append(_hatch(570, 80, 14, 70))
    o.append(_wavy(570, 150, 14, 2))
    o.append(_rect(570, 90, 14, 14, fill="#ffffff", sw=1.0))
    o.append(_circle(577, 97, 3.5, fill="#ffffff", sw=1.1))
    o.append(T(500, 52, "Flamepath", 6.0, anchor="start"))
    o.append(_lead(556, 54, 576, 88))
    o.append(T(470, 124, "'0' ring", 6.0, anchor="start"))
    o.append(_lead(526, 126, 577, 99))
    o.append(T(640, 100, "Enclosure", 6.0))
    o.append(T(640, 111, "interior", 6.0))
    o.append(T(550, 170, "'0' ring in spigot inside flamepath", 5.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.8")),
                "Hình 10.8 · Bố trí vòng đệm kiểu '0' ring",
                "Figure 10.8 · Arrangement of '0' ring type gasket",
                "Ba mặt cắt góc L gạch chéo, mỗi mặt có vòng tròn nhỏ trong "
                "rãnh và nhãn Enclosure interior: bên trái vòng nằm trong "
                "mặt bích ngoài khe hở, giữa vòng nằm trong phần mở rộng "
                "ngoài khe hở, phải vòng nằm trong phần mở rộng bên trong "
                "khe hở; mũi tên ‘0’ ring và Flamepath; nhãn dưới từng mặt "
                "cắt theo bản in",
                "Three hatched L-sections, each with a small ring in a groove "
                "and an Enclosure interior label: left the ring lies in the "
                "flange outside the flamepath, middle it lies in the spigot "
                "outside the flamepath, right it lies in the spigot inside "
                "the flamepath; '0' ring and Flamepath leaders; printed "
                "sub-caption beneath each view")


# ------------------------------------------------------------------ 10.9

@_reg
def fig_f1009():
    """Figure 10.9 - flat compressible gasket arrangements."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 9, "Bố trí vòng đệm phẳng nén được",
           "Arrangement for flat compressible gaskets")
    _sub(o, "Hai mặt cắt gạch chéo · vòng đệm là hình chữ nhật đen / "
             "gasket drawn as a solid black rectangle")

    # Left: gasket outside the flamepath.
    o.append(_hatch(110, 70, 110, 12))
    o.append(_hatch(200, 82, 14, 80))
    o.append(_wavy(200, 162, 14, 2))
    o.append(_rect(150, 74, 14, 8, fill=INK, sw=0))
    o.append(T(100, 54, "Gasket", 6.0, anchor="start"))
    o.append(_lead(146, 56, 157, 76))
    o.append(T(60, 110, "Flamepath", 6.0, anchor="start"))
    o.append(_lead(116, 112, 208, 108))
    o.append(T(270, 110, "Enclosure", 6.0))
    o.append(T(270, 121, "interior", 6.0))
    o.append(T(180, 182, "Gasket outside flamepath", 6.0))

    # Right: gasket inside the flamepath in the cylindrical part.
    o.append(_hatch(430, 70, 110, 12))
    o.append(_hatch(520, 82, 14, 80))
    o.append(_wavy(520, 162, 14, 2))
    o.append(_rect(520, 100, 14, 10, fill=INK, sw=0))
    o.append(T(400, 100, "Flamepath", 6.0, anchor="start"))
    o.append(_lead(456, 102, 528, 94))
    o.append(T(430, 140, "Gasket", 6.0, anchor="start"))
    o.append(_lead(474, 142, 527, 106))
    o.append(T(590, 110, "Enclosure", 6.0))
    o.append(T(590, 121, "interior", 6.0))
    o.append(T(500, 182, "Gasket inside flamepath", 6.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.9")),
                "Hình 10.9 · Bố trí vòng đệm phẳng nén được",
                "Figure 10.9 · Arrangement for flat compressible gaskets",
                "Hai mặt cắt góc L gạch chéo với vòng đệm là hình chữ nhật "
                "đen: bên trái vòng nằm trên mặt bích ngoài khe hở, bên phải "
                "vòng nằm trong phần trụ bên trong khe hở; mũi tên Gasket và "
                "Flamepath, nhãn Enclosure interior; nhãn dưới mặt cắt Gasket "
                "outside flamepath và Gasket inside flamepath",
                "Two hatched L-sections with the gasket drawn as a solid "
                "black rectangle: left the gasket lies in the plane part "
                "outside the flamepath, right it lies in the cylindrical "
                "part inside the flamepath; Gasket and Flamepath leaders, "
                "Enclosure interior labels; sub-captions Gasket outside "
                "flamepath and Gasket inside flamepath")


# ------------------------------------------------------------------ 10.10

@_reg
def fig_f1010():
    """Figure 10.10 - boltholes on composite spigot joints, three views."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 10, "Ảnh hưởng của lỗ bu lông lên mối nối",
           "Effects of boltholes on joints")
    _sub(o, "Ba mặt cắt · bu lông xuyên qua phần mặt bích / "
             "bolt passing through the plane part")

    # Upper-left: head above, short hatched leg at the far left.
    o.append(_hatch(90, 58, 120, 12))
    o.append(_hatch(90, 70, 12, 40))
    o.append(_rect(140, 48, 20, 8, fill="#ffffff", sw=1.1))
    o.append(_rect(146, 56, 8, 40, fill="#ffffff", sw=1.0))
    o.append(_dimh(110, 160, 52, "b", ly=45))
    o.append(_dimv(70, 72, 110, "a", lx=62))
    o.append(T(58, 52, "f", 6.0))
    o.append(_lead(62, 54, 96, 70))
    o.append(T(58, 90, "f", 6.0))
    o.append(_lead(62, 92, 104, 80))
    o.append(T(150, 84, "l", 6.0))
    o.append(_arrow(138, 76, 145, 76, sw=0.8, color=GREY, head="a6s"))
    o.append(_arrow(155, 76, 148, 76, sw=0.8, color=GREY, head="a6s"))
    o.append(T(188, 100, "Inside of", 6.0))
    o.append(T(188, 111, "enclosure", 6.0))

    # Upper-right: head below, hatched wall at the left.
    o.append(_hatch(370, 58, 120, 12))
    o.append(_hatch(370, 70, 14, 50))
    o.append(_rect(420, 94, 20, 8, fill="#ffffff", sw=1.1))
    o.append(_rect(426, 58, 8, 38, fill="#ffffff", sw=1.0))
    o.append(_dimh(390, 450, 52, "b", ly=45))
    o.append(_dimv(470, 70, 110, "a", lx=478))
    o.append(T(386, 68, "f", 6.0))
    o.append(_lead(390, 70, 374, 74))
    o.append(T(410, 68, "f", 6.0))
    o.append(_lead(414, 70, 388, 76))
    o.append(T(390, 84, "l", 6.0))
    o.append(_arrow(380, 76, 387, 76, sw=0.8, color=GREY, head="a6s"))
    o.append(_arrow(397, 76, 390, 76, sw=0.8, color=GREY, head="a6s"))
    o.append(T(510, 100, "Inside of", 6.0))
    o.append(T(510, 111, "enclosure", 6.0))

    # Lower-centre: head above with the extra dimension c.
    o.append(_hatch(250, 146, 130, 12))
    o.append(_hatch(300, 158, 14, 40))
    o.append(_rect(320, 136, 20, 8, fill="#ffffff", sw=1.1))
    o.append(_rect(326, 146, 8, 40, fill="#ffffff", sw=1.0))
    o.append(_dimh(270, 340, 140, "b", ly=133))
    o.append(_dimv(240, 158, 196, "a", lx=232))
    o.append(T(288, 130, "c", 6.0))
    o.append(_lead(292, 132, 312, 152))
    o.append(T(230, 160, "f", 6.0))
    o.append(_lead(234, 162, 304, 164))
    o.append(T(322, 192, "l", 6.0))
    o.append(_arrow(316, 188, 322, 194, sw=0.8, color=GREY, head="a6s"))
    o.append(T(400, 180, "Inside of", 6.0))
    o.append(T(400, 191, "enclosure", 6.0))

    o.append(T(80, 212, "a = Length of cylindrical part of joint", 5.4, anchor="start"))
    o.append(T(80, 219, "b = Length of plane part of joint", 5.4, anchor="start"))
    o.append(T(80, 226, "f = Encroachment of chamfer or radius into plane or cylindrical planes",
               5.4, anchor="start"))
    o.append(T(80, 233, "l = Length of flamepath up to bolt hole (a + c where l is composite of",
               5.4, anchor="start"))
    o.append(T(86, 240, "plane and cylindrical parts) (l = 0.2 mm max for sub-group IIA and IIB,",
               5.4, anchor="start"))
    o.append(T(86, 247, "0.1 mm max for sub-group IIC)", 5.4, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig 10.10")),
                "Hình 10.10 · Ảnh hưởng của lỗ bu lông lên mối nối",
                "Figure 10.10 · Effects of boltholes on joints",
                "Ba mặt cắt gạch chéo có bu lông xuyên qua phần mặt bích: "
                "trái đầu bu lông ở trên và chân mở rộng ngắn ở trái, phải "
                "đầu bu lông ở dưới và thành vỏ ở trái, dưới cùng đầu bu "
                "lông ở trên với kích thước c bổ sung; các ký hiệu a, b, f, "
                "l, c và nhãn Inside of enclosure; chú giải a, b, f, l với "
                "giá trị l tối đa 0,2 mm cho IIA/IIB và 0,1 mm cho IIC",
                "Three hatched sections with a bolt through the plane part: "
                "left the bolt head is above with a short leg at the far "
                "left, right the head is below with a wall at the left, "
                "lower centre the head is above with an extra dimension c; "
                "callouts a, b, f, l and c with Inside of enclosure labels; "
                "legend a, b, f, l with l 0.2 mm max for IIA/IIB and 0.1 mm "
                "max for IIC")
