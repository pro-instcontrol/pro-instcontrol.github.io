# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.19-13.27 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Protection concept intrinsic
safety 'i'".

All nine drawings are simplified vector redraws of the rendered pages
p400, p401, p406, p409, p411, p412 and p413.  The printed English captions,
including every Note line and the printed quirks (Type 1a/1b digit one,
"unless material is non-conducting" in Fig. 13.26, the missing terminal full
stop in Figs 13.22-13.27), are reproduced verbatim after the bilingual
prefix.  Printed in-figure labels and legends are transcribed onto the
drawings, with the printed English retained in parentheses after the
Vietnamese term.  Each public callable returns the standard five-tuple
through ``vfig._fig()`` and is registered in ``FIGS`` by the ``_reg``
decorator.
"""
import sys
import os

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
    """Literal Unicode only; escape raw ampersands and angle brackets."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def T(x, y, s, size=6.8, **kw):
    """Plain on-canvas text, clamped to the 6.8-9.5 px contract."""
    size = max(6.8, min(9.5, size))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 13.%d · %s / Figure 13.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, size=6.8):
    o.append(T(340, 29, s, size, color=GREY))


def _bi(o, x, y, vi, en, size=6.8, weight="", anchor="middle"):
    """Vietnamese label first, printed English term in parentheses below."""
    o.append(T(x, y, vi, size, color=INK, weight=weight, anchor=anchor))
    o.append(T(x, y + size + 1.6, "(" + en + ")", size, color=GREY, anchor=anchor))


def _lab(o, x, y, vi, en, anchor="start"):
    """Two-line bilingual leader label."""
    o.append(T(x, y, vi, 6.8, anchor=anchor, color=INK))
    o.append(T(x, y + 9, "(" + en + ")", 6.8, anchor=anchor, color=GREY))


def _lead(x1, y1, x2, y2, sw=0.8):
    return _arrow(x1, y1, x2, y2, sw=sw, color=INK, head="a7")


def _dimh(x1, x2, y, label):
    """Horizontal dimension line with arrowheads at both ends."""
    o = [_line(x1, y, x2, y, sw=0.8, color=INK)]
    o.append(_poly([(x1, y), (x1 + 3.5, y - 1.6), (x1 + 3.5, y + 1.6)],
                   fill=INK, sw=0, close=True))
    o.append(_poly([(x2, y), (x2 - 3.5, y - 1.6), (x2 - 3.5, y + 1.6)],
                   fill=INK, sw=0, close=True))
    o.append(T((x1 + x2) / 2.0, y - 2.5, label, 6.8, color=INK))
    return "".join(o)


def _dimv(y1, y2, x, label, side="right"):
    """Vertical dimension line with arrowheads at both ends."""
    o = [_line(x, y1, x, y2, sw=0.8, color=INK)]
    o.append(_poly([(x, y1), (x - 1.6, y1 + 3.5), (x + 1.6, y1 + 3.5)],
                   fill=INK, sw=0, close=True))
    o.append(_poly([(x, y2), (x - 1.6, y2 - 3.5), (x + 1.6, y2 - 3.5)],
                   fill=INK, sw=0, close=True))
    ax = x + 4 if side == "right" else x - 4
    an = "start" if side == "right" else "end"
    o.append(T(ax, (y1 + y2) / 2.0 + 2.4, label, 6.8, anchor=an, color=INK))
    return "".join(o)


def _vtxt(x, y, s, size=6.8, color=INK, weight=""):
    """Vertical (bottom-to-top) winding label."""
    w = ("font-weight:%s;" % weight) if weight else ""
    return ('<text x="%.2f" y="%.2f" text-anchor="middle" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;%s" '
            'transform="rotate(-90 %.2f %.2f)">%s</text>'
            % (x, y, size, color, w, x, y, esc(s)))


def _hatch(x, y, w, h):
    return _rect(x, y, w, h, fill="url(#h6)", sw=1.0)


def _earth(o, x, y):
    o.append(_line(x, y, x, y + 7, sw=1.1))
    o.append(_line(x - 8, y + 7, x + 8, y + 7, sw=1.1))
    o.append(_line(x - 5, y + 10, x + 5, y + 10, sw=1.1))
    o.append(_line(x - 2, y + 13, x + 2, y + 13, sw=1.1))


def _coil(o, x, y0, y1, n=6, amp=6.0):
    """Simplified vertical winding symbol (zig-zag loops)."""
    pts = [(x, y0)]
    step = (y1 - y0) / float(n)
    for i in range(n):
        pts.append((x + amp, y0 + step * i + step * 0.5))
        pts.append((x, y0 + step * (i + 1)))
    o.append(_poly(pts, fill="none", sw=1.3, color=INK))


def _resistor(o, x1, x2, y):
    n = 5
    pts = [(x1, y)]
    w = (x2 - x1) / float(n)
    for i in range(n):
        pts.append((x1 + w * i + w * 0.5, y - 5))
        pts.append((x1 + w * (i + 1), y))
    o.append(_poly(pts, fill="none", sw=1.3, color=INK))


# ------------------------------------------------------------------ 13.19

