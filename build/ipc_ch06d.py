# -*- coding: utf-8 -*-
"""Chapter 6, section 6.4 "Derivative control" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 295-297, printed pp. 283-285, decoded
text lines 11353-11445 in work/ipc_decoded.txt.  Equation (6.4) was
transcribed from the printed page image work/ipc6_pages/p296.png because the
text layer garbles it.  Figures 6.11-6.13 are inserted where the prose refers
to them.  The figure suppliers are authored in parallel; until they are
importable the three small vector redraws below are installed with
non-overwriting hasattr guards.
"""

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG

_INK = "#1f3a5f"
_GREY = "#777777"


# --------------------------------------------------------------- SVG helpers
def _t(x, y, s, size=7.4, anchor="middle", color=_INK):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _ln(x1, y1, x2, y2, sw=1.2, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, _INK, sw, d))


def _poly(pts, sw=1.6, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    p = " ".join("%.1f,%.1f" % (x, y) for x, y in pts)
    return ('<polyline points="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>' % (p, _INK, sw, d))


def _rect(x, y, w, h, sw=1.2):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="#ffffff" '
            'stroke="%s" stroke-width="%s"/>' % (x, y, w, h, _INK, sw))


def _defs(mid):
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="%s"/></marker></defs>' % (mid, _INK))


def _ar(x1, y1, x2, y2, mid, sw=1.2):
    return ('<path d="M%s %s L%s %s" fill="none" stroke="%s" '
            'stroke-width="%s" marker-end="url(#%s)"/>'
            % (x1, y1, x2, y2, _INK, sw, mid))


def _mk(n, o, cvi, cen, avi, aen):
    o.append(_t(340, 242, "Hình 6.%d   ·   Figure 6.%d" % (n, n),
                6.4, color=_GREY))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg,
            "Hình 6.%d · %s" % (n, cvi),
            "Figure 6.%d · %s" % (n, cen),
            avi, aen)


# --------------------------------------------------------- fallback figures
def _fig11():
    """Derivative response: a step in measurement input and the output kick."""
    mid = "ipc6dA11"
    o = [_defs(mid)]
    o.append(_ln(150, 60, 150, 195))                 # amplitude axis
    o.append(_ar(150, 195, 430, 195, mid))           # time axis
    o.append(_t(300, 212, "Time", 8))
    # measurement input step (solid) and its extended level (dashed)
    o.append(_poly([(170, 160), (280, 160), (280, 105), (390, 105)], 2.0))
    o.append(_ln(280, 105, 400, 105, 1.0, "5 4"))
    o.append(_ar(400, 95, 330, 95, mid))
    o.append(_t(410, 98, "Measurement input change", 7.6, anchor="start"))
    # output: narrow negative pulse at the transition, then a new plateau
    o.append(_poly([(170, 178), (280, 178), (280, 188), (298, 188),
                    (298, 145), (390, 145)], 2.0))
    o.append(_ar(400, 140, 330, 140, mid))
    o.append(_t(410, 143, "Output", 7.6, anchor="start"))
    return _mk(11, o,
               "Đáp ứng vi phân",
               "Derivative response",
               "Đồ thị đáp ứng vi phân: đầu vào thay đổi bước và xung đầu ra tương ứng",
               "Derivative response plot: a step in the measurement input and the resulting output kick")


