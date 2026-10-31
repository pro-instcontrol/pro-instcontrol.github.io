# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 14, Justification for a Safety System
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis14fig as F

PAGES_SRC = 19
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Justification</em> — biện minh: chứng minh bằng số rằng chi phí cho hệ an toàn là đáng. · "
            "<em>Risk receptor</em> — đối tượng chịu rủi ro: con người, môi trường, sản lượng, thiết bị vốn, "
            "uy tín công ty. · "
            "<em>Nuisance trip / spurious trip</em> — cắt nhầm: hệ an toàn cắt dây chuyền dù không có yêu "
            "cầu. · "
            "<em>Lifecycle cost</em> — chi phí vòng đời: toàn bộ chi phí sở hữu hệ, từ đặc tả tới thanh lý. · "
            "<em>Present value (PV)</em> — hiện giá: giá trị hôm nay của một chuỗi chi phí trong tương lai. · "
            "<em>RRF</em> — hệ số giảm rủi ro, bằng 1/PFD. · "
            "<em>MTTF<sup>spurious</sup></em> — thời gian trung bình tới một lần cắt nhầm.")
    return note(
        "<b>Key terms.</b> <em>Justification</em> — showing, in numbers, that the money spent on a safety "
        "system is money well spent. · <em>Risk receptor</em> — what the risk lands on: people, the "
        "environment, production, capital equipment, company image. · <em>Nuisance trip / spurious "
        "trip</em> — the safety system shuts the plant down when nothing demanded it. · <em>Lifecycle "
        "cost</em> — the total cost of owning the system, from specification to disposal. · <em>Present "
        "value (PV)</em> — what a stream of future payments is worth today. · <em>RRF</em> — risk reduction "
        "factor, equal to 1/PFD. · <em>MTTF<sup>spurious</sup></em> — mean time to a spurious trip.")


