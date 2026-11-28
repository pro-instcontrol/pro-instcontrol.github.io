# -*- coding: utf-8 -*-
"""Vector redraws of Figures 17.1-17.3 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 17 "Selection of power supply,
apparatus and interconnecting cabling system for both gas/vapour/mist risks
and dust risks".

The three drawings are simplified vector redraws of the rendered pages
p504 and p505. Fig. 17.1 is a TN-C-S multi-outlet distribution with a
combined PEN conductor earthed at the source and at each consumer outlet;
Fig. 17.2 is the TN-S counterpart with a separate neutral and PE and no
outlet earth rods; Fig. 17.3 is the earthing arrangement for explosive
atmosphere risks, with A inputs, B tap points and a local isolating
transformer. Printed English caption wording is retained verbatim,
including the two forms "Note:" / "Notes:", the en dashes in T–N–C–S and
the printed quirk "exits". Every displayed string is literal Unicode.
Each public callable returns the standard five-tuple through ``vfig._fig()``
and is registered in ``FIGS`` by the ``_reg`` decorator.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (_circle, _defs, _fig, _f, _line, _path, _poly, _rect,
                  _txt, svg, INK, PAPER)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=7.6, **kw):
    """Plain text: clamp into the 6.8-9.5 px contract, vet, delegate to vfig."""
    size = min(9.5, max(6.8, float(size)))
    return _txt(x, y, esc(s), size, **kw)


def IT(x, y, s, size=7.6, **kw):
    """Italic text for the PEN / phase conductor labels under the outlets."""
    return T(x, y, s, size, **kw).replace('style="font:',
                                          'style="font-style:italic;font:', 1)


# ------------------------------------------------------------------ helpers

def _wire(o, pts, sw=1.1, color=INK):
    """A polyline conductor with an explicit fill attribute."""
    o.append(_poly(pts, fill="none", sw=sw, color=color))


def _zig(o, p0, p1, teeth=5, amp=3.4, sw=1.1):
    """A zigzag resistor / winding between two points."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    length = math.hypot(dx, dy)
    if not length:
        return
    ux, uy = dx / length, dy / length
    nx, ny = -uy, ux
    pts = [p0]
    for i in range(1, 2 * teeth):
        t = i / (2.0 * teeth)
        a = amp if i % 2 else -amp
        pts.append((p0[0] + dx * t + nx * a, p0[1] + dy * t + ny * a))
    pts.append(p1)
    _wire(o, pts, sw=sw)


def _dot(o, x, y, r=2.0):
    o.append(_circle(x, y, r, fill=INK, sw=0, color=INK))


def _delta(o, top, bl, br, teeth=4):
    """Generator delta: three zigzags forming a triangle with solid nodes."""
    _zig(o, top, bl, teeth)
    _zig(o, bl, br, teeth)
    _zig(o, br, top, teeth)
    for x, y in (top, bl, br):
        _dot(o, x, y, 1.9)


def _star(o, centre, ends, teeth=3):
    """Star-connected winding: zigzag arms meeting at an earthed centre."""
    for e in ends:
        _zig(o, centre, e, teeth, 3.0)
    _dot(o, centre[0], centre[1], 2.2)


def _transformer(o, cx, y0, y1):
    """Two vertical coil stacks with a laminated core of horizontal bars."""
    _zig(o, (cx - 12, y0), (cx - 12, y1), teeth=6, amp=3.8)
    _zig(o, (cx + 12, y0), (cx + 12, y1), teeth=6, amp=3.8)
    for k in range(4):
        yy = y0 + (y1 - y0) * (k + 0.5) / 4.0
        _wire(o, [(cx - 6, yy), (cx + 6, yy)], sw=1.6)


def _earth(o, x, y_top, y_bar):
    """Earth rod: vertical stake with three descending ground bars."""
    _wire(o, [(x, y_top), (x, y_bar)])
    _wire(o, [(x - 7, y_bar), (x + 7, y_bar)], sw=1.3)
    _wire(o, [(x - 4.5, y_bar + 4), (x + 4.5, y_bar + 4)], sw=1.3)
    _wire(o, [(x - 2, y_bar + 8), (x + 2, y_bar + 8)], sw=1.3)


