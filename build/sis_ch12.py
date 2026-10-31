# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 12, Functional Testing
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis12fig as F

PAGES_SRC = 14
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Thử chức năng (functional test)</em> — phép thử định kỳ để phát hiện hỏng hóc nguy hiểm "
            "mà hệ không tự bộc lộ. · "
            "<em>Chu kỳ thử (TI, proof test interval)</em> — khoảng thời gian giữa hai lần thử. · "
            "<em>Hiệu quả thử (ET)</em> — tỉ lệ hỏng hóc mà phép thử phát hiện được, từ 0 đến 1. · "
            "<em>Thời gian sống của hệ (SL)</em> — khoảng thời gian hệ tồn tại giữa hai lần thay thế hoàn "
            "toàn; hỏng hóc không phát hiện được sẽ nằm im suốt khoảng đó. · "
            "<em>PFD<sub>avg</sub></em> — xác suất trung bình hệ không đáp ứng được yêu cầu. · "
            "<em>RRF</em> — hệ số giảm rủi ro, bằng 1/PFD. · "
            "<em>Force</em> — gán cưỡng bức giá trị vào/ra; <em>không</em> phải là thử nghiệm. · "
            "<em>As-found / as-left</em> — trạng thái ghi nhận trước khi sửa và sau khi sửa.")
    return note(
        "<b>Key terms.</b> <em>Functional test</em> — the periodic test that finds dangerous failures the "
        "system does not reveal by itself. · <em>Proof test interval (TI)</em> — the time between two "
        "tests. · <em>Test effectiveness (ET)</em> — the fraction of failures the test actually finds, 0 "
        "to 1. · <em>System lifetime (SL)</em> — how long the system exists between complete replacements; "
        "a failure the test missed stays latent for all of it. · <em>PFD<sub>avg</sub></em> — the average "
        "probability that the system fails to respond to a demand. · <em>RRF</em> — risk reduction factor, "
        "1/PFD. · <em>Force</em> — overwriting an I/O value; not a test. · <em>As-found / as-left</em> — "
        "the condition recorded before and after repair.")


