# -*- coding: utf-8 -*-
"""Vector figures for Chapter 7 "Steam Conditioning" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 162-175.

Fourteen simplified but faithful figures ``fig_f7_01`` ... ``fig_f7_14``.
Every function is registered with :func:`_reg` and returns the standard
5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through
:func:`_finish`. All text is XML-escaped with :func:`T` / :func:`esc`.

Source quirk: in the text dump the caption for Figure 7.8 precedes that of
Figure 7.7 on printed p. 168, and Figure 7.9 carries a leading space and sits
adrift among the labels of 7.8. The functions here are numbered and placed
in logical order (7.7, then 7.8, then 7.9); see ``source_notes`` in the prose
module.
"""
import math

from cvh6fig import (_reg, _finish, _leader, _labels, _c4_labels, esc, T,
                     _defs, _rect, _line, _circle, _ellipse, _poly, _path,
                     _arrow, _spring, _num, svg, _legend, _curve,
                     INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not re-exported by `cvh6fig`.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# small local helpers
# ---------------------------------------------------------------------------
def _pipe_h(o, x0, x1, y, ht=44, arrows=3):
    """A horizontal pipe section with flow arrows."""
    o.append(_rect(x0, y, x1 - x0, ht, fill="#eef3fb", sw=1.5))
    o.append(_line(x0, y, x1, y, sw=1.7, color=INK))
    o.append(_line(x0, y + ht, x1, y + ht, sw=1.7, color=INK))
    for i in range(arrows):
        ax = x0 + (i + 0.5) * (x1 - x0) / arrows
        o.append(_arrow(ax - 13, y + ht / 2.0, ax + 13, y + ht / 2.0,
                        sw=1.2, color=GREEN))


def _pipe_v(o, x, y0, y1, wd=36, arrows=2, up=True):
    """A vertical pipe section with flow arrows."""
    o.append(_rect(x, y0, wd, y1 - y0, fill="#eef3fb", sw=1.5))
    o.append(_line(x, y0, x, y1, sw=1.7, color=INK))
    o.append(_line(x + wd, y0, x + wd, y1, sw=1.7, color=INK))
    for i in range(arrows):
        ay = y0 + (i + 0.5) * (y1 - y0) / arrows
        if up:
            o.append(_arrow(x + wd / 2.0, ay + 12, x + wd / 2.0, ay - 12,
                            sw=1.2, color=GREEN))
        else:
            o.append(_arrow(x + wd / 2.0, ay - 12, x + wd / 2.0, ay + 12,
                            sw=1.2, color=GREEN))


def _bub(o, cx, cy, tag, r=11):
    """An instrument bubble (TC, TE, SV, LS ...)."""
    o.append(_circle(cx, cy, r, fill="#ffffff", sw=1.3, color=INK))
    o.append(T(cx, cy + 3, tag, 7.4, weight="600"))


def _valve(o, cx, cy, sc=10):
    """A bow-tie control-valve symbol."""
    o.append(_poly([(cx - sc, cy - sc), (cx + sc, cy), (cx - sc, cy + sc)],
                   fill=GOLD, sw=1.2, close=True))
    o.append(_poly([(cx + sc, cy - sc), (cx - sc, cy), (cx + sc, cy + sc)],
                   fill=GOLD, sw=1.2, close=True))


def _hspring(o, x0, x1, y, width=24, turns=5, color=GREY):
    """A horizontal zigzag spring."""
    pts = [(x0, y)]
    n = turns * 2
    for i in range(1, n):
        pts.append((x0 + (x1 - x0) * i / float(n),
                    y + (width / 2.0 if i % 2 else -width / 2.0)))
    pts.append((x1, y))
    o.append(_poly(pts, sw=1.2, color=color))


def _droplets(o, x, y, nx=5, spread=44, length=30, color=BLUE):
    """A fan of spray droplets / arrows."""
    for i in range(nx):
        dx = x + (i - (nx - 1) / 2.0) * (spread / max(nx - 1, 1))
        o.append(_arrow(dx, y, dx + (dx - x) * 0.22, y + length,
                        sw=1.0, color=color))


# ---------------------------------------------------------------------------
# Figure 7.1 - Typical insertion-style desuperheater and control loop
# ---------------------------------------------------------------------------
@_reg
def fig_f7_01():
    """Figure 7.1 (p. 163) - Insertion-style desuperheater installation."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Lắp đặt thiết bị giảm nhiệt dạng chèn và vòng điều khiển nhiệt độ / "
               "Insertion-Style Desuperheater and Temperature Control Loop", 8.6, weight="600"))
    # steam line
    _pipe_h(o, 60, 620, 250, 44, arrows=4)
    o.append(T(70, 242, "Hơi / Steam", 7.6, anchor="start"))
    # spraywater supply and control valve
    o.append(_line(60, 160, 300, 160, sw=1.8, color=BLUE))
    o.append(_arrow(95, 160, 140, 160, sw=1.4, color=BLUE))
    o.append(T(62, 150, "Nước phun / Spraywater", 7.4, anchor="start"))
    _valve(o, 170, 160)
    # branch tee and insertion unit
    o.append(_rect(292, 170, 16, 80, fill="#eef3fb", sw=1.4))
    o.append(_rect(284, 166, 32, 8, fill="#e9eef4", sw=1.3))
    o.append(_line(300, 174, 300, 278, sw=2.8, color=INK))
    _droplets(o, 300, 278, nx=5, spread=40, length=16)
    # TE sensor and TC controller
    o.append(_line(520, 250, 520, 242, sw=1.6, color=INK))
    _bub(o, 520, 232, "TE")
    _bub(o, 520, 90, "TC", r=12)
    o.append(_line(520, 221, 520, 102, sw=1.0, dash="4 3", color=GREY))
    o.append(_line(508, 90, 170, 90, sw=1.0, dash="4 3", color=BLUE))
    o.append(_line(170, 90, 170, 150, sw=1.0, dash="4 3", color=BLUE))
    # numbered callouts
    for cx, cy, n in [(170, 132, 1), (300, 206, 2), (105, 272, 3),
                      (546, 232, 4), (546, 90, 5)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Van điều khiển nước phun / Spraywater control valve",
        "Thiết bị giảm nhiệt dạng chèn / Insertion-style desuperheater",
        "Dòng hơi / Steam flow",
        "Cảm biến nhiệt độ / Temperature sensor (TE)",
        "Bộ điều khiển nhiệt độ / Temperature controller (TC)",
    ], 60, 330, lh=19))
    return _finish(w, h, o,
                   "Figure 7.1 (p. 163) - Insertion-style desuperheater and control loop",
                   "Hình 7.1 (tr. 163) · Thiết bị giảm nhiệt dạng chèn và vòng điều khiển nhiệt độ",
                   "Hình 7.1 (tr. 163) · Sơ đồ lắp đặt thiết bị giảm nhiệt dạng chèn vào đường ống "
                   "hơi: van điều khiển định lượng nước phun, cảm biến TE đo nhiệt độ phía sau và "
                   "bộ điều khiển TC đóng vòng điều khiển.",
                   "Figure 7.1 (p. 163) · Schematic of an insertion-style desuperheater installed in "
                   "a steam line: a control valve meters the spraywater, a downstream TE element "
                   "senses temperature, and a TC controller closes the temperature loop.",
                   "Sơ đồ Hình 7.1 (tr. 163) thiết bị giảm nhiệt dạng chèn và vòng điều khiển nhiệt độ",
                   "Schematic of Figure 7.1 (p. 163) insertion desuperheater and temperature loop")


# ---------------------------------------------------------------------------
# Figure 7.2 - Desuperheating installations
# ---------------------------------------------------------------------------
@_reg
def fig_f7_02():
    """Figure 7.2 (p. 164) - Variations in desuperheater installation."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Các biến thể lắp đặt thiết bị giảm nhiệt / Desuperheating Installations",
               9.0, weight="600"))
    # A: vertical upflow (optimum)
    _pipe_v(o, 70, 80, 190, 36, arrows=2, up=True)
    o.append(_line(50, 170, 70, 170, sw=1.8, color=BLUE))
    o.append(_arrow(54, 170, 68, 170, sw=1.2, color=BLUE))
    o.append(T(126, 92, "Thẳng đứng, chảy lên / Vertical, flow up", 7.2, anchor="start"))
    o.append(T(126, 108, "Tối ưu / Optimum", 7.2, anchor="start", color=GREEN))
    # B: horizontal with close elbow
    _pipe_h(o, 400, 620, 100, 40, arrows=2)
    o.append(_rect(560, 140, 40, 52, fill="#eef3fb", sw=1.4))
    o.append(_line(560, 140, 600, 140, sw=1.6, color=INK))
    o.append(_line(430, 92, 430, 100, sw=2.0, color=BLUE))
    o.append(T(400, 84, "Cút ngay sau điểm phun / Elbow right after injection",
               7.2, anchor="start"))
    o.append(T(400, 212, "Nhiễu loạn và va đập giọt nước / Turbulence and droplet impingement",
               7.0, anchor="start", color=GREY))
    # C: vertical downflow
    _pipe_v(o, 70, 240, 350, 36, arrows=2, up=False)
    o.append(_line(50, 266, 70, 266, sw=1.8, color=BLUE))
    o.append(T(126, 252, "Thẳng đứng, chảy xuống / Vertical, flow down", 7.2, anchor="start"))
    o.append(T(126, 268, "Giọt nước dễ rơi ra / Droplets may fall out", 7.0, anchor="start",
               color=GREY))
    # D: horizontal with close tee
    _pipe_h(o, 400, 620, 270, 40, arrows=2)
    o.append(_rect(552, 228, 40, 42, fill="#eef3fb", sw=1.4))
    o.append(_line(430, 262, 430, 270, sw=2.0, color=BLUE))
    o.append(T(400, 254, "Tê gần điểm phun / Tee near injection", 7.2, anchor="start"))
    o.append(T(340, 378,
               "Hầu như mọi hướng đều hoạt động nếu mọi thông số được đưa đúng vào thiết kế / "
               "Almost any orientation works when all parameters are designed in",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 7.2 (p. 164) - Desuperheating installations",
                   "Hình 7.2 (tr. 164) · Các biến thể lắp đặt thiết bị giảm nhiệt",
                   "Hình 7.2 (tr. 164) · Bốn cách lắp đặt thiết bị giảm nhiệt: ống thẳng đứng "
                   "chảy lên (tối ưu), chảy xuống, và đường ống ngang có cút hoặc tê ngay phía "
                   "sau điểm phun nước.",
                   "Figure 7.2 (p. 164) · Four desuperheater installations: vertical upflow "
                   "(optimum), vertical downflow, and horizontal runs with an elbow or a tee just "
                   "downstream of the water injection point.",
                   "Sơ đồ Hình 7.2 (tr. 164) các biến thể lắp đặt thiết bị giảm nhiệt",
                   "Schematic of Figure 7.2 (p. 164) desuperheating installation variants")


# ---------------------------------------------------------------------------
# Figure 7.3 - Desuperheater spray penetration
# ---------------------------------------------------------------------------
@_reg
def fig_f7_03():
    """Figure 7.3 (p. 165) - Spray penetration and thermal stratification."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Độ xuyên thấu của tia phun / Desuperheater Spray Penetration",
               9.0, weight="600"))
    # left: single point, poor coverage
    o.append(_ellipse(180, 200, 110, 84, fill="#eef3fb", sw=1.8, color=INK))
    o.append(_ellipse(180, 205, 42, 58, fill="#dbe9f6", sw=1.2, color=BLUE))
    o.append(_poly([(152, 92), (208, 92), (194, 146), (166, 146)],
                   fill=FILL, sw=1.3, close=True))
    o.append(_arrow(180, 100, 180, 168, sw=1.6, color=BLUE))
    o.append(T(180, 74, "Phun điểm đơn / Single-point", 8.0, weight="600"))
    o.append(T(180, 306, "Lõi lạnh bị hơi quá nhiệt bao bọc / Cool core shrouded by "
               "superheated steam", 7.0, color=GREY))
    # right: multi-nozzle, full coverage
    o.append(_ellipse(500, 200, 110, 84, fill="#eef3fb", sw=1.8, color=INK))
    o.append(_circle(500, 200, 52, fill="#e4f0e8", sw=1.1, color=GREEN))
    for ang in (0, 90, 180, 270):
        r = math.radians(ang)
        sx = 500 + 100 * math.cos(r)
        sy = 200 + 78 * math.sin(r)
        ex = 500 + 38 * math.cos(r)
        ey = 200 + 30 * math.sin(r)
        o.append(_arrow(sx, sy, ex, ey, sw=1.3, color=BLUE))
    for i in range(24):
        a = i * 0.52
        rr = 16 + (i % 4) * 11
        o.append(_circle(500 + rr * math.cos(a), 200 + rr * 0.75 * math.sin(a),
                         1.6, fill=GREEN, sw=0))
    o.append(T(500, 74, "Nhiều vòi năng lượng cao / Multi-nozzle high-energy",
               8.0, weight="600"))
    o.append(T(500, 306, "Phân bố đều, không phân tầng / Even distribution, no stratification",
               7.0, color=GREY))
    for cx, cy, n in [(180, 128, 1), (180, 205, 2), (500, 140, 3), (500, 200, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Vòi phun đơn / Single nozzle",
        "Phân tầng nhiệt / Thermal stratification",
        "Các vòi phun quanh chu vi / Circumferential nozzles",
        "Trộn lẫn đồng đều / Uniform mixing",
    ], 60, 336, lh=18))
    return _finish(w, h, o,
                   "Figure 7.3 (p. 165) - Desuperheater spray penetration",
                   "Hình 7.3 (tr. 165) · Độ xuyên thấu của tia phun",
                   "Hình 7.3 (tr. 165) · So sánh mặt cắt đường ống: vòi phun điểm đơn tạo lõi "
                   "lạnh bị bao bởi hơi quá nhiệt và gây phân tầng nhiệt, trong khi nhiều vòi năng "
                   "lượng cao phân bố nước khắp mặt cắt.",
                   "Figure 7.3 (p. 165) · Pipe cross-sections comparing a single nozzle, which "
                   "leaves a subcooled core shrouded by superheated steam and causes thermal "
                   "stratification, with high-energy multi-nozzle units that distribute water "
                   "across the whole section.",
                   "Sơ đồ Hình 7.3 (tr. 165) độ xuyên thấu của tia phun và phân tầng nhiệt",
                   "Schematic of Figure 7.3 (p. 165) spray penetration and stratification")


# ---------------------------------------------------------------------------
# Figure 7.4 - Fixed-geometry nozzle design
# ---------------------------------------------------------------------------
@_reg
def fig_f7_04():
    """Figure 7.4 (p. 167) - Fixed-geometry nozzle desuperheater."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Thiết kế vòi phun hình học cố định / Fixed-Geometry Nozzle Design",
               9.0, weight="600"))
    _pipe_h(o, 60, 620, 230, 50, arrows=3)
    o.append(_line(60, 170, 300, 170, sw=1.8, color=BLUE))
    o.append(_arrow(100, 170, 142, 170, sw=1.3, color=BLUE))
    _valve(o, 170, 170)
    o.append(T(62, 160, "Nước phun / Spraywater", 7.4, anchor="start"))
    o.append(_rect(292, 170, 16, 60, fill="#eef3fb", sw=1.4))
    o.append(_rect(284, 166, 32, 8, fill="#e9eef4", sw=1.3))
    o.append(_line(300, 178, 300, 262, sw=2.6, color=INK))
    o.append(_circle(300, 258, 7, fill=GOLD, sw=1.1))
    _droplets(o, 300, 264, nx=5, spread=44, length=18)
    o.append(_line(520, 230, 520, 222, sw=1.5, color=INK))
    _bub(o, 520, 212, "TE")
    o.append(T(330, 196, "Vòi cố định / Fixed nozzles", 7.2, anchor="start"))
    o.append(T(340, 306, "Phạm vi điều chỉnh đến 5:1 · vận tốc 25–30 ft/s · NPS 6 (DN 150) trở lên / "
               "Rangeability up to 5:1 · 25-30 ft/s · NPS 6 (DN 150) and larger",
               7.0, color=GREY))
    for cx, cy, n in [(170, 142, 1), (300, 210, 2), (300, 276, 3), (520, 192, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Van nước bên ngoài / External water valve",
        "Đầu nối bích / Flanged branch tee",
        "Vòi phun hình học cố định / Fixed-geometry nozzles",
        "Cảm biến nhiệt độ phía sau / Downstream temperature sensor",
    ], 60, 340, lh=20))
    return _finish(w, h, o,
                   "Figure 7.4 (p. 167) - Fixed-geometry nozzle design",
                   "Hình 7.4 (tr. 167) · Thiết kế vòi phun hình học cố định",
                   "Hình 7.4 (tr. 167) · Thiết bị giảm nhiệt phun sương cơ khí có một hoặc nhiều "
                   "vòi phun hình học cố định, lắp qua cút nhánh nối bích và cần van nước bên "
                   "ngoài; phù hợp thay đổi tải gần như không đổi.",
                   "Figure 7.4 (p. 167) · A mechanically atomized desuperheater with one or more "
                   "fixed-geometry spray nozzles, mounted through a flanged branch tee and fed by "
                   "an external water valve; suited to nearly constant load changes.",
                   "Sơ đồ Hình 7.4 (tr. 167) thiết kế vòi phun hình học cố định",
                   "Schematic of Figure 7.4 (p. 167) fixed-geometry nozzle design")


