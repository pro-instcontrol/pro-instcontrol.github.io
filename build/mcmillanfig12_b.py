# -*- coding: utf-8 -*-
"""Vector redraws of Figures 12.5-12.8 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 12 "Protection concept increased
safety 'e'".

Every drawing is a simplified vector redraw of the authoritative rendered
pages p324-p329.  Printed English captions (including the "continued" lines,
the numbered notes of Figs 12.6 and 12.7 and the a/b notes of Fig 12.8) are
reproduced verbatim in the returned English captions/ARIA text, with a
Vietnamese translation alongside.  Each public callable returns the standard
five-tuple through ``vfig._fig()`` on a 680-wide canvas and is registered in
``FIGS`` by the ``_reg`` decorator.
"""
import math
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (_defs, _fig, _line, _rect, _txt, _arrow, _circle, _poly, svg,
                  GREY, INK, PAPER, BLUE, RED, GREEN)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with XML metacharacters escaped."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def T(x, y, s, size=6.8, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

INS = "url(#h6)"     # hatched insulating material (45 deg)
INS2 = "url(#h7)"    # second hatch: a separately cemented rib
CREEP = RED          # creepage path (dotted)
CLEAR = BLUE         # clearance path (dashed)


def _panel(ox, oy, inner):
    """Place a locally-drawn fragment inside a translated group."""
    return '<g transform="translate(%s %s)">%s</g>' % (ox, oy, inner)


def _cond(x, y, w=22, h=6):
    """Dark conductor block whose bottom sits on the surface y."""
    return _rect(x, y - h, w, h, fill=INK, sw=0.8)


def _creep(pts):
    """Dotted red creepage path following the insulating surface."""
    return _poly(pts, fill="none", sw=1.6, color=CREEP, dash="1 2")


def _clear(x1, y1, x2, y2):
    """Dashed blue straight-line clearance through air."""
    return _line(x1, y1, x2, y2, sw=1.2, color=CLEAR, dash="5 3")


def _dimh(x1, x2, y, label, above=False, color=INK):
    """Double-headed dimension arrow with an explicit label."""
    o = [_line(x1, y - 5, x1, y + 4, sw=0.7, color=color),
         _line(x2, y - 5, x2, y + 4, sw=0.7, color=color),
         _arrow(x1 + 2, y, x2 - 2, y, sw=0.8, color=color, head="a7"),
         _arrow(x2 - 2, y, x1 + 2, y, sw=0.8, color=color, head="a7")]
    o.append(T((x1 + x2) / 2.0, (y - 6) if above else (y + 12), label, 6.8,
               color=color))
    return "".join(o)


def _lab(tx, ty, ax, ay, s, size=6.8, color=INK, anchor="middle"):
    """Bilingual label with a thin grey leader to a feature."""
    return (T(tx, ty, s, size, anchor=anchor, color=color) +
            _arrow(tx, ty + 2, ax, ay, sw=0.7, color=GREY, head="a7"))


def _title(o, n, vi, en):
    o.append(T(340, 14, "Hình 12.%d · %s" % (n, vi), 7.8, weight="600"))
    o.append(T(340, 24, "Figure 12.%d · %s" % (n, en), 7.2, color=GREY))


def _legend(o, y=36):
    o.append(_line(120, y, 150, y, sw=1.8, color=CREEP, dash="1 2"))
    o.append(T(156, y + 2.4, "Đường rò (Creepage distance)", 6.8,
               anchor="start", color=CREEP))
    o.append(_line(360, y, 390, y, sw=1.4, color=CLEAR, dash="5 3"))
    o.append(T(396, y + 2.4, "Khoảng hở (Clearance)", 6.8,
               anchor="start", color=CLEAR))


# ------------------------------------------------------------------ 12.6 helpers