def body_vi():
    b = []
    b.append(lead(
        "Một mức SIL chỉ là con số trên giấy cho tới khi có người thật sự đi thử hệ thống. Chương này nói "
        "về việc đó: thử cái gì, bao lâu một lần, ai làm, và tại sao “thử nhiều hơn” không đồng nghĩa với "
        "“an toàn hơn”."))

    # ------------------------------------------------------------------ 12.1
    b.append(h2("12.1 Giới thiệu", "Introduction"))
    b.append(p("Thử chức năng phải được thực hiện định kỳ để kiểm chứng hoạt động của hệ thống an toàn "
               "(SIS) và để bảo đảm rằng mức toàn vẹn an toàn (SIL) mục tiêu đang đạt được. Việc thử phải "
               "bao trùm toàn hệ (tức cảm biến, bộ giải logic, cơ cấu chấp hành cuối và các báo động liên "
               "quan) và phải dựa trên những mục tiêu rõ ràng, được định nghĩa tốt. Phải phân công trách "
               "nhiệm và phải tuân thủ quy trình bằng văn bản."))
    b.append(p("Nên coi việc thử là một hoạt động bảo trì phòng ngừa bình thường. Không thể mong một SIS "
               "hoạt động thoả đáng mà không có thử chức năng định kỳ. Mọi thứ đều hỏng, vấn đề chỉ là "
               "khi nào. Vì hệ an toàn là thụ động, không phải mọi hỏng hóc đều tự bộc lộ. Cảm biến và van "
               "có thể kẹt, và linh kiện điện tử có thể hỏng trong trạng thái đang được cấp điện. Vì thế "
               "hệ an toàn phải được thử để tìm ra những hỏng hóc nguy hiểm có thể khiến hệ không đáp ứng "
               "được một yêu cầu thật."))
    b.append(p("Việc thử có thể tự động hoặc thủ công, và có thể gồm phần cứng và/hoặc phần mềm. Thử phần "
               "mềm là một vấn đề gây tranh cãi. Cần nhận ra rằng chỉ thử thôi thì không thể phát hiện mọi "
               "lỗi phần mềm (ví dụ lỗi thiết kế). Như đã nói ở các chương trước, phần lớn lỗi phần mềm "
               "đều bắt nguồn từ đặc tả yêu cầu. Vì thế thử phần mềm dựa trên đặc tả yêu cầu có thể sẽ "
               "không bộc lộ hết lỗi. Chương này tập trung vào việc thử thủ công định kỳ đối với phần cứng."))

    # ------------------------------------------------------------------ 12.2
    b.append(h2("12.2 Vì sao phải thử", "The Need for Testing"))
    b.append(p("Không phải là chuyện hiếm gặp khi bắt gặp những hệ an toàn chưa từng được thử kể từ lần "
               "lắp đặt ban đầu. Khi cuối cùng những hệ ấy được thử, người ta tìm thấy hỏng hóc nguy hiểm, "
               "phần lớn gắn với thiết bị trường. Mỗi hỏng hóc trong số đó đều có khả năng góp phần vào "
               "một vụ tai nạn tiềm tàng. Những lý do chính khiến cách làm này vẫn tồn tại là:"))
    b.append(ol([
        "Hệ thống an toàn thường bị nhìn nhận giống như hệ điều khiển quá trình cơ bản (BPCS), kéo theo "
        "giả định rằng mọi hỏng hóc của hệ an toàn đều sẽ bộc lộ. Chương 3, “Điều khiển quá trình và "
        "điều khiển an toàn”, đã nhấn mạnh những khác biệt giữa điều khiển và an toàn. Một khác biệt then "
        "chốt là cách hệ an toàn hỏng. Không như hệ điều khiển, hệ an toàn có thể hỏng theo hai chế độ "
        "riêng biệt. Chúng có thể hỏng an toàn và gây cắt nhầm, hoặc hỏng nguy hiểm và không đáp ứng một "
        "yêu cầu thật (xin xem thêm mục 8.4). Hệ điều khiển là chủ động và động, nên phần lớn hỏng hóc "
        "vốn dĩ tự bộc lộ. Hệ điều khiển thông thường không gặp hỏng hóc nguy hiểm. Hệ an toàn thì thụ "
        "động hay nằm im, và không phải mọi hỏng hóc đều tự bộc lộ. Mục tiêu chính của thử chức năng là "
        "nhận diện những hỏng hóc nguy hiểm của hệ.",
        "Tiêu chí thử được định nghĩa tốt có thể đã không được thiết lập trong giai đoạn thiết kế. Kể cả "
        "khi đã thiết lập, việc thử dự kiến và chu kỳ thử có thể đã không được truyền đạt tới bộ phận bảo "
        "trì hay vận hành — những người chịu trách nhiệm thực hiện.",
        "Có thể đã nhận ra rằng cần phải thử, nhưng quy trình và phương tiện thích hợp không được cung "
        "cấp, nên việc thử không được làm. Trong trường hợp đó, việc thử có thể bị hoãn tới lần đại tu "
        "lớn tiếp theo. Chu kỳ thử thu được khi ấy có thể không thoả đáng.",
    ]))
    b.append(p("Những điểm trên sẽ được giải quyết nếu tuân theo vòng đời đã phác ra ở Chương 2. Vòng đời "
               "đề cập tới quy trình và nhu cầu thử chức năng trong các pha đặc tả, thiết kế, vận hành và "
               "bảo trì."))
    b.append(p("Thử chức năng các hệ an toàn không phải là việc đơn giản (nhất là khi phải thử trực tuyến "
               "trong lúc phân xưởng vẫn đang chạy). Cần một khối lượng đáng kể công tác đào tạo, phối "
               "hợp và hoạch định để thực hiện được những phép thử như vậy mà không dừng phân xưởng một "
               "cách không cần thiết. Những lần dừng ngoài kế hoạch có thể xảy ra, và chúng có thể tạo ra "
               "thêm tình huống nguy hiểm cùng tổn thất sản xuất. Vì thế có thể gặp sự phản đối việc thử "
               "từ nhiều bộ phận khác nhau. Những câu như “Đừng có mà làm lúc tôi đang trực” hay “Nó chưa "
               "hỏng thì đừng có sửa” có thể sẽ được nghe thấy."))
    b.append(p("Một lợi ích thứ cấp của việc thử là nó làm tăng hiểu biết và sự tự tin của nhân sự liên "
               "quan đến hệ thống."))
    b.append(p("Quy định về quản lý an toàn quá trình của OSHA (29 CFR 1910.119) yêu cầu người sử dụng "
               "lao động phải “thiết lập các hệ bảo trì cho thiết bị quan trọng liên quan đến quá trình, "
               "bao gồm quy trình bằng văn bản, đào tạo nhân viên, kiểm tra phù hợp và thử nghiệm thiết bị "
               "đó để bảo đảm toàn vẹn cơ học lâu dài”. Quy định của OSHA còn quy định thêm rằng “quy "
               "trình kiểm tra và thử nghiệm phải theo những thực hành kỹ thuật tốt đã được công nhận và "
               "thường được chấp nhận”."))
    b.append(p("Để hiểu rõ hơn nhu cầu và lý lẽ của thử chức năng, hãy xét một chức năng an toàn áp suất "
               "cao (SIF) rất đơn giản gồm một bộ biến đổi áp suất, logic rơ-le và một van cắt duy nhất, "
               "như trên Hình 12-1."))
    b.append(fig(1, F.fig_12_1(), "vi"))
    b.append(p("Giả sử không có dự phòng và không có tự chẩn đoán, xác suất hỏng trung bình khi có yêu cầu "
               "(PFD<sub>avg</sub>) có thể biểu diễn như sau:"))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>d</sub> · TI / 2", "12.1"))
    b.append(p("trong đó:"))
    b.append(ul([
        "λ<sub>d</sub> = suất hỏng nguy hiểm của toàn hệ (tức cảm biến, bộ giải logic, cơ cấu chấp hành "
        "cuối);",
        "TI = chu kỳ thử nghiệm chứng minh.",
    ]))
    b.append(p("Từ phương trình trên có thể thấy chu kỳ thử nghiệm chứng minh (TI) là một nhân tố quan "
               "trọng đối với hiệu năng của hệ ngang với suất hỏng nguy hiểm của các thành phần phần cứng. "
               "Về lý thuyết, nếu một hệ không bao giờ được thử thì xác suất hệ không đáp ứng được một yêu "
               "cầu tiến tới 1, tức 100 %. Nói cách khác, nếu hệ không bao giờ được thử thì khó có khả "
               "năng nó sẽ làm việc đúng khi cần."))
    b.append(p("Phương trình trên không tính đến tự chẩn đoán, và cũng giả định rằng việc thử thủ công đạt "
               "hiệu quả 100 %. Nếu việc thử không triệt để 100 %, một số hỏng hóc nguy hiểm có thể không "
               "được nhận ra và có thể nằm im suốt đời sống của hệ. Kết quả là PFD<sub>avg</sub> sẽ còn "
               "cao hơn nữa. Có thể tính PFD<sub>avg</sub> cho trường hợp hiệu quả thử dưới 100 % bằng "
               "công thức sau:"))
    b.append(eq("PFD<sub>avg</sub> = ET · λ<sub>d</sub> · TI / 2 + (1 − ET) · λ<sub>d</sub> · SL / 2",
                "12.2"))
    b.append(p("trong đó:"))
    b.append(ul([
        "ET = hiệu quả của phép thử nghiệm chứng minh (từ 0 đến 1);",
        "SL = thời gian sống của hệ. Thời gian sống của hệ có thể là khoảng thời gian cho tới khi hệ được "
        "thử hoàn toàn, được thay thế, hoặc là thời gian sống của nhà máy nếu hệ không bao giờ được thử "
        "hoàn toàn hay thay thế.",
    ]))
    b.append(h3("Ví dụ", "Example"))
    b.append(p("Một van cắt có suất hỏng nguy hiểm là 0,025 lần hỏng mỗi năm (tức thời gian hỏng trung "
               "bình [MTTF] là 40 năm). Giả sử một lần kiểm tra định kỳ hằng năm phát hiện được 95 % số "
               "hỏng hóc. Van được vận hành mười năm trước khi được đưa ra khỏi vận hành và thay thế. "
               "PFD<sub>avg</sub> trong khoảng vận hành mười năm là bao nhiêu, với hai kịch bản sau?"))
    b.append(ul([
        "(a) Van được thử mỗi năm một lần và được thay mỗi 10 năm.",
        "(b) Van không bao giờ được thử, chỉ được thay mỗi 10 năm.",
    ]))
    b.append(table(
        ["Kịch bản", "PFD<sub>avg</sub>", "RRF", "Mức"],
        [["(a) thử hằng năm, thay mỗi 10 năm",
          "(0,95 · 0,025/năm · 1 năm / 2)<br>+ (0,05 · 0,025/năm · 10 năm / 2)<br>= <b>0,018</b>",
          "55", "SIL 1"],
         ["(b) không thử, chỉ thay mỗi 10 năm",
          "0,025/năm · 10 năm / 2<br>= <b>0,125</b>",
          "8", "SIL 0"]],
        caption="Bảng 12-1. Hai kịch bản của cùng một van. RRF = 1/PFD<sub>avg</sub>. Chênh lệch giữa hai "
                "dòng — hệ số 7 về PFD và một bậc SIL — hoàn toàn đến từ việc có thử hay không, chứ không "
                "phải từ phần cứng."))
    b.append(p("Công thức trên chỉ có sai số nhỏ chừng nào thời gian hỏng trung bình còn lớn hơn đáng kể "
               "so với khoảng thời gian thử hoặc thời gian sống. Khi giả định ấy không còn đúng thì phải "
               "làm những phép tính chi tiết hơn."))

    b.append(h3("12.2.1 Yêu cầu của ANSI/ISA-84.00.01-2004 về thử chức năng",
                "ANSI/ISA-84.00.01-2004 Requirements for Functional Testing"))
    b.append(p("Tiểu mục 11.8 của tiêu chuẩn quy định:"))
    b.append(quote("Thiết kế phải cho phép thử SIS hoặc theo kiểu đầu-cuối, hoặc theo từng phần. Khi "
                   "khoảng thời gian giữa các lần dừng quá trình theo kế hoạch lớn hơn chu kỳ thử nghiệm "
                   "chứng minh, thì bắt buộc phải có phương tiện thử trực tuyến.",
                   "ANSI/ISA-84.00.01-2004, tiểu mục 11.8"))
    b.append(p("Tiểu mục 16.2.8 quy định:"))
    b.append(quote("Phải xây dựng quy trình thử nghiệm chứng minh bằng văn bản cho từng SIF để bộc lộ những "
                   "hỏng hóc nguy hiểm mà chẩn đoán không phát hiện được. Những quy trình thử bằng văn bản "
                   "này phải mô tả từng bước cần thực hiện và phải bao gồm: hoạt động đúng của từng cảm "
                   "biến và từng cơ cấu chấp hành cuối; tác động logic đúng; báo động và chỉ thị đúng.",
                   "ANSI/ISA-84.00.01-2004, tiểu mục 16.2.8"))
    b.append(p("Tiểu mục 16.3.1.5 quy định rằng “tại một chu kỳ nào đó (do người sử dụng xác định), tần "
               "suất thử phải được đánh giá lại dựa trên nhiều nhân tố, bao gồm dữ liệu thử trong quá "
               "khứ, kinh nghiệm nhà máy, sự xuống cấp của phần cứng và độ tin cậy của phần mềm”. Kinh "
               "nghiệm có thể cho thấy những suất hỏng giả định trong các phép tính ban đầu là sai, và "
               "chu kỳ thử có thể cần được xem lại."))
    b.append(p("Ngoài việc thử thật, từng chức năng an toàn nên được kiểm tra bằng mắt định kỳ để bảo đảm "
               "không có thay đổi trái phép và/hoặc không có hư hại nhìn thấy được (ví dụ thiếu bu-lông "
               "hay nắp thiết bị, giá đỡ gỉ, dây hở, ống luồn dây đứt, hệ gia nhiệt bằng điện trở đứt, và "
               "thiếu cách nhiệt). Một trong các tác giả đã từng thấy một trường hợp: một tủ NEMA 7 (chống "
               "nổ) rất lớn chỉ còn hai bu-lông giữ nắp. Viết trên mặt trước tủ bằng bút lông đen là dòng "
               "chữ: “Cái anh kỹ sư thiết kế ra cái này đáng bị bắn!”. Có lẽ người kỹ thuật viên không "
               "hiểu rằng cần phải có đủ mọi bu-lông. Một lần kiểm tra bằng mắt đơn giản của người có "
               "chuyên môn sẽ phát hiện ra vấn đề. (Tác giả đã báo cho chủ nhà.)"))
    b.append(p("Người sử dụng cần duy trì hồ sơ chứng minh rằng các phép thử nghiệm chứng minh và các lần "
               "kiểm tra đã được hoàn thành đúng như yêu cầu. Những hồ sơ này tối thiểu phải gồm:"))
    b.append(ul([
        "(a) mô tả các phép thử và các lần kiểm tra đã thực hiện;",
        "(b) ngày thực hiện các phép thử và các lần kiểm tra;",
        "(c) tên người thực hiện các phép thử và các lần kiểm tra;",
        "(d) số sê-ri hoặc định danh duy nhất khác của hệ được thử (ví dụ số vòng đo, số tag, số thiết bị "
        "và số SIF);",
        "(e) kết quả của các phép thử và các lần kiểm tra (ví dụ trạng thái “như khi phát hiện” và “như "
        "khi để lại”).",
    ]))
    b.append(p("Ngoài tiêu chuẩn, Uỷ ban ISA SP84 đã viết thêm một báo cáo kỹ thuật về thử nghiệm hệ "
               "thống. ISA-TR84.00.03-2002 (“Hướng dẫn thử nghiệm các chức năng an toàn quá trình (SIF) "
               "được thực hiện như hoặc trong các hệ thống an toàn (SIS)”) dày hơn 220 trang về việc thử "
               "nhiều loại cảm biến, hệ logic và cơ cấu chấp hành cuối khác nhau."))

    b.append(h3("12.2.2 Hướng dẫn chung", "General Guidelines"))
    b.append(p("Khi không thể thử trực tuyến mọi thành phần (ví dụ một số van hoặc bộ khởi động động cơ), "
               "những thiết bị ấy nên được thiết kế với đặc tính an toàn khi hỏng, chẩn đoán và/hoặc dự "
               "phòng thoả đáng để có thể thử trong kỳ đại tu nhà máy mà vẫn duy trì được hiệu năng yêu "
               "cầu. Phương tiện thử phải cho phép thực hiện việc thử một cách dễ dàng mà không làm gián "
               "đoạn vận hành bình thường của quá trình. Chu kỳ thử thiết kế cho các thiết bị nên ít nhất "
               "bằng khoảng thời gian đại tu dự kiến của nhà máy."))
    b.append(p("Cần thận trọng khi dùng công tắc bypass để thử chức năng. Mỗi khi có những công tắc như "
               "vậy, tín hiệu đầu vào phục vụ ghi dữ liệu và báo động <em>không</em> được bypass. Nên xem "
               "xét dùng một báo động để chỉ ra rằng đang có bypass. An toàn phải được duy trì kể cả khi "
               "một thiết bị đang bị đặt vào bypass. Phải ban hành và tuân thủ quy trình về việc dùng "
               "bypass."))
    b.append(p("Việc force đầu vào hay đầu ra trong hệ logic để mô phỏng tín hiệu vào hoặc kích hoạt đầu "
               "ra <em>không</em> được coi là tương đương với thử nghiệm. Việc force phải được giới hạn "
               "trong các hoạt động bảo trì, khi cần đưa một phần của hệ ra khỏi vận hành. Phải ban hành "
               "và thực thi quy trình để bảo đảm bypass không bị lạm dụng."))
    b.append(p("Trong lúc thử, một phần của hệ an toàn có thể nằm ngoài vận hành, hoặc khả năng cắt của hệ "
               "có thể bị giảm. Điều này ảnh hưởng tới hiệu năng tổng thể của hệ, như đã trình bày ở mục "
               "8.9.1. Không bao giờ thử có tác động tiêu cực; thử quá thường xuyên và cố ý đưa hệ ra khỏi "
               "vận hành cũng có tác động tiêu cực. Vì thế nên cố gắng tối ưu hoá tần suất thử. Trong một "
               "nghiên cứu năm 1985, Lihou và Kabir bàn về một kỹ thuật thống kê để tối ưu hoá tần suất "
               "thử các thiết bị trường dựa trên hiệu năng trong quá khứ [Tài liệu 2]."))
    b.append(p("Trong giai đoạn thử nghiệm và trước khởi động của bất kỳ dự án nào, người ta có thể thực "
               "hiện các sửa đổi trên hệ để làm cho nó “chạy được”. Những sửa đổi ấy có thể là thay giá "
               "trị đặt, thay cài đặt bộ định thời, lắp cầu nối hoặc bypass, hay vô hiệu hoá các chức năng "
               "cắt. Những “sửa đổi” này cần được kiểm soát. Hệ phải được thử lại để kiểm chứng rằng nó "
               "nhất quán với đặc tả yêu cầu an toàn."))
    b.append(p("Việc thử các van cắt thường chỉ kiểm chứng xem van có mở hoặc đóng trong khoảng thời gian "
               "quy định hay không. Có thể khó kiểm tra được những vấn đề cơ khí bên trong. Nếu điều đó là "
               "then chốt thì có thể cần thêm phương tiện (ví dụ van dự phòng)."))

    # ------------------------------------------------------------------ 12.3
    b.append(h2("12.3 Xác lập chu kỳ thử", "Establishing Test Frequencies"))
    b.append(p("Không có quy tắc cứng nhắc nào để xác định chu kỳ thử thủ công. Không thể chỉ nói đơn giản "
               "rằng, ví dụ, hệ SIL 3 phải được thử hằng tháng, hệ SIL 2 hằng quý và hệ SIL 1 hằng năm. "
               "Một số công ty đã đặt ra tiêu chuẩn quy định rằng hệ an toàn phải được nhân sự được đào "
               "tạo thử ít nhất mỗi năm một lần. Những tiêu chí như vậy có thể dùng để xác lập một số yêu "
               "cầu tối thiểu, nhưng có thể dẫn tới đơn giản hoá quá mức. Có hệ cần thử thường xuyên hơn, "
               "có hệ cần thử ít hơn. Tần suất thử yêu cầu là một biến số của từng hệ, phụ thuộc vào công "
               "nghệ, cấu hình và mức rủi ro mục tiêu."))
    b.append(p("Như đã trình bày ở Chương 8, chu kỳ thử thủ công ảnh hưởng đáng kể tới hiệu năng tổng thể "
               "của hệ. Có thể giải các công thức để xác định chu kỳ thử tối ưu theo cách định lượng. Bảng "
               "tính và/hoặc các chương trình khác có thể vẽ đồ thị hiệu năng của hệ theo những chu kỳ thử "
               "thủ công khác nhau. Những đồ thị thu được sẽ chỉ ra chu kỳ thử thủ công cần thiết dựa trên "
               "mức hiệu năng mong muốn của hệ. Nhiều người lắp hệ dự phòng chính là để không phải thử "
               "chúng thường xuyên như vậy."))
    b.append(p("Tần suất của các phép thử nghiệm chứng minh có thể được xác định bằng các phép tính "
               "PFD<sub>avg</sub> như trong ví dụ trên và trong Chương 8. Những phần khác nhau của hệ có "
               "thể cần chu kỳ thử khác nhau. Ví dụ thiết bị trường, đặc biệt là van, có thể cần thử thường "
               "xuyên hơn bộ giải logic. Mọi khiếm khuyết phát hiện trong lúc thử phải được sửa chữa một "
               "cách an toàn và kịp thời."))
    b.append(p("Khi xác định chu kỳ thử thủ công theo cách định lượng, cần nhận ra tác động của thời lượng "
               "một lần thử (như đã trình bày ở mục 8.9.1). Ví dụ khi thử một hệ đơn tuyến, thường phải "
               "đặt hệ vào bypass (để không dừng quá trình trong lúc thử). Độ sẵn sàng của hệ khi đang "
               "bypass là bao nhiêu? Bằng không. Điều này phải được tính vào phép tính. Trong lúc thử, một "
               "hệ đơn tuyến bị giảm về không, một hệ kép bị giảm về đơn tuyến, và một hệ ba kênh bị giảm "
               "về kép. Các công thức để tính đến điều này đã được nêu ở mục 8.9.1. Điều đó có nghĩa là "
               "tồn tại một chu kỳ thử thủ công tối ưu cho bất kỳ hệ nào. Một ví dụ đồ thị được trình bày "
               "trên Hình 12-2."))
    b.append(fig(2, F.fig_12_2(), "vi"))

    # ------------------------------------------------------------------ 12.4
    b.append(h2("12.4 Trách nhiệm thử nghiệm", "Responsibilities for Testing"))
    b.append(p("Điều thiết yếu là những người tham gia thử chức năng hệ an toàn phải hiểu biết cả về quá "
               "trình lẫn về thiết kế hệ an toàn. Quy trình nên được viết với sự đóng góp của kỹ thuật, "
               "vận hành và bảo trì. Việc thử có thể do nhân sự thuộc bộ phận quá trình, thiết bị đo, bảo "
               "trì hoặc vận hành thực hiện. Trách nhiệm thử phải thuộc về những người chịu trách nhiệm "
               "cuối cùng về việc vận hành an toàn của nhà máy. Phải thiết lập phương tiện và quy trình "
               "thử mà những người trực tiếp thử có thể hiểu và tuân theo. Ngoài việc kiểm chứng tính toàn "
               "vẹn của hệ an toàn, việc thử còn là một khoá đào tạo có giá trị cho chính những người thực "
               "hiện, cũng như đào tạo định hướng cho nhân viên mới khi chứng kiến các phép thử."))

    # ------------------------------------------------------------------ 12.5
    b.append(h2("12.5 Phương tiện và quy trình thử", "Test Facilities and Procedures"))
    b.append(p("Quy trình thử sẽ rất khác nhau tuỳ theo loại thiết bị, các yêu cầu thử và phương tiện được "
               "cung cấp cho việc thử. Việc thử hệ thống trên Hình 12-1 có thể đòi hỏi phải dừng phân "
               "xưởng. Đó sẽ được coi là thử ngoại tuyến. Để thử hệ trong khi vẫn duy trì sản xuất, cần bổ "
               "sung các khả năng thử trực tuyến. Ví dụ, để có thể thử trực tuyến hệ thống trên Hình 12-1:"))
    b.append(ol([
        "Cần có các van để cách ly đầu nối quá trình và tăng áp cho bộ biến đổi PT-100.",
        "Cần lắp các van chặn và van bypass để thử van PV-100.",
        "Hình 12-3 là một ví dụ về một công trình lắp đặt tương tự cho phép thử trực tuyến. Để thử hệ, "
        "người ta mở van bypass HV-100 và thay đổi tín hiệu tới bộ biến đổi PT-100 để giả một tín hiệu "
        "cắt. Van cắt chính PV-100 phải đóng tại đúng giá trị đặt quy định của PT-100. Có thể dùng một "
        "dạng hồi tiếp nào đó (ví dụ công tắc hành trình) để kiểm chứng rằng van PV-100 thật sự đã đóng "
        "hết.",
    ]))
    b.append(fig(3, F.fig_12_3(), "vi"))
    b.append(p("Một cách để thử một thiết bị cảm biến áp suất thấp là đóng van cách ly quá trình và xả "
               "tín hiệu khỏi thiết bị (nếu khả thi về môi trường) cho tới khi nó tác động. Tương tự, một "
               "cách để thử thiết bị cảm biến áp suất cao là đóng van cách ly quá trình và bơm một tín "
               "hiệu quá trình vào thiết bị cho tới khi nó tác động. Phải có phương tiện để phát hiện rằng "
               "hệ tác động đúng tại giá trị đã ghi trong đặc tả yêu cầu."))
    b.append(p("Với hệ khí nén, có thể xem xét dùng các bộ điều khiển bật/tắt khí nén có chỉ thị tại chỗ "
               "làm thiết bị đầu vào. Tín hiệu ra từ các bộ điều khiển bật/tắt ấy là 3 hoặc 15 psi. Một "
               "công tắc áp suất đặt ở 9 psi có thể đóng vai trò đầu vào của hệ logic. Bằng việc thay đổi "
               "giá trị đặt của bộ điều khiển bật/tắt, có thể thử các thiết bị đầu vào một cách dễ dàng."))
    b.append(p("Nếu một van mở ra khi có lệnh cắt, có thể lắp một van chặn thường đóng nối tiếp ở phía "
               "thượng lưu của van được truyền động. Khi ấy có thể đóng van chặn này và mở van cắt ra để "
               "thử. Sau khi thử, mọi thứ phải được đưa trở về vị trí ban đầu."))
    b.append(p("Nên hạn chế việc dùng công tắc bypass thủ công để vô hiệu hoá việc đóng của van cắt (vì "
               "chúng có thể bị lạm dụng), nhưng vẫn dùng khi không thực tế để lắp một đường bypass quanh "
               "van."))
    b.append(p("Trong một số trường hợp, có thể không thể thử hoặc dừng một cơ cấu chấp hành cuối (ví dụ "
               "máy nén, bơm hoặc van lớn). Khi ấy có thể cần lắp một dạng bypass nào đó để bảo đảm cơ cấu "
               "chấp hành cuối không tác động trong lúc thử phần tử cảm biến và phần logic. Ví dụ với máy "
               "nén, có thể cấp điện cho rơ-le cắt cuối và bypass tín hiệu từ rơ-le cắt tới bộ khởi động "
               "máy nén."))
    b.append(p("Nếu phải lắp các công tắc bypass vận hành bằng tay, mỗi lần chỉ được thao tác một công "
               "tắc. Các bypass đang hoạt động phải được báo động theo một cách nào đó. Một số bypass có "
               "thể là cần thiết để cho phép khởi động nhà máy (ví dụ mức thấp hoặc lưu lượng thấp). Những "
               "bypass ấy có thể cần được điều khiển bằng bộ định thời, cho phép lập lại các chức năng cắt "
               "sau một khoảng thời gian cố định. Phải xây dựng và tuân thủ quy trình về việc dùng bypass."))
    b.append(p("Mọi khiếm khuyết phát hiện trong lúc thử phải được báo cáo và việc sửa chữa phải được lên "
               "lịch dựa trên mức trọng yếu của hệ. Hệ dự phòng cũng phải được thử để bảo đảm mọi thành "
               "phần đều hoạt động đầy đủ."))

    # ------------------------------------------------------------------ 12.6
    b.append(h2("12.6 Tài liệu", "Documentation"))
    b.append(p("Mọi quy trình vận hành, thử và bảo trì phải được ghi chép đầy đủ và phải sẵn có cho nhân "
               "sự. (Tuy vậy, chỉ có quy trình thôi thì không bảo đảm là chúng sẽ được đọc.) Nên không chỉ "
               "lôi kéo bộ phận kỹ thuật mà cả nhân sự vận hành và bảo trì cùng tham gia xây dựng quy trình "
               "thử. Không ai hiểu rõ hơn họ về việc mọi thứ thật sự có thể và cần được làm như thế nào. "
               "Ngôn ngữ và thuật ngữ dùng trong quy trình phải được mọi bên hiểu. Mỗi chức năng cắt phải "
               "có một quy trình thử riêng. Mọi việc thử đều phải để lại một dấu vết giấy tờ, sao cho một "
               "người hay một nhóm độc lập có thể kiểm toán lại về sau."))

    b.append(h3("12.6.1 Mẫu tài liệu quy trình thử", "Sample Test Procedure Documentation"))
    b.append(p("Quy trình thử phải chứa và liệt kê những thông tin mà người thực hiện cần. Danh sách các "
               "hành động cần làm để thực hiện phép thử phải được ghi chép rõ ràng theo từng bước."))
    b.append(p("Một ví dụ về những mục chính cần có trong một quy trình thử như sau:"))
    b.append(table(
        ["Mục", "Nội dung"],
        [["1.0 Mục đích", "Nêu rõ mục đích và mục tiêu của phép thử."],
         ["2.0 Trách nhiệm thử", "Một người phải chịu trách nhiệm chung cho phép thử. Những nhân sự được "
                                 "huy động hỗ trợ người chịu trách nhiệm cũng phải được liệt kê."],
         ["3.0 Dụng cụ và vật tư cần thiết", "Mọi dụng cụ đặc biệt và phương tiện khác cần thiết phải "
                                             "được liệt kê. Dụng cụ phải được hiệu chuẩn và ở tình trạng "
                                             "hoạt động tốt."],
         ["4.0 Tần suất / chu kỳ kiểm tra cắt", "Ghi rõ tần suất hoặc chu kỳ thử."],
         ["5.0 Mối nguy", "Mọi mối nguy đặc biệt thuộc về phép thử, hoặc có thể phát sinh do phép thử, "
                          "phải được ghi chép đầy đủ."],
         ["6.0 Thông tin tham chiếu", "Có thể đưa vào quy trình một bản phác hoạ hoặc mô tả đơn giản về "
                                      "hoạt động của hệ. Ngoài ra phải liệt kê các bản vẽ vòng đo, phiếu "
                                      "đặc tả, sơ đồ, sổ tay tham chiếu hoặc sổ tay nhà cung cấp, hay "
                                      "phiếu dữ liệu vật liệu liên quan."],
         ["7.0 Quy trình thử chi tiết từng bước",
          "Quy trình từng bước phải bảo đảm (tối thiểu) xác nhận được: chức năng đúng của các thiết bị "
          "đầu vào, phần logic, đầu ra, reset và báo động; tốc độ phản ứng của hệ là chấp nhận được; và "
          "giá trị “như khi phát hiện” so với giá trị mong đợi phải được ghi lại."]],
        caption="Bảng 12-2. Mẫu quy trình thử cắt · Số quy trình: ____________"))
    b.append(p("Sau bước 7.0, mẫu còn có một khối <em>Kết quả / Nhận xét / Khiếm khuyết</em> để ghi kết quả "
               "phép thử cùng mọi nhận xét hoặc khiếm khuyết phát hiện được, và một dòng ký xác nhận: "
               "“Phép thử cắt hoàn thành bởi: ____________ Ngày: ____________”."))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Việc thử các hệ thống an toàn phải được thực hiện để kiểm chứng rằng chúng làm việc được "
               "và để bảo đảm tính toàn vẹn (hiệu năng) của chúng. Việc thử cũng là một yêu cầu của nhiều "
               "tiêu chuẩn, thực hành được khuyến nghị, hướng dẫn và quy định của chính phủ. Việc thử phải "
               "bao trùm toàn hệ (tức cảm biến, bộ giải logic, cơ cấu chấp hành cuối và các báo động liên "
               "quan) và phải dựa trên những mục tiêu rõ ràng, được định nghĩa tốt. Phải phân công trách "
               "nhiệm và phải tuân thủ quy trình bằng văn bản. Những phần khác nhau của hệ có thể được thử "
               "với chu kỳ khác nhau. Có thể xác định chu kỳ thử tối ưu bằng những phép tính đại số đơn "
               "giản. Hồ sơ thử phải được lưu giữ và phải thực hiện kiểm toán định kỳ để kiểm tra hiệu quả "
               "của quy trình và để so sánh các thông tin, chẳng hạn suất hỏng, với những giả định đã đưa "
               "ra trong giai đoạn thiết kế ban đầu của vòng đời."))

    b.append(note(
        "<b>Ba điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Miền giá trị của ET bị in sai đơn vị.</b> Mục 12.2 định nghĩa “ET = hiệu quả của phép thử "
        "(0 – 100 %)”, nhưng chính ví dụ ngay dưới đó lại dùng 0,95 và nhân trực tiếp vào λ<sub>d</sub>. "
        "Nếu hiểu là phần trăm thì kết quả sẽ sai 100 lần. Bản dịch ghi miền giá trị là 0 đến 1 cho khớp "
        "với cách dùng trong công thức (12.2).<br>"
        "<b>(2) Hình 12-2 được vẽ lại từ mô hình, không phải phóng theo hình gốc.</b> Hình trong sách chỉ "
        "là một đồ thị không kèm tham số: trục tung là RRF thang logarit 1000–10000, trục hoành là chu kỳ "
        "thử 0–36 tháng, đỉnh ở khoảng 6–9 tháng. Bản dịch tính lại đường cong từ chính mô hình mà mục "
        "8.9.1 mô tả (PFD = λ<sub>d</sub>·TI/2 + T<sub>thử</sub>/TI), chọn λ<sub>d</sub> = 5×10⁻⁴/năm và "
        "thời lượng thử 1,4 giờ để khớp dải trục của hình gốc; tham số được ghi ngay trong chú thích hình. "
        "Đỉnh tính ra là 9,6 tháng, hơi lệch về phía phải so với hình gốc.<br>"
        "<b>(3) Tiêu đề mục 12.2.1 khác nhau giữa mục lục và thân bài.</b> Mục lục ghi “ANSI/ISA-84.00.01-"
        "2004, Parts 1-3 (IEC 61511 Mod) Requirements for Functional Testing”, còn tiêu đề trong thân bài "
        "chỉ ghi “ANSI/ISA-84.00.01-2004 Requirements for Functional Testing”. Bản dịch theo thân bài."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi). <em>Functional Safety: Safety "
        "Instrumented Systems for the Process Industry Sector</em>.",
        "Lihou, D. và Z. Kabir. “Sequential testing of safety systems”. <em>The Chemical Engineer</em>, "
        "tháng 12/1985.",
        "29 CFR Part 1910.119. <em>Process Safety Management of Highly Hazardous Chemicals</em>. U.S. "
        "Federal Register, 24/02/1992.",
        "ISA-TR84.00.03-2002. <em>Guidance for Testing of Process Sector Safety Instrumented Functions "
        "(SIF) Implemented as or Within Safety Instrumented Systems (SIS)</em>.",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "A SIL is a number on paper until somebody actually goes out and tests the loop. This chapter is "
        "about that: what to test, how often, who does it, and why testing more often is not the same as "
        "being safer."))

    b.append(h2("Everything fails; the only question is when you find out"))
    b.append(p("Section 12.1 puts the argument in five words: everything fails, it is just a matter of "
               "when. The whole chapter follows from the second half of that sentence. A control loop is "
               "active, so its failures announce themselves — the reading goes wrong, the operator sees it, "
               "somebody fixes it. A safety loop is dormant. It sits at its healthy state doing nothing "
               "visible, and a dangerous failure leaves it sitting there looking exactly as healthy as "
               "before."))
    b.append(p("That asymmetry is why the first of the three reasons in 12.2 is the important one: safety "
               "systems get treated like control systems, and the assumption that failures will reveal "
               "themselves is carried across from a system where it happens to be true. It is not true "
               "here. A welded-shut relay, a plugged impulse line, a valve that has not moved in four years "
               "— none of these produce an alarm. They produce a demand that is not met."))
    b.append(fig(1, F.fig_12_1(), "en"))

    b.append(h2("The test interval is a design parameter, not a maintenance preference"))
    b.append(p("Equation 12.1 is one line long and it reorders the priorities of everyone who reads it. "
               "PFD<sub>avg</sub> = λ<sub>d</sub>·TI/2. The failure rate of the hardware and the interval "
               "between tests enter the same expression with the same weight. A system built from mediocre "
               "devices and tested diligently can beat a system built from excellent devices and tested "
               "once a decade, and it will usually cost less."))
    b.append(p("The corollary is uncomfortable for anyone who treats testing as a maintenance chore. If TI "
               "is a design parameter, then it belongs in the safety requirements specification, it "
               "belongs in the SIL calculation, and the number in the calculation has to be the number the "
               "site actually achieves. A verification that assumes a one-year interval while the plant "
               "gets round to it every four years is not a conservative calculation; it is a wrong one, "
               "and it is wrong in the dangerous direction."))

    b.append(h2("Test effectiveness is the number nobody measures"))
    b.append(p("Equation 12.2 introduces ET, and it is the most quietly damning term in the chapter. The "
               "first term assumes the test finds the failures; the second term assumes it does not, and "
               "lets them sit for the whole system lifetime SL. With ET at 95 per cent, a tenth of the "
               "dangerous failures are effectively never tested at all — they are only discovered when the "
               "system is replaced."))
    b.append(p("The worked example makes the scale concrete. The same valve, same failure rate, same "
               "replacement policy: tested annually it lands in SIL 1 with an RRF of 55, never tested it "
               "lands in SIL 0 with an RRF of 8. Nothing about the hardware changed. The seven-fold "
               "difference is entirely the test."))
    b.append(p("The uncomfortable part is that ET is almost never measured. It is asserted in the "
               "calculation, then assumed thereafter. The only way to know it is to record as-found "
               "conditions honestly and compare them with what the test claims to detect — which is "
               "precisely what the five record items in 12.2.1 exist for."))

    b.append(h2("The optimum test interval is not zero"))
    b.append(p("Figure 12-2 is the counter-intuitive one, and it is worth sitting with. The curve is not "
               "monotonic. Testing more often improves availability of the function but takes the system "
               "out of service for the duration of each test, and at some point the second effect overtakes "
               "the first. A simplex system in bypass has an availability of zero, not 99 per cent; a "
               "triplicated system in test is a dual system."))
    b.append(fig(2, F.fig_12_2(), "en"))
    b.append(p("So there is a genuine optimum, and it is a calculable number rather than a matter of "
               "opinion. For the parameters drawn here it lands near nine months. The practical lesson is "
               "not the exact figure — it depends on the loop — but that the curve has two arms with two "
               "different causes, and that a test policy justified by \"more is better\" is as unexamined "
               "as a policy justified by \"we do it at turnaround\"."))

    b.append(h2("Forcing is not testing"))
    b.append(p("Section 12.2.2 draws a line that gets crossed constantly in practice: forcing an input or "
               "an output in the logic solver is not a test. A force proves that the software responds to a "
               "value somebody typed. It proves nothing about the transmitter, the cable, the impulse "
               "line, the solenoid or the valve, because none of them is in the circuit."))
    b.append(p("Forcing is worse than a jumper in one specific way. A jumper on a terminal is at least "
               "visible to the next person who opens the cabinet. A force lives in the controller, "
               "survives downloads in many systems, and is invisible to anyone not logged in and looking. "
               "That is why the chapter wants forcing confined to maintenance and why chapter 11 wants an "
               "alarm on every forced point."))

    b.append(h2("One procedure per function, written by the people who will run it"))
    b.append(p("The sample form in 12.6.1 looks bureaucratic until you notice what it asks for in item "
               "2.0 and item 5.0. Item 2.0 wants one named person with overall responsibility — not a "
               "department, a person. Item 5.0 wants the hazards of the test itself written down, which is "
               "the item most often skipped and the one that gets people hurt: a test that closes a valve "
               "on a live process is a hazard in its own right, and it needs to be assessed as one."))
    b.append(p("Testability, meanwhile, is designed rather than discovered. The loop in Figure 12-3 has an "
               "isolation valve so the transmitter can be pressurised, a bypass valve so the process keeps "
               "running around the shutdown valve, and two limit switches confirming that the valve "
               "actually reached its end position. Three additions, and a unit shutdown becomes a "
               "twenty-minute exercise — which is the only reason the interval in the calculation is "
               "achievable at all."))
    b.append(fig(3, F.fig_12_3(), "en"))
    b.append(p("The chapter's insistence that operations and maintenance help write the procedure is not "
               "politeness. A procedure written by an engineer in an office describes the system as "
               "designed. A procedure written with the technician describes the system as it is, including "
               "the valve that has to be tapped to seat and the junction box that needs a second person to "
               "hold the door."))

    b.append(h2("The record is the deliverable"))
    b.append(p("The five record items in 12.2.1 are short, and the last one carries the weight: results, "
               "including as-found and as-left conditions. As-found is the only honest measure of whether "
               "the test works and whether the assumed failure rate was right. As-left is the only evidence "
               "that the loop went back into service in the condition the calculation assumes."))
    b.append(p("A test without a record is an anecdote. It cannot be audited, it cannot update a failure "
               "rate, and it cannot defend the plant in an inquiry. The chapter closes by asking for "
               "periodic audits of the records precisely so that the assumptions made at design time can be "
               "compared with what the plant has actually been doing — which is the only feedback loop the "
               "safety lifecycle has."))
    return "".join(b)
