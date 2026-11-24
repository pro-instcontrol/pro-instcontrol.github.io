# -*- coding: utf-8 -*-
"""Vector figures for Chapter 3 of Book 9 (PPIC): "Study of Control Strategy
of the Converter in Solar Photovoltaic Power System".

Eight source figures are redrawn as clean vectors, preserving the topology,
blocks, signal paths and labels of the originals:

  Figure 3.1 - block diagram of the PV power system.
  Figure 3.2 - MATLAB/Simulink simulation model structure.
  Figure 3.3 - simulation control subsystem block.
  Figure 3.4 - SPWM control pulses of IGBT1 and IGBT2.
  Figure 3.5 - simulation output voltage waveforms, with and without filter.
  Figure 3.6 - control card of TMS320F28035.
  Figure 3.7 - control pulses for the switches of the inverter.
  Figure 3.8 - output voltage waveform of the inverter.

Every function returns the standard 5-tuple ``(svg, caption_vi, caption_en,
aria_vi, aria_en)`` through ``_fig()``.  All SVG text is XML-escaped via
``esc()``/``T()``; captions and aria text contain no ampersands and no CJK.
"""
import math
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
GOLD = "#d4a017"
ORANGE = "#f5a623"
PURPLE = "#b74bd0"
SCOPE = "#0b1a12"


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


def _wave(x0, x1, ymid, amp, cycles, n=241, ripple=0.0,
          color=INK, sw=1.7, phase=0.0):
    """Sine (plus optional high-frequency ripple) as a smooth polyline."""
    pts = []
    for i in range(n):
        t = i / (n - 1.0)
        v = math.sin(2 * math.pi * cycles * t + phase)
        if ripple:
            v += ripple * math.sin(2 * math.pi * cycles * 24 * t)
        pts.append((x0 + t * (x1 - x0), ymid - amp * v))
    return _poly(pts, fill="none", sw=sw, color=color)


# ---------------------------------------------------------------------------
@_reg
def fig_f31():
    """Figure 1 - block diagram of the PV power system."""
    w, h = 680, 330
    o = [_defs()]

    # Main power path along the top row.
    o.append(_rect(36, 58, 92, 44, fill=ICE, sw=1.3, color=NAVY))
    # Small PV panel icon with cell divisions.
    o.append(_rect(52, 64, 60, 16, fill="#3a6ea5", sw=0.8, color="#234570"))
    for gx in (67, 82, 97):
        o.append(_line(gx, 64, gx, 80, sw=0.6, color="#cfe0f5"))
    o.append(_line(52, 72, 112, 72, sw=0.6, color="#cfe0f5"))
    o.append(T(82, 98, "PV array", 8.5, anchor="middle", color=INK))

    o.append(_rect(158, 58, 104, 44, fill=CREAM, sw=1.3, color=NAVY))
    o.append(T(210, 77, "DC/DC", 9.2, anchor="middle", color=INK,
               weight="600"))
    o.append(T(210, 91, "Boost", 9.2, anchor="middle", color=INK,
               weight="600"))

    o.append(_rect(292, 58, 104, 44, fill=ICE, sw=1.3, color=NAVY))
    o.append(T(344, 84, "Inverter", 9.5, anchor="middle", color=INK,
               weight="600"))

    o.append(_rect(426, 58, 92, 44, fill=ICE, sw=1.3, color=NAVY))
    o.append(T(472, 84, "Filter", 9.5, anchor="middle", color=INK,
               weight="600"))

    o.append(_rect(548, 58, 88, 44, fill=CYAN, sw=1.3, color=NAVY))
    o.append(T(592, 84, "Grid", 9.5, anchor="middle", color=INK,
               weight="600"))

    for x1, x2 in ((128, 158), (262, 292), (396, 426), (518, 548)):
        o.append(_arrow(x1, 80, x2, 80, sw=1.6, color=INK))

    # PLL senses the grid and returns a synchronising reference.
    o.append(_rect(548, 150, 88, 44, fill=CYAN, sw=1.3, color=NAVY))
    o.append(T(592, 176, "PLL", 9.5, anchor="middle", color=INK,
               weight="600"))
    o.append(_arrow(592, 102, 592, 150, sw=1.5, color=BLUE))
    o.append(_arrow(546, 172, 430, 172, sw=1.5, color=BLUE))
    o.append(_dot(430, 172, 3.4, BLUE))
    o.append(_arrow(430, 172, 430, 250, sw=1.5, color=BLUE))

    # Controller with its actuating and feedback links.
    o.append(_rect(236, 250, 224, 48, fill=CREAM, sw=1.6, color=NAVY))
    o.append(T(348, 279, "Controller(DSP)", 10.5, anchor="middle",
               color=INK, weight="600"))
    # DC/DC boost: one up-link and one down-link (closed voltage loop).
    o.append(_arrow(220, 248, 220, 104, sw=1.5, color=BLUE))
    o.append(_arrow(248, 104, 248, 248, sw=1.5, color=BLUE))
    # Inverter SPWM drive.
    o.append(_arrow(330, 248, 344, 104, sw=1.5, color=BLUE))
    # Filter output voltage feedback.
    o.append(_arrow(470, 104, 410, 248, sw=1.5, color=BLUE))

    # Human-machine interface over SCI.
    o.append(_rect(548, 250, 88, 48, fill=STEEL, sw=1.3, color=NAVY))
    o.append(T(592, 279, "PC", 9.5, anchor="middle", color=INK,
               weight="600"))
    o.append(_arrow(462, 270, 546, 270, sw=1.5, color=BLUE))
    o.append(_arrow(546, 282, 462, 282, sw=1.5, color=BLUE))
    o.append(T(504, 265, "SCI", 7.8, anchor="middle", color=GREY))

    s = svg(w, h, "".join(o),
            esc("Figure 3.1 - Block diagram of PV power system"))
    return _fig(s,
                "Hình 3.1 · Sơ đồ khối của hệ thống điện mặt trời quang điện.",
                "Figure 3.1 · Block diagram of PV power system.",
                "Sơ đồ khối hệ thống điện mặt trời gồm mảng PV, bộ tăng áp DC/DC, inverter, bộ lọc và lưới, cùng PLL, bộ điều khiển DSP và máy tính giám sát",
                "Block diagram of the PV power system with PV array, DC/DC boost, inverter, filter and grid, plus PLL feedback, a DSP controller and a PC interface")


