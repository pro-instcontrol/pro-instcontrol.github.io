# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 11 — Level Measurement (Detlef Brumbi).

Fifteen figures, 11.1 to 11.15. Every drawing is built from the geometry the
chapter states: the echo triangle of Equation 11.12, the FMCW ramp of Equation
11.16, the three radii of Equation 11.19, the exponential decay of 11.22.
Nothing is a raster crop.

In-figure labels stay symbolic (h, d, L, TX, RX, VCO, DRO) so the same SVG can
serve the Vietnamese page and the English companion page without translation.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

BLUE = "#2f5d8a"
RED = "#a8322d"
GREEN = "#3f6b47"
SAND = "#f7f4ed"
WATER = "#dbe7f2"
WATER2 = "#b9d0e3"
GREY = "#ececec"
STEEL = "#c9cdd2"

STY = ('<style>'
       '.b11{font:9.4px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}'
       '.t11{font:8.8px Inter,Helvetica,sans-serif;fill:#111}'
       '.s11{font:8.0px Inter,Helvetica,sans-serif;fill:#555}'
       '.k11{font:7.2px Inter,Helvetica,sans-serif;fill:#666}'
       '.m11{font:8.6px "Cambria Math",Georgia,serif;fill:#111;font-style:italic}'
       '</style>')


# ---------------------------------------------------------------- primitives
def _t(x, y, s, fs=8.8, anchor="middle", fill=TXT, bold=False, rot=None, ital=False):
    w = ' font-weight="600"' if bold else ""
    i = ' font-style="italic"' if ital else ""
    r = ' transform="rotate(%s %s %s)"' % (rot, _f(x), _f(y)) if rot else ""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s"%s%s%s>%s</text>'
            % (_f(x), _f(y), fs, fill, anchor, w, i, r, s))


def _l(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _r(x, y, w, h, fill="none", sw=1.0, stroke=INK, rx=0):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, stroke, sw))


def _c(cx, cy, r, fill="none", sw=1.0, stroke=INK):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy), _f(r), fill, stroke, sw))


def _poly(pts, fill="none", sw=1.0, stroke=INK, close=False):
    d = "M " + " L ".join("%s %s" % (_f(x), _f(y)) for x, y in pts) + (" Z" if close else "")
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (d, fill, stroke, sw)


def _p(d, fill="none", sw=1.0, color=INK, dash=""):
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (d, fill, color, sw, ds)


