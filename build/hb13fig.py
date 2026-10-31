# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 13
(Volume Measurement). Every function returns
(svg, caption_vi, caption_en, aria_vi, aria_en).
Medical/imaging figures are drawn as clean labelled line diagrams; the two
plots (13.1, 13.7, 13.8) use simple computed curves.
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
            '<marker id="ah13" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah13g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G))


def _ax(x0, y0, w, h, xl, yl):
    o = ['<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
         % (_f(x0), _f(y0), _f(x0 + w), _f(y0), E),
         '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
         % (_f(x0), _f(y0), _f(x0), _f(y0 - h), E)]
    o.append(_lbl(x0 + w, y0 + 14, xl, "ts", "end"))
    o.append(_lbl(x0 - 6, y0 - h - 4, yl, "ts", "end"))
    return o


# ---------------------------------------------------------------- 13.1
def fig_13_1():
    o = [_defs()]
    x0, y0, w, h = 90, 180, 500, 120
    o += _ax(x0, y0, w, h, "thời gian t", "thể tích V")
    # venous occlusion recording: volume rises then plateaus
    pts = []
    for i in range(0, 101):
        x = x0 + w * i / 100.0
        # ramp up then plateau with slight noise-free curve
        tt = i / 100.0
        if tt < 0.12:
            v = 0.10 * tt / 0.12
        else:
            v = 0.10 + 0.85 * (1 - math.exp(-(tt - 0.12) * 6))
        y = y0 - h * v
        pts.append((x, y))
    d = "M" + " L".join("%s %s" % (_f(x), _f(y)) for x, y in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, G))
    # occlusion marker
    ox = x0 + w * 0.12
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>'
            % (_f(ox), _f(y0), _f(ox), _f(y0 - h - 6), S))
    o.append(_lbl(ox + 4, y0 - h - 8, "tắc tĩnh mạch", "ts"))
    o.append(_lbl(x0 + 10, y0 - h * 0.95, "V tăng do máu động mạch tiếp tục chảy vào", "ts"))
    return _fig(
        svg(680, 240, "".join(o), "Đồ thị đo thể tích bằng plethysmograph khí khi tắc tĩnh mạch"),
        "Hình 13.1 · Bản ghi điển hình từ plethysmograph khí trong lúc tắc tĩnh mạch, cho thấy sự thay "
        "đổi thể tích theo thời gian gây ra bởi dòng chảy vào của động mạch.",
        "Figure 13.1 · Typical recording from air plethysmograph during venous occlusion, revealing the "
        "changes in volume over time caused by arterial in-flow.",
        "Đồ thị thể tích theo thời gian: sau khi tắc tĩnh mạch, thể tích tăng lên do máu động mạch vẫn chảy "
        "vào, sau đó đạt giá trị bằng phẳng.",
        "A volume-vs-time plot: after venous occlusion the volume rises because arterial inflow continues, "
        "then reaches a plateau.")


