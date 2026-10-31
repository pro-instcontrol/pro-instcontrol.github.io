# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 6 (Displacement Measurement).

Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
Curves are computed from the governing formulas, never sketched.
"""
import math
import re

from hbfig import Box, STYLE, _f, _fig, svg

INK = "#2a2a2a"
GOLD = "#b45309"
GREY = "#888"
FILL = "#f6e6c8"


# ---------------------------------------------------------------- helpers
def _rect(x, y, w, h, fill="#fff", sw=1.1, dash=""):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, INK, sw, d))


def _line(x1, y1, x2, y2, sw=1, dash="", color=INK):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _txt(x, y, s, size=8.5, anchor="middle", color="#111", weight=""):
    s = re.sub(r"<sub>(.*?)</sub>",
               r'<tspan baseline-shift="sub" font-size="0.72em">\1</tspan>', s)
    s = re.sub(r"<sup>(.*?)</sup>",
               r'<tspan baseline-shift="super" font-size="0.72em">\1</tspan>', s)
    w = ("font-weight:%s;" % weight) if weight else ""
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx Inter,Helvetica,sans-serif;'
            'fill:%s;%s">%s</text>' % (_f(x), _f(y), anchor, size, color, w, s))


def _arrow(x1, y1, x2, y2, sw=1.2, color=INK, dash=""):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s '
            'marker-end="url(#a6)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _defs():
    return ('<defs><marker id="a6" markerWidth="7" markerHeight="7" refX="5.5" refY="2.5" '
            'orient="auto"><path d="M0,0 L5.5,2.5 L0,5 Z" fill="%s"/></marker>'
            '<pattern id="h6" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="#9a9a9a" stroke-width="0.7"/></pattern></defs>' % INK)


def _hatch(x, y, w, h, step=7):
    """Diagonal hatching inside a rectangle (a resistive element)."""
    o = []
    n = int((w + h) / step)
    for i in range(n + 1):
        x1 = x + i * step
        x2 = x1 - h
        o.append(_line(max(x, x1), y, max(x, x2), y + h, sw=0.6, color=GREY))
    return "".join(o)


def _ring(cx, cy, r_in, r_out, fill="#e9e3d6"):
    """A filled ring drawn as two circles — no radial seam like _annulus."""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.1"/>'
            % (_f(cx), _f(cy), _f(r_out), fill, INK)
            + '<circle cx="%s" cy="%s" r="%s" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>'
            % (_f(cx), _f(cy), _f(r_in), INK))


def _annulus(cx, cy, r_in, r_out, a1, a2, fill=FILL):
    """Annular sector from angle a1 to a2 (degrees, SVG orientation)."""
    rad = math.radians
    p1 = (cx + r_out * math.cos(rad(a1)), cy + r_out * math.sin(rad(a1)))
    p2 = (cx + r_out * math.cos(rad(a2)), cy + r_out * math.sin(rad(a2)))
    p3 = (cx + r_in * math.cos(rad(a2)), cy + r_in * math.sin(rad(a2)))
    p4 = (cx + r_in * math.cos(rad(a1)), cy + r_in * math.sin(rad(a1)))
    large = 1 if abs(a2 - a1) > 180 else 0
    d = ("M%s %s A%s %s 0 %d 1 %s %s L%s %s A%s %s 0 %d 0 %s %s Z"
         % (_f(p1[0]), _f(p1[1]), _f(r_out), _f(r_out), large, _f(p2[0]), _f(p2[1]),
            _f(p3[0]), _f(p3[1]), _f(r_in), _f(r_in), large, _f(p4[0]), _f(p4[1])))
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="1.1"/>' % (d, fill, INK)


# ---------------------------------------------------------------- 6.1
def fig_6_1():
    o = [_defs()]
    # ---------------- (a) linear-motion pot, cut away
    o.append(_rect(30, 34, 250, 120, "#fdfdfd"))
    o.append(_rect(48, 52, 214, 18, FILL))
    o.append(_hatch(48, 52, 214, 18))
    o.append(_rect(48, 52, 214, 18, "none"))
    # wiper: a small triangle riding under the element
    o.append('<path d="M142 70 L158 70 L150 80 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (INK, INK))
    o.append(_line(150, 80, 150, 104, sw=1.4))
    o.append(_rect(142, 104, 16, 8, "#e8e8e8"))
    o.append(_line(150, 112, 150, 154, sw=1.6))
    # terminals
    for x, lab in ((48, "1"), (262, "3")):
        o.append(_line(x, 52, x, 34, sw=1.1))
        o.append(_txt(x, 30, lab, 8, weight="600"))
    o.append(_line(150, 104, 190, 104, sw=1.1))
    o.append(_txt(198, 107, "2", 8, anchor="start", weight="600"))
    o.append(_txt(150, 88, "chổi quét", 8, color=GOLD))
    o.append(_txt(96, 44, "phần tử điện trở", 8, color=GREY))
    o.append(_txt(150, 170, "trục chuyển động thẳng", 8, color=GREY))
    o.append(_txt(155, 24, "(a) dịch chuyển thẳng", 9, weight="600"))

    # ---------------- (b) rotary pot, cut away
    cx, cy = 440, 100
    o.append('<circle cx="%s" cy="%s" r="78" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>'
             % (_f(cx), _f(cy), INK))
    o.append(_annulus(cx, cy, 54, 68, -58, 238))
    o.append(_txt(cx, cy + 96, "vùng chết", 7.5, color=GREY))
    # wiper arm at 40 degrees
    a = math.radians(40)
    o.append(_line(cx, cy, cx + 54 * math.cos(a), cy + 54 * math.sin(a), sw=2))
    o.append('<circle cx="%s" cy="%s" r="9" fill="#e8e8e8" stroke="%s" stroke-width="1.1"/>'
             % (_f(cx), _f(cy), INK))
    o.append(_txt(cx + 74, cy - 46, "phần tử điện trở", 7.5, anchor="start", color=GREY))
    o.append(_line(cx + 54 * math.cos(a), cy + 54 * math.sin(a), cx + 78 * math.cos(a),
                   cy + 78 * math.sin(a), sw=1.1))
    o.append(_txt(cx + 84 * math.cos(a), cy + 84 * math.sin(a) + 3, "2", 8, anchor="start",
                  weight="600"))
    o.append(_txt(cx, cy + 4, "trục", 7.5, color=GREY))
    o.append(_txt(cx, 24, "(b) dịch chuyển góc", 9, weight="600"))

    return _fig(svg(560, 196, "".join(o), "Mặt cắt biến trở dịch chuyển thẳng và biến trở quay"),
                "Hình 6-1 · Mặt cắt tiêu biểu của biến trở dịch chuyển thẳng (a) và biến trở quay (b). "
                "Phần tử điện trở bị “chia” tại điểm tiếp xúc của chổi quét, nên điện áp ra tỉ lệ với vị trí. "
                "Ở biến trở quay, phần tử điện trở không khép kín vòng tròn nên luôn có một vùng chết.",
                "Figure 6.1 · Representative cutaways of linear-motion (a) and rotary (b) potentiometers. "
                "The resistive element is “divided” at the wiper contact, so the output voltage tracks the "
                "wiper position. A rotary element cannot close the full circle, so it always has a dead zone.",
                "Mặt cắt biến trở dịch chuyển thẳng và biến trở quay",
                "Cutaway of a linear and a rotary potentiometer")


def fig_6_2():
    o = [_defs()]
    # ---------------- (a) voltage divider
    o.append(_rect(70, 60, 150, 16, FILL))
    o.append(_rect(70, 60, 150, 16, "none"))
    o.append(_txt(70, 52, "1", 8, weight="600"))
    o.append(_txt(220, 52, "3", 8, weight="600"))
    o.append(_line(70, 60, 70, 40, sw=1.2))
    o.append(_line(220, 60, 220, 40, sw=1.2))
    # supply
    o.append(_line(70, 40, 145, 40, sw=1.2))
    o.append(_line(220, 40, 145, 40, sw=1.2))
    o.append('<circle cx="145" cy="40" r="12" fill="#fff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(145, 43, "v", 9))
    o.append(_txt(160, 36, "r", 6.5, anchor="start", color=GREY))
    o.append(_txt(145, 24, "nguồn chuẩn", 7.5, color=GREY))
    # wiper
    o.append('<path d="M145 76 L156 92 L134 92 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (INK, INK))
    o.append(_line(145, 76, 145, 76, sw=1))
    o.append(_txt(122, 90, "2", 8, anchor="end", weight="600"))
    o.append(_line(145, 92, 145, 128, sw=1.2))
    o.append(_line(145, 128, 300, 128, sw=1.2))
    # load
    o.append(_rect(292, 140, 16, 46, "#fff"))
    o.append(_line(145, 128, 145, 186, sw=1.2))
    o.append(_line(145, 186, 292, 186, sw=1.2))
    o.append(_line(300, 186, 300, 186, sw=1.2))
    o.append(_txt(316, 166, "R", 9, anchor="start"))
    o.append(_txt(324, 170, "L", 6.5, anchor="start", color=GREY))
    o.append(_txt(300, 132, "v", 9))
    o.append(_txt(307, 136, "o", 6.5, anchor="start", color=GREY))
    o.append(_txt(232, 112, "R", 9, anchor="start"))
    o.append(_txt(240, 116, "P", 6.5, anchor="start", color=GREY))
    o.append(_txt(160, 196, "(a) cầu phân áp", 9, weight="600"))

    # ---------------- (b) ideal output
    b = Box(280, 196, (0, 1), (0, 1), pad=(46, 22, 16, 40))
    b.w, b.h = 280, 196
    b = Box(280, 196, (0, 1), (0, 1), pad=(48, 26, 18, 44))
    g = [b.axes("x / xP", "vo / vr", xt=[(0, "0"), (1, "1")], yt=[(0, "0"), (1, "1")])]
    g.append(b.curve([(k / 40.0, k / 40.0) for k in range(41)], "c1"))
    g.append(b.dot(0.62, 0.62, 3.2))
    g.append(b.label(0.62, 0.62, "điểm làm việc", "ts", "start", dx=6, dy=-6))
    g.append(_txt(140, 190, "(b) hàm truyền lí tưởng", 9, weight="600"))
    o.append('<g transform="translate(280,0)">%s</g>' % "".join(g))
    return _fig(svg(560, 212, "".join(o), "Sơ đồ cầu phân áp của biến trở và hàm truyền lí tưởng"),
                "Hình 6-2 · (a) Sơ đồ biểu diễn biến trở như một điện trở với mũi tên là chổi quét, mắc thành "
                "cầu phân áp — cấu hình ưu tiên cho đo lường chính xác. R<sub>P</sub> là tổng trở của biến trở, "
                "R<sub>L</sub> là trở tải, v<sub>r</sub> là điện áp nguồn và v<sub>o</sub> là điện áp ra. "
                "(b) Hàm ra tuyến tính lí tưởng, với x là vị trí chổi quét và x<sub>P</sub> là vị trí cực đại.",
                "Figure 6.2 · (a) A potentiometer drawn as a resistor with an arrow for the wiper, wired as a "
                "variable voltage divider — the preferred configuration for precision measurement. RP is the "
                "total resistance, RL the load, vr the supply and vo the output. (b) The ideal linear output "
                "function, where x is the wiper position and xP its maximum.",
                "Cầu phân áp của biến trở và hàm truyền lí tưởng",
                "Potentiometer voltage divider and its ideal transfer function")


def fig_6_3():
    b = Box(560, 250, (0, 1), (0, 1), pad=(56, 24, 24, 46))
    o = [b.axes("x / xP", "vo / vr", xt=[(0, "0"), (0.25, "0,25"), (0.5, "0,5"), (0.75, "0,75"),
                                         (1, "1")], yt=[(0, "0"), (1, "1")])]
    # best-fit straight line through the actual curve
    o.append(b.curve([(0, 0.035), (1, 0.965)], "c3"))
    # actual output: slightly S-shaped, as a real pot behaves near the ends
    pts = []
    for i in range(61):
        k = i / 60.0
        v = k - 0.055 * math.sin(2 * math.pi * k) * 0.55
        pts.append((k, v))
    o.append(b.curve(pts, "c1"))
    # maximum deviation markers
    k0 = 0.25
    v_act = k0 - 0.055 * math.sin(2 * math.pi * k0) * 0.55
    v_fit = 0.035 + k0 * 0.93
    o.append(_line(b.x(k0), b.y(v_act), b.x(k0), b.y(v_fit), sw=1.2, color=GOLD))
    o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (_f(b.x(k0)), _f(b.y(v_act)), GOLD))
    o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (_f(b.x(k0)), _f(b.y(v_fit)), GREY))
    o.append(b.label(k0, v_fit, "đường thẳng khớp nhất", "ts", "start", dx=10, dy=-8))
    o.append(b.label(k0, (v_act + v_fit) / 2, "độ lệch cực đại", "t", "start", dx=10, dy=22))
    o.append(b.label(0.6, 0.60, "hàm ra thực", "t", "start", dx=4, dy=-8))
    return _fig(svg(560, 250, "".join(o), "Độ tuyến tính độc lập của biến trở"),
                "Hình 6-3 · Độ tuyến tính độc lập là mức lệch cực đại của hàm ra thực so với đường thẳng khớp "
                "nhất. Đường thẳng này được chọn sao cho sai số tuyến tính trên tập điểm lấy mẫu là nhỏ nhất, "
                "không nhất thiết phải đo trên toàn dải của biến trở.",
                "Figure 6.3 · Independent linearity is the maximum amount by which the actual output function "
                "deviates from a line of best fit — the line chosen to minimise the linearity error over the "
                "sampled points, not necessarily over the full range of the pot.",
                "Độ tuyến tính độc lập của biến trở",
                "Independent linearity of a potentiometer")


def fig_6_4():
    b = Box(560, 260, (0, 1), (0, 1), pad=(58, 24, 150, 46))
    o = [b.axes("x / xP", "vo / vr", xt=[(0, "0"), (0.5, "0,5"), (1, "1")], yt=[(0, "0"), (1, "1")])]

    def curve_for(n):
        pts = []
        for i in range(81):
            k = i / 80.0
            if n is None:
                v = k
            else:
                v = k / (1.0 + k * (1 - k) / n)
            pts.append((k, v))
        return pts

    series = [(None, "c3", "R", "L", "/R", "P", " = ∞"),
              (10, "c1", "R", "L", "/R", "P", " = 10"),
              (1, "c2", "R", "L", "/R", "P", " = 1"),
              (0.1, "c3", "R", "L", "/R", "P", " = 0,1")]
    for i, (n, cls, *_rest) in enumerate(series):
        o.append(b.curve(curve_for(n), cls if n != 0.1 else "c3"))
    # legend at the right, outside the plot
    lx = b.l + b.pw + 16
    for i, (n, _cls, a, bb, c, d, tail) in enumerate(series):
        y = 62 + i * 30
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.8"%s/>'
                 % (_f(lx), _f(y), _f(lx + 22), _f(y), INK,
                    ' stroke-dasharray="5 4"' if n in (None, 0.1) else ""))
        lab = ("∞" if n is None else ("0,1" if n == 0.1 else str(n)))
        o.append(_txt(lx + 28, y + 3, "R<sub>L</sub>/R<sub>P</sub> = %s" % lab, 8, anchor="start"))
    o.append(_txt(lx, 42, "tải càng nhẹ", 7.5, anchor="start", color=GREY))
    o.append(_txt(lx, 196, "tải càng nặng", 7.5, anchor="start", color=GREY))
    o.append(_txt(b.l + b.pw / 2, 226, "độ lệch tăng khi tải nặng, lớn nhất ở giữa dải", 8, color=GREY))
    return _fig(svg(560, 260, "".join(o), "Ảnh hưởng của tải đến độ tuyến tính của biến trở"),
                "Hình 6-4 · Độ tuyến tính chịu ảnh hưởng lớn của tỉ số giữa trở tải R<sub>L</sub> và tổng trở "
                "biến trở R<sub>P</sub>. Bốn đường cong được tính từ công thức (6.1); sai số do tải lớn nhất ở "
                "giữa dải và bằng không ở hai đầu. Giữ R<sub>L</sub>/R<sub>P</sub> ≥ 10 thì sai số do tải dưới "
                "khoảng 1 % toàn thang.",
                "Figure 6.4 · Linearity is greatly influenced by the ratio of load resistance RL to "
                "potentiometer resistance RP. The four curves are computed from Equation 6.1; the loading error "
                "peaks at mid-travel and vanishes at both ends. Keeping RL/RP ≥ 10 holds it below about 1 % of "
                "full-scale output.",
                "Ảnh hưởng của tải đến độ tuyến tính của biến trở",
                "Effect of load resistance on potentiometer linearity")


def fig_6_5():
    o = [_defs()]
    # ---------------- (a) bushing mount
    o.append(_txt(150, 20, "(a) lắp kiểu ống lót", 9, weight="600"))
    o.append(_rect(40, 62, 220, 14, "#e8e8e8"))          # panel
    o.append(_txt(40, 92, "tấm lắp", 7.5, anchor="start", color=GREY))
    # threaded sleeve through the hole
    o.append(_rect(132, 40, 36, 58, "#fff"))
    for i in range(7):
        y = 44 + i * 8
        o.append(_line(132, y, 168, y + 4, sw=0.7, color=GREY))
    o.append(_txt(150, 34, "ống ren", 7.5, color=GOLD))
    # pot body behind the panel
    o.append(_rect(104, 76, 92, 52, "#fdfdfd"))
    o.append(_txt(150, 106, "thân biến trở", 7.5, color=GREY))
    o.append(_line(150, 76, 150, 62, sw=1.6))
    # nut and lock washer
    o.append(_rect(124, 96, 52, 12, "#dcdcdc"))
    o.append(_txt(196, 105, "đai ốc + vòng hãm", 7.5, anchor="start", color=GREY))
    # anti-rotation tab
    o.append(_rect(104, 62, 10, 14, "#dcdcdc"))
    o.append(_txt(70, 132, "chốt chống xoay", 7.5, anchor="middle", color=GREY))
    o.append(_line(109, 69, 92, 124, sw=0.8, dash="3 3", color=GREY))

    # ---------------- (b) servo mount
    o.append(_txt(430, 20, "(b) lắp kiểu servo", 9, weight="600"))
    o.append(_rect(320, 62, 220, 14, "#e8e8e8"))
    o.append(_txt(320, 92, "tấm lắp", 7.5, anchor="start", color=GREY))
    # precision bore + flange
    o.append(_rect(392, 44, 76, 10, "#dcdcdc"))          # flange ring
    o.append(_rect(404, 54, 52, 30, "#fff"))             # spigot into the bore
    o.append(_txt(430, 36, "vành định vị", 7.5, color=GOLD))
    o.append(_rect(384, 76, 92, 52, "#fdfdfd"))
    o.append(_txt(430, 106, "thân biến trở", 7.5, color=GREY))
    o.append(_line(430, 76, 430, 54, sw=1.6))
    # clamps
    for x in (368, 476):
        o.append(_rect(x, 40, 16, 26, "#dcdcdc"))
        o.append(_line(x + 8, 40, x + 8, 30, sw=1))
    o.append(_txt(430, 140, "kẹp servo (vặn vít)", 7.5, color=GREY))
    return _fig(svg(560, 156, "".join(o), "Hai kiểu lắp biến trở quay: ống lót và servo"),
                "Hình 6-5 · Hai kiểu lắp biến trở quay thông dụng nhất: (a) lắp kiểu ống lót — chỉ cần khoan "
                "một lỗ, nhưng độ chính xác khi căn chỉnh kém; (b) lắp kiểu servo — vành định vị ăn khớp với "
                "lỗ doa chính xác, kẹp bằng hai kẹp servo, chính xác và dễ chỉnh nhưng tốn công gia công.",
                "Figure 6.5 · The two most common rotary pot mounts: (a) the bushing mount needs only a drilled "
                "hole but is awkward to align precisely; (b) the servo mount registers a machined flange in a "
                "precision-bored hole and clamps with servo clamps — accurate and easy to adjust, at the cost "
                "of precision machining.",
                "Hai kiểu lắp biến trở quay: ống lót và servo",
                "Bushing mount and servo mount for a rotary potentiometer")


def fig_6_6():
    o = [_defs()]
    cw, ch = 130, 104
    cells = [(0, 0, "(a) đai và puly"), (1, 0, "(b) thanh răng – bánh răng"),
             (2, 0, "(c) vít me"), (3, 0, "(d) tang quấn cáp"),
             (0, 1, "(e) cam"), (1, 1, "(f) bánh răng côn"),
             (2, 1, "(g) bánh răng trụ")]
    for col, row, lab in cells:
        ox, oy = 10 + col * cw, 10 + row * (ch + 26)
        o.append(_rect(ox, oy, cw - 8, ch, "#fdfdfd", sw=0.9))
        o.append(_txt(ox + (cw - 8) / 2, oy + ch + 15, lab, 8))
    # (a) belt and pulley
    o.append('<circle cx="52" cy="62" r="18" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    o.append('<circle cx="100" cy="62" r="10" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    o.append(_line(52, 44, 100, 52, sw=1.6))
    o.append(_line(52, 80, 100, 72, sw=1.6))
    # (b) rack and pinion
    o.append('<circle cx="150" cy="58" r="14" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    o.append(_rect(122, 72, 60, 8, "#e8e8e8"))
    for i in range(8):
        o.append(_line(124 + i * 7, 72, 124 + i * 7, 66, sw=0.8, color=GREY))
    o.append(_arrow(122, 92, 178, 92, sw=1))
    # (c) lead screw
    o.append(_rect(258, 58, 56, 8, "#e8e8e8"))
    for i in range(9):
        o.append(_line(260 + i * 6, 58, 264 + i * 6, 66, sw=0.8, color=GREY))
    o.append(_rect(272, 44, 14, 14, FILL))
    o.append(_arrow(258, 84, 312, 84, sw=1))
    # (d) cabled drum
    o.append('<circle cx="400" cy="62" r="16" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    o.append('<circle cx="400" cy="62" r="5" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_line(416, 62, 440, 62, sw=1.4))
    o.append(_arrow(418, 80, 440, 80, sw=1))
    # (e) cam
    o.append('<path d="M60 152 a18 18 0 1 1 26 14 a18 18 0 1 0 -26 -14 Z" fill="%s" stroke="%s" '
             'stroke-width="1.1"/>' % (FILL, INK))
    o.append('<circle cx="60" cy="166" r="4" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_line(86, 158, 110, 158, sw=1.2))
    # (f) bevel gears
    o.append('<path d="M176 148 L206 148 L206 176 L176 176 Z" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, INK))
    o.append('<path d="M186 176 L216 186 L216 196 L186 186 Z" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, INK))
    o.append(_line(191, 162, 191, 150, sw=1))
    # (g) spur gears
    o.append('<circle cx="296" cy="166" r="15" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    o.append('<circle cx="326" cy="166" r="15" fill="%s" stroke="%s" stroke-width="1.1"/>' % (FILL, INK))
    for i in range(12):
        a = math.radians(i * 30)
        o.append(_line(296 + 15 * math.cos(a), 166 + 15 * math.sin(a),
                       296 + 18 * math.cos(a), 166 + 18 * math.sin(a), sw=0.8))
        o.append(_line(326 + 15 * math.cos(a), 166 + 15 * math.sin(a),
                       326 + 18 * math.cos(a), 166 + 18 * math.sin(a), sw=0.8))
    return _fig(svg(540, 246, "".join(o), "Bảy cơ cấu mở rộng khả năng của biến trở"),
                "Hình 6-6 · Các cơ cấu mở rộng khả năng của biến trở chính xác: đai và puly (a), thanh răng – "
                "bánh răng (b), vít me (c), tang quấn cáp (d), cam (e), bánh răng côn (f) và bánh răng trụ (g). "
                "Mỗi cơ cấu đổi tỉ lệ, đổi loại chuyển động hoặc đưa biến trở ra xa nguồn chuyển động.",
                "Figure 6.6 · Mechanisms that extend a precision potentiometer’s capabilities: belts and pulleys "
                "(a), rack-and-pinion (b), lead-screws (c), cabled drums (d), cams (e), bevel gears (f) and spur "
                "gears (g). Each one rescales the motion, converts between linear and rotary, or moves the pot "
                "away from the motion source.",
                "Bảy cơ cấu mở rộng khả năng của biến trở",
                "Seven mechanisms that extend a potentiometer")


# ---------------------------------------------------------------- 6.2
def _coil(x, y, w, h, n=6, axis="v"):
    """A coil symbol: a stack of arcs."""
    o = []
    if axis == "v":
        step = h / float(n)
        for i in range(n):
            o.append('<path d="M%s %s q%s 0 %s %s" fill="none" stroke="%s" stroke-width="1.1"/>'
                     % (_f(x - 7), _f(y + i * step), _f(14), _f(14), _f(step), INK))
    return "".join(o)


def _sine(x0, y0, w, amp, cycles, phase=0.0, cls="c1", n=90):
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        pts.append((x0 + w * t, y0 - amp * math.sin(2 * math.pi * cycles * t + phase)))
    return '<path class="%s" d="M%s" fill="none"/>' % (
        cls, " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts))


def fig_6_7():
    o = [_defs()]
    # C-core with a coil on the left leg and an air gap at the top
    o.append('<path d="M60 40 H300 V150 H240 V70 H120 V150 H60 Z" fill="%s" stroke="%s" '
             'stroke-width="1.2"/>' % (FILL, INK))
    # air gap
    o.append(_rect(60, 34, 240, 8, "#fff"))
    o.append(_txt(180, 28, "khe hở không khí d", 8, color=GOLD))
    # coil
    for i in range(7):
        o.append('<path d="M120 %s q-16 0 -16 6" fill="none" stroke="%s" stroke-width="1.2"/>'
                 % (_f(76 + i * 10), INK))
    o.append(_txt(88, 168, "n vòng dây", 8, color=GREY))
    # flux arrow
    o.append('<path d="M180 96 H300" stroke="%s" stroke-width="1.4" stroke-dasharray="5 3" '
             'marker-end="url(#a6)" fill="none"/>' % GOLD)
    o.append(_txt(236, 90, "Φ", 10, color=GOLD))
    o.append(_txt(330, 60, "lõi sắt từ", 8, anchor="start", color=GREY))
    o.append(_line(320, 56, 302, 70, sw=0.8, color=GREY))
    o.append(_txt(330, 120, "mmf = ni", 9, anchor="start"))
    return _fig(svg(460, 180, "".join(o), "Mạch từ cơ bản của cảm biến cảm ứng"),
                "Hình 6-7 · Cảm biến cảm ứng cơ bản là một mạch từ gồm lõi sắt từ có cuộn dây quấn trên đó. Cuộn "
                "dây tạo sức từ động (mmf) đẩy từ thông Φ qua mạch từ và qua khe hở không khí. Khe hở làm từ trở "
                "tăng mạnh và từ thông giảm tương ứng, nên một thay đổi nhỏ của khe hở cho một thay đổi đo được "
                "của điện cảm.",
                "Figure 6.7 · A basic inductive sensor is a magnetic circuit: a ferromagnetic core with a coil "
                "wound on it. The coil is the source of magnetomotive force that drives flux through the core "
                "and the air gap. The gap raises the reluctance sharply and lowers the flux, so a small change "
                "in gap produces a measurable change in inductance.",
                "Mạch từ cơ bản của cảm biến cảm ứng",
                "Basic magnetic circuit of an inductive sensor")


def fig_6_8():
    o = [_defs()]
    # semicircular core
    o.append(_annulus(150, 130, 44, 62, 180, 360))
    o.append(_rect(96, 130, 108, 10, "#fff"))
    o.append(_txt(150, 92, "lõi bán nguyệt", 8, color=GREY))
    # coil on the core
    for i in range(6):
        o.append('<path d="M%s 96 q0 -10 8 -10" fill="none" stroke="%s" stroke-width="1.1"/>'
                 % (_f(178 + i * 9), INK))
    o.append(_txt(196, 78, "cuộn dây", 8, color=GREY))
    # armature plate
    o.append(_rect(96, 152, 108, 12, FILL))
    o.append(_txt(150, 178, "tấm phần ứng", 8, color=GREY))
    # gap
    o.append(_line(212, 140, 240, 140, sw=0.9))
    o.append(_line(212, 152, 240, 152, sw=0.9))
    o.append(_txt(246, 149, "d", 9, anchor="start", color=GOLD))
    o.append(_arrow(150, 190, 150, 172, sw=1))
    o.append(_txt(150, 204, "x", 9))
    return _fig(svg(460, 214, "".join(o), "Cảm biến từ trở biến thiên một cuộn dây"),
                "Hình 6-8 · Cảm biến dịch chuyển từ trở biến thiên một cuộn dây điển hình, gồm ba phần tử: lõi "
                "sắt từ hình vành bán nguyệt, khe hở không khí biến thiên và một tấm sắt từ. Từ trở của cuộn "
                "phụ thuộc một biến duy nhất là khe hở, và tăng phi tuyến khi khe hở tăng.",
                "Figure 6.8 · A typical single-coil variable-reluctance displacement sensor: a ferromagnetic "
                "core in the shape of a semicircular ring, a variable air gap, and a ferromagnetic plate. The "
                "reluctance depends on one variable only — the gap — and rises nonlinearly as the gap opens.",
                "Cảm biến từ trở biến thiên một cuộn dây",
                "Single-coil variable-reluctance sensor")


def fig_6_9():
    o = [_defs()]
    for cx in (110, 330):
        o.append(_rect(cx - 40, 40, 80, 90, FILL))
        o.append(_rect(cx - 40, 40, 80, 90, "none"))
        for i in range(5):
            o.append('<path d="M%s 52 q-14 0 -14 6" fill="none" stroke="%s" stroke-width="1.1"/>'
                     % (_f(cx - 40 + 2), INK) if False else "")
    # two E cores facing each other with an armature between
    o.append('<path d="M40 40 H96 V58 H64 V76 H96 V94 H64 V112 H96 V130 H40 Z" fill="%s" stroke="%s" '
             'stroke-width="1.2"/>' % (FILL, INK))
    o.append('<path d="M400 40 H344 V58 H376 V76 H344 V94 H376 V112 H344 V130 H400 Z" fill="%s" '
             'stroke="%s" stroke-width="1.2"/>' % (FILL, INK))
    o.append(_rect(190, 60, 60, 50, "#e8e8e8"))
    o.append(_txt(220, 90, "phần ứng", 8))
    o.append(_txt(220, 126, "2d", 9, color=GOLD))
    o.append(_line(150, 60, 250, 60, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(150, 110, 250, 110, sw=0.8, dash="3 3", color=GREY))
    o.append(_txt(120, 34, "cuộn 1", 8, color=GREY))
    o.append(_txt(320, 34, "cuộn 2", 8, color=GREY))
    o.append(_arrow(220, 152, 220, 134, sw=1))
    o.append(_txt(220, 166, "x", 9))
    return _fig(svg(460, 176, "".join(o), "Cảm biến từ trở vi sai biến thiên"),
                "Hình 6-9 · Cảm biến từ trở vi sai gồm một phần ứng chuyển động giữa hai lõi giống nhau, cách "
                "nhau một khoảng cố định. Phần ứng dịch trong khe hở theo đầu vào cơ, làm thay đổi từ trở của "
                "cuộn 1 và cuộn 2, nhờ đó khắc phục được tính phi tuyến cố hữu của cảm biến một cuộn.",
                "Figure 6.9 · A variable-differential reluctance sensor: an armature moves between two identical "
                "cores held a fixed distance apart. The armature shifts in the gap with the mechanical input and "
                "changes the reluctance of coils 1 and 2 — which is how the arrangement escapes the nonlinearity "
                "inherent in the single-coil sensor.",
                "Cảm biến từ trở vi sai biến thiên",
                "Variable-differential reluctance sensor")


def fig_6_10():
    o = [_defs()]
    # two E frames, one inverted, with the core between them
    for y0, flip in ((46, 1), (120, -1)):
        o.append('<path d="M70 %s H200 V%s H150 V%s H120 V%s H150 V%s H70 Z" fill="%s" stroke="%s" '
                 'stroke-width="1.2"/>'
                 % (_f(y0), _f(y0 + 14 * flip), _f(y0 + 28 * flip), _f(y0 + 46 * flip),
                    _f(y0 + 60 * flip), FILL, INK))
    o.append(_rect(196, 74, 34, 60, "#e8e8e8"))
    o.append(_txt(258, 108, "lõi sắt", 8, anchor="start", color=GREY))
    o.append(_line(232, 104, 250, 106, sw=0.8, color=GREY))
    o.append(_txt(135, 40, "khung chữ E trên", 8, color=GREY))
    o.append(_txt(135, 196, "khung chữ E dưới", 8, color=GREY))
    o.append(_arrow(213, 160, 213, 142, sw=1))
    o.append(_txt(226, 158, "x", 9, anchor="start"))
    return _fig(svg(460, 206, "".join(o), "Cảm biến vi sai thương mại kiểu hai khung chữ E"),
                "Hình 6-10 · Một cảm biến vi sai thương mại điển hình. Lõi sắt nằm giữa hai khung chữ E. Mọi "
                "chuyển động của lõi làm tăng khe hở phía này và giảm khe hở phía kia, khiến từ trở thay đổi và "
                "cảm ứng điện áp lớn hơn ở một phía. Chuyển động ngược lại đảo tác dụng với độ lệch pha 180° tại "
                "điểm không.",
                "Figure 6.10 · A typical commercial variable-differential sensor. The iron core sits halfway "
                "between two E-shaped frames. Any motion of the core opens the gap on one side and closes it on "
                "the other, so one coil sees more induced voltage than the other; motion the other way reverses "
                "the action with a 180° phase shift at null.",
                "Cảm biến vi sai thương mại kiểu hai khung chữ E",
                "Commercial variable-differential sensor with two E frames")


def fig_6_11():
    o = [_defs()]
    # toothed wheel
    cx, cy, R = 110, 100, 52
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), _f(R), FILL, INK))
    for i in range(12):
        a = math.radians(i * 30)
        o.append('<path d="M%s %s L%s %s" stroke="%s" stroke-width="7" stroke-linecap="butt"/>'
                 % (_f(cx + R * math.cos(a)), _f(cy + R * math.sin(a)),
                    _f(cx + (R + 12) * math.cos(a)), _f(cy + (R + 12) * math.sin(a)), FILL))
    o.append('<circle cx="%s" cy="%s" r="6" fill="#fff" stroke="%s" stroke-width="1.1"/>'
             % (_f(cx), _f(cy), INK))
    o.append(_txt(110, 178, "bánh răng từ tính, m răng", 8, color=GREY))
    # pole piece + magnet + coil
    o.append(_rect(186, 92, 40, 16, "#e8e8e8"))
    o.append(_txt(206, 86, "cực từ", 7.5, color=GREY))
    o.append(_rect(226, 92, 70, 16, "#dcdcdc"))
    o.append(_txt(261, 86, "nam châm vĩnh cửu", 7.5, color=GREY))
    for i in range(6):
        o.append('<path d="M%s 108 q0 12 8 12" fill="none" stroke="%s" stroke-width="1.1"/>'
                 % (_f(300 + i * 10), INK))
    o.append(_txt(330, 138, "cuộn dây", 7.5, color=GREY))
    o.append(_txt(430, 112, "e", 9, anchor="middle", color=GOLD))
    return _fig(svg(460, 190, "".join(o), "Máy phát tốc độ từ trở biến thiên"),
                "Hình 6-11 · Máy phát tốc độ từ trở biến thiên dựa trên định luật cảm ứng điện từ Faraday: một "
                "bánh răng sắt từ gắn trên trục quay và một cuộn dây quấn trên nam châm vĩnh cửu, nối dài bằng "
                "cực từ sắt non. Bánh răng quay sát cực từ làm từ thông móc vòng cuộn dây thay đổi, cảm ứng ra "
                "một điện áp gần dạng xung vuông có tần số tỉ lệ với tốc độ quay và số răng.",
                "Figure 6.11 · A variable-reluctance tachogenerator works on Faraday’s law: a ferromagnetic "
                "toothed wheel on the rotating shaft, and a coil wound on a permanent magnet extended by a soft "
                "iron pole piece. The wheel turning close to the pole changes the flux linked by the coil, "
                "inducing an output close to a square wave whose frequency depends on speed and tooth count.",
                "Máy phát tốc độ từ trở biến thiên",
                "Variable-reluctance tachogenerator")


def fig_6_12():
    o = [_defs()]
    cx, cy = 150, 100
    o.append('<circle cx="%s" cy="%s" r="66" fill="#fdfdfd" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<circle cx="%s" cy="%s" r="30" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), FILL, INK))
    for i, lab in enumerate(("1", "2", "3", "4")):
        a = math.radians(-90 + i * 90)
        x, y = cx + 48 * math.cos(a), cy + 48 * math.sin(a)
        o.append(_rect(x - 13, y - 13, 26, 26, "#e8e8e8"))
        o.append(_txt(x, y + 4, lab, 9, weight="600"))
    o.append(_txt(cx, cy + 4, "rôto", 8, color=GREY))
    o.append(_txt(150, 190, "bốn cuộn dây trên stato", 8, color=GREY))
    o.append(_txt(300, 96, "tại vị trí không:", 8, anchor="start", color=GREY))
    o.append(_txt(300, 112, "e₁ + e₃ = e₂ + e₄", 9, anchor="start"))
    o.append(_txt(300, 132, "→ e", 9, anchor="start", color=GOLD))
    o.append(_txt(322, 136, "o", 6.5, anchor="start", color=GOLD))
    o.append(_txt(300, 148, "= 0", 9, anchor="start", color=GOLD))
    return _fig(svg(460, 200, "".join(o), "Cảm biến từ trở vi sai kiểu microsyn"),
                "Hình 6-12 · Microsyn là một cảm biến từ trở biến thiên gồm rôto sắt từ và stato mang bốn cuộn "
                "dây. Các cuộn được đấu sao cho tại vị trí không, điện áp cảm ứng ở cuộn 1 và 3 cân bằng với "
                "điện áp ở cuộn 2 và 4. Rôto quay một chiều làm tăng từ trở hai cuộn đối diện và giảm ở hai cuộn "
                "kia, cho điện áp ra tổng e<sub>o</sub>; quay chiều ngược lại đảo tác dụng với độ lệch pha 180°.",
                "Figure 6.12 · A microsyn is a variable-reluctance transducer: a ferromagnetic rotor inside a "
                "stator carrying four coils. The coils are connected so that at the null position the voltages "
                "induced in 1 and 3 balance those in 2 and 4. Turning the rotor one way raises the reluctance of "
                "one opposite pair and lowers the other, giving a net output eo; turning it the other way "
                "reverses the effect with a 180° phase shift.",
                "Cảm biến từ trở vi sai kiểu microsyn",
                "Microsyn variable-reluctance transducer")


def fig_6_13():
    o = [_defs()]
    cx, cy = 130, 96
    o.append('<circle cx="%s" cy="%s" r="64" fill="#fdfdfd" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<circle cx="%s" cy="%s" r="34" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), FILL, INK))
    for i in range(3):
        a = math.radians(-90 + i * 120)
        x, y = cx + 49 * math.cos(a), cy + 49 * math.sin(a)
        o.append(_rect(x - 11, y - 11, 22, 22, "#e8e8e8"))
        o.append(_txt(x, y + 4, "S%d" % (i + 1), 7.5))
    o.append(_line(cx - 22, cy - 8, cx + 22, cy + 8, sw=1.4))
    o.append(_txt(cx, cy + 4, "R", 8))
    o.append(_txt(130, 186, "stato 3 cuộn — rôto 1 cuộn", 8, color=GREY))
    o.append(_txt(300, 78, "điện áp ba pha", 9, anchor="start", weight="600"))
    o.append(_txt(300, 96, "định vị góc rôto", 8, anchor="start", color=GREY))
    o.append(_txt(300, 118, "v₁ ∝ sin θ", 9, anchor="start"))
    o.append(_txt(300, 134, "v₂ ∝ sin(θ − 120°)", 9, anchor="start"))
    o.append(_txt(300, 150, "v₃ ∝ sin(θ + 120°)", 9, anchor="start"))
    return _fig(svg(460, 196, "".join(o), "Cấu tạo synchro kiểu động cơ cảm ứng rôto dây quấn"),
                "Hình 6-13 · Synchro có cấu tạo tương tự động cơ cảm ứng rôto dây quấn. Rôto quay làm thay đổi "
                "hỗ cảm giữa cuộn rôto và ba cuộn stato; ba điện áp lấy từ các cuộn stato xác định vị trí góc "
                "của rôto. Synchro chủ yếu dùng để đo góc và thường có mặt trong kỹ thuật điều khiển như một bộ "
                "phận của hệ servo, máy công cụ, anten…",
                "Figure 6.13 · A synchro is built like a wound-rotor induction motor. Rotating the rotor changes "
                "the mutual inductance between the rotor coil and the three stator coils, and the three stator "
                "voltages define the rotor’s angular position. Synchros are used mainly for angle measurement, "
                "and turn up throughout control engineering inside servomechanisms, machine tools and antennas.",
                "Cấu tạo synchro kiểu động cơ cảm ứng rôto dây quấn",
                "Synchro construction")


def fig_6_14():
    o = [_defs()]
    # former with a centre-tapped winding and a plunger
    o.append(_rect(80, 44, 300, 26, "#fdfdfd"))
    for i in range(20):
        o.append('<path d="M%s 44 q0 26 0 26" fill="none" stroke="%s" stroke-width="1.1"/>'
                 % (_f(92 + i * 14), INK) if False else "")
    # draw the winding as a zig-zag
    pts = []
    for i in range(40):
        x = 90 + i * 7.2
        pts.append((x, 44 if i % 2 == 0 else 70))
    o.append('<path d="M%s" fill="none" stroke="%s" stroke-width="1.1"/>'
             % (" L".join("%s %s" % (_f(a), _f(b)) for a, b in pts), INK))
    o.append(_line(234, 44, 234, 34, sw=1.2))
    o.append(_txt(234, 28, "điểm giữa", 8, color=GREY))
    # plunger
    o.append(_rect(150, 74, 160, 14, FILL))
    o.append(_txt(230, 100, "lõi (plunger), chiều dài l", 8, color=GREY))
    o.append(_arrow(230, 122, 230, 106, sw=1))
    o.append(_txt(244, 120, "δl", 9, anchor="start"))
    o.append(_line(90, 82, 390, 82, sw=0.7, dash="3 3", color=GREY))
    o.append(_txt(90, 96, "cuộn dây quấn trên khuôn", 8, anchor="start", color=GREY))
    return _fig(svg(460, 140, "".join(o), "Cuộn cảm biến thiên tuyến tính kiểu ghép biến thiên"),
                "Hình 6-14 · Cuộn cảm biến thiên tuyến tính điển hình gồm một lõi sắt di động bên trong khuôn "
                "mang cuộn dây có điểm giữa. Lõi và hai cuộn có cùng chiều dài l. Khi lõi ở vị trí chuẩn, mỗi "
                "cuộn có điện cảm bằng nhau và bằng L; khi lõi dịch δl, các điện cảm đổi thành +δL và −δL, tạo "
                "ra điện áp ra trên cầu.",
                "Figure 6.14 · A typical linear variable inductor: a movable iron core inside a former carrying a "
                "centre-tapped winding. Core and coils share the same length l. At the reference position each "
                "coil has inductance L; moving the core by δl makes the inductances +δL and −δL, which is what "
                "the bridge turns into an output voltage.",
                "Cuộn cảm biến thiên tuyến tính kiểu ghép biến thiên",
                "Linear variable inductor with a variable coupling")


def fig_6_15():
    o = [_defs()]
    # (a) resistive bridge
    o.append(_txt(140, 20, "(a) cầu dùng điện trở", 9, weight="600"))
    o.append(_rect(60, 44, 160, 12, FILL))
    o.append(_txt(60, 38, "L+δL", 7.5, color=GREY))
    o.append(_txt(220, 38, "L−δL", 7.5, anchor="end", color=GREY))
    o.append(_line(140, 56, 140, 74, sw=1.2))
    o.append(_rect(60, 74, 56, 12, "#e8e8e8"))
    o.append(_rect(164, 74, 56, 12, "#e8e8e8"))
    o.append(_txt(88, 100, "R", 9))
    o.append(_txt(192, 100, "R", 9))
    o.append(_line(60, 86, 60, 112, sw=1.2))
    o.append(_line(220, 86, 220, 112, sw=1.2))
    o.append(_line(60, 112, 220, 112, sw=1.2))
    o.append(_line(140, 74, 140, 112, sw=1.2))
    o.append(_line(140, 112, 250, 112, sw=1.2))
    o.append(_txt(258, 116, "e", 9, anchor="start", color=GOLD))
    o.append(_txt(266, 120, "o", 6.5, anchor="start", color=GOLD))
    # (b) transformer bridge
    o.append(_txt(370, 20, "(b) cầu dùng biến áp", 9, weight="600"))
    o.append(_rect(290, 44, 160, 12, FILL))
    o.append(_line(370, 56, 370, 78, sw=1.2))
    o.append(_rect(300, 78, 40, 30, "#fff"))
    o.append(_rect(400, 78, 40, 30, "#fff"))
    for i in range(4):
        o.append('<path d="M%s 82 q0 8 6 8" fill="none" stroke="%s" stroke-width="1"/>'
                 % (_f(306 + i * 8), INK))
        o.append('<path d="M%s 82 q0 8 6 8" fill="none" stroke="%s" stroke-width="1"/>'
                 % (_f(406 + i * 8), INK))
    o.append(_line(290, 108, 370, 108, sw=1.2))
    o.append(_line(450, 108, 370, 108, sw=1.2))
    o.append(_line(370, 108, 370, 126, sw=1.2))
    o.append(_txt(378, 130, "e", 9, anchor="start", color=GOLD))
    o.append(_txt(386, 134, "o", 6.5, anchor="start", color=GOLD))
    o.append(_txt(370, 148, "hai cuộn thứ cấp có điểm giữa", 7.5, color=GREY))
    return _fig(svg(500, 158, "".join(o), "Cầu đo cho cuộn cảm biến thiên"),
                "Hình 6-15 · Hai cuộn của một cuộn cảm biến thiên thường được đặt thành hai nhánh của cầu, cùng "
                "hai điện trở cân bằng (a). Cầu được kích bằng xoay chiều 5–25 V, tần số 50 Hz – 5 kHz; ở tần số "
                "đã chọn, tổng trở bộ cảm biến tại điểm không được đặt trong khoảng 100–1000 Ω. Với cầu được "
                "chế tạo cẩn thận, điện áp ra là hàm tuyến tính của dịch chuyển trong một dải hạn chế. Muốn giảm "
                "tổn hao nhiệt trên điện trở, có thể dùng biến áp có điểm giữa làm một phần của cầu (b).",
                "Figure 6.15 · The two coils of a linear variable inductor usually form two arms of a bridge, "
                "with two equal balancing resistors (a). The bridge is excited at 5–25 V ac, 50 Hz – 5 kHz, and "
                "the transducer impedance at null is set to 100–1000 Ω at that frequency. Carefully built, the "
                "bridge output is a linear function of displacement over a limited range. To cut the heat "
                "dissipated in the resistors, centre-tapped transformers can replace them (b).",
                "Cầu đo cho cuộn cảm biến thiên",
                "Bridge circuit for a variable inductor")


def fig_6_16():
    o = [_defs()]
    cx, cy = 140, 96
    o.append('<circle cx="%s" cy="%s" r="60" fill="#fdfdfd" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<circle cx="%s" cy="%s" r="30" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), FILL, INK))
    # concentrated stator winding
    o.append('<path d="M140 36 a60 60 0 0 1 42 18 l-12 12 a44 44 0 0 0 -30 -13 Z" fill="#e8e8e8" '
             'stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(186, 52, "cuộn stato", 7.5, anchor="start", color=GREY))
    o.append('<path d="M140 96 L170 96" stroke="%s" stroke-width="3"/>' % INK)
    o.append(_txt(140, cy + 4, "rôto", 8, color=GREY))
    o.append(_txt(140, 186, "góc quay θ", 8, color=GREY))
    o.append(_txt(300, 78, "v", 9, anchor="start"))
    o.append(_txt(308, 82, "o", 6.5, anchor="start", color=GREY))
    o.append(_txt(300, 98, "∝ M(θ)", 9, anchor="start"))
    o.append(_txt(300, 120, "M ~ cos θ với cuộn tập trung", 7.5, anchor="start", color=GREY))
    o.append(_txt(300, 138, "tuyến tính 180° nếu cuộn rải", 7.5, anchor="start", color=GREY))
    return _fig(svg(500, 196, "".join(o), "Chiết áp cảm ứng kiểu cuộn tập trung"),
                "Hình 6-16 · Chiết áp cảm ứng là một cuộn cảm biến thiên kiểu quay với hai cuộn tập trung quấn "
                "trên stato và rôto. Cuộn rôto được kích bằng xoay chiều, cảm ứng điện áp sang cuộn stato. Biên "
                "độ điện áp ra phụ thuộc hỗ cảm giữa hai cuộn, mà hỗ cảm lại phụ thuộc góc quay. Với cuộn tập "
                "trung, biên độ biến thiên theo sin nên chỉ tuyến tính quanh vị trí không; cuộn rải được thiết "
                "kế cẩn thận cho phân bố tuyến tính trên 180°.",
                "Figure 6.16 · An induction potentiometer is a rotary variable inductor with two concentrated "
                "windings, one on the stator and one on the rotor. The rotor winding is excited with ac and "
                "induces voltage in the stator; the amplitude depends on the mutual inductance between them, "
                "which depends on the angle of rotation. With concentrated coils the amplitude varies "
                "sinusoidally, so linearity holds only near null; distributed coils give a linear distribution "
                "over 180°.",
                "Chiết áp cảm ứng kiểu cuộn tập trung",
                "Induction potentiometer")


def fig_6_17():
    o = [_defs()]
    # tubular former
    o.append(_rect(60, 58, 380, 56, "#fdfdfd"))
    o.append(_rect(60, 58, 380, 56, "none", dash="4 3"))
    # windings: S1 | P | S2
    def wind(x0, x1, lab):
        pts = []
        for i in range(int((x1 - x0) / 7)):
            pts.append((x0 + i * 7, 58 if i % 2 == 0 else 80))
        o.append('<path d="M%s" fill="none" stroke="%s" stroke-width="1.2"/>'
                 % (" L".join("%s %s" % (_f(a), _f(b)) for a, b in pts), INK))
        o.append(_txt((x0 + x1) / 2, 46, lab, 8.5, weight="600"))
    wind(76, 176, "cuộn thứ cấp 1")
    wind(200, 300, "cuộn sơ cấp")
    wind(324, 424, "cuộn thứ cấp 2")
    # core
    o.append(_rect(150, 128, 200, 14, FILL))
    o.append(_txt(250, 156, "lõi sắt từ (plunger)", 8, color=GREY))
    o.append(_line(150, 120, 150, 128, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(350, 120, 350, 128, sw=0.8, dash="3 3", color=GREY))
    o.append(_txt(250, 34, "trục ống sắt từ", 7.5, color=GREY))
    o.append(_arrow(250, 176, 250, 148, sw=1))
    o.append(_txt(266, 172, "x", 9, anchor="start"))
    return _fig(svg(500, 190, "".join(o), "Cấu tạo biến áp vi sai tuyến tính LVDT"),
                "Hình 6-17 · LVDT là một đầu đo cảm ứng thụ động gồm một cuộn sơ cấp đặt giữa hai cuộn thứ cấp "
                "giống nhau, quấn trên một ống lõi sắt từ. Khi lõi bên trong ống dịch chuyển, đường từ thông giữa "
                "sơ cấp và các thứ cấp thay đổi, cho đầu ra thứ cấp tỉ lệ với dịch chuyển. Hai cuộn thứ cấp được "
                "chế tạo càng giống nhau càng tốt: cùng kích thước, hình dạng và số vòng.",
                "Figure 6.17 · An LVDT is a passive inductive transducer: one primary winding between two "
                "identical secondary windings, all wound on a tubular ferromagnetic former. As the core inside "
                "the former moves, the magnetic paths from primary to secondaries change, so the secondary "
                "outputs track the movement. The two secondaries are made as identical as possible — equal size, "
                "shape and turns.",
                "Cấu tạo biến áp vi sai tuyến tính LVDT",
                "Linear variable-differential transformer construction")


def fig_6_18():
    o = [_defs()]
    # (a) circuit
    o.append(_txt(110, 18, "(a) sơ đồ đấu", 9, weight="600"))
    o.append(_rect(30, 40, 60, 40, FILL))
    o.append(_txt(60, 66, "S₁", 10))
    o.append(_rect(130, 40, 60, 40, FILL))
    o.append(_txt(160, 66, "S₂", 10))
    o.append(_line(30, 80, 30, 100, sw=1.1))
    o.append(_line(190, 80, 190, 100, sw=1.1))
    o.append(_line(30, 100, 190, 100, sw=1.1))
    o.append(_line(110, 100, 110, 116, sw=1.1))
    o.append(_txt(118, 120, "v", 9, anchor="start", color=GOLD))
    o.append(_txt(126, 124, "o", 6.5, anchor="start", color=GOLD))
    o.append(_txt(60, 34, "v₁", 8, color=GREY))
    o.append(_txt(160, 34, "v₂", 8, color=GREY))
    # (b) waveforms at null
    o.append(_txt(300, 18, "(b) tại vị trí không", 9, weight="600"))
    o.append(_line(220, 72, 430, 72, sw=0.8, color=GREY))
    o.append(_sine(220, 72, 200, 24, 1.5, 0.0, "c1"))
    o.append(_sine(220, 72, 200, 24, 1.5, 0.0, "c3"))
    o.append(_txt(230, 40, "v₁ = v₂", 8, anchor="start", color=GREY))
    # (c) output vs core position
    b = Box(240, 150, (-1, 1), (-1, 1), pad=(34, 18, 14, 34))
    g = [b.axes("x", "vo", xt=[(-1, "−x"), (0, "0"), (1, "+x")], yt=[])]
    g.append(b.curve([(-1, 0.85), (-0.5, 0.42), (0, 0), (0.5, -0.42), (1, -0.85)], "c2"))
    g.append(_line(b.x(0), b.y(-1), b.x(0), b.y(1), sw=0.8, dash="3 3", color=GREY))
    g.append(_txt(b.x(0) + 6, b.y(0.9), "pha 0°", 7.5, anchor="start", color=GREY))
    g.append(_txt(b.x(0) + 6, b.y(-0.8), "pha 180°", 7.5, anchor="start", color=GREY))
    o.append('<g transform="translate(190,60)">%s</g>' % "".join(g))
    o.append(_txt(345, 232, "(c) biên độ và pha theo vị trí lõi", 8, color=GREY))
    return _fig(svg(520, 246, "".join(o), "Điện áp thứ cấp và đầu ra của LVDT"),
                "Hình 6-18 · Điện áp cảm ứng trên các cuộn thứ cấp của LVDT (a) có thể được xử lý theo nhiều "
                "cách. Tại vị trí không, hai điện áp v₁ và v₂ bằng nhau và cùng pha (b). Khi đấu đối nhau, điện "
                "áp ra v₀ trở thành hàm của vị trí lõi x và của góc pha α (c); lưu ý độ lệch pha 180° khi lõi "
                "đi qua vị trí không.",
                "Figure 6.18 · The voltages induced in the secondaries of an LVDT (a) can be processed in several "
                "ways. At null, v1 and v2 are equal and in phase (b). Connected in opposition, the output v0 "
                "becomes a function of core position x and phase angle α (c) — note the 180° phase reversal as "
                "the core crosses the null position.",
                "Điện áp thứ cấp và đầu ra của LVDT",
                "LVDT secondary voltages and output")


def fig_6_19():
    o = [_defs()]
    # (a) block diagram
    o.append(_txt(150, 18, "(a) tách sóng nhạy pha", 9, weight="600"))
    blocks = [(30, "LVDT"), (110, "tách sóng\nnhạy pha"), (210, "lọc thông thấp"), (310, "v₀ dc")]
    for x, lab in blocks:
        o.append(_rect(x, 40, 76, 40, "#fdfdfd"))
        for i, ln in enumerate(lab.split("\n")):
            o.append(_txt(x + 38, 56 + i * 11, ln, 7.5))
    for x in (106, 186, 286):
        o.append(_arrow(x, 60, x + 4, 60, sw=1))
    o.append(_line(106, 60, 110, 60, sw=1))
    o.append(_arrow(186, 60, 210, 60, sw=1))
    o.append(_arrow(286, 60, 310, 60, sw=1))
    o.append(_line(30, 80, 30, 96, sw=0.9, dash="3 3", color=GREY))
    o.append(_txt(30, 110, "x", 9, color=GREY))
    # (b) demodulated output
    b = Box(230, 150, (-1, 1), (-1, 1), pad=(34, 18, 14, 34))
    g = [b.axes("x", "vo", xt=[(-1, "−x"), (0, "0"), (1, "+x")], yt=[])]
    g.append(b.curve([(-1, -0.85), (-0.5, -0.42), (0, 0), (0.5, 0.42), (1, 0.85)], "c1"))
    g.append(_line(b.x(0), b.y(-1), b.x(0), b.y(1), sw=0.8, dash="3 3", color=GREY))
    o.append('<g transform="translate(250,60)">%s</g>' % "".join(g))
    o.append(_txt(340, 232, "(b) đầu ra sau tách sóng", 8, color=GREY))
    return _fig(svg(520, 246, "".join(o), "Tách sóng nhạy pha cho LVDT"),
                "Hình 6-19 · Bộ tách sóng nhạy pha (a) thường được dùng để lấy tín hiệu tỉ lệ dịch chuyển từ LVDT "
                "và các cảm biến cảm ứng kiểu vi sai khác. Nó đổi đầu ra xoay chiều thành giá trị một chiều và "
                "chỉ ra chiều dịch chuyển của lõi so với vị trí không. Đầu ra điển hình sau tách sóng (b) là hàm "
                "bậc nhất của vị trí lõi, đổi dấu khi lõi qua điểm không.",
                "Figure 6.19 · A phase-sensitive demodulator (a) is the usual way to get a displacement-"
                "proportional signal out of an LVDT and the other differential inductive sensors. It converts the "
                "ac output to dc and indicates which way the core moved from null. The typical demodulated output "
                "(b) is a straight line through the null, changing sign as the core crosses it.",
                "Tách sóng nhạy pha cho LVDT",
                "Phase-sensitive demodulation of an LVDT")


def fig_6_20():
    o = [_defs()]
    o.append(_txt(150, 18, "(a) cầu diode", 9, weight="600"))
    for x, lab in ((30, "cầu 1"), (30, "")):
        pass
    # bridge 1
    o.append(_rect(40, 44, 90, 56, "#fdfdfd"))
    o.append(_txt(85, 76, "cầu 1", 9))
    o.append(_rect(180, 44, 90, 56, "#fdfdfd"))
    o.append(_txt(225, 76, "cầu 2", 9))
    o.append(_line(40, 72, 20, 72, sw=1.1))
    o.append(_line(20, 72, 20, 120, sw=1.1))
    o.append(_line(180, 72, 160, 72, sw=1.1))
    o.append(_line(160, 72, 160, 120, sw=1.1))
    o.append(_line(20, 120, 160, 120, sw=1.1))
    o.append(_line(90, 120, 90, 136, sw=1.1))
    o.append(_txt(98, 140, "v", 9, anchor="start", color=GOLD))
    o.append(_txt(106, 144, "o", 6.5, anchor="start", color=GOLD))
    o.append(_txt(85, 34, "thứ cấp 1", 7.5, color=GREY))
    o.append(_txt(225, 34, "thứ cấp 2", 7.5, color=GREY))
    # (b) output
    b = Box(220, 140, (-1, 1), (-1, 1), pad=(30, 16, 12, 30))
    g = [b.axes("x", "v₀", xt=[(-1, "−x"), (0, "0"), (1, "+x")], yt=[])]
    g.append(b.curve([(-1, -0.8), (0, 0), (1, 0.8)], "c1"))
    o.append('<g transform="translate(260,60)">%s</g>' % "".join(g))
    o.append(_txt(360, 222, "(b) hiệu hai cầu", 8, color=GREY))
    return _fig(svg(520, 232, "".join(o), "Mạch tách sóng nhạy pha dùng cầu diode"),
                "Hình 6-20 · Mạch tách sóng nhạy pha điển hình dùng hai cầu diode (a). Cầu 1 chỉnh lưu tín hiệu "
                "thứ cấp 1, cầu 2 chỉnh lưu tín hiệu thứ cấp 2, và điện áp ra là hiệu hai đầu ra của hai cầu (b). "
                "Vị trí lõi xác định từ biên độ điện áp một chiều, còn chiều dịch chuyển xác định từ dấu của "
                "điện áp. Với chuyển động nhanh phải lọc đầu ra bằng một mạch RC đơn giản được thiết kế phù hợp.",
                "Figure 6.20 · A typical phase-sensitive demodulator built from two diode bridges (a). Bridge 1 "
                "rectifies secondary 1, bridge 2 rectifies secondary 2, and the output is the difference between "
                "them (b). Core position comes from the amplitude of the dc output, direction from its sign. For "
                "fast core motion the bridge outputs must be filtered — a simple RC filter of the right time "
                "constant is usually enough.",
                "Mạch tách sóng nhạy pha dùng cầu diode",
                "Diode-bridge phase-sensitive demodulator")


def fig_6_21():
    o = [_defs()]
    # E core with primary on the centre leg and secondaries on the outer legs
    o.append('<path d="M50 40 H330 V150 H270 V64 H110 V150 H50 Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (FILL, INK))
    o.append(_rect(120, 40, 40, 24, "#e8e8e8"))
    o.append(_txt(140, 34, "sơ cấp", 7.5, color=GREY))
    o.append(_rect(52, 40, 24, 24, "#e8e8e8"))
    o.append(_rect(304, 40, 24, 24, "#e8e8e8"))
    o.append(_txt(64, 34, "S₁", 7.5, color=GREY))
    o.append(_txt(316, 34, "S₂", 7.5, color=GREY))
    # armature above the centre leg, pivoted
    o.append(_rect(96, 12, 92, 10, "#dcdcdc"))
    o.append('<circle cx="142" cy="8" r="4" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(142, 4, "trục quay", 7, color=GREY))
    o.append('<path d="M188 22 a14 14 0 0 1 0 14" fill="none" stroke="%s" stroke-width="1" '
             'marker-end="url(#a6)"/>' % GOLD)
    o.append(_txt(212, 32, "θ", 9, color=GOLD, anchor="start"))
    o.append(_txt(190, 176, "phần ứng quay trên trụ giữa", 8, color=GREY))
    return _fig(svg(520, 188, "".join(o), "Biến áp vi sai lõi quay"),
                "Hình 6-21 · Biến áp vi sai lõi quay có lõi chữ E: cuộn sơ cấp quấn trên trụ giữa, hai cuộn thứ "
                "cấp quấn trên hai trụ ngoài (a). Phần ứng quay quanh một điểm tựa phía trên trụ giữa dưới tác "
                "dụng của lực ngoài (b). Khi phần ứng lệch khỏi vị trí cân bằng, từ trở của mạch từ qua một cuộn "
                "thứ cấp giảm và qua cuộn kia tăng, nên sức điện động cảm ứng ở hai cuộn khác nhau về biên độ và "
                "pha; đấu đối nhau cho ta nguyên lý làm việc giống LVDT.",
                "Figure 6.21 · A rotary core differential transformer has an E-shaped core with the primary on the "
                "centre leg and the two secondaries on the outer legs (a). The armature rotates about a pivot "
                "above the centre leg under an externally applied force (b). Displacing the armature from "
                "balance lowers the reluctance through one secondary and raises it through the other, so the "
                "induced emfs differ in magnitude and phase; wired in opposition the device behaves like an "
                "LVDT.",
                "Biến áp vi sai lõi quay",
                "Rotary core differential transformer")


def fig_6_22():
    o = [_defs()]
    # probe body
    o.append(_rect(40, 60, 150, 40, "#fdfdfd"))
    o.append(_rect(190, 66, 50, 28, "#e8e8e8"))
    o.append(_txt(115, 84, "đầu dò", 9))
    # two coils inside
    o.append(_rect(70, 66, 50, 12, FILL))
    o.append(_txt(95, 62, "cuộn tích cực", 7, color=GREY))
    o.append(_rect(130, 66, 50, 12, "#dcdcdc"))
    o.append(_txt(155, 62, "cuộn cân bằng", 7, color=GREY))
    # target
    o.append(_rect(240, 40, 22, 100, "#dcdcdc"))
    o.append(_txt(251, 156, "vật dẫn", 8, color=GREY))
    # eddy currents
    for i in range(3):
        o.append('<ellipse cx="%s" cy="90" rx="6" ry="%s" fill="none" stroke="%s" stroke-width="1"/>'
                 % (_f(254 + i * 4), _f(10 - i * 2), GOLD))
    o.append(_txt(300, 76, "dòng xoáy", 8, anchor="start", color=GOLD))
    o.append(_line(292, 80, 268, 88, sw=0.8, color=GOLD))
    # standoff
    o.append(_line(240, 124, 240, 136, sw=0.9))
    o.append(_line(240, 124, 240, 124, sw=0.9))
    o.append(_txt(240, 150, "khoảng đứng (standoff)", 7.5, color=GREY))
    return _fig(svg(520, 168, "".join(o), "Đầu dò dòng xoáy"),
                "Hình 6-22 · Cảm biến dòng xoáy là đầu đo cảm ứng gồm một cuộn tích cực và một cuộn cân bằng. "
                "Cuộn tích cực chịu ảnh hưởng của vật dẫn mục tiêu, cuộn cân bằng hoàn thiện cầu đo và bù nhiệt. "
                "Khi đầu dò lại gần mục tiêu, từ thông từ đầu dò móc vòng sang mục tiêu và sinh dòng xoáy trong "
                "đó; dòng xoáy làm thay đổi tổng trở cuộn tích cực, và cầu đo phát hiện thay đổi ấy.",
                "Figure 6.22 · An eddy-current sensor is a probe with two coils: an active coil that responds to "
                "the conducting target, and a balance coil that completes the bridge and compensates temperature. "
                "Brought close to the target, the probe’s flux links into it and induces eddy currents; those "
                "currents change the impedance of the active coil, and the bridge detects the change.",
                "Đầu dò dòng xoáy",
                "Eddy-current probe")


# ---------------------------------------------------------------- 6.3
def _res(x, y, w, horiz=True, n=4):
    """Zigzag resistor symbol, either horizontal (length w) or vertical."""
    if horiz:
        seg = w / (n * 2.0)
        pts = [(x, y)]
        for i in range(n * 2):
            pts.append((x + seg * (i + 1), y + (-7 if i % 2 == 0 else 7)))
        pts.append((x + w, y))
    else:
        seg = w / (n * 2.0)
        pts = [(x, y)]
        for i in range(n * 2):
            pts.append((x + (-7 if i % 2 == 0 else 7), y + seg * (i + 1)))
        pts.append((x, y + w))
    d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    return '<path d="%s" fill="none" stroke="%s" stroke-width="1.1"/>' % (d, INK)


def _opamp(x, y, w=44, h=38, inv=True):
    d = "M%s %s L%s %s L%s %s Z" % (_f(x), _f(y), _f(x), _f(y + h), _f(x + w), _f(y + h / 2.0))
    o = ['<path d="%s" fill="#fff" stroke="%s" stroke-width="1.2"/>' % (d, INK)]
    if inv:
        o.append(_line(x + 4, y + 9, x + 14, y + 9, sw=1.1))
        o.append(_line(x + 4, y + h - 9, x + 14, y + h - 9, sw=1.1))
        o.append(_txt(x + 9, y + 12, "−", 9))
        o.append(_txt(x + 9, y + h - 6, "+", 9))
    return "".join(o)


def _gnd(x, y):
    return (_line(x, y, x, y + 8, sw=1) + _line(x - 9, y + 8, x + 9, y + 8, sw=1)
            + _line(x - 5, y + 12, x + 5, y + 12, sw=1) + _line(x - 1.5, y + 16, x + 1.5, y + 16, sw=1))


def fig_6_23():
    o = [_defs()]
    # --- panel A: cross-section
    o.append(_rect(46, 52, 176, 12, "#cfcfcf"))
    o.append(_txt(134, 44, "bản cực cố định", 8, color=GREY))
    o.append(_rect(46, 140, 176, 12, "#cfcfcf"))
    for xx in (66, 96, 126, 156, 186, 212):
        o.append(_line(xx, 64, xx, 140, sw=0.5, color="#d8bb7d"))
    o.append(_arrow(134, 200, 134, 158))
    o.append(_txt(150, 192, "x", 10, anchor="start", color=GOLD, weight="600"))
    o.append(_line(246, 64, 246, 140, sw=0.7, dash="3 3", color=GREY))
    o.append(_line(239, 64, 253, 64, sw=0.7, color=GREY))
    o.append(_line(239, 140, 253, 140, sw=0.7, color=GREY))
    o.append(_txt(259, 106, "x", 10, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(134, 232, "A — tiết diện ngang", 8, color=GREY))
    # --- panel B: transfer
    ox, oy = 396, 252
    o.append(_line(ox, oy, 632, oy, sw=1))
    o.append(_line(ox, oy, ox, 66, sw=1))
    o.append(_arrow(632, oy, 644, oy, sw=1))
    o.append(_arrow(ox, 66, ox, 54, sw=1))
    ux = lambda u: ox + (u - 0.5) * 65.7
    uy = lambda c: oy - c * 81.8
    pts = []
    u = 0.5
    while u <= 4.001:
        pts.append("%s %s" % (_f(ux(u)), _f(uy(1.0 / u))))
        u += 0.02
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), GOLD))
    # tangent at u = 1
    o.append(_line(ux(0.6), uy(1.4), ux(1.6), uy(0.4), sw=1, dash="4 3", color=GREY))
    o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (_f(ux(1)), _f(uy(1)), INK))
    for uu in (0.5, 1, 2, 3, 4):
        o.append(_line(ux(uu), oy, ux(uu), oy + 4, sw=0.8))
        o.append(_txt(ux(uu), oy + 16, ("%.1f" % uu).rstrip("0").rstrip("."), 7.5, color=GREY))
    for cc in (1, 2):
        o.append(_line(ox - 4, uy(cc), ox, uy(cc), sw=0.8))
        o.append(_txt(ox - 8, uy(cc) + 3, "%d" % cc, 7.5, anchor="end", color=GREY))
    o.append(_txt(ox - 8, 58, "C/C₀", 8.5, anchor="end", color=INK))
    o.append(_txt(640, oy + 34, "x/x₀", 8.5, anchor="end", color=INK))
    o.append(_txt(452, 92, "C ∝ 1/x", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(470, 236, "độ dốc = −C/x²", 7.5, anchor="start", color=GREY))
    o.append(_txt(514, 288, "B — hàm truyền hyperbolic", 8, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Cảm biến điện dung biến thiên khoảng cách"),
                "Hình 6-23 · Cảm biến điện dung kiểu biến thiên khoảng cách. Một trong hai bản cực di chuyển để thay đổi "
                "khoảng cách giữa hai bản theo biến vật lý. Đầu ra của đầu đo phi tuyến theo khoảng cách x, có đặc tính "
                "truyền hyperbolic (C = εA/x); vì vậy cần xử lý tín hiệu thích hợp để tuyến tính hoá. Đường đứt nét là "
                "tiếp tuyến tại x = x₀, có độ dốc −C/x².",
                "Figure 6.23 · A variable-distance capacitive displacement sensor. One plate moves to change the gap in "
                "response to a physical variable. The output is nonlinear in x, with a hyperbolic transfer characteristic "
                "(C = εA/x), so signal processing must linearise it. The dashed line is the tangent at x = x₀, of slope "
                "−C/x².",
                "Cảm biến điện dung biến thiên khoảng cách",
                "Variable-distance capacitive sensor")


def fig_6_24():
    o = [_defs()]
    o.append(_rect(46, 58, 210, 12, "#cfcfcf"))
    o.append(_txt(151, 50, "bản cực cố định", 8, color=GREY))
    o.append(_rect(46, 134, 118, 12, "#cfcfcf"))
    o.append(_txt(105, 160, "bản cực trượt", 8, color=GREY))
    # overlap region (the area the two plates actually share)
    o.append('<rect x="46" y="70" width="118" height="64" fill="#f6e6c8" fill-opacity=".55" '
             'stroke="%s" stroke-width=".9" stroke-dasharray="3 3"/>' % GOLD)
    o.append(_arrow(230, 140, 168, 140))
    o.append(_txt(234, 143, "x", 10, anchor="start", color=GOLD, weight="600"))
    o.append(_line(46, 178, 164, 178, sw=0.8, color=GREY))
    o.append(_txt(105, 192, "w − x", 8, color=GREY))
    o.append(_txt(268, 104, "A = w·(w−x)", 8, anchor="start", color=GREY))
    # panel B linear
    ox, oy = 412, 240
    o.append(_line(ox, oy, 636, oy, sw=1))
    o.append(_line(ox, oy, ox, 70, sw=1))
    o.append(_arrow(636, oy, 648, oy, sw=1))
    o.append(_arrow(ox, 70, ox, 58, sw=1))
    o.append(_line(ox, oy, 620, 92, sw=1.8, color=GOLD))
    for i, lab in enumerate(("0", "0.5", "1")):
        xx = ox + i * 104
        o.append(_line(xx, oy, xx, oy + 4, sw=0.8))
        o.append(_txt(xx, oy + 16, lab, 7.5, color=GREY))
    o.append(_txt(ox - 8, 62, "C", 8.5, anchor="end"))
    o.append(_txt(650, oy + 16, "x", 8.5, anchor="end"))
    o.append(_txt(556, 112, "tuyến tính", 8.5, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(524, 288, "B — đầu ra tuyến tính theo x", 8, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Cảm biến điện dung biến thiên diện tích"),
                "Hình 6-24 · Cảm biến điện dung kiểu biến thiên diện tích. Cảm biến hoạt động dựa trên sự thay đổi diện "
                "tích hiệu dụng giữa hai bản của tụ phẳng. Đầu ra tuyến tính theo dịch chuyển x. Kiểu này thường được "
                "chế tạo dưới dạng tụ quay để đo dịch chuyển góc, và cũng dùng làm vôn kế điện dung.",
                "Figure 6.24 · A variable-area capacitive displacement sensor. It works on the change in effective area "
                "between the plates of a flat capacitor. The output is linear in displacement x. The type is normally "
                "built as a rotating capacitor for angular displacement, and also serves as a capacitive voltmeter.",
                "Cảm biến điện dung biến thiên diện tích",
                "Variable-area capacitive sensor")


def fig_6_25():
    o = [_defs()]
    o.append(_rect(46, 56, 216, 12, "#cfcfcf"))
    o.append(_txt(154, 48, "bản cực trên", 8, color=GREY))
    o.append(_rect(46, 132, 216, 12, "#cfcfcf"))
    o.append(_txt(154, 160, "bản cực dưới", 8, color=GREY))
    # dielectric slab partly inserted
    o.append(_rect(46, 68, 104, 64, "#f3f7ee"))
    o.append(_rect(150, 68, 112, 64, "#e8f0e0"))
    o.append(_txt(206, 100, "ε₁", 9, color="#4a6b3a"))
    o.append(_txt(96, 100, "ε₂", 9, color="#4a6b3a"))
    o.append(_arrow(118, 118, 158, 118))
    o.append(_txt(112, 122, "x", 9, anchor="end", color=GOLD, weight="600"))
    o.append(_line(150, 68, 150, 132, sw=0.9, dash="3 3", color=GOLD))
    o.append(_txt(206, 184, "chất điện môi di chuyển", 8, color=GREY))
    # panel B
    ox, oy = 412, 240
    o.append(_line(ox, oy, 636, oy, sw=1))
    o.append(_line(ox, oy, ox, 70, sw=1))
    o.append(_arrow(636, oy, 648, oy, sw=1))
    o.append(_arrow(ox, 70, ox, 58, sw=1))
    o.append(_line(ox, oy - 30, 620, oy - 148, sw=1.8, color=GOLD))
    o.append(_line(ox, oy - 30, 620, oy - 30, sw=1.2, dash="4 3", color=GREY))
    o.append(_txt(496, 116, "ε₁ > ε₂", 8, color=GREY))
    o.append(_txt(496, 230, "ε₁ = ε₂", 8, color=GREY))
    for i, lab in enumerate(("0", "0.5", "1")):
        xx = ox + i * 104
        o.append(_line(xx, oy, xx, oy + 4, sw=0.8))
        o.append(_txt(xx, oy + 16, lab, 7.5, color=GREY))
    o.append(_txt(ox - 8, 62, "C", 8.5, anchor="end"))
    o.append(_txt(650, oy + 16, "x", 8.5, anchor="end"))
    o.append(_txt(524, 288, "B — đầu ra tuyến tính", 8, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Cảm biến điện dung biến thiên chất điện môi"),
                "Hình 6-25 · Cảm biến điện dung kiểu biến thiên chất điện môi. Chất điện môi giữa hai bản tụ phẳng di "
                "chuyển, làm thay đổi hằng số điện môi hiệu dụng. Đầu ra của cảm biến là tuyến tính. Kiểu này chủ yếu "
                "dùng dưới dạng hai trụ đồng tâm để đo mức chất lỏng trong bồn.",
                "Figure 6.25 · A variable-dielectric capacitive displacement sensor. The dielectric between the two "
                "parallel plates moves, changing the effective permittivity. The output is linear. The type is used "
                "mainly as two concentric cylinders to measure liquid level in tanks.",
                "Cảm biến điện dung biến thiên chất điện môi",
                "Variable-dielectric capacitive sensor")


def fig_6_26():
    o = [_defs()]
    # three plates
    o.append(_rect(56, 50, 12, 110, "#cfcfcf"))
    o.append(_txt(62, 42, "bản ngoài", 7.5, color=GREY))
    o.append(_rect(232, 50, 12, 110, "#cfcfcf"))
    o.append(_txt(238, 42, "bản ngoài", 7.5, color=GREY))
    o.append(_rect(146, 50, 12, 110, "#b9b9b9"))
    o.append(_arrow(152, 196, 152, 166))
    o.append(_txt(166, 190, "δd", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_line(68, 60, 146, 60, sw=0.5, color="#d8bb7d"))
    o.append(_line(68, 150, 146, 150, sw=0.5, color="#d8bb7d"))
    o.append(_line(158, 60, 232, 60, sw=0.5, color="#d8bb7d"))
    o.append(_line(158, 150, 232, 150, sw=0.5, color="#d8bb7d"))
    o.append(_txt(107, 110, "C₁", 10, color=GOLD, weight="600"))
    o.append(_txt(195, 110, "C₂", 10, color=GOLD, weight="600"))
    o.append(_line(152, 50, 152, 26, sw=1))
    o.append(_txt(152, 22, "ra", 8, color=GREY))
    o.append(_line(62, 160, 62, 176, sw=1))
    o.append(_txt(62, 190, "e₁", 8, color=GREY))
    o.append(_line(238, 160, 238, 176, sw=1))
    o.append(_txt(238, 190, "e₂", 8, color=GREY))
    o.append(_txt(152, 224, "A — ba bản cực, bản giữa di động", 8, color=GREY))
    # panel B linear
    ox, oy = 400, 150
    o.append(_line(ox - 60, oy, ox + 190, oy, sw=1))
    o.append(_line(ox, 40, ox, 250, sw=1))
    o.append(_arrow(ox + 190, oy, ox + 202, oy, sw=1))
    o.append(_line(ox - 120, oy + 120, ox + 120, oy - 120, sw=1.8, color=GOLD))
    o.append(_txt(ox + 8, 36, "δC/C", 8, anchor="start"))
    o.append(_txt(ox + 206, oy + 16, "δd/d", 8, anchor="end"))
    o.append(_txt(ox + 32, 58, "δC/C = δd/d", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(ox + 40, 288, "B — tuyến tính hơn kiểu hai bản", 8, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Cảm biến điện dung vi sai"),
                "Hình 6-26 · Cảm biến điện dung vi sai. Về bản chất đây là tụ ba cực: một bản giữa cố định và hai bản "
                "ngoài. Đáp ứng với biến vật lý là tuyến tính. Ở một số phiên bản bản giữa di động còn hai bản ngoài "
                "cố định; ở phiên bản khác thì ngược lại. Đầu ra lấy từ bản giữa bằng không tại vị trí danh định.",
                "Figure 6.26 · A differential capacitive sensor. Essentially a three-terminal capacitor: one fixed "
                "centre plate and two outer plates. The response to the physical variable is linear. In some versions "
                "the centre plate moves; in others it is fixed and the outer plates move. The centre-plate output is "
                "zero at the nominal position.",
                "Cảm biến điện dung vi sai",
                "Differential capacitive sensor")


def fig_6_27():
    o = [_defs()]
    # electrode with guard
    o.append(_rect(60, 66, 150, 60, "#ececec"))
    o.append(_rect(110, 82, 50, 28, "#cfcfcf"))
    o.append(_txt(135, 100, "Cx", 9, color=INK, weight="600"))
    o.append(_txt(135, 56, "điện cực bảo vệ", 8, color=GREY))
    o.append(_txt(212, 100, "bản nhỏ", 7.5, anchor="start", color=GREY))
    o.append(_line(206, 96, 164, 96, sw=0.7, color=GREY))
    o.append(_txt(135, 146, "A — điện cực bảo vệ quanh bản nhỏ", 8, color=GREY))
    o.append(_txt(60, 178, "δ < exp(−πx/d),  δ < exp(−πd/s)", 8, anchor="start", color=GREY))
    # panel B: three-signal chain
    y = 96
    boxes = [("dao động", 330, 62), ("Cx", 406, 40), ("tách sóng", 460, 66), ("ADC", 540, 44)]
    for lab, bx, bw in boxes:
        o.append(_rect(bx, y - 16, bw, 32, "#fff"))
        o.append(_txt(bx + bw / 2.0, y + 4, lab, 7.5))
    for bx in (392, 446, 526):
        o.append(_arrow(bx, y, bx + 12, y, sw=1))
    o.append(_arrow(584, y, 604, y, sw=1))
    o.append(_txt(608, y + 4, "µC", 8, anchor="start"))
    o.append(_txt(466, 214, "B — đo ba tín hiệu: Cx, Cref, offset", 8, color=GREY))
    return _fig(svg(660, 230, "".join(o), "Cảm biến vị trí điện dung thông minh"),
                "Hình 6-27 · Cảm biến vị trí điện dung thông minh điển hình. Kết cấu vi cơ này có ba điện cực, hai cố "
                "định và một di động một lượng rất nhỏ so với hai điện cực kia. Tuy đáp ứng rất phi tuyến, chip tích "
                "hợp đã có mạch tuyến tính hoá. Dải đo 0–1 mm với độ chính xác 1 µm.",
                "Figure 6.27 · A typical smart capacitive position sensor. The microstructure has three electrodes, two "
                "fixed and one moving infinitesimally relative to the others. Although the response is highly "
                "nonlinear, the integrated chip carries linearisation circuitry. Range 0–1 mm at 1 µm accuracy.",
                "Cảm biến vị trí điện dung thông minh",
                "Smart capacitive position sensor")


def fig_6_28():
    o = [_defs()]
    # housing
    o.append(_rect(56, 52, 14, 96, "#cfcfcf"))
    o.append(_rect(240, 52, 14, 96, "#cfcfcf"))
    o.append(_rect(56, 140, 198, 10, "#cfcfcf"))
    # diaphragm deflected (full diameter: r runs -a .. +a)
    pts = []
    for i in range(61):
        rr = -1 + i / 30.0
        yy = 62 + 26 * ((1 - rr * rr) ** 2)
        pts.append("%s %s" % (_f(155 + rr * 85), _f(yy)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), GOLD))
    o.append(_txt(155, 44, "màng mỏng kẹp chu vi", 8, color=GREY))
    o.append(_arrow(155, 24, 155, 40, sw=1))
    o.append(_txt(155, 170, "bản cực cố định", 8, color=GREY))
    o.append(_line(155, 90, 155, 138, sw=0.7, dash="3 3", color=GREY))
    o.append(_txt(163, 120, "d", 8, anchor="start", color=GREY))
    # panel B deflection profile
    ox, oy = 372, 214
    o.append(_line(ox, oy, 606, oy, sw=1))
    o.append(_line(ox, oy, ox, 60, sw=1))
    o.append(_arrow(606, oy, 618, oy, sw=1))
    o.append(_arrow(ox, 60, ox, 48, sw=1))
    pts = []
    for i in range(81):
        r = i / 80.0
        pts.append("%s %s" % (_f(ox + r * 220), _f(oy - 140 * ((1 - r * r) ** 2))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), GOLD))
    o.append(_txt(ox + 6, 44, "y(r)", 8, anchor="start"))
    o.append(_txt(614, oy + 16, "r/a", 8, anchor="end"))
    o.append(_txt(ox + 130, 86, "y ∝ (a² − r²)²", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(496, 246, "ΔC/C = ȳ/d = y₀/3d", 8.5, color=INK, weight="600"))
    o.append(_txt(496, 268, "B — biên dạng võng và tín hiệu", 8, color=GREY))
    return _fig(svg(660, 290, "".join(o), "Cảm biến áp suất điện dung"),
                "Hình 6-28 · Cảm biến áp suất điện dung. Cảm biến gồm một bản kim loại cố định và một màng mỏng đàn hồi. "
                "Màng tròn phẳng được kẹp ở chu vi và võng thành mặt cong dưới áp suất P. Độ võng tỉ lệ với P, và sự "
                "biến dạng làm giảm khoảng cách trung bình giữa hai bản, do đó điện dung tăng.",
                "Figure 6.28 · A capacitive pressure sensor. It consists of a fixed metal plate and a flexible "
                "diaphragm. The flat circular diaphragm is clamped at its circumference and bows under pressure P. "
                "The deflection is proportional to P, and the deformation reduces the mean plate separation, so the "
                "capacitance rises.",
                "Cảm biến áp suất điện dung",
                "Capacitive pressure sensor")


def fig_6_29():
    o = [_defs()]
    o.append(_rect(52, 56, 240, 110, "#fbfbfb"))
    o.append(_rect(52, 56, 240, 10, "#cfcfcf"))
    o.append(_rect(52, 156, 240, 10, "#cfcfcf"))
    o.append(_rect(164, 66, 12, 90, "#b9b9b9"))
    o.append(_line(60, 96, 164, 96, sw=0.6, color="#d8bb7d"))
    o.append(_line(176, 96, 284, 96, sw=0.6, color="#d8bb7d"))
    o.append(_txt(112, 122, "C₁", 10, color=GOLD, weight="600"))
    o.append(_txt(230, 122, "C₂", 10, color=GOLD, weight="600"))
    o.append(_arrow(120, 40, 120, 54, sw=1))
    o.append(_txt(120, 34, "P₁", 9, color=GREY))
    o.append(_arrow(230, 40, 230, 54, sw=1))
    o.append(_txt(230, 34, "P₂", 9, color=GREY))
    o.append(_txt(170, 194, "ra ∝ (P₁ − P₂)", 9, color=INK, weight="600"))
    o.append(_txt(170, 216, "A — tụ vi sai, hiệu áp", 8, color=GREY))
    # panel B transfer
    ox, oy = 400, 130
    o.append(_line(ox - 40, oy, ox + 190, oy, sw=1))
    o.append(_line(ox + 75, 30, ox + 75, 236, sw=1))
    o.append(_line(ox - 70, oy + 80, ox + 165, oy - 80, sw=1.8, color=GOLD))
    o.append(_txt(ox + 80, 26, "ra", 8, anchor="start"))
    o.append(_txt(ox + 190, oy + 16, "ΔP", 8, anchor="end"))
    o.append(_txt(ox + 30, 78, "đảo pha 180°", 7.5, anchor="start", color=GREY))
    o.append(_txt(ox + 60, 288, "B — đầu ra vi phân, đổi dấu", 8, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Cảm biến áp suất điện dung vi sai"),
                "Hình 6-29 · Cảm biến áp suất điện dung vi sai. Điện dung C₁ và C₂ thay đổi so với bản giữa cố định khi "
                "áp suất P₁ và P₂ tác động lên hai phía. Đầu ra tỉ lệ với (P₁ − P₂); khi hiệu áp đổi dấu, pha đổi 180°.",
                "Figure 6.29 · A differential capacitive pressure sensor. C₁ and C₂ change about the fixed centre plate "
                "as pressures P₁ and P₂ are applied. The output is proportional to (P₁ − P₂); when the difference "
                "reverses, the phase shifts by 180°.",
                "Cảm biến áp suất điện dung vi sai",
                "Differential capacitive pressure sensor")


def fig_6_30():
    o = [_defs()]
    # frame
    o.append(_rect(56, 56, 236, 14, "#cfcfcf"))
    o.append(_rect(56, 152, 236, 14, "#cfcfcf"))
    # springs
    o.append(_res(58, 110, 40))
    o.append(_res(250, 110, 40))
    # proof mass
    o.append(_rect(100, 82, 148, 56, "#b9b9b9"))
    o.append(_txt(174, 114, "khối chứng", 9, color="#fff"))
    o.append(_arrow(174, 190, 174, 142, sw=1.3))
    o.append(_txt(186, 184, "a", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_line(86, 138, 86, 152, sw=0.7, dash="3 3", color=GREY))
    o.append(_txt(80, 149, "d", 8, anchor="end", color=GREY))
    o.append(_txt(174, 216, "A — khối chứng là một bản cực", 8, color=GREY))
    # panel B: energy balance curve
    ox, oy = 400, 210
    o.append(_line(ox, oy, 610, oy, sw=1))
    o.append(_line(ox, oy, ox, 56, sw=1))
    o.append(_arrow(610, oy, 622, oy, sw=1))
    o.append(_arrow(ox, 56, ox, 44, sw=1))
    for k, lab, col in ((1.0, "V lớn", GOLD), (0.62, "V nhỏ", "#c98f3a")):
        pts = []
        for i in range(41):
            u = 0.35 + (i / 40.0) * 0.65
            pts.append("%s %s" % (_f(ox + (i / 40.0) * 200), _f(oy - 130 * k * (0.35 / u) ** 2)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.7"/>' % (" ".join(pts), col))
    o.append(_txt(ox + 6, 40, "F(x)", 8, anchor="start"))
    o.append(_txt(618, oy + 16, "x", 8, anchor="end"))
    o.append(_txt(ox + 120, 96, "F = ½V²dC/dx", 8.5, color=GOLD, weight="600"))
    o.append(_txt(ox + 108, 246, "B — lực Coulomb tăng khi x giảm", 8, color=GREY))
    return _fig(svg(660, 260, "".join(o), "Gia tốc kế điện dung vi cơ"),
                "Hình 6-30 · Đầu đo lực kiểu điện dung. Gia tốc kế vi cơ điện dung điển hình dùng khối chứng làm một "
                "bản cực, bản kia cố định và đóng vai trò đế. Khi cảm biến được gia tốc, khối chứng dịch chuyển, làm "
                "thay đổi khoảng cách bản cực và điện áp trên tụ; độ thay đổi ấy tỉ lệ với gia tốc tác dụng.",
                "Figure 6.30 · A capacitive force transducer. A typical micromachined accelerometer uses the proof mass "
                "as one plate and the base as the other. Under acceleration the proof mass moves, changing the plate "
                "separation and the voltage across the capacitor; that change is proportional to the applied "
                "acceleration.",
                "Gia tốc kế điện dung vi cơ",
                "Capacitive micromachined accelerometer")


def fig_6_31():
    o = [_defs()]
    # outer tank
    o.append(_rect(70, 56, 150, 150, "#fbfbfb"))
    # liquid first, so the electrode reads as standing in it
    o.append('<rect x="70" y="132" width="150" height="74" fill="#dce9f5" stroke="none"/>')
    o.append(_line(70, 132, 220, 132, sw=1, color="#6b8fb3"))
    o.append(_txt(196, 128, "mức h", 8, anchor="end", color="#4a6b8a"))
    # inner electrode
    o.append(_rect(126, 76, 38, 130, "#cfcfcf"))
    o.append(_txt(145, 70, "r₁", 8, color=GREY))
    o.append(_txt(78, 70, "r₂", 8, anchor="start", color=GREY))
    # total height dimension
    o.append(_line(236, 56, 236, 206, sw=0.8, dash="3 3", color=GREY))
    o.append(_line(231, 56, 241, 56, sw=0.8, color=GREY))
    o.append(_line(231, 206, 241, 206, sw=0.8, color=GREY))
    o.append(_txt(244, 134, "l", 8, anchor="start", color=GREY))
    o.append(_txt(145, 232, "A — hai trụ đồng tâm", 8, color=GREY))
    # panel B: C vs h
    ox, oy = 396, 232
    o.append(_line(ox, oy, 610, oy, sw=1))
    o.append(_line(ox, oy, ox, 62, sw=1))
    o.append(_arrow(610, oy, 622, oy, sw=1))
    o.append(_arrow(ox, 62, ox, 50, sw=1))
    o.append(_line(ox, oy - 40, 596, oy - 150, sw=1.8, color=GOLD))
    o.append(_line(ox, oy - 40, 596, oy - 40, sw=1.1, dash="4 3", color=GREY))
    o.append(_txt(ox + 6, 46, "C", 8, anchor="start"))
    o.append(_txt(618, oy + 16, "h", 8, anchor="end"))
    o.append(_txt(ox + 8, oy - 26, "h = 0 (không khí)", 7.5, anchor="start", color=GREY))
    o.append(_txt(ox + 120, 258, "B — điện dung tỉ lệ với mức", 8, color=GREY))
    return _fig(svg(660, 272, "".join(o), "Cảm biến mức chất lỏng điện dung"),
                "Hình 6-31 · Cảm biến mức chất lỏng điện dung. Hai trụ kim loại đồng tâm làm hai điện cực của tụ. Giá "
                "trị điện dung phụ thuộc hằng số điện môi của chất lỏng và của khí phía trên; tổng hằng số điện môi "
                "thay đổi theo mức chất lỏng. Thiết bị thường dùng cho chất lỏng không dẫn điện.",
                "Figure 6.31 · A capacitive liquid-level sensor. Two concentric metal cylinders form the electrodes. The "
                "capacitance depends on the permittivity of the liquid and of the gas above it; the combined "
                "permittivity tracks the liquid level. These devices are used for non-conducting liquids.",
                "Cảm biến mức chất lỏng điện dung",
                "Capacitive liquid-level sensor")


def fig_6_32():
    o = [_defs()]
    # substrate
    o.append(_rect(56, 148, 250, 26, "#b9b9b9"))
    o.append(_txt(181, 190, "nhôm (Al)", 8, color=GREY))
    # oxide with columnar pores
    o.append(_rect(56, 92, 250, 56, "#e7ded0"))
    for i in range(11):
        xx = 68 + i * 22
        o.append(_rect(xx, 96, 9, 48, "#fffdf8", sw=0.6))
    o.append(_txt(322, 126, "lỗ mao quản", 8, anchor="start", color=GREY))
    o.append(_line(318, 120, 300, 116, sw=0.7, color=GREY))
    # gold film
    o.append(_rect(56, 84, 250, 8, "#c9a227"))
    o.append(_txt(181, 76, "màng vàng xốp (điện cực thứ hai)", 8, color=GREY))
    # water molecules
    for xx, yy in ((96, 62), (150, 56), (206, 62), (120, 40), (188, 40)):
        o.append('<circle cx="%s" cy="%s" r="4.5" fill="#9fc6e8" stroke="%s" stroke-width=".7"/>'
                 % (_f(xx), _f(yy), "#6b8fb3"))
    o.append(_txt(244, 44, "H₂O", 8, anchor="start", color="#4a6b8a"))
    o.append(_arrow(264, 70, 264, 90, sw=0.9, color="#6b8fb3"))
    o.append(_txt(181, 224, "A — cấu trúc lỗ xốp", 8, color=GREY))
    # panel B: R and C vs RH
    ox, oy = 420, 224
    o.append(_line(ox, oy, 630, oy, sw=1))
    o.append(_line(ox, oy, ox, 58, sw=1))
    o.append(_arrow(630, oy, 642, oy, sw=1))
    o.append(_arrow(ox, 58, ox, 46, sw=1))
    # C rises
    pts = []
    for i in range(51):
        x = i / 50.0
        pts.append("%s %s" % (_f(ox + x * 190), _f(oy - (18 + 120 * x * x))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), GOLD))
    # R falls (log)
    pts = []
    for i in range(51):
        x = i / 50.0
        pts.append("%s %s" % (_f(ox + x * 190), _f(oy - 14 - 116 * (1 - x) ** 2.6)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="5 3"/>'
             % (" ".join(pts), GREY))
    o.append(_txt(ox + 152, 74, "C", 9, color=GOLD, weight="600"))
    o.append(_txt(ox + 26, 78, "R", 9, color=GREY, weight="600"))
    o.append(_txt(ox + 96, oy + 18, "%RH", 8))
    o.append(_txt(ox - 6, 46, "C, R", 8, anchor="end"))
    o.append(_txt(ox + 100, 258, "B — ở ẩm cao, C là đại lượng đo tốt", 8, color=GREY))
    return _fig(svg(660, 272, "".join(o), "Cảm biến độ ẩm điện dung"),
                "Hình 6-32 · Cảm biến độ ẩm điện dung điển hình. Cảm biến có cấu trúc lỗ xốp hoặc dạng khảm nứt để hơi "
                "ẩm trong không khí hoặc khí tiếp cận chất điện môi. Tính chất của chất điện môi thay đổi theo lượng "
                "nước hấp thụ, làm giảm điện trở và tăng điện dung. Đại lượng đo có thể là điện trở, điện dung hoặc "
                "tổng trở; ở độ ẩm cao nên đo điện dung vì điện trở biến thiên rất nhỏ.",
                "Figure 6.32 · A typical capacitive humidity sensor. The sensor has a pore or cracked-mosaic structure "
                "that lets moisture in air or gas reach the dielectric. The dielectric’s properties change with the "
                "water absorbed, lowering resistance and raising capacitance. The measured quantity may be "
                "resistance, capacitance or impedance; at high humidity capacitance is preferred because resistance "
                "changes become vanishingly small.",
                "Cảm biến độ ẩm điện dung",
                "Capacitive humidity sensor")


def fig_6_33():
    o = [_defs()]
    # chamber
    o.append('<rect x="70" y="52" width="150" height="140" rx="4" fill="#fbfbfb" stroke="%s" stroke-width="1.1"/>' % INK)
    # grain
    import random as _rnd
    _rnd.seed(7)
    for _ in range(90):
        cx = 82 + _rnd.random() * 126
        cy = 108 + _rnd.random() * 74
        o.append('<ellipse cx="%s" cy="%s" rx="4.2" ry="2.8" fill="#e3d3b0" stroke="#c8b48a" '
                 'stroke-width=".5" transform="rotate(%s %s %s)"/>'
                 % (_f(cx), _f(cy), _f(_rnd.randint(-40, 40)), _f(cx), _f(cy)))
    # electrodes on the wall
    o.append(_rect(64, 52, 6, 140, "#b9b9b9"))
    o.append(_rect(220, 52, 6, 140, "#b9b9b9"))
    o.append(_txt(145, 44, "buồng trụ kín", 8, color=GREY))
    # depth dimension
    o.append(_line(236, 52, 236, 192, sw=0.7, color=GREY))
    o.append(_line(231, 52, 241, 52, sw=0.7, color=GREY))
    o.append(_line(231, 192, 241, 192, sw=0.7, color=GREY))
    o.append(_txt(244, 126, "150 mm", 7.5, anchor="start", color=GREY))
    # diameter dimension
    o.append(_line(70, 206, 220, 206, sw=0.7, color=GREY))
    o.append(_line(70, 201, 70, 211, sw=0.7, color=GREY))
    o.append(_line(220, 201, 220, 211, sw=0.7, color=GREY))
    o.append(_txt(145, 224, "Ø100 mm", 7.5, color=GREY))
    o.append(_txt(145, 244, "mẫu hạt (lúa mì, ngũ cốc)", 8, color=GREY))
    # panel B: oscillator
    y = 128
    o.append(_rect(300, y - 16, 74, 32, "#fff"))
    o.append(_txt(337, y + 4, "dao động", 7.5))
    o.append(_rect(392, y - 16, 62, 32, "#fff"))
    o.append(_txt(423, y + 4, "Cx", 7.5))
    o.append(_rect(472, y - 16, 74, 32, "#fff"))
    o.append(_txt(509, y + 4, "đếm tần số", 7.5))
    o.append(_arrow(374, y, 386, y, sw=1))
    o.append(_arrow(454, y, 466, y, sw=1))
    o.append(_arrow(546, y, 566, y, sw=1))
    o.append(_txt(570, y + 4, "f", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(470, 236, "B — tụ nằm trong mạch dao động", 8, color=GREY))
    return _fig(svg(660, 258, "".join(o), "Cảm biến độ ẩm vật liệu dạng hạt"),
                "Hình 6-33 · Cảm biến độ ẩm điện dung cho vật liệu hạt. Hằng số điện môi của vật liệu giữa hai bản "
                "(trụ hoặc phẳng, kích thước cố định) thay đổi theo độ ẩm của mẫu trong buồng. Sự biến thiên điện dung "
                "theo hàm lượng nước được xử lý; tụ được ghép vào mạch dao động làm việc ở tần số thích hợp, thường "
                "ở dải tần số vô tuyến.",
                "Figure 6.33 · A capacitive moisture sensor for granular material. The permittivity of the material "
                "between the fixed plates (cylindrical or flat) changes with the moisture of the sample in the "
                "chamber. The capacitance variation with water content is processed; the capacitor sits inside an "
                "oscillator running at a suitable frequency, usually in the radio range.",
                "Cảm biến độ ẩm vật liệu hạt",
                "Capacitive moisture sensor")


def fig_6_34():
    o = [_defs()]
    yi, yo = 86, 96          # inverting node level / output level
    # input wire
    o.append(_line(44, yi, 150, yi, sw=1))
    o.append(_txt(44, yi - 9, "ei", 8, anchor="start", color=GREY))
    # Cx to ground
    o.append(_line(96, yi, 96, 116, sw=1))
    o.append(_line(76, 116, 116, 116, sw=1.4))
    o.append(_line(76, 124, 116, 124, sw=1.4))
    o.append(_line(96, 124, 96, 142, sw=1))
    o.append(_gnd(96, 142))
    o.append(_txt(122, 124, "Cx", 9, anchor="start", color=GOLD, weight="600"))
    # op-amp
    o.append(_opamp(150, 77))
    # feedback branch carrying Cf
    o.append(_line(140, yi, 140, 40, sw=1))
    o.append(_line(140, 40, 190, 40, sw=1))
    o.append(_line(196, 30, 196, 50, sw=1.4))
    o.append(_line(204, 30, 204, 50, sw=1.4))
    o.append(_line(210, 40, 250, 40, sw=1))
    o.append(_line(250, 40, 250, yo, sw=1))
    o.append(_txt(200, 22, "Cf", 9, color=GOLD, weight="600"))
    # output
    o.append(_line(194, yo, 288, yo, sw=1))
    o.append(_arrow(262, yo, 274, yo, sw=1))
    o.append(_txt(292, yo + 4, "e\u2080", 9, anchor="start", color=GREY))
    # equations
    o.append(_txt(150, 198, "e\u2080 = \u2212(Cx/Cf)\u00b7ei", 10, color=INK, weight="600"))
    o.append(_txt(150, 220, "\u21d2 e\u2080 tuy\u1ebfn t\u00ednh theo Cx", 9, color=GOLD))
    o.append(_txt(150, 244, "tuy\u1ebfn t\u00ednh ho\u00e1 nh\u1edd t\u1ee5 ph\u1ea3n h\u1ed3i", 8, color=GREY))
    return _fig(svg(420, 258, "".join(o), "B\u1ed9 khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n t\u00edch"),
                "H\u00ecnh 6-34 \u00b7 B\u1ed9 x\u1eed l\u00fd t\u00edn hi\u1ec7u d\u00f9ng khu\u1ebfch \u0111\u1ea1i thu\u1eadt to\u00e1n. C\u00e1ch n\u00e0y kh\u1eed \u0111\u01b0\u1ee3c t\u00ednh phi tuy\u1ebfn c\u1ee7a quan h\u1ec7 "
                "gi\u1eefa bi\u1ebfn v\u1eadt l\u00fd (v\u00ed d\u1ee5 c\u1ea3m bi\u1ebfn hai b\u1ea3n) v\u00e0 \u0111i\u1ec7n dung C. V\u1edbi tr\u1edf kh\u00e1ng v\u00e0o l\u1edbn, \u0111\u1ea7u ra kh\u00f4ng b\u00e3o ho\u00e0 "
                "v\u00e0 \u0111i\u1ec7n \u00e1p v\u00e0o nh\u1ecf, \u0111i\u1ec7n \u00e1p ra t\u1ec9 l\u1ec7 ngh\u1ecbch v\u1edbi Cx \u2014 ngh\u0129a l\u00e0 t\u1ec9 l\u1ec7 thu\u1eadn v\u1edbi l\u01b0\u1ee3ng d\u1ecbch chuy\u1ec3n c\u1ee7a "
                "c\u1ea3m bi\u1ebfn bi\u1ebfn thi\u00ean di\u1ec7n t\u00edch.",
                "Figure 6.34 \u00b7 An operational-amplifier signal processor. This removes the nonlinearity between the "
                "physical variable (a two-plate sensor, for instance) and the capacitance C. With high input "
                "impedance, an unsaturated output and a small input voltage, the output is inversely proportional "
                "to Cx \u2014 that is, directly proportional to the displacement of a variable-area sensor.",
                "B\u1ed9 khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n t\u00edch",
                "Charge amplifier")


def fig_6_35():
    o = [_defs()]
    yi, yo = 110, 120
    # input
    o.append(_line(44, yi, 168, yi, sw=1))
    o.append(_txt(44, yi - 9, "ei", 8, anchor="start", color=GREY))
    # Cx to ground
    o.append(_line(100, yi, 100, 140, sw=1))
    o.append(_line(80, 140, 120, 140, sw=1.4))
    o.append(_line(80, 148, 120, 148, sw=1.4))
    o.append(_line(100, 148, 100, 166, sw=1))
    o.append(_gnd(100, 166))
    o.append(_txt(72, 148, "Cx", 9, anchor="end", color=GOLD, weight="600"))
    # op-amp
    o.append(_opamp(168, 101))
    # non-inverting input and bias resistor R4
    o.append(_line(150, 130, 168, 130, sw=1))
    o.append(_line(150, 130, 150, 140, sw=1))
    o.append(_res(150, 140, 34, horiz=False))
    o.append(_gnd(150, 174))
    o.append(_txt(138, 162, "R\u2084", 8, anchor="end", color=GREY))
    # feedback network R3 + (R1 // R2)
    o.append(_line(158, yi, 158, 52, sw=1))
    o.append(_line(158, 52, 190, 52, sw=1))
    o.append(_res(190, 52, 40))
    o.append(_txt(210, 40, "R\u2083", 8, color=GREY))
    o.append(_line(230, 52, 250, 52, sw=1))
    o.append(_res(250, 52, 40))
    o.append(_txt(270, 40, "R\u2081", 8, color=GREY))
    o.append(_line(290, 52, 300, 52, sw=1))
    o.append(_line(300, 52, 300, yo, sw=1))
    o.append(_line(250, 52, 250, 82, sw=1))
    o.append(_res(250, 82, 40))
    o.append(_line(290, 82, 290, 52, sw=1))
    o.append(_txt(270, 100, "R\u2082", 8, color=GREY))
    o.append(_txt(240, 26, "m\u1ea1ng h\u1ed3i ti\u1ebfp", 8, color=GREY))
    # output
    o.append(_line(212, yo, 340, yo, sw=1))
    o.append(_arrow(314, yo, 326, yo, sw=1))
    o.append(_txt(344, yo + 4, "e\u2080", 9, anchor="start", color=GREY))
    # notes
    o.append(_txt(235, 206, "R_ef = R\u2083 + (R\u2081\u00b7R\u2082)/(R\u2081+R\u2082)", 10, color=INK, weight="600"))
    o.append(_txt(235, 230, "R\u2084 b\u00f9 d\u00f2ng ph\u00e2n c\u1ef1c \u1edf l\u1ed1i v\u00e0o \u0111\u1ea3o", 8, color=GREY))
    return _fig(svg(470, 244, "".join(o), "M\u1ea1ch khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n t\u00edch th\u1ef1c d\u1ee5ng"),
                "H\u00ecnh 6-35 \u00b7 M\u1ea1ch khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n t\u00edch th\u1ef1c d\u1ee5ng. \u0110i\u1ec7n tr\u1edf h\u1ed3i ti\u1ebfp hi\u1ec7u d\u1ee5ng l\u00e0 h\u00e0m c\u1ee7a c\u00e1c \u0111i\u1ec7n tr\u1edf "
                "kh\u00e1c; ch\u1ecdn tr\u1ecb s\u1ed1 th\u00edch h\u1ee3p s\u1ebd gi\u1ea3m m\u1ea1nh \u0111\u1ed9 tr\u00f4i \u0111\u1ea7u ra. C\u00f3 th\u1ec3 n\u00e2ng \u0111\u1ed9 ch\u00ednh x\u00e1c b\u1eb1ng c\u00e1ch gh\u00e9p t\u1ea7ng "
                "hai hay nhi\u1ec1u khu\u1ebfch \u0111\u1ea1i, \u0111\u1ed3ng th\u1eddi c\u1ea3i thi\u1ec7n \u0111\u00e1ng k\u1ec3 t\u1ec9 s\u1ed1 t\u00edn hi\u1ec7u tr\u00ean t\u1ea1p \u00e2m. \u0110i\u1ec7n tr\u1edf R\u2084 \u1edf l\u1ed1i "
                "v\u00e0o \u0111\u1ea3o l\u00e0 c\u1ea7n thi\u1ebft v\u00ec d\u00f2ng ph\u00e2n c\u1ef1c.",
                "Figure 6.35 \u00b7 A practical charge amplifier. The effective feedback resistance is a function of the "
                "other resistors; choosing them well reduces output drift substantially. Accuracy improves by "
                "cascading two or more amplifiers, which also lifts the signal-to-noise ratio. R\u2084 at the inverting "
                "input is needed for bias current.",
                "M\u1ea1ch khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n t\u00edch th\u1ef1c d\u1ee5ng",
                "Practical charge amplifier")


def fig_6_36():
    o = [_defs()]
    # carrier with modulation envelope
    ox, oy = 56, 118
    o.append(_line(ox, oy, 620, oy, sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(ox - 6, oy + 4, "0", 8, anchor="end", color=GREY))
    pts = []
    for i in range(721):
        x = i / 720.0
        env = 1.0 - 0.55 * math.sin(2 * math.pi * 1.0 * x) ** 2
        yy = oy - 62 * env * math.sin(2 * math.pi * 14 * x)
        pts.append("%s %s" % (_f(ox + x * 560), _f(yy)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.1"/>' % (" ".join(pts), GOLD))
    # envelope
    for s in (1, -1):
        ep = []
        for i in range(181):
            x = i / 180.0
            env = 1.0 - 0.55 * math.sin(2 * math.pi * 1.0 * x) ** 2
            ep.append("%s %s" % (_f(ox + x * 560), _f(oy - s * 62 * env)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 3"/>'
                 % (" ".join(ep), GREY))
    o.append(_txt(ox + 300, 34, "bao hình", 8, color=GREY))
    o.append(_txt(ox + 300, 206, "giá trị trung bình = khoảng cách trung bình", 8.5, color=INK, weight="600"))
    o.append(_txt(ox + 300, 228, "sau tách sóng và lọc thông thấp → biên độ dao động", 8, color=GREY))
    return _fig(svg(660, 240, "".join(o), "Tín hiệu điều biên"),
                "Hình 6-36 · Tín hiệu điều biên. Một số cảm biến có thể được cấu hình để cho ra tín hiệu điều biên, như "
                "trường hợp cảm biến dịch chuyển rung động kiểu điện dung. Sau khi chỉnh lưu, giá trị trung bình của "
                "sóng cho khoảng cách trung bình giữa hai bản. Biên độ dao động quanh vị trí trung bình được tách ra "
                "bằng bộ tách sóng và mạch lọc thông thấp.",
                "Figure 6.36 · An amplitude-modulated signal. Some sensors can be configured to give an "
                "amplitude-modulated output, as with capacitive vibration-displacement sensors. Rectified, the mean "
                "value of the wave gives the mean plate separation. The vibration amplitude about that mean is "
                "extracted by a demodulator and low-pass filter.",
                "Tín hiệu điều biên",
                "Amplitude-modulated signal")


def fig_6_37():
    o = [_defs()]
    y = 96
    # two driven capacitors
    o.append(_rect(44, 62, 84, 30, "#fff"))
    o.append(_txt(86, 81, "e₁ (C₁)", 7.5))
    o.append(_rect(44, 108, 84, 30, "#fff"))
    o.append(_txt(86, 127, "e₂ (C₂)", 7.5))
    o.append(_txt(86, 54, "xung đối pha 400 kHz", 7.5, color=GREY))
    o.append(_arrow(128, 77, 152, 88, sw=1))
    o.append(_arrow(128, 123, 152, 112, sw=1))
    # differencing block
    o.append(_rect(152, 74, 56, 52, "#fff"))
    o.append(_txt(180, 96, "Σ", 12))
    o.append(_txt(180, 112, "−", 9))
    o.append(_arrow(208, 100, 232, 100, sw=1))
    # average
    o.append(_rect(232, 78, 66, 44, "#fff"))
    o.append(_txt(265, 96, "trung bình", 7.5))
    o.append(_txt(265, 110, "thông thấp", 7.5))
    o.append(_arrow(298, 100, 322, 100, sw=1))
    # output
    o.append(_txt(326, 104, "e₀", 9, anchor="start", color=GOLD, weight="600"))
    # waveform sketch
    bx, by, bw, amp, ncy = 372, 150, 200, 34, 6
    o.append(_line(bx, by, bx + bw, by, sw=0.8, color=GREY))
    step = bw / float(ncy * 2)
    d = ["M%s %s" % (_f(bx), _f(by - amp))]
    for k in range(ncy * 2):
        x0 = bx + k * step
        y = by - amp if k % 2 == 0 else by + amp
        d.append("L%s %s" % (_f(x0), _f(y)))
        d.append("L%s %s" % (_f(x0 + step), _f(y)))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(d), GOLD))
    o.append(_txt(bx + bw / 2.0, by + 56, "e₁ = e₂: sóng đối xứng, trung bình 0", 7.5, color=GREY))
    o.append(_txt(360, 228, "e₀ = −ei·(C₁ − C₂)/(C₁ + C₂) = −ei·xi/x₀", 9.5, color=INK, weight="600"))
    o.append(_txt(360, 250, "đầu ra tỉ lệ trực tiếp với dịch chuyển xi", 8, color=GOLD))
    return _fig(svg(660, 264, "".join(o), "Sơ đồ khối mạch tuyến tính hoá xung vuông"),
                "Hình 6-37 · Sơ đồ khối mạch tuyến tính hoá dạng xung vuông. Cách này đặc biệt hữu ích cho cảm biến "
                "điện dung vi sai. Điện áp trên hai tụ được cho đảo pha liên tục với tần số kích thích cao giữa mức "
                "kích thích và đất. Khi vị trí tương đối của các bản thay đổi do rung động, giá trị trung bình của "
                "điện áp ra lệch khỏi không và trở nên dương hoặc âm tuỳ chiều dịch chuyển.",
                "Figure 6.37 · Block diagram of a square-wave linearisation circuit. It is particularly useful for "
                "differential capacitive sensors. The voltages on the two capacitors are switched back and forth at "
                "a high excitation frequency between the excitation level and ground. As the relative plate "
                "positions change with vibration, the average output voltage shifts away from zero, becoming "
                "positive or negative with the direction of displacement.",
                "Sơ đồ khối mạch tuyến tính hoá xung vuông",
                "Square-wave linearisation block diagram")


# ---------------------------------------------------------------- 6.4
def _cube(cx, cy, s, shift=0.0, label_axes=True):
    """Oblique perovskite cell: 8 corner cations, face-centre anions, body-centre cation."""
    d = s * 0.42
    # front and back squares
    o = []
    o.append(_rect(cx - s / 2.0, cy - s / 2.0, s, s, "none", sw=1.2))
    o.append(_rect(cx - s / 2.0 + d, cy - s / 2.0 - d, s, s, "none", sw=0.9, dash="4 3"))
    for sx in (-1, 1):
        for sy in (-1, 1):
            o.append(_line(cx + sx * s / 2.0, cy + sy * s / 2.0,
                           cx + sx * s / 2.0 + d, cy + sy * s / 2.0 - d, sw=0.9, color=GREY))
    # corner cations (front square + back square)
    for px, py in ((cx - s / 2.0, cy - s / 2.0), (cx + s / 2.0, cy - s / 2.0),
                   (cx - s / 2.0, cy + s / 2.0), (cx + s / 2.0, cy + s / 2.0)):
        o.append('<circle cx="%s" cy="%s" r="7" fill="#c8b48a" stroke="%s" stroke-width=".8"/>'
                 % (_f(px), _f(py), INK))
        o.append('<circle cx="%s" cy="%s" r="7" fill="#c8b48a" stroke="%s" stroke-width=".8"/>'
                 % (_f(px + d), _f(py - d), INK))
    # face-centre anions
    fc = [(cx, cy - s / 2.0), (cx, cy + s / 2.0), (cx - s / 2.0, cy), (cx + s / 2.0, cy)]
    for px, py in fc:
        o.append('<circle cx="%s" cy="%s" r="5" fill="#9fc6e8" stroke="%s" stroke-width=".7"/>'
                 % (_f(px), _f(py), INK))
    # body centre cation, optionally displaced upward
    o.append('<circle cx="%s" cy="%s" r="6.5" fill="#e0a24a" stroke="%s" stroke-width=".9"/>'
             % (_f(cx), _f(cy - shift), INK))
    if shift:
        o.append(_line(cx, cy, cx, cy - shift, sw=0.7, dash="2 2", color=GREY))
    return "".join(o)


def fig_6_38():
    o = [_defs()]
    # (a) converse effect
    o.append(_rect(112, 74, 96, 76, FILL))
    for xx in (136, 160, 184):
        o.append(_arrow(xx, 66, xx, 158, sw=0.9, color="#6b8fb3"))
    o.append(_txt(206, 64, "E", 9, anchor="start", color="#4a6b8a", weight="600"))
    o.append(_arrow(112, 112, 92, 112, sw=1.2, color=GOLD))
    o.append(_arrow(208, 112, 228, 112, sw=1.2, color=GOLD))
    o.append(_txt(160, 176, "vật liệu giãn ra", 8, color=GREY))
    o.append(_txt(160, 210, "(a) hiệu ứng nghịch", 8.5, color=INK, weight="600"))
    o.append(_txt(160, 228, "điện trường → biến dạng", 8, color=GREY))
    # (b) direct effect
    o.append(_rect(444, 74, 96, 76, FILL))
    o.append(_arrow(492, 34, 492, 66, sw=1.2, color=GOLD))
    o.append(_txt(500, 40, "F", 9, anchor="start", color=GOLD, weight="600"))
    for xx in (462, 492, 522):
        o.append(_txt(xx, 70, "+", 10, color="#b03a2e", weight="600"))
        o.append(_txt(xx, 166, "−", 10, color="#1f618d", weight="600"))
    o.append(_line(444, 74, 540, 74, sw=1.6, color="#b03a2e"))
    o.append(_line(444, 150, 540, 150, sw=1.6, color="#1f618d"))
    o.append(_txt(492, 190, "Q = d₃₃·F", 9, color=INK, weight="600"))
    o.append(_txt(492, 210, "(b) hiệu ứng thuận", 8.5, color=INK, weight="600"))
    o.append(_txt(492, 228, "lực → điện tích bề mặt", 8, color=GREY))
    return _fig(svg(660, 244, "".join(o), "Hiệu ứng áp điện thuận và nghịch"),
                "Hình 6-38 · Sơ đồ hiệu ứng áp điện thuận và nghịch. (a) Điện trường đặt lên vật liệu làm thay đổi "
                "hình dạng của nó — đây là chức năng chấp hành. (b) Một lực tác dụng lên vật liệu sinh ra điện tích "
                "mặt — đây là chức năng cảm nhận, và điện tích tỉ lệ với lực qua hệ số d₃₃.",
                "Figure 6.38 · The direct and converse piezoelectric effect. (a) An electric field applied to the "
                "material changes its shape — the actuating function. (b) A stress on the material yields a surface "
                "charge proportional to the force through d₃₃ — the sensing function.",
                "Hiệu ứng áp điện thuận và nghịch",
                "Direct and converse piezoelectric effect")


def fig_6_39():
    o = [_defs()]
    import random as _rnd
    _rnd.seed(11)
    for panel, (bx, aligned) in enumerate(((60, False), (368, True))):
        o.append(_rect(bx, 56, 180, 132, "#fbfbfb"))
        for i in range(3):
            for j in range(3):
                gx = bx + 30 + i * 60
                gy = 76 + j * 42
                ang = 0 if aligned else _rnd.choice([-70, -35, 15, 55, 100, 145, 190])
                o.append('<g transform="translate(%s,%s) rotate(%s)">'
                         '<line x1="-14" y1="0" x2="14" y2="0" stroke="%s" stroke-width="1.4" '
                         'marker-end="url(#a6)"/></g>' % (_f(gx), _f(gy), ang, GOLD))
        o.append(_txt(bx + 90, 208, "chưa phân cực — mômen triệt tiêu" if not aligned
                      else "sau phân cực — mômen cùng chiều", 8, color=GREY))
        o.append(_txt(bx + 90, 228, "(a)" if not aligned else "(b)", 9, color=INK, weight="600"))
    o.append(_arrow(300, 122, 340, 122, sw=1.3, color="#6b8fb3"))
    o.append(_txt(320, 112, "E", 9, color="#4a6b8a", weight="600"))
    o.append(_txt(320, 140, "phân cực", 7.5, color=GREY))
    return _fig(svg(660, 244, "".join(o), "Quá trình phân cực gốm áp điện"),
                "Hình 6-39 · Sơ đồ quá trình phân cực gốm áp điện. (a) Khi không có điện trường, các đômen có hướng "
                "phân cực ngẫu nhiên nên mômen tổng bằng không và gốm không có tính áp điện. (b) Dưới điện trường một "
                "chiều mạnh, phân cực trong các đômen định hướng theo chiều điện trường; gốm còn lại một phân cực "
                "tổng dọc trục phân cực.",
                "Figure 6.39 · Poling of a piezoelectric ceramic. (a) With no field the domains have randomly oriented "
                "polarization, the net moment is zero and the ceramic is not piezoelectric. (b) Under a strong dc "
                "field the polarization within each domain aligns with the field, leaving a net polarization along "
                "the poling axis.",
                "Quá trình phân cực gốm áp điện",
                "Poling of a piezoelectric ceramic")


def fig_6_40():
    o = [_defs()]
    o.append(_cube(150, 130, 108, 0))
    o.append(_txt(150, 222, "(a) pha lập phương, T > T₀", 8.5, color=INK, weight="600"))
    o.append(_txt(150, 240, "tâm điện tích dương trùng tâm âm", 8, color=GREY))
    o.append(_cube(480, 130, 108, 14))
    o.append(_arrow(496, 128, 496, 108, sw=1.0, color=GOLD))
    o.append(_txt(504, 116, "lệch", 7.5, anchor="start", color=GOLD))
    o.append(_txt(480, 222, "(b) pha tứ giác, T < T₀", 8.5, color=INK, weight="600"))
    o.append(_txt(480, 240, "Ti⁴⁺ lệch khỏi tâm so với O²⁻", 8, color=GREY))
    # legend
    o.append('<circle cx="300" cy="96" r="6" fill="#c8b48a" stroke="%s" stroke-width=".8"/>' % INK)
    o.append(_txt(312, 100, "Ba²⁺", 8, anchor="start", color=GREY))
    o.append('<circle cx="300" cy="126" r="5" fill="#9fc6e8" stroke="%s" stroke-width=".7"/>' % INK)
    o.append(_txt(312, 130, "O²⁻", 8, anchor="start", color=GREY))
    o.append('<circle cx="300" cy="156" r="6" fill="#e0a24a" stroke="%s" stroke-width=".9"/>' % INK)
    o.append(_txt(312, 160, "Ti⁴⁺", 8, anchor="start", color=GREY))
    return _fig(svg(660, 254, "".join(o), "Cấu trúc tinh thể BaTiO3"),
                "Hình 6-40 · Cấu trúc tinh thể của BaTiO₃. (a) Trên điểm Curie, ô mạng là lập phương và tâm điện tích "
                "dương (Ba²⁺, Ti⁴⁺) trùng với tâm điện tích âm (O²⁻), nên không có mômen lưỡng cực. (b) Dưới điểm "
                "Curie, ô mạng chuyển sang tứ giác với Ti⁴⁺ dịch khỏi tâm so với các ion O²⁻, hình thành lưỡng cực "
                "điện — nguồn gốc của tính sắt điện và tính áp điện.",
                "Figure 6.40 · The crystal structure of BaTiO₃. (a) Above the Curie point the cell is cubic and the "
                "centre of positive charge (Ba²⁺, Ti⁴⁺) coincides with the centre of negative charge (O²⁻), so there "
                "is no dipole. (b) Below the Curie point the cell is tetragonal with Ti⁴⁺ displaced from the centre "
                "relative to the O²⁻ ions, forming electric dipoles — the origin of ferroelectricity and "
                "piezoelectricity.",
                "Cấu trúc tinh thể BaTiO3",
                "BaTiO3 crystal structure")


def fig_6_41():
    o = [_defs()]
    steps = [
        ("Cân nguyên liệu tinh khiết theo tỉ lệ", "oxit, cacbonat"),
        ("Trộn cơ học hoặc hoá học", "mixing"),
        ("Nung sơ bộ (calcination)", "pha áp điện hình thành"),
        ("Nghiền thành hạt mịn", "milling"),
        ("Tạo hình", "ép bột, đúc băng, đúc trượt, đùn"),
        ("Loại chất kết dính", "500–600 °C"),
        ("Thiêu kết", "khí quyển PbO cho hệ chứa chì"),
        ("Mạ điện cực và phân cực", "điện trường một chiều mạnh"),
        ("Gia công tinh và đặc trưng hoá", "đo d₃₃, k, ε"),
    ]
    x, w = 190, 280
    for i, (name, note) in enumerate(steps):
        y = 26 + i * 46
        fill = "#f6e6c8" if i in (2, 6, 7) else "#fff"
        o.append(_rect(x, y, w, 32, fill))
        o.append(_txt(x + w / 2.0, y + 15, name, 8.5))
        o.append(_txt(x + w / 2.0, y + 27, note, 7, color=GREY))
        if i < len(steps) - 1:
            o.append(_arrow(x + w / 2.0, y + 32, x + w / 2.0, y + 44, sw=1))
    o.append(_txt(560, 200, "các bước then chốt", 7.5, anchor="start", color=GREY))
    o.append(_line(556, 196, 474, 150, sw=0.7, color=GREY))
    return _fig(svg(660, 450, "".join(o), "Lưu đồ chế tạo gốm áp điện"),
                "Hình 6-41 · Lưu đồ quy trình chế tạo gốm áp điện theo phương pháp oxit. Từng bước đều phải được kiểm "
                "soát chặt chẽ vì tính chất cơ–điện của gốm phụ thuộc mạnh vào điều kiện chế tạo. Ba bước then chốt "
                "được tô đậm: nung sơ bộ để hình thành pha áp điện, thiêu kết để đạt mật độ tối ưu, và phân cực để "
                "gốm có tính áp điện.",
                "Figure 6.41 · Flow chart of the oxide route for piezoelectric ceramics. Every step must be controlled "
                "closely, because the electromechanical properties depend strongly on processing conditions. The "
                "three highlighted steps are the critical ones: calcination to form the piezoelectric phase, "
                "sintering to reach optimum density, and poling to make the ceramic piezoelectric.",
                "Lưu đồ chế tạo gốm áp điện",
                "Processing flow chart for piezoelectric ceramics")


def fig_6_42():
    o = [_defs()]
    # ---- (a) equivalent circuit: C0 in parallel with R1-L1-C1
    xa, xb = 70, 310
    yt, yb = 80, 150
    o.append(_line(xa, yt, xa, yb, sw=1))
    o.append(_line(xb, yt, xb, yb, sw=1))
    # top path with C0
    o.append(_line(xa, yt, 184, yt, sw=1))
    o.append(_line(196, yt, xb, yt, sw=1))
    o.append(_line(184, yt - 12, 184, yt + 12, sw=1.4))
    o.append(_line(196, yt - 12, 196, yt + 12, sw=1.4))
    o.append(_txt(190, yt - 20, "C\u2080", 8.5, color=GOLD, weight="600"))
    # bottom path: R1 - L1 - C1 in series
    o.append(_line(xa, yb, 90, yb, sw=1))
    o.append(_res(90, yb, 40))
    o.append(_line(130, yb, 148, yb, sw=1))
    for k in range(4):
        o.append('<path d="M%s %s a6 6 0 1 1 12 0" fill="none" stroke="%s" stroke-width="1.1"/>'
                 % (_f(148 + k * 9), _f(yb - 6), INK))
    o.append(_line(184, yb, 198, yb, sw=1))
    o.append(_line(198, yb - 12, 198, yb + 12, sw=1.4))
    o.append(_line(208, yb - 12, 208, yb + 12, sw=1.4))
    o.append(_line(208, yb, xb, yb, sw=1))
    o.append(_txt(110, yb + 20, "R\u2081", 8, color=GREY))
    o.append(_txt(166, yb + 20, "L\u2081", 8, color=GREY))
    o.append(_txt(203, yb + 20, "C\u2081", 8, color=GREY))
    o.append(_txt(190, yb + 44, "(a) m\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng g\u1ea7n c\u1ed9ng h\u01b0\u1edfng", 8.5, color=INK, weight="600"))
    o.append(_txt(190, yb + 62, "C\u2080 song song v\u1edbi nh\u00e1nh n\u1ed1i ti\u1ebfp R\u2081\u2013L\u2081\u2013C\u2081", 7.5, color=GREY))
    # ---- (b) reactance
    ox, oy = 400, 150
    o.append(_line(ox, oy, 630, oy, sw=1))
    o.append(_line(ox, 40, ox, 258, sw=1))
    o.append(_arrow(630, oy, 642, oy, sw=1))
    fs, fp = 1.0, 1.10
    seg = []
    for i in range(721):
        f = 0.70 + i * (0.62 / 720.0)
        den = (f * f - fp * fp) * f
        if abs(den) < 1e-5:
            continue
        X = -(f * f - fs * fs) / den
        yy = oy - X * 46
        if 42 < yy < 256:
            seg.append("%s %s" % (_f(ox + (f - 0.70) * 300), _f(yy)))
        else:
            if seg:
                o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>'
                         % (" ".join(seg), GOLD))
            seg = []
    if seg:
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(seg), GOLD))
    for ff, lab in ((fs, "f_s"), (fp, "f_p")):
        xx = ox + (ff - 0.70) * 300
        o.append(_line(xx, 40, xx, 258, sw=0.7, dash="3 3", color=GREY))
        o.append(_txt(xx, 272, lab, 8, color=GREY))
    o.append(_txt(ox - 8, 52, "X", 8.5, anchor="end"))
    o.append(_txt(636, oy + 18, "f", 8.5, anchor="end"))
    o.append(_txt(ox + 148, 66, "c\u1ea3m \u1ee9ng", 7.5, color=GREY))
    o.append(_txt(ox + 14, 214, "\u0111i\u1ec7n dung", 7.5, anchor="start", color=GREY))
    o.append(_txt(520, 296, "(b) \u0111i\u1ec7n kh\u00e1ng theo t\u1ea7n s\u1ed1", 8.5, color=INK, weight="600"))
    return _fig(svg(660, 310, "".join(o), "M\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng v\u00e0 \u0111i\u1ec7n kh\u00e1ng c\u1ee7a m\u1eabu \u00e1p \u0111i\u1ec7n"),
                "H\u00ecnh 6-42 \u00b7 (a) M\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng c\u1ee7a m\u1eabu \u00e1p \u0111i\u1ec7n g\u1ea7n c\u1ed9ng h\u01b0\u1edfng c\u01a1\u2013\u0111i\u1ec7n c\u01a1 b\u1ea3n: \u0111i\u1ec7n dung t\u0129nh C\u2080 m\u1eafc song song v\u1edbi nh\u00e1nh "
                "n\u1ed1i ti\u1ebfp R\u2081\u2013L\u2081\u2013C\u2081 \u0111\u1ea1i di\u1ec7n cho ph\u1ea7n c\u01a1. (b) \u0110i\u1ec7n kh\u00e1ng c\u1ee7a m\u1eabu theo t\u1ea7n s\u1ed1. T\u1ea1i t\u1ea7n s\u1ed1 c\u1ed9ng "
                "h\u01b0\u1edfng n\u1ed1i ti\u1ebfp f_s \u0111i\u1ec7n kh\u00e1ng b\u1eb1ng kh\u00f4ng; gi\u1eefa f_s v\u00e0 f_p m\u1eabu mang t\u00ednh c\u1ea3m \u1ee9ng; ngo\u00e0i kho\u1ea3ng \u1ea5y "
                "m\u1eabu mang t\u00ednh \u0111i\u1ec7n dung.",
                "Figure 6.42 \u00b7 (a) Equivalent circuit of a piezoelectric sample near its fundamental "
                "electromechanical resonance: the static capacitance C\u2080 in parallel with a series "
                "R\u2081\u2013L\u2081\u2013C\u2081 branch representing the mechanical part. (b) Reactance against "
                "frequency. At the series resonance f_s the reactance is zero; between f_s and f_p the sample is "
                "inductive; outside that band it is capacitive.",
                "M\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng v\u00e0 \u0111i\u1ec7n kh\u00e1ng c\u1ee7a m\u1eabu \u00e1p \u0111i\u1ec7n",
                "Equivalent circuit and reactance of a piezoelectric sample")


def fig_6_43():
    o = [_defs()]

    def par(x, yt, yb, kind, lab, colour=GREY):
        """One element hanging between two rails, plus its label below the bottom rail."""
        s = []
        if kind == "res":
            s.append(_line(x, yt, x, 100, sw=1))
            s.append(_res(x, 100, 34, horiz=False))
            s.append(_line(x, 134, x, yb, sw=1))
        elif kind == "cap":
            s.append(_line(x, yt, x, 112, sw=1))
            s.append(_line(x - 16, 112, x + 16, 112, sw=1.4))
            s.append(_line(x - 16, 120, x + 16, 120, sw=1.4))
            s.append(_line(x, 120, x, yb, sw=1))
        s.append(_txt(x, yb + 16, lab, 7.5, color=colour))
        return "".join(s)

    # ---- (a) full equivalent circuit
    yt, yb = 84, 180
    o.append(_line(56, yt, 316, yt, sw=1))
    o.append(_line(56, yb, 316, yb, sw=1))
    # charge generator
    o.append(_line(56, yt, 56, yb, sw=1))
    o.append('<circle cx="56" cy="132" r="13" fill="#fff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_arrow(56, 145, 56, 119, sw=1))
    o.append(_txt(34, 136, "Q", 8, anchor="end", color=GOLD, weight="600"))
    o.append(par(110, yt, yb, "res", "Rs"))
    o.append(par(152, yt, yb, "cap", "Cs"))
    o.append(par(194, yt, yb, "cap", "Cc"))
    o.append(par(236, yt, yb, "res", "Ra"))
    o.append(par(278, yt, yb, "cap", "Ca"))
    o.append(_line(316, yt, 316, yb, sw=1))
    # output voltage across the rails
    o.append(_arrow(336, yt, 336, yb, sw=1.1, color=GOLD))
    o.append(_txt(346, 136, "V", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(200, 214, "(a) m\u1ea1ch \u0111\u1ea7y \u0111\u1ee7 v\u1edbi khu\u1ebfch \u0111\u1ea1i \u0111i\u1ec7n \u00e1p", 8.5, color=INK, weight="600"))

    # ---- (b) simplified
    yt2, yb2 = 84, 180
    o.append(_line(420, yt2, 580, yt2, sw=1))
    o.append(_line(420, yb2, 580, yb2, sw=1))
    o.append(_line(420, yt2, 420, yb2, sw=1))
    o.append('<circle cx="420" cy="132" r="13" fill="#fff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_arrow(420, 145, 420, 119, sw=1))
    o.append(_txt(398, 136, "I", 8, anchor="end", color=GOLD, weight="600"))
    o.append(par(480, yt2, yb2, "res", "R"))
    o.append(par(540, yt2, yb2, "cap", "C"))
    o.append(_line(580, yt2, 580, yb2, sw=1))
    o.append(_txt(500, 214, "(b) m\u1ea1ch r\u00fat g\u1ecdn", 8.5, color=INK, weight="600"))
    o.append(_txt(500, 232, "I = d\u2083\u2083\u00b7dF/dt", 8, color=GREY))
    return _fig(svg(660, 244, "".join(o), "M\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng c\u1ee7a c\u1ea3m bi\u1ebfn \u00e1p \u0111i\u1ec7n"),
                "H\u00ecnh 6-43 \u00b7 M\u1ea1ch \u0111i\u1ec7n t\u01b0\u01a1ng \u0111\u01b0\u01a1ng \u0111\u1ea7y \u0111\u1ee7 (a) v\u00e0 r\u00fat g\u1ecdn (b) c\u1ee7a c\u1ea3m bi\u1ebfn \u00e1p \u0111i\u1ec7n n\u1ed1i v\u1edbi khu\u1ebfch \u0111\u1ea1i "
                "\u0111i\u1ec7n \u00e1p. B\u1ed9 ph\u00e1t \u0111i\u1ec7n t\u00edch Q = d\u2083\u2083F m\u1eafc song song v\u1edbi \u0111i\u1ec7n tr\u1edf r\u00f2 Rs, \u0111i\u1ec7n dung \u0111\u1ea7u \u0111o Cs, \u0111i\u1ec7n dung "
                "d\u00e2y n\u1ed1i Cc, c\u00f9ng \u0111i\u1ec7n tr\u1edf v\u00e0 \u0111i\u1ec7n dung l\u1ed1i v\u00e0o khu\u1ebfch \u0111\u1ea1i Ra v\u00e0 Ca. \u0110i\u1ec7n \u00e1p ra V \u0111o tr\u00ean to\u00e0n b\u1ed9 "
                "n\u00e1m th\u00e0nh ph\u1ea7n song song \u1ea5y.",
                "Figure 6.43 \u00b7 Full (a) and simplified (b) equivalent circuits of a piezoelectric sensor "
                "connected to a voltage amplifier. The charge generator Q = d\u2083\u2083F sits in parallel with the "
                "transducer leakage resistance Rs, transducer capacitance Cs, cable capacitance Cc, and the "
                "amplifier input resistance and capacitance Ra and Ca. The output voltage V appears across that "
                "whole parallel combination.",
                "M\u1ea1ch t\u01b0\u01a1ng \u0111\u01b0\u01a1ng c\u1ee7a c\u1ea3m bi\u1ebfn \u00e1p \u0111i\u1ec7n",
                "Equivalent circuit of a piezoelectric sensor")


def fig_6_44():
    o = [_defs()]
    yi, yo = 100, 110
    o.append(_line(52, yi, 170, yi, sw=1))
    o.append(_txt(52, yi - 9, "Q", 8, anchor="start", color=GOLD, weight="600"))
    # transducer capacitance to ground
    o.append(_line(100, yi, 100, 130, sw=1))
    o.append(_line(84, 130, 116, 130, sw=1.4))
    o.append(_line(84, 138, 116, 138, sw=1.4))
    o.append(_line(100, 138, 100, 156, sw=1))
    o.append(_gnd(100, 156))
    o.append(_txt(122, 138, "Cs", 8, anchor="start", color=GREY))
    o.append(_opamp(170, 91))
    # feedback Cf and optional Rf
    o.append(_line(160, yi, 160, 46, sw=1))
    o.append(_line(160, 46, 210, 46, sw=1))
    o.append(_line(216, 36, 216, 56, sw=1.4))
    o.append(_line(224, 36, 224, 56, sw=1.4))
    o.append(_line(230, 46, 268, 46, sw=1))
    o.append(_line(268, 46, 268, yo, sw=1))
    o.append(_txt(220, 28, "Cf", 8.5, color=GOLD, weight="600"))
    # Rf dashed in parallel
    o.append(_line(160, 46, 160, 24, sw=1, dash="4 3", color=GREY))
    o.append(_line(160, 24, 186, 24, sw=1, dash="4 3", color=GREY))
    o.append(_res(186, 24, 34))
    o.append(_line(220, 24, 268, 24, sw=1, dash="4 3", color=GREY))
    o.append(_line(268, 24, 268, 46, sw=1, dash="4 3", color=GREY))
    o.append(_txt(203, 14, "Rf", 8, color=GREY))
    # output
    o.append(_line(214, yo, 316, yo, sw=1))
    o.append(_arrow(288, yo, 300, yo, sw=1))
    o.append(_txt(320, yo + 4, "V", 9, anchor="start", color=GREY))
    o.append(_txt(210, 186, "V = −Q/Cf = −d₃₃F/Cf", 10, color=INK, weight="600"))
    o.append(_txt(210, 208, "Rf (nét đứt) chống nạp Cf do dòng vào, tránh bão hoà", 7.5, color=GREY))
    return _fig(svg(460, 220, "".join(o), "Mạch khuếch đại điện tích cho cảm biến áp điện"),
                "Hình 6-44 · Mạch tương đương của cảm biến áp điện nối với khuếch đại điện tích. Khuếch đại thuật "
                "toán dùng lối vào FET, có tụ Cf trong mạch hồi tiếp; khi ấy đầu ra không phụ thuộc tần số và chỉ do "
                "d₃₃ cùng Cf quyết định. Điện trở Rf (nét đứt) được thêm vào để tránh việc dòng vào nhỏ của khuếch "
                "đại nạp dần tụ hồi tiếp và làm bão hoà đầu ra.",
                "Figure 6.44 · Equivalent circuit of a piezoelectric sensor connected to a charge amplifier. A "
                "FET-input operational amplifier has Cf in its feedback loop, so the output is frequency independent "
                "and set only by d₃₃ and Cf. The shunt resistor Rf (dashed) is added to stop the amplifier’s small "
                "input current from charging the feedback capacitor and saturating the output.",
                "Mạch khuếch đại điện tích cho cảm biến áp điện",
                "Charge amplifier for a piezoelectric sensor")


def fig_6_45():
    o = [_defs()]
    # (a) bimorph cantilever
    o.append(_rect(46, 96, 40, 24, "#b9b9b9"))
    o.append(_txt(66, 88, "kẹp", 7.5, color=GREY))
    o.append(_rect(86, 92, 190, 14, FILL))
    o.append(_rect(86, 106, 190, 14, "#e8d7b0"))
    o.append(_line(86, 106, 276, 106, sw=1.4))
    o.append(_txt(140, 100, "P↑", 7.5, color="#b03a2e"))
    o.append(_txt(140, 116, "P↓", 7.5, color="#1f618d"))
    o.append(_line(86, 92, 276, 92, sw=1.2))
    o.append(_line(86, 120, 276, 120, sw=1.2))
    # deflected tip
    pts = []
    for i in range(41):
        s = i / 40.0
        pts.append("%s %s" % (_f(86 + s * 190), _f(92 - 22 * s * s)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>'
             % (" ".join(pts), GOLD))
    o.append(_arrow(276, 92, 276, 62, sw=1.1, color=GOLD))
    o.append(_txt(284, 70, "∆l", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(180, 156, "(a) bimorph gốm — cảm biến dịch chuyển", 8.5, color=INK, weight="600"))
    o.append(_txt(180, 174, "hai dầm phân cực ngược, điện cực chung ở giữa", 7.5, color=GREY))
    # (b) polymer diaphragm microphone
    cx, cy, r = 500, 104, 62
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#eef4ea" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx), _f(cy), _f(r), INK))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 3"/>'
             % (_f(cx), _f(cy), _f(r - 10), GREY))
    o.append(_txt(cx, cy + 4, "màng polymer", 7.5, color="#4a6b3a"))
    for i in range(5):
        xx = cx - 40 + i * 20
        o.append(_arrow(xx, 26, xx, 40, sw=1, color="#6b8fb3"))
    o.append(_txt(cx + 52, 30, "p", 9, anchor="start", color="#4a6b8a", weight="600"))
    o.append(_txt(cx, 190, "(b) màng polymer — cảm biến áp suất", 8.5, color=INK, weight="600"))
    o.append(_txt(cx, 208, "hai lớp phân cực ngược kẹp ở chu vi, tạo micro", 7.5, color=GREY))
    return _fig(svg(660, 222, "".join(o), "Cảm biến dịch chuyển và áp suất kiểu áp điện"),
                "Hình 6-45 · Sơ đồ kết cấu cảm biến dịch chuyển dùng gốm áp điện (a) và cảm biến áp suất dùng màng "
                "polymer áp điện (b). Mũi tên chỉ chiều phân cực sắt điện trong vật liệu. Ở bimorph, hai dầm phân cực "
                "ngược được gắn với nhau, một điện cực chung ở giữa và hai điện cực ở mặt ngoài; khi uốn, dầm trên "
                "giãn còn dầm dưới nén, nên điện tích sinh ra cùng dấu ở hai dầm mắc nối tiếp.",
                "Figure 6.45 · Schematic of a displacement sensor based on piezoelectric ceramic (a) and a pressure "
                "sensor based on piezoelectric polymer film (b). Arrows show the direction of ferroelectric "
                "polarization. In the bimorph, two oppositely poled beams are cemented together with one common "
                "electrode in the middle and two on the outer faces; on bending, the upper beam stretches and the "
                "lower compresses, so the two series-connected beams deliver charge of the same polarity.",
                "Cảm biến dịch chuyển và áp suất kiểu áp điện",
                "Piezoelectric displacement and pressure sensors")


# ---------------------------------------------------------------- 6.5
def _beam(x1, y1, x2, y2, color="#c0392b", sw=1.4):
    return _line(x1, y1, x2, y2, sw=sw, color=color)


def _mirror(x, y, ang=0, w=22):
    """Flat mirror drawn as a thick bar rotated about its centre."""
    return ('<g transform="translate(%s,%s) rotate(%s)"><line x1="0" y1="%s" x2="0" y2="%s" '
            'stroke="%s" stroke-width="3"/><line x1="-4" y1="%s" x2="-4" y2="%s" stroke="%s" '
            'stroke-width="0.7" stroke-dasharray="2 2"/></g>'
            % (_f(x), _f(y), ang, _f(-w / 2.0), _f(w / 2.0), INK, _f(-w / 2.0), _f(w / 2.0), GREY))


def _bsplit(x, y, s=16):
    """Beam-splitter square drawn at 45°."""
    return ('<g transform="translate(%s,%s) rotate(45)"><rect x="%s" y="%s" width="%s" height="%s" '
            'fill="#e8eef4" stroke="%s" stroke-width="1.1"/></g>'
            % (_f(x), _f(y), _f(-s / 2.0), _f(-s / 2.0), _f(s), _f(s), INK))


def fig_6_46():
    o = [_defs()]
    y = 110
    # tube
    o.append(_rect(70, y - 22, 300, 44, "#f7fbff", sw=1.2))
    o.append(_rect(70, y - 22, 300, 44, "none", sw=0))
    o.append(_txt(220, 44, "ống phóng điện", 8, color=GREY))
    # Brewster windows
    for xx in (86, 354):
        o.append(_line(xx - 8, y + 18, xx + 8, y - 18, sw=2, color="#7fa8c9"))
    o.append(_txt(86, y + 34, "cửa sổ Brewster", 7, color=GREY))
    # gas fill
    o.append(_txt(220, 76, "He³ ≈ 10⁵ Pa  ·  Ne²⁰ ≈ 13 Pa", 8, color="#4a6b8a"))
    # electrodes
    o.append(_rect(120, y - 14, 18, 28, "#b9b9b9"))
    o.append(_rect(300, y - 14, 18, 28, "#b9b9b9"))
    o.append(_txt(129, y + 34, "anôt", 7, color=GREY))
    o.append(_txt(309, y + 34, "catôt", 7, color=GREY))
    o.append(_line(129, y + 14, 129, y + 44, sw=1))
    o.append(_line(309, y + 14, 309, y + 44, sw=1))
    o.append(_rect(180, y + 44, 80, 26, "#fff"))
    o.append(_txt(220, y + 61, "nguồn kV", 7.5))
    o.append(_line(129, y + 44, 180, y + 57, sw=1))
    o.append(_line(309, y + 44, 260, y + 57, sw=1))
    # mirrors
    o.append(_mirror(60, y, 0, 46))
    o.append(_mirror(380, y, 0, 46))
    o.append(_txt(60, y - 34, "gương sau", 7, color=GREY))
    o.append(_txt(380, y - 34, "gương ra", 7, color=GREY))
    # beam
    o.append(_beam(60, y, 470, y))
    o.append(_arrow(444, y, 458, y, sw=1.2, color="#c0392b"))
    o.append(_txt(470, y + 4, "λ ≈ 633 nm", 8, anchor="start", color="#c0392b"))
    # cavity length
    o.append(_line(60, y + 96, 380, y + 96, sw=0.7, color=GREY))
    o.append(_line(60, y + 90, 60, y + 102, sw=0.7, color=GREY))
    o.append(_line(380, y + 90, 380, y + 102, sw=0.7, color=GREY))
    o.append(_txt(220, y + 112, "chiều dài hốc cộng hưởng L = m·λ/2", 8, color=GREY))
    return _fig(svg(660, 240, "".join(o), "Sơ đồ laser He–Ne"),
                "Hình 6-46 · Sơ đồ laser heli–neon. Ống phóng điện chứa khí heli đơn đồng vị (He³) ở áp suất riêng "
                "phần ≈ 10⁵ Pa và neon (Ne²⁰) ở ≈ 13 Pa, được bơm điện bằng điện áp cỡ kilôvôn với dòng vài miliampe. "
                "Heli chỉ làm nhiệm vụ kích thích neon; các nguyên tử neon bị kích thích phát xạ cảm ứng ánh sáng rất "
                "kết hợp. Hai gương ở hai đầu hốc cộng hưởng phản xạ phần lớn ánh sáng, cho nó đi qua môi trường hoạt "
                "động nhiều lần và khuếch đại mạnh khi L là bội số nguyên của λ/2.",
                "Figure 6.46 · Schematic of the helium–neon laser. The discharge tube holds single-isotope helium "
                "(He³) at a partial pressure of ≈10⁵ Pa and neon (Ne²⁰) at ≈13 Pa, pumped electrically at a few "
                "kilovolts and a few milliamperes. Helium only serves to excite the neon; the excited neon atoms emit "
                "highly coherent light by stimulated emission. The two cavity mirrors reflect most of the light, "
                "sending it through the active volume many times and amplifying it strongly when L is an integer "
                "multiple of λ/2.",
                "Sơ đồ laser He–Ne",
                "Helium–neon laser schematic")


def fig_6_47():
    o = [_defs()]
    ox, oy = 70, 190
    o.append(_line(ox, oy, 620, oy, sw=1))
    o.append(_line(ox, oy, ox, 50, sw=1))
    o.append(_arrow(620, oy, 632, oy, sw=1))
    o.append(_arrow(ox, 50, ox, 38, sw=1))
    # gain envelope
    pts = []
    for i in range(101):
        u = i / 100.0
        g = math.exp(-((u - 0.5) ** 2) / (2 * 0.16 ** 2))
        pts.append("%s %s" % (_f(ox + u * 520), _f(oy - g * 116)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), GREY))
    o.append(_txt(ox + 260, 62, "đường bao khuếch đại", 8, color=GREY))
    # axial modes
    for k in range(-4, 5):
        u = 0.5 + k * 0.083
        g = math.exp(-((u - 0.5) ** 2) / (2 * 0.16 ** 2))
        xx = ox + u * 520
        o.append(_line(xx, oy, xx, oy - g * 116, sw=1.8, color=GOLD))
    o.append(_txt(ox + 60, oy - 96, "các mode dọc", 8, anchor="start", color=GOLD, weight="600"))
    # spacing
    x1 = ox + (0.5 - 0.083) * 520
    x2 = ox + 0.5 * 520
    o.append(_line(x1, oy + 14, x2, oy + 14, sw=0.9))
    o.append(_line(x1, oy + 9, x1, oy + 19, sw=0.9))
    o.append(_line(x2, oy + 9, x2, oy + 19, sw=0.9))
    o.append(_txt((x1 + x2) / 2.0, oy + 30, "∆f = c/(2n_M L)", 8, color=INK, weight="600"))
    o.append(_txt(620, oy + 18, "f", 8.5, anchor="end"))
    return _fig(svg(660, 236, "".join(o), "Nhiều mode cộng hưởng của laser He–Ne"),
                "Hình 6-47 · Laser He–Ne có thể có nhiều mode cộng hưởng (vẽ cho chiều dài hốc ≈ 20 cm). Đường bao "
                "khuếch đại rộng cỡ gigahéc, nên nhiều mode dọc cùng cộng hưởng; khoảng cách giữa hai mode kề nhau là "
                "dải phổ tự do ∆f, chỉ phụ thuộc chiều dài hốc L, chiết suất môi trường hoạt động n_M và tốc độ ánh "
                "sáng c. Nhiều mode đồng thời làm phát sinh tần số phách, giới hạn tính kết hợp thời gian và khiến "
                "laser không dùng được cho giao thoa kế.",
                "Figure 6.47 · A He–Ne laser can have multiple resonating modes (drawn for a ≈20 cm cavity). The gain "
                "envelope is gigahertz wide, so several longitudinal modes resonate together; the spacing between "
                "adjacent modes is the free spectral range ∆f, which depends only on the cavity length L, the "
                "refractive index n_M of the active medium and the speed of light c. Multiple modes produce a beat "
                "frequency that limits temporal coherence and makes the laser unusable for interferometry.",
                "Nhiều mode cộng hưởng của laser He–Ne",
                "Multiple axial modes of a He–Ne laser")


def fig_6_48():
    o = [_defs()]
    y = 92
    # axial permanent magnet
    o.append(_rect(46, 50, 242, 13, "#c9c9c9"))
    o.append(_rect(46, 118, 242, 13, "#c9c9c9"))
    o.append(_txt(167, 44, "nam châm vĩnh cửu dọc trục", 8, color=GREY))
    for xx in (80, 118, 156, 194, 232):
        o.append(_arrow(xx, 64, xx, 76, sw=0.8, color="#6b8fb3"))
        o.append(_arrow(xx, 117, xx, 105, sw=0.8, color="#6b8fb3"))
    # tube
    o.append(_rect(64, 79, 214, 26, "#f7fbff"))
    o.append(_txt(171, 96, "ống laser", 7.5, color="#4a6b8a"))
    o.append(_mirror(56, y, 0, 36))
    o.append(_mirror(282, y, 0, 36))
    # piezo actuator on the output mirror
    o.append(_beam(284, y, 470, y))
    o.append(_rect(292, 80, 14, 24, "#e0a24a"))
    o.append(_txt(310, 98, "piezo", 7, anchor="start", color=GREY))
    # heater
    o.append(_rect(64, 140, 200, 8, "#f0c9a8"))
    o.append(_txt(164, 162, "lò điện trở (điều khiển chậm)", 7.5, color=GREY))
    # beam out
    o.append(_txt(474, y + 4, "ra", 8, anchor="start", color="#c0392b"))
    # detector tap and electronics
    o.append(_line(430, y, 430, 176, sw=0.8, dash="3 3", color=GREY))
    o.append(_arrow(430, 168, 430, 176, sw=0.8, color=GREY))
    o.append(_rect(392, 176, 74, 26, "#fff"))
    o.append(_txt(429, 193, "tách mode", 7.5))
    o.append(_rect(492, 176, 74, 26, "#fff"))
    o.append(_txt(529, 193, "so pha", 7.5))
    o.append(_arrow(466, 189, 488, 189, sw=1))
    o.append(_arrow(566, 189, 588, 189, sw=1))
    o.append(_txt(592, 193, "∆f", 8, anchor="start", color=GOLD, weight="600"))
    # feedback to the piezo
    o.append(_line(529, 202, 529, 230, sw=1))
    o.append(_line(529, 230, 299, 230, sw=1))
    o.append(_line(299, 230, 299, 106, sw=1))
    o.append(_arrow(299, 114, 299, 105, sw=1))
    o.append(_txt(414, 224, "hồi tiếp: điều khiển chiều dài hốc", 7.5, color=GREY))
    return _fig(svg(660, 262, "".join(o), "Ổn định tần số bằng hiệu ứng Zeeman dọc"),
                "Hình 6-48 · Có thể ổn định bước sóng laser nhờ hiệu ứng Zeeman. Ống laser nằm trong một nam châm vĩnh "
                "cửu dọc trục; từ trường làm các tần số chuyển mức của neon tách đối xứng quanh tần số danh định, và "
                "mode dọc duy nhất của laser tách thành hai mode phân cực tròn phải và trái lệch nhau cỡ 1,5 MHz. "
                "Hiệu số tần số này đạt cực trị khi tần số laser trùng đúng tần số chuyển mức nguyên tử; vì vậy "
                "người ta điều khiển chiều dài hốc — bằng lò điện trở cho thay đổi chậm và bằng bộ chấp hành áp điện "
                "cho thay đổi nhanh — để khoá tần số vào cực trị ấy.",
                "Figure 6.48 · The laser wavelength can be stabilised with the Zeeman effect. The tube sits inside an "
                "axial permanent magnet; the field splits the neon transition frequencies symmetrically about the "
                "nominal one, and the single longitudinal mode splits into right and left circularly polarised modes "
                "about 1.5 MHz apart. That difference peaks when the laser frequency matches the atomic transition "
                "exactly, so the cavity length is controlled — slowly by a heater, quickly by a piezoelectric "
                "actuator — to lock the frequency to that extremum.",
                "Ổn định tần số bằng hiệu ứng Zeeman dọc",
                "Longitudinal Zeeman stabilisation")


def fig_6_49():
    o = [_defs()]
    y = 110
    # laser
    o.append(_rect(40, y - 14, 84, 28, "#f7fbff"))
    o.append(_txt(82, y + 4, "laser He–Ne", 7.5))
    o.append(_beam(124, y, 268, y))
    # beam splitter
    o.append(_bsplit(268, y))
    # arm 1 up to fixed mirror
    o.append(_beam(268, y, 268, 46))
    o.append(_mirror(268, 40, 90, 26))
    o.append(_txt(268, 30, "gương cố định", 7.5, color=GREY))
    o.append(_beam(268, 46, 268, y))
    # arm 2 right to moving mirror
    o.append(_beam(268, y, 470, y))
    o.append(_mirror(476, y, 90, 40))
    o.append(_txt(476, y + 32, "gương di động (x)", 7.5, color=GREY))
    o.append(_arrow(476, y + 46, 476, y + 66, sw=1.1, color=GOLD))
    o.append(_beam(470, y, 268, y))
    # recombined beam down
    o.append(_beam(268, y, 268, 186))
    o.append(_txt(268, 200, "thấu kính phân kỳ", 7.5, color=GREY))
    o.append('<path d="M256 186 L280 186 L268 202 Z" fill="#dce9f5" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_beam(268, 202, 268, 226))
    o.append(_line(258, 230, 278, 230, sw=2.4))
    o.append(_txt(268, 246, "lỗ nhỏ", 7, color=GREY))
    o.append(_beam(268, 234, 268, 258))
    o.append(_rect(240, 258, 56, 24, "#fff"))
    o.append(_txt(268, 274, "tách sóng", 7))
    o.append(_arrow(268, 282, 268, 296, sw=1))
    o.append(_txt(268, 310, "đếm vân", 7.5, color=INK, weight="600"))
    return _fig(svg(660, 322, "".join(o), "Giao thoa kế Michelson cơ bản"),
                "Hình 6-49 · Sơ đồ giao thoa kế Michelson cơ bản. Ánh sáng đơn sắc kết hợp của laser He–Ne đã ổn định "
                "bước sóng tới bộ tách chùm, chia thành hai chùm cường độ bằng nhau. Hai chùm phản xạ trên gương cố "
                "định và gương di động (cần đo dịch chuyển x) rồi hợp lại tại bộ tách; do tính kết hợp, các mặt sóng "
                "có quan hệ pha xác định phụ thuộc hiệu quang trình. Dịch chuyển gương làm cường độ sau thấu kính "
                "biến thiên hình sin thành hệ vân vành; lỗ nhỏ xác định đúng vị trí quan sát và bộ tách sóng thu tín "
                "hiệu biến thiên ấy.",
                "Figure 6.49 · Schematic of the basic Michelson interferometer. Coherent monochromatic light from a "
                "wavelength-stabilised He–Ne laser reaches the beam splitter and is divided into two beams of equal "
                "intensity. They reflect off the fixed and the moving mirror (whose displacement x is to be measured) "
                "and recombine at the splitter; because the light is coherent, the wavefronts have a well-defined "
                "phase relation set by the optical path difference. Moving the mirror varies the intensity behind the "
                "lens sinusoidally as an annular fringe pattern; the pinhole fixes the observation point and the "
                "photodetector picks up the variation.",
                "Giao thoa kế Michelson cơ bản",
                "Basic Michelson interferometer")


def fig_6_50():
    o = [_defs()]
    y = 104
    o.append(_rect(36, y - 14, 78, 28, "#f7fbff"))
    o.append(_txt(75, y + 4, "laser Zeeman", 7))
    o.append(_txt(75, y + 34, "hai mode f₁, f₂", 7, color=GREY))
    o.append(_beam(114, y, 168, y))
    o.append(_rect(168, y - 12, 16, 24, "#dce9f5"))
    o.append(_txt(176, y + 34, "λ/4", 7, color=GREY))
    o.append(_beam(184, y, 240, y))
    o.append(_bsplit(240, y))
    # arm 1: reference detector with polariser
    o.append(_beam(240, y, 240, 44))
    o.append(_rect(232, 30, 16, 14, "#e8d7b0"))
    o.append(_txt(252, 40, "P 45°", 7, anchor="start", color=GREY))
    o.append(_beam(240, 44, 240, 30))
    o.append(_arrow(240, 30, 240, 16, sw=1, color="#c0392b"))
    o.append(_rect(214, 4, 52, 14, "#fff"))
    o.append(_txt(240, 14, "D_ref", 7))
    # arm 2: polarising splitter
    o.append(_beam(240, y, 360, y))
    o.append(_bsplit(360, y))
    o.append(_txt(360, y + 36, "chia phân cực", 7, color=GREY))
    # measuring arm up
    o.append(_beam(360, y, 360, 46))
    o.append(_mirror(360, 40, 90, 26))
    o.append(_txt(360, 30, "gương đo (x)", 7, color=GREY))
    o.append(_beam(360, 46, 360, y))
    # reference arm right
    o.append(_beam(360, y, 480, y))
    o.append(_mirror(486, y, 90, 34))
    o.append(_txt(486, y + 34, "gương chuẩn", 7, color=GREY))
    o.append(_beam(480, y, 360, y))
    # recombine down through polariser to detector
    o.append(_beam(360, y, 360, 176))
    o.append(_rect(352, 176, 16, 14, "#e8d7b0"))
    o.append(_txt(372, 186, "P 45°", 7, anchor="start", color=GREY))
    o.append(_beam(360, 190, 360, 214))
    o.append(_rect(334, 214, 52, 16, "#fff"))
    o.append(_txt(360, 225, "D_sig", 7))
    o.append(_arrow(360, 230, 360, 246, sw=1))
    o.append(_txt(360, 262, "đếm f₂ − f₁ − f_D", 7.5, color=INK, weight="600"))
    return _fig(svg(660, 276, "".join(o), "Giao thoa kế dị tần hai tần số"),
                "Hình 6-50 · Giao thoa kế Michelson hai tần số bán trên thị trường, làm việc với nguồn laser He–Ne ổn "
                "định bằng hiệu ứng Zeeman. Laser phát hai mode dọc tần số f₁ và f₂, phân cực tròn ngược chiều nhau; "
                "qua bản phần tư bước sóng chúng thành hai sóng phân cực thẳng vuông góc. Nhánh đo mang thành phần f₁ "
                "và bị dịch Doppler f_D do gương chuyển động, nhánh chuẩn mang f₂. Sau khi hợp lại và qua bản phân cực "
                "45°, bộ tách sóng thu hiệu tần f₂ − f₁ − f_D; hiệu liên tục của hai bộ đếm cho ra dịch chuyển theo "
                "bội số của λ_A/2, và dấu của số đếm cho biết chiều chuyển động.",
                "Figure 6.50 · The commercial two-frequency Michelson interferometer, operating with a Zeeman-stabilised "
                "He–Ne source. The laser emits two longitudinal modes at f₁ and f₂, circularly polarised in opposite "
                "senses; a quarter-wave plate turns them into two orthogonally linearly polarised waves. The "
                "measuring arm carries f₁, Doppler-shifted by f_D as the reflector moves; the reference arm carries "
                "f₂. Recombined and passed through a 45° polariser, the detector sees the difference frequency "
                "f₂ − f₁ − f_D; the running difference of the two counters gives the displacement in multiples of "
                "λ_A/2, and the sign of the count gives the direction of motion.",
                "Giao thoa kế dị tần hai tần số",
                "Two-frequency heterodyne interferometer")


def fig_6_51():
    o = [_defs()]
    y = 100
    o.append(_rect(34, y - 14, 74, 28, "#f7fbff"))
    o.append(_txt(71, y + 4, "laser Zeeman", 7))
    o.append(_beam(108, y, 160, y))
    o.append(_rect(160, y - 12, 16, 24, "#dce9f5"))
    o.append(_txt(168, y + 34, "λ/4", 7, color=GREY))
    o.append(_beam(176, y, 232, y))
    # polarising splitter I: rejects f2
    o.append(_bsplit(232, y))
    o.append(_beam(232, y, 232, 42))
    o.append(_arrow(232, 42, 232, 22, sw=1, color="#c0392b"))
    o.append(_txt(232, 16, "f₂ loại ra", 7, color=GREY))
    o.append(_beam(232, y, 350, y))
    o.append(_txt(291, y - 10, "P 45°", 7, color=GREY))
    # splitter II
    o.append(_bsplit(350, y))
    o.append(_beam(350, y, 350, 44))
    o.append(_mirror(350, 38, 90, 26))
    o.append(_txt(350, 28, "gương đo (x)", 7, color=GREY))
    o.append(_beam(350, 44, 350, y))
    o.append(_beam(350, y, 466, y))
    o.append(_mirror(472, y, 90, 34))
    o.append(_txt(472, y + 32, "gương chuẩn", 7, color=GREY))
    o.append(_beam(466, y, 350, y))
    # recombine down
    o.append(_beam(350, y, 350, 150))
    o.append(_rect(342, 150, 16, 14, "#dce9f5"))
    o.append(_txt(362, 162, "λ/4 ở 45°", 7, anchor="start", color=GREY))
    o.append(_beam(350, 164, 350, 186))
    o.append(_bsplit(350, 186))
    # four detectors
    o.append(_beam(350, 186, 350, 210))
    o.append(_rect(328, 210, 44, 14, "#fff"))
    o.append(_txt(350, 220, "A", 7))
    o.append(_beam(350, 186, 470, 186))
    o.append(_rect(470, 178, 16, 14, "#e8d7b0"))
    o.append(_txt(468, 166, "P 45°", 7, anchor="end", color=GREY))
    o.append(_beam(486, 186, 520, 186))
    o.append(_bsplit(520, 186))
    o.append(_beam(520, 186, 520, 160))
    o.append(_rect(508, 146, 24, 14, "#fff"))
    o.append(_txt(520, 156, "C", 7))
    o.append(_beam(520, 186, 520, 212))
    o.append(_rect(508, 212, 24, 14, "#fff"))
    o.append(_txt(520, 222, "D", 7))
    o.append(_beam(350, 186, 290, 186))
    o.append(_rect(266, 178, 24, 14, "#fff"))
    o.append(_txt(278, 188, "B", 7))
    o.append(_txt(350, 250, "A, B, C, D → tín hiệu vuông pha", 7.5, color=INK, weight="600"))
    return _fig(svg(660, 264, "".join(o), "Giao thoa kế đồng tần đơn mode"),
                "Hình 6-51 · Giao thoa kế đồng tần đơn mode. Nguồn laser ổn định bằng hiệu ứng Zeeman phát hai mode "
                "dọc lệch tần, phân cực tròn; qua bản phần tư bước sóng chỉ một thành phần (f₁) được dùng, thành phần "
                "kia bị bộ chia phân cực loại ra khỏi đường quang. Hai nhánh giữ phân cực trực giao nên sau gương "
                "phản xạ chúng chưa giao thoa; qua bản phần tư bước sóng đặt ở 45° chúng thành hai sóng phân cực tròn "
                "ngược chiều, mô tả được bằng một phasor quay Φ(t) với tốc độ tuỳ tần số Doppler. Bốn bộ tách sóng "
                "A–D sau các bản phân cực cho ra bốn tín hiệu lệch pha nhau, nhờ đó khử được cả nhoè dấu và ảnh "
                "hưởng của biến thiên cường độ.",
                "Figure 6.51 · Single-mode homodyne interferometer. A Zeeman-stabilised source emits two "
                "frequency-displaced circularly polarised longitudinal modes; after a quarter-wave plate only one "
                "(f₁) is used, the other being rejected by a polarising splitter. The two arms keep orthogonal "
                "polarisations, so after the reflector they do not interfere; a quarter-wave plate at 45° turns them "
                "into two opposite circular waves described by a rotating phasor Φ(t) whose rate follows the Doppler "
                "frequency. Four detectors A–D behind polarisers give four phase-shifted signals, which removes both "
                "the sign ambiguity and the sensitivity to intensity drift.",
                "Giao thoa kế đồng tần đơn mode",
                "Single-mode homodyne interferometer")


def fig_6_52():
    o = [_defs()]
    y = 96
    # input pairs A/B and C/D
    for k, (lab, yy) in enumerate((("A", 56), ("B", 74), ("C", 128), ("D", 146))):
        o.append(_line(40, yy, 96, yy, sw=1))
        o.append(_txt(34, yy + 4, lab, 8, anchor="end", color=GREY))
    # comparator 1
    o.append('<path d="M110 44 L110 88 L148 66 Z" fill="#fff" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_line(96, 56, 110, 56, sw=1))
    o.append(_line(96, 74, 110, 74, sw=1))
    o.append(_txt(118, 52, "−", 9))
    o.append(_txt(118, 82, "+", 9))
    o.append(_arrow(148, 66, 186, 66, sw=1))
    o.append(_txt(190, 70, "E", 9, anchor="start", color=GOLD, weight="600"))
    # comparator 2
    o.append('<path d="M110 118 L110 162 L148 140 Z" fill="#fff" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_line(96, 128, 110, 128, sw=1))
    o.append(_line(96, 146, 110, 146, sw=1))
    o.append(_txt(118, 124, "−", 9))
    o.append(_txt(118, 156, "+", 9))
    o.append(_arrow(148, 140, 186, 140, sw=1))
    o.append(_txt(190, 144, "F", 9, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(190, 84, "vuông pha", 7, anchor="start", color=GREY))
    # XOR and counter
    o.append(_rect(240, 92, 56, 34, "#fff"))
    o.append(_txt(268, 113, "E ⊕ F", 8))
    o.append(_arrow(196, 66, 226, 66, sw=1))
    o.append(_line(226, 66, 226, 100, sw=1))
    o.append(_arrow(226, 100, 240, 100, sw=1))
    o.append(_arrow(196, 140, 226, 140, sw=1))
    o.append(_line(226, 140, 226, 118, sw=1))
    o.append(_arrow(226, 118, 240, 118, sw=1))
    o.append(_rect(330, 92, 76, 34, "#fff"))
    o.append(_txt(368, 113, "bộ đếm", 8))
    o.append(_arrow(296, 109, 330, 109, sw=1))
    o.append(_arrow(406, 109, 430, 109, sw=1))
    o.append(_txt(434, 113, "N", 9, anchor="start", color=INK, weight="600"))
    o.append(_line(368, 126, 368, 158, sw=1))
    o.append(_line(368, 158, 268, 158, sw=1))
    o.append(_arrow(268, 158, 268, 130, sw=1))
    o.append(_txt(318, 154, "lên/xuống", 7, color=GREY))
    o.append(_txt(300, 200, "E&F → chọn chiều; E⊕F → xung đếm (nội suy ×4)", 7.5, color=INK, weight="600"))
    return _fig(svg(660, 214, "".join(o), "Mạch xử lý tín hiệu giao thoa kế"),
                "Hình 6-52 · Mạch xử lý tín hiệu đơn giản cho ra hai tín hiệu vuông pha E và F. Các bộ tách sóng chỉ "
                "nhạy với cường độ, nên tín hiệu hình sin do gương chuyển động luôn chồng lên một nền một chiều tỉ lệ "
                "với cường độ trung bình. Hai bộ so sánh lấy hiệu các cặp tín hiệu A–B và C–D, nhờ đó khử được nền và "
                "cho ra tín hiệu qua không độc lập với nền. Hai tín hiệu vuông pha này cho phép nội suy vân theo hệ số "
                "4, đưa độ phân giải chia nhỏ nhất xuống còn ≈ 160 nm; nếu dùng E⊕F làm xung đếm và E&F làm tín hiệu "
                "chiều thì mạch đếm vẫn xác định đúng chiều chuyển động.",
                "Figure 6.52 · A simple signal conditioning circuit yielding the quadrature signals E and F. "
                "Photodetectors respond to intensity only, so the sinusoidal signal from the moving reflector always "
                "sits on a dc pedestal proportional to the mean intensity. The two comparators difference the pairs "
                "A–B and C–D, which removes the pedestal and gives zero-crossings independent of it. The two "
                "quadrature signals allow a fringe interpolation by a factor of 4, bringing the least-count "
                "resolution down to ≈160 nm; feeding E⊕F to the count input and E&F to the direction input keeps the "
                "counter tracking the right way.",
                "Mạch xử lý tín hiệu giao thoa kế",
                "Interferometer signal conditioning circuit")


# ---------------------------------------------------------------- 6.6
def _knurl(x, y, w, h, step=6):
    o = []
    i = 0
    while x + 4 + i * step < x + w - 3:
        o.append(_line(x + 4 + i * step, y + 3, x + 4 + i * step, y + h - 3, sw=0.5, color="#9a9a9a"))
        i += 1
    return "".join(o)


def _plug(x, y, w, h, lab="", fill="#e9eef4"):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="1.1"/>'
         % (_f(x), _f(y), _f(w), _f(h), _f(h / 2.0), fill, INK)]
    if lab:
        o.append(_txt(x + w / 2.0, y + h / 2.0 + 3, lab, 7.5))
    return "".join(o)


def _handle(x, y, w, h=18):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="3" fill="#dcdcdc" stroke="%s" stroke-width="1.1"/>'
            % (_f(x), _f(y), _f(w), _f(h), INK)) + _knurl(x, y, w, h)


def fig_6_53():
    o = [_defs()]
    # ---- (a) two separate single-end members
    o.append(_plug(58, 42, 76, 12, "GO"))
    o.append(_handle(138, 39, 48))
    o.append(_plug(58, 76, 76, 12, "NO-GO"))
    o.append(_handle(138, 73, 48))
    o.append(_txt(24, 70, "(a)", 8, anchor="start", weight="600"))
    o.append(_txt(150, 104, "hai chi tiết đo rời", 7, color=GREY))
    # ---- (b) double-end
    o.append(_plug(40, 126, 62, 12, "GO"))
    o.append(_handle(106, 123, 56))
    o.append(_plug(166, 126, 62, 12, "NO-GO"))
    o.append(_txt(24, 136, "(b)", 8, anchor="start", weight="600"))
    o.append(_txt(134, 154, "hai chi tiết trên một tay cầm", 7, color=GREY))
    # ---- (c) progressive
    o.append(_handle(40, 181, 48))
    o.append(_plug(92, 185, 46, 10))
    o.append(_plug(140, 181, 76, 18, "NO-GO"))
    o.append(_txt(24, 194, "(c)", 8, anchor="start", weight="600"))
    o.append(_txt(178, 212, "kiểu lũy tiến: phần GO đi trước, phần NO-GO theo sau", 7, color=GREY))
    # dimension call-out on (b)
    o.append(_line(40, 148, 228, 148, sw=0.6, color=GREY))
    o.append(_line(40, 143, 40, 153, sw=0.6, color=GREY))
    o.append(_line(228, 143, 228, 153, sw=0.6, color=GREY))
    o.append(_txt(134, 166, "", 7))
    return _fig(svg(660, 228, "".join(o), "Ba kiểu căn lỗ trục trơn theo chuẩn AGD"),
                "Hình 6-53 · Căn lỗ trục trơn tiêu chuẩn AGD dùng để kiểm tra đường kính lỗ: (a) hai chi tiết đo rời, "
                "mỗi chi tiết một đầu; (b) hai chi tiết đo lắp trên cùng một tay cầm, mỗi đầu một chi tiết; "
                "(c) căn kiểu lũy tiến — phần “qua” đi trước, phần “không qua” theo sau trên cùng một thân. "
                "Căn loại này không cho số đo; chúng chỉ trả lời lỗ đạt hay không đạt kích thước giới hạn.",
                "Figure 6.53 · AGD cylindrical plug gages for inspecting hole diameter: (a) two separate gage "
                "members; (b) two gage members mounted on one handle, one at each end; (c) progressive gage — the "
                "go portion leads and the no-go portion follows on the same body. These gages give no reading; they "
                "only answer whether the bore is within its limit size.",
                "Ba kiểu căn lỗ trục trơn tiêu chuẩn AGD",
                "Three types of AGD plug gages")


def fig_6_54():
    o = [_defs()]
    # bore walls in section
    for x in (150, 470):
        o.append(_rect(x, 72, 26, 168, "url(#h6)"))
        o.append(_rect(x, 72, 26, 168, "none"))
    # gage body
    o.append(_rect(298, 98, 54, 116, "#f7fbff"))
    o.append(_txt(325, 150, "thân", 7.5, color="#4a6b8a"))
    # contacts
    o.append(_rect(176, 196, 122, 9, "#c9c9c9"))
    o.append(_rect(352, 196, 118, 9, "#c9c9c9"))
    o.append(_txt(236, 190, "đầu đo di động", 7, color=GREY))
    o.append(_txt(412, 190, "đầu đo cố định", 7, color=GREY))
    # rocking lever from the moving contact into the body
    o.append(_line(240, 205, 300, 212, sw=1.3))
    o.append(_txt(252, 224, "đòn bẩy", 7, color=GREY))
    # internal transfer rod, drawn hidden
    o.append(_line(324, 214, 324, 100, sw=0.9, dash="4 3", color=GREY))
    # dial
    o.append('<circle cx="325" cy="66" r="30" fill="#fff" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_annulus(325, 66, 24, 28, 205, 240, "#f3c9c9"))
    o.append(_annulus(325, 66, 24, 28, 240, 262, "#f6e6a8"))
    o.append(_annulus(325, 66, 24, 28, 262, 300, "#cfe8cf"))
    o.append(_annulus(325, 66, 24, 28, 300, 335, "#f6e6a8"))
    o.append(_annulus(325, 66, 24, 28, 335, 10, "#f3c9c9"))
    o.append(_line(325, 66, 342, 46, sw=1.4))
    o.append('<circle cx="325" cy="66" r="2.4" fill="%s"/>' % INK)
    o.append(_txt(368, 50, "đồng hồ so", 7.5, anchor="start", color=GREY))
    o.append(_txt(368, 106, "vùng dung sai trên mặt số:", 7, anchor="start", color=GREY))
    o.append(_txt(368, 118, "xanh — đạt", 7, anchor="start", color=GREY))
    o.append(_txt(368, 130, "vàng — còn sửa được", 7, anchor="start", color=GREY))
    o.append(_txt(368, 142, "đỏ — phế phẩm", 7, anchor="start", color=GREY))
    # diameter dimension
    o.append(_line(176, 256, 470, 256, sw=0.7, color=GREY))
    o.append(_line(176, 250, 176, 262, sw=0.7, color=GREY))
    o.append(_line(470, 250, 470, 262, sw=0.7, color=GREY))
    o.append(_txt(323, 272, "đường kính lỗ D", 8, color=GREY))
    # zero setting note
    o.append(_txt(96, 54, "đặt zero bằng vòng chuẩn", 7.5, anchor="start", color=GREY))
    o.append(_txt(96, 66, "đúng đường kính danh nghĩa", 7.5, anchor="start", color=GREY))
    o.append(_line(206, 62, 292, 62, sw=0.7, color=GREY))
    return _fig(svg(660, 288, "".join(o), "Đồng hồ đo lỗ hai điểm tiếp xúc"),
                "Hình 6-54 · Đồng hồ đo lỗ kiểu hai điểm tiếp xúc — loại dụng cụ đo lỗ phổ biến nhất. Một đầu đo cố "
                "định tì vào thành lỗ, đầu kia di động và truyền chuyển vị qua một đòn bẩy tới đồng hồ so. Trước khi "
                "đo phải đặt đồng hồ về zero trên một vòng chuẩn đúng bằng đường kính danh nghĩa; khi ấy kim đồng hồ "
                "chỉ trực tiếp lượng lỗ to hơn hay nhỏ hơn danh nghĩa. Trên các đồng hồ điện tử hiện đại, vùng dung "
                "sai được tô màu: xanh là đạt, vàng là còn sửa được, đỏ là phế phẩm.",
                "Figure 6.54 · The two-point dial bore gage — the most widely used bore gage. One contact rests on "
                "the bore wall, the other moves and transfers its displacement through a rocking lever to a dial "
                "indicator. Before use the indicator is zeroed on a master ring of exactly the nominal diameter; the "
                "needle then reads directly how much the bore is over or under nominal. On modern electronic gages "
                "the tolerance zones are colour-coded: green within tolerance, yellow reworkable, red scrap.",
                "Đồng hồ đo lỗ hai điểm tiếp xúc",
                "Two-point dial bore gage")


def fig_6_55():
    o = [_defs()]
    for cx, span, lab in ((120, 66, "35–50 mm"), (330, 92, "50–100 mm"), (540, 116, "100–150 mm")):
        o.append('<circle cx="%s" cy="56" r="24" fill="#fff" stroke="%s" stroke-width="1.2"/>' % (_f(cx), INK))
        o.append(_line(cx, 56, cx + 14, 43, sw=1.3))
        o.append('<circle cx="%s" cy="56" r="2.2" fill="%s"/>' % (_f(cx), INK))
        o.append(_rect(cx - 6, 78, 12, 8, "#dcdcdc", sw=0.9))
        o.append(_rect(cx - 13, 86, 26, 50, "#f0f0f0"))
        for k in range(4):
            o.append(_line(cx - 9, 96 + k * 11, cx + 9, 96 + k * 11, sw=0.6, color="#9a9a9a"))
        o.append(_rect(cx - 2.5, 136, 5, span, "#c9c9c9", sw=0.9))
        o.append(_rect(cx - 12, 136 + span, 24, 5, "#b9b9b9", sw=0.9))
        o.append(_txt(cx, 274, lab, 8, color=GREY))
        o.append(_line(cx, 136 + span + 9, cx, 262, sw=0.6, color=GREY, dash="3 3"))
    o.append(_txt(104, 108, "thân", 7, anchor="end", color="#4a6b8a"))
    o.append(_txt(104, 152, "đầu đo", 7, anchor="end", color="#4a6b8a"))
    return _fig(svg(660, 288, "".join(o), "Bộ đồng hồ đo lỗ cho dải 35 mm đến 150 mm"),
                "Hình 6-55 · Một bộ đồng hồ đo lỗ phủ dải 35 mm đến 150 mm. Đồng hồ so đặt trên cùng, thân và đầu đo "
                "dài dần theo dải đo để vẫn giữ được độ cứng vững khi đo lỗ sâu; mỗi đồng hồ chỉ dùng cho một dải hẹp "
                "và phải hiệu chuẩn riêng bằng vòng chuẩn tương ứng.",
                "Figure 6.55 · A set of dial bore gages covering 35 mm to 150 mm. The dial sits on top; body and probe "
                "grow longer with the measuring range so that stiffness is preserved in deep holes. Each gage covers "
                "only a narrow range and must be calibrated with its own master ring.",
                "Bộ đồng hồ đo lỗ 35–150 mm",
                "Dial bore gage set, 35–150 mm")


def fig_6_56():
    o = [_defs()]
    cx, cy, R = 196, 172, 94
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#fbfdff" stroke="%s" stroke-width="1.5"/>'
             % (_f(cx), _f(cy), _f(R), INK))
    # instrument body
    o.append('<circle cx="%s" cy="%s" r="34" fill="#eef4fa" stroke="%s" stroke-width="1.1"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<path d="M%s %s L%s %s L%s %s Z" fill="%s" stroke="%s" stroke-width="1"/>'
             % (_f(cx - 15), _f(cy - 16), _f(cx + 15), _f(cy - 16), _f(cx), _f(cy + 14), "#e0a24a", INK))
    o.append(_txt(cx, cy + 30, "côn", 7, color="#8a5a10"))
    # three arms at 120 degrees
    for a in (-90, 30, 150):
        r = math.radians(a)
        o.append(_line(cx + 30 * math.cos(r), cy + 30 * math.sin(r),
                       cx + (R - 8) * math.cos(r), cy + (R - 8) * math.sin(r), sw=3.2, color="#8a6d3b"))
        o.append('<circle cx="%s" cy="%s" r="3.2" fill="%s"/>'
                 % (_f(cx + R * math.cos(r)), _f(cy + R * math.sin(r)), INK))
    # 120 degree annotation between the upper and the lower-right arm
    arc = []
    for k in range(41):
        th = math.radians(-90 + 120.0 * k / 40)
        arc.append("%s %s" % (_f(cx + 62 * math.cos(th)), _f(cy + 62 * math.sin(th))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 3"/>'
             % (" ".join(arc), GREY))
    o.append(_txt(cx + 66, cy - 30, "120°", 8, color=GOLD, weight="600"))
    # leader to the reading thimble
    o.append(_line(cx + 26, cy - 24, 404, 62, sw=0.9, color=GREY, dash="4 3"))
    o.append(_rect(404, 42, 54, 20, "#fff"))
    o.append(_rect(404, 62, 54, 34, "#f0f0f0"))
    for k in range(7):
        o.append(_line(410 + k * 7, 64, 410 + k * 7, 72, sw=0.7))
    o.append(_txt(431, 36, "thước đọc", 7.5, color=GREY))
    o.append(_txt(490, 60, "thân thước", 7.5, anchor="start", color=GREY))
    o.append(_txt(cx, cy + 138, "ba điểm tiếp xúc cách nhau 120° → tự định tâm", 8.5, color=INK))
    return _fig(svg(660, 322, "".join(o), "Panme đo trong ba điểm tiếp xúc"),
                "Hình 6-56 · Panme đo trong kiểu ba điểm tiếp xúc (Intrimic), nhìn dọc theo trục lỗ. Ba đầu đo bố trí "
                "cách nhau 120° tì lên thành lỗ nên dụng cụ tự định tâm và tự căn chỉnh theo trục lỗ — đặc biệt quan "
                "trọng với lỗ sâu. Một côn ở giữa được vít tiến ra để đẩy đồng thời cả ba đầu đo; lượng dịch của côn, "
                "đọc trên thân thước phía ngoài, chính là lượng thay đổi đường kính. Đầu đo bằng cacbit vonfram để "
                "chống mòn và có thể đo tới đáy lỗ kín.",
                "Figure 6.56 · Three-point internal micrometer (Intrimic), seen along the bore axis. The three contacts "
                "spaced 120° apart rest on the bore wall, so the instrument self-centres and self-aligns with the "
                "bore axis — essential in deep holes. A central cone is screwed forward to push all three contacts "
                "outward; the cone travel, read on the thimble outside, is the change in diameter. The tips are "
                "tungsten carbide to resist wear and reach the bottom of blind holes.",
                "Panme đo trong ba điểm tiếp xúc",
                "Three-point internal micrometer")


def fig_6_57():
    o = [_defs()]
    # ---- part in section: a horizontal bore, material above and below
    o.append(_rect(40, 50, 268, 28, "url(#h6)"))
    o.append(_rect(40, 50, 268, 28, "none"))
    o.append(_rect(40, 184, 268, 28, "url(#h6)"))
    o.append(_rect(40, 184, 268, 28, "none"))
    # air plug inside the bore
    o.append('<rect x="20" y="94" width="252" height="78" rx="8" fill="#e9eef4" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(146, 137, "đầu đo khí", 7.5))
    # air supply
    o.append(_arrow(4, 133, 18, 133, sw=1.6, color="#2f6f9f"))
    o.append(_txt(6, 123, "khí nén", 7.5, anchor="start", color="#2f6f9f"))
    # jets into the clearance
    for xx in (90, 190):
        o.append(_arrow(xx, 94, xx, 80, sw=1, color="#2f6f9f"))
        o.append(_arrow(xx, 172, xx, 184, sw=1, color="#2f6f9f"))
    o.append(_txt(90, 42, "vòi phun", 7, color="#2f6f9f"))
    # clearance call-out
    o.append(_txt(296, 96, "khe hở h", 7.5, anchor="start", color=GREY))
    o.append(_line(294, 92, 280, 88, sw=0.7, color=GREY))
    # bore diameter
    o.append(_line(40, 232, 308, 232, sw=0.6, color=GREY))
    o.append(_line(40, 226, 40, 238, sw=0.6, color=GREY))
    o.append(_line(308, 226, 308, 238, sw=0.6, color=GREY))
    o.append(_txt(174, 250, "đường kính lỗ", 7.5, color=GREY))
    o.append(_txt(174, 272, "lưu lượng hay áp suất ngược", 8, color=INK))
    o.append(_txt(174, 284, "phụ thuộc khe hở", 8, color=INK))
    # ---- back-pressure curve
    ox, oy, w, h = 372, 200, 226, 138
    o.append(_line(ox, oy, ox + w, oy, sw=1.1))
    o.append(_line(ox, oy, ox, oy - h, sw=1.1))
    o.append(_arrow(ox + w - 4, oy, ox + w, oy, sw=1.1))
    o.append(_arrow(ox, oy - h + 4, ox, oy - h, sw=1.1))
    o.append(_txt(ox + w, oy + 16, "h", 8, anchor="end"))
    o.append(_txt(ox - 8, oy - h + 6, "p", 8, anchor="end"))
    pts = []
    for i in range(61):
        u = i / 60.0
        hh = 0.04 + 3.0 * u
        pp = 1.0 / (1.0 + 2.2 * hh * hh)
        pts.append("%s %s" % (_f(ox + 6 + u * (w - 20)), _f(oy - 6 - pp * (h - 20))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2"/>' % (" ".join(pts), GOLD))
    o.append(_txt(ox + 86, oy - h + 34, "p ∝ 1/(1 + k h²)", 8, color=GOLD, weight="600"))
    o.append(_txt(ox + 100, oy + 34, "áp suất ngược giảm khi khe hở tăng", 7.5, color=GREY))
    return _fig(svg(660, 292, "".join(o), "Đầu đo khí và quan hệ áp suất ngược với khe hở"),
                "Hình 6-57 · Đầu đo lỗ bằng khí (trục khí), vẽ theo mặt cắt dọc lỗ. Khí nén được dẫn vào đầu đo rồi "
                "thoát ra qua hai vòi phun trên chu vi; khi đầu đo nằm trong lỗ, khe hở giữa mặt vòi phun và thành lỗ "
                "hạn chế dòng thoát. Lỗ to hơn một chút làm khe hở tăng, lưu lượng tăng và áp suất ngược trong mạch "
                "giảm — đó chính là đại lượng được đo. Đồ thị bên phải cho dạng quan hệ phi tuyến ấy; hệ thống được "
                "hiệu chuẩn và đặt điểm zero bằng các lỗ chuẩn.",
                "Figure 6.57 · The air plug gage (air spindle), drawn in longitudinal section. Compressed air is fed "
                "into the plug and escapes through two or more jets on its periphery; inside a bore, the clearance "
                "between the jet faces and the wall restricts the flow. A slightly larger bore increases that "
                "clearance, raises the flow and lowers the back pressure in the circuit — and that is the quantity "
                "measured. The curve on the right shows the non-linear relationship; the system is calibrated and "
                "zeroed on master holes.",
                "Đầu đo khí và quan hệ áp suất ngược",
                "Air plug gage and back-pressure curve")


def fig_6_58():
    o = [_defs()]
    # ---- (a) three-point head
    cx, cy, R = 138, 138, 74
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#fbfdff" stroke="%s" stroke-width="1.4"/>' % (_f(cx), _f(cy), _f(R), INK))
    for a in (-90, 30, 150):
        r = math.radians(a)
        o.append(_line(cx + (R - 22) * math.cos(r), cy + (R - 22) * math.sin(r),
                       cx + R * math.cos(r), cy + R * math.sin(r), sw=2.4, color="#8a6d3b"))
        o.append('<circle cx="%s" cy="%s" r="2.8" fill="%s"/>'
                 % (_f(cx + R * math.cos(r)), _f(cy + R * math.sin(r)), INK))
        o.append(_line(cx, cy, cx + (R - 22) * math.cos(r), cy + (R - 22) * math.sin(r), sw=0.7, color=GREY, dash="3 3"))
    o.append('<circle cx="%s" cy="%s" r="16" fill="#f0f0f0" stroke="%s" stroke-width="1"/>' % (_f(cx), _f(cy), INK))
    o.append(_txt(cx, cy + 3, "côn", 7))
    o.append(_txt(cx, 30, "(a) đầu đo ba điểm", 8, weight="600"))
    o.append(_txt(cx, 240, "ba tiếp điểm 120°", 7.5, color=GREY))
    o.append(_txt(cx, 252, "→ tự định tâm trong lỗ sâu", 7.5, color=GREY))
    # ---- (b) five form errors
    bx = 300
    o.append(_txt(bx + 172, 30, "(b) năm dạng sai lệch hình dạng", 8, weight="600"))
    forms = [
        ("độ côn", "taper"),
        ("miệng loe", "bell"),
        ("phình giữa", "barrel"),
        ("ô van", "oval"),
        ("múi (lobing)", "lobe"),
    ]
    for i, (lab, kind) in enumerate(forms):
        col, row = i % 2, i // 2
        x0 = bx + col * 176
        y0 = 52 + row * 66
        w, h = 64, 46
        cxx, cyy = x0 + 34, y0 + 26
        if kind == "taper":
            o.append('<path d="M%s %s L%s %s L%s %s L%s %s Z" fill="#eef4fa" stroke="%s" stroke-width="1.2"/>'
                     % (_f(cxx - 20), _f(cyy - h / 2), _f(cxx + 20), _f(cyy - h / 2),
                        _f(cxx + 27), _f(cyy + h / 2), _f(cxx - 27), _f(cyy + h / 2), INK))
        elif kind == "bell":
            o.append('<path d="M%s %s L%s %s Q%s %s %s %s L%s %s L%s %s L%s %s Q%s %s %s %s Z" '
                     'fill="#eef4fa" stroke="%s" stroke-width="1.2"/>'
                     % (_f(cxx - 26), _f(cyy - h / 2), _f(cxx + 26), _f(cyy - h / 2),
                        _f(cxx + 26), _f(cyy - h / 2 + 18), _f(cxx + 15), _f(cyy - h / 2 + 20),
                        _f(cxx + 15), _f(cyy + h / 2), _f(cxx - 15), _f(cyy + h / 2),
                        _f(cxx - 15), _f(cyy - h / 2 + 20),
                        _f(cxx - 26), _f(cyy - h / 2 + 18), _f(cxx - 26), _f(cyy - h / 2), INK))
        elif kind == "barrel":
            o.append('<path d="M%s %s Q%s %s %s %s L%s %s Q%s %s %s %s Z" fill="#eef4fa" stroke="%s" stroke-width="1.2"/>'
                     % (_f(cxx - 17), _f(cyy - h / 2), _f(cxx - 25), _f(cyy), _f(cxx - 17), _f(cyy + h / 2),
                        _f(cxx + 17), _f(cyy + h / 2), _f(cxx + 25), _f(cyy), _f(cxx + 17), _f(cyy - h / 2), INK))
        elif kind == "oval":
            o.append('<ellipse cx="%s" cy="%s" rx="25" ry="18" fill="#eef4fa" stroke="%s" stroke-width="1.2"/>'
                     % (_f(cxx), _f(cyy), INK))
        else:
            pts = []
            for k in range(73):
                th = 2 * math.pi * k / 72
                rr = 20 * (1 + 0.16 * math.cos(3 * th))
                pts.append("%s %s" % (_f(cxx + rr * math.cos(th)), _f(cyy + rr * math.sin(th))))
            o.append('<polygon points="%s" fill="#eef4fa" stroke="%s" stroke-width="1.2"/>' % (" ".join(pts), INK))
        o.append(_txt(x0 + 34, y0 + 60, lab, 7.5, color=INK))
    return _fig(svg(660, 268, "".join(o), "Đầu đo ba điểm và năm dạng sai lệch hình dạng lỗ"),
                "Hình 6-58 · (a) Đầu đo điện tử ba điểm tiếp xúc, ba điểm cách nhau 120°, nhờ đó tự định tâm và căn "
                "thẳng theo trục lỗ — điều kiện bắt buộc với lỗ sâu. (b) Năm dạng sai lệch hình dạng mà các đầu đo "
                "nhiều điểm phát hiện được: độ côn, miệng loe, phình giữa, ô van và múi. Muốn phân biệt chúng, người "
                "ta đo ở nhiều độ sâu và nhiều phương góc khác nhau rồi so với hình dạng lý tưởng.",
                "Figure 6.58 · (a) A three-point electronic bore head with contacts 120° apart, which self-centres "
                "and aligns with the bore axis — essential in deep holes. (b) Five form errors that multi-point "
                "heads can detect: taper, bell mouthing, barrelling, ovality and lobing. Distinguishing them "
                "requires measurements at several depths and angular orientations, compared against the ideal "
                "shape.",
                "Đầu đo ba điểm và năm dạng sai lệch hình dạng",
                "Three-point head and five bore form errors")


def fig_6_59():
    o = [_defs()]
    # turntable
    o.append('<ellipse cx="150" cy="196" rx="96" ry="24" fill="#e6e6e6" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_rect(120, 172, 60, 24, "#f7fbff"))
    o.append('<ellipse cx="150" cy="172" rx="30" ry="9" fill="#f7fbff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(150, 216, "bàn quay", 7.5, color=GREY))
    o.append('<path d="M132 246 A26 26 0 0 1 168 246" fill="none" stroke="%s" stroke-width="1"/>' % GREY)
    o.append(_arrow(166, 240, 170, 236, sw=1, color=GREY))
    # column and arm
    o.append(_rect(276, 70, 20, 176, "#e6e6e6"))
    o.append(_rect(276, 70, 20, 176, "none"))
    o.append(_rect(150, 96, 128, 12, "#d8d8d8"))
    o.append(_rect(144, 108, 12, 52, "#c9c9c9"))
    o.append(_txt(238, 90, "đầu đo", 7.5, color=GREY))
    o.append(_txt(286, 62, "trụ Z", 7.5, color=GREY))
    o.append(_txt(196, 180, "chi tiết", 7, anchor="start", color=GREY))
    o.append(_line(184, 178, 194, 178, sw=0.7, color=GREY))
    # polar roundness trace
    cx, cy, R = 470, 150, 92
    o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="0.8" stroke-dasharray="4 4"/>'
             % (_f(cx), _f(cy), _f(R), GREY))
    pts = []
    for k in range(181):
        th = 2 * math.pi * k / 180
        rr = R * (1 + 0.075 * math.cos(3 * th + 0.6))
        pts.append("%s %s" % (_f(cx + rr * math.cos(th)), _f(cy + rr * math.sin(th))))
    o.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), GOLD))
    o.append(_txt(cx, cy - R - 12, "vết độ tròn (phóng đại)", 7.5, color=GREY))
    o.append(_txt(cx, cy + R + 22, "đường tròn quy chiếu", 7.5, color=GREY))
    o.append(_line(cx, cy, cx + R * 1.0, cy, sw=0.7, color=GREY, dash="2 3"))
    return _fig(svg(660, 276, "".join(o), "Máy đo độ tròn: bàn quay, đầu đo và vết cực"),
                "Hình 6-59 · Máy đo hình dạng: chi tiết được gá trên bàn quay, đầu đo tì vào mặt chi tiết. Khi bàn "
                "quay, đầu đo ghi độ lệch so với đường tròn thật; máy dựng đường tròn quy chiếu bằng bình phương tối "
                "thiểu rồi phóng đại sai lệch lên hàng nghìn lần để vẽ thành vết cực như hình bên phải. Với đầu đo "
                "gắn trên giá đỡ cứng vững, máy còn đo được độ đồng tâm, độ đảo hướng kính và mặt đầu, độ vuông góc, "
                "độ phẳng, độ song song và độ đồng trục.",
                "Figure 6.59 · Form measuring machine: the workpiece is staged on a turntable and a gage head rests "
                "against its surface. As the table rotates the head records deviation from a true circle; the machine "
                "fits a least-squares reference circle and magnifies the deviation thousands of times into the polar "
                "trace at the right. With the head on a rigid stand it also measures concentricity, radial and face "
                "runout, perpendicularity, flatness, parallelism and coaxiality.",
                "Máy đo độ tròn và vết cực",
                "Roundness machine and polar trace")


def fig_6_60():
    o = [_defs()]
    # gantry frame
    o.append(_rect(70, 54, 16, 176, "#e0e0e0"))
    o.append(_rect(392, 54, 16, 176, "#e0e0e0"))
    o.append(_rect(70, 54, 338, 14, "#e0e0e0"))
    o.append(_rect(70, 54, 16, 176, "none"))
    o.append(_rect(392, 54, 16, 176, "none"))
    o.append(_rect(70, 54, 338, 14, "none"))
    # Z carriage
    o.append(_rect(214, 68, 48, 30, "#f0c9a8"))
    o.append(_line(238, 98, 238, 160, sw=1.6))
    o.append('<path d="M238 166 l-5 -9 l10 0 Z" fill="%s"/>' % INK)
    o.append(_txt(268, 146, "đầu đo", 7.5, anchor="start", color=GREY))
    # rotary table
    o.append('<ellipse cx="238" cy="196" rx="86" ry="22" fill="#e6e6e6" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_rect(196, 176, 84, 20, "#f7fbff"))
    o.append('<ellipse cx="238" cy="176" rx="42" ry="11" fill="#f7fbff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(238, 230, "bàn quay định tâm tự động", 7.5, color=GREY))
    # axes
    o.append(_arrow(300, 44, 366, 44, sw=1, color=GOLD))
    o.append(_txt(370, 47, "X", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_arrow(420, 130, 420, 74, sw=1, color=GOLD))
    o.append(_txt(424, 100, "Z", 8, anchor="start", color=GOLD, weight="600"))
    o.append('<path d="M120 210 A40 40 0 0 1 150 178" fill="none" stroke="%s" stroke-width="1"/>' % GREY)
    o.append(_arrow(146, 180, 152, 176, sw=1, color=GREY))
    o.append(_txt(120, 226, "θ", 8, color=GREY, weight="600"))
    # control cabinet
    o.append(_rect(468, 108, 150, 100, "#f7fbff"))
    o.append(_rect(478, 118, 130, 48, "#eef4fa"))
    o.append(_txt(543, 148, "giao diện đồ hoạ", 7.5, color="#4a6b8a"))
    o.append(_txt(543, 178, "thu thập &amp; xử lý số liệu", 7))
    o.append(_txt(543, 192, "thời gian thực", 7))
    o.append(_line(416, 158, 466, 158, sw=1, dash="4 3"))
    o.append(_txt(440, 150, "dữ liệu", 7, color=GREY))
    return _fig(svg(660, 246, "".join(o), "Máy đo hình dạng tự động hoàn toàn"),
                "Hình 6-60 · Máy đo hình dạng tự động hoàn toàn (dòng RA-600). Máy có cổng khung động theo trục X và "
                "trụ thẳng đứng theo trục Z; bàn quay tự định tâm và tự cân bằng khi phát hiện độ lệch trong lần đo "
                "sơ bộ, nhờ đó không cần căn chỉnh thủ công. Ngoài độ tròn, máy còn đo được độ dày, độ vuông góc, độ "
                "trụ, độ trụ xoắn, độ thẳng, độ đảo toàn phần và độ song song thẳng đứng. Dữ liệu được đưa sang phần "
                "mềm thu thập để phân tích và phản hồi ngay cho sản xuất.",
                "Figure 6.60 · A fully automatic form measuring machine (RA-600 series). A moving gantry carries the "
                "head along X and a vertical column along Z; the rotary table centres and levels itself when the "
                "preliminary measurement detects a deviation, so no manual alignment is needed. Besides roundness the "
                "machine measures thickness, squareness, cylindricity, spiral cylindricity, straightness, total "
                "runout and vertical parallelism. Data go to acquisition software for immediate analysis and "
                "feedback to production.",
                "Máy đo hình dạng tự động hoàn toàn",
                "Fully automatic form measuring machine")


# ---------------------------------------------------------------- 6.7
def _wavearc(cx, cy, r, color="#c0392b", sw=1.4):
    return ('<path d="M%s %s A%s %s 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy - r * 0.62), _f(r), _f(r), _f(cx), _f(cy + r * 0.62), color, sw))


def fig_6_61():
    o = [_defs()]
    # transducer, transmitter above and receiver below
    o.append(_rect(46, 62, 46, 34, "#f7fbff"))
    o.append(_txt(69, 83, "Tr", 8, weight="600"))
    o.append(_rect(46, 116, 46, 34, "#f7fbff"))
    o.append(_txt(69, 137, "Re", 8, weight="600"))
    # outgoing train
    for k, r in enumerate((16, 26, 36)):
        o.append(_wavearc(100 + k * 16, 79, r))
    o.append(_arrow(170, 79, 470, 79, sw=1.2, color="#c0392b"))
    o.append(_txt(310, 70, "xung phát", 7.5, color="#c0392b"))
    # object
    o.append(_rect(492, 48, 26, 118, "url(#h6)"))
    o.append(_rect(492, 48, 26, 118, "none"))
    o.append(_txt(505, 40, "vật phản xạ", 7.5, color=GREY))
    # echo
    for k, r in enumerate((16, 26, 36)):
        o.append(_wavearc(470 - k * 16, 137, r))
    o.append(_arrow(432, 137, 190, 137, sw=1.2, color="#2f6f9f"))
    o.append(_txt(310, 152, "xung dội", 7.5, color="#2f6f9f"))
    # distance
    o.append(_line(69, 196, 505, 196, sw=0.7, color=GREY))
    o.append(_line(69, 190, 69, 202, sw=0.7, color=GREY))
    o.append(_line(505, 190, 505, 202, sw=0.7, color=GREY))
    o.append(_txt(287, 212, "khoảng cách d", 8, color=GREY))
    o.append(_txt(287, 238, "d = c · t / 2", 11, color=INK, weight="600"))
    # time axis sketch
    o.append(_line(540, 96, 640, 96, sw=1))
    o.append(_line(540, 96, 540, 180, sw=1))
    o.append(_arrow(636, 96, 640, 96, sw=1))
    o.append(_arrow(540, 100, 540, 96, sw=1))
    o.append(_txt(632, 90, "t", 8, anchor="end"))
    o.append('<polyline points="546 96 552 60 558 96 596 96 602 72 608 96" fill="none" stroke="%s" '
             'stroke-width="1.4"/>' % GOLD)
    o.append(_line(552, 96, 552, 172, sw=0.6, color=GREY, dash="3 3"))
    o.append(_line(602, 96, 602, 172, sw=0.6, color=GREY, dash="3 3"))
    o.append(_arrow(552, 166, 602, 166, sw=0.9))
    o.append(_arrow(602, 166, 552, 166, sw=0.9))
    o.append(_txt(577, 186, "t", 8, color=GOLD, weight="600"))
    return _fig(svg(660, 250, "".join(o), "Nguyên lý đo khoảng cách bằng xung–dội"),
                "Hình 6-61 · Nguyên lý hệ siêu âm xung–dội dùng để đo khoảng cách (Tr = phát, Re = thu). Bộ dao động "
                "tạo tín hiệu điện điển hình 40 kHz; tín hiệu này được biến thành dao động cơ cùng tần số ở đầu phát, "
                "tạo ra sóng âm lan truyền tới vật và bị phản xạ. Xung dội trở về gây một tín hiệu điện ở đầu thu. "
                "Khi biết tốc độ âm c, khoảng thời gian t giữa lúc phát và lúc nhận xung dội là thước đo khoảng cách "
                "d tới vật gây phản xạ. Trên thực tế đầu phát và đầu thu thường là cùng một đầu đo; ở đây chúng được "
                "vẽ tách ra cho rõ.",
                "Figure 6.61 · Principle of a pulse-echo ultrasound system for distance measurement (Tr = transmitter, "
                "Re = receiver). The oscillator generates an electric signal, typically at 40 kHz, which the "
                "transmitter turns into mechanical vibration at the same frequency; the resulting sound wave travels "
                "to the object and is reflected. The returning echo produces an electric signal in the receiver. "
                "With the speed of sound c known, the elapsed time t between emission and detection of the echo is "
                "a measure of the distance d to the object causing it. In practice transmitter and receiver are the "
                "same device; they are drawn apart here for clarity.",
                "Nguyên lý đo khoảng cách bằng xung–dội",
                "Pulse-echo ranging principle")


def fig_6_62():
    o = [_defs()]
    o.append(_rect(40, 44, 260, 130, "#f4f8fc"))
    o.append(_rect(40, 44, 260, 130, "none"))
    o.append(_rect(300, 44, 280, 130, "#fbf4e8"))
    o.append(_rect(300, 44, 280, 130, "none"))
    o.append(_line(300, 44, 300, 174, sw=2.2))
    o.append(_txt(170, 62, "môi trường 1", 8, color=GREY))
    o.append(_txt(170, 76, "R₁ = ρ₁c₁", 8.5, color=INK))
    o.append(_txt(440, 62, "môi trường 2", 8, color=GREY))
    o.append(_txt(440, 76, "R₂ = ρ₂c₂", 8.5, color=INK))
    o.append(_arrow(90, 118, 288, 118, sw=2, color="#c0392b"))
    o.append(_txt(190, 110, "tới", 8, color="#c0392b"))
    o.append(_arrow(288, 152, 96, 152, sw=2, color="#2f6f9f"))
    o.append(_txt(190, 168, "phản xạ", 8, color="#2f6f9f"))
    o.append(_arrow(312, 118, 540, 118, sw=2, color="#2e7d32"))
    o.append(_txt(430, 110, "truyền qua", 8, color="#2e7d32"))
    # coefficient box
    o.append(_rect(40, 188, 540, 62, "#fff"))
    o.append(_txt(60, 212, "Hệ số phản xạ", 8.5, anchor="start", color=INK))
    o.append(_txt(60, 236, "Hệ số truyền qua", 8.5, anchor="start", color=INK))
    o.append(_txt(250, 212, "(R₂ − R₁)² / (R₁ + R₂)²", 9, anchor="start", color=INK))
    o.append(_txt(250, 236, "4 R₁R₂ / (R₁ + R₂)²", 9, anchor="start", color=INK))
    return _fig(svg(660, 262, "".join(o), "Phản xạ và truyền qua của sóng âm tại mặt phân cách"),
                "Hình 6-62 · Phản xạ và truyền qua của sóng âm tại mặt phân cách giữa hai môi trường có trở kháng đặc "
                "trưng khác nhau. Trở kháng đặc trưng R = ρc là tích của khối lượng riêng và tốc độ âm trong môi "
                "trường, và không phụ thuộc tần số. Khi hai trở kháng xấp xỉ nhau thì gần như toàn bộ cường độ truyền "
                "qua; khi chúng chênh nhau nhiều — như trường hợp màng gốm áp điện và không khí — phần lớn cường độ "
                "âm bị phản xạ ngay tại mặt phân cách, và đó là tổn thất lớn nhất của mọi hệ siêu âm làm việc trong "
                "không khí.",
                "Figure 6.62 · Reflection and transmission of a sound wave at the interface between two media of "
                "different characteristic impedance. The characteristic impedance R = ρc is the product of density "
                "and sound speed, and is independent of frequency. When the two impedances are comparable almost all "
                "the intensity is transmitted; when they differ strongly — as between a piezoelectric ceramic and "
                "air — most of the acoustic intensity is reflected at the interface, and that is the largest loss "
                "in any air-coupled ultrasound system.",
                "Phản xạ và truyền qua tại mặt phân cách",
                "Reflection and transmission at an interface")


def fig_6_63():
    o = [_defs()]
    o.append(_rect(50, 62, 16, 96, "#c9c9c9"))
    o.append(_txt(58, 52, "D", 8, weight="600"))
    o.append(_rect(66, 74, 214, 72, "#eef4fa"))
    o.append(_rect(66, 74, 214, 72, "none"))
    o.append('<path d="M280 74 L600 34 L600 186 L280 146 Z" fill="#f7fbff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_line(280, 74, 280, 146, sw=1, color=GREY, dash="4 3"))
    o.append(_txt(160, 116, "trường gần", 8, color="#4a6b8a"))
    o.append(_txt(450, 130, "trường xa", 8, color="#4a6b8a"))
    o.append(_line(66, 200, 280, 200, sw=0.7, color=GREY))
    o.append(_line(66, 194, 66, 206, sw=0.7, color=GREY))
    o.append(_line(280, 194, 280, 206, sw=0.7, color=GREY))
    o.append(_txt(173, 216, "L ≈ D²/4λ", 9, color=INK))
    # beta between the axis and the upper cone edge
    o.append(_line(280, 110, 600, 110, sw=0.7, color=GREY, dash="3 3"))
    o.append('<path d="M380 110 A100 100 0 0 0 370 66" fill="none" stroke="%s" stroke-width="1"/>' % GOLD)
    o.append(_txt(392, 94, "β", 9, color=GOLD, weight="600"))
    o.append(_txt(420, 214, "sin β = 1,22 λ/D", 9, color=INK))
    return _fig(svg(660, 232, "".join(o), "Chùm siêu âm ở trường gần và trường xa"),
                "Hình 6-63 · Chùm siêu âm ở trường gần và trường xa của đầu đo. Trong không khí tự do, chùm lan "
                "truyền như một chùm song song trên một đoạn dài L ≈ D²/4λ, với D là đường kính màng phát và λ là "
                "bước sóng; xa hơn khoảng ấy chùm loe ra với nửa góc loe β thoả sin β = 1,22λ/D. Trong trường gần, "
                "cường độ phân bố phức tạp do giao thoa giữa các phần khác nhau của màng; trong trường xa cường độ "
                "gần như đồng đều. Muốn chùm hẹp thì phải tăng D so với λ, nhưng không thể tăng tần số tuỳ ý vì siêu "
                "âm tần số cao bị hấp thụ nhanh hơn.",
                "Figure 6.63 · The ultrasound beam in the near field and the far field of the transducer. In free air "
                "the beam travels parallel for a length L ≈ D²/4λ, where D is the membrane diameter and λ the "
                "wavelength; beyond that it diverges with a half angle β given by sin β = 1.22λ/D. In the near field "
                "the intensity is complicated by interference between different parts of the membrane; in the far "
                "field it is nearly uniform. A narrow beam calls for a large D relative to λ, but the frequency "
                "cannot simply be raised, because high-frequency ultrasound is absorbed faster.",
                "Chùm siêu âm ở trường gần và trường xa",
                "Near field and far field of the beam")


def fig_6_64():
    o = [_defs()]
    # ---- piezoelectric (left)
    o.append(_txt(150, 32, "(a) áp điện", 8, weight="600"))
    o.append(_rect(96, 52, 96, 24, "#e6e6e6"))
    o.append(_rect(96, 76, 96, 16, "#e0a24a"))
    o.append(_rect(96, 92, 96, 12, "#dce9f5"))
    o.append(_rect(96, 104, 96, 7, "#f0f0f0"))
    o.append(_txt(202, 60, "vật liệu hấp thụ", 7, anchor="start", color=GREY))
    o.append(_txt(202, 84, "gốm áp điện", 7, anchor="start", color="#8a5a10"))
    o.append(_txt(202, 100, "lớp phối âm", 7, anchor="start", color="#4a6b8a"))
    o.append(_txt(202, 116, "màng", 7, anchor="start", color=GREY))
    o.append(_line(192, 57, 200, 57, sw=0.6, color=GREY))
    o.append(_line(192, 81, 200, 81, sw=0.6, color=GREY))
    o.append(_line(192, 97, 200, 97, sw=0.6, color=GREY))
    o.append(_line(192, 110, 200, 110, sw=0.6, color=GREY))
    # drive
    o.append(_line(96, 84, 62, 84, sw=1))
    o.append(_line(192, 84, 226, 84, sw=1))
    o.append(_line(62, 84, 62, 150, sw=1))
    o.append(_line(226, 84, 226, 150, sw=1))
    o.append('<circle cx="62" cy="158" r="13" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(62, 162, "~", 9))
    o.append('<circle cx="226" cy="158" r="13" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(226, 162, "~", 9))
    o.append(_txt(144, 186, "U(t) đặt lên gốm", 7.5, color=GOLD))
    # ---- electrostatic (right)
    o.append(_txt(470, 32, "(b) tĩnh điện", 8, weight="600"))
    o.append(_rect(400, 56, 132, 10, "#f0f0f0"))
    o.append(_rect(400, 72, 132, 24, "#c9c9c9"))
    for k in range(8):
        o.append(_rect(406 + k * 16, 78, 9, 12, "#9a9a9a", sw=0.6))
    o.append(_rect(400, 118, 132, 9, "#e6e6e6"))
    o.append(_txt(540, 62, "màng", 7, anchor="start", color=GREY))
    o.append(_txt(540, 88, "bản cực có rãnh", 7, anchor="start", color=GREY))
    o.append(_txt(540, 124, "đế", 7, anchor="start", color=GREY))
    o.append(_line(400, 61, 372, 61, sw=1))
    o.append(_line(532, 61, 560, 61, sw=1))
    o.append(_line(372, 61, 372, 158, sw=1))
    o.append(_line(560, 61, 560, 158, sw=1))
    o.append('<circle cx="372" cy="170" r="13" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(372, 174, "~", 9))
    o.append('<circle cx="560" cy="170" r="13" fill="#fff" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(560, 174, "~", 9))
    o.append(_txt(466, 198, "phân cực một chiều + tín hiệu xoay chiều", 7.5, color=GREY))
    return _fig(svg(660, 214, "".join(o), "Đầu đo siêu âm áp điện và tĩnh điện"),
                "Hình 6-64 · Hai kiểu đầu đo siêu âm làm việc trong không khí. (a) Đầu đo áp điện: một đĩa gốm áp "
                "điện kẹp giữa lớp hấp thụ phía sau và lớp phối âm phía trước. Đặt điện áp xoay chiều lên gốm, nó "
                "thay đổi kích thước theo tần số điện áp, và ngược lại khi bị xung âm ép dao động nó sinh ra điện "
                "áp — nhờ vậy một đầu đo vừa phát vừa thu được. Đầu đo hiệu quả nhất khi làm việc gần tần số cộng "
                "hưởng cơ của gốm. (b) Đầu đo tĩnh điện: một tụ bản phẳng, một bản cố định có rãnh, bản kia là màng "
                "mỏng tự do dao động; lực tĩnh điện giữa hai bản làm màng rung. Cả hai kiểu đều có thể dùng làm đầu "
                "phát và đầu thu.",
                "Figure 6.64 · Two kinds of air-coupled ultrasonic transducer. (a) Piezoelectric: a ceramic disc "
                "clamped between a backing absorber and a matching layer. An alternating voltage across the ceramic "
                "changes its dimensions at the drive frequency, and conversely a sound pulse forcing it to vibrate "
                "generates a voltage — so one transducer both transmits and receives. It works best near the "
                "mechanical resonance of the ceramic. (b) Electrostatic: a plate capacitor with one grooved fixed "
                "plate and one free conducting membrane; electrostatic force makes the membrane vibrate. Either kind "
                "can serve as transmitter and as receiver.",
                "Đầu đo siêu âm áp điện và tĩnh điện",
                "Piezoelectric and electrostatic transducers")


def fig_6_65():
    o = [_defs()]
    def box(x, y, w, h, t1, t2=""):
        o.append(_rect(x, y, w, h, "#fff"))
        o.append(_txt(x + w / 2.0, y + (h / 2.0 + 3 if not t2 else h / 2.0 - 1), t1, 7.5))
        if t2:
            o.append(_txt(x + w / 2.0, y + h / 2.0 + 10, t2, 7, color=GREY))
    box(40, 58, 84, 32, "nguồn phát", "x(t)")
    box(156, 58, 88, 32, "kênh truyền", "h(t, t₀)")
    box(276, 58, 80, 32, "thu", "y(t)")
    box(276, 146, 80, 32, "ADC", "lấy mẫu")
    box(392, 146, 80, 32, "FFT", "S_xy / S_xx")
    box(508, 146, 100, 32, "nghịch đảo", "h(t − t₀)")
    box(508, 214, 100, 30, "làm khớp + lọc số", "bình phương tối thiểu")
    o.append(_arrow(124, 74, 152, 74, sw=1))
    o.append(_arrow(244, 74, 272, 74, sw=1))
    o.append(_arrow(316, 90, 316, 144, sw=1))
    o.append(_arrow(356, 162, 388, 162, sw=1))
    o.append(_arrow(472, 162, 504, 162, sw=1))
    o.append(_arrow(558, 178, 558, 212, sw=1))
    o.append(_arrow(608, 229, 632, 229, sw=1))
    o.append(_txt(636, 233, "t − t₀", 8.5, anchor="start", color=GOLD, weight="600"))
    # x(t) also feeds the cross-spectrum denominator
    o.append(_line(82, 90, 82, 190, sw=1, dash="4 3"))
    o.append(_line(82, 190, 432, 190, sw=1, dash="4 3"))
    o.append(_arrow(432, 190, 432, 180, sw=1))
    o.append(_txt(200, 186, "S_xx(f)", 7.5, color=GREY))
    o.append(_txt(330, 254, "ước lượng thời gian bay chính xác hơn nhờ làm khớp đường cong", 8, color=GREY))
    return _fig(svg(660, 268, "".join(o), "Sơ đồ hệ đo thời gian bay dựa trên tương quan"),
                "Hình 6-65 · Sơ đồ hệ đo thời gian bay dựa trên tương quan. Tín hiệu phát x(t) và tín hiệu thu y(t) "
                "được đưa vào tính hàm tương quan chéo; khi x(t) là một chuỗi ngẫu nhiên (nhiễu Gauss trắng), hàm "
                "tương quan chéo chính là ước lượng đáp ứng xung h(t, t₀) của hệ, và đáp ứng xung là chỉ báo nhạy "
                "cho mọi độ trễ thời gian có thể. Trong miền tần số, phép chia S_xy(f)/S_xx(f) thực hiện đúng việc "
                "ấy. Độ chính xác của ước lượng khoảng cách — và do đó của khoảng thời gian t − t₀ — được cải thiện "
                "bằng cách làm khớp đường cong theo bình phương tối thiểu và lọc số trên máy tính.",
                "Figure 6.65 · Diagram of a correlation-based time-of-flight system. The transmitted signal x(t) and "
                "the received signal y(t) are cross-correlated; when x(t) is a random sequence (white Gaussian "
                "noise) the cross-correlation estimates the impulse response h(t, t₀) of the system, and that "
                "response is a sensitive indicator of every possible time delay. In the frequency domain the "
                "division S_xy(f)/S_xx(f) does exactly that. The accuracy of the range estimate — and therefore of "
                "the interval t − t₀ — is improved by least-squares curve fitting and digital filtering of that "
                "estimate on a computer.",
                "Sơ đồ hệ đo thời gian bay dựa trên tương quan",
                "Correlation-based time-of-flight system")


# ---------------------------------------------------------------- 6.8
def _cells(x0, y, cw, ch, pattern, fill="#2a2a2a"):
    """Draw a track as a row of cells; pattern is a string of '0'/'1'."""
    o = []
    for i, ch_ in enumerate(pattern):
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="0.6"/>'
                 % (_f(x0 + i * cw), _f(y), _f(cw), _f(ch), "#fff" if ch_ == "0" else fill, GREY))
    return "".join(o)


def fig_6_66():
    o = [_defs()]
    rows = [
        (46, "Bản chất thông tin", 34,
         [["Tuyệt đối"], ["Gia số (incremental)"]]),
        (128, "Loại tín hiệu", 46,
         [["Nhị phân", "trực tiếp"], ["Gray"], ["Vee-scan"],
          ["Giả ngẫu", "nhiên"], ["Vuông pha", "số"], ["Vuông pha", "tương tự"]]),
        (224, "Công nghệ tạo tín hiệu", 34,
         [["Che hình học"], ["Vân Moiré"], ["Nhiễu xạ"]]),
    ]
    for y, lab, bh, items in rows:
        o.append(_rect(28, y - bh / 2.0, 150, bh, "#f6e6c8"))
        o.append(_txt(103, y + 3, lab, 8, weight="600"))
        n = len(items)
        gap = 10
        w = (448 - gap * (n - 1)) / float(n)
        for i, lines in enumerate(items):
            x = 196 + i * (w + gap)
            o.append(_rect(x, y - bh / 2.0, w, bh, "#fff"))
            k = len(lines)
            for j, ln in enumerate(lines):
                ty = y + 3 + (j - (k - 1) / 2.0) * 11
                o.append(_txt(x + w / 2.0, ty, ln, 7.5))
        o.append(_arrow(178, y, 194, y, sw=0.9))
    o.append(_txt(330, 278, "ba trục phân loại độc lập nhau", 8, color=GREY))
    return _fig(svg(660, 296, "".join(o), "Phân loại bộ mã hoá quang"),
                "Hình 6-66 · Phân loại bộ mã hoá quang theo ba trục độc lập: (1) bản chất thông tin cuối cùng được cung "
                "cấp — tuyệt đối hay gia số; (2) loại tín hiệu được tạo ra — nhị phân trực tiếp, Gray, vee-scan, giải "
                "mã quang, giả ngẫu nhiên, hoặc vuông pha số và tương tự; và (3) công nghệ dùng để tạo tín hiệu — che "
                "hình học, vân Moiré hay nhiễu xạ. Mọi bộ mã hoá tuyệt đối đều dùng che hình học để tạo mã.",
                "Figure 6.66 · Classification of optical encoders along three independent axes: (1) the nature of the "
                "final information supplied — absolute or incremental; (2) the type of signal generated — direct "
                "binary, Gray, vee-scan, optical resolving, pseudorandom, or digital and analog quadrature; and "
                "(3) the technology used to generate the signal — geometric masking, Moiré fringes or diffraction. "
                "All absolute encoders use geometric masking to generate their code.",
                "Phân loại bộ mã hoá quang",
                "Classification of optical encoders")


def fig_6_67():
    o = [_defs()]
    cw, x0 = 14.0, 78
    y0, th, gap = 46, 15, 4
    # four tracks, MSB (one cycle) at the bottom
    tracks = []
    for t in range(4):
        n_cells = 2 ** (t + 1)              # 2, 4, 8, 16 cells across the 16 positions
        pat = "".join("1" if ((i * n_cells) // 16) % 2 else "0" for i in range(16))
        tracks.append(pat)
    for t, pat in enumerate(tracks):
        y = y0 + (3 - t) * (th + gap)
        o.append(_cells(x0, y, cw, th, pat))
        o.append(_txt(x0 - 12, y + 11, "2%s" % ("³²¹⁰"[t]), 8, anchor="end", color=GREY))
    # read head at position 7
    hx = x0 + 7 * cw
    o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="2"/>'
             % (_f(hx), _f(y0 - 4), _f(cw), _f(4 * (th + gap) - gap + 8), GOLD))
    o.append(_arrow(hx + cw / 2, y0 - 12, hx + cw / 2, y0 - 5, sw=1, color=GOLD))
    o.append(_txt(hx + cw / 2, y0 - 18, "đầu đọc", 7.5, color=GOLD))

    # position scale
    for i in range(17):
        o.append(_line(x0 + i * cw, 132, x0 + i * cw, 136, sw=0.6, color=GREY))
    for i in range(0, 17, 2):
        o.append(_txt(x0 + i * cw, 146, str(i), 6.5, color=GREY))
    # (b) analog output of the LSB track
    oy, hgt = 212, 44
    o.append(_line(x0, oy, x0 + 16 * cw, oy, sw=1))
    o.append(_line(x0, oy, x0, oy - hgt - 6, sw=1))
    o.append(_txt(x0 - 6, oy - hgt - 2, "I", 8, anchor="end"))
    pts = []
    for i in range(320):
        u = i / 320.0 * 16.0
        f = u - int(u)
        v = min(1.0, max(0.0, (f - 0.12) / 0.76))
        pts.append("%s %s" % (_f(x0 + u * cw), _f(oy - v * hgt)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), "#c0392b"))
    o.append(_txt(x0 + 16 * cw, oy - hgt - 8, "(b) quang thông trên rãnh LSB", 7.5, anchor="end", color=GREY))
    # (c) squared
    oy2 = 292
    o.append(_line(x0, oy2, x0 + 16 * cw, oy2, sw=1))
    o.append(_line(x0, oy2, x0, oy2 - 34, sw=1))
    pts = []
    for i in range(16):
        x = x0 + i * cw
        f_on = 0.12
        f_off = 0.88
        pts.append("%s %s" % (_f(x), _f(oy2)))
        pts.append("%s %s" % (_f(x + f_on * cw), _f(oy2)))
        pts.append("%s %s" % (_f(x + f_on * cw), _f(oy2 - 26)))
        pts.append("%s %s" % (_f(x + f_off * cw), _f(oy2 - 26)))
        pts.append("%s %s" % (_f(x + f_off * cw), _f(oy2)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), "#2f6f9f"))
    o.append(_txt(x0 + 16 * cw, oy2 + 14, "(c) bit sau khi cắt ngưỡng", 7.5, anchor="end", color=GREY))
    return _fig(svg(660, 318, "".join(o), "Bộ mã hoá tuyệt đối dùng mã nhị phân tự nhiên bốn rãnh"),
                "Hình 6-67 · (a) Bộ mã hoá tuyệt đối dùng mã nhị phân tự nhiên bốn chữ số, cần bốn rãnh. Đầu đọc di "
                "động có bốn cửa sổ và đang ở vị trí 7 trên thang. Rãnh dưới cùng mang chữ số có trọng số lớn nhất "
                "2³, rãnh trên cùng mang trọng số 2⁰. (b) Quang thông qua cửa sổ tương ứng với rãnh có trọng số nhỏ "
                "nhất — một sóng tam giác bị cắt bằng, thể hiện tỉ lệ diện tích sáng phủ lên cửa sổ. (c) Chữ số nhị "
                "phân thu được sau khi cắt ngưỡng tín hiệu thô. Với vị trí trong hình: 0×2³ + 1×2² + 1×2¹ + 1×2⁰ = 7.",
                "Figure 6.67 · (a) An absolute encoder using a natural binary code of four digits, requiring four "
                "tracks. The moving read head has four apertures and is shown at position 7 along the scale. The "
                "lowest track carries the most significant digit, weight 2³; the uppermost carries weight 2⁰. "
                "(b) The light flux through the aperture of the least significant track — a truncated triangular "
                "wave representing the proportion of bright area covering the aperture. (c) The binary digit "
                "obtained after thresholding the raw signal. For the position shown: 0×2³ + 1×2² + 1×2¹ + 1×2⁰ = 7.",
                "Bộ mã hoá tuyệt đối mã nhị phân bốn rãnh",
                "Four-track direct binary absolute encoder")


def fig_6_68():
    o = [_defs()]
    cw, x0 = 14.0, 88
    y0, th, gap = 44, 15, 4
    tracks = []
    for t in range(4):
        n_cells = 2 ** (t + 1)
        tracks.append("".join("1" if ((i * n_cells) // 16) % 2 else "0" for i in range(16)))
    for t, pat in enumerate(tracks):
        o.append(_cells(x0, y0 + (3 - t) * (th + gap), cw, th, pat))
        o.append(_txt(x0 - 12, y0 + (3 - t) * (th + gap) + 11, "2%s" % ("³²¹⁰"[t]), 8, anchor="end", color=GREY))
    # V-shaped read points: staggered left to right down the tracks
    offs = [-1.4, -0.5, 0.5, 1.4]
    base = 6.0
    xs = []
    for t in range(4):
        xx = x0 + (base + offs[t]) * cw
        xs.append(xx)
        y = y0 + (3 - t) * (th + gap)
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="1.6"/>'
                 % (_f(xx), _f(y - 2), _f(cw), _f(th + 4), GOLD))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>'
             % (" ".join("%s %s" % (_f(xs[t]), _f(y0 + (3 - t) * (th + gap) + th / 2.0)) for t in range(4)), GOLD))
    o.append(_txt(x0 + 8 * cw, 40, "điểm đọc xếp theo hình chữ V", 7.5, color=GOLD))
    o.append(_txt(171, 232, "dung sai vị trí của mỗi đầu đọc chỉ cần ±1/8 chu kỳ rãnh", 8, color=GREY))
    # logic block
    o.append(_rect(96, 158, 150, 52, "#fff"))
    o.append(_txt(171, 180, "logic tổ hợp", 8))
    o.append(_txt(171, 196, "4 đầu đọc → 4 bit", 7, color=GREY))
    o.append(_arrow(171, 120, 171, 156, sw=1))
    o.append(_arrow(246, 184, 300, 184, sw=1))
    o.append(_txt(306, 188, "mã nhị phân tự nhiên", 8, anchor="start", color=INK))
    o.append(_txt(306, 204, "(không còn nhập nhằng)", 7.5, anchor="start", color=GREY))
    return _fig(svg(660, 246, "".join(o), "Bố trí đầu đọc kiểu vee-scan"),
                "Hình 6-68 · Bố trí các đầu đọc theo hình chữ V loại bỏ tính nhập nhằng của thang nhị phân tự nhiên. "
                "Ưu điểm chính là dung sai vị trí của điểm chuyển mức trên mỗi đầu đọc chỉ cần ±1/8 chiều dài chu kỳ "
                "của rãnh tương ứng — ví dụ ±45° với rãnh có trọng số lớn nhất trên đĩa bộ mã hoá quay. Các tín hiệu "
                "đã cắt ngưỡng sau đó được tổ hợp bằng logic tổ hợp để cho ra từ nhị phân tự nhiên. Cái giá phải trả "
                "là thêm đầu đọc và thêm mạch xử lý.",
                "Figure 6.68 · The vee-scan configuration of reading units removes the ambiguity of a natural binary "
                "scale. Its main advantage is that the location tolerance of the transition point of each reading "
                "unit need only be ±1/8 of the cycle length of that particular track — for example ±45° for the most "
                "significant track of a rotary disk. The thresholded signals are then combined by combinational "
                "logic to give the natural binary word. The price is additional reading heads and additional "
                "processing electronics.",
                "Bố trí đầu đọc kiểu vee-scan",
                "Vee-scan read-head configuration")


def fig_6_69():
    o = [_defs()]
    cw, x0 = 14.0, 92
    y0, th, gap = 44, 15, 4
    # Gray code per column, MSB first
    pats = ["", "", "", ""]
    for i in range(16):
        g = i ^ (i >> 1)
        for b in range(4):
            pats[b] += "1" if (g >> (3 - b)) & 1 else "0"
    for t in range(4):
        o.append(_cells(x0, y0 + (3 - t) * (th + gap), cw, th, pats[t]))
        o.append(_txt(x0 - 12, y0 + (3 - t) * (th + gap) + 11, "g%s" % ("³²¹⁰"[t]), 8, anchor="end", color=GREY))
    for i in range(0, 17, 2):
        o.append(_txt(x0 + i * cw, 128, str(i), 6.5, color=GREY))
    o.append(_txt(x0 + 8 * cw, 36, "(a) thang mã Gray — mỗi bước chỉ đổi một bit", 7.5, color=GREY))
    # (b) conversion chain
    bx, by = 130, 194
    o.append(_txt(bx + 150, 172, "(b) chuyển Gray → nhị phân bằng cộng modul-2", 8, color=INK))
    labs = ["b₃ = g₃", "b₂ = b₃ ⊕ g₂", "b₁ = b₂ ⊕ g₁", "b₀ = b₁ ⊕ g₀"]
    for k, lab in enumerate(labs):
        y = by + k * 30
        if k == 0:
            o.append(_rect(bx, y - 14, 120, 24, "#f6e6c8"))
            o.append(_txt(bx + 60, y + 2, lab, 8))
        else:
            o.append(_rect(bx, y - 14, 120, 24, "#fff"))
            o.append(_txt(bx + 60, y + 2, lab, 8))
        if k < 3:
            o.append(_line(bx, y - 4, bx - 26, y - 4, sw=1))
            o.append(_line(bx - 26, y - 4, bx - 26, y + 30, sw=1))
            o.append(_arrow(bx - 26, y + 30, bx - 4, y + 30, sw=1))
    o.append(_txt(bx + 176, by + 26, "⊕ là phép XOR", 7.5, anchor="start", color=GREY))
    return _fig(svg(660, 322, "".join(o), "Mã Gray và cách chuyển sang nhị phân tự nhiên"),
                "Hình 6-69 · (a) Mã Gray cho phép chỉ chuyển mức trên một rãnh giữa hai vị trí liên tiếp, nhờ đó không "
                "phát sinh nhập nhằng. Mã Gray là mã đơn vị khoảng cách: chỉ một bit đổi giữa hai số liên tiếp. Nó "
                "có hai ưu điểm: dễ chuyển sang mã nhị phân trực tiếp, và các rãnh mịn có bề rộng gấp đôi so với "
                "rãnh tương đương của mã nhị phân trực tiếp. (b) Sơ đồ chuyển đổi: bit có trọng số lớn nhất của mã "
                "nhị phân bằng bit lớn nhất của mã Gray; sau đó cộng modul-2 bit vừa nhận được với bit kế tiếp của "
                "mã Gray để được bit nhị phân kế tiếp, và lặp lại cho tới hết. Phép cộng modul-2 chính là phép XOR.",
                "Figure 6.69 · (a) Gray code allows a transition on only one track between successive positions, so "
                "no ambiguity arises. Gray code is a unit-distance code: exactly one bit changes between consecutive "
                "numbers. It has two advantages — it converts easily to direct binary, and its finest tracks are "
                "twice the width of the equivalent direct binary tracks. (b) The conversion scheme: the most "
                "significant binary bit equals the most significant Gray bit; each subsequent binary bit is the "
                "modulo-2 sum of the previous binary bit and the next Gray bit. Modulo-2 addition is an exclusive-OR.",
                "Mã Gray và phép chuyển đổi",
                "Gray code and its conversion")


def fig_6_70():
    o = [_defs()]
    cx, cy = 168, 148
    # PRBS track: 15 sectors of 24 degrees
    seq = "111101011001000"
    for i, b in enumerate(seq):
        a1 = -90 + i * 24.0
        a2 = a1 + 24.0
        o.append(_annulus(cx, cy, 72, 92, a1, a2, "#2a2a2a" if b == "1" else "#ffffff"))
    # synchronization track: same record width, same phase, alternating
    sync = "101010101010101"
    for i, b in enumerate(sync):
        a1 = -90 + i * 24.0
        o.append(_annulus(cx, cy, 50, 62, a1, a1 + 24.0, "#2a2a2a" if b == "1" else "#ffffff"))
    o.append('<circle cx="%s" cy="%s" r="50" fill="none" stroke="%s" stroke-width="1"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<circle cx="%s" cy="%s" r="62" fill="none" stroke="%s" stroke-width="1"/>'
             % (_f(cx), _f(cy), INK))
    o.append('<circle cx="%s" cy="%s" r="9" fill="#fff" stroke="%s" stroke-width="1"/>'
             % (_f(cx), _f(cy), INK))
    o.append(_txt(cx, cy + 3, "trục", 6.5, color=GREY))

    # four reading heads on the PRBS track, one record apart
    for k, ang in enumerate((-36, -12, 12, 36)):
        o.append('<g transform="rotate(%s %s %s)"><rect x="%s" y="%s" width="14" height="7" '
                 'fill="#e0a24a" stroke="%s" stroke-width="0.7"/></g>'
                 % (ang, _f(cx), _f(cy), _f(cx + 74), _f(cy - 3.5), INK))
    o.append(_txt(cx + 96, cy - 56, "H(i)", 7, anchor="start", color="#8a5a10"))
    o.append(_line(cx + 94, cy - 58, cx + 72, cy - 50, sw=0.7, color="#8a5a10"))

    # one head unit with the two apertures A and B, half a record apart
    o.append(_rect(cx + 50, cy - 6, 12, 12, "#7fa8c9", sw=0.8))
    o.append(_line(cx + 50, cy, cx + 62, cy, sw=0.6, color=INK))
    o.append(_txt(cx, 34, "rãnh giả ngẫu nhiên 15 ô (n = 4)", 7.5, color=GREY))
    o.append(_txt(cx, 250, "rãnh đồng bộ", 7.5, color=GREY))
    o.append(_txt(cx, 264, "ô xanh: hai đầu đọc A, B lệch nửa ô", 7, color="#2f6f9f"))

    # processing chain
    bx, by = 330, 96
    def blk(y, t1, t2=""):
        o.append(_rect(bx, y, 140, 34, "#fff"))
        o.append(_txt(bx + 70, y + (17 if not t2 else 14), t1, 7.5))
        if t2:
            o.append(_txt(bx + 70, y + 26, t2, 7, color=GREY))
    blk(by, "n-tuple từ H(i)", "n bit")
    blk(by + 56, "logic hồi tiếp ngược", "dịch tới chuỗi ban đầu")
    blk(by + 112, "bộ đếm j", "số bước đã dịch")
    o.append(_arrow(bx + 70, by + 34, bx + 70, by + 54, sw=1))
    o.append(_arrow(bx + 70, by + 90, bx + 70, by + 110, sw=1))
    o.append(_arrow(bx + 140, by + 129, bx + 178, by + 129, sw=1))
    o.append(_txt(bx + 184, by + 124, "vị trí", 8, anchor="start", color=INK))
    o.append(_txt(bx + 184, by + 138, "j · 360/(2ⁿ−1)", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_line(cx + 108, cy, 300, cy, sw=0.8, color=GREY, dash="3 3"))
    o.append(_line(300, cy, 300, by + 17, sw=0.8, color=GREY, dash="3 3"))
    o.append(_arrow(300, by + 17, bx - 2, by + 17, sw=0.8, color=GREY))
    return _fig(svg(660, 274, "".join(o), "Bộ mã hoá trục giả ngẫu nhiên có rãnh đồng bộ"),
                "Hình 6-70 · Bộ mã hoá trục giả ngẫu nhiên với một rãnh đồng bộ đơn giản để kiểm chứng kết quả đọc "
                "của bộ n-tuple do các đầu đọc H(i) đọc được, với i = n, …, 1. Rãnh ngoài chứa chuỗi nhị phân giả ngẫu "
                "nhiên: mỗi dãy n ô liên tiếp là duy nhất, nên chỉ cần đọc n ô là biết ngay đang ở vị trí nào. Mạch "
                "bên phải là sơ đồ chuyển mã đơn giản sang nhị phân dựa trên logic hồi tiếp ngược: bộ đếm đếm số "
                "bước cần thiết để trở về chuỗi ban đầu, và chính số bước ấy là chỉ số vị trí j. Với bộ mã hoá quay, "
                "góc hiện tại là j·360/(2ⁿ−1); với bộ mã hoá thẳng, vị trí là j·P với P là bước của thang.",
                "Figure 6.70 · Pseudorandom shaft encoder with a simple synchronization track to validate the readout "
                "of the n-tuple read by the heads H(i), i = n, …, 1. The outer track carries a pseudorandom binary "
                "sequence: every run of n cells is unique, so reading n cells identifies the position immediately. "
                "The circuit at the right is a simplified code conversion to binary based on the reverse feedback "
                "logic: the counter counts the number of steps required to return to the initial sequence, and that "
                "count is the position index j. For a rotary encoder the angle is j·360/(2ⁿ−1); for a linear encoder "
                "the position is j·P, where P is the scale pitch.",
                "Bộ mã hoá giả ngẫu nhiên có rãnh đồng bộ",
                "Pseudorandom encoder with a synchronisation track")


def fig_6_71():
    o = [_defs()]
    cx, cy, R = 150, 132, 84
    # two cycles: four sectors of 90 degrees, alternating
    for i in range(4):
        a1 = -90 + i * 90.0
        o.append(_annulus(cx, cy, 70, R, a1, a1 + 90, "#2a2a2a" if i % 2 == 0 else "#ffffff"))
    o.append('<circle cx="%s" cy="%s" r="66" fill="none" stroke="%s" stroke-width="1"/>' % (_f(cx), _f(cy), GREY))
    o.append(_annulus(cx, cy, 54, 62, -90, -78, "#b45309"))
    o.append('<circle cx="%s" cy="%s" r="52" fill="none" stroke="%s" stroke-width="0.8" stroke-dasharray="3 3"/>'
             % (_f(cx), _f(cy), GREY))
    o.append('<circle cx="%s" cy="%s" r="10" fill="#fff" stroke="%s" stroke-width="1"/>' % (_f(cx), _f(cy), INK))
    o.append(_txt(cx, cy + 3, "trục", 6.5, color=GREY))
    # mask apertures
    o.append(_rect(cx + 84, cy - 26, 16, 16, "#e0a24a", sw=0.9))
    o.append(_txt(cx + 92, cy - 34, "A", 8, color="#8a5a10", weight="600"))
    o.append(_rect(cx + 60, cy - 84, 16, 16, "#e0a24a", sw=0.9))
    o.append(_txt(cx + 92, cy - 74, "B", 8, color="#8a5a10", weight="600"))
    o.append(_rect(cx - 8, cy - 66, 16, 8, "#7fa8c9", sw=0.8))
    o.append(_txt(cx - 18, cy - 58, "z", 8, anchor="end", color="#2f6f9f", weight="600"))
    o.append(_txt(cx, 34, "n = 2 chu kỳ trên một vòng", 7.5, color=GREY))
    o.append(_txt(cx + 60, cy + 92, "hai cửa sổ A và B lệch nhau 1/4 chu kỳ", 7.5, color=GREY))
    # quadrature waveforms
    ox, oy, w, amp = 300, 96, 320, 30
    o.append(_line(ox, oy + 10, ox + w, oy + 10, sw=1))
    o.append(_line(ox, oy + 10, ox, oy - amp - 8, sw=1))
    o.append(_txt(ox - 8, oy - amp, "A", 8, anchor="end", weight="600"))
    pts = []
    for i in range(4):
        x = ox + i * 80
        pts += ["%s %s" % (_f(x), _f(oy + 10)), "%s %s" % (_f(x), _f(oy - amp)),
                "%s %s" % (_f(x + 40), _f(oy - amp)), "%s %s" % (_f(x + 40), _f(oy + 10))]
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), "#c0392b"))
    oy2 = oy + 78
    o.append(_line(ox, oy2 + 10, ox + w, oy2 + 10, sw=1))
    o.append(_line(ox, oy2 + 10, ox, oy2 - amp - 8, sw=1))
    o.append(_txt(ox - 8, oy2 - amp, "B", 8, anchor="end", weight="600"))
    pts = []
    for i in range(4):
        x = ox + 20 + i * 80
        pts += ["%s %s" % (_f(x), _f(oy2 + 10)), "%s %s" % (_f(x), _f(oy2 - amp)),
                "%s %s" % (_f(x + 40), _f(oy2 - amp)), "%s %s" % (_f(x + 40), _f(oy2 + 10))]
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), "#2f6f9f"))
    o.append(_txt(ox + w, oy2 + 30, "90° điện", 7.5, anchor="end", color=GREY))
    o.append(_txt(ox + w / 2, oy - amp - 16, "hai kênh vuông pha sau khi cắt ngưỡng", 7.5, color=GREY))
    return _fig(svg(660, 264, "".join(o), "Bộ mã hoá quay gia số với hai kênh vuông pha"),
                "Hình 6-71 · Độ phân giải thấp nhất có thể của một bộ mã hoá quay gia số. Rãnh ngoài cung cấp n = 2 "
                "chu kỳ của các ô đen và trong xen kẽ. Hai đầu đọc A và B lệch nhau 90° cho ra, sau khi cắt ngưỡng, "
                "hai xung vuông vuông pha. Khi một ô sáng phủ lên cửa sổ thì có tín hiệu 1, ô tối cho 0; tại chỗ "
                "chuyển tiếp xuất hiện sườn lên hoặc sườn xuống. Các tín hiệu này phải qua tiền xử lý để làm vuông "
                "và tránh ảnh hưởng của chuyển động chậm tại vị trí chuyển tiếp. Rãnh trong cùng mang xung z dùng "
                "để đặt lại bộ đếm.",
                "Figure 6.71 · The lowest possible resolution of a rotary incremental encoder. The outer track provides "
                "n = 2 cycles of alternating dark and clear records. Two heads A and B displaced by 90° give, after "
                "squaring, two square waves in quadrature. A light sector over a window produces a 1, a dark one a 0; "
                "at a transition a rising or falling edge occurs. These signals need preprocessing to square them and "
                "to avoid the slow-edge problems of slow motion at a transition. The innermost track carries the "
                "z-phase used to reset the counter.",
                "Bộ mã hoá quay gia số hai kênh vuông pha",
                "Incremental rotary encoder with quadrature outputs")


def fig_6_72():
    o = [_defs()]
    panels = [
        (16, "(a) Conner", ["Schmitt", "D flip-flop"], "xung đếm + hướng"),
        (228, "(b) Kuzdrall", ["2 flip-flop", "74HC193"], "xung lên / xuống"),
        (440, "(c) Venugopal", ["monostable ×2", "74LS193"], "xung lên / xuống"),
    ]
    for x, title, blocks, out in panels:
        o.append(_txt(x + 100, 36, title, 8, weight="600"))
        o.append(_rect(x + 26, 52, 148, 34, "#fff"))
        o.append(_txt(x + 100, 66, "A, B", 7.5))
        o.append(_txt(x + 100, 79, "hai kênh vuông pha", 7, color=GREY))
        for k, bl in enumerate(blocks):
            y = 106 + k * 46
            o.append(_rect(x + 26, y, 148, 34, "#fff"))
            o.append(_txt(x + 100, y + 21, bl, 7.5))
            o.append(_arrow(x + 100, y - 20 if k == 0 else y - 12, x + 100, y - 2, sw=1))
        ylast = 106 + len(blocks) * 46 - 12
        o.append(_arrow(x + 174, 69, x + 174, 104, sw=1))
        o.append(_line(x + 174, 69, x + 174, 69, sw=1))
        o.append(_arrow(x + 174, ylast + 22, x + 174, ylast + 40, sw=1))
        o.append(_txt(x + 100, ylast + 58, out, 7.5, color=GOLD, weight="600"))
    o.append(_txt(330, 262, "cả ba mạch đều cho một xung mỗi chu kỳ vuông pha", 8, color=GREY))
    return _fig(svg(660, 276, "".join(o), "Ba mạch tạo xung đếm và tín hiệu hướng"),
                "Hình 6-72 · Ba mạch tạo xung đếm và tín hiệu hướng từ hai kênh vuông pha. (a) Mạch của Conner cho một "
                "xung mỗi chu kỳ vuông pha, kèm thông tin hướng; các Schmitt trigger tạo một lượng trễ và làm sạch "
                "các sườn. Cần thận trọng khi dùng mạch này để đếm, vì có thể phát sinh nhiều xung khi bộ mã hoá dao "
                "động quanh các trạng thái A = 0, B = 0 và A = 0, B = 1. (b) Mạch của Kuzdrall đếm lên và đếm xuống "
                "tại cùng một chỗ chuyển trạng thái, tuỳ theo chiều chuyển động, nhờ đó giảm được vấn đề dao động "
                "nhỏ quanh một vị trí. (c) Mạch của Venugopal dùng hai monostable để đạt hiệu quả tương tự: chỉ đếm "
                "khi B ở mức thấp và có chuyển mức trên A.",
                "Figure 6.72 · Three circuits producing a count and a direction signal from two quadrature channels. "
                "(a) Conner’s circuit gives one count per quadrature cycle together with direction information; "
                "Schmitt triggers provide hysteresis and clean the edges. Care is needed when using it for counting, "
                "since multiple counts are possible when the encoder oscillates around the A = 0, B = 0 and "
                "A = 0, B = 1 states. (b) Kuzdrall’s circuit counts up and down at the same state transition, "
                "depending on the direction of movement, which reduces the problem of small oscillations about a "
                "position. (c) Venugopal’s circuit uses two monostables to the same effect: a count occurs only when "
                "B is low and there is a transition on A.",
                "Ba mạch tạo xung đếm và hướng",
                "Three quadrature counting circuits")


def fig_6_73():
    o = [_defs()]
    o.append(_rect(30, 60, 90, 40, "#fff"))
    o.append(_txt(75, 78, "A, B", 8))
    o.append(_txt(75, 92, "vuông pha", 7, color=GREY))
    o.append(_rect(150, 44, 100, 34, "#fff"))
    o.append(_txt(200, 66, "thanh ghi dịch 1", 7.5))
    o.append(_rect(150, 86, 100, 34, "#fff"))
    o.append(_txt(200, 108, "thanh ghi dịch 2", 7.5))
    o.append(_arrow(120, 80, 148, 61, sw=1))
    o.append(_arrow(120, 80, 148, 103, sw=1))
    o.append(_rect(280, 60, 80, 44, "#fff"))
    o.append(_txt(320, 78, "3 cổng XOR", 7.5))
    o.append(_txt(320, 92, "mã 4 bit", 7, color=GREY))
    o.append(_arrow(250, 61, 278, 74, sw=1))
    o.append(_arrow(250, 103, 278, 90, sw=1))
    o.append(_rect(390, 60, 96, 44, "#fff"))
    o.append(_txt(438, 78, "74LS138", 7.5))
    o.append(_txt(438, 92, "giải mã 8 kênh", 7, color=GREY))
    o.append(_arrow(360, 82, 388, 82, sw=1))
    o.append(_rect(516, 60, 108, 44, "#fff"))
    o.append(_txt(570, 78, "74ALS193", 7.5))
    o.append(_txt(570, 92, "nối tầng", 7, color=GREY))
    o.append(_arrow(486, 76, 514, 76, sw=1))
    o.append(_arrow(486, 90, 514, 90, sw=1))
    o.append(_txt(570, 56, "đếm lên", 6.5, color=GREY))
    o.append(_txt(570, 118, "đếm xuống", 6.5, color=GREY))
    o.append(_txt(330, 152, "tần số nhịp ≥ 8·N·S", 9, color=GOLD, weight="600"))
    o.append(_txt(330, 170, "N: số chu kỳ mỗi vòng · S: tốc độ lớn nhất (vòng/s)", 7.5, color=GREY))
    o.append(_txt(330, 196, "phân tích trạng thái hiện tại và trạng thái trước của A, B", 7.5, color=INK))
    o.append(_txt(330, 212, "→ đếm lên, đếm xuống, hoặc báo lỗi khi trình tự sai", 7.5, color=INK))
    return _fig(svg(660, 230, "".join(o), "Mạch chia bốn cho bốn xung mỗi chu kỳ vuông pha"),
                "Hình 6-73 · Mạch chia bốn cho bốn xung mỗi chu kỳ của tín hiệu vuông pha, dựa trên thiết kế của "
                "Butler, chỉ thay bộ giải mã 4051 bằng 74LS138 vì bộ kia có thời gian lên và xuống không bằng nhau. "
                "Hai thanh ghi dịch 4 bit, ba cổng XOR và một bộ giải mã 8 kênh tạo ra các tín hiệu đếm lên và đếm "
                "xuống. Các thanh ghi dịch được nhịp tạo mã 4 bit cho bộ giải mã ở mỗi chu kỳ nhịp. Để không bỏ sót "
                "chuyển mức nào của bộ mã hoá, tần số nhịp phải ít nhất bằng 8 lần tích N·S, với N là số chu kỳ mỗi "
                "vòng và S là tốc độ lớn nhất tính bằng vòng trên giây. Mạch phân tích trạng thái hiện tại và trạng "
                "thái trước của hai kênh để quyết định đếm lên, đếm xuống hay phát cờ lỗi khi trình tự sai.",
                "Figure 6.73 · A divide-by-four circuit giving four counts per quadrature cycle, based on Butler’s "
                "design with the LS138 decoder replacing the suggested 4051 because of the latter’s unequal rise and "
                "fall times. Two 4-bit shift registers, three exclusive-OR gates and an eight-channel demultiplexer "
                "derive the up and down count signals; the clocked shift registers generate a 4-bit code for the "
                "demultiplexer on each clock cycle. To ensure that no encoder transition is missed, the clock "
                "frequency should be at least 8 times N·S, where N is the number of cycles per revolution and S the "
                "maximum speed in revolutions per second. The circuit analyses the current and previous states of the "
                "A and B channels to count up, count down, or issue an error flag when the sequence is improper.",
                "Mạch chia bốn",
                "Divide-by-four circuit")


def fig_6_74():
    o = [_defs()]
    # ---------------- (a) vector combination in a resistor network
    o.append(_txt(300, 30, "(a) tạo tín hiệu lệch pha bằng mạng điện trở", 8, weight="600"))
    o.append(_txt(28, 86, "A = sin θ", 8, anchor="start"))
    o.append(_txt(28, 150, "B = cos θ", 8, anchor="start"))
    o.append(_arrow(108, 82, 150, 82, sw=1))
    o.append(_arrow(108, 146, 150, 146, sw=1))
    o.append(_rect(150, 60, 110, 112, "#fbfcfd"))
    o.append(_txt(205, 108, "mạng trọng số", 7.4))
    o.append(_txt(205, 124, "A·cos α + B·sin α", 6.6, color=GREY))
    for y, lab, col in ((82, "sin(θ + α)", GOLD), (146, "cos(θ + α)", "#2f6f9f")):
        o.append(_arrow(260, y, 330, y, sw=1))
        o.append(_txt(295, y - 7, lab, 7, color=col, weight="600"))
        o.append(_rect(330, y - 15, 62, 30, "#fff"))
        o.append(_txt(361, y + 4, "so sánh", 7.2))
        o.append(_arrow(392, y, 420, y, sw=1))
        o.append(_rect(420, y - 15, 46, 30, "#fff"))
        o.append(_txt(443, y + 4, "TTL", 7.2))
        o.append(_arrow(466, y, 494, y, sw=1))
    o.append(_rect(494, 60, 92, 112, "#fff"))
    o.append(_txt(540, 106, "XOR", 8.6))
    o.append(_txt(540, 124, "8 tín hiệu", 6.8, color=GREY))
    o.append(_txt(540, 138, "cộng modulo 2", 6.8, color=GREY))
    for y, lab, col in ((82, "A′", "#c0392b"), (146, "B′", "#2f6f9f")):
        o.append(_arrow(586, y, 620, y, sw=1.2))
        o.append(_txt(626, y + 4, lab, 9, anchor="start", color=col, weight="600"))

    # ---------------- (b) eight phase-shifted signals
    o.append(_txt(330, 206, "(b) tám tín hiệu lệch nhau α = iπ/8 và kết quả sau khi làm vuông", 8, weight="600"))
    ox, w, base, amp = 60.0, 420.0, 300.0, 22.0
    o.append(_txt(ox, 266, "α = iπ/8,  i = 0 … 7", 7, anchor="start", color=GREY))
    for k in range(8):
        t = k / 7.0
        r = int(138 + t * 86)
        g = int(58 + t * 110)
        b = int(12 + t * 94)
        col = "#%02x%02x%02x" % (r, g, b)
        pts = []
        for i in range(181):
            x = i / 180.0
            v = math.sin(2 * math.pi * (3 * x + k / 16.0))
            pts.append("%s %s" % (_f(ox + x * w), _f(base - v * amp)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.1"/>'
                 % (" ".join(pts), col))
    o.append(_line(ox, 336, ox + w, 336, sw=0.7, color=GREY))
    o.append(_txt(ox + w + 8, 339, "t", 7.5, anchor="start", color=GREY))
    # squared results
    for k, (lab, col, off, yb) in enumerate((("A′", "#c0392b", 0, 372),
                                             ("B′", "#2f6f9f", 35, 410))):
        pts = []
        if off:
            pts += ["%s %s" % (_f(ox), _f(yb - 15 if 0 % 2 == 0 else yb)),
                    "%s %s" % (_f(ox + off), _f(yb - 15))]
        for j in range(6):
            x0 = ox + off + j * 70.0
            x1 = min(x0 + 70.0, ox + w)
            if x0 >= ox + w:
                break
            yv = yb - 15 if j % 2 == 0 else yb
            pts += ["%s %s" % (_f(x0), _f(yv)), "%s %s" % (_f(x1), _f(yv))]
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>'
                 % (" ".join(pts), col))
        o.append(_txt(ox - 8, yb - 4, lab, 8.5, anchor="end", color=col, weight="600"))
    return _fig(svg(660, 428, "".join(o), "Nội suy bằng mạng điện trở theo phương pháp của Benzaid"),
                "Hình 6-74 · Mạch nội suy của Benzaid và cộng sự. Hai tín hiệu sin và cos từ bộ mã hoá được tổ hợp "
                "vectơ để tạo ra các tín hiệu lệch pha khác nhau: ngoài A và B còn sáu tín hiệu nữa, ba tín hiệu lệch "
                "π/8, π/4 và 3π/8 so với A, ba tín hiệu còn lại lệch tương tự so với B. Như vậy có tổng cộng tám tín "
                "hiệu sin lệch pha nhau α = iπ/8 với i = 0, 1, …, 7. Tổng quát, muốn tăng độ phân giải m lần cần 2m "
                "tín hiệu lệch pha nhau iπ/2m. Sau khi làm vuông bằng các bộ chuyển mức TTL, việc cộng modul-2 các "
                "tín hiệu có i chẵn cho A′ và các tín hiệu có i lẻ cho B′ — phép cộng modul-2 thực hiện bằng cổng "
                "XOR. Biên độ của các tín hiệu lệch pha không quan trọng, vì chính điểm qua zero mới tạo ra sườn "
                "xung vuông.",
                "Figure 6.74 · The interpolation circuit of Benzaid et al. The sine and cosine signals from the encoder "
                "are vector-combined to produce phase-shifted signals: besides A and B, six more, three shifted by "
                "π/8, π/4 and 3π/8 from A and three shifted similarly from B — eight sinusoidal signals in all, "
                "phase-shifted by α = iπ/8 with i = 0, 1, …, 7. In general an m-fold increase in resolution requires "
                "2m signals phase-shifted by iπ/2m. After TTL squaring, the modulo-2 sum of the even-i signals gives "
                "A′ and of the odd-i signals gives B′; the modulo-2 sum is performed by exclusive-OR gates. The "
                "amplitudes of the shifted signals are not critical, since it is their zero crossings that produce "
                "the square-wave transitions.",
                "Nội suy bằng mạng điện trở",
                "Resistor-network interpolation")


def fig_6_75():
    o = [_defs()]
    # ---- (a) 8x8 grid
    ox, oy, cell = 90, 226, 26
    n = 6
    o.append(_txt(ox + n * cell / 2.0, 44, "(a) bảng tra hai chiều", 8, weight="600"))
    for i in range(n + 1):
        o.append(_line(ox + i * cell, oy - n * cell, ox + i * cell, oy, sw=0.6, color=GREY))
        o.append(_line(ox, oy - i * cell, ox + n * cell, oy - i * cell, sw=0.6, color=GREY))
    # highlighted cell
    hx, hy = 4, 2
    o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" opacity="0.55"/>'
             % (_f(ox + hx * cell), _f(oy - (hy + 1) * cell), _f(cell), _f(cell), FILL))
    o.append(_txt(ox + (hx + 0.5) * cell, oy - (hy + 0.5) * cell + 3, "θ", 8, color=GOLD, weight="600"))
    # angle ray
    o.append(_arrow(ox + n * cell / 2.0, oy - n * cell / 2.0,
                    ox + (hx + 0.5) * cell, oy - (hy + 0.5) * cell, sw=1, color="#c0392b"))
    o.append('<circle cx="%s" cy="%s" r="2.5" fill="%s"/>'
             % (_f(ox + n * cell / 2.0), _f(oy - n * cell / 2.0), INK))
    o.append(_txt(ox + n * cell / 2.0, oy + 16, "D_a", 8, color=GREY))
    o.append(_txt(ox - 10, oy - n * cell / 2.0, "D_b", 8, anchor="end", color=GREY))
    o.append(_txt(ox + n * cell / 2.0, oy + 34, "giá trị số hoá của A, B", 7.5, color=GREY))
    # ---- (b) phase code
    bx = 330
    o.append(_txt(bx + 130, 44, "(b) mã pha gán cho mỗi ô", 8, weight="600"))
    o.append(_rect(bx, 76, 260, 46, "#fff"))
    o.append(_txt(bx + 130, 98, "mã pha = phần nguyên của", 7.5))
    o.append(_txt(bx + 130, 112, "2ⁿ · θ / 2π", 9, color=GOLD, weight="600"))
    o.append(_rect(bx, 146, 260, 46, "#fff"))
    o.append(_txt(bx + 130, 168, "cộng dồn các giá trị nội suy", 7.5))
    o.append(_txt(bx + 130, 182, "→ vị trí tuyệt đối", 7.5))
    o.append(_arrow(bx + 130, 122, bx + 130, 144, sw=1))
    o.append(_rect(bx, 216, 260, 46, "#fff"))
    o.append(_txt(bx + 130, 238, "hiệu chỉnh theo sai số đã biết", 7.5))
    o.append(_txt(bx + 130, 252, "của tín hiệu so với vị trí thật", 7.5))
    o.append(_arrow(bx + 130, 192, bx + 130, 214, sw=1))
    return _fig(svg(660, 292, "".join(o), "Bảng tra hai chiều để nội suy tín hiệu vuông pha"),
                "Hình 6-75 · Hagiwara đề xuất một bảng tra hai chiều gán một giá trị pha lượng tử hoá cho mỗi cặp giá "
                "trị số hoá của hai tín hiệu vuông pha. (a) Một bộ chuyển đổi A/D m bit số hoá A và B thành các số "
                "nhị phân D_a và D_b; hai số này làm địa chỉ của một ma trận 2ᵐ × 2ᵐ (ở đây vẽ với m = 3). Một góc pha "
                "được gán cho tâm mỗi ô bằng một phép tính arctan đơn giản. (b) Góc pha ấy sau đó được gán cho một "
                "trong 2ⁿ − 1 mã pha. Mạch còn có phương tiện cộng dồn các giá trị nội suy để cho ra vị trí tuyệt đối "
                "của bộ mã hoá, và có thể hiệu chỉnh mã pha theo những sai số đã biết của tín hiệu so với vị trí thật.",
                "Figure 6.75 · Hagiwara proposes a two-dimensional look-up table that associates a quantised phase "
                "value with each digitised pair of the quadrature signals. (a) An m-bit ADC digitises A and B into "
                "the binary numbers D_a and D_b, which serve as the address of a 2ᵐ × 2ᵐ grid (drawn here for m = 3). "
                "A phase angle is associated with the centre of each cell by a simple arctangent calculation. (b) "
                "That angle is then associated with one of 2ⁿ − 1 phase codes. The circuit also accumulates the "
                "interpolated values to deliver the absolute position, and can compensate the phase code for known "
                "errors of the signals with respect to the actual position.",
                "Bảng tra hai chiều để nội suy",
                "Two-dimensional look-up table")


def fig_6_76():
    o = [_defs()]
    # source
    o.append(_rect(24, 96, 34, 30, "#f7fbff"))
    o.append(_txt(41, 114, "LED", 7.5))
    o.append(_txt(41, 86, "nguồn sáng", 7, color=GREY))
    # condenser
    o.append('<ellipse cx="92" cy="111" rx="9" ry="22" fill="#dce9f5" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(92, 146, "thấu kính", 7, color=GREY))
    o.append(_txt(92, 158, "chuẩn trực", 7, color=GREY))
    # collimated rays
    for yy in (98, 111, 124):
        o.append(_arrow(102, yy, 168, yy, sw=0.9, color="#c0392b"))
    # index grating
    for k in range(9):
        o.append(_line(172 + k * 5, 82, 172 + k * 5, 140, sw=1.4, color="#4a6b8a"))
    o.append(_txt(190, 72, "cách tử chỉ mục (cố định)", 7.5, color="#4a6b8a"))
    # moving grating
    for k in range(9):
        o.append(_line(250 + k * 5, 82, 250 + k * 5, 140, sw=1.4, color=INK))
    o.append(_arrow(272, 158, 272, 148, sw=1))
    o.append(_txt(272, 174, "cách tử động", 7.5))
    o.append(_txt(272, 186, "dịch theo chuyển động cần đo", 7, color=GREY))
    # transmitted bands
    for yy in (98, 111, 124):
        o.append(_arrow(296, yy, 360, yy, sw=0.9, color="#c0392b"))
    o.append(_txt(328, 88, "vùng sáng tối", 7, color="#c0392b"))
    # detector
    o.append(_rect(364, 84, 18, 54, "#f6e6c8"))
    o.append(_txt(373, 152, "bộ tách sóng", 7.5))
    o.append(_txt(373, 164, "quang", 7.5))
    o.append(_arrow(382, 111, 424, 111, sw=1))
    o.append(_txt(430, 115, "tín hiệu tỉ lệ", 7.5, anchor="start"))
    o.append(_txt(430, 127, "với tổng quang thông", 7.5, anchor="start"))
    # waveform
    ox, oy = 430, 210
    o.append(_line(ox, oy, ox + 190, oy, sw=1))
    pts = []
    for i in range(121):
        u = i / 120.0
        pts.append("%s %s" % (_f(ox + u * 190), _f(oy - 30 * (0.5 + 0.5 * math.cos(2 * math.pi * u * 4)))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), GOLD))
    o.append(_txt(ox + 95, oy + 16, "một chu kỳ = một bước cách tử", 7.5, color=GREY))
    return _fig(svg(660, 236, "".join(o), "Che hình học trong bộ mã hoá quang"),
                "Hình 6-76 · Nguyên lý che hình học. Đầu đọc chứa một nguồn sáng — có thể là bóng đèn sợi đốt hoặc "
                "điốt phát quang — và một thấu kính tụ quang để chuẩn trực chùm tia, tức làm cho các tia sáng song song "
                "và vuông góc với mặt cách tử. Cách tử chỉ mục cố định chia chùm sáng thành từng dải, các dải này đi "
                "qua cách tử động. Tuỳ vị trí tương đối của hai cách tử mà nhiều hay ít ánh sáng tới được bộ tách "
                "sóng; bộ tách sóng tạo ra tín hiệu tỉ lệ với tổng lượng ánh sáng rơi trên bề mặt nhạy của nó. Với "
                "bộ mã hoá gia số, đầu đọc thứ hai đọc trên cùng cách tử động nhưng lệch đi n + 1/4 bước để tạo tín "
                "hiệu thứ hai lệch pha 90°.",
                "Figure 6.76 · The principle of geometric masking. The read head contains a light source — an "
                "incandescent bulb or a light-emitting diode — and a condenser that collimates the beam so that the "
                "rays travel perpendicular to the gratings. The stationary index grating structures the light into "
                "bands, which then cross the moving grating. Depending on the relative position of the two gratings, "
                "more or less light reaches the photodetector, which produces a signal proportional to the total "
                "light on its sensitive surface. In an incremental encoder a second head reads the same moving "
                "grating displaced by n + 1/4 pitch to produce a second signal 90° out of phase.",
                "Che hình học",
                "Geometric masking")


def fig_6_77():
    o = [_defs()]
    # ---------------- (a) two linear gratings rotated by a small angle
    ax, ay, aw, ah = 46, 48, 196, 196
    cx0, cy0 = ax + aw / 2.0, ay + ah / 2.0
    P = 5.0
    gam = math.radians(8.0)
    o.append('<clipPath id="c77a"><rect x="%s" y="%s" width="%s" height="%s"/></clipPath>'
             % (_f(ax), _f(ay), _f(aw), _f(ah)))
    o.append(_rect(ax, ay, aw, ah, "#ffffff"))
    o.append('<g clip-path="url(#c77a)">')
    for ang, col in ((-4.0, "#3f6c8f"), (4.0, "#c0392b")):
        o.append('<g transform="rotate(%s %s %s)">' % (ang, _f(cx0), _f(cy0)))
        for k in range(-72, 73):
            yy = cy0 + k * P
            o.append(_line(ax - 70, yy, ax + aw + 70, yy, sw=0.8, color=col))
        o.append('</g>')
    # moiré fringes: vertical, period d = P / (2 sin(gamma/2))
    d = P / (2 * math.sin(gam / 2))
    nb = int(aw / d) + 2
    for k in range(-nb, nb + 1):
        xc = cx0 + k * d
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#141414" opacity="0.28"/>'
                 % (_f(xc - d / 2), _f(ay), _f(d / 2), _f(ah)))
    o.append('</g>')
    o.append(_rect(ax, ay, aw, ah, "none", sw=1.2))
    o.append(_txt(cx0, 268, "(a) hai cách tử thẳng lệch nhau góc nhỏ γ", 7.6))
    o.append(_txt(cx0, 285, "vân thẳng đứng, chu kỳ d = P / (2 sin γ/2)", 7, color=GREY))

    # ---------------- (b) radial gratings with displaced centres
    bx, by, R = 498, 146, 86
    delta = 3.0
    o.append('<clipPath id="c77b"><circle cx="%s" cy="%s" r="%s"/></clipPath>'
             % (_f(bx), _f(by), _f(R)))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.2"/>'
             % (_f(bx), _f(by), _f(R), INK))
    o.append('<g clip-path="url(#c77b)">')
    for k in range(60):
        a = math.radians(k * 6.0)
        o.append(_line(bx + 13 * math.cos(a), by + 13 * math.sin(a),
                       bx + R * math.cos(a), by + R * math.sin(a), sw=0.55, color="#3f6c8f"))
    for k in range(60):
        a = math.radians(k * 6.0 + 3.0)
        o.append(_line(bx + 2 * delta + 13 * math.cos(a), by + 13 * math.sin(a),
                       bx + 2 * delta + R * math.cos(a), by + R * math.sin(a),
                       sw=0.55, color="#c0392b"))
    # fringes: circles through both centres
    step = 15.0
    for k in list(range(-7, 0)) + list(range(1, 8)):
        cyk = by + k * step
        rr = math.hypot(delta, k * step)
        o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="#1a1a1a" '
                 'stroke-width="1.9" opacity="0.75"/>'
                 % (_f(bx + delta), _f(cyk), _f(rr)))
    o.append('</g>')
    o.append('<circle cx="%s" cy="%s" r="1.9" fill="%s"/>' % (_f(bx), _f(by), INK))
    o.append('<circle cx="%s" cy="%s" r="1.9" fill="%s"/>' % (_f(bx + 2 * delta), _f(by), INK))
    o.append(_txt(bx, 268, "(b) hai cách tử hướng tâm lệch tâm 2δ", 7.6))
    o.append(_txt(bx, 285, "vân là đường tròn đi qua cả hai tâm", 7, color=GREY))

    return _fig(svg(660, 300, "".join(o), "Vân Moiré tạo bởi hai cách tử chồng lên nhau"),
                "Hình 6-77 · Vân Moiré xuất hiện khi hai cách tử cùng bước được chồng lên nhau. (a) Hai cách tử thẳng "
                "bị xoay lệch nhau một góc nhỏ — chẳng hạn do sai số lắp ráp. Khi ấy vân Moiré xuất hiện song song với "
                "đường phân giác của hai hướng cách tử và có chu kỳ lớn hơn bước rất nhiều: d = P/(2 sin γ/2). Dịch "
                "chuyển bình thường của một cách tử đi nửa bước làm mẫu vân Moiré đổi pha 180° tại mọi điểm quan sát "
                "cố định. (b) Hai cách tử hướng tâm có tâm lệch nhau: vân luôn là những đường tròn và đều đi qua hai "
                "tâm; bề rộng vân phụ thuộc lượng lệch tâm. Nếu hai tâm trùng nhau thì toàn bộ vùng quan sát chuyển "
                "từ tối sang sáng đồng thời — hiện tượng mà Burch gọi là vân “xù” ra tới bề rộng vô hạn.",
                "Figure 6.77 · Moiré fringes appear when two gratings of equal pitch are superimposed. (a) Two linear "
                "gratings rotated by a small angle — as an assembly error might do. The Moiré fringes then run "
                "parallel to the bisector of the two grating directions with a period far larger than the pitch: "
                "d = P/(2 sin γ/2). Normal displacement of one grating by half a pitch changes the phase of the "
                "fringe pattern by 180° at any fixed observation point. (b) Two radial gratings with displaced "
                "centres: the fringes are always circles passing through both centres, and their width depends on "
                "the offset. If the centres coincide, the whole region goes from dark to bright at once — the "
                "fringes are said to be fluffed out to infinite width.",
                "Vân Moiré",
                "Moiré fringes")


def fig_6_78():
    o = [_defs()]
    # ---- incoming plane wavefronts
    for x in (26, 44, 62, 80):
        o.append(_line(x, 56, x, 226, sw=1, color="#c0392b"))
    o.append(_arrow(96, 141, 130, 141, sw=1.2, color="#c0392b"))
    o.append(_txt(56, 46, "sóng tới", 7.4, color="#c0392b"))

    # ---- grating: opaque bar with three slits
    o.append(_rect(140, 48, 12, 186, INK, sw=0.8))
    for y in (100, 140, 180):
        o.append('<rect x="140" y="%s" width="12" height="9" fill="#ffffff"/>' % _f(y - 4.5))
    o.append(_txt(146, 252, "cách tử", 7.2, color=GREY))

    # ---- circular wavefronts fanning out of each slit
    for cy in (100, 140, 180):
        for j in range(1, 6):
            r = j * 18.0
            a1, a2 = math.radians(-60), math.radians(60)
            o.append('<path d="M%s %s A%s %s 0 0 1 %s %s" fill="none" stroke="#3f6c8f" '
                     'stroke-width="0.8" opacity="0.55"/>'
                     % (_f(152 + r * math.cos(a1)), _f(cy + r * math.sin(a1)), _f(r), _f(r),
                        _f(152 + r * math.cos(a2)), _f(cy + r * math.sin(a2))))

    # ---- diffracted beam: plane wavefronts at angle theta
    th = math.radians(18)
    ox, oy = 152.0, 140.0
    ux, uy = math.cos(th), math.sin(th)
    px, py = -uy, ux
    L, half, dlam, t0 = 320.0, 46.0, 20.0, 180.0
    for k in range(int(t0 / dlam), int(L / dlam) + 1):
        t = k * dlam
        cxp, cyp = ox + t * ux, oy + t * uy
        o.append(_line(cxp - half * px, cyp - half * py, cxp + half * px, cyp + half * py,
                       sw=1.1, color=GOLD))
    o.append(_arrow(ox, oy, ox + L * ux, oy + L * uy, sw=1.2, color=GOLD))

    # ---- reference axis (order m = 0)
    o.append(_line(152, 140, 600, 140, sw=0.7, color=GREY, dash="4 4"))
    o.append(_txt(596, 132, "bậc 0", 7, anchor="end", color=GREY))

    # ---- angle between the axis and the diffracted beam
    r = 150.0
    ex, ey = ox + r, oy
    fx, fy = ox + r * math.cos(th), oy + r * math.sin(th)
    o.append('<path d="M%s %s A%s %s 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="1.1"/>'
             % (_f(ex), _f(ey), _f(r), _f(r), _f(fx), _f(fy), INK))
    o.append(_txt(312, 166, "θ₁", 9, color=INK, weight="600"))

    o.append(_txt(482, 250, "sóng nhiễu xạ bậc m = 1", 7.4, anchor="start", color=GOLD))
    o.append(_txt(320, 304, "sin θ_m = m λ / P", 10, color=INK, weight="600"))

    return _fig(svg(660, 318, "".join(o), "Nhiễu xạ của sóng phẳng qua cách tử"),
                "Hình 6-78 · Cách tử nhiễu xạ sóng phẳng kết hợp tới từ bên trái thành một loạt sóng cầu. Mỗi khe có "
                "thể coi như một nguồn sáng kết hợp phát ra mặt sóng tròn. Dọc theo những phương nhất định, các phần "
                "mặt sóng ấy đồng pha với nhau; phương ấy được cho bởi sin θ_m = mλ/P, với m là số nguyên dương hoặc "
                "âm gọi là bậc nhiễu xạ và P là bước của cách tử. Nếu các khe dịch đi một đoạn x thì pha của mặt sóng "
                "tại một điểm cố định tăng (với m dương) hoặc giảm (với m âm) một lượng 2πmx/P. Khi cách tử dịch đúng "
                "một bước, hai mặt sóng đã lệch pha nhau 2m chu kỳ; hai mặt sóng lệch pha ấy có thể được hợp lại để "
                "tạo vân giao thoa.",
                "Figure 6.78 · The grating diffracts the coherent plane wavefront arriving from the left into a series "
                "of circular wavefronts. Each slit acts as a coherent source emitting circular wavefronts. Along "
                "certain directions these wavefronts are in phase with each other; those directions are given by "
                "sin θ_m = mλ/P, where m is a positive or negative integer — the order of diffraction — and P is the "
                "grating period. If the slits move by x, the phase at a stationary point increases for positive m and "
                "decreases for negative m by 2πmx/P. When the pattern has moved by one period, the two wavefronts "
                "have developed a relative phase change of 2m cycles, and the two phase-shifted wavefronts may be "
                "recombined to produce interference fringes.",
                "Nhiễu xạ qua cách tử",
                "Diffraction at a grating")


def fig_6_79():
    o = [_defs()]
    # ---- laser diode
    o.append(_rect(28, 138, 64, 26, "#f7fbff"))
    o.append(_txt(60, 155, "laser bán dẫn", 6.6))
    o.append(_arrow(92, 151, 166, 151, sw=1.3, color="#c0392b"))

    # ---- beam splitter
    o.append('<rect x="164" y="136" width="30" height="30" fill="#dce9f5" stroke="%s" stroke-width="1.1" '
             'transform="rotate(45 179 151)"/>' % INK)
    o.append(_txt(179, 122, "bộ chia chùm", 6.6, color=GREY))

    # ---- the two arms, drawn to the grating points U and L
    U = (300.0, 86.0)
    Lo = (300.0, 216.0)
    du = (0.898, -0.441)
    dl = (0.898, 0.441)

    # ---- hologram grating (the moving scale)
    o.append(_rect(300, 46, 13, 208, "#f2f2f2"))
    for k in range(22):
        o.append(_line(302, 50 + k * 9, 311, 56 + k * 9, sw=0.8, color=GREY))
    o.append(_txt(306, 38, "cách tử 0,55 µm", 6.6, color=GREY))

    # ---- plane mirrors, perpendicular to each arm, just beyond the grating
    def _mirror(pt, ux, uy, tag_y, lab):
        cx, cy = pt[0] + 70 * ux, pt[1] + 70 * uy
        px, py = -uy, ux
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#9a9a9a" stroke-width="5.5" '
                 'stroke-linecap="round"/>'
                 % (_f(cx - 18 * px), _f(cy - 18 * py), _f(cx + 18 * px), _f(cy + 18 * py)))
        o.append(_txt(cx + 22, tag_y, lab, 6.6, anchor="start", color=GREY))
        return (cx, cy)

    MU = _mirror(U, du[0], du[1], 40, "gương")
    ML = _mirror(Lo, dl[0], dl[1], 274, "gương")

    # ---- each arm: outbound (red) and return (blue) on parallel offset lines
    def _beam2(p0, p1, off=8.0):
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        n = math.hypot(dx, dy)
        px, py = -dy / n * off / 2, dx / n * off / 2
        o.append(_arrow(p0[0] + px, p0[1] + py, p1[0] + px, p1[1] + py, sw=1.2, color="#c0392b"))
        o.append(_arrow(p1[0] - px, p1[1] - py, p0[0] - px, p0[1] - py, sw=1.2, color="#2f6f9f"))

    _beam2((185.0, 146.0), MU)
    _beam2((185.0, 156.0), ML)

    # ---- detector
    o.append(_arrow(179, 168, 179, 238, sw=1.1, color="#2f6f9f"))
    o.append(_rect(152, 238, 54, 22, FILL))
    o.append(_txt(179, 253, "bộ tách sóng", 6.6))
    o.append(_txt(179, 276, "(giao thoa)", 6.4, color=GREY))

    # ---- annotation panel
    o.append('<rect x="404" y="98" width="238" height="126" rx="4" fill="#fbfcfd" stroke="#d8dee5" '
             'stroke-width="0.8"/>')
    o.append(_txt(418, 120, "chùm tia đi và về hai lần qua cách tử", 7, anchor="start", color=INK))
    o.append(_txt(418, 148, "cách tử dịch một bước P", 7, anchor="start", color=INK))
    o.append(_txt(418, 164, "→ thu được bốn chu kỳ vân", 7, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(418, 194, "2 P sin ψ = λ", 9, anchor="start", color=INK, weight="600"))
    o.append(_txt(418, 210, "ψ: góc nhiễu xạ của chùm tia", 6.6, anchor="start", color=GREY))

    return _fig(svg(660, 290, "".join(o), "Bộ mã hoá thẳng dùng cách tử hologram của Sony"),
                "Hình 6-79 · Nguyên lý làm việc của bộ mã hoá thẳng dùng cách tử hologram. Chùm sáng kết hợp của laser "
                "bán dẫn bị bộ chia chùm tách làm hai, mỗi chùm đọc cách tử tại một vị trí riêng. Hai chùm bị cách tử "
                "nhiễu xạ, phản xạ trên gương rồi đi qua cách tử lần thứ hai, cuối cùng được hợp lại ở bộ tách sóng để "
                "tạo vân giao thoa. Vì hai chùm bị nhiễu xạ theo hai chiều ngược nhau và đều đi qua cách tử hai lần, "
                "nên khi cách tử dịch đúng một bước P thì thu được bốn chu kỳ tín hiệu. Về lý thuyết, để cường độ "
                "chùm phản xạ qua cách tử hologram đạt cực đại, hiệu quang trình giữa hai gương phẳng liên tiếp phải "
                "bằng λ, tức 2P sin ψ = λ.",
                "Figure 6.79 · Principle of the hologram-grating linear encoder. The coherent beam of a semiconductor "
                "laser is split in two by the beam splitter, and each beam interrogates the grating at a separate "
                "location. Both beams are diffracted by the grating, reflected at the mirrors, pass through the "
                "grating a second time, and are finally recombined at the photodetector to produce interference "
                "fringes. Because the two beams are diffracted in opposite directions and each passes twice through "
                "the grating, a displacement of one pitch P yields four signal cycles. For maximum intensity of the "
                "reflected beam, the path difference between successive plane mirrors must equal λ, that is "
                "2P sin ψ = λ.",
                "Bộ mã hoá thẳng dùng cách tử hologram",
                "Hologram-grating linear encoder")


# ---------------------------------------------------------------- 6.9
def fig_6_80():
    o = [_defs()]
    x0, y0, W, Hh = 96, 62, 320, 168
    o.append(_arrow(x0, y0 + Hh, x0 + W + 30, y0 + Hh, sw=1))
    o.append(_arrow(x0, y0 + Hh, x0, y0 - 22, sw=1))
    o.append(_txt(x0 + W + 26, y0 + Hh + 16, "đại lượng vào", 7.5, anchor="end", color=GREY))
    o.append(_txt(x0 + 6, y0 - 26, "đại lượng ra", 7.5, anchor="start", color=GREY))

    def f(u):
        return 0.5 + 0.5 * math.tanh(4.0 * (u - 0.5))

    h = 0.075
    up, dn = [], []
    for i in range(161):
        u = i / 160.0
        up.append("%s %s" % (_f(x0 + u * W), _f(y0 + Hh - f(u - h) * Hh)))
        dn.append("%s %s" % (_f(x0 + u * W), _f(y0 + Hh - f(u + h) * Hh)))
    o.append('<polyline points="%s" fill="none" stroke="#c0392b" stroke-width="1.6"/>' % " ".join(up))
    o.append('<polyline points="%s" fill="none" stroke="#2f6f9f" stroke-width="1.6"/>' % " ".join(dn))

    # direction arrows on each branch
    o.append(_arrow(x0 + 0.30 * W, y0 + Hh - f(0.30 - h) * Hh,
                    x0 + 0.42 * W, y0 + Hh - f(0.42 - h) * Hh, sw=1.1, color="#c0392b"))
    o.append(_arrow(x0 + 0.70 * W, y0 + Hh - f(0.70 + h) * Hh,
                    x0 + 0.58 * W, y0 + Hh - f(0.58 + h) * Hh, sw=1.1, color="#2f6f9f"))

    # hysteresis gap at mid-scale
    xm = x0 + 0.5 * W
    ya = y0 + Hh - f(0.5 - h) * Hh
    yb = y0 + Hh - f(0.5 + h) * Hh
    o.append(_line(xm, ya, xm, yb, sw=1, color=INK, dash="3 3"))
    o.append(_line(xm - 8, ya, xm + 8, ya, sw=1, color=INK))
    o.append(_line(xm - 8, yb, xm + 8, yb, sw=1, color=INK))
    o.append(_txt(xm + 12, (ya + yb) / 2.0 + 3, "độ trễ", 7.5, anchor="start", color=INK))
    o.append(_txt(x0 + 0.20 * W, y0 + Hh - f(0.20 - h) * Hh + 20, "chiều tăng", 7, color="#c0392b"))
    o.append(_txt(x0 + 0.80 * W, y0 + Hh - f(0.80 + h) * Hh - 12, "chiều giảm", 7, color="#2f6f9f"))
    return _fig(svg(660, 268, "".join(o), "Đường cong trễ của cảm biến dịch chuyển"),
                "Hình 6-80 · Độ trễ: quan hệ đầu ra–đầu vào. Đường cong đi lên và đường cong đi xuống không trùng "
                "nhau, nên tại cùng một giá trị đầu vào ta đọc được hai giá trị đầu ra khác nhau tuỳ theo chiều đi "
                "tới. Khoảng cách giữa hai nhánh tại một điểm chính là độ trễ — đại lượng thường được tính bằng phần "
                "trăm của toàn dải đo.",
                "Figure 6.80 · Hysteresis: output versus input. The upscale and downscale curves do not coincide, so "
                "the same input yields two different outputs depending on the direction of approach. The separation "
                "of the two branches at a given input is the hysteresis, usually quoted as a percentage of full "
                "scale.",
                "Đường cong trễ",
                "Hysteresis curve")


def fig_6_81():
    o = [_defs()]
    x0, y0, W, Hh = 110, 52, 300, 180
    cx, cy = x0 + W / 2.0, y0 + Hh / 2.0
    o.append(_arrow(x0 - 40, cy, x0 + W + 44, cy, sw=1))
    o.append(_arrow(cx, y0 + Hh + 34, cx, y0 - 30, sw=1))
    o.append(_txt(x0 + W + 40, cy + 16, "H", 9, anchor="end", weight="600"))
    o.append(_txt(cx + 12, y0 - 32, "B", 9, weight="600"))

    def hx(hv):
        return cx + hv / 3.0 * (W / 2.0)

    def by(bv):
        return cy - bv * (Hh / 2.0) / 1.06

    asc = ["%s %s" % (_f(hx(-3 + 6 * i / 160.0)), _f(by(math.tanh((-3 + 6 * i / 160.0) + 1.0))))
           for i in range(161)]
    dsc = ["%s %s" % (_f(hx(3 - 6 * i / 160.0)), _f(by(math.tanh((3 - 6 * i / 160.0) - 1.0))))
           for i in range(161)]
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(asc), INK))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(dsc), INK))

    # remanence and coercivity markers
    br = math.tanh(1.0)
    o.append(_line(cx, by(br), cx + 30, by(br), sw=0.8, color=GOLD, dash="3 3"))
    o.append(_line(cx, by(-br), cx + 30, by(-br), sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(cx + 34, by(br) + 3, "B<sub>r</sub>", 7.5, anchor="start", color=GOLD, weight="600"))
    o.append(_line(hx(1), cy, hx(1), cy + 26, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_line(hx(-1), cy, hx(-1), cy + 26, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(hx(1) + 4, cy + 34, "H<sub>c</sub>", 7.5, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(hx(-1) - 4, cy + 34, "–H<sub>c</sub>", 7.5, anchor="end", color=GOLD, weight="600"))
    o.append(_txt(hx(2.4), by(1.0) - 6, "B<sub>s</sub>", 7.5, color=GREY))
    o.append(_txt(hx(-2.4), by(-1.0) + 12, "–B<sub>s</sub>", 7.5, color=GREY))
    o.append(_txt(292, 276, "diện tích vòng = tổn hao trễ mỗi chu kỳ", 7, color=GREY, anchor="start"))
    return _fig(svg(660, 288, "".join(o), "Vòng trễ từ"),
                "Hình 6-81 · Độ trễ từ. Khi đặt một vật liệu sắt từ vào một từ trường xoay chiều, cảm ứng từ B chậm "
                "pha so với lực từ hoá H đã sinh ra nó, tạo thành một vòng kín. Diện tích dưới vòng trễ là tổn hao "
                "trễ trên mỗi chu kỳ: lớn với nam châm vĩnh cửu, nhỏ với vật liệu từ có độ từ thẩm cao và tổn hao "
                "thấp. B<sub>r</sub> là cảm ứng từ dư, H<sub>c</sub> là lực kháng từ, B<sub>s</sub> là cảm ứng từ bão "
                "hoà.",
                "Figure 6.81 · Magnetic hysteresis. When a ferromagnetic material is placed in an alternating field, "
                "the flux density B lags behind the magnetising force H that causes it, tracing a closed loop. The "
                "area under the loop is the hysteresis loss per cycle: high for permanent magnets, low for "
                "high-permeability low-loss magnetic materials. B<sub>r</sub> is the remanence, H<sub>c</sub> the "
                "coercivity and B<sub>s</sub> the saturation flux density.",
                "Vòng trễ từ",
                "Magnetic hysteresis loop")


def fig_6_82():
    o = [_defs()]
    # electronics head
    o.append(_rect(24, 92, 78, 56, "#fbfcfd"))
    o.append(_txt(63, 114, "đầu điện tử", 7.2))
    o.append(_txt(63, 130, "(xử lý thời gian)", 6.4, color=GREY))
    # waveguide
    o.append(_rect(102, 114, 486, 13, "#f6e6c8"))
    o.append(_rect(102, 114, 486, 13, "none", sw=1.1))
    o.append(_txt(300, 146, "ống dẫn sóng (dây sắt từ)", 7.2, color=GREY))
    # pickup coil inside the head
    for k in range(4):
        o.append(_line(112 + k * 7, 110, 112 + k * 7, 131, sw=1, color="#2f6f9f"))
    o.append(_txt(126, 100, "bộ thu", 6.8, color="#2f6f9f"))
    # damping element
    o.append(_rect(560, 108, 28, 25, "url(#h6)", sw=1))
    o.append(_txt(574, 152, "giảm chấn", 6.8, color=GREY))
    o.append(_txt(574, 164, "vùng chết", 6.4, color=GREY))
    # position magnet straddling the tube
    mx = 380
    o.append(_rect(mx - 16, 96, 32, 12, "#c0392b", sw=0.9))
    o.append(_rect(mx - 16, 133, 32, 12, "#c0392b", sw=0.9))
    o.append(_txt(mx, 92, "N", 7, color="#fff", weight="600"))
    o.append(_txt(mx, 143, "S", 7, color="#fff", weight="600"))
    # moving member
    o.append(_rect(mx - 40, 40, 80, 18, "#eef2f6"))
    o.append(_txt(mx, 53, "đối tượng cần đo", 6.6))
    o.append(_line(mx, 58, mx, 96, sw=1.2))
    o.append(_txt(mx + 46, 82, "nam châm vị trí", 7, anchor="start", color="#c0392b"))
    o.append(_line(mx + 44, 80, mx + 16, 90, sw=0.7, color="#c0392b"))
    # measuring span
    o.append(_arrow(150, 182, mx, 182, sw=0.9, color=GREY))
    o.append(_arrow(mx, 182, 150, 182, sw=0.9, color=GREY))
    o.append(_txt((150 + mx) / 2.0, 196, "khoảng cách đo được", 7, color=GREY))
    return _fig(svg(660, 214, "".join(o), "Cảm biến dịch chuyển từ giảo với nam châm vị trí"),
                "Hình 6-82 · Cảm biến từ giảo dùng một phần tử sắt từ để phát hiện vị trí của một nam châm vị trí dịch "
                "dọc theo chiều dài của nó. Nam châm vị trí gắn vào chi tiết cần đo, còn thân cảm biến đứng yên. Nam "
                "châm di chuyển dọc vùng đo mà không tiếp xúc với phần tử cảm biến — đó là ưu điểm quyết định của "
                "loại cảm biến này.",
                "Figure 6.82 · A magnetostrictive sensor uses a ferromagnetic element to detect the position of a "
                "position magnet displaced along its length. The position magnet is attached to the member whose "
                "position is to be sensed while the sensor body stays stationary. The magnet travels along the "
                "measuring area without touching the sensing element — the decisive advantage of this sensor type.",
                "Cảm biến từ giảo",
                "Magnetostrictive sensor")


def fig_6_83():
    o = [_defs()]
    rnd = [(0.3, 0.9), (2.2, 0.4), (1.1, 2.4), (2.7, 1.7), (0.8, 1.5),
           (1.9, 0.9), (0.2, 2.1), (2.4, 2.6), (1.5, 1.1), (2.9, 0.6)]
    for panel, (bx, title, aligned) in enumerate(((40, "(a) chưa từ hoá", False),
                                                  (350, "(b) đã từ hoá theo H", True))):
        bw, bh = (250, 110) if panel == 0 else (268, 110)
        o.append(_rect(bx, 52, bw, bh, "#fdfdfd"))
        for i in range(10):
            cxx = bx + 32 + (i % 5) * 46
            cyy = 52 + 32 + (i // 5) * 50
            ang = 0.0 if aligned else rnd[i][0]
            if aligned:
                ang = 0.0
            dx, dy = 15 * math.cos(ang), 15 * math.sin(ang)
            o.append(_arrow(cxx - dx, cyy - dy, cxx + dx, cyy + dy, sw=1.1, color="#2f6f9f"))
        o.append(_txt(bx + bw / 2.0, 42, title, 7.6, weight="600"))
    # field arrow on the magnetised panel
    o.append(_txt(165, 180, "chiều dài ban đầu", 6.8, color=GREY))
    o.append(_txt(475, 180, "chiều dài tăng ΔL", 6.8, color="#c0392b"))
    o.append(_arrow(350, 198, 618, 198, sw=1.4, color="#c0392b"))
    o.append(_txt(484, 214, "H", 9, color="#c0392b", weight="600"))
    return _fig(svg(660, 224, "".join(o), "Đô men từ và sự thay đổi kích thước"),
                "Hình 6-83 · Đô men từ: sự sắp xếp theo từ trường H gây ra thay đổi kích thước. (a) Khi vật liệu chưa "
                "bị từ hoá, các đô men định hướng ngẫu nhiên. (b) Khi bị từ hoá, các đô men quay trục của chúng gần "
                "song song với nhau và theo phương của H; mạng tinh thể biến dạng, làm chiều dài theo phương ấy tăng "
                "lên một lượng ΔL. Hiệu ứng này có thể được tối ưu bằng cách điều khiển trật tự đô men qua chọn hợp "
                "kim, ủ nhiệt, biến dạng nguội và cường độ từ trường.",
                "Figure 6.83 · Magnetic domains: alignment with the field H causes dimensional change. (a) In an "
                "unmagnetised material the domains are randomly oriented. (b) When the material is magnetised the "
                "domains rotate so that their axes lie roughly parallel to each other and to H; the crystal lattice "
                "strains and the length along that direction grows by ΔL. The effect can be optimised by controlling "
                "the domain order through alloy selection, thermal annealing, cold working and field strength.",
                "Đô men từ",
                "Magnetic domains")


def fig_6_84():
    o = [_defs()]
    # waveguide
    o.append(_rect(90, 62, 500, 12, "#f6e6c8"))
    o.append(_rect(90, 62, 500, 12, "none", sw=1))
    o.append(_rect(24, 46, 66, 44, "#fbfcfd"))
    o.append(_txt(57, 72, "đầu điện tử", 6.8))
    o.append(_txt(57, 100, "phát xung I", 6.6, color="#2f6f9f"))
    o.append(_arrow(57, 96, 57, 82, sw=0.9, color="#2f6f9f"))
    # magnet
    mx = 400
    o.append(_rect(mx - 12, 48, 24, 10, "#c0392b", sw=0.8))
    o.append(_rect(mx - 12, 78, 24, 10, "#c0392b", sw=0.8))
    o.append(_txt(mx, 36, "nam châm vị trí", 6.8, color="#c0392b"))
    # torsion waves
    o.append(_arrow(mx - 18, 68, 150, 68, sw=1.4, color=GOLD))
    o.append(_arrow(mx + 18, 68, 574, 68, sw=1.4, color=GREY))
    o.append(_txt(250, 58, "sóng xoắn về phía bộ thu", 6.8, color=GOLD))
    o.append(_txt(500, 58, "sóng bị giảm chấn", 6.8, anchor="middle", color=GREY))
    # damping
    o.append(_rect(574, 58, 16, 20, "url(#h6)", sw=0.9))
    # time axis
    ty = 168
    o.append(_arrow(90, ty, 610, ty, sw=1))
    o.append(_txt(614, ty + 4, "t", 8, anchor="start", color=GREY))
    # launch pulse
    o.append('<polyline points="%s" fill="none" stroke="#2f6f9f" stroke-width="1.5"/>'
             % " ".join(["90 %s" % _f(ty), "110 %s" % _f(ty), "110 %s" % _f(ty - 26),
                         "124 %s" % _f(ty - 26), "124 %s" % _f(ty)]))
    o.append(_txt(107, ty - 32, "xung dò I", 6.8, color="#2f6f9f"))
    # echo pulse at proportional position
    px = 90 + (mx - 90)
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (" ".join(["%s %s" % (_f(px), _f(ty)), "%s %s" % (_f(px + 12), _f(ty)),
                          "%s %s" % (_f(px + 12), _f(ty - 26)), "%s %s" % (_f(px + 26), _f(ty - 26)),
                          "%s %s" % (_f(px + 26), _f(ty))]), GOLD))
    o.append(_txt(px + 30, ty - 32, "xung thu được", 6.8, anchor="start", color=GOLD))
    # interval
    o.append(_arrow(124, ty - 46, px + 12, ty - 46, sw=0.9, color=INK))
    o.append(_arrow(px + 12, ty - 46, 124, ty - 46, sw=0.9, color=INK))
    o.append(_txt((124 + px + 12) / 2.0, ty - 52, "t", 8.5, weight="600"))
    o.append(_txt(330, 202, "x = v · t,   v ≈ 3000 m·s⁻¹", 9, color=INK, weight="600"))
    return _fig(svg(660, 218, "".join(o), "Nguyên lý hoạt động của cảm biến vị trí từ giảo"),
                "Hình 6-84 · Nguyên lý hoạt động của cảm biến vị trí từ giảo. Một xung dòng I (xung dò, dài 1–2 µs) "
                "được đưa vào ống dẫn sóng, tạo tức thời một từ trường bao quanh nó trên toàn chiều dài. Tại vị trí "
                "nam châm, hiệu ứng Wiedemann sinh ra một sóng xoắn cơ học lan theo hai chiều. Phần sóng đi về phía "
                "bộ thu được phát hiện khi tới nơi; khoảng thời gian từ lúc phát xung dòng tới lúc thu được sóng "
                "chính là vị trí của nam châm. Phần sóng đi ngược lại bị phần tử giảm chấn hấp thụ ở cuối ống để "
                "không phản xạ trở lại thành nhiễu.",
                "Figure 6.84 · Operation of a magnetostrictive position sensor. A current pulse I — the interrogation "
                "pulse, 1–2 µs long — is applied to the waveguide and instantly surrounds it with a magnetic field "
                "along its whole length. At the position magnet the Wiedemann effect launches a torsional mechanical "
                "wave in both directions. The portion travelling toward the pickup is detected when it arrives; the "
                "time from the current pulse to that detection is the position of the magnet. The portion travelling "
                "the other way is absorbed by a damping element at the far end so that it cannot reflect back as "
                "interference.",
                "Cảm biến từ giảo — nguyên lý",
                "Magnetostrictive sensor principle")


def fig_6_85():
    o = [_defs()]
    # (a) field perpendicular to the current
    o.append(_txt(120, 34, "(a) B vuông góc với dòng", 7.6, weight="600"))
    o.append(_rect(46, 52, 150, 44, "#dce9f5"))
    o.append(_arrow(20, 74, 44, 74, sw=1.2, color="#c0392b"))
    o.append(_arrow(198, 74, 222, 74, sw=1.2, color="#c0392b"))
    o.append(_txt(18, 62, "I", 8, color="#c0392b", weight="600"))
    for k in range(3):
        o.append(_txt(86 + k * 35, 80, "×", 13, color="#2f6f9f"))
    o.append(_txt(120, 114, "B (vào trang) → R giảm", 7, color="#2f6f9f"))
    # (b) field parallel to the current
    o.append(_txt(430, 34, "(b) B song song với dòng", 7.6, weight="600"))
    o.append(_rect(356, 52, 150, 44, "#dce9f5"))
    o.append(_arrow(330, 74, 354, 74, sw=1.2, color="#c0392b"))
    o.append(_arrow(508, 74, 532, 74, sw=1.2, color="#c0392b"))
    o.append(_txt(328, 62, "I", 8, color="#c0392b", weight="600"))
    for k in range(3):
        o.append(_arrow(382 + k * 44, 82, 410 + k * 44, 82, sw=1, color="#2f6f9f"))
    o.append(_txt(430, 114, "B song song → R tăng", 7, color="#2f6f9f"))
    # (c) R vs B
    x0, y0, W, Hh = 90, 156, 300, 92
    o.append(_arrow(x0, y0 + Hh, x0 + W + 26, y0 + Hh, sw=1))
    o.append(_arrow(x0, y0 + Hh, x0, y0 - 12, sw=1))
    o.append(_txt(x0 + W + 22, y0 + Hh + 16, "B", 8, anchor="end", color=GREY))
    o.append(_txt(x0 + 8, y0 - 16, "R", 8, color=GREY))
    pts = []
    for i in range(81):
        b = 4.0 * i / 80.0
        r = 1.0 - 0.30 * math.tanh(b / 1.6)
        pts.append("%s %s" % (_f(x0 + b / 4.0 * W), _f(y0 + Hh - (r - 0.66) / 0.36 * Hh)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), INK))
    o.append(_txt(x0 + W * 0.42, y0 + 26, "bão hoà từ", 6.8, color=GREY))
    o.append(_txt(330, 272, "R(B) giảm khoảng 1% ở nhiệt độ phòng (0,3% với sắt, 2% với niken)",
                  7, color=GREY))
    return _fig(svg(660, 288, "".join(o), "Hiệu ứng từ điện trở"),
                "Hình 6-85 · Từ điện trở. Trong hầu hết vật liệu từ, điện trở giảm khi có từ trường tác dụng và "
                "hướng từ hoá vuông góc với dòng điện (a); mức giảm khoảng 1% ở nhiệt độ phòng — 0,3% với sắt và 2% "
                "với niken. Khi từ trường song song với dòng điện (b), điện trở lại tăng theo cường độ từ trường. "
                "Độ nhạy lớn nhất khi từ trường vuông góc với dòng. Đường cong (c) cho thấy điện trở giảm dần theo "
                "cảm ứng từ cho tới khi vật liệu bão hoà, và tốc độ giảm chậm dần khi tới gần bão hoà.",
                "Figure 6.85 · Magnetoresistance. In most magnetic materials the electrical resistance falls when a "
                "magnetic field is applied with the magnetisation perpendicular to the current flow (a); the change "
                "is of order 1% at room temperature — 0.3% in iron, 2% in nickel. When the field is parallel to the "
                "current (b) the resistance rises with field strength instead. Sensitivity is greatest for a field "
                "perpendicular to the current. Curve (c) shows the resistance falling with flux density until the "
                "material saturates, with the rate of fall decreasing as saturation is approached.",
                "Từ điện trở",
                "Magnetoresistance")


def fig_6_86():
    o = [_defs()]
    o.append(_rect(150, 66, 220, 96, "#dce9f5"))
    o.append(_arrow(96, 114, 148, 114, sw=1.3, color="#c0392b"))
    o.append(_arrow(372, 114, 416, 114, sw=1.3, color="#c0392b"))
    o.append(_txt(104, 104, "I", 9, color="#c0392b", weight="600"))
    o.append(_txt(404, 104, "I", 9, color="#c0392b", weight="600"))
    for k in range(3):
        for j in range(2):
            o.append(_txt(196 + k * 66, 100 + j * 32, "×", 12, color="#2f6f9f"))
    o.append(_txt(260, 186, "B hướng vào trang", 7.4, color="#2f6f9f"))
    # carrier deflection
    for k in range(4):
        x = 180 + k * 42
        o.append(_arrow(x, 130, x + 8, 76, sw=0.9, color=GOLD))
    o.append(_txt(150, 58, "điện tích bị đẩy lệch", 6.8, anchor="start", color=GOLD))
    # Hall voltage measured between the two faces
    o.append('<polyline points="370 66 468 66 490 102" fill="none" stroke="%s" stroke-width="1"/>' % INK)
    o.append('<polyline points="370 162 468 162 490 126" fill="none" stroke="%s" stroke-width="1"/>' % INK)
    o.append('<circle cx="504" cy="114" r="15" fill="#fff" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(504, 118, "V", 9, weight="600"))
    o.append(_txt(376, 58, "+", 9, color="#c0392b", weight="600"))
    o.append(_txt(376, 178, "–", 9, color="#2f6f9f", weight="600"))
    o.append(_txt(330, 212, "V<sub>H</sub> = K<sub>H</sub> · β · I / z", 9.2, color=INK, weight="600"))
    o.append(_txt(330, 228, "z: bề dày tấm dẫn", 7, color=GREY))
    return _fig(svg(660, 240, "".join(o), "Hiệu ứng Hall"),
                "Hình 6-86 · Hiệu ứng Hall. Khi một từ trường tác dụng vuông góc với dòng điện, xuất hiện một hiệu "
                "điện thế V<sub>H</sub> — gọi là điện áp Hall — trên hai mặt bên của vật dẫn. Chiều của nó vuông góc "
                "với cả từ trường lẫn dòng điện, độ lớn tỉ lệ với cả cảm ứng từ β và dòng I. Từ trường làm sinh ra "
                "gradien nồng độ hạt tải trên bề rộng vật dẫn; số hạt tải ở một bên nhiều hơn bên kia chính là "
                "nguyên nhân của hiệu điện thế ấy. Hằng số Hall K<sub>H</sub> càng lớn thì đầu ra càng lớn, điều này "
                "đòi hỏi độ linh động hạt tải cao.",
                "Figure 6.86 · The Hall effect. When a magnetic field is applied at right angles to the current, a "
                "potential V<sub>H</sub> — the Hall voltage — appears across the conductor. Its direction is "
                "perpendicular to both the field and the current, and its magnitude is proportional to both the flux "
                "density β and the current I. The field produces a gradient of carrier concentration across the "
                "conductor; the larger number of carriers on one side than on the other is what creates the "
                "potential. A large Hall constant K<sub>H</sub> gives the largest output, which requires high carrier "
                "mobility.",
                "Hiệu ứng Hall",
                "Hall effect")


def fig_6_87():
    o = [_defs()]
    # two magnets, both N poles facing the sensor
    o.append(_rect(58, 52, 34, 76, "#c0392b", sw=0.9))
    o.append(_txt(75, 96, "N", 10, color="#fff", weight="600"))
    o.append(_rect(288, 52, 34, 76, "#c0392b", sw=0.9))
    o.append(_txt(305, 96, "N", 10, color="#fff", weight="600"))
    # field arrows converging
    for dy in (-22, 0, 22):
        o.append(_arrow(96, 90 + dy, 176, 90 + dy * 0.45, sw=0.9, color="#2f6f9f"))
        o.append(_arrow(284, 90 + dy, 204, 90 + dy * 0.45, sw=0.9, color="#2f6f9f"))
    # hall sensor
    o.append(_rect(182, 76, 18, 28, "#f6e6c8", sw=1))
    o.append(_txt(191, 122, "cảm biến Hall", 6.8, color=GREY))
    o.append(_txt(191, 46, "từ trường triệt tiêu khi ở chính giữa", 7, color=INK))
    # output curve
    x0, y0, W, Hh = 80, 188, 300, 70
    cx, cy = x0 + W / 2.0, y0 + Hh / 2.0
    o.append(_arrow(x0, cy, x0 + W + 26, cy, sw=1))
    o.append(_arrow(cx, y0 + Hh + 26, cx, y0 - 8, sw=1))
    o.append(_txt(x0 + W + 22, cy + 15, "vị trí", 7, anchor="end", color=GREY))
    o.append(_txt(cx + 8, y0 - 12, "B", 8, color=GREY))
    pts = []
    for i in range(81):
        u = -1 + 2.0 * i / 80.0
        v = -math.tanh(1.6 * u) / math.tanh(1.6)
        pts.append("%s %s" % (_f(cx + u * W / 2.0), _f(cy - v * Hh / 2.0)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), INK))
    o.append(_txt(cx, cy + 22, "0", 7.5, color=GOLD, weight="600"))
    return _fig(svg(660, 292, "".join(o), "Cảm biến Hall hai nam châm"),
                "Hình 6-87 · Hai nam châm bố trí với một cảm biến Hall cho từ trường gần bằng không khi cảm biến nằm "
                "chính giữa hai cực. Đường cong phía dưới cho thấy đầu ra biến thiên gần tuyến tính quanh điểm giữa "
                "và bão hoà về hai phía. Cấu hình một cảm biến Hall như thế có dải tuyến tính rất hẹp; muốn dải dài "
                "hơn phải dùng nhiều cảm biến Hall rải dọc một đế mang và giải mã xem cảm biến nào đang chịu ảnh "
                "hưởng của nam châm.",
                "Figure 6.87 · Two magnets arranged with one Hall sensor yield a near-zero field when the sensor is "
                "equidistant between the poles. The curve below shows the output varying almost linearly about the "
                "midpoint and saturating on either side. A single Hall device gives a very limited linear range; "
                "longer ranges need many Hall sensors spaced along a carrier substrate, with decoding of which "
                "sensors the magnet is affecting.",
                "Cảm biến Hall hai nam châm",
                "Two-magnet Hall sensor")


def fig_6_88():
    o = [_defs()]
    ox, W = 96, 420
    for k, (lab, col, base, off) in enumerate((("A", "#c0392b", 74, 0.0),
                                               ("B", "#2f6f9f", 132, 0.25))):
        pts = []
        n = 8
        step = W / float(n)
        for j in range(n):
            x0 = ox + off * step + j * step
            x1 = min(x0 + step, ox + W)
            if x0 >= ox + W:
                break
            yv = base - 20 if j % 2 == 0 else base
            pts += ["%s %s" % (_f(x0), _f(yv)), "%s %s" % (_f(x1), _f(yv))]
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.7"/>' % (" ".join(pts), col))
        o.append(_txt(ox - 14, base - 6, lab, 9, anchor="end", color=col, weight="600"))
    o.append(_line(ox, 156, ox + W, 156, sw=0.7, color=GREY))
    # sample at the rising edge of A
    ex = ox + 0.25 * W
    o.append(_line(ex, 44, ex, 156, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(ex + 6, 40, "A lên 0 → 1", 7, anchor="start", color=GOLD))
    o.append(_txt(ex + 6, 176, "B = 0 → chiều dương", 7, anchor="start", color="#c0392b"))
    ex2 = ox + 0.625 * W
    o.append(_line(ex2, 44, ex2, 156, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(ex2 + 6, 40, "A xuống 1 → 0", 7, anchor="start", color=GOLD))
    o.append(_txt(ex2 + 6, 192, "B = 1 → chiều âm", 7, anchor="start", color="#2f6f9f"))
    return _fig(svg(660, 208, "".join(o), "Đầu ra vuông pha của bộ mã hoá từ"),
                "Hình 6-88 · Đầu ra vuông pha. Hai kênh A và B lệch pha 90°, dạng xung vuông, sin hoặc tam giác. Số "
                "lần chuyển tiếp — số “xung đếm” — tỉ lệ với độ lớn dịch chuyển, còn chiều dịch chuyển được xác định "
                "bằng cách so sánh hai pha: tại thời điểm pha A chuyển từ 0 lên 1, trạng thái của pha B cho biết "
                "đang đi theo chiều nào. Chẳng hạn B = 0 ứng với chiều dương và B = 1 ứng với chiều âm.",
                "Figure 6.88 · Quadrature output. The two channels A and B are 90° apart, in square, sinusoidal or "
                "triangular form. The number of transitions — the count — is proportional to the magnitude of the "
                "displacement, while the direction is found by comparing the two phases: at the instant phase A goes "
                "from 0 to 1, the state of phase B tells the direction of travel. A logic 0 on B might mean the "
                "positive direction and a logic 1 the negative.",
                "Đầu ra vuông pha",
                "Quadrature output")


# ---------------------------------------------------------------- block helpers
def _box(x, y, w, h, label, fill="#eef3fb", sw=1.1, size=8):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="3" fill="%s" stroke="%s" stroke-width="%s"/>'
         % (_f(x), _f(y), _f(w), _f(h), fill, INK, sw)]
    if "\n" in label:
        parts = label.split("\n")
        yy = y + h / 2.0 + 3 - (len(parts) - 1) * 5.0
        tsp = "".join('<tspan x="%s" dy="%s">%s</tspan>'
                      % (_f(x + w / 2.0), "0" if i == 0 else "10", part)
                      for i, part in enumerate(parts))
        o.append('<text x="%s" y="%s" text-anchor="middle" style="font:%spx '
                 'Inter,Helvetica,sans-serif;fill:#111">%s</text>' % (_f(x + w / 2.0), _f(yy), size, tsp))
    else:
        o.append(_txt(x + w / 2.0, y + h / 2.0 + 3, label, size))
    return "".join(o)


def _node(x, y, label, fill="#eef3fb", r=14):
    o = ['<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.1"/>'
         % (_f(x), _f(y), _f(r), fill, INK)]
    o.append(_txt(x, y + 3, label, 8))
    return "".join(o)


# ---------------------------------------------------------------- 6.10
def fig_6_89():
    o = [_defs()]
    # (a) cross-section of an induction potentiometer
    cx, cy = 156, 120
    o.append(_txt(156, 28, "(a) tiết diện", 9, weight="600"))
    o.append('<circle cx="%s" cy="%s" r="84" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    # stator iron ring
    o.append(_ring(cx, cy, 58, 84))
    # two slots top and bottom
    for ang in (90, 270):
        a = math.radians(ang)
        x1 = cx + 60 * math.cos(a); y1 = cy + 60 * math.sin(a)
        x2 = cx + 82 * math.cos(a); y2 = cy + 82 * math.sin(a)
        o.append(_line(x1, y1, x2, y2, sw=5, color="#ffffff"))
    # stator pole coils (left and right), drawn as little racetracks
    for px in (cx - 71, cx + 71):
        o.append('<rect x="%s" y="%s" width="16" height="34" rx="8" fill="#cfe0ef" stroke="%s" stroke-width="1"/>'
                 % (_f(px - 8), _f(cy - 17), INK))
        for k in range(3):
            o.append(_line(px - 6 + k * 6, cy - 14, px - 6 + k * 6, cy + 14, sw=0.7, color=GREY))
    # rotor
    o.append('<circle cx="%s" cy="%s" r="50" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    # rotor winding lobes (top and bottom) show the rotor carries a winding
    for ry in (cy - 38, cy + 38):
        o.append('<rect x="%s" y="%s" width="30" height="14" rx="7" fill="#f4c9b0" stroke="%s" stroke-width="1"/>'
                 % (_f(cx - 15), _f(ry - 7), INK))
    o.append('<circle cx="%s" cy="%s" r="6" fill="#e8e8e8" stroke="%s" stroke-width="1"/>' % (_f(cx), _f(cy), INK))
    o.append(_txt(20, 120, "dây quấn stato", 6.6, anchor="start", color=GREY))
    o.append(_txt(cx, cy + 64, "dây quấn roto", 6.6, color=GREY))

    # (b) output vs angle
    x0, y0, W, H = 410, 60, 222, 140
    o.append(_txt(521, 28, "(b) đầu ra theo góc", 9, weight="600"))
    o.append(_arrow(x0, y0 + H, x0 + W + 22, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1))
    o.append(_txt(x0 + W + 18, y0 + H + 14, "θ", 8, anchor="end", color=GREY))
    o.append(_txt(x0 + 6, y0 - 16, "V", 8, color=GREY))
    # gridlines at ±60 and ±75 degrees
    def X(th):
        return x0 + (th + 90.0) / 180.0 * W
    pts_r = []; pts_i = []
    for th in range(-90, 91, 3):
        u = math.radians(th)
        vr = math.sin(u)
        vi = min(1.6, 1.45 * math.sin(u))
        pts_r.append("%s %s" % (_f(X(th)), _f(y0 + H - (vr + 1.6) / 3.2 * H)))
        pts_i.append("%s %s" % (_f(X(th)), _f(y0 + H - (vi + 1.6) / 3.2 * H)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts_r), GREY))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts_i), GOLD))
    o.append(_txt(X(-90), y0 + H + 22, "-90°", 6.6, color=GREY))
    o.append(_txt(X(0), y0 + H + 22, "0°", 6.6, color=GREY))
    o.append(_txt(X(90), y0 + H + 22, "90°", 6.6, color=GREY))
    o.append(_txt(X(-60), y0 + 6, "±60°", 6.4, color=GREY))
    o.append(_txt(X(75), y0 + 6, "±75°", 6.4, color=GOLD))
    o.append(_txt(x0 + 6, y0 + 14, "kiểu pot", 7, color=GOLD))
    o.append(_txt(x0 + 6, y0 + 28, "RVDT", 7, color=GREY))
    return _fig(svg(660, 250, "".join(o), "Cảm ứng kiểu pot"),
                "Hình 6-89 · Cảm biến kiểu pot cảm ứng. Đặt thêm dây quấn lên roto (a) làm tăng đầu ra (thêm vôn trên "
                "mỗi độ), cải thiện tỉ số tín hiệu/nhiễu và cho phép một dải góc hơi rộng hơn so với RVDT (b). Nhược "
                "điểm là thêm dây quấn, cần không gian lớn hơn, chênh lệch theo nhiệt độ lớn hơn và độ lệch pha lớn "
                "hơn.",
                "Figure 6.89 · The induction potentiometer places windings on the rotor as well as the stator (a), "
                "which boosts the output (more volts per degree), improves signal-to-noise and gives a slightly wider "
                "angular range than an RVDT (b). The penalties are extra windings, more space, greater temperature "
                "variation and a larger phase shift.",
                "Cảm ứng kiểu pot",
                "Induction potentiometer")


def fig_6_90():
    o = [_defs()]
    # (a) 16-slot stator lamination
    cx, cy = 150, 130
    o.append(_txt(150, 26, "(a) 16 khe stato", 8.6, weight="600"))
    o.append('<circle cx="%s" cy="%s" r="92" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    o.append(_ring(cx, cy, 64, 86))
    # 16 slots
    for k in range(16):
        a = math.radians(k * 22.5)
        x1 = cx + 64 * math.cos(a); y1 = cy + 64 * math.sin(a)
        x2 = cx + 86 * math.cos(a); y2 = cy + 86 * math.sin(a)
        o.append(_line(x1, y1, x2, y2, sw=4.5, color="#ffffff"))
    o.append('<circle cx="%s" cy="%s" r="50" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    o.append(_txt(cx, cy + 4, "roto", 7.5, color=GREY))

    # (b) distributed winding: turns per slot follow a sine
    x0, yb, W, H = 360, 172, 268, 62
    n = 16
    o.append(_txt(494, 26, "(b) phân bố từ thông ∝ sin", 8.6, weight="600"))
    o.append(_line(x0, yb, x0 + W, yb, sw=1))
    env = []
    for k in range(n + 1):
        th = k * 2 * math.pi / n
        env.append((x0 + k * W / float(n), yb - math.sin(th) * H))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>'
             % (" ".join("%s %s" % (_f(px), _f(py)) for px, py in env), GOLD))
    bw = W / float(n)
    for k in range(n):
        th = k * 2 * math.pi / n
        t = math.sin(th) * H
        bx = x0 + k * bw + 2
        if t >= 0:
            o.append(_rect(bx, yb - t, bw - 4, t, fill="#cfe0ef"))
        else:
            o.append(_rect(bx, yb, bw - 4, -t, fill="#cfe0ef"))
    o.append(_txt(x0 + 4, yb - H - 8, "số vòng dây", 7, color=GREY))
    o.append(_txt(x0 + W, yb + H + 14, "khe 1→16", 7, anchor="end", color=GREY))
    return _fig(svg(660, 250, "".join(o), "Stato 16 khe"),
                "Hình 6-90 · Stato cảm biến kiểu resolver dùng tấm thép xếp 16 khe. Khi dây quấn được phân bố thành "
                "những cuộn đồng tâm nằm trong từng phần tư của lõi (b), số vòng dây trên mỗi khe tuân theo một bao "
                "sin, nhờ đó đầu ra tiệm cận một sóng sin (trên một cuộn thứ cấp) và một sóng cosin (trên cuộn kia).",
                "Figure 6.90 · The resolver stator uses a 16-slot lamination. When the windings are distributed as "
                "concentric coils in each quadrant of the stack (b), the number of turns per slot follows a sine "
                "envelope, so the output is a close approximation to a sine on one secondary winding and a cosine on "
                "the other.",
                "Stato 16 khe của bộ resolver",
                "Resolver 16-slot stator")


def fig_6_91():
    o = [_defs()]
    cx, cy = 170, 120
    o.append(_txt(170, 28, "(a) mặt cắt ngang", 8.6, weight="600"))
    o.append('<circle cx="%s" cy="%s" r="86" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    o.append(_ring(cx, cy, 56, 86))
    # stator winding pair S1-S3 (horizontal) and S2-S4 (vertical)
    for (ax, ay, lab) in ((1, 0, "S1–S3"), (0, 1, "S2–S4")):
        px = cx + 71 * ax; py = cy + 71 * ay
        o.append('<rect x="%s" y="%s" width="16" height="34" rx="8" fill="#cfe0ef" stroke="%s" stroke-width="1"/>'
                 % (_f(px - 8 - (16 if ax else 0)), _f(py - 17 - (0 if ay else 0)), INK))
    # rotor winding R1-R3
    o.append('<circle cx="%s" cy="%s" r="48" fill="#fdfdfd" stroke="%s" stroke-width="1.1"/>' % (_f(cx), _f(cy), INK))
    o.append('<rect x="%s" y="%s" width="30" height="14" rx="7" fill="#f4c9b0" stroke="%s" stroke-width="1"/>'
             % (_f(cx - 15), _f(cy - 7), INK))
    o.append(_txt(cx, 148, "R1–R3 (roto)", 7, color=GREY))
    o.append(_txt(222, 96, "S1–S3", 6.6, color=GREY))
    o.append(_txt(cx, 218, "S2–S4", 6.6, color=GREY))

    # (b) brushless rotary transformer + lead legend
    o.append(_txt(500, 28, "(b) biến áp quay không chổi than", 8.6, weight="600"))
    bx, by = 470, 84
    o.append('<circle cx="%s" cy="%s" r="46" fill="#e9e3d6" stroke="%s" stroke-width="1.2"/>'
             % (_f(bx), _f(by), INK))
    o.append('<circle cx="%s" cy="%s" r="28" fill="#fdfdfd" stroke="%s" stroke-width="1.2"/>'
             % (_f(bx), _f(by), INK))
    o.append(_txt(bx, by + 4, "T", 8, color=GREY))
    rows = [("R1 (đỏ/trắng)", "#c0392b"), ("R3 (vàng/trắng)", "#c9a227"),
            ("S1 (đỏ)", "#c0392b"), ("S3 (đen)", "#333"), ("S2 (vàng)", "#c9a227"), ("S4 (xanh)", "#2f6f9f")]
    yy = 156
    for lab, col in rows:
        o.append('<rect x="%s" y="%s" width="14" height="9" fill="%s"/>' % (452, _f(yy), col))
        o.append(_txt(472, yy + 8, lab, 7.4, anchor="start", color=INK))
        yy += 16
    return _fig(svg(660, 262, "".join(o), "Bộ resolver không chổi than"),
                "Hình 6-91 · Bộ resolver không chổi than điều biến điện áp kích thích trên roto theo góc quay. Cuộn "
                "sơ cấp R1–R3 nằm trên roto, hai cặp cuộn thứ cấp S1–S3 và S2–S4 vuông góc nhau nằm trên stato (a). "
                "Sự ghép từ được thực hiện qua một biến áp quay, nên không cần chổi than (b); màu dây dẫn tuân theo "
                "quy ước của nhà sản xuất.",
                "Figure 6.91 · The brushless resolver amplitude-modulates the ac excitation on the rotor by the "
                "rotation angle. The primary R1–R3 winding is on the rotor, and the two secondary pairs S1–S3 and "
                "S2–S4 are at right angles on the stator (a). Coupling is by a rotary transformer, so no brushes are "
                "needed (b); the lead colours follow the manufacturer convention.",
                "Bộ resolver không chổi than",
                "Brushless resolver")


def fig_6_92():
    o = [_defs()]
    o.append(_txt(330, 26, "Roto R1–R3 được kích thích bằng điện áp định mức Eₓ", 8.4, weight="600"))
    # AC source
    o.append('<circle cx="58" cy="120" r="20" fill="#fdfdfd" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append('<path d="M46 120 q12 -16 24 0 q-12 16 -24 0" fill="none" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_txt(58, 158, "Eₓ", 8, weight="600"))
    # primary winding R1-R3 (rotor) as a coil
    o.append('<rect x="150" y="86" width="40" height="68" rx="6" fill="#f4c9b0" stroke="%s" stroke-width="1.1"/>' % INK)
    for k in range(4):
        o.append(_line(156 + k * 8, 92, 156 + k * 8, 148, sw=0.7, color=GREY))
    o.append(_txt(170, 78, "R1–R3 (roto)", 7.4, color=GREY))
    # transformer core linking
    o.append('<rect x="208" y="100" width="14" height="40" fill="#e9e3d6" stroke="%s" stroke-width="1"/>' % INK)
    # secondary S2-S4 (vertical pair) -> output sin theta
    o.append('<rect x="250" y="40" width="36" height="44" rx="6" fill="#cfe0ef" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(268, 66, "S2–S4", 6.6, color=GREY))
    # secondary S1-S3 (horizontal pair) -> output cos theta
    o.append('<rect x="250" y="156" width="36" height="44" rx="6" fill="#cfe0ef" stroke="%s" stroke-width="1.1"/>' % INK)
    o.append(_txt(268, 182, "S1–S3", 6.6, color=GREY))
    # wires
    o.append(_line(78, 120, 150, 120, sw=1))
    o.append(_arrow(150, 120, 190, 120, sw=1))
    o.append(_line(190, 120, 208, 120, sw=1))
    o.append(_line(222, 120, 250, 62, sw=1))
    o.append(_line(222, 120, 250, 178, sw=1))
    # output leads with sine symbols
    o.append(_line(286, 62, 420, 62, sw=1.1, color=GOLD))
    o.append(_line(286, 178, 420, 178, sw=1.1, color="#2f6f9f"))
    sx, sy, sw2 = 320, 62, 0
    pts = []
    for i in range(41):
        x = 300 + i * 3.2
        y = 62 - 14 * math.sin(i / 40.0 * 2 * math.pi)
        pts.append("%s %s" % (_f(x), _f(y)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), GOLD))
    pts = []
    for i in range(41):
        x = 300 + i * 3.2
        y = 178 - 14 * math.cos(i / 40.0 * 2 * math.pi)
        pts.append("%s %s" % (_f(x), _f(y)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), "#2f6f9f"))
    o.append(_txt(440, 66, "Eₓ sin θ", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_txt(440, 182, "Eₓ cos θ", 8, anchor="start", color="#2f6f9f", weight="600"))
    return _fig(svg(660, 240, "".join(o), "Kích thích cuộn roto"),
                "Hình 6-92 · Khi cuộn roto R1–R3 được kích thích bằng điện áp định mức Eₓ, biên độ đầu ra trên cuộn "
                "thứ cấp S2–S4 tỉ lệ với sin θ và trên cuộn S1–S3 tỉ lệ với cos θ. Đây là chế độ “bộ phát điều "
                "khiển”, được dùng với hầu hết bộ chuyển đổi resolver–số hiện đại.",
                "Figure 6.92 · When the rotor winding R1–R3 is excited with the rated voltage Eₓ, the output on the "
                "secondary S2–S4 is proportional to sin θ and the output on S1–S3 is proportional to cos θ. This is "
                "the “control transmitter” mode, used with most modern resolver-to-digital converters.",
                "Kích thích cuộn roto",
                "Rotor winding excited")


def fig_6_93():
    o = [_defs()]
    x0, y0, W, H, n = 70, 60, 520, 150, 360
    o.append(_arrow(x0, y0 + H, x0 + W + 22, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1))
    o.append(_txt(x0 + W + 18, y0 + H + 14, "θ (°)", 8, anchor="end", color=GREY))
    o.append(_txt(x0 + 6, y0 - 16, "V", 8, color=GREY))
    # baseline at 0
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.7, color=GREY))
    pts_s = []; pts_c = []
    for i in range(0, n + 1):
        th = i / float(n) * 2 * math.pi
        xs = x0 + i / float(n) * W
        ys = y0 + H / 2.0 - 0.42 * H * math.sin(th)
        yc = y0 + H / 2.0 - 0.42 * H * math.cos(th)
        pts_s.append("%s %s" % (_f(xs), _f(ys)))
        pts_c.append("%s %s" % (_f(xs), _f(yc)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts_s), GOLD))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts_c), "#2f6f9f"))
    # null markers
    for deg, col, lab in ((0, GOLD, "0°"), (180, GOLD, "180°"), (90, "#2f6f9f", "90°"), (270, "#2f6f9f", "270°")):
        x = x0 + deg / 360.0 * W
        o.append(_line(x, y0 + H / 2.0 - 3, x, y0 + H / 2.0 + 3, sw=1.2, color=col))
        o.append(_txt(x, y0 + H + 18, lab, 7, color=col))
    o.append(_txt(602, y0 + 40, "sin θ (S2–S4)", 7.2, anchor="end", color=GOLD))
    o.append(_txt(602, y0 + 54, "cos θ (S1–S3)", 7.2, anchor="end", color="#2f6f9f"))
    return _fig(svg(660, 248, "".join(o), "Đầu ra sin/cos"),
                "Hình 6-93 · Đầu ra của bộ resolver tốc độ đơn là sin θ trên một cuộn thứ cấp và cos θ trên cuộn kia. "
                "Các điểm triệt (null) xuất hiện trên S2–S4 ở 0° và 180°, và trên S1–S3 ở 90° và 270°. Vị trí roto tại "
                "đó điện áp ra cực tiểu được gọi là điện áp không (electrical zero).",
                "Figure 6.93 · The single-speed resolver output is sin θ on one secondary winding and cos θ on the "
                "other. Nulls occur on S2–S4 at 0° and 180°, and on S1–S3 at 90° and 270°. The rotor positions where "
                "the output is minimum define the electrical zero.",
                "Đầu ra sin/cos của bộ resolver",
                "Resolver sine/cosine output")


def fig_6_94():
    o = [_defs()]
    x0, y0, W, H, n = 60, 70, 540, 120, 360
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1))
    o.append(_txt(x0 + W + 12, y0 + H + 14, "t", 8, anchor="end", color=GREY))
    # reference and phase-shifted output (225 deg)
    ph = math.radians(225)
    pts_r = []; pts_o = []
    for i in range(0, n + 1):
        x = x0 + i / float(n) * W
        yr = y0 + H / 2.0 - 0.40 * H * math.sin(i / float(n) * 2 * math.pi)
        yo = y0 + H / 2.0 - 0.40 * H * math.sin(i / float(n) * 2 * math.pi + ph)
        pts_r.append("%s %s" % (_f(x), _f(yr)))
        pts_o.append("%s %s" % (_f(x), _f(yo)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts_r), INK))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts_o), GOLD))
    o.append(_txt(x0 + 4, y0 - 6, "vào (tham chiếu)", 7, anchor="start", color=INK))
    o.append(_txt(x0 + 70, y0 + H + 16, "ra (S1–S3)", 7, anchor="start", color=GOLD))
    # phase shift arrow between two zero crossings
    xa = x0; xb = x0 + ph / (2 * math.pi) * W
    o.append(_arrow(xa, y0 + H + 26, xb, y0 + H + 26, sw=1.1, color=GOLD))
    o.append(_txt((xa + xb) / 2.0, y0 + H + 38, "độ lệch pha 225°", 7.4, color=GOLD, weight="600"))
    # constant amplitude bracket
    o.append(_txt(x0 + W - 4, y0 - 6, "biên độ không đổi", 7, anchor="end", color=GREY))
    return _fig(svg(660, 232, "".join(o), "Tương tự pha"),
                "Hình 6-94 · Ở chế độ “bộ biến áp điều khiển”, khi S1–S3 được kích thích ở 0° và S2–S4 ở 90°, điện áp "
                "trên cuộn roto không đổi biên độ nhưng lệch pha so với điện áp tham chiếu một góc đúng bằng góc quay "
                "cơ khí (ví dụ 225°). Đo độ lệch thời gian giữa hai điểm đi qua zero cho ra góc vị trí.",
                "Figure 6.94 · In the “control transformer” mode, with S1–S3 excited at 0° and S2–S4 at 90°, the rotor "
                "voltage keeps a constant amplitude but shifts in phase from the reference by exactly the mechanical "
                "angle (here 225°). Measuring the time between the two zero crossings yields the angular position.",
                "Đầu ra tương tự pha",
                "Phase-analog output")


def fig_6_95():
    o = [_defs()]
    o.append(_txt(330, 24, "Nguyên nhân gây sai số trong resolver và synchro", 8.4, weight="600"))
    panels = [("1 lần/vòng", "(lệch tâm roto–stato)", 1, 40),
              ("2 lần/vòng", "(mép cực không tròn)", 2, 255),
              ("bậc cao", "(gợn răng khe)", 5, 470)]
    py, bw, bh = 44, 150, 88
    for lab, sub, m, px in panels:
        o.append(_rect(px, py, bw, bh, "#fdfdfd"))
        bx0 = px + 16
        bx1 = px + bw - 12
        byc = py + bh / 2.0
        o.append(_arrow(bx0 - 8, byc, bx1 + 6, byc, sw=0.8))
        o.append(_arrow(bx0, byc + 18, bx0, py + 8, sw=0.8))
        pts = []
        for j in range(0, 121):
            th = j / 120.0 * 2 * math.pi
            x = bx0 + j / 120.0 * (bx1 - bx0)
            y = byc - 26 * math.sin(m * th)
            pts.append("%s %s" % (_f(x), _f(y)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (" ".join(pts), INK))
        o.append(_txt(px + bw / 2.0, py + bh + 14, lab, 7.4, color=GREY))
        o.append(_txt(px + bw / 2.0, py + bh + 25, sub, 7.0, color=GREY))
    return _fig(svg(660, 172, "".join(o), "Sai số"),
                "Hình 6-95 · Các nguồn sai số trong resolver và synchro. Lệch tâm roto–stato sinh ra thành phần lỗi "
                "một lần mỗi vòng (trái); mép cực không tròn sinh ra thành phần hai lần mỗi vòng (giữa); gợn do răng "
                "khe (sóng hài bậc cao) sinh ra thành phần bậc cao (phải). Các lỗi này gây ra những điểm không rõ ràng "
                "và giới hạn độ phân giải thực tế.",
                "Figure 6.95 · Error sources in resolvers and synchros. Rotor–stator eccentricity produces a once-per-"
                "revolution error (left); non-circular pole faces produce a twice-per-rev error (centre); slot ripple "
                "(high-order harmonic) produces a high-order component (right). These errors create ambiguous output "
                "voltages and limit the practical resolution.",
                "Nguyên nhân sai số",
                "Error sources")


def fig_6_96():
    o = [_defs()]
    x0, y0, W, H, n = 70, 60, 520, 150, 360
    o.append(_arrow(x0, y0 + H, x0 + W + 22, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1))
    o.append(_txt(x0 + W - 6, y0 - 6, "θ (°)", 8, anchor="end", color=GREY))
    o.append(_txt(x0 + 6, y0 - 16, "V", 8, color=GREY))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.7, color=GREY))
    pts_1 = []; pts_2 = []
    for i in range(0, n + 1):
        th = i / float(n) * 2 * math.pi
        x = x0 + i / float(n) * W
        y1 = y0 + H / 2.0 - 0.42 * H * math.sin(th)
        y2 = y0 + H / 2.0 - 0.42 * H * math.sin(2 * th)
        pts_1.append("%s %s" % (_f(x), _f(y1)))
        pts_2.append("%s %s" % (_f(x), _f(y2)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (" ".join(pts_1), GREY))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2"/>' % (" ".join(pts_2), GOLD))
    for deg, lab in ((180, "180°"), (360, "360°")):
        x = x0 + deg / 360.0 * W
        o.append(_line(x, y0 + H / 2.0 - 3, x, y0 + H / 2.0 + 3, sw=1.2, color=GOLD))
        o.append(_txt(x, y0 + H + 18, lab, 7, color=GOLD))
    o.append(_txt(560, y0 + 40, "2×: 1 chu kỳ/180°", 7.2, anchor="end", color=GOLD))
    o.append(_txt(560, y0 + 54, "1×: 1 chu kỳ/360°", 7.2, anchor="end", color=GREY))
    return _fig(svg(660, 248, "".join(o), "Resolver đa tốc độ"),
                "Hình 6-96 · Bộ resolver đa tốc độ (2×, 3×, …) hoàn thành nhiều chu kỳ sin điện trong một vòng quay cơ "
                "khí. Ở tốc độ 2×, một chu kỳ đầy đủ xảy ra trong 180° thay vì 360°, nên độ phân giải tăng theo bội số "
                "tốc độ. Tăng số cặp cực trên roto và stato tạo ra bộ đa tốc độ.",
                "Figure 6.96 · A multispeed resolver (2×, 3×, …) completes several electrical sine cycles per "
                "mechanical revolution. At 2× a full cycle occurs in 180° instead of 360°, so the resolution rises by "
                "the speed factor. Multispeed units are made by increasing the pole pairs on rotor and stator.",
                "Bộ resolver đa tốc độ",
                "Multispeed resolver")


def fig_6_97():
    o = [_defs()]
    o.append(_txt(330, 22, "Mô hình servo vòng kín dùng bộ chuyển đổi resolver–số", 8.2, weight="600"))
    y = 110
    # command
    o.append(_box(30, y - 18, 78, 36, "Lệnh", fill="#fdeccf"))
    o.append(_arrow(108, y, 150, y, sw=1.1))
    # sum
    o.append(_node(168, y, "Σ"))
    o.append(_arrow(186, y, 226, y, sw=1.1))
    # error amp
    o.append(_box(226, y - 18, 78, 36, "Khuếch đại\nsai số"))
    o.append(_arrow(304, y, 344, y, sw=1.1))
    # drive + motor
    o.append(_box(344, y - 18, 78, 36, "Truyền động\nĐộng cơ"))
    o.append(_arrow(422, y, 462, y, sw=1.1))
    # load
    o.append(_box(462, y - 18, 70, 36, "Tải / Trục", fill="#e6f3e6"))
    # resolver on shaft (below load), output from its left edge
    o.append(_line(497, y + 18, 497, y + 52, sw=1))
    o.append(_box(458, y + 52, 80, 34, "Resolver", fill="#eef3fb"))
    o.append(_line(458, y + 69, 458, y + 102, sw=1))
    o.append(_box(408, y + 102, 100, 32, "Chuyển đổi R→S", fill="#eef3fb"))
    o.append(_arrow(408, y + 118, 200, y + 118, sw=1))
    o.append(_arrow(200, y + 118, 168, y + 36, sw=1))
    o.append(_txt(150, y + 132, "phản hồi vị trí", 6.8, color=GREY))
    # velocity output
    o.append(_line(538, y + 69, 560, y + 69, sw=1))
    o.append(_txt(564, y + 73, "vận tốc", 7, anchor="start", color=GREY))
    return _fig(svg(660, 232, "".join(o), "Servo vòng kín"),
                "Hình 6-97 · Trong một mô hình servo vòng kín điển hình, cảm biến vị trí (resolver gắn trên trục) "
                "liên tục cập nhật thông tin vị trí và vận tốc. Bộ chuyển đổi resolver–số xuất ra dữ liệu số dùng để "
                "so sánh với lệnh, và đầu ra vận tốc còn được dùng để ổn định vòng lặp. Độ chính xác hệ thống bị giới "
                "hạn bởi độ phân giải nhỏ nhất của cảm biến vị trí.",
                "Figure 6.97 · In a typical closed-loop servo model, the position sensor (a resolver on the shaft) "
                "constantly updates position and velocity information. The resolver-to-digital converter provides "
                "digital data for comparison with the command, and a velocity output that helps stabilise the loop. "
                "System accuracy is bounded by the smallest resolution of the position-sensing device.",
                "Mô hình servo vòng kín",
                "Closed-loop servo")


def fig_6_98():
    o = [_defs()]
    o.append(_txt(330, 22, "Xử lý sai số dùng bộ chuyển đổi R→S dạng Type II", 8.2, weight="600"))
    # inputs
    o.append(_box(24, 40, 72, 32, "sin θ", fill="#fdeccf"))
    o.append(_box(24, 236, 72, 32, "cos θ", fill="#fdeccf"))
    # quadrant selector
    o.append(_box(120, 118, 96, 36, "Bộ chọn\ngóc phần tư", fill="#eef3fb"))
    o.append(_arrow(96, 56, 132, 122, sw=1))
    o.append(_arrow(96, 252, 132, 152, sw=1))
    # sine / cosine multipliers
    o.append(_box(236, 80, 96, 34, "× sin φ", fill="#eef3fb"))
    o.append(_box(236, 176, 96, 34, "× cos φ", fill="#eef3fb"))
    o.append(_arrow(216, 136, 236, 97, sw=1))
    o.append(_arrow(216, 136, 236, 193, sw=1))
    # subtractor
    o.append(_box(356, 120, 84, 36, "Số trừ", fill="#eef3fb"))
    o.append(_arrow(332, 97, 356, 126, sw=1))
    o.append(_arrow(332, 193, 356, 150, sw=1))
    o.append(_txt(450, 110, "sin(θ−φ)", 7.4, color=GREY))
    # demodulator
    o.append(_box(460, 120, 84, 36, "Bộ tách sóng", fill="#eef3fb"))
    o.append(_arrow(440, 138, 460, 138, sw=1))
    # integrator + VCO
    o.append(_box(566, 80, 80, 34, "Tích phân", fill="#eef3fb"))
    o.append(_box(566, 176, 80, 34, "VCO", fill="#eef3fb"))
    o.append(_arrow(544, 138, 566, 97, sw=1))
    o.append(_arrow(606, 114, 606, 176, sw=1))
    # up/down counter
    o.append(_box(440, 254, 100, 34, "Bộ đếm ↑/↓ (φ)", fill="#eef3fb"))
    o.append(_arrow(606, 210, 606, 273, sw=1))
    o.append(_arrow(606, 273, 540, 273, sw=1))
    # feedback phi into the two multipliers (dashed)
    o.append(_arrow(440, 273, 440, 210, sw=1, dash="4 3"))
    o.append(_arrow(440, 210, 284, 210, sw=1, dash="4 3"))
    o.append(_arrow(440, 210, 440, 114, sw=1, dash="4 3"))
    o.append(_arrow(440, 114, 284, 114, sw=1, dash="4 3"))
    o.append(_txt(452, 162, "φ", 8, color=GOLD, weight="600"))
    # notes
    o.append(_txt(360, 176, "e: sai số xoay chiều", 6.6, color=GREY))
    o.append(_txt(360, 104, "D: sai số một chiều", 6.6, color=GREY))
    o.append(_txt(492, 240, "U: chiều đếm", 6.6, color=GREY))
    return _fig(svg(660, 300, "".join(o), "Bộ chuyển đổi R→S Type II"),
                "Hình 6-98 · Xử lý sai số dùng bộ chuyển đổi resolver–số dạng Type II. sin θ và cos θ được đưa qua bộ "
                "chọn góc phần tư, rồi vào hai bộ nhân số với góc φ lưu trong bộ đếm. Hiệu của hai tích bằng sin(θ − "
                "φ). Sau khi tách sóng được điện áp một chiều tỉ lệ với sin(θ − φ), mạch tích phân + VCO + bộ đếm lên/"
                "xuống tạo thành một vòng lặp servomechanism kín hai tích phân, luôn nỗ lực triệt tiêu sai số. Đầu ra "
                "còn cho một điện áp vận tốc tỉ lệ với tốc độ góc.",
                "Figure 6.98 · Error processing in a Type II tracking resolver-to-digital converter. sin θ and cos θ "
                "pass through a quadrant selector and then two multipliers driven by the angle φ stored in the "
                "counter. Their difference is sin(θ − φ). After demodulation to a dc level proportional to sin(θ − φ), "
                "an integrator plus VCO plus up/down counter form a closed two-integrator servoloop that continually "
                "nulls the error. The output also provides a velocity voltage proportional to the angular rate.",
                "Bộ chuyển đổi resolver–số Type II",
                "Type II resolver-to-digital converter")


# ---------------------------------------------------------------- 6.11
def _fiber(x1, x2, y, label="", col=INK, sw=1.4):
    """A simple fibre drawn as two parallel lines."""
    return (_line(x1, y - 4, x2, y - 4, sw=sw, color=col)
            + _line(x1, y + 4, x2, y + 4, sw=sw, color=col))


def fig_6_99():
    o = [_defs()]
    # laser
    o.append(_box(24, 74, 62, 26, "laser diode", fill="#fdeccf", size=7.4))
    # fused coupler
    o.append(_rect(108, 78, 58, 56, "#fdfdfd"))
    o.append(_line(112, 82, 162, 130, sw=1.2))
    o.append(_line(112, 130, 162, 82, sw=1.2))
    o.append(_line(86, 87, 112, 87, sw=1.2))
    o.append(_txt(137, 148, "bộ ghép thuôn", 6.6, color=GREY))
    # sensor arm
    o.append(_line(166, 87, 300, 87, sw=1.2))
    # hollow-core tube
    o.append(_line(300, 79, 420, 79, sw=1.2))
    o.append(_line(300, 95, 420, 95, sw=1.2))
    o.append(_line(300, 79, 300, 95, sw=1.2))
    o.append(_line(420, 79, 420, 95, sw=1.2))
    # input fibre end and reflecting fibre
    o.append(_fiber(176, 330, 87))
    o.append(_fiber(352, 470, 87, col=GOLD))
    # cavity
    o.append(_line(330, 100, 330, 120, sw=0.8, color=GREY))
    o.append(_line(352, 100, 352, 120, sw=0.8, color=GREY))
    o.append(_arrow(330, 112, 352, 112, sw=0.9, color=GREY))
    o.append(_arrow(352, 112, 330, 112, sw=0.9, color=GREY))
    o.append(_txt(341, 126, "d", 8, color=GREY, weight="600"))
    # reflections back toward the coupler
    o.append(_arrow(330, 68, 290, 68, sw=1, color="#2f6f9f"))
    o.append(_arrow(352, 60, 300, 60, sw=1, color=GOLD))
    o.append(_txt(276, 65, "R1", 7.4, anchor="end", color="#2f6f9f"))
    o.append(_txt(292, 57, "R2", 7.4, anchor="end", color=GOLD))
    o.append(_txt(300, 150, "sợi lõi rỗng", 6.6, color=GREY))
    o.append(_txt(176, 76, "sợi dẫn vào", 6.6, anchor="start", color=GREY))
    o.append(_txt(430, 76, "sợi phản xạ", 6.6, anchor="start", color=GREY))
    # detector
    o.append(_line(137, 134, 137, 168, sw=1.2))
    o.append(_rect(115, 168, 44, 28, "#e6f3e6"))
    o.append(_txt(137, 186, "đầu dò", 7.2))
    return _fig(svg(660, 212, "".join(o), "Cấu hình cảm biến EFPI"),
                "Hình 6-99 · Cấu hình đơn giản của hệ cảm biến giao thoa Fabry–Perot ngoại (EFPI). Laser diode đơn mode "
                "chiếu sáng khoang Fabry–Perot qua một bộ ghép sợi thuôn nóng chảy. Khoang được tạo giữa sợi đơn mode "
                "dẫn vào và sợi phản xạ, căn chỉnh bằng một đoạn sợi silica lõi rỗng. Phản xạ thứ nhất R1 là phản xạ "
                "tham chiếu, không phụ thuộc nhiễu động; phản xạ thứ hai R2 phụ thuộc chiều dài khoang d.",
                "Figure 6.99 · A simple configuration of an extrinsic Fabry–Perot interferometric (EFPI) sensing "
                "system. A single-mode laser diode illuminates the Fabry–Perot cavity through a fused biconical "
                "tapered coupler. The cavity is formed between an input single-mode fibre and a reflecting fibre, "
                "aligned by a hollow-core silica fibre. The first reflection R1 is the reference and is independent "
                "of the perturbation; the second reflection R2 depends on the cavity length d.",
                "Cấu hình cảm biến EFPI",
                "EFPI sensing system")


def fig_6_100():
    o = [_defs()]
    x0, y0, W, H = 80, 50, 460, 140
    o.append(_arrow(x0, y0 + H, x0 + W + 24, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 14, sw=1))
    o.append(_txt(x0 + W + 20, y0 + H + 16, "d (đơn vị λ)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 + 8, y0 - 16, "I / I₀", 8, color=GREY))
    pts = []
    n = 360
    for i in range(n + 1):
        d = 3.0 * i / n
        I = math.cos(4 * math.pi * d) ** 2
        pts.append("%s %s" % (_f(x0 + d / 3.0 * W), _f(y0 + H - I * H)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), INK))
    # Q point: where I = I0/2 and the slope is greatest (d = lambda/16)
    dq = 0.0625
    xq = x0 + dq / 3.0 * W
    o.append(_line(xq, y0 + H, xq, y0 + H / 2.0, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(xq - 6, y0 + H / 2.0 - 8, "điểm Q", 7.4, anchor="end", color=GOLD, weight="600"))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.6, color=GREY, dash="2 3"))
    # one fringe = lambda/2
    xa = x0 + 1.0 / 3.0 * W
    xb = x0 + 1.5 / 3.0 * W
    o.append(_arrow(xa, y0 + H + 10, xb, y0 + H + 10, sw=0.9, color="#2f6f9f"))
    o.append(_txt((xa + xb) / 2.0, y0 + H + 24, "một vân = λ/2", 7, color="#2f6f9f"))
    return _fig(svg(660, 236, "".join(o), "Hàm truyền EFPI"),
                "Hình 6-100 · Đường cong hàm truyền điển hình của EFPI. Cường độ I tại đầu dò biến thiên theo "
                "I = I₀ cos²(4πd/λ) với chiều dài khoang d. Những nhiễu động nhỏ quanh điểm làm việc tĩnh (điểm Q) "
                "cho một biến thiên tuyến tính của cường độ đầu ra. Mỗi vân ứng với một thay đổi chiều dài khoang "
                "bằng nửa bước sóng làm việc.",
                "Figure 6.100 · A typical EFPI transfer function. The intensity I at the detector varies as "
                "I = I₀ cos²(4πd/λ) with the cavity length d. Small perturbations around the quiescent operating "
                "point (the Q-point) give a linear variation in output intensity. Each fringe corresponds to a change "
                "in cavity length of one half of the operating wavelength.",
                "Hàm truyền EFPI",
                "EFPI transfer function")


def fig_6_101():
    o = [_defs()]
    o.append(_box(22, 96, 74, 28, "laser diode", fill="#fdeccf", size=7.2))
    o.append(_txt(59, 140, "cách ly quang", 6.6, color=GREY))
    # 2x2 coupler
    o.append(_rect(126, 86, 60, 52, "#fdfdfd"))
    o.append(_line(130, 90, 182, 134, sw=1.2))
    o.append(_line(130, 134, 182, 90, sw=1.2))
    o.append(_line(96, 110, 126, 110, sw=1.2))
    # upper output leg to the sensing fibre
    o.append(_line(182, 94, 300, 94, sw=1.2))
    o.append(_fiber(300, 470, 94))
    # cavity inside the fibre: two Fresnel reflectors
    for xx in (360, 424):
        o.append(_line(xx, 88, xx, 100, sw=1.6, color=GOLD))
    o.append(_txt(392, 78, "khoang trong sợi", 6.6, color=GREY))
    o.append(_arrow(470, 116, 430, 116, sw=1, color=GOLD))
    o.append(_arrow(356, 116, 300, 116, sw=1, color="#2f6f9f"))
    o.append(_txt(300, 130, "R", 7.4, anchor="start", color="#2f6f9f"))
    o.append(_txt(470, 130, "S", 7.4, anchor="end", color=GOLD))
    # lower output leg to detector
    o.append(_line(156, 138, 156, 172, sw=1.2))
    o.append(_rect(130, 172, 52, 28, "#e6f3e6"))
    o.append(_txt(156, 190, "đầu dò", 7.2))
    return _fig(svg(660, 214, "".join(o), "Cảm biến IFPI"),
                "Hình 6-101 · Cảm biến giao thoa Fabry–Perot nội (IFPI). Laser diode đã cách ly quang đưa vào một "
                "nhánh của bộ ghép 2 × 2 hai chiều. Khoang Fabry–Perot được tạo bằng cách hàn nóng chảy một đoạn ngắn "
                "sợi đơn mode vào một trong các nhánh ra, hoặc bằng hai điểm phản xạ Fresnel — chỗ gián đoạn chiết "
                "suất — dọc theo sợi. Phản xạ tham chiếu R và phản xạ cảm biến S giao thoa tại mặt đầu dò, cho một "
                "biến thiên cường độ dạng sin.",
                "Figure 6.101 · An intrinsic Fabry–Perot interferometric (IFPI) sensor. An optically isolated laser "
                "diode feeds one input arm of a bidirectional 2 × 2 coupler. The Fabry–Perot cavity is formed by "
                "fusing a short length of single-mode fibre to one of the output legs, or by two Fresnel reflectors — "
                "refractive-index discontinuities — along the fibre. The reference reflection R and the sensing "
                "reflection S interfere at the detector face, giving a sinusoidal intensity variation.",
                "Cảm biến IFPI",
                "Intrinsic Fabry–Perot sensor")


def fig_6_102():
    o = [_defs()]
    o.append(_txt(330, 24, "Giản đồ β của cách tử Bragg sợi quang", 8.4, weight="600"))
    x0, y0, W, H = 110, 60, 380, 150
    o.append(_arrow(x0, y0 + H / 2.0, x0 + W + 20, y0 + H / 2.0, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 16, sw=1))
    o.append(_txt(x0 + W + 16, y0 + H / 2.0 + 15, "ω", 8, anchor="end", color=GREY))
    o.append(_txt(x0 + 8, y0 - 20, "β", 8, color=GREY))
    # forward branch +beta01 and reverse branch -beta01
    for sgn, lab in ((1, "β₀₁"), (-1, "−β₀₁")):
        pts = []
        for i in range(61):
            x = x0 + i / 60.0 * W
            v = 0.9 * math.tanh((i / 60.0 - 0.42) * 2.4)
            pts.append("%s %s" % (_f(x), _f(y0 + H / 2.0 - sgn * v * H / 2.0)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), INK))
        o.append(_txt(x0 + W + 6, y0 + H / 2.0 - sgn * 0.86 * H / 2.0 + 3, lab, 7.4,
                      anchor="start", color=GREY))
    # grating vector connecting the two branches at the Bragg wavelength
    xb = x0 + 0.62 * W
    ymid = y0 + H / 2.0
    o.append(_arrow(xb, ymid, xb, ymid - 0.72 * H / 2.0, sw=1.2, color=GOLD))
    o.append(_arrow(xb, ymid, xb, ymid + 0.72 * H / 2.0, sw=1.2, color=GOLD))
    o.append(_txt(xb + 6, ymid - 6, "2π/Λ", 8, anchor="start", color=GOLD, weight="600"))
    o.append(_line(xb, y0 + H, xb, y0 + H + 8, sw=0.8, color=GREY))
    o.append(_txt(xb, y0 + H + 20, "λ_B", 8, color=GREY))
    return _fig(svg(660, 240, "".join(o), "Giản đồ beta"),
                "Hình 6-102 · Cơ chế ghép mode trong cách tử Bragg sợi quang, biểu diễn trên giản đồ β. Cách tử nối "
                "mode cơ bản lan truyền thuận LP₀₁ với mode cơ bản lan truyền ngược. Vì hiệu các hằng số lan truyền "
                "Δβ giữa hai mode là lớn, chỉ cần một chu kỳ cách tử Λ nhỏ — cỡ 0,5 µm — để tạo ra ghép mode, và bước "
                "sóng Bragg tương ứng khoảng 1,5 µm.",
                "Figure 6.102 · The mode-coupling mechanism in a fibre Bragg grating, shown on a β-plot. The grating "
                "couples the forward-propagating fundamental LP₀₁ mode to the reverse-propagating fundamental mode. "
                "Because the difference in propagation constants Δβ between the two modes is large, only a small "
                "grating period Λ — of order 0.5 µm — is needed to induce the coupling, giving a Bragg wavelength "
                "near 1.5 µm.",
                "Giản đồ β của cách tử Bragg",
                "β-plot of a Bragg grating")


def fig_6_103():
    o = [_defs()]
    o.append(_txt(330, 24, "Phương pháp giao thoa", 8.4, weight="600"))
    # UV beam into the splitter
    o.append(_arrow(28, 120, 150, 120, sw=1.6, color="#7b3fa0"))
    o.append(_txt(28, 108, "chùm UV 244/248 nm", 7, anchor="start", color="#7b3fa0"))
    # beamsplitter at 45 degrees
    o.append(_line(132, 102, 168, 138, sw=2.2, color=INK))
    o.append(_txt(120, 96, "bộ tách chùm", 6.6, anchor="start", color=GREY))
    # reflected beam up to the top mirror, transmitted beam down to the bottom mirror
    o.append(_line(150, 120, 150, 56, sw=1.1, color="#7b3fa0"))
    o.append(_line(150, 120, 150, 184, sw=1.1, color="#7b3fa0"))
    # mirrors
    o.append(_line(136, 48, 176, 64, sw=2.6))
    o.append(_line(136, 192, 176, 176, sw=2.6))
    o.append(_txt(186, 46, "gương", 6.6, anchor="start", color=GREY))
    o.append(_txt(186, 198, "gương", 6.6, anchor="start", color=GREY))
    # the two beams converge on the fibre
    o.append(_line(168, 56, 372, 112, sw=1.1, color="#7b3fa0"))
    o.append(_line(168, 184, 372, 128, sw=1.1, color="#7b3fa0"))
    # cylindrical lenses in each arm
    o.append('<ellipse cx="320" cy="90" rx="6" ry="16" fill="#dce9f5" stroke="%s" stroke-width="1"/>' % INK)
    o.append('<ellipse cx="320" cy="150" rx="6" ry="16" fill="#dce9f5" stroke="%s" stroke-width="1"/>' % INK)
    o.append(_txt(320, 66, "thấu kính trụ", 6.4, color=GREY))
    # fibre
    o.append(_fiber(372, 630, 120, col=GOLD))
    o.append(_txt(500, 106, "sợi pha Ge (đã bóc vỏ)", 6.8, color=GREY))
    # interference region
    o.append(_line(392, 104, 392, 136, sw=1, color=GOLD, dash="3 2"))
    o.append(_line(430, 104, 430, 136, sw=1, color=GOLD, dash="3 2"))
    o.append(_txt(411, 150, "vùng giao thoa", 6.6, color=GOLD))
    return _fig(svg(660, 232, "".join(o), "Ghi cách tử bằng giao thoa"),
                "Hình 6-103 · Cách tử Bragg sợi quang ghi bằng phương pháp giao thoa. Một chùm UV ở 244 hoặc 248 nm "
                "được bộ tách chùm chia thành hai phần bằng nhau; hai chùm được hội tụ lên một đoạn sợi pha Ge (đã "
                "bóc lớp bảo vệ) bằng các thấu kính trụ. Chu kỳ của vân giao thoa — và do đó bước sóng Bragg — được "
                "thay đổi bằng cách thay đổi góc hợp nhau θ giữa hai chùm.",
                "Figure 6.103 · Writing a fibre Bragg grating by the interferometric method. A UV beam at 244 or "
                "248 nm is split into two equal parts by a beam splitter; the two beams are focused onto a section of "
                "Ge-doped fibre (with the protective coating removed) by cylindrical lenses. The periodicity of the "
                "resulting interference pattern — and hence the Bragg wavelength — is varied by altering the mutual "
                "angle θ between the beams.",
                "Ghi cách tử bằng giao thoa",
                "Interferometric grating writing")


def fig_6_104():
    o = [_defs()]
    o.append(_txt(330, 24, "Giao thoa kế dùng lăng kính vuông góc", 8.4, weight="600"))
    # right-angled prism: right angle bottom-left, hypotenuse top-right
    o.append('<path d="M150 60 L150 178 L330 178 Z" fill="#e8f0f8" stroke="%s" stroke-width="1.4"/>' % INK)
    o.append(_txt(196, 160, "lăng kính", 7.2, color=GREY))
    # incoming UV beam
    o.append(_arrow(30, 108, 150, 108, sw=1.6, color="#7b3fa0"))
    o.append(_txt(30, 96, "chùm UV", 7, anchor="start", color="#7b3fa0"))
    # short internal path: straight to the hypotenuse, then down and out
    o.append(_line(150, 108, 219, 108, sw=1.3, color="#7b3fa0"))
    o.append(_line(219, 108, 219, 178, sw=1.3, color="#7b3fa0"))
    # long internal path: down, across, then out
    o.append(_line(150, 108, 150, 140, sw=1.1, color="#7b3fa0", dash="0"))
    o.append(_line(150, 140, 282, 140, sw=1.1, color="#7b3fa0"))
    o.append(_line(282, 140, 282, 178, sw=1.1, color="#7b3fa0"))
    o.append(_txt(232, 100, "đường ngắn", 6.4, anchor="start", color=GREY))
    o.append(_txt(196, 132, "đường dài", 6.4, anchor="start", color=GREY))
    # beams leave the bottom face and reach the fibre
    o.append(_line(219, 178, 219, 196, sw=1.2, color="#7b3fa0"))
    o.append(_line(282, 178, 282, 196, sw=1.2, color="#7b3fa0"))
    # fibre below the prism
    o.append(_fiber(150, 590, 196, col=GOLD))
    o.append(_txt(520, 182, "sợi quang", 6.8, color=GREY))
    o.append(_line(210, 188, 210, 204, sw=1, color=GOLD, dash="3 2"))
    o.append(_line(291, 188, 291, 204, sw=1, color=GOLD, dash="3 2"))
    o.append(_txt(250, 216, "vân giao thoa", 6.6, color=GOLD))
    return _fig(svg(660, 232, "".join(o), "Giao thoa kế lăng kính"),
                "Hình 6-104 · Giao thoa kế cải tiến dùng lăng kính vuông góc. Hiệu quang trình giữa hai chùm UV giao "
                "thoa được tạo ra nhờ truyền qua lăng kính, thay vì nhờ hai gương rời. Kỹ thuật này ổn định về bản "
                "chất vì mọi rung động của lăng kính đều tác động như nhau lên cả hai chùm.",
                "Figure 6.104 · The improved interferometer using a right-angled prism. The path difference between "
                "the two interfering UV beams is produced by propagation through the prism rather than by two "
                "separate mirrors. The technique is inherently stable because any vibration of the prism perturbs "
                "both beams similarly.",
                "Giao thoa kế lăng kính",
                "Prism interferometer")


def fig_6_105():
    o = [_defs()]
    o.append(_txt(330, 24, "Phương pháp mặt nạ pha", 8.4, weight="600"))
    # UV beam down
    o.append(_arrow(180, 44, 180, 84, sw=1.6, color="#7b3fa0"))
    o.append(_txt(188, 52, "chùm UV", 7, anchor="start", color="#7b3fa0"))
    # phase mask
    o.append(_rect(120, 84, 120, 14, "#e9e3d6"))
    for k in range(9):
        o.append(_line(130 + k * 13, 86, 130 + k * 13, 96, sw=0.8, color=GREY))
    o.append(_txt(120, 78, "mặt nạ pha (cách tử nổi)", 6.6, anchor="start", color=GREY))
    # diffracted orders
    o.append(_arrow(180, 100, 180, 128, sw=1, color=GREY))
    o.append(_txt(186, 120, "bậc 0", 6.4, anchor="start", color=GREY))
    o.append(_arrow(180, 100, 236, 136, sw=1.2, color=GOLD))
    o.append(_arrow(180, 100, 124, 136, sw=1.2, color=GOLD))
    o.append(_txt(244, 132, "+1", 7, anchor="start", color=GOLD))
    o.append(_txt(116, 132, "−1", 7, anchor="end", color=GOLD))
    # rectangular prism with TIR at glass/air interface
    o.append(_rect(96, 136, 172, 44, "#e8f0f8"))
    o.append(_txt(182, 196, "lăng kính chữ nhật", 6.6, color=GREY))
    o.append(_line(124, 136, 156, 180, sw=1.2, color=GOLD))
    o.append(_line(236, 136, 204, 180, sw=1.2, color=GOLD))
    # fibre behind the mask
    o.append(_fiber(120, 500, 182, col=GOLD))
    o.append(_txt(360, 170, "sợi quang (sau mặt nạ)", 6.8, color=GREY))
    o.append(_line(176, 172, 176, 192, sw=1, color=GOLD, dash="3 2"))
    o.append(_line(206, 172, 206, 192, sw=1, color=GOLD, dash="3 2"))
    return _fig(svg(660, 220, "".join(o), "Phương pháp mặt nạ pha"),
                "Hình 6-105 · Phương pháp mặt nạ pha để chế tạo cách tử. Chùm UV tới bị nhiễu xạ thành các bậc −1, 0 "
                "và +1 bởi một cách tử nổi tạo trên bản silica bằng chiếu chùm điện tử và ăn mòn plasma. Hai bậc nhiễu "
                "xạ thứ nhất phản xạ toàn phần tại mặt phân cách thuỷ tinh/không khí của một lăng kính chữ nhật rồi "
                "giao thoa trên bề mặt sợi trần đặt ngay sau mặt nạ. Kỹ thuật này phụ thuộc bước sóng vì chu kỳ vân "
                "giao thoa được quyết định duy nhất bởi góc nhiễu xạ của hai bậc ±1.",
                "Figure 6.105 · The phase-mask technique for grating fabrication. The incident UV beam is diffracted "
                "into −1, 0 and +1 orders by a relief grating produced on a silica plate by e-beam exposure and "
                "plasma etching. The two first orders undergo total internal reflection at the glass/air interface of "
                "a rectangular prism and interfere on the bare fibre surface placed directly behind the mask. The "
                "technique is wavelength-specific, because the periodicity of the two-beam pattern is set uniquely by "
                "the diffraction angle of the ±1 orders.",
                "Phương pháp mặt nạ pha",
                "Phase-mask technique")


def fig_6_106():
    o = [_defs()]
    o.append(_txt(330, 24, "Theo dõi sự phát triển của cách tử trong khi ghi", 8.2, weight="600"))
    o.append(_box(26, 96, 84, 30, "nguồn quang rộng", fill="#fdeccf", size=7))
    o.append(_line(110, 111, 150, 111, sw=1.2))
    # coupler tap
    o.append(_rect(150, 92, 44, 38, "#fdfdfd"))
    o.append(_line(154, 96, 190, 126, sw=1.1))
    o.append(_line(154, 126, 190, 96, sw=1.1))
    o.append(_line(194, 111, 330, 111, sw=1.2))
    # grating in the fibre
    o.append(_fiber(330, 520, 111, col=GOLD))
    for k in range(10):
        o.append(_line(356 + k * 12, 105, 356 + k * 12, 117, sw=0.9, color=GOLD))
    o.append(_txt(416, 96, "cách tử đang ghi", 6.6, color=GOLD))
    o.append(_line(520, 111, 566, 111, sw=1.2))
    # analyser
    o.append(_box(566, 96, 70, 30, "máy phân tích phổ", fill="#e6f3e6", size=6.6))
    # tap to a power meter
    o.append(_line(172, 130, 172, 168, sw=1.1))
    o.append(_box(140, 168, 66, 26, "đo công suất", fill="#e6f3e6", size=6.6))
    return _fig(svg(660, 210, "".join(o), "Theo dõi cách tử"),
                "Hình 6-106 · Sơ đồ bố trí theo dõi sự phát triển của cách tử qua phổ truyền trong khi chế tạo. Ánh "
                "sáng từ một nguồn quang rộng đi qua cách tử đang được ghi; một nhánh ghép lấy ra một phần công suất "
                "để theo dõi mức truyền, còn phần chính được đưa tới máy phân tích phổ để quan sát đỉnh cách tử.",
                "Figure 6.106 · Diagram of the setup for monitoring the growth of the grating in transmission during "
                "fabrication. Light from a broadband source passes through the grating being written; a tapped arm "
                "takes a fraction of the power for a transmission monitor, while the main path feeds a spectrum "
                "analyser that watches the grating peak.",
                "Theo dõi sự phát triển của cách tử",
                "Monitoring grating growth")


def fig_6_107():
    o = [_defs()]
    o.append(_txt(330, 22, "So sánh giản đồ β của cách tử Bragg và cách tử chu kỳ dài", 8.2, weight="600"))
    for idx, (px, lab, dy, vec) in enumerate(((
            90, "(a) cách tử Bragg: Δβ lớn, Λ nhỏ", 0.78, "2π/Λ nhỏ"),
            (390, "(b) cách tử chu kỳ dài: Δβ nhỏ, Λ lớn", 0.20, "2π/Λ lớn"))):
        o.append(_txt(px + 90, 46, lab, 7.2, weight="600"))
        x0, y0, W, H = px, 64, 170, 120
        o.append(_arrow(x0, y0 + H / 2.0, x0 + W + 12, y0 + H / 2.0, sw=0.9))
        o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=0.9))
        o.append(_txt(x0 + W + 8, y0 + H / 2.0 + 13, "ω", 7, anchor="end", color=GREY))
        o.append(_txt(x0 + 6, y0 - 12, "β", 7, color=GREY))
        for sgn in (1, -1):
            pts = []
            for i in range(41):
                x = x0 + i / 40.0 * W
                v = 0.9 * math.tanh((i / 40.0 - 0.45) * 2.6)
                pts.append("%s %s" % (_f(x), _f(y0 + H / 2.0 - sgn * v * H / 2.0)))
            o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.3"/>' % (" ".join(pts), INK))
        xb = x0 + 0.60 * W
        ymid = y0 + H / 2.0
        o.append(_arrow(xb, ymid, xb, ymid - dy * H / 2.0, sw=1.2, color=GOLD))
        o.append(_arrow(xb, ymid, xb, ymid + dy * H / 2.0, sw=1.2, color=GOLD))
        o.append(_txt(xb + 8, ymid - 18, vec, 6.6, anchor="start", color=GOLD))
    return _fig(svg(660, 210, "".join(o), "So sánh giản đồ beta"),
                "Hình 6-107 · So sánh giản đồ β. (a) Trong cách tử Bragg, mode LP₀₁ thuận ghép với mode LP₀₁ ngược nên "
                "Δβ lớn và chu kỳ cách tử nhỏ, cỡ 1 µm. (b) Trong cách tử chu kỳ dài không nghiêng, biến thiên chiết "
                "suất song song với trục sợi khiến mode cơ bản ghép với các mode vỏ lan truyền thuận, có Δβ nhỏ hơn "
                "nhiều, nhờ đó chu kỳ cách tử lên tới hàng trăm micrômét.",
                "Figure 6.107 · Comparison of β-plots. (a) In a Bragg grating the forward LP₀₁ mode couples to the "
                "reverse LP₀₁ mode, so Δβ is large and the grating period is small — of order 1 µm. (b) In an "
                "unblazed long-period grating the index variation parallel to the fibre axis couples the fundamental "
                "mode to forward-propagating cladding modes, for which Δβ is far smaller, so the period runs to "
                "hundreds of micrometres.",
                "So sánh giản đồ β",
                "β-plot comparison")


def fig_6_108():
    o = [_defs()]
    o.append(_txt(330, 24, "Chế tạo cách tử chu kỳ dài", 8.4, weight="600"))
    o.append(_box(34, 44, 140, 34, "laser excimer KrF\n248 nm", fill="#fdeccf", size=6.8))
    o.append(_arrow(174, 61, 250, 61, sw=1.4, color="#7b3fa0"))
    o.append(_arrow(250, 63, 250, 96, sw=1.4, color="#7b3fa0"))
    o.append(_txt(256, 90, "chùm UV", 7, anchor="start", color="#7b3fa0"))
    # amplitude mask
    o.append(_rect(150, 96, 200, 14, "#e9e3d6"))
    for k in range(13):
        o.append(_rect(158 + k * 15, 98, 8, 10, "#ffffff"))
    o.append(_txt(150, 90, "mặt nạ biên độ (Cr)", 6.6, anchor="start", color=GREY))
    # fibre
    o.append(_fiber(120, 560, 126, col=GOLD))
    o.append(_txt(558, 114, "sợi germano-silicat nạp hydro", 6.6, anchor="end", color=GREY))
    # exposed length
    o.append(_line(240, 140, 240, 158, sw=0.8, color=GREY))
    o.append(_line(400, 140, 400, 158, sw=0.8, color=GREY))
    o.append(_arrow(240, 150, 400, 150, sw=0.9, color=GREY))
    o.append(_arrow(400, 150, 240, 150, sw=0.9, color=GREY))
    o.append(_txt(320, 166, "chiều dài chiếu 2,5 cm", 6.8, color=GREY))
    o.append(_txt(320, 190, "20 Hz · xung 8 ns · 100 mJ·cm⁻²·xung⁻¹ · 6–15 phút", 7, color=GREY))
    return _fig(svg(660, 208, "".join(o), "Chế tạo cách tử chu kỳ dài"),
                "Hình 6-108 · Sơ đồ chế tạo cách tử chu kỳ dài. Sợi germano-silicat nạp hydro (3,4 mol%) được chiếu "
                "xạ UV 248 nm từ laser excimer KrF qua một mặt nạ biên độ mạ crôm có hàm truyền chữ nhật tuần hoàn. "
                "Laser phát xung ở 20 Hz với độ dài xung 8 ns; thời gian ghi điển hình với năng lượng 100 mJ·cm⁻² mỗi "
                "xung và chiều dài chiếu 2,5 cm là từ 6 đến 15 phút tuỳ loại sợi.",
                "Figure 6.108 · Setup used to fabricate long-period gratings. Hydrogen-loaded (3.4 mol%) "
                "germanosilicate fibre is exposed to 248 nm UV radiation from a KrF excimer laser through a "
                "chrome-plated amplitude mask with a periodic rectangular transmittance function. The laser is pulsed "
                "at 20 Hz with an 8 ns pulse duration; typical writing times for 100 mJ·cm⁻² per pulse over a 2.5 cm "
                "exposed length are 6 to 15 minutes, depending on the fibre.",
                "Chế tạo cách tử chu kỳ dài",
                "Long-period grating fabrication")


def fig_6_109():
    o = [_defs()]
    x0, y0, W, H = 80, 54, 470, 140
    o.append(_arrow(x0, y0, x0 + W + 22, y0, sw=1))
    o.append(_arrow(x0, y0, x0, y0 + H + 14, sw=1))
    o.append(_txt(x0 + W + 18, y0 - 8, "λ (nm)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 - 8, y0 + 14, "T (dB)", 7.4, anchor="end", color=GREY))
    # transmission: 0 dB baseline with gaussian dips
    bands = [(1150, 4, 40), (1230, 11, 34), (1317, 18, 30), (1420, 9, 34), (1530, 6, 38), (1620, 4, 42)]
    def lam2x(l):
        return x0 + (l - 1100.0) / 600.0 * W
    pts = []
    for i in range(301):
        l = 1100 + 600.0 * i / 300.0
        t = 0.0
        for (lc, dep, wd) in bands:
            t += dep * math.exp(-((l - lc) / wd) ** 2)
        pts.append("%s %s" % (_f(lam2x(l)), _f(y0 + t / 20.0 * H)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (" ".join(pts), INK))
    for lc, dep, wd in bands:
        o.append(_line(lam2x(lc), y0, lam2x(lc), y0 + 5, sw=0.8, color=GREY))
        o.append(_txt(lam2x(lc), y0 - 12, str(lc), 6.4, color=GREY))
    o.append(_txt(lam2x(1317), y0 - 26, "băng tắt sâu nhất", 6.8, color=GOLD))
    o.append(_txt(x0, y0 + H + 24, "các băng suy hao ứng với ghép vào các mode vỏ bậc khác nhau",
                  6.8, anchor="start", color=GREY))
    return _fig(svg(660, 226, "".join(o), "Phổ truyền của cách tử chu kỳ dài"),
                "Hình 6-109 · Phổ truyền điển hình của một cách tử chu kỳ dài. Các băng suy hao khác nhau ứng với "
                "việc ghép vào những mode vỏ rời rạc có bậc khác nhau. Độ cách ly tối đa (mức mất mát cường độ "
                "truyền qua) điển hình trong khoảng 5 đến 20 dB, tuỳ tham số sợi, thời gian chiếu UV và chu kỳ mặt nạ.",
                "Figure 6.109 · Typical transmission of a long-period grating. The various attenuation bands "
                "correspond to coupling to discrete cladding modes of different orders. Maximum isolation — the loss "
                "in transmitted intensity — is typically in the 5 to 20 dB range, depending on the fibre parameters, "
                "the UV exposure time and the mask periodicity.",
                "Phổ truyền của cách tử chu kỳ dài",
                "Long-period grating transmission")


def fig_6_110():
    o = [_defs()]
    x0, y0, W, H = 96, 54, 430, 140
    o.append(_arrow(x0, y0 + H, x0 + W + 24, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 12, sw=1))
    o.append(_txt(x0 + W + 20, y0 + H + 16, "biến dạng ε (µε)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 + 8, y0 - 16, "Δλ (nm)", 8, color=GREY))
    # fibre D: 15.2 nm per 1% strain -> 0.00152 nm per microstrain
    # Bragg: 9 nm per 1% strain -> 0.0009 nm per microstrain
    for kd, col, lab, xoff in ((0.00152, GOLD, "sợi D: 15,2 nm/%ε", 0),
                               (0.00090, GREY, "cách tử Bragg: 9 nm/%ε", 0)):
        p0 = (x0, y0 + H)
        p1 = (x0 + W, y0 + H - kd * 1000.0 / 1.8 * H)
        o.append(_line(p0[0], p0[1], p1[0], p1[1], sw=1.8, color=col))
    o.append(_txt(x0 + W - 4, y0 + 46, "sợi D: 15,2 nm/%ε", 7, anchor="end", color=GOLD))
    o.append(_txt(x0 + W - 4, y0 + 102, "cách tử Bragg: 9 nm/%ε", 7, anchor="end", color=GREY))
    o.append(_txt(x0 + W / 2.0, y0 + H - 5, "độ nhạy biến dạng của sợi D lớn hơn 50%", 6.8,
                  color=INK))
    return _fig(svg(660, 226, "".join(o), "Độ nhạy biến dạng"),
                "Hình 6-110 · Độ dịch của bước sóng mất mát đỉnh theo biến dạng áp đặt, với sợi D và với một cách tử "
                "Bragg (khoảng 9 nm trên mỗi % biến dạng, ở 1300 nm). Hệ số của sợi D là 15,2 nm/%ε, tức độ dịch do "
                "biến dạng lớn hơn 50% so với cách tử Bragg thông thường; với độ phân giải bước sóng phát hiện được "
                "0,1 nm, độ phân giải biến dạng của sợi này là 65,75 µε.",
                "Figure 6.110 · Shift in peak loss wavelength as a function of the applied strain, for fibre D and "
                "for a Bragg grating (about 9 nm per % strain at 1300 nm). Fibre D has a coefficient of 15.2 nm/%ε, "
                "giving a strain-induced shift 50% larger than a conventional Bragg grating; with a detectable "
                "wavelength shift of 0.1 nm the strain resolution of this fibre is 65.75 µε.",
                "Độ nhạy biến dạng của cách tử chu kỳ dài",
                "Long-period grating strain sensitivity")


def fig_6_111():
    o = [_defs()]
    x0, y0, W, H = 84, 56, 460, 132
    o.append(_arrow(x0, y0, x0 + W + 22, y0, sw=1))
    o.append(_arrow(x0, y0, x0, y0 + H + 14, sw=1))
    o.append(_txt(x0 + W + 18, y0 - 8, "λ (nm)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 - 8, y0 + 14, "T (dB)", 7.4, anchor="end", color=GREY))
    def lam2x(l):
        return x0 + (l - 1260.0) / 120.0 * W
    # two dips: baseline and strained (shifted right)
    for shift, col, dash in ((0.0, INK, ""), (6.0, GOLD, "5 3")):
        pts = []
        for i in range(241):
            l = 1260 + 120.0 * i / 240.0
            t = 14 * math.exp(-((l - (1317 + shift)) / 14.0) ** 2)
            pts.append("%s %s" % (_f(lam2x(l)), _f(y0 + t / 16.0 * H)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"%s/>'
                 % (" ".join(pts), col, (' stroke-dasharray="%s"' % dash) if dash else ""))
    o.append(_line(lam2x(1317), y0 - 6, lam2x(1317), y0 + H, sw=0.9, color="#2f6f9f", dash="3 3"))
    o.append(_txt(lam2x(1317), y0 + H + 22, "1317 nm", 7, color="#2f6f9f"))
    o.append(_txt(lam2x(1266), y0 + 26, "chưa biến dạng", 7, anchor="start", color=INK))
    o.append(_txt(lam2x(1330), y0 + 26, "có biến dạng", 7, anchor="start", color=GOLD))
    # 1.6 dB arrow
    o.append(_arrow(lam2x(1305), y0 + 0.42 * H, lam2x(1305), y0 + 0.42 * H - 18, sw=1, color="#c0392b"))
    o.append(_txt(lam2x(1300), y0 + 0.42 * H + 14, "tăng 1,6 dB", 6.8, anchor="end", color="#c0392b"))
    return _fig(svg(660, 216, "".join(o), "Dịch phổ do biến dạng"),
                "Hình 6-111 · Độ dịch do biến dạng gây ra trong một cách tử ghi trên sợi C. Mức tăng mất mát tại "
                "1317 nm khoảng 1,6 dB. Một laser diode phát tại 1317 nm được dùng làm nguồn quang, và sự thay đổi "
                "cường độ truyền qua được theo dõi theo biến dạng áp đặt — nhờ đó chỉ cần một đầu dò và một bộ "
                "khuếch đại là đủ.",
                "Figure 6.111 · The shift induced by strain in a grating written in fibre C. The increase in loss at "
                "1317 nm is about 1.6 dB. A laser diode centred at 1317 nm is used as the optical source, and the "
                "change in transmitted intensity is monitored as a function of applied strain — so a simple detector "
                "and amplifier at the output suffice.",
                "Dịch phổ do biến dạng",
                "Strain-induced spectral shift")


def fig_6_112():
    o = [_defs()]
    x0, y0, W, H = 96, 54, 420, 140
    o.append(_arrow(x0, y0 + H, x0 + W + 24, y0 + H, sw=1))
    o.append(_arrow(x0, y0 + H, x0, y0 - 12, sw=1))
    o.append(_txt(x0 + W + 20, y0 + H + 16, "biến dạng ε (µε)", 7.4, anchor="end", color=GREY))
    o.append(_txt(x0 + 8, y0 - 16, "cường độ truyền qua", 7.4, color=GREY))
    trials = [(-0.62, 0.045, 0.0, "#2f6f9f"), (-0.66, 0.0, 1.6, GOLD),
              (-0.59, -0.045, -1.4, "#c0392b")]
    for slope, off, ph, col in trials:
        pts = []
        for i in range(41):
            e = 1000.0 * i / 40.0
            v = 0.86 + slope * e / 1000.0 + off
            sc = 0.010 * math.sin(i * 2.7 + ph * 3.1)
            pts.append("%s %s" % (_f(x0 + i / 40.0 * W), _f(y0 + H - (v + sc) * H)))
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (" ".join(pts), col))
    o.append(_txt(x0 + W - 6, y0 + 30, "ba lần thử", 7, anchor="end", color=GREY))
    return _fig(svg(660, 216, "".join(o), "Cường độ truyền qua theo biến dạng"),
                "Hình 6-112 · Đồ thị thay đổi cường độ truyền qua theo biến dạng, với ba lần thử khác nhau. Độ lặp "
                "lại của thí nghiệm chứng minh tính khả thi của việc dùng sơ đồ đơn giản này để khai thác độ nhạy "
                "cao của cách tử chu kỳ dài. Truyền qua của một laser diode đặt trên sườn phổ của cách tử, về một "
                "phía của bước sóng cộng hưởng, có thể dùng làm thước đo biến dạng áp đặt.",
                "Figure 6.112 · Plot of the change in transmitted intensity as a function of strain, for three "
                "different trials. The repeatability of the experiment demonstrates the feasibility of using this "
                "simple scheme to exploit the high sensitivity of long-period gratings. Transmission of a laser diode "
                "centred on the slope of the grating spectrum, on either side of the resonance wavelength, serves as "
                "a measure of the applied strain.",
                "Cường độ truyền qua theo biến dạng",
                "Transmitted intensity versus strain")


# ---------------------------------------------------------------- 6.12
def _axes(x0, y0, W, H, xlab, ylab):
    o = [_arrow(x0, y0 + H, x0 + W + 22, y0 + H, sw=1),
         _arrow(x0, y0 + H, x0, y0 - 12, sw=1),
         _txt(x0 + W + 18, y0 + H + 15, xlab, 7.4, anchor="end", color=GREY),
         _txt(x0 + 6, y0 - 14, ylab, 7.6, color=GREY)]
    return "".join(o)


def fig_6_113():
    o = [_defs()]
    o.append(_txt(330, 24, "Cấu hình cảm biến lệch chùm tia cơ bản", 8.4, weight="600"))
    # laser
    o.append(_box(28, 150, 74, 28, "laser", fill="#fdeccf", size=7.6))
    # incident beam down-right to the sample
    o.append(_arrow(102, 164, 250, 196, sw=1.6, color="#c0392b"))
    # sample surface
    o.append(_line(180, 206, 330, 206, sw=2.4))
    o.append(_txt(196, 222, "bề mặt mẫu", 7, anchor="start", color=GREY))
    # reflected beam to the PSD (undeflected, solid)
    o.append(_arrow(250, 196, 470, 78, sw=1.6, color="#c0392b"))
    # deflected surface and beam (dashed)
    o.append(_line(180, 194, 330, 194, sw=1.6, dash="5 3", color=GREY))
    o.append(_arrow(250, 184, 492, 66, sw=1.4, color="#7b3fa0"))
    o.append('<line x1="250" y1="196" x2="250" y2="184" stroke="%s" stroke-width="0.9"/>' % INK)
    o.append(_txt(238, 176, "u", 8, anchor="end", color=GREY, weight="600"))
    # PSD screen
    o.append('<line x1="486" y1="56" x2="512" y2="96" stroke="%s" stroke-width="3.2"/>' % INK)
    o.append(_txt(530, 58, "PSD", 8, anchor="start", weight="600"))
    o.append(_txt(486, 44, "P", 8, anchor="end", color="#c0392b", weight="600"))
    o.append(_txt(512, 44, "P′", 8, anchor="start", color="#7b3fa0", weight="600"))
    o.append(_txt(404, 156, "chùm phản xạ", 6.8, anchor="start", color=GREY))
    return _fig(svg(660, 240, "".join(o), "Cấu hình OBD"),
                "Hình 6-113 · Sơ đồ cấu hình cảm biến lệch chùm tia quang cơ bản. Dịch chuyển u của bề mặt làm vị trí "
                "của chùm phản xạ trên đầu dò vị trí (PSD) chuyển từ điểm P sang điểm P′; thay đổi vị trí này tạo ra "
                "một thay đổi điện áp đầu ra của PSD. Điện áp ra V của phần điện tử PSD có thể được hiệu chuẩn theo "
                "dịch chuyển thực u bằng cách đo V theo u với những dịch chuyển đã biết.",
                "Figure 6.113 · A schematic diagram of the basic optical-beam-deflection (OBD) sensing configuration. "
                "The displacement u of the surface causes the position of the reflected beam on the position-sensing "
                "detector (PSD) to move from point P to point P′; this positional change produces a change in the "
                "output voltage of the PSD. The output voltage V can be calibrated in terms of the actual "
                "displacement u by measuring V versus u for known displacements.",
                "Cấu hình cảm biến lệch chùm tia",
                "Optical beam deflection configuration")


def fig_6_114():
    o = [_defs()]
    o.append(_txt(330, 20, "Đầu dò có lưỡi dao", 8.4, weight="600"))
    # photodetector plate, below the knife edge
    o.append(_rect(160, 106, 300, 84, "#dce9f5"))
    o.append(_txt(310, 176, "photodiode", 7.6, color=GREY))
    # Gaussian cross-section, centred on the edge y = 0: grey above the edge
    # (blocked), gold below it (reaching the detector). The band the blade
    # itself covers is left blank so the hatching is not drawn over.
    for k in range(-7, 8):
        y = 106 + 6 * k
        w = 110 * math.exp(-(k * k) / 20.0)
        if y < 88:
            o.append(_line(310 - w / 2.0, y, 310 + w / 2.0, y, sw=1, color=GREY, dash="2 2"))
        elif y > 108:
            o.append(_line(310 - w / 2.0, y, 310 + w / 2.0, y, sw=1.1, color=GOLD))
    # knife blade: hatched bar whose lower face is y = 0
    o.append('<rect x="120" y="86" width="380" height="20" fill="url(#h6)" stroke="%s" stroke-width="1.2"/>' % INK)
    o.append(_line(120, 106, 500, 106, sw=2.4))
    o.append(_txt(504, 100, "lưỡi dao", 7, anchor="start", color=GREY))
    o.append(_txt(310, 52, "chùm Gauss (phần trên bị chắn)", 7, color=GREY))
    o.append(_txt(310, 206, "phần chùm tới được đầu dò", 7, color=GOLD))
    # coordinate frame: +y points down, y = 0 on the blade edge
    o.append(_arrow(100, 46, 100, 198, sw=1))
    o.append(_txt(92, 110, "y = 0", 7, anchor="end", color=GREY))
    o.append(_txt(108, 194, "y", 8, anchor="start", color=GREY))
    # displacement of the beam centre
    o.append(_arrow(440, 106, 440, 128, sw=1, color="#7b3fa0"))
    o.append(_txt(448, 124, "u", 8, anchor="start", color="#7b3fa0", weight="600"))
    o.append(_line(310, 128, 440, 128, sw=0.8, color="#7b3fa0", dash="3 3"))
    return _fig(svg(660, 224, "".join(o), "Đầu dò lưỡi dao"),
                "Hình 6-114 · Những nét cơ bản của một đầu dò vị trí, biểu diễn bằng một photodiode bị che bởi một "
                "lưỡi dao nửa vô hạn, y < 0. Như có thể dự đoán từ tính đối xứng của bố trí và được chứng minh bằng "
                "toán học, độ nhạy lệch cực đại xảy ra khi chùm chưa lệch nằm đúng tâm trên mép lưỡi dao: khi ấy một "
                "nửa công suất chùm bị chắn và một nửa tới được đầu dò.",
                "Figure 6.114 · Essential features of a position-sensing detector, represented by a photodetector "
                "shadowed by a semi-infinite knife edge, y < 0. As can be anticipated from the symmetry of the "
                "arrangement and proved mathematically, the maximal deflection sensitivity occurs when the "
                "undeflected beam is centred on the knife edge: half the beam power is then blocked and half reaches "
                "the detector.",
                "Đầu dò lưỡi dao",
                "Knife-edge detector")


def fig_6_115():
    o = [_defs()]
    x0, y0, W, H = 96, 50, 440, 140
    o.append(_axes(x0, y0, W, H, "u / r₁", "P_d / P"))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    # true small-signal tangent at u = 0:  P_d/P = 1/2 + u/(r1 sqrt(pi))
    ua, ub = -0.886, 0.85
    o.append(_line(x0 + (ua + 3.0) / 6.0 * W, y0 + H - (0.5 + ua / math.sqrt(math.pi)) * H,
                   x0 + (ub + 3.0) / 6.0 * W, y0 + H - (0.5 + ub / math.sqrt(math.pi)) * H,
                   sw=1.0, color="#9a8f7d", dash="4 3"))
    pts = []
    for i in range(241):
        u = -3.0 + 6.0 * i / 240.0
        v = 0.5 * (1.0 + math.erf(u))
        pts.append("%s %s" % (_f(x0 + (u + 3.0) / 6.0 * W), _f(y0 + H - v * H)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), INK))
    # u = r1 gives 97.7 %
    xr = x0 + (1.0 + 3.0) / 6.0 * W
    yr = y0 + H - 0.977 * H
    o.append(_line(xr, y0 + H, xr, yr, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_line(xr - 62, yr, xr, yr, sw=0.8, color=GOLD, dash="3 3"))
    o.append(_txt(xr + 5, yr - 6, "u = r₁ → 97,7%", 7, anchor="start", color=GOLD, weight="600"))
    # the linear range |u| <= 0.387 r1, marked on the u axis
    xl = x0 + (-0.387 + 3.0) / 6.0 * W
    xrr = x0 + (0.387 + 3.0) / 6.0 * W
    yb = y0 + H + 8
    o.append(_line(xl, yb, xrr, yb, sw=0.9, color=GREY))
    o.append(_line(xl, yb - 3, xl, yb + 3, sw=0.9, color=GREY))
    o.append(_line(xrr, yb - 3, xrr, yb + 3, sw=0.9, color=GREY))
    o.append(_txt((xl + xrr) / 2.0, yb + 15, "tuyến tính: |u| ≤ 0,387 r₁", 6.8, color=GREY))
    return _fig(svg(660, 220, "".join(o), "Đáp ứng chuẩn hoá của lưỡi dao"),
                "Hình 6-115 · Đáp ứng chuẩn hoá P_d/P theo u/r₁ (u là dịch chuyển tâm chùm; r₁ là bán kính chùm "
                "Gauss; P_d là công suất trên đầu dò; P là tổng công suất chùm tới). Khi u = r₁ thì P_d = 97,7% P. "
                "Tín hiệu của photodiode sẽ tuyến tính theo dịch chuyển nếu u ≤ 0,387 r₁.",
                "Figure 6.115 · The normalized response P_d/P as a function of u/r₁ (u is the displacement of the "
                "beam centre; r₁ is the Gaussian beam radius; P_d is the power on the detector; P is the total "
                "incident beam power). When u = r₁, P_d = 97.7% P. The photodetector signal is linear in "
                "displacement if u ≤ 0.387 r₁.",
                "Đáp ứng chuẩn hoá của cảm biến lưỡi dao",
                "Knife-edge normalized response")


def fig_6_116():
    o = [_defs()]
    o.append(_txt(330, 20, "Đầu dò hai ô (bicell)", 8.4, weight="600"))
    # the two cells, separated by the insensitive gap
    o.append(_rect(200, 62, 270, 78, "#dce9f5"))
    o.append(_rect(200, 170, 270, 78, "#dce9f5"))
    o.append(_txt(232, 106, "ô trên  P₂", 7.4, color=GREY))
    o.append(_txt(232, 216, "ô dưới  P₁", 7.4, color=GREY))
    # gap boundaries
    o.append(_line(186, 140, 486, 140, sw=0.7, color=GREY, dash="3 3"))
    o.append(_line(186, 170, 486, 170, sw=0.7, color=GREY, dash="3 3"))
    # gap dimension, marked to the right of the cells
    o.append(_arrow(495, 155, 495, 140, sw=0.9))
    o.append(_arrow(495, 155, 495, 170, sw=0.9))
    o.append(_txt(502, 152, "khe 2y₁", 6.9, anchor="start", color=GREY))
    o.append(_txt(502, 164, "y₁ = y₂", 6.9, anchor="start", color=GREY))
    # Gaussian beam, centred on y = 0 in the middle of the gap
    for k in range(-8, 9):
        y = 155 + 6 * k
        w = 110 * math.exp(-(k * k) / 22.0)
        o.append(_line(335 - w / 2.0, y, 335 + w / 2.0, y, sw=1.1, color=GOLD))
    o.append(_line(186, 155, 486, 155, sw=0.8, color=INK, dash="5 3"))
    o.append(_txt(180, 152, "y = 0", 6.9, anchor="end", color=INK))
    o.append(_txt(335, 262, "chùm Gauss nằm giữa khe", 7, color=GOLD))
    # displacement of the beam centre
    o.append(_arrow(450, 155, 450, 185, sw=1, color="#7b3fa0"))
    o.append(_txt(458, 182, "u", 8, anchor="start", color="#7b3fa0", weight="600"))
    o.append(_line(335, 185, 450, 185, sw=0.8, color="#7b3fa0", dash="3 3"))
    return _fig(svg(660, 272, "".join(o), "Đầu dò bicell"),
                "Hình 6-116 · Độ lệch của một chùm Gauss ban đầu nằm đúng tâm trong khe không nhạy của một đầu dò hai "
                "ô. Công suất tới ô trên là P₂ và tới ô dưới là P₁; mỗi dòng quang được biến đổi thành điện áp bằng "
                "những bộ khuếch đại trở kháng truyền giống nhau, rồi một bộ khuếch đại hiệu tạo ra tín hiệu hiệu "
                "V = V₂ − V₁.",
                "Figure 6.116 · Deflection of a Gaussian beam initially centred in the insensitive gap of a bicell "
                "detector. The power incident on the upper half is P₂ and on the lower half P₁; each photocurrent is "
                "converted to a voltage by identical transimpedance amplifiers, and a difference amplifier then "
                "forms the bicell signal V = V₂ − V₁.",
                "Đầu dò hai ô",
                "Bicell detector")


def fig_6_117():
    o = [_defs()]
    x0, y0, W, H = 96, 50, 440, 140
    o.append(_axes(x0, y0, W, H, "u / r₁", "2V / (KZP)"))
    o.append(_line(x0, y0 + H / 2.0, x0 + W, y0 + H / 2.0, sw=0.6, color=GREY, dash="2 3"))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    y1 = 0.1
    pts = []
    for i in range(241):
        u = -3.0 + 6.0 * i / 240.0
        v = math.erf(y1 + u) - math.erf(y1 - u)
        pts.append("%s %s" % (_f(x0 + (u + 3.0) / 6.0 * W), _f(y0 + H / 2.0 - v * (H / 4.0))))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(pts), INK))
    o.append('<circle cx="%s" cy="%s" r="2.6" fill="%s"/>'
             % (_f(x0 + W / 2.0), _f(y0 + H / 2.0), INK))
    o.append(_txt(x0 + 10, y0 + 22, "điểm làm việc tĩnh: V₁ − V₂ = 0", 6.8, anchor="start", color=INK))
    o.append(_line(x0 + 168, y0 + 26, x0 + W / 2.0 - 5, y0 + H / 2.0 - 5, sw=0.6, color=GREY, dash="2 2"))
    o.append(_txt(x0 + W - 8, y0 + 20, "y₁ = y₂ = r₁/10", 7, anchor="end", color=GREY))
    o.append(_txt(x0 + W - 8, y0 + H - 8, "bão hoà ở ±2", 6.6, anchor="end", color=GREY))
    return _fig(svg(660, 220, "".join(o), "Đáp ứng chuẩn hoá của bicell"),
                "Hình 6-117 · Đáp ứng chuẩn hoá 2V/(KZP) của một đầu dò hai ô theo u/r₁ với y₁ = y₂ = r₁/10. Vùng "
                "tuyến tính nằm quanh điểm làm việc tĩnh tối ưu (V₁ − V₂ = 0); độ nhạy nhỏ tín hiệu đạt cực đại khi "
                "r₁ = 2y₁ và giá trị tối ưu là 0,484/y₁.",
                "Figure 6.117 · The normalized response 2V/(KZP) in a bicell detector as a function of u/r₁ for "
                "y₁ = y₂ = r₁/10. The linear region is centred on the optimal quiescent point (V₁ − V₂ = 0); the "
                "small-signal sensitivity is optimised when r₁ = 2y₁, and the optimal value is 0.484/y₁.",
                "Đáp ứng chuẩn hoá của bicell",
                "Bicell normalized response")


def _measured(x0, y0, W, H, fn, xlab, ylab, npts=21, seed=0.0, title=""):
    o = [_axes(x0, y0, W, H, xlab, ylab)]
    pts = []
    for i in range(241):
        u = -1.0 + 2.0 * i / 240.0
        pts.append("%s %s" % (_f(x0 + (u + 1.0) / 2.0 * W), _f(y0 + H - fn(u) * H)))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (" ".join(pts), INK))
    for i in range(npts):
        u = -0.94 + 1.88 * i / float(npts - 1)
        v = fn(u) + 0.008 * math.sin(i * 2.3 + seed)
        o.append('<circle cx="%s" cy="%s" r="1.9" fill="%s"/>'
                 % (_f(x0 + (u + 1.0) / 2.0 * W), _f(y0 + H - v * H), GOLD))
    if title:
        o.append(_txt(x0 + W / 2.0, y0 - 14, title, 7.4, color=GREY))
    return "".join(o)


def fig_6_118():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H, lambda u: 0.5 * (1 + math.erf(2.5 * u)),
                       "u / r₁", "V / V_max", npts=17, seed=0.7))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    o.append(_txt(x0 + W - 6, y0 + 18, "r₁ = 0,4 mm", 7, anchor="end", color=GOLD))
    return _fig(svg(660, 224, "".join(o), "Dữ liệu đo của một ô bicell"),
                "Hình 6-118 · Điện áp ra của bộ khuếch đại trở kháng truyền ứng với dòng tín hiệu từ một ô của bicell "
                "UDT SPOT2D, theo dịch chuyển; số liệu được vẽ dưới dạng điện áp ô đã chuẩn hoá theo u/r₁. Vì tín "
                "hiệu từ một ô của bicell tương đương với một đầu dò lưỡi dao, có thể so sánh số liệu với Hình 6-115. "
                "Sự phù hợp là hợp lý với u/r₁ < 1 và khớp tốt nhất cho phép suy ra r₁ = 0,4 mm.",
                "Figure 6.118 · Transimpedance amplifier output voltage corresponding to the current signal from one "
                "cell of a United Detector Technology (UDT) SPOT2D bicell as a function of displacement; the data are "
                "plotted as normalized cell voltage versus u/r₁. Since the signal from one cell of a bicell is "
                "equivalent to a knife-edge photodetector, the data can be compared with Figure 6.115. Agreement is "
                "reasonable for u/r₁ < 1, and a best fit gives r₁ = 0.4 mm.",
                "Dữ liệu đo của một ô bicell",
                "Measured single-cell response")


def fig_6_119():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H,
                       lambda u: 0.5 + 0.45 * math.tanh(2.6 * u) / math.tanh(2.6),
                       "dịch chuyển (mm)", "V_d (V)", npts=19, seed=1.9))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    o.append(_txt(x0 + 8, y0 + 20, "A₁₂ = 4,88 mV/µm", 7, anchor="start", color=GOLD))
    return _fig(svg(660, 224, "".join(o), "Điện áp hiệu của bicell"),
                "Hình 6-119 · Điện áp hiệu theo dịch chuyển của bicell UDT SPOT2D. Những sai lệch so với đường cong lý "
                "thuyết trên Hình 6-117 ở u ≤ 0,4 mm và u ≥ 1,1 mm là do chùm đi ra ngoài mép của bicell. Vùng tuyến "
                "tính của PSD nằm quanh điểm làm việc tĩnh tối ưu (V₁ − V₂ = 0); khớp bình phương tối thiểu cho một "
                "đường thẳng có độ dốc A₁₂ = 4,88 mV/µm.",
                "Figure 6.119 · Difference voltage as a function of displacement for the UDT SPOT2D bicell. The "
                "deviations from the theoretical curve of Figure 6.117 for u ≤ 0.4 mm and u ≥ 1.1 mm are due to the "
                "beam moving off the outside edges of the bicell. The linear region is centred on the optimal "
                "quiescent point (V₁ − V₂ = 0); a least-squares fit gives a slope A₁₂ = 4.88 mV/µm.",
                "Điện áp hiệu của bicell",
                "Bicell difference voltage")


def fig_6_120():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H,
                       lambda u: 0.86 - 0.10 * max(0.0, abs(u) - 0.72) / 0.28,
                       "dịch chuyển (mm)", "V_s (V)", npts=17, seed=0.3))
    o.append(_txt(x0 + W / 2.0, y0 + H - 38, "V_sx gần như không đổi", 7, color=GOLD))
    return _fig(svg(660, 224, "".join(o), "Điện áp tổng của PSD liên tục"),
                "Hình 6-120 · Điện áp tổng theo dịch chuyển của trục x trên PSD liên tục UDT SC10. PSD được định "
                "hướng sao cho trục y thẳng đứng; như vậy về lý thuyết V_dy là hằng số khi PSD dịch chuyển, trừ gần "
                "các mép của thiết bị 10 mm × 10 mm. V_sx gần như không đổi trừ gần các mép, nghĩa là độ nhạy quang "
                "K không thay đổi nhiều theo vị trí chùm trên đầu dò này.",
                "Figure 6.120 · Sum voltage versus displacement for the x axis of the UDT SC10 continuous PSD. The "
                "PSD was oriented so that its y axis was vertical; ideally V_dy is therefore constant as the PSD is "
                "translated, except near the edges of the 10 mm × 10 mm device. V_sx is virtually constant except "
                "near those edges, which means the optical responsivity K does not vary greatly with beam position.",
                "Điện áp tổng của PSD liên tục",
                "Continuous PSD sum voltage")


def fig_6_121():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H,
                       lambda u: 0.5 + 0.46 * math.tanh(1.9 * u) / math.tanh(1.9),
                       "dịch chuyển (mm)", "V_dx (V)", npts=19, seed=2.4))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    o.append(_txt(x0 + W - 8, y0 + 20, "dải tuyến tính rộng", 7, anchor="end", color=GOLD))
    return _fig(svg(660, 224, "".join(o), "Điện áp hiệu của SC10"),
                "Hình 6-121 · Điện áp hiệu theo dịch chuyển của trục x trên PSD liên tục UDT SC10. PSD này có một dải "
                "tuyến tính rộng, nhờ đó có thể đo những dịch chuyển lớn hơn nhiều so với kích thước chùm laser.",
                "Figure 6.121 · Difference voltage versus displacement for the x axis of the UDT SC10 continuous PSD. "
                "This detector has a broad linear range, which allows displacements much larger than the laser beam "
                "size to be measured.",
                "Điện áp hiệu của SC10",
                "SC10 difference voltage")


def fig_6_122():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H,
                       lambda u: 0.5 + 0.44 * math.tanh(2.2 * u) / math.tanh(2.2),
                       "dịch chuyển (mm)", "V_dx / V_sx", npts=19, seed=0.9))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    o.append(_txt(x0 + 8, y0 + 20, "độ nhạy 183 m⁻¹", 7, anchor="start", color=GOLD))
    return _fig(svg(660, 224, "".join(o), "Tỉ số hiệu trên tổng của SC10"),
                "Hình 6-122 · Tỉ số điện áp hiệu trên điện áp tổng theo dịch chuyển của trục x trên PSD liên tục UDT "
                "SC10. Độ tuyến tính của PSD liên tục thường có thể được cải thiện bằng cách dùng tỉ số V_dx/V_sx; "
                "độ nhạy của PSD này được xác định từ khớp bình phương tối thiểu trên phần tuyến tính của đặc tuyến "
                "là 183 m⁻¹.",
                "Figure 6.122 · Ratio of difference voltage to sum voltage versus displacement for the x axis of the "
                "UDT SC10 continuous PSD. The linearity of continuous PSDs can often be improved by using the ratio "
                "V_dx/V_sx; the sensitivity of this detector, from a least-squares fit of the linear part, is "
                "183 m⁻¹.",
                "Tỉ số hiệu trên tổng của SC10",
                "SC10 difference-to-sum ratio")


def fig_6_123():
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 136
    o.append(_measured(x0, y0, W, H,
                       lambda u: 0.5 + 0.44 * math.tanh(3.4 * u) / math.tanh(3.4),
                       "dịch chuyển (mm)", "V_d / V_s", npts=19, seed=1.3))
    o.append(_line(x0 + W / 2.0, y0, x0 + W / 2.0, y0 + H, sw=0.6, color=GREY, dash="2 3"))
    o.append(_txt(x0 + 8, y0 + 20, "độ nhạy 307 m⁻¹", 7, anchor="start", color=GOLD))
    o.append(_txt(x0 + W - 8, y0 + H - 12, "dải hoạt động 10 mm", 7, anchor="end", color=GREY))
    return _fig(svg(660, 224, "".join(o), "Tỉ số của Sitek 1L10"),
                "Hình 6-123 · Tỉ số điện áp hiệu trên điện áp tổng theo dịch chuyển của PSD liên tục một trục Sitek "
                "1L10, một loại PSD mới hơn và thường tuyến tính hơn. Độ nhạy được xác định từ khớp bình phương tối "
                "thiểu trên phần tuyến tính của đặc tuyến là 307 m⁻¹.",
                "Figure 6.123 · Ratio of difference voltage to sum voltage versus displacement for the Sitek 1L10 "
                "single-axis continuous PSD, a newer class of detector that is typically more linear. The "
                "sensitivity, from a least-squares fit of the linear part, is 307 m⁻¹.",
                "Tỉ số của Sitek 1L10",
                "Sitek 1L10 ratio")
