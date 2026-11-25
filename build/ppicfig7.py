# -*- coding: utf-8 -*-
"""Vector figures 7.1-7.2 for PPIC Chapter 7 (spatial aspects of the
environmental impact of power plants).

Simplified SVG redraws of the two raster figures on PDF pages 145 and 154:
(1) the SEA procedure and methodological flowchart, with the participation
inputs, the GIS analysis row, the four highlighted core boxes, the three
outputs and the reporting and decision chain, and (2) the two side-by-side
horizontal bar panels of impact intensity on SEA goals 1-21 for the coal and
reversible hydroelectric plant strategies.

Every figure returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` and is registered in
``FIGS``. Caption numbering uses ``7.n`` through a local ``_mk`` (the shared
ppicfig5_common hardcodes ``5.n`` and is not used here).
"""
import re

from vfig import (GREY, INK, _arrow, _defs, _f, _fig, _line, _rect,
                  _txt, svg)

W, H = 680, 400

FIGS = {}


def _reg(f):
    """Register the evaluated 5-tuple of a figure builder."""
    FIGS[f.__name__] = f()
    return f


AMP = chr(38)


def esc(s):
    """Escape SVG text, leaving already-escaped entities intact."""
    s = str(s)
    s = re.sub(AMP + r"(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", AMP + "amp;", s)
    return s.replace("<", AMP + "lt;").replace(">", AMP + "gt;").replace(
        '"', AMP + "quot;")


def T(x, y, s, size=8.0, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _ar(x1, y1, x2, y2, color=INK, sw=1.1):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color)


def _block(x, y, w, h, lines, fill="#eef3fb", size=7.0, color=INK,
           sw=0.9, stroke=None, bold=False):
    """A labelled flowchart box; ``lines`` is a list of centred text lines."""
    o = [_rect(x, y, w, h, fill, sw=sw, stroke=stroke)]
    if isinstance(lines, str):
        lines = [lines]
    lines = list(lines)
    lh = size * 1.25
    y0 = y + h / 2.0 - (len(lines) - 1) * lh / 2.0 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * lh, ln, size, color=color,
                   weight="600" if bold else ""))
    return "".join(o)


def _mk(n, o, title, cvi, cen, avi, aen, h=H):
    """Close a figure with a bilingual 7.n strip and build the 5-tuple."""
    o.append(T(W / 2.0, h - 6, "Hình 7.%d   ·   Figure 7.%d" % (n, n),
               6.6, color=GREY))
    return _fig(
        svg(W, h, "".join(o), esc(title)),
        "Hình 7.%d · %s" % (n, cvi),
        "Figure 7.%d · %s" % (n, cen),
        avi, aen)


PINK = "#fbe9e7"
PINK_LINE = "#b03a2e"
PALE_GREEN = "#eaf4ea"
GREEN_LINE = "#2e7d4f"


