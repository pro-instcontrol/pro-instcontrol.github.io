# -*- coding: utf-8 -*-
"""Figures 92.7–92.12 for Handbook Chapter 92 — Liquid Crystal Displays.

92.7  the four director deformations: equilibrium, splay, twist, bend
92.8  a passive matrix-addressed LCD: plan view and cross-section
92.9  the LCD assembly flowchart
92.10 the twisted nematic effect, off and on, with the transmission curve
92.11 STN midplane tilt against reduced voltage, for five twist angles
92.12 the electrically controlled birefringence cell, off and on

Figures 92.13–92.16 are in `hb92figc.py`.

NOTE: write the parallel sign as U+2016 (‖), not U+2225 (∥) — see hb92base.
"""
import math

from hbfig import svg, _fig, _f
from hb92base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      INK, ROD, RODHI, GLASSBLUE, POLAR, ITO,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, _slab, Frame,
                      rod, rod_field, legend_line, arrow_light, sine_wave)


# ---------------------------------------------------------------- helpers
def _box3d(x, y, w, h, dx=15, dy=9, fill="#fdfdfd", top="#f5f5f5", side="#eaeaea"):
    """A block seen in isometric: front face plus top and right faces."""
    return (_rect(x, y, w, h, 1.1, fill, "", E)
            + _poly([(x, y), (x + w, y), (x + w + dx, y - dy), (x + dx, y - dy)],
                    1.0, top, E)
            + _poly([(x + w, y), (x + w + dx, y - dy), (x + w + dx, y + h - dy),
                     (x + w, y + h)], 1.0, side, E))


def _flat_rod(x, y, phi, L=22.0, W=6.4, col=ROD):
    """A rod lying in a horizontal plane at azimuth `phi` (degrees, 0 = across).

    Seen from the front the rod foreshortens, so a director pointing into the
    page shows up as a circle — which is exactly how a twist reads in a
    two-dimensional drawing.
    """
    a = math.radians(phi)
    rx = abs(L / 2.0 * math.cos(a)) + abs(W / 2.0 * math.sin(a))
    ry = W / 2.0
    if rx < ry:
        rx = ry
    return ('<g transform="translate(%s %s)">'
            '<ellipse rx="%s" ry="%s" fill="%s"/>'
            '<ellipse cx="%s" rx="%s" ry="%s" fill="%s"/></g>'
            % (_f(x), _f(y), _f(rx), _f(ry), col,
               _f(-rx * 0.22), _f(rx * 0.28), _f(ry * 0.42), RODHI))


def _fbox(cx, cy, w, txt, h=23):
    return (_rect(cx - w / 2.0, cy - h / 2.0, w, h, 1.0, "#fff", "", E)
            + _lbl(cx, cy + 3.4, txt, "ts", "middle"))


def _vlabel(x, y, txt, cls="ts"):
    """A vertical label reading bottom-to-top, used on narrow strips."""
    return ('<text class="%s" x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>'
            % (cls, _f(x), _f(y), _f(x), _f(y), txt))