def _slot_panel(ox, oy, idx, kind, sw, sd, dimtxt, note3=False):
    """One slot/groove sub-figure of Fig 12.6, local box 320x128."""
    o = [T(10, 11, "(%s)" % idx, 6.8, anchor="start", color=GREY)]
    cx = 160.0
    if kind == "slot":
        pts = [(30, 42), (cx - sw / 2.0, 42), (cx - sw / 2.0, 42 + sd),
               (cx + sw / 2.0, 42 + sd), (cx + sw / 2.0, 42),
               (290, 42), (290, 78), (30, 78)]
        creep = [(130, 41), (cx - sw / 2.0, 41), (cx - sw / 2.0, 41 + sd),
                 (cx + sw / 2.0, 41 + sd), (cx + sw / 2.0, 41), (190, 41)]
        clr = _clear(130, 34, 190, 34)
        rbase, dx1, dx2 = 42, cx - sw / 2.0, cx + sw / 2.0
        n3x = cx + sw / 2.0 + 2
    else:  # step: right-hand conductor sits on a lower ledge
        pts = [(30, 42), (160, 42), (160, 42 + sd), (290, 42 + sd),
               (290, 78), (30, 78)]
        creep = [(130, 41), (160, 41), (160, 41 + sd), (190, 41 + sd)]
        clr = _clear(130, 36, 190, 36 + sd)
        rbase, dx1, dx2, n3x = 42 + sd, 160.0, 190.0, 175.0
    o.append(_poly(pts, fill=INS, sw=1.0, close=True))
    o.append(_cond(108, 42, 22, 6))
    o.append(_cond(190, rbase, 22, 6))
    o.append(_creep(creep))
    o.append(clr)
    o.append(_dimh(dx1, dx2, 92, dimtxt))
    o.append(_lab(100, 26, 118, 35, "Dây dẫn (note 2)", 6.8))
    o.append(_lab(220, 26, 202, rbase - 7, "Dây dẫn (note 2)", 6.8))
    o.append(_lab(160, 122, 160, 80, "Chất cách điện (Insulation)", 6.8))
    if note3:
        o.append(_lab(255, 56, n3x, 48, "(Note 3)", 6.8, color=GREY))
    return _panel(ox, oy, "".join(o))


# ------------------------------------------------------------------ 12.7 helpers

def _rib_panel(ox, oy, idx, cfg):
    """One rib sub-figure of Fig 12.7, local box 216x158."""
    o = [T(8, 10, "(%s)" % idx, 6.8, anchor="start", color=GREY)]
    cx = 108.0
    rw = 6 if cfg.get("thin") else 12
    rh = 24 if cfg.get("thin") else 28
    rt = 70 - rh
    o.append(_dimh(cx - rw / 2.0, cx + rw / 2.0, 16, cfg["dim"], above=True))
    o.append(_rect(16, 70, 184, 34, fill=INS, sw=1.0))
    if cfg.get("open"):
        o.append(_rect(cx - rw / 2.0, rt, rw, rh - 4, fill=INS, sw=1.0))
        o.append(_rect(cx - rw / 2.0, 66, rw, 4, fill=PAPER, sw=0.8))
    else:
        rf = INS2 if cfg.get("cemented") else INS
        o.append(_rect(cx - rw / 2.0, rt, rw, rh, fill=rf, sw=1.0))
    o.append(_cond(45, 70, 22, 6))
    o.append(_cond(149, 70, 22, 6))
    if cfg.get("flatcreep"):
        o.append(_creep([(67, 69), (149, 69)]))
    else:
        o.append(_creep([(67, 69), (cx - rw / 2.0, 69), (cx - rw / 2.0, rt - 1),
                         (cx + rw / 2.0, rt - 1), (cx + rw / 2.0, 69),
                         (149, 69)]))
    o.append(_clear(67, 62, 149, 62))
    o.append(_lab(168, 42, cx + rw / 2.0, rt + 2, "Rib (note 2)", 6.8))
    if cfg.get("joint"):
        o.append(_lab(108, 122, 108, 106, cfg["joint"], 6.8))
        o.append(T(108, 136, "Chất cách điện (Insulation)", 6.8, color=GREY))
    else:
        o.append(_lab(108, 122, 108, 106, "Chất cách điện (Insulation)", 6.8))
    if cfg.get("note3"):
        o.append(T(46, 56, "(Note 3)", 6.8, color=GREY))
    return _panel(ox, oy, "".join(o))


# ------------------------------------------------------------------ 12.8 helpers

def _screw(cx, top, fill):
    """Simplified screw/bolt: head, drive slot and two thread lines."""
    return (_rect(cx - 12, top, 24, 18, fill=fill, sw=1.0) +
            _line(cx - 9, top + 6, cx + 9, top + 6, sw=1.0) +
            _line(cx - 10, top + 11, cx + 10, top + 11, sw=0.6) +
            _line(cx - 10, top + 15, cx + 10, top + 15, sw=0.6))


