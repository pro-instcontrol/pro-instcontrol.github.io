# -*- coding: utf-8 -*-
"""Vector figures for Practical Process Control, Chapter 3 (control valves).

Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
Curves are computed from the governing characteristic equations.
"""
import math

from vfig import (BLUE, GOLD, GREY, INK, PAPER, RED, GREEN, _arrow, _axes, _box,
                  _circle, _curve, _defs, _ellipse, _f, _fig, _hatch, _label,
                  _line, _path, _poly, _rect, _ring, _txt, svg)


def _finish(o, w, h, vi, en, aria_vi="", aria_en=""):
    return _fig(svg(w, h, _defs() + "".join(o), aria_vi or vi), vi, en,
                aria_vi or vi, aria_en or en)


def _legend(x, y, rows, w=126):
    """Small colour-key box: rows of (colour, label, dash)."""
    h = 12 * len(rows) + 8
    o = [_rect(x, y, w, h, "#ffffff", sw=0.7, stroke="#d8d8d8")]
    for i, (col, lab, dash) in enumerate(rows):
        yy = y + 12 + i * 12
        o.append(_line(x + 6, yy - 2.6, x + 22, yy - 2.6, sw=1.6, color=col, dash=dash))
        o.append(_txt(x + 26, yy, lab, 6.4, anchor="start", color=INK))
    return "".join(o)


def _legend_h(x, y, rows, gap=22):
    """Horizontal colour key: entries laid out left to right, no box.

    Used under the abscissa when every corner of the plot is crossed by a
    curve and a boxed legend would hide part of one.
    """
    o = []
    cx = x
    for col, lab, dash in rows:
        o.append(_line(cx, y, cx + 14, y, sw=1.6, color=col, dash=dash))
        o.append(_txt(cx + 18, y + 2.6, lab, 6.4, anchor="start", color=INK))
        cx += 18 + 3.4 * len(lab) + gap
    return "".join(o)


def _spring(cx, y0, y1, amp=13, n=6, color=GOLD):
    """Vertical helical spring drawn as a zigzag between two flat ends."""
    step = (y1 - y0) / float(2 * n)
    pts = []
    for i in range(2 * n + 1):
        dx = 0 if i in (0, 2 * n) else (amp if i % 2 else -amp)
        pts.append((cx + dx, y0 + i * step))
    return _poly(pts, sw=1.3, color=color)


# ---------------------------------------------------------------- curves
def _eqpct(x, R=50.0):
    """Equal-percentage inherent characteristic, normalised to 1 at x = 1."""
    return R ** (x - 1.0)


def _linear(x):
    return x


def _quick(x):
    return math.sqrt(max(0.0, x))


def _installed(f, x, dc):
    """Boger's installed characteristic: q = f / sqrt(DC + (1-DC) f^2)."""
    v = f(x)
    return v / math.sqrt(dc + (1.0 - dc) * v * v)


# ---------------------------------------------------------------- 3.1
def fig_3_1():
    o = [_txt(330, 18, "Van bi: loại khoan thẳng và loại có hình dạng", 8.6, weight="600")]
    for k, (cx, kind) in enumerate(((180, "conv"), (480, "char"))):
        cy = 96
        o.append(_rect(cx - 96, cy - 34, 192, 68, "#eef3fb"))
        o.append(_txt(cx, cy + 54, "(a) khoan thẳng, quay 1/4 vòng" if k == 0
                      else "(b) có hình dạng, cửa chữ V", 7.2, color=GREY))
        # seat rings
        o.append(_rect(cx - 96, cy - 30, 10, 60, "#d8d2c4"))
        o.append(_rect(cx + 86, cy - 30, 10, 60, "#d8d2c4"))
        # ball
        o.append(_circle(cx, cy, 26, fill="#f3ead6"))
        if kind == "conv":
            # bore straight through: the valve is shown open
            o.append(_rect(cx - 26, cy - 7, 52, 14, PAPER, sw=1.0))
            o.append(_txt(cx, cy - 14, "lỗ xuyên", 6.2, color=GREY))
        else:
            # V notch cut into the downstream face
            o.append(_poly([(cx + 26, cy - 15), (cx + 4, cy), (cx + 26, cy + 15)],
                           fill=PAPER, sw=1.0, close=True))
            o.append(_txt(cx - 6, cy + 4, "V", 7.4, color=GREY))
        # stem + handle
        o.append(_rect(cx - 4, cy - 56, 8, 32, "#cfc8b8"))
        o.append(_line(cx - 18, cy - 58, cx + 18, cy - 58, sw=3.2, color="#b9b0a0"))
        o.append(_txt(cx, cy - 66, "trục quay", 6.6, color=GREY))
        o.append(_arrow(cx - 122, cy, cx - 100, cy, sw=1.4, color=BLUE))
        o.append(_arrow(cx + 100, cy, cx + 122, cy, sw=1.4, color=BLUE))
    o.append(_txt(330, 182, "chiều dòng chảy", 7, color=BLUE))
    return _finish(o, 660, 194,
                   "Hình 3-1 · Mặt cắt của van bi khoan thẳng và van bi có hình dạng.",
                   "Figure 3.1 · Cross-sectional views of conventional and characterised ball valves.",
                   "Van bi khoan thẳng có lỗ tròn xuyên tâm; van bi có hình dạng có cửa cắt chữ V.")


