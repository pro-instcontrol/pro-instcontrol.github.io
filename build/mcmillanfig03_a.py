# -*- coding: utf-8 -*-
"""Vector redraws of Figures 3.1-3.5 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 3 "Area classification practice for gases,
vapours and mists in freely ventilated situations".

Fig. 3.1 is the hatch legend (square grid = Zone 0, crosshatch = Zone 1,
single diagonal = Zone 2); Figs. 3.2-3.5 show extents of Zone 2 around a
pipe flange, including the gravitational bias for heavy/light gas and the
effect of proximity to ground and walls.  All art is XML-valid SVG text;
no raster images are used.  Architecture mirrors `mcmillanfig02_a.py`:
each figure returns the standard five-tuple through `vfig._fig()` and is
registered in `FIGS` by the `_reg` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, PAPER, _arrow, _circle, _defs, _fig,
                  _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape all XML-significant characters in displayed text."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.0, **kw):
    """Text helper: escape first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# --------------------------------------------------------------- primitives
def _grid(x, y, w, h, step=11):
    """True square grid (Zone 0 hatch), clipped to the given rectangle."""
    o = []
    xx = x + step
    while xx < x + w - 0.1:
        o.append(_line(xx, y, xx, y + h, sw=0.6, color="#9a9a9a"))
        xx += step
    yy = y + step
    while yy < y + h - 0.1:
        o.append(_line(x, yy, x + w, yy, sw=0.6, color="#9a9a9a"))
        yy += step
    return "".join(o)


def _dv(x, y1, y2, label, size=7.2, color=INK):
    """Vertical double-headed dimension with a horizontal label at left."""
    return "".join([
        _line(x - 3, y1, x + 3, y1, sw=0.7, color=GREY),
        _line(x - 3, y2, x + 3, y2, sw=0.7, color=GREY),
        _arrow(x, y1 + 3, x, y2 - 3, sw=0.9, color=GREY, head="a7"),
        _arrow(x, y2 - 3, x, y1 + 3, sw=0.9, color=GREY, head="a7"),
        T(x - 6, (y1 + y2) / 2.0 + 2.4, label, size,
          anchor="end", color=color),
    ])


def _dh(x1, x2, y, label, size=7.2, color=INK):
    """Horizontal double-headed dimension with the label above the line."""
    return "".join([
        _line(x1, y - 3, x1, y + 3, sw=0.7, color=GREY),
        _line(x2, y - 3, x2, y + 3, sw=0.7, color=GREY),
        _arrow(x1 + 3, y, x2 - 3, y, sw=0.9, color=GREY, head="a7"),
        _arrow(x2 - 3, y, x1 + 3, y, sw=0.9, color=GREY, head="a7"),
        T((x1 + x2) / 2.0, y - 5, label, size, color=color),
    ])


def _vcapsule(cx, top, bottom, width, fill="url(#h6)", sw=1.1, color=INK):
    """Vertically elongated capsule with semicircular ends."""
    r = width / 2.0
    ty = top + r
    by = bottom - r
    if by < ty:
        by = ty
    d = ("M %s %s A %s %s 0 0 1 %s %s L %s %s A %s %s 0 0 1 %s %s Z"
         % (cx - r, ty, r, r, cx + r, ty, cx + r, by, r, r, cx - r, by))
    return _path(d, fill=fill, sw=sw, color=color)


def _dome(cx, ground, width, height_to_dome, fill="url(#h6)"):
    """Dome-topped shape standing on a ground line."""
    r = width / 2.0
    dy = ground - height_to_dome
    d = ("M %s %s L %s %s A %s %s 0 0 1 %s %s L %s %s Z"
         % (cx - r, ground, cx - r, dy, r, r, cx + r, dy, cx + r, ground))
    return _path(d, fill=fill, sw=1.1, color=INK)


def _ground(cx, y, half=125):
    """Horizontal ground line with short diagonal hatching beneath."""
    o = [_line(cx - half, y, cx + half, y, sw=1.2, color=INK)]
    x = int(cx - half)
    while x < cx + half - 6:
        o.append(_line(x + 6, y + 6, x, y, sw=0.6, color=GREY))
        x += 9
    return "".join(o)


def _dashed_arc(cx, ground, width, depth):
    """Dashed concave-up boundary dipping toward the ground."""
    r = width / 2.0
    d = ("M %s %s Q %s %s %s %s"
         % (cx - r, ground - 2.0 * depth, cx, ground + 0.25 * depth,
            cx + r, ground - 2.0 * depth))
    return _path(d, fill="none", sw=1.0, color=GREY, dash="4 3")