def _screw_panel(oy, idx, metal=False):
    """One screw/bolt cross-section of Fig 12.8, local box 664x120."""
    o = [T(12, 8, "(%s)" % idx, 6.8, anchor="start", color=GREY)]
    o.append(_dimh(116, 208, 16, "a", above=True))
    o.append(_dimh(482, 548, 16, "a", above=True))
    o.append(_clear(116, 30, 322, 30))
    o.append(_clear(348, 30, 548, 30))
    o.append(_cond(90, 40, 26, 6))
    o.append(_cond(322, 40, 26, 6))
    o.append(_cond(548, 40, 26, 6))
    pts = [(20, 40), (208, 40), (208, 66), (252, 66), (252, 40),
           (438, 40), (438, 66), (482, 66), (482, 40), (644, 40),
           (644, 76), (20, 76)]
    o.append(_poly(pts, fill=INS, sw=1.0, close=True))
    o.append(_screw(230, 44, GREY if metal else "#fff"))
    o.append(_screw(460, 44, GREY if metal else "#fff"))
    o.append(_creep([(116, 39), (208, 39), (208, 65), (252, 65),
                     (252, 39), (322, 39)]))
    o.append(_creep([(348, 39), (438, 39), (438, 65), (482, 65),
                     (482, 39), (548, 39)]))
    o.append(_lab(100, 24, 103, 33, "Dây dẫn (Conductor)", 6.8))
    o.append(_lab(335, 24, 335, 33, "Dây dẫn (Conductor)", 6.8))
    o.append(_lab(561, 24, 561, 33, "Dây dẫn (Conductor)", 6.8))
    o.append(_dimh(208, 252, 90, "b"))
    o.append(_dimh(438, 482, 90, "b"))
    o.append(_lab(80, 98, 80, 78, "Chất cách điện (Insulation)", 6.8))
    cap = ("Vít kim loại (Conducting metal screws)" if metal
           else "Vít nhựa (Insulating plastic screws)")
    o.append(T(332, 114, cap, 6.8, color=GREY))
    return _panel(0, oy, "".join(o))


# ------------------------------------------------------------------ 12.5

@_reg
def fig_f1205():
    """Figure 12.5 - basic creepage distances and clearances."""
    w, h = 680, 340
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Đường rò và khoảng hở cơ bản",
           "Basic creepage distances and clearances")
    _legend(o, 36)

    # (a) flat insulation slab with a shallow groove between two conductors.
    a = [T(12, 60, "(a)", 6.8, anchor="start", color=GREY)]
    a.append(_poly([(150, 70), (300, 70), (320, 78), (360, 78), (380, 70),
                    (530, 70), (530, 104), (150, 104)],
                   fill=INS, sw=1.0, close=True))
    a.append(_cond(235, 70, 30, 6))
    a.append(_cond(415, 70, 30, 6))
    a.append(_creep([(265, 69), (300, 69), (320, 77), (360, 77),
                     (380, 69), (415, 69)]))
    a.append(_clear(265, 62, 415, 62))
    a.append(_lab(250, 50, 250, 63, "Dây dẫn (Conductors)", 6.8))
    a.append(_lab(470, 128, 470, 107, "Chất cách điện (Insulator)", 6.8))
    o.append("".join(a))

    # (b) curved insulation: the creepage path hugs the concave surface.
    b = [T(150, 160, "(b)", 6.8, anchor="start", color=GREY)]
    inner, outer = [], []
    for i in range(15):
        x = 200 + 20 * i
        t = (x - 200) / 280.0
        yy = 205 + 40 * (math.sin(math.pi * t) ** 2)
        inner.append((x, yy))
        outer.append((x, yy + 18))
    b.append(_poly(inner + outer[::-1], fill=INS, sw=1.0, close=True))
    b.append(_cond(200, 206, 28, 6))
    b.append(_cond(452, 206, 28, 6))
    b.append(_creep([(x, y - 3) for (x, y) in inner if 228 <= x <= 452]))
    b.append(_clear(228, 200, 452, 200))
    b.append(_lab(214, 182, 214, 199, "Dây dẫn (Conductor)", 6.8))
    b.append(_lab(466, 182, 466, 199, "Dây dẫn (Conductor)", 6.8))
    b.append(_lab(270, 222, 295, 233, "Đường rò (Creepage distance)", 6.8))
    b.append(_lab(410, 222, 400, 202, "Khoảng hở (Clearance)", 6.8))
    b.append(_lab(340, 300, 340, 265, "Chất cách điện (Insulation)", 6.8))
    o.append("".join(b))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.5")),
                "Hình 12.5 · Đường rò và khoảng hở cơ bản",
                "Figure 12.5 · Basic creepage distances and clearances",
                "Hai cấu hình cách điện. (a) Tấm cách điện phẳng có rãnh nông "
                "giữa hai dây dẫn: đường rò là đường chấm đi sát bề mặt và xuống "
                "đáy rãnh, khoảng hở là đường gạch đứt thẳng ngang qua không khí. "
                "Nhãn Dây dẫn (Conductors) và Chất cách điện (Insulator). "
                "(b) Tấm cách điện cong hình máng: hai dây dẫn ở hai đầu, đường "
                "rò chạy theo mặt lõm, khoảng hở là đường thẳng nối hai dây dẫn.",
                "Two insulating configurations. (a) A flat insulating slab with "
                "a shallow groove between two conductors: the creepage path is "
                "the dotted line hugging the surface and dipping into the "
                "groove, the clearance is the straight dashed line through air. "
                "Labelled Conductors and Insulator. (b) A curved bowl-shaped "
                "insulation: two conductors at the ends, the creepage path "
                "follows the concave surface and the clearance is the straight "
                "line joining the two conductors.")


