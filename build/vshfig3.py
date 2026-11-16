# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 5 — Manual Valves I (source ch. 3,
Figures 3-1 … 3-24).  Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.

Manufacturer cutaways (Figures 3-2 … 3-14, 3-17 … 3-24) are redrawn as
simplified vector cross-sections that keep the topology and the variant
features named in the original caption; a numbered legend carries the
feature names (vi / en).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _axes, _box, _circle, _defs, _f as fmt,
                  _fig, _hatch, _line, _path, _poly, _rect, _txt, svg)


# ------------------------------------------------------------ op plumbing
def _rot_pts(pts, deg, cx=0.0, cy=0.0):
    """Rotate point list by deg (y-down screen coords) about (cx, cy)."""
    a = math.radians(deg)
    ca, sa = math.cos(a), math.sin(a)
    out = []
    for x, y in pts:
        dx, dy = x - cx, y - cy
        out.append((cx + dx * ca - dy * sa, cy + dx * sa + dy * ca))
    return out


def _emit(o, ops, rot=0.0, cx=0.0, cy=0.0, dx=0.0, dy=0.0):
    """Render local-frame ops into primitive list o, optionally rotated and
    translated onto the canvas."""
    for op in ops:
        k = op[0]
        if k == "poly":
            _, pts, fill, sw, color, dash, close = op
            pts = _rot_pts(pts, rot, cx, cy) if rot else pts
            if dx or dy:
                pts = [(x + dx, y + dy) for x, y in pts]
            o.append(_poly(pts, fill=fill, sw=sw, color=color, dash=dash,
                           close=close))
        elif k == "line":
            _, x1, y1, x2, y2, sw, color, dash = op
            if rot:
                (x1, y1), (x2, y2) = _rot_pts([(x1, y1), (x2, y2)], rot, cx, cy)
            o.append(_line(x1 + dx, y1 + dy, x2 + dx, y2 + dy, sw,
                           dash=dash, color=color))
        elif k == "circ":
            _, cxx, cyy, r, sw, color, fill = op
            if rot:
                (cxx, cyy), = _rot_pts([(cxx, cyy)], rot, cx, cy)
            o.append(_circle(cxx + dx, cyy + dy, r, sw=sw, color=color))
            if fill:
                o.append(_circle(cxx + dx, cyy + dy, r, sw=0, color=fill))
        elif k == "dot":                     # numbered feature marker
            _, cxx, cyy, n = op
            if rot:
                (cxx, cyy), = _rot_pts([(cxx, cyy)], rot, cx, cy)
            o.append(_circle(cxx + dx, cyy + dy, 7.5, sw=1.2, color=INK))
            o.append(_txt(cxx + dx, cyy + dy - 0.5, str(n), 8.0,
                          weight="bold"))


def _ell(cx, cy, rx, ry, n=18, rot=0.0):
    """Ellipse point list (for handwheels), optional rotation."""
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        pts.append((cx + rx * math.cos(t), cy + ry * math.sin(t)))
    return _rot_pts(pts, rot) if rot else pts


# ------------------------------------------------- globe/piston section ops
BULB_F = "#f5f5f1"
RING_F = "#e2e2dc"
DISC_F = "#d9d9d2"
PACK_F = "url(#h6)"