def _pipe(cx, y, length, height=24):
    """Horizontal pipe in outline with a small flange bar at its centre."""
    left, right = cx - length / 2.0, cx + length / 2.0
    top, bot = y - height / 2.0, y + height / 2.0
    o = [
        _rect(left, top, length, height, fill=PAPER, sw=1.1),
        _path("M %s %s Q %s %s %s %s" % (left, top, left + 7, y, left, bot),
              fill="none", sw=0.9, color=INK),
        _path("M %s %s Q %s %s %s %s" % (right, top, right - 7, y, right, bot),
              fill="none", sw=0.9, color=INK),
        _rect(cx - 5, y - 20, 10, 40, fill=PAPER, sw=1.0),
        _line(cx, y - 20, cx, y + 20, sw=0.6, color=GREY),
    ]
    return "".join(o)


def _ring(cx, cy, outer=17, inner=10):
    """Unhatched bore/flange ring at the centre of an end view."""
    return (_circle(cx, cy, outer, fill=PAPER, sw=1.1)
            + _circle(cx, cy, inner, fill="none", sw=1.0))


# ------------------------------------------------------------------- figures
@_reg
def fig_f301():
    """Figure 3.1 - Identification of zones (hatch legend)."""
    w, h = 680, 400
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.1 · Nhận biết các vùng / "
               "Figure 3.1 · Identification of zones",
               9.6, color=INK, weight="600"))
    o.append(T(340, 34,
               "Ba mẫu họa tiết dùng trong toàn chương / "
               "The three hatch samples used throughout the chapter",
               6.8, color=GREY))

    x, bw, bh = 210.0, 220.0, 70.0
    for yy in (80.0, 170.0, 260.0):
        o.append(_rect(x, yy, bw, bh, fill=PAPER, sw=1.1))

    # Zone 0: square grid.
    o.append(_grid(x, 80.0, bw, bh, step=11))
    # Zone 1: dense crosshatch (the two vfig diagonals layered).
    o.append(_rect(x, 170.0, bw, bh, fill="url(#h6)", sw=0))
    o.append(_rect(x, 170.0, bw, bh, fill="url(#h7)", sw=0))
    o.append(_rect(x, 170.0, bw, bh, fill="none", sw=1.1))
    # Zone 2: single diagonal.
    o.append(_rect(x, 260.0, bw, bh, fill="url(#h6)", sw=1.1))

    o.append(T(445, 120, "Vùng 0 / Zone 0", 9.2,
               anchor="start", color=INK, weight="600"))
    o.append(T(445, 210, "Vùng 1 / Zone 1", 9.2,
               anchor="start", color=INK, weight="600"))
    o.append(T(445, 300, "Vùng 2 / Zone 2", 9.2,
               anchor="start", color=INK, weight="600"))

    o.append(T(340, 360,
               "Lưới ô vuông = Vùng 0 · Chéo chữ thập = Vùng 1 · "
               "Chéo đơn = Vùng 2", 7.6, color=INK))
    o.append(T(340, 370,
               "Square grid = Zone 0 · Crosshatch = Zone 1 · "
               "Single diagonal = Zone 2", 7.2, color=GREY))
    o.append(T(340, 389,
               "Hình 3.1 · Nhận biết các vùng / "
               "Figure 3.1 · Identification of zones", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Ba hình chữ nhật xếp chồng: lưới ô vuông, chéo chữ thập "
                        "và chéo đơn, với nhãn Zone 0, Zone 1, Zone 2")),
                "Hình 3.1 · Nhận biết các vùng / Identification of zones. "
                "Ba mẫu họa tiết: lưới ô vuông = Vùng 0, chéo chữ thập = Vùng 1, "
                "chéo đơn = Vùng 2.",
                "Figure 3.1 · Identification of zones. Three hatch samples: "
                "square grid = Zone 0, crosshatch = Zone 1, single diagonal = Zone 2.",
                "Ba hình chữ nhật xếp chồng cùng chiều rộng, bên phải có nhãn "
                "Zone 0, Zone 1, Zone 2; lần lượt dùng lưới ô vuông, chéo chữ thập "
                "và chéo đơn.",
                "Three stacked rectangles of equal width labelled Zone 0, Zone 1 "
                "and Zone 2 at right, filled respectively with a square grid, a "
                "crosshatch and a single diagonal hatch.")


