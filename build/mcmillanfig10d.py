# -*- coding: utf-8 -*-
"""Vector redraws of Figures 10.26-10.29 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 10 "Flameproof enclosure 'd'".

The four drawings are simplified vector redraws of the rendered page images
(pdf pp.292-294 / printed pp.271-273).  Captions follow the printed English
wording verbatim with the bilingual ``Figure / Hinh`` prefix; leaders and
letter legends are transcribed from the pages.  Architecture mirrors the
sibling ``mcmillanfig10a``..``mcmillanfig10c`` modules: each figure returns the
standard five-tuple through ``vfig._fig()`` and is registered in ``FIGS`` by
the ``_reg`` decorator, while the named callables ``fig_f1026()`` ...
``fig_f1029()`` remain the public API.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _fig, _line, _path, _poly,
                  _rect, _txt, svg)

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

def _defs10():
    """Arrow heads used by the leader lines and the dimension line."""
    return ('<defs>'
            '<marker id="a10" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a10s" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '</defs>' % (INK, GREY))


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a10s")


def _head(o, n, vi, en, size=7.2):
    """Short bilingual identifier drawn at the top of the canvas."""
    o.append(T(340, 15, "Hình 10.%d · %s  /  Figure 10.%d · %s"
               % (n, vi, n, en), size, color=INK, weight="600"))
    o.append(T(340, 29, "Bản vẽ đơn giản hóa · Simplified redraw · "
               "nhãn theo bản in / labels as printed", 5.9, color=GREY))


def _thread(x, y0, y1, amp=3.0, step=7.0):
    """Zigzag screw-thread edge; endpoints coincide with the plain edge."""
    n = max(2, int(round((y1 - y0) / step)))
    pts = []
    for i in range(n + 1):
        y = y0 + (y1 - y0) * i / float(n)
        dx = 0 if i in (0, n) else (amp if i % 2 else -amp)
        pts.append((x + dx, y))
    return pts


def _cap(o, x0, x1, y0, y1, threaded=True):
    """Lampcap: plain top and bottom, optional zigzag thread side edges."""
    o.append(_line(x0, y0, x1, y0))
    o.append(_line(x0, y1, x1, y1))
    if threaded:
        o.append(_poly(_thread(x0, y0, y1)))
        o.append(_poly(_thread(x1, y0, y1, amp=-3.0)))
    else:
        o.append(_line(x0, y0, x0, y1))
        o.append(_line(x1, y0, x1, y1))


def _bulb(o, cx, cy, r, neck):
    """Circular lamp bulb plus its two sloping neck lines.

    `neck` holds the two sides as ((x_top, y_top), (x_bottom, y_bottom)).
    """
    o.append(_circle(cx, cy, r))
    for (x0, y0), (x1, y1) in neck:
        o.append(_line(x0, y0, x1, y1))


# ------------------------------------------------------------------ 10.26

@_reg
def fig_f1026():
    """Figure 10.26 - E10 and E14 screw lamp and lampcap."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, 26, "Đèn vặn E10 và E14", "E10 and E14 screw lamp")

    # Fixed contact, with its leader from the caption line above.
    o.append(T(340, 42, "Fixed contact", 7.0))
    o.append(T(340, 51, "(may be solid or spring)", 6.6))
    o.append(_lead(340, 55, 340, 70))

    # Screw lampcap with zigzag threads on both vertical edges.
    _cap(o, 316, 364, 60, 122)
    o.append(_circle(340, 74, 4.2, fill=INK, color=INK))   # fixed contact
    o.append(_circle(340, 104, 4.2, fill=INK, color=INK))  # lamp contact
    o.append(_line(322, 110, 358, 110, sw=1.0))

    # Bulb neck flares into the circular bulb.
    _bulb(o, 340, 196, 62, (((316, 122), (313, 140)), ((364, 122), (367, 140))))
    o.append(T(340, 199, "Lamp", 9.0))

    # Left-hand thread legend and right-hand lamp-contact legend.
    for i, s in enumerate(("Threads complying", "with normal lamp",
                           "and lamp holder", "specifications")):
        o.append(T(28, 88 + i * 10, s, 6.6, anchor="start"))
    o.append(_lead(100, 103, 313, 103))
    o.append(T(392, 104, "Lamp contact", 7.5, anchor="start"))
    o.append(_lead(388, 104, 346, 104))

    return _fig(svg(w, h, "".join(o), esc("Figure 10.26 - E10 and E14 screw lamp")),
                "Hình 10.26 · Đèn vặn và chụp đèn cho đèn vặn E10 và E14. "
                "Ghi chú: Tối thiểu hai vòng ren hoàn chỉnh được ăn khớp tại thời điểm "
                "tách tiếp điểm cố định và tiếp điểm của đèn",
                "Figure 10.26 · Screw Lamps and lampcaps for E10 and E14 screw lamps. "
                "Note: Minimum two complete turns of thread engaged at time of "
                "separation of fixed and lamp contacts",
                "Screw lamp and lampcap for E10 and E14: a circular bulb with a narrow "
                "neck carrying a small rectangular cap, zigzag threads on both cap "
                "edges, two stacked dark contact dots inside, a leader from above to "
                "the fixed contact and leaders to the threads and the lamp contact",
                "Đèn vặn và chụp đèn E10 và E14: bóng đèn tròn với cổ hẹp, chụp nhỏ "
                "có ren zíc-zắc hai bên, hai chấm tiếp điểm xếp dọc, mũi tên tới tiếp "
                "điểm cố định, ren và tiếp điểm của đèn")


