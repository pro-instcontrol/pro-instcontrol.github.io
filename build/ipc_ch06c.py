# -*- coding: utf-8 -*-
"""Chapter 6, section 6.3 "Integral control" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 292-294, printed pp. 280-282, decoded
text lines 11275-11352.  Covers integral (proportional speed floating)
action, its electronic and pneumatic implementations, offset elimination
and the numbered equation (6.3), transcribed from the printed page:

    E_o = (1/T_i) ∫ E_s dt + B

Figures 6.8-6.10 are supplied by the parallel `ipcfig6_*` agents.  When a
supplier has not registered a callable yet, a simple but genuine vector
redraw is installed through a non-overwriting `hasattr` fallback, so the
real supplier always wins once it becomes available.
"""

import ipcfig6 as F
import ipcfig6_common as FC
from vfig import (BLUE, GREEN, GREY, INK, _arrow, _circle, _defs, _line,
                  _poly, _rect, svg)
from ipc_ch06_lib import H, P, E, FIG

W, HGT = FC.W, FC.H


# --------------------------------------------------------- figure fallbacks
def _fig08():
    """Electronic integrator: input divider, Rv/Cin and op-amp with Cfb."""
    o = [_defs()]
    # input terminals and error-signal arrow
    o.append(_line(78, 92, 215, 92))
    o.append(_line(78, 176, 430, 176))
    o.append(_circle(78, 92, 2.6, fill=INK, sw=0))
    o.append(_circle(78, 176, 2.6, fill=INK, sw=0))
    o.append(_arrow(60, 172, 60, 96, color=BLUE))
    o.append(FC.T(30, 140, "Error signal", 7.2))
    o.append(FC.T(100, 82, "E<sub>in</sub>", 7.4))
    # potential divider R1 / R2 across the input
    o.append(_line(150, 92, 150, 100))
    o.append(_rect(146, 100, 8, 26, "#eef3fb"))
    o.append(_line(150, 126, 150, 134))
    o.append(_circle(150, 134, 2.4, fill=INK, sw=0))
    o.append(_line(150, 134, 150, 142))
    o.append(_rect(146, 142, 8, 26, "#eef3fb"))
    o.append(_line(150, 168, 150, 176))
    o.append(FC.T(120, 112, "R1", 7.2))
    o.append(FC.T(120, 156, "R2", 7.2))
    # integral adjustment: variable resistor Rv from divider midpoint
    o.append(_line(150, 134, 185, 134))
    o.append(_rect(185, 130, 30, 8, "#eef3fb"))
    o.append(_arrow(196, 122, 204, 130, color=GREY, sw=1.0))
    o.append(_line(215, 134, 240, 134))
    o.append(_line(240, 134, 262, 118))
    o.append(FC.T(200, 124, "R<sub>v</sub>", 7.4))
    o.append(FC.T(200, 152, "Integral adjustment", 7.0))
    # input capacitor Cin in series with the upper rail
    o.append(_line(215, 92, 222, 92))
    o.append(_line(222, 84, 222, 100))
    o.append(_line(229, 84, 229, 100))
    o.append(_line(229, 92, 262, 92))
    o.append(_line(262, 92, 262, 118))
    o.append(FC.T(200, 82, "C<sub>in</sub>", 7.4))
    # summing node and operational amplifier
    o.append(_circle(262, 118, 2.6, fill=INK, sw=0))
    o.append(_poly([(295, 96), (295, 172), (375, 134)], fill="#ffffff"))
    o.append(_line(262, 118, 295, 118))
    o.append(_line(295, 158, 430, 158))
    o.append(_line(430, 158, 430, 176))
    o.append(FC.T(288, 118, "−", 9.0))
    o.append(FC.T(288, 160, "+", 9.0))
    o.append(FC.T(335, 126, "Op.", 7.2))
    o.append(FC.T(335, 142, "Amp.", 7.2))
    # feedback capacitor Cfb
    o.append(_line(375, 134, 375, 62))
    o.append(_line(375, 62, 325, 62))
    o.append(_line(325, 54, 325, 70))
    o.append(_line(331, 54, 331, 70))
    o.append(_line(331, 62, 262, 62))
    o.append(_line(262, 62, 262, 118))
    o.append(FC.T(315, 52, "C<sub>fb</sub>", 7.4))
    # output and ground
    o.append(_line(375, 134, 555, 134))
    o.append(FC.T(565, 130, "E<sub>o</sub>", 7.4))
    o.append(_line(430, 176, 430, 184))
    for i, y in enumerate((184, 188, 192)):
        o.append(_line(430 - 7 + i * 2, y, 430 + 7 - i * 2, y, sw=0.9))
    return FC._mk(8, o, "Electronic integrator circuit",
                  "Mạch tích phân điện tử", "Electronic integrator circuit",
                  "Mạch điện tử thực hiện hành động tích phân, với Rv là bộ chỉnh tốc độ tích phân.",
                  "Electronic circuit implementing integral action, with Rv as the integral-rate adjustment.",
                  h=HGT)


