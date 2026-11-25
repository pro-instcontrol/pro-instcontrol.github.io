# -*- coding: utf-8 -*-
"""Vector redraws of Figures 20-1 to 20-5 in Baumann Chapter 20,
*Control Valve Primer*, 5th ed. — "Methods of Aerodynamic Valve Noise
Reduction".

Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` and is registered in
:data:`FIGS` through :func:`_reg`, mirroring ``build/cvpfig19.py``.

The drawings are genuine SVG primitives: sectional valve bodies are hatched,
the annular throttling teeth, cage slots, labyrinth grooves, stamped plates
and fluted disk are generated geometrically, and every flow path carries
arrows and engineering labels.  No raster images are embedded.  All text is
escaped; ×, −, √ and subscripts are literal Unicode; no CJK and no bare '&'
is emitted.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (GREY, INK, _circle, _fig, _line, _path, _poly,
                  _rect, _txt, svg)

FIGS = {}

BLUE = "#1f5f8b"
METAL = "#efe9dc"
STEEL = "#e6dfcf"
FLOW = "#dbe9f4"


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


def _arr(o, x1, y1, x2, y2, sw=1.25, color=BLUE, head=5.0):
    """A line with a filled triangular head (no marker defs, no id clashes)."""
    o.append(_line(x1, y1, x2, y2, sw=sw, color=color))
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 + head * math.cos(a + math.pi - 0.42),
          y2 + head * math.sin(a + math.pi - 0.42))
    p2 = (x2 + head * math.cos(a + math.pi + 0.42),
          y2 + head * math.sin(a + math.pi + 0.42))
    o.append(_poly([(x2, y2), p1, p2], fill=color, sw=0, close=True))


def _hatch_rect(o, x, y, w, h, step=7, color="#9a9a9a"):
    """Clipped 45-degree section hatching inside a rectangle."""
    for s in range(-int(h), int(w + h), step):
        u_lo, u_hi = max(0, s - w), min(h, s)
        if u_lo < u_hi:
            o.append(_line(x + s - u_lo, y + u_lo,
                           x + s - u_hi, y + u_hi, sw=0.55, color=color))


def _hdr(o, title, sub):
    o.append(_txt(340, 16, esc(title), 10.2, color=INK, weight="600"))
    o.append(_txt(340, 32, esc(sub), 7.6, color=GREY))


def _strip(o, vi, en):
    o.append(_txt(340, 360, esc(vi), 7.1, color=INK))
    o.append(_txt(340, 378, esc(en), 7.1, color=GREY))


def _zig(y0, y1, n, x_even, x_odd, mirror=False):
    """Alternating (tooth / root) points down a vertical serrated edge."""
    pts = []
    for i in range(2 * n + 1):
        x = x_even if i % 2 == 0 else x_odd
        if mirror:
            x = 680.0 - x
        pts.append((x, y0 + (y1 - y0) * i / (2.0 * n)))
    return pts


@_reg
def fig_f201():
    """Figure 20-1 — longitudinal section of an 11-step annular trim plug."""
    w, h = 680, 400
    o = []
    _hdr(o, "Figure 20-1 · Single-flow-area multistep plug",
         "Section · 11 zig-zag steps · 1.089:1 per step · −63.1 dB (28.3 dB saving)")

    o.append(_line(340, 54, 340, 332, sw=0.9, dash="5 4", color=GREY))

    # Static valve body and bonnet, shown in section.
    for x in (170, 432):
        o.append(_rect(x, 105, 78, 200, fill=METAL, sw=1.3))
        _hatch_rect(o, x, 105, 78, 200)
    for x in (250, 380):
        o.append(_rect(x, 76, 50, 64, fill=METAL, sw=1.2))
        _hatch_rect(o, x, 76, 50, 64, step=6)
    for x in (250, 374):
        o.append(_rect(x, 276, 55, 29, fill=METAL, sw=1.2))
        _hatch_rect(o, x, 276, 55, 29, step=6)

    # Stem and its central guide.
    o.append(_rect(334, 55, 12, 86, fill="#d8d2c4", sw=1.2))

    # Serrated annular seat and plug: 11 teeth on each side.
    y0, y1, n = 140, 276, 11
    cage_l = _zig(y0, y1, n, 312, 300)
    cage_r = _zig(y0, y1, n, 312, 300, mirror=True)
    plug_l = _zig(y0, y1, n, 320, 308)
    plug_r = _zig(y0, y1, n, 320, 308, mirror=True)

    o.append(_poly([(248, y0)] + cage_l + [(248, y1)],
                   fill=STEEL, sw=1.2, close=True))
    o.append(_poly([(432, y0)] + cage_r + [(432, y1)],
                   fill=STEEL, sw=1.2, close=True))
    o.append(_poly(plug_l + [(360, y1)] + list(reversed(plug_r)),
                   fill=METAL, sw=1.3, close=True))

    # Highlight the single annular flow area: it widens toward the outlet.
    o.append(_poly(plug_l + list(reversed(cage_l)),
                   fill=FLOW, sw=0.8, close=True))
    o.append(_poly(plug_r + list(reversed(cage_r)),
                   fill=FLOW, sw=0.8, close=True))

    # Flow through the teeth, then out through the two outlet legs.
    for yy in (164, 189, 214, 239):
        _arr(o, 316, yy, 316, yy + 7, sw=1.0, head=4.0)
        _arr(o, 364, yy, 364, yy + 7, sw=1.0, head=4.0)
    _arr(o, 248, 98, 294, 124, sw=1.3)
    _arr(o, 294, 124, 306, 152, sw=1.2)
    _arr(o, 326, 306, 326, 338, sw=1.3)
    _arr(o, 354, 306, 354, 338, sw=1.3)

    # Leaders and labels, kept clear of the hatched metal.
    o.append(_txt(150, 105, esc("INLET"), 8.2, anchor="end", color=INK))
    o.append(_line(154, 104, 248, 106, sw=0.8, color=GREY))
    o.append(_txt(150, 250, esc("WIDENING ANNULAR GAP"), 8.0,
                  anchor="end", color=INK))
    o.append(_line(154, 249, 300, 252, sw=0.8, color=GREY))
    o.append(_txt(150, 318, esc("OUTLET"), 8.2, anchor="end", color=INK))
    o.append(_line(154, 317, 310, 322, sw=0.8, color=GREY))
    o.append(_txt(530, 62, esc("STEM"), 8.2, anchor="start", color=INK))
    o.append(_line(526, 61, 348, 62, sw=0.8, color=GREY))
    o.append(_txt(530, 150, esc("11 THROTTLING STEPS"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(526, 149, 386, 176, sw=0.8, color=GREY))

    _strip(o,
           "Hình 20-1 · Van cắm đa cấp, một diện tích chảy — 11 bước tiết lưu và khe hở hình khuyên rộng dần.",
           "Figure 20-1 · Single-flow-area multistep plug — 11 throttling steps and a widening annular gap.")
    title = "Baumann Figure 20-1: single-flow-area multistep valve plug in section"
    return _fig(svg(w, h, "".join(o), esc(title)),
                "Hình 20-1 · Van cắm đa cấp, một diện tích chảy — 11 bước tiết lưu và khe hở hình khuyên rộng dần.",
                "Figure 20-1 · Single-flow-area multistep plug — 11 throttling steps and a widening annular gap.",
                "Mặt cắt dọc van: thân van, thân cắm, đường chảy hình khuyên ngoằn ngoèo với 11 bước tiết lưu, khe hở rộng dần về phía dưới và mũi tên chảy vào rồi ra.",
                "Longitudinal valve section: body, stem, plug and a zig-zag annular flow path with 11 throttling steps, the gap widening downward, with inlet and outlet flow arrows.")


@_reg
def fig_f202():
    """Figure 20-2 — multi-orifice cage ring (top view) and slotted cage."""
    w, h = 680, 400
    o = []
    _hdr(o, "Figure 20-2 · Multi-orifice cage trim",
         "Top and side views · n₀ = 16 parallel ports · Fd = 0.25 · peak frequency ×4")

    # ---- top view: annular cage ring with radial rectangular jets ----
    cx, cy, ro, ri = 180, 180, 92, 55
    o.append(_circle(cx, cy, ro, fill=METAL, sw=1.4))
    o.append(_circle(cx, cy, ri, fill="#ffffff", sw=1.2))
    for k in range(24):
        a = 2 * math.pi * k / 24.0
        hw = 0.055
        pts = []
        for r, ang in ((ri + 2, a - hw), (ro - 2, a - hw),
                       (ro - 2, a + hw), (ri + 2, a + hw)):
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        o.append(_poly(pts, fill="#ffffff", sw=0.8, close=True))
    for dx, dy in ((-9, -6), (4, -10), (11, 2), (-4, 9)):
        o.append(_line(cx + dx, cy + dy, cx + dx + 7, cy + dy - 5,
                       sw=0.9, color=GREY))
    for p1, p2 in (((92, 118), (70, 146)), ((106, 258), (136, 274)),
                   ((252, 258), (278, 240)), ((266, 118), (272, 92))):
        _arr(o, p1[0], p1[1], p2[0], p2[1], sw=1.1, head=4.6)
    o.append(_txt(180, 62, esc("TOP VIEW · CAGE RING"), 8.6,
                  color=INK, weight="600"))
    o.append(_txt(180, 302, esc("RECTANGULAR JETS"), 8.0, color=INK))
    _arr(o, 180, 294, 226, 256, sw=0.9, head=4.0)

    # ---- side view: slotted cage surrounding the plug ----
    o.append(_line(470, 146, 470, 312, sw=0.8, dash="5 4", color=GREY))
    o.append(_path("M420 190 Q470 150 520 190 Z", fill=METAL, sw=1.3))
    o.append(_rect(392, 190, 156, 110, fill=METAL, sw=1.3))
    for x, ht in zip((406, 431, 456, 481, 506, 531), (70, 80, 90, 90, 80, 70)):
        o.append(_rect(x, 294 - ht, 10, ht, fill="#ffffff", sw=0.8))
    _arr(o, 352, 300, 386, 272, sw=1.2)
    _arr(o, 588, 300, 554, 272, sw=1.2)
    _arr(o, 461, 210, 461, 246, sw=1.0, head=4.2)
    _arr(o, 495, 210, 495, 246, sw=1.0, head=4.2)
    o.append(_txt(470, 130, esc("SIDE VIEW · SLOTTED CAGE"), 8.6,
                  color=INK, weight="600"))
    o.append(_txt(600, 152, esc("VALVE PLUG"), 8.0, anchor="start", color=INK))
    o.append(_line(596, 151, 512, 168, sw=0.8, color=GREY))
    o.append(_txt(600, 222, esc("SLOTTED CAGE"), 8.0, anchor="start", color=INK))
    o.append(_line(596, 221, 548, 236, sw=0.8, color=GREY))

    _strip(o,
           "Hình 20-2 · Lồng tiết lưu nhiều lỗ — tiết lưu một cấp qua nhiều đường song song.",
           "Figure 20-2 · Multi-orifice cage trim — single-stage throttling through many parallel passages.")
    title = "Baumann Figure 20-2: multi-orifice cage trim, top and side views"
    return _fig(svg(w, h, "".join(o), esc(title)),
                "Hình 20-2 · Lồng tiết lưu nhiều lỗ — tiết lưu một cấp qua nhiều đường song song.",
                "Figure 20-2 · Multi-orifice cage trim — single-stage throttling through many parallel passages.",
                "Nhìn từ trên: vòng lồng có các khe hở tia chữ nhật xuyên tâm; nhìn bên: lồng có khe xung quanh nút van, với mũi tên chảy vào và ra.",
                "Top view of a cage ring with rectangular radial jet slots; side view of a slotted cage around a valve plug, with flow arrows entering and leaving.")


@_reg
def fig_f203():
    """Figure 20-3 — circular labyrinth cage insert with four grooved sectors."""
    w, h = 680, 400
    o = []
    _hdr(o, "Figure 20-3 · Labyrinth-type cage insert",
         "Four grooved sectors · multistep and multipath · reductions up to 30 dB")

    cx, cy = 250, 190
    o.append(_circle(cx, cy, 118, fill=METAL, sw=1.4))
    o.append(_circle(cx, cy, 106, fill="#ffffff", sw=1.1))

    # Four dark sectors carrying white serpentine grooves.
    for deg in (-45, -135, 135, 45):
        a0 = math.radians(deg - 27)
        a1 = math.radians(deg + 27)
        pts = []
        for i in range(13):
            a = a0 + (a1 - a0) * i / 12.0
            pts.append((cx + 104 * math.cos(a), cy + 104 * math.sin(a)))
        for i in range(12, -1, -1):
            a = a0 + (a1 - a0) * i / 12.0
            pts.append((cx + 45 * math.cos(a), cy + 45 * math.sin(a)))
        o.append(_poly(pts, fill="#3b3b3b", sw=0.8, close=True))

        groove = []
        for k in range(6):
            r = 52 + k * 9.0
            aa, bb = (a0 + 0.06, a1 - 0.06) if k % 2 == 0 else (a1 - 0.06, a0 + 0.06)
            groove.append((cx + r * math.cos(aa), cy + r * math.sin(aa)))
            groove.append((cx + r * math.cos(bb), cy + r * math.sin(bb)))
        o.append(_poly(groove, sw=3.1, color="#ffffff"))

        ax, ay = cx + 108 * math.cos(math.radians(deg)), cy + 108 * math.sin(math.radians(deg))
        bx, by = cx + 140 * math.cos(math.radians(deg)), cy + 140 * math.sin(math.radians(deg))
        _arr(o, ax, ay, bx, by, sw=1.2, head=5.0)

    # Central plug with its characteristic diagonal marks.
    o.append(_circle(cx, cy, 42, fill="#ffffff", sw=1.3))
    for dx, dy in ((-16, -8), (-4, -14), (10, -6), (-10, 4), (5, 8)):
        o.append(_line(cx + dx, cy + dy, cx + dx + 8, cy + dy - 5,
                       sw=0.9, color=GREY))
    o.append(_txt(cx, cy + 27, esc("VALVE PLUG"), 6.6, color=INK))

    o.append(_txt(470, 130, esc("GROOVED LABYRINTH"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(466, 129, 336, 142, sw=0.8, color=GREY))
    o.append(_txt(470, 165, esc("MULTIPATH CHANNELS"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(466, 164, 340, 176, sw=0.8, color=GREY))
    o.append(_txt(470, 230, esc("OUTWARD JETS"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(466, 229, 344, 236, sw=0.8, color=GREY))
    _strip(o,
           "Hình 20-3 · Lồng dạng mê cung — các kênh rãnh xếp chồng, nhiều cấp và nhiều đường chảy.",
           "Figure 20-3 · Labyrinth-type cage insert — stacked multipath grooved channels.")
    title = "Baumann Figure 20-3: labyrinth cage insert with four grooved sectors"
    return _fig(svg(w, h, "".join(o), esc(title)),
                "Hình 20-3 · Lồng dạng mê cung — các kênh rãnh xếp chồng, nhiều cấp và nhiều đường chảy.",
                "Figure 20-3 · Labyrinth-type cage insert — stacked multipath grooved channels.",
                "Vòng lồng tròn với bốn cung có rãnh ngoằn ngoèo quanh nút van ở giữa và bốn mũi tên chảy hướng ra ngoài.",
                "Circular cage insert with four grooved labyrinth sectors around a central valve plug and four outward flow arrows.")


@_reg
def fig_f204():
    """Figure 20-4 — perspective stack of identical laser-cut plates."""
    w, h = 680, 400
    o = []
    _hdr(o, "Figure 20-4 · Two-stage multiarea trim",
         "Streamlined inlet and abrupt larger outlet · 6:1 area ratio · overall ratio up to 8:1")

    xL, xR = 110, 420
    for k in range(6):
        yL, yR, t = 275 - k * 27, 225 - k * 27, 8
        o.append(_poly([(xL, yL), (xR, yR), (xR, yR + t), (xL, yL + t)],
                       fill=METAL, sw=1.15, close=True))
        for i in range(5):
            x = 140 + i * 22
            yy = yL + (yR - yL) * (x - xL) / (xR - xL)
            o.append(_rect(x, yy - 2.5, 10, 4, fill="#ffffff", sw=0.6))
        for i in range(3):
            x = 350 + i * 20
            yy = yL + (yR - yL) * (x - xL) / (xR - xL)
            o.append(_rect(x, yy - 4, 16, 9, fill="#ffffff", sw=0.7))

    for yy in (175, 205, 235):
        _arr(o, 425, yy, 476, yy, sw=1.2, head=5.0)

    o.append(_txt(70, 268, esc("INLET"), 8.2, anchor="start", color=INK))
    o.append(_line(112, 265, 142, 252, sw=0.8, color=GREY))
    o.append(_txt(490, 205, esc("OUTLET"), 8.2, anchor="start", color=INK))
    o.append(_line(486, 204, 478, 205, sw=0.8, color=GREY))
    o.append(_txt(470, 110, esc("STREAMLINED INLET PASSAGES"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(466, 109, 214, 185, sw=0.8, color=GREY))
    o.append(_txt(470, 135, esc("ABRUPT LARGER-AREA OUTLETS"), 8.0,
                  anchor="start", color=INK))
    o.append(_line(466, 134, 372, 193, sw=0.8, color=GREY))
    _strip(o,
           "Hình 20-4 · Bộ lọc nhiều cấp hai giai đoạn — các tấm cắt laser giống hệt nhau.",
           "Figure 20-4 · Two-stage multiarea trim — identical laser-cut plates.")
    title = "Baumann Figure 20-4: two-stage multiarea trim of identical stamped plates"
    return _fig(svg(w, h, "".join(o), esc(title)),
                "Hình 20-4 · Bộ lọc nhiều cấp hai giai đoạn — các tấm cắt laser giống hệt nhau.",
                "Figure 20-4 · Two-stage multiarea trim — identical laser-cut plates.",
                "Chồng các tấm dập giống hệt nhau theo phối cảnh: lối vào mảnh dần tạo tia siêu thanh, lối ra đột ngột diện tích lớn hơn, có nhãn vào và ra.",
                "Perspective stack of identical stamped plates: streamlined inlet passages make supersonic jets, abrupt larger-area outlets keep flow subsonic, with inlet and outlet labels.")


@_reg
def fig_f205():
    """Figure 20-5 — fluted butterfly valve plus multistage restrictor."""
    w, h = 680, 400
    o = []
    _hdr(o, "Figure 20-5 · Fluted butterfly valve with multistage restrictor",
         "Valve ratio 1.1–1.5 at design flow · static plate takes the rest · about 20 dB")

    # Pipe centreline and the three pipe sections.
    o.append(_line(40, 190, 640, 190, sw=0.8, dash="6 5", color=GREY))
    for x, y, ww in ((40, 160, 110), (40, 220, 110), (150, 120, 100),
                     (150, 220, 100), (330, 135, 310), (330, 235, 310)):
        o.append(_rect(x, y, ww, 10, fill=METAL, sw=1.2))
        _hatch_rect(o, x, y, ww, 10, step=7)
    o.append(_poly([(250, 160), (330, 135), (330, 145), (250, 170)],
                   fill=METAL, sw=1.1, close=True))
    o.append(_poly([(250, 220), (330, 245), (330, 235), (250, 210)],
                   fill=METAL, sw=1.1, close=True))
    o.append(_rect(246, 118, 8, 42, fill=METAL, sw=1.1))

    # Fluted butterfly disk, tilted in the flow.
    disk = []
    rot = math.radians(-34)
    for i in range(80):
        t = 2 * math.pi * i / 80.0
        r = 33 * (1 + 0.11 * math.cos(8 * t))
        ux, uy = r * math.cos(t), r * math.sin(t) * 0.58
        disk.append((200 + ux * math.cos(rot) - uy * math.sin(rot),
                     190 + ux * math.sin(rot) + uy * math.cos(rot)))
    o.append(_poly(disk, fill="#dcd6c8", sw=1.2, close=True))

    # Static multistage restrictor: a stack of perforated plates.
    for x in (380, 416, 452):
        o.append(_rect(x, 145, 9, 90, fill=STEEL, sw=1.1))
        _hatch_rect(o, x, 145, 9, 90, step=6)
        o.append(_rect(x + 1, 172, 7, 36, fill="#ffffff", sw=0.8))
    for p1, p2 in (((477, 179), (556, 179)), ((477, 190), (568, 190)),
                   ((477, 201), (556, 201))):
        _arr(o, p1[0], p1[1], p2[0], p2[1], sw=1.15, head=5.0)

    _arr(o, 52, 190, 106, 190, sw=1.3, head=5.4)
    o.append(_txt(50, 148, esc("INLET FLOW"), 8.0, anchor="start", color=INK))
    o.append(_txt(200, 100, esc("FLUTED DISK"), 8.2,
                  color=INK, weight="600"))
    o.append(_line(200, 107, 206, 162, sw=0.8, color=GREY))
    o.append(_txt(452, 108, esc("MULTISTAGE RESTRICTOR"), 8.2,
                  color=INK, weight="600"))
    o.append(_line(452, 115, 430, 144, sw=0.8, color=GREY))
    o.append(_txt(452, 292, esc("STATIC PLATE STACK"), 8.0, color=INK))
    o.append(_line(452, 284, 440, 236, sw=0.8, color=GREY))
    o.append(_txt(600, 268, esc("OUTLET"), 8.2, anchor="start", color=INK))
    o.append(_line(596, 267, 566, 206, sw=0.8, color=GREY))

    _strip(o,
           "Hình 20-5 · Van bướm cánh gờ kết hợp bộ hạn chế dòng nhiều cấp.",
           "Figure 20-5 · Fluted butterfly valve with a multistage fluid restrictor.")
    title = "Baumann Figure 20-5: fluted butterfly valve and multistage fluid restrictor"
    return _fig(svg(w, h, "".join(o), esc(title)),
                "Hình 20-5 · Van bướm cánh gờ kết hợp bộ hạn chế dòng nhiều cấp.",
                "Figure 20-5 · Fluted butterfly valve with a multistage fluid restrictor.",
                "Đường ống có van bướm đĩa gờ nghiêng, đoạn loe dần và chồng tấm hạn chế tĩnh ở phía sau; mũi tên chảy từ trái sang phải.",
                "Pipe with a fluted butterfly disk, an expanding transition and a downstream stack of static restrictor plates; flow arrows run left to right.")