@_reg
def fig_f302():
    """Figure 3.2 - Extent of Zone 2 (relative density 0.7 to 1.3)."""
    w, h = 680, 360
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.2 · Phạm vi Vùng 2 (tỷ trọng tương đối 0.7 đến 1.3) / "
               "Figure 3.2 · Extent of Zone 2 (relative density 0.7 to 1.3)",
               8.4, color=INK, weight="600"))
    o.append(T(340, 34, "Mặt đầu / End view · Mặt cạnh / Side view",
               6.8, color=GREY))

    # ---- Left: end view.
    ecx, ecy, R = 190.0, 180.0, 72.0
    o.append(_circle(ecx, ecy, R, fill="url(#h6)", sw=1.2))
    o.append(_ring(ecx, ecy))
    for yy in (ecy - R, ecy - 17, ecy + 17, ecy + R):
        o.append(_line(100, yy, 120, yy, sw=0.8, color=GREY))
    o.append(_dv(100, ecy - R, ecy - 17, "x = d"))
    o.append(T(93, ecy - 4, "Flange", 7.0, anchor="end", color=INK))
    o.append(T(93, ecy + 5, "diameter", 7.0, anchor="end", color=INK))
    o.append(_dv(100, ecy + 17, ecy + R, "x = d"))
    o.append(T(ecx, 285, "Mặt đầu / End view", 7.2, color=GREY))

    # ---- Right: side view.
    scx = 490.0
    o.append(_vcapsule(scx, 108, 252, 100, fill="url(#h6)"))
    o.append(_pipe(scx, 180.0, 190, height=24))
    for xx in (440.0, 540.0):
        o.append(_line(xx, 90, xx, 110, sw=0.8, color=GREY))
    o.append(_dh(440, 540, 88, "x = d"))
    o.append(T(scx, 285, "Mặt cạnh / Side view", 7.2, color=GREY))

    o.append(T(340, 312, "d = extent from Table 3.2 / d = phạm vi theo Bảng 3.2",
               7.6, color=INK))
    o.append(T(340, 340,
               "Hình 3.2 · Phạm vi Vùng 2 / "
               "Figure 3.2 · Extent of Zone 2 (relative density 0.7 to 1.3)",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Hai views của mối nối mặt bích: mặt đầu hình tròn có lỗ "
                        "ở giữa và mặt cạnh hình nang đứng, đều có gạch chéo đơn, "
                        "với các kích thước x = d và Flange diameter")),
                "Hình 3.2 · Phạm vi Vùng 2 / Extent of Zone 2 (relative density "
                "0.7 to 1.3). Phạm vi x = d phía trên và dưới mặt bích; "
                "d lấy theo Bảng 3.2.",
                "Figure 3.2 · Extent of Zone 2 (relative density 0.7 to 1.3). "
                "The extent is x = d above and below the flange; d is taken "
                "from Table 3.2.",
                "Mặt đầu: vùng gạch chéo đơn hình tròn có vòng lỗ tâm, với x = d "
                "phía trên và dưới, và khoảng Flange diameter. Mặt cạnh: ống ngang "
                "xuyên qua vùng gạch chéo hình nang đứng, có x = d phía trên.",
                "End view: a single-diagonal hatched circle with a central bore "
                "ring, x = d above and below, and a Flange diameter span. Side "
                "view: a horizontal pipe through a tall hatched capsule, with "
                "x = d marked above.")