def _fig09():
    """Response diagram: step in measured input, fixed set value, ramping output."""
    o = [_defs()]
    o.append(_arrow(90, 190, 92, 40, color=INK))
    o.append(_arrow(90, 190, 580, 190, color=INK))
    o.append(FC.T(560, 208, "Time", 7.4))
    # measured input step and its projection lines
    o.append(_poly([(100, 150), (180, 150), (180, 70), (320, 70),
                    (320, 150), (420, 150)], color=BLUE, sw=2.0))
    o.append(_line(180, 70, 180, 150, color=GREY, sw=0.9, dash="4 3"))
    o.append(_line(320, 70, 320, 168, color=GREY, sw=0.9, dash="4 3"))
    o.append(FC.T(340, 52, "Measurement input change", 7.5))
    o.append(_arrow(340, 60, 300, 68, color=BLUE, sw=1.0))
    # set value
    o.append(_line(90, 110, 430, 110, color=GREY, sw=1.3, dash="6 4"))
    o.append(_arrow(470, 110, 436, 110, color=GREY, sw=1.1))
    o.append(FC.T(500, 106, "Set value", 7.5, anchor="start"))
    # integral output ramps while the deviation persists
    o.append(_poly([(100, 150), (180, 150), (320, 168), (430, 168)],
                   color=GREEN, sw=2.0))
    o.append(_arrow(470, 168, 436, 168, color=GREEN, sw=1.1))
    o.append(FC.T(500, 164, "Output", 7.5, anchor="start"))
    return FC._mk(9, o, "Graphical representation of integral action",
                  "Đồ thị hành động tích phân", "Graphical representation of integral action",
                  "Đầu vào đo thay đổi dạng bậc, giá trị cài đặt không đổi và đầu ra thay đổi liên tục trong thời gian độ lệch tồn tại.",
                  "A step change in measured input, a constant set value and an output that keeps changing while the deviation persists.",
                  h=HGT)


