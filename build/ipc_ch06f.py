# -*- coding: utf-8 -*-
"""Chapter 6, sections 6.6-6.7: PID control and integral windup.

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 300-303, printed pp. 288-291, decoded
text lines 11538-11689.  Covers the PID response, the electronic and
pneumatic implementations of PID, the steady-state and transient response
conditions, the suitability of PID for temperature loops (including the
printed gain setting of 1 to 10), integral windup, the recovery delay and
the low/high limit-selector limiter circuit with bias and preload, with
Figures 6.16-6.18.

The text layer scrambles the figure labels; they were checked against the
page renders.  There are no numbered equations, tables or references in
this portion, so none are invented.  Figure suppliers are written in
parallel; non-overwriting fallbacks are installed below only when a
supplier has not yet been registered.
"""

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
_FIG_STUB_TEXT = {
    16: ("Mạch điện tử bộ điều khiển PID", "Electronic PID controller circuit"),
    17: ("Mạch khí nén bộ điều khiển PID", "Pneumatic PID controller circuit"),
    18: ("Mạch giới hạn chống tích phân bão hòa", "Integral-windup limiter circuit"),
}


def _stub_fig(n):
    cvi, cen = _FIG_STUB_TEXT[n]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250"><rect width="680" height="250" '
        'fill="#ffffff"/><text x="340" y="120" text-anchor="middle" '
        'font-size="14" fill="#1f3a5f">Figure 6.%d</text></svg>' % n
    )
    return (svg, "Hình 6.%d · %s" % (n, cvi),
            "Figure 6.%d · %s" % (n, cen),
            "Sơ đồ minh họa Hình 6.%d" % n,
            "Illustration for Figure 6.%d" % n)