# ================================================================ 92.7
def fig_92_7():
    tag = "927"
    o = [_defs(tag)]
    w, h, dx, dy = 116, 130, 15, 9
    y0 = 34
    cols, rows = 4, 6

    def field(x, angfn, kind="rod"):
        out = []
        for r in range(rows):
            for c in range(cols):
                px = x + 14 + (w - 28) * (c / float(cols - 1))
                py = y0 + 14 + (h - 28) * (r / float(rows - 1))
                if kind == "rod":
                    out.append(rod(px, py, angfn(c, r), 24, 6.6))
                else:
                    out.append(_flat_rod(px, py, angfn(c, r), 24, 6.6))
        return "".join(out)

    panels = [
        (30, lambda c, r: 0.0, "rod", "C\u00e2n b\u1eb1ng (a)"),
        (190, lambda c, r: -46.0 + 92.0 * c / float(cols - 1), "rod", "D\u00e3n (b)"),
        (350, lambda c, r: 90.0 * c / float(cols - 1), "flat", "Xo\u1eafn (c)"),
        (510, lambda c, r: 44.0 * math.sin(math.pi * r / float(rows - 1)), "rod",
         "U\u1ed1n (d)"),
    ]
    for (x, fn, kind, cap) in panels:
        o.append(_box3d(x, y0, w, h, dx, dy))
        o.append(field(x, fn, kind))
        o.append(_lbl(x + w / 2.0, y0 + h + 20, cap, "ts", "middle"))

    return _fig(
        svg(660, 200, "".join(o),
            "B\u1ed1n ki\u1ec3u bi\u1ebfn d\u1ea1ng c\u1ee7a ch\u1ec9 h\u01b0\u1edbng"),
        "H\u00ecnh 92.7 \u00b7 Bi\u1ebfn d\u1ea1ng c\u1ee7a ph\u00e2n t\u1eed tinh th\u1ec3 l\u1ecfng nematic "
        "kh\u1ecfi c\u1ea5u h\u00ecnh c\u00e2n b\u1eb1ng: (a) c\u1ea5u h\u00ecnh c\u00e2n b\u1eb1ng; (b) d\u00e3n "
        "(splay); (c) xo\u1eafn (twist); (d) u\u1ed1n (bend). Ba ki\u1ec3u bi\u1ebfn d\u1ea1ng n\u00e0y "
        "m\u00f4 t\u1ea3 \u0111\u01b0\u1ee3c m\u1ecdi bi\u1ebfn d\u1ea1ng c\u00f3 th\u1ec3 c\u00f3.",
        "Figure 92.7 \u00b7 Deformation of nematic liquid crystal molecules away from the "
        "equilibrium configuration: (a) equilibrium; (b) splay; (c) twist; (d) bend. The "
        "three deformations describe every possible distortion.",
        "B\u1ed1n kh\u1ed1i ph\u00e2n t\u1eed: \u0111\u1ec1u song song, xo\u00e8 qu\u1ea1t, quay trong m\u1eb7t "
        "ph\u1eb3ng ngang v\u00e0 u\u1ed1n cong",
        "Four blocks of molecules: all parallel, fanning out, rotating in the horizontal "
        "plane, and bowing")