def _fig10():
    """Pneumatic integrator: restriction, relay, flapper and two bellows."""
    o = [_defs()]
    # air supply and restriction
    o.append(_arrow(70, 72, 120, 72, color=BLUE))
    o.append(FC.T(72, 50, "Air supply", 7.2, anchor="start"))
    o.append(FC.T(72, 62, "1.4 kg/cm²", 7.2, anchor="start"))
    o.append(_line(70, 72, 520, 72))
    o.append(_poly([(424, 66), (424, 78), (432, 72)],
                   fill=INK, sw=0.6, close=True))
    o.append(_poly([(438, 66), (438, 78), (430, 72)],
                   fill=INK, sw=0.6, close=True))
    o.append(FC.T(431, 56, "Restriction", 7.2))
    # flapper operated by the process variable
    o.append(_circle(520, 72, 3, fill="#ffffff"))
    o.append(_line(516, 58, 528, 84, sw=1.5))
    o.append(FC.T(545, 52, "Flapper operated by", 7.0, anchor="start"))
    o.append(FC.T(545, 64, "process variable", 7.0, anchor="start"))
    # pneumatic relay
    o.append(_line(250, 72, 250, 100))
    o.append(_rect(170, 100, 120, 45, "#eef3fb"))
    o.append(FC.T(230, 118, "Pneumatic", 8.0))
    o.append(FC.T(230, 132, "relay", 8.0))
    o.append(_line(230, 145, 230, 172))
    # bellows bank with integral and proportional elements
    o.append(_line(200, 180, 520, 180, sw=1.2))
    for x0 in (238, 456):
        o.append(_poly([(x0 - 22, 180), (x0 - 16, 170), (x0 - 10, 180),
                        (x0 - 4, 170), (x0 + 2, 180), (x0 + 8, 170),
                        (x0 + 14, 180), (x0 + 20, 170), (x0 + 26, 180)],
                       color=INK, sw=1.1))
    # spring between the bellows
    o.append(_poly([(360, 180), (368, 168), (376, 180), (384, 168),
                    (392, 180), (400, 168), (408, 180), (416, 168),
                    (424, 180)], color=INK, sw=1.1))
    o.append(FC.T(392, 158, "Spring (K<sub>p</sub>)", 7.2))
    # integral restriction branch and output
    o.append(_poly([(262, 180), (262, 208), (304, 208), (304, 180)],
                   color=GREEN, sw=1.2))
    o.append(_rect(276, 204, 14, 8, "#eef3fb"))
    o.append(FC.T(283, 221, "Integral restriction", 7.0))
    o.append(FC.T(540, 180, "Proportional bellows", 7.0, anchor="start"))
    o.append(_arrow(150, 180, 124, 180, color=BLUE))
    o.append(FC.T(96, 186, "Output", 7.2, anchor="start"))
    return FC._mk(10, o, "Pneumatic integral controller",
                  "Điều khiển tích phân khí nén", "Pneumatic integral controller",
                  "Mạch khí nén bổ sung tiết lưu và ống màng tích phân cạnh ống màng tỷ lệ.",
                  "Pneumatic circuit adding an integral restriction and bellows beside the proportional bellows.",
                  h=HGT)


