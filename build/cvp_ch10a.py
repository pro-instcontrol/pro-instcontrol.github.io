# -*- coding: utf-8 -*-
"""Book 7, Chapter 10, Section A - Valve Positioners (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), the complete
section "When to Use Valve Positioners", printed pp. 67-71 (source lines
2122-2235 of work/cvp_raw.txt). Covers the positioner as an inner valve-stem
position control loop, the six unavoidable-use cases, the remote I/P caveat,
adjustable gain/speed and the time-constant ratio, the open-loop-gain
footnote, the Figure 10-1 break-frequency example, Table 10-1, and the final
slow/fast process advice. Figure 10-1 is redrawn in cvpfig10.py.
"""
from cvp_common import fig, h2, note, p, table, ul
import cvpfig10 as F


def body_vi():
    b = []
    b.append(h2("Bộ định vị van — bộ điều khiển vị trí thân van",
                "The positioner as a valve stem position controller"))
    b.append(p("Dù bộ định vị van làm phức tạp thêm độ ổn định chung của vòng điều khiển, "
               "hầu hết các van điều khiển không thể vận hành nếu thiếu chúng. Nói rộng ra, "
               "dùng bộ định vị van — thực chất là một «bộ điều khiển vị trí thân van» "
               "(valve stem position controller) — chính là thêm một vòng điều khiển bên "
               "trong một vòng điều khiển. Ở đây, giá trị đặt (set point) là tín hiệu từ bộ "
               "điều khiển gửi tới bộ định vị; phản hồi đến từ cần đòn bẩy gắn với thân của "
               "bộ truyền động, cảm nhận vị trí của thân van; bộ điều khiển là vòi phun–cánh "
               "chắn (flapper-nozzle) hay van thí điểm (pilot valve), cảm nhận sự khác biệt "
               "giữa lực do tín hiệu điều khiển tạo ra và lực của lò xo phản hồi gắn trên "
               "đòn bẩy; còn phần tử điều khiển cuối là rơ-le gửi áp suất khí tới bộ truyền "
               "động của van. Mô tả trên nói về bộ định vị khí nén, nhưng các chức năng cơ "
               "bản của bộ định vị số cũng giống hệt, chỉ khác là lực đầu vào do tín hiệu "
               "tạo ra nay đến từ cuộn dây âm thanh (voice coil), mô-tơ mô-men (torque motor) "
               "hoặc cuộn điện từ (solenoid)."))
    b.append(p("Như mọi vòng điều khiển khác, vòng của bộ định vị có thời gian trễ thuần "
               "(dead time), hằng số thời gian (time constant) và độ lợi (gain) riêng, thường "
               "gây nhiễu tới động học của vòng điều khiển quá trình ban đầu [1]. Điều này "
               "có thể làm nhiệm vụ của bộ điều khiển quá trình trở nên khó khăn hơn khi gặp "
               "các vòng nhanh, chẳng hạn điều khiển áp suất hoặc lưu lượng."))

    b.append(h2("Những trường hợp không thể thiếu bộ định vị",
                "When a positioner is unavoidable"))
    b.append(p("Sau khi đã phác thảo xong vấn đề, giờ là lúc nói về lợi ích. Trước hết, có "
               "những trường hợp bắt buộc phải dùng bộ định vị van:"))
    b.append(ul([
        "Khi dùng bộ truyền động dạng xi lăng (cylinder actuator) cần áp suất khí vượt quá "
        "15 psi: khi đó bộ định vị vừa đóng vai trò bộ nhân áp suất, vừa là bộ điều khiển vị "
        "trí thân van.",
        "Khi chia dải tín hiệu (split-ranging) hai van: nối đầu ra của bộ điều khiển tới van "
        "thứ nhất có bộ định vị với dải tín hiệu 3–9 psi (4–12 mA). Nối cùng tín hiệu đó tới "
        "van thứ hai có bộ định vị được hiệu chỉnh ở dải 9–15 psi (12–20 mA). Cách này giúp "
        "van thứ nhất mở hoàn toàn trước khi van thứ hai tiếp quản. Thực hành tốt là cho hai "
        "dải tín hiệu chồng lấp lên nhau, chẳng hạn 3–10 psi và 8–15 psi, để việc chuyển giao "
        "chất lỏng được êm ái. Một cách phổ biến là chọn một van nhỏ cùng với một van lớn hơn "
        "để có dải lưu lượng rộng hơn. Một trường hợp khác là dùng van thứ nhất (dòng chảy "
        "đóng, flow-to-close) xử lý chất lỏng gia nhiệt cùng với van thứ hai xử lý chất lỏng "
        "làm mát (dòng chảy mở, flow-to-open) để điều khiển nhiệt độ tốt hơn.",
        "Khi các van (thường là một trong hai van) được vận hành ở chế độ tác động ngược "
        "(reverse-acting): tức là khi một van fail-closed (bộ truyền động khí mở, "
        "air-to-open) vì lý do an toàn, nó lại được vận hành theo hướng tín hiệu đóng "
        "(signal-to-close).",
        "Khi vùng chết (deadband) dự kiến của tổ hợp bộ truyền động/van vượt quá 5% dải tín "
        "hiệu (0,6 psi hoặc 0,8 mA, hay tín hiệu điện hai chiều tương đương) do ma sát quá "
        "lớn ở thân van hoặc bộ lõi (trim).",
        "Khi phải dùng rơ-le tăng áp (booster) để đạt tốc độ hành trình cao và van có thể có "
        "vùng chết quá lớn.",
        "Khi bạn muốn có khả năng chẩn đoán trực tuyến online (chỉ có ở bộ định vị thông "
        "minh — smart positioners).",
    ]))
    b.append(p("Tôi không biết thêm lý do nào khác để dùng bộ định vị van, có lẽ trừ trường "
               "hợp muốn tăng tốc độ đáp ứng khi van đặt quá xa bộ chuyển đổi dòng–áp (I/P) "
               "lắp trong phòng điều khiển. Nhưng ngay cả khi đó, một bộ chuyển đổi lắp ngay "
               "trên van hoặc rơ-le tăng áp (booster relay) sẽ làm việc tốt hơn với một van "
               "thông thường không đáp ứng tiêu chí nào nêu trên. Hãy nghĩ thêm về số tiền "
               "sẽ tiết kiệm được, không chỉ ở phần cứng mà còn ở đường ống, cụm khí (air "
               "sets) và công bảo trì."))
    b.append(p("Tuy nhiên, vì bộ định vị là cần thiết trong hầu hết trường hợp, hãy cố gắng "
               "chỉ định một phiên bản hiện đại cho phép thay đổi đặc tính vận hành của chính "
               "nó (và của van được nối với nó). Trước kia, bộ định vị van cũng giống như bộ "
               "điều khiển quá trình nhưng thiếu cả chỉnh dải tỷ lệ (proportional band) lẫn "
               "chỉnh reset. Có thể bạn may mắn và mọi thứ đều ổn định; tuy nhiên, van (hoặc "
               "toàn bộ vòng điều khiển) có thể «hunt» ở chế độ không ổn định. Ngày xưa, đi "
               "dạo qua một nhà máy lọc dầu hay nhà máy hóa chất điển hình để đếm số van điều "
               "khiển đang vận hành mà bộ định vị bị ngắt hoặc chuyển sang chế độ bypass quả "
               "là một bài học đầy tính giáo dục!"))

    b.append(h2("Tốc độ, độ lợi và tỷ lệ hằng số thời gian",
                "Speed, gain and the time-constant ratio"))
    b.append(p("Để cuộc sống của người vận hành ngày nay dễ dàng hơn, nhiều bộ định vị mới có "
               "chỉnh tốc độ và chỉnh độ lợi, hoặc kết hợp cả hai. Điều này giống như lắp lại "
               "các núm chỉnh vào vỏ bộ điều khiển. Tính năng này cho phép bạn thay đổi đặc "
               "tính đáp ứng tần số (hay hằng số thời gian) của phần tử điều khiển cuối theo "
               "quan hệ tối ưu với quá trình. Bạn có lẽ đã biết rằng một vòng điều khiển "
               "không thể ổn định nếu hằng số thời gian của quá trình bằng hoặc gần bằng "
               "hằng số thời gian của tổ hợp bộ điều khiển/van. Để có một vòng ổn định, tỷ lệ "
               "giữa hằng số thời gian của van và của hệ thống phải ít nhất là 3:1 (hoặc "
               "0,3:1), hay tốt hơn là 5:1 (hoặc 0,2:1). Lý tưởng nhất là vòng van/bộ định vị "
               "phải nhanh hơn vòng quá trình, điều này đôi khi khó đạt được."))
    b.append(p("Với tổ hợp van/bộ định vị thông thường (không số), bạn không có lựa chọn nào "
               "khác ngoài việc giảm cài đặt của bộ điều khiển (dải tỷ lệ cao — reset dài) "
               "hoặc bóp ống đầu ra từ bộ định vị tới bộ truyền động để làm van chậm lại, đặc "
               "biệt khi bộ định vị không ổn định do ma sát thân van quá lớn. Giờ đây, hy "
               "vọng là tránh được rủi ro có người vô tình nghịch các núm chỉnh ngoài hiện "
               "trường, bạn có thể thay đổi tốc độ hành trình của van (thường theo tỷ lệ 5:1) "
               "và/hoặc cài đặt độ lợi vòng hở<sup>1</sup> (độ nhạy) của bộ định vị (thường "
               "theo tỷ lệ 10:1), ngay cả khi van đang vận hành. (Một lời cảnh báo: sau khi đổi "
               "cài đặt độ lợi, bạn có thể phải chỉnh lại điểm zero đôi chút.)"))
    b.append(note("<b>Chú thích 1.</b> Định nghĩa của «độ lợi vòng hở» (open-loop gain) của bộ "
                  "định vị là sự thay đổi của tín hiệu đầu ra chia cho sự thay đổi của tín "
                  "hiệu đầu vào (khi đã ngắt phản hồi). Vì vậy, độ lợi 200:1 gây ra sự thay đổi "
                  "tín hiệu đầu ra 20 psi cho mỗi 0,1 psi thay đổi tín hiệu đầu vào. Độ lợi là "
                  "nghịch đảo của phần trăm dải tỷ lệ; do đó độ lợi 200:1 tương đương 0,5% dải "
                  "tỷ lệ. Một số bộ định vị chỉ có độ lợi thấp tới 30:1; trong khi một số khác "
                  "vượt quá 200:1. Một số bộ định vị số dùng van điện từ đẩy–kéo (push-pull "
                  "solenoid) cho quá trình chuyển đổi I/P có thể cần cài đặt độ lợi thấp hơn "
                  "để tránh hiện tượng rung rít («chattering») của các thiết bị bên trong này."))

    b.append(h2("Ví dụ Hình 10-1 và Bảng 10-1", "Figure 10-1 example and Table 10-1"))
    b.append(p("Một ví dụ điển hình về cách có thể thay đổi hằng số thời gian của van được "
               "thể hiện trong Hình 10-1. Với lưu lượng khí cực đại và cài đặt độ lợi thấp "
               "hơn, «tần số gãy» (break frequency) là 0,75 cps. Ở đầu kia của dải, lưu lượng "
               "khí chỉ 0,6 m³/h và độ lợi cao hơn bằng 67 (tương đương 1,5% dải tỷ lệ) cho "
               "tần số gãy 0,32 cps — gần như thay đổi 220% hằng số thời gian."))
    b.append(fig(1, F.fig_f101()))
    b.append(p("Hằng số thời gian của một van điều khiển được định nghĩa là thời gian (tính "
               "bằng giây) để thân van đi từ zero tới 66,7% hành trình định mức khi toàn bộ "
               "tín hiệu được áp dụng. Bảng 10-1 liệt kê các hằng số thời gian điển hình của "
               "van điều khiển có bộ định vị."))
    b.append(table(["Kích thước bộ truyền động", "Hành trình định mức", "Khí vào", "Khí xả"],
                   [["32 in²", "1/2 in", "1.1", "2.5"],
                    ["32 in²", "3/4 in", "1.8", "2.6"],
                    ["54 in²", "3/4 in", "5", "7"],
                    ["108 in²", "2 1/4 in", "10", "12"]],
                   caption="Bảng 10-1. Hằng số thời gian (tính bằng giây) (theo bản in)."))

    b.append(h2("Lời khuyên khi không nắm rõ động học quá trình",
                "Advice even without a notion of process dynamics"))
    b.append(p("Ngay cả khi bạn không có chút khái niệm nào về động học của quá trình, hãy ghi "
               "nhớ lời khuyên sau:"))
    b.append(ul([
        "Nếu bạn có một quá trình chậm như điều khiển nhiệt độ, hãy đặt độ lợi ở mức tối đa "
        "hoặc gần tối đa. Cách này giúp van đáp ứng được những thay đổi tín hiệu nhỏ hơn (nhờ "
        "tác dụng reset của bộ điều khiển). Tuy nhiên, hãy đặt tốc độ (lưu lượng khí ra) gần "
        "mức tối thiểu, nhằm tránh bộ truyền động không ổn định.",
        "Nếu bạn có một quá trình nhanh như điều khiển áp suất hoặc lưu lượng, hãy đặt độ lợi "
        "gần mức tối thiểu và tốc độ hành trình của bộ truyền động ở giá trị cực đại, tạo ra "
        "một van đáp ứng nhanh nhưng vẫn ổn định.",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Bộ định vị van — bộ điều khiển vị trí thân van",
                "The positioner as a valve stem position controller"))
    b.append(p("Although positioners complicate overall loop stability, most control valves "
               "cannot operate without them. Broadly speaking, the use of a valve positioner, "
               "which really is a “valve stem position controller,” adds another control loop "
               "within a control loop. Here the set point is the controller signal to the "
               "positioner; the feedback comes from the lever attached to the actuator stem "
               "sensing the latter's position; the controller is the flapper-nozzle, or pilot "
               "valve, sensing the difference between the force created by the controller "
               "signal and that of a feedback spring attached to the lever; and the final "
               "control element is the relay that sends air pressure to the valve actuator. "
               "While the latter description refers to pneumatic positioners, the basic "
               "functions are identical for digital positioners, except that here the "
               "signal-created input force comes from a voice coil, a torque motor, or a "
               "solenoid."))
    b.append(p("Like any other loop, the positioner loop has its own dead time, time constant, "
               "and gain, which often interfere with the original process control loop "
               "dynamics [1]. This can make the task of the process controller more difficult "
               "when fast loops, such as those for pressure or flow control, are encountered."))

    b.append(h2("Những trường hợp không thể thiếu bộ định vị",
                "When a positioner is unavoidable"))
    b.append(p("So much for outlining the problem; now to the benefits. First, there are "
               "instances in which the use of a valve positioner is unavoidable:"))
    b.append(ul([
        "When a cylinder actuator that requires air pressure in excess of 15 psi is used. "
        "Here, the positioner is used both as a pressure multiplier and a stem position "
        "controller.",
        "When split-ranging two valves: connect the controller output to the first valve "
        "that has a positioner with a signal range of 3–9 psi (4–12 mA). Connect the same "
        "signal to a second valve that has a positioner calibration of 9–15 psi (12–20 mA). "
        "This way, the first valve will be fully open when the second valve takes over. Good "
        "practice is to have the two positioner signals overlap, such as 3–10 psi and 8–15 "
        "psi, to get a smooth transfer of fluid. A common practice is to select a small valve "
        "size together with a larger one to get a wider flow range. Another case is to use a "
        "first valve (flow-to-close) handling heating fluid together with a second valve "
        "handling cooling fluid (flow-to-open) for better temperature control.",
        "When valves (usually one of two) are operated in a reverse-acting mode. That is, "
        "when a valve fails closed (air-to-open actuator) for safety reasons, it shall be "
        "operated in the signal-to-close direction.",
        "When the expected deadband of the actuator/valve combination exceeds 5% of the "
        "signal span (0.6 psi or 0.8 mA, or an equivalent bidirectional electronic signal) "
        "because of excessive stem or trim friction.",
        "When a booster has to be used for high travel speed and the valve may have excessive "
        "deadband.",
        "When you want to have diagnostic capabilities online (smart positioners only).",
    ]))
    b.append(p("I am not aware of any other reasons a valve positioner should be used, except "
               "perhaps to increase the speed of response in case a valve is located too far "
               "away from an I/P transducer installed in the control room. But even there, a "
               "valve-mounted transducer or booster relay will perform better with an "
               "ordinary valve not meeting any of the criteria outlined earlier. Think also "
               "of how much money will be saved, not only in hardware but also in piping, air "
               "sets, and maintenance."))
    b.append(p("However, because a positioner is required in most cases, try to specify a "
               "modern version that offers the ability to vary its (and the connected "
               "valve's) operating characteristic. Formerly, valve positioners were like "
               "process controllers without proportional band and reset adjustments. One may "
               "get lucky, and everything will be stable; however, the valve (or the complete "
               "control loop) might “hunt” in an unstable mode. It used to be educational to "
               "walk through a typical refinery or chemical plant and count all the control "
               "valves in operation with the valve positioner disconnected or in the bypass "
               "mode!"))

    b.append(h2("Tốc độ, độ lợi và tỷ lệ hằng số thời gian",
                "Speed, gain and the time-constant ratio"))
    b.append(p("To make life easier for today's process operators, many new positioners offer "
               "speed and gain adjustments or a combination of the two. This is like adding "
               "the adjusting knobs back onto the controller housing. This feature enables "
               "you to change the frequency response characteristic (or time constant) of the "
               "final control element in optimum relation to that of the process. You "
               "probably know that a loop cannot be stable if the process time constant is "
               "equal to or close to that of the controller/valve combination. To have a "
               "stable loop, the ratio between the valve and the system time constants should "
               "be at least 3:1 (or 0.3:1) or, better yet, 5:1 (or 0.2:1). Ideally, the "
               "valve/positioner loop should be faster than the process loop, which is "
               "sometimes hard to accomplish."))
    b.append(p("With a conventional (and nondigital) valve/positioner combination, you had no "
               "choice but to either reduce the controller settings (high proportional "
               "band—long reset action) or crimp the output tubing from the positioner to the "
               "actuator to slow the valve down, particularly when the positioner was unstable "
               "due to excessive valve stem friction. Now, hopefully avoiding the pitfalls of "
               "having somebody ignorantly playing with the adjustments in the field, you can "
               "change the speed of the valve travel (typically by 5:1) and/or the open-loop "
               "gain<sup>1</sup> setting (sensitivity) of the positioner (typically by 10:1) "
               "even while the valve is in operation. (A word of caution: You may have to "
               "realign the zero adjustment somewhat after changing the gain setting.)"))
    b.append(note("<b>Footnote 1.</b> The definition of the “open-loop gain” of a positioner is "
                  "the change in the output signal over the change in the input signal (when "
                  "the feedback is disconnected). Thus, a gain of 200:1 causes a 20 psi output "
                  "signal change per 0.1 psi input signal change. Gain is the reciprocal of "
                  "percent band; therefore, a gain of 200:1 is equivalent to 0.5% proportional "
                  "band. Some positioners have gains only as low as 30:1; however, some exceed "
                  "200:1. Some digital positioners that employ push-pull solenoid valves for "
                  "I/P conversion may need a lower gain setting to avoid “chattering” of these "
                  "internal devices."))

    b.append(h2("Ví dụ Hình 10-1 và Bảng 10-1", "Figure 10-1 example and Table 10-1"))
    b.append(p("A typical example of how the time constant of the valve can be varied is shown "
               "in Figure 10-1. With maximum airflow and a lower gain setting, the “break "
               "frequency” is 0.75 cps. At the other extreme, an airflow of only 0.6 m³/h and "
               "a higher gain of 67 (equivalent to 1.5% proportional band) produces a break "
               "frequency of 0.32 cps—almost a 220% change in the time constant."))
    b.append(fig(1, F.fig_f101()))
    b.append(p("The time constant of a control valve is defined as the time in seconds that it "
               "takes to travel from zero to 66.7% of rated travel when the full signal is "
               "applied. Table 10-1 shows a tabulation of typical time constants for control "
               "valves with positioners."))
    b.append(table(["Actuator Size", "Rated Travel", "Air In", "Air Exhaust"],
                   [["32 in²", "1/2 in", "1.1", "2.5"],
                    ["32 in²", "3/4 in", "1.8", "2.6"],
                    ["54 in²", "3/4 in", "5", "7"],
                    ["108 in²", "2 1/4 in", "10", "12"]],
                   caption="Table 10-1. Time constant(s) in seconds (as printed)."))

    b.append(h2("Lời khuyên khi không nắm rõ động học quá trình",
                "Advice even without a notion of process dynamics"))
    b.append(p("Even if you do not have the faintest notion about your process dynamics, keep "
               "the following advice in mind:"))
    b.append(ul([
        "If you have a slow process such as temperature control, set the gain at or near "
        "maximum. This way, the valve will respond to the smaller incremental signal change "
        "(due to the reset action of the controller). However, set the speed (air output) near "
        "minimum, thus avoiding an unstable actuator.",
        "If you have a fast process such as pressure or flow control, set the gain near minimum "
        "and the actuator travel speed at its maximum value, thus creating a highly responsive "
        "but stable valve.",
    ]))
    return "".join(b)
