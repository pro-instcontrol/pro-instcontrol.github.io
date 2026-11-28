# -*- coding: utf-8 -*-
"""Vector redraws of Figures 11.1-11.8 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 11 "Apparatus with protection
concept pressurization 'p'".

Every drawing is a simplified vector redraw of the authoritative rendered
pages p298, p310-p314.  Printed English captions (including the Note. line of
Fig. 11.3) are reproduced verbatim with a bilingual prefix; printed box labels,
legend words and pressure values are transcribed onto the drawings.  Each
public callable returns the standard five-tuple through ``vfig._fig()`` on a
680x300 canvas and is registered in ``FIGS`` by the ``_reg`` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _ellipse, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _defs11():
    """Arrow markers used by all eight drawings."""
    return ('<defs>'
            '<marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<marker id="a6s" markerWidth="6" markerHeight="6" refX="5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="%s"/></marker>'
            '</defs>' % (INK, INK))


def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 11.%d · %s / Figure 11.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, size=5.5):
    o.append(T(340, 27, s, size, color=GREY))


def _bx(x, y, w, h, label, size=5.2, fill="#fff", sw=1.0, weight=""):
    """Rectangular box (square corners, as printed) with centred label."""
    o = [_rect(x, y, w, h, fill=fill, sw=sw)]
    lines = label.split("\n")
    cy = y + h / 2.0 + (0 if len(lines) == 1 else -size * 0.5)
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, cy + i * (size + 0.9), ln, size, weight=weight))
    return "".join(o)


def _ortho(pts, sw=0.9, color=INK):
    """Orthogonal connector: plain segments plus an arrow on the last one."""
    o = []
    for a, b in zip(pts, pts[1:]):
        if b == pts[-1]:
            o.append(_arrow(a[0], a[1], b[0], b[1], sw=sw, color=color, head="a6s"))
        else:
            o.append(_line(a[0], a[1], b[0], b[1], sw=sw, color=color))
    return "".join(o)


def _lead(x1, y1, x2, y2):
    return _arrow(x1, y1, x2, y2, sw=0.8, color=GREY, head="a6s")


def _wavy(x, y, w, n=4):
    d = "M %s %s" % (x, y)
    seg = w / float(n)
    for i in range(n):
        yy = y - 5 if i % 2 == 0 else y + 5
        d += " Q %s %s %s %s" % (x + (i + 0.5) * seg, yy, x + (i + 1) * seg, y)
    return _path(d, sw=1.0)


def _valve(cx, cy, r=8):
    """The printed bow-tie outlet-control valve symbol."""
    return (_poly([(cx - r, cy - r), (cx, cy), (cx - r, cy + r)],
                  fill="#fff", sw=1.0, close=True)
            + _poly([(cx + r, cy - r), (cx, cy), (cx + r, cy + r)],
                    fill="#fff", sw=1.0, close=True))


def _fan(cx, cy, r=14):
    o = [_circle(cx, cy, r, fill="#fff", sw=1.2)]
    o.append(_path("M %s %s Q %s %s %s %s M %s %s Q %s %s %s %s M %s %s Q %s %s %s %s"
                   % (cx, cy, cx + 8, cy - 10, cx + 12, cy,
                      cx, cy, cx - 8, cy + 10, cx - 12, cy,
                      cx, cy, cx + 6, cy + 10, cx + 10, cy), sw=1.0))
    return "".join(o)


# ------------------------------------------------------------------ 11.1

@_reg
def fig_f1101():
    """Figure 11.1 - use of pressurization: the decision flowchart."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Sử dụng áp suất dương", "Use of pressurization", 7.2)
    _sub(o, "Sơ đồ lựa chọn phương pháp / Method-selection flowchart", 5.4)

    def bx(x, y, bw, bh, label, size=5.2):
        o.append(_bx(x, y, bw, bh, label, size))

    def link(pts):
        o.append(_ortho(pts))

    def lab(x, y, s, size=4.6):
        o.append(T(x, y, s, size))

    # Top spine and the first decision.
    bx(288, 38, 104, 18, "Pressurized\nenclosure", 5.2)
    link([(340, 56), (340, 66)])
    bx(262, 66, 156, 20, "Is there an internal release?", 5.6)
    link([(262, 76), (170, 76), (170, 96)])
    link([(418, 76), (510, 76), (510, 96)])
    lab(212, 72, "No")
    lab(468, 72, "Yes")

    # Second pair of decisions: "Do people enter?".
    bx(132, 96, 76, 20, "Do people\nenter?", 5.4)
    bx(472, 96, 76, 20, "Do people\nenter?", 5.4)
    link([(132, 106), (72, 106), (72, 122)])
    link([(208, 106), (280, 106), (280, 122)])
    lab(100, 102, "No")
    lab(244, 102, "Yes")
    link([(472, 106), (400, 106), (400, 122)])
    link([(548, 106), (592, 106), (592, 122)])
    lab(436, 102, "No")
    lab(570, 102, "Yes")

    # Equipment boxes under the second decisions.
    bx(32, 122, 80, 30, "Instruments,\nswitch gear,\nmotors, etc.", 4.8)
    bx(232, 122, 96, 30,
       "Control rooms,\nswitch rooms,\naccommodation,\nworkshops", 4.5)
    bx(356, 122, 88, 30, "Analysers,\nchromatographs,\netc.", 4.8)
    bx(540, 122, 126, 32, "Analyser houses,\nand cabins,\netc.", 4.8)

    # No / No: three method boxes fan out, each with its own gas label.
    link([(72, 152), (72, 158)])
    o.append(_line(50, 158, 176, 158, sw=0.9))
    link([(50, 158), (50, 164)])
    link([(111, 158), (111, 164)])
    link([(176, 158), (176, 164)])
    bx(18, 164, 58, 26, "Static,\npressurization", 4.8)
    bx(82, 164, 58, 26, "Pressurization\nwith leakage\ncompensation", 4.3)
    bx(146, 164, 58, 26, "Pressurization\nwith continuous\ndilution", 4.3)
    link([(47, 190), (47, 196)])
    link([(111, 190), (111, 196)])
    link([(175, 190), (175, 196)])
    bx(26, 196, 42, 24, "Inert gas\nonly", 4.6)
    bx(90, 196, 42, 24, "Air or\ninert gas", 4.6)
    bx(154, 196, 42, 24, "Air or\ninert gas", 4.6)
    o.append(_line(47, 220, 47, 226, sw=0.9))
    o.append(_line(111, 220, 111, 226, sw=0.9))
    o.append(_line(175, 220, 175, 226, sw=0.9))
    o.append(_line(47, 226, 175, 226, sw=0.9))
    link([(111, 226), (111, 230)])
    bx(62, 230, 98, 16, "BS/EN 50016", 5.4)

    # No / Yes: continuous dilution only, air only, Installation Code.
    link([(280, 152), (280, 164)])
    bx(244, 164, 72, 26, "Continuous\ndilution only", 4.8)
    link([(280, 190), (280, 196)])
    bx(266, 196, 28, 20, "Air\nonly", 4.8)
    link([(280, 216), (280, 224)])
    bx(252, 224, 56, 18, "Installation\nCode", 4.8)

    # Yes / No: "Can internal release be limited and specified?".
    link([(400, 152), (400, 158)])
    bx(336, 158, 168, 22, "Can internal release be limited and specified?", 5.0)
    o.append(_line(378, 180, 378, 182, sw=0.9))
    o.append(_line(353, 182, 403, 182, sw=0.9))
    o.append(_line(478, 180, 478, 182, sw=0.9))
    o.append(_line(453, 182, 503, 182, sw=0.9))
    for xx in (353, 403, 453, 503):
        o.append(_line(xx, 182, xx, 186, sw=0.9))
    lab(350, 178, "No")
    lab(490, 178, "Yes")
    bx(330, 186, 46, 28, "Pressurization\nwith leakage\ncompensation", 4.1)
    bx(380, 186, 46, 28, "Pressurization\nwith continuous\ndilution", 4.1)
    bx(430, 186, 46, 28, "Pressurization\nwith leakage\ncompensation", 4.1)
    bx(480, 186, 46, 28, "Pressurization\nwith continuous\ndilution", 4.1)
    for xx in (353, 403, 453, 503):
        link([(xx, 214), (xx, 218)])
    bx(336, 218, 34, 18, "Inert gas\nonly", 4.3)
    bx(386, 218, 34, 18, "Inert gas\nonly", 4.3)
    bx(436, 218, 34, 18, "Inert gas\nonly", 4.3)
    bx(486, 218, 34, 18, "Air or\ninert gas", 4.3)
    o.append(_line(353, 236, 353, 240, sw=0.9))
    o.append(_line(403, 236, 403, 240, sw=0.9))
    o.append(_line(353, 240, 403, 240, sw=0.9))
    link([(378, 240), (378, 244)])
    bx(344, 244, 72, 14, "BS/EN 50016", 4.8)
    o.append(_line(453, 236, 453, 240, sw=0.9))
    o.append(_line(503, 236, 503, 240, sw=0.9))
    o.append(_line(453, 240, 503, 240, sw=0.9))
    link([(478, 240), (478, 244)])
    bx(444, 244, 72, 14, "BS/EN 50016", 4.8)

    # Yes / Yes: "Can interior release be limited and specified?".
    link([(592, 154), (592, 158)])
    bx(536, 158, 132, 22, "Can interior release be limited and specified?", 4.8)
    link([(561, 180), (561, 188)])
    bx(536, 188, 50, 20, "Not\npermitted", 4.8)
    link([(630, 180), (630, 186)])
    bx(592, 186, 76, 28, "Pressurization\nwith continuous\ndilution", 4.2)
    link([(630, 214), (630, 222)])
    bx(614, 222, 32, 20, "Air\nonly", 4.8)
    link([(630, 242), (630, 246)])
    bx(602, 246, 56, 16, "Installation\nCode", 4.6)
    lab(550, 178, "No")
    lab(610, 178, "Yes")

    return _fig(svg(w, h, "".join(o), esc("Fig 11.1")),
                "Hình 11.1 · Sử dụng áp suất dương",
                "Figure 11.1 · Use of pressurization",
                "Sơ đồ quyết định bắt đầu từ Pressurized enclosure và câu hỏi "
                "Is there an internal release. Nhánh No hỏi Do people enter: "
                "No dẫn đến Instruments, switch gear, motors, gồm Static, "
                "pressurization, Pressurization with leakage compensation và "
                "Pressurization with continuous dilution với nhãn khí riêng và "
                "BS/EN 50016; Yes dẫn đến Control rooms, switch rooms, "
                "accommodation, workshops rồi Continuous dilution only, Air "
                "only, Installation Code. Nhánh Yes hỏi Do people enter: No "
                "dẫn đến Analysers, chromatographs, etc. và câu hỏi Can internal "
                "release be limited and specified với các cặp phương pháp và "
                "BS/EN 50016; Yes dẫn đến Analyser houses, and cabins, etc., "
                "câu hỏi Can interior release be limited and specified, rồi "
                "Not permitted hoặc Pressurization with continuous dilution, "
                "Air only, Installation Code",
                "Decision flowchart starting at Pressurized enclosure with the "
                "question Is there an internal release. The No branch asks Do "
                "people enter: No leads to Instruments, switch gear, motors "
                "with Static, pressurization, Pressurization with leakage "
                "compensation and Pressurization with continuous dilution, "
                "each with its gas label and BS/EN 50016; Yes leads to Control "
                "rooms, switch rooms, accommodation, workshops, then Continuous "
                "dilution only, Air only, Installation Code. The Yes branch asks "
                "Do people enter: No leads to Analysers, chromatographs, etc. "
                "and Can internal release be limited and specified with pairs "
                "of methods and BS/EN 50016; Yes leads to Analyser houses, and "
                "cabins, etc., Can interior release be limited and specified, "
                "then Not permitted or Pressurization with continuous dilution, "
                "Air only, Installation Code")


