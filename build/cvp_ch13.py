# -*- coding: utf-8 -*-
"""Book 7, Chapter 13 - How Good Is the Valve I Purchased? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
95-98 (PDF pp. 98-101). Two vector figures (closed-loop differentiation and
static open-loop step response), one long footnote on installed gain,
two references and three additional-reading items.
"""
from cvp_common import fig, h2, h3, note, p, refs, ul
import cvpfig13 as F

PAGES_SRC = 4
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "How Good Is the Valve I Purchased?"
TITLE_VI = "Van mình mua tốt đến đâu?"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 13.</b> hiệu năng van trong vòng điều khiển (valve "
                "performance in a control loop) · yêu cầu về mặt bích và áp lực (flange "
                "and pressure vessel code) · khả năng lưu lượng (flow capacity) · đặc "
                "tính lưu lượng (flow characteristic) · tuyến tính (linearity) · độ nhạy "
                "ngưỡng (threshold sensitivity) · vùng chết (deadband) · độ trễ (hysteresis) "
                "· đặc tính lưu lượng lắp đặt (installed flow characteristic) · thời gian "
                "trễ (dead time) do thể tích khí trong bộ truyền động · ma sát thân van (stem "
                "friction) · hằng số thời gian van (valve time constant) · vòng lưu lượng "
                "thử nghiệm (flow loop) · thử phân biệt hiệu năng (performance "
                "differentiation) · độ biến thiên (variability) · hệ số khuếch đại bộ "
                "điều khiển Kc · chỉnh nhanh/chậm (faster/slower tuning) · thử tĩnh vòng "
                "hở (static/open-loop test) · bước tín hiệu (step input) · hành trình "
                "thân van (valve travel) · lưu lượng (flow rate) · chuyển động mất / khe "
                "hở (lost motion / play) · bộ định vị (positioner) · hệ số khuếch đại "
                "lắp đặt (installed gain) · độ dốc đặc tính lưu lượng lắp đặt · quy tắc "
                "80% · dải lưu lượng có thể điều khiển (controllable flow range) · khả "
                "năng điều chỉnh lắp đặt (installed rangeability) · van quay (rotary "
                "valve) · van cầu (globe valve) · độ bền chắc (rugged, heavy-duty) · "
                "đế van / bệ van / mặt tựa của van (seat).")
    return ("<b>Key terms.</b> valve performance in a control loop · flange and pressure "
            "vessel code · flow capacity · flow characteristic · linearity · threshold "
            "sensitivity · deadband · hysteresis · installed flow characteristic · dead "
            "time from actuator air volume · stem friction · valve time constant · test "
            "flow loop · performance differentiation · variability · controller gain Kc · "
            "faster/slower tuning · static (open-loop) test · step input · valve travel · "
            "flow rate · lost motion / play · positioner · installed gain · installed "
            "flow-characteristic slope · 80% rule · controllable flow range · installed "
            "rangeability · rotary valve · globe valve · rugged heavy-duty construction · "
            "seat.")