# ------------------------------------------------------------------ 10.27

@_reg
def fig_f1027():
    """Figure 10.27 - E27 and E40 screw lamps, groups IIA / IIB / IIC."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, 27, "Đèn vặn E27 và E40", "E27 and E40 screw lamp")

    # Outer flameproof enclosure surrounding the top of the cap.
    o.append(_rect(300, 58, 82, 60, fill="none"))
    # Screw cap with zigzag threads and the spring-loaded contact above.
    _cap(o, 314, 368, 70, 130)
    o.append(_poly(_thread(340, 62, 76, amp=3.0, step=4.0)))
    o.append(_circle(340, 82, 4.5, fill=INK, color=INK))   # fixed contact
    o.append(_circle(340, 110, 4.5, fill=INK, color=INK))  # lamp contact
    o.append(_line(322, 116, 358, 116, sw=1.0))

    _bulb(o, 340, 196, 60, (((314, 130), (312, 144)), ((368, 130), (370, 144))))
    o.append(T(340, 199, "Lamp", 9.0))

    # Leaders and legends, in the same relative positions as the print.
    o.append(T(286, 62, "Enclosure", 7.2, anchor="end"))
    o.append(T(286, 71, "(note 3)", 7.2, anchor="end"))
    o.append(_lead(290, 68, 302, 74))

    o.append(T(398, 58, "Spring loaded fixed", 7.2, anchor="start"))
    o.append(T(398, 67, "contact", 7.2, anchor="start"))
    o.append(_lead(394, 64, 346, 78))

    o.append(T(398, 104, "Lamp contact", 7.2, anchor="start"))
    o.append(_lead(394, 104, 346, 110))

    o.append(T(286, 104, "Engagement", 7.2, anchor="end"))
    o.append(T(286, 113, "(note 2)", 7.2, anchor="end"))
    o.append(_line(296, 98, 296, 122, sw=0.8, color=GREY))
    o.append(_line(291, 98, 301, 98, sw=0.8, color=GREY))
    o.append(_line(291, 122, 301, 122, sw=0.8, color=GREY))
    o.append(_lead(290, 110, 296, 110))

    o.append(T(398, 140, "Threads", 7.2, anchor="start"))
    o.append(T(398, 149, "(note 1)", 7.2, anchor="start"))
    o.append(_lead(394, 144, 366, 118))

    return _fig(svg(w, h, "".join(o), esc("Figure 10.27 - E27 and E40 screw lamp")),
                "Hình 10.27 · Đèn vặn và chụp đèn E27 và E40. Ghi chú: (1) Ren phù hợp "
                "với yêu cầu thông thường của đèn và giá đèn đối với nhóm IIA nhưng phải "
                "đáp ứng yêu cầu mối nối chống cháy nổ ren đối với Nhóm IIB và IIC. "
                "(2) Tại thời điểm tách điện, 2 ren được ăn khớp đối với nhóm IIA nhưng "
                "phải là mối nối ren chống cháy nổ đối với nhóm IIB và IIC. (3) Phải là "
                "vỏ chống cháy nổ đối với các nhóm IIB và IIC",
                "Figure 10.27 · Screw lamps and lampcaps E27 and E40. Notes: "
                "(1) Threads comply with normal lamp/lampholder requirements for group "
                "IIA but with threaded flameproof joint requirements for Group IIB and "
                "IIC. (2) At time of electrical separation 2 threads engaged for group "
                "IIA but must be a flameproof threaded joint for group IIB and IIC. "
                "(3) Must be a flameproof enclosure for groups IIB and IIC",
                "E27 and E40 screw lamp and lampcap: the circular lamp has a threaded "
                "cap inside an outer rectangular enclosure, a spring-loaded fixed "
                "contact and a lower lamp contact, a bracket at left marking thread "
                "engagement and leaders labelled enclosure, threads and lamp contact",
                "Đèn vặn và chụp đèn E27 và E40: bóng tròn có chụp ren trong vỏ chữ nhật "
                "bên ngoài, tiếp điểm cố định có lò xo và tiếp điểm đèn bên dưới, ngoặc "
                "bên trái đánh dấu chiều dài ăn khớp ren, các mũi tên tới vỏ, ren và tiếp điểm")


# ------------------------------------------------------------------ 10.28

@_reg
def fig_f1028():
    """Figure 10.28 - Single-pin TLX fluorescent flameproof joint."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, 28, "Đèn huỳnh quang TLX một chân", "Single-pin TLX fluorescent")

    # Fluorescent tube; the wavy break at the left shows it continues.
    o.append(_path("M70,118 C58,126 82,138 70,150 C58,162 82,174 70,182"))
    o.append(_line(70, 118, 326, 118))
    o.append(_line(70, 122, 326, 122))
    o.append(_line(70, 178, 326, 178))
    o.append(_line(70, 182, 326, 182))
    o.append(T(195, 154, "Tube", 9.0))

    # Lampcap and single pin entering the holder: the flameproof joint.
    o.append(_rect(326, 126, 26, 48, fill="none"))
    o.append(_poly(_thread(354, 128, 172, amp=1.5, step=6.0)))
    o.append(_rect(356, 145, 8, 6, fill="none"))
    o.append(_rect(364, 108, 141, 84, fill="none"))
    o.append(_poly([(364, 148), (404, 148), (404, 166), (420, 166),
                    (420, 148), (446, 148)]))
    o.append(_circle(446, 148, 4.2, fill=INK, color=INK))
    o.append(_line(446, 148, 560, 148))

    o.append(T(446, 84, "Fixed contact", 7.5))
    o.append(_lead(446, 90, 446, 143))
    o.append(T(344, 218, "Lamp cap", 7.5))
    o.append(_lead(344, 206, 344, 176))
    o.append(T(446, 218, "Lamp holder", 7.5))
    o.append(_lead(446, 206, 446, 194))

    return _fig(svg(w, h, "".join(o), esc("Figure 10.28 - TLX fluorescent flameproof joint")),
                "Hình 10.28 · Mối nối chống cháy nổ của đèn huỳnh quang một chân (TLX). "
                "Ghi chú: Chụp đèn và giá đèn phải phù hợp với bảng dữ liệu Fab của IEC 61 "
                "để đảm bảo không có sự truyền ngọn lửa",
                "Figure 10.28 · Flameproof joint of single pin (TLX) fluorescent. "
                "Note: Lampcap and holder comply with data sheet Fab of IEC 61 to "
                "ensure no flame transmission",
                "Horizontal TLX fluorescent tube with a wavy break at its left end, a "
                "small lampcap carrying one pin that plugs into a rectangular lamp "
                "holder at the right; the stepped conductor ends in a dark fixed "
                "contact and continues out as a lead, with the cap and holder "
                "interface forming the flameproof joint",
                "Ống đèn huỳnh quang TLX nằm ngang có đường gãy sóng ở đầu trái, chụp "
                "nhỏ với một chân cắm vào giá đèn chữ nhật bên phải; dẫn điện gập khúc "
                "tới tiếp điểm cố định rồi kéo dài ra ngoài, bề mặt chụp và giá đèn tạo "
                "mối nối chống cháy nổ")


