# -*- coding: utf-8 -*-
"""Chapter 11, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 275-281 (PDF pp. 296-302).

Covers the chapter opener, 11.1 Standards for pressurization 'p', 11.2
Methods of pressurization, 11.2.1 Static pressurization and 11.2.2
Pressurization with leakage compensation (including its unnumbered
sub-heading). Figure 11.1 sits at its printed position, between the two
halves of the Group II paragraph on printed pp. 276 and 278; Table 11.1
sits at the top of printed p. 278, ahead of that paragraph's continuation.
The chapter shell owns the chapter h2, the references and the end matter.

Printed quirks are kept in the English text (the 1995/1996 conflict,
'principle approaches', mismatched curly quotes, the unnumbered heading,
the self-reference to Chapter 11, the extra closing parenthesis, 'per cent'
versus '%', and the ± sign) with bilingual notes; the Vietnamese follows
the intended meaning. This is an unofficial study translation. The source
PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig11 as F
import mcmillan_tbl11_1_2 as T


def body_vi():
    b = []

    # Printed p.275. The shell owns the chapter h2; the module owns the
    # printed subtitle line and the chapter-opening prose.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("<b>(BS/EN 50016 (1995))</b>"))
    b.append(note("<b>Lưu ý về năm trong tiêu đề và trong thân bài.</b> Trang "
                  "mở đầu chương ghi '(BS/EN 50016 (1995))', còn thân bài (xem "
                  "11.1) ghi 'BS/EN 50016 (1996)⁶'. Cả hai được giữ nguyên theo "
                  "bản in; sự khác biệt này có trong nguyên bản và không được "
                  "tự ý chỉnh cho khớp."))
    b.append(note("<b>Lưu ý về ký hiệu chú thích viết ở dạng mũ.</b> Bản in dùng "
                  "các ký hiệu ¹ ² ³ ⁴ ⁵ ⁶ ⁷ dạng mũ (ví dụ 'Part 2,¹', "
                  "'76/117/EEC³', 'BS 5501, Part 3⁵', 'BS/EN 50016 (1996)⁶', "
                  "'BS/EN 50014⁷' và '50 N/m²'); lớp văn bản OCR đọc nhầm thành "
                  "các chữ số thường dính vào tên tiêu chuẩn ('500147', "
                  "'Part 35', 'N/m2'). Bản dịch giữ dạng mũ như bản in."))
    b.append(p("Nguyên lý bảo vệ (kiểu bảo vệ) tạo áp ‘p’ đã được sử dụng "
               "nhiều năm, dù ở Anh nó từ lâu được xem là vấn đề thuộc về quy "
               "tắc thực hành (người sử dụng). Trước khi có Tiêu chuẩn về "
               "nguyên lý bảo vệ, kỹ thuật này được xem là phương pháp dùng "
               "theo cách khá tùy hứng, khi không có nguyên lý bảo vệ nào khác "
               "có thể dùng hiệu quả. Điều đó không có gì đáng ngạc nhiên, vì "
               "nguyên lý bảo vệ này phụ thuộc rất nhiều vào các yếu tố nằm "
               "ngoài thiết bị, như ống dẫn dùng cho môi chất tạo áp, bản thân "
               "môi chất tạo áp, và các thiết bị điều khiển điện điều khiển "
               "nguyên lý này. Dù kỹ thuật đã được nhắc đến trong BS/CP 1003, "
               "Phần 2,¹, không có Tiêu chuẩn Quốc gia nào được xây dựng cho "
               "nó và người ta cho rằng vấn đề này không thuộc về chứng nhận "
               "thiết bị theo nguyên lý bảo vệ mà là vấn đề lắp đặt thực tế "
               "dành cho người lắp đặt và người sử dụng."))
    b.append(p("Thái độ ở Anh (và nơi khác) bắt đầu thay đổi khi ngành công "
               "nghiệp dầu khí Bắc Hải phát triển, vì nhiều thiết bị khoan được "
               "dùng chỉ có thể được bảo vệ bằng tạo áp, và kỹ thuật này đã "
               "được phát triển rất xa ở Mỹ, bằng chứng là nó được đưa vào "
               "National Electrical Code.² Cùng lúc đó, hoạt động sáng tạo của "
               "các doanh nhân ở Anh dẫn đến tình huống thiết bị điều khiển "
               "tạo áp trở nên sẵn có trên thị trường, thay vì phải được phát "
               "triển riêng cho từng lần sử dụng (vốn là trường hợp phổ biến "
               "trong lịch sử). Những thay đổi này, cùng với những thay đổi "
               "tương tự về thái độ ở các nước châu Âu khác, đã dẫn đến Tiêu "
               "chuẩn đầu tiên được xây dựng cho thiết bị có kiểu bảo vệ ’p’, "
               "và sau đó nguyên lý bảo vệ trở thành một trong các nguyên lý "
               "bảo vệ Tiêu chuẩn, chứ không chỉ là vấn đề lắp đặt."))
    b.append(note("<b>Lưu ý về dấu ngoặc kép trong bản in.</b> Bản in dùng các "
                  "cặp dấu ngoặc kép lệch chiều, chẳng hạn ’off the shelf‘ "
                  "(mở bằng dấu ngoặc phải), ’p’ và, ở trang 279, "
                  "’minimum purge time’. Cách viết này được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt theo nghĩa và không sao chép "
                  "kiểu đặt dấu này."))

    b.append(h3("11.1 Tiêu chuẩn về tạo áp ‘p’",
                "11.1 Standards for pressurization ‘p’"))
    b.append(p("Mối quan tâm đối với nguyên lý tạo áp lớn đến mức khi Chỉ thị "
               "đầu tiên của Liên minh Châu Âu về Bầu khí quyển nổ, "
               "76/117/EEC³, được ban hành, nó đã viện dẫn Tiêu chuẩn CENELEC, "
               "EN 50016 (1977)⁴, được xuất bản ở Anh với tên BS 5501, Phần 3: "
               "(1977)⁵ cho việc tạo áp, trao cho nguyên lý bảo vệ tư cách "
               "pháp lý thay vì cách tiếp cận 'người sử dụng'."))
    b.append(p("BS 5501, Phần 3⁵ chỉ chứa các yêu cầu đối với thiết bị không "
               "chứa cũng như không được đưa vào bất kỳ vật liệu dễ cháy nào. "
               "Điều này thực tế loại trừ việc dùng nó với mọi thiết bị phân "
               "tích và nhà phân tích, vốn thường là các phòng được chế tạo "
               "sẵn chứa thiết bị phân tích và có người ra vào. Nó cũng loại "
               "trừ các phòng được tạo áp, vốn cũng rất quan trọng đối với "
               "công nghiệp vì trong nhiều trường hợp tạo áp là nguyên lý bảo "
               "vệ áp dụng cho các phòng đó."))
    b.append(p("Tình hình này kéo dài cho đến khi ấn bản thứ hai của Tiêu "
               "chuẩn Châu Âu được xuất bản tại Anh với tên BS/EN 50016 "
               "(1996)⁶, với hai khái niệm mới. Thứ nhất, và quan trọng nhất, "
               "nó đưa vào khái niệm thiết bị điện được tạo áp mà bên trong "
               "có đưa vật liệu dễ cháy vào, và mở rộng kỹ thuật này sang "
               "thiết bị phân tích, loại thiết bị ngày càng trở nên phổ biến "
               "khi sản phẩm trở nên tinh vi hơn. Thứ hai, nó chính thức hóa "
               "tạo áp tĩnh, vốn trước khi ấn bản này ra đời không phải ai "
               "cũng cho là đã được bao gồm. Điều này đã tạo ra một cú hích "
               "rõ rệt và rất cần thiết cho kỹ thuật, vì tạo áp tĩnh không cần "
               "bất kỳ ống dẫn hoặc nguồn cấp khí nào như các dạng chính thống "
               "của kỹ thuật này, mà chỉ dựa vào chất lượng của các lớp bịt "
               "kín bên trong để giữ áp suất nội bộ. Tuy nhiên, nhà phân tích "
               "và phòng được tạo áp vẫn bị loại khỏi Tiêu chuẩn, và khó có "
               "thể thấy chúng có thể được đưa vào thế nào vì bản chất của "
               "chúng: có người ra vào thường xuyên và nội dung thay đổi theo "
               "thời gian, cả hai yếu tố đều đòi hỏi một cách tiếp cận năng "
               "động hơn như được quy định trong các quy tắc thực hành thay "
               "vì trong các Tiêu chuẩn (xem phần Lắp đặt của cuốn sách này). "
               "Hình 11.1 cho thấy tình hình hiện tại về điểm giao giữa các "
               "phần của nguyên lý bảo vệ thuộc về thiết bị và các phần do "
               "người sử dụng kiểm soát."))
    b.append(p("Có ba cách tiếp cận chính để tạo áp được nêu trong Tiêu chuẩn "
               "này để áp dụng cho từng thiết bị. Thứ nhất, tạo áp tĩnh, trong "
               "đó thiết bị được tạo áp bên ngoài vùng nguy hiểm và chỉ dựa "
               "vào các lớp bịt kín để duy trì an toàn liên tục. Thứ hai, tạo "
               "áp với bù rò rỉ, trong đó thiết bị được bịt kín ở mức tối đa "
               "có thể và môi chất tạo áp vẫn được nối để cho khí tạo áp đi "
               "vào thay thế phần bị mất do rò rỉ qua các lớp bịt kín không "
               "hoàn hảo. Thứ ba, tạo áp với dòng chảy liên tục của khí bảo "
               "vệ, trong đó một lưu lượng khí tối thiểu xác định được bố trí "
               "theo thiết kế trong suốt thời gian vỏ bọc được tạo áp."))
    b.append(note("<b>Lưu ý về cách viết 'principle approaches'.</b> Bản in "
                  "viết 'There are three principle approaches', dùng 'principle' "
                  "thay vì 'principal'. Cách viết này được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt dịch theo ý định là ba cách "
                  "tiếp cận chính."))
    b.append(p("Các công dụng khác nhau của ba phương pháp tạo áp này được "
               "nêu trong Bảng 11.1 và chi tiết về cách thực hiện được trình "
               "bày trong các đoạn sau. Cả ba hệ thống tạo áp đều được dự "
               "định dùng cho Vùng 1 và các vùng ít nguy hiểm hơn, với điều "
               "kiện thiết bị phải được cắt điện nếu việc tạo áp bị mất, "
               "nhưng có thể bị giới hạn ở Vùng 2 nơi mức độ an toàn thấp hơn "
               "(ví dụ, chỉ có còi báo khi áp suất bị mất)."))

    # Printed p.276 ends with '...which may'; Fig. 11.1 occupies printed p.277;
    # Table 11.1 heads printed p.278 ahead of the continuation of this sentence.
    b.append(p("Vì chúng hoạt động bằng cách loại trừ khí quyển xung quanh, "
               "các vỏ bọc được tạo áp thường được dự định cho tất cả khí, hơi "
               "và sương mù chất lỏng thuộc Nhóm II trong trường hợp này. Tuy "
               "nhiên, khi một vỏ bọc chỉ được chứng minh là làm sạch hiệu quả "
               "với một số khí nhất định, hoặc có khả năng phát thải bên "
               "trong, có thể có hạn chế về phạm vi khí, hơi và sương mù chất "
               "lỏng mà vỏ bọc có thể được dùng hoặc có thể"))
    b.append(fig(1, F.fig_f1101()))
    b.append(table(T.HEAD111_VI, T.ROWS111_VI, T.CAPTION111_VI))
    b.append(note(T.NOTE111_VI))
    b.append(note("<b>Lưu ý về cách ghi 'per cent' và '%'.</b> Thân văn bản "
                  "dùng 'per cent' (viết bằng chữ), còn Bảng 11.1 và các chú "
                  "thích của bảng dùng '%'. Sự khác biệt này được giữ nguyên "
                  "theo bản in."))
    b.append(p("được phép nằm bên trong vỏ bọc. Điều này sẽ không tạo ra sự "
               "phân nhóm phụ như được mô tả trong Chương 11, nhưng có thể "
               "yêu cầu xác định giới hạn cho các vỏ bọc cụ thể trên cơ sở, "
               "ví dụ, mật độ khí."))
    b.append(note("<b>Lưu ý về tham chiếu 'Chương 11'.</b> Bản in viết 'sự "
                  "phân nhóm phụ như được mô tả trong Chương 11' ngay trong "
                  "Chương 11. Cụm này được giữ nguyên theo bản in; nhiều khả "
                  "năng đây là lỗi tham chiếu của nguyên bản và không được "
                  "sửa sang số chương khác."))
    b.append(note("<b>Lưu ý về nhãn trong Hình 11.1.</b> Bản in có dấu phẩy "
                  "sau 'Static' trong ô 'Static, pressurization', dùng "
                  "'internal' trong một ô quyết định và 'interior' trong ô kia "
                  "('Can internal release...' so với 'Can interior release...'), "
                  "và các nhãn như 'Air or inert gas', 'Inert gas only', "
                  "'Air only', 'Installation Code', 'Not permitted' đều viết "
                  "thường không có dấu chấm cuối. Tất cả được giữ nguyên theo "
                  "bản in trong hình vẽ lại."))

    b.append(h3("11.2 Phương pháp tạo áp", "11.2 Methods of pressurization"))
    b.append(p("Chi tiết của ba phương pháp tạo áp và cách áp dụng chúng như "
               "sau:"))

    # Printed p.279. OCR prints '17.2.7'; the page render confirms 11.2.1.
    b.append(h4("11.2.1 Tạo áp tĩnh", "11.2.1 Static pressurization"))
    b.append(p("Như đã nêu, tạo áp tĩnh là phương pháp tạo áp trong đó vỏ bọc "
               "được cấp đầy khí trơ ở áp suất, sau đó được bịt kín ở mức cho "
               "phép vận hành trong một khoảng thời gian đủ cho việc vận hành "
               "và sử dụng, mà áp suất không giảm đến mức gây nguy hiểm. Điển "
               "hình của các trường hợp sử dụng này là những trường hợp cần "
               "đặt thiết bị vào bên trong bình chứa, đường ống và các vị trí "
               "tương tự, nơi việc dùng hệ thống tạo áp đòi hỏi nối liên tục "
               "với nguồn cấp khí hoặc không khí là không thực tế."))
    b.append(p("Môi chất tạo áp cho tạo áp tĩnh phải là khí trơ chứa ít hơn 1 "
               "phần trăm oxy, vì tạo áp bằng không khí không được xem là đạt "
               "mức an toàn yêu cầu. Đó là do hàm lượng oxy của không khí sẽ "
               "duy trì sự cháy đang có bên trong vỏ bọc, cho phép bất kỳ đám "
               "cháy nào phát sinh bên trong vỏ bọc do sự cố điện, v.v., tiếp "
               "diễn và gây hư hại thiết bị ngay cả sau khi đã cắt nguồn điện."))
    b.append(p("Vỏ bọc nên được tạo áp bằng khí trơ ở bên ngoài vùng nguy "
               "hiểm và kỹ thuật được dùng phải đảm bảo toàn bộ không khí "
               "được đẩy ra. Thường thì điều này đòi hỏi phương pháp tạo áp "
               "phải bao gồm một chu trình làm sạch (purge), được bố trí để "
               "đảm bảo quét sạch vỏ bọc một cách đầy đủ. Mức độ đầy đủ của "
               "việc làm sạch này được xác định bằng một thử nghiệm kiểu, "
               "trong đó vỏ bọc được làm sạch và các phép đo được thực hiện "
               "tại nhiều vị trí bên trong vỏ bọc để đảm bảo toàn bộ không "
               "khí đã được đẩy ra bởi chu trình làm sạch. Thời gian để điều "
               "đó xảy ra chính là 'thời gian làm sạch tối thiểu', và việc "
               "áp dụng chu trình làm sạch theo cùng cách như trong thử "
               "nghiệm trong khoảng thời gian đó sẽ luôn đảm bảo không khí "
               "được đẩy ra khỏi vỏ bọc. Tiêu chí để một lần làm sạch thành "
               "công là nồng độ oxy đã giảm xuống dưới 2 phần trăm. Dĩ nhiên "
               "là nên quy định thời gian dài hơn một chút so với mức tối "
               "thiểu để đảm bảo một hệ số an toàn nhất định, và người ta đề "
               "nghị tăng thêm 10 phần trăm thời gian."))
    b.append(p("Sau đó vỏ bọc được tạo áp, với cửa thoát khí được bịt kín, "
               "đến áp suất yêu cầu. Sự rò rỉ khí từ vỏ bọc phải đảm bảo rằng "
               "thời gian để áp suất bên trong giảm, từ áp suất nạp thiết "
               "kế, xuống còn 50 N/m² cao hơn áp suất ngoài, dài hơn thời "
               "gian mà vận hành yêu cầu thiết bị phải được sử dụng. Thời "
               "gian này cần dài hơn nếu bên trong vỏ bọc có các thiết bị "
               "tích trữ năng lượng hoặc bề mặt nóng, và cần cho phép điện "
               "tích hoặc nhiệt độ của chúng giảm xuống mức an toàn (xem "
               "BS/EN 50014 (1993))⁷ sau khi nguồn điện đã bị cắt và trước "
               "khi giới hạn dưới 50 N/m² được đạt tới."))
    b.append(note("<b>Lưu ý về đơn vị áp suất và dấu ngoặc trong bản in.</b> "
                  "Bản in ghi '50 N/m²' có dấu cách và số 2 ở dạng mũ; lớp "
                  "văn bản OCR đọc nhầm thành '50N/m2'. Cũng theo bản in, cụm "
                  "'(1993))⁷' có thêm một dấu ngoặc đơn đóng trước ký hiệu chú "
                  "thích dạng mũ. Các dạng này được giữ nguyên; không đổi "
                  "đơn vị."))
    b.append(p("Thiết bị cần có hai cơ cấu riêng biệt chỉ báo cho người sử "
               "dụng biết rằng đã đạt đến một áp suất sao cho, trong vòng một "
               "giờ, hoặc 100 lần thời gian cần để điện tích hoặc nhiệt độ "
               "giảm (nếu thời gian đó dài hơn), áp suất sẽ đã giảm xuống còn "
               "50 N/m² ở các tốc độ rò rỉ dự kiến bình thường."))
    b.append(p("Giá trị 100 lần nhằm cho phép một hệ số an toàn để đảm bảo "
               "rằng, ngay cả khi mọi biến số đều ở mức xấu nhất, vẫn có độ "
               "chắc chắn rất cao là thiết bị đã bị cắt điện và đưa ra khỏi "
               "vùng nguy hiểm trước khi áp suất giảm đủ để cho phép bầu khí "
               "quyển nổ xâm nhập vào vỏ bọc. Do bản chất của cách tiếp cận "
               "tạo áp tĩnh, các cơ cấu này cần được lắp đặt bởi nhà sản xuất "
               "thiết bị. Vì, theo yêu cầu tất yếu, các cơ cấu chỉ báo này "
               "cần nối tới các mạch bên ngoài vỏ bọc được tạo áp và thường "
               "vẫn duy trì được cấp điện sau khi thiết bị đã bị cắt điện, "
               "các mạch mà chúng được lắp vào cần được bảo vệ bằng cách khác "
               "(ví dụ, các cơ cấu có thể nằm trong một vỏ chống cháy bên "
               "trong thiết bị, hoặc các mạch mà chúng được lắp vào có thể là "
               "mạch an toàn nội tại)."))
    b.append(p("Hoạt động của các cơ cấu này như mô tả ở trên, nhưng các hành "
               "động được thực hiện sau khi chúng tác động là trách nhiệm của "
               "người sử dụng thiết bị. Tương tự, việc kiểm soát quá trình "
               "làm sạch vỏ bọc là vấn đề của người sử dụng, dù nó phải tuân "
               "theo thông số kỹ thuật do nhà sản xuất cung cấp (xem Mục 11.5 "
               "của chương này)."))
    b.append(p("Cuối cùng, phải nhận ra rằng việc dùng khí trơ trong quá "
               "trình nạp có thể gây nguy cơ ngạt ở những nơi kín khi nạp đầy "
               "vỏ bọc, và người sử dụng kỹ thuật này cần được cảnh báo về "
               "điều đó."))

    # Printed p.280. OCR prints '1 1.2.2'; the page render confirms 11.2.2.
    b.append(h4("11.2.2 Tạo áp với bù rò rỉ",
                "11.2.2 Pressurization with leakage compensation"))
    b.append(p("Đây là phương pháp tạo áp tiết kiệm nhất, dùng nguồn cấp khí "
               "tạo áp được nối cố định để bù các tổn thất do rò rỉ, vì lượng "
               "khí sử dụng chỉ được xác định bởi tốc độ rò rỉ và sự mất áp "
               "suất bên trong. Vì vậy, phương pháp này an toàn hơn tạo áp "
               "tĩnh, và không khí được phép làm môi chất tạo áp trong một số "
               "trường hợp, giúp tiết kiệm thêm."))
    b.append(p("Như đối với tạo áp tĩnh, cần đảm bảo rằng khi tạo áp bị mất, "
               "sự xâm nhập của bất kỳ bầu khí quyển nổ bên ngoài nào phải đủ "
               "chậm để cho phép bất kỳ điện tích dư hoặc bề mặt nóng nào giảm "
               "xuống mức an toàn trước khi khí có thể đi vào (xem BS/EN "
               "50014⁷). Trong trường hợp này, khác với tình huống trong tạo "
               "áp tĩnh, việc mở vỏ bọc có chủ đích cũng phải được tính đến "
               "vấn đề này. Nhìn chung, một dạng hạn chế nào đó ở ống dẫn đầu "
               "ra, cùng với một biển cảnh báo, sẽ đủ để đảm bảo điều này "
               "trong thực tế, nhưng sự hạn chế có thể phải được kích hoạt "
               "bằng việc phát hiện mất tạo áp hoặc bằng việc cắt các mạch "
               "điện bên trong vỏ bọc."))
    b.append(h4("Không có phát thải bên trong vật liệu dễ cháy",
                "No internal release of flammable material"))
    b.append(p("Khi vỏ bọc dự định được làm sạch và tạo áp bằng khí trơ, vỏ "
               "bọc được thử nghiệm như đối với tạo áp tĩnh, với khí trơ đó "
               "được dùng làm môi chất làm sạch, để xác định thời gian nồng "
               "độ oxy bên trong vỏ bọc giảm xuống dưới 2 phần trăm. Thời "
               "gian này trở thành thời gian làm sạch tối thiểu và, một lần "
               "nữa, người ta đề nghị quy định thời gian yêu cầu với hệ số an "
               "toàn 10 phần trăm để tính đến các biến đổi trong ứng dụng. "
               "Nhược điểm của việc làm sạch và tạo áp bằng khí trơ là có thể "
               "có nguy cơ ngạt, và điều này phải được đánh giá cho từng lần "
               "sử dụng."))
    b.append(note("<b>Lưu ý về tiêu đề không đánh số.</b> Bản in đặt 'No "
                  "internal release of flammable material' làm tiêu đề in đậm "
                  "không có số, nằm dưới 11.2.2. Tiêu đề này được giữ không "
                  "đánh số, không nâng thành 11.2.2.1."))

    # Printed p.281.
    b.append(p("Khi vỏ bọc dự định được làm sạch và tạo áp bằng không khí, "
               "tình hình phức tạp hơn một chút vì vỏ bọc chứa đủ oxy để duy "
               "trì sự cháy sau khi quá trình làm sạch hoàn tất. Điều này làm "
               "cho việc không còn khí dễ cháy nào trong vỏ bọc sau khi làm "
               "sạch trở nên quan trọng hơn nhiều, và để đạt được điều đó "
               "cần tính đến các mật độ khác nhau của các khí liên quan (ví "
               "dụ, hydro có mật độ chỉ 0.07 so với không khí, trong khi một "
               "số hydrocarbon dễ cháy có mật độ vượt quá 5 lần mật độ không "
               "khí). Vì vậy, quy trình xác định thời gian làm sạch cần khác "
               "đi, và hai loại thử nghiệm được thực hiện: thứ nhất dùng khí "
               "nạp ban đầu cho vỏ bọc nhẹ hơn không khí (thường dùng heli có "
               "mật độ bằng 0.14 mật độ không khí); và thứ hai dùng khí nặng "
               "hơn không khí (các lựa chọn ở đây là carbon dioxide, có mật "
               "độ bằng 1.6 lần mật độ không khí, hoặc argon có mật độ bằng "
               "1.4 lần mật độ không khí)."))
    b.append(p("Các thử nghiệm nên xác định thời gian để nồng độ của các khí "
               "thử (heli và carbon dioxide/argon) ở bất kỳ vị trí nào trong "
               "vỏ bọc giảm xuống dưới 1 phần trăm đối với heli hoặc 0.25 phần "
               "trăm đối với carbon dioxide/argon, với vỏ bọc ban đầu được "
               "nạp một trong các khí đó đến nồng độ tối thiểu 70 phần trăm ở "
               "bất kỳ vị trí nào trong vỏ bọc. Việc cần đo các mức rất thấp "
               "này cho thấy sẽ cần các thiết bị giám sát oxy rất nhạy nếu "
               "xác định gián tiếp (tức là, bằng sự khác biệt giữa nồng độ oxy "
               "của khí làm sạch và nồng độ của các mẫu khí lấy từ vỏ bọc, "
               "trong đó đối với carbon dioxide sự khác biệt nồng độ oxy 0.05 "
               "phần trăm là tình huống giới hạn), và có thể cần đo trực tiếp "
               "khí đang xét."))
    b.append(p("Thời gian dài hơn trong hai thời gian đó là thời gian nên được "
               "quy định làm thời gian làm sạch, và người ta đề nghị thêm hệ "
               "số an toàn 10 phần trăm để tính đến các biến đổi."))
    b.append(p("Trong một số trường hợp, một vỏ bọc có thể cần được quy định "
               "là làm sạch và tạo áp bằng không khí hoặc khí trơ. Trong "
               "những trường hợp này, thử nghiệm làm sạch bằng không khí là "
               "đủ nếu mật độ của khí trơ nằm trong khoảng ±10 phần trăm so "
               "với không khí. Trong các trường hợp khác, thời gian làm sạch "
               "sẽ cần được xác định với cả không khí và khí trơ và quy định "
               "thời gian dài hơn trong hai thời gian đó, hoặc quy định các "
               "thời gian riêng cho từng trường hợp (tức là, làm sạch bằng "
               "không khí và làm sạch bằng khí trơ)."))
    b.append(note("<b>Lưu ý về dấu ± trong bản in.</b> Bản in ghi 'within ±10 "
                  "per cent of air'; lớp văn bản OCR đọc nhầm thành 'within "
                  "610 per cent of air'. Dấu ± được giữ theo bản in."))
    b.append(p("Sau khi làm sạch, cửa ra của vỏ bọc được đóng lại và vỏ bọc "
               "được cho tăng lên áp suất thiết kế của nó, áp suất này phải "
               "cao hơn 50 N/m² đo theo áp kế, với khí làm sạch vẫn được nối "
               "và thay thế lượng khí bị mất do rò rỉ nhờ đó duy trì áp suất."))
    b.append(p("Khác với tình huống trong tạo áp tĩnh, không có sự suy giảm "
               "áp suất trừ khi xảy ra sự cố và chỉ cần lắp một thiết bị cảm "
               "biến áp suất thấp. Trong trường hợp này, thiết bị có thể được "
               "lắp bởi nhà sản xuất và là một phần của bộ vỏ bọc, nhưng cũng "
               "có thể do người lắp đặt cung cấp theo thông số kỹ thuật của "
               "nhà sản xuất. Khác với tạo áp tĩnh, việc làm sạch được thực "
               "hiện tại chỗ và nếu nguồn cấp khí bị mất, vỏ bọc phải trải "
               "lại chu trình làm sạch ngay khi nguồn khí được khôi phục và "
               "trước khi thiết bị được cấp điện lại nếu thiết bị đã bị cắt "
               "điện trong thời gian sự cố."))
    b.append(p("Ngoài ra, vì hệ thống lắp đặt sẽ có ống dẫn hoặc đường ống để "
               "dẫn khí làm sạch và khí bù sang vỏ bọc, những đoạn này cũng "
               "phải được làm sạch,"))
    b.append(note("<b>Lưu ý về ranh giới câu cuối.</b> Câu cuối cùng trong "
                  "phạm vi này kết thúc bằng dấu phẩy vì tiếp tục sang trang "
                  "in tiếp theo (nằm ngoài phạm vi của module này). Dấu phẩy "
                  "được giữ nguyên theo bản in."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.275. The shell owns the chapter h2; the module owns the
    # printed subtitle line and the chapter-opening prose.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("<b>(BS/EN 50016 (1995))</b>"))
    b.append(note("<b>Note on the year in the title and in the text.</b> The "
                  "chapter opener prints '(BS/EN 50016 (1995))' while the text "
                  "(see 11.1) prints 'BS/EN 50016 (1996)⁶'. Both are kept as "
                  "printed; the discrepancy is in the source and is not "
                  "silently harmonized."))
    b.append(note("<b>Note on superscript footnote markers.</b> The print uses "
                  "superscript ¹ ² ³ ⁴ ⁵ ⁶ ⁷ (for example 'Part 2,¹', "
                  "'76/117/EEC³', 'BS 5501, Part 3⁵', 'BS/EN 50016 (1996)⁶', "
                  "'BS/EN 50014⁷' and '50 N/m²'); the OCR text layer merges "
                  "them into ordinary digits attached to standard designations "
                  "('500147', 'Part 35', 'N/m2'). The superscripts are retained "
                  "as printed."))
    b.append(p("Protection concept (type of protection) pressurization ‘p’ has "
               "been used for many years, although it has historically been "
               "considered as a code of practice (user) matter in the UK. "
               "Before the advent of a protection concept Standard, the "
               "technique has been considered as a method to be used on a "
               "fairly ad-hoc basis, when no other protection concept could "
               "effectively be used. This was not surprising as the protection "
               "concept relied heavily upon items outside the apparatus, such "
               "as ducting for the pressurization medium, the pressurization "
               "medium itself, and the electrical control devices which "
               "control the concept. Although the technique was referred to in "
               "BS/CP 1003, Part 2,¹ no National Standard was ever written for "
               "it and, it was considered that the matter was one not for "
               "certification as an apparatus protection concept but for "
               "installers and users as a practical installation matter."))
    b.append(p("The attitude in the UK (and elsewhere) began to change as the "
               "North Sea oil industry developed because much of the drilling "
               "equipment used could only be protected by pressurization, and "
               "the technique had been developed to a great degree in the USA "
               "as evidenced by its inclusion in the National Electrical "
               "Code.² Coincident with this, entrepreneurial activity in the "
               "UK led to a situation where the control equipment for "
               "pressurization became available ’off the shelf‘, rather than "
               "having to be developed individually for each use (which had "
               "largely been the case historically). These changes, together "
               "with similar changes in attitude in the other countries of "
               "Europe led to the first Standard being produced for apparatus "
               "with protection type ’p’ and subsequently the protection "
               "concept became one of the Standard protection concepts, rather "
               "than an installation matter only."))
    b.append(note("<b>Note on the printed curly quotes.</b> The print uses "
                  "mismatched curly quote pairs, such as ’off the shelf‘ "
                  "(opened with a right quote), ’p’ and, on printed p. 279, "
                  "’minimum purge time’. The spelling is retained in English; "
                  "the Vietnamese follows the intended sense rather than "
                  "reproducing the typography."))

    b.append(h3("11.1 Standards for pressurization ‘p’",
                "11.1 Standards for pressurization ‘p’"))
    b.append(p("Such was the interest in the pressurization concept that when "
               "the first European Union Explosive Atmospheres Directive, "
               "76/117/EEC³ was published it referred to a CENELEC Standard, "
               "EN 50016 (1977)⁴ which was published in the UK as BS 5501, "
               "Part 3: (1977)⁵ in respect of pressurization, giving the "
               "protection concept legal status, rather than a ’user’ "
               "approach."))
    b.append(p("BS 5501, Part 3⁵ contained requirements only for apparatus "
               "which did not contain, or have brought to it, any flammable "
               "material. This effectively excluded its use with any "
               "analytical equipment and analyzer houses, which are normally "
               "prefabricated rooms containing analytical equipment into which "
               "personnel have access. It also excluded pressurized rooms "
               "which were also very important to industry as pressurization "
               "is the protection concept applied to such rooms in many "
               "circumstances."))
    b.append(p("This situation remained until the second edition of the "
               "European Standard was published in the UK as BS/EN 50016 "
               "(1996)⁶ which introduced two new concepts. First, and most "
               "important, it introduced the concept of pressurized electrical "
               "equipment into which flammable materials were brought, and "
               "extended the technique to analytical equipment which continues "
               "to become more and more common as products become more "
               "sophisticated. Second it formalized static pressurization, "
               "which before its publication had not been considered by some "
               "to be included. This gave a clear and much-needed boost to the "
               "technique as static pressurization needs none of the ducts and "
               "gas supplies required by its counterparts in the mainstream of "
               "the technique, relying only on the quality of the seals it "
               "contained to hold the internal pressure. Analyzer houses and "
               "pressurized rooms are, however, still excluded from the "
               "standard and it is difficult to see how they could be included "
               "because of their very nature; in that they have regular human "
               "access and their content varies from time to time, both of "
               "which factors require a more dynamic approach as provided in "
               "codes of practice rather than Standards (see Installation "
               "section of this book). Figure 11.1 shows the current situation "
               "in regard to the interface between the apparatus parts of the "
               "protection concept and the user-controlled parts."))
    b.append(p("There are three principle approaches to pressurization "
               "contained in this Standard for application to individual items "
               "of apparatus. First, static pressurization, in which the "
               "apparatus is pressurized outside the hazardous area and relies "
               "on its seals alone for its continued safety. Second, "
               "pressurization with leakage compensation, where the apparatus "
               "is sealed as far as possible and the pressurizing medium "
               "remains connected to allow entry of pressurizing gas to "
               "replace any lost by leakage caused by imperfect sealing. Third, "
               "pressurization with continuous flow of protective gas, where a "
               "defined minimum flow of gas is arranged by design throughout "
               "the time for which the enclosure is pressurized."))
    b.append(note("<b>Note on 'principle approaches'.</b> The print reads "
                  "'There are three principle approaches', using 'principle' "
                  "where 'principal' would be expected. The printed wording is "
                  "retained in English; the Vietnamese follows the intended "
                  "meaning of three principal approaches."))
    b.append(p("The various uses of these three methods of pressurization are "
               "given in Table 11.1 and details of their implementation in the "
               "following text. All three pressurization systems are intended "
               "for use in Zone 1 and less hazardous areas, provided that the "
               "apparatus is de-energized if the pressurization fails, but may "
               "be restricted to Zone 2 where a lower level of security exists "
               "(e.g., alarm only on pressure failure)."))

    # Printed p.276 ends with '...which may'; Fig. 11.1 occupies printed p.277;
    # Table 11.1 heads printed p.278 ahead of the continuation of this sentence.
    b.append(p("Because they operate by exclusion of the surrounding "
               "atmosphere, pressurized enclosures are normally intended for "
               "all Group II gases, vapours and mists in this regard. Where, "
               "however, enclosures have been shown to only purge effectively "
               "with certain gases, or there is the possibility of internal "
               "release, there may be restrictions on the range of such gases, "
               "vapours and mists in which the enclosure may be used or which "
               "may"))
    b.append(fig(1, F.fig_f1101()))
    b.append(table(T.HEAD111_EN, T.ROWS111, T.CAPTION111_EN))
    b.append(note(T.NOTE111_EN))
    b.append(note("<b>Note on 'per cent' and '%'.</b> The prose spells out "
                  "'per cent', while Table 11.1 and its footnotes use '%'. The "
                  "distinction is kept as printed."))
    b.append(p("be permitted inside the enclosure. This will not produce "
               "sub-grouping as described in Chapter 11, but may require limits "
               "to be defined for particular enclosures on the basis of, for "
               "example, gas density."))
    b.append(note("<b>Note on the 'Chapter 11' cross-reference.</b> The print "
                  "reads 'sub-grouping as described in Chapter 11' inside "
                  "Chapter 11 itself. The wording is kept as printed; it is "
                  "likely a source cross-reference error and is not silently "
                  "changed to another chapter number."))
    b.append(note("<b>Note on the labels in Figure 11.1.</b> The print carries "
                  "a stray comma after 'Static' in the box 'Static, "
                  "pressurization', uses 'internal' in one decision box and "
                  "'interior' in the other ('Can internal release...' versus "
                  "'Can interior release...'), and labels such as 'Air or "
                  "inert gas', 'Inert gas only', 'Air only', 'Installation "
                  "Code' and 'Not permitted' are in sentence case with no "
                  "terminal punctuation. All are retained as printed in the "
                  "redraw."))

    b.append(h3("11.2 Methods of pressurization",
                "11.2 Methods of pressurization"))
    b.append(p("The detail of the three methods of pressurization and their "
               "application are as follows:"))

    # Printed p.279. OCR prints '17.2.7'; the page render confirms 11.2.1.
    b.append(h4("11.2.1 Static pressurization", "11.2.1 Static pressurization"))
    b.append(p("As already stated, static pressurization is a method of "
               "pressurization where the enclosure is filled with an inert gas "
               "at pressure, and then sealed to a degree which will allow "
               "operation for a length of time which will allow its operation "
               "and use, without the pressure falling sufficiently to cause "
               "danger. Typical of such uses are those which require the "
               "insertion of the apparatus into vessels, pipelines and similar "
               "locations where it would be impractical to utilize a "
               "pressurization system requiring continuous connection to a gas "
               "or air supply."))
    b.append(p("The pressurization medium for static pressurization must be an "
               "inert gas which contains less than 1 per cent oxygen, as "
               "pressurization with air is not considered to give the required "
               "level of security. This is because of its oxygen content which "
               "would support any combustion existing within the enclosure, "
               "allowing any burning occurring within the enclosure due to "
               "electrical fault, etc., to be perpetuated and allow damage to "
               "the apparatus even after isolation of the electrical supplies."))
    b.append(p("The enclosure should be pressurized with the inert gas outside "
               "the hazardous area and the technique used should be such as to "
               "ensure that all air is evacuated. This will normally require "
               "the pressurization method to include a purge, which is arranged "
               "to ensure adequate scavenging of the enclosure. This purge "
               "adequacy is determined by a type test in which the enclosure "
               "is purged and measurements taken at various places inside the "
               "enclosure to ensure that all air is removed by the purge. The "
               "time taken for this to happen is then the ’minimum purge "
               "time’ and applying the purge in the same way, as for the test, "
               "for that time should always ensure that the air is removed from "
               "the enclosure. The criterion for a successful purge is when "
               "the oxygen concentration has fallen to less than 2 per cent. "
               "It is of course wise to specify a time slightly longer than "
               "the minimum to ensure some safety factor and a figure of 10 "
               "per cent additional time is suggested."))
    b.append(p("The enclosure is then pressurized, with the gas outlet sealed, "
               "to the pressure required. The leakage of gas from the enclosure "
               "should ensure that the time taken for the internal pressure "
               "to drop, from the design filling pressure, to 50 N/m² above "
               "external pressure is longer than the time for which operation "
               "demands that the apparatus be in use. The time needs to be "
               "longer if there are energy-storing devices or hot surfaces "
               "within the enclosure and needs to allow their charge or "
               "temperature to decay to a safe level (see BS/EN 50014 "
               "(1993))⁷ after the electrical supplies have been switched off "
               "and before the lower limit of 50 N/m² is reached."))
    b.append(note("<b>Note on the pressure unit and the parenthesis in the "
                  "print.</b> The print reads '50 N/m²' with a space and a "
                  "superscript 2; the OCR text layer reads '50N/m2'. The print "
                  "also has an extra closing parenthesis in '(1993))⁷' before "
                  "the superscript footnote marker. Both are kept as printed; "
                  "no unit conversion is made."))
    b.append(p("The apparatus requires two separate devices which indicate to "
               "a user that a pressure has been reached, such that within one "
               "hour, or 100 times the time taken for decay of charge or "
               "temperature (if this is longer), the pressure will have fallen "
               "to 50 N/m² at normal expected leakage rates."))
    b.append(p("The 100 times figure is intended to allow a safety factor to "
               "ensure that with all possible variables at their worst, there "
               "is still a very high degree of certainty that the apparatus "
               "will have been switched off and removed from the hazardous "
               "area before the pressure falls sufficiently to allow an "
               "explosive atmosphere into the enclosure. Because of the nature "
               "of the static pressurization approach, these devices need to be "
               "fitted by the manufacturer of the apparatus. As, of necessity, "
               "these indicating devices will need to connect to circuits "
               "outside the pressurized enclosure, and normally remain "
               "energized after the removal of power to the apparatus, the "
               "circuits in which they are installed will need to be otherwise "
               "protected (for example, the devices may be in a flameproof "
               "enclosure within the apparatus, or the circuits in which they "
               "are installed may be intrinsically safe circuits)."))
    b.append(p("The operation of these devices is as described above but the "
               "actions taken after operation are the responsibility of the "
               "user of the apparatus. Likewise, the control of the purging of "
               "the enclosure is a matter for the user, although it must comply "
               "with the specification provided by the manufacturer (see "
               "Section 11.5 of this chapter)."))
    b.append(p("Finally, it must be recognized that the use of inert gas in "
               "the filling process could present an asphyxiation risk in "
               "confined places when filling the enclosure, and users of the "
               "technique need to be warned of this."))

    # Printed p.280. OCR prints '1 1.2.2'; the page render confirms 11.2.2.
    b.append(h4("11.2.2 Pressurization with leakage compensation",
                "11.2.2 Pressurization with leakage compensation"))
    b.append(p("This is the most economical method of pressurization, using a "
               "permanently connected supply of pressurizing gas to make up "
               "losses due to leakage, because the use of gas is determined "
               "only by the rate of leakage and loss of internal pressure. It, "
               "therefore, is more secure than static pressurization, and air "
               "is permitted as the pressurizing medium in some cases "
               "effecting further economy."))
    b.append(p("As for static pressurization, it is necessary to ensure that "
               "on pressurization failure the ingress of any external "
               "explosive atmosphere is sufficiently slow to permit any "
               "residual charge or hot surface to fall to a safe level before "
               "the gas can enter (see BS/EN 50014⁷). In this case, unlike the "
               "situation in static pressurization, deliberate opening of the "
               "enclosure must also take this problem into account. Normally "
               "some form of restriction in the exit duct, together with a "
               "warning notice, will be sufficient to ensure this in practice, "
               "but the restriction may have to be initiated by the "
               "identification of pressurization failure or the isolation of "
               "the electrical circuits within the enclosure."))
    b.append(h4("No internal release of flammable material",
                "No internal release of flammable material"))
    b.append(p("Where the enclosure is intended to be purged and pressurized "
               "with an inert gas, the enclosure is tested as for static "
               "pressurization with that inert gas used as a purge medium to "
               "ascertain the time taken for the oxygen concentration inside "
               "the enclosure to fall to below 2 per cent. This then becomes "
               "the minimum purge time and, again, it is suggested that the "
               "time required be specified using a 10 per cent safety factor "
               "to cover variations in application. The disadvantage of "
               "purging and pressurization with inert gas is that there may be "
               "an asphyxiation risk, and this must be evaluated for each use."))
    b.append(note("<b>Note on the unnumbered heading.</b> The print sets 'No "
                  "internal release of flammable material' as a bold, "
                  "unnumbered heading under 11.2.2. It is kept unnumbered and "
                  "is not promoted to 11.2.2.1."))

    # Printed p.281.
    b.append(p("Where the enclosure is intended to be purged and pressurized "
               "with air the situation is somewhat more complicated as the "
               "enclosure contains enough oxygen to support combustion after "
               "the purge is complete. This makes it much more important that "
               "no flammable gas exists in the enclosure after purging, and to "
               "this end account must be taken of the various densities of the "
               "gases involved (e.g., hydrogen has a density of only 0.07 "
               "relative to air, whereas some flammable hydrocarbons have "
               "densities in excess of 5 times that of air). The procedure for "
               "determination of purging time needs to be different, therefore, "
               "and two types of test are carried out; the first using an "
               "initial filling gas for the enclosure which is lighter than "
               "air (helium whose density is 0.14 that of air is normally "
               "used); and second using a gas which is heavier than air "
               "(possibilities here are carbon dioxide, which has a density of "
               "1.6 times that of air, or argon which has a density of 1.4 "
               "times that of air)."))
    b.append(p("The tests should determine the time taken for the concentration "
               "of the test gases (helium and carbon dioxide/argon) anywhere "
               "in the enclosure to fall in concentration to less than 1 per "
               "cent for helium or 0.25 per cent for carbon dioxide/argon, the "
               "enclosure having been filled with one of these gases to a "
               "minimum concentration of 70 per cent anywhere in the enclosure. "
               "The low levels of these gases that it is necessary to measure "
               "indicates that very sensitive oxygen monitors would be "
               "necessary if it is to be determined indirectly (i.e., by "
               "variation between the oxygen concentration of the purge gas "
               "and that of the gas samples taken from the enclosure, where "
               "for carbon dioxide a difference in oxygen concentration of "
               "0.05 per cent is the limit situation) and direct measurement "
               "of the gas in question may be necessary."))
    b.append(p("The longest of these two times is the one which should be "
               "specified as the purge time, and it is suggested that a 10 per "
               "cent safety factor is added to allow for variations."))
    b.append(p("In some circumstances, an enclosure may need to be specified "
               "as purged and pressurized by air or inert gas. In these cases "
               "the air purge test is sufficient if the inert gas has a density "
               "within ±10 per cent of air. In other circumstances the purge "
               "times will need to be determined with both air and the inert "
               "gas and the longest of these specified, or separate times "
               "specified, for each case (i.e., air purge and inert gas purge)."))
    b.append(note("<b>Note on the ± sign in the print.</b> The print reads "
                  "'within ±10 per cent of air'; the OCR text layer misreads it "
                  "as 'within 610 per cent of air'. The ± sign is kept as "
                  "printed."))
    b.append(p("After purge the outlet of the enclosure is closed and the "
               "enclosure is permitted to rise to its design pressure which "
               "must be above 50 N/m² gauge, the purge gas remaining connected "
               "and replacing any gas lost by leakage thereby maintaining the "
               "pressure."))
    b.append(p("Unlike the situation in static pressurization there is no "
               "pressure decay unless a fault occurs and only one low pressure "
               "sensing device needs to be fitted. In this case, the device can "
               "be fitted by the manufacturer and be part of the enclosure "
               "package, but it may also be provided by the installer to the "
               "specification of the manufacturer. Unlike static pressurization, "
               "purging is in situ and if the gas supply fails the enclosure "
               "must go through its purge cycle again as soon as the gas supply "
               "is reinstated and before the apparatus is energized if the "
               "apparatus was switched off during the failure."))
    b.append(p("In addition, because the installation will have ducts or pipes "
               "to carry the purge and compensation gas to the enclosure these "
               "also must be purged,"))
    b.append(note("<b>Note on the final sentence boundary.</b> The last sentence "
                  "in this span ends with a comma because it continues onto the "
                  "next printed page (outside this module's range). The comma is "
                  "kept as printed."))
    return "".join(b)