def body_vi():
    b = []
    b.append(h2("Hiệu năng trong vòng điều khiển",
                "Performance in the control loop"))
    b.append(p("Đây là một câu hỏi hoàn toàn chính đáng của người mua và người sử dụng "
               "van điều khiển. Ngoài việc đáp ứng các yêu cầu hiển nhiên — như quy chuẩn "
               "về mặt bích và bình áp lực, và có đúng khả năng lưu lượng cùng đặc tính "
               "lưu lượng — còn có một câu hỏi quan trọng khác: van sẽ hoạt động thế nào "
               "trong vòng điều khiển của tôi?"))
    b.append(p("Các người dùng lớn đã xây dựng tiêu chuẩn nội bộ để cố gắng trả lời câu "
               "hỏi này. Hầu hết các tiêu chuẩn đó nêu các tiêu chí hiệu năng tối thiểu "
               "như tuyến tính, độ nhạy ngưỡng (thường là 0,2% dải với bộ định vị), vùng "
               "chết (tối đa 0,5% dải khi có bộ định vị và 5% khi không có), và độ trễ "
               "(hysteresis)."))
    b.append(p("Tuy nhiên, ngay cả khi một van đáp ứng tất cả các tiêu chí này, van từ "
               "hai nhà sản xuất khác nhau vẫn không thể kỳ vọng sẽ hành xử giống nhau "
               "khi lắp vào cùng một vòng điều khiển. Lý do là sự tương tác giữa đặc "
               "tính lưu lượng lắp đặt, thời gian trễ (do thể tích khí trong bộ truyền "
               "động hoặc ma sát thân van gây ra) và hằng số thời gian của van."))

    b.append(h2("Thử phân biệt hiệu năng vòng kín",
                "Closed-loop performance differentiation"))
    b.append(p("Để trả lời câu hỏi về “hành vi vòng điều khiển” một cách thực tế hơn, "
               "một số nhà sản xuất van điều khiển đã nghĩ ra ý định thử van trong một "
               "vòng lưu lượng thực [1], thường là điều khiển tốc độ dòng chảy (dùng "
               "nước bơm). Một vòng như vậy chạy rất nhanh và đặt yêu cầu cao lên van "
               "và hệ thống định vị của nó. Tiêu chí hiệu năng là mức độ lệch của biến "
               "được điều khiển khỏi điểm đặt của bộ điều khiển trong các điều kiện "
               "lưu lượng (tải) khác nhau, với thời gian trễ của vòng và cài đặt hệ số "
               "khuếch đại bộ điều khiển (dải tỷ lệ) được thay đổi. Độ lệch giữa giá trị "
               "thực và điểm đặt, đã chuẩn hóa và lấy trung bình — đôi khi gọi là độ "
               "biến thiên (variability) — sau đó được vẽ theo hằng số thời gian vòng "
               "kín ở một tải hoặc một vị trí hành trình van đã cho (xem Hình 13-1)."))
    b.append(fig(1, F.fig_f131()))
    b.append(p("Một phép thử liên quan đến nhiều van khác nhau có thể được gọi là thử "
               "phân biệt hiệu năng (performance differentiation) và có thể được bổ "
               "sung bằng một phép thử tĩnh (điều khiển vòng hở, bộ điều khiển ở chế độ "
               "thủ công). Hành trình của van và/hoặc sự thay đổi lưu lượng được quan "
               "sát và ghi lại sau một bước thay đổi tín hiệu điều khiển (bước thay đổi "
               "tối thiểu = 0,5%); xem Hình 13-2."))
    b.append(fig(2, F.fig_f132()))
    b.append(p("Như rõ từ Hình 13-1, các loại van khác nhau, hoặc van từ các nhà sản "
               "xuất khác nhau, hành xử rất khác nhau dù mỗi van đều đáp ứng các tiêu "
               "chí mà khách hàng yêu cầu trong phiếu đặt hàng. Đồ thị cho thấy tất cả "
               "các loại van đều hoạt động tốt khi hằng số thời gian vòng rất dài, chẳng "
               "hạn trong hệ thống điều khiển nhiệt độ chậm, nhưng bắt đầu lệch rõ khi "
               "tốc độ tăng lên (thời gian trễ ngắn hơn, như trong vòng điều khiển áp "
               "suất hoặc lưu lượng). Ví dụ, van A có độ biến thiên 2,4% ở hằng số thời "
               "gian một giây, so với van C cho điều khiển chặt chẽ hơn nhiều với độ "
               "biến thiên chỉ 1,4%. Van B nằm ở giữa. Bạn không thể đoán trước sự khác "
               "biệt ấy chỉ bằng cách nhìn dữ liệu trong catalog của từng van."))

    b.append(h2("Đọc tín hiệu tĩnh: lưu lượng mới là thước đo",
                "Reading the static test: flow is the measure"))
    b.append(p("Dữ liệu thử tĩnh trong Hình 13-2 cho thấy một tổ hợp van/bộ định vị kém "
               "đôi khi thậm chí không phản ứng với một bước thay đổi tín hiệu 1% (trường "
               "hợp trước có thể là dấu hiệu của ma sát thân van quá lớn). Các ảnh hưởng "
               "động gây thay đổi lực thân van, do mất ổn định động ở một số vị trí hành "
               "trình nhất định, cũng biểu hiện ra và có thể được chẩn đoán."))
    b.append(p("Để có điều khiển tốt, chúng ta thường kỳ vọng một cụm van điều khiển có "
               "thể phản ứng với những thay đổi của biến quá trình từ 1% trở xuống. Lưu "
               "ý ở Hình 13-2 rằng van này có thể tạo chính xác một thay đổi hành trình "
               "cho dù tín hiệu vào chỉ đổi 0,5%. Tuy nhiên, không có sự thay đổi lưu "
               "lượng nào được quan sát cho đến khi tín hiệu đổi tới 1%. Đây là dấu "
               "hiệu của một liên kết lỏng giữa bộ truyền động và phần tử đóng. Điều "
               "này có thể xảy ra ở một số van quay, nơi có khe hở trong kết nối giữa "
               "thân bộ truyền động và thân van."))
    b.append(p("Khi tiến hành các phép thử kiểu này, điều quan trọng là so sánh sự thay "
               "đổi lưu lượng theo tín hiệu đầu vào thay vì chỉ so sánh hành trình thân "
               "van với tín hiệu. Một sự thay đổi vị trí thân van không có tác dụng gì "
               "trong việc hiệu chỉnh biến quá trình nếu không có sự thay đổi lưu lượng "
               "tương ứng."))
    b.append(p("Cuối cùng, một hệ thống thử như vậy có thể đo hệ số khuếch đại lắp đặt<sup>1</sup> "
               "(độ dốc của đặc tính lưu lượng lắp đặt) và tốc độ dòng chảy nhỏ nhất "
               "lớn nhất (ví dụ, tính bằng gallông/phút) mà một van cho phép điều khiển "
               "trong vòng thử. Trong khi hệ số khuếch đại của quá trình thường bằng 1 "
               "với cài đặt bộ phát đúng cách, hệ số khuếch đại lắp đặt của van thường "
               "cao hơn. Hệ số khuếch đại trung bình của van (thường nằm giữa 1,2 và 2,5) "
               "không được lệch với tỷ lệ lớn hơn 2:1. Ví dụ, nếu hệ số khuếch đại lắp "
               "đặt trung bình của van là 1,5, ở 8% lưu lượng định mức hệ số là 3 và "
               "tăng lên 3,2 ở 7% lưu lượng, trong khi ở 90% lưu lượng định mức hệ số "
               "đo được chỉ là 0,75 (3 là giới hạn trên và 0,75 là giới hạn dưới của hệ "
               "số khuếch đại), khi đó ta có thể nói “dải lưu lượng có thể điều khiển” "
               "là 90% / 8% = 11,25:1. Đó là một cách tốt để định nghĩa “khả năng điều "
               "chỉnh lắp đặt” (installed rangeability)."))
    b.append(note("<b>Chú thích 1.</b> Hệ số khuếch đại lắp đặt của van điều khiển được "
                  "định nghĩa là tỷ lệ thay đổi lưu lượng trên thay đổi tín hiệu điều "
                  "khiển. Ví dụ, van có lưu lượng thay đổi 10% lưu lượng cực đại khi "
                  "tín hiệu thay đổi 5% thì hệ số khuếch đại lắp đặt bằng 2. Nhiều người "
                  "lầm tưởng hệ số khuếch đại lắp đặt phải bằng 1, tức 10% thay đổi "
                  "lưu lượng cho 10% thay đổi tín hiệu. Điều đó không thể đúng, vì nó "
                  "sẽ đòi hỏi hành trình van 100% ở lưu lượng định mức. (Điều này vi "
                  "phạm quy tắc 80%; xem tiểu mục «Chọn cỡ van nào» trong Chương 5.) Dù "
                  "hệ số khuếch đại là bao nhiêu, hệ số tỷ lệ/khuếch đại của bộ điều "
                  "khiển có thể dễ dàng chỉnh để khớp với hệ số của van, miễn là hệ số "
                  "của van tương đối không đổi trong dải lưu lượng áp dụng."))
    b.append(p("Có lẽ không ngạc nhiên khi phép thử “phân biệt” này [2] chứng minh rằng "
               "các van điều khiển quay được thiết kế tốt (giả sử không có «độ rơ» giữa "
               "thân van với bộ truyền động hoặc với phần tử đóng) hoạt động cũng tốt "
               "như các van cầu tốt; và, trái với trực giác, một van cầu chắc chắn, hạng "
               "nặng không nhất thiết vượt trội một van nhỏ hơn, nhẹ hơn được thiết kế "
               "tốt khi nói đến việc đáp ứng các điều kiện vòng điều khiển đa dạng. "
               "Điều này không có nghĩa là van nhỏ có thể chịu được ứng dụng chênh áp "
               "cao. Xét cho cùng, hành vi vòng điều khiển chỉ là một phần của quá trình "
               "đánh giá van."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "C. Taylor and B. Davey, “Control Valve Performance Requirements for Optimum "
        "Process Control,” Proceedings of the 34th Annual International Pulp &amp; Paper "
        "Symposium, 1994 (Research Triangle, NC: ISA [International Society of "
        "Automation]): 5-1 to 5-7.",
        "ISA-75.25.01-2000 (R2010), Test Procedure for Control Valve Response Measurement "
        "from Step Inputs (Research Triangle, NC: ISA [International Society of "
        "Automation]).",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "ANSI/ISA-75.13.01-2013, Method of Evaluating the Performance of Positioners with "
        "Analog Input Signals and Pneumatic Output (Research Triangle Park, NC: ISA "
        "[Instrument Society of Automation]).",
        "ANSI/ISA-TR75.25.02-2000 (R2010), Control Valve Response Measurement from Step "
        "Inputs (Research Triangle Park, NC: ISA [Instrument Society of Automation]).",
        "R. Ali, “Smart Positioners to the Rescue,” InTech (June 2002): 72–73.",
    ]))
    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có các dấu gạch nối khi "
                  "xuống dòng («manu-facturers», «man-ufacturers», «differ-»); bản dịch "
                  "ghép lại thành từ hoàn chỉnh. (2) Chữ số trong ví dụ hệ số khuếch đại "
                  "được giữ nguyên theo bản in, kể cả cặp «8% lưu lượng định mức» và «7% "
                  "lưu lượng» trong cùng một ví dụ. (3) Các giá trị độ biến thiên 2,4% và "
                  "1,4% ở τ = 1 giây được giữ nguyên theo văn bản in, dù đường cong trên "
                  "Hình 13-1 khi đọc bằng mắt cho giá trị gần đúng tương ứng; hai hình "
                  "được vẽ lại dạng vector đã đơn giản hóa, giữ cấu trúc và nhãn của bản "
                  "gốc. (4) Hình 13-1 và 13-2 có ghi nguồn «Courtesy of Emerson Process "
                  "Control» trong bản in; bản dịch giữ ghi nhận này trong chú thích hình."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 13 chiếm các trang in 95–98 của ấn bản in (PDF tr. 98–101). "
               "Nguyên bản gồm phần mở đầu, thuyết minh thử vòng kín và thử tĩnh, một "
               "chú thích dài về hệ số khuếch đại lắp đặt, hai tài liệu tham khảo và ba "
               "mục đọc thêm — tất cả đều được giữ lại. Các tiêu đề phụ trong bản dịch "
               "được biên tập thêm vì nguyên bản không có tiểu mục được đánh số."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Hiệu năng trong vòng điều khiển",
                "Performance in the control loop"))
    b.append(p("This is a legitimate question for buyers and users of control valves. "
               "Aside from being able to meet the obvious requirements, such as the "
               "flange and pressure vessel code requirements and having the right flow "
               "capacity and characteristic, there is another important question: How "
               "will it perform in my control loop?"))
    b.append(p("Major users have developed internal standards that attempt to address "
               "this question. Most of these standards state certain minimum "
               "performance criteria, such as linearity, threshold sensitivity (usually "
               "0.2% of span with positioner), deadband (maximum 0.5% of span with "
               "positioner and 5% without), and hysteresis."))
    b.append(p("However, even if a valve meets all these criteria, valves from two "
               "different manufacturers cannot be expected to act the same when "
               "installed in a given control loop. The reason is the interaction of the "
               "installed flow characteristic, dead time (caused by air volume in the "
               "actuator or stem friction), and the valve time constant."))

    b.append(h2("Closed-loop performance differentiation",
                "Closed-loop performance differentiation"))
    b.append(p("To address the question of “loop behavior” more realistically, some "
               "control valve manufacturers have come up with the idea of testing a "
               "valve in an actual flow loop [1], typically controlling the rate of flow "
               "(using pumped water). Such a control loop is very fast and poses high "
               "demands on a valve and its positioning system. The performance criteria "
               "are the amount of deviation of the controlled variable from the "
               "controller set point under various flow (load) conditions and varying "
               "the loop's time constant and controller gain (proportional band) "
               "settings. The normalized, averaged deviation of the actual versus "
               "set-point error, sometimes called variability, is then plotted against "
               "the closed-loop time constant at a given load or valve travel setting "
               "(see Figure 13-1)."))
    b.append(fig(1, F.fig_f131()))
    b.append(p("Such a test involving several different valves may be called "
               "performance differentiation and can be supplemented by a static test "
               "(open-loop control, controller on manual). The travel of the valve "
               "and/or the change in flow is observed and recorded following a step "
               "change in the controller signal (minimum change = 0.5%); see Figure "
               "13-2."))
    b.append(fig(2, F.fig_f132()))
    b.append(p("As is evident from Figure 13-1, different valve types, or valves from "
               "different manufacturers, behave quite dissimilarly even though each of "
               "them meets the customer's requested valve requisition criteria. The "
               "graph indicates that all valve types perform well when the loop time "
               "constant is very long, such as in a slow temperature control system, but "
               "they start to deviate markedly with increasing speed (shorter time "
               "constant, such as is found in a pressure or flow control loop). For "
               "example, valve A exhibits a variability of 2.4% for a time constant of "
               "one second, compared to valve C, which gives much tighter control, with "
               "a variability of only 1.4%. Valve B falls in between. You could not "
               "foresee such a difference just by looking at the catalog data for each "
               "valve."))

    b.append(h2("Reading the static test: flow is the measure",
                "Reading the static test: flow is the measure"))
    b.append(p("The static test data represented by Figure 13-2 reveals that a poor "
               "valve/positioner combination sometimes will not even respond to a 1% "
               "change in signal (the previous one could be an indication of too much "
               "stem friction). Dynamic influences causing changes of valve stem forces, "
               "due to dynamic instability at certain travel positions, also show up and "
               "can be diagnosed."))
    b.append(p("To achieve good control, we would normally expect a control valve "
               "assembly to be able to respond to process variable changes of 1% or "
               "less. Note in Figure 13-2 that this valve is capable of accurately "
               "producing a travel change for as little as a 0.5% change in input "
               "signal. However, there is no observable flow change until the signal "
               "exchange reaches 1%. This is an indication of a loose connection between "
               "the actuator and the closure member. This could happen with some rotary "
               "valves where there is clearance in the connection between the actuator "
               "stem and the valve stem."))
    b.append(p("When conducting these kinds of tests, it is important to compare the "
               "flow change in relation to the input signal rather than comparing the "
               "stem travel to the input. A stem position change does nothing to correct "
               "the process variable unless a corresponding flow change occurs."))
    b.append(p("Finally, such a test system can measure the installed gain<sup>1</sup> "
               "(installed flow characteristic slope) of a valve and the minimum and "
               "maximum rate of flow (e.g., in gallons per minute) that can be "
               "controlled by a given valve in the test loop. Whereas the process gain "
               "is typically 1 with the proper transmitter settings, the installed gain "
               "of the valve is usually higher. The average gain of the valve (typically "
               "between 1.2 to 2.5) should not deviate by a ratio of more than 2:1. For "
               "example, if the average installed gain of the valve is 1.5, at 8% of "
               "rated flow the gain is 3 going to 3.2 at 7% flow, and at 90% of the "
               "rated flow the measured gain is only 0.75 (3 being the upper limit and "
               "0.75 the lower limit of the gain), then we could say that the "
               "“controllable flow range” is 90% / 8% = 11.25:1. This would be a good "
               "way to define “installed rangeability.”"))
    b.append(note("<b>Footnote 1.</b> Installed control valve gain is defined as the "
                  "ratio of flow change per controller signal change. For example, a "
                  "valve with a flow change of 10% of maximum flow for a signal change "
                  "of 5% has an installed gain of 2. Many people mistakenly believe "
                  "that the installed gain must be 1, that is, 10% flow change per 10% "
                  "signal change. This cannot be true because it would require 100% "
                  "valve travel at rated flow. (This violates the 80% rule; see the "
                  "Chapter 5 subsection, “What Size Valve to Choose.”) In any case, "
                  "whatever the gain is, the proportional or gain of the controller can "
                  "easily be adjusted to match the gain of the valve as long as the "
                  "latter is relatively constant throughout the applicable flow rates."))
    b.append(p("Perhaps not surprisingly, this “differentiation testing” [2] proved "
               "that well-designed rotary control valves (assuming no “play” between "
               "the stem and actuator, or the closure member) perform equally as well as "
               "good globe valves, and, contrary to our instincts, a rugged, heavy-duty "
               "globe valve does not necessarily outperform a well-designed smaller and "
               "lighter-duty valve when it comes to meeting diverse loop conditions. "
               "This does not mean that the small valve can handle high-pressure drop "
               "applications, for example. Loop behavior, after all, is only one part of "
               "the valve evaluation process."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "C. Taylor and B. Davey, “Control Valve Performance Requirements for Optimum "
        "Process Control,” Proceedings of the 34th Annual International Pulp &amp; Paper "
        "Symposium, 1994 (Research Triangle, NC: ISA [International Society of "
        "Automation]): 5-1 to 5-7.",
        "ISA-75.25.01-2000 (R2010), Test Procedure for Control Valve Response Measurement "
        "from Step Inputs (Research Triangle, NC: ISA [International Society of "
        "Automation]).",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "ANSI/ISA-75.13.01-2013, Method of Evaluating the Performance of Positioners with "
        "Analog Input Signals and Pneumatic Output (Research Triangle Park, NC: ISA "
        "[Instrument Society of Automation]).",
        "ANSI/ISA-TR75.25.02-2000 (R2010), Control Valve Response Measurement from Step "
        "Inputs (Research Triangle Park, NC: ISA [Instrument Society of Automation]).",
        "R. Ali, “Smart Positioners to the Rescue,” InTech (June 2002): 72–73.",
    ]))
    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains line-break "
                  "hyphenations («manu-facturers», «man-ufacturers»); the translation "
                  "rejoins them into whole words. (2) The numbers in the installed-gain "
                  "example are retained as printed, including the pair «8% of rated "
                  "flow» and «7% flow» within the same example. (3) The variability "
                  "figures of 2.4% and 1.4% at τ = 1 second are retained as printed even "
                  "though a visual reading of Figure 13-1 gives approximately similar "
                  "values; both figures are simplified vector redrawings that keep the "
                  "topology and labels of the originals. (4) Figures 13-1 and 13-2 carry "
                  "a «Courtesy of Emerson Process Control» credit in the source; the "
                  "credit is kept in the figure captions."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 13 occupies printed pp. 95-98 of the book (PDF pp. 98-101). The "
               "source consists of an opening passage, accounts of closed-loop and "
               "static testing, a long footnote on installed gain, two references and "
               "three additional-reading items, all of which are retained. The "
               "editorial subheadings in the translation were added because the source "
               "has no numbered subsections."))
    return "".join(b)
