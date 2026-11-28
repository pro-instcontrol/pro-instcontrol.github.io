# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.13-13.18 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Intrinsic safety 'i'".

All six drawings are simplified vector redraws of the rendered pages
p386, p387, p389, p398 and p399.  The printed English captions,
including the Note line of Fig. 13.15 and the final full stops of
Figs. 13.17 and 13.18, are reproduced verbatim with a bilingual
prefix; printed part labels, inequality glyphs and the dimension
letters ``d`` are transcribed onto the drawings.  The odd printed
label ``Out out`` of Fig. 13.13 and the left-to-right earth numbering
1, 3, 2 of Fig. 13.14 are retained.  Each public callable returns the
standard five-tuple through ``vfig._fig()`` and is registered in
``FIGS`` by the ``_reg`` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _f, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Literal Unicode text; escape raw ampersands and the strict less-than
    glyphs of Figs. 13.16/13.18 so every SVG stays XML-valid (no named HTML
    entities: numeric character references are used for '<')."""
    return (str(s).replace("&", "&amp;")
            .replace("<", "&#60;"))


def T(x, y, s, size=7.0, **kw):
    """Plain text: clamp to the 6.8-9.5 px contract, vet, then delegate."""
    size = max(6.8, min(9.5, size))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def ln(x1, y1, x2, y2, sw=0.9, color=INK, dash=""):
    """Stroke line with an explicit fill, so every shape is fully specified."""
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def ar(x1, y1, x2, y2, sw=0.9, color=INK, dash=""):
    """Leader / dimension arrow with an explicit fill."""
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s marker-end="url(#a7)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 13.%d · %s / Figure 13.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, size=6.8):
    """All displayed type stays within the 6.8-9.5 px contract."""
    o.append(T(340, 29, s, size, color=GREY))


def _lab(o, x, y, vi, en, anchor="middle", size=6.8, weight=""):
    """Vietnamese label with the printed English term in parentheses below."""
    o.append(T(x, y, vi, size, anchor=anchor, color=INK, weight=weight))
    o.append(T(x, y + size + 1.4, "(" + en + ")", size,
               anchor=anchor, color=GREY))


def _dim_h(o, x1, x2, y, lab="d", color=INK):
    """Horizontal dimension line with end ticks and a label above it."""
    o.append(ln(x1, y, x2, y, 0.9, color, dash="4 3"))
    o.append(ln(x1, y - 4, x1, y + 4, 0.9, color))
    o.append(ln(x2, y - 4, x2, y + 4, 0.9, color))
    o.append(T((x1 + x2) / 2.0, y - 4, lab, 6.8, color=color))


def _dim_v(o, x, y1, y2, lab="d", color=INK):
    """Vertical dimension line with end ticks and a label to its left."""
    o.append(ln(x, y1, x, y2, 0.9, color, dash="4 3"))
    o.append(ln(x - 4, y1, x + 4, y1, 0.9, color))
    o.append(ln(x - 4, y2, x + 4, y2, 0.9, color))
    o.append(T(x - 6, (y1 + y2) / 2.0 + 2.4, lab, 6.8,
               anchor="end", color=color))


# ------------------------------------------------------------------ 13.13

@_reg
def fig_f1313():
    """Figure 13.13 - typical keyed edge connector, side and plan views."""
    w, h = 680, 350
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 13, "Đầu nối cạnh có chốt định vị điển hình",
           "Typical keyed edge connector")
    _sub(o, "Mặt cạnh và mặt bằng · bảng mạch, tiếp điểm cạnh, ổ cắm / "
            "Side and plan views of a keyed connector")

    o.append(T(46, 48, "Mặt cạnh / Side view", 6.8, anchor="start", color=GREY))
    o.append(_poly([(95, 68), (170, 63), (250, 67), (330, 62),
                    (410, 67), (490, 63), (560, 68)],
                   fill="none", sw=1.2, color=INK))
    _lab(o, 210, 45, "Bảng mạch in", "Printed circuit board")
    o.append(ln(210, 56, 210, 64, 0.8))

    o.append(ln(110, 150, 560, 150, 1.0))
    for x in (150, 196, 242, 288, 372, 418, 464):
        o.append(_rect(x, 100, 24, 50, fill="url(#h6)", sw=0.9))
    # One receptacle position keyed out: the space is filled solid.
    o.append(_rect(326, 104, 32, 42, fill="#8a8a8a", sw=1.0))
    _lab(o, 342, 76, "Chốt định vị", "Out out")
    o.append(ln(342, 88, 342, 102, 0.8))
    _lab(o, 470, 80, "Các tiếp điểm cạnh", "Edge connections")
    o.append(ar(450, 94, 430, 108, 0.8))

    o.append(T(46, 178, "Mặt bằng / Plan view", 6.8, anchor="start", color=GREY))
    o.append(_rect(120, 184, 440, 54, fill="#ffffff", sw=1.1))
    for px in (170, 230, 290, 350, 410, 470):
        o.append(ln(px, 186, px, 236, 0.8, color=GREY, dash="3 3"))
        o.append(ln(px + 10, 186, px + 10, 236, 0.8, color=GREY, dash="3 3"))
        if px != 410:
            o.append(_rect(px + 2, 238, 6, 28, fill="#cfcfcf", sw=0.8))
    o.append(_rect(404, 186, 22, 50, fill="url(#h7)", sw=0.9))

    _lab(o, 92, 292, "Ổ cắm", "Socket")
    o.append(ar(112, 286, 138, 214, 0.8))
    _lab(o, 300, 292, "Các ổ tiếp điểm cạnh", "Edge connection receptacles")
    o.append(ar(300, 284, 296, 252, 0.8))
    _lab(o, 528, 292, "Ổ đã tháo, chỗ trống bị lấp đặc",
         "Receptacle removed and space solid filled")
    o.append(ar(520, 284, 418, 212, 0.8))
    o.append(T(340, 330, "Nhãn in gốc 'Out out' được giữ nguyên · "
                "Printed label 'Out out' retained", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.13")),
                "Hình 13.13 · Đầu nối cạnh có chốt định vị điển hình",
                "Figure 13.13 · Typical keyed edge connector",
                "Hình vẽ gồm hai phần. Phía trên là mặt cạnh của bảng mạch in: đường viền "
                "hơi cong phía trên, bên dưới là bảy tiếp điểm cạnh được gạch chéo, trong "
                "đó một vị trí đã bị cắt bỏ và thay bằng một khối đặc, được mũi tên chỉ "
                "kèm nhãn in gốc 'Out out'. Các nhãn Bảng mạch in (Printed circuit board) "
                "và Các tiếp điểm cạnh (Edge connections) có đường dẫn tới board và tới "
                "một tiếp điểm. Phía dưới là mặt bằng ổ cắm: hộp chữ nhật chứa sáu cặp "
                "đường đứt nét đánh dấu các ổ tiếp điểm, năm chân nhô xuống dưới; riêng "
                "ổ thứ năm bị bỏ đi và ô trống được tô gạch chéo đặc. Các nhãn Ổ cắm "
                "(Socket), Các ổ tiếp điểm cạnh (Edge connection receptacles) và Ổ đã "
                "tháo, chỗ trống bị lấp đặc (Receptacle removed and space solid filled) "
                "đều có mũi tên chỉ tới đúng vị trí tương ứng",
                "Two views of a keyed edge connector. The upper side view shows a slightly "
                "wavy printed circuit board edge over seven hatched contact fingers; one "
                "contact position is keyed out and replaced by a solid filled block, "
                "pointed to by the retained printed label 'Out out'. Leaders name the "
                "Printed circuit board and the Edge connections. The lower plan view is "
                "a rectangular socket housing with six pairs of dashed receptacle "
                "outlines and five pins projecting below; the fifth receptacle is removed "
                "and its space is hatched solid. Leaders identify the Socket, the Edge "
                "connection receptacles and the receptacle removed and space solid filled")


# ------------------------------------------------------------------ 13.14

@_reg
def fig_f1314():
    """Figure 13.14 - in-line plug/socket layouts and board earth points."""
    w, h = 680, 380
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 14, "Bố trí mối nối trên phích cắm và ổ cắm thẳng hàng",
           "Layout of connections on in-line plugs and sockets")
    _sub(o, "Mối nối độc lập và không độc lập · các điểm tiếp địa / "
            "Independent joints and earthing of the board")

    # Left: three independent connections, acceptable.
    o.append(_rect(120, 72, 120, 58, fill="#ffffff", sw=1.2))
    for x in (150, 180, 210):
        o.append(ar(x, 120, x, 84, 0.9))
    o.append(ar(180, 132, 180, 144, 0.9))
    _lab(o, 180, 52, "Mối nối không chịu sự cố (an toàn)",
         "Joint not subject to fault (infallible)")
    o.append(ln(180, 62, 180, 70, 0.8))
    _lab(o, 180, 156, "Mối nối không chịu sự cố (an toàn)",
         "Joint not subject to fault (infallible)")
    o.append(ln(180, 150, 180, 146, 0.8))
    _lab(o, 48, 98, "Chân và ổ cắm", "Pins and sockets", anchor="start")
    o.append(ar(108, 100, 148, 92, 0.8))
    _lab(o, 180, 184, "Bố trí chấp nhận được của 3 mối nối độc lập",
         "Acceptable layout of 3 independent connections")

    # Right: three connections that are not independent, unacceptable.
    o.append(_poly([(458, 74), (542, 74), (554, 92), (542, 126),
                    (458, 126), (446, 92)],
                   fill="#ffffff", sw=1.2, close=True))
    o.append(_rect(492, 78, 16, 44, fill="#cfcfcf", sw=0.9))
    for yy in (86, 100, 114):
        o.append(ar(508, yy, 540, yy, 0.8))
    _lab(o, 404, 104, "Chân và ổ cắm", "Pin and socket", anchor="end")
    o.append(ar(410, 102, 466, 96, 0.8))
    _lab(o, 628, 58, "Các mối nối không chịu sự cố (an toàn)",
         "Joints not subject to fault (infallible)", anchor="end")
    o.append(ar(588, 70, 548, 84, 0.8))
    _lab(o, 500, 156, "Bố trí không chấp nhận được của 3 mối nối "
         "(không độc lập)",
         "Unacceptable layout of 3 connections (not independent)")

    # Printed circuit board with the three earth connections, 1 - 3 - 2.
    o.append(_rect(100, 236, 480, 46, fill="#ffffff", sw=1.2))
    pts = [(104 + 15 * i, 236 - (4 if i % 2 else 0)) for i in range(33)]
    o.append(_poly(pts, fill="none", sw=1.0, color=INK))
    for xx in range(112, 576, 14):
        o.append(ln(xx, 240, xx, 280, 0.6, color=GREY))
    _lab(o, 150, 212, "Các tiếp điểm cạnh", "Edge connections")
    o.append(ar(170, 222, 190, 234, 0.8))
    _lab(o, 540, 212, "Bảng mạch in", "Printed circuit board")
    o.append(ar(530, 222, 524, 236, 0.8))

    for x, vi, en in (
            (200, "Tiếp địa 1 (mạch ia và ib)",
             "Earth connection 1 (ia and ib circuits)"),
            (390, "Tiếp địa 3 (mạch ia)",
             "Earth connection 3 (ia circuits)"),
            (560, "Tiếp địa 2 (mạch ia và ib)",
             "Earth connection 2 (ia and ib circuits)")):
        o.append(ar(x, 324, x, 284, 0.9))
        _lab(o, x, 336, vi, en)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.14")),
                "Hình 13.14 · Bố trí các mối nối trên phích cắm và ổ cắm thẳng hàng",
                "Figure 13.14 · Layout of connections on in-line plugs and sockets",
                "Hình gồm ba phần. Bên trái là sơ đồ chấp nhận được: một hộp chữ nhật có "
                "ba mũi tên hướng lên và một mũi tên hướng xuống ở đáy, với hai nhãn "
                "Mối nối không chịu sự cố (an toàn) chỉ vào mối nối trên và dưới, và nhãn "
                "Chân và ổ cắm (Pins and sockets). Bên phải là sơ đồ không chấp nhận được: "
                "một đa giác có thanh dẫn giữa và ba mũi tên, nhãn Chân và ổ cắm số ít "
                "(Pin and socket), nhãn số nhiều Các mối nối không chịu sự cố (an toàn) "
                "và chú thích bố trí không độc lập. Phía dưới là bảng mạch in dạng thanh "
                "dài có mép trên gợn sóng, các tiếp điểm cạnh và ba mũi tên tiếp địa từ "
                "trái sang phải được đánh số 1, 3, 2: tiếp địa 1 cho mạch ia và ib, tiếp "
                "địa 3 chỉ cho mạch ia, tiếp địa 2 cho mạch ia và ib",
                "Three drawings. Left, the acceptable layout: a rectangular housing with "
                "three upward pins and one downward joint, two singular labels 'Joint not "
                "subject to fault (infallible)' pointing to the top and bottom joints, and "
                "the plural label 'Pins and sockets'. Right, the unacceptable layout: a "
                "polygonal housing with a central conducting bar and three arrows, the "
                "singular label 'Pin and socket', the plural label 'Joints not subject to "
                "fault (infallible)' and the caption 'Unacceptable layout of 3 connections "
                "(not independent)'. Below, a long hatched printed circuit board with a "
                "scalloped top edge and three earthing arrows; the earth connections read "
                "left to right 1, 3, 2, with connection 3 for ia circuits only and "
                "connections 1 and 2 for ia and ib circuits")


# ------------------------------------------------------------------ 13.15

@_reg
def fig_f1315():
    """Figure 13.15 - external terminal spacing, section and perspective."""
    w, h = 680, 400
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 15, "Khoảng cách đầu nối bên ngoài", "External terminal spacing")
    _sub(o, "Kim loại tiếp địa · vật liệu cách điện · cọc terminal / "
            "Earthed metal, insulation and metal terminals")

    # Upper: section through a row of terminals between earthed metal.
    o.append(T(46, 50, "Mặt cắt / Section", 6.8, anchor="start", color=GREY))
    o.append(_rect(120, 80, 14, 80, fill="url(#h6)", sw=0.9))
    o.append(_rect(120, 160, 38, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(546, 80, 14, 80, fill="url(#h6)", sw=0.9))
    o.append(_rect(522, 160, 38, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(140, 148, 400, 12, fill="#e9e3d6", sw=1.0))
    for x in (200, 280, 360, 440):
        o.append(_rect(x, 120, 26, 28, fill="#cfcfcf", sw=0.9))
        o.append(_circle(x + 13, 132, 6, fill="#ffffff", sw=0.8))
        o.append(ln(x + 8, 136, x + 18, 128, 0.7))
        o.append(_poly([(x + 13, 160), (x + 4, 178), (x + 4, 194)],
                       fill="none", sw=0.9, color=INK))
    _lab(o, 170, 70, "Kim loại tiếp địa", "Earthed metal")
    o.append(ar(140, 80, 130, 92, 0.8))
    _lab(o, 250, 106, "Vật liệu cách điện", "Insulation")
    o.append(ar(250, 116, 250, 146, 0.8))
    _lab(o, 390, 96, "Cọc terminal bằng kim loại", "Metal terminal")
    o.append(ar(380, 106, 370, 124, 0.8))
    _lab(o, 548, 70, "Kim loại tiếp địa", "Earthed metal")
    o.append(ar(548, 80, 556, 92, 0.8))
    _dim_h(o, 134, 200, 202, "d ≥ 3")
    _dim_h(o, 306, 360, 202, "d ≥ 6")
    _dim_h(o, 466, 546, 202, "d ≥ 3")

    # Lower: the same arrangement in perspective.
    o.append(T(46, 236, "Góc nhìn phối cảnh / Perspective view", 6.8,
               anchor="start", color=GREY))
    o.append(_poly([(170, 262), (430, 256), (482, 288), (222, 294)],
                   fill="#f3f1ea", sw=1.1, close=True))
    o.append(_poly([(222, 294), (482, 288), (482, 322), (222, 328)],
                   fill="#e9e3d6", sw=1.1, close=True))
    o.append(_poly([(430, 256), (482, 252), (482, 288), (430, 284)],
                   fill="url(#h6)", sw=0.9, close=True))
    for x, y in ((230, 268), (290, 266), (350, 264), (410, 262)):
        o.append(_circle(x, y, 6, fill="#ffffff", sw=0.8))
    o.append(_poly([(482, 252), (498, 246), (498, 318), (482, 322)],
                   fill="url(#h6)", sw=0.9, close=True))
    _dim_v(o, 150, 252, 288, "d ≥ 6")
    _dim_v(o, 196, 296, 326, "d ≥ 3")
    _dim_h(o, 222, 280, 338, "d ≥ 3")
    _dim_h(o, 300, 420, 338, "d ≥ 6 mm")
    _lab(o, 560, 274, "Vật liệu cách điện", "Insulation")
    o.append(ar(520, 284, 462, 292, 0.8))
    _lab(o, 560, 310, "Kim loại tiếp địa", "Earthed metal")
    o.append(ar(520, 320, 498, 304, 0.8))

    o.append(T(340, 364, "Lưu ý: Đối với khoảng cách giữa đầu nối an toàn nội tại "
                "và không an toàn nội tại, khoảng cách ≥ 6 mm được tăng lên ≥ 50 mm",
               6.8, color=INK))
    o.append(T(340, 376, "Note: For separation between intrinsically safe and "
                "non-intrinsically safe terminals the ≥ 6 mm distance is increased to "
                "≥ 50 mm", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.15")),
                "Hình 13.15 · Khoảng cách đầu nối bên ngoài. Lưu ý: Đối với khoảng cách "
                "giữa các đầu nối an toàn nội tại và không an toàn nội tại, khoảng cách "
                "≥ 6 mm được tăng lên ≥ 50 mm",
                "Figure 13.15 · External terminal spacing. Note: For separation between "
                "intrinsically safe and non-intrinsically safe terminals the ≥ 6 mm "
                "distance is increased to ≥ 50 mm",
                "Hình gồm hai cách vẽ. Ở mặt cắt phía trên, bốn cọc terminal kim loại có "
                "vít nằm trên nền cách điện, nằm giữa hai thành kim loại tiếp địa được "
                "gạch chéo ở hai đầu; các dây dẫn đi xuống từ mỗi cọc. Ba đường kích "
                "thước ở dưới ghi d ≥ 3 ở hai bên và d ≥ 6 ở giữa. Các nhãn Kim loại tiếp "
                "địa (Earthed metal), Vật liệu cách điện (Insulation) và Cọc terminal bằng "
                "kim loại (Metal terminal) có mũi tên chỉ tới thành, nền và cọc. Ở góc "
                "nhìn phối cảnh phía dưới, một bảng cách điện nghiêng có bốn đầu vít và "
                "một thành kim loại tiếp địa bên phải; bốn kích thước ghi d ≥ 6, d ≥ 3, "
                "d ≥ 3 và d ≥ 6 mm. Hai dòng chú thích cuối hình nhắc rằng khoảng cách "
                "≥ 6 mm tăng lên ≥ 50 mm khi phân biệt đầu nối an toàn nội tại và không "
                "an toàn nội tại",
                "Two drawings. The upper section shows four slotted metal terminals on an "
                "insulating base between two hatched earthed-metal walls, with leads "
                "dropping from each terminal. Dimension lines read d ≥ 3 at each end and "
                "d ≥ 6 between the middle pair; leaders name the Earthed metal, the "
                "Insulation and the Metal terminal. The lower perspective view shows a "
                "slanted insulating board with four screw terminals and an earthed metal "
                "wall on the right, dimensioned d ≥ 6, d ≥ 3, d ≥ 3 and d ≥ 6 mm. The two "
                "printed Note lines at the bottom state that the ≥ 6 mm distance is "
                "increased to ≥ 50 mm for separation between intrinsically safe and "
                "non-intrinsically safe terminals")


# ------------------------------------------------------------------ 13.16

@_reg
def fig_f1316():
    """Figure 13.16 - seven clearance and separation measurement cases."""
    w, h = 680, 540
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 16, "Đo khoảng hở và khoảng cách cách ly",
           "Measurement of clearance and separation distance")
    _sub(o, "Bảy trường hợp đo · dây dẫn, vật cách điện, khe hở và gờ / "
            "Conductors, insulation, slots and ribs")

    # 1 - conductors on a plain insulating slab.
    o.append(_rect(260, 88, 180, 18, fill="url(#h6)", sw=1.0))
    o.append(_rect(292, 80, 28, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(380, 80, 28, 8, fill="#3a3a3a", sw=0))
    _dim_h(o, 320, 380, 74)
    _lab(o, 140, 82, "Dây dẫn", "Conductor")
    o.append(ar(184, 80, 292, 82, 0.8))
    _lab(o, 545, 94, "Vật liệu cách điện", "Insulation")
    o.append(ar(505, 94, 446, 96, 0.8))

    # 2 - slot of any width between the conductors.
    o.append(_rect(260, 148, 80, 18, fill="url(#h6)", sw=1.0))
    o.append(_rect(360, 148, 80, 18, fill="url(#h6)", sw=1.0))
    o.append(_rect(292, 140, 28, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(380, 140, 28, 8, fill="#3a3a3a", sw=0))
    _dim_h(o, 320, 380, 134)
    _lab(o, 140, 152, "Khe hở (mọi chiều rộng)", "Slot (any width)")
    o.append(ar(200, 150, 344, 158, 0.8))
    _lab(o, 545, 144, "Dây dẫn", "Conductor")
    o.append(ar(505, 146, 416, 142, 0.8))
    _lab(o, 545, 160, "Vật liệu cách điện", "Insulation")
    o.append(ar(505, 162, 446, 158, 0.8))

    # 3 - rib at least 0.9 mm wide: d passes straight over the rib.
    o.append(_rect(260, 208, 180, 18, fill="url(#h6)", sw=1.0))
    o.append(_rect(336, 182, 28, 26, fill="url(#h7)", sw=0.9))
    o.append(_rect(292, 200, 28, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(380, 200, 28, 8, fill="#3a3a3a", sw=0))
    _dim_h(o, 320, 380, 176)
    _lab(o, 140, 206, "Gờ (rộng ≥0.9 mm)", "Rib (≥0.9 mm width)")
    o.append(ar(214, 204, 340, 196, 0.8))
    _lab(o, 545, 204, "Dây dẫn", "Conductor")
    o.append(ar(505, 206, 416, 202, 0.8))
    _lab(o, 545, 220, "Vật liệu cách điện", "Insulation")
    o.append(ar(505, 222, 446, 218, 0.8))

    # 4 - rib less than 0.9 mm wide: d dips around the narrow rib.
    o.append(_rect(260, 268, 180, 18, fill="url(#h6)", sw=1.0))
    o.append(_rect(342, 252, 12, 16, fill="url(#h7)", sw=0.9))
    o.append(_rect(292, 260, 28, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(380, 260, 28, 8, fill="#3a3a3a", sw=0))
    o.append(_poly([(320, 258), (320, 270), (354, 270), (354, 258)],
                   fill="none", sw=0.9, dash="4 3", color=INK))
    o.append(T(337, 266, "d", 6.8))
    _lab(o, 140, 266, "Gờ (rộng <0.9 mm)", "Rib (<0.9 mm width)")
    o.append(ar(214, 264, 346, 262, 0.8))
    _lab(o, 545, 264, "Dây dẫn", "Conductor")
    o.append(ar(505, 266, 416, 262, 0.8))
    _lab(o, 545, 280, "Vật liệu cách điện", "Insulation")
    o.append(ar(505, 282, 446, 278, 0.8))

    # 5 - two conductors in free air.
    o.append(_circle(292, 318, 4, fill="#3a3a3a", sw=0))
    o.append(_circle(380, 318, 4, fill="#3a3a3a", sw=0))
    _dim_h(o, 292, 380, 310)
    _lab(o, 545, 318, "Dây dẫn", "Conductor")
    o.append(ar(505, 318, 386, 318, 0.8))

    # 6 - insulating rib less than 0.9 mm wide, ignored by the measurement.
    o.append(_circle(292, 368, 4, fill="#3a3a3a", sw=0))
    o.append(_circle(380, 368, 4, fill="#3a3a3a", sw=0))
    o.append(_rect(334, 356, 12, 24, fill="url(#h7)", sw=0.9))
    _dim_h(o, 292, 380, 360)
    _lab(o, 140, 362, "Gờ cách điện (<0.9 mm)",
         "Insulating rib (<0.9 mm width)")
    o.append(ar(238, 362, 338, 368, 0.8))
    _lab(o, 545, 368, "Dây dẫn", "Conductor")
    o.append(ar(505, 368, 386, 368, 0.8))

    # 7 - insulating rib at least 0.9 mm wide, measured above and below.
    o.append(_circle(292, 418, 4, fill="#3a3a3a", sw=0))
    o.append(_circle(380, 418, 4, fill="#3a3a3a", sw=0))
    o.append(_rect(326, 398, 28, 40, fill="url(#h7)", sw=0.9))
    o.append(_poly([(292, 414), (292, 394), (380, 394), (380, 414)],
                   fill="none", sw=0.9, dash="4 3", color=INK))
    o.append(_poly([(292, 422), (292, 442), (380, 442), (380, 422)],
                   fill="none", sw=0.9, dash="4 3", color=INK))
    o.append(T(336, 389, "d", 6.8))
    o.append(T(336, 452, "d", 6.8))
    _lab(o, 140, 414, "Gờ cách điện (≥0.9 mm)",
         "Insulating rib (≥0.9 mm width)")
    o.append(ar(238, 414, 330, 412, 0.8))
    _lab(o, 545, 418, "Dây dẫn", "Conductor")
    o.append(ar(505, 418, 386, 418, 0.8))

    o.append(ln(80, 466, 600, 466, 0.8, color=GREY))
    o.append(T(340, 480, "d = Khoảng hở nếu môi trường chung là không khí",
               6.8, color=INK))
    o.append(T(340, 489, "  = Khoảng cách cách ly qua hợp chất đúc nếu dây dẫn "
                "và bộ phận cách điện được bọc kín", 6.8, color=INK))
    o.append(T(340, 502, "d = Clearance if general medium is air", 6.8, color=INK))
    o.append(T(340, 511, "  = Separation through casting compound if conductors",
               6.8, color=INK))
    o.append(T(340, 520, "    and insulating parts are encapsulated", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.16")),
                "Hình 13.16 · Đo khoảng hở và khoảng cách cách ly",
                "Figure 13.16 · Measurement of clearance and separation distance",
                "Bảy sơ đồ nhỏ xếp dọc. Bốn sơ đồ đầu là hai dây dẫn đặt trên nền cách "
                "điện gạch chéo: phẳng, có khe hở mọi chiều rộng, có gờ rộng ≥0.9 mm "
                "và gờ hẹp <0.9 mm; mỗi sơ đồ có đường kích thước đứt nét mang chữ d, "
                "trong đó gờ rộng được đo thẳng qua đỉnh còn gờ hẹp được đo vòng qua "
                "chân gờ. Sơ đồ năm là hai dây dẫn dạng chấm trong không khí tự do. Sơ đồ "
                "sáu có gờ cách điện hẹp <0.9 mm bị bỏ qua, đường d thẳng xuyên qua gờ. "
                "Sơ đồ bảy có gờ cách điện rộng ≥0.9 mm với hai đường d riêng biệt đi "
                "qua đỉnh và qua đáy gờ. Các nhãn Dây dẫn (Conductor) và Vật liệu cách "
                "điện (Insulation) lặp lại ở các sơ đồ. Khối định nghĩa cuối hình ghi "
                "d là khoảng hở nếu môi trường là không khí, và là khoảng cách cách ly "
                "qua hợp chất đúc nếu dây dẫn và bộ phận cách điện được bọc kín",
                "Seven small diagrams stacked vertically. The first four show two "
                "conductors on a hatched insulating slab: plain, with a slot of any "
                "width, with a rib at least 0.9 mm wide and with a rib less than 0.9 mm "
                "wide; each carries a dashed dimension d, straight over the wide rib and "
                "dipping around the narrow one. The fifth shows two dot-like conductors "
                "in free air. The sixth has a narrow insulating rib less than 0.9 mm "
                "which is ignored, the d line running straight across it. The seventh "
                "has a wide insulating rib at least 0.9 mm with two separate d paths, "
                "one over the top and one under the bottom. Conductor and Insulation "
                "labels recur throughout. The definition block states that d is the "
                "clearance when the general medium is air, or the separation through "
                "casting compound when conductors and insulating parts are encapsulated")


# ------------------------------------------------------------------ 13.17

@_reg
def fig_f1317():
    """Figure 13.17 - basic measurement of creepage distance."""
    w, h = 680, 320
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 17, "Phép đo cơ bản khoảng cách rò bề mặt",
           "Basic measurement of creepage distance")
    _sub(o, "Bề mặt phẳng và bề mặt cong · đường d rò sát bề mặt / "
            "Flat and curved insulating surfaces")

    # Flat slab.
    o.append(_rect(230, 92, 220, 30, fill="url(#h6)", sw=1.1))
    o.append(_rect(270, 84, 34, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(376, 84, 34, 8, fill="#3a3a3a", sw=0))
    _dim_h(o, 304, 376, 78)
    _lab(o, 140, 84, "Dây dẫn", "Conductor")
    o.append(ar(184, 84, 270, 86, 0.8))
    _lab(o, 555, 100, "Vật liệu cách điện", "Insulation")
    o.append(ar(515, 100, 450, 102, 0.8))

    # Curved insulating surface, with the creepage path following the face.
    o.append(_path("M170,186 Q340,292 510,186 L510,200 Q340,310 170,200 Z",
                   fill="url(#h6)", sw=1.1))
    o.append(_poly([(196, 214), (214, 206), (220, 216), (202, 224)],
                   fill="#3a3a3a", sw=0, close=True))
    o.append(_poly([(466, 206), (484, 214), (478, 224), (460, 216)],
                   fill="#3a3a3a", sw=0, close=True))
    o.append(_path("M214,212 Q340,282 466,212",
                   fill="none", sw=1.0, dash="4 3", color=INK))
    o.append(T(340, 232, "d", 6.8))
    _lab(o, 140, 206, "Dây dẫn", "Conductor")
    o.append(ar(184, 208, 200, 212, 0.8))
    _lab(o, 560, 186, "Vật liệu cách điện", "Insulation")
    o.append(ar(520, 194, 504, 200, 0.8))

    o.append(T(340, 284, "d = khoảng cách rò bề mặt", 6.8, color=INK,
               weight="600"))
    o.append(T(340, 293, "d = creepage distance", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.17")),
                "Hình 13.17 · Phép đo cơ bản khoảng cách rò bề mặt.",
                "Figure 13.17 · Basic measurement of creepage distance.",
                "Hai bản vẽ. Bản trên là một bản cách điện gạch chéo phẳng, có hai dây "
                "dẫn đậm nằm sát mặt trên; đường kích thước đứt nét mang chữ d nối mép "
                "trong của hai dây dẫn theo đường thẳng ngang. Các nhãn Dây dẫn "
                "(Conductor) và Vật liệu cách điện (Insulation) có mũi tên chỉ tới dây "
                "và tới bản. Bản dưới là một bản cách điện gạch chéo cong hình máng, "
                "có hai dây dẫn đậm nằm sát bề mặt lõm ở hai đầu; đường d đứt nét chạy "
                "theo đường cong của bề mặt giữa hai dây dẫn, với chữ d đặt trong lòng "
                "máng. Dòng chữ d = khoảng cách rò bề mặt / d = creepage distance được "
                "đặt căn giữa bên dưới hai bản vẽ",
                "Two drawings. The upper one is a flat hatched insulating slab with two "
                "dark conductors resting on its top face; a dashed dimension line "
                "labelled d spans the inner edges of the conductors in a straight line. "
                "Leaders name the Conductor and the Insulation. The lower drawing is a "
                "concave curved insulating slab with two dark conductors against its "
                "inner face at the ends; the dashed d path follows the curved surface "
                "between them, with the letter d inside the hollow. The centred line "
                "reads d = creepage distance")


# ------------------------------------------------------------------ 13.18

def _slot_pair(o, cx, y, top, screw=False, vdim=None, bdim=None):
    """One insulant block with a slot, two conductors and a creepage path."""
    gap = 18.0 if top.startswith("≥3") else 7.0
    left_w = (110.0 - gap) / 2.0
    o.append(_rect(cx - 55, y + 22, left_w, 26, fill="url(#h7)", sw=0.9))
    o.append(_rect(cx - 55 + left_w + gap, y + 22, left_w, 26,
                   fill="url(#h7)", sw=0.9))
    o.append(_rect(cx - 38, y + 12, 24, 8, fill="#3a3a3a", sw=0))
    o.append(_rect(cx + 14, y + 12, 24, 8, fill="#3a3a3a", sw=0))
    # Width of the slot above the block.
    o.append(ln(cx - gap / 2.0, y + 4, cx + gap / 2.0, y + 4, 0.8))
    o.append(ln(cx - gap / 2.0, y + 1, cx - gap / 2.0, y + 7, 0.8))
    o.append(ln(cx + gap / 2.0, y + 1, cx + gap / 2.0, y + 7, 0.8))
    o.append(T(cx, y - 2, top, 6.8))
    # Creepage path: straight across a narrow slot, down into a wide one.
    if gap >= 18:
        o.append(_poly([(cx - 14, y + 14), (cx - 14, y + 44),
                        (cx + 14, y + 44), (cx + 14, y + 14)],
                       fill="none", sw=0.9, dash="4 3", color=INK))
        o.append(T(cx, y + 36, "d", 6.8))
    else:
        o.append(ln(cx - 14, y + 14, cx + 14, y + 14, 0.9, dash="4 3"))
        o.append(T(cx, y + 9, "d", 6.8))
    _lab(o, cx - 26, y - 14, "Dây dẫn", "Conductor", anchor="end")
    _lab(o, cx + 26, y - 14, "Dây dẫn", "Conductor", anchor="start")
    _lab(o, cx - 62, y + 38, "Vật cách điện", "Insulant", anchor="end")
    if vdim:
        o.append(ln(cx + 62, y + 22, cx + 62, y + 48, 0.8))
        o.append(ln(cx + 58, y + 22, cx + 66, y + 22, 0.8))
        o.append(ln(cx + 58, y + 48, cx + 66, y + 48, 0.8))
        o.append(T(cx + 68, y + 38, vdim, 6.8, anchor="start"))
    if bdim:
        o.append(ln(cx - 30, y + 55, cx + 30, y + 55, 0.8))
        o.append(ln(cx - 30, y + 52, cx - 30, y + 58, 0.8))
        o.append(ln(cx + 30, y + 52, cx + 30, y + 58, 0.8))
        o.append(T(cx, y + 64, bdim, 6.8))
    if screw:
        o.append(_rect(cx - 3, y + 18, 6, 34, fill="#3a3a3a", sw=0))
        o.append(_circle(cx, y + 54, 5, fill="#8a8a8a", sw=0.8))
        _lab(o, cx + 10, y + 58, "Vít kim loại (tiếp địa)",
             "Metal screw (earthed)", anchor="start")


@_reg
def fig_f1318():
    """Figure 13.18 - effect of slots on creepage distance, four paired rows."""
    w, h = 680, 500
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 18, "Ảnh hưởng của khe hở đến khoảng cách rò bề mặt",
           "Effect of slots on creepage distance")
    _sub(o, "Bốn hàng sơ đồ so sánh · khe hở hẹp, khe hở rộng, vít tiếp địa / "
            "Narrow and wide slots with and without an earthed screw")

    # Row 1: narrow slot versus wide slot.
    _slot_pair(o, 215, 76, "<3")
    _slot_pair(o, 465, 76, "≥3")

    # Row 2: narrow gap with a side dimension versus a wider stepped gap.
    _slot_pair(o, 215, 176, "<3", vdim="<3")
    _slot_pair(o, 465, 176, "≥1", vdim="≥3", bdim="≥3")

    # Row 3: narrow slot with an earthed metal screw in both drawings.
    _slot_pair(o, 215, 276, "<3", screw=True)
    _slot_pair(o, 465, 276, "<3", screw=True)

    # Row 4: wide slot, plain and with an earthed metal screw.
    _slot_pair(o, 215, 376, "≥3")
    _slot_pair(o, 465, 376, "≥3", screw=True)

    o.append(T(340, 466, "d = khoảng cách rò bề mặt", 6.8, color=INK,
               weight="600"))
    o.append(T(340, 475, "d = creepage distance", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.18")),
                "Hình 13.18 · Ảnh hưởng của khe hở đến khoảng cách rò bề mặt.",
                "Figure 13.18 · Effect of slots on creepage distance.",
                "Tám sơ đồ nhỏ xếp thành bốn hàng, mỗi hàng một cặp trái và phải. Mỗi sơ "
                "đồ gồm một khối vật cách điện gạch chéo có khe hở giữa, hai dây dẫn đậm "
                "nằm ở mép trên hai bên khe, và một đường d đứt nét: với khe hẹp <3 đường "
                "d đi thẳng ngang qua miệng khe, với khe rộng ≥3 đường d đi xuống sát "
                "thành khe rồi lên. Các nhãn Dây dẫn (Conductor), Vật cách điện "
                "(Insulant) và chữ d lặp ở từng sơ đồ. Hàng 1 so sánh <3 và ≥3. Hàng 2 "
                "bên trái có kích thước thẳng đứng <3 ở mép phải; bên phải có các kích "
                "thước ≥1 phía trên, ≥3 thẳng đứng bên phải và ≥3 phía dưới. Hàng 3 có "
                "vít kim loại tiếp địa xuyên qua cả hai khối, khe đều <3. Hàng 4 bên trái "
                "là khe ≥3 không có vít, bên phải là khe ≥3 có vít kim loại tiếp địa. "
                "Dòng d = khoảng cách rò bề mặt / d = creepage distance nằm căn giữa "
                "trên chú thích",
                "Eight small diagrams in four rows of two. Each shows a cross-hatched "
                "insulant block with a central slot, two dark conductors on the upper "
                "edges and a dashed creepage path d: across the mouth for a slot narrower "
                "than 3 mm, and down and up the slot walls for a slot of at least 3 mm. "
                "Conductor and Insulant labels and the letter d recur in each diagram. "
                "Row 1 compares <3 with ≥3. Row 2 left carries a vertical <3 dimension at "
                "the right edge; row 2 right carries ≥1 above, ≥3 vertically at the right "
                "and ≥3 below. Row 3 has an earthed metal screw through both blocks with "
                "slots <3. Row 4 has a ≥3 slot on the left without a screw and a ≥3 slot "
                "on the right with an earthed metal screw. The centred line reads "
                "d = creepage distance above the caption")


if __name__ == "__main__":
    for _name in sorted(FIGS):
        print(_name, len(FIGS[_name]))
