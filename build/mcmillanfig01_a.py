# -*- coding: utf-8 -*-
"""Vector redraws of Figures 1-1 to 1-3 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 1 "Introduction".

Fig. 1-1 is the explosion triangle, Fig. 1-2 the Davy safety lamp and
Fig. 1-3 the Distinctive Community Mark. All are drawn as simplified,
bilingual VI/EN SVG vectors; no raster art is used. Architecture mirrors
`expbfig01.py`: each function returns the standard five-tuple through
`vfig._fig()` and is registered in `FIGS` by the `_reg` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _defs, _fig,
                  _line, _path, _poly, _rect, _txt, svg)

YELLOW = "#f4d03f"

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


@_reg
def fig_f101():
    """Figure 1-1 - The explosion triangle (fuel, oxygen, ignition)."""
    w, h = 680, 360
    o = [_defs()]
    o.append(T(340, 18,
               "Tam giác nổ / Explosion triangle — Ba yếu tố cần có / Three required elements",
               9.6, color=INK, weight="600"))

    # Inverted triangle with three inward arrows.
    o.append(_poly([(200, 78), (480, 78), (340, 268)],
                   fill="none", sw=5.0, color=INK, close=True))
    o.append(_arrow(246, 108, 306, 152, sw=1.5, color=GREY))
    o.append(_arrow(434, 108, 374, 152, sw=1.5, color=GREY))
    o.append(_arrow(340, 250, 340, 208, sw=1.5, color=GREY))
    o.append(T(340, 184, "Vụ nổ / Explosion", 11.5, color=INK, weight="600"))

    # Corner callouts: Vietnamese first, English second.
    o.append(T(196, 48, "Nhiên liệu / Fuel", 8.4, anchor="end",
               color=INK, weight="600"))
    o.append(T(196, 60, "(khí, hơi, sương mù hoặc bụi dễ cháy)", 6.3,
               anchor="end", color=GREY))
    o.append(T(196, 71, "(flammable gas, vapour, mist or dust)", 6.2,
               anchor="end", color=GREY))
    o.append(T(484, 48, "Oxy / Oxygen", 8.4, anchor="start",
               color=INK, weight="600"))
    o.append(T(484, 60, "(không khí / air)", 6.4, anchor="start", color=GREY))
    o.append(T(340, 292, "Nguồn đánh lửa / Ignition source", 8.4,
               color=INK, weight="600"))
    o.append(T(340, 304, "(sự vận hành hoặc sai vận hành của thiết bị điện)", 6.3,
               color=GREY))
    o.append(T(340, 315, "(operation or maloperation of electrical equipment)", 6.2,
               color=GREY))
    o.append(T(340, 344,
               "Hình 1-1 · Tam giác nổ / Figure 1-1 · Explosion triangle",
               6.5, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Tam giác nổ đảo với Nhiên liệu, Oxy, Nguồn đánh lửa và Vụ nổ ở giữa")),
                "Hình 1-1 · Tam giác nổ: Nhiên liệu (khí, hơi, sương mù hoặc bụi dễ cháy), "
                "Oxy (không khí) và Nguồn đánh lửa (sự vận hành hoặc sai vận hành thiết bị điện) "
                "cùng hội tụ gây ra vụ nổ",
                "Figure 1-1 · The explosion triangle: Fuel (flammable gas, vapour, mist or "
                "dust), Oxygen (air) and an Ignition source (operation or maloperation of "
                "electrical equipment) coincide to cause an explosion",
                "Tam giác nổ đảo với nhãn Nhiên liệu và Oxy ở hai góc trên, Nguồn đánh lửa ở đáy, "
                "ba mũi tên hướng vào chữ Vụ nổ ở giữa",
                "Inverted explosion triangle with Fuel and Oxygen at the upper corners, "
                "Ignition source at the apex below, and three arrows pointing inwards to "
                "Explosion in the centre")


@_reg
def fig_f102():
    """Figure 1-2 - Principle of the Davy safety lamp."""
    w, h = 680, 396
    o = [_defs()]
    o.append(T(340, 18, "Nguyên lý đèn Davy / Principle of Davy Lamp", 9.8,
               color=INK, weight="600"))
    o.append(T(340, 33,
               "Methane vào được nhưng không cháy lan ra ngoài / Methane enters but cannot ignite outside",
               6.8, color=GREY))

    # Hanging loop, hood and cylindrical body.
    o.append(_circle(340, 52, 11, fill="none", sw=1.8))
    o.append(_circle(340, 52, 6, fill="none", sw=1.4))
    o.append(_poly([(316, 84), (364, 84), (374, 150), (306, 150)],
                   fill=PAPER, sw=1.6, color=INK, close=True))
    o.append(_rect(306, 150, 68, 150, fill=PAPER, sw=1.6))
    o.append(_line(306, 150, 374, 150, sw=1.6))

    # Gauze flame trap drawn as a fine metal grid.
    gx, gy, gw, gh = 312, 176, 56, 90
    o.append(_rect(gx, gy, gw, gh, fill=PAPER, sw=1.0, stroke=GREY))
    for x in range(gx + 7, gx + gw, 7):
        o.append(_line(x, gy, x, gy + gh, sw=0.5, color="#b9b0a0"))
    for yy in range(gy + 7, gy + gh, 7):
        o.append(_line(gx, yy, gx + gw, yy, sw=0.5, color="#b9b0a0"))

    # Flame: outer teardrop and bright core.
    o.append(_path("M340,184 C328,200 326,214 333,226 C336,232 344,232 347,226 "
                   "C354,214 352,200 340,184 Z", fill=YELLOW, sw=1.4, color=INK))
    o.append(_path("M340,200 C335,209 334,217 338,223 C340,226 342,226 344,223 "
                   "C348,217 345,209 340,200 Z", fill=PAPER, sw=0.9, color=GREY))

    # Oil reservoir below the slanted divider.
    o.append(_line(306, 272, 374, 264, sw=1.4))
    o.append(T(340, 290, "Dầu / Oil", 6.2, color=GREY))

    # Bilingual callouts.
    o.append(T(272, 196, "Ngọn lửa / Flame", 7.6, anchor="end",
               color=INK, weight="600"))
    o.append(T(272, 208, "(nến hoặc dầu/bấc)", 6.2, anchor="end", color=GREY))
    o.append(T(272, 219, "(candle or oil/wick)", 6.0, anchor="end", color=GREY))
    o.append(_arrow(276, 212, 326, 208, sw=1.1, color=GREY))

    o.append(T(412, 178, "Lưới lửa / Gauze flame trap", 7.4, anchor="start",
               color=INK, weight="600"))
    o.append(T(412, 190, "(không cản methane vào, nhưng ngăn", 6.0,
               anchor="start", color=GREY))
    o.append(T(412, 201, "đánh lửa methane/khí ngoài đèn)", 6.0,
               anchor="start", color=GREY))
    o.append(T(412, 213, "(does not prevent methane access but", 5.9,
               anchor="start", color=GREY))
    o.append(T(412, 224, "prevents ignition outside the lamp)", 5.9,
               anchor="start", color=GREY))
    o.append(_arrow(406, 234, 368, 224, sw=1.1, color=GREY))

    o.append(T(250, 316, "Bình dầu / Oil reservoir", 7.4, anchor="end",
               color=INK, weight="600"))
    o.append(_arrow(256, 312, 312, 286, sw=1.1, color=GREY))

    o.append(T(340, 380,
               "Hình 1-2 · Nguyên lý đèn Davy / Figure 1-2 · Principle of Davy Lamp",
               6.5, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Đèn Davy có vòng treo, ngọn lửa, lưới lửa và bình dầu; methane vào được nhưng không đánh lửa bên ngoài")),
                "Hình 1-2 · Nguyên lý đèn Davy: ngọn lửa nằm trong lưới lửa; methane có thể vào "
                "đèn nhưng lưới ngăn không cho đánh lửa hỗn hợp methane/khí bên ngoài",
                "Figure 1-2 · Principle of the Davy lamp: the flame is enclosed by a fine gauze "
                "trap; methane can reach the flame but ignition of the methane/air outside the "
                "lamp is prevented",
                "Đèn Davy có vòng treo ở trên, thân hình trụ, ngọn lửa ở giữa được bao bởi lưới lửa "
                "dạng lưới ô vuông và bình dầu ở dưới, kèm chú thích hai ngôn ngữ",
                "Davy lamp with a hanging loop, a cylindrical body, a central flame surrounded "
                "by a fine square-mesh gauze trap and an oil reservoir below, with bilingual "
                "callouts")


@_reg
def fig_f103():
    """Figure 1-3 - The Distinctive Community Mark (thick Ex hexagon)."""
    w, h = 680, 376
    o = [_defs()]
    o.append(T(340, 18, "Dấu nhận diện Cộng đồng / Distinctive Community Mark", 9.8,
               color=INK, weight="600"))
    o.append(T(340, 34,
               "Chỉ thiết bị được chứng nhận mới được mang dấu này / Only certified equipment may bear the mark",
               6.8, color=GREY))

    cx, cy, R = 340, 200, 120
    dy = R * 0.866
    hexa = [(cx + R, cy), (cx + R / 2.0, cy + dy),
            (cx - R / 2.0, cy + dy), (cx - R, cy),
            (cx - R / 2.0, cy - dy), (cx + R / 2.0, cy - dy)]
    o.append(_poly(hexa, fill="none", sw=10, color=INK, close=True))

    # Stylised Ex: an epsilon-like E with a middle bar, plus a crossed x.
    o.append(_path("M332,150 C285,150 266,172 266,200 C266,228 285,250 332,250",
                   fill="none", sw=13, color=INK))
    o.append(_line(270, 200, 318, 200, sw=13, color=INK))
    o.append(_line(362, 158, 414, 242, sw=12, color=INK))
    o.append(_line(414, 158, 362, 242, sw=12, color=INK))

    o.append(T(340, 340, "Ex = Môi trường nổ / Explosive Atmospheres", 7.4, color=INK))
    o.append(T(340, 356,
               "Hình 1-3 · Dấu Ex / Figure 1-3 · The Ex mark", 6.4, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Hình lục giác đậm chứa ký hiệu Ex cách điệu, tức Dấu nhận diện Cộng đồng")),
                "Hình 1-3 · Dấu nhận diện Cộng đồng: hình lục giác đậm chứa ký hiệu Ex cách điệu, "
                "chỉ được dùng trên thiết bị đã được chứng nhận",
                "Figure 1-3 · The Distinctive Community Mark: a thick hexagon enclosing a "
                "stylised Ex symbol, used only on certified equipment",
                "Hình lục giác viền đậm với ký tự Ex cách điệu màu đen ở giữa và nhãn dấu nhận diện "
                "Cộng đồng bên dưới",
                "A thick-outlined hexagon enclosing a bold stylised Ex symbol, with the "
                "Distinctive Community Mark label below")
