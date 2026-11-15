# -*- coding: utf-8 -*-
"""Vector figures for Book 4 — Crosby *Pressure Relief Valve Engineering Handbook*.

Chapter 2 (Design Fundamentals) references the source figures F2-2 … F2-9: the
spring-loaded valve force balance, the control / huddling chamber and nozzle ring,
the liquid trim, the soft seat, and the pilot-operated valve.  The source originals
are dense mechanical cutaways; they are redrawn here as clean, labelled schematics
that show the *mechanism* the text describes (spring vs. process-fluid force balance,
the adjustable control chamber, the pilot that vents the piston chamber).  Every
function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import math
import re
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _axes, _box, _circle, _defs, _f as fmt, _fig, _line,
                  _path, _poly, _rect, _txt, svg)


def esc(s):
    """XML-escape SVG text, preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _spring(x, y0, y1, coils=5, w=13):
    pts = [(x, y0)]
    dy = y1 - y0
    for i in range(coils):
        yy = y0 + dy * (i + 0.5) / coils
        xo = x + (-1 if i % 2 == 0 else 1) * w / 2.0
        pts.append((xo, yy))
    pts.append((x, y1))
    return _poly(pts, fill="none", sw=1.3, color=INK)


def _spring_loaded(w, h, open_state=False):
    """Schematic cross-section of a spring-loaded PRV (closed or lifted)."""
    o = [_defs()]
    # --- body / bonnet outline ---
    o.append(_rect(120, 60, 120, 120, fill="#f4f7fb", sw=1.4))
    # inlet nozzle (left) + outlet (right)
    o.append(_poly([(40, 110), (120, 110), (120, 140), (40, 140)], fill="#e9eef6", sw=1.2))
    o.append(_poly([(240, 110), (320, 110), (320, 140), (240, 140)], fill="#e9eef6", sw=1.2))
    # nozzle seat (center) where area A1 acts
    o.append(_rect(196, 120, 8, 30, fill="#cdd7e3", sw=1.1))
    # disc
    dy = 14 if open_state else 0
    o.append(_poly([(180, 118 - dy), (204, 118 - dy), (210, 128 - dy),
                    (174, 128 - dy)], fill=GOLD, sw=1.2))
    # spring
    o.append(_spring(192, 60, 112 - dy, coils=6, w=22))
    # adjust screw
    o.append(_rect(186, 44, 12, 16, fill="#dfe6ef", sw=1.1))
    o.append(_line(192, 44, 192, 60, sw=1.1))
    # process pressure arrows onto area A1
    o.append(_arrow(60, 125, 174, 125, sw=1.4, color=BLUE, head="a7"))
    o.append(_txt(110, 110, "p · A1", 8, color=BLUE))
    # spring force arrow
    o.append(_arrow(192, 100 - dy, 192, 112 - dy, sw=1.4, color=RED, head="a7"))
    o.append(_txt(214, 100 - dy, "F spring", 7.5, color=RED))
    if open_state:
        o.append(_arrow(214, 124 - dy, 250, 124 - dy, sw=1.4, color=GREEN, head="a7"))
        o.append(_txt(232, 138, "flow out", 7, color=GREEN))
    o.append(_txt(192, 188, ("(a) Closed — spring force > p·A1"
                              if not open_state else "(b) Open — p·A1 ≥ F spring, disc lifts"),
               7.4, color=INK))
    return svg(w, h, "".join(o), esc("Spring-loaded pressure relief valve cross-section"))


