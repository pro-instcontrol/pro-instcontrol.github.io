# -*- coding: utf-8 -*-
"""Vector figures 11.1-11.2 for PPIC chapter 11 (adaptive power control).

Genuine vector redraws of the two printed schematic figures:
  fig_f01 -- MHTGR-based nuclear steam supplying module (NSSM), printed p.257
             (PDF p.273): vertical cutaway of the pebble-bed reactor beside
             the OTSG and helium blower, joined by a coaxial gas duct.
  fig_f02 -- micro-grid constituted by nuclear fission and photovoltaic
             energy, printed p.258 (PDF p.274): electrical and heat/water
             paths between the plants, the combined grid and the consumers.
"""
import math

from ppicfig11_common import (BLUE, GREEN, GREY, INK, RED, W, T, _ar,
                              _circle, _defs, _fig, _frame, _line,
                              _poly, _rect, _mk, _series, make_registry)

FIGS, _reg = make_registry()


def _blk(x, y, w, h, label, fill="#eef3fb"):
    """Labelled plant/consumer block with an optional second text line."""
    o = [_rect(x, y, w, h, fill, sw=1.2)]
    lines = label.split("\n")
    cy = y + h / 2.0 - (len(lines) - 1) * 4.7 + 2.6
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, cy + i * 9.6, ln, 7.2, color=INK))
    return "".join(o)


