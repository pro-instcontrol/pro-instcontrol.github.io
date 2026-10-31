# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 13, Managing Changes to a System
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis13fig as F

PAGES_SRC = 9
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>MOC (management of change)</em> — quản lý thay đổi: quy trình khởi tạo, ghi chép, xem "
            "xét, thực hiện và phê duyệt mọi thay đổi. · "
            "<em>Replacement in kind</em> — thay thế cùng loại. Với thiết bị an toàn, nghĩa là “like for "
            "like” — cùng kiểu, cùng đặc tính hỏng, chứ không chỉ cùng thông số điện. · "
            "<em>Cơ sở thiết kế an toàn ban đầu</em> — tập hợp giả định, ràng buộc và đặc điểm thiết kế "
            "mà người bảo trì phải biết để không vô tình xoá bỏ. · "
            "<em>Pha đầu tiên bị ảnh hưởng</em> — mốc quay lại của vòng đời sau mỗi thay đổi. · "
            "<em>PSAT</em> — thử nghiệm chấp nhận trước khởi động. · "
            "<em>Decommissioning</em> — ngừng đưa một hệ ra khỏi vận hành; cũng cần MOC.")
    return note(
        "<b>Key terms.</b> <em>MOC (management of change)</em> — the procedure that initiates, documents, "
        "reviews, implements and approves every change. · <em>Replacement in kind</em> — for safety "
        "equipment this means like for like: same failure modes and failure rate, not merely the same "
        "electrical ratings. · <em>Original safety design basis</em> — the assumptions, constraints and "
        "design features maintainers must know in order not to delete them by accident. · <em>First "
        "affected phase</em> — the point in the lifecycle to which every change returns. · <em>PSAT</em> — "
        "pre-startup acceptance testing. · <em>Decommissioning</em> — taking a system out of service, which "
        "also needs MOC.")