def _arrow(x1, y1, x2, y2, sw=1.0, color=INK, dash="", head=7.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    L, W = head, head * 0.42
    xa, ya = x2 - L * math.cos(ang) + W * math.sin(ang), y2 - L * math.sin(ang) - W * math.cos(ang)
    xb, yb = x2 - L * math.cos(ang) - W * math.sin(ang), y2 - L * math.sin(ang) + W * math.cos(ang)
    return (_l(x1, y1, x2, y2, sw, color, dash)
            + _poly([(x2, y2), (xa, ya), (xb, yb)], color, 0.7, color, close=True))


def _dim(x1, y1, x2, y2, lx, ly, label, fs=8.4, color="#666"):
    """Dimension line with arrowheads at both ends and a label at (lx, ly)."""
    return (_arrow(x1, y1, x2, y2, 0.7, color, head=5.0)
            + _arrow(x2, y2, x1, y1, 0.7, color, head=5.0)
            + _t(lx, ly, label, fs, "middle", color, ital=True))


def _liq(x, y, w, h, fill=WATER, top="#5b7c99"):
    return (_r(x, y, w, h, fill, 0, "none")
            + _l(x, y, x + w, y, 1.1, top))


def _tank(x, y, w, h, wall=2.4):
    """Open-topped vessel: two walls and a floor."""
    return (_l(x, y, x, y + h, wall) + _l(x + w, y, x + w, y + h, wall)
            + _l(x - wall / 2, y + h, x + w + wall / 2, y + h, wall))


def _gnd(x, y, w=18):
    return (_l(x, y, x, y + 6, 1.1) + _l(x - w / 2, y + 6, x + w / 2, y + 6, 1.4)
            + _l(x - w / 3, y + 9, x + w / 3, y + 9, 1.1)
            + _l(x - w / 6, y + 12, x + w / 6, y + 12, 1.0))


def _burst(x0, y, w, amp, cycles=4, color=INK, sw=1.2):
    pts = []
    for i in range(49):
        u = i / 48.0
        env = math.sin(math.pi * u) ** 0.45
        pts.append((x0 + u * w, y - amp * env * math.sin(2 * math.pi * cycles * u)))
    return _poly(pts, "none", sw, color)


# ---------------------------------------------------------------- 11.1
def fig_11_1():
    """Tank with the four mounting modes, plus h, d, L."""
    W, H = 680, 250
    b = []
    tw, th, top = 106, 138, 62
    bot = top + th
    surf = top + 52
    cx = [88, 250, 412, 574]

    for i, x in enumerate(cx):
        left = x - tw / 2
        b.append(_liq(left + 3, surf, tw - 6, bot - surf - 3))
        b.append(_tank(left, top, tw, bot - top))
        b.append(_t(x, 220, "(%s)" % "abcd"[i], 9.0, "middle", "#555"))

    # (a) sensor in the bottom, in contact with the product
    a = cx[0]
    b.append(_r(a - 15, bot - 26, 30, 15, STEEL, 1.0))
    b.append(_l(a, bot - 11, a, bot + 18, 1.2))
    b.append(_t(a + 22, bot - 15, "LS", 7.2, "start", "#555", True))

    # (b) contactless instrument on the roof, and the two dimensions it implies
    c = cx[1]
    b.append(_r(c - 14, top - 20, 28, 16, STEEL, 1.0))
    b.append(_l(c - 3, top - 4, c - 24, surf, 0.8, "#666", "4 3"))
    b.append(_l(c + 3, top - 4, c + 24, surf, 0.8, "#666", "4 3"))
    b.append(_l(c, top - 4, c, surf, 0.7, "#888", "2 3"))
    b.append(_dim(c + 70, top, c + 70, surf, c + 76, (top + surf) / 2 + 3, "d", 8.6))
    b.append(_dim(c + 70, surf, c + 70, bot, c + 76, (surf + bot) / 2 + 3, "L", 8.6))

    # (c) intrusive probe
    e = cx[2]
    b.append(_r(e - 14, top - 20, 28, 16, STEEL, 1.0))
    b.append(_r(e - 4, top - 4, 8, bot - top - 8, "#9aa2ab", 0.9))
    b.append(_t(e + 12, top + 40, "LI", 7.2, "start", "#555", True))

    # (d) switch through the side wall
    g = cx[3]
    b.append(_r(g + tw / 2 - 1, surf + 26, 16, 15, STEEL, 1.0))
    b.append(_l(g + tw / 2 + 15, surf + 33, g + tw / 2 + 34, surf + 33, 1.2))
    b.append(_t(g + tw / 2 + 38, surf + 36, "LS", 7.2, "start", "#555", True))

    # h on the first tank
    b.append(_dim(cx[0] - 70, top, cx[0] - 70, bot, cx[0] - 76, (top + bot) / 2, "h", 8.6))

    return _fig(
        svg(W, H, STY + "".join(b), "Bốn cách lắp cảm biến đo mức trên một bồn chứa"),
        "Hình 11.1. Một bồn chứa chất lỏng hay vật liệu rời (phần gạch chéo) — đối tượng cần đo. "
        "Cảm biến mức có thể được lắp (a) tiếp xúc với sản phẩm ở đáy, (b) không tiếp xúc trên nóc, "
        "(c) như một đầu dò xuyên vào bồn, hoặc (d) ở thành bên như một công tắc mức. Chiều cao bồn "
        "h coi như không đổi, nên mức L suy ra từ khoảng cách d: L = h − d.",
        "Figure 11.1. A tank holding a liquid or a bulk solid (hatched area) — the product to be "
        "measured. The level sensor can be mounted (a) in contact with the product at the bottom, "
        "(b) as a contactless instrument on the roof, (c) as an intrusive probe, or (d) in the side "
        "wall as a level switch. The tank height h is constant, so the level L follows from the "
        "distance d: L = h − d.",
        "Bốn bồn chứa cạnh nhau minh hoạ bốn cách lắp đặt: cảm biến ở đáy, cảm biến không tiếp xúc "
        "trên nóc với hai kích thước d và L, đầu dò xuyên qua nóc, và công tắc mức ở thành bên. "
        "Bồn thứ nhất có kích thước chiều cao h.",
        "Four tanks side by side showing the four mounting modes: a sensor in the bottom, a "
        "contactless sensor on the roof with the dimensions d and L, an intrusive probe through "
        "the roof, and a level switch in the side wall. The first tank carries the height h.")


# ---------------------------------------------------------------- 11.2
def fig_11_2():
    """Buoyancy on a partly dipped body, and the force balance."""
    W, H = 680, 300
    b = []
    vx, vy, vw, vh = 80, 92, 320, 186
    surf = vy + 58
    b.append(_liq(vx + 3, surf, vw - 6, vh - 58 - 3))
    b.append(_tank(vx, vy, vw, vh))
    b.append(_t(vx + 10, surf - 7, "\u03c1\u2097", 9.4, "start", "#2f5d8a", ital=True))

    # the body
    rx, rw = 225, 40
    b.append(_r(rx, 66, rw, 184, "#d7dde4", 1.2))
    b.append(_t(rx + rw / 2, 86, "\u03c1, A", 9.0, "middle", "#111", ital=True))
    b.append(_r(rx - 30, 34, 100, 26, SAND, 1.0))
    b.append(_t(rx + 20, 51, "F\u1d3f", 9.4, "middle", "#111", True))
    b.append(_l(rx + rw / 2, 60, rx + rw / 2, 66, 1.2))

    # weight and buoyancy
    b.append(_arrow(198, 160, 198, 248, 1.4, RED))
    b.append(_t(198, 153, "F\u1d33", 9.4, "middle", RED, True))
    b.append(_arrow(292, 214, 292, 152, 1.4, BLUE))
    b.append(_t(292, 145, "F\u1d2e", 9.4, "middle", BLUE, True))

    # b and Ld
    b.append(_dim(160, 66, 160, 250, 152, 160, "b", 8.6))
    b.append(_l(160, 66, rx, 66, 0.6, "#aaa", "3 3"))
    b.append(_l(160, 250, rx, 250, 0.6, "#aaa", "3 3"))
    b.append(_dim(316, surf, 316, 250, 330, (surf + 250) / 2, "L\u2091", 8.6))
    b.append(_l(316, surf, vx + vw, surf, 0.6, "#aaa", "3 3"))

    # force balance inset
    b.append(_r(432, 84, 228, 172, SAND, 1.0, "#c9c2b4", 6))
    b.append(_t(546, 108, "F\u1d3f = F\u1d33 \u2212 F\u1d2e", 10.2, "middle", "#111", True))
    b.append(_l(470, 150, 470, 150, 0.1, "#000"))
    b.append(_arrow(470, 130, 470, 196, 1.2, RED))
    b.append(_t(470, 124, "F\u1d33", 8.6, "middle", RED, True))
    b.append(_arrow(470, 130, 470, 132, 0.1, BLUE))
    b.append(_t(508, 160, "\u03c1 g A b", 9.0, "start", "#333", ital=True))
    b.append(_arrow(556, 196, 556, 130, 1.2, BLUE))
    b.append(_t(556, 124, "F\u1d2e", 8.6, "middle", BLUE, True))
    b.append(_t(594, 160, "\u03c1\u2097 g A L\u2091", 9.0, "start", "#333", ital=True))
    b.append(_t(546, 232, "F\u1d3f \u2192 c\u1ea3m bi\u1ebfn l\u1ef1c", 8.2, "middle", "#666"))

    return _fig(
        svg(W, H, STY + "".join(b), "Lực nổi tác dụng lên một vật nhúng một phần trong chất lỏng"),
        "Hình 11.2. Các đại lượng của một vật rắn nhúng trong chất lỏng. Các lực F tính được từ "
        "phương trình 11.2, 11.3 và 11.4. \u03c1 = khối lượng riêng; b = chiều dài vật; L\u2091 = "
        "phần chiều dài bị nhúng.",
        "Figure 11.2. Quantities of a solid body immersed in a liquid. The forces F follow from "
        "Equations 11.2, 11.3 and 11.4. \u03c1 = density; b = length of the body; L\u2091 = dipped "
        "length.",
        "Một bồn chứa chất lỏng có treo một thanh rắn tiết diện A, chiều dài b, nhúng xuống độ sâu "
        "L\u2091. Trọng lực F\u1d33 hướng xuống, lực nổi F\u1d2e hướng lên, hợp lực F\u1d3f đo được "
        "ở đầu treo. Khung bên phải ghi công thức của ba lực.",
        "A tank with a solid rod of cross-section A and length b hung in it, dipped to the depth "
        "L\u2091. Weight F\u1d33 points down, buoyancy F\u1d2e points up, and the resultant "
        "F\u1d3f is measured at the suspension. The panel on the right gives the three forces.")


# ---------------------------------------------------------------- 11.3
def fig_11_3():
    """Servo displacer: stepping motor, wire, ball, resonant frequency."""
    W, H = 680, 300
    b = []
    vx, vy, vw, vh = 250, 176, 180, 112
    surf = vy + 38
    b.append(_liq(vx + 3, surf, vw - 6, vh - 38 - 3))
    b.append(_tank(vx, vy, vw, vh))
    b.append(_t(vx + vw + 8, surf - 6, "\u03c1\u2097", 9.0, "start", "#2f5d8a", ital=True))

    # motor and wire
    b.append(_r(250, 44, 72, 34, SAND, 1.0))
    b.append(_t(286, 66, "M", 10.0, "middle", "#111", True))
    b.append(_l(286, 78, 286, 248, 1.4))
    b.append(_c(286, 256, 8, "#c9cdd2", 1.0))
    b.append(_t(306, 260, "V", 9.0, "start", "#111", ital=True))

    # lever arm and sensor coil
    b.append(_l(286, 108, 372, 108, 2.6))
    b.append(_c(372, 108, 3.2, "#fff", 1.0))
    b.append(_r(372, 92, 54, 32, SAND, 1.0))
    b.append(_t(399, 112, "coil", 7.6, "middle", "#555"))

    # points A and B — both above the vessel, so the dimension stays clear
    b.append(_c(286, 108, 2.4, INK, 0.6, INK))
    b.append(_t(274, 104, "A", 8.6, "end", "#111", True))
    b.append(_c(286, 160, 2.4, INK, 0.6, INK))
    b.append(_t(274, 164, "B", 8.6, "end", "#111", True))
    b.append(_dim(306, 108, 306, 160, 316, 136, "l", 8.4))

    # signal converter
    b.append(_r(470, 84, 160, 62, SAND, 1.0))
    b.append(_t(550, 108, "SC", 10.0, "middle", "#111", True))
    b.append(_t(550, 126, "f \u2192 L, \u03c1", 8.2, "middle", "#555"))
    b.append(_arrow(426, 108, 470, 108, 1.1))
    b.append(_p("M 470 138 L 448 138 L 448 61 L 322 61", "none", 0.9, "#666", "5 4"))
    b.append(_arrow(340, 61, 322, 61, 0.9, "#666", "5 4"))

    return _fig(
        svg(W, H, STY + "".join(b), "Cảm biến đo mức, mặt phân cách và khối lượng riêng bằng lực nổi"),
        "Hình 11.3. Cảm biến đo mức, mặt phân cách và khối lượng riêng dựa trên hiệu ứng lực nổi. "
        "Một động cơ bước kéo quả cầu nhỏ gắn ở đầu sợi dây mảnh tới những độ cao khác nhau trong "
        "chất lỏng hoặc tới các mặt phân cách. Hợp lực F — hiệu giữa trọng lực và lực nổi — được đo "
        "qua tần số cộng hưởng của hệ dây–cầu. Cần gạt kích sợi dây dao động, cuộn cảm biến ghép với "
        "cần gạt đo tần số ấy. Bộ chuyển đổi tín hiệu điều khiển động cơ bước và tính ra các giá trị "
        "đo [6].",
        "Figure 11.3. Level, interface and density sensor using the effects of buoyancy. A stepping "
        "motor drives the small ball attached to the thin wire to different heights in the liquid or "
        "to the interfaces. The resulting force F, the difference between weight and buoyancy, is "
        "measured from the resonant frequency of the wire-ball system. The lever arm excites the wire "
        "into oscillation and a sensor coil coupled to the lever arm measures its frequency. The "
        "signal converter controls the stepping motor and computes the measured values [6].",
        "Một bồn chứa chất lỏng, phía trên có động cơ bước M kéo sợi dây mảnh xuống quả cầu nhỏ V "
        "nhúng trong chất lỏng. Cần gạt nằm ngang ở điểm A kích dây dao động, cuộn cảm biến đo tần "
        "số; đoạn dây giữa A và B dài l. Bộ chuyển đổi tín hiệu SC nối với cuộn cảm biến và có đường "
        "hồi tiếp về động cơ.",
        "A tank of liquid with a stepping motor M above it driving a thin wire down to a small ball V "
        "immersed in the liquid. A horizontal lever at point A excites the wire, a sensor coil reads "
        "the frequency, and the wire length between A and B is l. The signal converter SC connects to "
        "the coil and feeds back to the motor.")


# ---------------------------------------------------------------- 11.4
def fig_11_4():
    """(a) float with counterweight, (b) float with a reed switch."""
    W, H = 680, 290
    b = []

    # (a)
    ax, ay, aw, ah = 60, 82, 180, 186
    surf = ay + 70
    b.append(_liq(ax + 3, surf, aw - 6, ah - 70 - 3))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_r(96, surf - 9, 68, 16, SAND, 1.1, "#8a7a5e", 3))
    b.append(_l(130, surf - 9, 130, 58, 1.1))
    b.append(_l(130, 58, 262, 58, 1.1))
    b.append(_c(268, 58, 8, "#fff", 1.1))
    b.append(_c(268, 58, 2.0, INK, 0.6, INK))
    b.append(_l(276, 58, 276, 118, 1.1))
    b.append(_r(264, 118, 24, 30, "#c9cdd2", 1.0))
    b.append(_t(300, 136, "G", 9.0, "start", "#111", ital=True))
    b.append(_t(130, 274, "(a)", 9.0, "middle", "#555"))

    # (b)
    bx, by, bw, bh = 380, 82, 170, 186
    b2 = by + 70
    b.append(_liq(bx + 3, b2, bw - 6, bh - 70 - 3))
    b.append(_tank(bx, by, bw, bh))
    b.append(_r(bx + 76, 52, 18, 218, "#f2f2f2", 1.1))
    # float ring, drawn before the tube so the tube reads as passing through it
    b.append(_r(bx + 62, b2 - 9, 46, 18, SAND, 1.1, "#8a7a5e", 3))
    b.append(_r(bx + 76, 52, 18, 218, "#f2f2f2", 1.1))
    # magnet halves
    b.append(_r(bx + 66, b2 - 5, 7, 10, "#333", 0.8))
    b.append(_r(bx + 97, b2 - 5, 7, 10, "#333", 0.8))
    # reed contact at the surface, and two alternative heights
    b.append(_l(bx + 80, b2 - 8, bx + 85, b2, 1.1, RED))
    b.append(_l(bx + 85, b2, bx + 80, b2 + 8, 1.1, RED))
    b.append(_l(bx + 90, b2 - 8, bx + 85, b2, 1.1, RED))
    b.append(_l(bx + 85, b2, bx + 90, b2 + 8, 1.1, RED))
    for dy in (-46, 46):
        b.append(_l(bx + 81, b2 + dy - 7, bx + 85, b2 + dy, 0.9, "#bbb"))
        b.append(_l(bx + 89, b2 + dy - 7, bx + 85, b2 + dy, 0.9, "#bbb"))
    b.append(_l(bx + 85, 52, bx + 85, 34, 1.1))
    b.append(_l(bx + 85, 34, bx + 150, 34, 1.1))
    b.append(_r(bx + 150, 24, 40, 22, SAND, 1.0))
    b.append(_t(bx + 170, 39, "LS", 8.4, "middle", "#111", True))
    b.append(_t(bx + 85, 274, "(b)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Hai kiểu phao đo mức: phao đối trọng và phao có công tắc lưỡi gà"),
        "Hình 11.4. Nguyên lý làm việc của phao đo mức. (a) Một đối trọng cân bằng với phao nổi trên "
        "mặt chất lỏng; vị trí của nó biểu thị mức. (b) Trong phao có một nam châm tiếp xúc với công "
        "tắc lưỡi gà đặt trong ống dẫn hướng. Dùng rơ-le hai trạng thái, hệ này trở thành công tắc "
        "mức. Có thể đặt nhiều rơ-le trong ống để có nhiều điểm chuyển mạch, đạt chế độ gần liên tục.",
        "Figure 11.4. Principle of operation of float level meters. (a) A counterweight balances the "
        "float that swims on the liquid surface; its position represents the level. (b) The float "
        "contains a magnet that closes a reed switch inside a guide tube. With a bistable relay the "
        "arrangement works as a level switch, and several relays can be stacked in the tube for "
        "quasi-continuous operation.",
        "Hai hình: (a) bồn chứa có phao nổi, dây cáp vắt qua ròng rọc nối với đối trọng G; (b) bồn "
        "chứa có ống dẫn hướng thẳng đứng, phao hình vành khuyên trượt quanh ống với hai nửa nam "
        "châm, bên trong ống là công tắc lưỡi gà và hai vị trí chuyển mạch thay thế, dây dẫn lên hộp "
        "công tắc LS.",
        "Two views: (a) a tank with a float, its cable running over a pulley to the counterweight G; "
        "(b) a tank with a vertical guide tube, a ring float carrying two magnet halves sliding on it, "
        "a reed contact inside the tube with two alternative switching heights, and leads running up "
        "to the switch box LS.")