for _n, _builder in ((8, _fig08), (9, _fig09), (10, _fig10)):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _b=_builder: _b()))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    H(b, lang, "6.3 Điều khiển tích phân", "6.3 Integral control")

    P(b, lang,
      "Hành động điều khiển tích phân còn được gọi là điều khiển nổi tỷ lệ theo "
      "tốc độ (proportional speed floating control). Trong hành động này, đầu ra "
      "của bộ điều khiển thay đổi với tốc độ tỷ lệ với độ lệch. Độ lệch càng lớn "
      "thì đầu ra thay đổi càng nhanh; vì vậy, chừng nào độ lệch còn tồn tại thì "
      "sự thay đổi đầu ra còn tiếp diễn. Tác động của bộ điều khiển đáp ứng cả độ "
      "lớn lẫn thời gian tồn tại của độ lệch — đây là điểm đặc biệt của hành động "
      "điều khiển này. Việc áp dụng hiệu chỉnh được tiếp tục cho đến khi tạo ra "
      "đúng lượng hiệu chỉnh cần thiết cho mọi thay đổi tải. Vì tốc độ hiệu chỉnh "
      "tăng theo độ lớn của thay đổi tải, hành động này có thể đáp ứng cả những "
      "thay đổi tải nhanh, ngay cả khi tự điều chỉnh của quá trình kém. Do đó nó "
      "phù hợp với quá trình có hằng số thời gian nhỏ và thời gian trễ nhỏ, đồng "
      "thời có thể xử lý các thay đổi tải lớn.",
      "Integral control action is also known as proportional speed floating "
      "control. In this control action the controller output changes its value "
      "at a rate proportional to the deviation. The higher the deviation, the "
      "faster the change in controller output, and hence as long as the "
      "deviation persists the change in output continues. The action of the "
      "controller responds to the amount as well as the duration of the "
      "deviation; in this way the control action is unique. The application of "
      "correction continues until it produces the exact amount of correction "
      "for any load changes. Since the rate of correction increases according "
      "to the amount of load change, the action is able to cope with faster "
      "load changes even when self-regulation is considerably less. Naturally "
      "it is suitable for a process with a small time constant and small dead "
      "time, and it can also handle large load changes.")

    P(b, lang,
      "Việc thực hiện hành động tích phân có thể làm bằng mạch điện tử như Hình "
      "6.8. Một bộ chia điện thế được đặt trên tín hiệu đầu vào sai số Ein và "
      "một biến trở Rv mắc song song với Cin đóng vai trò bộ chỉnh tích phân. Khi "
      "có tín hiệu sai số Ein, bộ chia điện thế cùng với Rv tạo đường dẫn cho "
      "dòng điện chảy. Sự liên tục của dòng này phụ thuộc vào điện áp chênh lệch "
      "giữa biến quá trình và giá trị cài đặt. Theo cách đó, dòng phản hồi tiếp "
      "tục phóng qua Cfb chừng nào còn tín hiệu sai số Ein. Bộ khuếch đại tạo ra "
      "sự thay đổi liên tục ở đầu ra trong khi tín hiệu vào còn hiện diện; đó "
      "chính là hành động tích phân. Nếu tại một thời điểm tín hiệu sai số Ein "
      "về không, dòng đầu vào ngừng chảy. Dòng đầu vào, và do đó hành động tích "
      "phân, có thể thay đổi bằng cách chỉnh giá trị Rv; người ta yêu cầu dòng "
      "đầu ra tăng nhanh hơn để quan sát được sự thay đổi tương ứng trên Cfb, "
      "cho hành động tích phân nhanh hơn. Để có hành động tích phân chậm, bộ chia "
      "điện thế được đưa vào mạch đầu vào. Khi hành động tích phân được dùng "
      "cùng hành động tỷ lệ, giá trị điện trở tích phân xác định số lần hành động "
      "tỷ lệ được lặp lại trong một phút. Hành động tích phân được biểu diễn trên "
      "giản đồ đồ thị Hình 6.9.",
      "Implementation of integral action can be done electronically as "
      "indicated in Figure 6.8. A potential divider has been set across the "
      "error input signal Ein and a variable resistance unit Rv connected in "
      "parallel with Cin works as the integral adjustment unit. Whenever an "
      "error input signal Ein is present, the potential divider along with Rv "
      "provides a path for the flow of current. The continuity of this current "
      "depends upon the differential voltage available due to the difference "
      "between the process variable and the set value. The feedback current, in "
      "this way, continues to discharge through Cfb as long as an error input "
      "signal Ein is present. The amplifier provides a continuous variation in "
      "the output as long as the signal input is present, and this provides "
      "integral action. If at any time the error signal input Ein becomes zero, "
      "the input current stops flowing. The input current, and hence the "
      "integral action, can be varied by changing the value of Rv; the output "
      "current is required to increase at a faster rate so that a matching "
      "change can be observed across Cfb, resulting in faster integral action. "
      "To produce a slow integral action, the potential divider has been "
      "included in the input circuit. It will become clear later, when integral "
      "action is used in conjunction with proportional action, that the value "
      "of the integral resistance determines the number of times the "
      "proportional action is repeated per minute. The integral action has been "
      "indicated on the graphical diagram Figure 6.9.")

    FIG(b, 8, F.fig_f08(), lang)
    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Đầu ra của hành động điều khiển này được biểu diễn bằng biểu thức:",
      "Output of this control action is expressed by the expression:")
    E(b, lang, "E_o = (1/T_i) ∫ E_s dt + B", "E_o = (1/T_i) ∫ E_s dt + B",
      num="6.3")
    P(b, lang,
      "trong đó T_i là hằng số thời gian tích phân.",
      "where Ti is the integral time.")

    P(b, lang,
      "Việc thực hiện điều khiển tích phân ở dạng khí nén được tiến hành bằng "
      "cách thêm một tiết lưu tích phân và cụm ống màng đối với ống màng tỷ lệ "
      "(xem Hình 6.7), như trình bày ở Hình 6.10.",
      "Implementation of integral control in its pneumatic form can be done by "
      "adding an integral restriction and bellows combination unit against the "
      "proportional bellows (refer to Figure 6.7), as shown in Figure 6.10.")

    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Đặc tính quan trọng nhất của hành động tích phân là nó loại bỏ độ lệch do "
      "chỉ áp dụng hành động tỷ lệ gây ra.",
      "The most important characteristic of the integral action is that it "
      "eliminates the offset caused by applying proportional action alone.")

    return b
