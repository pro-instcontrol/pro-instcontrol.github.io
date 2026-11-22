# -*- coding: utf-8 -*-
"""Book 7, Chapter 1 — What Is a Control Valve and How Does It Affect My
Control Loop? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer: A User's Guide*, 5th ed. (ISA / Wiley),
printed pp. 1–8 (PDF pp. 9–16). Three source figures: 1-1 terminology tree,
1-2 control-loop block diagram, 1-3 early 1932 double-seated valve.
"""
from cvp_common import (fig, h2, h3, note, p, ul)
import cvpfig as F

PAGES_SRC = 8
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "What Is a Control Valve and How Does It Affect My Control Loop?"
TITLE_VI = "Van điều khiển là gì và nó ảnh hưởng thế nào đến vòng điều khiển?"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 1.</b> vòng điều khiển · phần tử chấp hành cuối (final "
                "control element) · độ khuếch đại van K<sub>v</sub> · thời gian chết T<sub>Dv</sub> "
                "· hằng số thời gian T<sub>Cv</sub> · vùng chết (deadband) · độ trễ (hysteresis) "
                "· đặc tính lưu lượng lắp đặt (installed flow characteristic) · khả năng điều "
                "tiết (rangeability) · C<sub>v</sub> hệ số lưu lượng · bộ định vị (positioner) · "
                "van điều khiển tự tác dụng (self-acting regulator).")
    return ("<b>Key terms.</b> control loop · final control element · valve gain K<sub>v</sub> · "
            "dead time T<sub>Dv</sub> · time constant T<sub>Cv</sub> · deadband · hysteresis · "
            "installed flow characteristic · rangeability · C<sub>v</sub> flow coefficient · "
            "positioner · self-acting regulator.")


