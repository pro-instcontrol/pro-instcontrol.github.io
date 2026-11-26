# -*- coding: utf-8 -*-
"""Chapter 7, section 7.1 "Recorders" with 7.1.1 and 7.1.2 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 329-333, printed pp. 317-321, decoded
text lines 12745-12914. Figures 7.1-7.7 are embedded in printed order;
Figure 7.8 opens the fanfold topic and belongs to the next section module,
so only its introductory sentence is translated here.

The `ipcfig7_a` supplier is authored in parallel with this module. Until it
is importable, small genuine vector redraws of the seven printed diagrams
are installed as non-overwriting fallbacks; once the real supplier
registers `fig_f01` ... `fig_f07`, those callables win.
"""

import ipcfig7 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _T(x, y, s, size=7.6, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _box(x, y, w, h, label, fill="#eef3fb", size=7.6):
    lines = str(label).split("\n")
    o = ['<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" '
         'stroke="#1f3a5f" stroke-width="1.1"/>' % (x, y, w, h, fill)]
    y0 = y + h / 2.0 - (len(lines) - 1) * size * 0.56 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(_T(x + w / 2.0, y0 + i * size * 1.15, ln, size))
    return "".join(o)


def _line(x1, y1, x2, y2, color="#1f3a5f", sw=1.2, dash=""):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="M%d %d L%d %d" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, color, sw, d))


def _ar(x1, y1, x2, y2, mid, color="#1f3a5f"):
    return ('<path d="M%d %d L%d %d" fill="none" stroke="%s" '
            'stroke-width="1.3" marker-end="url(#%s)"/>' % (x1, y1, x2, y2, color, mid))


def _circ(cx, cy, r=3.0, fill="#ffffff"):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" '
            'stroke="#1f3a5f" stroke-width="1.1"/>' % (cx, cy, r, fill))


