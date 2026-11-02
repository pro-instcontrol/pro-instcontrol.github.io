# -*- coding: utf-8 -*-
"""Figures 92.1–92.6 for Handbook Chapter 92 — Liquid Crystal Displays.

92.1 the three phases (solid, liquid crystal, liquid)
92.2 molecular order in smectic A, smectic C, nematic and cholesteric phases
92.3 order parameter against temperature for PAA
92.4 dielectric constants against temperature for a cyanobiphenyl
92.5 the index ellipsoid of a uniaxial liquid crystal
92.6 refractive indices against temperature and against wavelength

Figures 92.7–92.12 are in `hb92figb.py`, 92.13–92.16 in `hb92figc.py`.
"""
import math

from hbfig import svg, _fig, _f
from hb92base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      INK, ROD, RODHI, GLASSBLUE, POLAR, ITO,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, _slab, _isostrip, Frame,
                      rod, rod_field, layer_plane, legend_line, sine_wave)


# ================================================================ 92.1
def fig_92_1():
    tag = "921"
    o = [_defs(tag)]
    import random as _rnd

    panels = [(40, [("T < T", False), ("m", True)], "Rắn", 0.0, 0.0, False),
              (250, [("T", False), ("m", True), (" < T < T", False), ("c", True)],
               "Tinh thể lỏng", 11.0, 0.22, False),
              (460, [("T > T", False), ("c", True)], "Chất lỏng", 0.0, 0.0, True)]
    for (x, parts, name, ja, jp, random_all) in panels:
        o.append(_r(x + 80, 26, parts, "middle", "ts"))
        if random_all:
            rnd = _rnd.Random(5)
            body = []
            for r in range(7):
                for c in range(6):
                    px = x + 160 / 6.0 * (c + 0.5) + rnd.uniform(-7, 7)
                    py = 44 + 150 / 7.0 * (r + 0.5) + rnd.uniform(-4, 4)
                    body.append(rod(px, py, rnd.uniform(0, 180), 21, 7.4))
            o.append("".join(body))
        else:
            o.append(rod_field(x, 44, 160, 150, 6, 7, 0.0, ja, jp, seed=3 if not ja else 11,
                               L=21, W=7.4))
        o.append(_lbl(x + 80, 212, name, "tm", "middle"))

    return _fig(
        svg(660, 226, "".join(o),
            "Ba pha: chất rắn, tinh thể lỏng và chất lỏng"),
        "Hình 92.1 · Chất rắn, tinh thể lỏng và chất lỏng. Chất rắn có cả trật tự định hướng lẫn "
        "trật tự vị trí; tinh thể lỏng chỉ có trật tự định hướng; pha lỏng đẳng hướng, không có "
        "trật tự nào.",
        "Figure 92.1 · A solid, a liquid crystal and a liquid. A solid has orientational as well "
        "as positional order; a liquid crystal has orientational order only; a liquid is isotropic "
        "with neither.",
        "Ba khối phân tử que: mạng tinh thể đều, các phân tử song song nhưng lệch vị trí, và các "
        "phân tử định hướng ngẫu nhiên",
        "Three blocks of rod molecules: a regular lattice, parallel rods with positional disorder, "
        "and randomly oriented rods")