# ---------------------------------------------------------------------------
@_reg
def fig_f32():
    """Figure 2 - MATLAB/Simulink simulation model structure."""
    w, h = 680, 330
    o = [_defs()]

    # Sample-time and scope blocks.
    o.append(_rect(176, 26, 124, 30, fill="#eef3fb", sw=1.1, color=INK))
    o.append(T(238, 46, "Discrete  Ts = 5e-6 s", 8.5, anchor="middle",
               color=INK))
    o.append(_rect(548, 26, 104, 36, fill="#eef3fb", sw=1.1, color=INK))
    o.append(T(600, 48, "Scope 3", 9.0, anchor="middle", color=INK))
    o.append(_line(566, 54, 578, 54, sw=0.9, color=BLUE))
    o.append(_line(578, 54, 584, 48, sw=0.9, color=BLUE))
    o.append(_line(584, 48, 590, 56, sw=0.9, color=BLUE))
    o.append(_line(590, 56, 598, 50, sw=0.9, color=BLUE))

    # PV array model with a small panel icon.
    o.append(_rect(24, 118, 84, 70, fill="#eef3fb", sw=1.2, color=INK))
    o.append(_rect(38, 130, 56, 26, fill="#3a6ea5", sw=0.8, color="#234570"))
    for gx in (52, 66, 80):
        o.append(_line(gx, 130, gx, 156, sw=0.6, color="#cfe0f5"))
    o.append(_line(38, 143, 94, 143, sw=0.6, color="#cfe0f5"))
    o.append(T(66, 178, "PV Array Model", 8.0, anchor="middle", color=INK))

    # DC/DC boost subsystem with an inductor and a capacitor.
    o.append(_rect(132, 114, 96, 78, fill="#fff4cc", sw=1.2, color=INK))
    o.append(_line(132, 150, 150, 150, sw=1.2, color=INK))
    o.append(_path("M150,150 q7,-11 14,0 q7,-11 14,0 q7,-11 14,0",
                   fill="none", sw=1.2, color=INK))
    o.append(_line(192, 150, 196, 150, sw=1.2, color=INK))
    o.append(_line(196, 138, 196, 162, sw=1.4, color=INK))
    o.append(_line(206, 138, 206, 162, sw=1.4, color=INK))
    o.append(_line(206, 150, 228, 150, sw=1.2, color=INK))
    o.append(T(180, 184, "DC/DC Boost", 8.5, anchor="middle", color=INK))

    # DC bus capacitor.
    o.append(_rect(252, 126, 56, 54, fill="#eef3fb", sw=1.2, color=INK))
    o.append(_line(252, 152, 274, 152, sw=1.2, color=INK))
    o.append(_line(274, 139, 274, 165, sw=1.6, color=INK))
    o.append(_line(284, 139, 284, 165, sw=1.6, color=INK))
    o.append(_line(284, 152, 308, 152, sw=1.2, color=INK))
    o.append(T(280, 174, "DC Bus C", 8.0, anchor="middle", color=INK))

    # Universal bridge with three IGBT legs and freewheeling diodes.
    o.append(_rect(332, 108, 96, 90, fill="#fff4cc", sw=1.2, color=INK))
    o.append(_line(340, 124, 420, 124, sw=1.4, color=INK))
    o.append(_line(340, 170, 420, 170, sw=1.4, color=INK))
    for cx in (352, 380, 408):
        o.append(_line(cx, 124, cx, 134, sw=1.2, color=INK))
        o.append(_rect(cx - 7, 134, 14, 12, fill="#ffffff", sw=1.0,
                       color=INK))
        o.append(_line(cx, 146, cx, 156, sw=1.2, color=INK))
        o.append(_tri(cx, 164, cx - 6, 156, cx + 6, 156, INK))
        o.append(_line(cx, 164, cx, 170, sw=1.2, color=INK))
    o.append(T(380, 190, "Universal Bridge", 8.5, anchor="middle",
               color=INK))

    # LCL filter block.
    o.append(_rect(452, 122, 72, 66, fill="#eef7ee", sw=1.2, color=INK))
    o.append(_path("M460,146 q5,-8 10,0 q5,-8 10,0 q5,-8 10,0",
                   fill="none", sw=1.1, color=INK))
    o.append(_line(490, 146, 496, 146, sw=1.1, color=INK))
    o.append(_line(496, 136, 496, 156, sw=1.3, color=INK))
    o.append(_line(505, 136, 505, 156, sw=1.3, color=INK))
    o.append(T(488, 180, "Filters (LCL)", 7.8, anchor="middle", color=INK))

    # Measurement and grid blocks.
    o.append(_rect(548, 114, 104, 78, fill="#eef3fb", sw=1.2, color=INK))
    o.append(T(600, 140, "Three-phase", 8.5, anchor="middle", color=INK))
    o.append(T(600, 154, "V-I Measurement", 8.0, anchor="middle", color=INK))
    o.append(_wave(566, 634, 173, 5, 1.5, n=81, color=BLUE, sw=0.9))
    o.append(_rect(548, 216, 104, 52, fill=CYAN, sw=1.2, color=INK))
    o.append(T(600, 238, "Power System", 8.5, anchor="middle", color=INK))
    o.append(T(600, 252, "(Grid)", 8.0, anchor="middle", color=INK))

    # Main signal path.
    for x1, x2 in ((108, 132), (228, 252), (308, 332), (428, 452),
                   (524, 548)):
        o.append(_arrow(x1, 152, x2, 152, sw=1.5, color=INK))
    o.append(_arrow(600, 192, 600, 216, sw=1.5, color=INK))
    o.append(_arrow(600, 114, 600, 62, sw=1.3, color=INK))
    o.append(T(612, 92, "mux", 7.5, anchor="start", color=GREY))

    # Measurement feedback to the boost stage.
    o.append(_line(640, 192, 640, 286, sw=1.3, color=BLUE))
    o.append(_arrow(640, 286, 180, 286, sw=1.3, color=BLUE))
    o.append(_arrow(180, 286, 180, 192, sw=1.3, color=BLUE))
    o.append(T(400, 280, "feedback signals", 8.0, anchor="middle",
               color=GREY))

    # Discrete PWM control feeds the boost and the bridge.
    o.append(_arrow(220, 56, 180, 114, sw=1.0, dash="4 3", color=BLUE))
    o.append(_arrow(300, 41, 380, 41, sw=1.0, dash="4 3", color=BLUE))
    o.append(_arrow(380, 41, 380, 108, sw=1.0, dash="4 3", color=BLUE))
    o.append(T(332, 34, "PWM control", 7.5, anchor="middle", color=BLUE))

    s = svg(w, h, "".join(o),
            esc("Figure 3.2 - Simulation model structure"))
    return _fig(s,
                "Hình 3.2 · Cấu trúc mô phỏng trong MATLAB/Simulink.",
                "Figure 3.2 · Simulation model structure.",
                "Mô hình Simulink gồm mảng PV, bộ tăng áp DC/DC, tụ DC bus, cầu nghịch lưu, bộ lọc LCL, khối đo lường và hệ thống điện lưới",
                "Simulink model with PV array, DC/DC boost, DC bus capacitor, inverter bridge, LCL filter, measurement block and power grid")


