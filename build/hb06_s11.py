# -*- coding: utf-8 -*-
"""Handbook 6.11 — Optical Fiber Displacement Sensors (Claus, Bhatia & Wang)."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Mục này trình bày một phân tích lý thuyết và thực nghiệm chặt chẽ về các cảm biến sợi quang có chiều dài "
        "chuẩn ngắn dùng để đo biến dạng chu kỳ trên hoặc trong vật liệu. Bốn loại cảm biến khác nhau được đánh giá "
        "một cách có hệ thống theo nhiều tiêu chí hiệu năng như độ phân giải biến dạng, dải động, độ nhạy chéo với "
        "các nhiễu động môi trường khác, mức độ đơn giản của việc chế tạo, và độ phức tạp của quá trình giải điều "
        "chế. Các phương pháp cảm biến được khảo sát gồm những công nghệ đã được khẳng định như cách tử Bragg sợi "
        "quang, và những kỹ thuật đo đang phát triển nhanh như cách tử chu kỳ dài. Ngoài các cảm biến dựa trên cách "
        "tử, hai phiên bản phổ biến của cảm biến giao thoa Fabry–Perot (nội và ngoại) cũng được đánh giá về mức độ "
        "phù hợp. Một nghiên cứu lý thuyết về độ nhạy chéo của các cảm biến này với một tổ hợp vectơ biến dạng và "
        "nhiệt độ bất kỳ, tương tự như nghiên cứu Sirkis đề xuất trong bài báo SPIE năm 1991 [1], cũng sẽ được "
        "triển khai."))
    b.append(p(
        "Bố cục của mục này như sau. Nguyên lý hoạt động và quy trình chế tạo của từng cảm biến trong bốn loại được "
        "trình bày riêng. Độ nhạy với biến dạng và với các nhiễu động đồng thời khác như nhiệt độ được phân tích. "
        "Tổng chi phí và hiệu năng của một kỹ thuật cảm biến phụ thuộc rất nhiều vào quá trình giải điều chế tín "
        "hiệu; các sơ đồ phát hiện cho cả bốn cảm biến được thảo luận và so sánh theo độ phức tạp. Cuối cùng, một "
        "phân tích lý thuyết về độ nhạy chéo của bốn sơ đồ cảm biến được trình bày và hiệu năng của chúng được so "
        "sánh."))
    b.append(p(
        "Việc đo biến dạng bằng cảm biến sợi quang ở cả cấu hình nhúng trong vật liệu lẫn cấu hình dán trên bề mặt "
        "đã được các nhà nghiên cứu báo cáo trước đây [2]. Cảm biến sợi quang có kích thước nhỏ, không bị nhiễu điện "
        "từ, và có thể dễ dàng tích hợp với các tuyến thông tin sợi quang hiện có. Những cảm biến như vậy thường có "
        "thể được ghép kênh dễ dàng, tạo ra các mạng phân tán dùng để giám sát sức khoẻ của vật liệu và kết cấu "
        "hiệu năng cao tích hợp. Cảm biến sợi quang dùng đo biến dạng cần có một số đặc tính quan trọng. Chúng phải "
        "hoặc không nhạy với dao động nhiệt độ và áp suất môi trường, hoặc phải có kỹ thuật giải điều chế bù được "
        "những thay đổi của tín hiệu đầu ra do các nhiễu động không mong muốn gây ra. Ở cấu hình nhúng, cảm biến đo "
        "biến dạng dọc trục phải có độ nhạy chéo tối thiểu với các trạng thái biến dạng khác. Bản thân tín hiệu cảm "
        "biến phải đơn giản và dễ giải điều chế; tính phi tuyến của đầu ra đòi hỏi những thủ tục giải mã đắt tiền "
        "hoặc phải hiệu chuẩn trước cảm biến. Cảm biến lý tưởng phải cho một phép đo biến dạng tuyệt đối và theo thời "
        "gian thực ở dạng dễ xử lý. Với những môi trường dự kiến có biến dạng lớn, cảm biến phải có dải động rộng "
        "đồng thời vẫn duy trì được độ nhạy mong muốn. Phần tiếp theo thảo luận riêng từng sơ đồ cảm biến trong bốn "
        "sơ đồ, cùng những ưu nhược điểm tương đối của chúng."))

    # ------------------------------------------------------------- EFPI
    b.append(h2("Cảm biến giao thoa Fabry–Perot ngoại", "Extrinsic Fabry–Perot interferometric sensor"))
    b.append(p(
        "Cảm biến giao thoa Fabry–Perot ngoại (EFPI) do Murphy và cộng sự đề xuất là một trong những cảm biến sợi "
        "quang phổ biến nhất dùng cho các ứng dụng giám sát sức khoẻ của vật liệu và kết cấu thông minh [3]. Đúng "
        "như tên gọi, EFPI là một cảm biến giao thoa trong đó cường độ được phát hiện bị điều biến bởi chính tham số "
        "cần đo. Cấu hình đơn giản nhất của EFPI được trình bày trên Hình 6-99."))
    b.append(fig(99, F.fig_6_99()))
    b.append(p(
        "Hệ EFPI gồm một laser diode đơn mode chiếu sáng một khoang Fabry–Perot qua một bộ ghép sợi thuôn nóng chảy. "
        "Khoang được tạo giữa một sợi đơn mode dẫn vào và một sợi đơn mode hoặc đa mode phản xạ. Vì khoang nằm ngoài "
        "sợi dẫn vào và dẫn ra, cảm biến EFPI độc lập với biến dạng ngang và với những dao động nhiệt độ môi trường "
        "nhỏ. Sợi dẫn vào và sợi phản xạ được căn chỉnh nhờ một sợi silica lõi rỗng. Với đầu sợi không phủ lớp, tại "
        "cả hai đầu xuất hiện một phản xạ Fresnel 4%. Phản xạ thứ nhất, R1, gọi là phản xạ tham chiếu, độc lập với "
        "nhiễu động áp đặt. Phản xạ thứ hai, R2, gọi là phản xạ cảm biến, phụ thuộc chiều dài khoang d, mà chiều dài "
        "ấy lại bị điều biến bởi nhiễu động áp đặt. Hai phản xạ này giao thoa với nhau (với điều kiện 2d < L<sub>c</sub>, "
        "độ dài kết hợp của laser diode), và cường độ I tại đầu dò biến thiên theo chiều dài khoang:"))
    b.append(eq("I = I₀ cos² (4πd / λ)", "6.117"))
    b.append(p(
        "trong đó I₀ là giá trị lớn nhất của cường độ đầu ra và λ là bước sóng trung tâm của laser diode."))
    b.append(p(
        "Đường cong hàm truyền điển hình của EFPI được trình bày trên Hình 6-100. Những nhiễu động nhỏ khiến cảm "
        "biến làm việc quanh điểm làm việc tĩnh hay điểm Q dẫn tới một biến thiên tuyến tính của cường độ đầu ra. Một "
        "vân trong tín hiệu đầu ra được định nghĩa là sự thay đổi cường độ từ một cực đại tới một cực đại, hoặc từ "
        "một cực tiểu tới một cực tiểu. Mỗi vân ứng với một thay đổi chiều dài khoang bằng một nửa bước sóng làm "
        "việc λ. Thay đổi chiều dài khoang Δd sau đó được dùng để tính biến dạng ε theo biểu thức:"))
    b.append(fig(100, F.fig_6_100()))
    b.append(eq("ε = Δd / L", "6.118"))
    b.append(p(
        "trong đó L là chiều dài chuẩn của cảm biến, thường là khoảng cách giữa hai điểm mà sợi dẫn vào và sợi phản "
        "xạ được gắn vào sợi lõi rỗng. Việc làm cho biên độ hai tín hiệu phản xạ bằng nhau cho phép đạt độ tương "
        "phản vân tốt trong tín hiệu đầu ra."))
    b.append(p(
        "Cảm biến EFPI đã được dùng rộng rãi để đo tải trọng mỏi trên cánh máy bay F-15, phát hiện sự hình thành và "
        "lan truyền vết nứt trong các kết cấu dân dụng, và giám sát quá trình đóng rắn cũng như tuổi thọ của các mẫu "
        "bê tông và vật liệu composite [2, 4]. Tính không nhạy với nhiệt độ khiến cảm biến này hấp dẫn với rất nhiều "
        "ứng dụng. EFPI có khả năng đo những dịch chuyển dưới một angstrom với độ phân giải biến dạng tốt hơn 1 µε và "
        "dải động lớn hơn 10.000 µε. Mặc dù sự thay đổi cường độ đầu ra của EFPI là phi tuyến theo độ lớn của tham "
        "số cần đo, với những nhiễu động nhỏ có thể giới hạn vùng làm việc quanh điểm Q của đường cong hàm truyền. "
        "Hơn nữa, băng thông lớn sẵn có của cảm biến này làm đơn giản việc đo biến dạng có tính chu kỳ cao. EFPI có "
        "khả năng làm việc một đầu, nên phù hợp với những ứng dụng nơi việc tiếp cận vùng thử bị hạn chế. Cảm biến "
        "chỉ cần thiết bị chế tạo đơn giản, rẻ tiền và thời gian lắp ráp dưới 10 phút. Thêm nữa, vì khoang nằm ngoài "
        "các sợi, những thành phần biến dạng ngang — vốn ảnh hưởng tới cảm biến nội thông qua hiệu ứng Poisson — hầu "
        "như không tác động lên đầu ra của EFPI. Việc chỉ nhạy với biến dạng dọc trục và không nhạy với trạng thái "
        "phân cực đầu vào đã khiến EFPI trở thành cảm biến sợi quang được ưa chuộng nhất cho các ứng dụng nhúng [1]. "
        "Nhìn chung, hệ cảm biến EFPI rất phù hợp để đo biến dạng chu kỳ có độ lớn nhỏ."))
    b.append(p(
        "Mặc dù đã có một phiên bản EFPI cho đầu ra tuyệt đối được trình diễn, phiên bản ấy thiếu băng thông thường "
        "được mong muốn khi đo biến dạng chu kỳ [5]. Gần đây chúng tôi cũng đã đề xuất một cảm biến EFPI có khoang "
        "ngắn và độ tinh xảo cao để đo những nhiễu động nhỏ [6]. Cấu hình này có đầu ra đơn giản, có thể giải điều "
        "chế bằng một tổ hợp lọc quang và đầu dò quang."))

    # ------------------------------------------------------------- IFPI
    b.append(h2("Cảm biến giao thoa Fabry–Perot nội", "Intrinsic Fabry–Perot interferometric sensor"))
    b.append(p(
        "Cảm biến giao thoa Fabry–Perot nội (IFPI) hoạt động tương tự phiên bản ngoại nhưng có những khác biệt đáng "
        "kể về cấu hình [7]. Cảm biến IFPI cơ bản được trình bày trên Hình 6-101. Một laser diode đã cách ly quang "
        "được dùng làm nguồn quang cho một trong các nhánh vào của bộ ghép 2 × 2 hai chiều. Khoang Fabry–Perot được "
        "tạo bằng cách hàn nóng chảy một đoạn ngắn sợi đơn mode vào một trong các nhánh ra của bộ ghép. Như trên "
        "Hình 6-101, phản xạ tham chiếu (R) và phản xạ cảm biến (S) giao thoa tại mặt đầu dò, cho một biến thiên "
        "cường độ dạng sin. Khoang cũng có thể đạt được bằng cách đưa vào hai điểm phản xạ Fresnel — những chỗ gián "
        "đoạn chiết suất — dọc theo chiều dài của một sợi duy nhất. Tính nhạy sáng của sợi germano-silicat trước đây "
        "đã được dùng để chế tạo những điểm phản xạ băng rộng bao quanh một khoang IFPI [8]. Vì khoang được tạo bên "
        "trong một sợi quang, những thay đổi chiết suất của sợi do nhiễu động áp đặt có thể làm thay đổi đáng kể pha "
        "của tín hiệu cảm biến S. Do đó, khoang nội khiến cảm biến nhạy với dao động nhiệt độ môi trường và với mọi "
        "trạng thái biến dạng."))
    b.append(fig(101, F.fig_6_101()))
    b.append(p(
        "Cảm biến IFPI, giống như mọi tín hiệu giao thoa khác, có đầu ra phi tuyến, điều này làm phức tạp việc đo "
        "biến dạng có độ lớn lớn. Có thể khắc phục bằng cách cho cảm biến làm việc trong vùng tuyến tính quanh điểm Q "
        "của đường cong hàm truyền dạng sin. Hạn chế chính của cảm biến biến dạng IFPI là sự thay đổi chiết suất do "
        "hiệu ứng quang đàn hồi dẫn tới một quan hệ phi tuyến giữa nhiễu động áp đặt và thay đổi chiều dài khoang. "
        "Thực tế, với hầu hết cảm biến IFPI, sự thay đổi hằng số lan truyền của mode cơ bản chi phối sự thay đổi "
        "chiều dài khoang. Do đó IFPI rất dễ bị ảnh hưởng bởi thay đổi nhiệt độ và bởi các thành phần biến dạng ngang "
        "[1]. Trong các ứng dụng nhúng, độ nhạy với mọi thành phần biến dạng có thể dẫn tới những đầu ra sai."))
    b.append(p(
        "Quy trình chế tạo cảm biến biến dạng IFPI phức tạp hơn so với EFPI vì khoang cảm biến phải được tạo bên "
        "trong sợi quang bằng một thủ tục đặc biệt nào đó. Độ phân giải biến dạng của IFPI cũng được dự kiến vào "
        "khoảng 1 µε với dải làm việc lớn hơn 10.000 µε. Cảm biến IFPI còn bị trôi tín hiệu đầu ra do biến thiên "
        "trạng thái phân cực của ánh sáng đầu vào."))
    b.append(p(
        "Như vậy, phân tích sơ bộ cho thấy phiên bản ngoại của cảm biến sợi quang Fabry–Perot dường như có ưu thế "
        "tổng thể so với phiên bản nội. Cảm biến ngoại có độ nhạy chéo không đáng kể với nhiệt độ và biến dạng ngang. "
        "Mặc dù độ nhạy biến dạng, dải động và băng thông của hai cảm biến là tương đương, IFPI có thể đắt và cồng "
        "kềnh khi chế tạo do bản chất nội của khoang cảm biến."))
    b.append(p(
        "Cả hai cảm biến giao thoa Fabry–Perot ngoại và nội đều có đầu ra dạng sin phi tuyến, làm phức tạp việc xử lý "
        "tín hiệu ở phía thu. Mặc dù cảm biến dựa trên cường độ có biến thiên đầu ra đơn giản, chúng bị hạn chế về độ "
        "nhạy với biến dạng hay các nhiễu động quan tâm khác. Các cảm biến dựa trên cách tử gần đây đã trở nên phổ "
        "biến như những đầu đo cho tín hiệu đầu ra được mã hoá theo bước sóng, thường có thể giải điều chế dễ dàng để "
        "suy ra thông tin về nhiễu động đang khảo sát. Ưu nhược điểm của công nghệ cảm biến cách tử Bragg được thảo "
        "luận trước. Cơ chế hoạt động cơ bản của cảm biến biến dạng dựa trên cách tử Bragg được làm rõ và các biểu "
        "thức cho độ phân giải biến dạng được rút ra. Sau đó các cảm biến này được so sánh với cách tử chu kỳ dài "
        "mới phát triển về quy trình chế tạo, độ nhạy chéo với các tham số khác, và mức độ đơn giản của việc giải "
        "điều chế tín hiệu."))

    # ------------------------------------------------------------- FBG
    b.append(h2("Cảm biến cách tử Bragg sợi quang", "Fiber Bragg grating sensor"))
    b.append(p(
        "Hiện tượng nhạy sáng trong sợi quang được Hill và cộng sự phát hiện năm 1978 [9]. Người ta thấy rằng có thể "
        "tạo ra những thay đổi chiết suất vĩnh viễn trong sợi bằng cách cho lõi pha germani tiếp xúc với ánh sáng "
        "mạnh ở 488 hoặc 514 nm. Sự điều biến sin của chiết suất trong lõi do biến thiên không gian của chùm ghi tạo "
        "ra một cách tử chiết suất có thể dùng để ghép năng lượng trong mode dẫn cơ bản sang các mode dẫn và mode tổn "
        "hao khác nhau. Sau đó Meltz và cộng sự đề xuất rằng tính nhạy sáng hiệu quả hơn nếu sợi được chiếu nghiêng "
        "qua một hình vân ở những bước sóng gần bước sóng hấp thụ (242 nm) của các khuyết tật germani trong sợi "
        "[10]. Quá trình ghi nghiêng đã đơn giản hoá việc chế tạo cách tử Bragg, và những linh kiện này gần đây đã "
        "nổi lên như những thành phần rất linh hoạt cho các hệ thống thông tin và cảm biến. Gần đây, việc nạp hydro "
        "vào sợi được báo cáo là cho mức thay đổi chiết suất cao hơn hai bậc độ lớn trong sợi germano-silicat [11]."))

    b.append(h3("Nguyên lý hoạt động", "Principle of operation"))
    b.append(p(
        "Cách tử Bragg dựa trên điều kiện phù hợp pha giữa các mode không gian lan truyền trong sợi quang. Điều kiện "
        "phù hợp pha này được cho bởi:"))
    b.append(eq("k<sub>g</sub> + k<sub>c</sub> = k<sub>B</sub>", "6.119"))
    b.append(p(
        "trong đó k<sub>g</sub>, k<sub>c</sub> và k<sub>B</sub> lần lượt là vectơ sóng của mode dẫn được ghép, của "
        "mode ghép tạo thành, và của cách tử. Với tương tác bậc một, k<sub>B</sub> = 2π/Λ, với Λ là chu kỳ cách tử. "
        "Vì thông lệ là dùng hằng số lan truyền khi làm việc với các mode sợi quang, điều kiện này rút gọn thành "
        "phương trình được dùng rộng rãi cho ghép mode do một nhiễu động tuần hoàn:"))
    b.append(eq("Δβ = 2π / Λ", "6.120"))
    b.append(p(
        "trong đó Δβ là hiệu các hằng số lan truyền của hai mode tham gia ghép mode (cả hai được giả định lan truyền "
        "cùng chiều)."))
    b.append(p(
        "Cách tử Bragg sợi quang (FBG) liên quan tới việc ghép mode dẫn sóng quang LP₀₁ cơ bản lan truyền thuận với "
        "mode LP₀₁ lan truyền ngược [12]. Xét một sợi đơn mode với β₀₁ và −β₀₁ là hằng số lan truyền của các mode "
        "LP₀₁ cơ bản lan truyền thuận và ngược. Để thoả mãn điều kiện phù hợp pha:"))
    b.append(eq("−β₀₁ − β₀₁ = −2π / Λ", "6.121"))
    b.append(p(
        "trong đó β₀₁ = 2πn<sub>eff</sub>/λ (n<sub>eff</sub> là chiết suất hiệu dụng của mode cơ bản và λ là bước "
        "sóng trong chân không). Phương trình 6.121 rút gọn thành [12]:"))
    b.append(eq("λ<sub>B</sub> = 2Λn<sub>eff</sub>", "6.122"))
    b.append(p(
        "trong đó λ<sub>B</sub> được gọi là bước sóng Bragg. Bước sóng Bragg là bước sóng tại đó mode LP₀₁ lan truyền "
        "thuận ghép với mode LP₀₁ lan truyền ngược. Sự ghép này phụ thuộc bước sóng vì hằng số lan truyền của hai "
        "mode là hàm của bước sóng. Do đó, nếu một FBG được hỏi bằng một nguồn quang băng rộng, bước sóng tại đó xảy "
        "ra phù hợp pha sẽ bị phản xạ trở lại. Bước sóng này là hàm của chu kỳ cách tử (Λ) và chiết suất hiệu dụng "
        "(n<sub>eff</sub>) của mode cơ bản (phương trình 6.122). Vì các hiệu ứng biến dạng và nhiệt độ có thể điều "
        "biến cả hai tham số ấy, bước sóng Bragg dịch theo những nhiễu động bên ngoài này. Độ dịch phổ này được khai "
        "thác để chế tạo FBG cho các ứng dụng cảm biến."))
    b.append(fig(102, F.fig_6_102()))
    b.append(p(
        "Hình 6-102 trình bày cơ chế ghép mode trong cách tử Bragg sợi quang bằng giản đồ β. Vì hiệu các hằng số lan "
        "truyền (Δβ) giữa hai mode tham gia ghép là lớn, phương trình 6.120 cho thấy chỉ cần một giá trị chu kỳ Λ nhỏ "
        "để tạo ra ghép mode này. Thông thường với các ứng dụng viễn thông, giá trị λ<sub>B</sub> vào khoảng 1,5 µm. "
        "Từ phương trình 6.122, Λ được xác định là 0,5 µm (với n<sub>eff</sub> = 1,5). Do chu kỳ nhỏ (cỡ 1 µm), FBG "
        "được xếp vào loại cách tử chu kỳ ngắn."))

    b.append(h3("Kỹ thuật chế tạo", "Fabrication techniques"))
    b.append(p(
        "Cách tử Bragg sợi quang thường được chế tạo bằng hai kỹ thuật chiếu nghiêng: phương pháp giao thoa và "
        "phương pháp mặt nạ pha. Phương pháp giao thoa, được mô tả trên Hình 6-103, gồm một chùm UV ở 244 hoặc "
        "248 nm được bộ tách chùm chia thành hai phần bằng nhau [10]. Hai chùm sau đó được hội tụ lên một đoạn sợi "
        "pha Ge (đã bóc lớp bảo vệ) bằng các thấu kính trụ, và chu kỳ của vân giao thoa tạo thành — do đó cả bước "
        "sóng Bragg — được thay đổi bằng cách thay đổi góc hợp nhau θ. Hạn chế của phương pháp này là mọi rung động "
        "tương đối của cặp gương và thấu kính đều có thể làm suy giảm chất lượng của cách tử cuối cùng, và do đó "
        "toàn bộ hệ có yêu cầu ổn định rất khắt khe. Để khắc phục nhược điểm này, Kashyap và cộng sự đã đề xuất một "
        "kỹ thuật giao thoa mới, trong đó hiệu quang trình giữa hai chùm UV giao thoa được tạo ra nhờ truyền qua một "
        "lăng kính vuông góc (Hình 6-104) [12]. Kỹ thuật này ổn định về bản chất vì mọi rung động của lăng kính đều "
        "tác động như nhau lên cả hai chùm."))
    b.append(fig(103, F.fig_6_103()))
    b.append(fig(104, F.fig_6_104()))
    b.append(p(
        "Phương pháp mặt nạ pha gần đây đã trở nên phổ biến như một thủ tục ghi nghiêng bằng holography hiệu quả để "
        "chế tạo cách tử [13]. Trong phương pháp này, như trên Hình 6-105, một chùm UV tới bị nhiễu xạ thành các bậc "
        "−1, 0 và +1 bởi một cách tử nổi tạo trên bản silica bằng chiếu chùm điện tử và ăn mòn plasma. Hai bậc nhiễu "
        "xạ thứ nhất phản xạ toàn phần tại mặt phân cách thuỷ tinh/không khí của một lăng kính chữ nhật rồi giao thoa "
        "trên bề mặt sợi trần đặt ngay sau mặt nạ. Kỹ thuật này phụ thuộc bước sóng vì chu kỳ của vân giao thoa hai "
        "chùm tạo thành được quyết định duy nhất bởi góc nhiễu xạ của các bậc −1 và +1, và do đó bởi tính chất của "
        "mặt nạ pha. Rõ ràng là cần những mặt nạ pha khác nhau để chế tạo cách tử ở các bước sóng Bragg khác nhau. Sơ "
        "đồ bố trí theo dõi chủ động sự phát triển của cách tử qua phổ truyền trong khi chế tạo được trình bày trên "
        "Hình 6-106."))
    b.append(fig(105, F.fig_6_105()))
    b.append(fig(106, F.fig_6_106()))

    b.append(h3("Cảm biến cách tử Bragg", "Bragg grating sensors"))
    b.append(p(
        "Từ phương trình 6.122 ta thấy rằng một thay đổi của n<sub>eff</sub> và/hoặc Λ có thể làm bước sóng Bragg λ "
        "dịch đi. Thay đổi tương đối của bước sóng cộng hưởng, Δλ/λ, được cho bởi biểu thức:"))
    b.append(eq("Δλ / λ = ΔΛ / Λ + Δn<sub>eff</sub> / n<sub>eff</sub>", "6.123"))
    b.append(p(
        "trong đó ΔΛ/Λ và Δn<sub>eff</sub>/n<sub>eff</sub> lần lượt là các thay đổi tương đối của chu kỳ và của chiết "
        "suất hiệu dụng. Độ lớn tương đối của hai thay đổi này phụ thuộc loại nhiễu động mà cách tử chịu tác dụng; "
        "với hầu hết ứng dụng, hiệu ứng do thay đổi chiết suất hiệu dụng là cơ chế chi phối."))
    b.append(p(
        "Mọi biến dạng dọc trục ε áp lên cách tử đều làm thay đổi chu kỳ và chiết suất hiệu dụng, dẫn tới một độ "
        "dịch của bước sóng Bragg, cho bởi:"))
    b.append(eq("Δλ / λ = ε + Δn<sub>eff</sub> / n<sub>eff</sub>", "6.124"))
    b.append(p(
        "Số hạng thứ nhất ở vế phải bằng một đơn vị, còn số hạng thứ hai có nguồn gốc từ hiệu ứng quang đàn hồi. Một "
        "biến dạng dọc trục trên sợi làm thay đổi chiết suất của cả lõi lẫn lớp bọc. Điều này dẫn tới biến thiên của "
        "chiết suất hiệu dụng của thuỷ tinh. Hệ số quang đàn hồi hay hệ số biến dạng–quang liên hệ sự thay đổi chiết "
        "suất do dịch chuyển cơ khí có giá trị khoảng −0,27. Như vậy, biến thiên của n<sub>eff</sub> và Λ do biến dạng "
        "có tác dụng ngược chiều nhau lên đỉnh Bragg. Thay đổi tương đối của bước sóng Bragg do biến dạng dọc trục là "
        "0,73ε, tức 73% của biến dạng áp đặt. Ở 1550 và 1300 nm, độ dịch bước sóng cộng hưởng lần lượt là 11 nm/%ε và "
        "9 nm/%ε. Với nhiệt độ, một FBG ở 1500 nm dịch 1,6 nm cho mỗi 100 °C tăng nhiệt độ [9]."))

    b.append(h3("Hạn chế của cảm biến biến dạng cách tử Bragg",
                "Limitations of Bragg grating strain sensors"))
    b.append(p(
        "Hạn chế lớn của cảm biến cách tử Bragg là kỹ thuật chế tạo phức tạp và đắt tiền. Mặc dù ghi nghiêng được "
        "dùng phổ biến để chế tạo các cách tử này, yêu cầu về những mặt nạ pha đắt tiền làm tăng chi phí của hệ cảm "
        "biến. Trong kỹ thuật giao thoa, độ ổn định của sơ đồ là yếu tố then chốt để có được cách tử chất lượng cao. "
        "Vì cần những thay đổi chiết suất cỡ 10⁻³ để chế tạo các cách tử này, cần những xung laser có mức năng lượng "
        "cao. Điều này có thể làm giảm tuổi thọ làm việc của laser và dẫn tới chi phí bảo trì tăng. Thêm nữa, việc "
        "đưa hydro hoặc deuteri vào sợi cho phép điều biến chiết suất lớn hơn nhờ quá trình chiếu xạ."))
    b.append(p(
        "Hạn chế lớn thứ hai của cách tử Bragg là băng thông hạn chế. Giá trị điển hình của độ rộng toàn phần tại nửa "
        "cực đại (FWHM) nằm trong khoảng 0,1 đến 1 nm. Mặc dù có thể đạt băng thông cao hơn bằng cách tạo chirp cho "
        "chiết suất hoặc chu kỳ dọc theo chiều dài cách tử, việc này làm tăng chi phí chế tạo. Băng thông hạn chế đòi "
        "hỏi những máy phân tích phổ có độ phân giải cao để theo dõi phổ cách tử. Kersey và cộng sự đã đề xuất một "
        "giao thoa kế Mach–Zehnder không cân bằng để phát hiện độ dịch bước sóng do nhiễu động [14]. Hai nhánh không "
        "bằng nhau của giao thoa kế Mach–Zehnder được kích thích bởi phản xạ ngược từ một phần tử cảm biến cách tử "
        "Bragg. Mọi thay đổi của bước sóng quang đầu vào đều điều biến hiệu pha giữa hai nhánh và tạo ra một cường độ "
        "hình sin biến thiên theo thời gian ở đầu ra. Tín hiệu giao thoa này có thể liên hệ với độ dịch của đỉnh Bragg "
        "và do đó xác định được độ lớn của nhiễu động. Gần đây, các giao thoa kế mode cũng đã được đề xuất để giải "
        "điều chế đầu ra của cảm biến cách tử Bragg [15]. Các giao thoa kế không cân bằng cũng dễ bị ảnh hưởng bởi "
        "nhiễu động bên ngoài, nên cần được cách ly khỏi tham số đang khảo sát. Hơn nữa, đầu ra phi tuyến có thể đòi "
        "hỏi thiết bị đếm vân — vốn có thể phức tạp và đắt tiền. Thêm nữa, sự đổi chiều của nhiễu động tại các cực đại "
        "hoặc cực tiểu của đường cong hàm truyền sẽ không được sơ đồ giải điều chế này phát hiện. Để khắc phục hạn "
        "chế đó, có thể dùng hai giao thoa kế không cân bằng cho các phép đo động."))
    b.append(p(
        "Độ nhạy chéo với dao động nhiệt độ dẫn tới những phép đo biến dạng sai trong các ứng dụng mà nhiệt độ môi "
        "trường biến thiên theo thời gian. Do đó phải dùng một cách tử tham chiếu đo thay đổi nhiệt độ để bù cho đầu ra "
        "của cảm biến biến dạng. Gần đây, cảm biến không phụ thuộc nhiệt độ đã được trình diễn bằng cách dùng cách tử "
        "tạo chirp ghi trên sợi quang thuôn (taper) [16]."))
    b.append(p(
        "Cuối cùng, độ nhạy của cảm biến biến dạng cách tử Bragg sợi quang có thể chưa đủ với một số ứng dụng. Độ nhạy "
        "của cảm biến phụ thuộc vào độ dịch bước sóng nhỏ nhất phát hiện được ở phía thu. Mặc dù có thể đạt độ phân "
        "giải bước sóng rất tốt bằng các kỹ thuật phát hiện giao thoa không cân bằng, các máy phân tích phổ tiêu chuẩn "
        "thường chỉ cho độ phân giải 0,1 nm. Ở 1300 nm, thay đổi bước sóng nhỏ nhất phát hiện được này tương ứng với "
        "độ phân giải biến dạng 111 µε. Do đó, trong những ứng dụng dự kiến có biến dạng nhỏ hơn 100 µε, cảm biến cách "
        "tử Bragg có thể không thực tế. Dải động của phép đo biến dạng có thể lên tới 15.000 µε."))

    # ------------------------------------------------------------- LPG
    b.append(h2("Cảm biến cách tử chu kỳ dài", "Long-period grating sensor"))
    b.append(p(
        "Phần này thảo luận việc dùng cách tử chu kỳ dài như những thiết bị cảm biến biến dạng. Nguyên lý hoạt động "
        "của các cách tử này, quy trình chế tạo, các thử nghiệm biến dạng sơ bộ, quá trình giải điều chế, và độ nhạy "
        "chéo với nhiệt độ môi trường đều được phân tích."))

    b.append(h3("Nguyên lý hoạt động", "Principle of operation"))
    b.append(p(
        "Cách tử chu kỳ dài ghép mode dẫn cơ bản với các mode dẫn khác nhau đã được trình diễn trước đây [17, 18]. "
        "Những cách tử có chu kỳ dài hơn, liên quan tới việc ghép một mode dẫn với các mode lớp bọc lan truyền thuận, "
        "được Vengsarkar và cộng sự đề xuất gần đây [19, 20]. Như đã nêu, cách tử sợi quang thoả mãn điều kiện phù hợp "
        "pha Bragg giữa mode dẫn với các mode lớp bọc hoặc mode bức xạ, hoặc với một mode dẫn khác. Điều kiện phù hợp "
        "pha phụ thuộc bước sóng này được cho bởi:"))
    b.append(eq("β₀₁ − β = 2π / Λ", "6.125"))
    b.append(p(
        "trong đó Λ là chu kỳ của cách tử, β₀₁ và β lần lượt là hằng số lan truyền của mode dẫn cơ bản và của mode mà "
        "việc ghép xảy ra với nó."))
    b.append(p(
        "Với cách tử Bragg sợi quang thông thường, việc ghép của mode LP₀₁ lan truyền thuận xảy ra với mode LP₀₁ lan "
        "truyền ngược (β = −β₀₁). Vì Δβ trong trường hợp này lớn (Hình 6-107(a)), chu kỳ cách tử nhỏ, điển hình cỡ "
        "1 µm. Cách tử chu kỳ dài không nghiêng, có biến thiên chiết suất song song với trục dài của sợi, ghép mode cơ "
        "bản với các mode lớp bọc rời rạc, đối xứng tròn, lan truyền thuận (β = β<sub>n</sub>), dẫn tới những giá trị "
        "Δβ nhỏ hơn (Hình 6-107(b)) và do đó những chu kỳ vào cỡ hàng trăm micrômét [19]. Các mode lớp bọc suy giảm "
        "nhanh khi lan truyền dọc theo chiều dài sợi do mặt phân cách lớp bọc–lớp phủ tổn hao và do các chỗ uốn của "
        "sợi. Vì Δβ là rời rạc và là hàm của bước sóng, việc ghép vào các mode lớp bọc này có tính chọn lọc cao, dẫn "
        "tới một mất mát phụ thuộc bước sóng. Kết quả là mọi điều biến tính chất dẫn của lõi và lớp bọc đều làm thay "
        "đổi đáp ứng phổ của cách tử chu kỳ dài, và hiện tượng này có thể được khai thác cho mục đích cảm biến. Hơn "
        "nữa, vì các mode lớp bọc tương tác với lớp phủ sợi hoặc mọi vật liệu khác bao quanh lớp bọc, những thay đổi "
        "tính chất của các vật liệu môi trường ấy cũng có thể được phát hiện."))
    b.append(fig(107, F.fig_6_107()))

    b.append(h3("Quy trình chế tạo", "Fabrication procedure"))
    b.append(p(
        "Để chế tạo cách tử chu kỳ dài, sợi germano-silicat nạp hydro (3,4 mol%) được chiếu xạ UV 248 nm từ một laser "
        "excimer KrF, qua một mặt nạ biên độ mạ crôm có hàm truyền chữ nhật tuần hoàn. Hình 6-108 trình bày sơ đồ "
        "dùng để chế tạo cách tử. Laser phát xung ở 20 Hz với độ dài xung 8 ns. Thời gian ghi điển hình với năng lượng "
        "100 mJ·cm⁻² mỗi xung và chiều dài chiếu 2,5 cm thay đổi trong khoảng 6 đến 15 phút tuỳ loại sợi. Bước sóng "
        "ghép λ<sub>P</sub> dịch về phía lớn hơn trong khi chiếu xạ, do sự tăng chiết suất của lõi sợi được cảm ứng "
        "quang và do đó β₀₁ tăng. Sau khi ghi, cách tử được ủ ở 150 °C trong 10 giờ để loại bỏ hydro chưa phản ứng. "
        "Việc ủ ở nhiệt độ cao này khiến λ<sub>P</sub> dịch về phía bước sóng ngắn hơn do sự phân rã của các khuyết "
        "tật do UV tạo ra và do sự khuếch tán hydro phân tử ra khỏi sợi. Hình 6-109 mô tả độ truyền qua điển hình của "
        "một cách tử. Các băng suy hao khác nhau ứng với việc ghép vào những mode lớp bọc rời rạc có bậc khác nhau. "
        "Có thể chế tạo nhiều cách tử cùng lúc bằng cách đặt nhiều hơn một sợi phía sau mặt nạ biên độ. Hơn nữa, yêu "
        "cầu ổn định trong quá trình ghi không khắt khe như với cách tử Bragg chu kỳ ngắn."))
    b.append(fig(108, F.fig_6_108()))
    b.append(fig(109, F.fig_6_109()))
    b.append(p(
        "Với việc ghép vào mode lớp bọc bậc cao nhất, độ cách ly tối đa (mất mát cường độ truyền qua) điển hình nằm "
        "trong khoảng 5 đến 20 dB, tuỳ tham số sợi, thời gian chiếu UV và chu kỳ mặt nạ. Bước sóng ghép cơ bản mong "
        "muốn có thể thay đổi dễ dàng nhờ những mặt nạ biên độ rẻ tiền có chu kỳ khác nhau. Mất mát chèn, tán sắc mode "
        "phân cực, phản xạ ngược và mất mát phụ thuộc phân cực của một cách tử điển hình lần lượt là 0,2 dB; 0,01 ps; "
        "−80 dB và 0,02 dB. Độ nhạy phân cực và phản xạ ngược không đáng kể của những thiết bị này loại bỏ nhu cầu về "
        "các bộ phân cực và bộ cách ly đắt tiền."))
    b.append(p(
        "Các thí nghiệm sơ bộ đã được thực hiện để khảo sát độ nhạy biến dạng của cách tử chu kỳ dài ghi trên các loại "
        "sợi khác nhau [21, 22]. Cách tử được chế tạo trên bốn loại sợi: sợi dịch tán sắc tiêu chuẩn (DSF), sợi "
        "1550 nm tiêu chuẩn, và sợi đơn mode 980 và 1050 nm thông thường; để ngắn gọn chúng được gọi lần lượt là sợi "
        "A, B, C và D. Độ nhạy biến dạng của cách tử ghi trên các loại sợi khác nhau được xác định bằng cách kéo biến "
        "dạng dọc trục cách tử giữa hai bàn dịch chuyển đặt cách xa nhau theo chiều dọc. Độ dịch của bước sóng mất mát "
        "đỉnh của cách tử trên sợi D theo biến dạng áp đặt được trình bày trên Hình 6-110, cùng với độ dịch của một "
        "cách tử Bragg (khoảng 9 nm trên mỗi % biến dạng, ở 1300 nm) [9]. Hệ số dịch bước sóng theo biến dạng (β) của "
        "các sợi A, B, C và D được cho trong Bảng 6.28. Sợi D có hệ số 15,2 nm/%ε, khiến độ dịch do biến dạng của nó "
        "lớn hơn 50% so với cách tử Bragg thông thường. Độ phân giải biến dạng của sợi này, với độ dịch bước sóng phát "
        "hiện được 0,1 nm, là 65,75 µε."))
    b.append(fig(110, F.fig_6_110()))
    b.append(table(
        ["Loại sợi", "Độ nhạy biến dạng (nm %ε⁻¹)"],
        [["A — Sợi dịch tán sắc tiêu chuẩn (DSF)", "−7,27"],
         ["B — Sợi thông tin 1550 nm tiêu chuẩn", "4,73"],
         ["C — Sợi đơn mode 980 nm thông thường", "4,29"],
         ["D — Sợi đơn mode 1060 nm thông thường", "15,21"]],
        "Bảng 6.28 · Độ nhạy biến dạng của cách tử chu kỳ dài ghi trên bốn loại sợi khác nhau. Các giá trị ứng với độ "
        "dịch của bước sóng cộng hưởng bậc cao nhất."))
    b.append(p(
        "Sơ đồ giải điều chế của một cảm biến quyết định mức độ đơn giản và độ nhạy tổng thể của hệ cảm biến. Cảm biến "
        "cách tử Bragg chu kỳ ngắn được cho thấy đòi hỏi những kỹ thuật xử lý tín hiệu phức tạp và đắt tiền khi triển "
        "khai. Với cách tử chu kỳ dài, có thể dùng một phương pháp giải điều chế đơn giản để trích thông tin. Băng "
        "thông rộng của các băng cộng hưởng cho phép chuyển độ dịch bước sóng do nhiễu động bên ngoài thành một biến "
        "thiên cường độ dễ phát hiện. Hình 6-111 trình bày độ dịch do biến dạng gây ra trong một cách tử ghi trên sợi "
        "C. Mức tăng mất mát tại 1317 nm khoảng 1,6 dB. Một laser diode phát tại 1317 nm được dùng làm nguồn quang, và "
        "sự thay đổi cường độ truyền qua được theo dõi theo biến dạng áp đặt. Cường độ truyền qua được vẽ trên Hình "
        "6-112 cho ba lần thử khác nhau. Độ lặp lại của thí nghiệm chứng minh tính khả thi của việc dùng sơ đồ đơn "
        "giản này để khai thác độ nhạy cao của cách tử chu kỳ dài. Truyền qua của một laser diode đặt trên sườn phổ "
        "của cách tử, về một trong hai phía của bước sóng cộng hưởng, có thể dùng làm thước đo nhiễu động áp đặt. Một "
        "tổ hợp đầu dò và bộ khuếch đại đơn giản ở đầu ra có thể dùng để xác định mức truyền qua đầu dò. Mặt khác, "
        "cũng có thể dùng một nguồn băng rộng để hỏi cách tử. Ở đầu ra, một bộ lọc thông dải quang có thể được dùng để "
        "chỉ cho một băng thông cố định của tín hiệu đi tới đầu dò; bộ lọc thông dải này cũng phải đặt trên một trong "
        "hai phía của băng mất mát đỉnh của băng cộng hưởng. Những sơ đồ này dễ triển khai, và khác với cách tử Bragg "
        "thông thường, không cần tới những sơ đồ giải điều chế giao thoa phức tạp và đắt tiền [22]."))
    b.append(fig(111, F.fig_6_111()))
    b.append(fig(112, F.fig_6_112()))

    b.append(h3("Độ nhạy nhiệt của cách tử chu kỳ dài", "Temperature sensitivity"))
    b.append(p(
        "Cách tử ghi trên các loại sợi khác nhau cũng được thử độ nhạy chéo với nhiệt độ [22]. Hệ số dịch bước sóng "
        "theo nhiệt độ của các loại sợi khác nhau được cho trong Bảng 6.29. Độ nhạy nhiệt của một cách tử Bragg sợi "
        "quang là 0,014 nm °C⁻¹. Như vậy, độ nhạy nhiệt của một cách tử chu kỳ dài điển hình cao hơn một bậc độ lớn "
        "so với cách tử Bragg. Độ nhạy chéo lớn với nhiệt độ môi trường này có thể làm suy giảm hiệu năng cảm biến "
        "biến dạng của hệ, trừ khi tín hiệu đầu ra được bù thoả đáng. Cảm biến đa tham số dùng cách tử chu kỳ dài đã "
        "được đề xuất để có được những phép đo biến dạng chính xác trong môi trường có dao động nhiệt độ [21]."))
    b.append(table(
        ["Loại sợi", "Độ nhạy nhiệt (nm °C⁻¹)"],
        [["A — Sợi dịch tán sắc tiêu chuẩn (DSF)", "0,062"],
         ["B — Sợi thông tin 1550 nm tiêu chuẩn", "0,058"],
         ["C — Sợi đơn mode 980 nm thông thường", "0,154"],
         ["D — Sợi đơn mode 1060 nm thông thường", "0,111"]],
        "Bảng 6.29 · Độ nhạy nhiệt của cách tử chu kỳ dài ghi trên bốn loại sợi khác nhau. Các giá trị ứng với độ "
        "dịch của bước sóng cộng hưởng bậc cao nhất."))
    b.append(p(
        "Tóm lại, cảm biến cách tử chu kỳ dài rất linh hoạt. Những cảm biến này có thể dễ dàng được dùng cùng với các "
        "kỹ thuật phát hiện đơn giản và rẻ tiền. Kết quả thực nghiệm chứng minh rằng có thể dùng các phương pháp này "
        "một cách hiệu quả mà không phải hy sinh độ phân giải cao của cảm biến. Cảm biến cách tử chu kỳ dài không nhạy "
        "với phân cực đầu vào và không cần nguồn quang kết hợp. Độ nhạy chéo với nhiệt độ là mối quan ngại chính khi "
        "dùng các cách tử này để đo biến dạng."))

    b.append(h2("So sánh các sơ đồ cảm biến", "Comparison of sensing schemes"))
    b.append(p(
        "Dựa trên các kết quả trên, cảm biến giao thoa có độ nhạy và băng thông cao nhưng bị hạn chế bởi tính phi "
        "tuyến của tín hiệu đầu ra. Ngược lại, cảm biến nội dễ bị ảnh hưởng bởi thay đổi nhiệt độ môi trường, trong "
        "khi cảm biến dựa trên cách tử lại dễ ghép kênh hơn. Mỗi loại có thể được dùng trong những ứng dụng cụ thể."))

    b.append(h2("Kết luận", "Conclusion"))
    b.append(p(
        "Chúng tôi đã khảo sát hiệu năng của bốn loại cảm biến giao thoa và dựa trên cách tử khác nhau. Phân tích này "
        "dựa trên việc chế tạo và chi phí đầu đo, xử lý tín hiệu, độ nhạy chéo với nhiệt độ, độ phân giải và dải làm "
        "việc. Những ưu nhược điểm tương đối của các sơ đồ cảm biến khác nhau cũng đã được thảo luận."))
    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. Sirkis, Phase-strain-temperature model for structurally embedded interferometric optical fiber strain "
        "sensors with applications, <i>Fiber Optic Smart Structures and Skins IV</i>, SPIE, Vol. 1588, 1991.",
        "R. O. Claus, M. F. Gunther, A. Wang, and K. A. Murphy, Extrinsic Fabry–Perot sensor for strain and crack "
        "opening displacement measurements from −200 to 900 °C, <i>J. Smart Materials and Structures</i>, 1, "
        "237–242, 1992.",
        "K. A. Murphy, M. F. Gunther, A. M. Vengsarkar, and R. O. Claus, Fabry–Perot fiber optic sensors in "
        "full-scale fatigue testing on an F-15 aircraft, <i>Appl. Optics</i>, 31, 431–433, 1991.",
        "V. Bhatia, C. A. Schmid, K. A. Murphy, R. O. Claus, T. A. Tran, J. A. Greene, and M. S. Miller, Optical "
        "fiber sensing technique for edge-induced and internal delamination detection in composites, <i>J. Smart "
        "Materials Structures</i>, 4, 164–169, 1995.",
        "V. Bhatia, M. J. de Vries, K. A. Murphy, R. O. Claus, T. A. Tran, and J. A. Greene, Extrinsic Fabry–Perot "
        "interferometers for absolute measurements, <i>Fiberoptic Product News</i>, 9(Dec.), 12–13, 1994.",
        "V. Bhatia, M. B. Sen, K. A. Murphy, and R. O. Claus, Wavelength-tracked white light interferometry for "
        "highly sensitive strain and temperature measurements, <i>Electron. Lett.</i>, 32, 247–249, 1996.",
        "C. E. Lee and H. F. Taylor, Fiber-optic Fabry–Perot temperature sensor using a low-coherence light source, "
        "<i>J. Lightwave Technol.</i>, 9, 129–134, 1991.",
        "J. A. Greene, T. A. Tran, K. A. Murphy, A. J. Plante, V. Bhatia, M. B. Sen, and R. O. Claus, Photoinduced "
        "Fresnel reflectors for point-wise and distributed sensing applications, <i>Proc. Conf. Smart Structures "
        "and Materials</i>, SPIE’95, paper 2444-05, February 1995.",
        "K. O. Hill, Y. Fuijii, D. C. Johnson, and B. S. Kawasaki, Photosensitivity in optical fiber waveguides: "
        "applications to reflection filter fabrication, <i>Appl. Phys. Lett.</i>, 32, 647, 1978.",
        "G. Meltz, W. W. Morey, and W. H. Glenn, Formation of Bragg gratings in optical fibers by transverse "
        "holographic method, <i>Optics Lett.</i>, 14, 823, 1989.",
        "P. J. Lemaire, A. M. Vengsarkar, W. A. Reed, V. Mizrahi, and K. S. Kranz, Refractive index changes in "
        "optical fibers sensitized with molecular hydrogen, in <i>Proc. Conf. Optical Fiber Communications</i>, "
        "OFC’94, Technical Digest, paper TuL1, 47, 1994.",
        "R. Kashyap, Photosensitive optical fibers: devices and applications, <i>Optical Fiber Technol.</i>, 1, "
        "17–34, 1994.",
        "D. Z. Anderson, V. Mizrahi, T. Ergodan, and A. E. White, Phase-mask method for volume manufacturing of "
        "fiber phase gratings, in <i>Proc. Conf. Optical Fiber Communication</i>, post-deadline paper PD16, 1993, "
        "p. 68.",
        "A. D. Kersey and T. A. Berkoff, Fiber-optic Bragg-grating differential-temperature sensor, <i>IEEE "
        "Photonics Technol. Lett.</i>, 4, 1183–1185, 1992.",
        "V. Bhatia, M. B. Sen, K. A. Murphy, A. Wang, R. O. Claus, M. E. Jones, J. L. Grace, and J. A. Greene, "
        "Demodulation of wavelength-encoded optical fiber sensor signals using fiber modal interferometers, "
        "<i>SPIE Photonics East</i>, Philadelphia, PA, paper 2594-09, October 1995.",
        "M. G. Xu, L. Dong, L. Reekie, J. A. Tucknott, and J. L. Cruz, Chirped fiber gratings for "
        "temperature-independent strain sensing, in <i>Proc. First OSA Topical Meet. Photosensitivity and "
        "Quadratic Nonlinearity in Glass Waveguides</i>, paper PMB2, 1995.",
        "K. O. Hill, B. Malo, K. Vineberg, F. Bilodeau, D. Johnson, and I. Skinner, Efficient mode-conversion in "
        "telecommunication fiber using externally written gratings, <i>Electron. Lett.</i>, 26, 1270–1272, 1990.",
        "F. Bilodeau, K. O. Hill, B. Malo, D. Johnson, and I. Skinner, Efficient narrowband LP01 ↔ LP02 mode "
        "convertors fabricated in photosensitive fiber: spectral response, <i>Electron. Lett.</i>, 27, 682–684, "
        "1991.",
        "A. M. Vengsarkar, P. J. Lemaire, J. B. Judkins, V. Bhatia, J. E. Sipe, and T. E. Ergodan, Long-period "
        "fiber gratings as band-rejection filters, <i>Proc. Conf. Optical Fiber Communications</i>, OFC ’95, "
        "post-deadline paper, PD4-2, 1995.",
        "A. M. Vengsarkar, P. J. Lemaire, J. B. Judkins, V. Bhatia, J. E. Sipe, and T. E. Ergodan, Long-period "
        "fiber gratings as band-rejection filters, <i>J. Lightwave Technol.</i>, 14, 58–65, 1996.",
        "V. Bhatia, M. B. Burford, K. A. Murphy, and A. M. Vengsarkar, Long-period fiber grating sensors, "
        "<i>Proc. Conf. Optical Fiber Communication</i>, paper ThP1, February 1996.",
        "V. Bhatia and A. M. Vengsarkar, Optical fiber long-period grating sensors, <i>Optics Lett.</i>, 21, "
        "692–694, 1996.",
        "C. D. Butter and G. B. Hocker, Fiber optics strain gage, <i>Appl. Optics</i>, 17, 2867–2869, 1978.",
        "J. S. Sirkis and H. W. Haslach, Interferometric strain measurement by arbitrarily configured, surface "
        "mounted, optical fiber, <i>J. Lightwave Technol.</i>, 8, 1497–1503, 1990.",
    ]))
    b.append(quote(
        "Một cảm biến sợi quang tốt không phải là cảm biến có đầu ra đẹp nhất, mà là cảm biến mà phía thu có thể "
        "giải mã bằng những linh kiện sẵn có trên thị trường.",
        "Richard O. Claus, Vikram Bhatia &amp; Anbo Wang"))
    b.append(nav(11, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Four sensors are compared here, and they divide cleanly into two families. The Fabry–Perot pair modulates "
        "intensity; the grating pair encodes wavelength. Everything else in the section follows from that split — "
        "the demodulation cost, the cross-sensitivity, and the reason the authors end up recommending different "
        "sensors for different jobs rather than one winner."))
    b.append(p(
        "The comparison is also a good example of how to read a sensor paper. The criteria are stated up front — "
        "strain resolution, dynamic range, cross-sensitivity, fabrication simplicity, demodulation complexity — and "
        "each sensor is then judged against all five. Very few of the numbers are surprising in isolation; what is "
        "useful is seeing them side by side."))

    b.append(h2("Extrinsic versus intrinsic", "Ngoại so với nội"))
    b.append(p(
        "The EFPI puts its cavity in the air gap between two fibre ends. That single design decision buys three "
        "things at once: the cavity is not strained when the fibre is strained transversely, so the Poisson effect "
        "does not reach the measurement; the temperature coefficient is small because the cavity is mostly air; and "
        "the sensor can be built single-ended, which matters when you can only reach one side of a structure."))
    b.append(p(
        "The IFPI puts its cavity inside the glass. Now the light travels through material that changes its "
        "refractive index when it is strained — the photoelastic effect — and that index change, not the length "
        "change, dominates the output. The consequence is that an IFPI responds to every strain component and to "
        "temperature, which is exactly what an embedded sensor must not do. It is a textbook case of a device that "
        "is elegant in principle and awkward in a real structure."))
    b.append(p(
        "Equation 6.117 is worth pausing on. I = I₀cos²(4πd/λ) has a period of λ/2 in d, which is why the text can "
        "say that one fringe equals half a wavelength. And because the cosine is symmetric, the same intensity "
        "occurs on both slopes — which is why the sensor is operated on one slope only, around the Q-point, where "
        "the response is linear and the sign of the change is unambiguous."))

    b.append(h2("Why wavelength encoding wins", "Vì sao mã hoá bước sóng thắng"))
    b.append(p(
        "An intensity sensor carries its information in a quantity that everything else also changes: connector "
        "loss, bend loss, source ageing, detector drift. A grating carries its information in wavelength, and "
        "wavelength is the one property of light that survives a long fibre link intact. That is the whole argument "
        "for fibre Bragg gratings, and it is why they became the default sensing element in structural monitoring "
        "despite being difficult to make."))
    b.append(p(
        "The price is in the interrogation. A Bragg grating has a bandwidth of 0.1 to 1 nm and shifts by about "
        "11 nm per per cent strain at 1550 nm, so you need a spectrometer or an interferometric scheme to read it. "
        "Equation 6.122, λ_B = 2Λn_eff, tells you why both strain and temperature work: they change Λ and they "
        "change n_eff, and the sensor cannot tell which did what. Hence the reference grating, and hence the "
        "temperature-compensated packages that dominate the product literature."))
    b.append(p(
        "The 111 µε figure at 1300 nm is the number that decides applications. With a 0.1 nm spectrum analyser, a "
        "Bragg grating simply cannot resolve strains below about a hundred microstrain — not because the grating is "
        "bad, but because the readout is. This is a recurring theme in the chapter: the transducer is often better "
        "than the instrument attached to it."))

    b.append(h2("The long-period alternative", "Giải pháp chu kỳ dài"))
    b.append(p(
        "A long-period grating couples the core mode to cladding modes travelling in the same direction. Because "
        "Δβ is small, the period is large — hundreds of micrometres — and the resonance bands are broad. Broad bands "
        "are usually a defect in a filter and a gift in a sensor: a broad slope means you can put a fixed-wavelength "
        "laser on the side of the band and read the shift as an intensity change, with nothing more than a "
        "photodiode."))
    b.append(p(
        "That is the trade the section is really describing. You give up the sharp, easily multiplexed Bragg peak "
        "and you get a demodulator that costs a few dollars. Table 6.28 shows why the trade can pay: fibre D shifts "
        "by 15.2 nm per per cent strain, half again as much as a Bragg grating, and the sign of the coefficient even "
        "differs between fibres — negative for the dispersion-shifted fibre, positive for the rest."))
    b.append(p(
        "The catch is temperature. Table 6.29 gives 0.062 to 0.154 nm/°C against 0.014 nm/°C for a Bragg grating — "
        "an order of magnitude worse. A long-period grating is therefore a strain sensor that also measures "
        "temperature very well and cannot distinguish the two, which is why multiparameter schemes appear in the "
        "literature almost as soon as the gratings themselves."))

    b.append(h2("What the comparison actually says", "Điều phần so sánh thực sự nói"))
    b.append(p(
        "The closing comparison is deliberately unheroic: interferometric sensors are sensitive and fast but "
        "nonlinear; intrinsic sensors drift with temperature; gratings multiplex easily. Each may be used in "
        "specific applications. That is the honest conclusion, and it is more useful than a ranking, because the "
        "choice between them is usually made by the structure being monitored rather than by the sensor."))
    b.append(nav(11, "en"))
    return "".join(b)
