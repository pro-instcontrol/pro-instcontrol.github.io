# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 10, Engineering a System
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis10fig as F

PAGES_SRC = 16
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>PIP (primary integrity parameter)</em> — cách gọi (hơi khôi hài) của tác giả cho các yếu "
            "tố quyết định tính toàn vẹn: công nghệ, kiến trúc, suất hỏng, chẩn đoán, nguồn, giao diện, an "
            "ninh, chu kỳ thử. · "
            "<em>Cắt bằng ngắt điện</em> — bình thường có điện, mất điện là lệnh cắt; đây là chuẩn của "
            "phần lớn SIS. · "
            "<em>Cắt bằng cấp điện</em> — bình thường không có điện, cấp điện mới là lệnh cắt (thường dùng "
            "cho bảo vệ máy và hệ báo cháy-nổ). · "
            "<em>Giám sát đường dây</em> — đo dòng nhỏ để phân biệt đứt dây với tiếp điểm mở. · "
            "<em>Forcing</em> — gán cưỡng bức giá trị vào/ra trong PLC, tương đương một bypass nhưng "
            "không để lại dấu vết bên ngoài. · "
            "<em>Mô hình V</em> — mỗi bước thiết kế ở nhánh trái có một bước kiểm chứng đối xứng ở nhánh "
            "phải. · "
            "<em>FPL / LVL / FVL</em> — ngôn ngữ cố định / ít biến thiên / toàn biến thiên. · "
            "<em>Emulation / simulation</em> — chạy thử trên chính bộ xử lý của hệ / chạy thử trên PC phát "
            "triển.")
    return note(
        "<b>Key terms.</b> <em>PIP</em> — the authors' half-serious name for the factors that decide "
        "integrity: technology, architecture, failure rates, diagnostics, power, interfaces, security, "
        "test interval. · <em>De-energise to trip</em> — normally live; losing power is the trip, the norm "
        "for most SIS. · <em>Energise to trip</em> — normally dead; applying power is the trip, usual in "
        "machinery protection and fire and gas. · <em>Line monitoring</em> — measuring a trickle current to "
        "tell a "
        "broken wire from an open contact. · <em>Forcing</em> — writing a value over an I/O point in a PLC, "
        "which is a bypass with no visible evidence. · <em>V-model</em> — every design step on the left leg "
        "has a matching verification step on the right. · <em>FPL / LVL / FVL</em> — fixed, limited "
        "variability and full variability languages. · <em>Emulation / simulation</em> — running the logic "
        "on the target processor versus on the development PC.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Chương 7 bàn ưu nhược điểm của các công nghệ hệ logic. Nhưng thiết kế một SIS không chỉ là chọn "
        "một hộp logic. Chương 9 bàn các vấn đề thiết bị trường. Chương này bàn những khía cạnh quản lý, "
        "phần cứng và phần mềm còn lại — những thứ không thể đưa vào mô hình độ tin cậy (chủ đề của "
        "chương 8) nhưng lại ảnh hưởng sâu sắc đến hiệu năng của hệ."))

    b.append(note_terms("vi"))

    b.append(quote("Mọi thứ nên được làm đơn giản nhất có thể, nhưng không đơn giản hơn thế.",
                   "Albert Einstein"))
    b.append(p("Mục tiêu của nhiều kỹ sư và nhiều công ty là xây một “sách dạy nấu ăn” cho thiết kế hệ "
               "thống. Các kỹ sư lâu năm, với kinh nghiệm và hiểu biết của mình, sẽ viết ra các quy tắc và "
               "phương pháp để các kỹ sư trẻ làm theo. Nhưng phải cẩn thận: một bộ quy tắc hay quy trình "
               "đơn lẻ không thể áp dụng cho mọi hệ thống và mọi tổ chức."))

    # ------------------------------------------------------------------ 10.1
    b.append(h2("10.1 Những vấn đề quản lý chung", "General Management Considerations"))
    b.append(p("Mục 5 của IEC 61511 bàn về quản lý an toàn chức năng. Tiêu chuẩn dĩ nhiên tập trung vào "
               "những vấn đề liên quan đến hệ thống đo lường an toàn, không phải các vấn đề sức khoẻ và an "
               "toàn nói chung. IEC 61511 nêu rằng phải xác định các chính sách và chiến lược để đạt được "
               "an toàn, cùng cách đánh giá việc đạt được ấy. Phải xác định con người và các bộ phận, và "
               "thông báo cho họ biết trách nhiệm của mình. Nhân sự phải có năng lực để thực hiện các hoạt "
               "động được giao. Năng lực là hàm của kiến thức, kinh nghiệm và đào tạo. Các yêu cầu về năng "
               "lực phải được xác định và ghi thành văn bản."))

    b.append(h3("10.1.1 Thời điểm và định nghĩa công việc", "Job Timing and Definition"))
    b.append(p("Nhiều vấn đề của hệ thống bắt nguồn từ hai yếu tố đơn giản: sự kết hợp giữa định nghĩa "
               "kém và thời điểm. Hoặc phạm vi công việc quá mơ hồ, đặc tả thiếu (hoặc không tồn tại ở thời "
               "điểm mua hàng hay thậm chí ở thời điểm thiết kế), và công việc thì đáng lẽ phải xong từ "
               "tuần trước. Đặc tả không đầy đủ thường dẫn đến phạm vi bị nới rộng, chi phí tăng, chậm "
               "tiến độ và bất mãn. Càng xác lập và ghi chép chắc chắn được bao nhiêu ngay từ đầu thì mọi "
               "người càng dễ chịu bấy nhiêu. Chương 2 đã tóm tắt phát hiện của Cơ quan An toàn và Sức "
               "khoẻ Anh: phần lớn vấn đề của hệ thống (44 %) là do đặc tả sai (cả đặc tả chức năng lẫn "
               "đặc tả toàn vẹn)."))

    b.append(h3("10.1.2 Nhân sự", "Personnel"))
    b.append(p("Sau khi hợp đồng được ký, tốt nhất là không thay đổi con người trong suốt dự án. Dù hàng "
               "đống tài liệu chắc chắn là một phần của mọi hợp đồng, định luật Murphy dự báo rằng đúng cái "
               "duy nhất không có trong đó sẽ xuất hiện và cắn bạn. Cái duy nhất ấy chỉ tồn tại trong đầu "
               "một ai đó, và khi người ấy bị chuyển đi thì mẩu thông tin ấy đi theo, để rồi ló cái đầu xấu "
               "xí của nó ra vào đúng thời điểm tệ nhất."))
    b.append(p("Dù viết ra giấy nhiều đến đâu, đặc tả bao giờ cũng mở ra nhiều cách hiểu. Nếu thay người, "
               "phương hướng dự án sẽ bị mất trong lúc người mới định hình lại ý kiến. Điều này có thể gây "
               "hậu quả nghiêm trọng cho tiến độ và giá hợp đồng, vì có thể phải đàm phán lại các hạng "
               "mục."))

    b.append(h3("10.1.3 Trao đổi giữa các bên", "Communication Between Parties"))
    b.append(p("Điều quan trọng là thiết lập các kênh trao đổi rõ ràng giữa các công ty tham gia. Quản lý "
               "dự án của công ty A nên là người duy nhất nói chuyện với quản lý dự án của công ty B. Nếu "
               "các bên khác bắt đầu dính vào, một số hạng mục có thể không được ghi chép, cấp quản lý có "
               "thể không được thông báo, và những mẩu thông tin quan trọng chắc chắn sẽ rơi qua khe, để "
               "rồi gây đau đầu lớn về sau."))

    b.append(h3("10.1.4 Tài liệu", "Documentation"))
    b.append(p("Tài liệu sẽ được cung cấp theo định dạng chuẩn của người dùng, của công ty kỹ thuật, hay "
               "của đơn vị tích hợp? Bản vẽ khổ bao nhiêu? Chỉ trên giấy hay cả dạng số? Nếu dạng số thì "
               "dùng chương trình nào? Sẽ có 200 sơ đồ vòng lặp, hay chỉ một vòng lặp “điển hình” kèm một "
               "bảng tóm tắt thông tin của 199 vòng còn lại? Những chuyện nhỏ như vậy rất dễ bị bỏ qua cho "
               "đến lúc chúng trở thành điểm tranh chấp lớn."))

    # ------------------------------------------------------------------ 10.2
    b.append(h2("10.2 Những vấn đề phần cứng chung", "General Hardware Considerations"))
    b.append(p("Thiết kế và phân tích một hệ an toàn đòi hỏi xét nhiều yếu tố khác nhau: chọn công nghệ, "
               "kiến trúc, suất hỏng và chế độ hỏng, chẩn đoán, nguồn, giao diện, an ninh, chu kỳ thử… "
               "Nhiều yếu tố trong số đó đã được bàn và phân tích ở chương 7, 8 và 9. Có người còn gọi "
               "những yếu tố này là PIP (primary integrity parameter — thông số toàn vẹn chính). Có những "
               "người rất thích chữ viết tắt!"))
    b.append(fig(2, F.fig_10_2(), "vi"))

    b.append(h3("10.2.1 Hệ có điện và hệ không có điện", "Energized vs. De-energized Systems"))
    b.append(p("Phần lớn ứng dụng SIS là loại bình thường có điện (ngắt điện để dừng). Một số ứng dụng "
               "(điển hình là điều khiển máy) thì ngược lại: bình thường không có điện và cấp điện để tác "
               "động. Khác biệt trong thiết kế hệ này kéo theo những điều cần xét riêng. Hệ thiết kế cho "
               "kiểu này có thể không phù hợp với kiểu kia. Không thể chỉ dùng một dạng đảo logic là "
               "xong. [Ref. 8]"))
    b.append(p("Ví dụ, trong một hệ bình thường có điện, trạng thái logic khoẻ mạnh là 1 (có điện). Một hư "
               "hỏng an toàn hay việc tháo mất một thành phần sẽ khiến hệ không dự phòng dừng lại (logic "
               "0). Với một hệ bình thường không có điện, trạng thái logic khoẻ mạnh là 0 (không điện). Một "
               "hư hỏng an toàn hay việc tháo mất một thành phần trong hệ như vậy <em>không</em> làm hệ dừng "
               "— muốn dừng thì đầu ra phải nhảy lên logic 1 — nên hỏng hóc cứ thế nằm im; trong khi hệ sẽ "
               "dừng ngay nếu chỉ đơn giản đảo logic. Những hệ ấy phải được thiết kế khác đi."))
    b.append(p("Với hệ bình thường không có điện, van điện từ đầu ra phải có cơ cấu chốt để khi có lệnh "
               "cắt, van chốt ở đúng trạng thái. Nếu không, khi mất điện sau một lần dừng, hoặc khi pin "
               "cạn, thiết bị có thể quay về trạng thái chạy bất thường, và điều đó có thể tạo ra tình "
               "trạng nguy hiểm."))
    b.append(p("Với hệ bình thường không có điện, nên dùng cầu chì có tiếp điểm báo hỏng. Loại này phát "
               "báo động khi cầu chì đứt. Nếu không, một cầu chì đứt trong hệ bình thường không có điện sẽ "
               "không được nhận ra, tạo ra hư hỏng nguy hiểm tiềm ẩn có thể khiến hệ không hoạt động."))
    b.append(p("Với hệ bình thường không có điện, nên giám sát đường dây (giám sát mạch) cho cáp trường "
               "vào và ra (và một số hệ bắt buộc phải làm). Giám sát đường dây cáp trường cho phép phát "
               "hiện mạch hở — cũng là những hư hỏng nguy hiểm tiềm ẩn có thể khiến hệ bình thường không "
               "có điện không hoạt động đúng."))
    b.append(p("Hệ bình thường không có điện cũng cần theo dõi (và báo động) được việc mất nguồn."))
    b.append(p("Hệ bình thường không có điện thường được chọn khi việc chống cắt nhầm là ưu tiên hàng đầu. "
               "Đó thường là trường hợp của hệ báo cháy và khí, và hệ bảo vệ máy. Những hệ này tác động "
               "nhầm có thể gây hư hại thiết bị và tình trạng nguy hiểm cho con người."))

    b.append(h3("10.2.2 Chẩn đoán hệ thống", "System Diagnostics"))
    b.append(p("Mọi SIS, bất kể công nghệ hay mức dự phòng nào, đều cần chẩn đoán kỹ lưỡng. Hệ an toàn, "
               "do bản chất, là tĩnh tại hay thụ động; vì thế một số hư hỏng có thể không tự bộc lộ. Hư "
               "hỏng nguy hiểm có thể khiến hệ không phản ứng với một yêu cầu thật của quá trình. Với hệ an "
               "toàn khi hỏng (thừa nhận rằng không gì an toàn 100 %), như một số hệ rơ-le hay hệ bán dẫn "
               "rắn kiểu châu Âu, có thể thực hiện chẩn đoán định kỳ bằng tay (ví dụ đóng-ngắt mạch để xem "
               "chúng có đáp ứng đúng không). Với phần lớn công nghệ khác, phải đưa thêm khả năng chẩn đoán "
               "tự động vào thiết kế hệ."))
    b.append(p("Một số hệ có sẵn trên thị trường với chẩn đoán rất kỹ. Với những hệ ấy, gần như không cần "
               "người dùng can thiệp thêm. Với một số hệ khác — cụ thể là thiết bị đa dụng — tự chẩn đoán "
               "có thể rất hạn chế. Những hệ này thường đòi hỏi người dùng can thiệp thêm."))
    b.append(p("Ví dụ, linh kiện điện tử có thể hỏng ở trạng thái dẫn, tức có điện. Trong một hệ bình "
               "thường có điện, hư hỏng như vậy có thể không được chú ý. Điều này nguy hiểm tiềm ẩn, vì nếu "
               "có yêu cầu thật của quá trình thì hệ sẽ không ngắt điện được. PLC đa dụng thường có rất ít "
               "chẩn đoán trong mô-đun vào/ra (tức độ phủ chẩn đoán thấp). Một số người dùng đã viết bài về "
               "chủ đề này và mô tả những mô-đun vào/ra cùng phần lập trình ứng dụng phải thêm vào để đưa "
               "hệ đạt mức chẩn đoán chấp nhận được."))

    b.append(h3("10.2.3 Giảm thiểu nguyên nhân chung", "Minimize Common Cause"))
    b.append(p("Hư hỏng do nguyên nhân chung là những tác nhân căng thẳng hay lỗi duy nhất làm hỏng cả hệ "
               "dự phòng. Ví dụ hiển nhiên là nguồn (ví dụ cấp nguồn đơn cho một bộ điều khiển ba kênh), "
               "phần mềm (một lỗi sẽ làm mọi kênh hỏng), và công tắc dự phòng (nếu công tắc không làm việc "
               "thì hệ dự phòng đôi sẽ hỏng). Đáng tiếc là không phải mọi hư hỏng đều hiển nhiên như vậy. "
               "Các nghiên cứu trong nhà máy điện hạt nhân cho thấy khoảng 25 % số hư hỏng ở trạm phát điện "
               "là do vấn đề nguyên nhân chung. [Ref. 4] Máy bay đã rơi vì đường điều khiển ba kênh bị cắt "
               "đứt. Một hệ máy tính chính phủ dự phòng bảy đường đã hỏng khi một sợi cáp quang duy nhất bị "
               "cắt. [Ref. 6]"))
    b.append(p("Một vòng luẩn quẩn bắt đầu xuất hiện: hệ dự phòng đưa vào thêm độ phức tạp, độ phức tạp ấy "
               "làm vấn đề nguyên nhân chung trầm trọng thêm, và có thể dẫn đến việc lắp thêm nhiều thiết "
               "bị hơn nữa. Khi dùng hệ dự phòng, các ảnh hưởng nguyên nhân chung thường mang tính bên "
               "ngoài (nhiệt độ, rung, xung điện áp, nhiễu tần số vô tuyến) cùng sự can thiệp vô ý của con "
               "người. Dự phòng có hiệu quả với hư hỏng ngẫu nhiên của phần cứng, nhưng không hiệu quả với "
               "sai sót thiết kế hay sai sót hệ thống khác. Cách hiệu quả nhất để giảm vấn đề nguyên nhân "
               "chung là a) tách thiết bị về mặt vật lý, và b) dùng thiết bị đa dạng (không giống nhau). "
               "Nếu các bộ điều khiển dự phòng được đặt trong các tủ khác nhau ở các phòng khác nhau, một "
               "hư hỏng chung khó xảy ra. Nếu dùng hai bộ chuyển đổi áp suất khác nhau, của hai hãng khác "
               "nhau, dựa trên hai công nghệ đo khác nhau, thì khả năng chúng có vấn đề chung còn thấp hơn "
               "nữa. Có thể sẽ có người bật cười trước khả năng nguyên nhân chung hiển nhiên đến thế khi "
               "đấu nhiều cảm biến vào cùng một điểm lấy mẫu — nhưng chuyện ấy đã xảy ra không chỉ một "
               "lần. Nếu ai đó làm được thì chắc chắn sẽ có người làm!"))
    b.append(p("Một hệ quả thực dụng: nếu hai bộ điều khiển dự phòng nằm chung một tủ, thì cái tủ ấy là "
               "một khối nguyên nhân chung. Quạt làm mát hỏng, chuột cắn dây, hay một lần nước tràn vào "
               "phòng đều đánh vào cả hai kênh cùng lúc — và mô hình Markov sẽ không bao giờ nhìn thấy "
               "điều đó."))

    b.append(h3("10.2.4 Kích thước và bố trí tủ", "Panel Size and Layout"))
    b.append(p("Một trong những tài liệu đầu tiên được tạo ra ở giai đoạn thiết kế hệ là bản vẽ bố trí "
               "tổng thể. Những bản vẽ này xác định kích thước và trọng lượng tổng của tủ. Người ta kể "
               "nhiều chuyện về việc bản vẽ được lập, được xem xét và được khách hàng ký, hệ được chế tạo "
               "và giao đi, rồi tủ lại quá lớn không lọt qua cửa phòng điều khiển."))
    b.append(p("Cần xét đến việc nhân viên sẽ tiếp cận hệ như thế nào. Kỹ thuật viên phải có đủ chỗ để "
               "tiếp cận các phần khác nhau bên trong tủ. Nếu không, người phải chen giữa hai thiết bị có "
               "thể vô tình ngắt một cầu dao. Phải có đủ ánh sáng bên trong tủ. Các bộ phận phải được dán "
               "nhãn rõ ràng."))
    b.append(p("Rất phổ biến là đặt thanh cái điện ở phía dưới hầu hết các tủ, đơn giản vì phần lớn tủ được "
               "thiết kế cho cáp vào từ dưới. Điều này có thể gây vấn đề nếu kỹ thuật viên đặt hộp cơm kim "
               "loại hay dụng cụ của họ trên sàn tủ. Chính vì lý do ấy, một số đơn vị tích hợp đặt thanh "
               "cái ở phía trần tủ."))

    b.append(h3("10.2.5 Điều kiện môi trường", "Environmental Considerations"))
    b.append(p("Điều quan trọng là phải nêu yêu cầu về môi trường trong đặc tả hệ thống. Phải có bảo vệ "
               "thích đáng chống nhiệt độ, độ ẩm, rung, nhiễu điện, vấn đề nối đất, chất bẩn…"))
    b.append(p("Ví dụ, một trong các tác giả biết một hệ mà người dùng muốn lập trình được bằng phần mềm, "
               "nhưng trong toà nhà điều khiển không còn chỗ. Tủ phải đặt ngoài trời, ở Nam Texas, cạnh "
               "lò đốt mà nó điều khiển, trong khu vực Class 1 Division 2. Hệ được cung cấp trong một vỏ "
               "kín, chống thời tiết, có sục khí, với bộ làm mát khí xoáy để giữ mát mùa hè và một điện "
               "trở sưởi để chống ngưng tụ mùa đông. Nếu đơn vị tích hợp không được cho biết về những vấn "
               "đề vị trí đặc thù ấy, hệ đã không chạy được lâu."))
    b.append(p("Một người dùng cuối ở Trung Đông yêu cầu hệ phải làm việc ở 60 °C mà không cần quạt làm "
               "mát. Không nhiều hệ làm được điều đó. Chỉ có thể tự hỏi người dùng ấy đã trải qua bao nhiêu "
               "hư hỏng trước khi đưa yêu cầu này vào đặc tả của mình."))
    b.append(p("Một trong các tác giả từng đến một cơ sở mà phần lớn tủ điều khiển đều có biển đỏ rất lớn "
               "ghi: “Không bấm bộ đàm trong phạm vi 4,5 m quanh tủ này.” Chỉ có thể hình dung những vấn "
               "đề họ đã gặp khiến họ phải lắp những cảnh báo như vậy. Ít nhất một hệ an toàn đã dừng vì "
               "một kỹ thuật viên đang làm việc với tủ mở cửa chỉ việc trả lời điện thoại di động!"))
    b.append(p("Nói chung, tăng nhiệt độ của thiết bị điện tử thêm 10 °C làm giảm tuổi thọ khoảng 50 %. "
               "Thông gió tủ (ví dụ quạt) phải giữ nhiệt độ bên trong tủ trong giới hạn đặc tả của nhà sản "
               "xuất thì hệ mới tin cậy được. Cũng phải xét tương tự với rung, khí ăn mòn… Có những hệ với "
               "mô-đun có tản nhiệt kim loại lớn, gioăng cao su và mạch phủ conformal để chịu được môi "
               "trường khắc nghiệt như vậy. Thiết kế ấy dĩ nhiên đi kèm chi phí cao hơn."))

    b.append(h3("10.2.6 Nguồn điện", "Power"))
    b.append(p("Nguồn điện, như nhiều chủ đề khác, không phải vấn đề trắng đen. Không có cách xử lý nguồn "
               "nào rõ ràng là đúng hay sai. Nói đơn giản: hệ cần nguồn sạch, được bảo vệ và ổn định. Phải "
               "có biến áp cách ly để chống xung, quá độ, nhiễu, quá áp/sụt áp…"))
    b.append(p("Hệ an toàn quan trọng thường được cấp từ hai nguồn dự phòng. Có nhiều cách làm việc này. "
               "Mỗi hệ và/hoặc mỗi cách đều có ưu nhược điểm riêng cho từng ứng dụng. Phải đánh giá từng "
               "hệ theo mục đích sử dụng. Chuyển sang bộ dự phòng có thật sự không gây gián đoạn? Cách làm "
               "hiệu quả cho một công trình có thể không hiệu quả cho công trình khác. Pin dự phòng, như "
               "mọi thứ khác, sẽ không làm việc nếu không được bảo trì. Có gì thật sự “không ngắt được” "
               "không?! Mọi phần của hệ đều phải được thử định kỳ. Có thể khắc phục nhiều vấn đề trên bằng "
               "cách dùng hai nguồn DC dự phòng, ghép chúng qua đi-ốt (diode ORing) để loại bỏ công tắc "
               "xoay chiều."))
    b.append(p("Bộ nguồn phải được lắp sao cho tản nhiệt tốt nhất mà vẫn dễ tiếp cận và tìm lỗi."))

    b.append(h3("10.2.7 Nối đất", "Grounding"))
    b.append(p("Nối đất đúng là điều quan trọng để lắp đặt thành công. Nối đất thường quan trọng hơn với "
               "hệ phần mềm/điện tử so với hệ điện cũ. Phải tuân thủ sát khuyến nghị của nhà sản xuất. Một "
               "số hệ yêu cầu nối đất cố định; số khác yêu cầu nối đất thả nổi. Một hệ thiết kế cho kiểu "
               "này có thể không chạy đúng nếu đấu kiểu kia. Một danh mục kiểm tra sơ bộ gồm: ăn mòn, bảo "
               "vệ catốt, tĩnh điện, và các barie an toàn tia lửa."))

    b.append(h3("10.2.8 Chọn công tắc và rơ-le", "Selection of Switches and Relays"))
    b.append(p("Rơ-le phải được chọn không chỉ theo tải lớn nhất (để tránh hàn dính tiếp điểm — kiểu hỏng "
               "nguy hiểm nhất trong một SIS) mà cả theo tải nhỏ nhất. Nếu không tính đến điều này, dòng "
               "nhỏ trong mạch có thể không đủ để giữ tiếp điểm rơ-le sạch, và nhiều năm sau mạch có thể "
               "hở vì tiếp điểm bẩn. Điều này khó chẩn đoán, vì đó thường không phải thứ đầu tiên người ta "
               "nghĩ tới."))

    b.append(h3("10.2.9 Bypass", "Bypasses"))
    b.append(p("Có thể cần bypass cho một số hoạt động bảo trì và khởi động. Tuy nhiên, để hệ ở trạng thái "
               "bypass là rất nguy hiểm. Nếu quá trình có thể nguy hiểm trong khi một chức năng SIS đang bị "
               "bypass, phải có biện pháp kiểm soát hành chính và quy trình bằng văn bản để duy trì an toàn "
               "cho quá trình."))
    b.append(p("Có thể thực hiện bypass theo nhiều cách. Lắp dây nhảy là cách nguy hiểm tiềm ẩn vì không "
               "có dấu hiệu bên ngoài cho biết có thứ gì đó đang bị bypass. Người vận hành có thể đang tự "
               "hỏi vì sao hệ không làm việc đúng, mà không hề biết rằng một kỹ thuật viên ở đâu đó đã đặt "
               "một thứ gì vào bypass để bảo trì."))
    b.append(p("Gần như mọi PLC đều có thể dùng “forcing” vào/ra để làm việc tương tự bypass. Chính sự dễ "
               "dàng của việc này ở một số hệ là điều đáng lo. Để các điểm vào/ra bị forcing mà không có "
               "dấu hiệu nào về tình trạng ấy là rất nguy hiểm tiềm ẩn."))
    b.append(p("Quản lý bypass rất quan trọng để bảo đảm bypass được gỡ nhanh và đúng. Việc này tương tự "
               "giấy phép làm việc nóng — một vấn đề đã góp phần vào thảm hoạ Piper Alpha ở Biển Bắc, nơi "
               "hơn 160 người thiệt mạng. Cần có ghi chép và kiểm soát chặt chẽ. Nên dùng một loại phiếu "
               "bypass. Phiếu này phải có sự hiểu biết và phê duyệt của bộ phận vận hành, có giới hạn thời "
               "gian nêu rõ và được gia hạn khi đổi ca, và có thể yêu cầu nhiều cấp phê duyệt."))
    b.append(p("Với nhiều hệ, khi một đầu vào đang bị bypass, không có chỉ thị nào ở tủ cho biết trạng "
               "thái thật của đầu vào. Làm sao biết tín hiệu có khoẻ không trước khi gỡ bypass? Nếu đầu vào "
               "vào báo động trong lúc đang bypass thì sao? Làm sao biết được? Hệ phải được thiết kế sao cho "
               "kể cả khi một đầu vào đang bị bypass, hệ vẫn cho biết trạng thái thật của thiết bị trường."))
    b.append(p("Có nhiều cách đưa hệ về điều kiện bình thường sau một lần bypass khởi động. Ví dụ, cảm biến "
               "lửa cần được bypass để khởi động hệ đốt. Khi đã phát hiện lửa, có thể gỡ bypass vì không "
               "còn cần nữa. Một khoá dừng do mức thấp có thể cần bypass để khởi động một tổ máy. Khi mức "
               "đạt giá trị bình thường, có thể gỡ bypass. Ở một số ứng dụng, có thể dùng bộ định thời để "
               "tự gỡ bypass."))
    b.append(p("Đã có ghi chép về những tai nạn nghiêm trọng trong công nghiệp hoá chất khi hệ bị tạm ngưng "
               "hoạt động, hoặc khi một phần hệ được vận hành bằng tay mà người khác không biết. [Ref. 6 và "
               "7]"))

    b.append(h3("10.2.10 Thử chức năng", "Functional Testing"))
    b.append(p("Yêu cầu về thử nghiệm hệ phải được đưa vào thiết kế. Hệ sẽ được thử thế nào? Có bypass từng "
               "phần và thử bằng tay không? Có đưa vào một dạng thử tự động nào không, kể cả cho thiết bị "
               "trường? Người thiết kế có thể giả định thiết bị sẽ được thử hằng năm. Kỹ thuật viên bảo trì "
               "có thể thấy yêu cầu ấy hoàn toàn vô lý so với thực tế của cơ sở. Ngoài ra, thiết bị cần thử "
               "có thể khó tiếp cận, khiến việc thử khó xảy ra. Người thiết kế có thể muốn đưa vào thử hành "
               "trình một phần cho van. Bộ phận vận hành có thể lo ngại về khả năng cắt nhầm và vì thế hoàn "
               "toàn phản đối ý ấy. Sẽ hữu ích nếu đưa nhân sự bảo trì và vận hành vào một buổi xem xét "
               "thiết kế để bắt được những vấn đề tiềm ẩn như vậy."))

    b.append(h3("10.2.11 An ninh", "Security"))
    b.append(p("Hệ sẽ được bảo vệ đến mức nào? Ai nên có quyền truy cập và ai không? Mỗi người khác nhau "
               "nên truy cập được bao nhiêu phần của hệ? Quyền truy cập sẽ được kiểm soát thế nào?"))
    b.append(p("Một trong các tác giả biết một kỹ sư tự nhận mình là người duy nhất, với chiếc máy tính "
               "xách tay duy nhất, chịu trách nhiệm thay đổi một hệ nọ. Vậy mà mỗi lần anh ta kết nối vào, "
               "trong bộ điều khiển lại đang chạy một phiên bản chương trình khác với bản trên máy anh ta. "
               "Người khác đang thay đổi mà không được phép. Sao có thể như vậy? Một số hệ không có tính "
               "năng an ninh thật sự nào. Nếu vậy, phải áp dụng các quy trình quản lý để ngăn truy cập trái "
               "phép. Đáng tiếc là quy trình có thể và sẽ bị vi phạm vào lúc này lúc khác."))
    b.append(p("Một trong các tác giả nghe kể về một kỹ sư bất mãn đã từ máy tính ở nhà qua modem xâm nhập "
               "được vào DCS của nhà máy và sửa cơ sở dữ liệu của nó. Một lần nữa, điều như vậy lẽ ra không "
               "bao giờ có thể xảy ra với một SIS. Tuy nhiên vấn đề muôn thuở là nhìn lại thì bao giờ cũng "
               "rõ. Rõ ràng là khó hơn một chút khi phải nhìn trước và dự đoán những sự kiện có thể chưa "
               "từng xảy ra. Có lẽ nên ghi nhớ một biến thể của định luật Murphy: nếu hệ cho phép, và ai đó "
               "làm được, thì đến lúc nào đó họ sẽ làm — dù được cảnh báo bao nhiêu lần đi nữa."))
    b.append(p("Một trong các tác giả từng tham quan một cơ sở nơi kỹ sư điều khiển tỏ ra tự hào về quy "
               "trình an ninh của mình. Khi đi qua phòng điều khiển, tác giả nhận thấy nhiều tủ điều khiển "
               "mở toang, chìa khoá cắm trong ổ, và không có ai khác trong khu vực. Vị kỹ sư có thể hài "
               "lòng với an ninh của họ, nhưng tác giả thì không."))
    b.append(p("Có thể dùng chìa khoá để kiểm soát truy cập, nhưng phải có và phải thực thi quy trình quản "
               "lý việc cấp phát và sử dụng chìa. Mật khẩu có thể cho nhiều mức truy cập khác nhau (ví dụ "
               "để bypass, forcing, sửa phần mềm), nhưng việc dùng mật khẩu cũng phải được kiểm soát chặt. "
               "Đừng dán mật khẩu lên giao diện vận hành!"))

    b.append(h3("10.2.12 Giao diện vận hành", "Operator Interfaces"))
    b.append(p("Nhiều thiết bị khác nhau có thể dùng làm giao diện vận hành: màn hình, báo động, đèn, nút "
               "bấm… Tất cả đều có thể dùng để truyền thông tin cho người vận hành, như hành động dừng đã "
               "thực hiện, nhật ký bypass, chẩn đoán hệ thống, trạng thái thiết bị trường và logic, mất "
               "nguồn năng lượng ảnh hưởng an toàn, hỏng thiết bị môi trường… Tuy nhiên, việc vận hành hệ "
               "không được phụ thuộc vào giao diện, vì giao diện có thể không phải lúc nào cũng hoạt động "
               "hay sẵn có."))
    b.append(p("Cần trả lời những câu hỏi sau trong đặc tả yêu cầu, cho từng mục dữ liệu được hiển thị:"))
    b.append(ol([
        "Sự kiện nào khiến mục này được hiển thị?",
        "Mục hiển thị có thể và có nên được cập nhật không, và nếu có thì do sự kiện nào (ví dụ thời gian, "
        "hành động đã thực hiện…)?",
        "Sự kiện nào khiến dữ liệu hiển thị biến mất?",
    ]))
    b.append(p("Không nêu rõ những tiêu chí trên có thể dẫn đến đặc tả thiếu và trở thành nguồn nguy hiểm "
               "tiềm ẩn."))
    b.append(p("Điều quan trọng là cung cấp một số thông tin cho người vận hành (tuy không đến mức quá "
               "tải), nhưng cũng quan trọng không kém là giới hạn những gì người vận hành thật sự làm được "
               "ở giao diện. Ví dụ, nếu một phần của hệ bị đặt bypass, có chỉ thị nào cảnh báo người khác "
               "không?"))
    b.append(p("Giao diện vận hành là quan trọng, nhưng không nên là yếu tố then chốt hay bắt buộc để vận "
               "hành đúng. Không được cho phép sửa cách vận hành của hệ an toàn từ giao diện vận hành. Cần "
               "suy nghĩ xem điều gì nên xảy ra nếu màn hình giao diện trắng (điều đã được báo cáo không "
               "chỉ một lần)."))
    b.append(p("Tín hiệu cảnh báo không nên xuất hiện quá thường xuyên hay quá lâu, vì người ta có xu hướng "
               "trở nên vô cảm với kích thích liên tục."))

    # ------------------------------------------------------------------ 10.3
    b.append(h2("10.3 Những vấn đề phần mềm chung", "General Software Considerations"))
    b.append(quote("Và họ nhìn vào phần mềm, và thấy rằng nó tốt. Nhưng họ chỉ cần thêm đúng một tính năng "
                   "nữa thôi…", "G. F. McCormick"))
    b.append(p("Chất lượng phần mềm ứng dụng do người dùng cuối phát triển dĩ nhiên là vấn đề quan trọng "
               "ảnh hưởng đến hiệu năng tổng của hệ. Việc đặc tả, thiết kế, lắp đặt và thử nghiệm phần mềm "
               "ứng dụng không phải lúc nào cũng được ưu tiên và nhấn mạnh đúng mức. Điều này có thể dẫn "
               "đến vận hành sai, chậm trễ và chi phí tăng."))
    b.append(p("Trong công nghiệp chế biến, thường thấy nhóm chịu trách nhiệm phát triển phần mềm cho hệ "
               "điều khiển quá trình cơ bản (BPCS) cũng chịu trách nhiệm phát triển phần mềm cho hệ thống "
               "đo lường an toàn (SIS). Cùng một nhóm người và cùng một quy trình thường được dùng để triển "
               "khai cả hai. Điều này có thể không chỉ tạo ra vấn đề nguyên nhân chung đáng kể, mà còn tạo "
               "ra một quy trình phát triển phần mềm tiềm ẩn không đầy đủ."))

    b.append(h3("10.3.1 Vòng đời phần mềm", "Software Lifecycle"))
    b.append(p("Nhiều kỹ thuật, mô hình và phương pháp đã được dùng để phát triển phần mềm ứng dụng. Những "
               "kỹ thuật này thường theo một trình tự hay bộ bước nhất định để bảo đảm thành công. Ý định "
               "là làm đúng ngay lần đầu, thay vì buộc phải làm lại."))
    b.append(p("Phương pháp ít hình thức nhất, và có lẽ phổ biến nhất, có thể gọi là “viết rồi sửa”. Trong "
               "trường hợp đó, yêu cầu không được định nghĩa hay đặc tả rõ. Người lập trình có thể buộc "
               "phải viết mã rồi hỏi: “Có phải cái anh muốn là thế này không?” Quá trình lặp ấy có thể kéo "
               "dài cho đến khi một hệ trông có vẻ chạy được hình thành. Phần mềm rốt cuộc được phát triển "
               "dựa trên các hướng dẫn chung, và yêu cầu thật thì được xác định sau khi phần lớn mã đã viết "
               "xong. Đây rõ ràng là cách làm không hiệu quả, tốn thời gian và tốn kém."))
    b.append(p("Cũng như có một vòng đời tổng thể cho việc phát triển hệ an toàn, phần mềm cũng nên theo "
               "một quy trình phát triển theo vòng đời hiệu quả. Hình 10-1 cho thấy mô hình V cho phát "
               "triển phần mềm. Lưu ý rằng đây chỉ là một trong nhiều mô hình phát triển phần mềm. Mô hình "
               "V mô tả cách tiếp cận từ trên xuống trong thiết kế và thử nghiệm. Cần định nghĩa yêu cầu và "
               "thiết lập quy trình kiểm chứng để kiểm tra rằng từng yêu cầu (mỗi khối trong Hình 10-1) đã "
               "được đáp ứng."))
    b.append(fig(1, F.fig_10_1(), "vi"))
    b.append(p("Ví dụ về những hạng mục và vấn đề cần xét:"))
    b.append(ul([
        "<b>Yêu cầu phần mềm:</b> mọi yêu cầu có thể có của phần mềm — kể cả khởi động hệ, vận hành, bảo "
        "trì, dừng, báo động, bypass… — phải được ghi chép rõ ràng. Cơ sở để phát triển phần mềm là đặc "
        "tính yêu cầu an toàn (SRS). SRS phải chứa yêu cầu logic cho từng chức năng an toàn. Nếu SRS "
        "không tồn tại hoặc không đầy đủ, việc phát triển phần mềm hiệu quả sẽ rất khó.",
        "<b>Kiến trúc phần mềm:</b> xác định cấu trúc tổng thể của phần mềm sẽ dùng, gồm ngôn ngữ, cấu "
        "trúc chương trình chính, các chương trình con, tương tác giữa chương trình chính và chương trình "
        "con, các khối hàm chuẩn, các hàm bổ sung hay tuỳ chỉnh…",
        "<b>Lập trình:</b> việc viết mã hay tạo ra phần mềm thật sự dựa trên ngôn ngữ và kiến trúc đã xác "
        "định trước đó. Có thể có một hoặc nhiều chương trình tuỳ theo yêu cầu.",
        "<b>Tích hợp:</b> bảo đảm mọi giao diện và tương tác với hệ thống và chương trình khác hoạt động "
        "đúng như dự định.",
        "<b>Thử nghiệm:</b> bảo đảm các yêu cầu tổng thể đã được đáp ứng.",
    ]))

    b.append(h3("10.3.2 Các loại chương trình và ngôn ngữ", "Program and Language Types"))
    b.append(p("IEC 61511 mô tả ba loại phần mềm: ứng dụng, tiện ích và nhúng. Phần mềm ứng dụng là phần "
               "người dùng hệ viết và nạp vào bộ điều khiển. Phần mềm tiện ích dùng để phát triển và kiểm "
               "chứng chương trình ứng dụng. Phần mềm nhúng được cung cấp như một phần của hệ khả trình, "
               "ví dụ hệ điều hành của bộ điều khiển."))
    b.append(p("Người dùng chủ yếu quan tâm đến việc phát triển phần mềm ứng dụng. Tiêu chuẩn mô tả ba "
               "loại ngôn ngữ phát triển: chương trình cố định (FPL), ít biến thiên (LVL) và toàn biến "
               "thiên (FVL). Ngôn ngữ cố định là loại người dùng chỉ được điều chỉnh vài thông số, ví dụ "
               "đặt dải đo cho một bộ chuyển đổi áp suất. Ngôn ngữ ít biến thiên bị giới hạn trong các hàm "
               "thư viện định trước, chuyên cho ứng dụng. Logic bậc thang và lập trình khối hàm là ví dụ về "
               "ngôn ngữ ít biến thiên. Chương trình viết bằng ngôn ngữ toàn biến thiên phức tạp hơn và "
               "cung cấp dải chức năng rộng hơn nhiều, ví dụ C hay Pascal."))
    b.append(p("Dùng ngôn ngữ cố định và ít biến thiên được coi là phù hợp cho ứng dụng SIL 1–3. Tiêu "
               "chuẩn không quy định yêu cầu lập trình khác nhau cho ứng dụng SIL 1–3. "
               "ANSI/ISA-84.00.01/IEC 61511 không bao gồm việc dùng ngôn ngữ toàn biến thiên hay ứng dụng "
               "SIL 4; người đọc được dẫn sang IEC 61508. Người ta mong rằng ngôn ngữ toàn biến thiên và "
               "ứng dụng SIL 4 sẽ không được triển khai trong công nghiệp chế biến."))
    b.append(p("Dùng lại phần mềm hay sơ đồ logic sẵn có (ví dụ lập trình một PLC hoàn toàn dựa trên sơ đồ "
               "logic bậc thang của hệ rơ-le mà nó thay thế) không nhất thiết làm tăng an toàn. Thật ra nó "
               "có thể làm giảm an toàn. Như đã nêu, phần lớn sai sót có thể truy về đặc tả yêu cầu. Nếu "
               "yêu cầu không được xem xét cẩn thận trong lần ứng dụng đầu tiên, lỗi có thể vẫn còn đó. "
               "Ngoài ra, những mối nguy gắn với hệ mới thì không thể đã được xét khi hệ cũ được lắp (ví "
               "dụ PLC không an toàn khi hỏng theo cùng cách rơ-le)."))
    b.append(p("Một trong những ngôn ngữ lập trình phổ biến nhất cho hệ an toàn dựa trên phần mềm là logic "
               "bậc thang. Logic bậc thang tương đối đơn giản và nói chung dễ hiểu với chính người viết ra "
               "nó (ít nhất là trong tuần đó). Đáng tiếc là người phải sửa hệ nhiều năm sau sẽ không phải "
               "người đã lập trình ban đầu. Những cách lập trình lạ và tuỳ chỉnh thường khó bảo trì. Điều "
               "này không có nghĩa là không bao giờ nên làm. Có thể chú thích đầy đủ cho chương trình logic "
               "bậc thang bằng những ghi chú chi tiết, nhưng điều đó không bảo đảm nó rõ ràng."))
    b.append(p("Có nhiều ngôn ngữ khác nhau để lập trình hệ dựa trên phần mềm. Như đã nêu, logic bậc thang "
               "có lẽ là ngôn ngữ phổ biến nhất; nó là sản phẩm phát triển tự nhiên từ các hệ rơ-le đấu dây "
               "cứng. Tuy nhiên logic bậc thang có thể không phải ngôn ngữ phù hợp nhất cho một số loại "
               "chức năng khác. Ví dụ, vận hành tuần tự hay theo mẻ dễ xử lý hơn bằng ngôn ngữ khác: sơ đồ "
               "chức năng tuần tự. Các hàm toán học có thể dễ triển khai hơn bằng văn bản có cấu trúc. Tiêu "
               "chuẩn IEC 61131-3 bao gồm năm ngôn ngữ: logic bậc thang, khối hàm, sơ đồ chức năng tuần "
               "tự, văn bản có cấu trúc và danh sách lệnh. Dùng một hệ triển khai nhiều ngôn ngữ cho phép "
               "làm từng chức năng bằng ngôn ngữ phù hợp nhất. Việc này có thể dễ hơn và rẻ hơn so với cố "
               "nhồi mọi thứ vào một ngôn ngữ rốt cuộc hoá ra khá gượng gạo."))
    b.append(p("Tiêu chuẩn nêu rằng phần mềm phải được ghi chép rõ ràng, chính xác và đầy đủ. Nói thì rất "
               "dễ, làm không phải lúc nào cũng dễ. Nhiều chương trình ứng dụng được phát triển từ những "
               "đoạn văn mô tả. Đáng tiếc là văn bản có thể được hiểu theo nhiều cách khác nhau. Ví dụ, bạn "
               "hình dung được bao nhiêu bức tranh từ ba chữ đơn giản “sư tử ăn thịt người”? Đó có thể là "
               "một người đàn ông trong nhà hàng đang ăn bít tết. Bít tết sư tử. Một số chương trình ứng "
               "dụng được phát triển từ yêu cầu logic ghi trong ma trận nguyên nhân – kết quả. Tuy nhiên, "
               "nếu PLC được dùng phải lập trình bằng logic bậc thang, thì ai đó phải chuyển logic từ ma "
               "trận sang bậc thang. Sai sót do diễn giải có thể phát sinh từ đó."))
    b.append(p("Có người đã lập trình hệ dự phòng đa dạng bằng các nhóm khác nhau, dùng hộp logic khác nhau "
               "và gói phần mềm khác nhau. Việc này không chỉ trở thành cơn ác mộng về thiết kế, gỡ lỗi, "
               "bảo trì và tài liệu, mà lịch sử đã cho thấy nó không hiệu quả. Mọi chương trình đều phải "
               "được viết theo một đặc tả chung, và phần lớn vấn đề nằm ở chính chỗ đó. Vấn đề tương tự "
               "cũng có với việc thử phần mềm: người thử có thể bỏ sót đúng những trường hợp lạ mà người "
               "phát triển đã bỏ sót."))

    b.append(h3("10.3.3 Định lượng hiệu năng phần mềm", "Quantifying Software Performance"))
    b.append(p("Phần mềm không xuống cấp và hỏng theo cách các thành phần cơ khí hỏng. Phần mềm hoặc được "
               "viết đúng, hoặc không. Thường chính một tổ hợp sự kiện không lường trước làm hệ dựa trên "
               "phần mềm hỏng."))
    b.append(p("Nhiều người đã cố định lượng hiệu năng của phần mềm. Việc này đã trở thành một vấn đề gây "
               "tranh cãi gay gắt. Có hàng chục kỹ thuật và chúng cho những đáp án rất khác nhau. Vì thế "
               "các uỷ ban soạn tiêu chuẩn hệ an toàn đã từ bỏ ý định định lượng hiệu năng phần mềm. Thay "
               "vào đó, người dùng được khuyến khích theo một vòng đời có phương pháp, nêu rõ yêu cầu, phát "
               "triển và thử nghiệm. Thực hành đặc tả và phát triển tốt phải dẫn đến phần mềm tốt. Định "
               "lượng những thực hành mà nhiều người có thể nhận ra là kém thì chẳng cải thiện được gì."))

    b.append(h3("10.3.4 Thử nghiệm phần mềm", "Testing Software"))
    b.append(p("Một ưu điểm của việc dùng hệ khả trình là khả năng thử logic. Có thể làm việc này bằng bộ "
               "xử lý của chính hệ điện tử khả trình (PES) — thường gọi là “emulation” — hoặc trên máy tính "
               "phát triển — thường gọi là “simulation”. Emulation là thử bằng đúng bộ xử lý mà chương "
               "trình sẽ chạy trên đó. Simulation là thử bằng một bộ xử lý nhiều khả năng khác với bộ xử lý "
               "dùng trong SIS. Khác biệt có thể tinh vi, nhưng đáng để ý. Chỉ vì chương trình chạy được "
               "trong một môi trường không bảo đảm nó sẽ chạy trong môi trường khác. Nhiều nhà cung cấp PES "
               "cung cấp một dạng khả năng emulation và/hoặc simulation chương trình ứng dụng cùng hệ của "
               "họ. Điều này cho phép người dùng thử logic ứng dụng cả trong và sau khi phát triển chương "
               "trình."))
    b.append(p("Thử phần mềm là cách thử chức năng logic PES và giao diện vận hành mà không đấu vào/ra "
               "trường. Việc thử được thực hiện trước khi lắp đặt tại hiện trường, với nguồn lực hạn chế và "
               "xa môi trường nhà máy. Thử phần mềm PES không phải là mô phỏng quá trình hay nhà máy (tuy "
               "có các gói mô phỏng riêng), cũng không bao gồm việc thử logic BPCS hay thiết bị trường."))
    b.append(p("Một số lợi ích của việc thử phần mềm:"))
    b.append(ul([
        "<b>Chi phí:</b> cả chi phí kỹ thuật lẫn chi phí khởi động. Sửa vấn đề phần mềm hay lập trình ở "
        "ngoài nhà máy, trong môi trường được kiểm soát, dễ hơn và hiệu quả hơn về chi phí so với làm tại "
        "nhà máy ngay trước khi khởi động. Tiến độ dự án dễ giữ hơn vì vấn đề tại hiện trường được giảm "
        "thiểu.",
        "<b>Sửa lỗi sớm.</b> Không hệ nào hoàn hảo và lỗi sẽ tồn tại. Càng phát hiện và sửa sớm càng tốt.",
        "<b>Ít bất ngờ hơn trong chạy thử và khởi động.</b> Logic đã được thử và các bên liên quan đã "
        "“sờ tận tay”. Có thể tách vấn đề phần mềm khỏi vấn đề phần cứng vì đã tin rằng logic được thử "
        "đầy đủ. Sẽ ít chuyện đổ lỗi cho nhau hơn.",
        "<b>Simulation/emulation là công cụ đào tạo tuyệt vời.</b>",
        "<b>Đưa được phản hồi sớm của người dùng vào.</b>",
    ]))
    b.append(p("Có thể làm simulation/emulation ngay tại văn phòng người thiết kế một cách liên tục trong "
               "khi logic đang được phát triển, vì không cần vào/ra vật lý. Với simulation chỉ cần phần mềm "
               "phát triển ứng dụng (tức không cần phần cứng PES thật)."))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Thiết kế một SIS bao gồm nhiều lựa chọn về quản lý, phần cứng và phần mềm. Dù nhiều hạng "
               "mục trong số đó khó — nếu không muốn nói là không thể — định lượng trong một mô hình độ tin "
               "cậy, chúng đều có tầm quan trọng sống còn với việc vận hành đúng và bền lâu của hệ."))

    b.append(note(
        "<b>Hai điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Hình 10-2 là hình bổ sung.</b> Mục 10.2.1 chỉ mô tả bằng lời sự khác nhau giữa hệ bình "
        "thường có điện và hệ bình thường không có điện, cùng lý do vì sao “chỉ đảo logic” là sai. Bản dịch "
        "vẽ thêm bảng so sánh bốn trạng thái cho mỗi kiểu, vì đây là chỗ dễ hiểu nhầm nhất trong cả "
        "chương.<br>"
        "<b>(2) Một câu trong bản gốc bị lặp từ.</b> Đoạn về logic bậc thang in “This is not imply to it "
        "should never be done” — rõ ràng là lỗi ấn loát của câu “This is not to imply it should never be "
        "done”. Bản dịch hiểu theo nghĩa sau. Ngoài ra, tác giả dùng “dissimilar” và “diverse” như hai từ "
        "đồng nghĩa trong cùng một đoạn về dự phòng đa dạng; bản dịch giữ cả hai nghĩa bằng một thuật ngữ "
        "thống nhất là “đa dạng”."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "ISA-84.01-1996. <em>Application of Safety Instrumented Systems for the Process Industries</em>.",
        "IEC 61508-1998. <em>Functional Safety of Electrical/Electronic/Programmable Electronic "
        "Safety-Related Systems</em>.",
        "<em>Guidelines for Safe Automation of Chemical Processes</em>. American Institute of Chemical "
        "Engineers – Center for Chemical Process Safety, 1993.",
        "Smith, David J. <em>Reliability, Maintainability, and Risk: Practical Methods for Engineers</em>. "
        "Ấn bản 4. Butterworth-Heinemann, 1993. (Ấn bản 5 [1997] và 6 [2001] cũng có.)",
        "Leveson, Nancy G. <em>Safeware — System Safety and Computers</em>. Addison-Wesley, 1995.",
        "Neumann, Peter G. <em>Computer Related Risks</em>. Addison-Wesley, 1995.",
        "Belke, James C. <em>Recurring Causes of Recent Chemical Accidents</em>. U.S. Environmental "
        "Protection Agency – Chemical Emergency Preparedness and Prevention Office, 1997.",
        "Gruhn, Paul và A. Rentcome. “Safety Control System Design: Are All the Bases Covered?” "
        "<em>Control</em>, tháng 7/1992.",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "This is the chapter about everything that does not fit in the model. Panel doors, password "
        "stickers, lunch buckets on bus bars, the engineer who left the project in month four. None of it "
        "appears in a Markov diagram, and all of it decides whether the system still works in year twelve."))

    b.append(h2("The specification is the failure mode"))
    b.append(p("The 44 % figure from the UK Health and Safety Executive is the most useful number in this "
               "chapter, and it is not about hardware at all. Nearly half of system problems trace back to "
               "a specification that was wrong, incomplete, or written after the purchase order. Section "
               "10.1.1 describes the mechanism precisely: vague scope plus a deadline that has already "
               "passed, which produces scope creep, which produces a renegotiation, which produces a system "
               "that meets the contract and not the plant."))
    b.append(p("The V-model in Figure 10-1 is the structural answer, and its point is often missed. It is "
               "not that you test at the end; it is that each test is designed at the same time as the "
               "thing it tests. A requirement with no acceptance criterion is not a requirement, it is a "
               "wish, and it will be discovered as a defect during commissioning when the fix is most "
               "expensive."))
    b.append(fig(1, F.fig_10_1(), "en"))

    b.append(h2("Energise to trip versus de-energise to trip"))
    b.append(p("Section 10.2.1 contains a trap that catches people who think they are being clever. A "
               "normally energised system fails safe by dropping out: loss of power trips the plant. A "
               "normally de-energised system, common in fire and gas and in machinery protection, fails "
               "safe by energising — so loss of power means no trip, and an inverted logic solver gives you "
               "exactly the wrong behaviour."))
    b.append(fig(2, F.fig_10_2(), "en"))
    b.append(p("Everything else in that section follows from this one fact. The latching solenoids, the "
               "alarm fuses, the line monitoring: each exists because in a de-energised system a broken "
               "wire and a healthy circuit look identical. That is the price of choosing the architecture "
               "that does not trip the plant every time a fuse blows, and it is a price worth paying only "
               "if somebody actually installs the monitoring."))

    b.append(h2("Common cause is an installation problem, not a component problem"))
    b.append(p("The nuclear industry figure — a quarter of all failures attributable to common cause — is "
               "usually read as an argument for diversity. It is better read as an argument for looking at "
               "the room. Two diverse transmitters on one process tap share a plugging failure. Two "
               "redundant controllers in one cabinet share a fan, a door and a flood. The Beta factor in "
               "chapter 8 quantifies this, but the fix is architectural and it is cheap: separate the "
               "taps, separate the cabinets, separate the power feeds."))
    b.append(p("The authors' line — if someone can, someone inevitably will — is the right frame for the "
               "whole chapter. Every bypass that can be left in place will be left in place. Every "
               "password that can be shared will be shared. Every forced I/O point that leaves no visible "
               "trace will eventually be left forced over a weekend."))

    b.append(h2("Bypass administration is a safety function"))
    b.append(p("The Piper Alpha reference in section 10.2.9 is not rhetorical. A permit-to-work system "
               "that fails is a bypass that nobody removes, and 167 people died because a procedure was "
               "not followed. The design consequences are concrete: a bypass should be visible at the "
               "panel, should have a time limit, should require shift-by-shift renewal, and should not "
               "hide the true state of the field device while it is in place."))
    b.append(p("Forcing is the quiet version of the same problem. It is a bypass with no jumper wire and no "
               "evidence, available from a laptop, and in many systems it survives a download. If the "
               "system permits it, somebody will do it at three in the morning during a startup."))

    b.append(h2("Software: stop trying to measure it, start trying to specify it"))
    b.append(p("Section 10.3.3 is refreshingly honest. Software does not wear out, so the failure rate "
               "model of chapter 8 simply does not apply; the standards committees looked at the dozens of "
               "quantification techniques, saw that they disagreed by orders of magnitude, and abandoned "
               "the exercise. What they kept was the lifecycle, because a specification defect is a "
               "design defect, and a design defect in software is a permanent one."))
    b.append(p("The ladder-logic warning is worth repeating: reusing the relay system's logic diagram as "
               "the PLC program carries forward every requirement error of the original design, and adds a "
               "new class of hazard the original never had. The relay was fail-safe by physics. The PLC is "
               "fail-safe only by configuration."))
    return "".join(b)