# ---------------------------------------------------------------- 13.2
def fig_13_2():
    o = [_defs()]
    # limb as a horizontal cylinder segment
    o.append('<rect x="120" y="100" width="440" height="70" rx="35" fill="#f3f7f2" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(340, 92, "chi (limb)", "ts", "middle"))
    # four electrode bands
    ex = [180, 250, 410, 480]
    labels = [("I+", "cực cấp dòng ngoài"), ("V+", "cực đo áp trong"),
              ("V-", "cực đo áp trong"), ("I-", "cực cấp dòng ngoài")]
    for x, (tag, desc) in zip(ex, labels):
        o.append('<rect x="%d" y="92" width="10" height="86" rx="3" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x - 5, G))
        o.append(_lbl(x, 196, tag, "tb", "middle"))
    # current path outer, voltage inner
    o.append('<text class="ts" x="215" y="216">cấp dòng (outer)</text>')
    o.append('<text class="ts" x="430" y="216">đo áp (inner)</text>')
    o.append(_lbl(120, 250, "Hai điện cực ngoài cấp dòng; hai điện cực trong đo hiệu điện thế. Sự thay đổi "
              "trở kháng tỉ lệ với thể tích máu.", "ts"))
    return _fig(
        svg(680, 280, "".join(o), "Vị trí bốn điện cực trong đo trở kháng plethysmography"),
        "Hình 13.2 · Vị trí đặt điện cực cho plethysmography trở kháng dùng phát hiện sớm xơ vữa động mạch "
        "ngoại vi: hai điện cực ngoài cấp dòng còn hai điện cực trong đo hiệu điện thế.",
        "Figure 13.2 · Electrode positioning for impedance plethysmography used for early detection of "
        "peripheral atherosclerosis: the outer two supply current while the inner two measure voltage.",
        "Bốn điện cực băng quanh chi: hai ngoài cấp dòng điện, hai trong đo hiệu điện thế; sự thay đổi trở "
        "kháng dùng ước tính thể tích.",
        "Four electrodes around a limb: the outer pair drives current, the inner pair measures voltage; the "
        "impedance change estimates volume.")


# ---------------------------------------------------------------- 13.3
def fig_13_3():
    o = [_defs()]
    # thorax/neck region with 4 electrodes for stroke volume
    o.append('<path d="M150 120 Q340 60 530 120 L530 200 Q340 250 150 200 Z" fill="#f3f7f2" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(340, 100, "ngực / cổ", "ts", "middle"))
    ex = [210, 280, 400, 470]
    tags = ["I+", "V+", "V-", "I-"]
    for x, tag in zip(ex, tags):
        o.append('<rect x="%d" y="138" width="9" height="44" rx="3" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x - 4, G))
        o.append(_lbl(x, 196, tag, "tb", "middle"))
    o.append(_lbl(340, 230, "Bố trí tương tự Hình 13.2, dùng ước tính thể tích nhát bóp (stroke volume).", "ts", "middle"))
    return _fig(
        svg(680, 260, "".join(o), "Vị trí bốn điện cực ước tính thể tích nhát bóp"),
        "Hình 13.3 · Một ví dụ thứ hai về vị trí đặt điện cực cho plethysmography trở kháng, ở đây dùng để "
        "ước tính thể tích nhát bóp: hai điện cực ngoài cấp dòng, hai điện cực trong đo hiệu điện thế.",
        "Figure 13.3 · A second example of electrode positioning for impedance plethysmography, here used "
        "to estimate stroke volume: the outer two supply current while the inner two measure voltage.",
        "Bốn điện cực quanh ngực/cổ, bố trí như Hình 13.2, dùng ước tính thể tích nhát bóp.",
        "Four electrodes around the thorax/neck, arranged like Figure 13.2, used to estimate stroke volume.")


# ---------------------------------------------------------------- 13.4
def fig_13_4():
    o = [_defs()]
    # ellipsoid with three dimensions L, H, W
    cx, cy = 340, 130
    rx, ry, rz = 130, 70, 90  # x=width, y=height, z->depth
    # main ellipse (front view): width x height
    o.append('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="#faf6ef" stroke="%s" stroke-width="2"/>' % (cx, cy, rx, ry, E))
    # width dimension (horizontal)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>'
            % (_f(cx - rx), _f(cy + ry + 24), _f(cx + rx), _f(cy + ry + 24), S))
    o.append(_lbl(cx, cy + ry + 40, "chiều rộng W", "tb", "middle"))
    # height dimension (vertical)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>'
            % (_f(cx - rx - 24), _f(cy - ry), _f(cx - rx - 24), _f(cy + ry), S))
    o.append(_lbl(cx - rx - 30, cy, "cao H", "tb", "middle"))
    # length dimension (depth, dashed through center)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>'
            % (_f(cx), _f(cy), _f(cx + rx + 70), _f(cy - 30), S))
    o.append(_lbl(cx + rx + 40, cy - 44, "dài L", "tb"))
    # formula
    o.append(_lbl(360, 60, "V = (π/6) L H W   (hình ellipsoid)", "tb"))
    o.append(_lbl(360, 82, "tái tạo 3-D các mặt cắt ngang", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Ước tính thể tích tuyến tiền liệt từ mô hình ellipsoid"),
        "Hình 13.4 · Ước tính thể tích tuyến tiền liệt, thu được từ tái tạo 3-D các ảnh mặt cắt ngang, dùng "
        "các kích thước trong ba mặt phẳng: chiều dài, chiều cao và chiều rộng trong công thức thể tích mô "
        "tả hình ellipsoid.",
        "Figure 13.4 · Volume estimate of a prostate, obtained from 3-D reconstruction of cross-sectional "
        "images, using the dimensions in three planes: the length, height, and width in a volume formula "
        "describing an ellipsoid shape.",
        "Hình ellipsoid với ba kích thước L (dài), H (cao), W (rộng); thể tích V = (π/6)·L·H·W từ tái tạo "
        "3-D các mặt cắt ngang.",
        "An ellipsoid with length L, height H and width W; volume V = (π/6)·L·H·W from 3-D reconstruction "
        "of cross-sections.")


# ---------------------------------------------------------------- 13.5
def fig_13_5():
    o = [_defs()]
    # stacked transverse cross-section contours (irregular blobs) with step h
    x = 170
    step = 60
    ys = [190, 130, 70]
    for i, y in enumerate(ys):
        # irregular contour
        pts = [(x - 40, y), (x + 10, y - 26), (x + 46, y - 8), (x + 40, y + 24),
               (x - 6, y + 30), (x - 44, y + 14)]
        d = "M" + " L".join("%s %s" % p for p in pts) + " Z"
        o.append('<path d="%s" fill="#faf6ef" stroke="%s" stroke-width="1.8"/>' % (d, E))
        o.append(_lbl(x + 60, y, "mặt cắt %d" % (i + 1), "ts"))
    # step size arrow
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
            % (_f(x - 60), _f(ys[0]), _f(x - 60), _f(ys[2]), S))
    o.append(_lbl(x - 66, (ys[0] + ys[2]) / 2.0, "h = 4 mm", "tb", "end"))
    o.append(_lbl(380, 130, "Mỗi diện tích mặt cắt được cộng lại", "ts"))
    o.append(_lbl(380, 152, "sau khi nhân với bước h → tổng thể tích.", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Các đường bao mặt cắt ngang dùng đo thể tích bằng phương pháp planimetric"),
        "Hình 13.5 · Các đường bao của ảnh mặt cắt ngang tuyến tiền liệt dùng đo thể tích bằng phương pháp "
        "planimetric: các mặt cắt ngang thu được với bước 4 mm được một người quan sát chuyên gia vẽ bao, "
        "và đóng góp của mỗi mặt cắt vào tổng thể tích thu được bằng cách xác định diện tích giới hạn bởi "
        "đường bao.",
        "Figure 13.5 · Outlines of cross-sectional images of the prostate used for planimetric volumetry of "
        "the prostate: transverse cross-sections obtained with a step size of 4 mm have been outlined by an "
        "expert observer, and the contribution of each section to the total volume is obtained by determining "
        "the area enclosed by the prostate contour.",
        "Ba mặt cắt ngang cách nhau h = 4 mm, mỗi mặt cắt có đường bao không đều; diện tích từng mặt cắt "
        "nhân với h rồi cộng lại thành thể tích.",
        "Three transverse cross-sections spaced 4 mm apart, each outlined; the area of each is multiplied "
        "by the step and summed into the total volume.")


# ---------------------------------------------------------------- 13.6
def fig_13_6():
    o = [_defs()]
    cx, cy = 340, 130
    rx, ry = 130, 80
    o.append('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="#faf6ef" stroke="%s" stroke-width="2"/>' % (cx, cy, rx, ry, E))
    # probe axis through center at angle alpha
    a = math.radians(35)
    L = 170
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
            % (_f(cx - L * math.cos(a)), _f(cy + L * math.sin(a)), _f(cx + L * math.cos(a)), _f(cy - L * math.sin(a)), G))
    o.append(_lbl(cx + L * math.cos(a) + 6, cy - L * math.sin(a), "trục đầu dò (probe)", "ts"))
    # intersection distance h (perpendicular tick on axis)
    hx, hy = cx + rx * math.cos(a) * 0.6, cy - rx * math.sin(a) * 0.6
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
            % (_f(hx - 6), _f(hy - 10), _f(hx + 6), _f(hy + 10), E))
    o.append(_lbl(hx + 10, hy, "h", "tb"))
    # alpha arc at center
    o.append('<path d="M%s %s A 28 28 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="1"/>'
            % (_f(cx + 28), _f(cy), _f(cx + 28 * math.cos(a)), _f(cy - 28 * math.sin(a)), S))
    o.append(_lbl(cx + 34, cy - 18, "α", "tb"))
    o.append(_lbl(120, 220, "Mô hình ellipsoid: khoảng cách giao cắt h và góc quét α với trục đầu dò.", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Mô hình ellipsoid tuyến tiền liệt với khoảng cách giao cắt h và góc quét α"),
        "Hình 13.6 · Mô hình hình ellipsoid của tuyến tiền liệt dùng cho phân tích lý thuyết phương pháp đo "
        "thể tích planimetric. Thể hiện là khoảng cách giao cắt h và góc quét α với trục của đầu dò.",
        "Figure 13.6 · An ellipsoid-shaped model of the prostate that was used for theoretical analysis of "
        "planimetric volumetry. Indicated are the intersection distance h and the scan angle α with the axis "
        "of the probe.",
        "Hình ellipsoid với trục đầu dò theo góc α; khoảng cách giao cắt h dọc theo trục dùng trong phân "
        "tích sai số planimetric.",
        "An ellipsoid with the probe axis at angle alpha; the intersection distance h along the axis is "
        "used in the planimetric error analysis.")


# ---------------------------------------------------------------- 13.7
def fig_13_7():
    o = [_defs()]
    x0, y0, w, h = 90, 200, 500, 140
    o += _ax(x0, y0, w, h, "vị trí mặt cắt đầu (0…h)", "sai số (%)")
    # error curves for different step sizes: oscillating decaying with increasing amplitude for larger h
    styles = [(1.0, E), (0.6, S), (0.35, G)]
    for k, (amp, col) in enumerate(styles):
        pts = []
        for i in range(0, 101):
            x = x0 + w * i / 100.0
            xx = i / 100.0
            yv = amp * (0.35 * math.sin(xx * math.pi * (3 + k)) + 0.15 * math.sin(xx * math.pi * 7))
            y = y0 - h * 0.5 * (yv + 0.5)
            pts.append((x, y))
        d = "M" + " L".join("%s %s" % (_f(x), _f(y)) for x, y in pts)
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, col))
    o.append(_lbl(x0 + 10, y0 - h + 6, "h nhỏ", "ts"))
    o.append(_lbl(x0 + w - 70, y0 - h + 6, "h lớn", "ts"))
    o.append(_lbl(380, 50, "Sai số giảm khi bước h nhỏ hơn", "tb", "middle"))
    return _fig(
        svg(680, 250, "".join(o), "Sai số ước tính mặt phẳng theo bước h"),
        "Hình 13.7 · Các sai số trong ước tính mặt phẳng bằng tích phân số cho các bước h khác nhau, trình "
        "bày theo phần trăm của nghiệm chính xác, như một hàm của vị trí mặt cắt đầu nằm giữa 0 và h.",
        "Figure 13.7 · The errors in surface estimates by numerical integration for different step sizes h "
        "presented as percentage of the exact solution, as a function of the position of the first section, "
        "located between 0 and h.",
        "Đồ thị sai số (%) theo vị trí mặt cắt đầu cho ba bước h: bước nhỏ cho sai số nhỏ, bước lớn cho "
        "sai số lớn hơn.",
        "Error (%) versus first-section position for three step sizes; smaller h gives smaller error, larger "
        "h gives larger error.")