# ---------------------------------------------------------------- 11.5
def fig_11_5():
    """Hydrostatic level gaging: DP cell, HTG, bubble tube."""
    W, H = 680, 290
    b = []

    # (a) differential pressure against the roof space
    ax, ay, aw, ah = 52, 88, 108, 168
    surf = ay + 54
    b.append(_liq(ax + 3, surf, aw - 6, ah - 54 - 3))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_l(ax + aw / 2, ay + 4, ax + aw / 2, surf, 0.7, "#888", "2 3"))
    b.append(_l(ax + aw / 2, ay + 6, 186, ay + 6, 0.9, "#666"))
    b.append(_l(186, ay + 6, 186, 208, 0.9, "#666"))
    b.append(_l(ax + aw / 2, ay + ah, 186, ay + ah, 0.9, "#666"))
    b.append(_l(186, ay + ah, 186, 224, 0.9, "#666"))
    b.append(_r(164, 208, 46, 34, SAND, 1.0))
    b.append(_t(187, 229, "DP", 8.6, "middle", "#111", True))
    b.append(_t(146, 89, "p\u2080", 8.0, "middle", "#555", ital=True))
    b.append(_t(196, ay + ah - 8, "p", 8.0, "start", "#555", ital=True))
    b.append(_t(106, 276, "(a)", 9.0, "middle", "#555"))

    # (b) three sensors inside the liquid
    bx, by, bw, bh = 268, 88, 92, 168
    b.append(_liq(bx + 3, by + 40, bw - 6, bh - 40 - 3))
    b.append(_tank(bx, by, bw, bh))
    for i, yy in enumerate((by + 62, by + 112, by + 158)):
        b.append(_r(bx + bw - 2, yy - 6, 20, 12, STEEL, 1.0))
        b.append(_t(bx + bw + 22, yy - 5, "p%d" % (i + 1), 7.8, "middle", "#333", ital=True))
        b.append(_l(bx + bw + 18, yy, 404, yy, 0.8, "#666"))
    b.append(_r(404, 122, 42, 74, SAND, 1.0))
    b.append(_t(425, 152, "PC", 8.6, "middle", "#111", True))
    b.append(_t(425, 172, "HTG", 7.4, "middle", "#666"))
    b.append(_t(314, 276, "(b)", 9.0, "middle", "#555"))

    # (c) bubble tube: gas in at the top of the pipe, pressure tapped at the inlet
    cx0, cy0, cw, ch = 500, 88, 92, 168
    b.append(_liq(cx0 + 3, cy0 + 40, cw - 6, ch - 40 - 3))
    b.append(_tank(cx0, cy0, cw, ch))
    b.append(_r(452, 104, 38, 22, SAND, 1.0))
    b.append(_t(471, 119, "p", 8.4, "middle", "#111", ital=True))
    b.append(_l(471, 126, 471, 202, 1.0, "#666"))
    b.append(_r(456, 206, 30, 38, "#dfe4ea", 1.1, "#8a94a0", 3))
    b.append(_r(466, 196, 10, 12, "#dfe4ea", 1.1, "#8a94a0"))
    b.append(_l(471, 150, 520, 150, 0.9, "#666"))
    b.append(_l(520, 150, 520, 234, 0.9, "#666"))
    for dx, dy, r in ((514, 228, 2.4), (525, 233, 1.9), (509, 236, 1.6), (523, 220, 1.5)):
        b.append(_c(dx, dy, r, "#fff", 0.8, "#5b7c99"))
    b.append(_t(546, 276, "(c)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Ba cách đo mức bằng áp suất thuỷ tĩnh"),
        "Hình 11.5. Đo mức bằng áp suất thuỷ tĩnh; áp suất đáy p tỉ lệ với mức. (a) Áp suất khí "
        "quyển p\u2080 được loại trừ bằng phép đo hiệu áp: phía áp thấp của cảm biến hiệu áp nối "
        "bằng một ống mảnh lên nóc bồn. (b) Đo hiệu áp ngay trong lòng chất lỏng — gọi là “đo mức "
        "bồn bằng thuỷ tĩnh”, HTG — cho phép bù sai số do khối lượng riêng thay đổi; máy tính xử lý "
        "tín hiệu của cả ba cảm biến. (c) Với “ống sục bong bóng”, cảm biến đặt được trên nóc bồn: "
        "khí trơ được sục vào ống sao cho bong bóng thoát ra ở đầu ống; lưu lượng khí giữ không đổi "
        "nên áp suất cột áp đo được ngay tại đầu vào của ống.",
        "Figure 11.5. Level gaging by hydrostatic pressure; the bottom pressure p is proportional to "
        "the level. (a) Atmospheric pressure p\u2080 is removed by a differential measurement, the low "
        "side of the cell being piped to the roof of the tank. (b) A differential measurement inside "
        "the liquid — hydrostatic tank gaging, HTG — compensates errors from density variation, with a "
        "computer evaluating all three sensors. (c) With a bubble tube the sensor can sit on the roof: "
        "an inert gas is injected so that bubbles escape from the open end, and because the gas flow "
        "is constant the head pressure can be read at the inlet of the pipe.",
        "Ba bồn chứa cạnh nhau: (a) bồn có cảm biến hiệu áp DP ở đáy, phía áp thấp nối lên khoảng "
        "không trên mặt thoáng; (b) bồn có ba cảm biến áp suất p1, p2, p3 nối về máy tính; (c) bồn "
        "có ống sục khí từ bình khí trơ xuống gần đáy, áp kế đặt ở đầu vào ống và bong bóng thoát ra "
        "ở đầu ống.",
        "Three tanks: (a) with a DP cell at the bottom whose low side is piped to the headspace; "
        "(b) with three pressure sensors p1, p2, p3 wired to a computer; (c) with a purge tube running "
        "from a gas bottle down near the bottom, a pressure tap at the inlet, and bubbles escaping "
        "from the open end.")