def body_vi():
    b = []
    b.append(lead(
        "“Thứ duy nhất không đổi trong bất kỳ tổ chức nào là sự thay đổi.” Chương này là về cái giá phải "
        "trả khi câu đó được áp vào một hệ an toàn mà không có ai đứng ra kiểm soát."))

    # ------------------------------------------------------------------ 13.1
    b.append(h2("13.1 Giới thiệu", "Introduction"))
    b.append(p("Việc thay đổi quá trình, hệ điều khiển, hệ an toàn, thiết bị và quy trình là không thể "
               "tránh khỏi. Sửa đổi là cần thiết vì nhiều lý do, trong đó có thay đổi công nghệ, yêu cầu "
               "chất lượng, hỏng hóc thiết bị hoặc vấn đề an toàn."))
    b.append(p("OSHA 29 CFR 1910.119 (“Quản lý an toàn quá trình đối với hoá chất có mức nguy hiểm cao”) "
               "yêu cầu người sử dụng lao động “xây dựng và thực hiện các quy trình bằng văn bản để quản lý "
               "thay đổi (trừ ‘thay thế cùng loại’) đối với hoá chất quá trình, công nghệ, thiết bị và quy "
               "trình; và đối với những thay đổi tại cơ sở có ảnh hưởng tới một quá trình thuộc diện quản "
               "lý” [Tài liệu 1]."))
    b.append(p("Tiểu mục 5.2.6.2.2 của ANSI/ISA-84.00.01-2004 quy định rằng “phải có các quy trình quản lý "
               "sửa đổi để khởi tạo, ghi chép, xem xét, thực hiện và phê duyệt mọi thay đổi đối với hệ "
               "thống an toàn, trừ trường hợp thay thế cùng loại (tức like for like)”."))
    b.append(p("Chương này tập trung vào quản lý thay đổi (MOC) trong mối liên hệ với hệ an toàn, có dẫn "
               "chiếu cụ thể tới các yêu cầu của OSHA và ANSI/ISA-84.00.01-2004. Các quy trình MOC là bắt "
               "buộc để bảo đảm mọi thay đổi được thực hiện một cách an toàn, nhất quán và được ghi chép "
               "đầy đủ."))

    # ------------------------------------------------------------------ 13.2
    b.append(h2("13.2 Vì sao phải quản lý thay đổi", "The Need for Managing Changes"))
    b.append(p("Những thay đổi thực hiện trên một quá trình, dù nhỏ đến đâu, đều có thể có những hệ quả an "
               "toàn nghiêm trọng. Hãy lấy một vụ tai nạn quá trình lớn — vụ nổ Flixborough ở Anh — làm ví "
               "dụ."))
    b.append(p("Tháng 6 năm 1974, một vụ nổ lớn xảy ra tại nhà máy Nypro ở Flixborough, và nó đã thay đổi "
               "tận gốc cách mọi ngành công nghiệp quản lý an toàn."))
    b.append(p("Nhà máy Nypro sản xuất một chất trung gian dùng để làm nylon. Phân xưởng bị nổ ô-xy hoá "
               "xyclohexan bằng không khí để tạo ra xyclohexanon và xyclohexanol. Quá trình gồm một dãy sáu "
               "bình phản ứng, mỗi bình chứa 20 tấn, và mỗi bình được nối một phần bằng một khớp mềm. Chất "
               "lỏng tràn từ bình này sang bình kế tiếp, không khí mới được thêm vào từng bình. Người ta "
               "phát hiện một vết nứt và rò rỉ trên một trong các bình, và bình ấy được tháo ra để sửa. Một "
               "đoạn ống nối tạm được lắp vào thay chỗ để duy trì sản xuất."))
    b.append(p("Không ai tham vấn một kỹ sư có đủ năng lực. Bản duy nhất mô tả thay đổi là một hình vẽ bằng "
               "phấn đúng tỉ lệ thật, tìm thấy trên nền xưởng. Hệ được thử áp một lần sau khi lắp; nhưng đó "
               "là thử bằng khí nén chứ không phải bằng thuỷ lực, và được thử tới 127 psig thay vì tới áp "
               "suất của van an toàn là 156 psig. Thiết kế ấy vi phạm các tiêu chuẩn và hướng dẫn của Anh."))
    b.append(p("Đoạn ống tạm làm việc bình thường trong 2 tháng cho tới khi có một đợt tăng áp nhẹ. Áp suất "
               "ấy thấp hơn áp suất van an toàn nhưng đủ làm đoạn ống tạm bị xoắn. Mô-men uốn đủ mạnh để "
               "xé rách khớp nối mềm và bắn đoạn ống tạm ra ngoài, để lại hai lỗ hở 28 inch."))
    b.append(p("Đám mây khí tạo thành, ước tính chứa 40 đến 50 tấn vật chất, gặp một nguồn đánh lửa trong "
               "nhà máy và bốc cháy. Vụ nổ tạo ra khiến 28 người chết và 36 người bị thương, và được ước "
               "tính tương đương 15 đến 45 tấn TNT. Nhà máy bị tàn phá, các toà nhà trong vòng 1/3 dặm bị "
               "phá huỷ, cửa kính vỡ tới 8 dặm, và tiếng nổ nghe thấy ở khoảng cách 30 dặm. Ngọn lửa từ "
               "đám cháy sau đó tiếp tục cháy trong 10 ngày, cản trở công tác cứu hộ tại hiện trường."))
    b.append(p("Bài học chính rút ra là mọi sửa đổi đều phải được thiết kế và xem xét bởi nhân sự có đủ "
               "năng lực. Những người lắp đoạn ống ấy không có kiến thức chuyên môn cần thiết. Như chuyên "
               "gia an toàn nổi tiếng thế giới Trevor Kletz đã nói: “họ không biết những gì họ không "
               "biết”."))
    b.append(p("Phải tuân thủ những quy trình quản lý thay đổi chặt chẽ để phân tích tác động của mọi thay "
               "đổi. Một thay đổi có vẻ không đáng kể với người này lại có thể thực sự đại diện cho một rủi "
               "ro đáng kể. Điều đó đòi hỏi ý kiến đóng góp của những người hiểu về thiết bị đo, về hệ điều "
               "khiển, về quá trình và về các hệ cơ khí/kết cấu. Điều quan trọng là phải để lại một dấu vết "
               "được ghi chép và có thể kiểm toán."))
    b.append(p("Để thực hiện bất kỳ thay đổi nào trên hệ, điều quan trọng là phải xem lại cơ sở thiết kế an "
               "toàn ban đầu. Các kỹ sư của cả phần cứng lẫn phần mềm cần nêu rõ các ràng buộc, giả định và "
               "đặc điểm thiết kế, để những người bảo trì không vô tình vi phạm các giả định hay xoá bỏ các "
               "đặc điểm an toàn. Những người ra quyết định cần biết vì sao ban đầu người ta đưa ra những "
               "quyết định liên quan đến an toàn, để họ không vô tình đảo ngược chúng [Tài liệu 3]. Nói "
               "cách khác, đừng thay đổi bất cứ thứ gì (ví dụ một quy trình, một thiết bị) trừ khi bạn biết "
               "vì sao ban đầu nó được lắp đặt hay thực hiện như vậy."))
    b.append(p("Những thay đổi có thể vô tình xoá bỏ các đặc điểm an toàn quan trọng hoặc làm giảm hiệu "
               "lực của các biện pháp kiểm soát. Nhiều vụ tai nạn được quy cho việc hệ không vận hành như "
               "dự định, bởi vì các thay đổi đã không được phân tích đầy đủ để xác định tác động của chúng "
               "lên hệ [Tài liệu 3]."))

    # ------------------------------------------------------------------ 13.3
    b.append(h2("13.3 Khi nào bắt buộc phải có MOC?", "When Is MOC Required?"))
    b.append(p("MOC áp dụng cho mọi thành phần của quá trình và của hệ an toàn, gồm thiết bị trường, phần "
               "logic, cơ cấu chấp hành cuối, báo động, giao diện người dùng và phần logic ứng dụng. Phải "
               "tuân thủ quy trình MOC cho những thay đổi đối với:"))
    b.append(ul([
        "quá trình;",
        "quy trình vận hành;",
        "quy định an toàn mới hoặc được sửa đổi;",
        "đặc tả yêu cầu an toàn;",
        "hệ an toàn;",
        "phần mềm hoặc phần sụn (nhúng, tiện ích, ứng dụng);",
        "việc sửa chữa các hỏng hóc mang tính hệ thống;",
        "thiết kế của hệ do suất hỏng cao hơn dự kiến;",
        "thiết kế của hệ do tần suất yêu cầu cao hơn dự kiến;",
        "quy trình thử nghiệm hoặc bảo trì.",
    ]))
    b.append(p("Một thay đổi về phần sụn là một sửa đổi đủ lớn về tiềm năng để phải tuân theo quy trình "
               "MOC. Các nhà sản xuất có khả năng sửa đổi và bổ sung chức năng cho thiết bị thông qua thay "
               "đổi phần mềm. Việc này có thể không làm thay đổi mã số catalô của thiết bị nhưng có thể sẽ "
               "làm thay đổi mức hiệu đính của thiết bị. Người dùng sẽ làm việc với nhà sản xuất để đánh "
               "giá xem thiết bị đã sửa đổi có dùng được trong hệ của mình hay không. Nếu thấy phù hợp, "
               "trước tiên họ có thể đưa nó vào một kênh của một hệ dự phòng, cho phép đối chiếu hoạt động "
               "của nó với một thiết bị đã được nhà máy chấp thuận trước đó. Khi đã tích luỹ đủ kinh nghiệm "
               "về hiệu năng của nó, họ có thể nâng nó lên trạng thái thay thế hoàn toàn."))

    # ------------------------------------------------------------------ 13.4
    b.append(h2("13.4 Khi nào không cần MOC?", "When Is MOC Not Required?"))
    b.append(p("Quy trình MOC thông thường không bắt buộc đối với:"))
    b.append(ul([
        "Những thay đổi được coi là “thay thế cùng loại”. “Thay thế cùng loại” không có cùng ý nghĩa đối "
        "với các thành phần của hệ an toàn như khi thay một động cơ điện. Khi thay một động cơ điện, có "
        "thể lắp động cơ của nhà sản xuất khác nếu công suất, điện áp, tần số, tốc độ và kích thước vỏ "
        "giống nhau. Tuy nhiên, để thay một thành phần của hệ an toàn — ví dụ một bộ biến đổi — thì suất "
        "hỏng và các chế độ hỏng của thiết bị mới cũng là những yếu tố then chốt, vì chúng ảnh hưởng trực "
        "tiếp tới hiệu năng của hệ. Với hệ an toàn, “thay thế cùng loại” phải là “like for like”, tức một "
        "phương án thay thế đã được chấp thuận trước và thoả mãn đặc tả ban đầu.",
        "Mọi thay đổi nằm trong phạm vi đặc tả yêu cầu an toàn.",
        "Việc sửa chữa thiết bị trở về trạng thái ban đầu sau khi hỏng.",
        "Việc hiệu chuẩn, xả hoặc đặt lại điểm không cho các thiết bị đo trường thuộc hệ an toàn.",
        "Thay đổi dải đo, thay đổi báo động hoặc thay đổi điểm cắt nằm trong điều kiện thiết kế hoặc "
        "điều kiện vận hành đã nêu trong đặc tả yêu cầu an toàn.",
        "Mọi thay đổi đã được một quy trình nội bộ khác của công ty bao trùm, trong đó nêu rõ rằng không "
        "cần áp dụng MOC cho thay đổi cụ thể ấy.",
    ]))

    # ------------------------------------------------------------------ 13.5
    b.append(h2("13.5 Yêu cầu của ANSI/ISA-84.00.01-2004",
                "ANSI/ISA-84.00.01-2004 Requirements"))
    b.append(p("Điều 17 của tiêu chuẩn đề cập đến việc sửa đổi hệ an toàn. Mục tiêu là bảo đảm mọi sửa đổi "
               "trên bất kỳ hệ thống an toàn nào đều được hoạch định, xem xét và phê duyệt đúng đắn trước "
               "khi thực hiện, và bảo đảm mức toàn vẹn an toàn yêu cầu của hệ được duy trì."))
    b.append(p("Trước khi tiến hành bất kỳ sửa đổi nào, phải có sẵn các quy trình cấp phép và kiểm soát "
               "thay đổi. Quy trình phải bao gồm một cách rõ ràng để nhận diện và yêu cầu công việc cần "
               "làm, cùng những mối nguy có thể bị ảnh hưởng. Phải thực hiện một phân tích để xác định tác "
               "động mà sửa đổi đề xuất sẽ có lên an toàn chức năng. Khi phân tích cho thấy sửa đổi đề xuất "
               "sẽ ảnh hưởng tới an toàn, phải quay lại pha đầu tiên của vòng đời an toàn mà sửa đổi ấy "
               "chạm tới. Không được bắt đầu sửa đổi khi chưa có phê duyệt đúng thẩm quyền."))
    b.append(p("Những điểm khác cần được giải quyết trước khi có bất kỳ thay đổi nào đối với hệ an toàn là:"))
    b.append(ul([
        "cơ sở kỹ thuật của thay đổi đề xuất;",
        "tác động của thay đổi lên an toàn và sức khoẻ;",
        "các sửa đổi cần thiết đối với quy trình vận hành;",
        "khoảng thời gian cần thiết cho thay đổi;",
        "các yêu cầu về thẩm quyền phê duyệt cho thay đổi đề xuất;",
        "dung lượng bộ nhớ còn trống của bộ điều khiển;",
        "ảnh hưởng lên thời gian đáp ứng;",
        "thay đổi trực tuyến hay ngoại tuyến, và những rủi ro đi kèm.",
    ]))
    b.append(p("Việc xem xét thay đổi phải bảo đảm rằng mức toàn vẹn an toàn yêu cầu đã được đánh giá lại, "
               "và rằng nhân sự thuộc các chuyên ngành phù hợp đã tham gia vào quá trình xem xét."))
    b.append(p("Mọi thay đổi đối với một hệ an toàn đều phải khởi động việc quay về pha thích hợp của vòng "
               "đời an toàn (tức pha đầu tiên bị sửa đổi ảnh hưởng). Sau đó phải thực hiện toàn bộ các pha "
               "tiếp theo của vòng đời an toàn, kể cả việc kiểm chứng phù hợp rằng thay đổi đã được thực "
               "hiện đúng và đã được ghi chép. Việc thực hiện mọi thay đổi (kể cả phần mềm ứng dụng) phải "
               "tuân thủ các quy trình thiết kế đã thiết lập trước đó."))
    b.append(p("Khi một hệ cắt được vô hiệu hoá, cần có quy trình quản lý thay đổi để bảo đảm không có hệ "
               "thống hay quá trình nào khác bị ảnh hưởng. Vì thế mọi hoạt động ngừng đưa hệ ra khỏi vận "
               "hành đều cần có quy trình quản lý thay đổi."))
    b.append(p("Phải duy trì thông tin phù hợp cho mọi thay đổi của hệ an toàn. Thông tin ấy tối thiểu phải "
               "gồm:"))
    b.append(ul([
        "mô tả sửa đổi hoặc thay đổi;",
        "lý do của thay đổi;",
        "những mối nguy đã được nhận diện có thể bị ảnh hưởng;",
        "phân tích tác động của hoạt động sửa đổi lên SIS;",
        "mọi phê duyệt cần có cho các thay đổi;",
        "các phép thử dùng để kiểm chứng rằng thay đổi đã được thực hiện đúng và SIS hoạt động như yêu "
        "cầu;",
        "lịch sử cấu hình phù hợp;",
        "các phép thử dùng để kiểm chứng rằng thay đổi không gây ảnh hưởng xấu tới những phần của SIS "
        "không bị sửa đổi.",
    ]))
    b.append(p("Việc sửa đổi phải do nhân sự có đủ năng lực và đã được đào tạo đúng mức thực hiện. Mọi nhân "
               "sự bị ảnh hưởng và có liên quan phải được thông báo về các thay đổi và được đào tạo về "
               "thay đổi đó."))
    b.append(p("Điều 12 của tiêu chuẩn đề cập đến phần mềm, kể cả các thay đổi. Quy trình MOC cũng bắt buộc "
               "đối với những thay đổi thực hiện trên phần mềm. Tương tự như thay đổi phần cứng, mục tiêu "
               "của MOC liên quan đến phần mềm là bảo đảm phần mềm tiếp tục đáp ứng đặc tả yêu cầu an toàn "
               "của phần mềm. Việc sửa đổi phần mềm phải được thực hiện theo các yêu cầu bổ sung sau:"))
    b.append(ul([
        "Trước khi sửa đổi, phải thực hiện một phân tích về ảnh hưởng của sửa đổi lên an toàn của quá "
        "trình và lên trạng thái thiết kế của phần mềm, và dùng phân tích ấy để định hướng việc sửa đổi.",
        "Phải có sẵn kế hoạch an toàn cho việc sửa đổi và cho việc kiểm chứng lại.",
        "Việc sửa đổi và kiểm chứng lại phải được thực hiện theo đúng kế hoạch.",
        "Phải xem xét việc hoạch định các điều kiện cần thiết trong lúc sửa đổi và thử nghiệm.",
        "Mọi tài liệu bị ảnh hưởng bởi sửa đổi phải được cập nhật.",
        "Phải có sẵn chi tiết của mọi hoạt động sửa đổi SIS (ví dụ một sổ nhật ký).",
    ]))
    b.append(p("Nên đối xử với các thay đổi phần mềm một cách nghiêm túc ngang với các thay đổi của nhà máy "
               "hay quá trình, và áp dụng biện pháp kiểm soát tương tự. Mọi thay đổi đối với phần mềm đều "
               "phải yêu cầu thử lại toàn bộ phần logic liên quan đến thay đổi ấy."))
    b.append(p("Một người dùng ngoài khơi có một hệ an toàn dựa trên PLC. Hệ này có một số chức năng logic "
               "mà khi tác động sẽ gây dừng toàn giàn, như trên Hình 13-1."))
    b.append(fig(1, F.fig_13_1(), "vi"))
    b.append(p("Có một lúc họ cần thêm một chức năng logic mới, cũng sẽ gây dừng toàn giàn. Họ giao việc "
               "lập trình cho một lập trình viên tương đối ít kinh nghiệm. Dòng cuối cùng của logic thang "
               "có rất nhiều tiếp điểm mà khi tác động sẽ gây dừng toàn bộ (cuộn dây cuối). Trong trường "
               "hợp cụ thể này, không còn chỗ trống cho bất kỳ tiếp điểm mới nào trên dòng ấy. “Không vấn "
               "đề!” — người kỹ sư nghĩ — “tôi chỉ cần thêm một dòng mới và lặp lại cuộn dây ở dòng thứ "
               "hai.” Logic thu được như trên Hình 13-2."))
    b.append(fig(2, F.fig_13_2(), "vi"))
    b.append(p("Người dùng đã thử phần mềm. Đương nhiên, họ chỉ thử phần vừa sửa, và nó hoạt động đúng như "
               "mong muốn. Họ không thử bất kỳ phần logic gốc nào. Bất kỳ ai hiểu logic thang đều sẽ thấy "
               "xung đột."))
    b.append(p("PLC không ghi thẳng ra đầu ra trong lúc quét logic. Các biến được giữ trong bộ nhớ suốt "
               "vòng quét logic, và sau đó mới được ghi ra đầu ra. Ghi vào một đầu ra ở nhiều hơn một chỗ "
               "trong chương trình đơn giản chỉ là một cách lập trình tồi. Một dòng logic có thể làm mất "
               "điện một đầu ra, trong khi một dòng khác lại cấp điện lại cho nó. Tất cả những điều ấy "
               "diễn ra trong bộ nhớ trước khi thật sự ghi ra bất kỳ đầu ra nào. Nói cách khác, trong logic "
               "thang, dòng cuối cùng thắng. (Trong trường hợp này, dòng gốc có thể ra lệnh cắt, nhưng dòng "
               "cuối sẽ đặt lại trạng thái của đầu ra trong bộ nhớ về “bình thường”. Đầu ra sẽ không mất "
               "điện như dự định.) Vấn đề chỉ bộc lộ khi một thanh tra chính phủ tình cờ đến thăm giàn. Ông "
               "ấy yêu cầu được xem một phép thử dừng giàn. Các nhân viên vận hành sững sờ khi hệ không "
               "hoạt động như dự định. “Nhưng chúng tôi đã thử nó rồi mà!” Họ thử một chức năng cắt khác. "
               "Cũng không chạy. Vị thanh tra cho dừng giàn, và chủ sở hữu phải đối mặt với một khoản tiền "
               "phạt đáng kể."))

    # ------------------------------------------------------------------ 13.6
    b.append(h2("13.6 Quy trình MOC", "MOC Procedure"))
    b.append(p("Trước khi đi vào từng hạng mục, Hình 13-3 tóm tắt điều mà cả quy trình phải bảo "
               "đảm, và cũng là điều dễ bị coi nhẹ nhất: một thay đổi không phải là một lần sửa, "
               "mà là một lần quay lại vòng đời."))
    b.append(fig(3, F.fig_13_3(), "vi"))
    b.append(p("Quy trình quản lý thay đổi nên bao gồm những nội dung sau:"))
    b.append(table(
        ["Hạng mục", "Ghi chú"],
        [["Cách khởi tạo hoặc yêu cầu thay đổi",
          "Phải xây dựng các mẫu phiếu phê duyệt thay đổi và đưa vào quy trình MOC. Cơ sở kỹ thuật của "
          "thay đổi nên được ghi trong phiếu. Phiếu này thường dùng chung cho mọi thay đổi tại cơ sở. "
          "Phải bao gồm cả thay đổi tạm thời lẫn thay đổi vĩnh viễn."],
         ["Phê duyệt yêu cầu thay đổi", "Phải thiết lập quy trình cấp phép/phê duyệt cho thay đổi."],
         ["Trách nhiệm",
          "Xác định (các) cá nhân chịu trách nhiệm: phê duyệt yêu cầu thay đổi; nhận diện sự cần thiết "
          "phải áp dụng quy trình MOC; và bảo đảm quy trình sẽ được tuân thủ."],
         ["Đánh giá mối nguy",
          "Những người tham gia đánh giá mối nguy có thể không phải là nhóm đã xem xét ban đầu. Cần xác "
          "định rõ những người này. Thường có nhiều nhân sự vận hành và bảo trì hơn tham gia đánh giá. "
          "Các kỹ thuật cần dùng cho việc đánh giá phải được xác định dựa trên bản chất, quy mô và tác "
          "động của thay đổi."],
         ["Tài liệu", "Tài liệu nào phải được cập nhật? Việc cập nhật tài liệu sẽ được thực hiện như thế "
                      "nào?"],
         ["Xem xét và ký duyệt", "Ai sẽ xem xét tài liệu đã cập nhật và ký duyệt?"],
         ["Đào tạo", "Mọi người bị ảnh hưởng bởi thay đổi đều cần được thông báo và đào tạo."],
         ["Xây lắp", "Các thay đổi sẽ được thực hiện tại hiện trường khi nào và như thế nào?"],
         ["Kiểm tra chạy thử",
          "Nên có một tổ riêng chịu trách nhiệm kiểm tra chạy thử, dựa trên những quy trình được ghi chép "
          "đầy đủ."],
         ["Khởi động", "Các thay đổi phải được bộ phận vận hành phê duyệt trước khi khởi động."],
         ["Hoàn tất cuối cùng",
          "Phải ký duyệt và phát hành một báo cáo cuối cùng sau khi khởi động thành công."],
         ["Kiểm toán và kiểm chứng",
          "Phải có một hệ thống kiểm toán và kiểm chứng để xác nhận rằng các quy trình đang được tuân "
          "thủ."]],
        caption="Bảng 13-1. Mười hai hạng mục của một quy trình MOC. Chú ý hai dòng cuối: một quy trình "
                "không có kiểm toán thì không ai biết nó có được tuân thủ hay không, và một quy trình "
                "không có báo cáo hoàn tất thì không ai biết thay đổi đã kết thúc hay chưa.",
                cls="tbl moc"))

    # ------------------------------------------------------------------ 13.7
    b.append(h2("13.7 Tài liệu của MOC", "MOC Documentation"))
    b.append(p("Những tài liệu liên quan sau phải được cập nhật:"))
    b.append(ul([
        "phần logic ứng dụng;",
        "tài liệu thiết kế;",
        "các quy trình chạy thử và thử nghiệm chấp nhận trước khởi động (PSAT);",
        "các quy trình vận hành;",
        "các quy trình bảo trì;",
        "các quy trình thử nghiệm;",
        "các đặc tả yêu cầu an toàn.",
    ]))
    b.append(p("Duy trì tài liệu cập nhật và chính xác cho hệ an toàn là điều then chốt. Bản thân tài liệu "
               "không chính xác đã có thể tạo ra những mối nguy tiềm ẩn. Một số yêu cầu tài liệu then chốt "
               "liên quan đến quản lý thay đổi là:"))
    b.append(ul([
        "Mọi thay đổi đối với quy trình vận hành, thông tin an toàn quá trình và tài liệu SIS (kể cả phần "
        "mềm) phải được ghi nhận trước khi khởi động và phải được cập nhật cho tương ứng.",
        "Tài liệu phải được bảo vệ phù hợp để chống lại việc sửa đổi, phá huỷ hoặc thất lạc trái phép.",
        "Mọi tài liệu SIS phải được sửa đổi, tu chỉnh, xem xét và phê duyệt, và phải nằm dưới sự kiểm soát "
        "của một quy trình kiểm soát tài liệu phù hợp.",
    ]))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Việc thay đổi quá trình, hệ điều khiển, hệ an toàn, thiết bị và quy trình là không thể tránh "
               "khỏi. Sửa đổi là cần thiết vì nhiều lý do, trong đó có thay đổi công nghệ, yêu cầu chất "
               "lượng, hỏng hóc thiết bị hoặc vấn đề an toàn. Các quy định và tiêu chuẩn yêu cầu phải tuân "
               "thủ quy trình quản lý thay đổi đối với mọi thay đổi nằm ngoài đặc tả yêu cầu an toàn. Quy "
               "trình phải bảo đảm rằng các thay đổi:"))
    b.append(ul([
        "được nêu rõ và được thiết kế bởi những cá nhân có đủ năng lực;",
        "được một nhóm phù hợp xem xét, nhóm này có khả năng đánh giá cơ sở kỹ thuật của thay đổi và nhận "
        "diện tác động của nó;",
        "được kiểm tra và thử đầy đủ trước khi đưa hệ trở lại vận hành;",
        "được ghi chép đầy đủ;",
        "được thông báo tới những nhân viên bị ảnh hưởng để họ được thông tin và đào tạo thoả đáng.",
    ]))

    b.append(note(
        "<b>Ba điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Tiêu đề mục 13.5 khác nhau giữa mục lục và thân bài.</b> Mục lục ghi “13.5 Considerations” "
        "(Những điểm cần xét), còn tiêu đề trong thân bài là “13.5 ANSI/ISA-84.00.01-2004 Requirements”. "
        "Bản dịch theo thân bài, vì đó mới là nội dung thực sự của mục: tám điểm cần giải quyết trước khi "
        "thay đổi, tám thông tin phải lưu giữ, và sáu yêu cầu bổ sung cho phần mềm — tất cả đều dẫn ra từ "
        "tiêu chuẩn.<br>"
        "<b>(2) Bảng MOC mười hai dòng bị chèn đôi trong bản gốc.</b> Trong bản in, bảng của mục 13.6 bị "
        "cắt làm hai: dòng đầu (“Cách khởi tạo hoặc yêu cầu thay đổi”) nằm ở trang 238, rồi tiêu đề mục "
        "13.7 và danh sách tài liệu chen vào giữa, và mười một dòng còn lại mới xuất hiện ở trang 239. Bản "
        "dịch gom đủ mười hai dòng vào Bảng 13-1 đặt trong mục 13.6, vì bảng này rõ ràng thuộc về mục "
        "ấy.<br>"
        "<b>(3) Hình 13-3 là hình bổ sung.</b> Yêu cầu “quay về pha đầu tiên bị ảnh hưởng rồi chạy lại mọi "
        "pha sau đó” chỉ được nêu bằng lời trong mục 13.5. Bản dịch vẽ thêm sơ đồ, vì đây là yêu cầu dễ bị "
        "coi nhẹ nhất trong cả chương: thêm một tiếp điểm vào logic trông như việc của mười phút, cho tới "
        "khi người ta nhớ ra nó là một thay đổi thiết kế."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "29 CFR Part 1910.119. <em>Process Safety Management of Highly Hazardous Chemicals</em>. U.S. "
        "Federal Register, 24/02/1992.",
        "ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi). <em>Functional Safety: Safety "
        "Instrumented Systems for the Process Industry Sector</em>.",
        "Leveson, Nancy G. <em>Safeware — System Safety and Computers</em>. Addison-Wesley, 1995.",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "The only constant in any organisation is change. This chapter is about what that sentence costs "
        "when it is applied to a safety system and nobody is standing at the gate."))

    b.append(h2("Flixborough is not a story about a pipe"))
    b.append(p("Section 13.2 spends a page on a temporary pipe, and it is worth reading slowly, because "
               "every detail is a decision that a procedure would have caught. A reactor is removed for "
               "repair. A bypass link is installed to keep production running. No qualified engineer is "
               "consulted. The only drawing of the change is a full-scale chalk outline on the workshop "
               "floor. The assembly is pressure-tested once — pneumatically rather than hydraulically, and "
               "to 127 psig rather than the 156 psig of the relief valve."))
    b.append(p("Twenty-eight people died two months later. The pipe held until a pressure transient below "
               "the relief valve setting twisted it, tore the flexible connection and left two 28-inch "
               "openings. Between forty and fifty tonnes of cyclohexane found an ignition source."))
    b.append(p("The lesson the chapter draws is Trevor Kletz's line: they did not know what they did not "
               "know. That is not a comment about intelligence; it is a comment about scope. The people "
               "installing the pipe knew how to install a pipe. They did not know that the flexible "
               "bellows had a pressure rating, that the design pressure came from the relief valve, that a "
               "pneumatic test stores far more energy than a hydraulic one, or that a temporary modification "
               "needs the same review as a permanent one. Nobody in the loop was responsible for knowing "
               "any of it."))

    b.append(h2("Replacement in kind is a phrase that has killed people"))
    b.append(p("Section 13.4 contains the most useful paragraph in the chapter, and it is the one most often "
               "skimmed. For an electric motor, replacement in kind means same power, voltage, frequency, "
               "speed and frame size — interchangeability is a physical property, and any motor that fits "
               "will do. For a transmitter it is not. Two transmitters with identical ranges, identical "
               "outputs and identical mounting can have failure rates that differ by a factor of five, and "
               "different proportions of detected versus undetected dangerous failures."))
    b.append(p("That difference goes straight into the PFD calculation that justified the SIL. A swap that "
               "looks like a like-for-like replacement on the datasheet can quietly move the loop out of "
               "its target integrity level, and nothing on the plant will look any different. This is why "
               "the chapter insists on \"like for like\" and on pre-approved replacements rather than "
               "interchangeability."))

    b.append(h2("The last line wins"))
    b.append(p("The offshore anecdote in section 13.5 is the best illustration in the book of why testing "
               "the revision is not testing the system. A shutdown coil already sat at the end of a rung "
               "that had no room left. The programmer added a second rung and repeated the coil, which is "
               "exactly what you would do if you were thinking of the diagram as a drawing rather than as "
               "an execution order."))
    b.append(fig(1, F.fig_13_1(), "en"))
    b.append(p("Ladder logic does not write to the output during the scan. Values accumulate in memory and "
               "are written at the end, so the later rung overwrites the earlier one: the original rung "
               "calls for a shutdown, the new rung resets the bit to normal, and the valve never moves. The "
               "revision worked exactly as designed. The original logic was never re-tested, so nobody "
               "found out until a government inspector asked for a demonstration."))
    b.append(fig(2, F.fig_13_2(), "en"))
    b.append(p("Two general rules come out of it, and both are cheap. Never write to the same output in more "
               "than one place — if you need a second condition, put it in series on the same rung or use "
               "an intermediate bit. And when you change logic, re-test the whole logic, not the diff. The "
               "second rule costs an afternoon; the first one would have cost ten minutes."))

    b.append(h2("A change to software is a change to design"))
    b.append(p("Section 13.5 applies the lifecycle rule to software without softening it: a modification "
               "returns you to the first affected phase, and every later phase must be re-run, including "
               "re-verification and documentation. That is inconvenient, because software changes feel "
               "like edits rather than engineering. The programmer in the anecdote made a ten-minute "
               "change and treated it as one."))
    b.append(fig(3, F.fig_13_3(), "en"))
    b.append(p("The standard's six software requirements are worth reading as a checklist rather than as "
               "prose, because each one maps to a failure mode: analyse the effect before you modify; plan "
               "the modification and the re-verification; follow the plan; plan the conditions during "
               "modification and testing; update every affected document; keep a log. Skip the first and "
               "you change something whose purpose you did not understand. Skip the second and you test "
               "what you remember rather than what you specified."))

    b.append(p("Here is the twelve-item table the standard lays out for an MOC procedure, in English, "
               "because the list is the part of this chapter a plant actually implements:"))
    b.append(table(
        ["Item", "Notes"],
        [["How a change is initiated or requested",
          "Approval forms must be built and put into the MOC procedure. The technical basis for the change "
          "should be recorded on the form. The form is usually shared across every change on the site. It "
          "must cover both temporary and permanent changes."],
         ["Approval of the change request",
          "An authorisation and approval procedure must be established for the change."],
         ["Responsibilities",
          "Identify the individual(s) responsible for approving the change request, for recognising that "
          "the MOC procedure must be applied, and for ensuring the procedure is followed."],
         ["Hazard assessment",
          "The people taking part in the hazard assessment may not be the group that reviewed the change "
          "originally, and must be identified. More operations and maintenance staff usually take part than "
          "in the original review. The techniques used must be chosen from the nature, size and effect of "
          "the change."],
         ["Documentation",
          "Which documents must be updated, and how will the update be carried out?"],
         ["Review and sign-off",
          "Who reviews the updated documents and signs them off?"],
         ["Training",
          "Everyone affected by the change must be informed and trained."],
         ["Construction",
          "When and how will the change be implemented in the field?"],
         ["Checkout",
          "A separate crew should be responsible for checkout, working from fully documented procedures."],
         ["Startup",
          "The change must be approved by operations before startup."],
         ["Final completion",
          "A final report must be signed off and issued after a successful startup."],
         ["Audit and verification",
          "An audit and verification system must exist to confirm that the procedures are being followed."]],
        caption="Table 13-1. The twelve items of an MOC procedure. The last two rows are the ones most "
                "often dropped: a procedure with no audit leaves nobody knowing whether it is followed, "
                "and a procedure with no completion report leaves nobody knowing whether the change ended.",
                cls="tbl moc"))

    b.append(h2("MOC is a gate, not a form"))
    b.append(p("The twelve-row table in 13.6 is often implemented as a form to be filled in, and that is "
               "where it stops working. Read the rows as a sequence of gates instead. Hazard assessment is "
               "a gate: somebody qualified decides whether the change touches a protected function. Check "
               "out is a gate, and the chapter is specific that it should be a separate crew — the people "
               "who installed the change are the worst possible people to confirm that it works. Startup is "
               "a gate: operations approves before the change goes live."))
    b.append(p("The last two rows are the ones that distinguish a procedure from a ritual. Auditing and "
               "verification asks whether the procedure is actually being followed, which is a question "
               "nobody asks if the form is the deliverable. Final completion asks for a signed report, "
               "which is the only artefact that tells a future reader that the change is finished rather "
               "than abandoned halfway."))
    b.append(p("And the reason all of this matters is in section 13.2: decision makers need to know why the "
               "safety features were put there originally, so that they do not inadvertently undo them. A "
               "safety system is a set of arguments made concrete. A change is an edit to one of those "
               "arguments, and an argument edited by someone who never read it is not an argument any "
               "more."))
    return "".join(b)
