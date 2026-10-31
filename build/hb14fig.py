# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 14
(Angle Measurement). Chapter 14 has only three figures, all geometric line
diagrams: the vernier protractor (14.1), the sine bar (14.2) and the two-ball
taper measuring setup (14.3). Every function returns
(svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah14" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah14g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G))


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy - r * math.sin(a))


# ---------------------------------------------------------------- 14.1
def fig_14_1():
    o = [_defs()]
    cx, cy, R = 250, 250, 150
    # body of the protractor (semicircle band)
    o.append('<path d="M%s %s A %s %s 0 0 1 %s %s L%s %s A %s %s 0 0 0 %s %s Z" '
             'fill="#faf6ef" stroke="%s" stroke-width="1.4"/>'
             % (_f(cx - R), _f(cy), R, R, _f(cx + R), _f(cy), _f(cx + R - 22), _f(cy),
                R - 22, R - 22, _f(cx - R + 22), _f(cy), E))
    # main degree scale
    for d in range(0, 181, 10):
        p1 = _pt(cx, cy, R - 22, d)
        p2 = _pt(cx, cy, R - 30, d)
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
                 % (_f(p1[0]), _f(p1[1]), _f(p2[0]), _f(p2[1]), E))
        if d % 30 == 0:
            lp = _pt(cx, cy, R - 44, d)
            o.append(_lbl(lp[0], lp[1] + 4, str(d), "tb", "middle"))
    # blade pointing at ~35 deg
    bp = _pt(cx, cy, R + 28, 35)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3"/>'
             % (_f(cx), _f(cy), _f(bp[0]), _f(bp[1]), G))
    o.append(_lbl(bp[0] + 6, bp[1], "lưỡi (blade) ≈ 35°", "ts"))
    # vernier reading call-out
    bx, by = 440, 30
    o.append('<rect x="%s" y="%s" width="220" height="130" rx="6" fill="#fff" stroke="%s" stroke-width="1.2"/>' % (bx, by, S))
    o.append(_lbl(bx + 8, by + 16, "Phóng to vạch đọc (vernier)", "tb"))
    # main scale inside box
    my = by + 70
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (bx + 14, my, bx + 206, my, E))
    o.append(_lbl(bx + 14, my - 6, "35°", "ts", "middle"))
    o.append(_lbl(bx + 206, my - 6, "36°", "ts", "middle"))
    # main tick at +20' (4th vernier line) for alignment
    ax = bx + 14 + 150 * (20.0 / 60.0)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>' % (_f(ax), my - 5, _f(ax), my + 5, S))
    # vernier scale (12 divisions, each 5')
    vy = my + 16
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>' % (bx + 14, vy, bx + 206, vy, G))
    step = 150.0 / 12.0
    for i in range(13):
        x = bx + 14 + i * step
        col = G if i == 4 else E
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>' % (_f(x), vy, _f(x), vy + 6, col))
    o.append(_lbl(bx + 14 + 4 * step, vy + 22, "vạch thứ 4 trùng → +20′", "ts", "middle"))
    return _fig(
        svg(680, 290, "".join(o), "Thước đo góc có du xích (vernier protractor)"),
        "Hình 14.1 · Thước đo góc có du xích. Khi vạch 0 của du xích nằm bên phải vạch 0 của thước chính, "
        "dùng cạnh phải của du xích; tìm vạch du xích trùng khớp nhất với một vạch thước chính, đếm số vạch "
        "từ 0 đến đó (mỗi vạch = 5′). Trong ví dụ, vạch thứ tư trùng khớp, nên cộng 20′ vào số độ đọc được.",
        "Figure 14.1 · Vernier protractor. If the zero of the vernier is to the right of the main-scale zero, "
        "use the right side of the vernier; find the vernier line that best aligns with a main-scale line, "
        "count the lines from zero (each = 5′ of arc). In the example the fourth line aligns, adding 20′ "
        "to the indicated degrees.",
        "Thước bán nguyệt chia độ 0–180, lưỡi chỉ hướng ~35°, và một ô phóng to du xích: vạch thứ 4 của "
        "du xích trùng với vạch thước chính, ứng với 20′.",
        "A semicircular 0–180 protractor with a blade at about 35° and a zoomed vernier: the fourth vernier "
        "line aligns with a main-scale line, meaning +20′.")


