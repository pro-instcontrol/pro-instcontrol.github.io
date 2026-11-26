# -*- coding: utf-8 -*-
"""Book 7, Chapter 24 - Avoiding Leaky Valve Stem Packing / Tránh rò rỉ đệm
làm kín thân van (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
147-152 (PDF pp. 145-150; printed = PDF + 2). Six printed pages, eight packing
rules, three leakage examples, one figure (an unlabelled bellows-seal cutaway
in the source, redrawn here as a labelled vector schematic), bellows failure
modes, two references and two additional-reading items.
"""
from cvp_common import fig, h2, h3, h4, lead, note, ol, p, refs, ul

import cvpfig24 as F

PAGES_SRC = 6
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Avoiding Leaky Valve Stem Packing"
TITLE_VI = "Tránh rò rỉ đệm làm kín thân van"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 24.</b> đệm làm kín thân van (stem packing) · rò rỉ · "
                "ma sát thân van · thời gian chết (dead time) · vòng V bằng Teflon · đệm "
                "Chevron · đệm TFE-asbestos · Kalrez · bôi trơn · vòng cắt rời (split ring) · "
                "bích ép đệm · hệ số giãn nở nhiệt · chiều sâu đệm hữu dụng · hành trình van "
                "· mòn rãnh · van quay · mất căn chỉnh · đệm màng (bellows seal) · đệm dự phòng "
                "· kết nối báo động (telltale connection) · áp suất cấp trong/ngoài · "
                "đệm màng thành đôi · thử áp lực đường ống · búa nước · mỏi · xung áp · "
                "bộ giảm xung · hư hỏng cơ khí · van không đệm (packless valve)")
    return ("<b>Key terms.</b> valve stem packing · leakage · stem friction · dead time · "
            "Teflon V-ring · Chevron packing · TFE-asbestos packing · Kalrez · lubricator · "
            "split ring · packing follower · thermal expansion coefficient · effective "
            "packing depth · valve travel · groove wear · rotary valve · misalignment · "
            "bellows seal · backup packing · telltale connection · internal/external "
            "pressurization · double-walled bellows · hydrostatic line test · water hammer · "
            "fatigue · pressure pulsation · pulsation damper · mechanical damage · packless valve")


