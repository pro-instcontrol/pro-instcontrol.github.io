# -*- coding: utf-8 -*-
"""Vector figures 6.1-6.3 for PPIC Chapter 6 (power system protection and control).

Simplified SVG redraws of the printed figures on PDF pages 125, 132 and 136:
(1) the 1900-2010 protection-technology timeline with its three eras and
    rising technology band, (2) the three-level integrated wide-area
    protection and control architecture, and (3) the distributed power cloud
    with its regional/substation bands, monitoring cloud and substation clouds.

Every figure returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` and is registered in
``FIGS``. Caption numbering uses ``6.n`` (ppicfig5_common hardcodes ``5.n``,
so a local ``_mk`` closes each figure with the chapter-6 strip instead).
"""
import re

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _circle, _defs,
                  _ellipse, _f, _fig, _line, _poly, _rect, _txt, svg)

W, H = 680, 400

FIGS = {}


def _reg(f):
    """Register the evaluated 5-tuple of a figure builder."""
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape SVG text, leaving already-escaped entities intact."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.0, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _ar(x1, y1, x2, y2, color=BLUE, sw=1.4):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color)


def _block(x, y, w, h, lines, fill="#eef3fb", size=7.0, color=INK,
           sw=0.9, rx=0, bold=False):
    """A labelled block; ``lines`` is a list of centred text lines."""
    o = []
    if rx:
        o.append('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" '
                 'fill="%s" stroke="%s" stroke-width="%s"/>'
                 % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, INK, _f(sw)))
    else:
        o.append(_rect(x, y, w, h, fill, sw=sw))
    if isinstance(lines, str):
        lines = [lines]
    lines = list(lines)
    lh = size * 1.25
    y0 = y + h / 2.0 - (len(lines) - 1) * lh / 2.0 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * lh, ln, size, color=color,
                   weight="600" if bold else ""))
    return "".join(o)


def _cloud(x, y, w, h, fill="#f7f8f4", rx=18, sw=1.0):
    """A rounded 'cloud' box (clouds/rounded boxes per the redraw brief)."""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" '
            'fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, INK, _f(sw)))


def _rot(x, y, s, size=7.0, color=INK):
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (_f(x), _f(y), _f(x), _f(y), _f(size), color, esc(s)))