# ---------------------------------------------------------------------------
@_reg
def fig_f33():
    """Figure 3 - simulation control subsystem block."""
    w, h = 680, 240
    o = [_defs()]

    # Main control chain, left to right.
    o.append(_ellipse(38, 74, 26, 11, fill="#eef3fb", sw=1.1, color=INK))
    o.append(T(38, 77, "Vabc (pu)", 7.8, anchor="middle", color=INK))

    o.append(_rect(90, 50, 96, 48, fill=ICE, sw=1.2, color=INK))
    o.append(T(138, 68, "abc to dq0", 8.5, anchor="middle", color=INK))
    o.append(T(138, 82, "Transformation", 7.6, anchor="middle", color=INK))

    o.append(_rect(210, 50, 64, 48, fill=ICE, sw=1.2, color=INK))
    o.append(T(242, 68, "Selector", 8.5, anchor="middle", color=INK))
    o.append(T(242, 82, "Vd Vq", 8.5, anchor="middle", color=INK))

    o.append(_circle(304, 74, 11, fill="#ffffff", sw=1.2, color=INK))
    o.append(T(304, 78, "+", 11, anchor="middle", color=INK, weight="600"))

    o.append(_rect(336, 50, 96, 48, fill=CREAM, sw=1.2, color=INK))
    o.append(T(384, 68, "Discrete PI", 8.5, anchor="middle", color=INK))
    o.append(T(384, 82, "Controller", 8.5, anchor="middle", color=INK))

    o.append(_rect(452, 50, 72, 48, fill=ICE, sw=1.2, color=INK))
    o.append(T(488, 68, "Vd Vq", 8.5, anchor="middle", color=INK))
    o.append(T(488, 82, "inverter", 8.0, anchor="middle", color=INK))

    o.append(_rect(540, 50, 78, 48, fill=ICE, sw=1.2, color=INK))
    o.append(T(579, 68, "dq0 to abc", 8.2, anchor="middle", color=INK))
    o.append(T(579, 82, "Transformation", 7.4, anchor="middle", color=INK))

    o.append(_ellipse(650, 74, 24, 11, fill="#eef3fb", sw=1.1, color=INK))
    o.append(T(650, 77, "Valc_inv", 7.6, anchor="middle", color=INK))

    for x1, x2 in ((64, 90), (186, 210), (274, 293), (315, 336),
                   (432, 452), (524, 540), (618, 626)):
        o.append(_arrow(x1, 74, x2, 74, sw=1.5, color=INK))

    # Reference constants feeding the summing junction.
    o.append(_rect(224, 150, 88, 30, fill=CREAM, sw=1.1, color=INK))
    o.append(T(268, 169, "Vd_ref = 2", 8.0, anchor="middle", color=INK))
    o.append(_arrow(268, 150, 299, 85, sw=1.3, color=BLUE))
    o.append(_rect(330, 150, 88, 30, fill=CREAM, sw=1.1, color=INK))
    o.append(T(374, 169, "Vq_ref = 0", 8.0, anchor="middle", color=INK))
    o.append(_arrow(330, 160, 310, 86, sw=1.3, color=BLUE))

    # Virtual PLL and its wt bus to both transformations.
    o.append(_ellipse(28, 176, 20, 9, fill="#eef3fb", sw=1.0, color=INK))
    o.append(T(28, 179, "Freq", 7.5, anchor="middle", color=INK))
    o.append(_rect(50, 150, 130, 52, fill=CYAN, sw=1.2, color=INK))
    o.append(T(115, 168, "Discrete Virtual PLL", 8.5, anchor="middle",
               color=INK))
    o.append(T(115, 182, "50 Hz", 8.0, anchor="middle", color=INK))
    o.append(T(115, 194, "(Sin_Cos, wt)", 7.5, anchor="middle", color=GREY))
    o.append(_arrow(48, 176, 50, 176, sw=1.3, color=BLUE))
    o.append(_line(138, 176, 600, 176, sw=1.3, color=BLUE))
    o.append(_arrow(180, 176, 183, 176, sw=1.3, color=BLUE))
    o.append(_arrow(138, 176, 138, 98, sw=1.3, color=BLUE))
    o.append(_arrow(579, 176, 579, 98, sw=1.3, color=BLUE))
    o.append(T(470, 170, "wt (sin_cos)", 8.0, anchor="middle", color=BLUE))

    # Modulation-index monitor tapped from the PI output.
    o.append(_line(442, 74, 442, 26, sw=1.1, color=INK))
    o.append(_arrow(442, 26, 460, 26, sw=1.1, color=INK))
    o.append(_rect(460, 16, 56, 20, fill="#eef3fb", sw=1.0, color=INK))
    o.append(T(488, 30, "Scope", 8.0, anchor="middle", color=INK))
    o.append(_arrow(516, 26, 538, 26, sw=1.1, color=INK))
    o.append(_ellipse(552, 26, 14, 8, fill="#eef3fb", sw=1.0, color=INK))
    o.append(T(552, 29, "m", 8.5, anchor="middle", color=INK))
    o.append(T(580, 29, "modulation index m", 8.0, anchor="start",
               color=GREY))

    s = svg(w, h, "".join(o),
            esc("Figure 3.3 - Simulation control subsystem block"))
    return _fig(s,
                "Hình 3.3 · Khối điều khiển trong mô phỏng.",
                "Figure 3.3 · Simulation control subsystem block.",
                "Sơ đồ điều khiển gồm PLL ảo 50 Hz, biến đổi abc sang dq0, bộ chọn Vd Vq, bộ điều khiển PI, biến đổi dq0 sang abc và bộ phát xung PWM",
                "Control subsystem with a 50 Hz virtual PLL, abc to dq0 conversion, Vd Vq selector, PI controller, dq0 to abc conversion and PWM pulse generation")