# ---------------------------------------------------------------- 11.6
def fig_11_6():
    """Echo geometry and the burst timing."""
    W, H = 680, 300
    b = []

    # (a) geometry
    tx, ty, tw = 120, 62, 96
    ax, ay, aw, ah = 96, 88, 190, 184
    surf = ay + 88
    b.append(_liq(ax + 3, surf, aw - 6, ah - 88 - 3))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_r(ax + 30, ty - 24, 66, 24, SAND, 1.0))
    b.append(_t(ax + 63, ty - 8, "TX/RX", 8.2, "middle", "#111", True))
    b.append(_l(ax + 46, ty, ax + 22, surf, 0.8, "#666", "4 3"))
    b.append(_l(ax + 80, ty, ax + 104, surf, 0.8, "#666", "4 3"))
    b.append(_l(ax + 63, ty, ax + 63, surf, 1.0, RED))
    b.append(_arrow(ax + 63, surf - 6, ax + 63, ty + 8, 1.0, RED, "4 3"))
    b.append(_dim(ax + aw + 16, ay, ax + aw + 16, surf, ax + aw + 24, (ay + surf) / 2, "d", 8.6))
    b.append(_dim(ax + aw + 16, surf, ax + aw + 16, ay + ah, ax + aw + 24,
                  (surf + ay + ah) / 2, "L", 8.6))
    b.append(_dim(ax - 24, ay, ax - 24, ay + ah, ax - 32, (ay + ay + ah) / 2, "h", 8.6))
    b.append(_t(191, 288, "(a)", 9.0, "middle", "#555"))

    # (b) timing
    x0, x1 = 396, 640
    yTX, yRX = 128, 206
    b.append(_l(x0, 246, x1 + 4, 246, 1.1))
    b.append(_arrow(x0, 246, x0, 76, 1.0))
    b.append(_t(x1 + 10, 250, "t", 9.0, "start", "#333", ital=True))
    b.append(_t(x0 - 8, 84, "A", 9.0, "end", "#333", ital=True))
    b.append(_burst(x0 + 10, yTX, 52, 18, 4, INK, 1.2))
    b.append(_burst(x0 + 116, yRX, 52, 18, 4, RED, 1.2))
    b.append(_t(x0 + 36, yTX - 26, "TX", 8.2, "middle", "#111", True))
    b.append(_t(x0 + 142, yRX + 34, "RX", 8.2, "middle", RED, True))
    b.append(_l(x0 + 10, yTX - 20, x0 + 10, 254, 0.8, "#aaa", "3 3"))
    b.append(_l(x0 + 116, yRX + 26, x0 + 116, 254, 0.8, "#aaa", "3 3"))
    b.append(_dim(x0 + 10, 236, x0 + 116, 236, x0 + 63, 232, "t", 8.6, "#333"))
    b.append(_t(518, 288, "(b)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Nguyên lý đo mức bằng thời gian bay của sóng"),
        "Hình 11.6. (a) Sơ đồ đo thời gian bay: bộ phát ghép một sóng (siêu âm hoặc điện từ) vào "
        "khoảng không trên mặt sản phẩm; sóng truyền tới mặt chất lỏng, bị phản xạ và được một cảm "
        "biến thu lại. (b) Do tốc độ truyền v hữu hạn, có một khoảng trễ giữa lúc phát và lúc thu; "
        "ví dụ này dùng một chuỗi xung có điều chế. Thang thời gian là tuỳ ý.",
        "Figure 11.6. (a) The echo geometry: the emitter couples a wave (ultrasonic or "
        "electromagnetic) into the space above the product, the surface reflects it, and a sensor "
        "receives it. (b) Because the propagation velocity v is finite, a delay is measured between "
        "emission and reception; this example uses a modulated burst. The time scale is arbitrary.",
        "Hai phần: (a) bồn chứa có hộp phát–thu TX/RX trên nóc, chùm sóng hình nón chiếu xuống mặt "
        "chất lỏng, các kích thước h, d, L; (b) đồ thị thời gian với chuỗi xung phát TX và chuỗi xung "
        "thu RX lệch nhau một khoảng t.",
        "Two parts: (a) a tank with a TX/RX head on the roof, a conical beam reaching the liquid "
        "surface, and the dimensions h, d, L; (b) a timing diagram with the transmitted burst TX and "
        "the received burst RX separated by the delay t.")


# ---------------------------------------------------------------- 11.7
def fig_11_7():
    """Three antenna forms."""
    W, H = 680, 240
    b = []

    # (a) conical horn
    b.append(_poly([(92, 96), (92, 148), (74, 168), (74, 76)], "#e9edf1", 1.2, INK, True))
    b.append(_poly([(92, 96), (92, 148), (166, 176), (166, 68)], "#f4f6f8", 1.2, INK, True))
    b.append(_l(74, 76, 74, 96, 0.8))
    b.append(_l(166, 68, 166, 176, 1.6))
    for yy in (84, 104, 124, 144, 164):
        b.append(_l(166, yy, 190, yy - 6, 0.6, "#bbb", "3 3"))
    b.append(_t(130, 208, "(a)", 9.0, "middle", "#555"))

    # (b) dielectric rod
    b.append(_r(276, 74, 56, 22, "#dfe4ea", 1.1))
    b.append(_poly([(292, 96), (316, 96), (322, 156), (310, 186), (298, 186), (286, 156)],
                   "#eef1f4", 1.2, INK, True))
    b.append(_l(286, 156, 322, 156, 0.7, "#999", "3 3"))
    b.append(_t(304, 208, "(b)", 9.0, "middle", "#555"))

    # (c) Cassegrain: main parabola, subreflector, feed
    cx0, cy0 = 470, 150
    pts = []
    for i in range(31):
        u = -1.0 + 2.0 * i / 30.0
        pts.append((cx0 - 52 + 74 * u * u, cy0 - 62 * u))
    b.append(_poly(pts, "none", 2.0))
    # rim ticks at the two edges of the dish
    for u in (-1.0, 1.0):
        b.append(_l(cx0 - 52 + 74 * u * u, cy0 - 62 * u,
                    cx0 - 52 + 74 * u * u + 10, cy0 - 62 * u, 1.2, "#999"))
    # subreflector
    b.append(_p("M %s %s Q %s %s %s %s" % (_f(cx0 + 6), _f(cy0 - 20), _f(cx0 + 22), _f(cy0),
                                            _f(cx0 + 6), _f(cy0 + 20)), "#e9edf1", 1.2, INK))
    # rays: subreflector edge -> dish -> out to the left
    for sgn in (-1, 1):
        px = cx0 - 52 + 74 * 0.36
        py = cy0 + sgn * 62 * 0.6
        b.append(_l(cx0 + 6, cy0 + sgn * 20, px, py, 0.7, "#c07a3a", "4 3"))
        b.append(_l(px, py, cx0 - 46, py, 0.9, "#c07a3a"))
        b.append(_arrow(cx0 - 46, py, cx0 - 54, py, 0.9, "#c07a3a"))
    b.append(_l(cx0 + 22, cy0, cx0 + 58, cy0, 0.8, "#666"))
    b.append(_t(cx0 + 64, cy0 + 3, "feed", 7.6, "start", "#555"))
    b.append(_t(470, 208, "(c)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Ba dạng anten dùng cho radar đo mức"),
        "Hình 11.7. Các dạng anten thực tế dùng trong thiết bị radar đo mức: (a) anten còi hình "
        "nón, (b) anten thanh điện môi, (c) gương parabol với một anten nhỏ làm bộ bức xạ sơ cấp và "
        "một gương phụ cho góc chùm rất hẹp (kiểu Cassegrain).",
        "Figure 11.7. Practical antenna forms used for radar level instruments: (a) conical horn "
        "antenna, (b) dielectric rod antenna, and (c) parabolic mirror with a small antenna as primary "
        "radiator and an auxiliary reflector giving a very small beam angle (the Cassegrain model).",
        "Ba anten: (a) còi hình nón có ống dẫn sóng phía sau và các tia song song ở miệng; (b) thanh "
        "điện môi thuôn nhỏ dần gắn trên mặt bích; (c) gương parabol với gương phụ nhỏ ở tiêu điểm "
        "và bộ bức xạ sơ cấp, các tia phản xạ song song.",
        "Three antennas: (a) a conical horn with a waveguide behind it and parallel rays at the "
        "mouth; (b) a tapered dielectric rod on a flange; (c) a parabolic mirror with a small "
        "subreflector at the focus and a primary feed, the outgoing rays parallel.")