# ---------------------------------------------------------------------------
# Figure 7.5 - Variable-geometry nozzle design
# ---------------------------------------------------------------------------
@_reg
def fig_f7_05():
    """Figure 7.5 (p. 167) - Variable-geometry nozzle desuperheater."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Thiết kế vòi phun hình học thay đổi / Variable-Geometry Nozzle Design",
               9.0, weight="600"))
    _pipe_h(o, 60, 620, 230, 50, arrows=3)
    o.append(_line(60, 170, 300, 170, sw=1.8, color=BLUE))
    o.append(_arrow(100, 170, 142, 170, sw=1.3, color=BLUE))
    _valve(o, 170, 170)
    o.append(T(62, 160, "Nước phun / Spraywater", 7.4, anchor="start"))
    o.append(_rect(288, 170, 24, 60, fill="#eef3fb", sw=1.4))
    o.append(_rect(280, 166, 40, 8, fill="#e9eef4", sw=1.3))
    # variable nozzle detail: spring-loaded moving plug
    o.append(_spring(300, 180, 232, width=20, turns=4))
    o.append(_poly([(292, 232), (308, 232), (304, 246), (296, 246)],
                   fill=GOLD, sw=1.2, close=True))
    _droplets(o, 300, 250, nx=5, spread=48, length=18)
    o.append(_line(520, 230, 520, 222, sw=1.5, color=INK))
    _bub(o, 520, 212, "TE")
    o.append(_leader(316, 204, 366, 194))
    o.append(T(372, 198, "Kích hoạt bằng áp suất ngược / Backpressure activated",
               7.2, anchor="start"))
    o.append(T(340, 306, "Phạm vi điều chỉnh đến 20:1 · vận tốc 25–30 ft/s · NPS 8 (DN 200) trở lên / "
               "Rangeability up to 20:1 · 25-30 ft/s · NPS 8 (DN 200) and larger",
               7.0, color=GREY))
    for cx, cy, n in [(170, 142, 1), (300, 210, 2), (300, 260, 3), (520, 192, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Van nước bên ngoài / External water valve",
        "Vòi hình học thay đổi có lò xo / Spring-loaded variable nozzle",
        "Tia phun / Spray pattern",
        "Cảm biến nhiệt độ phía sau / Downstream temperature sensor",
    ], 60, 340, lh=20))
    return _finish(w, h, o,
                   "Figure 7.5 (p. 167) - Variable-geometry nozzle design",
                   "Hình 7.5 (tr. 167) · Thiết kế vòi phun hình học thay đổi",
                   "Hình 7.5 (tr. 167) · Thiết bị phun sương cơ khí dùng vòi phun hình học thay "
                   "đổi, kích hoạt bằng áp suất ngược, cho phép điều khiển thay đổi tải vừa phải "
                   "đến 20:1.",
                   "Figure 7.5 (p. 167) · A mechanically atomized unit using variable-geometry, "
                   "backpressure-activated spray nozzles, allowing control over moderate load "
                   "changes up to 20:1.",
                   "Sơ đồ Hình 7.5 (tr. 167) thiết kế vòi phun hình học thay đổi",
                   "Schematic of Figure 7.5 (p. 167) variable-geometry nozzle design")


# ---------------------------------------------------------------------------
# Figure 7.6 - Self-contained design
# ---------------------------------------------------------------------------
@_reg
def fig_f7_06():
    """Figure 7.6 (p. 168) - Self-contained desuperheater design."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Thiết kế tích hợp / Self-Contained Design",
               9.0, weight="600"))
    _pipe_h(o, 60, 620, 250, 50, arrows=3)
    # packaged unit: control element + desuperheater in one housing
    o.append(_rect(248, 132, 116, 118, fill="#f4f7fb", sw=1.8))
    o.append(T(306, 148, "Cụm tích hợp / Packaged unit", 7.4))
    o.append(_rect(268, 158, 76, 42, fill="#e9eef4", sw=1.3))
    _valve(o, 306, 179, sc=9)
    o.append(T(306, 214, "Phần tử điều khiển nước / Water control element", 6.8, color=GREY))
    o.append(_line(306, 200, 306, 236, sw=2.4, color=INK))
    o.append(_rect(270, 116, 72, 16, fill="#eef3fb", sw=1.4))
    _droplets(o, 306, 254, nx=5, spread=46, length=16)
    o.append(_line(520, 250, 520, 242, sw=1.5, color=INK))
    _bub(o, 520, 232, "TE")
    o.append(T(340, 322, "Gộp van nước và thiết bị giảm nhiệt vào một cụm · phạm vi điều chỉnh "
               "đến 25:1 / Combines water valve and desuperheater · rangeability up to 25:1",
               7.0, color=GREY))
    for cx, cy, n in [(306, 179, 1), (306, 232, 2), (306, 124, 3), (520, 212, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Phần tử điều khiển lưu lượng nước / Water flow control element",
        "Vòi hình học thay đổi / Variable-geometry nozzle(s)",
        "Cơ cấu chấp hành tích hợp / Integrated actuator",
        "Cảm biến nhiệt độ phía sau / Downstream temperature sensor",
    ], 60, 352, lh=20))
    return _finish(w, h, o,
                   "Figure 7.6 (p. 168) - Self-contained design",
                   "Hình 7.6 (tr. 168) · Thiết kế tích hợp",
                   "Hình 7.6 (tr. 168) · Van điều khiển nước và thiết bị giảm nhiệt được đóng "
                   "gói trong một cụm duy nhất, phối hợp chặt chẽ với vòi phun hình học thay đổi "
                   "để xử lý thay đổi tải từ vừa đến cao.",
                   "Figure 7.6 (p. 168) · The water control valve and desuperheater are packaged "
                   "in a single unit, closely coordinated with variable-geometry nozzles to handle "
                   "moderate to high load changes.",
                   "Sơ đồ Hình 7.6 (tr. 168) thiết kế giảm nhiệt tích hợp",
                   "Schematic of Figure 7.6 (p. 168) self-contained design")


