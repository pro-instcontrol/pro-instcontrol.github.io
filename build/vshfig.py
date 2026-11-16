# -*- coding: utf-8 -*-
"""Vector figures for Book 6 — Smith & Zappe, *Valve Selection Handbook*,
5th ed. (Gulf Professional Publishing / Elsevier, 2004).

Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.  Figures whose number
matches the source (e.g. Figure 2-1, Figure 3-12) are redraws of the
originals; editorial schematics that do not exist in the source are labelled
as such in both captions.  The source book is extremely figure-dense (243
numbered figures — valve cutaways, seat-detail drawings and sizing charts);
each is redrawn as a simplified vector schematic that keeps the topology and
labels of the original.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _axes, _box, _circle, _curve, _defs, _f as fmt,
                  _fig, _line, _path, _poly, _rect, _txt, svg)


def esc(s):
    """XML-escape SVG text, preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


# ============================================================ ch01 (editorial)
def fig_vsh_intro():
    """Editorial schematic: valve families grouped by duty (source ch. 1)."""
    w, h = 560, 300
    o = [_defs()]

    # Manual valves group
    o.append(_box(14, 14, 258, 118, "", fill="#eef3fb"))
    o.append(_txt(143, 32, "MANUAL VALVES · van điều khiển tay", 9,
                  weight="bold", color=BLUE))
    o.append(_txt(143, 44, "stop/start · throttle · divert", 7.2, color=GREY))
    fams = ["globe", "gate", "plug", "ball", "butterfly", "pinch", "diaphragm"]
    for i, name in enumerate(fams):
        x = 24 + (i % 4) * 62
        y = 56 + (i // 4) * 34
        o.append(_box(x, y, 56, 24, name, fill="#fff", size=7.6))
    # closure-member movement glyph: vertical slide, rotate 90°, flexible
    o.append(_line(30, 122, 30, 128, 1.2))
    o.append(_txt(52, 126, "linear / slide / rotary / flex-body", 6.6,
                  anchor="start", color=GREY))

    # Check valves group
    o.append(_box(296, 14, 250, 118, "", fill="#eaf3ec"))
    o.append(_txt(421, 32, "CHECK VALVES · VAN một chiều", 9,
                  weight="bold", color=GREEN))
    o.append(_txt(421, 44, "prevent backflow · fast closing", 7.2, color=GREY))
    for i, name in enumerate(["lift", "swing", "tilting-disc", "diaphragm"]):
        x = 316 + (i % 2) * 118
        y = 54 + (i // 2) * 30
        o.append(_box(x, y, 108, 22, name, fill="#fff", size=7.6))
    o.append(_arrow(340, 118, 382, 118, 1.2, color=GREEN))
    o.append(_line(402, 118, 440, 118, 1.2, dash="4 3", color=GREEN))
    o.append(_txt(450, 121, "flow", 6.8, anchor="start", color=GREY))

    # Pressure relief valves group
    o.append(_box(14, 148, 258, 96, "", fill="#fbeeea"))
    o.append(_txt(143, 166, "PRESSURE RELIEF VALVES · VAN an toàn áp suất", 8.6,
                  weight="bold", color=RED))
    o.append(_txt(143, 178, "reclosing · relieving pressure", 7.2, color=GREY))
    for i, name in enumerate(["direct-loaded", "pilot-operated",
                              "+ auxiliary actuator", "powered (code duty)"]):
        x = 24 + (i % 2) * 122
        y = 188 + (i // 2) * 26
        o.append(_box(x, y, 114, 20, name, fill="#fff", size=7.2))
    o.append(_arrow(30, 236, 70, 236, 1.1, color=RED))
    o.append(_txt(80, 239, "system pressure acts on the closure member", 6.4,
                  anchor="start", color=GREY))

    # Rupture discs group
    o.append(_box(296, 148, 250, 96, "", fill="#faf5e6"))
    o.append(_txt(421, 166, "RUPTURE DISCS · ĐĨA nứt vỡ", 8.6,
                  weight="bold", color=GOLD))
    o.append(_txt(421, 178, "non-reclosing · single shot", 7.2, color=GREY))
    # forward-domed glyph (arc bulges up, fails in tension), label centred below
    o.append(_path("M326 212 A24 24 0 0 1 374 212", sw=1.4, color=INK))
    o.append(_txt(350, 224, "forward-domed", 7.0))
    o.append(_txt(350, 232, "fails in tension", 6.4, color=GREY))
    # reverse-buckling glyph (dashed arc, fails in compression)
    o.append(_path("M446 212 A24 24 0 0 1 494 212", sw=1.4, color=INK,
                   dash="4 3"))
    o.append(_txt(470, 224, "reverse-buckling", 7.0))
    o.append(_txt(470, 232, "fails in compression", 6.4, color=GREY))
    o.append(_txt(421, 241, "also: violent excursions · vent panels", 6.6,
                  color=GREY))

    # Bottom connector: selection criteria
    o.append(_line(14, 256, 546, 256, 1.0, dash="2 3", color=GREY))
    o.append(_txt(280, 272, "selection = function · material · pressure/temperature · "
                            "plant life · ends · operation · weight", 7.4))
    o.append(_txt(280, 286, "availability · maintenance · cost (last — a valve that "
                            "fails the design criteria is too expensive)", 7.0,
                  color=GREY))

    return _fig(svg(w, h, "".join(o), "Valve families and duties"),
                "Hình E1 · Sơ đồ biên tập: bốn họ van và thiết bị giải áp, nhóm "
                "theo nhiệm vụ (dừng/khống chế/phân luồng dòng, chặn dòng ngược, "
                "giải áp tái đóng, giải áp một lần) cùng tiêu chí lựa chọn ở "
                "chương 1.",
                "Figure E1 · Editorial schematic: the four valve and pressure-"
                "relief families grouped by duty (stop/start, throttle, divert; "
                "prevent backflow; reclosing relief; non-reclosing relief) with "
                "the selection criteria of chapter 1.",
                "Bốn nhóm van: van tay, van một chiều, van an toàn áp suất và "
                "đĩa nứt vỡ, cùng tiêu chí lựa chọn.",
                "Four valve groups: manual valves, check valves, pressure relief "
                "valves and rupture discs, with selection criteria.")


FIGS.update({
    "fig_vsh_intro": fig_vsh_intro,
})