def _break(o, x, y0, y1):
    """One wavy vertical break mark; a pair is drawn at x and x + 8."""
    pts = []
    for i in range(25):
        t = i / 24.0
        pts.append((x + 3.0 * math.sin(t * 4 * math.pi),
                    y0 + (y1 - y0) * t))
    _wire(o, pts, sw=1.2)


def _drop(o, x, y_from, y_to):
    """A tap dropping from a busbar to a filled downward arrowhead."""
    _wire(o, [(x, y_from), (x, y_to)])
    o.append(_poly([(x - 2.6, y_to - 5), (x + 2.6, y_to - 5), (x, y_to + 1)],
                   fill=INK, sw=0, close=True))


# ------------------------------------------------------------------ 17.1

@_reg
def fig_f1701():
    """Figure 17.1 - TN-C-S distribution, PEN earthed at source and outlets."""
    w, h = 680, 240
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]

    # Generator delta and its three incoming stubs.
    for y in (126, 146, 166):
        _dot(o, 24, y, 1.9)
    _wire(o, [(24, 126), (56, 126)])
    _wire(o, [(24, 146), (46, 146)])
    _wire(o, [(24, 166), (36, 166)])
    _delta(o, (56, 126), (36, 166), (76, 166))

    # Supply transformer: primary fed from the delta, earthed star secondary.
    _wire(o, [(56, 126), (120, 126), (120, 54), (140, 54)])
    _wire(o, [(76, 166), (120, 166), (120, 108), (140, 108)])
    _transformer(o, 152, 54, 108)
    _wire(o, [(164, 96), (188, 96)])
    _star(o, (188, 96), [(188, 52), (206, 70), (224, 88)])
    _earth(o, 188, 106, 126)

    # Four busbars: three phases plus the combined PEN.
    _wire(o, [(188, 52), (548, 52)])
    _wire(o, [(206, 70), (548, 70)])
    _wire(o, [(224, 88), (548, 88)])
    _wire(o, [(188, 106), (548, 106)])

    # Two pairs of wavy break marks.
    for x in (296, 304, 396, 404):
        _break(o, x, 48, 112)

    # Outlet 1: four taps and a local earth rod off the PEN.
    for x, yy in ((350, 52), (342, 70), (334, 88), (326, 106)):
        _drop(o, x, yy, 164)
    _wire(o, [(316, 106), (316, 132)])
    _earth(o, 316, 132, 132)

    # Outlet 2: four taps and a local earth rod off the PEN.
    for x, yy in ((450, 52), (442, 70), (434, 88), (426, 106)):
        _drop(o, x, yy, 164)
    _wire(o, [(416, 106), (416, 132)])
    _earth(o, 416, 132, 132)

    # Far-right busbar labels.
    for y in (52, 70, 88):
        o.append(T(556, y + 2.5, "Phase CDR", 7.4, anchor="start"))
    for s, y in (("Combined", 106), ("neutral and", 116),
                 ("protective", 126), ("CDR (PEN)", 136)):
        o.append(T(556, y + 2.5, s, 7.4, anchor="start"))

    # Source, transformer and earth-rod labels.
    for s, y in (("Electrical", 186), ("supply", 195),
                 ("from", 204), ("generator", 213)):
        o.append(T(54, y, s, 7.0))
    o.append(T(142, 132, "Supply", 7.0))
    o.append(T(142, 141, "transformer", 7.0))
    o.append(T(212, 128, "Earth rod", 7.0, anchor="start"))
    o.append(T(312, 146, "Earth rod", 7.0, anchor="end"))
    o.append(T(412, 146, "Earth rod", 7.0, anchor="end"))

    # Outlet labels.
    for cx, num in ((338, "1"), (438, "2")):
        o.append(IT(cx, 178, "PEN P P P", 7.6))
        o.append(T(cx, 192, "Outlet (consumer)", 7.0))
        o.append(T(cx, 205, num, 7.6))

    return _fig(svg(w, h, "".join(o), esc("Fig 17.1")),
                "Hình 17.1 · Hệ thống phân phối điện điển hình nhiều ổ cắm "
                "T–N–C–S. Lưu ý: Tất cả kim loại hở đều được nối với dây dẫn PEN",
                "Figure 17.1 · Typical multi-outlet T–N–C–S electricity "
                "distribution system. Note: All exposed metal is connected to "
                "the PEN conductor",
                "Sơ đồ nguồn phát ba pha hình tam giác gồm ba cuộn zigzag, nối "
                "tới máy biến áp có hai cột cuộn dây và lõi các thanh ngang; "
                "điểm sao của máy biến áp được nối với cọc tiếp đất. Bốn thanh "
                "dẫn ngang chạy sang phải gồm ba pha và một dây PEN chung, bị "
                "ngắt bởi hai cặp vết gợn sóng. Mỗi trong hai ổ cắm có bốn nhánh "
                "dẫn xuống mũi tên, một cọc tiếp đất rẽ từ dây PEN, nhãn nghiêng "
                "PEN P P P và số 1 hoặc 2. Ở đầu phải các thanh dẫn được ghi "
                "Phase CDR và Combined neutral and protective CDR (PEN)",
                "A three-phase generator drawn as a triangle of three zigzag "
                "windings feeds a supply transformer with two vertical coil "
                "stacks and a laminated core; its star point drops to an earth "
                "rod. Four horizontal busbars - three phases and a combined "
                "PEN - run rightwards, interrupted by two pairs of wavy break "
                "marks. Each of two consumer outlets has four taps ending in "
                "downward arrowheads, an earth rod branching from the PEN, "
                "the italic label PEN P P P and the numeral 1 or 2. At the far "
                "right the lines are labelled Phase CDR three times and "
                "Combined neutral and protective CDR (PEN)")


