# -*- coding: utf-8 -*-
"""Chapter 17, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 490-496 (PDF pp. 511-517).

Opens with the lowercase mid-sentence continuation after Module A's
`However,`, gives the unnumbered surface-temperature equation and its
four-line `where` key, the USA temperature sub-divisions, both
`Selection on the basis of certification` sections, 17.3.2 dust risks,
17.3.3 zone of risk, and the numbered lists for Zones 0, 1, 2, 20 and 21
(including the complete nine-item Zone 21 list). Item 9 on printed p. 496
is complete, so the Survey B/C seam is clean.

The two unnumbered display blocks are the only `eq()` calls in this module.
No figures and no tables are emitted. Printed quirks are kept verbatim in
the English text and flagged with bilingual notes; the Vietnamese follows
the intended meaning. This is an unofficial study translation; the source
PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, eq, ol


def body_vi():
    b = []

    # ---- printed p.490: B1 (continuation after Module A's `However,`).
    b.append(p("một phân loại nhiệt độ bề mặt có thể được đưa ra cho nhiệt độ "
               "môi trường 40 °C, dù nhiệt độ hoạt động tối đa được quy định "
               "là một nhiệt độ cao hơn. Trong những trường hợp như vậy phải "
               "nhớ rằng phân loại nhiệt độ dựa trên sự tăng nhiệt của thiết "
               "bị so với môi trường và, ví dụ, thiết bị T5 được giả định có "
               "tự nâng nhiệt 60 °C nếu được phân loại ở 40 °C. Vì vậy, nếu "
               "thiết bị như vậy có thể dùng an toàn ở nhiệt độ môi trường "
               "100 °C, nhiệt độ bề mặt của nó khi sử dụng sẽ là 160 °C (tức "
               "là tương đương với T3 – hạn chế hơn hai cấp). Khi điều này "
               "xảy ra, cấp nhiệt độ thực tế khi sử dụng nên được suy ra như "
               "sau:"))

    # B2 - unnumbered display: the surface-temperature equation.
    b.append(eq("T<sub>x</sub> = T<sub>c</sub> − T<sub>a1</sub> + T<sub>a2</sub>"))

    # B3 - unnumbered display: the four-line `where` key.
    b.append(eq("where  T<sub>x</sub>  = nhiệt độ bề mặt tối đa khi sử dụng thực tế<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>c</sub>  = phân loại nhiệt độ bề mặt tại T<sub>a1</sub><br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>a1</sub> = nhiệt độ môi trường tối đa dùng để phân loại<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;nhiệt độ bề mặt<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>a2</sub> = nhiệt độ môi trường tối đa khi sử dụng thực tế"))

    # B4.
    b.append(p("Cần nhấn mạnh rằng cách tiếp cận này chỉ có thể áp dụng khi "
               "thiết bị đáp ứng yêu cầu của khái niệm bảo vệ tại "
               "T<sub>a2</sub>."))

    # B5 - USA temperature sub-divisions.
    b.append(p("Thiết bị từ Hoa Kỳ theo các yêu cầu hiện hành của Hoa Kỳ có "
               "hệ thống phân loại nhiệt độ phức tạp hơn nhiều – T2, T3 và T4 "
               "được chia nhỏ thêm. Nếu thiết bị như vậy được xác định là "
               "phù hợp về mặt khác, nên bỏ qua các phân chia nhỏ đó (tức là "
               "thiết bị T2A, T2B, T2C và T2D nên được xem là T2). Dù về "
               "nguyên tắc có thể sử dụng chúng nếu nhiệt độ gây cháy của "
               "khí, hơi hoặc sương mù đã biết, việc sử dụng chúng có khả "
               "năng gây nhiều nhầm lẫn và có thể dẫn đến nguy hiểm trừ khi "
               "mọi người liên quan đến việc lựa chọn, lắp đặt và bảo trì "
               "thiết bị đều hiểu rõ. Tương tự, thiết bị theo hệ thống cũ của "
               "Hoa Kỳ, trong đó nhiệt độ bề mặt không được xác định riêng mà "
               "liên quan đến hệ thống phân nhóm của Hoa Kỳ, có thể dùng được "
               "về mặt kỹ thuật nhưng việc sử dụng có thể gây nhầm lẫn đáng "
               "kể và nên tránh nếu có thể, trừ khi tình huống được hiểu rõ "
               "như trước. Việc thực hiện Chỉ thị mới của EU 94/9/EC có khả "
               "năng yêu cầu loại dần việc sử dụng thiết bị như vậy dù sao "
               "đi nữa, trừ khi nó đáp ứng Tiêu chuẩn châu Âu, khi đó sẽ yêu "
               "cầu dùng hệ thống phân loại nhiệt độ bề mặt của châu Âu."))
    b.append(note("<b>Ghi chú về các cụm in trong đoạn về Hoa Kỳ.</b> Bản in "
                  "viết ‘EU Directive 94/9/EU’ (chữ ‘EU’, không phải ‘EC’ như "
                  "ở các chỗ khác), ‘the equivalent of T3 – two classes more "
                  "restrictive’ (dấu gạch ngang dài) và ‘a self elevation of "
                  "60 °C’ (hai từ, không có dấu nối); bản tiếng Việt theo "
                  "nghĩa đúng, bản tiếng Anh giữ nguyên."))

    # B6 - heading.
    b.append(h4("Lựa chọn trên cơ sở chứng nhận",
                "Selection on the basis of certification"))

    # B7+B8 - certification paragraph, joined across printed 490/491.
    b.append(p("Hiện nay, chứng nhận thiết bị không phải là yêu cầu pháp lý ở "
               "Vương quốc Anh đối với thiết bị dùng trong bất kỳ vùng nguy "
               "hiểm nào. Tuy nhiên, mặc dù vậy, các Quy tắc Quốc gia "
               "(BS 5345, Phần 1³) khuyến nghị mạnh mẽ việc chứng nhận bởi "
               "một tổ chức chứng nhận được công nhận quốc gia cho Vùng 0 và "
               "1, và dù khuyến nghị này yếu hơn đáng kể đối với Vùng 2 thì "
               "nó vẫn còn tồn tại. Ở Vương quốc Anh, theo truyền thống đã có "
               "một thói quen chỉ sử dụng thiết bị đã được chứng nhận ở Vùng "
               "0 và 1 và chủ yếu dùng thiết bị đã chứng nhận ở Vùng 2. Chỉ "
               "trong những trường hợp đặc biệt, chẳng hạn như sử dụng các "
               "loại thiết bị đặc biệt sản xuất một lần, cách tiếp cận chung "
               "này mới được thay đổi và ngay cả khi đó cũng phải hết sức "
               "cẩn thận bảo đảm rằng việc đánh giá bởi những người có chuyên "
               "môn tương đương với nhân viên của các tổ chức chứng nhận được "
               "thực hiện, và việc đánh giá như vậy được khuyến nghị trong "
               "BS 5345, Phần 1³. Tình huống này sẽ được củng cố bởi Chỉ thị "
               "mới 94/9/EC², theo đó sẽ yêu cầu chứng nhận cho mọi thiết bị "
               "được đưa ra thị trường để dùng ở Vùng 0 và 1, và bởi một Chỉ "
               "thị khác về An toàn và Sức khỏe sẽ áp đặt giới hạn việc sử "
               "dụng thiết bị chưa được chứng nhận."))

    # B9.
    b.append(p("Vì vậy, rất khôn ngoan là luôn sử dụng thiết bị đã được chứng "
               "nhận bởi bên thứ ba ở Vùng 0 và 1, trừ những trường hợp rất "
               "đặc biệt, và cố gắng áp dụng cách tiếp cận tương tự ở Vùng 2 "
               "dù trong trường hợp này hiện nay có thể linh hoạt hơn về "
               "chính sách. Tuy nhiên, mọi thiết bị chưa được chứng nhận đều "
               "nên luôn được đánh giá bởi chuyên gia để bảo đảm rằng nó "
               "không đưa vào một rủi ro không thể chấp nhận."))

    # ---- printed p.491: 17.3.2 and dust enclosure/surface temperature.
    b.append(h3("17.3.2 Lựa chọn thiết bị cho nguy cơ bụi",
                "17.3.2 Selection of apparatus for dust risks"))

    # B11.
    b.append(p("Sự phân biệt giữa phát tia lửa và không phát tia lửa thường "
               "không có vị trí trong việc lựa chọn thiết bị cho nguy cơ bụi, "
               "vì bảo vệ thường là bằng cách loại trừ bụi ra khỏi bên trong "
               "vỏ bọc và loại trừ nó khỏi vùng lân cận của các tiếp điểm "
               "phát tia lửa. Các tiêu chí, được nêu trong BS 6467, Phần 2⁴, "
               "đơn giản hơn nhiều."))

    # B12 - heading.
    b.append(h4("Lựa chọn trên cơ sở bảo vệ bằng vỏ bọc",
                "Selection on the basis of enclosure protection"))

    # B13.
    b.append(p("Thiết bị dùng trong bầu khí quyển nổ của bụi và không khí cần "
               "đáp ứng yêu cầu về cấu tạo của BS 6467, Phần 1⁴, vỏ bọc của "
               "chúng loại trừ bầu khí quyển nổ ở mức độ cần thiết như quy "
               "định trong Tiêu chuẩn đó (IP5X hoặc IP6X) tùy theo Vùng sử "
               "dụng dự kiến (xem phần sau trong chương này). Bất kể Vùng sử "
               "dụng, vỏ bọc IP6X luôn được yêu cầu khi bụi là bụi dẫn điện. "
               "Trong thực tế điều này có nghĩa là đối với mọi môi trường "
               "bình thường sẽ cần vỏ bọc IP65 hoặc IP54 tùy theo Vùng sử "
               "dụng và loại bụi, với các chữ số thứ hai nhỏ hơn chỉ được "
               "chấp nhận khi có thể loại trừ sự xâm nhập của chất lỏng "
               "(chẳng hạn như trong môi trường trong nhà được kiểm soát về "
               "sự hiện diện của độ ẩm)."))
    b.append(note("<b>Ghi chú về ‘enlosures’ và ‘are much more simple’.</b> "
                  "Bản in viết ‘enlosures of IP6X’ (thiếu chữ ‘c’) và ‘are "
                  "much more simple’; bản tiếng Anh giữ nguyên cả hai, bản "
                  "tiếng Việt theo nghĩa đúng."))

    # B14 - heading.
    b.append(h4("Lựa chọn trên cơ sở nhiệt độ bề mặt bên ngoài",
                "Selection on the basis of external surface temperature"))

    # B15+B16 - dust layer/cloud conditions, joined across printed 491/492.
    b.append(p("Thiết bị theo BS 6467, Phần 1⁴ được cấp một nhiệt độ bề mặt "
               "tối đa trên cơ sở nhiệt độ bề mặt tối đa mà nó đạt được trong "
               "các thử nghiệm theo Tiêu chuẩn đó. Thiết bị như vậy có thể "
               "được dùng với lớp bụi và đám bụi như sau: thứ nhất, với bất "
               "kỳ loại bụi nào mà một lớp dày 5 mm không thể bị gây cháy bởi "
               "nhiệt độ cao hơn 75 °C so với nhiệt độ bề mặt tối đa của "
               "thiết bị; và thứ hai, với bất kỳ loại bụi nào có nhiệt độ "
               "gây cháy tối thiểu của đám bụi bằng 1,5 lần nhiệt độ bề mặt "
               "tối đa của thiết bị."))
    b.append(note("<b>Ghi chú về ‘ignition ignition’.</b> Bản in viết ‘minimum "
                  "cloud ignition ignition temperature’ (từ ‘ignition’ lặp "
                  "lại) và có khoảng trắng trong ‘5 mm’ và ‘75 °C’; bản tiếng "
                  "Anh giữ nguyên, bản tiếng Việt theo nghĩa đúng."))

    # ---- printed p.492: apparatus complying also with gas/vapour requirements.
    b.append(h4("Lựa chọn thiết bị cũng đáp ứng yêu cầu về nguy cơ khí và hơi",
                "Selection of apparatus complying also with requirements for gas and vapour risks"))

    # B18.
    b.append(p("Nhiều công việc đã được thực hiện để đưa ra các yêu cầu đối "
               "với thiết bị dùng cho nguy cơ khí và hơi, và có thể thu được "
               "lợi ích đáng kể bằng cách mở rộng việc sử dụng thiết bị như "
               "vậy vào các khu vực có nguy cơ bụi. Ngoài ra, nhiều khu vực "
               "nguy hiểm trở nên nguy hiểm do sự hiện diện đồng thời của "
               "bầu khí quyển nổ của cả khí và bụi, nên thiết bị phải phù hợp "
               "với cả hai nguy cơ. Điều này trở nên dễ dàng nhờ thực tế là "
               "nhiều yêu cầu về độ bền và các yêu cầu khác áp dụng cho thiết "
               "bị dùng cho nguy cơ khí rất giống với các yêu cầu đối với "
               "nguy cơ bụi."))
    b.append(note("<b>Ghi chú về cách diễn đạt tự tham chiếu.</b> Bản in viết "
                  "‘requirements applicable to apparatus for dust risks are "
                  "very similar to those required for dust risks’ (chỗ đầu "
                  "đáng lẽ là ‘gas risks’); bản tiếng Anh giữ nguyên, bản "
                  "tiếng Việt theo nghĩa đúng."))

    # B19.
    b.append(p("Việc lựa chọn thiết bị như vậy chủ yếu là bằng cách xác định, "
               "ngoài các yêu cầu áp dụng cho nguy cơ khí và hơi, tính toàn "
               "vẹn của vỏ bọc là IP5X hoặc IP6X như đối với thiết bị theo "
               "BS 6467, Phần 1⁴. Các yêu cầu lựa chọn thực tế liên quan đến "
               "từng khái niệm bảo vệ khí/hơi được quy định trong BS 7535⁵ "
               "và được thảo luận chi tiết trong Chương 15."))

    # B20.
    b.append(p("Như đã nêu, không giống như trường hợp khí/hơi, không có hệ "
               "thống phân loại chính thức, nên mỗi thiết bị được quy định có "
               "một nhiệt độ bề mặt tối đa cụ thể và nhiệt độ đó phải được so "
               "sánh với nhiệt độ gây cháy tối thiểu của từng loại bụi để "
               "chứng minh sự phù hợp."))

    # B21.
    b.append(p("Khi thiết bị được chứng minh rõ ràng là phù hợp với nguy cơ "
               "khí và hơi và có phân loại nhiệt độ bề mặt, nhìn chung có thể "
               "lấy phân loại nhiệt độ bề mặt làm chỉ dẫn về nhiệt độ bề mặt "
               "của bên ngoài thiết bị (xem Chương 15). Tuy nhiên, vì hệ số "
               "an toàn đối với các cấp nhiệt độ T3, T4, T5 và T6 chỉ là "
               "5 °C (tức là cấp nhiệt độ dựa trên nhiệt độ cao hơn 5 °C so "
               "với nhiệt độ bề mặt tối đa đo được), thay vì 10 °C dùng trong "
               "trường hợp nguy cơ bụi (xem BS 6467, Phần 1), mối quan hệ "
               "giữa cấp nhiệt độ và nhiệt độ gây cháy tối thiểu của lớp bụi "
               "và đám bụi nên là như cho trong Bảng 15.1 trong chương 15. Tất "
               "nhiên, điều này giả định rằng thiết bị phù hợp về mặt khác "
               "với nguy cơ bụi."))
    b.append(note("<b>Ghi chú về ‘Table 15.1 in chapter 15’.</b> Bản in viết "
                  "‘chapter’ thường (chữ ‘c’ thường), không phải ‘Chapter’; "
                  "bản tiếng Anh giữ nguyên."))

    # B22 - second `Selection on the basis of certification` heading.
    b.append(h4("Lựa chọn trên cơ sở chứng nhận",
                "Selection on the basis of certification"))

    # B23+B24 - dust certification paragraph, joined across printed 492/493.
    b.append(p("Khác với tình huống trong lĩnh vực nguy cơ khí, hơi và sương "
               "mù, có rất ít lịch sử về chứng nhận và rất ít thiết bị đã được "
               "chứng nhận có sẵn, ngoại trừ thiết bị được chứng nhận cho nguy "
               "cơ khí và hơi cũng phù hợp với nguy cơ bụi. Ngay cả trong "
               "trường hợp sau, chứng nhận chỉ mở rộng đến mức phù hợp với "
               "nguy cơ khí và hơi, để lại mọi yêu cầu bổ sung đối với nguy "
               "cơ bụi phải được đánh giá riêng. Chỉ thị mới 94/9/EC² sẽ thay "
               "đổi tất cả điều này, đưa thiết bị dùng cho nguy cơ bụi vào "
               "cùng một khuôn khổ với thiết bị dùng cho nguy cơ khí, hơi và "
               "sương mù, và yêu cầu chứng nhận bởi một tổ chức được thông "
               "báo đối với bất kỳ thiết bị như vậy được đưa ra thị trường "
               "trong EU cho Vùng 20 và 21. Điều này cuối cùng sẽ dẫn đến một "
               "văn hóa chứng nhận tương tự như văn hóa dành cho khí/hơi và "
               "sương mù, cho tất cả các Vùng có nguy cơ bụi. Tuy nhiên, điều "
               "này không thể xảy ra cho đến khi có các Tiêu chuẩn châu Âu cho "
               "thiết bị dùng cho nguy cơ bụi, và mặc dù hiện đang soạn thảo "
               "các tiêu chuẩn này, rất khó có khả năng bất kỳ thay đổi nào "
               "có thể trở thành bắt buộc trong vài năm tới."))
    b.append(note("<b>Ghi chú về ‘the gas/vapour, mist culture’ và ‘Zone 20 "
                  "and 21’.</b> Bản in đặt dấu phẩy sau ‘gas/vapour’ và viết "
                  "‘Zone 20 and 21’ (không lặp lại chữ ‘Zone’); bản tiếng Anh "
                  "giữ nguyên cả hai."))

    # B25.
    b.append(p("Ngoài các Tiêu chuẩn đã tồn tại khi cách tiếp cận đối với "
               "nguy cơ bụi ban đầu được hình thành, còn có các Tiêu chuẩn "
               "dành cho thiết bị dùng cho nguy cơ bụi mang tính xác định hơn "
               "nhiều, chứa các thử nghiệm cụ thể để xác định sự phù hợp. Việc "
               "thực hiện các thử nghiệm này có khả năng đòi hỏi các tổ chức "
               "tương tự như các tổ chức chứng nhận hiện được công nhận đối "
               "với thiết bị dùng cho nguy cơ khí và hơi, và các tổ chức "
               "chứng nhận này sẽ ngày càng tham gia nhiều hơn vì mong muốn "
               "của nhà sản xuất là thể hiện rõ thiết bị phù hợp và mong muốn "
               "của người sử dụng là có một số bảo đảm về điều đó. Vì vậy, "
               "chứng nhận có thể được kỳ vọng sẽ tăng nhanh như con đường "
               "ưu tiên để thể hiện sự phù hợp, bất kể Chỉ thị EU mất bao lâu "
               "để thực hiện, và đây là một sự phát triển hợp lý."))

    # ---- printed p.493: 17.3.3, zone of risk, Zone 0 policy.
    b.append(h3("17.3.3 Lựa chọn trên cơ sở vùng nguy cơ",
                "17.3.3 Selection on the basis of zone of risk"))
    b.append(h4("Nguy cơ khí và hơi", "Gas and vapour risks"))
    b.append(p("Ba Vùng phù hợp với nguy cơ khí, hơi và sương mù là Vùng 0, "
               "Vùng 1 và Vùng 2 theo thứ tự mức độ nghiêm trọng giảm dần."))

    b.append(h4("Vùng 0", "Zone 0"))
    b.append(p("Cần nhớ lại (xem Chương 2) rằng Vùng 0 thực sự là những nơi rất "
               "nguy hiểm, được giả định là luôn có bầu khí quyển nổ hiện "
               "diện. Vì lý do này, các vùng này rất hạn chế về kích thước và "
               "được ngăn chứa bằng một cách nào đó vì nguy cơ truy cập trái "
               "phép, với nguy cơ nổ kèm theo, là quá lớn. Ngoài ra, chỉ có "
               "một trong các dạng bảo vệ tiêu chuẩn phù hợp để lắp đặt ở "
               "Vùng 0, đó là an toàn nội tại ở hạng cao hơn ‘ia’. Điều này "
               "dẫn đến chính sách sau đây cần được áp dụng trong mọi "
               "trường hợp."))
    b.append(note("<b>Ghi chú về các cụm in ở Vùng 0.</b> Bản in viết ‘that "
                  "Zone 0 are very dangerous places indeed’ (số nhiều ‘are’), "
                  "‘contained in some way as the risk’ (‘as’ thay vì ‘against’) "
                  "và ‘This installation is instrumentation’; bản tiếng Anh "
                  "giữ nguyên cả ba."))

    # B31-B34 - Zone 0 numbered policy items 1-3 (item 3 joined across 493/494).
    b.append(ol([
        "Không nên có bất kỳ lắp đặt điện nào ở Vùng 0 trừ khi có thể xác định "
        "rõ một nhu cầu, chẳng hạn như lợi ích đáng kể về tối ưu hóa hoặc "
        "tăng cường an toàn vận hành. Mọi lắp đặt đề xuất ở Vùng 0 nên được "
        "xem xét cẩn thận theo các tiêu chí này trước khi thực hiện, để việc "
        "sử dụng nó có thể được biện minh trên cơ sở vững chắc và nhân viên "
        "không bị đặt vào bất kỳ rủi ro không cần thiết bổ sung nào.",
        "Khi các tiêu chí nêu trên được đáp ứng, các lắp đặt nên, trong chừng "
        "mực có thể, là các lắp đặt an toàn nội tại hạng ‘ia’. Điều này nên "
        "đáp ứng hầu hết các yêu cầu vì có nhiều kinh nghiệm vận hành xác "
        "định các giải pháp thay thế cho các lắp đặt ở Vùng 0 đối với hầu hết "
        "mọi loại lắp đặt điện, ngoại trừ các cảm biến cung cấp thông tin "
        "vận hành và an toàn. Lắp đặt này là thiết bị đo đạc và gần như luôn "
        "có thể được bảo vệ bằng an toàn nội tại hạng ‘ia’ nếu cần lắp đặt ở "
        "Vùng 0.",
        "Khi thiết bị không thể được bảo vệ bằng an toàn nội tại hạng ‘ia’ "
        "được lắp đặt ở Vùng 0, gần như chắc chắn theo định nghĩa nó mạnh hơn "
        "và có khả năng gây cháy lớn hơn. Do đó, các lắp đặt của thiết bị như "
        "vậy phải được xem xét phê phán hơn nhiều. Bất kỳ thiết bị nào như "
        "vậy thường là đối tượng của một cuộc đánh giá bởi tổ chức chứng nhận "
        "được công nhận quốc gia và chứng nhận là Loại ‘s’, được xác định "
        "riêng là đã được chế tạo để dùng ở Vùng 0. Số lượng thiết bị sẽ rất "
        "hạn chế và điều này một lần nữa ủng hộ lập luận rằng các lắp đặt ở "
        "Vùng 0 của thiết bị như vậy hiếm khi cần thiết. Khuyến nghị rằng chỉ "
        "xem xét loại lắp đặt này khi thực sự cần thiết. Một lắp đặt mà lý do "
        "tồn tại (raison d’être) chỉ là tăng nhẹ tính kinh tế vận hành thì khó "
        "có thể được coi là hợp lý, trong khi một lắp đặt quan trọng cho an "
        "toàn tổng thể thì có.",
    ]))
    b.append(note("<b>Ghi chú về các cụm in ở mục 3.</b> Bản in viết ‘In Zone "
                  "the presence’ (thiếu ‘1’), ‘certification as Type ‘s’’ với "
                  "dấu ngoặc nhọn, cụm tiếng Pháp nghiêng ‘raison d’être’ và "
                  "‘BS/EN 60079⁶ which will supersede BS 5345, will remove "
                  "that restriction’ (dấu phẩy đôi); bản tiếng Anh giữ nguyên, "
                  "bản tiếng Việt theo nghĩa đúng."))

    # ---- printed p.494: Zone 1 and its ten numbered items.
    b.append(h4("Vùng 1", "Zone 1"))
    b.append(p("Ở Vùng 1 sự hiện diện của bầu khí quyển nổ được dự kiến trong "
               "chưa tới 10 phần trăm thời gian của năm và, không giống như "
               "tình huống ở Vùng 0, nơi bầu khí quyển nổ luôn được dự kiến "
               "hiện diện, có thêm an toàn do khả năng thấp hơn là bầu khí "
               "quyển nổ trùng hợp với các lỗi có khả năng gây cháy, miễn là "
               "bảo vệ điện cho các lắp đặt là đầy đủ. Tình huống này được "
               "thừa nhận trong các khái niệm bảo vệ đa dạng cho thiết bị hiện "
               "có cho Vùng 1. Dù việc biện minh cho tất cả các lắp đặt điện "
               "vẫn cần thiết, vì ngay cả các lắp đặt được bảo vệ đúng cách "
               "cũng thực sự làm tăng nhẹ rủi ro so với mức sẽ tồn tại nếu "
               "chúng không có ở đó, các tiêu chí biện minh có thể được nới "
               "lỏng và các yếu tố kinh tế được coi trọng hơn. Cần nhớ, "
               "tuy nhiên, rằng Vùng 1 thường rất nhỏ và chỉ cần một chút "
               "suy nghĩ, nhiều lắp đặt có thể được đặt ở Vùng 2 lân cận hoặc "
               "các khu vực không nguy hiểm mà không mất nhiều hiệu quả. Với "
               "giả định rằng đã thực hiện các đánh giá như vậy, các khái "
               "niệm bảo vệ sau đây được chấp nhận cho Vùng 1:"))

    # B37-B46 - Zone 1 items 1-10 (items 8-10 on printed p.495).
    b.append(ol([
        "Bất kỳ thiết bị nào phù hợp cho Vùng 0 nhìn chung cũng được chấp nhận "
        "cho Vùng 1.",
        "Mạch an toàn nội tại ‘ib’ (xem Chương 13).",
        "Vỏ chống cháy ‘d’ (xem Chương 10).",
        "Thiết bị áp lực ‘p’ (xem Chương 11). Trong trường hợp này, hành động "
        "thực hiện khi mất áp là quan trọng và nhìn chung nên cách ly hoàn "
        "toàn mọi nguồn điện, dù trực tiếp hay gián tiếp qua các mạch truyền "
        "tín hiệu, ngay khi áp lực bị mất.",
        "Thiết bị nhồi bột ‘q’ (xem Chương 9). Ấn bản hiện hành của "
        "BS 5345, Phần 1³ không công nhận loại thiết bị này cho Vùng 1 nhưng "
        "BS/EN 60079⁶ mới được công bố, sẽ thay thế BS 5345, sẽ bỏ hạn chế đó.",
        "Thiết bị ngâm dầu ‘o’ (xem Chương 9). Một lần nữa, ấn bản hiện hành "
        "của BS 5345, Phần 1 không công nhận loại thiết bị này cho Vùng 1 "
        "nhưng BS/EN 60079–14 mới được công bố, sẽ thay thế BS 5345, bỏ hạn "
        "chế đó.",
        "Thiết bị an toàn tăng cường ‘e’ (xem Chương 12).",
        "Thiết bị bọc kín ‘m’ ( xem Chương 9). Khái niệm bảo vệ này không được "
        "ấn bản hiện hành của BS 5345, Phần 1 công nhận vì nó ra đời sau khi "
        "tài liệu đó được soạn thảo. Tuy nhiên, nó được công nhận trong "
        "BS/EN 60079 mới được công bố và sẽ thay thế BS 5345.",
        "Thiết bị được chứng nhận là Loại ‘s’ (có bảo vệ đặc biệt – xem "
        "Chương 16) bởi một tổ chức chứng nhận được công nhận quốc gia.",
        "Thiết bị được chứng nhận là Loại ‘s’ bởi một tổ chức chứng nhận châu "
        "Âu được thông báo theo Chỉ thị 76/117/EEC⁷, dùng giấy chứng nhận "
        "kiểm tra.",
    ]))
    b.append(note("<b>Ghi chú về các cụm in ở các mục 5, 6 và 8.</b> Bản in "
                  "viết ‘BS/EN 60079⁶ which will supersede BS 5345, will remove "
                  "that restriction’ (dấu phẩy đôi), ‘BS/EN 60079–14 … remove "
                  "that restriction’ (dấu gạch ngang dài; ‘remove’ chứ không "
                  "phải ‘will remove’) và ‘‘m’ ( see Chapter 9)’ (có khoảng "
                  "trắng sau dấu ngoặc) cùng ‘BS/EN 60079 recently published "
                  "and which will supersede BS 5345’ (thiếu ‘which was’); bản "
                  "tiếng Anh giữ nguyên."))

    # ---- printed p.495: Zone 2, dust apparatus, Zone 20.
    b.append(h4("Vùng 2", "Zone 2"))
    b.append(p("Vùng 2 là vùng ít nguy hiểm nhất trong số các khu vực nguy "
               "hiểm liên quan đến nguy cơ khí, hơi và sương mù, có bầu khí "
               "quyển nổ hiện diện không quá 0,1 phần trăm thời gian của năm. "
               "Mức bảo vệ tối thiểu cho thiết bị điện được giảm và những "
               "thiết bị sau đây được chấp nhận:"))
    b.append(ol([
        "Bất kỳ thiết bị nào được chấp nhận dùng ở Vùng 0 nhìn chung cũng được "
        "chấp nhận ở Vùng 2.",
        "Bất kỳ thiết bị nào được chấp nhận dùng ở Vùng 1 nhìn chung cũng được "
        "chấp nhận ở Vùng 2.",
        "Thiết bị có dạng bảo vệ ‘N’ (xem Chương 14). Hiện đang soạn thảo một "
        "Tiêu chuẩn Châu Âu và Quốc tế cho dạng bảo vệ ‘n’. Thiết bị theo "
        "Tiêu chuẩn đó nhìn chung cũng sẽ được chấp nhận.",
        "Thiết bị công nghiệp không phát hồ quang hay tia lửa và không tạo ra "
        "bề mặt nóng có khả năng gây cháy trong vận hành bình thường cũng được "
        "chấp nhận, miễn là đã được các chuyên gia đánh giá như vậy. Rất có "
        "thể nhu cầu về thiết bị như vậy sẽ dần biến mất theo thời gian khi "
        "thiết bị Loại ‘N’ hoặc ‘n’ trở nên sẵn có hơn. Cần nhấn mạnh rằng nếu "
        "thiết bị Loại ‘N’ hoặc ‘n’ có sẵn thì lý do biện minh cho việc sử dụng "
        "thiết bị công nghiệp này yếu hơn nhiều.",
    ]))

    b.append(h4("Thiết bị cho nguy cơ bụi", "Apparatus for dust risks"))
    b.append(p("Dù không rõ ràng bằng, sự phân chia giữa các Vùng bụi về cơ bản "
               "là giữa các Vùng khí và hơi. Có những cách tiếp cận tương tự "
               "cũng tồn tại nhưng cần nhớ rằng Vùng 20, tương đương với Vùng "
               "0, trước đây chưa từng tồn tại và cách tiếp cận đối với các "
               "lắp đặt trong Vùng này yếu hơn nhiều."))

    b.append(h4("Vùng 20", "Zone 20"))
    b.append(p("Vùng 20, là Vùng mà các đám bụi luôn hoặc gần như luôn hiện "
               "diện, thường là một Vùng được ngăn chứa bên trong các bình chế "
               "biến bụi. Như với tương đương khí/hơi của nó (Vùng 0), các "
               "lắp đặt điện chỉ nên được đặt ở Vùng 20 khi thực sự cần thiết. "
               "Tình huống trở nên nghiêm trọng hơn ở đây vì ảnh hưởng của bụi "
               "xâm nhập vào bên trong vỏ bọc và gây ra các vấn đề đặc biệt do "
               "sự hiện diện liên tục của nó bên trong, và khái niệm bảo vệ "
               "dẫn đến là loại trừ bụi. Điều này có nghĩa là không có thiết bị "
               "điện nào có thể được bảo vệ hiệu quả để dùng ở Vùng 20 nếu "
               "nguồn cấp và các kết nối điện khác của nó chứa năng lượng có "
               "khả năng gây cháy. Ngoại lệ là an toàn nội tại, trong đó nguồn "
               "cấp đến thiết bị không có khả năng gây cháy nhưng, ngay cả ở "
               "đây, sự hiện diện của bụi bên trong, dù dẫn điện hay không, "
               "có thể gây chập mạch bên trong, đặc biệt trong điều kiện ẩm "
               "ướt. Vì vậy, thiết bị duy nhất có thể được sử dụng ở Vùng 20 "
               "là mạch an toàn nội tại hạng ‘ia’ (xem Chương 13), trong đó vỏ "
               "bọc ít nhất là IP6X và mạch được đánh giá lại với giả định "
               "khả năng kết nối giữa bất kỳ bộ phận dẫn điện bên trong nào "
               "không được phủ, bọc kín hoặc cách điện."))
    b.append(note("<b>Ghi chú về câu cuối của Vùng 20.</b> Bản in viết ‘the only "
                  "apparatus which could possibly be used in Zone 20 "
                  "intrinsically safe circuits category ‘ia’’ (thiếu ‘is’ "
                  "sau ‘Zone 20’); bản tiếng Anh giữ nguyên, bản tiếng Việt "
                  "theo nghĩa đúng."))

    # ---- printed p.496: Zone 21 (Zone Z) and its nine numbered items.
    b.append(h4("Vùng 21 (Vùng Z)", "Zone 21 (Zone Z)"))
    b.append(p("Đây là tương đương của Vùng 1 và cách tiếp cận đối với thiết bị "
               "phù hợp tương tự nhưng có tính đến các vấn đề lắng đọng riêng "
               "của bụi. Vì vậy, các thiết bị sau đây được chấp nhận:"))
    b.append(ol([
        "Thiết bị phù hợp cho Vùng 20 nhìn chung được chấp nhận.",
        "Thiết bị theo BS 6467, Phần 1⁴ với vỏ bọc IP6X (xem Chương 15).",
        "Thiết bị ngâm dầu ‘o’ (xem các Chương 9 và 15), miễn là vỏ bọc của nó "
        "ít nhất là IP6X.",
        "Thiết bị áp lực ‘p’ (xem các Chương 11 và 15), miễn là vỏ bọc của nó "
        "ít nhất là IP6X (không tính các lối xả) khi không có áp lực. Hành động "
        "thực hiện khi mất áp lực nên giống như yêu cầu ở Vùng 1.",
        "Thiết bị nhồi bột ‘q’ (xem các Chương 9 và 15), miễn là vỏ bọc của nó "
        "ít nhất là IP6X.",
        "Vỏ chống cháy ‘p’ (xem các Chương 10 và 15), với điều kiện vỏ bọc của "
        "nó ít nhất là IP6X.",
        "Thiết bị an toàn tăng cường ‘e’ (xem các Chương 12 và 15), miễn là vỏ "
        "bọc của nó ít nhất là IP6X.",
        "Mạch an toàn nội tại thuộc cả hai hạng ‘ia’ và ‘ib’ (xem các Chương "
        "13 và 15), miễn là vỏ bọc của chúng ít nhất là IP6X hoặc, nếu không "
        "phải vậy, hạng ‘ia’ với việc đánh giá lại giả định rằng mọi bộ phận "
        "dẫn điện không được phủ, bọc kín hoặc cách điện được giả định là có "
        "khả năng kết nối với nhau.",
        "Thiết bị bọc kín ‘m’ (xem Chương 9). Trong trường hợp này, chất bọc "
        "kín được xem là đầy đủ mà không cần vỏ bọc IP6X, dù vỏ bọc như vậy "
        "vẫn cần thiết cho bất kỳ đầu nối tiếp xúc nào bị lộ.",
    ]))
    b.append(note("<b>Ghi chú về mục 6 của Vùng 21.</b> Bản in viết ‘Flameproof "
                  "enclosures ‘p’ (see Chapters 10 and 15)’ – ký hiệu ‘p’ thay "
                  "vì ‘d’ như ở mục 3 của Vùng 1 – và dùng ‘providing’ thay vì "
                  "‘provided’; bản tiếng Anh giữ nguyên, bản tiếng Việt theo "
                  "nghĩa đúng."))

    return "".join(b)


def body_en():
    b = []

    # ---- printed p.490: B1 (continuation after Module A's `However,`).
    b.append(p("a surface temperature classification may be given for an "
               "ambient of 40 °C, despite the maximum operating temperature "
               "being specified as a higher temperature. In such cases it must "
               "be remembered that the temperature classification is based "
               "upon the rise of the apparatus above ambient and, for example, "
               "T5 apparatus is assumed to have a self elevation of 60 °C if "
               "classified at 40 °C. If such apparatus can be safely used at "
               "an ambient of 100 °C, therefore, its surface temperature for "
               "the purpose of use would be 160 °C (i.e., the equivalent of T3 "
               "– two classes more restrictive). Where this occurs the actual "
               "temperature class of usage should be derived as follows:"))

    # B2 - unnumbered display: the surface-temperature equation.
    b.append(eq("T<sub>x</sub> = T<sub>c</sub> − T<sub>a1</sub> + T<sub>a2</sub>"))

    # B3 - unnumbered display: the four-line `where` key.
    b.append(eq("where  T<sub>x</sub>  = maximum surface temperature for actual use<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>c</sub>  = surface temperature classification at T<sub>a1</sub><br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>a1</sub> = maximum ambient temperature used for surface<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;temperature classification<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;T<sub>a2</sub> = maximum ambient temperature of actual use"))

    # B4.
    b.append(p("It must be stressed that such an approach is only possible "
               "where the apparatus satisfies the requirements of the "
               "protection concept at T<sub>a2</sub>."))

    # B5 - USA temperature sub-divisions.
    b.append(p("Apparatus from the USA to current US requirements has a much "
               "more complex temperature classification system – T2, T3 and T4 "
               "being further sub-divided. If such apparatus is decided to be "
               "otherwise suitable for use then it is recommended that the "
               "sub-divisions be disregarded (i.e., T2A, T2B, T2C and T2D "
               "apparatus should be considered as T2). While, in principle, it "
               "is possible to utilize them if the ignition temperature of the "
               "gas, vapour or mist is known, their use is likely to cause much "
               "confusion and could lead to danger unless it is clearly "
               "understood by all concerned in selection, installation and "
               "maintenance of apparatus. Likewise apparatus to the historic "
               "US system, where surface temperature was not separately "
               "identified and was related to the US grouping system, may be "
               "technically usable but, its use could cause considerable "
               "confusion and should be avoided if possible unless the "
               "situation is clearly understood as before. The implementation "
               "of the new EU Directive 94/9/EU is likely to require the "
               "phasing out of the use of such apparatus in any event unless "
               "it complies with European Standards which would require it to "
               "use the European surface temperature classification system."))
    b.append(note("<b>Source quirks in the USA paragraph.</b> The print reads "
                  "‘EU Directive 94/9/EU’ (‘EU’, not ‘EC’ as elsewhere), ‘the "
                  "equivalent of T3 – two classes more restrictive’ (en dash) "
                  "and ‘a self elevation of 60 °C’ (two words, no hyphen); all "
                  "retained."))

    # B6 - heading.
    b.append(h4("Selection on the basis of certification",
                "Selection on the basis of certification"))

    # B7+B8 - certification paragraph, joined across printed 490/491.
    b.append(p("At present certification of apparatus is not a legal "
               "requirement in the UK for apparatus for use in any zone of "
               "risk. Notwithstanding this, however, National Codes "
               "(BS 5345, Part 1³) strongly recommend certification by a "
               "nationally recognized certification body for Zone 0 and 1 and "
               "although this recommendation is considerably weaker in "
               "relation to Zone 2 it is still present. In the UK there has, "
               "historically been a culture of utilizing only certified "
               "apparatus in Zone 0 and 1 and mainly certified apparatus in "
               "Zone 2. Only in exceptional circumstances, such as the use of "
               "special one-off types of apparatus, has this general approach "
               "been varied and even then great care has been taken to ensure "
               "that an evaluation by people of the expertise of those "
               "employed by certification bodies is carried out, and such an "
               "evaluation is recommended in BS 5345, Part 1³. This situation "
               "will be reinforced by the new Directive 94/9/EC² which will "
               "require such certification for all equipment marketed for "
               "Zone 0 and 1 use and by a further Directive on Health and "
               "Safety which will impose limits on the use of uncertified "
               "apparatus."))

    # B9.
    b.append(p("It is very wise, therefore, to always use apparatus which has "
               "been third-party certified in Zone 0 and 1, except in very "
               "special circumstances, and to try to use the same approach in "
               "Zone 2 although in this case more flexibility in policy is "
               "currently possible. All non-certified apparatus should, "
               "however, always be expertly evaluated to ensure that it does "
               "not introduce an unacceptable risk."))

    # ---- printed p.491: 17.3.2 and dust enclosure/surface temperature.
    b.append(h3("17.3.2 Selection of apparatus for dust risks",
                "17.3.2 Selection of apparatus for dust risks"))

    # B11.
    b.append(p("The sparking/non-sparking differentiation does not normally "
               "have a place in selection of apparatus for dust risks as "
               "protection is normally by exclusion of dust from within "
               "enclosures and its exclusion from the proximity of sparking "
               "contacts. The criteria, which are given in BS 6467, Part 2⁴, "
               "are much more simple."))

    # B12 - heading.
    b.append(h4("Selection on the basis of enclosure protection",
                "Selection on the basis of enclosure protection"))

    # B13.
    b.append(p("Apparatus for use in explosive atmospheres of dust and air "
               "need to comply with the constructional requirement of "
               "BS 6467, Part 1⁴, their enclosures excluding the explosive "
               "atmosphere to the degree necessary as defined in that Standard "
               "(IP5X or IP6X) depending upon the intended Zone of use (see "
               "later in this chapter). Regardless of the Zone of use, "
               "enlosures of IP6X are always required where the dust is a "
               "conducting dust. In practice this means that for all normal "
               "environments enclosures of IP65 or IP54 will be required "
               "depending upon the Zone of use and the type of dust, with "
               "lesser second numerals only acceptable where liquid ingress "
               "can be discounted (such as in indoor environments which are "
               "controlled as to the presence of moisture)."))
    b.append(note("<b>Source quirks: ‘enlosures’ and ‘are much more simple’.</b> "
                  "The print has ‘enlosures of IP6X’ (missing ‘c’) and ‘are "
                  "much more simple’; both retained."))

    # B14 - heading.
    b.append(h4("Selection on the basis of external surface temperature",
                "Selection on the basis of external surface temperature"))

    # B15+B16 - dust layer/cloud conditions, joined across printed 491/492.
    b.append(p("Apparatus to BS 6467, Part 1⁴ is given a maximum surface "
               "temperature on the basis of the maximum surface temperature "
               "which it achieves in tests in accordance with that Standard. "
               "Such apparatus may be used with dust layers and clouds as "
               "follows: first, with any dust where a layer of 5 mm cannot be "
               "ignited by a temperature 75 °C in excess of the maximum "
               "surface temperature of the apparatus; and second, with any "
               "dust with a minimum cloud ignition ignition temperature of "
               "1.5 times the maximum surface temperature of the apparatus."))
    b.append(note("<b>Source quirk: ‘ignition ignition’.</b> The print reads "
                  "‘minimum cloud ignition ignition temperature’ (the word "
                  "‘ignition’ is duplicated) and has a space in ‘5 mm’ and "
                  "‘75 °C’; retained."))

    # ---- printed p.492: apparatus complying also with gas/vapour requirements.
    b.append(h4("Selection of apparatus complying also with requirements for gas and vapour risks",
                "Selection of apparatus complying also with requirements for gas and vapour risks"))

    # B18.
    b.append(p("Much work has gone into the production of requirements for "
               "apparatus for gas and vapour risks and considerable benefit "
               "can be obtained by extending the use of such apparatus into "
               "dust risk areas. In addition, many hazardous areas are made "
               "hazardous by the presence of explosive atmospheres of both gas "
               "and dust, so that apparatus must be suitable for both risks. "
               "This is made easy by the fact that many of the strength and "
               "other requirements applicable to apparatus for dust risks are "
               "very similar to those required for dust risks."))
    b.append(note("<b>Source quirk: self-referential wording.</b> The print "
                  "reads ‘requirements applicable to apparatus for dust risks "
                  "are very similar to those required for dust risks’ (the "
                  "first should presumably read ‘gas risks’); retained."))

    # B19.
    b.append(p("The selection of such apparatus is principally by identifying, "
               "in addition to those requirements applied for gas and vapour "
               "risks, the integrity of the enclosure as IP5X or IP6X as for "
               "apparatus to BS 6467, Part 1⁴. The actual selection "
               "requirements in relation to each gas/vapour protection concept "
               "are specified in BS 7535⁵ and are discussed in detail in "
               "Chapter 15."))

    # B20.
    b.append(p("As already specified there is, unlike the gas/vapour "
               "situation, no formal classification system and so each item "
               "of apparatus is specified as having a particular maximum "
               "surface temperature and that must be compared with the "
               "minimum ignition temperature of each dust to demonstrate "
               "suitability."))

    # B21.
    b.append(p("Where apparatus is demonstrably suitable for gas and vapour "
               "risks and has a surface temperature classification it will "
               "normally be possible to take the surface temperature "
               "classification as an indication of the surface temperature of "
               "the outside of the apparatus (see Chapter 15). However, "
               "because the safety factor for temperature classes T3, T4, T5 "
               "and T6 is only 5 °C (i.e., the temperature class is based upon "
               "a temperature 5 °C higher than the measured maximum surface "
               "temperature), rather than 10 °C used in the case of dust risks "
               "(see BS 6467, Part 1), the relationship between the temperature "
               "class and the minimum dust layer and cloud ignition "
               "temperature should be that given in Table 15.1 in chapter 15. "
               "This presupposes, of course, that the apparatus is otherwise "
               "suitable for dust risks."))
    b.append(note("<b>Source quirk: ‘Table 15.1 in chapter 15’.</b> The print "
                  "uses a lowercase ‘chapter’ here; retained."))

    # B22 - second `Selection on the basis of certification` heading.
    b.append(h4("Selection on the basis of certification",
                "Selection on the basis of certification"))

    # B23+B24 - dust certification paragraph, joined across printed 492/493.
    b.append(p("Unlike the situation in the area of gas, vapour and mist risks "
               "there is little history of certification and little certified "
               "apparatus is available except for that certified for gas and "
               "vapour risks which is also suitable for dust risks. Even in "
               "this latter case the certification only extends as far as the "
               "suitability for gas and vapour risks leaving any additional "
               "requirements for dust risks to be separately assessed. The new "
               "Directive 94/9/EC² will change all this bringing apparatus for "
               "dust risks under the same umbrella as that for gas, vapour and "
               "mist risks and requiring certification by a notified body for "
               "any such apparatus marketed in the EU for Zone 20 and 21. This "
               "will ultimately lead to a certification culture similar to the "
               "gas/vapour, mist culture for all dust risk Zones. This cannot "
               "happen, however, until European Standards exist for apparatus "
               "for dust risks and although these are currently being written "
               "it is not likely that any change could become mandatory for "
               "some years."))
    b.append(note("<b>Source quirks: ‘the gas/vapour, mist culture’ and ‘Zone "
                  "20 and 21’.</b> The print places a comma after "
                  "‘gas/vapour’ and writes ‘Zone 20 and 21’ without repeating "
                  "‘Zone’; both retained."))

    # B25.
    b.append(p("In addition to Standards which existed when the approach to "
               "dust risks was initially formed there are Standards for "
               "apparatus for dust risks which are much more definitive, "
               "containing specific testing to determine suitability. The "
               "execution of these tests is likely to require organizations "
               "similar to the currently recognized certification bodies for "
               "gas and vapour risk equipment and these certification bodies "
               "will become more and more involved because of the desire of "
               "manufacturers to show clearly that the apparatus is suitable, "
               "and the desire of users to have some guarantee of this. Thus "
               "certification may be expected to increase rapidly as the "
               "preferred route to show suitability, however long the EU "
               "Directive takes to implement it, and this is a sensible "
               "development."))

    # ---- printed p.493: 17.3.3, zone of risk, Zone 0 policy.
    b.append(h3("17.3.3 Selection on the basis of zone of risk",
                "17.3.3 Selection on the basis of zone of risk"))
    b.append(h4("Gas and vapour risks", "Gas and vapour risks"))
    b.append(p("The three Zones appropriate to gas, vapour and mist risks are "
               "Zone 0, Zone 1 and Zone 2 in descending order of severity."))

    b.append(h4("Zone 0", "Zone 0"))
    b.append(p("It will be remembered (see Chapter 2) that Zone 0 are very "
               "dangerous places indeed, being assumed to have an explosive "
               "atmosphere always present. For this reason they are very "
               "limited in size and contained in some way as the risk of "
               "unauthorized access, with the attendant risk of explosion, is "
               "too great. In addition, there is only one of the standard "
               "forms of protection suitable for installation in Zone 0 and "
               "that is intrinsic safety of the higher category ‘ia’. This "
               "leads to the following policy which should be used in all "
               "cases."))
    b.append(note("<b>Source quirks in the Zone 0 paragraph.</b> The print "
                  "reads ‘that Zone 0 are very dangerous places indeed’ "
                  "(plural ‘are’), ‘contained in some way as the risk’ (‘as’ "
                  "where ‘against’ might be expected) and ‘This installation "
                  "is instrumentation’; all retained."))

    # B31-B34 - Zone 0 numbered policy items 1-3 (item 3 joined across 493/494).
    b.append(ol([
        "No electrical installations should be present in Zone 0 unless a "
        "clear requirement can be identified, such as significant "
        "optimization benefit or increase in operational safety. Every "
        "proposed Zone 0 installation should be carefully examined against "
        "these criteria before being implemented so that its use can be "
        "defended on secure grounds and personnel are not placed at any "
        "additional unnecessary risk.",
        "Where the above criteria are satisfied installations should, as far "
        "as possible, be intrinsically safe installations of category ‘ia’. "
        "This should satisfy most requirements as there is much operational "
        "history which identifies alternatives to Zone 0 installations for "
        "almost all types of electrical installation, save such things as "
        "sensors providing operational and safety information. This "
        "installation is instrumentation and can almost always be protected "
        "by intrinsic safety category ‘ia’ if it needs to be fitted in Zone 0.",
        "Where equipment which cannot be protected by intrinsic safety "
        "category ‘ia’ is to be installed in Zone 0, it is almost certainly by "
        "definition more powerful and potentially more ignition capable. "
        "Installations of such apparatus therefore must be much more "
        "critically examined. Any such apparatus is normally the subject of "
        "an evaluation by a nationally recognized certification body and "
        "certification as Type ‘s’ which is specifically identified as having "
        "been constructed for Zone 0 use. The amount of apparatus will be very "
        "limited and this again supports the argument that Zone 0 "
        "installations of such apparatus are rarely necessary. It is "
        "recommended that this type of installation only be considered when "
        "it is absolutely necessary. Such an installation whose raison "
        "d’être was a small increase in economy of operation would be unlikely "
        "to be justifiable, whereas one which was important to overall safety "
        "would.",
    ]))
    b.append(note("<b>Source quirks in item 3.</b> The print has ‘In Zone the "
                  "presence’ (missing ‘1’), ‘certification as Type ‘s’’ with "
                  "curly quotes, the italic French phrase ‘raison d’être’, and "
                  "‘BS/EN 60079⁶ which will supersede BS 5345, will remove that "
                  "restriction’ with a double comma; all retained."))

    # ---- printed p.494: Zone 1 and its ten numbered items.
    b.append(h4("Zone 1", "Zone 1"))
    b.append(p("In Zone the presence of an explosive atmosphere is expected "
               "for less than 10 per cent of the year and, unlike the situation "
               "in Zone 0 where an explosive atmosphere is always expected to "
               "be present, there is added security in the lower likelihood of "
               "coincidence of explosive atmosphere and ignition-capable "
               "faults, provided electrical protection of installations is "
               "adequate. This situation is recognized in the multiple "
               "protection concepts for equipment which exist for Zone 1. "
               "While the justification for all electrical installations is "
               "still necessary, as even properly protected installations do "
               "constitute a slight increase in risk over that which would "
               "exist if they were not there, the justification criteria can "
               "be eased and economic factors given more weight. It should be "
               "remembered, however, that Zone 1 is often very small and with "
               "a little thought many installations could be sited in adjacent "
               "Zone 2 or non-hazardous areas with little loss of "
               "effectiveness. Given that such appraisals have been carried "
               "out the following protection concepts are acceptable for "
               "Zone 1:"))

    # B37-B46 - Zone 1 items 1-10 (items 8-10 on printed p.495).
    b.append(ol([
        "Any apparatus suitable for Zone 0 is usually acceptable for Zone 1 "
        "also.",
        "Intrinsically safe circuits ‘ib’ (see Chapter 13).",
        "Flameproof enclosure ‘d’ (see Chapter 10).",
        "Pressurized apparatus ‘p’ (see Chapter 11). In this case the action "
        "taken on pressure failure is important and normally total isolation "
        "of all electrical supplies, whether direct or indirect through "
        "information transfer circuits, should occur as soon as the "
        "pressurization fails.",
        "Powder-filled apparatus ‘q’ (see Chapter 9). The current edition of "
        "BS 5345, Part 1³ does not recognize this type of apparatus for Zone 1 "
        "but the recently published BS/EN 60079⁶ which will supersede BS 5345, "
        "will remove that restriction.",
        "Oil-immersed apparatus ‘o’ (see Chapter 9). Again the current edition "
        "of BS 5345, Part 1 does not recognize this type of apparatus for Zone "
        "1 but the recently published BS/EN 60079–14, which will supersede BS "
        "5345, remove that restriction.",
        "Increased safety apparatus ‘e’ (see Chapter 12).",
        "Encapsulated apparatus ‘m’ ( see Chapter 9). This protection concept "
        "is not recognized by the current edition of BS 5345, Part 1 as it "
        "post dates the production of that document. It is, however, "
        "recognized in BS/EN 60079 recently published and which will supersede "
        "BS 5345.",
        "Apparatus which is certified as Type ‘s’ (having special protection "
        "– see Chapter 16) by a nationally recognized certification body.",
        "Apparatus which is certified as Type ‘s’ by a Notified European "
        "certification body under Directive 76/117/EEC⁷ using an inspection "
        "certificate.",
    ]))
    b.append(note("<b>Source quirks in items 5, 6 and 8.</b> The print has "
                  "‘BS/EN 60079⁶ which will supersede BS 5345, will remove that "
                  "restriction’ (double comma), ‘BS/EN 60079–14 … remove that "
                  "restriction’ (en dash; ‘remove’ not ‘will remove’), ‘‘m’ ( "
                  "see Chapter 9)’ with a space after the opening parenthesis, "
                  "and ‘BS/EN 60079 recently published and which will supersede "
                  "BS 5345’ (missing ‘which was’); all retained."))

    # ---- printed p.495: Zone 2, dust apparatus, Zone 20.
    b.append(h4("Zone 2", "Zone 2"))
    b.append(p("Zone 2 is the least hazardous of the hazardous areas "
               "associated with gas, vapour and mist risks having explosive "
               "atmospheres present for no more than 0.1 per cent of the year. "
               "The minimum protection of electrical apparatus is reduced and "
               "the following are acceptable:"))
    b.append(ol([
        "Any apparatus acceptable for use in Zone 0 is normally acceptable in "
        "Zone 2 also.",
        "Any apparatus acceptable for use in Zone 1 is normally acceptable in "
        "Zone 2 also.",
        "Apparatus with type of protection ‘N’ (see Chapter 14). A European "
        "and International Standard for type of protection ‘n’ is currently "
        "being produced. Apparatus in accordance with this Standard will also "
        "normally be acceptable.",
        "Industrial apparatus which does not arc or spark and does not produce "
        "ignition-capable hot surfaces in normal operation is also acceptable, "
        "provided that it has been so evaluated by experts. It is likely that "
        "the need for such apparatus will slowly disappear as time progresses "
        "and Type ‘N’ or ‘n’ apparatus becomes more readily available. It is "
        "stressed that if Type ‘N’ or ‘n’ apparatus is available the "
        "justification for the use of this industrial apparatus is much "
        "weaker.",
    ]))

    b.append(h4("Apparatus for dust risks", "Apparatus for dust risks"))
    b.append(p("Although it is not as clear cut, the division between dust "
               "Zones is essentially that between gas and vapour Zones. "
               "Similar approaches also exist but it must be remembered that "
               "Zone 20, the equivalent of Zone 0, has not historically "
               "existed and the approach to installations in this Zone is much "
               "more tenuous."))

    b.append(h4("Zone 20", "Zone 20"))
    b.append(p("Zone 20, being the Zone in which dust clouds are always or "
               "nearly always present, is usually a contained Zone inside "
               "dust processing vessels. As with its gas/vapour counterpart "
               "(Zone 0) electrical installations should only be placed in "
               "Zone 20 when absolutely necessary. The situation is "
               "exacerbated here because of the effect of dust entering an "
               "enclosure and causing special problems because of its "
               "continued presence once inside, and the resultant protection "
               "concept of excluding the dust. This means that no electrical "
               "apparatus can be effectively protected for use in Zone 20 if "
               "its supplies and other electrical connections contain "
               "ignition-capable energies. The exception is intrinsic safety "
               "where the feeds to the apparatus are not ignition capable "
               "but, even here, the presence of dust in the interior, whether "
               "it is conducting or not, may cause internal short circuits "
               "particularly in damp conditions. Thus the only apparatus "
               "which could possibly be used in Zone 20 intrinsically safe "
               "circuits category ‘ia’ (see Chapter 13) where the enclosure is "
               "at least IP6X and the circuit is reassessed assuming the "
               "possibility of connection between any internal conducting "
               "parts which are not coated, encapsulated or insulated."))
    b.append(note("<b>Source quirk: the final Zone 20 sentence.</b> The print "
                  "reads ‘the only apparatus which could possibly be used in "
                  "Zone 20 intrinsically safe circuits category ‘ia’’ (missing "
                  "‘is’ after ‘Zone 20’); retained."))

    # ---- printed p.496: Zone 21 (Zone Z) and its nine numbered items.
    b.append(h4("Zone 21 (Zone Z)", "Zone 21 (Zone Z)"))
    b.append(p("This is the equivalent of Zone 1 and the approach to suitable "
               "apparatus is similar but takes into account the problems of "
               "settlement particular to dusts. The following apparatus is "
               "therefore acceptable:"))
    b.append(ol([
        "Apparatus suitable for Zone 20 is normally acceptable.",
        "Apparatus in accordance with BS 6467, Part 1⁴ with an IP6X enclosure "
        "(see Chapter 15).",
        "Oil-immersed apparatus ‘o’ (see Chapters 9 and 15), provided its "
        "enclosure is at least IP6X.",
        "Pressurized apparatus ‘p’ (see Chapters 11 and 15), provided its "
        "enclosure is at least IP6X (excluding purge outlets) in the absence "
        "of pressurization. The action taken on pressurization failure should "
        "be as that required in Zone 1.",
        "Powder-filled apparatus ‘q’ (see Chapters 9 and 15), provided its "
        "enclosure is at least IP6X.",
        "Flameproof enclosures ‘p’ (see Chapters 10 and 15), providing its "
        "enclosure is at least IP6X.",
        "Increased safety apparatus ‘e’ (see Chapters 12 and 15), provided "
        "its enclosure is at least IP6X.",
        "Intrinsically safe circuits of both categories ‘ia’ and ‘ib’ (see "
        "Chapters 13 and 15), provided their enclosure is at least IP6X or, "
        "where this is not so, category ‘ia’ with reassessment assuming that "
        "all conducting parts not coated, encapsulated or insulated are "
        "assumed to be capable of interconnection.",
        "Encapsulated apparatus ‘m’ (see Chapter 9). In this case the "
        "encapsulant is considered as adequate without the necessity for an "
        "IP6X enclosure, although such an enclosure will be necessary for any "
        "exposed termination facilities.",
    ]))
    b.append(note("<b>Source quirk: Zone 21 item 6.</b> The print reads "
                  "‘Flameproof enclosures ‘p’ (see Chapters 10 and 15)’ – "
                  "‘p’ where flameproof is ‘d’ in the Zone 1 list – and uses "
                  "‘providing’ rather than ‘provided’; retained."))

    return "".join(b)