# ------------------------------------------------------------------- fig 11.1
@_reg
def fig_f01():
    o = [_defs()]
    o.append(T(340, 12, "MHTGR-based nuclear steam supplying module (NSSM)",
               8.6, color=INK, anchor="middle", weight="600"))

    # ---- reactor vessel, vertical cutaway ---------------------------------
    o.append(_poly([(205, 72), (212, 56), (228, 48), (282, 48), (298, 56),
                    (305, 72), (305, 250), (298, 260), (282, 267),
                    (228, 267), (212, 260), (205, 250)],
                   fill="#fbfaf7", sw=1.6, close=True))
    # reflector band inside the vessel
    o.append(_poly([(213, 74), (218, 63), (232, 57), (278, 57), (292, 63),
                    (297, 74), (297, 244), (292, 253), (278, 258),
                    (232, 258), (218, 253), (213, 244)],
                   fill="#e8ecef", sw=1.0, color=GREY, close=True))
    # cold helium riser (annular channel on the core outer side)
    o.append(_rect(284, 88, 11, 120, fill="#e7f0fb", sw=0.8, stroke=BLUE))
    # pebble-bed core
    o.append(_rect(228, 88, 54, 120, fill="#fff4e6", sw=0.9,
                   stroke="#c8915a"))
    for r in range(10):
        yy = 94.0 + r * 11.5
        for c in range(5):
            xx = 233.0 + c * 11.0 + (5.5 if r % 2 else 0.0)
            if xx <= 280:
                o.append(_circle(xx, yy, 3.0, fill="#d98a3a", sw=0.5,
                                 color="#a85f22"))
    # hot helium chamber at the vessel bottom
    o.append(_rect(215, 208, 80, 36, fill="#fde3d8", sw=0.9, stroke=RED))
    for xx in (240, 255, 270):
        o.append(_ar(xx, 198, xx, 207, color=RED, sw=1.1))
    for yy0, yy1 in ((190, 162), (152, 124), (114, 96)):
        o.append(_ar(289, yy0, 289, yy1, color=BLUE, sw=1.2))

    # control rod driving mechanism on the vessel head
    o.append(_rect(240, 22, 30, 18, fill="#dfe8f3", sw=1.2, stroke=BLUE))
    for xx in (248, 262):
        o.append(_line(xx, 40, xx, 96, sw=1.5, color=BLUE))
        o.append(_rect(xx - 2.5, 92, 5, 8, fill="#5b6b7a", sw=0))

    # ---- coaxial hot/cold gas duct ----------------------------------------
    o.append(_rect(300, 206, 115, 36, fill="#fdece7", sw=1.2))
    o.append(_rect(300, 215, 115, 18, fill="#e7f0fb", sw=1.0, stroke=BLUE))
    for yy in (211, 237):
        o.append(_ar(304, yy, 411, yy, color=RED, sw=1.6))
    o.append(_ar(411, 224, 304, 224, color=BLUE, sw=1.8))

    # ---- OTSG and helium blower -------------------------------------------
    o.append(_rect(415, 72, 63, 178, fill="#fbfaf7", sw=1.4))
    o.append(_rect(415, 72, 63, 16, fill="#dfe8f3", sw=1.0, stroke=BLUE))
    for xx in range(423, 476, 9):
        o.append(_line(xx, 92, xx, 150, sw=2.0, color=RED))
        o.append(_line(xx, 150, xx, 236, sw=2.0, color=GREEN))
    o.append(_rect(415, 236, 63, 14, fill="#fde3d8", sw=0.9, stroke=RED))
    for xx in (432, 450, 468):
        o.append(_ar(xx, 146, xx, 108, color=RED, sw=1.2))
    # blower above the steam generator, with its short connecting neck
    o.append(_rect(440, 64, 12, 8, fill="#dfe8f3", sw=0.9, stroke=BLUE))
    o.append(_circle(446, 53, 13, fill="#dfe8f3", sw=1.3, color=BLUE))
    for a in (0, 120, 240):
        rad = a * math.pi / 180.0
        o.append(_line(446, 53, 446 + 9 * math.cos(rad),
                       53 + 9 * math.sin(rad), sw=1.1, color=BLUE))
    o.append(_ar(446, 68, 446, 73, color=BLUE, sw=1.1))

    # ---- component labels with leader lines -------------------------------
    o.append(T(318, 26, "Control rod driving mechanism", 6.8, color=INK,
               anchor="start"))
    o.append(_line(271, 30, 314, 26, sw=0.7, color=GREY))
    o.append(T(70, 96, "Reflector", 6.8, color=INK, anchor="start"))
    o.append(_line(119, 96, 213, 100, sw=0.7, color=GREY))
    o.append(T(318, 110, "Pebble-bed of fuel elements", 6.8, color=INK,
               anchor="start"))
    o.append(_line(283, 112, 314, 110, sw=0.7, color=GREY))
    o.append(T(318, 145, "Cold helium riser", 6.8, color=BLUE, anchor="start"))
    o.append(_line(296, 147, 314, 145, sw=0.7, color=GREY))
    o.append(T(70, 232, "Hot helium chamber", 6.8, color=RED, anchor="start"))
    o.append(_line(142, 232, 215, 230, sw=0.7, color=GREY))
    o.append(T(357, 257, "Coaxial hot/cold gas duct", 6.8, color=INK,
               anchor="middle"))
    o.append(T(490, 52, "Helium blower", 6.8, color=BLUE, anchor="start"))
    o.append(_line(460, 53, 486, 52, sw=0.7, color=GREY))
    o.append(T(490, 185, "OTSG (once-through steam generator)", 6.8,
               color=INK, anchor="start"))
    o.append(_line(479, 185, 486, 185, sw=0.7, color=GREY))

    # flow colour key
    o.append(_line(56, 298, 76, 298, sw=2.0, color=RED))
    o.append(T(80, 301, "hot helium", 6.2, color=RED, anchor="start"))
    o.append(_line(160, 298, 180, 298, sw=2.0, color=BLUE))
    o.append(T(184, 301, "cold helium", 6.2, color=BLUE, anchor="start"))

    return _mk(
        1, o,
        "Schematic view of an MHTGR-based NSSM",
        "Sơ đồ mô-đun cung cấp hơi nước NSSM dùng lò phản ứng MHTGR",
        "Schematic view of an MHTGR-based nuclear steam supplying module",
        "Sơ đồ cắt ngang mô-đun NSSM dùng MHTGR gồm cơ cấu dẫn thanh điều khiển, lớp phản xạ, giường nhiên liệu dạng viên, đường nâng khí lạnh, buồng khí nóng, ống dẫn đồng trục, máy thổi khí và máy phát hơi nước một lần chảy.",
        "Vertical cutaway of an MHTGR-based nuclear steam supplying module showing the control rod drive mechanism, reflector, pebble-bed fuel elements, cold helium riser, hot helium chamber, coaxial hot/cold gas duct, helium blower and once-through steam generator.")