# ------------------------------------------------------------------ 12.6

@_reg
def fig_f1206():
    """Figure 12.6 - creepage distances and clearances in the case of slots."""
    w, h = 680, 380
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 6, "Đường rò và khoảng hở trong trường hợp rãnh",
           "Creepage distances and clearances in the case of slots")
    _legend(o, 36)

    o.append(_slot_panel(6, 46, "a", "slot", 20, 22, "\u22642.5 mm (note 1)"))
    o.append(_slot_panel(348, 46, "b", "slot", 40, 24, "\u22652.5 mm (note 1)",
                         note3=True))
    o.append(_slot_panel(6, 178, "c", "step", 0, 22, "\u22642.5 mm (note 1)"))
    o.append(_slot_panel(348, 178, "d", "step", 0, 24, "\u22652.5 mm (note 1)",
                         note3=True))

    # (e) continued on p. 305: V-shaped groove.
    v = [T(12, 8, "(e)", 6.8, anchor="start", color=GREY)]
    v.append(_poly([(30, 14), (280, 14), (340, 36), (400, 14), (644, 14),
                    (644, 42), (30, 42)], fill=INS, sw=1.0, close=True))
    v.append(_cond(220, 14, 24, 6))
    v.append(_cond(438, 14, 24, 6))
    v.append(_creep([(244, 13), (280, 13), (340, 35), (400, 13), (438, 13)]))
    v.append(_clear(244, 6, 438, 6))
    v.append(_lab(150, 11, 231, 15, "Dây dẫn (Note 2)", 6.8, anchor="end"))
    v.append(_lab(530, 11, 449, 15, "Dây dẫn (Note 2)", 6.8, anchor="start"))
    v.append(_dimh(310, 370, 50, "2.5 mm (note 1)"))
    v.append(_lab(80, 60, 80, 44, "Chất cách điện (Insulation)", 6.8))
    v.append(_lab(570, 60, 397, 22, "(Note 3)", 6.8, color=GREY))
    o.append(_panel(0, 310, "".join(v)))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.6")),
                "Hình 12.6 · Đường rò và khoảng hở trong trường hợp rãnh "
                "(tiếp theo ở tr. 305). Ghi chú: (1) Khi tổng chiều dài đường rò "
                "yêu cầu nhỏ hơn 3 mm thì có thể giảm kích thước này xuống 1,5 mm. "
                "(2) Dây dẫn có thể là dây dẫn dòng điện hoặc dây dẫn cô lập, "
                "nhưng xem thêm Hình 12.9. (3) Khi độ sâu hiệu dụng của rãnh nhỏ "
                "hơn 2,5 mm thì bỏ qua rãnh khi đo đường rò.",
                "Figure 12.6 · Creepage distances and clearances in the case of "
                "slots (Figure continued on p. 305). Notes: (1) Where total "
                "creepage distance required is less than 3mm this dimension may "
                "be reduced to 1.5mm. (2) Conductors may be current conductors "
                "or isolated conduction, but see also Fig. 12.9. (3) Where the "
                "effective slot depth is less than 2.5mm the slot is ignored for "
                "creepage distance measurement.",
                "Bốn mặt cắt rãnh trên tấm cách điện: rãnh hẹp \u22642,5 mm, rãnh "
                "rộng \u22652,5 mm có (Note 3), và hai bậc thang tương ứng. Mỗi "
                "mặt cắt có hai dây dẫn (note 2), đường rò chấm đỏ đi xuống đáy "
                "rãnh, khoảng hở gạch đứt xanh đi thẳng, kích thước miệng rãnh "
                "và Chất cách điện (Insulation). (e) Hình tiếp theo ở tr. 305: "
                "rãnh chữ V giữa hai dây dẫn với (Note 3). Ghi chú (1) kích thước "
                "có thể giảm xuống 1,5 mm nếu tổng đường rò yêu cầu dưới 3 mm; "
                "(2) dây dẫn có thể dẫn dòng hoặc cô lập, xem Hình 12.9; (3) rãnh "
                "sâu dưới 2,5 mm thì bỏ qua khi đo đường rò.",
                "Four slot sections in insulating material: a narrow \u22642.5 mm "
                "slot, a wide \u22652.5 mm slot with (Note 3), and two matching "
                "steps. Each shows two conductors (note 2), a dotted red "
                "creepage path dipping to the slot bottom, a dashed blue straight "
                "clearance, the slot-width dimension and Insulation. (e) The "
                "figure continued on p. 305: a V-shaped groove between two "
                "conductors with (Note 3). Notes: (1) the dimension may be "
                "reduced to 1.5mm if total creepage required is less than 3mm; "
                "(2) conductors may be current conductors or isolated conduction, "
                "see Fig. 12.9; (3) an effective slot depth under 2.5mm is ignored "
                "for creepage measurement.")


