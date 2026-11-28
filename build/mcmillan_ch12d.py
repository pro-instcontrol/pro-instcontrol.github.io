# -*- coding: utf-8 -*-
"""Chapter 12, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 312-318 (PDF pp. 333-339, the last
page partial).

Covers the continuation of 12.3.1 "Terminal enclosures", 12.3.2 "Mains powered
luminaires", 12.3.3 "Caplamps" and 12.3.4 "Measuring instruments and
transformers". Figure 12.10 sits below the first paragraph of printed p. 312;
Figure 12.11 interrupts a paragraph on printed p. 314; Tables 12.5, 12.6 and
12.7 sit at their printed positions on printed pp. 315, 316 and 318. The chapter
shell owns the chapter h2, the printed references, the glossary, the
source-quirk note and the copyright.

Printed quirks are kept in the English text (the stray comma in 'inside the
terminal, box', the superscript footnote markers, '15°' and '50 °C', 'for as
starter', the spacing of 'type 'e'' and the capitalisation of the parenthetical
chapter references, the Ith/Idyn subscripts, 'an safety factor', 'sinusiodal'
and 'may exit a piece of apparatus') with bilingual notes; the Vietnamese
follows the intended meaning. This is an unofficial study translation. The
source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig12_c as FC
import mcmillan_tbl12_5_7 as T2


def body_vi():
    b = []

    # Printed p.312. Continuation of the 12.3.1 paragraph from the previous
    # module; the heading itself belongs to module C.
    b.append(p("tổng công suất bên trong có thể được tiêu tán bên trong vỏ bọc "
               "bởi tất cả các cọc nối và dây dẫn bên trong đó. Để xác định "
               "trường hợp xấu nhất cho bất kỳ hộp cọc nối nào, vì vậy cần xác "
               "định cọc nối xấu nhất dự định sử dụng trong đó. Đó là cọc nối "
               "đạt nhiệt độ bề mặt cực đại khi được nối với một dây dẫn có "
               "kích thước quy định lớn nhất của nó, dây này có, bên trong hộp "
               "cọc nối, chiều dài bằng kích thước đường chéo của hộp cọc nối "
               "(ví dụ, 1,4 m cho hộp cọc nối 1 m x 1 m). Sau đó hộp được lắp "
               "với số cọc nối lớn nhất loại đó mà nó được thiết kế, được nối "
               "nối tiếp (xem Hình 12.10). Vì các dây dẫn bên trong hộp thường "
               "được bó lại với nhau, các dây dẫn dùng cho mục đích này được "
               "bó lại với nhau, theo nhóm sáu, sau đó dòng danh định cực đại "
               "được áp vào mạch tạo ra. Khi đó cần xác định nhiệt độ cao nhất "
               "đạt được bên trong hộp và đây sẽ là nhiệt độ quyết định phân "
               "loại nhiệt độ của hộp. Công suất dùng trong đánh giá này cũng "
               "có thể được tính khi đã biết điện trở của dây dẫn và của mối "
               "nối dây/cọc nối, và khi đó nó sẽ cấu thành công suất tiêu tán "
               "tối đa cho phép của hộp. Khi đưa vào sử dụng, hộp có thể được "
               "dùng cho bất kỳ số cọc nối trường hợp xấu nhất nào hoặc các "
               "cọc nối ít hạn chế hơn, miễn là không vượt quá số công suất "
               "tối đa và không cọc nối nào hoạt động ở dòng vượt quá dòng "
               "danh định của nó. Các thông số của tất cả cọc nối dự định sau "
               "đó cần được nêu để các tổ hợp được phép dễ xác định."))
    b.append(note("<b>Lưu ý về cụm 'inside the terminal, box' trong bản in.</b> "
                  "Bản in có dấu phẩy sau 'terminal' trong cụm 'which has, "
                  "inside the terminal, box a length equal to the diagonal "
                  "dimension of the terminal box'. Cụm này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt dịch theo ý định là "
                  "'bên trong hộp cọc nối, có chiều dài bằng...'."))
    b.append(fig(10, FC.fig_f1210()))
    b.append(note("<b>Lưu ý về công thức trong chú thích Hình 12.10.</b> Lớp "
                  "văn bản OCR đọc công thức trong chú thích là '(m)', nhưng "
                  "trang render cho thấy '(√(H² + W²))'. Hình vẽ lại dùng dạng "
                  "đúng từ trang render; không thay thế ký hiệu căn."))

    # Printed p.313.
    b.append(p("Là kết quả của điều này, phân loại nhiệt độ có thể được quy "
               "định hoặc là phân loại đạt được bởi các tổ hợp cụ thể của cọc "
               "nối, hoặc bởi bất kỳ tổ hợp nào của các loại cọc nối cụ thể mà "
               "cùng nhau không tiêu tán nhiều hơn giới hạn công suất quy "
               "định."))

    b.append(h4("12.3.2 Thiết bị chiếu sáng cấp nguồn từ lưới điện",
                "12.3.2 Mains powered luminaires"))
    b.append(p("Dù rõ ràng là có thể dùng bất kỳ loại đèn nào mà không nhiệt độ "
               "nào có khả năng gây cháy, kể cả nhiệt độ bên trong chính thủy "
               "tinh đèn khi đèn bị vỡ, điều này không phải là sự linh hoạt "
               "thực tế vì hầu hết đèn có dây tóc nóng sáng hoặc hoạt động ở "
               "nhiệt độ cao và sẽ không đáp ứng yêu cầu này. Loại đèn duy "
               "nhất thường được chấp nhận trong những trường hợp như vậy là "
               "loại catot lạnh (huỳnh quang), trong đó nhiệt độ bên trong "
               "luôn nằm trong các giới hạn đó. Ngoài ra, việc sử dụng đèn "
               "phải rất cụ thể vì vỡ đèn có thể dẫn đến cháy, hoặc có các "
               "yêu cầu kết cấu cụ thể tồn tại trong trường hợp những thứ như "
               "sắp xếp kết nối đèn. Thông thường cần quy định từ danh sách "
               "sau:"))
    b.append(p("1. đèn dây tóc vonfram theo cả BS 5971 (1988)¹² và BS 161 "
               "(1990);¹³"))
    b.append(p("2. đèn hỗn hợp ánh sáng (vonfram và thủy ngân huỳnh quang) loại "
               "MBTF. (Đây là các loại áp suất cao vì hàm lượng trong đèn thấp "
               "hơn so với đèn áp suất thấp (MTAF), do đó giảm các vấn đề khi "
               "vỡ);"))
    b.append(p("3. đèn huỳnh quang khởi động nguội theo EN 60061 (1993)¹⁴ "
               "(điều này không giống với IEC 61-1). Có thể nhớ lại từ Chương "
               "10 rằng các đèn này có một chân duy nhất để dùng trong đế đèn "
               "'kiểu chống cháy'."))
    b.append(note("<b>Lưu ý về ký hiệu chú thích dạng mũ trong danh sách "
                  "đèn.</b> Bản in dùng ¹² sau 'BS 5971 (1988)', ¹³ sau dấu "
                  "chấm phẩy sau '(1990)', ¹⁴ sau 'EN 60061 (1993)' và ¹³ sau "
                  "'BS/EN 50018'; lớp văn bản OCR đọc nhầm thành dấu nháy kép "
                  "hoặc chữ số thường dính vào tên tiêu chuẩn. Các ký hiệu "
                  "dạng mũ được giữ theo bản in."))
    b.append(p("Nhìn chung, tất cả đèn và chụp đèn của chúng được yêu cầu tạo "
               "thành các vỏ bọc mà, tại thời điểm tách tiếp điểm, vượt qua "
               "các thử nghiệm truyền ngọn lửa quy định cho vỏ bọc chống cháy "
               "(xem BS/EN 50018¹³ và Chương 10), hoặc được sắp xếp sao cho "
               "sự tách xảy ra trong một vỏ bọc chống cháy riêng tuân thủ Tiêu "
               "chuẩn này trước khi tách các tiếp điểm của đèn. Điều này "
               "không cần thiết nếu kết nối được thực hiện bằng các tiếp điểm "
               "có thể được coi là không phát tia lửa (ví dụ, nhiều tiếp điểm "
               "với áp lực đủ), việc tháo đèn bị ngăn cản khi thiết bị chiếu "
               "sáng còn có điện (ví dụ, bằng cách có một công tắc cách ly "
               "được liên khóa với nắp ngoài của thiết bị chiếu sáng), và "
               "đảm bảo đèn không thể bị lỏng (ví dụ, bằng cách dùng cơ cấu "
               "khóa để ngăn vặn ra trong trường hợp đèn vặn ren hoặc ngăn "
               "đế đèn bị lệch đầu trong trường hợp đèn huỳnh quang). Dù "
               "những tình huống sau này không được đề cập cụ thể trong "
               "trường hợp thiết bị chiếu sáng, chúng được đề cập trong "
               "trường hợp phích cắm và ổ cắm và sẽ có giá trị như nhau cho "
               "thiết bị chiếu sáng. Vấn đề chính trong việc áp dụng chúng là "
               "các tiếp điểm được tạo trong phích cắm và ổ cắm không được "
               "coi là phát tia lửa được tạo ở hai hoặc nhiều vị trí theo "
               "thiết kế. Điều này thường không phải là trường hợp đối với "
               "đèn, vốn thường chỉ có một"))

    # Printed p.314.
    b.append(p("kết nối và không phù hợp với cách tiếp cận này. Tuy nhiên, nó "
               "đã được dùng trong trường hợp ống huỳnh quang có đế hai chân "
               "và thường được dùng với catot nóng. Trong những trường hợp "
               "này, người ta đã chứng minh rằng các ống đó có thể làm việc "
               "với catot lạnh và, cho mục đích kết nối, các chân đầu được "
               "nối với nhau bằng một dây gia nhiệt điện trở thấp, có thể "
               "được dùng hiệu quả song song để đạt được độ an toàn kết nối "
               "yêu cầu, miễn là chụp đèn của chúng được sửa đổi để tăng độ "
               "an toàn của kết nối."))
    b.append(p("Trong trường hợp bình thường, cách tiếp cận trên không thể "
               "áp dụng và cần tính đến việc phát tia lửa khi tháo đèn. Điều "
               "này được thực hiện hoặc bằng cách dùng cụm chụp đèn/đế đèn "
               "như một dạng vỏ bọc chống cháy cần đáp ứng một số hoặc tất "
               "cả yêu cầu của BS/EN 50018 (Xem Chương 10) được quy định cho "
               "các tổ hợp chụp đèn/đế đèn trong điều 18 của Tiêu chuẩn đó, "
               "hoặc bằng một sắp xếp sao cho mạch điện bị ngắt trong một vỏ "
               "bọc chống cháy riêng (xem Hình 12.11) trước"))
    b.append(fig(11, FC.fig_f1211()))
    b.append(note("<b>Lưu ý về nhãn và số hiệu Hình 12.11.</b> Bản in có nhãn "
                  "'Flameproof bushing' (lớp văn bản OCR đọc nhầm thành "
                  "'Flameoroof') và số hiệu 'Fig. 12.11' (OCR tách thành "
                  "'Fig. 12.1 1'); chú thích in gồm cả câu bắt đầu bằng "
                  "'Note: If final connection...'. Hình vẽ lại dùng dạng đúng "
                  "từ trang render."))

    # Printed p.315.
    b.append(p("khi kết nối giữa chụp đèn và đế đèn bị ngắt. Trong cả hai "
               "trường hợp, cụm phải phù hợp với nhóm phụ IIC."))
    b.append(p("Trong mọi trường hợp, kết nối điện với đèn cần chắc chắn để "
               "đảm bảo không phát tia lửa khi đèn được lắp hoàn toàn. Dù "
               "điều này có thể được coi là yêu cầu quá mức, vì cụm đã được "
               "chứng minh không truyền ngọn lửa, cần nhớ rằng có sự khác "
               "biệt giữa tia lửa thỉnh thoảng trong khi tháo và tia lửa "
               "liên tục do lỏng hoặc tiếp xúc kém. Độ chắc chắn của tiếp "
               "điểm được đảm bảo bằng một trong các biện pháp sau. Thứ "
               "nhất, các tiếp điểm lò xo dùng trong trường hợp tiếp điểm "
               "chân hình trụ, chẳng hạn như dùng trong ống huỳnh quang, cần "
               "có lực tiếp điểm 10N khi đèn được lắp hoàn toàn. Thứ hai, các "
               "tiếp điểm lò xo của đèn cắm hình trụ, chẳng hạn như đèn kiểu "
               "ngàm bajonet, cần có lực tiếp điểm 10N khi các ngàm bajonet "
               "được lắp hoàn toàn. Thứ ba, trong trường hợp chụp ren, tiếp "
               "điểm lò xo đầu cần có lực ít nhất 15N khi đèn được vặn hoàn "
               "toàn vào và tiếp điểm ren cần được tạo qua ít nhất hai ren "
               "đầy hoặc, thay thế, qua các tiếp điểm bên dạng lò xo có lực "
               "30N. Trong các trường hợp kết nối đèn bị ngắt trong một vỏ "
               "bọc chống cháy riêng trong lúc tháo đèn khỏi đế đèn, trước "
               "khi các tiếp điểm của đèn bị ngắt, lực tối thiểu yêu cầu của "
               "bất kỳ phần tử tiếp điểm lò xo nào được giảm xuống 7.5 N."))
    b.append(p("Có một vấn đề riêng trong trường hợp đèn vặn ren là nó thường "
               "không được cố định chắc chắn chống lại sự lỏng, và do đó cần "
               "có biện pháp chứng minh độ chắc chắn của nó đối với vấn đề "
               "này. Để đạt được điều đó, có thể áp dụng một phép thử. Đèn "
               "có thể được lắp vào đế đèn với một mô-men xác định và sau đó "
               "vặn ra 15°. Mô-men cần thiết để vặn tiếp phải cao hơn một giá "
               "trị tối thiểu nhất định. Bảng 12.5 cho biết các giá trị mô-men "
               "cần thiết và độ chắc chắn cần thiết có thể, nếu muốn, đạt "
               "được bằng cách dùng cơ cấu khóa để ngăn tháo đèn."))
    b.append(note("<b>Lưu ý về dấu độ trong bản in.</b> Bản in ghi 'unscrewed "
                  "by 15°', '50 °C lower' và '200 °C'; lớp văn bản OCR đọc "
                  "dấu độ thành dấu nháy kép ('15\"', '50 \"C', '200 \"C'). "
                  "Dấu độ được giữ theo bản in."))
    b.append(p("Đèn (trừ những đèn dùng trong bộ đèn huỳnh quang) thường rất "
               "nóng và, để giảm thiểu nguy cơ nắp thiết bị chiếu sáng bị "
               "hư hại do nhiệt và cho phép luồng không khí lưu thông tốt "
               "quanh đèn, khoảng cách giữa đèn và nắp thiết bị chiếu sáng "
               "cần lớn hơn một"))
    b.append(table(T2.HEAD125_VI, T2.ROWS125_VI, T2.CAPTION125_VI))
    if T2.NOTE125_VI:
        b.append(note(T2.NOTE125_VI))

    # Printed p.316.
    b.append(p("giá trị tối thiểu quy định. Giá trị này được cho trong Bảng "
               "12.6 cho tất cả đèn trừ đèn huỳnh quang. Đối với đèn huỳnh "
               "quang, vì ít nhiệt hơn có thể áp dụng giải pháp đơn giản hơn "
               "và áp dụng mức tối thiểu 5mm. Mức này được giảm tiếp xuống "
               "2mm khi nắp thực chất là một ống bổ sung bao quanh ống huỳnh "
               "quang."))
    b.append(table(T2.HEAD126_VI, T2.ROWS126_VI, T2.CAPTION126_VI))
    if T2.NOTE126_VI:
        b.append(note(T2.NOTE126_VI))
    b.append(p("Không gian hạn chế bên trong thiết bị chiếu sáng có ảnh hưởng "
               "đến sự cháy của bầu khí quyển nổ chứa bên trong, có thể do các "
               "quá trình như đối lưu, gây chuyển động khí từ các bộ phận nóng "
               "của thiết bị chiếu sáng đến các bộ phận mát hơn dẫn đến mất "
               "nhiệt. Hiệu ứng này có thể được dùng bằng cách nạp vào một "
               "thiết bị chiếu sáng cụ thể hỗn hợp dễ cháy nhất của một khí "
               "dễ cháy cụ thể với không khí, và xác định nhiệt độ đèn mà tại "
               "đó xảy ra cháy. Bằng cách này, có thể cho phép một đèn vượt "
               "quá cấp, mức tối đa cho một cấp nhiệt độ nhất định, miễn là "
               "nhiệt độ cực đại của nó thấp hơn 50 °C so với nhiệt độ cháy "
               "tối thiểu đo được cho thiết bị chiếu sáng đó và bầu khí quyển "
               "nổ đó. Tuy nhiên, sự miễn trừ này chỉ được phép khi các thử "
               "nghiệm riêng lẻ đã chứng minh hiệu quả của nó trong các thiết "
               "bị chiếu sáng cụ thể, và danh sách các bầu khí quyển nổ mà sự "
               "miễn trừ được xác nhận bằng thử nghiệm trong từng trường hợp "
               "cần được quy định cho thiết bị chiếu sáng cụ thể."))
    b.append(p("Nhiều thiết bị chiếu sáng dùng thiết bị điều khiển (ví dụ, "
               "cuộn chấn, tụ điện và sắp xếp khởi động) cho thiết bị chiếu "
               "sáng huỳnh quang. Những thứ này đưa ra các vấn đề cụ thể cần "
               "lưu ý, đặc biệt vì hỏng đèn (nhưng không vỡ vỏ) được coi là "
               "hoạt động bình thường."))
    b.append(p("Trong trường hợp thiết bị chiếu sáng huỳnh quang, cách tiếp "
               "cận sau là thông thường. Bộ khởi động công tắc thông thường "
               "dùng trong đèn huỳnh quang chứa một công tắc mà, dù thường "
               "được bịt kín kín khí, không được chấp nhận trong nguyên lý "
               "kiểu 'e'. Để khắc phục, đèn huỳnh quang kiểu 'e' thường khởi "
               "động không công tắc (bán cộng hưởng). Cách này đắt hơn khi sử "
               "dụng nhưng bỏ đi nhu cầu dùng một bộ khởi động. Nếu dùng bộ "
               "khởi động công tắc, nó sẽ cần chống cháy (xem Chương 10), "
               "điều sẽ làm nó đắt hơn cách khởi động không công tắc và, vì "
               "lý do đó, nó hiếm khi được dùng. Nhìn chung, khi ống huỳnh "
               "quang hỏng, cuộn chấn trong bộ đèn sẽ quá nhiệt. Điều này"))
    b.append(note("<b>Lưu ý về cụm 'for as starter'.</b> Bản in viết 'removes "
                  "the need for as starter'; lớp văn bản OCR cũng ghi như "
                  "vậy. Cụm này được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt dịch theo ý định là 'bỏ đi nhu cầu dùng một bộ "
                  "khởi động'."))

    # Printed p.317.
    b.append(p("không được chấp nhận trong kiểu 'e' vì nó có thể vừa làm bộ "
               "đèn nóng lên vượt quá phân loại nhiệt độ của nó, vừa làm "
               "chính cuộn chấn hỏng. Cả hai đều không được chấp nhận. Trong "
               "trường hợp hỏng ống, cuộn chấn không được nóng vượt quá định "
               "mức vật liệu của nó hoặc vượt quá phân loại nhiệt độ của bộ "
               "đèn. Điều này có thể đạt được bằng thiết kế cuộn chấn hoặc "
               "bằng cách dùng sự tăng dòng cuộn chấn khi đèn không hoạt động "
               "để vận hành bảo vệ điện. Tụ điện dùng trong bộ đèn huỳnh "
               "quang không thể đáp ứng yêu cầu kiểu 'e' vì cấu tạo của "
               "chúng có hai lớp lá rất gần nhau, và do đó không thể đáp ứng "
               "yêu cầu tách biệt của kiểu 'e'. Để khắc phục, các tụ điện "
               "như vậy cần được bảo vệ bằng cách khác. Cách điển hình để "
               "làm điều này là đặt tụ điện trong vỏ bọc chống cháy (xem "
               "Chương 10) hoặc dùng vật liệu độn bột (xem Chương 9)."))
    b.append(note("<b>Lưu ý về kiểu viết cụm 'type e' có trích dẫn và chữ hoa "
                  "trong bản in.</b> Trang render cho thấy có dấu cách giữa "
                  "'type' và chữ e được đặt trong dấu nháy; lớp văn bản OCR "
                  "đôi khi bỏ dấu cách đó. Ngoài ra bản in viết '(e.g., "
                  "Intrinsic Safety - See Chapter 13)' với 'See' viết hoa, "
                  "nhưng '(e.g., Flameproof - see Chapter 10)' với 'see' viết "
                  "thường, và '(e.g., intrinsic safety - see Chapter 13)' viết "
                  "thường. Các dạng này được giữ nguyên trong bản tiếng Anh."))

    b.append(h4("12.3.3 Đèn đội đầu", "12.3.3 Caplamps"))
    b.append(p("Đây thường là thiết bị chạy bằng pin và có cụm pin riêng. Dù "
               "an toàn tăng cường cũng được dùng cho đèn trong những thứ như "
               "đèn pin, người ta thường không dùng kỹ thuật này ngoại trừ "
               "các thiết bị mạnh nhất trong số đó, hoặc kết hợp với một "
               "nguyên lý bảo vệ khác (ví dụ, an toàn nội tại - xem Chương "
               "13)."))
    b.append(p("Yêu cầu đối với đèn đội đầu tương đối đơn giản vì đèn, nếu vặn "
               "ren, thường là E10 hoặc nhỏ hơn, và do đó không tồn tại yêu "
               "cầu mô-men lắp. Đèn cần có nắp bảo vệ và nếu nắp này có diện "
               "tích bề mặt nhỏ hơn 50 cm², trường hợp phổ biến hơn, thì chỉ "
               "cần một vành bảo vệ cao ít nhất 2 mm. Tuy nhiên, nếu diện tích "
               "bề mặt vượt quá giá trị này, cần có một lồng bảo vệ đầy đủ "
               "đáp ứng BS/EN 50014⁷."))
    b.append(note("<b>Lưu ý về đơn vị và dấu cách trong bản in.</b> Bản in ghi "
                  "'50 cm² surface area' (số 2 dạng mũ) và '2 mm height' có "
                  "dấu cách; lớp văn bản OCR đọc '50cm2' và '2mm'. Các dạng in "
                  "được giữ nguyên; bản tiếng Việt dùng '50 cm²' và '2 mm'."))
    b.append(p("Pin cần đáp ứng yêu cầu của nguyên lý bảo vệ này hoặc một "
               "nguyên lý khác (ví dụ, An toàn nội tại - Xem Chương 13) và "
               "công tắc cần hoặc được liên khóa để ngăn không cho tách ra "
               "trong Vùng Nguy hiểm, hoặc được bảo vệ bằng cách khác (ví dụ, "
               "Chống cháy - xem Chương 10)."))
    b.append(note("<b>Lưu ý về chữ hoa trong các tài liệu tham chiếu liên "
                  "chương.</b> Bản in viết 'Intrinsic Safety - See Chapter "
                  "13' và 'Flameproof - see Chapter 10' với cách viết hoa "
                  "không nhất quán ('See' so với 'see'). Các dạng này được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt dịch theo "
                  "ý định."))

    b.append(h4("12.3.4 Thiết bị đo và máy biến áp",
                "12.3.4 Measuring instruments and transformers"))
    b.append(p("Yêu cầu đối với các thiết bị an toàn tăng cường như vậy nhắm "
               "vào thiết bị đo điện áp và dòng điện, thiết bị sau dùng máy "
               "biến dòng, và máy biến áp điện áp thông thường. Không hình "
               "dung đến thiết bị đo điện tử và, vì sự mong manh của lò xo "
               "kết nối, không giả định rằng thiết bị cuộn di động nào có thể "
               "đáp ứng yêu cầu an toàn tăng cường."))
    b.append(p("Máy biến áp điện áp hoặc dòng điện thông thường cần đáp ứng "
               "yêu cầu đối với dây quấn và độ tăng nhiệt của chúng để lựa "
               "chọn cấp cách điện, và phân loại nhiệt độ được xác định ở tải "
               "danh định. Độ tăng nhiệt của chúng có thể được hạn chế bởi "
               "một thiết bị bảo vệ tích hợp hoặc một thiết bị bên ngoài, miễn "
               "là, nếu ở bên ngoài, thiết bị được quy định đầy đủ. Khi tải "
               "của máy biến áp nằm bên ngoài thiết bị,"))

    # Printed p.318 (partial page; the chunk ends at LF 14031).
    b.append(p("mức độ kiểm soát yêu cầu không thể thực hiện được và độ tăng "
               "nhiệt, lại với các thiết bị bảo vệ trong mạch, được đo với "
               "đầu thứ hai bị ngắn mạch trong trường hợp máy biến áp điện "
               "áp, hoặc hở mạch trong trường hợp máy biến dòng, và nếu có "
               "thể xác định được điều kiện bên ngoài bất lợi hơn thì cũng "
               "phải tính đến nó."))
    b.append(p("Khi các máy biến áp như vậy nằm bên trong thiết bị và trở "
               "thành 'máy biến áp đo', chúng phải, thêm vào đó, chịu được "
               "không hư hại 1.2 lần dòng hoặc điện áp cực đại danh định của "
               "chúng. Nếu được coi là máy biến dòng, trong trường hợp này "
               "chúng phải có khả năng chịu các ứng suất nhiệt và động lực "
               "học do việc áp dụng các dòng được tính với hệ số an toàn cụ "
               "thể Ith (dòng rms được tính hệ số an toàn dùng để xác định "
               "ứng suất nhiệt và độ tăng nhiệt) và Idyn (dòng đỉnh được tính "
               "hệ số an toàn dùng để đánh giá ứng suất động lực học) cho "
               "trong Bảng 12.7. Trong trường hợp Idyn, hai hệ số an toàn "
               "được dùng. Thứ nhất là 1.25 và nhằm cho một hệ số an toàn "
               "chung cho các ứng suất động với các biến đổi bình thường, và "
               "thứ hai là 2.5 và nhằm cho một hệ số an toàn để tính đến các "
               "dạng sóng khác với dạng sin. Ith là dòng dùng để xác định "
               "nhiệt độ vận hành cực đại trong những trường hợp này, và "
               "ngoài việc nhiệt độ đó phải nằm trong giới hạn do cách điện "
               "và phân loại nhiệt độ quy định, một giới hạn chung 200 °C "
               "được áp dụng trong những trường hợp này. Có thể máy biến dòng "
               "đi ra khỏi một thiết bị, và trong những trường hợp như vậy "
               "cần xác định điều này và đảm bảo người sử dụng biết về nhu "
               "cầu ngăn không cho xảy ra hở mạch."))
    b.append(note("<b>Lưu ý về ký hiệu Ith và Idyn.</b> Bản in dùng chữ I "
                  "nghiêng với chỉ số dưới 'th' và 'dyn' (I_th, I_dyn); lớp "
                  "văn bản OCR làm mất chỉ số dưới hoặc đọc nhầm thành ký hiệu "
                  "khác. Bản dịch dùng 'Ith' và 'Idyn' để khớp với nhãn trong "
                  "Bảng 12.7."))
    b.append(note("<b>Lưu ý về 'an safety factor' và 'sinusiodal'.</b> Cả hai "
                  "được xác nhận trong trang render: bản in viết 'intended to "
                  "give an safety factor to allow for waveforms other than "
                  "sinusiodal'. Chúng được giữ nguyên trong bản tiếng Anh; "
                  "bản tiếng Việt dịch theo ý định là 'một hệ số an toàn' và "
                  "'dạng sin'."))
    b.append(note("<b>Lưu ý về cụm 'may exit a piece of apparatus'.</b> Cụm này "
                  "được xác nhận trong bản in và được giữ nguyên trong bản "
                  "tiếng Anh, dù cách diễn đạt thông thường sẽ là 'exit from'. "
                  "Không sửa lặng lẽ cụm này."))
    b.append(p("Thiết bị đo được xử lý tương tự, ở chỗ chúng phải có khả năng "
               "chịu được 1.2 lần điện áp hoặc dòng danh định của chúng vô "
               "thời hạn, và không vượt quá nhiệt độ tối đa cho phép xác định "
               "bởi"))
    b.append(table(T2.HEAD127_VI, T2.ROWS127_VI, T2.CAPTION127_VI))
    if T2.NOTE127_VI:
        b.append(note(T2.NOTE127_VI))
    b.append(note("<b>Lưu ý về ranh giới đoạn cuối.</b> Đoạn 'Measuring "
                  "instruments are similarly treated...' kết thúc bằng "
                  "'determined by' vì tiếp tục ở trang in tiếp theo (nằm "
                  "ngoài phạm vi module này) với 'insulation requirements and "
                  "temperature classification...'. Chỗ ngắt được giữ nguyên "
                  "theo bản in."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.312. Continuation of the 12.3.1 paragraph from the previous
    # module; the heading itself belongs to module C.
    b.append(p("total internal power, which can be dissipated within the "
               "enclosure by all terminals and wiring therein. In order to "
               "determine the worst case for any terminal box it is therefore "
               "necessary to identify the worst terminal intended for use "
               "therein. This is the terminal which achieves the maximum "
               "surface temperature when connected to a conductor of its "
               "maximum specified size which has, inside the terminal, box a "
               "length equal to the diagonal dimension of the terminal box "
               "(e.g., 1.4 m for a 1 m x 1 m terminal box). The box is then "
               "fitted with the maximum number of such terminals of that type "
               "for which it is designed which are wired in series (see Fig. "
               "12.10). As conductors within the box will often be loomed "
               "together, the conductors used for this purpose are loomed "
               "together, in sets of six and then the maximum rated current "
               "is then applied to the circuit produced. It is then necessary "
               "to identify the maximum temperature reached within the box "
               "and this will be the temperature which determines the "
               "temperature classification of the box. The power used in this "
               "evaluation can also be calculated once the wire and "
               "wire/terminal connection resistance is known, and this will "
               "then constitute the maximum power dissipation permitted for "
               "the box. When in service the box may then be used for any "
               "number of the worst case terminals or other less limiting "
               "terminals, provided the maximum power figure is not exceeded "
               "and no terminal operates at more than its rated current. The "
               "parameters of all intended terminals then need to be quoted "
               "so that the permissible combinations are easy to determine."))
    b.append(note("<b>Note on 'inside the terminal, box' in the print.</b> The "
                  "print has a comma after 'terminal' in 'which has, inside "
                  "the terminal, box a length equal to the diagonal dimension "
                  "of the terminal box'. The wording is retained in English; "
                  "the Vietnamese follows the intended sense."))
    b.append(fig(10, FC.fig_f1210()))
    b.append(note("<b>Note on the formula in the Fig. 12.10 note.</b> The OCR "
                  "text layer reads the note formula as '(m)', while the page "
                  "render shows '(√(H² + W²))'. The redraw follows the "
                  "rendered form; the radical is not replaced."))

    # Printed p.313.
    b.append(p("As a result of this the temperature classification can be "
               "specified as either the classification achieved by specific "
               "combinations of terminals, or by any combination of specific "
               "types of terminal which together do not dissipate more than "
               "the specified power limitation."))

    b.append(h4("12.3.2 Mains powered luminaires",
                "12.3.2 Mains powered luminaires"))
    b.append(p("Although it is obviously possible to utilize any type of lamp "
               "in which no temperature will be ignition capable, even that "
               "inside the lamp glass itself when the lamp is broken, this is "
               "not a real flexibility as most lamps have incandescent "
               "filaments or operate at high temperature and would not satisfy "
               "this requirement. The only type of lamp which will normally "
               "be acceptable in such circumstances is the cold cathode "
               "(fluorescent) type where internal temperatures are always "
               "within those limits. Other than that, the use of lamps must "
               "be very specific as breakage could lead to ignition, or "
               "specific constructional requirements exist in the case of "
               "such things as lamp connection arrangements. It is normally "
               "necessary to specify from the following list:"))
    b.append(p("1. tungsten filament lamps in accordance with both BS 5971 "
               "(1988)¹² and BS 161 (1990);¹³"))
    b.append(p("2. mixed light (tungsten and mercury fluorescent) lamps type "
               "MBTF. (These are high pressure types as the content of the "
               "lamp is lower than for low pressure (MTAF) lamps, thus reducing "
               "problems on breakage);"))
    b.append(p("3. cold starting fluorescent lamps in accordance with EN "
               "60061 (1993)¹⁴ (this is not the same as IEC 61-1). It will be "
               "remembered from Chapter 10 that these lamps have a single pin "
               "for use in 'flameproof type' lampholders."))
    b.append(note("<b>Note on the superscript footnote markers in the lamp "
                  "list.</b> The print uses ¹² after 'BS 5971 (1988)', ¹³ "
                  "after the semicolon following '(1990)', ¹⁴ after 'EN "
                  "60061 (1993)' and ¹³ after 'BS/EN 50018'; the OCR text "
                  "layer misreads them as doubled apostrophes or ordinary "
                  "digits attached to the standard designations. The "
                  "superscripts are retained as printed."))
    b.append(p("In general, all lamps and their lampcaps are required to form "
               "enclosures which, at the time of contact separation, pass the "
               "flame transmission tests specified for flameproof enclosures "
               "(see BS/EN 50018¹³ and Chapter 10) or be arranged so that "
               "separation occurs in a separate flameproof enclosure complying "
               "with this standard prior to separation of the lamp contacts. "
               "This is not necessary if the connection is made by contacts "
               "which can be assumed to be non-sparking (e.g., multiple "
               "contacts with sufficient pressure), removal of the lamp is "
               "prevented while the luminaire is energized (e.g., by having "
               "an isolating switch interlocked with the outer cover of the "
               "luminaire), and ensuring that the lamp cannot work loose "
               "(e.g., by the use of a locking device to prevent unscrewing "
               "in the case of a screw lamp or to prevent end-cap float in the "
               "case of a fluorescent). While these latter situations are not "
               "specifically addressed in the case of luminaires, they are in "
               "the case of plugs and sockets and will be equally valid for "
               "luminaires. The main problem in their application is that the "
               "contacts made in a plug and socket which are not considered "
               "as sparking are made in two or more places by design. This is "
               "not normally the case in respect of lamps which usually only "
               "have one"))

    # Printed p.314.
    b.append(p("connection and do not lend themselves to this approach. It "
               "has, however, been used in the case of fluorescent tubes which "
               "have bi-pin bases and are normally used with hot cathodes. In "
               "these cases it has been shown that such tubes can work with "
               "cold cathodes and for the purposes of connection the endpins, "
               "connected as they are by a low resistance heater, can be "
               "effectively used in parallel to achieve the required security "
               "of connection, provided their lamp cap is modified to increase "
               "the security of connection."))
    b.append(p("In normal circumstances the above approach is not possible "
               "and it is necessary to allow for sparking on lamp "
               "disconnection. This is done either by using the lampcap/"
               "lampholder assembly as a sort of flameproof enclosure which "
               "needs to satisfy some or all of the requirements of BS/EN "
               "50018 (See Chapter 10) which are specified for lampcap/"
               "lampholder combinations in clause 18 of that Standard, or by "
               "an arrangement so that the electrical circuit is broken in a "
               "separate flameproof enclosure (see Fig. 12.11) before"))
    b.append(fig(11, FC.fig_f1211()))
    b.append(note("<b>Note on the labels and number of Fig. 12.11.</b> The "
                  "print carries the label 'Flameproof bushing' (the OCR text "
                  "layer reads 'Flameoroof') and the number 'Fig. 12.11' (OCR "
                  "splits it as 'Fig. 12.1 1'); the printed caption includes "
                  "the sentence beginning 'Note: If final connection...'. The "
                  "redraw follows the rendered forms."))

    # Printed p.315.
    b.append(p("the connection between the lampcap and lampholder is broken. "
               "In either case the assembly must be suitable for sub-group "
               "IIC."))
    b.append(p("In all cases the electrical connection to the lamp needs to be "
               "secure to ensure that no sparking occurs when the lamp is "
               "fully inserted. While this may be considered as too great a "
               "requirement, as the assembly is shown not to transmit flame, "
               "it must be remembered that there is a difference between "
               "occasional sparking during removal and continuous sparking "
               "due to loosening or bad contact. Security of contact is "
               "assured by one of the following means. First, the spring "
               "contacts used in the case of cylindrical pin contacts, such "
               "as those used in fluorescent tubes, need to have a contact "
               "force of 10N when the lamp is fully engaged. Second, the "
               "spring contacts of cylindrical plug-in lamps, such as bayonet "
               "fitting lamps, need to have a contact force of 10N when the "
               "bayonets are fully engaged. Third, in the case of screw caps, "
               "the end-spring contact should have a force of at least 15N "
               "when the lamp is fully home and the thread contact should be "
               "made through at least two full threads or, alternatively, "
               "through spring side contacts having a force of 30N. In cases "
               "where the lamp connection is broken in a separate flameproof "
               "enclosure during removal of the lamp from the lampholder, "
               "before the lamp contacts are broken, the minimum required "
               "force of any spring contact elements is reduced to 7.5 N."))
    b.append(p("There is a particular problem in the case of a screw lamp in "
               "that it is not normally positively secured against loosening, "
               "and as a result there needs to be some measure used to "
               "demonstrate its security against this problem. To achieve "
               "this a test may be applied. The lamp may be inserted into the "
               "lampholder with a specific torque and then unscrewed by 15°. "
               "The torque necessary to achieve further unscrewing must then "
               "be above a certain minimum value. Table 12.5 indicates the "
               "necessary torque values and the necessary security may, if "
               "desired, be achieved by the use of a locking device to prevent "
               "lamp removal."))
    b.append(note("<b>Note on the degree signs in the print.</b> The print "
                  "reads 'unscrewed by 15°', '50 °C lower' and '200 °C'; the "
                  "OCR text layer reads the degree sign as a double quote "
                  "('15\"', '50 \"C', '200 \"C'). The degree signs are retained "
                  "as printed."))
    b.append(p("Lamps (except those used in fluorescent fittings) are normally "
               "extremely hot and, to minimize the risk of the cover of the "
               "luminaire suffering damage due to heat and to allow good air "
               "circulation around the lamp, the separation between the lamp "
               "and luminaire cover needs to be above a"))
    b.append(table(T2.HEAD125_EN, T2.ROWS125, T2.CAPTION125_EN))
    if T2.NOTE125_EN:
        b.append(note(T2.NOTE125_EN))

    # Printed p.316.
    b.append(p("specified minimum figure. This figure is given in Table 12.6 "
               "for all except fluorescent lamps. For fluorescent lamps, where "
               "there is less heat a more simple solution may be adopted and a "
               "5mm minimum is applied. This is further reduced to 2mm where "
               "the cover is effectively an additional tube around the "
               "fluorescent tube."))
    b.append(table(T2.HEAD126_EN, T2.ROWS126, T2.CAPTION126_EN))
    if T2.NOTE126_EN:
        b.append(note(T2.NOTE126_EN))
    b.append(p("The confined space inside luminaires has an effect upon the "
               "ignition of contained explosive atmospheres, probably due to "
               "processes such as convection, causing gas movement from hot "
               "parts of the luminaire to cooler parts resulting in causing "
               "heat loss. This effect can be used by filling a particular "
               "luminaire with the most easily ignited mixture of a particular "
               "flammable gas and air, and determining the lamp temperature at "
               "which ignition occurs. By this means a lamp can be permitted "
               "which exceeds the class, maximum for a given temperature "
               "class, provided its maximum temperature is 50 °C lower than "
               "the minimum ignition temperature measured for that luminaire "
               "and that explosive atmosphere. This relaxation is, however, "
               "only permitted where individual tests have proved its efficacy "
               "in particular luminaires, and the list of explosive "
               "atmospheres for which the relaxation is validated by tests in "
               "each case needs to be specified for the particular luminaire."))
    b.append(p("Many luminaires utilize control equipment (e.g., chokes, "
               "capacitors and starting arrangements) for fluorescent "
               "luminaires. These present specific problems which require "
               "attention, particularly as lamp failure (but not envelope "
               "fracture) is considered as normal operation."))
    b.append(p("In the case of fluorescent luminaires the following approach "
               "is usual. The normal switch starter which is used in "
               "fluorescent lamps contains a switch which, although usually "
               "hermetically sealed, is not acceptable in the type 'e' "
               "concept. To overcome this, type 'e' fluorescents are usually "
               "switchless (semi-resonant) starting. This is more expensive "
               "to use but removes the need for as starter. If a switch "
               "starter was to be used it would need to be flameproof (see "
               "Chapter 10) which would make it more expensive than the "
               "switchless-start approach and, for this reason, it is seldom "
               "used. Generally, when a fluorescent tube fails, the choke in "
               "the fitting will overheat. This is"))
    b.append(note("<b>Note on 'for as starter'.</b> The print reads 'removes "
                  "the need for as starter', and the OCR text layer agrees. "
                  "The wording is retained in English; the Vietnamese follows "
                  "the intended meaning."))

    # Printed p.317.
    b.append(p("not acceptable in type 'e' as it could both cause the fitting "
               "to heat to above its temperature classification, and the choke "
               "itself to fail. Either would not be acceptable. In case of "
               "tube failure the choke must not heat either beyond its "
               "material rating or the fitting temperature classification. "
               "This can be achieved by choke design or by utilizing the "
               "increase in choke current when the lamp fails to operate "
               "electrical protection. Capacitors used in fluorescent fittings "
               "cannot comply with type 'e' requirements because of their "
               "construction in having two layers of foil very close "
               "together, and therefore not being able to satisfy the "
               "separation requirements of type 'e'. To overcome this, such "
               "capacitors need to be otherwise protected. Typical ways in "
               "which this is done are to arrange the capacitor in a "
               "flameproof enclosure (see Chapter 10) or use powder filling "
               "(see Chapter 9)."))
    b.append(note("<b>Note on the spacing of the quoted 'type e' phrase and on "
                  "capitalisation in the print.</b> The page render shows a "
                  "space between 'type' and the quoted letter e; the OCR text "
                  "layer sometimes drops that space. The print also writes "
                  "'(e.g., Intrinsic Safety - See Chapter 13)' with a capital "
                  "'See', '(e.g., Flameproof - see Chapter 10)' with a "
                  "lower-case 'see', and '(e.g., intrinsic safety - see "
                  "Chapter 13)' in lower case. These forms are retained as "
                  "printed."))

    b.append(h4("12.3.3 Caplamps", "12.3.3 Caplamps"))
    b.append(p("These are normally battery-operated devices and have a "
               "separate battery pack. While increased safety is also used "
               "for lamps in such things as torches, it is not usual to use "
               "the technique in any but the most powerful of such devices, "
               "or in conjunction with another protection concept (e.g., "
               "intrinsic safety - see Chapter 13)."))
    b.append(p("The requirements for caplamps are relatively simple as the "
               "lamps, if screwed in, are normally E10 or less, and so no "
               "insertion torque requirements exist. The lamp needs a "
               "protective cover and if this has less than a 50 cm² surface "
               "area, which is the more likely case, then all that is "
               "required is a guarding rim of at least 2 mm height. Should the "
               "surface area exceed this figure, however, a full guard "
               "satisfying BS/EN 50014⁷ is necessary."))
    b.append(note("<b>Note on units and spacing in the print.</b> The print "
                  "reads '50 cm² surface area' (with a superscript 2) and '2 "
                  "mm height' with a space; the OCR text layer reads '50cm2' "
                  "and '2mm'. The printed forms are retained."))
    b.append(p("The batteries need to satisfy the requirements of this "
               "protection concept or another (e.g., Intrinsic Safety - See "
               "Chapter 13) and the switch needs to either be interlocked to "
               "prevent its separation in a Hazardous Area or be otherwise "
               "protected (e.g., Flameproof - see Chapter 10)."))
    b.append(note("<b>Note on capitalisation in the chapter references.</b> "
                  "The print writes 'Intrinsic Safety - See Chapter 13' and "
                  "'Flameproof - see Chapter 10' with inconsistent "
                  "capitalisation ('See' versus 'see'). The forms are retained "
                  "as printed."))

    b.append(h4("12.3.4 Measuring instruments and transformers",
                "12.3.4 Measuring instruments and transformers"))
    b.append(p("The requirements for such devices of increased safety are "
               "aimed at voltage and current measuring devices, the latter "
               "using current transformers, and normal electrical voltage "
               "transformers. No electronic measuring devices are envisaged "
               "and, because of the fragility of connection springs, no moving "
               "coil devices are presumed to be capable of complying with the "
               "requirements for increased safety."))
    b.append(p("Normal voltage or current transformers need to comply with "
               "the requirements for windings and their temperature rise for "
               "selection of insulation grade, and temperature classification "
               "is determined at rated load. Their temperature rise may be "
               "limited by either an integral protective device or an external "
               "device, provided that, if external, the device is fully "
               "specified. Where the transformer load is external to the "
               "apparatus, the"))

    # Printed p.318 (partial page; the chunk ends at LF 14031).
    b.append(p("required degree of control cannot be exercised and the "
               "temperature rise, again with protective devices in circuit, "
               "is measured with the secondary short circuit in the case of "
               "voltage transformers, or open circuit in the case of current "
               "transformers also and, if a more adverse external condition "
               "can be identified, it must also be taken into account."))
    b.append(p("Where such transformers are within instruments and become "
               "'instrument transformers' they must, additionally, withstand "
               "without damage 1.2 times their maximum-rated current or "
               "voltage. If deemed current transformers they must, in this "
               "case, be capable of suffering the thermal and dynamic stresses "
               "produced by the application of the specifically safety-"
               "factored currents Ith (a safety factored rms current used to "
               "determine thermal stresses and temperature rise) and Idyn (a "
               "safety factored peak current for dynamic stress evaluation) "
               "given in Table 12.7. In the case of Idyn two safety factors "
               "are used. The first is 1.25 and is intended to give a general "
               "safety factor for dynamic stresses with normal variations and "
               "the second is 2.5 and is intended to give an safety factor to "
               "allow for waveforms other than sinusiodal. Ith is the current "
               "used for determination of maximum operating temperature in "
               "these cases, and apart from that temperature having to be "
               "within the limit specified by the insulation and temperature "
               "classification, an overall limit of 200 °C is applied in these "
               "cases. It is possible that current transformers may exit a "
               "piece of apparatus, and in such cases it is necessary to "
               "identify this and ensure that users are aware of the need to "
               "prevent open circuits occurring."))
    b.append(note("<b>Note on Ith and Idyn.</b> The print uses an italic I with "
                  "subscripts 'th' and 'dyn' (I_th, I_dyn); the OCR text layer "
                  "loses the subscripts or misreads the symbols. The "
                  "translation uses 'Ith' and 'Idyn' to match the row labels "
                  "in Table 12.7."))
    b.append(note("<b>Note on 'an safety factor' and 'sinusiodal'.</b> Both are "
                  "confirmed in the page render: the print reads 'intended to "
                  "give an safety factor to allow for waveforms other than "
                  "sinusiodal'. They are retained in English."))
    b.append(note("<b>Note on 'may exit a piece of apparatus'.</b> This wording "
                  "is confirmed in the print and is retained in English, "
                  "although the more usual expression would be 'exit from'. "
                  "No silent emendation is made."))
    b.append(p("Measuring instruments are similarly treated, in that they "
               "should be capable of withstanding 1.2 times their rated "
               "voltage or current indefinitely, and not exceed the maximum "
               "permissible temperature determined by"))
    b.append(table(T2.HEAD127_EN, T2.ROWS127_EN, T2.CAPTION127_EN))
    if T2.NOTE127_EN:
        b.append(note(T2.NOTE127_EN))
    b.append(note("<b>Note on the final sentence boundary.</b> The paragraph "
                  "'Measuring instruments are similarly treated...' ends with "
                  "'determined by' because it continues on the next printed "
                  "page (outside this module's range) with 'insulation "
                  "requirements and temperature classification...'. The "
                  "boundary is kept as printed."))
    return "".join(b)
