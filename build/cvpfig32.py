# -*- coding: utf-8 -*-
"""Vector redraws of the two figures in Baumann Chapter 32,
*Control Valve Primer*, 5th ed. -- "Pipe Vibration Due to Sound".

Figure 32-1 is a log-log correlation of pipe acceleration with sound power
level and frequency; its three parallel lines are computed from the stated
relationship a proportional to f times 10**(Lwi/20), calibrated so that
4000 Hz at Lwi = 120 dB gives 140 m/s**2 (14 G).  Figure 32-2 is a labelled
section through an angle valve with an enlarged outlet, showing the
converging sonic jet and the turbulent eddies in the downstream pipe.

Both functions return the standard 5-tuple via :func:`vfig._fig` and are
registered in :data:`FIGS` through :func:`_reg`, mirroring ``cvpfig22.py``.
All text is escaped; there are no raster images, no CJK and no bare '&'.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, _arrow, _circle, _defs,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


def _fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def T(x, y, s, size=8.2, **kw):
    """Escaped text primitive."""
    return _txt(x, y, esc(s), size, **kw)


def _rtxt(x, y, s, deg, size=7.8, color=INK, anchor="middle", weight=""):
    """Text rotated about its own anchor point, for labels along a curve."""
    inner = _txt(x, y, esc(s), size, anchor=anchor, color=color, weight=weight)
    return '<g transform="rotate(%s %s %s)">%s</g>' % (
        _fmt(deg), _fmt(x), _fmt(y), inner)


def _ylabel(cx, cy, s, size=7.6):
    """Vertical axis title reading bottom-to-top."""
    inner = _txt(cx, cy, esc(s), size, color=INK)
    return '<g transform="rotate(-90 %s %s)">%s</g>' % (
        _fmt(cx), _fmt(cy), inner)


def _lead(o, x, y, tx, ty, text, size=7.6, color=INK, anchor="end"):
    """Grey leader line plus a bilingual T() label."""
    o.append(_line(x, y, tx, ty, sw=0.9, color=GREY))
    lx = tx - 4 if anchor == "end" else tx + 4
    o.append(T(lx, ty + 2.5, text, size, anchor=anchor, color=color))
    return o


@_reg
def fig_f321():
    """Figure 32-1 -- log-log acceleration / sound power / frequency graph."""
    w, h = 680, 410
    L, T0, R, B = 104, 60, 440, 326
    o = []

    def px(f):
        return L + (math.log10(f) - 2.0) / 3.0 * (R - L)

    def py(a):
        return B - math.log10(a) / 3.0 * (B - T0)

    def acc(f, lwi):
        # a ~ f * 10**(Lwi/20), pinned to 140 m/s2 at 4000 Hz and 120 dB.
        return 0.035 * f * (10.0 ** ((lwi - 120.0) / 20.0))

    o.append(T(340, 16,
               "Gia tốc, mức công suất âm và tần số / Acceleration, sound power level and frequency",
               10.2, color=INK, weight="600"))
    o.append(T(340, 32, "Thang log-log · a ∝ f × 10^(Lwi/20) · 10 m/s² = 1 G",
               7.6, color=GREY))

    # Frame and faint minor log gridlines.
    o.append(_rect(L, T0, R - L, B - T0, fill="#fdfcf9", sw=1.1))
    for decade in range(3):
        for m in range(2, 10):
            f = m * (10 ** (2 + decade))
            if f < 100000:
                o.append(_line(px(f), T0, px(f), B, sw=0.4, color="#f0f1f3"))
            a = m * (10 ** decade)
            if a < 1000:
                o.append(_line(L, py(a), R, py(a), sw=0.4, color="#f0f1f3"))

    # Major decades, gridlines and readable tick labels.
    for a in (1, 10, 100, 1000):
        yy = py(a)
        o.append(_line(L, yy, R, yy, sw=0.8, color="#ccd0d4"))
        o.append(_txt(L - 8, yy + 2.6, str(a), 7.2, anchor="end", color=GREY))
    for f, lab in ((100, "100"), (1000, "1000"),
                   (10000, "10,000"), (100000, "100,000")):
        xx = px(f)
        o.append(_line(xx, T0, xx, B, sw=0.7, color="#e0e2e5"))
        o.append(_txt(xx, B + 13, lab, 7.2, color=GREY))

    o.append(_ylabel(22, (T0 + B) / 2.0, "Gia tốc m/s² / Acceleration m/s²"))
    o.append(T((L + R) / 2.0, B + 30,
               "Tần số âm thanh Hz / Sound frequency Hz", 7.8, color=INK))

    # The three physically derived parallel lines.
    colors = ((160, BLUE), (120, INK), (80, GREEN))
    for lwi, color in colors:
        pts = []
        for i in range(241):
            f = 10 ** (2.0 + 3.0 * i / 240.0)
            a = acc(f, lwi)
            if 1.0 <= a <= 1000.0:
                pts.append((px(f), py(a)))
        o.append(_poly(pts, sw=1.5, color=color))

    deg = -math.degrees(math.atan2(py(1) - py(10), px(1000) - px(100)))
    for lwi, f, color in ((160, 130, BLUE), (120, 1500, INK), (80, 30000, GREEN)):
        o.append(_rtxt(px(f), py(acc(f, lwi)) - 3,
                       "Lwi = %d dB" % lwi, deg, 7.8,
                       color=color, weight="600"))

    # Dotted guide: vertical at 4000 Hz, horizontal at 140 m/s2.
    gx, gy = px(4000.0), py(140.0)
    o.append(_line(gx, B, gx, gy, sw=0.9, dash="3,3", color=GREY))
    o.append(_line(L, gy, gx, gy, sw=0.9, dash="3,3", color=GREY))
    o.append(_circle(gx, gy, 3.2, fill=INK, sw=0.9, color="#ffffff"))
    o.append(_txt(gx, B + 13, "4000", 6.6, color=BLUE))

    # Right-hand explanation and guide callout.
    o.append(T(557, 70, "Mối liên hệ / Relationship", 8.2,
               anchor="middle", color=INK, weight="600"))
    o.append(T(557, 86, "a ∝ f × 10^(Lwi/20)", 8.2,
               anchor="middle", color=GREY))
    o.append(_rect(452, 116, 210, 44, fill="#ffffff", sw=1.0, stroke=GREY))
    o.append(T(458, 132, "4000 Hz · 120 dB ·", 8.4,
               anchor="start", color=INK, weight="600"))
    o.append(T(458, 147, "140 m/s² (14 G)", 8.4,
               anchor="start", color=BLUE, weight="600"))
    o.append(_line(452, 138, gx + 4, gy, sw=0.8, dash="2,2", color=GREY))

    # In-SVG bilingual strip.
    o.append(T(340, 384, "Hình 32-1 · Gia tốc theo mức công suất âm và tần số.",
               7.2, color=INK))
    o.append(T(340, 398, "Figure 32-1 · Acceleration versus sound power level and frequency.",
               7.2, color=GREY))

    title = "Đồ thị log-log gia tốc theo công suất âm và tần số"
    caption_vi = ("Hình 32-1 · Tương quan giữa gia tốc, mức công suất âm và tần số. "
                  "Đường chấm chỉ mối liên hệ giữa 4000 Hz (cps), mức công suất âm "
                  "120 dB và gia tốc 140 m/s² (14 G).")
    caption_en = ("Figure 32-1 · Correlation between acceleration, sound power level, "
                  "and frequency. The dotted line shows the relationships between "
                  "4000 Hz (cps), 120 dB sound power level, and 140 m/s² (14 G) "
                  "acceleration.")
    aria_vi = ("Đồ thị log-log: gia tốc từ 1 đến 1000 m/s² theo tần số âm thanh từ 100 "
               "đến 100000 Hz; ba đường song song ứng với Lwi bằng 160, 120 và 80 dB; "
               "đường chấm tại 4000 Hz cắt đường 120 dB ở 140 m/s² (14 G).")
    aria_en = ("Log-log graph: acceleration from 1 to 1000 m/s² against sound "
               "frequency from 100 to 100000 Hz; three parallel lines for Lwi = 160, "
               "120 and 80 dB; a dotted guide at 4000 Hz meets the 120 dB line at "
               "140 m/s² (14 G).")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)


@_reg
def fig_f322():
    """Figure 32-2 -- angle valve with enlarged outlet and velocity zones."""
    w, h = 680, 460
    o = [_defs()]

    o.append(T(340, 18,
               "Van góc có cửa ra mở rộng / Angle valve with enlarged outlet",
               10.2, color=INK, weight="600"))
    o.append(T(340, 34,
               "Sơ đồ phân bố vận tốc và vùng nhiễu loạn / Velocity gradients and turbulent zones",
               7.6, color=GREY))

    # Valve centreline.
    o.append(_line(300, 42, 300, 428, sw=0.9, color=GREY, dash="6,4"))

    # Bonnet, actuator and stem.
    o.append(_rect(248, 66, 104, 106, fill="url(#h6)", sw=1.3))
    o.append(_rect(288, 66, 24, 120, fill=PAPER, sw=1.0))
    o.append(_rect(268, 38, 64, 10, fill="#cbd5df", sw=1.1))
    o.append(_rect(294, 46, 12, 172, fill="#dfe7f0", sw=1.2))

    # Horizontal inlet from the left, and the upper valve chamber.
    o.append(_rect(96, 170, 152, 16, fill="url(#h6)", sw=1.2))
    o.append(_rect(96, 248, 152, 16, fill="url(#h6)", sw=1.2))
    o.append(_rect(86, 162, 12, 110, fill="url(#h6)", sw=1.2))
    o.append(_rect(108, 186, 140, 62, fill=PAPER, sw=0.6))
    o.append(_rect(232, 170, 16, 96, fill="url(#h6)", sw=1.2))
    o.append(_rect(352, 170, 16, 96, fill="url(#h6)", sw=1.2))
    o.append(_rect(248, 184, 104, 64, fill=PAPER, sw=0.6))

    # Plug on the stem and the seat ring with its central opening.
    o.append(_poly([(286, 202), (314, 202), (306, 244), (294, 244)],
                   fill="#c9d4de", sw=1.3, close=True))
    o.append(_rect(270, 246, 18, 10, fill="#9aa9b8", sw=1.0))
    o.append(_rect(312, 246, 18, 10, fill="#9aa9b8", sw=1.0))

    # Converging passage from the chamber down to the throat.
    o.append(_poly([(248, 248), (270, 256), (278, 304), (248, 304)],
                   fill="url(#h6)", sw=1.1, close=True))
    o.append(_poly([(352, 248), (330, 256), (322, 304), (352, 304)],
                   fill="url(#h6)", sw=1.1, close=True))
    o.append(_poly([(270, 256), (288, 256), (294, 304), (278, 304)],
                   fill="url(#h6)", sw=1.0, close=True))
    o.append(_poly([(312, 256), (330, 256), (322, 304), (306, 304)],
                   fill="url(#h6)", sw=1.0, close=True))

    # Enlarged downstream pipe with its flange.
    o.append(_rect(248, 304, 104, 118, fill=PAPER, sw=0.6))
    o.append(_rect(232, 304, 16, 118, fill="url(#h6)", sw=1.2))
    o.append(_rect(352, 304, 16, 118, fill="url(#h6)", sw=1.2))
    o.append(_rect(216, 304, 32, 12, fill="url(#h6)", sw=1.2))
    o.append(_rect(352, 304, 32, 12, fill="url(#h6)", sw=1.2))

    # The sonic jet: converging cone then spreading plume.
    o.append(_poly([(288, 256), (312, 256), (307, 304), (293, 304)],
                   fill="#dbeaf5", sw=1.2, color=BLUE, close=True))
    o.append(_poly([(293, 304), (307, 304), (318, 350), (282, 350)],
                   fill="#e7f0f7", sw=1.0, color=BLUE, dash="3,2", close=True))

    # Turbulent eddies dissolving into the enlarged outlet.
    for cx, cy, r in ((272, 344, 4), (288, 358, 5), (306, 350, 3),
                      (320, 366, 4), (278, 378, 3), (298, 382, 5),
                      (316, 390, 3), (286, 400, 4), (306, 404, 3)):
        o.append(_circle(cx, cy, r, fill="#ffffff", sw=0.9, color=GREY))
    for d in ("M262,356 q6,-7 12,0 q6,7 12,0",
              "M300,368 q7,-8 14,0 q7,8 14,0",
              "M274,390 q6,-7 12,0 q6,7 12,0"):
        o.append(_path(d, fill="none", sw=0.9, color=GREY))

    # Flow arrows: inlet, jet through the seat, downstream turbulence.
    o.append(_arrow(36, 218, 106, 218, sw=1.6, color=GREEN))
    o.append(_arrow(300, 262, 300, 300, sw=1.5, color=BLUE))
    o.append(_arrow(300, 354, 300, 414, sw=1.4, color=BLUE, dash="4,3"))

    # Bilingual part callouts.
    o.append(T(30, 170, "Đầu vào / Inlet", 8.0, anchor="start", color=GREEN))
    _lead(o, 252, 104, 172, 96, "Nắp van / Bonnet")
    _lead(o, 300, 58, 392, 54, "Thân van / Stem", anchor="start")
    _lead(o, 308, 214, 392, 186, "Nút van / Plug", anchor="start")
    _lead(o, 272, 250, 172, 264, "Đế van / Seat")
    _lead(o, 238, 330, 132, 320, "Cửa ra mở rộng / Enlarged outlet")
    _lead(o, 326, 368, 392, 356, "Xoáy nhiễu loạn / Turbulent eddies",
          anchor="start")

    # Four bilingual velocity zones with the printed labels.
    o.append(T(500, 250, "Vùng vận tốc / Velocity zones", 7.4,
               anchor="middle", color=GREY))
    o.append(T(150, 226, "1 = Mach 0.1", 8.2,
               anchor="middle", color=INK, weight="600"))
    o.append(_line(312, 284, 386, 282, sw=0.8, color=GREY))
    o.append(T(392, 284, "2 = Mach 1", 8.2,
               anchor="start", color=INK, weight="600"))
    o.append(_line(302, 324, 386, 326, sw=0.8, color=GREY))
    o.append(T(392, 328, "3 = Mach 1", 8.2,
               anchor="start", color=INK, weight="600"))
    o.append(_line(320, 398, 386, 402, sw=0.8, color=GREY))
    o.append(T(392, 404, "4 = Mach 0.1", 8.2,
               anchor="start", color=INK, weight="600"))

    # In-SVG bilingual strip.
    o.append(T(340, 438, "Hình 32-2 · Van góc có cửa ra mở rộng và vùng nhiễu loạn",
               7.0, color=INK))
    o.append(T(340, 452, "Figure 32-2 · Angle valve with an enlarged outlet and turbulent eddies",
               7.0, color=GREY))

    title = "Sơ đồ van góc có cửa ra mở rộng và các vùng vận tốc"
    caption_vi = ("Hình 32-2 · Sơ đồ cắt van góc có cửa ra mở rộng. Các gradient "
                  "vận tốc xấp xỉ là 1 = Mach 0.1, 2 = Mach 1, 3 = Mach 1 và "
                  "4 = Mach 0.1.")
    caption_en = ("Figure 32-2 · Schematic view of an angle valve with an enlarged "
                  "outlet. The approximate velocity gradients are 1 = Mach 0.1, "
                  "2 = Mach 1, 3 = Mach 1, and 4 = Mach 0.1.")
    aria_vi = ("Sơ đồ cắt van góc: đầu vào bên trái, nắp van, thân van và nút van, "
               "dòng tia hội tụ qua đế van, ống ra mở rộng chứa các xoáy nhiễu loạn; "
               "bốn vùng vận tốc được ghi nhãn 1 = Mach 0.1, 2 = Mach 1, 3 = Mach 1 "
               "và 4 = Mach 0.1.")
    aria_en = ("Section through an angle valve: inlet from the left, bonnet, stem "
               "and plug, a converging jet through the seat, an enlarged downstream "
               "pipe filled with turbulent eddies; four velocity zones labelled "
               "1 = Mach 0.1, 2 = Mach 1, 3 = Mach 1 and 4 = Mach 0.1.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)