# ---------------------------------------------------------------------------
# Figure 7.7 - Steam-atomized design
# ---------------------------------------------------------------------------
@_reg
def fig_f7_07():
    """Figure 7.7 (p. 168) - Steam-atomized desuperheater design."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28,
               "Thiết kế phun sương bằng hơi / Steam-Atomized Design",
               9.0, weight="600"))
    _pipe_h(o, 60, 620, 260, 50, arrows=3)
    # spraywater in from the left
    o.append(_line(70, 190, 320, 190, sw=1.8, color=BLUE))
    o.append(_arrow(110, 190, 152, 190, sw=1.3, color=BLUE))
    o.append(T(72, 180, "Nước phun / Spraywater", 7.4, anchor="start"))
    # atomizing steam in from the top right
    o.append(_line(470, 110, 360, 110, sw=1.8, color=RED))
    o.append(_line(360, 110, 360, 172, sw=1.8, color=RED))
    o.append(_arrow(450, 110, 405, 110, sw=1.3, color=RED))
    o.append(T(474, 102, "Hơi phun sương / Atomizing steam", 7.4, anchor="start"))
    o.append(T(474, 118, "khoảng 2× áp suất hơi chính / about 2x main steam pressure",
               6.8, anchor="start", color=GREY))
    # nozzle chamber
    o.append(_rect(312, 172, 96, 88, fill="#f4f7fb", sw=1.8))
    o.append(T(360, 188, "Buồng vòi / Chamber", 6.8))
    _droplets(o, 360, 260, nx=7, spread=56, length=20, color=GREEN)
    o.append(T(340, 326, "Giọt rất mịn bay hơi nhanh · vận tốc hơi tới ~10 ft/s · phạm vi đến 50:1 / "
               "Very fine droplets vaporize fast · steam velocity down to ~10 ft/s · "
               "rangeability up to 50:1", 7.0, color=GREY))
    for cx, cy, n in [(360, 200, 1), (360, 110, 2), (360, 248, 3)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Nước phun / Spraywater",
        "Hơi phun sương áp suất cao / High-pressure atomizing steam",
        "Buồng vòi phun / Spray nozzle chamber",
        "Giọt mịn phân tán trong dòng hơi / Fine droplets in steam flow",
    ], 60, 356, lh=20))
    return _finish(w, h, o,
                   "Figure 7.7 (p. 168) - Steam-atomized design",
                   "Hình 7.7 (tr. 168) · Thiết kế phun sương bằng hơi",
                   "Hình 7.7 (tr. 168) · Hơi áp suất cao gặp nước trong buồng vòi phun và biến "
                   "nước thành giọt rất mịn, cho phép bay hơi hoàn toàn ngay ở vận tốc hơi thấp.",
                   "Figure 7.7 (p. 168) · High-pressure steam meets water in the nozzle chamber "
                   "and breaks it into very fine droplets, allowing complete vaporization even at "
                   "low steam velocity.",
                   "Sơ đồ Hình 7.7 (tr. 168) thiết kế phun sương bằng hơi",
                   "Schematic of Figure 7.7 (p. 168) steam-atomized design")


# ---------------------------------------------------------------------------
# Figure 7.8 - Control loop with steam-assisted desuperheater
# ---------------------------------------------------------------------------
@_reg
def fig_f7_08():
    """Figure 7.8 (p. 168) - Control loop, steam-assisted desuperheater."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Vòng điều khiển với thiết bị giảm nhiệt hỗ trợ bằng hơi / "
               "Control Loop with Steam-Assisted Desuperheater", 8.4, weight="600"))
    _pipe_h(o, 60, 620, 300, 44, arrows=3)
    o.append(T(72, 292, "Hơi / Steam", 7.4, anchor="start"))
    # desuperheater body
    o.append(_rect(326, 244, 32, 56, fill="#eef3fb", sw=1.5))
    o.append(T(250, 232, "Thiết bị giảm nhiệt / Desuperheater", 7.0, anchor="end"))
    # spraywater branch with control valve
    o.append(_line(110, 160, 342, 160, sw=1.8, color=BLUE))
    o.append(_line(342, 160, 342, 244, sw=1.8, color=BLUE))
    o.append(_arrow(140, 160, 184, 160, sw=1.3, color=BLUE))
    _valve(o, 220, 160)
    o.append(T(112, 150, "Nước phun / Spraywater", 7.4, anchor="start"))
    # atomizing steam branch with isolation valve SV and limit switch LS
    o.append(_line(560, 110, 366, 110, sw=1.8, color=RED))
    o.append(_line(366, 110, 366, 244, sw=1.8, color=RED))
    o.append(_arrow(540, 110, 500, 110, sw=1.3, color=RED))
    _valve(o, 470, 110, sc=9)
    _bub(o, 470, 74, "SV", r=10)
    _bub(o, 520, 74, "LS", r=10)
    o.append(T(566, 102, "Hơi phun sương / Atomized steam", 7.2, anchor="start"))
    # temperature controller and sensor
    _bub(o, 220, 74, "TC", r=12)
    o.append(_line(560, 300, 560, 288, sw=1.5, color=INK))
    _bub(o, 560, 278, "TE")
    o.append(_line(548, 278, 232, 278, sw=1.0, dash="4 3", color=GREY))
    o.append(_line(220, 266, 220, 86, sw=1.0, dash="4 3", color=GREY))
    o.append(_line(232, 74, 470, 74, sw=1.0, dash="4 3", color=BLUE))
    o.append(_line(470, 86, 470, 100, sw=1.0, dash="4 3", color=BLUE))
    o.append(_line(220, 86, 220, 150, sw=1.0, dash="4 3", color=BLUE))
    for cx, cy, n in [(220, 132, 1), (470, 132, 2), (342, 266, 3), (560, 254, 4), (220, 60, 5)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Van điều khiển nước phun / Spraywater control valve",
        "Van cô lập hơi phun sương SV / Steam isolation valve SV",
        "Thiết bị giảm nhiệt / Desuperheater",
        "Cảm biến nhiệt độ TE / Temperature sensor TE",
        "Bộ điều khiển TC / Temperature controller TC",
    ], 60, 372, lh=16, size=7.0))
    return _finish(w, h, o,
                   "Figure 7.8 (p. 168) - Control loop with steam-assisted desuperheater",
                   "Hình 7.8 (tr. 168) · Vòng điều khiển với thiết bị giảm nhiệt hỗ trợ bằng hơi",
                   "Hình 7.8 (tr. 168) · Vòng điều khiển nhiệt độ dùng bộ điều khiển TC và cảm "
                   "biến TE để điều chỉnh van nước phun, trong khi van cô lập SV cấp hơi phun "
                   "sương cho thiết bị giảm nhiệt.",
                   "Figure 7.8 (p. 168) · The temperature loop uses a TC controller and TE sensor "
                   "to adjust the spraywater valve, while isolation valve SV supplies atomizing "
                   "steam to the desuperheater.",
                   "Sơ đồ Hình 7.8 (tr. 168) vòng điều khiển thiết bị giảm nhiệt hỗ trợ bằng hơi",
                   "Schematic of Figure 7.8 (p. 168) steam-assisted desuperheater control loop")