# ------------------------------------------------------------------ 12.7

@_reg
def fig_f1207():
    """Figure 12.7 - creepage distances and clearances in the case of ribs."""
    w, h = 680, 380
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 7, "Đường rò và khoảng hở trong trường hợp gờ",
           "Creepage distances and clearances in the case of ribs")
    _legend(o, 36)

    cemented = "Mối xi măng (Insulating cemented joint)"
    uncemented = "Mối không xi măng (Non-cemented joint)"
    cfg = [
        dict(idx="a", dim="\u22651 mm (note 1)"),
        dict(idx="b", dim="<1 mm (note 1)", thin=True, flatcreep=True),
        dict(idx="c", dim="\u22651 mm (note 1)", cemented=True, joint=cemented),
        dict(idx="d", dim="\u22651 mm (note 1)", open=True, joint=uncemented,
             note3=True, flatcreep=True),
        dict(idx="e", dim="\u22651 mm (note 1)", cemented=True, joint=cemented),
        dict(idx="f", dim="\u22651 mm (note 1)", open=True, joint=uncemented,
             note3=True, flatcreep=True),
    ]
    for i, c in enumerate(cfg):
        col, row = i % 3, i // 3
        o.append(_rib_panel(6 + 224 * col, 46 + 160 * row, c["idx"], c))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.7")),
                "Hình 12.7 · Đường rò và khoảng hở trong trường hợp gờ "
                "(tiếp theo ở tr. 307). Ghi chú: (1) Ngoài chiều rộng tối thiểu "
                "1 mm, gờ phải đủ rộng để bền vững về cơ khí. (2) Gờ phải cao tối "
                "thiểu 2,5 mm, nếu không sẽ bị bỏ qua và đường rò cùng khoảng hở "
                "được đo thẳng trên bề mặt nằm ngang. (3) Nếu đường rò ngắn hơn "
                "khoảng hở thì khoảng hở được đo dưới vách ngăn và bằng đường rò.",
                "Figure 12.7 · Creepage distances and clearances in the case of "
                "ribs (continued on p. 307). Notes: (1) In addition to a minimum "
                "of 1 mm the rib must be sufficiently wide to be mechanically "
                "sound. (2) The rib must be 2.5mm minimum height or it will be "
                "discounted and creepage distances and clearances measured "
                "directly across the horizontal surfaces. (3) If creepage "
                "distance is shorter than clearance then clearance will be "
                "measured under barrier and be equal to creepage distance.",
                "Sáu mặt cắt gờ giữa hai dây dẫn trên tấm cách điện. Gờ rộng "
                "\u22651 mm (note 1) với nhãn Rib (note 2) bắt đường rò chấm đỏ "
                "đi vượt qua đỉnh gờ; gờ hẹp <1 mm bị bỏ qua nên đường rò đi "
                "thẳng. Có gờ nguyên khối, gờ xi măng (Insulating cemented "
                "joint) và gờ không xi măng (Non-cemented joint) với Clearance "
                "(Note 3). Khoảng hở là đường gạch đứt xanh; hai hình cuối là "
                "phần tiếp theo ở tr. 307. Ghi chú (1) gờ phải đủ rộng; (2) gờ "
                "cao tối thiểu 2,5 mm nếu không bị bỏ qua; (3) nếu đường rò ngắn "
                "hơn khoảng hở thì đo khoảng hở dưới vách ngăn.",
                "Six rib sections between two conductors on insulating material. "
                "A rib \u22651 mm wide (note 1), labelled Rib (note 2), makes the "
                "dotted red creepage path climb over its top; a rib <1 mm is "
                "discounted so creepage runs straight across. Variants include "
                "an integral rib, an Insulating cemented joint and a "
                "Non-cemented joint with Clearance (Note 3). Clearance is the "
                "dashed blue line; the last two panels are continued on p. 307. "
                "Notes: (1) the rib must be sufficiently wide; (2) it must be at "
                "least 2.5mm high or be discounted; (3) if creepage is shorter "
                "than clearance, clearance is measured under the barrier.")