def _huddling_chamber(w, h):
    o = [_defs()]
    o.append(_rect(120, 50, 140, 130, fill="#f4f7fb", sw=1.4))
    # control / huddling chamber above disc
    o.append(_rect(150, 56, 80, 34, fill="#e7eef8", sw=1.2))
    o.append(_txt(190, 75, "control chamber", 7.5, color=INK))
    # disc + nozzle
    o.append(_poly([(176, 150), (204, 150), (210, 160), (170, 160)], fill=GOLD, sw=1.2))
    o.append(_rect(196, 160, 8, 20, fill="#cdd7e3", sw=1.1))
    # adjustable nozzle ring
    o.append(_rect(150, 150, 80, 10, fill="#d7dee9", sw=1.1))
    o.append(_txt(190, 178, "adjustable nozzle ring", 7, color=GREY))
    # flow path into chamber when lifted
    o.append(_arrow(120, 120, 150, 120, sw=1.3, color=BLUE, head="a7"))
    o.append(_arrow(230, 90, 200, 90, sw=1.3, color=GREEN, head="a7"))
    o.append(_txt(190, 200, "Geometry set by the nozzle ring changes blowdown", 7, color=INK))
    return svg(w, h, "".join(o), esc("Control (huddling) chamber and adjustable nozzle ring"))


def _liquid_trim(w, h):
    o = [_defs()]
    o.append(_rect(120, 60, 120, 120, fill="#f4f7fb", sw=1.4))
    o.append(_rect(196, 120, 8, 30, fill="#cdd7e3", sw=1.1))
    o.append(_poly([(178, 118), (202, 118), (208, 128), (172, 128)], fill=GOLD, sw=1.2))
    # soft seat insert
    o.append(_rect(196, 128, 8, 6, fill=GREEN, sw=1.0))
    o.append(_spring(192, 60, 112, coils=6, w=20))
    o.append(_txt(192, 192, "Soft / metal seat — stable, non-chattering trim", 7.2, color=INK))
    return svg(w, h, "".join(o), esc("Liquid trim (Style JLT) with soft or metal seat"))


def _soft_seat(w, h):
    o = [_defs()]
    # enlarged seating detail
    o.append(_circle(150, 120, 60, fill="#f4f7fb", sw=1.4))
    o.append(_poly([(120, 110), (180, 110), (180, 130), (120, 130)], fill="#dfe6ef", sw=1.1))
    o.append(_rect(146, 128, 8, 12, fill=GOLD, sw=1.1))
    o.append(_rect(146, 138, 8, 5, fill=GREEN, sw=1.0))  # elastomer insert
    o.append(_txt(150, 200, "Optically flat seating + elastomer insert → tight shut-off", 7, color=INK))
    return svg(w, h, "".join(o), esc("Soft seat construction for tight shut-off"))


def _pilot_operated(w, h):
    o = [_defs()]
    # main valve (left)
    o.append(_rect(40, 60, 130, 130, fill="#f4f7fb", sw=1.4))
    o.append(_rect(98, 120, 8, 34, fill="#cdd7e3", sw=1.1))
    o.append(_poly([(80, 116), (104, 116), (110, 126), (74, 126)], fill=GOLD, sw=1.2))
    o.append(_circle(98, 96, 18, fill="#e7eef8", sw=1.2))  # piston
    o.append(_txt(60, 210, "Main valve", 7.4, color=INK))
    # pilot (right)
    o.append(_box(240, 70, 110, 60, "Pilot", fill="#eef3fb"))
    o.append(_txt(295, 200, "Pilot senses set pressure", 7, color=INK))
    # sensing line from inlet to pilot
    o.append(_arrow(60, 150, 200, 150, sw=1.2, color=BLUE, head="a7"))
    o.append(_txt(130, 162, "system pressure", 7, color=BLUE))
    # to piston chamber
    o.append(_arrow(295, 110, 116, 110, sw=1.2, color=BLUE, head="a7"))
    o.append(_txt(205, 100, "pilot vents → disc opens", 7, color=GREEN))
    return svg(w, h, "".join(o), esc("Pilot-operated pressure relief valve: main valve + pilot"))


# ------------------------------------------------------------------ public
def fig_f22_closed():
    s = _spring_loaded(360, 210, open_state=False)
    return _fig(s,
                "Hình F2-2 · Van xả áp lò xo ở trạng thái đóng: lực lò xo lớn hơn p·A1.",
                "Figure F2-2 · Spring-loaded PRV in the closed position: spring force exceeds p·A1.",
                "Sơ đồ van xả áp lò xo trạng thái đóng, lực lò xo lớn hơn áp suất nhân diện tích",
                "Closed spring-loaded relief valve: spring force greater than pressure times area")


