# -*- coding: utf-8 -*-
"""Vector figures for Chapter 2 of Book 9 (PPIC): "Advanced Measuring
(Instrumentation) Methods for Nuclear Installations: A Review".

Seven source figures are redrawn as clean vectors, preserving the topology,
layers, nodes, arrows and labels of the originals:

  Figure 2.1 (source p. 31) - MMGAS detector cross-section.
  Figure 2.2 (source p. 32) - ATR core cross-section irradiation locations.
  Figure 2.3 (source p. 35) - optical network for polarization-diverse
                              Rayleigh backscatter measurement.
  Figure 2.4 (source p. 38) - multipass MPBR of fuel circulation.
  Figure 2.5 (source p. 41) - pressurized water Cherenkov detector.
  Figure 2.6 (source p. 42) - probabilistic neural network.
  Figure 2.7 (source p. 43) - functional structure of ESMADP.

Every function returns the standard 5-tuple ``(svg, caption_vi, caption_en,
aria_vi, aria_en)`` through ``_fig()``.  All SVG text is XML-escaped via
``esc()``/``T()``; captions and aria text contain no ampersands and no CJK.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path,
                  _poly, _rect, _txt, svg)

FIGS = {}

# vfig's rectangle primitive names the outline "stroke", while its other
# primitives use "color".  This adapter lets every shape use "color".
_vfig_rect = _rect


def _rect(x, y, w, h, fill="#fff", sw=1.1, dash="", color=None, stroke=None):
    return _vfig_rect(x, y, w, h, fill=fill, sw=sw, dash=dash,
                      stroke=stroke or color)


def _reg(f):
    # Register the evaluated 5-tuple: `fig(num, key)` consumes a fresh tuple,
    # while the XML validation import checks every value stored in FIGS.
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


# Local palette - every shape gets an explicit colour.
NAVY = "#2f3a8f"
CREAM = "#f4e7c8"
LIME = "#a6cf14"
ICE = "#d6ecf7"
CYAN = "#cfe8e8"
TEAL = "#0aa197"
STEEL = "#c8d2d8"
FUEL = "#909090"
CONN = "#9aa0a6"
PIPE = "#6fa8c8"
PaleArrow = "#8fc7d9"


def _rrect(x, y, w, h, r, fill, stroke=INK, sw=1.2):
    """Rounded rectangle drawn with an explicit rx."""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" '
            'stroke="%s" stroke-width="%s"/>'
            % (x, y, w, h, r, fill, stroke, sw))


def _dot(cx, cy, r=5, fill=INK):
    return _circle(cx, cy, r, fill=fill, sw=0, color=fill)


def _tri(tipx, tipy, b1x, b1y, b2x, b2y, fill):
    """A solid triangle, used when an arrowhead must match a coloured line."""
    return _poly([(tipx, tipy), (b1x, b1y), (b2x, b2y)],
                 fill=fill, sw=0, color=fill, close=True)


# ---------------------------------------------------------------------------
@_reg
def fig_f21():
    """Figure 2.1 (source p. 31) - MMGAS detector cross-section."""
    w, h = 680, 320
    o = [_defs()]

    # Supporting blocks above the anode strip.
    o.append(_rect(150, 102, 36, 24, fill=NAVY, sw=1.2, color=NAVY))
    o.append(_rect(494, 102, 36, 24, fill=NAVY, sw=1.2, color=NAVY))
    # Anode pad strip.
    o.append(_rect(150, 126, 380, 18, fill="#000000", sw=1.0, color="#000000"))
    # Row of narrow beige Kapton cells.
    for i in range(26):
        o.append(_rect(152 + i * 14.5, 146, 12.5, 30,
                       fill=CREAM, sw=0.7, color="#7a6a45"))
    # Micromesh: horizontal green strip across the full width.
    o.append(_rect(140, 176, 400, 12, fill=LIME, sw=1.1, color="#6b8b06"))
    # Chamber: side supports plus the open white interior.
    o.append(_rect(150, 188, 36, 70, fill=NAVY, sw=1.2, color=NAVY))
    o.append(_rect(494, 188, 36, 70, fill=NAVY, sw=1.2, color=NAVY))
    o.append(_rect(186, 188, 308, 70, fill="#ffffff", sw=1.2, color=INK))
    # U235 fission strip and the bottom anode block.
    o.append(_rect(252, 242, 176, 5, fill=RED, sw=0, color=RED))
    o.append(_rect(150, 258, 380, 14, fill="#000000", sw=1.0, color="#000000"))

    # Leaders and labels.
    o.append(_arrow(268, 96, 306, 126, sw=0.9))
    o.append(T(248, 90, "Anode pad", 9.0, anchor="middle", color=INK))
    o.append(_arrow(486, 96, 516, 104, sw=0.9))
    o.append(T(478, 90, "Plexiglas", 9.0, anchor="middle", color=INK))
    o.append(_arrow(308, 202, 334, 180, sw=0.9))
    o.append(T(266, 206, "Micromesh", 9.0, anchor="middle", color=INK))
    o.append(_arrow(430, 196, 446, 180, sw=0.9))
    o.append(T(426, 206, "Kapton pillar", 9.0, anchor="middle", color=INK))
    o.append(_arrow(452, 234, 496, 232, sw=0.9))
    o.append(T(408, 238, "Drift electrode", 9.0, anchor="middle", color=INK))
    o.append(T(340, 236, "U235", 9.0, anchor="middle", color=RED,
               weight="600"))

    s = svg(w, h, "".join(o),
            esc("Figure 2.1 - Detail of the MMGAS detectors"))
    return _fig(s,
                "Hình 2.1 · Chi tiết của đầu dò MMGAS.",
                "Figure 2.1 · Detail of the MMGAS detectors.",
                "Sơ đồ cắt ngang đầu dò MMGAS với cực anode, tấm Plexiglas, micromesh, cột Kapton, điện cực trôi và thanh U235",
                "Cross-section of the MMGAS detector showing the anode pad, Plexiglas, micromesh, Kapton pillar, drift electrode and U235 bar")


# ---------------------------------------------------------------------------
@_reg
def fig_f22():
    """Figure 2.2 (source p. 32) - ATR core cross-section."""
    w, h = 680, 420
    o = [_defs()]

    # Reactor vessel and the two gridded side blocks.
    o.append(_circle(340, 210, 150, fill=ICE, sw=1.6, color=INK))
    for bx in (130, 490):
        o.append(_rect(bx, 168, 60, 84, fill=ICE, sw=1.3, color=INK))
        for gy in (189, 210, 231):
            o.append(_line(bx, gy, bx + 60, gy, sw=0.7, color="#5f7f92"))
        for gx in (bx + 20, bx + 40):
            o.append(_line(gx, 168, gx, 252, sw=0.7, color="#5f7f92"))

    # Eight circular fuel assemblies in a ring.
    for ax, ay in ((270, 130), (340, 130), (410, 130),
                   (270, 210), (410, 210),
                   (270, 290), (340, 290), (410, 290)):
        o.append(_circle(ax, ay, 24, fill=FUEL, sw=1.2, color=INK))

    # Central capsule irradiation tank with its red core.
    o.append(_circle(340, 210, 31, fill=TEAL, sw=1.4, color=INK))
    o.append(_circle(340, 210, 12, fill=RED, sw=1.2, color=INK))

    # Four black position markers at north, east, south, west.
    for px, py in ((340, 60), (490, 210), (340, 360), (190, 210)):
        o.append(_circle(px, py, 8, fill="#000000", sw=0, color="#000000"))

    # Leaders and labels.
    o.append(_arrow(392, 48, 346, 58, sw=0.9))
    o.append(T(400, 42, "Positions", 9.0, anchor="start", color=INK))
    o.append(_arrow(504, 114, 428, 128, sw=0.9))
    o.append(T(510, 108, "Control drums", 9.0, anchor="start", color=INK))
    o.append(_arrow(552, 152, 522, 180, sw=0.9))
    o.append(T(556, 146, "Capsule irradiation tank", 8.5,
               anchor="start", color=INK))
    o.append(_arrow(246, 174, 276, 194, sw=0.9))
    o.append(T(220, 168, "Fuel assembly", 9.0, anchor="middle", color=INK))
    o.append(_arrow(296, 322, 324, 238, sw=0.9))
    o.append(T(250, 332, "In-pile tubes", 9.0, anchor="middle", color=INK))

    s = svg(w, h, "".join(o),
            esc("Figure 2.2 - The irradiation locations of ATR core cross-section"))
    return _fig(s,
                "Hình 2.2 · Vị trí chiếu xạ trên mặt cắt lõi ATR.",
                "Figure 2.2 · The irradiation locations of ATR core cross-section.",
                "Mặt cắt lõi ATR với tám cụm nhiên liệu, bình chiếu xạ trung tâm, khối điều khiển hai bên và bốn vị trí đánh dấu",
                "ATR core cross-section with eight fuel assemblies, a central capsule tank, side control blocks and four marked positions")


# ---------------------------------------------------------------------------
@_reg
def fig_f23():
    """Figure 2.3 (source p. 35) - polarization-diverse Rayleigh network."""
    w, h = 680, 330
    o = [_defs()]

    # Red fibre: the V joining the two couplers to the heat-applied stem.
    o.append(_line(344, 130, 292, 190, sw=1.5, color=RED))
    o.append(_line(344, 250, 292, 190, sw=1.5, color=RED))
    o.append(_line(292, 190, 238, 190, sw=1.7, color=RED))
    o.append(_tri(236, 190, 248, 185, 248, 195, RED))

    # Two stacked couplers with the polarization controller between them.
    o.append(_line(360, 148, 360, 172, sw=1.5, color=RED))
    o.append(_ellipse(360, 190, 7, 18, fill=ICE, sw=1.1, color=INK))
    o.append(_line(360, 208, 360, 232, sw=1.5, color=RED))
    o.append(_circle(360, 130, 17, fill=ICE, sw=1.2, color=INK))
    o.append(_circle(360, 250, 17, fill=ICE, sw=1.2, color=INK))

    # Upper branch: beam splitter with P and S outputs.
    o.append(_line(360, 113, 360, 72, sw=1.5, color=RED))
    o.append(_line(360, 72, 432, 72, sw=1.5, color=RED))
    o.append(_rect(432, 62, 76, 22, fill=ICE, sw=1.2, color=INK))
    o.append(_line(436, 84, 504, 64, sw=1.0, color=BLUE))
    o.append(_line(508, 73, 550, 73, sw=1.4, color=RED))
    o.append(_tri(552, 73, 542, 69, 542, 77, RED))
    o.append(_line(470, 84, 470, 112, sw=1.4, color=RED))
    o.append(_tri(470, 114, 466, 104, 474, 104, RED))

    # Lower branch: small connector and the green TSL module.
    o.append(_line(360, 267, 360, 294, sw=1.5, color=RED))
    o.append(_line(360, 294, 420, 294, sw=1.5, color=RED))
    o.append(_rect(420, 287, 16, 14, fill=STEEL, sw=1.0, color=INK))
    o.append(_rect(436, 282, 56, 24, fill="#4f9d32", sw=1.2, color="#2e6b1c"))

    # Labels.
    o.append(T(250, 176, "Heat applied", 9.0, anchor="middle", color=INK))
    o.append(T(386, 134, "Coupler", 9.0, anchor="start", color=INK))
    o.append(T(386, 194, "Polariz controller", 9.0, anchor="start",
               color=INK))
    o.append(T(470, 52, "Polariz beam splitter", 9.0, anchor="middle",
               color=INK))
    o.append(T(560, 76, "P", 9.5, anchor="middle", color=INK))
    o.append(T(480, 114, "S", 9.5, anchor="middle", color=INK))
    o.append(T(464, 298, "TSL", 9.0, anchor="middle", color="#ffffff",
               weight="600"))

    s = svg(w, h, "".join(o),
            esc("Figure 2.3 - Optical network applied for polarization diverse measurement of Rayleigh backscatter"))
    return _fig(s,
                "Hình 2.3 · Mạng quang dùng cho đo tán xạ Rayleigh phân cực đa dạng.",
                "Figure 2.3 · Optical network applied for polarization diverse measurement of Rayleigh backscatter.",
                "Mạng quang gồm hai bộ ghép, bộ điều khiển phân cực, bộ tách chùm tia và mô-đun TSL",
                "Optical network with two couplers, a polarization controller, a beam splitter and a TSL module")


# ---------------------------------------------------------------------------
@_reg
def fig_f24():
    """Figure 2.4 (source p. 38) - multipass MPBR of fuel circulation."""
    w, h = 680, 340
    o = [_defs()]

    # Conical vessel with a domed mouth and fuel pellets.
    o.append(_path("M160,104 Q230,76 300,104 L228,272 Z",
                   fill="#ffffff", sw=1.5, color=INK))
    for px, py in ((190, 112), (214, 108), (240, 110), (268, 114), (288, 118),
                   (202, 132), (228, 130), (256, 134), (278, 138),
                   (214, 152), (244, 150), (266, 155), (226, 172),
                   (250, 174), (232, 194), (246, 196), (236, 216), (228, 236)):
        o.append(_dot(px, py, 5))

    # Two light-blue rounded boxes.
    o.append(_rrect(380, 96, 200, 44, 8, ICE, INK, 1.4))
    o.append(T(480, 123, "Fuel circulation and reload", 10.0,
               anchor="middle", color=INK))
    o.append(_rrect(380, 232, 200, 44, 8, ICE, INK, 1.4))
    o.append(T(480, 259, "Burn monitor system", 10.0,
               anchor="middle", color=INK))

    # Circulation loop. Arrowheads follow the source figure: the upper run
    # points left into the cone, the lower run points right into the monitor,
    # and the vertical run points up back to the reload box.
    o.append(_arrow(380, 118, 304, 112, sw=2.2, color=PIPE))
    o.append(_dot(384, 118, 5))
    o.append(_dot(306, 112, 5))
    o.append(_arrow(480, 232, 480, 142, sw=2.2, color=PIPE))
    o.append(_dot(480, 236, 5))
    o.append(_dot(480, 138, 5))
    o.append(_line(228, 272, 228, 286, sw=2.2, color=PIPE))
    o.append(_arrow(228, 286, 378, 258, sw=2.2, color=PIPE))
    o.append(_dot(228, 272, 5))
    o.append(_dot(380, 258, 5))

    # Diagonal fuel-discharge outlet.
    o.append(_arrow(580, 246, 632, 210, sw=2.0, color=PIPE))
    o.append(T(612, 202, "Fuel discharge", 9.0, anchor="start", color=INK))

    s = svg(w, h, "".join(o),
            esc("Figure 2.4 - The multipass MPBR of fuel circulation"))
    return _fig(s,
                "Hình 2.4 · MPBR đa lượt cho tuần hoàn nhiên liệu.",
                "Figure 2.4 · The multipass MPBR of fuel circulation.",
                "Bình hình nón chứa hạt nhiên liệu liên kết với khối nạp lại và khối giám sát độ cháy theo vòng lặp",
                "Conical vessel with fuel pellets linked in a loop to the reload box and the burn monitor box")


# ---------------------------------------------------------------------------
@_reg
def fig_f25():
    """Figure 2.5 (source p. 41) - pressurized water Cherenkov detector."""
    w, h = 680, 300
    o = [_defs()]

    # Seven black photodetector bars with pale gap markers.
    for i in range(7):
        o.append(_rect(208 + i * 40, 70, 24, 44, fill="#232323",
                       sw=0, color="#232323"))
    for i in range(6):
        o.append(_rect(232 + i * 40, 62, 16, 60, fill="#ffffff",
                       sw=1.0, color="#b7dce8"))

    # Seven red elements seated on green domes above the platform.
    for i in range(7):
        cx = 220 + i * 40
        o.append(_rect(cx - 9, 128, 18, 22, fill="#e53935", sw=0,
                       color="#e53935"))
        o.append(_path("M%s,152 A14,8 0 0 1 %s,152 Z" % (cx - 14, cx + 14),
                       fill="#8bc34a", sw=0.8, color="#5a9216"))
    # White platform outline and the large dark base block.
    o.append(_rect(200, 152, 280, 34, fill="#ffffff", sw=1.4, color=INK))
    o.append(_rect(200, 210, 280, 46, fill="#2b2b2b", sw=1.2, color="#2b2b2b"))

    s = svg(w, h, "".join(o),
            esc("Figure 2.5 - A schematic of the pressurized water Cherenkov detector"))
    return _fig(s,
                "Hình 2.5 · Sơ đồ đầu dò Cherenkov nước áp lực.",
                "Figure 2.5 · A schematic of the pressurized water Cherenkov detector.",
                "Sơ đồ đầu dò Cherenkov nước áp lực gồm bảy thanh quang điện, bảy phần tử đỏ xanh, bệ và khối đế",
                "Pressurized water Cherenkov detector with seven photodetector bars, seven red-green elements, a platform and a base block")


# ---------------------------------------------------------------------------
@_reg
def fig_f26():
    """Figure 2.6 (source p. 42) - probabilistic neural network."""
    w, h = 680, 360
    o = [_defs()]

    # Dense inter-layer connections first, so the nodes sit on top.
    inp = [(150, 90), (150, 150), (150, 210), (150, 310)]
    hid1 = [(300, y) for y in (80, 130, 180, 230, 280)]
    hid2 = [(430, y) for y in (110, 190, 270)]
    out = (560, 190)
    for a in inp:
        for b in hid1:
            o.append(_line(a[0], a[1], b[0], b[1], sw=0.7, color=CONN))
    for a in hid1:
        for b in hid2:
            o.append(_line(a[0], a[1], b[0], b[1], sw=0.7, color=CONN))
    for b in hid2:
        o.append(_line(b[0], b[1], out[0], out[1], sw=0.7, color=CONN))

    # Nodes.
    for cx, cy in inp:
        o.append(_circle(cx, cy, 11, fill="#000000", sw=0, color="#000000"))
    for cx, cy in hid1 + hid2:
        o.append(_circle(cx, cy, 11, fill="#000000", sw=0, color="#000000"))
    o.append(_circle(out[0], out[1], 22, fill="#000000", sw=0,
                     color="#000000"))

    # Input and output arrows (pale blue, clear of the node labels).
    o.append(_line(40, 150, 92, 150, sw=8, color=PaleArrow))
    o.append(_tri(104, 150, 90, 141, 90, 159, PaleArrow))
    o.append(T(68, 138, "Input", 10.0, anchor="middle", color=INK))
    o.append(_line(586, 190, 638, 190, sw=8, color=PaleArrow))
    o.append(_tri(650, 190, 636, 181, 636, 199, PaleArrow))
    o.append(T(616, 178, "Output", 10.0, anchor="middle", color=INK))

    # Node labels.
    o.append(T(128, 94, "x1", 9.5, anchor="end", color=INK))
    o.append(T(128, 154, "x2", 9.5, anchor="end", color=INK))
    o.append(T(128, 214, "x3", 9.5, anchor="end", color=INK))
    o.append(T(128, 262, "…", 12.0, anchor="end", color=GREY))
    o.append(T(128, 314, "xn", 9.5, anchor="end", color=INK))
    o.append(T(548, 158, "Y", 11.0, anchor="middle", color=INK, weight="600"))

    s = svg(w, h, "".join(o),
            esc("Figure 2.6 - The probabilistic neural network"))
    return _fig(s,
                "Hình 2.6 · Mạng nơ-ron xác suất.",
                "Figure 2.6 · The probabilistic neural network.",
                "Mạng nơ-ron xác suất với các nút đầu vào, hai lớp ẩn và một nút đầu ra Y",
                "Probabilistic neural network with input nodes, two hidden layers and a single output node Y")


# ---------------------------------------------------------------------------
@_reg
def fig_f27():
    """Figure 2.7 (source p. 43) - functional structure of ESMADP."""
    w, h = 680, 420
    o = [_defs()]

    # Top emergency source and its two down-links.
    o.append(_rect(150, 40, 380, 34, fill=CYAN, sw=1.3, color=INK))
    o.append(T(340, 62, "All kinds of emergency", 11.0,
               anchor="middle", color=INK, weight="600"))
    o.append(_arrow(300, 74, 300, 112, sw=3.0, color="#000000"))
    o.append(_arrow(430, 74, 430, 112, sw=3.0, color="#000000"))
    o.append(T(215, 96, "Alarm processing", 9.0, anchor="middle", color=INK))
    o.append(T(500, 96, "Alarm diagnosis", 9.0, anchor="middle", color=INK))

    # Left group: alarm order and intelligent processor with a two-way link.
    o.append(_rect(170, 112, 170, 104, fill="#ffffff", sw=1.2, color=INK))
    o.append(_rect(182, 126, 62, 52, fill=CYAN, sw=1.1, color=INK))
    o.append(_rect(256, 126, 76, 52, fill=CYAN, sw=1.1, color=INK))
    o.append(T(213, 146, "Alarm", 9.0, anchor="middle", color=INK))
    o.append(T(213, 158, "order", 9.0, anchor="middle", color=INK))
    o.append(T(294, 143, "Intelligent", 8.5, anchor="middle", color=INK))
    o.append(T(294, 155, "processor", 8.5, anchor="middle", color=INK))
    o.append(_arrow(244, 143, 254, 143, sw=2.2, color="#000000"))
    o.append(_arrow(256, 165, 246, 165, sw=2.2, color="#000000"))

    # Right group: emergency action and failure diagnosis.
    o.append(_rect(370, 112, 170, 104, fill="#ffffff", sw=1.2, color=INK))
    o.append(_rect(382, 132, 72, 44, fill=CYAN, sw=1.1, color=INK))
    o.append(_rect(466, 132, 64, 44, fill=CYAN, sw=1.1, color=INK))
    o.append(T(418, 149, "Emergency", 8.5, anchor="middle", color=INK))
    o.append(T(418, 161, "action", 8.5, anchor="middle", color=INK))
    o.append(T(498, 149, "Failure", 8.5, anchor="middle", color=INK))
    o.append(T(498, 161, "diagnosis", 8.5, anchor="middle", color=INK))

    # Inference engine fed by both groups.
    o.append(_ellipse(340, 206, 58, 17, fill=CYAN, sw=1.2, color=INK))
    o.append(T(340, 210, "Inference engine", 9.5, anchor="middle",
               color=INK))
    o.append(_arrow(294, 180, 306, 194, sw=1.8, color="#000000"))
    o.append(_arrow(410, 180, 398, 194, sw=1.8, color="#000000"))

    # ESMADP control room and its vertical links.
    o.append(_rrect(200, 278, 280, 56, 12, CYAN, INK, 1.3))
    o.append(T(340, 310, "ESMADP control room", 11.0,
               anchor="middle", color=INK, weight="600"))
    o.append(_arrow(276, 180, 276, 278, sw=2.6, color="#000000"))
    o.append(_arrow(340, 223, 340, 278, sw=2.6, color="#000000"))
    o.append(_arrow(466, 176, 466, 278, sw=2.6, color="#000000"))
    o.append(_arrow(240, 368, 240, 282, sw=2.6, color="#000000"))
    o.append(_arrow(440, 368, 440, 282, sw=2.6, color="#000000"))
    o.append(T(390, 254, "Information", 9.0, anchor="start", color=INK))
    o.append(T(170, 382, "Multiple alarm input", 9.0,
               anchor="middle", color=INK))
    o.append(T(520, 382, "Symptom input", 9.0, anchor="middle", color=INK))

    s = svg(w, h, "".join(o),
            esc("Figure 2.7 - The functional structure of ESMADP"))
    return _fig(s,
                "Hình 2.7 · Cấu trúc chức năng của ESMADP.",
                "Figure 2.7 · The functional structure of ESMADP.",
                "Sơ đồ chức năng ESMADP gồm các nhóm xử lý báo động, chẩn đoán, cơ chế suy luận và phòng điều khiển",
                "Functional structure of ESMADP with alarm processing, diagnosis groups, an inference engine and a control room")