@_reg
def fig_f303():
    """Figure 3.3 - Extent of Zone 2 (relative density > 1.3): heavy gas."""
    w, h = 680, 425
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.3 · Phạm vi Vùng 2 (tỷ trọng tương đối > 1.3) / "
               "Figure 3.3 · Extent of Zone 2 (relative density > 1.3)",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "Khí nặng: vùng mở rộng về phía dưới / "
               "Heavy gas: the zone is biased downwards",
               6.8, color=GREY))

    # ---- Left: end view; bore high, so the zone reaches lower (y = 1.5 d).
    ecx, ecy = 190.0, 180.0
    o.append(_vcapsule(ecx, 93, 302, 150, fill="url(#h6)"))
    o.append(_ring(ecx, ecy))
    for yy in (93, ecy - 17, ecy + 17, 302):
        o.append(_line(100, yy, 118, yy, sw=0.8, color=GREY))
    o.append(_dv(100, 93, ecy - 17, "x = d"))
    o.append(T(93, ecy - 4, "Flange", 7.0, anchor="end", color=INK))
    o.append(T(93, ecy + 5, "diameter", 7.0, anchor="end", color=INK))
    o.append(_dv(100, ecy + 17, 302, "y = 1.5 d"))
    o.append(T(ecx, 320, "Mặt đầu / End view", 7.2, color=GREY))

    # ---- Right: side view; capsule hangs well below the pipe.
    scx = 490.0
    o.append(_vcapsule(scx, 110, 285, 120, fill="url(#h6)"))
    o.append(_pipe(scx, 180.0, 190, height=24))
    for xx in (430.0, 550.0):
        o.append(_line(xx, 92, xx, 112, sw=0.8, color=GREY))
    o.append(_dh(430, 550, 90, "x = d"))
    o.append(T(scx, 320, "Mặt cạnh / Side view", 7.2, color=GREY))

    o.append(T(340, 342, "d = extent from Table 3.2 / d = phạm vi theo Bảng 3.2",
               7.6, color=INK))
    o.append(T(340, 408,
               "Hình 3.3 · Phạm vi Vùng 2 / "
               "Figure 3.3 · Extent of Zone 2 (relative density > 1.3)",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Mặt đầu và mặt cạnh của mặt bích, vùng gạch chéo đơn "
                        "lệch xuống dưới với x = d ở trên và y = 1.5 d ở dưới")),
                "Hình 3.3 · Phạm vi Vùng 2 / Extent of Zone 2 (relative density "
                "> 1.3). Khí nặng: x = d phía trên, y = 1.5 d phía dưới mặt bích.",
                "Figure 3.3 · Extent of Zone 2 (relative density > 1.3). Heavy "
                "gas: x = d above the flange, y = 1.5 d below it.",
                "Mặt đầu: vùng gạch chéo có vòng lỗ đặt cao, x = d ở trên và "
                "y = 1.5 d ở dưới. Mặt cạnh: vùng gạch chéo kéo dài xuống dưới ống.",
                "End view: hatched zone with the bore high, x = d above and "
                "y = 1.5 d below. Side view: the hatched zone extends far below "
                "the horizontal pipe.")


@_reg
def fig_f304():
    """Figure 3.4 - Extent of Zone 2 (relative density < 0.7): light gas."""
    w, h = 680, 425
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.4 · Phạm vi Vùng 2 (tỷ trọng tương đối < 0.7) / "
               "Figure 3.4 · Extent of Zone 2 (relative density < 0.7)",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "Khí nhẹ: vùng mở rộng về phía trên / "
               "Light gas: the zone is biased upwards",
               6.8, color=GREY))

    # ---- Left: end view; bore low, so the zone reaches higher (y = 1.5 d).
    ecx, ecy = 190.0, 180.0
    o.append(_vcapsule(ecx, 58, 267, 150, fill="url(#h6)"))
    o.append(_ring(ecx, ecy))
    for yy in (58, ecy - 17, ecy + 17, 267):
        o.append(_line(100, yy, 118, yy, sw=0.8, color=GREY))
    o.append(_dv(100, 58, ecy - 17, "y = 1.5 d"))
    o.append(T(93, ecy - 4, "Flange", 7.0, anchor="end", color=INK))
    o.append(T(93, ecy + 5, "diameter", 7.0, anchor="end", color=INK))
    o.append(_dv(100, ecy + 17, 267, "x = d"))
    o.append(T(ecx, 285, "Mặt đầu / End view", 7.2, color=GREY))

    # ---- Right: side view; capsule rises well above the pipe.
    scx = 490.0
    o.append(_vcapsule(scx, 75, 250, 120, fill="url(#h6)"))
    o.append(_pipe(scx, 180.0, 190, height=24))
    for xx in (430.0, 550.0):
        o.append(_line(xx, 60, xx, 77, sw=0.8, color=GREY))
    o.append(_dh(430, 550, 58, "x = d"))
    o.append(T(scx, 285, "Mặt cạnh / Side view", 7.2, color=GREY))

    o.append(T(340, 312, "d = extent from Table 3.2 / d = phạm vi theo Bảng 3.2",
               7.6, color=INK))
    o.append(T(340, 408,
               "Hình 3.4 · Phạm vi Vùng 2 / "
               "Figure 3.4 · Extent of Zone 2 (relative density < 0.7)",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Mặt đầu và mặt cạnh của mặt bích, vùng gạch chéo đơn "
                        "lệch lên trên với y = 1.5 d ở trên và x = d ở dưới")),
                "Hình 3.4 · Phạm vi Vùng 2 / Extent of Zone 2 (relative density "
                "< 0.7). Khí nhẹ: y = 1.5 d phía trên, x = d phía dưới mặt bích.",
                "Figure 3.4 · Extent of Zone 2 (relative density < 0.7). Light "
                "gas: y = 1.5 d above the flange, x = d below it.",
                "Mặt đầu: vùng gạch chéo có vòng lỗ đặt thấp, y = 1.5 d ở trên "
                "và x = d ở dưới. Mặt cạnh: vùng gạch chéo kéo dài lên trên ống.",
                "End view: hatched zone with the bore low, y = 1.5 d above and "
                "x = d below. Side view: the hatched zone extends far above the "
                "horizontal pipe.")


