# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 9, Issues Relating to Field Devices
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, lead, note, ol, p, quote, refs,
                          table, ul)

import sis09fig as F

PAGES_SRC = 24
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Thiết bị trường</em> — cảm biến, đường xung áp, phần tử cuối, dây dẫn trường và mọi thứ "
            "nối vào đầu cực vào/ra của hệ logic. · "
            "<em>Đánh thức để cắt (energize to trip)</em> — mạch thường có điện; mất điện chính là lệnh "
            "cắt. · "
            "<em>Mạch có giám sát</em> — mạch có điện trở cuối đường để hệ logic phân biệt được đứt dây "
            "với tiếp điểm mở. · "
            "<em>HART</em> — giao thức số chạy chồng trên dòng 4–20 mA, mang thêm dữ liệu chẩn đoán. · "
            "<em>Bộ định vị van thông minh</em> — bộ định vị có chẩn đoán và thử hành trình một phần. · "
            "<em>Đo suy diễn</em> — suy một đại lượng từ đại lượng khác (ví dụ suy áp suất từ nhiệt độ). · "
            "<em>Dự phòng đa dạng</em> — hai kênh khác công nghệ, khác hãng, khác phần mềm, để giảm "
            "nguyên nhân chung.")
    return note(
        "<b>Key terms.</b> <em>Field devices</em> — sensors, impulse lines, final elements, field wiring "
        "and everything else landing on the I/O terminals of the logic solver. · <em>Energize to trip</em> "
        "— the circuit is normally live, so losing power <em>is</em> the trip command. · <em>Supervised "
        "circuit</em> — a loop with an end-of-line resistor, so the logic solver can tell a broken wire "
        "from an open contact. · <em>HART</em> — the digital protocol riding on top of the 4–20 mA signal, "
        "carrying diagnostic data. · <em>Smart valve positioner</em> — a positioner with diagnostics and "
        "partial-stroke capability. · <em>Inferential measurement</em> — inferring one variable from "
        "another. · <em>Diverse redundancy</em> — two channels of different technology, maker and "
        "firmware, to cut common cause.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Thiết bị trường gồm cảm biến, đường xung áp, phần tử cuối, dây dẫn trường và những thiết bị khác "
        "nối vào đầu cực vào/ra của hệ logic. Đây thường là những phần tử quan trọng nhất, và có lẽ cũng "
        "là những phần tử bị hiểu sai và dùng sai nhiều nhất trong hệ an toàn. Mức quan tâm dành cho "
        "thiết bị trường trong thiết kế và ứng dụng hệ an toàn thấp một cách không tương xứng so với ảnh "
        "hưởng tiềm tàng của chúng lên hiệu năng của cả hệ. Người ta ước tính khoảng 90 % vấn đề của hệ an "
        "toàn có thể quy về thiết bị trường."))

    b.append(note_terms("vi"))

    b.append(quote("Khi mua bất động sản, ba tiêu chí chọn lựa quan trọng nhất là vị trí, vị trí và vị "
                   "trí. Khi mua một hệ thống đo lường an toàn, ba tiêu chí quan trọng nhất là chẩn đoán, "
                   "chẩn đoán và chẩn đoán.", "Trích đầu chương 9"))

    # ------------------------------------------------------------------ 9.1
    b.append(h2("9.1 Giới thiệu", "Introduction"))
    b.append(p("Rơ-le, bán dẫn rắn và PLC đa dụng đều đã được dùng làm bộ xử lý logic cho hệ an toàn. PLC "
               "có ưu điểm là lập trình được bằng phần mềm, nhưng tỷ lệ phân chia chế độ hỏng nguy hiểm "
               "của chúng rất khác rơ-le; vì thế hiệu năng an toàn của chúng cũng rất khác. (Đó là nội "
               "dung chương 7 và 8.) Nhiều người — và đương nhiên cả nhà cung cấp — có xu hướng tập trung "
               "vào khác biệt giữa các công nghệ bộ xử lý logic. Nay khi PLC đa dụng và PLC “an toàn” đã "
               "có suất hỏng nguy hiểm, ẩn thấp hơn và độ tin cậy tốt hơn, sự chú ý đang quay về phía "
               "thiết bị trường."))
    b.append(p("Có nhiều tài liệu mô tả các loại thiết bị trường cho nhiều ứng dụng khác nhau. Mục tiêu "
               "chính của chương này là bàn những vấn đề cần giải quyết khi dùng thiết bị trường trong "
               "ứng dụng an toàn. Một số vấn đề ấy là:"))
    b.append(ul([
        "chẩn đoán",
        "bộ chuyển đổi so với công tắc",
        "bộ chuyển đổi thông minh",
        "van thông minh",
        "dự phòng",
        "đo suy diễn",
        "yêu cầu riêng của từng ứng dụng",
    ]))

    # ------------------------------------------------------------------ 9.2
    b.append(h2("9.2 Tầm quan trọng của thiết bị trường", "Importance of Field Devices"))
    b.append(p("Thiết bị ngoại vi — cảm biến và phần tử cuối — của hệ điều khiển quá trình cơ bản (BPCS) "
               "gặp nhiều hư hỏng phần cứng hơn chính thiết bị trong phòng điều khiển. Điều tương tự cũng "
               "đúng với các thành phần của hệ an toàn."))

    b.append(h3("9.2.1 Ảnh hưởng của thiết bị trường lên hiệu năng hệ", "Impact of Field Devices on System Performance"))
    b.append(p("Để thấy rõ ảnh hưởng của thiết bị trường lên hiệu năng của hệ an toàn, hãy xét ví dụ sau:"))
    b.append(p("Một hệ thống đo lường an toàn gồm một cảm biến áp suất, logic rơ-le, một van điện từ và "
               "một van dừng được đề xuất cho một ứng dụng SIL 1. Theo yêu cầu SIL trên, PFD<sub>avg</sub> "
               "phải nằm trong khoảng 0,1 đến 0,01. Ban đầu chọn chu kỳ thử là mỗi năm một lần. Có thể "
               "tính PFD<sub>avg</sub> cho từng phần tử không dự phòng của hệ bằng công thức:"))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>d</sub> · TI / 2", "9.1"))
    b.append(p("trong đó λ<sub>d</sub> là suất hỏng nguy hiểm của thành phần; TI là chu kỳ thử nghiệm "
               "của thành phần; λ = 1/MTTF (thời gian trung bình tới lần hỏng)."))
    b.append(p("Số liệu độ tin cậy và hiệu năng của SIS đề xuất được trình bày ở Bảng 9-1."))
    b.append(table(
        ["Thiết bị", "MTTF nguy hiểm (năm)", "PFD<sub>avg</sub>", "Đóng góp (%)"],
        [
            ["Cảm biến", "20", "0,025", "42"],
            ["Hệ logic (4 rơ-le)", "100", "0,005", "8"],
            ["Van điện từ", "33", "0,015", "25"],
            ["Van dừng", "33", "0,015", "25"],
            ["<b>Tổng</b>", "<b>8,3</b>", "<b>0,06</b>", "<b>100</b>"],
        ],
        caption="Bảng 9-1. Số liệu độ tin cậy và hiệu năng. Cột MTTF của hàng tổng là nghịch đảo của tổng "
                "các suất hỏng nguy hiểm (1/0,1206 ≈ 8,3 năm), không phải tổng của bốn MTTF. Tổng "
                "PFD 0,06 cho RRF = 1/0,06 ≈ 16."))
    b.append(p("Hệ số giảm rủi ro tổng của hệ (RRF, bằng 1/PFD) là 16. Ảnh hưởng của thiết bị trường lên "
               "hiệu năng tổng của hệ là 92 %."))

    b.append(h3("9.2.2 Tỷ lệ phân chia hư hỏng của hệ", "Percentage Split of System Failures"))
    b.append(p("Hình 9-1 cho thấy tỷ lệ phân chia hư hỏng giữa các phần tử chính của hệ đã phân tích và "
               "tổng hợp ở Bảng 9-1."))
    b.append(p("Theo quy tắc chung, thiết bị trường có thể chiếm khoảng 90 % số hư hỏng của hệ. Hệ logic "
               "có thể chỉ chiếm 10 %. Đây phần nào là đơn giản hoá, vì các con số có thể thay đổi đáng kể "
               "theo công nghệ và cấu hình."))
    b.append(p("Số liệu trên chỉ tính hư hỏng ngẫu nhiên. Hư hỏng hệ thống (ví dụ đặc tính kỹ thuật không "
               "đầy đủ, quy trình bảo trì kém, sai hiệu chuẩn, thiếu đào tạo…) cũng có thể ảnh hưởng đáng "
               "kể lên hiệu năng tổng của hệ. Hư hỏng hệ thống của thiết bị trường có thể còn cao hơn của "
               "thiết bị logic, vì nhiều hoạt động có thể tập trung vào những thiết bị ấy hơn."))
    b.append(fig(1, F.fig_9_1(), "vi"))

    # ------------------------------------------------------------------ 9.3
    b.append(h2("9.3 Cảm biến", "Sensors"))
    b.append(p("Dưới đây bàn những vấn đề chung về công nghệ cảm biến, chế độ hỏng và chẩn đoán."))

    b.append(h3("9.3.1 Chung", "General"))
    b.append(p("Cảm biến dùng để đo nhiệt độ, áp suất, lưu lượng, mức… Chúng có thể là công tắc khí nén "
               "hay điện đơn giản, đổi trạng thái khi đạt giá trị đặt, hoặc có thể chứa bộ chuyển đổi "
               "tương tự khí nén hay điện tử cho đầu ra biến thiên theo độ lớn của biến quá trình."))
    b.append(p("Cảm biến, như mọi thiết bị khác, có thể hỏng theo nhiều cách. Chúng có thể hỏng an toàn và "
               "gây cắt nhầm (tức kích hoạt mà không có thay đổi tương ứng của tín hiệu vào). Chúng cũng "
               "có thể hỏng nguy hiểm (tức không phản ứng với một yêu cầu thật hay một thay đổi của tín "
               "hiệu vào). Đây là hai nhóm chế độ hỏng đáng quan tâm nhất với hệ an toàn. Các ví dụ khác "
               "về hỏng cảm biến:"))
    b.append(ul([
        "tắc đường xung áp",
        "rò đường xung áp",
        "tích tụ chất lỏng trong ống nhánh",
        "hư hỏng cơ khí hoặc rò bên trong",
        "bẩn, bám cặn ở công tắc",
        "ăn mòn tiếp điểm",
        "đứt cặp nhiệt điện",
        "bộ chuyển đổi hỏng về phía cao hoặc phía thấp",
        "bộ chuyển đổi thông minh bị bỏ ở chế độ “đầu ra cưỡng bức”",
        "đầu ra thất thường",
        "tín hiệu bộ chuyển đổi bị đóng băng",
        "trôi điểm không",
    ]))
    b.append(p("Hầu hết hệ an toàn được thiết kế theo hướng an toàn khi hỏng. Điều này thường có nghĩa: "
               "khi mất nguồn (điện, khí nén hay thuỷ lực), hệ an toàn đưa quá trình về trạng thái an "
               "toàn — thường là dừng thiết bị và ngừng sản xuất. Phải suy nghĩ xem cảm biến nên phản ứng "
               "thế nào để đạt được tính an toàn khi hỏng ấy. Cũng phải tránh cắt nhầm vì lý do an toàn, "
               "bởi chế độ khởi động và dừng thường là lúc rủi ro cao nhất. Ngoài ra, một hệ gây cắt nhầm "
               "quá nhiều có thể bị đặt bypass, và khi ấy mất toàn bộ bảo vệ."))
    b.append(p("Các yêu cầu chung cho vận hành an toàn khi hỏng là:"))
    b.append(ul([
        "tiếp điểm cảm biến đóng và có điện trong quá trình vận hành bình thường",
        "tín hiệu bộ chuyển đổi chuyển sang trạng thái cắt khi hỏng (hoặc ít nhất được hệ phát hiện để có "
        "thể xử lý)",
        "tiếp điểm đầu ra của hệ logic thường đóng và có điện",
        "phần tử cuối chuyển về vị trí an toàn khi mất khí (ví dụ van đóng lại)",
        "các thiết bị cuối khác (ví dụ động cơ hay tuabin) dừng lại",
    ]))
    b.append(p("Bộ chuyển đổi thường có thể được cấu hình để hỏng về phía cao hoặc phía thấp khi điện tử "
               "bên trong hỏng. Tuy nhiên không phải mọi hư hỏng đều phát hiện được, nên không có gì bảo "
               "đảm thiết bị luôn đạt được trạng thái mong muốn khi hỏng. Cần suy nghĩ về chế độ hỏng cho "
               "từng cảm biến. Ví dụ, có thể mong bộ chuyển đổi đo mức thấp hỏng về phía thấp, nhưng bộ "
               "chuyển đổi đo áp suất cao lại hỏng về phía cao. Không thể đưa ra một khuyến nghị chung "
               "cho mọi cảm biến. (Như thường làm với van điều khiển, chế độ hỏng của bộ chuyển đổi phải "
               "được xác định và đưa vào đặc tính yêu cầu an toàn — SRS; xem chương 5.)"))
    b.append(p("Một số phép đo có thể được suy ra từ biến khác. Ví dụ, nếu một hệ được thiết kế để dừng khi "
               "áp suất cao, có thể hữu ích nếu đồng thời theo dõi nhiệt độ (nếu theo quá trình, nhiệt độ "
               "tăng cao cũng có thể hàm ý áp suất cao). Có thể dùng phép đo suy diễn để khởi phát lệnh "
               "dừng. Khi dùng những phép đo như vậy cần xét:"))
    b.append(ul([
        "<b>Thời gian đáp ứng:</b> đáp ứng của biến được đo phải nằm trong thời gian an toàn của quá "
        "trình như đã định trong đặc tính yêu cầu.",
        "<b>Tương quan:</b> quan hệ giữa hai biến phải được hiểu rõ.",
        "<b>Độ chính xác:</b> quan hệ ấy phải cho một biểu diễn chính xác.",
    ]))
    b.append(p("Nếu còn chưa chắc chắn về biến suy diễn, nên cân nhắc chỉ dùng phép đo ấy cho mục đích báo "
               "động. Người vận hành có thể ra quyết định cuối cùng sau khi xem xét các thông số quá "
               "trình khác. Biến suy diễn cũng có thể dùng làm công cụ chẩn đoán mở rộng: so sánh đầu ra "
               "của bộ chuyển đổi hay công tắc với giá trị suy diễn của nó có thể dùng để kích hoạt báo "
               "động chẩn đoán."))
    b.append(p("Cần đặc biệt cẩn thận khi vận hành cảm biến ở sát đầu mút dải đo vì có thể gặp vấn đề độ "
               "chính xác thấp. Ví dụ, một cảm biến thiết kế để làm việc ở 1.000 psi có thể không phân "
               "biệt được 20 với 25 psi. Phần lớn phần tử sơ cấp công bố độ chính xác theo phần trăm toàn "
               "thang. Một bộ chuyển đổi có độ chính xác công bố 1 % thật ra có thể sai 100 % khi đang đo "
               "1 % đầu tiên của thang."))
    b.append(p("Nói chung không nên dùng chung cảm biến với BPCS, vì những lý do sau:"))
    b.append(ul([
        "SIS có thể phải ra tay chính vì một thành phần của BPCS hỏng. Hỏng hóc của BPCS có thể là cảm "
        "biến, hệ logic hoặc phần tử cuối. Nếu một cảm biến trong BPCS hỏng và tạo ra mối nguy tiềm ẩn, "
        "thì việc cố vận hành SIS từ chính cảm biến đã hỏng ấy là điều vô nghĩa.",
        "Quy trình thử, hiệu chuẩn và bảo trì SIS thường chặt chẽ hơn của BPCS. Tính toàn vẹn của hệ an "
        "toàn có thể bị xâm phạm nếu thay đổi cảm biến của nó mà không theo đúng quy trình.",
        "Có thể không thử được thiết bị trường dùng chung khi đang vận hành.",
    ]))
    b.append(p("Lập luận trên cũng đúng cho phần tử cuối."))

    b.append(h3("9.3.2 Công tắc", "Switches"))
    b.append(p("Công tắc rời rạc không cung cấp bất kỳ dạng thông tin chẩn đoán nào. Ví dụ, nếu trong vận "
               "hành bình thường một công tắc áp suất có bộ tiếp điểm báo động đang đóng, được thiết kế để "
               "mở khi áp suất thấp, mà các tiếp điểm ấy bị kẹt và không mở được, thì cảm biến không có "
               "cách nào phát hiện hay thông báo hư hỏng đó. Cách duy nhất để biết thiết bị ấy có làm việc "
               "hay không là thử định kỳ."))
    b.append(p("Công tắc rời rạc/bật-tắt đã được dùng trong quá khứ vì những lý do sau:"))
    b.append(ul([
        "phần lớn chức năng dừng là rời rạc (bật/tắt, mở/đóng)",
        "logic rơ-le rời rạc từng được dùng rộng rãi",
        "PLC nguyên thuỷ được thiết kế cho vào/ra rời rạc",
        "chi phí thấp hơn",
    ]))
    b.append(p("Để khắc phục phần nào nhược điểm của thiết bị rời rạc, tĩnh tại (tức thiếu chẩn đoán), có "
               "thể dùng một bộ điều khiển chỉ thị khí nén bật/tắt có cảm biến tích hợp làm cảm biến "
               "chính. Điểm đặt của bộ điều khiển sẽ đặt tại giá trị cắt của quá trình. Tín hiệu ra của bộ "
               "điều khiển khí nén sẽ là 3 hoặc 15 psi. Tín hiệu ấy có thể dẫn ống tới một công tắc áp "
               "suất đặt ở 9 psi, và tiếp điểm của công tắc này đấu vào hệ logic điện (rơ-le), điện tử "
               "(bán dẫn rắn) hay dựa trên phần mềm (PLC)."))
    b.append(p("Một số ưu điểm của việc dùng bộ điều khiển bật/tắt:"))
    b.append(ol([
        "chỉ thị tại chỗ biến quá trình",
        "dễ thử một phần khi đang vận hành — có thể đổi điểm đặt của bộ điều khiển để kích hoạt một lần "
        "cắt",
        "độ chính xác, dải đo và độ tin cậy tốt hơn so với công tắc",
        "có thể khoá chìa bộ điều khiển để bảo đảm an ninh",
    ]))

    b.append(h3("9.3.3 Bộ chuyển đổi", "Transmitters"))
    b.append(p("Bộ chuyển đổi cung cấp tín hiệu tương tự theo biến vào. Điều này ít nhất cũng cho biết, "
               "trong một mức độ hạn chế, thiết bị có đang hoạt động hay không. Có thông tin vẫn hơn không "
               "có gì. Tuy nhiên, nếu đầu ra động của bộ chuyển đổi không bao giờ được người vận hành hay "
               "hệ logic theo dõi thay đổi, thì lượng thông tin dùng được có thể chẳng hơn gì một công tắc "
               "rời rạc. Giống như có một máy in màu nhưng chỉ in tài liệu đen trắng: lợi ích cảm nhận "
               "được từ chiếc máy in màu là ảo, nếu ta không dùng được nó."))
    b.append(p("Dù có thể đắt hơn công tắc rời rạc, bộ chuyển đổi tương tự thường được ưa chuộng vì:"))
    b.append(ul([
        "nhiều chẩn đoán hơn",
        "có chỉ thị tại chỗ",
        "suất hỏng an toàn và nguy hiểm thấp hơn",
        "so sánh được tín hiệu với BPCS",
        "một bộ chuyển đổi có thể thay nhiều công tắc",
        "độ chính xác và độ lặp tốt hơn công tắc",
    ]))
    b.append(p("Thường có thể đặt trước chế độ hỏng của bộ chuyển đổi (tức đọc 0 % hoặc 100 %). (Lưu ý: "
               "nếu cảm biến chỉ có 30 % chẩn đoán — mức giới hạn của nhiều loại — thì cảm biến sẽ không "
               "phải lúc nào cũng đi đúng về chế độ hỏng đã chọn khi cần.) Ngoài ra, bằng cách phân tích "
               "tín hiệu 4–20 mA từ bộ chuyển đổi, có thể xác định tình trạng hoạt động của thiết bị (ví "
               "dụ dòng nhỏ hơn 4 mA hoặc lớn hơn 20 mA cho thấy bộ chuyển đổi đã hỏng)."))
    b.append(p("Cũng có thể xét dùng bộ giám sát báo động theo giao thức HART (highway addressable remote "
               "transducer). (Thiết bị cho giao thức khác cũng có, nhưng phần này chỉ bàn HART.) Bộ chuyển "
               "đổi thông minh có giao thức HART có khả năng cung cấp rất nhiều dữ liệu ngoài tín hiệu đo "
               "4–20 mA đơn thuần. Bằng cách nối một bộ giám sát báo động HART vào một bộ chuyển đổi "
               "4–20 mA, bộ giám sát có thể cung cấp tín hiệu báo hỏng bộ chuyển đổi song song với tín "
               "hiệu quá trình. Điều này có tiềm năng nâng độ phủ chẩn đoán và cải thiện hiệu năng an toàn "
               "của cả hệ. Bộ giám sát có thể phát tín hiệu báo hỏng bộ chuyển đổi nếu một trong các điều "
               "kiện sau xảy ra:"))
    b.append(ul([
        "bộ chuyển đổi trục trặc",
        "đầu vào cảm biến ra ngoài dải",
        "đầu ra tương tự của bộ chuyển đổi bị đóng băng",
        "đầu ra tương tự ra ngoài dải",
    ]))
    b.append(p("Nhờ những chẩn đoán trên, độ phủ chẩn đoán của bộ chuyển đổi có thể tăng khoảng 20 %. Cần "
               "thực hiện phân tích chế độ hỏng, ảnh hưởng và chẩn đoán (FMEDA) chi tiết để xác định mức "
               "phủ chẩn đoán chính xác."))
    b.append(p("Hai tín hiệu — từ bộ chuyển đổi và từ bộ giám sát báo động — có thể được đấu vào hệ logic "
               "để tạo ra tín hiệu báo động hoặc tín hiệu dừng (xem mục 9.5 và Bảng 9-2 để phân tích thêm)."))
    b.append(fig(2, F.fig_9_2(), "vi"))

    b.append(h3("9.3.4 Chẩn đoán cảm biến", "Sensor Diagnostics"))
    b.append(p("Cải thiện chẩn đoán (tức độ phủ chẩn đoán) của một hệ an toàn sẽ cải thiện hiệu năng an "
               "toàn của hệ. Nói cách khác, nó làm giảm xác suất hỏng khi có yêu cầu (PFD), tức làm tăng "
               "hệ số giảm rủi ro (RRF = 1/PFD). Công thức sau cho thấy ảnh hưởng của độ phủ chẩn đoán lên "
               "suất hỏng nguy hiểm."))
    b.append(eq("λ<sub>DD</sub> = λ<sub>d</sub> · C<sub>d</sub>", "9.2"))
    b.append(eq("λ<sub>DU</sub> = λ<sub>d</sub> · (1 − C<sub>d</sub>)", "9.3"))
    b.append(p("trong đó C<sub>d</sub> là hệ số phủ chẩn đoán của hư hỏng nguy hiểm; λ<sub>d</sub> là tổng "
               "suất hỏng nguy hiểm; λ<sub>DD</sub> là suất hỏng nguy hiểm, phát hiện được; "
               "λ<sub>DU</sub> là suất hỏng nguy hiểm, ẩn."))
    b.append(p("Tăng hệ số phủ chẩn đoán của hư hỏng nguy hiểm (C<sub>d</sub>) sẽ làm tăng suất hỏng nguy "
               "hiểm phát hiện được (λ<sub>DD</sub>) và giảm suất hỏng nguy hiểm, ẩn (λ<sub>DU</sub>). Lưu "
               "ý rằng chẩn đoán không thay đổi tổng suất hỏng, chỉ thay đổi tỷ lệ hư hỏng được phát hiện."))
    b.append(p("Một lợi ích của việc tăng chẩn đoán là người thiết kế hệ an toàn có lựa chọn dừng quá "
               "trình hoặc chỉ phát báo động khi phát hiện hư hỏng nguy hiểm ở một cảm biến. Nói cách "
               "khác, thay vì dừng sản xuất vì một cảm biến hỏng, hệ có thể đặt bypass tín hiệu hỏng ấy "
               "cho đến khi sửa xong. Dĩ nhiên phải có quy trình bảo đảm an toàn trong khi thiết bị đang bị "
               "bypass."))
    b.append(p("Lý tưởng là có cảm biến với 100 % chẩn đoán, và vì thế không có hư hỏng nguy hiểm, ẩn nào. "
               "Đáng tiếc là 100 % chẩn đoán là không thể; mục tiêu là đưa nó cao đến mức có thể."))
    b.append(p("Một thông số mới hơn dùng để biểu thị hiệu quả của chẩn đoán là tỷ lệ hư hỏng an toàn "
               "(SFF). Tỷ lệ hư hỏng an toàn được định nghĩa là tỷ số giữa tổng suất hỏng an toàn cộng "
               "suất hỏng nguy hiểm phát hiện được, chia cho tổng suất hỏng. Có thể biểu diễn bằng công "
               "thức dưới đây. Tỷ lệ hư hỏng an toàn có thể xác định cho từng thành phần trong hệ (cảm "
               "biến, logic hoặc phần tử cuối)."))
    b.append(eq("SFF = (λ<sub>SD</sub> + λ<sub>SU</sub> + λ<sub>DD</sub>) / "
                "(λ<sub>SD</sub> + λ<sub>SU</sub> + λ<sub>DD</sub> + λ<sub>DU</sub>)", "9.4"))
    b.append(p("Có thể giảm nhu cầu bảo trì định kỳ và thử bằng tay bằng cách cải thiện chẩn đoán cảm "
               "biến."))
    b.append(p("Một phương pháp đơn giản nhưng hiệu quả để cải thiện chẩn đoán cảm biến là so sánh tín "
               "hiệu của một bộ chuyển đổi với các biến liên quan khác (ví dụ bộ chuyển đổi của hệ điều "
               "khiển đang đọc cùng biến quá trình). Sai lệch giữa hai tín hiệu sẽ chỉ ra những vấn đề mà "
               "một thiết bị đơn lẻ có thể không tự chẩn đoán được. Ngoài ra, bộ chuyển đổi thông minh "
               "thường cung cấp mức chẩn đoán cao hơn bộ chuyển đổi thông thường (xem mục 9.3.5)."))
    b.append(p("Hiện đã có bộ chuyển đổi được chứng nhận cho ứng dụng an toàn. Chúng thường được gọi là "
               "“bộ chuyển đổi an toàn” để phân biệt với bộ chuyển đổi tiêu chuẩn. Khác biệt chính là "
               "những thiết bị này cung cấp mức chẩn đoán cao hơn, và thường có mạch bên trong dự phòng, "
               "so với bộ chuyển đổi thông thường hay thông minh. Cuốn <em>Safety-Related Field "
               "Instruments for the Process Industries</em> của Rainer Faller cung cấp thêm thông tin về "
               "việc dùng những bộ chuyển đổi này. [Ref. 4]"))

    b.append(h3("9.3.5 Bộ chuyển đổi thông minh", "Smart Transmitters"))
    b.append(p("Một số ưu điểm của bộ chuyển đổi thông minh (tức bộ chuyển đổi có thêm chẩn đoán và truyền "
               "thông số, thay vì loại “thông thường” chỉ có đầu ra tương tự 4–20 mA) trong ứng dụng an "
               "toàn:"))
    b.append(ol([
        "độ chính xác tốt hơn bộ chuyển đổi thông thường",
        "trôi dài hạn không đáng kể và độ ổn định rất tốt",
        "chẩn đoán tốt hơn: hiện đã đạt hệ số phủ chẩn đoán và SFF lớn hơn 80 % dựa trên phân tích chế "
        "độ hỏng, ảnh hưởng và chẩn đoán (FMEDA)",
        "chế độ hỏng dự đoán được tốt hơn",
        "khả năng hiệu chuẩn, bảo trì từ xa *",
        "kỹ thuật viên bảo trì ít phải tiếp xúc môi trường nguy hiểm hơn *",
        "có thể không cần giấy phép làm việc an toàn đặc biệt nhờ khả năng bảo trì từ xa *",
    ]))
    b.append(p("* Lưu ý: việc chỉnh các thông số liên quan quá trình của cảm biến phải được bảo vệ và "
               "kiểm soát, chống thay đổi trái phép và/hoặc vô ý."))
    b.append(p("Một số nhược điểm của bộ chuyển đổi thông minh:"))
    b.append(ol([
        "dễ đổi thông số (ví dụ dải đo) mà không bảo đảm thay đổi ấy được phản ánh trong logic và các hệ "
        "khác",
        "dễ để sót bộ chuyển đổi ở chế độ thử hoặc “đầu ra cưỡng bức”",
        "chi phí — bộ chuyển đổi thông minh đắt hơn bộ chuyển đổi thông thường",
        "đáp ứng có thể chậm hơn bộ chuyển đổi tương tự thông thường",
    ]))
    b.append(p("Dù còn những nhược điểm trên, bộ chuyển đổi thông minh ngày càng được dùng nhiều trong ứng "
               "dụng an toàn."))

    # ------------------------------------------------------------------ 9.4
    b.append(h2("9.4 Phần tử cuối", "Final Elements"))
    b.append(p("Dưới đây bàn những vấn đề chung về van và chẩn đoán."))

    b.append(h3("9.4.1 Chung", "General"))
    b.append(p("Phần tử cuối là thiết bị dùng để thực hiện việc dừng an toàn một quá trình. Phần tử cuối "
               "phổ biến nhất là van điều khiển bằng điện từ, cấp khí cho một bộ truyền động màng hay "
               "pít-tông. Xả khí thường khiến van về trạng thái an toàn."))
    b.append(p("Phần tử cuối nói chung có suất hỏng cao nhất trong mọi thành phần của cả hệ. Chúng là thiết "
               "bị cơ khí chịu điều kiện quá trình khắc nghiệt. Van dừng thường ở trạng thái mở và không "
               "được tác động trong thời gian dài, trừ khi thử. Một kiểu hỏng nguy hiểm thường gặp của "
               "những van này là kẹt. Một kiểu hỏng an toàn thường gặp là cuộn điện từ bị cháy."))
    b.append(p("Van phải an toàn khi mất nguồn. Van truyền động bằng màng và pít-tông thường cần bộ truyền "
               "động có lò xo hồi hoặc bình tích áp để an toàn khi mất khí. Van tác động kép (cấp khí để "
               "mở và cấp khí để đóng) được dùng khi cần van “giữ” vị trí cuối cùng khi mất khí, hoặc khi "
               "kích thước và chi phí của bộ truyền động một tác động có lò xo là không khả thi."))
    b.append(p("Các chế độ hỏng điển hình của phần tử cuối:"))
    b.append(h3("Van điện từ", "Solenoid Valves"))
    b.append(ul([
        "cháy cuộn dây",
        "tắc lỗ hoặc lỗ thông hơi",
        "ăn mòn đầu cực hay thân van làm van điện từ không hoạt động",
        "môi trường khắc nghiệt và/hoặc khí dụng cụ chất lượng kém gây kẹt",
    ]))
    b.append(h3("Van dừng", "Shutdown Valves"))
    b.append(ul([
        "van bị rò",
        "bộ truyền động không đủ lực để đóng ngược áp suất chặn",
        "thân van hoặc đế van bị kẹt dính",
        "đường khí bị tắc hoặc bị bẹp",
        "kẹt",
    ]))
    b.append(p("Có người dùng luôn van điều khiển của BPCS làm van dừng. Họ thấy có lợi vì van điều khiển "
               "luôn chuyển động, nên coi nó là “tự thử”. Như với cảm biến, nói chung không nên dùng chung "
               "phần tử cuối với BPCS (xem mục 9.3). Thêm những lý do khác khiến không nên dùng van điều "
               "khiển quá trình làm van dừng:"))
    b.append(ul([
        "Van điều khiển chiếm tỷ lệ lớn nhất trong số hư hỏng thiết bị đo.",
        "Van điều khiển quá trình được thiết kế cho khả năng điều khiển của chúng. Có những thông số quan "
        "trọng khác đối với van dừng mà có thể không được xét khi chọn van điều khiển (ví dụ độ rò, khả "
        "năng chịu cháy, tốc độ đáp ứng…).",
    ]))
    b.append(p("Bất chấp những nguyên tắc chung ấy, van điều khiển quá trình có thể được dùng để thực hiện "
               "chức năng dừng trong trường hợp lắp một van dừng riêng là không thực tế hoặc không hiệu "
               "quả về chi phí. Khuyến nghị trong những trường hợp đó có thể gồm: dẫn ống từ van điện từ "
               "thẳng tới bộ truyền động, bỏ qua bộ định vị van; hoặc dùng van điện từ dự phòng. Cũng cần "
               "chọn cỡ van điện từ cẩn thận để bảo đảm tốc độ đáp ứng đủ của van chính. Phải xây dựng một "
               "hồ sơ an toàn chứng minh rằng rủi ro gắn với việc dùng một van chung là chấp nhận được."))
    b.append(p("Một số ngoại lệ tiềm tàng cho những nguyên tắc trên là động cơ khởi động và các hệ truyền "
               "động phi điện."))

    b.append(h3("9.4.2 Chẩn đoán van", "Valve Diagnostics"))
    b.append(p("Van dừng phải hoạt động khi có tín hiệu từ hệ logic gửi tới. Trong vận hành bình thường, "
               "những van này thường mở hoàn toàn và ở nguyên trạng thái đó trong thời gian dài, trừ khi "
               "được thử hoặc được hệ logic tác động theo cách nào đó. Cần xét chẩn đoán van cả khi van ở "
               "trạng thái ổn định bình thường (ví dụ đang mở) lẫn khi van được tác động."))
    b.append(p("<b>1. Vận hành bình thường.</b> Trong vận hành bình thường có thể dùng những kỹ thuật sau "
               "để chẩn đoán trạng thái van:"))
    b.append(ul([
        "thử bằng tay khi đang vận hành (xem chương 12)",
        "dùng bộ định vị van thông minh (xem mục 9.4.3)",
        "báo động nếu van đổi trạng thái mà không có tín hiệu từ hệ logic",
        "thử hành trình một phần. Thử van tự động bằng cách để hệ logic tự dịch van một tỷ lệ nhỏ và "
        "theo dõi chuyển động. Một cách khác là để hệ logic gửi tín hiệu tới van trong một khoảng thời "
        "gian định trước (thường vài giây, tuỳ động học của van và quá trình). Nếu trong khoảng thời gian "
        "ấy hệ logic không thấy chuyển động qua một chỉ thị vị trí, một báo động sẽ được kích hoạt, cho "
        "thấy vấn đề tiềm ẩn của hệ. Có thể phải lắp thêm linh kiện để làm được việc này. Có nhiều kỹ "
        "thuật khác để thực hiện thử hành trình một phần.",
    ]))
    b.append(p("<b>2. Khi được tác động.</b> Công tắc hành trình hoặc chỉ thị vị trí được lắp để phản hồi "
               "cho biết van đã hoạt động đúng hay không. Không nên coi những chẩn đoán này là “chủ động”. "
               "Nếu van không chạy trong một thời gian dài, công tắc hành trình sẽ không cho biết khi van "
               "thật sự hỏng kẹt."))

    b.append(h3("9.4.3 Bộ định vị van thông minh", "Smart Valve Positioners"))
    b.append(p("Có người đã lắp bộ định vị van thông minh trên van dừng để có thêm dữ liệu chẩn đoán về "
               "tình trạng của van. Bộ định vị có thể được lắp chỉ để cung cấp dữ liệu chẩn đoán, hoặc có "
               "thể được dùng để tác động van. Trong trường hợp sau, tín hiệu dừng từ hộp logic được nối "
               "trực tiếp tới bộ định vị. Thông tin có thể lấy từ bộ định vị van thông minh gồm:"))
    b.append(ul([
        "phản hồi vị trí",
        "vấn đề về nguồn khí hoặc bộ truyền động",
        "trạng thái công tắc hành trình",
        "trạng thái vị trí van",
        "báo động và tự chẩn đoán của bộ định vị",
    ]))
    b.append(p("Nhiều bộ định vị thông minh cho phép thử hành trình một phần cho van dừng, tại chỗ hoặc từ "
               "xa. Thử hành trình một phần là một cách đáp ứng yêu cầu cho ứng dụng SIL 2 và SIL 3. Phép "
               "thử này thường dịch van khoảng 10 % và cho hệ số phủ chẩn đoán từ 60 đến 90 %. Van sẽ được "
               "thử hoàn toàn (tức đóng hẳn) trong lần bảo dưỡng lớn của nhà máy. Có nhiều giải pháp thử "
               "hành trình một phần bán trên thị trường (và đã được chứng nhận). Mục 8.13.1 cho thấy ảnh "
               "hưởng của việc thử hành trình một phần lên hiệu năng."))

    # ------------------------------------------------------------------ 9.5
    b.append(h2("9.5 Dự phòng", "Redundancy"))
    b.append(p("Nếu không thể chấp nhận hư hỏng của bất kỳ cảm biến đơn lẻ nào (tức không chấp nhận cắt "
               "nhầm hay không hành động), hoặc nếu một cảm biến đơn không đáp ứng được yêu cầu hiệu "
               "năng, thì có thể dùng cảm biến dự phòng hoặc nhiều cảm biến. Lý tưởng là khả năng hai cảm "
               "biến hỏng cùng lúc phải rất nhỏ. Đáng tiếc là điều này không tính đến nguyên nhân chung "
               "hay hư hỏng hệ thống có thể đánh vào nhiều cảm biến cùng lúc. Hư hỏng do nguyên nhân chung "
               "thường gắn với yếu tố môi trường bên ngoài như nhiệt, rung, ăn mòn và tắc nghẽn, hoặc với "
               "sai sót của con người. Nếu dùng nhiều cảm biến, nên đấu chúng vào quá trình qua những điểm "
               "lấy mẫu khác nhau (nếu có thể) và dùng nguồn riêng, để tránh tắc nghẽn và mất nguồn do "
               "nguyên nhân chung. Cũng có thể xét dùng cảm biến của các hãng khác nhau, và để những người "
               "bảo trì khác nhau làm việc trên chúng, nhằm tránh khả năng sai sót thiết kế hoặc sai sót "
               "của con người."))
    b.append(p("Mỗi khi dùng bộ chuyển đổi dự phòng, nên xét dùng công nghệ khác nhau (ví dụ đo mức bằng cả "
               "phép đo áp suất vi sai và một đầu dò điện dung). Cả hai cảm biến phải có lịch sử hiệu năng "
               "đã được chứng minh trong ứng dụng như vậy. Nếu chỉ một cảm biến có thành tích đã được "
               "chứng minh, thì tốt nhất có thể là dùng chính thiết bị ấy cho cả hai cảm biến. Dùng công "
               "nghệ đa dạng tuy làm giảm khả năng gặp vấn đề nguyên nhân chung, nhưng lại kéo theo những "
               "bất lợi khác cần xét (ví dụ phụ tùng dự trữ, đào tạo, bảo trì, thiết kế…)."))
    b.append(p("Dự phòng đa dạng dùng công nghệ, thiết kế, nhà sản xuất, phần mềm, phần sụn… khác nhau để "
               "giảm ảnh hưởng của lỗi nguyên nhân chung. Nên xét dự phòng đa dạng nếu cần giảm nguyên "
               "nhân chung để đạt SIL yêu cầu (xem mục 8.12.1). Không nên dùng dự phòng đa dạng khi việc "
               "áp dụng nó có thể dẫn đến dùng những linh kiện có độ tin cậy thấp hơn, không đáp ứng yêu "
               "cầu độ tin cậy của hệ. Hư hỏng hệ thống không bị ngăn ngừa bằng dự phòng, tuy có thể giảm "
               "bớt nếu dùng dự phòng đa dạng."))

    b.append(h3("9.5.1 Sơ đồ bỏ phiếu và dự phòng", "Voting Schemes and Redundancy"))
    b.append(p("Mức dự phòng và cách bỏ phiếu cần thiết phụ thuộc nhiều yếu tố (yêu cầu SIL, tỷ lệ cắt "
               "nhầm mong muốn, tần suất thử, suất hỏng và chế độ hỏng của thành phần, chẩn đoán…). Bảng "
               "dưới đây cho thấy những cấu hình thường dùng với cảm biến và phần tử cuối. Mục 8.8 bàn chi "
               "tiết hơn về dự phòng."))
    b.append(table(
        ["Cấu hình", "Ý nghĩa"],
        [
            ["<b>Cảm biến</b>", ""],
            ["1oo1", "1 trong 1 (một cảm biến). Dùng khi thành phần đáp ứng được yêu cầu hiệu năng."],
            ["1oo1D", "1 trong 1 có chẩn đoán. Chẩn đoán có thể do một bộ giám sát báo động bổ sung cung "
                      "cấp, hoặc tích hợp trong cảm biến (tức cảm biến an toàn đã chứng nhận). Xem "
                      "Bảng 9-2."],
            ["1oo2", "1 trong 2. Lắp hai cảm biến nhưng chỉ cần một để dừng. Cấu hình này an toàn hơn "
                     "1oo1 nhưng số lần cắt nhầm gấp đôi."],
            ["1oo2D", "1 trong 2 có chẩn đoán. Chẩn đoán có thể do bộ giám sát báo động bổ sung hoặc tích "
                      "hợp trong cảm biến. Cấu hình này “chịu lỗi” và sống được qua một hư hỏng an toàn "
                      "hoặc nguy hiểm đơn lẻ, vẫn tiếp tục hoạt động đúng."],
            ["2oo2", "2 trong 2. Lắp hai cảm biến và cần cả hai để dừng. Sơ đồ này kém an toàn hơn 1oo1 "
                     "nhưng ít cắt nhầm hơn."],
            ["2oo3", "2 trong 3. Lắp ba cảm biến và cần hai để dừng. Như 1oo2D, cấu hình này cũng “chịu "
                     "lỗi” và sống được qua một hư hỏng an toàn hoặc nguy hiểm đơn lẻ."],
            ["<b>Phần tử cuối</b>", ""],
            ["1oo1", "Một van. Dùng khi thiết bị đáp ứng yêu cầu hiệu năng."],
            ["1oo2", "1 trong 2. Lắp hai van nhưng chỉ cần một để dừng. Như với cảm biến, sơ đồ này an "
                     "toàn hơn 1oo1 nhưng dễ bị cắt nhầm gấp đôi."],
            ["2oo2", "2 trong 2. Lắp hai van và cần cả hai để dừng. Như với cảm biến, sơ đồ này kém an "
                     "toàn hơn 1oo1 nhưng ít cắt nhầm hơn."],
        ],
        caption="Các cấu hình dự phòng thường dùng cho cảm biến và phần tử cuối. Bảng này không được đánh "
                "số trong bản gốc; bản dịch giữ nguyên như vậy để không xô lệch số hiệu của Bảng 9-2."))

    b.append(h3("9.5.1.1 Logic bỏ phiếu cho cấu hình 1oo1D", "Voting Logic for 1oo1D Configurations"))
    b.append(p("Hình 9-2 cho thấy có thể dùng một bộ chuyển đổi thông minh có chẩn đoán để giảm suất hỏng "
               "nguy hiểm, ẩn λ<sub>DU</sub> như thế nào."))
    b.append(p("Với hệ trên, bộ chuyển đổi có chẩn đoán và giao thức HART. Bộ giám sát báo động HART kiểm "
               "tra tín hiệu số HART của bộ chuyển đổi và phát báo động nếu biến quá trình ra ngoài giới "
               "hạn đặt, hoặc nếu chẩn đoán bên trong bộ giám sát phát hiện hư hỏng. Cách này giống với "
               "hoạt động của bộ chuyển đổi an toàn. Bảng 9-2 dưới đây cho thấy các trạng thái có thể có "
               "của một bộ chuyển đổi đơn."))
    b.append(table(
        ["Trạng thái", "Trạng thái quá trình do bộ chuyển đổi cảm nhận<br>(1 = không cắt, 0 = cắt)",
         "Trạng thái bộ chuyển đổi do chẩn đoán cảm nhận<br>(1 = không lỗi, 0 = phát hiện hỏng)",
         "Trạng thái logic 1oo1D"],
        [
            ["1", "1", "1", "OK"],
            ["2", "0", "1", "Cắt"],
            ["3", "1", "0", "Cắt hoặc báo động"],
            ["4", "0", "0", "Cắt hoặc báo động"],
        ],
        caption="Bảng 9-2. Các trạng thái logic 1oo1D. <br>Điều kiện 1: trạng thái quá trình bình thường "
                "(OK) và không phát hiện lỗi ở bộ chuyển đổi. <br>Điều kiện 2: trạng thái quá trình ra "
                "ngoài giới hạn bình thường và không phát hiện lỗi ở bộ chuyển đổi — trạng thái cắt. "
                "<br>Điều kiện 3 và 4: trạng thái quá trình được coi là không xác định vì đã phát hiện lỗi "
                "ở bộ chuyển đổi. Hệ logic có thể được lập trình để cắt hoặc báo động trong những điều "
                "kiện này. Lựa chọn nào cũng ảnh hưởng đến hiệu năng an toàn và hiệu năng nguy hiểm tổng "
                "của hệ. <br><b>Lưu ý:</b> phải luôn phát báo động nếu bộ chuyển đổi có lỗi."))
    b.append(p("Có thể tính PFD<sub>avg</sub>, RRF (1/PFD) và MTTF<sub>spurious</sub> cho một bộ chuyển đổi "
               "điển hình ở cấu hình 1oo1 và 1oo1D. Giả sử số liệu sau: MTTF<sub>s</sub> = 25 năm; "
               "MTTF<sub>d</sub> = 50 năm; TI = 1 năm; C<sub>d</sub> = 60 %; MTTR = 12 giờ; λ = 1/MTTF; "
               "λ<sub>DD</sub> = λ<sub>d</sub>C<sub>d</sub>; λ<sub>DU</sub> = λ<sub>d</sub>(1 − "
               "C<sub>d</sub>)."))
    b.append(p("Với cấu hình 1oo1:"))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>d</sub> · TI/2 = 0,02 · 1/2 = 0,01", "9.5"))
    b.append(eq("MTTF<sub>spurious</sub> = 1/λ<sub>s</sub> = 25 năm", "9.6"))
    b.append(p("Với cấu hình 1oo1D:"))
    b.append(eq("MTTF<sub>spurious</sub> = 1/λ<sub>s</sub> = 25 năm", "9.7"))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>DD</sub> · MTTR + λ<sub>DU</sub> · TI/2 = 0,004", "9.8"))
    b.append(p("Với cấu hình 1oo1D đã mô hình hoá ở trên, PFD<sub>avg</sub> giảm, tuy không đáng kể. Một bộ "
               "chuyển đổi an toàn đã chứng nhận sẽ cho hiệu năng tốt hơn nữa, vì hệ số phủ chẩn đoán của "
               "nó vào khoảng 90 %."))
    b.append(table(
        ["Cấu hình", "PFD<sub>avg</sub>", "RRF", "MTTF<sub>spurious</sub> (năm)"],
        [
            ["1oo1", "0,01", "100", "25"],
            ["1oo1D", "0,004", "250", "25"],
        ],
        caption="Bảng so sánh 1oo1 và 1oo1D với cùng số liệu. Chẩn đoán không làm thay đổi số lần cắt "
                "nhầm — nó chỉ chuyển hư hỏng nguy hiểm từ “ẩn” sang “phát hiện được”, và nhờ đó cắt PFD "
                "xuống 2,5 lần."))
    b.append(fig(3, F.fig_9_3(), "vi"))

    # ------------------------------------------------------------------ 9.6
    b.append(h2("9.6 Yêu cầu thiết kế cho thiết bị trường", "Design Requirements for Field Devices"))
    b.append(p("Thiết bị trường là phần không tách rời của hệ an toàn tổng thể. Vì thế chúng phải được "
               "chọn, thiết kế và lắp đặt để đáp ứng yêu cầu hiệu năng (SIL) của từng chức năng an toàn "
               "(SIF)."))
    b.append(p("Như đã bàn ở chương 3 và các mục trên, thiết bị trường cho hệ an toàn phải tách biệt và "
               "độc lập với hệ điều khiển quá trình cơ bản (BPCS) và các hệ không liên quan an toàn khác. "
               "(Luôn có ngoại lệ, ví dụ khi dùng cảm biến dự phòng, miễn là không hư hỏng đơn lẻ nào gây "
               "được vấn đề.) Dùng chung cảm biến với BPCS có thể tạo ra vấn đề về bảo trì và quy trình "
               "(ví dụ an ninh, đổi dải đo, thử…). Để đạt được tính độc lập cần thiết, những thành phần "
               "sau phải tách khỏi BPCS:"))
    b.append(ul([
        "cảm biến trường, điểm lấy mẫu, van gốc và đường xung áp",
        "phần tử cuối (ví dụ van điện từ, van dừng chính…)",
        "cáp, hộp nối, đường khí và bảng đấu liên quan đến vào/ra, cùng các bảng điều khiển riêng cho hệ "
        "an toàn",
        "nguồn cấp",
    ]))
    b.append(p("Nếu tín hiệu thiết bị trường của hệ an toàn được gửi sang BPCS để ghi dữ liệu hoặc so sánh, "
               "thì tín hiệu giữa hai hệ phải được cách ly (ví dụ dùng bộ cách ly quang) để một hư hỏng đơn "
               "lẻ không ảnh hưởng cả hai hệ."))
    b.append(p("Việc lắp đặt thiết bị trường phải tuân thủ các quy định địa phương và mọi quy định liên "
               "bang liên quan. Thiết bị trường phải “an toàn khi hỏng”. Trong phần lớn trường hợp, điều "
               "này có nghĩa thiết bị thường có điện; ngắt điện hay mất nguồn sẽ khởi phát một lệnh dừng."))
    b.append(p("Hệ “đánh thức để cắt” được dùng để giảm những lần cắt nhầm nguy hiểm tiềm ẩn do mất nguồn, "
               "sụt áp, hỏng linh kiện và đứt dây. Trong trường hợp đó, mạch hở không có điện sẽ dùng cách "
               "giám sát đường dây — còn gọi là mạch có giám sát — cần một linh kiện cuối đường và việc "
               "theo dõi một dòng điện nhỏ. Cách này cho phép hệ logic phân biệt mạch thường hở, mạch "
               "đóng, ngắn mạch dây, hay đứt dây."))
    b.append(p("Chỉ nên dùng công nghệ đã được chứng minh trong ứng dụng an toàn. Phải có thành tích đã "
               "được chứng minh và được chấp nhận trước khi dùng thiết bị trường trong hệ an toàn."))

    b.append(h3("9.6.1 Yêu cầu thiết kế cảm biến", "Sensor Design Requirements"))
    b.append(p("Cần xét những yêu cầu chung sau:"))
    b.append(ul([
        "Hệ an toàn khi hỏng phải dùng tiếp điểm thường đóng và mạch thường có điện.",
        "Cảm biến phải được đấu trực tiếp vào hệ logic. Không được đấu vào bất kỳ hệ nào khác không "
        "thuộc hệ dừng.",
        "Bộ chuyển đổi thông minh ngày càng được dùng nhiều cho hệ an toàn vì chẩn đoán tốt hơn và độ tin "
        "cậy cao hơn. Khi dùng loại này, phải có quy trình bảo đảm không thể để chúng ở chế độ “đầu ra "
        "cưỡng bức”. Cần có quy trình quản lý thay đổi và kiểm soát truy cập để cho phép thay đổi cấu "
        "hình hoặc hiệu chuẩn.",
        "Tiếp điểm của công tắc điện phải được bịt kín hoàn toàn để có độ tin cậy cao hơn.",
        "Có thể dùng bộ khuếch đại cắt điện tử/rơ-le dòng đấu với bộ chuyển đổi trường tương tự chuyên "
        "dụng của hệ an toàn, làm đầu vào cho hệ logic rời rạc (ví dụ rơ-le).",
        "Cảm biến trường thuộc hệ an toàn phải được phân biệt bằng cách nào đó với cảm biến của BPCS (ví "
        "dụ nhãn riêng, hệ thống số hiệu riêng, hoặc màu riêng).",
        "Khi dùng cảm biến dự phòng, phải có báo động sai lệch để chỉ ra hư hỏng của một cảm biến đơn.",
    ]))

    b.append(h3("9.6.1.1 Cảm biến lưu lượng", "Flow Sensors"))
    b.append(p("Dù tấm tiết lưu chiếm phần lớn ứng dụng và đủ “đã được chứng minh” cũng như đủ tin cậy "
               "trong hầu hết trường hợp, lưu lượng kế xoáy và lưu lượng kế điện từ có thể có ưu thế như "
               "dễ lắp đặt hơn và hiệu năng tốt hơn."))

    b.append(h3("9.6.1.2 Cảm biến nhiệt độ", "Temperature Sensors"))
    b.append(p("Chế độ hỏng chính của cặp nhiệt điện là đứt; vì thế phải dùng phát hiện đứt và báo động."))
    b.append(p("Với hệ không an toàn khi hỏng, có thể xét chỉ thị đứt về phía cao cho nhiệt độ thấp, và về "
               "phía thấp cho nhiệt độ cao."))

    b.append(h3("9.6.1.3 Cảm biến áp suất", "Pressure Sensors"))
    b.append(p("Bộ chuyển đổi áp suất dễ lắp và rất tin cậy. Những lưu ý chính khi chọn thiết bị áp suất:"))
    b.append(ul([
        "<b>Chọn dải đo</b> — bảo đảm giá trị đặt cắt nằm trong khoảng 30 đến 70 % dải của bộ chuyển đổi.",
        "Cần có phương tiện chỉnh điểm không cho bộ chuyển đổi.",
        "Việc lắp đặt phải bảo đảm nước ngưng tích tụ không gây dịch chuyển điểm hiệu chuẩn.",
        "Dùng màng niêm kín từ xa thay cho ống nhánh dài có thể hiệu quả trong việc loại bỏ vấn đề của "
        "ống nhánh.",
    ]))

    b.append(h3("9.6.1.4 Cảm biến mức", "Level Sensors"))
    b.append(p("Hệ thổi bọt có sục khí hoặc nitơ đã được chứng minh là tin cậy và nói chung cần ít bảo "
               "trì, tuy điều này dĩ nhiên tuỳ ứng dụng. Bộ chuyển đổi áp suất với hệ mao dẫn niêm kín "
               "cũng rất tin cậy và cần rất ít bảo trì. Phao, radar, siêu âm, đầu dò điện dung và thiết bị "
               "hạt nhân cũng được dùng cho nhiều ứng dụng."))

    b.append(h3("9.6.2 Yêu cầu thiết kế phần tử cuối", "Final Element Design Requirements"))
    b.append(p("Sau một lần cắt, phần tử cuối nói chung phải giữ ở trạng thái an toàn (đã dừng) cho đến khi "
               "được đặt lại bằng tay. Chỉ nên cho chúng trở về trạng thái bình thường nếu các yếu tố khởi "
               "phát cắt đã trở về điều kiện vận hành bình thường. Khi chọn phần tử cuối cần xét:"))
    b.append(ul([
        "tốc độ mở/đóng",
        "áp suất vi sai chặn theo cả hai chiều dòng",
        "độ rò",
        "khả năng chịu cháy",
        "độ phù hợp/tương thích của vật liệu",
        "yêu cầu chẩn đoán",
        "trạng thái an toàn khi hỏng của van (tức hỏng mở hay hỏng đóng)",
        "nhu cầu về chỉ thị vị trí hoặc công tắc hành trình",
        "kinh nghiệm/thành tích của thiết bị",
        "khả năng bảo trì khi đang vận hành",
    ]))

    b.append(h3("9.6.2.1 Bộ truyền động và van", "Actuators and Valves"))
    b.append(p("Nên tránh dùng kích tay trên van dừng để van không thể bị bỏ ở trạng thái bị kích hoặc "
               "không hoạt động. Nếu có lắp kích tay, phải niêm chì và phải có quy trình chính thức kiểm "
               "soát việc dùng chúng."))
    b.append(p("Có thể xét lắp van chặn và van bypass cho mỗi van hỏng ở trạng thái đóng. Với van hỏng ở "
               "trạng thái mở, có thể chỉ cần van chặn. Trường hợp dùng cả van chặn lẫn van bypass, có thể "
               "phải lắp thêm van xả phía trên van chặn phía hạ lưu. Có thể dùng công tắc hành trình để "
               "phát báo động nếu van bypass bị mở hoặc van chặn bị đóng. Một số công ty hài lòng với việc "
               "kiểm soát hoạt động của van chặn và van bypass bằng niêm chì và/hoặc bằng quy trình."))
    b.append(p("Nói chung, van chặn an toàn phải chuyên dụng và tách khỏi van điều khiển (xem mục 9.4 và "
               "chương 3). Được phép dùng chung van cho cả điều khiển và an toàn, nhưng phải xem xét và "
               "biện minh cẩn thận."))

    b.append(h3("9.6.2.2 Van điện từ", "Solenoids"))
    b.append(p("Van điện từ nguyên thuỷ được thiết kế để lắp trong môi trường phòng điều khiển. Sau những "
               "sửa đổi nhỏ cho dùng ngoài trời, nay chúng được dùng ở hiện trường, nơi chúng phải hoạt "
               "động liên tục trong điều kiện khắc nghiệt."))
    b.append(p("Nói chung, độ tin cậy của van điện từ thấp. Vì thế chúng có thể là một trong những thành "
               "phần quan trọng nhất (yếu nhất) của cả hệ. Một kiểu hỏng thường gặp là cuộn dây cháy, gây "
               "cắt nhầm. Điều quan trọng là dùng van điện từ loại công nghiệp tốt, nhất là khi dùng ngoài "
               "trời. Van phải chịu được nhiệt độ cao, kể cả nhiệt do chính cuộn dây sinh ra, cùng nhiệt từ "
               "lò, từ ánh nắng… Có loại hai cuộn dây để giữ van điện từ vẫn có điện nếu một cuộn cháy. "
               "Cũng có thể dùng cách bố trí van điện từ dự phòng."))
    b.append(p("Van điện từ công suất thấp (24 VDC) có vẻ tin cậy hơn vì công suất thấp nên ít sinh nhiệt. "
               "Tuy nhiên, van điện từ công suất rất thấp — như loại an toàn tia lửa (IS) — có thể cực kỳ "
               "tin cậy về mặt cháy cuộn dây, nhưng phải chọn cẩn thận vì nhiều loại là van điều khiển "
               "bằng áp lực mồi (pilot operated). Một số người dùng đã báo cáo vấn đề kẹt và tắc với van "
               "điều khiển bằng mồi (tuy điều này dĩ nhiên tuỳ ứng dụng và môi trường). Vì lý do ấy, một số "
               "người dùng thích loại van điện từ “đấu trực tiếp” (không qua mồi)."))
    b.append(p("Một người dùng cuối từng gặp vấn đề van điện từ do chất lượng khí dụng cụ kém. “Cách sửa” "
               "của họ là thay khí dụng cụ bằng nitơ. Đáng tiếc là nitơ rất khô lại tạo ra vấn đề khác với "
               "phần bên trong van điện từ, khiến 90 % số van bị kẹt. Như đã bàn ở chương 13, phải rất cẩn "
               "thận khi thay đổi. Những thay đổi làm với ý định tốt nhất (như phần lớn các thay đổi) có "
               "thể để lại tác dụng phụ nghiêm trọng."))

    # ------------------------------------------------------------------ 9.7
    b.append(h2("9.7 Những lưu ý khi lắp đặt", "Installation Concerns"))
    b.append(p("Những điều cần xét khi lắp đặt thiết bị trường:"))
    b.append(ul([
        "môi trường (nhiệt độ, rung, va đập, ăn mòn, độ ẩm, nhiễu điện từ/tần số vô tuyến)",
        "thử khi đang vận hành (nếu cần)",
        "yêu cầu bảo trì",
        "khả năng tiếp cận",
        "chỉ thị tại chỗ",
        "chống đông giá (nếu cần)",
    ]))
    b.append(p("Xem chương 11 để biết thêm chi tiết về các vấn đề lắp đặt."))

    # ------------------------------------------------------------------ 9.8
    b.append(h2("9.8 Đấu dây thiết bị trường", "Wiring of Field Devices"))
    b.append(p("Những kiểu hỏng dây dẫn thường gặp:"))
    b.append(ul(["hở/ngắn mạch", "chạm đất", "nhiễu/điện áp cảm ứng"]))
    b.append(p("Dưới đây là những hướng dẫn chung nhằm giảm thiểu vấn đề về dây dẫn:"))
    b.append(ul([
        "Tiêu chuẩn quy định “mỗi thiết bị trường phải có dây dẫn riêng” về hệ logic, trừ khi có một bus "
        "phù hợp đáp ứng yêu cầu hiệu năng.",
        "Tính đến thời điểm viết tài liệu này (mùa xuân 2005), chưa có fieldbus liên quan an toàn nào "
        "được dùng rộng rãi trong công nghiệp chế biến, tuy một số đang được phát triển (ví dụ "
        "FOUNDATION Fieldbus) và một số đã dùng trong ngành khác (ví dụ Profisafe, AS-i). Uỷ ban ISA SP84 "
        "hiện có một nhóm công tác đang xây dựng đặc tính kỹ thuật fieldbus an toàn mức cao. Uỷ ban nhận "
        "thức đầy đủ rằng fieldbus an toàn sẽ có cho công nghiệp chế biến trong tương lai gần, và vì thế "
        "mới có câu ngoại lệ ở gạch đầu dòng trên.",
        "Một thực hành khá phổ biến là đấu nhiều công tắc vào rời rạc vào một kênh vào của hệ logic để "
        "tiết kiệm dây và chi phí mô-đun vào. Tuy vậy, một nhược điểm của cách này là khó tìm lỗi và chẩn "
        "đoán vấn đề hơn. Đấu một đầu ra tới nhiều phần tử cuối cũng khá phổ biến và có thể chấp nhận "
        "được, miễn là mọi thiết bị đều thuộc cùng một chức năng.",
        "Mỗi đầu vào và đầu ra trường phải được đặt cầu chì hoặc giới hạn dòng. Có thể làm ngay trong "
        "mô-đun vào/ra của hệ logic, hoặc dùng cầu chì ngoài.",
        "Một khuyến nghị chung là tách cáp, dây dẫn và hộp nối của SIS khỏi mọi dây điều khiển và/hoặc "
        "dây thiết bị đo khác, và dán nhãn rõ chúng là phần của SIS.",
        "Chú ý đến độ tự cảm, điện dung và chiều dài tuyến cáp. Tuỳ cỡ dây và khoảng cách, có thể xuất "
        "hiện điện áp cảm ứng khiến mạch vào/ra không nhả được.",
    ]))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Thiết bị trường gồm cảm biến, phần tử cuối, dây dẫn trường và những thiết bị khác nối vào "
               "đầu cực vào/ra của hệ logic. Những thiết bị này có thể chiếm khoảng 90 % các vấn đề tiềm "
               "ẩn gắn với hệ thống đo lường an toàn. Có thể dùng dự phòng và/hoặc chẩn đoán để cải thiện "
               "hiệu năng của thiết bị trường."))

    b.append(note(
        "<b>Ba điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Mục lục của bản gốc đánh số sai.</b> Trang mục lục liệt kê “9.3.2 Công tắc”, rồi “9.5.2 Bộ "
        "chuyển đổi” và “9.5.3 Chẩn đoán cảm biến”, rồi “9.3.3 Bộ chuyển đổi thông minh”. Thân chương lại "
        "đánh số đúng theo trình tự 9.3.3 Bộ chuyển đổi, 9.3.4 Chẩn đoán cảm biến, 9.3.5 Bộ chuyển đổi "
        "thông minh. Bản dịch theo thân chương, vì đó là trình tự đọc thật.<br>"
        "<b>(2) Bảng cấu hình dự phòng không có số.</b> Bản gốc chèn bảng cấu hình 1oo1…2oo3 ngay trong "
        "mục 9.5.1 mà không đánh số, rồi mới đến Bảng 9-2 ở trang sau. Bản dịch giữ nguyên: bảng ấy không "
        "mang số, để Bảng 9-2 vẫn là Bảng 9-2.<br>"
        "<b>(3) Hình 9-3 là hình bổ sung.</b> Mạch có giám sát chỉ được mô tả bằng lời ở mục 9.6; bản dịch "
        "vẽ thêm để thấy rõ vì sao bốn trạng thái phân biệt được. Ngoài ra, hàng “Tổng” của Bảng 9-1 được "
        "ghi chú: con số 8,3 năm là nghịch đảo của tổng suất hỏng, không phải tổng của bốn MTTF — một chỗ "
        "dễ đọc nhầm thành “trung bình cộng”."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3 Mod). <em>Functional Safety: Safety "
        "Instrumented Systems for the Process Industry Sector</em>.",
        "<em>Guidelines for Safe Automation of Chemical Processes</em>. American Institute of Chemical "
        "Engineers – Center for Chemical Process Safety, 1993.",
        "Cusimano, J. A. “Applying Sensors in Safety Instrumented Systems.” <em>ISA TECH/EXPO Technology "
        "Update</em>. Vol. 1, Phần 4 (1997). tr. 131–137. Có tại www.isa.org (truy cập 28/6/2005).",
        "Faller, R. <em>Safety-Related Field Instruments for the Process Industry</em>. TÜV Product "
        "Service GmbH, 1996.",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "Ninety percent of the problems in a safety instrumented system are in the ten percent of the "
        "budget that nobody argues about. The logic solver gets the meetings, the certification and the "
        "architecture diagrams; the solenoid gets whatever is left in the procurement budget. This chapter "
        "is the correction."))

    b.append(h2("One table, and the argument is over"))
    b.append(p("Table 9-1 is four rows long and settles most of the debate in this book. A pressure sensor, "
               "four relays, a solenoid and a shutdown valve, tested once a year, come to a total PFD of "
               "0.06 — RRF 16, barely SIL 1. The logic is 8 % of that. The two valves are 50 %. No choice "
               "of PLC, no TMR architecture and no certification will move a number whose eighth part is "
               "the only part you were negotiating about."))
    b.append(p("The solenoid deserves particular attention because it is the cheapest item on the list and "
               "the second largest contributor. It is a coil of wire in a weatherproof box, asked to sit "
               "energised for years in a plant where the ambient temperature swings forty degrees, and it "
               "fails by burning out — which is a nuisance trip, not a dangerous failure, which is why "
               "nobody counts it as a safety problem until the trips become frequent enough that somebody "
               "bypasses it."))

    b.append(h2("Diagnostics are worth more than redundancy"))
    b.append(p("The 1oo1D example in section 9.5.1.1 makes the arithmetic plain. Adding 60 % diagnostic "
               "coverage to a single transmitter takes PFD from 0.01 to 0.004 — a factor of 2.5 — for the "
               "price of a HART monitor and no additional process connection. A second transmitter in a "
               "1oo2 arrangement buys a much larger factor and costs a tap, a root valve, an impulse line, "
               "a cable, an input card and a maintenance procedure. Neither is wrong; the point is that "
               "the cheap option is usually tried last."))
    b.append(p("There is a second, quieter benefit. A transmitter that can tell you it has failed lets you "
               "bypass the failed signal and keep producing, instead of tripping the plant on a sensor that "
               "is merely broken. That decision — alarm versus trip on a detected fault — is the whole of "
               "Table 9-2, and it is a process decision, not an instrument one."))

    b.append(h2("Why the field device is hard to fix"))
    b.append(p("A logic solver is one box from one vendor with one failure rate. A loop is a tap, a root "
               "valve, an impulse line, a transmitter, a cable, a junction box, an input card, a solenoid, "
               "an air line, an actuator, a stem, a seat and a spring. Nine of those thirteen items are "
               "mechanical, most are outdoors, and several are maintained by people who never see the "
               "safety requirement specification. This is why the 90 % figure is stable across industries "
               "and decades: it is a property of the topology, not of any particular product."))
    b.append(p("It is also why partial stroke testing spread so quickly. It is the only technique in this "
               "book that improves the largest contributor without stopping the process, and section 8.13.1 "
               "shows the arithmetic: RRF 80 to RRF 300 for a monthly test at 80 % coverage."))

    b.append(h2("The shared-sensor argument, and when to break it"))
    b.append(p("Section 9.3 gives three reasons not to share a sensor with the BPCS, and the first is the "
               "strongest: the SIS exists partly because BPCS components fail, so building it on a BPCS "
               "sensor means building it on the thing it is supposed to protect you from. The other two — "
               "stricter maintenance procedures and the impossibility of online testing — are practical "
               "rather than fundamental."))
    b.append(p("The exception in section 9.4.1 is worth reading carefully, because it is how most real "
               "plants actually operate. Where a separate shutdown valve is impractical, a control valve "
               "can carry the function provided the solenoid is tubed directly to the actuator, bypassing "
               "the positioner, and provided somebody writes a safety case. The safety case is the price "
               "of the exception, and it should be a real document, not a paragraph in a design file."))

    b.append(h2("Two sentences that repay rereading"))
    b.append(p("“Diagnostics do not change the overall failure rate, just the percentage of failures that "
               "are detected.” This is the most misunderstood sentence in functional safety. Diagnostics "
               "move failures from the undetected column to the detected column; they do not remove them. "
               "A device with 99 % diagnostic coverage still fails exactly as often as the same device "
               "with none — it just tells you sooner, and telling you sooner is what converts a dangerous "
               "undetected failure into a nuisance trip you can fix."))
    b.append(p("The second is the note under Table 9-2: an alarm should always be generated if a "
               "transmitter fault occurs. The logic may be configured to trip or to alarm, and both are "
               "defensible, but silence is not. A fault that is detected and not annunciated is worse than "
               "a fault that was never detected, because it consumes the diagnostic coverage you paid for "
               "and returns nothing."))
    return "".join(b)
