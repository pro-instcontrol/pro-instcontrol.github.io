# -*- coding: utf-8 -*-
"""Vector figures for Chapter 1 "Transducers - I" of Prasad, Jayaswal &
Priye, *Instrumentation and Process Control* (I.K. International, 2019),
printed pp. 1-62 (PDF pp. 13-74).

The source carries 51 numbered figures (Fig. 1.1 - Fig. 1.51).  The originals
are images in the PDF; only their captions survive in the text layer.  Every
figure is therefore redrawn here as a compact, simplified vector schematic
consistent with its caption and the surrounding prose.  Multi-panel originals
(e.g. Fig. 1.18, 1.23, 1.24, 1.26, 1.39, 1.41) keep their sub-panel letters.

Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through ``_fig()``.
All SVG text is escaped with ``esc()`` before it reaches a tag.
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
W, H = 680, 250


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


def T(x, y, s, size=8.0, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _mk(n, o, title, cvi, cen, avi, aen, h=H):
    """Close a figure with a bilingual number strip and build the 5-tuple."""
    o.append(T(W / 2.0, h - 5, "Hình 1.%d   ·   Figure 1.%d" % (n, n),
               6.4, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 1.%d · %s" % (n, cvi),
        "Figure 1.%d · %s" % (n, cen),
        avi, aen)


def _b(x, y, w, h, label, fill="#eef3fb", size=7.8, color=INK):
    """A compact labelled block; ``\n`` starts a new line."""
    lines = str(label).split("\n")
    o = [_rect(x, y, w, h, fill)]
    y0 = y + h / 2.0 - (len(lines) - 1) * size * 0.55 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * size * 1.15, ln, size, color=color))
    return "".join(o)


def _ar(x1, y1, x2, y2, color=BLUE, sw=1.6):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color)


def _frame(x0, y0, w, h, xr, yr, xt, yt, xlab, ylab, logy=False):
    """Axes box, grid, ticks and titles; returns (markup, mx, my) mappers."""
    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * w

    if logy:
        la, lb = math.log10(yr[0]), math.log10(yr[1])

        def my(v):
            return y0 + h - (math.log10(v) - la) / (lb - la) * h
    else:
        def my(v):
            return y0 + h - (v - yr[0]) / (yr[1] - yr[0]) * h

    o = [_rect(x0, y0, w, h, fill="#fbfaf7", sw=1.0)]
    for v, lab in yt:
        py = my(v)
        o.append(_line(x0, py, x0 + w, py, sw=0.5, color="#dcdcdc"))
        o.append(_line(x0 - 3, py, x0, py, sw=0.7))
        o.append(T(x0 - 6, py + 2.3, lab, 6.4, anchor="end", color=GREY))
    for v, lab in xt:
        px = mx(v)
        o.append(_line(px, y0 + h, px, y0 + h + 3, sw=0.7))
        o.append(T(px, y0 + h + 11, lab, 6.4, color=GREY))
    o.append(T(x0 + w / 2.0, y0 + h + 23, xlab, 7.4, color=INK))
    o.append('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
             'style="font:7.4px Inter,Helvetica,sans-serif;fill:%s">%s</text>'
             % (x0 - 30, y0 + h / 2.0, x0 - 30, y0 + h / 2.0, INK, esc(ylab)))
    return "".join(o), mx, my


def _series(points, mx, my, color, dot=1.9, dash=""):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=1.7, color=color, dash=dash)]
    for px, py in pts:
        o.append(_circle(px, py, dot, fill=color, sw=0))
    return "".join(o)


def _legend(items, x, y, w=76, lh=13, size=7.0):
    h = 11 + len(items) * lh
    o = [_rect(x, y, w, h, fill="#ffffff", sw=0.9)]
    for i, (col, lab) in enumerate(items):
        yy = y + 13 + i * lh
        o.append(_line(x + 5, yy - 2, x + 20, yy - 2, sw=2.0, color=col))
        o.append(T(x + 24, yy, lab, size, anchor="start"))
    return "".join(o)


def _wavey(x, y0, amp, n, step=9, phase=0):
    """A little corrugation / coil line, useful in several sensor cross-sections."""
    return [(x + i * step, y0 + (amp if i % 2 else -amp) * (1 if phase == 0 else -1))
            for i in range(n + 1)]


# ===========================================================================
@_reg
def fig_f01():
    """Fig. 1.1 - Transducer block."""
    o = [_defs()]
    o.append(_b(46, 72, 150, 66, "Environmental changes\nheat, pressure, light"))
    o.append(_b(246, 72, 160, 66, "Changes in resistance,\ninductance, capacitance,\nshape, colour"))
    o.append(_b(448, 72, 110, 66, "Conditioning\nsystem"))
    o.append(_ar(196, 105, 246, 105))
    o.append(_ar(406, 105, 448, 105))
    o.append(_ar(503, 138, 503, 166))
    o.append(_b(330, 166, 340, 44,
                "Available output: 4-20 mA or 1-5 V electrical; 0.2-1.0 kg/cm2 pneumatic",
                fill="#fff6e5", size=7.6))
    return _mk(1, o, "Figure 1.1 - Transducer block",
               "Sơ đồ khối bộ chuyển đổi: thay đổi môi trường gây thay đổi điện trở, cảm ứng, điện dung, hình dạng hoặc màu, được hệ thống điều hòa biến thành đầu ra 4-20 mA, 1-5 V hoặc 0,2-1,0 kg/cm2.",
               "Transducer block: environmental changes produce changes in resistance, inductance, capacitance, shape or colour, which a conditioning system turns into a 4-20 mA, 1-5 V or 0.2-1.0 kg/cm2 output.",
               "Sơ đồ khối ba tầng của bộ chuyển đổi với đầu ra điện và khí nén",
               "Three-block transducer diagram with electrical and pneumatic outputs")


@_reg
def fig_f02():
    """Fig. 1.2 - Transmitter block."""
    o = [_defs()]
    for x, lab in ((44, "Process\ninput"), (216, "Input\ntransducers"),
                   (390, "Output\ntransducers"), (560, "Output signal")):
        o.append(_b(x, 88, 120, 58, lab))
    for a, b in ((164, 216), (336, 390), (510, 560)):
        o.append(_ar(a, 117, b, 117))
    return _mk(2, o, "Figure 1.2 - Transmitter block",
               "Sơ đồ khối bộ phát: đầu vào quá trình đi qua bộ chuyển đổi đầu vào và bộ chuyển đổi đầu ra để tạo tín hiệu đầu ra.",
               "Transmitter block: a process input passes through input and output transducers to produce an output signal.",
               "Sơ đồ bốn khối của bộ phát từ đầu vào quá trình đến tín hiệu đầu ra",
               "Four-block transmitter chain from process input to output signal")


@_reg
def fig_f03():
    """Fig. 1.3 - Thermocouple (two fused dissimilar metals)."""
    o = [_defs()]
    o.append(_poly([(120, 90), (300, 90)], sw=4.0, color=BLUE))
    o.append(_poly([(300, 90), (340, 120), (300, 150)], sw=4.0, color=RED))
    o.append(_poly([(300, 150), (120, 150)], sw=4.0, color=BLUE))
    o.append(_circle(340, 120, 7, fill=RED, sw=0.8))
    o.append(T(340, 100, "Tip fused / hot junction", 7.4, anchor="middle"))
    o.append(_b(60, 176, 110, 40, "Measurement\ncircuit", fill="#fff6e5", size=7.2))
    o.append(_line(120, 90, 120, 176, sw=1.2, color=BLUE))
    o.append(_line(120, 150, 120, 176, sw=1.2, color=BLUE))
    o.append(T(115, 80, "Platinum", 7.4, anchor="end", color=BLUE))
    o.append(T(115, 166, "Rhodium", 7.4, anchor="end", color=RED))
    o.append(T(380, 150, "Cold junction at the measurement circuit", 7.2, anchor="start", color=GREY))
    return _mk(3, o, "Figure 1.3 - Thermocouple",
               "Cặp nhiệt điện gồm hai kim loại khác nhau hàn tại một đầu; đầu hàn là mối nóng còn hai đầu kia nối vào mạch đo tạo mối lạnh. Chênh nhiệt độ sinh ra thermo-emf.",
               "A thermocouple made of two dissimilar metals fused at one end: the fused tip is the hot junction, the other ends form the cold junction at the measuring circuit. The temperature difference induces a thermo-emf.",
               "Hai thanh kim loại hàn ở đầu, nối vào mạch đo",
               "Two metal rods fused at one tip and connected to a measuring circuit")


@_reg
def fig_f04():
    """Fig. 1.4 - Wheatstone bridge with RTD element."""
    o = [_defs()]
    A, B, C, D = (250, 42), (430, 42), (250, 178), (430, 178)
    for p, q in ((A, B), (B, C), (C, D), (D, A)):
        o.append(_line(p[0], p[1], q[0], q[1], sw=1.2))
    o.append(_line(340, 42, 340, 178, sw=1.0, color=GREY))
    o.append(_rect(238, 74, 70, 16, fill="#ffffff"))
    o.append(T(273, 86, "Rb", 7.4))
    o.append(_rect(238, 132, 70, 16, fill="#ffffff"))
    o.append(T(273, 144, "Rx (RTD)", 7.4))
    o.append(_rect(398, 74, 64, 16, fill="#ffffff"))
    o.append(T(430, 86, "Rc", 7.4))
    o.append(_rect(398, 132, 64, 16, fill="#ffffff"))
    o.append(T(430, 144, "Ra", 7.4))
    o.append(_b(482, 88, 84, 44, "DE\ndetector", fill="#fff6e5", size=7.4))
    o.append(T(250, 32, "A", 7.6))
    o.append(T(430, 32, "B", 7.6))
    o.append(T(340, 196, "Eb supply across A-B; out-of-balance current through DE", 7.2, color=GREY))
    return _mk(4, o, "Figure 1.4 - Wheatstone bridge RTD system",
               "Cầu Wheatstone có phần tử RTD ở một nhánh và đầu dò DE ở đường chéo; dòng mất cân bằng qua DE phản ánh sự thay đổi điện trở do nhiệt độ.",
               "A Wheatstone bridge with the RTD in one arm and a detecting element DE on the diagonal; the out-of-balance current through DE reflects the temperature-induced resistance change.",
               "Cầu Wheatstone với RTD và đầu dò ở đường chéo",
               "Wheatstone bridge with an RTD arm and a diagonal detector")


@_reg
def fig_f05():
    """Fig. 1.5 - NO and NC relay contacts."""
    o = [_defs()]
    o.append(T(175, 44, "NO-contact of relay", 7.8))
    o.append(_line(105, 150, 105, 92, sw=1.6))
    o.append(_line(245, 150, 245, 92, sw=1.6))
    o.append(_circle(105, 92, 3.2, fill=INK))
    o.append(_circle(245, 92, 3.2, fill=INK))
    o.append(_line(105, 92, 233, 76, sw=2.0, color=BLUE))
    o.append(T(175, 176, "open at rest", 7.0, color=GREY))
    o.append(T(505, 44, "NC-contact of relay", 7.8))
    o.append(_line(435, 150, 435, 92, sw=1.6))
    o.append(_line(575, 150, 575, 92, sw=1.6))
    o.append(_circle(435, 92, 3.2, fill=INK))
    o.append(_circle(575, 92, 3.2, fill=INK))
    o.append(_line(435, 92, 575, 92, sw=2.0, color=RED))
    o.append(T(505, 176, "closed at rest", 7.0, color=GREY))
    return _mk(5, o, "Figure 1.5 - NO and NC relay contacts",
               "Tiếp điểm thường mở NO và tiếp điểm thường đóng NC của rơ le điện từ: hai vị trí rời rạc như công tắc bật-tắt, được coi là bộ chuyển đổi số.",
               "The normally open (NO) and normally closed (NC) contacts of an electromagnetic relay: two distinct positions like an on-off switch, regarded as a digital transducer.",
               "Hai tiếp điểm rơ le NO và NC ở trạng thái nghỉ",
               "Relay NO and NC contacts in their rest states")


@_reg
def fig_f06():
    """Fig. 1.6 - Pressure transducer plus ADC."""
    o = [_defs()]
    for x, w, lab in ((40, 110, "Input\nvariable"), (200, 140, "Pressure\ntransducer"),
                      (390, 80, "ADC"), (520, 120, "Digital\noutput")):
        o.append(_b(x, 92, w, 56, lab))
    for a, b in ((150, 200), (340, 390), (470, 520)):
        o.append(_ar(a, 120, b, 120))
    o.append(T(340, 176, "primary transducer", 7.0, color=GREY))
    o.append(T(430, 176, "secondary transducer", 7.0, color=GREY))
    return _mk(6, o, "Figure 1.6 - Pressure transducer with ADC",
               "Bộ chuyển đổi số: tín hiệu tương tự từ bộ chuyển đổi áp suất (sơ cấp) được ADC (thứ cấp) đổi thành đầu ra số.",
               "A digital transducer: the analog signal from a pressure transducer (primary) is converted by an ADC (secondary) into a digital output.",
               "Sơ đồ đầu vào, bộ chuyển đổi áp suất, ADC và đầu ra số",
               "Block chain of input, pressure transducer, ADC and digital output")


@_reg
def fig_f07():
    """Fig. 1.7 - Pressure control loop."""
    o = [_defs()]
    o.append(_b(28, 60, 108, 48, "Uncontrolled\ninlet", fill="#fff6e5"))
    o.append(_b(172, 60, 106, 48, "Passive pressure\ntransducer"))
    o.append(_b(320, 60, 78, 48, "Transmitter\nunit"))
    o.append(_b(440, 34, 74, 44, "PIC"))
    o.append(_b(440, 96, 92, 48, "Inverse\ntransducer", fill="#fff6e5"))
    o.append(_b(566, 96, 90, 48, "Final control\nelement"))
    o.append(_ar(136, 84, 172, 84))
    o.append(_ar(278, 84, 320, 84))
    o.append(_ar(398, 84, 440, 58))
    o.append(_line(477, 78, 477, 96, sw=1.4, color=RED))
    o.append(_ar(532, 120, 566, 120, color=RED))
    o.append(_b(540, 172, 116, 40, "Controlled output\nto another system", fill="#eaf6ee", size=7.2))
    o.append(_ar(611, 144, 611, 172, color=GREEN))
    o.append(_line(172, 92, 172, 192, sw=1.0, color=GREY, dash="4 4"))
    o.append(_line(172, 192, 540, 192, sw=1.0, color=GREY, dash="4 4"))
    o.append(_ar(540, 192, 540, 172, color=GREY))
    return _mk(7, o, "Figure 1.7 - Pressure control loop",
               "Vòng điều khiển áp suất: tín hiệu từ bộ chuyển đổi áp suất thụ động qua bộ phát tới bộ điều khiển PIC; bộ chuyển đổi ngược nằm trước phần tử điều khiển cuối để điều khiển van khí nén.",
               "Pressure control loop: the passive pressure transducer signal goes through a transmitter to a PIC; the inverse transducer sits before the final control element to drive a pneumatic control valve.",
               "Sơ đồ vòng điều khiển áp suất có bộ chuyển đổi ngược trước van",
               "Pressure loop with an inverse transducer ahead of the final control valve")


@_reg
def fig_f08():
    """Fig. 1.8 - Zero error."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (5, "5"), (10, "10")],
                        [(0, "0"), (5, "5"), (10, "10")], "Input", "Output")
    o.append(fr)
    o.append(_series([(0, 0), (10, 10)], mx, my, BLUE, dot=0))
    o.append(_series([(0, 2), (10, 12)], mx, my, RED, dot=0))
    o.append(_line(mx(7), my(7), mx(7), my(9), sw=1.0, color=GREY))
    o.append(T(mx(7) + 5, my(8), "e", 8.0, anchor="start", color=RED))
    o.append(_legend([(BLUE, "Desired curve"), (RED, "Actual curve")], 540, 70))
    return _mk(8, o, "Figure 1.8 - Zero error",
               "Sai số gốc: đường thực tế song song và lệch một lượng e so với đường mong muốn trong toàn bộ thang đo.",
               "Zero error: the actual curve is parallel to the desired curve but offset by a fixed amount e over the whole scale.",
               "Đồ thị đường thực tế lệch song song với đường mong muốn",
               "Plot of an actual curve parallel-offset from the desired curve")


