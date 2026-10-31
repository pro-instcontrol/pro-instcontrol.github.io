# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 7, Choosing a Technology
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

import sis07fig as F

PAGES_SRC = 20
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>PLC (bộ điều khiển logic khả trình)</em> — máy tính công nghiệp chạy chương trình quét "
            "vòng; ra đời năm 1969 để thay rơ-le. · "
            "<em>Chẩn đoán (diagnostics)</em> — phần mềm và mạch tự kiểm để phát hiện hỏng hóc mà mắt "
            "người không thấy. · "
            "<em>Độ phủ chẩn đoán (DC)</em> — tỷ lệ hỏng hóc mà hệ tự phát hiện được. · "
            "<em>FMEDA</em> — phân tích chế độ hỏng, ảnh hưởng và chẩn đoán: bảng liệt kê từng linh kiện, "
            "từng cách hỏng, suất hỏng và có tự phát hiện được không. · "
            "<em>TMR</em> — ba kênh dự phòng, bỏ phiếu 2 trên 3. · "
            "<em>1oo2D</em> — hai kênh, mỗi kênh tự chẩn đoán, một kênh đã đủ tác động. · "
            "<em>Đã qua sử dụng (prior use)</em> — căn cứ thay thế cho chứng nhận: dựa trên số liệu hỏng "
            "hóc thực tế của chính người dùng.")
    return note(
        "<b>Key terms.</b> <em>PLC</em> — the industrial computer that scans a program in a loop, invented "
        "in 1969 to replace relays. · <em>Diagnostics</em> — the self-test circuits and software that find "
        "failures the eye cannot see. · <em>Diagnostic coverage</em> — the fraction of failures the system "
        "detects on its own. · <em>FMEDA</em> — failure modes, effects and diagnostic analysis: a table of "
        "every component, every way it fails, its failure rate, and whether that failure is detectable. · "
        "<em>TMR</em> — three redundant channels voting two-out-of-three. · <em>1oo2D</em> — two channels, "
        "each self-diagnosing, either one sufficient to act. · <em>Prior use</em> — the evidence route "
        "that substitutes for certification, built on the user's own failure history.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Có bốn công nghệ để làm một hệ dừng khẩn: khí nén, rơ-le điện cơ, bán dẫn rắn và PLC. Không có "
        "công nghệ nào tốt nhất nói chung — cũng như không có chiếc ô tô nào tốt nhất nói chung, dù các "
        "nhà cung cấp có nói gì đi nữa. Câu hỏi đúng không phải “cái nào tốt nhất” mà “cái nào phù hợp "
        "nhất”, và câu trả lời phụ thuộc vào ngân sách, quy mô, mức rủi ro, độ phức tạp, khả năng bảo trì, "
        "yêu cầu giao tiếp và cả mức độ an ninh mà bạn cần."))

    # ---------------------------------------------------------------- 7.1
    b.append(h2("7.1 Hệ khí nén", "Pneumatic Systems"))
    b.append(p("Hệ khí nén vẫn đang được dùng và hoàn toàn phù hợp với một số ứng dụng nhất định. Một ứng "
               "dụng rất phổ biến của hệ khí nén là ngành dầu khí ngoài khơi, nơi hệ thống phải làm việc mà "
               "không có điện. Hệ khí nén tương đối đơn giản (với điều kiện là nhỏ) và tương đối an toàn "
               "khi hỏng. “An toàn khi hỏng” ở đây nghĩa là một hỏng hóc hay rò rỉ thường sẽ làm hệ mất áp, "
               "và việc mất áp sẽ khởi động một lệnh dừng."))
    b.append(p("Khí sạch và khô thường là điều kiện bắt buộc. Nếu bụi hút ẩm từ bộ sấy khí dụng cụ, hoặc "
               "hơi ẩm do việc sấy và lọc không hiệu quả, lọt vào hệ, thì các cửa nhỏ và lỗ xả dùng trong "
               "mạch khí sẽ dễ bị tắc và kẹt. Điều đó làm cho mạch dễ gặp những hỏng hóc <em>nguy hiểm</em> "
               "hơn — loại hỏng mà hệ không hành động khi được yêu cầu. Việc vận hành và/hoặc kiểm tra "
               "thường xuyên thường là cần thiết để các bộ phận không bị kẹt. Các nhà vận hành ngoài khơi ở "
               "vùng Vịnh Mexico của Hoa Kỳ được yêu cầu kiểm tra hệ an toàn khí nén hằng tháng chính vì lý "
               "do này. Hệ khí nén thường được dùng trong các ứng dụng nhỏ, nơi người ta muốn sự đơn giản, "
               "an toàn nội tại và không có điện lưới."))

    # ---------------------------------------------------------------- 7.2
    b.append(h2("7.2 Hệ rơ-le", "Relay Systems"))
    b.append(p("Hệ rơ-le có một số ưu điểm:"))
    b.append(ul([
        "Đơn giản (ít nhất là khi nhỏ);",
        "Chi phí vốn thấp;",
        "Miễn nhiễm với hầu hết các dạng nhiễu điện từ và nhiễu tần số vô tuyến (EMI/RFI);",
        "Có sẵn cho nhiều dải điện áp khác nhau;",
        "Thời gian đáp ứng nhanh (không quét vòng như PLC);",
        "Không có phần mềm — điều mà nhiều người vẫn còn e ngại;",
        "An toàn khi hỏng.",
    ]))
    b.append(p("“An toàn khi hỏng” nghĩa là chế độ hỏng đã biết và dự đoán được (thường là mạch đóng và có "
               "điện sẽ hỏng thành hở và mất điện). Tuy vậy, không có gì an toàn khi hỏng 100 %. Có những "
               "rơ-le an toàn đạt mức hoạt động an toàn khi hỏng trên 99,9 %."))
    b.append(p("Hệ rơ-le cũng có một số nhược điểm:"))
    b.append(ul([
        "<b>Dừng nhầm.</b> Hệ rơ-le thường không dự phòng, nghĩa là chỉ một rơ-le hỏng đã có thể làm quá "
        "trình dừng nhầm. Điều này ảnh hưởng đáng kể tới chi phí vận hành chung.",
        "<b>Hệ lớn thì phức tạp.</b> Hệ rơ-le càng lớn càng khó điều khiển. Một hệ 10 điểm vào/ra thì còn "
        "quản lý được. Một hệ 700 điểm vào/ra thì không. Một người dùng kể cho một trong các tác giả nghe "
        "những rắc rối với hệ rơ-le 700 điểm của họ. Có một mạch gồm: một cảm biến khí nén, nối tới một "
        "công tắc điện, nối tới một PLC, nối tới một vệ tinh (thật đấy!), nối tới một DCS, nối tới bảng "
        "rơ-le, rồi lại đi ngược ra. (Rõ ràng đây không phải một hệ rơ-le điển hình!) Vị kỹ sư nói rằng "
        "giữa cảm biến và phần tử chấp hành có tới 57 lần chuyển tiếp tín hiệu. Tác giả hỏi: “Anh nghĩ khả "
        "năng nó thực sự làm việc đúng khi cần là bao nhiêu?”. Câu trả lời: “Không. Chúng tôi biết là nó "
        "sẽ không chạy.” Hỏi thêm thì vị kỹ sư thừa nhận: “Ai trong nhà máy này cũng biết: ‘Đừng có lại "
        "gần cái tủ đó!’ Chỉ cần mở cửa tủ ra là đã có thể gây dừng nhầm rồi!”",
        "<b>Sửa dây và sửa bản vẽ bằng tay.</b> Mỗi khi cần thay đổi logic trong một hệ đấu dây cứng, phải "
        "sửa dây thật và phải cập nhật bản vẽ bằng tay. Giữ bản vẽ luôn đúng đòi hỏi kỷ luật chặt và việc "
        "thực thi quy trình nghiêm túc. Nếu bạn có một tủ rơ-le đã hơn mười năm, hãy thử phép thử đơn giản "
        "này: lấy bộ bản vẽ logic kỹ thuật ra, đi tới tủ, và xem hai thứ có thực sự khớp nhau không. Có thể "
        "bạn sẽ hơi bất ngờ!",
        "<b>Không truyền thông nối tiếp.</b> Hệ rơ-le không cung cấp bất kỳ hình thức liên lạc nào với hệ "
        "khác (ngoài việc lặp tiếp điểm). Về cơ bản, chúng điếc, câm và mù.",
        "<b>Không có sẵn phương tiện kiểm tra hay bỏ qua.</b> Hệ rơ-le không có các tính năng tiêu chuẩn để "
        "kiểm tra hay để bỏ qua (bypass). Có thể thêm vào, nhưng kích thước, độ phức tạp và chi phí của tủ "
        "sẽ tăng lên đáng kể.",
        "<b>Chỉ tín hiệu rời rạc.</b> Hệ rơ-le dựa trên tín hiệu logic rời rạc (đóng/ngắt). Theo truyền "
        "thống, người ta dùng cảm biến vào rời rạc (tức công tắc). Có thể đưa tín hiệu tương tự (4–20 mA) "
        "vào bằng bộ khuếch đại ngưỡng, thứ cho ra một đầu ra rời rạc khi tín hiệu tương tự vượt ngưỡng "
        "đặt. Tuy vậy, bộ khuếch đại ngưỡng không có đặc tính an toàn khi hỏng vốn có như rơ-le.",
    ]))
    b.append(p("Hệ rơ-le thường được dùng cho những hệ rất nhỏ, điển hình dưới 15 điểm vào/ra. Hệ rơ-le là "
               "an toàn và có thể đạt yêu cầu hiệu năng SIL 3, với điều kiện dùng đúng loại rơ-le và thiết "
               "kế hệ đúng cách."))

    # ---------------------------------------------------------------- 7.3
    b.append(h2("7.3 Hệ bán dẫn rắn", "Solid-state Systems"))
    b.append(p("Hệ bán dẫn rắn ra đời để thay rơ-le bằng những mạch bán dẫn nhỏ hơn, công suất thấp hơn "
               "(ví dụ CMOS — bán dẫn oxit kim loại bù), giống như đài bán dẫn đã thay thế những thiết kế "
               "đèn chân không to lớn hơn trước đó. Tuy vẫn còn được sản xuất (tính đến thời điểm viết "
               "sách, chỉ còn hai nhà cung cấp châu Âu), những hệ này rất chuyên dụng, tương đối đắt (so "
               "với các lựa chọn khác), ít ứng dụng, và vì thế không còn phổ biến."))
    b.append(p("Trong lịch sử có hai loại hệ bán dẫn rắn khác nhau. Một thiết kế châu Âu được gọi là “bán "
               "dẫn rắn an toàn khi hỏng vốn có”: giống rơ-le, nó có chế độ hỏng đã biết và dự đoán được. "
               "Các hệ khác có thể được xếp vào loại bán dẫn rắn “thông thường”, nghĩa là chế độ hỏng của "
               "chúng chia đôi kiểu 50/50 (50 % hỏng an toàn gây dừng nhầm, 50 % hỏng nguy hiểm làm mất "
               "chức năng)."))
    b.append(p("Hệ bán dẫn rắn có một số ưu điểm:"))
    b.append(ul([
        "<b>Có khả năng kiểm tra và bỏ qua.</b> Các hệ bán dẫn rắn được chế tạo cho mục đích an toàn "
        "thường có sẵn tính năng kiểm tra (nút bấm và đèn) và bỏ qua (chìa khoá).",
        "<b>Có khả năng truyền thông nối tiếp.</b> Một số hệ cung cấp một dạng truyền thông nối tiếp tới "
        "các hệ dựa trên máy tính bên ngoài. Có thể dùng để hiển thị trạng thái hệ, thông báo cảnh báo…",
        "<b>Tốc độ cao.</b> Những hệ này không quét vào/ra như PLC, nên chúng có thể đáp ứng nhanh hơn các "
        "hệ dựa trên phần mềm (không tính tới những thứ như trễ lọc đầu vào).",
    ]))
    b.append(p("Hệ bán dẫn rắn có một số nhược điểm (nhiều điểm giống hệ rơ-le):"))
    b.append(ul([
        "<b>Đấu dây cứng.</b> Hệ bán dẫn rắn đấu dây cứng, giống rơ-le. Mở những tủ này ra và nhìn toàn bộ "
        "dây dẫn cùng mối nối bên trong có thể gây choáng. Mỗi khi cần thay đổi logic, phải sửa dây và sửa "
        "bản vẽ bằng tay.",
        "<b>Logic nhị phân.</b> Hệ bán dẫn rắn thực hiện cùng loại logic nhị phân (đóng/ngắt) như rơ-le. "
        "Chúng không làm được điều khiển tương tự hay PID, dù hiện nay phần lớn đã nhận được tín hiệu vào "
        "tương tự. Điều này đương nhiên loại chúng khỏi những ứng dụng cần tính toán.",
        "<b>Chi phí cao.</b> Những hệ này có thể rất đắt, đôi khi còn đắt hơn cả PLC ba kênh. Vậy thì có "
        "người sẽ hỏi: “Thế dùng chúng làm gì?”. Câu trả lời đơn giản: có những người muốn nhiều chức năng "
        "hơn rơ-le nhưng không muốn một hệ an toàn phụ thuộc vào phần mềm.",
        "<b>Không dự phòng.</b> Giống rơ-le, hệ bán dẫn rắn thường được cung cấp ở cấu hình không dự phòng. "
        "Cũng như rơ-le, chỉ một mô-đun hỏng đã có thể làm quá trình dừng nhầm.",
    ]))
    b.append(p("Dù cân nhắc loại hệ bán dẫn rắn nào, tất cả đều có cấu tạo tương tự nhau (xem hình 7-1). Có "
               "các mô-đun riêng cho đầu vào, đầu ra và chức năng logic. Những hệ này không dùng thẻ vào/ra "
               "nhiều kênh như PLC. Các mô-đun phải được đấu dây theo đúng cấu hình logic cần có. Trong một "
               "số hệ, việc đó có thể ngốn hàng dặm dây. Khi dừng lại nghĩ tới toàn bộ công việc thiết kế "
               "chi tiết và chế tạo phải làm, không lạ gì khi những hệ này đắt đến vậy."))
    b.append(fig(1, F.fig_7_1(), "vi"))
    b.append(p("Công dụng chính của hệ bán dẫn rắn là những ứng dụng nhỏ nhưng đòi hỏi mức toàn vẹn an toàn "
               "cao. Có hai nhà cung cấp có hệ được chứng nhận dùng trong SIL 4. Một tài liệu của Anh "
               "khuyến nghị dùng những hệ này (chứ không phải hệ dựa trên phần mềm) cho các ứng dụng ngoài "
               "khơi nhỏ với yêu cầu từ SIL 3 trở lên [Ref. 1]."))

    # ---------------------------------------------------------------- 7.4
    b.append(h2("7.4 Hệ vi xử lý / PLC (dựa trên phần mềm)", "Microprocessor/PLC (Software-based) Systems"))
    b.append(p("Hệ dựa trên phần mềm được dùng trong phần lớn các ứng dụng. Tuy vậy, không có một tất yếu kỹ "
               "thuật nào nói rằng chúng ta buộc phải dùng hệ vi xử lý. PLC vốn được thiết kế để thay thế "
               "rơ-le; việc dùng chúng trong hệ an toàn vì thế có vẻ là điều không tránh khỏi — nhưng ứng "
               "dụng của chúng trong lĩnh vực an toàn đòi hỏi phải soi xét kỹ."))
    b.append(p("Hệ dựa trên phần mềm có một số ưu điểm:"))
    b.append(ul([
        "Chi phí hợp lý;",
        "Dễ và linh hoạt khi cần thay đổi;",
        "Có truyền thông nối tiếp;",
        "Có giao diện đồ hoạ cho người vận hành;",
        "Tự ghi tài liệu;",
        "Chiếm ít chỗ.",
    ]))
    b.append(p("Tuy nhiên, PLC đa dụng không được thiết kế để dùng trong những ứng dụng an toàn then chốt. "
               "Phần lớn các máy không có khả năng chẩn đoán, không có đặc tính an toàn khi hỏng, và không "
               "có mức dự phòng hiệu quả để dùng vượt quá SIL 1."))

    b.append(h3("7.4.1 Linh hoạt: thuốc hay bệnh?", "Flexibility: Cure or Curse?"))
    b.append(p("Tính linh hoạt (tức là sự dễ dàng khi muốn thay đổi) mang lại lợi ích cho một số người, "
               "nhưng cũng tạo ra vấn đề. Sự dễ dàng thay đổi chắc chắn sẽ khuyến khích người ta thực sự "
               "thay đổi. Trừ khi đã có quy trình quản lý thay đổi (MOC) hiệu quả, điều này rất dễ dẫn tới "
               "tăng thêm độ phức tạp và đưa vào những lỗi mới. Tính linh hoạt khuyến khích việc định nghĩa "
               "lại công việc vào giai đoạn muộn của quá trình phát triển, hoặc thậm chí sau khi đã lắp đặt, "
               "để khắc phục những thiếu sót phát hiện ở chỗ khác trong hệ. John Shore đã diễn đạt điều này "
               "rất gọn: “Phần mềm là chỗ để chứa những ý nghĩ nảy ra sau cùng.”"))
    b.append(p("Tính linh hoạt cũng khuyến khích việc xây dựng quá sớm. Ít kỹ sư nào bắt đầu xây một nhà "
               "máy hoá chất trước khi các nhà thiết kế hoàn tất bản vẽ chi tiết, vậy mà điều đó lại thường "
               "xảy ra với các hệ dựa trên phần mềm. Tính linh hoạt còn cho phép dùng những kỹ thuật độc "
               "đáo và đôi khi chưa được kiểm chứng. Tương tự, ít kỹ sư nào thiết kế một hệ phức tạp như "
               "một chiếc máy bay phản lực sau khi chỉ mới dựng một mô hình."))
    b.append(p("Hệ đấu dây cứng áp những giới hạn vật lý lên thiết kế của một hệ. Điều đó giúp kiểm soát độ "
               "phức tạp: suy cho cùng, bạn chỉ có thể nối được ngần ấy dây, ngần ấy bộ định thời và ngần "
               "ấy rơ-le trong một tủ nhất định. Ngược lại, phần mềm không có giới hạn vật lý tương ứng. "
               "Hoàn toàn có thể xây những hệ dựa trên phần mềm cực kỳ phức tạp."))
    b.append(p("Mức độ tự chẩn đoán bên trong của các hệ dựa trên phần mềm rất khác nhau. Vì phần lớn PLC đa "
               "dụng được thiết kế cho điều khiển chủ động, năng động, chúng không cần chẩn đoán rộng. "
               "Trong hệ điều khiển chủ động, phần lớn hỏng hóc tự bộc lộ, và chẩn đoán chỉ làm tăng chi "
               "phí. Sự thiếu chẩn đoán ấy chính là mắt yếu chủ yếu của những hệ này, xét theo khía cạnh an "
               "toàn."))

    b.append(h3("7.4.2 Vấn đề phần mềm", "Software Issues"))
    b.append(quote("“Và họ nhìn vào phần mềm và thấy rằng nó tốt. Nhưng họ lại cứ phải thêm đúng một tính "
                   "năng nữa.”", "G. F. McCormick"))
    b.append(p("Cũng như nhiều người liệt kê phần mềm là lợi ích chính của những hệ này, những người khác "
               "lại coi sự phụ thuộc vào phần mềm là điều bất lợi chính. Điều này liên quan tới hai lĩnh "
               "vực: độ tin cậy và an ninh. Bao nhiêu lập trình viên, khi xong một dự án, dám bước vào "
               "phòng sếp, đặt tay lên ngực và khẳng định: “Sếp ạ, nó sẽ chạy đúng mọi lần, tôi bảo đảm.”? "
               "Và phần lớn hệ khả trình cũng cung cấp rất ít về mặt an ninh truy cập."))
    b.append(p("Theo một ước lượng, sai sót trong phần mềm của hệ (phần mềm đi kèm theo hệ) có thể dao động "
               "từ một lỗi trên ba mươi dòng trong trường hợp xấu nhất, tới một lỗi trên một nghìn dòng "
               "trong trường hợp tốt nhất."))
    b.append(p("Michael Gondran [Ref. 2] dẫn các con số sau về xác suất có một sai sót đáng kể trong phần "
               "mềm ứng dụng của một hệ điều khiển dựa trên vi xử lý điển hình:"))
    b.append(ul([
        "Hệ thông thường: 10<sup>−2</sup> đến 10<sup>−3</sup>.",
        "Để đạt 10<sup>−4</sup> cần nỗ lực đáng kể.",
        "Để đạt 10<sup>−6</sup>, nỗ lực bổ sung phải lớn ngang với nỗ lực phát triển ban đầu.",
    ]))
    b.append(p("Một số nhà cung cấp đùa rằng lỗi phần mềm là “tính năng không có trong tài liệu”. Khi phát "
               "hiện lỗi phần mềm, người ta thường gửi thư cho toàn bộ khách hàng đã đăng ký để thông báo "
               "vấn đề. Có thể bạn cũng đoán được: phần lớn vấn đề phần mềm không phải do nhà cung cấp phát "
               "hiện. Phần lớn được người dùng ngoài hiện trường phát hiện; họ báo lại cho nhà cung cấp, và "
               "nhà cung cấp cố gắng tái hiện vấn đề. Có những lỗi đã gây dừng nhầm. Có những lỗi đã khiến "
               "hệ không làm việc đúng. Một số lỗi chỉ lộ ra khi phần mềm được sửa và nạp xuống hệ. Những "
               "thay đổi trực tuyến (tức sửa bộ điều khiển trong khi quá trình vẫn đang chạy) nói chung "
               "không được khuyến nghị."))
    b.append(p("Một hỏng hóc đơn lẻ trong hệ rơ-le hay hệ bán dẫn rắn chỉ ảnh hưởng tới một kênh. Nhưng một "
               "hỏng hóc đơn lẻ trong mô-đun xử lý của PLC có thể ảnh hưởng tới toàn hệ. Vì thế, nhiều hệ "
               "dựa trên phần mềm dùng một dạng dự phòng nào đó, thường là dự phòng bộ xử lý chính. Một vấn "
               "đề gắn với hệ dự phòng là <b>nguyên nhân chung</b>: một tác nhân gây căng thẳng hay một lỗi "
               "duy nhất có thể làm hỏng cả các phần tử dự phòng. Phần mềm là một vấn đề tiềm tàng như vậy. "
               "Nếu phần mềm có lỗi, toàn bộ hệ dự phòng có thể không làm việc đúng."))

    b.append(h3("7.4.3 PLC đa dụng", "General-Purpose PLCs"))
    b.append(p("PLC ra đời năm 1969 và được thiết kế để thay thế các hệ điều khiển bằng rơ-le. Việc người ta "
               "đưa PLC vào hệ an toàn là điều không tránh khỏi. PLC đa dụng có một số ưu điểm, nhưng cũng "
               "có những hạn chế nghiêm trọng khi dùng trong an toàn. Việc chỉ đơn giản thay rơ-le bằng PLC "
               "thực tế đã gây ra một số tai nạn. Công nghệ mới hơn không nhất thiết có nghĩa là tốt hơn ở "
               "mọi khía cạnh."))

    b.append(h4("7.4.3.1 PLC dự phòng nóng · Hot Back-up PLCs"))
    b.append(p("Dù nhiều người dùng PLC không dự phòng cho ứng dụng an toàn, nhiều hệ PLC có sẵn một dạng dự "
               "phòng nào đó. Một trong những sơ đồ phổ biến nhất là hệ dự phòng nóng (xem hình 7-2). Hệ "
               "này dùng CPU dự phòng — tuy chỉ một cái trực tuyến tại một thời điểm — và các mô-đun vào/ra "
               "đơn tuyến. Một số hệ có sẵn chỗ cho mô-đun vào/ra dự phòng, số khác thì không. Cơ cấu "
               "chuyển mạch giữa hai CPU có thể được thực hiện theo nhiều cách khác nhau. Có vài điểm đáng "
               "lưu ý về những hệ như vậy."))
    b.append(fig(2, F.fig_7_2(), "vi"))
    b.append(p("Để hệ chuyển sang CPU dự phòng, trước hết hệ phải phát hiện được hỏng hóc bên trong máy "
               "chính, tức máy đang trực tuyến. Đáng tiếc là điều này không xảy ra 100 % thời gian, vì chẩn "
               "đoán CPU không phát hiện được 100 % mọi hỏng hóc có thể. Con số chung là khoảng 80 % độ phủ "
               "chẩn đoán, có thể lên tới 95 % nếu thêm một số tính năng (ví dụ bộ định thời canh gác). "
               "(Chẩn đoán là đề tài của mục 7.4.4.1 trong sách này.) Đã có báo cáo về những hỏng hóc không "
               "được phát hiện, nên hệ không chuyển. Đã có báo cáo về những hệ đang chạy tốt mà chức năng "
               "chuyển mạch lại kích hoạt khi không nên kích hoạt, và việc chuyển sang máy dự phòng không "
               "phải là chuyển không gián đoạn (bumpless) nên đã làm quá trình dừng. Cũng đã có báo cáo về "
               "những hệ chuyển sang máy dự phòng, rồi mới phát hiện máy dự phòng cũng đã hỏng, khiến toàn "
               "hệ dừng."))
    b.append(p("Phần lớn nhà cung cấp PLC giả định — ít nhất là trong mô hình hoá hệ của họ — rằng việc "
               "chuyển mạch hiệu quả 100 %. Đây rõ ràng là một giả định lý tưởng hoá, vì đã có nhiều báo cáo "
               "về hỏng hóc của chính cơ cấu chuyển mạch. Một người dùng kể rằng anh ta rút mô-đun xử lý "
               "chính ra để thử chức năng chuyển mạch. Không có gì xảy ra. Sau đó người này phát hiện ra "
               "rằng cơ cấu chuyển mạch cần phải được lập trình thì mới hoạt động. Nhiều nhân viên bán PLC "
               "kể riêng rằng PLC đa dụng có dự phòng lại có nhiều vấn đề hơn hệ không dự phòng."))
    b.append(p("Tuy vậy, mắt yếu thật sự trong phần lớn PLC đa dụng là khả năng thiếu chẩn đoán bên trong "
               "các mô-đun vào/ra. Có những máy hoàn toàn không có khả năng chẩn đoán nào. Người dùng được "
               "khuyến nghị hỏi nhà cung cấp loại thông tin này. Ngay từ năm 1996, ANSI/ISA-84.01 đã nêu "
               "rằng nhà cung cấp phải cung cấp thông tin đó. Có một số máy có chẩn đoán tương đối tốt. Khi "
               "được hỏi tại sao có người không dùng những hệ có chẩn đoán kỹ hơn, câu trả lời điển hình "
               "là: “Chúng đắt quá.” Đúng thế thật! Bạn nhận được đúng cái mà bạn trả tiền."))
    b.append(p("Người ta kể khá nhiều câu chuyện đáng sợ về những hệ đa dụng được dùng trong ứng dụng an "
               "toàn. Đáng tiếc là chúng không được công bố rộng rãi vì tính chất nhạy cảm."))
    b.append(p("Ví dụ, một trong các tác giả biết một kỹ sư kể chuyện công ty anh ta đang cân nhắc dùng PLC "
               "cho mục đích an toàn. Họ đưa một hệ trình diễn qua một loạt phép thử. Một phép thử là lấy "
               "một hệ đang chạy, với toàn bộ vào/ra đang có điện, và rút chip CPU ra trong khi hệ vẫn đang "
               "chạy. Họ làm đúng như vậy và hệ không phản ứng gì cả! Toàn bộ vào/ra vẫn có điện, không có "
               "cảnh báo hay dấu hiệu nào về bất kỳ vấn đề gì! Anh ta diễn đạt khá hay: “Chúng tôi lấy não "
               "của hệ ra và nó thậm chí không nhận ra là có chuyện gì xảy ra!”. Câu tiếp theo của anh ta "
               "là: “Rõ ràng chúng tôi không dùng hệ đó.”"))
    b.append(p("Một cơ sở có bảy hệ đa dụng cho các ứng dụng liên quan an toàn nghe được vài câu chuyện "
               "đáng lo nên đã ra kiểm tra các máy. (Nhiều người nhận ra nhu cầu kiểm tra thiết bị trường "
               "nhưng lại không tin rằng việc kiểm tra hệ logic là cần thiết.) Về cơ bản họ thực hiện một "
               "phép thử nghiệm thu tại chỗ, kích từng đầu vào và kiểm tra xem đầu ra có đáp ứng đúng "
               "không. Trong bảy hệ được thử, <b>bốn hệ không đáp ứng đúng</b>! Điều đáng báo động là không "
               "ai biết có gì sai cho tới khi họ thực sự ra kiểm tra. Đèn nào cũng xanh nên đương nhiên họ "
               "tưởng mọi thứ đều ổn."))
    b.append(p("Một kỹ sư ở văn phòng công ty kể rằng anh ta gửi công văn tới toàn bộ các nhà máy của công "
               "ty, yêu cầu kiểm tra các PLC dùng cho mục đích an toàn. Các báo cáo gửi về cho thấy "
               "<b>từ 30 đến 60 %</b> số hệ không đáp ứng đúng! Một lần nữa, đây không phải chuyện lên trang "
               "nhất và là đề tài rất nhạy cảm. Không ai trình bày một báo cáo tại hội nghị ISA với tiêu đề "
               "“50 % hệ an toàn của chúng tôi không hoạt động. Chúng tôi đã làm hỏng to” cả!"))
    b.append(p("Một kỹ sư khác kể rằng công ty thiết kế và xây dựng (E&C) của anh ta thiết kế một hệ PLC dự "
               "phòng nóng theo đúng đặc tả của khách hàng. Họ lắp đặt, kiểm tra và nói rằng mọi thứ chạy "
               "tốt. Một năm sau họ kiểm tra lại và nói rằng mọi thứ vẫn tốt. Rồi một ngày PLC làm nhà máy "
               "dừng. Khi kiểm tra hệ, họ phát hiện máy trực tuyến đã hỏng, hệ đã chuyển sang máy dự phòng, "
               "nhưng <b>cáp của CPU dự phòng chưa từng được lắp</b>! Hệ đã chạy một năm rưỡi mà thậm chí "
               "không phát hiện hay báo được rằng bản dự phòng còn chưa được nối. Rõ ràng hệ đã không được "
               "kiểm tra kỹ tại cơ sở của đơn vị tích hợp, cũng không được kiểm tra khi khởi động nhà máy, "
               "cũng không được kiểm tra trong bảo trì. Đây là ví dụ về nhóm lỗi mà Cơ quan An toàn và Sức "
               "khoẻ Anh xếp vào loại “lỗi thiết kế và lắp đặt”, chiếm khoảng 15 % các lỗi được phát hiện."))

    b.append(h4("7.4.3.2 PLC đa dụng dự phòng kép · Dual Redundant General-Purpose PLCs"))
    b.append(p("Một số người lấy phần cứng PLC đa dụng có sẵn trên thị trường rồi sửa đổi hệ (tức tuỳ biến "
               "nó) để cố cung cấp độ phủ chẩn đoán cao hơn. Một sơ đồ như vậy bao gồm việc thêm mô-đun "
               "vào/ra, thử vòng hồi tiếp và lập trình ứng dụng bổ sung (xem hình 7-3)."))
    b.append(fig(3, F.fig_7_3(), "vi"))
    b.append(p("Đáng tiếc là những hệ kiểu này thường lớn và bị tuỳ biến, lại dùng thêm phần mềm mà một số "
               "người thấy khó hiểu và khó bảo trì. Khi tính tới phần cứng, phần mềm và công sức kỹ thuật "
               "bổ sung, chi phí có thể trở nên khá cao. Một từ mà một số người dùng để mô tả hệ như vậy "
               "(và có thể làm người khác phật lòng) là “mối vá víu” (kludge). Một trong các tác giả biết "
               "những người đã thử cách này rồi nói: “Không bao giờ nữa!”. Cách tiếp cận kép đặc biệt này "
               "có thể đã hợp lý vào những năm 1980, nhưng nó không kinh tế lắm khi so với những hệ tiêu "
               "chuẩn hiện có."))
    b.append(p("Có một vấn đề vốn có với bất kỳ hệ kép loại này. Khi hai kênh không đồng ý với nhau, làm sao "
               "biết kênh nào đúng? Có phải một kênh đang gặp hỏng hóc an toàn? Trong trường hợp đó bạn "
               "không muốn dừng, nên có thể chọn bỏ phiếu 2oo2 (hai trên hai). Hay một kênh có thể không "
               "đáp ứng vì một hỏng hóc nguy hiểm? Trong trường hợp đó cảnh báo có thể là thật và bạn muốn "
               "dừng, nên có thể chọn bỏ phiếu 1oo2 (một trên hai). Một lần nữa: kênh nào đúng? Với phần "
               "lớn hệ tiêu chuẩn có sẵn trên thị trường, việc này rất khó, nếu không muốn nói là bất khả."))

    b.append(h3("7.4.4 PLC an toàn", "Safety PLCs"))
    b.append(p("Một số người dùng và nhà cung cấp nhận ra những hạn chế của hệ PLC đa dụng trong các ứng "
               "dụng then chốt, và đi phát triển những hệ phù hợp hơn. NASA đã dẫn dắt phần lớn nghiên cứu "
               "về tính toán chịu lỗi vào những năm 1970. Những đặc điểm phân biệt chính của PLC an toàn là "
               "mức chẩn đoán, cách hiện thực dự phòng và chứng nhận độc lập."))

    b.append(h4("7.4.4.1 Chẩn đoán · Diagnostics"))
    b.append(p("Chẩn đoán là một khía cạnh quan trọng của bất kỳ hệ an toàn nào. Cần chẩn đoán để phát hiện "
               "những hỏng hóc nguy hiểm có thể khiến hệ không đáp ứng được khi có yêu cầu. Nhiều PLC đa "
               "dụng không có chẩn đoán kỹ. Thực ra, chẩn đoán nói chung không cần thiết cho hệ điều khiển "
               "chủ động, nơi phần lớn hỏng hóc tự bộc lộ."))
    b.append(p("Mức độ phủ chẩn đoán (tức tỷ lệ hỏng hóc mà hệ có thể tự phát hiện) có ảnh hưởng đáng kể "
               "tới hiệu năng an toàn. Điều này sẽ được bàn kỹ hơn ở chương 8 về đánh giá hiệu năng hệ "
               "thống. Bản ANSI/ISA-84.01 năm 1996 nêu rằng nhà cung cấp bộ xử lý logic phải cung cấp thông "
               "tin về suất hỏng, chế độ hỏng và độ phủ chẩn đoán. Làm việc đó bằng cách nào?"))
    b.append(p("Quân đội Hoa Kỳ cũng gặp những vấn đề tương tự và đã phát triển các kỹ thuật để ước lượng "
               "suất hỏng và chế độ hỏng của thiết bị điện tử. Một kỹ thuật, gọi là phân tích chế độ hỏng và "
               "ảnh hưởng (FMEA), đã được sửa đổi đôi chút và được các nhà cung cấp hệ điều khiển sử dụng. "
               "Kỹ thuật sửa đổi ấy được gọi là <b>phân tích chế độ hỏng, ảnh hưởng và chẩn đoán</b> "
               "(FMEDA). Nó bao gồm việc ghi lại mọi linh kiện trong một hệ, cách chúng có thể hỏng, suất "
               "hỏng của chúng, và liệu hệ có thể tự phát hiện được những hỏng hóc đó hay không."))
    b.append(p("Hình 7-4 là sơ đồ một mạch vào của PLC. Bảng 7-1 trình bày FMEDA của mạch đó. Bảng tính "
               "liệt kê từng linh kiện trong mạch, mọi chế độ hỏng đã biết của từng linh kiện, ảnh hưởng "
               "của mỗi hỏng hóc lên hoạt động của hệ (ví dụ dừng nhầm, hay mất chức năng), suất hỏng của "
               "từng linh kiện ở từng chế độ hỏng, và liệu từng linh kiện cùng từng chế độ hỏng có thể được "
               "hệ tự phát hiện hay không. Khi kết thúc nghiên cứu, nhà cung cấp có thể cho khách hàng biết "
               "suất hỏng an toàn, suất hỏng nguy hiểm và mức chẩn đoán của hệ."))
    b.append(fig(4, F.fig_7_4(), "vi"))
    b.append(table(
        ["Linh kiện", "Chế độ hỏng", "Ảnh hưởng", "Loại", "FIT", "Phát hiện", "Kỹ thuật chẩn đoán"],
        [
            ["R1 – 10K", "ngắn", "dịch ngưỡng", "An toàn", "0,13", "không", "xung vào"],
            ["", "hở", "hở mạch", "An toàn", "0,5", "không", "xung vào"],
            ["R2 – 100K", "ngắn", "ngắn đầu vào", "An toàn", "0,13", "không", "xung vào"],
            ["", "hở", "dịch ngưỡng", "An toàn", "0,5", "không", "xung vào"],
            ["D1", "ngắn", "quá áp", "An toàn", "2", "không", "xung vào"],
            ["", "hở", "hở mạch", "An toàn", "5", "không", "xung vào"],
            ["D2", "ngắn", "quá áp", "An toàn", "2", "không", "xung vào"],
            ["", "hở", "hở mạch", "An toàn", "5", "không", "xung vào"],
            ["DC1", "LED mờ", "không có ánh sáng", "An toàn", "28", "không", "so sánh chéo"],
            ["", "transistor ngắn", "đọc ra logic 1", "Nguy hiểm", "10", "có", "so sánh chéo"],
            ["", "transistor hở", "đọc ra logic 0", "An toàn", "6", "không", "so sánh chéo"],
            ["DC2", "LED mờ", "không có ánh sáng", "An toàn", "28", "không", "so sánh chéo"],
            ["", "transistor ngắn", "đọc ra logic 1", "Nguy hiểm", "10", "có", "so sánh chéo"],
            ["", "transistor hở", "đọc ra logic 0", "An toàn", "6", "không", "so sánh chéo"],
            ["R3 – 100K", "ngắn", "lọc lỏng", "An toàn", "0,13", "không", "so sánh chéo"],
            ["", "hở", "đầu vào nổi mức cao", "Nguy hiểm", "0,5", "có", "so sánh chéo"],
            ["R4 – 10K", "ngắn", "đọc ra logic 0", "An toàn", "0,13", "không", "so sánh chéo"],
            ["", "hở", "đọc ra logic 1", "Nguy hiểm", "0,5", "có", "so sánh chéo"],
            ["R5 – 100K", "ngắn", "lọc lỏng", "An toàn", "0,13", "không", "so sánh chéo"],
            ["", "hở", "đầu vào nổi mức cao", "Nguy hiểm", "0,5", "có", "so sánh chéo"],
            ["R6 – 10K", "ngắn", "đọc ra logic 0", "An toàn", "0,13", "không", "so sánh chéo"],
            ["", "hở", "đọc ra logic 1", "Nguy hiểm", "0,5", "có", "so sánh chéo"],
            ["C1", "ngắn", "đọc ra logic 0", "An toàn", "2", "không", "so sánh chéo"],
            ["", "hở", "lọc lỏng", "An toàn", "0,5", "không", "so sánh chéo"],
            ["C2", "ngắn", "đọc ra logic 0", "An toàn", "2", "không", "so sánh chéo"],
            ["", "hở", "lọc lỏng", "An toàn", "0,5", "không", "so sánh chéo"],
            ["<b>Tổng</b>", "", "", "<b>111 FIT</b>", "<b>88,75</b>", "<b>22</b>",
             "<b>phủ an toàn 97,9 % · phủ nguy hiểm 100 %</b>"],
        ],
        caption="Bảng 7-1. FMEDA của mạch vào trên hình 7-4. Mỗi linh kiện xuất hiện hai lần — một lần "
                "cho chế độ ngắn, một lần cho chế độ hở — vì suất hỏng phải được chia theo chế độ, và một "
                "linh kiện có thể hỏng an toàn ở chế độ này nhưng hỏng nguy hiểm ở chế độ kia. Cột “Loại” "
                "là kết quả phán đoán kỹ thuật, không phải số liệu đo được: nó nói rằng hỏng hóc ấy dẫn tới "
                "hành động hay tới im lặng. FIT là số hỏng hóc trên 10<sup>9</sup> giờ."))
    b.append(p("Hệ đa dụng điển hình có mức chẩn đoán rất thấp. Điều khiến một PLC được xếp vào loại PLC an "
               "toàn chính là mức tự chẩn đoán cao hơn nhiều của nó."))

    b.append(h4("7.4.4.2 Hệ TMR · TMR Systems"))
    b.append(p("Hệ ba kênh dự phòng (triple modular redundant, TMR) về bản chất là những PLC ba kênh chuyên "
               "dụng (xem hình 7-5). Nghiên cứu ban đầu cho những hệ này do NASA tài trợ vào những năm "
               "1970. Những hệ được phát triển thương mại có cùng các lợi ích đã nêu ở trên cho PLC, nhưng "
               "được thiết kế riêng cho ứng dụng an toàn và có dự phòng cùng chẩn đoán rộng khắp. Với mạch "
               "ba kênh, một hệ như vậy có thể chịu được một (và đôi khi nhiều) hỏng hóc linh kiện, dù an "
               "toàn hay nguy hiểm — vì thế mới có thuật ngữ “chịu lỗi”. Những hệ này phù hợp cho các ứng "
               "dụng tới và bao gồm SIL 3. Tuy nhiên, điều đó <em>không</em> có nghĩa là chỉ cần dùng một "
               "hộp logic như vậy là sẽ có một <em>hệ</em> SIL 3. Hiệu năng của hệ còn phụ thuộc vào thiết "
               "bị trường, như sẽ thấy."))
    b.append(fig(5, F.fig_7_5(), "vi"))
    b.append(p("Sơ đồ trên là dạng tổng quát. Một số hệ dùng đầu ra bốn kênh. Một số dùng mạch dự phòng trên "
               "cùng một bo (mô-đun), số khác dùng nhiều mô-đun."))
    b.append(p("Nói chung, những hệ này không đòi hỏi thêm phần mềm phụ trợ nào để thực hiện chẩn đoán (tuy "
               "có ngoại lệ). Người dùng chỉ viết và nạp một chương trình, không phải ba chương trình riêng "
               "(tuy có ngoại lệ). Về bản chất, việc ba kênh hoá được thiết kế để trong suốt với người "
               "dùng."))

    b.append(h4("7.4.4.3 Hệ 1oo2D · Dual 1oo2D Systems"))
    b.append(p("Một số hệ hai kênh đã được phát triển từ cuối những năm 1980 dành riêng cho công nghiệp chế "
               "biến. Thuật ngữ 1oo2D (một trên hai, có chẩn đoán) do William Goble đặt năm 1992 trong cuốn "
               "sách giáo khoa của ông do ISA xuất bản [Ref. 4]. Một số nhà cung cấp hệ hai kênh nhanh "
               "chóng nhận lấy thuật ngữ này. Những hệ này được thiết kế chịu lỗi ở mức ngang với hệ ba "
               "kênh: phải hai hỏng hóc an toàn đồng thời mới gây dừng nhầm, và hai hỏng hóc nguy hiểm đồng "
               "thời mới làm mất chức năng. (Chế độ hỏng được trình bày kỹ hơn ở chương 8.) Những hệ này "
               "dựa trên những khái niệm và công nghệ gần đây hơn, và được các tổ chức độc lập như TÜV và "
               "FM chứng nhận tới cùng mức an toàn như hệ ba kênh. Ngoài cấu hình hai kênh, những nhà cung "
               "cấp này còn có thể cung cấp hệ đơn tuyến (không dự phòng) mà vẫn được chứng nhận dùng trong "
               "SIL 2, và trong một số trường hợp cả SIL 3. Một ví dụ về hệ như vậy được trình bày trên "
               "hình 7-6."))
    b.append(fig(6, F.fig_7_6(), "vi"))

    # ---------------------------------------------------------------- 7.5
    b.append(h2("7.5 Vấn đề quy mô hệ thống", "Issues Related to System Size"))
    b.append(p("Phần lớn hệ rơ-le đều nhỏ và phân tán khắp nhà máy. Mỗi đơn vị quá trình hay mỗi thiết bị "
               "thường có hệ dừng riêng. Cũng như hệ điều khiển bằng máy tính trong phần lớn nhà máy trở "
               "nên tập trung, các hệ dừng cũng trở nên tập trung hơn. Thay vì giữ nhiều hệ đấu dây cứng "
               "nhỏ, nhiều người dùng chuyển sang những đơn vị lớn, tập trung, duy nhất. Đó thường là cách "
               "duy nhất để đủ tiền mua công nghệ mới hơn. Tuy nhiên, hệ càng lớn thì có thể càng phức tạp. "
               "Một tủ rơ-le nhỏ thì tương đối dễ quản lý và bảo trì. Một hệ rơ-le 500 điểm vào/ra thì "
               "không. Hệ đấu dây cứng thường được thay bằng những hệ dựa trên phần mềm nhỏ gọn hơn, dễ "
               "quản lý hơn. Nhưng việc tập trung hoá này đưa vào một loạt vấn đề mới: hỏng hóc đơn lẻ giờ "
               "có thể có tác động rộng hơn nhiều."))
    b.append(fig(7, F.fig_7_7(), "vi"))
    b.append(p("Hỏng hóc đơn lẻ trong những hệ nhỏ tách rời chỉ có tác động hạn chế, cục bộ. Nhưng hỏng hóc "
               "đơn lẻ trong những hệ lớn tập trung có thể có tác động lớn. Ví dụ, nếu một PLC không dự "
               "phòng đang điều khiển 300 điểm vào/ra mà CPU hỏng, thì mất kiểm soát cả 300 điểm. Vì lý do "
               "này, nhiều hệ dựa trên phần mềm được thiết kế với một dạng dự phòng nào đó. Nhược điểm của "
               "dự phòng là nó thường dẫn tới tăng độ phức tạp của hệ. Một số dạng dự phòng (ví dụ hệ chuyển "
               "sang máy dự phòng) thường đưa vào những điểm hỏng đơn lẻ và những vấn đề nguyên nhân chung "
               "khác."))
    b.append(p("Quy mô cũng ảnh hưởng tới việc mô hình hoá hiệu năng của hệ. Đề tài này sẽ được bàn ở "
               "chương 8."))

    # ---------------------------------------------------------------- 7.6
    b.append(h2("7.6 Vấn đề độ phức tạp của hệ thống", "Issues Related to System Complexity"))
    b.append(p("Một cách để xử lý độ phức tạp là chia thiết kế (ví dụ phần mềm) thành những phần hay mô-đun "
               "nhỏ hơn. Cách này có thể giảm độ phức tạp của từng thành phần, nhưng lại làm tăng số lượng "
               "giao diện giữa các thành phần. Điều đó có thể có tác dụng ngược, thực sự làm tăng độ phức "
               "tạp tổng thể. Việc phân tích, thậm chí chỉ là hiểu được, vô số tình huống có thể nảy sinh từ "
               "tương tác giữa các thành phần trở nên khó khăn."))
    b.append(p("Xét về hệ thống đo lường an toàn, đơn giản hơn là tốt hơn. Thay vì tiêu tiền để mua thêm độ "
               "phức tạp, về lâu dài có lẽ tốt hơn là tiêu tiền để mua sự đơn giản. Hệ đơn giản hơn thì dễ "
               "hiểu, dễ phân tích, dễ thiết kế, dễ chế tạo, dễ kiểm tra và dễ bảo trì hơn."))
    b.append(p("Độ phức tạp có thể được đưa vào khi mô hình hoá hiệu năng của một hệ. Có thể đưa một suất "
               "hỏng chức năng hay suất hỏng hệ thống vào phép tính. Đó có thể là lỗi thiết kế, lỗi lập "
               "trình, lỗi chế tạo, lỗi lắp đặt hay lỗi bảo trì. Con số chính xác được chọn có thể khá chủ "
               "quan và khó chứng minh, nhưng việc đưa nó vào mô hình thì tương đối dễ. Một bài tập như vậy "
               "hữu ích chỉ để xem nó tác động tới hiệu năng tổng thể theo kiểu nào. Xin xem ví dụ ở "
               "chương 8."))

    # ---------------------------------------------------------------- 7.7
    b.append(h2("7.7 Giao tiếp với các hệ khác", "Communications with Other Systems"))
    b.append(p("Phần lớn nhà máy hiện nay có một dạng hệ điều khiển tập trung với màn hình đồ hoạ cho người "
               "vận hành. Thay vì có một bộ màn hình riêng cho hệ thống đo lường an toàn, việc đưa thông "
               "tin của SIS lên hiển thị tại các bàn điều khiển chính có những lợi ích (chi phí thấp hơn, "
               "ít chỗ hơn, chỉ phải học một hệ…). Việc này thường đòi hỏi một dạng liên kết truyền thông "
               "nối tiếp giữa các hệ."))
    b.append(p("Phần lớn hệ dùng máy tính đều cung cấp một dạng truyền thông nối tiếp. Việc để hệ điều khiển "
               "quá trình đọc hay hỏi vòng SIS và hiển thị thông tin — như trạng thái của toàn bộ vào/ra, "
               "các trạng thái bỏ qua, các cảnh báo — là tương đối dễ. Việc để hệ điều khiển quá trình ghi "
               "vào SIS cũng dễ y như vậy, và mối nguy tiềm tàng nằm chính ở đây."))
    b.append(p("Nhiều hệ điều khiển và hệ an toàn do các nhà sản xuất khác nhau cung cấp. Để chúng giao tiếp "
               "được với nhau, chúng phải dùng một giao thức truyền thông chung. Một giao thức phổ biến là "
               "Modbus. Một hạn chế của Modbus là nó không dùng và không nhận tên thẻ chữ - số. Thay vào "
               "đó, mọi biến phải được tham chiếu bằng những con số gắn với địa chỉ ô nhớ. Hãy hình dung "
               "một hệ điều khiển và một hệ an toàn giao tiếp qua Modbus. Điều gì sẽ xảy ra nếu cơ sở dữ "
               "liệu trong hệ an toàn bị sửa đổi? Nếu các biến được chèn vào giữa danh sách, thay vì thêm "
               "vào cuối danh sách, thì toàn bộ các địa chỉ còn lại sẽ thay đổi. Hệ điều khiển sẽ không có "
               "dấu hiệu nào về thay đổi đó, và kết quả là có thể giao tiếp với toàn bộ những biến sai. "
               "Điều này đương nhiên có thể dẫn tới những vấn đề nghiêm trọng. Những phương thức truyền "
               "thông mới và tiên tiến hơn, như liên kết và nhúng đối tượng cho điều khiển quá trình (OPC), "
               "nên làm giảm bớt một số vấn đề này."))
    b.append(p("Một số công ty cho phép ghi vào hệ an toàn, số khác thì không. Chắc chắn sẽ có những trường "
               "hợp hệ điều khiển cần ghi vào SIS. Các tiêu chuẩn không cấm chức năng này. Điều cần cân "
               "nhắc chính là: không được để hệ điều khiển làm hỏng bộ nhớ của SIS. Điều đó đòi hỏi một "
               "dạng kiểm soát nào đó. Hãy xét việc thử đọc lại để chắc chắn rằng chỉ đúng biến dự định bị "
               "thay đổi. Mọi lệnh ghi vào hệ an toàn đều phải được cân nhắc kỹ và kiểm soát chặt."))
    b.append(p("Các fieldbus an toàn, dùng để truyền thông giữa các hệ an toàn hoặc bên trong một hệ an "
               "toàn, được bàn ở mục 9.8."))

    # ---------------------------------------------------------------- 7.8
    b.append(h2("7.8 Chứng nhận và đã qua sử dụng", "Certified vs. Prior Use"))
    b.append(p("Có nhiều nhà cung cấp cạnh tranh để giành việc làm ăn trên mọi thị trường, kể cả thị trường "
               "an toàn. Sản phẩm thường rất khác nhau về thiết kế. Xét tới độ phức tạp của nhiều hệ logic "
               "dựa trên phần mềm, cùng với những câu chuyện trái ngược nhau mà các nhà cung cấp kể, người "
               "dùng rơi vào một thế tiến thoái lưỡng nan: làm sao đánh giá hiệu quả được ngần ấy sản phẩm "
               "khác nhau? Người dùng cuối trong công nghiệp chế biến chuyên về chế biến dầu, khí và các "
               "hoá chất khác nhau; họ không kinh doanh để trở thành chuyên gia đánh giá hệ an toàn. Người "
               "dùng khó có thể biện minh cho việc mua vài hệ khác nhau rồi đánh giá chúng trong vài tháng "
               "chỉ để xem mình thích cái nào nhất — nhất là với những hệ hoàn toàn mới, chưa có kinh "
               "nghiệm người dùng nào trước đó. Chính ở đây xuất hiện nhu cầu về đánh giá độc lập của bên "
               "thứ ba."))
    b.append(p("Cạnh tranh giữa các nhà cung cấp rất gay gắt trong mọi ngành, nhất là trong an toàn. Các "
               "nhà cung cấp hệ hai kênh nói sản phẩm của họ tốt ngang hệ ba kênh. Một số nhà cung cấp nay "
               "đưa ra hệ bốn kênh và đương nhiên khẳng định hệ của họ tốt hơn hệ ba kênh. Một số nhà cung "
               "cấp đưa ra những hệ (trông như) không dự phòng mà vẫn phù hợp dùng trong SIL 3. Biết tin "
               "ai, và quan trọng hơn là vì sao? Chính ở đây xuất hiện nhu cầu về đánh giá độc lập của bên "
               "thứ ba."))
    b.append(p("Một cách để người dùng đánh giá hệ thống và để nhà sản xuất tự phân biệt mình trên thị "
               "trường an toàn là <b>chứng nhận của bên thứ ba</b>. Những tổ chức như TÜV của Đức, hay FM "
               "ở Hoa Kỳ, có thể cung cấp đánh giá độc lập theo nhiều tiêu chuẩn khác nhau. Trước khi tiêu "
               "chuẩn IEC 61508 ra đời vào cuối những năm 1990, TÜV dùng các tiêu chuẩn quốc gia khác của "
               "Đức."))
    b.append(p("Quá trình chứng nhận vừa mất thời gian vừa tốn kém. Nhà cung cấp phải chuyển chi phí đó cho "
               "người dùng. Chứng nhận được coi là hợp lý (ít nhất là với một số người) đối với những hệ "
               "logic phức tạp và đắt tiền. Tuy nhiên, chứng nhận cho những thiết bị trường đơn giản và rẻ "
               "hơn thì có vẻ đáng ngờ."))
    b.append(p("Người dùng không muốn bị buộc phải dùng thiết bị đã được chứng nhận. Các tiêu chuẩn không "
               "bắt buộc dùng thiết bị đã chứng nhận. Nhưng người dùng vẫn cần một cách nào đó để tự đảm bảo "
               "rằng thiết bị phù hợp để dùng. Bản ANSI/ISA-84.01 năm 1996 gọi khái niệm này là “người dùng "
               "phê chuẩn”. Thuật ngữ dùng trong các tiêu chuẩn IEC gần đây là “đã được chứng minh trong sử "
               "dụng”, hay “đã qua sử dụng”. Về bản chất, người dùng phải đánh giá chương trình chất lượng "
               "của nhà cung cấp và phải có một mẫu đủ lớn trong một môi trường tương tự để có số liệu suất "
               "hỏng có ý nghĩa. Đây thường được coi là cách chấp nhận được để biện minh cho việc dùng những "
               "thiết bị trường tương đối đơn giản, nhưng được coi là cực kỳ khó làm với những bộ xử lý "
               "logic phức tạp."))

    # ---------------------------------------------------------------- Tóm tắt
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Có một số công nghệ để dùng trong hệ thống đo lường an toàn: khí nén, rơ-le điện cơ, bán "
               "dẫn rắn, và PLC. Không có một hệ nào tốt nhất nói chung. Mỗi loại đều có ưu và nhược điểm. "
               "Việc quyết định hệ nào phù hợp nhất cho một ứng dụng phụ thuộc vào nhiều yếu tố như ngân "
               "sách, quy mô, mức rủi ro, tính linh hoạt, độ phức tạp, bảo trì, yêu cầu giao diện và truyền "
               "thông, an ninh…"))
    b.append(table(
        ["Đặc điểm", "Khí nén", "Rơ-le", "Bán dẫn rắn", "PLC đa dụng", "PLC an toàn"],
        [
            ["Quy mô phù hợp", "nhỏ", "&lt; 15 I/O", "nhỏ", "mọi quy mô", "mọi quy mô"],
            ["SIL tối đa", "SIL 3", "SIL 3", "SIL 4", "SIL 1", "SIL 3"],
            ["Phần mềm", "không", "không", "không", "có", "có"],
            ["Chẩn đoán", "không", "không", "hạn chế", "rất thấp", "cao"],
            ["Truyền thông", "không", "không", "một số", "có", "có"],
            ["Kiểm tra / bỏ qua", "không", "không", "có", "có", "có"],
            ["Thay đổi logic", "đấu lại dây", "đấu lại dây", "đấu lại dây", "lập trình lại",
             "lập trình lại"],
            ["Chi phí", "thấp", "thấp", "rất cao", "trung bình", "cao"],
        ],
        caption="Bảng 7-2. So sánh năm công nghệ, tổng hợp từ chính phần tóm tắt và các mục 7.1–7.4 của "
                "chương. Cột “SIL tối đa” là mức mà <em>hộp logic</em> có thể đạt, không phải mức của cả "
                "hệ: một hộp logic SIL 3 nối với một cảm biến duy nhất vẫn chỉ là một hệ SIL 1."))
    b.append(p("Hệ khí nén phù hợp nhất với những ứng dụng nhỏ, nơi cần sự đơn giản, an toàn nội tại và "
               "không có điện lưới."))
    b.append(p("Hệ rơ-le khá đơn giản, tương đối rẻ khi mua, miễn nhiễm với hầu hết các dạng nhiễu EMI/RFI, "
               "và có thể chế tạo cho nhiều dải điện áp khác nhau. Chúng nói chung không có bất kỳ dạng giao "
               "diện hay truyền thông nào. Thay đổi logic đòi hỏi phải sửa tài liệu bằng tay. Nói chung, hệ "
               "rơ-le được dùng cho những ứng dụng tương đối nhỏ và đơn giản."))
    b.append(p("Hệ bán dẫn rắn (tức hệ đấu dây cứng không có phần mềm) vẫn còn có sẵn. Một số hệ được chế "
               "tạo riêng cho ứng dụng an toàn và có tính năng kiểm tra, bỏ qua và truyền thông. Thay đổi "
               "logic vẫn đòi hỏi cập nhật tài liệu bằng tay. Những hệ này đã mất uy tín với nhiều người "
               "dùng vì tính linh hoạt hạn chế và chi phí cao, cùng với việc các hệ dựa trên phần mềm đã "
               "được chấp nhận. Chúng vẫn được dùng trong những ứng dụng nhỏ, đơn giản, đòi hỏi mức toàn "
               "vẹn an toàn cao."))
    b.append(p("Hệ dựa trên phần mềm, từ PLC đa dụng tới PLC an toàn chuyên dụng, mang lại tính linh hoạt "
               "của phần mềm, khả năng tự ghi tài liệu, truyền thông và giao diện cấp cao hơn. Đáng tiếc là "
               "nhiều hệ đa dụng không được thiết kế riêng cho an toàn và không có những tính năng (như an "
               "ninh, mức chẩn đoán cao, dự phòng hiệu quả) có thể là yêu cầu bắt buộc. Tuy vậy, những PLC "
               "an toàn được thiết kế gần đây được phát triển riêng cho các ứng dụng then chốt hơn, và đã "
               "trở nên vững chắc trong công nghiệp chế biến."))
    b.append(note(
        "<b>Ghi chú của người dịch — ba điểm cần đối chiếu.</b> "
        "(1) <b>Đánh số hình bị lệch.</b> Nguyên bản có bảy hình; ở đây hình 7-5 và 7-6 của nguyên bản "
        "(TMR và 1oo2D) thành hình 7-5 và 7-6, còn hình FMEDA của nguyên bản (hình 7-5) được trình bày lại "
        "thành bảng 7-1 vì nó vốn là một bảng tính; hình 7-7 (tập trung hoá) là hình thêm vào để minh hoạ "
        "mục 7.5. "
        "(2) <b>Trích dẫn lệch.</b> Nguyên bản viết “Michael Gondran [Ref. 2]” nhưng danh mục tài liệu lại "
        "xếp Gondran ở số 3 và số 2 là Taylor. Ở đây giữ nguyên số như trong thân bài và ghi rõ danh mục ở "
        "cuối chương. "
        "(3) <b>Tham chiếu mục không tồn tại.</b> Mục 7.4.3.1 nhắc tới “mục 7.4.5.1” về chẩn đoán, nhưng "
        "chương này không có mục 7.4.5.1 — phần chẩn đoán nằm ở mục 7.4.4.1. Đã sửa lại số mục trong bản "
        "dịch."))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "Four technologies can close a valve on demand: compressed air, a relay, a solid-state module, or a "
        "programmable logic controller. None of them is best in general, and the choice is not really "
        "technical. It is a judgement about how much diagnostic machinery you are willing to pay for, and "
        "about what happens to the plant when that machinery is wrong."))

    b.append(h2("The relay panel is the honest baseline"))
    b.append(p("It is fashionable to treat relay logic as obsolete. Read section 7.2 again and it looks more "
               "like a specification than a relic. A relay is simple, cheap, immune to most electrical "
               "interference, needs no software, and fails in a known direction — de-energised. Its "
               "limitations are all consequences of being physical: it cannot tell you anything, it cannot "
               "be tested without being wired for it, and every logic change is a change to copper."))
    b.append(p("The 700-I/O panel in the chapter, with fifty-seven signal handoffs between sensor and final "
               "element and a satellite in the middle, is not a joke about bad engineering. It is what "
               "happens when a technology is scaled past the size at which its virtues hold. Relays are "
               "excellent below about fifteen I/O and become unmanageable somewhere before a hundred. The "
               "number is not a standard; it is the point at which nobody can trace a cause to an effect "
               "any more."))
    b.append(p("The solid-state system of section 7.3 replaces the relay with a module and the copper with "
               "a printed board, and in integrity terms it buys very little: the logic is still fixed in "
               "the wiring, the failure modes are still physical, and a logic change still means redrawing "
               "the schematic."))
    b.append(fig(1, F.fig_7_1(), "en"))

    b.append(h2("Diagnostics are the whole difference"))
    b.append(p("Every technology in this chapter delivers the same thing when it works: a discrete output. "
               "What separates them is what they can tell you about themselves while nothing is happening. "
               "A general-purpose PLC has almost no answer to that question, because it was designed for "
               "active control, where a failed input announces itself by making the process misbehave. In a "
               "safety system the process is quiet by design, so a failed input announces nothing at all."))
    b.append(p("The input circuit shows why the problem is structural rather than a matter of better "
               "components. The opto-coupler that makes the channel safe — no conductive path between field "
               "and logic — is the same component that makes a stuck switch undetectable, because there is "
               "no return path to test against. Diagnostics have to be designed in, by adding a second "
               "channel or a pulse test, not switched on."))
    b.append(fig(4, F.fig_7_4(), "en"))
    b.append(p("This is why the chapter's horror stories are all the same story. The demo system with the "
               "CPU chip removed that kept every output energised; the four out of seven systems that failed "
               "a site acceptance test nobody had thought to run; the backup CPU cable that was never "
               "installed and was not detected for eighteen months. In each case the hardware was working. "
               "The lights were green. Nothing was measuring the thing that mattered."))

    b.append(h2("The FMEDA is where a vendor becomes accountable"))
    b.append(p("Table 7-1 is worth reading as a document rather than as data. Every component appears twice, "
               "once for each failure mode, because a resistor that fails short and a resistor that fails "
               "open do different things to the loop. Each row is classified safe or dangerous, given a FIT "
               "rate, and marked as detectable or not. The totals at the bottom — 111 FIT, 88.75 safe, 22 "
               "dangerous, 97.9 % safe coverage, 100 % dangerous coverage — are the vendor's claim in its "
               "most falsifiable form."))
    b.append(p("Two things about that table repay attention. First, the dangerous modes are a minority of "
               "the total but a majority of the risk: 22 FIT out of 111, all of them detected, which is "
               "exactly the arrangement a safety circuit is supposed to have. Second, the coverage figures "
               "are only achievable because the circuit compares two channels. A single-channel version of "
               "the same schematic would have the same failure rates and almost none of the coverage — the "
               "hardware would be identical and the SIL claim would be two bands lower."))

    b.append(h2("Redundancy architectures are arguments about disagreement"))
    b.append(p("Hot back-up, active parallel, TMR and 1oo2D are usually presented as a ladder of increasing "
               "integrity. They are better understood as four different answers to one question: when the "
               "channels disagree, who decides?"))
    b.append(p("A hot back-up never has to answer, because only one CPU is running, and it pays for that by "
               "being unable to detect its own failure. All three of its failure routes meet at the same "
               "joint: diagnostics that do not cover every failure, a switch that may not be bumpless, and "
               "a standby that may already be dead."))
    b.append(fig(2, F.fig_7_2(), "en"))
    b.append(p("Active parallel has to answer every time, and has no basis on which to do it. Both channels "
               "process, so there is no standby copy to compare against the running one; the only "
               "arbitration available is a voting rule chosen in advance, and that rule — not the hardware "
               "— decides whether the system fails safe or fails dangerous."))
    b.append(fig(3, F.fig_7_3(), "en"))
    b.append(p("TMR answers by majority, which works until two channels fail the same way. It survives any "
               "single failure, including a dangerous one, because two channels still agree — but the three "
               "channels protect only the logic. The sensor and the valve are still single points of "
               "failure, and they are where most of the unreliability actually lives."))
    b.append(fig(5, F.fig_7_5(), "en"))
    b.append(p("1oo2D answers by diagnostics rather than by voting, which is why it needs only two channels "
               "and why its integrity depends entirely on the diagnostic coverage it claims. Two "
               "simultaneous safe failures are needed for a nuisance trip and two simultaneous dangerous "
               "failures for loss of function: fault tolerance equal to a triple system, from two channels "
               "and a diagnostic that must actually work."))
    b.append(fig(6, F.fig_7_6(), "en"))
    b.append(p("The common-cause problem runs underneath all four. Redundancy counts independent failures; "
               "software bugs, shared power supplies, shared impulse lines and shared maintenance procedures "
               "are not independent. A triple system with a single shared root cause is a single system with "
               "three times the hardware."))

    b.append(h2("Centralisation buys convenience and sells blast radius"))
    b.append(p("Section 7.5 is the shortest in the chapter and the most consequential. Consolidating a dozen "
               "small shutdown systems into one large one is almost always the right commercial decision: "
               "one spare-parts list, one maintenance team, one programming environment, one screen. It is "
               "also a decision to convert a set of independent single points of failure into one shared "
               "single point of failure, and to convert a local trip into a plant trip."))
    b.append(fig(7, F.fig_7_7(), "en"))
    b.append(p("The mitigation is redundancy, and the trap is that redundancy is exactly what makes the "
               "system complex enough to need more of it. Every hot back-up adds a switch that can fail; "
               "every switch adds a diagnostic that must itself be tested; every test adds a procedure that "
               "can be performed wrongly. Simplicity is not an aesthetic preference in a safety system. It "
               "is the only property that reduces the number of things that must be got right."))

    b.append(h2("Prior use is a claim about your own history, not the vendor's brochure"))
    b.append(p("The chapter ends on certification, and the honest observation that most field devices are "
               "never going to be certified. The prior-use route is the alternative, and it is frequently "
               "misused. It requires a quality programme you have actually audited, a sample size large "
               "enough to mean something, and an environment similar enough that the failure data "
               "transfers. It does not mean “we have used these for years and nothing has gone wrong” — "
               "which is a statement about luck, not about failure rate."))
    b.append(p("The distinction the chapter draws between simple field devices and complex logic solvers is "
               "the practical one. A pressure switch has a small enough failure space that field history "
               "can characterise it. A safety PLC has a failure space dominated by software, where field "
               "history tells you almost nothing about the failure you have not had yet."))
    return "\n".join(b)