def _mk(n, o, title, cvi, cen, avi, aen, h=H):
    """Close a figure with a bilingual 6.n strip and build the 5-tuple."""
    o.append(T(W / 2.0, h - 6, "Hình 6.%d   ·   Figure 6.%d" % (n, n),
               6.6, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 6.%d · %s" % (n, cvi),
        "Figure 6.%d · %s" % (n, cen),
        avi, aen)


# ---------------------------------------------------------------- 6.1
@_reg
def fig_f61():
    """Figure 6.1 - history of power system protection, 1900 to 2010."""
    o = [_defs()]
    o.append(T(340, 12, "History of power system protection (1900-2010)",
               8.8, color=INK, weight="600"))

    # Three shaded eras across the top.
    eras = [(80, 160, "Conventional Protection", "#dce9f2"),
            (240, 145, "Modern Protection", "#e3efe2"),
            (385, 175, "New development", "#f4ead6")]
    for x, w, lab, fill in eras:
        o.append(_rect(x, 22, w, 24, fill, sw=0.8))
        o.append(T(x + w / 2.0, 38, lab, 7.2, color=INK))
    for xx in (240, 385):
        o.append(_line(xx, 46, xx, 300, sw=0.7, color="#b0b0b0", dash="3 3"))

    # Earliest principles and milestones, climbing with time.
    o.append(_block(84, 150, 124, 104,
                    ["Early principles:", "Overcurrent (1801)",
                     "Differential (1908)", "Directional (1910)",
                     "Distance (1923)", "Power-line carrier (1927)"], size=6.6))
    o.append(_ellipse(232, 116, 46, 16, fill="#f3e6f0", sw=0.9))
    o.append(T(232, 113, "Computer relay", 6.6))
    o.append(T(232, 123, "(1970)", 6.2))
    o.append(_block(246, 156, 120, 62,
                    ["Artificial Intelligence", "and Adaptive",
                     "(1980s-1990s)"], size=6.8))
    o.append(_block(250, 228, 104, 32,
                    ["Travelling wave", "(1970s)"], size=6.6))
    o.append(_ellipse(400, 130, 38, 15, fill="#e7eef7", sw=0.9))
    o.append(T(400, 133, "GPS (1990)", 7.0))
    o.append(_block(370, 166, 84, 30,
                    ["Integrated", "schemes (2000s)"], size=6.6))
    o.append(_block(420, 222, 116, 34,
                    ["Wide-area protection", "and control"], size=6.6))
    o.append(_ellipse(505, 166, 46, 15, fill="#f3e6f0", sw=0.9))
    o.append(T(505, 163, "Intelligent", 6.6))
    o.append(T(505, 173, "relays", 6.4))
    o.append(_block(528, 78, 140, 44,
                    ["Integrated regional", "level (about 2010)"],
                    size=7.0, fill="#e7eef7"))

    # Progress arrows linking the milestones in rising order.
    for x1, y1, x2, y2 in (
            (208, 170, 205, 134), (276, 122, 252, 154),
            (366, 175, 395, 146), (438, 128, 527, 104),
            (354, 238, 372, 198), (454, 180, 460, 169),
            (536, 232, 550, 183), (550, 158, 580, 123)):
        o.append(_ar(x1, y1, x2, y2, color=GREY, sw=1.1))
    for x1, y1, x2, y2 in ((222, 288, 222, 262),
                           (372, 275, 372, 258),
                           (560, 253, 560, 240)):
        o.append(_ar(x1, y1, x2, y2, color=BLUE, sw=1.8))

    # Rising "technology progress" band and its four technology stages.
    o.append(_poly([(80, 310), (600, 250), (600, 280), (80, 340)],
                   fill="#c9d3df", sw=0.9, color=INK, close=True))
    for xx, yy, lab, sz in (
            (140, 322, "electromechanical", 6.4),
            (265, 307, "integrated circuit/transistor", 6.0),
            (385, 293, "microprocessor", 6.4),
            (475, 282, "communication/information", 5.8)):
        o.append(T(xx, yy, lab, sz))
    o.append(T(565, 272, "TECHNOLOGY PROGRESS", 6.2, color=GREY))

    # Year axis.
    o.append(_ar(70, 348, 628, 348, color=INK, sw=1.0))
    for xx, lab in ((80, "1900"), (240, "1970"), (310, "1980"),
                    (385, "1990"), (465, "2000"), (545, "2010")):
        o.append(_line(xx, 348, xx, 352, sw=0.7))
        o.append(T(xx, 365, lab, 6.6, color=GREY))
    o.append(T(600, 365, "year", 6.6, color=INK, anchor="start"))

    return _mk(1, o, "History of power system protection",
               "Lịch sử phát triển của bảo vệ hệ thống điện",
               "History of power system protection",
               "Dòng thời gian từ 1900 đến 2010 gồm ba giai đoạn, băng công nghệ "
               "tiến triển và các mốc bảo vệ được nối bằng mũi tên tiến bộ.",
               "Timeline from 1900 to 2010 with three eras, a rising technology "
               "band and labelled protection milestones joined by progress arrows.")


# ---------------------------------------------------------------- 6.2
@_reg
def fig_f62():
    """Figure 6.2 - three-level integrated wide-area protection and control."""
    o = [_defs()]
    o.append(T(340, 10, "Integrated wide area protection and control",
               8.8, color=INK, weight="600"))

    # Wide-area / regional level.
    o.append(_block(238, 16, 204, 34,
                    ["Integrated regional protection", "and control functions"],
                    size=7.4, fill="#dce9f2"))
    o.append(_block(70, 62, 540, 32,
                    ["Regional P and C synchronising data platform",
                     "supported by a high-speed communication network"],
                    size=7.0, fill="#e8eef7", rx=8))
    o.append(_ar(320, 50, 320, 62, color=GREY, sw=1.1))
    o.append(_ar(360, 62, 360, 50, color=GREY, sw=1.1))

    # Substation / plant level.
    o.append(_block(38, 110, 148, 60,
                    ["Integrated substation", "protection and",
                     "control functions"], size=7.0))
    o.append(_block(248, 110, 184, 60,
                    ["Substation network",
                     "MU, intelligent terminal,",
                     "metering, PMU, local protection"], size=6.8))
    o.append(_block(494, 110, 148, 60,
                    ["Local protection and", "wind-turbine",
                     "protection"], size=7.0))
    for xd, xu in ((100, 130), (320, 350), (550, 580)):
        o.append(_ar(xd, 94, xd, 110, color=GREY, sw=1.0))
        o.append(_ar(xu, 110, xu, 94, color=GREY, sw=1.0))

    # Local level: sources, AC/DC lines, transformer and distribution network.
    o.append(_rect(36, 204, 150, 120, "#eaf4ea", sw=1.0))
    o.append(T(111, 218, "Sources and lines", 7.0, color=INK, weight="600"))
    for cy in (250, 292):
        o.append(_circle(62, cy, 10, fill="#ffffff", sw=1.0))
        o.append(T(62, cy + 2.4, "~", 8.0, color=INK))
    o.append(_line(72, 250, 120, 250, sw=1.2))
    o.append(_line(72, 292, 120, 292, sw=1.2))
    o.append(T(100, 245, "AC line", 6.4, color=INK))
    o.append(T(100, 287, "DC line", 6.4, color=INK))
    o.append(_circle(146, 258, 9, fill="none", sw=1.0))
    o.append(_circle(146, 276, 9, fill="none", sw=1.0))
    o.append(T(150, 306, "transformer", 6.2, color=GREY))

    o.append(_rect(186, 204, 458, 120, "#eaf1f8", sw=1.0))
    o.append(T(415, 218, "Distribution network", 7.0,
               color=INK, weight="600"))
    o.append(_line(196, 236, 634, 236, sw=1.2))
    o.append(_circle(206, 262, 9, fill="none", sw=1.0))
    o.append(_circle(206, 280, 9, fill="none", sw=1.0))
    o.append(_line(206, 236, 206, 253, sw=1.0))
    o.append(T(206, 231, "transformer", 6.0, color=GREY))
    for cx, w, lines in ((250, 46, ["load"]), (312, 42, ["PV"]),
                         (372, 46, ["load"]), (432, 44, ["STC"]),
                         (494, 58, ["Storage"]),
                         (580, 80, ["Micro turbine", "Wind farm"])):
        o.append(_line(cx, 236, cx, 274, sw=0.8, color="#7f9ab0"))
        o.append(_block(cx - w / 2.0, 274, w, 30, lines,
                        size=6.6, fill="#f7fafd"))

    # Bidirectional links from the substation level to the primary apparatus.
    for xd, xu in ((90, 130), (318, 358), (546, 586)):
        o.append(_ar(xd, 170, xd, 204, color=GREY, sw=1.0))
        o.append(_ar(xu, 204, xu, 170, color=GREY, sw=1.0))

    for xx, yy, lab in ((18, 62, "Regional level"),
                        (18, 140, "Substation level"),
                        (18, 270, "Local level")):
        o.append(_rot(xx, yy, lab, 7.0, color=GREY))

    return _mk(2, o, "Integrated wide area protection and control",
               "Bảo vệ và điều khiển diện rộng tích hợp",
               "Integrated wide area protection and control",
               "Sơ đồ ba cấp: chức năng bảo vệ và điều khiển vùng, nền tảng dữ liệu "
               "đồng bộ trên mạng tốc độ cao, trạm biến áp tích hợp và thiết bị tại "
               "chỗ với đường dây, phụ tải, PV, lưu trữ và trang trại gió.",
               "Three-level diagram: regional protection and control functions, a "
               "synchronised data platform on a high-speed network, integrated "
               "substation and local equipment with lines, loads, PV, storage and "
               "a wind farm.")


# ---------------------------------------------------------------- 6.3
@_reg
def fig_f63():
    """Figure 6.3 - structure of the distributed power cloud."""
    o = [_defs()]
    o.append(T(340, 10, "Structure of distributed power cloud",
               8.8, color=INK, weight="600"))

    # Two vertical scope bands.
    o.append(_rect(8, 30, 18, 150, "#f4ead6", sw=0.8))
    o.append(_rect(8, 196, 18, 118, "#e3efe2", sw=0.8))
    o.append(_rot(17, 108, "Wide-area protection and control", 6.8, color=GREY))
    o.append(_rot(17, 256, "Substation protection and control", 6.8, color=GREY))

    # Monitoring cloud.
    o.append(_cloud(46, 26, 506, 156, fill="#f7f8f4", rx=18))
    o.append(T(60, 42, "Monitoring", 8.2, color=INK, weight="600"))
    o.append(_block(58, 56, 92, 56,
                    ["P and C layer", "Sample control", "platform"],
                    size=6.6, fill="#eef3fb"))
    for x, lab in ((160, ["Regional dynamic", "monitoring"]),
                   (254, ["Regional protection", "monitoring"]),
                   (348, ["Maintenance and", "management"])):
        o.append(_block(x, 54, 88, 30, lab, size=6.6, fill="#fbf7e8"))
    for x, lab in ((160, ["Information", "processing"]),
                   (254, ["Topology analysis"]),
                   (348, ["Short-circuit", "current"])):
        o.append(_block(x, 90, 88, 30, lab, size=6.6, fill="#fbf7e8"))
    o.append(_ar(204, 121, 250, 131, color=GREY, sw=1.0))
    o.append(_ar(298, 121, 298, 131, color=GREY, sw=1.0))
    o.append(_ar(392, 121, 350, 131, color=GREY, sw=1.0))
    o.append(_block(196, 133, 196, 32, ["Distribution control platform"],
                    size=7.4, fill="#dce9f2", bold=True))
    o.append(_block(404, 128, 132, 42,
                    ["Regional information", "and regional P and C"],
                    size=6.6, fill="#eef3fb"))

    # EMS cloud to the right, linked by dashed data arrows.
    o.append(_cloud(566, 60, 92, 64, fill="#eef3fb", rx=16))
    o.append(T(612, 96, "EMS", 8.0, color=INK, weight="600"))
    o.append(_ar(552, 80, 566, 80, color=GREY, sw=1.0))
    o.append(_ar(566, 104, 552, 104, color=GREY, sw=1.0))

    # Data flow between the regional monitoring platform and substation clouds.
    for xd, xu in ((150, 178), (510, 538)):
        o.append(_ar(xd, 182, xd, 196, color=GREY, sw=1.0))
        o.append(_ar(xu, 196, xu, 182, color=GREY, sw=1.0))

    # Substation cloud 1.
    o.append(_cloud(66, 196, 232, 118, fill="#f7f8f4", rx=16))
    o.append(T(80, 212, "Substation cloud 1", 7.6,
               color=INK, weight="600", anchor="start"))
    o.append(_block(76, 222, 64, 22, ["FGC layer"], size=6.4, fill="#eef3fb"))
    o.append(_block(76, 250, 64, 34,
                    ["Sample control", "platform"], size=6.4, fill="#eef3fb"))
    o.append(_block(148, 222, 76, 34,
                    ["Substation electrical", "quantity acquisition"],
                    size=6.2, fill="#fbf7e8"))
    o.append(_block(148, 262, 76, 30,
                    ["Distributed local", "control"], size=6.4, fill="#fbf7e8"))
    o.append(_block(232, 222, 58, 44,
                    ["Substation backup", "protection and", "control"],
                    size=6.2, fill="#eef3fb"))
    o.append(T(294, 306, "...", 7.0, color=GREY))

    # Further substation clouds.
    o.append(_cloud(466, 196, 150, 118, fill="#f7f8f4", rx=16))
    o.append(T(480, 212, "Substation cloud N", 7.6,
               color=INK, weight="600", anchor="start"))
    o.append(_block(482, 224, 116, 56,
                    ["Sample, control", "and protection", "functions"],
                    size=6.6, fill="#eef3fb"))
    for yy in (242, 260):
        o.append(_line(484, yy, 596, yy, sw=0.5, color="#b8c4d0"))
    for xx in (518, 554, 590):
        o.append(_line(xx, 226, xx, 278, sw=0.5, color="#b8c4d0"))

    # Process level.
    o.append(_rect(86, 332, 516, 24, "#e8eef7", sw=1.0))
    o.append(T(344, 348, "Sample and control at process level", 7.6, color=INK))
    for xd, xu in ((166, 196), (520, 550)):
        o.append(_ar(xd, 314, xd, 332, color=GREY, sw=1.0))
        o.append(_ar(xu, 332, xu, 314, color=GREY, sw=1.0))

    return _mk(3, o, "Structure of distributed power cloud",
               "Cấu trúc điện toán đám mây phân tán",
               "Structure of distributed power cloud",
               "Sơ đồ gồm hai dải vùng và trạm, đám mây giám sát với phân tích tô pô "
               "và dòng ngắn mạch, nền tảng điều khiển phân phối, các đám mây trạm, "
               "EMS và mẫu và điều khiển cấp quá trình.",
               "Diagram with regional and substation bands, a monitoring cloud with "
               "topology and short-circuit analysis, a distribution control platform, "
               "substation clouds, EMS and sample and control at process level.")