@_reg
def fig_f09():
    """Fig. 1.9 - Sensitivity error."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 10), (0, 14),
                        [(0, "0"), (5, "5"), (10, "10")],
                        [(0, "0"), (5, "5"), (10, "10")], "Input", "Output")
    o.append(fr)
    o.append(_series([(0, 0), (10, 10)], mx, my, BLUE, dot=0))
    o.append(_series([(0, 0), (10, 13)], mx, my, RED, dot=0))
    o.append(T(mx(8), my(12.6), "k po", 7.6, anchor="start", color=RED))
    o.append(T(mx(6), my(6.3), "po", 7.6, anchor="end", color=BLUE))
    o.append(_legend([(BLUE, "Desired po"), (RED, "Actual k po")], 540, 70))
    return _mk(9, o, "Figure 1.9 - Sensitivity error",
               "Sai số độ nhạy: đầu ra thực tế bằng k po thay vì po trong toàn bộ thang đo, với k là hằng số.",
               "Sensitivity error: the output is k po instead of po over the whole scale, where k is a constant.",
               "Đồ thị hai đường dốc khác nhau cắt nhau tại gốc tọa độ",
               "Plot of two different slopes meeting at the origin")


@_reg
def fig_f10():
    """Fig. 1.10 - Non-conformity error."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (5, "5"), (10, "10")],
                        [(0, "0"), (5, "5"), (10, "10")], "Input", "Output")
    o.append(fr)
    o.append(_series([(0, 0), (10, 10)], mx, my, BLUE, dot=0))
    o.append(_series([(0, 0), (2, 2.6), (4, 4.1), (6, 6.6), (8, 8.0), (10, 10)],
                     mx, my, RED))
    o.append(_legend([(BLUE, "Desired curve"), (RED, "Actual curve")], 540, 70))
    return _mk(10, o, "Figure 1.10 - Non-conformity error",
               "Sai số không phù hợp: hàm chuyển đổi thực tế khác với hàm mong muốn ở hầu hết các giá trị đầu vào.",
               "Non-conformity error: the actual transducer function differs from the desired one for almost all input values.",
               "Đồ thị đường thực tế cong khác với đường thẳng mong muốn",
               "Plot of a curved actual response against the desired straight line")


@_reg
def fig_f11():
    """Fig. 1.11 - Hysteresis error."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (5, "5"), (10, "10")],
                        [(0, "0"), (5, "5"), (10, "10")], "Input", "Output")
    o.append(fr)
    o.append(_series([(0, 0), (2, 2.1), (4, 4.0), (6, 6.2), (8, 8.1), (10, 10)],
                     mx, my, BLUE))
    o.append(_series([(10, 8.4), (8, 6.9), (6, 5.2), (4, 3.3), (2, 1.5), (0, 0)],
                     mx, my, RED))
    o.append(T(mx(6), my(6.2), "increasing", 7.0, anchor="start", color=BLUE))
    o.append(T(mx(4), my(4.0), "decreasing", 7.0, anchor="end", color=RED))
    o.append(_legend([(BLUE, "Increasing order"), (RED, "Decreasing order")], 540, 70, w=92))
    return _mk(11, o, "Figure 1.11 - Hysteresis error",
               "Sai số trễ: đường đi theo chiều tăng khác với chiều giảm, các giá trị giảm cao hơn các giá trị tăng.",
               "Hysteresis error: the increasing-order curve differs from the decreasing-order curve, the decreasing values being higher than the increasing ones.",
               "Vòng lặp trễ giữa đường tăng và đường giảm",
               "Hysteresis loop between increasing and decreasing curves")


@_reg
def fig_f12():
    """Fig. 1.12 - Gain versus frequency."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 10), (0, 1),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (0.5, "0.5"), (1, "1")], "Frequency", "Gain")
    o.append(fr)
    o.append(_series([(0, 1), (4, 1), (5.5, 0.96), (7, 0.74), (8.5, 0.36), (10, 0.1)],
                     mx, my, BLUE))
    o.append(_line(mx(5.5), my(0), mx(5.5), my(1), sw=0.8, color=GREY, dash="4 4"))
    o.append(T(mx(5.5) + 4, my(0.9), "cut-off", 7.0, anchor="start", color=GREY))
    return _mk(12, o, "Figure 1.12 - Gain fall-off with frequency",
               "Đặc tính tần số: với đầu vào hình sin, đầu ra giữ dạng sin nhưng khi tần số vượt một giá trị nhất định thì độ khuếch đại giảm và dịch pha tăng.",
               "Frequency response: a sinusoidal input gives a sinusoidal output, but beyond a certain frequency the gain drops and the phase shift increases.",
               "Đồ thị độ khuếch đại phẳng rồi giảm dần theo tần số",
               "Plot of flat gain that rolls off as frequency rises")


