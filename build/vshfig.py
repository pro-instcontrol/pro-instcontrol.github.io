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


# ============================================================ ch03 (Figure 2-3)
def fig_vsh_2_3():
    """Figure 2-3 — Fluid pressure distribution along a stuffing box packed
    with four rings (Denny & Turnbull)."""
    w, h = 560, 296
    o = [_defs()]
    x0, y0, W, H = 70, 24, 430, 200

    # axes: x = position along the stuffing box (4 packing rings, gland right)
    o.append(_rect(x0, y0, W, H, fill="none", sw=1.2))
    for v in range(5):
        o.append(_line(x0 + v * W / 4.0, y0, x0 + v * W / 4.0, y0 + H, 0.6,
                       color="#d8d4c8"))
        o.append(_txt(x0 + v * W / 4.0, y0 + H + 12,
                      ["1", "2", "3", "4", "gland"][v], 7.0, color=GREY))
    for v in range(6):
        ly = y0 + H - v * H / 5.0
        o.append(_line(x0, ly, x0 + W, ly, 0.6, color="#d8d4c8"))
        o.append(_txt(x0 - 6, ly + 2.4, "%.1f" % (v * 0.2), 6.8,
                      anchor="end", color=GREY))
    o.append(_txt(x0 + W, y0 - 10, "vị trí dọc hộp gioăng (số vòng packing) / "
                                   "position along the stuffing box", 7.0,
                  anchor="end", color=GREY))
    o.append(_txt(x0 - 8, y0 - 10, "Pf = P\u0302f/P\u0302f", 7.4,
                  anchor="start", color=GREY))

    # low fluid pressure: near-uniform gradient (26.2 .. 250 lb/in2)
    def uniform(pdrop):
        pts = []
        for i in range(41):
            fx = i / 40.0
            pts.append((x0 + fx * W, y0 + H - (1.0 - fx * pdrop) * H))
        return _poly(pts, sw=1.2, color=BLUE)

    o.append(uniform(0.30))    # 26.2 lb/in2
    o.append(uniform(0.45))    # 75
    o.append(uniform(0.60))    # 250

    # high fluid pressure: flat, then steep drop across ring below the gland
    def autoseal(fstart, drop):
        pts = []
        for i in range(41):
            fx = i / 40.0
            if fx < fstart:
                val = 1.0 - fx * 0.10
            else:
                k = (fx - fstart) / (1.0 - fstart)
                val = (1.0 - fstart * 0.10) - k * drop
            pts.append((x0 + fx * W, y0 + H - val * H))
        return _poly(pts, sw=1.4, color=RED)

    o.append(autoseal(0.72, 0.30))   # 400 lb/in2
    o.append(autoseal(0.62, 0.45))   # 700
    o.append(autoseal(0.55, 0.55))   # 1000

    # legend (below the plot, clear of the curves)
    o.append(_line(x0 + 4, y0 + H + 27, x0 + 30, y0 + H + 27, 1.6, color=BLUE))
    o.append(_txt(x0 + 36, y0 + H + 30,
                  "áp suất thấp (26–250 lb/in²): gradient gần đều / low "
                  "pressure: near-uniform gradient", 6.8, anchor="start",
                  color=GREY))
    o.append(_line(x0 + 4, y0 + H + 41, x0 + 30, y0 + H + 41, 1.6, color=RED))
    o.append(_txt(x0 + 36, y0 + H + 44,
                  "áp suất cao (400–1000 lb/in²): 90% sụt áp qua vòng dưới "
                  "gland / 90% of the drop across the ring below the gland",
                  6.8, anchor="start", color=GREY))

    return _fig(svg(w, h, "".join(o),
                    "Fluid pressure gradient along a packed stuffing box"),
                "Hình 2-3 · Phân bố áp suất chất lỏng cho bốn vòng packing "
                "bông cotton thấm PTFE (Denny & Turnbull, Proc. Instn Mech "
                "Engrs 174 No. 6, 1960) — vẽ lại dạng sơ đồ: ở áp suất thấp "
                "gradient gần đều; ở áp suất cao ~90% sụt áp tập trung qua "
                "vòng packing ngay dưới gland. Áp suất gland 250 lb/in²; tốc "
                "độ trục 850 rev/min; áp suất nước 26,2–1000 lb/in².",
                "Figure 2-3 · Distribution of fluid pressure for four rings "
                "of PTFE-impregnated plaited cotton packing (Denny & "
                "Turnbull, Proc. Instn Mech Engrs 174 No. 6, 1960) — redrawn "
                "as a schematic: at low fluid pressure the gradient is "
                "near-uniform; at high pressure ~90% of the drop occurs "
                "across the packing ring just below the gland. Gland "
                "pressure 250 lb/in2; shaft speed 850 rev/min; water "
                "pressure 26.2–1000 lb/in2.",
                "Đường phân bố áp suất dọc hộp gioăng với bốn vòng packing, "
                "tách bạch áp suất thấp và áp suất cao.",
                "Pressure gradient curves along a four-ring stuffing box, "
                "separating low- and high-pressure behaviour.")


FIGS.update({
    "fig_vsh_2_3": fig_vsh_2_3,
})