# ---------------------------------------------------------------- 13.8
def fig_13_8():
    o = [_defs()]
    x0, y0, w, h = 90, 200, 500, 140
    o += _ax(x0, y0, w, h, "thời gian t", "nồng độ C(t)")
    # indicator time-concentration curve: rise to peak then decay
    pts = []
    for i in range(0, 101):
        x = x0 + w * i / 100.0
        tt = i / 100.0
        c = (tt / 0.12) * math.exp(1 - tt / 0.12) if tt > 0 else 0
        y = y0 - h * min(1, c)
        pts.append((x, y))
    d = "M" + " L".join("%s %s" % (_f(x), _f(y)) for x, y in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, G))
    # shade area under curve
    area = "M%s %s " % (_f(x0), _f(y0)) + "L" + " ".join("%s %s" % (_f(x), _f(y)) for x, y in pts) + "L%s %s Z" % (_f(pts[-1][0]), _f(y0))
    o.append('<path d="%s" fill="%s" opacity="0.18"/>' % (area, G))
    o.append(_lbl(x0 + w * 0.5, y0 - h - 6, "diện tích = ∫ C(t) dt", "tb", "middle"))
    o.append(_lbl(380, 60, "Thể tích dòng thu được từ diện tích dưới đường cong nồng độ–thời gian", "ts", "middle"))
    return _fig(
        svg(680, 250, "".join(o), "Đường cong nồng độ–thời gian của chất chỉ thị"),
        "Hình 13.8 · Đường cong nồng độ–thời gian của chất chỉ thị dùng để thu được thể tích chưa biết của "
        "chất lỏng. Diện tích dưới đường cong nồng độ–thời gian cần thiết để ước tính tốc độ dòng thể tích.",
        "Figure 13.8 · The time-concentration curve of the indicator is used to obtain the unknown volume of "
        "the fluid. The area under the time-concentration curve is needed to estimate the volumetric flow rate.",
        "Đường cong nồng độ C(t) theo thời gian vươn tới đỉnh rồi giảm; diện tích dưới đường cong tỉ lệ với "
        "thể tích chất chỉ thị.",
        "The indicator concentration C(t) rises to a peak and decays; the area under the curve is proportional "
        "to the indicator volume.")