@_reg
def fig_f13():
    """Fig. 1.13 - Spiral spring."""
    o = [_defs()]
    pts = []
    for i in range(90):
        t = i * 0.30
        r = 5 + 1.55 * t
        pts.append((300 + r * math.cos(t), 112 + r * math.sin(t)))
    o.append(_poly(pts, sw=2.2, color=BLUE))
    o.append(_ar(300, 34, 300, 66, color=RED))
    o.append(T(312, 50, "Force applied", 7.6, anchor="start", color=RED))
    o.append(_line(300, 194, 370, 194, sw=1.0, color=GREY))
    o.append(_line(300, 188, 300, 200, sw=1.0, color=GREY))
    o.append(_line(370, 188, 370, 200, sw=1.0, color=GREY))
    o.append(T(335, 190, "D", 8.0, color=INK))
    return _mk(13, o, "Figure 1.13 - Spiral spring",
               "Lò xo dạng xoắn ốc chịu lực tác dụng; độ lệch Q tỉ lệ với mô-men xung lực Td.",
               "A spiral-shaped spring under an applied force; the deflection Q is related to the applied torque Td.",
               "Lò xo xoắn ốc có mũi tên lực và kích thước D",
               "Spiral spring with a force arrow and dimension D")


@_reg
def fig_f14():
    """Fig. 1.14 - Helical spring."""
    o = [_defs()]
    pts = []
    for i in range(41):
        x = 160 + i * 9
        y = 112 + (-26 if i % 2 == 0 else 26)
        pts.append((x, y))
    o.append(_poly(pts, sw=2.2, color=BLUE))
    o.append(_line(160, 86, 160, 138, sw=1.6, color=INK))
    o.append(_line(520, 86, 520, 138, sw=1.6, color=INK))
    o.append(_ar(340, 40, 340, 74, color=RED))
    o.append(T(352, 56, "Fa", 8.0, anchor="start", color=RED))
    o.append(_line(160, 174, 520, 174, sw=1.0, color=GREY))
    o.append(T(340, 170, "displacement D", 7.4, color=GREY))
    return _mk(14, o, "Figure 1.14 - Helical spring",
               "Lò xo dạng xoắn ống chịu lực Fa; dịch chuyển D tùy thuộc lực, đường kính vòng dây, số vòng và mô-đun trượt.",
               "A helical spring under force Fa; the displacement D depends on the force, coil diameters, number of turns and shear modulus.",
               "Lò xo xoắn ống nằm ngang có lực tác dụng",
               "Horizontal helical spring with an applied force")


@_reg
def fig_f15():
    """Fig. 1.15 - Proving ring."""
    o = [_defs()]
    o.append(_circle(340, 110, 58, fill="#eef3fb", sw=2.0))
    o.append(_circle(340, 110, 42, fill="none", sw=1.0, color="#9ab6cc"))
    o.append(_ar(340, 26, 340, 52, color=RED))
    o.append(_ar(340, 194, 340, 168, color=RED))
    o.append(T(352, 44, "Fa", 8.0, anchor="start", color=RED))
    o.append(T(352, 184, "Fa", 8.0, anchor="start", color=RED))
    o.append(_line(282, 110, 398, 110, sw=0.8, color=GREY, dash="4 4"))
    o.append(T(340, 104, "d", 8.0))
    o.append(T(386, 80, "θ", 9.0, color=BLUE))
    return _mk(15, o, "Figure 1.15 - Proving ring",
               "Vòng đo lực (ring dynamometer): lực Fa ép vào vòng tạo ứng suất chu vi; biến dạng được đo bằng căng kế.",
               "A proving ring (ring dynamometer): forces Fa create circumferential stress; the resulting strains are measured with strain gauges.",
               "Vòng tròn chịu hai lực ép đối nhau",
               "Circular proving ring loaded by two opposing forces")


@_reg
def fig_f16():
    """Fig. 1.16 - Flexure arm."""
    o = [_defs()]
    o.append(_rect(230, 42, 220, 58, fill="#dbe4ec"))
    o.append(T(340, 76, "Free body", 8.0))
    o.append(_rect(230, 172, 220, 34, fill="#dbe4ec"))
    o.append(T(340, 193, "Fixed base / brazed to the surface", 7.2))
    o.append(_rect(334, 100, 12, 72, fill="#fdf3e6", sw=1.4))
    o.append(T(346, 138, "Thin flexible steel strip", 7.4, anchor="start"))
    o.append(_circle(340, 102, 3.0, fill=INK))
    o.append(_circle(340, 170, 3.0, fill=INK))
    o.append(_ar(450, 74, 450, 104, color=RED))
    o.append(T(462, 90, "Fa", 7.8, anchor="start", color=RED))
    return _mk(16, o, "Figure 1.16 - Flexure arm",
               "Cánh uốn là dải thép mỏng được hàn ở hai đầu vào khối tự do; nó nhận toàn bộ chuyển vị và gần như không ma sát.",
               "A flexure arm is a thin steel strip brazed at both ends to a free body; it takes up the deflection and moves almost without friction.",
               "Dải thép mỏng nối khối tự do với đế cố định",
               "Thin steel strip linking a free body to a fixed base")


@_reg
def fig_f17():
    """Fig. 1.17 - Cantilever beam."""
    o = [_defs()]
    o.append(_rect(158, 48, 24, 130, fill="url(#h6)", sw=1.2))
    o.append(_line(182, 112, 540, 112, sw=4.0, color="#8fa6b8"))
    o.append(_poly([(182, 112), (280, 118), (380, 138), (470, 166), (540, 190)],
                   sw=1.8, color=RED, dash="5 4"))
    o.append(_ar(540, 146, 540, 186, color=RED))
    o.append(T(520, 140, "Fa", 8.0, anchor="end", color=RED))
    o.append(T(360, 128, "Displaced state", 7.2, anchor="start", color=RED))
    o.append(_line(540, 200, 540, 216, sw=0.8, color=GREY))
    o.append(T(548, 212, "d", 7.8, anchor="start"))
    return _mk(17, o, "Figure 1.17 - Cantilever beam",
               "Dầm công xôn được gắn cứng một đầu; lực Fa ở đầu tự do sinh mô-men uốn, độ lệch d lớn nhất ở đầu tự do còn ứng suất lớn nhất ở đầu cố định.",
               "A cantilever beam fixed at one end: force Fa at the free end creates a bending moment; deflection d is greatest at the free end and strain greatest at the fixed end.",
               "Dầm một đầu cố định với đường cong biến dạng",
               "Cantilever beam fixed at one end with a deflected outline")


@_reg
def fig_f18():
    """Fig. 1.18 - Bourdon tube shapes (a)-(d)."""
    o = [_defs()]
    # (a) C shape
    cpts = [(340 + 62 * math.cos(math.radians(a)), 112 + 62 * math.sin(math.radians(a)))
            for a in range(30, 330, 6)]
    o.append(_poly(cpts, sw=5.0, color=BLUE))
    o.append(_circle(cpts[0][0], cpts[0][1], 3, fill=INK))
    o.append(T(340, 200, "(a) C shape", 7.6))
    o.append(T(340, 216, "up to 225 degrees", 6.8, color=GREY))
    # (b) spiral
    spts = [(140 + (5 + 2.0 * t) * math.cos(t), 112 + (5 + 2.0 * t) * math.sin(t))
            for t in [i * 0.35 for i in range(52)]]
    o.append(_poly(spts, sw=2.4, color=BLUE))
    o.append(T(140, 200, "(b) Spiral shape", 7.6))
    # (c) second spiral / multi-turn
    s2 = [(330 + (4 + 1.6 * t) * math.cos(t), 112 + (4 + 1.6 * t) * math.sin(t))
          for t in [i * 0.38 for i in range(50)]]
    o.append(_poly(s2, sw=2.2, color=GREEN))
    o.append(T(330, 200, "(c) Spiral shape", 7.6))
    # (d) helical
    for i in range(7):
        o.append(_ellipse(540 + i * 12, 112, 12, 30, fill="none", sw=1.8, color=BLUE))
    o.append(T(560, 200, "(d) Helical shape", 7.6))
    o.append(T(340, 34, "Sealed end = tip; open end admits the measurement fluid", 7.4, color=GREY))
    return _mk(18, o, "Figure 1.18 - Bourdon tube shapes",
               "Ống Bourdon có bốn dạng: chữ C, xoắn ốc, xoắn ốc nhiều vòng và xoắn ống; đầu bịt kín là đầu dịch chuyển, đầu mở nhận chất đo.",
               "Bourdon tubes in four forms: C-shape, spiral, multi-turn spiral and helical; the sealed end is the tip that moves, the open end admits the measured fluid.",
               "Bốn dạng ống Bourdon chữ C, xoắn ốc và xoắn ống",
               "Four Bourdon tube forms: C, spiral and helical")


