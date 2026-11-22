# -*- coding: utf-8 -*-
"""Vector figures for Book 7 — Baumann, *Control Valve Primer*, 5th ed.

Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
Diagrams are simplified vector re-drawings of the source figures.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _box, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f11():
    """Figure 1-1 — basic control valve terminology tree (ANSI/ISA-75.05.01)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(_box(276, 12, 128, 30, "Control valve", fill="#fdf3e6", sw=1.5, size=10))
    # two main branches
    o.append(_box(40, 76, 220, 30, "Actuated (power)", fill="#eef3fb", sw=1.2, size=9))
    o.append(_box(420, 76, 220, 30, "Manually actuated", fill="#eef3fb", sw=1.2, size=9))
    o.append(_arrow(310, 42, 150, 76, sw=1.1))
    o.append(_arrow(370, 42, 530, 76, sw=1.1))
    # actuated types
    for i, lab in enumerate(["Pneumatic diaphragm", "Pneumatic piston",
                             "Electric motor", "Electro-hydraulic", "Hydraulic"]):
        o.append(_box(18 + i * 50, 132, 48, 56, lab, fill="#f4f7fb", sw=0.9, size=6.4))
    o.append(_arrow(150, 106, 143, 132, sw=0.9))
    # manual / self acting
    for i, lab in enumerate(["Handwheel", "Lever", "Regulator", "Relief valve"]):
        o.append(_box(398 + i * 62, 136, 60, 48, lab, fill="#f4f7fb", sw=0.9, size=7.0))
    o.append(_arrow(530, 106, 500, 136, sw=0.9))
    # valve body families
    o.append(_txt(340, 218, esc("Valve body styles — linear motion / rotary motion"),
                  9.4, color=INK, weight="600"))
    lin = ["Globe", "Gate", "Diaphragm", "Pinch / clamp", "Angle", "Three-way", "Knife"]
    rot = ["Ball", "Segmented ball", "Butterfly", "Plug — cylindrical",
           "Plug — tapered", "Eccentric sphere"]
    for i, lab in enumerate(lin):
        o.append(_box(24 + (i % 4) * 84, 240 + (i // 4) * 40, 80, 32, lab,
                      fill="#eaf6ee", sw=1.0, size=7.0))
    for i, lab in enumerate(rot):
        o.append(_box(370 + (i % 3) * 100, 240 + (i // 3) * 40, 96, 32, lab,
                      fill="#eaf6ee", sw=1.0, size=6.8))
    o.append(_txt(340, 338, "Positioner (optional) — pneumatic / electric / electro-pneumatic",
                  8.2, color=GREY))
    o.append(_txt(340, 366,
                  "Sơ đồ thuật ngữ theo ANSI/ISA-75.05.01-2000 (R2005) · vẽ lại dạng vector",
                  7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Control valve terminology tree after ANSI/ISA-75.05.01"))
    return _fig(s,
                "Hình 1-1 · Cây thuật ngữ van điều khiển theo ANSI/ISA-75.05.01-2000 (R2005): "
                "van được chia theo cơ cấu chấp hành (khí nén, điện, thủy lực) và kiểu thân "
                "van (chuyển động tuyến tính hoặc quay), với bộ định vị là tùy chọn.",
                "Figure 1-1 · Control valve terminology tree after ANSI/ISA-75.05.01-2000 "
                "(R2005): valves classified by actuator (pneumatic, electric, hydraulic) and "
                "body style (linear or rotary motion), with the positioner optional.",
                "Cây thuật ngữ van điều khiển theo ANSI/ISA-75.05.01",
                "Control valve terminology tree after ANSI/ISA-75.05.01")


@_reg
def fig_f12():
    """Figure 1-2 — control-loop block diagram with valve dynamic blocks."""
    w, h = 680, 300
    o = [_defs()]
    # main loop
    boxes = [(18, 92, 110, 42, "Transmitter"), (168, 92, 110, 42, "Controller"),
             (330, 92, 130, 42, "Control valve"), (502, 92, 150, 42, "Process")]
    for x, y, bw, bh, lab in boxes:
        o.append(_box(x, y, bw, bh, lab, fill="#eef3fb", sw=1.2, size=9))
    o.append(_arrow(128, 113, 168, 113, color=BLUE))
    o.append(_arrow(278, 113, 330, 113, color=BLUE))
    o.append(_arrow(460, 113, 502, 113, color=BLUE))
    # feedback line
    o.append(_line(577, 134, 577, 236, sw=1.1, color=GREY))
    o.append(_line(577, 236, 73, 236, sw=1.1, color=GREY))
    o.append(_arrow(73, 236, 73, 134, color=GREY))
    o.append(_txt(325, 252, "Process variable feedback", 7.6, color=GREY))
    # set point
    o.append(_arrow(223, 46, 223, 92, color=GREEN))
    o.append(_txt(223, 38, "Set point", 8.4, color=GREEN))
    # dynamic blocks above the valve
    o.append(_txt(395, 30, "Valve dynamic blocks", 8.8, color=INK, weight="600"))
    dyn = [("Kᵥ", "Valve gain"), ("Tᴅᵥ", "Dead time"), ("Tᴄᵥ", "Time constant")]
    for i, (sym, lab) in enumerate(dyn):
        x = 300 + i * 122
        o.append(_rect(x, 158, 112, 48, fill="#fdf3e6", sw=1.1))
        o.append(_txt(x + 56, 178, sym, 11, color=RED, weight="600"))
        o.append(_txt(x + 56, 196, lab, 7.4, color=INK))
    o.append(_txt(340, 280,
                  "Sơ đồ khối vòng điều khiển · Kᵥ, Tᴅᵥ, Tᴄᵥ là ba thông số động học của van",
                  7.6, color=GREY))
    s = svg(w, h, "".join(o), esc("Control loop block diagram with valve dynamics"))
    return _fig(s,
                "Hình 1-2 · Sơ đồ khối của vòng điều khiển: cảm biến – bộ phát – bộ điều khiển – "
                "van điều khiển – quá trình, với ba khối động học của van là độ khuếch đại Kᵥ, "
                "thời gian chết Tᴅᵥ và hằng số thời gian Tᴄᵥ.",
                "Figure 1-2 · Block diagram of a control loop: sensor – transmitter – "
                "controller – control valve – process, with the three valve dynamic blocks "
                "of gain Kᵥ, dead time Tᴅᵥ and time constant Tᴄᵥ.",
                "Sơ đồ khối vòng điều khiển với các thông số động học của van",
                "Control loop block diagram with valve dynamic parameters")


@_reg
def fig_f13():
    """Figure 1-3 — early 1932 spring-diaphragm double-seated control valve."""
    w, h = 560, 380
    o = [_defs()]
    # actuator housing
    o.append(_rect(150, 24, 260, 92, fill="#eef3fb", sw=1.4))
    o.append(_txt(280, 44, "Spring-diaphragm actuator", 9, color=INK, weight="600"))
    # diaphragm
    o.append(_line(160, 72, 400, 72, sw=2.2, color=BLUE))
    o.append(_txt(280, 88, "Diaphragm", 7.8, color=BLUE))
    # spring (zigzag)
    pts = [(280, 74)]
    for i in range(9):
        pts.append((268 if i % 2 == 0 else 292, 84 + i * 3))
    pts.append((280, 112))
    o.append(_poly(pts, sw=1.5, color=GREY))
    o.append(_txt(318, 100, "Spring", 7.6, color=GREY))
    # stem
    o.append(_line(280, 112, 280, 250, sw=2.4, color=INK))
    o.append(_txt(296, 180, "Stem", 7.6, color=GREY))
    # valve body
    o.append(_rect(170, 250, 220, 88, fill="#f4f7fb", sw=1.6))
    o.append(_txt(280, 268, "Double-seated valve body", 8.2, color=INK, weight="600"))
    # two plugs
    o.append(_circle(244, 296, 15, fill="#fdf3e6", sw=1.4))
    o.append(_circle(326, 296, 15, fill="#fdf3e6", sw=1.4))
    o.append(_txt(244, 299, "↑", 10, color=RED))
    o.append(_txt(326, 299, "↓", 10, color=RED))
    o.append(_txt(285, 300, "fluid forces", 7.2, color=GREY))
    # flow path
    o.append(_line(170, 310, 390, 310, sw=3, color=GREEN))
    o.append(_txt(280, 332, "Flow tends to cancel — reduced actuator force", 7.4, color=GREEN))
    o.append(_txt(280, 366,
                  "Cắt ngang van điều khiển sơ kỳ năm 1932 (Neilan Co.) · vẽ lại dạng vector",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Early 1932 double-seated spring-diaphragm control valve"))
    return _fig(s,
                "Hình 1-3 · Mặt cắt van điều khiển lò xo–màng sơ kỳ (khoảng 1932) của hãng "
                "Neilan: van hai chỗ ngồi được phát triển để giảm lực chấp hành — áp suất "
                "chất lỏng đẩy nút trên lên và nút dưới xuống, làm triệt tiêu gần như hoàn toàn "
                "lưu chất.",
                "Figure 1-3 · Cross-section of an early spring-diaphragm control valve "
                "(circa 1932) by the Neilan Company: the double-seated design was developed "
                "to reduce actuator forces — fluid pressure pushes the upper plug up and "
                "the lower plug down, achieving near cancellation of fluid forces.",
                "Mặt cắt van điều khiển lò xo–màng hai chỗ ngồi năm 1932",
                "Cross-section of an early double-seated spring-diaphragm control valve")


@_reg
def fig_f31():
    """Figure 3-1 — idealized modern cage-type control valve, section view."""
    w, h = 680, 440
    o = [_defs()]
    o.append(_txt(340, 19, esc("Cage-type control valve - section view"), 10.5,
                  color=INK, weight="600"))

    # Flow passages and the central chamber
    o.append(_rect(40, 196, 200, 54, fill="#dceaf5", sw=1.2))
    o.append(_rect(440, 196, 200, 54, fill="#dceaf5", sw=1.2))
    o.append(_rect(240, 150, 200, 150, fill="#fbfaf7", sw=1.2))
    # Body metal in section hatch
    for x, y, bw, bh in ((40, 250, 200, 26), (40, 178, 200, 18),
                         (440, 250, 200, 26), (440, 178, 200, 18),
                         (240, 300, 200, 24)):
        o.append(_rect(x, y, bw, bh, fill="url(#h6)", sw=1.0))
    # Seat ring with a central bore
    o.append(_rect(258, 284, 72, 18, fill="url(#h6)", sw=1.2))
    o.append(_rect(350, 284, 72, 18, fill="url(#h6)", sw=1.2))
    # Bonnet, studs, stem packing
    o.append(_rect(286, 60, 108, 58, fill="url(#h6)", sw=1.2))
    o.append(_line(280, 64, 280, 116, sw=2.2, color=GREY))
    o.append(_line(400, 64, 400, 116, sw=2.2, color=GREY))
    o.append(_rect(330, 92, 20, 26, fill="#f6e6c8", sw=1.1))
    # Cage: two walls with a window gap, split top ring
    o.append(_rect(272, 118, 18, 58, fill="url(#h6)", sw=1.1))
    o.append(_rect(272, 208, 18, 76, fill="url(#h6)", sw=1.1))
    o.append(_rect(390, 118, 18, 58, fill="url(#h6)", sw=1.1))
    o.append(_rect(390, 208, 18, 76, fill="url(#h6)", sw=1.1))
    o.append(_rect(272, 118, 58, 12, fill="url(#h6)", sw=1.1))
    o.append(_rect(350, 118, 58, 12, fill="url(#h6)", sw=1.1))
    # Plug / piston with contoured tip and upper protrusion
    o.append(_rect(300, 166, 80, 72, fill="#f6e6c8", sw=1.4))
    o.append(_poly([(300, 238), (340, 258), (380, 238)],
                   fill="#f6e6c8", sw=1.4, close=True))
    o.append(_rect(380, 178, 18, 16, fill="#f6e6c8", sw=1.2))
    o.append(_line(340, 52, 340, 166, sw=3, color=INK))
    # Seals B and C, staked connection E
    o.append(_rect(300, 158, 80, 8, fill=RED, sw=1.0))
    o.append(_rect(272, 112, 136, 6, fill=RED, sw=1.0))
    o.append(_circle(340, 160, 4, fill=RED, sw=0))
    # Flow path: inlet, first stage, window, outlet
    o.append(_arrow(120, 223, 250, 223, sw=2, color=BLUE))
    o.append(_arrow(300, 316, 336, 298, sw=2, color=BLUE))
    o.append(_arrow(340, 280, 340, 254, sw=2, color=BLUE))
    o.append(_arrow(360, 244, 424, 200, sw=2, color=BLUE))
    o.append(_arrow(462, 223, 610, 223, sw=2, color=BLUE))

    def mk(x, y, lab, tx, ty):
        return (_circle(x, y, 9, fill="#ffffff", sw=1.3, color=RED)
                + _txt(x, y + 3.2, lab, 8, color=RED, weight="700")
                + _line(x, y, tx, ty, sw=0.9, color=GREY))

    o.append(mk(448, 176, "A", 406, 194))
    o.append(mk(300, 146, "B", 320, 158))
    o.append(mk(262, 110, "C", 284, 114))
    o.append(mk(252, 276, "D", 274, 270))
    o.append(mk(420, 80, "E", 348, 96))

    o.append(_line(40, 336, 640, 336, sw=0.8, color=GREY))
    legend = [
        "A · dual-stage throttling / tiết lưu hai cấp",
        "B · flexible top seal / phớt trên mềm",
        "C · compressible bonnet seal / phớt nắp nén",
        "D · cage screwed into body / lồng vặn ren vào thân",
        "E · staked stem joint / mối nối thân ép chốt",
    ]
    for i, t in enumerate(legend[:3]):
        o.append(_txt(40, 356 + i * 22, esc(t), 8, anchor="start", color=INK))
    for i, t in enumerate(legend[3:]):
        o.append(_txt(360, 356 + i * 22, esc(t), 8, anchor="start", color=INK))
    o.append(_txt(340, 426,
                  esc("After Baumann, Control Valve Primer - US Patents 6,701,958; "
                      "6,766,826; 7,083,160 (Fisher Controls International)."),
                  7.2, color=GREY))
    s = svg(w, h, "".join(o), esc("Cage-type control valve section with callouts A to E"))
    return _fig(s,
                "Hình 3-1 · Mặt cắt thân van điều khiển kiểu lồng hiện đại: A tiết lưu hai cấp "
                "(chống xâm thực, dải điều tiết rộng), B phớt trên mềm, C phớt nắp van nén dẻo, "
                "D lồng được vặn ren vào thân, E mối nối thân nút được ép chốt thay vì dùng chốt "
                "hầm. Nguồn: US Patents 6,701,958; 6,766,826; 7,083,160 (Fisher Controls "
                "International).",
                "Figure 3-1 · Section of a modern cage-type control valve body: A dual-stage "
                "throttling (greater cavitation resistance and high rangeability), B flexible "
                "top seal, C compressible bonnet-to-cage seal, D cage screwed into the body, "
                "E staked stem-to-plug connection instead of a loose pin. Reference: US Patents "
                "6,701,958; 6,766,826; 7,083,160 (Fisher Controls International).",
                "Mặt cắt van điều khiển kiểu lồng với chú thích A đến E",
                "Cross-section of a cage-type control valve with callouts A to E")


@_reg
def fig_f32():
    """Figure 3-2 — single-seated globe valve, screwed-in seat, V-port plug."""
    w, h = 620, 410
    o = [_defs()]
    o.append(_txt(310, 18, esc("Single-seated globe valve - section view"), 10.5,
                  color=INK, weight="600"))
    # Flow passages and chamber
    o.append(_rect(40, 232, 180, 52, fill="#dceaf5", sw=1.2))
    o.append(_rect(400, 232, 180, 52, fill="#dceaf5", sw=1.2))
    o.append(_rect(220, 148, 180, 152, fill="#fbfaf7", sw=1.2))
    # Body metal in section hatch
    for x, y, bw, bh in ((40, 284, 180, 26), (40, 210, 180, 22),
                         (400, 284, 180, 26), (400, 210, 180, 22),
                         (198, 148, 22, 162), (400, 148, 22, 162),
                         (220, 300, 180, 24), (220, 148, 68, 14),
                         (322, 148, 78, 14)):
        o.append(_rect(x, y, bw, bh, fill="url(#h6)", sw=1.0))
    # Screwed-in seat ring, split by the bore; thread marks on the outer edges
    o.append(_rect(258, 254, 40, 18, fill="url(#h6)", sw=1.2))
    o.append(_rect(322, 254, 40, 18, fill="url(#h6)", sw=1.2))
    for dx in (252, 256, 260):
        o.append(_line(dx, 258, dx + 6, 252, sw=0.9, color=INK))
    for dx in (356, 360, 364):
        o.append(_line(dx, 258, dx + 6, 252, sw=0.9, color=INK))
    # V-port plug and stem
    o.append(_poly([(272, 180), (348, 180), (348, 236), (332, 236),
                    (310, 252), (288, 236), (272, 236)],
                   fill="#f6e6c8", sw=1.5, close=True))
    o.append(_line(310, 70, 310, 180, sw=3, color=INK))
    # Bonnet, packing, actuator stub
    o.append(_rect(268, 76, 84, 72, fill="url(#h6)", sw=1.2))
    o.append(_rect(298, 104, 24, 36, fill="#f6e6c8", sw=1.1))
    o.append(_rect(240, 36, 140, 40, fill="#eef3fb", sw=1.2))
    o.append(_txt(310, 60, esc("Actuator stem"), 8, color=INK))
    # Flow path
    o.append(_arrow(86, 258, 268, 258, sw=2, color=BLUE))
    o.append(_arrow(310, 266, 310, 244, sw=2, color=BLUE))
    o.append(_arrow(338, 240, 424, 258, sw=2, color=BLUE))
    o.append(_arrow(466, 258, 566, 258, sw=2, color=BLUE))

    def mk(x, y, lab, tx, ty):
        return (_circle(x, y, 9, fill="#ffffff", sw=1.3, color=RED)
                + _txt(x, y + 3.2, lab, 8, color=RED, weight="700")
                + _line(x, y, tx, ty, sw=0.9, color=GREY))

    o.append(mk(430, 186, "1", 350, 208))
    o.append(mk(430, 292, "2", 364, 262))
    o.append(mk(214, 120, "3", 300, 116))

    o.append(_line(40, 330, 580, 330, sw=0.8, color=GREY))
    for i, t in enumerate(["1 · V-port plug / nút cổng chữ V",
                           "2 · screwed-in seat ring / vòng đế vặn ren",
                           "3 · stem packing / bao bình thân van"]):
        o.append(_txt(40, 348 + i * 20, esc(t), 8, anchor="start", color=INK))
    o.append(_txt(310, 402,
                  esc("Plug and seat ring: type 316 stainless steel - source: SAMSON AG"),
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Single-seated globe valve with screwed-in seat and V-port plug"))
    return _fig(s,
                "Hình 3-2 · Mặt cắt van cầu một chỗ ngồi cỡ nhỏ với vòng đế vặn ren vào thân "
                "và nút có cổng chữ V: 1 nút cổng chữ V, 2 vòng đế vặn ren, 3 bao bình thân "
                "giúp ma sát và vùng chết thấp. Nút và vòng đế thường làm bằng thép không gỉ "
                "type 316. Nguồn: SAMSON AG.",
                "Figure 3-2 · Section of a smaller single-seated globe valve with a screwed-in "
                "seat ring and a V-port plug: 1 V-port plug, 2 screwed-in seat ring, 3 stem "
                "packing for low friction and deadband. Plug and seat ring are typically made "
                "from type 316 stainless steel. Source: Courtesy of SAMSON AG.",
                "Mặt cắt van cầu một chỗ ngồi với vòng đế vặn ren và nút cổng chữ V",
                "Section of a single-seated globe valve with screwed-in seat and V-port plug")


@_reg
def fig_f33():
    """Figure 3-3 — rotary control valve with field-replaceable seat and insert."""
    w, h = 680, 420
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Rotary control valve - high-performance butterfly, section"),
                  10.5, color=INK, weight="600"))
    # Body ring, bore, and field-replaceable seat/seal
    o.append(_circle(250, 190, 116, fill="url(#h6)", sw=1.5))
    o.append(_circle(250, 190, 96, fill="#fbfaf7", sw=1.3))
    o.append(_circle(250, 190, 90, fill="none", sw=3, color=RED))
    # Rotating disc (closure member)
    o.append(_poly([(327, 147), (317, 132), (173, 233), (183, 248)],
                   fill="#f6e6c8", sw=1.6, close=True))
    # Shaft and actuator
    o.append(_line(250, 62, 250, 318, sw=4, color=INK))
    o.append(_circle(250, 190, 5, fill=INK, sw=0))
    o.append(_rect(186, 26, 128, 36, fill="#eef3fb", sw=1.2))
    o.append(_txt(250, 48, esc("Actuator + positioner"), 8, color=INK))
    # Flow path
    o.append(_arrow(70, 190, 176, 190, sw=2, color=BLUE))
    o.append(_arrow(324, 190, 392, 190, sw=2, color=BLUE))
    # Perforated low-noise insert segments
    for x, y in ((292, 236), (308, 242), (324, 248), (340, 254)):
        o.append(_rect(x, y, 14, 9, fill="#dceaf5", sw=1.0, stroke=BLUE))

    def mk(x, y, lab, tx, ty):
        return (_circle(x, y, 9, fill="#ffffff", sw=1.3, color=RED)
                + _txt(x, y + 3.2, lab, 8, color=RED, weight="700")
                + _line(x, y, tx, ty, sw=0.9, color=GREY))

    o.append(mk(348, 138, "1", 322, 143))
    o.append(mk(300, 96, "2", 254, 92))
    o.append(mk(150, 282, "3", 178, 254))
    o.append(mk(362, 262, "4", 348, 256))

    o.append(_txt(410, 100, esc("Legend / Chú thích"), 9, anchor="start",
                  color=INK, weight="600"))
    legend = [
        (120, "1 - rotating disc (closure member)", "   đĩa quay (cơ cấu đóng)"),
        (156, "2 - shaft, backlash-free link", "   trục, liên kết không hở"),
        (192, "3 - field-replaceable seat and seal", "   chỗ ngồi và phớt thay tại hiện trường"),
        (228, "4 - field-attachable low-noise insert", "   chi tiết giảm ồn lắp tại hiện trường"),
    ]
    for y, en, vi in legend:
        o.append(_txt(410, y, esc(en), 8, anchor="start", color=INK))
        o.append(_txt(410, y + 13, esc(vi), 7.6, anchor="start", color=GREY))
    o.append(_txt(340, 398,
                  esc("After Baumann, Control Valve Primer - source: H. D. Baumann Inc."),
                  7.2, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Rotary control valve section with replaceable seat and low-noise insert"))
    return _fig(s,
                "Hình 3-3 · Van quay thiết kế riêng cho điều khiển (butterfly hiệu năng cao), "
                "mặt cắt: 1 đĩa quay là cơ cấu đóng, 2 trục với liên kết không hở tới cơ cấu "
                "chấp hành, 3 chỗ ngồi và phớt thay được tại hiện trường, 4 chi tiết giảm ồn, "
                "chống xâm thực lắp tại hiện trường. Nguồn: H. D. Baumann Inc.",
                "Figure 3-3 · Rotary valve designed especially for control (high-performance "
                "butterfly), section view: 1 rotating disc as the closure member, 2 shaft with "
                "a backlash-free link to the actuator, 3 field-replaceable seat and seal, "
                "4 field-attachable low-noise, anticavitation insert. Source: Courtesy of "
                "H. D. Baumann Inc.",
                "Mặt cắt van quay điều khiển với chỗ ngồi thay được và chi tiết giảm ồn",
                "Rotary control valve section with replaceable seat and low-noise insert")


@_reg
def fig_f41():
    """Figure 4-1 — spring-diaphragm-operated pressure-reducing regulator."""
    w, h = 680, 560
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Spring-diaphragm pressure-reducing regulator - section (simplified)"),
                  10.5, color=INK, weight="600"))

    # Upper spring case, setting screw and spring (spring pushes the
    # diaphragm down, which opens the plug; downstream pressure pushes back).
    o.append(_rect(250, 44, 180, 96, fill="#eef3fb", sw=1.4))
    o.append(_rect(329, 20, 22, 6, fill="#f6e6c8", sw=1.1))
    o.append(_rect(333, 24, 14, 22, fill="#f6e6c8", sw=1.1))
    o.append(_line(340, 44, 340, 58, sw=1.6, color=INK))
    pts = [(340, 56)]
    for i in range(11):
        pts.append((330 if i % 2 == 0 else 350, 62 + i * 7))
    pts.append((340, 138))
    o.append(_poly(pts, sw=1.6, color=GREY))

    # Diaphragm chamber and the diaphragm clamped at its rim.
    o.append(_rect(252, 140, 176, 50, fill="#fdf6e9", sw=1.3))
    o.append(_line(244, 140, 436, 140, sw=2.6, color=BLUE))
    o.append(_rect(240, 134, 10, 12, fill="url(#h6)", sw=1.0))
    o.append(_rect(432, 134, 10, 12, fill="url(#h6)", sw=1.0))

    # Stem runs down from the diaphragm to the plug below the seat.
    o.append(_line(340, 140, 340, 364, sw=2.6, color=INK))

    # Valve body in section, with fluid cavities above and below the seat.
    o.append(_rect(150, 290, 380, 110, fill="url(#h6)", sw=1.5))
    o.append(_rect(155, 300, 370, 36, fill="#eef5fa", sw=0.8))
    o.append(_rect(155, 352, 370, 38, fill="#eef5fa", sw=0.8))
    o.append(_rect(295, 336, 90, 16, fill="url(#h6)", sw=1.2))
    o.append(_rect(332, 336, 16, 16, fill="#eef5fa", sw=1.0))
    o.append(_poly([(320, 384), (360, 384), (350, 364), (330, 364)],
                   fill="#f6e6c8", sw=1.4, close=True))
    o.append(_rect(55, 352, 100, 38, fill="#dceaf5", sw=1.2))
    o.append(_rect(525, 300, 100, 36, fill="#dceaf5", sw=1.2))

    # Flow path: inlet, lower chamber, up through the seat, outlet.
    o.append(_arrow(62, 371, 152, 371, sw=2, color=BLUE))
    o.append(_arrow(170, 371, 312, 371, sw=2, color=BLUE))
    o.append(_arrow(340, 360, 340, 338, sw=2, color=BLUE))
    o.append(_arrow(360, 318, 520, 318, sw=2, color=BLUE))
    o.append(_arrow(532, 318, 615, 318, sw=2, color=BLUE))
    o.append(_txt(105, 342, esc("Flow"), 7.6, color=GREEN, weight="600"))

    # Downstream sensing line feeding the underside of the diaphragm.
    o.append(_poly([(560, 300), (560, 170), (428, 170)],
                   sw=1.3, color=BLUE, dash="5 3"))
    o.append(_circle(560, 300, 3, fill=BLUE, sw=0))
    o.append(_txt(494, 162, esc("Sensing line (downstream pressure)"),
                  7.2, color=BLUE))

    def mk(x, y, lab, tx, ty):
        return (_circle(x, y, 9, fill="#ffffff", sw=1.3, color=RED)
                + _txt(x, y + 3.2, lab, 8, color=RED, weight="700")
                + _line(x, y, tx, ty, sw=0.9, color=GREY))

    o.append(mk(200, 272, "1", 205, 292))
    o.append(mk(95, 415, "2", 95, 390))
    o.append(mk(610, 365, "3", 590, 336))
    o.append(mk(460, 118, "4", 434, 140))
    o.append(mk(450, 82, "5", 352, 84))
    o.append(mk(450, 33, "6", 348, 30))
    o.append(mk(240, 412, "7", 325, 380))
    o.append(mk(605, 200, "8", 562, 200))

    o.append(_line(40, 430, 640, 430, sw=0.8, color=GREY))
    legend_left = [
        "1 · Valve body / Thân van",
        "2 · Inlet, upstream / Đầu vào, thượng lưu",
        "3 · Outlet, downstream / Đầu ra, hạ lưu",
        "4 · Diaphragm / Màng",
    ]
    legend_right = [
        "5 · Adjustable spring / Lò xo điều chỉnh",
        "6 · Setting screw / Vít chỉnh áp",
        "7 · Plug and seat / Nút và đế van",
        "8 · Downstream sensing line / Ống dẫn áp hạ lưu",
    ]
    for i, t in enumerate(legend_left):
        o.append(_txt(40, 452 + i * 22, esc(t), 8.2, anchor="start", color=INK))
    for i, t in enumerate(legend_right):
        o.append(_txt(350, 452 + i * 22, esc(t), 8.2, anchor="start", color=INK))
    o.append(_txt(340, 545,
                  esc("After Baumann, Control Valve Primer - Fig. 4-1 - vector redraw; "
                      "sensing line drawn schematically."),
                  7.2, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Spring-diaphragm pressure-reducing regulator cross-section with callouts 1 to 8"))
    return _fig(s,
                "Hình 4-1 · Bộ điều chỉnh giảm áp vận hành bằng lò xo–màng (mặt cắt đơn giản "
                "hóa). Tải trọng lò xo điều chỉnh được tác dụng lên màng xác định áp suất đầu "
                "ra mong muốn; ống dẫn áp hạ lưu (vẽ dạng sơ đồ) giúp tăng độ chính xác của "
                "việc điều khiển áp suất. Khi áp suất hạ lưu tăng, màng đẩy nút lên cho đến "
                "khi lực trên màng cân bằng với tải trọng lò xo.",
                "Figure 4-1 · A spring-diaphragm-operated pressure-reducing regulator "
                "(simplified section). An adjustable spring load acting on the diaphragm "
                "determines the desired valve outlet pressure; a downstream sensing line "
                "(shown schematically) improves the accuracy of pressure control. As "
                "downstream pressure increases, the diaphragm moves the plug up until the "
                "force on the diaphragm equals the applied spring load.",
                "Mặt cắt bộ điều chỉnh giảm áp lò xo–màng với chú thích 1 đến 8",
                "Cross-section of a spring-diaphragm pressure-reducing regulator with callouts 1 to 8")