# ---------------------------------------------------------------------------
@_reg
def fig_f34():
    """Figure 4 - SPWM control pulses of IGBT1 and IGBT2."""
    w, h = 680, 300
    o = [_defs()]

    x0, x1, n = 90, 640, 60
    period = (x1 - x0) / float(n)

    def _pulses(y_top, y_bot, fill, stroke, complement=False):
        pts = []
        for i in range(n):
            t = (i + 0.5) / n
            duty = 0.5 + 0.44 * math.sin(2 * math.pi * t)
            if complement:
                duty = 1.0 - duty
            duty = max(0.05, min(0.95, duty))
            bw = duty * period
            bx = x0 + i * period + (period - bw) / 2.0
            pts.append(_rect(bx, y_top, bw, y_bot - y_top, fill=fill,
                             sw=0.5, color=stroke))
        return "".join(pts)

    # Upper trace - IGBT1 pulses.
    o.append(T(x0, 26, "V1_Pulse", 9.0, anchor="start", color=BLUE,
               weight="600"))
    o.append(_line(x0, 110, 648, 110, sw=1.0, color=INK))
    o.append(_arrow(x0, 110, 650, 110, sw=1.0, color=INK))
    o.append(_pulses(40, 110, "#dbeafe", BLUE))
    o.append(T(84, 44, "1", 8.0, anchor="end", color=GREY))
    o.append(T(84, 108, "0", 8.0, anchor="end", color=GREY))

    # Lower trace - complementary IGBT2 pulses.
    o.append(T(x0, 156, "V2_Pulse", 9.0, anchor="start", color=RED,
               weight="600"))
    o.append(_line(x0, 240, 648, 240, sw=1.0, color=INK))
    o.append(_arrow(x0, 240, 650, 240, sw=1.0, color=INK))
    o.append(_pulses(170, 240, "#f7d6d2", RED, complement=True))
    o.append(T(84, 174, "1", 8.0, anchor="end", color=GREY))
    o.append(T(84, 238, "0", 8.0, anchor="end", color=GREY))

    # Time axis.
    for i in range(7):
        tx = x0 + i * (x1 - x0) / 6.0
        o.append(_line(tx, 240, tx, 244, sw=0.8, color=INK))
        o.append(T(tx, 256, "0.%02d" % i, 7.6, anchor="middle",
                   color=GREY))
    o.append(T(648, 276, "t (s)", 8.0, anchor="end", color=GREY))

    s = svg(w, h, "".join(o),
            esc("Figure 3.4 - SPWM control pulses of IGBT1 and IGBT2"))
    return _fig(s,
                "Hình 3.4 · Xung điều khiển SPWM cho IGBT1 và IGBT2.",
                "Figure 3.4 · SPWM control pulses of IGBT1 and IGBT2.",
                "Hai dãy xung SPWM bổ sung nhau cho IGBT1 và IGBT2 trong cùng một nhánh cầu, độ rộng xung thay đổi theo hình sin",
                "Two complementary SPWM pulse trains for IGBT1 and IGBT2 in one bridge arm, with pulse width varying sinusoidally")


