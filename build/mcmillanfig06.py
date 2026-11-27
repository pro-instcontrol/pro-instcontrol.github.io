# -*- coding: utf-8 -*-
"""Vector redraws of Figures 6.1-6.3 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 6 "Area classification practice for dusts".

All three figures are sectional / elevation line drawings with three distinct
hatch patterns taken from the legend printed inside Fig. 6.1:

    square grid      = Zone 20  (interiors of cyclone/hooper/bag filter)
    diagonal cross-X = Zone 21  (around discharge or manhole)
    single diagonal  = Zone 22  (outer halos, whole-room extents)

No axes or scale bars appear. Architecture mirrors `mcmillanfig05_a.py` and
`mcmillanfig04_a.py`: every figure returns the standard five-tuple through
`vfig._fig()` and is registered in `FIGS` by the `_reg` decorator, while the
named callables `fig_f601()` ... `fig_f603()` remain the public API.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _ellipse, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """All displayed strings are pre-vetted Unicode with no XML-special chars.

    Keeping the helper mirrors the Chapter 4/5 figure modules; no named
    entities and no ampersands are used anywhere in these three drawings.
    """
    return str(s)


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


def TM(x, y, s, size=8.0, **kw):
    """Markup text: delegate to vfig._txt(), which handles sup/sub spans."""
    return _txt(x, y, str(s), size, **kw)


def _defs():
    """Markers plus the three printed hatch conventions of Fig. 6.1."""
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a7" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="z20" width="6" height="6" patternUnits="userSpaceOnUse">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#5f6b73" stroke-width="0.5"/>'
            '<line x1="0" y1="0" x2="6" y2="0" stroke="#5f6b73" stroke-width="0.5"/>'
            '</pattern>'
            '<pattern id="z21" width="8" height="8" patternUnits="userSpaceOnUse">'
            '<path d="M0 0 L8 8 M8 0 L0 8" fill="none" stroke="#7a5c3e" '
            'stroke-width="0.55"/></pattern>'
            '<pattern id="z22" width="7" height="7" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="#9a9a9a" stroke-width="0.7"/>'
            '</pattern>'
            '</defs>' % (INK, INK))


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


def _bowtie(cx, cy, w=16, h=10):
    """Rotary-valve / air-sealed-joint bow-tie symbol."""
    x1, x2 = cx - w / 2.0, cx + w / 2.0
    y1, y2 = cy - h / 2.0, cy + h / 2.0
    return (_poly([(x1, y1), (cx, cy), (x1, y2)], fill=PAPER, sw=1.0, close=True)
            + _poly([(x2, y1), (cx, cy), (x2, y2)], fill=PAPER, sw=1.0, close=True))


def _strip(o, h, n, vi, en, note, size=6.2):
    """Small bilingual caption strip at the foot of every SVG."""
    o.append(T(340, h - 42,
               "Hình 6.%d · %s / Figure 6.%d · %s" % (n, vi, n, en),
               size, color=INK))
    o.append(T(340, h - 18, note, 5.9, color=GREY))


def _hatch_note():
    return ("Lưới = Vùng 20 · chéo chữ thập = Vùng 21 · chéo đơn = Vùng 22 / "
            "Grid = Zone 20 · cross-hatch = Zone 21 · single diagonal = Zone 22")


@_reg
def fig_f601():
    """Figure 6.1 - Cyclone and bag filter in a small room."""
    w, h = 680, 520
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 6.1 · Cyclone và túi lọc bụi / "
               "Figure 6.1 · Cyclone and bag filter",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32,
               "Mặt cắt phòng · ba kiểu gạch theo chú thích in / "
               "Room section · three hatch patterns from the printed legend",
               6.6, color=GREY))

    # ---- room shell ------------------------------------------------------
    o.append(_line(80, 70, 440, 70, sw=6.0, color=INK))       # roof
    o.append(_rect(80, 70, 7, 360, fill=INK, sw=0))           # left wall
    o.append(_rect(433, 70, 7, 360, fill=INK, sw=0))          # right wall
    o.append(_line(58, 430, 620, 430, sw=1.4, color=INK))     # ground
    o.append(T(260, 62, "Roof", 7.4, color=INK))
    o.append(T(72, 88, "Wall", 7.4, anchor="end", color=INK))
    o.append(T(448, 88, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(616, 444, "Ground", 7.2, anchor="end", color=INK))

    # ---- cyclone, joints, product hopper and drum ------------------------
    o.append(_arrow(54, 122, 128, 122, sw=1.0))               # inlet
    o.append(_rect(106, 102, 54, 6, fill=PAPER, sw=1.0))
    o.append(_path("M 110 108 L 156 108 L 156 146 L 133 190 L 110 146 Z",
                   fill=PAPER, sw=1.3))
    o.append(T(176, 166, "Cyclone", 7.2, anchor="start", color=INK))
    o.append(_lead(172, 164, 155, 160))

    o.append(_bowtie(133, 196))
    o.append(T(176, 198, "Air sealed joint", 7.0, anchor="start", color=INK))
    o.append(_lead(172, 196, 141, 196))

    o.append(_rect(110, 204, 46, 64, fill=PAPER, sw=1.2))
    o.append(_path("M 110 268 L 133 298 L 156 268 Z",
                   fill=PAPER, sw=1.2))
    o.append(T(106, 249, "Product hopper", 7.0, anchor="end", color=INK))
    o.append(_lead(110, 247, 134, 247))

    o.append(_bowtie(133, 304))
    o.append(T(176, 306, "Air sealed joint", 7.0, anchor="start", color=INK))
    o.append(_lead(172, 304, 141, 304))

    o.append(_rect(112, 314, 44, 114, fill=PAPER, sw=1.2))
    o.append(T(106, 371, "Product drum", 7.0, anchor="end", color=INK))
    o.append(_lead(110, 369, 136, 369))

    # ---- pipe from cyclone into the bag filter ---------------------------
    o.append(_path("M 156 115 L 250 115 L 250 224 L 306 224 L 306 230",
                   fill="none", sw=1.0))
    o.append(_arrow(298, 224, 306, 224, sw=1.0))

    # ---- bag filter (Zone 20), fan and discharge -------------------------
    o.append(_rect(262, 230, 88, 88, fill="url(#z20)", sw=1.3))
    o.append(_rect(278, 236, 56, 13, fill=PAPER, sw=0))
    o.append(T(306, 245.5, "Bag filter", 6.8, color=INK))

    o.append(_line(306, 230, 306, 192, sw=1.0))
    o.append(_circle(306, 175, 16, fill=PAPER, sw=1.2))
    o.append(_circle(306, 175, 6, fill=PAPER, sw=1.0))
    o.append(T(306, 154, "Fan", 7.2, color=INK))
    o.append(_path("M 306 159 L 306 138 L 470 138", fill="none", sw=1.2))
    o.append(_dimv(132, 146, 452, "y", lab_dx=6))
    o.append(T(610, 101, "Outside of", 7.2, anchor="end", color=INK))
    o.append(T(610, 111, "building", 7.2, anchor="end", color=INK))

    # ---- Zone 22 halo outside the building -------------------------------
    o.append(_ellipse(530, 180, 95, 56, fill="url(#z22)", sw=1.3, color=INK))
    o.append(_dimh(440, 625, 252, "z", lab_dy=-5))

    # ---- bag-filter discharge, Zone 21 lobe, dust drum -------------------
    o.append(_line(306, 318, 306, 346, sw=1.0))
    o.append(_ellipse(306, 326, 46, 26, fill="url(#z21)", sw=1.3, color=INK))
    o.append(_dimv(300, 352, 364, "x", lab_dx=6))
    o.append(_rect(274, 346, 64, 82, fill="url(#z20)", sw=1.3))
    o.append(T(454, 386, "Dust collection", 7.0, anchor="start", color=INK))
    o.append(T(454, 398, "drum", 7.0, anchor="start", color=INK))
    o.append(_lead(450, 390, 340, 390))

    # ---- verbatim three-swatch legend ------------------------------------
    o.append(_rect(470, 286, 182, 86, fill=PAPER, sw=1.0))
    for k, (pat, lab) in enumerate((("z20", "Zone 20"),
                                    ("z21", "Zone 21"),
                                    ("z22", "Zone 22"))):
        yy = 298 + k * 24
        o.append(_rect(484, yy, 22, 14, fill="url(#%s)" % pat, sw=0.8))
        o.append(T(514, yy + 11, lab, 7.6, anchor="start", color=INK))

    _strip(o, h, 1,
           "Cyclone và túi lọc bụi. x = 1.5 m, y = 1.5 m, z = 2 m",
           "Cyclone and bag filter. x = 1.5 m, y = 1.5 m, z = 2 m",
           _hatch_note())
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt phòng có cyclone, hai khớp nối kín khí, phễu và "
                        "thùng sản phẩm, túi lọc bụi, quạt thổi ra ngoài nhà; "
                        "ba vùng được gạch lưới, gạch chéo chữ thập và gạch chéo "
                        "đơn, có chú thích ba ô và các kích thước x, y, z")),
                "Hình 6.1 Cyclone và túi lọc bụi. x = 1.5 m, y = 1.5 m, z = 2 m",
                "Figure 6.1 Cyclone and bag filter. x = 1.5 m, y = 1.5 m, z = 2 m",
                "Mặt cắt phòng có cyclone bên trái với ống vào, hai khớp nối kín khí, "
                "phễu chứa và thùng sản phẩm; bên phải là túi lọc bụi gạch lưới, quạt "
                "và ống xả ra ngoài nhà trong vùng gạch chéo đơn mang kích thước z; "
                "vùng gạch chéo chữ thập quanh cửa xả bụi mang kích thước x, kích "
                "thước y ở ống xả của quạt; ô chú thích ba mẫu gạch Zone 20, Zone 21, "
                "Zone 22 nằm bên phải",
                "Room section with a cyclone at left and its inlet pipe, two air "
                "sealed joints, product hopper and product drum; at right a grid-hatched "
                "bag filter, fan and discharge to outside within a single-hatched halo "
                "marked z; a cross-hatched lobe around the dust discharge marked x and "
                "dimension y at the fan discharge; a three-swatch legend box for Zone "
                "20, Zone 21 and Zone 22 at the right")


@_reg
def fig_f602():
    """Figure 6.2 - Manually loaded hopper without air purge, inside a building."""
    w, h = 680, 600
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 6.2 · Phễu nạp liệu trong nhà / "
               "Figure 6.2 · Indoor loading hopper",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32,
               "Không thổi khí vào trong qua cửa nạp · X = 1.5 m / "
               "No air purge inwards through manhole · X = 1.5 m",
               6.6, color=GREY))

    # ---- Zone 22: the whole room above the floor -------------------------
    o.append(_rect(187, 77, 306, 303, fill="url(#z22)", sw=0))

    # ---- room shell ------------------------------------------------------
    o.append(_line(180, 70, 500, 70, sw=6.0, color=INK))       # roof
    o.append(_rect(180, 70, 7, 310, fill=INK, sw=0))
    o.append(_rect(493, 70, 7, 310, fill=INK, sw=0))
    o.append(_line(180, 380, 500, 380, sw=5.0, color=INK))     # floor
    o.append(_line(183.5, 380, 183.5, 470, sw=1.2, color=INK))
    o.append(_line(496.5, 380, 496.5, 470, sw=1.2, color=INK))
    o.append(_line(176, 470, 191, 470, sw=1.2, color=INK))
    o.append(_line(489, 470, 504, 470, sw=1.2, color=INK))
    o.append(T(340, 62, "Roof", 7.4, color=INK))
    o.append(T(172, 190, "Wall", 7.4, anchor="end", color=INK))
    o.append(T(508, 190, "Wall", 7.4, anchor="start", color=INK))
    o.append(T(172, 394, "Floor", 7.4, anchor="end", color=INK))

    # ---- hopper interior (Zone 20) ---------------------------------------
    o.append(_rect(248, 384, 184, 68, fill="url(#z20)", sw=1.3))
    o.append(_path("M 248 452 L 340 510 L 432 452 Z",
                   fill="url(#z20)", sw=1.3))
    o.append(_bowtie(340, 514))
    o.append(_line(340, 519, 340, 530, sw=1.0))
    o.append(T(444, 430, "Hopper", 7.4, anchor="start", color=INK))
    o.append(_lead(440, 428, 430, 424))

    # ---- manhole and its Zone 21 dome ------------------------------------
    o.append(_rect(316, 374, 48, 10, fill=PAPER, sw=1.2))
    o.append(_path("M 290 380 A 50 50 0 0 1 390 380 Z",
                   fill="url(#z21)", sw=1.3))
    o.append(T(340, 346, "X", 9.0, color=INK))
    o.append(_rect(310, 394, 60, 13, fill=PAPER, sw=0))
    o.append(T(340, 403.5, "Manhole", 6.8, color=INK))

    _strip(o, h, 2,
           "Phễu nạp liệu trong nhà, không thổi khí vào · X = 1.5 m",
           "Indoor loading hopper, no air purge · X = 1.5 m",
           _hatch_note() + " / Lỗi in: Zone 2 / Printed typo: Zone 2")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt phòng có mái, hai bức tường và sàn; toàn bộ thể "
                        "tích phòng phía trên sàn được gạch chéo đơn là Vùng 22; "
                        "phễu bên dưới sàn có nắp cửa nạp, bên trong gạch lưới là "
                        "Vùng 20, vòm bán nguyệt gạch chéo chữ thập quanh cửa nạp "
                        "là Vùng 21 với kích thước X")),
                "Hình 6.2 Phễu nạp liệu bằng tay không có khí thổi vào trong qua cửa "
                "nạp trong nhà. X = 1.5 m. Ghi chú: (1) Khu vực bên dưới mức sàn nạp "
                "liệu không được xét đến. (2) Khi không khí được hút vào phễu qua cửa "
                "nạp, đám mây bụi tạo Vùng 21 sẽ không tồn tại miễn là lưu lượng khí "
                "tại miệng cửa nạp ít nhất 1 m/s hướng vào trong. (3) Nếu dọn dẹp đủ "
                "để không hình thành lớp bụi nào thì Zone 2 có thể được giới hạn ở "
                "2-2.5 m quanh phễu (giữ nguyên lỗi in; nhiều khả năng là Vùng 22)",
                "Figure 6.2 Manually loaded hopper without air purge inwards through "
                "manhole in a building. X = 1.5 m. Notes: (1) The area below loading "
                "floor level is not addressed. (2) Where air is drawn into the hopper "
                "through the manhole, the dust cloud producing the Zone 21 will not "
                "exist provided airflow at manhole mouth is at least 1 m/s inwards. "
                "(3) If housekeeping is sufficient to prevent any layers forming the "
                "Zone 2 may be limited to 2-2.5 m around the hopper",
                "Mặt cắt có mái, hai bức tường dày và sàn ngang; toàn bộ phòng phía "
                "trên sàn gạch chéo đơn, phễu gạch lưới đặt dưới sàn có cửa nạp và "
                "vòm gạch chéo chữ thập mang kích thước X, van hình bướm ở đáy phễu",
                "Section with a roof, two thick walls and a horizontal floor; the "
                "whole room above the floor is single-hatched, a grid-hatched hopper "
                "below the floor has a manhole and a cross-hatched dome marked X, "
                "with a bow-tie valve at the hopper point")


@_reg
def fig_f603():
    """Figure 6.3 - Manually loaded hopper without air purge, outdoors."""
    w, h = 680, 560
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 6.3 · Phễu nạp liệu ngoài nhà / "
               "Figure 6.3 · Outdoor loading hopper",
               8.6, color=INK, weight="600"))
    o.append(T(340, 32,
               "Không thổi khí vào trong qua cửa nạp · X = 1.5 m, y = 2.5 m / "
               "No air purge inwards through manhole · X = 1.5 m, y = 2.5 m",
               6.4, color=GREY))

    # ---- Zone 22 finite outdoor halo -------------------------------------
    o.append(_line(150, 360, 530, 360, sw=2.6, color=INK))     # floor
    o.append(_path("M 175 360 A 165 165 0 0 1 505 360 Z",
                   fill="url(#z22)", sw=1.3))
    o.append(T(200, 380, "Floor", 7.6, anchor="start", color=INK))
    o.append(_arrow(223, 243, 260, 280, sw=1.0))
    o.append(T(240, 266, "y", 8.0, color=INK))

    # ---- hopper interior (Zone 20) ---------------------------------------
    o.append(_rect(270, 364, 140, 66, fill="url(#z20)", sw=1.3))
    o.append(_path("M 270 430 L 340 486 L 410 430 Z",
                   fill="url(#z20)", sw=1.3))
    o.append(_bowtie(340, 490))
    o.append(_line(340, 495, 340, 502, sw=1.0))
    o.append(T(422, 402, "Hopper", 7.6, anchor="start", color=INK))
    o.append(_lead(418, 400, 410, 398))

    # ---- manhole and its Zone 21 dome ------------------------------------
    o.append(_rect(318, 354, 44, 10, fill=PAPER, sw=1.2))
    o.append(_path("M 288 360 A 52 52 0 0 1 392 360 Z",
                   fill="url(#z21)", sw=1.3))
    o.append(T(340, 328, "X", 9.0, color=INK))
    o.append(_rect(310, 376, 60, 13, fill=PAPER, sw=0))
    o.append(T(340, 385.5, "Manhole", 6.8, color=INK))

    _strip(o, h, 3,
           "Phễu nạp liệu ngoài nhà, không thổi khí vào · X = 1.5 m, y = 2.5 m",
           "Outdoor loading hopper, no air purge · X = 1.5 m, y = 2.5 m",
           _hatch_note() + " / Gió hạn chế Vùng 22 / Wind limits the Zone 22 halo")
    return _fig(svg(w, h, "".join(o),
                    esc("Mặt cắt ngoài nhà có đường sàn dày, phễu gạch lưới với cửa "
                        "nạp và van đáy, vòm bán nguyệt gạch chéo chữ thập quanh cửa "
                        "nạp mang kích thước X, vùng gạch chéo đơn bán nguyệt lớn "
                        "trên sàn mang kích thước y")),
                "Hình 6.3 Phễu nạp liệu bằng tay không có khí thổi vào trong qua cửa "
                "nạp ngoài nhà. X = 1.5 m, y = 2.5 m. Ghi chú: (1) Khu vực bên dưới "
                "sàn nạp liệu không được xét đến. (2) Khi không khí được hút vào phễu "
                "qua cửa nạp, đám mây bụi tạo Vùng 21 sẽ không tồn tại miễn là lưu "
                "lượng khí tại miệng cửa nạp vượt quá 1 m/s",
                "Figure 6.3 Manually loaded hopper without air purge inwards through "
                "manhole outside a building. X = 1.5 m, y = 2.5 m. Notes: (1) The area "
                "below the loading floor is not addressed. (2) Where air is drawn into "
                "the hopper through the manhole, the dust cloud producing the Zone 21 "
                "will not exist provided the airflow at the manhole mouth exceeds 1 m/s",
                "Mặt cắt ngoài trời có đường sàn dày, phễu gạch lưới treo dưới sàn "
                "với cửa nạp, vòm gạch chéo chữ thập mang kích thước X và vòm gạch "
                "chéo đơn lớn mang kích thước y ở phía trên bên trái",
                "Outdoor section with a thick floor line, a grid-hatched hopper below "
                "it and a manhole, a cross-hatched dome marked X and a large "
                "single-hatched semicircular Zone 22 halo marked y at the upper left")
