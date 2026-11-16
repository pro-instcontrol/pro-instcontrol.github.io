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
                  _fig, _hatch, _line, _path, _poly, _rect, _txt, svg)


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


# ============================================================ ch02 (Figure 2-1)
def fig_vsh_2_1():
    """Figure 2-1 — Proposed Zero Gas Leakage Criterion (JPL TR 32-926)."""
    w, h = 560, 280
    o = [_defs()]
    x0, y0, W, H = 74, 20, 440, 212   # plot box: top y0, bottom y0+H
    LX0, LX1 = -1.0, 4.0              # log10 lb/in^2: 0.1 .. 10000
    LY0, LY1 = -10.0, -5.0            # log10 std cm3/s

    def px(lx):
        return x0 + (lx - LX0) / (LX1 - LX0) * W

    def py(ly):
        return y0 + H - (ly - LY0) / (LY1 - LY0) * H

    # grid + ticks
    for i in range(6):
        lx = LX0 + i
        o.append(_line(px(lx), y0, px(lx), y0 + H, 0.6, color="#d8d4c8"))
        o.append(_txt(px(lx), y0 + H + 11,
                      ["0.1", "1.0", "10", "100", "1000", "10000"][i], 6.8,
                      color=GREY))
        o.append(_txt(px(lx), y0 + H + 21,
                      ["6.9×10²", "6.9×10³", "6.9×10⁴", "6.9×10⁵",
                       "6.9×10⁶", "6.9×10⁷"][i], 6.0, color=GREY))
    for i in range(6):
        ly = LY0 + i
        o.append(_line(x0, py(ly), x0 + W, py(ly), 0.6, color="#d8d4c8"))
        o.append(_txt(x0 - 6, py(ly) + 2.4,
                      "10<sup>%d</sup>" % (i - 10), 6.8, anchor="end",
                      color=GREY))
    # frame
    o.append(_rect(x0, y0, W, H, fill="none", sw=1.3))

    # criterion curve: rise (-0.26,-10) -> (1.48,-7), flat -> (2.9,-7),
    # rise -> (4.0,-5.35)  [log-log, mapped via px()/py()]
    def seg(lxa, lya, lxb, lyb):
        pts = []
        for i in range(61):
            lx = lxa + (lxb - lxa) * i / 60.0
            ly = lya + (lyb - lya) * i / 60.0
            pts.append((px(lx), py(ly)))
        return _poly(pts, sw=1.8, color=INK)

    o.append(seg(-0.26, -10.0, 1.48, -7.0))
    o.append(_line(px(1.48), py(-7.0), px(2.9), py(-7.0), 1.8))
    o.append(seg(2.9, -7.0, 4.0, -5.35))

    o.append(_txt(x0 + W + 8, y0 + H + 11, "lb/in²", 7.0, anchor="start",
                  color=GREY))
    o.append(_txt(x0 + W + 8, y0 + H + 21, "Pa", 6.4, anchor="start",
                  color=GREY))
    o.append(_txt(x0 + W / 2, y0 + H + 34,
                  "áp suất chênh lệch qua chỗ kín / differential pressure "
                  "across the seal", 7.2))
    o.append(_txt(x0 - 34, y0 + 8,
                  "rò rỉ khí / gaseous leakage", 7.2, anchor="start"))
    o.append(_txt(x0 - 44, y0 + 18, "std cm³/s", 7.2, anchor="start"))
    o.append(_txt(px(2.2), py(-7.0) - 6,
                  "ngưỡng tiêu chuẩn / specification limit 10<sup>-7</sup>",
                  6.6, color=RED))

    return _fig(svg(w, h, "".join(o),
                    "Zero gas leakage criterion: leakage rises with pressure"),
                "Hình 2-1 · Tiêu chuẩn rò rỉ khí bằng không đề xuất (JPL "
                "Technical Report No. 32-926) — đường tiêu chuẩn cho phép vẽ "
                "lại dạng sơ đồ theo trục log–log: rò rỉ tăng theo áp suất, "
                "chặn tại ngưỡng 10<sup>-7</sup> std cm³/s trên dải trung "
                "gian, rồi tăng lại ở áp suất cao.",
                "Figure 2-1 · Proposed Zero Gas Leakage Criterion (JPL "
                "Technical Report No. 32-926) — redrawn as a log–log "
                "schematic: leakage rises with pressure, is capped at the "
                "10<sup>-7</sup> std cm³/s specification limit across the "
                "mid-range, then rises again at high pressure.",
                "Đường tiêu chuẩn rò rỉ khí bằng không trên biểu đồ log–log "
                "áp suất – tốc độ rò rỉ.",
                "Zero gas leakage criterion curve on a log–log "
                "pressure–leakage chart.")