# ---------------------------------------------------------------------------
# Figure 7.9 - Geometry-assisted wafer design
# ---------------------------------------------------------------------------
@_reg
def fig_f7_09():
    """Figure 7.9 (p. 168) - Geometry-assisted wafer desuperheater."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Thiết kế wafer hỗ trợ bằng hình học / Geometry-Assisted Wafer Design",
               9.0, weight="600"))
    # steam pipe with two flanges
    o.append(_line(60, 170, 210, 170, sw=1.8, color=INK))
    o.append(_line(60, 270, 210, 270, sw=1.8, color=INK))
    o.append(_line(470, 170, 620, 170, sw=1.8, color=INK))
    o.append(_line(470, 270, 620, 270, sw=1.8, color=INK))
    o.append(_rect(196, 160, 14, 120, fill="#e9eef4", sw=1.4))
    o.append(_rect(470, 160, 14, 120, fill="#e9eef4", sw=1.4))
    # wafer: venturi converging then diverging
    o.append(_poly([(210, 170), (300, 170), (340, 208), (380, 170), (470, 170),
                    (470, 190), (384, 190), (340, 216), (296, 190), (210, 190)],
                   fill="#eef3fb", sw=1.5, close=True))
    o.append(_poly([(210, 270), (300, 270), (340, 232), (380, 270), (470, 270),
                    (470, 250), (384, 250), (340, 224), (296, 250), (210, 250)],
                   fill="#eef3fb", sw=1.5, close=True))
    # drilled holes around the wafer and inward sprays
    for hx in (250, 280, 400, 430):
        o.append(_circle(hx, 180, 2.6, fill=BLUE, sw=0))
        o.append(_circle(hx, 260, 2.6, fill=BLUE, sw=0))
    o.append(_arrow(250, 182, 258, 200, sw=1.0, color=BLUE))
    o.append(_arrow(430, 258, 422, 240, sw=1.0, color=BLUE))
    o.append(_arrow(120, 220, 180, 220, sw=1.3, color=GREEN))
    o.append(_arrow(480, 220, 560, 220, sw=1.3, color=GREEN))
    o.append(T(340, 130, "Cổ hẹp venturi tăng vận tốc tại điểm phun / "
               "Venturi throat raises velocity at injection", 7.2))
    o.append(T(340, 306, "Wafer giữa hai bích · lỗ khoan hoặc vòi nhỏ · NPS 1–24 · phạm vi đến 20:1 / "
               "Wafer between flanges · drilled holes or small nozzles · NPS 1-24 · "
               "rangeability up to 20:1", 7.0, color=GREY))
    for cx, cy, n in [(340, 220, 1), (270, 180, 2), (540, 220, 3)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Cổ hẹp venturi / Venturi throat",
        "Lỗ khoan phun nước / Drilled spray holes",
        "Dòng hơi tăng tốc / Accelerated steam flow",
    ], 60, 340, lh=20))
    return _finish(w, h, o,
                   "Figure 7.9 (p. 168) - Geometry-assisted wafer design",
                   "Hình 7.9 (tr. 168) · Thiết kế wafer hỗ trợ bằng hình học",
                   "Hình 7.9 (tr. 168) · Wafer lắp giữa hai bích có cổ hẹp venturi làm tăng vận "
                   "tốc hơi tại điểm phun, giúp phun nước qua nhiều lỗ khoan hoặc vòi nhỏ để trộn "
                   "đều trong đường ống nhỏ.",
                   "Figure 7.9 (p. 168) · A wafer installed between flanges uses a venturi throat "
                   "to raise steam velocity at injection, so water sprays through multiple drilled "
                   "holes or small nozzles for good mixing in small lines.",
                   "Sơ đồ Hình 7.9 (tr. 168) thiết kế wafer hỗ trợ bằng hình học",
                   "Schematic of Figure 7.9 (p. 168) geometry-assisted wafer design")


# ---------------------------------------------------------------------------
# Figure 7.10 - Cross-section of steam conditioning valve
# ---------------------------------------------------------------------------
@_reg
def fig_f7_10():
    """Figure 7.10 (p. 170) - Cross-section of a steam conditioning valve."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Mặt cắt van điều hòa hơi / Cross-Section View of Steam Conditioning Valve",
               9.0, weight="600"))
    # actuator and stem
    o.append(_rect(285, 70, 110, 60, fill="#f4f7fb", sw=1.6))
    o.append(_spring(340, 76, 124, width=34, turns=5))
    o.append(_line(340, 130, 340, 226, sw=3.0, color=INK))
    # forged body
    o.append(_rect(190, 170, 300, 170, fill="#eef3fb", sw=1.9))
    # inlet from below (flow-up)
    o.append(_rect(320, 340, 60, 56, fill="#e9eef4", sw=1.5))
    o.append(_rect(312, 388, 76, 10, fill="#e9eef4", sw=1.4))
    o.append(_arrow(350, 380, 350, 320, sw=1.4, color=GREEN))
    # cage with holes
    o.append(_rect(240, 210, 200, 110, fill="#ffffff", sw=1.4, stroke=BLUE))
    for gx in range(252, 432, 18):
        for gy in (224, 306):
            o.append(_circle(gx, gy, 2.2, fill="#ffffff", sw=0.8, color=GREY))
    # plug and seat
    o.append(_poly([(322, 252), (358, 252), (350, 218), (330, 218)],
                   fill=GOLD, sw=1.3, close=True))
    o.append(_rect(310, 278, 60, 10, fill="#dfe7ef", sw=1.2))
    # expanded outlet to the right
    o.append(_rect(490, 230, 120, 80, fill="#e9eef4", sw=1.6))
    o.append(_rect(604, 224, 12, 92, fill="#e9eef4", sw=1.4))
    o.append(_arrow(500, 270, 590, 270, sw=1.4, color=GREEN))
    # spraywater manifold downstream of pressure reduction
    o.append(_line(430, 150, 430, 206, sw=2.0, color=BLUE))
    o.append(_rect(422, 148, 16, 10, fill="#e9eef4", sw=1.3))
    _droplets(o, 430, 212, nx=4, spread=26, length=22, color=BLUE)
    o.append(_num(340, 206, 1))
    o.append(_num(250, 264, 2))
    o.append(_num(340, 288, 3))
    o.append(_num(548, 250, 4))
    o.append(_num(430, 168, 5))
    o.append(_num(340, 100, 6))
    o.append(_legend([
        "Thân rèn-chế tạo / Forged-fabricated body",
        "Cage tôi cứng / Case-hardened cage",
        "Nút dẫn hướng / Guided plug",
        "Đầu ra mở rộng / Expanded outlet",
        "Manifold nước phun / Spraywater manifold",
        "Cơ cấu chấp hành / Actuator",
    ], 500, 80, lh=24, size=7.0))
    return _finish(w, h, o,
                   "Figure 7.10 (p. 170) - Cross-section view of steam conditioning valve",
                   "Hình 7.10 (tr. 170) · Mặt cắt van điều hòa hơi",
                   "Hình 7.10 (tr. 170) · Mặt cắt van điều hòa hơi kết hợp giảm áp và điều khiển "
                   "nhiệt độ: thân rèn-chế tạo, cage tôi cứng, nút dẫn hướng, đầu ra mở rộng và "
                   "manifold nước phun phía sau cấp giảm áp.",
                   "Figure 7.10 (p. 170) · Cross-section of a steam conditioning valve combining "
                   "pressure reduction and temperature control: forged-fabricated body, "
                   "case-hardened cage, guided plug, expanded outlet and a spraywater manifold "
                   "downstream of the reduction stage.",
                   "Sơ đồ Hình 7.10 (tr. 170) mặt cắt van điều hòa hơi",
                   "Schematic of Figure 7.10 (p. 170) steam conditioning valve cross-section")