# ================================================================ 92.2
def fig_92_2():
    tag = "922"
    o = [_defs(tag)]
    pw = 146
    xs = [16, 176, 336, 496]
    dx, dy = 24, 12

    def sheet(x, y, w=None, fill="#fbfbfb"):
        w = pw if w is None else w
        return _poly([(x, y), (x + w - 28, y), (x + w - 28 + dx, y - dy),
                      (x + dx, y - dy)], 0.8, fill, "#9a9a9a")

    def flat_rod(x, y, ang, L=18, W=7.2, col=ROD):
        """A rod lying in the plane of a layer: an ellipse squashed by the isometric view."""
        return ('<g transform="translate(%s %s) rotate(%s) scale(1 0.46)">'
                '<ellipse rx="%s" ry="%s" fill="%s"/></g>'
                % (_f(x), _f(y), _f(ang), _f(L / 2.0), _f(W / 2.0), col))

    # ---- (a) smectic A: upright rods standing between the sheets
    x = xs[0]
    for k in range(4):
        ly = 196 - k * 42
        o.append(sheet(x, ly))
        for c in range(4):
            o.append(rod(x + 26 + c * 26, ly - 21, 0, 34, 7.4))
    o.append(_lbl(x + pw / 2.0, 228, "Smectic A (a)", "ts", "middle"))

    # ---- (b) smectic C: the same sheets, rods tilted
    x = xs[1]
    for k in range(4):
        ly = 196 - k * 42
        o.append(sheet(x, ly))
        for c in range(4):
            o.append(rod(x + 28 + c * 26, ly - 20, 30, 34, 7.4))
    o.append(_lbl(x + pw / 2.0, 228, "Smectic C (b)", "ts", "middle"))

    # ---- (c) nematic: no sheets at all
    x = xs[2]
    o.append(rod_field(x + 4, 44, pw - 24, 156, 5, 6, 0.0, 6.0, 0.18, seed=23, L=32, W=7.6))
    o.append(_lbl(x + pw / 2.0, 228, "Nematic (c)", "ts", "middle"))

    # ---- (d) cholesteric: in-plane rods whose direction turns sheet by sheet
    x = xs[3]
    sx = x + 26                      # leave room on the left for the helix axis
    for k in range(5):
        ly = 200 - k * 34
        o.append(sheet(sx, ly, 118))
        for c in range(4):
            o.append(flat_rod(sx + 16 + c * 27, ly - 6, 12 + k * 34))
    hx = x + 8
    o.append(_arr(hx, 202, hx, 46, tag, 1.0, "#7a7a7a", "a"))
    o.append(_lbl(hx + 13, 48, "tr\u1ee5c xo\u1eafn", "ts"))
    o.append(_lbl(x + pw / 2.0, 228, "Cholesteric (d)", "ts", "middle"))

    return _fig(
        svg(660, 242, "".join(o),
            "Định hướng phân tử trong các pha tinh thể lỏng"),
        "Hình 92.2 · Định hướng phân tử trong các pha tinh thể lỏng: (a) smectic A — phân tử xếp "
        "thành lớp, trục phân tử vuông góc với mặt lớp; (b) smectic C — trục nghiêng so với pháp "
        "tuyến của lớp; (c) nematic — không có lớp, các phân tử song song nhưng trượt tự do; "
        "(d) cholesteric — phân tử nằm trong mặt lớp và hướng quay dần theo chiều dày, tạo cấu "
        "trúc xoắn ốc.",
        "Figure 92.2 · Molecular orientation in the liquid crystal phases: (a) smectic A, with the "
        "molecules in layers and the axis normal to the layer; (b) smectic C, with the axis tilted "
        "from the layer normal; (c) nematic, with no layers and the molecules free to slide along "
        "their axis; (d) cholesteric, with the molecules lying in the layer and their direction "
        "rotating from layer to layer.",
        "Bốn khối phân tử: hai pha smectic xếp lớp với trục đứng và trục nghiêng, pha nematic "
        "không lớp, pha cholesteric có hướng quay dần theo chiều dày",
        "Four blocks of rod molecules: two layered smectic phases with upright and tilted axes, a "
        "layerless nematic phase, and a cholesteric phase whose direction rotates through the "
        "thickness")