# ---------------------------------------------------------------------------
@_reg
def fig_f35():
    """Figure 5 - simulation output waveforms, with and without filter."""
    w, h = 680, 380
    o = [_defs()]

    x0, x1, n = 90, 640, 150
    period = (x1 - x0) / float(n)

    # Unfiltered SPWM inverter output: rectangular pulses in a sine envelope.
    o.append(T(x0, 26, "Vab_inverter", 9.0, anchor="start", color=BLUE,
               weight="600"))
    o.append(_line(x0, 85, 648, 85, sw=0.8, color=GREY))
    for i in range(n):
        t = (i + 0.5) / n
        v = math.sin(2 * math.pi * 3 * t)
        duty = min(1.0, abs(v)) * 0.95
        if duty < 0.06:
            continue
        bw = duty * period
        bx = x0 + i * period + (period - bw) / 2.0
        if v >= 0:
            o.append(_rect(bx, 42, bw, 43, fill="#bcd6f5", sw=0.4,
                           color=BLUE))
        else:
            o.append(_rect(bx, 85, bw, 43, fill="#f7c9c5", sw=0.4,
                           color=RED))
    o.append(T(84, 46, "+1", 8.0, anchor="end", color=GREY))
    o.append(T(84, 88, "0", 8.0, anchor="end", color=GREY))
    o.append(T(84, 128, "-1", 8.0, anchor="end", color=GREY))

    # Filtered load voltage: smooth sine with a small switching ripple.
    o.append(T(x0, 156, "Vab_load", 9.0, anchor="start", color=GREEN,
               weight="600"))
    o.append(_line(x0, 210, 648, 210, sw=0.8, color=GREY))
    o.append(_wave(x0, x1, 210, 34, 3, n=301, ripple=0.035,
                   color=GREEN, sw=1.8))
    o.append(T(84, 168, "300", 8.0, anchor="end", color=GREY))
    o.append(T(84, 212, "0", 8.0, anchor="end", color=GREY))
    o.append(T(84, 254, "-300", 8.0, anchor="end", color=GREY))

    # Load current: in-phase sine of smaller amplitude.
    o.append(T(x0, 286, "I_load", 9.0, anchor="start", color=PURPLE,
               weight="600"))
    o.append(_line(x0, 326, 648, 326, sw=0.8, color=GREY))
    o.append(_wave(x0, x1, 326, 22, 3, n=301, ripple=0.03,
                   color=PURPLE, sw=1.7))
    o.append(T(84, 294, "20", 8.0, anchor="end", color=GREY))
    o.append(T(84, 328, "0", 8.0, anchor="end", color=GREY))
    o.append(T(84, 362, "-20", 8.0, anchor="end", color=GREY))

    # Shared time axis.
    for i in range(7):
        tx = x0 + i * (x1 - x0) / 6.0
        o.append(_line(tx, 362, tx, 366, sw=0.8, color=INK))
        o.append(T(tx, 376, "0.%02d" % i, 7.6, anchor="middle",
                   color=GREY))

    s = svg(w, h, "".join(o),
            esc("Figure 3.5 - Simulation output voltage waveform without filter; voltage waveform with filter"))
    return _fig(s,
                "Hình 3.5 · Điện áp đầu ra mô phỏng khi chưa lọc và sau khi lọc.",
                "Figure 3.5 · Simulation output voltage waveform without filter; voltage waveform with filter.",
                "Ba dạng sóng xếp chồng gồm điện áp SPWM chưa lọc của inverter, điện áp tải sau bộ lọc LCL và dòng tải, cho thấy hài bậc cao đã bị loại bỏ",
                "Three stacked waveforms of unfiltered SPWM inverter output voltage, filtered load voltage and load current, showing the high-order harmonics removed by the filter")