# ---------------------------------------------------------------- 3.2
def fig_3_2():
    o = [_txt(330, 16, "Đặc tuyến van bi theo phần trăm hành trình", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 140
    o.append(_axes(x0, y0, W, H, "% hành trình", "% lưu lượng",
                   xt=[(0, "0"), (0.25, "25"), (0.5, "50"), (0.75, "75"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: x, x0, y0, W, H, color=INK, sw=1.8))
    o.append(_curve(lambda x: _eqpct(x, 50.0), x0, y0, W, H, color=GOLD, sw=1.8))
    o.append(_curve(lambda x: _installed(_eqpct, x, 0.2), x0, y0, W, H, color=GOLD, sw=1.3, dash="5 4"))
    o.append(_legend(x0 + 10, y0 + 6,
                     [(INK, "khoan thẳng: tuyến tính", ""),
                      (GOLD, "bi hình dạng: parabol", ""),
                      (GOLD, "lắp đặt, DC = 0,2", "5 4")], w=130))
    return _finish(o, 660, 200,
                   "Hình 3-2 · Van bi có hình dạng với cửa parabol gần đặc tuyến phần trăm đều, còn van bi "
                   "khoan thẳng và kiểu lồng gần tuyến tính khi dùng cho nước. Với khí ở vận tốc tới hạn, "
                   "đường đặc tuyến của van bi có hình dạng dịch về phía tuyến tính.",
                   "Figure 3.2 · The characterised ball valve with a parabolic notch is nearly equal percentage, "
                   "while the ball and cage characteristics are closer to linear on water service. On gas "
                   "service at critical velocities the characterised curves move towards linear.")


# ---------------------------------------------------------------- 3.3
def fig_3_3():
    o = [_txt(330, 18, "Ba vị trí của cánh van bướm", 8.6, weight="600")]
    for cx, ang, lab in ((130, 0, "đóng hoàn toàn (0°)"),
                         (330, 45, "tiết lưu (45°)"),
                         (530, 90, "mở hoàn toàn (90°)")):
        cy = 92
        o.append(_rect(cx - 62, cy - 34, 124, 68, "#f2f5fa", sw=1.0))
        o.append(_line(cx - 62, cy - 34, cx - 62, cy + 34, sw=1.4))
        o.append(_line(cx + 62, cy - 34, cx + 62, cy + 34, sw=1.4))
        # disc: perpendicular to the flow when closed (0°), parallel when open (90°)
        disc = _ellipse(cx, cy, 8, 31, fill="#d9cfb6", sw=1.2)
        o.append('<g transform="rotate(%.1f %d %d)">%s</g>' % (ang, cx, cy, disc))
        o.append(_txt(cx, cy + 54, lab, 6.9, color=GREY))
        o.append(_arrow(cx - 92, cy, cx - 70, cy, sw=1.2, color=BLUE))
        if ang == 0:
            o.append(_txt(cx, cy - 42, "chắn kín dòng", 6.4, color=RED))
    return _finish(o, 660, 176,
                   "Hình 3-3 · Các vị trí của cánh van bướm. Ở 0° đĩa vuông góc với dòng và van đóng; ở 90° "
                   "đĩa song song với dòng và van mở hoàn toàn.",
                   "Figure 3.3 · Vane positions of a butterfly valve. At 0° the disc is across the flow and "
                   "the valve is closed; at 90° the disc is parallel to the flow and the valve is wide open.")


# ---------------------------------------------------------------- 3.4
def fig_3_4():
    o = [_txt(330, 16, "Đặc tuyến van bướm theo góc mở", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 140
    o.append(_axes(x0, y0, W, H, "góc mở (độ)", "% lưu lượng",
                   xt=[(0, "0"), (60 / 90.0, "60"), (1, "90")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))

    def flap(a, p=1.6):
        return min(1.0, math.sin(math.pi * (a / 90.0) / 2.0) ** p)

    # eccentric shaft swings the disc clear of the seat earlier in the stroke
    o.append(_curve(lambda a: flap(a, 1.0), x0, y0, W, H, n=181, xr=(0, 90),
                    color=GOLD, sw=1.6, dash="5 4"))
    o.append(_curve(flap, x0, y0, W, H, n=181, xr=(0, 90), color=INK, sw=1.8))
    xr = x0 + (60 / 90.0) * W
    o.append(_line(xr, y0, xr, y0 + H, sw=0.8, color=GOLD, dash="4 3"))
    o.append(_label(xr - 4, y0 - 6, "giới hạn tiết lưu 60°", 6.8, GOLD, anchor="end"))
    o.append(_legend(x0 + W - 152, y0 + H - 46,
                     [(INK, "trục thẳng", ""),
                      (GOLD, "trục lệch tâm", "5 4")], w=150))
    return _finish(o, 660, 200,
                   "Hình 3-4 · Đặc tuyến lưu lượng của van bướm phụ thuộc vị trí trục (thẳng hay lệch tâm) và "
                   "tỉ lệ kích thước trục so với cỡ van. Với mục đích tiết lưu, van thường chỉ được quay "
                   "trong khoảng 0–60°.",
                   "Figure 3.4 · The flow characteristic of a butterfly valve depends on shaft position "
                   "(aligned or eccentric) and on shaft size relative to valve size. For throttling the valve "
                   "is usually limited to 0–60°.")


# ---------------------------------------------------------------- 3.5
def fig_3_5():
    o = [_txt(330, 18, "Van số: mỗi cửa gấp đôi cửa nhỏ hơn kề nó", 8.6, weight="600")]
    o.append(_rect(70, 46, 520, 56, "#eef3fb"))
    widths = (14, 20, 28, 40, 56, 78, 104)
    total = sum(widths) + 6 * 6
    x = 70 + (520 - total) / 2.0
    for i, w in enumerate(widths):
        o.append(_rect(x, 54, w, 40, "#f3ead6"))
        o.append(_txt(x + w / 2.0, 78, str(2 ** i), 6.6, color=GREY))
        x += w + 6
    o.append(_txt(330, 120, "cửa 1 · 2 · 4 · 8 · 16 · 32 · 64 đơn vị tiết diện", 7, color=GREY))
    o.append(_arrow(70, 132, 590, 132, sw=1.2, color=BLUE))
    o.append(_txt(330, 146, "dòng chảy", 7, color=BLUE))
    o.append(_label(330, 168, "độ phân giải = 2ⁿ − 1 : 1   →   8 bit = 255:1, 16 bit = 65.535:1", 7.2, INK))
    return _finish(o, 660, 184,
                   "Hình 3-5 · Trong một van số, mỗi phần tử van có tiết diện gấp đôi phần tử nhỏ hơn kề nó.",
                   "Figure 3.5 · In a digital valve each element is twice the size of its smaller neighbour.")


# ---------------------------------------------------------------- 3.6
def fig_3_6():
    o = [_txt(330, 18, "Mặt cắt van cầu một cửa", 8.6, weight="600")]
    # body: two side ports opening into a taller central chamber
    o.append(_path("M 96 96 L 206 96 L 246 62 L 414 62 L 454 96 L 564 96 "
                   "L 564 140 L 454 140 L 414 174 L 246 174 L 206 140 L 96 140 Z",
                   fill="#eef3fb", sw=1.3))
    # internal partition with the single seat opening in the middle
    o.append(_rect(246, 120, 62, 10, "#d9cfb6"))
    o.append(_rect(352, 120, 62, 10, "#d9cfb6"))
    # plug above the seat, on the stem
    o.append(_poly([(306, 94), (354, 94), (346, 118), (314, 118)],
                   fill="#d9cfb6", sw=1.1, close=True))
    o.append(_rect(324, 44, 12, 52, "#cfc8b8"))
    o.append(_rect(314, 38, 32, 8, "#cfc8b8"))
    # flow: in from the left, up through the seat, out to the right
    o.append(_arrow(66, 118, 92, 118, sw=1.4, color=BLUE))
    o.append(_arrow(568, 118, 594, 118, sw=1.4, color=BLUE))
    o.append(_arrow(330, 152, 330, 126, sw=1.0, color=GREY, dash="3 3"))
    # labels, each on a leader so nothing floats
    o.append(_line(338, 50, 350, 50, sw=0.7, color=GREY))
    o.append(_txt(352, 52, "trục van", 6.8, color=GREY, anchor="start"))
    o.append(_line(356, 104, 372, 104, sw=0.7, color=GREY))
    o.append(_txt(374, 106, "nút van (plug)", 6.8, color=GREY, anchor="start"))
    o.append(_line(358, 132, 374, 146, sw=0.7, color=GREY))
    o.append(_txt(376, 148, "đệm kín (seat)", 6.8, color=GREY, anchor="start"))
    o.append(_line(150, 186, 150, 144, sw=0.7, color=GREY))
    o.append(_txt(150, 198, "thân van", 6.8, color=GREY))
    o.append(_txt(80, 110, "cửa vào", 6.8, color=BLUE))
    o.append(_txt(580, 110, "cửa ra", 6.8, color=BLUE))
    return _finish(o, 660, 212,
                   "Hình 3-6 · Mặt cắt của một van cầu một cửa.",
                   "Figure 3.6 · Cross-section of a single-ported globe valve.")


# ---------------------------------------------------------------- 3.7
def fig_3_7():
    o = [_txt(330, 16, "Đặc tuyến lý thuyết dịch chuyển theo cách lắp đặt", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "% hành trình", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(_linear, x0, y0, W, H, color=INK, sw=1.6))
    o.append(_curve(lambda x: _installed(_linear, x, 0.2), x0, y0, W, H, color=INK, sw=1.3, dash="5 4"))
    o.append(_curve(lambda x: _eqpct(x, 50.0), x0, y0, W, H, color=GOLD, sw=1.6))
    o.append(_curve(lambda x: _installed(_eqpct, x, 0.2), x0, y0, W, H, color=GOLD, sw=1.3, dash="5 4"))
    o.append(_legend(x0 + 10, y0 + 4,
                     [(INK, "tuyến tính", ""),
                      (GOLD, "phần trăm đều", ""),
                      (GREY, "nét đứt: đã lắp đặt, DC = 0,2", "5 4")], w=126))
    o.append(_txt(330, 196, "đặc tuyến bản chất (nét liền) so với đặc tuyến lắp đặt (nét đứt)",
                  6.6, color=GREY))
    return _finish(o, 660, 208,
                   "Hình 3-7 · Đặc tuyến lý thuyết của van dịch chuyển theo cách lắp đặt. Các đường nét đứt "
                   "phản ánh sự dịch chuyển đó trong một quá trình chủ yếu là ma sát, nơi 100% lưu lượng và "
                   "20% tổng tổn thất áp suất được gán cho van điều khiển.",
                   "Figure 3.7 · The theoretical valve characteristics shift with installation. The dotted "
                   "lines reflect that shift in a mostly friction process where 100 % flow and 20 % of the "
                   "total pressure drop were assigned to the control valve.")


# ---------------------------------------------------------------- 3.8
def fig_3_8():
    o = [_txt(330, 16, "Van kẹp với cơ cấu đóng chính xác", 8.6, weight="600")]
    o.append(_rect(150, 52, 360, 84, "#eef3fb"))
    o.append(_path("M 150 68 L 250 68 Q 300 70 300 94 Q 300 118 250 120 L 150 120", sw=1.6))
    o.append(_path("M 510 68 L 350 68 Q 300 70 300 94 Q 300 118 350 120 L 510 120", sw=1.6))
    # pinch bar sits on the body top face
    o.append(_rect(282, 34, 36, 18, "#cfc8b8"))
    o.append(_arrow(300, 22, 300, 32, sw=1.2, color=GOLD))
    o.append(_txt(306, 28, "lực kẹp", 6.8, color=GOLD, anchor="start"))
    o.append(_arrow(108, 94, 146, 94, sw=1.4, color=BLUE))
    o.append(_arrow(514, 94, 552, 94, sw=1.4, color=BLUE))
    o.append(_line(168, 168, 206, 121, sw=0.7, color=GREY))
    o.append(_txt(156, 178, "ống mềm", 6.8, color=GREY, anchor="start"))
    o.append(_line(494, 168, 466, 132, sw=0.7, color=GREY))
    o.append(_txt(506, 178, "thân van", 6.8, color=GREY, anchor="end"))
    return _finish(o, 660, 188,
                   "Hình 3-8 · Van kẹp với cơ cấu “đóng chính xác”.",
                   "Figure 3.8 · Pinch valve with “accurate closure”.")


# ---------------------------------------------------------------- 3.9
def fig_3_9():
    o = [_txt(330, 16, "Cải thiện đặc tuyến bằng ống lót hình nón", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "% hành trình", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: min(1.0, x ** 0.45), x0, y0, W, H, color=INK, sw=1.7))
    o.append(_curve(lambda x: x ** 0.85, x0, y0, W, H, color=GOLD, sw=1.7))
    o.append(_legend(x0 + W - 148, y0 + H - 46,
                     [(INK, "ống lót thẳng: mở nhanh", ""),
                      (GOLD, "ống lót hình nón: gần tuyến tính", "")], w=146))
    return _finish(o, 660, 200,
                   "Hình 3-9 · Bằng cách giảm tiết diện cửa hoặc làm ống lót có dạng hình nón, đặc tuyến trở "
                   "nên tuyến tính hơn. Việc thêm một tiết lưu biến thiên trong ống lót tạo ra khả năng tiết "
                   "lưu ở nửa trên của hành trình.",
                   "Figure 3.9 · Reducing the port size or making the sleeve cone-shaped makes the "
                   "characteristic more linear. A variable orifice inside the sleeve provides throttling in "
                   "the upper half of the stroke.")


# ---------------------------------------------------------------- 3.10
def fig_3_10():
    o = [_txt(330, 18, "Van nút (plug) — mặt cắt điển hình", 8.6, weight="600")]
    o.append(_rect(120, 52, 420, 96, "#eef3fb"))
    # tapered plug, wider at the top so it wedges down into the seat
    o.append(_poly([(302, 62), (358, 62), (350, 138), (310, 138)],
                   fill="#d9cfb6", sw=1.2, close=True))
    # the port is a straight through-opening on the flow axis
    o.append(_rect(306, 88, 48, 24, PAPER, sw=0))
    o.append(_txt(330, 103, "cửa", 6.4, color=GREY))
    # re-stroke the plug outline so the bore does not cut it in two
    o.append(_poly([(302, 62), (358, 62), (350, 138), (310, 138)],
                   fill="none", sw=1.2, close=True))
    o.append(_rect(324, 30, 12, 34, "#cfc8b8"))
    o.append(_rect(314, 24, 32, 7, "#cfc8b8"))
    o.append(_arrow(86, 100, 118, 100, sw=1.4, color=BLUE))
    o.append(_arrow(542, 100, 574, 100, sw=1.4, color=BLUE))
    o.append(_line(338, 36, 348, 36, sw=0.7, color=GREY))
    o.append(_txt(350, 38, "trục quay 90°", 6.8, color=GREY, anchor="start"))
    o.append(_line(150, 160, 150, 150, sw=0.7, color=GREY))
    o.append(_txt(150, 172, "thân van", 6.8, color=GREY))
    o.append(_line(392, 156, 352, 122, sw=0.7, color=GREY))
    o.append(_txt(394, 168, "nút côn", 6.8, color=GREY, anchor="start"))
    return _finish(o, 660, 186,
                   "Hình 3-10 · Mặt cắt điển hình của một van nút.",
                   "Figure 3.10 · Typical sectional view of a plug valve.")


# ---------------------------------------------------------------- 3.11
def fig_3_11():
    o = [_txt(330, 16, "Đặc tuyến van nút theo hình dạng cửa tiết lưu", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "% góc quay", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: min(1.0, x ** 0.5), x0, y0, W, H, color=INK, sw=1.7))
    o.append(_curve(lambda x: x ** 0.9, x0, y0, W, H, color=GOLD, sw=1.7))
    o.append(_legend(x0 + W - 142, y0 + H - 46,
                     [(INK, "cửa chữ nhật: mở nhanh", ""),
                      (GOLD, "cửa chữ V: gần tuyến tính", "")], w=140))
    return _finish(o, 660, 200,
                   "Hình 3-11 · Đặc tuyến của van nút là hàm của hình dạng tấm tiết lưu hay cửa chữ V.",
                   "Figure 3.11 · Plug valve characteristics are a function of the shape of the throttling "
                   "plate or V-port.")


# ---------------------------------------------------------------- 3.12
def fig_3_12():
    o = [_txt(330, 18, "Van Saunders kiểu tràn: ba vị trí chính", 8.6, weight="600")]
    for cx, bulge, lab in ((130, 2, "mở"), (330, 18, "giữa"), (530, 32, "đóng")):
        # closed body with a fixed weir inside
        o.append(_path("M %d 126 L %d 58 L %d 58 L %d 126 Z"
                       % (cx - 54, cx - 54, cx + 54, cx + 54), fill="#eef3fb", sw=1.6))
        # weir
        o.append(_poly([(cx - 22, 126), (cx, 94), (cx + 22, 126)], fill="#d9cfb6", sw=1.0, close=True))
        # diaphragm across the top, bulging down towards the weir
        o.append(_path("M %d 60 Q %d %d %d 60" % (cx - 54, cx, 60 + 2 * bulge, cx + 54),
                       sw=2.8, color="#8a7f6a"))
        # actuator stem pushing the diaphragm
        o.append(_rect(cx - 4, 40, 8, 20, "#cfc8b8"))
        o.append(_txt(cx, 144, lab, 6.9, color=GREY))
    o.append(_label(330, 164, "màng ngăn di chuyển so với gờ tràn cố định", 7, GREY))
    return _finish(o, 660, 176,
                   "Hình 3-12 · Các vị trí chính của van Saunders kiểu tràn.",
                   "Figure 3.12 · Main positions of a weir-type Saunders control valve.")


# ---------------------------------------------------------------- 3.13
def fig_3_13():
    o = [_txt(330, 16, "Đặc tuyến van Saunders: thường và hai dải", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "% hành trình", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: min(1.0, x ** 0.4), x0, y0, W, H, color=INK, sw=1.7))
    o.append(_curve(lambda x: x ** 0.9, x0, y0, W, H, color=GOLD, sw=1.7))
    o.append(_legend(x0 + W - 150, y0 + H - 46,
                     [(INK, "kiểu thường: gần mở nhanh", ""),
                      (GOLD, "kiểu hai dải: gần tuyến tính", "")], w=148))
    return _finish(o, 660, 200,
                   "Hình 3-13 · Đặc tuyến của van Saunders thông thường gần với mở nhanh, còn đặc tuyến của "
                   "kiểu hai dải gần tuyến tính hơn.",
                   "Figure 3.13 · The characteristic of a conventional Saunders valve is close to quick "
                   "opening, while the dual-range design is closer to linear.")


# ---------------------------------------------------------------- 3.14
def fig_3_14():
    o = [_txt(330, 18, "Van cổng trượt với tấm chèn chữ V", 8.6, weight="600")]
    o.append(_rect(110, 46, 440, 96, "#eef3fb"))
    # fixed plate with a round bore
    o.append(_rect(250, 56, 22, 76, "#d9cfb6"))
    o.append(_circle(261, 94, 17, fill=PAPER))
    # sliding plate, V notch cut into the edge that faces the bore
    o.append(_path("M 300 56 L 322 56 L 322 132 L 300 132 L 300 114 L 314 94 L 300 74 Z",
                   fill="#cfc8b8", sw=1.2))
    # gate travel
    o.append(_arrow(340, 58, 340, 128, sw=1.2, color=GOLD))
    o.append(_txt(346, 62, "trượt", 6.8, color=GOLD, anchor="start"))
    o.append(_arrow(70, 94, 108, 94, sw=1.4, color=BLUE))
    o.append(_arrow(554, 94, 592, 94, sw=1.4, color=BLUE))
    o.append(_line(212, 158, 252, 136, sw=0.7, color=GREY))
    o.append(_txt(210, 168, "tấm cố định (lỗ tròn)", 6.8, color=GREY, anchor="end"))
    o.append(_line(412, 158, 322, 136, sw=0.7, color=GREY))
    o.append(_txt(414, 168, "tấm trượt (chèn chữ V)", 6.8, color=GREY, anchor="start"))
    return _finish(o, 660, 186,
                   "Hình 3-14 · Van cổng trượt điển hình với tấm chèn chữ V.",
                   "Figure 3.14 · Typical sliding gate valve with a “V” insert.")


# ---------------------------------------------------------------- 3.15
def fig_3_15():
    o = [_txt(330, 16, "Đặc tuyến các kiểu van cổng trượt", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "% hành trình", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: min(1.0, x ** 0.3), x0, y0, W, H, color=GREY, sw=1.6))
    o.append(_curve(lambda x: x ** 0.75, x0, y0, W, H, color=INK, sw=1.7))
    o.append(_curve(lambda x: x, x0, y0, W, H, color=GOLD, sw=1.7))
    o.append(_legend(x0 + W - 152, y0 + H - 58,
                     [(GREY, "A — cổng dao cắt: 10:1", ""),
                      (INK, "B — chèn chữ V: 20:1", ""),
                      (GOLD, "C — tấm/đĩa nhiều lỗ: 50:1", "")], w=150))
    return _finish(o, 660, 200,
                   "Hình 3-15 · Đặc tuyến của các kiểu van cổng trượt khác nhau.",
                   "Figure 3.15 · Characteristics of various sliding gate valve types.")


# ---------------------------------------------------------------- 3.16
def fig_3_16():
    o = [_txt(330, 18, "Van nút cân bằng động", 8.6, weight="600")]
    o.append(_rect(120, 60, 420, 92, "#eef3fb"))
    # plug
    o.append(_rect(330, 74, 16, 64, "#d9cfb6"))
    # return spring, compressed by the plug
    xs = [352, 362, 372, 382, 392, 402, 412]
    o.append(_path("M " + " L ".join("%d %d" % (x, 106 + (7 if i % 2 else -7))
                                     for i, x in enumerate(xs)), sw=1.4, color=GOLD))
    o.append(_txt(382, 134, "lò xo hồi vị", 6.6, color=GOLD))
    # process pressure pushing the plug
    o.append(_arrow(150, 122, 326, 122, sw=1.6, color=RED))
    o.append(_txt(142, 126, "P₁", 7.4, color=RED, anchor="end"))
    # outlet
    o.append(_arrow(542, 106, 574, 106, sw=1.3, color=BLUE))
    o.append(_txt(558, 98, "ra", 6.8, color=BLUE))
    # pilot poppet, inside the body, acting on the plug
    o.append(_box(168, 66, 100, 24, "van thí điểm", fill="#fdeccf", size=6.8))
    o.append(_line(268, 78, 330, 78, sw=0.9, color=GREY, dash="3 2"))
    o.append(_arrow(86, 106, 118, 106, sw=1.4, color=BLUE))
    return _finish(o, 660, 176,
                   "Hình 3-16 · Sơ đồ hoạt động của van nút cân bằng động: áp suất tĩnh của dòng quá trình "
                   "đẩy nút van thắng lực lò xo hồi vị; việc điều khiển do cụm van thí điểm kiểu poppet "
                   "đảm nhiệm.",
                   "Figure 3.16 · Operation of a dynamically balanced plug valve: the static pressure of the "
                   "process fluid moves the plug against a return spring, and control is achieved with a "
                   "pilot poppet assembly.")


# ---------------------------------------------------------------- 3.17
def fig_3_17():
    o = [_txt(330, 18, "Van thẳng dòng kiểu xy-lanh điều khiển bằng màng", 8.6, weight="600")]
    # actuator: air chamber closed by a diaphragm
    o.append(_rect(258, 36, 144, 40, "#f6e6c8"))
    o.append(_path("M 258 76 Q 330 90 402 76", sw=2.6, color="#8a7f6a"))
    o.append(_arrow(236, 54, 254, 54, sw=1.2, color=GOLD))
    o.append(_txt(234, 58, "khí", 6.8, color=GOLD, anchor="end"))
    # stem down to the plug
    o.append(_rect(324, 86, 12, 34, "#cfc8b8"))
    # body with the seat across the bore
    o.append(_rect(140, 104, 380, 74, "#eef3fb"))
    o.append(_poly([(306, 120), (354, 120), (344, 148), (316, 148)],
                   fill="#d9cfb6", sw=1.1, close=True))
    o.append(_rect(200, 148, 106, 8, "#d9cfb6"))
    o.append(_rect(354, 148, 106, 8, "#d9cfb6"))
    o.append(_arrow(100, 138, 138, 138, sw=1.4, color=BLUE))
    o.append(_arrow(522, 138, 560, 138, sw=1.4, color=BLUE))
    o.append(_line(404, 80, 422, 86, sw=0.7, color=GREY))
    o.append(_txt(424, 88, "màng ngăn", 6.8, color=GREY, anchor="start"))
    o.append(_line(356, 130, 380, 136, sw=0.7, color=GREY))
    o.append(_txt(382, 138, "nút van", 6.8, color=GREY, anchor="start"))
    o.append(_line(176, 192, 176, 180, sw=0.7, color=GREY))
    o.append(_txt(176, 204, "thân van", 6.8, color=GREY))
    return _finish(o, 660, 216,
                   "Hình 3-17 · Mặt cắt của van thẳng dòng kiểu xy-lanh điều khiển bằng màng.",
                   "Figure 3.17 · Sectional view of a diaphragm-operated cylinder in-line valve.")


# ---------------------------------------------------------------- 3.18
def fig_3_18():
    o = [_txt(330, 18, "Van thẳng dòng có phần tử giãn nở", 8.6, weight="600")]
    o.append(_rect(110, 56, 440, 100, "#eef3fb"))
    # solid rubber cylinder; the annulus around it is the variable restriction
    o.append(_path("M 292 84 L 368 84 Q 380 84 380 106 Q 380 128 368 128 "
                   "L 292 128 Q 280 128 280 106 Q 280 84 292 84 Z",
                   fill="#d9cfb6", sw=1.2))
    o.append(_arrow(330, 30, 330, 80, sw=1.4, color=GOLD))
    o.append(_txt(336, 34, "áp suất điều khiển", 6.8, color=GOLD, anchor="start"))
    o.append(_arrow(66, 106, 108, 106, sw=1.4, color=BLUE))
    o.append(_arrow(556, 106, 598, 106, sw=1.4, color=BLUE))
    o.append(_line(428, 62, 368, 72, sw=0.7, color=GREY))
    o.append(_txt(430, 60, "khe vành khuyên", 6.8, color=GREY, anchor="start"))
    o.append(_line(330, 168, 330, 132, sw=0.7, color=GREY))
    o.append(_txt(330, 180, "xy-lanh cao su giãn nở", 6.8, color=GREY))
    return _finish(o, 660, 192,
                   "Hình 3-18 · Hình dạng tổng thể của van thẳng dòng có phần tử giãn nở: một xy-lanh cao su "
                   "đặc được giãn ra hoặc co lại để thay đổi tiết diện khe vành khuyên.",
                   "Figure 3.18 · General view of an expandable-element in-line valve: a solid rubber "
                   "cylinder is expanded or contracted to change the area of an annular space.")


# ---------------------------------------------------------------- 3.19
def fig_3_19():
    o = [_txt(330, 18, "Van tương tác dòng — hiệu ứng Coanda", 8.6, weight="600")]
    # ducts drawn as thick strokes with an outline
    for x1, y1, x2, y2, wd in ((110, 96, 268, 96, 34), (268, 96, 436, 50, 24),
                               (268, 96, 436, 142, 24)):
        o.append(_path("M %d %d L %d %d" % (x1, y1, x2, y2), sw=wd, color="#dfe7f2"))
        o.append(_path("M %d %d L %d %d" % (x1, y1, x2, y2), sw=1.2, color=INK))
    # the jet attaches to one branch (Coanda) …
    o.append(_path("M 128 96 L 268 96 L 420 54", sw=2.6, color=BLUE))
    o.append(_arrow(408, 58, 428, 51, sw=2.6, color=BLUE))
    # … and can be flipped to the other
    o.append(_path("M 268 96 L 420 140", sw=1.4, color=GREY, dash="5 4"))
    o.append(_arrow(60, 96, 106, 96, sw=1.6, color=BLUE))
    o.append(_txt(58, 88, "nguồn", 6.8, color=BLUE, anchor="end"))
    # control ports at the base of the Y
    o.append(_arrow(250, 44, 250, 80, sw=1.3, color=RED))
    o.append(_arrow(250, 148, 250, 112, sw=1.3, color=RED))
    o.append(_txt(250, 38, "cửa điều khiển", 6.6, color=RED))
    o.append(_txt(250, 162, "cửa điều khiển", 6.6, color=RED))
    o.append(_txt(446, 48, "ra B", 7.2, color=GREY, anchor="start"))
    o.append(_txt(446, 146, "ra A", 7.2, color=GREY, anchor="start"))
    return _finish(o, 660, 180,
                   "Hình 3-19 · Hoạt động của van tương tác dòng: hai cửa điều khiển đặt ở đáy chỗ giao chữ Y "
                   "bẻ dòng xả sang nhánh này hay nhánh kia theo kiểu lật trạng thái.",
                   "Figure 3.19 · Operation of fluid-interaction valves: two lateral control ports at the "
                   "base of the Y intersection divert the discharge from one port to the other in a "
                   "flip-flop action.")


# ---------------------------------------------------------------- 3.20
def fig_3_20():
    o = [_txt(330, 16, "Đặc tuyến lưu lượng bản chất của van", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 140
    o.append(_axes(x0, y0, W, H, "% hành trình van", "% lưu lượng tối đa",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(_quick, x0, y0, W, H, color=GREY, sw=1.7))
    o.append(_curve(_linear, x0, y0, W, H, color=INK, sw=1.7))
    o.append(_curve(lambda x: _eqpct(x, 50.0), x0, y0, W, H, color=GOLD, sw=1.7))
    o.append(_legend(x0 + W - 130, y0 + H - 58,
                     [(GREY, "mở nhanh", ""),
                      (INK, "tuyến tính", ""),
                      (GOLD, "phần trăm đều (R = 50)", "")], w=128))
    return _finish(o, 660, 200,
                   "Hình 3-20 · Đặc tuyến lưu lượng bản chất: mở nhanh, tuyến tính và phần trăm đều.",
                   "Figure 3.20 · Inherent flow characteristics: quick opening, linear and equal percentage.")


# ---------------------------------------------------------------- 3.21
def fig_3_21():
    o = [_txt(330, 16, "Ảnh hưởng của hệ số méo dạng DC", 8.6, weight="600")]
    x0, y0, W, H = 90, 40, 430, 140
    o.append(_axes(x0, y0, W, H, "% hành trình van", "% lưu lượng",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    for dc, col, dash in ((1.0, GREY, "2 3"), (0.5, "#b9b0a0", "3 3"), (0.2, INK, ""),
                          (0.05, GOLD, "")):
        o.append(_curve(lambda x, d=dc: _installed(_linear, x, d), x0, y0, W, H,
                        color=col, sw=1.6, dash=dash))
    for dc, col, dash in ((0.2, INK, "5 4"), (0.05, GOLD, "5 4")):
        o.append(_curve(lambda x, d=dc: _installed(_eqpct, x, d), x0, y0, W, H,
                        color=col, sw=1.2, dash=dash))
    o.append(_txt(330, 200, "DC càng nhỏ, đặc tuyến càng bão hoà sớm và hành trình hữu ích càng ngắn",
                  6.6, color=GREY))
    # key below the axis: inside the plot every corner is crossed by a curve
    for x, y, col, lab, dash in ((92, 216, GREY, "tuyến tính, DC = 1", "2 3"),
                                 (268, 216, "#b9b0a0", "tuyến tính, DC = 0,5", "3 3"),
                                 (444, 216, INK, "tuyến tính, DC = 0,2", ""),
                                 (92, 232, GOLD, "tuyến tính, DC = 0,05", ""),
                                 (268, 232, INK, "phần trăm đều (nét đứt)", "5 4")):
        o.append(_line(x, y - 2.5, x + 16, y - 2.5, sw=1.6, color=col, dash=dash))
        o.append(_txt(x + 20, y, lab, 6.4, anchor="start", color=INK))
    return _finish(o, 660, 244,
                   "Hình 3-21 · Ảnh hưởng của hệ số méo dạng (DC) lên van tuyến tính và van phần trăm đều "
                   "theo Boger. DC là tỉ lệ tổn thất áp suất trên van so với tổng tổn thất của hệ khi lưu "
                   "lượng cực đại.",
                   "Figure 3.21 · The effect of the distortion coefficient (DC) on inherently linear and "
                   "equal-percentage valves, after Boger. DC is the fraction of the total system pressure "
                   "drop that appears across the valve at maximum flow.")


# ---------------------------------------------------------------- 3.22
def fig_3_22():
    o = [_txt(330, 18, "Cân bằng lực trên van màng – lò xo", 8.6, weight="600")]
    for cx, direct, title in ((180, True, "(a) tác động thuận"),
                              (480, False, "(b) tác động nghịch")):
        if direct:
            # air above the diaphragm pushes down, spring below resists
            o.append(_rect(cx - 60, 46, 120, 46, "#eef3fb"))
            o.append(_line(cx - 60, 70, cx + 60, 70, sw=2.4, color="#8a7f6a"))
            o.append(_arrow(cx - 34, 30, cx - 34, 66, sw=1.2, color=BLUE))
            o.append(_txt(cx - 40, 34, "P", 7.4, color=BLUE, anchor="end"))
            o.append(_spring(cx, 96, 134))
        else:
            # spring above, air below the diaphragm pushes up
            o.append(_spring(cx, 42, 80))
            o.append(_rect(cx - 60, 84, 120, 46, "#eef3fb"))
            o.append(_line(cx - 60, 106, cx + 60, 106, sw=2.4, color="#8a7f6a"))
            o.append(_arrow(cx - 34, 126, cx - 34, 110, sw=1.2, color=BLUE))
            o.append(_txt(cx - 40, 130, "P", 7.4, color=BLUE, anchor="end"))
        o.append(_line(cx, 46 if not direct else 70, cx, 150, sw=2.2))
        o.append(_poly([(cx - 17, 150), (cx + 17, 150), (cx + 10, 164), (cx - 10, 164)],
                       fill="#d9cfb6", sw=1.0, close=True))
        o.append(_arrow(cx + 32, 180, cx + 32, 166, sw=1.2, color=RED))
        o.append(_txt(cx + 38, 178, "P<sub>V</sub>·A<sub>V</sub>", 6.6, color=RED, anchor="start"))
        o.append(_txt(cx, 198, title, 7.2, color=GREY))
    return _finish(o, 660, 208,
                   "Hình 3-22 · Các lực tác dụng lên van màng – lò xo, tác động thuận (a) và tác động nghịch "
                   "(b). Ở kiểu thuận, áp suất màng đẩy màng ngăn xuống; ở kiểu nghịch, áp suất màng đẩy "
                   "màng ngăn lên và lò xo nằm phía trên.",
                   "Figure 3.22 · Forces on a spring-and-diaphragm valve, direct acting (a) and reverse "
                   "acting (b). In the direct type the diaphragm pressure pushes the diaphragm down; in the "
                   "reverse type it pushes up and the spring sits above.")


# ---------------------------------------------------------------- 3.23
def fig_3_23():
    o = [_txt(330, 16, "Quan hệ lý thuyết và thực tế giữa áp suất màng và hành trình trục", 8.6,
              weight="600")]
    x0, y0, W, H = 90, 40, 430, 130
    o.append(_axes(x0, y0, W, H, "áp suất màng", "hành trình trục",
                   xt=[(0, "0"), (0.5, "50"), (1, "100")],
                   yt=[(0, "0"), (0.5, "50"), (1, "100")]))
    o.append(_curve(lambda x: x, x0, y0, W, H, color=GREY, sw=1.4, dash="5 4"))
    # two branches offset by the dead band: up on rising pressure, down on falling
    n = 40
    up = [(0.06 + 0.88 * i / n, (i / float(n)) ** 0.9) for i in range(n + 1)]
    dn = [(0.16 + 0.84 * i / n, (i / float(n)) ** 0.9) for i in range(n + 1)]
    band = up + dn[::-1]
    o.append(_poly([(x0 + a * W, y0 + H - b * H) for a, b in band],
                   fill="#f3e3c2", sw=1.2, color="#c9a86a", close=True))
    o.append(_poly([(x0 + a * W, y0 + H - b * H) for a, b in up], color=INK, sw=1.8))
    o.append(_poly([(x0 + a * W, y0 + H - b * H) for a, b in dn], color=INK, sw=1.8))
    o.append(_legend(x0 + W - 150, y0 + H - 46,
                     [(GREY, "lý thuyết: tuyến tính", "5 4"),
                      (INK, "thực tế: vòng trễ", "")], w=148))
    o.append(_line(212, 158, 200, 150, sw=0.7, color=GREY))
    o.append(_txt(214, 168, "vùng chết (bề rộng vòng)", 6.6, color=GREY, anchor="start"))
    return _finish(o, 660, 200,
                   "Hình 3-23 · Quan hệ lý thuyết và thực tế giữa áp suất trên màng và hành trình của trục "
                   "van — một nguồn phi tuyến và méo dạng nữa. Bề rộng vòng trễ là vùng chết mà bộ điều "
                   "khiển phải vượt qua trước khi van nhúc nhích.",
                   "Figure 3.23 · Ideal and actual relationship between diaphragm pressure and valve stem "
                   "travel — another source of non-linearity and distortion. The width of the loop is the "
                   "dead band the controller must overcome before the valve moves at all.")


# ---------------------------------------------------------------- 3.24
def fig_3_24():
    o = [_txt(330, 18, "Bộ định vị thông minh trong vòng điều khiển", 8.6, weight="600")]
    y = 74
    o.append(_box(20, y, 96, 40, "Bộ điều khiển\nquá trình", fill="#eef3fb"))
    o.append(_box(150, y, 96, 40, "Bộ định vị\n(tỉ lệ, K cao)", fill="#fdeccf"))
    o.append(_box(280, y, 96, 40, "Cơ cấu chấp\nhành + van", fill="#eef3fb"))
    o.append(_box(410, y, 96, 40, "Quá trình", fill="#eef3fb"))
    o.append(_box(540, y, 96, 40, "Cảm biến", fill="#eef3fb"))
    for a, b in ((116, 150), (246, 280), (376, 410), (506, 540)):
        o.append(_arrow(a, y + 20, b, y + 20, sw=1.2))
    o.append(_arrow(588, y + 40, 588, y + 76, sw=1.2))
    o.append(_line(588, y + 76, 68, y + 76, sw=1.2))
    o.append(_arrow(68, y + 76, 68, y + 42, sw=1.2))
    o.append(_arrow(330, y + 40, 330, y + 104, sw=1.1, color=GOLD))
    o.append(_line(330, y + 104, 198, y + 104, sw=1.1, color=GOLD))
    o.append(_arrow(198, y + 104, 198, y + 42, sw=1.1, color=GOLD))
    o.append(_txt(264, y + 116, "phản hồi vị trí trục (±0,1 mm)", 6.8, color=GOLD))
    o.append(_txt(330, 34, "tín hiệu đặt = đầu ra của bộ điều khiển chính", 6.9, color=GREY))
    return _finish(o, 660, 196,
                   "Hình 3-24 · Bộ định vị là một bộ điều khiển tỉ lệ có hệ số khuếch đại cao: nó đo vị trí "
                   "trục van tới ±0,1 mm, so với tín hiệu đặt do bộ điều khiển quá trình đưa ra và hiệu "
                   "chỉnh sai lệch. Hệ số khuếch đại vòng hở 10–200 ứng với dải tỉ lệ 10%–0,5%.",
                   "Figure 3.24 · A positioner is a high-gain proportional controller: it measures stem "
                   "position to within 0.1 mm, compares it with the set point supplied by the process "
                   "controller and corrects the error. Open-loop gain is 10–200, a proportional band of "
                   "10 %–0.5 %.")
