# -*- coding: utf-8 -*-
"""Chapter 12, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 296-301 (PDF pp. 317-322).

Covers the chapter opener, 12.1 The situation in regard to standardization,
12.2 Basic construction requirements, 12.2.1 Construction of enclosures,
12.2.2 Terminals and connection facilities, and the opening paragraph of
12.2.3 Separation of conducting parts. Figures 12.1 and 12.2 sit at their
printed position on printed p.300, between the lead-in to internal
connections and the numbered list of internal connection methods.
The chapter shell owns the chapter h2, the references and the end matter.

Printed quirks are kept in the English text (the misspelled German term,
the missing 'as', the superscript footnote markers, the en dash in
'IEC 79-7', the lowercase 'part', the stray comma, the run-on colon list,
the mixed 'Figure'/'Fig.' references, the 'Screw head'/'Screwhead' labels
and the 'eylet' spelling) with bilingual notes; the Vietnamese follows the
intended meaning. This is an unofficial study translation. The source PDF
is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig12_a as FA


def body_vi():
    b = []

    # Printed p.296. The shell owns the chapter h2; the module owns the
    # printed subtitle line and the chapter-opening prose.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("<b>(BS/EN 50019 (1994))</b>"))
    b.append(p("Nguyên lý bảo vệ (kiểu bảo vệ) an toàn tăng cường là một "
               "nguyên lý dự định dùng cho Vùng 1 và các vùng ít nguy hiểm "
               "hơn. Đây là một phát triển của Đức (erhohtesichereit), giải "
               "thích việc dùng 'e' làm ký hiệu nguyên lý của nó. An toàn "
               "tăng cường không chiếm vị trí đáng kể trong tư duy ở Anh "
               "trước năm 1970 và chỉ trở nên quan trọng khi đó vì tác động "
               "đối với thái độ của Anh do tầm quan trọng ngày càng tăng của "
               "khía cạnh châu Âu xuất hiện vào thời điểm Hiệp hội Mậu dịch "
               "Tự do Châu Âu (EFTA), mà Anh là thành viên trước khi gia "
               "nhập Liên minh Châu Âu (EU). Nó càng trở nên quan trọng hơn "
               "trong tư duy ở Anh khi chính Anh gia nhập EU."))
    b.append(note("<b>Lưu ý về từ tiếng Đức trong bản in.</b> Bản in ghi "
                  "'(erhohtesichereit)' — không có dấu umlaut và viết "
                  "'sichereit' thay vì 'sicherheit' (tức là từ định viết "
                  "tiếng Đức chỉ an toàn tăng cường). Cách viết này được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt theo "
                  "nghĩa định viết."))
    b.append(p("Đây là kiểu bảo vệ trong đó, dù không ngăn được sự xâm nhập "
               "của bầu khí quyển nổ vào vỏ bọc, thiết bị không đánh lửa, "
               "không tạo hồ quang hay trở nên quá nóng trong vận hành "
               "bình thường và, thêm vào đó, có chất lượng sao cho khó có "
               "khả năng bị hỏng theo cách khiến nó có khả năng gây cháy "
               "nổ. Độ an toàn chống lỗi này được tăng cường thêm nhờ sự "
               "bảo vệ của vỏ bọc khỏi môi trường xung quanh, giảm nguy cơ "
               "các điều kiện môi trường ảnh hưởng bất lợi đến hoạt động "
               "của nó. Tuy nhiên, kiểu bảo vệ này nhạy cảm hơn nhiều với "
               "các thiết bị bảo vệ điện (cầu chì, cầu dao, v.v.) so với "
               "các kiểu bảo vệ khác đã xem xét cho đến nay, vì bất kỳ lỗi "
               "nào (ví dụ, ngắn mạch bên trong, hỏng kết nối, v.v.) đều có "
               "khả năng làm nó có khả năng gây cháy nổ. Do đó, một phần "
               "của sự bảo vệ phụ thuộc vào khoảng thời gian mà tình trạng "
               "như vậy có thể tồn tại trước khi các thiết bị bảo vệ tác "
               "động."))
    b.append(p("Đã có nhiều e ngại ở Anh về việc chấp nhận an toàn tăng "
               "cường làm nguyên lý bảo vệ phù hợp cho Vùng 1 và các vùng "
               "ít nguy hiểm hơn, đặc biệt đối với những thứ như máy quay "
               "và đèn chiếu sáng, vì các yêu cầu đối với nguyên lý bảo vệ "
               "trong Tiêu chuẩn Quốc gia của Đức (VDE 0171) dường như, đối "
               "với nhiều người, không tăng đáng kể so với các yêu cầu mà "
               "Tiêu chuẩn Anh áp dụng cho thiết bị công nghiệp tiêu chuẩn "
               "loại đó ở Anh. Vẫn còn nhiều e ngại đáng kể đối với máy điện "
               "quay, và vấn đề này được đề cập sau trong chương này."))
    b.append(note("<b>Lưu ý về cụm 'such things a rotating machines'.</b> "
                  "Bản in thiếu 'as' sau 'things'. Cụm này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt dịch theo nghĩa "
                  "'những thứ như máy quay'."))
    # A4 (printed p.296) continues as B1 (printed p.297) with no intervening
    # figure; the two halves are joined into one printed paragraph.
    b.append(p("Dù có sự e ngại này, người ta vẫn chấp nhận rằng an toàn "
               "tăng cường sẽ trở thành một nguyên lý bảo vệ tiêu chuẩn ở "
               "Châu Âu và trên khắp thế giới, và việc loại trừ nó ở Anh vì "
               "những lý do kỹ thuật, đối với đa số người ở Anh, không "
               "thuyết phục (không có bằng chứng thực tế nào vào thời điểm "
               "đó cho thấy mức độ bảo vệ của nó quá thấp, mà đúng hơn là "
               "cách tiếp cận lịch sử của Anh quá cao) chỉ làm tổn hại ngành "
               "sản xuất của Anh. Người ta cũng lưu ý rằng một Tiêu chuẩn "
               "Quốc tế (IEC 79–7 (1969)¹) có khả năng được hầu hết các quốc "
               "gia trên thế giới chấp nhận."))
    b.append(note("<b>Lưu ý về các ký hiệu chú thích dạng mũ và dấu gạch "
                  "ngang.</b> Bản in dùng các ký hiệu ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ¹⁰ "
                  "dạng mũ ngay sau tên tiêu chuẩn, đôi khi nằm trong dấu "
                  "ngoặc đóng (ví dụ '(IEC 79–7 (1969)¹)', '(BS 4683, Phần "
                  "4²)', 'BS/EN 50019 (1994)⁴', 'BS/EN 60529⁵', 'BS 4999 "
                  "part 105⁶', 'BS/EN 50014⁷', 'BS/EN 50018⁸' và 'BS 5901 "
                  "(1980)¹⁰'). Lớp văn bản OCR đọc nhầm thành dấu nháy đơn, "
                  "dấu sao hoặc chữ số thường (ví dụ 'IEC 79-7 (1969)'', "
                  "'Part 4*', '500147' và 'BS/EN 50018*'); bản in dùng dấu "
                  "gạch ngang dài trong '79–7'. Các dạng in được giữ "
                  "nguyên."))

    b.append(h3("12.1 Tình hình liên quan đến việc chuẩn hóa",
                "12.1 The situation in regard to standardization"))
    b.append(p("Anh đã chấp nhận nguyên lý bảo vệ an toàn tăng cường và một "
               "Tiêu chuẩn Quốc gia đã được ban hành năm 1973 (BS 4683, "
               "Phần 4²). Tiêu chuẩn này nhanh chóng bị lỗi thời bởi BS 5501 "
               "Phần 6 (1977)³ (là ấn bản đầu tiên của Tiêu chuẩn Châu Âu, "
               "EN 50019), và cả hai Tiêu chuẩn này hiện đều đã bị lỗi thời "
               "bởi BS/EN 50019 (1994)⁴, là ấn bản thứ hai của Tiêu chuẩn "
               "Châu Âu và trên thực tế sẽ là Tiêu chuẩn mà các thiết bị "
               "tương lai được chế tạo theo. Vì vậy, chương này sẽ dựa trên "
               "các yêu cầu của BS/EN 50019."))

    b.append(h3("12.2 Yêu cầu cơ bản về cấu tạo",
                "12.2 Basic construction requirements"))
    b.append(p("Độ an toàn cơ bản của thiết bị an toàn tăng cường nằm ở "
               "chính cấu tạo của thiết bị và ở các hạn chế đối với các "
               "loại thiết bị mà nguyên lý bảo vệ này áp dụng được. Các "
               "hạn chế đó là:"))
    b.append(p("1. Thiết bị không được tạo hồ quang hay đánh lửa hoặc sinh "
               "ra bề mặt nóng có khả năng gây cháy nổ trong vận hành bình "
               "thường"))
    b.append(p("2. Không thiết bị nào vận hành ở điện áp nguồn lớn hơn 11 kV "
               "rms, hoặc sinh ra bên trong điện áp vượt quá giá trị này, "
               "có thể được bảo vệ theo nguyên lý bảo vệ này."))
    b.append(p("3. Thiết bị mà cấu tạo của các linh kiện không thể được xác "
               "định theo cách cho phép tuân thủ các yêu cầu của nguyên lý "
               "bảo vệ, hoặc không thể tuân thủ do cấu tạo của chúng (ví "
               "dụ, các thiết bị bán dẫn) không thể được xử lý theo nguyên "
               "lý bảo vệ này. Do đó, an toàn tăng cường thường không áp "
               "dụng được cho thiết bị đo lường."))
    b.append(p("Điều trên có nghĩa là nguyên lý bảo vệ được ứng dụng nhiều "
               "nhất trong các thiết bị như hộp kết nối, đèn chiếu sáng, "
               "máy quay, máy biến áp, ắc quy, thiết bị gia nhiệt điện trở "
               "và thiết bị đo lường (đồng hồ cơ bản, v.v.)."))

    b.append(h4("12.2.1 Cấu tạo của vỏ bọc",
                "12.2.1 Construction of enclosures"))
    b.append(p("Vỏ bọc cần tuân thủ các yêu cầu chung đối với khu vực nguy "
               "hiểm (xem Chương 8), nhưng vì bản chất của nguyên lý bảo vệ "
               "này, chúng phải đáp ứng thêm các yêu cầu bổ sung."))
    b.append(p("Như đã nêu trước đó, nguyên lý bảo vệ dựa rất nhiều vào việc "
               "loại trừ môi trường bên ngoài (giữ cho thời tiết không xâm "
               "nhập nhưng không phải khí), và vì mục đích này, vỏ bọc phải "
               "có mức bảo vệ ít nhất là IP54 theo BS/EN 60529⁵ (Như ở "
               "những nơi khác, phương pháp xác định mức IP đối với máy điện "
               "quay hơi khác và BS 4999 part 105⁶ được dùng thay cho "
               "BS/EN 60529⁵ cho các máy đó). Khi vỏ bọc chỉ chứa dây dẫn "
               "và linh kiện được cách điện, thay vì các bộ phận mang điện "
               "trần, độ kín của vỏ bọc có thể giảm xuống IP44. Việc giảm "
               "thêm là được phép nếu các lỗ thông hơi hoặc thoát nước là "
               "cần thiết để thiết bị hoạt động tin cậy. Trong những "
               "trường hợp đó, IP44 được chấp nhận đối với vỏ bọc chứa các "
               "bộ phận mang điện trần và IP24 đối với vỏ bọc chỉ chứa dây "
               "dẫn và linh kiện được cách điện. Trong những trường hợp sau "
               "này, để dùng được các mức IP thấp hơn, vị trí của các lỗ là "
               "rất quan trọng và thiết bị sẽ phải chịu các điều kiện lắp "
               "đặt làm giảm thiểu khả năng xâm nhập của chất lỏng hoặc vật "
               "lạ rắn tại vị trí lắp đặt của nó."))
    b.append(note("<b>Lưu ý về chữ 'part' viết thường.</b> Bản in ghi "
                  "'BS 4999 part 105⁶' với chữ 'part' viết thường, dù ở "
                  "những chỗ khác tiêu chuẩn này được trích dẫn là "
                  "'BS 4999 Part 105'. Cách viết này được giữ nguyên theo "
                  "bản in."))
    b.append(p("Các yêu cầu trở nên phức tạp hơn khi nguyên lý bảo vệ này "
               "được dùng cùng với an toàn nội tại (xem Chương 13 thảo luận "
               "về an toàn nội tại), như đôi khi xảy ra khi cần các thiết bị "
               "giám sát bên trong (ví dụ, cảm biến nhiệt độ trong cuộn dây "
               "máy quay) để đảm bảo ngắt sớm khi có sự cố. Rõ ràng là cấu "
               "tạo thực tế của thiết bị phải sao cho an toàn nội tại không "
               "bị suy giảm, nhưng có một điểm cụ thể mà các ảnh hưởng bên "
               "ngoài có thể tạo ra sự suy giảm đó. Đó là nơi các kết nối "
               "bên ngoài của phần an toàn tăng cường của thiết bị được "
               "thực hiện ở cùng một vị trí (hộp đấu dây, v.v.) với các "
               "kết nối bên ngoài của an toàn nội tại. Trong những trường "
               "hợp này, cần có một nắp bên trong có mức bảo vệ ít nhất "
               "IP30 cho các phương tiện kết nối của an toàn tăng cường, và "
               "cần có cảnh báo để đảm bảo nắp này không bị tháo ra khi nắp "
               "ngoài đã tháo và các đầu nối an toàn tăng cường còn có "
               "điện, hoặc khi các mạch an toàn nội tại được nối vào các "
               "mạch bên ngoài. Việc áp dụng không chủ ý các mức điện áp có "
               "trong hầu hết thiết bị an toàn tăng cường có thể làm hỏng "
               "một hệ thống lắp đặt an toàn nội tại theo cách không thể "
               "nhận thấy và có thể gây nguy hiểm, không chỉ trong hệ thống "
               "lắp đặt cụ thể đó mà còn trong các hệ thống lắp đặt an toàn "
               "nội tại khác dùng chung phương tiện với nó."))
    b.append(p("Những vỏ bọc và nắp này cần được cố định bằng các bộ phận "
               "gia cố đặc biệt như mô tả trong Chương 8."))

    b.append(h4("12.2.2 Cọc đấu nối và phương tiện kết nối",
                "12.2.2 Terminals and connection facilities"))
    # C4 (printed p.298) continues as D1 (printed p.299) with no intervening
    # figure; the two halves are joined into one printed paragraph.
    b.append(p("Tất cả các kết nối điện, cả những kết nối bên trong thiết bị "
               "lẫn những kết nối để nối dây dẫn điện bên ngoài, đều quan "
               "trọng trong nguyên lý này vì bất kỳ sự hỏng nào, dù chỉ một "
               "phần, của một kết nối cũng có thể gây đánh lửa. Trong số "
               "các kết nối điện có thể có cho chính dây dẫn bên ngoài, chỉ "
               "có các cọc đấu nối (terminal) được đề cập cụ thể với các "
               "yêu cầu chi tiết riêng phải đáp ứng để đảm bảo độ tin cậy "
               "của chúng. Việc sử dụng chung phích cắm và ổ cắm không được "
               "nhắc đến cụ thể trong bất kỳ Tiêu chuẩn nào cho nguyên lý "
               "bảo vệ này nhưng, dù điều này có thể được hiểu là loại trừ "
               "việc dùng chúng, một sự nới lỏng đối với các yêu cầu chung "
               "về phích cắm và ổ cắm trong trường hợp bộ ắc quy (xem "
               "BS/EN 50014⁷ và Chương 8) cho thấy chúng được chấp nhận miễn "
               "là đáp ứng các yêu cầu của BS/EN 50014 và các phương tiện "
               "kết nối mà chúng cung cấp cho dây dẫn đáp ứng các yêu cầu "
               "của an toàn tăng cường (hoặc là các cọc đấu nối, hoặc là "
               "các kết nối bên trong khi phích cắm và/hoặc ổ cắm được cấp "
               "cùng với cáp cố định)."))
    b.append(note("<b>Lưu ý về dấu phẩy trước ngoặc đơn.</b> Bản in có dấu "
                  "phẩy sau 'battery assemblies' trước cụm '(see BS/EN "
                  "50014⁷ and Chapter 8)'. Dấu phẩy này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt bỏ dấu phẩy theo "
                  "cách diễn đạt tự nhiên."))
    b.append(p("Có thể nhớ lại rằng các yêu cầu chung đối với phích cắm và "
               "ổ cắm là chúng phải được liên khóa, sao cho bất kỳ nỗ lực "
               "tách chúng nào cũng cắt điện nguồn của chúng, hoặc được cố "
               "định với nhau bằng các bộ phận gia cố đặc biệt và có các "
               "cảnh báo phù hợp trên thiết bị chống việc tách ra khi còn "
               "có điện. Cũng cần nhớ rằng đối với dòng vận hành không vượt "
               "quá 10 A rms xoay chiều hoặc một chiều, ở điện áp nhỏ hơn "
               "250 V rms xoay chiều hoặc 60 V một chiều, các yêu cầu nêu "
               "trên có thể được bỏ qua, với điều kiện là phần của cặp kết "
               "nối còn có điện sau khi tách là ổ cắm; mạch được cắt trước "
               "khi các chân phích cắm tách khỏi ổ cắm để đảm bảo mọi hồ "
               "quang được dập tắt trước khi tách hoàn toàn, và cụm kết nối "
               "vẫn chống cháy theo BS/EN 50018⁸ trong thời gian dập hồ "
               "quang. Ngoài ra, các tiếp điểm của ổ cắm vẫn còn có điện "
               "cần được bảo vệ để ngăn gây cháy. Yêu cầu sau này thường "
               "được đáp ứng bằng cách bố trí ổ cắm sao cho nó là một vỏ "
               "bọc chống cháy sau khi phích cắm đã được rút ra, hoặc trong "
               "trường hợp đó nó tạo thành một vỏ bọc an toàn tăng cường. "
               "Trong cả hai trường hợp, cần lắp các bộ phận tự động chuyển "
               "động vào ổ cắm để hoàn thiện vỏ bọc sau khi rút phích cắm."))
    b.append(note("<b>Lưu ý về khoảng cách giữa số và đơn vị.</b> Bản in ghi "
                  "'10 A rms ac or dc' và '250 V rms ac or 60 V dc' có dấu "
                  "cách; lớp văn bản OCR đọc nhầm dạng đầu thành '10Arms'. "
                  "Cách ghi của bản in được giữ nguyên."))
    b.append(p("Các cọc đấu nối dùng cho kết nối bên trong hoặc bên ngoài, "
               "kể cả những cọc cho phép nối dây dẫn vào phích cắm và ổ "
               "cắm, cần được chế tạo sao cho chúng: được cố định đủ chắc "
               "để đảm bảo các ứng suất (như ứng suất sinh ra khi siết vít) "
               "không ảnh hưởng bất lợi đến kết nối của cọc với các mạch "
               "bên trong; và các linh kiện không có khả năng làm hỏng dây "
               "dẫn bên ngoài được nối vào chúng bằng những thứ như nối "
               "trực tiếp vào vít tạo áp lực kết nối hoặc bất kỳ bề mặt sắc "
               "nhọn nào trên các bộ phận của chúng; và vẫn đáp ứng được "
               "các yêu cầu này ngay cả khi nối dây dẫn bện. Được phép dùng "
               "đầu cos ép chặt (ferrule) trong trường hợp dây dẫn bện và "
               "vít của cọc đấu nối có thể ép trực tiếp vào đầu cos đó, "
               "nhưng điều này không được phép đối với dây dẫn bện không "
               "có đầu cos."))
    b.append(note("<b>Lưu ý về dãy yêu cầu sau dấu hai chấm.</b> Bản in dùng "
                  "dấu hai chấm để đưa vào một chuỗi yêu cầu không có số "
                  "thứ tự, khiến câu khá khó đọc. Bản tiếng Anh giữ nguyên "
                  "cấu trúc này; bản tiếng Việt thêm dấu chấm phẩy để dễ "
                  "theo dõi mà không bỏ ý nào."))
    b.append(p("Khi nhiều hơn một dây dẫn được đấu vào một cọc (một tình "
               "huống bất thường cần tránh tối đa), số lượng dây dẫn tối "
               "đa có thể đấu vào một cọc cần được quy định trong từng "
               "trường hợp. Hình 12.1 cho thấy một ví dụ về cọc đấu nối "
               "được chấp nhận cho một dây dẫn đơn và Hình 12.2 cho cọc "
               "đấu nối nhiều dây. Miếng đệm trung gian giữa vít và dây "
               "dẫn là không cần thiết khi dây dẫn được lắp đầu cos ép "
               "chặt."))
    b.append(note("<b>Lưu ý về cách viết 'Figure' và 'Fig.'.</b> Bản in viết "
                  "'Figure 12.1' đầy đủ nhưng 'Fig. 12.2' viết tắt trong "
                  "cùng một câu. Cả hai được giữ nguyên theo bản in."))
    b.append(p("Ngoài việc dùng các phương tiện đã mô tả cho kết nối bên "
               "ngoài, các kết nối bên trong có thể được thực hiện bằng:"))

    # Printed p.300: Figs 12.1 and 12.2 sit above the numbered list.
    b.append(fig(1, FA.fig_f1201()))
    b.append(fig(2, FA.fig_f1202()))
    b.append(note("<b>Lưu ý về nhãn trong Hình 12.1 và Hình 12.2.</b> Bản in "
                  "dùng 'Screw head' (hai từ) trong Hình 12.1 nhưng "
                  "'Screwhead' (một từ) trong Hình 12.2. Sự không nhất quán "
                  "này được giữ nguyên trong bản vẽ lại."))
    b.append(p("1. bất kỳ dạng kết nối vặn vít hoặc bắt bulông nào không làm "
               "hỏng dây dẫn, cho kết nối điện tốt và được khóa chống lỏng "
               "(xem Hình 12.3);"))
    b.append(p("2. các kết nối ép chặt, như những kết nối dùng đầu cos ép, "
               "trong đó các dây dẫn được đặt cùng nhau trong đầu cos và "
               "được cố định bằng một lần ép duy nhất, hoặc riêng biệt ở "
               "mỗi đầu và mỗi dây được cố định bằng một lần ép riêng (xem "
               "Hình 12.4);"))
    b.append(p("3. các kết nối hàn đồng hoặc hàn;"))
    b.append(p("4. các kết nối hàn thiếc, trong đó mối nối không được để "
               "chính lớp thiếc chịu lực vì độ bền cơ học thấp của các mối "
               "nối dạng này."))
    b.append(note("<b>Lưu ý về cách viết 'eylet'.</b> Chú thích và phần ghi "
                  "chú của Hình 12.3 viết 'eylet' (không phải 'eyelet'), và "
                  "cách viết đó cũng xuất hiện trong nhãn 'Spade/eylet "
                  "terminal' của Hình 12.4. Cách viết của bản in được giữ "
                  "nguyên."))

    b.append(h4("12.2.3 Ngăn cách các bộ phận dẫn điện",
                "12.2.3 Separation of conducting parts"))
    # E3 (printed p.300) continues as F1 (printed p.301); joined across the
    # intervening all-figure page in the same printed paragraph.
    b.append(p("Vì vỏ bọc không được bịt kín chống sự xâm nhập của không khí "
               "bên ngoài, vốn có thể chứa tạp chất ẩm và, dĩ nhiên, khí, "
               "hơi và sương mù dễ cháy, nên có khả năng xảy ra sự phá vỡ "
               "điện của không khí giữa các bộ phận dẫn điện trần riêng "
               "biệt hoặc sự phá vỡ bề mặt của bất kỳ vật liệu cách điện nào "
               "ngăn cách và/hoặc đỡ các dây dẫn. Để tránh khả năng này, "
               "các dây dẫn mang điện trần được yêu cầu phải được ngăn cách "
               "bằng những khoảng cách tối thiểu nhất định trong không khí, "
               "và những khoảng cách này được gọi là khe hở (clearance). "
               "Ngoài ra, khi các bộ phận mang điện trần — và chúng có thể "
               "chỉ là đầu trần của một dây dẫn được cách điện tại vị trí "
               "nối vào cọc đấu nối — được ngăn cách bằng bề mặt của vật "
               "liệu cách điện, vật liệu cách điện phải có chất lượng nhất "
               "định, và khoảng cách dọc theo bề mặt của nó phải ít nhất "
               "bằng một giá trị tối thiểu quy định, gọi là khoảng cách rò "
               "(creepage distance). Chất lượng cách điện được xác định bằng "
               "các phép đo chỉ số theo dõi so sánh (CTI), theo "
               "BS 5901 (1980)¹⁰, là phép đo xác định khả năng của bề mặt "
               "cách điện duy trì các tính chất của nó khi có chất gây ô "
               "nhiễm."))
    b.append(note("<b>Lưu ý về vị trí của ký hiệu chú thích ¹⁰.</b> Bản in đặt "
                  "¹⁰ ngay sau dấu ngoặc đóng của '(1980)', tức là "
                  "'BS 5901 (1980)¹⁰', không có dấu ngoặc quanh số chú "
                  "thích. Vị trí này được giữ nguyên."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.296. The shell owns the chapter h2; the module owns the
    # printed subtitle line and the chapter-opening prose.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("<b>(BS/EN 50019 (1994))</b>"))
    b.append(p("The protection concept (type of protection) of increased "
               "safety is one intended for use in Zone 1 and less hazardous "
               "areas. It is a German development (erhohtesichereit) which "
               "explains the use of 'e' as its concept symbol. Increased "
               "safety did not figure significantly in UK thinking before "
               "1970 and only became important then because of the effect on "
               "UK attitudes produced by the increasing importance of the "
               "European dimension emerging at the time of the European "
               "Free Trade Association (EFTA), of which the UK was a member "
               "prior to its entry into the European Union (EU). It gained "
               "further importance in UK thinking with the UK's entry into "
               "the EU itself."))
    b.append(note("<b>Note on the German term in the print.</b> The print "
                  "reads '(erhohtesichereit)' - no umlaut, and 'sichereit' "
                  "rather than the expected 'sicherheit' (the intended "
                  "German term for increased safety). The printed spelling "
                  "is retained in English; the Vietnamese follows the "
                  "intended meaning."))
    b.append(p("It is a type of protection where, even though the ingress of "
               "an explosive atmosphere into the enclosure is not prevented, "
               "the apparatus does not spark, arc or become excessively hot "
               "in normal operation and, in addition, is of such quality "
               "that it is unlikely to become faulty in a way which would "
               "make it ignition capable. This security from fault is "
               "further increased by enclosure protection from its "
               "environment, reducing the risk of environmental conditions "
               "adversely affecting its operation. The protection, however, "
               "is much more sensitive to electrical protection devices "
               "(fuses, circuit breakers, etc.) than the other types of "
               "protection so far considered as any fault (e.g., internal "
               "short circuit, connection failure, etc.) is likely to make "
               "it ignition capable. Therefore part of the protection "
               "depends upon the length of time for which such a situation "
               "can exist prior to the protective devices operating."))
    b.append(p("There were many misgivings in the UK concerning the adoption "
               "of increased safety as a protection concept suitable for "
               "Zone 1 and less hazardous areas, particularly for such "
               "things a rotating machines and luminaires, as the "
               "requirements for the protection concept in the German "
               "National Standard (VDE 0171) did not, to many, appear to "
               "offer a significant increase in the requirements applied by "
               "British Standards to Standard industrial equipment of these "
               "types in UK. There is still considerable concern in respect "
               "of rotating electrical machines and this is dealt with later "
               "in this chapter."))
    b.append(note("<b>Note on 'such things a rotating machines'.</b> The "
                  "print omits 'as' after 'things'. The wording is retained "
                  "in English; the Vietnamese follows the intended sense "
                  "('such things as rotating machines')."))
    # A4 (printed p.296) continues as B1 (printed p.297) with no intervening
    # figure; the two halves are joined into one printed paragraph.
    b.append(p("Despite this reservation it was accepted that increased "
               "safety would become a standard protection concept in Europe "
               "and the world at large and to exclude it in the UK for what "
               "were, to the majority in the UK, unconvincing technical "
               "reasons (no real evidence existing at the time of its level "
               "of protection being too low, rather than historic UK "
               "approaches being too high) would merely damage UK "
               "manufacturing industry. It was also noted that an "
               "International Standard (IEC 79–7 (1969)¹) was likely to be "
               "accepted by most countries of the world."))
    b.append(note("<b>Note on superscript footnote markers and the dash.</b> "
                  "The print uses superscript ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ¹⁰ immediately "
                  "after standard designations, sometimes inside a closing "
                  "parenthesis (for example '(IEC 79–7 (1969)¹)', "
                  "'(BS 4683, Part 4²)', 'BS/EN 50019 (1994)⁴', "
                  "'BS/EN 60529⁵', 'BS 4999 part 105⁶', 'BS/EN 50014⁷', "
                  "'BS/EN 50018⁸' and 'BS 5901 (1980)¹⁰'). The OCR text "
                  "layer misreads these as apostrophes, asterisks or "
                  "ordinary digits (for example 'IEC 79-7 (1969)'', "
                  "'Part 4*', '500147' and 'BS/EN 50018*'); the render prints "
                  "an en dash in '79–7'. The printed forms are retained."))

    b.append(h3("12.1 The situation in regard to standardization",
                "12.1 The situation in regard to standardization"))
    b.append(p("The UK accepted the protection concept of increased safety "
               "and a National Standard was produced in 1973 "
               "(BS 4683, Part 4²). This Standard was rapidly overtaken by "
               "BS 5501 Part 6 (1977)³ (which was the first edition of a "
               "European Standard, EN 50019) and both of these Standards "
               "have now been overtaken by BS/EN 50019 (1994)⁴ which is the "
               "second edition of the European Standard and will, in effect, "
               "be the Standard to which future apparatus will be "
               "constructed. This chapter will therefore be based upon the "
               "requirements of BS/EN 50019."))

    b.append(h3("12.2 Basic construction requirements",
                "12.2 Basic construction requirements"))
    b.append(p("The basic security of increased safety apparatus is in the "
               "construction of the apparatus itself and the limitations of "
               "the types of apparatus to which the protection concept is "
               "applicable. These limitations are:"))
    b.append(p("1. The apparatus must not arc or spark or produce ignition "
               "capable hot surfaces in normal operation"))
    b.append(p("2. No apparatus operating at a supply voltage of more than "
               "11 kV rms, or which internally produces voltages in excess "
               "of this, can be protected within this protection concept."))
    b.append(p("3. Apparatus where component construction cannot be defined "
               "in a way which will permit compliance with the requirements "
               "of the protection concept, or which cannot comply by virtue "
               "of their construction (e.g., semiconductor devices) cannot "
               "be dealt with in this protection concept. Therefore, "
               "increased safety is not normally applicable to "
               "instrumentation."))
    b.append(p("The above means that the protection concept finds its "
               "greatest application in such apparatus as connection boxes, "
               "luminaires, rotating machines, transformers, batteries, "
               "resistance heating devices and measuring instruments (basic "
               "meters, etc.)."))

    b.append(h4("12.2.1 Construction of enclosures",
                "12.2.1 Construction of enclosures"))
    b.append(p("Enclosures need to comply with the general hazardous area "
               "requirements (see Chapter 8) but because of the nature of "
               "this protection concept they must satisfy additional "
               "requirements."))
    b.append(p("As previously stated, the protection concept relies to a "
               "high degree on the exclusion of the external environment "
               "(keeping out the weather but not gas) and to this end the "
               "enclosures must have a degree of protection of at least "
               "IP54 in accordance with BS/EN 60529⁵ (As elsewhere, the "
               "method of determination of IP-rating for rotating electrical "
               "machines is slightly different and BS 4999 part 105⁶ is used "
               "in place of BS/EN 60529⁵ for such machines). Where the "
               "enclosure contains only insulated conductors and components, "
               "rather than bare live parts, this enclosure integrity may "
               "be reduced to IP44. Further reductions are permissible if "
               "breathing or draining holes are necessary for the reliable "
               "operation of the apparatus. In these circumstances IP44 is "
               "acceptable for enclosures containing bare live parts, and "
               "IP24 for enclosures containing only insulated conductors "
               "and components. In these latter cases, to utilize the lower "
               "IP-ratings, the position of the holes is critical and the "
               "apparatus will be subjected to installation conditions which "
               "minimize the possibility of ingress of liquid or solid "
               "foreign bodies in its installed location."))
    b.append(note("<b>Note on the lowercase 'part'.</b> The print reads "
                  "'BS 4999 part 105⁶' with a lowercase 'part', although "
                  "elsewhere the standard is cited as 'BS 4999 Part 105'. "
                  "The printed form is retained."))
    b.append(p("The requirements become more complex when this protection "
               "concept is used in conjunction with intrinsic safety (see "
               "Chapter 13 which discusses intrinsic safety) as is sometimes "
               "the case when it needs internal monitoring devices (e.g., "
               "temperature sensors in rotating machine windings) to ensure "
               "that early isolation takes place in case of fault. It is "
               "clear that the actual construction of the apparatus must be "
               "such that the intrinsic safety is not compromised but there "
               "is a particular point where outside influences can produce "
               "such a compromising effect. This is where the external "
               "connections are made for the increased safety part of the "
               "apparatus in the same place (terminal box, etc.) as the "
               "intrinsic safety external connections. In these circumstances "
               "an inner cover of at least IP30 is necessary for the "
               "increased safety connection facilities and a warning is "
               "necessary to ensure that this cover is not removed when the "
               "outer cover is off and the increased safety terminations "
               "energized or the intrinsically safe circuits are connected "
               "to external circuits. The inadvertent application of the "
               "levels of voltage in most increased safety apparatus could "
               "damage an intrinsically safe installation in a way which "
               "would not be apparent and which may cause danger, not only "
               "in the particular installation but in other intrinsically "
               "safe installations using facilities in common with it."))
    b.append(p("These enclosures and covers need to be fixed by special "
               "fasteners as described in Chapter 8."))

    b.append(h4("12.2.2 Terminals and connection facilities",
                "12.2.2 Terminals and connection facilities"))
    # C4 (printed p.298) continues as D1 (printed p.299) with no intervening
    # figure; the two halves are joined into one printed paragraph.
    b.append(p("All electrical connections, both those within the apparatus "
               "and those to permit connection of external electrical "
               "conductors, are important in this concept as any failure, "
               "even partial, of a connection can give rise to sparking. Of "
               "the possible electrical connections for external conductors "
               "themselves, only terminals are specifically addressed with "
               "specific detailed requirements which have to be satisfied "
               "to ensure they are reliable. The general use of plugs and "
               "sockets is not specifically mentioned in any Standards for "
               "this protection concept but, although this may be thought "
               "as precluding their use, a relaxation in respect of the "
               "general requirements for plugs and sockets in the case of "
               "battery assemblies, (see BS/EN 50014⁷ and Chapter 8) "
               "indicates that they are acceptable provided they meet the "
               "requirements of BS/EN 50014, and that the connection "
               "facilities which they provide for conductors satisfy the "
               "requirements of increased safety (either as terminals or as "
               "internal connections when the plug and/or socket is supplied "
               "with a fixed cable)."))
    b.append(note("<b>Note on the comma before the parenthesis.</b> The "
                  "print has a comma after 'battery assemblies' before "
                  "'(see BS/EN 50014⁷ and Chapter 8)'. The comma is kept in "
                  "English; the Vietnamese follows the natural phrasing and "
                  "drops it."))
    b.append(p("It will be remembered that the general requirements for "
               "plugs and sockets are that they should either be "
               "interlocked, so that any attempt to separate them isolates "
               "their electrical supplies, or that they are secured together "
               "by special fasteners and suitable warnings are supplied on "
               "the apparatus against separation while energized. It will "
               "be remembered that for operational currents not exceeding "
               "10 A rms ac or dc, at voltages of less than 250 V rms ac or "
               "60 V dc, foregoing requirements may be removed, provided "
               "that the part of the coupling remaining energized after "
               "separation is the socket; the circuit is broken before the "
               "plug pins separate from the socket to ensure that any arc is "
               "extinguished before total separation, and the combination "
               "remains flameproof in accordance with BS/EN 50018⁸ during "
               "the arc extinguishing period. In addition, the socket "
               "contacts which remain energized need to be protected to "
               "prevent ignition. This latter requirement is normally "
               "achieved by arranging the socket so that it is a flameproof "
               "enclosure after the plug has been removed, or that it forms "
               "an increased safety enclosure in such circumstances. In both "
               "cases automatically moving parts will need to be fitted to "
               "the socket to complete the enclosure after plug removal."))
    b.append(note("<b>Note on number/unit spacing.</b> The print reads "
                  "'10 A rms ac or dc' and '250 V rms ac or 60 V dc' with "
                  "spaces; the OCR text layer merges the first into "
                  "'10Arms'. The printed spacing is retained."))
    b.append(p("Terminals for either internal or external connections, "
               "including those permitting connection of conductors to "
               "plugs and sockets, need to be constructed so that they are: "
               "sufficiently well fixed to ensure that stresses (such as "
               "those produced by tightening screws) do not adversely affect "
               "the connection of the terminal to internal circuits and "
               "components are not able to damage the external conductors "
               "being connected to them by such things as direct connection "
               "to the screw providing the connection pressure or any sharp "
               "surfaces on their parts and are able to satisfy these "
               "requirements even when connecting stranded conductors. "
               "Crimped ferrules are permitted in the case of stranded "
               "conductors and screws of terminals may impinge directly on "
               "the ferrule but this is not permitted in the case of a "
               "stranded conductor without a ferrule."))
    b.append(note("<b>Note on the run-on list after the colon.</b> The print "
                  "uses a colon to introduce a string of requirements "
                  "without enumeration markers, leaving the sentence "
                  "awkward. The structure is retained in English; the "
                  "Vietnamese adds semicolons for readability without "
                  "dropping any point."))
    b.append(p("When more than one conductor is terminated in one terminal "
               "(an unusual situation which should be avoided as far as "
               "possible), the maximum number of conductors which may be "
               "terminated in a single terminal needs to be specified in "
               "each case. Figure 12.1 gives an example of a terminal which "
               "is acceptable for a single conductor and Fig. 12.2 for a "
               "multiple conductor terminal. The intermediate pad between "
               "the screw and the conductor is not necessary when the "
               "conductor is fitted with a crimped ferrule."))
    b.append(note("<b>Note on 'Figure' and 'Fig.'.</b> The print writes "
                  "'Figure 12.1' in full but 'Fig. 12.2' abbreviated in the "
                  "same sentence. Both forms are kept as printed."))
    b.append(p("In addition to using the means described for external "
               "connection internal connections may be made by:"))

    # Printed p.300: Figs 12.1 and 12.2 sit above the numbered list.
    b.append(fig(1, FA.fig_f1201()))
    b.append(fig(2, FA.fig_f1202()))
    b.append(note("<b>Note on the labels in Figures 12.1 and 12.2.</b> The "
                  "print uses 'Screw head' (two words) in Fig. 12.1 but "
                  "'Screwhead' (one word) in Fig. 12.2. The inconsistency is "
                  "retained in the redraw."))
    b.append(p("1. any form of screwed or bolted connection which does not "
               "damage the conductor, provides good electrical connection, "
               "and is locked against loosening (see Fig. 12.3);"))
    b.append(p("2. crimped connections such as those using a crimped ferrule "
               "where the conductors are either placed in the ferrule "
               "together and secured by a single crimping action or "
               "separately at each end and each is secured by a separate "
               "crimping action, (see Fig. 12.4);"))
    b.append(p("3. brazed or welded connections;"))
    b.append(p("4. soldered connections where the joint is not supported by "
               "the solder in view of the lower level of physical strength "
               "of such joints."))
    b.append(note("<b>Note on 'eylet'.</b> The caption and legend of "
                  "Fig. 12.3 print 'eylet' (not 'eyelet'), and the same "
                  "spelling appears in the 'Spade/eylet terminal' label of "
                  "Fig. 12.4. The printed spelling is retained."))

    b.append(h4("12.2.3 Separation of conducting parts",
                "12.2.3 Separation of conducting parts"))
    # E3 (printed p.300) continues as F1 (printed p.301); joined across the
    # intervening all-figure page in the same printed paragraph.
    b.append(p("As the enclosure is not sealed against the ingress of the "
               "outside air which may contain moisture impurities and, of "
               "course, flammable gases, vapours and mists, there is the "
               "possibility of breakdown of the air between separate bare "
               "conducting parts or the breakdown of the surface of any "
               "insulating material separating and/or supporting the "
               "conductors. To avoid this possibility, bare live conductors "
               "are required to be separated by certain minimum distances "
               "in air and these are called clearances. In addition where "
               "the bare live parts, and these may be just the bare end of "
               "an insulated wire where it is connected into a terminal, "
               "are separated by the surface of an insulating material, the "
               "insulant must be of a certain quality, and the distance "
               "along its surface must be of at least a specified minimum "
               "value which is called a creepage distance. The insulation "
               "quality is determined by measurements of the comparative "
               "tracking index (CTI), in accordance with BS 5901 (1980)¹⁰ "
               "which is a measurement identifying the capability of the "
               "insulating surface to retain its properties in the presence "
               "of contaminants."))
    b.append(note("<b>Note on the placement of footnote ¹⁰.</b> The print "
                  "places ¹⁰ immediately after the closing parenthesis of "
                  "'(1980)', giving 'BS 5901 (1980)¹⁰', with no bracket "
                  "around the note numeral. The placement is retained."))
    return "".join(b)