# ------------------------------------------------------------------ 17.2

@_reg
def fig_f1702():
    """Figure 17.2 - TN-S distribution with separate neutral and PE."""
    w, h = 680, 240
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]

    # Same source as Fig. 17.1.
    for y in (126, 146, 166):
        _dot(o, 24, y, 1.9)
    _wire(o, [(24, 126), (56, 126)])
    _wire(o, [(24, 146), (46, 146)])
    _wire(o, [(24, 166), (36, 166)])
    _delta(o, (56, 126), (36, 166), (76, 166))

    _wire(o, [(56, 126), (120, 126), (120, 50), (140, 50)])
    _wire(o, [(76, 166), (120, 166), (120, 104), (140, 104)])
    _transformer(o, 152, 50, 104)
    _wire(o, [(164, 94), (188, 94)])
    _star(o, (188, 94), [(188, 48), (206, 64), (224, 80)])
    _earth(o, 188, 96, 126)

    # Five separate busbars: three phases, neutral and protective PE.
    _wire(o, [(188, 48), (548, 48)])
    _wire(o, [(206, 64), (548, 64)])
    _wire(o, [(224, 80), (548, 80)])
    _wire(o, [(188, 96), (548, 96)])
    _wire(o, [(188, 112), (548, 112)])
    _wire(o, [(188, 112), (188, 126)])

    for x in (296, 304, 396, 404):
        _break(o, x, 44, 118)

    # Two outlets, five taps each; no earth rods at the outlets.
    for x, yy in ((358, 48), (350, 64), (342, 80), (334, 96), (326, 112)):
        _drop(o, x, yy, 168)
    for x, yy in ((458, 48), (450, 64), (442, 80), (434, 96), (426, 112)):
        _drop(o, x, yy, 168)

    for y in (48, 64, 80):
        o.append(T(556, y + 2.5, "Phase CDR", 7.4, anchor="start"))
    o.append(T(556, 98.5, "Neutral CDR", 7.4, anchor="start"))
    o.append(T(556, 108.5, "Protective", 7.4, anchor="start"))
    o.append(T(556, 118.5, "CDR (PE)", 7.4, anchor="start"))

    for s, y in (("Electrical", 186), ("supply", 195),
                 ("from", 204), ("generator", 213)):
        o.append(T(54, y, s, 7.0))
    o.append(T(142, 132, "Supply", 7.0))
    o.append(T(142, 141, "transformer", 7.0))
    o.append(T(212, 128, "Earth rod", 7.0, anchor="start"))

    for cx, num in ((342, "1"), (442, "2")):
        o.append(IT(cx, 182, "PEN P P PP", 7.6))
        o.append(T(cx, 196, "Outlet (consumer)", 7.0))
        o.append(T(cx, 209, num, 7.6))

    return _fig(svg(w, h, "".join(o), esc("Fig 17.2")),
                "Hình 17.2 · Hệ thống phân phối điện điển hình nhiều ổ cắm "
                "TN-S. Lưu ý: Tất cả kim loại hở đều được nối với dây dẫn PE",
                "Figure 17.2 · Typical multi-outlet TN-S electricity "
                "distribution system. Note: All exposed metal is connected to "
                "the PE conductor",
                "Cùng nguồn phát hình tam giác và máy biến áp như hình trước, "
                "nhưng có năm thanh dẫn riêng biệt: ba pha, một dây trung tính "
                "và một dây bảo vệ PE, chỉ có một cọc tiếp đất tại điểm sao "
                "của máy biến áp. Hai cặp vết gợn sóng ngắt các thanh dẫn. "
                "Mỗi ổ cắm có năm nhánh dẫn xuống mũi tên, không có cọc tiếp "
                "đất tại chỗ, kèm nhãn nghiêng PEN P P PP và số 1 hoặc 2. "
                "Đầu phải ghi Phase CDR ba lần, Neutral CDR và Protective "
                "CDR (PE)",
                "The same delta generator and supply transformer as the "
                "previous drawing, but five separate busbars: three phases, "
                "a neutral and a protective PE, with a single earth rod at "
                "the transformer star point only. Two pairs of wavy break "
                "marks interrupt the busbars. Each outlet has five taps "
                "ending in downward arrowheads, no local earth rod, the "
                "italic label PEN P P PP and the numeral 1 or 2. The far "
                "right is labelled Phase CDR three times, Neutral CDR and "
                "Protective CDR (PE)")