def _fig12():
    """Electronic derivative implementation with an operational amplifier."""
    mid = "ipc6dA12"
    o = [_defs(mid)]
    # input and series capacitor Cin
    o.append(_t(45, 112, "Ein", 7.4, anchor="start"))
    o.append(_ln(55, 120, 100, 120))
    o.append(_ln(100, 111, 100, 129))
    o.append(_ln(106, 111, 106, 129))
    o.append(_t(103, 104, "Cin", 7.2))
    o.append(_ln(106, 120, 170, 120))
    # operational amplifier
    o.append(_poly([(170, 90), (170, 150), (240, 120), (170, 90)], 1.4))
    o.append(_t(195, 124, "OA", 8))
    # output line
    o.append(_ln(240, 120, 430, 120))
    o.append(_t(440, 123, "E0", 7.4, anchor="start"))
    # feedback network: Cfd in parallel with adjustable Rd
    o.append(_ln(150, 60, 205, 60))
    o.append(_ln(150, 60, 150, 120))
    o.append(_ln(205, 52, 205, 95))
    o.append(_ln(265, 52, 265, 95))
    o.append(_ln(265, 60, 300, 60))
    o.append(_ln(300, 60, 300, 120))
    o.append(_ln(205, 60, 232, 60))
    o.append(_ln(232, 52, 232, 70))
    o.append(_ln(238, 52, 238, 70))
    o.append(_ln(238, 60, 265, 60))
    o.append(_t(235, 44, "Cfd", 7.2))
    o.append(_poly([(205, 88), (212, 84), (219, 92), (226, 84), (233, 92),
                    (240, 84), (247, 92), (254, 84), (265, 88)], 1.2))
    o.append(_ar(235, 102, 235, 92, mid))
    o.append(_t(235, 112, "Derivative adjustment", 7.0))
    # proportional-band resistor Rp
    o.append(_ln(360, 120, 360, 150))
    o.append(_poly([(360, 150), (354, 156), (366, 164), (354, 172),
                    (366, 180), (354, 188), (360, 194)], 1.2))
    o.append(_ln(360, 194, 360, 205))
    o.append(_t(390, 168, "Rp", 7.2, anchor="start"))
    o.append(_t(390, 180, "Proportional band", 7.0, anchor="start"))
    o.append(_t(390, 191, "adjustment", 7.0, anchor="start"))
    # derivative capacitor Cd and the divider resistors R3, R4
    o.append(_ln(360, 150, 394, 150))
    o.append(_ln(394, 142, 394, 158))
    o.append(_ln(400, 142, 400, 158))
    o.append(_ln(400, 150, 410, 150))
    o.append(_t(397, 135, "Cd", 7.2))
    o.append(_t(305, 160, "Derivative capacitor", 7.0, anchor="start"))
    o.append(_poly([(410, 150), (404, 158), (416, 166), (404, 174),
                    (416, 182), (410, 190)], 1.2))
    o.append(_t(420, 170, "R3", 7.0, anchor="start"))
    o.append(_poly([(410, 190), (404, 196), (416, 204), (410, 210)], 1.2))
    o.append(_t(420, 202, "R4", 7.0, anchor="start"))
    return _mk(12, o,
               "Cài đặt điện tử của hành động vi phân",
               "Electronic implementation of derivative action",
               "Mạch khuếch đại thuật toán với tụ vi phân Cfd, điện trở chỉnh Rd và tụ Cd",
               "Operational-amplifier circuit with derivative capacitor Cfd, adjustment resistor Rd and capacitor Cd")


def _fig13():
    """Pneumatic derivative implementation with a restriction in the output line."""
    mid = "ipc6dA13"
    o = [_defs(mid)]
    # air supply and main line
    o.append(_ar(55, 62, 110, 62, mid))
    o.append(_t(55, 48, "Air supply", 7.2, anchor="start"))
    o.append(_t(55, 80, "1.4 kg/cm²", 7.2, anchor="start"))
    o.append(_ln(110, 62, 250, 62))
    # fixed restriction
    o.append(_poly([(205, 54), (215, 62), (205, 70), (205, 54)], 1.0))
    o.append(_poly([(225, 54), (215, 62), (225, 70), (225, 54)], 1.0))
    o.append(_t(215, 42, "Restriction", 7.2))
    # nozzle and flapper
    o.append(_poly([(250, 57), (268, 57), (268, 67), (250, 67)], 1.0))
    o.append(_t(272, 44, "Nozzle", 7.2, anchor="start"))
    o.append(_ln(282, 46, 282, 100, 1.6))
    o.append(_ar(302, 60, 285, 60, mid))
    o.append(_t(307, 62, "Flapper operated by", 7.0, anchor="start"))
    o.append(_t(307, 73, "process variable", 7.0, anchor="start"))
    # pneumatic relay
    o.append(_ln(205, 62, 205, 100))
    o.append(_rect(150, 100, 110, 40))
    o.append(_t(205, 123, "Pneumatic", 7.6))
    o.append(_t(205, 134, "relay", 7.6))
    o.append(_ln(268, 67, 260, 100))
    # output line
    o.append(_ln(205, 140, 205, 200))
    o.append(_ar(205, 200, 80, 200, mid))
    o.append(_t(72, 203, "Output", 7.4, anchor="end"))
    # proportional bellows, spring and the derivative restriction
    o.append(_ln(260, 120, 360, 120))
    o.append(_poly([(320, 114), (330, 120), (320, 126), (320, 114)], 1.0))
    o.append(_poly([(340, 114), (330, 120), (340, 126), (340, 114)], 1.0))
    o.append(_ar(352, 100, 336, 112, mid))
    o.append(_t(360, 96, "Derivative restriction", 7.0, anchor="start"))
    o.append(_rect(360, 105, 60, 30))
    o.append(_poly([(365, 108), (372, 132), (379, 108), (386, 132),
                    (393, 108), (400, 132), (407, 108), (414, 132)], 1.0))
    o.append(_t(390, 101, "Proportional bellows", 7.0))
    o.append(_poly([(390, 135), (384, 142), (396, 149), (384, 156),
                    (396, 163), (390, 170)], 1.2))
    o.append(_t(350, 182, "Spring (k_p)", 7.0, anchor="start"))
    return _mk(13, o,
               "Cài đặt khí nén của hành động vi phân",
               "Pneumatic implementation of derivative action",
               "Mạch khí nén với vòi phun, cánh flap, buồng tỷ lệ và tiết lưu vi phân",
               "Pneumatic circuit with nozzle, flapper, proportional bellows and derivative restriction")