# ---------------------------------------------------------------------------
@_reg
def fig_f36():
    """Figure 6 - control card of TMS320F28035."""
    w, h = 680, 340
    o = [_defs()]

    # Green printed-circuit board with gold edge fingers.
    o.append(_rrect(60, 90, 560, 150, 8, "#1d5c35", "#0d361f", 2.0))
    o.append(_rect(170, 240, 340, 22, fill=GOLD, sw=1.0, color="#8a6508"))
    for gx in range(176, 506, 10):
        o.append(_line(gx, 240, gx, 262, sw=1.0, color="#8a6508"))
    # Card notches either side of the edge fingers.
    o.append(_circle(163, 251, 7, fill="#ffffff", sw=1.0, color="#0d361f"))
    o.append(_circle(517, 251, 7, fill="#ffffff", sw=1.0, color="#0d361f"))

    o.append(T(340, 108, "TMS320F28035 controlCARD", 9.2, anchor="middle",
               color="#dff0d8", weight="600"))

    # White 12-pin interface connector on the left.
    o.append(_rect(88, 124, 54, 86, fill="#f2f2f2", sw=1.0, color="#666666"))
    for py in (136, 149, 162, 175, 188, 201):
        o.append(_circle(101, py, 3.0, fill="#9aa0a6", sw=0.6,
                         color="#555555"))
        o.append(_circle(130, py, 3.0, fill="#9aa0a6", sw=0.6,
                         color="#555555"))
    o.append(T(115, 219, "J1", 7.5, anchor="middle", color="#222222"))

    # Two small logic ICs.
    for iy, tag in ((132, "U2"), (182, "U3")):
        o.append(_rect(170, iy, 50, 26, fill="#1a1a1a", sw=0.8,
                       color="#555555"))
        for px in range(178, 216, 8):
            o.append(_line(px, iy - 4, px, iy, sw=0.8, color="#b9c2c9"))
            o.append(_line(px, iy + 26, px, iy + 30, sw=0.8,
                           color="#b9c2c9"))
        o.append(T(195, iy + 16, tag, 7.0, anchor="middle",
                   color="#dddddd"))

    # Crystal oscillator and decoupling capacitors.
    o.append(_rect(250, 134, 26, 26, fill="#b0b8bd", sw=0.9,
                   color="#666666"))
    o.append(_circle(263, 147, 7, fill="#d7dde1", sw=0.8, color="#666666"))
    o.append(T(263, 174, "Y1", 7.0, anchor="middle", color="#e8f5e9"))
    for cx in (240, 262, 284):
        o.append(_rect(cx, 190, 12, 20, fill="#2b2b2b", sw=0.7,
                       color="#666666"))
        o.append(_line(cx, 193, cx + 12, 193, sw=1.2, color="#9aa0a6"))
    o.append(T(262, 222, "C1  C2  C3", 7.0, anchor="middle",
               color="#e8f5e9"))

    # JTAG header.
    o.append(_rect(300, 98, 40, 16, fill="#333333", sw=0.8,
                   color="#888888"))
    for px in range(306, 338, 5):
        o.append(_line(px, 100, px, 112, sw=1.0, color="#d4a017"))
    o.append(T(320, 126, "JTAG", 7.0, anchor="middle", color="#e8f5e9"))

    # Central DSP package with pins on all four sides.
    o.append(_rect(360, 124, 116, 72, fill="#1e1e1e", sw=1.2,
                   color="#6b7280"))
    for px in range(368, 469, 9):
        o.append(_line(px, 120, px, 124, sw=1.0, color="#b9c2c9"))
        o.append(_line(px, 196, px, 200, sw=1.0, color="#b9c2c9"))
    for py in range(132, 190, 9):
        o.append(_line(356, py, 360, py, sw=1.0, color="#b9c2c9"))
        o.append(_line(476, py, 480, py, sw=1.0, color="#b9c2c9"))
    o.append(T(418, 149, "TI", 10.5, anchor="middle", color="#ffffff",
               weight="600"))
    o.append(T(418, 166, "TMS320F28035", 8.0, anchor="middle",
               color="#ffffff"))
    o.append(T(418, 182, "32-bit DSP / MCU", 7.0, anchor="middle",
               color="#cbd5d0"))

    # Voltage regulator, status LEDs and pin headers on the right.
    o.append(_rect(506, 126, 44, 30, fill="#242424", sw=0.8,
                   color="#777777"))
    o.append(T(528, 145, "U4", 7.5, anchor="middle", color="#dddddd"))
    for lx, lc, lab in ((508, "#e53935", "PWR"), (534, "#f5a623", "ERR"),
                        (560, "#39b54a", "RUN")):
        o.append(_circle(lx, 182, 5.0, fill=lc, sw=0.8, color="#0d361f"))
        o.append(T(lx, 198, lab, 6.8, anchor="middle", color="#e8f5e9"))
    for px in (508, 528, 548, 568):
        o.append(_rect(px, 100, 8, 12, fill=GOLD, sw=0.7,
                       color="#8a6508"))
    o.append(T(540, 126, "SCI / GPIO", 7.0, anchor="middle",
               color="#e8f5e9"))

    s = svg(w, h, "".join(o),
            esc("Figure 3.6 - Control card of TMS320F28035"))
    return _fig(s,
                "Hình 3.6 · Thẻ điều khiển TMS320F28035.",
                "Figure 3.6 · Control card of TMS320F28035.",
                "Thẻ điều khiển TMS320F28035 dạng vector với chip DSP trung tâm, đầu nối J1, thạch anh, tụ điện, đèn trạng thái và chân tiếp xúc vàng",
                "Vector drawing of the TMS320F28035 control card with the central DSP chip, connector J1, oscillator, capacitors, status LEDs and gold edge fingers")


