# -*- coding: utf-8 -*-
"""Chapter 10, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 226-230 (PDF pp. 247-251).

Covers the unfoliated chapter opener (history, USA status, early
development), 10.1 Standards for flameproof apparatus, 10.2 Construction
and testing requirements for flamepaths, and the heading of 10.2.1
Joints between the interior of flameproof enclosures and the external
atmosphere, including its five-item list of joint types. Prose only: no
figures, tables, equations or reference list. The chapter shell owns the
chapter h2, references and end matter. Printed quirks are kept in the
English text (chapter number 10, the German establishment name,
capitalised 'Flameproof Enclosure', superscript footnote markers with
footnote 9 uncited, the en-dash in IEC 79-1, and the mixed capitals in
the joint list), with bilingual notes; the Vietnamese text follows the
intended meaning.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note


def body_vi():
    b = []
    b.append(h3("Mở đầu chương", "Chapter opening"))

    b.append(p("<b>(BS/EN 50018 (1995))</b>"))
    b.append(note("<b>Lưu ý về trang mở đầu chương in.</b> Lớp văn bản OCR đọc "
                  "số chương là '70' và phụ đề là 'BS/EN 5001 8 (1 995)'; trang "
                  "in cho thấy chương 10 và 'BS/EN 50018 (1995)'. Bản tiếng Anh "
                  "theo trang in."))

    b.append(p("Vỏ chống cháy có lẽ là nguyên lý bảo vệ lâu đời nhất được xem "
               "xét ở Anh và châu Âu như một giải pháp phù hợp cho Vùng 1 và các "
               "khu vực ít nguy hiểm hơn, có từ trước Thế chiến thứ hai. Có "
               "nhiều tranh cãi về việc ai đã ‘phát minh’ ra nó, cả Đức và Anh "
               "đều đòi vinh dự đó. Dù sự thật chưa hoàn toàn rõ, lịch sử cho "
               "thấy nó đã phát triển trong ngành khai thác mỏ, và sự phát "
               "triển ấy diễn ra ở cả Đức và Anh. Những động lực chính dường "
               "như là Bergerwerkshaftlische Versuchstrekke ở Đức (nay gọi là "
               "BVS, một trong những tổ chức chứng nhận được công nhận tại "
               "Đức) và Safety in Mines Research Establishment ở Anh (nay gọi "
               "là Health and Safety Laboratory thuộc Health and Safety "
               "Executive [HSE]), đơn vị có liên hệ với Electrical Equipment "
               "Certification Service (EECS/BASEEFA). Dr Ing Carl Beyling đã "
               "soạn một tài liệu mô tả việc áp dụng cái sau này được gọi là "
               "‘druckfeste kapselung’ (vỏ chống cháy) cho các máy điện vào "
               "năm 1908 và đã được trao huy chương của Institution of Mining "
               "Engineers Anh quốc năm 1938 cho công trình của ông về an toàn "
               "hầm mỏ. Điều này bác bỏ mọi gợi ý về sự cạnh tranh và cho thấy "
               "mức độ hợp tác giữa Anh và Đức trong giai đoạn đó. Cũng đáng "
               "lưu ý rằng nguyên lý bảo vệ (kiểu bảo vệ) lấy chữ cái đặc "
               "trưng ‘d’ từ tên gọi tiếng Đức, dù nguồn gốc lịch sử của nó "
               "có thể nằm ở các thỏa hiệp đạt được trong quá trình xây dựng "
               "tiêu chuẩn quốc tế và các vấn đề lịch sử của tiêu chuẩn Đức, "
               "hơn là quyền sở hữu ban đầu."))
    b.append(note("<b>Lưu ý về tên cơ sở Đức.</b> Trang in ghi "
                  "'Bergerwerkshaftlische Versuchstrekke', một cách viết Đức "
                  "bất thường; giữ nguyên như bản in thay vì chuẩn hóa. Lớp "
                  "văn bản OCR đọc là 'Bergenverkshaftlische Versuchstrekke'."))

    b.append(p("Điều đáng lưu ý thêm là vỏ chống cháy (gọi là vỏ chống nổ ở "
               "Mỹ) là một trong ba nguyên lý bảo vệ duy nhất được chấp nhận "
               "cho Class 1 Division 1 tại Mỹ. Điều này tương đương với Vùng 0 "
               "và 1, vì về mặt lịch sử Mỹ không phân biệt giữa hai vùng này. "
               "Giờ đây, trong ấn bản mới nhất của Chương 5 (Điều 500) của "
               "National Electrical Code, Mỹ đã bắt đầu chấp nhận hệ thống ba "
               "Vùng châu Âu cho chất khí và hơi, và đang tích cực xem xét các "
               "nguyên lý bảo vệ khác hiện chưa được chấp nhận ở Mỹ nhưng đã "
               "được sử dụng ở châu Âu."))

    b.append(p("Sự phát triển của ‘vỏ chống cháy’ diễn ra rất nhanh sau khi "
               "việc sử dụng điện trong các hầm mỏ than được phát triển (các "
               "vấn đề công nghiệp trên mặt đất không phải là động lực chính "
               "trong những năm đầu phát triển) và sau khi người ta nhận ra "
               "rằng các máy điện quay (mô tơ điện), vốn đều dùng dc vào đầu "
               "thế kỷ hai mươi, tạo ra tia lửa có khả năng gây cháy rất cao "
               "trong hoạt động bình thường."))

    b.append(p("Lý tưởng nhất là có thể loại trừ khí quyển nổ khỏi bên trong "
               "thiết bị điện, qua đó loại bỏ nguy cơ nổ, nhưng người ta nhanh "
               "chóng nhận ra rằng cách tiếp cận đó nhìn chung không khả thi, "
               "đặc biệt xét đến sự không đáng tin cậy của thiết bị vào thời "
               "điểm đó. Điều này dẫn đến việc thường xuyên mở thiết bị để bảo "
               "trì, phá vỡ các lớp bịt kín và kéo theo khó khăn trong việc "
               "làm lại chúng một cách chắc chắn. (Điều này vẫn phần nào đúng "
               "ở một mức độ nhất định, vì người ta vẫn cho rằng việc tạo và "
               "phá vỡ một lớp bịt kín đúng chất lượng tại hiện trường một "
               "cách chắc chắn nhìn chung là không thể.) Bên cạnh đó, các máy "
               "quay và thiết bị dẫn động khác cũng có trục và thanh truyền "
               "xuyên qua vỏ bọc của thiết bị, khiến việc bịt kín ở mức độ và "
               "với độ bền yêu cầu trở nên khó khăn hơn nhiều."))

    b.append(p("Sau khi chấp nhận rằng không thể loại trừ khí quyển nổ và, nói "
               "chung, cũng không thể loại trừ nguồn gây cháy vì tia lửa phát "
               "ra bình thường trong bộ chuyển mạch và công tắc, tư duy "
               "chuyển sang một phương pháp cho phép vụ nổ bên trong khí quyển "
               "nổ và sắp xếp để nó không làm hư hại thiết bị cũng như không "
               "gây cháy khí quyển nổ bên ngoài. Rõ ràng, để chịu được vụ nổ "
               "bên trong mà không bị hư hại, vỏ bọc phải chắc chắn, dẫn đến "
               "các vỏ bọc bằng kim loại nặng (thường là đúc). Người ta phát "
               "hiện rằng mặt ngọn lửa do vụ nổ gây ra có thể trở nên vô hại "
               "khi cho nó đi qua một khe hở nhỏ: nếu kích thước khe hở có thể "
               "được đảm bảo ở một giá trị <i>tối đa</i> xác định trong suốt "
               "vụ nổ, thì thiết bị được bao bọc như vậy sẽ không gây ra nguy "
               "cơ không chấp nhận được, ngay cả khi khí quyển nổ thực sự xâm "
               "nhập vào vỏ bọc và bị gây cháy bên trong (xem Hình 10.1). Như "
               "vậy là nguyên lý vỏ chống cháy đã ra đời. Cần lưu ý rằng nói "
               "chung không quy định khe hở tối thiểu nào — khe hở quan trọng "
               "duy nhất là khe hở đạt được trong điều kiện sai lệch cực đại."))

    b.append(p("Trong những ngày đầu, tất cả vỏ chống cháy đều làm bằng kim "
               "loại và người ta đã hình thành một quan niệm sai là bắt buộc "
               "phải dùng kim loại để thực hiện chức năng của chúng, vì mục "
               "tiêu chỉ được cho là đạt được bằng cách làm nguội ngọn lửa khi "
               "nó thoát ra khỏi vỏ bọc qua khe hở. Giờ đây người ta biết điều "
               "đó không hoàn toàn đúng; hiệu ứng được chấp nhận là làm nguội "
               "khi đi ra qua khe hở mặt bích và, thêm vào đó, là sự cuốn hút "
               "nhanh các khí mát bao quanh vỏ bọc ngay khi thoát ra khỏi khe "
               "hở (xem Hình 10.1). Điều này được H. Phillips chứng minh trong "
               "bài báo trình bày tại hội nghị IEE năm 1971,¹ trong đó ông đưa "
               "ra phương pháp tính Khe hở an toàn thử nghiệm tối thiểu (MESG) "
               "bằng sử dụng hai đặc tính này. Các công trình ở châu Âu, đặc "
               "biệt là ở Đức, đã xác nhận điều đó bằng cách cho thấy vỏ bọc "
               "bằng nhựa — vốn theo định nghĩa có nhiệt dung nhỏ hơn vỏ kim "
               "loại — hoạt động về cơ bản theo cách tương tự. Kết quả là vỏ "
               "bọc nhựa hiện được chấp nhận song song với vỏ kim loại, miễn "
               "là chúng đáp ứng cùng các tiêu chí, đặc biệt vì nhựa hiện đã "
               "được phát triển có độ cứng và độ bền tương tự kim loại. Điều "
               "này làm cho kỹ thuật trở nên hấp dẫn và linh hoạt hơn nhiều về "
               "mặt thương mại."))

    b.append(p("Vì vậy, các yêu cầu đối với vỏ chống cháy là: nó phải chứa "
               "được vụ nổ bên trong của khí quyển nổ tồi nhất mà nó được "
               "thiết kế cho, mà không bị hư hại; các mối nối giữa các bộ phận "
               "của nó thông ra khí quyển bên ngoài phải có kích thước tối đa "
               "quy định; và độ bền của nó phải sao cho các mối nối đó không "
               "bị giãn rộng trong điều kiện nổ bên trong của khí quyển nổ "
               "tồi nhất mà nó được thiết kế, đến mức ngọn lửa truyền ra "
               "ngoài vỏ bọc và gây cháy khí quyển bên ngoài. Thêm vào đó, "
               "vật liệu chế tạo của nó không được bị hư hại do sự cháy bên "
               "trong liên quan đến vụ nổ của khí quyển nổ tồi nhất."))
    b.append(note("<b>Lưu ý về cách viết hoa.</b> Bản in dùng 'Flameproof "
                  "Enclosure' với chữ hoa giữa câu trong đoạn này ('Thus was "
                  "the concept of Flameproof Enclosure born' và 'The "
                  "requirements of a Flameproof Enclosure'); giữ nguyên chữ "
                  "hoa ở bản tiếng Anh."))

    b.append(p("Rõ ràng là vỏ bọc không được xuống cấp trong môi trường nơi nó "
               "được lắp đặt, nhưng đây không phải là yêu cầu riêng đối với "
               "khí quyển nổ và không nằm trong nội dung chi tiết của các yêu "
               "cầu về vỏ chống cháy; nó được xác định là điều người sử dụng "
               "phải cân nhắc khi lựa chọn thiết bị cho một vị trí cụ thể."))

    b.append(h3("10.1 Tiêu chuẩn về thiết bị chống cháy",
                "10.1 Standards for flameproof apparatus"))
    b.append(p("Phù hợp với tuổi đời của nó, nguyên lý bảo vệ đã được đề cập "
               "trong một số Tiêu chuẩn áp dụng tại Anh qua các năm; có lẽ "
               "đáng để xem xét các Tiêu chuẩn này vì chúng cho thấy sự phát "
               "triển của kỹ thuật."))
    b.append(p("Tiêu chuẩn quan trọng đầu tiên là BS 229², lần đầu được ban "
               "hành năm 1926 với các lần sửa đổi vào các năm 1929, 1940, 1946 "
               "và 1957. Giống như các Tiêu chuẩn đương thời, Tiêu chuẩn này "
               "không yêu cầu các bộ phận của vỏ bọc tiếp xúc trực tiếp với "
               "khí quyển nổ bên ngoài phải được phân loại nhiệt độ, vì nó ra "
               "đời trước hệ thống phân loại nhiệt độ bề mặt. Người sử dụng "
               "không được hướng dẫn gì về việc sử dụng liên quan đến việc "
               "gây cháy nhiệt của khí quyển nổ."))
    b.append(note("<b>Lưu ý về cách viết và số chú thích in.</b> Từ in "
                  "'significance' bị xáo trộn trong lớp văn bản OCR; bản tiếng "
                  "Anh theo trang in. Các số chú thích dạng mũ được giữ như "
                  "bản in (BS 229², BS 4683, Phần 2³, BS 5501, Phần 5⁵, "
                  "BS/EN 50018⁶, IEC 79–1⁷, IEC⁸, ISO 468 (1982)¹⁰)."))

    b.append(p("Ngoài ra, nó không cho phép các phương tiện kết nối bên ngoài "
               "nằm trong bộ phận chính bao bọc các phần của vỏ bọc, mà nhất "
               "quyết yêu cầu đặt chúng trong một hộp đấu dây riêng (xem Mục "
               "10.2). Nó cũng giới hạn vỏ bọc chỉ làm bằng kim loại, yêu cầu "
               "các sắp xếp bịt kín ren nghiêm ngặt hơn nhiều (chiều dài ren "
               "ăn khớp của một đầu nối ren trong thành vỏ bọc là 18 mm, thay "
               "vì 8 mm hiện được phép (xem Mục 10.2) và, quan trọng nhất, nó "
               "không cho phép vỏ chống cháy dùng cho cái hiện là nhóm khí, "
               "hơi và sương mù IIC. Vì vậy, ở bất cứ nơi nào có hydro hoặc "
               "axetylen, trước khi áp dụng áp suất dương nhiều năm sau đó, "
               "đã không có nguyên lý bảo vệ tiêu chuẩn nào cho thiết bị điện "
               "có khả năng gây cháy do chính hoạt động của nó. Thiết bị theo "
               "BS 229² phần lớn đã trở thành di sản lịch sử và không nên "
               "chọn để sử dụng, dù một số vẫn còn tồn tại trong các lắp đặt "
               "cũ."))

    b.append(p("BS 229² đã thực sự được thay thế vào năm 1971 bởi BS 4683, "
               "Phần 2³, bao gồm nhiều ý tưởng đang được phát triển ở châu Âu "
               "và quốc tế vào thời điểm đó. Tiêu chuẩn này rất gần với các "
               "Tiêu chuẩn châu Âu hiện hành về nội dung. Tiêu chuẩn đã đưa "
               "khái niệm vỏ bọc phi kim loại — đã rất phổ biến ở Đức — vào "
               "Anh, bổ sung các yêu cầu đối với vỏ bọc nhóm IIC (dù vẫn ngại "
               "ngùng với vỏ bọc dùng cho hỗn hợp axetylen) và giảm chiều dài "
               "ăn khớp ren của đầu nối xuống 8 mm. Tiêu chuẩn này được ban "
               "hành ngay trước thỏa thuận tạm dừng châu Âu, theo đó các quốc "
               "gia thành viên bị ngăn không được ban hành Tiêu chuẩn Quốc "
               "gia khi CENELEC⁴ đang chuẩn bị một Tiêu chuẩn song song, nên "
               "có lẽ nó đã không bao giờ ra đời. Tuy nhiên, nó là cần thiết "
               "vì thực hành chống cháy của Anh đã tụt hậu so với đối thủ "
               "cạnh tranh ở châu Âu và cần được sửa ngay. Điều này giải thích "
               "vòng đời ngắn của BS 4683, Phần 2, được thay thế tại Anh bởi "
               "BS 5501, Phần 5⁵ năm 1977 — ấn bản đầu tiên của Tiêu chuẩn "
               "châu Âu EN 50018. Tiêu chuẩn châu Âu này rất giống về nội "
               "dung với BS 4683, Phần 2³ vì Anh đã tham gia vào việc xây "
               "dựng nó song song với công việc châu Âu, và sự trao đổi ý "
               "tưởng tốt đã diễn ra. Đúng là có khác biệt liên quan đến "
               "phương pháp thử và ở những chỗ khác, nhưng không khác biệt "
               "nào dẫn đến tình huống người ta phải bày tỏ quan ngại về việc "
               "sử dụng thiết bị theo BS 4683, Phần 2, trong đó nhiều thiết bị "
               "vẫn còn tồn tại. Tuy nhiên, theo các thỏa thuận châu Âu, Tiêu "
               "chuẩn này đã bị rút lui và mọi thiết bị trong tương lai sẽ "
               "theo Tiêu chuẩn châu Âu."))

    b.append(p("Tiêu chuẩn châu Âu BS 5501, Phần 5⁵ hiện đã được thay thế "
               "bằng một ấn bản thứ hai và, không giống ấn bản đầu tiên, ấn "
               "bản này không được cấp một số BS riêng mà giữ lại số châu Âu "
               "và có tên là BS/EN 50018⁶. Ấn bản thứ hai này được xuất bản "
               "năm 1995 và có ý nghĩa rất lớn ở chỗ nó cho phép, lần đầu tiên "
               "trong nguyên lý bảo vệ này, các thiết bị thở và thoát nước "
               "không tuân thủ các yêu cầu kết cấu về kích thước của tiêu "
               "chuẩn và không có kích thước đo được nào ngoại trừ kích "
               "thước bên ngoài. Ý nghĩa của điều này là lần đầu tiên đưa vào "
               "việc tuân thủ chỉ bằng thử nghiệm, thay vì bằng quy định kích "
               "thước và thử nghiệm. Vì ấn bản thứ hai của EN 50018 hiện đang "
               "có hiệu lực, chương này sẽ đề cập đến Tiêu chuẩn đó. Tuy "
               "nhiên, như đã nêu ở trên, hầu hết khác biệt giữa nó và ấn bản "
               "đầu tiên trước đó — và thực sự là cả BS 4683, Phần 2³ — đều "
               "tương đối nhỏ."))

    b.append(p("Có thêm một Tiêu chuẩn nữa là Tiêu chuẩn Quốc tế IEC 79–1⁷. "
               "Tiêu chuẩn này rất giống BS/EN 50018⁶ nhưng chỉ mang tính tự "
               "nguyện, và ở châu Âu thì bắt buộc phải tuân thủ Tiêu chuẩn "
               "châu Âu, nên văn bản quốc tế không quan trọng bằng. Một thỏa "
               "thuận giữa cơ quan tiêu chuẩn châu Âu (CENELEC) và cơ quan "
               "tương đương quốc tế của nó (IEC⁸) yêu cầu các Tiêu chuẩn của "
               "hai cơ quan được hài hòa, và có thể kỳ vọng IEC 79–1 và "
               "BS/EN 50018⁶ sẽ tiến đến thống nhất trong những năm tới."))
    b.append(note("<b>Lưu ý về ký hiệu IEC và số chú thích.</b> Bản in viết "
                  "'IEC 79–1' với dấu gạch ngang dài giữa 79 và 1, được giữ "
                  "nguyên ở đây. Chú thích số 9 không được trích dẫn ở đâu giữa "
                  "chú thích 8 và 10 trong phần này của chương; giữ nguyên số "
                  "gốc, không đánh số lại."))

    b.append(h3("10.2 Yêu cầu về kết cấu và thử nghiệm đối với đường dẫn "
                "ngọn lửa",
                "10.2 Construction and testing requirements for flamepaths"))
    b.append(p("Các yêu cầu chi tiết về kết cấu của vỏ chống cháy hiện được "
               "đưa ra trong BS/EN 50018 (1995). Như có thể đoán trước, phần "
               "lớn Tiêu chuẩn dành để mô tả các loại mối nối giữa, ví dụ, vỏ "
               "bọc và nắp, và độ bền của vỏ bọc, vì đây là hai yếu tố mà "
               "nguyên lý bảo vệ dựa trên. Tiêu chuẩn cũng chứa các yêu cầu "
               "bổ sung cho đầu vào cáp, chẳng hạn như các đầu nối ren cũng "
               "tạo thành lối vào vỏ bọc; các thiết bị thở và thoát nước, là "
               "thay đổi chính giữa Tiêu chuẩn này và Tiêu chuẩn tiền nhiệm; "
               "và các yêu cầu bổ sung cho những thứ như vỏ bọc phi kim loại "
               "và chụp đèn khi chúng tạo thành các mối nối chống cháy (ví dụ, "
               "trong thiết bị theo BS/EN 50018⁶)."))

    b.append(h4("10.2.1 Mối nối giữa bên trong vỏ chống cháy và khí quyển "
                "bên ngoài",
                "10.2.1 Joints between the interior of flameproof enclosures "
                "and the external atmosphere"))
    b.append(p("Thực tế có năm loại mối nối được sử dụng trong vỏ chống cháy. "
               "Ngoài ra, còn có các yêu cầu đối với mối nối dùng cho trục "
               "quay, cùng với một loại mối nối bổ sung. Đó là:"))
    b.append(p("1. Mối nối mặt bích phẳng."))
    b.append(p("2. Mối nối lồng ghép (spigot)."))
    b.append(p("3. Mối nối hình trụ, mối nối thanh dẫn động và mối nối hình "
               "trụ một phần."))
    b.append(p("4. Mối nối ren."))
    b.append(p("5. Mối nối xi măng."))
    b.append(note("<b>Lưu ý về cách viết hoa trong danh sách mối nối.</b> Bản "
                  "in viết 'Threaded Joints.' và 'Cemented Joints.' với chữ J "
                  "hoa, nhưng 'Flat flange joints.', 'Spigot joints.' và "
                  "'Cylindrical joints, operating rod joints and partial "
                  "cylindrical joints.' với chữ j thường; giữ nguyên từng cách "
                  "viết ở bản tiếng Anh."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("Chapter opening", "Chapter opening"))

    b.append(p("<b>(BS/EN 50018 (1995))</b>"))
    b.append(note("<b>Note on the printed chapter opener.</b> The OCR text "
                  "layer reads '70' for the chapter number and "
                  "'BS/EN 5001 8 (1 995)' for the subtitle; the printed page "
                  "shows chapter 10 and 'BS/EN 50018 (1995)'. The English "
                  "text follows the printed page."))

    b.append(p("Flameproof enclosure is probably the oldest of the protection "
               "concepts considered in the UK and Europe as suitable for Zone "
               "1 and less hazardous areas dating back to before the Second "
               "World War. There is much controversy as to who ‘invented’ it "
               "with both Germany and the UK claiming that accolade. While "
               "the truth of the matter is not fully clear, history shows it "
               "to have developed in the mining industry and that development "
               "was done in both Germany and the UK. The prime movers appear "
               "to have been the Bergerwerkshaftlische Versuchstrekke in "
               "Germany (now known as BVS and one of the German-recognized "
               "certification bodies) and the Safety in Mines Research "
               "Establishment in the UK (now known as the Health &amp; Safety "
               "Laboratory of the Health and Safety Executive [HSE]), which "
               "is associated with the Electrical Equipment Certification "
               "Service (EECS/BASEEFA). Dr Ing Carl Beyling produced a "
               "document describing the application of what was later to "
               "become known as ‘druckfeste kapselung’ (flameproof enclosure) "
               "to electric motors in 1908 and was awarded the medal of the "
               "UK. Institution of Mining Engineers in 1938 for his work on "
               "safety in mines. This gives a lie to any suggestion of "
               "rivalry and shows the level of cooperation existing between "
               "the UK and Germany during this period. It is also worth "
               "noting that the protection concept (type of protection) takes "
               "its defining letter ‘d’ from the German title, although this "
               "may have its historical roots in compromises reached in the "
               "International Standards-making process and historical issues "
               "of German Standards than initial ownership."))
    b.append(note("<b>Note on the German establishment name.</b> The printed "
                  "page reads 'Bergerwerkshaftlische Versuchstrekke', an "
                  "unusual German form; it is retained as printed rather than "
                  "normalised. The OCR text layer read "
                  "'Bergenverkshaftlische Versuchstrekke'."))

    b.append(p("It is further worthy of note that flameproof enclosure "
               "(called explosion-proof enclosure in the USA) is one of only "
               "three protection concepts accepted for Class 1 Division 1 in "
               "the USA. This is the equivalent of Zone 0 and 1, as "
               "historically the USA did not differentiate between the two. "
               "Now, however, in the latest edition of Chapter 5 (Article "
               "500) of the National Electrical Code the USA has begun to "
               "accept the European three-Zone system for gases and vapours "
               "and is now actively considering other protection concepts "
               "currently not acceptable in the USA but used in Europe."))

    b.append(p("The development of the ‘flameproof enclosure’ followed very "
               "quickly upon the development of usage of electricity in coal "
               "mines (industrial problems on the surface not being prime "
               "mover during the early years of development) and the "
               "recognition that rotating electrical machines (electric "
               "motors), which were all dc in the early part of the twentieth "
               "century, produced highly ignition-capable sparking in normal "
               "operation."))

    b.append(p("While it would have been ideal if the explosive atmosphere "
               "could be excluded from the interior of electrical equipment, "
               "removing the explosion risk, it was rapidly recognized that "
               "such an approach was not generally feasible, particularly in "
               "the light of the unreliability of equipment at that time. "
               "This resulted in the regular opening of apparatus for "
               "maintenance, breaking any seal with the attendant difficulty "
               "of remaking it with confidence. (This is still, to a degree, "
               "the case as it is still considered that to make and break a "
               "seal of the desired quality in the field with confidence is "
               "generally not possible). In addition, such things as "
               "rotating machines and other actuating devices also have "
               "shafts and rods which penetrate the enclosure of apparatus "
               "making sealing to the required degree and with the required "
               "longevity even more difficult."))

    b.append(p("Having accepted that the explosive atmosphere could not be "
               "excluded and, in general, neither could the ignition source "
               "because of the normal sparking which goes on in commutators "
               "and switches, the thought patterns turned to a method of "
               "allowing the internal explosion of the explosive atmosphere "
               "and making arrangements for it not to damage the equipment "
               "nor cause ignition of the external explosive atmosphere. "
               "Obviously, to withstand an internal explosion without damage "
               "the enclosure had to be strong which led to heavy metal "
               "enclosures (usually cast). It was discovered that the "
               "flamefront caused by the explosion could be rendered harmless "
               "by passing it through a small gap, (if the gap size could be "
               "guaranteed to have a specific <i>maximum</i> dimension during "
               "the explosion) the apparatus so enclosed would not constitute "
               "an unacceptable risk, even if the explosive atmosphere did "
               "penetrate its enclosure and was ignited internally (see Fig. "
               "10.1). Thus was the concept of Flameproof Enclosure born. It "
               "must be noted that there is generally no minimum gap "
               "specified as the only gap that matters is that achieved in "
               "maximum deviation conditions."))

    b.append(p("In the early days, all flameproof enclosures were of metal "
               "construction and a myth developed that they had to be to "
               "perform their function, as the objective was achieved only "
               "by cooling the flame as it exited the enclosure via the gap. "
               "This is now known not to be fully true and the effect is "
               "accepted as being one of cooling while exiting through the "
               "flange gap and, in addition, rapid entrainment on exit from "
               "the gap with cool gases surrounding the enclosure (see Fig. "
               "10.1). This is demonstrated by H. Phillips in his paper to "
               "the 1971 IEE conference¹ in which he demonstrates a method "
               "of the calculation of the Minimum Experimental Safe Gap "
               "(MESG) utilizing these two characteristics. Work in Europe, "
               "and particularly in Germany, confirmed this in demonstrating "
               "that plastic enclosures which, by definition, have less heat "
               "capacity than those of metal performed in essentially the "
               "same way. As a result of this, plastic enclosures are now "
               "accepted alongside their metallic counterparts provided they "
               "satisfy the same criteria, particularly as plastics have now "
               "been developed which exhibit similar rigidity and strength "
               "as metal. This gives the technique much more commercial "
               "attractiveness and flexibility."))

    b.append(p("The requirements of a Flameproof Enclosure are therefore as "
               "follows: it must contain an internal explosion of the worst "
               "case explosive atmosphere for which it is designed, without "
               "damage; the joints between its parts which access the "
               "external atmosphere must be of specified maximum dimensions "
               "and its strength must be such that those joints do not widen "
               "under conditions of internal explosion of the worst case "
               "explosive atmosphere for which it is designed, to a point "
               "where the flame is transmitted outside the enclosure and "
               "ignites the external atmosphere. In addition, its material "
               "of construction must not be damaged by the internal burning "
               "associated with an internal explosion of the worst case "
               "explosive atmosphere."))
    b.append(note("<b>Note on capitalisation.</b> The printed text uses "
                  "'Flameproof Enclosure' with capital letters mid-sentence "
                  "in this passage ('Thus was the concept of Flameproof "
                  "Enclosure born' and 'The requirements of a Flameproof "
                  "Enclosure'); the capitals are retained."))

    b.append(p("Obviously, the enclosure must not deteriorate in the "
               "environment in which it is installed, but this is not a "
               "specific explosive atmosphere requirement and is not "
               "included in the detail of the flameproof enclosure "
               "requirements, but is identified as something the user must "
               "consider when selecting equipment for a particular location."))

    b.append(h3("10.1 Standards for flameproof apparatus",
                "10.1 Standards for flameproof apparatus"))
    b.append(p("As befits its age, the protection concept has been addressed "
               "in several Standards applicable in the UK over the years, and "
               "it is probably worthwhile to address these because they "
               "identify the development of the technique."))
    b.append(p("The first Standard of significance was BS 229² which was "
               "first issued in 1926 with revisions in 1929, 1940, 1946 and "
               "1957. This Standard did not require, in common with its "
               "contemporary Standards, that the parts of enclosures in "
               "direct contact with an external explosive atmosphere be "
               "temperature classified as it pre-dated the surface "
               "temperature classification system. Users were given no "
               "guidance on usage in respect of thermal ignition of an "
               "explosive atmosphere."))
    b.append(note("<b>Note on printed spellings and footnote markers.</b> "
                  "The printed word 'significance' was garbled in the OCR "
                  "text layer; the English text follows the printed page. "
                  "Superscript footnote numbers are retained as printed "
                  "(BS 229², BS 4683, Part 2³, BS 5501, Part 5⁵, "
                  "BS/EN 50018⁶, IEC 79–1⁷, IEC⁸, ISO 468 (1982)¹⁰)."))

    b.append(p("In addition, it did not permit facilities for external "
               "connection to be within the main component enclosing parts "
               "of the enclosure, but insisted they be in a separate terminal "
               "box (see Section 10.2). It also limited enclosures to those "
               "made of metal, required far more severe glanding arrangements "
               "(the engaged thread of a gland within the enclosure wall was "
               "18 mm, rather than the now permitted 8 mm (see Section 10.2) "
               "and, most importantly, it did not allow flameproof enclosures "
               "for use in what is now Group IIC gases, vapours and mists. "
               "Therefore, wherever hydrogen or acetylene was present, there "
               "was no Standard protection concept for electrical equipment "
               "which was, by its operation, ignition capable until "
               "pressurization came into use much later. BS 229² equipment is "
               "largely now historic and should not be selected for use, "
               "although some still exists in older installations."))

    b.append(p("BS 229² was effectively replaced in 1971 by BS 4683, Part 2³ "
               "which included many of the ideas at that time being developed "
               "in Europe and internationally. This Standard was very close "
               "to the current European Standards in content. The Standard "
               "introduced the concept of non-metallic enclosures, already "
               "commonplace in Germany, to the UK, added requirements for "
               "Group IIC enclosures (although it still baulked at enclosures "
               "for acetylene mixtures) and reduced the gland thread "
               "engagement to 8 mm. This Standard was produced shortly before "
               "the European standstill agreement which prevented member "
               "states from issuing National Standards where CENELEC⁴ was "
               "preparing a parallel Standard or it may never have appeared. "
               "It was, however, necessary as UK flameproof practice had "
               "fallen behind competition in Europe and urgent correction was "
               "necessary. This explains the short life of BS 4683, Part 2 "
               "which was superseded in the UK by BS 5501, Part 5⁵ in 1977, "
               "this being the first edition of the European Standard, EN "
               "50018. This European Standard was very similar in content to "
               "BS 4683, Part 2³ as the UK was involved in its production in "
               "parallel to the European work, and a good degree of cross "
               "fertilization occurred. It is true that differences exist in "
               "relationship to testing methods and elsewhere but none of "
               "these would lead to a situation where concern would be "
               "expressed over the use of BS 4683, Part 2 apparatus, much of "
               "which still exists. In accordance with European agreements, "
               "however, it is withdrawn and all future equipment will be to "
               "the European Standard."))

    b.append(p("The European Standard, BS 5501, Part 5⁵ has now been "
               "superseded by a second edition and, unlike the first edition, "
               "is not given a separate BS number but retains its European "
               "number and is titled BS/EN 50018⁶. This second edition was "
               "published in 1995 and was very significant in that it "
               "permitted breathing and draining devices, which did not "
               "comply with the dimensional constructional requirements of "
               "the standard and, did not have any measurable dimensions "
               "except the external size, in the protection concept for the "
               "first time. The significance of this is the introduction for "
               "the first time of compliance by test only, rather than by "
               "dimensional specification and test. As the second edition of "
               "EN 50018 is now current, this chapter will address that "
               "Standard. As already stated, however, most of the differences "
               "between this and its preceding first edition and, indeed, "
               "BS 4683, Part 2³ are relatively small."))

    b.append(p("There is a further Standard in existence which is the "
               "International Standard, IEC 79–1⁷. This Standard is very "
               "similar to BS/EN 50018⁶ but is voluntary only and in Europe "
               "it is necessary to comply with the European Standard, so the "
               "international document is not so important. An agreement "
               "between the European Standards body (CENELEC) and its "
               "international equivalent (IEC⁸) requires that the Standards "
               "of the two bodies are harmonized and IEC 79–1 and BS/EN "
               "50018⁶ may be expected to come together in the next few "
               "years."))
    b.append(note("<b>Note on the IEC designation and footnote numbers.</b> "
                  "The printed 'IEC 79–1' uses a long dash between 79 and 1, "
                  "as reproduced here. Footnote 9 is not cited anywhere "
                  "between footnotes 8 and 10 in this part of the chapter; "
                  "the original numbering is kept and not renumbered."))

    b.append(h3("10.2 Construction and testing requirements for flamepaths",
                "10.2 Construction and testing requirements for flamepaths"))
    b.append(p("The detailed requirements for the construction of flameproof "
               "enclosures are currently given in BS/EN 50018 (1995). As may "
               "be expected, much of the Standard is given over to "
               "description of the types of joint between, for example, "
               "enclosure and cover and enclosure strength as these are the "
               "two factors upon which the protection concept is based. It "
               "also contains additional requirements for cable entries, "
               "such as glands which also form entries into the enclosure, "
               "breathing and draining devices, which are the main change "
               "between this Standard and its predecessor, and additional "
               "requirements for such things as non-metallic enclosures and "
               "lamp caps where these form flameproof joints (e.g., in "
               "apparatus to BS/EN 50018⁶)."))

    b.append(h4("10.2.1 Joints between the interior of flameproof enclosures "
                "and the external atmosphere",
                "10.2.1 Joints between the interior of flameproof enclosures "
                "and the external atmosphere"))
    b.append(p("There are effectively five types of joint used in flameproof "
               "enclosures. In addition, there are requirements for joints "
               "used for rotating shafts together with an additional type of "
               "joint. These are:"))
    b.append(p("1. Flat flange joints."))
    b.append(p("2. Spigot joints."))
    b.append(p("3. Cylindrical joints, operating rod joints and partial "
               "cylindrical joints."))
    b.append(p("4. Threaded Joints."))
    b.append(p("5. Cemented Joints."))
    b.append(note("<b>Note on capitalisation in the joint list.</b> The "
                  "printed list gives 'Threaded Joints.' and 'Cemented "
                  "Joints.' with a capital J, but 'Flat flange joints.', "
                  "'Spigot joints.' and 'Cylindrical joints, operating rod "
                  "joints and partial cylindrical joints.' with a lowercase "
                  "j; all are reproduced as printed."))
    return "".join(b)
