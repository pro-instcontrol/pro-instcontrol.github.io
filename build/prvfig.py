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
import re
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _box, _circle, _defs, _f as fmt, _fig, _line,
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


FIGS = {
    "f22_closed": fig_f22_closed, "f22_open": fig_f22_open,
    "f23": fig_f23, "f24": fig_f24, "f26": fig_f26, "f29": fig_f29,
}
