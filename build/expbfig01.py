# -*- coding: utf-8 -*-
"""Vector redraws of Figures 1-1 and 1-2 in R. STAHL, *Basics of
Explosion Protection* -- "Hazardous Locations" (printed A2).

Figure 1-1 contrasts the Class/Division risk model (yellow Division 2,
red Division 1); Figure 1-2 contrasts the Zone model (yellow Zone 2,
red Zone 1, hatched Zone 0). Both show the rising risk curve against
duration of time gas is present. Drawn as SVG with bilingual VI/EN
labels, never as raster art. Architecture mirrors `cvpfig26.py`.
"""
from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _defs, _fig,
                  _line, _poly, _rect, _txt, svg)

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


def _tick(x, base, en, vi):
    """A short tick plus two-line bilingual label below the axis."""
    o = [_line(x, base, x, base + 4, sw=0.9)]
    o.append(T(x, base + 15, en, 6.6, color=INK))
    o.append(T(x, base + 25, vi, 6.4, color=GREY))
    return "".join(o)


@_reg
def fig_f101():
    """Figure 1-1 -- Class/Division System risk comparison chart."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 18,
               "Hệ phân chia / Division System — Rủi ro theo thời gian khí hiện diện / Risk vs. duration",
               9.4, color=INK, weight="600"))

    base = 278
    # Axes.
    o.append(_arrow(120, base, 606, base, sw=1.1, color=INK))
    o.append(_arrow(120, base, 120, 50, sw=1.1, color=INK))
    o.append(T(126, 46, "Risk / Rủi ro", 7.6, anchor="start", color=GREY))

    # Risk bands: yellow Division 2, red Division 1.
    o.append(_rect(170, 246, 185, 32, fill=YELLOW, sw=1.2))
    o.append(_rect(355, 86, 205, 192, fill=RED, sw=1.2))
    o.append(T(262, 268, "Division 2", 9.0, color=INK, weight="600"))
    o.append(T(458, 186, "Division 1", 11.0, color=PAPER, weight="600"))

    # Rising risk curve.
    curve = [(120, 276), (170, 274), (230, 269), (300, 259), (355, 246),
             (410, 224), (460, 194), (510, 156), (545, 120), (560, 90)]
    o.append(_poly(curve, sw=2.2, color=BLUE))

    # Low-risk / not-classified region and band arrows.
    o.append(T(128, 271, "Not Classified / Không phân loại", 6.6,
               anchor="start", color=GREY))
    o.append(_arrow(352, 238, 205, 238, sw=1.2, color=INK))
    o.append(T(278, 232, "Division 2", 7.4, color=INK))
    o.append(_arrow(556, 78, 420, 78, sw=1.2, color=INK))
    o.append(T(488, 72, "Division 1", 7.4, color=INK))

    # Time scale.
    o.append(_tick(170, base, "1 Hour per Year", "1 giờ / năm"))
    o.append(_tick(355, base, "10 Hours per Year", "10 giờ / năm"))
    o.append(T(590, 326,
               "Duration of time gas is present / Thời gian khí hiện diện",
               7.2, anchor="end", color=GREY))

    # Bilingual caption strip inside the SVG.
    o.append(T(340, 344,
               "Hình 1-1 · Hệ Division / Figure 1-1 · Division System "
               "(Division 2 vàng / yellow, Division 1 đỏ / red)",
               6.4, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Biểu đồ rủi ro hệ Division với khối Division 2 màu vàng, Division 1 màu đỏ và đường rủi ro tăng")),
                "Hình 1-1 · Hệ Class/Division: vùng Division 2 (vàng, nguy cơ thấp hơn) và Division 1 (đỏ), với đường rủi ro tăng dần theo thời gian khí hiện diện",
                "Figure 1-1 · The Class/Division System: the yellow Division 2 band and red Division 1 band, with a rising risk curve plotted against duration of time gas is present",
                "Biểu đồ so sánh rủi ro hệ Division: khối vàng Division 2, khối đỏ Division 1, đường cong rủi ro tăng, mốc 1 giờ và 10 giờ mỗi năm, vùng không phân loại",
                "Division System risk chart with yellow Division 2 block, red Division 1 block, rising risk curve, one- and ten-hours-per-year marks and a not-classified region")


@_reg
def fig_f102():
    """Figure 1-2 -- Zone System risk comparison chart."""
    w, h = 680, 372
    o = [_defs()]
    o.append(T(340, 18,
               "Hệ Zone / Zone System — Rủi ro theo thời gian khí hiện diện / Risk vs. duration",
               9.4, color=INK, weight="600"))

    base = 296
    # Axes.
    o.append(_arrow(120, base, 616, base, sw=1.1, color=INK))
    o.append(_arrow(120, base, 120, 48, sw=1.1, color=INK))
    o.append(T(126, 44, "Risk / Rủi ro", 7.6, anchor="start", color=GREY))

    # Risk bands: yellow Zone 2, red Zone 1, hatched Zone 0.
    o.append(_rect(170, 266, 190, 30, fill=YELLOW, sw=1.2))
    o.append(_rect(360, 110, 180, 186, fill=RED, sw=1.2))
    o.append(_rect(540, 52, 35, 244, fill="url(#h6)", sw=1.2))
    o.append(T(265, 287, "Zone 2", 9.0, color=INK, weight="600"))
    o.append(T(450, 202, "Zone 1", 11.0, color=PAPER, weight="600"))
    o.append(T(557, 172, "Zone 0", 7.2, color=INK, anchor="middle", weight="600"))

    # Rising risk curve.
    curve = [(120, 294), (170, 292), (240, 286), (310, 275), (360, 266),
             (420, 242), (470, 212), (515, 172), (545, 132), (575, 60)]
    o.append(_poly(curve, sw=2.2, color=BLUE))

    # Low-risk region and band arrows.
    o.append(T(128, 289, "Not Classified / Không phân loại", 6.6,
               anchor="start", color=GREY))
    o.append(_arrow(358, 258, 205, 258, sw=1.2, color=INK))
    o.append(T(281, 252, "Zone 2", 7.4, color=INK))
    o.append(_arrow(538, 102, 410, 102, sw=1.2, color=INK))
    o.append(T(474, 96, "Zone 1", 7.4, color=INK))
    o.append(_arrow(557, 40, 557, 52, sw=1.1, color=INK))
    o.append(T(596, 44, "Zone 0", 7.4, color=INK, anchor="end"))

    # Time scale.
    o.append(_tick(170, base, "1 Hour per Year", "1 giờ / năm"))
    o.append(_tick(360, base, "10 Hours per Year", "10 giờ / năm"))
    o.append(_tick(557, base, "1000 Hours per Year", "1000 giờ / năm"))
    o.append(T(600, 346,
               "Duration of time gas is present / Thời gian khí hiện diện",
               7.2, anchor="end", color=GREY))

    # Bilingual caption strip inside the SVG.
    o.append(T(340, 366,
               "Hình 1-2 · Hệ Zone / Figure 1-2 · Zone System "
               "(Zone 2 vàng, Zone 1 đỏ, Zone 0 gạch chéo / hatched)",
               6.4, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Biểu đồ rủi ro hệ Zone với Zone 2 màu vàng, Zone 1 màu đỏ, Zone 0 gạch chéo và đường rủi ro tăng")),
                "Hình 1-2 · Hệ Zone: Zone 2 (vàng), Zone 1 (đỏ) và Zone 0 (gạch chéo), với đường rủi ro tăng dần theo thời gian khí hiện diện",
                "Figure 1-2 · The Zone System: yellow Zone 2, red Zone 1 and hatched Zone 0 bands, with a rising risk curve plotted against duration of time gas is present",
                "Biểu đồ so sánh rủi ro hệ Zone: khối vàng Zone 2, khối đỏ Zone 1, khối Zone 0 gạch chéo, đường cong rủi ro tăng, mốc 1, 10 và 1000 giờ mỗi năm",
                "Zone System risk chart with yellow Zone 2 block, red Zone 1 block, hatched Zone 0 block, rising risk curve and one-, ten- and one-thousand-hours-per-year marks")
