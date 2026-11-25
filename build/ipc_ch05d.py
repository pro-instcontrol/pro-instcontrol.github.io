# -*- coding: utf-8 -*-
"""Chapter 5, section 5.3.2 "Data Conversion (ADC and DAC)" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 255-258, printed pp. 243-246, decoded
text lines 9687-9863.  Covers the four ADC techniques named in the text but
fully described here only for the ramp, integrating and potentiometer types:
Figures 5.19-5.24.  The successive-approximation detail and its Figures
5.25-5.26 continue in the next source block and belong to the following
module.  The single printed formula (integrator output) is reproduced as an
unnumbered equation; the source has no tables, so none are invented.

The printed diagrams are images in the PDF.  The `ipcfig5_b` and `ipcfig5_c`
suppliers are authored in parallel with this prose module.  Until those
suppliers register `fig_f19` .. `fig_f24`, simple vector redraws are installed
as non-overwriting fallbacks; the real callables always win.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _t(x, y, s, size=7.2, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _r(x, y, w, h, fill="#eef3fb"):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
            'stroke="#1f3a5f" stroke-width="1.1"/>' % (x, y, w, h, fill))


_MID = "ipc5d"


def _defs():
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>'
            % _MID)


def _w(pts, arrow=False, dash=False):
    d = "M" + " L".join("%g %g" % p for p in pts)
    m = ' marker-end="url(#%s)"' % _MID if arrow else ""
    da = ' stroke-dasharray="3 2"' if dash else ""
    return ('<path d="%s" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.1"%s%s/>' % (d, da, m))


def _node(x, y):
    return '<circle cx="%d" cy="%d" r="2.2" fill="#1f3a5f"/>' % (x, y)


_FIG_TEXT = {
    19: ("Giản đồ chuyển đổi điện áp sang thời gian",
         "Voltage to time conversion diagram",
         "Điện áp dốc bắt đầu ở +12 V, cắt mức điện áp chưa biết tại điểm "
         "trùng nhau rồi giảm về −12 V; cổng mở trong khoảng thời gian t để "
         "các xung nhịp đi qua",
         "A ramp starts at +12 V, crosses the unknown voltage level at the "
         "point of coincidence and falls to −12 V; the gate opens for time t "
         "so that clock pulses pass through"),
    20: ("Bộ chuyển đổi ADC kiểu dốc",
         "Ramp type ADC block diagram",
         "Bộ so sánh đầu vào và bộ so sánh nối đất điều khiển cổng; bộ dao "
         "động xung nhịp, cổng, bộ đếm và đầu ra nằm trên đường tín hiệu; bộ "
         "đa hồi tần số lấy mẫu khởi động bộ phát dốc và đặt lại bộ đếm",
         "The input comparator and the ground comparator control the gate; "
         "clock oscillator, gate, counter and output lie on the signal path; "
         "the sample rate multivibrator starts the ramp generator and resets "
         "the counter"),
    21: ("Đồ thị mức điện áp đầu vào", "Input voltage level graph",
         "Ba mức điện áp đầu vào không đổi Ei1, Ei2 và Ei3 được vẽ theo thời gian",
         "Three constant input voltage levels Ei1, Ei2 and Ei3 are drawn "
         "against time"),
    22: ("Đồ thị mức điện áp đầu ra", "Output voltage level graph",
         "Đầu ra của bộ tích phân gồm các dốc đi xuống từ gốc tọa độ; điện áp "
         "đầu vào càng cao thì độ dốc càng lớn",
         "The integrator output consists of descending ramps from the origin; "
         "a higher input voltage gives a steeper slope"),
    23: ("Mạch chuyển đổi điện áp sang tần số",
         "Voltage to frequency conversion circuit",
         "Tín hiệu Ei đi qua bộ tích phân, bộ phát hiện mức và cổng bộ phát "
         "xung; xung phản hồi được trừ vào đầu vào, còn cổng chính cho xung "
         "tới bộ đếm và bộ chỉ thị",
         "Ei passes through an integrator, a level detector and a pulse "
         "generator gate; a feedback pulse opposes the input while the main "
         "gate feeds pulses to the counter and indicator"),
    24: ("Mạch chiết áp tự cân bằng",
         "Self-balancing potentiometer circuit",
         "Điện áp chưa biết và điện áp tham chiếu vào bộ chiết áp chính xác; "
         "điện áp sai số đi qua bộ chuyển đổi một chiều sang xoay chiều, bộ "
         "khuếch đại sơ, bộ khuếch đại servo và hệ thống cân bằng servo, được "
         "nối cơ khí với dây trượt và bộ đếm cơ điện",
         "The unknown and reference voltages feed a precision potentiometer; "
         "the error voltage passes through a DC to AC converter, preamplifier, "
         "servo-amplifier and servo balancing system, mechanically coupled to "
         "the slide wire and an electromechanical counter"),
}


def _standalone_fig(n):
    o = [_defs()]

    if n == 19:
        for yy, lab in ((48, "+12 V"), (74, "Unknown voltage"),
                        (112, "0"), (154, "−12 V")):
            o += [_w([(120, yy), (520, yy)], dash=True),
                  _t(112, yy + 3, lab, 7.0, anchor="end")]
        o += [_w([(180, 48), (300, 154), (410, 48)]),
              _t(180, 40, "Start instant of measurement", 7.0),
              _node(180, 48), _node(232, 74),
              _t(250, 68, "Point of coincidence", 7.0, anchor="start"),
              _t(420, 120, "Ramp voltage", 7.0, anchor="start"),
              _w([(180, 48), (180, 190)], dash=True),
              _w([(300, 154), (300, 190)], dash=True),
              _w([(232, 74), (232, 186)], dash=True),
              _t(210, 178, "Time for gating t", 7.0),
              _w([(180, 186), (300, 186)]),
              _node(180, 186), _node(300, 186),
              _t(150, 205, "Clock pulse", 7.0, anchor="start")]
        for xx in range(195, 297, 16):
            o.append(_w([(xx, 203), (xx, 213)]))
        o.append(_w([(120, 213), (520, 213)]))

    elif n == 20:
        o += [_t(55, 48, "Signal input after conditioning", 6.8,
                 anchor="start"),
              _w([(60, 54), (140, 70)], True),
              _r(140, 55, 95, 34),
              _t(187, 76, "Input comparator", 7.0),
              _w([(235, 72), (320, 72)], True),
              _r(320, 56, 60, 32), _t(350, 76, "Gate", 7.5),
              _w([(380, 72), (440, 72)], True),
              _r(440, 56, 70, 32), _t(475, 76, "Counter", 7.5),
              _w([(510, 72), (555, 72)], True),
              _t(560, 76, "Output", 7.0, anchor="start"),
              _r(40, 118, 95, 32), _t(87, 138, "Clock oscillator", 7.0),
              _w([(135, 134), (320, 82)], True),
              _r(40, 162, 95, 32), _t(87, 182, "Sample rate", 7.0),
              _t(87, 193, "multivibrator", 7.0),
              _r(180, 160, 95, 32), _t(227, 180, "Ramp generator", 7.0),
              _w([(135, 178), (180, 176)], True),
              _r(310, 160, 95, 32), _t(357, 180, "Ground comparator", 7.0),
              _w([(275, 176), (310, 176)], True),
              _w([(357, 176), (357, 160)]),
              _t(357, 155, "ground", 6.6),
              _w([(405, 176), (350, 90), (350, 88)], True),
              _t(300, 120, "Start pulse", 6.6),
              _t(330, 148, "Stop pulse", 6.6),
              _w([(87, 160), (87, 215), (475, 215), (475, 88)], True)]

    elif n == 21:
        o += [_t(105, 48, "Input voltage level", 7.0, anchor="start"),
              _w([(105, 58), (105, 185)], True),
              _w([(105, 185), (520, 185)], True),
              _t(100, 200, "O", 7.5),
              _t(510, 200, "Time", 7.0, anchor="end")]
        for yy, lab in ((85, "Ei3"), (120, "Ei2"), (155, "Ei1")):
            o += [_w([(115, yy), (470, yy)]),
                  _t(480, yy + 3, lab, 7.5, anchor="start")]

    elif n == 22:
        o += [_t(430, 40, "Time", 7.0, anchor="start"),
              _w([(170, 45), (520, 45)], True),
              _w([(170, 45), (170, 195)], True),
              _t(160, 60, "O", 7.5, anchor="end"),
              _t(100, 70, "Output voltage", 7.0, anchor="start"),
              _t(100, 82, "level", 7.0, anchor="start")]
        for k, lab in enumerate(("Eo3", "Eo2", "Eo1")):
            x2 = 300 + k * 80
            y2 = 185 - k * 42
            o += [_w([(170, 45), (x2, y2)], True),
                  _t(x2 + 8, y2 + 3, lab, 7.2, anchor="start")]

    elif n == 23:
        o += [_t(55, 52, "Ei", 8.0, anchor="start"),
              _w([(75, 55), (150, 55)], True),
              _r(150, 38, 100, 34), _t(200, 59, "Integrator", 7.2),
              _t(258, 52, "Eo", 7.5),
              _w([(250, 55), (310, 55)], True),
              _r(310, 38, 110, 34), _t(365, 59, "Level detector", 7.2),
              _w([(365, 72), (365, 108), (300, 108)], True),
              _r(150, 92, 110, 34),
              _t(205, 113, "Pulse generator", 7.2),
              _w([(150, 109), (87, 109)], True),
              _r(400, 92, 105, 34),
              _t(452, 113, "Clock oscillator", 7.2),
              _w([(400, 109), (265, 109)], True),
              _t(290, 130, "Pulse generator gate", 6.8),
              _w([(365, 108), (365, 132), (365, 146)], True),
              _w([(452, 126), (452, 146), (365, 146)], True),
              _r(300, 146, 130, 30),
              _t(365, 165, "Time base selection", 7.0),
              _w([(365, 176), (365, 190), (270, 190)], True),
              _r(180, 176, 95, 28),
              _t(227, 194, "Start/stop gate", 7.0),
              _w([(180, 190), (130, 190), (130, 155)], True),
              _w([(87, 109), (87, 148), (112, 148)], True),
              _t(120, 143, "Main gate", 6.8),
              _w([(112, 152), (112, 205)], True),
              _r(150, 190, 80, 30), _t(190, 209, "Counter", 7.5),
              _w([(230, 205), (270, 205)], True),
              _r(270, 190, 90, 30), _t(315, 209, "Indicator", 7.5),
              _w([(452, 176), (452, 205), (360, 205)], True)]

    else:  # n == 24
        o += [_r(40, 145, 135, 38),
              _t(107, 161, "Precision", 7.2),
              _t(107, 174, "potentiometer circuit", 7.0),
              _w([(40, 156), (25, 156), (25, 130), (40, 130)], True),
              _t(20, 124, "Unknown", 6.6, anchor="start"),
              _t(20, 136, "voltage", 6.6, anchor="start"),
              _w([(175, 164), (215, 164)], True),
              _t(195, 156, "Reference", 6.6),
              _t(195, 178, "voltage", 6.6),
              _r(220, 145, 85, 38), _t(262, 168, "Error voltage", 7.2),
              _w([(305, 164), (335, 164)], True),
              _r(335, 145, 95, 38), _t(382, 161, "Converter", 7.2),
              _t(382, 174, "DC to AC", 7.0),
              _w([(430, 164), (465, 164)], True),
              _r(465, 145, 85, 38), _t(507, 168, "Preamplifier", 7.2),
              _w([(262, 145), (262, 92), (335, 92)], True),
              _r(335, 76, 95, 34), _t(382, 97, "Servo-amplifier", 7.2),
              _w([(430, 93), (505, 93)], True),
              _r(505, 76, 120, 34),
              _t(565, 92, "Servo balancing", 7.2),
              _t(565, 104, "system", 7.2),
              _w([(565, 76), (565, 42)], True),
              _r(470, 15, 190, 28),
              _t(565, 33, "24 V DC electromechanical counter", 6.8),
              _w([(505, 132), (565, 132), (565, 110)], dash=True),
              _t(420, 128, "Mechanical coupling with slide-wire", 6.6)]

    cvi, cen, avi, aen = _FIG_TEXT[n]
    o.append(_t(340, 242, "Hình 5.%d   ·   Figure 5.%d" % (n, n),
                6.4, color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 5.%d · %s" % (n, cvi),
            "Figure 5.%d · %s" % (n, cen), avi, aen)


for _n in range(19, 25):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # -------------------------------------------------------------- 5.3.2
    H(b, lang, "5.3.2 Chuyển đổi dữ liệu (ADC và DAC)",
      "5.3.2 Data Conversion (ADC and DAC)")

    P(b, lang,
      "Hầu hết các đầu vào của quá trình đo về cơ bản được hình thành dưới "
      "dạng tương tự và không cần chuyển đổi dữ liệu nếu hệ thống thiết bị đo "
      "thuộc kiểu tương tự, ví dụ hiển thị, ghi hoặc điều khiển. Nhưng nếu hệ "
      "thống thiết bị đo và điều khiển mang tính chất số thì các tín hiệu đo "
      "tương tự phải được chuyển sang dạng số để thuận tiện cho việc hiển thị, "
      "ghi và điều khiển số trong hệ thống thông thường. Ngoài ra, các tín "
      "hiệu thu được này có thể được xử lý hiệu quả qua hệ thống máy tính cho "
      "các chức năng điều khiển tiên tiến.",
      "Most of the measurement process inputs are basically formed in analog "
      "form and do not need any data conversion if the system of "
      "instrumentation is of analog type, e.g. indication, record or control. "
      "But if the system of instrumentation and control is of digital nature "
      "then the analog measurement signals have to be converted into digital "
      "form for facilitating digital indication, record and control in the "
      "conventional system. Also the signals so obtained can be processed "
      "effectively through computer system for advanced control functions.")

    P(b, lang,
      "Hệ thống chuyển đổi tương tự - số (ADC) dùng bốn kỹ thuật khác nhau:",
      "An analog-to-digital conversion (ADC) system employs four different "
      "techniques:")

    L(b, lang,
      ["Kiểu dốc",
       "Kiểu tích phân",
       "Kiểu chiết áp hay kiểu cân bằng liên tục",
       "Kiểu xấp xỉ liên tiếp"],
      ["Ramp type",
       "Integrating type",
       "Potentiometer type or continuous balance type",
       "Successive approximation type"], ordered=True)

    # ------------------------------------------------------- ramp type ADC
    H(b, lang, "1. Bộ chuyển đổi ADC kiểu dốc",
      "1. Ramp type ADC conversion", level=3)

    P(b, lang,
      "Ở kiểu này, khoảng thời gian mà một điện áp chuẩn kiểu dốc mất để "
      "thay đổi từ mức điện áp đầu vào về mức không được đo bằng một bộ đếm "
      "khoảng thời gian điện tử.",
      "In this type, the time interval that a ramp type standard voltage will "
      "take to change from an input voltage level to its zero level is "
      "measured by an electronic time interval counter.")

    P(b, lang,
      "Như Hình 5.19 cho thấy, một điện áp dốc chủ động khi đưa vào mạch đo "
      "được so sánh liên tục với điện áp chưa biết cần đo. Khi điện áp dốc lần "
      "đầu trùng với điện áp đầu vào, bộ so sánh đầu vào phát một xung để mở "
      "cổng như Hình 5.20.",
      "As shown in Figure 5.19, an active ramp voltage when applied to the "
      "measurement circuit is continuously compared with respect to the "
      "unknown voltage to be measured. When the ramp voltage first coincides "
      "with the input voltage, an input comparator initiates a pulse to open "
      "the gate as shown in Figure 5.20.")

    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang,
      "Khi điện áp dốc (trong lúc giảm) đạt đến mức không của điện áp đầu vào, "
      "bộ so sánh nối đất phát một xung và đóng cổng. Khoảng thời gian giữa "
      "lúc mở và đóng cổng là t, và đây là khoảng thời gian mà các xung do bộ "
      "dao động xung nhịp tạo ra đi qua cổng được đếm và hiển thị dưới dạng "
      "điện áp số. Bộ dao động đa hồi tần số lấy mẫu xác định nhịp khởi động "
      "của chu kỳ đo. Mạch tần số lấy mẫu đồng thời khởi động bộ phát dốc và "
      "đặt lại các bộ đếm.",
      "When the ramp voltage (while decreasing) reaches zero level of the "
      "input voltage, the ground comparator initiates a pulse and closes the "
      "gate. The time between opening and closing of the gate is t and this "
      "is the interval during which whatever pulses, generated by clock "
      "oscillator, pass through the gate are counted and displayed as voltage "
      "in digital form. The sample rate multivibrator determines the rate of "
      "initiation of measurement cycle. The sample rate circuit simultaneously "
      "initiates starting of the ramp generator as well as resetting of "
      "counters.")

    FIG(b, 20, F.fig_f20(), lang)

    # ---------------------------------------------------- integrating type
    H(b, lang, "2. Bộ chuyển đổi ADC kiểu tích phân",
      "2. Integrating type ADC conversion", level=3)

    P(b, lang,
      "Như ta đã biết, mạch ADC kiểu dốc lấy mẫu giá trị đầu vào vào cuối chu "
      "kỳ đo, trong khi mạch kiểu tích phân lại đo giá trị trung bình của đầu "
      "vào trong một chu kỳ đo cố định. Kỹ thuật dùng ở đây là chuyển đổi điện "
      "áp sang tần số, hoạt động như một hệ thống điều khiển phản hồi điều "
      "chỉnh tốc độ phát xung theo độ lớn của điện áp tín hiệu đầu vào. Thực "
      "chất, tần số của các xung được tạo ra phụ thuộc vào điện áp đầu vào Ei "
      "cần đo. Vì vậy, số xung xuất hiện trong một khoảng thời gian xác định "
      "được đếm và là biểu thị của điện áp đầu vào dưới dạng số. Bộ khuếch đại "
      "thuật toán dùng trong kỹ thuật này đóng vai trò bộ tích phân, và đầu ra "
      "Eo của bộ tích phân được cho bởi phương trình:",
      "As we know that the ADC conversion employing ramp type circuit samples "
      "the input value at the end of measurement period, the integrating type "
      "circuit, on the other hand, measures the average value of the input "
      "over a fixed measurement period. The technique employed here is the "
      "voltage to frequency conversion which works as a feedback control "
      "system governing rate of pulse generation with respect to magnitude of "
      "input signal voltage. In effect the frequency of the generated pulses "
      "depends upon the input voltage Ei to be measured. Therefore, number of "
      "pulses appearing during a definite interval is counted and is the "
      "indication of input voltage in digital form. Operational amplifier "
      "used in this technique acts as an integrator and the output Eo of the "
      "integrator is given by the equation:")

    E(b, lang, "Eo = −Ei × (1/RC) × t", "Eo = −Ei × (1/RC) × t", num="")

    P(b, lang,
      "Phương trình này mô tả rằng với một đầu vào điện áp không đổi, đầu ra "
      "của bộ tích phân là một điện áp dốc có cực tính ngược lại. Đặc tính này "
      "cũng được thể hiện bằng đồ họa trên Hình 5.21 và Hình 5.22, từ đó còn "
      "cho thấy rõ ràng rằng với giá trị điện áp đầu vào lớn hơn thì độ dốc "
      "của điện áp đầu ra lớn hơn.",
      "This equation describes that for a constant voltage input the output "
      "of the integrator is a ramp voltage of opposite polarity. The same "
      "characteristics have been shown on graphical presentation as well on "
      "Figures 5.21 and 5.22 from where it is also clear that for higher "
      "values at input voltage, the slope of output voltage is sharper.")

    FIG(b, 21, F.fig_f21(), lang)
    FIG(b, 22, F.fig_f22(), lang)

    P(b, lang,
      "Hình 5.23 trình bày cách hiện thực hóa mô tả trên. Đầu vào Ei được đưa "
      "tới bộ tích phân và đầu ra Eo được đưa tới mạch phát hiện mức, mạch này "
      "gửi một xung tới cổng bộ phát xung khi mức Eo đạt tới mức tham chiếu cố "
      "định. Bộ phát hiện mức thực chất là mạch so sánh điện áp, trong đó Eo "
      "được so với một giá trị tham chiếu. Ei càng lớn thì độ dốc của Eo càng "
      "lớn và Eo càng nhanh đạt tới mức tham chiếu trong mạch phát hiện mức. "
      "Khi cổng bộ phát xung được kích hoạt bởi tín hiệu từ bộ phát hiện mức, "
      "cổng này truyền các xung của bộ dao động xung nhịp tới bộ phát xung. "
      "Đầu ra của bộ phát xung là các xung có biên độ và độ rộng không đổi "
      "nhưng lớn hơn, có cực tính ngược với Ei. Tín hiệu này được phản hồi tới "
      "bộ tích phân và do đầu vào của bộ tích phân bị đảo ngược, đầu vào ròng "
      "thay đổi và đầu ra Eo tụt trở lại mức ban đầu. Vì Eo giảm dưới mức tham "
      "chiếu của bộ phát hiện mức, không có đầu ra từ mạch phát hiện mức tới "
      "cổng bộ phát xung, do đó cổng này đóng lại và không còn xung nào được "
      "phản hồi tới bộ tích phân. Vì thế Ei lại được khôi phục về giá trị ban "
      "đầu và Eo lại bắt đầu tăng, rồi toàn bộ quá trình lại lặp lại. Như vậy, "
      "dạng sóng của Eo sẽ là sóng răng cưa, có thời gian tăng phụ thuộc vào "
      "Ei và thời gian giảm do độ rộng của xung đầu ra từ bộ phát xung quyết "
      "định. Do đó tần số của Eo (sóng răng cưa) là hàm của độ lớn Ei.",
      "Figure 5.23 indicates implementation of the above description. The "
      "input Ei is applied to integrator and the output Eo is fed to a level "
      "detection circuit which sends a pulse to a pulse generator gate when "
      "the level of Eo reaches a fixed reference level. The level detector in "
      "effect is a voltage comparator circuit where Eo is compared with "
      "respect to a reference. Greater the value of Ei, sharper shall be the "
      "slope of Eo and faster the Eo will reach the reference level in the "
      "level detector circuit. The pulse generator gate when enabled by level "
      "detector signal, sends clock oscillator pulses to pulse generator. "
      "Output of pulse generator are pulses of constant but, higher amplitude "
      "and width whose polarity is opposite to Ei. This is fed back to the "
      "integrator and due to reversal of input to the integrator, net input "
      "is changed and also the output Eo drops back to original level. Since "
      "Eo drops below the reference of level detector, there is no output "
      "from level detector circuit to pulse generator gate and so this gate "
      "is closed and no more pulse is fed back to integrator. So Ei again gets "
      "restored to original value and Eo again starts rising and whole process "
      "is once again restarted. Thus, the wave form of Eo will be seen as "
      "sawtooth wave whose risetime will depend upon the input Ei and fall "
      "time will be determined by the width of output pulse of the pulse "
      "generator. Hence the frequency of Eo (sawtooth wave) is a function of "
      "magnitude of Ei.")

    FIG(b, 23, F.fig_f23(), lang)

    P(b, lang,
      "Với mỗi chu kỳ của Eo dưới dạng sóng răng cưa, bộ phát xung cho một "
      "xung, nên số xung tạo ra trong một khoảng thời gian nhất định, tức là "
      "tần số của sóng răng cưa, là thước đo điện áp chưa biết. Để đo tần số "
      "này, xung của bộ dao động xung nhịp cũng được đưa tới bộ chọn cơ sở "
      "thời gian, bộ này mở cổng bắt đầu - dừng, rồi đến lượt nó mở cổng "
      "chính, và đầu ra của bộ phát xung cùng với đầu vào tích phân đi vào "
      "cổng chính. Xung tiếp theo từ bộ chọn cơ sở thời gian đóng cổng bắt "
      "đầu - dừng và cũng đóng cả cổng chính. Vì vậy bộ đếm sẽ chỉ thị số xung "
      "đã đi qua trong một khoảng thời gian đã biết. Đây chính là giá trị điện "
      "áp cần đo. Biên độ và độ rộng xung của bộ phát xung có thể được điều "
      "chỉnh để đọc trực tiếp bộ đếm theo đơn vị điện áp.",
      "Since for each cycle of Eo in the form of sawtooth wave, one pulse is "
      "obtained from the pulse generator, number of pulses produced in this "
      "way in a given interval, i.e. frequency of sawtooth wave is a measure "
      "of unknown voltage. For measurement of this frequency, the clock "
      "oscillator pulse is also applied to time base selector, which opens "
      "start-stop gate and in turn opens the main gate and the pulse generator "
      "output enters the main gate in addition to the integrator. Next pulse "
      "from time base selector closes start-stop gate and also the main gate. "
      "Hence, the counter will indicate the number of pulses that have passed "
      "during a known interval of time. This is the value of voltage to be "
      "measured. The amplitude and pulse width of the pulse generator can be "
      "adjusted to read the counter directly in voltage.")

    # -------------------------------------------------- potentiometer type
    H(b, lang, "3. Bộ chuyển đổi ADC kiểu chiết áp",
      "3. Potentiometer type ADC conversion", level=3)

    P(b, lang,
      "Mạch chiết áp dùng cho kiểu chuyển đổi ADC này về cơ bản là kiểu tự "
      "cân bằng. Điện áp đầu vào chưa biết cần đo được đưa tới bộ chiết áp "
      "chính xác và được so sánh với điện áp tham chiếu do nguồn diode Zener "
      "cung cấp như Hình 5.24. Điện áp sai số thu được (vốn có dạng một chiều) "
      "được bộ chuyển đổi đổi sang dạng xoay chiều, rồi đưa qua bộ khuếch đại "
      "sơ tới bộ khuếch đại servo. Khuếch đại servo cần thiết để tăng mức tín "
      "hiệu tới mức cần cho hoạt động của hệ thống cân bằng servo. Hệ thống "
      "cân bằng servo, gồm motor servo cùng các cuộn dây điều khiển và tham "
      "chiếu, cân bằng chiết áp và đưa dây trượt trở lại trạng thái cân bằng.",
      "The potentiometer circuit employed for this type of ADC conversion is "
      "basically self-balancing type. The unknown input voltage to be "
      "measured is applied to the precision potentiometer unit and is compared "
      "with respect to reference voltage supplied by zener diode voltage "
      "source as shown in Figure 5.24. The resulting error voltage is "
      "converted to A.C. (error voltage being of D.C. type) by converter and "
      "then fed to servo-amplifier through pre-amplifier. Servo-amplification "
      "is needed to increase the signal level necessary for operation of "
      "servo-balancing system. The servo-balancing system, consisting of "
      "servo-motor along with its control and reference windings, balances the "
      "potentiometer and brings back the slide wire to equilibrium state.")

    FIG(b, 24, F.fig_f24(), lang)

    return b
