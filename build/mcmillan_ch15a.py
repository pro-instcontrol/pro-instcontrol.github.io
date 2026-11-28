# -*- coding: utf-8 -*-
"""Chapter 15, prose module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 456-461 (PDF pp. 477-482).

Covers the two printed standard subtitles and the opening paragraphs, 15.1
Situation in respect of standardization (with the unnumbered Zone 20, Zone 21
and Zone 22 subheadings), 15.2 Basic types of apparatus for use with
combustible dusts, 15.2.1 Degrees of enclosure (with 'Apparatus with dust
tight enclosures' and 'Dust-protected enclosures'), 15.3 Operational
requirements, 15.4 Basic constructional requirements and 15.4.1 Enclosure
materials and mechanical strength (with the 'Enclosure materials'
subheading). Table 15.1 sits at its printed place on p.460, interrupting the
temperature-classification sentence. The chapter shell owns the chapter h2,
the ten printed references, the glossary, the source note and the copyright.

Full faithful EN/VI translation of survey A blocks A0-F5. Printed quirks are
kept verbatim in the English text (the assumed 5 mm layer, (RoSPA/IC13),
IP6X to BS/EN 60529, BS 4999 Part 10 with run-together superscripts, 10 g/m3,
+/-10 per cent, the unmatched braces of [280 x 2/3] - 10, the 85 C versus
225 - 75 - 10 contradiction, the non-numeric table row order, the doubled
parentheses of 'N(n)', and the predominance footnote), each flagged with a
bilingual note; the Vietnamese follows the intended meaning. The final
sentence on printed p.461 is the last complete one written here; its
continuation on printed p.462 belongs to the next module. This is an
unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, ul, ol
import mcmillan_tbl15_1_2 as T


def body_vi():
    b = []

    # A0-A2 (printed p.456). The shell owns the chapter h2; the module owns
    # the two printed standard subtitle lines and the opening paragraphs.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("<b>(BS 6467, Part 1 (1985))<br>(BS 7535 (1992))</b>"))
    b.append(p("Cách tiếp cận bảo vệ thiết bị dùng trong môi trường có bụi "
               "dễ cháy luôn khác khá nhiều so với cách tiếp cận dành cho "
               "khí và hơi. Việc các đám mây bụi nhìn thấy rõ, tạo ra mức độ "
               "che khuất cao, đã dẫn đến tình huống là quá trình chế biến "
               "bụi cần có mức kiểm soát cao đối với các đám mây bụi để công "
               "việc có thể tiến hành. Ngoài ra, việc ngăn không cho các hạt "
               "vật chất như bụi xâm nhập vào bên trong thiết bị điện tương "
               "đối dễ dàng thông qua việc quy định cấp bảo vệ của vỏ bọc, "
               "khác với trường hợp khí và hơi vốn khó đạt được và duy trì "
               "điều đó."))
    b.append(p("Ngược lại, bụi lắng xuống, khác với khí và hơi, và một sự rò "
               "rỉ dẫn đến đám mây bụi sẽ để lại một lớp bụi quanh điểm rò rỉ "
               "thay vì phân tán đi. Điều này đòi hỏi tiêu chuẩn vệ sinh công "
               "nghiệp cao và phải xem xét ảnh hưởng của các lớp bụi (danh "
               "nghĩa giả định có độ dày tối đa 5 mm) đến nhiệt độ bề mặt của "
               "vỏ bọc. Điều này đã ảnh hưởng đến cách tiếp cận sử dụng thiết "
               "bị điện trong môi trường có nguy cơ bụi và dẫn đến tình huống "
               "là cấu tạo thiết bị dựa trên khả năng loại trừ bụi, và một "
               "hình thức kiểm soát chứng nhận ít nghiêm ngặt hơn đã được áp "
               "dụng. Ảnh hưởng của các lớp bụi làm tăng nhiệt độ vỏ bọc được "
               "xử lý trong khâu lựa chọn thiết bị, chứ không phải trong khâu "
               "chế tạo."))
    b.append(note("<b>Ghi chú về lớp bụi 5 mm.</b> Bản in giả định danh nghĩa "
                  "lớp bụi có độ dày tối đa 5 mm; hình thức này được giữ "
                  "nguyên trong bản tiếng Anh."))

    # A3-A4+A5-B1-C2 (printed pp.456-458), heading 15.1 and zone headings.
    b.append(h3("15.1 Tình hình liên quan đến việc chuẩn hóa",
                "15.1 Situation in respect of standardization"))
    b.append(p("Mặc dù việc lắp đặt thiết bị trong các khu vực có nguy cơ bụi "
               "đã được thực hiện từ rất nhiều năm, thiết bị nói chung được "
               "lựa chọn từ các dòng thiết bị công nghiệp dựa trên khả năng "
               "loại trừ bụi của chúng và không có Tiêu chuẩn chính thức hay "
               "quy trình Chứng nhận/Phê duyệt nào tồn tại. Tình hình này thay "
               "đổi vào năm 1985 với việc công bố BS 6467, Phần 1¹, lần đầu "
               "tiên quy định khá chi tiết các yêu cầu cấu tạo đối với thiết "
               "bị dùng cho loại bầu khí quyển nổ này."))
    b.append(p("BS 6467, Phần 1 (1985)¹ quy định hai loại thiết bị: thiết bị "
               "kín bụi và thiết bị được bảo vệ chống bụi. Điều này phản ánh "
               "cách tiếp cận thời đó, chia các khu vực nguy hiểm có bụi "
               "thành hai khu vực, Vùng Z và Vùng Y, khu vực trước có định "
               "nghĩa tương tự Vùng 1 trong trường hợp khí và hơi, còn khu vực "
               "sau tương tự Vùng 2 — cách tiếp cận này sau đó được xác nhận "
               "trong BS 6467, Phần 2¹ năm 1988. Cách tiếp cận này loại trừ "
               "mọi xem xét đối với các khu vực như bên trong bình chứa bụi, "
               "vốn sẽ là Vùng 0 trong trường hợp khí hoặc hơi, và các Vùng "
               "này được coi là những nơi không nên lắp thiết bị điện, hoặc "
               "chỉ lắp trong điều kiện đặc biệt và trong những trường hợp đó "
               "thì được xử lý riêng. Điều này không gây quá nhiều khó khăn vì "
               "các lắp đặt trong những Vùng này mà bụi là vấn đề có xu hướng "
               "hiếm, và thường là các thiết bị như cặp nhiệt điện, nhiệt kế "
               "điện trở và các thiết bị tương tự, chỉ cần đưa một ống thép "
               "không gỉ hoặc ống tương tự được bịt kín vào khu vực đó. Chính "
               "trên cơ sở này mà các yêu cầu trong BS 6467, Phần 1 (1985) "
               "đối với ‘Thiết bị có bảo vệ bằng vỏ bọc để sử dụng trong môi "
               "trường có bụi dễ cháy’ được xây dựng. (Việc dùng thuật ngữ "
               "‘Bụi dễ cháy’ thay vì ‘bụi cháy được’ nhằm nhấn mạnh rằng bụi "
               "có hành vi khác với khí và hơi)."))
    b.append(p("BS 6467, Phần 1¹ thực chất xem xét thiết bị được bảo vệ chống "
               "sự xâm nhập của bụi, trong đó bụi có thể vào nhưng không đủ số "
               "lượng để cản trở hoạt động của thiết bị, và thiết bị kín bụi, "
               "trong đó bụi bị loại trừ hoàn toàn. Lý do có hai mức độ khác "
               "nhau là để liên hệ với Vùng Z, nơi cần thiết bị kín bụi, và "
               "Vùng Y, nơi chỉ cần thiết bị được bảo vệ chống bụi, trừ khi "
               "bụi dẫn điện (khi đó không phân biệt vì nguy cơ chập mạch bên "
               "trong do bụi tăng thêm)."))
    b.append(p("Ngoài BS 6467, Phần 1¹, còn có một Tiêu chuẩn khác, BS 7535 "
               "(1992)², đưa ra hướng dẫn về lựa chọn thiết bị theo dãy Tiêu "
               "chuẩn BS/EN 500 (Thiết bị điện cho bầu khí quyển có khả năng "
               "nổ dạng khí/không khí, hơi/không khí hoặc sương/không khí, xem "
               "các Chương 7 đến 14) để sử dụng trong môi trường có bụi dễ "
               "cháy. Do tuổi đời của Tiêu chuẩn này, thực tế nó viện dẫn các "
               "Tiêu chuẩn Châu Âu ở phiên bản đầu tiên (dãy BS 5501), nhưng "
               "các tiêu chí của nó cũng liên quan như nhau đến các phiên bản "
               "thứ hai (dãy BS/EN 500). Lại cũng do tuổi đời của nó, Tiêu "
               "chuẩn này vẫn viện dẫn Vùng Z và Y."))
    b.append(p("Như đã giải thích trước đó trong Chương 6, tình hình liên quan "
               "đến phân loại khu vực đối với bụi sắp thay đổi trong thời "
               "gian rất ngắn sang một hệ thống ba Vùng tương tự như hệ "
               "thống dành cho khí. Điều này dựa trên một dự thảo tài liệu của "
               "IEC (IEC 1241-3), đã được phê duyệt với tư cách là một Tiêu "
               "chuẩn Anh mới tiềm năng và xác định các vùng sau."))
    b.append(h4("Vùng 20", "Zone 20"))
    b.append(p("Vùng 20 được định nghĩa là nơi các đám mây bụi hiện diện "
               "thường xuyên, chẳng hạn như bên trong bình chứa, và có định "
               "nghĩa tương tự Vùng 0 đối với khí và hơi."))
    b.append(h4("Vùng 21", "Zone 21"))
    b.append(p("Vùng 21 được định nghĩa là nơi các đám mây bụi được tạo ra "
               "thường xuyên, chẳng hạn như các cửa nạp liệu, và có định nghĩa "
               "tương tự Vùng 1 đối với khí và hơi."))
    b.append(h4("Vùng 22", "Zone 22"))
    b.append(p("Vùng 22 được định nghĩa là nơi các đám mây bụi hiếm khi xuất "
               "hiện, thường được tạo ra do sự xáo trộn các lớp bụi đã hình "
               "thành dù đã yêu cầu mức độ vệ sinh công nghiệp cao trong các "
               "khu vực này, và có định nghĩa tương tự Vùng 2 đối với khí và "
               "hơi."))
    b.append(p("Các yêu cầu cấu tạo cụ thể cho thiết bị dùng trong môi trường "
               "có nguy cơ bụi liên quan đến các Vùng này hiện vẫn chưa tồn "
               "tại, vì việc xây dựng các Tiêu chuẩn liên quan vẫn chưa hoàn "
               "tất. Tuy nhiên, về vấn đề này có một số hướng dẫn. Thứ nhất, "
               "Vùng 21 có thể liên hệ với Vùng Z, do đó thiết bị dùng cho "
               "Vùng Z, như đã mô tả trước đó, cũng có thể được coi là phù hợp "
               "cho Vùng 21, và thiết bị dùng cho Vùng Y cho Vùng 22. Còn lại "
               "Vùng 20, nơi mà trong lịch sử chưa từng có cách tiếp cận nào "
               "ở cấp quốc gia hay quốc tế. Tuy nhiên, vấn đề này không phải "
               "là mới và vào năm 1973, một Bộ quy tắc riêng của một công ty "
               "(RoSPA/IC13), nhận ra khả năng cuối cùng sẽ cần đến thiết bị "
               "đo lường tinh vi trong cái sau này sẽ là Vùng 20, đã dùng hệ "
               "thống phân loại ba Vùng cho bụi. Điều này dẫn đến một số hướng "
               "dẫn về thiết bị an toàn nội tại trong Vùng 20 xuất hiện cả "
               "trong bộ quy tắc đó lẫn trong các tài liệu khác dựa trên việc "
               "sử dụng thiết bị an toàn nội tại ‘ia’ đặt bên trong vỏ bọc "
               "IP6X theo BS/EN 60529⁴ (cũng như trường hợp rủi ro khí và hơi, "
               "thiết bị an toàn nội tại là loại thiết bị duy nhất có khả "
               "năng được chấp nhận trong những vùng có nguy cơ cao như vậy "
               "vì sự hiện diện liên tục hoặc gần như liên tục của bầu khí "
               "quyển nổ)."))
    b.append(note("<b>Ghi chú về (RoSPA/IC13) và IP6X.</b> Bản in viết "
                  "‘(RoSPA/IC13)’ và ‘an IP6X enclosure to BS/EN 60529⁴’; cả "
                  "hai được giữ nguyên trong bản tiếng Anh, còn bản tiếng "
                  "Việt nêu theo nghĩa định."))

    # C3-C6 (printed p.458), heading 15.2 with its italic subtitle.
    b.append(h3("15.2 Các loại thiết bị cơ bản để sử dụng với bụi dễ cháy",
                "15.2 Basic types of apparatus for use with combustible dusts"))
    b.append(p("<i>(apparatus in accordance with BS 6467, Part 1)</i>"))
    b.append(p("Phương pháp làm cho thiết bị này phù hợp để sử dụng trong bầu "
               "khí quyển nổ gồm bụi và không khí là loại trừ bụi ra khỏi bên "
               "trong vỏ bọc. Loại thiết bị này được thử nghiệm để bảo đảm "
               "rằng nó làm được điều đó."))
    b.append(note("<b>Ghi chú về dấu phẩy thừa.</b> Bản in viết ‘This type of "
                  "apparatus is, tested to ensure that it does so.’ với dấu "
                  "phẩy thừa sau ‘is’; hình thức này được giữ nguyên trong "
                  "bản tiếng Anh, còn bản tiếng Việt nêu theo nghĩa định."))
    b.append(p("Cần nhận ra khả năng áp suất giảm trong mọi vỏ bọc do thay đổi "
               "nhiệt độ, dù là nhiệt độ môi trường hay nhiệt độ vận hành, và "
               "vì vậy mọi vỏ bọc kín bụi đều được thử nghiệm trên cơ sở áp "
               "suất bên trong giảm như đã quy định trong Tiêu chuẩn thích "
               "hợp."))
    b.append(p("Mặc dù việc thử nghiệm sự xâm nhập của bụi là tất cả những gì "
               "cần thiết để đáp ứng các yêu cầu cơ bản của loại thiết bị "
               "này, cần nhận ra rằng thử nghiệm sự xâm nhập của chất lỏng "
               "cũng cần thiết cho mọi thiết bị dùng ngoài trời."))

    # C7-C9+D1-D2 (printed pp.458-459), heading 15.2.1 and its subheadings.
    b.append(h4("15.2.1 Mức độ vỏ bọc", "15.2.1 Degrees of enclosure"))
    b.append(p("Có hai loại thiết bị được phân biệt bởi mức độ vỏ bọc của "
               "chúng. Đó là những loại sau."))
    b.append(h4("Thiết bị có vỏ bọc kín bụi",
                "Apparatus with dust tight enclosures"))
    b.append(p("Đây là thiết bị có vỏ bọc được chế tạo sao cho loại trừ hoàn "
               "toàn sự xâm nhập của các hạt bụi có thể nhìn thấy. Điều này "
               "có nghĩa là thiết bị kín bụi, vì không có bụi nhìn thấy nào "
               "xâm nhập trong các thử nghiệm về tính phù hợp của vỏ bọc, vốn "
               "bao gồm việc cho vỏ bọc vận hành trong môi trường thử bụi ở "
               "áp suất giảm để tạo mọi cơ hội cho bụi xâm nhập. Những vỏ bọc "
               "như vậy phải được thử nghiệm theo Cấp bảo vệ IP6X phù hợp "
               "với BS/EN 60529⁴ (đối với các vỏ bọc cũ hơn được sản xuất "
               "trước khi đưa vào BS/EN 60529 thì Tiêu chuẩn đã dùng là BS "
               "5490⁵, và đối với thiết bị đóng cắt, hiện được đưa vào BS/EN "
               "60529 và do đó không có Tiêu chuẩn riêng biệt nào, BS 5420⁶ "
               "từng là Tiêu chuẩn phù hợp về mặt lịch sử). Đáng chú ý là ngay "
               "cả máy quay cũng phải đáp ứng yêu cầu này thay vì các yêu cầu "
               "của EN 60034, Phần 5⁷ (được sản xuất tại Anh với tên BS 4999, "
               "Phần 10⁵⁸), vốn cho phép các sai khác riêng liên quan đến vỏ "
               "bọc của máy quay và trong những trường hợp khác thường được "
               "coi là đủ. Đối với thiết bị dùng ngoài trời, cần có một gói "
               "toàn vẹn vỏ bọc hoàn chỉnh IP65, và mức vỏ bọc này được coi là "
               "cần thiết cho mọi thiết bị dùng trong Vùng Z và, trong trường "
               "hợp bụi dẫn điện, cho thiết bị dùng trong Vùng Y."))
    b.append(note("<b>Ghi chú về các Tiêu chuẩn và câu IP65.</b> Bản in viết "
                  "‘BS 4999, Part 10⁵⁸’ với hai chỉ số trên 5 và 8 chạy liền "
                  "nhau, và câu ‘For apparatus for outdoor use is a total "
                  "enclosure integrity package of IP65 is required’ với cấu "
                  "trúc lặp; cả hai được giữ nguyên trong bản tiếng Anh, còn "
                  "bản tiếng Việt nêu theo nghĩa định."))
    b.append(h4("Vỏ bọc được bảo vệ chống bụi",
                "Dust-protected enclosures"))
    b.append(p("Đây là mức độ toàn vẹn vỏ bọc thấp hơn, và yêu cầu ở đây là "
               "vỏ bọc ít nhất phải đạt IP5X theo BS/EN 60529⁴ hoặc các Tiêu "
               "chuẩn tương đương cũ hơn đã nêu ở trên. Ngoài ra, do mục "
               "đích sử dụng khác nhau, loại thiết bị này chỉ được giới hạn "
               "cho Vùng Y và chỉ được chấp nhận khi đó đối với bụi không "
               "dẫn điện). Ngoài ra, các vỏ bọc đạt IP5X theo EN 60034, Phần "
               "5⁷ (BS 4999, Phần 10⁵⁸) được chấp nhận trong những trường hợp "
               "này dù chúng cung cấp mức bảo vệ thấp hơn một chút do yêu cầu "
               "đối với máy quay thông thường. Tuy nhiên, trong trường hợp "
               "này có một quy định bổ sung ngoài các quy định trong các "
               "Tiêu chuẩn IP đã nêu ở trên, đó là lượng bụi xâm nhập vào vỏ "
               "bọc trong thử nghiệm không được vượt quá tương đương 10 g/m³, "
               "được suy ra từ khối lượng bụi xâm nhập chia cho thể tích tự "
               "do (sau khi trừ thể tích của các linh kiện và cụm lắp ráp bên "
               "trong vỏ bọc khỏi tổng thể tích bên trong của vỏ bọc) của vỏ "
               "bọc. Đây là một cách xác định các tiêu chí đậu thử nghiệm và "
               "giảm sự phụ thuộc vào ý kiến của chuyên gia thực hiện thử "
               "nghiệm, và một lần nữa cần nhớ rằng mức bụi nêu trên chỉ áp "
               "dụng cho bụi không dẫn điện. Điều này có nghĩa là vỏ bọc IP54 "
               "để sử dụng ngoài trời."))
    b.append(note("<b>Ghi chú về 10 g/m³ và dấu ngoặc.</b> Bản in viết "
                  "‘10 g/m³’ và câu kết thúc bằng ‘only then acceptable for "
                  "non-conducting dusts).’ với dấu ngoặc đóng thừa; cả hai "
                  "được giữ nguyên trong bản tiếng Anh, còn bản tiếng Việt "
                  "nêu theo nghĩa định."))

    # D3-E5 (printed pp.459-460), heading 15.3; Table 15.1 interrupts E5.
    b.append(h3("15.3 Yêu cầu vận hành", "15.3 Operational requirements"))
    b.append(p("Thiết bị có thể phát sinh tia lửa hoặc không bên trong vỏ bọc, "
               "vì chính vỏ bọc là biện pháp bảo vệ. Do đó không có yêu cầu "
               "giới hạn năng lượng của tia lửa hoặc hồ quang, mà chỉ cần "
               "giới hạn nhiệt độ bề mặt bên ngoài tối đa của vỏ bọc. Nhiệt độ "
               "vỏ bọc cần được xác định trong các điều kiện sau: thứ nhất, "
               "với vỏ bọc được lắp ở vị trí lắp đặt bình thường bất lợi nhất "
               "(vị trí cho nhiệt độ cao nhất tại bất kỳ điểm nào trên bề mặt "
               "vỏ bọc); thứ hai, điện áp nguồn cấp phải được điều chỉnh đến "
               "bất kỳ giá trị nào trong dung sai vận hành để cho nhiệt độ "
               "cao nhất tại vị trí nêu trên (khi không có dung sai điện áp "
               "nguồn được nêu, thường dùng ±10 phần trăm)."))
    b.append(note("<b>Ghi chú về ±10 per cent.</b> Bản in viết dung sai mặc "
                  "định là ‘±10 per cent’ (dùng chữ ‘per cent’ chứ không phải "
                  "ký hiệu %); hình thức này được giữ nguyên trong bản tiếng "
                  "Anh, còn bản tiếng Việt nêu là ‘phần trăm’."))
    b.append(p("Trong các điều kiện trên, nhiệt độ bề mặt tối đa của thiết bị "
               "phải thấp hơn 10°C so với nhiệt độ tối đa cho phép của bất kỳ "
               "đám mây bụi hoặc lớp bụi nào mà thiết bị dự định được sử dụng. "
               "Các nhiệt độ cho phép đó như sau."))
    b.append(p("Thứ nhất, nhiệt độ bề mặt tối đa của vỏ bọc thiết bị phải "
               "không vượt quá hai phần ba trừ đi 10°C so với nhiệt độ bắt "
               "lửa của đám mây bụi mà thiết bị có thể hoạt động trong đó. "
               "(Điều này có nghĩa, ví dụ, đối với loại bụi có nhiệt độ bắt "
               "lửa đám mây là 280°C (lưu huỳnh), nhiệt độ bề mặt tối đa của "
               "vỏ bọc không được vượt quá 176°C {[280 × 2/3] − 10) ở nhiệt "
               "độ môi trường tối đa (mức tăng nhiệt độ bề mặt là 136 °C ở "
               "nhiệt độ môi trường 40 °C))."))
    b.append(note("<b>Ghi chú về ngoặc trong ví dụ lưu huỳnh.</b> Bản in viết "
                  "biểu thức là ‘{[280 × 2/3] − 10)’ với dấu ngoặc nhọn mở "
                  "không được đóng và dấu ngoặc tròn đóng không được mở; hình "
                  "thức này được giữ nguyên trong bản tiếng Anh."))
    b.append(p("Thứ hai, nhiệt độ bề mặt tối đa của vỏ bọc thiết bị không "
               "được vượt quá nhiệt độ thấp hơn 85°C so với nhiệt độ bắt lửa "
               "tối thiểu của một lớp bụi 5mm. (Điều này có nghĩa là đối với "
               "lignit, có nhiệt độ bắt lửa lớp là 225°C, nhiệt độ bề mặt vỏ "
               "bọc tối đa cho phép sẽ là 140°C (225 − 75 − 10) hay mức tăng "
               "100 °C ở nhiệt độ môi trường 40 °C)."))
    b.append(note("<b>Ghi chú về mâu thuẫn 85 °C và 225 − 75 − 10.</b> Bản in "
                  "nêu quy định ‘85°C lower’ nhưng ví dụ lignit lại tính "
                  "‘140°C (225 − 75 − 10)’, và viết ‘5mm’ không có dấu cách "
                  "cùng ‘an layer ignition temperature’; tất cả được giữ "
                  "nguyên trong bản tiếng Anh, còn bản tiếng Việt nêu theo "
                  "nghĩa định."))
    b.append(p("Mức dự phòng 10 °C thường được đưa vào nhiệt độ bề mặt làm "
               "việc tối đa quy định cho thiết bị theo BS 6467, Phần 1¹ và do "
               "đó chỉ cần nhân nhiệt độ đám mây bụi với hai phần ba và trừ "
               "75 °C từ nhiệt độ bắt lửa lớp của nó để xác định tính phù hợp "
               "của thiết bị. Trường hợp thiết bị đáp ứng các yêu cầu này "
               "cũng được dùng trong môi trường có nguy cơ khí và hơi và vì "
               "thế được phân loại nhiệt độ, thì"))

    # E6/F1 (printed pp.460-461), Table 15.1 and the resumed sentence.
    b.append(table(T.HEAD151_VI, T.ROWS151_VI, T.CAPTION151_VI))
    if T.NOTE151_VI:
        b.append(note(T.NOTE151_VI))
    b.append(note("<b>Ghi chú về các nét in đặc biệt của Bảng 15.1.</b> Bản in "
                  "xếp các dòng theo thứ tự T1, T4, T2, T3, T5, T6, dùng "
                  "nhan đề ‘N(’n’)’ với dấu ngoặc đôi, và đánh dấu ¹ vào giá "
                  "trị chiếm ưu thế trong từng dòng; các hình thức này được "
                  "giữ nguyên trong bản tiếng Anh, còn bản tiếng Việt nêu "
                  "theo nghĩa định."))
    b.append(p("mức dự phòng 10 °C không nhất thiết được tính đến trong phân "
               "loại nhiệt độ. Đối với mọi loại bảo vệ thích hợp cho rủi ro "
               "khí hoặc hơi, ngoại trừ loại bảo vệ ‘N’, chỉ dùng hệ số 5 °C "
               "cho các cấp nhiệt độ T3–T6, với 10 °C chỉ được áp dụng cho T1 "
               "và T2. (Đối với loại bảo vệ ‘N’ không dùng hệ số nào cả.) Trường "
               "hợp thiết bị đã được phân loại nhiệt độ theo BS/EN 50014⁹ "
               "được dùng trong môi trường bụi mà không thay đổi gì vì, ngoài "
               "các xét đoán về nhiệt độ bề mặt, có thể chứng minh là nó đáp "
               "ứng BS 6467, phần 1,⁴ thì cách sử dụng được phép của thiết bị "
               "được cho trong Bảng 15.1."))
    b.append(note("<b>Ghi chú về ‘part 1,⁴’.</b> Bản in viết chữ ‘part’ thường "
                  "ở cụm ‘BS 6467, part 1,⁴’ (khác với ‘Part 1¹’ ở nơi khác); "
                  "hình thức này được giữ nguyên trong bản tiếng Anh."))

    # F2-F5 (printed p.461), headings 15.4 and 15.4.1, 'Enclosure materials'.
    b.append(h3("15.4 Yêu cầu cấu tạo cơ bản",
                "15.4 Basic constructional requirements"))
    b.append(p("Như có thể dự liệu, các yêu cầu về cấu tạo của loại thiết bị "
               "này chủ yếu xoay quanh nhu cầu về toàn vẹn vỏ bọc đã được đề "
               "cập trong Mục 15.2. Tuy nhiên, vẫn có các yêu cầu về độ bền "
               "vật lý và kết nối điện, nhưng những yêu cầu này rất tổng "
               "quát và không khác nhiều so với những yêu cầu áp dụng cho "
               "thiết bị dùng trong môi trường có nguy cơ khí và hơi."))
    b.append(h4("15.4.1 Vật liệu vỏ bọc và độ bền cơ học",
                "15.4.1 Enclosure materials and mechanical strength"))
    b.append(h4("Vật liệu vỏ bọc", "Enclosure materials"))
    b.append(p("Yêu cầu cơ bản về vật liệu vỏ bọc là nó phải chịu được các "
               "điều kiện môi trường và các điều kiện vận hành khác mà nó có "
               "thể phải đối mặt trong vận hành. Những điều này chủ yếu là "
               "vấn đề bảo đảm rằng thông số kỹ thuật vật liệu của nhà sản "
               "xuất phù hợp với mục đích sử dụng đã chọn và với các tiêu chí "
               "lựa chọn. Tuy nhiên, có một yêu cầu cụ thể là bảo đảm rằng mọi "
               "vật liệu vỏ bọc không bị vận hành vượt quá các định mức của "
               "nhà sản xuất khi chịu nhiệt độ cao hơn 10 °C so với nhiệt độ "
               "tối đa mà chúng sẽ đạt được ở nhiệt độ môi trường tối đa và "
               "trong các điều kiện dịch vụ khắc nghiệt nhất mà chúng được "
               "thiết kế. Điều này dễ xác định ở giai đoạn chế tạo và cần "
               "thiết để bảo đảm có thể duy trì độ bền vỏ bọc và xếp hạng IP. "
               "Yêu cầu này đương nhiên không khắc nghiệt hơn các yêu cầu áp "
               "dụng cho thiết bị dùng trong môi trường có nguy cơ khí và "
               "hơi."))
    b.append(p("Như đối với vỏ bọc của thiết bị dùng trong môi trường có nguy "
               "cơ khí và hơi, có một hạn chế về hàm lượng magiê trong bất kỳ "
               "vỏ bọc kim loại nhẹ nào tiếp xúc bên ngoài hoặc trong các bộ "
               "phận của nó, nhằm giảm thiểu nguy cơ tia lửa nhiệt nhôm "
               "(thermite) nếu vỏ bọc bị vật thể thép bị ôxy hóa (gỉ) va "
               "chạm."))
    b.append(p("Một yêu cầu cuối cùng là vật liệu không được cháy hoặc lan "
               "truyền ngọn lửa nếu bị đánh lửa. Đây không chủ yếu là yêu cầu "
               "đối với vỏ bọc, vì nếu vỏ bọc bị đánh lửa từ bên ngoài thì "
               "nguồn gây đánh lửa bụi đã hiện diện sẵn."))
    # The unfinished sentence continuing onto printed p.462 is out of scope.
    return "".join(b)


def body_en():
    b = []

    # A0-A2 (printed p.456). The shell owns the chapter h2; the module owns
    # the two printed standard subtitle lines and the opening paragraphs.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("<b>(BS 6467, Part 1 (1985))<br>(BS 7535 (1992))</b>"))
    b.append(p("The approach to protection of apparatus for use in the "
               "presence of combustible dusts has always been quite different "
               "to that for gases and vapours. The fact that dust clouds are "
               "clearly visible, producing a high degree of opacity, has "
               "created a situation where processing of dusts needs a high "
               "degree of control of dust clouds so that work can take place. "
               "In addition, the prevention of entry of particulate matter "
               "such as dust into the interior of electrical apparatus is "
               "relatively easy by the specification of its enclosure, unlike "
               "the situation in gases and vapours where this is difficult to "
               "achieve and maintain."))
    b.append(p("Conversely, dust settles unlike gases and vapours and a "
               "release leading to a dust cloud will leave a dust layer around "
               "the point of release rather than dispersing. This requires a "
               "high standard of housekeeping and the consideration of the "
               "effects of layers of dust (nominally assumed to be 5 mm of "
               "maximum thickness) on surface temperatures of enclosures. "
               "This has coloured the approach to use of electrical apparatus "
               "in dust risks and led to a situation where the construction "
               "of apparatus is based upon the ability to exclude dust, and a "
               "less rigorous form of certification control has been applied. "
               "The effects of dust layers raising the temperature of "
               "enclosures is dealt with in the selection of apparatus and "
               "not the construction."))
    b.append(note("<b>Source quirk: the 5 mm dust layer.</b> The print states "
                  "a nominally assumed maximum dust-layer thickness of 5 mm; "
                  "this is retained as printed."))

    # A3-A4+A5-B1-C2 (printed pp.456-458), heading 15.1 and zone headings.
    b.append(h3("15.1 Situation in respect of standardization",
                "15.1 Situation in respect of standardization"))
    b.append(p("Although the installation of apparatus in dust risk areas has "
               "been practiced for very many years, the apparatus was "
               "generally selected from industrial ranges of apparatus on the "
               "basis of its ability to exclude dust and no formal Standards "
               "or Certification/Approval procedures have been present. This "
               "changed in 1985 with the publication of BS 6467, Part 1¹ which, "
               "for the first time, specified in considerable detail the "
               "constructional requirements for apparatus for this type of "
               "explosive atmosphere."))
    b.append(p("BS 6467, Part 1 (1985)¹ specified two types of apparatus: dust "
               "tight apparatus; and dust protected apparatus. This reflected "
               "the approach at the time which divided hazardous areas where "
               "dust was present into two areas, Zone Z and Zone Y, the former "
               "being similar in definition to Zone 1 in the case of gases and "
               "vapours, and the latter to Zone 2, an approach later confirmed "
               "in BS 6467, Part 2¹ in 1988. This approach excluded any "
               "consideration of areas such as the interior of dust vessels, "
               "which would be Zone 0 in the gas or vapour case, and such "
               "Zones have been considered as those in which electrical "
               "equipment should not be mounted or only be mounted in "
               "exceptional conditions and, in those cases, treated specially. "
               "This has not produced too much of a hardship as installations "
               "in such Zones where dust is a problem have tended to be rare "
               "and often have been such things as thermocouples, resistance "
               "thermometers and similar devices, which need only to insert a "
               "sealed stainless steel or similar tube into the area. It is "
               "upon this basis that the requirements in BS 6467, Part 1 "
               "(1985) for ‘Apparatus with Protection by Enclosure for Use in "
               "the Presence of Combustible Dust’ were framed. (The use of the "
               "term ‘Combustible Dust’ is used rather than ‘flammable dust’ "
               "to emphasize that dusts behave differently to gases and "
               "vapours)."))
    b.append(p("BS 6467, Part 1¹ effectively considers apparatus protected "
               "against the ingress of dust, where dust can enter but not in "
               "sufficient quantities to interfere with the operation of "
               "apparatus, and dust tight apparatus, where dust is effectively "
               "excluded. The reason for the two different levels is to relate "
               "to Zone Z where dust tight apparatus is necessary, and Zone Y "
               "where only dust protected apparatus is necessary except where "
               "the dust is conducting (when no differentiation is made "
               "because of the added risk of internal short circuiting by the "
               "dust)."))
    b.append(p("In addition to BS 6467, Part 1¹, a further Standard, BS 7535 "
               "(1992)² exists which gives guidance upon the selection of "
               "apparatus to the BS/EN 500 range of Standards (Electrical "
               "Apparatus for Potentially Explosive Atmospheres of gas/air, "
               "vapour/air or mist/air, see Chapters 7 to 14) for use in the "
               "presence of combustible dusts. This Standard actually refers "
               "to the European Standards in their first editions (BS 5501 "
               "series) due to its age but its criteria are equally relevant "
               "to the second editions (BS/EN 500 range). Again, because of "
               "its age, it still refers to Zone Z and Y."))
    b.append(p("As earlier explained in Chapter 6, the situation in regard to "
               "area classification for dusts is set to change in a very short "
               "time to a three-Zone system similar to that for gases. This is "
               "based upon an IEC draft document (IEC 1241-3), which has "
               "received approval as a possible new British Standard and "
               "identifies the following zones."))
    b.append(h4("Zone 20", "Zone 20"))
    b.append(p("Zone 20 is defined as being where dust clouds are normally "
               "present, such as the inside of vessels, and is similar in "
               "definition to Zone 0 for gases and vapours."))
    b.append(h4("Zone 21", "Zone 21"))
    b.append(p("Zone 21 is defined as being where dust clouds are regularly "
               "produced, such as loading apertures, and is similar in "
               "definition to Zone 1 for gases and vapours."))
    b.append(h4("Zone 22", "Zone 22"))
    b.append(p("Zone 22 is defined as being where dust clouds are rare, "
               "usually being produced by disturbance of dust layers which "
               "have formed despite the high level of housekeeping required "
               "in such areas, and is similar in definition to Zone 2 for "
               "gases and vapours."))
    b.append(p("The specific construction requirements for apparatus for dust "
               "risks in respect of these Zones do not yet exist, the "
               "production of the relevant Standards not yet being complete. "
               "There is, however, some guidance in this matter. First Zone "
               "21 can be related to Zone Z and thus apparatus for Zone Z, as "
               "previously described, may also be considered as appropriate "
               "to Zone 21 and apparatus for Zone Y for Zone 22. This leaves "
               "Zone 20 where no national or international approach has "
               "historically existed. The problem is not, however, new and in "
               "1973 a particular company Code (RoSPA/IC13), recognizing the "
               "ultimate likelihood of a requirement for sophisticated "
               "instrumentation in what will be Zone 20, used a three-Zone "
               "classification system for dusts. This led to some guidance "
               "for intrinsically safe apparatus in Zone 20 appearing in both "
               "that code and other documents based upon the use of "
               "intrinsically safe apparatus ‘ia’ contained within an IP6X "
               "enclosure to BS/EN 60529⁴ (like the situation in gas and "
               "vapour risks intrinsically safe apparatus is the only type of "
               "equipment likely to be acceptable in such high risk zones "
               "because of the constant or nearly constant presence of the "
               "explosive atmosphere)."))
    b.append(note("<b>Source quirks: ‘(RoSPA/IC13)’ and ‘IP6X to BS/EN "
                  "60529⁴’.</b> Both printed forms are retained verbatim here; "
                  "the Vietnamese follows the intended meaning."))

    # C3-C6 (printed p.458), heading 15.2 with its italic subtitle.
    b.append(h3("15.2 Basic types of apparatus for use with combustible dusts",
                "15.2 Basic types of apparatus for use with combustible dusts"))
    b.append(p("<i>(apparatus in accordance with BS 6467, Part 1)</i>"))
    b.append(p("The method by which this apparatus is made suitable for use "
               "in explosive atmospheres of dust and air is to exclude the "
               "dust from within the enclosure. This type of apparatus is, "
               "tested to ensure that it does so."))
    b.append(note("<b>Source quirk: stray comma.</b> The print reads ‘This "
                  "type of apparatus is, tested to ensure that it does so.’ "
                  "with a stray comma after ‘is’; it is retained verbatim."))
    b.append(p("The possibility of decrease in pressure in all enclosures due "
               "to temperature changes, either ambient or operational, needs "
               "to be recognized and thus all dust-tight enclosures are "
               "tested on the basis of reduced internal pressure as defined "
               "in the appropriate Standard."))
    b.append(p("While testing for dust entry is all that is required to "
               "satisfy the basic requirements for this type of apparatus, it "
               "must be recognized that testing for liquid ingress is also "
               "necessary for all outdoor apparatus."))

    # C7-C9+D1-D2 (printed pp.458-459), heading 15.2.1 and its subheadings.
    b.append(h4("15.2.1 Degrees of enclosure",
                "15.2.1 Degrees of enclosure"))
    b.append(p("There are two types of apparatus which are differentiated by "
               "their degree of enclosure. These are as follows."))
    b.append(h4("Apparatus with dust tight enclosures",
                "Apparatus with dust tight enclosures"))
    b.append(p("This constitutes apparatus with an enclosure which is so "
               "constructed as to exclude all ingress of observable dust "
               "particles. This means that the apparatus is dust tight as no "
               "visible dust will have entered during the tests for enclosure "
               "suitability which includes the enclosure being operated in "
               "the dust-test atmosphere at reduced pressure to give dust "
               "every opportunity to enter. Such enclosures must be tested "
               "for Degree of Protection IP6X in accordance with BS/EN 60529⁴ "
               "(for older enclosures produced prior to the introduction of "
               "BS/EN 60529 the Standard used was BS 5490⁵ and for switchgear, "
               "which is now included in BS/EN 60529 and therefore does not "
               "have a specific unique Standard, BS 5420⁶ was historically "
               "appropriate). It is notable that even rotating machines must "
               "comply with this requirement rather than the requirements of "
               "EN 60034, Part 5⁷ (produced in the UK as BS 4999, Part 10⁵⁸) "
               "which allow variations specifically relating to enclosures of "
               "rotating machines and are in normal circumstances considered "
               "as sufficient in other areas. For apparatus for outdoor use "
               "is a total enclosure integrity package of IP65 is required "
               "and this enclosure is considered as necessary for all "
               "apparatus used in Zone Z and, in conducting dust situations, "
               "apparatus for Zone Y."))
    b.append(note("<b>Source quirks: ‘BS 4999, Part 10⁵⁸’ and the IP65 "
                  "sentence.</b> The print has superscripts 5 and 8 run "
                  "together as ‘Part 10⁵⁸’, and the sentence ‘For apparatus "
                  "for outdoor use is a total enclosure integrity package of "
                  "IP65 is required’; both are retained verbatim while the "
                  "Vietnamese states the intended meaning."))
    b.append(h4("Dust-protected enclosures", "Dust-protected enclosures"))
    b.append(p("This is a lower level of enclosure integrity and what is "
               "required here is that the enclosure is at least IP5X to "
               "BS/EN 60529⁴ or the more historic equivalent Standards already "
               "quoted. In addition, because of the different intended use "
               "such apparatus is restricted to Zone Y and only then "
               "acceptable for non-conducting dusts). In addition, enclosures "
               "offering IP5X to EN 60034, Part 5⁷ (BS 4999, Part 10⁵⁸) are "
               "acceptable in these circumstances even though they offer a "
               "slightly lower level of protection due to the requirement of "
               "normal rotating machines. In this case, however, there is a "
               "specification additional to those in the IP Standards quoted "
               "above in that the amount of dust entering the enclosure "
               "during the test must not exceed the equivalent of 10 g/m³ as "
               "derived from the mass of dust entering divided by the free "
               "volume (after deducting the volume of components and "
               "assemblies within the enclosure from the total internal "
               "enclosure volume) of the enclosure. This is an approach to "
               "defining the criteria for passing the test and reduce the "
               "reliance on the opinion of the expert executing the test, and "
               "again it must be remembered that the dust level quoted only "
               "refers to non-conducting dust. This means an IP54 enclosure "
               "for use outdoors."))
    b.append(note("<b>Source quirks: ‘10 g/m³’ and the unmatched "
                  "parenthesis.</b> The print reads ‘10 g/m³’ and ends the "
                  "sentence ‘only then acceptable for non-conducting dusts).’ "
                  "with an unmatched closing parenthesis; both are retained "
                  "verbatim."))

    # D3-E5 (printed pp.459-460), heading 15.3; Table 15.1 interrupts E5.
    b.append(h3("15.3 Operational requirements",
                "15.3 Operational requirements"))
    b.append(p("The apparatus may or may not spark within the enclosure as "
               "the enclosure constitutes the protection. Thus there is no "
               "requirement for energy limitation in a spark or arc but only "
               "of limitation of the maximum external surface temperature of "
               "the enclosure. The enclosure temperature needs to be "
               "determined in the following conditions: first, with the "
               "enclosure mounted in the most unfavourable normal mounting "
               "position (that which gives the maximum temperature on any "
               "part of the surface of the enclosure); second, the supply "
               "voltage must be adjusted to any value within its operating "
               "tolerance to give the maximum temperature in the above "
               "position (where no supply voltage tolerance is quoted it is "
               "normal to utilize ±10 per cent)."))
    b.append(note("<b>Source quirk: ‘±10 per cent’.</b> The print gives the "
                  "default supply tolerance as ‘±10 per cent’ rather than a "
                  "percentage sign; the printed form is retained."))
    b.append(p("In the above circumstances the maximum surface temperature of "
               "the apparatus must be 10°C lower than the maximum permitted "
               "temperature for any dust cloud or layer in which the "
               "apparatus is intended to be used. These permitted temperatures "
               "are as follows."))
    b.append(p("First, the maximum surface temperature of the apparatus "
               "enclosure must be not more than two thirds less 10°C of the "
               "ignition temperature of the dust cloud in which the apparatus "
               "may operate. (This means, for example, that for a dust with a "
               "cloud ignition temperature of 280°C (sulphur) the maximum "
               "surface temperature of the enclosure may not exceed 176°C "
               "{[280 × 2/3] − 10) at the maximum ambient temperature (a "
               "surface temperature elevation of 136 °C at an ambient of 40 "
               "°C))."))
    b.append(note("<b>Source quirk: ‘{[280 × 2/3] − 10)’.</b> The printed "
                  "expression has an unmatched opening brace and an unmatched "
                  "closing parenthesis; it is retained verbatim."))
    b.append(p("Second, the maximum surface temperature of the apparatus "
               "enclosure may not exceed a temperature 85°C lower than the "
               "minimum ignition temperature of a 5mm dust layer. (This means "
               "that for lignite, which has an layer ignition temperature of "
               "225°C, the maximum enclosure surface temperature permitted "
               "will be 140°C (225 − 75 − 10) or an elevation of 100 °C at an "
               "ambient of 40 °C)."))
    b.append(note("<b>Source quirks: ‘85°C lower’ versus ‘225 − 75 − 10’.</b> "
                  "The rule says ‘85°C lower’ while the lignite example "
                  "computes ‘140°C (225 − 75 − 10)’; the print also has "
                  "‘5mm’ without a space and ‘an layer ignition temperature’. "
                  "All are retained verbatim."))
    b.append(p("The 10 °C margin is normally included in the maximum operating "
               "surface temperature specified for apparatus to BS 6467, Part "
               "1¹ and thus it is only necessary to multiply the dust cloud "
               "temperature by two thirds and subtract 75 °C from its layer "
               "ignition temperature in order to identify the suitability of "
               "the apparatus. Where apparatus complying with these "
               "requirements is also used in gas and vapour risks and is thus "
               "temperature classified, the"))

    # E6/F1 (printed pp.460-461), Table 15.1 and the resumed sentence.
    b.append(table(T.HEAD151_EN, T.ROWS151_EN, T.CAPTION151_EN))
    if T.NOTE151_EN:
        b.append(note(T.NOTE151_EN))
    b.append(note("<b>Source quirks in Table 15.1.</b> The print orders the "
                  "rows T1, T4, T2, T3, T5, T6, prints the heading ‘N(’n’)’ "
                  "with doubled parentheses, and marks the predominant value "
                  "in each row with ¹; all are retained verbatim."))
    b.append(p("10 °C margin is not necessarily taken into account during "
               "temperature classification. For all types of protection "
               "appropriate to gas or vapour risks with the exception of type "
               "of protection ‘N’ a factor of only 5 °C is used for temperature "
               "classes T3–T6 with the 10 °C only being applied to T1 and T2. "
               "(For type of protection ‘N’ no factor at all is used.) Where "
               "apparatus which is temperature classified to BS/EN 50014⁹ is "
               "used in dust situations without change because, in other than "
               "surface temperature considerations, it can be shown to satisfy "
               "BS 6467, part 1,⁴ the permissible usage of the apparatus is "
               "shown in Table 15.1."))
    b.append(note("<b>Source quirk: ‘part 1,⁴’.</b> The print uses a lower-case "
                  "‘part’ in ‘BS 6467, part 1,⁴’ (elsewhere ‘Part 1¹’); the "
                  "printed form is retained."))

    # F2-F5 (printed p.461), headings 15.4 and 15.4.1, 'Enclosure materials'.
    b.append(h3("15.4 Basic constructional requirements",
                "15.4 Basic constructional requirements"))
    b.append(p("As may be expected, the requirements for the construction of "
               "this type of apparatus revolve principally around the needs "
               "of the enclosure integrity which have already been dealt with "
               "in Section 15.2. There are, however, requirements for physical "
               "strength and electrical connection but these are very general "
               "and not dissimilar to those applied to apparatus for gas and "
               "vapour risks."))
    b.append(h4("15.4.1 Enclosure materials and mechanical strength",
                "15.4.1 Enclosure materials and mechanical strength"))
    b.append(h4("Enclosure materials", "Enclosure materials"))
    b.append(p("The basic enclosure material requirement is that it will "
               "withstand the environmental and other operating conditions "
               "which it may be called upon to deal with in operation. These "
               "are mainly a matter of ensuring that the manufacturer's "
               "material specification matches chosen use and thus selection "
               "criteria. There is, however, a specific requirement to ensure "
               "that all enclosure materials are not operated outside their "
               "manufacturer's ratings when subjected to a temperature 10 °C "
               "higher than the maximum temperature which they will achieve "
               "at maximum ambient and in the most onerous service conditions "
               "for which they are designed. This is clearly identifiable at "
               "the construction stage and is necessary to ensure that "
               "enclosure strength and IP-rating can be maintained. This "
               "requirement is, of course, no more onerous than those applied "
               "to apparatus for gas and vapour risks."))
    b.append(p("As with enclosures for apparatus for gas and vapour risks, "
               "there is a restriction on the magnesium content of any of the "
               "externally exposed light metal enclosures or parts thereof to "
               "minimize the risk of thermite sparking if the enclosure is "
               "struck by an oxidized (rusty) steel item."))
    b.append(p("A final requirement is that materials must not be combustible "
               "or propagate flame if ignited. This is not principally an "
               "enclosure requirement as if the enclosure is ignited from "
               "outside the source of dust ignition already exists."))
    # The unfinished sentence continuing onto printed p.462 is out of scope.
    return "".join(b)