# ================================================================ 92.8
def fig_92_8():
    tag = "928"
    o = [_defs(tag)]

    # ---------------- (a) plan view ---------------------------------
    gx, gy, gw, gh = 170, 56, 300, 160
    o.append(_rect(gx, gy, gw, gh, 1.1, "#fcfcfc", "", E))
    o.append(_rect(gx + 18, gy + 18, gw - 36, gh - 36, 0.9, "none", "5 4", S))
    # the seal: a hatched frame just inside the plate edge
    o.append(_hatch(tag + "a", gx + 9, gy + 9, 9, gh - 18, 7))
    o.append(_hatch(tag + "b", gx + gw - 18, gy + 9, 9, gh - 18, 7))
    o.append(_hatch(tag + "c", gx + 18, gy + 9, gw - 36, 9, 7))
    o.append(_hatch(tag + "d", gx + 18, gy + gh - 18, gw - 36, 9, 7))
    # row electrodes: solid bars running across
    for k in range(7):
        o.append(_rect(gx + 22, gy + 26 + k * 18, gw - 44, 4, 0.7, "#dcdcdc", "", S))
    # column electrodes: dashed lines running down, upper part of the cell
    for k in range(9):
        xx = gx + 32 + k * 30
        o.append(_line(xx, gy + 22, xx, gy + 130, 1.1, "#8a8a8a", "4 3"))
    # interconnect region and fill hole
    o.append(_rect(gx + gw + 6, gy + 54, 44, 66, 0.9, "none", "4 3", S))
    o.append(_line(gx + gw, gy + 87, gx + gw + 6, gy + 87, 0.9, S))
    o.append(_circ(gx + 13, gy + 122, 5, E, "#fff", 1.0))

    # labels for (a)
    o.append(_line(gx + 62, gy - 4, gx + 72, gy + 16, 0.8, S))
    o.append(_lbl(gx + 8, gy - 12, "\u0110\u1ebf thu\u1ef7 tinh tr\u00ean", "ts"))
    o.append(_line(gx + 206, gy - 4, gx + 206, gy + 22, 0.8, S))
    o.append(_lbl(gx + 212, gy - 8, "\u0110i\u1ec7n c\u1ef1c c\u1ed9t (d\u1eef li\u1ec7u)", "ts"))
    o.append(_line(gx - 6, gy + 122, gx + 6, gy + 122, 0.8, S))
    o.append(_lbl(gx - 10, gy + 125, "L\u1ed7 n\u1ea1p", "ts", "end"))
    o.append(_line(gx + gw + 6, gy + 88, gx + gw + 2, gy + 88, 0.8, S))
    o.append(_lbl(gx + gw + 54, gy + 84, "V\u00f9ng n\u1ed1i", "ts"))
    o.append(_line(gx + 34, gy + gh + 6, gx + 40, gy + gh - 14, 0.8, S))
    o.append(_lbl(gx + 22, gy + gh + 20, "Keo vi\u1ec1n", "ts"))
    o.append(_line(gx + 214, gy + gh + 6, gx + 196, gy + gh - 30, 0.8, S))
    o.append(_lbl(gx + 208, gy + gh + 20, "\u0110i\u1ec7n c\u1ef1c h\u00e0ng (qu\u00e9t)", "ts"))
    o.append(_lbl(gx + gw / 2.0, gy + gh + 46, "(a)", "ts", "middle"))

    # ---------------- (b) cross-section ------------------------------
    bx, by, bw = 200, 300, 300
    th = [6, 21, 4, 4, 49, 4, 17, 4, 4, 21, 6]
    fill = [POLAR, GLASSBLUE, "#cfcfcf", "#e8e8e8", "#fbfbfb", "#cfcfcf",
            None, "#2a2a2a", "#e8e8e8", GLASSBLUE, POLAR]
    tops, yy = [], by
    for k in range(len(th)):
        tops.append(yy)
        if k == 6:                                  # the colour filters
            seg = bw / 3.0
            for c, cc in enumerate(("#f6cccc", "#cbe7cc", "#ccdcf6")):
                o.append(_rect(bx + c * seg + 2, yy, seg - 4, th[k], 0.7, cc, "", S))
        else:
            o.append(_rect(bx, yy, bw, th[k], 0.9, fill[k], "", S))
        yy += th[k]
    for k in range(7):                              # cell-gap spacers
        o.append(_circ(bx + 26 + k * 42, tops[4] + th[4] / 2.0, 4.5, S, "#fff", 0.9))
    for sx in (bx - 11, bx + bw + 1):               # seal, both ends
        o.append(_hatch(tag + ("e" if sx < bx else "f"), sx, by + 12, 10,
                        yy - by - 15, 6))

    def lead(k, ly, side):
        yc = tops[k] + th[k] / 2.0
        if side == "L":
            o.append(_line(bx - 13, yc, bx - 44, ly, 0.7, S))
            o.append(_lbl(bx - 48, ly + 3.2, LB[k], "ts", "end"))
        else:
            o.append(_line(bx + bw + 13, yc, bx + bw + 44, ly, 0.7, S))
            o.append(_lbl(bx + bw + 48, ly + 3.2, LB[k], "ts"))

    LB = ["Phin ph\u00e2n c\u1ef1c", "\u0110\u1ebf thu\u1ef7 tinh d\u01b0\u1edbi",
          "\u0110i\u1ec7n c\u1ef1c h\u00e0ng", "L\u1edbp \u0111\u1ecbnh h\u01b0\u1edbng",
          "V\u1eadt li\u1ec7u tinh th\u1ec3 l\u1ecfng", "\u0110i\u1ec7n c\u1ef1c c\u1ed9t",
          "K\u00ednh l\u1ecdc m\u00e0u R, G, B", "N\u1ec1n \u0111en",
          "L\u1edbp \u0111\u1ecbnh h\u01b0\u1edbng", "\u0110\u1ebf thu\u1ef7 tinh tr\u00ean",
          "Phin ph\u00e2n c\u1ef1c"]
    for (k, ly, side) in ((0, 4, "R"), (1, 22, "R"), (3, 40, "R"), (4, 62, "R"),
                          (8, 104, "R"), (9, 124, "R"), (10, 141, "R"),
                          (2, 58, "L"), (5, 88, "L"), (6, 110, "L"), (7, 131, "L")):
        lead(k, by + ly, side)

    o.append(_lbl(bx + bw / 2.0, yy + 26, "(b)", "ts", "middle"))

    return _fig(
        svg(660, 480, "".join(o),
            "LCD ma tr\u1eadn th\u1ee5 \u0111\u1ed9ng: m\u1eb7t b\u1eb1ng v\u00e0 m\u1eb7t c\u1eaft"),
        "H\u00ecnh 92.8 \u00b7 (a) M\u1eb7t b\u1eb1ng v\u00e0 (b) m\u1eb7t c\u1eaft c\u1ee7a m\u1ed9t LCD ma tr\u1eadn "
        "th\u1ee5 \u0111\u1ed9ng. \u0110i\u1ec7n c\u1ef1c c\u1ed9t ch\u1ea1y d\u1ecdc, \u0111i\u1ec7n c\u1ef1c h\u00e0ng ch\u1ea1y "
        "ngang; m\u1ed7i giao \u0111i\u1ec3m l\u00e0 m\u1ed9t \u0111i\u1ec3m \u1ea3nh.",
        "Figure 92.8 \u00b7 (a) Plan and (b) cross-sectional view of a passive "
        "matrix-addressed LCD. Column electrodes run one way and row electrodes the "
        "other; each crossing is one pixel.",
        "S\u01a1 \u0111\u1ed3 m\u1eb7t b\u1eb1ng v\u1edbi l\u01b0\u1edbi \u0111i\u1ec7n c\u1ef1c h\u00e0ng c\u1ed9t v\u00e0 s\u01a1 "
        "\u0111\u1ed3 m\u1eb7t c\u1eaft x\u1ebfp l\u1edbp c\u1ee7a m\u1ed9t cell LCD",
        "A plan view with a grid of row and column electrodes, and a layered "
        "cross-section through the cell")