# ---------------------------------------------------------------------------
@_reg
def fig_f37():
    """Figure 7 - control pulses for the switches of the inverter."""
    w, h = 680, 360
    o = [_defs()]

    # Oscilloscope screen and graticule.
    o.append(_rect(60, 30, 560, 278, fill=SCOPE, sw=1.4, color="#4b5563"))
    for gx in range(130, 620, 70):
        o.append(_line(gx, 30, gx, 308, sw=0.6, color="#1f3a2b"))
    for gy in range(86, 308, 56):
        o.append(_line(60, gy, 620, gy, sw=0.6, color="#1f3a2b"))
    o.append(T(70, 22, "Tek", 10.5, anchor="start", color="#ffffff",
               weight="600"))
    o.append(T(610, 22, "SAVE_REC", 8.0, anchor="end", color="#cbd5d0"))

    xa, period, duty = 90, 98.0, 52.0
    dead = 5.0

    def _train(yh, yl, starts, high_first, color):
        pts = [(xa, yh if high_first else yl)]
        for s in starts:
            if high_first:
                pts += [(s, yl), (s, yh), (s + duty, yh), (s + duty, yl)]
            else:
                pts += [(s - dead, yh), (s - dead, yl),
                        (s + duty + dead, yl), (s + duty + dead, yh)]
        pts.append((590, yh if not high_first else yl))
        return _poly(pts, fill="none", sw=1.9, color=color)

    starts = [xa + k * period for k in range(5)]

    # Four channels of the two inverter arms.
    traces = (
        (50, 95, starts, True, ORANGE, "CH1", "#f5a623"),
        (115, 160, starts, False, "#22c1c3", "CH2", "#22c1c3"),
        (180, 225, [s + 6 for s in starts], True, "#39b54a", "CH3",
         "#39b54a"),
        (245, 290, [s + 6 for s in starts], False, PURPLE, "CH4", PURPLE),
    )
    for yh, yl, st, hf, col, tag, tcol in traces:
        o.append(_train(yh, yl, st, hf, col))
        o.append(T(16, yh + 4, tag, 9.0, anchor="start", color=tcol,
                   weight="600"))
        o.append(T(16, yl - 3, "1.00V", 7.0, anchor="start", color=GREY))

    # Dead-time bands between complementary transitions.
    for s in (starts[1], starts[1] + 6):
        o.append(_rect(s - dead, 50, dead, 45, fill="#3a3a3a", sw=0))
        o.append(_rect(s - dead, 115, dead, 45, fill="#3a3a3a", sw=0))
    o.append(_arrow(232, 130, 192, 132, sw=1.0, color="#ffd166"))
    o.append(T(238, 128, "dead time", 8.0, anchor="start",
               color="#ffd166"))

    # Scope readout bar.
    o.append(T(60, 326, "CH1 1.00V    CH2 1.00V    CH3 1.00V    "
               "CH4 1.00V", 8.0, anchor="start", color=INK))
    o.append(T(60, 340, "M 10.0us    20-Dec-11 14:18", 8.0,
               anchor="start", color=INK))
    o.append(T(620, 340, "TEK0026.BMP", 7.5, anchor="end", color=GREY))

    s = svg(w, h, "".join(o),
            esc("Figure 3.7 - Control pulses for the switches of Inverter"))
    return _fig(s,
                "Hình 3.7 · Xung điều khiển các khóa của inverter.",
                "Figure 3.7 · Control pulses for the switches of Inverter.",
                "Bốn dạng xung SPWM trên máy hiện sóng cho hai nhánh của inverter, mỗi cặp xung bổ sung nhau và có vùng thời gian chết giữa các lần chuyển mạch",
                "Four oscilloscope SPWM pulse traces for the two inverter arms, each complementary pair separated by dead-time bands at the switching instants")


