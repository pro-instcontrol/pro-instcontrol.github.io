# -*- coding: utf-8 -*-
"""Vector redraw of Figure 31-1 in Baumann Chapter 31, *Control Valve Primer*.

The printed figure is an unlabelled cross-section of a modern cage-type
control valve body subassembly, with five letter callouts (A-E) explained in
the caption. This module redraws it as a labelled bilingual schematic: flanged
body, bonnet, cage, double-stage plug, stem, the three seals and the staked
stem connection, plus the inlet flow arrow. Every function returns the
standard 5-tuple via ``_fig()`` from ``vfig``.
"""
from vfig import (BLUE, GREY, INK, RED, _arrow, _circle, _defs, _fig,
                  _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


@_reg
def fig_f311():
    """Figure 31-1 -- cage-type control valve body subassembly, callouts A-E."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 24, "Cụm thân van điều khiển kiểu lồng / Cage-type control valve body subassembly",
               10.0, color=INK, weight="600"))
    o.append(T(340, 50, "Nắp van / Bonnet", 8.4, color=INK))

    # Flanged horizontal body: hatched metal walls around a white flow passage.
    o.append(_rect(90, 170, 65, 140, fill="url(#h6)", sw=1.3))
    o.append(_rect(525, 170, 65, 140, fill="url(#h6)", sw=1.3))
    for cx in (122, 557):
        for cy in (190, 290):
            o.append(_circle(cx, cy, 7, fill="#ffffff", sw=1.0))
    o.append(_poly([(155, 185), (210, 185), (210, 150), (470, 150),
                    (470, 185), (525, 185), (525, 295), (470, 295),
                    (470, 315), (210, 315), (210, 295), (155, 295)],
                   fill="url(#h6)", sw=1.4, close=True))
    o.append(_rect(155, 215, 85, 50, fill="#ffffff", sw=1.1))
    o.append(_rect(240, 185, 200, 80, fill="#ffffff", sw=1.1))
    o.append(_rect(440, 215, 85, 50, fill="#ffffff", sw=1.1))
    # Recess in the top wall for the cage top and its two seals.
    o.append(_rect(275, 150, 130, 22, fill="#ffffff", sw=1.0))
    o.append(T(122, 162, "Mặt bích / Flange", 8.0, color=GREY))
    o.append(T(190, 333, "Thân van / Valve body", 8.0, color=GREY))

    # Bonnet with its mounting flange; the stem is drawn on top of it.
    o.append(_poly([(290, 60), (390, 60), (390, 135), (430, 135),
                    (430, 150), (250, 150), (250, 135), (290, 135)],
                   fill="url(#h7)", sw=1.4, close=True))

    # Seat ring below the plug.
    o.append(_poly([(312, 255), (368, 255), (356, 285), (324, 285)],
                   fill="url(#h6)", sw=1.2, close=True))

    # Cage: perforated cylindrical walls, top collar and threaded lower edge.
    o.append(_rect(274, 166, 132, 9, fill="url(#h6)", sw=1.2))
    o.append(_rect(280, 174, 12, 82, fill="url(#h6)", sw=1.2))
    o.append(_rect(388, 174, 12, 82, fill="url(#h6)", sw=1.2))
    for cx in (286, 394):
        for cy in (196, 222):
            o.append(_circle(cx, cy, 3.5, fill="#ffffff", sw=0.9))
    for x in (281, 389):
        o.append(_line(x, 258, x + 11, 250, sw=0.8, color=GREY))
        o.append(_line(x, 265, x + 11, 257, sw=0.8, color=GREY))

    # Seal C between bonnet and cage top; seal B above the plug.
    o.append(_rect(298, 155, 84, 10, fill="#f2e5cf", sw=1.0, stroke=RED))
    o.append(_rect(308, 176, 64, 8, fill="#dbeaf5", sw=1.0, stroke=BLUE))

    # Double-stage plug (A) and its seat tip.
    o.append(_poly([(320, 184), (360, 184), (360, 206), (352, 206),
                    (352, 228), (360, 228), (360, 255), (320, 255),
                    (320, 228), (328, 228), (328, 206), (320, 206)],
                   fill="#e9dcc5", sw=1.3, close=True))
    o.append(_poly([(328, 255), (352, 255), (340, 270)],
                   fill="#e9dcc5", sw=1.2, close=True))

    # Stem and staked connection (E).
    o.append(_rect(334, 80, 12, 105, fill="#fbfaf7", sw=1.3))
    o.append(_circle(340, 182, 3, fill=INK, sw=0.8))
    o.append(_line(334, 178, 346, 186, sw=0.9, color=INK))

    # Flow from inlet to outlet.
    o.append(_arrow(105, 240, 200, 240, sw=1.8, color=BLUE))
    o.append(T(152, 232, "Dòng chảy / Flow", 8.0, color=BLUE))

    def lbl(ax, ay, tx, ty, text, color=INK, anchor="end", size=8.0):
        o.append(_line(ax, ay, tx, ty, sw=0.9, color=GREY))
        o.append(T(tx + (-4 if anchor == "end" else 4), ty + 2.5, text,
                   size, anchor=anchor, color=color))

    lbl(360, 220, 470, 220, "A · Nút van / Plug", color=RED, anchor="start")
    lbl(312, 180, 215, 112, "B · Phớt trên mềm / Flexible top seal", color=BLUE)
    lbl(330, 160, 215, 87, "C · Phớt nén / Compressible top seal", color=RED)
    lbl(286, 262, 250, 337, "D · Lồng vặn vào thân / Cage screwed into housing")
    lbl(340, 182, 470, 112, "E · Nút nối đóng ghim / Staked stem joint",
        anchor="start")
    lbl(394, 205, 466, 158, "Lồng / Cage", anchor="start")

    # Bilingual strip inside the SVG (present on both language pages).
    o.append(T(340, 370, "Hình 31-1 · Cụm thân van điều khiển kiểu lồng hiện đại.",
               7.0, color=INK))
    o.append(T(340, 386, "Figure 31-1 · A modern cage-type control valve body subassembly.",
               7.0, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt cụm thân van điều khiển kiểu lồng với các nhãn A đến E")),
                "Hình 31-1 · Cụm thân van điều khiển kiểu lồng hiện đại. Nút van (A) cho phép "
                "tiết lưu hai cấp nhằm tăng khả năng chống xâm thực và độ phạm vi lưu lượng "
                "cao. Tránh được các vòng làm kín trượt gây ma sát nhờ dùng phớt trên mềm (B), "
                "cho phép cân bằng lực, dung sai gia công và giãn nở nhiệt. Nắp van được làm "
                "kín với lồng bằng phớt trên có khả năng nén (C). Lồng được vặn vào thân van "
                "(D), loại bỏ các bulông nặng cần thiết để ép hai gioăng trên các van lồng "
                "thông thường. Cuối cùng, liên kết giữa thân van và nút van được đóng ghim "
                "(E) thay vì dùng chốt có thể bị lỏng.",
                "Figure 31-1 · A modern cage-type control valve body subassembly. The valve "
                "plug (A) allows for double-stage throttling for increased cavitation "
                "resistance and high rangeability. Friction-causing sliding seals are avoided "
                "by using a flexible top seal (B) allowing for balanced forces, machining "
                "tolerances, and thermal expansion. The bonnet is sealed against the cage by a "
                "compressible top seal (C). The cage is screwed into the housing (D) "
                "eliminating the heavy bolting required to compress two gaskets on conventional "
                "cage valves. Finally, the stem connection to the plug is staked (E) instead of "
                "using a pin which may become loose.",
                "Sơ đồ cắt cụm thân van kiểu lồng: mặt bích, nắp van, lồng, nút van hai cấp, "
                "thân van, phớt A đến E và mũi tên dòng chảy",
                "Cutaway of a cage-type control valve body subassembly: flanges, bonnet, cage, "
                "double-stage plug, stem, seals A to E and the flow arrow")