def _globe_ops(pattern="standard", bonnet="bolted", screw="external",
               seal="packing", disc="plug", special=None, flow=True):
    """Cross-section ops of a globe-type valve, seat centre at (0, 0)."""
    o = []
    ang = pattern == "angle"
    obl = pattern == "oblique"

    # ---- body bulb + ports ------------------------------------------------
    if ang:
        body = [(-84, 88), (-62, 64), (-34, 44), (-16, 30), (16, 30),
                (34, 44), (62, 64), (84, 88), (84, 114), (-84, 114)]
        o.append(("poly", body, BULB_F, 1.3, INK, "", True))
        # vertical bore walls (neck + outlet leg in one line)
        o.append(("line", -14, -44, -14, 114, 1.3, INK, ""))
        o.append(("line", 14, -44, 14, 114, 1.3, INK, ""))
        # outlet stub + flange
        o.append(("poly", [(-14, 114), (14, 114), (14, 126), (-14, 126)],
                  BULB_F, 1.2, INK, "", True))
        o.append(("poly", [(-24, 126), (24, 126), (24, 136), (-24, 136)],
                  RING_F, 1.2, INK, "", True))
        # inlet flange faces
        o.append(("poly", [(-92, 82), (-84, 82), (-84, 120), (-92, 120)],
                  RING_F, 1.2, INK, "", True))
        if flow:
            o.append(("line", -118, 101, -96, 101, 1.6, BLUE, ""))
            o.append(("poly", [(-96, 101), (-104, 97.5), (-104, 104.5)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 0, 60, 0, 84, 1.6, BLUE, ""))
            o.append(("poly", [(0, 84), (-3.5, 76), (3.5, 76)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 0, 136, 0, 156, 1.6, BLUE, ""))
            o.append(("poly", [(0, 156), (-3.5, 148), (3.5, 148)],
                      BLUE, 0, BLUE, "", True))
    elif obl:
        body = [(-84, 88), (-62, 64), (-34, 44), (-14, 36), (-14, 24),
                (14, 24), (14, 36), (34, 44), (62, 64), (84, 88), (84, 114),
                (62, 122), (0, 126), (-62, 122), (-84, 114)]
        o.append(("poly", body, BULB_F, 1.3, INK, "", True))
        o.append(("poly", [(-92, 82), (-84, 82), (-84, 120), (-92, 120)],
                  RING_F, 1.2, INK, "", True))
        o.append(("poly", [(92, 82), (84, 82), (84, 120), (92, 120)],
                  RING_F, 1.2, INK, "", True))
        if flow:
            o.append(("line", -118, 101, -96, 101, 1.6, BLUE, ""))
            o.append(("poly", [(-96, 101), (-104, 97.5), (-104, 104.5)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 0, 18, 0, -4, 1.6, BLUE, ""))
            o.append(("poly", [(0, -4), (-3.5, -12), (3.5, -12)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 96, 101, 118, 101, 1.6, BLUE, ""))
            o.append(("poly", [(118, 101), (110, 97.5), (110, 104.5)],
                      BLUE, 0, BLUE, "", True))
    else:  # standard
        body = [(-84, 88), (-62, 64), (-34, 44), (-14, 36), (-14, 24),
                (14, 24), (14, 36), (34, 44), (62, 64), (84, 88), (84, 114),
                (62, 122), (0, 126), (-62, 122), (-84, 114)]
        o.append(("poly", body, BULB_F, 1.3, INK, "", True))
        o.append(("poly", [(-92, 82), (-84, 82), (-84, 120), (-92, 120)],
                  RING_F, 1.2, INK, "", True))
        o.append(("poly", [(92, 82), (84, 82), (84, 120), (92, 120)],
                  RING_F, 1.2, INK, "", True))
        if flow:
            o.append(("line", -118, 101, -96, 101, 1.6, BLUE, ""))
            o.append(("poly", [(-96, 101), (-104, 97.5), (-104, 104.5)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 0, 20, 0, -4, 1.6, BLUE, ""))
            o.append(("poly", [(0, -4), (-3.5, -12), (3.5, -12)],
                      BLUE, 0, BLUE, "", True))
            o.append(("line", 96, 101, 118, 101, 1.6, BLUE, ""))
            o.append(("poly", [(118, 101), (110, 97.5), (110, 104.5)],
                      BLUE, 0, BLUE, "", True))

    # ---- seat rings ---------------------------------------------------------
    bw = 6 if disc == "needle" else 14            # half bore width
    if ang:
        o.append(("poly", [(-14, 34), (-8, 34), (-8, 48), (-14, 48)],
                  RING_F, 1.1, INK, "", True))
        o.append(("poly", [(14, 34), (8, 34), (8, 48), (14, 48)],
                  RING_F, 1.1, INK, "", True))
    else:
        o.append(("poly", [(-26, 16), (-bw, 16), (-bw, 30), (-26, 32)],
                  RING_F, 1.1, INK, "", True))
        o.append(("poly", [(26, 16), (bw, 16), (bw, 30), (26, 32)],
                  RING_F, 1.1, INK, "", True))

    # ---- disc ---------------------------------------------------------------
    top = 16
    if disc == "plug":
        o.append(("poly", [(-12, 2), (12, 2), (bw + 2, top), (-bw - 2, top)],
                  DISC_F, 1.2, INK, "", True))
    elif disc == "soft":
        o.append(("poly", [(-13, 0), (13, 0), (13, top), (-13, top)],
                  DISC_F, 1.2, INK, "", True))
        o.append(("line", -13, 6, 13, 6, 1.0, INK, "2 2"))
    elif disc == "needle":
        o.append(("poly", [(-2.5, -34), (2.5, -34), (1.5, top), (-1.5, top)],
                  DISC_F, 1.2, INK, "", True))
        top = -34
    elif disc == "vport":
        o.append(("poly", [(-12, -14), (12, -14), (bw + 2, top),
                           (-bw - 2, top)], DISC_F, 1.2, INK, "", True))
        for sx in (-6, 6):
            o.append(("line", sx - 2, -14, sx, -6, 1.0, INK, ""))
            o.append(("line", sx + 2, -14, sx, -6, 1.0, INK, ""))
        top = -14
    elif disc == "ball":
        o.append(("circ", 0, 8, 9, 1.2, INK, DISC_F))
        top = -2
    elif disc == "piston":
        plen = 108
        o.append(("poly", [(-12, top - plen), (12, top - plen),
                           (12, top - 2), (-12, top - 2)],
                  DISC_F, 1.2, INK, "", True))
        top = top - plen

    # ---- stem ---------------------------------------------------------------
    if disc not in ("piston", "none"):
        o.append(("line", 0, top, 0, -96, 2.4, INK, ""))

    # ---- stem seal ----------------------------------------------------------
    if seal == "packing":
        o.append(("poly", [(-10, -44), (10, -44), (10, -32), (-10, -32)],
                  PACK_F, 1.0, INK, "", True))
        o.append(("poly", [(-14, -48), (14, -48), (14, -43), (-14, -43)],
                  RING_F, 1.0, INK, "", True))
    elif seal == "bellows":
        zz = []
        for i in range(14):
            yy = -44 - i * 3
            zz.append(((-7 if i % 2 else 7), yy))
        o.append(("poly", zz, "none", 1.2, INK, "", False))
        o.append(("poly", [(-12, -86), (12, -86), (12, -78), (-12, -78)],
                  PACK_F, 1.0, INK, "", True))
        o.append(("poly", [(-15, -92), (15, -92), (15, -86), (-15, -86)],
                  RING_F, 1.0, INK, "", True))
    elif seal == "diaphragm":
        dm = []
        for i in range(13):
            t = i / 12.0
            dm.append((-18 + 36 * t, -46 - 26 * math.sin(math.pi * t)))
        o.append(("poly", dm + [(18, -46), (-18, -46)], "#eceadf", 1.2,
                  INK, "", True))
        o.append(("poly", [(-12, -78), (12, -78), (12, -71), (-12, -71)],
                  PACK_F, 1.0, INK, "", True))
        o.append(("poly", [(-15, -83), (15, -83), (15, -78), (-15, -78)],
                  RING_F, 1.0, INK, "", True))

    # ---- bonnet + joint ------------------------------------------------------
    if bonnet not in ("integral", "pseal"):
        o.append(("poly", [(-30, -96), (30, -96), (30, -44), (-30, -44)],
                  "#efefe9", 1.2, INK, "", True))
    if bonnet == "bolted":
        o.append(("poly", [(-38, -50), (38, -50), (38, -42), (-38, -42)],
                  RING_F, 1.1, INK, "", True))
        for bx in (-30, -10, 10, 30):
            o.append(("line", bx, -52, bx, -40, 1.0, INK, ""))
    elif bonnet == "union":
        o.append(("line", -30, -44, 30, -44, 1.1, INK, ""))
        o.append(("line", -30, -50, 30, -50, 1.1, INK, ""))
        o.append(("poly", [(-38, -52), (-30, -52), (-30, -42), (-38, -42)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(30, -52), (38, -52), (38, -42), (30, -42)],
                  RING_F, 1.0, INK, "", True))
    elif bonnet in ("screwed", "screwed+weld"):
        o.append(("line", -30, -44, 30, -44, 1.1, INK, ""))
        for tx in (-24, -12, 0, 12, 24):
            o.append(("line", tx, -44, tx + 4, -39, 0.9, INK, ""))
        if bonnet == "screwed+weld":
            for wx in (-27, 27):
                o.append(("poly", [(wx - 4, -44), (wx + 4, -44),
                                   (wx, -52)], RING_F, 1.0, INK, "", True))
    elif bonnet == "welded":
        for wx in (-27, 27):
            o.append(("poly", [(wx - 4, -44), (wx + 4, -44), (wx, -52)],
                      RING_F, 1.0, INK, "", True))
    elif bonnet == "pseal":
        o.append(("poly", [(-24, -96), (24, -96), (16, -44), (-16, -44)],
                  "#efefe9", 1.2, INK, "", True))
        o.append(("line", -32, -44, -16, -44, 1.2, INK, ""))
        o.append(("line", 32, -44, 16, -44, 1.2, INK, ""))
        o.append(("poly", [(-30, -48), (-24, -48), (-24, -41), (-30, -41)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", [(30, -48), (24, -48), (24, -41), (30, -41)],
                  RING_F, 1.0, INK, "", True))
    elif bonnet == "integral":
        pass
    if special == "split":
        o.append(("line", -26, 72, 26, 72, 1.3, INK, ""))
        o.append(("line", -26, 78, 26, 78, 1.0, INK, ""))

    # ---- screw / handwheel ---------------------------------------------------
    if screw == "internal":
        for ty in range(-88, -52, 8):
            o.append(("line", -5, ty, 5, ty + 3, 0.8, INK, ""))
        o.append(("poly", _ell(0, -104, 30, 8), "#e8e8e2", 1.2, INK, "", True))
        o.append(("circ", 0, -104, 5, 1.2, INK, RING_F))
    elif screw == "external":
        o.append(("line", -30, -44, -30, -128, 1.6, INK, ""))
        o.append(("line", 30, -44, 30, -128, 1.6, INK, ""))
        o.append(("poly", [(-22, -136), (22, -136), (22, -127), (-22, -127)],
                  RING_F, 1.1, INK, "", True))
        o.append(("line", 0, top if disc != "piston" else top,
                  0, -146, 2.4, INK, ""))
        if special == "impact":
            o.append(("poly", _ell(0, -152, 20, 6), "#e8e8e2", 1.2, INK,
                      "", True))
            o.append(("poly", _ell(0, -152, 34, 9), "#e8e8e2", 1.4, INK,
                      "", True))
        else:
            o.append(("poly", _ell(0, -152, 32, 8), "#e8e8e2", 1.2, INK,
                      "", True))
        o.append(("circ", 0, -152, 5, 1.2, INK, RING_F))
    elif screw == "nonrot":
        o.append(("line", -30, -44, -30, -128, 1.6, INK, ""))
        o.append(("line", 30, -44, 30, -128, 1.6, INK, ""))
        o.append(("poly", [(-22, -136), (22, -136), (22, -127), (-22, -127)],
                  RING_F, 1.1, INK, "", True))
        o.append(("line", 0, top, 0, -146, 2.4, INK, ""))
        o.append(("poly", [(-6, -30), (6, -30), (6, -20), (-6, -20)],
                  RING_F, 1.0, INK, "", True))
        o.append(("poly", _ell(0, -152, 32, 8), "#e8e8e2", 1.2, INK, "", True))
        o.append(("circ", 0, -152, 5, 1.2, INK, RING_F))
    return o


FIGS3 = {}


def _reg3(f):
    FIGS3[f.__name__] = f
    return f


# ------------------------------------------------------------ Figure 3-1
@_reg3
def fig_vsh_3_1():
    """Source Figure 3-1 — principal valve types grouped by flow regulation."""
    w, h = 600, 332
    o = [_defs()]
    cols = [
        (BLUE, "#eef3fb", "1 · CLOSING-DOWN", "van đóng (hướng trục)",
         "stopper di chuyển dọc trục chỗ kín",
         "stopper moves along the seat axis",
         ["globe (thẳng / góc / nghiêng)",
          "piston", "needle — kim"]),
        (GREEN, "#eaf3ec", "2 · SLIDE", "van trượt",
         "cửa nêm trượt ngang qua đường dòng",
         "gate slides across the flow passage",
         ["parallel gate — cửa song song",
          "wedge gate — cửa nêm",
          "knife gate — cửa dao",
          "conduit gate — cửa ống dẫn"]),
        (GOLD, "#faf5e6", "3 · ROTARY", "van quay",
         "ph part quay quanh trục vuông góc dòng",
         "plug/disc rotates about an axis normal to the flow",
         ["plug (thường / bôi trơn / lệ tâm)",
          "ball — bi", "butterfly — bướm"]),
        (RED, "#fbeeea", "4 · FLEX-BODY", "van thân mềm",
         "phần đóng làm mềm thân van",
         "closure member flexes the valve body",
         ["pinch — kẹp (ống mềm)",
          "diaphragm (weir / thẳng)"]),
    ]
    for i, (col, bg, ti, tvi, ds_vi, ds_en, names) in enumerate(cols):
        x = 12 + i * 146
        o.append(_box(x, 14, 138, 214, "", fill=bg))
        o.append(_txt(x + 69, 32, ti, 9.2, weight="bold", color=col))
        o.append(_txt(x + 69, 44, tvi, 7.4, color=GREY))
        # glyph: seat gap + closure member movement arrow
        gy = 78
        o.append(_poly([(x + 24, gy + 10), (x + 50, gy + 10), (x + 50, gy + 16),
                        (x + 24, gy + 16)], fill=RING_F, sw=1.0))
        if i == 0:      # closing-down: vertical stopper
            o.append(_poly([(x + 33, gy - 16), (x + 41, gy - 16),
                            (x + 41, gy + 9), (x + 33, gy + 9)],
                           fill=DISC_F, sw=1.0))
            o.append(_arrow(x + 37, gy - 34, x + 37, gy - 20, 1.1, color=col))
            o.append(_arrow(x + 37, gy - 6, x + 37, gy - 18, 0.9, color=GREY))
        elif i == 1:    # slide: horizontal gate
            o.append(_poly([(x + 26, gy - 8), (x + 62, gy - 8),
                            (x + 62, gy + 1), (x + 26, gy + 1)],
                           fill=DISC_F, sw=1.0))
            o.append(_arrow(x + 62, gy - 4, x + 78, gy - 4, 1.1, color=col))
        elif i == 2:    # rotary: disc on shaft
            o.append(_circle(x + 37, gy - 3, 10, sw=1.1, color=INK))
            o.append(_line(x + 37, gy - 13, x + 37, gy - 24, 1.1))
            o.append(_path("M%d %d A10 10 0 0 1 %d %d"
                           % (x + 27, gy - 3, x + 37, gy - 13),
                           sw=1.0, color=col))
        else:           # flex-body: tube squeezed
            o.append(_path("M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d"
                           % (x + 24, gy - 2, x + 34, gy - 2, x + 35, gy + 3,
                              x + 37, gy + 3, x + 39, gy + 3, x + 40, gy - 2,
                              x + 50, gy - 2), sw=1.6))
            o.append(_arrow(x + 37, gy - 22, x + 37, gy - 10, 1.1, color=col))
        for j, nm in enumerate(names):
            o.append(_txt(x + 69, 106 + j * 17, nm, 7.4, color=INK))
        o.append(_line(x + 12, 96 + len(names) * 17, x + 126,
                       96 + len(names) * 17, 0.7, dash="2 3", color=GREY))
        o.append(_txt(x + 69, 208, ds_vi, 6.6, color=GREY))
        o.append(_txt(x + 69, 219, ds_en, 6.6, color=GREY))
    o.append(_txt(300, 258, "Chọn nhóm theo nhiệm vụ · pick the group by duty:",
                  8.4, weight="bold"))
    o.append(_txt(300, 276, "dừng/khởi động dòng → nhóm 2, 3, 4 (trở lực thấp)",
                  7.4, color=GREY))
    o.append(_txt(300, 288, "khống chế lưu lượng → nhóm 1 (hành trình ∝ mở chỗ kín)",
                  7.4, color=GREY))
    o.append(_txt(300, 300, "phân luồng dòng (3+ cổng) → van quay: plug, ball",
                  7.4, color=GREY))
    o.append(_txt(300, 312, "chất lỏng có rắn lơ lửng → trượt/kẹp có chuyển động quét",
                  7.4, color=GREY))
    return _fig(svg(w, h, "".join(o), "Valve groups by flow regulation"),
                "Hình 3-1 · Các kiểu van chính, nhóm theo phương pháp khống chế "
                "dòng (vẽ lại theo nguồn): đóng hướng trục — van cầu, piston, "
                "kim; trượt — van cửa; quay — van phích, bi, bướm; thân mềm — "
                "van kẹp, van màng. Kèm gợi ý chọn nhóm theo nhiệm vụ.",
                "Figure 3-1 · Principal types of valves grouped according to "
                "the method of flow regulation — redrawn: closing-down, slide, "
                "rotary and flex-body groups, with the duty-based selection "
                "hints.",
                "Bốn nhóm van theo phương pháp khống chế dòng.",
                "Four valve groups by method of flow regulation.")


# --------------------------------------------------- globe variant factory
def _globe_variant_fig(num, pattern, bonnet, screw, seal, disc, special,
                       feats, title_en, title_vi, courtesy):
    """One redrawn globe-valve cutaway with numbered feature legend."""
    w, h = 560, 360
    o = [_defs()]
    ox, oy = 205, 190                       # seat centre on canvas
    if pattern == "oblique":
        ox, oy = 160, 185
    ops = _globe_ops(pattern, bonnet, screw, seal, disc, special)
    _emit(o, ops, rot=-45 if pattern == "oblique" else 0.0, cx=0, cy=0,
          dx=ox, dy=oy)
    # feature markers
    marks = []
    k = 0
    for key, pos in feats:
        k += 1
        marks.append((key, pos, k))
    for key, pos, n in marks:
        _emit(o, [("dot", pos[0], pos[1], n)], rot=-45 if pattern == "oblique"
              else 0.0, cx=0, cy=0, dx=ox, dy=oy)
    # legend column
    o.append(_line(392, 40, 392, 320, 0.8, dash="2 3", color=GREY))
    yy = 66
    for key, pos, n in marks:
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(n), 7.6, weight="bold"))
        vi, en = key
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.8, anchor="start", color=GREY))
        yy += 30
    o.append(_txt(476, 330, courtesy, 6.6, color=GREY))
    o.append(_txt(200, 344, "mũi tên xanh = hướng dòng · blue arrows = flow",
                  6.8, color=GREY))
    return _fig(svg(w, h, "".join(o), title_en),
                "Hình 3-%d · %s (vẽ lại). Nguồn: %s." % (num, title_vi,
                                                         courtesy),
                "Figure 3-%d · %s — redrawn. (Courtesy of %s.)"
                % (num, title_en, courtesy),
                title_vi, title_en)


# --------------------------------------------------- Figures 3-2 … 3-12
def _gv(num, pattern, bonnet, screw, seal, disc, special, feats, ten, tvi,
        courtesy):
    return _globe_variant_fig(num, pattern, bonnet, screw, seal, disc, special,
                              feats, ten, tvi, courtesy)


@_reg3
def fig_vsh_3_2():
    return _gv(2, "standard", "union", "internal", "packing", "soft", None,
               [(("\u0111\u0129a m\u1ec1m thay \u0111\u01b0\u1ee3c",
                  "renewable soft disc"), (0, 4)),
                (("n\u1eafp kh\u1edbp n\u1ed1i", "union bonnet"), (-40, -47)),
                (("tr\u1ee5c v\u00edt trong", "internal screw"), (26, -104)),
                (("gio\u0103ng tr\u1ee5c", "stem packing"), (-26, -38))],
               "Globe valve, standard pattern, union bonnet, internal screw "
               "and renewable soft disc",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp kh\u1edbp n\u1ed1i, "
               "tr\u1ee5c v\u00edt trong v\u00e0 \u0111\u0129a m\u1ec1m thay "
               "\u0111\u01b0\u1ee3c", "Crane Co.")


@_reg3
def fig_vsh_3_3():
    return _gv(3, "standard", "union", "internal", "packing", "plug", None,
               [(("\u0111\u0129a ph\u00edch", "plug disc"), (0, -8)),
                (("n\u1eafp kh\u1edbp n\u1ed1i", "union bonnet"), (-40, -47)),
                (("tr\u1ee5c v\u00edt trong", "internal screw"), (26, -104))],
               "Globe valve, standard pattern, union bonnet, internal screw, "
               "plug disc",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp kh\u1edbp "
               "n\u1ed1i, tr\u1ee5c v\u00edt trong, \u0111\u0129a ph\u00edch",
               "Crane Co.")


@_reg3
def fig_vsh_3_4():
    return _gv(4, "angle", "screwed", "internal", "packing", "needle", None,
               [(("\u0111\u0129a kim", "needle disc"), (0, -22)),
                (("n\u1eafp v\u00e1n \u1eb9p", "screwed-in bonnet"), (32, -42)),
                (("ki\u1ec3u g\u00f3c 90\u00b0", "angle pattern"), (105, 60)),
                (("tr\u1ee5c v\u00edt trong", "internal screw"), (26, -104))],
               "Globe valve, angle pattern, screwed-in bonnet, internal "
               "screw, needle disc",
               "Van c\u1ea7u ki\u1ec3u g\u00f3c, n\u1eafp v\u00e1n \u1eb9p, "
               "tr\u1ee5c v\u00edt trong, \u0111\u0129a kim", "Crane Co.")


@_reg3
def fig_vsh_3_5():
    return _gv(5, "standard", "integral", "external", "packing", "plug", None,
               [(("n\u1eafp li\u1ec1n th\u00e2n", "integral bonnet"), (0, -70)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -152)),
                (("\u0111\u0129a ph\u00edch", "plug disc"), (0, -8))],
               "Globe valve, standard pattern, integral bonnet, external "
               "screw, plug disc",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp li\u1ec1n th\u00e2n, "
               "tr\u1ee5c v\u00edt ngo\u00e0i, \u0111\u0129a ph\u00edch",
               "Velan Engineering Limited")


@_reg3
def fig_vsh_3_6():
    return _gv(6, "standard", "welded", "external", "bellows", "plug", None,
               [(("gio\u0103ng g\u1ea7n (bellows)", "bellows stem seal"),
                 (-24, -64)),
                (("gio\u0103ng n\u00e9n ph\u1ee5 tr\u1ee3",
                  "auxiliary compression packing"), (-26, -82)),
                (("n\u1eafp h\u00e0n", "welded bonnet"), (30, -46)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -152))],
               "Globe valve, standard pattern, welded bonnet, external screw, "
               "plug disc, bellows stem seal with auxiliary compression packing",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp h\u00e0n, "
               "tr\u1ee5c v\u00edt ngo\u00e0i, \u0111\u0129a ph\u00edch, "
               "gio\u0103ng g\u1ea7n k\u00e8m gio\u0103ng n\u00e9n ph\u1ee5 "
               "tr\u1ee3", "Pegler Hattersley Limited")