# ---------------------------------------------------------------- 14.2
def fig_14_2():
    o = [_defs()]
    cy = 250
    L = (220, cy - 24)          # left roll rests on the reference line
    A = math.radians(22)
    D = 300.0
    H = D * math.sin(A)
    Rr = (L[0] + D, L[1] - H)  # right roll raised by H
    r = 24
    # reference line
    o.append('<line x1="90" y1="%s" x2="600" y2="%s" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>' % (cy, cy, S))
    o.append(_lbl(95, cy + 16, "mặt phẳng tham chiếu (nằm ngang)", "ts"))
    # gage blocks under the right roll
    gb = Rr[1] + r
    o.append('<rect x="%s" y="%s" width="48" height="%s" fill="#faf6ef" stroke="%s" stroke-width="1.4"/>'
             % (_f(Rr[0] - 24), _f(gb), _f(cy - gb), E))
    o.append(_lbl(Rr[0] + 34, (gb + cy) / 2.0, "thước cữ gage blocks H", "ts"))
    # the sine bar (thick line between roll centers)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="11" stroke-linecap="round"/>'
             % (_f(L[0]), _f(L[1]), _f(Rr[0]), _f(Rr[1]), E))
    # rolls
    for c in (L, Rr):
        o.append('<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="2"/>' % (_f(c[0]), _f(c[1]), r, G))
    o.append(_lbl(L[0] - 30, L[1] - r - 8, "con lăn (rolls)", "ts"))
    o.append(_lbl((L[0] + Rr[0]) / 2.0, (L[1] + Rr[1]) / 2.0 - 18, "thanh sine (sine bar)", "tb"))
    # angle A
    a0 = _pt(L[0], L[1] - r, r + 24, 0)
    a1 = _pt(L[0], L[1] - r, r + 24, 22)
    o.append('<path d="M%s %s A %s %s 0 0 0 %s %s" fill="none" stroke="%s" stroke-width="1.2"/>'
             % (_f(a0[0]), _f(a0[1]), r + 24, r + 24, _f(a1[0]), _f(a1[1]), G))
    o.append(_lbl(L[0] + 52, L[1] - r - 14, "A", "tb"))
    # H dimension (vertical, right)
    hd = Rr[0] + 70
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2" marker-start="url(#ah14)"/>'
             % (_f(hd), _f(cy), _f(hd), _f(gb), E))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>'
             % (_f(hd), _f(cy), _f(Rr[0]), _f(cy), S))
    o.append(_lbl(hd + 8, (cy + gb) / 2.0, "H", "tb"))
    # D dimension (horizontal, bottom)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2" marker-start="url(#ah14)" marker-end="url(#ah14)"/>'
             % (_f(L[0]), _f(cy + 34), _f(Rr[0]), _f(cy + 34), E))
    o.append(_lbl((L[0] + Rr[0]) / 2.0, cy + 46, "D (khoảng cách giữa 2 con lăn)", "tb", "middle"))
    # equation
    o.append(_lbl((L[0] + Rr[0]) / 2.0, cy - 70, "sin A = H / D", "tb", "middle"))
    return _fig(
        svg(680, 300, "".join(o), "Thanh sine (sine bar) đo góc qua sin A = H/D"),
        "Hình 14.2 · Thanh sine dùng kèm thước cữ chính xác đặt dưới một con lăn, nâng đầu đó lên một khoảng "
        "H bằng sin của góc cần đo nhân khoảng cách D giữa hai con lăn. Phương trình chủ đạo: sin A = H/D.",
        "Figure 14.2 · A sine bar is used with precision gage blocks placed under one of the cylindrical "
        "rolls, raising that end a distance H equal to the sine of the desired angle times the distance D "
        "between the rolls. The governing equation is sin A = H/D.",
        "Thanh hình chữ nhật có hai con lăn ở hai đầu, đầu phải kê bằng thước cữ cao H; góc A giữa thanh và "
        "mặt phẳng nằm ngang, sin A = H/D với D là khoảng cách giữa hai con lăn.",
        "A rectangular bar with two cylindrical rolls; the right roll is raised by gage blocks of height H, "
        "and sin A = H/D where D is the roll-center distance.")