# ------------------------------------------------------------------- fig 11.2
@_reg
def fig_f02():
    o = [_defs()]
    o.append(T(340, 12, "Micro-grid with MHTGR-based nuclear and PV plants",
               8.6, color=INK, anchor="middle", weight="600"))

    # ---- plants, grid and consumers ---------------------------------------
    o.append(_blk(18, 34, 142, 42, "PV plant"))
    o.append(_blk(18, 96, 142, 46, "MHTGR-based\nnuclear plant"))
    o.append(_blk(18, 166, 142, 40, "Electricity\nconsumer"))
    o.append(_blk(18, 230, 142, 40, "Water consumer"))
    o.append(_blk(330, 34, 160, 46, "Combined grid", fill="#e8eef7"))
    o.append(_blk(330, 198, 160, 56, "Sea-water\ndesalination plant",
                  fill="#eaf2ec"))

    # central electrical busbar
    o.append(_line(232, 26, 232, 286, sw=3.0, color=INK))
    o.append(T(232, 20, "busbar", 6.2, color=GREY, anchor="middle"))

    # ---- electrical paths (gold) ------------------------------------------
    o.append(_ar(160, 55, 228, 55, color="#b45309", sw=1.9))
    o.append(T(194, 48, "electrical power", 6.2, color="#b45309"))
    o.append(_ar(160, 119, 228, 119, color="#b45309", sw=1.9))
    o.append(T(194, 112, "electrical power", 6.2, color="#b45309"))
    o.append(_ar(236, 57, 326, 57, color="#b45309", sw=1.9))
    o.append(T(281, 50, "electrical power", 6.2, color="#b45309"))
    o.append(_ar(228, 186, 164, 186, color="#b45309", sw=1.9))
    o.append(T(204, 179, "electricity", 6.2, color="#b45309"))
    o.append(_ar(236, 216, 326, 216, color="#b45309", sw=1.9))
    o.append(T(281, 209, "electricity", 6.2, color="#b45309"))

    # ---- process heat from the nuclear plant (red) ------------------------
    o.append(_poly([(160, 130), (182, 130), (182, 238), (310, 238)],
                   sw=1.9, color=RED))
    o.append(_ar(310, 238, 326, 238, color=RED, sw=1.9))
    o.append(_rect(176, 206, 12, 12, fill="#f6c453", sw=0.8))
    o.append(T(182, 215, "P", 5.5, color=INK, anchor="middle"))
    o.append(T(248, 232, "process heat", 6.2, color=RED, anchor="middle"))

    # ---- fresh water to the water consumer (blue) -------------------------
    o.append(_ar(326, 250, 164, 250, color=BLUE, sw=1.9))
    o.append(T(245, 244, "fresh water", 6.2, color=BLUE, anchor="middle"))

    # path colour key
    o.append(T(340, 300, "Gold: electricity    Red: process heat    "
                         "Blue: fresh water", 6.2, color=GREY,
               anchor="middle"))

    return _mk(
        2, o,
        "A micro-grid constituted by nuclear fission and photovoltaic energy",
        "Micro-lưới điện kết hợp năng lượng hạt nhân và quang điện",
        "A micro-grid constituted by nuclear fission and photovoltaic energy",
        "Sơ đồ micro-lưới điện: nhà máy quang điện và nhà máy hạt nhân MHTGR cùng cấp điện cho lưới kết hợp; người tiêu dùng điện và người tiêu dùng nước nối với lưới và nhà máy khử mặn nước biển qua đường dẫn nhiệt và nước ngọt.",
        "Micro-grid scheme: a PV plant and an MHTGR-based nuclear plant supply a combined grid; electricity and water consumers are linked to the grid and to a sea-water desalination plant through electrical, process-heat and fresh-water paths.")
