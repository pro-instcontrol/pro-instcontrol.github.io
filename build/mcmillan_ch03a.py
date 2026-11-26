# -*- coding: utf-8 -*-
"""Chapter 3, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 43-50 (PDF pp. 64-71).

Covers the chapter opening, 3.1/3.1.1-3.1.4, 3.2/3.2.1-3.2.2 and the
opening of 3.3 through Table 3.1. Section 3.3.1 belongs to the next
module. The integration module owns PAGES_SRC, refs, note_terms, the
end note and the copyright line.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, lead, p, note, ul, fig, table

_T31_HEAD_VI = ["Số nguồn nguy hiểm", "Số nguồn phát thải đồng thời"]
_T31_HEAD_EN = ["Number of sources of hazard", "Number releasing simultaneously"]
_T31_ROWS = [
    ["1", "1"],
    ["2", "2"],
    ["3–5", "3"],
    ["6–9", "4"],
    ["10–13", "5"],
    ["14–18", "6"],
    ["19–23", "7"],
    ["24–28", "8"],
    ["29–33", "9"],
    ["34–39", "10"],
    ["40–45", "11"],
    ["46–51", "12"],
]


def body_vi():
    b = []
    b.append(h2("3 — Thực hành phân loại khu vực đối với khí, hơi và sương mù "
                "trong tình huống thông gió tự nhiên",
                "3 — Area classification practice for gases, vapours and mists "
                "in freely ventilated situations"))
    b.append(lead("Từ nguyên lý đến phạm vi khu vực nguy hiểm"))
    b.append(p("Chương 2 đã xem xét các cơ chế phân loại khu vực, thành phần của "
               "nhóm thực hiện và thông tin chi tiết cần có để lập phân loại. Chương "
               "này chuyển sang việc lập phân loại thực tế cho một nhà máy hoặc cơ "
               "sở cụ thể, dựa trên thông tin thu được từ các công việc đó và kiến "
               "thức hiện có về cách khí, hơi và sương mù dễ cháy hành xử khi thoát "
               "ra vào bầu khí quyển hoặc khu vực có đủ oxy để duy trì cháy."))
    b.append(p("Một khối lượng lớn công trình nghiên cứu đã được tiến hành khá phối "
               "hợp về phương pháp bảo vệ thiết bị điện dùng trong bầu khí quyển nổ; "
               "điều đó không thể nói về công tác phân loại khu vực, vốn ít được đầu "
               "tư hơn và phân mảnh hơn. BS 5345 phần 2 (1983) đã mô tả rất rõ các "
               "khía cạnh và quy trình nhưng vẫn phải yêu cầu người đọc tìm đến các "
               "quy phạm công nghiệp khác để biết phạm vi khu vực nguy hiểm, vì quan "
               "điểm khác nhau giữa các ngành và giữa các công ty. Điều an tâm là "
               "gần như bất kỳ quy phạm công nghiệp được công bố nào cũng cho phân "
               "loại đủ an toàn nếu người áp dụng am hiểu, không chịu áp lực thương "
               "mại không đáng có và có đủ thông tin về vị trí được phân loại cùng "
               "vật liệu dễ cháy liên quan. Tuy nhiên, mỗi quy phạm dựa trên một cách "
               "tiếp cận riêng, và các cách tiếp cận đó khác nhau giữa các quy phạm; "
               "vì thế cần hết sức thận trọng khi dùng thông tin từ nhiều hơn một "
               "quy phạm cho cùng một nhà máy. Mục tiêu của chương là xem xét triết "
               "lý nền tảng, đưa ra ví dụ về phạm vi dựa trên triết lý đó và sử dụng "
               "các công thức toán học của Chương 4 khi thích hợp."))

    b.append(h3("3.1 Chứa giữ vật liệu dễ cháy",
                "3.1 Containment of flammable materials"))
    b.append(p("Vật liệu dễ cháy trong nhà máy được chứa theo nhiều cách; cách rõ "
               "ràng nhất là ở dạng khí hoặc hơi, thường với áp suất cao hơn để vận "
               "chuyển hoặc vì lý do công nghệ. Trong khu vực thông gió tự nhiên, khi "
               "đó chỉ còn cần xác định tốc độ phát thải và cơ chế trộn với không "
               "khí, thường là do chuyển động của chính dòng khí/hơi hoặc do gió. Các "
               "trạng thái chứa giữ khác phức tạp hơn nhiều và làm công tác phân loại "
               "khó khăn hơn đáng kể."))
    b.append(h4("3.1.1 Ảnh hưởng của điều kiện cất giữ",
                "3.1.1 Effects of storage conditions"))
    b.append(p("Vật liệu dễ cháy có thể được chứa ở áp suất cao, nên chất mà ở áp "
               "suất môi trường bình thường là hơi thì lại được cất giữ dưới dạng "
               "lỏng. Khi chất lỏng đó thoát ra, áp suất giảm và hiện tượng hóa hơi "
               "xảy ra — cũng là nguyên lý của tủ lạnh. Cần có nhiệt đầu vào để hóa "
               "hơi (nhiệt ẩn hóa hơi); trong quá trình hóa hơi, nhiệt độ chất lỏng "
               "giảm cho đến khi đạt điểm sôi, khi đó hóa hơi dừng lại cho đến khi có "
               "nhiệt từ bên ngoài. Vì thế có một tỷ lệ bay hơi ngay lập tức, sau đó "
               "là bay hơi chậm hơn khi phần lỏng còn lại gặp nguồn nhiệt. Tỷ lệ này "
               "cần được xác định; Chương 4 đưa ra một phương pháp tính toán khả dĩ."))
    b.append(p("Vật liệu cũng có thể được cất ở áp suất dưới điểm sôi, và người ta "
               "có thể nghĩ rằng nó sẽ không tạo nhiều hơi khi thoát ra. Điều đó "
               "không hoàn toàn đúng: lỗ thoát có thể đủ nhỏ để tạo sương mù chất "
               "lỏng — các hạt lỏng phân tán rất mịn có cách hành xử giống hơi trong "
               "việc tạo bầu khí quyển nổ. Với lỗ nhỏ, có thể hình thành sương mù "
               "đáng kể ngay ở áp suất đo thấp tới 2 × 10⁵ N/m²; với lỗ lớn thì khó "
               "hơn, dù một phần chất lỏng thoát ra vẫn có thể ở dạng sương mù. Sương "
               "mù có thể bắt cháy ngay cả khi chất lỏng tại điểm thoát đang dưới "
               "điểm cháy, miễn là trộn đúng với không khí. Một cơ chế khác là hơi dễ "
               "cháy được chứa dưới dạng lỏng có áp suất: độ nhiễu loạn do giảm áp, "
               "cộng với hóa hơi như đã mô tả, tạo ra cả hơi lẫn một lượng sương mù "
               "tại điểm thoát. Tất cả phải được tính đến."))
    b.append(p("Còn trường hợp chất lỏng dễ cháy được chứa ở nhiệt độ trên điểm cháy "
               "nhưng dưới điểm sôi. Khi thoát ra chỉ tạo rất ít hơi dễ cháy, vì thế "
               "có thể hình thành tia phun; nếu không bị chặn, tia có thể đi xa đáng "
               "kể trước khi chạm đất hoặc vật cản, và tại đó tạo thành vũng lỏng. "
               "Kích thước vũng được giới hạn bởi địa hình mặt đất hoặc tốc độ bay "
               "hơi, và có thể tạo khu vực nguy hiểm đáng kể cách nguồn rò một "
               "khoảng; thêm vào đó là nguy cơ tia lỏng chạm bề mặt nóng, làm tình "
               "huống xấu hơn. Mọi yếu tố trên đều phải được xem xét."))
    b.append(h4("3.1.2 Ảnh hưởng của ánh nắng mặt trời đối với bình chứa",
                "3.1.2 Effect of sunlight on storage vessels"))
    b.append(p("Một vấn đề khác phát sinh khi chất lỏng dễ cháy được cất giữ trong "
               "thời gian đáng kể và bình chứa phơi nắng trực tiếp — điển hình là "
               "bình chứa hàng tồn kho thông thường. Có nhiều bằng chứng cho thấy "
               "trong điều kiện đó bình hấp thụ đáng kể nhiệt mặt trời, và hỗn hợp "
               "hơi/không khí phía trên bề mặt lỏng có nhiệt độ cao hơn môi trường "
               "rõ rệt, thúc đẩy bay hơi. Chất lỏng có điểm cháy cao hơn nhiệt độ môi "
               "trường, vốn không bị coi là dễ cháy, có thể trở nên dễ cháy; một số "
               "chất lỏng dễ cháy có thể đạt đến điểm sôi. Những yếu tố này cũng cần "
               "được tính đến."))
    b.append(h4("3.1.3 Làm giàu oxy", "3.1.3 Oxygen enrichment"))
    b.append(p("Cuối cùng, cần nhớ rằng phân loại khu vực dựa trên hỗn hợp của khí, "
               "hơi hoặc sương mù dễ cháy với không khí ở áp suất khí quyển; công "
               "nghệ này cũng dựa trên hỗn hợp vật liệu dễ cháy với không khí. Điều "
               "kiện cần để đánh lửa thay đổi, đặc biệt khi tăng hàm lượng oxy như "
               "trong các quá trình oxy hóa. Thiết bị được coi là phù hợp cho bầu "
               "khí quyển nổ, vốn giả định áp suất khí quyển và không khí, có thể "
               "không phù hợp trong những hoàn cảnh đó. Khi gặp tình huống như vậy, "
               "đánh giá phân loại phải tính đến chúng và phải xác định đây là vị trí "
               "đặc biệt, để người lựa chọn thiết bị biết rằng thiết bị được bảo vệ "
               "thông thường có thể không phù hợp và phải loại trừ nó, chỉ chọn thiết "
               "bị đã được chứng minh là phù hợp với môi trường cụ thể."))
    b.append(h4("3.1.4 Xét chung về phát thải",
                "3.1.4 General consideration of release"))
    b.append(p("Từ những điều trên, cần xét mọi điểm có thể thoát vật liệu dễ cháy và "
               "xác định thích hợp các khu vực bị nhiễm bởi các phát thải đó. Trước "
               "đây người ta làm điều này bằng phương pháp phân loại khái quát, "
               "nhưng từ năm 1970 phương pháp nguồn nguy hiểm chính xác hơn, khách "
               "quan hơn đã được ưu tiên; các ví dụ trong chương này dựa trên phương "
               "pháp sau."))

    b.append(h3("3.2 Phương pháp phân loại khái quát",
                "3.2 Generalized method of area classification"))
    b.append(p("Phương pháp khái quát là phương pháp đã được dùng từ trước đến nay. "
               "Kiến thức thu được trong nhiều năm về hành vi của nhà máy giờ cho "
               "phép một phương pháp chính xác hơn, gọi là phương pháp nguồn nguy "
               "hiểm. Điều đó không có nghĩa là không được dùng phương pháp khái "
               "quát, nhưng nó ít được ưa chuộng hơn vì áp dụng đúng thường cho khu "
               "vực nguy hiểm lớn hơn mức thực tế, làm tăng chi phí vận hành và đôi "
               "khi gây tranh cãi khi cơ quan quản lý và các bên khác cho rằng các "
               "vùng có mức nguy hiểm cao (Vùng 0 và 1) là quá lớn — một trong những "
               "mục tiêu chính của phân loại là ảnh hưởng đến thiết kế nhà máy, nên "
               "điều này dẫn đến chi phí quá mức. Nếu thực hiện không cẩn thận, "
               "phương pháp này đôi khi cũng bỏ sót khu vực nguy hiểm, tạo nguy cơ "
               "không đáng có. Phương pháp khái quát không yêu cầu xác định riêng "
               "từng nguồn nguy hiểm mà đưa ra phán đoán dựa trên sự hiện diện của "
               "vật liệu dễ cháy trong một khu vực, cùng hiểu biết chung về loại "
               "thiết bị công nghệ thường bị rò rỉ; việc này đòi hỏi một bộ thước "
               "đo cơ bản làm cơ sở cho các phán đoán đó."))
    b.append(h4("3.2.1 Quy định phân loại vùng khái quát",
                "3.2.1 Generalized zonal classification specification"))
    b.append(p("<b>Vùng 0.</b> Vùng 0 gồm nội thất của bình chứa kín hoặc thông gió "
               "chứa chất lỏng hoặc hơi dễ cháy và không khí. Rõ ràng điều này chỉ áp "
               "dụng cho phần không gian hơi của bình kín hoặc thông gió chứa chất "
               "lỏng dễ cháy; vì lượng lỏng trong bình thường thay đổi, Vùng 0 kéo "
               "dài xuống mức lỏng thấp nhất có thể. Vùng 0 cũng xuất hiện trong phần "
               "không gian hơi của bình hở nắp chứa chất lỏng dễ cháy, và ở mọi nơi "
               "khác mà khí hoặc hơi dễ cháy thường được thải ra."))
    b.append(p("<b>Vùng 1.</b> Vùng 1 là khu vực có bình chứa, bơm, máy nén, phụ "
               "tùng đường ống và các thiết bị tương tự có thể được coi là rò rỉ "
               "trong vận hành bình thường (tức có mức độ đều đặn nhất định); cũng là "
               "khu vực có van xả áp, cổng thông khí và các thiết bị tương tự được "
               "thiết kế để thải khí, hơi hoặc chất lỏng dễ cháy trong vận hành bình "
               "thường. Các khu vực có điểm lấy mẫu không được thiết kế đặc biệt để "
               "ngăn phát thải trong vận hành bình thường cũng thuộc Vùng 1, dù với "
               "điểm lấy mẫu thì Vùng 1 có thể giới hạn ngay tại điểm đó, nhất là khi "
               "lấy mẫu thủ công. Cuối cùng, các khu vực có phát thải hiếm đến mức "
               "không giả định là xảy ra trong vận hành bình thường vẫn được xác "
               "định là Vùng 1 nếu thông gió bị hạn chế — gồm cả khu vực trong nhà và "
               "các khu vực khác mà vì hình thức chứa giữ hay hạn chế dòng khí nên "
               "thông gió được coi là hạn chế."))
    b.append(p("<b>Vùng 2.</b> Vùng 2 là khu vực có bình chứa, bơm, máy nén và thiết "
               "bị tương tự được bảo trì tốt đến mức rò rỉ chỉ được giả định là xảy "
               "ra rất hiếm (trong điều kiện bất thường), cùng van xả áp chỉ hoạt "
               "động rất hiếm (bất thường); cổng thông khí liên quan đến đĩa vỡ cũng "
               "thường tạo Vùng 2 tại nơi chúng hiện diện. Trong mọi trường hợp, "
               "việc xếp Vùng 2 chỉ chấp nhận được nếu khu vực đó thông gió tự "
               "nhiên, tức tương đương điều kiện ngoài trời bình thường, để hơi thoát "
               "ra phân tán nhanh. Những phần thông gió kém hơn trong các Vùng 2 này, "
               "chẳng hạn hố và rãnh, được xếp Vùng 1. Vì nguy cơ đối với nhân viên "
               "lấy mẫu, điểm lấy mẫu thường được thiết kế để bảo đảm mọi khu vực "
               "nhân viên tiếp cận để lấy mẫu đều là Vùng 2."))
    b.append(h4("3.2.2 Phạm vi khái quát của các vùng",
                "3.2.2 Generalized extents of zones"))
    b.append(p("Phạm vi của các vùng do cách tiếp cận này tạo ra có xu hướng tùy tiện "
               "và lớn. Nội thất bình chứa được xác định rõ, nhưng khi xét các khu "
               "vực ít nguy hiểm hơn — nhất là Vùng 2 — người ta phải phân loại toàn "
               "bộ địa điểm, và không phải hiếm khi cả một nhà máy được xếp Vùng 2. "
               "Dù vậy, dùng đúng cách thì phương pháp khái quát vẫn phải được thừa "
               "nhận là hợp lệ vì nó phân loại quá mức chứ không thiếu. Đáng tiếc là "
               "khả năng dùng sai rất lớn; các vùng được chỉ định là Vùng 1 và Vùng 2 "
               "thường lớn hơn mức chấp nhận được nếu dùng phương pháp nguồn nguy "
               "hiểm, gây mất uy tín đáng kể khi bị bên thứ ba nhận ra. Hiện phương "
               "pháp này ít được dùng, trừ những khu vực nhà máy rất chật chội, và "
               "ngay tại đó cũng chỉ là phương pháp bổ trợ cho phương pháp nguồn "
               "nguy hiểm."))

    b.append(h3("3.3 Phương pháp nguồn nguy hiểm trong phân loại khu vực",
                "3.3 The source of hazard method of area classification"))
    b.append(p("Phương pháp nguồn nguy hiểm được đưa vào dần từ khoảng năm 1970. "
               "Trước đó, phương pháp khái quát ở mục 3.2 đã được dùng rộng rãi, "
               "nhưng ngành ngày càng lo ngại rằng các khu vực nguy hiểm mà nó mô tả "
               "quá lớn so với thực tế, đặc biệt là Vùng 1 bao phủ những diện tích "
               "đáng kể. Điều này đặt ra câu hỏi về quyền tiếp cận tự do của nhân "
               "viên nhà máy vào vùng đó: tần suất phát thải chất dễ cháy ở Vùng 1 là "
               "đáng kể và nhiều chất dễ cháy có thể độc hại hoặc gây ngạt, nên việc "
               "phơi nhiễm cho nhân viên có thể không được chấp nhận. Cộng thêm ảnh "
               "hưởng chi phí, đã có nhiều áp lực nhằm thu hẹp các khu vực nguy hiểm "
               "này. Phương pháp khái quát không cho phép làm vậy mà không đưa vào "
               "rủi ro đáng kể, và các nỗ lực đạt mức thu hẹp cần thiết đã dẫn đến "
               "sự khác biệt rối ren trong kết luận, đe dọa niềm tin vào phân loại "
               "khu vực."))
    b.append(p("Những vấn đề đó dẫn đến việc xem xét kỹ hơn công nghệ phân loại khu "
               "vực, từ đó phát triển phương pháp nguồn nguy hiểm. Phương pháp này "
               "khác hẳn phương pháp khái quát: phải xác định từng nguồn phát thải "
               "cùng cơ chế phát thải tại điểm đó, xác định lượng phát thải và tiêu "
               "chí phân tán, rồi từ đó suy ra phạm vi khu vực nguy hiểm do một phát "
               "thải cụ thể tạo ra. Việc xác định phạm vi này một phần dùng cách tiếp "
               "cận toán học tương tự Chương 4, dù ở mức nhất định không chính xác — "
               "bằng chứng là người ta vẫn chưa thống nhất được một cách tiếp cận "
               "toán học duy nhất — và một phần dựa trên chứng cứ cùng quan sát thực "
               "nghiệm. Dù vẫn còn một số tranh cãi, hầu hết cách tiếp cận được công "
               "bố cho kết quả khá giống nhau và cho khu vực nguy hiểm nhỏ hơn so với "
               "phương pháp khái quát. Trong hơn 25 năm áp dụng phương pháp nguồn "
               "nguy hiểm, không có bằng chứng nào cho thấy kết quả đạt được làm tăng "
               "nguy cơ nổ khi kỹ thuật được áp dụng đúng cách."))
    b.append(p("Một điểm khác biệt mà cách tiếp cận nguồn nguy hiểm làm rõ lần đầu "
               "tiên là Vùng 1 không tự động được bao quanh bởi Vùng 2. Dù điều đó "
               "cũng đúng trong phương pháp khái quát, tính chất chung chung của "
               "phương pháp này đã che giấu điều đó và người ta thường tin rằng Vùng "
               "1 luôn được bao quanh bởi Vùng 2. Phương pháp nguồn nguy hiểm tự động "
               "xóa bỏ hiểu lầm đó: để có khu vực nguy hiểm trước hết phải xác định "
               "nguồn phát thải tạo ra nó. Do đó, một chỗ rò phải được xác định là có "
               "thể hành xử theo hai cách rất khác nhau để tạo ra cả Vùng 1 lẫn Vùng "
               "2. Điều này lại dẫn đến một nhận thức chưa từng được làm rõ trước đây: "
               "một nguồn rò duy nhất có thể hành xử khác nhau trong những hoàn cảnh "
               "khác nhau. Khi xác định một nguồn nguy hiểm theo phương pháp này, cần "
               "xác định xem nguồn đó có thể hành xử theo nhiều cách hay không, rồi "
               "xác định khu vực nguy hiểm do từng cách vận hành có thể tạo ra."))
    b.append(p("Dù phương pháp nguồn nguy hiểm xác định từng nguồn phát thải cùng "
               "khu vực nguy hiểm do nó tạo ra, vẫn còn vấn đề nhiều nguồn ở cùng vị "
               "trí hoặc gần nhau. Rõ ràng không phải mọi nguồn đều phát thải cùng "
               "lúc, nhưng trong nhiều trường hợp một số nguồn có thể phát thải đồng "
               "thời, và cần xác định phạm vi của khu vực nguy hiểm tạo ra. Với nguồn "
               "cấp phụ, phát thải quá hiếm nên không cần cộng dồn theo cách nào; "
               "không thể nói như vậy với nguồn cấp chính, vốn phát thải thường "
               "xuyên hơn nhiều. Trong những trường hợp đó phải tính đến phát thải "
               "đồng thời. Rõ ràng với nhiều nguồn như vậy không hợp lý khi giả định "
               "tất cả phát thải cùng lúc, nên cần một bảng hướng dẫn. Bảng 3.1 đưa "
               "ra cách tính tổng phát thải từ nhiều nguồn khi quyết định yêu cầu "
               "thông gió cho khu vực trong nhà, nhưng cũng có thể áp dụng khá tin "
               "cậy cho nhiều nguồn trong mọi tình huống. Bảng này lần đầu được công "
               "bố năm 1973 trong Quy phạm RoSPA/ICI."))
    b.append(table(_T31_HEAD_VI, _T31_ROWS,
                   "Bảng 3.1 · Phát thải đồng thời từ các nguồn nguy hiểm"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("3 — Area classification practice for gases, vapours and mists "
                "in freely ventilated situations",
                "3 — Area classification practice for gases, vapours and mists "
                "in freely ventilated situations"))
    b.append(lead("From principles to hazardous area extents"))
    b.append(p("Chapter 2 examined the mechanisms of area classification, the "
               "constitution of the teams carrying it out and the detail of the "
               "information needed to produce a classification. This chapter turns "
               "to the actual production of a classification for a particular works "
               "or plant, based on the information produced by those exercises and "
               "on available knowledge of how flammable gases, vapours and mists "
               "behave when released into an atmosphere or other area where "
               "sufficient oxygen exists to support combustion."))
    b.append(p("A tremendous amount of research has been carried out in a relatively "
               "coordinated way on methods of protecting electrical equipment for "
               "use in explosive atmospheres; the same cannot be said of work on "
               "area classification, which has been less intensive and more "
               "fragmented. BS 5345 Part 2 (1983) described the facets and procedures "
               "well but had to direct readers to other industrial and similar codes "
               "for the detail of extents, because of divergent views between those "
               "involved and between industries and companies. The reassuring thing "
               "is that adoption of almost any published industry code will produce "
               "an acceptably secure classification when applied by personnel "
               "knowledgeable in the subject, operating without undue commercial "
               "pressure and with full information about the site and the flammable "
               "materials involved. Each code, however, rests on a particular "
               "approach, and these approaches vary between codes; extreme care is "
               "therefore necessary if a plant is classified using information from "
               "more than one code. The objective here is to examine the background "
               "philosophy, give example extents based upon it, and use the "
               "mathematical formulae of Chapter 4 where appropriate."))

    b.append(h3("3.1 Containment of flammable materials",
                "3.1 Containment of flammable materials"))
    b.append(p("Flammable materials may be contained in a process plant in a variety "
               "of ways; the most obvious is as a gas or vapour, usually at some "
               "elevated pressure needed to transport it or for some other process "
               "reason. In freely ventilated areas the question is then simply one "
               "of determining the release rate and the mechanism by which the gas "
               "or vapour mixes with air, usually by virtue of its own motion or by "
               "wind effects. Several other ways in which a flammable material may "
               "exist make the classification exercise much more complicated."))
    b.append(h4("3.1.1 Effects of storage conditions",
                "3.1.1 Effects of storage conditions"))
    b.append(p("The material may, for instance, be contained at high pressure, so "
               "that what would be a vapour at normal ambient pressure is actually "
               "stored as a liquid. When such a liquid is released the pressure "
               "falls and vaporization takes place, much as in a refrigerator. Heat "
               "input is needed to effect vaporization (latent heat of vaporization): "
               "as the liquid vaporizes its temperature falls until it reaches its "
               "boiling point, at which point vaporization ceases until external "
               "heat is added. There is therefore an immediate evaporation of a "
               "percentage of the liquid, followed by slower evaporation when the "
               "residual liquid reaches a heat source. That percentage needs to be "
               "defined; a possible calculative method is given in Chapter 4."))
    b.append(p("The material may instead be contained at a pressure below its "
               "boiling point, and it might be thought that little vapour would be "
               "produced on initial release. That is not wholly true: the release "
               "orifice may support the formation of mists, finely divided liquid "
               "particles which behave like vapours as far as explosive atmospheres "
               "are concerned. With small orifices significant mist formation is "
               "possible at gauge pressures as low as 2 × 10⁵ N/m²; with larger "
               "orifices it is less likely, although part of the liquid release may "
               "still emerge as a mist. The mist may be ignitable even if the liquid "
               "at the point of release is below its flashpoint, provided it is "
               "appropriately mixed with air. Another typical method of producing a "
               "mist is a flammable vapour contained as a liquid at pressure: the "
               "turbulence created by pressure reduction, coupled with the "
               "vaporization already described, produces some mist in addition to "
               "the vapour at the point of release. All of this must be taken into "
               "account."))
    b.append(p("There is also the containment of a flammable liquid above its "
               "flashpoint but below its boiling point. Little flammable vapour is "
               "produced on release, so jet formation is possible. Unless contained, "
               "such jets can travel significant distances before striking the "
               "ground or an obstruction, and where they cease to travel a pool "
               "will be formed. The pool is controlled in size either by ground "
               "contours or by the evaporation rate of the material, and significant "
               "hazardous areas can be produced some distance from the source of "
               "leakage; in addition there is the risk that the liquid jet may come "
               "into contact with a hot surface, exacerbating the situation. All of "
               "these matters must be considered."))
    b.append(h4("3.1.2 Effect of sunlight on storage vessels",
                "3.1.2 Effect of sunlight on storage vessels"))
    b.append(p("A further problem exists where flammable liquids are contained for "
               "significant periods and the containment is in direct sunlight, "
               "typically the ordinary stock tank. There is considerable evidence "
               "that significant solar gain can occur in such circumstances and "
               "that the vapour/air mixture in the tank above the liquid adopts a "
               "temperature significantly above ambient, encouraging evaporation. "
               "Liquids with flashpoints above ambient, which would not otherwise "
               "be considered flammable, may thereby become flammable, and some "
               "flammable liquids may reach their boiling points. These matters "
               "also require to be taken into account."))
    b.append(h4("3.1.3 Oxygen enrichment", "3.1.3 Oxygen enrichment"))
    b.append(p("Finally, it must be remembered that area classification is based "
               "upon the mixture of a flammable gas, vapour or mist with air at "
               "atmospheric pressure; the technology is likewise based upon "
               "mixtures of flammable materials with air. The conditions necessary "
               "for ignition vary, particularly with increased levels of oxygen "
               "such as occur in oxidation processes. Equipment considered suitable "
               "for explosive atmospheres, assuming as it does atmospheric pressure "
               "and air, may not be suitable in such circumstances. Where such "
               "situations arise the classification evaluation must take account of "
               "them, and they must be identified as special so that those selecting "
               "equipment are aware that normally protected equipment may not be "
               "suitable and must be excluded in favour of apparatus shown to be "
               "suitable for the specific environment."))
    b.append(h4("3.1.4 General consideration of release",
                "3.1.4 General consideration of release"))
    b.append(p("Taking account of the above, it is necessary to consider all points "
               "from which flammable material may be released and to identify "
               "appropriately the areas contaminated by those releases. Historically "
               "this was done by the generalized method of area classification, but "
               "since 1970 the more exact and considerably more objective source of "
               "hazard method has come to the fore; the examples in this chapter "
               "are based on the latter."))

    b.append(h3("3.2 Generalized method of area classification",
                "3.2 Generalized method of area classification"))
    b.append(p("The generalized method is the method historically used. Knowledge "
               "of plant performance gained over many years has now permitted a "
               "more precise method, known as the source of hazard method. That does "
               "not mean the generalized method may not be used, but it has become "
               "less popular because correct application often gives more extensive "
               "hazardous areas than actually exist, increasing operating costs and "
               "sometimes causing conflict when regulatory bodies and others "
               "perceive Zones 0 and 1 as excessively large; since a principal "
               "objective of classification is to influence plant design, this "
               "leads to excessive expenditure. Occasionally, if not carefully "
               "executed, it can also fail to identify certain hazardous areas "
               "adequately, creating unnecessary danger. The generalized method "
               "does not require each source of hazard to be uniquely identified; "
               "a judgment is made from the presence of flammable materials in a "
               "particular area together with general identification of the types "
               "of process equipment known to leak. This requires a set of basic "
               "yardsticks against which such judgments may be made."))
    b.append(h4("3.2.1 Generalized zonal classification specification",
                "3.2.1 Generalized zonal classification specification"))
    b.append(p("<b>Zone 0.</b> Zone 0 includes the interiors of closed or ventilated "
               "vessels containing flammable liquids or vapours and air. Clearly "
               "this applies only to the vapour spaces of closed or ventilated "
               "tanks containing flammable liquids, and as these tanks usually "
               "contain a varying quantity of liquid the Zone 0 extends to the "
               "lowest possible liquid level. A Zone 0 will also occur in the vapour "
               "space of an open-topped tank containing a flammable liquid, as will "
               "all other places where flammable gas or vapour is normally "
               "released."))
    b.append(p("<b>Zone 1.</b> Zone 1 is any area containing vessels, pumps, "
               "compressors, pipe fittings and similar items of equipment which may "
               "be considered to leak in normal operation (that is, with some "
               "degree of regularity), and any area containing relief valves, vents "
               "and similar devices designed to release flammable gases, vapours or "
               "liquids in normal operation. Areas containing sample points not "
               "specially designed to prevent release in normal operation are also "
               "Zone 1, although in the case of sample points the Zone 1 can be "
               "limited to the immediate location of the point, particularly if "
               "sampling is manual. Finally, areas where releases are so rare as "
               "not to be assumed to occur in normal operation will also be "
               "identified as Zone 1 if ventilation is restricted, including both "
               "indoor areas and other areas where, as a result of containment or "
               "airflow restriction, ventilation is considered to be restricted."))
    b.append(p("<b>Zone 2.</b> Zone 2 is an area containing vessels, pumps, "
               "compressors and similar equipment so well maintained that leaks can "
               "be assumed to occur only very rarely (in abnormal operation), and "
               "relief valves which operate only very rarely (abnormally); vents "
               "associated with bursting discs will also normally give rise to Zone "
               "2 in the areas in which they occur. In all these cases the Zone 2 "
               "classification is acceptable only provided the areas in question "
               "are freely ventilated, that is, equivalent to a normal outdoor "
               "situation, so that the released vapour is rapidly dispersed. Less "
               "well-ventilated parts of these Zones 2, such as pits and trenches, "
               "will be defined as Zone 1. Because of the danger to personnel "
               "carrying out sampling, sampling points are normally designed to "
               "ensure that any area into which personnel access for sampling is "
               "Zone 2."))
    b.append(h4("3.2.2 Generalized extents of zones",
                "3.2.2 Generalized extents of zones"))
    b.append(p("The extents of the zones produced by this approach tend to be "
               "arbitrary and large. Vessel interiors are well defined, but when the "
               "less hazardous areas — particularly Zone 2 — are considered, "
               "entire locations have to be classified, and it is not unknown for a "
               "whole plant to be classified. Properly used, however, the "
               "generalized method must be accepted as valid since it over- rather "
               "than under-classifies. Regrettably, there is ample scope for "
               "incorrect use, and the areas designated as Zone 1 and Zone 2 often "
               "become larger than would be acceptable if the source of hazard "
               "method were used, causing considerable loss of credibility when "
               "identified by third parties. The method is now seldom used except "
               "in very congested parts of plant, and even there only as an adjunct "
               "to the source of hazard method."))

    b.append(h3("3.3 The source of hazard method of area classification",
                "3.3 The source of hazard method of area classification"))
    b.append(p("The source of hazard method was introduced progressively from "
               "around 1970. Before that time the generalized method of Section 3.2 "
               "had been used extensively, but there was growing concern in industry "
               "that the hazardous areas it described were too large to represent "
               "the true picture, particularly Zone 1, which covered significant "
               "areas. This raised questions about free access of plant personnel "
               "to the zone: the frequency of release of flammables in Zone 1 is "
               "significant and, as a significant number of flammables can be toxic "
               "or asphyxiant, exposure of personnel may not be considered "
               "acceptable. Together with the cost implications, this led to many "
               "pressures to restrict the size of these hazardous areas. The "
               "generalized method was found not to lend itself to this without "
               "introducing significant risk, and attempts to achieve the required "
               "reduction led to a bewildering variation of conclusions which "
               "threatened confidence in area classification."))
    b.append(p("These problems led to a much closer examination of the technology "
               "of area classification and hence to the development of the source "
               "of hazard method. This method differs sharply from the generalized "
               "method: each source of release and the mode of release at that point "
               "must be identified, release quantities and dispersal criteria must "
               "be established, and from this information the extent of the "
               "hazardous area emanating from a particular release is determined. "
               "The extent is derived partly from mathematical approaches similar "
               "to those explained in Chapter 4, although these are to a degree "
               "inexact, as witnessed by the failure of those involved to agree a "
               "single mathematical approach, and partly from experimental evidence "
               "and observation. Although some controversy remains, most published "
               "approaches give relatively similar results and smaller hazardous "
               "areas than the generalized method. In over 25 years of use of the "
               "source of hazard method there is no evidence that the results "
               "achieved have increased the risk of explosion where the technique "
               "has been properly applied."))
    b.append(p("Another difference brought about by the source of hazard approach "
               "is the clear identification, for the first time, that Zone 1 is not "
               "automatically surrounded by Zone 2. While this was also true in the "
               "generalized method, the fact tended to be obscured by its "
               "generality and it became common belief that Zone 1 was always "
               "surrounded by Zone 2. The source of hazard method automatically "
               "dispels that misunderstanding: to have a hazardous area it is first "
               "necessary to identify a source of release which creates it. A leak "
               "would therefore have to be identified as possibly behaving in two "
               "distinctly different ways in order to produce both a Zone 1 and a "
               "Zone 2. This in turn leads to another fact not previously clearly "
               "identified, namely that a single source of leakage can behave in "
               "different ways in different circumstances. When a source of hazard "
               "is identified under this method it is necessary to determine "
               "whether it can behave in more than one way and then to identify the "
               "hazardous area created by each possible mode of operation."))
    b.append(p("While the source of hazard method identifies each source of release "
               "and the hazardous area it creates, there remains the problem of "
               "multiple sources in the same or close locations. It is clearly not "
               "likely that all sources will release at the same time, but in "
               "multiple cases some may, and the extent of any hazardous area so "
               "produced needs to be identified. In the case of secondary grade "
               "sources the release is so infrequent that such sources need not be "
               "added in any way, but the same cannot be true of primary grade "
               "sources, which release much more frequently. In such cases account "
               "must be taken of simultaneous release. With many such sources it "
               "would clearly be unreasonable to assume that all release "
               "simultaneously, so some sort of guide is necessary. Table 3.1 gives "
               "a method of calculating total release from multiple sources when "
               "deciding upon ventilation requirements for indoor areas, but it can "
               "also be applied with some confidence to multiple sources in any "
               "situation. It was first published in 1973 in the RoSPA/ICI Code."))
    b.append(table(_T31_HEAD_EN, _T31_ROWS,
                   "Table 3.1 · Simultaneous release from sources of hazard"))
    return "".join(b)