@_reg
def fig_f19():
    """Fig. 1.19(a),(b) - Flat and corrugated diaphragm."""
    o = [_defs()]
    o.append(_rect(70, 72, 26, 76, fill="url(#h6)", sw=1.2))
    o.append(_rect(204, 72, 26, 76, fill="url(#h6)", sw=1.2))
    o.append(_line(96, 110, 204, 110, sw=2.4, color=BLUE))
    o.append(T(150, 176, "(a) Flat diaphragm", 7.8))
    o.append(_line(120, 118, 120, 138, sw=0.8, color=GREY))
    o.append(T(126, 132, "t", 7.6))
    o.append(_line(96, 152, 204, 152, sw=0.8, color=GREY))
    o.append(T(150, 148, "r", 7.6))
    o.append(_rect(392, 72, 26, 76, fill="url(#h6)", sw=1.2))
    o.append(_rect(526, 72, 26, 76, fill="url(#h6)", sw=1.2))
    o.append(_poly(_wavey(418, 110, 12, 10, step=11), sw=2.2, color=BLUE))
    o.append(T(472, 176, "(b) Corrugated diaphragm", 7.8))
    o.append(T(340, 40, "Metallic circular strip clamped at the periphery", 7.6, color=GREY))
    return _mk(19, o, "Figure 1.19 - Flat and corrugated diaphragm",
               "Màng ngăn phẳng và màng gờ sóng được kẹp quanh chu vi; gờ sóng tăng diện tích nên dịch chuyển lớn hơn.",
               "Flat and corrugated diaphragms clamped at the periphery; corrugation increases the area and therefore the overall displacement.",
               "Mặt cắt màng phẳng và màng có gờ sóng",
               "Cross-sections of a flat diaphragm and a corrugated diaphragm")


@_reg
def fig_f20():
    """Fig. 1.20 - Corrugation shapes."""
    o = [_defs()]
    panels = [
        ("(a) Sawtooth", [(40 + i * 12, 116 + (-14 if i % 2 else 14)) for i in range(21)]),
        ("(b) Trapezoidal", None),
        ("(c) Sinusoidal", None),
    ]
    o.append(_poly(panels[0][1], sw=2.0, color=BLUE))
    o.append(T(160, 166, panels[0][0], 7.6))
    trap = []
    for i in range(20):
        x = 270 + i * 10
        trap.append((x, 116 + (-14 if (i % 4) in (1, 2) else 14)))
    o.append(_poly(trap, sw=2.0, color=BLUE))
    o.append(T(360, 166, "(b) Trapezoidal", 7.6))
    sin = [(480 + i * 8, 116 - 15 * math.sin(i * 0.65)) for i in range(27)]
    o.append(_poly(sin, sw=2.0, color=BLUE))
    o.append(T(570, 166, "(c) Sinusoidal", 7.6))
    o.append(T(340, 60, "Corrugation increases the effective area and displacement", 7.8, color=GREY))
    return _mk(20, o, "Figure 1.20 - Corrugation shapes",
               "Ba dạng gờ sóng của màng ngăn: răng cưa, hình thang và hình sin.",
               "Three corrugation shapes for a diaphragm: sawtooth, trapezoidal and sinusoidal.",
               "Ba dạng gờ sóng răng cưa, hình thang và hình sin",
               "Sawtooth, trapezoidal and sinusoidal corrugation profiles")


@_reg
def fig_f21():
    """Fig. 1.21 - Capsule element."""
    o = [_defs()]
    o.append(_poly(_wavey(210, 92, 10, 12, step=20), sw=2.0, color=BLUE))
    o.append(_poly(_wavey(210, 148, 10, 12, step=20, phase=1), sw=2.0, color=RED))
    o.append(_line(210, 92, 210, 148, sw=2.0, color=INK))
    o.append(_line(450, 92, 450, 148, sw=2.0, color=INK))
    o.append(_ar(330, 48, 330, 82, color=GREEN))
    o.append(T(342, 62, "Inlet: process pressure applied", 7.4, anchor="start", color=GREEN))
    o.append(_ar(520, 120, 580, 120, color=RED))
    o.append(T(550, 112, "Displacement", 7.2, color=RED))
    return _mk(21, o, "Figure 1.21 - Diaphragm capsule",
               "Nang màng gồm hai màng gờ sóng hàn kín quanh chu vi; một đầu nhận áp suất chất lỏng, đầu kia lấy chuyển vị gấp đôi màng đơn.",
               "A diaphragm capsule is two corrugated diaphragms sealed at the periphery; one end receives the fluid pressure and the other takes up a displacement twice that of a single diaphragm.",
               "Hai màng gờ sóng ghép thành nang kín",
               "Two corrugated diaphragms joined into a sealed capsule")


@_reg
def fig_f22():
    """Fig. 1.22 - Bellows element."""
    o = [_defs()]
    o.append(_poly(_wavey(220, 110, 20, 14, step=20), sw=2.0, color=BLUE))
    o.append(_line(220, 90, 220, 130, sw=3.0, color=INK))
    o.append(_ar(220, 46, 220, 88, color=GREEN))
    o.append(T(234, 64, "Pa", 8.0, anchor="start", color=GREEN))
    o.append(_ar(500, 110, 568, 110, color=RED))
    o.append(T(534, 102, "Displacement", 7.4, color=RED))
    o.append(T(370, 168, "Bellows", 8.4))
    return _mk(22, o, "Figure 1.22 - Bellows element",
               "Ống sóng (bellows) là vỏ mỏng có nhiều nếp gấp; một đầu bịt kín lấy chuyển vị, đầu kia hở nhận áp suất chất lỏng.",
               "A bellows is a thin flexible shell with convolutions; one end is sealed to take up displacement and the other is open to the applied fluid pressure.",
               "Ống sóng có nhiều nếp gấp với áp suất và chuyển vị",
               "Convoluted bellows with pressure input and displacement output")


@_reg
def fig_f23():
    """Fig. 1.23(a),(b),(c) - Strain states of a gage."""
    o = [_defs()]
    for cx, lab, col in ((135, "(a) Unstrained", BLUE),
                         (340, "(b) Compression", RED),
                         (545, "(c) Tension", GREEN)):
        o.append(_rect(cx - 66, 84, 132, 60, fill="#eef3fb", sw=1.4))
        o.append(T(cx, 108, "A1", 7.8))
        o.append(T(cx, 166, lab, 7.8, color=col))
    o.append(_line(50, 76, 220, 76, sw=0.8, color=GREY))
    o.append(T(135, 68, "L1", 7.8, color=GREY))
    o.append(T(340, 108, "L1 - ΔL   /   A1 + ΔA", 7.2))
    o.append(T(545, 108, "L1 + ΔL   /   A1 - ΔA", 7.2))
    return _mk(23, o, "Figure 1.23 - Strain states of a gage element",
               "Ba trạng thái của phần tử căng kế: không biến dạng, nén (chiều dài giảm, tiết diện tăng) và kéo (chiều dài tăng, tiết diện giảm).",
               "Three states of a strain-gage element: unstrained, under compression (length decreases, area increases) and under tension (length increases, area decreases).",
               "Ba hình chữ nhật biểu diễn trạng thái nén và kéo",
               "Three rectangles showing compressed and stretched states")


@_reg
def fig_f24():
    """Fig. 1.24(a)-(e) - Forms of wire strain gages."""
    o = [_defs()]
    # (a) linear flat grid
    grid = []
    for i in range(9):
        y = 68 + i * 8
        grid.extend([(60, y), (150, y)])
        if i < 8:
            grid.append((150 if i % 2 == 0 else 60, y + 8))
    o.append(_poly(grid, sw=1.4, color=BLUE))
    o.append(T(105, 158, "(a) Linear flat grid", 7.0))
    # (b) rosette
    for ang in (0, 45, 90):
        r = 40
        x1, y1 = 270 + r * math.cos(math.radians(ang)), 110 - r * math.sin(math.radians(ang))
        o.append(_line(270 - r * math.cos(math.radians(ang)), 110 + r * math.sin(math.radians(ang)),
                       x1, y1, sw=2.0, color=BLUE))
    o.append(T(270, 158, "(b) Rosette type", 7.0))
    # (c) helical
    o.append(_poly(_wavey(380, 110, 14, 12, step=13), sw=1.8, color=BLUE))
    o.append(T(460, 158, "(c) Helical", 7.0))
    # (d) bonded foil
    o.append(_rect(512, 66, 120, 86, fill="#fdf3e6", sw=1.0))
    foil = []
    for i in range(7):
        y = 74 + i * 10
        foil.extend([(522, y), (622, y)])
        if i < 6:
            foil.append((622 if i % 2 == 0 else 522, y + 10))
    o.append(_poly(foil, sw=1.3, color=BLUE))
    o.append(T(572, 158, "(d) Bonded foil", 7.0))
    # (e) unbonded
    for px in (90, 150, 210):
        o.append(_rect(px - 5, 176, 10, 26, fill="#dbe4ec", sw=1.0))
    for px in (120, 180):
        o.append(_rect(px - 5, 176, 10, 26, fill="#dbe4ec", sw=1.0))
    o.append(_line(95, 182, 175, 196, sw=1.4, color=BLUE))
    o.append(_line(155, 182, 215, 196, sw=1.4, color=RED))
    o.append(T(155, 220, "(e) Unbonded strain gage", 7.0))
    return _mk(24, o, "Figure 1.24 - Forms of wire strain gages",
               "Năm dạng căng kế dây: lưới phẳng thẳng, kiểu hoa thị, kiểu xoắn ốc, lá kim loại dán và kiểu không dán.",
               "Five forms of wire strain gages: linear flat grid, rosette, helical, bonded foil and unbonded types.",
               "Năm dạng bố trí của căng kế dây và lá kim loại",
               "Five configurations of wire and foil strain gages")


@_reg
def fig_f25():
    """Fig. 1.25 - Metal foil strain gage."""
    o = [_defs()]
    o.append(_rect(180, 58, 320, 130, fill="#fdf3e6", sw=1.2))
    foil = []
    for i in range(11):
        y = 68 + i * 10
        foil.extend([(196, y), (484, y)])
        if i < 10:
            foil.append((484 if i % 2 == 0 else 196, y + 10))
    o.append(_poly(foil, sw=1.6, color=BLUE))
    o.append(T(340, 204, "Metal foil strain gage - grid on an insulating backing", 7.6, color=GREY))
    return _mk(25, o, "Figure 1.25 - Metal foil strain gage",
               "Căng kế lá kim loại: lưới dẫn được chế tạo trên nền cách điện, có độ tản nhiệt và độ dán tốt hơn loại dây.",
               "A metal foil strain gage: a conductive grid formed on an insulating backing, with better heat dissipation and bonding than the wire type.",
               "Lưới lá kim loại trên nền cách điện",
               "Metal foil grid on an insulating backing")