# ------------------------------------------------- ch04 shared: K1 log chart
def _k1_chart(curves, xlab_note, legends, w=560, h=300):
    """Log-y (1..10^3) vs linear-x (0..1) chart, ESDU style.
    curves: list of (points[(x,k1)], color, dash). legends: list of
    (text, color, dash)."""
    o = [_defs()]
    x0, y0, W, H = 64, 22, 440, 226   # plot box
    LX, LY = (0.0, 1.0), (0.0, 3.0)   # x data 0..1, log10 y 0..3

    def px(x):
        return x0 + (x - LX[0]) / (LX[1] - LX[0]) * W

    def py(k):
        import math
        l = math.log10(max(k, 1.0))
        return y0 + H - (l - LY[0]) / (LY[1] - LY[0]) * H

    # decade grid + minor 2/5 lines
    for d in range(4):
        ly = y0 + H - d * H / 3.0
        o.append(_line(x0, ly, x0 + W, ly, d == 0 and 0.9 or 0.6,
                       color="#d8d4c8"))
        o.append(_txt(x0 - 6, ly + 2.4, "10<sup>%d</sup>" % d, 6.8,
                      anchor="end", color=GREY))
        if d < 3:
            for m in (2, 5):
                import math
                lyy = py(m * 10 ** d)
                o.append(_line(x0, lyy, x0 + W, lyy, 0.5, color="#e7e3d8"))
    for i in range(6):
        lx = x0 + i * W / 5.0
        o.append(_line(lx, y0, lx, y0 + H, i in (0, 5) and 0.9 or 0.6,
                       color="#d8d4c8"))
        o.append(_txt(lx, y0 + H + 11, ["0", "0.2", "0.4", "0.6", "0.8",
                                        "1.0"][i], 6.8, color=GREY))
    o.append(_rect(x0, y0, W, H, fill="none", sw=1.2))
    o.append(_txt(x0, y0 + H + 22, xlab_note, 6.8, anchor="start",
                  color=GREY))
    o.append(_txt(x0 - 40, y0 + 6, "K<sub>1</sub>", 8.0, anchor="start",
                  weight="bold"))

    for pts, color, dash in curves:
        pp = [(px(x), py(k)) for x, k in pts]
        o.append(_poly(pp, sw=1.5, color=color, dash=dash))
    # legend rows
    yy = y0 + H + 34
    for text, color, dash in legends:
        o.append(_line(x0 + 6, yy - 2, x0 + 32, yy - 2, 1.5, color=color,
                       dash=dash))
        o.append(_txt(x0 + 38, yy, text, 6.8, anchor="start", color=GREY))
        yy += 12
    return o


# ============================================================ ch04 (Fig 2-4)
def fig_vsh_2_4():
    curves = [
        ([(0.075, 220), (0.1, 120), (0.15, 45), (0.2, 26), (0.3, 13),
          (0.4, 8), (0.5, 5.5), (0.6, 4), (0.7, 2.9), (0.8, 2.1),
          (0.9, 1.6), (1.0, 1.3)], BLUE, ""),
        ([(0.07, 90), (0.1, 55), (0.15, 25), (0.2, 15), (0.3, 8.5),
          (0.4, 5.5), (0.5, 3.8), (0.6, 2.7), (0.7, 2.0), (0.8, 1.6),
          (0.9, 1.35), (1.0, 1.2)], GREEN, ""),
        ([(0.07, 40), (0.1, 28), (0.15, 15), (0.2, 9.5), (0.3, 6),
          (0.4, 4.2), (0.5, 3.1), (0.6, 2.4), (0.7, 1.9), (0.8, 1.55),
          (0.9, 1.3), (1.0, 1.15)], RED, ""),
    ]
    legends = [
        ("globe kiểu chéo (oblique) / oblique pattern", BLUE, ""),
        ("globe kiểu góc (angle) / angle pattern", GREEN, ""),
        ("globe kiểu thẳng (straight) / straight pattern", RED, ""),
    ]
    o = _k1_chart(curves, "đóng (closed) ← tỉ lệ mở van → mở hoàn toàn "
                  "(fully open)", legends)
    return _fig(svg(560, 300, "".join(o), "Globe valve partial-opening "
                    "resistance correction"),
                "Hình 2-4 · Ảnh hưởng xấp xỉ của việc mở một phần van cầu "
                "(globe) tới hệ số trở lực (ESDU Item No. 69022, Hình 13) — "
                "vẽ lại: K<sub>1</sub> tăng vọt khi mở nhỏ; kiểu chéo cho K"
                "<sub>1</sub> cao nhất, kiểu thẳng thấp nhất; mọi đường hội tụ "
                "về K<sub>1</sub> ≈ 1 khi mở hoàn toàn.",
                "Figure 2-4 · Approximate effect of partial opening of globe "
                "valves on the resistance coefficient (ESDU Item No. 69022, "
                "Figure 13) — redrawn: K<sub>1</sub> rises steeply at small "
                "opening; oblique pattern highest, straight pattern lowest; "
                "all curves converge to K<sub>1</sub> ≈ 1 fully open.",
                "Ba đường K1 theo tỉ lệ mở van cầu: kiểu chéo, kiểu góc, "
                "kiểu thẳng.",
                "Three K1 vs opening curves for globe valves: oblique, "
                "angle and straight patterns.")


# ============================================================ ch04 (Fig 2-5)
def fig_vsh_2_5():
    curves = [
        ([(0.10, 95), (0.15, 30), (0.2, 14), (0.3, 7.5), (0.4, 5.0),
          (0.5, 3.6), (0.6, 2.7), (0.7, 2.1), (0.8, 1.7), (0.9, 1.45),
          (1.0, 1.3)], BLUE, ""),
        ([(0.10, 23), (0.15, 12), (0.2, 8), (0.3, 3.8), (0.4, 2.2),
          (0.5, 1.55), (0.6, 1.3), (0.7, 1.18), (0.8, 1.1), (0.9, 1.06),
          (1.0, 1.04)], RED, ""),
    ]
    legends = [
        ("kiểu đập chắn (weir) / weir type", BLUE, ""),
        ("kiểu thông suốt (straight-through) / straight-through type",
         RED, ""),
    ]
    o = _k1_chart(curves, "đóng (closed) ← tỉ lệ mở van cửa → mở hoàn toàn",
                  legends)
    return _fig(svg(560, 300, "".join(o), "Gate (diaphragm pair) partial-"
                    "opening correction"),
                "Hình 2-5 · Ảnh hưởng xấp xỉ của việc mở một phần van cửa "
                "(gate) tới hệ số trở lực (ESDU Item No. 69022, Hình 14) — "
                "vẽ lại: hai đường cắt nhau gần mức mở 0.17; kiểu thông suốt "
                "sụt K<sub>1</sub> nhanh hơn kiểu đập chắn.",
                "Figure 2-5 · Approximate effect of partial opening of gate "
                "valves on the resistance coefficient (ESDU Item No. 69022, "
                "Figure 14) — redrawn: the two curves cross near 0.17 "
                "opening; the straight-through type sheds K<sub>1</sub> "
                "faster than the weir type.",
                "Hai đường K1 theo tỉ lệ mở van cửa: kiểu đập chắn và kiểu "
                "thông suốt.",
                "Two K1 vs opening curves for gate valves: weir type and "
                "straight-through type.")


