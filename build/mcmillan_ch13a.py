# -*- coding: utf-8 -*-
"""Chapter 13, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 331-346 (PDF pp. 352-367).

Covers the chapter opening, 13.1 The situation in respect of standardization,
13.2 Basic application of the concept (13.2.1-13.2.6), 13.3 Levels of
intrinsic safety (13.3.1-13.3.2), 13.4 Countable and non-countable faults
(13.4.1-13.4.4), 13.5 Confirmation of intrinsic safety in respect of arc and
spark ignition (13.5.1-13.5.2) and the unnumbered 'Inductive circuits'
subsection. Figures 13.1-13.5 and Tables 13.1-13.2 sit at their printed
positions. The chapter shell owns the chapter h2, the seventeen printed
references, the glossary, the source-quirk note and the copyright.

Full faithful EN/VI translation of survey A blocks A1-Aend. Printed quirks
are kept verbatim in the English text (the duplicated associated-apparatus
phrase, the unmatched quote, 'conplies', 'breaklash', 'purposed', the
erroneous 'Table 13.6 on page 362', the conflicting IIB energies, the OCR
text-layer errors) with bilingual notes; the Vietnamese follows the intended
meaning. This is an unofficial study translation. The source PDF is not
republished.
"""
from mcmillan_common import h3, h4, p, eq, note, table, fig
import mcmillanfig13_a as FA
import mcmillan_tbl13_1_4 as T1