@_reg3
def fig_vsh_3_7():
    return _gv(7, "oblique", "screwed+weld", "external", "diaphragm", "plug",
               None,
               [(("m\u00e0ng v\u00f2m ch\u1ecbm", "domed diaphragm stem seal"),
                 (-28, -58)),
                (("gio\u0103ng n\u00e9n ph\u1ee5 tr\u1ee3",
                  "auxiliary compression packing"), (-26, -76)),
                (("n\u1eafp v\u00e1n \u1eb9p + h\u00e0n k\u00edn",
                  "screwed-in and seal-welded bonnet"), (30, -44)),
                (("d\u1ee5ng cho h\u1ea1t nh\u00e2n", "nuclear application"),
                 (85, -20))],
               "Globe valve, oblique pattern, screwed-in and seal-welded "
               "bonnet, external screw, plug disc, domed diaphragm stem seal "
               "with auxiliary compression packing, nuclear application",
               "Van c\u1ea7u ki\u1ec3u nghi\u00eang, n\u1eafp v\u00e1n "
               "\u1eb9p v\u00e0 h\u00e0n k\u00edn, tr\u1ee5c v\u00edt "
               "ngo\u00e0i, \u0111\u0129a ph\u00edch, gio\u0103ng m\u00e0ng "
               "v\u00f2m k\u00e8m gio\u0103ng n\u00e9n ph\u1ee5 tr\u1ee3, "
               "d\u1ee5ng cho h\u1ea1t nh\u00e2n", "Edward Valves Inc.")