# ---------------------------------------------------------------------------
# Figure 7.11 - Variable-geometry, backpressure-activated spray nozzle
# ---------------------------------------------------------------------------
@_reg
def fig_f7_11():
    """Figure 7.11 (p. 171) - Backpressure-activated spray nozzle."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Vòi phun hình học thay đổi, kích hoạt bằng áp suất ngược / "
               "Variable-Geometry, Backpressure-Activated Spray Nozzle", 8.0, weight="600"))
    # chamber
    o.append(_rect(160, 150, 260, 150, fill="#f4f7fb", sw=1.8))
    # water inlet
    o.append(_line(90, 225, 160, 225, sw=2.0, color=BLUE))
    o.append(_arrow(105, 225, 148, 225, sw=1.4, color=BLUE))
    o.append(T(92, 214, "Nước / Water", 7.4, anchor="start"))
    # horizontal spring pushing the plug toward the seat
    _hspring(o, 196, 330, 225, width=26, turns=5)
    o.append(_poly([(330, 212), (372, 212), (372, 238), (330, 238)],
                   fill=GOLD, sw=1.3, close=True))
    # seat and exit cone
    o.append(_rect(400, 200, 28, 50, fill="#dfe7ef", sw=1.4))
    o.append(_poly([(428, 205), (566, 178), (566, 272), (428, 245)],
                   fill="#eef3fb", sw=1.4, close=True))
    _droplets(o, 470, 214, nx=5, spread=44, length=22, color=BLUE)
    o.append(T(470, 300, "Hóa hơi qua lối ra vòi / Flashing across nozzle exit",
               7.0, color=GREY))
    # leaders and callouts
    o.append(_leader(270, 200, 270, 176))
    o.append(T(270, 170, "Lò xo / Spring", 7.2))
    o.append(_leader(350, 212, 350, 176))
    o.append(T(350, 170, "Nút / Plug", 7.2))
    o.append(_leader(414, 200, 414, 176))
    o.append(T(414, 170, "Đế / Seat", 7.2))
    o.append(T(340, 128, "Áp suất ngược vòi giữ lưu lượng tối thiểu thấp / "
               "Nozzle backpressure keeps minimum flow low", 7.0, color=GREY))
    for cx, cy, n in [(270, 200, 1), (350, 212, 2), (414, 200, 3), (500, 232, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Lò xo nút vòi / Nozzle plug spring",
        "Nút di động / Moving plug",
        "Đế vòi / Nozzle seat",
        "Tia phun vào hơi / Spray into steam",
    ], 60, 336, lh=18))
    return _finish(w, h, o,
                   "Figure 7.11 (p. 171) - Variable-geometry, backpressure-activated spray nozzle",
                   "Hình 7.11 (tr. 171) · Vòi phun kích hoạt bằng áp suất ngược",
                   "Hình 7.11 (tr. 171) · Mặt cắt vòi phun có nút tải lò xo: ở độ mở thấp, "
                   "áp suất ngược tăng làm nước bay hơi qua lối ra vòi và ép nút đóng, thiết lập "
                   "lại áp suất cho cột chất lỏng.",
                   "Figure 7.11 (p. 171) · Cross-section of a spring-loaded spray nozzle: at low "
                   "openings, nozzle backpressure makes water flash at the exit and forces the plug "
                   "closed, re-pressurizing the liquid leg.",
                   "Sơ đồ Hình 7.11 (tr. 171) vòi phun kích hoạt bằng áp suất ngược",
                   "Schematic of Figure 7.11 (p. 171) backpressure-activated spray nozzle")


# ---------------------------------------------------------------------------
# Figure 7.12 - Ring-style attemperator with liner
# ---------------------------------------------------------------------------
@_reg
def fig_f7_12():
    """Figure 7.12 (p. 171) - Ring-style attemperator with liner."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Bộ làm mát kiểu vòng có ống lót / Ring-Style Attemperator with Liner",
               9.0, weight="600"))
    # pipe and liner
    o.append(_rect(60, 180, 560, 90, fill="#eef3fb", sw=1.7))
    o.append(_line(60, 180, 620, 180, sw=1.7, color=INK))
    o.append(_line(60, 270, 620, 270, sw=1.7, color=INK))
    o.append(_line(60, 196, 620, 196, sw=1.0, dash="5 3", color=GREY))
    o.append(_line(60, 254, 620, 254, sw=1.0, dash="5 3", color=GREY))
    # ring manifold around the pipe
    o.append(_rect(230, 164, 220, 16, fill=FILL, sw=1.4))
    o.append(_rect(230, 270, 220, 16, fill=FILL, sw=1.4))
    o.append(_rect(322, 118, 16, 46, fill="#e9eef4", sw=1.4))
    o.append(_arrow(330, 122, 330, 160, sw=1.2, color=BLUE))
    o.append(T(330, 110, "Manifold cấp nước / Water supply manifold", 7.4))
    # radial spray nozzles
    for nx in (262, 310, 358, 406):
        o.append(_arrow(nx, 196, nx, 224, sw=1.2, color=BLUE))
        o.append(_arrow(nx, 254, nx, 226, sw=1.2, color=BLUE))
        o.append(_circle(nx, 180, 3.0, fill=GOLD, sw=0.9))
        o.append(_circle(nx, 270, 3.0, fill=GOLD, sw=0.9))
    # axial steam flow
    o.append(_arrow(90, 225, 170, 225, sw=1.4, color=GREEN))
    o.append(_arrow(470, 225, 580, 225, sw=1.4, color=GREEN))
    o.append(T(90, 214, "Dòng hơi dọc trục / Axial steam flow", 7.0, anchor="start"))
    for cx, cy, n in [(330, 140, 1), (262, 210, 2), (406, 240, 3), (540, 225, 4)]:
        o.append(_num(cx, cy, n))
    o.append(T(340, 310, "Phun hướng tâm vào vùng nhiễu loạn cao · diện tích tiếp xúc lớn · "
               "bay hơi nhanh / Radial spray into high turbulence · large contact area · "
               "rapid vaporization", 7.0, color=GREY))
    o.append(_legend([
        "Manifold cấp nước / Water supply manifold",
        "Vòi phun trên thành ống / Wall-mounted nozzles",
        "Ống lót / Liner",
        "Dòng hơi dọc trục / Axial steam flow",
    ], 60, 340, lh=18))
    return _finish(w, h, o,
                   "Figure 7.12 (p. 171) - Ring-style attemperator with liner",
                   "Hình 7.12 (tr. 171) · Bộ làm mát kiểu vòng có ống lót",
                   "Hình 7.12 (tr. 171) · Bộ làm mát hơi có manifold cấp nước vòng quanh đường "
                   "ống, phun nước theo phương hướng tâm qua các vòi trên thành ống vào dòng hơi "
                   "dọc trục nhiễu loạn, bên trong có ống lót.",
                   "Figure 7.12 (p. 171) · A steam attemperator whose water manifold rings the "
                   "pipe and feeds wall-mounted nozzles that spray radially into the turbulent "
                   "axial steam flow, with an internal liner.",
                   "Sơ đồ Hình 7.12 (tr. 171) bộ làm mát kiểu vòng có ống lót",
                   "Schematic of Figure 7.12 (p. 171) ring-style attemperator with liner")