def body_vi():
    b = []

    # A0 (printed p.331). The shell owns the chapter h2; the module owns
    # the printed standard subtitle lines and the chapter-opening prose.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("<b>(BS/EN 50020 — Apparatus)<br>"
               "(BS 5501, Part 9 — Systems)</b>"))
    # Quirks 43, 44: curly quotes, em dashes, continuous paragraph, comma.
    b.append(note("<b>Lưu ý về phần mở đầu chương.</b> Bản in đặt số 13 giữa "
                  "hai đường kẻ, nhan đề in nghiêng đậm trên ba dòng và hai "
                  "dòng tiêu chuẩn căn giữa, '(BS/EN 50020 — Apparatus)' và "
                  "'(BS 5501, Part 9 — Systems)', với dấu gạch ngang dài và "
                  "dấu nháy cong quanh 'i'. Đoạn văn mở đầu là một đoạn căn "
                  "đều liên tục, không có đầu dòng lùi vào, và viết 'It is "
                  "therefore, a 'system concept',' với dấu phẩy sau "
                  "'therefore'. Các dạng in được giữ nguyên trong bản tiếng "
                  "Anh; bản tiếng Việt theo nghĩa định."))
    # A1+B1 (printed pp.331-332): joined across the page break; no figure
    # intervenes. Quirks 1-5, 38, 39.
    b.append(p("An toàn nội tại là duy nhất trong số các nguyên lý bảo vệ "
               "về cách thức hoạt động. Tất cả các nguyên lý khác dựa vào "
               "việc ngăn ngừa tia lửa và bề mặt nóng, loại trừ bầu khí quyển "
               "nổ khỏi các nguồn đánh lửa đó, hoặc cô lập bất kỳ vụ nổ nào "
               "được tạo ra. An toàn nội tại hoàn toàn khác biệt ở chỗ không "
               "có nỗ lực nào nhằm ngăn tia lửa và cũng không có nỗ lực nào "
               "nhằm loại trừ bầu khí quyển nổ. An toàn đạt được bằng cách "
               "hạn chế công suất và năng lượng (ngoại trừ một số trường hợp "
               "hạn chế liên quan đến năng lượng tích trữ, khi có các biện "
               "pháp cụ thể để ngăn hoặc hạn chế tốc độ giải phóng của nó "
               "dưới dạng tia lửa hoặc hồ quang) trong khu vực nguy hiểm ở "
               "mức thấp hơn mức có thể gây đánh lửa. Ví dụ, vì hydro có thể "
               "bị đánh lửa bởi khoảng 20 μJ trong điều kiện lý tưởng, nên "
               "năng lượng cấp tới và sử dụng trong khu vực nguy hiểm bị "
               "hạn chế nghiêm ngặt, và an toàn nội tại chỉ thực sự khả thi "
               "cho những việc như thu thập thông tin, phân tích và các "
               "chức năng vận hành hạn chế. Kỹ thuật này phụ thuộc, gần như "
               "duy nhất, vào việc hạn chế hiệu quả năng lượng có thể đưa "
               "vào khu vực nguy hiểm, cũng như vào hiệu năng của chính "
               "thiết bị trong khu vực nguy hiểm. Do đó, đây là một 'khái "
               "niệm hệ thống', trong đó chi tiết của thiết bị trong khu vực "
               "nguy hiểm, thiết bị trong khu vực không nguy hiểm được nối "
               "với nó, và phương tiện kết nối đều quan trọng như nhau "
               "trong việc đạt được an toàn. Tương tự, vì nó tác động bằng "
               "cách hạn chế năng lượng sẵn có và hạn chế sự tích trữ hoặc "
               "giải phóng năng lượng đã tích trữ, nó dựa vào chính các mạch "
               "bên trong thiết bị, thay vì áp dụng vỏ bọc hoặc các biện "
               "pháp bổ sung khác để đạt được an toàn. Điều này có ưu điểm "
               "là giải phóng thiết bị khỏi những hạn chế phát sinh trong "
               "nhiều loại bảo vệ khác (tức là, nếu tia lửa xảy ra không có "
               "khả năng đánh lửa, thì sự cô lập cần thiết trong các loại "
               "bảo vệ khác cho mục đích kết nối/ngắt kết nối trở nên không "
               "cần thiết). Tuy nhiên, nó làm cho nguyên lý bảo vệ trở nên "
               "phức tạp hơn đôi chút trong cấu tạo và sử dụng. Dù vậy, các "
               "ưu điểm vượt xa các vấn đề phức tạp, bằng chứng là thực tế "
               "rằng tất cả các hệ thống lắp đặt thông thường trong Vùng 0 "
               "và gần như tất cả các hệ thống lắp đặt thiết bị đo trong "
               "Vùng 1 đều là an toàn nội tại. Việc sử dụng nó trong Vùng 0 "
               "có ý nghĩa quan trọng vì không có nguyên lý bảo vệ tiêu "
               "chuẩn nào khác được chấp nhận như thông lệ bình thường "
               "trong Vùng 0. Điều này là do, về bản chất, mức độ an toàn "
               "trong một hệ thống an toàn nội tại có thể được thay đổi "
               "tùy theo mức độ rủi ro của khu vực nguy hiểm, sao cho trong "
               "Vùng 0 (nơi rủi ro lớn nhất), mức độ an toàn có thể được "
               "nâng lên mức cao hơn nhiều so với bất kỳ loại bảo vệ tiêu "
               "chuẩn đơn lẻ nào khác."))
    b.append(note("<b>Lưu ý về các lỗi của lớp văn bản OCR ở phần mở đầu.</b> "
                  "Lớp văn bản đọc 'intrinsic safety 7’', 'BSIEN 50020 - "
                  "Apparatus' và 'BS 5501, Part 9 - Systems' cho các dòng "
                  "nhan đề, '20 FJ' thay cho '20 μJ' và 'llus has the "
                  "advantage' thay cho 'This has the advantage'. Đầu đề chạy "
                  "ở trang in 345 bị OCR đọc là 'Protection concept "
                  "intrinsic safefy 7’' nhưng bản in là 'Protection concept "
                  "intrinsic safety ‘i’'. Danh sách năng lượng trình bày ở "
                  "trang in 346 bị OCR đọc là '320 pJ / 120pJ / 40 pJ' nhưng "
                  "bản in là '320 μJ / 120 μJ / 40 μJ'. Cách đọc từ ảnh "
                  "trang in được dùng xuyên suốt."))

    # B2 (printed p.332). Quirks 45, 46.
    b.append(p("An toàn nội tại chỉ đứng sau vỏ bọc chống cháy (Chương 11) "
               "về tuổi đời, đã được phát triển trong ngành khai thác than "
               "để bao phủ các hệ thống tín hiệu đơn giản dùng trong ngành "
               "này (thường là mạch chuông/ắc quy leclanche), được nghi ngờ "
               "là đã gây đánh lửa trong ít nhất hai vụ nổ, một trong số đó "
               "là vụ nổ tồi tệ nhất từng xảy ra ở Anh."))
    b.append(note("<b>Lưu ý về 'leclanche' và 'Physicalisch'.</b> Bản in dùng "
                  "'leclanche cell/bell circuits' với 'leclanche' viết "
                  "thường, không dấu, và viết tên viện Đức là 'Physicalisch "
                  "Technische Bundesanstalt' (thường viết 'Physikalisch'). "
                  "Cả hai dạng in được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt theo nghĩa định."))

    # B3 -> heading 13.1 (printed p.332).
    b.append(h3("13.1 Tình hình liên quan đến việc chuẩn hóa",
                "13.1 The situation in respect of standardization"))
    # B4 (printed p.332). Quirks 6-16, 47.
    b.append(p("Dù được sử dụng rộng rãi ở Anh cho những thứ như hệ thống tín "
               "hiệu, hệ thống thông báo công cộng, van điện từ và cảm biến, "
               "đã không có Tiêu chuẩn Quốc gia dứt khoát nào tồn tại cho "
               "đến năm 1977, có lẽ vì các ứng dụng trước thời điểm đó tương "
               "đối đơn giản. Một Tiêu chuẩn Anh, BS 1259,¹ đã tồn tại từ "
               "năm 1958 nhưng thiếu đáng kể chi tiết và, với sự mở rộng "
               "nhanh chóng của việc sử dụng nguyên lý bảo vệ vì những lý "
               "do đã nêu ở trên, đã có sự thiếu hụt đáng kể các yêu cầu "
               "chi tiết về cấu tạo vào cuối những năm 1960. Vì một Tiêu "
               "chuẩn Châu Âu đang được xây dựng, người ta không cho rằng "
               "nên ban hành một Tiêu chuẩn Quốc gia, và điều này dẫn đến "
               "việc EECS/BASEEFA² là cơ quan chứng nhận/phê duyệt quốc gia "
               "duy nhất ở Anh vào thời điểm đó, đã ban hành tài liệu của "
               "riêng mình, SFA 3012,³ vào năm 1972, tài liệu này vẫn có "
               "hiệu lực cho đến khi Tiêu chuẩn Châu Âu được công bố dưới "
               "dạng BS 5501, Phần 7⁴ vào năm 1977 (ấn bản công bố tại Anh "
               "của EN 50020.⁵). Như vậy, từ sự gia tăng nhanh chóng của "
               "việc sử dụng nguyên lý bảo vệ, đến ngay sau sự ra mắt nhanh "
               "chóng của bóng bán dẫn thay thế đèn chân không, và sự mở "
               "rộng nhanh chóng tương tự của các yêu cầu đối với việc "
               "giám sát và điều khiển tinh vi các quá trình phức tạp, cho "
               "đến khi SFA 3012³ được công bố, việc phân xét về cái gì là "
               "an toàn nội tại phải do EECS/BASEEFA² thực hiện dựa trên "
               "các quy về bản chất chưa được công bố. Một tình huống tương "
               "tự đã tồn tại ở nơi khác và Physicalisch Technische "
               "Bundesanstalt (PTB⁶) ở Đức đã đóng một vai trò tương tự. "
               "SFA 3012 không được EECS/BASEEFA xây dựng một cách cô lập "
               "mà được rút ra từ một Tiêu chuẩn Quốc tế đang được Ủy ban "
               "Kỹ thuật Điện Quốc tế (IEC⁷) xây dựng, đó là IEC 79-11⁸. "
               "Tài liệu này cũng được dùng làm cơ sở cho BS 5501, Phần 7⁴ "
               "bởi cơ quan Tiêu chuẩn Châu Âu CENELEC⁹."))
    b.append(note("<b>Lưu ý về các ký hiệu chú thích dạng mũ.</b> Bản in đặt "
                  "¹ sau 'BS 1259,', ² sau 'EECS/BASEEFA' (hai lần), ³ sau "
                  "'SFA 3012,' (hai lần), ⁴ sau 'Part 7' (ba lần), ⁵ sau "
                  "'EN 50020.' trong ngoặc đơn, ⁶ trong '(PTB⁶)', ⁷ trong "
                  "'(IEC⁷)', ⁸ sau 'IEC 79-11', ⁹ sau 'CENELEC', ¹⁰ sau "
                  "'BS/EN 50020 (1995),' và sau 'BS/EN 50020', còn ¹¹ sau "
                  "'BS 5501, Part 9 (1982).'. Lớp văn bản OCR đọc nhầm "
                  "lần lượt thành ';', '?', ':', '4', '.5', '3', '2', '6', "
                  "'7', '8', dấu nháy đơn, '1°', '1O' và '.11'. Các ký hiệu "
                  "mũ của bản in, kể cả dấu chấm đứng trước chú thích bên "
                  "trong ngoặc đơn, được giữ nguyên."))
    # B5+C1 (printed pp.332-333): joined across the page break.
    # Quirks 17, 18, 19, 48, 49.
    b.append(p("Dù vậy, công nghệ an toàn nội tại vẫn còn rất non trẻ trong "
               "tình huống mới phức tạp hơn diễn ra khi chất bán dẫn được áp "
               "dụng, gây ra nhiều thảo luận và phát triển trong BS 5501, "
               "Phần 7, như bằng chứng là số lượng bài báo và bài viết được "
               "sản xuất trên các tạp chí và tại các hội nghị về chủ đề này "
               "và các cuộc thảo luận mà chúng dẫn đến. Tất cả các cuộc "
               "thảo luận này đã tạo ra sự phát triển nhanh chóng của nguyên "
               "lý bảo vệ và dẫn đến các tài liệu giải thích được ban hành "
               "ở Anh để làm rõ các vấn đề gặp phải khi áp dụng BS 5501, "
               "Phần 7 - khoảng 38 tài liệu trong giai đoạn 1981 đến 1992. "
               "Các bảng giải thích này, cùng với những bảng do các quốc "
               "gia thành viên CENELEC khác sản xuất, đã dẫn đến việc "
               "CENELEC công bố không ít hơn tám sửa đổi đối với Tiêu chuẩn "
               "và 20 bảng giải thích để làm rõ ý nghĩa của Tiêu chuẩn – "
               "một con số cao hơn nhiều so với bất kỳ Tiêu chuẩn Châu Âu "
               "nào khác trong dải tiêu chuẩn. Tất cả các sửa đổi và giải "
               "thích này hiện được đưa vào BS/EN 50020 (1995),¹⁰ là ấn "
               "bản thứ hai của Tiêu chuẩn Châu Âu. (Một bảng giải thích "
               "không sửa đổi Tiêu chuẩn mà chỉ làm rõ ý nghĩa của nó, trái "
               "với một sửa đổi có thể làm một trong hai hoặc cả hai)."))
    b.append(note("<b>Lưu ý về 'clarlfy' và dấu câu trong ngoặc đơn.</b> Lớp "
                  "văn bản OCR đọc 'clarlfy' ở chỗ bản in là 'clarify'. Cụm "
                  "'(An interpretation sheet does not amend a Standard but "
                  "only clarifies its meaning, unlike an amendment which "
                  "may do either or both).' đặt dấu chấm sau dấu ngoặc đóng. "
                  "'BS/EN 50020 (1995),¹⁰' có dấu phẩy trước chú thích trong "
                  "khi 'BS/EN 50020¹⁰' hai câu sau thì không có – không nhất "
                  "quán nhưng đúng như bản in. Các dạng in được giữ nguyên."))
    # C2 (printed p.333).
    b.append(p("BS/EN 50020¹⁰ và người tiền nhiệm của nó, BS 5501, Phần 7,⁴ "
               "chỉ nêu quy định đối với thiết bị an toàn nội tại và thiết "
               "bị liên kết. Như đã lưu ý, nguyên lý bảo vệ là duy nhất ở "
               "chỗ nó là một khái niệm hệ thống và cần xác định an toàn "
               "của một hệ thống trong mọi trường hợp. Vì sự phức tạp liên "
               "quan, điều này không thể luôn được thực hiện bằng một Quy "
               "chuẩn lắp đặt trong mọi trường hợp, và có một Tiêu chuẩn "
               "Châu Âu khác xác định cách các thiết bị và cáp kết nối có "
               "thể được kết hợp để tạo thành các hệ thống an toàn nội tại. "
               "Đó là BS 5501, Phần 9 (1982).¹¹"))

    # C3 -> heading 13.2 (printed p.333).
    b.append(h3("13.2 Áp dụng cơ bản của khái niệm",
                "13.2 Basic application of the concept"))
    # C4 (printed p.333).
    b.append(p("Như đã nêu trước đó, an toàn nội tại là một khái niệm hệ "
               "thống, dựa sự an toàn của nó vào thiết kế chi tiết của cả "
               "thiết bị trong khu vực nguy hiểm, thiết bị trong khu vực "
               "không nguy hiểm được nối với nó, và các kết nối giữa hai "
               "bên. Điều này khác với hầu hết các hình thức bảo vệ khác, ở "
               "đó chỉ các mạch bảo vệ điện trong khu vực không nguy hiểm "
               "là quan trọng, vì trong các nguyên lý bảo vệ đó, thiết bị "
               "trong khu vực nguy hiểm được thiết kế để duy trì an toàn "
               "hoặc giảm thiểu nguy hiểm trong quá trình cô lập, vốn tự "
               "động xảy ra sau một hỏng hóc của thiết bị. Do đó, có một số "
               "yếu tố cần được xem xét khi xác định một hệ thống an toàn "
               "nội tại."))

    # C5 -> heading 13.2.1 (printed p.333).
    b.append(h4("13.2.1 Thiết bị an toàn nội tại",
                "13.2.1 Intrinsically safe apparatus"))
    # C6+D1 (printed pp.333-334): joined across the page break.
    # Quirk 50: duplicated '(associated apparatus)'.
    b.append(p("Điều này được định nghĩa là 'Thiết bị mà tất cả các mạch đều "
               "là an toàn nội tại'. Thiết bị này dự định được lắp đặt trong "
               "khu vực nguy hiểm và sẽ được thiết kế sao cho, khi được cấp "
               "nguồn từ thiết bị thích hợp (thiết bị liên kết) trong khu "
               "vực không nguy hiểm (thiết bị liên kết), nó sẽ không tạo ra "
               "hồ quang, tia lửa hoặc bề mặt nóng có khả năng đánh lửa, dù "
               "khi vận hành bình thường hoặc khi xảy ra lỗi trong các mạch "
               "điện và linh kiện bên trong nó cùng với cáp kết nối của nó. "
               "Việc sử dụng các lỗi bên trong thiết bị và cáp kết nối của "
               "nó là phương pháp mà nhờ đó nó đạt được mức độ an toàn của "
               "mình. Các lỗi mạch hoặc linh kiện này có một xác suất xảy ra "
               "cụ thể về mặt thống kê và (vì khi một lỗi đã xảy ra, xác "
               "suất một lỗi độc lập khác xảy ra thấp hơn đáng kể) an toàn "
               "tổng thể của thiết bị được xác định bởi số lượng các lỗi "
               "như vậy xảy ra. Để đạt được mức độ an toàn chấp nhận được "
               "đối với các lỗi xảy ra, toàn bộ thiết bị phải tuân theo quy "
               "định chi tiết về chất lượng của các bộ phận cấu thành. Do "
               "đó, khả năng xảy ra lỗi được xác định và có thể lặp lại. "
               "Hình 13.1 cho thấy vị trí của thiết bị an toàn nội tại trong "
               "một hệ thống an toàn nội tại."))
    b.append(note("<b>Lưu ý về cụm lặp lại.</b> Bản in viết 'when fed from "
                  "appropriate apparatus (associated apparatus) in a "
                  "non-hazardous area (associated apparatus)'; cụm "
                  "'(associated apparatus)' xuất hiện hai lần. Cụm này được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt cũng giữ "
                  "cả hai lần xuất hiện."))

    # D2 -> heading 13.2.2 (printed p.334).
    b.append(h4("13.2.2 Thiết bị liên kết", "13.2.2 Associated apparatus"))
    # D3 (printed p.334).
    b.append(p("Thiết bị liên kết được định nghĩa là thiết bị chứa cả mạch an "
               "toàn nội tại và mạch không an toàn nội tại, được thiết kế "
               "sao cho các mạch không an toàn nội tại không thể ảnh hưởng "
               "bất lợi đến các mạch an toàn nội tại bên trong nó và đến "
               "thiết bị mà nó được nối vào. Thiết bị như vậy không định "
               "được lắp đặt trong khu vực nguy hiểm mà nhằm xác định công "
               "suất và năng lượng điện tạo thành đầu vào cho thiết bị an "
               "toàn nội tại mà nó được nối vào. Vai trò của nó là xác định "
               "điện áp, dòng điện, công suất và năng lượng (đầu vào) cho "
               "thiết bị đó và đảm bảo rằng ngay cả khi xảy ra lỗi, các mức "
               "này không bị vượt quá. Một lần nữa, các lỗi trong linh kiện "
               "và mạch bên trong thiết bị liên kết được tính đến, và số "
               "lượng lỗi được xem xét cho phép xác định mức độ an toàn đạt "
               "được. Cũng như đối với thiết bị an toàn nội tại, các yêu "
               "cầu được áp dụng cho chất lượng của các bộ phận cấu thành "
               "để đảm bảo mức độ an toàn xác định được và lặp lại được. "
               "Hình 13.1 cho thấy vị trí của thiết bị liên kết trong một "
               "hệ thống an toàn nội tại."))

    # D4 (printed p.334): Fig. 13.1 at its printed position.
    b.append(fig(1, FA.fig_f1301()))
    # Quirks 21, 74.
    b.append(note("<b>Lưu ý về nhan đề Hình 13.1.</b> Nhan đề in các Ghi chú "
                  "đánh số '(1) (2) (3)' bằng chữ số Ả Rập (OCR đọc '(I)' "
                  "thay cho '(1)'), có dấu phẩy trong cụm 'etc.,' ở Ghi chú 2 "
                  "và không có dấu chấm cuối sau 'additional evaluation'. "
                  "Nhan đề in được giữ nguyên trong hình; bản tiếng Việt "
                  "theo nghĩa định."))

    # E1 -> heading 13.2.3 (printed p.335).
    b.append(h4("13.2.3 Các kết nối liên kết", "13.2.3 Interconnections"))
    # E2 (printed p.335).
    b.append(p("Các kết nối giữa thiết bị an toàn nội tại và thiết bị liên "
               "kết cũng quan trọng vì hai lý do. Thứ nhất, chúng thường là "
               "cáp và có khả năng tích trữ năng lượng khi dòng điện chạy "
               "qua chúng do độ tự cảm và điện dung của chúng. Thứ hai, vì "
               "việc dùng cáp nhiều mạch nhiều lõi để kết nối là phổ biến, "
               "nên có khả năng xảy ra lỗi bên trong các cáp này có thể dẫn "
               "đến việc nối các mạch an toàn nội tại riêng biệt với nhau, "
               "và sự kết nối này có thể tạo ra một mạch tổng hợp có khả "
               "năng đánh lửa. Dù những cáp này không nguy hiểm bằng cáp "
               "chứa, ví dụ, mạch điện lưới, cấu tạo của chúng phải đạt mức "
               "tối thiểu để tránh các vấn đề, đặc biệt khi liên quan đến "
               "cáp nhiều lõi."))

    # E3 -> heading 13.2.4 (printed p.335).
    b.append(h4("13.2.4 Thiết bị đơn giản (các thiết bị)",
                "13.2.4 Simple apparatus (devices)"))
    # E4 (printed p.335). Quirks 22, 23, 51, 52.
    b.append(p("Người ta thừa nhận rằng một số thiết bị, như công tắc và hộp "
               "cọc đấu nối và các vật có cấu tạo đơn giản tương tự, không "
               "góp phần vào năng lượng sẵn có để tạo tia lửa hay sinh "
               "nhiệt vì chúng về cơ bản là trơ và các thông số của chúng "
               "có thể dễ dàng được xác định nhờ tính đơn giản của chúng. "
               "Chúng được gọi là thiết bị đơn giản và định nghĩa là loại "
               "thiết bị sẽ là một linh kiện hoặc cụm linh kiện có cấu tạo "
               "đơn giản, có các thông số điện được xác định rõ. Điều này "
               "bao gồm cặp nhiệt điện (nhưng không phải pin nhiệt điện), "
               "nhiệt kế điện trở, công tắc, cọc đấu nối và các thiết bị "
               "tương tự, và việc sử dụng chúng trong mạch an toàn nội tại "
               "được cho một mức độ tự do lớn nhờ tính đơn giản của chúng. "
               "Rất tiếc, đã có nhiều nỗ lực nhằm mở rộng việc sử dụng loại "
               "thiết bị được định nghĩa này để bao phủ các cụm linh kiện "
               "phức tạp dựa trên thực tế là không có độ tự cảm hay điện "
               "dung trong các cụm đó. Cách tiếp cận như vậy cần bị phản đối "
               "vì nó gần như chắc chắn sẽ dẫn đến các sai sót có hậu quả "
               "thảm khốc. Cần nhớ rằng định nghĩa ban đầu của loại thiết "
               "bị này trong BS 5501 Phần 1 (1977)¹² là 'các thiết bị trong "
               "đó, theo thông số của nhà sản xuất, không có giá trị nào "
               "vượt quá 1.2 vôn, 0.1 ampe 20μJ hoặc 25mW'. Rõ ràng ý định "
               "ban đầu là chỉ hạn chế việc nới lỏng đối với các thiết bị "
               "(linh kiện) và chỉ khi người ta nhận ra rằng một số cụm "
               "linh kiện (ví dụ, hộp cọc đấu nối) có thể phù hợp với các "
               "giới hạn đó thì từ 'device' mới được thay bằng 'apparatus'. "
               "Tuy nhiên, ý định vẫn như cũ và các nới lỏng trong nguyên "
               "lý bảo vệ đối với thiết bị đơn giản chỉ định áp dụng cho "
               "các thiết bị và các cụm rất đơn giản."))
    b.append(note("<b>Lưu ý về định nghĩa thiết bị đơn giản.</b> Bản in trích "
                  "dẫn BS 5501 Part 1 (1977)¹² là 'devices in which, "
                  "according to the manufacturers specifications, none of "
                  "the values of 1.2 volts, 0.1 amps 20μJ or 25mW were "
                  "exceeded': không có dấu phẩy sau 'amps', không có dấu "
                  "nháy đơn trong 'manufacturers' và không có dấu cách trong "
                  "'20μJ' hay '25mW'. Lớp OCR đọc '20pJ' thay cho '20μJ'. "
                  "Dòng 'intrinsically safe - that is,' dùng dấu gạch nối "
                  "có dấu cách. Cách viết in được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt theo nghĩa định."))

    # E5 -> heading 13.2.5 (printed p.335).
    b.append(h4("13.2.5 Mạch an toàn nội tại",
                "13.2.5 The intrinsically safe circuit"))
    # E6+F1 (printed pp.335-336): joined across the page break.
    b.append(p("Mạch an toàn nội tại là khối an toàn nội tại cơ bản. Nó là, "
               "khác với các nguyên lý bảo vệ khác, phần của hệ thống an "
               "toàn nội tại mà ở đó các mức năng lượng là an toàn nội tại "
               "- tức là, toàn bộ mạch bên dưới các linh kiện trong thiết bị "
               "liên kết xác định điện áp, dòng điện, công suất và năng "
               "lượng đưa vào khu vực nguy hiểm. Mạch an toàn nội tại thường "
               "gồm thiết bị an toàn nội tại, cáp kết nối, mọi thiết bị đơn "
               "giản lắp trên mạch và những phần của thiết bị liên kết nằm "
               "bên dưới các linh kiện hạn chế. Trên thực tế, đây là khối "
               "xây dựng cơ bản của an toàn nội tại, chứ không phải thiết bị "
               "an toàn nội tại (khác với trường hợp của các nguyên lý bảo "
               "vệ khác)."))

    # F2 -> heading 13.2.6 (printed p.336).
    b.append(h4("13.2.6 Hệ thống an toàn nội tại",
                "13.2.6 The intrinsically safe system"))
    # F3 (printed p.336).
    b.append(p("Hệ thống an toàn nội tại là toàn bộ hệ thống lắp đặt, bao "
               "gồm mọi phần có ảnh hưởng đến an toàn nội tại. Nó bao gồm "
               "mọi phần của thiết bị liên kết, khác với mạch an toàn nội "
               "tại vốn không bao gồm."))

    # F4 -> heading 13.3 (printed p.336).
    b.append(h3("13.3 Các cấp độ an toàn nội tại",
                "13.3 Levels of intrinsic safety"))
    # F5 (printed p.336). Quirks 24, 53, 54.
    b.append(p("Như đã nêu, an toàn nội tại là nguyên lý bảo vệ tiêu chuẩn "
               "đơn lẻ duy nhất thường được chấp nhận trong Vùng 0 và, ở "
               "dạng an toàn nhất, nó mang lại mức độ an toàn cao hơn nhiều "
               "so với các nguyên lý bảo vệ tiêu chuẩn khác. Nhận ra điều "
               "này, cũng rõ ràng là cấp độ an toàn nội tại phù hợp cho Vùng "
               "0 (và do đó cho mọi Vùng) có thể sẽ quá tốn kém và phức tạp "
               "đối với các hệ thống dự định dùng cho Vùng 1 và các khu "
               "vực ít nguy hiểm hơn. Để khắc phục vấn đề tiềm ẩn này, người "
               "ta công nhận hai cấp độ an toàn nội tại, đó là ‘ia’ (dự "
               "định cho mọi Vùng) và ‘ib’ (chỉ dự định cho Vùng 1 và 2). "
               "Cấp độ có thể áp dụng cho: một thiết bị an toàn nội tại, "
               "được giả định là nối vào thiết bị liên kết có các thông số "
               "đầu ra cụ thể và có mọi yêu cầu của cấp độ An toàn nội tại "
               "tương ứng được áp dụng bên trong nó; cho một thiết bị liên "
               "kết, trong đó các thông số đầu ra được xác định với mọi "
               "điều kiện thích hợp cho cấp độ an toàn nội tại được áp dụng "
               "bên trong nó; hoặc cho một hệ thống an toàn nội tại, trong "
               "đó các điều kiện thích hợp cho cấp độ an toàn nội tại được "
               "áp dụng cho toàn bộ hệ thống thay vì cho từng thiết bị "
               "riêng lẻ. Việc áp dụng cho từng thiết bị riêng lẻ là cách "
               "tiếp cận phổ biến nhất vì nó cho phép xác định các thông số "
               "của thiết bị trong trường hợp xấu nhất và việc xác định an "
               "toàn của sự kết nối vì thế dễ dàng hơn nhiều. Tuy nhiên, nó "
               "thường dẫn đến mức độ an toàn tổng thể cao hơn mức thực sự "
               "cần thiết."))
    b.append(note("<b>Lưu ý về tên cấp độ và danh sách sau dấu hai chấm.</b> "
                  "Bản in dùng ‘ia’ và ‘ib’ trong dấu nháy đơn cong (OCR đọc "
                  "'lib' thay cho ‘ib’). Câu 'The grade can apply to: an item "
                  "of ...' dùng dấu hai chấm để đưa vào một chuỗi liệt kê "
                  "không có số thứ tự. Các dạng in được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt thêm dấu phẩy để dễ theo "
                  "dõi mà không bỏ ý nào."))

    # F6 -> heading 13.3.1 (printed p.336).
    b.append(h4("13.3.1 An toàn nội tại cấp ‘ia’",
                "13.3.1 Intrinsic safety category ‘ia’"))
    # F7+G1 (printed pp.336-337): joined across the page break.
    b.append(p("Đây là cấp độ an toàn nội tại cao hơn, dự định cho phép các "
               "mạch an toàn nội tại của nó đi vào Vùng 0, và các thiết bị "
               "cùng hệ thống trong hạng mục này được yêu cầu phải không có "
               "khả năng gây đánh lửa bầu khí quyển nổ bằng hồ quang, tia "
               "lửa và bề mặt nóng trong tất cả các điều kiện sau."))
    # G2 (printed p.337): three numbered items, verbatim. Quirk 55.
    b.append(p("1. khi không áp dụng 'lỗi đếm được' nào và với sự kết hợp "
               "xấu nhất hoặc các sự kết hợp của 'lỗi không đếm được' áp "
               "dụng. (Hệ số an toàn 1.5 được áp dụng cho điện áp hoặc dòng "
               "điện - hoặc sự kết hợp của cả hai khi phù hợp - sẵn có "
               "trong các điều kiện này để gây ra hồ quang hoặc tia lửa "
               "nhưng không áp dụng hệ số an toàn cho thứ gây ra bề mặt "
               "nóng.);"))
    b.append(p("2. khi bất kỳ một trong các 'lỗi đếm được' có thể xảy ra "
               "được áp dụng cùng nhau, trong từng trường hợp, cùng với sự "
               "kết hợp xấu nhất của các 'lỗi không đếm được' được áp dụng. "
               "(Các hệ số an toàn áp dụng trong các điều kiện này như "
               "trong mục 1 ở trên.);"))
    b.append(p("3. khi bất kỳ hai trong các 'lỗi đếm được' có thể xảy ra "
               "được áp dụng cùng nhau, trong từng trường hợp, cùng với sự "
               "kết hợp xấu nhất của các 'lỗi không đếm được' được áp dụng. "
               "(Trong các điều kiện này không áp dụng hệ số an toàn cho "
               "điện áp hoặc dòng điện, hoặc sự kết hợp của chúng.)"))
    b.append(note("<b>Lưu ý về ba điều kiện trong 13.3.1.</b> Mục 1 in cụm "
                  "'of ‘non-countable faults applied.' với dấu nháy mở mà "
                  "không có dấu nháy đóng, và dùng dấu gạch nối có dấu cách "
                  "trong 'voltage or current - or combination of both as "
                  "appropriate -'. Các mục 1 và 2 kết thúc bằng dấu chấm "
                  "phẩy, mục 3 bằng dấu chấm. Dấu câu của bản in được giữ "
                  "nguyên trong bản tiếng Anh; bản tiếng Việt thêm dấu nháy "
                  "đóng theo nghĩa định."))
    # G3 (printed p.337).
    b.append(p("Rõ ràng, nếu không có lỗi đếm được nào có thể xảy ra thì "
               "thiết bị có thể là ‘ia’. Nếu sự kết hợp xấu nhất của các lỗi "
               "không đếm được có thể xảy ra không gây ra tia lửa hay hồ "
               "quang có khả năng đánh lửa với hệ số an toàn 1.5 được áp "
               "dụng, hoặc không tạo ra bề mặt nóng có khả năng đánh lửa khi "
               "không áp dụng hệ số an toàn, thì thiết bị hoặc mạch có thể "
               "được coi là ‘ia’. Tương tự, nếu chỉ có một lỗi đếm được có "
               "thể xảy ra, thiết bị có thể được coi là ‘ia’, với điều kiện "
               "là nó vẫn không gây đánh lửa với sự kết hợp xấu nhất của "
               "các lỗi không đếm được được áp dụng trong cả vận hành bình "
               "thường lẫn khi áp dụng lỗi đếm được đó, và với hệ số an toàn "
               "1.5 áp dụng cho đánh lửa do hồ quang hoặc tia lửa."))

    # G4 -> heading 13.3.2 (printed p.337).
    b.append(h4("13.3.2 An toàn nội tại cấp ‘ib’",
                "13.3.2 Intrinsic safety category ‘ib’"))
    # G5 (printed p.337). Quirk 25.
    b.append(p("Đây là cấp độ an toàn nội tại thấp hơn và khu vực nguy hiểm "
               "nhất mà các mạch của nó dự định đi vào là Vùng 1. Hiệu năng "
               "của nó trong cả vận hành bình thường và với bất kỳ một lỗi "
               "đếm được đơn lẻ có thể xảy ra phải đúng như quy định trong "
               "(1) và (2) áp dụng cho hạng mục ‘ia’ nhưng không cần xem "
               "xét bất kỳ tình huống nào mà hai lỗi đếm được xảy ra. Trong "
               "trường hợp không có lỗi đếm được nào có thể xảy ra, nó được "
               "xử lý theo cách giống như hạng mục ‘ia’."))
    b.append(note("<b>Lưu ý về ‘ia’ trong 13.3.2.</b> Lớp OCR đọc 'category "
                  "‘ia‘.' với dấu nháy đóng bị lệch hướng; bản in là "
                  "'category ‘ia’.' Dạng in được giữ nguyên."))

    # G6 -> heading 13.4 (printed p.337).
    b.append(h3("13.4 Lỗi đếm được và lỗi không đếm được",
                "13.4 Countable and non-countable faults"))
    # G7+H1 (printed pp.337-338): joined across the page break.
    b.append(p("Các lỗi, dù là đếm được hay không đếm được, là sự hỏng hóc "
               "của các linh kiện, dây dẫn và mọi hỏng hóc khác có thể xảy "
               "ra bên trong thiết bị hoặc hệ thống. Có ba tình huống trong "
               "thiết bị liên quan đến lỗi, và tình huống trong cáp kết nối "
               "được chi phối bởi thiết kế cáp. Chi tiết quy định cho linh "
               "kiện, kết nối, cáp, v.v., sẽ được trình bày chi tiết hơn sau "
               "trong chương này. Bất kỳ phần nào của thiết bị hoặc hệ "
               "thống không tuân thủ các yêu cầu của nguyên lý bảo vệ được "
               "giả định là có khả năng xảy ra lỗi ngay cả trong vận hành "
               "bình thường (lỗi không đếm được), và những phần tuân thủ "
               "thì phần lớn vẫn được coi là có khả năng xảy ra lỗi (lỗi "
               "đếm được)."))

    # H2 -> heading 13.4.1 (printed p.338).
    b.append(h4("13.4.1 Lỗi không đếm được", "13.4.1 Non-countable faults"))
    # H3 (printed p.338).
    b.append(p("Một lỗi không đếm được là sự hỏng của bất kỳ linh kiện, cụm "
               "hoặc kết nối nào bên trong thiết bị xảy ra ở bất kỳ thành "
               "phần nào không tuân thủ các yêu cầu cơ bản của nguyên lý "
               "bảo vệ. Khi chỉ có sự không tuân thủ một phần, lỗi chỉ liên "
               "quan đến hệ quả của sự không tuân thủ đó (ví dụ, khi một "
               "dây dẫn trần tuân thủ yêu cầu nhưng khoảng cách của nó với "
               "các dây dẫn trần khác thì không, thì ngắn mạch sẽ được coi "
               "là lỗi không đếm được nhưng đứt mạch của dây dẫn thì không)."))

    # H4 -> heading 13.4.2 (printed p.338).
    b.append(h4("13.4.2 Lỗi đếm được", "13.4.2 Countable faults"))
    # H5 (printed p.338).
    b.append(p("Sự hỏng của bất kỳ linh kiện, cụm hoặc kết nối nào tuân thủ "
               "các yêu cầu cấu tạo cơ bản của nguyên lý bảo vệ (trong hầu "
               "hết trường hợp bao gồm cả hệ số an toàn định mức) được gọi "
               "là lỗi đếm được."))
    # H6 (printed p.338).
    b.append(p("Tiêu chuẩn còn chứa các quy định nâng cao ngoài các quy định "
               "cơ bản và, khi linh kiện, cụm hoặc kết nối tuân thủ các yêu "
               "cầu cơ bản của nguyên lý bảo vệ và, thêm vào đó, tuân thủ "
               "các yêu cầu nâng cao, thì bất kỳ khía cạnh nào trong hoạt "
               "động của nó tuân thủ như vậy sẽ không bị coi là trở nên "
               "hỏng hóc. (Ví dụ, khoảng cách giữa các dây dẫn đáp ứng các "
               "yêu cầu bổ sung của nguyên lý bảo vệ sẽ không bị coi là khả "
               "năng ngắn mạch, trong khi bản thân các dây dẫn vẫn được coi "
               "là có thể bị đứt mạch nếu chúng chỉ đáp ứng các yêu cầu cơ "
               "bản)."))

    # H7 -> heading 13.4.3 (printed p.338).
    b.append(h4("13.4.3 Ảnh hưởng của các lỗi khác",
                "13.4.3 Effects of other faults"))
    # H8 (printed p.338).
    b.append(p("Khi một kết nối, cụm hoặc linh kiện đáp ứng các yêu cầu cơ "
               "bản của Tiêu chuẩn trong khi không có lỗi đếm được nào được "
               "áp dụng ở nơi khác trong mạch, nhưng không còn đáp ứng khi "
               "một (hoặc, trong trường hợp ‘ia’, hai) lỗi đếm được được áp "
               "dụng ở nơi khác, thì linh kiện, kết nối hoặc cụm đó không "
               "còn được coi là lỗi đếm được khi lỗi (các lỗi) đó được áp "
               "dụng và được coi là lỗi không đếm được có thể được áp dụng "
               "nếu nó ảnh hưởng bất lợi đến an toàn nội tại."))
    # H9+I1 (printed pp.338-339): joined across the page break.
    # Quirk 56: 'conplies'.
    b.append(p("Khi một linh kiện, cụm hoặc kết nối tuân thủ các quy định "
               "nâng cao của nguyên lý bảo vệ trong vận hành bình thường, "
               "nhưng không còn tuân thủ khi các lỗi thích hợp được áp dụng "
               "ở nơi khác trong mạch trong phạm vi của Tiêu chuẩn, thì "
               "linh kiện, cụm hoặc kết nối đó cũng bị hạ xuống mức được coi "
               "là lỗi đếm được hoặc lỗi không đếm được, tùy theo các điều "
               "kiện mà nó hoạt động trong những điều kiện lỗi đó."))
    b.append(note("<b>Lưu ý về 'conplies'.</b> Mục 13.4.3 in 'conplies with "
                  "enhanced specifications' thay vì 'complies'. Lỗi chính "
                  "tả này được giữ nguyên trong bản tiếng Anh; bản tiếng "
                  "Việt theo nghĩa định."))
    # I2 (printed p.339).
    b.append(p("Các lỗi của linh kiện, cụm hoặc kết nối chỉ quan trọng trong "
               "chừng mực chúng làm tăng nguy cơ nguy hiểm và, do đó, nếu "
               "chúng có tác động ngược lại (ví dụ, lỗi ngắn mạch ở đầu ra "
               "của thiết bị liên kết) thì không được áp dụng."))

    # I3 -> heading 13.4.4 (printed p.339).
    b.append(h4("13.4.4 Linh kiện, cụm hoặc kết nối không thể hỏng",
                "13.4.4 Infallible component, assembly or interconnection"))
    # I4 (printed p.339). Quirk 57.
    b.append(p("Khi bất kỳ linh kiện, cụm hoặc kết nối nào đáp ứng các yêu "
               "cầu bổ sung của nguyên lý bảo vệ đã thảo luận trong các Mục "
               "13.4.3 và 13.4.4, cho phép coi nó là không chịu hỏng hóc, "
               "thì nó được gọi là không thể hỏng. Tuy nhiên, nó chỉ được "
               "xem là không thể hỏng trong chế độ mà các yêu cầu bổ sung "
               "được áp dụng (ví dụ, một điện trở có cấu tạo đặc biệt có "
               "thể được coi là không thể hỏng về mặt hỏng thành giá trị "
               "điện trở thấp hơn giá trị quy định, nhưng vẫn được giả định "
               "là có thể bị đứt mạch). Tương tự, nó chỉ được coi là không "
               "thể hỏng với điều kiện các điều kiện tại điểm nối của nó "
               "vào mạch vẫn giữ nguyên. Nếu chúng thay đổi sao cho nó phải "
               "chịu, ví dụ, điện áp hoặc dòng điện cao hơn, thì nó có thể "
               "không còn là không thể hỏng trong những hoàn cảnh đó."))
    b.append(note("<b>Lưu ý về tự trích dẫn trong 13.4.4.</b> Bản in nói "
                  "'discussed in Sections 13.4.3 and 13.4.4' dù một mục "
                  "không thể tự trích dẫn chính nó; nhiều khả năng định "
                  "nói đến 13.4.2 và 13.4.3. Trích dẫn của bản in được giữ "
                  "nguyên."))

    # I5 -> heading 13.5 (printed p.339; two printed lines).
    b.append(h3("13.5 Xác nhận an toàn nội tại đối với đánh lửa do hồ quang "
                "và tia lửa",
                "13.5 Confirmation of intrinsic safety in respect of arc "
                "and spark ignition"))
    # I6 (printed p.339).
    b.append(p("Việc xác nhận an toàn nội tại được thực hiện bằng cách đảm "
               "bảo không có hồ quang hay tia lửa nào có khả năng đánh lửa, "
               "dù trong vận hành bình thường hay sau khi áp dụng các kịch "
               "bản lỗi khác nhau đã quy định trong Mục 13.3 ở trên."))
    # I7 (printed p.339): first half; Fig. 13.2 intervenes at the top of
    # printed p.340. Quirks 26, 28, 58, 59, 60, 61.
    b.append(p("Khả năng đánh lửa của bất kỳ phần nào của mạch an toàn nội "
               "tại (tức là thiết bị an toàn nội tại, cáp kết nối và phần "
               "của thiết bị liên kết nằm trong mạch an toàn nội tại - xem "
               "Hình 13.1) cần được chứng minh là không có khả năng gây đánh "
               "lửa bởi bất kỳ hồ quang hay tia lửa nào xảy ra tại những nơi "
               "mà hồ quang hoặc tia lửa đó được coi là có thể xảy ra, thường "
               "là ở những chỗ như giữa các dây dẫn, mắc nối tiếp với một "
               "dây dẫn, tại các cọc đấu nối, v.v., trừ khi cấu tạo của "
               "thiết bị bảo đảm rằng không thể xảy ra tia lửa như vậy (khi "
               "cấu tạo tạo ra tính không thể hỏng). Các bộ phận tạo thành "
               "các điện cực giữa đó tia lửa xảy ra rất khác nhau và, vì tính "
               "dễ đánh lửa của một tia lửa năng lượng thấp phụ thuộc đáng "
               "kể vào hình học của các điện cực này, cần có một thước đo "
               "cơ bản để đảm bảo tính lặp lại. Vì lý do này, một thiết bị "
               "thử tia lửa đặc biệt đã được phát triển để mô phỏng tia lửa "
               "có thể xảy ra và được thể hiện trong Hình 13.2 và 13.3. "
               "Thiết bị thử tia lửa này (gọi là breaklash ở Anh) nhạy hơn "
               "bất kỳ cấu hình điện cực thực tế nào thường gặp, vì nó dùng "
               "các tiếp điểm bằng dây vonfram rất nhỏ, đàn hồi hơn đồng làm "
               "một điện cực, nhờ đó tạo ra sự tự tin rằng nếu không đánh "
               "lửa xảy ra trong một phép thử dùng thiết bị này thì không "
               "đánh lửa sẽ xảy ra"))

    # J (printed p.340): Fig. 13.2 at the printed position, above the
    # continuation of I7. Quirks 27, 74.
    b.append(fig(2, FA.fig_f1302()))
    b.append(note("<b>Lưu ý về chú giải Hình 13.2.</b> Các số gọi ra bên cạnh "
                  "bản vẽ không theo thứ tự tăng dần; nhan đề cung cấp khóa "
                  "1–18 chuẩn xác, gồm '16 Gear wheel drive 50 : 12', '17 "
                  "Insulated coupling' và '18 Drive motor with reduction "
                  "gears 80 rev/min'. Lớp OCR đọc 'Contact wlre' và 'Clamp,'; "
                  "ảnh trang in cho 'Contact wire' và 'Clamp'. Nhan đề không "
                  "có dấu chấm cuối."))

    # J1 (printed p.340): continuation of I7.
    b.append(p("trong bất kỳ tình huống thực tế nào. Việc dùng cadimi cho "
               "đĩa dưới của thiết bị là để bao phủ tình huống mà cadimi, "
               "kẽm, magiê hoặc, ở mức độ thấp hơn, titan được đưa vào vật "
               "liệu bên trong thiết bị cần thử và có thể tạo thành các "
               "điện cực đánh lửa thực tế. Điều này là do người ta biết "
               "rằng các vật liệu này tăng tính dễ đánh lửa của tia lửa điện "
               "(có thể do giải phóng các gốc tự do) và làm cho đánh lửa dễ "
               "dàng hơn nhiều. Năng lượng khoảng 40 μJ được giải phóng "
               "hiệu quả trong một tia lửa sẽ đánh lửa hỗn hợp hydro/không "
               "khí lý tưởng khi có cadimi, trong khi khoảng 130 μJ là cần "
               "thiết khi không có cadimi cũng như các kim loại khác. Cadimi "
               "được dùng vì nó là kim loại nhạy nhất trong số các kim loại "
               "đang xét. Ngoài ra, mạ cadimi và kẽm rất phổ biến trong ngành "
               "cơ khí nên người ta cho rằng rất có khả năng, ngay cả khi "
               "các vật liệu này bị loại trừ trong quá trình chế tạo, công "
               "tác bảo trì sẽ đưa chúng vào trong sử dụng thông qua việc "
               "thay thế vít, v.v., và một hệ thống kiểm soát để ngăn điều "
               "này được coi là không thực tế."))
    b.append(note("<b>Lưu ý về đoạn thử tia lửa.</b> Bản in viết 'intrinsically "
                  "safe apparatus interconnecting cables' không có dấu phẩy "
                  "hay chữ 'and', viết 'Fig. 13.2 and 13.3' mà không lặp lại "
                  "'Fig.', gọi thiết bị là 'the breaklash in the UK' và viết "
                  "'neither cadmium or the other metals are present' trong "
                  "đó 'nor' sẽ hợp lý hơn. Lớp OCR cũng đọc '40 pJ' và "
                  "'130pJ' thay cho '40 μJ' và '130 μJ'. Tất cả dạng in được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt theo nghĩa "
                  "định."))

    # K1 (printed p.341): first half; Fig. 13.3 and Table 13.1 intervene.
    b.append(p("Cách vận hành là làm đầy buồng của thiết bị bằng khí thử phù "
               "hợp với phân nhóm mà thiết bị dự định dùng (các khí thử phù "
               "hợp được nêu trong Bảng 13.1). Sau đó thiết bị được hiệu "
               "chuẩn bằng cách bật nó để tạo tia lửa nhờ sự quay ngược "
               "chiều của hai đĩa, quay ngược chiều với tốc độ 80 rpm cho "
               "đĩa giữ"))

    # K (printed p.341): Fig. 13.3 at the printed position.
    b.append(fig(3, FA.fig_f1303()))
    # Quirks 29, 30, 62, 63.
    b.append(note("<b>Lưu ý về các nhãn Hình 13.3.</b> Nhãn 'Upper disc "
                  "dimension 38 mm' được in hai lần, mỗi lần cho một đĩa, dù "
                  "chỉ đĩa trên có kích thước đó; cả hai được giữ nguyên và "
                  "gắn cờ. Lớp OCR làm mất '0.2 mm minimum tungsten wire "
                  "length 11 mm' và bỏ sót 'Separation of discs 10 mm', cả "
                  "hai nhãn 'Upper disc dimension 38 mm' và 'Cadmium disc "
                  "diameter 38 mm'; ảnh trang in cung cấp các nhãn này. Cách "
                  "viết '80 rpm' (trang in 341) và '19.2rpm' (trang in 342) "
                  "không thống nhất như đã in."))

    # L (printed p.342): Table 13.1 at the printed position, before the
    # continuation of K1. Quirks 31, 32, 64; see also the table note.
    b.append(table(T1.HEAD131_VI, T1.ROWS131_VI, T1.CAPTION131_VI))
    b.append(note(T1.NOTE131_VI))
    b.append(note("<b>Lưu ý về Bảng 13.1 và khoảng cách số/đơn vị.</b> Nhan đề "
                  "in dấu gạch ngang kiểu en dash trước 'with electrical "
                  "safety factors' và các tiêu đề phụ in thường 'current' và "
                  "'energy'; lớp OCR đọc '±' thành 'f', '(% V/V)' thành "
                  "'(Yo W)' và dòng nguồn thành '(from BSEN 50020)'. Phần văn "
                  "bản in '24V dc' không có dấu cách nhưng '95 mH' có dấu "
                  "cách; cả hai được giữ nguyên."))

    # L1 (printed p.342): continuation of K1. Quirks 33, 65.
    b.append(p("các dây, và 19.2rpm cho đĩa cadimi. Sau đó các đĩa được cấp "
               "dòng điện nguồn hiệu chuẩn thể hiện trong Bảng 13.1, được "
               "tạo ra bằng cách đặt một điện trở mắc nối tiếp với nguồn "
               "hoặc ắc quy một chiều 24V để dòng điện là dòng ngắn mạch ở "
               "đầu ngoài của điện trở. Dòng điện này được đưa vào thiết bị "
               "thử qua một cuộn cảm không lõi 95 mH mắc nối tiếp và phải "
               "xảy ra đánh lửa trong vòng năm phút (400 vòng quay của đĩa "
               "trên) để xác nhận rằng thiết bị đã đạt độ nhạy tối thiểu. "
               "Cần lưu ý ở đây là không hiệu chuẩn độ nhạy tối đa và độ nhạy "
               "của mỗi phép thử có thể thay đổi. Dù có thể xảy ra sự thay "
               "đổi đáng kể về độ nhạy (người ta thường nói có thể tới 40 "
               "phần trăm, dù điều này không thể xác nhận), độ nhạy tối "
               "thiểu đủ (dù chưa phải hoàn toàn) để tạo sự tin tưởng rằng "
               "sẽ không xảy ra đánh lửa trong các hoàn cảnh thực tế. Do đó, "
               "sự thay đổi độ nhạy là một bất tiện hơn là một vấn đề an "
               "toàn."))
    # L2 (printed p.342).
    b.append(p("Sau khi hiệu chuẩn, thiết bị được làm đầy lại bằng hỗn hợp "
               "khí/không khí như cũ và hai đĩa của nó được nối mỗi đĩa vào "
               "một trong các điểm mà tại đó tia lửa được coi là có thể xảy "
               "ra, sau khi áp dụng các yêu cầu về lỗi cho nguyên lý bảo vệ "
               "và các hệ số an toàn cần thiết đã mô tả trong các Mục 13.3.1 "
               "và 13.3.2. Sau đó thiết bị được cấp điện và cho hoạt động "
               "trong 5 phút (400 vòng quay của đĩa trên) đối với mạch một "
               "chiều hoặc 12,5 phút (1000 vòng quay của đĩa trên) đối với "
               "mạch xoay chiều. Nếu không xảy ra đánh lửa và hỗn hợp "
               "khí/không khí trong buồng sau đó được cho nổ bằng cách lại "
               "áp dụng nguồn hiệu chuẩn vào các đĩa trong 5 phút, thì phép "
               "thử được coi là thành công."))
    # L3 (printed p.342).
    b.append(p("Lý do dùng 1000 vòng quay trong trường hợp mạch xoay chiều là "
               "vì không phải lúc nào cũng có thể sắp xếp để tia lửa xảy ra "
               "ở đỉnh của một chu kỳ và, vì vậy, để tối đa hóa khả năng "
               "làm được như vậy, thời gian thử được kéo dài."))
    # L4+M1 (printed pp.342-343): joined across the page break.
    b.append(p("Trong trường hợp mạch một chiều, phép thử thường dừng ở 2,5 "
               "phút và cực tính của kết nối được đảo ngược để đảm bảo rằng "
               "mọi ảnh hưởng của cực tính trong mạch đang thử đều được tính "
               "đến. Với mạch điện dung và, ở mức độ thấp hơn, mạch cảm ứng "
               "và mạch điện trở, cần đảm bảo rằng mạch có thể trở về trạng "
               "thái hở mạch giữa các tia lửa và điều này có thể không thực "
               "hiện được khi dùng thiết bị thử tiêu chuẩn. Vấn đề này được "
               "khắc phục bằng cách tháo dây khỏi đĩa trên để cho phép có "
               "thêm thời gian tích lại điện. Khi làm vậy, số vòng quay cho "
               "cả hiệu chuẩn và phép thử phải tăng lên (ví dụ, nếu tháo hai "
               "dây đối diện để chỉ còn hai dây, thời gian thử và hiệu "
               "chuẩn cần tăng gấp đôi)."))

    # M2 -> heading 13.5.1 (printed p.343). Quirks 34, 35, 66, 67.
    b.append(h4("13.5.1 Đạt được các hệ số an toàn",
                "13.5.1 Achievement of safety factors"))
    b.append(note("<b>Lưu ý về 13.5.1 và các trích dẫn chéo.</b> Nhan đề được "
                  "đánh số '13.5.1' trong ảnh trang in (OCR đọc '13.5. I'). "
                  "Văn bản in 'for testing purposed by a specially "
                  "constructed circuit' (lỗi chính tả 'purposed' của nguyên "
                  "bản) và trích dẫn 'Table 13.6 on page 362'; không có Bảng "
                  "13.6 nào trên trang đó, vốn có Bảng 13.1. Tất cả dạng in "
                  "được giữ nguyên."))
    # M3 (printed p.343).
    b.append(p("Các hệ số an toàn 1.5 khi được quy định là cần thiết (xem "
               "Mục 13.4) thường đạt được bằng cách chỉnh sửa thiết bị đang "
               "thử để tạo ra hệ số yêu cầu. Nếu điều này không thuận tiện "
               "hoặc không thể, mạch có thể được mô phỏng cho mục đích thử "
               "bằng một mạch chế tạo đặc biệt, dù cần hết sức cẩn trọng "
               "trong hoàn cảnh đó để đảm bảo rằng mạch mô phỏng thực sự "
               "giống hệt mạch thực. Vì lý do này, luôn ưu tiên tác động trên "
               "mạch thực. Các hệ số an toàn này luôn bổ sung cho bất kỳ "
               "điều chỉnh nào thực hiện để tính đến những thứ như biến "
               "động điện lưới. Mọi phép thử phải được thực hiện trong (ít "
               "nhất) các điều kiện sau. Thứ nhất, nguồn điện lưới cấp cho "
               "thiết bị phải tăng lên 110 phần trăm giá trị danh định của "
               "chúng (giả định rằng dung sai điện lưới không vượt quá mức "
               "này). Thứ hai, mọi nguồn cấp khác và mạch hạn chế điện áp, "
               "cùng các thiết bị như diode zener, phải được tăng lên để "
               "cho điện áp tối đa xảy ra ở sự kết hợp xấu nhất của dung sai "
               "linh kiện với bất kỳ nguồn lưới nào cấp cho chúng ở 110 phần "
               "trăm giá trị danh định. Thứ ba, ắc quy phải được sắp xếp hoặc "
               "mô phỏng để cho các điện áp quy định trong Bảng 13.6 trên "
               "trang 362."))
    # M4 (printed p.343).
    b.append(p("Các hành động trên cần được thực hiện trong mọi trường hợp "
               "nhưng, ngoài ra, khi yêu cầu hệ số an toàn 1.5, các hành động "
               "sau cũng phải được thực hiện trước khi bắt đầu phép thử. "
               "Thứ nhất, đối với mạch điện trở, dòng điện chảy vào ngắn mạch "
               "phải tăng lên 1.5 lần giá trị lớn nhất bình thường của nó "
               "bằng cách giảm các thứ như điện trở hạn chế dòng, hoặc nếu "
               "điều này không thể thì bằng cách tăng điện áp trong mạch, dù "
               "điều này tạo ra một phép thử nặng hơn. Việc này cần được "
               "thực hiện ngay cả với các nguồn cấp có bảo vệ crowbar, dù "
               "trong trường hợp này phải sắp xếp sao cho nguồn phục hồi "
               "giữa các lần ngắn mạch do phép thử tạo ra, điều có thể yêu "
               "cầu cả việc tháo dây khỏi thiết bị thử lẫn thay đổi mạch "
               "crowbar."))
    # M5 (printed p.343).
    b.append(p("Thứ hai, đối với mạch cảm ứng, dòng điện qua cuộn cảm cần "
               "tăng lên 1.5 lần giá trị đạt được khi mọi nguồn đều ở giá trị "
               "lớn nhất của chúng, như đã quy định bằng các phương pháp xác "
               "định cho mạch điện trở ở trên, dù cần cẩn trọng để đảm bảo "
               "rằng bản thân mạch điện trở không tự trở nên có khả năng "
               "đánh lửa do cách này và cho kết quả thử sai lệch. Thứ ba, đối "
               "với mạch điện dung, điện áp trên điện dung của mạch cần tăng "
               "lên 1.5 lần giá trị lớn nhất mà nó đạt được trong điều kiện "
               "xấu nhất, có tính đến dung sai, v.v., và cần đảm bảo rằng "
               "mạch không trở nên có khả năng đánh lửa do điện trở và cho "
               "kết quả sai lệch."))
    # M6+N1 (printed pp.343-344): joined across the page break.
    b.append(p("Các phương pháp xác định điều kiện thử nêu trên áp dụng cho "
               "các mạch cảm ứng, điện dung hoặc điện trở đơn giản. Trong "
               "hầu hết các trường hợp thực tế, mạch sẽ chứa ít nhất hai "
               "trong số các thông số (ví dụ, công suất điện trở và năng "
               "lượng điện dung, công suất điện trở và năng lượng cảm ứng, "
               "hoặc cả năng lượng cảm ứng lẫn điện dung). Trong những "
               "trường hợp như vậy hoặc khi mạch chứa cả ba thông số, thường "
               "cần thử với hệ số an toàn tạo ra bằng tăng dòng điện, và "
               "lặp lại phép thử với hệ số này tạo ra bằng tăng điện áp để "
               "bao phủ mọi khả năng."))
    # N2 (printed p.344). Quirk 68.
    b.append(p("Khi việc tăng dòng điện hoặc điện áp không được coi là thuận "
               "tiện như một giải pháp thay thế được chấp nhận, có thể thay "
               "đổi khí thử để tạo ra hệ số an toàn yêu cầu. Các hỗn hợp khí "
               "có hệ số cho các phân nhóm khác nhau được nêu trong Bảng 13.2 "
               "cùng với các dòng hiệu chuẩn giảm cho các hỗn hợp khí này. "
               "Các dòng thử được tạo ra bằng cách đặt một điện trở hạn chế "
               "mắc nối tiếp với nguồn một chiều 24V sao cho dòng điện thực "
               "chất là dòng ngắn mạch và sau đó đưa dòng điện này vào thiết "
               "bị thử qua một cuộn cảm không lõi 95 mH mắc nối tiếp."))
    b.append(note("<b>Lưu ý về chữ 'the' lạc đề.</b> Bản in viết 'so that the "
                  "current is actually the short circuit current and the "
                  "feeding this current to the test apparatus via a series "
                  "95 mH air-cored inductance'. Chữ 'the' trước 'feeding' "
                  "được giữ nguyên trong bản tiếng Anh; bản tiếng Việt theo "
                  "nghĩa định."))

    # N3 (printed p.344): Table 13.2 at its printed position.
    # Quirk 69 is covered by the appended table note.
    b.append(table(T1.HEAD132_VI, T1.ROWS132_VI, T1.CAPTION132_VI))
    b.append(note(T1.NOTE132_VI))
    b.append(note("<b>Lưu ý về các ghi chú của Bảng 13.2.</b> Dòng nguồn in "
                  "nghiêng viết thường '(gas mixtures from BS/EN 50020)' và "
                  "Ghi chú bên dưới là 'Note: These mixtures provide safety "
                  "factors equivalent to a 1.5 safety factor on current or "
                  "voltage.' Lớp OCR đọc '±' thành 'i' hoặc 'f' và '(% V/V)' "
                  "thành '(Yo W)'; ảnh trang in là nguồn quyết định. Các "
                  "nhãn phân nhóm lặp lại và ô 'None' đúng như bản in."))

    # N4 -> heading 13.5.2 (printed p.344).
    b.append(h4("13.5.2 Đánh giá mạch", "13.5.2 Assessment of circuits"))
    # N5 (printed p.344). Quirk 37.
    b.append(p("Để hỗ trợ thiết kế mạch và đơn giản hóa quá trình xác nhận "
               "an toàn nội tại, một bộ đường cong đã được xây dựng để xác "
               "định độ nhạy tối thiểu của thiết bị thử và có thể được dùng "
               "trong các trường hợp mà mạch đơn giản và có thể xác định "
               "một cách chắc chắn. Các đường cong được dùng dự định cho các "
               "mạch đơn giản, ở đó các đường cong điện dung chỉ liên quan "
               "đến tia lửa điện dung, các mạch cảm ứng chỉ với tia lửa cảm "
               "ứng và các mạch điện trở chỉ với tia lửa điện trở. Tuy "
               "nhiên, các mạch thực tế hiếm khi đạt được mức độ thuần khiết "
               "như vậy, nên việc sử dụng các đường cong có giới hạn. Tình "
               "huống được hỗ trợ bởi bản chất của sự đánh lửa vốn khác "
               "nhau đối với các nguồn khác nhau (ví dụ, cảm ứng, điện dung "
               "hoặc điện trở)."))
    b.append(note("<b>Lưu ý về 'idenhfy'.</b> Lớp OCR đọc 'idenhfy' ở chỗ ảnh "
                  "trang in là 'identify'; cách đọc từ ảnh trang in được "
                  "dùng."))

    # O1 -> unnumbered heading 'Inductive circuits' (printed p.345).
    b.append(h4("Mạch cảm ứng", "Inductive circuits"))
    # O2 (printed p.345). Quirk 70.
    b.append(p("Cơ chế đánh lửa cảm ứng thường là tia lửa ngắt mạch tạo ra "
               "khi các tiếp điểm ngắt ra và một sức điện động ngược cao "
               "được sinh ra do sự sụp đổ của từ trường (xem Hình 13.4). Vì "
               "tia lửa không được tạo ra bởi ngắn mạch (vì khi đó hầu như "
               "không có hoặc có rất ít năng lượng cảm ứng tích trữ) mà bởi "
               "sự ngắt của mạch cảm ứng khi sức điện động ngược tìm cách "
               "duy trì dòng điện, nó tăng lên mức cao, duy trì tia lửa hoặc "
               "hồ quang, cho đến khi toàn bộ năng lượng được tiêu tán. Tia "
               "lửa cảm ứng là loại hiệu quả nhất trong việc giải phóng năng "
               "lượng vào tia lửa và, trong thiết bị thử, các năng lượng sau "
               "đây là đủ để đánh lửa các khí thử cho ba phân nhóm."))
    b.append(note("<b>Lưu ý về 'back emf' và 'back EMF'.</b> Câu đầu in 'back "
                  "emf' viết thường và một câu sau trong cùng đoạn in 'back "
                  "EMF' viết hoa. Cả hai được giữ nguyên như bản in."))

    # O3 (printed p.345): Fig. 13.4 at the printed position.
    b.append(fig(4, FA.fig_f1304()))
    # Quirk 71, 74.
    b.append(note("<b>Lưu ý về các nhãn Hình 13.4.</b> Bản vẽ ghi 'Arc/spark "
                  "gap' có dấu gạch chéo và cho 'L = inductance' cùng 'r = "
                  "internal resistance' bằng các ký hiệu in nghiêng viết "
                  "thường; các ký tự nhỏ tại cọc đấu nối là dấu không đọc "
                  "được, không phải chữ. Nhan đề không có dấu chấm cuối. Các "
                  "nhãn in được giữ nguyên."))

    # P1 (printed p.346): displayed energy list. Quirks 39, 72.
    b.append(eq("IIA = 320 μJ<br>IIB = 120 μJ<br>IIC = 40 μJ"))
    b.append(note("<b>Lưu ý về giá trị IIB xung đột.</b> Danh sách trình bày ở "
                  "trang in 346 cho 'IIB = 120 μJ' trong khi nhãn đường cong "
                  "trong Hình 13.5 cho 'IIB (160 μJ)'. Cả hai giá trị in "
                  "được giữ lại; IIA (320 μJ) và IIC (40 μJ) thì thống "
                  "nhất."))
    # P2 (printed p.346).
    b.append(p("Hình 13.5 cho thấy mức độ tự cảm tối thiểu để đánh lửa ở "
               "24 V và các dòng điện khác nhau từ loại nguồn thể hiện trong "
               "Hình 13.4, và Hình 13.6 cho thấy thông tin tương tự cho các "
               "điện áp thấp hơn. (Ở điện áp trên 24 V, thông tin trong Hình "
               "13.5 là phù hợp). Các giá trị này là trường hợp xấu nhất vì "
               "chúng đề cập đến các cuộn cảm không lõi và, vì hầu hết các "
               "cuộn cảm có lõi từ bằng sắt hoặc các vật liệu từ tính rắn "
               "khác kém hiệu quả hơn về mặt phóng điện, nên có thể dùng "
               "chúng một cách chắc chắn nói chung."))

    # P3 (printed p.346): Fig. 13.5 at the printed position.
    b.append(fig(5, FA.fig_f1305()))
    # Quirks 40, 41, 42, 73, 74.
    b.append(note("<b>Lưu ý về Hình 13.5.</b> Lớp OCR đọc '1 .o' thay cho vạch "
                  "trục tung '1.0' và bỏ sót vạch '0.01' được in. Nhan đề in "
                  "'threshold/inductive' không có dấu cách quanh dấu gạch "
                  "chéo, 'with V = 24 V' có dấu cách và không có dấu chấm "
                  "cuối sau Ghi chú. Nhãn đường cong 'IIB (160 μJ)' xung đột "
                  "với danh sách 'IIB = 120 μJ' trình bày ở trên. Nhan đề các "
                  "Hình 13.1–13.5 được in đậm và không nhan đề nào có dấu "
                  "chấm cuối sau mục cuối; tất cả được giữ nguyên từng chữ."))
    return "".join(b)


