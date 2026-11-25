# -*- coding: utf-8 -*-
"""Chapter 6, section 6.2 "Proportional control" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 289-292, printed pp. 277-280, decoded
text lines 11125-11272.  Equations (6.1) and (6.2) were transcribed from the
printed page image work/ipc6_pages/p291.png because the decoded text garbles
them.  Figures 6.4-6.7 are inserted where the prose refers to them.  The
figure suppliers are authored in parallel; until they are importable the four
small vector redraws below are installed with non-overwriting hasattr guards.
"""

import math

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG

INK = "#1f3a5f"
GREY = "#777777"


# --------------------------------------------------------------- SVG helpers
def _t(x, y, s, size=7.6, anchor="middle", color=INK):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _ln(x1, y1, x2, y2, color=INK, sw=1.2, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, color, sw, d))


def _poly(pts, color=INK, sw=1.6, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    p = " ".join("%.1f,%.1f" % (x, y) for x, y in pts)
    return ('<polyline points="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>' % (p, color, sw, d))


def _rect(x, y, w, h, fill="#ffffff", color=INK, sw=1.2):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" '
            'stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, color, sw))


def _arrow(mid):
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="%s"/></marker></defs>' % (mid, INK))


def _ar(x1, y1, x2, y2, mid, sw=1.2):
    return ('<path d="M%s %s L%s %s" fill="none" stroke="%s" '
            'stroke-width="%s" marker-end="url(#%s)"/>'
            % (x1, y1, x2, y2, INK, sw, mid))


# --------------------------------------------------------- fallback figures
def _standalone_fig(n):
    """A simplified vector redraw used only if a supplier is not present."""
    mid = "ipc6b%d" % n
    o = [_arrow(mid)]

    if n == 4:                                   # quarter amplitude decay
        title = "Quarter-amplitude decay"
        cvi = "Suy giảm biên độ một phần tư"
        cen = "Response with quarter-amplitude decay"
        avi = ("Dao động quanh giá trị cài đặt với biên độ giảm dần; biên độ x "
               "của chu kỳ sau bằng một phần tư biên độ y của chu kỳ trước")
        aen = ("Oscillation about the set value with decreasing amplitude; the "
               "amplitude x of the following cycle is one quarter of the "
               "preceding amplitude y")
        o += [_ln(120, 60, 120, 175), _ln(120, 175, 620, 175),
              _ar(120, 60, 120, 42, mid), _ar(120, 175, 640, 175, mid),
              _t(100, 53, "Controlled", 7.0, anchor="end"),
              _t(100, 63, "variable", 7.0, anchor="end"),
              _t(620, 194, "Time", 7.4),
              _ln(140, 118, 610, 118, color=GREY, sw=1.0, dash="5,4")]
        pts = []
        for i in range(241):
            t = i / 240.0
            pts.append((150 + 450 * t,
                        118 - 44 * math.exp(-3.0 * t) * math.sin(2 * math.pi * 2.2 * t)))
        o.append(_poly(pts, sw=1.7))
        o += [_ar(201, 114, 201, 88, mid), _ar(201, 93, 201, 118, mid),
              _t(194, 105, "y", 8.0, anchor="end"),
              _ar(406, 116, 406, 110, mid), _ar(406, 112, 406, 118, mid),
              _t(399, 115, "x", 8.0, anchor="end"),
              _t(548, 96, "x/y = 1/4", 8.0)]

    elif n == 5:                                 # high-gain cycling
        title = "Oscillation around the set value"
        cvi = "Dao động quanh giá trị cài đặt"
        cen = "Oscillation about the set value"
        avi = ("Biến điều khiển dao động quanh giá trị cài đặt với nhiều chu kỳ "
               "không tắt dần khi độ lợi quá cao")
        aen = ("The controlled variable oscillates about the set value in "
               "sustained cycles when the gain is too high")
        o += [_ln(120, 55, 120, 175), _ln(120, 175, 620, 175),
              _ar(120, 55, 120, 38, mid), _ar(120, 175, 640, 175, mid),
              _t(100, 48, "Controlled", 7.0, anchor="end"),
              _t(100, 58, "variable", 7.0, anchor="end"),
              _t(620, 194, "Time", 7.4),
              _ln(140, 115, 610, 115, color=GREY, sw=1.0, dash="5,4")]
        pts = []
        for i in range(321):
            t = i / 320.0
            pts.append((145 + 455 * t,
                        115 - (32 * math.exp(-2.2 * t) + 7) *
                        math.sin(2 * math.pi * 3.2 * t)))
        o.append(_poly(pts, sw=1.6))

    elif n == 6:                                 # electronic implementation
        title = "Electronic proportional controller"
        cvi = "Bộ điều khiển tỷ lệ điện tử"
        cen = "Electronic implementation of proportional action"
        avi = ("Tín hiệu sai số đi qua tụ đầu vào tới bộ khuếch đại thuật toán; "
               "tụ phản hồi và chiết áp chỉnh dải tỷ lệ tạo đường phản hồi")
        aen = ("The error signal passes through the input capacitor to the "
               "operational amplifier; a feedback capacitor and a band-setting "
               "potentiometer form the feedback path")
        o += [_ar(45, 80, 150, 80, mid),
              _t(48, 66, "Ein (error signal)", 7.4, anchor="start"),
              _t(135, 51, "Input capacitor", 7.0), _t(153, 70, "Cin", 7.4),
              _ln(150, 68, 150, 92, sw=1.6), _ln(157, 68, 157, 92, sw=1.6),
              _ln(157, 80, 255, 80),
              _poly([(255, 55), (255, 145), (355, 100), (255, 55)], sw=1.4),
              _t(298, 90, "OA", 8.0),
              _ln(255, 120, 205, 120), _ln(205, 120, 205, 155),
              _ln(190, 155, 220, 155), _ln(195, 159, 215, 159),
              _ln(200, 163, 210, 163),
              _ar(355, 100, 560, 100, mid),
              _t(565, 104, "E0 (Controller output)", 7.4, anchor="start"),
              _ln(355, 100, 355, 48), _ln(355, 48, 305, 48),
              _ln(298, 48, 255, 48), _ln(255, 48, 255, 80),
              _ln(298, 42, 298, 54, sw=1.6), _ln(305, 42, 305, 54, sw=1.6),
              _t(301, 34, "Cfb", 7.4),
              _t(430, 38, "Feedback capacitor", 7.0, anchor="start"),
              _ln(205, 155, 560, 155), _ln(560, 100, 560, 155),
              _ln(440, 100, 440, 155, sw=1.6),
              _ar(474, 128, 446, 124, mid),
              _t(470, 178, "Proportional band adjustment potentiometer",
                 7.0, anchor="start")]

    else:                                        # pneumatic implementation
        title = "Pneumatic proportional controller"
        cvi = "Bộ điều khiển tỷ lệ khí nén"
        cen = "Pneumatic implementation of proportional action"
        avi = ("Áp suất cấp đi qua bộ hạn chế tới vòi phun; cánh flap nổi giữa "
               "lò xo và buồng khí tỷ lệ, bộ rơ le khí nén tạo áp suất đầu ra")
        aen = ("Supply air passes through a restriction to the nozzle; the "
               "flapper floats between a spring and a proportional bellows, "
               "and a pneumatic relay develops the output pressure")
        o += [_ar(40, 85, 145, 85, mid),
              _t(45, 65, "Air supply", 7.4, anchor="start"),
              _t(45, 77, "1.4 kg/cm²", 7.0, anchor="start"),
              _ln(145, 85, 320, 85),
              _rect(245, 78, 10, 14, fill=INK),
              _t(250, 68, "Restriction", 7.2),
              _poly([(320, 79), (340, 85), (320, 91), (320, 79)], sw=1.3),
              _t(330, 68, "Nozzle", 7.2),
              _poly([(345, 72), (351, 181)], sw=2.0),
              _t(400, 96, "Flapper operated by", 7.2, anchor="start"),
              _t(400, 106, "process variable", 7.2, anchor="start"),
              _rect(190, 110, 100, 45, fill="#eef3fb"),
              _t(240, 128, "Pneumatic", 7.4), _t(240, 139, "relay", 7.4),
              _ln(180, 85, 180, 132), _ln(180, 132, 190, 132),
              _ln(290, 132, 318, 132), _ln(318, 132, 318, 91),
              _ar(190, 143, 60, 143, mid),
              _t(66, 135, "Output", 7.4, anchor="start"),
              _ln(351, 181, 430, 181),
              _poly([(355, 170), (361, 180), (355, 190), (361, 200),
                     (367, 190), (373, 200), (379, 190), (385, 200),
                     (391, 190), (397, 181)], sw=1.4),
              _t(372, 215, "Spring", 7.2),
              _rect(430, 169, 55, 24, fill="#eef3fb"),
              _poly([(434, 175), (441, 181), (448, 175), (455, 181),
                     (462, 175), (469, 181), (481, 175)], sw=1.0),
              _t(500, 178, "Proportional", 7.2, anchor="start"),
              _t(500, 188, "bellows", 7.2, anchor="start")]

    o.append(_t(340, 242, "Hình 6.%d   ·   Figure 6.%d" % (n, n),
                6.4, color=GREY))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" fill="#ffffff"/>'
           '%s</svg>' % "".join(o))
    return (svg,
            "Hình 6.%d · %s" % (n, cvi),
            "Figure 6.%d · %s" % (n, cen),
            avi, aen)