def fig_f22_open():
    s = _spring_loaded(360, 210, open_state=True)
    return _fig(s,
                "Hình F2-2b · Khi p·A1 đạt áp lực thiết lập, đĩa nhấc lên và chất lưu xả ra.",
                "Figure F2-2b · When p·A1 reaches set pressure the disc lifts and fluid escapes.",
                "Sơ đồ van xả áp lò xo trạng thái mở, đĩa nhấc lên cho chất lưu thoát ra",
                "Open spring-loaded relief valve with the disc lifted and flow escaping")


def fig_f23():
    s = _huddling_chamber(380, 220)
    return _fig(s,
                "Hình F2-3 · Buồng điều khiển (huddling) và vòng miệng phun điều chỉnh thay đổi blowdown.",
                "Figure F2-3 · The control (huddling) chamber and adjustable nozzle ring set the blowdown.",
                "Sơ đồ buồng điều khiển và vòng miệng phun điều chỉnh tỷ lệ đóng lại",
                "Control chamber and adjustable nozzle ring that sets blowdown")


def fig_f24():
    s = _liquid_trim(360, 210)
    return _fig(s,
                "Hình F2-4 · Cụm trim lưu chất (kiểu JLT) với đệm mềm hoặc kim loại, vận hành không rung.",
                "Figure F2-4 · Liquid trim (Style JLT) with soft or metal seat — stable, non-chattering.",
                "Sơ đồ cụm trim lưu chất kiểu JLT với đệm mềm hoặc kim loại",
                "Liquid trim with soft or metal seat for stable non-chattering performance")


def fig_f26():
    s = _soft_seat(320, 230)
    return _fig(s,
                "Hình F2-6 · Kết cấu đệm mềm: bề mặt tiếp xúc phẳng quang học và lớp đệm đàn hồi kín khít.",
                "Figure F2-6 · Soft-seat construction: optically flat seating and an elastomer insert.",
                "Sơ đồ kết cấu đệm mềm với bề mặt phẳng quang học và lớp đệm đàn hồi",
                "Soft seat with optically flat seating surface and elastomer insert")


def fig_f29():
    s = _pilot_operated(420, 230)
    return _fig(s,
                "Hình F2-9 · Van xả áp vận hành bằng pilot: van chính có piston và pilot điều khiển.",
                "Figure F2-9 · Pilot-operated PRV: a main valve with piston and a sensing pilot.",
                "Sơ đồ van xả áp vận hành bằng pilot gồm van chính có piston và pilot",
                "Pilot-operated relief valve with main valve piston and sensing pilot")


# ------------------------------------------------------------------ plotting
def _mpl(pts, x0, y0, W, H, xr, yr, **kw):
    lo, hi = xr
    a, b = yr

    def px(x):
        return x0 + (x - lo) / (hi - lo) * W

    def py(y):
        return y0 + H - (y - a) / (b - a) * H
    return _poly([(px(x), py(y)) for x, y in pts], **kw)


def _mpl_logx(pts, x0, y0, W, H, xr, yr, **kw):
    lo, hi = math.log10(xr[0]), math.log10(xr[1])
    a, b = yr

    def px(x):
        return x0 + (math.log10(x) - lo) / (hi - lo) * W

    def py(y):
        return y0 + H - (y - a) / (b - a) * H
    return _poly([(px(x), py(y)) for x, y in pts], **kw)


def _chart(w, h, x0, y0, W, H, xlab, ylab):
    """Common frame: defs + axes for a 520x340 chart canvas."""
    return _defs() + _axes(x0, y0, W, H, xlab, ylab)