@_reg3
def fig_vsh_3_8():
    return _gv(8, "angle", "bolted", "external", "packing", "vport", None,
               [(("v\u00e1y V-Port", "V-port skirt"), (0, -10)),
                (("n\u1eafp b\u00e1n l\u1eb7p", "bolted bonnet"), (40, -46)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -152)),
                (("khống chế mịn", "sensitive throttling"), (105, 60))],
               "Globe valve, angle pattern, bolted bonnet, external screw, "
               "plug disc with V-port skirt for sensitive throttling control",
               "Van c\u1ea7u ki\u1ec3u g\u00f3c, n\u1eafp b\u00e1n l\u1eb7p, "
               "tr\u1ee5c v\u00edt ngo\u00e0i, \u0111\u0129a ph\u00edch c\u00f3 "
               "v\u00e1y V-Port cho kh\u1ed1ng ch\u1ebf m\u1ecbn",
               "Crane Co.")


@_reg3
def fig_vsh_3_9():
    return _gv(9, "standard", "bolted", "external", "packing", "plug", None,
               [(("n\u1eafp b\u00e1n l\u1eb7p", "bolted bonnet"), (40, -46)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -152)),
                (("\u0111\u0129a ph\u00edch", "plug disc"), (0, -8))],
               "Globe valve, standard pattern, bolted bonnet, external screw, "
               "plug disc",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp b\u00e1n "
               "l\u1eb7p, tr\u1ee5c v\u00edt ngo\u00e0i, \u0111\u0129a "
               "ph\u00edch", "Crane Co.")


@_reg3
def fig_vsh_3_10():
    return _gv(10, "oblique", "pseal", "external", "packing", "plug",
               "impact",
               [(("n\u1eafp k\u00edn \u00e1p (pressure-seal)",
                  "pressure-seal bonnet"), (-30, -44)),
                (("b\u00e1nh tay v\u00e2m (impact handwheel)",
                  "impact handwheel"), (38, -152)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -128))],
               "Globe valve, oblique pattern, pressure-seal bonnet, external "
               "screw with impact handwheel, plug disc",
               "Van c\u1ea7u ki\u1ec3u nghi\u00eang, n\u1eafp k\u00edn "
               "\u00e1p, tr\u1ee5c v\u00edt ngo\u00e0i k\u00e8m b\u00e1nh tay "
               "v\u00e2m, \u0111\u0129a ph\u00edch", "Edward Valves Inc.")


@_reg3
def fig_vsh_3_11():
    return _gv(11, "standard", "integral", "nonrot", "packing", "plug", None,
               [(("\u0111\u0129a li\u1ec1n tr\u1ee5c kh\u00f4ng quay",
                  "disc integral with non-rotating stem"), (10, -24)),
                (("n\u1eafp li\u1ec1n th\u00e2n", "integral bonnet"),
                 (0, -70)),
                (("tr\u1ee5c v\u00edt ngo\u00e0i", "external screw"),
                 (34, -152))],
               "Globe valve, standard pattern, integral bonnet, plug-type "
               "disc integral with non-rotating stem",
               "Van c\u1ea7u, ki\u1ec3u chu\u1ea9n, n\u1eafp li\u1ec1n "
               "th\u00e2n, \u0111\u0129a ph\u00edch li\u1ec1n v\u1edbi "
               "tr\u1ee5c kh\u00f4ng quay", "Sempell A.G.")


@_reg3
def fig_vsh_3_12():
    return _gv(12, "oblique", "bolted", "external", "packing", "plug",
               "split",
               [(("th\u00e2n t\u00e1ch l\u00f9a", "split body"), (30, 75)),
                (("c\u01a1 ch\u1ebf qu\u00e9t ch\u1ed7 k\u00edn",
                  "seat-wiping mechanism"), (0, -6)),
                (("d\u00f9ng cho slurry (h\u1ed7n h\u1ee3p qu\u00e1nh)",
                  "slurry service"), (85, 80))],
               "Globe valve, oblique pattern, split body, external screw, "
               "with seat-wiping mechanism for slurry service",
               "Van c\u1ea7u ki\u1ec3u nghi\u00eang, th\u00e2n t\u00e1ch "
               "l\u00f9a, tr\u1ee5c v\u00edt ngo\u00e0i, c\u00f3 c\u01a1 "
               "ch\u1ebf qu\u00e9t ch\u1ed7 k\u00edn cho d\u1ecbch v\u1ee5 "
               "slurry", "Langley Alloys Limited")


# ------------------------------------------------------ Figure 3-13 (drain)
@_reg3
def fig_vsh_3_13():
    """Source Figure 3-13 — globe valve for draining vessels, seat flush."""
    w, h = 560, 360
    o = [_defs()]
    cx = 200
    # vessel bottom plate (hatched, spans width)
    o.append(_rect(60, 96, 280, 12, fill="url(#h6)", sw=1.1))
    o.append(_txt(66, 88, "\u0111\u00e1y b\u00ecnh / vessel bottom", 7.4,
                  anchor="start"))
    # body block below plate with bore
    o.append(_poly([(cx - 34, 108), (cx + 34, 108), (cx + 34, 168),
                    (cx - 34, 168)], fill=BULB_F, sw=1.2, close=True))
    o.append(_line(cx - 12, 108, cx - 12, 168, 1.2, color=INK))
    o.append(_line(cx + 12, 108, cx + 12, 168, 1.2, color=INK))
    # seat rings flush with plate
    o.append(_poly([(cx - 22, 96), (cx - 12, 96), (cx - 12, 110),
                    (cx - 22, 110)], fill=RING_F, sw=1.0, close=True))
    o.append(_poly([(cx + 22, 96), (cx + 12, 96), (cx + 12, 110),
                    (cx + 22, 110)], fill=RING_F, sw=1.0, close=True))
    # disc below seat (pushed up to close), stem down to bonnet
    o.append(_poly([(cx - 10, 114), (cx + 10, 114), (cx + 11, 130),
                    (cx - 11, 130)], fill=DISC_F, sw=1.2, close=True))
    o.append(_line(cx, 130, cx, 176, 2.4, color=INK))
    # bonnet below + handwheel
    o.append(_poly([(cx - 26, 176), (cx + 26, 176), (cx + 26, 216),
                    (cx - 26, 216)], fill="#efefe9", sw=1.2, close=True))
    o.append(_poly([(cx - 10, 176), (cx + 10, 176), (cx + 10, 188),
                    (cx - 10, 188)], fill=PACK_F, sw=1.0, close=True))
    o.append(_poly(_ell(cx, 226, 32, 8), "#e8e8e2", sw=1.2, close=True))
    o.append(_circle(cx, 226, 5, sw=1.1, color=INK))
    # drain flow
    o.append(_line(cx, 84, cx, 60, 1.6, color=BLUE, dash=""))
    o.append(_poly([(cx, 60), (cx - 3.5, 68), (cx + 3.5, 68)], fill=BLUE,
                   sw=0, close=True))
    o.append(_txt(476, 330, "Langley Alloys Limited.", 6.6, color=GREY))
    # legend
    for i, (vi, en) in enumerate([
            ("ch\u1ed7 k\u00edn s\u00e1t \u0111\u00e1y b\u00ecnh",
             "seat flush with vessel bottom"),
            ("\u0111\u0129a \u0111\u00f3ng h\u01b0\u1edbng l\u00ean",
             "disc closes upward"),
            ("bonnet d\u01b0\u1edbi, x\u1ea3 n\u01b0\u1edbc \u0111\u1ea7y "
             "b\u00ecnh", "drains the vessel completely")]):
        yy = 80 + i * 30
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.8, anchor="start", color=GREY))
    o.append(_circle(cx, 104, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx, 104.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx, 122, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx, 122.5, "2", 8.0, weight="bold"))
    o.append(_circle(cx, 196, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx, 196.5, "3", 8.0, weight="bold"))
    return _fig(svg(w, h, "".join(o), "Globe valve for draining vessels"),
                "H\u00ecnh 3-13 \u00b7 Van c\u1ea7u d\u00f9ng \u0111\u1ec3 "
                "x\u1ea3 n\u01b0\u1edbc b\u00ecnh ch\u1ee9a, ch\u1ed7 k\u00edn "
                "s\u00e1t l\u00e9t \u0111\u00e1y b\u00ecnh (v\u1ebd l\u1ea1i). "
                "Ngu\u1ed3n: Langley Alloys Limited.",
                "Figure 3-13 \u00b7 Globe valve adapted for the draining of "
                "vessels, seat flush with bottom of vessel — redrawn. "
                "(Courtesy of Langley Alloys Limited.)",
                "Van x\u1ea3 b\u00ecnh, ch\u1ed7 k\u00edn s\u00e1t \u0111\u00e1y.",
                "Vessel drain valve, seat flush with bottom.")