# ---------------------------------------------------------------- 11.8
def fig_11_8():
    """Compact radar head, block diagram."""
    W, H = 680, 300
    b = []

    # flange and antenna
    b.append(_r(48, 92, 96, 14, STEEL, 1.1))
    b.append(_poly([(74, 106), (118, 106), (132, 168), (60, 168)], "#f4f6f8", 1.2, INK, True))
    b.append(_l(60, 168, 132, 168, 1.8))
    for i in range(6):
        xx = 66 + i * 12
        b.append(_l(xx, 168, xx - 8 + i * 3, 206, 0.5, "#bbb", "3 3"))
    b.append(_t(96, 84, "flange", 7.6, "middle", "#555"))
    b.append(_t(96, 240, "s\u00f3ng radar", 7.4, "middle", "#888"))

    # blocks, first row
    row1 = [(170, "MW", "m\u1ea1ch si\u00eau cao t\u1ea7n"),
            (278, "DSP", "x\u1eed l\u00fd t\u00edn hi\u1ec7u"),
            (386, "\u00b5P", "\u0111i\u1ec1u khi\u1ec3n")]
    for x, lab, sub in row1:
        b.append(_r(x, 84, 84, 56, SAND, 1.1))
        b.append(_t(x + 42, 108, lab, 9.6, "middle", "#111", True))
        b.append(_t(x + 42, 126, sub, 6.8, "middle", "#666"))
    b.append(_arrow(144, 112, 170, 112, 1.1))
    b.append(_arrow(254, 112, 278, 112, 1.1))
    b.append(_arrow(362, 112, 386, 112, 1.1))

    # blocks, second row
    b.append(_r(386, 184, 84, 48, "#eef2f6", 1.1))
    b.append(_t(428, 204, "PSU", 9.4, "middle", "#111", True))
    b.append(_t(428, 220, "ngu\u1ed3n", 6.8, "middle", "#666"))
    b.append(_r(504, 84, 76, 56, "#eef2f6", 1.1))
    b.append(_t(542, 106, "display", 8.6, "middle", "#111", True))
    b.append(_t(542, 124, "hi\u1ec3n th\u1ecb", 6.8, "middle", "#666"))
    b.append(_r(504, 184, 76, 48, "#eef2f6", 1.1))
    b.append(_t(542, 204, "4\u201320 mA", 8.4, "middle", "#111", True))
    b.append(_t(542, 220, "\u0111\u1ea7u ra", 6.8, "middle", "#666"))
    b.append(_arrow(470, 112, 504, 112, 1.1))
    b.append(_arrow(470, 200, 504, 200, 1.1))
    b.append(_l(428, 184, 428, 146, 1.0, "#888"))
    b.append(_arrow(428, 150, 428, 146, 0.9, "#888"))
    b.append(_t(96, 276, "b\u1ed9 chuy\u1ec3n \u0111\u1ed5i tr\u00ean m\u1eb7t b\u00edch",
               7.8, "middle", "#666"))

    return _fig(
        svg(W, H, STY + "".join(b), "Sơ đồ khối một đầu đo radar công nghiệp kiểu compact"),
        "Hình 11.8. Kết cấu một hệ radar đo mức công nghiệp kiểu compact. Bộ chuyển đổi nằm trên "
        "mặt bích gồm toàn bộ mạch siêu cao tần, các tầng xử lý tín hiệu, khối vi xử lý, hiển thị, "
        "nguồn nuôi và đầu ra tín hiệu [6].",
        "Figure 11.8. Design of a compact industrial level radar system. The converter above the "
        "flange contains the complete microwave circuitry, the signal-processing stages, the "
        "microprocessor control, the display, the power supply and the output signal [6].",
        "Mặt bích nằm ngang có anten còi hướng xuống, chùm sóng radar chiếu vào bồn. Phía trên là "
        "các khối nối tiếp nhau: mạch siêu cao tần, xử lý tín hiệu, vi xử lý; vi xử lý nối tới khối "
        "hiển thị và khối đầu ra 4–20 mA, khối nguồn PSU cấp cho toàn bộ.",
        "A horizontal flange with a horn antenna pointing down into the tank. Above it the blocks run "
        "in series: microwave circuit, signal processing, microprocessor; the microprocessor drives "
        "the display and the 4–20 mA output, and the PSU feeds the whole head.")


# ---------------------------------------------------------------- 11.9
def fig_11_9():
    """TDR on a two-wire line: geometry and echo trace."""
    W, H = 680, 300
    b = []

    # (a) probe in a two-layer product
    ax, ay, aw, ah = 66, 84, 176, 190
    y1 = ay + 62
    y2 = ay + 128
    b.append(_r(ax + 3, y1, aw - 6, y2 - y1, WATER, 0, "none"))
    b.append(_r(ax + 3, y2, aw - 6, ay + ah - y2 - 3, WATER2, 0, "none"))
    b.append(_l(ax + 3, y1, ax + aw - 3, y1, 1.1, "#5b7c99"))
    b.append(_l(ax + 3, y2, ax + aw - 3, y2, 1.2, "#3f6b7a"))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_r(ax + 40, ay - 22, 96, 22, SAND, 1.0))
    b.append(_t(ax + 88, ay - 7, "TDR", 8.4, "middle", "#111", True))
    for xx in (ax + 74, ax + 102):
        b.append(_l(xx, ay - 2, xx, ay + ah - 14, 1.6, "#9aa2ab"))
    b.append(_l(ax + 74, ay + ah - 14, ax + 102, ay + ah - 14, 1.6, "#9aa2ab"))
    b.append(_t(ax + aw + 8, y1 - 4, "t\u2081", 8.4, "start", "#333", ital=True))
    b.append(_t(ax + aw + 8, y2 - 4, "t\u2082", 8.4, "start", "#333", ital=True))
    b.append(_t(ax + aw + 8, ay + ah - 12, "t\u2083", 8.4, "start", "#333", ital=True))
    b.append(_l(ax + 102, y1, ax + aw + 4, y1, 0.5, "#aaa", "2 3"))
    b.append(_l(ax + 102, y2, ax + aw + 4, y2, 0.5, "#aaa", "2 3"))
    b.append(_l(ax + 102, ay + ah - 14, ax + aw + 4, ay + ah - 14, 0.5, "#aaa", "2 3"))
    b.append(_t(154, 292, "(a)", 9.0, "middle", "#555"))

    # (b) echo trace
    x0, x1, yb = 366, 646, 178
    b.append(_l(x0, yb, x1 + 4, yb, 1.1))
    b.append(_arrow(x0, yb, x0, 66, 1.0))
    b.append(_t(x1 + 10, yb + 4, "t", 9.0, "start", "#333", ital=True))
    b.append(_t(x0 - 8, 76, "A", 9.0, "end", "#333", ital=True))

    def spike(x, h, up=False):
        yy = yb - h if up else yb + h
        return _l(x, yb, x, yy, 1.8, RED if up else BLUE)

    b.append(spike(x0 + 16, 54, True))
    b.append(spike(x0 + 84, 26, False))
    b.append(spike(x0 + 148, 40, False))
    b.append(spike(x0 + 226, 34, True))
    b.append(_l(x0 + 16, yb - 54, x0 + 16, 236, 0.6, "#ddd", "2 3"))
    b.append(_t(x0 + 16, 250, "t\u2080", 8.2, "middle", "#555", ital=True))
    b.append(_t(x0 + 84, 250, "2t\u2081", 8.2, "middle", "#555", ital=True))
    b.append(_t(x0 + 148, 250, "2t\u2082", 8.2, "middle", "#555", ital=True))
    b.append(_t(x0 + 226, 250, "2t\u2083", 8.2, "middle", "#555", ital=True))
    b.append(_t(506, 292, "(b)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Nguyên lý đo mức bằng phản xạ miền thời gian trên dây dẫn"),
        "Hình 11.9. Nguyên lý làm việc của hệ đo mức cao tần dẫn sóng theo dây. (a) Một xung điện "
        "được phát ra (thời điểm t\u2080) và đường dây hai sợi dẫn sóng điện từ đi xuống. Ở mỗi vị "
        "trí mà hằng số điện môi \u03b5 của môi trường xung quanh thay đổi, một phần sóng bị phản xạ "
        "mạnh (thời điểm t\u2081) trở về cảm biến. Sóng tiếp tục truyền hết đường dây và bị phản xạ "
        "lần thứ hai (t\u2082) tại mặt phân cách giữa hai chất lỏng, lần thứ ba tại đầu cuối dây. "
        "(b) Các khoảng trễ 2t\u2081, 2t\u2082, 2t\u2083 biểu thị vị trí các mặt phân cách so với "
        "đầu cuối dây — điểm có thể dùng làm mốc. Cực tính tín hiệu bị đảo khi phản xạ từ môi trường "
        "có hằng số điện môi thấp sang môi trường có hằng số điện môi cao hơn. Thang thời gian là "
        "tuỳ ý.",
        "Figure 11.9. Principle of operation of a wire-conducting high-frequency level system. (a) An "
        "electrical pulse is generated at t\u2080 and a two-wire line guides the wave down. Wherever "
        "the surrounding permittivity \u03b5 changes, part of the wave is sharply reflected back to "
        "the sensor at t\u2081; the wave runs on to the interface between the two liquids, reflects a "
        "second time at t\u2082, and a third time at the end of the line. (b) The delays 2t\u2081, "
        "2t\u2082, 2t\u2083 give the positions of the interfaces relative to the end of the line, "
        "which serves as the reference. The polarity inverts on reflection from a lower to a higher "
        "permittivity. The time scale is arbitrary.",
        "Hai phần: (a) bồn chứa hai lớp chất lỏng, đầu đo TDR trên nóc với hai sợi dây song song "
        "thả xuống gần đáy, các mốc t\u2081 ở mặt thoáng, t\u2082 ở mặt phân cách, t\u2083 ở đầu "
        "dây; (b) dấu vết xung theo thời gian với xung phát tại t\u2080 và ba xung phản xạ tại "
        "2t\u2081, 2t\u2082, 2t\u2083, hai xung đầu cực tính âm và xung cuối cực tính dương.",
        "Two parts: (a) a tank with two liquid layers and a TDR head on the roof whose two parallel "
        "wires reach almost to the bottom, marked t\u2081 at the surface, t\u2082 at the interface and "
        "t\u2083 at the end of the line; (b) the echo trace with the launch pulse at t\u2080 and three "
        "reflections at 2t\u2081, 2t\u2082, 2t\u2083, the first two negative and the last positive.")