def body_vi():
    b = []
    b.append(h2("Van điều khiển — “cơ bắp” của vòng điều khiển",
                "The control valve — the muscle of the loop"))
    b.append(p("Van điều khiển có thể là bộ phận quan trọng nhất, nhưng đôi khi lại bị bỏ quên, "
               "của một vòng điều khiển. Lý do thường là kỹ sư thiết bị không quen thuộc với "
               "nhiều mặt, thuật ngữ và lĩnh vực kỹ thuật có thể liên quan — cơ học chất lưu, "
               "luyện kim, kiểm soát tiếng ồn, thiết kế đường ống và bình chứa — tùy theo mức "
               "độ khắc nghiệt của điều kiện làm việc."))
    b.append(p("Một vòng điều khiển thường gồm cảm biến trạng thái quá trình, bộ phát tín hiệu "
               "và bộ điều khiển so sánh biến quá trình nhận được với điểm đặt, tức trạng thái "
               "quá trình mong muốn. Bộ điều khiển gửi tín hiệu hiệu chỉnh tới <b>phần tử chấp "
               "hành cuối</b> — phần cuối của vòng và là “cơ bắp” của hệ thống điều khiển quá "
               "trình. Nếu cảm biến là mắt và bộ điều khiển là não, thì phần tử chấp hành cuối "
               "là đôi tay của vòng điều khiển. Điều này khiến nó trở thành bộ phận quan trọng "
               "nhất — than ôi, đôi khi cũng là bộ phận ít được hiểu rõ nhất — của một hệ thống "
               "điều khiển tự động. Một phần nguyên nhân là sự gắn bó quá mức của chúng ta với "
               "hệ thống điện tử và máy tính, khiến ta hơi xao nhãng việc hiểu đúng và dùng đúng "
               "phần cứng then chốt đó."))
    b.append(p("Van điều khiển là loại phần tử chấp hành cuối phổ biến nhất; tuy nhiên còn có "
               "những loại khác:"))
    b.append(ul([
        "thiết bị điều tiết (tiết lưu) năng lượng điện, chẳng hạn SCR (silicon-controlled rectifier);",
        "bộ truyền động tốc độ thay đổi;",
        "bộ cấp liệu, bơm và bộ truyền băng;",
        "cửa gió (damper).",
    ]))
    b.append(p("Một số thiết bị này thực hiện chức năng tương tự van điều khiển và có thể dùng "
               "thay thế. Chẳng hạn, để điều khiển pH, có thể dùng bơm định lượng kiểu hành "
               "trình thay đổi để bơm axit vào nước thải (thay vì dùng van điều khiển lót "
               "PTFE — polytetrafluoroethylene)."))

    b.append(h2("Thế nào là van điều khiển?",
                "What, then, is a control valve?"))
    b.append(p("Đây là câu hỏi khó, vì có sự chồng chéo đáng kể với các loại van khác. Chẳng hạn, "
               "một van chỉ đóng/mở hoàn toàn (như van điện từ nước nóng trong hệ thống sưởi "
               "gia đình) có thể thay bằng một van bi đơn giản do xi lanh khí nén vận hành — "
               "kiểu thường gọi là van tự động hóa (automated valve). Điểm khác biệt thường được "
               "chấp nhận giữa <b>van tự động hóa</b> và <b>van điều khiển</b> là khả năng "
               "<i>điều tiết liên tục</i> của loại sau: nó có thể nhận vô số vị trí tiết lưu "
               "trong quá trình điều khiển bình thường."))
    b.append(p("Có ba thành phần vật lý cơ bản của van điều khiển:"))
    b.append(ul([
        "<b>Cụm thân van</b> — bộ phận làm việc, tự thân nó là một bình áp lực.",
        "<b>Cơ cấu chấp hành (actuator)</b> — thiết bị định vị phần tử tiết lưu bên trong thân van.",
        "<b>Phụ tùng</b> — bộ định vị, bộ chuyển đổi I/P, công tắc hành trình, tay quay, bộ "
        "điều chỉnh khí (air set), cảm biến vị trí, van điện từ và chặn hành trình.",
    ]))
    b.append(p("Bảng phân loại chi tiết hơn về các loại van, cơ cấu chấp hành và bộ định vị "
               "được thể hiện ở Hình 1-1."))
    b.append(fig(1, F.fig_f11()))

    b.append(h2("Van điều khiển phải làm gì?",
                "What should the control valve do?"))
    b.append(p("Giờ ta xét xem van điều khiển cần làm gì. Nhìn vào Hình 1-2 — sơ đồ vòng điều "
               "khiển quá trình được đơn giản hóa — ta thấy ba khối chức năng quan trọng phía "
               "trên ký hiệu van điều khiển."))
    b.append(p("Thứ nhất là <b>độ khuếch đại van K<sub>v</sub></b>. Nó được xác định bởi "
               "<i>đặc tính lưu lượng “lắp đặt”</i> của van — rất khác với đặc tính ghi trong "
               "catalog của nhà sản xuất. K<sub>v</sub> cho biết lưu lượng qua van thay đổi "
               "bao nhiêu khi tín hiệu thay đổi một lượng nhất định (xem thêm Chương 8, “Về an "
               "toàn khi mất điện”)."))
    b.append(p("Thứ hai là <b>thời gian chết của van T<sub>Dv</sub></b> — thời gian trôi qua "
               "trước khi van bắt đầu chuyển động sau khi bộ điều khiển thay đổi tín hiệu. Thường "
               "do ma sát của van và cơ cấu chấp hành, nhưng cũng có thể gồm độ trễ do đường "
               "truyền tín hiệu khí nén dài và thời gian tăng áp trong buồng màng."))
    b.append(p("Cuối cùng, khối thứ ba là <b>hằng số thời gian của van T<sub>Cv</sub></b> — liên "
               "quan đơn giản đến tốc độ hành trình của cơ cấu chấp hành, hoặc của tổ hợp cơ "
               "cấu chấp hành và bộ định vị (xem Chương 9, “Vì sao hầu hết chọn đặc tính lưu "
               "lượng phần trăm bằng nhau”), tức van phản ứng nhanh thế nào trước một nhiễu "
               "động của biến được điều khiển. Tất cả các khối chức năng này tương tác với nhau, "
               "và mỗi khối cần được xem xét khi đánh giá một ứng dụng van điều khiển."))
    b.append(fig(2, F.fig_f12()))
    b.append(p("<b>Van “lý tưởng”</b> sẽ có độ khuếch đại không đổi trong toàn dải lưu lượng "
               "— tức đặc tính lưu lượng “lắp đặt” tuyến tính — không có thời gian chết khi "
               "bao bình đã được siết chặt, và hằng số thời gian khác với của quá trình ít nhất "
               "ba lần. Không cần phải nói là <b>van điều khiển “lý tưởng” không hề tồn tại</b>. "
               "Vì thế, ta hãy cố đạt một sự thỏa hiệp khả thi."))

    b.append(h2("Điều cần tìm ở thiết kế van điều khiển tốt",
                "What to look for in a good control valve design"))
    b.append(p("Trên thị trường có nhiều loại van, nhưng phần lớn (khoảng 80%) dùng để đóng cắt. "
               "Điều làm van điều khiển khác biệt nhất là khả năng <b>điều tiết lưu lượng liên "
               "tục một cách có thể dự báo và kiểm soát được</b>."))
    b.append(p("Ngoài những điều hiển nhiên như tay nghề gia công tốt, lựa chọn vật liệu đúng "
               "và mức phát thải tiếng ồn, cần chú ý đặc biệt đến hai vấn đề:"))
    b.append(ul([
        "<b>Vùng chết thấp</b> của tổ hợp cơ cấu chấp hành/van (với bao bình siết chặt);",
        "<b>Đóng kín chặt</b> trong trường hợp van cầu một chỗ ngồi và một số van quay (nếu yêu cầu).",
    ]))
    b.append(p("Mối quan tâm hàng đầu của người vận hành một vòng điều khiển quá trình là "
               "<b>vòng phải ổn định</b>. (Không gì làm người ta căng thẳng bằng một mực đỏ "
               "dày đặc và những nét nhem nhuốc trên giấy ghi của máy ghi bút.) Phần tử chấp "
               "hành cuối ảnh hưởng đến độ ổn định của vòng nhiều hơn tất cả các phần tử điều "
               "khiển khác cộng lại."))

    b.append(h2("Thời gian chết và vùng chết",
                "Dead time and deadband"))
    b.append(p("Thủ phạm lớn nhất ở đây là <b>thời gian chết</b>.<sup>1</sup> Đó là thời gian để "
               "bộ điều khiển thay đổi tín hiệu đầu ra đủ để cơ cấu chấp hành và van chuyển sang "
               "vị trí mới. Nói cách khác, thời gian chết T<sub>Dv</sub> là thời gian để cơ cấu "
               "chấp hành khí nén thay đổi áp suất nhằm chuyển sang một vị trí hành trình khác. "
               "Nó thường liên quan đến vùng chết của tổ hợp cơ cấu chấp hành/van; hoặc, khi "
               "dùng bộ định vị, bằng vùng chết của van chia cho độ khuếch đại vòng hở của bộ "
               "định vị<sup>2</sup> cộng với vùng chết của chính bộ định vị. (Vùng chết khiến "
               "van không đáp ứng ngay khi tín hiệu thay đổi, từ đó gây ra thời gian chết.)"))
    b.append(p("Bản thân van không bao giờ nên có vùng chết lớn hơn <b>5% dải tín hiệu</b> — "
               "tức dưới 0,6 psi với dải tín hiệu 3 đến 15 psi, hoặc 0,8 mA với tín hiệu 4 "
               "đến 20 mA. Tổ hợp bộ định vị/van không nên vượt quá <b>0,5% dải tín hiệu</b>. "
               "Nếu bỏ qua động học của quá trình, một bộ định vị vì thế có thể cải thiện tình "
               "hình lên cả một bậc độ lớn. Tuy nhiên, bộ định vị có thể gây rối loạn động học "
               "của vòng điều khiển (xem Chương 9)."))
    b.append(p("Van lý tưởng vẫn là van mà <b>vùng chết vận hành với bao bình thân van siết "
               "chặt nhỏ hơn 1%</b>. Khi đó ta có độ ổn định tối đa mà không cần chi phí và độ "
               "phức tạp của bộ định vị. Tiếc là phần lớn van không thể làm việc mà không có bộ "
               "định vị. May mắn thay, bộ định vị hiện đại có khả năng chỉnh điện tử giúp giảm "
               "vùng chết (xem Chương 9)."))
    b.append(note("<sup>1</sup> Thời gian chết thường bị nhầm với độ trễ (hysteresis) — vùng "
                  "chết tạo ra khi cho hành trình đi lên xuống 100% rồi đo sự khác biệt tín "
                  "hiệu tại một điểm. Độ trễ không quan trọng trong hệ thống vòng kín. "
                  "<sup>2</sup> Giá trị này thường từ 50 đến 200; xem catalog bộ định vị của "
                  "nhà sản xuất."))
    b.append(fig(3, F.fig_f13()))
    b.append(p("Những van điều khiển đầu tiên đã nhận ra giá trị của vùng chết thấp. Van trong "
               "Hình 1-3 chẳng hạn có <b>ổ bi quanh thân cơ cấu chấp hành</b> để tránh xoắn lò "
               "xo và nhờ đó giảm ma sát (khoảng năm 1932)."))

    b.append(h2("Rò rỉ chỗ ngồi thấp và khả năng điều tiết",
                "Low seat leakage and rangeability"))
    b.append(p("<b>Rò rỉ chỗ ngồi thấp</b> có thể mang lại lợi ích. Thứ nhất, nó tiết kiệm chi "
               "phí bổ sung của một van đóng cắt khi hệ thống phải dừng. (Lưu ý: vì lý do an "
               "toàn, <b>không bao giờ được tin vào van điều khiển để đóng kín tuyệt đối</b>.) "
               "Thứ hai, nó tiết kiệm năng lượng. Thứ ba, đó là yêu cầu không thể thương lượng "
               "trong các ứng dụng điều khiển nhiệt độ của quá trình theo mẻ, đặc biệt khi cấp "
               "chất lỏng gia nhiệt cho một hóa chất có thể xảy ra phản ứng tỏa nhiệt."))
    b.append(p("Một đặc điểm khác là <b>khả năng điều tiết (rangeability)</b> tốt. Như bạn có "
               "thể đã biết, van thường bị chọn quá lớn — nghĩa là trong điều kiện lưu lượng "
               "bình thường chúng chỉ làm việc ở khoảng 30% C<sub>v</sub> định mức. Hơn nữa, "
               "không nên vận hành bộ lót van thông thường dưới <b>5% hành trình</b>. Lý do là "
               "bộ điều khiển có thể hơi mất ổn định ở lưu lượng thấp, và cơ cấu chấp hành, đi "
               "theo dao động hình sin của tín hiệu điều khiển, sẽ đẩy nút van vào chỗ ngồi. "
               "Khi đó cơ cấu chấp hành và bộ định vị sẽ xì hết không khí, tạo ra một thời gian "
               "chết rất lớn (trước khi van lại chuyển động) khi tín hiệu đảo chiều. Nói ngắn "
               "gọn: bạn có một mớ hỗn độn và không còn sự điều khiển."))
    b.append(p("Với giới hạn 5% hành trình, ta xác định C<sub>v</sub> chỉ khoảng <b>7% của "
               "C<sub>v</sub> định mức</b> với đặc tính tuyến tính, và không thấp hơn nhiều với "
               "hầu hết nút van có đặc tính phần trăm bằng nhau. Điều này cho ta một dải hữu "
               "dụng của C<sub>v</sub> trên mức bình thường là 30% chia cho 7%, tức <b>4,5:1</b>. "
               "Tuy nhiên, trong hầu hết các vòng, tổn thất áp suất qua van luôn thay đổi tỷ "
               "nghịch với lưu lượng — tức Δp thấp ở lưu lượng lớn và Δp cao ở lưu lượng nhỏ. "
               "Vì vậy tỷ lệ lưu lượng lớn/nhỏ có thể điều khiển được trên thực tế có thể chỉ "
               "khoảng <b>3:1</b>."))
    b.append(p("Tỷ lệ này chính là <b>khả năng điều tiết</b>: khả năng điều tiết nội tại của van "
               "là tỷ lệ giữa C<sub>v</sub> lớn nhất và nhỏ nhất có thể điều khiển, còn khả "
               "năng điều tiết lắp đặt là tỷ lệ giữa lưu lượng lớn nhất và nhỏ nhất có thể "
               "điều khiển trong vòng."))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 1 chiếm tr. 1–8 của ấn bản in (PDF tr. 9–16). Nguyên bản có ba hình: "
               "Hình 1-1 cây thuật ngữ theo ANSI/ISA-75.05.01, Hình 1-2 sơ đồ khối vòng điều "
               "khiển và Hình 1-3 mặt cắt van lò xo–màng hai chỗ ngồi năm 1932. Cả ba được vẽ "
               "lại dạng vector trong bản dịch này."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("The control valve — the muscle of the loop",
                "Van điều khiển — “cơ bắp” của vòng điều khiển"))
    b.append(p("Control valves may be the most important, but sometimes the most neglected, "
               "part of a control loop. The reason is usually the instrument engineer's "
               "unfamiliarity with the many facets, terminologies, and areas of engineering "
               "disciplines — such as fluid mechanics, metallurgy, noise control, and piping "
               "and vessel design — that can be involved depending on the severity of service "
               "conditions."))
    b.append(p("Any control loop usually consists of a sensor of the process condition, a "
               "transmitter, and a controller that compares the process variable received "
               "from the transmitter with the set point, that is, the desired process "
               "condition. The controller, in turn, sends a corrective signal to the <b>final "
               "control element</b>, the last part of the loop and the “muscle” of the process "
               "control system. If the sensors of the process variables are the eyes, and the "
               "controller is the brain, then the final control element is the hands of the "
               "control loop. This makes it the most important, alas sometimes the least "
               "understood, part of an automatic control system. This comes about, in part, "
               "due to our strong attachment to electronic systems and computers causing "
               "some neglect in the proper understanding and proper use of the all-important "
               "hardware."))
    b.append(p("Control valves are the most common type of final control elements; however, "
               "there are other types, such as"))
    b.append(ul([
        "devices that regulate (throttle) electric energy such as silicon-controlled rectifiers;",
        "variable-speed drives;",
        "feeders, pumps, and belt drives; and",
        "dampers.",
    ]))
    b.append(p("Some of these devices perform functions similar to those of control valves and "
               "could be used as an alternative. For example, to control the pH level, a "
               "variable stroke-type metering pump may be used to inject acid into wastewater "
               "(instead of using a control valve lined with polytetrafluoroethylene [PTFE])."))

    b.append(h2("What, then, is a control valve?",
                "Thế nào là van điều khiển?"))
    b.append(p("This is a difficult question because there is considerable overlap with other "
               "types of valves. For example, a valve operating strictly in the on-off mode "
               "(such as the hydronic solenoid valve in your home heating system) could be "
               "replaced by a simple ball valve operated by a pneumatic cylinder, a type "
               "usually referred to as an automated valve. The distinction between "
               "<b>automated</b> and <b>control valves</b> is usually considered to be the "
               "ability of the latter to <i>modulate</i>, that is, to assume an infinite number "
               "of “throttling” travel positions during normal control service."))
    b.append(p("There are three basic physical components of a control valve:"))
    b.append(ul([
        "<b>The valve body subassembly</b> — the working part and, in itself, a pressure vessel.",
        "<b>The actuator</b> — the device that positions the throttling element inside the "
        "valve body.",
        "<b>Accessories</b> — positioners, I/P transducers, limit switches, handwheels, air "
        "sets, position sensors, solenoid valves, and travel stops.",
    ]))
    b.append(p("A more detailed breakdown of the various types of valves, actuators, and "
               "positioners is shown in Figure 1-1."))
    b.append(fig(1, F.fig_f11()))

    b.append(h2("What should the control valve do?",
                "Van điều khiển phải làm gì?"))
    b.append(p("Now let us discuss what the control valve should do. Referring to Figure 1-2, "
               "which shows a somewhat simplified process control loop diagram, we see three "
               "important function blocks above the control valve symbol."))
    b.append(p("The first one is <b>control valve gain (Kᵥ)</b>. This is determined by the "
               "<i>installed flow characteristic</i> of the valve (quite different from the "
               "characteristic shown in the vendor's catalog). Kᵥ tells you how much the flow "
               "through the valve is changing per a given signal change (see Chapter 8, "
               "“What About Fail-Safe?”)."))
    b.append(p("The second block shows the <b>control valve dead time (Tᴅᵥ)</b>. This is the "
               "time it takes before a valve moves following a controller signal change. This "
               "is usually determined by the valve and actuator friction but may include time "
               "lags due to long pneumatic signal transmission lines and the time to build "
               "the pressure in a diaphragm case, for example."))
    b.append(p("Finally, the third block shows the <b>time constant of the valve (Tᴄᵥ)</b>. "
               "This is simply related to the stroking speed of the actuator or "
               "actuator/positioner combination (see Chapter 9, “Why Most People Choose "
               "‘Equal Percentage’ as a Flow Characteristic”), that is, how fast the valve is "
               "responding to an upset in the controlled variable. All these function blocks "
               "interact, and each one should be considered in evaluating a control valve "
               "application."))
    b.append(fig(2, F.fig_f12()))
    b.append(p("The <b>“ideal” valve</b> should have a constant gain throughout the flow range, "
               "that is, a linear “installed” flow characteristic, no dead time with packing "
               "tightened, and a time constant that is different from that of the process by "
               "at least a factor of three. Need I tell you that there is no such thing as the "
               "<b>“ideal” control valve</b>? So, let us attempt to develop a workable compromise."))

    b.append(h2("What to look for in a good control valve design",
                "Điều cần tìm ở thiết kế van điều khiển tốt"))
    b.append(p("There are many valve types on the market — most (about 80%) are used for "
               "shutoff purposes. What distinguishes control valves most is that they can "
               "<b>continuously modulate flow in a predicted and controlled manner</b>."))
    b.append(p("Besides the obvious, such as good quality workmanship, correct selection of "
               "materials, and noise emission, special attention should be paid to two areas:"))
    b.append(ul([
        "<b>Low deadband</b> of the actuator/valve combination (with tight packing).",
        "<b>Tight shutoff</b>, in cases of single-seated globe valves and some rotary valves "
        "(if required).",
    ]))
    b.append(p("The prime concern of the operator of a process control loop is to have a "
               "<b>loop that is stable</b>. (Nothing makes people more nervous than a lot of "
               "red ink and scattered lines on a strip of paper from a recorder.) The final "
               "control element will influence the stability of a loop more than all the other "
               "control elements combined."))

    b.append(h2("Dead time and deadband", "Thời gian chết và vùng chết"))
    b.append(p("The biggest culprit here is <b>dead time</b>.<sup>1</sup> This is the time it "
               "takes for the controller to vary the output signal sufficiently to make the "
               "actuator and the valve move to a new position. In other words, dead time "
               "(Tᴅᵥ), is the time it takes for the pneumatic actuator to change the pressure "
               "in order to move to a different travel position. It is most commonly related "
               "to the deadband of the actuator/valve combination, or in the case where a "
               "positioner is used, the deadband of the valve divided by the open-loop gain "
               "of the positioner<sup>2</sup> plus the positioner's deadband. (Deadband keeps "
               "the valve from responding instantly when the signal changes, which, in turn, "
               "causes dead time.)"))
    b.append(p("The valve itself should never have a deadband of more than <b>5% of span</b>, "
               "that is, less than 0.6 psi for a 3 to 15 psi signal span or 0.8 mA for a 4 to "
               "20 mA signal. The positioner/valve combination should have no more than "
               "<b>0.5% of signal span</b>. Ignoring process dynamics, a positioner may, "
               "therefore, improve matters by an order of magnitude. However, positioners can "
               "raise havoc with the dynamics of a control loop (see Chapter 9)."))
    b.append(p("The ideal valve is still the one in which the <b>operating deadband with tight "
               "stem packing is less than 1%</b>. There you have maximum stability without the "
               "extra cost and complication of having to use a valve positioner. Unfortunately, "
               "the majority of valves cannot operate without a positioner. Luckily, modern "
               "positioners have electronic tuning capabilities that can help to drive the "
               "deadband down (see Chapter 9)."))
    b.append(note("<sup>1</sup> This is often confused with hysteresis, a deadband produced by "
                  "moving the travel up and down 100% and then measure the difference in "
                  "signal at a given point. Hysteresis is not important in a closed-loop "
                  "system. <sup>2</sup> This value is usually 50 to 200. Consult the vendor's "
                  "published positioner catalog."))
    b.append(fig(3, F.fig_f13()))
    b.append(p("The first control valves recognized the value of low deadband. The valve in "
               "Figure 1-3, for example, features <b>ballbearings around the actuator stem</b> "
               "to avoid twisting the spring and thereby reducing friction (circa 1932)."))

    b.append(h2("Low seat leakage and rangeability",
                "Rò rỉ chỗ ngồi thấp và khả năng điều tiết"))
    b.append(p("<b>Low seat leakage</b> can be beneficial. First, it saves the extra expense of "
               "a shutoff valve in case the system closes down. (Note: For safety reasons, "
               "<b>never rely on the control valve for absolute tight shutoff</b>.) Second, it "
               "saves energy. Third, it is an unqualified requirement in temperature control "
               "applications in a batch process, especially when you are supplying a heating "
               "fluid to a chemical that can undergo an exothermic reaction."))
    b.append(p("Another feature is good <b>rangeability</b>. As you probably already know, "
               "valves are usually terribly oversized. That is, they operate at perhaps only "
               "30% of their rated Cᵥ under normal flow conditions. Furthermore, it is not wise "
               "to operate a conventional valve trim at less than <b>5% travel</b>. The reason "
               "is that the controller might be slightly unstable at the low flow rates, and "
               "the actuator, following the sinusoidal output of the controller signal, will "
               "push the plug against the seat. When this happens, the actuator and positioner "
               "will bleed all the air out, resulting in a really big dead time (before the "
               "valve gets moving again) on signal reversal. In short, you have a big mess and "
               "no control."))
    b.append(p("Using the 5% travel limit, we determine that the Cᵥ is only about <b>7% of the "
               "rated Cᵥ</b> with a linear characteristic and not much less with most equal "
               "percentage characterized plugs. This gives us a useful range for the "
               "above-normal Cᵥ of 30% divided by 7%, which is <b>4.5:1</b>. However, in most "
               "loops, the pressure drop across the valve always varies inversely with the "
               "flow, that is, a low Δp at maximum flow and a high Δp with low flow. We "
               "therefore might find that the actual controllable ratio of maximum to minimum "
               "flow is perhaps only <b>3:1</b>."))
    b.append(p("Incidentally, this ratio is the <b>rangeability</b>: the inherent rangeability "
               "of a valve is the ratio of maximum to minimum controllable Cᵥ, while the "
               "installed rangeability is the ratio of maximum to minimum controllable flow "
               "rate in the loop."))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 1 occupies printed pp. 1–8 (PDF pp. 9–16). The source has three "
               "figures: Figure 1-1 terminology tree after ANSI/ISA-75.05.01, Figure 1-2 "
               "control-loop block diagram, and Figure 1-3 the 1932 double-seated "
               "spring-diaphragm valve cross-section. All three are redrawn as vectors here."))
    return "".join(b)