# ============================================================ ch04 (Fig 2-6)
def fig_vsh_2_6():
    curves = [
        ([(0.15, 1000), (0.2, 210), (0.3, 55), (0.4, 22), (0.5, 10.5),
          (0.6, 6), (0.7, 3.6), (0.8, 2.4), (0.9, 1.7), (1.0, 1.3)],
         BLUE, ""),
    ]
    o = _k1_chart(curves, "đóng (closed) ← tỉ lệ mở van màng → mở hoàn "
                  "toàn", [])
    return _fig(svg(560, 300, "".join(o), "Diaphragm valve partial-opening "
                    "correction"),
                "Hình 2-6 · Ảnh hưởng xấp xỉ của việc mở một phần van màng "
                "(diaphragm) tới hệ số trở lực (ESDU Item No. 69022, Hình "
                "15) — vẽ lại: K<sub>1</sub> gần 10³ ở mức mở 0.15 và giảm "
                "gần log-tuyến tính tới ≈1.3 khi mở hoàn toàn.",
                "Figure 2-6 · Approximate effect of partial opening of "
                "diaphragm valves on the resistance coefficient (ESDU Item "
                "No. 69022, Figure 15) — redrawn: K<sub>1</sub> approaches "
                "10³ at 0.15 opening and falls near-log-linearly to ≈1.3 "
                "fully open.",
                "Một đường K1 theo tỉ lệ mở van màng.",
                "A single K1 vs opening curve for diaphragm valves.")


# ============================================================ ch04 (Fig 2-7)
def fig_vsh_2_7():
    curves = [
        ([(0.20, 1000), (0.25, 350), (0.3, 150), (0.35, 80), (0.4, 45),
          (0.5, 20), (0.6, 10), (0.7, 5.5), (0.8, 3.2), (0.9, 2.0),
          (1.0, 1.3)], BLUE, ""),
        ([(0.30, 1000), (0.4, 300), (0.5, 110), (0.6, 45), (0.7, 18),
          (0.8, 7.5), (0.9, 3.2), (1.0, 1.2)], RED, ""),
    ]
    legends = [
        ("đĩa thấu kính (lenticular disc)", BLUE, ""),
        ("tấm phẳng (flat plate)", RED, ""),
    ]
    o = _k1_chart(curves, "đóng (closed) ← tỉ lệ mở van bướm → mở hoàn toàn",
                  legends)
    return _fig(svg(560, 300, "".join(o), "Butterfly valve partial-opening "
                    "correction"),
                "Hình 2-7 · Ảnh hưởng xấp xỉ của việc mở một phần van bướm "
                "tới hệ số trở lực (ESDU Item No. 69022, Hình 12) — vẽ lại: "
                "đĩa thấu kính mở muộn hơn tấm phẳng; ở mức mở 0.5, K"
                "<sub>1</sub> khoảng 20 (thấu kính) so với ~110 (tấm phẳng).",
                "Figure 2-7 · Approximate effect of partial opening of "
                "butterfly valves on the resistance coefficient (ESDU Item "
                "No. 69022, Figure 12) — redrawn: the lenticular disc opens "
                "earlier than the flat plate; at 0.5 opening K<sub>1</sub> "
                "is about 20 (lenticular) versus ~110 (flat plate).",
                "Hai đường K1 theo tỉ lệ mở van bướm: đĩa thấu kính và tấm "
                "phẳng.",
                "Two K1 vs opening curves for butterfly valves: lenticular "
                "disc and flat plate.")


FIGS.update({
    "fig_vsh_2_4": fig_vsh_2_4,
    "fig_vsh_2_5": fig_vsh_2_5,
    "fig_vsh_2_6": fig_vsh_2_6,
    "fig_vsh_2_7": fig_vsh_2_7,
})


