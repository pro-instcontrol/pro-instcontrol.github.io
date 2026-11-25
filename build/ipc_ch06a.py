# -*- coding: utf-8 -*-
"""Chapter 6, section 6.1 "Introduction" and 6.1.1 "ON-OFF Control Action"
(EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 284-288, printed pp. 272-276, decoded
text lines 10908-11124. Figure 6.1 (measurement and valve-output cycling),
Figure 6.2 (electrical thermostatic switch and two relays) and Figure 6.3
(pneumatic restriction, nozzle, flapper and relay) are placed where the
printed prose refers to them. There are no numbered equations in this span.

The `ipcfig6_a` supplier is authored in parallel with this module. Until it
is importable, small but genuine vector redraws of the three printed
diagrams are installed as non-overwriting fallbacks; once the real supplier
registers `fig_f01` / `fig_f02` / `fig_f03`, those callables win.
"""

import math

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _T(x, y, s, size=8.0, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _box(x, y, w, h, fill="#eef3fb", stroke="#1f3a5f"):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
            'stroke="%s" stroke-width="1.1"/>' % (x, y, w, h, fill, stroke))


def _ar(x1, y1, x2, y2, mid, color="#1f3a5f"):
    return ('<path d="M%d %d L%d %d" fill="none" stroke="%s" '
            'stroke-width="1.2" marker-end="url(#%s)"/>' % (x1, y1, x2, y2, color, mid))


def _wire(pts, color="#1f3a5f"):
    d = "M" + " L".join("%d %d" % p for p in pts)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="1.2"/>' % (d, color))


def _dash(x1, y1, x2, y2, color="#9aa7b8"):
    return ('<path d="M%d %d L%d %d" fill="none" stroke="%s" stroke-width="0.9" '
            'stroke-dasharray="4 3"/>' % (x1, y1, x2, y2, color))


def _circ(x, y, r=3.0):
    return ('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" '
            'stroke="#1f3a5f" stroke-width="1.1"/>' % (x, y, r))


