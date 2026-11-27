# -*- coding: utf-8 -*-
"""Chapter 9, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 220-224 (PDF pp. 241-245).

Covers 9.3.3 Electrical components and circuits with Tables 9.2 and 9.3 and
all their printed notes, 9.3.4 External connections, 9.3.5 Type testing and
the closing Temperature testing subsection. The chapter shell owns the
chapter h2, the reference list and all end matter; this module owns the two
powder-filling tables, obtained from mcmillan_tbl91_93. Printed quirks are
retained in the English text and flagged in notes rather than silently
corrected. This is an unofficial study translation; the source PDF is not
republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillan_tbl91_93 as T91


def body_vi():
    b = []
    b.append(h3("9.3.3 Linh kiện và mạch điện",
                "9.3.3 Electrical components and circuits"))
    b.append(p("Các linh kiện và mạch điện bên trong vật liệu điền đầy phải "
               "được cách ly với vỏ bọc thông qua vật liệu này ở những khoảng "
               "cách như trong Bảng 9.2 và Bảng 9.3, ngay cả khi điện áp phát "
               "sinh từ bất kỳ quá tải và điều kiện sự cố nào có thể xảy ra, "
               "chẳng hạn như ngắn mạch linh kiện, hở mạch và hỏng bo mạch in, "
               "tác động lên các mạch điện. Khi xem xét các điều kiện sự cố "
               "này, có thể áp dụng những hạn chế sau:"))
    b.append(p("– Máy biến áp, cuộn dây và các cuộn dây quấn tuân thủ "
               "BS/EN 50019¹⁰ (1994) thì không bị coi là chịu sự cố;"))
    b.append(note("<b>Lưu ý về năm công bố của BS/EN 50019¹⁰.</b> Nguyên bản "
                  "in 'BS/EN 50019¹⁰ (1993)' ở đây, trong khi tài liệu tham "
                  "khảo 10 ghi BS/EN 50019 (1994). Bản dịch tiếng Việt dùng "
                  "năm (1994) theo tài liệu tham khảo; bản tiếng Anh giữ nguyên "
                  "năm in (1993) kèm chú thích này."))
    b.append(p("– Máy biến áp tuân thủ 8.1 của BS/EN 50020 (1994)⁷, ngoại trừ "
               "máy biến áp loại 2a, không bị coi là chịu sự cố;"))
    b.append(table(T91.HEAD92_VI, T91.ROWS92, T91.CAPTION92_VI))
    b.append(note(T91.NOTE92_VI))
    b.append(p("– Các bộ ghép quang và rơ le được thiết kế để cách ly các mạch "
               "có điện áp chênh lệch ít nhất bằng 1,5 lần điện áp chênh lệch "
               "thực tế, thì không bị coi là chịu sự cố, miễn là điện áp được "
               "cách ly không vượt quá 1000 V đỉnh;"))
    b.append(p("– Tụ điện bằng màng nhựa, gốm và giấy không bị coi là chịu sự "
               "cố ngắn mạch, miễn là chúng không làm việc ở điện áp vượt quá "
               "hai phần ba điện áp danh định cực đại;"))
    b.append(p("– Điện trở loại màng và điện trở dây quấn (một lớp) chỉ hỏng "
               "theo hướng tăng điện trở."))
    b.append(p("Ngoài ra, các khoảng cách cách ly theo Bảng 9.3 không bị coi "
               "là chịu sự cố ngắn mạch."))
    b.append(p("Các linh kiện như rơ le được phép đặt bên trong vật liệu điền "
               "đầy, với điều kiện là chúng có vỏ bọc riêng chịu được các sự cố "
               "bên trong chúng và thể tích bên trong của chúng nhỏ hơn "
               "30 cm³; tuy nhiên, nếu thể tích bên trong lớn hơn 3 cm³ thì "
               "áp dụng mức tối thiểu 15 mm khi dùng Bảng 9.2. Yêu cầu này "
               "chấp nhận rằng khí quyển nổ có thể đi vào khoảng rỗng bên trong "
               "được tạo ra, nhưng một sự đánh lửa sẽ không gây hư hỏng cho "
               "thiết bị dẫn đến nguy hiểm và ngọn lửa của nó cũng sẽ bị vật "
               "liệu điền đầy dập tắt."))
    b.append(p("Vì khái niệm bảo vệ thừa nhận sự cố, nên thường sẽ cần một "
               "hình thức hạn chế nhiệt độ nào đó. Điều này có thể được bảo "
               "đảm"))
    b.append(table(T91.HEAD93_VI, T91.ROWS93, T91.CAPTION93_VI))
    b.append(note(T91.NOTE93_VI))
    b.append(p("bằng cầu chì theo BS/EN 60127⁸ hoặc IEC 269¹¹² bên trong vật "
               "liệu điền đầy, hoặc bằng các cầu dao nhiệt, miễn là cầu dao "
               "nhiệt không tự thiết lập lại."))
    b.append(p("Tiêu chuẩn cũng thảo luận về bất kỳ vật liệu cách điện nào có "
               "thể có giữa các bộ phận cấu thành của thiết bị và thành vỏ bọc "
               "trong khu vực được xác định là chỗ điền đầy theo Bảng 9.2 và, "
               "với ngoại lệ là lớp cách điện của dây dẫn đi ra khỏi vật liệu "
               "điền đầy, ví dụ để nối đến các phương tiện đấu nối và chính "
               "vật liệu điền đầy, đồng thời yêu cầu vật liệu đó không cháy "
               "trong hơn 60 giây sau khi rời ngọn lửa và không bị phá hủy quá "
               "60 mm chiều dài mẫu thử khi thử theo BS 2782, Phần 1 (1992).²⁸ "
               "Yêu cầu này áp dụng cho các bộ phận đỡ bằng nhựa và những thứ "
               "như bạc lót."))
    b.append(note("<b>Lưu ý về cách viện dẫn BS 2782²⁸.</b> Nguyên bản trích "
                  "'BS 2782, Part 1 (1992)²⁸', trong khi tài liệu tham khảo 28 "
                  "là BS 2782 (1992), Phương pháp 140A, về hành vi cháy của "
                  "mẫu thử nằm ngang và đứng khi tiếp xúc với nguồn đánh lửa "
                  "ngọn lửa nhỏ. Cách trích của nguyên bản được giữ nguyên."))
    b.append(p("Tập hợp các yêu cầu này khác rất nhiều so với những yêu cầu "
               "trong lần xuất bản đầu tiên của Tiêu chuẩn, BS 5501, Phần 4 "
               "(1977).²⁹ Trong Tiêu chuẩn đó có một thử nghiệm rất nghiêm "
               "ngặt để bảo đảm không thể truyền sự đánh lửa từ bên trong vỏ "
               "bọc ra ngoài; vật liệu điền đầy được yêu cầu có kích thước nhỏ "
               "hơn nhiều và khoảng hở giữa các dẫn điện bên trong vật liệu "
               "điền đầy lớn hơn nhiều. Lý do là các yêu cầu của BS/EN 50017 "
               "(1994)²⁶ giới hạn thiết bị được bảo vệ ở thiết bị làm việc dưới "
               "1000 V, 16 A và 1000 VA, một giới hạn không có trong phiên bản "
               "tiền nhiệm. Vì vậy, cách tiếp cận đã thay đổi đáng kể. Do đó, "
               "không nên dùng thiết bị nhồi bột theo BS 5501, Phần 4 (1977)²⁹ "
               "trong tương lai."))
    b.append(h3("9.3.4 Đấu nối bên ngoài", "9.3.4 External connections"))
    b.append(p("Bất kỳ phương tiện đấu nối nào cho các mạch bên ngoài đều không "
               "được nằm trong phạm vi của phương pháp nhồi bột, đặc biệt là "
               "vì vỏ bọc đã được bịt kín vĩnh viễn trong giai đoạn chế tạo. "
               "Do đó, cần phải bảo vệ các cọc đấu nối và các phương tiện "
               "tương tự bằng một khái niệm bảo vệ khác (ví dụ, BS/EN 50019 "
               "(1994)¹⁰)."))
    b.append(h3("9.3.5 Thử nghiệm kiểu", "9.3.5 Type testing"))
    b.append(p("Thử nghiệm cụ thể của loại thiết bị này chỉ giới hạn ở: thử áp "
               "lực vỏ bọc; thử tính dễ cháy của vật liệu; thử độ bền điện của "
               "vật liệu điền đầy; và thử nhiệt độ tối đa ở bên ngoài thiết bị."))
    b.append(h4("Thử áp lực vỏ bọc", "Pressure testing of the enclosure"))
    b.append(p("Vỏ bọc được chịu áp suất gấp 1,5 lần áp suất khí quyển trong "
               "1 phút mà không bị biến dạng vượt quá 0,5 mm."))
    b.append(h4("Thử tính dễ cháy của vật liệu vỏ bọc",
                "Flammability testing of enclosure material"))
    b.append(p("Thử nghiệm được thực hiện bằng ngọn lửa đốt khí Bunzen theo "
               "BS 2782²⁸ và không được dẫn đến chiều dài bị phá hủy trung "
               "bình vượt quá 6 cm, với thời gian cháy không vượt quá 60 giây "
               "sau khi rời ngọn lửa. Nếu không thể thực hiện thử nghiệm này "
               "thì BS/EN 50017²⁶ có các phương pháp thay thế."))
    b.append(h4("Thử độ bền điện", "Electric strength testing"))
    b.append(p("Dùng bố trí điện cực trong Hình 9.2, áp 1000 V dc. Ở nhiệt độ "
               "25 ± 2 °C và độ ẩm tương đối 45–55 phần trăm, dòng rò không "
               "được vượt quá 10⁻⁶ A."))
    b.append(h4("Thử nhiệt độ", "Temperature testing"))
    b.append(p("Nhiệt độ bề mặt tối đa của vỏ bọc phải được đo trong điều kiện "
               "đầy tải và gồm tất cả quá tải được công nhận. Khi thiết bị được "
               "bảo vệ bằng cầu chì, nhiệt độ được đo ở dòng gấp 1,7 lần dòng "
               "danh định của cầu chì. Đối với các thiết bị bảo vệ khác, dòng "
               "điện phải là dòng lớn nhất có thể chảy liên tục mà không "
               "tác động."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("9.3.3 Electrical components and circuits",
                "9.3.3 Electrical components and circuits"))
    b.append(p("The electrical components and circuits inside the filling are "
               "required to be separated from the enclosure through the "
               "material by the distances shown in Tables 9.2 and 9.3 even "
               "when the voltages are derived with any possible overloads and "
               "fault conditions, such as component short circuits, open "
               "circuits and printed circuit board failures, applied to the "
               "electrical circuits. In considering these fault conditions, "
               "the following limitations can be applied:"))
    b.append(p("– transformers, coils and windings complying with "
               "BS/EN 50019¹⁰ (1993) are not subject to fault;"))
    b.append(note("<b>Note on the publication year of BS/EN 50019¹⁰.</b> The "
                  "prose prints 'BS/EN 50019¹⁰ (1993)' here, whereas "
                  "reference 10 gives BS/EN 50019 (1994). The printed year is "
                  "retained in the English text with this note; the standard "
                  "concerned is the increased-safety 'e' Standard."))
    b.append(p("– transformers complying with 8.1 of BS/EN 50020 (1994),⁷ "
               "other than type 2a transformers, are not considered as "
               "subject to fault;"))
    b.append(table(T91.HEAD92_EN, T91.ROWS92, T91.CAPTION92_EN))
    b.append(note(T91.NOTE92_EN))
    b.append(p("– optocouplers and relays which are designed to separate "
               "circuits having at least 1.5 times the voltage differential "
               "which actually exists, are not subject to fault provided the "
               "voltage separated does not exceed 1000 V peak;"))
    b.append(p("– plastic foil, ceramic and paper capacitors are not "
               "considered as subject to short-circuit fault provided they do "
               "not operate at more than two thirds of their maximum rated "
               "voltage;"))
    b.append(p("– film type and wire wound (single layer) resistors will only "
               "fail to higher resistance."))
    b.append(p("In addition, separations in accordance with Table 9.3 are not "
               "considered as subject to short circuit failure."))
    b.append(p("Components such as relays are permitted within the filling "
               "material, provided they have their own enclosure which will "
               "withstand faults within them and their internal volume is "
               "less than 30 cm³, however, if the internal volume is more than "
               "3 cm³ a 15 mm minimum is applied when Table 9.2 is used. This "
               "requirement accepts that the explosive atmosphere can enter "
               "the inner void so produced, but an ignition will not cause "
               "damage to the apparatus which will produce danger and its "
               "flame will likewise be quenched by the filling material."))
    b.append(p("As the protection concept recognizes faults, then some form "
               "of temperature limitation is often going to be necessary. "
               "This can be provided"))
    b.append(table(T91.HEAD93_EN, T91.ROWS93, T91.CAPTION93_EN))
    b.append(note(T91.NOTE93_EN))
    b.append(p("by fuses to BS/EN 60127⁸ or IEC 269¹¹² within the filling, or "
               "thermal trips provided the latter are not self resetting."))
    b.append(p("The Standard also discusses any insulating materials which "
               "may be present between the component parts of the apparatus "
               "and the enclosure wall in the area defined as filled by "
               "Table 9.2 and, with the exception of the insulation of the "
               "wiring which exits the filling, for example, to connect to "
               "the connection facilities and the filling itself, and "
               "requires it to not burn for more than 60 seconds after "
               "removal of the flame and resist more than 60 mm of the test "
               "piece length being destroyed when tested in accordance with "
               "BS 2782, Part 1 (1992).²⁸ This requirement will apply to "
               "support members in plastic and such things as bushings."))
    b.append(note("<b>Note on the BS 2782²⁸ cross-reference.</b> The prose "
                  "cites 'BS 2782, Part 1 (1992)²⁸', whereas reference 28 is "
                  "BS 2782 (1992), Method 140A, on the burning behaviour of "
                  "horizontal and vertical specimens in contact with a "
                  "small-flame ignition source. The printed citation is "
                  "retained here."))
    b.append(p("This set of requirements is very different to those in the "
               "first edition of the Standard BS 5501, Part 4 (1977).²⁹ In "
               "that Standard a very severe test to ensure that ignition "
               "could not be transmitted from within the enclosure was "
               "included, filling materials were required to be much smaller "
               "in size, and clearances between electrical conductors within "
               "the filling were much larger. The reason for this is that the "
               "requirements of BS/EN 50017 (1994)²⁶ limit the apparatus "
               "protected to that which operates at less than 1000 V, 16 A "
               "and 1000 VA which limitation is not in its predecessor. The "
               "approach has, therefore, been significantly changed. For this "
               "reason, it is not recommended that powder-filled apparatus to "
               "BS 5501, Part 4 (1977)²⁹ is used in the future."))
    b.append(h3("9.3.4 External connections", "9.3.4 External connections"))
    b.append(p("Any connection facilities for external circuits cannot be "
               "such as to fall within the scope of powder filling, "
               "particularly as the filled enclosure is sealed permanently "
               "at the manufacturing stage. There will, therefore, be the "
               "need to protect terminals and similar facilities by another "
               "protection concept (e.g., BS/EN 50019 (1994)¹⁰)."))
    b.append(h3("9.3.5 Type testing", "9.3.5 Type testing"))
    b.append(p("The specific testing of this type of apparatus is limited to; "
               "pressure testing of the enclosure; flammability testing of "
               "its materials; electric-strength testing of the filling "
               "material; and maximum temperature testing of the outside of "
               "the apparatus."))
    b.append(h4("Pressure testing of the enclosure",
                "Pressure testing of the enclosure"))
    b.append(p("The enclosure is subjected to 1.5 times atmospheric pressure "
               "for 1 minute without deformation exceeding 0.5 mm."))
    b.append(h4("Flammability testing of enclosure material",
                "Flammability testing of enclosure material"))
    b.append(p("The test is carried out with a bunsen burner in accordance "
               "with BS 2782²⁸ and should not result in an average destroyed "
               "length of more than 6 cms with burning, not exceeding 60 "
               "seconds after removal of the flame. If this test is not "
               "possible alternatives are included in BS/EN 50017²⁶."))
    b.append(h4("Electric strength testing", "Electric strength testing"))
    b.append(p("Using the electrode arrangement in Fig. 9.2, 1000 V dc is "
               "applied. With the temperature at 25 ± 2 °C and relative "
               "humidity at 45–55 per cent, leakage current should not exceed "
               "10⁻⁶ A."))
    b.append(h4("Temperature testing", "Temperature testing"))
    b.append(p("The maximum surface temperature of the enclosure should be "
               "measured in full load conditions and including all recognized "
               "overloads. Where the apparatus is protected by fuses, the "
               "temperature will be measured at 1.7 times the fuse-rated "
               "current. For other protective devices the current should be "
               "the maximum which can continuously flow without operation."))
    return "".join(b)