def body_en():
    b = []

    # A0 (printed p.331). The shell owns the chapter h2; the module owns
    # the printed standard subtitle lines and the chapter-opening prose.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("<b>(BS/EN 50020 — Apparatus)<br>"
               "(BS 5501, Part 9 — Systems)</b>"))
    # Quirks 43, 44.
    b.append(note("<b>Note on the chapter opening.</b> The print sets the "
                  "number 13 between rules, a bold-italic three-line title "
                  "and two centred standard lines, '(BS/EN 50020 — "
                  "Apparatus)' and '(BS 5501, Part 9 — Systems)', with em "
                  "dashes and curly quotes around 'i'. The opening prose is "
                  "one continuous justified paragraph with no first-line "
                  "indents and reads 'It is therefore, a 'system concept',' "
                  "with a comma after 'therefore'. The printed forms are "
                  "kept in English; the Vietnamese follows the intended "
                  "meaning."))
    # A1+B1 (printed pp.331-332): joined across the page break.
    # Quirks 1-5, 38, 39.
    b.append(p("Intrinsic safety is unique among the protection concepts in "
               "its mode of operation. All other concepts rely on prevention "
               "of sparking and hot surfaces, the exclusion of explosive "
               "atmospheres from such ignition sources, or containment of "
               "any explosion produced. Intrinsic safety is quite different "
               "in that no attempt is made to prevent sparking and no attempt "
               "is made to exclude explosive atmospheres. Safety is achieved "
               "by limiting the power and energy (apart from limited cases "
               "where stored energy is concerned and specific measures are "
               "taken to prevent or limit its rate of release as a spark or "
               "arc) in the hazardous area to levels below those which can "
               "cause ignition. As hydrogen, for example, can be ignited by "
               "around 20 μJ in ideal circumstances the energy fed to and "
               "used in a hazardous area is severely limited and intrinsic "
               "safety is only really practicable for such things as "
               "intelligence gathering, analysis, and limited operating "
               "functions. The technique depends, almost uniquely, on the "
               "effective limitation of the energy which can be fed to a "
               "hazardous area, as well as the performance of the apparatus "
               "in the hazardous area itself. It is therefore, a 'system "
               "concept', where the detail of the apparatus in the hazardous "
               "area, in a non-hazardous area with which it is "
               "interconnected, and the means of interconnection are equally "
               "important in achieving safety. Likewise, because it acts by "
               "limiting available energy and restricting storage or release "
               "of stored energy, it relies on the circuits within the "
               "apparatus themselves, rather than applying enclosures or "
               "other additional means to achieve safety. This has the "
               "advantage of freeing the apparatus from the limitations "
               "produced in many of the other types of protection (i.e., if "
               "sparking which occurs is not ignition capable, the isolation "
               "required in other types of protection for "
               "connection/disconnection purposes becomes unnecessary). It "
               "does, however, make the protection concept somewhat more "
               "complex in construction and use. Notwithstanding this, the "
               "advantages far outweigh the complexity problems as evidenced "
               "by the fact that all normal installations in Zone 0 and "
               "almost all instrument installations in Zone 1 are "
               "intrinsically safe. Its use in Zone 0 is significant as no "
               "other standard protection concept is accepted as a matter of "
               "normal practice in Zone 0. This is because, by its nature, "
               "the level of security in an intrinsically safe system can be "
               "varied depending upon the hazardous area risk, so that in "
               "Zone 0 (where the risk is greatest) the level of security "
               "can be increased to a much higher level than is possible for "
               "any of the other single standard types of protection."))
    b.append(note("<b>Note on OCR errors at the opening.</b> The text layer "
                  "reads 'intrinsic safety 7’', 'BSIEN 50020 - Apparatus' and "
                  "'BS 5501, Part 9 - Systems' for the title lines, '20 FJ' "
                  "for '20 μJ', and 'llus has the advantage' for 'This has "
                  "the advantage'. The running header on printed p.345 is "
                  "OCR'd as 'Protection concept intrinsic safefy 7’' but "
                  "prints 'Protection concept intrinsic safety ‘i’'. The "
                  "displayed list on printed p.346 is OCR'd as '320 pJ / "
                  "120pJ / 40 pJ' but prints '320 μJ / 120 μJ / 40 μJ'. The "
                  "render readings are used throughout."))

    # B2 (printed p.332). Quirks 45, 46.
    b.append(p("Intrinsic safety is second only to flameproof enclosure "
               "(Chapter 11) in age, having been developed in the coalmining "
               "industry to cover the simple signalling systems used in that "
               "industry (typically, leclanche cell/bell circuits) which were "
               "suspected of causing ignition in at least two explosions, one "
               "of which was the worst which ever occurred in the UK."))
    b.append(note("<b>Note on 'leclanche' and 'Physicalisch'.</b> The print "
                  "uses lowercase 'leclanche cell/bell circuits' without an "
                  "accent, and spells the German institute 'Physicalisch "
                  "Technische Bundesanstalt' (normally 'Physikalisch'). Both "
                  "printed forms are retained in English; the Vietnamese "
                  "follows the intended meaning."))

    # B3 -> heading 13.1 (printed p.332).
    b.append(h3("13.1 The situation in respect of standardization",
                "13.1 The situation in respect of standardization"))
    # B4 (printed p.332). Quirks 6-16, 47.
    b.append(p("Although used widely in the UK for such things as signalling "
               "systems, public address systems, solenoid valves and sensors, "
               "no definitive National Standard existed until 1977, probably "
               "because the applications prior to that date were relatively "
               "simple. A British Standard, BS 1259,¹ had existed from 1958 "
               "but was significantly lacking in detail and with the rapid "
               "expansion of the use of the protection concept for reasons "
               "described earlier, there was a significant lack of detailed "
               "constructional requirements by the late 1960s. Because a "
               "European Standard was being produced it was not considered "
               "as appropriate to produce a National Standard and this "
               "resulted in EECS/BASEEFA² being the only national "
               "certification/approvals body in the UK at that time, producing "
               "their own document, SFA 3012,³ in 1972 which remained in "
               "force until the publication of the European Standard as BS "
               "5501, Part 7⁴ in 1977 (the UK publication of EN 50020.⁵) "
               "Thus, from the rapid increase of the use of the protection "
               "concept which came on the heels of the equally rapid "
               "introduction of the transistor to replace the thermionic "
               "valve, and the equally rapid expansion of the requirements "
               "for sophisticated monitoring and control of complex "
               "processes, until the publication of SFA 3012,³ arbitration on "
               "what was intrinsically safe had to be by EECS/BASEEFA² "
               "against essentially unpublished rules. A similar situation "
               "existed elsewhere and the Physicalisch Technische "
               "Bundesanstalt (PTB⁶) in Germany had a similar role. SFA 3012 "
               "was not produced by EECS/BASEEFA in isolation but was derived "
               "from an International Standard being produced by the "
               "International Electrotechnical Commission (IEC⁷) as IEC "
               "79-11⁸. This document was also used as a basis for BS 5501, "
               "Part 7⁴ by the European Standards body CENELEC⁹."))
    b.append(note("<b>Note on superscript footnote numerals.</b> The print "
                  "places ¹ after 'BS 1259,', ² after 'EECS/BASEEFA' (twice), "
                  "³ after 'SFA 3012,' (twice), ⁴ after 'Part 7' (three "
                  "times), ⁵ after 'EN 50020.' inside the parenthesis, ⁶ in "
                  "'(PTB⁶)', ⁷ in '(IEC⁷)', ⁸ after 'IEC 79-11', ⁹ after "
                  "'CENELEC', ¹⁰ after 'BS/EN 50020 (1995),' and after "
                  "'BS/EN 50020', and ¹¹ after 'BS 5501, Part 9 (1982).'. "
                  "The OCR text layer misreads these in turn as ';', '?', "
                  "':', '4', '.5', '3', '2', '6', '7', '8', an apostrophe, "
                  "'1°', '1O' and '.11'. The printed superscripts, including "
                  "the full stop inside the parenthesis before a superscript, "
                  "are retained."))
    # B5+C1 (printed pp.332-333): joined across the page break.
    # Quirks 17, 18, 19, 48, 49.
    b.append(p("Even so, the technology of intrinsic safety was still very "
               "much in its infancy in the new more complex scenario which "
               "ensued where semiconductors were applied causing many "
               "discussions and developments in BS 5501, Part 7, as witnessed "
               "by the number of papers and articles produced in journals and "
               "at conferences on the subject and the discussion which these "
               "led to. All of this discussion produced rapid development of "
               "the protection concept and led to interpretive documents "
               "which were issued in the UK to clarify problems encountered "
               "with the application of BS 5501, Part 7 - some 38 between "
               "1981 and 1992. These interpretation sheets, together with "
               "those produced by other CENELEC member countries, resulted "
               "in the publication by CENELEC of no less than eight amendments "
               "to the Standard and 20 interpretation sheets to clarify the "
               "meaning of the Standard – a far higher number than for any "
               "of the other European Standards in the range. All of these "
               "amendments and interpretations are now included in BS/EN "
               "50020 (1995),¹⁰ the second edition of the European Standard. "
               "(An interpretation sheet does not amend a Standard but only "
               "clarifies its meaning, unlike an amendment which may do "
               "either or both)."))
    b.append(note("<b>Note on 'clarlfy' and parenthetical punctuation.</b> "
                  "The OCR text layer reads 'clarlfy' where the render prints "
                  "'clarify'. The parenthetical '(An interpretation sheet "
                  "does not amend a Standard but only clarifies its meaning, "
                  "unlike an amendment which may do either or both).' places "
                  "its full stop after the closing parenthesis. 'BS/EN 50020 "
                  "(1995),¹⁰' has a comma before the superscript while "
                  "'BS/EN 50020¹⁰' two sentences later has none - "
                  "inconsistent but as printed. The printed forms are kept."))
    # C2 (printed p.333).
    b.append(p("BS/EN 50020¹⁰ and its predecessor, BS 5501, Part 7⁴ carry "
               "specifications for intrinsically safe and associated "
               "apparatus only. As already noted, the protection concept is "
               "unique in that it is a system concept and it is necessary to "
               "determine the safety of a system in all cases. Because of the "
               "complexity involved this cannot be done by an installation "
               "Code in all cases, and a further European Standard exists to "
               "define how items of apparatus and interconnecting cabling can "
               "be combined to form intrinsically safe systems. This is BS "
               "5501, Part 9 (1982).¹¹"))

    # C3 -> heading 13.2 (printed p.333).
    b.append(h3("13.2 Basic application of the concept",
                "13.2 Basic application of the concept"))
    # C4 (printed p.333).
    b.append(p("As previously stated, intrinsic safety is a system concept "
               "relying for its security upon the detailed design of both "
               "the apparatus in the hazardous area, the apparatus in the "
               "non-hazardous area which is interconnected with it, and the "
               "interconnections between the two. This is unlike most other "
               "forms of protection where only the electrical protection "
               "circuits in the non-hazardous area are important as, in those "
               "protection concepts, the apparatus in the hazardous area is "
               "designed to maintain safety or minimize danger during "
               "isolation which automatically follows an equipment failure. "
               "There are, therefore, several elements which need to be "
               "considered when defining an intrinsically safe system."))

    # C5 -> heading 13.2.1 (printed p.333).
    b.append(h4("13.2.1 Intrinsically safe apparatus",
                "13.2.1 Intrinsically safe apparatus"))
    # C6+D1 (printed pp.333-334): joined across the page break.
    # Quirk 50.
    b.append(p("This is defined as ‘Apparatus in which all the circuits are "
               "intrinsically safe’. This apparatus is intended for "
               "installation in a hazardous area and will be designed so "
               "that, when fed from appropriate apparatus (associated "
               "apparatus) in a non-hazardous area (associated apparatus) it "
               "will not produce incendive arcs, sparks or hot surfaces, "
               "either when it is operating normally or when faults occur in "
               "the electrical circuits and components within it and its "
               "interconnecting cables. The use of faults within the apparatus "
               "and its interconnecting cables is the method by which it "
               "derives its level of safety. These circuit or component "
               "faults have a particular statistical likelihood of occurrence "
               "and (as when one has occurred the likelihood of another "
               "independent fault occurring is considerably lower) the "
               "overall security of the apparatus is determined by the number "
               "of such faults occurring. To give a level of security of "
               "faults occurring which is acceptable, the entire apparatus is "
               "subject to detailed specification as to the quality of its "
               "component parts. Therefore, the possibility of faults "
               "occurring is defined and repeatable. Figure 13.1 indicates "
               "the position of intrinsically safe apparatus within an "
               "intrinsically safe system."))
    b.append(note("<b>Note on the duplicated phrase.</b> The print reads "
                  "'when fed from appropriate apparatus (associated "
                  "apparatus) in a non-hazardous area (associated apparatus)'; "
                  "the phrase '(associated apparatus)' appears twice. It is "
                  "retained in English; the Vietnamese keeps both "
                  "occurrences."))

    # D2 -> heading 13.2.2 (printed p.334).
    b.append(h4("13.2.2 Associated apparatus", "13.2.2 Associated apparatus"))
    # D3 (printed p.334).
    b.append(p("Associated apparatus is defined as apparatus which contains "
               "both intrinsically safe and non-intrinsically safe circuits, "
               "designed so that the non-intrinsically safe circuits cannot "
               "adversely affect the intrinsically safe circuits within it "
               "and to which it is connected. Such apparatus is not intended "
               "to be installed in the hazardous area but is intended to "
               "define the electrical power and energy constituting the "
               "input to the intrinsically safe apparatus to which it is "
               "connected. Its role is to define the voltage, current, power "
               "and energy (input) to such apparatus and to ensure that even "
               "when faults occur those levels are not exceeded. Again, "
               "faults in the components and circuits within the associated "
               "apparatus are considered in the equation and the number of "
               "these taken into account allows the determination of the "
               "level of safety achieved. As with intrinsically safe "
               "apparatus, requirements are applied to the quality of "
               "component parts to ensure a definable, repeatable level of "
               "safety. Figure 13.1 shows the position of the associated "
               "apparatus in an intrinsically safe system."))

    # D4 (printed p.334): Fig. 13.1 at its printed position.
    b.append(fig(1, FA.fig_f1301()))
    # Quirks 21, 74.
    b.append(note("<b>Note on the caption of Fig. 13.1.</b> The caption prints "
                  "the Notes numbered '(1) (2) (3)' with Arabic digits (the "
                  "OCR reads '(I)' for '(1)'), a comma in 'etc.,' in Note 2, "
                  "and no final full stop after 'additional evaluation'. The "
                  "printed caption is retained verbatim in the figure; the "
                  "Vietnamese follows the intended meaning."))

    # E1 -> heading 13.2.3 (printed p.335).
    b.append(h4("13.2.3 Interconnections", "13.2.3 Interconnections"))
    # E2 (printed p.335).
    b.append(p("The interconnections between intrinsically safe apparatus and "
               "associated apparatus are also important for two reasons. "
               "First, they are normally cables and are capable of storing "
               "energy when electrical currents are passed through them due "
               "to their inductance and capacitance. Second, as it is common "
               "to use multicircuit multicore cables for interconnection, "
               "there is the possibility of faults within such cables which "
               "could give rise to the interconnection of separate "
               "intrinsically safe circuits whose interconnection could give "
               "rise to a composite circuit which is ignition capable. "
               "Although these cables are not as dangerous as those "
               "containing, for example, mains circuits their construction "
               "must reach a minimum level to avoid problems, particularly "
               "where multicore cables are involved."))

    # E3 -> heading 13.2.4 (printed p.335).
    b.append(h4("13.2.4 Simple apparatus (devices)",
                "13.2.4 Simple apparatus (devices)"))
    # E4 (printed p.335). Quirks 22, 23, 51, 52.
    b.append(p("It is recognized that some devices, such as switches and "
               "terminal boxes and similar items of simple construction, do "
               "not contribute to the energy available for sparking or "
               "heating as they are essentially inert and their parameters "
               "can easily be defined because of their simplicity. These are "
               "called simple apparatus and the definition is that such "
               "apparatus will be a component or assembly of components of "
               "simple construction having well-defined electrical "
               "parameters. This would include thermocouples (but not "
               "thermopiles), resistance thermometers, switches, terminals "
               "and similar devices, and their use in intrinsically safe "
               "circuits is given a great degree of freedom because of their "
               "simplicity. Unfortunately, many attempts have been made to "
               "extend the use of this type of defined apparatus to cover "
               "complicated assemblies of components on the basis of the "
               "fact that no inductance or capacitance is present in such "
               "assemblies. Such an approach should be resisted as it would "
               "almost certainly lead to errors which could have disastrous "
               "results. It should be remembered that the original definition "
               "of such apparatus in BS 5501 Part 1 (1977)¹² was 'devices in "
               "which, according to the manufacturers specifications, none "
               "of the values of 1.2 volts, 0.1 amps 20μJ or 25mW were "
               "exceeded'. Clearly the initial intent was to limit the "
               "relaxations to devices (components) and it was only when it "
               "was recognized that some assemblies of components (e.g., "
               "terminal boxes) could fit the same limitations that device "
               "was replaced by apparatus. The intent, however, remains the "
               "same and the relaxations in the protection concept for simple "
               "apparatus are intended only to apply to devices and very "
               "simple assemblies."))
    b.append(note("<b>Note on the simple-apparatus definition.</b> The print "
                  "quotes BS 5501 Part 1 (1977)¹² as 'devices in which, "
                  "according to the manufacturers specifications, none of "
                  "the values of 1.2 volts, 0.1 amps 20μJ or 25mW were "
                  "exceeded': no comma after 'amps', no apostrophe in "
                  "'manufacturers', and no space in '20μJ' or '25mW'. The OCR "
                  "reads '20pJ' for '20μJ'. The line 'intrinsically safe - "
                  "that is,' uses a spaced hyphen. The printed wording is "
                  "retained in English; the Vietnamese follows the intended "
                  "meaning."))

    # E5 -> heading 13.2.5 (printed p.335).
    b.append(h4("13.2.5 The intrinsically safe circuit",
                "13.2.5 The intrinsically safe circuit"))
    # E6+F1 (printed pp.335-336): joined across the page break.
    b.append(p("The intrinsically safe circuit is the basic intrinsically "
               "safe block. It is, unlike the other protection concepts, that "
               "part of the intrinsically safe system where the energy levels "
               "are intrinsically safe - that is, all of the circuit "
               "downstream of the components in the associated apparatus "
               "which define the voltage, current, power and energy fed to "
               "the hazardous area. The intrinsically safe circuit normally "
               "comprises of the intrinsically safe apparatus, the "
               "interconnecting cables, any simple apparatus fitted to the "
               "circuit, and those parts of the associated apparatus "
               "downstream of the limiting components. This is, in fact, the "
               "basic building block of intrinsic safety, rather than the "
               "intrinsically safe apparatus (unlike the case of the other "
               "protection concepts)."))

    # F2 -> heading 13.2.6 (printed p.336).
    b.append(h4("13.2.6 The intrinsically safe system",
                "13.2.6 The intrinsically safe system"))
    # F3 (printed p.336).
    b.append(p("The intrinsically safe system is the entirety of the "
               "installation including all parts which have an effect on "
               "intrinsic safety. It includes all parts of the associated "
               "apparatus, unlike the intrinsically safe circuit which does "
               "not."))

    # F4 -> heading 13.3 (printed p.336).
    b.append(h3("13.3 Levels of intrinsic safety",
                "13.3 Levels of intrinsic safety"))
    # F5 (printed p.336). Quirks 24, 53, 54.
    b.append(p("As already stated, intrinsic safety is the only single "
               "standard protection concept which is normally acceptable in "
               "Zone 0 and in its most secure form it offers a much higher "
               "level of security than do the other standard protection "
               "concepts. Recognizing this, it is also obvious that the "
               "standard of intrinsic safety which is suitable for Zone 0 "
               "(and hence all Zones) will probably be overly expensive and "
               "complex for systems intended for Zone 1 and less-hazardous "
               "areas. To overcome this potential problem, two grades of "
               "intrinsic safety are recognized, that called ‘ia’ (which is "
               "intended for all Zones) and that called ‘ib’ (which is "
               "intended for Zones 1 and 2 only). The grade can apply to: an "
               "item of intrinsically safe apparatus, which is assumed to be "
               "connected to associated apparatus with specific output "
               "parameters and has all the requirements of the particular "
               "grade of Intrinsic Safety applied within it; to an item of "
               "associated apparatus, where the output parameters are "
               "defined with all the conditions appropriate to the grade of "
               "intrinsic safety applied within it; or to an intrinsically "
               "safe system where the conditions appropriate to the grade of "
               "intrinsic safety are applied to the intrinsically safe system "
               "as a whole, rather than to the items of apparatus in "
               "isolation. Applications to items of apparatus in isolation "
               "is the most common approach as this allows parameters of "
               "apparatus to be defined in the worst case and determination "
               "of the safety of the interconnection is then much easier. It "
               "does, however, often lead to a higher level of overall "
               "security than is absolutely necessary."))
    b.append(note("<b>Note on the grade names and the colon list.</b> The "
                  "print uses the curly-quoted names ‘ia’ and ‘ib’ (the OCR "
                  "reads 'lib' for ‘ib’). The sentence 'The grade can apply "
                  "to: an item of ...' uses a colon to introduce a run-on "
                  "list with no enumeration markers. The printed forms are "
                  "kept in English; the Vietnamese adds commas for "
                  "readability without dropping any point."))

    # F6 -> heading 13.3.1 (printed p.336).
    b.append(h4("13.3.1 Intrinsic safety category ‘ia’",
                "13.3.1 Intrinsic safety category ‘ia’"))
    # F7+G1 (printed pp.336-337): joined across the page break.
    b.append(p("This is the higher grade of intrinsic safety intended to "
               "permit its intrinsically safe circuits to enter Zone 0, and "
               "apparatus and systems in this category are required to be "
               "incapable of causing ignition of an explosive atmosphere by "
               "arcs, sparks and hot surfaces in all of the following "
               "conditions."))
    # G2 (printed p.337): three numbered items, verbatim. Quirk 55.
    b.append(p("1. with no ‘countable faults’ applied and with the worst "
               "combination or combinations of ‘non-countable faults applied. "
               "(A safety factor of 1.5 is applied to voltage or current - or "
               "combination of both as appropriate - which is available in "
               "these conditions to cause an arc or spark but no safety "
               "factor is applied to that causing hot surfaces.);"))
    b.append(p("2. with any one of the possible ‘countable faults’ applied "
               "together, in each case, with the worst combinations of "
               "‘non-countable faults’ applied. (The safety factors applied "
               "in these conditions are as in 1 above.);"))
    b.append(p("3. with any two of the possible ‘countable faults’ applied "
               "together, in each case, with the worst combinations of "
               "‘non-countable faults’ applied. (In these conditions no "
               "safety factor is applied to voltage or current, or the "
               "combination thereof.)"))
    b.append(note("<b>Note on the numbered conditions in 13.3.1.</b> Item 1 "
                  "prints 'of ‘non-countable faults applied.' with an opening "
                  "quote and no closing mate, and uses spaced hyphens in "
                  "'voltage or current - or combination of both as "
                  "appropriate -'. Items 1 and 2 end with a semicolon, item 3 "
                  "with a full stop. The printed punctuation is retained in "
                  "English; the Vietnamese supplies the closing quote."))
    # G3 (printed p.337).
    b.append(p("Clearly, if no countable faults are possible the apparatus can "
               "be ‘ia’. If the worst combinations of possible non-countable "
               "faults do not cause an incendive arc or spark with the 1.5 "
               "safety factor applied, or produce an ignition-capable hot "
               "surface with no safety factor, the apparatus or circuit can "
               "be considered as ‘ia’. Likewise, if only one countable fault "
               "is possible the apparatus may be considered as ‘ia’, provided "
               "it remains non-incendive with the worst combinations of "
               "non-countable faults applied in both normal operation, and "
               "with the one countable fault applied, and the safety factor "
               "of 1.5 applied for arc or spark ignition."))

    # G4 -> heading 13.3.2 (printed p.337).
    b.append(h4("13.3.2 Intrinsic safety category ‘ib’",
                "13.3.2 Intrinsic safety category ‘ib’"))
    # G5 (printed p.337). Quirk 25.
    b.append(p("This is the lower grade of intrinsic safety and the most "
               "hazardous area into which its circuits are intended to enter "
               "is Zone 1. Its performance in both normal operation and with "
               "any possible single countable fault should be exactly as "
               "specified in (1) and (2) as applied to category ‘ia’ but, "
               "there is no need to address any situation in which two "
               "countable faults occur. In cases where no countable faults "
               "are possible it is treated in the same way as category ‘ia’."))
    b.append(note("<b>Note on ‘ia’ in category ‘ib’.</b> The OCR reads "
                  "'category ‘ia‘.' with a misoriented closing quote; the "
                  "render prints 'category ‘ia’.' The printed form is "
                  "retained."))

    # G6 -> heading 13.4 (printed p.337).
    b.append(h3("13.4 Countable and non-countable faults",
                "13.4 Countable and non-countable faults"))
    # G7+H1 (printed pp.337-338): joined across the page break.
    b.append(p("Faults, be they countable or non-countable, are failures of "
               "components conductors and any other failures which are "
               "possible within the apparatus or system. There are three "
               "situations within apparatus relating to faults, and the "
               "situation in interconnecting cables is governed by cable "
               "design. Details of specifications for components, "
               "connections, cables etc., will be detailed later in this "
               "chapter. Any part of the apparatus or system which does not "
               "comply with the requirements of the protection concept is "
               "assumed to be capable of fault as of normal operation "
               "(non-countable fault), and those which comply are mostly "
               "considered as still capable of fault (countable fault)."))

    # H2 -> heading 13.4.1 (printed p.338).
    b.append(h4("13.4.1 Non-countable faults",
                "13.4.1 Non-countable faults"))
    # H3 (printed p.338).
    b.append(p("A non-countable fault is a failure of any component, assembly "
               "or interconnection within the apparatus which occurs in any "
               "of those which do not comply with the basic requirements of "
               "the protection concept. Where only partial non-compliance is "
               "present, the fault is only related to the effect of that "
               "non-compliance (e.g., where a bare conductor complies with "
               "the requirements but its separation from other bare "
               "conductors does not, then short circuits will be considered "
               "as non-countable faults but open circuit of the conductor "
               "will not)."))

    # H4 -> heading 13.4.2 (printed p.338).
    b.append(h4("13.4.2 Countable faults", "13.4.2 Countable faults"))
    # H5 (printed p.338).
    b.append(p("A failure of any component, assembly or interconnection which "
               "complies with the basic constructional requirements of the "
               "protection concept (which in most cases include rating safety "
               "factors) is called a countable fault."))
    # H6 (printed p.338).
    b.append(p("The Standard also contains enhanced specifications in "
               "addition to its basic specifications and where the component, "
               "assembly or interconnection complies with the basic "
               "requirements of the protection concept and, additionally, "
               "complies with the enhanced requirements, any facet of its "
               "operation which so complies will not be considered as "
               "becoming faulty. (For example, a separation of conductors "
               "which meets the additional requirements of the protection "
               "concept will not be considered as a possible short circuit, "
               "whereas the conductors themselves will be considered as going "
               "open circuit if they only comply with the basic "
               "requirements)."))

    # H7 -> heading 13.4.3 (printed p.338).
    b.append(h4("13.4.3 Effects of other faults",
                "13.4.3 Effects of other faults"))
    # H8 (printed p.338).
    b.append(p("Where a component interconnection or assembly satisfies the "
               "basic requirements of the Standard when no countable faults "
               "are applied elsewhere in the circuit, but ceases to do so "
               "when one (or in the case of ‘ia’ two) countable faults are "
               "applied elsewhere, then that component, interconnection or "
               "assembly ceases to be considered as a countable fault when "
               "that fault (those faults) are applied and is considered to be "
               "a non-countable fault which may be applied if it adversely "
               "affects intrinsic safety."))
    # H9+I1 (printed pp.338-339): joined across the page break.
    # Quirk 56: 'conplies'.
    b.append(p("Where a component, assembly or interconnection conplies with "
               "enhanced specifications of the protection concept in normal "
               "operation, but ceases to do so when appropriate faults are "
               "applied elsewhere in the circuit within the scope of the "
               "Standard, then that component, assembly or connection is "
               "likewise reduced to being considered as a countable or "
               "non-countable fault, depending upon the conditions in which "
               "it operates in those fault conditions."))
    b.append(note("<b>Note on 'conplies'.</b> Section 13.4.3 prints "
                  "'conplies with enhanced specifications' for 'complies'. "
                  "The misspelling is retained in English; the Vietnamese "
                  "follows the intended meaning."))
    # I2 (printed p.339).
    b.append(p("Component, assembly or interconnection faults are only "
               "important insofar as they increase the risk of danger and, "
               "therefore, if they have the reverse effect (e.g., a short "
               "circuit fault on the output of an associated apparatus) they "
               "are not applied."))

    # I3 -> heading 13.4.4 (printed p.339).
    b.append(h4("13.4.4 Infallible component, assembly or interconnection",
                "13.4.4 Infallible component, assembly or interconnection"))
    # I4 (printed p.339). Quirk 57.
    b.append(p("Where any component, assembly or connection satisfies the "
               "additional requirements of the protection concept discussed "
               "in Sections 13.4.3 and 13.4.4, which enable it to be "
               "considered not subject to fault it will be called infallible. "
               "It will only, however, be viewed as infallible in the mode "
               "where the additional requirements are applied (e.g., a "
               "resistor of specific construction may be considered as "
               "infallible as far as failure to a value of resistance lower "
               "than its specified value, but will still be assumed to be "
               "capable of open circuiting). Likewise, it will only be "
               "considered as infallible provided the conditions at its point "
               "of connection into the circuit remain the same. If they "
               "change so that it is subjected to, for example, higher "
               "voltages or currents then it may cease to be infallible in "
               "those circumstances."))
    b.append(note("<b>Note on the self-reference in 13.4.4.</b> The print "
                  "says 'discussed in Sections 13.4.3 and 13.4.4' although "
                  "the section cannot refer to itself; 13.4.2 and 13.4.3 are "
                  "presumably intended. The printed reference is kept."))

    # I5 -> heading 13.5 (printed p.339; two printed lines).
    b.append(h3("13.5 Confirmation of intrinsic safety in respect of arc "
                "and spark ignition",
                "13.5 Confirmation of intrinsic safety in respect of arc "
                "and spark ignition"))
    # I6 (printed p.339).
    b.append(p("Confirmation of intrinsic safety is by ensuring that no arc "
               "or spark is ignition capable, either in normal operation or "
               "after applying the various fault scenarios specified in "
               "Section 13.3 above."))
    # I7 (printed p.339): first half; Fig. 13.2 intervenes at the top of
    # printed p.340. Quirks 26, 28, 58, 59, 60, 61.
    b.append(p("The ignition capability of any part of an intrinsically safe "
               "circuit (i.e., intrinsically safe apparatus interconnecting "
               "cables and that part of associated apparatus within the "
               "intrinsically safe circuit - see Fig. 13.1) needs to be shown "
               "to be incapable of causing an ignition by any arc or spark "
               "occurring where such an arc or spark is considered possible, "
               "which is normally in such places as between conductors, in "
               "series with a conductor, at terminals, etc., unless the "
               "construction of the apparatus gives confidence that such "
               "sparking cannot occur (where construction endows "
               "infallibility). The parts which form the electrodes between "
               "which sparking occurs will vary widely and, as the "
               "incendivity of a low energy spark depends to a considerable "
               "extent on the geometry of these electrodes a basic yardstick "
               "is necessary to ensure repeatability. For this reason a "
               "special spark test apparatus has been developed to simulate "
               "sparking which may occur and this is shown in Fig. 13.2 and "
               "13.3. This spark test apparatus (called the breaklash in the "
               "UK) is more sensitive than any typically expected practical "
               "electrode configuration, using as it does very small tungsten "
               "wire contacts which are more springy than copper as one "
               "electrode, thereby giving confidence that if no ignition "
               "occurs in a test in which it is employed then no ignition "
               "will occur"))

    # J (printed p.340): Fig. 13.2 at the printed position.
    b.append(fig(2, FA.fig_f1302()))
    # Quirks 27, 74.
    b.append(note("<b>Note on the legend of Fig. 13.2.</b> The callout numbers "
                  "beside the drawing are not in ascending order; the caption "
                  "supplies the authoritative 1–18 key (including '16 Gear "
                  "wheel drive 50 : 12', '17 Insulated coupling' and '18 Drive "
                  "motor with reduction gears 80 rev/min'). The OCR reads "
                  "'Contact wlre' and 'Clamp,'; the render gives 'Contact "
                  "wire' and 'Clamp'. The caption has no final full stop."))

    # J1 (printed p.340): continuation of I7.
    b.append(p("in any practical situation. The use of cadmium for the lower "
               "disc of the device is to cover the situation where cadmium, "
               "zinc, magnesium or, to a lesser degree, titanium is included "
               "in the materials within the apparatus to be tested and which "
               "may form the actual sparking electrodes. This is because it "
               "is known that these materials enhance the incendivity of "
               "electrical sparks (probably by the release of free radicals) "
               "and render ignition much easier. An energy of approximately "
               "40 μJ released efficiently in a spark will ignite an ideal "
               "mixture of hydrogen/air in the presence of cadmium, whereas "
               "approximately 130 μJ is necessary where neither cadmium or "
               "the other metals are present. Cadmium is used because it is "
               "the most sensitive of the metals in question. In addition, "
               "cadmium and zinc plating is so common in the engineering "
               "industry that it is considered highly likely that, even if "
               "these materials were excluded during manufacture, servicing "
               "would introduce them in service by replacement of screws, "
               "etc., and a control system to prevent this is not considered "
               "as practicable."))
    b.append(note("<b>Note on the spark-test paragraph.</b> The print reads "
                  "'intrinsically safe apparatus interconnecting cables' with "
                  "no comma or 'and', 'Fig. 13.2 and 13.3' without repeating "
                  "'Fig.', calls the apparatus 'the breaklash in the UK', and "
                  "says 'neither cadmium or the other metals are present' "
                  "where 'nor' would be expected. The OCR also reads '40 pJ' "
                  "and '130pJ' for '40 μJ' and '130 μJ'. All printed forms are "
                  "retained."))

    # K1 (printed p.341): first half; Fig. 13.3 and Table 13.1 intervene.
    b.append(p("The mode of operation is to fill the enclosure of the "
               "apparatus with the test gas appropriate to the sub-group for "
               "which the apparatus is intended (the appropriate test gases "
               "are given in Table 13.1). The apparatus is then standardized "
               "by switching it on so that sparks are produced by the "
               "contra-rotation of the two discs which contra-rotate at 80 "
               "rpm for the disc holding"))

    # K (printed p.341): Fig. 13.3 at the printed position.
    b.append(fig(3, FA.fig_f1303()))
    # Quirks 29, 30, 62, 63.
    b.append(note("<b>Note on the labels of Fig. 13.3.</b> The label 'Upper "
                  "disc dimension 38 mm' is printed twice, once for each "
                  "disc, although only the upper disc has that dimension; "
                  "both are kept and flagged. The OCR loses '0.2 mm minimum "
                  "tungsten wire length 11 mm' and omits 'Separation of discs "
                  "10 mm', both 'Upper disc dimension 38 mm' labels and "
                  "'Cadmium disc diameter 38 mm'; the render supplies them. "
                  "The spacing '80 rpm' (printed p.341) and '19.2rpm' "
                  "(printed p.342) is inconsistent as printed."))

    # L (printed p.342): Table 13.1 at the printed position.
    b.append(table(T1.HEAD131_EN, T1.ROWS131_EN, T1.CAPTION131_EN))
    b.append(note(T1.NOTE131_EN))
    b.append(note("<b>Note on Table 13.1 and number/unit spacing.</b> The "
                  "title prints an en dash before 'with electrical safety "
                  "factors' and the sub-heads print lowercase 'current' and "
                  "'energy'; the OCR reads '±' as 'f', '(% V/V)' as '(Yo W)' "
                  "and the source line as '(from BSEN 50020)'. The prose "
                  "prints '24V dc' without a space but '95 mH' with one; both "
                  "are preserved."))

    # L1 (printed p.342): continuation of K1.
    b.append(p("the wires, and 19.2rpm for the cadmium disc. The discs are "
               "then fed with the standardizing electrical supply current "
               "shown in Table 13.1, derived by placing a resistor in series "
               "with a 24V dc power supply or battery so that the current is "
               "the short circuit current on the outboard end of the "
               "resistor. This current is fed to the test apparatus through "
               "a 95 mH air-cored series inductor and an ignition must occur "
               "within five minutes (400 revolutions of the upper disc) to "
               "confirm that the apparatus has reached its minimum "
               "sensitivity. It should be noted here that no maximum "
               "sensitivity calibration is carried out and the sensitivity of "
               "each test can vary. Although it is possible for significant "
               "variation in sensitivity to occur (up to 40 per cent is often "
               "quoted as possible, although this cannot be confirmed), the "
               "minimum sensitivity gives sufficient (although not total) "
               "confidence that ignitions will not occur in practical "
               "circumstances. The sensitivity variation is therefore an "
               "inconvenience rather than a safety problem."))
    # L2 (printed p.342).
    b.append(p("After calibration the apparatus is refilled with the same "
               "gas/air mixture and its two discs connected, each to one of "
               "the points between which sparking is considered as possible, "
               "after applying the fault requirements for the protection "
               "concept and the necessary safety factors described in "
               "Sections 13.3.1 and 13.3.2. The apparatus is then energized "
               "and allowed to operate for 5 minutes (400 revolutions of the "
               "upper disc) for a dc circuit or 12.5 minutes (1000 "
               "revolutions of the upper disc) for ac circuits. If no "
               "ignition occurs and the gas/air mixture within the enclosure "
               "is then caused to explode by once again applying the "
               "calibration supply to the discs for 5 minutes, the test is "
               "considered as successful."))
    # L3 (printed p.342).
    b.append(p("The reason for using 1000 revolutions in the case of an ac "
               "circuit is because it is not always possible to arrange the "
               "spark at the peak of a cycle and thus, to maximize the "
               "possibility of so doing, the length of the test is increased."))
    # L4+M1 (printed pp.342-343): joined across the page break.
    b.append(p("In the case of a dc circuit, the test is normally stopped at "
               "2.5 minutes and the polarity of connection reversed to ensure "
               "that any polarity effects in the circuit being tested are "
               "taken into account. With capacitive circuits and, to a lesser "
               "extent, inductive and resistive circuits, it is necessary to "
               "ensure that the circuit can return to its open circuit "
               "condition between sparks and this may not be possible when "
               "using a standard test apparatus. This problem is overcome by "
               "removal of wires from the upper disc to allow more recharging "
               "time. When this is done the number of rotations for both "
               "standardization and test must be increased (e.g., if the two "
               "opposite wires are removed leaving two wires, the time for "
               "testing and calibration needs to be doubled)."))

    # M2 -> heading 13.5.1 (printed p.343).
    b.append(h4("13.5.1 Achievement of safety factors",
                "13.5.1 Achievement of safety factors"))
    b.append(note("<b>Note on 13.5.1 and its cross-references.</b> The heading "
                  "is numbered '13.5.1' in the render (the OCR reads '13.5. "
                  "I'). The prose prints 'for testing purposed by a specially "
                  "constructed circuit' (source typo 'purposed') and cites "
                  "'Table 13.6 on page 362'; no Table 13.6 appears on that "
                  "page, which carries Table 13.1. All printed forms are "
                  "retained."))
    # M3 (printed p.343).
    b.append(p("The safety factors of 1.5 where specified as necessary (see "
               "Section 13.4) are normally achieved by modification of the "
               "apparatus being tested to give the required factor. If this "
               "is not convenient or possible the circuit may be simulated "
               "for testing purposed by a specially constructed circuit, "
               "although great care is necessary in such circumstances to "
               "ensure that the simulated circuit is indeed identical to the "
               "actual circuit. For this reason it is always preferable to "
               "operate on the actual circuit. These safety factors are "
               "always in addition to any adjustments made to allow for such "
               "things as mains variations. All testing has to be carried out "
               "in (at least) the following conditions. First, the mains "
               "supplies to the apparatus must be increased to 110 per cent "
               "of their nominal value (it is assumed that mains tolerance "
               "will not exceed this). Second, any other power supplies and "
               "voltage-limiting circuits, and devices such as zener diodes, "
               "must be increased to give the maximum voltage which will "
               "occur at the worst combination of component tolerances with "
               "any mains supply to them at 110 per cent of its nominal "
               "value. Third, batteries shall be arranged or simulated to "
               "give the voltages specified in Table 13.6 on page 362."))
    # M4 (printed p.343).
    b.append(p("The above actions need to be taken in all cases but, in "
               "addition, where the safety factor of 1.5 is required, the "
               "following actions must also be carried out before the test "
               "is commenced. First, for resistive circuits the current which "
               "would flow into a short circuit should be increased to 1.5 "
               "times its normal maximum value by the reduction of such "
               "things as current-limiting resistors, or if this is not "
               "possible by increasing the voltage in the circuit although "
               "this gives a more onerous test. This needs to be done even "
               "with power supplies which have crowbar protection, although "
               "in this case it must be arranged so that the supply recovers "
               "between short circuits created by the test which may require "
               "both wire removal from the test apparatus and alteration of "
               "the crowbar circuit."))
    # M5 (printed p.343).
    b.append(p("Second, for inductive circuits the current through the "
               "inductance needs to be increased to 1.5 times its value "
               "achieved when all supplies are at the maximum of their "
               "maximum values, as already specified by the methods defined "
               "for resistive circuits, although care needs to be taken to "
               "ensure that the resistive circuit does not itself become "
               "incendive by this means and give a misleading test result. "
               "Third, for capacitive circuits the voltage across capacity "
               "of the circuit needs to be increased to 1.5 times the maximum "
               "which it achieves in the worst condition taking account of "
               "tolerances etc., and, it needs to be ensured that the circuit "
               "does not become resistively ignition capable and give a "
               "misleading result."))
    # M6+N1 (printed pp.343-344): joined across the page break.
    b.append(p("The above methods of determination of test conditions are "
               "applicable to simple inductive, capacitive or resistive "
               "circuits. In most practical cases, circuits will contain at "
               "least two of the parameters (e.g., resistive power and "
               "capacitive energy, resistive power and inductive energy, or "
               "both inductive and capacitive energy). In cases where this "
               "occurs or the circuit contains all three it is often "
               "necessary to test with the safety factor developed by "
               "increase of current, and repeat the test with it produced by "
               "increase in voltage to cover all possibilities."))
    # N2 (printed p.344). Quirk 68.
    b.append(p("Where increases in current or voltage are not considered to "
               "be convenient as an acceptable alternative, the test gases "
               "may be altered to give the required safety factor. The "
               "factored gas mixtures for the various sub-groups are given in "
               "Table 13.2 along with the reduced calibration currents for "
               "these gas mixtures. The test currents are derived by placing "
               "a limiting resistor in series with a 24V dc supply so that "
               "the current is actually the short circuit current and the "
               "feeding this current to the test apparatus via a series 95 "
               "mH air-cored inductance."))
    b.append(note("<b>Note on the stray 'the'.</b> The print reads 'so that "
                  "the current is actually the short circuit current and the "
                  "feeding this current to the test apparatus via a series "
                  "95 mH air-cored inductance'. The word 'the' before "
                  "'feeding' is retained in English; the Vietnamese follows "
                  "the intended meaning."))

    # N3 (printed p.344): Table 13.2 at its printed position.
    b.append(table(T1.HEAD132_EN, T1.ROWS132_EN, T1.CAPTION132_EN))
    b.append(note(T1.NOTE132_EN))
    b.append(note("<b>Note on the Table 13.2 notes.</b> The italic source line "
                  "prints '(gas mixtures from BS/EN 50020)' in lowercase and "
                  "the Note below reads 'Note: These mixtures provide safety "
                  "factors equivalent to a 1.5 safety factor on current or "
                  "voltage.' The OCR reads '±' as 'i' or 'f' and '(% V/V)' as "
                  "'(Yo W)'; the render governs. The repeated sub-group labels "
                  "and 'None' cells are as printed."))

    # N4 -> heading 13.5.2 (printed p.344).
    b.append(h4("13.5.2 Assessment of circuits",
                "13.5.2 Assessment of circuits"))
    # N5 (printed p.344). Quirk 37.
    b.append(p("In order to assist in design of circuits and to simplify the "
               "process of confirming intrinsic safety, a set of curves has "
               "been produced to identify the minimum sensitivity of the test "
               "apparatus and which may be used in cases where the circuits "
               "are simple and can be defined with confidence. The curves "
               "used are intended for circuits that are simple, in that the "
               "capacitive curves are concerned with capacitive sparks only, "
               "the inductive circuits with inductive sparks only, and the "
               "resistive circuits with resistive sparks only. Practical "
               "circuits, however, seldom achieve this degree of purity and "
               "so there are limits on the use of the curves. The situation "
               "is helped, by the nature of the sparking which is different "
               "for the different sources (e.g., inductive, capacitive or "
               "resistive)."))
    b.append(note("<b>Note on 'idenhfy'.</b> The OCR reads 'idenhfy' where the "
                  "render prints 'identify'; the render reading is used."))

    # O1 -> unnumbered heading 'Inductive circuits' (printed p.345).
    b.append(h4("Inductive circuits", "Inductive circuits"))
    # O2 (printed p.345). Quirk 70.
    b.append(p("The inductive sparking mechanism is usually a break spark "
               "produced when the contacts break and a high, back emf is "
               "generated by collapse of the magnetic field (see Fig. 13.4). "
               "As the spark is not created by a short circuit (as there is "
               "little or no inductive stored energy when that occurs) but "
               "by the breaking of an inductive circuit when the back EMF "
               "seeks to perpetuate the current flow, it rises to high "
               "levels, sustaining a spark or arc, until all of the energy is "
               "dissipated. Inductive sparks are the most efficient in "
               "releasing energy into sparks and, in the test apparatus, the "
               "following energies are sufficient to ignite the test gases "
               "for the three sub-groups."))
    b.append(note("<b>Note on 'back emf' and 'back EMF'.</b> The first sentence "
                  "prints 'back emf' in lowercase and a later sentence in the "
                  "same paragraph prints 'back EMF' in capitals. Both are kept "
                  "as printed."))

    # O3 (printed p.345): Fig. 13.4 at the printed position.
    b.append(fig(4, FA.fig_f1304()))
    # Quirk 71, 74.
    b.append(note("<b>Note on the labels of Fig. 13.4.</b> The diagram labels "
                  "'Arc/spark gap' with a slash and gives 'L = inductance' "
                  "and 'r = internal resistance' in lowercase italic symbols; "
                  "the small terminal glyphs are unreadable marks, not text. "
                  "The caption has no final full stop. The printed labels are "
                  "retained."))

    # P1 (printed p.346): displayed energy list. Quirks 39, 72.
    b.append(eq("IIA = 320 μJ<br>IIB = 120 μJ<br>IIC = 40 μJ"))
    b.append(note("<b>Note on the conflicting IIB energies.</b> The displayed "
                  "list on printed p.346 gives 'IIB = 120 μJ' while the curve "
                  "labels in Fig. 13.5 give 'IIB (160 μJ)'. Both printed values "
                  "are preserved; IIA (320 μJ) and IIC (40 μJ) agree."))
    # P2 (printed p.346).
    b.append(p("Figure 13.5 shows the minimum inductance levels for ignition "
               "at 24 V and various currents from the type of source shown in "
               "Fig. 13.4, and Fig. 13.6 shows the same information for lower "
               "voltages. (At voltages above 24 V the information in Fig. "
               "13.5 is appropriate). These values are worst case as they "
               "refer to air-cored inductors and, as most inductors have "
               "magnetic cores of iron or other solid magnetic materials "
               "which are less efficient from a discharge point of view, "
               "they can be used with confidence in general."))

    # P3 (printed p.346): Fig. 13.5 at the printed position.
    b.append(fig(5, FA.fig_f1305()))
    # Quirks 40, 41, 42, 73, 74.
    b.append(note("<b>Note on Fig. 13.5.</b> The OCR reads '1 .o' for the "
                  "'1.0' y-axis tick and omits the printed '0.01' tick. The "
                  "caption prints 'threshold/inductive' with no spaces around "
                  "the slash, 'with V = 24 V' with a space, and no final full "
                  "stop after the Note. The curve label 'IIB (160 μJ)' "
                  "conflicts with the displayed 'IIB = 120 μJ'. Captions of "
                  "Figs 13.1–13.5 are bold and none ends with a full stop "
                  "after the final item; all are retained verbatim."))
    return "".join(b)
