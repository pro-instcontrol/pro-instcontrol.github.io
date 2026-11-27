# -*- coding: utf-8 -*-
"""Chapter 9, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 209-211 (PDF pp. 230-232).

Covers the unfoliated chapter opener (the three protection concepts and the
Directives), the opening of 9.1 Encapsulation - 'm' with its Standards,
9.1.1 ten exclusions, 9.1.2 Specification of the encapsulation and 9.1.3
Types of apparatus for encapsulation (ending at raw line 9970). Prose
only: no figures, tables, equations or reference list. The chapter shell
owns the chapter h2, references and end matter. Printed quirks are kept
in the English text (notably the (1998) opener year and the (1995) date of
BS/EN 50020), with notes; the Vietnamese text follows the intended dates.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig


def body_vi():
    b = []
    b.append(h3("Mở đầu chương", "Chapter opening"))

    b.append(p("<b>(BS/EN 50015 (1994))</b>"))
    b.append(p("<b>(BS/EN 50017 (1994))</b>"))
    b.append(p("<b>(BS 5501 phần 8 (1988))</b>"))
    b.append(note("<b>Lưu ý về năm in ở trang mở đầu.</b> Trang mở đầu in là "
                  "'BS 5501 phần 8 (1998)', nhưng tài liệu tham khảo 3 ghi "
                  "'BS 5501 ... Part 8 (1988)'. Bản tiếng Việt dùng năm 1988 "
                  "theo tài liệu tham khảo; bản tiếng Anh giữ nguyên năm in "
                  "1998. Cả hai năm đều được ghi nhận ở đây."))

    b.append(p("Đây là chương đầu tiên trong số tám chương đề cập đến các "
               "loại hình bảo vệ cụ thể (các kiểu bảo vệ). Chương này sẽ đề "
               "cập đến ba loại hình bảo vệ chưa được sử dụng phổ biến ở "
               "Anh, không được phát triển tại Anh, nhưng được bao gồm "
               "trong các loại hình bảo vệ thuộc phạm vi của Chỉ thị "
               "76/117/EEC¹ và 94/9/EC.² Mặc dù việc sử dụng các loại hình "
               "bảo vệ ‘o’ và ‘q’ hiện chỉ giới hạn ở Vùng 2 tại Anh, rất "
               "có thể chúng sẽ được phép sử dụng ở Vùng 1 khi Chỉ thị "
               "liên quan đến an toàn lao động cuối cùng trở thành luật. "
               "Ở các quốc gia mà chúng bắt nguồn, chúng đã được phép sử "
               "dụng ở Vùng 1."))

    b.append(h3("9.1 Bọc kín – ‘m’", "9.1 Encapsulation – ‘m’"))
    b.append(p("<b>BS 5501 phần 8 (1988)³</b>"))
    b.append(p("<b>(EN 50028 (1987))</b>"))
    b.append(p("Vấn đề đầu tiên cần giải quyết trong Tiêu chuẩn này là thực "
               "tế là nó vẫn còn ở ấn bản thứ nhất và liên quan đến ấn bản "
               "thứ nhất của EN 50014, tức là BS 5501, Phần 1 (1977).⁴ Tuy "
               "nhiên, nó lại loại trừ nhiều phần của Tiêu chuẩn đó, và "
               "giữa những phần còn lại với các phần tương ứng trong ấn "
               "bản thứ hai, BS/EN 50014 (1993),⁵ có rất ít khác biệt."))

    b.append(h4("9.1.1 Loại trừ khỏi BS 5501, Phần 1 (1977)",
                "9.1.1 Exclusions from BS 5501, Part 1 (1977)"))
    b.append(p("Các phần bị loại trừ là:"))
    b.append(p("1. Yêu cầu về nhiệt độ bề mặt tối đa đối với các linh kiện "
               "Ex-m."))
    b.append(p("2. Thời gian trễ khi mở vỏ bọc (rõ ràng là không thể mở lớp "
               "bọc kín mà không phá hủy nó)."))
    b.append(p("3. Định nghĩa về vật liệu làm vỏ bọc đối với vỏ bọc phi kim "
               "loại (bọc kín, nói một cách chặt chẽ, không phải là vỏ bọc "
               "phi kim loại dù về bản chất là phi kim loại)."))
    b.append(p("4. Bọc kín không bắt buộc phải được gán chỉ số nhiệt độ vì, "
               "dù là phi kim loại, nó không phải là nhựa như được định "
               "nghĩa trong BS 5501, Phần 1 (1977). Tuy nhiên, hợp chất "
               "đóng gói vẫn phải vượt qua các phép thử độ bền nhiệt do "
               "Tiêu chuẩn đó quy định."))
    b.append(p("5. Các yêu cầu về lỗ ren trong vỏ bọc bằng nhựa không áp "
               "dụng cho bọc kín, vì không có phần nào của hợp chất đóng "
               "gói có thể tháo rời dễ dàng mà không làm phá hủy hợp chất "
               "đó."))
    b.append(p("6. Vì không có bộ phận nào định được tháo ra nên các yêu "
               "cầu về liên khóa bị loại trừ, cùng với các yêu cầu về chốt "
               "vít."))
    b.append(p("7. Các yêu cầu về đầu vào cho cáp và ống dẫn bị loại trừ vì "
               "trong loại hình bảo vệ này, cáp được bịt kín trong hợp "
               "chất đóng gói."))
    b.append(p("8. Các yêu cầu về thiết bị đóng cắt và cầu chì cũng bị loại "
               "trừ vì chúng chủ yếu đề cập đến việc ngăn ngừa tiếp cận và "
               "không thể tiếp cận khi đã được bọc kín."))
    b.append(p("9. Nhãn cảnh báo cho đèn chiếu sáng cũng không cần thiết vì "
               "đèn cũng không thể mở được khi đã bọc kín."))
    b.append(p("10. Một nhóm các phép thử bị loại trừ như sau:"))
    b.append(p("(a) không cần thử va đập các linh kiện Ex ‘m’;"))
    b.append(p("(b) các phép thử về cấp độ bảo vệ của vỏ bọc không liên "
               "quan;"))
    b.append(p("(c) các phép thử trong hỗn hợp nổ không liên quan vì hỗn hợp "
               "nổ không tiếp cận được với các mạch điện;"))
    b.append(p("(d) các phép thử về kẹp cáp không cần thiết vì đầu cáp được "
               "bịt kín trong hợp chất đóng gói."))
    b.append(p("BS 5501, Phần 8 (1988) cũng chứa các định nghĩa bổ sung cho "
               "những định nghĩa trong BS 5501, Phần 1 (1977)⁴ và BS/EN "
               "50014 (1993).⁵ Chúng sẽ được đưa vào danh sách các định "
               "nghĩa ở cuối sách này."))

    b.append(h4("9.1.2 Quy định cụ thể về lớp bọc kín",
                "9.1.2 Specification of the encapsulation"))
    b.append(p("Hợp chất dùng để bọc kín phải được xác định đầy đủ, bao gồm "
               "vật liệu chính xác với chi tiết về chất độn, các phụ gia "
               "khác và bất kỳ xử lý bề mặt nào được thực hiện sau khi bọc "
               "kín (ví dụ: sơn phủ). Phạm vi nhiệt độ của nó cần được xác "
               "định cùng với nhiệt độ làm việc liên tục tối đa (có thể "
               "cao hơn giới hạn trên của phạm vi vì phạm vi nhiệt độ là "
               "phạm vi mà trong đó vật liệu đáp ứng BS 5501, Phần 8 "
               "(1988)³). Sẽ rất hữu ích nếu có thể dùng một vật liệu bọc "
               "kín có số tham chiếu IEC."))
    b.append(p("Hợp chất đóng gói cũng được thử để xác nhận đặc tính cách "
               "điện và khả năng chống hút ẩm, trong đó phép thử sau chỉ "
               "được quy định là"))
    b.append(p("cần thiết nếu thiết bị được bọc kín dự định dùng trong môi "
               "trường ẩm. Trên thực tế, phép thử hút ẩm sẽ là cần thiết "
               "trong mọi trường hợp vì các nhà sản xuất sẽ thấy những hạn "
               "chế chỉ dùng trong môi trường khô là rất hạn chế cho mục "
               "đích sử dụng chung."))
    b.append(p("Cả hai phép thử đều cần các đĩa hợp chất đóng gói có đường "
               "kính 50 mm và dày 3 mm. Đối với phép thử độ bền điện, đĩa "
               "có hai điện cực đường kính 30 mm đặt ở giữa, mỗi điện cực ở "
               "một mặt. Sau đó đĩa được nung nóng đến nhiệt độ bằng nhiệt "
               "độ tối đa của phạm vi làm việc đã quy định và đặt 4000 V ở "
               "tần số danh định 50 Hz giữa hai điện cực. Bất kỳ sự phóng "
               "điện bề mặt hay sự phá hủy cách điện nào trong vòng 5 phút "
               "có nghĩa là lớp bọc kín không phù hợp để sử dụng cùng với "
               "BS 5501, Phần 8³ (1988)."))
    b.append(p("Đối với phép thử hút ẩm, các mẫu khô được cân rồi ngâm "
               "trong nước máy ở nhiệt độ phòng thí nghiệm (23 °C) trong "
               "24 giờ. Sau khi làm khô và cân lại, trọng lượng không được "
               "tăng quá 1 phần trăm."))
    b.append(p("Bọc kín có thể cứng hoặc mềm nhưng trong trường hợp sau, rất "
               "có thể nó cần được đặt trong một khuôn tạo thành một bộ "
               "phận của thiết bị."))

    b.append(h4("9.1.3 Các loại thiết bị dùng cho bọc kín",
                "9.1.3 Types of apparatus for encapsulation"))
    b.append(p("Xem xét các yêu cầu của BS 5501, Phần 8³ (1988) dẫn ngay "
               "đến kết luận rằng khái niệm này chỉ dành cho thiết bị điện "
               "và thiết bị đo ‘dòng nhẹ’."))
    b.append(p("Mặc dù Tiêu chuẩn chỉ giới hạn cụ thể thiết bị ở mức vận "
               "hành dưới 11 kV, nó cũng nêu rằng thiết bị phải có khả năng "
               "hoạt động trong các điều khoản của Tiêu chuẩn với nguồn "
               "cung cấp có khả năng dòng dự kiến 4000 A. Dòng dự kiến này "
               "điển hình cho các yêu cầu đã được đặt ra đối với thiết bị "
               "đo dùng điện lưới trong loại hình bảo vệ theo BS 5501, "
               "Phần 7 (1977).⁶ Yêu cầu này đã được giảm xuống 1500 A trong "
               "BS/EN 50020 (1994)⁷ (ấn bản thứ hai của Tiêu chuẩn Bảo vệ "
               "nội tại) vì việc sử dụng cầu chì IEC tiêu chuẩn theo "
               "BS/EN 60127 (1991), các Phần 1, 2 và 3,⁸ trong đó xác định "
               "và đề cập đến cầu chì thu nhỏ. Như vậy, yêu cầu này điển "
               "hình cho một yêu cầu được áp dụng cho thiết bị đo và thiết "
               "bị điện công suất thấp."))
    b.append(note("<b>Lưu ý về năm của BS/EN 50020.</b> Văn bản in ghi "
                  "'BS/EN 50020 (1995)⁷', trong khi tài liệu tham khảo 7 "
                  "ghi 'BS/EN 50020 (1994)'. Bản tiếng Việt dùng năm theo "
                  "tài liệu tham khảo; bản tiếng Anh giữ nguyên năm in "
                  "1995."))
    b.append(p("Rất khó có khả năng thiết bị đóng cắt có thể đáp ứng giới "
               "hạn dòng dự kiến nêu trên, hoặc mức 4000 A quy định trong "
               "BS 5501, Phần 8 (1988) và, dù sao đi nữa, người ta cũng "
               "không cho rằng thiết bị đóng cắt phải bị phá hủy để tiếp "
               "cận là kinh tế."))
    b.append(p("Đèn chiếu sáng phải bị phá hủy để thay bóng đèn hoặc ống "
               "đèn sẽ không kinh tế và chỉ những đèn điện áp thấp nhỏ "
               "trong những thiết bị như bộ báo hiệu (annunciator) mới có "
               "khả năng phù hợp để bảo vệ theo loại hình này."))
    b.append(p("Mặc dù Tiêu chuẩn có chứa các yêu cầu về bọc kín cuộn dây "
               "stato của máy quay, các lực từ giãn (magnetostrictive) "
               "liên quan không thuận lợi cho việc áp dụng loại hình bảo "
               "vệ này vào máy quay có kích thước đáng kể, và các kỹ thuật "
               "đã được áp dụng từ trước đây cho thấy là đủ."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("Chapter opening", "Chapter opening"))

    b.append(p("<b>(BS/EN 50015 (1994))</b>"))
    b.append(p("<b>(BS/EN 50017 (1994))</b>"))
    b.append(p("<b>(BS 5501 part 8 (1998))</b>"))
    b.append(note("<b>Note on the printed year on the opener.</b> The chapter "
                  "opener prints 'BS 5501 part 8 (1998)', whereas reference 3 "
                  "gives 'BS 5501 ... Part 8 (1988)'. The English text retains "
                  "the printed 1998; the Vietnamese text uses the 1988 date "
                  "of reference 3. Both dates are recorded here."))

    b.append(p("This is the first of eight chapters dealing with specific "
               "protection concepts (types of protection). It will deal with "
               "three types of protection which are not yet in common use in "
               "the UK, were not developed in the UK, but are included in the "
               "protection concepts covered by Directives 76/117/EEC¹ and "
               "94/9/EC.² Although the use of protection concepts ‘o’ and ‘q’ "
               "is currently limited to Zone 2 in the UK, it is very likely "
               "that they will be permitted in Zone 1 when the Directive "
               "concerned with safety at work eventually becomes law. They "
               "are permitted in Zone 1 in the countries from which they "
               "originated."))

    b.append(h3("9.1 Encapsulation – ‘m’", "9.1 Encapsulation – ‘m’"))
    b.append(p("<b>BS 5501 part 8 (1988)³</b>"))
    b.append(p("<b>(EN 50028 (1987))</b>"))
    b.append(p("The first matter which must be dealt with in this Standard is "
               "the fact that it still exists in its first edition and relates "
               "to the first edition of EN 50014 which is BS 5501, Part 1 "
               "(1977).⁴ It does, however, exclude many parts of that Standard "
               "and there is little difference between those that remain and "
               "their equivalents in the second edition, BS/EN 50014 (1993).⁵"))

    b.append(h4("9.1.1 Exclusions from BS 5501, Part 1 (1977)",
                "9.1.1 Exclusions from BS 5501, Part 1 (1977)"))
    b.append(p("The parts which are excluded are:"))
    b.append(p("1. Requirements for maximum surface temperature in respect of "
               "Ex-m components."))
    b.append(p("2. Time delays for opening of enclosures (obvious as it is not "
               "possible to open encapsulation without destroying it)."))
    b.append(p("3. Definition of enclosure material for non-metallic enclosures "
               "(encapsulation is not, strictly speaking, a non-metallic "
               "enclosure although non-metallic in substance)."))
    b.append(p("4. Encapsulation is not required to be given a temperature "
               "index as, although it is non-metallic, it is not a plastic as "
               "defined in BS 5501, Part 1 (1977). The encapsulant is, however, "
               "required to pass the thermal endurance tests prescribed by "
               "that Standard."))
    b.append(p("5. The requirements for threaded holes in plastics enclosures "
               "do not apply to encapsulation as there are no parts of the "
               "encapsulant which can readily be dismantled without destruction "
               "of the encapsulant."))
    b.append(p("6. Because no parts are intended for removal the requirements "
               "for interlocking are excluded, together with those for "
               "fasteners."))
    b.append(p("7. The requirements for cable and conduit entries are excluded "
               "as in this protection concept, the cable is sealed into the "
               "encapsulant."))
    b.append(p("8. The requirements for switchgear and fuses are also excluded "
               "as they mostly address the prevention of access and no access "
               "is possible when encapsulated."))
    b.append(p("9. The warning label for luminaires is also not necessary as "
               "they also cannot be opened if encapsulated."))
    b.append(p("10. A group of the tests is excluded as follows:"))
    b.append(p("(a) it is not necessary to impact test Ex ‘m’ components;"))
    b.append(p("(b) tests for degree of protection of enclosures are "
               "irrelevant;"))
    b.append(p("(c) tests in explosive mixtures are irrelevant as the explosive "
               "mixture does not have access to the electrical circuits;"))
    b.append(p("(d) tests for cable clamping are not necessary because the end "
               "of the cable is sealed in the encapsulant."))
    b.append(p("BS 5501, Part 8 (1988) also contains further definitions which "
               "supplement those in BS 5501, Part 1 (1977)⁴ and BS/EN 50014 "
               "(1993)⁵. These will be included in the list of definitions at "
               "the end of this book."))

    b.append(h4("9.1.2 Specification of the encapsulation",
                "9.1.2 Specification of the encapsulation"))
    b.append(p("The compound used for encapsulation must be fully defined "
               "including its exact material with detail of fillers, other "
               "additives and any surface treatment given after encapsulation "
               "(e.g., varnishing). Its temperature range needs to be defined "
               "together with its maximum continuous operating temperature "
               "(which may be higher than the upper range limit as the "
               "temperature range is the range through which the material "
               "satisfies BS 5501, Part 8 (1988)³). It is helpful if an "
               "encapsulating material with an IEC reference number can be "
               "used."))
    b.append(p("The encapsulant is also tested to confirm its insulating "
               "properties and its resistance to water absorption, the latter "
               "test only being specified as"))
    b.append(p("necessary if the encapsulated apparatus is intended for use in "
               "a moist environment. In reality the water absorption, test "
               "will be necessary in all cases as manufacturers would find "
               "the limitations to dry environments very restrictive for "
               "general usage purposes."))
    b.append(p("Both tests require discs of encapsulant of 50 mm diameter and "
               "3 mm thickness. For the electric strength test the disc has "
               "two 30 mm diameter electrodes placed centrally one on each "
               "side. The disc is then heated to a temperature equal to the "
               "maximum temperature of its specified operating range and 4000 "
               "V at nominally 50 Hz is applied between the electrodes. Any "
               "flashover or insulation breakdown within 5 minutes means that "
               "the encapsulation is not suitable for use in association with "
               "BS 5501, Part 8³ (1988)."))
    b.append(p("For the water absorption test, dry samples are weighed and "
               "then immersed in tap water at laboratory temperature (23 °C) "
               "for 24 hours. After drying and reweighing, the weight must not "
               "have increased by more than 1 per cent."))
    b.append(p("Encapsulation may be hard or soft but in the latter case it is "
               "likely that it would need to be in a mould which formed part "
               "of the apparatus."))

    b.append(h4("9.1.3 Types of apparatus for encapsulation",
                "9.1.3 Types of apparatus for encapsulation"))
    b.append(p("Examination of the requirements of BS 5501, Part 8³ (1988) "
               "leads immediately to the conclusion that the concept is "
               "intended for ‘light current’ electrical equipment and "
               "instrumentation only."))
    b.append(p("Although the Standard specifically only limits apparatus to "
               "that which operates below 11 kV, it also states that apparatus "
               "must be capable of operation within the terms of the Standard "
               "from a supply of 4000 A Prospective current capability. This "
               "prospective is typical of the requirements which were placed "
               "on mains-powered instrumentation in the protection concept in "
               "BS 5501, Part 7 (1977).⁶ This requirement was reduced to 1500 "
               "A in BS/EN 50020 (1995)⁷ (the second edition of the Intrinsic "
               "Safety Standard) because of the use of standard IEC fuses to "
               "BS/EN 60127, (1991) Parts 1, 2 and 3⁸ of which are identified "
               "and deal with miniature fuses. Thus, the requirement is "
               "typical of one which is applied to instrumentation and "
               "low-power electrical apparatus."))
    b.append(note("<b>Note on the year of BS/EN 50020.</b> The printed text "
                  "reads 'BS/EN 50020 (1995)⁷', whereas reference 7 gives "
                  "'BS/EN 50020 (1994)'. The English text retains the printed "
                  "1995; the Vietnamese text follows the reference."))
    b.append(p("It is highly unlikely that switchgear could satisfy the "
               "prospective current limits specified above, or the 4000 A "
               "specified in BS 5501, Part 8 (1988) and, in any event, it is "
               "not considered likely that switchgear which has to be "
               "destroyed to gain access would be economical."))
    b.append(p("Luminaires which have to be destroyed to change lamps or tubes "
               "would not be economical and only small low-voltage lamps in "
               "such things as annunciators are likely to be suitable for "
               "protection in accordance with this concept."))
    b.append(p("Although the Standard contains requirements for encapsulation "
               "of stator windings of rotating machines, the magnetostrictive "
               "forces involved do not lend the protection concept to rotating "
               "machines of significant size, and other more historically "
               "applied techniques are proving adequate."))
    return "".join(b)
