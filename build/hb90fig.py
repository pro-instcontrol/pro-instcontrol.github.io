# -*- coding: utf-8 -*-
"""Figure 90.1 for Handbook Chapter 90 — Human Factors in Displays.

90.1 four examples of alphanumeric display fonts: a 5 x 7 dot matrix, a
9 x 11 dot matrix, a seven-segment starburst and a sixteen-segment starburst.

Chapter 90 has a single figure, so there is no base module: the primitives come
straight from `hb93base.py`.

Every dot pattern and every lit/unlit segment in this figure was read off the
printed page rather than invented — the matrix cells were sampled from the
extracted page image at the measured row and column centres, and the segment
states were read from the same image. The 5 x 7 cell spells R, the 9 x 11 cell
spells K, the seven-segment cell shows 5 and the starburst shows M. The source
labels the last one a "16-segment font" although only fourteen segment
positions are drawn; the printed label is kept.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content.
"""
from hbfig import svg, _fig
from hb93base import E, S, _defs, _lbl, _line, _circ

ON = "#2a2a2a"        # lit segment / filled dot
OFF = "#d9d9d9"       # unlit segment (the source hatches these)
RING = "#4a4a4a"      # outline of an unlit dot

# ---- the four glyphs, read off the printed page ----------------------
P57 = [
    "####o",
    "#ooo#",
    "#ooo#",
    "####o",
    "#o#oo",
    "#oo#o",
    "#ooo#",
]

P911 = [
    "#ooooooo#",
    "#oooooo#o",
    "#ooooo#oo",
    "#oooo#ooo",
    "#ooo#oooo",
    "####ooooo",
    "#ooo#oooo",
    "#oooo#ooo",
    "#ooooo#oo",
    "#oooooo#o",
    "#ooooooo#",
]

# seven-segment: a, f, g, c, d lit  ->  "5"
SEG7 = {"a": True, "b": False, "c": True, "d": True,
        "e": False, "f": True, "g": True}

# fourteen drawn positions; verticals and upper diagonals lit  ->  "M"
SEG16 = {
    "a1": False, "a2": False, "g1": False, "g2": False, "d1": False, "d2": False,
    "f1": True, "f2": True, "b1": True, "b2": True,
    "h": True, "i": True, "j": False, "k": False,
}


def _seg(x1, y1, x2, y2, t, on):
    """One display segment: a round-capped line, lit or unlit."""
    return ('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" '
            'stroke-width="%.2f" stroke-linecap="round"/>'
            % (x1, y1, x2, y2, ON if on else OFF, t))


def _matrix(x0, y0, pitch, r, rows):
    """A dot-matrix cell: filled disc = lit, open ring = unlit."""
    o = []
    for ri, row in enumerate(rows):
        for ci, ch in enumerate(row):
            cx = x0 + pitch * (ci + 0.5)
            cy = y0 + pitch * (ri + 0.5)
            if ch == "#":
                o.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/>'
                         % (cx, cy, r, ON))
            else:
                o.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="#fff" '
                         'stroke="%s" stroke-width="%.2f"/>'
                         % (cx, cy, r, RING, max(1.0, r * 0.17)))
    return "".join(o)


def fig_90_1():
    tag = "901"
    o = [_defs(tag)]

    # ---- panel A: 5 x 7 dot matrix -----------------------------------
    o.append(_matrix(78, 34, 22.0, 8.0, P57))
    o.append(_lbl(133, 216, "phông ma trận 5 × 7", "tm", "middle"))

    # ---- panel B: 9 x 11 dot matrix ----------------------------------
    o.append(_matrix(430, 26, 15.5, 5.4, P911))
    o.append(_lbl(500, 216, "phông ma trận 9 × 11", "tm", "middle"))

    # ---- panel C: seven-segment --------------------------------------
    xL, xR, yT, yM, yB, t = 100.0, 180.0, 262.0, 347.0, 432.0, 11.0
    k = t / 2.0
    o.append(_seg(xL + k, yT, xR - k, yT, t, SEG7["a"]))
    o.append(_seg(xL + k, yM, xR - k, yM, t, SEG7["g"]))
    o.append(_seg(xL + k, yB, xR - k, yB, t, SEG7["d"]))
    o.append(_seg(xL, yT + k, xL, yM - k, t, SEG7["f"]))
    o.append(_seg(xR, yT + k, xR, yM - k, t, SEG7["b"]))
    o.append(_seg(xL, yM + k, xL, yB - k, t, SEG7["e"]))
    o.append(_seg(xR, yM + k, xR, yB - k, t, SEG7["c"]))
    o.append(_lbl(140, 452, "phông 7 đoạn", "tm", "middle"))

    # ---- panel D: sixteen-segment starburst ---------------------------
    xL, xR, yT, yB, t = 420.0, 550.0, 280.0, 410.0, 10.0
    cx, cy = (xL + xR) / 2.0, (yT + yB) / 2.0
    k = t / 2.0
    segs = {
        "a1": (xL + k, yT, cx - k, yT),
        "a2": (cx + k, yT, xR - k, yT),
        "g1": (xL + k, cy, cx - k, cy),
        "g2": (cx + k, cy, xR - k, cy),
        "d1": (xL + k, yB, cx - k, yB),
        "d2": (cx + k, yB, xR - k, yB),
        "f1": (xL, yT + k, xL, cy - k),
        "f2": (xL, cy + k, xL, yB - k),
        "b1": (xR, yT + k, xR, cy - k),
        "b2": (xR, cy + k, xR, yB - k),
        "h": (xL + k, yT + k, cx - k, cy - k),
        "i": (xR - k, yT + k, cx + k, cy - k),
        "j": (xL + k, yB - k, cx - k, cy + k),
        "k": (xR - k, yB - k, cx + k, cy + k),
    }
    for name in ("a1", "a2", "g1", "g2", "d1", "d2", "j", "k",
                 "f1", "f2", "b1", "b2", "h", "i"):
        x1, y1, x2, y2 = segs[name]
        o.append(_seg(x1, y1, x2, y2, t, SEG16[name]))
    o.append(_lbl(485, 452, "phông 16 đoạn", "tm", "middle"))

    return _fig(
        svg(680, 480, "".join(o),
            "Bốn kiểu phông chữ hiển thị chữ - số"),
        "Hình 90.1 · Ví dụ về các kiểu hiển thị chữ-số. Bốn ô: ma trận điểm 5 × 7, ma trận điểm "
        "9 × 11, phông bảy đoạn và phông mười sáu đoạn; đoạn sáng vẽ đậm, đoạn tắt vẽ nhạt.",
        "Figure 90.1 · Examples of alphanumeric displays. Four panels: a 5 × 7 dot matrix, a "
        "9 × 11 dot matrix, a seven-segment font and a sixteen-segment font; lit segments are "
        "drawn dark, unlit segments pale.",
        "Bốn ô minh hoạ phông chữ hiển thị: ma trận điểm 5 × 7, ma trận điểm 9 × 11, phông bảy "
        "đoạn và phông mười sáu đoạn, với các đoạn sáng và tắt được phân biệt bằng độ đậm",
        "Four font samples: a 5 × 7 dot matrix, a 9 × 11 dot matrix, a seven-segment font and a "
        "sixteen-segment starburst, with lit and unlit segments distinguished by weight")