# ------------------------------------------------------------------ 11.2

@_reg
def fig_f1102():
    """Figure 11.2 - disconnection on pressure failure."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Ngắt nguồn và mạch điện khi áp suất giảm",
           "Disconnection of electrical supplies and circuits on pressure failure", 6.8)
    _sub(o, "Sơ đồ liên khóa · công tắc áp suất / Interlock schematic · pressure switch", 5.5)

    # Hazardous / non-hazardous divider.
    o.append(_line(360, 48, 360, 256, sw=1.2))
    T(322, 44, "Hazardous", 5.8)
    T(322, 52, "area", 5.8)
    T(420, 44, "Non-hazardous", 5.8)
    T(420, 52, "area", 5.8)

    # Control supply loop and the relay/coil on the control line.
    T(570, 44, "Control", 6.0)
    T(570, 52, "supply", 6.0)
    o.append(_line(556, 64, 500, 64, sw=1.0))
    o.append(_line(500, 64, 500, 108, sw=1.0))
    o.append(_rect(466, 102, 20, 12, fill="#fff", sw=1.1))
    o.append(_line(486, 108, 500, 108, sw=1.0))
    o.append(_line(466, 108, 320, 108, sw=1.0))

    # Changeover switch inside its small box.
    o.append(_rect(270, 96, 50, 24, fill="#fff", sw=1.1))
    o.append(_circle(278, 104, 1.8, fill=INK, sw=0))
    o.append(_circle(278, 112, 1.8, fill=INK, sw=0))
    o.append(_line(278, 104, 310, 114, sw=1.2))
    o.append(_ortho([(295, 120), (295, 136), (250, 136), (250, 150)]))

    # Pressure switch leader and the pressurized enclosure.
    T(100, 88, "Pressure switch", 5.6, anchor="start")
    T(100, 96, "with separate", 5.6, anchor="start")
    T(100, 104, "protection", 5.6, anchor="start")
    T(100, 112, "concept", 5.6, anchor="start")
    o.append(_lead(178, 106, 276, 104))
    o.append(_rect(180, 150, 120, 64, fill="#fff", sw=1.1))
    o.append(_wavy(180, 214, 120, 4))
    T(240, 180, "Pressurized", 6.2)
    T(240, 188, "enclosure", 6.2)

    # Two ganged pairs of open blades on the right-hand conductors.
    o.append(_line(470, 136, 470, 226, sw=1.0, dash="4 3"))
    for yy in (146, 206):
        o.append(_line(320, yy, 470, yy, sw=1.0))
        o.append(_line(320, yy + 12, 470, yy + 12, sw=1.0))
        o.append(_line(432, yy + 4, 466, yy - 6, sw=1.3))
        o.append(_line(432, yy + 16, 466, yy + 6, sw=1.3))
        o.append(_circle(478, yy, 2, fill=INK, sw=0))
        o.append(_circle(478, yy + 12, 2, fill=INK, sw=0))
        o.append(_line(478, yy, 510, yy, sw=1.0))
        o.append(_line(478, yy + 12, 510, yy + 12, sw=1.0))
    T(390, 176, "Other", 5.6)
    T(390, 184, "electrical")
    T(390, 192, "circuits")
    T(390, 234, "Power", 5.6)
    T(390, 242, "supply")
    T(390, 250, "circuits")

    return _fig(svg(w, h, "".join(o), esc("Fig 11.2")),
                "Hình 11.2 · Ngắt nguồn điện và mạch điện khi áp suất giảm",
                "Figure 11.2 · Disconnection of electrical supplies and circuits on pressure failure",
                "Sơ đồ có đường phân chia thẳng đứng giữa vùng nguy hiểm và vùng "
                "không nguy hiểm. Bên phải là nguồn Control supply nối qua cuộn "
                "relay đến công tắc chuyển mạch; nhãn Pressure switch with "
                "separate protection concept có mũi tên chỉ vào công tắc, dây "
                "dẫn xuống vỏ Pressurized enclosure có đáy gãy lượn sóng. Bên "
                "phải có hai cặp lưỡi dao hở được liên động, dây gạch đứt và "
                "các đầu nối đen, với nhãn Other electrical circuits và Power "
                "supply circuits",
                "Schematic with a vertical divider between the hazardous and "
                "non-hazardous areas. At the right the Control supply loops "
                "through a relay coil to a changeover switch; the four-line "
                "Pressure switch with separate protection concept leader points "
                "to that switch and a lead drops into the Pressurized enclosure "
                "with its wavy bottom. On the right two pairs of ganged open "
                "blades sit on conductors with a dashed line and filled terminal "
                "dots, labelled Other electrical circuits and Power supply "
                "circuits")


# ------------------------------------------------------------------ 11.3

@_reg
def fig_f1103():
    """Figure 11.3 - defeating of control system, two arrangements."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Làm vô hiệu hóa hệ thống điều khiển", "Defeating of control system", 7.2)
    _sub(o, "Note. The preferred method ensures the repurge of the enclosure "
            "after reinstatement of pressure.", 5.4)

    # Upper arrangement: NOT PREFERRED.
    T(120, 58, "Purged", 6.0)
    T(120, 66, "enclosure", 6.0)
    o.append(_rect(60, 72, 120, 72, fill="#fff", sw=1.1))
    T(120, 82, "Electrical", 5.8)
    T(120, 90, "equipment", 5.8)
    o.append(_rect(90, 96, 60, 42, fill="#fff", sw=1.0))
    o.append(_circle(104, 106, 6, fill="#fff", sw=1.0))
    o.append(_circle(136, 106, 6, fill="#fff", sw=1.0))
    o.append(_rect(100, 118, 40, 8, fill="#fff", sw=0.9))
    o.append(_rect(104, 130, 32, 5, fill=INK, sw=0))
    o.append(_line(180, 104, 228, 104, sw=1.0))
    o.append(_line(180, 114, 228, 114, sw=1.0))
    o.append(_circle(240, 109, 12, fill="#fff", sw=1.2))
    o.append(_line(230, 109, 250, 109, sw=1.0))
    o.append(_circle(234, 109, 1.8, fill=INK, sw=0))
    o.append(_circle(246, 109, 1.8, fill=INK, sw=0))
    T(260, 112, "Pressure switch", 6.0, anchor="start")
    o.append(_line(230, 109, 230, 150, sw=1.0))
    o.append(_line(250, 109, 250, 152, sw=1.0))
    o.append(_circle(230, 124, 2, fill=INK, sw=0))
    o.append(_rect(280, 118, 64, 28, fill="#fff", sw=1.1))
    o.append(_circle(288, 126, 2, fill=INK, sw=0))
    o.append(_circle(288, 138, 2, fill=INK, sw=0))
    o.append(_line(288, 126, 336, 132, sw=1.3))
    o.append(_ortho([(230, 124), (230, 126), (280, 126)]))
    o.append(_circle(312, 152, 4, fill="none", sw=0.9))
    o.append(_line(312, 148, 312, 140, sw=0.9))
    T(352, 128, "Key operated", 5.8, anchor="start")
    T(352, 136, "switch", 5.8, anchor="start")
    o.append(_arrow(250, 145, 420, 145, sw=1.0))
    o.append(_arrow(250, 155, 420, 155, sw=1.0))
    T(430, 145, "To control", 5.8, anchor="start")
    T(430, 153, "unit", 5.8, anchor="start")
    T(600, 100, "NOT PREFERRED", 7.0, weight="600")

    # Lower arrangement: PREFERRED.
    T(600, 180, "PREFERRED", 7.0, weight="600")
    T(120, 174, "Contactor", 6.0)
    o.append(_rect(60, 180, 130, 46, fill="#fff", sw=1.1))
    for xx in (80, 95, 110, 125):
        o.append(_circle(xx, 196, 2, fill=INK, sw=0))
        o.append(_line(xx, 196, xx, 252, sw=1.0))
    o.append(_rect(150, 188, 18, 22, fill=INK, sw=0))
    for xx, s in ((80, "L1"), (95, "L2"), (110, "L3"), (125, "N")):
        T(xx, 262, s, 5.6)
    o.append(_arrow(420, 190, 200, 190, sw=1.0))
    o.append(_arrow(420, 202, 200, 202, sw=1.0))
    T(430, 190, "From control", 5.8, anchor="start")
    T(430, 198, "unit", 5.8, anchor="start")
    o.append(_arrow(420, 216, 250, 216, sw=1.0))
    T(430, 220, "Power", 5.8, anchor="start")
    o.append(_ortho([(250, 216), (250, 228), (280, 228)]))
    o.append(_rect(280, 228, 64, 24, fill="#fff", sw=1.1))
    o.append(_circle(288, 236, 2, fill=INK, sw=0))
    o.append(_circle(288, 244, 2, fill=INK, sw=0))
    o.append(_line(288, 244, 336, 244, sw=1.3))
    o.append(_circle(312, 260, 4, fill="none", sw=0.9))
    o.append(_line(312, 256, 312, 252, sw=0.9))
    T(352, 236, "Key operated", 5.8, anchor="start")
    T(352, 244, "switch", 5.8, anchor="start")

    return _fig(svg(w, h, "".join(o), esc("Fig 11.3")),
                "Hình 11.3 · Làm vô hiệu hóa hệ thống điều khiển. Lưu ý: Phương pháp "
                "ưu tiên đảm bảo thực hiện lại việc thổi sạch vỏ bọc sau khi áp suất "
                "được khôi phục",
                "Figure 11.3 · Defeating of control system. Note. The preferred method "
                "ensures the repurge of the enclosure after reinstatement of pressure.",
                "Sơ đồ hai phần. Phần trên NOT PREFERRED: vỏ Purged enclosure chứa "
                "Electrical equipment và mặt đồng hồ, dây dẫn tới Pressure switch "
                "dạng vòng có thanh ngang và hai chấm, xuống công tắc Key operated "
                "switch có biểu tượng chìa khóa, rồi hai dây có mũi tên To control "
                "unit. Phần dưới PREFERRED: Contactor có bốn đầu nối và khối đen, "
                "bốn dây dẫn xuống L1 L2 L3 N, hai dây From control unit và dây "
                "Power đi qua công tắc Key operated switch thứ hai",
                "Two-part ladder. Upper NOT PREFERRED part: a Purged enclosure "
                "holds Electrical equipment and an instrument face; wires run to "
                "a circular Pressure switch with a horizontal bar and two dots, "
                "down to a Key operated switch with a key symbol, then two "
                "arrowed wires to control unit. Lower PREFERRED part: a Contactor "
                "with four terminal dots and a dark block, four conductors down "
                "to L1 L2 L3 N, two wires from control unit and a Power wire "
                "through a second Key operated switch")


