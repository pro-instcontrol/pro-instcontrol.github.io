# -*- coding: utf-8 -*-
"""Vector redraws of Figures 16.1-16.2 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 16 "Other methods of protection
and future apparatus requirements".

The two drawings are simplified vector redraws of the rendered pages
p498 and p499. Fig. 16.1 is the solid-black geometric CE / Community Mark:
a bold open C and a matching E with a middle bar, with no lettering inside.
Fig. 16.2 is a bold flat-topped hexagonal outline enclosing the marking
"Ex" (a capital E and a lowercase x), with no legend, axis, scale or note.
Printed English caption wording is retained verbatim. Every displayed
string is literal Unicode. Each public callable returns the standard
five-tuple through ``vfig._fig()`` and is registered in ``FIGS`` by the
``_reg`` decorator.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (_defs, _fig, _f, _line, _path, _poly, _rect, _txt, svg,
                  INK, PAPER)

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

def _band(cx, cy, r_out, r_in, a0, a1):
    """Solid annular sector: thick open arc with square-cut terminals.

    Angles are degrees in SVG coordinates (0 east, 90 south, 180 west,
    270 north); a0 -> a1 is taken in the positive, clockwise direction.
    """
    def pt(r, a):
        t = math.radians(a)
        return (cx + r * math.cos(t), cy + r * math.sin(t))

    x0, y0 = pt(r_out, a0)
    x1, y1 = pt(r_out, a1)
    x2, y2 = pt(r_in, a1)
    x3, y3 = pt(r_in, a0)
    large = 1 if abs(a1 - a0) > 180 else 0
    return ("M%s %s A%s %s 0 %d 1 %s %s L%s %s A%s %s 0 %d 0 %s %s Z"
            % (_f(x0), _f(y0), _f(r_out), _f(r_out), large, _f(x1), _f(y1),
               _f(x2), _f(y2), _f(r_in), _f(r_in), large, _f(x3), _f(y3)))


def _ce_glyph(o, cx, cy, radius, thickness, bar=None):
    """One bold geometric CE letter: open arc plus optional middle bar."""
    o.append(_path(_band(cx, cy, radius, radius - thickness, 88, 272),
                   fill=INK, sw=0, color=INK))
    if bar is not None:
        # Middle bar of the E: from the outer left edge to the terminal.
        bw, bh = bar
        o.append(_rect(cx - radius, cy - bh / 2.0, bw, bh,
                       fill=INK, sw=0))


def _heading(o, vi, en, detail):
    """Two separated bilingual heading lines plus a small grey descriptor."""
    o.append(T(340, 16, vi, 7.6, color=INK, weight="600"))
    o.append(T(340, 28, en, 7.6, color=INK, weight="600"))
    o.append(T(340, 41, detail, 6.8, color=INK))


# ------------------------------------------------------------------ 16.1

@_reg
def fig_f1601():
    """Figure 16.1 - the solid-black geometric CE / Community Mark."""
    w, h = 680, 366
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _heading(o,
             "Hình 16.1 · Dấu cộng đồng",
             "Figure 16.1 · The community mark",
             "Biểu tượng · chữ C và E đen đặc, không có nhãn bên trong / "
             "Symbol · solid black C and E, no labels inside")

    # The C and the E share the same radius, stroke weight and baseline.
    # C: thick open arc, terminals cut square at the upper and lower right.
    _ce_glyph(o, 286, 205, 130, 36)
    # E: the same arc with a horizontal middle bar running out to the right.
    _ce_glyph(o, 519, 205, 130, 36, bar=(136, 42))

    return _fig(svg(w, h, "".join(o), esc("Fig 16.1")),
                "Hình 16.1 · Dấu cộng đồng",
                "Figure 16.1 · The community mark",
                "Dấu CE đen đặc gồm hai chữ cái hình học lớn. Bên trái là chữ C "
                "được tạo bởi một vòng cung tròn dày, hở sang phải, với hai đầu "
                "cắt phẳng ở trên và dưới. Bên phải là chữ E cùng kiểu, gồm vòng "
                "cung dày và một thanh ngang chạy ra phía phải ở giữa chiều cao. "
                "Bên trong hình không có chữ, chú giải, trục hay tỉ lệ",
                "A large solid-black CE mark made of two geometric letters. On "
                "the left a bold C is drawn as a thick circular arc open to the "
                "right, with square-cut terminals at the top and bottom. On the "
                "right a matching bold E is the same thick arc with a horizontal "
                "middle bar extending to the right. There is no lettering, "
                "legend, axis or scale inside the artwork")


# ------------------------------------------------------------------ 16.2

@_reg
def fig_f1602():
    """Figure 16.2 - the bold hexagonal explosion protection mark with Ex."""
    w, h = 680, 410
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _heading(o,
             "Hình 16.2 · Dấu bảo vệ chống nổ",
             "Figure 16.2 · The explosion protection mark",
             "Biểu tượng · lục giác viền đậm bao quanh chữ Ex / "
             "Symbol · bold hexagon enclosing the letters Ex")

    # Flat-topped regular hexagon: pointed left and right vertices.
    cx, cy, a, b = 340, 240, 160, 138
    hex_pts = [(cx - a, cy), (cx - a / 2.0, cy - b), (cx + a / 2.0, cy - b),
               (cx + a, cy), (cx + a / 2.0, cy + b), (cx - a / 2.0, cy + b)]
    o.append(_poly(hex_pts, fill=PAPER, sw=14, color=INK, close=True))

    # Bold capital E: thick rounded-stem form with a middle bar.
    _ce_glyph(o, 326, 240, 84, 22, bar=(89, 22))

    # Bold lowercase x: two crossing diagonal strokes, filling a square
    # only about half the height of the capital E and sharing its baseline.
    def stroke(p, q, half=10):
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = math.hypot(dx, dy)
        nx, ny = -dy / length * half, dx / length * half
        return [(p[0] - nx, p[1] - ny), (q[0] - nx, q[1] - ny),
                (q[0] + nx, q[1] + ny), (p[0] + nx, p[1] + ny)]

    o.append(_poly(stroke((352, 236), (438, 316)),
                   fill=INK, sw=0, close=True))
    o.append(_poly(stroke((438, 236), (352, 316)),
                   fill=INK, sw=0, close=True))

    return _fig(svg(w, h, "".join(o), esc("Fig 16.2")),
                "Hình 16.2 · Dấu bảo vệ chống nổ",
                "Figure 16.2 · The explosion protection mark",
                "Một hình lục giác đều viền đen dày, có cạnh trên và dưới nằm "
                "ngang, hai đỉnh nhọn ở trái và phải. Bên trong, ở giữa, là chữ "
                "E hoa đậm với thân cong dày và thanh ngang ở giữa, theo sau là "
                "chữ x thường đậm hơn nhỏ, gồm hai nét chéo cắt nhau cùng đường "
                "cơ sở với chữ E. Không có chú giải, trục, tỉ lệ hay ghi chú",
                "A large bold regular hexagon outlined in black, with flat "
                "horizontal top and bottom edges and pointed left and right "
                "vertices. Centred inside it is a bold capital E with a thick "
                "curved stem and a middle bar, followed by a smaller bold "
                "lowercase x formed by two crossing diagonal strokes on the "
                "same baseline. There is no legend, axis, scale or footnote")
