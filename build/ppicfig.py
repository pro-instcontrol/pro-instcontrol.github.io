# -*- coding: utf-8 -*-
"""Vector figures for Chapter 1 of the Handbook on Power Plant
Instrumentation and Control (L. N. Jalali ed., Bibliotex, 2019),
printed pp. 1-12 (PDF pp. 17-28).

The source chapter carries five numbered figures:

  Figure 1 (p. 4) - overview of the catalytic dissolved-oxygen removal
                    process: make-up tank, hydrogen cylinder, mixing
                    column, catalytic reactor, treated-water outlet.
  Figure 2 (p. 4) - outlet oxygen vs. temperature, two pressure curves.
  Figure 3 (p. 5) - outlet oxygen vs. pressure, three temperature curves
                    (semi-log ordinate).
  Figure 4 (p. 9) - remaining oxygen vs. time, three contact-time curves
                    (semi-log ordinate).
  Figure 5 (p. 9) - remaining oxygen vs. time, three inlet-DO curves
                    (semi-log ordinate).

All are redrawn as simplified vectors preserving the topology, axis
scales, series, markers and labels of the originals.  Each function
returns the standard 5-tuple ``(svg, caption_vi, caption_en, aria_vi,
aria_en)`` through ``_fig()``, and every piece of SVG text passes
through ``esc()`` before it reaches a tag.
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


def _vlabel(x, y, s, size=8.0, color=GREY):
    """Vertical axis title, rotated about its anchor point."""
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, x, y, size, color, esc(s)))


def _frame(x0, y0, W, H, xr, yr, xt, yt, xlab, ylab, logy=False):
    """Axes box, grid, ticks and titles; returns (markup, mx, my) mappers."""
    def mx(v):
        return x0 + (v - xr[0]) / (xr[1] - xr[0]) * W

    if logy:
        la, lb = math.log10(yr[0]), math.log10(yr[1])

        def my(v):
            return y0 + H - (math.log10(v) - la) / (lb - la) * H
    else:
        def my(v):
            return y0 + H - (v - yr[0]) / (yr[1] - yr[0]) * H

    o = [_rect(x0, y0, W, H, fill="#fbfaf7", sw=1.1)]
    for v, lab in yt:
        py = my(v)
        o.append(_line(x0, py, x0 + W, py, sw=0.6, color="#d8d8d8"))
        o.append(_line(x0 - 3, py, x0, py, sw=0.8))
        o.append(T(x0 - 6, py + 2.4, lab, 6.8, anchor="end", color=GREY))
    for v, lab in xt:
        px = mx(v)
        o.append(_line(px, y0 + H, px, y0 + H + 3, sw=0.8))
        o.append(T(px, y0 + H + 12, lab, 6.8, color=GREY))
    o.append(T(x0 + W / 2.0, y0 + H + 26, xlab, 8.0, color=INK))
    o.append(_vlabel(x0 - 34, y0 + H / 2.0, ylab, 8.0))
    return "".join(o), mx, my


def _legend(items, x, y, lh=15, size=7.6, w=78):
    """A small bordered legend of (color, label) pairs."""
    h = 12 + len(items) * lh
    o = [_rect(x, y, w, h, fill="#ffffff", sw=1.0)]
    for i, (col, lab) in enumerate(items):
        yy = y + 15 + i * lh
        o.append(_line(x + 6, yy - 2, x + 24, yy - 2, sw=2.2, color=col))
        o.append(_circle(x + 15, yy - 2, 2.2, fill=col, sw=0))
        o.append(T(x + 29, yy, lab, size, anchor="start"))
    return "".join(o)


def _series(points, mx, my, color, dot=2.4):
    pts = [(mx(a), my(b)) for a, b in points]
    o = [_poly(pts, sw=1.9, color=color)]
    for px, py in pts:
        o.append(_circle(px, py, dot, fill=color, sw=0))
    return "".join(o)


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """Figure 1 (source p. 4) - overview of the catalytic process."""
    w, h = 680, 350
    o = [_defs()]
    # make-up tank (blue bottle with a neck)
    tank = [(60, 196), (60, 122), (94, 96), (94, 72), (124, 72),
            (124, 96), (158, 122), (158, 196)]
    o.append(_poly(tank, fill="#0e9fc9", sw=1.4, close=True))
    o.append(_rect(78, 132, 62, 20, fill="#ffffff", sw=0.8))
    o.append(T(109, 146, "Make-up Tank", 7.4, color=INK, weight="600"))
    o.append(T(109, 214, "Bình chứa nước", 7.6, color=GREY))
    # hydrogen gas cylinder (purple)
    o.append(_rect(92, 262, 56, 58, fill="#6c2a91", sw=1.3))
    o.append(_ellipse(120, 262, 28, 12, fill="#6c2a91", sw=1.3))
    o.append(_rect(111, 242, 18, 12, fill="#6c2a91", sw=1.2))
    o.append(T(120, 290, "Hydrogen", 7.4, color="#ffffff", weight="600"))
    o.append(T(120, 302, "Khí hydro", 7.2, color="#e6d6f2"))
    # mixing column: rounded vessel, packed bed marked by a cross
    o.append(_rect(286, 104, 108, 138, fill="#dceef7", sw=1.4))
    o.append(_ellipse(340, 104, 54, 17, fill="#dceef7", sw=1.4))
    o.append(_ellipse(340, 242, 54, 17, fill="#dceef7", sw=1.4))
    o.append(_line(286, 128, 394, 128, sw=1.1))
    o.append(_line(286, 216, 394, 216, sw=1.1))
    o.append(_line(286, 128, 394, 216, sw=1.0, color="#7d9bad"))
    o.append(_line(394, 128, 286, 216, sw=1.0, color="#7d9bad"))
    o.append(T(340, 116, "Mixing Column", 8.0, weight="600"))
    o.append(T(340, 100, "Cột trộn", 7.2, color=GREY))
    # catalytic reactor: rounded vessel with two internal dividers
    o.append(_rect(468, 118, 108, 124, fill="#ffffff", sw=1.4))
    o.append(_ellipse(522, 118, 54, 17, fill="#ffffff", sw=1.4))
    o.append(_ellipse(522, 242, 54, 17, fill="#ffffff", sw=1.4))
    o.append(_line(468, 140, 576, 140, sw=1.1))
    o.append(_line(468, 204, 576, 204, sw=1.1))
    o.append(T(522, 132, "Catalytic Reactor", 7.6, weight="600"))
    o.append(T(522, 116, "Lò phản ứng xúc tác", 7.2, color=GREY))
    # water line: tank bottom -> bottom of the mixing column
    o.append(_line(140, 196, 140, 272, sw=2.0, color=BLUE))
    o.append(_line(140, 272, 322, 272, sw=2.0, color=BLUE))
    o.append(_arrow(322, 272, 322, 251, sw=2.0, color=BLUE))
    o.append(T(240, 266, "H₂O", 7.4, color=BLUE))
    # hydrogen line: cylinder -> bottom of the mixing column
    o.append(_line(120, 242, 120, 252, sw=2.0, color="#6c2a91"))
    o.append(_line(120, 252, 362, 252, sw=2.0, color="#6c2a91"))
    o.append(_arrow(362, 252, 362, 251, sw=2.0, color="#6c2a91"))
    o.append(T(300, 288, "H₂", 7.6, color="#6c2a91"))
    # overhead line: top of mixing column -> top of catalytic reactor
    o.append(_line(340, 88, 340, 56, sw=2.0, color=BLUE))
    o.append(_line(340, 56, 522, 56, sw=2.0, color=BLUE))
    o.append(_arrow(522, 56, 522, 102, sw=2.0, color=BLUE))
    # treated water outlet
    o.append(_line(522, 259, 522, 302, sw=2.0, color=BLUE))
    o.append(_arrow(522, 290, 522, 310, sw=2.0, color=BLUE))
    o.append(T(522, 324, "Treated Water", 7.8, color=BLUE, weight="600"))
    o.append(T(522, 336, "Nước đã xử lý", 7.0, color=GREY))
    o.append(T(340, 344, "Hình 1.1 (nguyên bản Hình 1, tr. 4)", 7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.1 - Catalytic dissolved oxygen removal process overview"))
    return _fig(s,
                "Hình 1.1 (nguyên bản Hình 1, tr. 4) · Tổng quan quá trình khử oxy hòa tan bằng "
                "xúc tác: nước từ bình chứa được đưa vào đáy cột trộn, khí hydro từ bình chứa "
                "cũng được cấp vào đáy cột; hỗn nước đã bão hòa H₂ và O₂ đi từ đỉnh cột trộn sang "
                "lò phản ứng xúc tác, và nước đã xử lý ra ở đáy lò.",
                "Figure 1.1 (source Figure 1, p. 4) · Overview of the catalytic dissolved-oxygen "
                "removal process: water from the make-up tank and hydrogen from the gas cylinder "
                "enter the bottom of the mixing column; the water saturated with H₂ and O₂ flows "
                "from the top of the mixing column to the catalytic reactor, and treated water "
                "leaves at the reactor bottom.",
                "Sơ đồ dây chuyền gồm bình chứa nước, bình hydro, cột trộn, lò phản ứng xúc tác và đầu ra nước đã xử lý",
                "Process schematic with a make-up tank, hydrogen cylinder, mixing column, catalytic reactor and treated-water outlet")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Figure 2 (source p. 4) - outlet oxygen vs. temperature."""
    w, h = 680, 300
    o = [_defs()]
    fr, mx, my = _frame(70, 38, 500, 204, (0, 60), (0, 70),
                        [(0, "0"), (10, "10"), (20, "20"), (30, "30"),
                         (40, "40"), (50, "50"), (60, "60")],
                        [(0, "0"), (10, "10"), (20, "20"), (30, "30"),
                         (40, "40"), (50, "50"), (60, "60"), (70, "70")],
                        "T (°C)", "Outlet Oxygen (ppb)")
    o.append(fr)
    red = [(5, 61), (8, 31), (11, 22), (14, 16), (18, 11), (23, 6),
           (28, 4), (34, 3), (42, 3), (50, 3)]
    blue = [(5, 40), (8, 22), (11, 14), (14, 10), (18, 5), (23, 2),
            (28, 1.3), (34, 1), (42, 1), (50, 1)]
    o.append(_series(red, mx, my, RED))
    o.append(_series(blue, mx, my, BLUE))
    o.append(_legend([(BLUE, "3 atm"), (RED, "2 atm")], 590, 76, w=72))
    o.append(T(320, 292, "Hình 1.2 (nguyên bản Hình 2, tr. 4)", 7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.2 - Effect of temperature on outlet oxygen"))
    return _fig(s,
                "Hình 1.2 (nguyên bản Hình 2, tr. 4) · Ảnh hưởng của nhiệt độ đến nồng độ oxy đầu "
                "ra, với hai đường cho áp suất 3 atm (xanh) và 2 atm (đỏ). Nồng độ oxy giảm nhanh "
                "khi nhiệt độ tăng từ khoảng 5 °C đến 20 °C; khoảng nhiệt độ thích hợp của hệ thống "
                "là 10-50 °C, và ở áp suất cao hơn thì oxy đầu ra thấp hơn.",
                "Figure 1.2 (source Figure 2, p. 4) · Effect of temperature on outlet oxygen, "
                "with curves at 3 atm (blue) and 2 atm (red). Outlet oxygen falls sharply as "
                "temperature rises from about 5 °C to 20 °C; the proper temperature range of the "
                "system is 10-50 °C, and the higher pressure gives the lower outlet oxygen.",
                "Đồ thị oxy đầu ra giảm dần theo nhiệt độ cho hai mức áp suất 3 atm và 2 atm",
                "Plot of outlet oxygen falling with temperature for 3 atm and 2 atm curves")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Figure 3 (source p. 5) - outlet oxygen vs. pressure (semi-log)."""
    w, h = 680, 300
    o = [_defs()]
    fr, mx, my = _frame(70, 38, 490, 204, (0, 5), (1, 10000),
                        [(0, "0"), (1, "1"), (2, "2"), (3, "3"),
                         (4, "4"), (5, "5")],
                        [(1, "1"), (10, "10"), (100, "100"),
                         (1000, "1000"), (10000, "10000")],
                        "P (atm)", "Outlet Oxygen (ppb)", logy=True)
    o.append(fr)
    blue = [(1, 6000), (1.3, 480), (1.6, 100), (2, 10), (2.5, 3),
            (3, 2.2), (3.5, 1.8), (4, 1.7)]
    red = [(1, 6000), (1.4, 1500), (1.9, 90), (2.4, 30), (2.9, 13),
           (3.4, 10), (4, 8)]
    green = [(1, 6000), (1.5, 1500), (2, 1000), (2.5, 90), (3, 40),
             (3.5, 25), (4, 20)]
    o.append(_series(green, mx, my, GREEN))
    o.append(_series(red, mx, my, RED))
    o.append(_series(blue, mx, my, BLUE))
    o.append(_legend([(BLUE, "20 °C"), (RED, "10 °C"), (GREEN, "5 °C")],
                     578, 76, size=7.4))
    o.append(T(315, 292, "Hình 1.3 (nguyên bản Hình 3, tr. 5)", 7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.3 - Effect of pressure on outlet oxygen"))
    return _fig(s,
                "Hình 1.3 (nguyên bản Hình 3, tr. 5) · Ảnh hưởng của áp suất đến oxy đầu ra (trục "
                "tung logarit), với các đường ở 20 °C (xanh), 10 °C (đỏ) và 5 °C (xanh lá). Oxy "
                "đầu ra giảm mạnh khi áp suất tăng; khoảng áp suất thích hợp là 1,7-3 atm, và ở "
                "nhiệt độ cao hơn thì cần áp suất cao hơn.",
                "Figure 1.3 (source Figure 3, p. 5) · Effect of pressure on outlet oxygen (log "
                "ordinate), with curves at 20 °C (blue), 10 °C (red) and 5 °C (green). Outlet "
                "oxygen drops steeply as pressure rises; the appropriate pressure range is "
                "1.7-3 atm, and a higher pressure is required at higher temperatures.",
                "Đồ thị bán log oxy đầu ra giảm theo áp suất cho ba mức nhiệt độ 20, 10 và 5 độ C",
                "Semi-log plot of outlet oxygen falling with pressure at 20, 10 and 5 degrees C")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Figure 4 (source p. 9) - remaining oxygen vs. time, by contact time."""
    w, h = 680, 300
    o = [_defs()]
    fr, mx, my = _frame(70, 38, 490, 204, (0, 140), (1, 10000),
                        [(0, "0"), (20, "20"), (40, "40"), (60, "60"),
                         (80, "80"), (100, "100"), (120, "120"), (140, "140")],
                        [(1, "1"), (10, "10"), (100, "100"),
                         (1000, "1000"), (10000, "10000")],
                        "time (min)", "Remain Oxygen (ppb)", logy=True)
    o.append(fr)
    blue = [(5, 6000), (10, 600), (20, 60), (35, 10), (50, 4),
            (75, 2.5), (100, 2), (130, 2)]
    red = [(5, 6000), (10, 800), (20, 150), (35, 25), (50, 10),
           (75, 5), (100, 4), (130, 3.5)]
    green = [(5, 6000), (20, 1000), (35, 150), (50, 60), (75, 30),
             (100, 25), (130, 22)]
    o.append(_series(green, mx, my, GREEN))
    o.append(_series(red, mx, my, RED))
    o.append(_series(blue, mx, my, BLUE))
    o.append(_legend([(BLUE, "120 sec"), (RED, "60 sec"), (GREEN, "45 sec")],
                     578, 76, size=7.4, w=80))
    o.append(T(315, 292, "Hình 1.4 (nguyên bản Hình 4, tr. 9)", 7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.4 - Effect of contact time on remaining oxygen"))
    return _fig(s,
                "Hình 1.4 (nguyên bản Hình 4, tr. 9) · Ảnh hưởng của thời gian tiếp xúc đến oxy còn "
                "lại (trục tung logarit), với các đường ứng với 120 giây (xanh), 60 giây (đỏ) và "
                "45 giây (xanh lá). Thời gian tiếp xúc càng dài thì oxy còn lại càng giảm nhanh; "
                "với thời gian dưới 45 giây không thể đưa oxy hòa tan xuống dưới 5 ppb.",
                "Figure 1.4 (source Figure 4, p. 9) · Effect of contact time on remaining oxygen "
                "(log ordinate), with curves for 120 seconds (blue), 60 seconds (red) and 45 "
                "seconds (green). Longer contact time removes oxygen faster; at contact times "
                "below 45 seconds it is not possible to bring dissolved oxygen under 5 ppb.",
                "Đồ thị bán log oxy còn lại giảm theo thời gian cho các thời gian tiếp xúc 120, 60 và 45 giây",
                "Semi-log plot of remaining oxygen versus time for 120, 60 and 45 second contact times")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Figure 5 (source p. 9) - remaining oxygen vs. time, by inlet DO."""
    w, h = 680, 300
    o = [_defs()]
    fr, mx, my = _frame(70, 38, 490, 204, (-30, 120), (1, 10000),
                        [(-30, "-30"), (20, "20"), (70, "70"), (120, "120")],
                        [(1, "1"), (10, "10"), (100, "100"),
                         (1000, "1000"), (10000, "10000")],
                        "time (min)", "Remain Oxygen (ppb)", logy=True)
    o.append(fr)
    blue = [(0, 100), (10, 90), (20, 30), (30, 4), (40, 2.5),
            (60, 2), (80, 1.8), (110, 1.5)]
    red = [(0, 1200), (10, 1000), (20, 200), (30, 80), (45, 20),
           (60, 8), (80, 4), (110, 3)]
    green = [(0, 5000), (10, 4000), (20, 1000), (35, 300), (50, 60),
             (70, 12), (85, 5), (110, 3.5)]
    o.append(_series(green, mx, my, GREEN))
    o.append(_series(red, mx, my, RED))
    o.append(_series(blue, mx, my, BLUE))
    o.append(_legend([(BLUE, "0.5 ppm"), (RED, "2 ppm"), (GREEN, "4 ppm")],
                     578, 76, size=7.4, w=80))
    o.append(T(315, 292, "Hình 1.5 (nguyên bản Hình 5, tr. 9)", 7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Figure 1.5 - Effect of different dissolved oxygen concentrations"))
    return _fig(s,
                "Hình 1.5 (nguyên bản Hình 5, tr. 9) · Ảnh hưởng của nồng độ oxy hòa tan đầu vào "
                "đến oxy còn lại theo thời gian (trục tung logarit), với các đường 0,5 ppm (xanh), "
                "2 ppm (đỏ) và 4 ppm (xanh lá). Nồng độ đầu vào càng thấp thì thời gian cần để đạt "
                "5 ppb càng ngắn; với đầu vào 0,5 ppm, thời gian đó rất ngắn ngay cả khi tiếp xúc "
                "30 giây.",
                "Figure 1.5 (source Figure 5, p. 9) · Effect of inlet dissolved-oxygen concentration "
                "on remaining oxygen versus time (log ordinate), with curves for 0.5 ppm (blue), "
                "2 ppm (red) and 4 ppm (green). The lower the inlet concentration, the shorter "
                "the time needed to reach 5 ppb; at 0.5 ppm inlet that time is short even at a "
                "30-second contact time.",
                "Đồ thị bán log oxy còn lại theo thời gian cho nồng độ đầu vào 0,5, 2 và 4 ppm",
                "Semi-log plot of remaining oxygen versus time for 0.5, 2 and 4 ppm inlet DO")