# ------------------------------------------------- Figure 3-14 (three-way)
@_reg3
def fig_vsh_3_14():
    """Source Figure 3-14 — three-way change-over globe for PRV installs."""
    w, h = 560, 360
    o = [_defs()]
    cx, cy = 230, 210
    # bottom inlet flange + stub
    o.append(_poly([(cx - 24, cy + 40), (cx + 24, cy + 40), (cx + 24, cy + 52),
                    (cx - 24, cy + 52)], fill=RING_F, sw=1.2, close=True))
    # body: central block with two angled branch necks
    o.append(_poly([(cx - 30, cy - 36), (cx + 30, cy - 36), (cx + 30, cy + 28),
                    (cx - 30, cy + 28)], fill=BULB_F, sw=1.2, close=True))
    for s in (-1, 1):
        o.append(_poly([(cx + s * 30, cy - 36), (cx + s * 78, cy - 84),
                        (cx + s * 96, cy - 70), (cx + s * 30, cy - 6)],
                       fill=BULB_F, sw=1.2, close=True))
        # branch flange
        o.append(_poly([(cx + s * 78 - 8, cy - 84), (cx + s * 96, cy - 70),
                        (cx + s * 110, cy - 88), (cx + s * 92, cy - 102)],
                       fill=RING_F, sw=1.1, close=True))
    # seats at branch entries
    for s in (-1, 1):
        o.append(_poly([(cx + s * 30 - (8 if s < 0 else 0), cy - 30),
                        (cx + s * 30 + (8 if s > 0 else 0), cy - 30),
                        (cx + s * 30, cy - 16)], fill=RING_F, sw=1.0,
                       close=True))
    # disc shown sealing the LEFT branch; right branch open
    o.append(_poly([(cx - 34, cy - 34), (cx - 12, cy - 34), (cx - 12, cy - 20),
                    (cx - 34, cy - 20)], fill=DISC_F, sw=1.2, close=True))
    o.append(_line(cx - 23, cy - 34, cx - 23, cy - 52, 2.2, color=INK))
    # yoke + handwheel over centre
    o.append(_line(cx - 30, cy + 28, cx - 30, cy - 96, 1.4, color=INK))
    o.append(_line(cx + 30, cy + 28, cx + 30, cy - 96, 1.4, color=INK))
    o.append(_poly([(cx - 22, cy - 104), (cx + 22, cy - 104), (cx + 22,
                    cy - 95), (cx - 22, cy - 95)], fill=RING_F, sw=1.1,
                   close=True))
    o.append(_poly(_ell(cx, cy - 112, 30, 8), "#e8e8e2", sw=1.2, close=True))
    o.append(_circle(cx, cy - 112, 5, sw=1.1, color=INK))
    # flows: bottom in, out to right branch; left branch blocked
    o.append(_line(cx, cy + 74, cx, cy + 56, 1.6, color=BLUE))
    o.append(_poly([(cx, cy + 56), (cx - 3.5, cy + 64), (cx + 3.5, cy + 64)],
                   fill=BLUE, sw=0, close=True))
    o.append(_line(cx + 14, cy, cx + 62, cy - 44, 1.6, color=BLUE))
    o.append(_poly([(cx + 62, cy - 44), (cx + 53, cy - 44), (cx + 57, cy - 51)],
                   fill=BLUE, sw=0, close=True))
    o.append(_line(cx - 14, cy, cx - 20, cy - 8, 1.4, color=RED))
    o.append(_txt(cx - 26, cy - 14, "kh\u00f3a / isolated", 6.8, anchor="end",
                  color=RED))
    o.append(_txt(cx + 40, cy - 52, "ph\u1ee5c v\u1ee5 / in service", 6.8,
                  color=GREEN))
    o.append(_txt(476, 330, "Bopp & Reuther GmbH.", 6.6, color=GREY))
    for i, (vi, en) in enumerate([
            ("van ba l\u1ed9 chuy\u1ec3n m\u1ea1ch",
             "three-way change-over valve"),
            ("m\u1ed9t PRV b\u1ecb c\u00f4 l\u1eadp", "one PRV isolated"),
            ("PRV kia \u0111ang ph\u1ee5c v\u1ee5",
             "the second PRV in service")]):
        yy = 80 + i * 30
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.8, anchor="start", color=GREY))
    o.append(_circle(cx, cy - 4, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx, cy - 3.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx - 24, cy - 28, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 24, cy - 27.5, "2", 8.0, weight="bold"))
    o.append(_circle(cx + 36, cy - 26, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx + 36, cy - 25.5, "3", 8.0, weight="bold"))
    return _fig(svg(w, h, "".join(o), "Three-way change-over globe valve"),
                "H\u00ecnh 3-14 \u00b7 Van c\u1ea7u ba l\u1ed9 d\u00f9ng "
                "nh\u01b0 van chuy\u1ec3n m\u1ea1ch trong thi\u1ebft b\u1ecb "
                "\u0111\u1eb7t van an t\u00e0n \u00e1p su\u1ea5t: m\u1ed9t van "
                "an t\u00e0n b\u1ecb c\u00f4 l\u1eadp trong khi van kia "
                "\u0111ang ph\u1ee5c v\u1ee5 (v\u1ebd l\u1ea1i). Ngu\u1ed3n: "
                "Bopp & Reuther GmbH.",
                "Figure 3-14 \u00b7 Globe valve, three-way, used as change-over "
                "valve in pressure relief valve installations: one pressure "
                "relief valve is isolated while the second one is in service "
                "— redrawn. (Courtesy of Bopp & Reuther GmbH.)",
                "Van ba l\u1ed9 chuy\u1ec3n m\u1ea1ch hai PRV.",
                "Three-way change-over between two PRVs.")


# ------------------------------------------ Figures 3-15 / 3-16 (seatings)
@_reg3
def fig_vsh_3_15():
    """Source Figure 3-15 — seating configurations in globe valves (a-d)."""
    w, h = 640, 250
    o = [_defs()]
    pw, ph, gap = 140, 150, 18
    panels = [
        ("a) ph\u1eb3ng / flat", "t\u1ef1 c\u0103n ch\u1ec9nh, k\u00edn kh\u00f4ng "
         "ma s\u00e1t", "self-aligning, friction-free mating"),
        ("b) c\u00f4n h\u1eb9p / narrow taper", "\u1ee9ng su\u00e1t r\u1ea5t cao, "
         "d\u1ec5 h\u01b0 h\u1ea1i", "very high stress, easily damaged"),
        ("c) c\u00f4n r\u1ed9ng / wide taper", "d\u1eabn d\u1eaft \u0111\u0129a "
         "t\u1ed1t, ch\u1ec9nh s\u00e2u h\u1eb9p d\u1ea7n",
         "guides the disc; width grows with load"),
        ("d) bi / ball on taper", "ti\u1ebfp x\u00fac tuy\u1ebfn, \u1ee9ng su\u00e1t "
         "c\u1ef1c cao", "line contact, extremely high stress"),
    ]
    for i, (ti, dv, de) in enumerate(panels):
        x0 = 14 + i * (pw + gap)
        y0 = 20
        o.append(_box(x0, y0, pw, ph, "", fill="#fafaf7"))
        o.append(_txt(x0 + pw / 2, y0 + 16, ti, 8.0, weight="bold"))
        scx, scy = x0 + pw / 2, y0 + 66          # seat contact level
        if i == 0:      # flat
            o.append(_rect(scx - 34, scy - 14, 68, 14, fill=DISC_F, sw=1.1))
            o.append(_rect(scx - 46, scy, 92, 12, fill=RING_F, sw=1.1))
            o.append(_line(scx, scy - 34, scx, scy - 14, 2.2, color=INK))
        elif i == 1:    # narrow taper
            o.append(_poly([(scx - 6, scy - 34), (scx + 6, scy - 34),
                            (scx + 8, scy), (scx - 8, scy)], fill=DISC_F,
                           sw=1.1, close=True))
            o.append(_poly([(scx - 40, scy), (scx - 8, scy), (scx - 10, scy + 12),
                            (scx - 40, scy + 12)], fill=RING_F, sw=1.1,
                           close=True))
            o.append(_poly([(scx + 40, scy), (scx + 8, scy), (scx + 10, scy + 12),
                            (scx + 40, scy + 12)], fill=RING_F, sw=1.1,
                           close=True))
        elif i == 2:    # wide taper
            o.append(_poly([(scx - 3, scy - 40), (scx + 3, scy - 40),
                            (scx + 16, scy + 16), (scx - 16, scy + 16)],
                           fill=DISC_F, sw=1.1, close=True))
            o.append(_poly([(scx - 44, scy), (scx - 3, scy), (scx - 4, scy + 5),
                            (scx - 20, scy + 16), (scx - 44, scy + 16)],
                           fill=RING_F, sw=1.1, close=True))
            o.append(_poly([(scx + 44, scy), (scx + 3, scy), (scx + 4, scy + 5),
                            (scx + 20, scy + 16), (scx + 44, scy + 16)],
                           fill=RING_F, sw=1.1, close=True))
        else:           # ball on taper
            o.append(_circle(scx, scy - 14, 16, sw=1.1, color=INK))
            o.append(_rect(scx - 34, scy - 34, 68, 20, fill="none", sw=0))
            o.append(_poly([(scx - 40, scy + 2), (scx - 5, scy + 2),
                            (scx - 12, scy + 16), (scx - 40, scy + 16)],
                           fill=RING_F, sw=1.1, close=True))
            o.append(_poly([(scx + 40, scy + 2), (scx + 5, scy + 2),
                            (scx + 12, scy + 16), (scx + 40, scy + 16)],
                           fill=RING_F, sw=1.1, close=True))
            o.append(_line(scx, scy - 46, scx, scy - 30, 2.2, color=INK))
        o.append(_txt(x0 + pw / 2, y0 + ph - 26, dv, 6.8, color=GREY))
        o.append(_txt(x0 + pw / 2, y0 + ph - 14, de, 6.8, color=GREY))
    o.append(_txt(320, 238, "\u1ee9ng su\u00e1t k\u00edn t\u0103ng d\u1ea7n "
                  "t\u1eeb a \u2192 d \u00b7 seating stress increases a \u2192 d",
                  7.6, color=GREY))
    return _fig(svg(w, h, "".join(o), "Globe valve seating configurations"),
                "H\u00ecnh 3-15 \u00b7 C\u00e1c c\u1ea5u h\u00ecnh ch\u1ed7 "
                "k\u00edn th\u01b0\u1eddng d\u00f9ng trong van c\u1ea7u "
                "(v\u1ebd l\u1ea1i): (a) ph\u1eb3ng \u2014 (b) c\u00f4n "
                "m\u1eb7t h\u1eb9p \u2014 (c) c\u00f4n m\u1eb7t r\u1ed9ng "
                "\u2014 (d) \u0111\u0129a bi ti\u1ebfp x\u00fac tuy\u1ebfn "
                "v\u1edbi ch\u1ed7 k\u00edn c\u00f4n.",
                "Figure 3-15 \u00b7 Seating configurations frequently employed "
                "in globe valves — redrawn: (a) flat, (b) narrow tapered face, "
                "(c) wide tapered face, (d) ball disc with line contact on a "
                "tapered seat.",
                "B\u1ed1n c\u1ea5u h\u00ecnh ch\u1ed7 k\u00edn van c\u1ea7u.",
                "Four globe valve seating configurations.")