for _n in (4, 5, 6, 7):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# --------------------------------------------------------------------- prose
def section(lang):
    b = []

    H(b, lang, "6.2 Điều khiển tỷ lệ", "6.2 Proportional control")

    P(b, lang,
      "Điều khiển tỷ lệ còn được gọi là điều khiển tiết lưu hay điều khiển "
      "điều hòa liên tục. Ở chế độ này tồn tại quan hệ tuyến tính liên tục "
      "giữa giá trị biến được điều khiển và đầu ra của bộ điều khiển: đầu ra "
      "thay đổi theo cách giống như độ lệch giữa giá trị cài đặt và giá trị "
      "đo được. Hành động chỉ tỷ lệ với độ lớn của độ lệch và không chịu "
      "ảnh hưởng của tốc độ thay đổi độ lệch. Vì vậy, không thể có sự thay đổi "
      "đầu ra của bộ điều khiển khi không có độ lệch đáng kể.",
      "Proportional control is also known as throttling control or modulating "
      "control. In this mode a continuous linear relationship exists between "
      "the value of the controlled variable and the output of the controller: "
      "the output changes in the same way as the indicated deviation between "
      "the set value and the measured value. The action is proportional to the "
      "amount of deviation only and has no effect due to the rate of change of "
      "deviation. Hence no change in controller output can be expected without "
      "a substantial amount of deviation.")

    P(b, lang,
      "Độ thay đổi cần thiết của biến đo hoặc biến được điều khiển để tạo ra "
      "sự thay đổi toàn phần ở đầu ra bộ điều khiển được gọi là dải tỷ lệ "
      "(PB); nó cũng được gọi là dải điều hòa hoặc dải tiết lưu. Dải tỷ lệ "
      "được biểu thị bằng phần trăm của toàn thang và có thể thay đổi từ dưới "
      "một phần trăm đến hơn 200 phần trăm.",
      "The necessary change in the measured or controlled variable needed to "
      "effect a full change in controller output is known as the proportional "
      "band (PB); it is also termed the modulating range or throttling range. "
      "PB is expressed as a percentage of the full range and can vary from "
      "less than one per cent to more than 200 per cent.")

    P(b, lang,
      "Một cách biểu diễn khác của dải tiết lưu là độ lợi bộ điều khiển (CG) "
      "hay độ nhạy, là nghịch đảo của dải tỷ lệ. Độ lợi cho thấy tỷ số giữa "
      "đầu ra và đầu vào của bộ điều khiển; ví dụ, dải tỷ lệ 50 phần trăm "
      "tương ứng với độ lợi bằng 2. Cơ cấu chỉnh trong bộ điều khiển có thể "
      "được thiết kế và hiệu chuẩn theo độ lợi hoặc theo dải tỷ lệ.",
      "Another way of representing the throttling range is controller gain "
      "(CG) or sensitivity, which are reciprocals of the proportional band. "
      "Gain indicates the ratio of controller output to its input; for "
      "instance, a 50 per cent proportional band corresponds to a gain of 2. "
      "The adjustment inside the controller can be designed and calibrated "
      "in terms of gain or proportional band.")

    P(b, lang,
      "Bất kỳ thay đổi nào của biến được điều khiển cũng đòi hỏi thay đổi đầu "
      "ra của bộ điều khiển để giữ biến ở giá trị cài đặt. Nhưng bộ điều khiển "
      "có hành động tỷ lệ cần một sự thay đổi độ lệch để tạo ra đầu ra, nên nó "
      "chỉ tạo tác động hiệu chỉnh cho một tải cụ thể; với mọi tải khác phải "
      "còn lại một độ lệch nhất định, gọi là độ lệch tĩnh (offset). Sự hiện "
      "diện của offset là đặc trưng của hành động tỷ lệ và chỉ có thể loại bỏ "
      "bằng cách chỉnh lại thủ công giá trị cài đặt để đưa biến được điều "
      "khiển về giá trị thực. Việc chỉnh lại này chỉ do người vận hành thực "
      "hiện và chỉ khi sự thay đổi tải không thường xuyên; nếu tải thay đổi "
      "thường xuyên thì không thể chỉnh tay được.",
      "Any change in the controlled variable requires a change in controller "
      "output to maintain the variable at the set value. But a controller with "
      "proportional action needs a change in deviation to generate output, so "
      "it produces corrective action for a particular load only; for all other "
      "loads some deviation must remain, which is called offset. The presence "
      "of offset is characteristic of proportional action and can be eliminated "
      "only by manually readjusting the set value to bring the controlled "
      "variable back to its actual value. That readjustment can be done only "
      "by the operator, and only where load changes are not very frequent; if "
      "load changes are frequent it is not practically possible to readjust "
      "manually.")

    P(b, lang,
      "Các tiêu chí dùng để đánh giá một hành động điều khiển là:",
      "The criteria used to evaluate a control action are:")
    L(b, lang,
      ["Độ lệch nhỏ nhất sau một nhiễu động",
       "Thời gian ngắn nhất trước khi trở về giá trị cài đặt",
       "Offset nhỏ nhất do thay đổi tải"],
      ["Minimum deviation following a disturbance",
       "Minimum time interval before returning to the set value",
       "Minimum offset due to changes in load"],
      ordered=True)

    P(b, lang,
      "Các tiêu chí này phù hợp với yêu cầu đáp ứng của bộ điều khiển có suy "
      "giảm biên độ một phần tư, như thể hiện trong Hình 6.4. Sau suy giảm "
      "biên độ một phần tư, biến được điều khiển nhất định phải đạt đến giá "
      "trị cài đặt (giá trị trạng thái ổn định).",
      "These criteria accord with the requirement of a controller response "
      "with quarter amplitude decay, as shown in Figure 6.4. After quarter "
      "amplitude decay the controlled variable should reach the set value "
      "(steady-state value) without fail.")
    FIG(b, 4, F.fig_f04(), lang)

    P(b, lang,
      "Tuy nhiên, ở khía cạnh này, hành động điều khiển tỷ lệ với độ lợi cao "
      "gây hiệu chỉnh quá mức biến được điều khiển quanh giá trị cài đặt. "
      "Chuyển động của kim quá trình (biểu thị biến được điều khiển) quanh "
      "kim cài đặt (biểu thị giá trị cài đặt) chính là dao động quanh giá trị "
      "cài đặt, như thể hiện trong Hình 6.5.",
      "In this respect, however, proportional control action with a higher "
      "gain produces over-correction of the controlled variable around the "
      "set value. The resulting movement of the process pointer (which "
      "indicates the controlled variable) around the set pointer (which "
      "indicates the set value) is an oscillation around the set value, as "
      "shown in Figure 6.5.")
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Mặt khác, nếu giảm độ lợi để hạn chế dao động lặp lại, đáp ứng trở nên "
      "chậm chạp, điều này hoàn toàn không mong muốn vì phản ứng nhanh rất "
      "quan trọng trong mọi hệ thống điều khiển quá trình. Xét hai thái cực "
      "đó, cần có sự thỏa hiệp trong lựa chọn độ lợi để đạt điều khiển tối "
      "ưu. Cài đặt độ lợi tạo ra một vài chu kỳ tắt dần nhanh là lựa chọn "
      "tốt nhất. Cài đặt này phụ thuộc vào độ lớn của thay đổi tải và cả thời "
      "gian hệ thống điều khiển cần để hiệu chỉnh độ lệch. Khi đáp ứng của "
      "quá trình nhanh, độ lợi nhỏ là lựa chọn tốt nhất.",
      "If, on the other hand, the gain is reduced to minimize the cyclic "
      "movement, the response becomes sluggish, which is not at all desirable "
      "because fast response is very important in any process control system. "
      "Considering both extremes, a compromise in the selection of gain for "
      "optimum control is called for. A gain setting that results in a few "
      "fast subsiding cycles is the best choice. Obviously, such a gain "
      "setting depends on the magnitude of load change and also on the time "
      "taken by the control system to correct the deviation. In a case where "
      "the response of the process is faster, a small gain is the best choice.")

    P(b, lang,
      "Điều khiển tỷ lệ phát huy tốt nhất khi dung lượng của quá trình lớn, "
      "tốc độ phản ứng của quá trình chậm và độ trễ (độ trễ quá trình và độ "
      "trễ vận chuyển) nhỏ. Những đặc tính này tạo ổn định nhanh hơn và cần "
      "độ lợi cao hơn, cuối cùng dẫn đến hành động hiệu chỉnh nhanh hơn. Khi "
      "đặc tính quá trình khác đi, độ lợi thấp hơn được chọn dù nó tạo ra "
      "offset đáng kể khi tải thay đổi. Tuy nhiên, độ lợi cao gây dao động "
      "lặp nếu đáp ứng của quá trình nhanh. Tình trạng này càng xấu hơn nếu "
      "có phần tử thời gian chết, vì việc hiệu chỉnh vượt quá cần nhiều thời "
      "gian hơn. Do đó có thể kết luận rằng hành động điều khiển tỷ lệ nên "
      "dùng cho các quá trình có hằng số thời gian lớn và thời gian chết "
      "nhỏ, với độ lớn thay đổi tải nhỏ dù tốc độ thay đổi tải nhanh.",
      "Proportional control is at its best when the capacitance of the process "
      "is large, the process reaction rate is slow and the lag (process lag "
      "and transport lag) is small. These characteristics bring stability "
      "faster and need higher gain, ultimately leading to faster corrective "
      "action. When the process characteristics are different, a lower gain "
      "is selected even if it creates a substantial amount of offset on load "
      "changes. High gain, however, results in cycling if the response of the "
      "process is faster. This condition worsens if a dead-time element is "
      "present, because the correction for overshoot takes more time. "
      "Therefore it can be concluded that proportional control action should "
      "be used in processes having a large time constant and small dead time, "
      "the magnitude of load changes being small even if the speed of load "
      "changes is fast.")

    P(b, lang,
      "Đầu ra và đầu vào của bộ điều khiển tỷ lệ liên hệ với nhau theo biểu "
      "thức:",
      "Output and input of a proportional controller are related according "
      "to the expression:")
    E(b, lang, "E₀ = (100/P_b)·E_s + B", "E₀ = (100/P_b)·E_s + B", num="6.1")

    P(b, lang,
      "trong đó P_b là dải tỷ lệ tính theo phần trăm, E_s là độ lớn của độ "
      "lệch hay sai số, B là cài đặt đầu ra thiên vị và E₀ là đầu ra.",
      "where P_b is the proportional band in percentage, E_s is the amount of "
      "deviation or error, B is the bias output setting and E₀ is the output.")

    P(b, lang,
      "Nếu tín hiệu độ lệch hay sai số bằng không, đầu ra của bộ điều khiển "
      "bằng giá trị cài đặt thiên vị. Ở đây cần lưu ý rằng độ lợi bộ điều "
      "khiển gồm hai phần: độ lợi trạng thái ổn định (gọi là K_g) và độ lợi "
      "động (gọi là g_d). Độ lợi trạng thái ổn định là đại lượng vô hướng, "
      "còn độ lợi động là đại lượng có hướng. Vì bộ điều khiển tỷ lệ không "
      "có phần tử động, độ lợi động của nó có thể lấy bằng 1.0 với góc pha "
      "bằng không. Sự dịch pha 180° xảy ra trong hệ thống phản hồi âm chỉ "
      "xuất hiện ở phần tử thời gian chết đối với bộ điều khiển tỷ lệ. Do "
      "đó, một quá trình có thời gian chết t sẽ dao động với chu kỳ 2t.",
      "If the deviation or error signal happens to be zero, the output of the "
      "controller equals the value of the bias setting. Here it is worth "
      "mentioning that controller gain consists of two parts, that is, "
      "steady-state gain (say K_g) and dynamic gain (say g_d). Steady-state "
      "gain is scalar whereas dynamic gain is a vector. Since a proportional "
      "controller does not have a dynamic element, its dynamic gain can be "
      "taken as 1.0 with zero degree phase angle. The phase shift of 180° "
      "which takes place in a negative feedback system comes up in the "
      "dead-time element only in the case of a proportional controller. "
      "Therefore a process having a dead time of t shall cycle with a period "
      "of 2t.")

    P(b, lang,
      "Độ lệch xuất hiện do thay đổi tải và tiếp tục duy trì được cho bởi:",
      "The deviation that appears due to a load change and continues to "
      "sustain is given by:")
    E(b, lang, "E_s = ((E₀ − B)·P_b)/100", "E_s = ((E₀ − B)·P_b)/100", num="6.2")

    P(b, lang,
      "Điều này thực chất xuất hiện như một offset, sẽ tiếp tục tăng khi dải "
      "tỷ lệ tăng.",
      "This in fact appears as an offset, which will go on increasing as the "
      "proportional band is increased.")

    P(b, lang,
      "Việc thực hiện hành động tỷ lệ bằng mạch điện tử được thể hiện trong "
      "Hình 6.6.",
      "Implementation of proportional action is shown electronically in "
      "Figure 6.6.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Trong cách thực hiện này, dải tỷ lệ được xác định bởi tỷ số giữa C_in "
      "và C_fb. Tỷ số này cũng chịu ảnh hưởng của độ lợi bộ khuếch đại thuật "
      "toán (OA). Khi tỷ số độ lợi hiệu dụng bằng 1, dải tỷ lệ bằng 100 phần "
      "trăm. Việc chỉnh dải tỷ lệ được thực hiện bằng chiết áp chỉnh dải tỷ "
      "lệ.",
      "In this implementation, the proportional band is determined by the "
      "ratio of C_in to C_fb. This ratio is affected by the operational "
      "amplifier (OA) gain as well. When the effective gain ratio is 1, then "
      "the proportional band becomes 100 per cent. The adjustment in "
      "proportional band is effected by the proportional band adjustment "
      "potentiometer.")

    P(b, lang,
      "Cách thực hiện tương đương dưới dạng khí nén được thể hiện trong Hình "
      "6.7.",
      "The equivalent implementation in its pneumatic form has been shown "
      "in Figure 6.7.")
    FIG(b, 7, F.fig_f07(), lang)

    P(b, lang,
      "Như quan sát trong Hình 6.7, cánh flap không cố định (như trong hành "
      "động điều khiển ON-OFF) mà ở trạng thái nổi giữa lò xo (với hằng số lò "
      "xo K_p) và buồng khí tỷ lệ. Buồng khí tỷ lệ, còn gọi là buồng khí phản "
      "hồi, và lò xo cùng chịu tác động của áp suất đầu ra để khôi phục cân "
      "bằng giữa vòi phun và hệ thống cánh flap. Nhờ đó, lực do buồng khí "
      "giãn ra khi có áp suất đầu ra bằng với lực do lò xo tác dụng. Tỷ số "
      "giữa chiều dài của cánh flap phía trên vị trí vòi phun và chiều dài "
      "phía dưới có ý nghĩa quan trọng trong cấu trúc này; tỷ số này thực "
      "chất quyết định độ lớn của độ lợi tỷ lệ và có thể chỉnh bằng cách "
      "thay đổi tỷ số đó.",
      "As is observed in Figure 6.7, the flapper is not fixed (as was the "
      "case in ON-OFF control action) but is in a floating state between the "
      "spring (having K_p as the spring constant) and the proportional "
      "bellows. The proportional bellows, which is also called the feedback "
      "bellows, and the spring together are acted upon by the output pressure "
      "for restoration of balance between the nozzle and the flapper system. "
      "In this way the force exerted by the expansion of the bellows due to "
      "the application of output pressure is equal to the force exerted by "
      "the spring. The ratio of flapper length above the nozzle position to "
      "that below the nozzle position is important in this arrangement; this "
      "ratio in fact decides the amount of proportional gain and can be "
      "adjusted by varying that ratio.")

    P(b, lang,
      "Hành động tỷ lệ là hành động điều khiển cơ bản trong lĩnh vực điều "
      "khiển quá trình liên tục.",
      "Proportional action is the basic controller action in the field of "
      "continuous process control.")

    return b