# ------------------------------------------------------------------ 12.8

@_reg
def fig_f1208():
    """Figure 12.8 - effects of screws and bolts on creepage distances."""
    w, h = 680, 340
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 8, "Ảnh hưởng của vít và bulông đến đường rò và khoảng hở",
           "Effects of screws and bolts on creepage distances and clearances")
    _legend(o, 36)

    o.append(_screw_panel(46, "a", metal=False))
    o.append(_screw_panel(170, "b", metal=True))
    o.append(T(340, 308,
               "a = Separation equal to or greater than 2.5 mm (1.5 mm if total "
               "creepage distance required is equal to or less than 3 mm)",
               6.8, color=GREY))
    o.append(T(340, 320,
               "b = Separation equal to or less then 2.5 mm (or 1.5 mm if total "
               "creepage distance required is equal to or less than 3 mm)",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.8")),
                "Hình 12.8 · Ảnh hưởng của vít và bulông đến đường rò và khoảng hở",
                "Figure 12.8 · Effects of screws and bolts on creepage distances "
                "and clearances",
                "Hai mặt cắt cách điện có ba dây dẫn và hai chỗ lõm chứa vít. "
                "(a) Vít nhựa (Insulating plastic screws): đường rò chấm đỏ đi "
                "xuống đáy mỗi lỗ vít rồi lên dây dẫn kế tiếp; khoảng hở gạch "
                "đứt xanh đi thẳng giữa các dây dẫn. (b) Vít kim loại "
                "(Conducting metal screws) bố trí tương tự. Các kích thước a và "
                "b được chú thích: a = khoảng cách lớn hơn hoặc bằng 2,5 mm "
                "(1,5 mm nếu tổng đường rò yêu cầu không vượt quá 3 mm); b = "
                "khoảng cách nhỏ hơn hoặc bằng 2,5 mm (hoặc 1,5 mm trong trường "
                "hợp tương tự).",
                "Two insulating sections each with three conductors and two "
                "recessed screw holes. (a) Insulating plastic screws: the dotted "
                "red creepage path dips to the bottom of each screw recess before "
                "rising to the next conductor, while the dashed blue clearance "
                "runs straight between conductors. (b) Conducting (Metal) screws "
                "in the same arrangement. Dimensions a and b are noted: a = "
                "separation equal to or greater than 2.5 mm (1.5 mm if total "
                "creepage distance required is equal to or less than 3 mm); b = "
                "separation equal to or less then 2.5 mm (or 1.5 mm in the same "
                "case).")
