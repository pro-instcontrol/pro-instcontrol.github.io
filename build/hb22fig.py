# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 22 — Strain Measurement
(Christopher S. Lynch, The Georgia Institute of Technology).

The source chapter contains exactly fourteen figures (22.1–22.14).
FIGS is a 14-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah22" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah22g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah22", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=5):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _rect(x, y, w, h, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, _f(sw), d))


def _dot(x, y, r=3.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _axes(x0, y0, x1, y1):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
            '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
            % (_f(x0), _f(y0), _f(x1), _f(y0), E, _f(x0), _f(y0), _f(x0), _f(y1), E))


# ---------------------------------------------------------------- 22.1
def fig_22_1():
    o = [_defs()]
    # undeformed outline
    o.append(_rect(200, 94, 280, 42, "#ffffff", S, 1.2, "6 4"))
    # deformed bar
    o.append(_rect(180, 90, 320, 50, FILL, E, 1.8))
    # forces
    o.append(_arr(120, 115, 174, 115, G, "ah22g", 2.0))
    o.append(_arr(560, 115, 506, 115, G, "ah22g", 2.0))
    # dimension L and dL
    o.append('<line x1="200" y1="158" x2="200" y2="172" stroke="%s" stroke-width="1"/>' % S)
    o.append('<line x1="480" y1="158" x2="480" y2="172" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(202, 166, 478, 166, S, "ah22", 1.1))
    o.append(_arr(478, 166, 202, 166, S, "ah22", 1.1))
    o.append('<line x1="180" y1="158" x2="180" y2="182" stroke="%s" stroke-width="1"/>' % S)
    o.append('<line x1="500" y1="158" x2="500" y2="182" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(182, 178, 498, 178, G, "ah22g", 1.1))
    o.append(_arr(498, 178, 182, 178, G, "ah22g", 1.1))

    o.append(_lbl(340, 44, "Thanh đồng nhất, đẳng hướng chịu tải kéo một trục", "tb", "middle"))
    o.append(_lbl(132, 104, "F", "tb"))
    o.append(_lbl(548, 104, "F", "tb", "end"))
    o.append(_lbl(340, 156, "L", "tb", "middle"))
    o.append(_lbl(340, 200, "L + ΔL", "tb", "middle"))
    o.append(_lbl(340, 224, "ε_L = ΔL / L        ε_t = Δw / w = −ν · ε_L", "tb", "middle"))
    return _fig(
        svg(680, 236, "".join(o), "Thanh chịu kéo một trục: giãn dọc và co ngang"),
        "Hình 22.1 · Khi một thanh đồng nhất, đẳng hướng bị kéo bởi một lực một trục, thanh giãn dài "
        "theo phương của lực và co lại theo phương vuông góc với lực. Độ giãn dài tương đối và độ co "
        "tương đối lần lượt được định nghĩa là biến dạng dọc ε_L và biến dạng ngang ε_t.",
        "Figure 22.1 · When a homogeneous isotropic bar is stretched by a uniaxial force, it elongates in "
        "the direction of the force and contracts perpendicular to it. The relative elongation and "
        "contraction are the longitudinal strain ε_L and the transverse strain ε_t.",
        "Thanh chịu kéo một trục: hai lực F ngược chiều, chiều dài L giãn thành L cộng delta L, tiết diện co lại",
        "Bar under uniaxial tension: two opposed forces F, length L extending to L plus delta L, "
        "cross-section contracting")


# ---------------------------------------------------------------- 22.2
def fig_22_2():
    o = [_defs()]
    o.append(_axes(80, 200, 360, 200))
    o.append('<line x1="80" y1="200" x2="80" y2="56" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="86" y1="194" x2="330" y2="76" stroke="%s" stroke-width="2.2"/>' % G)
    o.append('<line x1="330" y1="76" x2="356" y2="64" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="5 4"/>' % S)
    # slope triangle
    o.append('<path d="M230 132 L300 132 L300 100" fill="none" stroke="%s" stroke-width="1.1" '
             'stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(300, 96, "1", "ts", "middle"))
    o.append(_lbl(266, 146, "E = σ / ε", "tb", "middle"))

    o.append(_lbl(360, 214, "ε", "tb", "middle"))
    o.append(_lbl(70, 62, "σ", "tb", "end"))
    o.append(_lbl(200, 40, "Vùng đàn hồi tuyến tính", "ts", "middle"))

    # transverse vs longitudinal
    o.append(_axes(470, 160, 640, 160))
    o.append('<line x1="470" y1="160" x2="470" y2="80" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="474" y1="156" x2="620" y2="92" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(556, 174, "ε_L", "tb", "middle"))
    o.append(_lbl(460, 86, "ε_t", "tb", "end"))
    o.append(_lbl(556, 68, "độ dốc = −ν", "ts", "middle"))
    return _fig(
        svg(680, 228, "".join(o), "Đường cong ứng suất theo biến dạng và quan hệ biến dạng ngang"),
        "Hình 22.2 · Lực một trục trên Hình 22.1 tạo ứng suất một trục trong thanh. Khi phản ứng của "
        "vật liệu là tuyến tính, độ dốc của đường cong ứng suất – biến dạng chính là mô-đun Young E. Tỉ "
        "số âm giữa biến dạng ngang và biến dạng dọc là hệ số Poisson ν (đồ thị nhỏ bên phải).",
        "Figure 22.2 · The uniaxial force of Figure 22.1 produces uniaxial stress in the bar. When the "
        "material response is linear, the slope of the stress–strain curve is the Young's modulus E. The "
        "negative ratio of transverse to longitudinal strain is the Poisson's ratio ν (small plot, right).",
        "Đồ thị ứng suất theo biến dạng tuyến tính có độ dốc E, và đồ thị nhỏ biến dạng ngang theo biến dạng dọc có độ dốc âm",
        "Linear stress–strain plot with slope E, and a small transverse-versus-longitudinal plot with "
        "negative slope")


# ---------------------------------------------------------------- 22.3
def fig_22_3():
    o = [_defs()]
    o.append(_rect(240, 90, 160, 80, "#ffffff", S, 1.2, "6 4"))
    o.append('<polygon points="280,90 440,90 400,170 240,170" fill="%s" stroke="%s" '
             'stroke-width="1.8"/>' % (FILL, E))
    o.append(_arr(320, 70, 430, 70, G, "ah22g", 2.0))
    o.append(_arr(360, 190, 250, 190, G, "ah22g", 2.0))
    # shear angle
    o.append('<path d="M400 170 A 34 34 0 0 1 424 138" fill="none" stroke="%s" stroke-width="1.4"/>'
             % G)
    o.append(_lbl(430, 152, "γ", "tb"))
    o.append(_lbl(444, 66, "τ = F / A", "tb"))
    o.append(_lbl(200, 84, "Ô ban đầu", "ts", "end"))
    o.append(_lbl(300, 212, "Lực tiếp tuyến trên mặt song song làm vật méo đi; góc lệch là biến dạng trượt γ", "ts",
                  "middle"))
    return _fig(
        svg(680, 226, "".join(o), "Khối vật liệu chịu lực trượt và góc lệch gamma"),
        "Hình 22.3 · Khi một khối vật liệu chịu các lực song song với các mặt như hình vẽ, nó bị méo. "
        "Lực trên một đơn vị diện tích là ứng suất trượt τ, và góc thay đổi là biến dạng trượt γ. Khi "
        "quan hệ giữa ứng suất trượt và biến dạng trượt là tuyến tính, tỉ số giữa chúng là mô-đun trượt G.",
        "Figure 22.3 · When a block of material is subjected to forces parallel to its sides, it distorts. "
        "The force per unit area is the shear stress τ and the angle change is the shear strain γ. When "
        "the relation between them is linear, the ratio is the shear modulus G.",
        "Khối chịu trượt: ô ban đầu nét đứt, khối méo thành hình bình hành, lực tiếp tuyến ở mặt trên và dưới, góc lệch gamma",
        "Block in shear: dashed original square, distorted parallelogram, tangential forces top and "
        "bottom, shear angle gamma")


# ---------------------------------------------------------------- 22.4
def fig_22_4():
    o = [_defs()]
    o.append(_rect(140, 86, 400, 56, FILL, E, 1.8))
    o.append(_arr(96, 114, 134, 114, G, "ah22g", 2.0))
    o.append(_arr(584, 114, 546, 114, G, "ah22g", 2.0))
    # element aligned with the load: elongates only
    o.append(_rect(180, 98, 54, 32, "#ffffff", E, 1.6))
    # element at 45 degrees: distorted
    cx, cy, h = 320, 114, 26
    pts = [(cx - h, cy), (cx, cy - h), (cx + h, cy), (cx, cy + h)]
    o.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="1.6"/>'
             % (" ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts), E))
    o.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="5 4"/>'
             % (" ".join("%s,%s" % (_f(a), _f(b)) for a, b in
                         [(cx - h, cy), (cx, cy - h), (cx + h, cy), (cx, cy + h)]), S))

    o.append(_lbl(207, 152, "phương chính: chỉ giãn", "ts", "middle"))
    o.append(_lbl(320, 178, "45°: giãn + méo (góc thay đổi)", "ts", "middle"))
    o.append(_lbl(207, 76, "phần tử a", "ts", "middle"))
    o.append(_lbl(320, 76, "phần tử b", "ts", "middle"))
    o.append(_lbl(340, 206, "Trên một mặt bất kỳ luôn có ít nhất hai phương chính mà biến dạng thuần là giãn", "ts",
                  "middle"))
    return _fig(
        svg(680, 220, "".join(o), "Hai phần tử vuông trên thanh chịu kéo: một giãn, một méo"),
        "Hình 22.4 · Một số phần tử của thanh chịu kéo một trục chỉ giãn và co; những phần tử này nằm "
        "theo các phương chính. Các phần tử khác còn bị méo. Phần tử a (thẳng hàng với lực) chỉ giãn dài, "
        "còn phần tử b (đặt 45°) vừa giãn vừa bị méo vì góc của nó thay đổi.",
        "Figure 22.4 · Some elements of a bar under uniaxial tension undergo elongation and contraction "
        "only; these lie in principal directions. Other elements undergo distortion as well. Element a "
        "(aligned with the load) merely elongates, while element b (at 45°) both elongates and distorts "
        "because its angles change.",
        "Thanh chịu kéo với hai ô vuông: ô thẳng hàng với lực chỉ giãn, ô đặt 45 độ bị méo thành hình thoi",
        "Bar under tension with two squares: the aligned square only elongates, the 45-degree square "
        "distorts into a rhombus")


# ---------------------------------------------------------------- 22.5
def fig_22_5():
    o = [_defs()]
    # encapsulation layer
    o.append(_rect(210, 56, 270, 16, "#f2f2f2", E, 1.2, "5 3"))
    # foil grid (serpentine)
    ys = [100 + i * 9 for i in range(5)]
    g = ['<path d="M240 %s' % _f(ys[0])]
    for i, y in enumerate(ys):
        x_end = 400 if i % 2 == 0 else 240
        x_start = 240 if i % 2 == 0 else 400
        g.append(' L%s %s' % (_f(x_end), _f(y)))
        if i < len(ys) - 1:
            g.append(' L%s %s' % (_f(x_end), _f(ys[i + 1])))
    g.append('" fill="none" stroke="%s" stroke-width="2.6"/>' % G)
    o.append("".join(g))
    # lead wires
    o.append('<path d="M240 100 L186 92" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    o.append('<path d="M400 136 L452 144" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    # substrate
    o.append(_rect(200, 158, 290, 20, WARM, G, 1.4))

    o.append(_lbl(490, 62, "Lớp phủ cách điện", "ts"))
    o.append(_lbl(490, 76, "(polyimide)", "ts"))
    o.append(_lbl(490, 106, "Lưới foil constantan", "ts"))
    o.append(_lbl(490, 120, "(phần tử cảm biến)", "ts"))
    o.append(_lbl(490, 168, "Đế polyimide", "ts"))
    o.append(_lbl(176, 88, "Dây dẫn", "ts", "end"))
    o.append(_lbl(200, 202, "Hướng trục của gage (chiều dài lưới)", "ts", "middle"))
    o.append(_arr(200, 216, 400, 216, E, "ah22", 1.2))
    return _fig(
        svg(680, 228, "".join(o), "Cấu tạo của một gage điện trở lá mỏng"),
        "Hình 22.5 · Cấu tạo của gage điện trở lá mỏng hoặc gage dây: một đế cách điện mỏng (thường là "
        "màng polyimide), một lưới lá hoặc dây (thường bằng constantan) dán lên đế, các dây dẫn nối lưới "
        "với mạch đo điện trở, và thường có thêm một lớp bọc cách điện (một tấm polyimide thứ hai).",
        "Figure 22.5 · Gage construction of a foil or wire piezoresistive gage: a thin insulating "
        "substrate (usually polyimide film), a foil or wire grid (usually constantan) bonded to it, lead "
        "wires connecting the grid to a resistance-measuring circuit, and often an insulating "
        "encapsulation (a second polyimide sheet).",
        "Gage điện trở: lớp phủ cách điện phía trên, lưới foil hình rắn bò ở giữa, đế polyimide phía dưới, hai dây dẫn",
        "Resistance gage: encapsulation layer on top, serpentine foil grid in the middle, polyimide "
        "substrate below, two lead wires")


# ---------------------------------------------------------------- 22.6
def fig_22_6():
    o = [_defs()]
    o.append('<polygon points="260,80 300,58 440,58 400,80" fill="#f7f7f7" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append('<polygon points="400,80 440,58 440,120 400,142" fill="#f2f2f2" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append(_rect(260, 80, 140, 62, FILL, E, 1.6))
    o.append(_arr(300, 111, 360, 111, G, "ah22g", 1.8))

    o.append('<line x1="260" y1="152" x2="260" y2="164" stroke="%s" stroke-width="1"/>' % S)
    o.append('<line x1="400" y1="152" x2="400" y2="164" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(262, 160, 398, 160, S, "ah22", 1.1))
    o.append(_arr(398, 160, 262, 160, S, "ah22", 1.1))
    o.append('<line x1="440" y1="58" x2="470" y2="58" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(452, 58, 452, 118, S, "ah22", 1.1))
    o.append(_arr(452, 118, 452, 62, S, "ah22", 1.1))

    o.append(_lbl(330, 176, "L", "tb", "middle"))
    o.append(_lbl(478, 92, "w", "tb"))
    o.append(_lbl(370, 52, "t", "tb", "middle"))
    o.append(_lbl(330, 100, "i", "tb", "middle"))
    o.append(_lbl(330, 204, "R = ρ · L / A        A = w · t", "tb", "middle"))
    return _fig(
        svg(680, 218, "".join(o), "Một nhánh lưới của gage điện trở với chiều dài, chiều rộng và chiều dày"),
        "Hình 22.6 · Một nhánh đơn của lưới gage điện trở được dùng để giải thích nguồn gốc của sự thay "
        "đổi điện trở tương đối khi có biến dạng. Điện trở bằng điện trở suất nhân chiều dài chia cho "
        "diện tích tiết diện; khi nhánh bị kéo dài, cả chiều dài, tiết diện và điện trở suất đều thay đổi.",
        "Figure 22.6 · A single leg of a piezoresistive gage explains the origin of the relative "
        "resistance change that occurs in response to strain. The resistance is resistivity times length "
        "divided by cross-sectional area; when the leg is stretched, length, area and resistivity all "
        "change.",
        "Một nhánh lưới gage dạng khối hộp với chiều dài L, chiều rộng w, chiều dày t và dòng điện i",
        "One grid leg as a box with length L, width w, thickness t and current i")


# ---------------------------------------------------------------- 22.7
def fig_22_7():
    o = [_defs()]
    # rails
    o.append('<line x1="220" y1="60" x2="460" y2="60" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<line x1="220" y1="190" x2="460" y2="190" stroke="%s" stroke-width="1.6"/>' % E)
    # left branch
    o.append('<line x1="220" y1="60" x2="220" y2="74" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_rect(204, 74, 32, 32, "#ffffff", E, 1.6))
    o.append(_lbl(220, 95, "R₁", "tb", "middle"))
    o.append('<line x1="220" y1="106" x2="220" y2="140" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_rect(204, 140, 32, 32, "#ffffff", E, 1.6))
    o.append(_lbl(220, 161, "R₃", "tb", "middle"))
    o.append('<line x1="220" y1="172" x2="220" y2="190" stroke="%s" stroke-width="1.6"/>' % E)
    # right branch
    o.append('<line x1="460" y1="60" x2="460" y2="74" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_rect(444, 74, 32, 32, "#ffffff", E, 1.6))
    o.append(_lbl(460, 95, "R₂", "tb", "middle"))
    o.append('<line x1="460" y1="106" x2="460" y2="140" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_rect(444, 140, 32, 32, "#ffffff", E, 1.6))
    o.append(_lbl(460, 161, "R₄", "tb", "middle"))
    o.append('<line x1="460" y1="172" x2="460" y2="190" stroke="%s" stroke-width="1.6"/>' % E)
    # nodes
    o.append(_dot(340, 60))
    o.append(_dot(340, 190))
    o.append(_dot(220, 123))
    o.append(_dot(460, 123))
    o.append(_lbl(340, 50, "A", "tb", "middle"))
    o.append(_lbl(340, 208, "C", "tb", "middle"))
    o.append(_lbl(208, 120, "B", "tb", "end"))
    o.append(_lbl(472, 120, "D", "tb"))
    # source loop
    o.append('<path d="M340 60 L340 34 L120 34 L120 216 L340 216 L340 190" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="104" y1="112" x2="136" y2="112" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<line x1="110" y1="124" x2="130" y2="124" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(96, 120, "V_in", "tb", "end"))
    # output loop
    o.append('<path d="M220 123 L176 123 L176 250 L504 250 L504 123 L460 123" fill="none" '
             'stroke="%s" stroke-width="1.5" stroke-dasharray="6 4"/>' % G)
    o.append('<circle cx="340" cy="250" r="15" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % G)
    o.append(_lbl(340, 255, "V", "tb", "middle"))
    o.append(_lbl(340, 282, "V_out = V_B − V_D", "tb", "middle"))
    return _fig(
        svg(680, 292, "".join(o), "Sơ đồ cầu Wheatstone bốn nhánh với nguồn và đầu ra"),
        "Hình 22.7 · Cầu Wheatstone được dùng để đo sự thay đổi điện trở tương đối của các gage điện "
        "trở. Cầu là tổ hợp của bốn điện trở và một nguồn điện áp; một đến bốn nhánh có thể là gage. Đầu "
        "ra của cầu là hiệu điện áp giữa hai điểm B và D; các nhánh ABC và ADC là những bộ chia áp.",
        "Figure 22.7 · The Wheatstone bridge measures the relative resistance change of piezoresistive "
        "strain gages. It is a combination of four resistors and a voltage source; one to four arms may be "
        "gages. The output is the difference between the voltages at points B and D, since paths ABC and "
        "ADC are voltage dividers.",
        "Cầu Wheatstone: bốn điện trở R1 đến R4 trên hai nhánh, nút A trên và C dưới, nút B và D ở giữa, nguồn vào và đồng hồ ra",
        "Wheatstone bridge: four resistors R1 to R4 on two branches, nodes A and C top and bottom, nodes B "
        "and D in the middle, input source and output meter")


# ---------------------------------------------------------------- 22.8
def fig_22_8():
    o = [_defs()]
    cx, cy, r = 320, 150, 92
    o.append('<line x1="180" y1="150" x2="470" y2="150" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="320" y1="52" x2="320" y2="250" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="1.8"/>'
             % (_f(cx), _f(cy), _f(r), E))
    o.append(_dot(cx, cy, 3.4))
    o.append(_lbl(cx + 6, cy - 8, "C", "tb"))
    # radius and angle
    a = _m.radians(-42)
    px, py = cx + r * _m.cos(a), cy + r * _m.sin(a)
    a2 = a + _m.pi / 2
    qx, qy = cx + r * _m.cos(a2), cy + r * _m.sin(a2)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>'
             % (_f(cx), _f(cy), _f(px), _f(py), G))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>'
             % (_f(cx), _f(cy), _f(qx), _f(qy), G))
    o.append(_dot(px, py, 3.4, G))
    o.append(_dot(qx, qy, 3.4, G))
    o.append(_lbl(px + 8, py - 4, "ε_x", "tb"))
    o.append(_lbl(qx + 8, qy + 6, "ε_x′", "tb"))
    o.append('<path d="M%s %s A 40 40 0 0 0 %s %s" fill="none" stroke="%s" stroke-width="1.2"/>'
             % (_f(cx + 40 * _m.cos(a)), _f(cy + 40 * _m.sin(a)),
                _f(cx + 40 * _m.cos(a2)), _f(cy + 40 * _m.sin(a2)), S))
    o.append(_lbl(cx + 48, cy + 6, "2θ", "ts"))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="150" stroke="%s" stroke-width="1" '
             'stroke-dasharray="4 3"/>' % (_f(px), _f(py), _f(px), S))
    # principal points
    o.append(_dot(cx + r, cy, 3.4, E))
    o.append(_dot(cx - r, cy, 3.4, E))
    o.append(_lbl(cx + r + 8, cy - 6, "ε₁", "tb"))
    o.append(_lbl(cx - r - 8, cy - 6, "ε₂", "tb", "end"))
    o.append(_lbl(cx + 46, cy - 44, "R", "tb"))
    o.append(_lbl(470, 144, "ε", "tb"))
    o.append(_lbl(310, 48, "γ/2", "tb", "end"))
    o.append(_lbl(320, 274, "ε₁,₂ = C ± R,   C = (ε_x + ε_y)/2,   tan 2θ = (ε_x′ − C)/(ε_x − C)", "tb",
                  "middle"))
    return _fig(
        svg(680, 288, "".join(o), "Vòng tròn Mohr dùng để tìm phương chính và biến dạng chính"),
        "Hình 22.8 · Bộ ba gage (rosette) ba phần tử được dùng để đo biến dạng khi chưa biết các phương "
        "chính. Vòng tròn Mohr được dùng để tìm các phương chính và các giá trị biến dạng chính: biến "
        "dạng giãn nằm trên trục hoành, biến dạng trượt trên trục tung, tâm C và bán kính R. Các phương "
        "chính ứng với biến dạng trượt bằng không.",
        "Figure 22.8 · A three-element rosette measures strain when the principal directions are unknown. "
        "Mohr's circle finds the principal directions and principal strain values: elongational strain on "
        "the horizontal axis, shear strain on the vertical axis, centre C and radius R. Principal "
        "directions correspond to zero shear strain.",
        "Vòng tròn Mohr: tâm C, bán kính R, hai điểm biến dạng chính trên trục hoành, hai điểm ứng với gage xiên góc 2 theta",
        "Mohr's circle: centre C, radius R, two principal strain points on the horizontal axis, two points "
        "for the inclined gages at angle 2 theta")


# ---------------------------------------------------------------- 22.9
def fig_22_9():
    o = [_defs()]
    o.append(_rect(232, 62, 216, 10, "#f2f2f2", E, 1.1))
    o.append(_rect(232, 132, 216, 10, "#f2f2f2", E, 1.1))
    o.append(_rect(240, 74, 200, 6, "#dddddd", E, 1.1))
    o.append(_rect(240, 124, 200, 6, "#dddddd", E, 1.1))
    o.append(_rect(240, 80, 200, 44, WARM, G, 1.5))
    o.append('<path d="M240 86 L186 78" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<path d="M440 124 L494 132" fill="none" stroke="%s" stroke-width="1.6"/>' % E)

    o.append(_lbl(500, 76, "Lớp polyimide", "ts"))
    o.append(_lbl(500, 90, "cách điện", "ts"))
    o.append(_lbl(500, 106, "Điện cực kim loại", "ts"))
    o.append(_lbl(500, 130, "Màng PVDF", "ts"))
    o.append(_lbl(500, 144, "áp điện", "ts"))
    o.append(_lbl(178, 74, "Dây dẫn", "ts", "end"))
    o.append(_lbl(240, 168, "Điện cực có thể được bọc kín giữa các lớp polyimide", "ts"))
    return _fig(
        svg(680, 184, "".join(o), "Cấu tạo của một gage áp điện màng mỏng PVDF"),
        "Hình 22.9 · Cấu tạo điển hình của một gage áp điện. Gage PVDF gồm một màng áp điện mỏng có các "
        "điện cực kim loại; dây dẫn nối các điện cực với mạch đo điện tích. Có thể mua loại gage có các "
        "điện cực được bọc kín giữa các lớp polyimide cách điện.",
        "Figure 22.9 · Typical gage construction of a piezoelectric gage. The PVDF gage consists of a thin "
        "piezoelectric film with metal electrodes; lead wires connect the electrodes to a charge measuring "
        "circuit. Gages can be obtained with the electrodes encapsulated between insulating polyimide "
        "layers.",
        "Gage áp điện: màng PVDF ở giữa, hai điện cực kim loại trên và dưới, hai lớp polyimide bọc ngoài, dây dẫn hai bên",
        "Piezoelectric gage: PVDF film in the middle, metal electrodes above and below, two polyimide "
        "cover layers, lead wires on both sides")


# ---------------------------------------------------------------- 22.10
def fig_22_10():
    o = [_defs()]
    o.append(_rect(200, 78, 260, 10, "#dddddd", E, 1.3))
    o.append(_rect(200, 152, 260, 10, "#dddddd", E, 1.3))
    o.append(_rect(200, 88, 260, 64, FILL, E, 1.2))
    # dipoles
    for i in range(7):
        x = 222 + i * 36
        o.append(_arr(x, 144, x, 100, E, "ah22", 1.2))
    # charges
    for i in range(9):
        x = 214 + i * 28
        o.append(_lbl(x, 100, "+", "tb", "middle"))
        o.append(_lbl(x, 148, "−", "tb", "middle"))

    o.append(_lbl(470, 84, "Điện cực", "ts"))
    o.append(_lbl(470, 124, "Vật liệu áp điện", "ts"))
    o.append(_lbl(470, 138, "đã phân cực", "ts"))
    o.append(_lbl(470, 158, "Điện cực", "ts"))
    o.append('<line x1="200" y1="176" x2="460" y2="176" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(200, 172, 460, 172, S, "ah22", 1.1))
    o.append(_arr(460, 172, 200, 172, S, "ah22", 1.1))
    o.append(_lbl(330, 192, "d", "tb", "middle"))
    o.append(_lbl(330, 214, "P = Q · d / V      →      P ≈ Q / A", "tb", "middle"))
    return _fig(
        svg(680, 226, "".join(o), "Tiết diện vật liệu áp điện như một tụ điện bản song song"),
        "Hình 22.10 · Tiết diện đại diện của một vật liệu áp điện được tạo thành tụ điện bản song song. "
        "Vật liệu áp điện đã được phân cực, do đó có điện tích trên các điện cực. Khi vật liệu bị biến "
        "dạng, sự phân cực thay đổi và điện tích dịch chuyển.",
        "Figure 22.10 · A representative cross-section of a piezoelectric material formed into a parallel "
        "plate capacitor. The material is polarized, which puts charge on the electrodes. When the material "
        "is strained the polarization changes and charge flows.",
        "Tụ điện bản song song: hai điện cực, lớp vật liệu áp điện có các lưỡng cực hướng lên, điện tích dương và âm trên hai bản",
        "Parallel plate capacitor: two electrodes, piezoelectric layer with upward dipoles, positive and "
        "negative charges on the plates")


# ---------------------------------------------------------------- 22.11
def fig_22_11():
    o = [_defs()]
    # ---- electrometer
    o.append('<line x1="96" y1="86" x2="286" y2="86" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="96" y1="146" x2="286" y2="146" stroke="%s" stroke-width="1.5"/>' % E)
    # Cg
    o.append('<line x1="126" y1="98" x2="126" y2="112" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="126" y1="120" x2="126" y2="134" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="126" y1="86" x2="126" y2="98" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="126" y1="134" x2="126" y2="146" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(126, 162, "C_g (cảm biến)", "ts", "middle"))
    # C
    o.append('<line x1="240" y1="98" x2="240" y2="112" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="240" y1="120" x2="240" y2="134" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="240" y1="86" x2="240" y2="98" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="240" y1="134" x2="240" y2="146" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(240, 162, "C ≥ 1000 C_g", "ts", "middle"))
    # R in the loop
    o.append('<path d="M156 146 L166 146 L172 138 L180 154 L188 138 L196 154 L202 146 L212 146" '
             'fill="none" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(184, 172, "R", "ts", "middle"))
    o.append(_arr(286, 116, 320, 116, G, "ah22g", 1.4))
    o.append(_lbl(300, 104, "V", "tb", "middle"))
    o.append(_lbl(190, 46, "Điện kế (electrometer)", "tb", "middle"))

    # ---- charge amplifier
    o.append('<polygon points="440,78 440,154 500,116" fill="#ffffff" stroke="%s" '
             'stroke-width="1.6"/>' % E)
    o.append(_lbl(452, 108, "+", "tb", "middle"))
    o.append(_lbl(452, 136, "−", "tb", "middle"))
    o.append('<line x1="392" y1="104" x2="440" y2="104" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="392" y1="140" x2="440" y2="140" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="392" y1="104" x2="392" y2="140" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="392" y1="122" x2="368" y2="122" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(360, 126, "C_g", "ts", "end"))
    # feedback
    o.append('<path d="M440 104 L440 56 L536 56 L536 116" fill="none" stroke="%s" stroke-width="1.5"/>'
             % E)
    o.append('<line x1="524" y1="44" x2="548" y2="44" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="524" y1="52" x2="548" y2="52" stroke="%s" stroke-width="2.6"/>' % E)
    o.append('<line x1="536" y1="56" x2="536" y2="44" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="536" y1="52" x2="536" y2="56" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_lbl(560, 50, "C_f", "tb"))
    o.append('<line x1="500" y1="116" x2="576" y2="116" stroke="%s" stroke-width="1.5"/>' % E)
    o.append(_arr(540, 116, 576, 116, G, "ah22g", 1.4))
    o.append(_lbl(588, 120, "V", "tb"))
    o.append(_lbl(486, 178, "Bộ khuếch đại điện tích", "tb", "middle"))
    return _fig(
        svg(680, 194, "".join(o), "Hai mạch đo điện tích: điện kế và bộ khuếch đại điện tích"),
        "Hình 22.11 · Điện kế và bộ khuếch đại điện tích là hai mạch thường dùng nhất để đo điện tích từ "
        "các bộ chuyển đổi áp điện. Ở mạch điện kế, cảm biến áp điện được nối với một tụ điện có điện "
        "dung C lớn hơn ít nhất 1000 lần điện dung C_g của cảm biến; điện tích đo được từ điện áp trên tụ "
        "(Q = CV). Bộ khuếch đại điện tích thường là một khuếch đại thuật toán đầu vào FET có tụ hồi tiếp, "
        "tạo điện áp tỉ lệ với điện tích vào.",
        "Figure 22.11 · The electrometer and the charge amplifier are the most common circuits used to "
        "measure charge from piezoelectric transducers. In the electrometer the sensor drives a capacitor C "
        "at least 1000 times C_g and the charge follows from the voltage across it (Q = CV). The charge "
        "amplifier is usually an FET-input op amp with capacitive feedback, producing a voltage "
        "proportional to the input charge.",
        "Hai mạch: bên trái điện kế với tụ cảm biến, tụ lớn và điện trở; bên phải bộ khuếch đại điện tích với tụ hồi tiếp",
        "Two circuits: electrometer on the left with sensor capacitor, large capacitor and resistor; "
        "charge amplifier on the right with feedback capacitor")


# ---------------------------------------------------------------- 22.12
def fig_22_12():
    o = [_defs()]
    o.append(_box(70, 90, 74, 40, "Laser", E, "#ffffff", 11))
    o.append('<line x1="144" y1="110" x2="330" y2="110" stroke="%s" stroke-width="3"/>' % E)
    o.append(_box(330, 96, 44, 28, "C", E, WARM, 12))
    o.append('<line x1="374" y1="110" x2="452" y2="110" stroke="%s" stroke-width="3"/>' % E)
    # cavity mirrors
    o.append('<line x1="452" y1="88" x2="452" y2="132" stroke="%s" stroke-width="3"/>' % E)
    o.append('<line x1="524" y1="88" x2="524" y2="132" stroke="%s" stroke-width="3"/>' % E)
    # reflected beams
    o.append('<path d="M452 98 L392 78" fill="none" stroke="%s" stroke-width="1.3" '
             'stroke-dasharray="5 4"/>' % G)
    o.append('<path d="M524 122 L452 122" fill="none" stroke="%s" stroke-width="1.3" '
             'stroke-dasharray="5 4"/>' % G)
    o.append(_arr(452, 122, 400, 122, G, "ah22g", 1.2))
    o.append(_arr(392, 78, 352, 64, G, "ah22g", 1.2))
    # photodetector
    o.append(_box(556, 92, 76, 38, "Đầu dò", E, "#ffffff", 11))
    o.append('<path d="M352 124 L352 176 L594 176 L594 130" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % E)

    o.append(_lbl(220, 96, "Sợi quang đơn mode", "ts", "middle"))
    o.append(_lbl(340, 140, "Coupler", "ts", "middle"))
    o.append(_lbl(452, 152, "Gương bán mạ", "ts", "middle"))
    o.append(_lbl(488, 82, "Buồng đo", "ts", "middle"))
    o.append('<line x1="452" y1="160" x2="524" y2="160" stroke="%s" stroke-width="1"/>' % S)
    o.append(_arr(452, 156, 524, 156, S, "ah22", 1.1))
    o.append(_arr(524, 156, 452, 156, S, "ah22", 1.1))
    o.append(_lbl(488, 172, "d", "tb", "middle"))
    o.append(_lbl(400, 60, "chùm phản xạ", "ts"))
    o.append(_lbl(340, 200, "Hai chùm phản xạ giao thoa; khi buồng giãn, giao thoa luân phiên đồng pha và ngược pha", "ts",
                  "middle"))
    return _fig(
        svg(680, 212, "".join(o), "Sơ đồ gage biến dạng sợi quang Fabry-Perot"),
        "Hình 22.12 · Sơ đồ gage biến dạng sợi quang Fabry–Perot. Cảm biến gồm nguồn sáng laser, sợi "
        "quang đơn mode, một coupler (tương đương bộ tách chùm của quang học), một buồng đo biến dạng và "
        "một đầu dò quang. Khi buồng giãn ra, giao thoa đồng pha và ngược pha luân phiên xuất hiện; mỗi "
        "đỉnh đầu ra ứng với độ dịch khe 650 nm với nguồn 1,3 µm.",
        "Figure 22.12 · A schematic of the Fabry–Perot fiber optic strain gage: a laser source, single-mode "
        "fibers, a coupler (the fiber equivalent of a beam splitter), a strain-sensing cavity and a "
        "photodetector. When the cavity elongates, alternating constructive and destructive interference "
        "occur; for a 1.3 µm source each output peak corresponds to a 650 nm gap displacement.",
        "Gage sợi quang Fabry-Perot: laser, sợi quang, coupler, buồng đo có hai gương, chùm phản xạ và đầu dò quang",
        "Fabry–Perot fiber gage: laser, optical fiber, coupler, cavity with two mirrors, reflected beams "
        "and photodetector")


# ---------------------------------------------------------------- 22.13
def fig_22_13():
    o = [_defs()]
    o.append(_box(60, 92, 70, 36, "Nguồn sáng", E, "#ffffff", 9))
    o.append(_rect(164, 88, 16, 44, "#dddddd", E, 1.3))
    o.append(_rect(214, 88, 16, 44, "#e8e8e8", E, 1.3))
    o.append(_rect(300, 84, 84, 52, FILL, E, 1.6))
    o.append(_rect(418, 88, 16, 44, "#e8e8e8", E, 1.3))
    o.append(_rect(468, 88, 16, 44, "#dddddd", E, 1.3))
    o.append(_box(540, 92, 78, 36, "Quan sát", E, "#ffffff", 9))
    o.append('<line x1="130" y1="110" x2="540" y2="110" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="7 4"/>' % G)

    o.append(_lbl(172, 148, "P", "tb", "middle"))
    o.append(_lbl(222, 148, "λ/4", "tb", "middle"))
    o.append(_lbl(342, 152, "Mẫu", "tb", "middle"))
    o.append(_lbl(426, 148, "λ/4", "tb", "middle"))
    o.append(_lbl(476, 148, "A", "tb", "middle"))
    o.append(_lbl(165, 166, "phân cực", "ts", "middle"))
    o.append(_lbl(232, 166, "bản 1/4 sóng", "ts", "middle"))
    o.append(_lbl(416, 166, "bản 1/4 sóng", "ts", "middle"))
    o.append(_lbl(484, 166, "phân tích", "ts", "middle"))
    o.append(_lbl(340, 200, "Ánh sáng: phân cực phẳng → phân cực tròn → lệch pha trong mẫu → trở lại phẳng → phân tích", "ts",
                  "middle"))
    return _fig(
        svg(680, 212, "".join(o), "Sơ đồ hệ kính phân cực (polariscope) để quan sát lưỡng chiết"),
        "Hình 22.13 · Sơ đồ kính phân cực (polariscope) — hệ dùng để đo lưỡng chiết. Kỹ thuật này cho "
        "một phép đo toàn trường của hiệu các biến dạng chính. Ánh sáng lần lượt qua bản phân cực thứ "
        "nhất (phân cực phẳng), bản 1/4 sóng (phân cực tròn), mẫu (thay đổi pha), bản 1/4 sóng thứ hai "
        "(trở lại phân cực phẳng) và bản phân tích.",
        "Figure 22.13 · A schematic of the polariscope, a system for measuring birefringence. The technique "
        "gives a full-field measure of the difference in principal strains. Light passes through the first "
        "polarizer (plane polarization), a quarter wave plate (circular polarization), the specimen (phase "
        "changes), the second quarter wave plate (back to plane polarization) and the final analyzer.",
        "Kính phân cực: nguồn sáng, bản phân cực P, hai bản một phần tư sóng, mẫu ở giữa, bản phân tích A và màn quan sát",
        "Polariscope: light source, polarizer P, two quarter-wave plates, specimen in the middle, analyzer "
        "A and viewing screen")


# ---------------------------------------------------------------- 22.14
def fig_22_14():
    o = [_defs()]
    # panel (a): pure extension -> horizontal fringes
    x0, y0, w, h = 90, 78, 220, 120
    o.append(_rect(x0, y0, w, h, "#ffffff", E, 1.3))
    for i in range(1, 24):
        x = x0 + i * 9
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8"/>'
                 % (_f(x), _f(y0 + 2), _f(x), _f(y0 + h - 2), S))
    for j in range(4):
        yy = y0 + 14 + j * 30
        o.append('<rect x="%s" y="%s" width="%s" height="13" fill="#f2f2f2" stroke="none"/>'
                 % (_f(x0 + 2), _f(yy), _f(w - 4)))

    # panel (b): relative rotation -> vertical fringes
    x1 = 380
    o.append(_rect(x1, y0, w, h, "#ffffff", E, 1.3))
    for i in range(1, 24):
        x = x1 + i * 9
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8"/>'
                 % (_f(x), _f(y0 + 2), _f(x), _f(y0 + h - 2), S))
    for i in range(1, 24):
        xa = x1 + i * 9.6
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8"/>'
                 % (_f(xa), _f(y0 + 2), _f(xa + 10), _f(y0 + h - 2), G))
    for j in range(7):
        xx = x1 + 8 + j * 30
        o.append('<rect x="%s" y="%s" width="13" height="%s" fill="#f2f2f2" stroke="none"/>'
                 % (_f(xx), _f(y0 + 2), _f(h - 4)))

    o.append(_lbl(200, 216, "(a) giãn thuần → vân song song", "ts", "middle"))
    o.append(_lbl(490, 216, "(b) quay tương đối → vân gần thẳng đứng", "ts", "middle"))
    o.append(_lbl(200, 62, "hai cách tử chồng lên nhau", "ts", "middle"))
    o.append(_lbl(490, 62, "cách tử mẫu quay so với cách tử chuẩn", "ts", "middle"))
    o.append(_lbl(340, 240, "Vân sáng – tối là kết quả của việc giãn và quay tương đối giữa hai cách tử", "ts",
                  "middle"))
    return _fig(
        svg(680, 252, "".join(o), "Vân moiré tạo bởi hai cách tử chồng lên nhau"),
        "Hình 22.14 · Minh hoạ vân moiré tạo thành khi hai cách tử chồng lên nhau. Vân là kết quả của "
        "việc giãn và quay tương đối giữa các cách tử; hình ảnh vân được dùng để xác định trường dịch "
        "chuyển. (a) giãn thuần cho các vân song song; (b) quay tương đối cho các vân gần như thẳng đứng.",
        "Figure 22.14 · A demonstration of moiré fringes formed by overlapping gratings. The fringes result "
        "from stretching and relative rotation of the gratings and are used to determine displacement "
        "fields. (a) pure extension gives parallel fringes; (b) relative rotation gives near-vertical "
        "fringes.",
        "Hai ô vân moiré: ô trái có vân ngang do giãn thuần, ô phải có vân thẳng đứng do quay tương đối",
        "Two moiré panels: left with horizontal fringes from pure extension, right with vertical fringes "
        "from relative rotation")


FIGS = [fig_22_1, fig_22_2, fig_22_3, fig_22_4, fig_22_5, fig_22_6, fig_22_7, fig_22_8,
        fig_22_9, fig_22_10, fig_22_11, fig_22_12, fig_22_13, fig_22_14]


def fig(n):
    return FIGS[n - 1]()
