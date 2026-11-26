# -*- coding: utf-8 -*-
"""Chapter 3, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 72-80 (PDF pp. 93-101).

Covers Sections 3.4.4-3.4.8: road and rail tankers, oil/water separators,
other open vessels, open drains and trenches. Figures 3.12-3.14 are drawn
in mcmillanfig03_c and displayed here with sequential ids 9-11, following
the ids 6-8 used by module C for Figures 3.9-3.11.

Tables 3.7, 3.9 and 3.10 are named but their data lie in the eight missing
pages (PDF pp. 80-87), so no rows are fabricated. Page-level data and
headings are owned by the integration module; this file defines only the
two body functions.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h4, p, note, fig

import mcmillanfig03_c as FC


def body_vi():
    b = []
    b.append(h4("3.4.4 Xe bồn đường bộ và đường sắt chở chất lỏng dễ cháy",
                "3.4.4 Road and rail tanks for flammable liquids"))
    b.append(p("Chất lỏng được vận chuyển thường xuyên bằng đường bộ hoặc đường sắt. "
               "Nhìn chung, các khu vực mà chúng đi qua khi đang vận chuyển không được "
               "phân loại vì thời gian lưu lại ở đó ngắn, cộng với việc mọi rò rỉ trong "
               "lúc vận chuyển đều là bất thường, nên khả năng một khu vực bị nhiễm bầu "
               "khí nổ là rất thấp và việc phân loại khu vực không có ý nghĩa. Tuy nhiên, "
               "cần thận trọng: ở những nơi xe bồn lưu lại đáng kể hoặc có nhiều xe bồn "
               "đậu trong thời gian dài, phân loại khu vực có thể trở nên cần thiết. "
               "Ranh giới thường được lấy giữa các bãi đậu xe công cộng — nơi xe bồn có "
               "thể đậu qua đêm cùng phương tiện khác — và các vị trí dành riêng cho xe "
               "bồn, chẳng hạn khu vực bốc xếp tại sân bay."))
    b.append(p("Cách tiếp cận này có nghĩa là không cần phân loại các bãi đậu xe có khách "
               "tiếp cận công cộng, nhưng cần phân loại các bãi đậu trong khu vực cơ sở "
               "sử dụng vật liệu và được dành riêng cho xe bồn. Điển hình là đường sắt "
               "dành riêng cho việc xếp dỡ xe bồn, các khu vực nhất định trong bến cảng "
               "dành cho xe bồn trước khi bốc hoặc dỡ hàng, và các vị trí tương tự trong "
               "khu vực nhà máy. Cách khái quát hóa này không phải lúc nào cũng đúng: có "
               "những nơi nhiều xe bồn thường xuyên đậu, khi đó ranh giới nêu trên khó "
               "biện minh. Do tính chất không kiểm soát được của những chỗ đậu này, không "
               "thể áp dụng phân loại khu vực kinh điển, nên vai trò của người lái xe trở "
               "nên then chốt. Cần xác định lộ trình và quy trình đậu xe để giảm số xe "
               "bồn đậu lâu ở một vị trí, hạn chế đậu qua đêm và bảo đảm khi rời xe không "
               "có dấu hiệu rò rỉ; tất cả những điều đó giảm rủi ro xuống mức chấp nhận "
               "được. Có nhiều quy định của chính phủ trong lĩnh vực này, tiêu biểu là "
               "The Dangerous Substances (Conveyance by Road in Road Tankers and Tank "
               "Containers) Regulations 1981 (SI 1981/1059), cần được tham chiếu."))
    b.append(p("Bất cứ nơi nào xe bồn được nạp, dỡ hoặc đậu khi đã chứa hàng với số lượng "
               "đáng kể thì gần như không có lý do gì không áp dụng quy trình phân loại "
               "khu vực thông thường, và khi đó bản thân bể chứa và nội dung của nó là "
               "nguồn phát thải, trừ khi các nguồn phát thải cụ thể được ngăn chặn. Ví dụ, "
               "nguồn phát thải từ miệng thông hơi có thể được loại bỏ bằng hệ thống hút, "
               "khi đó không hình thành khu vực nguy hiểm ngoài vùng ngay sát miệng thông "
               "hơi, nhưng khí thải từ miệng này vẫn cần được xem xét. Ngoài ra, các vị trí "
               "chỉ dùng để dỡ hàng sẽ khác với nơi nạp hàng vì khi dỡ hơi thoát ra rất ít "
               "hoặc không đáng kể. Dưới đây là nội dung chính đối với xe bồn chở chất "
               "lỏng dễ cháy không áp lực, có điểm sôi cao hơn nhiệt độ môi trường."))
    b.append(p("Những xe bồn này thường có kết cấu chủ yếu là hàn, nên các nguồn phát thải "
               "cần xét chỉ gồm: rò ở các mối nối dùng để đấu đường ống; rò tại miệng "
               "thông hơi khi nạp; và rò từ ống mềm dùng nối xe bồn với thiết bị cố định. "
               "Phần phân loại dưới đây chỉ xét bản thân xe bồn và điểm đấu nối ngay sát "
               "nó; thiết bị cố định trong khu vực nạp phải được xử lý riêng. "
               "<b>Vùng 0:</b> bên trong bể chứa."))
    b.append(p("<b>Vùng 1.</b> Khi nạp hoặc dỡ, luôn có nguy cơ rò nhỏ tại điểm đấu nối "
               "hoặc tháo kết nối. Đây là nguồn phát thải cấp chính, nên cần xác định "
               "Vùng 1 quanh các điểm đấu nối. Kích thước của vùng này có phần tùy ý vì "
               "lượng chất lỏng rò do thao tác thủ công không biết chắc, nhưng không lớn; "
               "Vùng 1 kéo dài 1.5 m phía trên và quanh nguồn rò, chiếu thẳng đứng xuống "
               "mặt đất như trong Hình 3.12, sẽ bao phủ mọi tình huống. Việc chiếu xuống "
               "phản ánh khả năng hơi nặng hơn không khí. Trong Hình 3.12, ký hiệu a = "
               "1.5 m; b và c phụ thuộc vào đặc tính của vũng chất lỏng có thể hình thành, "
               "còn đường nét chấm φ là giới hạn Vùng 1 cho thao tác dỡ hàng."))
    b.append(fig(9, FC.fig_f312()))
    b.append(p("Khi dỡ hàng, khu vực nguy hiểm do miệng thông hơi gây ra không tồn tại, "
               "và khi đó phạm vi Vùng 1 do điểm đấu nối được xác định bởi các đường nét "
               "chấm trong Hình 3.12. Vùng 1 này kéo dài ngay dưới gầm xe bồn để tính đến "
               "thông gió bị hạn chế ở đó. Nguồn phát thải cấp chính thứ ba là ống mềm "
               "dùng nối xe bồn, chịu chuyển động thường xuyên và có thể hỏng trong vận "
               "hành bình thường. Hỏng hóc thường là vết nứt nhỏ và, vì áp suất thấp "
               "(thường chỉ là áp suất cột chất lỏng), mức phát thải tương ứng nhỏ. Vì vậy, "
               "Vùng 1 do ống mềm gây ra cũng được giới hạn ở 1.5 m phía trên và quanh "
               "điểm đấu nối, chiếu thẳng đứng xuống mặt đất."))
    b.append(p("<b>Vùng 2.</b> Vùng này xuất hiện trong các trường hợp bất thường. Thứ nhất "
               "là quá đầy: chất lỏng tràn qua miệng thông hơi, chảy xuống thành bể và tạo "
               "vũng trên mặt đất. Vùng 2 do sự kiện này tạo ra quanh bể không lớn hơn "
               "Vùng 1 do hơi gây ra, nên sẽ bị che lấp khi nạp xe bồn; nhưng vì là trường "
               "hợp bất thường, không được giả định là không tồn tại khi dỡ hàng. Do đó, "
               "trong mọi trường hợp đều có Vùng 2 kéo dài 1.5 m phía trên và quanh bể, "
               "chiếu thẳng đứng xuống mặt đất. Vũng chất lỏng trên mặt đất sẽ lớn dần cho "
               "đến khi bị chứa giữ lại hoặc cho đến khi tốc độ bay hơi bằng tốc độ rò; "
               "khu vực nguy hiểm do vũng này tạo ra là Vùng 2 và được xác định theo Bảng "
               "3.7."))
    b.append(p("Nguồn phát thải bất thường thứ hai là trường hợp ống nối mềm bị vỡ. Do lớp "
               "gia cố của loại ống này, không dự kiến vỡ hoàn toàn, nên rò tương tự như vỡ "
               "gioăng CAF được coi là mô hình hợp lý. Chất lỏng thoát ra tạo vũng có kích "
               "thước xác định được từ Bảng 3.3, và phạm vi khu vực nguy hiểm quanh vũng "
               "lại lấy từ Bảng 3.7. Vì áp suất thấp, khó có sương mù hình thành và Vùng 2 "
               "quanh ống nối là rất nhỏ; điều này không đáng kể vì Vùng 1 đã được xác "
               "định là 1.5 m sẽ bao trùm nó. Cuối cùng, hấp thụ nhiệt mặt trời rất khó xảy "
               "ra với xe bồn trừ khi đậu lâu dưới nắng trực tiếp ngay trước khi dỡ. Với sự "
               "cẩn trọng thích đáng, chỉ cần xét các chất lỏng có điểm cháy dưới 32 °C."))
    b.append(p("Xe bồn chở khí hoặc hơi dưới áp suất, hoặc khí/hơi hóa lỏng (vốn cũng ở dưới "
               "áp suất), cư xử như mọi bể chịu áp khác. Các cơ chế phát thải chủ yếu là: rò "
               "khi đấu hoặc tháo kết nối; rò do hỏng bộ truyền động van; rò do hỏng mối nối "
               "đường ống cố định; và rò do hỏng đầu nối mềm. Bên trong bể được coi là Vùng "
               "0 vì dù ít khả năng không khí lọt vào, vẫn luôn có khả năng bể thường xuyên "
               "rỗng, và thay vì xác định và kiểm soát những giai đoạn đó thì tốt hơn là giả "
               "định Vùng 0. Giả định này thường không gây hạn chế thừa."))
    b.append(p("<b>Vùng 1</b> phát sinh từ ba kịch bản nguồn phát thải cấp chính: hai do hỏng "
               "hóc và một do thao tác thủ công. Thứ nhất là thân van hoặc bộ truyền động; "
               "Vùng 1 lấy theo vùng thông thường của van được vận hành đều đặn, nên giả "
               "định có Vùng 1 kéo dài 1 m phía trên và quanh van. Thứ hai là hỏng ống nối "
               "mềm: lỗ rò dự kiến nhỏ, có thể coi như hóa hơi hoàn toàn tại điểm thoát, "
               "tương tự rò ở mối nối ren; Vùng 1 lấy từ Bảng 3.9 và Vùng 1 tại mặt đất lấy "
               "từ Bảng 3.10. Thứ ba là thao tác thủ công lúc đấu nối, dự kiến quá nhỏ nên "
               "nằm gọn trong Vùng 1 do hỏng ống mềm; nếu điểm đấu nối ở xa ống mềm thì cần "
               "bao quanh nó bằng Vùng 1 tương tự, áp dụng Bảng 3.9 và Bảng 3.10. "
               "<b>Vùng 2</b> do ống mềm, các đầu nối, mối nối khác và thân van tạo ra: phớt "
               "thân van được coi là gioăng gia cố xoắn ốc, còn mối nối mềm được coi là vỡ "
               "gioăng CAF; phạm vi lấy từ Bảng 3.9 và Bảng 3.10. Phần trên chỉ xét xe bồn "
               "và vùng ngay sát nó; khu vực nguy hiểm do thiết bị cố định bao quanh phải "
               "được xử lý riêng."))

    b.append(h4("3.4.5 Bể tách dầu/nước", "3.4.5 Oil/water separators"))
    b.append(p("Bể tách dầu/nước là bể hở, vào đó hỗn hợp nước và dầu (thường là dầu bị tràn) "
               "được dẫn vào và lưu lại đủ lâu để nước tách ra khỏi dầu, sao cho một phần "
               "có thể thải bỏ và phần kia đi vào hệ thống cống thông thường. Về lý thuyết, "
               "bể thường chứa chủ yếu dầu có độ bay hơi thấp vì dầu có độ bay hơi cao đã "
               "bay hơi đáng kể trước khi hỗn hợp đến bể. Ở những cơ sở mà phần lớn dầu sử "
               "dụng có độ bay hơi cao thì phương pháp tách dầu/nước này không phù hợp và "
               "cần chọn phương pháp khác, vì khu vực nguy hiểm do cách này tạo ra không "
               "chấp nhận được."))
    b.append(p("<b>Vùng 0</b> là bên trong bể tách, nhưng vùng này không vượt quá giới hạn của "
               "bể vì dầu chứa trong đó có độ bay hơi thấp. Sẽ không nên dùng bể tách dạng "
               "này nếu dầu có độ bay hơi cao; khi đó cần cách xử lý khác."))
    b.append(p("<b>Vùng 1</b> xuất hiện khi bể chứa dầu có độ bay hơi cao hơn bình thường và, "
               "do tác động của gió, tồn tại khu vực nguy hiểm bên ngoài bể. Trong những "
               "trường hợp này, thành phần dầu phải cho phép dùng cột 50% của Bảng 3.7, lấy "
               "diện tích bể làm kích thước vũng. Nếu một số lượng đáng kể dầu trong nhà máy "
               "có thể chảy vào bể là dầu độ bay hơi cao thì phải dùng cột >90%. Khu vực "
               "nguy hiểm được thể hiện trong Hình 3.13 đối với bể đặt tại mặt đất; nếu bể "
               "đặt cao hơn mặt đất, với đáy ngang mức mặt đất, Vùng 1 chỉ kéo dài thẳng "
               "đứng xuống theo thành bể."))
    b.append(fig(10, FC.fig_f313()))
    b.append(p("<b>Vùng 2</b> xuất hiện trong trường hợp bất thường, chẳng hạn sau một phát "
               "thải lớn dầu có độ bay hơi cao, khi đó khu vực nguy hiểm quanh bể lớn hơn. "
               "Phạm vi lấy từ Bảng 3.7 dùng cột >90%. Như đã nêu, vùng này trở thành Vùng 1 "
               "nếu một số lượng đáng kể dầu dùng tại cơ sở có độ bay hơi cao; khi đó không "
               "thấy Vùng 2 riêng biệt vì kích thước của nó trùng với Vùng 1. Hình 3.13 mô "
               "tả bể đặt tại mặt đất; nếu mặt đất ngang đáy bể thì Vùng 2 được chiếu thẳng "
               "đứng xuống theo thành bể. Giả định gió có vận tốc 2 m/sec khi dùng Bảng 3.7."))
    b.append(p("Cuối cùng, nếu bể tách bị tràn, sẽ hình thành vũng hỗn hợp dầu và nước. Vùng 2 "
               "tương ứng lấy từ Bảng 3.7 giả định có mặt dầu có độ bay hơi cao nhất. Vì có "
               "nước và hỗn hợp có thể lan xa hơn so với chỉ có dầu, nên nên hạn chế cơ học "
               "kích thước vũng bằng một bờ chắn có sức chứa bằng lượng tràn lớn nhất có "
               "thể. Kích thước này sau đó được dùng trong mọi trường hợp khi xác định phạm "
               "vi theo Bảng 3.7, kể cả khi vũng ở trạng thái cân bằng nhỏ hơn."))

    b.append(h4("3.4.6 Các bể hở khác", "3.4.6 Other open vessels"))
    b.append(p("Các bể hở cư xử rất giống bể tách dầu/nước, nhưng thường chỉ có một chất lỏng "
               "dễ cháy. <b>Vùng 0</b> là bên trong bể. <b>Vùng 1</b> xác định như đối với "
               "bể tách nhưng dựa trên điểm sôi của chất lỏng dễ cháy duy nhất đó khi thích "
               "hợp. Như trước, không nên dùng bể hở nếu điểm sôi của chất lỏng chứa thấp "
               "hơn hai lần nhiệt độ môi trường tại vị trí lắp đặt (ở Vương quốc Anh có nghĩa "
               "là điểm sôi cao hơn 65 °C). Cần phân biệt với tiêu chí độ bay hơi thấp dùng "
               "cho điểm lấy mẫu ở mục 3.4.9, ở đó điểm sôi phải ít nhất bằng bốn lần nhiệt "
               "độ môi trường."))
    b.append(p("Chỉ có trường hợp tràn mới tạo ra <b>Vùng 2</b>, và Vùng 2 này được xác định "
               "như đối với bể tách dầu/nước trong trường hợp đó."))

    b.append(h4("3.4.7 Mương/rãnh hở", "3.4.7 Open drains"))
    b.append(p("Mương thoát nước hở thường được dùng để thu các chất lỏng dễ cháy bị rò ra, "
               "nhờ đó kích thước của mọi vũng có thể được xác định chính xác, đồng thời tạo "
               "đường dẫn để thu gom và thải bỏ chúng. Khác với bể tách dầu/nước, mương "
               "thường không chứa chất lỏng dễ cháy nhưng có thể có khi xảy ra sự cố tràn. Sự "
               "hiện diện của chất lỏng trong mương vì thế hoặc là trong vận hành bình "
               "thường, hoặc chỉ là bất thường; và vì mương thực sự thoát chất lỏng đi nên "
               "tràn là bất thường. Điều này dẫn đến các khu vực nguy hiểm sau."))
    b.append(p("<b>Vùng 0.</b> Nếu dòng chảy vào mương là trong vận hành bình thường, bên trong "
               "mương là Vùng 0 do hiệu ứng tồn lưu mà sự giam giữ trong mương tạo ra. Trong "
               "các trường hợp khác không có Vùng 0; không được chấp nhận việc xả liên tục "
               "chất dễ cháy vào mương hở. Nếu phát thải vào mương là bất thường, Vùng 0 vẫn "
               "tồn tại bên trong mương tại những điểm mà do hình học của mương, chất lỏng "
               "tụ lại, đứng yên và tồn lưu cho đến khi bay hơi hết."))
    b.append(p("<b>Vùng 1.</b> Mương đóng vai trò như một vũng dài và hẹp, nên khu vực quanh "
               "nó đôi khi chứa bầu khí nổ do tác động của gió. Vùng 1 tồn tại quanh mương "
               "(xem Hình 3.14) dù phát thải vào mương là bình thường hay bất thường. Phạm vi "
               "danh nghĩa được chọn là 1 m; dù có phần tùy ý, giá trị này có khả năng lớn "
               "hơn khoảng cách thực tế nào đạt được. Việc chất lỏng tụ ở điểm thấp của "
               "mương ít ảnh hưởng đến phạm vi Vùng 1 nêu trên. Trong Hình 3.14, a = 1 m."))
    b.append(fig(11, FC.fig_f314()))
    b.append(p("<b>Vùng 2.</b> Sự kết hợp giữa phát thải bình thường vào mương và mương bị tắc "
               "có thể tạo vũng bên ngoài, vũng này lớn dần cho đến khi phát thải ngừng hoặc "
               "tốc độ bay hơi vượt tốc độ phát thải. Vũng này tạo Vùng 2 theo Bảng 3.7, với "
               "kích thước do bờ chắn giới hạn nếu có, hoặc do tính toán nếu không có bờ "
               "chắn (xem Chương 4)."))

    b.append(h4("3.4.8 Rãnh kỹ thuật", "3.4.8 Trenches"))
    b.append(p("Có hai loại rãnh thường gặp. Loại thứ nhất chứa đường ống và có khả năng rò "
               "bên trong do mối nối hoặc phớt van; rò có thể xảy ra trong vận hành bình "
               "thường (nguồn cấp chính) hoặc chỉ bất thường (nguồn cấp phụ). Những rãnh này "
               "được xử lý như mương, dựa trên loại rò và lượng chất lỏng dễ cháy rò ra. Nếu "
               "phát thải là khí hoặc hơi thì loại và phạm vi khu vực nguy hiểm lấy như thể "
               "rò xảy ra bên ngoài rãnh, nhưng phải kéo dài suốt chiều dài rãnh giữa các vị "
               "trí bị chặn. Người ta thường bố trí các chặn có chủ đích trong rãnh để ngăn "
               "vật liệu dễ cháy truyền từ khu vực này sang khu vực khác của nhà máy. Trong "
               "những trường hợp này, bên trong rãnh là Vùng 1 ngay cả khi phát thải chỉ là "
               "bất thường, vì chính rãnh gây tồn lưu."))
    b.append(p("Loại thứ hai là rãnh không dùng để chứa chất lỏng dễ cháy, chẳng hạn rãnh đi "
               "cáp. Loại này chỉ đáng kể khi nằm trong khu vực đã được xác định là nguy hiểm "
               "vì lý do khác. Khi đó khu vực nguy hiểm bên trong rãnh như sau: <b>Vùng 0 bên "
               "ngoài → Vùng 0 bên trong; Vùng 1 bên ngoài → Vùng 1 bên trong; Vùng 2 bên "
               "ngoài → Vùng 1 bên trong.</b> Việc nâng cấp từ Vùng 2 bên ngoài lên Vùng 1 "
               "bên trong là để tính đến sự tồn lưu trong rãnh. Khu vực trong rãnh lại tồn "
               "tại suốt chiều dài giữa các chặn. Mối quan hệ trên vẫn đúng trong trường hợp "
               "chất lỏng dễ cháy rò từ vũng bên ngoài vào rãnh; với chất lỏng, người ta giả "
               "định hành động được thực hiện trong thời gian hợp lý để loại bỏ vật liệu dễ "
               "cháy khỏi rãnh, và điều này được coi là thiết yếu."))
    b.append(note("<b>Khoảng trống nguồn.</b> Bảng 3.7, Bảng 3.9 và Bảng 3.10 chỉ được nhắc "
                  "tên trong phần này: dữ liệu của ba bảng nằm trong các trang bị thiếu (PDF "
                  "tr. 80–87), nên không có dòng dữ liệu nào được tái tạo. Các cột 50% và "
                  ">90% của Bảng 3.7, giả định gió 2 m/sec và các giá trị viện dẫn từ Bảng "
                  "3.9/3.10 được giữ lại như mô tả của nguồn, không phải như bảng dữ liệu."))
    return "".join(b)


def body_en():
    b = []
    b.append(h4("3.4.4 Road and rail tanks for flammable liquids",
                "3.4.4 Road and rail tanks for flammable liquids"))
    b.append(p("Liquids are regularly transported by road or rail. In general, the areas "
               "through which they pass in transit are not classified because the dwell "
               "time is short and any leakage during transit is abnormal, so the likelihood "
               "that a given area becomes contaminated with an explosive atmosphere is very "
               "low and area classification is not relevant. Care is needed, however: where "
               "transport tanks dwell for significant times, or where large numbers of them "
               "are stationary for a considerable time, area classification may become "
               "relevant. The usual dividing line is between general car parks, where tanks "
               "may reside overnight alongside other transporters, and locations "
               "specifically designated for tank parking, such as the vicinity of loading "
               "stations on airports."))
    b.append(p("This approach means that parking areas with general public access are not "
               "normally classified, whereas parking areas on sites where the materials are "
               "used and which are designated specifically for such tanks are classified. "
               "Typical examples are railway sidings dedicated to the marshalling of tanks, "
               "specific areas of dockyards dedicated to the location of tanks before "
               "loading or unloading, and similar locations in process plant areas. The "
               "generalization is not always valid, however: where many tankers regularly "
               "park, the division described above becomes harder to justify. Because such "
               "parking is uncontrolled, classic area classification cannot be used and the "
               "presence of the driver becomes critical. Routes and parking procedures need "
               "to be defined to minimize the number of tankers parked in any one location "
               "for significant periods, to reduce overnight parking and to ensure that "
               "there is no evidence of leakage when the vehicle is left; together these "
               "reduce the risk to an acceptable level. Many government regulations apply "
               "here, typically The Dangerous Substances (Conveyance by Road in Road Tankers "
               "and Tank Containers) Regulations 1981 (SI 1981/1059), which should be "
               "consulted."))
    b.append(p("Wherever tankers are loaded, off-loaded or parked when loaded in significant "
               "numbers, there is little justification for not applying the normal area "
               "classification procedures, and the tank and its contents then form a source "
               "of release unless particular sources are prevented. For example, release "
               "from tank vents may be removed by an extraction system so that no hazardous "
               "area forms beyond the immediate vicinity of the vent, but the vent exhaust "
               "still needs consideration. In addition, tanker bays used for unloading only "
               "will differ from those used for loading because there is little or no "
               "release from vents. The following treatment applies to tankers carrying "
               "unpressurized flammable liquids below their boiling point."))
    b.append(p("These tankers are normally of mostly welded construction, so the sources of "
               "release generally needing consideration are: releases from joints used for "
               "pipework connection; releases from vents during loading; and releases from "
               "flexible pipes used to connect the tanker to fixed plant. The classification "
               "below considers only the tanker itself and its immediate coupling; the "
               "fixed plant in the loading area must be dealt with separately. "
               "<b>Zone 0:</b> the interior of the tanker."))
    b.append(p("<b>Zone 1.</b> During loading or unloading there is always a danger of a small "
               "liquid leak while coupling or uncoupling. This is a primary grade source of "
               "release, so a Zone 1 must be defined around the coupling points. Its size is "
               "to a degree arbitrary because the amount of manually introduced leakage is "
               "unknown, but is not likely to be large: a Zone 1 of 1.5 m above and around "
               "the source of leakage, projected down to the ground as shown in Figure 3.12, "
               "should cover all eventualities. The downward projection reflects the "
               "likelihood that the vapour is heavier than air. In Figure 3.12, a = 1.5 m; b "
               "and c depend on the characteristics of the pool formed by any liquid "
               "release, and the dotted phi line is the limit of Zone 1 for the off-loading "
               "operation."))
    b.append(fig(9, FC.fig_f312()))
    b.append(p("During off-loading the hazardous area due to the vents does not exist, and "
               "the extent of Zone 1 from the coupling is then defined by the dotted lines "
               "in Figure 3.12. This Zone 1 extends right under the tanker to allow for the "
               "restricted ventilation caused by the tanker's presence. A third primary "
               "grade source of release is the flexible coupling pipe, which is subjected to "
               "regular movement and can fail in normal operation. Failure is likely to take "
               "the form of a small crack and, because the pressure is low (usually just the "
               "tank head pressure), the release is small. For this reason the Zone 1 "
               "produced is likewise limited to 1.5 m above and around the flexible "
               "coupling, projected vertically down to the ground."))
    b.append(p("<b>Zone 2.</b> This results from abnormal circumstances. The first is "
               "overfilling: liquid flows out of the vents, down the sides of the tank and "
               "ultimately forms a pool on the ground. The Zone 2 produced above and around "
               "the tank by this event is no larger than the Zone 1 from vapour release and "
               "will be invisible when road/rail tankers are loaded, but because it is "
               "abnormal it cannot be assumed not to exist in the unloading scenario. A Zone "
               "2 of 1.5 m above and around the tank will therefore be present in all "
               "circumstances and will be projected vertically down to the ground. The pool "
               "of flammable liquid grows until it is contained or until its vaporization "
               "rate equals the liquid release rate; the hazardous area created by this pool "
               "is Zone 2 and is sized as given in Table 3.7."))
    b.append(p("A second abnormal source is rupture of a flexible connecting pipe. Because of "
               "the reinforcement in such pipes, total rupture is not expected, so a release "
               "similar to that from rupture of a CAF gasket is considered a fair model. The "
               "released liquid forms a pool whose dimensions can be determined from Table "
               "3.3, and the extent of the hazardous area around that pool is then determined "
               "from Table 3.7. As the pressure is low, mist is unlikely to form and the Zone "
               "2 around the connecting pipe will be minimal; this is academic because the "
               "1.5 m Zone 1 already declared will encompass it. Finally, solar gain in "
               "road/rail tankers is highly unlikely unless they are parked for long periods "
               "in direct sunlight immediately before unloading. With proper care, only "
               "liquids with flashpoints below 32 °C need be considered."))
    b.append(p("Tankers containing gases or vapours under pressure, or liquefied gases or "
               "vapours (which are of course also under pressure), behave as any other "
               "vessel in such circumstances. The principal release mechanisms are: leakage "
               "during coupling and uncoupling; leakage due to valve actuator failure; "
               "leakage due to failure of fixed pipe joints; and leakage due to failure of "
               "flexible couplings. The interior of the tank is considered Zone 0 because, "
               "even though air is less likely to enter, there is always the possibility "
               "that the tank will regularly be empty and it is better to assume Zone 0 than "
               "to define and control such periods. This assumption will not normally be "
               "unnecessarily restrictive."))
    b.append(p("<b>Zone 1</b> results from three primary grade scenarios: two due to failure "
               "and one due to manual intervention. The first is the valve stem or "
               "actuator; the Zone 1 is based on that for a regularly operated valve, so a "
               "Zone 1 is assumed to exist for 1 m above and around the valve. The second is "
               "failure of the flexible coupling pipe: the orifice is expected to be small, "
               "total vaporization at the point of release can be assumed, and the release "
               "is treated as similar to leakage from a screwed joint; the Zone 1 is "
               "determined from Table 3.9 and that at ground level from Table 3.10. The "
               "third is manual intervention during coupling or uncoupling, expected to be "
               "so small that it is covered by the Zone 1 for flexible pipe failure; if the "
               "coupling point is remote from the flexible pipe it should be surrounded by a "
               "Zone 1 of similar proportions, with Tables 3.9 and 3.10 applying. <b>Zone "
               "2</b> arises from the flexible pipe, couplings, other joints and the valve "
               "actuating stem: the valve stem seal is treated as a spirally supported "
               "gasket and the flexible joint as a CAF gasket rupture, with extents derived "
               "from Tables 3.9 and 3.10. All of the above covers only the tanker and its "
               "immediate environs; fixed plant surrounding the tanker must be dealt with "
               "separately."))

    b.append(h4("3.4.5 Oil/water separators",
                "3.4.5 Oil/water separators"))
    b.append(p("Oil/water separators are open vessels into which a mixture of water and "
               "(usually spilled) oils is placed and allowed to dwell for a significant "
               "time, so that the water separates from the oil and the one can be disposed "
               "of while the other enters the normal drains. Theoretically the vessel "
               "normally contains mainly lower volatility oils, since oils of higher "
               "volatility will have undergone significant vaporization before the mixture "
               "reaches the separator. Where the majority of oils used at a site are of high "
               "volatility, this type of separation is not appropriate and another method "
               "should be chosen, because the hazardous areas it produces would not be "
               "acceptable."))
    b.append(p("<b>Zone 0</b> is the interior of the separator, but this zone does not extend "
               "beyond the extremities of the separator because the oils it contains are of "
               "low volatility. It would be unwise to use this type of separator if the oils "
               "were of high volatility, and some other approach should be used in those "
               "circumstances."))
    b.append(p("<b>Zone 1</b> occurs where the separator contains oils of higher volatility "
               "than normal and, through wind action, a hazardous area exists outside the "
               "separator. In these cases the mix of volatility should permit use of the 50 "
               "per cent column of Table 3.7, taking the area of the separator as the pool "
               "size. Where a significant number of the oils on the plant that may be fed to "
               "the separator are of high volatility, the >90 per cent column should be "
               "used. The hazardous area is shown in Figure 3.13 for a ground level "
               "separator; if the separator is above ground level with its base at or around "
               "ground level, Zone 1 merely extends vertically down the separator sides."))
    b.append(fig(10, FC.fig_f313()))
    b.append(p("<b>Zone 2</b> occurs in abnormal circumstances, such as after a major release "
               "of high volatility oil, when a larger hazardous area exists around the "
               "separator. Its extent is derived from Table 3.7 using the >90 per cent "
               "column. As stated above, this area becomes Zone 1 if a significant number of "
               "the oils used on the site are of high volatility; in such cases no Zone 2 is "
               "visible because its size is synonymous with that of Zone 1. Figure 3.13 "
               "shows a ground level separator; if the ground is at or about the base level "
               "of the separator, Zone 2 is projected vertically down the separator side. A "
               "wind speed of 2 m/sec is assumed when using Table 3.7."))
    b.append(p("Finally, if the separator overflows, a pool of mixed oil and water forms. The "
               "associated Zone 2 is derived from Table 3.7 assuming the highest volatility "
               "oil is present. Because water is present and may carry the mixture further "
               "than oil alone, it is advisable to limit the pool mechanically with "
               "containment sized to hold the maximum possible overflow. That containment "
               "size should then be used in all circumstances when determining extents from "
               "Table 3.7, even where the equilibrium pool size is smaller."))

    b.append(h4("3.4.6 Other open vessels", "3.4.6 Other open vessels"))
    b.append(p("Open vessels behave in a very similar manner to oil/water separators, except "
               "that usually only one flammable material is present. <b>Zone 0</b> is the "
               "interior of the vessel. <b>Zone 1</b> is as for an oil/water separator but "
               "defined, where appropriate, on the basis of the boiling point of the single "
               "flammable liquid. As before, open vessels are not recommended where the "
               "boiling point of the contained liquid is less than twice the ambient "
               "temperature of the location (in the United Kingdom this effectively means "
               "boiling points above 65 °C). This differs from the low volatility criterion "
               "used for sampling points in Section 3.4.9, where the boiling point must be at "
               "least four times ambient."))
    b.append(p("The only situation giving rise to <b>Zone 2</b> is overflow, and the resulting "
               "Zone 2 should be defined as for oil/water separators in that circumstance."))

    b.append(h4("3.4.7 Open drains", "3.4.7 Open drains"))
    b.append(p("Open drainage gullies are often used to collect released flammable liquids so "
               "that the dimensions of any pool can be accurately defined and to provide a "
               "route for collection and disposal. Unlike oil/water separators, they do not "
               "normally contain flammable liquids but may do so in cases of spillage. The "
               "presence of such liquids within them is therefore either in normal operation "
               "or abnormal only, and because the gullies actually drain the liquid away, "
               "overflow is abnormal. This leads to the following hazardous areas."))
    b.append(p("<b>Zone 0.</b> If the flow into the drain is in normal operation, the interior "
               "of the drain is Zone 0 because of the persistence effect introduced by "
               "containment within the drain. In other cases no Zone 0 exists; it would not "
               "be acceptable for flammable material to discharge continuously into an open "
               "drain. If release into the drain is abnormal, a Zone 0 will still exist within "
               "the drain at any point where the geometry causes liquid to collect, become "
               "static and persist until it has all evaporated."))
    b.append(p("<b>Zone 1.</b> The drain acts as a long narrow pool and the area around it "
               "will from time to time contain an explosive atmosphere through wind action. "
               "A Zone 1 exists around the drain (see Figure 3.14) whether release into it is "
               "in normal or abnormal operation. This is nominally 1 m; although to a degree "
               "arbitrary, it is likely to be larger than any practical distance achieved. "
               "Collection of flammable liquids at low spots in the drain is unlikely to "
               "affect this extent. In Figure 3.14, a = 1 m."))
    b.append(fig(11, FC.fig_f314()))
    b.append(p("<b>Zone 2.</b> Normal release into the drain coincident with drain blockage "
               "can produce an external pool, which grows until the release stops or the "
               "evaporation rate exceeds the release rate. This pool produces a Zone 2 in "
               "accordance with Table 3.7, its dimensions being set by containment where this "
               "exists or by calculation where no containment exists (see Chapter 4)."))

    b.append(h4("3.4.8 Trenches", "3.4.8 Trenches"))
    b.append(p("Two types of trench are normally encountered. The first contains pipework, "
               "with the possibility of leakage inside it from pipe joints or valve seals. "
               "Such a leak can occur in normal operation (a primary grade release) or only "
               "abnormally (a secondary grade source), and the trench should be treated in "
               "the same way as a drain based on the type of leak and the quantity of "
               "flammable material leaking, if the leak is liquid. If the release is of gas "
               "or vapour, the types and extents of hazardous areas should be those produced "
               "by a leak occurring outside the trench, but should extend throughout any "
               "length of trench between blockages. Deliberate blockages are normally placed "
               "in trenches to prevent flammable materials being transmitted from one part "
               "of a plant to another. In these cases the interior of the trench is Zone 1 "
               "even if the release is only abnormal, because of the persistence introduced "
               "by the trench."))
    b.append(p("The second type is not intended to contain any flammable material, such as a "
               "trench used for a cable route. Such trenches only matter insofar as they lie "
               "in areas defined as hazardous for another reason. The hazardous area inside "
               "the trench is then: <b>external Zone 0 → internal Zone 0; external Zone 1 → "
               "internal Zone 1; external Zone 2 → internal Zone 1.</b> The upgrade from "
               "external Zone 2 to internal Zone 1 allows for persistence within the trench. "
               "The hazardous area within the trench again exists for the entire length "
               "between blockages. The same relationship holds where flammable liquid leaks "
               "into the drain from an external pool; in the case of liquids it is assumed "
               "that action is taken within a reasonable time to remove the flammable "
               "material from the drain, which is considered essential."))
    b.append(note("<b>Source gap.</b> Tables 3.7, 3.9 and 3.10 are named only in this section: "
                  "their data lie in the missing pages (PDF pp. 80-87), so no rows are "
                  "reproduced. The 50 per cent and >90 per cent columns of Table 3.7, the 2 "
                  "m/sec wind assumption, and the values cited from Tables 3.9/3.10 are "
                  "retained as descriptions from the source, not as tabulated data."))
    return "".join(b)