# ---------------------------------------------------------------- 7.1
@_reg
def fig_f71():
    """Figure 7.1 - procedure and methodological framework for the SEA."""
    o = [_defs()]
    o.append(T(340, 11, "SEA procedure and methodological framework",
               8.6, color=INK, weight="600"))

    # Decision at the head of the procedure.
    o.append(_block(250, 20, 180, 20,
                    ["Making decision on undertaking",
                     "and coverage of SEA"], size=7.0, fill="#eef3fb"))

    # Participation inputs at the two sides.
    o.append(_block(90, 58, 135, 20,
                    ["Participating of professional",
                     "community"], size=6.4, fill="#f7f8f4"))
    o.append(_block(455, 58, 135, 20,
                    ["Participation of relevant",
                     "institutions"], size=6.4, fill="#f7f8f4"))

    # Overviews and the GIS analysis, linked in both directions.
    o.append(_block(80, 92, 145, 20,
                    ["Overview of contents and",
                     "objectives of the Plan"], size=6.2))
    o.append(_block(250, 92, 180, 20,
                    ["Analysis of the state of the",
                     "environment using GIS"], size=6.2, fill="#e7eef7"))
    o.append(_block(455, 92, 145, 20,
                    ["Relationship to other",
                     "documents"], size=6.2))
    for x1, x2 in ((225, 250), (430, 455)):
        o.append(_ar(x1, 99, x2, 99, color=GREY, sw=1.0))
        o.append(_ar(x2, 106, x1, 106, color=GREY, sw=1.0))

    # Problem identification feeding the core objective-setting box.
    o.append(_block(80, 122, 145, 20,
                    ["Identification of",
                     "environmental problems"], size=6.2))
    o.append(_block(235, 122, 210, 20,
                    ["Setting objectives, indicators",
                     "and evaluation criteria"],
                    size=6.6, fill=PINK, stroke=PINK_LINE, sw=1.2))

    # The four core steps, highlighted in pale red and pale green as printed.
    o.append(_block(215, 154, 250, 20,
                    ["ASSESSMENT OF IMPACTS",
                     "ON THE SEA OBJECTIVES"],
                    size=7.0, fill=PINK, stroke=PINK_LINE, sw=1.2, bold=True))
    o.append(_block(165, 186, 350, 24,
                    ["Assessment of impacts of alternatives",
                     "and selection of the most suitable",
                     "alternative"],
                    size=6.6, fill=PINK, stroke=PINK_LINE, sw=1.2))
    o.append(_block(215, 222, 250, 20,
                    ["MULTI-CRITERIA",
                     "EVALUATION"],
                    size=7.2, fill=PALE_GREEN, stroke=GREEN_LINE,
                    sw=1.2, bold=True))

    # Three outputs of the multi-criteria evaluation.
    o.append(_block(45, 258, 160, 24,
                    ["Establishing measures for",
                     "limiting the negative effects"], size=6.4))
    o.append(_block(250, 258, 180, 24,
                    ["Guidelines for impact",
                     "assessment at lower",
                     "hierarchical levels"], size=6.2))
    o.append(_block(475, 258, 160, 24,
                    ["Establishing a",
                     "monitoring program"], size=6.4))

    # Reporting and decision chain.
    o.append(_block(270, 298, 140, 18, ["SEA REPORT"],
                    size=7.4, fill="#e7eef7", bold=True))
    o.append(_block(245, 328, 190, 18,
                    ["Actors in the decision making"], size=6.8))
    o.append(_block(280, 356, 120, 18, ["Decision making"],
                    size=7.0, fill="#eef3fb"))

    # Arrows: head, participation, overview and GIS analysis.
    o.append(_ar(256, 30, 225, 58, color=GREY))
    o.append(_ar(424, 30, 455, 58, color=GREY))
    o.append(_ar(340, 40, 340, 92, color=INK, sw=1.3))
    o.append(_ar(157.5, 78, 157.5, 92, color=GREY))
    o.append(_ar(522.5, 78, 522.5, 92, color=GREY))
    o.append(_ar(152.5, 112, 152.5, 122, color=GREY))
    o.append(_ar(340, 112, 340, 122, color=INK, sw=1.2))
    o.append(_ar(225, 132, 235, 132, color=GREY))

    # The vertical core sequence.
    for ya, yb in ((142, 154), (174, 186), (210, 222)):
        o.append(_ar(340, ya, 340, yb, color=PINK_LINE, sw=1.3))

    # Evaluation outputs and the report.
    for xa, xb in ((315, 125), (340, 340), (365, 555)):
        o.append(_ar(xa, 242, xb, 258, color=GREY))
    for xa, xb in ((125, 285), (340, 340), (555, 395)):
        o.append(_ar(xa, 282, xb, 298, color=GREY))
    o.append(_ar(340, 316, 340, 328, color=INK, sw=1.2))
    o.append(_ar(340, 346, 340, 356, color=INK, sw=1.2))

    # Side participation channels feeding the alternatives step and report.
    o.append(_line(90, 68, 40, 68, sw=1.0, color=GREY))
    o.append(_line(40, 68, 40, 307, sw=1.0, color=GREY))
    o.append(_ar(40, 198, 165, 198, color=GREY))
    o.append(_ar(40, 307, 270, 307, color=GREY))
    o.append(_line(590, 68, 640, 68, sw=1.0, color=GREY))
    o.append(_line(640, 68, 640, 307, sw=1.0, color=GREY))
    o.append(_ar(640, 198, 515, 198, color=GREY))
    o.append(_ar(640, 307, 410, 307, color=GREY))

    return _mk(
        1, o,
        "SEA procedure and methodological framework",
        "Quy trình và khung phương pháp luận của đánh giá môi trường chiến lược",
        "SEA procedure and methodological framework",
        "Sơ đồ quy trình SEA gồm quyết định thực hiện, các bên tham gia, phân tích "
        "bằng GIS, xác lập mục tiêu và tiêu chí, đánh giá tác động, đa tiêu chí, "
        "ba nhóm kết quả, báo cáo SEA và ra quyết định.",
        "Flowchart of the SEA procedure from the decision to undertake it, through "
        "participation, GIS analysis, objective setting, impact assessment, "
        "multi-criteria evaluation, three outputs, the SEA report and decision "
        "making.")


R_DARK = "#8b2f24"
R_MID = "#b03a2e"
O_DARK = "#a85a22"
O_MID = "#d97b3a"
G_DARK = "#2e6b3e"
G_MID = "#3f8f4f"
G_LIGHT = "#7ba85f"