# ------------------------------------------------------------------ Ch7 figs
def fig_f71():
    """Generalized compressibility factor Z vs reduced pressure Pr (schematic)."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "REDUCED PRESSURE  Pr = P / Pc", "Z")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 10.0, "%g" % (i / 10.0)) for i in range(0, 11, 2)],
                   yt=[(i / 6.0, "%.1f" % (i / 5.0 + 0.0)) for i in range(6)]))
    # schematic curves for several reduced temperatures Tr
    curves = [
        (1.2, "1.2", GOLD), (1.5, "1.5", BLUE), (2.0, "2.0", GREEN), (3.0, "3.0", RED),
    ]

    def z_of(pr, tr):
        return 1.0 - (1.0 - (1.0 / tr)) * math.exp(-((pr - 1.2 * tr) / (1.1 * tr)) ** 2)

    for tr, lab, col in curves:
        pts = [(pr / 10.0, z_of(pr / 10.0, tr)) for pr in range(2, 82)]
        o.append(_mpl(pts, x0, y0, W, H, (0, 8), (0, 1.2),
                      fill="none", sw=1.4, color=col))
        # label at right end
        last = pts[-1]
        o.append(_txt(x0 + (last[0] - 0) / 8.0 * W + 4,
                      y0 + H - (last[1] - 0) / 1.2 * H, "Tr=" + lab, 7, anchor="start", color=col))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Sơ đồ tổng quát hệ số nén Z (Tr = nhiệt độ quy giản)", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Generalized compressibility factor chart Z vs Pr"))
    return _fig(s,
                "Hình F7-1 · Sơ đồ tổng quát hệ số nén Z theo áp suất quy giản Pr cho các nhiệt độ quy giản Tr.",
                "Figure F7-1 · Generalized compressibility factor Z versus reduced pressure Pr for several reduced temperatures Tr.",
                "Đồ thị tổng quát hệ số nén Z theo áp suất quy giản với các đường cong Tr khác nhau",
                "Generalized compressibility chart with Z curves for several reduced temperatures")


def fig_f72():
    """Kb — back-pressure capacity correction for balanced (JBS / Series BP) valves, gas & vapor."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "BACK PRESSURE  Pb / P1  (%)", "Kb")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 10.0, "%d" % (i * 5)) for i in range(0, 11)],
                   yt=[(i / 10.0, "%.2f" % (0.5 + i * 0.05)) for i in range(0, 11)]))
    pts = [(0, 1.00), (5, 0.99), (10, 0.97), (15, 0.95), (20, 0.92), (25, 0.88),
           (30, 0.83), (35, 0.77), (40, 0.69), (45, 0.60), (50, 0.50)]
    o.append(_mpl(pts, x0, y0, W, H, (0, 50), (0.5, 1.0), fill="none", sw=1.6, color=BLUE))
    o.append(_txt(x0 + W - 6, y0 + 16, "JBS / Series BP — gas & vapor", 7.4, anchor="end", color=BLUE))
    # critical-pressure marker (≈55% absolute ratio → ~50% of set for relief)
    o.append(_line(x0 + W, y0, x0 + W, y0 + H, sw=0.8, dash="3 3", color=GREY))
    o.append(_txt(x0 + W - 4, y0 + H - 6, "critical ≈ 55%", 6.6, anchor="end", color=GREY))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Kb giảm dần khi áp suất ngược tăng trên van cân bằng", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Kb back-pressure correction for balanced valves, gas and vapor"))
    return _fig(s,
                "Hình F7-2 · Hệ số hiệu chỉnh áp suất ngược Kb cho van cân bằng (kiểu JBS / Series BP), khí và hơi.",
                "Figure F7-2 · Capacity correction factor Kb for balanced (JBS / Series BP) valves — gas and vapor.",
                "Đồ thị hệ số Kb giảm theo tỷ lệ áp suất ngược cho van cân bằng khí và hơi",
                "Kb versus back-pressure ratio for balanced valves on gas and vapor")