for _n, _fn in ((11, _fig11), (12, _fig12), (13, _fig13)):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, _fn)


# --------------------------------------------------------------------- prose
def section(lang):
    b = []

    H(b, lang, "6.4 Điều khiển vi phân", "6.4 Derivative control")

    P(b, lang,
      "Điều khiển vi phân còn được gọi là điều khiển khác biệt hay điều khiển "
      "tốc độ. Trong chế độ điều khiển này, đầu ra tỷ lệ với tốc độ thay đổi "
      "của biến quá trình. Chế độ này cố gắng chống lại sự thay đổi của biến "
      "quá trình nên có tác dụng ổn định tốt cho hệ thống điều khiển, nhưng "
      "không ảnh hưởng tới sai số do độ lệch (offset) gây ra.",
      "This is also known as differential control or rate control. In this "
      "control action, the output of the control action is proportional to "
      "the rate of change of process variable. This control action tries to "
      "oppose the change in process variable and therefore, have good "
      "stabilizing effect on the control system but have no effect on the "
      "error caused by the offset.")

    P(b, lang,
      "Hành động vi phân được biểu thị bằng thời gian vi phân (tính bằng "
      "phút), tức là khoảng thời gian mà hành động vi phân làm sớm hơn tác "
      "động của hành động tỷ lệ. Đây là một dạng điều khiển dự báo, hoạt động "
      "như một hành động phòng ngừa (hành động tăng cường). Tốc độ hiệu chỉnh "
      "phụ thuộc vào tốc độ biến quá trình lệch khỏi giá trị cài đặt. Hành động "
      "này đo tốc độ thay đổi của độ lệch giữa biến quá trình và giá trị cài "
      "đặt, dự báo trước hiện tượng vượt quá lớn (nếu có) trước khi nó thực sự "
      "xảy ra và áp dụng hiệu chỉnh để hạn chế. Điều này làm giảm các dao động "
      "không cần thiết có thể phát sinh do nhiễu loạn quá trình.",
      "The derivative action can be expressed by derivative time (in minutes) "
      "being the time in minutes by which a derivative action advances the "
      "effect of proportional action. It is a type of anticipatory control "
      "action working as preventive action (booster action). Speed of "
      "correction shall be dependent upon how fast the process variable drifts "
      "from its set value. It measures the rate of change of deviation between "
      "process variable and the set value and predicts the large overshoot if "
      "any before it can actually occur and apply correction to limit it. This "
      "reduces the unnecessary oscillations that may otherwise arise out of "
      "process disturbances.")

    P(b, lang,
      "Để hành động vi phân có tác dụng thực tế, tín hiệu đầu vào của biến quá "
      "trình hoặc tín hiệu đầu ra đi tới phần tử điều khiển cuối được tăng "
      "cường tỷ lệ với tốc độ thay đổi của tín hiệu thực. Hiệu ứng này tương "
      "đương với việc tăng tạm thời độ lợi, từ đó cải thiện điều khiển theo "
      "cách mà ngay cả hành động điều khiển chậm chạp cũng trở nên đủ nhanh. "
      "Ảnh hưởng gia tốc vốn có của tín hiệu đặc biệt quan trọng đối với quá "
      "trình có hằng số thời gian lớn và đáp ứng ban đầu thấp. Ảnh hưởng của "
      "thời gian trễ tương tự cũng được hành động vi phân khắc phục, làm giảm "
      "thêm chu kỳ dao động. Do đó, khi tải thay đổi đột ngột, biến quá trình, "
      "tức biến được điều khiển, được ổn định nhanh chóng quanh giá trị cài "
      "đặt. Việc chỉnh thời gian vi phân phụ thuộc vào mức độ trễ của quá "
      "trình, và cuối cùng sẽ làm thay đổi mức đáp ứng.",
      "To make the derivative action physically effective, either the process "
      "variable input signal or the output signal going to the final control "
      "element is enhanced in proportion to the rate of change of actual "
      "signal. The effect is equivalent to temporary increase in gain, which "
      "in effect improves the control in such a way that a sluggish control "
      "action also becomes sufficiently rapid. The inherent effect of "
      "acceleration in the signal is important for long time constant process "
      "having low response initially. The dead time effect is similarly "
      "counteracted by the derivative action, which brings further reduction "
      "in the period of the cycling. Therefore, on a sudden load change, the "
      "process variable, i.e. controlled variable is stabilized around the set "
      "value quickly. Adjustment of derivative time is dependent upon the "
      "amount of process lag, which ultimately will change the level of "
      "response.")

    P(b, lang,
      "Khi quá trình khởi động, hiệu chỉnh lớn do đặc tính của hành động vi "
      "phân đưa biến quá trình về gần giá trị cài đặt rất nhanh, nhờ đó giảm "
      "cả vượt quá lẫn dao động chu trình. Đáp ứng vi phân đã được thể hiện "
      "trong Hình 6.11.",
      "Initially when the process start-up takes place, large correction "
      "brought about by the characteristic derivative action brings the "
      "process variable near the set value quickly and thus reduces overshoot "
      "as well as cycling. The derivative response has been shown in Figure "
      "6.11.")
    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Đáp ứng của hành động điều khiển vi phân tuân theo biểu thức sau:",
      "Response of derivative control action is governed by the following "
      "expression:")
    E(b, lang, "E₀ = T_d · dE_s/dt + B", "E₀ = T_d · dE_s/dt + B", num="6.4")
    P(b, lang,
      "trong đó T_d là thời gian vi phân.",
      "where T_d is the derivative time.")

    P(b, lang,
      "Cài đặt điện tử của hành động vi phân được thể hiện trong Hình 6.12.",
      "Electronic implementation of derivative action has been shown in "
      "Figure 6.12.")
    FIG(b, 12, F.fig_f12(), lang)

    P(b, lang,
      "Ở đây hành động tỷ lệ cũng được đưa vào vì hành động tích phân cũng như "
      "vi phân không tồn tại độc lập. Chúng luôn được kết hợp riêng với hành "
      "động tỷ lệ để trở nên hữu ích trong một vòng điều khiển.",
      "Here proportional action has also been included because integral as "
      "well as derivative actions do not exist independently. These are "
      "always combined with proportional action separately for making them "
      "useful in a control loop.")

    P(b, lang,
      "Như quan sát từ sơ đồ, đầu ra đi qua tụ vi phân Cd và chỉ một phần của "
      "tổng đầu ra được đưa qua tụ phản hồi do sự hiện diện của bộ chia điện "
      "thế trong mạch đầu ra. Hiệu ứng là giảm dải tỷ lệ, cuối cùng dẫn đến "
      "sự thay đổi lớn hơn của đầu ra cho một tín hiệu đầu vào sai số nhất "
      "định. Trạng thái này tiếp diễn cho đến khi tụ vi phân Cd được nạp đầy. "
      "Thời gian trôi qua để nạp Cd liên quan tới hằng số thời gian của nó, "
      "có thể thay đổi nhờ điện trở biến đổi Rd dùng để chỉnh thời gian vi "
      "phân. Ảnh hưởng của bộ chia điện thế chấm dứt khi Cd được nạp đầy. Khi "
      "đó dải tỷ lệ được khôi phục về giá trị ban đầu.",
      "As is observed from the diagram, the output is passing through "
      "derivative capacitor Cd and only a portion of the total output is fed "
      "through feedback capacitor due to presence of potential divider in the "
      "output circuit. The effect is a decrease in proportional band, which "
      "ultimately results in greater change in output for a given error signal "
      "input. This status continues till the derivative capacitor charges "
      "fully. The time elapsed to charge the Cd is related to its time "
      "constant, which can be varied by the help of variable resistance Rd, "
      "which is used for adjustment of derivative time. The effect of "
      "potential divider ceases when the Cd gets fully charged. The "
      "proportional band is then restored to its original value.")

    P(b, lang,
      "Cài đặt khí nén của hành động vi phân được thể hiện trong Hình 6.13. "
      "Như có thể thấy từ hình, một tiết lưu nhỏ trên đường đầu ra đi tới buồng "
      "tỷ lệ tạo ra hành động vi phân bằng khí nén. Ở đây hành động vi phân "
      "cũng được thể hiện cùng với hành động tỷ lệ, làm nên một hệ thống "
      "hoàn chỉnh. Áp suất khí cấp là 1,4 kg/cm² như ghi trên hình.",
      "Pneumatic implementation of derivative action has been shown in Figure "
      "6.13. As it can be observed from the figure, a small restriction in the "
      "output line going to proportional bellows creates derivative action "
      "pneumatically. Here also the derivative action has been shown along "
      "with proportional action, which makes the system complete. The air "
      "supply is shown as 1.4 kg/cm² in the diagram.")
    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Đặc tính quan trọng nhất của hành động vi phân là nó thay đổi độ lợi "
      "tạm thời, giúp ổn định nhanh vòng điều khiển khi có thay đổi tải.",
      "The most important characteristic of the derivative action is that it "
      "changes the gain temporarily, which stabilizes the control loop "
      "quickly when load changes occur.")

    return b
