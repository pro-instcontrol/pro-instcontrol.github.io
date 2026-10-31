# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 15, SIS Design Checklist
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis15fig as F

PAGES_SRC = 22
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"

YES = "Y · N · N/A"

# (number, stem, sub-items) — subs is None or a list of (letter, text)
SECTIONS = [
    (1, "Yêu cầu quản lý", "Management Requirements", [
        ("1.1", "Người hoặc bộ phận chịu trách nhiệm thực hiện từng pha của vòng đời đã được xác định chưa?", None),
        ("1.2", "Người hoặc bộ phận chịu trách nhiệm thực hiện từng pha của vòng đời đã được thông báo về "
                "trách nhiệm của mình chưa?", None),
        ("1.3", "Những người ấy có đủ năng lực để làm công việc được giao không?", None),
        ("1.4", "Năng lực của nhân sự có được ghi nhận về kiến thức, kinh nghiệm và đào tạo không?", None),
        ("1.5", "Đã thực hiện đánh giá mối nguy/rủi ro chưa?", None),
        ("1.6", "Đã có kế hoạch an toàn xác định các hoạt động cần thiết chưa?", None),
        ("1.7", "Đã có quy trình bảo đảm các khuyến nghị được giải quyết nhanh chóng và thoả đáng chưa?", None),
        ("1.8", "Đã có quy trình kiểm toán việc tuân thủ các yêu cầu chưa?", None),
    ]),
    (2, "Đặc tả yêu cầu an toàn", "Safety Requirements Specification", [
        ("2.1", "Các yêu cầu an toàn có xuất phát từ một đánh giá mối nguy có hệ thống không? Nếu không, "
                "các yêu cầu ấy dựa trên cơ sở nào?", None),
        ("2.2", "Đã có mô tả rõ ràng và súc tích cho từng chức năng liên quan đến an toàn sẽ được thực hiện "
                "trong SIS chưa?", None),
        ("2.3", "Trạng thái an toàn của quá trình đã được xác định cho từng trạng thái vận hành của nhà máy "
                "chưa? (ví dụ: khởi động, vận hành bình thường, bảo trì…)", None),
        ("2.4", "Các chức năng an toàn đã được xác định cho từng trạng thái vận hành của nhà máy chưa?", None),
        ("2.5", "Các yêu cầu về hiệu năng (ví dụ: tốc độ, độ chính xác…) đã được xác định cho từng chức "
                "năng an toàn chưa?", None),
        ("2.6", "Mức toàn vẹn an toàn (SIL) yêu cầu đã được xác định cho từng chức năng an toàn chưa?", None),
        ("2.7", "Các đầu vào cảm biến đã được xác định về dải đo, độ chính xác, giới hạn nhiễu, băng thông… "
                "chưa?", None),
        ("2.8", "Các đầu ra đã được xác định về dải, độ chính xác, tần suất cập nhật… chưa?", None),
        ("2.9", "Khi hệ bị hỏng, người vận hành có đủ thông tin và phương tiện để nắm quyền điều khiển an "
                "toàn không?", None),
        ("2.10", "Giao diện vận hành đã được xác định về hiển thị dữ liệu, báo động… chưa?", None),
        ("2.11", "Các yêu cầu pháp chế của địa phương hoặc riêng cho ứng dụng đã được xét chưa?", None),
        ("2.12", "Cách thức hoạt động và cách thực hiện việc đặt lại (reset) đã được xác định cho từng đầu "
                 "vào và đầu ra chưa?", None),
        ("2.13", "Cách thức hoạt động của các bypass/ghi đè đã được xác định cho từng đầu vào và đầu ra "
                 "chưa?", None),
        ("2.14", "Đã xét các yếu tố nguyên nhân chung của quá trình chưa (ví dụ: ăn mòn, tắc nghẽn, bám "
                 "cặn…)?", None),
    ]),
    (3, "Thiết kế khái niệm SIS", "Conceptual SIS Design", [
        ("3.1", "Các chức năng an toàn có được xử lý bằng một hệ hoàn toàn tách biệt với hệ điều khiển quá "
                "trình không? Nếu không, biện minh thế nào?", None),
        ("3.2", "Nếu nhiều chức năng cùng được thực hiện trong một bộ xử lý logic, các thành phần dùng chung "
                "có đáp ứng mức SIL cao nhất không?", None),
        ("3.3", "Công nghệ và mức dự phòng đã được chọn cho từng chức năng an toàn chưa? Nếu đã chọn thì "
                "là gì?", None),
        ("3.4", "Khoảng thời gian thử thủ công đã được xác định và biện minh cho từng chức năng an toàn "
                "chưa?", None),
        ("3.5", "Hiệu năng của từng chức năng an toàn đã được phân tích và ghi nhận một cách định lượng để "
                "xem có đạt mức toàn vẹn an toàn (SIL) không chưa? Nếu chưa, cấu hình hệ được biện minh "
                "bằng gì?", None),
        ("3.6", "Đã xác lập tiêu chí “đã được chứng minh trong thực tế” (proven-in-use) cho thiết bị chưa "
                "được chứng nhận chưa?", None),
    ]),
    (4, "Thiết kế chi tiết SIS", "Detailed SIS Design", [
        ("4.1", "Tài liệu thiết kế có nằm dưới một chương trình kiểm soát phiên bản và phát hành chính thức "
                "không?", None),
        ("4.2", "SIL của hệ cuối cùng đã được phân tích và ghi nhận một cách định lượng chưa? Nếu chưa, cấu "
                "hình hệ được biện minh bằng gì?", None),
        ("4.3", "Các giao diện giữa thiết bị hiện trường và bộ xử lý logic đã được xác định phù hợp chưa?", None),
        ("4.4", "Các giao diện truyền thông đã được xác định về giao thức và thông tin trao đổi chưa?", None),
        ("4.5", "Đã có dự phòng cho việc mở rộng trong tương lai chưa?", None),
        ("4.6", "Đã có dự phòng cho việc đưa các thay đổi vào khi thiết kế đang tiến hành chưa?", None),
        ("4.7", "Hệ có an toàn khi hỏng (fail-safe) xét theo các trường hợp sau không?", [
            ("a", "Mất nguồn điện?"),
            ("b", "Mất khí dụng cụ?"),
            ("c", "Sự cố cáp hiện trường?"),
        ]),
        ("4.8", "Hành động của một chức năng phi an toàn có thể làm gián đoạn hoặc phương hại đến chức năng "
                "an toàn nào không?", None),
        ("4.9", "Trạng thái an toàn của từng thành phần trong hệ đã được xác định chưa?", None),
        ("4.10", "Tác động khi từng thành phần trong hệ bị hỏng đã được xét và hành động cần thực hiện đã "
                 "được xác định chưa?", None),
        ("4.11", "Nguồn cấp cho I/O hiện trường có tách riêng khỏi các mạch khác không?", None),
        ("4.12", "Đã tích hợp các bypass ở mức I/O chưa?", None),
        ("4.13", "Khi một bypass đầu vào được bật, vẫn xác định được trạng thái của cảm biến chứ?", None),
        ("4.14", "Có phương tiện báo động về một bypass sau một khoảng thời gian định trước không?", None),
        ("4.15", "Hệ có tích hợp việc đặt lại bằng tay để khởi động lại sản xuất không? Nếu không, biện minh "
                 "thế nào?", None),
    ]),
    (5, "Nguồn điện và nối đất", "Power & Grounding", [
        ("5.1", "Nguồn cấp có phải là điện một chiều (DC) không? Nếu không, biện minh thế nào?", None),
        ("5.2", "Có nguồn điện chính dư thừa không? Nếu không, biện minh thế nào?", None),
        ("5.3", "Tác động của việc mất điện đã được xét chưa?", None),
        ("5.4", "Các vấn đề về nguồn điện sau đã được xử lý chưa?", [
            ("a", "Dải điện áp và dòng điện, kể cả dòng khởi động?"),
            ("b", "Dải tần số?"),
            ("c", "Sóng hài?"),
            ("d", "Tải phi tuyến?"),
            ("e", "Thời gian chuyển đổi nguồn xoay chiều?"),
            ("f", "Bảo vệ quá tải và ngắn mạch?"),
            ("g", "Bảo vệ chống sét?"),
            ("h", "Bảo vệ chống xung nhọn, tăng vọt, sụt áp và nhiễu?"),
            ("i", "Điện áp thấp và điện áp cao?"),
        ]),
        ("5.5", "Các vấn đề về nối đất sau đã được xử lý chưa?", [
            ("a", "Bảo vệ chống ăn mòn?"),
            ("b", "Bảo vệ catốt?"),
            ("c", "Bảo vệ chống tĩnh điện?"),
            ("d", "Nối đất màn chắn?"),
            ("e", "Nối đất thử nghiệm?"),
            ("f", "Nối đất các hàng rào an toàn nội tại?"),
            ("g", "Các kỹ thuật truyền thông cách ly phù hợp (ví dụ: biến áp truyền thông, sợi quang) giữa "
                  "các mặt phẳng đất?"),
        ]),
    ]),
    (6, "Thiết bị hiện trường", "Field Devices", [
        ("6.1", "Đã có thông tin hợp lệ về tần suất hỏng, kiểu hỏng và độ phủ chẩn đoán cho mọi thiết bị "
                "chưa?", None),
        ("6.2", "Nhà cung cấp đã đưa ra khoảng thời gian và quy trình thử thủ công được khuyến nghị chưa?", None),
        ("6.3", "Sẽ có phương tiện để kiểm tra định kỳ các thiết bị nhằm phát hiện hỏng nguy hiểm ẩn không?", None),
        ("6.4", "Các mạch có thường được cấp điện không? Nếu không, có tích hợp giám sát đường dây (mạch có "
                "giám sát) không?", None),
        ("6.5", "Mỗi thiết bị có đường dây riêng không? Nếu không, biện minh thế nào?", None),
        ("6.6", "Nếu dùng cảm biến thông minh, chúng có được bảo vệ chống ghi không?", None),
        ("6.7", "Đã xét cả tải điện tối thiểu lẫn tối đa cho các mạch I/O hiện trường chưa?", None),
        ("6.8", "Có phản hồi để biết phần tử cuối đã chuyển sang trạng thái được lệnh chưa?", None),
        ("6.9", "Vật liệu (gioăng làm kín…) đã được chọn đúng cho ứng dụng cụ thể chưa?", None),
        ("6.10", "Người sử dụng đã có kinh nghiệm hiện trường tốt với các thiết bị này trong những ứng dụng "
                 "khác chưa?", None),
        ("6.11", "Van điện từ có được bảo vệ chống tắc nghẽn, bụi bẩn, côn trùng, đóng băng… không? Đã áp "
                 "dụng những biện pháp nào?", None),
        ("6.12", "Các khía cạnh sau đã được xét cho phần tử cuối chưa?", [
            ("a", "Tốc độ mở và đóng?"),
            ("b", "Chênh áp khi đóng kín?"),
            ("c", "Độ rò?"),
            ("d", "Khả năng chịu lửa của thân van, bộ chấp hành và đường xung?"),
        ]),
        ("6.13", "Các thiết bị hiện trường trọng yếu về an toàn có được nhận diện theo cách riêng (ví dụ: "
                 "mã màu, nhãn) không?", None),
    ]),
    (7, "Giao diện vận hành", "Operator Interface", [
        ("7.1", "Đã xét trường hợp hỏng (mất) giao diện chưa?", None),
        ("7.2", "Có phương tiện thay thế để đưa quá trình về trạng thái an toàn không?", None),
        ("7.3", "Các thông tin sau có được hiển thị trên giao diện không?", [
            ("a", "Quá trình đang ở bước nào trong một trình tự?"),
            ("b", "Dấu hiệu cho biết một hành động của SIS đã xảy ra?"),
            ("c", "Dấu hiệu cho biết một chức năng của SIS đang bị bypass?"),
            ("d", "Dấu hiệu cho biết một thành phần hay phân hệ của SIS đã hỏng hoặc đang ở trạng thái suy "
                  "giảm?"),
            ("e", "Trạng thái của các thiết bị hiện trường?"),
        ]),
        ("7.4", "Thời gian cập nhật có phù hợp với ứng dụng trong điều kiện khẩn cấp không?", None),
        ("7.5", "Người vận hành đã được kiểm tra mù màu chưa?", None),
        ("7.6", "Có thể thay đổi logic chương trình của SIS từ giao diện vận hành không?", None),
        ("7.7", "Các tham số có thể thay đổi có được bảo vệ bằng quyền truy cập an ninh không?", None),
    ]),
    (8, "Giao diện bảo trì/kỹ thuật", "Maintenance/Engineering Interface", [
        ("8.1", "Hỏng giao diện này có thể ảnh hưởng xấu tới SIS không?", None),
        ("8.2", "Mức an ninh truy cập đã đủ chưa? Dùng những phương thức nào?", None),
        ("8.3", "Giao diện bảo trì/kỹ thuật có được dùng làm giao diện vận hành không?", None),
        ("8.4", "Giao diện bảo trì/kỹ thuật có được ngắt ra trong khi hệ đang vận hành bình thường không?", None),
    ]),
    (9, "Truyền thông", "Communications", [
        ("9.1", "Hỏng truyền thông có thể ảnh hưởng xấu tới SIS không?", None),
        ("9.2", "Tín hiệu truyền thông có được cách ly khỏi các nguồn năng lượng khác không?", None),
        ("9.3", "Đã thực hiện bảo vệ chống ghi để các hệ bên ngoài không thể làm hỏng bộ nhớ của SIS chưa? "
                "Nếu chưa, vì sao?", None),
        ("9.4", "Các giao diện có đủ vững để chịu được nhiễu điện từ/tần số vô tuyến (EMI/RFI) và các nhiễu "
                "loạn nguồn không?", None),
    ]),
    (10, "Đặc tả phần cứng", "Hardware Specification", [
        ("10.1", "Môi trường vận hành thực tế đã được xác định và đã đặt ra các chỉ tiêu phù hợp cho những "
                 "yếu tố sau chưa?", [
            ("a", "Dải nhiệt độ?"),
            ("b", "Độ ẩm?"),
            ("c", "Rung và xóc?"),
            ("d", "Sự xâm nhập của bụi và/hoặc nước?"),
            ("e", "Khí ăn mòn?"),
            ("f", "Khí quyển nguy hiểm cháy nổ?"),
            ("g", "Dung sai điện áp nguồn cấp?"),
            ("h", "Gián đoạn nguồn cấp?"),
            ("i", "Nhiễu điện?"),
            ("j", "Bức xạ ion hoá?"),
        ]),
        ("10.2", "Kiểu hỏng của mọi thành phần đã được biết chưa?", None),
        ("10.3", "Nhà cung cấp đã cung cấp tần suất hỏng an toàn và hỏng nguy hiểm của hệ một cách định "
                 "lượng, kèm các giả định và dữ liệu thành phần đã dùng, chưa?", None),
        ("10.4", "Nhà cung cấp đã cung cấp các giá trị độ phủ chẩn đoán cho hệ của họ chưa?", None),
        ("10.5", "Các thành phần của hệ logic (mô-đun I/O, CPU, mô-đun truyền thông…) có cùng một nhà cung "
                 "cấp không?", None),
        ("10.6", "Hành động phát sinh khi cấp lại điện cho hệ đã được xét chưa?", None),
        ("10.7", "Mọi mô-đun I/O có được bảo vệ chống xung điện áp không?", None),
        ("10.8", "Nếu đang xét các thiết bị hoặc hệ dư thừa, đã có biện pháp giảm thiểu các vấn đề nguyên "
                 "nhân chung tiềm ẩn chưa? Nếu có thì là những biện pháp nào?", None),
    ]),
    (11, "Chế tạo phần cứng", "Hardware Manufacture", [
        ("11.1", "Nhà cung cấp có thể đưa ra bằng chứng về một đánh giá an toàn độc lập cho phần cứng "
                 "không?", None),
        ("11.2", "Nhà cung cấp có duy trì một chương trình kiểm soát phiên bản và phát hành chính thức "
                 "không?", None),
        ("11.3", "Trên phần cứng có chỉ dẫn nhìn thấy được về số phiên bản không?", None),
        ("11.4", "Nhà cung cấp có đặc tả và quy trình về chất lượng vật liệu, tay nghề và kiểm tra không?", None),
        ("11.5", "Đã có biện pháp phòng ngừa thoả đáng để tránh hư hỏng do phóng tĩnh điện chưa?", None),
    ]),
    (12, "Yêu cầu logic ứng dụng", "Application Logic Requirements", [
        ("12.1", "Mọi bên có một chương trình kiểm soát phiên bản và phát hành chính thức cho logic ứng "
                 "dụng không?", None),
        ("12.2", "Logic có được viết rõ ràng, không mập mờ và mọi bên đều hiểu được không?", None),
        ("12.3", "Chương trình có kèm chú thích không?", None),
        ("12.4", "Trong đặc tả logic, đã có phát biểu rõ ràng và súc tích về những điểm sau chưa?", [
            ("a", "Từng chức năng liên quan đến an toàn?"),
            ("b", "Thông tin cần đưa cho người vận hành?"),
            ("c", "Hành động yêu cầu của từng lệnh của người vận hành, kể cả các lệnh không hợp lệ hoặc "
                  "ngoài dự kiến?"),
            ("d", "Các yêu cầu truyền thông giữa SIS và các thiết bị khác?"),
            ("e", "Trạng thái ban đầu của mọi biến nội và mọi giao diện bên ngoài?"),
            ("f", "Hành động yêu cầu đối với các biến nằm ngoài dải?"),
        ]),
    ]),
    (13, "Phần mềm nhúng (của nhà cung cấp)", "Embedded (Vendor) Software", [
        ("13.1", "Nhà cung cấp có thể đưa ra bằng chứng về một đánh giá an toàn độc lập cho toàn bộ phần mềm "
                 "nhúng không?", None),
        ("13.2", "Phần mềm ấy đã được dùng trong những ứng dụng tương tự trong một thời gian đủ dài chưa?", None),
        ("13.3", "Phần mềm của nhà cung cấp có được ghi liệu đầy đủ để người sử dụng hiểu được cách nó hoạt "
                 "động và cách thực hiện chức năng mong muốn không?", None),
        ("13.4", "Kết quả của các phép toán bất thường có được ghi liệu đầy đủ không?", None),
        ("13.5", "Có quy trình kiểm soát các phiên bản phần mềm đang dùng và cập nhật cho mọi hệ tương tự "
                 "không?", None),
        ("13.6", "Với phụ tùng có chứa firmware, có quy trình bảo đảm mọi mô-đun tương thích với nhau "
                 "không?", None),
        ("13.7", "Có thể kiểm tra các phiên bản phần mềm đang dùng một cách dễ dàng không?", None),
        ("13.8", "Nếu phát hiện lỗi trong phần mềm nhúng, lỗi có được báo cho nhà cung cấp và được họ sửa, "
                 "rồi chỉ được đưa vào SIS sau khi đã kiểm tra và thử nghiệm đoạn mã đã sửa không?", None),
        ("13.9", "Nhà chế tạo có cung cấp hỗ trợ kỹ thuật có năng lực không?", None),
    ]),
    (14, "Viết mã phần mềm", "Software Coding", [
        ("14.1", "Có tiêu chuẩn và quy trình cho việc viết mã phần mềm không?", None),
        ("14.2", "Có quy trình ghi nhận và khắc phục mọi thiếu sót trong đặc tả hoặc trong thiết kế được "
                 "phát hiện ở giai đoạn viết mã không?", None),
        ("14.3", "Những chỗ lệch khỏi yêu cầu thiết kế hoặc bổ sung so với yêu cầu thiết kế có được ghi "
                 "nhận không?", None),
        ("14.4", "Có dùng một ngôn ngữ hình thức hoặc phương tiện nào khác để bảo đảm chương trình vừa chính "
                 "xác vừa không mập mờ không?", None),
        ("14.5", "Có quy trình tạo và duy trì tài liệu đầy đủ không?", None),
        ("14.6", "Ngôn ngữ lập trình có khuyến khích dùng các mô-đun nhỏ và dễ quản lý không?", None),
        ("14.7", "Mã có kèm chú thích đầy đủ không?", None),
        ("14.8", "Có thực hiện xem xét thiết kế trong quá trình phát triển chương trình, với sự tham gia "
                 "của người sử dụng, người thiết kế và người lập trình không?", None),
        ("14.9", "Phần mềm có đủ các phương tiện phát hiện lỗi gắn với việc khoanh vùng lỗi, phục hồi hoặc "
                 "dừng an toàn không?", None),
        ("14.10", "Mọi chức năng có thử nghiệm được không?", None),
        ("14.11", "Mã cuối cùng có được kiểm tra đối chiếu với các yêu cầu bởi những người không phải là "
                  "người viết mã không?", None),
        ("14.12", "Có dùng một trình biên dịch/trình hợp dịch đã được khẳng định không?", None),
        ("14.13", "Trình biên dịch/trình hợp dịch có được chứng nhận theo các tiêu chuẩn được công nhận "
                  "không?", None),
    ]),
    (15, "Thử nghiệm tại nhà máy", "Factory Test", [
        ("15.1", "Có quy trình thử nghiệm hệ đã hoàn thiện không?", None),
        ("15.2", "Kết quả thử nghiệm có được lưu hồ sơ không?", None),
        ("15.3", "Có quy trình ghi nhận và khắc phục mọi thiếu sót trong đặc tả, thiết kế hoặc lập trình "
                 "được phát hiện trong khi thử nghiệm không?", None),
        ("15.4", "Việc thử nghiệm có do những người không phải là người viết mã thực hiện không?", None),
        ("15.5", "Phần mềm có được thử nghiệm trên chính hệ đích thay vì trên hệ mô phỏng không?", None),
        ("15.6", "Từng luồng điều khiển hoặc từng nhánh logic có được thử nghiệm không?", None),
        ("15.7", "Các phép toán số học có được thử với giá trị nhỏ nhất và lớn nhất để bảo đảm không xảy ra "
                 "tràn không?", None),
        ("15.8", "Có các bài thử mô phỏng cả trường hợp ngoại lệ lẫn điều kiện bình thường không?", None),
        ("15.9", "Mọi hạng mục sau đã được thử nghiệm chưa?", [
            ("a", "Sự phụ thuộc vào các hệ/giao diện khác"),
            ("b", "Cấu hình bộ xử lý logic"),
            ("c", "Hoạt động của các bypass"),
            ("d", "Hoạt động của các lệnh đặt lại"),
            ("e", "Toàn bộ logic chức năng"),
        ]),
    ]),
    (16, "Lắp đặt và chạy thử", "Installation & Commissioning", [
        ("16.1", "Nhân sự đã được đào tạo phù hợp chưa?", None),
        ("16.2", "Mức độ độc lập giữa người thực hiện công việc và người kiểm tra công việc ấy đã đủ chưa?", None),
        ("16.3", "Đã có biện pháp phòng ngừa thoả đáng cho việc bảo quản vật tư trong thời gian lắp đặt "
                 "chưa?", None),
        ("16.4", "Quy trình lắp đặt cho mọi thiết bị có đủ chi tiết để không phải để lại những diễn giải hay "
                 "quyết định quan trọng cho nhân viên lắp đặt không?", None),
        ("16.5", "SIS đã được kiểm tra để phát hiện mọi hư hỏng do quá trình lắp đặt gây ra chưa?", None),
        ("16.6", "Các hạng mục như tủ, hộp đấu nối và cáp có được bảo vệ khỏi những yếu tố sau không?", [
            ("a", "Rò hơi nước?"),
            ("b", "Rò nước?"),
            ("c", "Rò dầu?"),
            ("d", "Nguồn nhiệt?"),
            ("e", "Hư hỏng cơ học?"),
            ("f", "Ăn mòn (ví dụ: dòng chất quá trình từ cảm biến hỏng chảy tới hộp đấu nối, tủ logic hoặc "
                  "phòng điều khiển)?"),
            ("g", "Khí quyển cháy nổ?"),
        ]),
        ("16.7", "Các hệ liên quan đến an toàn có được nhận diện rõ ràng để tránh bị can thiệp vô ý không?", None),
        ("16.8", "Hoạt động đúng của những hạng mục sau đã được xác nhận chưa?", [
            ("a", "Việc lắp đặt thiết bị và đi dây đúng?"),
            ("b", "Các nguồn năng lượng đang hoạt động?"),
            ("c", "Mọi thiết bị hiện trường đã được hiệu chuẩn?"),
            ("d", "Mọi thiết bị hiện trường đang hoạt động?"),
            ("e", "Bộ xử lý logic đang hoạt động?"),
            ("f", "Truyền thông với các hệ khác?"),
            ("g", "Hoạt động và chỉ báo của các bypass?"),
            ("h", "Hoạt động của các lệnh đặt lại?"),
            ("i", "Hoạt động của các lệnh dừng bằng tay?"),
        ]),
        ("16.9", "Tài liệu có khớp với thực tế lắp đặt không?", None),
        ("16.10", "Có tài liệu thể hiện những điểm sau không?", [
            ("a", "Nhận diện hệ đang được chạy thử?"),
            ("b", "Xác nhận rằng việc chạy thử đã hoàn thành tốt?"),
            ("c", "Ngày hệ được chạy thử?"),
            ("d", "Các quy trình đã dùng để chạy thử hệ?"),
            ("e", "Chữ ký có thẩm quyền xác nhận hệ đã được chạy thử thành công?"),
        ]),
    ]),
    (17, "Vận hành và bảo trì", "Operations & Maintenance", [
        ("17.1", "Nhân viên đã được đào tạo đầy đủ về quy trình vận hành và bảo trì hệ chưa?", None),
        ("17.2", "Quy trình vận hành có được ghi liệu đầy đủ không?", None),
        ("17.3", "Có sách hướng dẫn dành cho người sử dụng/người vận hành/nhân viên bảo trì không?", None),
        ("17.4", "Sách hướng dẫn có mô tả những điểm sau không?", [
            ("a", "Các giới hạn vận hành an toàn và hệ quả khi vượt qua chúng?"),
            ("b", "Cách hệ đưa quá trình về trạng thái an toàn?"),
            ("c", "Rủi ro gắn với các hỏng hóc của hệ và hành động cần làm ứng với từng loại hỏng?"),
        ]),
        ("17.5", "Có phương tiện chỉ cho phép người có thẩm quyền truy cập không?", None),
        ("17.6", "Mọi thiết đặt vận hành có thể được kiểm tra dễ dàng để bảo đảm luôn đúng không?", None),
        ("17.7", "Có phương tiện giới hạn dải của các giá trị đặt ngưỡng cắt không?", None),
        ("17.8", "Đã có phương tiện thoả đáng để bypass các chức năng an toàn chưa?", None),
        ("17.9", "Khi các chức năng bị bypass, chúng có được chỉ báo rõ ràng không?", None),
        ("17.10", "Đã có quy trình được ghi liệu để kiểm soát việc đặt và gỡ bypass chưa?", None),
        ("17.11", "Đã có quy trình được ghi liệu để bảo đảm an toàn cho nhà máy trong khi bảo trì SIS chưa?", None),
        ("17.12", "Quy trình bảo trì có đủ chi tiết để không phải để lại những diễn giải hay quyết định quan "
                  "trọng cho nhân viên bảo trì không?", None),
        ("17.13", "Hoạt động và lịch bảo trì đã được xác định cho mọi phần của hệ chưa?", None),
        ("17.14", "Các quy trình có được xem xét định kỳ không?", None),
        ("17.15", "Đã có quy trình ngăn ngừa việc can thiệp trái phép chưa?", None),
        ("17.16", "Có phương tiện để xác minh rằng việc sửa chữa được thực hiện trong khoảng thời gian đúng "
                  "như đã giả định trong đánh giá an toàn không?", None),
        ("17.17", "Đã có quy trình bảo trì và vận hành nhằm giảm thiểu việc tạo ra các vấn đề nguyên nhân "
                  "chung tiềm ẩn chưa?", None),
        ("17.18", "Tài liệu có khớp với quy trình bảo trì và vận hành thực tế không?", None),
    ]),
    (18, "Thử nghiệm", "Testing", [
        ("18.1", "Đã có quy định và quy trình được ghi liệu cho phép thử nghiệm chứng minh (proof test) mọi "
                 "chức năng an toàn, kể cả thiết bị hiện trường, chưa?", None),
        ("18.2", "Quy trình thử nghiệm có đủ chi tiết để không phải để lại những diễn giải hay quyết định "
                 "quan trọng cho nhân viên bảo trì không?", None),
        ("18.3", "Cơ sở để chọn khoảng thời gian thử định kỳ đã được ghi liệu chưa?", None),
        ("18.4", "Những hạng mục sau có được thử nghiệm không?", [
            ("a", "Đường xung?"),
            ("b", "Các thiết bị cảm biến?"),
            ("c", "Logic ứng dụng, các phép tính và/hoặc các trình tự?"),
            ("d", "Các điểm đặt ngưỡng cắt?"),
            ("e", "Các chức năng báo động?"),
            ("f", "Tốc độ đáp ứng?"),
            ("g", "Các phần tử cuối?"),
            ("h", "Các lệnh cắt bằng tay?"),
            ("i", "Các chức năng chẩn đoán?"),
        ]),
        ("18.5", "Có hệ thống báo cáo sự cố không?", None),
        ("18.6", "Đã có quy trình so sánh hiệu năng thực tế với hiệu năng dự đoán hoặc yêu cầu chưa?", None),
        ("18.7", "Đã có quy trình được ghi liệu để khắc phục mọi thiếu sót phát hiện được chưa?", None),
        ("18.8", "Việc hiệu chuẩn thiết bị thử nghiệm có được xác minh không?", None),
        ("18.9", "Hồ sơ thử nghiệm có được lưu giữ không?", None),
        ("18.10", "Hồ sơ thử nghiệm có thể hiện những điểm sau không?", [
            ("a", "Ngày kiểm tra/thử nghiệm?"),
            ("b", "Tên người thực hiện thử nghiệm?"),
            ("c", "Nhận diện thiết bị được thử?"),
            ("d", "Kết quả thử nghiệm?"),
        ]),
        ("18.11", "Đã có quy trình thử nghiệm nhằm giảm thiểu việc tạo ra các vấn đề nguyên nhân chung tiềm "
                  "ẩn chưa?", None),
        ("18.12", "Dữ liệu tần suất hỏng có được xem xét định kỳ và so sánh với dữ liệu đã dùng khi thiết "
                  "kế/phân tích hệ không?", None),
    ]),
    (19, "Quản lý thay đổi", "Management of Change", [
        ("19.1", "Đã có quy trình phê duyệt xét tới hệ quả an toàn của mọi sửa đổi, bao gồm những điểm sau "
                 "chưa?", [
            ("a", "Cơ sở kỹ thuật của thay đổi?"),
            ("b", "Tác động lên an toàn và sức khoẻ?"),
            ("c", "Tác động lên quy trình vận hành/bảo trì?"),
            ("d", "Thời gian cần thiết?"),
            ("e", "Ảnh hưởng lên thời gian đáp ứng?"),
        ]),
        ("19.2", "Đã có quy trình xác định mức xem xét/phê duyệt cần thiết tuỳ theo bản chất của thay đổi "
                 "chưa?", None),
        ("19.3", "Thay đổi được đề xuất có khởi động việc quay lại đúng pha của vòng đời không?", None),
        ("19.4", "Tài liệu của dự án (ví dụ: quy trình vận hành, thử nghiệm, bảo trì…) đã được sửa để phản "
                 "ánh thay đổi chưa?", None),
        ("19.5", "Toàn bộ hệ đã được thử nghiệm sau khi đưa thay đổi vào, và kết quả đã được ghi liệu chưa?", None),
        ("19.6", "Đã có quy trình được ghi liệu để xác minh rằng các thay đổi đã được hoàn thành thoả đáng "
                 "chưa?", None),
        ("19.7", "Mọi bộ phận bị ảnh hưởng đã được thông báo về thay đổi chưa?", None),
        ("19.8", "Việc truy cập phần cứng và phần mềm có bị giới hạn cho người có thẩm quyền và có năng lực "
                 "không?", None),
        ("19.9", "Việc truy cập tài liệu dự án có bị giới hạn cho người có thẩm quyền không?", None),
        ("19.10", "Tài liệu dự án có chịu sự kiểm soát phiên bản phù hợp không?", None),
        ("19.11", "Hệ quả của việc đưa vào các phiên bản phần mềm mới đã được xét chưa?", None),
    ]),
    (20, "Ngừng vận hành", "Decommissioning", [
        ("20.1", "Quy trình quản lý thay đổi có được tuân thủ cho các hoạt động ngừng vận hành không?", None),
        ("20.2", "Tác động lên các phân xưởng và cơ sở lân cận đang vận hành đã được đánh giá chưa?", None),
        ("20.3", "Đã có quy trình duy trì an toàn cho quá trình trong suốt thời gian ngừng vận hành chưa?", None),
        ("20.4", "Đã có quy trình xác định mức thẩm quyền cần thiết cho việc ngừng vận hành chưa?", None),
    ]),
]