# ------------------------------------------------------------------ 17.3

@_reg
def fig_f1703():
    """Figure 17.3 - earthing arrangements for explosive atmosphere risks."""
    w, h = 680, 310
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]

    # Three A phase inputs feeding the generator delta.
    for y in (72, 92, 112):
        o.append(T(36, y + 2.5, "A", 7.6, anchor="end"))
        _dot(o, 42, y, 1.9)
    _wire(o, [(42, 72), (86, 72)])
    _wire(o, [(42, 92), (66, 92)])
    _wire(o, [(42, 112), (66, 112)])
    _delta(o, (86, 72), (66, 112), (106, 112))

    # Supply transformer with its star point earthed.
    _wire(o, [(86, 72), (122, 72), (122, 54), (140, 54)])
    _wire(o, [(106, 112), (122, 112), (122, 108), (140, 108)])
    _transformer(o, 152, 54, 108)
    _wire(o, [(164, 96), (188, 96)])
    _star(o, (188, 96), [(188, 56), (206, 72), (224, 88)])
    _earth(o, 188, 104, 126)

    # Four busbars with the printed parenthetical beside the N line.
    _wire(o, [(188, 56), (470, 56)])
    _wire(o, [(206, 72), (470, 72)])
    _wire(o, [(224, 88), (470, 88)])
    _wire(o, [(188, 104), (470, 104)])
    for x in (276, 284, 346, 354):
        _break(o, x, 50, 110)

    # Three B taps feeding the local isolating transformer.
    for x, yy in ((396, 56), (418, 72), (440, 88)):
        _wire(o, [(x, yy), (x, 148)])
        _dot(o, x, yy, 2.1)
    _wire(o, [(396, 148), (418, 152)])
    _wire(o, [(418, 148), (418, 152)])
    _wire(o, [(440, 148), (418, 152)])
    _delta(o, (418, 152), (398, 190), (438, 190), teeth=3)

    # Local isolating transformer: thick core bar and a winding below.
    o.append(_rect(396, 196, 44, 4, fill=INK, sw=0))
    _zig(o, (418, 200), (418, 232), teeth=6, amp=4.0)
    _earth(o, 396, 196, 224)

    # Four outlet conductors.
    for x in (410, 422, 434, 446):
        _drop(o, x, 232, 262)

    # In-figure labels.
    for s, y in (("Electrical", 134), ("supply from", 143),
                 ("generator", 152)):
        o.append(T(86, y, s, 7.0))
    o.append(T(142, 134, "Supply", 7.0))
    o.append(T(142, 143, "transformer", 7.0))
    o.append(T(212, 128, "Earth rod", 7.0, anchor="start"))
    for y in (59, 75, 91, 107):
        o.append(T(486, y, "P", 7.6, anchor="start"))
    for s, y in (("(Either PEN", 62), ("CDR or just", 72),
                 ("N if separate", 82), ("PE CDR", 92), ("exits)", 102)):
        o.append(T(516, y, s, 7.0, anchor="start"))

    for s, x, y in (("B", 390, 68), ("B", 412, 84), ("B", 434, 100)):
        o.append(T(x, y, s, 7.6, anchor="end"))
    o.append(T(444, 112, "(Note 1)", 7.0, anchor="start"))

    for s, y in (("Local outlet", 176), ("isolating", 186),
                 ("transformer", 196)):
        o.append(T(380, y, s, 7.0, anchor="end"))
    for s, y in (("Earth rod", 240), ("(local to", 250),
                 ("outlet)", 260), ("(Note 2)", 270)):
        o.append(T(368, y, s, 7.0, anchor="end"))

    for s, x in (("PE", 410), ("NP", 422), ("P", 434), ("P", 446)):
        o.append(IT(x, 276, s, 7.6))
    o.append(T(428, 292, "Outlet", 7.6))

    return _fig(svg(w, h, "".join(o), esc("Fig 17.3")),
                "Hình 17.3 · Bố trí tiếp đất điển hình cho các lắp đặt có nguy "
                "cơ cháy nổ do khí quyển nổ. Ghi chú: (1) Các điểm ‘B’ có thể "
                "được cấp điện trực tiếp từ máy phát điện nếu nhu cầu lớn hoặc "
                "nếu thuận tiện. (2) Cọc tiếp đất chỉ dành riêng cho lắp đặt "
                "cụ thể đó",
                "Figure 17.3 · Typical earthing arrangements for installations "
                "with explosive atmosphere risks. Notes: (1) Points ‘B’ may be "
                "fed directly from power generator if demand is large or if "
                "convenient. (2) Earth rod reserved for particular installation",
                "Ba đầu vào pha mang nhãn A đi vào máy phát hình tam giác, rồi "
                "qua máy biến áp có điểm sao nối cọc tiếp đất. Bốn thanh dẫn "
                "ngang ghi P P P N, bên cạnh là nhãn (Either PEN CDR or just "
                "N if separate PE CDR exits), với hai cặp vết gợn sóng. Ba "
                "điểm nhánh mang nhãn B, điểm thứ ba có (Note 1), dẫn xuống "
                "cuộn sơ cấp hình tam giác của máy biến áp cách ly tại chỗ. "
                "Máy này có lõi thanh đậm, cuộn dây bên dưới và cọc tiếp đất "
                "riêng mang nhãn Earth rod (local to outlet) (Note 2). Bốn "
                "dây dẫn xuống ổ cắm ghi nghiêng PE NP P P, bên dưới là Outlet",
                "Three phase inputs labelled A feed a delta generator and a "
                "supply transformer whose star point drops to an earth rod. "
                "Four busbars labelled P P P N run rightwards beside the "
                "parenthetical (Either PEN CDR or just N if separate PE CDR "
                "exits), interrupted by two pairs of wavy break marks. Three "
                "taps marked B, the third tagged (Note 1), fall to the delta "
                "primary of a local isolating transformer. That transformer "
                "has a thick core bar, a winding below and its own earth rod "
                "labelled Earth rod (local to outlet) (Note 2). Four outlet "
                "conductors carry the italic labels PE NP P P above the word "
                "Outlet")
