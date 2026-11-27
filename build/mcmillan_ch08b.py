# -*- coding: utf-8 -*-
"""Chapter 8, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 183-187 (PDF pp. 204-208).

Finishes the flameproof sub-grouping (MESG limits, the MIC/MESG relationship
and the historic comparison), owns Figure 8.1 and Table 8.1, then covers
surface-temperature classification, temperature classes T1-T6, the small-
component rules and Table 8.2. The chapter h2, the 19 printed references and
the end matter belong to the integration shell and are not emitted here.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig08 as F
import mcmillan_tbl81_82 as T81


def body_vi():
    b = []

    # --- printed p.183 (PDF 204): Figure 8.1 and the flameproof sub-groups --
    b.append(fig(1, F.fig_f801()))

    b.append(p("Phân nhóm IIB: Thiết bị sẽ không bắt lửa một khí quyển nổ xung "
               "quanh khi được chứa đầy và được bao quanh bởi hỗn hợp 37 phần "
               "trăm hydro trong không khí (tương ứng với MESG là 0.35 mm) ở "
               "áp suất khí quyển. Các khí, hơi và sương mù khi trộn với không "
               "khí sẽ được xếp vào phân nhóm IIB khi MESG của chúng được đo "
               "bằng phương pháp mô tả trong IEC 79-1A (xem Hình 8.1) nằm giữa "
               "0.5 mm và 0.9 mm. Hệ số an toàn được tạo ra bằng cách dùng một "
               "hỗn hợp thử nhạy hơn cho thiết bị."))
    b.append(p("Phân nhóm IIC: Việc thử thiết bị ở đây rất khác vì việc đạt "
               "được hệ số an toàn trên khí thử khó hơn. Hệ số an toàn đạt được "
               "bằng cách tăng các khe hở do nhà chế tạo quy định rồi thử với "
               "các hỗn hợp nhạy nhất của cả hydro lẫn acetylen với không khí. "
               "(Đó là 28 phần trăm hydro trong không khí và 7.5 phần trăm "
               "acetylen trong không khí.) Các khí, hơi và sương mù khi trộn "
               "với không khí sẽ được xếp vào phân nhóm IIC khi MESG của chúng "
               "được đo theo phương pháp mô tả trong IEC 79-1A (xem Hình 8.1) "
               "nhỏ hơn 0.5 mm. Trong trường hợp này, hệ số an toàn thường đạt "
               "được bằng cách mở rộng khe hở có xu hướng nhạy hơn đáng kể so "
               "với các hỗn hợp thử."))
    b.append(p("Một lần nữa, cũng như trong trường hợp bản chất an toàn nội "
               "tại, nhận định về IIC dựa trên thực tế là hydro và acetylen là "
               "hai loại khí nhạy nhất đã biết, và chỉ có thể tạo được các "
               "hỗn hợp nhạy hơn bằng cách bổ sung thêm oxy, điều này nằm "
               "ngoài phạm vi của Tiêu chuẩn này và đòi hỏi phải xử lý riêng."))

    # --- printed p.183-184 ------------------------------------------------
    b.append(p("May mắn thay, có một mối quan hệ giữa MIC và MESG, và để xếp "
               "một khí, hơi hoặc sương mù vào một phân nhóm cụ thể thì chỉ "
               "cần thực hiện một trong hai phép thử MIC hoặc MESG chứ không "
               "cần cả hai. Tuy nhiên, điều này không còn đúng ở các giới hạn "
               "trên và khi cần phải thực hiện cả hai. Trong những trường hợp "
               "đó, các quy định sau đây áp dụng: khi MIC nằm trong khoảng "
               "0.8–0.9 mm, MESG sẽ xác định phân nhóm; khi MIC nằm trong "
               "khoảng 0.45–0.5 mm, MESG sẽ xác định phân nhóm; khi MESG nằm "
               "trong khoảng 0.5–0.55 mm, MIC sẽ xác định phân nhóm."))
    b.append(p("Những tiêu chí này là cần thiết để bảo đảm rằng thông số nhạy "
               "nhất được dùng để xác định phân nhóm."))
    b.append(p("Để hỗ trợ việc phân nhóm các khí, hơi và sương mù chưa được "
               "thử, thường có thể nhận diện chúng là một trong một dãy vật "
               "liệu có cấu trúc tương tự, trong trường hợp đó rất có thể "
               "phân nhóm của chúng sẽ giống như các khí, hơi và sương mù "
               "khác trong các vật liệu tương tự có khối lượng phân tử thấp "
               "hơn. Tuy nhiên, trong mọi trường hợp, phải thận trọng với các "
               "vật liệu chưa được xếp vào phân nhóm để bảo đảm không có đặc "
               "điểm đặc biệt nào của vật liệu làm cho việc phân loại trở "
               "nên không phù hợp. Ví dụ, etyl nitrat sẽ tạo ra áp suất nổ "
               "vượt quá của bất kỳ vật liệu đã được phân loại nào. Không có "
               "bảo đảm rằng thiết bị chống nổ có thể chịu được một vụ nổ bên "
               "trong của vật liệu này, và cần có các biện pháp phòng ngừa "
               "đặc biệt."))
    b.append(p("Hệ thống phân nhóm hiện đang dùng đã được đặt nền tảng trên "
               "các hệ thống khác nhằm đạt được mục tiêu tương tự ở Vương "
               "quốc Anh và các quốc gia khác. Mối quan hệ đại khái giữa hệ "
               "thống hiện hành và các hệ thống lịch sử đó được cho trong "
               "Bảng 8.1."))

    # --- printed p.184: surface temperature classification -----------------
    b.append(h4("Phân loại nhiệt độ bề mặt", "Surface temperature classification"))
    b.append(p("Bất kỳ bề mặt không được bảo vệ nào mà khí quyển nổ có thể "
               "tiếp cận đều có thể gây bắt lửa. Điều này có nghĩa là trong "
               "khi đối với các khái niệm bảo vệ như vỏ bọc chống nổ hoặc cấp "
               "áp, chỉ nhiệt độ của vỏ bọc bên ngoài là quan trọng. Khi xét "
               "đến bản chất an toàn nội tại và an toàn tăng cường, nhiệt độ "
               "của các bộ phận bên trong trở nên quan trọng vì khí quyển nổ "
               "có thể tiếp cận chúng và không có phương pháp nào ngăn ngừa "
               "sự truyền ngọn lửa. Đối với mọi bề mặt của thiết bị mà sự bắt "
               "lửa gây ra sẽ dẫn đến cháy không kiểm soát, dù bên trong hay "
               "chỉ trên vỏ bọc ngoài của thiết bị, cần xác định nhiệt độ đạt "
               "được trong trường hợp vận hành xấu nhất, bao gồm cả sự thay "
               "đổi nguồn cấp (trong trường hợp thiết bị cấp nguồn từ lưới "
               "điện thường là cộng hoặc trừ 10 phần trăm.)"))
    b.append(p("Điều này được thực hiện bằng cách phân loại nhiệt độ thiết bị "
               "thành sáu cấp nhiệt độ dựa trên nhiệt độ tối đa mà thiết bị "
               "đạt được trong điều kiện vận hành thiết kế cực đoan (có hệ số "
               "an toàn), đồng thời liên kết các khí, hơi và sương mù với các "
               "cấp đó dựa trên nhiệt độ bắt lửa của chúng, và gán cho thiết "
               "bị một cấp phân loại nhiệt độ. Do khó khăn lớn hơn trong việc "
               "gây bắt lửa nhiệt vì ảnh hưởng của chuyển động không khí, "
               "v.v., hệ số an toàn trong trường hợp này nhỏ hơn hệ số thường "
               "dùng để phân nhóm. Các cấp nhiệt độ như sau."))

    # --- printed p.185: Table 8.1, then classes T1 and T2 -------------------
    b.append(table(T81.HEAD81_VI, T81.ROWS81, T81.CAPTION81_VI))
    b.append(note(T81.NOTE81_VI))
    b.append(note("<b>Lưu ý về chữ 'european' viết thường trong tiêu đề Bảng "
                  "8.1.</b> Bản in viết 'Current european grouping system' với "
                  "chữ 'european' viết thường; cách viết này được giữ nguyên "
                  "trong bản dịch tiếng Anh và không sửa thành 'European'."))

    b.append(p("<b>T1</b>"))
    b.append(p("Đối với T1, nhiệt độ tối đa của thiết bị không được vượt quá "
               "440 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 400 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trên 450 °C."))
    b.append(p("<b>T2</b>"))
    b.append(p("Đối với T2, nhiệt độ tối đa của thiết bị không được vượt quá "
               "290 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 250 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trong khoảng 300 °C và "
               "450 °C."))

    # --- printed p.186: classes T3-T6, self-heating, small components -------
    b.append(p("<b>T3</b>"))
    b.append(p("Đối với T3, nhiệt độ tối đa của thiết bị không được vượt quá "
               "195 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 155 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trong khoảng 200 °C và "
               "300 °C."))
    b.append(p("<b>T4</b>"))
    b.append(p("Đối với T4, nhiệt độ tối đa của thiết bị không được vượt quá "
               "130 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 90 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trong khoảng 135 °C và "
               "200 °C."))
    b.append(p("<b>T5</b>"))
    b.append(p("Đối với T5, nhiệt độ tối đa của thiết bị không được vượt quá "
               "95 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 55 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trong khoảng 100 °C và "
               "135 °C."))
    b.append(p("<b>T6</b>"))
    b.append(p("Đối với T6, nhiệt độ tối đa của thiết bị không được vượt quá "
               "80 °C. (Vì việc phân loại nhiệt độ thường được thực hiện ở "
               "nhiệt độ môi trường 40 °C, điều này thường có nghĩa là độ tăng "
               "do tự nóng là 40 °C.) Các khí, hơi và sương mù thuộc cấp "
               "nhiệt độ này sẽ có nhiệt độ bắt lửa trong khoảng 85 °C và "
               "100 °C."))
    b.append(p("Như đã nêu, độ tự tăng nhiệt của thiết bị được phép trong mọi "
               "trường hợp phụ thuộc vào nhiệt độ môi trường mà tại đó việc "
               "phân loại nhiệt độ được thực hiện. Nếu một thiết bị được phân "
               "loại là T3 ở nhiệt độ môi trường 100 °C thì độ tự nóng được "
               "phép sẽ giảm xuống còn 95 °C, vì nhiệt độ tối đa tổng thể "
               "phải giữ nguyên."))
    b.append(p("Người ta cũng thừa nhận rằng các bộ phận nhỏ có thể vượt quá "
               "nhiệt độ bắt lửa của một khí, hơi hoặc sương mù cụ thể mà "
               "không gây bắt lửa, và điều này đã được chứng minh là đúng. "
               "Nhìn chung, sự khác biệt này phụ thuộc vào các yếu tố như khả "
               "năng đối lưu của khí, hơi hoặc sương mù cụ thể và cấu hình "
               "của bề mặt nóng. Vì lý do này, không có sự nới lỏng chung nào "
               "(ngoại trừ trong trường hợp bản chất an toàn nội tại, xem "
               "Chương 13) và từng loại bộ phận nhỏ phải được xử lý riêng. Để "
               "làm điều đó, cần xác định nhiệt độ mà tại đó bề mặt đang xét "
               "thực sự bắt lửa một khí đại diện cho khí nhạy nhất trong cấp "
               "nhiệt độ, rồi bảo đảm rằng bề mặt không vượt quá các nhiệt độ "
               "sau đây khi sử dụng:"))

    # --- printed p.187: in-service limits, Table 8.2 -----------------------
    b.append(p("T1 – nhiệt độ bắt lửa trừ 50 °C<br>"
               "T2 – nhiệt độ bắt lửa trừ 50 °C<br>"
               "T3 – nhiệt độ bắt lửa trừ 50 °C<br>"
               "T4 – nhiệt độ bắt lửa trừ 25 °C<br>"
               "T5 – nhiệt độ bắt lửa trừ 25 °C<br>"
               "T6 – nhiệt độ bắt lửa trừ 25 °C"))
    b.append(p("Đã từng tồn tại một hệ thống phân loại nhiệt độ có khái niệm "
               "tương tự ở Đức, và mối quan hệ giữa hệ thống đó với hệ thống "
               "hiện hành được cho trong Bảng 8.2. Tại Hoa Kỳ, ban đầu có một "
               "hệ thống trong đó phân loại thiết bị (tương đương với phân "
               "nhóm của họ) xác định nhiệt độ tối đa của thiết bị (xem Bảng "
               "8.1), nhưng trong những năm gần đây họ đã áp dụng một biến thể "
               "của hệ thống phân loại nhiệt độ châu Âu (xem Bảng 8.2)."))
    b.append(table(T81.HEAD82_VI, T81.ROWS82, T81.CAPTION82_VI))
    b.append(note(T81.NOTE82_VI))
    return "".join(b)


def body_en():
    b = []

    # --- printed p.183 (PDF 204): Figure 8.1 and the flameproof sub-groups --
    b.append(fig(1, F.fig_f801()))

    b.append(p("Sub-group IIB: Apparatus will not ignite a surrounding "
               "explosive atmosphere when filled with, and surrounded by, a "
               "mixture of 37 per cent hydrogen in air (equivalent to an MESG "
               "of 0.35 mm) at atmospheric pressure. Gases, vapours and mists "
               "in mixture with air will be associated with sub-group IIB "
               "when their MESG is measured by the method described in IEC "
               "79-1A (see Fig. 8.1) is between 0.5 mm and 0.9 mm. A safety "
               "factor is produced by using a more sensitive test gas for the "
               "apparatus."))
    b.append(p("Sub-group IIC: Apparatus testing is very different here as "
               "achieving a safety factor on the test gas is more difficult. "
               "The safety factor is achieved by increasing the gaps specified "
               "by the manufacturer and then testing with the most sensitive "
               "mixtures of both hydrogen and acetylene with air. (These are "
               "28 per cent hydrogen in air and 7.5 per cent acetylene in "
               "air.) Gases, vapours and mists in mixture with air will be "
               "associated with sub-group IIC when their MESG is measured in "
               "accordance with the method described in IEC 79-1A (see Fig. "
               "8.1) at less than 0.5 mm. In this case, the safety factor "
               "normally achieved by enlargement of gaps is rather more "
               "sensitive than test mixtures."))
    b.append(p("Once again, as in the case of intrinsic safety the IIC "
               "statement is based upon the fact that hydrogen and acetylene "
               "are the two most sensitive gases known and more sensitive "
               "mixtures can only be achieved by adding further oxygen, which "
               "is outside the scope of this Standard and requires special "
               "treatment."))

    # --- printed p.183-184 ------------------------------------------------
    b.append(p("Fortunately there is a relationship between MIC and MESG and "
               "to allocate a gas, vapour or mist to a particular sub-group it "
               "is only necessary to carry out either an MIC or an MESG test "
               "and not both. This ceases to be true, however, at the upper "
               "limits and where both need to be carried out. In such cases "
               "the following will be true: where MIC is between 0.8–0.9 mm, "
               "MESG will determine the sub-group; where MIC is between "
               "0.45–0.5 mm, MESG will determine the sub-group; where MESG is "
               "between 0.5–0.55 mm, the MIC will determine the sub-group."))
    b.append(p("These criteria are necessary to ensure that the most sensitive "
               "parameter is used to determine the sub-group."))
    b.append(p("To assist in sub-grouping gases, vapours and mists which have "
               "not been tested, it is often possible to identify them as one "
               "of a range of materials of similar structure, in which case "
               "it is highly likely that their sub-group will be the same as "
               "other gases, vapours and mists within similar materials which "
               "have a lower molecular weight. In all cases, however, care "
               "must be taken with materials not already allocated to a "
               "sub-group to ensure that no special feature of the material "
               "may make allocation unacceptable. Ethyl nitrate, for instance, "
               "will produce an explosion pressure in excess of any allocated "
               "material. There is no guarantee that flameproof apparatus "
               "will withstand an internal explosion of this material and "
               "special precautions are necessary."))
    b.append(p("The system for sub-grouping now used was preceded by different "
               "systems intended to achieve the same objective in the UK and "
               "other countries. The approximate relationship between the "
               "current system and these historic systems is given in Table "
               "8.1."))

    # --- printed p.184: surface temperature classification -----------------
    b.append(h4("Surface temperature classification",
                "Surface temperature classification"))
    b.append(p("Any unprotected surface to which an explosive atmosphere has "
               "access may cause ignition. This means that while for such "
               "protection concepts as flameproof enclosure or pressurization, "
               "only the external enclosure temperature is important. When "
               "intrinsic safety and increased safety are considered, the "
               "temperature of internal components becomes important as the "
               "explosive atmosphere has access to them and there is no method "
               "of preventing flame transmission. For all apparatus surfaces "
               "where any ignition caused would produce uncontrolled burning, "
               "be they inside or merely on the outer enclosure of the "
               "apparatus, it is necessary to identify the attained temperature "
               "in the worst case of operation, which includes supply "
               "variation (which in the case of mains-fed apparatus is "
               "normally plus or minus 10 per cent.)"))
    b.append(p("This is done by temperature classifying apparatus into six "
               "temperature classes on the basis of the maximum temperature it "
               "reaches in the extreme of its designed operating conditions "
               "(with a safety factor) and associating gases, vapours and "
               "mists with those classes on the basis of their ignition "
               "temperatures, and giving apparatus a temperature "
               "classification. Because of the greater difficulty in causing "
               "thermal ignition due to the effects of air movement, etc., the "
               "safety factor in this case is smaller than that normally used "
               "for grouping. The temperature classes are as follows."))

    # --- printed p.185: Table 8.1, then classes T1 and T2 -------------------
    b.append(table(T81.HEAD81_EN, T81.ROWS81, T81.CAPTION81_EN))
    b.append(note(T81.NOTE81_EN))
    b.append(note("<b>Note on lower-case 'european' in the Table 8.1 caption.</b> "
                  "The print reads 'Current european grouping system' with a "
                  "lower-case 'european'; this is preserved verbatim in the "
                  "English text and has not been corrected to 'European'."))

    b.append(p("<b>T1</b>"))
    b.append(p("For T1 the maximum apparatus temperature must not exceed "
               "440 °C. (As temperature classification is normally done at "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 400 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures in "
               "excess of 450 °C."))
    b.append(p("<b>T2</b>"))
    b.append(p("For T2 the maximum apparatus temperature must not exceed "
               "290 °C. (As temperature classification is normally done at "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 250 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures of "
               "between 300 °C and 450 °C."))

    # --- printed p.186: classes T3-T6, self-heating, small components -------
    b.append(p("<b>T3</b>"))
    b.append(p("For T3 the maximum apparatus temperature must not exceed "
               "195 °C. (As temperature classification is normally done at a "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 155 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures of "
               "between 200 °C and 300 °C."))
    b.append(p("<b>T4</b>"))
    b.append(p("For T4 the maximum apparatus temperature must not exceed "
               "130 °C. (As temperature classification is normally done at a "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 90 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures of "
               "between 135 °C and 200 °C."))
    b.append(p("<b>T5</b>"))
    b.append(p("For T5 the maximum apparatus temperature must not exceed "
               "95 °C. (As temperature classification is normally done at a "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 55 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures of "
               "between 100 °C and 135 °C."))
    b.append(p("<b>T6</b>"))
    b.append(p("For T6 the maximum apparatus temperature must not exceed "
               "80 °C. (As temperature classification is normally done at a "
               "40 °C ambient temperature, this usually means an elevation due "
               "to self heating of 40 °C.) Gases, vapours and mists associated "
               "with this temperature class will have ignition temperatures of "
               "between 85 °C and 100 °C."))
    b.append(p("As indicated, the self elevation of the apparatus permitted in "
               "all cases depends upon the ambient temperature at which "
               "temperature classification is carried out. If an item of "
               "apparatus is temperature classified as T3 at an ambient "
               "temperature of 100 °C its permitted self heating will be "
               "reduced to 95 °C, as the overall maximum temperature must "
               "remain the same."))
    b.append(p("It is also recognized that small components can exceed the "
               "ignition temperature of a particular gas, vapour or mist "
               "without causing ignition, and this has been demonstrated as "
               "the case. In general, this difference depends upon factors "
               "such as the convection performance of the particular gas, "
               "vapour or mist and the configuration of the hot surface. For "
               "this reason, there is no general relaxation (except in the "
               "case of intrinsic safety, see Chapter 13) and each type of "
               "small component must be treated individually. To do this it is "
               "necessary to determine the temperature at which the surface "
               "in question actually ignites a gas representative of the most "
               "sensitive in the temperature class, and then ensure that the "
               "surface does not exceed the following temperatures in service:"))

    # --- printed p.187: in-service limits, Table 8.2 -----------------------
    b.append(p("T1 – ignition temperature minus 50 °C<br>"
               "T2 – ignition temperature minus 50 °C<br>"
               "T3 – ignition temperature minus 50 °C<br>"
               "T4 – ignition temperature minus 25 °C<br>"
               "T5 – ignition temperature minus 25 °C<br>"
               "T6 – ignition temperature minus 25 °C"))
    b.append(p("A system of temperature classification similar in concept to "
               "this existed in Germany and the relationship between this and "
               "the current system is shown in Table 8.2. In the United States "
               "of America there was initially a system whereby apparatus "
               "classification (their equivalent of grouping) determined the "
               "maximum apparatus temperature (see Table 8.1) but in recent "
               "years they have adopted a variation on the European temperature "
               "classification system (see Table 8.2)."))
    b.append(table(T81.HEAD82_EN, T81.ROWS82, T81.CAPTION82_EN))
    b.append(note(T81.NOTE82_EN))
    return "".join(b)