# ---------------------------------------------------------------- 11.10
def fig_11_10():
    """FMCW: the sweep and the differential frequency."""
    W, H = 680, 290
    b = []
    x0, x1, yb, yt = 84, 620, 236, 74

    b.append(_l(x0, 250, x1 + 20, 250, 1.1))
    b.append(_arrow(x0, 250, x0, yt - 12, 1.0))
    b.append(_t(x1 + 26, 254, "t", 9.0, "start", "#333", ital=True))
    b.append(_t(x0 - 10, yt - 4, "f", 9.0, "end", "#333", ital=True))

    def seg(xa, xb, ya, ybb):
        return _l(xa, ya, xb, ybb, 1.8, INK)

    # transmitted: three sweeps
    b.append(seg(104, 300, yb, yt))
    b.append(seg(300, 300, yt, yb))
    b.append(seg(300, 500, yb, yt))
    b.append(seg(500, 500, yt, yb))
    b.append(seg(500, 620, yb, 148))
    # received: the same, delayed
    b.append(seg(144, 340, yb, yt))
    b.append(seg(340, 340, yt, yb))
    b.append(seg(340, 540, yb, yt))
    b.append(seg(540, 540, yt, yb))
    b.append(seg(540, 620, yb, 176))

    b.append(_t(150, yt - 8, "TX", 8.2, "middle", "#111", True))
    b.append(_t(196, 210, "RX", 8.2, "middle", RED, True))

    # differential frequency at one instant
    b.append(_l(450, 124, 450, 158, 0.8, "#bbb", "3 3"))
    b.append(_dim(450, 124, 450, 158, 462, 145, "\u0394f", 8.4, "#a8322d"))
    b.append(_t(470, 112, "TX", 7.4, "start", "#111", True))
    b.append(_t(470, 172, "RX", 7.4, "start", RED, True))

    # sweep interval T
    b.append(_dim(300, 266, 500, 266, 400, 280, "T", 8.8, "#333"))
    b.append(_l(300, 250, 300, 272, 0.6, "#aaa", "3 3"))
    b.append(_l(500, 250, 500, 272, 0.6, "#aaa", "3 3"))

    # sweep amplitude F
    b.append(_dim(64, yb, 64, yt, 56, (yb + yt) / 2, "F", 8.8, "#333"))
    b.append(_l(84, yb, 70, yb, 0.6, "#aaa", "3 3"))
    b.append(_l(84, yt, 70, yt, 0.6, "#aaa", "3 3"))

    return _fig(
        svg(W, H, STY + "".join(b), "Đặc tính làm việc của radar FMCW"),
        "Hình 11.10. Đặc tính làm việc của radar FMCW. Tần số của bộ phát tăng tuyến tính theo thời "
        "gian trong một khoảng quét. Tín hiệu thu có cùng dạng nhưng bị trễ thời gian. Tại mọi điểm "
        "trên đoạn quét, hiệu tần số là hằng số và tỉ lệ với độ trễ. Thang thời gian và tần số là "
        "tuỳ ý.",
        "Figure 11.10. Operation of FMCW radar. The transmitter frequency rises linearly with time "
        "over a sweep. The received signal has the same shape but is delayed. At every point of the "
        "sweep the difference frequency is constant and proportional to the delay. Time and frequency "
        "scales are arbitrary.",
        "Đồ thị tần số theo thời gian: hai chuỗi đoạn dốc song song, chuỗi phát TX và chuỗi thu RX "
        "lệch sang phải; khoảng cách đứng giữa hai đoạn dốc là hiệu tần số \u0394f, khoảng ngang của "
        "một đoạn quét là T, biên độ quét là F.",
        "A frequency-versus-time plot: two parallel sawtooth traces, the transmitted TX and the "
        "delayed received RX; the vertical gap between them is the difference frequency \u0394f, the "
        "horizontal span of one sweep is T, and the sweep height is F.")


# ---------------------------------------------------------------- 11.11
def fig_11_11():
    """FMCW radar block diagram."""
    W, H = 680, 300
    b = []
    blocks = [
        (56, 96, 78, 48, "VCO", "b\u1ed9 dao \u0111\u1ed9ng"),
        (166, 96, 78, 48, "amp", "khu\u1ebfch \u0111\u1ea1i"),
        (276, 96, 90, 48, "coupler", "\u0111\u1ecbnh h\u01b0\u1edbng"),
        (400, 96, 74, 48, "ant", "anten"),
    ]
    for x, y, w, h, lab, sub in blocks:
        b.append(_r(x, y, w, h, SAND, 1.1))
        b.append(_t(x + w / 2, y + 22, lab, 9.0, "middle", "#111", True))
        b.append(_t(x + w / 2, y + 37, sub, 6.6, "middle", "#666"))
    for x1, x2 in ((134, 166), (244, 276), (366, 400)):
        b.append(_arrow(x1, 120, x2, 120, 1.1))
    b.append(_arrow(474, 120, 502, 120, 1.1))
    b.append(_l(502, 120, 502, 92, 1.0, "#666"))
    b.append(_t(512, 88, "TX", 7.4, "start", "#555", True))

    # mixer row
    b.append(_r(276, 196, 90, 48, "#eef2f6", 1.1))
    b.append(_t(321, 218, "mixer", 9.0, "middle", "#111", True))
    b.append(_t(321, 233, "tr\u1ed9n", 6.6, "middle", "#666"))
    b.append(_r(400, 196, 74, 48, "#eef2f6", 1.1))
    b.append(_t(437, 218, "DRO", 9.0, "middle", "#111", True))
    b.append(_t(437, 233, "dao \u0111\u1ed9ng g\u1ed1m", 6.2, "middle", "#666"))
    b.append(_l(321, 144, 321, 196, 1.1))
    b.append(_arrow(321, 192, 321, 196, 1.0))
    b.append(_arrow(400, 220, 366, 220, 1.1))

    # processor
    b.append(_r(502, 176, 96, 68, SAND, 1.1))
    b.append(_t(550, 200, "\u00b5P", 10.0, "middle", "#111", True))
    b.append(_t(550, 216, "DSP + \u0111i\u1ec1u khi\u1ec3n", 6.6, "middle", "#666"))
    b.append(_t(550, 230, "L = c T \u0394f / 2F", 7.0, "middle", "#555"))
    # mixer output routed clear of the DRO block, then up into the processor
    b.append(_l(366, 220, 366, 264, 0.9, "#666"))
    b.append(_l(366, 264, 550, 264, 0.9, "#666"))
    b.append(_arrow(550, 260, 550, 248, 0.9, "#666"))
    # feedback to the VCO
    b.append(_p("M 550 176 L 550 62 L 95 62 L 95 96", "none", 0.9, "#666", "5 4"))
    b.append(_arrow(95, 90, 95, 96, 0.9, "#666", "5 4"))
    b.append(_t(330, 54, "qu\u00e9 t\u1ea7n s\u1ed1 tuy\u1ebfn t\u00ednh", 7.4, "middle", "#666"))

    return _fig(
        svg(W, H, STY + "".join(b), "Sơ đồ khối cơ bản của hệ radar FMCW"),
        "Hình 11.11. Sơ đồ khối cơ bản của một hệ radar FMCW: vi xử lý điều khiển bộ dao động điều "
        "khiển bằng điện áp (VCO) sao cho có được đoạn quét tần số mong muốn. Tín hiệu này được "
        "khuếch đại rồi đưa vào anten phát. Tần số tức thời phải được đo để bảo đảm độ tuyến tính "
        "tốt của đoạn quét; việc này thực hiện bằng cách đếm tần số sau khi trộn với tần số đã biết "
        "của một bộ dao động cộng hưởng điện môi (DRO). Một bộ ghép định hướng tách tín hiệu thu, "
        "trộn với tín hiệu phát rồi đưa vào vi xử lý.",
        "Figure 11.11. Basic block diagram of an FMCW radar system: a microprocessor controls a "
        "voltage-controlled oscillator (VCO) so as to obtain the wanted frequency sweep. The signal "
        "is amplified and fed to the transmitting antenna. The instantaneous frequency must be "
        "measured to guarantee sweep linearity, which is done by counting the frequency after mixing "
        "it with the known frequency of a dielectric resonance oscillator (DRO). A directional "
        "coupler decouples the received signal, which is mixed with the transmitted signal and "
        "processed by the microprocessor.",
        "Sơ đồ khối: VCO, bộ khuếch đại, bộ ghép định hướng, anten phát ở hàng trên; bộ trộn và DRO "
        "ở hàng dưới; vi xử lý ở cuối nhận tín hiệu trộn và có đường hồi tiếp quét tần số về VCO.",
        "Block diagram: VCO, amplifier, directional coupler and antenna on the top row; the mixer "
        "and the DRO below; the microprocessor at the end takes the mixed signal and feeds the sweep "
        "back to the VCO.")