# ================================================================ 92.9
def fig_92_9():
    tag = "929"
    o = [_defs(tag)]
    bw = 168
    xl, xr = 152, 468
    ys = [30, 64, 98, 132]

    left = ["\u0110\u1ebf thu\u1ef7 tinh d\u01b0\u1edbi", "T\u1ea1o h\u00ecnh \u0111i\u1ec7n c\u1ef1c",
            "X\u1eed l\u00fd l\u1edbp \u0111\u1ecbnh h\u01b0\u1edbng", "R\u1ea3i h\u1ea1t \u0111\u1ec7m"]
    right = ["\u0110\u1ebf thu\u1ef7 tinh tr\u00ean", "Ch\u1ebf t\u1ea1o k\u00ednh l\u1ecdc m\u00e0u",
             "T\u1ea1o h\u00ecnh \u0111i\u1ec7n c\u1ef1c", "X\u1eed l\u00fd l\u1edbp \u0111\u1ecbnh h\u01b0\u1edbng"]

    for (x, names) in ((xl, left), (xr, right)):
        for k, nm in enumerate(names):
            o.append(_fbox(x, ys[k], bw, nm))
            if k:
                o.append(_arr(x, ys[k - 1] + 11.5, x, ys[k] - 11.5, tag, 1.0))

    chain = ["D\u00e1n keo vi\u1ec1n cell", "N\u1ea1p v\u1eadt li\u1ec7u tinh th\u1ec3 l\u1ecfng",
             "B\u1ecbt l\u1ed7 n\u1ea1p", "D\u00e1n phin ph\u00e2n c\u1ef1c",
             "N\u1ed1i m\u1ea1ch l\u00e1i", "L\u1eafp r\u00e1p module", "Ki\u1ec3m tra"]
    cx = (xl + xr) / 2.0
    y1 = 170
    # the two columns converge on the first shared box
    o.append(_line(xl, ys[-1] + 11.5, xl, y1 - 22, 1.0))
    o.append(_line(xr, ys[-1] + 11.5, xr, y1 - 22, 1.0))
    o.append(_line(xl, y1 - 22, cx, y1 - 22, 1.0))
    o.append(_line(xr, y1 - 22, cx, y1 - 22, 1.0))
    o.append(_arr(cx, y1 - 22, cx, y1 - 11.5, tag, 1.0))

    for k, nm in enumerate(chain):
        y = y1 + k * 34
        o.append(_fbox(cx, y, bw + 40, nm))
        if k:
            o.append(_arr(cx, y - 34 + 11.5, cx, y - 11.5, tag, 1.0))

    return _fig(
        svg(660, 400, "".join(o),
            "L\u01b0u \u0111\u1ed3 l\u1eafp r\u00e1p LCD"),
        "H\u00ecnh 92.9 \u00b7 L\u01b0u \u0111\u1ed3 l\u1eafp r\u00e1p m\u1ed9t LCD. Hai \u0111\u1ebf \u0111\u01b0\u1ee3c x\u1eed l\u00fd "
        "song song r\u1ed3i gh\u00e9p l\u1ea1i; sau khi d\u00e1n keo vi\u1ec1n, cell \u0111\u01b0\u1ee3c n\u1ea1p tinh "
        "th\u1ec3 l\u1ecfng, b\u1ecbt l\u1ed7 n\u1ea1p, d\u00e1n phin ph\u00e2n c\u1ef1c v\u00e0 l\u1eafp module.",
        "Figure 92.9 \u00b7 LCD assembly flowchart. The two substrates are processed in "
        "parallel and then joined; after the perimeter is sealed the cell is filled with "
        "liquid crystal, plugged, polarised and assembled into a module.",
        "L\u01b0u \u0111\u1ed3 hai nh\u00e1nh x\u1eed l\u00fd \u0111\u1ebf song song r\u1ed3i h\u1ee3p th\u00e0nh m\u1ed9t "
        "chu\u1ed7i b\u01b0\u1edbc duy nh\u1ea5t",
        "A two-branch flowchart of substrate processing that merges into a single chain "
        "of steps")