@_reg
def fig_f26():
    """Fig. 1.26 - Semiconductor strain gage constructions."""
    o = [_defs()]
    labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]
    for i in range(6):
        cx = 130 + (i % 3) * 205
        cy = 78 + (i // 3) * 84
        o.append(_rect(cx - 70, cy - 26, 140, 52, fill="#eef3fb", sw=1.2))
        o.append(_line(cx - 52, cy + 8, cx + 52, cy + 8, sw=2.4, color=BLUE))
        for j in (-1, 1):
            o.append(_circle(cx + j * 52, cy + 8, 3.2, fill=INK))
        o.append(T(cx, cy - 8, labels[i], 7.6))
    o.append(T(340, 218, "Doped silicon bars utilizing the piezoresistive effect", 7.2, color=GREY))
    return _mk(26, o, "Figure 1.26 - Semiconductor strain gage types",
               "Sáu dạng chế tạo căng kế bán dẫn dùng thanh silic pha tạp, hoạt động theo hiệu ứng áp điện trở.",
               "Six constructions of semiconductor strain gages using doped silicon bars and the piezoresistive effect.",
               "Sáu dạng căng kế bán dẫn dạng thanh",
               "Six semiconductor strain gage bar configurations")


@_reg
def fig_f27():
    """Fig. 1.27 - RTD resistance-temperature characteristics."""
    o = [_defs()]
    fr, mx, my = _frame(90, 36, 420, 150, (0, 700), (0, 3.2),
                        [(0, "0"), (200, "200"), (400, "400"), (600, "600")],
                        [(1, "Ro"), (2, "2Ro"), (3, "3Ro")], "Temperature C", "Rt")
    o.append(fr)
    o.append(_series([(0, 1), (200, 1.29), (400, 1.57), (600, 1.85)], mx, my, BLUE, dot=0))
    o.append(_series([(0, 1), (160, 1.43), (400, 1.8)], mx, my, GREEN, dot=0))
    o.append(_series([(0, 1), (100, 1.4), (200, 1.8), (300, 2.4), (400, 3.1)], mx, my, RED))
    o.append(T(mx(520), my(1.7), "Platinum", 7.0, anchor="start", color=BLUE))
    o.append(T(mx(300), my(1.5), "Copper", 7.0, anchor="start", color=GREEN))
    o.append(T(mx(300), my(2.4), "Nickel", 7.0, anchor="start", color=RED))
    return _mk(27, o, "Figure 1.27 - RTD characteristics",
               "Đặc tính Rt theo nhiệt độ của ba vật liệu làm RTD: bạch kim tuyến tính, đồng gần tuyến tính và niken phi tuyến sau 50 °C.",
               "Resistance-versus-temperature characteristics of three RTD materials: platinum linear, copper nearly linear and nickel non-linear beyond 50 C.",
               "Đồ thị điện trở tăng theo nhiệt độ cho bạch kim, đồng, niken",
               "Plot of resistance rising with temperature for platinum, copper and nickel")


@_reg
def fig_f28():
    """Fig. 1.28 - Thermocouple Seebeck loop."""
    o = [_defs()]
    o.append(_line(150, 70, 530, 70, sw=4.0, color=BLUE))
    o.append(_line(530, 70, 530, 160, sw=4.0, color=RED))
    o.append(_line(530, 160, 150, 160, sw=4.0, color=BLUE))
    o.append(_line(150, 160, 150, 70, sw=4.0, color=RED))
    o.append(_circle(530, 115, 6, fill=RED, sw=0.8))
    o.append(T(530, 50, "Hot junction", 7.6))
    o.append(T(150, 186, "Cold junction", 7.6))
    o.append(T(340, 62, "Iron", 7.6, color=BLUE))
    o.append(T(340, 178, "Copper", 7.6, color=BLUE))
    o.append(_ar(300, 70, 360, 70, color=GREEN))
    o.append(T(340, 116, "current flows when junctions differ in temperature", 7.0, color=GREY))
    return _mk(28, o, "Figure 1.28 - Seebeck thermocouple loop",
               "Vòng dây gồm hai kim loại khác nhau (sắt và đồng); khi hai mối nối ở nhiệt độ khác nhau sẽ có dòng điện chạy.",
               "A loop of two dissimilar metals (iron and copper); when the two junctions are held at different temperatures a current flows.",
               "Vòng kim loại kép có mối nóng và mối lạnh",
               "Two-metal loop with hot and cold junctions")


@_reg
def fig_f29():
    """Fig. 1.29 - Thermoelectric diagram."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 410, 146, (0, 10), (0, 10),
                        [(0, "0"), (T1v := 2, "T1"), (T2v := 7, "T2")],
                        [], "Temperature", "Thermoelectric power")
    o.append(fr)
    o.append(_poly([(mx(0), my(2)), (mx(10), my(6))], sw=1.8, color=BLUE))
    o.append(_poly([(mx(0), my(5)), (mx(10), my(9))], sw=1.8, color=RED))
    o.append(_poly([(mx(T1v), my(2 + 0.4 * T1v)), (mx(T2v), my(2 + 0.4 * T2v)),
                    (mx(T2v), my(5 + 0.4 * T2v)), (mx(T1v), my(5 + 0.4 * T1v))],
                   fill="#f6e6c8", sw=1.0, color=GREY, close=True))
    o.append(T(mx(4.5), my(6.2), "Area ABCD", 7.6))
    o.append(T(mx(8), my(2.2), "metal 1", 7.0, anchor="start", color=BLUE))
    o.append(T(mx(8), my(5.2), "metal 2", 7.0, anchor="start", color=RED))
    return _mk(29, o, "Figure 1.29 - Thermoelectric diagram",
               "Giản đồ nhiệt điện: trục tung là nhiệt điện thế, diện tích ABCD giữa hai đường kim loại cho emf sinh ra giữa T1 và T2.",
               "Thermoelectric diagram: thermoelectric power on the ordinate; the area ABCD between the two metal lines gives the emf generated between T1 and T2.",
               "Đồ thị nhiệt điện với hai đường kim loại và vùng ABCD",
               "Thermoelectric plot with two metal lines and area ABCD")


@_reg
def fig_f30():
    """Fig. 1.30 - emf per degree versus temperature."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 430, 150, (-200, 600), (-20, 20),
                        [(-200, "-200"), (-100, "-100"), (0, "0"), (100, "100"),
                         (200, "200"), (400, "400"), (600, "600")],
                        [(-20, "-20"), (-10, "-10"), (0, "0"), (10, "10"), (20, "20")],
                        "Temperature C", "mV/degree C")
    o.append(fr)
    lines = [
        ("Iron", -16, 0.036, BLUE), ("Steel", -10, 0.024, GREEN),
        ("Platinum", -4, 0.007, GREY), ("Zinc", 6, -0.012, RED),
        ("Silver", 8, -0.015, "#6c2a91"), ("Copper", 12, -0.044, "#b45309"),
        ("Lead", -2, -0.010, "#888888"),
    ]
    for name, b0, slope, col in lines:
        o.append(_series([(-200, b0 + slope * -200), (600, b0 + slope * 600)],
                         mx, my, col, dot=0))
        o.append(T(mx(560), my(b0 + slope * 560), name, 6.8, anchor="end", color=col))
    o.append(_line(mx(270), my(-20), mx(270), my(20), sw=0.8, color=GREY, dash="4 4"))
    o.append(T(mx(270) + 4, my(18), "270 C", 7.0, anchor="start", color=GREY))
    return _mk(30, o, "Figure 1.30 - Thermoelectric emf per degree",
               "Đồ thị emf trên mỗi độ theo nhiệt độ của sắt, thép, bạch kim, kẽm, bạc, đồng và chì; đường sắt và đồng cắt nhau ở 270 °C.",
               "Emf per degree versus temperature for iron, steel, platinum, zinc, silver, copper and lead; the iron and copper lines cross at 270 C.",
               "Nhiều đường kim loại cắt nhau trên đồ thị nhiệt điện",
               "Several metal lines crossing on a thermoelectric plot")


@_reg
def fig_f31():
    """Fig. 1.31 - Thermistor resistivity vs temperature."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 420, 150, (0, 100), (0, 10),
                        [(0, "0"), (25, "25"), (50, "50"), (75, "75"), (100, "100")],
                        [(2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Temperature", "Resistivity (ohm-metre)")
    o.append(fr)
    pts = [(t, 10 * math.exp(-0.035 * t)) for t in range(0, 101, 5)]
    o.append(_series(pts, mx, my, RED))
    o.append(T(mx(62), my(4), "approx. linear over a limited range", 7.0, color=GREY))
    return _mk(31, o, "Figure 1.31 - Thermistor resistivity characteristic",
               "Đặc tính điện trở suất giảm theo nhiệt độ của nhiệt trở; có thể coi là tuyến tính trong một dải hẹp.",
               "Thermistor resistivity falling with temperature; approximately linear over a limited operating range.",
               "Đường điện trở suất giảm dần theo nhiệt độ",
               "Curve of resistivity decreasing with temperature")


@_reg
def fig_f32():
    """Fig. 1.32 - Thermistor voltage vs current."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 420, 150, (0, 10), (0, 12),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (4, "4"), (8, "8"), (12, "12")],
                        "Current (microampere)", "Voltage")
    o.append(fr)
    o.append(_series([(0, 0), (2, 4), (4, 6), (6, 5.6), (8, 4), (10, 2.6)], mx, my, BLUE))
    o.append(_series([(0, 0), (2, 6), (4, 9), (6, 8.6), (8, 6.2), (10, 4)], mx, my, RED))
    o.append(T(mx(6.5), my(8), "ambient ta", 7.0, anchor="start", color=BLUE))
    o.append(T(mx(6.5), my(10.6), "other t1", 7.0, anchor="start", color=RED))
    return _mk(32, o, "Figure 1.32 - Thermistor voltage-current characteristic",
               "Đặc tính điện áp-dòng của nhiệt trở ở nhiệt độ môi trường ta và ở nhiệt độ khác t1, thể hiện vùng điện trở âm.",
               "Thermistor voltage-current curves at ambient temperature ta and at another temperature t1, showing the negative-resistance region.",
               "Hai đường điện áp-dòng có đoạn điện trở âm",
               "Two voltage-current curves with a negative-resistance region")