# ---------------------------------------------------------------- 11.12
def fig_11_12():
    """Time of flight through the product, and the apparent bottom."""
    W, H = 680, 300
    b = []
    ax, ay, aw, ah = 110, 74, 190, 168
    surf = ay + 62
    bot = ay + ah
    b.append(_liq(ax + 3, surf, aw - 6, bot - surf - 3))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_r(ax + 58, ay - 24, 74, 24, SAND, 1.0))
    b.append(_t(ax + 95, ay - 9, "TX/RX", 8.2, "middle", "#111", True))

    cx0 = ax + 95
    # r1: surface reflection
    b.append(_arrow(cx0, ay - 2, cx0, surf - 2, 1.2, INK))
    b.append(_arrow(cx0, surf - 2, cx0, ay - 2, 1.2, RED, "4 3"))
    b.append(_t(cx0 + 8, surf - 10, "r\u2081", 8.4, "start", "#111", ital=True))
    # the part that enters the liquid
    b.append(_arrow(cx0, surf + 2, cx0, bot - 2, 1.2, "#7a8a99"))
    b.append(_arrow(cx0, bot - 2, cx0, surf + 2, 1.2, RED, "4 3"))
    b.append(_t(cx0 + 8, bot - 14, "r\u2082", 8.4, "start", "#111", ital=True))
    # apparent continuation
    b.append(_l(cx0, bot, cx0, bot + 46, 1.0, "#bbb", "4 3"))
    b.append(_l(ax - 6, bot, ax + aw + 6, bot, 1.4, "#555"))
    b.append(_l(ax - 6, bot + 46, ax + aw + 6, bot + 46, 0.9, "#bbb", "5 4"))

    b.append(_dim(ax - 40, ay, ax - 40, bot, ax - 48, (ay + bot) / 2, "h", 8.6))
    b.append(_dim(ax + aw + 18, ay, ax + aw + 18, surf, ax + aw + 26, (ay + surf) / 2, "d", 8.6))
    b.append(_dim(ax + aw + 18, surf, ax + aw + 18, bot, ax + aw + 26, (surf + bot) / 2, "L", 8.6))
    b.append(_dim(ax + aw + 66, ay, ax + aw + 66, bot + 46, ax + aw + 74, 176, "h\u1d65", 9.0,
                  "#a8322d"))
    # legend for the two bottom lines
    b.append(_l(452, 258, 478, 258, 1.6, "#555"))
    b.append(_t(484, 261, "\u0111\u00e1y th\u1ef1c", 8.0, "start", "#555"))
    b.append(_l(452, 280, 478, 280, 0.9, "#bbb", "5 4"))
    b.append(_t(484, 283, "\u0111\u00e1y bi\u1ec3u ki\u1ebfn", 8.0, "start", "#888"))

    return _fig(
        svg(W, H, STY + "".join(b), "Đo thời gian bay xuyên qua chất lỏng và đáy biểu kiến"),
        "Hình 11.12. Biểu diễn phép đo thời gian bay xuyên qua chất lỏng: sóng phản xạ một lần "
        "(r\u2081) tại mặt sản phẩm và lần thứ hai (r\u2082) tại đáy bồn. Do tốc độ truyền sóng "
        "trong chất lỏng nhỏ hơn, phản xạ r\u2082 hiện ra thấp hơn vị trí hình học của đáy. Từ độ "
        "lệch ấy tính được mức, xem phương trình 11.17 và 11.18.",
        "Figure 11.12. Time-of-flight measurement through the liquid: the wave reflects once "
        "(r\u2081) at the product surface and a second time (r\u2082) at the tank bottom. Because the "
        "wave travels more slowly in the liquid, the bottom echo appears below the geometric position "
        "of the bottom. The level follows from that shift; see Equations 11.17 and 11.18.",
        "Mặt cắt bồn chứa: đầu đo TX/RX trên nóc, tia sóng đi xuống, phản xạ r\u2081 tại mặt thoáng "
        "và r\u2082 tại đáy. Đáy thực vẽ bằng nét liền, đáy biểu kiến vẽ bằng nét đứt thấp hơn, với "
        "các kích thước h, d, L và chiều cao biểu kiến h\u1d65.",
        "A tank section: the TX/RX head on the roof, the ray travelling down, the reflection "
        "r\u2081 at the surface and r\u2082 at the bottom. The true bottom is a solid line, the "
        "apparent bottom a dashed line lower down, with the dimensions h, d, L and the apparent "
        "height h\u1d65.")