# ---------------------------------------------------------------- cell helpers
def _pol_axis(cx, cy, ang, tag, L=12.0, col=GOLD):
    """A double-headed arrow showing the transmission axis of a polarizer."""
    a = math.radians(ang)
    dx, dy = L * math.cos(a), L * math.sin(a)
    return (_arr(cx - dx, cy - dy, cx + dx, cy + dy, tag, 0.9, col, "h")
            + _arr(cx + dx, cy + dy, cx - dx, cy - dy, tag, 0.9, col, "h"))


def _lc_cell(x, y, w, gap, tag, mode="tn", tilt=34.0):
    """A liquid crystal cell seen edge-on.

    mode = "tn"    twisted nematic: the in-plane director turns 90 deg down the gap
    mode = "homo"  homeotropic: the director stands perpendicular to the plates
    mode = "tilt"  homeotropic, but tilted by `tilt` once the field is applied
    """
    o = []
    o.append(_rect(x, y, w, 4, 0.9, POLAR, "", S))
    o.append(_rect(x, y + 4, w, 9, 0.9, GLASSBLUE, "", E))
    o.append(_rect(x, y + gap + 13, w, 9, 0.9, GLASSBLUE, "", E))
    o.append(_rect(x, y + gap + 22, w, 4, 0.9, POLAR, "", S))
    y0, y1 = y + 13, y + gap + 13

    rows, cols = 5, 5
    for r in range(rows):
        py = y0 + 8 + (gap - 16) * r / float(rows - 1)
        for c in range(cols):
            px = x + 18 + (w - 36) * c / float(cols - 1)
            if mode == "tn":
                o.append(_flat_rod(px, py, 90.0 * r / float(rows - 1), 24, 7.0))
            elif mode == "homo":
                o.append(rod(px, py, 0, 24, 7.0))
            else:
                o.append(rod(px, py, -tilt, 24, 7.0))
    # the polarizer axes: horizontal on top, vertical below — crossed
    o.append(_pol_axis(x + w + 16, y + 2, 0, tag))
    o.append(_pol_axis(x + w + 16, y + gap + 24, 90, tag))
    return "".join(o), (y0, y1)