@_reg
def fig_f305():
    """Figure 3.5 - Effect of proximity to ground, walls, etc."""
    w, h = 680, 480
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 20,
               "Hình 3.5 · Ảnh hưởng của sự gần mặt đất, tường, v.v / "
               "Figure 3.5 · Effect of proximity to ground, walls, etc",
               8.8, color=INK, weight="600"))
    o.append(T(340, 34,
               "Bốn trường hợp: mặt đầu và mặt cạnh, có đường đứt nét gần mặt đất / "
               "Four cases: end and side views, with a dashed boundary near the ground",
               6.6, color=GREY))

    left, right = 175.0, 505.0
    rows = ((215.0, 46.0, 20.0, "x = d"),   # ground, dim-y, arc depth, top dim
            (410.0, 244.0, 10.0, "y = 1.5 d"))

    for ri, (g, dimy, depth, topdim) in enumerate(rows):
        for cx in (left, right):
            o.append(_dome(cx, g, 130, 90, fill="url(#h6)"))
            o.append(_ground(cx, g, 125))
            o.append(_dashed_arc(cx, g, 130, depth))
            o.append(_dh(cx - 65, cx + 65, dimy, topdim))
            for xx in (cx - 65, cx + 65):
                o.append(_line(xx, dimy + 3, xx, dimy + 15,
                               sw=0.8, color=GREY))
        # End views carry the bore; side views carry the pipe.
        o.append(_ring(left, g - 100))
        o.append(_pipe(right, g - 95, 200, height=20))

    # Top-left: height of the horizontal line near the bore.
    o.append(_line(70, 155, left - 65, 155, sw=0.8, color=GREY))
    o.append(_line(70, 215, left - 65, 215, sw=0.8, color=GREY))
    o.append(_dv(70, 155, 215, "1.5 - 3 m"))

    # Bottom-left: the dashed boundary is closer than 1.5 m to the ground.
    o.append(T(78, 404, "< 1.5 m", 7.2, anchor="end", color=INK))
    o.append(_arrow(84, 402, 138, 405, sw=0.9, color=INK, head="a7"))

    for cx, g in ((left, 215.0), (right, 215.0), (left, 410.0), (right, 410.0)):
        lab = "Mặt đầu / End view" if cx == left else "Mặt cạnh / Side view"
        o.append(T(cx, g + 17, lab, 6.8, color=GREY))

    o.append(T(340, 443, "d = extent from Table 3.2 / d = phạm vi theo Bảng 3.2",
               7.6, color=INK))
    o.append(T(340, 465,
               "Hình 3.5 · Ảnh hưởng của sự gần mặt đất, tường, v.v / "
               "Figure 3.5 · Effect of proximity to ground, walls, etc",
               6.6, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Bốn panel gạch chéo đơn: mặt đầu và mặt cạnh gần mặt đất, "
                        "có các kích thước x = d, y = 1.5 d, 1.5 - 3 m và < 1.5 m")),
                "Hình 3.5 · Ảnh hưởng của sự gần mặt đất, tường, v.v / Effect "
                "of proximity to ground, walls, etc. Khi chiều cao dưới 1.5 m, "
                "đường biên cong đứt nét nằm sát mặt đất.",
                "Figure 3.5 · Effect of proximity to ground, walls, etc. At "
                "heights below 1.5 m the dashed curved boundary lies close to "
                "the ground.",
                "Bốn panel xếp 2x2 gồm mặt đầu và mặt cạnh, vùng gạch chéo đơn "
                "đứng trên mặt đất; các nhãn x = d, y = 1.5 d, 1.5 - 3 m, < 1.5 m "
                "và đường cong đứt nét gần chân mặt đất.",
                "Four 2x2 panels, end and side views, with single-diagonal "
                "hatched zones standing on hatched ground lines; labels x = d, "
                "y = 1.5 d, 1.5 - 3 m, < 1.5 m and a dashed curved boundary near "
                "ground level.")
