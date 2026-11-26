# -*- coding: utf-8 -*-
"""Chapter 7, section 7.3 (continued): LCD field-effect display, gas-discharge,
liquid-vapour and electrophoretic displays, and the eleven-question exercise.

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 348-352, printed pp. 336-340, decoded
text lines 13440-13598.  Figures 7.28-7.32 are inserted in source order;
their labels were checked against work/ipc7_pages/p348.png ... p352.png.

The vector suppliers are authored in parallel.  Until they are importable the
five small redraws below are installed with non-overwriting ``hasattr`` guards,
so a real supplier callable is never replaced.
"""

import ipcfig7 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS

INK = "#1f3a5f"
GREY = "#777777"


# --------------------------------------------------------------- SVG helpers
def _t(x, y, s, size=7.4, anchor="middle", color=INK):
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx '
            'Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, anchor, size, color, s))


def _ln(x1, y1, x2, y2, color=INK, sw=1.1, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, color, sw, d))


def _poly(pts, color=INK, sw=1.4, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    p = " ".join("%.1f,%.1f" % (x, y) for x, y in pts)
    return ('<polyline points="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>' % (p, color, sw, d))


def _box(x, y, w, h, fill="#ffffff", color=INK, sw=1.1, rx=0, dash=""):
    r = ' rx="%s" ry="%s"' % (rx, rx) if rx else ""
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" '
            'stroke="%s" stroke-width="%s"%s%s/>'
            % (x, y, w, h, fill, color, sw, r, d))


def _dot(x, y, r=2.2, fill=INK):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
            % (x, y, r, fill))


def _mk(n, o, title, cvi, cen, avi, aen):
    o.append(_t(340, 245, "Hình 7.%d   ·   Figure 7.%d" % (n, n),
                6.4, color=GREY))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 7.%d · %s" % (n, cvi),
            "Figure 7.%d · %s" % (n, cen), avi, aen)


# --------------------------------------------------------- fallback figures
def _fig28():
    """Seven-segment liquid-crystal cell with a common terminal."""
    o = [_box(120, 35, 205, 170)]
    o.append(_t(222, 52, "a"))
    o.append(_t(216, 109, "f"))
    o.append(_t(287, 109, "b"))
    o.append(_t(222, 120, "g"))
    o.append(_t(216, 161, "e"))
    o.append(_t(287, 161, "c"))
    o.append(_t(222, 180, "d"))
    # Seven bar electrodes a-g.
    for y in (62, 111, 160):
        o.append(_box(170, y, 42, 6, fill="#223f66", sw=0))
    for x in (160, 222):
        for y in (69, 118):
            o.append(_box(x, y, 6, 38, fill="#223f66", sw=0))
    o.append(_t(222, 195, "Seven segment crystal", 6.8))
    o.append(_t(222, 203, "display unit", 6.8))
    # Terminals on the right, with simplified wiring.
    for lab, y, sx, sy in (("a", 52, 212, 65), ("b", 68, 225, 88),
                           ("c", 105, 225, 137), ("d", 122, 212, 163),
                           ("Common", 145, 160, 160), ("e", 170, 163, 137),
                           ("g", 190, 212, 114), ("f", 210, 163, 88)):
        o.append(_poly([(sx, sy), (465, sy), (465, y), (520, y)], sw=1.0))
        o.append(_t(526, y + 2.4, lab, 7.2, anchor="start"))
    return _mk(28, o, "Seven-segment LCD layout",
               "Bố trí LCD bảy đoạn", "Seven-segment crystal display unit",
               "Màn hình tinh thể lỏng bảy đoạn với điểm nối chung",
               "Seven-segment LCD with a common connection")