# ---------------------------------------------------------------- 14.3
def fig_14_3():
    o = [_defs()]
    # tapered hole walls (top wide, bottom narrow)
    wl = (250, 90, 305, 300)   # left wall top->bottom
    wr = (430, 90, 375, 300)   # right wall top->bottom
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2"/>' % (wl[0], wl[1], wl[2], wl[3], E))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2"/>' % (wr[0], wr[1], wr[2], wr[3], E))
    # balls
    b1 = (340, 168, 42)   # larger (top)
    b2 = (340, 250, 24)   # smaller (bottom)
    for c in (b1, b2):
        o.append('<circle cx="%s" cy="%s" r="%s" fill="#faf6ef" stroke="%s" stroke-width="2"/>' % (c[0], c[1], c[2], G))
    # depth dimension lines on the right
    rx = 470
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>' % (wl[0] + 0, 90, rx, 90, S))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1" marker-start="url(#ah14)"/>'
             % (_f(rx), _f(90), _f(rx), _f(b1[1] - b1[2]), E))
    o.append(_lbl(rx + 8, (90 + b1[1] - b1[2]) / 2.0, "h₁", "tb"))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1" marker-start="url(#ah14)"/>'
             % (_f(rx), _f(b1[1] - b1[2]), _f(rx), _f(b2[1] - b2[2]), E))
    o.append(_lbl(rx + 8, (b1[1] - b1[2] + b2[1] - b2[2]) / 2.0, "h₂", "tb"))
    # ball diameters
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>'
             % (_f(b1[0] - b1[2]), _f(b1[1] + b1[2] + 10), _f(b1[0] + b1[2]), _f(b1[1] + b1[2] + 10), S))
    o.append(_lbl(b1[0], b1[1] + b1[2] + 24, "d₁", "tb", "middle"))
    o.append(_lbl(b2[0], b2[1] + b2[2] + 20, "d₂", "tb", "middle"))
    # half-angle phi at the bottom
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>'
             % (_f((wl[2] + wr[2]) / 2.0), _f(300), _f((wl[2] + wr[2]) / 2.0), _f(360), S))
    o.append(_lbl((wl[2] + wr[2]) / 2.0 + 10, 340, "φ (nửa góc côn)", "ts"))
    o.append(_lbl(250, 78, "lỗ côn (tapered hole)", "ts"))
    return _fig(
        svg(680, 360, "".join(o), "Đo góc côn bằng hai quả cầu (measuring tapers)"),
        "Hình 14.3 · Đo góc côn bằng hai quả cầu (hoặc chốt cỡ) có đường kính đã biết. Chọn hai quả cầu "
        "vừa khít lỗ, đo độ sâu đến đỉnh mỗi quả (h₁, h₂) từ cùng một mặt tham chiếu; cùng bán kính r₁, r₂ "
        "biết trước, áp dụng các hệ thức hình học để tính nửa góc côn φ.",
        "Figure 14.3 · Measuring a taper with two balls (or gage pins) of known diameter. Select balls that "
        "fit the hole, measure the depth to the top of each ball (h₁, h₂) from a common reference, and with "
        "the known radii r₁, r₂ apply the geometry shown to determine the taper half-angle φ.",
        "Lỗ côn hình phễu với hai quả cầu kích thước khác nhau, các đường kích thước độ sâu h₁, h₂ và "
        "đường kính d₁, d₂, nửa góc côn φ ở đáy.",
        "A funnel-shaped tapered hole with two balls of different sizes, depth dimensions h₁/h₂ and "
        "diameters d₁/d₂, and the taper half-angle φ at the bottom.")


# expose
FIGS = [fig_14_1, fig_14_2, fig_14_3]


def fig(n):
    return FIGS[n - 1]()
