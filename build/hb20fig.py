# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 20 — Mass and Weight Measurement
(Mark Fritz and Emil Hazarian, Denver Instrument Company).

The source chapter contains exactly three figures (20.1–20.3).
FIGS is a 3-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah20" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah20g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah20", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=12):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="6" fill="%s" stroke="%s" stroke-width="1.4"/>'
         % (_f(x), _f(y), _f(w), _f(h), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _pan(cx, y, w=76):
    """Shallow weighing-pan bowl hanging below the suspension point."""
    return ('<path d="M%s %s L%s %s L%s %s Q%s %s %s %s Z" fill="#ffffff" stroke="%s" '
            'stroke-width="1.4"/>'
            % (_f(cx - w / 2.0), _f(y), _f(cx + w / 2.0), _f(y), _f(cx + w / 2.0 - 9),
               _f(y + 15), _f(cx), _f(y + 24), _f(cx - w / 2.0 + 9), _f(y + 15), E))


def _dish(cx, y, w=64):
    """Shallow dish that carries the load on top of the beam."""
    return ('<path d="M%s %s Q%s %s %s %s" fill="none" stroke="%s" stroke-width="1.6"/>'
            % (_f(cx - w / 2.0), _f(y), _f(cx), _f(y + 12), _f(cx + w / 2.0), _f(y), E))


# ---------------------------------------------------------------- 20.1
def fig_20_1():
    o = [_defs()]

    # base, column, pivot, beam
    o.append('<rect x="250" y="244" width="180" height="14" rx="3" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<rect x="330" y="126" width="20" height="120" fill="#fafafa" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<polygon points="340,112 326,132 354,132" fill="#e8e8e8" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append('<line x1="118" y1="112" x2="562" y2="112" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % E)
    o.append('<circle cx="340" cy="112" r="5" fill="%s"/>' % E)

    # pointer and scale
    o.append('<line x1="340" y1="112" x2="340" y2="198" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<path d="M302 206 Q340 224 378 206" fill="none" stroke="%s" stroke-width="1.2"/>' % E)

    # suspensions and pans
    o.append('<line x1="118" y1="112" x2="118" y2="158" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="562" y1="112" x2="562" y2="158" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_pan(118, 158))
    o.append(_pan(562, 158))

    # standard weight (left) and unknown (right)
    o.append('<rect x="104" y="134" width="28" height="22" rx="2" fill="#fdf6e3" '
             'stroke="%s" stroke-width="1.1"/>' % G)
    o.append('<circle cx="562" cy="146" r="11" fill="#eef2f7" stroke="%s" stroke-width="1.1"/>' % E)

    # equal-arm dimension
    o.append('<line x1="118" y1="82" x2="118" y2="92" stroke="%s" stroke-width="1"/>' % S)
    o.append('<line x1="340" y1="82" x2="340" y2="92" stroke="%s" stroke-width="1"/>' % S)
    o.append('<line x1="562" y1="82" x2="562" y2="92" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(120, 88, 332, 88, S, "ah20", 1.0))
    o.append(_arr(332, 88, 120, 88, S, "ah20", 1.0))
    o.append(_arr(348, 88, 560, 88, S, "ah20", 1.0))
    o.append(_arr(560, 88, 348, 88, S, "ah20", 1.0))

    # labels
    o.append(_lbl(340, 64, "Hai cánh tay đòn bằng nhau", "tb", "middle"))
    o.append(_lbl(226, 78, "L", "tb", "middle"))
    o.append(_lbl(454, 78, "L", "tb", "middle"))
    o.append(_lbl(140, 104, "Đòn cân", "t"))
    o.append(_lbl(362, 140, "Điểm tựa", "t"))
    o.append(_lbl(348, 182, "Kim chỉ", "t"))
    o.append(_lbl(388, 216, "Thang chia", "t"))
    o.append(_lbl(118, 208, "Đĩa cân — chuẩn", "ts", "middle"))
    o.append(_lbl(562, 208, "Đĩa cân — vật cần đo", "ts", "middle"))
    return _fig(
        svg(680, 262, "".join(o), "Sơ đồ cân hai đĩa có tay đòn bằng nhau"),
        "Hình 20.1 · Cân hai đĩa có tay đòn bằng nhau (cân Ainsworth dòng FV). Vật cần đo đặt trên "
        "đĩa phải được cân bằng với quả chuẩn trên đĩa trái; khi đòn cân nằm ngang thì khối lượng "
        "hai bên bằng nhau, nhờ đó đọc được khối lượng chưa biết.",
        "Figure 20.1 · Equal-arm two-pan balance (Ainsworth FV series). The unknown on the right pan "
        "is balanced against a standard on the left; when the beam is level the two masses are equal, "
        "which yields the unknown mass.",
        "Sơ đồ cân hai đĩa: trụ đứng, đòn ngang, hai đĩa treo cách đều điểm tựa, kim chỉ và thang chia",
        "Two-pan equal-arm balance: column, horizontal beam, two pans equidistant from the pivot, "
        "pointer and scale")


# ---------------------------------------------------------------- 20.2
def fig_20_2():
    o = [_defs()]

    o.append('<rect x="170" y="244" width="220" height="14" rx="3" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<rect x="240" y="136" width="20" height="110" fill="#fafafa" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<polygon points="250,116 236,138 264,138" fill="#e8e8e8" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append('<line x1="116" y1="116" x2="630" y2="116" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % E)
    o.append('<circle cx="250" cy="116" r="5" fill="%s"/>' % E)

    o.append('<line x1="250" y1="116" x2="250" y2="192" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<path d="M214 200 Q250 218 286 200" fill="none" stroke="%s" stroke-width="1.2"/>' % E)

    o.append('<line x1="116" y1="116" x2="116" y2="158" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_pan(116, 158))
    o.append('<circle cx="116" cy="147" r="10" fill="#eef2f7" stroke="%s" stroke-width="1.1"/>' % E)

    # notched positions along the beam
    for x in (300, 340, 380, 420, 460, 500, 540, 580, 620):
        o.append('<line x1="%d" y1="116" x2="%d" y2="123" stroke="%s" stroke-width="1.1"/>'
                 % (x, x, E))

    # sliding weights
    o.append('<rect x="322" y="100" width="20" height="16" rx="2" fill="#fdf6e3" '
             'stroke="%s" stroke-width="1.2"/>' % G)
    o.append('<rect x="462" y="98" width="26" height="18" rx="2" fill="#eef2f7" '
             'stroke="%s" stroke-width="1.2"/>' % E)

    o.append(_lbl(140, 106, "Đòn cân", "t"))
    o.append(_lbl(272, 152, "Điểm tựa", "t"))
    o.append(_lbl(260, 182, "Kim chỉ", "t"))
    o.append(_lbl(296, 214, "Thang chia", "t"))
    o.append(_lbl(332, 92, "Quả trượt nhỏ", "ts", "middle"))
    o.append(_lbl(475, 90, "Quả trượt lớn", "ts", "middle"))
    o.append(_lbl(632, 142, "Khấc chia độ", "ts", "end"))
    o.append(_lbl(116, 208, "Đĩa cân", "ts", "middle"))
    o.append(_lbl(400, 274, "Cánh tay đòn càng dài thì mô-men do quả trượt tạo ra càng lớn",
                  "ts", "middle"))
    return _fig(
        svg(680, 284, "".join(o), "Sơ đồ cân đòn một đĩa có quả trượt"),
        "Hình 20.2 · Cân đòn (beam balance). Chỉ có một đĩa cân, đòn được đặt lệch và một bộ quả "
        "trượt gắn trên đòn. Khi các quả trượt dịch ra xa điểm tựa, chúng có lợi thế cơ học; vị trí "
        "của từng quả trượt trên các khấc chia độ cho biết lực do nó tác dụng, và tổng các lực này "
        "là khối lượng của vật cần đo.",
        "Figure 20.2 · Beam balance. A single pan, an offset beam and a set of sliding weights. As the "
        "weights slide outward they gain mechanical advantage; the position of each weight on the "
        "notched beam indicates the force it applies, and the sum gives the mass of the unknown.",
        "Sơ đồ cân đòn: một đĩa cân, đòn lệch, các quả trượt trên khấc chia độ, kim chỉ và thang chia",
        "Beam balance: one pan, offset beam, sliding weights on notched positions, pointer and scale")


# ---------------------------------------------------------------- 20.3
def fig_20_3():
    o = [_defs()]

    # beam, fulcrum, base
    o.append('<line x1="66" y1="116" x2="388" y2="116" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % E)
    o.append('<polygon points="170,116 156,136 184,136" fill="#e8e8e8" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append('<rect x="164" y="136" width="12" height="50" fill="#fafafa" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<rect x="120" y="186" width="110" height="12" rx="3" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.2"/>' % E)

    # pan, stem, load
    o.append('<line x1="66" y1="116" x2="66" y2="90" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_dish(66, 84))
    o.append('<rect x="46" y="58" width="40" height="24" rx="3" fill="#eef2f7" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(66, 74, "Tải", "tb", "middle"))

    # null detector: LED, vane, photodiode
    o.append('<line x1="250" y1="116" x2="250" y2="92" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<rect x="246" y="78" width="8" height="14" fill="#dddddd" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append(_box(192, 74, 34, 20, "LED", E, "#ffffff", 9))
    o.append(_box(272, 74, 34, 20, "PD", E, "#ffffff", 9))
    o.append(_arr(228, 84, 242, 84, G, "ah20g", 1.2))
    o.append(_arr(258, 84, 270, 84, G, "ah20g", 1.2))

    # magnet and coil
    o.append('<rect x="374" y="74" width="58" height="20" fill="#eef2f7" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append('<rect x="374" y="142" width="58" height="20" fill="#fdf2ee" stroke="%s" '
             'stroke-width="1.2"/>' % E)
    o.append(_lbl(403, 89, "N", "tb", "middle"))
    o.append(_lbl(403, 157, "S", "tb", "middle"))
    o.append('<rect x="388" y="100" width="34" height="34" rx="4" fill="#fafafa" '
             'stroke="%s" stroke-width="1.6"/>' % G)

    # coil wiring to the servo electronics
    o.append('<path d="M422 117 L452 117 L452 200 L355 200 L355 212" fill="none" stroke="%s" '
             'stroke-width="1.4" marker-end="url(#ah20)"/>' % E)
    o.append(_box(300, 212, 110, 46, "Bộ khuếch đại\n(servo)", E, "#ffffff", 10))
    o.append(_arr(410, 235, 430, 235, E, "ah20", 1.4))
    o.append(_box(432, 220, 80, 30, "R cảm biến", E, "#fdf6e3", 10))
    o.append(_arr(512, 235, 532, 235, E, "ah20", 1.4))
    o.append(_box(534, 212, 116, 46, "Hiển thị số", E, "#ffffff", 11))

    # labels
    o.append(_lbl(250, 56, "Bộ phát hiện điểm không (LED + quang đi-ốt)", "ts", "middle"))
    o.append(_lbl(110, 88, "Đĩa cân", "t"))
    o.append(_lbl(120, 108, "Thanh đòn", "t"))
    o.append(_lbl(196, 142, "Điểm tựa lệch", "t"))
    o.append(_lbl(436, 68, "Nam châm vĩnh cửu", "ts"))
    o.append(_lbl(470, 172, "Cuộn dây trong từ trường", "ts"))
    o.append(_lbl(458, 196, "dòng bù i", "ts"))
    return _fig(
        svg(680, 272, "".join(o), "Sơ đồ load cell hoàn lực của cân điện tử"),
        "Hình 20.3 · Load cell hoàn lực (force restorative load cell) — lõi của cân điện tử. Khi đặt "
        "tải, thanh đòn lệch khỏi vị trí cân bằng; bộ phát hiện điểm không gồm LED và quang đi-ốt nhận "
        "ra độ lệch và dòng điện trong cuộn dây (đặt trong từ trường của nam châm) được tăng lên để "
        "kéo đòn về cân bằng. Dòng điện này được đo trên một điện trở cảm biến chính xác rồi chuyển "
        "thành số chỉ khối lượng.",
        "Figure 20.3 · Force-restorative load cell, the heart of an electronic balance. When a load is "
        "applied the beam leaves equilibrium; a null detector made of an LED and a photodiode senses the "
        "deflection and the current in the coil (suspended in a magnetic field) is increased until the "
        "beam is restored. That current is measured across a precision sense resistor and converted "
        "into a mass reading.",
        "Sơ đồ load cell hoàn lực: đĩa cân, thanh đòn có điểm tựa lệch, LED và quang đi-ốt phát hiện "
        "điểm không, cuộn dây giữa hai cực nam châm, bộ khuếch đại, điện trở cảm biến và hiển thị số",
        "Force-restorative load cell: pan, offset-fulcrum beam, LED/photodiode null detector, coil "
        "between magnet poles, servo amplifier, sense resistor and digital readout")


FIGS = [fig_20_1, fig_20_2, fig_20_3]


def fig(n):
    return FIGS[n - 1]()
