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
                  _defs, _fig, _line, _poly, _rect, _txt, svg)

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