LEFT_TITLE = [
    "Building the new coal-fired power plants with an",
    "installed generation capacity of 7000 MW by 2025",
    "(350MW by 2020)",
]
RIGHT_TITLE = [
    "Building the Reversible Hydroelectric Power Plant",
    "“Bistrica” and/or Reversible Hydroelectric Power",
    "Plant “Djerdap III”",
]

# SEA goal : list of (impact intensity, bar colour) drawn in the printed panel.
LEFT_BARS = {
    21: [(2, G_MID)],
    20: [(-1, R_MID)],
    18: [(2, G_DARK)],
    17: [(2, G_LIGHT)],
    16: [(2, G_MID)],
    14: [(-1, O_MID)],
    13: [(1, G_MID)],
    12: [(1, G_LIGHT)],
    11: [(1, G_MID)],
    9: [(-1, O_MID)],
    7: [(-2, O_DARK)],
    5: [(-1, O_MID)],
}
RIGHT_BARS = {
    21: [(3, G_DARK)],
    20: [(3, G_MID)],
    19: [(3, G_MID), (-2, R_DARK)],
    18: [(3, G_DARK)],
    17: [(2, G_LIGHT)],
    16: [(2, G_MID)],
    14: [(-1, O_MID)],
    13: [(1, G_DARK)],
    10: [(-2, O_MID)],
    9: [(-2, R_MID)],
    8: [(-2, R_DARK)],
    7: [(-2, R_MID)],
    6: [(-2, R_DARK)],
    5: [(-2, R_MID)],
    4: [(-3, R_DARK)],
}


def _panel(o, x0, x1, title, bars):
    """Draw one simplified two-dimensional impact-intensity bar panel."""
    cx = (x0 + x1) / 2.0
    for i, ln in enumerate(title):
        o.append(T(cx, 18 + i * 8, ln, 6.2, color=INK, weight="600"))

    o.append(T(x0 + 2, 48, "SEA Goals", 6.2, color=GREY, anchor="start"))

    pl, pr = x0 + 35, x1 - 8
    zero = (pl + pr) / 2.0
    scale = (pr - pl) / 6.0
    ytop, ystep = 60.0, 13.0

    def gy(g):
        return ytop + (21 - g) * ystep

    # Horizontal goal guides and the vertical intensity grid.
    for g in range(1, 22):
        o.append(_line(pl, gy(g), pr, gy(g), sw=0.5, color="#cccccc"))
    for v in range(-3, 4):
        xx = zero + v * scale
        o.append(_line(xx, 52, xx, 326,
                       sw=1.0 if v == 0 else 0.5,
                       color=INK if v == 0 else "#cccccc"))

    # Bars: negative values extend left, positive values extend right.
    for g, items in sorted(bars.items()):
        y = gy(g)
        for v, col in items:
            xa = zero if v > 0 else zero + v * scale
            w = abs(v) * scale
            o.append(_rect(xa, y - 3.5, w, 7.0, col, sw=0.6, stroke=col))

    # Goal numbers beside the grid.
    for g in range(1, 22):
        o.append(T(x0 + 22, gy(g) + 2.0, str(g), 6.0,
                   color=INK, anchor="end"))

    # Intensity scale and its caption.
    for v, lab in enumerate(("−3", "−2", "−1", "0", "1", "2", "3")):
        o.append(T(zero + (v - 3) * scale, 340, lab, 6.0, color=GREY))
    o.append(T(zero, 356, "Impact intensity", 6.6, color=INK))


# ---------------------------------------------------------------- 7.2
@_reg
def fig_f72():
    """Figure 7.2 - impact intensity on SEA goals for two plant strategies."""
    o = [_defs()]
    _panel(o, 35, 330, LEFT_TITLE, LEFT_BARS)
    _panel(o, 350, 645, RIGHT_TITLE, RIGHT_BARS)
    o.append(T(340, 372,
               "Red and orange bars show negative impact, green bars positive impact",
               6.0, color=GREY))
    return _mk(
        2, o,
        "SEA goal impact intensity charts",
        "Biểu đồ mức độ tác động lên các mục tiêu SEA",
        "SEA goal impact intensity charts",
        "Hai bảng cột ngang với 21 mục tiêu SEA và thang tác động từ âm ba đến dương "
        "ba; cột đỏ cam ở bên trái thể hiện tác động âm, cột xanh lục ở bên phải "
        "thể hiện tác động dương.",
        "Two horizontal bar panels with 21 SEA goals and an impact scale from minus "
        "three to plus three; red and orange bars extend left for negative impacts "
        "and green bars extend right for positive impacts.")