def _standalone_fig(n):
    mid = "ipc7a%d" % n
    o = ['<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
         'markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>' % mid]

    if n == 1:
        cap_vi = "Máy ghi thế kế: vòng cân bằng tự động"
        cap_en = "Potentiometric recorder: the self-balancing loop"
        avi = ("Sơ đồ vòng cân bằng gồm thế kế, bộ chuyển đổi, bộ khuếch đại "
               "xoay chiều, mô-tơ servo và cuộn tham chiếu")
        aen = ("Null-balance loop with a potentiometer, converter, A.C. amplifier, "
               "servomotor and reference winding")
        o.append(_box(36, 28, 124, 46, "Potentiometer\nThế kế"))
        o.append('<path d="M56 70 A42 42 0 0 1 140 70" fill="none" '
                 'stroke="#1f3a5f" stroke-width="1.3"/>')
        o.append(_line(98, 71, 138, 51))
        o.append(_circ(98, 71, 2.4))
        o.append(_T(98, 92, "Unknown potential", 7.2))
        o.append(_line(58, 74, 58, 172))
        o.append(_line(122, 74, 122, 172))
        o.append(_circ(58, 175, 2.6))
        o.append(_circ(122, 175, 2.6))
        o.append(_box(198, 116, 78, 34, "Converter\nBộ chuyển đổi"))
        o.append(_line(122, 150, 198, 137))
        o.append(_line(140, 71, 300, 71))
        o.append(_line(140, 71, 286, 133))
        o.append(_box(326, 140, 94, 40, "A.C. amplifier\nBộ khuếch đại"))
        o.append(_ar(276, 137, 326, 151, mid))
        o.append(_circ(452, 96, 22, "#f7f9fc"))
        o.append(_circ(452, 96, 3.2))
        o.append(_T(452, 63, "A.C. servomotor", 7.2))
        o.append(_line(420, 160, 452, 118))
        o.append('<path d="M493 84 q14 -12 0 -24 M493 90 q14 -12 0 -24 '
                 'M493 96 q14 -12 0 -24" fill="none" stroke="#1f3a5f" '
                 'stroke-width="1.2"/>')
        o.append(_line(493, 72, 560, 72))
        o.append(_line(493, 96, 560, 96))
        o.append(_circ(562, 72, 2.4))
        o.append(_circ(562, 96, 2.4))
        o.append(_T(556, 60, "Reference winding", 7.2, anchor="end"))
        o.append(_line(160, 60, 430, 60, "#9aa7b8", 1.0, "5 4"))
        o.append(_T(295, 55, "Mechanical coupling", 7.2))
        o.append(_T(340, 200, "Wiper driven by the mechanical linkage", 7.0))

    elif n == 2:
        cap_vi = "Cơ chế biểu đồ tròn"
        cap_en = "Circular chart mechanism"
        avi = ("Biểu đồ tròn có thang 0 đến 100 và 0 đến 10, cần bút quay "
               "từ tâm quanh trục biểu đồ")
        aen = ("Circular chart with 0-100 and 0-10 scales and a pen arm "
               "pivoting about the chart hub")
        o.append(_circ(250, 112, 82, "#fbfaf7"))
        o.append(_circ(250, 112, 70))
        for k in range(13):
            import math
            a = -math.pi / 2.0 + k * math.pi / 6.0
            x1, y1 = 250 + 66 * math.cos(a), 112 + 66 * math.sin(a)
            x2, y2 = 250 + 78 * math.cos(a), 112 + 78 * math.sin(a)
            o.append(_line(x1, y1, x2, y2))
        o.append(_T(250, 44, "0", 7.0))
        o.append(_T(333, 115, "100 / 10", 7.0, anchor="end"))
        o.append(_circ(250, 112, 9, "#eef3fb"))
        o.append(_T(250, 115, "Hub", 6.8))
        o.append(_line(250, 112, 309, 74, "#1f3a5f", 2.4))
        o.append(_circ(309, 74, 3.0, "#1f3a5f"))
        o.append(_T(330, 66, "Pen arm and tip", 7.4, anchor="start"))
        o.append(_T(250, 208, "Linear 0-100 / square root 0-10", 7.4))
        o.append(_box(410, 70, 118, 36, "Chart drive motor\nMô-tơ dẫn động"))
        o.append(_ar(408, 88, 335, 108, mid))
        o.append(_T(469, 50, "One revolution in 24 hours", 7.2))

    elif n == 3:
        cap_vi = "Cơ cấu ghi biểu đồ tròn và cụm bút ghi"
        cap_en = "Circular chart recorder with pen mounting arrangement"
        avi = ("Vỏ máy, trục biểu đồ, khe thời gian và cụm ba cần A, B, C "
               "truyền chuyển động tới cần bút")
        aen = ("Casing, chart hub, time slots and levers A, B, C driving the "
               "pen arm over the chart")
        o.append(_box(150, 30, 250, 180, "", "#fbfaf7"))
        o.append(_T(275, 48, "Mounting arrangement for pen", 7.2))
        o.append(_circ(268, 134, 56))
        o.append(_circ(268, 134, 44))
        o.append(_circ(268, 134, 7, "#eef3fb"))
        for a in range(0, 360, 30):
            import math
            r = math.radians(a)
            o.append(_line(268 + 48 * math.cos(r), 134 + 48 * math.sin(r),
                           268 + 55 * math.cos(r), 134 + 55 * math.sin(r)))
        o.append(_line(268, 134, 312, 96, "#1f3a5f", 2.2))
        o.append(_circ(312, 96, 3.0, "#1f3a5f"))
        o.append(_T(330, 88, "A", 8.4, anchor="start"))
        o.append(_line(268, 134, 236, 92, "#1f3a5f", 1.8))
        o.append(_T(226, 86, "B", 8.4))
        o.append(_line(268, 134, 296, 88, "#1f3a5f", 1.8))
        o.append(_T(303, 82, "C", 8.4))
        o.append(_T(120, 80, "Measuring assembly", 7.2, anchor="start"))
        o.append(_ar(190, 78, 232, 94, mid))
        o.append(_T(120, 116, "Pen arm", 7.2, anchor="start"))
        o.append(_T(120, 150, "Time slots", 7.2, anchor="start"))
        o.append(_T(120, 184, "Recorder pen", 7.2, anchor="start"))
        o.append(_T(410, 78, "Base end point", 7.2, anchor="start"))
        o.append(_T(410, 112, "Chart hub", 7.2, anchor="start"))
        o.append(_T(410, 146, "Casing", 7.2, anchor="start"))
        o.append(_T(410, 180, "Pen lifting system", 7.2, anchor="start"))
        o.append(_T(275, 222, "Three levers transmit the measured motion", 7.2))

    elif n == 4:
        cap_vi = "Máy ghi biểu đồ dải lắp thẳng đứng"
        cap_en = "Strip chart recorder with vertical chart installation"
        avi = ("Giấy biểu đồ cuộn dài có thang kép 0 đến 100 và 1 đến 10, "
               "bút nối với hệ thống servo, hai con lăn giả và chủ động")
        aen = ("Long roll of chart with dual 0-100 and 1-10 scales, servo-driven "
               "pen, and dummy and active rollers")
        o.append(_box(190, 26, 210, 168, "", "#fbfaf7"))
        for i in range(1, 10):
            y = 38 + i * 16
            o.append(_line(190, y, 400, y, "#d8dee8", 0.6))
            o.append(_T(182, y + 2.4, str(i * 10), 6.8, anchor="end"))
            o.append(_T(408, y + 2.4, str(i), 6.8, anchor="start"))
        o.append(_T(200, 22, "linear", 6.8))
        o.append(_T(390, 22, "square root", 6.8, anchor="end"))
        o.append(_circ(190, 194, 9))
        o.append(_circ(400, 194, 9))
        o.append(_T(190, 214, "Active roller", 7.0))
        o.append(_T(400, 214, "Dummy roller", 7.0))
        o.append(_line(224, 138, 250, 110, "#1f3a5f", 2.0))
        o.append(_circ(250, 110, 3.0, "#1f3a5f"))
        o.append(_ar(250, 110, 286, 84, mid))
        o.append(_box(452, 96, 96, 32, "Ink reservoir\nBình mực", "#eef3fb"))
        o.append(_ar(450, 112, 292, 88, mid))
        o.append(_T(500, 74, "Connected to servo system", 7.2))
        o.append(_T(500, 152, "Pen tip", 7.2))
        o.append(_T(295, 236, "Vertical chart, horizontal rotation", 7.2))

    elif n == 5:
        cap_vi = "Máy ghi thế kế cỡ lớn với biểu đồ nằm ngang"
        cap_en = "Larger potentiometric recorder with horizontal chart"
        avi = ("Biểu đồ dải lắp nằm ngang, chuyển động quay theo phương thẳng "
               "đứng, được dẫn động bởi hai con lăn và hệ bánh răng")
        aen = ("Horizontal strip chart with vertical rotation, driven by two "
               "rollers and a gear train")
        o.append('<path d="M110 70 L570 58 L570 158 L110 170 Z" fill="#fbfaf7" '
                 'stroke="#1f3a5f" stroke-width="1.2"/>')
        for k in range(1, 9):
            x = 110 + k * 56
            o.append(_line(x, 67, x, 168, "#d8dee8", 0.6))
        o.append(_T(340, 48, "Chart paper with linear and square-root scales", 7.4))
        o.append('<path d="M150 120 q40 -22 80 0 t80 0 t80 0 t80 0" fill="none" '
                 'stroke="#1f3a5f" stroke-width="1.6"/>')
        o.append(_circ(112, 120, 12))
        o.append(_circ(568, 116, 12))
        o.append(_T(112, 194, "Dummy roller", 7.2))
        o.append(_T(568, 190, "Active roller", 7.2))
        o.append(_box(250, 190, 180, 34, "Chart drive motor and gear system", "#eef3fb"))
        o.append(_ar(268, 188, 160, 136, mid))
        o.append(_T(340, 236, "Horizontal chart, vertical rotation", 7.2))

    elif n == 6:
        cap_vi = "Bình mực nỉ sáu ngăn"
        cap_en = "Six-bucket felt ink-pad"
        avi = ("Bình mực nỉ có tiết diện tròn, gồm sáu ngăn chứa mực đánh số "
               "1 đến 6 cho máy ghi đa điểm")
        aen = ("Circular felt ink-pad with six ink-filled buckets numbered 1 to 6 "
               "for multi-point recorders")
        o.append(_circ(250, 105, 68, "#fbfaf7"))
        o.append(_circ(250, 105, 26, "#eef3fb"))
        o.append(_circ(250, 105, 4.0, "#1f3a5f"))
        import math
        for k in range(6):
            a = -math.pi / 2.0 + k * math.pi / 3.0
            bx, by = 250 + 44 * math.cos(a), 105 + 44 * math.sin(a)
            o.append(_circ(bx, by, 16, "#e7f0ea"))
            o.append(_T(bx, by + 2.6, str(k + 1), 7.4))
        o.append(_T(250, 198, "Felt Ink-Pad", 8.2))
        o.append(_T(250, 216, "Six colours absorbed in felt buckets", 7.2))
        o.append(_T(470, 96, "Circular cross-section", 7.6))
        o.append(_T(470, 122, "Bucket-like cavities cast inside", 7.6))
        o.append(_T(470, 148, "Felt saturated with ink", 7.6))

    elif n == 7:
        cap_vi = "Đầu bút hình tròn có các điểm tẩm mực"
        cap_en = "Circular pen-tip with impregnated points"
        avi = ("Đầu bút hình tròn có nhiều điểm nhọn dạng răng được tẩm mực "
               "bố trí quanh rìa để in dấu chấm")
        aen = ("Circular pen-tip whose rim carries pointed, ink-impregnated "
               "teeth for dot printing")
        o.append(_circ(250, 108, 52, "#fbfaf7"))
        o.append(_circ(250, 108, 7, "#eef3fb"))
        import math
        for k in range(6):
            a = k * math.pi / 3.0 - math.pi / 2.0
            bx, by = 250 + 52 * math.cos(a), 108 + 52 * math.sin(a)
            tx, ty = 250 + 70 * math.cos(a), 108 + 70 * math.sin(a)
            px, py = 250 + 62 * math.cos(a + 0.18), 108 + 62 * math.sin(a + 0.18)
            o.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" '
                     'stroke="#1f3a5f" stroke-width="1.5"/>'
                     % (bx, by, px, py, tx, ty))
            o.append(_T(250 + 36 * math.cos(a), 108 + 36 * math.sin(a) + 2.4,
                        str(k + 1), 7.4))
        o.append(_T(250, 198, "Circular Pen-Tip", 8.2))
        o.append(_T(250, 216, "Teeth on the periphery print dots", 7.2))
        o.append(_T(470, 100, "Ink absorbed by the felt", 7.6))
        o.append(_T(470, 126, "Points rotate with the tip", 7.6))

    else:  # pragma: no cover - only figures 1-7 use this fallback
        cap_vi = "Hình minh họa"
        cap_en = "Illustration"
        avi = aen = ""
        o.append(_box(240, 100, 200, 40, "Figure 7.%d" % n))

    o.append(_T(340, 244, "Hình 7.%d   ·   Figure 7.%d" % (n, n), 6.4,
                color="#9aa7b8"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250">'
           '<rect width="680" height="250" fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 7.%d · %s" % (n, cap_vi),
            "Figure 7.%d · %s" % (n, cap_en), avi, aen)


for _n in (1, 2, 3, 4, 5, 6, 7):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 7.1
    H(b, lang, "7.1 Máy ghi", "7.1 Recorders")

    # -------------------------------------------------------------- 7.1.1
    H(b, lang, "7.1.1 Biểu đồ dải, ghi từ tính và kỹ thuật số",
      "7.1.1 Strip Chart, Magnetic and Digital")
    P(b, lang,
      "Một thiết bị chỉ thị có khả năng ghi liên tục một biến số công nghệ "
      "được gọi là 'máy ghi'. Thiết bị này hoàn toàn khác với máy ghi băng "
      "thông thường dùng trong công nghiệp âm nhạc. Các máy ghi ghi liên tục "
      "sự biến đổi giá trị của các biến số cần được quan sát trong một khoảng "
      "thời gian xác định.",
      "An indicating instrument having facility for continuous recording of a "
      "process variable is known as a 'recorder'. This is quite different from "
      "a usual tape-recorder used in the music industry. Recording instruments "
      "record continuously the variation in the value of variables which are "
      "required to be observed for a definite period of time.")

    # -------------------------------------------------------------- 7.1.2
    H(b, lang, "7.1.2 Mô tả hệ thống", "7.1.2 Description of the System")
    P(b, lang,
      "Hệ thống ghi liên tục đã trải qua nhiều giai đoạn phát triển. Trước đây, "
      "người ta dùng các hệ thống ghi kiểu lệch hoặc cuộn dây di động, hoạt "
      "động trên nguyên lý cơ bản của thiết bị cuộn dây di động có nam châm "
      "vĩnh cửu. Tuy nhiên, các máy ghi này vẫn còn được dùng ở một số nhà máy "
      "công nghệ cũ, nhưng những hạn chế của thiết kế này do trở kháng đầu vào "
      "kém và độ nhạy thấp đang khiến chúng trở nên lỗi thời đối với các nhà "
      "máy công nghệ trong tương lai.",
      "Continuous recording system has passed through several phases of its "
      "development. Earlier deflection or moving coil type recording systems "
      "were in use which operated on the basic principle of permanent magnet "
      "moving coil instrument. These recorders, however, are still in use in "
      "some of the older process plants, but limitations imposed on this design "
      "due to inferior input impedance and poor sensitivity are making them "
      "obsolete for coming process plants.")
    P(b, lang,
      "Máy ghi thế kế, về cơ bản là hệ thống kiểu cân bằng, cải thiện hiệu "
      "năng tổng thể của hệ thống ghi. Nguyên lý hoạt động cơ bản giống như "
      "thế kế tự cân bằng, như thể hiện trong Hình 7.1. Điện thế chưa biết, "
      "tỉ lệ với biến số công nghệ được đo, được so sánh với điện thế chuẩn "
      "có sẵn trên thế kế. Điện thế lệch cân bằng thu được được chuyển đổi, "
      "khuếch đại và dùng để đưa thế kế tới một thiết lập mới nhờ cơ cấu liên "
      "kết cơ khí và cần quét chạy trên thế kế. Bộ khuếch đại là bộ khuếch đại "
      "hai tầng (tiền khuếch đại và bộ khuếch đại servo) để có tín hiệu mức "
      "cao hơn điều khiển động cơ servo. Chi tiết hơn về máy ghi này có trong "
      "Chương 3 của cuốn sách.",
      "Potentiometric recorder, which is basically a null type system, improves "
      "overall performance of the recording system. Basic operation is similar "
      "to self-balancing potentiometer as shown in Figure 7.1. The unknown "
      "potential which is proportional to a measured process variable is "
      "compared with respect to the standard potential available across the "
      "potentiometer. The resulting out of balance potential is converted, "
      "amplified and used to balance the potentiometer to a new setting by "
      "means of the mechanical linkage and wiper running on the potentiometer. "
      "The amplifier is a two-stage amplifier (preamplifier and servo-amplifier) "
      "to have a higher-level signal to operate the servomotor. Further details "
      "of this recorder are available in Chapter 3 of this book.")
    FIG(b, 1, F.fig_f01(), lang)

    P(b, lang,
      "Biểu đồ của máy ghi là một bộ phận quan trọng của hệ thống; nó được làm "
      "từ giấy chất lượng cao, được phủ hóa chất và được chế tạo đặc biệt để "
      "ghi các biến số công nghệ hoặc các biến số khác.",
      "The chart of the recorder being an important part of the system is made "
      "up of fine quality, chemically quoted paper especially fabricated for "
      "recording of process or other variables.")
    P(b, lang, "Biểu đồ chủ yếu có ba loại:",
      "The chart is of mainly three types:")
    L(b, lang,
      ["Biểu đồ tròn", "Biểu đồ dải", "Biểu đồ xếp nếp"],
      ["Circular chart", "Strip chart", "Fanfold chard."],
      ordered=True)
    P(b, lang,
      "Trong khi nguyên lý tác động cơ bản của máy ghi vẫn không đổi, cấu tạo "
      "vận hành của cơ chế ghi lại thay đổi theo loại biểu đồ.",
      "While the basic principle of actuation of the recorder remains the same "
      "the operational construction of recording mechanism changes according "
      "to the type of chart.")

    # ------------------------------------------------------- (i) circular
    H(b, lang, "(i) Biểu đồ tròn", "(i) Circular chart", level=4)
    P(b, lang,
      "Như tên gọi cho thấy, biểu đồ có dạng hình tròn, như thể hiện trong Hình "
      "7.2. Thang đo được chia tuyến tính từ 0 đến 100 để ghi các biến số tuyến "
      "tính, ví dụ áp suất, mức, v.v., và theo căn bậc hai từ 0 đến 10 để ghi "
      "biến số phi tuyến là Lưu lượng (Lưu lượng ∝ √Chênh áp). Thang đo của biểu "
      "đồ bắt đầu từ tâm (vạch 0) và kết thúc gần rìa (vạch 100 hoặc 10) của "
      "biểu đồ.",
      "As the name suggests, the chart is circular in shape as shown in Figure "
      "7.2. The scale is marked from 0 to 100 linear for recording of linear "
      "variables, e.g. pressure, level, etc. and 0 to 10 square root for "
      "recording of non-linear variable of Flow (Flow ∝ √Differential Pressure). "
      "The scale of the chart starts from the centre (0 mark) and ends near the "
      "periphery (100 or 10 marking) of the chart.")
    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Cần ghi của bút ghi được nối với cơ chế chỉ thị biến số công nghệ, và "
      "đầu bút đặt nhẹ nhàng lên biểu đồ (đối lại với tác động của một lò xo "
      "nhẹ). Bút được chứa mực khô chậm có chất lượng cao. Toàn bộ hệ thống ghi "
      "được vận hành bởi một mô-tơ dẫn động biểu đồ. Tốc độ của mô-tơ dẫn động "
      "biểu đồ này rất thấp; nó phải hoàn thành một vòng quay đầy đủ trong 24 "
      "giờ. Biểu đồ được đánh dấu từ 8 giờ sáng của một ngày đến 8 giờ sáng "
      "ngày hôm sau, tức là 24 giờ. Điều này có nghĩa là biểu đồ phải được thay "
      "sau mỗi 24 giờ. Đây là nhược điểm lớn nhất của hệ thống biểu đồ tròn, do "
      "đó hiện hệ thống này đã trở nên lỗi thời ở mức độ nhất định; dù vậy, "
      "một mô tả ngắn gọn về hệ thống máy ghi biểu đồ tròn vẫn được nêu ở đây "
      "để tham khảo học thuật.",
      "The recording pen arm is connected to the process variable indicating "
      "mechanism and the tip of the pen rests gently (against the action of a "
      "light spring) on the chart. The pen is filled with slow drying ink of "
      "higher quality. The entire recording system is run by a chart drive "
      "motor. The speed of this chart drive motor is very low. It has to "
      "complete one full revolution in 24 hours time. The chart is marked from "
      "8 A.M. of a particular day to 8 A.M. next day, i.e. 24 hours. This means "
      "the chart has to be replaced after every 24 hours. This is the greatest "
      "disadvantage of circular chart system and therefore has been more or "
      "less obsolete nowadays even then a brief description on circular chart "
      "recorder system is mentioned here for academic interest.")
    P(b, lang,
      "Cụm đo được nối cơ khí với cụm lắp đặt bút ghi để sự thay đổi của tín "
      "hiệu đo đầu vào có thể được biểu thị bằng cần bút, như thể hiện trong "
      "Hình 7.3. Biểu đồ được cố định trên một tấm phẳng đỡ và được giữ chặt "
      "bằng một kẹp lò xo. Toàn bộ cơ chế máy ghi được vận hành nhờ sự kết hợp "
      "của ba cần đòn bẩy gắn A, B và C, thực chất truyền chuyển động do tín "
      "hiệu đo đầu vào tạo ra tới hệ thống ghi.",
      "The measuring assembly is connected mechanically to the pen mounting "
      "arrangement so that change in measurement input can be indicated by the "
      "pen arm as shown in Figure 7.3. The chart is fixed on a supporting flat "
      "plate and is secured properly by a spring clip. The complete recorder "
      "mechanism is operated by means of a combination of three levers attached "
      "A, B and C which actually transmit the motion generated by the "
      "measurement input to the recorder system.")
    FIG(b, 3, F.fig_f03(), lang)

    # ---------------------------------------------------- (ii) strip chart
    H(b, lang, "(ii) Máy ghi biểu đồ dải", "(ii) Strip chart recorder", level=4)
    P(b, lang,
      "Hệ thống ghi biểu đồ dải là một dạng ghi đồ họa hoàn toàn khác biệt. "
      "Trong hệ thống này, một cuộn giấy biểu đồ dài đã in thang đo được cho "
      "quay liên tục. Ở một thiết kế máy ghi có kích thước 6″ × 3″, biểu đồ "
      "được lắp thẳng đứng và chuyển động quay được thực hiện theo phương "
      "ngang, như thể hiện trong Hình 7.4. Ở thiết kế máy ghi cỡ lớn khác (máy "
      "ghi thế kế), như thể hiện trong Hình 7.5, biểu đồ được lắp nằm ngang và "
      "chuyển động quay được thực hiện theo phương thẳng đứng. Biểu đồ được di "
      "chuyển nhờ hai con lăn và một hệ thống bánh răng dẫn động nối với mô-tơ "
      "dẫn động biểu đồ, như thể hiện trong các sơ đồ. Một trong hai con lăn "
      "được gọi là con lăn giả, chỉ dùng để nạp biểu đồ mới. Con lăn thứ hai, "
      "con lăn chủ động, được dùng để cuốn phần biểu đồ đã sử dụng sau khi quá "
      "trình ghi hoặc in kết thúc.",
      "Strip chart recording system is completely a different type of graphic "
      "recording system. In this system, a long roll of scale-printed chart "
      "paper is allowed to rotate continuously. In one design of recorder of "
      "size 6″ × 3″, the chart is installed vertically and the rotation is "
      "effected horizontally as shown in Figure 7.4. In the other design of "
      "recorder of larger sizes (potentiometer recorders) as shown in Figure "
      "7.5, the chart is installed horizontally and the rotation is effected "
      "vertically. The chart is moved with the help of two rollers and a drive "
      "gear system connected to a chart drive motor as shown in the diagrams. "
      "One of the rollers is called a dummy roller which is used only for "
      "loading the fresh chart. The second roller, the active roller, is used "
      "to wind the used part of the chart after recording or printing is over.")
    FIG(b, 4, F.fig_f04(), lang)
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Ở cách lắp biểu đồ thẳng đứng, thang đo được ghi kép, tức là một thang "
      "tuyến tính (0 đến 100) và thang còn lại theo căn bậc hai (0 đến 10). "
      "Điều này đúng với máy ghi kiểu khí nén. Ở máy ghi dựa trên bộ vi xử lý, "
      "nơi tuyến tính hóa là một phần của hệ thống điều hòa tín hiệu, không "
      "cần thang căn bậc hai hay bất kỳ ghi phi tuyến nào khác. Bút được chứa "
      "mực khô chậm do một bình chứa mực nhỏ cung cấp, như thể hiện trong sơ đồ.",
      "In the vertical installation of the chart, the marking is dual, i.e. "
      "one linear (0 to 100) and the other one square root (0 to 10). This is "
      "true for pneumatic type of recorder. In the microprocessor based "
      "recorder where linearisation is a part of signal conditioning system, "
      "the square root or any other non-linear marking is not required. The "
      "pen is filled with slow drying ink supplied by a small ink reservoir as "
      "shown in the diagram.")
    P(b, lang,
      "Ở một thiết kế khác của hệ thống kết hợp bình mực, người ta dùng một "
      "bút nỉ nhỏ được cấp một lượng mực dùng một lần cố định.",
      "In another design of ink-pad combination system, a small felt pen "
      "supplied with fixed amount of disposable ink is used.")
    P(b, lang,
      "Ở một thiết kế khác nữa, áp dụng cho máy ghi thế kế kiểu cân bằng đa "
      "điểm có cơ chế in dấu chấm, người ta dùng một bình mực với sáu màu khác "
      "nhau. Bình mực này có tiết diện tròn với sáu hình dạng nhỏ giống cái xô "
      "(được đúc bên trong) và được nhồi nỉ thấm đẫm mực. Mực được hấp thụ "
      "hoàn toàn bởi nỉ và sẵn sàng để sử dụng. Một bình mực nỉ sáu ngăn đã "
      "được thể hiện trong Hình 7.6.",
      "In yet another design which is applied in the case of multi-point null "
      "type of potentiometric recorder having dot printing mechanism, an "
      "ink-pad of six different colours are used. This ink-pad is of circular "
      "cross-section having six small, bucket-like shape (casted inside) and "
      "is filled with felt which is full of ink. The ink is completely absorbed "
      "by the felt and is ready to be used. A six bucket felt ink-pad has been "
      "shown in Figure 7.6.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Bút dùng cho bình mực này có cấu trúc đặc biệt, như thể hiện trong Hình "
      "7.7. Đây là một đầu bút hình tròn, trên bề mặt có nhiều điểm được tẩm "
      "mực, có dạng răng nhọn và được bố trí ở rìa của vòng tròn. Mô-tơ dẫn "
      "động biểu đồ của máy ghi 6″ × 3″ có tốc độ 1/3 vòng trong một giờ, trong "
      "khi đối với máy ghi thế kế cỡ lớn, tốc độ của mô-tơ dẫn động biểu đồ có "
      "thể chọn bằng công tắc.",
      "The pen used for this ink-pad is of peculiar construction as shown in "
      "Figure 7.7. This is a circular pen-tip and number of points are "
      "impregnated on the surface having pointed teeth-like shape and put on "
      "the periphery of the circle. The chart drive motor for 6″ × 3″ recorder "
      "is having speed of 1/3 revolution in one hour whereas for larger size "
      "potentiometric recorder the speed of the chart drive motor is switch "
      "selectable.")
    FIG(b, 7, F.fig_f07(), lang)

    # --------------------------------------------------- (iii) fanfold chart
    H(b, lang, "(iii) Biểu đồ xếp nếp", "(iii) Fanfold chart", level=4)
    P(b, lang,
      "Ở loại này, giấy biểu đồ được gấp theo một hình dạng thiết kế cho cả hai",
      "In this type, the chart paper is folded according to a designed shape "
      "for both")

    return b