def body_vi():
    b = []
    b.append(lead(
        "Một hệ an toàn có thể bảo vệ con người, môi trường, sản lượng, thiết bị và uy tín của công ty — "
        "nhưng nó cũng tiêu tiền, và tiêu tiền ở ba chỗ khác nhau: lúc mua, lúc chạy, và lúc nó cắt nhầm. "
        "Chương này là về cách chứng minh — bằng số — rằng cả ba khoản ấy đều đáng."))
    b.append(ul([
        "Các kiểu hỏng của hệ an toàn",
        "Sự biện minh",
        "Trách nhiệm biện minh",
        "Cách biện minh",
        "Phân tích chi phí vòng đời",
        "Tối ưu hoá an toàn, độ tin cậy và chi phí vòng đời",
    ]))

    # ------------------------------------------------------------------ 14.1
    b.append(h2("14.1 Giới thiệu", "Introduction"))
    b.append(p("Muốn biện minh cho sự cần thiết của một hệ an toàn, trước hết phải hiểu vì sao người ta "
               "lắp những hệ ấy ngay từ đầu. Trong công nghiệp chế biến, hệ an toàn được dùng để hạ thấp "
               "rủi ro cho con người, cho môi trường, cho sản lượng, cho thiết bị vốn và cho uy tín công "
               "ty. Thực tế không hiếm trường hợp mức độ toàn vẹn an toàn (SIL) xác định cho một số chức "
               "năng an toàn lại cao hơn mức cần cho bảo vệ con người, vì lý do kinh tế hoặc môi trường."))
    b.append(p("SIL của mỗi chức năng thường dựa trên những thông lệ mà công ty đã xây dựng theo các tiêu "
               "chuẩn ngành (đã trình bày ở Chương 6). Các thông lệ nội bộ ấy thường được hiệu chỉnh để "
               "phản ánh mức rủi ro mà công ty chấp nhận. Khi ấy, có thể không cần thêm một bước biện minh "
               "nào nữa, vì bản thân quy trình nội bộ đã bao hàm việc biện minh."))
    b.append(p("Nhiều công ty chỉ lắp hệ an toàn để giải quyết vấn đề bảo vệ con người và tuân thủ yêu cầu "
               "pháp chế. Trong trường hợp ấy, SIL xác định chỉ phản ánh “SIL cho con người”. Cách làm này "
               "dựa trên giả định rằng cắt được quá trình là đã giải quyết xong mối lo an toàn. Thường "
               "không còn nhu cầu biện minh nào khác — các yêu cầu an toàn phải được thoả mãn vì lý do "
               "pháp lý, đạo đức, tài chính và luân lý. Biện minh cho một hệ an toàn thuần tuý từ góc độ an "
               "toàn con người hầu như không phải là vấn đề."))
    b.append(p("Một số công ty lại muốn có thêm một bước biện minh để chứng minh rằng chi phí bỏ ra cho hệ "
               "an toàn là đáng. Nếu làm một phân tích chi phí/lợi ích chi tiết, có thể phát hiện ra rằng "
               "chi phí cho hệ an toàn là quá cao và không thể biện minh được so với phương án không lắp "
               "hệ. Vì vậy, việc biện minh cho hệ dựa trên phân tích cẩn thận tác động của từng loại hậu "
               "quả."))
    b.append(p("Khi biện minh cho sự cần thiết của một hệ an toàn, cần xét hai vấn đề tách biệt:"))
    b.append(ol([
        "Các chức năng an toàn có thể biện minh được không dựa trên những mức toàn vẹn đã chọn để xử lý "
        "các đối tượng chịu rủi ro khác ngoài con người (ví dụ: mất sản lượng, hư hỏng thiết bị)?",
        "Mối liên hệ giữa an toàn, độ tin cậy và chi phí vòng đời của hệ an toàn. Vấn đề an toàn nói về "
        "hiệu năng an toàn của hệ theo mức giảm rủi ro yêu cầu — nói cách khác, hệ có cắt khi cần không. "
        "Vấn đề độ tin cậy nói về hiệu năng cắt nhầm và tác động của những lần cắt nhầm ấy lên an toàn và "
        "lên tổng chi phí — nói cách khác, cắt nhầm gây thiệt hại gì cho sản lượng và cho an toàn (do "
        "những rủi ro phát sinh của việc dừng và khởi động ngoài kế hoạch)? Phân tích chi phí vòng đời "
        "nói về tổng chi phí của hệ trong suốt đời sống của nó.",
    ]))
    b.append(p("Vì thế, một hệ an toàn có thể được biện minh không chỉ bằng mức toàn vẹn an toàn đã chọn, "
               "mà còn bằng độ tin cậy và tổng chi phí vòng đời của nó."))
    b.append(p("Một vấn đề nữa mà người thiết kế hệ điều khiển thường gặp là dùng hệ an toàn để thay thế "
               "các lớp bảo vệ khác, chứ không phải để bổ sung cho chúng. Đôi khi người ta yêu cầu kỹ sư "
               "điều khiển phân tích và đề xuất lắp hệ an toàn thay cho lớp bảo vệ khác vì lý do chi phí, "
               "tiến độ hoặc cạnh tranh. Ví dụ điển hình là lắp hệ bảo vệ áp suất có mức toàn vẹn cao "
               "(HIPPS) để bỏ được các thiết bị xả áp cơ khí. Có những nhà máy đã qua quá nhiều lần nâng "
               "cấp và mở rộng đến mức hệ đốt bùng (flare) ban đầu không còn đủ lưu lượng cho một sự cố "
               "toàn nhà máy nữa. Khi ấy, lắp thiết bị đo bảo vệ áp suất (để van an toàn không mở, nhờ đó "
               "không làm quá tải hệ flare) có thể rẻ hơn là thay cả hệ flare."))
    b.append(p("Chương này sẽ trình bày những vấn đề sau và tác động của chúng lên việc biện minh cho hệ "
               "an toàn:"))
    b.append(ul([
        "các kiểu hỏng của hệ an toàn;",
        "sự biện minh;",
        "trách nhiệm biện minh;",
        "cách biện minh;",
        "phân tích chi phí vòng đời;",
        "tối ưu hoá an toàn, độ tin cậy và chi phí vòng đời.",
    ]))

    # ------------------------------------------------------------------ 14.2
    b.append(h2("14.2 Các kiểu hỏng của hệ an toàn", "Safety System Failure Modes"))
    b.append(p("Suốt cuốn sách này đã nhấn mạnh rằng hệ an toàn nói chung hỏng theo hai kiểu khác nhau: "
               "hỏng an toàn và hỏng nguy hiểm. Có thể hiểu rõ hơn tác động của những hỏng hóc ấy lên việc "
               "biện minh bằng cách chia tiếp hai kiểu ấy thành bốn loại:"))
    b.append(ol([
        "<b>Hỏng nguy hiểm không phát hiện được:</b> hệ đã hỏng theo chiều nguy hiểm và sẽ không đáp ứng "
        "một yêu cầu cắt, nhưng không có dấu hiệu nào cho biết có vấn đề.",
        "<b>Hỏng nguy hiểm phát hiện được:</b> hệ đã hỏng theo chiều nguy hiểm nhưng hỏng hóc được báo "
        "cho người vận hành qua chức năng tự chẩn đoán của hệ. Hệ sẽ không đáp ứng một yêu cầu cắt cho "
        "tới khi vấn đề được khắc phục.",
        "<b>Chế độ suy giảm do hỏng một phần của hệ dư thừa:</b> áp dụng cho hệ dư thừa có khả năng chịu "
        "lỗi. Hỏng một kênh (an toàn hay nguy hiểm) được báo cho người vận hành qua tự chẩn đoán, nhưng "
        "hệ vẫn đáp ứng được yêu cầu cắt.",
        "<b>Hỏng kiểu cắt nhầm:</b> hỏng hóc gây ra một lần cắt nhầm (tức một lần dừng ngoài kế hoạch). "
        "Nhà máy phải khởi động lại sau khi khắc phục xong.",
    ]))

    b.append(h3("Kiểu 1: hỏng nguy hiểm không phát hiện được", "Mode 1: Dangerous Undetected Failure"))
    b.append(p("Đây thường được coi là kịch bản xấu nhất. Xác suất hỏng nguy hiểm không phát hiện được là "
               "cơ sở để tính xác suất hỏng khi có yêu cầu (PFD<sub>avg</sub>) và mức toàn vẹn an toàn "
               "(SIL) của chức năng hay của hệ (đã trình bày ở Chương 8). Việc xác định SIL phải dựa trên "
               "triết lý chấp nhận rủi ro của công ty. Chính sách ấy phải được thiết lập rõ ràng và mọi "
               "bên liên quan phải hiểu. Nếu được như vậy, việc xác định SIL cho các vấn đề bảo vệ con "
               "người khó có thể bị ban lãnh đạo chất vấn. Kiến trúc hay mức dự phòng cần thiết để thoả mãn "
               "SIL đã xác định thường được chấp nhận không mấy khó khăn. Cách duy nhất để biết một hỏng "
               "nguy hiểm không phát hiện được đã xảy ra hay chưa là thử nghiệm thủ công."))

    b.append(h3("Kiểu 2: hỏng nguy hiểm phát hiện được", "Mode 2: Dangerous Detected Failure"))
    b.append(p("Nếu buộc phải có một hỏng nguy hiểm, thì đây là kiểu mong muốn nhất. Nếu thời gian sửa "
               "chữa trung bình (MTTR) của một hệ là tám giờ, và nếu trung bình sáu tháng mới có một yêu "
               "cầu cắt, thì xác suất xảy ra mối nguy trong khoảng tám giờ sửa chữa ấy vào khoảng một "
               "phần năm trăm năm mươi (1/550)."))
    b.append(p("Khi phát hiện một hỏng hóc như thế, người vận hành được kỳ vọng tuân theo các quy trình đã "
               "thiết lập. Quy trình vận hành có thể yêu cầu người vận hành:"))
    b.append(ol([
        "theo dõi sát hơn các tham số cắt và toàn bộ quá trình, sẵn sàng can thiệp thủ công để đưa quá "
        "trình về trạng thái an toàn khi có điều kiện bất thường. Trong trường hợp cực đoan, có thể phải "
        "dừng quá trình bằng tay ngay lập tức;",
        "yêu cầu nhân sự hỗ trợ khắc phục vấn đề. Nếu vấn đề không được khắc phục trong một giới hạn thời "
        "gian định trước, hệ có thể được thiết kế để tự động cắt. Giới hạn thời gian ấy thường do cơ quan "
        "chứng nhận đặt ra (ví dụ TÜV);",
        "mức độ chẩn đoán của hệ — kể cả của thiết bị hiện trường — phải được xác lập và phân tích như một "
        "phần của thiết kế tổng thể. Có thể phát sinh thêm chi phí để có được mức chẩn đoán yêu cầu, và "
        "khoản ấy cần được biện minh.",
    ]))

    b.append(h3("Kiểu 3: chế độ suy giảm", "Mode 3: Degraded Mode"))
    b.append(p("Hệ dư thừa có khả năng chịu lỗi (tức chịu được hỏng hóc mà vẫn vận hành đúng) và được dùng "
               "rộng rãi mỗi khi phải giải quyết đồng thời cả vấn đề an toàn lẫn vấn đề khả dụng/độ tin "
               "cậy. Đây rõ ràng là kiểu hỏng mong muốn nhất, vì hệ vẫn làm việc trong khi vấn đề đang được "
               "khắc phục. Dự phòng làm tăng chi phí lắp đặt ban đầu, nhưng tổng chi phí vòng đời của hệ "
               "lại có thể thấp hơn. Mục 14.7 và 14.8 trình bày một ví dụ như thế."))

    b.append(h3("Kiểu 4: hỏng kiểu cắt nhầm", "Mode 4: Nuisance Trip Failure"))
    b.append(p("Các tiêu chuẩn như IEC 61508 và IEC 61511 tập trung vào hỏng nguy hiểm và vấn đề hiệu "
               "năng (hệ có cắt khi cần không) mà không xử lý đầy đủ các vấn đề gắn với hỏng an toàn (tức "
               "cắt nhầm). Cứ mỗi lần hệ có sự cố là cắt cả một phân xưởng không phải lúc nào cũng là việc "
               "làm an toàn nhất hay kinh tế nhất. Đoạn sau trong 29 CFR 1910.119 tóm tắt những lo ngại về "
               "cắt nhầm:"))
    b.append(quote(
        "Trong các quá trình lọc hoá dầu, đôi khi có trường hợp một thiết bị vượt quá mức được coi là "
        "“chấp nhận được”, và người ta áp dụng các biện pháp tạm thời để đưa thiết bị trở lại đúng tham "
        "số vận hành an toàn. Theo (j)(4), khi phát hiện tình huống như vậy thì bắt buộc phải dừng ngay "
        "toàn bộ quá trình. Dừng và khởi động vốn là những thao tác nguy hiểm, và người ta cố tránh trừ "
        "khi thật cần thiết. Thêm nữa, tuổi thọ của một số bộ phận chịu ảnh hưởng trực tiếp của số lần "
        "chúng bị tác động. Chúng tôi cho rằng giữ số lần dừng ở mức tối thiểu là thúc đẩy an toàn chứ "
        "không phải làm giảm an toàn.",
        "29 CFR 1910.119"))
    b.append(p("Không hiếm trường hợp một phần hệ an toàn bị vô hiệu hoá hoặc bị bypass khi mức cắt nhầm "
               "không thể chấp nhận được bắt đầu ảnh hưởng xấu tới sản xuất. OSHA và EPA đã báo cáo những "
               "vụ tai nạn xảy ra chính vì các bypass ấy. [Tài liệu 3] Để giảm số lần cắt nhầm, hệ có thể "
               "cần thêm mức dự phòng (tức khả năng chịu lỗi). Điều này tác động tới chi phí và độ phức "
               "tạp của hệ, và cần được biện minh."))

    # ------------------------------------------------------------------ 14.3
    b.append(h2("14.3 Sự biện minh", "Justification"))
    b.append(p("Như đã nói ở phần giới thiệu, có một số đối tượng chịu rủi ro có thể được hưởng lợi từ "
               "việc lắp hệ an toàn: con người, môi trường, sản lượng, thiết bị vốn và uy tín công ty. Việc "
               "phân bổ tiền để bù đắp cho mất mát sinh mạng hay thương tích của con người là một vấn đề "
               "rất dễ gây tranh cãi. Nhiều công ty tránh công bố hoặc tránh dùng những con số như thế "
               "trong việc biện minh cho hệ an toàn. Tuy vậy, hoàn toàn có thể định lượng được tác động tài "
               "chính của việc không lắp hệ an toàn vì những lý do khác. Hư hỏng thiết bị thường kéo theo "
               "mất sản lượng, và hai yếu tố này có thể gộp lại với nhau. Một số vấn đề như tác động lên uy "
               "tín công ty thì khó định lượng, nhưng vẫn có thể xử lý theo cách định tính."))
    b.append(p("Việc biện minh cho một hệ an toàn thường cần đến chuyên môn của kỹ sư hệ điều khiển, vì họ "
               "nắm dữ liệu chi phí lắp đặt và vận hành hệ an toàn. Việc biện minh có thể dựa trên phân "
               "tích chi phí–lợi ích. Chi phí bao gồm thiết kế kỹ thuật, mua sắm, lắp đặt, vận hành và bảo "
               "trì hệ. Lợi ích là khoản tiết kiệm nhờ giảm số thương tích, số sự cố và mất sản lượng. "
               "Chương này tập trung vào việc biện minh từ hai góc độ sau:"))
    b.append(ol([
        "hư hỏng thiết bị và mất sản lượng kéo theo;",
        "tránh được những lần cắt nhầm.",
    ]))

    # ------------------------------------------------------------------ 14.4
    b.append(h2("14.4 Trách nhiệm biện minh", "Responsibilities for Justification"))
    b.append(p("Trách nhiệm biện minh cho một hệ có thể khác nhau, tuỳ theo hệ đang được xét để bảo vệ "
               "thiết bị và sản lượng hay để tránh cắt nhầm. (Như đã nói ở trên, biện minh cho hệ an toàn "
               "thuần tuý từ góc độ an toàn con người hầu như không phải là vấn đề.) Với hư hỏng thiết bị "
               "và mất sản lượng kéo theo, nhân sự kỹ thuật quá trình và kỹ thuật sản xuất có thể cần đóng "
               "vai trò chủ trì trong việc biện minh."))
    b.append(p("Vấn đề thường nảy sinh khi có đề xuất nâng cao hoặc cải thiện độ tin cậy của hệ để thoả "
               "mãn yêu cầu về cắt nhầm. Việc ấy thường làm tăng chi phí và/hoặc độ phức tạp của hệ. Những "
               "đề xuất như vậy thường vấp phải phản đối vì các lý do sau:"))
    b.append(ul([
        "một số người cho rằng đây là vấn đề sản xuất, không phải vấn đề an toàn. Nhận định ấy thường sai.",
        "mục tiêu của hệ an toàn là bảo vệ nhà máy. Những lần cắt không đáng có do hệ an toàn hỏng lại có "
        "thể bị coi là vấn đề của hệ điều khiển, và đáng lẽ phải do nhân sự điều khiển giải quyết. Các "
        "giám đốc sản xuất và vận hành không muốn thấy nhà máy dừng vì những lý do không cần thiết, và họ "
        "có thể đáp lại rằng: “Anh nói sao, hệ an toàn của anh sẽ cắt nhà máy của tôi ít nhất mỗi năm một "
        "lần?!”",
        "ngân sách dự án thường đã cố định ở giai đoạn này. Người ta thường ngại chi thêm tiền trừ khi "
        "chứng minh được rằng khoản ấy là hoàn toàn hợp lý.",
        "dữ liệu dùng để tính tần suất cắt nhầm có thể bị chất vấn.",
    ]))
    b.append(p("Việc biện minh cho một hệ an toàn vượt trên các yêu cầu SIL thường là trách nhiệm của kỹ "
               "sư hệ điều khiển. Lợi ích của một hệ an toàn có độ tin cậy cao hơn có vẻ hiển nhiên, nhưng "
               "đừng cho rằng mọi người đều đồng ý. Một số câu hỏi thường gặp:"))
    b.append(ul([
        "“Dự án trước đâu có cần hệ an toàn phức tạp đến thế. Sao bây giờ anh lại khăng khăng đòi sự phức "
        "tạp và chi phí ấy?”",
        "“Có thể nâng cấp hệ sau được không, nếu đúng là chúng ta có vấn đề?”",
        "“Anh đã xét những phương án rẻ hơn nào rồi? Phương án nào tốt nhất?”",
    ]))
    b.append(p("Cần biện minh thoả đáng cho mọi khoản chi. Mọi dự án đều đang cạnh tranh để giành phần "
               "ngày càng ít ỏi hơn của nguồn vốn. Tác động của khoản chi lên lợi nhuận cuối cùng sẽ bị "
               "soi xét rất kỹ."))

    # ------------------------------------------------------------------ 14.5
    b.append(h2("14.5 Cách biện minh", "How to Justify"))
    b.append(p("Việc biện minh cho bất kỳ hệ nào thường dựa trên phân tích tài chính. Vì vậy, cần ôn lại "
               "một số thuật ngữ và hàm tài chính cơ bản, cùng cách giá trị của đồng tiền thay đổi theo "
               "thời gian."))
    b.append(p("Giá trị tương lai (FV) của đồng tiền thay đổi theo thời gian và lãi suất. Nếu mỗi năm đầu "
               "tư một khoản cố định M, thì giá trị tương lai của khoản đầu tư ấy sau N năm, với lãi suất "
               "R, được biểu diễn bằng:"))
    b.append(eq("FV = M · [(1 + R)<sup>N</sup> − 1] / R", "14.1"))
    b.append(p("Cũng có thể tính hiện giá (PV) của những khoản đầu tư thực hiện đều đặn trong tương lai. "
               "Nếu mỗi năm đầu tư một khoản cố định M trong N năm, với lãi suất R, thì hiện giá của khoản "
               "đầu tư ấy được biểu diễn bằng:"))
    b.append(eq("PV = M · [1 − (1 + R)<sup>−N</sup>] / R", "14.2"))
    b.append(p("Khi biện minh cho một hệ an toàn, ta quan tâm tới hiện giá của những tổn thất có thể định "
               "lượng được theo năm trong một số năm. Nói cách khác: có thể tính tác động của một sự kiện "
               "nguy hiểm và/hoặc của những lần cắt nhầm theo năm, tính hiện giá của các tổn thất tương "
               "lai, rồi từ đó xác định mức chi phí giới hạn cho hệ an toàn. Nếu chi phí lớn hơn lợi ích "
               "thì việc biện minh là đáng ngờ."))

    b.append(h3("Ví dụ biện minh số 1 — hư hỏng thiết bị và mất sản lượng kéo theo",
                "Justification Example #1 — Equipment Damage and Associated Production Losses"))
    b.append(p("Một sự kiện nguy hiểm có thể gây nổ, ước tính thiệt hại thiết bị 1.000.000 $. Phân tích "
               "cho thấy tần suất kỳ vọng của sự kiện này là 2,0 × 10<sup>−3</sup>/năm (1/500 mỗi năm). "
               "Một hệ an toàn đề xuất có hệ số giảm rủi ro 100 sẽ đưa rủi ro tổng thể xuống còn "
               "2,0 × 10<sup>−5</sup>/năm (1/50.000 mỗi năm). Giả sử hệ an toàn có đời sống kỳ vọng 20 năm "
               "và lãi suất 6 %, thì mức chi phí ban đầu nào có thể biện minh được cho hệ ấy?"))
    b.append(p("<b>Lời giải:</b> Nếu hệ an toàn giảm rủi ro từ 2,0 × 10<sup>−3</sup>/năm xuống "
               "2,0 × 10<sup>−5</sup>/năm thì trung bình mỗi năm tiết kiệm được 2.000 $ − 20 $, tức 1.980 $ "
               "(1.000.000 $/500 − 1.000.000 $/50.000). Khoản tiền lớn nhất có thể biện minh cho hệ an "
               "toàn chính là hiện giá của một chuỗi 20 khoản thanh toán 1.980 $ mỗi năm với lãi suất 6 %. "
               "Tính theo phương trình 14.2:"))
    b.append(eq("PV = 1.980 $ × [1 − (1,06)<sup>−20</sup>] / 0,06 = 22.710 $"))
    b.append(p("Lời giải trên giả định chi phí vận hành và bảo trì của hệ an toàn là không đáng kể. Trên "
               "thực tế, những chi phí ấy cũng phải được tính vào."))

    b.append(h3("Ví dụ biện minh số 2 — tránh những lần cắt nhầm",
                "Justification Example #2 — Avoidance of Spurious Trips"))
    b.append(p("Tổng chi phí của một lần cắt nhầm đối với một phân xưởng ước tính 100.000 $. Tần suất cắt "
               "nhầm của hệ an toàn hiện hữu là một lần mỗi 5 năm. Có thể nâng cấp hệ với chi phí 70.000 $ "
               "để giảm tần suất cắt nhầm xuống một lần mỗi 10 năm. Nếu đời sống của hệ được giả định là 20 "
               "năm và lãi suất là 5 %, khoản chi này có biện minh được không?"))
    b.append(p("<b>Lời giải:</b> Chi phí cắt nhầm hằng năm khi không nâng cấp là 100.000 $/5 năm, tức "
               "20.000 $ mỗi năm. Chi phí cắt nhầm hằng năm sau khi nâng cấp là 100.000 $/10 năm, tức "
               "10.000 $ mỗi năm. Lợi ích tiềm năng là 10.000 $ mỗi năm (20.000 $ − 10.000 $)."))
    b.append(p("Chi phí hằng năm của việc vay 70.000 $ trong 20 năm với lãi suất 5 % thu được bằng cách "
               "giải phương trình 14.2 theo M:"))
    b.append(eq("M = (70.000 $ × 0,05) / [1 − (1 + 0,05)<sup>−20</sup>] = 5.617 $/năm"))
    b.append(p("Khoản chi này biện minh được, vì lợi ích lớn hơn chi phí."))

    # ------------------------------------------------------------------ 14.6
    b.append(h2("14.6 Chi phí vòng đời", "Lifecycle Costs"))
    b.append(p("Một cách để biện minh cho khoản chi cho hệ an toàn là hoàn thành một phân tích chi phí "
               "vòng đời cho các phương án đang được xét. Chi phí vòng đời phản ánh tổng chi phí sở hữu "
               "hệ. Bằng cách tính chi phí vòng đời, có thể phân tích các phương án một cách định lượng và "
               "nhất quán hơn. Bảng 14-1 mô tả những khoản chi chủ yếu phát sinh trong đời sống của một hệ "
               "an toàn. Danh sách được chia thành chi phí cố định ban đầu (tức chi phí thiết kế, mua sắm, "
               "lắp đặt, chạy thử và đưa vào vận hành) và chi phí hằng năm (tức bảo trì và những khoản chi "
               "thường xuyên khác gắn với hệ). Ở một mức độ nào đó, các khoản này phản ánh những hạng mục "
               "trong mô hình vòng đời đã trình bày ở Chương 2."))
    b.append(table(
        ["Hạng mục chi phí", "Ghi chú"],
        [
            "Chi phí cố định ban đầu",
            ["Xác định SIL", "Chi phí hoàn thành việc xác định mức toàn vẹn an toàn (sau khi đã xem xét an "
                             "toàn và kết luận là cần một hệ an toàn)."],
            ["Đặc tả yêu cầu an toàn và đặc tả thiết kế",
             "Chi phí nhân lực để hoàn thành đặc tả yêu cầu an toàn, thiết kế khái niệm và đặc tả thiết kế "
             "chi tiết."],
            ["Thiết kế chi tiết và kỹ thuật", "Chi phí cho toàn bộ thiết kế chi tiết và kỹ thuật."],
            ["Cảm biến", "Chi phí mua cảm biến."],
            ["Phần tử cuối", "Chi phí mua van và các phần tử cuối khác."],
            ["Hệ logic", "Chi phí mua hệ logic."],
            ["Khác: nguồn, dây, hộp đấu nối, giao diện vận hành",
             "Chi phí cho các thiết bị khác cần thiết để lắp đặt và giám sát hệ an toàn."],
            ["Đào tạo ban đầu",
             "Chi phí đào tạo nhân sự thiết kế, vận hành và hỗ trợ để họ thiết kế, lắp đặt và thử nghiệm "
             "hệ."],
            ["FAT/Lắp đặt/PSAT",
             "Chi phí thử nghiệm chấp nhận tại nhà máy, lắp đặt thiết bị và thử nghiệm chấp nhận trước "
             "khởi động."],
            ["Khởi động và hiệu chỉnh", "Hầu hết hệ đều cần một số hiệu chỉnh trước khi vận hành đầy đủ."],
            "Chi phí hằng năm",
            ["Đào tạo thường xuyên", "Đào tạo nhắc lại thường kỳ cho nhân sự vận hành và hỗ trợ."],
            ["Thay đổi kỹ thuật",
             "Khoản này có thể đáng kể do yêu cầu xem xét lại và cập nhật tài liệu."],
            ["Hợp đồng dịch vụ",
             "Hệ logic khả trình thường cần một hợp đồng dịch vụ với nhà chế tạo để giải quyết những vấn "
             "đề “khó”."],
            ["Chi phí vận hành và bảo trì cố định", "Điện, nước, các chương trình bảo trì phòng ngừa, v.v."],
            ["Phụ tùng", "Các phụ tùng trọng yếu theo khuyến nghị của nhà cung cấp."],
            ["Thử nghiệm định kỳ", "Thử nghiệm định kỳ do nhân sự vận hành và hỗ trợ thực hiện."],
            ["Chi phí sửa chữa",
             "Chi phí sửa chữa hoặc thay thế các mô-đun hỏng, dựa trên tần suất hỏng dự đoán."],
            ["Chi phí mối nguy",
             "Chi phí dựa trên phân tích mối nguy. Tần suất mối nguy là hàm của PFD của hệ và của tần suất "
             "yêu cầu cắt."],
            ["Chi phí cắt nhầm",
             "Chi phí mất sản lượng, dựa trên MTBF<sup>spurious</sup> của hệ."],
            ["Hiện giá của chi phí hằng năm",
             "Hiện giá của chi phí hằng năm, dựa trên lãi suất hiện hành và đời sống dự đoán của hệ. Khoản "
             "này được cộng vào chi phí cố định ban đầu để có hiện giá của toàn bộ chi phí. PV có thể tính "
             "bằng phương trình: PV = M[1 − (1 + R)<sup>−N</sup>]/R, trong đó M là chi phí hằng năm, R là "
             "lãi suất và N là số năm."],
            ["Tổng chi phí vòng đời",
             "Tổng chi phí trong đời sống của hệ: tổng của chi phí cố định ban đầu và hiện giá của chi phí "
             "cố định hằng năm."],
        ],
        caption="Bảng 14-1. Phân rã chi phí của một hệ an toàn. Chú ý hai dòng cuối của mỗi nhóm: một khoản "
                "chi hằng năm chỉ có nghĩa khi được quy về hiện giá, và một hệ chỉ thực sự rẻ hay đắt khi "
                "cả hai nhóm được cộng lại."))

    # ------------------------------------------------------------------ 14.7
    b.append(h2("14.7 Ví dụ xem xét", "Review Example"))
    b.append(p("Ví dụ sau đây sẽ được dùng để xây dựng chi phí vòng đời cho hai phương án hệ an toàn khả "
               "dĩ."))
    b.append(p("Hai vật liệu cháy được A và B được hệ điều khiển quá trình cơ bản (BPCS) nạp tự động và "
               "liên tục vào một bình phản ứng theo một tỉ lệ cố định. Điểm đặt của bộ điều khiển lưu lượng "
               "chính số 1 được đặt bởi bộ điều khiển mức của bình, nhằm giữ mức trong bình cố định. Bộ điều "
               "khiển lưu lượng của dòng A chỉnh điểm đặt của bộ điều khiển lưu lượng dòng B để giữ đúng "
               "tỉ lệ."))
    b.append(p("Hình 14-1 trình bày phần điều khiển quá trình cơ bản."))
    b.append(fig(1, F.fig_14_1(), "vi"))
    b.append(p("Trong một lần xem xét an toàn, người ta đã nhận diện được những sự kiện nguy hiểm sau:"))
    b.append(table(
        ["Mối nguy", "Nguyên nhân", "Hậu quả", "Khả năng xảy ra"],
        [
            ["Thải khí cháy ra môi trường", "Hỏng BPCS", "Cháy, nổ; thiệt hại 500.000 $", "Trung bình"],
            ["Vỡ bình", "Hỏng BPCS và van an toàn", "Thiệt hại 750.000 $", "Thấp"],
        ],
        caption="Bảng 14-2. Tóm tắt phân tích mối nguy. Ghi chú của bảng trong bản gốc: một lần cắt nhầm "
                "tốn 10.000 $. Con số ấy là đầu vào cho cột chi phí cắt nhầm ở Bảng 14-3 và 14-4.",
        cls="tbl moc"))
    b.append(p("Người ta đã đề xuất các thiết bị đo an toàn sau:"))
    b.append(ol([
        "lắp một chức năng cắt áp suất cao để đóng các dòng nạp A và B vào bình;",
        "lắp một chức năng cắt mức cao để đóng các dòng nạp A và B vào bình.",
    ]))
    b.append(p("Dựa trên dữ liệu trên, và dùng ma trận xác định SIL ba chiều đã mô tả ở Mục 6.8 và Hình "
               "6-2, mỗi chức năng an toàn (áp suất và mức) cần SIL 1."))
    b.append(p("Hai hệ an toàn sau đây được đề xuất:"))
    b.append(h4("Ca 1"))
    b.append(ul([
        "Cảm biến: cảm biến đơn.",
        "Logic: logic rơ-le.",
        "Van: van cắt độc lập, đơn, trên mỗi dòng.",
    ]))
    b.append(h4("Ca 2"))
    b.append(ul([
        "Cảm biến: ba cảm biến bỏ phiếu 2oo3 (chọn giá trị giữa).",
        "Logic: PLC an toàn chịu lỗi.",
        "Van: van cắt độc lập, đơn, trên mỗi dòng.",
    ]))

    b.append(h3("Tính PFD<sub>avg</sub> và MTTF<sub>spurious</sub> cho Ca 1",
                "PFDavg and MTTFspurious Calculations for Case 1"))
    b.append(p("Dữ liệu hỏng (số lần hỏng mỗi năm):"))
    b.append(ul([
        "Cảm biến: λ<sub>du</sub> = 0,01 (MTTF 100 năm); λ<sub>s</sub> = 0,02 (MTTF 50 năm)",
        "Van và van điện từ: λ<sub>du</sub> = 0,02 (MTTF 50 năm); λ<sub>s</sub> = 0,1 (MTTF 10 năm)",
        "Bộ khuếch đại ngưỡng: λ<sub>du</sub> = 0,01 (MTTF 100 năm); λ<sub>s</sub> = 0,01 (MTTF 100 năm)",
        "Rơ-le điện-cơ: λ<sub>du</sub> = 0,002 (MTTF 500 năm); λ<sub>s</sub> = 0,02 (MTTF 50 năm)",
    ]))
    b.append(p("Dữ liệu bổ sung: khoảng thời gian thử nghiệm (TI) là 6 tháng."))
    b.append(h4("Tính PFD<sub>avg</sub>"))
    b.append(p("SIL được xác định cho từng chức năng riêng lẻ. Vì vậy, mô hình xác suất hỏng khi có yêu "
               "cầu (PFD) chỉ nên bao gồm một chức năng: 1 cảm biến, 1 bộ khuếch đại ngưỡng, 3 rơ-le điện-"
               "cơ và cả hai van."))
    b.append(ul([
        "PFD<sub>avg</sub> = λ<sub>du</sub> × TI/2",
        "PFD<sub>avg</sub> (cảm biến) = 0,01 × 0,5/2 = 0,0025",
        "PFD<sub>avg</sub> (bộ khuếch đại ngưỡng) = 0,01 × 0,5/2 = 0,0025",
        "PFD<sub>avg</sub> (rơ-le điện-cơ) = 3 × 0,002 × 0,5/2 = 0,0015",
        "PFD<sub>avg</sub> (van và van điện từ) = 2 × 0,02 × 0,5/2 = 0,0100",
        "<b>PFD<sub>avg</sub> (tổng) = 0,0165</b>",
    ]))
    b.append(p("Giá trị lớn nhất cho phép đối với một chức năng SIL 1 là 0,1. Vì vậy, hệ trên thoả mãn các "
               "yêu cầu an toàn. (Hệ số giảm rủi ro [1/PFD] là 60, nằm trong khoảng 10 đến 100 mà SIL 1 yêu "
               "cầu.)"))
    b.append(h4("Tính MTTF<sub>spurious</sub>"))
    b.append(p("Phép tính thời gian trung bình tới một lần cắt nhầm (MTTF<sub>spurious</sub>) phải bao gồm "
               "mọi thành phần có thể gây ra một lần cắt: cả hai cảm biến, cả hai bộ khuếch đại ngưỡng, 4 "
               "rơ-le điện-cơ, và cả hai van cùng van điện từ. Nguồn cấp được giả định là dư thừa nên được "
               "bỏ qua trong phép tính (vì các thành phần không dư thừa sẽ chi phối kết quả)."))
    b.append(ul([
        "MTTF<sub>spurious</sub> = 1/λ<sub>s</sub>",
        "MTTF<sub>spurious</sub> (cảm biến) = 1/(2 × 0,02) = 25 năm",
        "MTTF<sub>spurious</sub> (bộ khuếch đại ngưỡng) = 1/(2 × 0,01) = 50 năm",
        "MTTF<sub>spurious</sub> (rơ-le điện-cơ) = 1/(4 × 0,02) = 12,5 năm",
        "MTTF<sub>spurious</sub> (van và van điện từ) = 1/(2 × 0,1) = 5 năm",
        "<b>MTTF<sub>spurious</sub> (tổng) = 3 năm</b>",
    ]))
    b.append(p("Như vậy, trung bình khoảng 3 năm sẽ có một lần cắt nhầm."))
    b.append(p("Hệ của Ca 1 tuy thoả mãn yêu cầu của SIL 1, nhưng người ta cũng xét thêm một hệ có cảm "
               "biến dư thừa và logic khả trình."))
    b.append(fig(2, F.fig_14_2(), "vi"))

    b.append(h3("Tính PFD<sub>avg</sub> và MTTF<sub>spurious</sub> cho Ca 2",
                "PFDavg and MTTFspurious Calculations for Case 2"))
    b.append(p("Dữ liệu tần suất hỏng của các thiết bị hiện trường giống như Ca 1. Nhà cung cấp hệ logic "
               "thường cung cấp số liệu về hiệu năng an toàn và hiệu năng nguy hiểm của phần cứng họ bán. "
               "Mười phần trăm nguyên nhân chung được tính cho các cảm biến dư thừa và cho hệ logic. Chín "
               "mươi chín phần trăm chẩn đoán được giả định cho cấu hình cảm biến dư thừa. Về các công thức "
               "khác nhau, xem Chương 8. Cảm biến 2oo3 và hệ logic sẽ được thử ba năm một lần. Các van vẫn "
               "được thử sáu tháng một lần."))
    b.append(h4("Tính PFD<sub>avg</sub>"))
    b.append(p("SIL được xác định cho từng chức năng riêng lẻ. Vì vậy, mô hình PFD chỉ nên bao gồm một "
               "chức năng: cảm biến 2oo3, PLC an toàn 2oo3, và cả hai van. Chỉ cần tính phần nguyên nhân "
               "chung của các thành phần dư thừa (vì phần này sẽ chi phối kết quả)."))
    b.append(ul([
        "PFD<sub>avg</sub> (cảm biến 2oo3) = 0,01 × 0,01 × 0,1 × 3/2 = 0,000015 "
        "<span style=\"color:#888\">(tần suất hỏng × % hỏng không phát hiện × % nguyên nhân chung × "
        "khoảng thời gian thử/2)</span>",
        "PFD<sub>avg</sub> (PLC an toàn 2oo3) = (theo nhà cung cấp) = 0,00005",
        "PFD<sub>avg</sub> (van và van điện từ) = 2 × 0,02 × 0,5/2 = 0,0100",
        "<b>PFD<sub>avg</sub> (tổng) = 0,01</b>",
    ]))
    b.append(p("Giá trị lớn nhất cho phép đối với một chức năng SIL 1 là 0,1. Vì vậy, hệ này cũng thoả mãn "
               "các yêu cầu an toàn. (Hệ số giảm rủi ro [1/PFD] là 100, đúng ranh giới giữa SIL 1 và "
               "SIL 2.)"))
    b.append(h4("Tính MTTF<sub>spurious</sub>"))
    b.append(p("Phép tính MTTF<sub>spurious</sub> phải bao gồm mọi thành phần có thể gây ra một lần cắt: cả "
               "hai nhóm cảm biến 2oo3, PLC an toàn 2oo3, và cả hai van cùng van điện từ. Chỉ cần tính phần "
               "nguyên nhân chung của các thành phần dư thừa (vì phần này sẽ chi phối kết quả)."))
    b.append(ul([
        "MTTF<sub>spurious</sub> (cảm biến 2oo3) = 1/(2 × 0,02 × 0,1) = 250 năm "
        "<span style=\"color:#888\">(1 / số lượng × tần suất hỏng × % nguyên nhân chung)</span>",
        "MTTF<sub>spurious</sub> (PLC an toàn) = (theo nhà cung cấp) = 200 năm",
        "MTTF<sub>spurious</sub> (van và van điện từ) = 1/(2 × 0,1) = 5 năm",
        "<b>MTTF<sub>spurious</sub> (tổng) = 5 năm</b>",
    ]))
    b.append(p("Như vậy, trung bình khoảng 5 năm sẽ có một lần cắt nhầm. Van là mắt xích yếu trong Ca 2 (cả "
               "về an toàn lẫn về cắt nhầm), vì các phần còn lại của hệ đều chịu được lỗi. Hệ của Ca 2 an "
               "toàn hơn Ca 1 và ít cắt nhầm hơn. Phần phân tích chi phí vòng đời dưới đây so sánh tiếp hai "
               "hệ."))
    b.append(fig(3, F.fig_14_3(), "vi"))

    # ------------------------------------------------------------------ 14.8
    b.append(h2("14.8 Phân tích chi phí vòng đời chi tiết", "Detailed Lifecycle Cost Analysis"))
    b.append(p("Phân tích này nhằm minh hoạ kỹ thuật thực hiện một phân tích chi phí vòng đời. Số liệu ở "
               "đây rất chủ quan và không nhằm phản ánh chi phí thực của bất kỳ sản phẩm hay kỹ thuật lắp "
               "đặt cụ thể nào. Muốn có con số chính xác hơn, mỗi người phải dựa vào dữ liệu trong chính tổ "
               "chức của mình."))
    b.append(table(
        ["Hạng mục", "Vật tư ($)", "Nhân công ($)", "Tổng ($)"],
        [
            "Chi phí cố định ban đầu",
            ["Xác định SIL", "—", "2.000", "2.000"],
            ["Đặc tả yêu cầu an toàn/đặc tả thiết kế", "—", "5.000", "5.000"],
            ["Thiết kế chi tiết và kỹ thuật", "—", "30.000", "30.000"],
            ["Cảm biến", "4.000", "—", "4.000"],
            ["Phần tử cuối", "3.000", "—", "3.000"],
            ["Hệ logic", "10.000", "—", "10.000"],
            ["Khác: nguồn, dây, hộp đấu nối", "5.000", "—", "5.000"],
            ["Đào tạo ban đầu", "—", "5.000", "5.000"],
            ["FAT/Lắp đặt/PSAT", "5.000", "25.000", "30.000"],
            ["Khởi động và hiệu chỉnh", "2.000", "8.000", "10.000"],
            ["<b>Tổng chi phí cố định</b>", "", "", "<b>104.000</b>"],
            "Chi phí hằng năm",
            ["Đào tạo thường xuyên", "—", "3.000", "3.000"],
            ["Thay đổi kỹ thuật", "1.000", "4.000", "5.000"],
            ["Hợp đồng dịch vụ", "—", "—", "—"],
            ["Chi phí vận hành và bảo trì cố định", "—", "1.000", "1.000"],
            ["Phụ tùng", "2.000", "—", "2.000"],
            ["Thử nghiệm thủ công", "—", "25.000", "25.000"],
            ["Chi phí sửa chữa", "1.000", "500", "1.500"],
            ["Chi phí mối nguy", "—", "—", "12.000"],
            ["Chi phí cắt nhầm", "—", "—", "4.000"],
            ["<b>Tổng chi phí hằng năm</b>", "", "", "<b>45.500</b>"],
            ["Hiện giá chi phí hằng năm (đời 20 năm, lãi suất 5 %)", "", "", "567.031"],
            ["<b>Tổng chi phí vòng đời</b>", "", "", "<b>671.031</b>"],
        ],
        caption="Bảng 14-3. Chi phí vòng đời của Ca 1. Chín dòng chi phí hằng năm cộng lại là 53.500 $, "
                "nhưng bản gốc in tổng 45.500 $ — xem ghi chú (1) của người dịch ở cuối chương.",
        cls="tbl cost"))
    b.append(table(
        ["Hạng mục", "Vật tư ($)", "Nhân công ($)", "Tổng ($)"],
        [
            "Chi phí cố định ban đầu",
            ["Xác định SIL", "—", "2.000", "2.000"],
            ["Đặc tả yêu cầu an toàn/đặc tả thiết kế", "—", "5.000", "5.000"],
            ["Thiết kế chi tiết và kỹ thuật", "—", "30.000", "30.000"],
            ["Cảm biến", "12.000", "—", "12.000"],
            ["Phần tử cuối", "3.000", "—", "3.000"],
            ["Hệ logic", "30.000", "—", "30.000"],
            ["Khác: nguồn, dây, hộp đấu nối", "5.000", "—", "5.000"],
            ["Đào tạo ban đầu", "—", "15.000", "15.000"],
            ["FAT/Lắp đặt/PSAT", "5.000", "25.000", "30.000"],
            ["Khởi động và hiệu chỉnh", "2.000", "8.000", "10.000"],
            ["<b>Tổng chi phí cố định</b>", "", "", "<b>142.000</b>"],
            "Chi phí hằng năm",
            ["Đào tạo thường xuyên", "—", "3.000", "3.000"],
            ["Thay đổi kỹ thuật", "1.000", "1.000", "2.000"],
            ["Hợp đồng dịch vụ", "—", "2.000", "2.000"],
            ["Chi phí vận hành và bảo trì cố định", "—", "1.000", "1.000"],
            ["Phụ tùng", "4.000", "—", "4.000"],
            ["Thử nghiệm thủ công", "—", "15.000", "15.000"],
            ["Chi phí sửa chữa", "1.000", "500", "1.500"],
            ["Chi phí mối nguy", "—", "—", "6.000"],
            ["Chi phí cắt nhầm", "—", "—", "2.000"],
            ["<b>Tổng chi phí hằng năm</b>", "", "", "<b>36.500</b>"],
            ["Hiện giá chi phí hằng năm (đời 20 năm, lãi suất 5 %)", "", "", "454.871"],
            ["<b>Tổng chi phí vòng đời</b>", "", "", "<b>596.871</b>"],
        ],
        caption="Bảng 14-4. Chi phí vòng đời của Ca 2. Ở bảng này, các dòng cộng lại đúng bằng tổng in "
                "trong sách — đó là lý do ghi chú (1) của người dịch chỉ áp dụng cho Bảng 14-3.",
        cls="tbl cost"))
    b.append(p("Hệ của Ca 2 ít cắt nhầm hơn và an toàn hơn Ca 1. Ngoài chi phí thử nghiệm thủ công thấp "
               "hơn (nhờ thử cảm biến và hệ logic ít thường xuyên hơn), tổng chi phí vòng đời cũng thấp "
               "hơn, nghĩa là hệ của Ca 2 là phương án được ưu tiên và có thể biện minh được."))

    # ------------------------------------------------------------------ 14.9
    b.append(h2("14.9 Tối ưu hoá an toàn, độ tin cậy và chi phí vòng đời",
                "Optimizing Safety, Reliability and Lifecycle Costs"))
    b.append(p("Trước đây, nhiều người chỉ tập trung vào khối logic. Nhưng mô hình hoá đơn giản thường cho "
               "thấy thiết bị hiện trường có tác động lớn hơn nhiều, không chỉ lên hiệu năng an toàn mà cả "
               "lên hiệu năng cắt nhầm và tổng chi phí vòng đời. Có thể phân tích và so sánh nhiều phương án "
               "khác nhau (ví dụ dự phòng, khoảng thời gian thử, mức chẩn đoán tự động, nguyên nhân chung) "
               "dựa trên tác động dài hạn của chúng lên an toàn, độ tin cậy và chi phí."))
    b.append(p("Mô hình hoá độ tin cậy và phân tích chi phí vòng đời là những công cụ rất hiệu quả để tối "
               "ưu hoá thiết kế một hệ an toàn. Chúng cho phép tập trung vào đúng những phần tử của hệ cần "
               "được chú ý hơn. Nhờ các mô hình và phân tích chi phí, có thể biện minh tốt hơn cho cấu hình "
               "hệ và cho khoảng thời gian thử nghiệm dựa trên lợi ích dài hạn. Như ví dụ trên đã cho thấy, "
               "một hệ chịu lỗi có thể tốn hơn lúc đầu nhưng lại có chi phí vòng đời thấp hơn nhờ ít cắt "
               "nhầm hơn và giảm được chi phí thử nghiệm."))
    b.append(fig(4, F.fig_14_4(), "vi"))
    b.append(p("Cách tiếp cận này cũng dùng được để phân tích xem có thể dùng một hệ an toàn thay cho các "
               "lớp bảo vệ độc lập khác hay không. Điều thiết yếu là phải có kỹ sư quá trình cùng các "
               "chuyên gia hệ thống khác tham gia vào phân tích tổng thể."))

    # ------------------------------------------------------------------ summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Hầu hết công ty đều đã có sẵn những thông lệ để nhận diện nhu cầu về hệ an toàn nhằm giải "
               "quyết vấn đề an toàn con người. Trong những trường hợp ấy, việc biện minh cho hệ an toàn "
               "thường không phải là vấn đề."))
    b.append(p("Tuy vậy, hệ an toàn có thể được biện minh không chỉ vì an toàn con người, mà còn vì độ tin "
               "cậy và lợi ích tổng thể về chi phí vòng đời. Những yếu tố khác có thể biện minh cho việc "
               "dùng hệ an toàn gồm bảo vệ thiết bị vốn, mất sản lượng, môi trường và uy tín công ty. Mô "
               "hình hoá độ tin cậy và phân tích chi phí vòng đời là những công cụ lý tưởng để biện minh "
               "cho việc thiết kế và lắp đặt hệ an toàn."))

    # ------------------------------------------------------------------ note
    b.append(note(
        "<b>Ba điểm lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Bảng 14-3 có một dòng bị in sai.</b> Chín dòng chi phí hằng năm của Ca 1 cộng lại là "
        "53.500 $ (3.000 + 5.000 + 0 + 1.000 + 2.000 + 25.000 + 1.500 + 12.000 + 4.000), nhưng sách in tổng "
        "là 45.500 $. Hiện giá 567.031 $ đúng bằng 45.500 $ × 12,4622 (hệ số hiện giá 20 năm, 5 %), và "
        "tổng 671.031 $ cũng tính từ con số ấy — nghĩa là sai lệch nằm ở một dòng, không nằm ở phép cộng "
        "sau đó. Nhiều khả năng dòng “thử nghiệm thủ công” đáng lẽ là 17.000 $ chứ không phải 25.000 $. "
        "Bảng 14-4 không có vấn đề này: các dòng của Ca 2 cộng đúng 36.500 $. Kết luận của mục 14.8 không "
        "đổi trong cả hai cách tính — Ca 1 vẫn đắt hơn Ca 2.<br>"
        "<b>(2) Mục lục và thân bài ghi tên mục 14.7 khác nhau.</b> Mục lục ghi “14.7 Example”, thân bài "
        "ghi “14.7 Review Example”. Bản dịch theo thân bài.<br>"
        "<b>(3) Sách dùng lẫn hai tên cho cùng một khoản chi.</b> Bảng 14-1 gọi là “online testing” (thử "
        "nghiệm định kỳ), Bảng 14-3 và 14-4 gọi là “manual testing” (thử nghiệm thủ công). Đây là cùng một "
        "khoản: thử nghiệm do người thực hiện để phát hiện hỏng nguy hiểm không tự chẩn đoán được. Bản "
        "dịch giữ “thử nghiệm định kỳ” ở phần văn và “thử nghiệm thủ công” ở hai bảng chi phí, để khớp với "
        "số liệu của bản gốc.<br>"
        "<b>Ngoài ra, một điểm về cách đọc hình:</b> Hình 14-2 và 14-3 vẽ cả hai cảm biến cùng đi vào một "
        "khối logic, trong khi mô hình PFD ở mục 14.7 tính cho từng chức năng riêng lẻ (một cảm biến, một "
        "bộ khuếch đại ngưỡng, ba rơ-le và cả hai van). Hai hình ấy là sơ đồ khối, không phải sơ đồ đấu "
        "dây: chúng cho biết mức dự phòng của từng phần, không cho biết điểm đấu nối thực tế."))

    b.append(refs([
        "Goble, W. M. <em>Control Systems Safety Evaluation and Reliability</em>. Ấn bản thứ hai. ISA, 1998.",
        "29 CFR Part 1910.119. <em>Process Safety Management of Highly Hazardous Chemicals</em>. U.S. "
        "Federal Register, 24 tháng 2 năm 1992.",
        "Belke, James C. <em>Recurring Causes of Recent Chemical Accidents</em>. U.S. Environmental "
        "Protection Agency — Chemical Emergency Preparedness and Prevention Office, 1997.",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(p("Every chapter of this book up to here has been about making a safety function work: "
               "specifying it, calculating its PFD, testing it, changing it safely. This chapter is about "
               "the conversation that happens before any of that — the one where somebody asks what the "
               "system is worth, and expects an answer in money."))
    b.append(p("The book's answer is more interesting than a cost-benefit table. It says a safety system "
               "has three separate claims on the money: it protects people, it protects the plant, and it "
               "avoids shutting the plant down when nothing is wrong. Only the first is easy to defend, and "
               "it is the one that most companies have already settled by policy. The argument that "
               "actually gets argued is the second and third."))

    b.append(h2("Four failure modes, four different arguments"))
    b.append(p("Section 14.2 splits the usual safe/dangerous pair into four modes, and the split is worth "
               "taking seriously because each mode attacks a different part of the business case. A "
               "dangerous undetected failure attacks the safety case and is invisible until somebody tests "
               "for it. A dangerous detected failure attacks availability: the function is gone until "
               "somebody repairs it, and the question becomes how long the plant can run without it. A "
               "degraded mode attacks nothing, which is exactly why redundancy sells. A nuisance trip "
               "attacks production directly and, through the bypasses it provokes, attacks safety "
               "indirectly."))
    b.append(p("That last mechanism is the one worth dwelling on. The chapter quotes 29 CFR 1910.119 making "
               "an argument that sounds almost heretical in a safety book: shutting down is itself "
               "dangerous, and keeping shutdowns to a minimum promotes safety. The regulation is right, and "
               "the practical consequence is that a safety system which trips too often gets bypassed. The "
               "bypass is the real failure mode, and it is caused by good reliability engineering done "
               "badly — or not done at all."))

    b.append(h2("Why the numbers are smaller than they look"))
    b.append(p("Example 1 is the chapter's most useful reality check. A million-dollar explosion, once "
               "every five hundred years, reduced by a factor of a hundred. The annual saving is $1,980. "
               "Discounted at six percent over twenty years, the entire justified expenditure is $22,710."))
    b.append(p("Twenty-two thousand dollars for a safety system that prevents a million-dollar explosion. "
               "That number surprises people, and the surprise is the lesson: a risk reduction factor of "
               "100 sounds enormous, but it is applied to an event that almost never happens, and then "
               "discounted over twenty years. The arithmetic is not arguing against safety systems. It is "
               "arguing that the financial case for a safety system is usually thin, and that pretending "
               "otherwise is how a justification gets written that nobody believes."))
    b.append(p("Which is why the chapter immediately notes what the example leaves out: operation and "
               "maintenance costs are assumed negligible. Put them back and the twenty-two thousand shrinks "
               "further. The honest conclusion is that most safety systems cannot be justified on equipment "
               "damage alone — and that this is a reason to justify them on the right grounds rather than "
               "to inflate the grounds that do not hold."))

    b.append(h2("The reliability argument is the strong one"))
    b.append(p("Example 2 makes the opposite point. Seventy thousand dollars to halve the spurious trip "
               "rate, against a ten-thousand-dollar annual benefit, borrowed at five percent over twenty "
               "years at $5,617 a year. That is a payback of about seven years and a clear yes."))
    b.append(p("The asymmetry is the whole chapter. Protecting equipment from a rare explosion is hard to "
               "justify because the event is rare. Avoiding a nuisance trip is easy to justify because the "
               "event is frequent, its cost is known from the production ledger, and the benefit arrives "
               "every year. Reliability spending pays back on a schedule a finance department recognises; "
               "safety spending pays back in events that never happen, which is a much harder line item to "
               "defend."))
    b.append(p("This is why the chapter insists that justification is usually the control systems "
               "engineer's job. The safety case was settled upstream by the SIL determination and the "
               "company's risk tolerance. What remains to argue is the increment above the SIL: the extra "
               "redundancy, the better diagnostics, the shorter test interval. Those are reliability "
               "purchases wearing safety clothing, and they need the reliability arithmetic."))

    b.append(h2("Lifecycle cost turns the argument around"))
    b.append(p("The two cases in section 14.7 are the same plant, the same hazards and the same SIL "
               "requirement, solved two ways. Case 1 is single transmitters and relay logic; Case 2 is "
               "triplicated 2oo3 transmitters and a fault-tolerant safety PLC. Both meet SIL 1. Case 1 has "
               "a PFD of 0.0165 and trips spuriously every three years. Case 2 has a PFD of 0.0100 and "
               "trips every five years."))
    b.append(p("Case 2 costs $38,000 more to buy and $74,160 less to own. The mechanism is worth spelling "
               "out because it is not obvious from the purchase order: the 2oo3 sensors and the safety PLC "
               "can be tested every three years instead of every six months, and that single change removes "
               "the largest annual cost line in Case 1 — $25,000 of manual testing. The redundancy did not "
               "just buy safety margin; it bought test interval, and test interval is where the money is."))
    b.append(p("There is a sting in the tail that the chapter states plainly and then moves past. The "
               "valves are single in both cases, and they dominate both the PFD and the spurious trip rate "
               "of Case 2. Doubling the sensor count and buying a fault-tolerant PLC reduced the PFD from "
               "0.0165 to 0.0100 — a factor of 1.65 — because 0.0100 of the 0.0100 is the valves. The "
               "expensive redundancy is propping up a number that the cheapest component in the loop "
               "controls."))

    b.append(h2("What a justification document should actually contain"))
    b.append(p("Reading sections 14.3 to 14.9 together, a defensible justification has four parts, and "
               "most real ones are missing at least two."))
    b.append(ol([
        "A statement of which risk receptor is being protected. Personnel risk is settled by policy; "
        "equipment, production and environmental risk are not, and lumping them together hides the fact "
        "that only some of them carry a financial case.",
        "The annual loss avoided, not the event loss avoided. A million-dollar event every five hundred "
        "years is two thousand dollars a year; presenting the million is how a weak case is made to look "
        "strong.",
        "The present value of that annual figure over the asset life, at a stated interest rate. Without "
        "discounting, twenty years of savings is overstated by roughly a factor of two at five percent.",
        "The cost side computed the same way — including the annual costs, not just the capital. A "
        "justification that compares a discounted benefit against an undiscounted capital cost is not a "
        "comparison.",
    ]))
    b.append(p("And one thing that is not on the list: a number for a human life. The chapter is explicit "
               "that companies avoid publishing or using such figures, and it does not supply one. That "
               "reticence is not evasion. A safety system justified by a body count is a safety system "
               "that will be re-justified downward the moment somebody finds a cheaper body count, and the "
               "regulatory and ethical floor exists precisely so that the calculation never has to be made."))

    b.append(h2("The sentence to remember"))
    b.append(p("Section 14.9 contains the observation that reorganises the whole chapter: for decades "
               "people optimised the logic box, and modelling shows the field devices dominate. In the "
               "worked example the logic system is 10 percent of the capital cost in Case 1 and 21 percent "
               "in Case 2, while the valves alone contribute 61 percent of the PFD in Case 1 and essentially all of it in Case 2. The place where "
               "money buys safety is not the place where money is usually spent."))
    b.append(p("That is also the answer to the question a project manager asks when handed a lifecycle "
               "cost analysis: why are we comparing twenty-year totals for a decision being made today? "
               "Because the decision being made today is which system to own for twenty years. The purchase "
               "order is the smallest part of it."))
    return "".join(b)