# ---------------------------------------------------------------------------
@_reg
def fig_f38():
    """Figure 8 - output voltage waveform of the inverter."""
    w, h = 680, 370
    o = [_defs()]

    # Oscilloscope screen and graticule.
    o.append(_rect(70, 30, 540, 250, fill=SCOPE, sw=1.4, color="#4b5563"))
    for gx in range(140, 610, 70):
        o.append(_line(gx, 30, gx, 280, sw=0.6, color="#1f3a2b"))
    for gy in range(78, 280, 50):
        o.append(_line(70, gy, 610, gy, sw=0.6, color="#1f3a2b"))
    o.append(T(80, 22, "Tek", 10.5, anchor="start", color="#ffffff",
               weight="600"))
    o.append(T(610, 22, "SAVE_REC", 8.0, anchor="end", color="#cbd5d0"))

    x0, x1 = 90, 590
    o.append(_line(x0, 165, x1, 165, sw=0.8, color="#3d5c4a", dash="4 4"))

    # Four oscilloscope channels.
    o.append(_line(x0, 60, x1, 60, sw=2.0, color=ORANGE))
    o.append(_wave(x0, x1, 165, 70, 3, n=301, color="#22c1c3", sw=2.0))
    o.append(_wave(x0, x1, 165, 38, 3, n=301, ripple=0.04,
                   color="#39b54a", sw=2.0))
    o.append(_wave(x0, x1, 165, 22, 3, n=301, color=PURPLE, sw=2.0))

    # In-phase cue at a grid-voltage peak.
    o.append(_arrow(300, 96, 300, 88, sw=1.0, color="#ffd166"))
    o.append(T(308, 92, "same phase, same frequency", 8.0,
               anchor="start", color="#ffd166"))

    # Readout bar and four-colour legend.
    o.append(T(70, 300, "CH1 5.00V    CH2 5.00V    CH3 1.00V    "
               "M 5.00ms", 8.0, anchor="start", color=INK))
    o.append(T(70, 314, "24-Dec-11 16:23    49.9696 Hz", 8.0,
               anchor="start", color=INK))
    legend = ((70, ORANGE, "DC bus"), (180, "#22c1c3", "Grid voltage"),
              (320, "#39b54a", "Inverter voltage"),
              (470, PURPLE, "Inverter current"))
    for lx, col, lab in legend:
        o.append(_line(lx, 335, lx + 20, 335, sw=2.4, color=col))
        o.append(T(lx + 26, 338, lab, 8.0, anchor="start", color=INK))

    s = svg(w, h, "".join(o),
            esc("Figure 3.8 - Output voltage waveform of Inverter"))
    return _fig(s,
                "Hình 3.8 · Dạng sóng điện áp đầu ra của inverter.",
                "Figure 3.8 · Output voltage waveform of Inverter.",
                "Dạng sóng máy hiện sóng gồm bốn kênh: điện áp bus DC màu vàng, điện áp lưới màu xanh dương, điện áp đầu ra inverter màu xanh lá và dòng đầu ra màu tím cùng pha và cùng tần số với lưới",
                "Oscilloscope traces with four channels: yellow DC bus, blue grid voltage, green inverter output voltage and purple inverter output current in phase and in frequency with the grid")