def body_vi():
    b = []
    b.append(lead("Đệm làm kín thân van là một trong những bộ phận quan trọng nhất của van "
                  "điều khiển, nhưng lại thường bị hiểu sai. Một đệm bị mòn gây rò rỉ chất "
                  "lỏng ra ngoài; ngược lại, một đệm quá chặt có thể làm vòng điều khiển "
                  "mất ổn định. Đệm tốt phải có ma sát thấp và rò rỉ thấp — không phải rò rỉ "
                  "bằng không, vì không có cái gọi là rò rỉ zero."))

    b.append(h2("Vật liệu đệm và kinh nghiệm lắp đặt", "Packing materials and installation practice"))
    b.append(p("Thời kỳ amiăng còn là vật liệu chuẩn, hộp đệm có bộ bôi trơn để người bảo trì "
               "bơm mỡ vào đệm. Mỡ vừa giảm ma sát, vừa tạo lớp trung gian có độ nhớt cao "
               "giữa thành hộp và bề mặt thân van, giúp làm kín tốt hơn. Mỗi phân xưởng bảo "
               "trì phải dựng nhiều loại mỡ với độ nhớt khác nhau theo nhiệt độ và khả năng "
               "chống ăn mòn của chất lưu."))
    b.append(p("Teflon đã thay đổi mọi thứ. Đệm V-ring toàn Teflon hoặc dạng Chevron được một "
               "số người ưa chuộng, trong khi đệm amiăng bôi TFE lại được số khác ưa chuộng; "
               "cả hai trở thành tiêu chuẩn công nghiệp. Ngày nay còn có nhiều vật liệu nhựa "
               "khác như Kalrez. Dạng vòng cắt rời (split ring) của đệm TFE-graphite hoặc "
               "TFE-Kevlar cho phép sửa van khẩn cấp ngay trên đường ống bằng cách luồn thêm "
               "một hoặc hai vòng dưới bích ép đệm. Nhược điểm vẫn là độ kín phụ thuộc vào "
               "\"cảm giác\" của người bảo trì: nhiều bộ điều khiển được chỉnh rất kỹ đã "
               "mất ổn định vì siết đệm quá chặt làm tăng ma sát và thời gian chết của van."))

    b.append(h2("Các quy tắc tránh sự cố với đệm thân van",
                "Rules for avoiding trouble with valve stem packing"))
    b.append(ol([
        "Đảm bảo đệm đã được siết chặt trước khi đưa van vào vận hành; một số nhà sản xuất "
        "giao van với bích hoặc đai ốc ép đệm còn lỏng.",
        "Nếu dùng chất lỏng nóng, siết lại đệm sau khi van đã đạt nhiệt độ làm việc đầy đủ "
        "trong lần chạy đầu tiên.",
        "Trong khi lắp đặt, không xoay cơ cấu chấp hành (ví dụ để đổi vị trí bộ định vị) khi "
        "chưa nới lỏng đệm: tâm thân van và tâm đệm không hoàn toàn trùng nhau; đệm lỏng sẽ "
        "thích ứng được với sự thay đổi tâm.",
        "Không để vòng điều khiển hoặc cơ cấu chấp hành dao động ổn định trong thời gian dài. "
        "Chỉ một chu kỳ mỗi giây cũng tương đương 2,5 triệu chu kỳ mòn đệm trong một tháng — "
        "lúc đó đệm đã mòn hoàn toàn.",
        "Không dùng vật liệu đệm có hệ số giãn nở nhiệt cao trong hệ thống có hơi nước hoặc "
        "chất lỏng nóng.",
        "Chiều sâu đệm hữu dụng tổng cộng phải luôn lớn hơn chiều dài hành trình của van; "
        "điều này tránh tạo rãnh trong lỗ đệm nếu thân van có một vết xước nhỏ.",
        "Đệm cho van quay có hiệu năng tốt hơn đệm cho van thân tịnh tiến, miễn là trục van "
        "quay được đỡ tốt để hấp thụ lực đẩy vuông góc của cơ cấu chấp hành hoặc biến dạng "
        "lệch tâm do khớp nối bị lệch.",
        "Sai lệch giữa thân van và thân cơ cấu chấp hành gây mòn và ma sát. Điều này có thể "
        "xảy ra khi giá đỡ bằng thép hoặc nhôm bị cong sau một cú rơi trong vận chuyển (giá "
        "bằng gang thì gãy), hoặc khi cơ cấu chấp hành nặng được lắp nằm ngang mà không có "
        "đỡ phù hợp.",
    ]))

    b.append(h2("Mức rò rỉ có thể mong đợi", "What leakage to expect"))
    b.append(p("Dù không đệm nào kín tuyệt đối, cần nhớ rằng tốc độ thẩm thấu qua chính thép "
               "đặc cũng đã nằm trong ngưỡng nhạy của máy phổ khối. Vì thế đừng đòi hỏi quá "
               "mức. Sau đây là vài ví dụ thực tế:"))
    b.append(ul([
        "Một đệm thân đường kính 5/16 inch dùng vòng Chevron TFE đặc (đã được nén sẵn) có "
        "độ rò rỉ khoảng 0,4 scc/min khi thử bằng khí 55 psi ở 70°F sau 100.000 chu kỳ hành "
        "trình đầy đủ, tức khoảng 550 scc/ngày, vào khoảng 2 × 10⁻⁵ kg/h và vẫn thấp hơn "
        "giới hạn 500 ppm. Cùng van đó rò 1 × 10⁻⁵ kg/h nước trong điều kiện tương tự. Các "
        "số liệu này đo trong phòng thí nghiệm, không tính ăn mòn hay bụi bẩn — những yếu "
        "tố làm rò rỉ tệ hơn ngoài thực tế.",
        "Một vòng điều khiển ổn định có rất nhiều lần 100.000 chu kỳ hành trình đầy đủ, và "
        "đệm có thể không cần thay trong vài năm. Ở trường hợp khác phải lập lịch bảo trì "
        "chặt chẽ. Có thể cân nhắc rằng mòn tương đương 100.000 chu kỳ × 1/2 inch hành trình "
        "bằng 625 ngày vận hành. Ngược lại, một van mất ổn định với chuyển động trung bình "
        "±0,30 in ở tốc độ hai chu kỳ mỗi phút tích lũy 1,05 triệu chu kỳ trong một năm. "
        "Điều đó cho thấy cần một vòng điều khiển và cơ cấu chấp hành ổn định.",
        "Khi mọi cách khác đều thất bại, hãy chỉ định van không đệm: van màng (kim loại hoặc "
        "elastomer), van kẹp (chỉ elastomer), van tay áo mềm (elastomer nhiệt dẻo, nhựa hoặc "
        "elastomer) hoặc van bịt kín bằng ống màng (bellows seal).",
    ]))

    b.append(h2("Đệm màng (bellows seals)", "Bellows seals"))
    b.append(p("Dùng đệm màng (Hình 24-1) là một cách tránh rò rỉ thân van và đáp ứng yêu cầu "
               "được EPA công nhận về tránh rò rỉ chất nguy hại (các cách khác gồm van màng "
               "và van kẹp). Đệm màng làm việc tốt nếu được bảo trì đúng cách và không bị "
               "quá tải. Luôn dùng kèm đệm dự phòng và một kết nối báo động (telltale) giữa "
               "đệm màng và đệm dự phòng, dẫn tới công tắc hoặc đồng hồ áp suất để báo cho "
               "người vận hành khi đệm màng hỏng. Đệm màng được cấp áp từ bên ngoài thường "
               "có khả năng chịu áp cao hơn."))
    b.append(fig(1, F.fig_f241()))
    b.append(p("Có thể dùng đệm màng thành đôi để tăng khả năng chống rò. Lưu ý: để tháo lắp "
               "đệm màng, cần một gioăng tốt tại giao diện giữa phần tĩnh của đệm màng và "
               "nắp van."))

    b.append(h3("Nguyên nhân hỏng đệm màng", "Causes of bellows failure"))
    b.append(h4("Quá áp (overpressurization)", "Overpressurization"))
    b.append(p("Thường xảy ra khi van có đệm màng bị đưa vào thử thủy lực ở áp lực đường ống "
               "mà đệm màng thông thường không thiết kế cho mức đó (cần hỏi nhà sản xuất). "
               "Các nguồn áp quá mức khác là sóng áp như \"búa nước\" do mở van đột ngột, "
               "hoặc sự giãn nở nhiệt của chất lỏng bị kẹt trong van và ống khi nhiệt độ "
               "môi trường thay đổi (có thể cần van an toàn)."))
    b.append(h4("Mỏi (fatigue)", "Fatigue"))
    b.append(p("Do quá nhiều chu kỳ đóng mở. Hầu hết đệm màng được đánh giá tối thiểu "
               "100.000 chu kỳ hành trình đầy đủ, tức nhiều năm làm việc tiết lưu bình "
               "thường (hai chu kỳ mở–đóng hoàn toàn mỗi ngày sẽ mất 137 năm để đạt 100.000 "
               "chu kỳ). Nhưng nếu dùng van ở chế độ đóng–mở một chu kỳ mỗi 5 phút, đạt "
               "200.000 chu kỳ trong khoảng một năm."))
    b.append(p("Mỏi cũng có thể tinh vi hơn. Ví dụ, đệm màng chịu dao động áp của bơm thể "
               "tích dương chạy 100 chu kỳ/phút có thể làm từng nếp gấp uốn một phần ở tốc "
               "độ một triệu chu kỳ mỗi tuần và cuối cùng gãy (khi đó cần bộ giảm xung phía "
               "sau bơm). Tín hiệu điều khiển điện tử dao động, không ổn định gửi tới cơ cấu "
               "chấp hành cũng gây hại tương tự bằng cách đặt thân van và đệm màng trước "
               "hàng triệu chu kỳ nhỏ."))
    b.append(h4("Hư hỏng cơ khí (mechanical damage)", "Mechanical damage"))
    b.append(p("Thường do lắp đặt hoặc bảo trì không đúng. Lỗi phổ biến nhất là xoắn đệm màng "
               "khi quay thân van. Thiết kế van tốt phải ngăn được hiện tượng này trong lúc "
               "lắp hoặc tháo van. Hãy nhớ: người ta thường chỉ đọc hướng dẫn sau khi sự cố "
               "đã xảy ra! Cũng cần cẩn thận khi tháo cơ cấu chấp hành: có thể vô tình đẩy "
               "hoặc kéo thân van (cùng đệm màng gắn liền) vượt quá hành trình bình thường."))
    b.append(p("Cấp áp cho bên ngoài đệm màng tăng khả năng chịu áp làm việc khoảng 50%, nhưng "
               "nắp giữ phải chịu áp và/hoặc chịu ăn mòn. Tăng áp cân bằng bên trong đệm màng "
               "cũng nâng mức chịu áp, nhưng chất lưu phải trơ; với chất lỏng cần có van an "
               "toàn đầy đủ để xả thể tích bị đẩy ra trong khi van chuyển động."))

    b.append(note("<b>Đặc điểm của nguyên bản.</b> Ảnh cắt đệm màng trong sách không có nhãn; "
                  "bản này vẽ lại thành sơ đồ vector và thêm các chú thích song ngữ lấy từ "
                  "văn bản chương. Các con số rò rỉ, số chu kỳ và mức áp được giữ nguyên như "
                  "bản in. Chương có 2 tài liệu tham khảo và 2 mục đọc thêm."))
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “Should a Control Valve Leak?” Instrument and Control Systems, "
        "August (1966).",
        "OSHA 1910.119-1992, Process Safety Management for Highly Hazardous Chemicals "
        "(Washington, DC: OSHA [Occupational Safety and Health Administration]).",
    ]))
    b.append(h3("Đọc thêm", "Additional reading"))
    b.append(ul([
        "IEC 60534-8-3 (2000), Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
        "H. D. Baumann and J. Kiesbauer, “A Method to Estimate Hydrodynamic Noise Produced "
        "in Valves by Submerged Turbulent and Cavitating Water Jets,” Noise Control "
        "Engineering Journal 52-2 (March–April 2004): 49–55.",
    ]))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 2011 Hans D. Baumann, xuất bản bởi ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(lead("A valve stem packing is one of the most important elements of a control "
                  "valve, yet one that is not fully understood. A worn packing causes external "
                  "leakage, but a tight packing can make the controller go unstable. The "
                  "combination of low friction and low stem leakage is what makes a good "
                  "packing — low leakage, not zero leakage, because there is no such thing "
                  "as zero leakage."))

    b.append(h2("Packing materials and installation practice", "Packing materials and installation practice"))
    b.append(p("In former times when asbestos was the standard packing material, packing boxes "
               "had lubricators whereby the maintenance people could inject grease into the "
               "packing, which not only reduced friction but also provided a high-viscosity "
               "interface between the packing bore and the stem exterior to improve "
               "sealability. Any maintenance department had to stock a variety of packing "
               "greases with varying viscosities (depending on service temperature) specially "
               "composed to resist corrosive attacks by certain fluids."))
    b.append(p("Teflon changed all that, and the all-Teflon V-ring or Chevron packing, preferred "
               "by some, and the tetrafluoroethylene (TFE)-lubricated asbestos packing, "
               "preferred by others, became the industry standard. Now, a variety of plastic "
               "materials, such as Kalrez, are also available. The TFE-graphite or TFE-Kevlar "
               "packings now current are made in the form of a split-ring and enable the "
               "emergency repair of a valve in the line by slipping one or two extra rings "
               "under the packing follower. The disadvantage was, and still is, that its "
               "tightness depends on the “feel” of the maintenance person. Many a carefully "
               "tuned process controller has gone unstable because of added stem friction "
               "(increased valve dead time) due to an over-tightened stem packing."))

    b.append(h2("Rules for avoiding trouble with valve stem packing",
                "Rules for avoiding trouble with valve stem packing"))
    b.append(ol([
        "Make sure the packing is tight before placing the valve in operation. Some "
        "manufacturers ship the valve with a loose packing flange or nut.",
        "If hot fluids are involved, retighten the packing after the valve has fully warmed "
        "up when first placed in service.",
        "During installation, do not rotate the actuator (e.g., to change positioner location) "
        "without loosening the packing before moving the actuator. Realize that the center of "
        "the stem and the center of the packing are not perfectly aligned. A loose packing "
        "will adapt to a change in the center.",
        "Do not allow the control loop or actuator to become unstable for a long time. "
        "Remember, even one cycle per second cyclic motion can translate into 2½ million "
        "cycles of packing wear in only one month! The packing is completely worn at that time.",
        "Do not use packing material that has a high coefficient of thermal expansion in a "
        "system containing steam or hot fluids.",
        "Total effective packing depth should always exceed the length of valve travel. This "
        "will avoid creating a groove inside the packing bore in case there is some “nick” on "
        "the surface of the valve stem.",
        "Packing for rotary valves is superior in performance to those for reciprocating stem "
        "valves as long as the rotary valve shaft is well supported to absorb the "
        "perpendicular actuator thrust or the off-center strain caused by a misaligned "
        "stem-coupled rotary actuator.",
        "Misalignment between the valve stem and the actuator stem causes wear and friction. "
        "This can happen when an actuator yoke, made from steel or aluminum, bends following "
        "a drop during shipment. Cast iron yokes cannot do this — they break. Misalignment can "
        "also happen when a heavy actuator is mounted in a horizontal position without proper "
        "support.",
    ]))

    b.append(h2("How much leakage to expect", "How much leakage to expect"))
    b.append(p("Although no packing is tight, remember that the permeation rate [1] through "
               "solid steel alone is already within the measurement sensitivity of mass "
               "spectrometers. So, do not expect too much. Here are some rough examples of "
               "what you can expect in the form of packing leakage:"))
    b.append(ul([
        "A typical 5/16-inch stem diameter packing with solid TFE Chevron rings (preloaded) "
        "exhibited a stem leakage when subjected to 55 psi air at 70°F of about 0.4 scc/min "
        "(standard cubic centimeters per minute) after 100,000 full travel cycles, or about "
        "550 scc/day, which is roughly 2 × 10⁻⁵ kg/h and is still below the 500 parts/million "
        "limit. The same valve exhibited a leakage of 1 × 10⁻⁵ kg/h of water under the same "
        "conditions. These test data are based on laboratory measurements and exclude "
        "environmental effects such as corrosion or dirt, which make things worse in real life.",
        "There are many 100,000 full travel cycles in a stable control loop situation, and a "
        "valve packing may not need to be replaced for several years. In other cases, a tight "
        "maintenance schedule must be instituted. You may want to consider that the packing "
        "wear equivalent to 100,000 × 1/2 in travel cycles is 625 days of operation. However, "
        "an unstable valve with average stem excursions of ±0.30 in at a rate of two cycles per "
        "minute accumulates 1.05 million cycles in a year! This demonstrates the need for a "
        "stable loop and a stable actuator.",
        "When all else fails, specify a packless valve such as a diaphragm valve (metal or "
        "elastomers), a pinch valve (elastomers only), a flexible sleeve valve (thermoplastic "
        "elastomer, plastic, or elastomer), or a bellows seal valve.",
    ]))

    b.append(h2("Bellows seals", "Bellows seals"))
    b.append(p("The use of bellows (see Figure 24-1) is one method for avoiding valve stem "
               "leakage and meeting Environmental Protection Agency–recognized avoidance of "
               "hazardous leakage from valves [2] (other methods include the use of diaphragm "
               "and pinch valves). Bellows seals work well if properly maintained and not "
               "overstressed. They should always be used with a backup packing and a telltale "
               "connection between the bellows seal and packing that leads to a pressure "
               "switch or pressure gauge to inform or alarm the operator in case of bellows "
               "failure. Bellows pressurized from the outside typically give higher pressure "
               "ratings."))
    b.append(fig(1, F.fig_f241()))
    b.append(p("Finally, double-walled bellows are available for added leakage protection. "
               "Note: Removability of the bellows requires a good gasket at the interface "
               "between the static portion of the bellows and the bonnet."))

    b.append(h3("Causes of bellows failure", "Causes of bellows failure"))
    b.append(h4("Overpressurization", "Overpressurization"))
    b.append(p("This is usually caused by subjecting the valve with bellows to hydrostatic line "
               "test pressure for which typical bellows are not designed (consult the "
               "manufacturer). Other sources of excess pressure are pressure waves such as "
               "“water hammer,” which are caused by a sudden valve opening or the thermal "
               "expansion of liquid trapped in the valve and pipe due to ambient temperature "
               "changes (a relief valve may be required)."))
    b.append(h4("Fatigue", "Fatigue"))
    b.append(p("This can be caused by excess valve cycles. Most bellows are rated for a minimum "
               "of 100,000 full travel cycles, which means many years of normal throttling "
               "service (two full open-to-closure cycles per day will yield 100,000 cycles in "
               "137 years!). However, if this valve is used in an on-off mode at one cycle "
               "every 5 min, 200,000 cycles are reached in about 1 year."))
    b.append(p("However, fatigue problems can be more subtle. For example, having the bellows "
               "subjected to the pressure fluctuations of a positive displacement pump "
               "operating at 100 cycles per minute can partly deflect the individual bellows "
               "convolutions at a rate of 1 million cycles per week and subsequently break the "
               "bellows (here a pulsation damper downstream of the pump is the answer). An "
               "unstable, cycling electronic control signal to the actuator can do the same "
               "damage by subjecting the stem and bellows to millions of minute cycles."))
    b.append(h4("Mechanical damage", "Mechanical damage"))
    b.append(p("This is usually caused by improper installation or maintenance. The most common "
               "problem is the twisting of the bellows when the valve stem is turned. A good "
               "valve design prevents the possibility of twisting the bellows during assembly "
               "or disassembly of the valve. Remember: Typically, instructions are read only "
               "after things have gone wrong! Also, be careful when removing the actuator; you "
               "might inadvertently push or pull the valve stem (with the attached bellows) "
               "above the normal travel distance."))
    b.append(p("Pressurization of the exterior of the bellows increases resistance to working "
               "pressure by about 50%. However, this requires the retaining bonnet to be "
               "pressure and/or corrosion-resistant. Adding balancing pressure inside the "
               "bellows will increase the pressure rating. However, the fluid has to be inert, "
               "and in the case of liquids, adequate relief must be provided to allow for "
               "venting displaced volume during valve travel."))

    b.append(note("<b>Source quirks.</b> The printed bellows cutaway has no labels; it has been "
                  "redrawn as a vector schematic with bilingual callouts taken from the "
                  "chapter text. All leakage figures, cycle counts and pressure statements "
                  "follow the printed source. The chapter has two references and two "
                  "additional-reading items."))
    b.append(h3("References", "References"))
    b.append(refs([
        "H. D. Baumann, “Should a Control Valve Leak?” Instrument and Control Systems, "
        "August (1966).",
        "OSHA 1910.119-1992, Process Safety Management for Highly Hazardous Chemicals "
        "(Washington, DC: OSHA [Occupational Safety and Health Administration]).",
    ]))
    b.append(h3("Additional reading", "Additional reading"))
    b.append(ul([
        "IEC 60534-8-3 (2000), Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
        "H. D. Baumann and J. Kiesbauer, “A Method to Estimate Hydrodynamic Noise Produced "
        "in Valves by Submerged Turbulent and Cavitating Water Jets,” Noise Control "
        "Engineering Journal 52-2 (March–April 2004): 49–55.",
    ]))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
