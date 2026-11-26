# -*- coding: utf-8 -*-
"""Vector redraw of Figure 4-1 in R. STAHL, *Basics of Explosion Protection*
-- "Ingress Protection (IP)" (printed A8).

The printed chart pairs a FIRST NUMBER column (0-6, protection against
solid objects) with a SECOND NUMBER column (0-8, protection against water).
Both columns carry a simple pictogram and the exact printed English
description, with the Vietnamese rendering underneath. Redrawn entirely as
SVG vector strokes; no raster art. Architecture mirrors `cvpfig26.py`.
"""
from vfig import (BLUE, GREY, INK, PAPER, _circle, _defs, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


# Exact printed English descriptions, split only for typesetting; the VI
# lines are the study translations placed underneath on the same figure.
_SOLID = [
    ("0", "none", ["Non-protected."],
     ["Không được bảo vệ."]),
    ("1", "hand", ["Protected against a solid object",
                   "greater than 50mm such as a hand."],
     ["Bảo vệ chống vật thể rắn lớn hơn 50mm,", "chẳng hạn như bàn tay."]),
    ("2", "finger", ["Protected against a solid object",
                     "greater than 12mm, such as a finger."],
     ["Bảo vệ chống vật thể rắn lớn hơn 12mm,", "chẳng hạn như ngón tay."]),
    ("3", "wire", ["Protected against a solid object",
                   "greater than 2.5mm, such as wire", "or a tool."],
     ["Bảo vệ chống vật thể rắn lớn hơn 2,5mm,", "chẳng hạn như dây hoặc dụng cụ."]),
    ("4", "thinwire", ["Protected against a solid object",
                       "greater than 1.0 mm, such as wire", "or thin strips."],
     ["Bảo vệ chống vật thể rắn lớn hơn 1,0 mm,", "chẳng hạn như dây hoặc dải mỏng."]),
    ("5", "dust", ["Dust-protected. Prevents ingress of",
                   "dust sufficient to cause harm."],
     ["Bảo vệ chống bụi. Ngăn bụi xâm nhập", "gây hại."]),
    ("6", "dusttight", ["Dust tight. No dust ingress."],
     ["Kín bụi. Không có bụi xâm nhập."]),
]

_WATER = [
    ("0", "none", ["Non-protected."],
     ["Không được bảo vệ."]),
    ("1", "drip", ["Protected against water dripping",
                   "vertically, such as condensation."],
     ["Bảo vệ chống nước nhỏ giọt thẳng đứng,", "chẳng hạn như hơi ngưng tụ."]),
    ("2", "tilt", ["Protected against dripping water",
                   "when tilted up to 15°."],
     ["Bảo vệ chống nước nhỏ giọt khi nghiêng", "đến 15°."]),
    ("3", "spray", ["Protected against water spraying at",
                    "an angle of up to 60°."],
     ["Bảo vệ chống nước phun ở góc", "lên đến 60°."]),
    ("4", "splash", ["Protected against water splashing",
                     "from any direction."],
     ["Bảo vệ chống nước văng từ mọi hướng."]),
    ("5", "jet", ["Protected against jets of water",
                  "from any direction."],
     ["Bảo vệ chống tia nước từ mọi hướng."]),
    ("6", "waves", ["Protection against heavy seas or",
                    "powerful jets of water."],
     ["Bảo vệ chống sóng lớn hoặc tia nước mạnh."]),
    ("7", "immersion", ["Protected against harmful ingress of",
                        "water when immersed between a depth",
                        "of 150mm to 1 meter."],
     ["Bảo vệ chống nước xâm nhập gây hại", "khi nhúng ở độ sâu từ 150mm",
      "đến 1 mét."]),
    ("8", "submersion", ["Protected against submersion.",
                         "Suitable for continuous immersion", "in water."],
     ["Bảo vệ chống ngập nước. Phù hợp", "để ngâm liên tục trong nước."]),
]


def _picto(cx, cy, kind, r=23):
    """One small vector pictogram inside a circle."""
    o = [_circle(cx, cy, r, fill=PAPER, sw=1.2)]
    if kind == "hand":
        o.append(_poly([(cx - 8, cy - 3), (cx + 6, cy - 3),
                        (cx + 8, cy + 9), (cx - 7, cy + 9)],
                       fill="#dfe7f0", sw=1.0, close=True))
        for i in range(4):
            o.append(_line(cx - 6 + i * 4, cy - 3, cx - 6 + i * 4, cy - 13,
                           sw=1.8, color=INK))
        o.append(_line(cx - 8, cy + 1, cx - 14, cy - 5, sw=1.8, color=INK))
    elif kind == "finger":
        o.append(_rect(cx - 4, cy - 10, 8, 19, fill="#dfe7f0", sw=1.1))
        o.append(_circle(cx, cy - 10, 4, fill="#dfe7f0", sw=1.1))
        o.append(_circle(cx, cy + 7, 4, fill="#dfe7f0", sw=1.1))
        o.append(_line(cx - 1, cy - 5, cx - 1, cy + 4, sw=0.8, color=GREY))
    elif kind == "wire":
        o.append(_line(cx - 10, cy + 10, cx + 9, cy - 9, sw=4.0, color=INK))
        o.append(_circle(cx + 10, cy - 10, 3.2, fill="#dfe7f0", sw=1.0))
    elif kind == "thinwire":
        o.append(_line(cx - 10, cy + 9, cx + 10, cy - 9, sw=1.8, color=INK))
        o.append(_circle(cx + 10, cy - 9, 2.2, fill=PAPER, sw=0.9))
    elif kind == "dust":
        for dx, dy in ((-9, -5), (-2, -9), (6, -6), (-6, 3),
                       (2, 4), (9, 2), (-2, 10)):
            o.append(_circle(cx + dx, cy + dy, 1.5, fill=INK, sw=0))
    elif kind == "dusttight":
        o.append(_line(cx - r + 3, cy + 1, cx + r - 3, cy + 1, sw=2.4, color=INK))
        for dx, dy in ((-8, -7), (0, -10), (8, -7), (-4, -3), (5, -4)):
            o.append(_circle(cx + dx, cy + dy, 1.4, fill=INK, sw=0))
    elif kind == "drip":
        o.append(_line(cx - r + 4, cy + 8, cx + r - 4, cy + 8, sw=1.8, color=BLUE))
        for x in (cx - 8, cx, cx + 8):
            o.append(_line(x, cy - 9, x, cy + 3, sw=1.2, color=BLUE))
            o.append(_circle(x, cy + 4, 2, fill=BLUE, sw=0))
    elif kind == "tilt":
        o.append(_line(cx - r + 4, cy + 8, cx + r - 4, cy + 8, sw=1.8, color=BLUE))
        for x in (cx - 8, cx, cx + 8):
            o.append(_line(x - 4, cy - 9, x + 2, cy + 3, sw=1.2, color=BLUE))
            o.append(_circle(x + 2.5, cy + 4, 2, fill=BLUE, sw=0))
    elif kind == "spray":
        o.append(_line(cx - r + 4, cy + 9, cx + r - 4, cy + 9, sw=1.5, color=BLUE))
        for x in (cx - 10, cx - 3, cx + 4, cx + 11):
            o.append(_line(x - 2, cy - 10, x + 3, cy + 4, sw=1.2, color=BLUE))
    elif kind == "splash":
        o.append(_line(cx - r + 4, cy + 9, cx + r - 4, cy + 9, sw=1.5, color=BLUE))
        for dx, dy in ((-10, -4), (-5, -9), (0, -11), (5, -9), (10, -4)):
            o.append(_line(cx + dx, cy + dy, cx + dx * 0.35, cy + dy * 0.35 + 3,
                           sw=1.1, color=BLUE))
        o.append(_circle(cx, cy + 4, 3, fill=BLUE, sw=0))
    elif kind == "jet":
        o.append(_rect(cx - r + 2, cy - 4, 8, 8, fill="#dfe7f0", sw=1.1))
        for dy in (-5, 0, 5):
            o.append(_line(cx - r + 10, cy + dy, cx + r - 3, cy + dy,
                           sw=1.3, color=BLUE))
    elif kind == "waves":
        o.append(_line(cx - r + 3, cy, cx + r - 3, cy, sw=2.2, color=INK))
        o.append(_path("M %s,%s q 5,-5 10,0 t 10,0 t 10,0" % (cx - 15, cy - 6),
                       sw=1.2, color=BLUE))
    elif kind == "immersion":
        o.append(_line(cx - r + 3, cy - 2, cx + r - 3, cy - 2, sw=2.2, color=INK))
        o.append(_path("M %s,%s q 5,-4 10,0 t 10,0 t 10,0" % (cx - 15, cy - 10),
                       sw=1.1, color=BLUE))
        for dy in (cy + 5, cy + 11):
            o.append(_line(cx - 10, dy, cx + 10, dy, sw=0.8, color=GREY))
    elif kind == "submersion":
        o.append(_line(cx - r + 3, cy - 5, cx + r - 3, cy - 5, sw=2.2, color=INK))
        o.append(_path("M %s,%s q 5,-4 10,0 t 10,0 t 10,0" % (cx - 15, cy - 12),
                       sw=1.1, color=BLUE))
        o.append(_circle(cx, cy + 7, 7, fill="#dfe7f0", sw=1.1))
    return "".join(o)


def _row(o, y, rh, x0, x1, digit, kind, en_lines, vi_lines):
    """One digit row: shaded digit cell, vector pictogram, bilingual text."""
    o.append(_rect(x0, y + 2, 28, rh - 4, fill="#eef2f7", sw=1.0))
    o.append(T(x0 + 14, y + rh / 2.0 + 3.4, digit, 9.2, weight="600"))
    o.append(_picto(x0 + 55, y + rh / 2.0, kind))
    ty = y + 15
    for ln in en_lines:
        o.append(T(x0 + 92, ty, ln, 6.4, anchor="start", color=INK))
        ty += 9.5
    ty += 2.5
    for ln in vi_lines:
        o.append(T(x0 + 92, ty, ln, 6.2, anchor="start", color=GREY))
        ty += 9
    o.append(_line(x0, y + rh, x1, y + rh, sw=0.6, color="#cccccc"))


@_reg
def fig_f401():
    """Figure 4-1 -- IP ingress-protection chart (first 0-6, second 0-8)."""
    w, h = 680, 810
    o = [_defs()]
    o.append(T(340, 19, "Ingress Protection (IP) / Chỉ số bảo vệ xâm nhập (IP)",
               10.0, color=INK, weight="600"))
    o.append(T(340, 36, "IEC 60 529 · two-digit code / mã hai chữ số",
               7.2, color=GREY))

    # Column headers.
    o.append(_rect(24, 48, 308, 40, fill="#eef2f7", sw=1.1))
    o.append(T(40, 74, "IP", 11.0, weight="600", anchor="start"))
    o.append(T(180, 64, "FIRST NUMBER · SỐ THỨ NHẤT", 7.8, weight="600"))
    o.append(T(180, 79, "Degree of protection against solid objects / "
                        "Mức bảo vệ chống vật thể rắn", 6.4, color=GREY))
    o.append(_rect(340, 48, 316, 40, fill="#eef2f7", sw=1.1))
    o.append(T(498, 64, "SECOND NUMBER · SỐ THỨ HAI", 7.8, weight="600"))
    o.append(T(498, 79, "Degree of protection against water / "
                        "Mức bảo vệ chống nước", 6.4, color=GREY))

    # Left column: 7 rows; right column: 9 rows. Both end at y = 749.
    top = 92
    for i, (digit, kind, en, vi) in enumerate(_SOLID):
        _row(o, top + i * 94, 94, 24, 332, digit, kind, en, vi)
    for i, (digit, kind, en, vi) in enumerate(_WATER):
        _row(o, top + i * 73, 73, 340, 656, digit, kind, en, vi)

    o.append(T(340, 770, "Hình 4-1 · Bảng chỉ số IP: chữ số thứ nhất 0–6 (vật thể rắn), "
                         "chữ số thứ hai 0–8 (nước)", 6.8, color=INK))
    o.append(T(340, 788, "Figure 4-1 · IP ingress-protection chart: first digit 0–6 "
                         "(solids), second digit 0–8 (water)", 6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Bảng chỉ số bảo vệ xâm nhập IP theo IEC 60 529")),
                "Hình 4-1 · Bảng chỉ số bảo vệ xâm nhập (IP) theo IEC 60 529: chữ số "
                "thứ nhất 0–6 cho vật thể rắn, chữ số thứ hai 0–8 cho nước",
                "Figure 4-1 · IP ingress-protection chart from printed A8: first digit "
                "0–6 for solid objects, second digit 0–8 for water, per IEC 60 529",
                "Bảng IP hai cột: chữ số thứ nhất 0 đến 6 kèm hình bàn tay, ngón tay, "
                "dây dẫn và bụi; chữ số thứ hai 0 đến 8 kèm hình giọt nước, tia nước và sóng",
                "Two-column IP chart: first digit 0 to 6 with hand, finger, wire and dust "
                "pictograms; second digit 0 to 8 with drops, jets and waves pictograms")