@_reg3
def fig_vsh_3_16():
    """Source Figure 3-16 — globe seatings adapted for throttling duty."""
    w, h = 640, 230
    o = [_defs()]
    # panel 1: needle seat
    x0, y0 = 14, 18
    o.append(_box(x0, y0, 300, 170, "", fill="#fafaf7"))
    o.append(_txt(x0 + 150, y0 + 16, "\u0111\u0129a kim / needle seat", 8.2,
                  weight="bold"))
    cx, cy = x0 + 150, y0 + 92
    o.append(_poly([(cx - 44, cy - 4), (cx - 8, cy - 4), (cx - 10, cy + 10),
                    (cx - 44, cy + 10)], fill=RING_F, sw=1.1, close=True))
    o.append(_poly([(cx + 44, cy - 4), (cx + 8, cy - 4), (cx + 10, cy + 10),
                    (cx + 44, cy + 10)], fill=RING_F, sw=1.1, close=True))
    o.append(_poly([(cx - 2.5, cy - 56), (cx + 2.5, cy - 56), (cx + 1.5, cy - 4),
                    (cx - 1.5, cy - 4)], fill=DISC_F, sw=1.1, close=True))
    o.append(_line(cx, cy - 56, cx, cy - 74, 2.0, color=INK))
    o.append(_txt(cx, cy + 40, "m\u1ecfng tinh ch\u1ec9nh l\u01b0u l\u01b0\u1ee3ng "
                  "nh\u1ecf", 6.8, color=GREY))
    o.append(_txt(cx, cy + 52, "fine adjustment of small flows", 6.8,
                  color=GREY))
    # panel 2: V-port seat
    x0 = 332
    o.append(_box(x0, y0, 300, 170, "", fill="#fafaf7"))
    o.append(_txt(x0 + 150, y0 + 16, "v\u00e1y V-Port / V-port skirt", 8.2,
                  weight="bold"))
    cx, cy = x0 + 150, y0 + 92
    o.append(_poly([(cx - 44, cy - 4), (cx - 10, cy - 4), (cx - 12, cy + 10),
                    (cx - 44, cy + 10)], fill=RING_F, sw=1.1, close=True))
    o.append(_poly([(cx + 44, cy - 4), (cx + 10, cy - 4), (cx + 12, cy + 10),
                    (cx + 44, cy + 10)], fill=RING_F, sw=1.1, close=True))
    # disc lifted: seating faces parted, flow through V-ports
    o.append(_poly([(cx - 12, cy - 34), (cx + 12, cy - 34), (cx + 14, cy - 22),
                    (cx - 14, cy - 22)], fill=DISC_F, sw=1.1, close=True))
    for sx in (-6, 6):
        o.append(_line(cx + sx - 3, cy - 22, cx + sx, cy - 12, 1.0, color=INK))
        o.append(_line(cx + sx + 3, cy - 22, cx + sx, cy - 12, 1.0, color=INK))
    o.append(_arrow(cx, cy - 8, cx, cy + 2, 1.2, color=BLUE))
    o.append(_txt(cx, cy + 40, "m\u1eb7t k\u00edn t\u00e1ch tr\u01b0\u1edbc "
                  "V-Port m\u1edf \u2192 ch\u1ed1ng x\u00f3i m\u00f2n",
                  6.8, color=GREY))
    o.append(_txt(cx, cy + 52, "seating faces part before ports open", 6.8,
                  color=GREY))
    o.append(_txt(320, 214, "(Pegler Hattersley) \u00b7 ch\u1ed7 k\u00edn "
                  "th\u00edch nghi cho nhi\u1ec7m v\u1ee5 kh\u00f4ng ch\u1ebf "
                  "m\u1ecbn", 7.4, color=GREY))
    return _fig(svg(w, h, "".join(o), "Globe seatings for throttling duty"),
                "H\u00ecnh 3-16 \u00b7 Ch\u1ed7 k\u00edn c\u1ee7a van "
                "c\u1ea7u th\u00edch nghi cho nhi\u1ec7m v\u1ee5 kh\u00f4ng "
                "ch\u1ebf (v\u1ebd l\u1ea1i): \u0111\u0129a kim v\u00e0 "
                "\u0111\u0129a v\u00e1y V-Port \u2014 m\u1eb7t k\u00edn t\u00e1ch "
                "kh\u1ecfi nhau tr\u01b0\u1edbc khi c\u00e1c c\u1ed5ng V m\u1edf, "
                "gi\u00fap b\u1ea3o v\u1ec7 ch\u1ed1ng x\u00f3i m\u00f2n.",
                "Figure 3-16 \u00b7 Seatings of globe valves adapted for "
                "throttling duty — redrawn: needle seat and V-port skirt "
                "(the seating faces separate before the V-ports open, "
                "protecting them against erosion). (Courtesy of Pegler "
                "Hattersley Limited.)",
                "Hai ch\u1ed7 k\u00edn kh\u00f4ng ch\u1ebf: kim, V-Port.",
                "Two throttling seatings: needle, V-port.")


# ------------------------------------------ Figures 3-17 … 3-19 (stuffing)
def _stuffing_panel(o, x0, y0, variant):
    """Basic stuffing-box section drawn into box at (x0, y0), 300x220."""
    cx = x0 + 150
    top = y0 + 26
    o.append(_txt(cx, y0 - 6, variant[0], 8.2, weight="bold"))
    # body walls (annular chamber between them)
    o.append(_rect(cx - 70, top, 30, 150, fill=BULB_F, sw=1.2))
    o.append(_rect(cx + 40, top, 30, 150, fill=BULB_F, sw=1.2))
    o.append(_line(cx - 40, top, cx - 40, top + 150, 1.2, color=INK))
    o.append(_line(cx + 40, top, cx + 40, top + 150, 1.2, color=INK))
    # stem
    o.append(_rect(cx - 11, top - 18, 22, 186, fill=DISC_F, sw=1.1))
    # packing column (below chamber top)
    pt, pb = top + 44, top + 128
    if variant[1] == "basic":
        o.append(_rect(cx - 40, pt, 80, pb - pt, fill=PACK_F, sw=1.1))
        o.append(_rect(cx - 46, pt - 10, 92, 10, fill=RING_F, sw=1.1))  # gland
    elif variant[1] == "condense":
        # condensing chamber at bottom: annulus + test plug
        o.append(_rect(cx - 40, pt, 80, pb - pt - 34, fill=PACK_F, sw=1.1))
        o.append(_rect(cx - 46, pt - 10, 92, 10, fill=RING_F, sw=1.1))
        o.append(_rect(cx - 40, pb - 30, 80, 26, fill="#eef2f8", sw=1.1))
        o.append(_line(cx - 70, pb - 16, cx - 84, pb - 16, 1.4, color=INK))
        o.append(_rect(cx - 90, pb - 20, 8, 8, fill=RING_F, sw=1.0))
        o.append(_txt(cx - 92, pb - 26, "test plug", 6.6, anchor="end",
                      color=GREY))
    else:  # lantern ring
        o.append(_rect(cx - 40, pt, 80, 34, fill=PACK_F, sw=1.1))
        o.append(_rect(cx - 40, pt + 34, 80, 22, fill="#e9e9e4", sw=1.1))
        o.append(_rect(cx - 40, pt + 56, 80, pb - pt - 56, fill=PACK_F,
                       sw=1.1))
        o.append(_rect(cx - 46, pt - 10, 92, 10, fill=RING_F, sw=1.1))
        o.append(_txt(cx + 46, pt + 45, "lantern ring", 6.6, anchor="start",
                      color=GREY))
    # back seat at chamber bottom
    o.append(_poly([(cx - 40, top + 150), (cx - 16, top + 150),
                    (cx - 16, top + 143), (cx - 40, top + 143)],
                   fill=RING_F, sw=1.0, close=True))
    return