# ------------------------------------------------------------------ 11.4

@_reg
def fig_f1104():
    """Figure 11.4 - pressurization using compressed gas."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Áp suất hóa bằng khí nén", "Pressurization using compressed gas", 7.2)
    _sub(o, "Sơ đồ cấp khí · đường áp suất / Gas supply · pressure profile", 5.5)

    # Cylinder and pressure regulator.
    o.append(_rect(90, 150, 30, 58, fill="#fff", sw=1.2))
    o.append(_ellipse(105, 150, 15, 5, fill="#fff", sw=1.2))
    o.append(_ellipse(105, 208, 15, 5, fill="#fff", sw=1.2))
    o.append(_rect(103, 142, 4, 8, fill="#fff", sw=1.0))
    T(78, 196, "Compressed", 6.0, anchor="end")
    T(78, 204, "gas/air", 6.0, anchor="end")
    o.append(_circle(120, 140, 3, fill="#fff", sw=1.0))
    o.append(_ortho([(120, 140), (150, 140), (160, 140)]))
    T(150, 130, "Pressure", 6.0)
    T(150, 138, "regulator", 6.0)

    # Pressurized enclosure, sensor and outlet.
    o.append(_rect(160, 96, 310, 94, fill="#fff", sw=1.3))
    T(315, 148, "Pressurized", 7.0)
    T(315, 158, "enclosure", 7.0)
    o.append(_rect(388, 80, 28, 12, fill="#fff", sw=1.1))
    o.append(_line(402, 92, 402, 96, sw=1.0))
    T(402, 64, "Pressure", 6.0)
    T(402, 72, "sensor", 6.0)
    o.append(_line(470, 140, 478, 140, sw=1.0))
    o.append(_valve(490, 140, 8))
    o.append(_arrow(498, 140, 530, 140, sw=1.0))
    T(540, 143, "Exit", 6.0, anchor="start")
    T(490, 116, "Outlet", 6.0)
    T(490, 124, "control", 6.0)

    # Pressure profile beneath the schematic.
    T(130, 222, "Cylinder pressure", 6.0, anchor="start")
    o.append(_poly([(120, 228), (200, 244)], sw=1.3))
    T(250, 238, "Regulator outlet pressure", 6.0, anchor="start")
    o.append(_poly([(200, 244), (510, 250)], sw=1.3))
    T(540, 244, "50 N/m²", 6.0, anchor="start")
    o.append(_line(100, 256, 600, 256, sw=1.0))
    T(500, 268, "Atmospheric pressure", 6.0)

    return _fig(svg(w, h, "".join(o), esc("Fig 11.4")),
                "Hình 11.4 · Áp suất hóa bằng khí nén",
                "Figure 11.4 · Pressurization using compressed gas",
                "Bình Compressed gas/air nhỏ ở bên trái cấp khí qua Pressure "
                "regulator vào vỏ Pressurized enclosure; trên vỏ có Pressure "
                "sensor, bên phải có van Outlet control và mũi tên Exit. Phía "
                "dưới là đồ thị áp suất: đường Cylinder pressure giảm xuống "
                "Regulator outlet pressure, mức 50 N/m² nằm trên đường cơ sở "
                "Atmospheric pressure",
                "A small Compressed gas/air cylinder at the left feeds through "
                "a Pressure regulator into a Pressurized enclosure; a Pressure "
                "sensor sits on top and an Outlet control valve with an Exit "
                "arrow at the right. Below, a pressure profile falls from "
                "Cylinder pressure to Regulator outlet pressure, with 50 N/m² "
                "above the Atmospheric pressure baseline")


# ------------------------------------------------------------------ 11.5

@_reg
def fig_f1105():
    """Figure 11.5 - fan pressurizing with fan at enclosure inlet."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Quạt cấp khí đặt ở đầu vào vỏ bọc",
           "Fan pressurizing with fan at enclosure inlet", 7.2)
    _sub(o, "Đường dẫn khí · áp suất dương / Ducting · pressure profile", 5.5)

    o.append(_line(250, 48, 250, 182, sw=1.0, dash="5 4"))
    T(150, 42, "Non-hazardous", 5.8)
    T(150, 50, "area", 5.8)
    T(390, 42, "Hazardous area", 5.8)

    # Ducting with the fan at the inlet, in the hazardous area.
    o.append(_line(60, 120, 280, 120, sw=1.1))
    o.append(_line(60, 136, 280, 136, sw=1.1))
    T(140, 114, "Ducting", 6.0)
    o.append(_fan(230, 128, 14))
    T(230, 104, "Fan", 6.0)

    # Pressurized enclosure, pressure switch and outlet control.
    o.append(_rect(280, 90, 190, 80, fill="#fff", sw=1.2))
    T(375, 132, "Pressurized", 6.6)
    T(375, 142, "enclosure", 6.6)
    o.append(_rect(390, 76, 20, 12, fill="#fff", sw=1.1))
    o.append(_line(400, 88, 400, 90, sw=1.0))
    T(400, 62, "Pressure", 6.0)
    T(400, 70, "switch", 6.0)
    o.append(_line(470, 124, 478, 124, sw=1.0))
    o.append(_valve(490, 124, 8))
    o.append(_line(498, 124, 520, 124, sw=1.0))
    o.append(_rect(520, 118, 24, 12, fill="#fff", sw=1.0))
    T(490, 104, "Outlet", 6.0)
    T(490, 112, "control", 6.0)

    # Pressure profile: fan delivery above, fan inlet below atmosphere.
    o.append(_poly([(160, 202), (500, 224)], sw=1.3))
    T(250, 194, "Fan delivery", 6.0)
    T(250, 202, "pressure", 6.0)
    o.append(_line(100, 228, 610, 228, sw=1.0))
    T(510, 240, "Atmospheric pressure", 6.0)
    o.append(_poly([(160, 230), (230, 244), (420, 244)], sw=1.2))
    T(200, 258, "Fan inlet", 6.0)
    T(200, 266, "pressure", 6.0)
    T(540, 222, "50 N/m² minimum", 6.0)

    return _fig(svg(w, h, "".join(o), esc("Fig 11.5")),
                "Hình 11.5 · Quạt cấp khí đặt ở đầu vào vỏ bọc",
                "Figure 11.5 · Fan pressurizing with fan at enclosure inlet",
                "Đường biên gạch đứt chia vùng không nguy hiểm bên trái và vùng "
                "nguy hiểm bên phải. Trong vùng nguy hiểm, Ducting dẫn khí qua "
                "Fan đặt ngay đầu vào vỏ Pressurized enclosure; trên vỏ có "
                "Pressure switch và van Outlet control. Đồ thị áp suất cho thấy "
                "Fan delivery pressure cao hơn Atmospheric pressure, Fan inlet "
                "pressure thấp hơn và mức 50 N/m² minimum",
                "A dashed boundary divides the non-hazardous area on the left "
                "from the hazardous area on the right. In the hazardous area "
                "Ducting carries air through a Fan at the inlet of the "
                "Pressurized enclosure; a Pressure switch and Outlet control "
                "sit on the box. The pressure profile shows Fan delivery "
                "pressure above Atmospheric pressure, Fan inlet pressure below "
                "it, and 50 N/m² minimum")