def _standalone_fig(n):
    mid = "ipc6a%d" % n
    o = ['<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
         'markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>' % mid]

    if n == 1:
        title = "ON-OFF control action"
        cvi = ("Điều khiển ON-OFF: tín hiệu đo dao động quanh giá trị cài đặt, "
               "đầu ra van bật giữa 100% và 0%")
        cen = ("ON-OFF control action: the measurement cycles about the set value "
               "while the valve output switches between 100% and 0%")
        avi = ("Đường đo lường dao động quanh giá trị cài đặt; tín hiệu tới van "
               "đóng cắt giữa 100% và 0% theo thời gian")
        aen = ("The measurement oscillates about the set value while the signal "
               "to the control valve switches between 100% and 0% over time")

        x0, x1 = 110, 560
        o.append(_wire([(x0, 45), (x0, 185)]))
        o.append(_dash(95, 75, 590, 75))
        o.append(_T(100, 78, "Set value", 7.6, anchor="end"))
        o.append(_dash(60, 130, x0, 130))
        o.append(_T(56, 133, "100%", 7.6, anchor="end"))
        o.append(_dash(60, 175, x0, 175))
        o.append(_T(56, 178, "0%", 7.6, anchor="end"))

        pts = []
        for i in range(0, 181):
            t = i / 180.0
            pts.append((x0 + t * (x1 - x0), 75 - 16.0 * math.sin(6 * math.pi * t)))
        d = "M" + " L".join("%.1f %.1f" % p for p in pts)
        o.append('<path d="%s" fill="none" stroke="#2e7d5b" stroke-width="1.7"/>' % d)

        for k in range(7):
            xs = x0 + k * (x1 - x0) / 6.0
            o.append(_dash(xs, 75, xs, 175, "#c3ccd8"))
            top = 130 if k % 2 == 0 else 175
            bot = 175 if k % 2 == 0 else 130
            o.append(_wire([(xs, top), (xs, bot)]))
            if k < 6:
                xe = x0 + (k + 1) * (x1 - x0) / 6.0
                o.append(_wire([(xs, bot), (xe, bot)]))

        o.append(_ar(472, 47, 442, 63, mid))
        o.append(_T(480, 50, "Measurement", 7.8, anchor="start", color="#2e7d5b"))
        o.append(_ar(x0, 195, 612, 195, mid))
        o.append(_T(620, 199, "Time", 7.8, anchor="start"))
        o.append(_T(62, 215, "Output signal to control valve", 7.8, anchor="start"))

    elif n == 2:
        title = "Electrical ON-OFF control implementation"
        cvi = ("Mạch điều khiển ON-OFF dùng điện: công tắc nhiệt TS, rơ le R1, R2 "
               "và tiếp điểm 1R1, 1R2")
        cen = ("Electrical ON-OFF control circuit: thermostatic switch TS, relays "
               "R1 and R2, and contacts 1R1 and 1R2")
        avi = ("Công tắc nhiệt TS đóng sẽ cấp điện cho rơ le R1; tiếp điểm 1R1 "
               "đóng cấp điện cho R2 và tiếp điểm 1R2 đưa nguồn tới tải")
        aen = ("Closing thermostatic switch TS energises relay R1; contact 1R1 "
               "then energises R2 and contact 1R2 feeds the controlled load")

        o.append(_ar(70, 158, 70, 58, mid))
        o.append(_T(28, 100, "Control", 7.6, anchor="start"))
        o.append(_T(28, 112, "supply", 7.6, anchor="start"))
        o.append(_wire([(70, 55), (610, 55)]))
        o.append(_wire([(70, 165), (610, 165)]))

        o.append(_box(145, 72, 50, 34))
        o.append(_circ(165, 82))
        o.append(_circ(182, 98))
        o.append(_wire([(165, 82), (182, 98)]))
        o.append(_T(202, 83, "TS", 8.0, anchor="start"))
        o.append(_wire([(170, 55), (170, 72)]))
        o.append(_wire([(170, 106), (170, 118)]))
        o.append(_box(155, 118, 30, 24))
        o.append(_T(170, 134, "R1", 7.8))
        o.append(_wire([(170, 142), (170, 165)]))
        o.append(_ar(112, 152, 148, 130, mid))
        o.append(_T(76, 158, "Thermostat", 7.6, anchor="start"))

        o.append(_circ(350, 80))
        o.append(_circ(350, 100))
        o.append(_wire([(350, 80), (350, 100)]))
        o.append(_T(362, 85, "1R1", 8.0, anchor="start"))
        o.append(_wire([(350, 55), (350, 80)]))
        o.append(_wire([(350, 100), (350, 118)]))
        o.append(_box(335, 118, 30, 24))
        o.append(_T(350, 134, "R2", 7.8))
        o.append(_wire([(350, 142), (350, 165)]))

        o.append(_circ(560, 80))
        o.append(_circ(560, 100))
        o.append(_wire([(560, 80), (560, 100)]))
        o.append(_T(572, 85, "1R2", 8.0, anchor="start"))
        o.append(_wire([(560, 55), (560, 80)]))
        o.append(_wire([(560, 100), (560, 118)]))
        o.append(_box(505, 118, 110, 30))
        o.append(_T(560, 136, "Supply to ON-OFF action.", 7.0))
        o.append(_wire([(560, 148), (560, 165)]))

    else:
        title = "Pneumatic ON-OFF control implementation"
        cvi = ("Mạch điều khiển ON-OFF khí nén: nguồn 1,4 kg/cm², bộ tiết lưu, "
               "vòi phun, cánh flap và rơ le khí nén")
        cen = ("Pneumatic ON-OFF control circuit: 1.4 kg/cm² supply, restriction, "
               "nozzle, flapper and pneumatic relay")
        avi = ("Áp suất cấp đi qua bộ tiết lưu và vòi phun tạo áp suất ngược "
               "tác động lên rơ le khí nén để tạo đầu ra ON-OFF")
        aen = ("Supply air through the restriction and nozzle builds a backpressure "
               "that drives the pneumatic relay into an ON-OFF output")

        o.append(_ar(48, 72, 190, 72, mid))
        o.append(_T(52, 54, "Pneumatic supply", 7.8, anchor="start"))
        o.append(_T(52, 64, "(1.4 kg/cm²)", 7.8, anchor="start"))
        o.append(_T(214, 58, "Restriction", 7.6))
        o.append(_box(204, 65, 22, 13, fill="#c9d4e4"))
        o.append(_wire([(226, 72), (385, 72)]))
        o.append(_wire([(385, 72), (385, 90)]))
        o.append(_T(403, 66, "Nozzle", 7.6, anchor="start"))
        o.append(_box(360, 90, 66, 58, fill="#ffffff"))
        o.append(_wire([(400, 94), (410, 137)]))
        o.append(_wire([(404, 137), (416, 137)]))
        o.append(_ar(432, 102, 412, 104, mid))
        o.append(_T(440, 99, "Flapper operated by", 7.6, anchor="start"))
        o.append(_T(440, 110, "process variable", 7.6, anchor="start"))
        o.append(_wire([(385, 100), (385, 114), (250, 114), (250, 125)]))
        o.append(_box(200, 125, 100, 35))
        o.append(_T(250, 140, "Pneumatic", 7.8))
        o.append(_T(250, 152, "relay", 7.8))
        o.append(_ar(250, 160, 250, 186, mid))
        o.append(_T(262, 181, "Output", 7.8, anchor="start"))

    o.append(_T(340, 242, "Hình 6.%d   ·   Figure 6.%d" % (n, n), 6.4, color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" fill="#ffffff"/>'
           '%s</svg>' % "".join(o))
    return (svg, "Hình 6.%d · %s" % (n, cvi), "Figure 6.%d · %s" % (n, cen),
            avi, aen)


for _n in (1, 2, 3):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 6.1
    H(b, lang, "6.1 Giới thiệu", "6.1 Introduction")

    P(b, lang,
      "Một quá trình gồm nhiều hoạt động có hệ thống (nhưng vận hành trong những "
      "ranh giới phối hợp với nhau), đi từng bước để tạo ra một đầu ra cuối cùng. "
      "Vì quá trình phải làm việc một cách có hệ thống và mạch lạc, cần có một "
      "dạng điều khiển nào đó đối với các hoạt động khác nhau của nó. Không cần "
      "phải nói rằng một hoạt động không được điều khiển của quá trình không bao "
      "giờ cho ra kết quả hữu ích, mà đôi khi còn gây hư hỏng nghiêm trọng cho "
      "thiết bị được nối với nó.",
      "A process consists of several systematic operations, functioning within "
      "co-ordinated boundaries, which go step by step to produce a final output. "
      "Since a process has to work systematically and in a coherent manner, some "
      "sort of control over its different activities is needed. It is needless to "
      "mention that an uncontrolled process activity can never deliver fruitful "
      "output; rather, it may sometimes result in severe damage to the connected "
      "equipment.")

    P(b, lang,
      "Sự hiện diện của điều khiển quá trình có thể thấy rõ ngay trong các hoạt "
      "động hằng ngày của con người. Các hành động của một người (từ lúc rời "
      "giường cho đến cả trong giấc mơ) là những ví dụ lớn nhất về một hệ thống "
      "điều khiển. Khi một người đi với mắt nhắm, đó được xem là ví dụ về hệ "
      "thống điều khiển hở, vì hai chân của người đó không có sự phối hợp. Chân "
      "không được điều khiển theo hướng nào cả và người đó thậm chí có thể bị ngã. "
      "Mặt khác, khi đi với mắt mở, tình huống hoàn toàn khác: mắt cùng với não "
      "liên tục quan sát hai chân một cách phối hợp. Mắt nhìn thấy trước các chướng "
      "ngại vật trên đường và gửi tín hiệu đầu vào tới não. Não thực hiện nhiều "
      "xử lý bên trong (cách thức thực hiện vẫn ít được chúng ta biết) và cuối "
      "cùng hướng chân đi đúng hướng. Cơ chế điều khiển dạng này được gọi là hệ "
      "thống điều khiển kín.",
      "The appearance of process control can be visualized very clearly in "
      "day-to-day human activity. The various actions of a human being, from "
      "rising in the morning even to dreaming, are the greatest examples of a "
      "control system. When a person walks with eyes closed, it is understood to "
      "be an example of an open-loop control system, because the legs do not move "
      "in a co-ordinated way. There is no control over the direction in which "
      "they move, and the person may even fall. When the person walks with eyes "
      "open, the situation is entirely different: the eyes, together with the "
      "brain, keep a constant and co-ordinated watch on the legs. The eyes see "
      "obstacles lying ahead on the path well in advance and accordingly send an "
      "input signal to the brain. The brain performs a great deal of internal "
      "manipulation, in a way that is still little known to us, and finally "
      "directs the legs towards the right direction. This type of control "
      "mechanism is known as a closed-loop control system.")

    P(b, lang,
      "Phản hồi, như ta gọi trong thuật ngữ điều khiển, xuất hiện tự nhiên trong "
      "một hệ thống kín. Thực tế, chính sự xuất hiện của phản hồi biến một hệ "
      "thống điều khiển hở thành hệ thống điều khiển kín. Trong ví dụ trên, mắt "
      "cùng với não tạo ra hoạt động phản hồi cần thiết. Mắt gửi tín hiệu đầu vào "
      "tới não; não so sánh với hướng đi trước đó và chỉnh lại chân để đổi hướng "
      "nếu cần.",
      "Feedback, as we call it in control terminology, appears naturally in a "
      "closed-loop system. In fact, it is the appearance of feedback that turns "
      "an open-loop control system into a closed-loop one. In the example above, "
      "the eyes together with the brain create the necessary feedback operation. "
      "The eye sends the input signal to the brain, which compares the previous "
      "direction of walking and redirects the legs to change direction if "
      "required.")

    P(b, lang,
      "Phản hồi âm là cơ chế điều khiển cơ bản cho toàn bộ hệ thống. Phản hồi âm "
      "điều chỉnh hướng đi sao cho khoảng cách giữa hướng đi trước đó và hướng "
      "mới được gán là nhỏ nhất. Dù vẫn tồn tại các cơ chế điều khiển khác, chẳng "
      "hạn phản hồi dương và điều khiển đón đầu, nhưng chúng không thể áp dụng "
      "cho ví dụ này. Các hệ thống đó có công dụng riêng và sẽ được trình bày ở "
      "những chỗ thích hợp.",
      "Negative feedback is the basic control mechanism for the whole system. "
      "It adjusts the direction of walking in such a way that the gap between the "
      "earlier direction of walking and the newly assigned direction is minimized. "
      "Although other control mechanisms also exist, for example positive "
      "feedback and feed forward, these cannot be applied in this example. Those "
      "systems have different utilities and will be described at the appropriate "
      "places.")

    P(b, lang,
      "Trong các ngành công nghiệp quá trình, các quá trình khác nhau cần những "
      "hệ thống điều khiển khác nhau. Yêu cầu về điều khiển dựa trên việc đạt "
      "đúng thông số kỹ thuật của sản phẩm. Có thể đáp ứng thông số đó bằng cách "
      "điều khiển thích hợp bốn biến công nghệ cơ bản là áp suất, nhiệt độ, lưu "
      "lượng và mức, ngoài ra còn có các biến khác. Những biến này luôn ở trạng "
      "thái động, và bất kỳ thay đổi đáng kể nào cũng cho thấy sự mất cân bằng "
      "năng lượng hoặc khối lượng. Vì vậy, chức năng quan trọng nhất của hệ thống "
      "điều khiển quá trình là thao tác cân bằng năng lượng hoặc khối lượng sao "
      "cho các biến chỉ thị này luôn nằm trong giới hạn quy định.",
      "In process industries, different processes require different control "
      "systems. The need for control is based on obtaining the right product "
      "specifications. The required specification can be met by suitably "
      "controlling the four basic process variables, namely pressure, temperature, "
      "flow and level, in addition to others. These process variables are always "
      "in a dynamic state, and any substantial change in them indicates an energy "
      "or mass unbalance. Thus the most important function of a process control "
      "system is to manipulate the energy or mass balance in such a way that "
      "these indicative variables are maintained within specified limits.")

    P(b, lang,
      "Bộ điều khiển tự động là thiết bị nhận biến công nghệ làm đầu vào và "
      "thao tác đầu vào này theo các giá trị cài đặt sao cho sai lệch được giảm "
      "thiểu tự động. Biến công nghệ được điều khiển như vậy gọi là biến được "
      "điều khiển. Bộ điều khiển hoạt động thông qua một môi trường khác (bộ "
      "điều khiển khí nén dùng không khí, bộ điều khiển điện tử dùng tín hiệu "
      "điện) để thực hiện hiệu chỉnh cần thiết cho biến công nghệ; môi trường "
      "này gọi là biến thao tác.",
      "An automatic controller is a device that takes the process variable as "
      "input and manipulates this process input with respect to set values so as "
      "to minimize the deviation automatically. The process variable so "
      "controlled is called the controlled variable. The controller operates "
      "through another medium, a pneumatic controller through air and an "
      "electronic controller through an electrical signal, in order to make the "
      "required correction in the process variable; this medium is called the "
      "manipulated variable.")

    P(b, lang,
      "Cách bộ điều khiển tự động thay đổi đầu ra của nó theo đầu vào của quá "
      "trình được gọi là tác động điều khiển. Về cơ bản có bốn tác động điều "
      "khiển, đôi khi còn gọi là bốn chế độ điều khiển:",
      "The manner in which an automatic controller changes its output with "
      "respect to the process input is known as control action. Basically there "
      "are four control actions, sometimes called modes of control:")

    L(b, lang,
      ["(i) Điều khiển ON-OFF;",
       "(ii) Điều khiển tỷ lệ;",
       "(iii) Điều khiển tích phân;",
       "(iv) Điều khiển vi phân."],
      ["(i) On-off control;",
       "(ii) Proportional control;",
       "(iii) Integral control;",
       "(iv) Derivative control."])

    P(b, lang,
      "Mỗi chế độ điều khiển đều có ưu điểm và hạn chế riêng. Một bộ điều khiển "
      "tự động có thể được thiết kế để chỉ tạo ra một trong bốn tác động trên, "
      "hoặc tổ hợp của hai hay ba tác động, nhằm điều khiển quá trình như mong "
      "muốn. Trước khi đi vào mô tả chi tiết từng tác động của bộ điều khiển, "
      "chúng ta sẽ xem xét các đặc tính của quá trình, vì chính những đặc tính "
      "này cuối cùng quyết định việc chọn loại tác động điều khiển.",
      "Each mode of control has its own advantages as well as limitations. An "
      "automatic controller can be designed to produce only one of the four "
      "actions, or a combination of two or three actions, for the desired process "
      "control. Before describing the different controller actions in detail, we "
      "shall study the various process characteristics that ultimately govern "
      "the choice of a particular type of control action.")

    P(b, lang,
      "Việc chọn tác động điều khiển phù hợp cho một điều kiện quá trình cụ thể "
      "dựa trên nhiều đặc tính của quá trình. Nhìn chung, quá trình biểu hiện "
      "hai hiệu ứng: (i) sự thay đổi của biến được điều khiển do thay đổi tải, và "
      "(ii) độ trễ về thời gian để biến công nghệ đạt giá trị mới khi xảy ra "
      "thay đổi tải, gọi là độ trễ quá trình. Độ trễ này thường do một hoặc nhiều "
      "đặc tính của quá trình gây ra, đó là sức chứa, thời gian chết và sức cản.",
      "The choice of a suitable controller action for a particular process "
      "condition is based on various process characteristics. In general, "
      "processes exhibit two effects: (i) variations in the controlled variable "
      "owing to load changes, and (ii) a delay in the time taken by the process "
      "variable to reach a new value when load changes occur, called process lag. "
      "Process lag is generally contributed by one or more process behaviours: "
      "capacitance, dead time and resistance.")

    P(b, lang,
      "Tải của một quá trình là tổng nhu cầu về tác nhân điều khiển (chất lỏng "
      "hoặc bất kỳ vật liệu nào khác) của quá trình tại một thời điểm bất kỳ. Vì "
      "phần tử điều khiển cuối cùng điều chỉnh lưu lượng của tác nhân điều khiển "
      "để giữ biến được điều khiển ở giá trị cài đặt, tải liên quan trực tiếp đến "
      "vị trí của phần tử điều khiển cuối cùng. Do đó, mỗi khi tải thay đổi lại "
      "cần một vị trí mới của phần tử điều khiển cuối cùng nhằm giảm sai lệch của "
      "biến được điều khiển so với giá trị cài đặt. Vì vậy, cả độ lớn lẫn tốc độ "
      "thay đổi của tải đều là những yếu tố quan trọng đối với một tác động điều "
      "khiển cụ thể.",
      "Load in any process is the total requirement of the control agent, fluid "
      "or any other material, for the process at any instant of time. Since the "
      "final control element regulates the flow of the control agent in order to "
      "keep the controlled variable at its set value, load is directly related to "
      "the position of the final control element. Therefore, every time load "
      "changes, a new position of the final control element is called for, to "
      "minimize the deviation of the controlled variable from the set value. "
      "Thus the magnitude as well as the rate of change of load are both "
      "important factors for a particular control action.")

    P(b, lang,
      "Một vấn đề khác là đôi khi không dễ nhận biết sự thay đổi tải. Ví dụ:",
      "Another problem is that sometimes load changes cannot be recognized "
      "easily. For instance:")

    L(b, lang,
      ["(i) sự thay đổi của điều kiện môi trường;",
       "(ii) sự thay đổi tốc độ phản ứng của quá trình;",
       "(iii) sự thay đổi thành phần của tác nhân điều khiển."],
      ["(i) change in ambient conditions;",
       "(ii) changes in the process reaction rate;",
       "(iii) changes in the composition of the control agent."])

    P(b, lang,
      "Ngoài ba dạng trên, dạng thay đổi tải chủ yếu vẫn là sự thay đổi nhu cầu "
      "về tác nhân điều khiển theo nhu cầu của sản phẩm cuối cùng.",
      "In addition to these three, the main form of load change is, however, "
      "the change in the requirement for the control agent according to the "
      "demand for the final product.")

    P(b, lang,
      "Sức chứa của một quá trình là khả năng chứa của nó đối với dòng tác nhân "
      "điều khiển. Sức chứa của quá trình có thể được coi là tỷ lệ với thời gian "
      "lưu giữ của nó. Các quá trình có sức chứa lớn có xu hướng lớn hơn trong "
      "việc giữ biến được điều khiển ở giá trị cài đặt dù tải thay đổi mạnh. "
      "Nhưng hạn chế của quá trình có sức chứa lớn, tức thời gian lưu giữ dài, "
      "là biến được điều khiển không dễ đạt được giá trị mới. Đó là vì sức chứa "
      "lớn tạo ra độ trễ giữa thời điểm bắt đầu thay đổi tác nhân điều khiển và "
      "thời điểm biến được điều khiển phản ánh sự thay đổi đó. Ở đây xuất hiện "
      "một thuật ngữ mới là tốc độ phản ứng của quá trình. Hiệu ứng của hành động "
      "hiệu chỉnh do một tác động điều khiển thực hiện nhằm giữ biến được điều "
      "khiển ở giá trị cài đặt phụ thuộc vào tốc độ phản ứng của quá trình.",
      "The capacitance of a process is its holding capacity with respect to the "
      "flow of the control agent. It may be considered proportional to the "
      "retention time of the process. Processes with large capacitance have a "
      "greater tendency to maintain the controlled variable at its set value in "
      "spite of severe load changes. But the limitation of a high-capacity "
      "process, with its long retention time, is that the controlled variable "
      "cannot easily achieve a new value. This is because higher capacitance "
      "introduces a time lag between the moment a change is initiated in the "
      "control agent and the moment the controlled variable reflects that change. "
      "A new term now appears: the process reaction rate. The effect of the "
      "corrective action brought about by a control action to keep the controlled "
      "variable at its set value depends on the process reaction rate.")

    P(b, lang,
      "Sức cản, được định nghĩa là sự chống lại tự nhiên đối với dòng chảy, là "
      "đặc tính cơ bản thứ hai của quá trình. Nếu đang gia nhiệt một vật liệu "
      "trong quá trình có sức cản nhiệt lớn, cần nhiều tác nhân điều khiển hơn "
      "để tạo ra sự thay đổi nhiệt độ đáng kể trong vật liệu. Ngược lại, nhu cầu "
      "này giảm mạnh trong quá trình có sức cản nhiệt nhỏ.",
      "Resistance, defined as the natural opposition to flow, is the second "
      "basic characteristic of a process. If a material is being heated in a "
      "process with higher thermal resistance, more control agent is required to "
      "bring about a substantial temperature change in the material. On the "
      "other hand, this requirement falls drastically in a process with lower "
      "thermal resistance.")

    P(b, lang,
      "Một số quá trình có hệ thống đa sức chứa, chẳng hạn hệ thống đo nhiệt độ "
      "với vòi phun nhiệt, sau đó là ống bảo vệ nhiệt và cuối cùng là phần tử đo "
      "nhiệt độ. Năng lượng nhiệt chảy từ sức chứa này sang sức chứa kia, tạo "
      "thành hệ thống đo có nhiều sức chứa. Độ trễ trong đáp ứng do hệ thống đo "
      "đa sức chứa tạo ra được gọi là độ trễ truyền. Lĩnh vực chịu ảnh hưởng nặng "
      "nhất bởi độ trễ truyền là hệ thống điều khiển nhiệt độ. Điều này thực sự "
      "giới hạn chính tốc độ truyền nhiệt tới tác nhân điều khiển để tác động lên "
      "biến được điều khiển. Hiện tượng này tạo ra sự vượt giá trị cài đặt, vì "
      "việc truyền nhiệt tới tác nhân điều khiển không được cảm nhận ngay, và do "
      "đó không có thay đổi nào có thể được khởi xướng bởi tác động điều khiển.",
      "Some processes have a multi-capacitance system, for example a temperature "
      "measurement system in which there is a thermo-nozzle, then a thermo-well "
      "and finally the temperature element. Heat energy flows from one capacitance "
      "to another, forming a multi-capacity measurement system. The time lag in "
      "the response created by such a multi-capacitance measurement system is "
      "called transfer lag. The area most affected by transfer lag is the "
      "temperature control system. In fact this limits the very rate at which "
      "heat is transferred to the control agent to effect control of the "
      "controlled variable. This generates an overshoot around the set value, "
      "because the transfer of heat to the control agent is not sensed "
      "immediately and consequently no change can be initiated by the control "
      "action.")

    P(b, lang,
      "Có một dạng trễ khác gọi là thời gian chết, độ trễ vận chuyển, hoặc độ trễ "
      "khoảng cách – vận tốc. Dạng này do vấn đề lắp đặt thiết bị gây ra. Nếu "
      "phần tử điều khiển cuối cùng được lắp ở khoảng cách đáng kể so với hệ "
      "thống đo, hoặc hệ thống đo được lắp xa quá trình thực tế, thì sẽ xuất "
      "hiện dạng trễ này. Nó gây chậm đáp ứng của hệ thống đo, và cuối cùng dẫn "
      "đến chậm hành động của phần tử điều khiển cuối cùng.",
      "There is another kind of lag, called dead time, transport lag or "
      "distance-velocity lag. It is created by an instrument-installation "
      "problem. If a final control element has been installed at an appreciable "
      "distance from the measurement system, or the measurement system has been "
      "installed away from the actual process, this type of lag results. It "
      "creates a delay in the response of the measurement system, which "
      "ultimately results in a delay in the action of the final control element.")

    P(b, lang,
      "Từ thảo luận trên có thể thấy rõ thời gian chết hay độ trễ vận chuyển là "
      "yếu tố khó nhất đối với điều khiển. Việc dự báo độ trễ và quyết định hành "
      "động hiệu chỉnh thực sự gây khó khăn cho một vòng điều khiển. Mặt khác, "
      "sức chứa không phải là yếu tố khó; nó tạo ra sự tự điều chỉnh, cuối cùng "
      "hướng tới khôi phục trạng thái cân bằng.",
      "From the above discussion it is clear that dead time, or transport lag, "
      "is the difficult element as far as control is concerned. It is really "
      "troublesome for a control loop to anticipate the delay and decide on "
      "corrective action. Capacitance, on the other hand, is not a difficult "
      "element; it creates self-regulation, which ultimately acts towards "
      "restoring the equilibrium condition.")

    # ------------------------------------------------------------ 6.1.1
    H(b, lang, "6.1.1 Điều khiển ON-OFF", "6.1.1 ON-OFF Control Action",
      level=3)

    P(b, lang,
      "Tác động điều khiển ON-OFF về bản chất là điều khiển hai vị trí. Điều này "
      "nghĩa là đầu ra của bộ điều khiển ở mức lớn nhất cho một tập hợp điều kiện "
      "này và ở mức nhỏ nhất cho một tập hợp điều kiện khác, không có vị trí điều "
      "khiển trung gian nào. Giả sử giá trị cài đặt cho dạng điều khiển này là "
      "60%, điểm điều khiển cực đại cho một tập điều kiện là 65% và điểm điều "
      "khiển cực tiểu là 55%. Trong điều kiện đó, đầu ra bộ điều khiển nhận hai "
      "vị trí nói trên và tiếp tục dao động giữa chúng. Vì vậy, dải điều khiển là "
      "10%, tức ± 5% so với giá trị cài đặt 60%.",
      "An ON-OFF control action is necessarily a two-position control. This "
      "means the controller output is at a maximum for one set of conditions and "
      "at a minimum for another set of conditions, with no intermediate position "
      "of control at all. Suppose the set value for this kind of control action "
      "is 60%, the maximum control point for one set of conditions is 65% and the "
      "minimum control point is 55%. Under these conditions the controller output "
      "takes the two positions mentioned above and continues to move between "
      "them. The control band is therefore 10%, or ± 5% with respect to the 60% "
      "set value.")

    P(b, lang,
      "Nhược điểm của dạng điều khiển này là chu trình thay đổi giữa 65% và 55% "
      "tiếp diễn vô hạn, vì dạng điều khiển này không thể cân bằng giữa cung cấp "
      "và tải của hệ thống. Dù vậy, chế độ này rất phổ biến cho các dịch vụ điều "
      "khiển mà chỉ cần tác động ON-OFF, tức chỉ giữ hệ thống quá trình nằm trong "
      "tầm kiểm soát. Ví dụ:",
      "The defect of this kind of control action is that the cycle of variation "
      "between 65% and 55% continues indefinitely, because this control action "
      "cannot balance supply against load in the control system. Even so, this "
      "mode of control is very popular for control services where ON-OFF action "
      "is sufficient, merely to keep the process system under control. For "
      "example:")

    L(b, lang,
      ["điều khiển hệ thống sưởi trong gia đình;",
       "điều khiển nhiệt độ của hệ thống làm lạnh;",
       "điều khiển mức của bồn nước trên cao."],
      ["control of a domestic heating system;",
       "temperature control of a refrigeration system;",
       "level control of an overhead water tank."])

    P(b, lang,
      "Tất cả ba hệ thống này, cũng như các hệ thống tương tự khác, đều cần một "
      "công tắc vận hành ON-OFF được khởi động bằng hệ thống nhiệt hoặc bằng "
      "công tắc mức kiểu thủy ngân lắp tại hiện trường.",
      "All three of these systems, as well as other similar systems, are "
      "required to have an ON-OFF operating switch initiated by a thermostatic "
      "system or by a field-mounted level switch of the mercury type.")

    P(b, lang,
      "Trong vận hành thực tế thông thường, tín hiệu đầu ra của bộ điều khiển "
      "bật ON khi đầu vào tín hiệu đo nằm dưới giá trị cài đặt và tắt OFF khi đầu "
      "vào ở mức cao nhất so với giá trị cài đặt. Nhưng luôn tồn tại một khe hở "
      "hẹp, trông như một sai số, giữa hai sự thay đổi bắt đầu tác động thực tế "
      "này. Đặc tính đó có lợi vì làm giảm hiệu ứng dao động lặp. Dao động lặp "
      "gây thêm xáo trộn cho vận hành quá trình và cũng gây mòn bên trong van "
      "điều khiển. Thời gian chu kỳ của tác động bộ điều khiển phụ thuộc vào "
      "thời gian chết của quá trình. Thời gian chết này xác định thời điểm đảo "
      "chiều của tín hiệu đầu vào đo cắt ngang giá trị cài đặt. Các quá trình có "
      "sức chứa lớn có hằng số thời gian dài, làm tín hiệu đầu vào đo thay đổi "
      "chậm. Điều này cuối cùng tạo ra một dải hẹp quanh giá trị cài đặt; nếu "
      "chu trình dao động chậm và đều đặn thì tác động điều khiển là thỏa mãn. "
      "Tác động điều khiển được chỉ ra trong Hình 6.1.",
      "In normal practical operation, the controller output signals ON when the "
      "measurement input is below the set value and triggers OFF when the input "
      "is at its highest with respect to the set value. But a narrow gap, which "
      "appears as an error, always exists between these two changes that start "
      "the actual operation. This characteristic is advantageous because it "
      "minimizes the cycling effect. Cycling causes further upsets in process "
      "operation and also contributes to wear in the internals of control valves. "
      "The cycle time of controller action depends on process dead time. Process "
      "dead time determines the reversal time of the measurement input signal as "
      "it crosses the set value. Large-capacity processes have a long time "
      "constant, resulting in a slow change in the measurement input signal. "
      "This ultimately makes a narrow band around the set value; if the cycle is "
      "slow and systematic, the control action is satisfactory. The control "
      "action is indicated in Figure 6.1.")

    FIG(b, 1, F.fig_f01(), lang)

    P(b, lang,
      "Điều khiển ON-OFF đạt hiệu năng tốt nhất khi dải tỷ lệ nhỏ hơn 1%, tức độ "
      "lợi lớn nhất, tốc độ phản ứng của quá trình chậm, thời gian chết thấp và "
      "độ trễ truyền thấp. Tuy nhiên, nếu sự thay đổi của quá trình, phản ánh "
      "qua tín hiệu đầu vào đo, nhạy hơn đối với dao động của nguồn cung, thì độ "
      "lớn và tần số của chu trình dao động bắt đầu tăng. Điều này cuối cùng đòi "
      "hỏi một dạng tác động điều khiển được cải tiến hơn, sẽ được thảo luận sau.",
      "ON-OFF control is at its best in performance when the proportional band "
      "is less than 1%, that is, at maximum gain, with a slow process reaction "
      "rate, low dead time and low transfer lag. However, if the change in the "
      "process, reflected in the measurement input signal, is more sensitive to "
      "fluctuation in supply, the amplitude as well as the frequency of the cycle "
      "start to increase. This ultimately calls for a comparatively more improved "
      "version of control action, which will be discussed a little later.")

    P(b, lang,
      "Việc triển khai tác động điều khiển ON-OFF bằng điện được thể hiện trong "
      "Hình 6.2.",
      "The electrical implementation of ON-OFF control action is shown in "
      "Figure 6.2.")

    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Như trong sơ đồ, khi công tắc TS (nhiệt) đóng ở một nhiệt độ xác định, "
      "được cài đặt theo yêu cầu của quá trình, rơ le R1 được cấp điện. Tiếp "
      "điểm thường mở NO 1R1 của rơ le R1 đóng và cấp điện cho rơ le R2 khác; "
      "tiếp điểm thường mở NO 1R2 của rơ le này đóng và đưa nguồn tới tác động "
      "ON-OFF cho vận hành quá trình, làm cắt hệ thống sưởi. Khi hệ thống nguội "
      "đến một nhiệt độ quy định, hoạt động sưởi lại bắt đầu.",
      "As shown in the diagram, when the thermostatic switch TS closes at a "
      "particular temperature, set according to the requirement of the process, "
      "relay R1 is energized. The normally open (NO) contact 1R1 of relay R1 "
      "closes and energizes another relay R2, whose normally open contact 1R2 "
      "closes and sends supply for the ON-OFF action of the process operation, "
      "cutting off the heating system. When the system cools to a specified "
      "temperature, heating starts once again.")

    P(b, lang,
      "Việc triển khai tác động điều khiển ON-OFF bằng khí nén được thể hiện "
      "trong Hình 6.3.",
      "The pneumatic implementation of ON-OFF control action is shown in "
      "Figure 6.3.")

    FIG(b, 3, F.fig_f03(), lang)

    NOTE(b, lang,
      "<b>Ghi nhớ.</b> Giá trị cài đặt 60% với các điểm điều khiển 65% và 55% "
      "cho dải điều khiển 10%, tức ± 5%. Điều khiển ON-OFF tốt nhất khi dải tỷ lệ "
      "dưới 1%; nguồn khí nén của Hình 6.3 là 1,4 kg/cm².",
      "<b>Remember.</b> The 60% set value with control points at 65% and 55% "
      "gives a 10% control band, that is ± 5%. ON-OFF control performs best with "
      "a proportional band below 1%; the pneumatic supply in Figure 6.3 is "
      "1.4 kg/cm².")

    return b
