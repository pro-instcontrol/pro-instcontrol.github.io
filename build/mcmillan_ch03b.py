# -*- coding: utf-8 -*-
"""Chapter 3, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 50-58 (PDF pp. 71-79).

Covers Sections 3.3.1 (types of release), 3.3.2 (releases from pipe
joints) and the surviving part of 3.3.3 (typical extents of Zone 2 from
pipe joint releases), with Figures 3.1-3.5 and Tables 3.2-3.4.
Module A owns the h3 heading for Section 3.3; the integration module owns
PAGES_SRC, refs, note_terms, the end note and the copyright line.

Eight source pages (printed 59-66 / PDF 80-87) are literal "MISSING PAGE"
placeholders. They are flagged explicitly below; nothing from them is
invented here.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig, table

import mcmillanfig03_a as FA


_T32_HEAD_VI = ["Áp suất 10⁵ N/m² / Phạm vi khu vực nguy hiểm tính bằng mét",
                "1", "2", "3", "4"]
_T32_HEAD_EN = ["Pressure 10⁵ N/m² / Extent of hazardous area in metres",
                "1", "2", "3", "4"]
# Pressure (×10⁵ N/m²) followed by the four extent columns.
_T32_ROWS = [
    ["1.35", "3.0", "1.0", "0.5", "0.5"],
    ["1.7", "3.5", "1.0", "0.5", "0.5"],
    ["2.0", "4.5", "1.0", "1.0", "0.5"],
    ["3.0", "5.5", "1.5", "1.0", "1.0"],
    ["5.0", "7.0", "2.0", "1.0", "1.0"],
    ["10.0", "9.5", "2.5", "1.5", "1.0"],
    ["20.0", "13.5", "3.5", "2.5", "1.5"],
    ["30.0", "16.5", "4.5", "3.0", "2.0"],
    ["50.0", "21.5", "5.5", "3.5", "2.5"],
    ["100.0", "31.5", "8.5", "5.0", "3.5"],
]

_T33_HEAD_VI = ["Áp suất phát thải chất lỏng N/m² — diện tích vũng (m²) theo "
                "phần trăm áp suất khí quyển", "<10%", "25%", "50%", "75%", ">90%"]
_T33_HEAD_EN = ["Liquid release pressure N/m² — pool area (m²) at percentages "
                "of atmospheric pressure", "<10%", "25%", "50%", "75%", ">90%"]
_T33_ROWS = [
    ["1 × 10⁴", "207", "83", "42", "28", "23"],
    ["3 × 10⁴", "399", "160", "80", "53", "44"],
    ["1 × 10⁵", "765", "306", "173", "102", "85"],
    ["3 × 10⁵", "1515", "606", "303", "202", "168"],
    ["1 × 10⁶", "2767", "1107", "553", "369", "307"],
    ["3 × 10⁶", "5192", "2077", "1040", "692", "577"],
    ["1 × 10⁷", "9702", "3881", "1920", "1293", "1078"],
]

_T34_HEAD_VI = ["Áp suất phát thải chất lỏng N/m² — diện tích vũng (m²) theo "
                "phần trăm áp suất khí quyển", "<10%", "25%", "50%", "75%", ">90%"]
_T34_HEAD_EN = ["Liquid release pressure N/m² — pool area (m²) at percentages "
                "of atmospheric pressure", "<10%", "25%", "50%", "75%", ">90%"]
_T34_ROWS = [
    ["1 × 10⁴", "12.0", "4.0", "2.0", "1.5", "1.0"],
    ["3 × 10⁴", "21.0", "8.0", "3.5", "2.5", "2.0"],
    ["1 × 10⁵", "41.0", "16.5", "7.5", "5.0", "3.5"],
    ["3 × 10⁵", "70.0", "28.0", "13.0", "9.0", "6.5"],
    ["1 × 10⁶", "144.0", "62.0", "29.0", "19.0", "15.0"],
    ["3 × 10⁶", "249.0", "113.0", "53.0", "33.0", "28.0"],
    ["1 × 10⁷", "506.0", "243.0", "115.0", "72.0", "60.0"],
]


def body_vi():
    b = []
    b.append(h4("3.3.1 Các loại phát thải", "3.3.1 Types of release"))
    b.append(p("Trong bất kỳ quy trình nào cũng có những phát thải điển hình thuộc "
               "các nhóm nhất định, và hầu hết phát thải thường gặp đều thuộc một "
               "trong các nhóm đó. Sáu nhóm dưới đây là điển hình. Tuy nhiên, "
               "phương pháp nguồn nguy hiểm vẫn đòi hỏi xác định từng nguồn cụ thể "
               "và khu vực nguy hiểm do nó tạo ra; các nhóm này chỉ là hướng dẫn, "
               "không thay thế cho công việc đó."))
    b.append(p("<b>Phát thải khí hoặc hơi dưới áp suất.</b> Hầu hết quy trình đặt "
               "khí và hơi dưới áp suất để vận chuyển, giữ chúng ổn định hoặc phun "
               "vào bình công nghệ. Loại phát thải này có vận tốc cao, thường bằng "
               "tốc độ âm thanh trong chính khí hoặc hơi đó, và tự trộn với không "
               "khí nhờ độ nhiễu loạn của nó; vì thế ngoài trời gió hiện hành gần "
               "như không ảnh hưởng. Điều này vẫn đúng trừ khi tia khí gặp vật cản: "
               "khi đó vận tốc giảm mạnh và gió trở thành tác nhân phân tán chính. "
               "Trong nhà hoặc nơi thông gió kém, sự phân tán diễn ra trong một "
               "lượng không khí hạn chế và có hiệu ứng tích lũy, có thể nhiễm toàn "
               "bộ khu vực trong nhà hoặc được che chắn. Thường cần biện pháp đặc "
               "biệt: dùng rộng rãi hệ thống hút gió cục bộ và loại trừ khí, hơi "
               "có áp suất khỏi những nơi thông gió hạn chế nhiều nhất có thể."))
    b.append(p("<b>Phát thải chất lỏng dưới áp suất.</b> Chất lỏng được chứa dưới "
               "áp suất thường thoát ra dưới dạng tia, và quãng đường tia đi được "
               "có thể xác định một phần khu vực nguy hiểm. Tại điểm thoát, hóa hơi "
               "rất ít khi chất lỏng còn dưới điểm sôi ở áp suất khí quyển, nên "
               "nguồn hơi chính là bay hơi từ mặt vũng lỏng do tia tạo ra. Vì tia "
               "đi xa, thường nên lắp tấm chắn tại mọi nguồn rò có thể để ngăn tia "
               "phun hình thành và giới hạn vị trí vũng lỏng; kích thước vũng cũng "
               "có thể giới hạn nhờ thiết kế chỗ chứa, dẫn đến bờ chắn (bund). Có "
               "thể tạo sương mù chất lỏng — các hạt lỏng phân tán rất mịn có cách "
               "hành xử như khí hoặc hơi — ngay ở áp suất đo thấp tới 2 × 10⁵ N/m². "
               "Khi có thể tạo sương mù, điểm cháy không còn là tiêu chí phân biệt, vì sương mù "
               "của chất lỏng dưới điểm cháy vẫn có thể bắt cháy."))
    b.append(p("<b>Phát thải khí và hơi đã hóa lỏng.</b> Khi khí và hơi được giữ ở "
               "dạng lỏng bằng áp suất, hoặc bằng áp suất kết hợp nhiệt độ, phát "
               "thải thường làm một phần vật liệu hóa hơi ngay lập tức. Phần còn "
               "lại vẫn là chất lỏng cho đến khi nhận đủ nhiệt để chuyển thành khí "
               "hoặc hơi. Vì thế vừa có khu vực nguy hiểm do khí và hơi hình thành "
               "ngay, vừa có kịch bản vũng lỏng; độ nhiễu loạn của hóa hơi còn tạo "
               "thêm một lượng sương mù. Tình huống tạo ra rất phức tạp."))
    b.append(p("<b>Phát thải không dưới áp suất.</b> Nhiều bình chứa — bình hàng "
               "tồn kho, xe bồn đường bộ, bể sơn — có bầu khí quyển nổ trong phần "
               "không gian hơi, do hơi từ chất lỏng ở nhiệt độ trên điểm cháy nhưng "
               "dưới điểm sôi. Trong điều kiện bình thường các hơi này tương đối "
               "nặng và không thoát ra ngoài với số lượng đáng kể khi còn giữ được "
               "cân bằng. Tuy nhiên, các bình này thường được nạp đầy, và việc nạp "
               "đẩy vật liệu dễ cháy ra khu vực xung quanh, tạo thành khu vực nguy "
               "hiểm."))
    b.append(p("<b>Thông liên giữa các vị trí vật lý.</b> Một khu vực nguy hiểm có "
               "thể được giới hạn bởi bức tường hoặc vật cản tương tự, về thực chất "
               "xác định ranh giới của vùng. Khi đó cần xét mọi lỗ mở trên tường, "
               "như cửa ra vào hoặc hộp cáp: chúng có thể đóng vai trò ống dẫn, "
               "chuyển bầu khí quyển nổ từ khu vực này sang khu vực khác. Cách xử "
               "lý duy nhất có hiệu quả là coi mỗi lỗ mở như một nguồn nguy hiểm ở "
               "khu vực bên kia và phân loại tương ứng."))
    b.append(p("<b>Khí và hóa chất dưới áp suất.</b> Trong nhiều trường hợp, khí "
               "hoặc hóa chất được dùng ở nhiệt độ trên điểm cháy được đưa vào hoặc "
               "hiện diện tại một khu vực cụ thể, ví dụ để phân tích. Dù không liên "
               "quan trực tiếp đến quy trình, những vật liệu dễ cháy này cũng là "
               "nguồn nguy hiểm và phải được xử lý như vậy. Khó khăn là nếu chúng "
               "không được xác định khi xây dựng nhà máy, chúng có thể nhạy cảm hơn "
               "đáng kể so với vật liệu công nghệ, và thiết bị đã chọn cho nhà máy "
               "có thể không phù hợp với chúng."))
    b.append(p("Dù phương pháp nguồn nguy hiểm đòi hỏi xác định từng nguồn và khu "
               "vực nguy hiểm tương ứng, vẫn có thể dùng một số khái quát hóa để "
               "đơn giản hóa công việc. Chúng thường cho khu vực nguy hiểm lớn hơn "
               "mức cần thiết, nhưng khách quan hơn phương pháp khái quát và có thể "
               "tiết kiệm đáng kể thời gian lẫn chi phí mà không làm giảm an toàn. "
               "Thuật ngữ dùng cho các cấp khu vực nguy hiểm được trình bày tại "
               "Hình 3.1."))
    b.append(fig(1, FA.fig_f301()))

    b.append(h4("3.3.2 Phát thải từ mối nối đường ống",
                "3.3.2 Releases from pipe joints"))
    b.append(p("Có năm cách chính để nối hai đoạn ống: hàn, dùng gioăng, đầu nối "
               "ép (olive), vòng đệm O và ren. Mối hàn làm hai đoạn ống về thực "
               "chất thành một đoạn liên tục; nếu thực hiện và kiểm tra đúng cách, "
               "nó không được coi là nguồn phát thải cho mục đích phân loại khu "
               "vực. Mối hàn vẫn có thể đứt, nhưng với tần suất quá thấp đến mức "
               "có thể bỏ qua trong phân loại."))
    b.append(p("Trong số các loại mối nối còn lại, không loại nào được coi là "
               "không đủ tin cậy đến mức phát thải trong vận hành bình thường nếu "
               "chọn và lắp đặt đúng cách, trừ trường hợp có sự can thiệp của con "
               "người. Nhìn chung mối nối đường ống không được coi là nguồn cấp "
               "chính: chúng thường tạo Vùng 2 và có khả năng tạo phát thải cấp "
               "phụ, với cơ chế riêng cho từng loại. Mối nối ren rò rỉ dọc theo "
               "ren, lượng phát thải tương đối nhỏ và vận tốc thấp, nên gió là tác "
               "nhân phân tán chính. Mối nối ép cho phát thải dạng đường nhỏ qua "
               "olive, cũng ở vận tốc thấp do cấu tạo của mối nối. Vòng đệm O chỉ "
               "rò khi bị nứt; vì nằm trong rãnh nên gần như không thể bị thổi bay, "
               "hình dạng rò là một vết nứt và vận tốc có thể cao vì không có yếu "
               "tố nào làm chậm dòng chảy."))
    b.append(p("Cuối cùng, gioăng là loại mối nối đường ống phổ biến nhất, với hai "
               "khả năng. Gioăng sợi amiăng ép (CAF) thông thường chỉ được giữ bằng "
               "áp suất, nên ở mọi áp suất ngoài mức rất thấp phải tính đến khả "
               "năng một phần gioăng bị thổi bay, tạo lỗ thoát khá lớn. Kích thước "
               "phần bị thổi bay thường liên quan đến vị trí bu lông trên mặt "
               "bích, và có thể nêu một kích thước điển hình. Để ngăn hiện tượng "
               "này, có thể dùng gioăng gia cố xoắn ốc: vật liệu tương tự nhưng có "
               "dải kim loại xoắn ốc được quấn bên trong. Khi đó gioăng gần như "
               "không bị thổi bay, nhưng vẫn có thể rò giữa mặt bích và gioăng do "
               "ứng suất hoặc chùng mối nối; vì gioăng thường dùng cho ống lớn hơn, "
               "lỗ rò này lớn hơn so với mối nối ép."))
    b.append(p("Khi các mối nối phải tháo lắp thường xuyên, ví dụ tháo ống để đưa "
               "thiết bị ra hoặc để người vào bình, sự can thiệp của con người ngay "
               "gần mặt bích làm tăng khả năng rò rỉ và phải được tính đến. Hơn 50 "
               "per cent vật liệu dễ cháy có độc tính ở mức thấp hơn nhiều so với "
               "giới hạn nổ dưới (LEL), và việc tạo bầu khí quyển nổ đáng kể tại "
               "thời điểm có người hiện diện là không chấp nhận được. Vì vậy phải "
               "loại bỏ vật liệu dễ cháy khỏi đường ống trước khi bắt đầu công việc, "
               "và quy trình phải loại trừ khả năng hình thành bầu khí quyển nổ "
               "đáng kể lúc tháo mối nối. Vì quy trình có thể hỏng, nên thận trọng "
               "xác định một Vùng 1 danh nghĩa bán kính 1 m quanh mối nối. Điều này "
               "chỉ áp dụng cho việc tháo mối nối tương đối thường xuyên, ví dụ "
               "có thể hơn một lần một tháng trung bình; việc tháo ít thường xuyên "
               "hơn thuộc các kịch bản phát thải ngẫu nhiên tạo Vùng 2 đã xét trong "
               "chương này."))
    b.append(p("Từ những xét đoán trên, có thể xác định các phát thải điển hình bao "
               "phủ hầu hết tình huống bình thường. Trong các ví dụ và bảng sau, "
               "độ mở lỗ thoát và vận tốc giả định là: gioăng CAF — 4 × 10⁻⁵ m² "
               "(25 mm × 1.6 mm), vận tốc cao khi không bị cản hoặc thấp khi bị "
               "cản, dựa trên một mảnh gioăng bị đẩy ra giữa hai bu lông; gioăng gia "
               "cố xoắn ốc — 2.5 × 10⁻⁶ m² (50 mm × 0.05 mm), vận tốc cao hoặc "
               "thấp, dựa trên sự chùng của mối nối vì các phần gioăng không thể bị "
               "đẩy ra; vòng đệm O — 10⁻⁶ m² (1 mm × 1 mm), vận tốc cao hoặc thấp, "
               "dựa trên một vết nứt trong vòng đệm; mối nối ép — 10⁻⁶ m² "
               "(0.1 mm × 10 mm), vận tốc thấp, dựa trên sự chùng giữa bề mặt kim "
               "loại với đường dẫn ngoằn ngoèo quanh olive; mối nối ren — "
               "5 × 10⁻⁷ m², nhỏ và ngoằn ngoèo, vận tốc thấp, dựa trên đường thoát "
               "qua ren."))
    b.append(p("Dù có phần tùy tiện, các con số trên khá bảo thủ, nên khó có khả "
               "năng nhỏ hơn mức thực tế xảy ra; khu vực nguy hiểm tính từ chúng "
               "trong đại đa số trường hợp lớn hơn khu vực thực tế. Nếu thông tin "
               "tại chỗ cho số liệu chính xác hơn cho tình huống cụ thể thì phải "
               "dùng giá trị lớn hơn. Dù vận tốc phát thải của gioăng và vòng đệm O "
               "được cho là cao, mọi vật cản trong lỗ thoát sau điểm hẹp nhất hoặc "
               "ngay gần đó sẽ làm giảm đáng kể vận tốc này; trừ khi có thể loại "
               "trừ chắc chắn các vật cản đó, luôn phải xét đến sự phân tán do gió."))

    b.append(h4("3.3.3 Phạm vi điển hình của Vùng 2 do phát thải tại mối nối "
                "đường ống",
                "3.3.3 Typical extents of Zone 2 from pipe joint releases"))
    b.append(p("<b>Phát thải khí hoặc hơi.</b> Khu vực nguy hiểm thường gặp do phát "
               "thải khí hoặc hơi được trình bày tại Hình 3.2, còn giá trị phạm vi "
               "cho cả phát thải vận tốc cao và thấp được cho trong Bảng 3.2. Các "
               "con số này dựa trên phép tính ở Chương 4, được coi là kịch bản xấu "
               "nhất và đôi khi lớn hơn mức dự kiến trong thực tế; có thể giảm chúng "
               "khi có chứng cứ thích hợp. Về cơ bản đây là khoảng cách hướng tâm "
               "tính từ mặt ngoài đường ống và chỉ áp dụng cho khí hoặc hơi có tỷ "
               "trọng tương đối gần với không khí (0.7 đến 1.3)."))
    b.append(fig(2, FA.fig_f302()))
    b.append(table(_T32_HEAD_VI, _T32_ROWS,
                   "Bảng 3.2 · Phạm vi khu vực nguy hiểm – phát thải khí"))
    b.append(p("<small><b>Ghi chú 1.</b> Phát thải từ gioăng CAF · <b>Ghi chú 2.</b> "
               "Phát thải từ gioăng gia cố xoắn ốc · <b>Ghi chú 3.</b> Phát thải từ "
               "vòng đệm O hoặc mối nối ép (olive) · <b>Ghi chú 4.</b> Phát thải từ "
               "mối nối ren.</small>"))
    b.append(p("Khi tỷ trọng tương đối lớn hơn 1.3, trọng lực làm khu vực nguy hiểm "
               "lệch xuống dưới. Hình 3.3 cho thấy mặt đầu và mặt cạnh: phạm vi "
               "phía trên mối nối vẫn là x = d, còn phía dưới là y = 1.5 d, với d "
               "là phạm vi lấy từ Bảng 3.2."))
    b.append(fig(3, FA.fig_f303()))
    b.append(p("Với tỷ trọng tương đối dưới 0.7, hình học là ảnh gương: Hình 3.4 có "
               "y = 1.5 d phía trên lỗ và x = d phía dưới, còn mặt cạnh mở rộng về "
               "phía trên đường ống nhiều hơn về phía dưới."))
    b.append(fig(4, FA.fig_f304()))
    b.append(p("Hình 3.5 cho thấy ảnh hưởng của sự gần mặt đất, tường và các bề mặt "
               "tương tự, nơi chuyển động không khí yếu hơn ở vị trí cao. Bốn "
               "trường hợp gồm độ cao 1.5 đến 3 m và trường hợp dưới 1.5 m, với "
               "đường biên đứt nét gần mặt đất. Khi xác định phạm vi khu vực nguy "
               "hiểm trong một trường hợp cụ thể, phải tính đồng thời tất cả các "
               "ảnh hưởng này."))
    b.append(fig(5, FA.fig_f305()))
    b.append(p("<b>Phát thải chất lỏng.</b> Khi chất lỏng thoát ra còn có vấn đề "
               "thêm là tia lỏng có thể đi xa đáng kể trước khi chạm đất và vũng "
               "lỏng thoát hơi sau khi chạm đất. Nên lắp tấm chắn tại mối nối để "
               "ngăn tia hình thành, rồi kiểm soát vũng lỏng nhằm hạn chế khu vực "
               "nguy hiểm. Cách bố trí ưu tiên cho vũng có kích thước đã biết, được "
               "kiểm soát dưới đường ống, hoặc bờ chắn tại chỗ thu chất lỏng và "
               "chuyển đến nơi xử lý an toàn. Nếu vũng không được chứa giữ có chủ "
               "đích, nó sẽ phát triển đến khi tốc độ bay hơi từ mặt vũng bằng tốc "
               "độ rò rỉ. Vũng nhỏ dần khi nhiệt độ chất lỏng tiến gần điểm sôi, "
               "nhưng khu vực nguy hiểm quanh vũng lại lớn dần vì hóa hơi nhanh "
               "hơn."))
    b.append(p("Bảng 3.3 và Bảng 3.4 cho diện tích vũng do rò từ gioăng CAF hoặc "
               "gioăng gia cố xoắn ốc ở các áp suất phía trên điểm rò, với các cột "
               "áp suất hơi là phần trăm áp suất khí quyển (<10%, 25%, 50%, 75% và "
               ">90%) và diện tích tính bằng m². Trên mặt phẳng vũng phát triển "
               "đối xứng, nhưng độ dốc làm méo hình dạng và vì thế làm méo cả khu "
               "vực nguy hiểm. Khi kích thước vũng do bờ chắn quyết định, bờ chắn "
               "phải chứa được thể tích lớn nhất có thể rò trong một sự cố. Vì vậy "
               "cách ưu tiên là che chở mối nối để ngăn tia và thu chất lỏng gần "
               "đường ống nhất có thể, chuyển nó sang hệ thống thu gom và xử lý."))
    b.append(table(_T33_HEAD_VI, _T33_ROWS,
                   "Bảng 3.3 · Diện tích vũng chất lỏng do rò từ gioăng CAF ở các "
                   "áp suất khác nhau"))
    b.append(table(_T34_HEAD_VI, _T34_ROWS,
                   "Bảng 3.4 · Diện tích vũng do rò chất lỏng từ gioăng gia cố "
                   "xoắn ốc ở các áp suất khác nhau"))
    b.append(p("Khu vực nguy hiểm quanh vũng phụ thuộc vào hình dạng vũng và mức "
               "gần của nhiệt độ vũng với điểm sôi của vật liệu dễ cháy. Phạm vi "
               "điển hình được cho trong Bảng 3.7 (xem ghi chú về khoảng trống "
               "nguồn bên dưới). Bảng đó dựa trên áp suất riêng phần do vật liệu "
               "tạo ra, ảnh hưởng đến giới hạn nổ dưới hiệu dụng của hỗn hợp rời "
               "khỏi mép vũng; sau mép vũng, hỗn hợp bị pha loãng bởi nhiễu loạn "
               "gió và được coi là nguồn đường mang hơi bão hòa. Vận tốc gió dùng "
               "là 2 m/sec."))
    b.append(note("<b>Khoảng trống của nguồn.</b> Tám trang của tệp PDF được cung "
                  "cấp (trang in 59–66; trang PDF 80–87) chỉ chứa nguyên văn cụm "
                  "từ 'MISSING PAGE' cả trong lớp văn bản lẫn trong ảnh quét trang. "
                  "Vì vậy phần cuối của Mục 3.3.3, toàn bộ Mục 3.3.4, phần lớn "
                  "Mục 3.3.5, các Hình 3.6–3.8 và các Bảng 3.5–3.7 không thể tái "
                  "hiện ở đây. Không có chú thích, hình, giá trị hay văn bản nào "
                  "được bịa đặt cho phần tài liệu bị thiếu; chương tiếp tục với "
                  "đoạn văn còn lại của Mục 3.3.5 trong mô-đun tiếp theo."))
    return "".join(b)


def body_en():
    b = []
    b.append(h4("3.3.1 Types of release", "3.3.1 Types of release"))
    b.append(p("In any process there are typical releases which fall into "
               "recognizable categories, and most releases normally encountered "
               "will fall into one of them. The following six are typical. The "
               "source of hazard method nevertheless requires each individual "
               "source and its resulting hazardous area to be identified, so "
               "these categories are a guide rather than a substitute for that "
               "exercise."))
    b.append(p("<b>Release of gas or vapour under pressure.</b> Most processes put "
               "gases and vapours under pressure to transport them, to keep them "
               "stable, or to inject them into process vessels. Such a release has "
               "a high velocity, normally the speed of sound in the gas or vapour "
               "concerned, and it mixes with air through its own turbulence; "
               "prevailing wind then has little or no effect outdoors. This "
               "remains true unless the jet meets an obstruction, when its "
               "velocity falls sharply and the wind becomes the main dispersant. "
               "Indoors, or in less well-ventilated situations, dispersion is into "
               "a limited volume of air and the effect is cumulative, so that the "
               "whole indoor or shielded area can become contaminated. Special "
               "precautions are often necessary: extensive local extract "
               "ventilation, and excluding pressurized gases and vapours as far "
               "as possible from areas where ventilation is restricted."))
    b.append(p("<b>Release of liquids under pressure.</b> A liquid contained under "
               "pressure will often escape as a jet, and the distance the jet "
               "travels may partly define the hazardous area. Vaporization at the "
               "point of release is minimal while the liquid is below its boiling "
               "point at atmospheric pressure, so the main source of vapour is "
               "evaporation from the surface of the pool formed by the jet. "
               "Because jets travel far, it is often wise to fit a baffle at any "
               "possible leak source to prevent jet formation and fix the location "
               "of the pool; the pool can also be limited by the design of its "
               "location, leading to bunding. Mists may also form: finely divided "
               "liquid droplets which behave like a gas or vapour, produced at "
               "gauge pressures as low as 2 × 10⁵ N/m². Where mists can form, "
               "flashpoint ceases to be a dividing criterion, because mists of "
               "liquids below their flashpoints can be ignited."))
    b.append(p("<b>Release of liquefied gases and vapours.</b> Where gases and "
               "vapours are kept liquid by pressure, or by a combination of "
               "pressure and temperature, release usually causes part of the "
               "material to vaporize instantly. The remainder stays liquid until "
               "it can obtain enough heat to become a gas or vapour. There is thus "
               "a hazardous area from the gas or vapour formed immediately, plus "
               "the pool scenario, and the turbulence of vaporization also creates "
               "some mist. The resulting situation is very complex indeed."))
    b.append(p("<b>Unpressurized releases.</b> Many containers, such as stock "
               "tanks, road tankers and paint vats, have an explosive atmosphere "
               "in their vapour space, caused by vapour from liquids above their "
               "flashpoint but below their boiling point. In normal circumstances "
               "these vapours are relatively heavy and do not leave the vapour "
               "space in significant quantity while equilibrium is maintained. "
               "Such containers are, however, frequently filled, and filling "
               "expels the flammable material into the surrounding area, creating "
               "a hazardous area."))
    b.append(p("<b>Communication between physical locations.</b> A hazardous area "
               "may be bounded by a wall or similar barrier which effectively "
               "sets the zonal limit. Any opening in that wall, such as a door or "
               "a cable trunk, must then be considered: it can act as a conduit "
               "carrying the explosive atmosphere from one area to another. The "
               "only effective treatment is to regard each such opening as a "
               "source of hazard in the remote area and classify accordingly."))
    b.append(p("<b>Pressurized gases and reagents.</b> In many cases gases or "
               "reagents used above their flashpoint are brought into, or present "
               "in, particular areas for purposes such as analysis. Although not "
               "directly related to the process, these flammable materials are "
               "equally sources of hazard and must be treated as such. The "
               "difficulty is that, if they were not identified when the plant was "
               "built, they may be considerably more sensitive than the process "
               "materials and the equipment selected for the plant may be "
               "unsuitable for them."))
    b.append(p("While the source of hazard method requires each source and its "
               "hazardous area to be identified, some generalizations are "
               "permissible and may simplify classification. They tend to give "
               "excessive hazardous areas, but they are more objective than the "
               "generalized method and can save significant time and money "
               "without endangering security. The nomenclature used for the "
               "various grades of hazardous area is shown in Figure 3.1."))
    b.append(fig(1, FA.fig_f301()))

    b.append(h4("3.3.2 Releases from pipe joints",
                "3.3.2 Releases from pipe joints"))
    b.append(p("There are five principal ways of joining two pipes: welding, "
               "gasketing, compression (olive) glands, 'O' rings and screwing. A "
               "welded joint makes the two sections effectively continuous, and "
               "if properly made and checked it is not considered a source of "
               "release for area classification purposes. Welds can still rupture, "
               "but so rarely that the frequency may be neglected here."))
    b.append(p("None of the other joint types is considered unreliable enough to "
               "release in normal operation if properly chosen and installed, "
               "except where human intervention is likely. Pipe joints in general "
               "are not treated as primary grade sources: they generally "
               "constitute Zone 2 and are capable of producing secondary grade "
               "releases, by a different mechanism in each case. A screwed joint "
               "leaks up its threads, releasing relatively small quantities at low "
               "velocity, so wind dispersion is the norm. A compression joint "
               "gives a small line release past the olive, also at low velocity "
               "because of its construction. An 'O' ring leaks only if it cracks; "
               "seated in a recess, it has little chance of blowout, so the leak "
               "geometry is a crack and the release velocity may be high because "
               "there is little to modify the flow."))
    b.append(p("Finally, the gasket is the most common pipe joint, with two "
               "possibilities. A normal compressed asbestos fibre (CAF) gasket is "
               "held by pressure alone, so at all but very low pressures blowout "
               "of part of the gasket must be considered, giving a fairly large "
               "orifice. The size of the blowout is normally related to the "
               "position of the flange bolts, and a typical size can be quoted. To "
               "prevent blowout, a spirally supported gasket may be used: a "
               "similar material with a spiral metal support wound into it. "
               "Blowouts are then effectively prevented, but leakage can still "
               "occur between the flange and the gasket through joint stress or "
               "relaxation; since gaskets are usually fitted to larger pipes, this "
               "leak is larger than for compression fittings."))
    b.append(p("Where joints are regularly broken, for example when pipes are "
               "spaded off to remove equipment or to allow entry to a vessel, "
               "human intervention close to the flange increases the possibility "
               "of leakage and must be taken into account. Well over 50 per cent "
               "of flammable materials are toxic at levels far below their lower "
               "explosive limit (LEL), and creating a significant explosive "
               "atmosphere where personnel are present at that moment is "
               "unacceptable. The material must therefore be removed from the "
               "pipe before the work starts, and the procedure should eliminate "
               "significant explosive atmospheres at the moment of breaking. "
               "Since such procedures can fail, it is prudent to identify a "
               "nominal Zone 1 of 1 m radius around the joint. This applies only "
               "to joint breaking on a relatively regular basis, for example "
               "possibly more than once a month on average; less frequent breaking "
               "falls under the random release scenarios giving Zone 2 dealt with "
               "in this chapter."))
    b.append(p("Taking these considerations into account, typical leaks covering "
               "most normal situations may be defined. In the following examples "
               "and tables the assumed release apertures and velocities are: CAF "
               "gasket — 4 × 10⁻⁵ m² (25 mm × 1.6 mm), velocity high when "
               "unimpeded or low when impeded, based on a piece of gasket ejected "
               "between two flange bolts; spirally supported gasket — 2.5 × 10⁻⁶ "
               "m² (50 mm × 0.05 mm), high or low velocity, based on relaxation of "
               "the joint because parts of the gasket cannot be ejected; 'O' ring "
               "— 10⁻⁶ m² (1 mm × 1 mm), high or low velocity, based on a crack in "
               "the ring; compression joint — 10⁻⁶ m² (0.1 mm × 10 mm), low "
               "velocity, based on relaxation of the metal-to-metal contact with "
               "a labyrinthine path around the olive; screwed joint — 5 × 10⁻⁷ "
               "m², small and labyrinthine, low velocity, based on exit via the "
               "threads."))
    b.append(p("Although to a degree arbitrary, these figures are fairly "
               "conservative, so they are unlikely to be smaller than what "
               "actually happens in practice, and the areas calculated from them "
               "will in the great majority of cases be larger than those which "
               "occur. If local knowledge provides more accurate figures for the "
               "particular situation, the larger values should be used. Although "
               "release velocities for gaskets and 'O' rings are given as high, "
               "any obstruction within the orifice after its smallest point or "
               "close to it will significantly reduce that velocity; unless such "
               "obstructions can confidently be ruled out, dispersion by the wind "
               "should always be considered."))

    b.append(h4("3.3.3 Typical extents of Zone 2 from pipe joint releases",
                "3.3.3 Typical extents of Zone 2 from pipe joint releases"))
    b.append(p("<b>Gas or vapour release.</b> The hazardous area typically created "
               "by a gas or vapour release is shown in Figure 3.2, and values for "
               "its extent at both high and low release velocities are given in "
               "Table 3.2. These figures, based on the calculations in Chapter 4, "
               "are considered a worst case and will occasionally be larger than "
               "would be expected in practice; they may be reduced when suitable "
               "evidence justifies a reduction. They are basically radial "
               "distances from the outside of the pipe and apply only to gases "
               "and vapours of density similar to air (relative density 0.7 to "
               "1.3)."))
    b.append(fig(2, FA.fig_f302()))
    b.append(table(_T32_HEAD_EN, _T32_ROWS,
                   "Table 3.2 · Extent of hazardous area – gas release"))
    b.append(p("<small><b>Note 1.</b> Release from CAF gasket · <b>Note 2.</b> "
               "Release from spirally supported gasket · <b>Note 3.</b> Release "
               "from 'O' ring or compression joint with olive · <b>Note 4.</b> "
               "Release from screwed joint.</small>"))
    b.append(p("When the relative density is greater than 1.3, gravity makes the "
               "hazardous area biased downwards. Figure 3.3 shows the end and side "
               "views: the extent above the joint remains x = d, while below it "
               "becomes y = 1.5 d, where d is the extent from Table 3.2."))
    b.append(fig(3, FA.fig_f303()))
    b.append(p("For relative density below 0.7 the geometry is the mirror image: "
               "Figure 3.4 has y = 1.5 d above the bore and x = d below, with the "
               "side view extending much further above the pipe than below."))
    b.append(fig(4, FA.fig_f304()))
    b.append(p("Figure 3.5 shows the effect of proximity to the ground, walls and "
               "similar surfaces, where air movement is less than in elevated "
               "circumstances. The four cases cover heights of 1.5 to 3 m and the "
               "case below 1.5 m, with a dashed boundary near the ground. When "
               "determining the extent of a hazardous area in a particular case, "
               "all of these effects must be taken into account together."))
    b.append(fig(5, FA.fig_f305()))
    b.append(p("<b>Liquid releases.</b> When a liquid is released there is the "
               "further problem of jets which can travel significant distances "
               "before striking the ground, and of pools from which vapour "
               "escapes once the liquid has landed. It is preferable to baffle the "
               "joint to prevent jet formation and then to control any pool so as "
               "to limit the resulting hazardous area. The preferred arrangement "
               "gives a pool of known, controlled dimensions under the pipe, or "
               "containment local to the pipe which collects the liquid and "
               "transfers it to safe disposal. If the pool is not deliberately "
               "contained it will grow until the rate of vaporization from its "
               "surface equals the rate of leakage. The pool becomes smaller as "
               "the liquid temperature approaches its boiling point, while the "
               "hazardous area around it becomes larger because vaporization is "
               "faster."))
    b.append(p("Tables 3.3 and 3.4 give the pool areas produced by a leak from a "
               "CAF gasket or a spirally supported gasket at various pressures "
               "upstream of the leak, with columns for vapour pressure as a "
               "percentage of atmospheric pressure (<10%, 25%, 50%, 75% and "
               ">90%) and areas in m². On a flat surface the pool develops "
               "symmetrically, but any slope distorts its shape and hence the "
               "hazardous area. Where the dimensions are set by containment, that "
               "containment must hold the maximum volume likely to leak in any "
               "one incident. The preferred method is therefore to shroud the "
               "joint to prevent jets and collect the liquid as near to the pipe "
               "as possible for diversion to a collection and disposal system."))
    b.append(table(_T33_HEAD_EN, _T33_ROWS,
                   "Table 3.3 · Areas of pools formed by leaks from CAF gaskets "
                   "at various pressures"))
    b.append(table(_T34_HEAD_EN, _T34_ROWS,
                   "Table 3.4 · Areas of pools produced by liquid leaks from "
                   "spirally supported gaskets at various pressures"))
    b.append(p("The hazardous area around a pool depends on the pool geometry and "
               "on how close the pool temperature is to the boiling point of the "
               "flammable material. Typical extents are given in Table 3.7 (see "
               "the source-gap note below). That table is based on the partial "
               "pressure developed by the material, which affects the effective "
               "lower explosive limit of the mixture leaving the pool edge; "
               "beyond the edge the mixture is diluted by wind turbulence and "
               "treated as a line source carrying saturated vapour. The wind "
               "speed used is 2 m/sec."))
    b.append(note("<b>Source gap.</b> Eight pages of the supplied PDF (printed "
                  "pp. 59–66; PDF pp. 80–87) contain only the literal words "
                  "'MISSING PAGE' in both the text layer and the page renders. "
                  "Consequently the tail of Section 3.3.3, all of Section 3.3.4, "
                  "most of Section 3.3.5, Figures 3.6–3.8 and Tables 3.5–3.7 "
                  "cannot be reproduced here. No captions, figures, values or "
                  "prose for that material have been invented; the chapter "
                  "resumes with the surviving text of Section 3.3.5 in the next "
                  "module."))
    return "".join(b)