# ================================================================ 92.3
def fig_92_3():
    tag = "923"
    o = [_defs(tag)]
    F = Frame(90, 40, 350, 190, (-40, 0), (0.25, 0.75))
    o.append(F.frame())
    o.append(F.hgrid([0.3, 0.4, 0.5, 0.6, 0.7]))
    o.append(F.vgrid([-40, -30, -20, -10]))
    o.append(F.xticks([(-40, "\u221240"), (-30, "\u221230"), (-20, "\u221220"),
                       (-10, "\u221210"), (0, "0")]))
    o.append(F.yticks([(0.3, "0,3"), (0.4, "0,4"), (0.5, "0,5"), (0.6, "0,6"), (0.7, "0,7")]))
    o.append(_r(F.x + F.w / 2.0, F.y + F.h + 34,
                [("Nhiệt độ T \u2212 T", False), ("c", True), (" (\u00b0C)", False)],
                "middle", "ts"))
    o.append(F.ylab("Tham số trật tự, S", -52))

    # S = 0.70 - 0.37 exp(-(u/9)^1.3),  u = Tc - T = -x
    pts = []
    xv = -40.0
    while xv <= 0.0001:
        u = -xv
        s = 0.70 - 0.37 * math.exp(-((u / 9.0) ** 1.3))
        pts.append((xv, s))
        xv += 0.4
    o.append(F.curve(pts, 1.7))
    # the clearing point
    o.append(_line(F.X(0), F.y, F.X(0), F.y + F.h, 0.9, S, "4 3"))
    o.append(_r(F.X(0) - 4, F.y + 12, [("T", False), ("c", True)], "end", "ts"))

    return _fig(
        svg(560, 300, "".join(o),
            "Tham số trật tự theo nhiệt độ của tinh thể lỏng PAA"),
        "Hình 92.3 · Sự phụ thuộc nhiệt độ của tham số trật tự S của tinh thể lỏng nematic "
        "p-azoxyanisol (PAA) [10]. S giảm khi nhiệt độ tăng và tiến nhanh về 0 gần điểm trong "
        "T<sub>c</sub>.",
        "Figure 92.3 · Temperature dependence of the order parameter S of the nematic liquid "
        "crystal p-azoxyanisole (PAA) [10]. S falls as the temperature rises and approaches zero "
        "near the clearing point.",
        "Đường cong tham số trật tự giảm từ 0,7 xuống khoảng 0,33 khi tiến tới điểm trong",
        "A curve of the order parameter falling from 0.7 to about 0.33 as the clearing point is "
        "approached")


# ================================================================ 92.4
def fig_92_4():
    tag = "924"
    o = [_defs(tag)]
    F = Frame(90, 40, 360, 190, (25, 58), (5, 17))
    o.append(F.frame())
    o.append(F.hgrid([5, 10, 15]))
    o.append(F.vgrid([30, 40, 50]))
    o.append(F.xticks([(30, "30"), (40, "40"), (50, "50")]))
    o.append(F.yticks([(5, "5"), (10, "10"), (15, "15")]))
    o.append(F.xlab("Nhiệt độ (\u00b0C)", 34))
    o.append(F.ylab("Hằng số điện môi", -56))

    par = [(28.0, 16.40), (32.0, 16.30), (36.0, 16.05), (39.0, 15.80), (41.0, 15.55),
           (42.6, 15.20)]
    perp = [(28.0, 6.00), (33.0, 6.10), (37.0, 6.40), (40.0, 6.85), (42.0, 7.45)]
    above = [(44.0, 10.0), (48.0, 10.10), (53.0, 10.20), (57.0, 10.25)]

    o.append(F.curve(par, 1.6))
    o.append(F.curve(perp, 1.6))
    o.append(F.curve(above, 1.6))
    # the discontinuous jump at the clearing point
    o.append(_line(F.X(42.8), F.Y(15.0), F.X(42.8), F.Y(10.0), 1.2, E, "3 3"))
    for (vx, vy) in par + perp + above:
        o.append(_circ(F.X(vx), F.Y(vy), 2.6, E, "#fff", 1.0))

    # curve labels sit clear of the data, in the empty band right of the jump
    o.append(_line(F.X(43.6), F.Y(15.20), F.X(42.75), F.Y(15.20), 0.8, S))
    o.append(_r(F.X(44.2), F.Y(15.20) + 3.4, [("\u03b5", False), ("\u2016", False)],
                "start", "tb"))
    o.append(_line(F.X(43.6), F.Y(7.45), F.X(42.15), F.Y(7.45), 0.8, S))
    o.append(_r(F.X(44.2), F.Y(7.45) + 3.4, [("\u03b5", False), ("\u22a5", False)],
                "start", "tb"))

    return _fig(
        svg(560, 300, "".join(o),
            "Hằng số điện môi theo nhiệt độ của cyanobiphenyl"),
        "Hình 92.4 · Sự phụ thuộc nhiệt độ của hằng số điện môi của tinh thể lỏng nematic "
        "cyanobiphenyl ở tần số 100 kHz [13], một vật liệu có dị hướng điện môi dương "
        "(ε<sub>∥</sub> &gt; ε<sub>⊥</sub>). ε<sub>∥</sub> giảm còn ε<sub>⊥</sub> tăng theo nhiệt "
        "độ cho tới khi hai giá trị bằng nhau tại điểm trong.",
        "Figure 92.4 · Temperature dependence of the dielectric constants of the nematic liquid "
        "crystal cyanobiphenyl at 100 kHz [13], a material with positive dielectric anisotropy. "
        "The parallel constant falls and the perpendicular one rises until they meet at the "
        "clearing point.",
        "Hai đường hằng số điện môi: đường song song giảm, đường vuông góc tăng, gặp nhau tại "
        "điểm trong",
        "Two dielectric-constant curves, the parallel one falling and the perpendicular one "
        "rising, meeting at the clearing point")


