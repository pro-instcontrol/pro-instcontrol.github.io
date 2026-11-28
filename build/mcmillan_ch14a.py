# -*- coding: utf-8 -*-
"""Chapter 14, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 427-436 (PDF pp. 448-457).

Covers the chapter-opening paragraphs and standard subtitle lines, 14.1 The
situation in respect of standardization, 14.2 Basic requirements of the
protection concept, 14.3 General constructional requirements (14.3.1-14.3.5),
and every unnumbered subheading through 'Insulation tests between conductors
and the frame or earth'. Tables 14.1-14.3 sit at their printed positions.
The chapter shell owns the chapter h2, the printed references, the glossary,
the source-quirk note and the copyright.

Full faithful EN/VI translation of survey A blocks A1-J9. Printed quirks are
kept verbatim in the English text (historically, counties, the unclosed quote
in 'Type 'N apparatus.', etc.., 1 Kg, 20cms, the stray comma after 'may', the
1 A / 15N inconsistency, 70 °C against 80°C, 90 V peak against 90V peak, and
'in excess of one third of the other distances'), with bilingual notes; the
Vietnamese follows the intended meaning. The sentence continuing onto
printed p.437 is deliberately excluded. This is an unofficial study
translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, ul, ol
import mcmillan_tbl14_1_3 as T1


def body_vi():
    b = []

    # A0-A2 (printed p.427). The shell owns the chapter h2; the module owns
    # the printed standard subtitle lines and the two opening paragraphs.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("<b>(BS 6941 (1988))<br>(IEC 79-15 (1987))</b>"))
    b.append(p("Khác với các nguyên lý bảo vệ đã được mô tả trước đây, nguyên "
               "lý bảo vệ (loại bảo vệ) ‘N’ chỉ được thiết kế để lắp đặt trong "
               "các khu vực Vùng 2. Ở những khu vực này, nguy cơ xuất hiện bầu "
               "khí quyển nổ thấp hơn rất nhiều so với Vùng 0 và Vùng 1, đến "
               "mức người ta từng coi rằng việc lắp đặt thiết bị công nghiệp "
               "‘chất lượng cao’, vốn không phát sinh tia lửa hay bề mặt nóng "
               "có khả năng gây đánh lửa trong vận hành bình thường, là đủ để "
               "đối phó với nguy cơ đó. Việc dùng thuật ngữ ‘chất lượng cao’ "
               "không hàm ý thiết bị đặc biệt, mà được dùng để bảo đảm rằng "
               "người lắp đặt không cắt giảm công đoạn và sử dụng thiết bị "
               "thực sự không dành cho môi trường công nghiệp. Trước đây, bất "
               "kỳ thiết bị không phát sinh tia lửa nào được thiết kế riêng "
               "cho môi trường công nghiệp và không có tính năng đặc biệt nào "
               "đòi hỏi mức bảo trì cao hơn mức bình thường đều được chấp "
               "nhận. Đối với thiết bị có phát sinh tia lửa hoặc trở nên đủ "
               "nóng để gây đánh lửa trong vận hành bình thường, phải sử dụng "
               "các nguyên lý bảo vệ tương thích với Vùng 1."))
    b.append(note("<b>Ghi chú về các nét in đặc biệt ở đoạn mở đầu.</b> Từ "
                  "‘historically’ xuất hiện hai lần và câu cuối in là ‘the "
                  "Zone 1 compatible protection concepts would, have to be "
                  "used’ với dấu phẩy thừa sau ‘would’. Cả hai được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt nêu theo nghĩa định."))
    b.append(p("Tình hình này tiếp diễn cho đến năm 1972, khi một Tiêu chuẩn "
               "Anh lần đầu tiên đưa vào khả năng thiết bị có thể tạo ra hồ "
               "quang hoặc tia lửa được ban hành. Tiêu chuẩn này đề xuất một "
               "số phương pháp tránh đánh lửa từ các tia lửa đó, dựa trên các "
               "cách tiếp cận dùng cho Vùng 1, nhưng với mức độ an toàn thấp "
               "hơn để phản ánh khả năng thấp hơn của sự hiện diện của bầu "
               "khí quyển nổ."))

    # A3-A4+B1-C6 (printed pp.427-429), heading 14.1.
    b.append(h3("14.1 Tình hình liên quan đến việc chuẩn hóa",
                "14.1 The situation in respect of standardization"))
    b.append(p("Cách tiếp cận trong lựa chọn và sử dụng thiết bị cho Vùng 2 "
               "ban đầu được mô tả trong BS/CP1003, Phần 3¹ (sử dụng) và "
               "trong BS 4137², được xây dựng để cung cấp chi tiết về lựa "
               "chọn thiết bị công nghiệp không phát sinh tia lửa dùng trong "
               "Vùng 2. Cách tiếp cận này tiếp tục được áp dụng đến ngày nay "
               "và việc sử dụng ‘thiết bị công nghiệp được lựa chọn’ vẫn được "
               "công nhận, nhưng hiện nay BS 5345, Phần 1³ quy định các phẩm "
               "chất cần có của những người lựa chọn thiết bị như sau: thứ "
               "nhất, họ phải quen thuộc với các yêu cầu của mọi Tiêu chuẩn "
               "và Quy thực hành liên quan, kể cả cách diễn giải của chúng. "
               "(Yêu cầu này rõ ràng nhằm bảo đảm rằng họ có một mức độ chuyên "
               "môn nhất định về cấu tạo và lắp đặt thiết bị được bảo vệ "
               "chống nổ); thứ hai, họ phải có được mọi thông tin cần thiết "
               "để có thể thực hiện việc lựa chọn. (Điều này có nghĩa là họ "
               "cần biết chi tiết thiết kế và mục đích sử dụng của thiết bị); "
               "và thứ ba, nếu cần thử nghiệm thì các thử nghiệm đó phải được "
               "thực hiện bằng thiết bị và quy trình thử nghiệm tương tự như "
               "những gì được dùng bởi các phòng thử nghiệm bên thứ ba được "
               "công nhận. (Điều này có nghĩa là các phương tiện và kiến thức "
               "sẵn có của những người lựa chọn thiết bị phải tương tự như "
               "những gì mà các ‘Tổ chức thông báo’ có theo Chỉ thị "
               "76/117/EEC⁴ hoặc 94/9/EC⁵)."))
    b.append(p("Các yêu cầu nêu trên cho thấy rõ rằng việc lựa chọn thiết bị "
               "công nghiệp dựa trên tính chất không phát sinh tia lửa và "
               "không trở nên đủ nóng để gây đánh lửa không phải, và chưa từng "
               "là, một cách tiếp cận tương đối lỏng lẻo do mọi người lắp đặt "
               "sử dụng, mà là một cách tiếp cận tương đối trang trọng và, dù "
               "được sử dụng bởi những bên không phải là tổ chức chứng "
               "nhận/phê duyệt bên thứ ba, vẫn được dự định bao gồm mức độ "
               "chi tiết tương tự như mức độ sẽ liên quan nếu một tổ chức "
               "chứng nhận/phê duyệt bên thứ ba được sử dụng."))
    b.append(p("Tình hình lựa chọn chưa bao giờ hoàn toàn thỏa đáng và dẫn "
               "đến việc ngành công nghiệp tìm kiếm một hình thức phê duyệt "
               "bên thứ ba nào đó cho thiết bị họ dự định sử dụng và, không "
               "có gì ngạc nhiên, đã hướng sang HM Factory Inspectorate, cơ "
               "quan quản lý công nghiệp ngoài ngành khai thác than. Vì không "
               "có Tiêu chuẩn cụ thể và do đó không có bộ quy tắc chi tiết để "
               "phê duyệt các thiết bị như vậy, Factory Inspectorate không "
               "thể phê duyệt thiết bị nhưng có thể xác nhận rằng thiết bị "
               "không có tiếp điểm phát sinh tia lửa, không có bề mặt nóng và "
               "không có đặc điểm kỳ lạ nào khác khiến nó không được chấp "
               "nhận theo hiểu biết hiện có vào thời điểm đó. Điều này được "
               "thực hiện thông qua việc ban hành một ‘Thư không có ý kiến "
               "phản đối’, được coi là sự phê duyệt, nhưng thực tế thì không "
               "phải vậy. Đó đúng là những gì nó nói – một sự xác nhận rằng "
               "Factory Inspectorate không biết có lý do gì khiến thiết bị "
               "không được lắp đặt trong Vùng 2. Khác với hầu hết các chứng "
               "nhận vẫn tiếp tục có giá trị ngay cả sau khi các yêu cầu "
               "thay đổi, miễn là không có bằng chứng về nguy hiểm sắp xảy "
               "ra, thì thư này sẽ trở nên vô hiệu nếu sự hiểu biết gia tăng "
               "làm lộ ra vấn đề."))
    b.append(p("Tình hình này, ngoại trừ đặc thù của Anh về ‘Thư không có ý "
               "kiến phản đối’, gần như giống hệt tình hình Vùng 2 ở hầu hết "
               "các quốc gia phát triển khác – chẳng hạn Đức có yêu cầu lựa "
               "chọn trong tài liệu lắp đặt VDE 0165, và Hoa Kỳ có Điều 500 "
               "của Bộ quy tắc điện quốc gia."))
    b.append(note("<b>Ghi chú về ‘counties’.</b> Bản in viết ‘most other "
                  "developed counties’ (counties thay vì countries); hình "
                  "thức in này được giữ nguyên trong bản tiếng Anh, còn bản "
                  "tiếng Việt dịch theo nghĩa ‘các quốc gia’."))
    b.append(p("Khi công nghiệp phát triển, đã có nhu cầu đáng kể về thiết bị "
               "Vùng 2 có phát sinh tia lửa, vì người ta nhận ra rằng các "
               "yêu cầu của Vùng 0 và Vùng 1 từng được áp dụng trước đây quá "
               "hạn chế đối với Vùng 2 và, như trong mọi lĩnh vực khác, sự "
               "xuất hiện của bóng bán dẫn đã đưa thêm nhiều phức tạp vào lĩnh "
               "vực này, tạo ra nhiều thiết bị hơn được lắp đặt trong khu vực "
               "nguy hiểm. Bên cạnh đó, nhu cầu ngày càng tăng về các yêu cầu "
               "cấu tạo dứt khoát đối với thiết bị Vùng 2 nhằm loại bỏ yếu tố "
               "‘phán đoán’ vốn có trong các quy trình lựa chọn. Điều này dẫn "
               "đến việc công bố Tiêu chuẩn Anh đầu tiên về sản xuất thiết bị "
               "cho Vùng 2, có tên là ‘Thiết bị có loại bảo vệ ’N’ và là "
               "BS 4683, Phần 3 (1972)⁶. Tiêu chuẩn này bắt đầu quá trình "
               "chuyển các tiêu chí lựa chọn thiết bị thành các yêu cầu về "
               "cấu tạo và mở đường cho việc chứng nhận đầy đủ bởi bên thứ "
               "ba."))
    b.append(p("Sự quan tâm quốc tế đối với các yêu cầu cấu tạo về thiết bị "
               "dùng trong Vùng 2 cũng tăng lên trong giai đoạn này và một ủy "
               "ban IEC⁷ đã được thành lập để xây dựng Tiêu chuẩn quốc tế cho "
               "loại thiết bị này, dùng ký hiệu quốc tế ‘n’ (Tiêu chuẩn Anh "
               "dùng ‘N’ để cho thấy nguyên lý bảo vệ là nguyên lý quốc gia, "
               "không phải quốc tế). Ủy ban IEC, không có gì ngạc nhiên khi "
               "đây là nỗ lực đầu tiên nhằm quốc tế hóa một tình hình vốn mang "
               "tính quốc gia cho đến thời điểm đó và bao gồm rất nhiều ý "
               "tưởng quốc gia khác nhau mà một số quốc gia khác không chấp "
               "nhận hoặc thậm chí không hiểu, đã gặp rất nhiều khó khăn "
               "trong việc đi đến thỏa thuận."))
    b.append(p("Đồng thời, những hạn chế của BS 4683, Phần 3, khi xét theo "
               "những tiến bộ tiếp theo, ngày càng rõ ràng và có nhiều ủng hộ "
               "việc thay thế nó bằng một Tiêu chuẩn chi tiết hơn bao gồm tất "
               "cả các ý tưởng trong ủy ban IEC⁷ mà Anh đồng ý (về cơ bản "
               "tất cả đều giống nhau, ngoại trừ khái niệm thở hạn chế do "
               "Thụy Sĩ phát triển). Tiêu chuẩn này được công bố năm 1988 với "
               "tên BS 6941⁸. Tiêu chuẩn này cũng đề cập đến các loại thiết "
               "bị cụ thể, chẳng hạn như động cơ điện loại ‘N’ (cũng được đề "
               "cập trong BS 5000, Phần 16 (1972)⁹) và các thiết bị chiếu "
               "sáng có bảo vệ loại ‘N’. (Cũng được đề cập trong BS 4533, "
               "Phần 2, Mục 2.1 (1976)¹⁰)."))
    b.append(p("Cuối cùng ủy ban IEC đã hoàn thiện văn bản của mình thành IEC "
               "79-15 (1987)¹¹ nhưng, do sự khác biệt về quan điểm trong "
               "IEC⁷, văn bản được ban hành dưới dạng báo cáo thay vì Tiêu "
               "chuẩn. Tuy nhiên, thực tế là BS 6941⁸ theo gần như chính xác "
               "văn bản của IEC 79-15¹¹ (ngoại trừ khái niệm thở hạn chế) "
               "khiến việc sử dụng Tiêu chuẩn này trở thành một cách tiếp "
               "cận cơ bản hợp lệ cho các yêu cầu kỹ thuật của loại bảo vệ "
               "‘N’."))
    b.append(p("IEC và CENELEC¹² hiện đang xây dựng một Tiêu chuẩn sẽ vừa "
               "mang tính châu Âu vừa mang tính quốc tế, dựa trên IEC "
               "79-15¹¹, điều này càng làm tăng sức nặng cho các yêu cầu "
               "trong BS 6941⁸."))
    b.append(p("Mặc dù hiện đã có một tiêu chuẩn cấu tạo chi tiết, sự linh "
               "hoạt trong lựa chọn thiết bị cho Vùng 2 mà không có yêu cầu "
               "bắt buộc phải được bên thứ ba phê duyệt vẫn tồn tại cả ở cấp "
               "quốc gia tại Anh và trong Chỉ thị 94/9/EC⁵ của EU. Tuy nhiên, "
               "các quy tắc mà theo đó việc lựa chọn này được thực hiện giờ "
               "sẽ là các quy tắc hiện có trong BS 6941⁸ và người kế nhiệm "
               "cấp châu Âu và quốc tế của nó."))
    b.append(note("<b>Ghi chú về lỗi in ở cuối 14.1.</b> Bản in viết ‘The "
                  "rules against which this selection takes place, however, "
                  "will now by those exist in BS 6941⁸ and its European and "
                  "international successor.’; cụm ‘by those exist’ được giữ "
                  "nguyên trong bản tiếng Anh, còn bản tiếng Việt nêu theo "
                  "nghĩa định."))

    # C7-C8+D1-D3 (printed pp.429-430), heading 14.2.
    b.append(h3("14.2 Yêu cầu cơ bản của khái niệm bảo vệ",
                "14.2 Basic requirements of the protection concept"))
    b.append(p("Định nghĩa của thiết bị Loại ‘N’ (n) là thiết bị không có khả "
               "năng gây đánh lửa bầu khí quyển nổ trong vận hành bình thường "
               "và lỗi khiến thiết bị có khả năng đó là khó có thể xảy ra. Giờ "
               "đây, khi tia lửa được chấp nhận là một phần của nguyên lý bảo "
               "vệ, định nghĩa cơ bản này có thể được mở rộng để bao hàm điều "
               "đó như sau: thứ nhất, trong vận hành bình thường thiết bị "
               "không được tạo ra hồ quang hay tia lửa có thể gây đánh lửa "
               "bầu khí quyển nổ, trừ khi hồ quang hoặc tia lửa đó được ngăn "
               "không gây đánh lửa bằng cách hạn chế dòng điện hoặc bằng một "
               "số biện pháp khác được xác định là có khả năng ngăn chặn sự "
               "đánh lửa đó; và thứ hai, thiết bị không được tạo ra nhiệt độ "
               "bề mặt có khả năng gây đánh lửa bầu khí quyển nổ, trừ khi "
               "nhiệt độ bề mặt đó được ngăn không gây đánh lửa bằng cách bao "
               "chứa hoặc bằng một biện pháp phù hợp khác."))
    b.append(p("Mặc dù các ‘Yêu cầu chung’ được xác định ở Chương 8 nói chung "
               "không áp dụng cho thiết bị Loại ‘N’, nhưng một số yêu cầu vẫn "
               "phù hợp – ví dụ việc phân nhóm thành IIA, IIB và IIC được "
               "thực hiện đối với thiết bị phát sinh tia lửa. Tương tự, "
               "phương pháp phân loại nhiệt độ bề mặt được dùng trong các "
               "nguyên lý bảo vệ khác cũng phù hợp với thiết bị Loại ‘N’."))
    b.append(note("<b>Ghi chú về dấu nháy chưa đóng.</b> Câu cuối in là "
                  "‘also appropriate to Type ‘N apparatus.’ – không có dấu "
                  "nháy đóng sau ‘N’; nhan đề in ở trang trước, ‘Apparatus "
                  "with Type of Protection ’N’ and was BS 4683, Part 3 "
                  "(1972)⁶’, cũng có cách đặt dấu nháy bất thường. Cả hai "
                  "được giữ nguyên trong bản tiếng Anh; bản tiếng Việt theo "
                  "nghĩa định."))
    b.append(p("Thiết bị cũng được kỳ vọng, giống như các thiết bị được bảo "
               "vệ khác, sẽ có các tính năng bổ sung khi được sử dụng trong "
               "những môi trường khắc nghiệt hơn môi trường ngoài trời bình "
               "thường, chẳng hạn như những nơi có thể xuất hiện hơi dung môi "
               "và nơi vỏ bằng nhựa có thể không phù hợp. Các yêu cầu bổ sung "
               "này, như trường hợp của các nguyên lý bảo vệ khác, được "
               "thỏa thuận trong từng trường hợp cụ thể liên quan đến từng "
               "rủi ro cụ thể, chẳng hạn như tiếp xúc thêm với hư hỏng cơ học "
               "hoặc hư hỏng hóa học, môi trường ẩm bất thường, v.v."))
    b.append(note("<b>Ghi chú về ‘etc..’.</b> Bản in viết ‘etc..’ với hai "
                  "dấu chấm; hình thức in này được giữ nguyên trong bản "
                  "tiếng Anh, còn bản tiếng Việt viết ‘v.v.’."))

    # D4-E4 (printed pp.430-431), headings 14.3 and 14.3.1-14.3.2.
    b.append(h3("14.3 Yêu cầu chung về cấu tạo",
                "14.3 General constructional requirements"))
    b.append(p("Các yêu cầu chung về cấu tạo là những yêu cầu áp dụng cho mọi "
               "loại thiết bị Loại ‘N’ và đề cập đến bảo vệ môi trường, độ bền "
               "cơ học và các kết nối điện."))
    b.append(h4("14.3.1 Bảo vệ môi trường", "14.3.1 Environmental protection"))
    b.append(p("Vì thiết bị Loại ‘N’ được giả định là bao gồm các mạch điện có "
               "thể chứa năng lượng gây cháy, nên sự xâm nhập của môi trường "
               "được giả định là có thể gây ra các lỗi bên trong cho phép các "
               "năng lượng đó được giải phóng. Vì lý do này, cũng như đối với "
               "các hình thức bảo vệ khác có hiện tượng tương tự, vỏ bọc của "
               "thiết bị được yêu cầu phải cung cấp mức độ bảo vệ thích hợp "
               "chống lại sự xâm nhập của chất lỏng và chất rắn có trong môi "
               "trường bên ngoài. Mức độ bảo vệ cần thiết trong trường hợp "
               "này như sau: đối với sử dụng chung, cần IP54 khi thiết bị chứa "
               "các bộ phận mang điện trần, giảm xuống IP44 khi tất cả các bộ "
               "phận mang điện bên trong được che phủ bằng vật liệu cách "
               "điện, vật liệu đóng gói hoặc biện pháp bảo vệ tương tự; đối "
               "với thiết bị dự định lắp đặt ở những khu vực mà nguy cơ xâm "
               "nhập của vật thể rắn lạ hoặc chất lỏng đã được ngăn chặn bằng "
               "biện pháp khác, chẳng hạn như lắp đặt trong nhà trong môi "
               "trường sạch, mức bảo vệ do vỏ bọc cung cấp có thể giảm xuống "
               "IP4X đối với bộ phận mang điện trần và IP2X khi các bộ phận "
               "mang điện được che phủ bằng vật liệu cách điện, vật liệu đóng "
               "gói hoặc biện pháp bảo vệ tương tự. (X cho biết không có yêu "
               "cầu cơ bản về loại trừ chất lỏng)."))
    b.append(p("Tiêu chuẩn phù hợp để xác định xếp hạng IP là BS 5490¹³ trong "
               "trường hợp chung và BS 4999¹⁴ đối với máy quay. Những vỏ bọc "
               "này chỉ cần thiết khi có thể xâm nhập và điều đó có thể tạo "
               "ra tình huống có khả năng gây đánh lửa. Trong những trường hợp "
               "như nhiệt kế điện trở, cảm biến biến dạng và các thiết bị "
               "năng lượng thấp tương tự, khi có thể loại trừ tia lửa có khả "
               "năng gây đánh lửa, thì các mức vỏ bọc nêu trên không áp dụng "
               "và, tương tự, trong một số trường hợp được xác định trong "
               "nguyên lý bảo vệ thì yêu cầu mức bảo vệ cao hơn. Cũng cần "
               "nhấn mạnh rằng xếp hạng IP là mức cần thiết để bảo đảm hoạt "
               "động đúng của thiết bị, chứ không chỉ là mức cần thiết để "
               "tránh các tình huống có khả năng gây đánh lửa."))
    b.append(h4("14.3.2 Độ bền cơ học", "14.3.2 Mechanical strength"))
    b.append(p("Vỏ bọc của thiết bị được yêu cầu phải chống được hư hỏng cơ "
               "học và điều này được chứng minh bằng cách cho thiết bị chịu "
               "thử nghiệm va đập cơ học được mô tả trong Chương 8. Tuy nhiên, "
               "do khả năng hiện diện của bầu khí quyển nổ ở Vùng 2 thấp hơn "
               "và khả năng rằng một quy trình kiểm tra hợp lý có thể phát "
               "hiện hư hỏng trước khi bầu khí quyển đó xuất hiện, thử nghiệm "
               "độ bền được giảm xuống mức số liệu cho trong Bảng 14.1. Điều "
               "đó rõ ràng có nghĩa là trong nhiều trường hợp thiết bị thử va "
               "đập tiêu chuẩn ở 1 Kg sẽ cần độ cao 20cms trở xuống, khiến "
               "thử nghiệm khó xác định hơn. Vì lý do này, thử nghiệm có thể "
               "được tiến hành với thiết bị thử có khối lượng giảm theo Bảng "
               "14.2."))
    b.append(note("<b>Ghi chú về các nét in đặc biệt trong 14.3.2.</b> Bản in "
                  "viết ‘1 Kg’ (K viết hoa), ‘20cms’ (không có dấu cách) và "
                  "‘the test may, be carried out’ với dấu phẩy thừa sau "
                  "‘may’. Cả ba được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt nêu theo nghĩa định."))
    b.append(p("Thử nghiệm này có thể làm sứt mẻ thiết bị hoặc gây biến dạng "
               "vỏ bọc nhưng trong cả hai trường hợp, mức độ bảo vệ (xếp hạng "
               "IP) của vỏ bọc cũng như hoạt động đúng của thiết bị không "
               "được bị ảnh hưởng bất lợi."))

    # E5 (printed p.431), Table 14.1.
    b.append(table(T1.HEAD141_VI, T1.ROWS141_VI, T1.CAPTION141_VI))
    b.append(note(T1.NOTE141_VI))

    # F1 (printed p.432), Table 14.2.
    b.append(table(T1.HEAD142_VI, T1.ROWS142_VI, T1.CAPTION142_VI))
    b.append(note(T1.NOTE142_VI))

    # F2-G2 (printed pp.432-433), heading 14.3.3 and its subheadings.
    b.append(h4("14.3.3 Dây dẫn và các kết nối bên trong",
                "14.3.3 Wiring and internal connections"))
    b.append(h4("Dây dẫn", "Wiring"))
    b.append(p("Dây dẫn bên trong của thiết bị Loại ‘N’ chỉ cần đáp ứng các "
               "yêu cầu đối với thiết bị công nghiệp thông thường, ngoại trừ "
               "việc cần cẩn trọng thêm để tránh hư hỏng do cọ xát với các "
               "bộ phận kim loại hoặc cạnh sắc. Điều này thường đạt được bằng "
               "cách cố định dây dẫn bên tại nơi tiếp xúc với các bộ phận khác "
               "của thiết bị để ngăn chuyển động và hư hỏng, đồng thời bảo "
               "đảm không có cạnh sắc bên trong thiết bị."))
    b.append(h4("Các kết nối bên trong", "Internal connections"))
    b.append(p("Dây dẫn có thể được nối vào các linh kiện và bộ phận kim loại "
               "khác bằng các phương pháp sau, tất cả đều được coi là không "
               "phát sinh tia lửa:"))
    b.append(ol([
        "các nối vặn hoặc nối bulông, kể cả vít kẹp, khi dây dẫn không bị hư "
        "hỏng bởi vít, bulông hoặc phương pháp nối;",
        "các nối ép (crimped);",
        "hàn thiếc;",
        "hàn cứng (brazing);",
        "hàn (welding);",
        "đầu nối dây dạng ép, trong đó kết nối được thực hiện bằng cách đưa "
        "dây vào giữa hai mảnh kim loại được lò xo ép lại và tạo áp lực lên "
        "dây dẫn đã đưa vào, ngăn không cho dây dịch chuyển;",
        "quấn máy dây dẫn quanh một chốt (thường được gọi là quấn kiểu súng) "
        "nhưng trong trường hợp này kỹ thuật chỉ giới hạn ở dây dẫn có dòng "
        "điện không vượt quá 1 A khi vận hành bình thường;",
        "phích cắm và ổ cắm, với điều kiện việc tách chúng yêu cầu tác dụng "
        "một lực ít nhất 15N và chúng được bố trí sao cho không thể cắm sai "
        "hoặc cắm sai được nhận biết rõ bằng một hình thức sắp xếp hoặc đánh "
        "dấu nào đó.",
    ]))
    b.append(note("<b>Ghi chú về ‘1 A’ và ‘15N’.</b> Khoản 7 in ‘1 A or less’ "
                  "có dấu cách giữa số và đơn vị, còn khoản 8 in ‘a force of "
                  "at least 15N’ không có dấu cách. Cả hai hình thức in đều "
                  "được giữ nguyên trong bản tiếng Anh."))
    b.append(p("Mọi hình thức kết nối khác và mọi phích cắm và ổ cắm không "
               "đáp ứng các điều nêu trên phải được coi là bình thường phát "
               "sinh tia lửa."))

    # G3-G8 (printed p.433), heading 14.3.4.
    b.append(h4("14.3.4 Phương tiện kết nối bên ngoài",
                "14.3.4 External connection facilities"))
    b.append(p("Đó thường là phích cắm và ổ cắm hoặc các cọc đấu dây, trừ khi "
               "thiết bị được trang bị dây dẫn rời (cáp nối liền vĩnh viễn)."))
    b.append(p("Bên cạnh các yêu cầu đối với phích cắm và ổ cắm bên trong, "
               "các yêu cầu đối với kết nối bên ngoài cần được bố trí sao cho "
               "tia lửa khó có thể xuất hiện do việc ngắt điện áp không chủ "
               "ý. Có thể đạt được điều này bằng cách liên khóa chúng để xảy "
               "ra sự cô lập nếu cố tách khi tổ hợp còn có điện, hoặc bằng "
               "cách giữ chúng lại với nhau bằng các chi tiết bắt chặt kèm "
               "nhãn cảnh báo quy định phải cô lập trước khi tách. Điều quan "
               "trọng là bộ phận cố định của tổ hợp phích cắm và ổ cắm không "
               "làm ảnh hưởng bất lợi đến mức độ bảo vệ (IP) của vỏ bọc khi "
               "bộ phận di động đã được tháo ra, và không để bụi, chất lỏng "
               "hay vật lạ tích tụ khi phích cắm và ổ cắm bị tách ra. Điều "
               "này nhiều khả năng là vấn đề đối với ổ cắm, nơi sự tích tụ "
               "sẽ không dễ thấy."))
    b.append(p("Cọc đấu dây dùng để kết nối bên ngoài cần đáp ứng các yêu cầu "
               "tương tự như cọc dùng cho các loại bảo vệ Vùng 1 (xem Chương "
               "8 và Chương 12), nhưng trong trường hợp này, độ chắc chắn của "
               "cọc đấu dây có thể chỉ cần đạt được bằng ma sát."))
    b.append(p("Cáp có thể đi vào vỏ bọc của thiết bị Loại ‘N’ qua các đầu nối "
               "cáp hoặc ống dẫn, nhưng trong cả hai trường hợp mức độ bảo vệ "
               "(IP) của vỏ bọc phải được duy trì. Điều này đặc biệt đúng khi "
               "dùng ống dẫn, vì cần dùng hộp chặn để bịt kín đầu ống dẫn. "
               "Trường hợp dùng cáp, các loại đầu nối cáp thông thường dùng "
               "ngoài trời sẽ thường đủ. Điều quan trọng là đối với đầu nối "
               "cáp, đầu nối phải kẹp chặt cơ học cáp để ngăn ứng suất tác "
               "dụng lên cọc đấu dây."))
    b.append(p("Các loại cáp thường dùng sẽ là cáp cách điện và vỏ bọc bằng "
               "polyetylen hoặc PVC. Vì lý do này, thiết bị sinh nhiệt có thể "
               "làm nhiệt độ cáp vượt quá nhiệt độ vận hành tối đa. Do đó, khi "
               "nhiệt độ tại vị trí lắp đầu nối cáp vượt quá 70 °C, hoặc "
               "nhiệt độ tại vị trí dây dẫn tách ra bên trong vỏ bọc vượt quá "
               "80°C, cần đưa ra cảnh báo (thường bằng nhãn) cho người lắp "
               "đặt để họ lựa chọn cáp phù hợp."))
    b.append(note("<b>Ghi chú về ‘70 °C’ và ‘80°C’.</b> Bản in viết nhiệt độ "
                  "tại đầu nối là ‘70 °C’ (có dấu cách trước °C) nhưng nhiệt "
                  "độ tại điểm dây dẫn tách ra là ‘80°C’ (không có dấu cách). "
                  "Sự không nhất quán này được giữ nguyên trong bản tiếng "
                  "Anh; bản tiếng Việt nêu theo nghĩa định."))

    # G9-H1 (printed pp.433-434), heading 14.3.5, sentence interrupted by
    # Table 14.3.
    b.append(h4("14.3.5 Cách điện và phân tách dây dẫn",
                "14.3.5 Conductor insulation and separation"))
    b.append(p("Như đối với an toàn tăng cường ‘e’ (Chương 12) và an toàn nội "
               "tại ‘i’ (Chương 13), cũng có các yêu cầu về phân tách các dây "
               "dẫn không cách điện trong không khí (khoảng hở), phân tách các "
               "dây dẫn không cách điện trên bề mặt vật liệu cách điện (độ rò "
               "trong không khí), phân tách các dây dẫn không cách điện trên "
               "bề mặt đã phủ vecni (độ rò dưới lớp phủ), và phân tách qua vật "
               "liệu đóng gói, khi việc phân tách này bị phá vỡ có thể tạo ra "
               "tia lửa gây cháy tại điểm phá vỡ hoặc ở nơi khác. Các khoảng "
               "cách tối thiểu liên quan được cho trong Bảng 14.3. Cần lưu ý "
               "rằng"))

    # H2 (printed p.434), Table 14.3.
    b.append(table(T1.HEAD143_VI, T1.ROWS143_VI, T1.CAPTION143_VI))
    b.append(note(T1.NOTE143_VI))

    # I1-I10+J1-J9 (printed pp.435-436): resumption, definitions, tests.
    b.append(p("không có yêu cầu nào về phân tách qua cách điện rắn nhưng, "
               "khi thiếu các yêu cầu này, nên dùng vật liệu cách điện đáp "
               "ứng khoảng cách phân tách qua cách điện rắn. Bảng 14.3 đi theo "
               "cách tiếp cận tương tự như các bảng trong các nguyên lý bảo "
               "vệ ‘e’ và ‘i’, được rút ra từ công việc của IEC về khoảng "
               "cách phân tách tối thiểu trong các điều kiện môi trường khác "
               "nhau. Tuy nhiên, bảng được rút ra bởi các ủy ban khác nhau vào "
               "những thời điểm khác nhau và dù các tiêu chí rút ra cơ bản "
               "giống nhau, sự khác biệt là không thể tránh khỏi. Những khác "
               "biệt này không ảnh hưởng bất lợi đến an toàn, vì chúng là "
               "những thay đổi nhỏ; và việc so sánh chúng với các bảng tương "
               "ứng của các nguyên lý bảo vệ khác cho thấy rõ chúng lớn hơn "
               "một phần ba so với các khoảng cách kia. Điều đó là đủ, xét "
               "rằng con số này đại diện cho một mức lỗi đếm được trong an "
               "toàn nội tại (chương 13), vốn đủ cho Vùng 2 theo rủi ro thấp "
               "hơn về sự hiện diện của bầu khí quyển nổ."))
    b.append(note("<b>Ghi chú về cụm từ in bất thường.</b> Bản in viết ‘they "
                  "are in excess of one third of the other distances’ và ‘(chapter "
                  "13)’ với chữ ‘c’ thường; cả hai được giữ nguyên trong bản "
                  "tiếng Anh, còn bản tiếng Việt nêu theo nghĩa so sánh định."))
    b.append(p("Bảng trong Tiêu chuẩn dành cho Loại ‘N’ (BS 6941) khác với "
               "các bảng trong các Tiêu chuẩn khác ở chỗ dùng các thuật ngữ "
               "khác, nhưng điều đó chỉ là do một ủy ban khác đã xây dựng các "
               "yêu cầu chứ không phải do có bất kỳ khác biệt nào về ý định. "
               "Ý nghĩa thực tế của các thuật ngữ như sau."))
    b.append(h4("Độ rò", "Creepage"))
    b.append(p("Độ rò là khoảng cách rò trên bề mặt cách điện không được bảo "
               "vệ và trong các tài liệu khác được gọi là ‘khoảng cách rò "
               "trong không khí’."))
    b.append(h4("Khoảng hở và phân tách trong không khí",
                "Clearance and separation in air"))
    b.append(p("Khoảng hở và phân tách trong không khí là khoảng cách trực "
               "tiếp ngắn nhất trong không khí giữa hai bộ phận dẫn điện "
               "không được cách điện và ở nơi khác được gọi là ‘khoảng hở’."))
    b.append(h4("Phân tách – kín", "Separation – sealed"))
    b.append(p("Đây là khoảng cách tối thiểu trên bề mặt cách điện mà bề mặt "
               "và các bộ phận dẫn điện được phủ vecni hoặc tương tự, và được "
               "gọi ở nơi khác là ‘độ rò dưới lớp phủ’. Lớp phủ trong trường "
               "hợp này được gọi là lớp phủ đồng hình và BS 5917¹⁶ được viện "
               "dẫn là tiêu chuẩn kiểm soát nó. Tuy nhiên, tham chiếu đến IEC "
               "79-15¹¹ cho thấy ý định, vì văn bản này quy định dùng một lớp "
               "môi trường đông cứng mềm hoặc hai lớp sơn mài hay vecni. Ý "
               "định là bảo đảm lớp phủ hoàn chỉnh, không có lỗ kim. Khi các "
               "bộ phận dẫn điện không cách điện thoát ra khỏi lớp phủ, thì "
               "như ở nơi khác, số liệu độ rò trong không khí được áp dụng và "
               "cả vật liệu phủ lẫn lớp cách điện nâng đỡ đều cần có CTI cần "
               "thiết."))
    b.append(h4("Phân tách – đóng gói", "Separation – encapsulated"))
    b.append(p("Đây là khoảng cách giữa hai bộ phận dẫn điện không cách điện "
               "xuyên qua lớp vật liệu đóng gói và ở nơi khác được gọi là "
               "‘khoảng cách phân tách qua hợp chất đúc’. Yêu cầu ở đây là "
               "vật liệu đóng gói phải bao quanh cả hai bộ phận dẫn điện với "
               "độ sâu ít nhất 0.4mm. Tuy nhiên, con số 0.4mm chỉ quan trọng "
               "đến 500V, vì trên điện áp này yêu cầu phân tách là 0.9mm và "
               "đường từ cả hai bộ phận dẫn điện tới bề mặt vật liệu đóng gói "
               "chỉ là 0.8mm. Trong trường hợp này không thể cộng thêm độ rò "
               "trên bề mặt vật liệu đóng gói, vì trong Loại ‘N’ không có "
               "phương pháp quy định cho việc đó và độ sâu của vật liệu đóng "
               "gói sẽ cần được tăng lên để đạt được sự phân tách cần thiết. "
               "Không có quy định giảm thêm cụ thể nào cho sự phân tách qua "
               "cách điện rắn, vì vậy các yêu cầu này cũng áp dụng cho cách "
               "điện rắn."))
    b.append(h4("Thử nghiệm cách điện giữa các dây dẫn",
                "Insulation tests between conductors"))
    b.append(p("Các yêu cầu của Bảng 14.3 không quá nặng nề, vì chúng có thể "
               "được miễn nếu cách điện giữa hai dây dẫn (ví dụ bảng mạch in "
               "nâng đỡ, vật liệu đóng gói, vật liệu cách điện, v.v.) vượt "
               "qua thử nghiệm độ bền điện sau đây. Một điện áp có giá trị "
               "tối thiểu (1500 + 2U) V rms (xoay chiều hoặc một chiều tùy "
               "theo trường hợp) phải được đặt giữa hai bộ phận dẫn điện "
               "trong một phút mà không làm phá vỡ cách điện."))
    b.append(note("<b>Ghi chú về lỗi in trong ví dụ.</b> Bản in viết ‘the "
                  "encapsulant the insulation, etc.’ – thiếu từ nối trước ‘the "
                  "insulation’. Cụm này được giữ nguyên trong bản tiếng Anh; "
                  "bản tiếng Việt nêu theo nghĩa định."))
    b.append(p("Có thể áp dụng điện áp này bằng cách tăng điện áp tới mức cần "
               "thiết trong 10 giây rồi giữ ở mức đó trong một phút. Mọi dòng "
               "rò phải giữ ổn định hoặc giảm trong khi thử nghiệm. Sự tăng "
               "lên được coi là dấu hiệu báo trước của hỏng cách điện."))
    b.append(p("Đây là thử nghiệm thường quy và phải được áp dụng cho mọi "
               "thiết bị khi không đáp ứng các yêu cầu của Bảng 14.3. Trong "
               "thiết bị điện tử, các linh kiện như bóng bán dẫn và mạch tích "
               "hợp có thể bị hỏng do thử nghiệm thì không cần lắp vào thời "
               "điểm thử nghiệm, vì thử nghiệm nhằm chứng minh riêng tính toàn "
               "vẹn của cách điện."))
    b.append(h4("Thử nghiệm cách điện giữa các dây dẫn và khung hoặc đất",
                "Insulation tests between conductors and the frame or earth"))
    b.append(p("Bên cạnh đó, khi thiết bị không được nối với khung hoặc đất, "
               "trong mọi trường hợp – kể cả khi đã đáp ứng các yêu cầu của "
               "Bảng 14.3 – cách điện giữa các mạch điện và đất phải đáp ứng "
               "các thử nghiệm điện áp sau đây."))
    b.append(p("Thứ nhất, khi cả điện áp nguồn cấp cho thiết bị và mọi điện áp "
               "bên trong đều vượt quá 90 V peak, cách điện hoặc khoảng cách "
               "phân tách giữa đất hoặc khung và các mạch điện không được phá "
               "vỡ khi một điện áp thử (1000 + 2U)Vrms xoay chiều hoặc một "
               "chiều tùy theo trường hợp được đặt giữa chúng, như trước. Các "
               "tụ điện triệt nhiễu RF phải được đưa vào thử nghiệm và dòng "
               "điện của chúng, nếu thử nghiệm dùng điện áp xoay chiều, phải "
               "được tính đến khi xác định sự phá vỡ."))
    b.append(note("<b>Ghi chú về ‘90 V peak’ và ‘90V peak’.</b> Thử nghiệm "
                  "điện áp cao hơn ở đoạn trên in ‘90 V peak’ (có dấu cách), "
                  "còn thử nghiệm điện áp giảm ở đoạn sau in ‘90V peak’ (không "
                  "có dấu cách). Cả hai hình thức được giữ nguyên trong bản "
                  "tiếng Anh."))
    b.append(p("Thứ hai, khi điện áp nguồn cấp cho thiết bị không vượt quá "
               "90V peak và tương tự các điện áp bên trong không vượt quá giá "
               "trị đó (không có quy định tăng điện áp bên trong), điện áp thử "
               "giữa đất hoặc khung có thể giảm xuống 500Vrms xoay chiều hoặc "
               "một chiều tùy theo trường hợp."))
    # The sentence continuing onto printed p.437 belongs to writer B; stop here.
    return "".join(b)


def body_en():
    b = []

    # A0-A2 (printed p.427). The shell owns the chapter h2; the module owns
    # the printed standard subtitle lines and the two opening paragraphs.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("<b>(BS 6941 (1988))<br>(IEC 79-15 (1987))</b>"))
    b.append(p("Unlike the protection concepts already described, protection "
               "concept (type of protection) ‘N’ is intended for installation "
               "only in Zone 2 areas. In such areas the risk of an explosive "
               "atmosphere occurring is so much less than in Zone 0 and 1 "
               "that historically it has been considered that the installation "
               "of ‘high quality’ industrial equipment, which does not spark "
               "or produce ignition-capable hot surfaces in normal operation "
               "is sufficient for this risk. The use of the term ‘high "
               "quality’ did not imply special equipment but was used to "
               "ensure that installers did not cut corners and use equipment "
               "not really intended for the industrial environment. "
               "Historically, any non-sparking equipment which was "
               "specifically designed for the industrial environment and had "
               "no special features demanding higher than the normal level of "
               "maintenance was acceptable. For equipment which did spark or "
               "become hot enough to cause ignition in normal operation, the "
               "Zone 1 compatible protection concepts would, have to be used."))
    b.append(note("<b>Source quirks in the opening paragraph.</b> ‘historically’ "
                  "occurs twice, and the printed sentence ends ‘the Zone 1 "
                  "compatible protection concepts would, have to be used’ with "
                  "a stray comma after ‘would’. Both printed forms are "
                  "retained here; the Vietnamese states the intended meaning."))
    b.append(p("This situation continued until 1972 when a British Standard "
               "which, for the first time introduced the possibility of "
               "apparatus which could create arcs or sparks, was published. "
               "This Standard suggested several methods of avoiding ignition "
               "from such sparking based upon those approaches used for Zone "
               "1, but with lower security to reflect the lower possibility "
               "of the presence of an explosive atmosphere."))

    # A3-A4+B1-C6 (printed pp.427-429), heading 14.1.
    b.append(h3("14.1 The situation in respect of standardization",
                "14.1 The situation in respect of standardization"))
    b.append(p("The approach to selection and use of apparatus for Zone 2 was "
               "described initially in BS/CP1003, Part 3¹ (use) and, in BS "
               "4137² which was produced to give detail upon selection of non "
               "sparking-industrial apparatus for Zone 2 use. This approach "
               "has continued up to the present day and the use of ‘selected "
               "industrial apparatus’ is still recognized but now in BS 5345, "
               "Part 1³ there is a specification of the required qualities of "
               "those who select such apparatus and these are: first, that "
               "they must be familiar with the requirements of any relevant "
               "Standards and Codes of Practice including their "
               "interpretations. (This requirement is clearly intended to "
               "ensure that they are to a degree expert in the construction "
               "and installation of explosion-protected apparatus); second, "
               "they must have access to all the necessary information so "
               "that they can carry out the selection. (This will mean that "
               "they will need to know the detail of the apparatus design and "
               "intended use); and third, that if any tests are necessary "
               "these must be done using test apparatus and procedures "
               "similar to those used by recognized third-party test "
               "laboratories. (This means that the facilities and knowledge "
               "available to those who select apparatus must be similar to "
               "what is available to ‘Notified Bodies’ under Directive "
               "76/117/EEC⁴ or 94/9/EC⁵)."))
    b.append(p("The above requirements make it quite clear that the selection "
               "of industrial equipment on the basis of it being non-sparking "
               "and not becoming hot enough to cause ignition is not, and "
               "never was, intended to be a relatively relaxed approach used "
               "by all installers, but rather a relatively formal approach "
               "and, while used by other than third party "
               "certification/approval bodies, was intended to include the "
               "level of detail similar to that which would be involved if a "
               "third party certification/approval body had been used."))
    b.append(p("The selection situation was never fully satisfactory and led "
               "to the position where industry sought some form of third "
               "party approval for the apparatus which they intended to use "
               "and, not surprisingly, turned for this to HM Factory "
               "Inspectorate, the body which regulated industry other than "
               "coalmining. Because there was no specific Standard and thus "
               "no detailed set of rules to which to approve such apparatus, "
               "the Factory Inspectorate could not approve apparatus but could "
               "identify that it had no sparking contacts, no hot surfaces "
               "and no other peculiarities which would make it unacceptable "
               "in the light of knowledge available at the time. This was "
               "done by the issue of a ‘Letter of no objection’ which was "
               "taken as approval, but was not in fact that. It was what it "
               "said – an identification that the Factory Inspectorate knew "
               "of no reason why it should not be installed in Zone 2. The "
               "letter would, unlike most certificates which continue in "
               "validity even after requirements have changed providing there "
               "is no evidence of imminent danger, become invalid if an "
               "increase in knowledge identified problems."))
    b.append(p("The situation, apart from the UK peculiarities of the ‘Letter "
               "of no objection’, was almost identical to the Zone 2 situation "
               "in most other developed counties - Germany, for example, "
               "having selection requirements in their installation document "
               "VDE 0165, and the United States of America in Article 500 of "
               "the National Electrical Code."))
    b.append(note("<b>Source quirk: ‘counties’.</b> The print reads ‘most other "
                  "developed counties’ where ‘countries’ is meant; the printed "
                  "word is retained here while the Vietnamese follows the "
                  "intended meaning."))
    b.append(p("As industry developed there was a considerable demand for "
               "sparking Zone 2 apparatus as it was recognized that the Zones "
               "0 and 1 requirements, which had hitherto been applied, were "
               "overly restrictive for Zone 2 and, as in all other fields, "
               "the advent of the transistor had introduced much more "
               "complexity into the field causing much more hazardous area "
               "mounted apparatus. In addition, there was an increasing demand "
               "for definitive constructional requirements for Zone 2 apparatus "
               "to remove the ‘judgement’ element present in the selection "
               "procedures. This led to the publication of the first British "
               "Standard for the production of apparatus for Zone 2 which was "
               "called ‘Apparatus with Type of Protection ’N’ and was BS "
               "4683, Part 3 (1972)⁶. This Standard began the process of "
               "translating the criteria for apparatus selection into "
               "requirements for construction, and opened the door for full "
               "third-party certification."))
    b.append(p("International interest in construction requirements for "
               "apparatus for Zone 2 increased during this period also and an "
               "IEC⁷ committee was formed to produce an International Standard "
               "for this type of apparatus using the international coding ‘n’ "
               "(the UK Standard used ‘N’ to show that the protection concept "
               "was a national concept and not an international one). The IEC "
               "committee, not surprisingly as this was the first attempt to "
               "internationalize a situation which had been national until "
               "this time and included a wide range of national ideas not "
               "accepted or even understood by some other countries, had "
               "considerable difficulties in coming to an agreement."))
    b.append(p("At the same time the limitations of BS 4683, Part 3, in the "
               "light of further progress, were becoming evident and there "
               "was considerable support for replacing it by a more detailed "
               "Standard which would include all of the ideas in the IEC⁷ "
               "committee with which the UK agreed (which were all essentially "
               "the same except for the Swiss developed restricted breathing "
               "concept). This Standard was published in 1988 as BS 6941⁸. "
               "This Standard also addressed particular types of equipment, "
               "such as Type ‘N’ electric motors (addressed also in BS 5000, "
               "Part 16 (1972)⁹) and luminaires with Type ‘N’ protection. "
               "(Addressed also in BS 4533, Part 2, Section 2.1 (1976)¹⁰)."))
    b.append(p("The IEC committee ultimately produced their document as IEC "
               "79-15 (1987)¹¹ but, because of the divergence of opinion in the "
               "IEC⁷ the document was produced as a report rather than a "
               "Standard. The fact, however, that BS 6941⁸ followed almost "
               "exactly IEC 79-15¹¹ text (with the exception of the restricted "
               "breathing concept) makes the use of that Standard a valid "
               "basic approach for the technical requirements of type of "
               "protection ‘N’."))
    b.append(p("The IEC and CENELEC¹² are now producing a Standard which will "
               "be both European and international, based upon IEC 79-15¹¹ "
               "which adds further weight to the requirements in BS 6941⁸."))
    b.append(p("Notwithstanding the fact that a detailed construction standard "
               "now exists, the flexibility of selecting apparatus for Zone 2 "
               "with no absolute requirement for third-party approval still "
               "remains both nationally in the UK and in Directive 94/9/EC⁵ "
               "in the EU. The rules against which this selection takes place, "
               "however, will now by those exist in BS 6941⁸ and its European "
               "and international successor."))
    b.append(note("<b>Source quirk at the end of 14.1.</b> The print reads "
                  "‘The rules against which this selection takes place, "
                  "however, will now by those exist in BS 6941⁸ and its "
                  "European and international successor.’; the words ‘by "
                  "those exist’ are kept as printed while the Vietnamese "
                  "states the intended meaning."))

    # C7-C8+D1-D3 (printed pp.429-430), heading 14.2.
    b.append(h3("14.2 Basic requirements of the protection concept",
                "14.2 Basic requirements of the protection concept"))
    b.append(p("The definition of Type ‘N’ (n) apparatus is that it will not "
               "be capable of causing the ignition of an explosive atmosphere "
               "in normal operation and that a fault making it so capable is "
               "unlikely to occur. Now that sparking is accepted as part of "
               "the protection concept, this basic definition may be expanded "
               "to cover this as follows: first, the apparatus must not "
               "produce an arc or spark in normal operation which can cause "
               "ignition of an explosive atmosphere, unless that arc or spark "
               "is prevented from so doing either by current limitation or "
               "by some other means which are defined as being capable of "
               "prevention of such ignition; and second, that the apparatus "
               "must not produce a surface temperature capable of igniting an "
               "explosive atmosphere, unless that surface temperature is "
               "prevented from causing such an ignition by containment or "
               "some other suitable means."))
    b.append(p("While the ‘General Requirements’ identified in Chapter 8 do "
               "not, in general, apply to apparatus of Type ‘N’, some are "
               "appropriate - for example, sub-grouping into IIA, IIB and IIC "
               "which is carried out for sparking apparatus. Likewise, the "
               "method of surface temperature classification used in other "
               "protection concepts is also appropriate to Type ‘N apparatus."))
    b.append(note("<b>Source quirk: unclosed quotation mark.</b> The sentence "
                  "ends ‘also appropriate to Type ‘N apparatus.’ with no "
                  "closing quotation mark after ‘N’; the earlier title ‘Apparatus "
                  "with Type of Protection ’N’ and was BS 4683, Part 3 (1972)⁶’ "
                  "is also printed with unusual quoting. Both are retained as "
                  "printed."))
    b.append(p("The apparatus is also expected, in common with other "
               "protected apparatus, to have additional features where it is "
               "used in environments which are more onerous than normal "
               "outdoor environments, such as those where solvent vapours may "
               "occur and where plastics enclosures may not be appropriate. "
               "These additional requirements are, as in the case of other "
               "protection concepts, agreed in particular cases in relation "
               "to particular risks, such as additional exposure to mechanical "
               "damage or chemical damage, unusually moist environments, etc.."))
    b.append(note("<b>Source quirk: ‘etc..’.</b> The print has two full stops "
                  "in ‘etc..’, retained verbatim here; the Vietnamese uses the "
                  "normal abbreviation."))

    # D4-E4 (printed pp.430-431), headings 14.3 and 14.3.1-14.3.2.
    b.append(h3("14.3 General constructional requirements",
                "14.3 General constructional requirements"))
    b.append(p("The general constructional requirements are those which apply "
               "to all types of Type ‘N’ apparatus and address environmental "
               "protection, mechanical strength and electrical connections."))
    b.append(h4("14.3.1 Environmental protection",
                "14.3.1 Environmental protection"))
    b.append(p("Because Type ‘N’ apparatus is assumed to include electrical "
               "circuits which can contain incendive energies, the entry of "
               "the environment is assumed to be able to cause internal faults "
               "which would allow those energies to be released. For this "
               "reason, as with other forms of protection exhibiting this "
               "phenomenon, the enclosure of the apparatus is required to "
               "provide a suitable degree of protection against entry of "
               "liquids and solids present in the external environment. The "
               "degree of protection necessary in this regard is as follows: "
               "in the case of general use, IP54 is necessary where the "
               "apparatus contains bare live parts reducing to IP44 where all "
               "internal live parts are covered with insulation, encapsulant "
               "or similar protection; in the case of equipment intended for "
               "installation in areas where the risk of entry of solid foreign "
               "bodies or liquids is prevented by other means, such as indoor "
               "installation in a clean environment, the protection afforded "
               "by the enclosure can be reduced to IP4X for bare live parts "
               "reducing to IP2X where live parts are covered by insulation, "
               "encapsulant or similar protection. (The X indicates there is "
               "no basic requirement for exclusion of liquids)."))
    b.append(p("The standards appropriate to the determination of IP rating "
               "are BS 5490¹³ in the general case, and BS 4999¹⁴ in the case "
               "of rotating machines. These enclosures are only necessary "
               "where ingress is possible and could cause an ignition-capable "
               "situation. In cases such as resistance thermometers, strain "
               "gauges and similar low energy devices where ignition-capable "
               "sparking can be precluded, the above degrees of enclosure do "
               "not apply and, likewise, in some cases identified in the "
               "protection concept a higher degree of protection is required. "
               "It should also be stressed that the IP-rating is that which "
               "is necessary to ensure the correct operation of the apparatus "
               "and not only that necessary to avoid ignition-capable "
               "situations."))
    b.append(h4("14.3.2 Mechanical strength", "14.3.2 Mechanical strength"))
    b.append(p("The apparatus enclosure is required to be proof against "
               "mechanical damage and this is shown by subjecting it to the "
               "mechanical impact test described in Chapter 8. However, due "
               "to the reduced likelihood of the presence of an explosive "
               "atmosphere in Zone 2 and the likelihood that a reasonable "
               "inspection routine is likely to identify damage before such "
               "an atmosphere occurs, the strength test is reduced to the "
               "figures given in Table 14.1. These would clearly mean that in "
               "many cases the Standard impact device at 1 Kg would require "
               "a height of 20cms or less which would make the test less easy "
               "to define. For this reason the test may, be carried out with "
               "reduced mass testing devices in accordance with Table 14.2."))
    b.append(note("<b>Source quirks in 14.3.2.</b> The print has ‘1 Kg’ with a "
                  "capital K, ‘20cms’ with no space, and ‘the test may, be "
                  "carried out’ with a stray comma after ‘may’. All three "
                  "printed forms are retained here."))
    b.append(p("This test may chip the apparatus or may cause deformation of "
               "the enclosure but in either case neither the degree of "
               "protection (IP-rating) of the enclosure nor the correct "
               "operation of the apparatus must be adversely affected."))

    # E5 (printed p.431), Table 14.1.
    b.append(table(T1.HEAD141_EN, T1.ROWS141_EN, T1.CAPTION141_EN))
    b.append(note(T1.NOTE141_EN))

    # F1 (printed p.432), Table 14.2.
    b.append(table(T1.HEAD142_EN, T1.ROWS142_EN, T1.CAPTION142_EN))
    b.append(note(T1.NOTE142_EN))

    # F2-G2 (printed pp.432-433), heading 14.3.3 and its subheadings.
    b.append(h4("14.3.3 Wiring and internal connections",
                "14.3.3 Wiring and internal connections"))
    b.append(h4("Wiring", "Wiring"))
    b.append(p("The internal wiring of Type ‘N’ apparatus need only comply "
               "with the requirements for normal industrial apparatus except "
               "that additional care needs to be taken to avoid damage by "
               "rubbing against metallic parts or sharp edges. This is "
               "normally achieved by securing internal wiring where it comes "
               "into contact with other parts of the apparatus to prevent "
               "movement and damage, and ensure there are no sharp edges "
               "inside the apparatus."))
    b.append(h4("Internal connections", "Internal connections"))
    b.append(p("The wiring may be connected to components and other metallic "
               "parts by the following means all of which are considered as "
               "non-sparking:"))
    b.append(ol([
        "screwed or bolted connections including pinching screws where "
        "conductors are not damaged by the screws or bolts or connection "
        "method;",
        "crimped connections;",
        "soldering;",
        "brazing;",
        "welding;",
        "pressure-type wire connectors where connection is made by inserting "
        "the wire in between two pieces of metal which are sprung together "
        "and provide a pressure on the inserted conductor, preventing its "
        "movement;",
        "machine wrapping of conductors around a post (more normally known "
        "as gun wrapping) but in this case the technique is limited to "
        "conductors which carry 1 A or less in normal service;",
        "plugs and sockets, provided their separation requires the "
        "application of a force of at least 15N and they are either arranged "
        "so that incorrect connection is not possible or is obvious by some "
        "form of arrangement or identification.",
    ]))
    b.append(note("<b>Source quirks: ‘1 A’ and ‘15N’.</b> Item 7 prints ‘1 A "
                  "or less’ with a space between the numeral and the unit, "
                  "whereas item 8 prints ‘a force of at least 15N’ with no "
                  "space. Both printed forms are retained."))
    b.append(p("Other forms of connection and plugs and sockets not complying "
               "with the above must be considered as normally sparking."))

    # G3-G8 (printed p.433), heading 14.3.4.
    b.append(h4("14.3.4 External connection facilities",
                "14.3.4 External connection facilities"))
    b.append(p("These are normally plugs and sockets or terminals unless the "
               "apparatus is fitted with a flying lead (permanently connected "
               "cable)."))
    b.append(p("In addition to the requirements for internal plugs and sockets "
               "those for external connection need to be arranged so that "
               "sparking is unlikely to occur due to inadvertent energized "
               "separation. This can be achieved by interlocking them so that "
               "isolation occurs if separation is attempted while the "
               "combination is energized, or by securing them together by "
               "fasteners with a warning label to specify pre-separation "
               "isolation. It is also important that the fixed part of the "
               "plug and socket combination does not adversely affect the "
               "degree of protection of the enclosure (IP) when the moveable "
               "part has been removed and that accumulations of dust, liquids "
               "and other foreign bodies do not occur while the plug and "
               "socket are separated. This is most likely to be a problem in "
               "relation to the socket where the accumulation will not be so "
               "obvious."))
    b.append(p("Terminals for external connection need to satisfy similar "
               "requirements to those used for Zone 1 types of protection "
               "(see Chapters 8 and 12) but, in this case, terminal security "
               "may be achieved by friction alone."))
    b.append(p("Cables can enter Type ‘N’ enclosure via cable glands or "
               "conduit but in either case the degree of protection (IP) of "
               "the enclosure must be maintained. This is particularly true "
               "where conduit is used as a stopper box needs to be used to "
               "seal the end of the conduit. In the case of cables the normal "
               "types of cable gland for outdoor use will usually be "
               "adequate. It is important that, in the case of cable glands, "
               "the gland provides mechanical clamping of the cable to "
               "prevent stress on the terminals."))
    b.append(p("The normal types of cable used will be polyethylene or PVC "
               "insulated and sheathed. For this reason, apparatus which "
               "generates heat could raise the cable temperature above its "
               "maximum operating temperature. For this reason where the "
               "temperature at the point of fitting of the gland exceeds 70 "
               "°C, or that at the point where the conductors separate inside "
               "the enclosure exceeds 80°C, a warning needs to be given "
               "(normally by a label) to the installer identifying this so "
               "that the cable can be chosen accordingly."))
    b.append(note("<b>Source quirk: ‘70 °C’ and ‘80°C’.</b> The gland "
                  "temperature is printed as ‘70 °C’ with a space but the "
                  "conductor-separation temperature as ‘80°C’ without one. "
                  "The inconsistency is retained here."))

    # G9-H1 (printed pp.433-434), heading 14.3.5, sentence interrupted by
    # Table 14.3.
    b.append(h4("14.3.5 Conductor insulation and separation",
                "14.3.5 Conductor insulation and separation"))
    b.append(p("As with increased safety ‘e’ (Chapter 12) and intrinsic safety "
               "‘i’ (Chapter 13) there are requirements for separation of "
               "uninsulated conductors in air (clearance), for uninsulated "
               "conductors across a surface of insulating material (creepage "
               "in air), separation of uninsulated conductors across varnished "
               "surfaces (creepage under coating), and separation distances "
               "through encapsulation where breakdown of such distances could "
               "produce incendive sparking either at the point of breakdown "
               "or elsewhere. The minimum distances in question are given in "
               "Table 14.3. It will be noted that"))

    # H2 (printed p.434), Table 14.3.
    b.append(table(T1.HEAD143_EN, T1.ROWS143_EN, T1.CAPTION143_EN))
    b.append(note(T1.NOTE143_EN))

    # I1-I10+J1-J9 (printed pp.435-436): resumption, definitions, tests.
    b.append(p("there are no requirements for separation through solid "
               "insulation but, in the absence of these, insulation satisfying "
               "the separation distance through solid insulation should be "
               "used. Table 14.3 follows a similar approach to those in "
               "protection concepts ‘e’ and ‘i’, being derived from IEC work "
               "on minimum separations in various environmental conditions. "
               "It was, however, derived by different committees at a "
               "different time and although the base derivation criteria "
               "were similar, differences will inevitably arise. These will "
               "not have an adverse effect on safety as they are minor "
               "variations and, a comparison of them with the tables "
               "associated with other protection concepts shows clearly that "
               "they are in excess of one third of the other distances. This "
               "is adequate bearing in mind that this figure represents a "
               "countable fault level in intrinsic safety (chapter 13) which "
               "is adequate for Zone 2 in the light of the reduced risk of the "
               "presence of an explosive atmosphere."))
    b.append(note("<b>Source quirk: ‘in excess of one third of the other "
                  "distances’.</b> The printed comparison is retained verbatim, "
                  "as is the lower-case ‘(chapter 13)’; the Vietnamese follows "
                  "the intended meaning."))
    b.append(p("The table in the Standard for Type ‘N’ (BS 6941) differs from "
               "those in other Standards in that it uses different terms but "
               "this is only because a different committee produced the "
               "requirements and not because there is any difference in the "
               "intent. The actual meaning of the terms is as follows."))
    b.append(h4("Creepage", "Creepage"))
    b.append(p("Creepage is the creepage distance across an unprotected "
               "insulating surface and is specified as ‘Creepage distance in "
               "air’ in other documents."))
    b.append(h4("Clearance and separation in air",
                "Clearance and separation in air"))
    b.append(p("Clearance and separation in air is the minimum direct distance "
               "in air between two uninsulated conductive parts and is "
               "elsewhere referred to as ‘clearance’."))
    b.append(h4("Separation – sealed", "Separation – sealed"))
    b.append(p("This is the minimum distance across an insulating surface "
               "where the surface and conductive parts are covered with "
               "varnish or similar and is referred to elsewhere as ‘creepage "
               "under coating’. The covering is in this case referred to as a "
               "conformal coating and BS 5917¹⁶ is referred to as controlling "
               "it. Reference to IEC 79-15¹¹, however, shows the intent in that "
               "it specifies the use of a single coat of a soft setting medium "
               "or two coats of lacquer or varnish. The intent is to ensure "
               "that the coating is complete without pinholes. Where "
               "uninsulated conductive parts exit the coating, as elsewhere, "
               "the creepage in air figures apply and both the coating "
               "material and the supporting insulation require to have the "
               "necessary CTI."))
    b.append(h4("Separation – encapsulated", "Separation – encapsulated"))
    b.append(p("This is the distance between two uninsulated conductive parts "
               "through encapsulation and is elsewhere known as ‘separation "
               "distance through casting compound’. The requirement here is "
               "for encapsulation to surround both conductive parts to a "
               "depth of at least 0.4mm. This 0.4mm figure is only of "
               "importance up to 500V, however, as above this distance the "
               "separation requirement is for 0.9mm and the path from both "
               "conductive parts to the surface of the encapsulant is only "
               "0.8mm. The creepage across the surface of the encapsulant "
               "cannot, in this case, be added as there is no method "
               "specified for this in Type ‘N’ and the encapsulant depth would "
               "need to be enhanced to achieve the necessary separation. "
               "There are no specific further reductions for separations "
               "through solid insulation and so these requirements will apply "
               "to solid insulation also."))
    b.append(h4("Insulation tests between conductors",
                "Insulation tests between conductors"))
    b.append(p("The requirements of Table 14.3 are not excessively onerous as "
               "they may be waived if the electrical insulation between the "
               "two conductors (e.g., the supporting printed circuit board, "
               "the encapsulant the insulation, etc.) passes the following "
               "electric strength test. A voltage of minimum value (1500 + "
               "2U) V rms (either ac or dc as appropriate) should be applied "
               "between the two conductive parts for one minute without "
               "breakdown of the insulation."))
    b.append(note("<b>Source quirk in the examples.</b> The print reads ‘the "
                  "encapsulant the insulation, etc.’ with no conjunction "
                  "before ‘the insulation’; the wording is retained verbatim."))
    b.append(p("This voltage may be applied by increasing the voltage to the "
               "necessary level in 10 seconds and then holding it for one "
               "minute. Any leakage current should remain stable or fall "
               "during the test. Increases are assumed to be a precursor of "
               "failure."))
    b.append(p("This test is a routine test and must be applied to all "
               "apparatus where the requirements of Table 14.3 are not "
               "complied with. In electronic apparatus items such as "
               "transistors and integrated circuits, which would be damaged "
               "by the test, need not be installed at the time of testing as "
               "the test is to prove the integrity of insulation alone."))
    b.append(h4("Insulation tests between conductors and the frame or earth",
                "Insulation tests between conductors and the frame or earth"))
    b.append(p("In addition, where the apparatus is not intended to be "
               "connected to the frame or earth, in all cases – even where the "
               "requirements of Table 14.3 are met – the insulation between "
               "the electrical circuits and earth must satisfy the following "
               "voltage tests."))
    b.append(p("First, where both the supply voltage to the apparatus and any "
               "internal voltages exceed 90 V peak the insulation or "
               "separation between earth or the frame and the electrical "
               "circuits must not break down when a test voltage of (1000 + "
               "2U)Vrms ac or dc as appropriate is applied between them, as "
               "before. RF-suppression capacitors must be included in this "
               "test and their current, if the test is ac, allowed for in the "
               "identification of breakdown."))
    b.append(note("<b>Source quirk: ‘90 V peak’ and ‘90V peak’.</b> The higher-"
                  "voltage test above prints ‘90 V peak’ with a space while "
                  "the reduced-voltage test below prints ‘90V peak’ without "
                  "one; both printed forms are preserved."))
    b.append(p("Second, where the supply voltage to the apparatus is not more "
               "than 90V peak and likewise the internal voltages do not "
               "exceed that figure (there are no internal voltage enhancement "
               "provisions) the earth or frame test voltage may be reduced to "
               "500Vrms ac or dc as appropriate."))
    # The sentence continuing onto printed p.437 belongs to writer B; stop here.
    return "".join(b)