def _section(num, tvi, items):
    rows = []
    for no, stem, subs in items:
        if subs:
            rows.append([no, stem, ""])
            for letter, txt in subs:
                rows.append(["", '<span style="display:inline-block;padding-left:1.6rem">%s) %s'
                             '</span>' % (letter, txt), YES])
        else:
            rows.append([no, stem, YES])
    return table(["Số", "Hạng mục", "Lựa chọn"], rows, cls="tbl chk")


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Cách dùng chương này.</b> Đây không phải một chương để đọc từ đầu tới cuối, mà là một "
            "danh sách để làm. Mỗi dòng là một câu hỏi; cột cuối là ba lựa chọn <em>Y</em> (có), <em>N</em> "
            "(không) và <em>N/A</em> (không áp dụng). Trong bản in, cột ấy là ba ô để khoanh tròn; ở đây "
            "được gộp lại thành một ô. · "
            "<em>SRS</em> — đặc tả yêu cầu an toàn. · "
            "<em>Proven-in-use</em> — đã được chứng minh trong thực tế: tiêu chí thay thế cho chứng nhận "
            "khi dùng thiết bị chưa được chứng nhận. · "
            "<em>Proof test</em> — thử nghiệm chứng minh, thử nghiệm định kỳ để phát hiện hỏng nguy hiểm ẩn. · "
            "<em>Chẩn đoán (diagnostics)</em> — khả năng tự phát hiện hỏng của hệ.")
    return note(
        "<b>How to use this chapter.</b> This is not a chapter to read from end to end; it is a list to "
        "work through. Every line is a question, and the last column offers three answers: <em>Y</em>, "
        "<em>N</em> and <em>N/A</em>. In the printed book that column is three boxes to circle; here it is "
        "collapsed into one cell. · <em>SRS</em> — safety requirements specification. · "
        "<em>Proven-in-use</em> — the route to acceptance for equipment that carries no certificate. · "
        "<em>Proof test</em> — the periodic test that reveals hidden dangerous failures. · "
        "<em>Diagnostics</em> — the system's own ability to detect its failures.")