@_reg
def fig_f33():
    """Fig. 1.33 - Thermistor current vs time."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Time", "Current (mA)")
    o.append(fr)
    o.append(_series([(0, 1), (2, 1.1), (4, 1.6), (6, 3.4), (8, 5.4), (10, 5.6)], mx, my, BLUE))
    o.append(_series([(0, 2), (2, 2.2), (4, 3.4), (6, 6.4), (8, 8.4), (10, 8.6)], mx, my, RED))
    o.append(T(mx(8), my(5.6), "V1", 7.4, anchor="start", color=BLUE))
    o.append(T(mx(8), my(8.6), "V2", 7.4, anchor="start", color=RED))
    return _mk(33, o, "Figure 1.33 - Thermistor current-time characteristic",
               "Đặc tính dòng theo thời gian: cần một khoảng thời gian để nhiệt độ và dòng ổn định tăng lên; khoảng này đổi được bằng điện áp đặt vào.",
               "Current versus time: a finite interval is needed for the thermistor temperature and steady-state current to rise; the interval changes with the applied voltage.",
               "Hai đường dòng tăng dần theo thời gian cho V1 và V2",
               "Two current curves rising over time for V1 and V2")


@_reg
def fig_f34():
    """Fig. 1.34 - Capacitance versus gap length."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Gap length D", "Capacitance C")
    o.append(fr)
    o.append(_series([(d, 10 / (d + 1)) for d in [i * 0.5 for i in range(21)]], mx, my, BLUE))
    return _mk(34, o, "Figure 1.34 - Capacitance versus gap length",
               "Đồ thị điện dung C giảm phi tuyến theo khoảng cách D giữa hai bản cực; độ phi tuyến giảm khi dùng môi trường có hằng số điện môi lớn.",
               "Capacitance C falling non-linearly with the gap D between the plates; the non-linearity is reduced by a medium of high dielectric constant.",
               "Đường điện dung giảm dần theo khoảng cách bản cực",
               "Curve of capacitance decreasing with plate gap")


@_reg
def fig_f35():
    """Fig. 1.35 - Coaxial tube capacitive transducer."""
    o = [_defs()]
    o.append(_rect(180, 64, 300, 26, fill="#eef3fb", sw=1.4))
    o.append(_rect(180, 150, 300, 26, fill="#eef3fb", sw=1.4))
    o.append(_rect(200, 96, 260, 48, fill="#fdf3e6", sw=1.4))
    o.append(T(330, 120, "Stationary", 7.6))
    o.append(T(330, 78, "Movable", 7.6, color=BLUE))
    o.append(T(330, 196, "Dielectric material", 7.6, color=GREY))
    o.append(_ar(520, 108, 580, 108, color=RED))
    o.append(T(550, 100, "displacement", 6.8, color=RED))
    return _mk(35, o, "Figure 1.35 - Capacitive transducer with hollow tubes",
               "Bộ chuyển đổi điện dung dùng hai ống kim loại rỗng: một ống cố định, ống kia dịch chuyển tương đối làm điện dung thay đổi.",
               "A capacitive transducer using two hollow metal tubes: one stationary and the other moving relative to it, changing the capacitance.",
               "Hai ống kim loại rỗng lồng nhau có lớp điện môi",
               "Two nested hollow metal tubes with dielectric between them")


@_reg
def fig_f36():
    """Fig. 1.36 - Parallel plate capacitive transducer."""
    o = [_defs()]
    o.append(_rect(150, 82, 380, 14, fill="#dbe4ec", sw=1.2))
    o.append(_rect(150, 156, 380, 14, fill="#dbe4ec", sw=1.2))
    o.append(_rect(150, 96, 380, 60, fill="#fdf3e6", sw=0.8, stroke="#c9b48a"))
    o.append(T(340, 128, "Gap filled with dielectric material", 7.6))
    o.append(T(340, 70, "Stationary plate", 7.4, color=BLUE))
    o.append(T(340, 188, "Movable plate", 7.4, color=RED))
    return _mk(36, o, "Figure 1.36 - Parallel plate capacitive transducer",
               "Hai bản dẫn phẳng xếp lên nhau, khe hở giữa chúng chứa vật liệu điện môi; điện dung thay đổi khi tiết diện chồng lấp thay đổi.",
               "Two rectangular conducting plates stacked with a dielectric-filled gap; capacitance changes as the overlapping area changes.",
               "Hai bản cực phẳng có khe chứa điện môi",
               "Two parallel plates with a dielectric-filled gap")