def _fig29():
    """Nixie tube: anode plate and ten digit-shaped cathodes 0-9."""
    o = [_box(110, 45, 460, 110, rx=48)]
    o.append(_ln(150, 78, 530, 78, sw=2.0))
    o.append(_poly([(330, 78), (338, 70), (346, 86), (354, 70),
                    (362, 86), (370, 70), (378, 78)]))
    o.append(_t(330, 42, "+", 9.0))
    _ar_label(o, 540, 76, "Anode")
    xs = [152 + 41 * i for i in range(10)]
    for i, x in enumerate(xs):
        o.append(_dot(x, 108, 2.4))
        o.append(_ln(x, 110, x, 129, sw=0.9))
        o.append(_t(x, 140, str(i), 7.4))
        o.append(_ln(x - 5, 133, x + 5, 127, sw=1.0))
    o.append(_poly([(140, 146), (140, 152), (528, 152), (528, 146)],
                   color=GREY, sw=0.8, dash="3,3"))
    o.append(_ln(158, 152, 158, 160, sw=1.0))
    for d in (4, 8, 12):
        o.append(_ln(158 - d / 2, 160, 158 + d / 2, 160, sw=1.0))
    o.append(_t(87, 108, "Cathodes", 7.4, anchor="start"))
    o.append(_poly([(145, 106), (120, 106)], sw=1.0))
    return _mk(29, o, "Nixie tube with ten cathodes",
               "Đèn Nixie với mười catốt", "Anode and digit cathodes 0-9",
               "Đèn Nixie có bản cực dương và mười catốt dạng chữ số 0-9",
               "Nixie tube with an anode and digit-shaped cathodes 0-9")


def _ar_label(o, x, y, text):
    o.append(_poly([(x - 34, y), (x - 8, y)], sw=1.0))
    o.append(_t(x - 4, y + 2.5, text, 7.4, anchor="start"))


def _fig30():
    """Fifteen-segment Nixie tube for decimal and alphabetic display."""
    o = [_box(245, 35, 190, 165, rx=42)]
    o.append(_box(270, 55, 140, 130, fill="#fbfcfe",
                  color=GREY, sw=0.8, dash="5,4"))
    # Seven straight segments of the familiar digit pattern.
    for x1, x2, y in ((292, 388, 70), (292, 388, 170)):
        o.append(_ln(x1, y, x2, y, sw=3.0))
    for x in (292, 388):
        o.append(_ln(x, 76, x, 112, sw=3.0))
        o.append(_ln(x, 128, x, 164, sw=3.0))
    o.append(_ln(292, 119, 388, 119, sw=3.0))
    # Eight diagonal segments forming the two half-X patterns.
    for x1, y1, x2, y2 in ((294, 72, 337, 117), (386, 72, 343, 117),
                           (294, 166, 337, 121), (386, 166, 343, 121),
                           (340, 72, 340, 117), (340, 121, 340, 166)):
        o.append(_ln(x1, y1, x2, y2, sw=2.4, color="#557199"))
    for x in (277, 292, 307, 322, 337, 352, 367, 382, 397):
        o.append(_ln(x, 200, x, 214, sw=1.2))
    o.append(_t(340, 27, "Fifteen-segment Nixie tube", 7.6))
    return _mk(30, o, "Fifteen-segment Nixie tube",
               "Đèn Nixie mười lăm đoạn", "Digits and alphabets, 15 segments",
               "Đèn Nixie mười lăm đoạn dùng cho chữ số và chữ cái",
               "Fifteen-segment Nixie tube for numerals and letters")


def _fig31():
    """Liquid-vapour display cell: rough glass, painted block and electrode."""
    o = [_box(250, 52, 180, 145)]
    o.append(_box(414, 56, 14, 137, fill="#26313c", sw=0))
    # Rough inner surface of the front glass.
    _wave(o, 263, 59, 137)
    o.append(_t(297, 209, "Rough glass surface", 6.8))
    o.append(_t(448, 128, "Painted block", 7.2, anchor="start"))
    o.append(_poly([(440, 126), (429, 126)], sw=1.0))
    # Transparent electrode immersed in the liquid, with supply Eb.
    o.append(_ln(397, 62, 397, 178, sw=2.0))
    o.append(_poly([(397, 62), (397, 36), (470, 36)]))
    o.append(_box(452, 30, 22, 12, fill="#ffffff", sw=1.0))
    o.append(_ln(474, 36, 512, 36, sw=1.0))
    o.append(_t(526, 39, "Eb", 7.8, anchor="start"))
    o.append(_ln(512, 36, 512, 70, sw=1.0))
    for d in (4, 8, 12):
        o.append(_ln(512 - d / 2, 70, 512 + d / 2, 70, sw=1.0))
    o.append(_t(402, 189, "Electrode", 6.8, anchor="start"))
    o.append(_poly([(402, 185), (396, 170)], sw=1.0))
    o.append(_t(206, 124, "Viewer", 7.4, anchor="start"))
    o.append(_poly([(252, 124), (270, 124)], sw=1.2))
    return _mk(31, o, "Liquid-vapour display cell",
               "Tế bào hiển thị lỏng-hơi",
               "Rough glass, liquid, electrode and dark background",
               "Tế bào hiển thị lỏng-hơi với kính nhám, điện cực và nền tối",
               "Liquid-vapour display cell with rough glass and electrode")


