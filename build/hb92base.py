# -*- coding: utf-8 -*-
"""Shared drawing primitives for the Chapter 92 figures (92.1–92.16).

The generic layer — colours, `_lbl`/`_r`/`_line`/`_arr`/`_rect`/`_poly`/`_path`,
`_dot`/`_circ`/`_hatch`, the isometric `_slab` and the `Frame` axis mapper — is
imported from `hb93base` rather than copied, so the two chapters cannot drift
apart. This module adds only what a liquid-crystal chapter needs on top:

  rod()          a rod-shaped LC molecule (rotated ellipse with a highlight)
  rod_field()    a jittered field of rods, for the phase illustrations
  layer_plane()  one smectic layer drawn in isometric
  cell_side()    a cell seen from the side: two plates, gap, electrodes
  isocell()      the isometric sandwich used for the TN and ECB figures
  legend_line()  a short line sample for a figure legend

NOTE: never emit <sub>/<sup> inside <svg> — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Use `_r()`.

NOTE: write the parallel sign as U+2016 (‖), not U+2225 (∥). At the 9.5 px
bold label size the ∥ fallback collapses into a single solid block, while ‖
still renders as two separated bars. Perpendicular U+22A5 (⊥) is fine.
"""
import math
import random

from hbfig import svg, _fig, _f
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, _slab, _isostrip, _isostrip_d, Frame)

INK = "#1f1f1f"
ROD = "#3a3a3a"
RODHI = "#8e8e8e"
GLASSBLUE = "#eef3f8"
POLAR = "#cfd8e3"
ITO = "#dfe8f2"


def rod(x, y, ang=0.0, L=17.0, W=6.0, col=ROD, hi=RODHI, sw=0.9):
    """One rod-shaped molecule, centred on (x, y), rotated by `ang` degrees."""
    rx, ry = W / 2.0, L / 2.0
    return ('<g transform="translate(%s %s) rotate(%s)">'
            '<ellipse rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="none"/>'
            '</g>'
            % (_f(x), _f(y), _f(ang), _f(rx), _f(ry), col, col, sw,
               _f(-rx * 0.30), _f(-ry * 0.22), _f(rx * 0.30), _f(ry * 0.46), hi))


def rod_field(x0, y0, w, h, cols, rows, ang=0.0, jitter_a=0.0, jitter_p=0.0,
              seed=7, L=17.0, W=6.0, col=ROD):
    """A field of rods on a grid, optionally jittered in angle and position."""
    rnd = random.Random(seed)
    out = []
    dx = w / float(cols)
    dy = h / float(rows)
    for r in range(rows):
        for c in range(cols):
            px = x0 + dx * (c + 0.5)
            py = y0 + dy * (r + 0.5)
            a = ang + (rnd.uniform(-jitter_a, jitter_a) if jitter_a else 0.0)
            if jitter_p:
                px += rnd.uniform(-jitter_p, jitter_p) * dx
                py += rnd.uniform(-jitter_p, jitter_p) * dy
            out.append(rod(px, py, a, L, W, col))
    return "".join(out)


def layer_plane(x, y, w, d, dx, dy, fill="#f7f7f7", col="#9a9a9a", sw=0.7):
    """One smectic layer, drawn as an isometric parallelogram."""
    return _poly([(x, y), (x + w, y), (x + w + dx, y - dy), (x + dx, y - dy)],
                 sw, fill, col)


def cell_side(x, y, w, gap, t=7, col=E):
    """Two horizontal plates (a cell seen edge-on), with the gap between them."""
    return (_rect(x, y, w, t, 1.0, GLASSBLUE, col)
            + _rect(x, y + t + gap, w, t, 1.0, GLASSBLUE, col))


def isocell(x, y, w, d, dx, dy, gap, t=6):
    """An isometric sandwich: bottom plate, gap, top plate. Returns (svg, gap-y)."""
    bot = _slab(x, y, w, d, t, dx, dy, GLASSBLUE)
    top = _slab(x, y - gap - t, w, d, t, dx, dy, GLASSBLUE)
    return bot + top


def legend_line(x, y, dash="", col=E, sw=1.6, w=20):
    return _line(x, y, x + w, y, sw, col, dash)


def arrow_light(x1, y1, x2, y2, tag, col="#8a8a8a", sw=1.2):
    """A thin propagation arrow for the light path."""
    return _arr(x1, y1, x2, y2, tag, sw, col, "h")


def sine_wave(x0, y0, w, amp, periods, n=160, col=E, sw=1.2, phase=0.0):
    """A sine trace, used for the optical-field illustrations."""
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        pts.append((x0 + w * t, y0 - amp * math.sin(2 * math.pi * periods * t + phase)))
    return _path(pts, sw, col)