# ============================================================ ch04 (Fig 2-8)
def fig_vsh_2_8():
    """K vs D/d for fully open gate valves with converging-diverging flow
    passage (BWK Arbeitsblatt 42, Haferkamp & Kreuz)."""
    w, h = 560, 300
    o = [_defs()]
    x0, y0, W, H = 64, 22, 400, 226
    YMAX = math.log10(7.0)

    def px(v):
        return x0 + (v - 0.9) / 1.1 * W

    def py(k):
        return y0 + H - (math.log10(max(k, 0.1)) + 1.0) / (YMAX + 1.0) * H

    # log grid: decades 0.1, 1 and intermediate 0.2..0.9, 2..7
    for k, major in [(0.1, 1), (0.2, 0), (0.3, 0), (0.4, 0), (0.5, 0),
                     (0.6, 0), (0.7, 0), (0.8, 0), (0.9, 0), (1, 1),
                     (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]:
        o.append(_line(x0, py(k), x0 + W, py(k), 0.9 if major else 0.5,
                       color="#c9c4b8" if major else "#e7e3d8"))
        if major or k in (0.2, 0.3, 0.4, 0.5, 2, 3, 4, 5, 6, 7):
            lab = ("%g" % k).replace(".", "\u00b7")
            o.append(_txt(x0 - 6, py(k) + 2.4, lab, 6.6, anchor="end",
                          color=GREY))
    for i in range(12):
        v = 0.9 + i * 0.1
        o.append(_line(px(v), y0, px(v), y0 + H, 0.5 if i % 5 else 0.9,
                       color="#e7e3d8" if i % 5 else "#c9c4b8"))
        if i % 3 == 0:
            lab = ("%g" % v).replace(".", "\u00b7")
            o.append(_txt(px(v), y0 + H + 11, lab, 6.6, color=GREY))
    o.append(_rect(x0, y0, W, H, fill="none", sw=1.2))
    o.append(_txt(x0 + W + 6, y0 + H + 11, "D/d", 7.6, anchor="start",
                  color=GREY))
    o.append(_txt(x0 - 44, y0 + 6, "K", 8.4, anchor="start", weight="bold"))

    def curve(pts, dash="", color=INK):
        pp = [(px(a), py(b)) for a, b in pts]
        return _poly(pp, sw=1.5, color=color, dash=dash)

    o.append(curve([(1.0, 0.1), (1.1, 0.55), (1.2, 1.35), (1.3, 2.1),
                    (1.4, 3.0), (1.5, 4.4), (1.6, 6.2), (1.65, 7.0)]))
    o.append(curve([(1.0, 0.1), (1.2, 0.45), (1.4, 1.0), (1.5, 1.5),
                    (1.6, 2.2), (1.7, 3.1), (1.8, 4.1), (1.9, 5.1),
                    (2.0, 6.2)], dash="6 4", color=BLUE))
    o.append(curve([(1.0, 0.1), (1.3, 0.55), (1.5, 1.2), (1.7, 2.2),
                    (1.8, 2.8), (1.9, 3.3), (2.0, 3.8)], dash="6 4",
                   color=GREEN))
    o.append(curve([(1.0, 0.1), (1.3, 0.4), (1.5, 0.85), (1.7, 1.5),
                    (1.8, 1.9), (1.9, 2.25), (2.0, 2.6)], dash="6 4",
                   color=RED))
    # curve labels
    o.append(_txt(px(1.22) + 6, py(1.8), "d (L = 0)", 7.0, anchor="start"))
    o.append(_txt(px(1.62) + 6, py(2.6), "\u03b1/2 = 30\u00b0", 7.0,
                  anchor="start", color=BLUE))
    o.append(_txt(px(1.85) + 6, py(3.0), "12\u00b0", 7.0, anchor="start",
                  color=GREEN))
    o.append(_txt(px(1.95) + 6, py(2.15), "4\u00b0", 7.0, anchor="start",
                  color=RED))
    o.append(_txt(x0 + W + 6, y0 + 24,
                  "\u03b1/2: g\u00f3c loe / taper angle", 6.6, anchor="start",
                  color=GREY))
    o.append(_txt(x0 + W + 6, y0 + 34, "d: L\u00e0 m\u1ed9t c\u1ee7a van",
                  6.6, anchor="start", color=GREY))
    o.append(_txt(x0 + W + 6, y0 + 44, "D: \u0110\u01b0\u1eddng d\u1eabn", 6.6,
                  anchor="start", color=GREY))

    return _fig(svg(w, h, "".join(o), "Gate valve venturi passage resistance"),
                "H\u00ecnh 2-8 \u00b7 H\u1ec7 s\u1ed1 tr\u1edf l\u1ef1c c\u1ee7a "
                "van c\u1eeda m\u1edf ho\u00e0n to\u00e0n c\u00f3 \u0111\u01b0\u1eddng "
                "d\u00f2ng co h\u1eb9p \u2013 ph\u00ecnh r\u1ed9ng v\u00e0 mi\u1ebfng "
                "m\u1eaft (eye piece) gi\u1eefa hai seat (BWK Arbeitsblatt 42, "
                "Haferkamp & Kreuz) \u2014 v\u1ebd l\u1ea1i: \u0111\u01b0\u1eddng d "
                "(L = 0, t\u00e1c d\u1ee5ng th\u1ee5t Borda-Carnot t\u1ed1i "
                "\u0111a) cao nh\u1ea5t; c\u00e1c \u0111\u01b0\u1eddng a\u2013c "
                "(L \u2265 12D) cho g\u00f3c loe 30\u00b0, 12\u00b0, 4\u00b0 \u2014 "
                "g\u00f3c nh\u1ecf h\u01a1n th\u00ec K th\u1ea5p h\u01a1n.",
                "Figure 2-8 \u00b7 Resistance coefficient of fully open gate "
                "valves with converging-diverging flow passage and eye piece "
                "between the seats (BWK Arbeitsblatt 42, Haferkamp & Kreuz) "
                "\u2014 redrawn: curve d (L = 0, the Borda-Carnot maximum) is "
                "highest; curves a\u2013c (L \u2265 12D) apply to taper "
                "half-angles 30\u00b0, 12\u00b0, 4\u00b0 \u2014 smaller taper "
                "angle, lower K.",
                "B\u1ed1n \u0111\u01b0\u1eddng K theo t\u1ef7 l\u1ec7 D/d "
                "cho van c\u1eeda venturi.",
                "Four K vs D/d curves for venturi-type gate valves.")


# ============================================================ ch04 (Fig 2-9)
def fig_vsh_2_9():
    w, h = 560, 280
    o = [_defs()]
    x0, y0, W, H = 60, 24, 240, 220

    def px(v):
        return x0 + v * W

    def py(v):
        return y0 + H - v * H

    o.append(_rect(x0, y0, W, H, fill="none", sw=1.3))
    o.append(_arrow(x0 - 14, y0 + H, x0 - 14, y0 + 4, 1.0))
    o.append(_arrow(x0, y0 + H + 14, x0 + W, y0 + H + 14, 1.0))
    o.append(_txt(x0 - 20, y0 + 16, "d\u00f2ng / flow", 7.0, anchor="start",
                  color=GREY))
    o.append(_txt(x0 + W / 2, y0 + H + 30,
                  "v\u1ecb tr\u00ed m\u1edf van / valve opening position",
                  7.2, color=GREY))
    o.append(_txt(x0 - 8, y0 + H + 4, "0", 7.0, anchor="end", color=GREY))
    o.append(_txt(x0 + W + 4, y0 + H + 4, "1", 7.0, anchor="start",
                  color=GREY))
    o.append(_txt(x0 - 8, y0 - 2, "1", 7.0, anchor="end", color=GREY))
    o.append(_txt(x0 - 8, y0 + H + 4, "0", 7.0, anchor="end", color=GREY))

    def curve(pts, color, dash=""):
        return _poly([(px(a), py(b)) for a, b in pts], sw=1.5, color=color,
                     dash=dash)

    o.append(curve([(0, 0), (0.1, 0.35), (0.2, 0.65), (0.3, 0.85),
                    (0.4, 0.93), (0.5, 0.96), (0.6, 0.975), (0.8, 0.99),
                    (1.0, 1.0)], BLUE))
    pts = [(i / 20.0, (i / 20.0) ** 0.5) for i in range(21)]
    o.append(curve(pts, GREEN))
    o.append(curve([(0, 0), (1, 1)], INK))
    o.append(curve([(0, 0), (0.2, 0.05), (0.4, 0.15), (0.6, 0.35),
                    (0.8, 0.65), (1.0, 1.0)], RED))
    o.append(_txt(px(0.22), py(0.52), "1", 8.4, color=BLUE, weight="bold"))
    o.append(_txt(px(0.52), py(0.76), "2", 8.4, color=GREEN, weight="bold"))
    o.append(_txt(px(0.52), py(0.42), "3", 8.4, weight="bold"))
    o.append(_txt(px(0.62), py(0.18), "4", 8.4, color=RED, weight="bold"))
    # legend
    lx = x0 + W + 40
    ly = y0 + 16
    entries = [("1  quick opening \u00b7 m\u1edf nhanh", BLUE),
               ("2  square root \u00b7 c\u0103n b\u1eadc hai", GREEN),
               ("3  linear \u00b7 tuy\u1ebfn t\u00ednh", INK),
               ("4  equal percentage \u00b7 ph\u0103n tr\u0103m b\u1eb1ng nhau",
                RED)]
    for text, color in entries:
        o.append(_txt(lx, ly, text, 7.4, anchor="start", color=color))
        ly += 18
    o.append(_txt(lx, ly + 8,
                  "\u0111\u1ed3 th\u1ecb theo \u0111i\u1ec3m % (h\u1eb3n "
                  "h\u1ee5c) / inherent", 6.6, anchor="start", color=GREY))

    return _fig(svg(w, h, "".join(o), "Inherent flow characteristics"),
                "H\u00ecnh 2-9 \u00b7 \u0110\u1eb7c t\u00ednh d\u00f2ng "
                "t\u1ef1 nhi\u00ean c\u1ee7a van (flow t\u1ea1i m\u1ecdi v\u1ecb "
                "tr\u00ed m\u1edf, \u00e1p \u0111\u1ea7u v\u00e0o kh\u00f4ng "
                "\u0111\u1ed5i) \u2014 v\u1ebd l\u1ea1i: m\u1edf nhanh (1), "
                "c\u0103n b\u1eadc hai (2), tuy\u1ebfn t\u00ednh (3), ph\u0103n "
                "tr\u0103m b\u1eb1ng nhau (4).",
                "Figure 2-9 \u00b7 Inherent flow characteristics of valves "
                "(flow at all opening positions at constant inlet pressure) "
                "\u2014 redrawn: quick opening (1), square root (2), linear "
                "(3), equal percentage (4).",
                "B\u1ed1n \u0111\u01b0\u1eddng \u0111\u1eb7c t\u00ednh d\u00f2ng "
                "t\u1ef1 nhi\u00ean c\u1ee7a van.",
                "Four inherent flow characteristic curves.")


# ============================================================ ch04 (Fig 2-10)
def fig_vsh_2_10():
    w, h = 560, 460
    o = [_defs()]
    x0, W = 70, 330

    # ---- upper panel: pressure vs flow
    y0u, Hu = 30, 180

    def pxu(f):
        return x0 + f * W

    def pyu(p):          # p in 0..1 (0 = zero pressure line)
        return y0u + Hu - p * Hu

    o.append(_rect(x0, y0u, W, Hu, fill="none", sw=1.2))
    o.append(_arrow(x0 - 14, y0u + Hu, x0 - 14, y0u + 4, 1.0))
    o.append(_txt(x0 - 20, y0u + 14, "\u00e1p su\u1ea5t / pressure", 7.0,
                  anchor="start", color=GREY))
    o.append(_txt(x0, y0u + Hu + 4, "0", 7.0, anchor="end", color=GREY))
    # pump pressure curve: declines from top-left
    o.append(_poly([(pxu(f), pyu(1.0 - 0.42 * f * f)) for f in
                    [i / 20.0 for i in range(21)]], sw=1.5, color=BLUE))
    # pipeline loss curve: rises from base
    o.append(_poly([(pxu(f), pyu(0.12 + 0.35 * f * f)) for f in
                    [i / 20.0 for i in range(21)]], sw=1.5, color=RED))
    o.append(_txt(x0 + 60, y0u + 22, "\u00e1p b\u01a1m / pump pressure", 7.0,
                  anchor="start", color=BLUE))
    o.append(_txt(x0 + 40, y0u + Hu - 30,
                  "t\u1ed5n th\u1ea5t \u0111\u01b0\u1eddng \u1ed1ng / "
                  "pipeline loss", 7.0, anchor="start", color=RED))
    # right-side brackets
    bx = x0 + W
    for (pa, pb, lab, col) in [
            (0.86, 1.0, "t\u1ed5n \u00e1p b\u01a1m / loss of pumping "
             "pressure", GREY),
            (0.62, 0.86, "t\u1ed5n th\u1ea5t qua van / pressure loss in "
             "valve", GREY),
            (0.44, 0.62, "t\u1ed5n th\u1ea5t \u0111\u01b0\u1eddng \u1ed1ng / "
             "pressure loss in pipeline", GREY),
            (0.12, 0.44, "\u00e1p ng\u01b0\u1ee3c / back pressure", GREY)]:
        o.append(_line(bx + 4, pyu(pa), bx + 4, pyu(pb), 0.8, color=col))
        o.append(_line(bx + 4, pyu(pa), bx + 10, pyu(pa), 0.8, color=col))
        o.append(_line(bx + 4, pyu(pb), bx + 10, pyu(pb), 0.8, color=col))
        o.append(_txt(bx + 14, (pyu(pa) + pyu(pb)) / 2 + 2, lab, 6.8,
                      anchor="start", color=GREY))
    # design flow dashed line through both panels
    xd = pxu(0.42)
    o.append(_line(xd, y0u, xd, y0u + Hu, 0.9, dash="5 4", color=GREY))

    # ---- lower panel: valve opening position vs flow (y inverted)
    y0l = y0u + Hu + 56
    Hl = 170

    def pyl(op):
        return y0l + Hl - op * Hl

    o.append(_rect(x0, y0l, W, Hl, fill="none", sw=1.2))
    o.append(_arrow(x0 - 14, y0l + Hl, x0 - 14, y0l + 4, 1.0))
    o.append(_txt(x0 - 20, y0l + 14,
                  "v\u1ecb tr\u00ed m\u1edf van / valve opening", 7.0,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W / 2, y0l + Hl + 26,
                  "l\u01b0u l\u01b0\u1ee3ng / flow rate", 7.2, color=GREY))
    o.append(_txt(x0, y0l + Hl + 4, "0", 7.0, anchor="end", color=GREY))
    o.append(_txt(x0 + W + 4, y0l + Hl + 4, "1", 7.0, anchor="start",
                  color=GREY))
    # installed flow characteristic: rises slowly then steeply
    o.append(_poly([(pxu(f), pyl(0.02 + 0.98 * f * f * f)) for f in
                    [i / 20.0 for i in range(21)]], sw=1.5, color=GREEN))
    o.append(_txt(pxu(0.60), pyl(0.30) - 8,
                  "\u0111\u1eb7c t\u00ednh d\u00f2ng l\u1eafp \u0111\u1eb7t / "
                  "installed flow characteristic", 6.8, anchor="start",
                  color=GREEN))
    o.append(_line(xd, y0l, xd, y0l + Hl, 0.9, dash="5 4", color=GREY))
    o.append(_arrow(bx - 66, y0l + 34, xd + 2, y0l + 34, 0.8, color=GREY))
    o.append(_txt(bx - 62, y0l + 37,
                  "d\u00f2ng thi\u1ebft k\u1ebf / design flow", 6.8,
                  anchor="start", color=GREY))
    o.append(_line(x0, pyl(0.12), x0 + W, pyl(0.12), 0.7, color=GREY))
    o.append(_txt(x0 + W + 6, pyl(0.12) + 2,
                  "v\u1ecb tr\u00ed m\u1edf / opening position", 6.8,
                  anchor="start", color=GREY))

    return _fig(svg(w, h, "".join(o), "Installed valve flow characteristic "
                    "in a pumping system"),
                "H\u00ecnh 2-10 \u00b7 Quan h\u1ec7 gi\u1eefa l\u01b0u "
                "l\u01b0\u1ee3ng, v\u1ecb tr\u00ed m\u1edf van v\u00e0 "
                "t\u1ed5n th\u1ea5t \u00e1p su\u1ea5t trong h\u1ec7 th\u1ed1ng "
                "b\u01a1m \u2014 v\u1ebd l\u1ea1i: ph\u00eda tr\u00ean l\u00e0 "
                "\u0111\u01b0\u1eddng \u00e1p b\u01a1m v\u00e0 t\u1ed5n "
                "th\u1ea5t \u0111\u01b0\u1eddng \u1ed1ng theo l\u01b0u "
                "l\u01b0\u1ee3ng (ph\u1ea3i: m\u1ea3nh t\u1ed5n \u00e1p b\u01a1m, "
                "t\u1ed5n qua van, t\u1ed5n \u0111\u01b0\u1eddng \u1ed1ng, "
                "\u00e1p ng\u01b0\u1ee3c); ph\u00eda d\u01b0\u1edbi l\u00e0 "
                "\u0111\u1eb7c t\u00ednh d\u00f2ng l\u1eafp \u0111\u1eb7t \u2014 "
                "ri\u00eang cho m\u1ed7i installation.",
                "Figure 2-10 \u00b7 Relationship between flow rate, valve "
                "opening position and pressure loss in a pumping system "
                "\u2014 redrawn: upper panel shows the pump pressure and "
                "pipeline loss curves against flow (right: segments for loss "
                "of pumping pressure, valve loss, pipeline loss, back "
                "pressure); lower panel shows the installed flow "
                "characteristic \u2014 unique for each valve installation.",
                "S\u01a1 \u0111\u1ed3 hai panel: \u00e1p su\u1ea5t\u2013l\u01b0u "
                "l\u01b0\u1ee3ng v\u00e0 v\u1ecb tr\u00ed m\u1edf\u2013l\u01b0u "
                "l\u01b0\u1ee3ng.",
                "Two-panel diagram: pressure\u2013flow and opening\u2013flow "
                "with design-flow marker.")


# ============================================================ ch04 (Fig 2-11)
def _cav_panel(x0, y0, W, H, lower, upper, title):
    o = [_rect(x0, y0, W, H, fill="none", sw=1.0)]
    o.append(_txt(x0 + W / 2, y0 - 6, title, 7.4, weight="bold"))

    def px(v):
        return x0 + v / 100.0 * W

    def py(c):
        return y0 + H - c / 5.0 * H

    for v in (20, 40, 60, 80):
        o.append(_line(px(v), y0, px(v), y0 + H, 0.5, color="#e7e3d8"))
    for c in (1, 2, 3, 4):
        o.append(_line(x0, py(c), x0 + W, py(c), 0.5, color="#e7e3d8"))
        o.append(_txt(x0 - 5, py(c) + 2.4, "%d" % c, 6.4, anchor="end",
                      color=GREY))
    o.append(_txt(x0 - 5, y0 + H + 2, "0", 6.4, anchor="end", color=GREY))
    o.append(_txt(x0 - 5, y0 - 2, "5", 6.4, anchor="end", color=GREY))
    for v in (0, 20, 40, 60, 80, 100):
        o.append(_txt(px(v), y0 + H + 10, "%d" % v, 6.4, color=GREY))
    lo = [(px(a), py(b)) for a, b in lower]
    up = [(px(a), py(b)) for a, b in upper] + lo[::-1]
    o.append(_poly(up, fill="url(#h6)", sw=0))
    o.append(_poly(lo, sw=1.2, color=INK))
    o.append(_poly([(px(a), py(b)) for a, b in upper], sw=1.4, color=INK))
    o.append(_txt(x0 + W / 2, y0 + H + 22,
                  "m\u1edf van (%) / valve opening (%)", 6.6, color=GREY))
    return "".join(o)


def fig_vsh_2_11():
    w, h = 560, 380
    o = [_defs()]
    pw, ph, gap = 246, 128, 30
    o.append(_cav_panel(58, 40, pw, ph,
                        [(15, 1.6), (25, 0.8), (40, 1.0), (60, 1.5),
                         (80, 2.4)],
                        [(15, 1.55), (25, 1.9), (40, 3.3), (55, 3.9),
                         (80, 4.1)],
                        "GLOBE \u00b7 van c\u1ea7u"))
    o.append(_cav_panel(58 + pw + gap, 40, pw, ph,
                        [(20, 2.5), (40, 1.0), (55, 2.0), (75, 4.8)],
                        [(20, 2.55), (40, 2.7), (60, 3.5), (78, 4.85)],
                        "BALL \u00b7 van bi"))
    o.append(_cav_panel(58, 40 + ph + 62, pw, ph,
                        [(15, 1.4), (25, 0.75), (40, 0.85), (60, 1.5),
                         (80, 2.15)],
                        [(15, 1.6), (30, 1.9), (50, 2.4), (70, 3.0),
                         (80, 3.45)],
                        "GATE \u00b7 van c\u1eeda"))
    o.append(_cav_panel(58 + pw + gap, 40 + ph + 62, pw, ph,
                        [(20, 0.9), (50, 1.5), (80, 2.15)],
                        [(20, 2.2), (50, 2.6), (80, 3.45)],
                        "BUTTERFLY \u00b7 van b\u01b0\u1edbm"))
    o.append(_txt(58, 40 + ph + 62 + ph + 40,
                  "C = (Pd \u2212 Pv)/(Pu \u2212 Pd) \u00b7 d\u1ea3i nghi\u1ec7m "
                  "th\u1ee9 theo Sydney Metropolitan Water Sewerage and "
                  "Drainage Board", 6.8, color=GREY))
    return _fig(svg(w, h, "".join(o), "Incipient cavitation characteristics "
                    "of in-line valves"),
                "H\u00ecnh 2-11 \u00b7 \u0110\u1eb7c t\u00ednh x\u00e2m "
                "th\u1ef1c b\u1eaft \u0111\u1ea7u c\u1ee7a c\u00e1c van d\u1ea1ng "
                "n\u1ed1i tuy\u1ebfn (globe, ball, gate, butterfly), m\u00f4i "
                "ch\u1ee9 n\u01b0\u1edbc \u2014 v\u1ebd l\u1ea1i: d\u1ea3i "
                "g\u1ea1ch ch\u00e9o l\u00e0 d\u1ea3i nghi\u1ec7m th\u1ee9; "
                "ch\u1ec9 d\u00f9ng d\u01b0\u1ee3ng h\u01b0\u1edbng d\u1eabn "
                "v\u00ec nhi\u1ec7t \u0111\u1ed9, kh\u00f4ng kh\u00ed l\u1eabn, "
                "t\u1ea1p ch\u1ea5t, dung sai m\u00f4 h\u00ecnh v\u00e0 nh\u1eadn "
                "\u0111\u1ecbnh ng\u01b0\u1eddi quan s\u00e1t \u0111\u1ec1u "
                "\u1ea3nh h\u01b0\u1edfng k\u1ebft qu\u1ea3.",
                "Figure 2-11 \u00b7 Incipient cavitation characteristics of "
                "various \u201cin-line\u201d valves (globe, ball, gate, "
                "butterfly), water medium \u2014 redrawn: hatched areas are "
                "the experimental scatter; the graphs serve only as a guide "
                "since temperature, entrained air, impurities, model "
                "tolerances and observer judgment influence the results.",
                "B\u1ed1n mini-\u0111\u1ed3 C theo m\u1ee9c m\u1edf van cho "
                "b\u1ed1n ki\u1ec3u van.",
                "Four mini-charts of cavitation index C against valve "
                "opening.")


# ============================================================ ch04 (Fig 2-12)
def fig_vsh_2_12():
    w, h = 560, 300
    o = [_defs()]
    x0, y0, W, H = 64, 24, 420, 220

    def px(v):
        return x0 + v * W

    def py(a):
        return y0 + H - a / 1300.0 * H

    for a in (250, 500, 750, 1000, 1250):
        o.append(_line(x0, py(a), x0 + W, py(a), 0.5, color="#e7e3d8"))
        o.append(_txt(x0 - 6, py(a) + 2.4, "%d" % a, 6.6, anchor="end",
                      color=GREY))
    for v in (0.2, 0.4, 0.6, 0.8, 1.0):
        o.append(_line(px(v), y0, px(v), y0 + H, 0.5, color="#e7e3d8"))
        o.append(_txt(px(v), y0 + H + 11, "%g" % v, 6.6, color=GREY))
    o.append(_rect(x0, y0, W, H, fill="none", sw=1.2))
    o.append(_txt(x0 + W / 2, y0 + H + 26,
                  "V<sub>g</sub>/V, % \u00b7 h\u00e0m l\u01b0\u1ee3ng kh\u00f4ng "
                  "kh\u00ed / air content", 7.0, color=GREY))
    o.append(_txt(x0 - 8, y0 - 8, "a (m/s)", 7.6, anchor="start",
                  weight="bold"))
    # theory curve
    o.append(_poly([(px(t), py(a)) for t, a in
                    [(0, 1250), (0.05, 870), (0.1, 640), (0.15, 540),
                     (0.2, 460), (0.3, 390), (0.4, 340), (0.5, 310),
                     (0.6, 280), (0.8, 250), (1.0, 230)]],
                   sw=1.6, color=BLUE))
    # experimental points
    pts = [(0.01, 1310), (0.02, 1290), (0.02, 1220), (0.03, 1200),
           (0.05, 1090), (0.06, 1040), (0.07, 1010), (0.08, 875),
           (0.09, 860), (0.09, 850), (0.10, 870), (0.11, 645),
           (0.12, 585), (0.15, 570), (0.17, 460), (0.18, 455),
           (0.20, 445), (0.21, 420), (0.23, 410), (0.35, 330),
           (0.36, 335), (0.44, 330), (0.45, 320), (0.45, 285),
           (0.55, 255)]
    for t, a in pts:
        o.append(_circle(px(t), py(a), 2.6, sw=1.0, color=INK))
    # legend + notes
    o.append(_circle(x0 + W - 120, y0 + 26, 3.0, sw=1.0, color=INK))
    o.append(_txt(x0 + W - 110, y0 + 29, "nghi\u1ec7m th\u1ee9 / "
                  "experimental", 6.8, anchor="start", color=GREY))
    o.append(_line(x0 + W - 120, y0 + 44, x0 + W - 96, y0 + 44, 1.6,
                   color=BLUE))
    o.append(_txt(x0 + W - 110, y0 + 47, "l\u00fd thuy\u1ebft / theory", 6.8,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W - 120, y0 + 66, "\u00e1p t\u0129nh 47 psi \u00b7 "
                  "324 kPa", 6.8, anchor="start", color=GREY))
    o.append(_line(x0, py(318), x0 + W, py(318), 0.8, dash="4 3",
                   color=RED))
    o.append(_txt(x0 + W - 4, py(318) - 5,
                  "t\u1ed1c \u0111\u1ed9 \u00e2m trong kh\u00f4ng kh\u00ed "
                  "kh\u00f4 20\u00b0C = 318 m/s", 6.6, anchor="end",
                  color=RED))
    return _fig(svg(w, h, "".join(o), "Wave propagation velocity vs air "
                    "content"),
                "H\u00ecnh 2-12 \u00b7 T\u1ed1c \u0111\u1ed9 truy\u1ec1n "
                "\u00e1p s\u00f3ng a trong \u0111\u01b0\u1eddng \u1ed1ng theo "
                "h\u00e0m l\u01b0\u1ee3ng kh\u00f4ng kh\u00ed (Wylie & "
                "Streeter, Fluid Transients) \u2014 v\u1ebd l\u1ea1i: l\u01b0\u1ee3ng "
                "kh\u00f4ng kh\u00ed nh\u1ecf \u0111\u00e3 l\u00e0m t\u1ed1c "
                "\u0111\u1ed9 s\u00f3ng th\u1ea5p h\u01a1n t\u1ed1c \u0111\u1ed9 "
                "\u00e2m trong kh\u00f4ng kh\u00ed (318 m/s, 20\u00b0C, \u00e1p "
                "kh\u00ed quy\u1ec3n).",
                "Figure 2-12 \u00b7 Propagation velocity \u03b1 of a pressure "
                "wave in a pipeline for varying air content (Wylie & "
                "Streeter, Fluid Transients) \u2014 redrawn: a small air "
                "content drives the wave speed below the speed of sound in "
                "air (318 m/s, 20\u00b0C, atmospheric pressure).",
                "\u0110\u01b0\u1eddng l\u00fd thuy\u1ebft v\u00e0 \u0111i\u1ec3m "
                "nghi\u1ec7m th\u1ee9 a theo h\u00e0m l\u01b0\u1ee3ng kh\u00f4ng "
                "kh\u00ed.",
                "Theory curve and experimental points of wave speed against "
                "air content.")


FIGS.update({
    "fig_vsh_2_8": fig_vsh_2_8,
    "fig_vsh_2_9": fig_vsh_2_9,
    "fig_vsh_2_10": fig_vsh_2_10,
    "fig_vsh_2_11": fig_vsh_2_11,
    "fig_vsh_2_12": fig_vsh_2_12,
})