def fig_f73():
    """Kw — back-pressure capacity correction for balanced (JBS / Series BP) valves, liquid."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "BACK PRESSURE  Pb / P1  (%)", "Kw")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 10.0, "%d" % (i * 5)) for i in range(0, 11)],
                   yt=[(i / 10.0, "%.2f" % (0.5 + i * 0.05)) for i in range(0, 11)]))
    pts = [(0, 1.00), (5, 0.99), (10, 0.975), (15, 0.95), (20, 0.92), (25, 0.87),
           (30, 0.80), (35, 0.72), (40, 0.63), (45, 0.54), (50, 0.47)]
    o.append(_mpl(pts, x0, y0, W, H, (0, 50), (0.5, 1.0), fill="none", sw=1.6, color=GREEN))
    o.append(_txt(x0 + W - 6, y0 + 16, "JBS / Series BP — liquid", 7.4, anchor="end", color=GREEN))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Kw giảm dần khi áp suất ngược tăng trên van cân bằng lưu chất", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Kw back-pressure correction for balanced valves, liquid"))
    return _fig(s,
                "Hình F7-3 · Hệ số hiệu chỉnh áp suất ngược Kw cho van cân bằng (kiểu JBS / Series BP), chất lỏng.",
                "Figure F7-3 · Capacity correction factor Kw for balanced (JBS / Series BP) valves — liquid.",
                "Đồ thị hệ số Kw giảm theo tỷ lệ áp suất ngược cho van cân bằng chất lỏng",
                "Kw versus back-pressure ratio for balanced valves on liquid")


def fig_f74():
    """Kn — high-pressure (dry saturated) steam capacity correction factor."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "RELIEVING PRESSURE  P1  (kPaa)", "Kn")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 10.0, "%g" % (10000 + i * 1200)) for i in range(0, 11)],
                   yt=[(i / 10.0, "%.2f" % (0.95 + i * 0.03)) for i in range(0, 11)]))
    # Kn = 1.00 up to 10,346 kPaa, then rises to ~1.22 at 22,060 kPaa
    pts = [(10000, 1.00), (10346, 1.00), (12000, 1.03), (14000, 1.08),
           (16000, 1.13), (18000, 1.17), (20000, 1.20), (22000, 1.22), (22060, 1.22)]
    o.append(_mpl(pts, x0, y0, W, H, (10000, 22060), (0.95, 1.25), fill="none", sw=1.6, color=RED))
    # threshold marker
    tx = x0 + (10346 - 10000) / (22060 - 10000) * W
    o.append(_line(tx, y0, tx, y0 + H, sw=0.8, dash="3 3", color=GREY))
    o.append(_txt(tx + 3, y0 + 12, "10,346 kPaa", 6.6, anchor="start", color=GREY))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Kn = 1,00 dưới 10.346 kPaa, tăng với hơi bão hòa áp suất cao", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Kn high-pressure steam correction factor"))
    return _fig(s,
                "Hình F7-4 · Hệ số hiệu chỉnh Kn cho hơi nước bão hòa khô áp suất cao (trên 10.346 kPaa).",
                "Figure F7-4 · Capacity correction factor Kn for dry saturated steam above 10,346 kPaa.",
                "Đồ thị hệ số Kn tăng theo áp suất xả cho hơi bão hòa khô áp suất cao",
                "Kn versus relieving pressure for high-pressure dry saturated steam")