for _n in range(16, 19):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 6.6
    H(b, lang,
      "6.6 Điều khiển tỷ lệ – tích phân – vi phân (PID)",
      "6.6 Proportional-cum-Integral-cum-Derivative (PID) Control")

    P(b, lang,
      "Như tên gọi (PID) cho thấy, đầu ra của bộ điều khiển PID phụ thuộc vào "
      "độ lớn, thời gian tồn tại và tốc độ thay đổi của độ lệch giữa biến quá "
      "trình (biến được điều khiển) và giá trị đặt. Sự kết hợp các tác động "
      "điều khiển này mang theo hiệu ứng bù cho hằng số thời gian lớn với "
      "đáp ứng ban đầu chậm, như thấy trong hệ thống điều khiển nhiệt độ. "
      "Sự kết hợp này mang lại tính ổn định ngoài việc loại bỏ độ lệch do "
      "riêng tác động tỷ lệ gây ra. Nó xử lý rất hiệu quả các thay đổi tải "
      "chậm và lớn, đồng thời cũng dùng được trong các ứng dụng mà hằng số "
      "thời gian nhỏ, thời gian chết lớn và tải thay đổi lớn, nhanh. Tóm lại, "
      "sự kết hợp này có thể xử lý bất kỳ tải khó khăn nào.",
      "As the name (PID) suggests, the output of a PID controller depends on "
      "the magnitude, the duration and the rate of change of the deviation "
      "between the process variable (controlled variable) and the set value. "
      "This combination of control actions carries the compensation effect "
      "needed for a large time constant with an initially slow response, "
      "such as is found in temperature control systems. The combination "
      "brings stability in addition to removing the offset caused by "
      "proportional action alone. It can handle slow and large load changes "
      "very effectively, and also applications in which the time constant "
      "is small, the dead time is large, and the load changes are large and "
      "fast. In short, this combination can handle any difficult load.")

    P(b, lang,
      "Thực tế, tác động vi phân trước tiên tạo ra một sự hiệu chỉnh lớn ngay "
      "khi xuất hiện độ lệch, làm cho phần tử điều khiển cuối cùng dịch "
      "chuyển xa hơn mức thực sự cần thiết và áp dụng nhiều hiệu chỉnh hơn "
      "mức yêu cầu. Vì vậy bộ điều khiển bắt đầu hoạt động để loại bỏ ảnh "
      "hưởng của sự hiệu chỉnh ban đầu lớn đó, chỉ còn lại sự hiệu chỉnh do "
      "đáp ứng PI tạo ra để xác định vị trí cuối cùng của phần tử điều khiển "
      "cuối cùng. Sự thay đổi sớm và thặng dư của đầu vào quá trình có xu "
      "hướng trung hòa tác động không mong muốn của độ trễ quá trình; đó là "
      "một sự hiệu chỉnh thặng dư tạm thời tỷ lệ với mức độ của độ lệch.",
      "In fact, derivative action first provides a large correction as soon "
      "as a deviation occurs, which moves the final control element further "
      "than is actually required and applies more correction than is needed. "
      "The controller therefore starts working to remove the effect of that "
      "large initial correction, leaving only the correction provided by the "
      "PI response to determine the final position of the final control "
      "element. The early and extra change of the process input tends to "
      "counteract the unwanted effect of process lags; it is a temporary "
      "extra correction proportional to the amount of deviation.")

    FIG(b, 16, F.fig_f16(), lang)

    P(b, lang,
      "Hình 6.16 cho thấy sơ đồ hiện thực điện tử của bộ điều khiển PID. Độ "
      "lợi của bộ điều khiển được điều chỉnh bằng chiết áp chỉnh dải tỷ lệ, "
      "làm thay đổi lượng phản hồi âm theo yêu cầu của đặc tính quá trình. "
      "Việc chỉnh tốc độ tích phân tạo phản hồi dương để loại bỏ độ lệch khi "
      "có thay đổi tải. Việc chỉnh vi phân tạo phản hồi âm để có độ ổn định "
      "hoàn hảo của hệ thống.",
      "Figure 6.16 shows the schematic of the electronic implementation of "
      "the PID controller. The gain of the controller is regulated by means "
      "of the proportional-band adjustment potentiometer, which changes the "
      "amount of negative feedback according to the requirements of the "
      "process characteristics. Integral-rate adjustment provides positive "
      "feedback for the elimination of offset in the event of load changes. "
      "Derivative adjustment provides negative feedback for perfect system "
      "stability.")

    P(b, lang,
      "Sơ đồ Hình 6.17 cho thấy cách hiện thực khí nén của bộ điều khiển PID. "
      "Như đã đề cập trước đó, các tiết lưu — cả vi phân lẫn tích phân — "
      "được tạo ra bằng cách lắp các van kim được thiết kế đặc biệt. Các van "
      "kim này có cần điều chỉnh nhỏ, được tiết lưu trong đường dẫn để chỉnh "
      "tác động vi phân và tác động tích phân.",
      "The diagram in Figure 6.17 shows the pneumatic implementation of the "
      "PID controller. As mentioned earlier, the restrictions — both "
      "derivative and integral — are created by installing specially designed "
      "needle valves. These needle valves have small adjustable stems, which "
      "are throttled in the lines to adjust the derivative and integral "
      "actions.")

    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Trong trường hợp bình thường, một thay đổi tải làm biến quá trình lệch "
      "khỏi giá trị đặt, tạo ra tín hiệu sai số. Các tác động điều khiển sau "
      "đó cố đưa biến quá trình trở về giá trị đặt ban đầu. Trong tình huống "
      "lý tưởng, một nhiễu loạn của hệ thống phải kích hoạt đáp ứng ngay lập "
      "tức để tạo ra điều khiển chặt chẽ, nhưng trên thực tế tình huống hoàn "
      "toàn khác. Do các đặc tính quá trình điển hình như thời gian chết, "
      "hằng số thời gian và sự giảm chấn, điều khiển chặt chẽ là không thể. "
      "Sai số phát sinh ban đầu hoạt động để giảm độ lệch của biến quá trình "
      "so với giá trị đặt. Tuy nhiên, sự hiệu chỉnh do phần tử điều khiển "
      "cuối cùng áp dụng làm biến quá trình vượt quá giá trị đặt, làm đảo "
      "ngược sai số đã tạo ra. Hệ thống sau đó bắt đầu hiệu chỉnh sai số mới "
      "này và biến quá trình lại vượt quá giá trị đặt một lần nữa, lại đảo "
      "ngược cơ chế sai số. Quá trình này tiếp tục tạo ra dao động của biến "
      "quá trình quanh giá trị đặt. Nếu biên độ dao động tắt dần theo thời "
      "gian, cuối cùng đạt được trạng thái ổn định; mặt khác, nếu biên độ "
      "bằng cách nào đó được duy trì, không đạt được trạng thái ổn định. Hai "
      "tình huống cực đoan này của tiêu chuẩn ổn định được gọi lần lượt là "
      "điều kiện đáp ứng trạng thái ổn định và điều kiện đáp ứng quá độ.",
      "In the normal case, a load change deviates the process variable from "
      "its set value, producing an error signal. The controller actions then "
      "attempt to return the process variable to the original set value. In "
      "an ideal situation a system disturbance should trigger an immediate "
      "response to produce tight control, but in practice the situation is "
      "quite different. Because of typical process characteristics such as "
      "dead time, time constant and damping, tight control is impossible. "
      "The error developed initially works to reduce the deviation of the "
      "process variable from its set value. The correction applied by the "
      "final control element, however, causes the process variable to "
      "overshoot the set value, thereby reversing the error. The system then "
      "starts correcting this new error, and the process variable overshoots "
      "the set value once again, reversing the error mechanism again. This "
      "continues to create oscillations in the process variable about the "
      "set value. If the amplitude of these oscillations dies down with "
      "time, a stable condition is eventually achieved; if, on the other "
      "hand, the amplitude is somehow maintained, no stable condition is "
      "reached. These two extreme situations of the stability criterion are "
      "known as the steady-state response condition and the transient "
      "response condition respectively.")

    P(b, lang,
      "Kiểu đáp ứng mà một hệ thống tạo ra đối với thay đổi tải tạo thành "
      "tiêu chuẩn đánh giá chất lượng điều khiển. Các bài toán điều khiển "
      "gặp trong công nghiệp quá trình nói chung là những bài toán đòi hỏi "
      "độ ổn định hoàn toàn trước các nhiễu loạn của quá trình, kèm theo "
      "đáp ứng nhanh trong các điều kiện vận hành đã quy định. Tác động "
      "điều khiển này (PID) rất phù hợp với các bài toán điều khiển nhiệt độ. "
      "Đặc tính của quá trình và cài đặt độ lợi được mô tả như sau:",
      "The type of response that a particular system generates to load "
      "changes forms the criterion of quality of control. The control "
      "problems encountered in the process industries are generally those "
      "that require complete stability against process upsets followed by a "
      "rapid response under specified operating conditions. This controller "
      "action (PID) is most suitable for temperature control problems. The "
      "characteristics of the process and the gain setting are described "
      "below:")

    L(b, lang,
      ["Độ chứa = hai hoặc nhiều hơn (hoặc lớn)",
       "Độ trễ truyền = trung bình hoặc lớn",
       "Thời gian chết = nhỏ hoặc lớn",
       "Cài đặt độ lợi = 1 đến 10"],
      ["Capacitance = two or more (or large)",
       "Transfer lag = medium or large",
       "Dead time = small or large",
       "Gain setting = 1 to 10"])

    # ---------------------------------------------------------------- 6.7
    H(b, lang,
      "6.7 Tích phân bão hòa",
      "6.7 Integral Windup")

    P(b, lang,
      "Tích phân bão hòa là đặc tính điển hình thấy ở bất kỳ bộ điều khiển "
      "nào có tác động tích phân hoạt động cùng với một tác động khác. Hành "
      "vi cơ bản của tác động tích phân là tiếp tục thay đổi đầu ra chừng "
      "nào còn độ lệch giữa biến quá trình và giá trị đặt. Bộ điều khiển áp "
      "dụng sự hiệu chỉnh theo cách của nó và cứ tiếp tục mở phần tử điều "
      "khiển cuối cùng. Nhưng nếu không có nguồn cung cấp vật liệu quá trình "
      "với số lượng đủ, hoặc nguồn cung cấp bị cắt hoàn toàn do van cô lập "
      "bị đóng hay bơm bị hỏng, thì tác động hiệu chỉnh do điều khiển tạo ra "
      "có thể không có hiệu quả. Tuy nhiên, đầu ra của bộ điều khiển vẫn "
      "tiếp tục tăng cho đến khi đạt đến trạng thái bão hòa. Trạng thái đó "
      "được gọi là tích phân bão hòa.",
      "Integral windup is a typical characteristic found in any controller "
      "unit that has integral mode in action in addition to another mode. "
      "The basic behaviour of integral mode is to continue changing its "
      "output as long as there is a deviation between the process variable "
      "and the set value. The controller applies the correction in its own "
      "way and goes on opening the final control element. But if there is no "
      "supply of process material in sufficient quantity, or the supply is "
      "completely cut off because an isolation valve has been closed or a "
      "pump has failed, the corrective action generated by the control "
      "action may not be effective. The controller output, however, "
      "continues to increase until it reaches a state of saturation. Such a "
      "state is called integral windup.")

    P(b, lang,
      "Khó khăn do tích phân bão hòa gây ra xuất hiện khi van cô lập đã đóng "
      "trên đường dẫn bất ngờ mở ra, hoặc bơm đã hỏng bất ngờ chạy lại. Trong "
      "tình huống này, khi nguồn cung cấp cho quá trình được phục hồi, yêu "
      "cầu bình thường là hoạt động của bộ điều khiển cũng phải phục hồi. "
      "Nhưng do tình trạng tích phân bão hòa đang tồn tại trong bộ điều "
      "khiển, nó sẽ không trở về hoạt động bình thường kịp thời ngay cả khi "
      "độ lệch giữa biến quá trình và giá trị đặt đã trở về không. Tình huống "
      "này kéo dài cho đến khi trạng thái bão hòa biến mất.",
      "The difficulty caused by integral windup is experienced when the "
      "closed isolation valve in the line suddenly opens, or the failed pump "
      "suddenly starts. Under this condition, when the supply to the process "
      "resumes, the normal requirement is that controller operation should "
      "also resume. But because of the integral windup condition prevailing "
      "in the controller, it will not return to normal operation in time "
      "even if the deviation between the process variable and the set value "
      "has returned to zero. This situation continues until the saturation "
      "state vanishes.")

    P(b, lang,
      "Để loại bỏ tình huống này trong thực tế, bộ điều khiển được trang bị "
      "mạch giới hạn, ngăn không cho đầu ra vượt quá giới hạn bão hòa. Mạch "
      "giới hạn gồm các công tắc chọn giới hạn thấp và cao kết hợp với một "
      "bộ khuếch đại độ lợi cao. Công tắc chọn giới hạn cao, kết hợp với bộ "
      "khuếch đại, ngăn đầu ra đi vào vòng điều khiển khi đầu ra có xu hướng "
      "tăng tới mức bão hòa. Trong điều kiện đó, một tín hiệu phân cực (bias) "
      "do công tắc chọn giới hạn cao đưa ra được phép đi vào vòng. Trong "
      "hoạt động bình thường, công tắc giới hạn cao không tác động; thay vào "
      "đó công tắc giới hạn thấp hoạt động và cho phép đầu ra bình thường đi "
      "vào vòng điều khiển. Cách bố trí này rất đơn giản và khá hiệu quả.",
      "To eliminate this situation in practice, the controller is equipped "
      "with a limiter circuit that prevents the output from crossing the "
      "saturation limit. The limiter circuit consists of low and high limit "
      "selector switches combined with a high-gain amplifier. The high "
      "selector switch, in combination with the amplifier, prevents the "
      "output from entering the control loop when the output tends to "
      "increase towards windup. In that condition a bias signal, given by "
      "the high selector switch, is allowed to enter the loop. In normal "
      "operation the high limit switch is not in action; rather the lower "
      "limit switch is in operation and allows the normal output to enter "
      "the control loop. The arrangement is very simple and quite "
      "effective.")

    P(b, lang,
      "Cách hiện thực lý thuyết của hệ thống điều khiển, cùng với vị trí của "
      "mạch giới hạn, được cho trong Hình 6.18. Giá trị nạp trước ở đây được "
      "bố trí để tránh bão hòa ở giới hạn dưới của đầu ra.",
      "The theoretical implementation of the control system, together with "
      "the position of the limiter circuit, is shown in Figure 6.18. The "
      "preload provided here avoids saturation at the lower limit of the "
      "output.")

    FIG(b, 18, F.fig_f18(), lang)

    return b