@_reg
def fig_f37():
    """Fig. 1.37 - Capacitance versus area."""
    o = [_defs()]
    fr, mx, my = _frame(96, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Cross-sectional area A", "Capacitance C")
    o.append(fr)
    o.append(_series([(0, 0), (10, 10)], mx, my, BLUE, dot=0))
    return _mk(37, o, "Figure 1.37 - Capacitance versus area",
               "Đồ thị điện dung C thay đổi tuyến tính theo tiết diện chồng lấp A của hai bản cực.",
               "Capacitance C varying linearly with the overlapping cross-sectional area A of the plates.",
               "Đường thẳng điện dung tăng theo diện tích bản cực",
               "Straight line of capacitance rising with plate area")


@_reg
def fig_f38():
    """Fig. 1.38 - Piezoelectric transducer."""
    o = [_defs()]
    o.append(_rect(230, 66, 220, 110, fill="#fdf3e6", sw=1.4))
    o.append(_line(230, 90, 450, 90, sw=2.0, color=INK))
    o.append(_line(230, 152, 450, 152, sw=2.0, color=INK))
    o.append(T(340, 126, "Piezoelectric substance", 7.6))
    o.append(_ar(340, 22, 340, 64, color=RED))
    o.append(_ar(340, 220, 340, 178, color=RED))
    o.append(T(352, 44, "Fa", 8.0, anchor="start", color=RED))
    o.append(T(352, 208, "Fa", 8.0, anchor="start", color=RED))
    o.append(_line(470, 90, 540, 90, sw=1.4, color=BLUE))
    o.append(_line(470, 152, 540, 152, sw=1.4, color=BLUE))
    o.append(_circle(548, 90, 3, fill=BLUE))
    o.append(_circle(548, 152, 3, fill=BLUE))
    o.append(T(570, 122, "Ve", 8.4, color=BLUE))
    o.append(_line(206, 90, 206, 152, sw=0.8, color=GREY))
    o.append(T(194, 122, "y - Δy", 7.2, anchor="end", color=GREY))
    return _mk(38, o, "Figure 1.38 - Piezoelectric element",
               "Vật liệu áp điện đặt giữa hai điện cực: lực Fa gây biến dạng Δy và xuất hiện điện áp Ve tỉ lệ với điện tích sinh ra.",
               "A piezoelectric substance between two electrodes: force Fa causes deformation Δy and a voltage Ve proportional to the induced charge.",
               "Khối áp điện giữa hai điện cực chịu lực",
               "Piezoelectric block between electrodes under force")


@_reg
def fig_f39():
    """Fig. 1.39(a),(b) - Piezoelectric equivalent circuits."""
    o = [_defs()]
    # (a) charge generator with parallel C and R
    o.append(_circle(130, 118, 15, fill="none", sw=1.4))
    o.append(_ar(114, 118, 146, 118, color=BLUE, sw=1.0))
    o.append(T(130, 92, "qe", 7.6))
    o.append(_line(130, 133, 130, 170, sw=1.2))
    o.append(_line(130, 170, 240, 170, sw=1.2))
    o.append(_line(130, 103, 130, 70, sw=1.2))
    o.append(_line(130, 70, 240, 70, sw=1.2))
    o.append(_line(180, 70, 180, 100, sw=1.2))
    o.append(_line(172, 100, 188, 100, sw=2.0))
    o.append(_line(172, 106, 188, 106, sw=2.0))
    o.append(_line(180, 106, 180, 170, sw=1.2))
    o.append(_line(220, 70, 220, 100, sw=1.2))
    o.append(_rect(214, 100, 12, 40, fill="#ffffff", sw=1.2))
    o.append(_line(220, 140, 220, 170, sw=1.2))
    o.append(T(180, 190, "C", 7.6))
    o.append(T(220, 190, "R", 7.6))
    o.append(T(180, 216, "(a) Charge generator", 7.4))
    # (b) voltage source
    o.append(_circle(450, 118, 15, fill="none", sw=1.4))
    o.append(_line(444, 110, 456, 126, sw=1.8))
    o.append(T(450, 92, "Ve", 7.6))
    o.append(_line(450, 133, 450, 170, sw=1.2))
    o.append(_line(450, 170, 560, 170, sw=1.2))
    o.append(_line(450, 103, 450, 70, sw=1.2))
    o.append(_line(450, 70, 560, 70, sw=1.2))
    o.append(_line(500, 70, 500, 100, sw=1.2))
    o.append(_line(492, 100, 508, 100, sw=2.0))
    o.append(_line(492, 106, 508, 106, sw=2.0))
    o.append(_line(500, 106, 500, 170, sw=1.2))
    o.append(_line(540, 70, 540, 100, sw=1.2))
    o.append(_rect(534, 100, 12, 40, fill="#ffffff", sw=1.2))
    o.append(_line(540, 140, 540, 170, sw=1.2))
    o.append(T(500, 190, "C", 7.6))
    o.append(T(540, 190, "R", 7.6))
    o.append(T(500, 216, "(b) Voltage source", 7.4))
    return _mk(39, o, "Figure 1.39 - Piezoelectric equivalent circuits",
               "Mạch tương đương của bộ chuyển đổi áp điện: máy phát điện tích mắc song song với điện dung C và điện trở rò R, có thể thay bằng nguồn áp tương đương.",
               "Equivalent circuit of a piezoelectric transducer: a charge generator in parallel with capacitance C and leakage resistance R, replaceable by an equivalent voltage source.",
               "Hai mạch tương đương nguồn điện tích và nguồn điện áp",
               "Two equivalent circuits: charge generator and voltage source")


@_reg
def fig_f40():
    """Fig. 1.40 - Hall effect element."""
    o = [_defs()]
    o.append(_rect(220, 68, 240, 116, fill="#eef3fb", sw=1.4))
    o.append(_ar(160, 126, 220, 126, color=BLUE))
    o.append(T(176, 116, "Current", 7.4, anchor="start", color=BLUE))
    o.append(_ar(520, 126, 460, 126, color=BLUE))
    o.append(_ar(340, 30, 340, 66, color=GREEN))
    o.append(T(352, 48, "Magnetic field B", 7.4, anchor="start", color=GREEN))
    o.append(_circle(340, 126, 4, fill=INK))
    o.append(T(300, 156, "Hall terminal", 7.2, color=RED))
    o.append(T(402, 156, "Vh", 8.0, color=RED))
    o.append(_line(340, 126, 340, 184, sw=1.2, color=RED))
    o.append(T(340, 206, "Vh proportional to i B / t", 7.6, color=GREY))
    return _mk(40, o, "Figure 1.40 - Hall effect transducer",
               "Tấm dẫn có từ trường ngang và dòng điện chạy vuông góc; điện áp Hall Vh xuất hiện vuông góc với cả từ trường và dòng điện.",
               "A conducting plate with a transverse magnetic field and a perpendicular current; the Hall voltage Vh appears perpendicular to both field and current.",
               "Tấm dẫn có từ trường, dòng điện và hai đầu Hall",
               "Conducting plate with magnetic field, current and Hall terminals")


@_reg
def fig_f41():
    """Fig. 1.41(a),(b),(c) - Photovoltaic cell."""
    o = [_defs()]
    # (a) layered cross-section
    layers = [("Glass cover", "#dbe4ec"), ("Transparent adhesive", "#eaf2f8"),
              ("Anti-reflection coating", "#d6e8d6"), ("p-type layer", "#f3d9e6"),
              ("n-type layer", "#d9e6f6")]
    for i, (lab, col) in enumerate(layers):
        y = 50 + i * 20
        o.append(_rect(60, y, 190, 18, fill=col, sw=0.8))
        o.append(T(155, y + 12, lab, 6.8))
    for x in (80, 120, 160, 200, 230):
        o.append(_line(x, 50, x, 58, sw=2.0, color="#888"))
    o.append(_ar(155, 20, 155, 46, color="#b45309"))
    o.append(T(168, 34, "Incident light", 7.0, anchor="start", color="#b45309"))
    o.append(T(155, 164, "(a) Photovoltaic cell", 7.2))
    # (b) circuit model
    o.append(_line(320, 78, 400, 78, sw=1.2))
    o.append(_circle(360, 78, 15, fill="none", sw=1.2))
    o.append(_ar(346, 78, 374, 78, color=BLUE, sw=1.0))
    o.append(T(360, 56, "Ie", 7.2))
    o.append(_line(400, 78, 400, 150, sw=1.2))
    o.append(_rect(388, 100, 24, 30, fill="#ffffff", sw=1.2))
    o.append(T(424, 118, "C", 7.2))
    o.append(_line(400, 150, 320, 150, sw=1.2))
    o.append(T(360, 170, "(b) Circuit model", 7.2))
    # (c) I vs light intensity
    fr, mx, my = _frame(470, 56, 160, 100, (0, 10), (0, 10),
                        [], [], "Light intensity", "Current")
    o.append(fr)
    o.append(_series([(0, 0), (2, 2.2), (4, 4.6), (6, 6.6), (8, 8.4), (10, 10)], mx, my, BLUE))
    o.append(T(550, 170, "(c) Output current", 7.2))
    return _mk(41, o, "Figure 1.41 - Photovoltaic cell",
               "Pin quang điện gồm các lớp kính, keo trong suốt, lớp chống phản xạ và lớp bán dẫn p, n; mạch tương đương gồm nguồn dòng Ie và điện dung C, dòng ra tăng theo cường độ sáng.",
               "A photovoltaic cell with glass, transparent adhesive, anti-reflection coating and p/n layers; its model is a current source Ie with capacitance C, and output current rises with light intensity.",
               "Mặt cắt pin quang điện, mạch tương đương và đồ thị dòng theo sáng",
               "Solar-cell cross-section, equivalent circuit and current versus light plot")


@_reg
def fig_f42():
    """Fig. 1.42 - Photodiode circuit."""
    o = [_defs()]
    o.append(_rect(250, 66, 180, 116, fill="#eef3fb", sw=1.2))
    o.append(_poly([(300, 96), (300, 154)], sw=1.6, color=BLUE))
    o.append(_poly([(300, 112), (272, 96)], sw=1.6, color=BLUE))
    o.append(_poly([(300, 112), (328, 96)], sw=1.6, color=BLUE))
    o.append(_poly([(380, 96), (380, 154)], sw=1.6, color=RED))
    o.append(T(340, 138, "Photodiode", 7.6))
    o.append(_ar(250, 126, 170, 126, color=GREEN))
    o.append(T(200, 116, "Light Iλ", 7.4, anchor="start", color=GREEN))
    o.append(_line(430, 66, 500, 66, sw=1.2))
    o.append(_rect(488, 66, 16, 60, fill="#ffffff", sw=1.2))
    o.append(T(520, 98, "Rl", 7.6))
    o.append(_line(496, 126, 496, 182, sw=1.2))
    o.append(T(440, 200, "Eb bias supply", 7.4, color=GREY))
    return _mk(42, o, "Figure 1.42 - Photodiode circuit",
               "Photodiode mắc ngược qua điện trở tải Rl và nguồn Eb; dòng Iλ tăng khi cường độ chiếu sáng tăng.",
               "A reverse-biased photodiode with load resistor Rl and supply Eb; the current Iλ rises as incident light intensity increases.",
               "Mạch photodiode có điện trở tải và nguồn một chiều",
               "Photodiode circuit with load resistor and DC bias")


@_reg
def fig_f43():
    """Fig. 1.43 - Photodiode characteristics."""
    o = [_defs()]
    fr, mx, my = _frame(100, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Reverse voltage", "Current Iλ")
    o.append(fr)
    for col, off, lab in ((GREY, 0, "Dark"), (BLUE, 2, "Light 1"),
                          (GREEN, 5, "Light 2"), (RED, 8, "Light 3")):
        o.append(_series([(0, off), (2, off + 0.1), (5, off + 0.3), (8, off + 0.7), (10, off + 1.0)],
                         mx, my, col, dot=0))
        o.append(T(mx(9), my(off + 0.9), lab, 6.8, anchor="start", color=col))
    return _mk(43, o, "Figure 1.43 - Photodiode characteristics",
               "Họ đặc tính dòng theo điện áp ngược của photodiode: dòng tăng theo cường độ sáng, intensity 3 lớn hơn intensity 2, 1 và mức tối.",
               "Photodiode current versus reverse voltage: current rises with light intensity, intensity 3 greater than 2, 1 and dark.",
               "Bốn đường đặc tính cho mức tối và ba cường độ sáng",
               "Four characteristic curves for dark and three light levels")


@_reg
def fig_f44():
    """Fig. 1.44 - Phototransistor."""
    o = [_defs()]
    o.append(_line(340, 60, 340, 172, sw=1.6, color=INK))
    o.append(_line(340, 84, 450, 54, sw=1.6, color=BLUE))
    o.append(_line(340, 148, 450, 178, sw=1.6, color=RED))
    o.append(_line(340, 100, 430, 100, sw=1.6, color=GREY))
    o.append(_ar(430, 100, 400, 90, color=GREY, sw=1.0))
    o.append(_ar(430, 100, 400, 110, color=GREY, sw=1.0))
    o.append(_ar(360, 20, 360, 92, color="#b45309"))
    o.append(T(374, 34, "Light", 7.6, anchor="start", color="#b45309"))
    o.append(T(470, 50, "C", 7.6, color=BLUE))
    o.append(T(470, 182, "E", 7.6, color=RED))
    o.append(T(448, 94, "B", 7.6, color=GREY))
    return _mk(44, o, "Figure 1.44 - Phototransistor",
               "Phototransistor là transistor có tiếp điểm base-emitter (P-N) được chiếu sáng; ánh sáng sinh cặp electron-lỗ và tạo dòng collectơ.",
               "A phototransistor is a transistor whose base-emitter (P-N) junction is exposed to light; photons generate electron-hole pairs and drive collector current.",
               "Ký hiệu phototransistor có mũi tên ánh sáng tới",
               "Phototransistor symbol with an incident-light arrow")


@_reg
def fig_f45():
    """Fig. 1.45 - Phototransistor characteristics."""
    o = [_defs()]
    fr, mx, my = _frame(100, 36, 420, 150, (0, 10), (0, 10),
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
                        "Collector voltage", "Collector current")
    o.append(fr)
    for col, off, lab in ((GREY, 0, "Dark"), (BLUE, 2, "Light 1"),
                          (GREEN, 5, "Light 2"), (RED, 8, "Light 3")):
        o.append(_series([(0, off), (1, off + 1.2), (3, off + 1.7),
                          (6, off + 1.9), (10, off + 2.0)], mx, my, col, dot=0))
        o.append(T(mx(7), my(off + 2.1), lab, 6.8, anchor="start", color=col))
    return _mk(45, o, "Figure 1.45 - Phototransistor characteristics",
               "Đặc tính dòng collectơ theo áp collectơ của phototransistor cho bốn mức chiếu sáng; sáng càng mạnh dòng càng lớn.",
               "Phototransistor collector current versus collector voltage at four light levels; stronger illumination gives a larger current.",
               "Bốn đường dòng collectơ theo áp collectơ",
               "Four collector-current curves versus collector voltage")


@_reg
def fig_f46():
    """Fig. 1.46 - Flapper-nozzle system."""
    o = [_defs()]
    o.append(_b(40, 56, 120, 46, "Measurement\ninput"))
    o.append(_b(40, 130, 120, 46, "Measurement\nbellow"))
    o.append(_b(480, 56, 140, 46, "Feedback\nbellow"))
    o.append(_line(160, 153, 250, 153, sw=1.4, color=BLUE))
    o.append(_line(160, 79, 250, 79, sw=1.4, color=BLUE))
    o.append(_poly([(250, 96), (400, 116)], sw=3.0, color=INK))
    o.append(_circle(250, 116, 7, fill="#dbe4ec", sw=1.2))
    o.append(T(250, 138, "Fulcrum", 7.0))
    o.append(_rect(392, 104, 16, 26, fill="#dbe4ec", sw=1.2))
    o.append(_line(400, 130, 400, 168, sw=1.4, color=BLUE))
    o.append(T(400, 182, "Nozzle", 7.2))
    o.append(_rect(356, 168, 88, 14, fill="#ffffff", sw=1.0))
    o.append(T(400, 178, "Restriction / orifice", 6.4))
    o.append(_line(304, 175, 356, 175, sw=1.4, color=GREEN))
    o.append(T(300, 168, "Air supply 1.4 kg/cm2", 6.8, anchor="end", color=GREEN))
    o.append(_ar(480, 79, 400, 116, color=RED))
    o.append(T(540, 120, "Output proportional to input", 7.0, color=RED))
    return _mk(46, o, "Figure 1.46 - Flapper-nozzle system",
               "Hệ thống vòi phun-cánh van khí nén: lực đầu vào qua ống đo bị cân bằng bởi ống phản hồi; cánh van che vòi phun tạo áp suất ngược tỉ lệ với đầu vào.",
               "A pneumatic flapper-nozzle system: the input force through the measurement bellow is restrained by a feedback bellow; the flapper caps the nozzle and generates a back-pressure proportional to the input.",
               "Sơ đồ cánh van, vòi phun, ống đo và ống phản hồi",
               "Schematic of flapper, nozzle, measurement and feedback bellows")


@_reg
def fig_f47():
    """Fig. 1.47 - Nozzle back-pressure versus gap."""
    o = [_defs()]
    fr, mx, my = _frame(100, 36, 420, 150, (0, 0.08), (0.2, 1.0),
                        [(0, "0"), (0.025, "0.025"), (0.05, "0.05")],
                        [(0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"), (0.8, "0.8"), (1.0, "1.0")],
                        "Gap between nozzle and flapper (mm)", "Nozzle back pressure (kg/cm2)")
    o.append(fr)
    o.append(_series([(0, 1.0), (0.005, 1.0), (0.012, 0.95), (0.02, 0.75),
                      (0.03, 0.48), (0.04, 0.32), (0.05, 0.26), (0.08, 0.2)], mx, my, BLUE))
    o.append(_line(mx(0), my(0.5), mx(0.025), my(0.5), sw=0.8, color=GREY, dash="4 4"))
    o.append(T(340, 54, "near-linear between 0.5 and 1.0 kg/cm2", 7.0, color=GREY))
    return _mk(47, o, "Figure 1.47 - Nozzle back-pressure characteristic",
               "Đồ thị áp suất ngược vòi phun theo khe hở: tuyến tính tốt giữa 0,5 và 1,0 kg/cm2 và gần tuyến tính trong dải 0,2 đến 1,0 kg/cm2.",
               "Nozzle back-pressure versus flapper gap: perfect linearity between 0.5 and 1.0 kg/cm2 and approximate linearity from 0.2 to 1.0 kg/cm2.",
               "Đường áp suất ngược giảm theo khe hở vòi phun",
               "Curve of nozzle back-pressure falling as the flapper gap grows")


@_reg
def fig_f48():
    """Fig. 1.48 - Pneumatic-electric conversion."""
    o = [_defs()]
    o.append(_b(36, 92, 120, 50, "Pneumatic signal\ninput 0.2-1.0"))
    o.append(_b(190, 92, 86, 50, "Bellow"))
    o.append(_b(310, 60, 110, 44, "Input spring"))
    o.append(_b(310, 118, 110, 44, "Force beam"))
    o.append(_b(456, 60, 110, 44, "Detector"))
    o.append(_b(456, 118, 110, 44, "Oscillator"))
    o.append(_b(36, 172, 150, 40, "24 V DC supply", fill="#fff6e5", size=7.2))
    o.append(_ar(156, 117, 190, 117))
    o.append(_ar(276, 117, 310, 140))
    o.append(_ar(420, 140, 456, 140))
    o.append(_ar(566, 82, 600, 82, color=RED))
    o.append(T(600, 76, "4-20 mA output", 7.0, anchor="end", color=RED))
    return _mk(48, o, "Figure 1.48 - Pneumatic-electric conversion",
               "Bộ chuyển đổi khí nén-điện: áp suất đầu vào làm ống sóng dịch chuyển, khe hở bộ dò thay đổi cảm ứng của mạch dao động, tạo đầu ra 4-20 mA.",
               "Pneumatic-electric converter: input pressure moves a bellow, the detector air gap changes the oscillator inductance, producing a 4-20 mA output.",
               "Sơ đồ bộ dò, dầm lực, ống sóng và mạch dao động",
               "Block chain of detector, force beam, bellow and oscillator")


@_reg
def fig_f49():
    """Fig. 1.49 - Electro-pneumatic conversion."""
    o = [_defs()]
    o.append(_b(30, 92, 120, 50, "4-20 mA\ncurrent input"))
    o.append(_rect(180, 70, 140, 96, fill="#eef3fb", sw=1.2))
    o.append(T(250, 100, "Permanent magnet", 7.2))
    o.append(_line(220, 120, 280, 120, sw=2.4, color=BLUE))
    o.append(T(250, 142, "coil", 7.0))
    o.append(_ar(150, 117, 180, 117))
    o.append(_b(350, 52, 110, 44, "Flapper-nozzle"))
    o.append(_b(350, 116, 110, 44, "Restrictor / relay"))
    o.append(_ar(320, 117, 350, 138))
    o.append(_ar(460, 138, 510, 138, color=RED))
    o.append(_b(510, 116, 150, 44, "Pneumatic output\n0.2-1.0 kg/cm2", fill="#fff6e5", size=7.2))
    o.append(T(250, 190, "24 V DC supply to the coil - force in a magnetic field", 7.0, color=GREY))
    return _mk(49, o, "Figure 1.49 - Electro-pneumatic conversion",
               "Bộ chuyển đổi điện-khí nén: dòng 4-20 mA chạy trong cuộn dây đặt trong nam châm vĩnh cửu tạo dịch chuyển, qua cánh van-vòi phun cho đầu ra 0,2-1,0 kg/cm2.",
               "Electro-pneumatic converter: a 4-20 mA current in a coil inside a permanent magnet produces displacement, which through a flapper-nozzle gives a 0.2-1.0 kg/cm2 output.",
               "Sơ đồ cuộn dây nam châm và cơ cấu cánh van-vòi phun",
               "Block chain of magnet coil and flapper-nozzle assembly")


@_reg
def fig_f50():
    """Fig. 1.50 - Wheatstone bridge RTD system."""
    o = [_defs()]
    A, B, C, D = (210, 52), (330, 52), (210, 160), (330, 160)
    for p, q in ((A, B), (B, C), (C, D), (D, A)):
        o.append(_line(p[0], p[1], q[0], q[1], sw=1.2))
    o.append(_line(270, 52, 270, 160, sw=1.0, color=GREY))
    for x, y, lab in ((198, 84, "Rb"), (198, 130, "Rx"),
                      (322, 84, "Rc"), (322, 130, "Ra")):
        o.append(_rect(x, y, 24, 14, fill="#ffffff", sw=1.0))
        o.append(T(x + 12, y + 10, lab, 6.8))
    o.append(_b(370, 84, 96, 44, "Amplifier", size=7.4))
    o.append(_b(496, 84, 150, 44, "Output 4-20 mA", fill="#fff6e5", size=7.4))
    o.append(_ar(334, 106, 370, 106))
    o.append(_ar(466, 106, 496, 106))
    o.append(T(270, 184, "RTD in one arm; servo can vary Rb to balance the bridge", 7.0, color=GREY))
    return _mk(50, o, "Figure 1.50 - Wheatstone bridge RTD system",
               "Hệ thống RTD-cầu Wheatstone: dòng mất cân bằng được khuếch đại thành tín hiệu 4-20 mA; servo điều chỉnh Rb để cân bằng cầu.",
               "Wheatstone-bridge RTD system: the out-of-balance current is amplified into a 4-20 mA signal; a servo varies Rb to balance the bridge.",
               "Cầu Wheatstone có RTD, bộ khuếch đại và đầu ra 4-20 mA",
               "Wheatstone bridge with RTD, amplifier and 4-20 mA output")


@_reg
def fig_f51():
    """Fig. 1.51 - Potentiometer-thermocouple system."""
    o = [_defs()]
    steps = [(36, "Thermocouple"), (170, "Preamplifier"), (304, "Convertor"),
             (438, "Servoamplifier"), (572, "A.C. servomotor")]
    for x, lab in steps:
        o.append(_b(x, 70, 116, 48, lab, size=7.2))
    for a in (152, 286, 420, 554):
        o.append(_ar(a, 94, a + 18, 94))
    o.append(_b(400, 160, 150, 44, "Potentiometer", fill="#fff6e5", size=7.4))
    o.append(_ar(630, 118, 550, 160, color=RED))
    o.append(_line(400, 182, 300, 182, sw=1.2, color=GREY, dash="4 4"))
    o.append(_line(300, 182, 300, 94, sw=1.2, color=GREY, dash="4 4"))
    o.append(T(348, 174, "Mechanical coupling", 6.8, color=GREY))
    o.append(T(340, 220, "Reference winding and control winding of the potentiometer", 7.0, color=GREY))
    return _mk(51, o, "Figure 1.51 - Potentiometer-thermocouple system",
               "Hệ thống chiết áp-thermocouple: tín hiệu mV của cặp nhiệt được tiền khuếch đại, đổi sang xoay chiều, khuếch đại servo và dùng động cơ cân bằng chiết áp để ghi nhiệt độ.",
               "Potentiometer-thermocouple system: the thermocouple millivolt signal is preamplified, converted to AC, servo-amplified and used to drive a motor that balances the potentiometer for temperature recording.",
               "Sơ đồ thermocouple, bộ đổi, servo và chiết áp tự cân bằng",
               "Chain of thermocouple, converter, servo and self-balancing potentiometer")