def fig_f75():
    """Kv — viscosity (flow) correction factor versus Reynolds number, log scale."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "REYNOLDS NUMBER  R", "Kv")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 5.0, "1e%d" % (i + 1)) for i in range(5)],
                   yt=[(i / 7.0, "%.1f" % (0.3 + i * 0.1)) for i in range(0, 8)]))
    pts = [(10, 0.35), (100, 0.62), (1000, 0.85), (10000, 0.97), (100000, 1.00)]
    o.append(_mpl_logx(pts, x0, y0, W, H, (10, 100000), (0.3, 1.0), fill="none", sw=1.6, color=GOLD))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Kv tiến về 1,0 khi số Reynolds tăng (độ nhớt giảm)", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Kv viscosity correction factor versus Reynolds number"))
    return _fig(s,
                "Hình F7-5 · Hệ số hiệu chỉnh độ nhớt Kv theo số Reynolds (trục log).",
                "Figure F7-5 · Flow correction factor Kv versus Reynolds number (log scale).",
                "Đồ thị hệ số Kv theo số Reynolds trên trục logarit",
                "Kv versus Reynolds number on a logarithmic axis")


def fig_f76():
    """k (ratio of specific heats) versus coefficient C — computed from the exact formula."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244

    def cfac(k):
        return 520.0 * math.sqrt(k * (2.0 / (k + 1.0)) ** ((k + 1.0) / (k - 1.0)))

    o = [_chart(w, h, x0, y0, W, H, "RATIO OF SPECIFIC HEATS  k", "C")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 10.0, "%.1f" % (1.0 + i * 0.1)) for i in range(0, 11)],
                   yt=[(i / 9.0, "%d" % (310 + i * 10)) for i in range(0, 10)]))
    pts = [(k / 100.0, cfac(k / 100.0)) for k in range(101, 201)]
    o.append(_mpl(pts, x0, y0, W, H, (1.0, 2.0), (310, 410), fill="none", sw=1.6, color=INK))
    # mark k=1.4 → C≈356
    mx = x0 + (1.4 - 1.0) / 1.0 * W
    my = y0 + H - (cfac(1.4) - 310) / 100.0 * H
    o.append(_circle(mx, my, 3, fill=RED, sw=0.8, color=RED))
    o.append(_txt(mx + 5, my - 4, "k=1.4 → C=356", 7, anchor="start", color=RED))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "C = 520√[ k (2/(k+1))^((k+1)/(k-1)) ]", 7.4, color=INK))
    s = svg(w, h, "".join(o), esc("Coefficient C versus ratio of specific heats k"))
    return _fig(s,
                "Hình F7-6 · Hệ số C theo tỷ số nhiệt dung riêng k (tính từ công thức chính xác).",
                "Figure F7-6 · Coefficient C versus ratio of specific heats k (from the exact formula).",
                "Đồ thị hệ số C theo tỷ số nhiệt dung riêng k",
                "Coefficient C versus ratio of specific heats k")


