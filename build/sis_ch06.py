# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 6, Determining the Safety Integrity Level
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

import sis06fig as F

PAGES_SRC = 26
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def _sci(e):
    """10 to the power e, as inline markup."""
    return "10<sup>−%d</sup>" % e


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>SIL (mức toàn vẹn an toàn)</em> — thước đo hiệu năng của cả một hệ, không phải của một "
            "thiết bị đơn lẻ. · "
            "<em>PFD (xác suất hỏng khi có yêu cầu)</em> — xác suất hệ không thực hiện được chức năng lúc "
            "được gọi. · "
            "<em>RRF (hệ số giảm rủi ro)</em> — nghịch đảo của PFD; cách nói dễ hình dung hơn. · "
            "<em>FAR (tỷ lệ tai nạn chết người)</em> — số ca tử vong trên một triệu giờ phơi nhiễm. · "
            "<em>ALARP</em> — nguyên lý “thấp tới mức hợp lý có thể thực hiện được”, một khái niệm pháp lý "
            "chứ không phải một con số kỹ thuật. · "
            "<em>IPL (lớp bảo vệ độc lập)</em> — lớp chỉ có thể được tính vào phép tính nếu thoả bốn điều "
            "kiện: chuyên biệt, độc lập, đáng tin, kiểm toán được. · "
            "<em>LOPA</em> — phương pháp bán định lượng cộng dồn xác suất của từng lớp bảo vệ.")
    return note(
        "<b>Key terms.</b> <em>SIL</em> — a measure of the performance of a whole system, never of a single "
        "device. · <em>PFD</em> — the probability that the system fails to act when demanded. · "
        "<em>RRF</em> — the reciprocal of PFD, and the easier number to picture. · <em>FAR</em> — fatalities "
        "per hundred million person-hours of exposure. · <em>ALARP</em> — “as low as reasonably "
        "practicable”, a legal concept rather than a technical number. · <em>IPL</em> — an independent "
        "protection layer, countable only if it is specific, independent, dependable and auditable. · "
        "<em>LOPA</em> — the semi-quantitative method that multiplies the PFD of each layer.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Chương này trả lời một câu hỏi nghe như kỹ thuật nhưng thật ra là câu hỏi về giá trị: một nhà máy "
        "phải an toàn tới mức nào, và ai có quyền trả lời? Các tiêu chuẩn hiện đại không quy định công nghệ, "
        "không quy định mức dự phòng, không quy định chu kỳ kiểm tra. Chúng chỉ nói một câu: rủi ro càng lớn "
        "thì hệ an toàn phải càng tốt. Toàn bộ chương này là về chỗ khó nằm trong câu nói ngắn đó — đo rủi ro "
        "thế nào, và chuyển nó thành một con số hiệu năng ra sao."))

    # ---------------------------------------------------------------- 6.1
    b.append(h2("6.1 Giới thiệu", "Introduction"))
    b.append(p("Các tiêu chuẩn về hệ an toàn ngày nay mang tính <em>dựa trên hiệu năng</em> (performance "
               "based) chứ không phải <em>quy định cứng</em> (prescriptive). Chúng không bắt buộc một công "
               "nghệ cụ thể, một mức dự phòng cụ thể, một chu kỳ kiểm tra cụ thể, hay một cấu trúc logic cụ "
               "thể. Về bản chất, chúng chỉ phát biểu một điều: mức rủi ro càng cao thì hệ an toàn dùng để "
               "kiểm soát nó phải càng tốt. Có nhiều phương pháp đánh giá rủi ro, và cũng có nhiều phương "
               "pháp quy đổi rủi ro thành hiệu năng yêu cầu của hệ an toàn. Một thuật ngữ dùng để mô tả hiệu "
               "năng của hệ an toàn là <b>mức toàn vẹn an toàn</b> (safety integrity level, SIL)."))
    b.append(p("Nhiều ngành công nghiệp có nhu cầu đánh giá và xếp hạng rủi ro, để từ đó ban lãnh đạo ra "
               "quyết định giữa các phương án thiết kế. Chẳng hạn: một cơ sở hạt nhân nên cách khu dân cư "
               "lớn bao xa, nếu phải cách? Mức dự phòng nào là phù hợp cho hệ điều khiển vũ khí trên máy bay "
               "quân sự? Cánh tuabin động cơ phản lực phải chịu được lực bao nhiêu để chống chim đâm? Thời "
               "hạn bảo hành nên đặt bao lâu, dựa trên số liệu về suất hỏng đã biết? Lý tưởng nhất là những "
               "quyết định như vậy được đưa ra trên cơ sở phân tích toán học. Thực tế thì việc lượng hoá mọi "
               "yếu tố là cực kỳ khó, nếu không muốn nói là bất khả, và đánh giá chủ quan cùng kinh nghiệm "
               "vẫn có chỗ đứng."))
    b.append(p("Các tổ chức quân sự là một trong những nhóm đầu tiên đối mặt với loại vấn đề này. Khi ai đó "
               "phải bấm nút có thể khởi động hoặc chấm dứt chiến tranh thế giới thứ ba, người ta hẳn muốn "
               "xác suất mạch điện tử hoạt động đúng được xếp vào loại khác chứ không chỉ là “cao”. Quân đội "
               "Hoa Kỳ đã xây dựng một tiêu chuẩn để phân loại rủi ro: MIL-STD 882 “Standard Practice for "
               "System Safety”, và tiêu chuẩn này đã được nhiều tổ chức và ngành khác chuyển thể theo nhiều "
               "hình thức khác nhau. Các nhóm và các quốc gia khác nhau đã nghĩ ra nhiều phương pháp quy đổi "
               "rủi ro thành hiệu năng hệ an toàn; một số mang tính định tính, một số định lượng nhiều hơn."))
    b.append(p("Cần làm rõ SIL <em>là gì</em> và <em>không là gì</em>. SIL là thước đo hiệu năng của một hệ "
               "an toàn. Một hệ gồm cảm biến, bộ xử lý logic và (các) phần tử chấp hành. Vì vậy, nói tới SIL "
               "của một thành phần riêng lẻ trong hệ — ví dụ một bộ xử lý logic đứng một mình — là sai. "
               "Chuỗi chỉ bền bằng mắt yếu nhất của nó. Một bộ xử lý logic có thể được xếp hạng để dùng "
               "trong SIL 3, nhưng nếu nó được nối với các thiết bị trường không dự phòng và ít được kiểm "
               "tra, thì cả hệ có thể chỉ đạt SIL 1."))
    b.append(p("Trong ngành đã có một xu hướng: các nhà cung cấp dùng những thuật ngữ như “giới hạn công bố "
               "SIL” (SIL claim limit) và “năng lực SIL” (SIL capability) để phân biệt giữa hiệu năng của "
               "thành phần và hiệu năng của hệ. Cách nói phù hợp hơn là nói tới <b>xác suất hỏng khi có yêu "
               "cầu</b> (probability of failure on demand, PFD) của từng thành phần. Đáng tiếc là các con số "
               "PFD thường rất nhỏ và phải viết bằng ký hiệu khoa học, nên nhiều người khó hình dung. Và "
               "cũng cần nhớ: SIL không phải thước đo rủi ro của quá trình. Nói “chúng tôi có một quy trình "
               "SIL 3” là sai."))

    # ---------------------------------------------------------------- 6.2
    b.append(h2("6.2 Ai chịu trách nhiệm?", "Who’s Responsible?"))
    b.append(p("Việc xác định SIL được nhắc tới trong các tiêu chuẩn về hệ an toàn. Vì thế nhiều người mặc "
               "định rằng công việc này thuộc về kỹ sư đo lường hay kỹ sư điều khiển. Không phải vậy. Đánh "
               "giá rủi ro quá trình và xác định mức toàn vẹn an toàn phù hợp là trách nhiệm của một "
               "<b>nhóm đa chuyên môn</b>, không phải của bất kỳ cá nhân nào. Kỹ sư điều khiển có thể — và "
               "nên — tham gia, nhưng quá trình soát xét còn cần những chuyên gia khác, điển hình là những "
               "người thường tham gia một nghiên cứu mối nguy và khả năng vận hành (HAZOP)."))
    b.append(p("Một số tổ chức thích xác định SIL ngay trong buổi HAZOP. Số khác cho rằng không cần thiết — "
               "thậm chí không mong muốn — huy động toàn bộ nhóm HAZOP, và việc xác định SIL nên được thực "
               "hiện như một nghiên cứu riêng sau HAZOP. Ở mức tối thiểu, đại diện của các bộ phận sau phải "
               "tham gia vào việc xác định SIL: công nghệ, thiết kế cơ khí, an toàn, vận hành và hệ điều "
               "khiển."))

    # ---------------------------------------------------------------- 6.3
    b.append(h2("6.3 Chọn kỹ thuật nào?", "Which Technique?"))
    b.append(p("Khi nói tới phân tích mối nguy và rủi ro cùng việc xác định mức toàn vẹn an toàn, không có "
               "câu trả lời nào có thể xếp vào loại đúng hay sai. Có nhiều cách đánh giá rủi ro quá trình, "
               "và không cách nào đúng hơn cách nào. Nhiều tài liệu trong ngành mô tả các phương pháp định "
               "tính và định lượng khác nhau để đánh giá rủi ro và xác định hiệu năng SIS [Ref. 2, 3 và 4]. "
               "Các phương pháp này ra đời ở những thời điểm khác nhau, do những quốc gia khác nhau. Tất cả "
               "đều hợp lệ. Đáng tiếc là tất cả cũng có thể cho ra những kết quả khác nhau."))
    b.append(p("Các kỹ thuật định tính dễ áp dụng và nhanh hơn, nhưng kinh nghiệm cho thấy chúng thường cho "
               "kết quả bảo thủ, nghĩa là yêu cầu SIL cao hơn mức cần thiết. Hệ quả là các chức năng an toàn "
               "bị thiết kế thừa, kéo theo những khoản chi phí có lẽ không cần thiết."))
    b.append(p("Các kỹ thuật định lượng đòi hỏi công sức nhiều hơn để xây dựng và sử dụng, nhưng kinh nghiệm "
               "cho thấy chúng thường cho yêu cầu SIL thấp hơn. Chênh lệch chi phí giữa một chức năng SIL 2 "
               "và một chức năng SIL 1 có thể lên tới hàng chục nghìn đô la. Chênh lệch giữa SIL 2 và SIL 3 "
               "còn lớn hơn nữa. Vì vậy, việc dùng các kỹ thuật định lượng chi tiết hơn có thể tiết kiệm "
               "đáng kể."))
    b.append(p("Nói chung, nếu các kỹ thuật định tính cho thấy yêu cầu không vượt quá SIL 1 thì cứ tiếp tục "
               "dùng chúng. Nhưng nếu kết quả định tính cho thấy một tỷ lệ đáng kể các yêu cầu là SIL 2 hoặc "
               "SIL 3, thì nên nghiêm túc cân nhắc dùng các kỹ thuật định lượng hơn, chẳng hạn phân tích các "
               "lớp bảo vệ (layer of protection analysis, LOPA). Khoản tiết kiệm tổng thể thu được — nhất là "
               "khi trải qua nhiều dự án — sẽ dễ dàng biện minh cho công sức xây dựng và sử dụng chúng."))

    # ---------------------------------------------------------------- 6.4
    b.append(h2("6.4 Những vấn đề chung", "Common Issues"))
    b.append(p("Dù chọn phương pháp phân tích rủi ro nào, vẫn có vài yếu tố chung cho tất cả. Chẳng hạn, mọi "
               "phương pháp đều liên quan tới việc đánh giá hai thành phần của rủi ro — xác suất và mức "
               "nghiêm trọng — thường bằng cách phân mỗi thành phần thành nhiều mức khác nhau."))
    b.append(p("Mỗi đơn vị quá trình có những sự kiện nguy hiểm khác nhau, và mỗi sự kiện có mức rủi ro riêng "
               "đi kèm. Lấy ví dụ một bình chứa mà ở đó người ta đo áp suất, nhiệt độ, mức và lưu lượng. Phép "
               "đo áp suất có lẽ nhằm phát hiện và ngăn ngừa tình trạng quá áp dẫn tới nổ; sự kiện này có một "
               "mức rủi ro tương ứng, tức một cặp xác suất – mức nghiêm trọng. Lưu lượng thấp có thể chỉ dẫn "
               "tới việc cháy bơm; sự kiện đó có xác suất và mức nghiêm trọng hoàn toàn khác, nên yêu cầu "
               "SIL cũng khác. Nhiệt độ cao có thể cho ra sản phẩm ngoài chỉ tiêu; điều này cũng có xác suất, "
               "mức nghiêm trọng và yêu cầu SIL hoàn toàn khác."))
    b.append(p("Điều đó có nghĩa là không nên cố xác định SIL cho cả một đơn vị quá trình hay một thiết bị, "
               "mà phải xác định SIL cho <b>từng chức năng an toàn</b>."))

    # ---------------------------------------------------------------- 6.5
    b.append(h2("6.5 Đánh giá rủi ro", "Evaluating Risk"))
    b.append(p("Rủi ro có ở khắp nơi. Làm việc trong một nhà máy hoá chất rõ ràng là có rủi ro, nhưng tắm "
               "cũng vậy. Một bên nhiều rủi ro hơn bên kia, nhưng mọi việc chúng ta làm đều có một mức rủi "
               "ro nào đó."))
    b.append(p("Không có thương tích nào có thể là mục tiêu của nhiều tổ chức, nhưng cần nhận ra rằng không "
               "hề tồn tại khái niệm “rủi ro bằng không”. Ngồi ở nhà xem truyền hình cũng đã là có rủi ro "
               "(nhồi máu cơ tim, lụt, lốc xoáy, động đất…). Vậy một nhà máy chế biến phải an toàn tới mức "
               "nào? Rủi ro khi làm việc trong nhà máy hoá chất có nên ngang với rủi ro khi ở nhà, khi lái "
               "xe, khi đi máy bay, hay khi nhảy dù? Trong điều kiện mọi thứ khác như nhau, nhà máy càng an "
               "toàn thì càng đắt. Đến một điểm nào đó phải có một cân nhắc kinh tế. Nếu mục tiêu an toàn "
               "khiến cho quá trình không thể khởi động được nữa, thì rõ ràng phải thay đổi một cái gì đó."))

    b.append(h3("6.5.1 Mối nguy", "Hazard"))
    b.append(p("Hiệp hội Kỹ sư Hoá học Hoa Kỳ (AIChE) định nghĩa <b>mối nguy</b> là “một đặc tính vật lý hoặc "
               "hoá học vốn có, có khả năng gây hại cho người, tài sản hoặc môi trường. Đó là sự kết hợp của "
               "một vật liệu nguy hiểm, một môi trường vận hành và những sự kiện không lường trước có thể "
               "dẫn tới tai nạn”."))
    b.append(p("Mối nguy luôn hiện diện. Ví dụ, xăng là chất lỏng dễ cháy. Chừng nào chưa có nguồn đánh lửa, "
               "xăng có thể được coi là tương đối vô hại. Mục tiêu của chúng ta là giảm thiểu hoặc loại bỏ "
               "các sự kiện nguy hiểm hay tai nạn — và vì thế chúng ta không cất xăng gần nguồn đánh lửa."))

    b.append(h3("6.5.2 Rủi ro", "Risk"))
    b.append(p("Rủi ro thường được định nghĩa là sự kết hợp giữa <em>mức nghiêm trọng</em> và <em>xác "
               "suất</em> của một sự kiện nguy hiểm. Nói cách khác: nó có thể xảy ra thường xuyên tới mức "
               "nào, và khi xảy ra thì tệ tới mức nào. Rủi ro có thể được đánh giá định tính hoặc định "
               "lượng."))
    b.append(p("Nhiều tiêu chuẩn về hệ an toàn dường như tập trung vào rủi ro cho con người, nhưng con người "
               "không phải là thứ duy nhất gặp rủi ro trong nhà máy chế biến. Chẳng hạn, các giàn khoan xa bờ "
               "không có người vẫn mang một lượng rủi ro đáng kể, dù phần lớn thời gian có thể không có ai "
               "trên giàn. Các yếu tố chịu rủi ro gồm:"))
    b.append(ul([
        "<b>Con người.</b> Cả nhân viên nhà máy lẫn công chúng ở gần.",
        "<b>Thời gian ngừng sản xuất.</b> Tổn thất do không bán được sản phẩm. Đây thường là yếu tố kinh tế "
        "lớn nhất.",
        "<b>Thiết bị vốn.</b> Chi phí thay thế thiết bị hư hỏng.",
        "<b>Môi trường.</b> Làm ô nhiễm nguồn thực phẩm mà nhiều quốc gia cùng sử dụng, hoặc buộc phải sơ "
        "tán một vùng, rõ ràng là điều cần tránh.",
        "<b>Chi phí kiện tụng.</b> Chi phí pháp lý liên quan tới thương tích, tử vong và tổn thất môi "
        "trường có thể rất lớn.",
        "<b>Hình ảnh công ty.</b> Báo chí xấu có thể khiến một công ty phá sản.",
    ]))
    b.append(p("Một số yếu tố trong danh sách trên (như thời gian ngừng sản xuất, thiết bị vốn) có thể lượng "
               "hoá được; một số khác (như hình ảnh công ty) thì khó lượng hoá hơn nhiều."))
    b.append(p("Có thể gán mức hiệu năng cho hệ an toàn dựa trên bất kỳ rủi ro nào ở trên. Chẳng hạn, có "
               "những tổ chức dùng <b>mức toàn vẹn an toàn</b> (SIL) dựa trên rủi ro cho con người, <b>mức "
               "toàn vẹn thương mại</b> (commercial integrity level, CIL) dựa trên các vấn đề kinh tế, và "
               "<b>mức toàn vẹn môi trường</b> (environmental integrity level, EIL) dựa trên các yếu tố môi "
               "trường."))

    b.append(h3("6.5.3 Tỷ lệ tử vong", "Fatality Rates"))
    b.append(p("Rủi ro rõ ràng và nghiêm trọng nhất đối với con người là tử vong. Người làm việc trong hoặc "
               "gần một nhà máy chế biến phải an toàn tới mức nào? Làm việc trong nhà máy chế biến có nên an "
               "toàn ngang với lái xe? Ở Hoa Kỳ có khoảng 45.000 ca tử vong mỗi năm do tai nạn ô tô. Nếu "
               "ngành chế biến có mức rủi ro tương đương thì có nghĩa là ngành này có thể giết 45.000 người "
               "mỗi năm hay sao? Rõ ràng là không! Thứ nhất, số người làm trong nhà máy chế biến không nhiều "
               "như số người lái ô tô. Vấn đề không phải là tổng số ca tử vong, mà là <b>tỷ lệ</b> tử vong."))
    b.append(p("Có hai cách phổ biến để biểu diễn tỷ lệ tử vong. Một là <b>tỷ lệ tai nạn chết người</b> "
               "(fatal accident rate, FAR) — số ca tử vong trên một triệu giờ phơi nhiễm của một người. Hai "
               "là xác suất trên một đơn vị thời gian. Có nhiều nguồn liệt kê tỷ lệ tử vong cho các hoạt động "
               "khác nhau, thuộc nhiều ngành, nhiều phương tiện giao thông và nhiều hoạt động giải trí, bao "
               "gồm cả rủi ro tự nguyện lẫn không tự nguyện. Bảng 6-1 liệt kê tỷ lệ tử vong cho một số hoạt "
               "động tại Vương quốc Anh [Ref. 1]."))
    b.append(eq("FAR = (số ca tử vong / số giờ phơi nhiễm) × 10<sup>8</sup>", "6.1"))
    b.append(p("Cần lưu ý rằng xác suất của hai hoạt động khác nhau có thể bằng nhau, trong khi FAR lại khác "
               "nhau, do số giờ phơi nhiễm khác nhau. Cũng cần lưu ý rằng các con số này đến từ nhiều nguồn "
               "khác nhau và không phải mọi thông tin nền đều sẵn có, nên không phải lúc nào cũng có cách "
               "liên hệ trực tiếp giữa xác suất và tỷ lệ — vì thế một số ô trong bảng 6-1 bị bỏ trống."))
    b.append(table(
        ["Hoạt động", "Xác suất (mỗi năm)", "FAR"],
        [
            ["<b>Đi lại</b>", "", ""],
            ["&nbsp;&nbsp;Máy bay", "2 × 10<sup>−6</sup>", "—"],
            ["&nbsp;&nbsp;Tàu hoả", "2 × 10<sup>−6</sup>", "3 – 5"],
            ["&nbsp;&nbsp;Xe buýt", "2 × 10<sup>−4</sup>", "4"],
            ["&nbsp;&nbsp;Ô tô", "2 × 10<sup>−4</sup>", "50 – 60"],
            ["&nbsp;&nbsp;Mô tô", "2 × 10<sup>−2</sup>", "500 – 1.000"],
            ["<b>Nghề nghiệp</b>", "", ""],
            ["&nbsp;&nbsp;Công nghiệp hoá chất", "5 × 10<sup>−5</sup>", "4"],
            ["&nbsp;&nbsp;Sản xuất chế tạo", "—", "8"],
            ["&nbsp;&nbsp;Hàng hải", "9 × 10<sup>−4</sup>", "8"],
            ["&nbsp;&nbsp;Khai thác than", "2 × 10<sup>−4</sup>", "10"],
            ["&nbsp;&nbsp;Nông nghiệp", "—", "10"],
            ["&nbsp;&nbsp;Quyền Anh", "—", "20.000"],
            ["<b>Tự nguyện</b>", "", ""],
            ["&nbsp;&nbsp;Thuốc tránh thai", "2 × 10<sup>−5</sup>", "—"],
            ["&nbsp;&nbsp;Leo núi", "1,4 × 10<sup>−4</sup>", "4.000"],
            ["&nbsp;&nbsp;Hút thuốc", "5 × 10<sup>−3</sup>", "—"],
            ["<b>Không tự nguyện</b>", "", ""],
            ["&nbsp;&nbsp;Thiên thạch", "6 × 10<sup>−11</sup>", "—"],
            ["&nbsp;&nbsp;Máy bay rơi", "2 × 10<sup>−8</sup>", "—"],
            ["&nbsp;&nbsp;Súng đạn", "2 × 10<sup>−6</sup>", "—"],
            ["&nbsp;&nbsp;Ung thư", "1 × 10<sup>−6</sup>", "—"],
            ["&nbsp;&nbsp;Hoả hoạn", "2,5 × 10<sup>−5</sup>", "—"],
            ["&nbsp;&nbsp;Ngã", "2 × 10<sup>−5</sup>", "—"],
            ["&nbsp;&nbsp;Ở nhà", "1 × 10<sup>−4</sup>", "1 – 4"],
        ],
        caption="Bảng 6-1. Tỷ lệ tai nạn chết người tại Vương quốc Anh [Ref. 1]. Các ô bỏ trống là những "
                "trường hợp nguồn số liệu không đủ để quy đổi giữa xác suất và FAR — hai đại lượng chỉ tương "
                "đương khi biết số giờ phơi nhiễm của từng hoạt động."))

    b.append(h3("6.5.4 Rủi ro vốn có trong xã hội hiện đại", "Risks Inherent in Modern Society"))
    b.append(p("“An toàn” rốt cuộc an toàn tới đâu? Làm việc trong nhà máy có nên có mức rủi ro ngang với "
               "nhảy dù (hoạt động giết khoảng 40 người mỗi năm ở Hoa Kỳ)? Có nên an toàn ngang với lái xe? "
               "Hay nên an toàn ngang với đi máy bay — phương tiện an toàn hơn lái xe hai bậc mười?"))
    b.append(p("Thuật ngữ FAR có thể dễ hiểu và là một thước đo hữu ích, nhưng nhiều công ty, đặc biệt ở Hoa "
               "Kỳ, không sẵn lòng đưa những mục tiêu như vậy ra thành văn bản. Hãy hình dung bước vào sảnh "
               "trụ sở sang trọng của công ty XYZ và thấy trên tường một tấm biển: “Chúng tôi, XYZ, coi việc "
               "4 người chết trên 100 triệu giờ công là mức có thể chấp nhận được.” Các luật sư sẽ có một "
               "ngày hội! Tuy vậy, như sẽ thấy, một số tổ chức đã thiết lập những mục tiêu rủi ro được lượng "
               "hoá như thế."))
    b.append(p("Nhận thức của con người về rủi ro thay đổi tuỳ theo mức hiểu biết và sự quen thuộc với rủi ro "
               "đó. Ví dụ, hầu hết mọi người quen với việc lái xe. Mức rủi ro cảm nhận được là khá thấp với "
               "phần lớn người, dù mỗi năm chỉ riêng ở Hoa Kỳ có khoảng 45.000 người chết vì tai nạn giao "
               "thông. Nếu một cơ sở hoá chất mới được đề xuất xây gần một khu dân cư, mức hiểu biết của cư "
               "dân về quá trình hoá chất có lẽ sẽ thấp, và sự bất an, hay mức rủi ro cảm nhận được của họ, "
               "chắc chắn sẽ cao — kể cả khi quá trình đó có bề dày an toàn rất tốt."))
    b.append(p("Nhận thức về rủi ro cũng thay đổi tỷ lệ với số người có thể chết trong một sự kiện cụ thể. "
               "Trong 45.000 ca tử vong giao thông mỗi năm, các ca thường xảy ra từng người một hoặc vài "
               "người một lần. Dù con số ấy cao đến bất ngờ, hầu như không có tiếng nói công chúng nào đòi "
               "phải làm gì để hạ nó xuống. Nhưng khi một vụ tai nạn liên quan tới xe buýt trường học làm "
               "nhiều trẻ em bị thương, thì thường có tiếng phản đối. Điều tương tự cũng đúng với những môn "
               "thể thao rủi ro cao như nhảy dù, lượn dù, máy bay siêu nhẹ. Dù các môn này có rủi ro tương "
               "đối cao, hiếm khi nghe nói tới nhiều ca tử vong trong cùng một vụ. Những người tham gia cũng "
               "đã tự mình chọn tham gia, và người ngoài thường không bị phơi ra trước rủi ro đó. Tai nạn "
               "trong công nghiệp hoá chất thì ngược lại: thường có nhiều người chết cùng lúc. Bhopal là vụ "
               "tệ nhất cho tới nay, với hơn 3.000 người chết và 200.000 người bị thương. Rủi ro tổng thể "
               "khi làm việc trong một nhà máy hoá chất có thể được chứng minh là thấp hơn rủi ro lái xe (ít "
               "nhất là ở Hoa Kỳ), vậy mà nhận thức của công chúng về hai rủi ro này thường lại đảo ngược."))

    b.append(h3("6.5.5 Rủi ro tự nguyện và không tự nguyện", "Voluntary vs. Involuntary Risk"))
    b.append(p("Có sự khác biệt giữa rủi ro tự nguyện và rủi ro không tự nguyện. Ví dụ về rủi ro tự nguyện: "
               "lái xe, hút thuốc… Ví dụ về rủi ro không tự nguyện: một nhà máy hoá chất được xây gần nhà bạn "
               "sau khi bạn đã sống ở đó nhiều năm, hoặc khói thuốc thụ động từ điếu thuốc của người khác."))
    b.append(p("Người ta có thể nhận thức những rủi ro giống nhau theo cách khác nhau. Ví dụ, gia đình Jones "
               "có một ngôi nhà ở nông thôn. Một ngày kia, công ty XYZ xây một nhà máy hoá chất độc hại gần "
               "đó. Sau khi nhà máy được xây xong, gia đình Smith mua một ngôi nhà cạnh nhà Jones. Cả hai hộ "
               "đối mặt với cùng một rủi ro, nhưng có lẽ mỗi hộ sẽ nhận thức nó khác nhau. Với cặp vợ chồng "
               "thứ nhất (Jones), những người sống ở đó trước khi nhà máy được xây, rủi ro là không tự nguyện "
               "(dù rõ ràng họ có thể chuyển đi). Với cặp thứ hai (Smith), những người mua nhà sau khi nhà "
               "máy đã được xây, rủi ro là tự nguyện."))
    b.append(p("Người ta thường sẵn lòng chấp nhận rủi ro tự nguyện cao hơn rủi ro không tự nguyện. Ví dụ, "
               "khi một trong các tác giả còn trẻ, ông sẵn lòng chấp nhận cả rủi ro đi mô tô trong một thành "
               "phố lớn lẫn rủi ro nhảy dù. Những rủi ro ấy là tự nguyện, và ông tự thấy mình là người duy "
               "nhất gặp rủi ro lúc đó (có thể tranh luận về điểm này). Nay đã là cha có gia đình, ông không "
               "còn muốn chấp nhận những rủi ro đó nữa — chưa nói tới việc ông không còn đủ tiền để theo "
               "đuổi chúng."))
    b.append(p("Một yếu tố khác trong nhận thức rủi ro là <b>sự kiểm soát</b>. Ví dụ, vợ của một trong các "
               "tác giả không thích đi máy bay (thực tế, đi máy bay là nỗi sợ thứ hai của người Mỹ; nói trước "
               "công chúng đứng thứ nhất). Lý do chị nêu ra là chị không cảm thấy mình “kiểm soát được tình "
               "hình”. Nhưng khi bạn ngồi sau vô lăng ở một biển dừng và một người lái xe say rượu đâm thẳng "
               "vào xe bạn, lúc đó bạn cũng đâu có kiểm soát được gì. Suy cho cùng, chẳng ai ra đường với kế "
               "hoạch gây tai nạn."))

    b.append(h3("6.5.6 Mức rủi ro có thể chấp nhận", "Tolerable Levels of Risk"))
    b.append(p("Khái niệm mức rủi ro có thể chấp nhận được không thuần tuý là vấn đề kỹ thuật; nó liên quan "
               "tới triết học, đạo đức và pháp lý. Câu hỏi “an toàn tới đâu là đủ an toàn” không thể trả lời "
               "bằng phương trình đại số hay bằng đánh giá xác suất. Alvin Weinberg gọi những câu hỏi như vậy "
               "là “câu hỏi xuyên khoa học” (transscientific questions), vì chúng vượt ra ngoài phạm vi khoa "
               "học [Ref. 7]."))
    b.append(p("Một vấn đề gây khó khăn là việc ước lượng thống kê những sự kiện cực kỳ ít khả năng. Ước "
               "lượng những sự kiện rất hiếm, như một tai nạn hoá chất nghiêm trọng, không thể có độ tin cậy "
               "như ước lượng cho những trường hợp có sẵn số liệu thống kê dồi dào. Vì các xác suất mong muốn "
               "có thể nhỏ tới mức như 10<sup>−6</sup> mỗi nhà máy mỗi năm, không có cách thực tế nào để xác "
               "định trực tiếp tỷ lệ đó. Không ai có thể xây một vạn nhà máy, vận hành chúng một trăm năm "
               "rồi lập bảng lịch sử vận hành. Nói đơn giản hơn: đo một thứ không hay xảy ra là việc khó."))

    b.append(h3("6.5.7 Rủi ro chấp nhận được trong công nghiệp chế biến",
                "Tolerable Risk in the Process Industries"))
    b.append(p("Người ta thường nhìn rủi ro cá nhân một cách chủ quan, theo trực giác. Nhiều người sẽ không "
               "cân nhắc lái mô tô, dù bạn bè chơi mô tô có nói hay tới đâu. Vợ của tác giả — người không "
               "thích đi máy bay — cho rằng cả nhà lái xe ra sân bay trên cùng một chiếc xe thì được, nhưng "
               "bay trên cùng một chiếc máy bay thì không (dù chị hiểu rằng bay an toàn hơn hai bậc mười). "
               "Logic không phải lúc nào cũng được áp dụng khi đánh giá rủi ro tương đối."))
    b.append(p("Tuy vậy, chúng ta không nên có thái độ chủ quan như thế với rủi ro trong công nghiệp chế "
               "biến. Thông thường, những người ra quyết định về rủi ro (ví dụ kỹ sư) không phải là những "
               "người cuối cùng phải đối mặt với rủi ro (ví dụ công nhân hay cư dân gần đó). Dù không tai nạn "
               "nổi tiếng nào trong ngành chế biến từng được coi là “chấp nhận được”, các công ty liên quan "
               "vẫn không phá sản ngay ngày hôm sau. Vậy là tổn thất hẳn đã được coi là “có thể chịu được”. "
               "Ngành này sẵn lòng coi bao nhiêu tai nạn là có thể chịu được? Phải xảy ra bao nhiêu tai nạn "
               "trước khi có tiếng phản đối của công chúng và chính trị gia?"))
    b.append(p("Chỉ riêng ở Hoa Kỳ có khoảng 2.300 nhà máy hoá dầu. Nếu trung bình mỗi năm một nhà máy gặp "
               "một sự kiện thảm khốc làm hơn 20 người chết — tức rủi ro của một nhà máy là 1/2.300 mỗi năm "
               "— thì bao lâu nữa sẽ có tiếng phản đối và chính phủ can thiệp? Nếu tai nạn như vậy chỉ xảy ra "
               "mười năm một lần (1/23.000 mỗi năm) thì sao? Không có chuyện rủi ro bằng không, nhưng rất khó "
               "quyết định mức nào cụ thể thì được coi là “có thể chịu được”."))
    b.append(p("Các số liệu thống kê liên quan có thể gây nhầm lẫn khá nhiều. Rủi ro cá nhân 1/2.300 mỗi năm "
               "nghĩa là trong 2.300 nhà máy, trung bình mỗi năm có thể có một cái “nổ”. Nhưng cần nhận ra "
               "rằng bạn không thể dự đoán nhà máy nào, và không thể dự đoán khi nào một cái sẽ “nổ”. Vì "
               "người ta không xây 2.300 nhà máy cùng một lúc, cũng không sống cạnh 2.300 nhà máy, họ muốn "
               "biết rủi ro của cái nhà máy duy nhất mà họ gắn với. Rủi ro cho một nhà máy vẫn là 1/2.300 mỗi "
               "năm. Nhưng có người không thấy thoải mái với con số như vậy. Một số người xoay sở một chút và "
               "nói rằng rủi ro tai nạn là “2.300 năm một lần”. Cách nói này còn gây nhầm lẫn hơn. Một số "
               "người rồi suy ra rằng phải 2.300 năm nữa mới có tai nạn, và vì thế họ chẳng có gì phải lo. "
               "Không có gì xa sự thật hơn thế."))
    b.append(p("Ví dụ, khoảng 1 trong 4.000 người ở Hoa Kỳ chết vì tai nạn ô tô mỗi năm. Nếu bạn tới một sự "
               "kiện thể thao có 4.000 người, có thể giả định rằng trong vòng 365 ngày tới sẽ có một người "
               "trong số đó chết vì tai nạn ô tô. Nhưng bạn không thể dự đoán là ai, và không thể dự đoán là "
               "ngày nào. Sai số của việc đảo ngược con số và nói rằng bạn sẽ sống 4.000 năm nữa trước khi "
               "chết vì tai nạn ô tô giờ hẳn đã rõ."))
    b.append(p("Việc quyết định mức rủi ro nào là chấp nhận được có thể so với việc chọn vũ khí trong trò "
               "chơi roulette Nga — bạn muốn khẩu súng có bao nhiêu nòng? Bạn có chọn một khẩu tự động luôn "
               "có đạn trong buồng? (Tôi hy vọng là không, dù đã từng có những người đoạt “giải Darwin” như "
               "vậy!) Hay bạn chọn một khẩu súng lục sáu nòng? Nếu có thể chọn khẩu năm mươi nòng, hoặc năm "
               "nghìn nòng thì sao? Rõ ràng càng nhiều nòng thì rủi ro trúng viên đạn khi bóp cò càng thấp. "
               "Dù thế nào thì bạn vẫn phải chơi trò chơi. Nhưng ít nhất bạn được chọn vũ khí. Không có "
               "chuyện rủi ro bằng không."))
    b.append(p("Một trên 2.300 mỗi năm, hoặc nghịch đảo sai là 2.300 năm giữa hai tai nạn, ban đầu có thể "
               "nghe xa xôi tới mức hầu hết mọi người không bận tâm. Một câu trả lời trực giác hơn ban đầu có "
               "lẽ là năm mươi năm (lý lẽ là một đời làm việc dài năm mươi năm, và người ta không muốn điều "
               "gì xảy ra trong đời mình). Nhưng nhà máy thực sự tồn tại bao lâu? Giả sử 25 năm. Vậy hãy lấy "
               "một khẩu súng năm mươi nòng và mỗi năm bóp cò một lần. Khả năng trúng viên đạn là bao nhiêu? "
               "50 %. (Tuy vậy, dựa trên một bộ giả định và đơn giản hoá khác, câu trả lời là 40 %. Ngay cả "
               "số liệu thống kê liên quan cũng không hiển nhiên!)"))
    b.append(p("Bạn có muốn tên mình nằm trên bản vẽ của một nhà máy nếu biết rằng có 50 % khả năng xảy ra một "
               "tai nạn thảm khốc trong vòng đời của nhà máy? Có lẽ là không."))
    b.append(p("Nếu thay vì năm mươi năm, bạn chọn năm trăm năm thì sao? Khi đó rủi ro sẽ là 25/500, tức 5 %. "
               "Mức đó có nên được coi là chấp nhận được? Còn năm nghìn năm? Khi đó nó thành 0,5 %. Không có "
               "chuyện rủi ro bằng không, nhưng phải thấp tới mức nào thì rủi ro mới được coi là chấp nhận "
               "được? Đó là câu hỏi trị giá 64.000 đô la mà không có câu trả lời khoa học."))
    b.append(note(
        "<b>Ghi chú của người dịch — phép tính khẩu súng.</b> Hình ảnh “nòng súng” ở trên là một cách nói "
        "rất hay, nhưng các con số trong nguyên bản không khớp nhau. Nếu rủi ro là 1/2.300 mỗi năm thì khẩu "
        "súng phải có <b>2.300 nòng</b>, chứ không phải 50; với 25 năm vận hành, khả năng trúng đạn là "
        "25/2.300 ≈ <b>1,1 %</b>, không phải 50 %. Con số 50 trong nguyên bản dường như đến từ “đời làm việc "
        "năm mươi năm” ở câu ngay trước đó, và nó làm kết quả phóng đại lên khoảng 45 lần. Hai phép tính "
        "tiếp theo — 25/500 = 5 % và 25/5.000 = 0,5 % — thì nhất quán với cách lấy số nòng bằng nghịch đảo "
        "của tần suất năm. Còn con số 40 % trong ngoặc không được giải thích ở đâu cả. Giữ nguyên văn để "
        "bạn đối chiếu, nhưng đừng dùng các con số này để thiết kế bất cứ thứ gì."))
    b.append(p("Ngành công nghiệp Hoa Kỳ không thể chịu nổi việc nổ tung cả một nhà máy, với hàng chục người "
               "chết, mỗi năm một lần (1/2.300). Báo chí tiêu cực và phản ứng của công chúng sẽ là thảm "
               "hoạ. Suy cho cùng, OSHA đã can thiệp và ban hành 29 CFR 1910.119 sau khi một loạt tai nạn lớn "
               "xảy ra ở vùng Bờ Vịnh trong khoảng mười năm. Một tai nạn nghiêm trọng mười năm một lần "
               "(1/23.000) có thể được coi là chấp nhận được. Các mục tiêu rủi ro trong khoảng 1/10.000 đã "
               "được ghi nhận trong tài liệu. Thực tế, ở Hà Lan, chính phủ còn công bố tỷ lệ tử vong mà họ "
               "coi là chấp nhận được. Thuỵ Sĩ và Singapore cũng làm vậy. Các tỷ lệ này thường ở mức "
               "1/1.000.000 mỗi năm [Ref. 8]."))

    # ---------------------------------------------------------------- 6.6
    b.append(h2("6.6 Mức toàn vẹn an toàn", "Safety Integrity Levels"))
    b.append(p("Mức rủi ro của quá trình càng cao thì hệ an toàn dùng để kiểm soát nó phải càng tốt. Mức toàn "
               "vẹn an toàn là thước đo hiệu năng của hệ an toàn. Nó <em>không</em> phải thước đo trực tiếp "
               "rủi ro của quá trình."))
    b.append(p("Các tiêu chuẩn và hướng dẫn đã phân thành bốn mức toàn vẹn an toàn. Cần lưu ý rằng các tài "
               "liệu trước đây của ngành chế biến Hoa Kỳ chỉ đi tới SIL 3. Cơ sở của các mục tiêu hiệu năng "
               "nêu trong bảng 6-2 và 6-3 từng là đề tài tranh cãi. Nói cách khác: các bảng này được “hiệu "
               "chuẩn” bằng cách nào? Có lẽ nên dịch các con số lên một hàng, hoặc xuống một hàng? Tại sao "
               "lại bắt đầu từ 90 % mà không phải 80 %? Chỉ có thể nói rằng các bảng này đã được nhiều nhóm "
               "ngành khác nhau chấp nhận và xuất hiện trong mọi tiêu chuẩn."))
    b.append(table(
        ["SIL", "PFD<br><span style='font-weight:400'>xác suất hỏng khi có yêu cầu</span>",
         "Độ khả dụng an toàn<br><span style='font-weight:400'>1 − PFD</span>",
         "Hệ số giảm rủi ro<br><span style='font-weight:400'>1 / PFD</span>"],
        [
            ["<b>4</b>", "0,0001 – 0,00001", "99,99 – 99,999 %", "10.000 – 100.000"],
            ["<b>3</b>", "0,001 – 0,0001", "99,9 – 99,99 %", "1.000 – 10.000"],
            ["<b>2</b>", "0,01 – 0,001", "99 – 99,9 %", "100 – 1.000"],
            ["<b>1</b>", "0,1 – 0,01", "90 – 99 %", "10 – 100"],
        ],
        caption="Bảng 6-2. Mức toàn vẹn an toàn và hiệu năng yêu cầu của hệ an toàn, cho hệ chế độ yêu cầu "
                "thấp (low demand mode). Nguyên bản in các khoảng theo chiều giảm dần; ở đây đảo lại thành "
                "tăng dần cho dễ đọc, giá trị không đổi."))
    b.append(table(
        ["SIL", "Suất hỏng nguy hiểm mỗi giờ"],
        [
            ["<b>4</b>", "≥ 10<sup>−9</sup> và &lt; 10<sup>−8</sup>"],
            ["<b>3</b>", "≥ 10<sup>−8</sup> và &lt; 10<sup>−7</sup>"],
            ["<b>2</b>", "≥ 10<sup>−7</sup> và &lt; 10<sup>−6</sup>"],
            ["<b>1</b>", "≥ 10<sup>−6</sup> và &lt; 10<sup>−5</sup>"],
        ],
        caption="Bảng 6-3. Mức toàn vẹn an toàn và hiệu năng yêu cầu, cho hệ chế độ liên tục (continuous "
                "mode). Ghi chú của nguyên bản: (1) thiết bị trường được tính trong các yêu cầu hiệu năng "
                "trên; (2) xem mục 3.3.2 của sách để thảo luận về chế độ yêu cầu thấp và chế độ liên tục."))
    b.append(p("Mỗi người dùng một thuật ngữ khác nhau để mô tả hiệu năng của hệ. Một thuật ngữ rất phổ biến, "
               "đặc biệt trong giới bán hệ điều khiển, là “độ khả dụng” nói chung. Uỷ ban ISA SP84 cố ý dùng "
               "một thuật ngữ khác, vì các tiêu chuẩn an toàn đang nói tới một loại hiệu năng hoàn toàn khác. "
               "Vấn đề này được bàn kỹ hơn ở chương 8."))
    b.append(p("“Độ khả dụng an toàn” vẫn có thể gây nhầm lẫn vì hầu hết các con số đều quá gần 100 %. Chẳng "
               "hạn, bạn có cho rằng có khác biệt đáng kể giữa 99 % và 99,99 %? Khác biệt đó có thể bị nhìn "
               "như chưa tới 1 %."))
    b.append(p("Phần bù của độ khả dụng an toàn được gọi là <b>xác suất hỏng khi có yêu cầu</b> (PFD). Giờ "
               "thì các con số nhỏ tới mức phải dùng ký hiệu khoa học. Bao nhiêu giám đốc nhà máy sẽ hiểu khi "
               "kỹ sư điều khiển của họ nói rằng chức năng an toàn đo lường của họ có PFD là 4,6 × "
               "10<sup>−3</sup>?"))
    b.append(eq("A<sub>S</sub> + PFD = 1", "6.2"))
    b.append(p("Nghịch đảo của PFD được gọi là <b>hệ số giảm rủi ro</b> (risk reduction factor, RRF). Lợi ích "
               "của thuật ngữ này là chênh lệch giữa các con số dễ thấy hơn. Chẳng hạn, chênh lệch giữa hệ số "
               "giảm rủi ro 100 và 10.000 rõ ràng là hai bậc mười. Thực ra, chênh lệch giữa độ khả dụng an "
               "toàn 99 % và 99,99 % cũng là hai bậc mười, dù ban đầu hầu như không ai nhận ra."))
    b.append(eq("RRF = 1 / PFD", "6.3"))
    b.append(fig(5, F.fig_6_5(), "vi"))
    b.append(p("Các mục sau trình bày những phương pháp khác nhau để xác định mức toàn vẹn an toàn cần thiết "
               "dựa trên các vấn đề rủi ro của quá trình. Các phương pháp này được mô tả trong cả hai tiêu "
               "chuẩn IEC 61508 và IEC 61511, cùng nhiều tài liệu khác. Xin nhớ rằng không phương pháp xác "
               "định SIL nào tốt hơn hay đúng hơn phương pháp nào. Chúng chỉ đơn giản được những nhóm khác "
               "nhau trên thế giới phát triển ở những thời điểm khác nhau. Tương tự, một chiếc Peugeot có lẽ "
               "không tốt hơn một chiếc Ford. Cả hai đều chỉ là ô tô do hai quốc gia khác nhau phát triển. "
               "Chắc chắn lòng tự hào dân tộc sẽ xen vào khi đánh giá từng chiếc, nhưng cả hai đều phục vụ "
               "mục đích của mình tốt như nhau."))

    # ---------------------------------------------------------------- 6.7
    b.append(h2("6.7 Phương pháp 1: Thấp tới mức hợp lý có thể thực hiện được (ALARP)",
                "Method #1: As Low As Reasonably Practicable (ALARP)"))
    b.append(p("Người Anh phát triển lý thuyết ALARP, và nó được coi là một khái niệm pháp lý. Tuy không "
               "phải là một phương pháp xác định mức toàn vẹn an toàn một cách trực tiếp, nó vẫn là một khái "
               "niệm có thể áp dụng trong lĩnh vực này. Ý tưởng xoay quanh ba mức rủi ro tổng thể và kinh tế "
               "của việc hạ thấp rủi ro. Ba mức đó được định nghĩa là “không chấp nhận được”, “chấp nhận "
               "được” và “chấp nhận rộng rãi”, như thể hiện trên hình 6-1."))
    b.append(fig(1, F.fig_6_1(), "vi"))
    b.append(p("Những rủi ro “không chấp nhận được” được nhìn nhận là cao tới mức không thể chịu đựng nổi. "
               "Ví dụ, nếu một phân tích rủi ro cho thấy xác suất phá huỷ một giàn khoan nước sâu lớn có "
               "người ở là một lần mỗi năm, thì khó có khả năng thiết kế đó được triển khai. Phải làm gì đó "
               "để hạ rủi ro xuống mức chịu được hơn, bất kể chi phí."))
    b.append(p("Những rủi ro “chấp nhận rộng rãi” là những rủi ro thấp tới mức không đáng bận tâm. Ví dụ, một "
               "nhà máy lọc dầu hoàn toàn có thể bị thiên thạch đâm trúng, hoặc bị máy bay không kích. Nhưng "
               "xây một hệ thống phòng thủ tên lửa quanh mọi nhà máy chế biến thì khó có thể coi là cần thiết "
               "hay khả thi về kinh tế."))
    b.append(p("Nằm giữa hai thái cực đó là những rủi ro được coi là “chấp nhận được” nếu lợi ích tích cực "
               "được thấy là lớn hơn tác động tiêu cực tiềm tàng. Lái xe là một ví dụ tuyệt vời. Việc khoảng "
               "45.000 người ở Hoa Kỳ chết vì tai nạn ô tô mỗi năm không ngăn được số còn lại trong chúng ta "
               "cầm lái."))
    b.append(p("Dù những quyết định như vậy chủ yếu mang tính kinh tế, các yếu tố khác cũng ảnh hưởng tới "
               "phán đoán của công ty. Ví dụ, không có nhà máy điện hạt nhân nào được xây ở Hoa Kỳ trong hơn "
               "hai thập kỷ. Tương tự, rất ít nhà máy hoá chất xây mới được dựng ở Hoa Kỳ, dù chúng có được "
               "chứng minh an toàn tới đâu, hay các yếu tố kinh tế cho cộng đồng có tích cực tới đâu. Sức "
               "mạnh tổng hợp của phong trào “đừng xây sau vườn nhà tôi” (NIMBY) đã khiến nhiều công ty xây "
               "cơ sở ở nước ngoài, nơi điều kiện công chúng, chính trị, pháp lý và kinh tế thuận lợi hơn."))

    # ---------------------------------------------------------------- 6.8
    b.append(h2("6.8 Phương pháp 2: Ma trận rủi ro", "Method #2: Risk Matrix"))
    b.append(p("Ma trận rủi ro xuất hiện trong nhiều tiêu chuẩn, thực hành được khuyến nghị và quy trình nội "
               "bộ của công ty, và nó có nhiều điểm tương đồng với một tiêu chuẩn quân sự Hoa Kỳ (MIL-STD "
               "882). Cả hai đều phân loại tần suất và mức nghiêm trọng của một sự kiện nguy hiểm bằng nhiều "
               "mức định tính. Tuy vậy, ma trận rủi ro thông dụng trong công nghiệp chế biến thường thêm một "
               "trục thứ ba để tính tới các lớp an toàn bổ sung."))

    b.append(h3("6.8.1 Đánh giá tần suất", "Evaluating the Frequency"))
    b.append(p("Tần suất hay xác suất của một sự kiện có thể được xếp hạng từ thấp tới cao, từ khó xảy ra tới "
               "thường xuyên, hoặc bất kỳ thuật ngữ nào phù hợp. Việc xếp hạng có thể áp cho một hạng mục, "
               "một nhóm hạng mục, một đơn vị quá trình hay cả nhà máy. Các mức có thể được xếp hạng định "
               "tính hoặc định lượng như trong bảng 6-4. Nếu chọn giá trị định lượng, nên để chúng khác nhau "
               "ít nhất một bậc mười, vì các mức toàn vẹn an toàn khác nhau đúng một bậc mười."))
    b.append(table(
        ["Mức", "Từ mô tả", "Tần suất định tính", "Tần suất định lượng"],
        [
            ["<b>5</b>", "Thường xuyên",
             "Hỏng hóc có thể được kỳ vọng một cách hợp lý là xảy ra nhiều hơn một lần trong vòng đời dự "
             "kiến của nhà máy", "Freq &gt; 1/10 mỗi năm"],
            ["<b>4</b>", "Có thể xảy ra",
             "Hỏng hóc có thể được kỳ vọng một cách hợp lý là xảy ra trong vòng đời dự kiến của nhà máy",
             "1/100 &lt; Freq &lt; 1/10 mỗi năm"],
            ["<b>3</b>", "Thỉnh thoảng",
             "Hỏng hóc với xác suất thấp xảy ra trong vòng đời dự kiến của nhà máy",
             "1/1.000 &lt; Freq &lt; 1/100 mỗi năm"],
            ["<b>2</b>", "Xa vời",
             "Một chuỗi hỏng hóc, với xác suất thấp xảy ra trong vòng đời dự kiến của nhà máy",
             "1/10.000 &lt; Freq &lt; 1/1.000 mỗi năm"],
            ["<b>1</b>", "Khó xảy ra",
             "Một chuỗi hỏng hóc, với xác suất rất thấp xảy ra trong vòng đời dự kiến của nhà máy",
             "Freq &lt; 1/10.000 mỗi năm"],
        ],
        caption="Bảng 6-4. Tần suất rủi ro (chỉ là ví dụ)."))

    b.append(h3("6.8.2 Đánh giá mức nghiêm trọng", "Evaluating the Severity"))
    b.append(p("Mức nghiêm trọng cũng có thể được phân loại theo các yếu tố chịu rủi ro khác nhau: con người, "
               "thiết bị vốn, sản xuất… Các con số trong bảng 6-4 và 6-5 chỉ là ví dụ và không nhằm thể hiện, "
               "dù chỉ là ngụ ý, bất kỳ khuyến nghị nào. Các giá trị tiền tệ trong bảng 6-5 cũng chỉ là ví "
               "dụ và cần được “hiệu chuẩn” cho từng tổ chức. Chẳng hạn, một tổn thất tài chính thảm khốc với "
               "tổ chức này có thể là tổn thất khá tầm thường với tổ chức khác."))
    b.append(table(
        ["Mức", "Từ mô tả", "Con người", "Môi trường", "Sản xuất / thiết bị"],
        [
            ["<b>V</b>", "Thảm khốc", "Nhiều người chết",
             "Phát thải ra ngoài cơ sở ở mức gây hại", "Tổn thất &gt; 1,5 triệu USD"],
            ["<b>IV</b>", "Nghiêm trọng", "Một người chết",
             "Phát thải ra ngoài cơ sở ở mức không gây hại", "Tổn thất 1,5 triệu – 500.000 USD"],
            ["<b>III</b>", "Nặng", "Tai nạn gây mất ngày công",
             "Phát thải trong cơ sở, không được cô lập ngay", "Tổn thất 500.000 – 100.000 USD"],
            ["<b>II</b>", "Nhẹ", "Phải điều trị y tế",
             "Phát thải trong cơ sở, được cô lập ngay", "Tổn thất 100.000 – 2.500 USD"],
            ["<b>I</b>", "Không đáng kể", "Chỉ sơ cứu",
             "Không phát thải", "Tổn thất &lt; 2.500 USD"],
        ],
        caption="Bảng 6-5. Mức nghiêm trọng của rủi ro (chỉ là ví dụ)."))

    b.append(h3("6.8.3 Đánh giá rủi ro tổng hợp", "Evaluating the Overall Risk"))
    b.append(p("Hai bộ số sau đó có thể được kết hợp thành một đồ thị hai chiều như bảng 6-6. Góc dưới bên "
               "trái đại diện cho rủi ro thấp (xác suất thấp và tần suất thấp), góc trên bên phải đại diện "
               "cho rủi ro cao (xác suất cao và tần suất cao). Cần lưu ý rằng việc định ra ranh giới giữa các "
               "loại khá chủ quan. Người ta cũng có thể dùng nhiều hơn ba loại tổng thể."))
    b.append(fig(2, F.fig_6_2(), "vi"))
    b.append(p("Các mức rủi ro này tương tự khái niệm ALARP. Nếu xác định được rủi ro cao thì có thể phải "
               "thay đổi quá trình, dù cơ sở là mới hay đã có. Nếu xác định được rủi ro thấp thì có thể "
               "không cần thay đổi gì. Nếu xác định được rủi ro trung bình thì có thể cần thêm lớp an toàn "
               "hoặc thêm quy trình. Cần nhớ rằng đây chỉ là những ví dụ."))

    b.append(h3("6.8.4 Đánh giá hiệu quả của các lớp bổ sung",
                "Evaluating the Effectiveness of Additional Layers"))
    b.append(p("Một trục thứ ba xuất hiện trong nhiều tiêu chuẩn và hướng dẫn, nhưng không có trong tiêu "
               "chuẩn quân sự (xem hình 6-2 của nguyên bản). Trục thứ ba này nhằm tính tới các lớp an toàn "
               "bổ sung thường thấy trong công nghiệp chế biến. Cần lưu ý rằng trục Z được ghi là “số lượng "
               "và/hoặc hiệu quả của các lớp bổ sung”. Điều này nói tới những lớp nằm ngoài hệ thống đo lường "
               "an toàn đang xét trong “sơ đồ củ hành” (xem hình 4-2). Nói cách khác: nếu hệ an toàn đang xét "
               "hỏng, liệu có (những) lớp khác có thể ngăn hoặc giảm nhẹ sự kiện nguy hiểm hay không? Cần lưu "
               "ý rằng hệ điều khiển quá trình cơ bản, các chuông báo và người vận hành đã được mặc định là "
               "có sẵn và không được tính vào trục Z."))
    b.append(p("Ví dụ, nếu đang cân nhắc một hệ điều khiển quá trình dự phòng, có thể cho phép dùng tần "
               "suất/xác suất thấp hơn trên trục X. Về cơ bản điều này có cùng tác dụng tổng thể là hạ thấp "
               "mức toàn vẹn an toàn yêu cầu của hệ an toàn."))
    b.append(fig(3, F.fig_6_3(), "vi"))
    b.append(p("Các con số hiển thị trong các ô của hình 6-2 (nguyên bản) là mức toàn vẹn an toàn và chỉ là "
               "ví dụ. Con số nào được đặt vào ô nào không thống nhất giữa các ngành và cần được từng tổ chức "
               "thống nhất. Ví dụ, các tiêu chuẩn Hoa Kỳ trước đây không công nhận SIL 4. Việc SIL 4 nay đã "
               "được định nghĩa trong các tiêu chuẩn gần đây không nhất thiết có nghĩa là các tổ chức phải sửa "
               "lại những đồ thị cũ, nhất là khi họ thấy mình vốn chẳng có yêu cầu SIL 3 nào."))
    b.append(p("Một khó khăn gắn với hình 6-2 (cũng như bảng 6-4) là các tần suất phải được chọn với giả định "
               "rằng các lớp an toàn <em>không</em> hiện diện. Nếu sự kiện nguy hiểm đang xét là quá áp một "
               "bình chứa dẫn tới nổ, thì hồ sơ lịch sử về các vụ nổ bình chứa vốn đã tính tới các lớp an "
               "toàn như hệ an toàn, van an toàn, đĩa vỡ… Ước lượng tần suất của sự kiện nguy hiểm khi "
               "<em>không</em> có các lớp đó hoá ra lại là một việc khó."))
    b.append(p("Lấy ví dụ, giả sử sự kiện nguy hiểm đang xét là tình trạng quá áp dẫn tới nổ một bình chứa. "
               "Nếu khu vực đó thường có người, có thể sẽ có nhiều người chết, và điều này có thể dẫn tới "
               "mức nghiêm trọng cao nhất. Hồ sơ lịch sử về các vụ nổ bình chứa có thể cho thấy tần suất rất "
               "thấp, dù hồ sơ đó đã tính tới nhiều lớp an toàn khác nhau. Một lần nữa, đây chỉ là ví dụ giả "
               "định. Nếu ngoài hệ thống đo lường an toàn không có lớp an toàn bổ sung nào thì không thể dùng "
               "trục Z. Khi đó kết quả là yêu cầu SIL 3 như trên hình 6-2. Tuy nhiên, nếu có các lớp bổ sung, "
               "chẳng hạn một van an toàn, thì có thể dùng trục Z và hạ yêu cầu thiết kế của hệ an toàn đang "
               "xét từ SIL 3 xuống SIL 2 — tức là đã tính van an toàn như một lớp duy nhất."))
    b.append(p("Cần lưu ý, trục Z cũng có thể dùng để tính tới <em>hiệu quả</em> của các lớp bổ sung. Một phân "
               "tích định lượng về một van an toàn có thể cho thấy nó có hiệu quả tương đương hai lớp. (Khái "
               "niệm này sẽ được trình bày kỹ hơn ở phần phân tích các lớp bảo vệ [LOPA].) Điều đó có nghĩa "
               "là mức toàn vẹn an toàn yêu cầu có thể được hạ từ SIL 3 xuống SIL 1."))
    b.append(p("Một lo ngại khi dùng phương pháp ma trận an toàn này liên quan tới các phán đoán định tính "
               "tham gia vào đó. Mỗi công ty có thể tuỳ ý định nghĩa các mức và cách xếp hạng hơi khác đi. Đại "
               "diện Cơ quan An toàn và Sức khoẻ Nghề nghiệp Hoa Kỳ (OSHA) đã thừa nhận rằng họ không phải "
               "chuyên gia quá trình. Họ sẽ không nói với người dùng rằng lẽ ra phải chọn SIL 3 thay vì SIL 2 "
               "cho một chức năng cụ thể. Họ chỉ muốn thấy dấu vết giấy tờ mà công ty bạn để lại và quá trình "
               "ra quyết định của bạn. Việc các địa điểm khác nhau trong cùng một công ty có thể định nghĩa "
               "mọi thứ khác nhau không thực sự quan trọng (ít nhất là với các tổ chức ban hành tiêu chuẩn), "
               "dù điều đó đương nhiên là nguyên nhân đáng lo. Ngành này đơn giản là chưa đạt được — và có lẽ "
               "sẽ không bao giờ đạt được — sự đồng thuận về mọi phán đoán chủ quan và cách xếp hạng tham gia "
               "vào đó."))
    b.append(p("Có một ý nghĩ đơn giản nhưng khá thô, nên giữ trong đầu suốt quá trình này: “Chúng ta sẽ bảo "
               "vệ quyết định này trước toà án như thế nào?” Nghe có vẻ đáng sợ, nhưng nó tóm gọn vấn đề khá "
               "tốt. Hãy nghĩ mà xem. Nếu xảy ra tai nạn và có người bị thương, vụ việc rất có thể sẽ ra toà. "
               "Ai đó, ở đâu đó, sẽ phải bảo vệ được các quyết định thiết kế của mình. Nếu bị hỏi tại sao lại "
               "ra một quyết định nào đó, và câu trả lời là “À, chúng tôi không chắc nên làm gì, nhưng nhà "
               "cung cấp khuyến nghị như vậy”, thì phản ứng của toà án khó có thể là rộng lượng."))

    # ---------------------------------------------------------------- 6.9
    b.append(h2("6.9 Phương pháp 3: Đồ thị rủi ro", "Method #3: Risk Graph"))
    b.append(p("Người Đức và người Na Uy đã phát triển những kỹ thuật khác nhau nhưng tương tự nhau để xác "
               "định mức toàn vẹn an toàn (xem hình 6-3 của nguyên bản). Cách diễn đạt trong hình được cố ý "
               "để mơ hồ và mở cho nhiều cách hiểu. Mỗi tổ chức cần định nghĩa ranh giới và cách phân loại "
               "chính xác hơn. Các tiêu chuẩn chỉ đang cố trình bày phương pháp luận, chứ không phải một ví dụ "
               "làm việc mà người ta có thể dùng sai."))
    b.append(fig(4, F.fig_6_4(), "vi"))
    b.append(p("Hình 6-3 (nguyên bản) được dành cho rủi ro đối với con người. Có thể xây dựng những đồ thị "
               "tương tự cho rủi ro gắn với thiết bị, tổn thất sản xuất, tác động môi trường…"))
    b.append(p("Người ta bắt đầu từ đầu bên trái của đồ thị. Trước hết: hậu quả đối với những người liên quan "
               "của sự kiện nguy hiểm đang xét là gì? Nếu có bốn người chết thì đó là “vài người chết” hay "
               "“nhiều người chết”? Một lần nữa, mỗi tổ chức được kỳ vọng định nghĩa ranh giới chính xác "
               "hơn."))
    b.append(p("Tiếp theo: tần suất và mức phơi nhiễm của nhân sự trước sự kiện nguy hiểm cụ thể đó là gì? "
               "Cần nhớ rằng dù quá trình có thể liên tục, nhân sự có thể chỉ ở trong khu vực đó 10 phút mỗi "
               "ngày, nên mức phơi nhiễm của họ không liên tục. Cũng nên tính tới việc số người có mặt có thể "
               "tăng lên trong lúc một sự kiện nguy hiểm đang hình thành. Mức phơi nhiễm từ thường xuyên tới "
               "liên tục có lẽ là hiếm. Một ví dụ rõ ràng là sống và làm việc trong một thành phố có nhà máy "
               "điện hạt nhân."))
    b.append(p("Tiếp theo, người ta xét khả năng tránh được tai nạn. Có nhiều yếu tố có thể tính tới ở đây. "
               "Ví dụ: “thời gian an toàn của quá trình” là gì — về bản chất được định nghĩa là thời gian để "
               "một sự kiện nguy hiểm xảy ra nếu mất toàn bộ khả năng kiểm soát? Thời gian phản ứng của quá "
               "trình có đủ chậm để con người hành động, hay động học quá trình nhanh tới mức người vận hành "
               "không thể can thiệp? Người vận hành có chỉ thị tại chỗ để biết chuyện gì đang xảy ra trong quá "
               "trình (để có thể hành động khắc phục)? Nhân sự có được huấn luyện đầy đủ để biết phải làm gì "
               "khi một tình huống bất thường phát triển (để có thể cố ngăn nó)? Các lối thoát có tiếp cận "
               "được để sơ tán khỏi khu vực nếu sự kiện nguy hiểm xảy ra? Ranh giới giữa “đôi khi có thể” và "
               "“gần như không thể” cần được mỗi tổ chức định nghĩa rõ hơn."))
    b.append(p("Cuối cùng, người ta xét xác suất sự kiện thực sự xảy ra, một lần nữa với giả định hệ an toàn "
               "không hiện diện. Điều này chủ yếu liên quan tới các lớp an toàn bổ sung và hồ sơ lịch sử của "
               "những sự cố tương tự. Nói cách khác: xét tất cả các lớp an toàn độc lập khác, khả năng thực "
               "tế để sự kiện cụ thể này xảy ra là bao nhiêu?"))
    b.append(p("Ranh giới giữa “rất nhỏ”, “nhỏ” và “tương đối cao” cần được mỗi tổ chức định nghĩa rõ hơn."))
    b.append(p("Có thể thấy tất cả những điều này khá chủ quan. Người ta cũng có thể đặt câu hỏi về việc hiệu "
               "chuẩn hình 6-3: ai nói rằng đồ thị này cũng không nên được dịch lên hay xuống một hàng? Chắc "
               "chắn người châu Âu đã có một lý lẽ nào đó khi phát triển nó."))

    # ---------------------------------------------------------------- 6.10
    b.append(h2("6.10 Phương pháp 4: Phân tích các lớp bảo vệ (LOPA)",
                "Method #4: Layers of Protection Analysis (LOPA)"))
    b.append(p("Một số kỹ sư không thấy thoải mái với các phương pháp thuần định tính nêu trên để xác định "
               "SIL. Tính lặp lại của các phương pháp này đã bị một số người đặt câu hỏi. Ví dụ, nếu bạn giao "
               "cùng một bài toán cho năm nhóm thiết kế khác nhau, và hai nhóm cho ra SIL 1, hai nhóm cho ra "
               "SIL 2, một nhóm cho ra SIL 3, thì bạn kết luận được gì? Những khác biệt như vậy sẽ dẫn tới "
               "những thiết kế SIS rất khác nhau. Có nhóm nào “đúng” và nhóm nào “sai” không? Thực ra, việc "
               "định nghĩa rõ ranh giới và huấn luyện các nhóm cho đúng sẽ làm cho quá trình xác định nói "
               "chung nhất quán và lặp lại được hơn."))
    b.append(p("Một số người thấy thoải mái hơn với phương pháp định lượng hơn. Ví dụ, nếu công ty bạn không "
               "muốn sự kiện nguy hiểm xảy ra thường xuyên hơn một lần trong một nghìn năm, và kinh nghiệm "
               "cho thấy trung bình mỗi năm có một lần quá trình đòi hỏi hệ an toàn phải hành động, thì việc "
               "xác định hiệu năng yêu cầu của các lớp an toàn là chuyện khá đơn giản."))
    b.append(p("Hai giáo trình của AIChE CCPS mô tả LOPA [Ref. 3 và 5]. Sơ đồ củ hành ở hình 4-2 minh hoạ "
               "cách một nhà máy chế biến nào cũng có nhiều lớp bảo vệ. Mỗi lớp có mức hiệu năng, hay mức "
               "giảm rủi ro, riêng. (Cần lưu ý rằng việc xác định hiệu năng thực tế của một lớp là đề tài của "
               "chương 8.) Nếu biết (a) mục tiêu an toàn tổng thể, tức mức rủi ro chấp nhận được; (b) mức rủi "
               "ro xuất phát, tức tần suất sự kiện khởi phát; (c) có bao nhiêu lớp an toàn đang hiện diện để "
               "ngăn hoặc giảm nhẹ sự kiện; và (d) mức hiệu năng của từng lớp — thì có thể tính và xác định "
               "xem mục tiêu rủi ro tổng thể có đạt được hay không. Khái niệm này tương đối dễ hiểu và được "
               "thể hiện trên hình 4-3. Tuy vậy, việc tìm ra các con số cho tất cả những thứ trên lại là một "
               "thách thức."))

    b.append(h3("6.10.1 Rủi ro chấp nhận được", "Tolerable Risk"))
    b.append(p("Bước đầu tiên là xác định một mức rủi ro chấp nhận được. Chủ đề này đã được bàn ở mục 6.5. "
               "Hệ thống pháp lý Hoa Kỳ khiến việc xác định và ghi thành văn bản những con số như vậy trở nên "
               "khó khăn; tuy vậy, việc đó đã được làm. Ngoài ra, một số chính phủ trên thế giới đã công bố "
               "một con số như vậy để ngành sử dụng. Bảng 6-7 (từ Ref. 5) liệt kê các ví dụ về xác suất tử "
               "vong chấp nhận được hằng năm. Tên các công ty đã được bỏ khỏi bảng này. Có thể xây dựng những "
               "bảng tương tự cho xác suất chấp nhận được của các mức tổn thất khác nhau, do tác động của môi "
               "trường, thời gian ngừng sản xuất, thiết bị vốn và các sự kiện khác."))
    b.append(table(
        ["Tổ chức", "Rủi ro tối đa chấp nhận được<br>cho lực lượng lao động<br>(tất cả kịch bản)",
         "Rủi ro không đáng kể<br>cho lực lượng lao động<br>(tất cả kịch bản)",
         "Rủi ro tối đa chấp nhận được<br>cho công chúng<br>(tất cả kịch bản)",
         "Rủi ro không đáng kể<br>cho công chúng<br>(tất cả kịch bản)"],
        [
            ["Công ty A", "10<sup>−3</sup>", "10<sup>−6</sup>", "—", "—"],
            ["Công ty B", "10<sup>−3</sup>", "10<sup>−6</sup>", "—", "—"],
            ["Công ty C", "3,3 × 10<sup>−5</sup>", "—", "10<sup>−4</sup>", "—"],
            ["Công ty D", "2,5 × 10<sup>−5</sup><br>(mỗi nhân viên)", "—",
             "10<sup>−5</sup>", "10<sup>−7</sup>"],
            ["Điển hình<br>(một kịch bản)", "10<sup>−4</sup>", "10<sup>−6</sup>",
             "10<sup>−4</sup>", "10<sup>−6</sup>"],
        ],
        caption="Bảng 6-7. Xác suất rủi ro chấp nhận được (mẫu). Bốn cột là bốn cách đặt mục tiêu khác nhau: "
                "cho toàn bộ lực lượng lao động hay cho công chúng, và ở mức tối đa chấp nhận được hay ở mức "
                "không đáng kể. Chênh lệch giữa cột thứ nhất và cột thứ hai thường là hai bậc mười — đó chính "
                "là khoảng mà ALARP để mở cho phán đoán."))

    b.append(h3("6.10.2 Tần suất sự kiện khởi phát", "Initiating Event Frequencies"))
    b.append(p("Bước tiếp theo là xác định tần suất hoặc xác suất của sự kiện khởi phát. Đó có thể là sự kiện "
               "bên ngoài (như sét đánh) hoặc hỏng hóc của một trong các lớp (như van của hệ điều khiển hỏng "
               "ở trạng thái mở, dẫn tới hình thành một sự kiện nguy hiểm). Cần xác định con số cho mọi sự "
               "kiện đang được xét. Bảng 6-8 (từ Ref. 5) là một ví dụ. Các con số có thể được xác định dựa "
               "trên hồ sơ lịch sử hoặc số liệu về suất hỏng (một dạng hồ sơ lịch sử)."))
    b.append(table(
        ["Sự kiện khởi phát", "Tần suất (mỗi năm)"],
        [
            ["Vỡ gioăng / bộ đệm làm kín", "1 × 10<sup>−2</sup>"],
            ["Sét đánh", "1 × 10<sup>−3</sup>"],
            ["Hỏng vòng điều khiển quá trình cơ bản (BPCS)", "1 × 10<sup>−1</sup>"],
            ["Van an toàn tự mở", "1 × 10<sup>−2</sup>"],
            ["Hỏng bộ điều áp", "1 × 10<sup>−1</sup>"],
            ["Sai quy trình (mỗi lần có cơ hội)", "1 × 10<sup>−3</sup>"],
            ["Sai sót của người vận hành (mỗi lần có cơ hội)", "1 × 10<sup>−2</sup>"],
        ],
        caption="Bảng 6-8. Tần suất sự kiện khởi phát (mẫu). Hai dòng cuối tính theo <em>cơ hội</em> chứ không "
                "theo năm: một quy trình chỉ có thể bị làm sai khi có người thực hiện nó."))
    b.append(p("Cần lưu ý rằng dù quy trình vận hành và bảo trì có thể được một số người coi là một lớp an "
               "toàn, người ta vẫn thừa nhận rằng sai sót sẽ xảy ra và quy trình sẽ bị vi phạm. Những vấn đề "
               "con người như vậy trong một số trường hợp có thể được coi là sự kiện khởi phát, trong trường "
               "hợp khác lại là lớp ngăn ngừa."))

    b.append(h3("6.10.3 Hiệu năng của từng lớp an toàn", "Performance of Each Safety Layer"))
    b.append(p("Bước tiếp theo là xác định mức hiệu năng của từng lớp an toàn. Có những quy tắc về việc cái gì "
               "có thể được coi là một <b>lớp bảo vệ độc lập</b> (independent protection layer, IPL). Ví dụ:"))
    b.append(ol([
        "<b>Tính chuyên biệt.</b> Một IPL được thiết kế chỉ để ngăn hoặc giảm nhẹ hậu quả của một sự kiện "
        "nguy hiểm tiềm tàng. Nhiều nguyên nhân có thể dẫn tới cùng một sự kiện nguy hiểm. Vì thế, nhiều "
        "kịch bản sự kiện có thể khởi động hành động của một IPL.",
        "<b>Tính độc lập.</b> Một IPL độc lập với các lớp bảo vệ khác gắn với mối nguy đã nhận diện. Hỏng "
        "một lớp sẽ không ngăn được lớp khác làm việc.",
        "<b>Độ tin cậy.</b> Có thể trông cậy vào nó để làm đúng việc nó được thiết kế để làm. Cả chế độ hỏng "
        "ngẫu nhiên lẫn hỏng hệ thống đều được xử lý trong thiết kế.",
        "<b>Tính kiểm toán được.</b> Nó được thiết kế để thuận tiện cho việc thẩm định định kỳ các chức năng "
        "bảo vệ. Việc thử nghiệm chứng minh và/hoặc bảo trì là bắt buộc.",
    ]))
    b.append(p("Bảng 6-9 (từ Ref. 5) là ví dụ về hiệu năng có thể gán cho các mức khác nhau. Các xác suất này "
               "chủ yếu dựa trên suất hỏng và chu kỳ kiểm tra. (Chương 8 trình bày ví dụ về cách tính những "
               "xác suất như vậy.)"))
    b.append(table(
        ["Lớp bảo vệ độc lập", "Xác suất hỏng khi có yêu cầu"],
        [
            ["<b>Lớp bảo vệ độc lập thụ động</b>", ""],
            ["&nbsp;&nbsp;Đê chắn", "1 × 10<sup>−2</sup>"],
            ["&nbsp;&nbsp;Chống cháy (fireproofing)", "1 × 10<sup>−2</sup>"],
            ["&nbsp;&nbsp;Tường chắn nổ / hầm trú ẩn", "1 × 10<sup>−3</sup>"],
            ["&nbsp;&nbsp;Bộ chặn lửa / chặn kích nổ", "1 × 10<sup>−2</sup>"],
            ["<b>Lớp bảo vệ độc lập chủ động</b>", ""],
            ["&nbsp;&nbsp;Van an toàn", "1 × 10<sup>−2</sup>"],
            ["&nbsp;&nbsp;Đĩa vỡ", "1 × 10<sup>−2</sup>"],
            ["&nbsp;&nbsp;Hệ điều khiển quá trình cơ bản (BPCS)", "1 × 10<sup>−1</sup>"],
        ],
        caption="Bảng 6-9. PFD mẫu cho các lớp bảo vệ độc lập khác nhau. Chú ý sự phân biệt giữa thụ động và "
                "chủ động: lớp thụ động không có phần tử chuyển động nên không hỏng vì “không chịu hành động”, "
                "và vì thế đáng tin hơn một bậc mười."))
    b.append(p("Việc coi hành động của con người là một lớp an toàn có thể khó và gây tranh cãi, vì sai sót "
               "của con người được ghi nhận rất rõ. Để tính con người như một lớp an toàn, phải thoả tất cả "
               "các điều kiện sau:"))
    b.append(ul([
        "quy trình dự kiến của họ phải được ghi thành văn bản,",
        "nhân sự phải được huấn luyện về đúng quy trình đó,",
        "nhân sự phải có đủ thời gian để hành động (ví dụ 15 phút),",
        "việc sử dụng quy trình phải được kiểm toán.",
    ]))
    b.append(p("Ngay cả khi đã thoả các điều kiện trên, một giới hạn xác suất (trần) cho sai sót của con "
               "người ở mức 1 × 10<sup>−1</sup> là hợp lý. Nói cách khác, khẳng định rằng một người sẽ phản "
               "ứng đúng trong một tình huống khẩn cấp áp lực cao với tỷ lệ tốt hơn 9 trên 10 lần (dù đã thoả "
               "cả bốn điều kiện trên) có thể bị coi là không thực tế. Để đưa ra khẳng định như vậy sẽ cần "
               "dùng những kỹ thuật chuyên biệt để đánh giá độ tin cậy của con người, và những kỹ thuật đó "
               "hiếm khi được dùng trong công nghiệp chế biến."))
    b.append(p("Bảng 6-9 rõ ràng chỉ là danh sách một phần các lớp an toàn thụ động và chủ động tiềm năng. Hệ "
               "báo cháy và khí có thể là một trong các lớp an toàn và có thể được lượng hoá hiệu năng (đó là "
               "đề tài của chương 8). Trong nhiều trường hợp, hiệu năng của hệ báo cháy và khí sẽ bị giới hạn "
               "ở mức PFD khoảng 1 × 10<sup>−1</sup>. Nếu hệ báo cháy và khí được coi là một hệ an toàn và "
               "được gán một mức toàn vẹn (theo các quy trình nêu trong chương này), thì yêu cầu hiệu năng "
               "(PFD) của nó có thể phải cao hơn đáng kể."))

    b.append(h3("6.10.4 Ví dụ dùng LOPA", "Example Using LOPA"))
    b.append(p("Ví dụ sau là một biến thể nhỏ của một ví dụ trong tài liệu tham khảo 5. Hình 6-4 (nguyên bản) "
               "trình bày quá trình mẫu. Một bình chứa được dùng để chứa hexane, một chất dễ cháy. Mức trong "
               "bình được điều khiển bằng một bộ điều khiển mức tác động lên một van. Nếu bình đầy quá, "
               "hexane sẽ thoát ra qua một ống thông hơi và được giữ lại trong một đê chắn. Một phân tích mối "
               "nguy đã được thực hiện và xác định rằng bộ điều khiển mức có thể hỏng, chất lỏng có thể thoát "
               "ra ngoài đê, một nguồn đánh lửa có thể đốt cháy hexane, và có thể có người tử vong. Tổ chức "
               "muốn xác định liệu cơ sở hiện hữu có đáp ứng tiêu chí rủi ro của công ty hay không, và nếu cần "
               "thay đổi (chẳng hạn thêm một hệ an toàn độc lập) thì phải thay đổi tới mức nào."))
    b.append(fig(6, F.fig_6_6(), "vi"))
    b.append(p("Tổ chức đặt ra giới hạn rủi ro chấp nhận được hằng năm cho một đám cháy là 10<sup>−4</sup> và "
               "cho một ca tử vong là 10<sup>−5</sup>. Sự kiện khởi phát của kịch bản này là hỏng hệ điều "
               "khiển, được ước lượng là 10<sup>−1</sup>. Lớp an toàn duy nhất hiện có là đê chắn, với PFD "
               "ước lượng 10<sup>−2</sup>."))
    b.append(p("Chuông báo và hành động của người vận hành không được tính tới, vì trong trường hợp này chính "
               "hệ điều khiển là sự kiện khởi phát, nên sẽ không có chuông báo nào được phát ra. Tổ chức chọn "
               "quan điểm bảo thủ rằng nếu vật liệu thoát ra ngoài đê thì khả năng nó tìm được nguồn đánh lửa "
               "là 100 %. Tuy nhiên, khu vực này không phải lúc nào cũng có người. Xác suất có người trong "
               "khu vực được ước lượng là 50 %. Xác suất người trong khu vực thực sự bị chết bởi đám cháy "
               "(chứ không chỉ bị thương) được ước lượng là 50 %."))
    b.append(fig(7, F.fig_6_7(), "vi"))
    b.append(p("Hình 6-5 (nguyên bản) trình bày cây sự kiện cho kịch bản này. Xác suất xảy ra đám cháy được "
               "biểu diễn bằng tích các xác suất của ba hàng dưới cùng, tức 10<sup>−3</sup> (0,1 × 0,01 × "
               "1,0). Xác suất tử vong được biểu diễn bằng hàng cuối cùng, tức 2,5 × 10<sup>−4</sup> "
               "(0,1 × 0,01 × 1,0 × 0,5 × 0,5)."))
    b.append(eq("F<sub>cháy</sub> = 0,1 × 0,01 × 1,0 = 1 × 10<sup>−3</sup> / năm", "6.4"))
    b.append(eq("F<sub>tử vong</sub> = 0,1 × 0,01 × 1,0 × 0,5 × 0,5 = 2,5 × 10<sup>−4</sup> / năm", "6.5"))
    b.append(p("Biết rằng mục tiêu rủi ro của công ty cho một đám cháy là 10<sup>−4</sup>, có thể thấy mục "
               "tiêu này đang bị vượt quá 10 lần (10<sup>−3</sup> / 10<sup>−4</sup>). Biết rằng mục tiêu rủi "
               "ro cho một ca tử vong là 10<sup>−5</sup>, có thể thấy mục tiêu đang bị vượt quá 25 lần "
               "(2,5 × 10<sup>−4</sup> / 10<sup>−5</sup>). Vì vậy, thiết kế hiện tại không đạt cả hai mục tiêu "
               "rủi ro của công ty và cần phải thay đổi. Một giải pháp khả dĩ là lắp một chức năng dừng mức "
               "cao riêng. Chức năng như vậy sẽ phải giảm rủi ro ít nhất 25 lần để đạt tiêu chí tổng thể. Một "
               "hệ số giảm rủi ro (RRF) bằng 25 nằm trong dải SIL 1 (10 – 100) như bảng 6-2. Tuy nhiên, rõ "
               "ràng không phải bất kỳ hệ SIL 1 nào cũng đủ. Hệ mới phải đạt hệ số giảm rủi ro ít nhất là 25."))
    b.append(eq("RRF<sub>cần</sub> = F<sub>chưa giảm</sub> / F<sub>mục tiêu</sub> = 2,5×10<sup>−4</sup> / "
                "10<sup>−5</sup> = 25", "6.6"))
    b.append(p("Hình 6-6 (nguyên bản) trình bày một phiếu làm việc mẫu để ghi lại kịch bản này. Ở đây nó được "
               "trình bày dưới dạng bảng 6-10, vì một phiếu làm việc vốn là một bảng chứ không phải một hình "
               "vẽ."))
    b.append(table(
        ["Trường", "Nội dung"],
        [
            ["Số kịch bản", "—"],
            ["Số thiết bị", "—"],
            ["Tên kịch bản",
             "Tràn bồn chứa đệm hexane. Chất lỏng tràn không được đê giữ lại."],
            ["Mô tả",
             "Hexane thoát ra ngoài đê do bồn tràn và đê hỏng, có khả năng bắt lửa và gây tử vong."],
            ["Mục tiêu rủi ro<br>(loại hoặc tần suất)",
             "Rủi ro tối đa chấp nhận được của một đám cháy nghiêm trọng: &lt; 1 × 10<sup>−4</sup><br>"
             "Rủi ro tối đa chấp nhận được của một ca tử vong: &lt; 1 × 10<sup>−5</sup>"],
            ["Sự kiện khởi phát<br>(thường là tần suất)", "Hỏng vòng điều khiển BPCS: 1 × 10<sup>−1</sup>"],
            ["Sự kiện tạo điều kiện", "Không áp dụng"],
            ["Yếu tố điều kiện<br>Xác suất có nguồn đánh lửa", "1"],
            ["Yếu tố điều kiện<br>Xác suất có người trong khu vực", "0,5"],
            ["Yếu tố điều kiện<br>Xác suất tử vong", "0,5"],
            ["Khác", "Không áp dụng"],
            ["Tần suất của hậu quả<br>khi chưa có lớp giảm nhẹ", "2,5 × 10<sup>−2</sup>"],
        ],
        caption="Bảng 6-10. Phiếu làm việc LOPA mẫu cho kịch bản hexane. Chú ý rằng “tần suất của hậu quả khi "
                "chưa có lớp giảm nhẹ” ở đây là 2,5 × 10<sup>−2</sup>, tức đã tính đê chắn nhưng chưa tính lớp "
                "bảo vệ nào sẽ được thêm vào — đó chính là con số mà RRF phải chia xuống."))
    b.append(note(
        "<b>Ghi chú của người dịch — bốn con số cần kiểm lại.</b> "
        "(1) <b>Phép nhân trong LOPA khớp.</b> 0,1 × 0,01 × 1,0 = 10<sup>−3</sup> cho đám cháy, và nhân thêm "
        "0,5 × 0,5 được 2,5 × 10<sup>−4</sup> cho tử vong; so với hai mục tiêu 10<sup>−4</sup> và "
        "10<sup>−5</sup>, thiếu đúng 10 lần và 25 lần, nên RRF ≥ 25 và rơi vào dải SIL 1. "
        "(2) <b>Đánh số mục bị lệch.</b> Nguyên bản gọi mục 6.9 là “Method #2: Risk Graph”, nhưng mục 6.8 đã "
        "là “Method #2: Risk Matrix” rồi; mục lục của sách lại ghi 6.9 là “Method #3”. Tương tự, mục 6.10 "
        "mang số “Method #3” trong đề mục nhưng “Method #4” trong mục lục. Ở bản dịch này các mục được đánh "
        "số 1–4 theo đúng mục lục. "
        "(3) <b>Hình bị đánh số lại.</b> Nguyên bản có sáu hình; bản dịch có bảy, vì thêm hình 6-5 (bốn dải "
        "SIL trên trục PFD) để minh hoạ bảng 6-2, và đổi phiếu làm việc LOPA thành bảng 6-10. Vì vậy hình "
        "6-4, 6-5 của nguyên bản tương ứng với hình 6-6, 6-7 ở đây. "
        "(4) <b>Bảng 6-1 có ô trống</b> — không phải lỗi in, mà vì xác suất và FAR chỉ quy đổi được cho nhau "
        "khi biết số giờ phơi nhiễm, và nguồn số liệu gốc không có đủ thông tin đó."))

    # ---------------------------------------------------------------- Tóm tắt
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Nhiều ngành có nhu cầu đánh giá và xếp hạng rủi ro, rồi gắn nó với hiệu năng của hệ an toàn. Có "
               "nhiều kỹ thuật, từ định tính tới định lượng. Mọi phương pháp đều liên quan tới việc đánh giá "
               "ít nhất hai thành phần của rủi ro: xác suất và mức nghiêm trọng. Không phương pháp nào chính "
               "xác hơn hay tốt hơn phương pháp nào. Tất cả đều là những kỹ thuật hợp lệ, được phát triển ở "
               "những quốc gia khác nhau vào những thời điểm khác nhau."))
    b.append(p("Công việc thực hiện phân tích mối nguy và rủi ro cùng việc gắn rủi ro với hiệu năng của hệ an "
               "toàn không chỉ thuộc về kỹ sư đo lường hay kỹ sư hệ điều khiển. Đó là công việc mà một nhóm đa "
               "chuyên môn phải thực hiện. Và người ta xác định SIL cho <b>từng chức năng an toàn đo lường</b> "
               "(SIF). Nói tới SIL của cả một đơn vị quá trình hay một thiết bị là sai."))
    b.append(quote("“Người khăng khăng đòi nhìn cho thật rõ ràng trước khi quyết định thì sẽ không bao giờ "
                   "quyết định.”", "H. F. Amiel"))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "This chapter is about a number that cannot be measured directly, chosen by a committee, defended in "
        "court, and then used to size a safety system. Everything in it — the fatality statistics, the "
        "matrices, the risk graphs, the LOPA arithmetic — is scaffolding around one uncomfortable fact: the "
        "tolerable level of risk is a decision, not a measurement. The engineering starts after the decision "
        "has been made."))

    b.append(h2("The number the standard will not give you"))
    b.append(p("A performance-based standard tells you that greater risk demands a better safety system. It "
               "does not tell you what “greater” means, what “better” means, or where the line sits. That "
               "abstention is deliberate and it is also the source of most of the difficulty in this "
               "chapter. A prescriptive standard can be checked: the valve is either redundant or it is "
               "not. A performance standard has to be interpreted, and interpretation needs a starting "
               "point — a tolerable risk target — that no standard supplies."))
    b.append(p("So the first task in any SIL determination is not technical at all. It is to find out what "
               "target the organisation has already committed to, in writing, somewhere else: a corporate "
               "risk matrix, a jurisdiction's published fatality rate, an insurance condition. If no such "
               "target exists, the team is not doing a SIL study. It is inventing policy, and it should say "
               "so before it starts, because the number it invents will be quoted back at it for the life "
               "of the plant."))

    b.append(h2("Why the statistics in section 6.5.7 feel wrong and are still useful"))
    b.append(p("The Russian roulette passage is the most quoted part of the chapter and also the least "
               "reliable arithmetically — the barrel count does not match the annual rate it is supposed to "
               "represent, and the parenthetical 40 % is never derived. But the passage earns its place "
               "because it demonstrates something the arithmetic obscures: a rate and a probability are "
               "different objects, and the public, the regulator and the lawyer all reason in the second "
               "while the engineer computes in the first."))
    b.append(p("One in 2,300 per year is not “safe for 2,300 years”. It is a 25-in-2,300 chance over a "
               "twenty-five year plant life — about 1 %. The reciprocal is a unit error that survives "
               "because it is rhetorically convenient: it turns a small but real probability into an "
               "apparently infinite deferral. Any safety case that uses the reciprocal form should be read "
               "as advocacy rather than analysis."))

    b.append(h2("Three ways to reach the same SIL, and why that is not a scandal"))
    b.append(p("The chapter presents ALARP, a risk matrix, a risk graph and LOPA as four methods, and then "
               "says plainly that none is more correct than another. Engineers find this unsatisfying. It "
               "is worth being precise about why the situation is tolerable. The methods do not disagree "
               "about physics; they disagree about how much resolution to buy. A qualitative matrix collapses "
               "a continuous frequency axis into five boxes and therefore rounds upwards, because rounding "
               "up is the safe direction. LOPA keeps the axis continuous and therefore rounds less. The "
               "difference between a SIL 2 and a SIL 1 answer is usually the difference between two "
               "resolutions, not between two truths."))
    b.append(p("What matters is that the method is fixed before the answers are known, applied consistently "
               "across the plant, and documented well enough that a second team would reach the same box. A "
               "site that uses a matrix for one unit and LOPA for the next has not bought accuracy; it has "
               "bought an inconsistency that will be very hard to defend when the two units are compared."))

    b.append(h2("The third axis is where the argument actually happens"))
    b.append(p("Adding a Z axis for “quantity and/or effectiveness of additional layers” is presented as a "
               "refinement of the risk matrix. In practice it is the whole negotiation. Every claim that a "
               "relief valve, a dike, a blast wall or a trained operator counts as a layer lowers the SIL "
               "requirement, and every such claim is a claim about independence that nobody can verify "
               "quantitatively."))
    b.append(p("The four IPL criteria — specificity, independence, dependability, auditability — are the "
               "discipline that keeps the negotiation honest. Independence is the one that fails most "
               "often, and it fails quietly. A relief valve sharing a nozzle with the instrument tapping is "
               "not independent of the pressure transmitter. A dike that is also the bund for the adjacent "
               "tank is not specific to this scenario. Neither failure shows up on a P&ID; both are found "
               "only by walking the plant."))

    b.append(h2("The human layer has a ceiling, and the ceiling is low"))
    b.append(p("Section 6.10.3 is unusually blunt: even with documented procedures, trained personnel, "
               "fifteen minutes to act and an audited compliance record, a probability cap of 1 × 10⁻¹ is "
               "the most that may be claimed for a human response. Nine times out of ten, in an emergency, "
               "under stress. Anyone who has watched an operator respond to a real trip will recognise the "
               "number as generous rather than conservative."))
    b.append(p("The consequence is structural. A human layer can never deliver better than one decade of "
               "risk reduction, which means it can never on its own satisfy a SIL 2 requirement. This is "
               "the arithmetic reason behind a design rule that is often stated as a preference: if the "
               "hazard needs more than one order of magnitude, an instrumented function has to do the work, "
               "and the operator is there to back it up rather than to carry it."))

    b.append(h2("LOPA is arithmetic, and arithmetic is auditable"))
    b.append(p("The worked example is worth reading as a template rather than a case. Four numbers, three "
               "multiplications, two comparisons: 10⁻³ against a 10⁻⁴ target, 2.5 × 10⁻⁴ against 10⁻⁵. The "
               "shortfalls are ten and twenty-five, the binding one is twenty-five, and twenty-five sits "
               "inside the SIL 1 band. Nothing in that chain is a judgement call except the inputs — and "
               "the inputs are exactly where the study earns or loses its value."))
    b.append(p("Note what the example does with the operator. Alarms and operator action are excluded "
               "because the control system is itself the initiating event, so no alarm would be generated. "
               "That single sentence is the difference between an honest LOPA and a flattering one. It is "
               "always possible to add a layer and lower the answer; it is only sometimes true that the "
               "layer would still be there when the demand arrives."))

    b.append(h2("SIL is a property of a loop, never of a box"))
    b.append(p("The distinction the chapter insists on — that a logic solver may be rated for SIL 3 while "
               "the loop it sits in achieves SIL 1 — is the one most often lost in procurement. Vendors "
               "sell SIL capability; systems achieve SIL. A transmitter with a certified failure rate, "
               "wired to a certified solver, driving a valve that is stroked once every five years, is a "
               "SIL 1 loop with three SIL 3 certificates attached to it."))
    b.append(p("This is why the phrase “we have a SIL 3 plant” is not merely imprecise but misleading: it "
               "suggests a property of the facility when the property belongs to individual functions, "
               "each with its own demand rate, its own proof-test interval and its own weak link. The "
               "correct unit of conversation is the safety instrumented function, and the correct question "
               "is not what it is rated for but what it will actually do on the day it is needed."))
    return "\n".join(b)