# ------------------------------------------------------------------ 10.29

@_reg
def fig_f1029():
    """Figure 10.29 - Cylindrical bayonet-type lamp."""
    w, h = 680, 300
    o = [_defs10(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _head(o, 29, "Đèn dạng trụ kiểu lê", "Cylindrical bayonet lamp")

    # Flameproof enclosure with a narrow cylindrical clearance at the left.
    o.append(_rect(300, 54, 80, 98, fill="none"))
    o.append(_line(307, 60, 307, 146, sw=0.9))
    # Cylindrical cap (no screw thread) and its two contacts.
    _cap(o, 312, 370, 62, 146, threaded=False)
    o.append(_circle(340, 76, 4.2, fill=INK, color=INK))   # fixed contact
    o.append(_circle(340, 106, 4.2, fill=INK, color=INK))  # lamp contact
    o.append(_line(324, 112, 356, 112, sw=1.0))
    # Bayonet slot with its hooked end at the bottom of the cap.
    o.append(_path("M330,146 L330,132 C330,122 348,122 348,132 L348,137 "
                   "C348,143 336,143 336,135"))

    _bulb(o, 340, 200, 58, (((312, 146), (310, 150)), ((370, 146), (370, 150))))
    o.append(T(340, 203, "Lamp", 9.0))

    o.append(T(398, 62, "Fixed contact", 7.5, anchor="start"))
    o.append(_lead(394, 62, 344, 74))
    o.append(T(286, 64, "Flameproof", 7.2, anchor="end"))
    o.append(T(286, 73, "enclosure", 7.2, anchor="end"))
    o.append(_lead(290, 70, 302, 76))
    o.append(T(286, 106, "Cylindrical", 7.2, anchor="end"))
    o.append(T(286, 115, "joint", 7.2, anchor="end"))
    o.append(_lead(290, 110, 303, 112))
    o.append(T(398, 104, "Lamp contact", 7.5, anchor="start"))
    o.append(_lead(394, 104, 346, 106))

    # Vertical joint-length dimension with opposing arrowheads.
    o.append(_line(382, 104, 432, 104, sw=0.8, color=GREY))
    o.append(_line(382, 142, 432, 142, sw=0.8, color=GREY))
    o.append(_arrow(432, 107, 432, 139, sw=0.8, color=GREY, head="a10s"))
    o.append(_arrow(432, 139, 432, 107, sw=0.8, color=GREY, head="a10s"))
    o.append(T(442, 126, "Joint length = 10 mm min", 7.2, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Figure 10.29 - Cylindrical bayonet lamp")),
                "Hình 10.29 · Đèn dạng trụ (kiểu lê). Ghi chú: Điểm này phải đáp ứng "
                "các yêu cầu đối với mối nối trụ nhưng cũng phải có chiều dài ít nhất "
                "10 mm khi các tiếp điểm tách ra",
                "Figure 10.29 · Cylindrical (bayonet type) lamps. Note: The point must "
                "comply with the cylindrical joint requirements but must also have a "
                "length of at least 10 mm when the contacts separate",
                "Cylindrical bayonet lamp: a circular bulb under a tall plain cylindrical "
                "cap inside an outer flameproof enclosure, with a narrow clearance at "
                "the left wall, two dark stacked contacts, a hooked bayonet slot at the "
                "bottom and a vertical dimension marked joint length 10 mm minimum",
                "Đèn dạng trụ kiểu lê: bóng tròn bên dưới chụp trụ dài không ren nằm "
                "trong vỏ chống cháy nổ, khe hở hẹp ở thành trái, hai tiếp điểm xếp dọc, "
                "rãnh lê móc ở đáy và kích thước dọc chiều dài mối nối tối thiểu 10 mm")