# ---------------------------------------------------------------- 11.13
def fig_11_13():
    """Capacitive probe and capacitive switch."""
    W, H = 680, 290
    b = []

    # (a) concentric electrode
    ax, ay, aw, ah = 84, 74, 200, 190
    surf = ay + 66
    b.append(_liq(ax + 3, surf, aw - 6, ay + ah - surf - 3))
    b.append(_tank(ax, ay, aw, ah))
    cx0 = ax + aw / 2
    b.append(_r(cx0 - 4, ay - 26, 8, ay + ah - ay + 16, "#555", 0.8))
    b.append(_r(cx0 - 9, ay - 26, 18, ay + ah - ay + 16, "#dfe4ea", 0.8, "#8a94a0"))
    b.append(_r(cx0 - 4, ay - 26, 8, ay + ah - ay + 16, "#555", 0.8))
    b.append(_t(cx0 + 16, ay + 26, "d\u2081", 7.6, "start", "#333", ital=True))
    b.append(_t(cx0 + 16, ay + 42, "d\u2082", 7.6, "start", "#333", ital=True))
    b.append(_t(ax + aw - 12, ay + 58, "d\u2083", 7.6, "end", "#333", ital=True))
    b.append(_l(cx0 + 4, ay + 22, cx0 + 13, ay + 22, 0.7, "#999"))
    b.append(_l(cx0 + 9, ay + 38, cx0 + 13, ay + 38, 0.7, "#999"))
    b.append(_l(ax + aw, ay + 54, ax + aw - 9, ay + 54, 0.7, "#999"))
    b.append(_t(cx0, 282, "(a)", 9.0, "middle", "#555"))

    # (b) switch through the wall
    bx = 420
    b.append(_l(bx, 74, bx, 264, 2.6))
    b.append(_l(bx + 26, 74, bx + 26, 264, 2.6))
    b.append(_liq(bx + 3, 150, 20, 112))
    b.append(_l(bx - 2, 150, bx + 28, 150, 1.0, "#5b7c99"))
    b.append(_l(bx, 74, bx + 26, 74, 2.6))
    b.append(_r(bx - 66, 128, 66, 44, SAND, 1.1))
    b.append(_t(bx - 33, 148, "C", 9.4, "middle", "#111", True))
    b.append(_t(bx - 33, 162, "c\u1ea3m bi\u1ebfn", 6.6, "middle", "#666"))
    b.append(_r(bx - 4, 142, 30, 16, "#9aa2ab", 1.0))
    b.append(_l(bx - 4, 150, bx - 24, 150, 1.4))
    b.append(_t(bx + 44, 200, "th\u00e0nh b\u1ed3n", 7.4, "start", "#666"))
    b.append(_l(bx + 40, 196, bx + 28, 180, 0.6, "#aaa"))
    b.append(_t(bx + 13, 282, "(b)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Nguyên lý cảm biến mức kiểu điện dung"),
        "Hình 11.13. Nguyên lý làm việc của thiết bị đo mức kiểu điện dung. (a) Một điện cực có "
        "cách điện nhô vào chất lỏng; điện dung giữa dây dẫn bên trong và thành bồn được đo. "
        "(b) Khi dùng làm công tắc mức điện dung, điện cực có thể được lắp thẳng vào thành bồn ở "
        "đúng vị trí cần báo.",
        "Figure 11.13. Principle of operation of a capacitance-type level device. (a) An insulated "
        "electrode protrudes into the liquid; the capacitance between the inner conductor and the "
        "tank wall is measured. (b) As a capacitance level switch the electrode can be mounted "
        "straight into the tank wall at the position where the alarm is wanted.",
        "Hai phần: (a) bồn hình trụ có điện cực thanh thẳng đứng ở giữa, gồm lõi dẫn và lớp cách "
        "điện, với ba bán kính d\u2081, d\u2082, d\u2083; (b) thành bồn cắt dọc có điện cực xuyên "
        "qua thành, hộp điện tử C ở phía ngoài.",
        "Two parts: (a) a cylindrical tank with a vertical rod electrode on the axis, an inner "
        "conductor inside an insulating sleeve, with the three radii d\u2081, d\u2082, d\u2083; "
        "(b) a section of the tank wall with the electrode passing through it and the electronics "
        "box C outside.")


# ---------------------------------------------------------------- 11.14
def fig_11_14():
    """Radiometric gaging: point source with rod detector, array with point detector."""
    W, H = 680, 290
    b = []

    def rays(sx, sy, targets):
        out = []
        for tx, ty in targets:
            out.append(_l(sx, sy, tx, ty, 0.7, "#c07a3a", "4 3"))
        return "".join(out)

    # (a) point source, rod detector
    ax, ay, aw, ah = 96, 86, 156, 172
    surf = ay + 64
    b.append(_liq(ax + 3, surf, aw - 6, ay + ah - surf - 3))
    b.append(_tank(ax, ay, aw, ah))
    b.append(_c(74, 150, 9, "#e8d7b8", 1.2, "#8a6d3b"))
    b.append(_c(74, 150, 3.2, "#8a6d3b", 0.8, "#8a6d3b"))
    b.append(_r(ax + aw + 12, 106, 12, 118, "#cbb894", 1.0, "#8a6d3b"))
    b.append(rays(83, 150, [(ax + aw + 12, 112), (ax + aw + 12, 150), (ax + aw + 12, 188)]))
    b.append(_t(74, 176, "Co-60", 6.8, "middle", "#8a6d3b"))
    b.append(_t(ax + aw + 18, 246, "detector", 6.8, "middle", "#666"))
    b.append(_t(174, 282, "(a)", 9.0, "middle", "#555"))

    # (b) source array, point detector
    bx, by, bw, bh = 404, 86, 152, 172
    b2 = by + 64
    b.append(_liq(bx + 3, b2, bw - 6, by + bh - b2 - 3))
    b.append(_tank(bx, by, bw, bh))
    for i, yy in enumerate((by + 46, by + 96, by + 146)):
        b.append(_c(bx - 26, yy, 7, "#e8d7b8", 1.2, "#8a6d3b"))
        b.append(_c(bx - 26, yy, 2.4, "#8a6d3b", 0.8, "#8a6d3b"))
        b.append(rays(bx - 19, yy, [(bx + bw + 12, by + 96)]))
    b.append(_c(bx + bw + 12, by + 96, 9, "#f2f2f2", 1.2, "#555"))
    b.append(_t(bx - 26, by + 176, "array", 6.8, "middle", "#8a6d3b"))
    b.append(_t(bx + bw + 12, 204, "detector", 6.8, "middle", "#666"))
    b.append(_t(480, 282, "(b)", 9.0, "middle", "#555"))

    return _fig(
        svg(W, H, STY + "".join(b), "Đo mức bức xạ: nguồn điểm với đầu dò thanh, và dãy nguồn với đầu dò điểm"),
        "Hình 11.14. Sơ đồ một thiết bị đo mức liên tục kiểu phóng xạ. Tia phát ra từ nguồn phóng xạ, "
        "xuyên qua thành bồn và bị chất lỏng làm suy giảm. Ở (a), một nguồn điểm được ghép với đầu "
        "dò dạng thanh (ví dụ thanh nhấp nháy); ở (b), một dãy nguồn được ghép với đầu dò điểm.",
        "Figure 11.14. A radiometric continuous level gage. The rays leave a radioactive source, pass "
        "through the tank walls and are attenuated by the liquid. In (a) a point source is combined "
        "with a rod detector (a scintillator rod, for instance); in (b) a source array is combined "
        "with a point detector.",
        "Hai bồn chứa: (a) nguồn điểm Co-60 bên trái, các tia chiếu ngang qua bồn tới một thanh đầu "
        "dò dài bên phải; (b) ba nguồn điểm xếp thành dãy bên trái, các tia hội về một đầu dò điểm "
        "bên phải.",
        "Two tanks: (a) a point Co-60 source on the left, rays crossing the tank to a long rod "
        "detector on the right; (b) three point sources stacked on the left, their rays converging on "
        "a single point detector on the right.")


# ---------------------------------------------------------------- 11.15
def fig_11_15():
    """Vibrating fork switch."""
    W, H = 680, 240
    b = []
    cx0 = 300
    b.append(_r(cx0 - 46, 34, 92, 42, SAND, 1.1))
    b.append(_t(cx0, 60, "E", 10.0, "middle", "#111", True))
    # the two paddles, tapering
    b.append(_poly([(cx0 - 26, 76), (cx0 - 8, 76), (cx0 - 14, 186), (cx0 - 30, 186)],
                   "#d7dde4", 1.2, INK, True))
    b.append(_poly([(cx0 + 8, 76), (cx0 + 26, 76), (cx0 + 30, 186), (cx0 + 14, 186)],
                   "#d7dde4", 1.2, INK, True))
    # vibration arcs
    for sgn in (-1, 1):
        for k, r in enumerate((16, 24)):
            x = cx0 + sgn * (30 + k * 2)
            b.append(_p("M %s %s Q %s %s %s %s" % (_f(x), _f(110), _f(x + sgn * 12), _f(130),
                                                   _f(x), _f(150)), "none", 1.0, "#8a94a0"))
    b.append(_t(cx0, 208, "dao \u0111\u1ed9ng", 8.0, "middle", "#666"))
    # electronics link
    b.append(_l(cx0 + 46, 55, 432, 55, 1.1))
    b.append(_r(432, 32, 128, 46, "#eef2f6", 1.1))
    b.append(_t(496, 50, "LS", 8.8, "middle", "#111", True))
    b.append(_t(496, 64, "\u0111o t\u1ed5n hao c\u00f4ng su\u1ea5t", 6.8, "middle", "#666"))

    return _fig(
        svg(W, H, STY + "".join(b), "Kết cấu công tắc mức kiểu âm thoa rung"),
        "Hình 11.15. Kết cấu một công tắc mức kiểu rung. Công tắc phản ứng với sự thay đổi độ nhớt "
        "của sản phẩm — yếu tố làm tắt dần dao động của các cánh [6].",
        "Figure 11.15. Design of a vibrating level switch. The switch reacts to a change in product "
        "viscosity, which damps the vibration of the paddles [6].",
        "Hộp điện tử E ở trên, hai cánh hình âm thoa thon nhỏ dần thò xuống dưới, hai cung dao động "
        "hai bên mỗi cánh, đường dây nối sang hộp mạch điện tử đo tổn hao công suất.",
        "The electronics box E on top, two tapering tuning-fork paddles reaching down, vibration "
        "arcs on both sides of each paddle, and a lead to the electronics that measures the power "
        "loss.")


FIGURES = [fig_11_1, fig_11_2, fig_11_3, fig_11_4, fig_11_5, fig_11_6, fig_11_7,
           fig_11_8, fig_11_9, fig_11_10, fig_11_11, fig_11_12, fig_11_13, fig_11_14,
           fig_11_15]