# ================================================================ 92.5
def fig_92_5():
    tag = "925"
    o = [_defs(tag)]
    cx, cy = 250, 152
    rx, ry = 56, 104

    # the ordinary-wave section (dashed circle) and the extraordinary section
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="#5f5f5f" '
             'stroke-width="1.3" stroke-dasharray="5 3.5"/>'
             % (_f(cx), _f(cy), _f(rx), _f(rx)))
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#fbfbfb" stroke="%s" '
             'stroke-width="1.5"/>' % (_f(cx), _f(cy), _f(rx), _f(ry), E))

    # director axis
    o.append(_arr(cx, cy + ry + 24, cx, cy - ry - 24, tag, 1.2, E, "a"))
    o.append(_lbl(cx + 12, cy - ry - 20, "Director n", "tb"))
    o.append(_lbl(cx + 12, cy + ry + 27, "Optic axis", "tb"))

    # the two principal radii, each with an end tick
    o.append(_line(cx, cy, cx, cy - ry, 1.2, GOLD))
    o.append(_line(cx, cy, cx + rx, cy, 1.2, GOLD))
    o.append(_line(cx - 6, cy - ry, cx + 6, cy - ry, 1.2, GOLD))
    o.append(_line(cx + rx, cy - 6, cx + rx, cy + 6, 1.2, GOLD))
    o.append(_dot(cx, cy, 2.4, E))

    o.append(_r(cx + 24, cy - ry + 2.0, [("n", False), ("e", True), (" = n", False),
                                         ("\u2016", False)], "start", "tb"))
    o.append(_r(cx + rx + 10, cy + 3.6, [("n", False), ("o", True), (" = n", False),
                                         ("\u22a5", False)], "start", "tb"))

    return _fig(
        svg(560, 300, "".join(o),
            "Ellipsoid chiết suất của tinh thể lỏng đơn trục"),
        "Hình 92.5 · Dị hướng chiết suất của tinh thể lỏng đơn trục. Chiết suất thường n<sub>o</sub> "
        "ứng với vectơ điện trường vuông góc với trục quang (vòng tròn nét đứt), chiết suất dị "
        "thường n<sub>e</sub> ứng với vectơ điện trường song song với trục quang.",
        "Figure 92.5 · Refractive index anisotropy of a uniaxial liquid crystal. The ordinary index "
        "belongs to light whose electric vector oscillates perpendicular to the optic axis (the "
        "dashed circle), the extraordinary index to light oscillating parallel to it.",
        "Ellipsoid chiết suất với trục dọc theo director và hai bán kính n_e, n_o",
        "An index ellipsoid with its long axis along the director and the two radii n_e and n_o")