# ============================================================ ch02 (Figure 2-2)
def fig_vsh_2_2():
    """Figure 2-2 — Effect of Surface Tension on Leakage Flow through
    Capillary."""
    w, h = 560, 260
    o = [_defs()]
    # capillary walls (hatched) with gap = 2r
    o.append(_rect(200, 40, 26, 180, fill="#e9e3d6"))
    o.append(_rect(334, 40, 26, 180, fill="#e9e3d6"))
    o.append(_rect(200, 40, 26, 180, fill="url(#h6)"))
    o.append(_rect(334, 40, 26, 180, fill="url(#h6)"))
    o.append(_line(200, 40, 200, 220, 1.2))
    o.append(_line(226, 40, 226, 220, 1.2))
    o.append(_line(334, 40, 334, 220, 1.2))
    o.append(_line(360, 40, 360, 220, 1.2))
    o.append(_txt(293, 30, "gas · khí", 7.4, color=GREY))

    # liquid below wetting meniscus (θ < 90°): edge higher than centre
    o.append(_path("M226 132 Q293 168 334 132 L334 220 L226 220 Z",
                   fill="#cfe0ef", sw=0))
    o.append(_path("M226 132 Q293 168 334 132", sw=1.5, color=BLUE))
    o.append(_txt(293, 205, "liquid · chất lỏng", 7.4, color=BLUE))

    # radius marker
    o.append(_line(226, 96, 334, 96, 0.8, dash="3 2", color=GREY))
    o.append(_arrow(280, 96, 226, 96, 0.9, color=GREY))
    o.append(_arrow(306, 96, 334, 96, 0.9, color=GREY))
    o.append(_txt(293, 92, "r", 8.0, color=INK))

    # contact angle at the left wall
    o.append(_path("M226 132 L262 128", sw=0.8, color=GREY, dash="2 2"))
    o.append(_txt(238, 126, "θ", 8.0, color=RED))

    # force pair: pressure drive down vs surface tension hold-up
    o.append(_arrow(293, 116, 293, 88, 1.6, color=RED))
    o.append(_txt(300, 76, "πr²·ΔP", 8.2, anchor="start", color=RED,
                  weight="bold"))
    o.append(_arrow(293, 184, 293, 156, 1.6, color=GREEN))
    o.append(_txt(300, 196, "2πrT·cosθ", 8.2, anchor="start", color=GREEN,
                  weight="bold"))
    o.append(_txt(140, 116, "lực đẩy", 7.2, anchor="end", color=RED))
    o.append(_txt(140, 126, "pressure drive", 6.6, anchor="end", color=GREY))
    o.append(_txt(140, 176, "lực căng bề mặt", 7.2, anchor="end", color=GREEN))
    o.append(_txt(140, 186, "surface tension hold-up", 6.6, anchor="end",
                  color=GREY))
    o.append(_txt(140, 156, "cân bằng:", 7.2, anchor="end", weight="bold"))
    o.append(_txt(140, 166, "πr²ΔP = 2πrT·cosθ", 7.4, anchor="end"))

    return _fig(svg(w, h, "".join(o),
                    "Surface tension acting on liquid in a leakage capillary"),
                "Hình 2-2 · Ảnh hưởng của sức căng bề mặt tới dòng rò rỉ qua "
                "mao dẫn (vẽ lại): lực đẩy do chênh áp πr²·ΔP cân bằng với "
                "lực căng bề mặt 2πrT·cosθ dọc đường tiếp xúc; góc tiếp xúc "
                "θ quyết định chất lỏng bị đẩy vào hay bị giữ lại trong mao "
                "dẫn.",
                "Figure 2-2 · Effect of surface tension on leakage flow "
                "through a capillary (redrawn): the pressure drive πr²·ΔP "
                "balances the surface-tension hold-up 2πrT·cosθ along the "
                "contact line; the contact angle θ decides whether the liquid "
                "is drawn into or repelled from the capillary.",
                "Mao dẫn với sức căng bề mặt giữ chất lỏng, góc tiếp xúc θ "
                "và hai lực đối trọng.",
                "Capillary with surface tension holding liquid, contact "
                "angle θ, and the two balancing forces.")


FIGS.update({
    "fig_vsh_2_1": fig_vsh_2_1,
    "fig_vsh_2_2": fig_vsh_2_2,
})