@_reg3
def fig_vsh_3_17():
    return _stuffing_fig(
        17, ("H\u1ed9p \u0111\u00f3n c\u01a1 b\u1ea3n", "basic"),
        "Basic stuffing box with back seating",
        "H\u1ed9p \u0111\u00f3n c\u01a1 b\u1ea3n, c\u00f3 ch\u1ed7 k\u00edn "
        "ng\u01b0\u1ee3c (back seat)",
        "B\u1ed9 m\u00e1y \u0111\u00f3n c\u01a1 b\u1ea3n c\u00f3 back seat.")


def _stuffing_fig(num, variant, ten, tvi, aria):
    """One stuffing-box redraw, 640x250 canvas with legend column."""
    w, h = 560, 268
    o = [_defs()]
    _stuffing_panel(o, 20, 30, variant)
    # legend
    labels = [("gio\u0103ng n\u00e9n", "compression packing"),
              ("b\u1ed9 \u00e9p gio\u0103ng", "gland"),
              ("ch\u1ed7 k\u00edn ng\u01b0\u1ee3c (back seat)",
               "back seat \u2014 isolates the packing when fully open"),
              ("tr\u1ee5c n\u00e2ng", "rising stem")]
    if variant[1] == "condense":
        labels.append(("ng\u0103n ng\u01b0ng k\u00edn h\u00f3a",
                       "condensing chamber"))
    if variant[1] == "lantern":
        labels.append(("v\u00f2ng l\u1ed3ng \u0111\u00e0n (lantern ring)",
                       "lantern ring \u2014 4 uses (see text)"))
    for i, (vi, en) in enumerate(labels):
        yy = 56 + i * 34
        o.append(_circle(388, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(388, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(402, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(402, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_txt(476, 258, "Babcock-Persta.", 6.6, color=GREY))
    # markers on the drawing (canvas coords)
    cx, top = 170, 56
    pt = top + 44
    marks = [(cx, pt + (70 if variant[1] != "lantern" else 40), 1),
             (cx, pt - 5, 2),
             (cx, top + 146, 3),
             (cx, top + 8, 4)]
    for mx, my, n in marks:
        o.append(_circle(mx, my, 7.5, sw=1.2, color=INK))
        o.append(_txt(mx, my - 0.5, str(n), 8.0, weight="bold"))
    if variant[1] == "condense":
        o.append(_circle(cx, top + 112, 7.5, sw=1.2, color=INK))
        o.append(_txt(cx, top + 112.5, "5", 8.0, weight="bold"))
    if variant[1] == "lantern":
        o.append(_circle(cx - 52, pt + 45, 7.5, sw=1.2, color=INK))
        o.append(_txt(cx - 52, pt + 45.5, "5", 8.0, weight="bold"))
    return _fig(svg(w, h, "".join(o), ten),
                "H\u00ecnh 3-%d \u00b7 %s (v\u1ebd l\u1ea1i). Ngu\u1ed3n: "
                "Babcock-Persta Armaturen-Vertriebsgesellschaft mbH."
                % (num, tvi),
                "Figure 3-%d \u00b7 %s — redrawn. (Courtesy of Babcock-Persta "
                "Armaturen-Vertriebsgesellschaft mbH.)" % (num, ten),
                tvi, aria)


@_reg3
def fig_vsh_3_18():
    return _stuffing_fig(
        18, ("C\u00f3 ng\u0103n ng\u01b0ng k\u00edn h\u00f3a", "condense"),
        "Stuffing box with condensing chamber and test plug",
        "H\u1ed9p \u0111\u00f3n c\u00f3 ng\u0103n ng\u01b0ng k\u00edn "
        "h\u00f3a, k\u00e8m n\u1eafm th\u1eed \u00e1p su\u1ea5t",
        "H\u1ed9p \u0111\u00f3n c\u00f3 ng\u0103n k\u00edn h\u00f3a v\u00e0 "
        "n\u1eafm th\u1eed.")


@_reg3
def fig_vsh_3_19():
    return _stuffing_fig(
        19, ("C\u00f3 v\u00f2ng l\u1ed3ng \u0111\u00e0n", "lantern"),
        "Stuffing box with lantern ring between two packing sections",
        "H\u1ed9p \u0111\u00f3n c\u00f3 v\u00f2ng l\u1ed3ng \u0111\u00e0n "
        "gi\u1eefa hai \u0111o\u1ea1n gio\u0103ng",
        "H\u1ed9p \u0111\u00f3n c\u00f3 v\u00f2ng lantern gi\u1eefa hai "
        "\u0111o\u1ea1n gio\u0103ng.")


# ------------------------------------------- Figures 3-20 … 3-24 (piston)
def _piston_fig(num, kind, ten, tvi, extra_marks):
    """Piston valve redraw. kind: inbody | inbody_bal | drain | ramseal |
    onpiston. 640x360 canvas."""
    w, h = 560, 380
    o = [_defs()]
    ox, oy = 200, 250                     # seat plane on canvas
    ops = _globe_ops("standard", "bolted", "external", "packing", "none",
                     None, flow=False)
    if kind in ("inbody", "inbody_bal"):
        # bore walls from bonnet to bulb
        for sx in (-1, 1):
            ops.append(("line", sx * 16, -44, sx * 16, 24, 1.3, INK, ""))
        # seat packing blocks in the bore mouth; piston slides between
        for sx in (-1, 1):
            ops.append(("poly", [(sx * 16, 22), (sx * 9, 22), (sx * 9, -18),
                                 (sx * 16, -18)], PACK_F, 1.0, INK, "", True))
            ops.append(("poly", [(sx * 16, -28), (sx * 9, -28), (sx * 9, -46),
                                 (sx * 16, -46)], PACK_F, 1.0, INK, "", True))
            ops.append(("poly", [(sx * 16, -18), (sx * 9, -18), (sx * 9, -28),
                                 (sx * 16, -28)], "#e9e9e4", 1.0, INK, "",
                        True))          # lantern ring between the two
        plen = 128
        ops.append(("poly", [(-9, 22 - plen), (9, 22 - plen), (9, 12),
                             (-9, 12)], DISC_F, 1.2, INK, "", True))
        ops.append(("line", 0, 22 - plen, 0, -146, 2.4, INK, ""))
        if kind == "inbody_bal":
            ops.append(("line", -4, 22 - plen + 8, -4, 4, 1.0, INK, "3 2"))
            ops.append(("line", 4, 22 - plen + 8, 4, 4, 1.0, INK, "3 2"))
    elif kind == "ramseal":
        for sx in (-1, 1):
            ops.append(("line", sx * 16, -44, sx * 16, 30, 1.3, INK, ""))
        # shoulder in seat bore
        ops.append(("poly", [(-16, 30), (-20, 30), (-20, 36), (-16, 36)],
                    RING_F, 1.0, INK, "", True))
        ops.append(("poly", [(16, 30), (20, 30), (20, 36), (16, 36)],
                    RING_F, 1.0, INK, "", True))
        plen = 118
        ops.append(("poly", [(-12, 22 - plen), (12, 22 - plen), (12, 2),
                             (-12, 2)], DISC_F, 1.2, INK, "", True))
        ops.append(("poly", [(-12, 2), (12, 2), (12, 20), (-12, 20)],
                    PACK_F, 1.0, INK, "", True))          # packing on piston
        ops.append(("poly", [(-12, 20), (12, 20), (12, 26), (-12, 26)],
                    RING_F, 1.0, INK, "", True))          # compression ring
        ops.append(("line", 0, 22 - plen, 0, -146, 2.4, INK, ""))
    elif kind == "onpiston":
        for sx in (-1, 1):
            ops.append(("line", sx * 16, -44, sx * 16, 30, 1.3, INK, ""))
        plen = 112
        ops.append(("poly", [(-12, 22 - plen), (12, 22 - plen), (12, 4),
                             (-12, 4)], DISC_F, 1.2, INK, "", True))
        ops.append(("poly", [(-12, 4), (12, 4), (12, 22), (-12, 22)],
                    PACK_F, 1.0, INK, "", True))
        zz = [(12, 22)]
        for i in range(5):
            zz.append((12 - (i + 1) * 3.2, 22 - (2 * i + 1) * -0 + 0))
        # friction ring as spring zigzag under packing
        zz = []
        for i in range(6):
            yy = 22 + i * 3
            zz.append(((12 if i % 2 else 4), yy))
        ops.append(("poly", zz, "none", 1.1, INK, "", False))
        zz2 = []
        for i in range(6):
            yy = 22 + i * 3
            zz2.append(((-12 if i % 2 else -4), yy))
        ops.append(("poly", zz2, "none", 1.1, INK, "", False))
        ops.append(("line", 0, 22 - plen, 0, -146, 2.4, INK, ""))
    elif kind == "drain":
        # vessel plate at top; body below; packing in body near plate
        o.append(_rect(60, 96, 280, 12, fill="url(#h6)", sw=1.1))
        o.append(_txt(66, 88, "\u0111\u00e1y b\u00ecnh / vessel bottom",
                      7.4, anchor="start"))
        o.append(_poly([(ox - 34, 108), (ox + 34, 108), (ox + 34, 180),
                        (ox - 34, 180)], fill=BULB_F, sw=1.2, close=True))
        for sx in (-1, 1):
            o.append(_poly([(ox + sx * 16, 110), (ox + sx * 9, 110),
                            (ox + sx * 9, 148), (ox + sx * 16, 148)],
                           fill=PACK_F, sw=1.0, close=True))
        o.append(_line(ox - 16, 96, ox - 16, 180, 1.2, color=INK))
        o.append(_line(ox + 16, 96, ox + 16, 180, 1.2, color=INK))
        o.append(_poly([(ox - 9, 152), (ox + 9, 152), (ox + 9, 220),
                        (ox - 9, 220)], fill=DISC_F, sw=1.2, close=True))
        o.append(_line(ox, 220, ox, 250, 2.4, color=INK))
        o.append(_poly([(ox - 26, 250), (ox + 26, 250), (ox + 26, 288),
                        (ox - 26, 288)], fill="#efefe9", sw=1.2, close=True))
        o.append(_poly(_ell(ox, 298, 32, 8), "#e8e8e2", sw=1.2, close=True))
        o.append(_circle(ox, 298, 5, sw=1.1, color=INK))
        o.append(_line(ox, 84, ox, 62, 1.6, color=BLUE))
        o.append(_poly([(ox, 62), (ox - 3.5, 70), (ox + 3.5, 70)], fill=BLUE,
                       sw=0, close=True))
        _emit_legend(o, 402, extra_marks)
        o.append(_txt(476, 360, "Yarway Corporation." if num == 22 else "",
                      6.6, color=GREY))
        return _fig(svg(w, h, "".join(o), ten),
                    "H\u00ecnh 3-%d \u00b7 %s (v\u1ebd l\u1ea1i)." % (num, tvi),
                    "Figure 3-%d \u00b7 %s — redrawn." % (num, ten),
                    tvi, ten)
    # common render for non-drain kinds (ops local frame -> canvas offset)
    DX, DY = 200, 250
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=DX, dy=DY)
    a_y = DY + 76
    o2.append(_line(DX - 118, a_y, DX - 96, a_y, 1.6, color=BLUE))
    o2.append(_poly([(DX - 96, a_y), (DX - 104, a_y - 3.5),
                     (DX - 104, a_y + 3.5)], fill=BLUE, sw=0, close=True))
    o2.append(_line(DX, a_y - 60, DX, a_y - 84, 1.6, color=BLUE))
    o2.append(_poly([(DX, a_y - 84), (DX - 3.5, a_y - 76),
                     (DX + 3.5, a_y - 76)], fill=BLUE, sw=0, close=True))
    o2.append(_line(DX + 96, a_y, DX + 118, a_y, 1.6, color=BLUE))
    o2.append(_poly([(DX + 118, a_y), (DX + 110, a_y - 3.5),
                     (DX + 110, a_y + 3.5)], fill=BLUE, sw=0, close=True))
    _emit_legend(o2, 402, extra_marks)
    courtesy = {20: "Rich. Klinger AG.", 21: "Rich. Klinger AG.",
                23: "Fetterolf Corporation.", 24: "Rich. Klinger AG."}[num]
    o2.append(_txt(476, 360, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, "".join(o2), ten),
                "H\u00ecnh 3-%d \u00b7 %s (v\u1ebd l\u1ea1i). Ngu\u1ed3n: %s."
                % (num, tvi, courtesy),
                "Figure 3-%d \u00b7 %s — redrawn. (Courtesy of %s.)"
                % (num, ten, courtesy), tvi, ten)


def _emit_legend(o, x0, marks):
    """Numbered legend column; marks = [((vi,en), (canvas_x, canvas_y))]."""
    for i, ((vi, en), (mx, my)) in enumerate(marks):
        yy = 56 + i * 34
        o.append(_circle(x0, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(x0, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(x0 + 14, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(x0 + 14, yy + 6, en, 6.6, anchor="start", color=GREY))
        o.append(_circle(mx, my, 7.5, sw=1.2, color=INK))
        o.append(_txt(mx, my - 0.5, str(i + 1), 8.0, weight="bold"))


@_reg3
def fig_vsh_3_20():
    return _piston_fig(
        20, "inbody",
        "Piston valve, standard pattern, seat packing mounted in valve body, "
        "piston pressure unbalanced",
        "Van piston, ki\u1ec3u chu\u1ea9n, gio\u0103ng ch\u1ed7 k\u00edn g\u1eafn "
        "tr\u00ean th\u00e2n van, piston kh\u00f4ng c\u00e2n b\u1eb1ng \u00e1p",
        [(("gio\u0103ng ch\u1ed7 k\u00edn trong th\u00e2n",
           "seat packing in the valve body"), (212, 252)),
         (("v\u00f2ng l\u1ed3ng \u0111\u00e0n", "lantern ring between the two "
           "packing sections"), (212, 227)),
         (("piston \u0111\u01b0\u1ee3c \u00e9p k\u00edn qua n\u1eafp",
           "piston; bonnet acts as the gland"), (200, 190))])


@_reg3
def fig_vsh_3_21():
    return _piston_fig(
        21, "inbody_bal",
        "Piston valve, standard pattern, seat packing mounted in valve body, "
        "piston pressure balanced",
        "Van piston, ki\u1ec3u chu\u1ea9n, gio\u0103ng ch\u1ed7 k\u00edn g\u1eafn "
        "tr\u00ean th\u00e2n van, piston c\u00e2n b\u1eb1ng \u00e1p",
        [(("gio\u0103ng ch\u1ed7 k\u00edn trong th\u00e2n",
           "seat packing in the valve body"), (212, 252)),
         (("piston c\u00e2n b\u1eb1ng \u00e1p (k\u00eanh n\u1ed1i)",
           "pressure-balanced piston (equalising channel)"), (196, 210)),
         (("v\u00f2ng l\u1ed3ng \u0111\u00e0n", "lantern ring"), (212, 227))])


@_reg3
def fig_vsh_3_22():
    return _piston_fig(
        22, "drain",
        "Piston valve adapted for draining vessels, seat packing mounted in "
        "valve body",
        "Van piston d\u00f9ng x\u1ea3 b\u00ecnh ch\u1ee9a, gio\u0103ng "
        "ch\u1ed7 k\u00edn g\u1eafn tr\u00ean th\u00e2n van",
        [(("ch\u1ed7 k\u00edn s\u00e1t \u0111\u00e1y b\u00ecnh",
           "seat packing flush with vessel bottom"), (140, 102)),
         (("gio\u0103ng ch\u1ed7 k\u00edn trong th\u00e2n",
           "seat packing in the valve body"), (212, 130)),
         (("piston \u0111\u1ea9y l\u00ean \u0111\u00f3ng",
           "piston closes upward"), (200, 180))])


@_reg3
def fig_vsh_3_23():
    return _piston_fig(
        23, "ramseal",
        "Piston valve adapted for draining vessels, seat packing mounted on "
        "piston; the ram-seal principle",
        "Van piston d\u00f9ng x\u1ea3 b\u00ecnh ch\u1ee9a, gio\u0103ng "
        "ch\u1ed7 k\u00edn g\u1eafn tr\u00ean piston \u2014 nguy\u00ean t\u1eafc "
        "Ram-Seal",
        [(("gio\u0103ng g\u1eafn tr\u00ean \u0111\u1ea7u piston",
           "seat packing carried on the piston"), (222, 258)),
         (("v\u00f2ng n\u00e9n r\u1eddi", "loose compression ring"),
          (222, 276)),
         (("v\u00e1i d\u1eebng trong l\u1ed3ng ch\u1ed7 k\u00edn",
           "shoulder in the seat bore stops the ring"), (180, 283))])


@_reg3
def fig_vsh_3_24():
    return _piston_fig(
        24, "onpiston",
        "Piston valve, standard pattern, seat packing mounted on piston",
        "Van piston, ki\u1ec3u chu\u1ea9n, gio\u0103ng ch\u1ed7 k\u00edn "
        "g\u1eafn tr\u00ean piston",
        [(("gio\u0103ng g\u1eafn tr\u00ean piston", "seat packing on the "
           "piston"), (200, 265)),
         (("v\u00f2ng ma s\u00e1t l\u00e0m l\u00f2 xo",
           "friction ring acting as a spring"), (208, 278))])