# ================================================================ 92.6
def fig_92_6():
    tag = "926"
    o = [_defs(tag)]

    # ---------------- (a) against temperature, axis runs 30 -> 0
    Fa = Frame(74, 40, 224, 180, (32, -2), (1.5, 1.85))
    o.append(Fa.frame())
    o.append(Fa.hgrid([1.5, 1.6, 1.7, 1.8]))
    o.append(Fa.vgrid([30, 20, 10, 0]))
    o.append(Fa.xticks([(30, "30"), (20, "20"), (10, "10"), (0, "0")]))
    o.append(Fa.yticks([(1.5, "1,5"), (1.6, "1,6"), (1.7, "1,7"), (1.8, "1,8")]))
    o.append(_r(Fa.x + Fa.w / 2.0, Fa.y + Fa.h + 34,
                [("Nhi\u1ec7t \u0111\u1ed9 T", False), ("c", True),
                 (" \u2212 T (\u00b0C)", False)], "middle", "ts"))
    o.append(Fa.ylab("Chiết suất", -50))

    npar = [(30, 1.780), (26, 1.772), (22, 1.766), (18, 1.766), (14, 1.772), (10, 1.782),
            (7, 1.793), (4, 1.800), (2, 1.770), (1, 1.700), (0.2, 1.650)]
    nper = [(30, 1.560), (26, 1.556), (22, 1.554), (18, 1.554), (14, 1.557), (10, 1.564),
            (7, 1.575), (4, 1.590), (2, 1.612), (1, 1.628), (0.2, 1.636)]
    o.append(Fa.curve(npar, 1.5))
    o.append(Fa.curve(nper, 1.5))
    for (vx, vy) in npar + nper:
        o.append(_circ(Fa.X(vx), Fa.Y(vy), 2.1, E, "#fff", 0.9))
    o.append(_line(Fa.X(0.2), Fa.y, Fa.X(0.2), Fa.y + Fa.h, 0.9, S, "4 3"))
    o.append(_lbl(Fa.X(26), Fa.Y(1.812), "n\u2016", "tb", "middle"))
    o.append(_lbl(Fa.X(26), Fa.Y(1.528), "n\u22a5", "tb", "middle"))
    o.append(_lbl(Fa.x, 30, "(a)", "ts"))

    # ---------------- (b) against wavelength, Cauchy law
    Fb = Frame(392, 40, 190, 180, (380, 720), (1.35, 1.85))
    o.append(Fb.frame())
    o.append(Fb.hgrid([1.4, 1.5, 1.6, 1.7, 1.8]))
    o.append(Fb.vgrid([400, 500, 600, 700]))
    o.append(Fb.xticks([(400, "400"), (500, "500"), (600, "600"), (700, "700")]))
    o.append(Fb.yticks([(1.4, "1,4"), (1.5, "1,5"), (1.6, "1,6"), (1.7, "1,7"), (1.8, "1,8")]))
    o.append(Fb.xlab("B\u01b0\u1edbc s\u00f3ng (nm)", 32))
    o.append(Fb.ylab("Chiết suất", -50))

    def cauchy(ninf, alpha, lam):
        return ninf + alpha / (lam * lam)

    for ninf, alpha, lab in ((1.419, 64150.0, "n\u2016"), (1.386, 21383.0, "n\u22a5")):
        pts = []
        lam = 390.0
        while lam <= 710:
            pts.append((lam, cauchy(ninf, alpha, lam)))
            lam += 5
        o.append(Fb.curve(pts, 1.5))
        for l0 in (400, 450, 500, 550, 600, 650, 700):
            o.append(_circ(Fb.X(l0), Fb.Y(cauchy(ninf, alpha, l0)), 2.1, E, "#fff", 0.9))
    o.append(_line(Fb.X(610), Fb.Y(1.745), Fb.X(610), Fb.Y(1.598), 0.8, S))
    o.append(_r(Fb.X(610), Fb.Y(1.775), [("n", False), ("\u2016", False)], "middle", "tb"))
    o.append(_line(Fb.X(610), Fb.Y(1.412), Fb.X(610), Fb.Y(1.443), 0.8, S))
    o.append(_r(Fb.X(610), Fb.Y(1.395), [("n", False), ("\u22a5", False)], "middle", "tb"))
    o.append(_lbl(Fb.x, 30, "(b)", "ts"))

    return _fig(
        svg(660, 272, "".join(o),
            "Chiết suất của tinh thể lỏng theo nhiệt độ và theo bước sóng"),
        "Hình 92.6 · (a) Sự phụ thuộc nhiệt độ của chiết suất n<sub>∥</sub> và n<sub>⊥</sub> của "
        "tinh thể lỏng nematic MBBA ở λ = 546 nm; (b) sự phụ thuộc bước sóng của chiết suất "
        "nematic 4-butoxyphenyl ester của axit 4′-hexyloxybenzoic ở 80 °C.",
        "Figure 92.6 · (a) Temperature dependence of n<sub>∥</sub> and n<sub>⊥</sub> for the nematic "
        "MBBA at 546 nm; (b) wavelength dependence of the refractive indices of the nematic "
        "4-butoxyphenyl ester of 4′-hexyloxybenzoic acid at 80 °C.",
        "Hai đồ thị chiết suất: theo nhiệt độ với hai nhánh hội tụ tại điểm trong, và theo bước "
        "sóng giảm dần từ tím sang đỏ",
        "Two refractive-index plots: against temperature with two branches converging at the "
        "clearing point, and against wavelength falling from blue to red")