# ------------------------------------------------------------------ 11.6

@_reg
def fig_f1106():
    """Figure 11.6 - fan pressurizing with fan in non-hazardous area."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 6, "Quạt cấp khí đặt trong khu vực không nguy hiểm",
           "Fan pressurizing with fan in non-hazardous area", 7.2)
    _sub(o, "Đường dẫn khí áp suất dương · đường áp suất / Pressurized ducting · pressure profile", 5.4)

    o.append(_line(300, 48, 300, 182, sw=1.0, dash="5 4"))
    T(170, 42, "Non-hazardous", 5.8)
    T(170, 50, "area", 5.8)
    T(420, 42, "Hazardous area", 5.8)

    # Fan remote in the non-hazardous area, duct crossing the boundary.
    o.append(_fan(150, 130, 14))
    T(150, 104, "Fan", 6.0)
    o.append(_line(164, 124, 360, 124, sw=1.1))
    o.append(_line(164, 138, 360, 138, sw=1.1))
    T(250, 116, "Ducting", 6.0)

    o.append(_rect(360, 90, 170, 80, fill="#fff", sw=1.2))
    T(445, 132, "Pressurized", 6.6)
    T(445, 142, "enclosure", 6.6)
    o.append(_rect(420, 76, 20, 12, fill="#fff", sw=1.1))
    o.append(_line(430, 88, 430, 90, sw=1.0))
    T(430, 62, "Pressure", 6.0)
    T(430, 70, "switch", 6.0)
    o.append(_line(530, 124, 538, 124, sw=1.0))
    o.append(_valve(548, 124, 8))
    o.append(_line(556, 124, 580, 124, sw=1.0))
    o.append(_rect(580, 118, 24, 12, fill="#fff", sw=1.0))
    T(548, 104, "Outlet", 6.0)
    T(548, 112, "control", 6.0)

    o.append(_poly([(90, 198), (500, 222)], sw=1.3))
    T(200, 190, "Fan delivery", 6.0)
    T(200, 198, "pressure", 6.0)
    T(90, 216, "Fan inlet", 6.0, anchor="start")
    T(90, 224, "pressure", 6.0, anchor="start")
    o.append(_line(80, 228, 620, 228, sw=1.0))
    T(520, 240, "Atmospheric pressure", 6.0)
    T(580, 222, "50 N/m² minimum", 6.0)

    return _fig(svg(w, h, "".join(o), esc("Fig 11.6")),
                "Hình 11.6 · Quạt cấp khí đặt trong khu vực không nguy hiểm",
                "Figure 11.6 · Fan pressurizing with fan in non-hazardous area",
                "Đường biên gạch đứt chia vùng không nguy hiểm bên trái và vùng "
                "nguy hiểm bên phải. Fan đặt hoàn toàn trong vùng không nguy "
                "hiểm và Ducting có áp suất dương dẫn khí qua biên giới vào vỏ "
                "Pressurized enclosure; trên vỏ có Pressure switch và van "
                "Outlet control. Đồ thị áp suất ghi Fan delivery pressure, Fan "
                "inlet pressure, Atmospheric pressure và mức 50 N/m² minimum",
                "A dashed boundary divides the non-hazardous area on the left "
                "from the hazardous area on the right. The Fan sits wholly in "
                "the non-hazardous area and pressurized Ducting crosses the "
                "boundary into the Pressurized enclosure, which carries a "
                "Pressure switch and Outlet control valve. The pressure profile "
                "marks Fan delivery pressure, Fan inlet pressure, Atmospheric "
                "pressure and 50 N/m² minimum")


# ------------------------------------------------------------------ 11.7

@_reg
def fig_f1107():
    """Figure 11.7 - spark and particle arresters, three views."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 7, "Bộ bắt tia lửa và hạt", "Spark and particle arresters", 7.2)
    _sub(o, "Ba dạng phần tử chặn · labyrinth và len thép / Three barrier forms · labyrinth and wire wool", 5.4)

    # (a) End cross-section: concentric labyrinth rings.
    T(160, 52, "End cross-section", 6.4)
    for r in (12, 20, 28, 36, 44):
        o.append(_circle(160, 110, r, fill="#fff", sw=1.0))
    T(60, 72, "Labyrinth", 5.8, anchor="start")
    o.append(_lead(116, 74, 130, 88))
    T(160, 166, "Labyrinthine", 6.0)

    # (b) Lengthwise cross-section with serpentine exhaust channels.
    T(460, 52, "Lengthwise cross-section", 6.4)
    o.append(_rect(360, 72, 200, 64, fill="#fff", sw=1.1))
    for yy in (82, 94, 106, 118, 130):
        o.append(_line(366, yy, 552, yy, sw=0.9))
        o.append(_arrow(382, yy, 540, yy, sw=0.8, head="a6s"))
        o.append(_line(552, yy, 552, yy + 6, sw=0.9))
    T(330, 92, "Exhaust gas", 5.8)
    o.append(_arrow(330, 104, 360, 104, sw=1.0))
    T(590, 76, "Labyrinth", 5.8, anchor="start")
    o.append(_lead(586, 78, 556, 90))
    o.append(_poly([(560, 104), (570, 104), (566, 98), (580, 104), (566, 110)], sw=1.0))
    o.append(_arrow(580, 104, 620, 104, sw=1.0))

    # (c) Inline device filled with wire wool or rings.
    o.append(_rect(250, 196, 150, 40, fill="#fff", sw=1.1))
    o.append(_rect(390, 196, 10, 40, fill="#e8e8e8", sw=1.0))
    T(325, 210, "Filling of", 5.6)
    T(325, 218, "wire wool")
    T(325, 226, "or rings")
    T(325, 248, "Filled", 5.8)
    T(450, 190, "Retaining", 5.6, anchor="start")
    T(450, 198, "gauze", 5.6, anchor="start")
    o.append(_lead(446, 196, 396, 206))
    o.append(_path("M 180 216 Q 190 206 200 216 Q 190 226 180 216", sw=1.0))
    o.append(_arrow(200, 216, 250, 216, sw=1.0))
    o.append(_arrow(400, 216, 460, 216, sw=1.0))
    o.append(_path("M 460 216 Q 470 206 480 216 Q 470 226 460 216", sw=1.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 11.7")),
                "Hình 11.7 · Bộ bắt tia lửa và hạt",
                "Figure 11.7 · Spark and particle arresters",
                "Ba dạng thiết bị chặn tia lửa và hạt: góc trên bên trái là mặt "
                "cắt đầu End cross-section gồm các vòng đồng tâm với nhãn "
                "Labyrinth và Labyrinthine; góc trên bên phải là mặt cắt dọc "
                "Lengthwise cross-section có các kênh ngoằn ngoèo và mũi tên "
                "Exhaust gas đi qua Labyrinth; bên dưới là thiết bị nối tiếp "
                "có Filling of wire wool or rings, nhãn Filled và Retaining "
                "gauze ở đầu ra",
                "Three spark and particle barrier forms: the upper left End "
                "cross-section shows concentric rings labelled Labyrinth and "
                "Labyrinthine; the upper right Lengthwise cross-section shows "
                "serpentine channels with an Exhaust gas arrow through the "
                "Labyrinth; below, an inline device has Filling of wire wool or "
                "rings, the label Filled and a Retaining gauze at the outlet")


# ------------------------------------------------------------------ 11.8

@_reg
def fig_f1108():
    """Figure 11.8 - internal release of explosive atmosphere."""
    w, h = 680, 300
    o = [_defs11(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 8, "Phóng thích bên trong tạo khí quyển dễ nổ",
           "Internal release of explosive atmosphere", 7.2)
    _sub(o, "Vị trí linh kiện và vùng pha loãng / Component siting and the dilution area", 5.4)

    o.append(_rect(150, 68, 410, 170, fill="#fff", sw=1.3))
    T(420, 206, "Pressurized enclosure", 6.4)

    # Flammable material entering from the left.
    o.append(_arrow(90, 112, 150, 112, sw=1.0))
    o.append(_arrow(90, 150, 150, 150, sw=1.0))
    T(90, 92, "Flammable", 5.8, anchor="start")
    T(90, 100, "material", 5.8, anchor="start")

    # Leak point, plume and its long printed label.
    o.append(_circle(360, 128, 5, fill="#fff", sw=1.2))
    o.append(_ellipse(360, 128, 74, 22, fill="#f2f2f2", sw=0.9))
    T(300, 74, "Leak of", 5.6)
    T(300, 82, "flammable")
    T(300, 90, "material")
    o.append(_lead(340, 92, 358, 122))
    T(410, 44, "Plume area where possible", 5.4)
    T(410, 51, "flammable atmosphere is", 5.4)
    T(410, 58, "present during dilution", 5.4)
    o.append(_lead(410, 62, 390, 108))
    T(500, 74, "No ignition capable", 5.4)
    T(500, 81, "electrical components", 5.4)
    o.append(_lead(500, 86, 470, 116))

    # Ignition-capable components kept away from the plume.
    o.append(_rect(180, 176, 70, 32, fill="#fff", sw=1.0))
    for cx, cy in ((192, 186), (212, 186), (232, 186), (192, 198), (212, 198)):
        o.append(_circle(cx, cy, 2, fill=INK, sw=0))
    T(215, 158, "Ignition capable", 5.4)
    T(215, 165, "electrical")
    T(215, 172, "components")

    # Pollution inlet, dilution outlet and flammable exit.
    o.append(_arrow(170, 250, 170, 238, sw=1.0))
    T(120, 254, "Pollution", 5.8, anchor="start")
    T(120, 262, "inlet", 5.8, anchor="start")
    o.append(_arrow(560, 96, 620, 96, sw=1.0))
    T(630, 92, "Dilution", 5.8, anchor="start")
    T(630, 100, "outlet", 5.8, anchor="start")
    o.append(_arrow(560, 150, 620, 150, sw=1.0))
    T(628, 146, "Flammable", 5.8, anchor="start")
    T(628, 154, "material", 5.8, anchor="start")

    return _fig(svg(w, h, "".join(o), esc("Fig 11.8")),
                "Hình 11.8 · Phóng thích bên trong tạo khí quyển dễ nổ",
                "Figure 11.8 · Internal release of explosive atmosphere",
                "Vỏ Pressurized enclosure có hai mũi tên Flammable material đi "
                "vào từ bên trái và Pollution inlet ở đáy. Tại điểm rò rỉ giữa "
                "vỏ có chùm Plume area where possible flammable atmosphere is "
                "present during dilution; linh kiện Ignition capable electrical "
                "components nằm xa chùm này trong khi góc trên bên phải ghi No "
                "ignition capable electrical components. Ở mép phải là Dilution "
                "outlet và mũi tên Flammable material thoát ra",
                "A Pressurized enclosure receives two Flammable material arrows "
                "at the left and a Pollution inlet at the bottom. A central leak "
                "feeds the Plume area where possible flammable atmosphere is "
                "present during dilution; Ignition capable electrical components "
                "are kept away from it while the top right is marked No ignition "
                "capable electrical components. A Dilution outlet and a "
                "Flammable material exit arrow sit on the right edge")