def body_vi():
    b = []
    b.append(lead(
        "Một danh sách kiểm tra tự nó không làm hệ an toàn hơn — cũng như một nghiên cứu HAZOP mà không ai "
        "làm theo khuyến nghị nào thì không làm nhà máy an toàn hơn. Giá trị của nó nằm ở chỗ: nếu ai đó "
        "thực sự đi qua từng dòng, thì những việc thường bị bỏ quên sẽ không bị bỏ quên."))

    b.append(h2("Giới thiệu", "Introduction"))
    b.append(p("Việc dùng một danh sách kiểm tra tự nó sẽ không dẫn tới những hệ an toàn hơn, cũng như việc "
               "thực hiện một nghiên cứu mối nguy và khả năng vận hành (HAZOP) mà không làm theo bất kỳ "
               "khuyến nghị nào sẽ không dẫn tới một cơ sở an toàn hơn. Chỉ khi tuân theo các quy trình "
               "được nêu trong danh sách — vốn dựa trên tiêu chuẩn ngành và kiến thức tích luỹ (phần nhiều "
               "được học theo cách “đắt giá”) — thì mới có thể có được những hệ an toàn hơn. Danh sách kiểm "
               "tra này là một nỗ lực liệt kê càng nhiều quy trình và thông lệ phổ biến càng tốt, với hy "
               "vọng rằng nhờ xem xét có hệ thống toàn bộ quá trình thiết kế, sẽ không có việc gì rơi qua "
               "khe hở của một tổ chức và bị lãng quên."))
    b.append(p("Danh sách này gồm nhiều phần khác nhau, mỗi phần tương ứng với một phần của vòng đời an "
               "toàn như mô tả trong các tiêu chuẩn. Những phần khác nhau nhắm tới những nhóm khác nhau "
               "tham gia vào thiết kế tổng thể hệ thống, từ người sử dụng, nhà thầu, nhà cung cấp cho tới "
               "đơn vị tích hợp hệ thống. Ai chịu trách nhiệm gì có thể thay đổi theo từng dự án. Vì vậy, "
               "danh sách này không quy định ai chịu trách nhiệm gì; nó chỉ tóm tắt các hạng mục trong từng "
               "bước của vòng đời."))
    b.append(p("Vậy tại sao phải bận tâm? Cơ quan An toàn và Sức khoẻ lao động Anh (HSE) đã xem xét và công "
               "bố kết quả của 34 vụ tai nạn là hậu quả trực tiếp của việc hệ điều khiển và hệ an toàn bị "
               "hỏng. Kết quả được tóm tắt ở Hình 15-1. Bốn mươi bốn phần trăm số vụ là do đặc tả sai và "
               "thiếu (cả đặc tả chức năng lẫn đặc tả mức toàn vẹn), và 20 % là do những thay đổi được thực "
               "hiện sau khi chạy thử. Có thể thấy rõ rằng phần lớn những vấn đề ấy nằm ở phía hoạt động của "
               "người sử dụng. (Nhìn lại thì bao giờ cũng sáng tỏ; nhìn trước thì khó hơn một chút.) Các "
               "tiêu chuẩn ngành cũng như danh sách này cố gắng bao quát mọi vấn đề, chứ không chỉ tập trung "
               "vào một lĩnh vực riêng nào."))
    b.append(fig(1, F.fig_15_1(), "vi"))
    b.append(p("Danh sách này không nên được coi là cuối cùng hay đầy đủ. Khi người khác xem xét và sử dụng, "
               "họ được khuyến khích bổ sung vào đó (vì lợi ích của những người có thể dùng nó sau này). "
               "Thực tế, mỗi phần đều bắt đầu ở một trang mới, để dành đủ chỗ cho những bổ sung và góp ý "
               "của bạn."))

    b.append(h2("Tổng quan", "Overview"))
    b.append(p("Danh sách này bao gồm các bước sau:"))
    b.append(ul([
        "Yêu cầu quản lý",
        "Đặc tả yêu cầu an toàn (SRS)",
        "Thiết kế khái niệm SIS",
        "Thiết kế chi tiết SIS",
        "Nguồn điện và nối đất",
        "Thiết bị hiện trường",
        "Giao diện vận hành",
        "Giao diện bảo trì/kỹ thuật",
        "Truyền thông",
        "Đặc tả phần cứng",
        "Chế tạo phần cứng",
        "Yêu cầu logic ứng dụng",
        "Phần mềm nhúng (của nhà cung cấp)",
        "Viết mã phần mềm",
        "Thử nghiệm tại nhà máy",
        "Lắp đặt và chạy thử",
        "Vận hành và bảo trì",
        "Thử nghiệm",
        "Quản lý thay đổi",
        "Ngừng vận hành",
    ]))

    for num, tvi, ten, items in SECTIONS:
        b.append(h3("Phần %d: %s" % (num, tvi), "Section %d: %s" % (num, ten)))
        b.append(_section(num, tvi, items))

    b.append(note(
        "<b>Ba điểm lưu ý khi dùng bản dịch này.</b><br>"
        "<b>(1) Cột “Comments” đã được bỏ.</b> Trong bản in, mỗi bảng có bốn cột: số thứ tự, hạng mục, ba ô "
        "để khoanh tròn (Y/N/N/A) và một cột “Comments” để trống cho người dùng ghi. Cột trống ấy không "
        "mang nội dung nào của tác giả, và chiếm gần một phần ba chiều rộng; bản dịch bỏ nó để bảng đọc "
        "được trên màn hình. Nếu in ra để điền tay, nên kẻ thêm cột ấy.<br>"
        "<b>(2) Ba ô Y/N/N/A được gộp thành một ô.</b> Bản in dành ba cột riêng cho ba lựa chọn; ở đây "
        "chúng được viết liền thành “Y · N · N/A” để bảng không bị vỡ trên màn hình hẹp.<br>"
        "<b>(3) Các câu hỏi con được tách thành dòng riêng.</b> Những hạng mục có các ý a), b), c)… trong "
        "bản in cũng là những dòng riêng, mỗi dòng có ô Y/N/N/A riêng; hạng mục mẹ thì để trống ô ấy, đúng "
        "như bản in. Số thứ tự và nội dung câu hỏi giữ nguyên, không rút gọn."))

    b.append(refs([
        "Gruhn, Paul, và Harry Cheddie. <em>Safety Instrumented Systems: Design, Analysis, and "
        "Justification</em>. Ấn bản thứ hai. ISA, 2006. — Chính chương này, cùng các chương 6, 8 và 14 đã "
        "dẫn tới danh sách trên.",
        "Health and Safety Executive (U.K.). <em>Out of Control: Why Control Systems Go Wrong and How to "
        "Prevent Failure</em>. HSE Books, 2003. — Nguồn của số liệu trong Hình 15-1.",
        "IEC 61511-1. <em>Functional Safety — Safety Instrumented Systems for the Process Industry "
        "Sector</em>. Phần 1: Khung, định nghĩa, yêu cầu hệ thống, phần cứng và phần mềm ứng dụng. "
        "IEC, 2003. — Cấu trúc các pha mà danh sách này bám theo.",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(p("This chapter is a checklist, and a checklist is a strange thing to translate. It has no "
               "argument, no worked example, no narrative. It has 179 questions arranged in twenty groups, "
               "and its value depends entirely on somebody actually answering them."))
    b.append(p("So the useful English companion is not a summary of the questions. It is an answer to the "
               "question the checklist itself raises and does not answer: why does a list of questions "
               "prevent accidents at all?"))

    b.append(h2("A checklist is a memory, not a method"))
    b.append(p("The chapter opens with the honest disclaimer: a checklist does not make a system safer, "
               "any more than a HAZOP makes a plant safer if nobody implements the recommendations. That "
               "sounds like modesty, but it is precise. A checklist has no power to change anything. It "
               "has only the power to remind."))
    b.append(p("Which means its value is exactly the value of the things people forget. And Figure 15-1 "
               "tells you what those things are. Of 34 accidents caused by control and safety system "
               "failures, 44 percent traced back to incorrect or incomplete specifications and 20 percent "
               "to changes made after commissioning. Sixty-four percent. Nearly two thirds of the failures "
               "happened before the equipment was ever stressed, in documents and decisions."))
    b.append(fig(1, F.fig_15_1(), "en"))

    b.append(h2("The two failure modes this checklist actually targets"))
    b.append(p("Those two numbers are not equally distributed across the twenty sections. Sections 1 to 4 "
               "— management, SRS, conceptual design, detailed design — are the 44 percent. Section 19, "
               "management of change, is the 20 percent. Everything else, all sixteen remaining sections, "
               "addresses the 36 percent that is left."))
    b.append(p("That distribution should change how the list is used. A project that works through sections "
               "5 to 18 thoroughly and skips the front matter has done the easy 36 percent and left the "
               "hard 64 percent undone. And it is easy to see why: sections 5 to 18 have answers that are "
               "checkable — is the power supply redundant, are the field devices calibrated, is there a "
               "fault reporting system. Sections 1 to 4 have answers that are judgements — is the "
               "specification complete, is the hazard assessment systematic, is the safe state defined for "
               "every operating state."))
    b.append(p("A judgement cannot be ticked. That is the whole difficulty, and it is why the specification "
               "failure keeps recurring across decades of accident reports."))

    b.append(h2("Why \"N/A\" is the most dangerous column"))
    b.append(p("Three options are offered for every line: yes, no, not applicable. The first two are "
               "honest. The third is where a checklist quietly dies, because \"not applicable\" is the "
               "answer that requires no work and provokes no argument."))
    b.append(p("Some lines genuinely are N/A — a pneumatic logic system has no software coding section. But "
               "the pattern to watch for is a section where every line is N/A. That is rarely a fact about "
               "the system. It is usually a fact about the person filling it in: nobody on the team owned "
               "that phase, so nobody could answer, so the whole section was closed with N/A and the "
               "project moved on. Item 1.1 asks whether the responsible persons have been identified, and "
               "if the answer to that is no, then the N/As further down are not answers at all."))
    b.append(p("A useful discipline: require a one-line justification for every N/A, exactly as item 3.1 "
               "does for its own question (\"If not, what is the justification?\"). The book asks that "
               "question in about a dozen places. It could profitably ask it everywhere."))

    b.append(h2("The questions that are really one question"))
    b.append(p("Read across the twenty sections and one theme repeats in almost every one: has somebody "
               "other than the person who did the work checked the work?"))
    b.append(p("Item 15.4 asks whether testing is carried out by persons other than those producing the "
               "code. Item 14.11 asks whether the final code is checked against requirements by persons "
               "other than those who wrote it. Item 16.2 asks about independence between those carrying "
               "out the work and those inspecting it. Item 18.4 through 18.10 ask whether tests happen, "
               "whether they are recorded, and who conducted them."))
    b.append(p("That is not bureaucratic duplication. It is the recognition that the person who wrote the "
               "logic is the worst possible person to confirm that the logic does what the specification "
               "said, because they will test what they meant rather than what they wrote. Chapter 13 makes "
               "the same point about MOC checkout with a specific instruction to use a separate crew. The "
               "checklist generalises it: independence is not a virtue, it is a control."))

    b.append(h2("How to use it without pretending"))
    b.append(p("Three practical notes for anyone who actually runs this list on a project."))
    b.append(ol([
        "Answer sections 1 to 4 first, and do not let them be answered by the same person who will later "
        "be measured on the schedule. They are the 44 percent, and they are the sections most likely to "
        "be compressed when the project is late — which is exactly when compressing them does the most "
        "damage.",
        "Treat section 19 as a living control, not a one-time answer. The 20 percent of accidents that "
        "came from post-commissioning changes did not come from changes that were reviewed and rejected; "
        "they came from changes that were never put through the process at all.",
        "Keep the completed list. It is the only document that records what the project believed about "
        "itself at the time, and it is the first thing an investigator will ask for after an incident. A "
        "list with honest N's in it is worth more than a list with all Y's, because the N's are where the "
        "risk actually was.",
    ]))
    b.append(p("And a closing observation about the checklist's own claim that it is not final or complete. "
               "That is not false modesty either. The twenty sections map onto a lifecycle that assumes a "
               "conventional project: specify, design, build, install, operate. Projects that do not look "
               "like that — a software update to a twenty-year-old SIS, a change of feedstock, a plant "
               "mothballed and restarted — will find sections that do not fit and will have to invent the "
               "questions. The list gives you the habit; it cannot give you the answers."))
    return "".join(b)