def _wave(o, x, y0, h):
    pts = [(x + (3 if i % 2 else 0), y0 + i * 7) for i in range(1, h // 7 + 1)]
    o.append(_poly(pts, color="#557199", sw=1.1))


def _fig32():
    """Electrophoretic display cell with pigment suspension and memory."""
    o = [_box(210, 50, 270, 145)]
    o.append(_ln(212, 55, 478, 55, sw=2.0))
    o.append(_t(500, 58, "Glass plate", 7.2, anchor="start"))
    o.append(_ln(212, 72, 478, 72, sw=2.0, color="#557199"))
    o.append(_t(500, 75, "Electrode (common)", 7.0, anchor="start"))
    for x in (232, 252, 272, 292, 312, 332, 352, 372, 392, 412, 432, 452):
        o.append(_dot(x, 84, 2.0))
    o.append(_t(168, 88, "Pigment", 7.0, anchor="start"))
    o.append(_t(168, 96, "particles", 7.0, anchor="start"))
    o.append(_poly([(213, 88), (227, 84)], sw=0.9))
    for y in (108, 122, 136):
        for x in (240, 268, 296, 324, 352, 380, 408, 436):
            o.append(_ln(x, y, x + 16, y, color=GREY, sw=0.8, dash="4,3"))
    o.append(_t(500, 126, "Liquid", 7.2, anchor="start"))
    o.append(_poly([(478, 126), (450, 126)], sw=0.9))
    for x in (232, 252, 272, 292, 312, 332, 352, 372, 392, 412, 432, 452):
        o.append(_dot(x, 176, 2.0))
    # Two separate bottom electrodes.
    o.append(_box(220, 181, 120, 8, fill="#d9e2ee", sw=1.0))
    o.append(_box(350, 181, 120, 8, fill="#d9e2ee", sw=1.0))
    o.append(_t(168, 193, "Electrodes", 7.0, anchor="start"))
    o.append(_poly([(213, 185), (218, 185)], sw=0.9))
    o.append(_t(330, 215, "Base", 7.2))
    o.append(_poly([(330, 205), (330, 191)], sw=1.0))
    # Bias supplies on both sides.
    o.append(_poly([(280, 189), (280, 205), (160, 205)]))
    o.append(_ln(160, 205, 160, 220, sw=1.0))
    for d in (4, 8, 12):
        o.append(_ln(160 - d / 2, 220, 160 + d / 2, 220, sw=1.0))
    o.append(_poly([(410, 189), (410, 205), (540, 205)]))
    o.append(_t(548, 208, "Eb", 7.8, anchor="start"))
    o.append(_ln(540, 205, 540, 220, sw=1.0))
    for d in (4, 8, 12):
        o.append(_ln(540 - d / 2, 220, 540 + d / 2, 220, sw=1.0))
    return _mk(32, o, "Electrophoretic display cell",
               "Tế bào hiển thị điện di", "Pigment particles in suspension",
               "Tế bào điện di với hạt màu lơ lửng giữa hai điện cực",
               "Electrophoretic cell with pigment particles between electrodes")


for _n, _fn in ((28, _fig28), (29, _fig29), (30, _fig30),
                (31, _fig31), (32, _fig32)):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, _fn)


# --------------------------------------------------------------------- prose
def section(lang):
    b = []

    # 7.3.3 continued - the seven-segment liquid-crystal display.
    P(b, lang,
      "Màn hình tinh thể lỏng thường có dạng hiển thị bảy đoạn với một điểm nối "
      "chung như thể hiện trong Hình 7.28. Mức tiêu thụ công suất của hệ thống "
      "hiển thị này thấp (1 µW cho mỗi centimet chiều dài) so với hệ thống "
      "hiển thị LED. Nó cũng có giá thành thấp hơn.",
      "Liquid crystal display is normally a seven segment type of display with a "
      "common connection as shown in Figure 7.28. Power consumption of this "
      "display system is low (1 microwatt per centimetre of length) in "
      "comparison to LED display system. This is also less costly.")
    FIG(b, 28, F.fig_f28(), lang)

    H(b, lang, "Ưu điểm của màn hình tinh thể lỏng (LCD)",
      "Advantages of liquid crystal display (LCD)", level=4)
    L(b, lang,
      ["Đây là thiết bị hoạt động ở điện áp thấp (tối đa 15 V), dòng điện thấp "
       "(nhỏ hơn 1 µA/cm² diện tích bề mặt) và công suất thấp (tối đa 1 µW/cm "
       "chiều dài).",
       "Khả năng nhìn của LCD tốt hơn LED ngay cả trong điều kiện ánh sáng môi "
       "trường kém.",
       "Đặc tính tiêu thụ công suất thấp của LCD làm cho nó hữu ích cho đồng hồ "
       "đeo tay và các thiết bị cầm tay nhỏ."],
      ["This is a low voltage (upto 15 volt), low current (less than 1 "
       "microampere/cm2 surface area) and low power (upto 1 microwatt/cm linear "
       "length) operated device.",
       "Visibility of LCD is superior to that of LED even in poor ambient light.",
       "Low power consumption characteristic of LCD makes it useful for watches "
       "and small portable instruments."], ordered=True)

    H(b, lang, "Nhược điểm", "Disadvantages", level=4)
    L(b, lang,
      ["Đây là một thiết bị rất chậm so với LED.",
       "Do sự suy biến hóa học, tuổi thọ của LCD bị hạn chế.",
       "Phạm vi nhiệt độ hoạt động chỉ từ 0 đến 60 °C."],
      ["This is a very slow device compared to LED.",
       "Due to chemical degeneration, life of LCD is limited.",
       "Operating range of temperature is from 0 to 60C only."], ordered=True)

    # 7.3.4 in the printed source is labelled (iii).
    H(b, lang, "(iii) Màn hình phóng điện khí",
      "(iii) Gas discharge-based display", level=4)
    P(b, lang,
      "Hệ thống hiển thị số quan trọng nhất dựa trên phóng điện khí là đèn Nixie "
      "(TM). Ống phóng điện khí được chứa khí trơ như neon. Có 10 catốt lạnh và "
      "một bản cực dương được lắp bên trong ống phóng điện như thể hiện trong "
      "Hình 7.29 (sơ đồ tiêu biểu của đèn Nixie).",
      "The most important digital display system based on the gas discharge is "
      "the Nixie (TM) tube. The gas discharge tube is filled with inert gas like "
      "neon. There are 10 numbers of cold cathodes and one anode plate installed "
      "inside the discharge tube as shown in Figure 7.29 (a representative "
      "diagram of Nixie tube).")
    FIG(b, 29, F.fig_f29(), lang)

    P(b, lang,
      "Các catốt nhìn có vẻ như những đốm nhỏ nhưng thực tế không phải vậy. "
      "Chúng được làm từ dây rất mảnh nhưng bền, được uốn theo hình các chữ số "
      "từ 0 đến 9 như thể hiện. Nguồn dương có điện áp cao hơn điện áp đánh thủng "
      "của khí neon (chứa trong đèn Nixie) được đặt vào. Khi công tắc của một "
      "catốt cụ thể được đóng, catốt đó phát sáng và chữ số tương ứng được hiển "
      "thị qua đèn Nixie. Khí neon có màu cam đặc trưng khi phát sáng. Trong "
      "điều kiện phát sáng, catốt đó sáng rực và chữ số trên catốt được thể hiện "
      "rõ ràng.",
      "The cathodes look like dots but it is not like that. It is made of very "
      "thin but strong wire wound in the shape of digits ranging from 0 to 9 as "
      "shown. The positive supply higher than the breakdown voltage of the Neon "
      "gas (filled in the Nixie tube) is applied. When a particular switch of "
      "the cathode is closed that cathode glows and the appropriate number or "
      "digit is displayed through the Nixie tube. Neon gas has characteristic "
      "colour of orange when it glows. Under the glowing condition, the "
      "particular cathode glows brightly and the digit on the cathode is "
      "indicated clearly.")

    P(b, lang,
      "Để hiển thị bảng chữ cái, nhà sản xuất ban đầu đã thiết kế một phiên bản "
      "khác của đèn Nixie gồm 15 đoạn như thể hiện trong Hình 7.30. Khi cần dùng "
      "màn hình cho cả chữ số thập phân lẫn chữ cái, đèn Nixie mười lăm đoạn "
      "được sử dụng.",
      "For indicating alphabet, another version of Nixie tube has been designed "
      "by the original manufacturer consisting of 15 segments as shown in "
      "Figure 7.30. When it is required to use the display for decimal as well "
      "as alphabets, the fifteen segment Nixie tube is employed.")
    FIG(b, 30, F.fig_f30(), lang)

    P(b, lang,
      "Yêu cầu điện áp nguồn để vận hành đèn Nixie cao hơn hầu hết các hệ thống "
      "hiển thị khác, lên tới 200 V một chiều. Tương tự, yêu cầu dòng điện cũng "
      "cao hơn một chút, lên tới 5 mA. Một đặc điểm quan trọng của hệ thống "
      "hiển thị đèn Nixie là chữ số có kích thước lớn, cao tới 30 mm.",
      "The supply voltage requirement for operating the Nixie tube is higher "
      "than most of the other display system being upto 200 volt D.C. Similarly, "
      "current requirement is also slightly higher being upto 5 milliampres. "
      "One important characteristic of Nixie tube display system is that the "
      "digits are of larger size being upto 30 millimetres in height.")

    # 7.3.5 in the printed source is labelled (iv).
    H(b, lang, "(iv) Màn hình dựa trên lỏng-hơi (LVD)",
      "(iv) Liquid vapour-based display (LVD)", level=4)
    P(b, lang,
      "Hệ thống hiển thị dựa trên lỏng-hơi là bổ sung mới nhất cho công nghệ "
      "hiển thị số. Cấu trúc gồm một chất lỏng trong suốt và dễ bay hơi được "
      "chứa giữa hai bản kính song song. Kính trước và kính sau được bịt kín "
      "bằng các miếng đệm thích hợp. Bề mặt bên trong của kính trước được làm "
      "nhám, trong khi bề mặt bên ngoài của kính sau được sơn màu đen để tạo "
      "nền tối. Chất lỏng tiếp xúc với bề mặt nhám sẽ làm ướt bề mặt kính. "
      "Chiết suất của kính và của chất lỏng tiếp xúc là như nhau. Một điện cực "
      "mỏng trong suốt nhúng trong chất lỏng được nung nóng bằng điện áp nguồn "
      "như thể hiện trong Hình 7.31.",
      "Liquid Vapour based display system is the latest addition to the digital "
      "display technology. The arrangement is consisting of a transparent and "
      "volatile liquid filled in between two parallel glass plates. The front "
      "and the rear glass are sealed with the help of suitable spacers. Internal "
      "surface of the front glass is made rough whereas the outer surface of the "
      "rear glass is painted black to provide dark background. The liquid in "
      "contact with the rough surface wets the glass surface. The refractive "
      "index of glass as well as that of the liquid in contact are same. A thin "
      "transparent electrode dipped inside the liquid is heated by supply "
      "voltage as shown in Figure 7.31.")
    FIG(b, 31, F.fig_f31(), lang)

    P(b, lang,
      "Khi không có điện áp đặt vào điện cực, kính sau với nền tối được nhìn "
      "thấy màu đen qua sự kết hợp của kính trước và chất lỏng. Khi điện áp được "
      "đặt vào điện cực, điện cực bị nung nóng, làm bắt đầu sự bay hơi của chất "
      "lỏng tiếp xúc với điện cực. Sự bay hơi tạo ra một màng hơi mỏng cùng với "
      "các bọt của nó quanh bề mặt nhám của kính. Vì chiết suất của hơi khác đi, "
      "xuất hiện sự không liên tục gần bề mặt tiếp giáp giữa bản kính và chất "
      "lỏng, dẫn đến tán xạ ánh sáng. Hiện tượng này được dùng để chế tạo thiết "
      "bị hiển thị. Hệ thống hiển thị chế tạo theo nguyên lý này tốt hơn thiết "
      "bị hiển thị dựa trên LCD.",
      "When there is no voltage applied to the electrode the rear glass with "
      "dark background is seen black through the front glass and the liquid "
      "combined. When the voltage is applied to the electrode, heating of "
      "electrode takes place resulting in starting of evaporation of the liquid "
      "that is in contact with the electrode. The evaporation presents thin "
      "vapour film as well as its bubble around the rough surface of the glass. "
      "Since the refractive index of the vapour is different, a discontinuity "
      "is seen near the interface of the glass plate and the liquid resulting in "
      "scattering of light. This action is utilized for making display device. "
      "The display system made on this principle is superior to LCD-based "
      "display device.")

    # 7.3.6 in the printed source is labelled (v).
    H(b, lang, "(v) Màn hình dựa trên EPI",
      "(v) EPI-based display", level=4)
    P(b, lang,
      "Nghiên cứu cho thấy khi một điện trường được đặt vào chất lỏng chứa các "
      "hạt màu lơ lửng, các hạt này sẽ tích điện và dẫn đến sự chuyển động của "
      "chúng. Hiện tượng này được gọi là điện di. Nguyên lý điện di được minh "
      "họa trong Hình 7.32. Như có thể thấy, dưới tác động của điện trường, các "
      "hạt màu mang điện di chuyển về một trong hai điện cực tùy theo cực tính "
      "của các hạt.",
      "Research has revealed that when an electric field is applied across a "
      "liquid having pigment particles in suspension gets charged and results in "
      "movement of these pigment particles. This is called electrophoresis. The "
      "principle of electrophoresis has been depicted in Figure 7.32. As is "
      "seen, under the influence of electric field, the charged pigment particles "
      "migrate towards either electrode depending upon the polarity of the "
      "charged particles.")
    FIG(b, 32, F.fig_f32(), lang)

    P(b, lang,
      "Chất lỏng (được nhuốm màu đen) được đặt giữa hai bản kính song song, một "
      "bản trong suốt và bản kia có khả năng phản xạ. Khi các hạt màu di chuyển "
      "do điện di, màu của ánh sáng phản xạ từ các hạt thay đổi, cho thấy khả "
      "năng thiết kế một hệ thống hiển thị.",
      "The liquid (coloured black) is placed in between two parallel glass "
      "plates, one glass being transparent and the other one being reflective. "
      "When the migration of pigment particles takes place electrophoretically, "
      "colour of reflected light of the particles changes indicating a potential "
      "for designing a display system.")

    P(b, lang,
      "Như thể hiện trong sơ đồ, điện cực chung trong suốt, còn điện cực kia "
      "được chia thành hai đoạn. Điện thế thay đổi được đặt vào các điện cực "
      "đoạn như đã chỉ ra. Nếu các hạt tích điện dương, chúng di chuyển về phía "
      "điện cực chung do điện áp dương được đặt vào đoạn, và các hạt có màu "
      "trắng khi nhìn từ phía người xem. Mặt khác, khi các hạt tích điện âm, "
      "việc đặt điện thế âm vào đoạn sẽ nhấn chìm các hạt vào dung dịch tối. "
      "Kết quả là ánh sáng phản xạ từ chất lỏng tối truyền tới người xem. Như "
      "vậy, ta thấy rằng khi kết hợp màu của dung dịch và màu của các hạt, có "
      "thể thu được một màn hình hiển thị dựa trên màu sắc.",
      "As shown in the diagram, the common electrode is transparent and the "
      "other electrode has been divided into two segments. Varying potential is "
      "applied to the segmented electrodes as indicated. If the particles get "
      "positively charged the movement is towards common electrode due to "
      "application of positive voltage upon the segment and the particles appear "
      "white when viewed from the viewers end. On the other hand, when the "
      "particles get negatively charged application of negative potential upon "
      "the segment immerses the particles into the dark suspension. As a result "
      "the reflection coming out of the dark liquid gets to the viewer. Thus, we "
      "observe that the colour of liquid suspension and the particles when "
      "combined together a display based on colour can be obtained "
      "successfully.")

    P(b, lang,
      "Người ta đã quan sát thấy rằng các hạt đã lắng đọng gần hoặc trên điện "
      "cực vẫn giữ nguyên ngay cả khi điện trường được loại bỏ. Phân tích hiện "
      "tượng này cho thấy khả năng thiết kế một phần tử nhớ tiềm năng.",
      "It has been observed that the particles which has been deposited near or "
      "upon the electrode remain unmoved even when the electric field is "
      "withdrawn. The analysis of this observation reveals possibility of design "
      "of a potential memory element.")

    # ---------------------------------------------------------- exercise
    H(b, lang, "Bài tập", "Exercise")
    L(b, lang,
      ["Máy ghi là gì? Vì sao cần một hệ thống ghi? Mô tả ngắn gọn hệ thống ghi "
       "dạng thế kế.",
       "Sự khác biệt giữa biểu đồ dải và biểu đồ xếp nếp là gì? Mô tả máy ghi "
       "biểu đồ tròn kèm sơ đồ.",
       "Mô tả hệ thống ghi từ tính với sự trợ giúp của một sơ đồ đơn giản. Đặc "
       "điểm đặc biệt của hệ thống ghi FM là gì?",
       "Máy ghi từ tính số hoạt động như thế nào? Sự khác biệt giữa cách ghi số "
       "tăng lượng và cách ghi số đồng bộ là gì?",
       "Máy vẽ X-Y là gì? Công dụng điển hình của nó là gì? Mô tả hoạt động của "
       "máy kèm sơ đồ.",
       "Mô tả máy ghi lập trình đa chức năng hiện đại với sự trợ giúp của sơ đồ "
       "khối đơn giản.",
       "Hệ thống ghi không giấy là gì? Nó có tốt hơn máy ghi biểu đồ bằng bút "
       "mực không? Thảo luận lập luận của bạn.",
       "Phân biệt hệ thống hiển thị LED và LCD theo các phương diện: (a) nguyên "
       "lý cấu tạo, (b) tốc độ đáp ứng, (c) kích thước vùng hiển thị, (d) khả "
       "năng nhìn, (e) mức tiêu thụ công suất.",
       "Nguyên lý cơ bản của hệ thống hiển thị lỏng-hơi (LVD) là gì? Có thể so "
       "sánh nó với hệ thống hiển thị LCD không?",
       "Nguyên lý cơ bản của hệ thống hiển thị dựa trên EPI là gì? Có thể so "
       "sánh nó với hệ thống hiển thị LED không?",
       "Mô tả hệ thống hiển thị dựa trên phóng điện khí dùng để hiển thị chữ và "
       "số. Phân biệt màn hình LCD tán xạ động và màn hình LCD hiệu ứng trường."],
      ["What is a recorder? What is the need of a recording system? Describe a "
       "potentiometric form of recording system in brief.",
       "What is the difference between strip chart and fanfold chart? Describe "
       "circular chart recorder with diagram.",
       "Describe magnetic recording system with the help of a simple diagram. "
       "What is the specialty of a FM recording system?",
       "How a digital magnetic recorder works? What is the difference between "
       "the incremental way and the synchronous way of digital recording?",
       "What is a X-Y recorder? What is its typical utility? Describe their "
       "functioning with the help of a diagram.",
       "Describe a modern multifunction programmable recorder with the help of "
       "a simple block diagram.",
       "What is paperless recording system? Is it superior to ink-pen-chart "
       "recorder? Discuss your logics.",
       "Differentiate between LED and LCD display system with respect to (a) "
       "Construction principle. (b) Speed of response (c) Size of display area "
       "(d) Visibility ( e) Power consumption.",
       "What is the basic principle of LV display system? Can it be compared to "
       "LCD display system?",
       "What is the basic principle of EPI-based display system? Is it "
       "comparable to EV display system.",
       "Describe gas discharge based display system for an alphanumeric "
       "display. Differentiate between dynamic scattering and field effect LCD "
       "system."], ordered=True)

    return b