# ================================================================ 92.10
def fig_92_10():
    tag = "9210"
    o = [_defs(tag)]
    w, gap = 132, 92
    y = 56

    # ---- (a) off state: the twist guides the light round to the exit polarizer
    xa = 46
    cell, (ya0, ya1) = _lc_cell(xa, y, w, gap, tag, "tn")
    o.append(cell)
    cxa = xa + w / 2.0
    o.append(_arr(cxa, y - 34, cxa, y - 8, tag, 1.2, GOLD, "h"))
    o.append(_arr(cxa, y + gap + 30, cxa, y + gap + 52, tag, 1.2, GOLD, "h"))
    o.append(_lbl(xa + w / 2.0, y + gap + 62, "T\u1eaeT (a)", "ts", "middle"))
    o.append(_lbl(xa + w + 26, y + 4, "0\u00b0", "txs"))
    o.append(_lbl(xa + w + 26, y + gap + 26, "90\u00b0", "txs"))

    # ---- (b) on state: the director stands up and the light is blocked
    xb = 250
    cell, (yb0, yb1) = _lc_cell(xb, y, w, gap, tag, "homo")
    o.append(cell)
    cxb = xb + w / 2.0
    o.append(_arr(cxb, y - 34, cxb, y - 8, tag, 1.2, GOLD, "h"))
    o.append(_line(cxb - 7, yb1 + 12, cxb + 7, yb1 + 26, 1.4, RED))
    o.append(_line(cxb + 7, yb1 + 12, cxb - 7, yb1 + 26, 1.4, RED))
    o.append(_lbl(xb + w / 2.0, y + gap + 62, "B\u1eacT (b)", "ts", "middle"))
    o.append(_lbl(xb + w + 26, y + 4, "0\u00b0", "txs"))
    o.append(_lbl(xb + w + 26, y + gap + 26, "90\u00b0", "txs"))

    # ---- (c) the electro-optic curve
    F = Frame(474, 62, 168, 150, (0, 5), (0, 100))
    o.append(F.frame())
    o.append(F.hgrid([50]))
    o.append(F.vgrid([1, 2, 3, 4]))
    o.append(F.xticks([(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]))
    o.append(F.yticks([(0, "0"), (50, "50"), (100, "100")]))
    o.append(F.xlab("Hi\u1ec7u \u0111i\u1ec7n th\u1ebf (V)", 30))
    o.append(F.ylab("Truy\u1ec1n qua (%)", -40))

    nw, nb = [], []
    v = 0.0
    while v <= 5.0001:
        t = 100.0 / (1.0 + math.exp((v - 2.35) / 0.25))
        nw.append((v, t))
        nb.append((v, 100.0 - t))
        v += 0.05
    o.append(F.curve(nw, 1.7))
    o.append(F.curve(nb, 1.5, E, "5 4"))
    o.append(_lbl(F.X(0.22), F.Y(84), "NW", "txs"))
    o.append(_lbl(F.X(4.05), F.Y(84), "NB", "txs"))
    o.append(_line(F.X(1.9), F.Y(0), F.X(1.9), F.Y(100), 0.8, S, "3 3"))
    o.append(_r(F.X(1.9) + 4, F.Y(94), [("V", False), ("th", True)], "start", "txs"))
    o.append(_lbl(F.x + F.w / 2.0, F.y + F.h + 52, "(c)", "ts", "middle"))

    return _fig(
        svg(660, 244, "".join(o),
            "Hi\u1ec7u \u1ee9ng nematic xo\u1eafn"),
        "H\u00ecnh 92.10 \u00b7 Hi\u1ec7u \u1ee9ng nematic xo\u1eafn (TN). (a) \u1ede tr\u1ea1ng th\u00e1i t\u1eaft, "
        "\u00e1nh s\u00e1ng ph\u00e2n c\u1ef1c l\u1ecdt qua phin v\u00e0o, b\u1ecb l\u1edbp TN quay 90\u00b0 r\u1ed3i l\u1ecdt "
        "qua phin ra \u0111\u1eb7t vu\u00f4ng g\u00f3c. (b) \u1ede tr\u1ea1ng th\u00e1i b\u1eadt, ph\u00e2n t\u1eed d\u1ef1ng "
        "\u0111\u1ee9ng n\u00ean kh\u00f4ng quay m\u1eb7t ph\u1eb3ng ph\u00e2n c\u1ef1c v\u00e0 \u00e1nh s\u00e1ng b\u1ecb ch\u1eb7n. "
        "(c) \u0110\u01b0\u1eddng li\u1ec1n: c\u1ea5u h\u00ecnh NW v\u1edbi phin vu\u00f4ng g\u00f3c; \u0111\u01b0\u1eddng n\u00e9t "
        "\u0111\u1ee9t: c\u1ea5u h\u00ecnh NB v\u1edbi phin song song.",
        "Figure 92.10 \u00b7 The twisted nematic effect. (a) Off state: the incident polarised "
        "light passes the entrance polarizer, is turned through 90\u00b0 by the TN layer and "
        "passes the crossed exit polarizer. (b) On state: the molecules stand up, the "
        "plane of polarisation is no longer rotated and the light is blocked. (c) Solid "
        "line: the NW configuration with crossed polarizers; dashed line: the NB "
        "configuration with parallel polarizers.",
        "Hai s\u01a1 \u0111\u1ed3 cell nematic xo\u1eafn \u1edf tr\u1ea1ng th\u00e1i t\u1eaft v\u00e0 b\u1eadt, k\u00e8m "
        "\u0111\u1ed3 th\u1ecb truy\u1ec1n qua theo hi\u1ec7u \u0111i\u1ec7n th\u1ebf",
        "Two twisted-nematic cells in the off and on states, with a transmission-against-"
        "voltage plot")


# ================================================================ 92.11
def fig_92_11():
    tag = "9211"
    o = [_defs(tag)]
    F = Frame(84, 44, 400, 206, (0, 2.5), (0, 90))
    o.append(F.frame())
    o.append(F.hgrid([30, 60]))
    o.append(F.vgrid([0.5, 1.0, 1.5, 2.0]))
    o.append(F.xticks([(0, "0,0"), (0.5, "0,5"), (1.0, "1,0"), (1.5, "1,5"),
                       (2.0, "2,0"), (2.5, "2,5")]))
    o.append(F.yticks([(0, "0"), (30, "30"), (60, "60"), (90, "90")]))
    o.append(F.xlab("Hi\u1ec7u \u0111i\u1ec7n th\u1ebf r\u00fat g\u1ecdn V/V\u209c\u2095", 32))
    o.append(F.ylab("G\u00f3c nghi\u00eang \u1edf m\u1eb7t gi\u1eefa (deg)", -52))

    # five twist angles; a larger twist gives a steeper curve. The curves
    # are numbered and keyed in the right margin so no label sits on a curve.
    specs = [(180, 1.62, 0.40), (210, 1.40, 0.34), (240, 1.18, 0.28),
             (255, 1.06, 0.24), (270, 0.94, 0.20)]
    for (phi, v0, w) in specs:
        pts, v = [], 0.0
        while v <= 2.5001:
            pts.append((v, 90.0 / (1.0 + math.exp(-(v - v0) / w))))
            v += 0.02
        o.append(F.curve(pts, 1.4))

    # a numbered badge on each curve at the 60-degree level
    for i, (phi, v0, w) in enumerate(specs, 1):
        v60 = v0 + w * math.log(2.0)
        bx, by = F.X(v60), F.Y(60)
        o.append(_circ(bx, by, 7.0, E, "#fff", 1.0))
        o.append(_lbl(bx, by + 3.4, str(i), "txs", "middle"))

    # the key
    o.append(_lbl(512, 62, "G\u00f3c xo\u1eafn \u03a6", "tb"))
    for i, (phi, v0, w) in enumerate(specs, 1):
        yy = 88 + (i - 1) * 21
        o.append(_lbl(512, yy, "%d" % i, "txs"))
        o.append(_line(524, yy - 3, 540, yy - 3, 1.4, E))
        o.append(_lbl(546, yy, "\u03a6 = %d\u00b0" % phi, "ts"))

    return _fig(
        svg(660, 300, "".join(o),
            "G\u00f3c nghi\u00eang c\u1ee7a ch\u1ec9 h\u01b0\u1edbng gi\u1eefa l\u1edbp STN"),
        "H\u00ecnh 92.11 \u00b7 C\u00e1c \u0111\u01b0\u1eddng t\u00ednh to\u00e1n c\u1ee7a g\u00f3c nghi\u00eang ch\u1ec9 h\u01b0\u1edbng "
        "\u1edf m\u1eb7t gi\u1eefa m\u1ed9t l\u1edbp STN theo hi\u1ec7u \u0111i\u1ec7n th\u1ebf r\u00fat g\u1ecdn V/V<sub>th</sub>, "
        "v\u1edbi V<sub>th</sub> l\u00e0 ng\u01b0\u1ee1ng Freedericksz c\u1ee7a m\u1ed9t l\u1edbp kh\u00f4ng xo\u1eafn v\u00e0 "
        "kh\u00f4ng nghi\u00eang s\u1eb5n. \u0110\u1ed9 d\u1ed1c c\u1ee7a \u0111\u01b0\u1eddng cong t\u0103ng theo g\u00f3c xo\u1eafn \u03a6; "
        "t\u00ednh l\u01b0\u1ee1ng \u1ed5n \u0111\u1ea1t \u0111\u01b0\u1ee3c khi \u03a6 &gt; 240\u00b0.",
        "Figure 92.11 \u00b7 Calculated tilt angle of the local directors in the midplane of an "
        "STN cell against the reduced voltage V/V<sub>th</sub>, where V<sub>th</sub> is the "
        "Freedericksz threshold of an untwisted layer with no pretilt. The curves steepen "
        "as the twist angle \u03a6 rises, and bistability is reached for \u03a6 &gt; 240\u00b0.",
        "N\u0103m \u0111\u01b0\u1eddng cong g\u00f3c nghi\u00eang t\u0103ng t\u1eeb 0 l\u00ean g\u1ea7n 90 \u0111\u1ed9, d\u1ed1c d\u1ea7n "
        "khi g\u00f3c xo\u1eafn t\u0103ng",
        "Five tilt-angle curves rising from zero to nearly 90 degrees, steeper as the "
        "twist angle increases")


# ================================================================ 92.12
def fig_92_12():
    tag = "9212"
    o = [_defs(tag)]
    w, gap = 132, 92
    y = 56

    # ---- (a) off: homeotropic, no birefringence, the crossed polarizer blocks
    xa = 46
    cell, (ya0, ya1) = _lc_cell(xa, y, w, gap, tag, "homo")
    o.append(cell)
    cxa = xa + w / 2.0
    o.append(_arr(cxa, y - 34, cxa, y - 8, tag, 1.2, GOLD, "h"))
    o.append(_line(cxa - 7, ya1 + 12, cxa + 7, ya1 + 26, 1.4, RED))
    o.append(_line(cxa + 7, ya1 + 12, cxa - 7, ya1 + 26, 1.4, RED))
    o.append(_lbl(xa + w / 2.0, y + gap + 62, "T\u1eaeT (a)", "ts", "middle"))
    o.append(_lbl(xa + w + 26, y + 4, "0\u00b0", "txs"))
    o.append(_lbl(xa + w + 26, y + gap + 26, "90\u00b0", "txs"))

    # ---- (b) on: the director tilts, the light becomes elliptical and leaks out
    xb = 250
    cell, (yb0, yb1) = _lc_cell(xb, y, w, gap, tag, "tilt", 34.0)
    o.append(cell)
    cxb = xb + w / 2.0
    o.append(_arr(cxb, y - 34, cxb, y - 8, tag, 1.2, GOLD, "h"))
    o.append(_arr(cxb, y + gap + 30, cxb, y + gap + 52, tag, 1.2, GOLD, "h"))
    # the tilt angle, marked on the left of the gap
    o.append(_line(xb + 12, yb1 - 6, xb + 44, yb1 - 6, 0.8, S, "3 3"))
    o.append(_line(xb + 12, yb1 - 6, xb + 12, yb1 - 40, 0.8, S, "3 3"))
    o.append(_lbl(xb + 16, yb1 - 42, "\u03b8", "txs"))
    o.append(_lbl(xb + w / 2.0, y + gap + 62, "B\u1eacT (b)", "ts", "middle"))
    o.append(_lbl(xb + w + 26, y + 4, "0\u00b0", "txs"))
    o.append(_lbl(xb + w + 26, y + gap + 26, "90\u00b0", "txs"))

    return _fig(
        svg(660, 244, "".join(o),
            "Cell l\u01b0\u1ee1ng chi\u1ebft \u0111i\u1ec1u khi\u1ec3n b\u1eb1ng \u0111i\u1ec7n"),
        "H\u00ecnh 92.12 \u00b7 Cell l\u01b0\u1ee1ng chi\u1ebft \u0111i\u1ec1u khi\u1ec3n b\u1eb1ng \u0111i\u1ec7n (ECB). "
        "(a) \u0110\u1ecbnh h\u01b0\u1edbng \u0111\u1ee9ng v\u1edbi phin ph\u00e2n c\u1ef1c vu\u00f4ng g\u00f3c: \u1edf tr\u1ea1ng th\u00e1i "
        "t\u1eaft cell kh\u00f4ng g\u00e2y l\u01b0\u1ee1ng chi\u1ebft n\u00ean m\u00e0n h\u00ecnh \u0111en. (b) \u1ede tr\u1ea1ng th\u00e1i "
        "b\u1eadt, tr\u1ee5c ph\u00e2n t\u1eed nghi\u00eang g\u00f3c \u03b8 n\u00ean \u00e1nh s\u00e1ng l\u00f3 ra kh\u1ecfi l\u1edbp "
        "tr\u1edf th\u00e0nh ph\u00e2n c\u1ef1c elip v\u00e0 m\u1ed9t ph\u1ea7n l\u1ecdt qua phin vu\u00f4ng g\u00f3c.",
        "Figure 92.12 \u00b7 An electrically controlled birefringence cell. (a) With "
        "homeotropic alignment and crossed polarizers the off state is black. (b) In the "
        "on state the molecular axis is inclined at \u03b8, so the light leaving the layer is "
        "elliptically polarised and part of it passes the crossed polarizer.",
        "Hai s\u01a1 \u0111\u1ed3 cell ECB: m\u1ed9t \u0111\u1ee9ng ho\u00e0n to\u00e0n cho m\u00e0n h\u00ecnh \u0111en, m\u1ed9t "
        "nghi\u00eang g\u00f3c theta cho \u00e1nh s\u00e1ng l\u1ecdt qua",
        "Two ECB cells: one perfectly homeotropic showing black, one tilted through theta "
        "letting light through")