def fig_f77():
    """Noise intensity L versus pressure ratio PR (from Figure F7-7)."""
    w, h = 520, 340
    x0, y0, W, H = 62, 42, 408, 244
    o = [_chart(w, h, x0, y0, W, H, "PRESSURE RATIO  PR = P1 / Pb(abs)", "L  (dB @ 100 ft)")]
    o.append(_axes(x0, y0, W, H, "", "",
                   xt=[(i / 8.5, "%.1f" % (1.5 + i * 1.0)) for i in range(0, 9)],
                   yt=[(i / 10.0, "%d" % (20 + i * 5)) for i in range(0, 11)]))
    pts = [(1.5, 68), (2, 62), (3, 56), (4, 50), (5, 44), (6, 39), (8, 30), (10, 24)]
    o.append(_mpl(pts, x0, y0, W, H, (1.5, 10), (20, 70), fill="none", sw=1.6, color=BLUE))
    # example point PR=3.8, L=54.5
    ex, ey = 3.8, 54.5
    px = x0 + (ex - 1.5) / 8.5 * W
    py = y0 + H - (ey - 20) / 50.0 * H
    o.append(_circle(px, py, 3.2, fill=RED, sw=0.8, color=RED))
    o.append(_txt(px + 5, py - 4, "Ví dụ: PR=3.8 → L=54.5 dB", 7, anchor="start", color=RED))
    o.append(_txt(x0 + W / 2.0, y0 + H + 30,
                  "Cường độ ồn giảm khi tỷ số áp suất tăng", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Noise intensity L versus pressure ratio PR"))
    return _fig(s,
                "Hình F7-7 · Cường độ ồn L (dB tại 100 ft) theo tỷ số áp suất PR.",
                "Figure F7-7 · Noise intensity L (dB at 100 ft) versus pressure ratio PR.",
                "Đồ thị cường độ ồn L theo tỷ số áp suất PR",
                "Noise intensity L versus pressure ratio PR")


def fig_f712():
    """F7-12 fire-sizing effective-liquid-level logic diagram."""
    w, h = 460, 540
    o = [_defs()]
    # node coordinates
    bx, bw, bh = 150, 170, 34
    # boxes
    o.append(_box(bx, 20, bw, bh, "K1 = H + F", fill="#eef3fb", size=8.5))
    # decision K1 < 25
    o.append(_poly([(bx + bw / 2.0 - 60, 70), (bx + bw / 2.0 + 60, 70),
                    (bx + bw / 2.0, 110), (bx + bw / 2.0 - 60, 70)], fill="#fff", sw=1.2, color=INK))
    o.append(_txt(bx + bw / 2.0, 96, "K1 < 25 ?", 8, color=INK))
    # K = 25 (NO) and K = K1 (YES)
    o.append(_box(bx, 132, bw, bh, "K = 25", fill="#fdf3e6", size=8.5))
    o.append(_box(bx, 178, bw, bh, "K = K1", fill="#fdf3e6", size=8.5))
    # E1 = K - H
    o.append(_box(bx, 234, bw, bh, "E1 = K − H", fill="#eef3fb", size=8.5))
    # decision E1 > 0
    o.append(_poly([(bx + bw / 2.0 - 60, 284), (bx + bw / 2.0 + 60, 284),
                    (bx + bw / 2.0, 324), (bx + bw / 2.0 - 60, 284)], fill="#fff", sw=1.2, color=INK))
    o.append(_txt(bx + bw / 2.0, 310, "E1 > 0 ?", 8, color=INK))
    # E=0 (NO) and E=E1 (YES)
    o.append(_box(bx, 336, bw, bh, "E = 0", fill="#fdf3e6", size=8.5))
    o.append(_box(bx, 382, bw, bh, "E = E1", fill="#fdf3e6", size=8.5))
    # decision spherical
    o.append(_poly([(bx + bw / 2.0 - 60, 432), (bx + bw / 2.0 + 60, 432),
                    (bx + bw / 2.0, 472), (bx + bw / 2.0 - 60, 432)], fill="#fff", sw=1.2, color=INK))
    o.append(_txt(bx + bw / 2.0, 458, "VESSEL SPHERICAL ?", 7.4, color=INK))
    o.append(_box(bx, 484, bw, bh, "Es = E", fill="#eaf6ee", size=8.5))
    o.append(_box(20, 484, bw, bh, "Es = D/2  (E>D/2)", fill="#eaf6ee", size=8))
    o.append(_box(280, 484, bw, bh, "Es = E  (E≤D/2)", fill="#eaf6ee", size=8))
    # arrows (flow)
    cy = lambda y: y + bh / 2.0
    o.append(_arrow(bx + bw / 2.0, 54, bx + bw / 2.0, 70, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 110, bx + bw / 2.0, 132, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 166, bx + bw / 2.0, 178, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 212, bx + bw / 2.0, 234, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 268, bx + bw / 2.0, 284, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 324, bx + bw / 2.0, 336, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 370, bx + bw / 2.0, 382, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 420, bx + bw / 2.0, 432, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 472, bx + bw / 2.0, 484, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 472, 100, 472, sw=1.1, color=INK, head="a6"))
    o.append(_arrow(bx + bw / 2.0, 472, 360, 472, sw=1.1, color=INK, head="a6"))
    # side labels
    o.append(_txt(bx + bw + 8, 96, "NO", 7, anchor="start", color=GREY))
    o.append(_txt(bx - 22, 96, "YES", 7, anchor="end", color=GREY))
    o.append(_txt(bx + bw + 8, 310, "NO", 7, anchor="start", color=GREY))
    o.append(_txt(bx - 22, 310, "YES", 7, anchor="end", color=GREY))
    o.append(_txt(bx + bw + 8, 458, "YES", 7, anchor="start", color=GREY))
    o.append(_txt(bx - 22, 458, "NO", 7, anchor="end", color=GREY))
    o.append(_txt(230, h - 14,
                  "Sơ đồ logic xác định mức chất lỏng hiệu dụng E / Es cho tính toán hỏa hoạn",
                  7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Fire-sizing effective liquid level logic diagram"))
    return _fig(s,
                "Hình F7-12 · Sơ đồ logic xác định mức chất lỏng hiệu dụng E / Es trong tính toán hỏa hoạn.",
                "Figure F7-12 · Logic diagram for the effective liquid level E / Es in fire sizing.",
                "Sơ đồ logic xác định mức chất lỏng hiệu dụng cho hỏa hoạn",
                "Logic diagram for effective liquid level in fire sizing")


def fig_f713():
    """F7-13 vessel/tank selection diagram (sphere, horizontal & vertical cylinders)."""
    w, h = 520, 360
    o = [_defs()]
    # Sphere
    o.append(_circle(95, 150, 60, fill="#f4f7fb", sw=1.4))
    o.append(_line(35, 150, 155, 150, sw=0.8, dash="2 2", color=GREY))
    o.append(_txt(95, 152, "D", 9, color=INK))
    o.append(_txt(95, 232, "Sphere", 8, color=INK))

    # Horizontal cylinder
    hx, hy, hww, hhh = 250, 120, 130, 50
    o.append(_rect(hx, hy, hww, hhh, fill="#f4f7fb", sw=1.4))
    o.append(_line(hx, hy + hhh, hx + hww, hy + hhh, sw=0.8, dash="2 2", color=GREY))  # L base? use H
    o.append(_line(hx, hy + hhh / 2.0, hx + hww, hy + hhh / 2.0, sw=0.8, dash="2 2", color=GREY))  # D
    o.append(_txt(hx + hww / 2.0, hy + hhh / 2.0 + 4, "D", 9, color=INK))
    o.append(_line(hx + 10, hy + hhh + 6, hx + hww - 10, hy + hhh + 6, sw=0.8, color=GREY))  # L
    o.append(_txt(hx + hww / 2.0, hy + hhh + 18, "L", 9, color=INK))
    # liquid depth F
    o.append(_line(hx + 18, hy + hhh - 14, hx + 18, hy + hhh, sw=1.0, color=BLUE))
    o.append(_txt(hx + 22, hy + hhh - 4, "F", 8, anchor="start", color=BLUE))
    o.append(_txt(hx + hww / 2.0, hy - 10, "Horizontal cylinder", 8, color=INK))

    # Vertical cylinder
    vx, vy, vw, vh = 430, 70, 60, 150
    o.append(_rect(vx, vy, vw, vh, fill="#f4f7fb", sw=1.4))
    o.append(_line(vx + vw, vy + vh, vx, vy + vh, sw=0.8, dash="2 2", color=GREY))  # D
    o.append(_txt(vx + vw / 2.0, vy + vh + 14, "D", 9, color=INK))
    o.append(_line(vx - 12, vy, vx - 12, vy + vh, sw=0.8, color=GREY))  # H
    o.append(_txt(vx - 16, vy + vh / 2.0, "H", 9, anchor="end", color=INK))
    o.append(_line(vx + vw + 8, vy + vh - 20, vx + vw + 8, vy + vh, sw=1.0, color=BLUE))  # F
    o.append(_txt(vx + vw + 12, vy + vh - 8, "F", 8, anchor="start", color=BLUE))
    o.append(_txt(vx + vw / 2.0, vy - 10, "Vertical cylinder", 8, color=INK))

    o.append(_txt(260, h - 10, "D — đường kính · L — chiều dài · H — chiều cao · F — mức chất lỏng", 7.2, color=INK))
    s = svg(w, h, "".join(o), esc("Vessel / tank selection diagram for fire sizing"))
    return _fig(s,
                "Hình F7-13 · Sơ đồ chọn bình (cầu, xi lanh ngang / đứng) cho tính toán hỏa hoạn.",
                "Figure F7-13 · Vessel (tank) selection diagram — sphere, horizontal & vertical cylinders.",
                "Sơ đồ các loại bình cho tính toán hỏa hoạn với kích thước D, L, H, F",
                "Vessel selection diagram showing sphere and horizontal/vertical cylinders")


FIGS = {
    "f22_closed": fig_f22_closed, "f22_open": fig_f22_open,
    "f23": fig_f23, "f24": fig_f24, "f26": fig_f26, "f29": fig_f29,
    "f71": fig_f71, "f72": fig_f72, "f73": fig_f73, "f74": fig_f74,
    "f75": fig_f75, "f76": fig_f76, "f77": fig_f77, "f712": fig_f712, "f713": fig_f713,
}