@_reg
def fig_f1319():
    """Figure 13.19 - effect of ribs on creepage distance, four diagrams."""
    w, h = 680, 410
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 19, "Ảnh hưởng của gân đến khoảng cách rò bề mặt",
           "Effect of ribs on creepage distance", 7.2)
    _sub(o, "Bốn cấu hình · ký hiệu kích thước ≥3, <3, ≥1 và d = d₁ + d₂ / "
            "Four configurations · dimension markers ≥3, <3, ≥1 and d = d₁ + d₂")

    # ---- upper-left: ribbed insulant, two conductors, d and >=3
    o.append(_hatch(70, 140, 220, 28))
    o.append(_rect(100, 118, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(216, 118, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(170, 104, 20, 36, fill="url(#h6)", sw=1.0))
    o.append(_dimh(100, 260, 76, "d"))
    o.append(_dimh(124, 216, 100, "≥3"))
    o.append(_dimv(118, 168, 292, "≥3"))
    o.append(T(178, 162, "<3", 6.8, color=INK))
    _bi(o, 96, 92, "Dây dẫn", "Conductor", 6.8)
    _bi(o, 258, 92, "Dây dẫn", "Conductor", 6.8)
    o.append(T(56, 154, "Vật cách điện (Insulant)", 6.8, anchor="start", color=INK))
    o.append(_lead(96, 156, 100, 152))

    # ---- upper-right: cemented joint, >=1 at the edge
    o.append(_hatch(390, 140, 220, 28))
    o.append(_rect(420, 118, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(536, 118, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(480, 122, 20, 18, fill="#dedede", sw=1.0))
    o.append(_dimh(420, 580, 76, "d"))
    o.append(_dimh(444, 536, 100, "≥3"))
    o.append(_dimv(118, 168, 612, "≥1"))
    _bi(o, 418, 92, "Dây dẫn", "Conductor", 6.8)
    _bi(o, 552, 92, "Dây dẫn", "Conductor", 6.8)
    o.append(T(376, 154, "Vật cách điện (Insulant)", 6.8, anchor="start", color=INK))
    _lab(o, 502, 172, "Mối nối xi măng", "Cemented joint", "middle")
    o.append(_lead(490, 158, 488, 134))

    # ---- lower-left: three conductors, centre metal isolated, d = d1 + d2
    o.append(_hatch(60, 300, 240, 28))
    for xx in (90, 170, 250):
        o.append(_rect(xx, 278, 40, 22, fill="#cfcfcf", sw=1.0))
    o.append(_dimh(90, 290, 250, "d = d₁ + d₂"))
    o.append(_dimh(130, 170, 268, "d₁"))
    o.append(_dimh(170, 210, 268, "d₂"))
    o.append(_dimh(210, 250, 268, "c"))
    o.append(T(200, 346, "Kim loại ở giữa không nối điện", 6.8, color=INK))
    o.append(T(200, 356, "(The central metal is not electrically connected)",
               6.8, color=GREY))
    o.append(T(48, 314, "Vật cách điện (Insulant)", 6.8, anchor="start", color=INK))

    # ---- lower-right: uncemented joint, exposed HT of r,b > d
    o.append(_hatch(390, 300, 220, 28))
    o.append(_rect(420, 278, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(536, 278, 44, 22, fill="#cfcfcf", sw=1.0))
    o.append(_dimh(420, 580, 250, "d"))
    o.append(_dimv(278, 328, 616, "d"))
    o.append(T(376, 314, "Vật cách điện (Insulant)", 6.8, anchor="start", color=INK))
    _lab(o, 500, 340, "Mối nối không xi măng", "Uncemented joint", "middle")
    o.append(T(500, 366, "Exposed HT of r,b > d", 6.8, color=INK))

    o.append(_line(30, 376, 650, 376, sw=0.8, color=GREY))
    o.append(T(340, 390, "d, d₁, d₂ = khoảng cách rò (d, d₁, d₂ = creepage distance)",
               6.8, color=INK, weight="600"))
    o.append(T(340, 402, "Các chỉ số ≥3, <3, ≥1 là giới hạn kích thước in trên hình / "
                "Printed dimension limits", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.19")),
                "Hình 13.19 · Ảnh hưởng của gân đến khoảng cách rò bề mặt.",
                "Figure 13.19 · Effect of ribs on creepage distance.",
                "Bốn mặt cắt cắt ngang họa hình ảnh hưởng của các gân cách điện đến đường rò "
                "bề mặt giữa các dây dẫn. Góc trên bên trái: hai dây dẫn nằm trên nền vật "
                "cách điện có một gân ở giữa, các mũi tên kích thước mang nhãn d và ≥3, "
                "kèm chú thích <3. Góc trên bên phải: hai dây dẫn được nối bằng mối nối "
                "xi măng (Cemented joint), kích thước d, ≥3 và ≥1. Góc dưới bên trái: ba "
                "dây dẫn, trong đó kim loại ở giữa không nối điện, các đoạn được ký hiệu "
                "d₁, d₂ và c với biểu thức d = d₁ + d₂. Góc dưới bên phải: mối nối không "
                "xi măng (Uncemented joint), kích thước d và ghi chú Exposed HT of r,b > d. "
                "Dòng chú thích chung ở cuối cho biết d, d₁, d₂ là khoảng cách rò.",
                "Four simplified cross-sections showing how insulating ribs affect the "
                "creepage path between conductors. Upper left: two conductors on a hatched "
                "insulant base with a rib between them, dimension arrows d and ≥3 and the "
                "annotation <3. Upper right: two conductors joined at a Cemented joint with "
                "dimensions d, ≥3 and ≥1. Lower left: three conductors, the central metal "
                "not electrically connected, with segments d₁, d₂ and c and the expression "
                "d = d₁ + d₂. Lower right: an Uncemented joint with dimension d and the "
                "printed annotation Exposed HT of r,b > d. A shared line beneath states "
                "that d, d₁ and d₂ are creepage distances")


# ------------------------------------------------------------------ 13.20

@_reg
def fig_f1320():
    """Figure 13.20 - composite clearance/separation criteria, A/B/C."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 20, "Tiêu chí khoảng hở và khoảng cách tách tổng hợp",
           "Composite clearance/separation criteria", 7.2)
    _sub(o, "Mặt cắt đồng trục · dây dẫn, cách điện rắn, lớp bọc và dây dẫn ngoài / "
            "Coaxial section · conductor, solid insulation, encapsulant, outer conductor")

    o.append(_circle(200, 148, 56, fill="url(#h7)", sw=1.2))
    o.append(_circle(200, 148, 18, fill="#e9e3d6", sw=1.1))
    o.append(_circle(200, 148, 7, fill="#8a8a8a", sw=1.0))
    o.append(_circle(430, 148, 10, fill="#8a8a8a", sw=1.0))
    o.append(_dimh(256, 420, 92, "A"))
    o.append(_dimh(218, 256, 78, "B"))
    o.append(_dimh(207, 218, 64, "C"))

    _lab(o, 46, 100, "Cách điện rắn", "Solid insulation", "start")
    o.append(_lead(140, 116, 190, 140))
    _lab(o, 40, 190, "Lớp bọc kín", "Encapsulant", "start")
    o.append(_lead(120, 186, 150, 166))
    _lab(o, 90, 234, "Dây dẫn", "Conductor", "start")
    o.append(_lead(146, 222, 199, 162))
    _lab(o, 468, 176, "Dây dẫn", "Conductor", "start")
    o.append(_lead(462, 174, 438, 156))

    o.append(_line(40, 250, 640, 250, sw=0.8, color=GREY))
    o.append(T(90, 264, "A = khoảng hở (A = clearance,)", 6.8, anchor="start", color=INK))
    o.append(T(90, 277, "B = khoảng cách tách qua hợp chất đúc "
                "(B = separation through casting compound,)", 6.8, anchor="start", color=INK))
    o.append(T(90, 290, "C = khoảng cách tách qua cách điện rắn "
                "(C = separation through solid insulation)", 6.8, anchor="start", color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.20")),
                "Hình 13.20 · Tiêu chí khoảng hở/khoảng cách tách hợp thành.",
                "Figure 13.20 · Composite clearance/separation criteria.",
                "Mặt cắt đồng trục gồm một dây dẫn nhỏ ở giữa được bao bởi một vòng cách điện "
                "rắn, rồi đến một khối lớp bọc kín gạch chéo, và một dây dẫn tròn riêng biệt "
                "ở bên phải. Ba mũi tên đo nằm phía trên được ký hiệu A (khoảng hở từ bề mặt "
                "lớp bọc đến dây dẫn ngoài), B (khoảng cách tách qua hợp chất đúc) và C "
                "(khoảng cách tách qua cách điện rắn). Các nhãn dẫn chỉ vào Cách điện rắn, "
                "Lớp bọc kín và hai Dây dẫn. Chú thích ba dòng ở cuối liệt kê A = clearance, "
                "B = separation through casting compound và C = separation through solid "
                "insulation.",
                "A coaxial section with a small central conductor surrounded by a ring of "
                "solid insulation, then a hatched mass of encapsulant, and a separate round "
                "conductor to the right. Three stacked dimension arrows above are marked A "
                "(clearance from the encapsulant surface to the outer conductor), B "
                "(separation through casting compound) and C (separation through solid "
                "insulation). Leaders name Solid insulation, Encapsulant and both Conductors. "
                "The three-line legend gives A = clearance, B = separation through casting "
                "compound and C = separation through solid insulation")


# ------------------------------------------------------------------ 13.21

@_reg
def fig_f1321():
    """Figure 13.21 - composite creepage distance criteria, A/B."""
    w, h = 680, 280
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 21, "Tiêu chí khoảng cách rò bề mặt tổng hợp",
           "Composite creepage distance criteria", 7.2)
    _sub(o, "Mặt cắt qua lớp sơn phủ · rò dưới lớp phủ và rò trong không khí / "
            "Coated section · creepage under coating and in air")

    o.append(_hatch(70, 190, 540, 34))
    o.append(_rect(170, 172, 34, 18, fill="#cfcfcf", sw=1.0))
    o.append(_rect(450, 172, 34, 18, fill="#cfcfcf", sw=1.0))
    o.append(_rect(160, 166, 180, 6, fill="#dedede", sw=0.9))
    o.append(_dimh(204, 340, 136, "A"))
    o.append(_dimh(340, 450, 136, "B"))

    _lab(o, 110, 112, "Dây dẫn", "Conductor", "start")
    o.append(_lead(144, 118, 176, 172))
    _lab(o, 214, 156, "Lớp sơn phủ", "Varnish", "start")
    o.append(_lead(250, 150, 262, 168))
    _lab(o, 470, 106, "Dây dẫn", "Conductor", "start")
    o.append(_lead(466, 112, 466, 170))
    o.append(T(592, 198, "Đế (Substrate)", 6.8, anchor="end", color=INK))
    o.append(_lead(584, 200, 548, 204))
    o.append(T(592, 222, "Cách điện (Insulation)", 6.8, anchor="end", color=INK))
    o.append(_lead(584, 222, 548, 216))

    o.append(_line(40, 234, 640, 234, sw=0.8, color=GREY))
    o.append(T(150, 248, "A = rò dưới lớp phủ (A = creepage under coating,)",
               6.8, color=INK))
    o.append(T(150, 262, "B = rò trong không khí (B = creepage in air)",
               6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.21")),
                "Hình 13.21 · Tiêu chí khoảng cách rò bề mặt tổng hợp.",
                "Figure 13.21 · Composite creepage distance criteria.",
                "Mặt cắt qua một đế cách điện gạch chéo với hai dây dẫn đặt trên bề mặt. "
                "Một lớp sơn phủ mỏng (Varnish) phủ lên dây dẫn bên trái và một phần của "
                "khoảng giữa. Hai mũi tên đo phía trên được ký hiệu A cho đoạn rò dưới lớp "
                "phủ và B cho đoạn rò trong không khí. Các nhãn dẫn chỉ vào Dây dẫn ở hai "
                "bên, Lớp sơn phủ, Đế (Substrate) và Cách điện (Insulation). Chú thích hai "
                "dòng ở cuối định nghĩa A là rò dưới lớp phủ và B là rò trong không khí.",
                "A section through a hatched insulating substrate carrying two conductors. "
                "A thin varnish layer covers the left conductor and part of the gap between "
                "them. Two dimension arrows above are marked A for the creepage path under "
                "the coating and B for the creepage path in air. Leaders identify the two "
                "Conductors, Varnish, Substrate and Insulation. The two-line legend defines "
                "A as creepage under coating and B as creepage in air")


# ------------------------------------------------------------------ 13.22

def _encap_panel(o, cy, kind):
    """One of the four encapsulation cross-sections of Fig. 13.22."""
    if kind == 1:
        o.append(_rect(300, cy - 40, 80, 80, fill="url(#h7)", sw=1.1))
        o.append(_rect(312, cy - 28, 56, 56, fill="#ffffff", sw=1.0))
    elif kind == 2:
        o.append(_rect(294, cy - 46, 92, 92, fill="#333333", sw=1.1))
        o.append(_rect(302, cy - 38, 76, 76, fill="url(#h7)", sw=0.9))
        o.append(_rect(312, cy - 28, 56, 56, fill="#ffffff", sw=1.0))
    elif kind == 3:
        o.append(_rect(294, cy - 46, 12, 92, fill="#333333", sw=0.9))
        o.append(_rect(374, cy - 46, 12, 92, fill="#333333", sw=0.9))
        o.append(_rect(294, cy + 34, 92, 12, fill="#333333", sw=0.9))
        o.append(_rect(306, cy - 46, 68, 80, fill="url(#h7)", sw=0.9))
        o.append(_rect(314, cy - 34, 52, 56, fill="#ffffff", sw=1.0))
    else:
        o.append(_rect(292, cy - 46, 96, 92, fill="#333333", sw=1.1))
        o.append(_rect(302, cy - 36, 76, 72, fill="url(#h7)", sw=0.9))
        o.append(_rect(312, cy - 26, 56, 52, fill="#ffffff", sw=1.0))


@_reg
def fig_f1322():
    """Figure 13.22 - four encapsulation procedures with Notes (1)-(3)."""
    w, h = 680, 520
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 22, "Quy trình bọc kín", "Encapsulation procedures", 7.2)
    _sub(o, "Bốn cấu hình · bề mặt tự do, lớp bọc kín và vỏ bọc / "
            "Four configurations · free surface, encapsulant and enclosure")

    # (1) free surface, encapsulant to Note 1
    _encap_panel(o, 95, 1)
    _lab(o, 30, 66, "Linh kiện hoặc cụm linh kiện", "Component or assembly", "start")
    o.append(T(30, 88, "(encapsulant need not penetrate)", 6.8, anchor="start", color=GREY))
    o.append(_lead(180, 84, 304, 90))
    _lab(o, 650, 62, "Bề mặt tự do", "Free surface", "end")
    o.append(_lead(520, 70, 372, 58))
    _lab(o, 650, 108, "Lớp bọc kín (Lưu ý 1)", "Encapsulant (Note 1)", "end")
    o.append(_lead(520, 114, 376, 100))

    # (2) enclosure, no minimum thickness
    _encap_panel(o, 215, 2)
    _lab(o, 30, 186, "Linh kiện hoặc cụm linh kiện", "Component or assembly", "start")
    o.append(T(30, 208, "(encapsulant need not penetrate)", 6.8, anchor="start", color=GREY))
    o.append(_lead(180, 204, 304, 210))
    o.append(T(30, 250, "Bề mặt tự do (Free surface)", 6.8, anchor="start", color=INK))
    o.append(_lead(190, 246, 300, 256))
    _lab(o, 650, 184, "Lớp bọc kín (không có độ dày tối thiểu)",
         "Encapsulant (no minimum thickness)", "end")
    o.append(T(650, 202, "(Note 3)", 6.8, anchor="end", color=GREY))
    o.append(_lead(520, 196, 382, 204))
    _lab(o, 650, 236, "Vỏ bọc (Lưu ý 2)", "Enclosure (Note 2)", "end")
    o.append(_lead(520, 242, 384, 252))

    # (3) enclosure open at the top, free surface, Note 2 and 3
    _encap_panel(o, 335, 3)
    _lab(o, 30, 306, "Bề mặt tự do", "Free surface", "start")
    o.append(_lead(180, 312, 306, 296))
    _lab(o, 30, 352, "Linh kiện hoặc cụm linh kiện", "Component or assembly", "start")
    o.append(T(30, 374, "(encapsulant need not penetrate)", 6.8, anchor="start", color=GREY))
    o.append(_lead(180, 368, 304, 350))
    _lab(o, 650, 310, "Lớp bọc kín (Lưu ý 1)", "Encapsulant (Note 1)", "end")
    o.append(_lead(520, 316, 378, 306))
    _lab(o, 650, 360, "Vỏ bọc (Lưu ý 2 & 3)", "Enclosure (Note 2 & 3)", "end")
    o.append(_lead(520, 366, 382, 372))

    # (4) metal enclosure both sides
    _encap_panel(o, 455, 4)
    _lab(o, 30, 426, "Vỏ bọc (Lưu ý 2)", "Enclosure (Note 2)", "start")
    o.append(_lead(180, 432, 292, 440))
    _lab(o, 30, 474, "Linh kiện hoặc cụm linh kiện", "Component or assembly", "start")
    o.append(T(30, 496, "(encapsulant need not penetrate)", 6.8, anchor="start", color=GREY))
    o.append(_lead(180, 490, 310, 470))
    _lab(o, 650, 426, "Vỏ bọc (Lưu ý 2)", "Enclosure (Note 2)", "end")
    o.append(_lead(520, 432, 390, 440))
    _lab(o, 650, 474, "Lớp bọc kín (không có độ dày tối thiểu)",
         "Encapsulant (no minimum thickness)", "end")
    o.append(T(650, 492, "(Note 3)", 6.8, anchor="end", color=GREY))
    o.append(_lead(520, 484, 388, 476))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.22")),
                "Hình 13.22 · Quy trình bọc kín. Lưu ý: (1) Lớp bọc kín phải có độ dày bằng "
                "một nửa độ dày yêu cầu cho mục đích tách (Bảng 13.7), với mức tối thiểu "
                "1 mm. (2) Vỏ bọc có thể bằng kim loại hoặc vật liệu cách điện. Kim loại "
                "không có độ dày tối thiểu nhưng vật liệu cách điện phải tuân theo độ dày "
                "quy định cho mục đích tách (Bảng 13.7). (3) Khi vỏ bọc bằng kim loại và có "
                "thể tiếp đất, độ dày của lớp bọc kín bên trong kim loại phải tuân theo "
                "Bảng 13.7 hoặc 13.8 tùy trường hợp nếu việc tiếp đất ảnh hưởng xấu đến an "
                "toàn nội tại",
                "Figure 13.22 · Encapsulation procedures. Notes: (1) Encapsulant must be "
                "half of the thickness required for separation purposes (Table 13.7) with a "
                "1 mm minimum. (2) Enclosure may be metal or insulating material. Metal has "
                "no minimum thickness but insulating material must conform to the thickness "
                "for separation purposes (Table 13.7). (3) Where enclosure is metal and can "
                "be earthed, thickness of encapsulant inside metal must conform to Table "
                "13.7 or 13.8 as appropriate if earthing adversely affects intrinsic safety",
                "Bốn mặt cắt bọc kín xếp dọc. Hình 1 có bề mặt tự do ở trên, lớp bọc kín "
                "gạch chéo bao quanh một linh kiện và nhãn Lưu ý 1. Hình 2 đặt cùng cấu trúc "
                "trong vỏ bọc kim loại dày, với nhãn Lưu ý 2 cho vỏ bọc và Lưu ý 3 cho lớp "
                "bọc không có độ dày tối thiểu. Hình 3 là vỏ bọc hở phía trên, để lộ bề mặt "
                "tự do, mang nhãn Lưu ý 2 và 3. Hình 4 là vỏ bọc kín hai bên. Mỗi hình đều "
                "ghi Linh kiện hoặc cụm linh kiện, với ghi chú rằng lớp bọc không cần thấm "
                "vào bên trong linh kiện; các mũi tên dẫn từ nhãn tới đúng lớp tương ứng.",
                "Four encapsulation cross-sections stacked vertically. The first shows a "
                "free surface above a hatched encapsulant surrounding a component, with a "
                "Note 1 label. The second places the same structure inside a thick metal "
                "enclosure, with Note 2 on the enclosure and Note 3 on an encapsulant of no "
                "minimum thickness. The third has an enclosure open at the top exposing the "
                "free surface, and carries the combined label Note 2 and 3. The fourth is "
                "closed on both sides. Each panel labels the component or assembly with the "
                "remark that the encapsulant need not penetrate it, and leaders connect "
                "every label to the correct layer")


# ------------------------------------------------------------------ 13.23

@_reg
def fig_f1323():
    """Figure 13.23 - Type 2b transformer with earthed screen, Notes (1)-(5)."""
    w, h = 680, 280
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 23, "Máy biến áp Loại 2b", "Type 2b transformer", 7.2)
    _sub(o, "Lõi gạch chéo · hai cuộn dây có màn chắn tiếp đất và lớp cách điện / "
            "Hatched core · two screened windings with insulation")

    o.append(_hatch(170, 60, 340, 170))
    # left winding pair inside a screen
    o.append(_rect(216, 77, 108, 136, fill="none", sw=0.9, dash="3 2", stroke="#555555"))
    o.append(_rect(220, 85, 100, 120, fill="#ffffff", sw=1.1))
    o.append(_rect(226, 91, 44, 108, fill="#e8eef5", sw=0.9))
    o.append(_rect(272, 91, 44, 108, fill="#f5ece0", sw=0.9))
    o.append(_vtxt(248, 145, "Secondary", 6.8))
    o.append(_vtxt(294, 145, "Primary", 6.8))
    # right winding pair
    o.append(_rect(366, 77, 108, 136, fill="none", sw=0.9, dash="3 2", stroke="#555555"))
    o.append(_rect(370, 85, 100, 120, fill="#ffffff", sw=1.1))
    o.append(_rect(376, 91, 44, 108, fill="#f5ece0", sw=0.9))
    o.append(_rect(422, 91, 44, 108, fill="#e8eef5", sw=0.9))
    o.append(_vtxt(398, 145, "Primary", 6.8))
    o.append(_vtxt(444, 145, "Secondary", 6.8))

    _lab(o, 270, 48, "Các cuộn dây (Lưu ý 5)", "Windings (Note 5)", "middle")
    o.append(_lead(270, 54, 270, 78))
    o.append(T(100, 100, "Lõi máy biến áp (Lưu ý 1)", 6.8, anchor="start", color=INK))
    o.append(T(100, 112, "(Transformer core (Note 1))", 6.8, anchor="start", color=GREY))
    o.append(_lead(196, 104, 196, 120))
    _lab(o, 270, 250, "Màn chắn (Lưu ý 2)", "Screen (Note 2)", "middle")
    o.append(_lead(270, 240, 270, 214))
    _lab(o, 470, 250, "Cách điện (Lưu ý 3)", "Insulation (Note 3)", "middle")
    o.append(_lead(470, 240, 470, 214))
    o.append(T(568, 130, "Cách điện (Lưu ý 4)", 6.8, anchor="start", color=INK))
    o.append(T(568, 142, "(Insulation (Note 4))", 6.8, anchor="start", color=GREY))
    o.append(_lead(562, 136, 470, 136))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.23")),
                "Hình 13.23 · Máy biến áp Loại 2b. Lưu ý: (1) Lõi phải được nối đất (xen kẽ "
                "trong các lá thép nếu phù hợp) trừ khi vật liệu lõi không dẫn điện. (2) Màn "
                "chắn phải có hai dây nối đất nếu làm bằng lá kim loại; nếu dùng các lớp dây "
                "thì cả hai lớp phải đưa một đầu ra. (3) Cách điện theo yêu cầu công nghiệp "
                "thông thường. (4) Cách điện phải chịu được thử nghiệm 500V trừ khi không "
                "chấp nhận được lỗi tiếp đất, khi đó áp dụng Bảng 13.7 tùy trường hợp. (5) "
                "Các cuộn dây phải được cố kết chặt",
                "Figure 13.23 · Type 2b transformer. Notes: (1) Core to be provided with "
                "earth connection (interleaved in laminations if appropriate) unless core "
                "material is non-conducting. (2) Screen to be provided with two earth "
                "connection wires if foil; both layers to have one end brought out if wire "
                "layers. (3) Insulation to normal industrial requirements. (4) Insulation to "
                "withstand 500V test unless earth faults not acceptable when Table 13.7 "
                "applies, as appropriate. (5) Windings to be consolidated",
                "Mặt cắt máy biến áp kiểu vỏ với lõi gạch chéo bao quanh hai bộ cuộn dây đặt "
                "cạnh nhau trên cùng một trục. Mỗi bộ gồm nửa cuộn Secondary và nửa cuộn "
                "Primary, được đặt trong một màn chắn đã nối đất và phân cách bằng lớp cách "
                "điện. Nhãn Lưu ý 1 chỉ lõi và yêu cầu nối đất, Lưu ý 2 chỉ màn chắn và hai "
                "dây nối đất, Lưu ý 3 và Lưu ý 4 chỉ các lớp cách điện ở mép cuộn. Nhãn Các "
                "cuộn dây mang Lưu ý 5 về việc cố kết chặt các cuộn dây.",
                "Section of a shell-type transformer whose hatched core encloses two "
                "windings side by side. Each assembly has a Secondary half and a Primary "
                "half, enclosed by an earthed screen and separated by insulating layers. "
                "The Note 1 label points to the core and its earth connection, Note 2 to "
                "the screen and its two earth wires, and Notes 3 and 4 to the insulation at "
                "the winding edges. The Windings label carries Note 5 on consolidation of "
                "the windings")


# ------------------------------------------------------------------ 13.24

@_reg
def fig_f1324():
    """Figure 13.24 - Type 1a transformer, Notes (1)-(6)."""
    w, h = 680, 270
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 24, "Máy biến áp Loại 1a", "Type 1a transformer", 7.2)
    _sub(o, "Lõi kiểu lõi · hai cuộn đặt cạnh nhau trên cùng một chân lõi / "
            "Core-type core · two windings side by side on one limb")

    o.append(_hatch(180, 60, 320, 150))
    for x0 in (245, 365):
        o.append(_rect(x0 - 6, 79, 82, 112, fill="none", sw=0.9, dash="3 2", stroke="#555555"))
        o.append(_rect(x0, 85, 70, 100, fill="#ffffff", sw=1.1))
        o.append(_rect(x0 + 3, 88, 64, 47, fill="#f5ece0", sw=0.9))
        o.append(_rect(x0 + 3, 135, 64, 47, fill="#e8eef5", sw=0.9))
        o.append(T(x0 + 35, 116, "Primary", 6.8, color=INK))
        o.append(T(x0 + 35, 163, "Secondary", 6.8, color=INK))

    o.append(T(150, 54, "Cách điện (Lưu ý 2)", 6.8, anchor="middle", color=INK))
    o.append(T(150, 66, "(Insulation (Note 2))", 6.8, anchor="middle", color=GREY))
    o.append(_lead(150, 70, 240, 84))
    o.append(T(560, 66, "Lõi (Lưu ý 1)", 6.8, anchor="start", color=INK))
    o.append(T(560, 78, "(Core (Note 1))", 6.8, anchor="start", color=GREY))
    o.append(_lead(554, 70, 498, 84))
    o.append(T(70, 150, "Cách điện (Lưu ý 5)", 6.8, anchor="start", color=INK))
    o.append(T(70, 162, "(Insulation (Note 5))", 6.8, anchor="start", color=GREY))
    o.append(_lead(160, 154, 240, 154))
    o.append(T(70, 196, "Cách điện (Lưu ý 3)", 6.8, anchor="start", color=INK))
    o.append(T(70, 208, "(Insulation (Note 3))", 6.8, anchor="start", color=GREY))
    o.append(_lead(160, 198, 240, 178))
    o.append(T(520, 232, "Các cuộn dây (Lưu ý 4 và 6)", 6.8, anchor="start", color=INK))
    o.append(T(520, 244, "(Windings (Notes 4 and 6))", 6.8, anchor="start", color=GREY))
    o.append(_lead(516, 226, 436, 180))
    _earth(o, 340, 208)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.24")),
                "Hình 13.24 · Máy biến áp Loại 1a. Lưu ý: (1) Lõi phải được nối đất (xen kẽ "
                "trong các lá thép nếu phù hợp) trừ khi vật liệu lõi không dẫn điện. (2) "
                "Cách điện theo tiêu chuẩn công nghiệp thông thường. (3) Cách điện phải chịu "
                "được thử nghiệm 500V trừ khi không chấp nhận được lỗi tiếp đất, khi đó áp "
                "dụng Bảng 13.10. (4) Nếu cần thiết để tránh quá nhiệt, phải lắm công tắc "
                "nhiệt ngay trong cuộn sơ cấp hoặc thứ cấp (tùy trường hợp). (5) Cách điện "
                "theo Bảng 13.10. (6) Các cuộn dây phải được cố kết chặt",
                "Figure 13.24 · Type 1a transformer. Notes: (1) Core to be provided with "
                "earth connection (interleaved in laminations if appropriate) unless core "
                "material is non-conducting. (2) Insulation to normal industrial standards. "
                "(3) Insulation to withstand 500V test unless earth faults are not acceptable "
                "when Table 13.10 applies. (4) If necessary to prevent overheating, thermal "
                "trip embedded in either primary or secondary (as appropriate). (5) Insulation "
                "to Table 13.10. (6) Windings to be consolidated",
                "Hai cuộn dây đặt cạnh nhau trên cùng một chân của lõi kiểu lõi gạch chéo. "
                "Mỗi cuộn chia làm hai phần, Primary ở trên và Secondary ở dưới, được bao "
                "bởi một đường viền cách điện. Lõi có ký hiệu nối đất ở dưới. Các nhãn dẫn "
                "chỉ vào Lõi (Lưu ý 1), ba vị trí Cách điện tương ứng Lưu ý 2, Lưu ý 3 và "
                "Lưu ý 5, và Các cuộn dây mang Lưu ý 4 và 6 cho công tắc nhiệt và việc cố "
                "kết. Các nhãn Primary và Secondary nằm ngay trong từng nửa cuộn.",
                "Two windings sit side by side on one limb of a hatched core-type core. "
                "Each winding is split into an upper Primary half and a lower Secondary "
                "half, enclosed by an insulation outline. The core carries an earth symbol "
                "below it. Leaders point to Core (Note 1), three Insulation positions for "
                "Notes 2, 3 and 5, and the Windings label carrying Notes 4 and 6 for the "
                "thermal trip and consolidation. Primary and Secondary are printed inside "
                "their respective half-windings")


# ------------------------------------------------------------------ 13.25

@_reg
def fig_f1325():
    """Figure 13.25 - Type 1b transformer, Notes (1)-(6)."""
    w, h = 680, 280
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 25, "Máy biến áp Loại 1b", "Type 1b transformer", 7.2)
    _sub(o, "Lõi kiểu vỏ · các cuộn riêng biệt trên các chân khác nhau / "
            "Shell-type core · separate windings on separate limbs")

    o.append(_hatch(200, 70, 280, 140))
    for x0, out in ((265, "Primary"), (360, "Primary")):
        o.append(_rect(x0 - 5, 84, 68, 112, fill="none", sw=0.9, dash="3 2", stroke="#555555"))
        o.append(_rect(x0, 90, 58, 100, fill="#ffffff", sw=1.1))
        o.append(_rect(x0 + 3, 93, 52, 47, fill="#f5ece0", sw=0.9))
        o.append(_rect(x0 + 3, 140, 52, 47, fill="#e8eef5", sw=0.9))
        o.append(T(x0 + 29, 119, "Primary", 6.8, color=INK))
        o.append(T(x0 + 29, 166, "Secondary", 6.8, color=INK))
    for x0, lab in ((150, "Primary"), (492, "Secondary")):
        o.append(_rect(x0, 95, 38, 90, fill="#ffffff", sw=1.1))
        o.append(_vtxt(x0 + 19, 140, lab, 6.8))

    _lab(o, 250, 58, "Lõi (Lưu ý 1)", "Core (Note 1)", "middle")
    o.append(_lead(250, 64, 250, 72))
    _lab(o, 440, 58, "Các cuộn dây (Lưu ý 4 và 6)", "Windings (Notes 4 and 6)", "middle")
    o.append(_lead(440, 64, 440, 84))
    _lab(o, 96, 210, "Cách điện (Lưu ý 2)", "Insulation (Note 2)", "start")
    o.append(_lead(180, 204, 264, 186))
    _lab(o, 290, 244, "Cách điện (Lưu ý 5)", "Insulation (Note 5)", "middle")
    o.append(_lead(290, 236, 290, 192))
    _lab(o, 430, 244, "Cách điện (Lưu ý 3)", "Insulation (Note 3)", "middle")
    o.append(_lead(430, 236, 415, 192))
    _earth(o, 340, 210)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.25")),
                "Hình 13.25 · Máy biến áp Loại 1b. Lưu ý: (1) Lõi phải được nối đất (xen kẽ "
                "trong các lá thép nếu phù hợp) trừ khi vật liệu lõi không dẫn điện. (2) "
                "Cách điện theo tiêu chuẩn công nghiệp thông thường. (3) Cách điện phải chịu "
                "được thử nghiệm 500V trừ khi không chấp nhận được lỗi tiếp đất, khi đó áp "
                "dụng Bảng 13.7. (4) Nếu cần thiết để tránh quá nhiệt, phải lắm công tắc "
                "nhiệt ngay trong một trong hai cuộn dây (tùy trường hợp). (5) Cách điện "
                "theo Bảng 13.7. (6) Các cuộn dây phải được cố kết chặt",
                "Figure 13.25 · Type 1b transformer. Notes: (1) Core to be provided with "
                "earth connection (interleaved in laminations if appropriate) unless core "
                "material is non-conducting. (2) Insulation to normal industrial standards. "
                "(3) Insulation to withstand 500V test unless earth faults are not acceptable "
                "when Table 13.7 applies. (4) If necessary to prevent overheating, thermal "
                "trip embedded in either winding (as appropriate). (5) Insulation to Table "
                "13.7. (6) Windings to be consolidated",
                "Lõi kiểu vỏ gạch chéo gồm một chân giữa đi qua các cuộn và hai chân ngoài "
                "bao quanh. Trên chân giữa là hai cuộn riêng biệt, mỗi cuộn có nửa Primary và "
                "nửa Secondary, trong khi hai cuộn ngoài lần lượt mang nhãn Primary và "
                "Secondary. Lõi có ký hiệu nối đất. Các nhãn dẫn chỉ vào Lõi (Lưu ý 1), ba "
                "vị trí cách điện theo Lưu ý 2, 3 và 5, cùng nhãn Các cuộn dây mang Lưu ý 4 "
                "và 6 về công tắc nhiệt và cố kết cuộn dây.",
                "A hatched shell-type core has a centre limb passing through the windings "
                "and two outer limbs surrounding them. Two separate windings on the centre "
                "limb each have a Primary half and a Secondary half, while the two outer "
                "windings are labelled Primary and Secondary. The core carries an earth "
                "symbol. Leaders identify Core (Note 1), three insulation positions for "
                "Notes 2, 3 and 5, and the Windings label with Notes 4 and 6 on the thermal "
                "trip and consolidation")


# ------------------------------------------------------------------ 13.26

@_reg
def fig_f1326():
    """Figure 13.26 - Type 2a transformer, no screen, Notes (1)-(6)."""
    w, h = 680, 280
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 26, "Máy biến áp Loại 2a", "Type 2a transformer", 7.2)
    _sub(o, "Không có màn chắn · các cuộn chồng lên nhau chỉ cách nhau bằng lớp cách điện / "
            "No screen · windings stacked with insulation only")

    o.append(_hatch(180, 60, 320, 150))
    for x0, left, right in ((235, "Secondary", "Primary"), (355, "Primary", "Secondary")):
        o.append(_rect(x0 - 6, 79, 112, 112, fill="none", sw=0.9, dash="3 2", stroke="#555555"))
        o.append(_rect(x0, 85, 100, 100, fill="#ffffff", sw=1.1))
        o.append(_rect(x0 + 3, 88, 44, 94, fill="#e8eef5" if left == "Secondary" else "#f5ece0", sw=0.9))
        o.append(_rect(x0 + 53, 88, 44, 94, fill="#f5ece0" if right == "Primary" else "#e8eef5", sw=0.9))
        o.append(_vtxt(x0 + 25, 135, left, 6.8))
        o.append(_vtxt(x0 + 75, 135, right, 6.8))

    _lab(o, 250, 48, "Các cuộn dây (Lưu ý 4 và 6)", "Windings (Notes 4 and 6)", "middle")
    o.append(_lead(250, 54, 250, 80))
    _lab(o, 470, 48, "Cách điện (Lưu ý 2)", "Insulation (Note 2)", "middle")
    o.append(_lead(470, 54, 470, 80))
    o.append(T(60, 124, "Lõi (Lưu ý 1)", 6.8, anchor="start", color=INK))
    o.append(T(60, 136, "(Core (Note 1))", 6.8, anchor="start", color=GREY))
    o.append(_lead(140, 130, 180, 136))
    o.append(T(570, 138, "Cách điện (Lưu ý 5)", 6.8, anchor="start", color=INK))
    o.append(T(570, 150, "(Insulation (Note 5))", 6.8, anchor="start", color=GREY))
    o.append(_lead(564, 142, 460, 148))
    o.append(T(570, 202, "Cách điện (Lưu ý 3)", 6.8, anchor="start", color=INK))
    o.append(T(570, 214, "(Insulation (Note 3))", 6.8, anchor="start", color=GREY))
    o.append(_lead(564, 206, 458, 172))
    _earth(o, 340, 208)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.26")),
                "Hình 13.26 · Máy biến áp Loại 2a. Lưu ý: (1) Lõi phải được nối đất (xen kẽ "
                "trong các lá thép nếu phù hợp) trừ khi vật liệu không dẫn điện. (2) Cách "
                "điện theo tiêu chuẩn công nghiệp thông thường. (3) Cách điện phải chịu được "
                "thử nghiệm 500V trừ khi không chấp nhận được lỗi tiếp đất, khi đó áp dụng "
                "Bảng 13.10. (4) Nếu cần thiết để tránh quá nhiệt công tắc nhiệt được lắm "
                "trong cuộn sơ cấp hoặc thứ cấp (tùy trường hợp). (5) Cách điện theo Bảng "
                "13.10. (6) Các cuộn dây phải được cố kết chặt",
                "Figure 13.26 · Type 2a transformer. Notes: (1) Core to be provided with "
                "earth connection (interleaved in laminations if appropriate) unless material "
                "is non-conducting. (2) Insulation to normal industrial standards. (3) "
                "Insulation to withstand 500V test unless earth faults are not acceptable "
                "when Table 13.10 applies. (4) If necessary to prevent overheating thermal "
                "trip embedded in primary or secondary winding (as appropriate). (5) "
                "Insulation to Table 13.10. (6) Windings to be consolidated",
                "Lõi gạch chéo với hai bộ cuộn đặt cạnh nhau nhưng không có màn chắn; giữa "
                "các cuộn chỉ có lớp cách điện. Bộ bên trái gồm nửa Secondary và nửa Primary, "
                "bộ bên phải gồm nửa Primary và nửa Secondary, toàn bộ nằm trong viền cách "
                "điện. Lõi có ký hiệu nối đất. Các nhãn dẫn chỉ Lõi (Lưu ý 1), Cách điện "
                "(Lưu ý 2), các vị trí cách điện theo Lưu ý 3 và Lưu ý 5, và Các cuộn dây "
                "mang Lưu ý 4 và 6.",
                "A hatched core encloses two winding assemblies side by side with no screen "
                "between them; insulation alone separates the windings. The left assembly "
                "has a Secondary half and a Primary half, the right a Primary half and a "
                "Secondary half, each inside an insulation outline. The core carries an earth "
                "symbol. Leaders identify Core (Note 1), Insulation (Note 2), the insulation "
                "positions of Notes 3 and 5, and the Windings label with Notes 4 and 6")


# ------------------------------------------------------------------ 13.27

@_reg
def fig_f1327():
    """Figure 13.27 - transformer winding/core or screen fault paths, Notes (1)-(2)."""
    w, h = 680, 330
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 27, "Ảnh hưởng của lỗi cuộn dây/lõi hoặc màn chắn máy biến áp",
           "Effect of transformer winding/core or screen faults", 7.0)
    _sub(o, "Sơ đồ đường lỗi · cầu chì, máy biến áp, điện trở hạn dòng và lỗi tiếp đất hiện "
            "trường / Fault-path schematic · fuse, transformer, limiting resistor, field earth fault")

    # Mains terminals and source symbol.
    o.append(_circle(70, 110, 5, fill="#ffffff", sw=1.1))
    o.append(_circle(70, 238, 5, fill="#ffffff", sw=1.1))
    o.append(T(70, 70, "~", 9.5, color=INK))
    _bi(o, 70, 88, "Nguồn", "Mains", 6.8)

    # Primary circuit: fuse then winding.
    o.append(_line(75, 110, 122, 110, sw=1.1))
    o.append(_rect(122, 104, 34, 12, fill="#ffffff", sw=1.1))
    o.append(_line(156, 110, 210, 110, sw=1.1))
    _bi(o, 140, 84, "Cầu chì bảo vệ", "Protective fuse", 6.8)
    _lead(140, 94, 140, 102)
    _coil(o, 210, 118, 232, 7)
    _bi(o, 210, 60, "Máy biến áp", "Transformer", 6.8)
    o.append(_line(70, 238, 210, 238, sw=1.1))

    # Core and its earth, point A.
    o.append(_line(226, 118, 226, 238, sw=0.9, color="#555555"))
    o.append(_line(226, 238, 226, 258, sw=1.1))
    _earth(o, 226, 258)
    _bi(o, 266, 286, "A (Lưu ý 2)", "A (Note 2)", 6.8)

    # Secondary circuit and limiting resistor.
    _coil(o, 300, 118, 232, 7)
    o.append(_line(300, 118, 300, 108, sw=1.1))
    o.append(_line(300, 108, 370, 108, sw=1.1))
    _resistor(o, 370, 446, 108)
    o.append(_line(446, 108, 520, 108, sw=1.1))
    o.append(_circle(520, 108, 4, fill=INK, sw=0))
    o.append(_line(520, 108, 632, 108, sw=1.1))
    o.append(_line(300, 238, 520, 238, sw=1.1))
    o.append(_circle(520, 238, 4, fill=INK, sw=0))
    o.append(_line(520, 238, 632, 238, sw=1.1))
    _bi(o, 408, 58, "Điện trở hạn dòng", "Current limiting resistor", 6.8)
    o.append(_vtxt(548, 172, "Output terminals / Đầu ra", 6.8, color=GREY))

    # Transformer fault path (dashed) to the field earth fault.
    o.append(_line(300, 118, 332, 118, sw=1.0, color=RED))
    o.append(T(470, 80, "Lỗi máy biến áp (Lưu ý 1)", 6.8, color=RED))
    o.append(T(470, 90, "(Transformer fault (Note 1))", 6.8, color=GREY))
    o.append(_line(332, 118, 332, 96, sw=1.0, color=RED, dash="4 3"))
    o.append(_line(332, 96, 604, 96, sw=1.0, color=RED, dash="4 3"))
    o.append(_line(604, 96, 604, 108, sw=1.0, color=RED, dash="4 3"))
    o.append(_line(604, 108, 604, 250, sw=1.0, color=RED, dash="4 3"))
    _earth(o, 604, 250)
    o.append(T(604, 292, "Lỗi tiếp đất hiện trường (Lưu ý 1)", 6.8, anchor="middle", color=RED))
    o.append(T(604, 304, "(Field earth fault (Note 1))", 6.8, anchor="middle", color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.27")),
                "Hình 13.27 · Ảnh hưởng của lỗi cuộn dây/lõi hoặc màn chắn của máy biến áp. "
                "Lưu ý: (1) Lỗi tiếp đất tại hiện trường có thể được coi là vận hành bình "
                "thường, do đó lỗi giữa cuộn thứ cấp và khung của máy biến áp (dù là một lỗi "
                "đếm được đơn lẻ hay lỗi không đếm được) sẽ đi tắt qua điện trở hạn dòng, "
                "phá hủy an toàn nội tại. (2) Nếu điểm này được nối đất không sai hỏng thì "
                "lỗi máy biến áp như đã vẽ chỉ làm chảy cầu chì bảo vệ, để an toàn nội tại "
                "nguyên vẹn",
                "Figure 13.27 · Effect of transformer winding/core or screen faults. Notes: "
                "(1) Field earth fault can be expected as normal operation and thus "
                "secondary/frame fault in transformer (either as single countable fault or "
                "non-countable fault) will bypass current limiting resistor destroying "
                "intrinsic safety. (2) If this point is infallibly earthed transformer fault "
                "shown will merely blow protective fuse leaving intrinsic safety intact",
                "Sơ đồ mạch có nguồn xoay chiều ở bên trái đi qua cầu chì bảo vệ tới cuộn sơ "
                "cấp của máy biến áp; cuộn thứ cấp nối qua điện trở hạn dòng tới hai đầu ra. "
                "Lõi máy biến áp được nối đất tại điểm A mang Lưu ý 2. Một đường lỗi đứt nét "
                "màu đỏ đi từ lỗi cuộn máy biến áp (Lưu ý 1) tới điểm lỗi tiếp đất hiện "
                "trường (Lưu ý 1) ở đầu ra, cho thấy đường đi tắt qua điện trở hạn dòng. "
                "Các nhãn Đầu ra được đặt dọc theo cột đầu ra.",
                "Circuit schematic with an AC mains source at the left feeding a protective "
                "fuse and then the transformer primary; the secondary passes through a "
                "current limiting resistor to two output terminals. The transformer core is "
                "earthed at point A, labelled Note 2. A red dashed fault path runs from the "
                "transformer fault (Note 1) to the field earth fault (Note 1) at the output, "
                "showing how the limiting resistor can be bypassed. The Output terminals "
                "label is set vertically beside the two output dots")
