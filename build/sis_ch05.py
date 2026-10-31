# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 5, Developing the Safety Requirement
Specifications (Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 14
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>SRS (đặc tả yêu cầu an toàn)</em> — bộ tài liệu quy định hệ phải làm gì và làm tốt tới "
            "đâu. · "
            "<em>Đặc tả yêu cầu chức năng</em> — logic: đầu vào nào dẫn tới đầu ra nào. · "
            "<em>Đặc tả yêu cầu toàn vẹn</em> — hiệu năng: chức năng đó phải đáng tin tới mức nào. · "
            "<em>Lỗi hệ thống (systematic failure)</em> — lỗi do thiết kế hay quy trình; không định lượng "
            "được, chỉ kiểm soát được bằng quy trình. · "
            "<em>Sơ đồ nguyên nhân – kết quả</em> — bảng ma trận nêu rõ mỗi đầu vào tác động lên những đầu "
            "ra nào. · "
            "<em>Quản lý thay đổi (MOC)</em> — quy trình bắt buộc trước khi sửa bất cứ thứ gì đã được phê "
            "duyệt.")
    return note(
        "<b>Key terms.</b> <em>SRS</em> — the safety requirement specification: what the system must do, "
        "and how well. · <em>Functional requirement</em> — the logic: which input drives which output. · "
        "<em>Integrity requirement</em> — the performance: how reliably that function must work. · "
        "<em>Systematic failure</em> — a design or process error; not quantifiable, controlled only by "
        "procedure. · <em>Cause and effect diagram</em> — the matrix showing which input acts on which "
        "outputs. · <em>Management of change</em> — the procedure that must precede any edit to an "
        "approved document.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Nếu chương 3 trả lời “vì sao phải là một hệ riêng”, chương này trả lời “hệ đó phải được viết ra "
        "thành giấy tờ như thế nào”. Câu trả lời có một con số đáng nhớ đứng sau: 44 % tai nạn do hệ điều "
        "khiển và hệ an toàn gây ra là do đặc tả sai hoặc thiếu — không phải do thiết bị hỏng. Nghĩa là "
        "phần lớn lỗi đã được viết vào hệ từ trước khi có ai lắp bất cứ thứ gì."))

    # ---------------------------------------------------------------- 5.1
    b.append(h2("5.1 Giới thiệu", "Introduction"))
    b.append(p("Khi đã xác định được nhu cầu về một hệ thống đo lường an toàn (SIS) và đã thiết lập được mức "
               "toàn vẹn an toàn (SIL) mục tiêu cho từng chức năng an toàn đo lường (SIF), bước tiếp theo là "
               "xây dựng <b>đặc tả yêu cầu an toàn</b> (SRS). SRS có thể là một tài liệu duy nhất hoặc một "
               "bộ tài liệu. SRS liệt kê các yêu cầu cho mọi chức năng mà hệ phải thực hiện, và cũng phải "
               "bao gồm các yêu cầu đối với phần mềm ứng dụng."))
    b.append(p("SRS gồm hai phần chính:"))
    b.append(ol([
        "Đặc tả yêu cầu chức năng;",
        "Đặc tả yêu cầu toàn vẹn.",
    ]))
    b.append(p("Yêu cầu chức năng mô tả <em>logic</em> của hệ — nói cách khác, nó định nghĩa mỗi chức năng an "
               "toàn phải làm gì. Ví dụ: áp suất thấp trong bình A sẽ làm van B đóng. Yêu cầu toàn vẹn mô "
               "tả <em>hiệu năng</em> cần có cho mỗi chức năng — nói cách khác, nó định nghĩa năng lực, hay "
               "mức độ tốt mà mỗi chức năng an toàn phải đạt. Ví dụ: xác suất (hay khả năng) van B đóng khi "
               "áp suất bình A thấp phải lớn hơn 99 %. Trong phần còn lại của chương này, khi dùng từ “đặc "
               "tả” thì muốn nói tới cả đặc tả yêu cầu chức năng lẫn đặc tả yêu cầu toàn vẹn."))
    b.append(p("Tốt nhất là thiết kế nhà máy an toàn vốn có — nơi mối nguy thậm chí không tồn tại. Đáng tiếc "
               "điều đó không phải lúc nào cũng làm được. Có những lúc cách duy nhất để ngăn một mối nguy là "
               "thêm thiết bị đo để giám sát điều kiện quá trình và vận hành thiết bị để thực hiện các hành "
               "động cần thiết. Việc quyết định giám sát tham số quá trình nào, hành động an toàn là gì, và "
               "hệ cần hoạt động tốt tới đâu — tất cả đều được phản ánh trong đặc tả chức năng và đặc tả "
               "toàn vẹn."))
    b.append(p("Chương 2 đã nêu: HSE Anh đã xem xét 34 vụ tai nạn là hậu quả trực tiếp của lỗi hệ điều khiển "
               "và hệ an toàn trong nhiều ngành khác nhau. Kết quả của họ cho thấy <b>44 %</b> tai nạn là do "
               "đặc tả sai (cả đặc tả chức năng lẫn đặc tả toàn vẹn). Tỉ lệ cao thứ hai (20 %) là do những "
               "thay đổi được thực hiện <em>sau khi đã chạy thử nghiệm thu</em>. Không thể nói quá tầm quan "
               "trọng của việc bảo đảm đặc tả hệ là đúng."))
    b.append(p("Đặc tả tồi sẽ dẫn tới <b>lỗi hệ thống</b> (lỗi thiết kế). Nói cách khác, hệ có thể làm đúng "
               "cái mà nó được thiết kế để làm, nhưng hành động đó lại là sai. Lỗi hệ thống không mang tính "
               "ngẫu nhiên và thường xảy ra trong cùng một điều kiện. Những lỗi này không thể định lượng "
               "thỏa đáng và nói chung được kiểm soát bằng cách bảo đảm mọi hoạt động trong vòng đời đều "
               "được tuân thủ."))
    b.append(p("Chương này nhận diện một số vấn đề liên quan tới việc xây dựng đặc tả, xem lại các yêu cầu "
               "của ANSI/ISA-84.00.01-2004 (IEC 61511 Mod), và nêu ví dụ về bộ tài liệu điển hình cần được "
               "xây dựng."))

    # ---------------------------------------------------------------- 5.2
    b.append(h2("5.2 Vì sao 44 % tai nạn do đặc tả sai?",
                "Why Are 44 % of Accidents Caused by Incorrect Specifications?"))
    b.append(p("Để hiểu vì sao phần lớn tai nạn lại do đặc tả sai, cần tập trung vào các <em>hệ thống và quy "
               "trình</em> dùng để tạo ra đặc tả. Theo mô hình vòng đời đã nêu ở chương 2, những hoạt động "
               "sau phải diễn ra <em>trước khi</em> chuẩn bị đặc tả:"))
    b.append(ol([
        "Thiết kế khái niệm quá trình;",
        "Phân tích mối nguy và đánh giá rủi ro;",
        "Áp dụng các lớp không phải SIS;",
        "Xác định SIL nếu cần một SIF.",
    ]))
    b.append(p("Bốn bước này tạo thành nền móng của một đặc tả đúng. Vì thế các quy trình dùng để hoàn thành "
               "bốn bước này trong một tổ chức phải hiệu quả và thỏa đáng. Nếu quy trình không tồn tại hoặc "
               "không thỏa đáng thì dù có bỏ bao nhiêu thời gian và công sức để xây dựng đặc tả hệ, cơ sở "
               "thiết kế nền tảng của hệ vẫn có thể sai."))
    b.append(p("Cuốn sách này không nhằm định nghĩa quy trình thiết kế quá trình hay kỹ thuật phân tích mối "
               "nguy. Có nhiều tài liệu về hai chủ đề đó. Nhưng cần nói rõ một điều: việc nhận diện và đánh "
               "giá mối nguy <b>không</b> phải là thứ làm cho một quá trình hay hệ trở nên an toàn. Chính "
               "thông tin thu được từ phân tích mối nguy — và quan trọng hơn, chính các hành động được thực "
               "hiện — mới quyết định an toàn của hệ. Chỉ thực hiện một HAZOP thì không làm nhà máy của bạn "
               "an toàn hơn chút nào; suy cho cùng, nghiên cứu đó chỉ tạo ra một báo cáo, một tờ giấy. Làm "
               "theo các khuyến nghị của nó mới là thứ làm mọi thứ an toàn hơn."))
    b.append(p("Ngoài các vấn đề về hệ thống và quy trình vừa nêu, dưới đây là các lý do khác khiến tỉ lệ "
               "lớn như vậy các lỗi được quy cho đặc tả sai:"))
    b.append(ul([
        "hệ thống quản lý;", "quy trình;", "việc bố trí lịch đánh giá;",
        "sự tham gia của các nhân sự chủ chốt;", "trách nhiệm không được định nghĩa rõ;",
        "đào tạo và công cụ;", "độ phức tạp và kỳ vọng không thực tế;",
        "tài liệu không đầy đủ;", "soát xét cuối cùng không thỏa đáng;",
        "thay đổi trái phép so với đặc tả.",
    ]))

    b.append(h3("5.2.1 Hệ thống quản lý", "Management Systems"))
    b.append(p("Một hệ thống quản lý (tức một hệ để bảo đảm tính hiệu quả) phải có thì mô hình vòng đời mới "
               "hiệu quả được. Hệ thống quản lý thường gồm các bước sau:"))
    b.append(ol([
        "Nhận diện các hoạt động trong mô hình vòng đời và kết quả mong đợi của từng hoạt động;",
        "Đặt ra các chuẩn hiệu năng để so sánh kết quả;",
        "Đo hiệu năng thực tế;",
        "Đánh giá và so sánh hiệu năng thực tế với chuẩn đã đặt;",
        "Thực hiện các hành động khắc phục cần thiết dựa trên đánh giá đó.",
    ]))
    b.append(p("Dù việc xây dựng các chuẩn và quy trình nội bộ có thể tương đối dễ, việc xây dựng và triển "
               "khai một hệ thống quản lý để bảo đảm tuân thủ đầy đủ lại có thể khó hơn. Nguyên nhân gốc của "
               "nhiều vấn đề thường truy về hệ thống quản lý không tồn tại hoặc không hiệu quả."))
    b.append(p("Cuốn <em>Practical Loss Control Leadership</em> của F. Bird và G. Germain là một tài liệu "
               "tuyệt vời về hệ thống quản lý. Thuật ngữ “management system” tuy được dùng rộng rãi nhưng "
               "hơi sai: những hệ này thường chẳng liên quan gì tới “quản lý” cả. Một thuật ngữ hay hơn "
               "được dùng phổ biến là “managing systems” — các hệ điều hành việc gì đó."))

    b.append(h3("5.2.2 Quy trình", "Procedures"))
    b.append(p("Quy trình phải được xây dựng, soát xét, phê duyệt và hiểu rõ cho mọi hoạt động, để việc phân "
               "tích mối nguy và xác định SIL được thực hiện hiệu quả. Ví dụ, quy trình xác định SIL chỉ "
               "nhằm bảo vệ con người, hay nhằm bao quát các đối tượng chịu rủi ro khác (sự cố môi trường, "
               "tổn thất tài chính, hư hỏng thiết bị/tài sản, gián đoạn kinh doanh, trách nhiệm pháp lý, uy "
               "tín công ty, mất thị phần)? Điều này phải được phản ánh rõ trong quy trình."))
    b.append(p("Phân tích mối nguy thường dùng các kỹ thuật như phân tích cây lỗi (FTA), phân tích kiểu và "
               "ảnh hưởng của lỗi (FMEA), nghiên cứu mối nguy và khả năng vận hành (HAZOP) và các phương "
               "pháp tương tự. HAZOP có lẽ là phương pháp được chấp nhận và dùng rộng rãi nhất trong ngành "
               "chế biến."))
    b.append(p("Các kỹ thuật xác định SIL (chủ đề của chương 6) chưa được thiết lập vững như vậy. Các tổ "
               "chức lớn thường có nguồn lực để xây dựng kỹ thuật và quy trình. Các tổ chức nhỏ hơn có thể "
               "phải dựa vào tư vấn bên ngoài."))

    b.append(h3("5.2.3 Việc bố trí lịch đánh giá", "Scheduling of Assessment"))
    b.append(p("Đôi khi việc đánh giá an toàn được thực hiện mà phương pháp chưa được định nghĩa hay hiểu rõ, "
               "đơn giản chỉ vì vội cho xong hoạt động. Người chịu trách nhiệm lập kế hoạch đánh giá phải "
               "bảo đảm rằng thiết kế quá trình và tài liệu cần thiết đã hoàn thành tới mức có thể thực hiện "
               "một phân tích an toàn có ý nghĩa. Việc đánh giá không được chỉ là một thủ tục hình thức để "
               "thỏa mãn tiến độ hay quy trình của dự án."))
    b.append(p("Việc xác định SIL nên là phần mở rộng của soát xét mối nguy. Điều đó bảo đảm những hiểu biết "
               "và sự cộng hưởng hình thành trong quá trình đánh giá an toàn được chuyển tiếp sang bước xác "
               "định SIL."))

    b.append(h3("5.2.4 Sự tham gia của nhân sự chủ chốt trong quá trình soát xét",
                "Participation of Key Personnel in the Review Process"))
    b.append(p("Phần lớn các cụm thiết bị và hệ thống trong nhà máy chế biến phức tạp tới mức không một ai có "
               "thể là chuyên gia toàn diện về chúng. Một người không thể vừa thông thạo hóa học của quá "
               "trình, vừa thông thạo vật liệu dùng để chứa nó, thiết bị đo dùng để giám sát nó, hệ điều "
               "khiển dùng để điều khiển nó, thiết bị quay dùng để dẫn động nó, hệ điện dùng để cấp nguồn "
               "cho nó, và các kỹ thuật an toàn dùng để phân tích nó."))
    b.append(p("Chính vì lý do đó, HAZOP và các kỹ thuật phân tích mối nguy khác thường đòi hỏi một nhóm đa "
               "ngành. Các đại diện của nhóm dự án, quá trình, vận hành, an toàn, bảo dưỡng, thiết bị đo và "
               "điện thường là bắt buộc. Những nghiên cứu này phân tích cái gì có thể sai trong vận hành nhà "
               "máy. Nếu một mối nguy được nhận diện và được coi là đáng kể thì phải đi tới một quyết định "
               "về cách ngăn ngừa hay giảm nhẹ nó."))
    b.append(p("Khi đi qua các giai đoạn khác nhau của phân tích mối nguy và xác định SIL, điều quan trọng là "
               "không được coi mỗi giai đoạn là một hoạt động tách biệt. Nói cách khác, không được quan niệm "
               "rằng khi một giai đoạn kết thúc thì kết quả được chuyển qua một “bức tường gạch đặc” cho "
               "một nhóm khác."))

    b.append(h3("5.2.5 Trách nhiệm không được định nghĩa rõ", "Responsibilities Not Well Defined"))
    b.append(p("Với mỗi hoạt động trong bốn hoạt động nêu ở đầu mục 5.2, cần xác định và thống nhất những cá "
               "nhân giữ vai trò chủ trì/chịu trách nhiệm. Những người được giao phải hiểu rõ vai trò của "
               "mình và bảo đảm các phân tích được hoàn thành theo quy trình đã thiết lập. Vai trò chủ trì "
               "điển hình cho bốn hoạt động như sau:"))
    b.append(table(
        ["Hoạt động", "Vai trò chủ trì"],
        [["Thiết kế khái niệm quá trình", "Thiết kế quá trình"],
         ["Phân tích mối nguy và đánh giá rủi ro", "Kỹ thuật an toàn"],
         ["Áp dụng các lớp không phải SIS", "Thiết kế quá trình"],
         ["Xác định SIL nếu cần một SIF", "Kỹ thuật an toàn"]],
        "Bảng 5-1 · Vai trò chủ trì cho bốn hoạt động nền tảng. Việc gán trách nhiệm rõ ràng là một trong "
        "mười nguyên nhân hàng đầu khiến đặc tả sai."))

    b.append(h3("5.2.6 Đào tạo và công cụ", "Training and Tools"))
    b.append(p("Các nhóm tham gia đánh giá phải được đào tạo thỏa đáng và được cung cấp công cụ cần thiết. Ví "
               "dụ, trước một đợt đánh giá có thể cần cho nhân sự điều khiển quá trình và điện được đào tạo "
               "về quá trình, hoặc cần cho nhân sự quá trình được đào tạo thỏa đáng về loại và năng lực của "
               "các hệ điều khiển. Điều này là thiết yếu để bảo đảm đối thoại và hiểu biết đúng trong quá "
               "trình soát xét. Năng lực và nhu cầu đào tạo của từng thành viên phải được xác định trước "
               "khi phân tích."))

    b.append(h3("5.2.7 Độ phức tạp và kỳ vọng không thực tế",
                "Complexity and Unrealistic Expectations"))
    b.append(p("Nói chung, thiết kế càng đơn giản càng tốt. Thiết kế phức tạp khó hiểu, khó hình dung và khó "
               "soát xét. Lấy một tai nạn do Trevor Kletz mô tả làm ví dụ."))
    b.append(p("Một tai nạn ở một nhà máy liên quan tới quá trình ethylene oxide rất nguy hiểm. Ba van được "
               "lắp nối tiếp, với hai van xả giữa chúng. Như thế vẫn chưa đủ: năm van này lại được nhân đôi "
               "để có thể thử hệ trong khi nhà máy đang chạy mà không phải ngắt sản xuất."))
    b.append(p("Việc vận hành hệ được thực hiện tự động bằng máy tính. Do một lỗi phần mềm, máy tính trong "
               "chốc lát đã vận hành các van sai. Vụ nổ và cháy sau đó của ba tấn khí gây thiệt hại lớn và "
               "làm mất sản xuất nhiều tháng. Lỗi phần mềm đó có thể quy cho độ phức tạp."))
    b.append(p("Nếu cần một hệ an toàn để ngăn ngừa hay giảm nhẹ một mối nguy thì các yêu cầu phải được phát "
               "biểu càng đơn giản càng tốt. Các thành viên nhóm nên tránh đưa ra những giải pháp quá phức "
               "tạp, vì điều đó có thể dẫn tới những kỳ vọng không thực tế và không có cơ sở."))

    b.append(h3("5.2.8 Tài liệu không đầy đủ", "Incomplete Documentation"))
    b.append(p("Nhân sự điều khiển quá trình và/hoặc thiết bị đo thường chịu trách nhiệm chuẩn bị đặc tả yêu "
               "cầu an toàn. Phương pháp ghi chép đặc tả phải đủ đơn giản để mọi người hiểu được cái gì sẽ "
               "được cung cấp."))
    b.append(p("<b>Bảng 5-2</b> tóm tắt thông tin nên có trong đặc tả. Cột “chi tiết yêu cầu” xác định xem "
               "thông tin về từng hạng mục có cần cung cấp cho ứng dụng cụ thể hay không. Các ghi chú cũng "
               "nên được đưa vào khi cần. Những hạng mục bổ sung được tóm tắt trong danh mục kiểm tra thiết "
               "kế ở chương 15."))
    b.append(table(
        ["Hạng mục", "Chi tiết yêu cầu"],
        [["<b>Tài liệu và yêu cầu đầu vào</b>", ""],
         ["P&amp;ID", "Bản vẽ đường ống và thiết bị"],
         ["Sơ đồ nguyên nhân – kết quả", "Mỗi đầu vào tác động lên đầu ra nào"],
         ["Sơ đồ logic", "Logic, hàm toán, chuỗi thời gian"],
         ["Bảng dữ liệu quá trình", "Điều kiện vận hành của từng điểm đo"],
         ["Thông tin quá trình của mỗi sự kiện nguy hiểm cần SIF",
          "Nguyên nhân sự cố, động học, phần tử cuối…"],
         ["Các xét nghiệm lỗi do nguyên nhân chung của quá trình",
          "Ăn mòn, tắc nghẽn, đóng cặn…"],
         ["Yêu cầu pháp quy tác động lên SIS", "Tiêu chuẩn, quy định địa phương và liên bang"],
         ["<b>Yêu cầu chi tiết cho từng SIF</b>", ""],
         ["Mã số của SIF", "Duy nhất, dùng xuyên suốt vòng đời"],
         ["SIL yêu cầu cho từng SIF", "1, 2 hoặc 3"],
         ["Tần suất yêu cầu dự kiến", "Số lần mỗi năm"],
         ["Khoảng thời gian thử nghiệm", "Chu kỳ proof test"],
         ["Định nghĩa trạng thái an toàn của quá trình cho từng sự kiện", "Cái gì là “an toàn” ở đây"],
         ["Các đầu vào quá trình và điểm tác động", "Ngưỡng cắt của từng cảm biến"],
         ["Dải làm việc bình thường và giới hạn vận hành của biến quá trình", ""],
         ["Các đầu ra quá trình và hành động của chúng", ""],
         ["Quan hệ chức năng giữa đầu vào và đầu ra",
          "Logic, hàm toán và mọi điều kiện cho phép"],
         ["Chọn cắt bằng mất điện hay cắt bằng có điện", "De-energize / energize to trip"],
         ["Xét việc dừng bằng tay", ""],
         ["Hành động khi mất nguồn cấp cho SIS", ""],
         ["Yêu cầu về thời gian đáp ứng để đưa quá trình về an toàn", ""],
         ["Hành động đáp lại chẩn đoán và lỗi đã bộc lộ", ""],
         ["Yêu cầu về giao diện người – máy (HMI)", ""],
         ["Chức năng reset", ""],
         ["Yêu cầu chẩn đoán để đạt SIL yêu cầu", ""],
         ["Yêu cầu bảo dưỡng và thử nghiệm để đạt SIL yêu cầu", ""],
         ["Yêu cầu độ tin cậy nếu việc dừng nhầm là nguy hiểm", ""],
         ["Chế độ hỏng của từng van điều khiển", ""],
         ["Chế độ hỏng của mọi cảm biến và bộ truyền", ""]],
        "Bảng 5-2 · Thông tin nên có trong đặc tả yêu cầu an toàn. Hai nhóm lớn là tài liệu đầu vào và các "
        "yêu cầu chi tiết cho từng SIF."))
    b.append(p("Một công cụ ghi chép đơn giản nhưng hiệu quả là <b>sơ đồ nguyên nhân – kết quả</b>. Sơ đồ này "
               "cho thấy quan hệ đầu vào/đầu ra của hệ an toàn, các điểm đặt cắt, SIL của từng chức năng và "
               "mọi yêu cầu thiết kế đặc biệt. Xem <b>Bảng 5-3</b>."))
    b.append(table(
        ["Mã số", "Mô tả", "SIL", "Dải đo · điểm cắt",
         "FV-1004", "XV-1005", "P-1007", "PV-1006", "Ghi chú"],
        [["FALL-1000", "Lưu lượng tới lò phản ứng chính R-100", "2", "0–200 GPM · 100,0",
          "X", "X", "", "", "1"],
         ["PAHH-1002", "Áp suất trong lò phản ứng", "2", "0–800 PSI · 600",
          "X", "X", "", "", "1, 2"],
         ["XA-1003", "Mất nguồn điều khiển", "", "—",
          "X", "X", "X", "X", ""],
         ["XA-1004", "Mất khí dụng cụ", "", "—",
          "X", "X", "X", "X", ""],
         ["HA-1005", "Dừng bằng tay", "", "—",
          "X", "X", "X", "X", ""]],
        "Bảng 5-3 · Sơ đồ nguyên nhân – kết quả: mỗi hàng là một nguyên nhân, mỗi cột là một tác động. "
        "Ghi chú 1 — cần trễ 2 giây trước khi đóng FV-1004. Ghi chú 2 — nút reset đặt tại van PV-1006.",
        cls="tbl matrix"))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản PDF gốc của trang này <b>là bản scan bị lỗi</b>: dòng tiêu đề "
        "của bốn cột tác động bị đảo thứ tự chữ, nên không xác định chắc chắn được động từ mô tả hành động "
        "của từng van. Bảng trên giữ nguyên mã thiết bị và toàn bộ dấu X đúng như bản gốc; phần mô tả hành "
        "động nên được đọc lại từ bản giấy trước khi dùng làm mẫu."))
    b.append(p("Đặc tả phải nêu <em>cái gì</em> cần đạt được, chứ không nhất thiết phải nêu <em>cách</em> đạt "
               "được. Điều đó cho người khác tự do quyết định cách tốt nhất để hoàn thành mục tiêu, và cũng "
               "để mở đường cho hiểu biết và kỹ thuật mới."))

    b.append(h3("5.2.9 Soát xét cuối cùng không thỏa đáng",
                "Inadequate Final Review of Specification"))
    b.append(p("Đặc tả phải được soát xét khi hoàn thành và được mọi bên liên quan tới việc xác định SIL phê "
               "duyệt. Điều đó bảo đảm sự hiểu biết và nhất trí. Người chịu trách nhiệm không được cho rằng "
               "mọi người tham gia đều có cùng cách hiểu trong suốt quá trình soát xét SIL. Lần soát xét "
               "cuối cùng này cho mọi người cơ hội suy ngẫm lại các quyết định và làm rõ mọi hiểu lầm."))

    b.append(h3("5.2.10 Thay đổi trái phép so với đặc tả",
                "Unauthorized Deviation from Specification"))
    b.append(p("Khi đặc tả đã được phê duyệt, không được thực hiện thay đổi nào trừ khi tuân theo quy trình "
               "thay đổi chính thức. Hệ và đặc tả có thể cần được cập nhật nếu có thay đổi trong quá trình "
               "dự án (xem chương 13, “Quản lý thay đổi một hệ thống”). Dù có thể cám dỗ thực hiện một số "
               "thay đổi để tránh rào cản về chi phí hay tiến độ, không được thay đổi gì mà không qua quy "
               "trình soát xét và phê duyệt phù hợp."))

    # ---------------------------------------------------------------- 5.3
    b.append(h2("5.3 Yêu cầu của ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511 Mod)",
                "ANSI/ISA-84.00.01-2004, Parts 1-3 (IEC 61511 Mod) Requirements"))
    b.append(p("Điều 10.3 của ANSI/ISA-84.00.01-2004 (IEC 61511 Mod) đưa ra bản tóm tắt các yêu cầu an toàn "
               "cho SIS. Dưới đây là những yêu cầu then chốt của tiêu chuẩn; các chi tiết khác xem trong "
               "tiêu chuẩn."))
    b.append(p("Các yêu cầu phải đủ để thiết kế SIS và phải bao gồm:"))
    b.append(ul([
        "Mô tả mọi SIF cần thiết để đạt được mức an toàn chức năng yêu cầu;",
        "Yêu cầu nhận diện và tính đến lỗi do nguyên nhân chung;",
        "Định nghĩa trạng thái an toàn của quá trình cho từng SIF đã nhận diện;",
        "Định nghĩa mọi trạng thái an toàn riêng lẻ mà khi xảy ra đồng thời lại tạo ra một mối nguy khác "
        "(ví dụ quá tải kho chứa khẩn cấp, nhiều dòng xả đồng thời về hệ thống đốt);",
        "Các nguồn yêu cầu giả định và tần suất yêu cầu của từng SIF;",
        "Yêu cầu về khoảng thời gian proof test;",
        "Yêu cầu về thời gian đáp ứng để SIF đưa quá trình về trạng thái an toàn;",
        "SIL và chế độ vận hành (theo yêu cầu/liên tục) của từng SIF;",
        "Mô tả các phép đo quá trình và điểm tác động của chúng;",
        "Mô tả các hành động đầu ra và tiêu chí vận hành thành công (ví dụ yêu cầu về van đóng kín);",
        "Quan hệ chức năng giữa đầu vào và đầu ra quá trình, gồm logic, hàm toán và mọi điều kiện cho phép;",
        "Yêu cầu về dừng bằng tay;",
        "Yêu cầu về việc cắt bằng có điện hay mất điện;",
        "Yêu cầu về reset SIF sau khi dừng;",
        "Tần suất dừng nhầm tối đa cho phép;",
        "Chế độ hỏng và đáp ứng mong muốn của SIF;",
        "Mọi yêu cầu cụ thể liên quan tới quy trình khởi động và khởi động lại SIF;",
        "Mọi giao diện giữa SIS và bất kỳ hệ nào khác (kể cả BPCS và người vận hành);",
        "Mô tả các chế độ vận hành của nhà máy và xác định những SIF cần làm việc trong mỗi chế độ;",
        "Các yêu cầu an toàn của phần mềm ứng dụng (liệt kê dưới đây);",
        "Yêu cầu về ghi đè/khóa/bypass, kể cả cách xóa chúng;",
        "Đặc tả mọi hành động cần thiết để đạt hoặc duy trì trạng thái an toàn khi phát hiện lỗi trong SIF;",
        "Thời gian sửa chữa trung bình khả thi cho SIF;",
        "Nhận diện các tổ hợp nguy hiểm của trạng thái đầu ra SIS cần tránh;",
        "Nhận diện các điều kiện môi trường cực đoan mà SIS có thể gặp;",
        "Nhận diện các chế độ bình thường và bất thường cho cả nhà máy (ví dụ khởi động nhà máy) và cho "
        "từng quy trình vận hành;",
        "Định nghĩa yêu cầu cho mọi chức năng an toàn cần sống sót qua một sự kiện tai nạn lớn (ví dụ thời "
        "gian một van phải còn làm việc được khi có cháy).",
    ]))
    b.append(p("Điều 12.2 của tiêu chuẩn đưa ra yêu cầu về đặc tả các yêu cầu an toàn của phần mềm ứng dụng. "
               "Điều thiết yếu là đặc tả phần mềm ứng dụng phải nhất quán với các yêu cầu an toàn nêu trên."))
    b.append(ul([
        "Phải xây dựng một đặc tả yêu cầu an toàn cho phần mềm ứng dụng.",
        "Đầu vào của đặc tả yêu cầu an toàn phần mềm cho từng phân hệ SIS phải bao gồm: các yêu cầu an toàn "
        "đã đặc tả của SIF; các yêu cầu phát sinh từ kiến trúc SIS; và mọi yêu cầu từ việc lập kế hoạch an "
        "toàn.",
        "Đặc tả yêu cầu an toàn phần mềm ứng dụng phải đủ chi tiết để cho phép thiết kế và triển khai đạt "
        "được mức toàn vẹn an toàn yêu cầu, và để có thể thực hiện việc đánh giá an toàn chức năng.",
        "Người phát triển phần mềm ứng dụng phải soát xét thông tin trong đặc tả để bảo đảm các yêu cầu là "
        "rõ ràng, nhất quán và dễ hiểu.",
        "Các yêu cầu an toàn phần mềm đã đặc tả phải được diễn đạt và cấu trúc sao cho rõ ràng, kiểm chứng "
        "được, thử nghiệm được, sửa đổi được và truy vết được.",
        "Đặc tả yêu cầu an toàn phần mềm ứng dụng phải cung cấp thông tin cho phép lựa chọn thiết bị phù hợp.",
    ]))

    # ---------------------------------------------------------------- 5.4
    b.append(h2("5.4 Ghi chép các yêu cầu đặc tả", "Documenting the Specification Requirements"))
    b.append(p("Vì đặc tả sẽ là nền tảng của thiết kế hệ an toàn, mọi thông tin cần thiết phải được tập hợp "
               "thành một bộ hoàn chỉnh. Bốn hạng mục sau là những tài liệu then chốt cũng phải nằm trong bộ "
               "SRS."))
    b.append(ol([
        "<b>Mô tả quá trình.</b> Phải bao gồm: bản vẽ đường ống và thiết bị (P&amp;ID); mô tả vận hành quá "
        "trình; mô tả điều khiển quá trình gồm triết lý thiết kế hệ điều khiển, loại điều khiển, giao diện "
        "người vận hành, quản lý cảnh báo và ghi dữ liệu lịch sử; các quy định an toàn đặc thù của công ty, "
        "địa phương, bang/tỉnh hoặc liên bang; các vấn đề độ tin cậy, chất lượng hay môi trường; danh sách "
        "các vấn đề vận hành hoặc bảo dưỡng.",
        "<b>Sơ đồ nguyên nhân – kết quả.</b> Có thể dùng để ghi chép các yêu cầu chức năng và yêu cầu toàn "
        "vẹn một cách đơn giản, dễ hiểu với mọi ngành. Xem ví dụ ở Bảng 5-3.",
        "<b>Sơ đồ logic.</b> Có thể dùng bổ sung cho sơ đồ nguyên nhân – kết quả với những chức năng và "
        "chuỗi phức tạp hơn và/hoặc có yếu tố thời gian mà sơ đồ nguyên nhân – kết quả khó mô tả. Sơ đồ "
        "logic phải được lập theo ISA-5.2-1976 (R1992).",
        "<b>Bảng dữ liệu quá trình.</b> Bảo đảm rằng thông tin cần thiết để hoàn thành các bảng đặc tả thiết "
        "bị đo được ghi chép đầy đủ.",
    ]))

    # ---------------------------------------------------------------- summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Đặc tả yêu cầu an toàn (SRS) gồm hai phần: đặc tả yêu cầu chức năng và đặc tả yêu cầu toàn "
               "vẹn. Nó bao gồm cả yêu cầu phần cứng lẫn phần mềm. Yêu cầu chức năng mô tả đầu vào, đầu ra "
               "và logic của hệ. Yêu cầu toàn vẹn mô tả hiệu năng của từng chức năng an toàn."))
    b.append(p("HSE Anh đã xem xét 34 vụ tai nạn là hậu quả trực tiếp của lỗi hệ điều khiển và hệ an toàn "
               "trong nhiều ngành khác nhau. Kết quả cho thấy 44 % tai nạn là do đặc tả sai và/hoặc thiếu "
               "(cả đặc tả chức năng lẫn đặc tả toàn vẹn)."))
    b.append(p("Không thể nói quá tầm quan trọng của việc bảo đảm đặc tả hệ là đúng."))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "If chapter 3 answered “why must it be a separate system”, this chapter answers “how must that "
        "system be written down”. Behind the answer sits one number worth remembering: 44 % of accidents "
        "caused by control and safety system failures come from specifications that were wrong or "
        "incomplete — not from hardware that broke. Most of the failure was written into the system before "
        "anybody installed anything."))

    b.append(h2("The specification is the design"))
    b.append(p("It is tempting to treat the safety requirement specification as paperwork that follows the "
               "engineering. It is the other way round. Once the SRS is approved, every later activity — "
               "the logic design, the factory acceptance test, the proof test procedure, the management of "
               "change — is checked against it. An error in the SRS therefore does not stay in one place. "
               "It propagates into the software, into the test that confirms the software, and into the "
               "procedure that maintains it, and it does so consistently, so that every check agrees with "
               "every other check and the error becomes invisible."))
    b.append(p("This is what makes a systematic failure different from a random one. A failed transmitter "
               "announces itself eventually. A specification that says “close valve B on low pressure in "
               "vessel A” when the process actually needs valve C, or needs the valve closed on high "
               "pressure, will be implemented exactly as written, tested exactly as written, and will work "
               "perfectly — until the day the demand arrives. No amount of reliability engineering "
               "addresses that failure, because nothing in the system is unreliable."))

    b.append(h2("Forty-four percent is a statement about process, not about engineers"))
    b.append(p("The HSE figure is often quoted as if it were a criticism of the people who write "
               "specifications. It is more useful read as a criticism of the sequence in which "
               "specifications get written. The four activities that precede a specification — conceptual "
               "design, hazard analysis, application of non-SIS layers, SIL determination — are exactly "
               "the four that get compressed when a project is late, and they are compressed in that "
               "order. The specification is then written against a design basis that was never finished."))
    b.append(p("The symptom is easy to recognise in a review: a specification that describes what the "
               "system will do, in great detail, without ever stating what it is protecting against. The "
               "document is not wrong; it is unanchored. Every sentence can be traced to an instrument "
               "tag, and no sentence can be traced to a hazard."))

    b.append(h2("Simple is not a style preference"))
    b.append(p("The ethylene oxide story in section 5.2.7 is usually told as a warning about software. It "
               "is better told as a warning about valve counts. Three valves in series with two bleeds "
               "between them is already a configuration whose failure modes are hard to enumerate; "
               "duplicating all five so the system can be tested online doubles the enumeration and adds "
               "a mode in which the test itself creates the hazard. The software error was the proximate "
               "cause; the configuration was the reason a software error could produce an explosion."))
    b.append(p("The practical test for a safety function is whether a competent engineer who has never "
               "seen the plant can follow the cause and effect diagram in one pass. If they need the "
               "narrative to explain it, the diagram is describing a design that is too complicated to "
               "be verified — and a function that cannot be verified cannot be claimed at a high SIL, "
               "whatever the hardware."))

    b.append(h2("What the standard actually requires the SRS to say"))
    b.append(p("Section 5.3 lists the contents that ANSI/ISA-84.00.01-2004 requires of a safety "
               "requirements specification. Read as a list of topics it is dry. Read as a checklist it is "
               "the most practical page in the book, because every item on it is something that cannot be "
               "added later without changing the design."))
    b.append(table(
        ["The SRS must state", "Why it cannot be deferred"],
        [["A description of each safety instrumented function",
          "The function, not the instrument. “Trip on high pressure” does not say what closes; if the "
          "sentence has no output in it, the design is being done at the wrong stage."],
         ["The safe state for each function",
          "De-energised, valve closed, fan stopped, damper open. The answer decides the wiring, the "
          "solenoid type and the failure direction of every component downstream."],
         ["The demand rate",
          "It is the denominator of the PFD. Without it the SIL target is a number with no units, and "
          "every calculation in chapter 8 is meaningless."],
         ["The target SIL for each function",
          "Derived from the hazard study and the risk tolerance, never from what the vendor's catalogue "
          "happens to offer."],
         ["The proof-test interval",
          "A design parameter, not a maintenance preference: it enters the PFD with the same weight as "
          "the failure rate (chapter 12)."],
         ["The response time, sensor to final element",
          "Usually dominated by the valve stroke and usually omitted. A trip that closes the valve in "
          "eleven seconds does not satisfy a requirement written for three."],
         ["The process measurements and trip points",
          "With units, ranges, and the source of the number. A trip point with no provenance is a guess "
          "that will be re-guessed at every review."],
         ["The output actions and the input–output relationship",
          "The cause and effect matrix. It is the document that survives commissioning, and the only one "
          "an operator will read at three in the morning."],
         ["The behaviour on failure of the SIS itself",
          "Fail-safe direction, and what the outputs do on loss of power or loss of the logic solver."],
         ["The reset and restart requirements",
          "Manual or automatic reset, what permissives must be satisfied, and who is permitted to reset."],
         ["The bypass and override provisions",
          "A function that cannot be tested online will not be tested. The bypass is what buys the test "
          "interval the PFD assumes."],
         ["The maximum spurious trip rate",
          "The second requirement, and in practice usually the binding one — see chapter 16, where the "
          "nuisance-trip budget is tighter than the SIL."]],
        "Table 5.1 · The contents the standard requires of a safety requirements specification, and the "
        "reason each one has to be settled before the design starts rather than after."))
    b.append(p("Two rows do more work than the rest. The <b>demand rate</b> turns a SIL from an adjective "
               "into a number, because it is the only thing that converts a probability into a frequency. "
               "The <b>proof-test interval</b> is the only item on the list that can be changed after "
               "commissioning without touching hardware — which is exactly why it gets changed informally, "
               "and why the calculation quietly stops being true."))

    b.append(h2("Cause and effect: the one document everybody reads"))
    b.append(p("Of all the documents in the SRS package, the cause and effect matrix is the one that "
               "actually gets used after commissioning. The P&ID is consulted when something is modified, "
               "the narrative is read once, the logic diagrams are read by the programmers — but the "
               "cause and effect matrix is what the operator, the maintenance technician and the auditor "
               "all reach for, because it answers the only question that matters at three in the morning: "
               "if this goes out of range, what happens?"))
    b.append(p("That makes its accuracy disproportionately important, and its format disproportionately "
               "conservative. One row per cause, one column per effect, one mark per action, and a notes "
               "column for everything that does not fit — delays, reset locations, permissives. A matrix "
               "that needs a footnote to explain a footnote has stopped being a matrix."))
    return "\n".join(b)
