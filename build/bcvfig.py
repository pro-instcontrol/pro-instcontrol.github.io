# -*- coding: utf-8 -*-
"""Vector figures for Borden/Friedmann, *Control Valves*, Chapter 5
"Control Valve Actuators" (ISA Practical Guides, 1998).

The local source is an image-only scan; the four numbered source figures
(5-1 ... 5-4) are redrawn here as simplified vector schematics.  Every
function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` built via ``_fig()``.
All SVG text is XML-escaped with ``esc()`` before it reaches ``_txt()``.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _fig, _line, _poly, _rect,
                  _txt, svg)

FIGS = {}


def _reg(f):
    # Register the evaluated 5-tuple: `fig(num, key)` consumes the tuple, and
    # the XML validation import does `ET.fromstring(s[0])` on every FIG value.
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _spring(cx, y0, y1, width=28, turns=6, color=GREY):
    """A helical compression spring drawn as a zigzag polyline."""
    pts = [(cx, y0)]
    n = turns * 2
    for i in range(1, n):
        yy = y0 + (y1 - y0) * i / float(n)
        pts.append((cx + (width / 2.0 if i % 2 else -width / 2.0), yy))
    pts.append((cx, y1))
    return _poly(pts, sw=1.5, color=color)


def _wheel(cx, cy, r=26, color=INK):
    """A handwheel: rim, hub, four spokes."""
    o = [_circle(cx, cy, r, sw=2.0, color=color),
         _circle(cx, cy, r * 0.22, fill="#fdf3e6", sw=1.2, color=color)]
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        o.append(_line(cx + dx * r * 0.22, cy + dy * r * 0.22,
                       cx + dx * r * 0.92, cy + dy * r * 0.92,
                       sw=1.2, color=color))
    return "".join(o)


@_reg
def fig_f51():
    """Figure 5-1 (source p. 94) — spring-opposed diaphragm, direct acting."""
    w, h = 560, 430
    o = [_defs()]
    # diaphragm case and air chamber
    o.append(_rect(150, 30, 260, 78, fill="#eef3fb", sw=1.4))
    o.append(_rect(168, 42, 224, 52, fill="#ffffff", sw=1.0))
    o.append(_arrow(74, 58, 148, 58, sw=1.5, color=BLUE))
    o.append(T(74, 48, "signal air (3-15 psig)", 7.8, anchor="start", color=BLUE))
    # diaphragm and plate
    o.append(_line(168, 80, 392, 80, sw=2.4, color=BLUE))
    o.append(_rect(262, 70, 36, 20, fill="#fdf3e6", sw=1.2))
    o.append(T(280, 68, "diaphragm / màng", 7.2, color=BLUE))
    # stem, spring, yoke
    o.append(_line(280, 90, 280, 300, sw=2.4, color=INK))
    o.append(T(300, 140, "valve stem", 7.4, anchor="start", color=GREY))
    o.append(T(300, 151, "thân van", 7.0, anchor="start", color=GREY))
    o.append(_spring(280, 106, 236, 30, 6))
    o.append(T(324, 168, "compression spring", 7.2, anchor="start", color=GREY))
    o.append(T(324, 179, "lò xo nén", 6.9, anchor="start", color=GREY))
    o.append(_rect(196, 100, 168, 200, fill="none", sw=1.2))
    o.append(T(280, 316, "yoke / giá đỡ", 7.2, color=GREY))
    # travel indicator
    o.append(_rect(366, 176, 26, 62, fill="#f4f7fb", sw=1.0))
    for i in range(5):
        o.append(_line(370, 186 + i * 11, 388, 186 + i * 11, sw=0.7, color=GREY))
    o.append(T(379, 168, "travel", 6.8, color=GREY))
    # valve body stub
    o.append(_rect(220, 300, 120, 56, fill="#f4f7fb", sw=1.4))
    o.append(T(280, 326, "to valve / tới van", 8.0))
    # direction of motion
    o.append(_arrow(150, 252, 150, 296, sw=1.5, color=BLUE))
    o.append(T(146, 244, "air to extend", 7.4, anchor="end", color=BLUE))
    o.append(T(146, 255, "direct acting", 7.0, anchor="end", color=GREY))
    o.append(T(280, 400,
               "Redrawn after Figure 5-1 (source p. 94): Series 127 direct-acting, "
               "air to extend.", 7.0, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 5-1: direct-acting spring-opposed diaphragm"))
    return _fig(s,
                "Hình 5-1 · Cơ cấu chấp hành màng đối lò xo, kiểu tác động trực tiếp "
                "(air-to-extend): áp suất tín hiệu ép vào mặt trên của màng, nén lò xo và "
                "đẩy thân van đi xuống; khi giảm áp, lò xo đẩy màng trở lại. Vẽ lại theo "
                "Hình 5-1 nguyên bản (tr. 94), Series 127 của Norriseal.",
                "Figure 5-1 · Spring-opposed diaphragm actuator, direct acting "
                "(air-to-extend): signal pressure acts on top of the diaphragm, "
                "compressing the spring and moving the stem downward; reducing the "
                "pressure lets the spring retract the diaphragm. Redrawn after the "
                "source Figure 5-1 (p. 94), Series 127 by Norriseal.",
                "Mặt cắt cơ cấu màng đối lò xo kiểu tác động trực tiếp",
                "Cross-section of a direct-acting spring-opposed diaphragm actuator")


@_reg
def fig_f52():
    """Figure 5-2 (source p. 95) — reverse-acting spring-opposed diaphragm."""
    w, h = 560, 430
    o = [_defs()]
    # housing; for reverse action the air is admitted below the diaphragm
    o.append(_rect(150, 30, 260, 86, fill="#eef3fb", sw=1.4))
    o.append(_rect(168, 42, 224, 62, fill="#ffffff", sw=1.0))
    o.append(_line(168, 72, 392, 72, sw=2.4, color=BLUE))
    o.append(_rect(262, 62, 36, 20, fill="#fdf3e6", sw=1.2))
    o.append(T(280, 60, "diaphragm / màng", 7.2, color=BLUE))
    # spring above the diaphragm opposes the upward air force
    o.append(_spring(280, 34, 62, 22, 3, color=GREY))
    o.append(T(324, 48, "spring", 7.0, anchor="start", color=GREY))
    o.append(_arrow(74, 96, 148, 96, sw=1.5, color=BLUE))
    o.append(T(74, 86, "air below diaphragm", 7.6, anchor="start", color=BLUE))
    # stem and yoke
    o.append(_line(280, 82, 280, 300, sw=2.4, color=INK))
    o.append(T(300, 140, "valve stem", 7.4, anchor="start", color=GREY))
    o.append(T(300, 151, "thân van", 7.0, anchor="start", color=GREY))
    o.append(_rect(196, 104, 168, 196, fill="none", sw=1.2))
    o.append(T(280, 316, "yoke / giá đỡ", 7.2, color=GREY))
    # travel indicator
    o.append(_rect(366, 176, 26, 62, fill="#f4f7fb", sw=1.0))
    for i in range(5):
        o.append(_line(370, 186 + i * 11, 388, 186 + i * 11, sw=0.7, color=GREY))
    o.append(T(379, 168, "travel", 6.8, color=GREY))
    o.append(_rect(220, 300, 120, 56, fill="#f4f7fb", sw=1.4))
    o.append(T(280, 326, "to valve / tới van", 8.0))
    # direction of motion
    o.append(_arrow(150, 256, 150, 212, sw=1.5, color=BLUE))
    o.append(T(146, 248, "air to retract", 7.4, anchor="end", color=BLUE))
    o.append(T(146, 269, "reverse acting", 7.0, anchor="end", color=GREY))
    o.append(T(280, 400,
               "Redrawn after Figure 5-2 (source p. 95): Series 137 reverse acting; "
               "the spring returns the stem when air pressure falls.", 7.0, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 5-2: reverse-acting spring-opposed diaphragm"))
    return _fig(s,
                "Hình 5-2 · Cơ cấu chấp hành màng đối lò xo, kiểu tác động ngược "
                "(air-to-retract): khí nén tác động bên dưới màng, đẩy màng và thân van "
                "đi lên; khi giảm áp, lò xo đẩy xuống. Đây là lựa chọn khi van phải "
                "đóng (fail-closed) nếu mất khí. Vẽ lại theo Hình 5-2 nguyên bản "
                "(tr. 95), Series 137 của Norriseal.",
                "Figure 5-2 · Spring-opposed diaphragm actuator, reverse acting "
                "(air-to-retract): air acts underneath the diaphragm, moving it and the "
                "stem upward; when pressure falls the spring moves them down. This is "
                "chosen when the valve should fail closed on loss of air. Redrawn after "
                "the source Figure 5-2 (p. 95), Series 137 by Norriseal.",
                "Mặt cắt cơ cấu màng đối lò xo kiểu tác động ngược",
                "Cross-section of a reverse-acting spring-opposed diaphragm actuator")


@_reg
def fig_f53():
    """Figure 5-3 (source p. 98) — piston actuator, two operating modes."""
    w, h = 680, 400
    o = [_defs()]

    def piston(cx, label, upper, arrow_up):
        p = []
        p.append(_wheel(cx, 26, 20))
        p.append(_line(cx, 46, cx, 300, sw=2.6, color=INK))
        p.append(_rect(cx - 72, 80, 144, 150, fill="#f4f7fb", sw=1.5))
        p.append(_rect(cx - 58, upper, 116, 26, fill="#fdf3e6", sw=1.4))
        p.append(_circle(cx - 58, upper + 13, 6, fill="#eef3fb", sw=1.0, color=BLUE))
        p.append(_circle(cx + 58, upper + 13, 6, fill="#eef3fb", sw=1.0, color=BLUE))
        p.append(T(cx, upper + 17, "piston / piston", 7.4, color=INK))
        p.append(_line(cx - 72, upper + 13, cx - 108, upper + 13, sw=1.4, color=BLUE))
        p.append(_line(cx + 72, upper + 13, cx + 108, upper + 13, sw=1.4, color=BLUE))
        p.append(T(cx - 112, upper + 4, "air", 6.8, anchor="end", color=BLUE))
        p.append(T(cx + 112, upper + 4, "air", 6.8, anchor="start", color=BLUE))
        p.append(_rect(cx - 46, 250, 92, 44, fill="#eaf6ee", sw=1.2))
        p.append(T(cx, 270, "positioner / bộ định vị", 6.8, color=INK))
        p.append(T(cx, 330, label, 8.2, color=INK, weight="600"))
        ay = 196
        p.append(_arrow(cx + 88, ay, cx + 88, ay - 52 if arrow_up else ay + 52,
                        sw=1.4, color=GREEN))
        return "".join(p)

    o.append(piston(170, "AIR-TO-RETRACT  (AIR-TO-OPEN)", 130, True))
    o.append(piston(510, "AIR-TO-EXTEND  (AIR-TO-CLOSE)", 170, False))
    o.append(T(340, 30, "Piston actuator — cylindrical sliding seal (O-ring)",
               9.0, color=INK, weight="600"))
    o.append(T(340, 372,
               "Redrawn after Figure 5-3 (source p. 98): Valtek piston actuators; "
               "both air-to-open and air-to-close arrangements are shown.",
               7.2, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 5-3: piston actuator in air-to-retract and air-to-extend modes"))
    return _fig(s,
                "Hình 5-3 · Cơ cấu chấp hành piston với phớt trượt dạng O-ring, hai cấu "
                "hình: air-to-retract (khí vào để thu thân van – van mở) và air-to-extend "
                "(khí vào để đẩy thân van – van đóng); bộ định vị được lắp ở dưới. Vẽ lại "
                "theo Hình 5-3 nguyên bản (tr. 98), Courtesy of Valtek.",
                "Figure 5-3 · Piston actuator with a cylindrical sliding O-ring seal, "
                "in two arrangements: air-to-retract (air opens the valve) and "
                "air-to-extend (air closes the valve), each with a positioner. Redrawn "
                "after the source Figure 5-3 (p. 98), courtesy of Valtek.",
                "Hai cấu hình cơ cấu chấp hành piston: khí vào để mở và khí vào để đóng",
                "Two piston actuator configurations: air-to-open and air-to-close")


@_reg
def fig_f54():
    """Figure 5-4 (source p. 102) — top- and side-mounted manual overrides."""
    w, h = 680, 420
    o = [_defs()]

    def body(cx):
        p = []
        p.append(_rect(cx - 78, 96, 156, 60, fill="#eef3fb", sw=1.4))
        p.append(_line(cx - 62, 132, cx + 62, 132, sw=2.2, color=BLUE))
        p.append(T(cx, 112, "diaphragm case / vỏ màng", 7.0, color=GREY))
        p.append(_rect(cx - 50, 156, 100, 150, fill="none", sw=1.2))
        p.append(_line(cx, 132, cx, 322, sw=2.4, color=INK))
        p.append(_spring(cx, 160, 226, 26, 5))
        p.append(_rect(cx - 46, 306, 92, 44, fill="#f4f7fb", sw=1.4))
        return "".join(p)

    # side-mounted handwheel
    o.append(body(170))
    o.append(_rect(246, 196, 54, 40, fill="#fdf3e6", sw=1.2))
    o.append(T(273, 190, "gear box", 6.8, color=GREY))
    o.append(_line(246, 216, 214, 216, sw=1.6, color=INK))
    o.append(_wheel(336, 216, 32))
    o.append(T(336, 276, "handwheel", 7.0, color=GREY))
    o.append(T(170, 372, "ACTUATOR WITH SIDE-MOUNTED HANDWHEEL", 8.0,
               color=INK, weight="600"))
    # top-mounted handwheel
    o.append(body(510))
    o.append(_line(510, 96, 510, 72, sw=2.0, color=INK))
    o.append(_wheel(510, 48, 34))
    o.append(T(510, 10, "top-mounted override", 7.4, color=GREY))
    o.append(T(510, 372, "ACTUATOR WITH TOP-MOUNTED HANDWHEEL", 8.0,
               color=INK, weight="600"))
    o.append(T(340, 30, "Manual overrides / tay quay dự phòng", 9.0,
               color=INK, weight="600"))
    o.append(T(340, 402,
               "Redrawn after Figure 5-4 (source p. 102): manual overrides by "
               "Norriseal — side-mounted and top-mounted.", 7.0, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 5-4: top- and side-mounted manual overrides"))
    return _fig(s,
                "Hình 5-4 · Bộ truyền động tay (tay quay dự phòng) lắp bên hông (trái) và "
                "lắp trên đỉnh (phải) của cơ cấu màng. Bên hông thường dùng cho piston và "
                "một số cơ cấu màng; trên đỉnh dùng cho cơ cấu màng, ép hoặc kéo theo chiều "
                "áp suất khí. Vẽ lại theo Hình 5-4 nguyên bản (tr. 102), Courtesy of Norriseal.",
                "Figure 5-4 · Manual overrides mounted at the side (left) and on top "
                "(right) of a spring-diaphragm actuator. Side mounting is used for pistons "
                "and some diaphragm actuators; top mounting pushes or pulls in the "
                "direction of the applied air pressure. Redrawn after the source "
                "Figure 5-4 (p. 102), courtesy of Norriseal.",
                "Tay quay dự phòng lắp bên hông và lắp trên đỉnh cơ cấu chấp hành",
                "Side-mounted and top-mounted manual handwheel overrides")
