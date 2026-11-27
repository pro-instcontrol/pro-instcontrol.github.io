# -*- coding: utf-8 -*-
"""Chapter 7, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 164-166 (PDF pp. 185-187).

Covers the chapter opener (the italic first golden rule and the real-benefit
yardstick), the unnumbered opening subtitle, sections 7.1, 7.1.1, 7.1.2 and
7.2 including the four numbered approaches. Owns the chapter h2, the h3 for
the subtitle and for sections 7.1 and 7.2, and the h4 for 7.1.1 and 7.1.2.
Section 7.2.1 and everything after it belong to the next module. Prose only:
no figures, tables, equations, worked examples or reference list. The
integration shell owns the page shell, references and end matter. Wording,
standards designations, dates, footnote markers and printed quirks follow the
verified survey brief and the page renders, not the garbled PDF text layer.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note


def body_vi():
    b = []
    b.append(h2("7 — Triết lý thiết kế thiết bị điện dùng trong khí quyển nổ",
                "7 — Design philosophy for electrical apparatus for explosive "
                "atmospheres"))
    b.append(h3("Phương pháp tiếp cận chung và các tiêu chuẩn áp dụng",
                "General approach and applicable standards"))

    b.append(p("Ba chương trước đã thảo luận các khía cạnh khác nhau của việc "
               "phân loại khu vực nguy hiểm do sự hiện diện có thể có của các "
               "bầu khí quyển nổ được cấu thành từ không khí trộn với khí, hơi, "
               "sương mù chất lỏng hoặc bụi. Từ những phân tích đó, có thể xác "
               "định được những khu vực mà tại đó mối nguy hiểm tồn tại, cùng "
               "với mức độ nghiêm trọng của mối nguy hiểm ấy. Giờ đây cần giải "
               "quyết đến việc chế tạo thiết bị điện phải được lắp đặt trong "
               "những khu vực như vậy nhằm giảm thiểu nguy cơ hỏa hoạn hoặc "
               "nổ."))
    b.append(p("Khi làm điều đó, phải thừa nhận rằng dù thiết bị điện có được "
               "bảo vệ tốt đến đâu, vẫn luôn tồn tại rủi ro tồn dư nếu thiết bị "
               "được đặt tại những nơi có thể xuất hiện bầu khí quyển nổ. Vì "
               "mục đích đó, nguyên tắc vàng đầu tiên là: <i>Chỉ nên đặt vào, "
               "hoặc cho thông vào, các bầu khí quyển nổ những thiết bị điện "
               "thực sự cần thiết mà thôi.</i>"))
    b.append(note("<b>Lưu ý về nguyên tắc vàng được in nghiêng.</b> Bản in đưa "
                  "câu 'Only that electrical apparatus which is really "
                  "necessary should be placed in or communicate with "
                  "explosive atmospheres' thành một câu in nghiêng ngay sau "
                  "nhãn 'the first golden rule'. Bản dịch giữ nguyên cả nhãn "
                  "'nguyên tắc vàng đầu tiên' lẫn câu in nghiêng để phản ánh "
                  "đúng sự nhấn mạnh của bản in; không gộp câu này vào văn "
                  "bản thường."))
    b.append(p("Sự cần thiết phải đặt thiết bị điện trong bầu khí quyển nổ "
               "phải được xác định không chỉ trên các lý do an toàn mà còn "
               "trên các lý do vận hành và kinh tế. Tuy nhiên, thước đo cần "
               "luôn được áp dụng là lợi ích thực tế, và trừ khi có thể nhận "
               "ra lợi ích đó, thiết bị không nên được lắp đặt."))

    b.append(h3("7.1 Lịch sử", "7.1 History"))
    b.append(p("Việc chế tạo thiết bị điện được thiết kế riêng để sử dụng "
               "trong những khu vực mà nguy cơ nổ có thể phát sinh do các đám "
               "mây khí, hơi, sương mù chất lỏng hoặc bụi là một vấn đề được "
               "giải quyết lần đầu vào đầu thế kỷ hai mươi, và ban đầu nhắm "
               "vào ngành khai thác than. Việc giải quyết ban đầu này tập "
               "trung vào các vấn đề liên quan đến khí mê-tan (firedamp) và "
               "các vấn đề về bụi than."))

    b.append(h4("7.1.1 Nguy cơ từ khí, hơi và sương mù chất lỏng",
                "7.1.1 Gas, vapour and mist risks"))
    b.append(p("Các loại hình bảo vệ được hình dung cho khai thác than là "
               "những loại liên quan đến bảo vệ chống lại các đám mây khí, và "
               "mức độ bảo vệ tổng thể được tính đến là mức phù hợp với các "
               "khu vực hầm lò nơi người làm việc thường xuyên hiện diện. "
               "Người ta cũng giả định thiết bị sẽ được tắt khi phát hiện "
               "thấy khí. Dù các đợt phun khí firedamp đáng kể (tức là những "
               "đợt có thể bao trùm người và thiết bị trước khi thiết bị kịp "
               "tắt) tương đối hiếm, khó khăn trong việc thoát ra khỏi hầm lò "
               "lại rất đáng kể, nên một mức độ bảo vệ tương đối cao đã được "
               "áp dụng. Mức độ này về sau trở thành chuẩn mực cho Vùng 1 trên "
               "mặt đất. Vì vậy, những loại hình bảo vệ cũ nhất hiện vẫn được "
               "dùng cho thiết bị điện trong công nghiệp trên mặt đất chính "
               "là những loại phù hợp với Vùng 1."))
    b.append(p("Công nghiệp trên mặt đất ban đầu không xem xét việc lắp đặt "
               "thiết bị điện trong Vùng 0 — một tình huống mà những người "
               "làm việc với nguy cơ bụi cũng từng quen thuộc — và chỉ khi "
               "thiết bị đo đạc phát triển nhanh chóng thì nhu cầu này mới "
               "trở nên đáng kể. Cần nhớ rằng Vùng 0 thường xuất hiện bên "
               "trong các bình chế biến, nên cho đến khi nhu cầu giám sát tự "
               "động quá trình tăng lên cùng với sự phát triển của các thiết "
               "bị tinh vi hơn vào một giai đoạn muộn hơn, đã không có nhu "
               "cầu về bảo vệ phù hợp cho Vùng 0. Ngay cả hiện nay, nhìn chung "
               "chỉ cần đặt cảm biến thiết bị đo trong Vùng 0, và chỉ loại "
               "hình bảo vệ phù hợp với các thiết bị đó đã được phát triển "
               "cho Vùng 0."))
    b.append(p("Kịch bản Vùng 2 không tồn tại dưới lòng đất mà rất nhiều là "
               "hiện tượng của công nghiệp trên mặt đất. Ban đầu, người ta "
               "cho rằng thiết bị công nghiệp chất lượng tốt, không phát tia "
               "lửa cũng không nóng lên trong vận hành bình thường, là phù hợp "
               "cho Vùng 2, và rất ít công việc được thực hiện đối với Tiêu "
               "chuẩn dành cho thiết bị Vùng 2 cho đến tương đối gần đây; "
               "ngành công nghiệp khi đó hài lòng với một Hướng dẫn Lựa chọn "
               "Thiết bị Điện cho Vùng 2¹."))
    b.append(p("Cách tiếp cận đối với Vùng 2 ngày càng trở nên ít được chấp "
               "nhận hơn theo năm tháng, và dù vẫn có thể áp dụng được, hiện "
               "đã có các Tiêu chuẩn chế tạo thiết bị Vùng 2 và các Chỉ thị "
               "EU² đang làm cho cách tiếp cận cũ 'Selected Industrial "
               "Apparatus' (Thiết bị công nghiệp được chọn lọc) ngày càng ít "
               "được chấp nhận."))
    b.append(note("<b>Lưu ý về cụm từ 'Selected Industrial Apparatus'.</b> Bản "
                  "in đặt cụm từ 'Selected Industrial Apparatus' trong dấu "
                  "ngoặc kép để gọi tên cách tiếp cận cũ: lựa chọn thiết bị "
                  "công nghiệp thông thường cho Vùng 2 thay vì dùng thiết bị "
                  "chế tạo theo Tiêu chuẩn chống nổ. Cụm từ được giữ nguyên "
                  "bằng tiếng Anh trong cả hai bản dịch, không thay thế bằng "
                  "một từ tương đương thuần Việt, để phản ánh đúng thuật ngữ "
                  "in."))
    b.append(p("Những điều trên giải thích lý do tại sao, đối với nguy cơ từ "
               "khí và hơi, các Tiêu chuẩn dành cho thiết bị Vùng 1 hiện phát "
               "triển hơn hẳn so với các Tiêu chuẩn dành cho thiết bị Vùng 0 "
               "hoặc Vùng 2, dù nhiều công việc đang được tiến hành để khắc "
               "phục tình trạng này."))
    b.append(note("<b>Lưu ý về sự mất cân đối giữa các Tiêu chuẩn Vùng 1, Vùng "
                  "0 và Vùng 2.</b> Bản in nêu rằng các Tiêu chuẩn dành cho "
                  "thiết bị Vùng 1 'phát triển hơn hẳn' so với Vùng 0 hoặc "
                  "Vùng 2 'vào thời điểm hiện tại', đồng thời ghi nhận rằng "
                  "'nhiều công việc đang được tiến hành để khắc phục'. Đây là "
                  "nhận xét mang tính thời điểm của bản in năm 1998, không phải "
                  "phát biểu về tình trạng hiện nay; cách diễn đạt được giữ "
                  "nguyên, không cập nhật theo các Tiêu chuẩn sau này."))

    b.append(h4("7.1.2 Nguy cơ từ bụi", "7.1.2 Dust risks"))
    b.append(p("Một tình huống tương tự tồn tại đối với thiết bị dùng cho "
               "bụi, vì theo truyền thống người ta không coi là có thể chấp "
               "nhận được việc đặt thiết bị bên trong các bình chế biến bụi, "
               "v.v., và các Tiêu chuẩn cho loại thiết bị đó không thừa nhận "
               "Vùng bên trong³. Hiện đã có một hệ thống ba Vùng dành cho bụi, "
               "và người ta kỳ vọng rằng các Tiêu chuẩn chế tạo thiết bị trong "
               "lĩnh vực này cũng sẽ phát triển trong tương lai. (Đáng chú ý "
               "là một Quy phạm đã dùng hệ thống ba Vùng vào đầu những năm "
               "1970's⁴, và điều đó cho thấy một phần sự trì trệ trong việc "
               "phát triển ý tưởng trong lĩnh vực bầu khí quyển nổ.)"))
    b.append(note("<b>Lưu ý về vị trí của ký hiệu chú thích '1970's⁴'.</b> Bản "
                  "in đặt ký hiệu chú thích ⁴ ngay sau '1970's' (sau dấu "
                  "apostrophe và chữ s), chứ không đặt sau cụm 'one Code'. "
                  "Cụm in nguyên văn là 'in the early 1970's⁴'. Vị trí này "
                  "được giữ nguyên trong cả hai bản dịch; không dời ký hiệu "
                  "sang sau tên Quy phạm."))
    b.append(p("May mắn là hiện nay đã có một hệ thống ba Vùng quốc tế dành "
               "cho bụi, tương tự như hệ thống đã được dùng nhiều năm cho "
               "khí, hơi và sương mù chất lỏng, với các định nghĩa tương tự, "
               "và người ta hy vọng rằng giờ đây sẽ hình thành một sự song "
               "song nhất định trong cách giải quyết các vấn đề về bầu khí "
               "quyển nổ."))

    b.append(h3("7.2 Bảo vệ thiết bị điện chống lại nguy cơ từ khí, hơi và "
                "sương mù chất lỏng",
                "7.2 Protection of electrical apparatus for gas, vapour and "
                "mist risks"))
    b.append(p("Như đã lưu ý trước đó, các đám mây khí, hơi hoặc sương mù chất "
               "lỏng được giải phóng sẽ phân tán tương đối nhanh sau khi thoát "
               "ra và không tạo thành lớp trên thiết bị như bụi. Nếu thiết bị "
               "được bảo vệ chống lại sự ngưng tụ, đặc biệt trong trường hợp "
               "hơi hoặc sương mù chất lỏng nóng, thì việc chúng xâm nhập vào "
               "bên trong thiết bị không nhất thiết là một vấn đề, miễn là "
               "các bộ phận và mạch điện bên trong vỏ không phát tia lửa có "
               "khả năng bắt lửa hoặc trở nên quá nóng. Nếu chúng thực sự "
               "phát tia lửa có khả năng bắt lửa hoặc trở nên quá nóng, thì "
               "việc ngăn không cho chúng xâm nhập là điều đương nhiên phải "
               "làm, trừ khi kết quả của sự bắt lửa gây ra có thể được xử lý "
               "hiệu quả. Vì vậy có bốn phương pháp cơ bản có thể được áp dụng "
               "để ngăn ngừa sự bắt lửa không kiểm soát của các đám mây khí, "
               "hơi hoặc sương mù chất lỏng trộn với không khí."))
    b.append(p("1. Đám mây khí, hơi hoặc sương mù chất lỏng trộn với không khí "
               "có thể được loại trừ bằng các rào cản cơ học hoặc bằng các "
               "biện pháp tương đương khác."))
    b.append(p("2. Các bộ phận của mạch điện có thể được ngăn không phát tia "
               "lửa hoặc trở nên nóng đến mức đủ để bắt lửa đám mây khí, hơi "
               "hoặc sương mù chất lỏng trộn với không khí."))
    b.append(p("3. Đám mây khí, hơi hoặc sương mù chất lỏng trộn với không khí "
               "có thể được cho phép xâm nhập vào vỏ thiết bị và bắt lửa "
               "bên trong, nhưng sự lan truyền của vụ nổ ra bên ngoài vỏ có "
               "thể được ngăn chặn bằng một dạng dập tắt ngọn lửa nào đó."))
    b.append(p("4. Các bộ phận điện bên trong vỏ có thể được cho phép phát tia "
               "lửa, nhưng năng lượng cấp vào vỏ sẽ được giới hạn ở mức không "
               "đủ khả năng bắt lửa đám mây khí, hơi hoặc sương mù chất lỏng "
               "trộn với không khí."))
    b.append(p("Bốn cách trên là bốn phương pháp chính để hạn chế nguy cơ nổ "
               "ở mức có thể chấp nhận được. Rõ ràng, trong nhiều trường hợp "
               "chúng sẽ có ảnh hưởng đáng kể đến thiết kế của thiết bị, và "
               "không bao giờ được quên rằng sẽ luôn tồn tại những yêu cầu "
               "cơ bản đối với thiết bị tại một vị trí cụ thể, ngay cả khi "
               "không tính đến nguy cơ nổ (ví dụ, thiết bị đặt ngoài trời "
               "thường cần phải chống thời tiết). Độ tin cậy vận hành của "
               "thiết bị dựa vào những yêu cầu cơ bản này, vốn bảo vệ thiết "
               "bị khỏi môi trường chung, còn các kỹ thuật bảo vệ chống nổ "
               "áp dụng cho thiết bị thường dựa trên độ tin cậy vận hành của "
               "chính thiết bị đó. Điều này có nghĩa là, nói chung, các đặc "
               "tính bảo vệ chống nổ của thiết bị sẽ bổ sung cho, chứ không "
               "phải thay thế cho, các yêu cầu vận hành cơ bản, chẳng hạn "
               "như bảo vệ khỏi môi trường. Dùng bốn tiêu chí nêu trên, các "
               "loại hình bảo vệ cụ thể đã được phát triển qua nhiều năm và "
               "phần lớn được đề cập trong các Tiêu chuẩn chế tạo chi tiết."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("7 — Design philosophy for electrical apparatus for explosive "
                "atmospheres",
                "7 — Design philosophy for electrical apparatus for explosive "
                "atmospheres"))
    b.append(h3("General approach and applicable standards",
                "General approach and applicable standards"))

    b.append(p("The preceding three chapters discuss the various facets of "
               "the classification of areas made hazardous by the possible "
               "presence of explosive atmospheres of air mixed with gas, "
               "vapour, mist or dust. From these, it is possible to identify "
               "the areas where the hazard exists, together with the severity "
               "of the hazard. It now becomes necessary to address the "
               "construction of electrical equipment which should be "
               "installed in such areas to minimize the risk of fire or "
               "explosion."))
    b.append(p("In doing this, it has to be recognized that however well "
               "protected electrical equipment may be, there will always be "
               "residual risk if it is placed in areas where explosive "
               "atmospheres may occur. To this end, the first golden rule is: "
               "<i>Only that electrical apparatus which is really necessary "
               "should be placed in or communicate with explosive "
               "atmospheres.</i>"))
    b.append(note("<b>Note on the italic golden rule.</b> The print sets the "
                  "sentence 'Only that electrical apparatus which is really "
                  "necessary should be placed in or communicate with "
                  "explosive atmospheres.' in italics immediately after the "
                  "label 'the first golden rule'. Both the label and the "
                  "italic emphasis are preserved here so that the printed "
                  "emphasis is reflected; the sentence is not folded into the "
                  "surrounding ordinary text."))
    b.append(p("The necessity of placing electrical equipment in explosive "
               "atmospheres has to be determined not only on safety grounds "
               "but also on operational and economic grounds. However, the "
               "yardstick which should always be applied is that of real "
               "benefit and unless such benefit can be recognized the "
               "equipment should not be installed."))

    b.append(h3("7.1 History", "7.1 History"))
    b.append(p("The construction of electrical equipment specifically for use "
               "in areas where explosion risks might occur due to clouds of "
               "gas, vapour, mist or dust was a problem first addressed in the "
               "early part of the twentieth century and initially was aimed "
               "at the coal-mining industry. This initial addressing of the "
               "problem concentrated upon the problems associated with "
               "methane (firedamp) and the problems of coal dust."))

    b.append(h4("7.1.1 Gas, vapour and mist risks",
                "7.1.1 Gas, vapour and mist risks"))
    b.append(p("The types of protection envisaged for coal mining were those "
               "associated with protection against gas clouds and the levels "
               "of overall protection envisaged were those which were "
               "suitable for underground areas where men normally worked. "
               "They also presumed the equipment to be switched off if any "
               "gas was detected. Although it was relatively rare for "
               "significant outbursts of firedamp to occur (i.e., those which "
               "would engulf the men and the equipment before the latter "
               "could be switched off) the difficulty of escape from a mine "
               "was significant and a relatively high level of protection was "
               "adopted. This level later became the norm for Zone 1 above "
               "ground. Therefore the oldest types of protection currently "
               "used for electrical equipment in surface industry are those "
               "appropriate to Zone 1."))
    b.append(p("Surface industry did not, in the early days, consider the "
               "installation of electrical equipment in Zone 0, a situation "
               "contemporarily familiar to those dealing with dust hazards, "
               "and it was only with the rapid development of instrumentation "
               "that any such demand became significant. It must be remembered "
               "that Zone 0 generally occurs inside such things as process "
               "vessels and so, until the demand for automatic process "
               "monitoring increased with the development of sophisticated "
               "instruments at a much later date, there was no demand for "
               "protection suitable for Zone 0. Even now it is generally only "
               "necessary to site instrument sensors in Zone 0 and only the "
               "type of protection suitable for such devices has been "
               "developed for Zone 0."))
    b.append(p("The Zone 2 scenario did not exist underground and was very "
               "much a surface industry phenomenon. Initially, it was presumed "
               "that good quality industrial equipment, which did not spark "
               "or get hot in normal operation, was suitable for Zone 2 and "
               "little work was done on Standards for Zone 2 equipment until "
               "relatively recently; industry being content with a Guide to "
               "Selection of Electrical Equipment for Zone 2¹."))
    b.append(p("The approach to Zone 2 has become less and less acceptable "
               "over the years and although it is still possible to utilize "
               "it there are now construction Standards for Zone 2 equipment "
               "and EU Directives² are making the old 'Selected Industrial "
               "Apparatus' approach less and less acceptable."))
    b.append(note("<b>Note on 'Selected Industrial Apparatus'.</b> The print "
                  "places the phrase 'Selected Industrial Apparatus' in "
                  "quotation marks to name the older approach of selecting "
                  "ordinary industrial equipment for Zone 2 rather than using "
                  "equipment built to an explosion-protection construction "
                  "Standard. The phrase is retained verbatim in both language "
                  "bodies and is not replaced by a local equivalent."))
    b.append(p("The above explains why, in respect of gas and vapour risks, "
               "the Standards for Zone 1 equipment are much more developed "
               "than those for Zone 0 or Zone 2 equipment at present, although "
               "much is being done to correct this."))
    b.append(note("<b>Note on the Zone 1 / Zone 0 / Zone 2 Standards "
                  "imbalance.</b> The print states that the Standards for Zone "
                  "1 equipment are 'much more developed' than those for Zone 0 "
                  "or Zone 2 equipment 'at present', while adding that much is "
                  "being done to correct this. This is a point-in-time "
                  "observation from the 1998 source, not a statement of the "
                  "current position; the wording is preserved as printed and "
                  "has not been brought up to date against later Standards."))

    b.append(h4("7.1.2 Dust risks", "7.1.2 Dust risks"))
    b.append(p("A similar situation exists in respect of equipment for dusts "
               "as, historically it has not been considered as acceptable to "
               "put equipment inside dust-processing vessels, etc. and the "
               "Standards for such equipment did not recognize the interior "
               "Zone³. There is now a three-Zone system for dusts and it is "
               "expected that the equipment Standards in this area also will "
               "develop in the future. (It is worthy of note that one Code "
               "used a three-Zone system in the early 1970's⁴ and this gives "
               "some idea of the inertia in developing ideas in the explosive "
               "atmospheres field.)"))
    b.append(note("<b>Note on the position of the '1970's⁴' marker.</b> The "
                  "print places footnote marker ⁴ immediately after '1970's' "
                  "(after the apostrophe and the s), not after the words 'one "
                  "Code'. The printed phrase reads 'in the early 1970's⁴'. "
                  "That position is preserved verbatim in both language "
                  "bodies; the marker has not been moved after the name of the "
                  "Code."))
    b.append(p("Fortunately, there is now an international three-Zone system "
               "for dusts, which is similar to that used for many years for "
               "gases, vapours and mists, with similar definitions and it is "
               "hoped that some parallelism will now develop in addressing "
               "the problems of explosive atmospheres."))

    b.append(h3("7.2 Protection of electrical apparatus for gas, vapour and "
                "mist risks",
                "7.2 Protection of electrical apparatus for gas, vapour and "
                "mist risks"))
    b.append(p("As previously noted, released gas, vapour or mist clouds "
               "disperse relatively quickly after release and do not form "
               "layers on equipment as dust does. If equipment is protected "
               "against condensation, particularly in the case of hot vapours "
               "or mists, access of these to the inside of the equipment is "
               "not necessarily a problem, provided that the electrical "
               "components and circuits within the enclosure do not spark "
               "incendively or become excessively hot. If they do spark "
               "incendively or become excessively hot then their entry does, "
               "of course, have to be prevented unless the results of the "
               "resultant ignition can be effectively dealt with. There are "
               "thus four basic approaches which can be adopted to prevent "
               "uncontrolled ignitions of gas, vapour or mist and air clouds."))
    b.append(p("1. The gas, vapour or mist/air cloud can be excluded by "
               "mechanical barriers or other equivalent means."))
    b.append(p("2. The components of the electrical circuits can be prevented "
               "from sparking or becoming sufficiently hot to ignite the gas, "
               "vapour or mist/air cloud."))
    b.append(p("3. The gas, vapour or mist/air cloud can be permitted to enter "
               "the equipment enclosure and ignited, but the ensuing "
               "propagation of the explosion outside the enclosure can be "
               "prevented by some form of quenching."))
    b.append(p("4. The electrical components within the enclosure can be "
               "permitted to spark, but the energy fed to the enclosure will "
               "be limited to a level which is not capable of igniting the "
               "gas, vapour or mist/air cloud."))
    b.append(p("The above are the four main approaches to the limitation of "
               "explosion risk to an acceptable level. Clearly, they will, in "
               "many cases, have significant effect upon the design of the "
               "equipment and it should never be forgotten that there will be "
               "certain basic requirements for the equipment in a particular "
               "location, even if the explosion risk is not taken into account "
               "(e.g., equipment sited out of doors will normally need to be "
               "weather proof). The operational reliability of the equipment "
               "relies upon these basic requirements, which protect it from "
               "its general environment and the explosion protection "
               "techniques applied to the equipment are normally based upon "
               "its operational reliability. This means that, in general, the "
               "explosion protection features of equipment will be additional "
               "to, and not instead of, the basic operational requirements, "
               "such as protection from the environment. Using the four "
               "criteria described above, specific types of protection have "
               "been developed over the years and are mostly referred to in "
               "detailed construction Standards."))
    return "".join(b)
