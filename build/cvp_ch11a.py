# -*- coding: utf-8 -*-
"""Book 7, Chapter 11, Section A - Line Pressure-Produced Valve Stem Forces
(EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), the chapter
introduction plus the section "The Valve Does Not Close Properly", printed
pp. 81-85 (PDF pp. 85-89), source lines 2506-2610 of work/cvp_raw.txt.
Covers the P1/shutoff-pressure specification requirement, the two closure
mechanisms, the hot-oil worked example, piston and spring-diaphragm actuator
sizing, the positioner output span fallacy, and the three remedies. Figure
11-1 is redrawn in cvpfig11.py.
"""
from cvp_common import eq, fig, h2, note, ol, p
import cvpfig11 as F


def body_vi():
    b = []
    b.append(h2("Bí ẩn lực thân van do áp suất đường ống, hay Chọn đúng kích cỡ "
                "bộ truyền động",
                "The mystery of line pressure-produced valve stem forces, or "
                "selecting the correct actuator size"))
    b.append(p("Việc chọn bộ truyền động (actuator) phù hợp cho van thường được để "
               "lại cho nhà cung cấp. Hầu hết thời gian cách này làm việc tốt, đặc "
               "biệt khi điều kiện áp suất mà van phải xử lý thấp hoặc kích cỡ van "
               "nhỏ. Tuy nhiên, sẽ rất có ích nếu bạn biết một số hậu quả của việc "
               "chọn sai (thường là quá nhỏ) kích cỡ bộ truyền động. Hãy nhớ rằng "
               "nhà cung cấp van trúng thầu có lẽ là người chào giá thấp nhất và, "
               "thường thì, chính là người đã cắt giảm kích cỡ bộ truyền động để hạ "
               "chi phí. Sau đây là mô tả về những gì có thể xảy ra sau khi lắp đặt."))

    b.append(h2("Van không đóng kín đúng cách", "The valve does not close properly"))
    b.append(p("Việc loại bỏ các đường bypass quanh van điều khiển vì lý do kinh tế "
               "đã dẫn đến yêu cầu van điều khiển phải có độ kín đế van (seat "
               "tightness) ANSI/FCI Class IV (để kiêm nhiệm vai trò van ngắt khi hệ "
               "thống ngừng hoạt động). Cách này làm việc tốt miễn là cài đặt lò xo "
               "ban đầu, áp suất khí và kích cỡ bộ truyền động đủ để khắc phục áp "
               "suất chất lỏng tác dụng lên nút van (giả sử là van cầu một đế, "
               "single-seated globe valve)."))
    b.append(p("Trước hết, điều quan trọng là phải báo cho nhà cung cấp biết áp "
               "suất vào lớn nhất là bao nhiêu! Thường thì đây là chênh áp qua nút "
               "van khi van đóng chặt, chứ không phải áp suất vào thấp hơn và áp "
               "suất ra cao hơn đáng kể mà van thấy trong quá trình tiết lưu bình "
               "thường, cũng không phải giá trị dùng để tính Cv của van. Một nhà "
               "cung cấp van có trách nhiệm sẽ luôn giả định van phải đóng chặt "
               "chống lại áp suất vào lớn nhất với áp suất ra bằng không (zero-"
               "gauge). Do đó, P1 phải được ghi rõ trên phiếu đặc tả (xem Hình "
               "11-1). Có hai mục đích của việc đóng van: một là ngăn dòng chảy, "
               "hai là ngăn rò rỉ [1]."))
    b.append(fig(1, F.fig_f111()))

    b.append(p("Cũng có hai cơ chế đóng van. Loại đẩy (push type), chẳng hạn nút "
               "van, đóng vào một lỗ tiết lưu (orifice). Để ngăn rò rỉ, cần một lực "
               "bổ sung vượt trên lực cần để khắc phục sự mất cân bằng (off-balance). "
               "Lực bổ sung này để đạt độ kín Class IV phải ít nhất bằng 2,5 lần "
               "diện tích mặt tựa tiếp xúc nhân với P1. Ví dụ, một lỗ tiết lưu 2 in "
               "có diện tích tiếp xúc vát cạnh là 2 in × 3,14 × 0,063 in = 0,4 in². "
               "Vì vậy, khi P1 là 100 psi, cần 100 psi × 0,4 in² × 2,5 = 100 lb lực "
               "tựa bổ sung."))
    b.append(eq("2 in × 3,14 × 0,063 in = 0,4 in²", ""))
    b.append(eq("100 psi × 0,4 in² × 2,5 = 100 lb", ""))
    b.append(p("Đối với Class V, có thể cần một lực nén bằng giới hạn chảy (yield "
               "point) của vùng tiếp xúc."))
    b.append(p("Hình thức đóng thứ hai là tiếp xúc trượt (sliding contact). Điều "
               "này điển hình cho van bướm lót (lined butterfly valves) và van bi "
               "phân đoạn (segmented ball valves), trong đó phần tử đóng phải "
               "trượt vào và biến dạng một phần lớp làm kín. Dù tiếp xúc ban đầu "
               "với vòng làm kín có thể ngăn dòng chảy, nó chưa đủ để ngăn rò rỉ. "
               "Cần thêm 5° hành trình của bộ truyền động để đưa phần tử đóng từ "
               "ngăn dòng chảy sang ngăn rò rỉ. Điều này phải được tính đến trong "
               "quá trình hiệu chuẩn bộ định vị và bộ truyền động ban đầu."))

    b.append(p("Ví dụ, một van gia nhiệt với lỗ tiết lưu 2 in xử lý dầu nóng sẽ "
               "thấy, ở lưu lượng bình thường và hành trình 75%, áp suất vào 125 "
               "psig và áp suất phía sau 110 psig. Lực tác dụng lên thân van (stem "
               "force) mà bộ truyền động cảm nhận trong những điều kiện này là "
               "(2²π/4) × (125 − 110) = 47 lb.<sup>1</sup>"))
    b.append(eq("(2²π/4) × (125 − 110) = 47 lb", ""))
    b.append(note("<b>Chú thích 1.</b> Bỏ qua diện tích của thân van để đơn giản hóa."))
    b.append(p("Tuy nhiên, nếu được lệnh đóng, áp suất vào sẽ tăng lên 140 psig do "
               "đặc tính của bơm, trong khi áp suất phía sau có thể bằng không. Trong "
               "trường hợp này, lực thân van tối thiểu sẽ là 140 psi nhân với diện "
               "tích mặt tựa của nút van (dùng đường kính mặt tựa ít nhất bằng đường "
               "kính lỗ tiết lưu cộng thêm 1/16 in) cộng với ma sát packing."))
    b.append(eq("(2,063²π/4) × 140 = 468 lb;   lực thân van (đóng) = 468 lb + ma "
                "sát packing", ""))
    b.append(p("Ma sát packing có thể thay đổi đáng kể; ví dụ, các thử nghiệm với "
               "vật liệu làm kín chứa tetrafluoroethylene (TFE) cho thấy lực ma sát "
               "ban đầu (hay lực ma sát phá vỡ, breakaway friction) lớn gấp 1,5 lần "
               "lực ma sát động (chuyển động liên tục) [2]. Tuy nhiên, theo quy tắc "
               "kinh nghiệm, dùng 1,5 × diện tích thân van × P1 lớn nhất. Trong "
               "trường hợp này, giả sử thân van 3/8 in, ma sát packing = "
               "1,5(0,375²π/4) × 140 psig = 23 lb. Tổng lực thân van (đóng) vì vậy "
               "là 468 + 23 = 491 lb."))
    b.append(eq("ma sát packing = 1,5(0,375²π/4) × 140 psig = 23 lb", ""))
    b.append(eq("Tổng lực thân van (đóng) = 468 + 23 = 491 lb", ""))
    b.append(p("Như bạn thấy, yêu cầu lực của bộ truyền động tăng lên hơn mười lần. "
               "Trong trường hợp bộ truyền động piston, và giả sử có sẵn khí ít nhất "
               "80 psi, diện tích xi lăng tối thiểu phải là 491 lb / 80 lb/in² = 6,2 "
               "in², hay đường kính piston 3 in cho tác động cấp khí để đóng "
               "(air-to-close). Bạn cần một lực lò xo tối thiểu 491 lb nếu van phải "
               "thoát khí an toàn ở trạng thái đóng (fail close) khi mất khí."))
    b.append(eq("491 lb / 80 lb/in² = 6,2 in²", ""))
    b.append(p("Nếu bạn muốn bộ truyền động màng lò xo (spring-diaphragm) thoát khí "
               "an toàn ở trạng thái đóng và bạn chỉ định bộ định vị van, một lò xo "
               "dải 6 đến 15 psi trong bộ truyền động 100 in² là đủ. Tín hiệu đầu ra "
               "từ bộ định vị sẽ thay đổi như sau:"))
    b.append(ol([
        "Ở hành trình bằng không (van đóng), lực do lò xo tạo ra là 6 psi × 100 in² "
        "= 600 lb. Tuy nhiên, vì lực thân van khi tựa ở đây là 491 lb (cố đẩy lên), "
        "chỉ còn lại 600 − 491 lb = 109 lb để bộ truyền động mở van. Do đó tín hiệu "
        "khí là 109 lb/100 in² = 1,1 psi."
        + eq("6 psi × 100 in² = 600 lb;   600 − 491 = 109 lb;   109 lb / 100 in² = "
             "1,1 psi", ""),
        "Nhớ rằng, ở hành trình 75% (điều kiện vận hành bình thường), lực thân van "
        "của chúng ta giảm còn 47 lb. Tại điểm này, lò xo tạo ra lực [(15 psi − 6 "
        "psi) × 0,75 + 6 psi] × 100 in² = 12,75 psi × 100 in² = 1275 lb. Trừ đi 47 "
        "lb tác động lên (tức ngược chiều lò xo) = 1275 − 47 = 1228 lb lực lò xo "
        "ròng. Điều này tương ứng với tín hiệu đầu ra của bộ định vị là 1228 "
        "lb/100 in² = 12,28 psi."
        + eq("[(15 psi − 6 psi) × 0,75 + 6 psi] × 100 in² = 12,75 psi × 100 in² = "
             "1275 lb;   1275 − 47 = 1228 lb;   1228 / 100 = 12,28 psi", ""),
        "Như vậy chúng ta có dải tín hiệu đầu ra lắp đặt của bộ định vị từ 1,1 đến "
        "12,28 psi giữa zero và lưu lượng cực đại ở hành trình 75%. Điều này trái "
        "ngược với tín hiệu từ bộ điều khiển tới bộ định vị là 3 đến 12 psi. Điều "
        "này bác bỏ quan niệm sai lầm phổ biến rằng tín hiệu đầu ra của bộ định vị "
        "phải khớp với tín hiệu đầu vào.",
    ]))

    b.append(p("Như bạn thấy từ ví dụ này, nếu ngắt bộ định vị, van sẽ không bao "
               "giờ đóng được với tín hiệu không đổi 3 psi từ bộ chuyển đổi dòng–áp "
               "(I/P transducer), tức thiết bị chuyển đổi điện–khí nén. Đây chính "
               "là điều đã xảy ra ở nhiều nhà máy sử dụng máy tính hoặc bộ điều "
               "khiển kỹ thuật số một vòng (single-loop digital controllers) để "
               "điều khiển quá trình [3]. Các thiết bị này khóa tín hiệu 4 mA ở "
               "điều kiện quá trình bằng không.<sup>2</sup>"))
    b.append(note("<b>Chú thích 2.</b> Có thể chỉnh máy tính để dải thấp hơn hoặc "
                  "cao hơn (underrange/overrange) tín hiệu thêm 5% hoặc 0,8 mA. "
                  "Tuy nhiên, để tín hiệu giảm xuống dưới 2 mA có thể gây hỏng một "
                  "số bộ chuyển đổi I/P, với hậu quả nghiêm trọng cho vòng điều "
                  "khiển quá trình!"))
    b.append(p("Nếu bạn có bộ chuyển đổi I/P được hiệu chỉnh để đầu ra 3 đến 15 psi "
               "với đầu vào 4 đến 20 mA (và hầu hết đều như vậy), bạn sẽ liên tục "
               "cấp 3 psi tới van và, kết quả là, có thể gây rò rỉ van. Không may là "
               "tình huống này thường dẫn đến cuộc gọi cho nhà cung cấp để phàn nàn "
               "rằng van của họ hỏng (chất lượng kém, v.v.)."))
    b.append(p("Có thể làm gì về vấn đề này? Theo thứ tự hiệu quả chi phí và ưu tiên "
               "kỹ thuật:"))
    b.append(ol([
        "Nếu có thể, giảm điểm zero của bộ chuyển đổi I/P xuống 1 psi tại 4 mA, "
        "hoặc chỉ định bộ chuyển đổi I/P có đầu ra 1 đến 17 psi theo tiêu chuẩn "
        "ANSI/FCI 87-2.",
        "Yêu cầu nhà cung cấp van chọn lò xo bộ truyền động có «dải bench» (bench "
        "range) 8 đến 15 psi. (Trong ví dụ trên, điều này sẽ cho dải lắp đặt từ 8 "
        "trừ 4,93 khi tựa đến 15 trừ 0,5 psi<sup>3</sup> ở hành trình 100%, tức "
        "3,1 đến 14,5 psi — đủ gần để gọi là dải 3 đến 15 psi!)",
        "Chỉ định bộ định vị van.",
    ]))
    b.append(note("<b>Chú thích 3.</b> Số 4,93 psi khi tựa tương ứng với 492 "
                  "lb/100 in² (lực thân van khi đóng chia cho diện tích bộ truyền "
                  "động 100 in²), còn 0,5 psi ở hành trình 100% tương ứng với 47 "
                  "lb/100 in² (lực thân van ở lưu lượng bình thường chia cho 100 "
                  "in²)."))
    b.append(p("Lưu ý rằng chỉ đơn giản tăng cài đặt lò xo ban đầu từ, chẳng hạn, "
               "3 psi lên 6 psi thì không được. Bạn sẽ có dải bench 6 đến 18 psi và "
               "van sẽ không mở đủ để xử lý những biến động lưu lượng. (Nhớ rằng "
               "tín hiệu I/P tiêu chuẩn không thể vượt quá 15 psi ở đầu vào 20 mA!)"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Bí ẩn lực thân van do áp suất đường ống, hay Chọn đúng kích cỡ "
                "bộ truyền động",
                "The mystery of line pressure-produced valve stem forces, or "
                "selecting the correct actuator size"))
    b.append(p("The selection of an adequate valve actuator is usually left up to "
               "the vendor. Most of the time this works well, especially if the "
               "pressure conditions the valve has to handle are low or the valve "
               "size is small. However, it will be of value to know some of the "
               "consequences of selecting the wrong (usually too small) actuator "
               "size. Remember, the valve vendor who got the job was probably the "
               "lowest bidder and, often, the bidder who cut the size of actuators "
               "in order to reduce costs. Following is a description of what can "
               "happen after installation."))

    b.append(h2("Van không đóng kín đúng cách", "The valve does not close properly"))
    b.append(p("The economically dictated demise of bypass installations around a "
               "control valve has led to the requirement that a control valve "
               "should have ANSI/FCI Class IV seat tightness (to double as a "
               "shutoff valve when the system is down). This works well as long as "
               "the initial spring setting, the air pressure, and the size of the "
               "actuator are adequate to overcome the fluid pressure acting on the "
               "valve plug (assuming a single-seated globe valve)."))
    b.append(p("To start with, it is important to tell the vendor what the maximum "
               "inlet pressure is! This is usually the pressure differential across "
               "the plug when the valve is shut off and not the lower inlet pressure "
               "and substantially higher outlet pressure that the valve sees during "
               "normal throttling or that is used for calculating the valve Cv. A "
               "responsible valve vendor will always assume the valve has to shut "
               "off against the maximum inlet pressure and with a zero-gauge outlet "
               "pressure. Therefore, P1 must be stated on the specification form "
               "(see Figure 11-1). There are two types of closure: one to stop flow "
               "and the other to stop leakage [1]."))
    b.append(fig(1, F.fig_f111()))

    b.append(p("There are also two types of valve closure mechanisms. A push type, "
               "such as a valve plug, closes against an orifice. To stop leakage, "
               "additional force above the one needed to overcome the off-balance "
               "is required. This additional force for Class IV tightness should be "
               "at least 2.5 times the contact seating area times P1. For example, "
               "a 2-inch orifice has a beveled contact area of 2 in × 3.14 × 0.063 "
               "in = 0.4 in². Thus, when P1 is 100 psi, one would need 100 psi × 0.4 "
               "in² × 2.5 = 100 lb extra seating force."))
    b.append(eq("2 in × 3.14 × 0.063 in = 0.4 in²", ""))
    b.append(eq("100 psi × 0.4 in² × 2.5 = 100 lb", ""))
    b.append(p("For Class V, one might need a compression force equal to the yield "
               "point of the contact area."))
    b.append(p("The second form of closure is sliding contact. This is typical for "
               "lined butterfly valves and segmented ball valves, where the closure "
               "member has to slide in and partially deform the seal. While the "
               "initial contact with a seal ring might stop flow, it is insufficient "
               "to stop leakage. An extra 5° of actuator travel is required to move "
               "the closure member from stopping flow to stopping leakage. This must "
               "be considered during the initial positioner and actuator "
               "calibration."))

    b.append(p("For example, a heating valve with a 2-inch orifice handling hot oil "
               "will see, at the normal flow rate and 75% valve travel, an inlet "
               "pressure of 125 psig and a downstream pressure of 110 psig. The stem "
               "forces sensed by the actuator under these conditions are (2²π/4) × "
               "(125 − 110) = 47 lb.<sup>1</sup>"))
    b.append(eq("(2²π/4) × (125 − 110) = 47 lb", ""))
    b.append(note("<b>Footnote 1.</b> Neglecting the area of the valve stem for "
                  "simplicity."))
    b.append(p("However, if called to close, the inlet pressure will be 140 psig due "
               "to the increase in pressure following the pump's characteristic, "
               "while the downstream pressure may be zero. In this case, the minimum "
               "stem force will be 140 psi times the seating area of the plug (use "
               "for seating diameter at least 1/16 in plus the orifice diameter) "
               "plus the packing friction."))
    b.append(eq("(2.063²π/4) × 140 = 468 lb;   stem force (closed) = 468 lb + "
                "packing friction", ""))
    b.append(p("Packing friction can vary considerably; for example, tests with "
               "tetrafluoroethylene (TFE)-containing packing material showed that "
               "starting friction (or breakaway friction) was 1.5 times that of "
               "dynamic (constant movement) friction [2]. However, as a rule of "
               "thumb, use 1.5 × stem area × maximum P1. In this case, assume a 3/8-"
               "inch stem, packing friction = 1.5(0.375²π/4) × 140 psig = 23 lb. "
               "Total stem force (closed) is, therefore, 468 + 23 = 491 lb."))
    b.append(eq("packing friction = 1.5(0.375²π/4) × 140 psig = 23 lb", ""))
    b.append(eq("Total stem force (closed) = 468 + 23 = 491 lb", ""))
    b.append(p("As you can see, there is more than a tenfold increase in actuator "
               "force requirement. In the case of a piston actuator, and assuming "
               "the availability of at least 80 psi air, the minimum cylinder area "
               "should be 491 lb / 80 lb/in² = 6.2 in², or a 3-inch piston diameter "
               "for air-to-close action. You need a minimum spring force of 491 lb "
               "if the valve should fail close on air failure."))
    b.append(eq("491 lb / 80 lb/in² = 6.2 in²", ""))
    b.append(p("If you want a spring-diaphragm actuator to fail close and you "
               "specify a valve positioner, a 6 to 15 psi span spring inside a 100 "
               "in² actuator would be adequate. The output signal from the "
               "positioner would vary as follows:"))
    b.append(ol([
        "At zero travel (valve shut), the force created by the spring is 6 psi × "
        "100 in² = 600 lb. However, because the seating stem force here is 491 lb "
        "(trying to push up), it leaves only 600 − 491 lb = 109 lb for the actuator "
        "to open the valve. Therefore, the air signal is 109 lb/100 in² = 1.1 psi."
        + eq("6 psi × 100 in² = 600 lb;   600 − 491 = 109 lb;   109 lb / 100 in² = "
             "1.1 psi", ""),
        "Remember, at 75% travel (normal operating conditions) our stem forces are "
        "reduced to 47 lb. At this point, our spring exerts a force of [(15 psi − 6 "
        "psi) × 0.75 + 6 psi] × 100 in² = 12.75 psi × 100 in² = 1275 lb. Subtracting "
        "from this value the 47 lb acting up (i.e., against the spring) = 1275 − 47 "
        "= 1228 lb net spring force. This translates into a positioner output signal "
        "of 1228 lb/100 in² = 12.28 psi."
        + eq("[(15 psi − 6 psi) × 0.75 + 6 psi] × 100 in² = 12.75 psi × 100 in² = "
             "1275 lb;   1275 − 47 = 1228 lb;   1228 / 100 = 12.28 psi", ""),
        "We thus have an installed positioner output signal span of 1.1 to 12.28 psi "
        "between zero and maximum flow at 75% travel. This is in contrast to a "
        "controller signal to the positioner of 3 to 12 psi. This contradicts a "
        "common fallacy that the output signal of a positioner has to match the "
        "input signal.",
    ]))

    b.append(p("As you can see from this example, if you were to disconnect the "
               "positioner, the valve would never close with a constant 3 psi input "
               "signal from an I/P transducer (electro-pneumatic converting "
               "instrument). This is exactly what has happened in many plants that "
               "utilize computers or single-loop digital controllers for process "
               "control [3]. These devices lock in the 4 mA signal at zero process "
               "conditions.<sup>2</sup>"))
    b.append(note("<b>Footnote 2.</b> It is possible to adjust your computer to "
                  "underrange or overrange the signal by 5% or 0.8 mA. However, "
                  "allowing the signal to decrease below 2 mA can cause the failure "
                  "of certain I/P transducers with dire consequences for your process "
                  "loop!"))
    b.append(p("If you have an I/P transducer that is calibrated to have a 3 to 15 "
               "psi output range for a 4 to 20 mA input signal (and most are), you "
               "will continuously feed 3 psi to the valve and, as a result, could "
               "cause valve leakage. Unfortunately, this situation most often leads "
               "to a call to the vendor informing it that its valve is bad (poor "
               "quality, etc.)."))
    b.append(p("What can be done about it? In order of cost-effectiveness and "
               "engineering preference:"))
    b.append(ol([
        "If you can, reduce the zero setting on your I/P transducer to 1 psi at 4 "
        "mA, or specify an I/P transducer with a 1 to 17 psi output per ANSI/FCI "
        "standard 87-2.",
        "Ask your valve vendor to select an actuator spring with an 8 to 15 psi "
        "“bench range.” (This, in the earlier example, will give you an installed "
        "range of between 8 minus 4.93 when seated and 15 minus 0.5 psi<sup>3</sup> "
        "at 100% travel, which is 3.1 to 14.5 psi, close enough to be called a 3 to "
        "15 psi range!)",
        "Specify a valve positioner.",
    ]))
    b.append(note("<b>Footnote 3.</b> The 4.93 psi seated correction corresponds to "
                  "492 lb/100 in² (the closed stem force divided by the 100 in² "
                  "actuator area), and the 0.5 psi correction at 100% travel "
                  "corresponds to 47 lb/100 in² (the normal-flow stem force divided "
                  "by 100 in²)."))
    b.append(p("Note that simply cranking up the initial spring setting from, say, "
               "3 psi to 6 psi will not do. You will end up with a bench range of 6 "
               "to 18 psi, and your valve will not open enough to handle flow "
               "upsets. (Remember, a standard I/P signal cannot exceed 15 psi at 20 "
               "mA input!)"))
    return "".join(b)