# ---------------------------------------------------------------- 13.9
def fig_13_9():
    o = [_defs()]
    # large tank with object, small overflow tank
    o.append('<rect x="90" y="90" width="200" height="160" rx="6" fill="#eef4f8" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="90" y="150" width="200" height="100" fill="#cfe3f0" stroke="none"/>')
    # object (sphere) lowered into large tank
    o.append('<circle cx="190" cy="130" r="34" fill="#fff" stroke="%s" stroke-width="2"/>' % G)
    o.append(_lbl(190, 64, "bồn lớn + vật", "ts", "middle"))
    o.append(_lbl(190, 270, "hạ vật xuống → nước tràn", "ts", "middle"))
    # arrow overflow to small tank
    o.append('<path d="M290 200 Q360 200 430 200" fill="none" stroke="%s" stroke-width="1.6" marker-end="url(#ah13)"/>' % E)
    # small tank
    o.append('<rect x="440" y="150" width="150" height="100" rx="6" fill="#cfe3f0" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(515, 140, "bồn nhỏ (tràn)", "ts", "middle"))
    o.append(_lbl(515, 270, "thể tích tràn = thể tích vật", "tb", "middle"))
    return _fig(
        svg(680, 300, "".join(o), "Phương pháp đo thể tích bằng thay thế nước (nước tràn)"),
        "Hình 13.9 · Tổng quan sơ đồ của một phương pháp đo thể tích dùng thay thế nước: thể tích cần đo của "
        "vật được biểu diễn bởi thể tích tràn trong bồn nhỏ sau khi hạ vật vào bồn lớn. Kỹ thuật này đặc "
        "biệt hữu ích cho các vật có hình dạng không đều đặn.",
        "Figure 13.9 · A schematic overview of a volume measuring method using water displacement: the desired "
        "volume of the object is represented by the overflow volume in the small tank after lowering the object "
        "into the large tank. This technique is especially useful for irregular-shaped objects.",
        "Vật được hạ vào bồn lớn, nước tràn sang bồn nhỏ; thể tích nước tràn chính là thể tích vật — thích hợp "
        "cho vật không đều đặn.",
        "Lowering the object into the large tank displaces water into the small tank; the overflow volume "
        "equals the object volume — good for irregular shapes.")


# ---------------------------------------------------------------- 13.10
def fig_13_10():
    o = [_defs()]
    # leg outline with horizontal disk slices
    leg = "M250 40 C300 60 300 120 285 170 C275 210 300 250 290 300"
    o.append('<path d="M210 40 C260 60 260 120 245 170 C235 210 260 250 250 300 '
            'L330 300 C320 250 345 210 335 170 C320 120 320 60 370 40 Z" '
            'fill="#f3f7f2" stroke="%s" stroke-width="2"/>' % E)
    # disk slices
    ys = [90, 140, 190, 240]
    for i, y in enumerate(ys):
        rw = 46 - i * 3
        o.append('<ellipse cx="292" cy="%d" rx="%d" ry="9" fill="none" stroke="%s" stroke-width="1.4"/>' % (y, rw, G))
        o.append(_lbl(360, y, "C%d, r%d" % (i + 1, rw), "ts"))
    o.append(_lbl(292, 330, "chân được chia thành các đoạn; mỗi đoạn coi như đĩa tròn có bán kính r", "ts", "middle"))
    o.append(_lbl(120, 60, "V = Σ π r² h", "tb"))
    return _fig(
        svg(680, 360, "".join(o), "Mô hình đĩa đo thể tích chân"),
        "Hình 13.10 · Minh hoạ mô hình đĩa để đo thể tích chân. Chân được chia thành các đoạn với một khoảng "
        "cách giao cắt cố định; chu vi của mỗi đoạn được xác định, sau đó dùng để mô tả chân như những hình "
        "tròn hoàn hảo với bán kính giả định tính được từ chu vi.",
        "Figure 13.10 · Illustration of the disk model to measure leg volume. The leg is divided in different "
        "sections with a fixed intersection distance; the circumference of each section is obtained. This "
        "circumference is then used to describe the leg as perfect circles with an assumed radius calculated "
        "from the circumference.",
        "Chân chia thành các lát; mỗi lát coi là đĩa tròn bán kính r tính từ chu vi, thể tích V = Σ π r² h.",
        "The leg is sliced into sections; each section is treated as a disk of radius r derived from its "
        "circumference, volume V = Σ π r² h.")


# expose
FIGS = [fig_13_1, fig_13_2, fig_13_3, fig_13_4, fig_13_5,
        fig_13_6, fig_13_7, fig_13_8, fig_13_9, fig_13_10]


def fig(n):
    return FIGS[n - 1]()