# ---------------------------------------------------------------------------
# Figure 7.13 - Steam sparger with drilled-hole noise control
# ---------------------------------------------------------------------------
@_reg
def fig_f7_13():
    """Figure 7.13 (p. 172) - Steam sparger with drilled-hole noise control."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28,
               "Ống phân phối hơi với công nghệ giảm ồn bằng lỗ khoan / "
               "Steam Sparger with Drilled-Hole Noise Control Technology", 7.8, weight="600"))
    # condenser / turbine exhaust duct
    o.append(_rect(100, 110, 540, 210, fill="#fafbfd", sw=1.7))
    o.append(T(370, 130, "Ống xả tụng điện hoặc tuabin / Condenser or turbine exhaust duct",
               7.2, color=GREY))
    # sparger pipe
    o.append(_rect(70, 200, 330, 44, fill="#e9eef4", sw=1.7))
    o.append(_rect(60, 194, 12, 56, fill="#e9eef4", sw=1.4))
    o.append(_arrow(66, 222, 130, 222, sw=1.4, color=GREEN))
    o.append(T(72, 188, "Hơi vào / Steam inlet", 7.2, anchor="start"))
    # drilled holes and jets
    for hx in range(140, 390, 30):
        o.append(_circle(hx, 200, 2.8, fill=BLUE, sw=0))
        o.append(_circle(hx, 244, 2.8, fill=BLUE, sw=0))
        o.append(_arrow(hx, 198, hx, 176, sw=0.9, color=BLUE))
        o.append(_arrow(hx, 246, hx, 268, sw=0.9, color=BLUE))
    o.append(T(230, 300, "Các lỗ khoan nhỏ giảm ồn do dòng chảy / "
               "Many small drilled holes abate flow-induced noise", 7.0, color=GREY))
    o.append(T(230, 316, "Tạo áp suất ngược cho van chuyển tải, hạn chế vận tốc hơi / "
               "Provides backpressure to the bypass valve and limits steam velocity",
               7.0, color=GREY))
    for cx, cy, n in [(230, 222, 1), (160, 190, 2), (340, 254, 3)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Đường ống phân phối hơi / Sparger pipe",
        "Lỗ khoan giảm ồn / Drilled noise-control holes",
        "Tia hơi xả vào tụng điện / Steam jets into the condenser",
    ], 60, 342, lh=20))
    return _finish(w, h, o,
                   "Figure 7.13 (p. 172) - Steam sparger with drilled-hole noise control",
                   "Hình 7.13 (tr. 172) · Ống phân phối hơi giảm ồn bằng lỗ khoan",
                   "Hình 7.13 (tr. 172) · Ống phân phối hơi giảm áp xả hơi an toàn vào tụng điện "
                   "qua nhiều lỗ khoan nhỏ, đồng thời tạo áp suất ngược cho van chuyển tải và "
                   "giảm ồn do dòng chảy.",
                   "Figure 7.13 (p. 172) · A pressure-reducing sparger discharges steam safely "
                   "into a condenser through many small drilled holes, providing backpressure to "
                   "the bypass valve and abating flow-induced noise.",
                   "Sơ đồ Hình 7.13 (tr. 172) ống phân phối hơi giảm ồn bằng lỗ khoan",
                   "Schematic of Figure 7.13 (p. 172) drilled-hole noise-control steam sparger")


# ---------------------------------------------------------------------------
# Figure 7.14 - Typical actuation package for turbine bypass
# ---------------------------------------------------------------------------
@_reg
def fig_f7_14():
    """Figure 7.14 (p. 174) - Typical actuation package for turbine bypass."""
    w, h = 680, 450
    o = [_defs()]
    o.append(T(340, 28,
               "Gói cơ cấu chấp hành điển hình cho ứng dụng chuyển tải tuabin / "
               "Typical Actuation Package for Turbine Bypass Applications", 8.0, weight="600"))
    # valve body
    o.append(_rect(285, 292, 110, 58, fill="#eef3fb", sw=1.7))
    o.append(_rect(270, 306, 16, 30, fill="#e9eef4", sw=1.3))
    o.append(_rect(394, 306, 16, 30, fill="#e9eef4", sw=1.3))
    o.append(_line(340, 292, 340, 250, sw=3.0, color=INK))
    # piston actuator
    o.append(_rect(295, 150, 90, 100, fill="#f4f7fb", sw=1.7))
    o.append(_line(295, 202, 385, 202, sw=1.4, color=BLUE))
    o.append(_spring(340, 155, 196, width=28, turns=3))
    o.append(T(340, 226, "Cơ cấu piston / Piston actuator", 7.0))
    # digital valve controller
    o.append(_rect(440, 160, 150, 72, fill="#fdf3e6", sw=1.7))
    o.append(T(515, 186, "Bộ điều khiển van số /", 7.2))
    o.append(T(515, 200, "Digital valve controller", 7.2))
    o.append(T(515, 218, "Chỉnh định từ xa / Remote tuning", 6.8, color=GREY))
    # air supply and feedback
    o.append(_line(100, 196, 440, 196, sw=1.7, color=BLUE))
    o.append(_arrow(130, 196, 180, 196, sw=1.3, color=BLUE))
    o.append(T(102, 186, "Cấp khí / Air supply", 7.2, anchor="start"))
    o.append(_line(340, 268, 440, 220, sw=1.0, dash="4 3", color=GREY))
    o.append(T(352, 268, "Phản hồi vị trí / Position feedback", 6.8, anchor="start"))
    o.append(T(340, 340, "Hành trình 2–4 giây · độ chính xác vị trí tốt hơn 1% / "
               "2-4 second stroke · better than 1% positioning accuracy", 7.0, color=GREY))
    for cx, cy, n in [(340, 178, 1), (515, 196, 2), (150, 196, 3), (386, 242, 4)]:
        o.append(_num(cx, cy, n))
    o.append(_legend([
        "Cơ cấu chấp hành piston khí nén / Pneumatic piston actuator",
        "Bộ điều khiển van số / Digital valve controller",
        "Nguồn cấp khí / Air supply",
        "Phản hồi vị trí và chỉnh định từ xa / Position feedback and remote tuning",
    ], 60, 354, lh=18, size=7.0))
    return _finish(w, h, o,
                   "Figure 7.14 (p. 174) - Typical actuation package for turbine bypass",
                   "Hình 7.14 (tr. 174) · Gói cơ cấu chấp hành cho chuyển tải tuabin",
                   "Hình 7.14 (tr. 174) · Gói cơ cấu chấp hành điển hình gồm piston khí nén, bộ "
                   "điều khiển van số, nguồn cấp khí và phản hồi vị trí, cho phép hành trình "
                   "2–4 giây với độ chính xác tốt hơn 1%.",
                   "Figure 7.14 (p. 174) · A typical actuation package with a pneumatic piston, "
                   "digital valve controller, air supply and position feedback, delivering a "
                   "2-4 second stroke with better than 1% positioning accuracy.",
                   "Sơ đồ Hình 7.14 (tr. 174) gói cơ cấu chấp hành chuyển tải tuabin",
                   "Schematic of Figure 7.14 (p. 174) turbine bypass actuation package")
