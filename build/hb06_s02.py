# -*- coding: utf-8 -*-
"""Handbook 6.2 — Inductive Displacement Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Cảm biến cảm ứng được dùng rộng rãi trong công nghiệp với rất nhiều ứng dụng khác nhau. Chúng chắc "
        "chắn, gọn, và ít chịu ảnh hưởng của các yếu tố môi trường (độ ẩm, bụi) so với cảm biến điện dung. Cảm "
        "biến cảm ứng chủ yếu dựa trên nguyên lý mạch từ. Có thể chia chúng thành loại tự sinh và loại thụ động. "
        "Loại tự sinh dùng nguyên lý máy phát điện: khi có chuyển động tương đối giữa vật dẫn và từ trường, một "
        "điện áp được cảm ứng trong vật dẫn; hoặc một từ trường biến thiên móc vòng một vật dẫn đứng yên cũng "
        "sinh ra điện áp trong vật dẫn ấy. Trong ứng dụng đo lường, từ trường có thể biến thiên với một tần số "
        "nào đó và vật dẫn cũng có thể đồng thời chuyển động. Ở cảm biến cảm ứng, chuyển động tương đối giữa "
        "từ trường và vật dẫn do sự thay đổi của đại lượng cần đo tạo ra, thường thông qua một chuyển động cơ "
        "nào đó. Ngược lại, đầu đo thụ động cần một nguồn năng lượng bên ngoài; khi ấy tác dụng của đầu đo chỉ "
        "là điều biến tín hiệu kích thích."))
    b.append(p(
        "Để giải thích nguyên lý cơ bản của cảm biến cảm ứng, Hình 6-7 trình bày một mạch từ đơn giản. Mạch từ "
        "gồm một lõi chế từ vật liệu sắt từ, trên đó quấn một cuộn dây n vòng. Cuộn dây đóng vai trò nguồn sức "
        "từ động (mmf) đẩy từ thông Φ qua mạch từ. Nếu giả thiết khe hở không khí bằng không, phương trình của "
        "mạch từ có thể viết:"))
    b.append(eq("mmf = Φ × ℜ &nbsp; (A·vòng)", "6.2"))
    b.append(p(
        "nghĩa là từ trở ℜ hạn chế từ thông trong mạch từ đúng như điện trở hạn chế dòng điện trong mạch điện. "
        "Viết sức từ động theo dòng điện, từ thông có thể biểu diễn là:"))
    b.append(eq("Φ = n·i / ℜ &nbsp; (weber)", "6.3"))
    b.append(p(
        "Trên Hình 6-7, từ thông móc vòng một vòng dây được tính theo công thức 6.3; nhưng tổng từ thông móc "
        "vòng toàn bộ n vòng của cuộn dây là:"))
    b.append(eq("Ψ = n·Φ = n²·i / ℜ &nbsp; (weber)", "6.4"))
    b.append(p(
        "Từ công thức 6.4 suy ra điện cảm tự cảm L của cuộn dây, được định nghĩa là tổng từ thông (Ψ weber) "
        "trên một đơn vị dòng điện của cuộn dây ấy, tức là:"))
    b.append(eq("L = Ψ / i = n² / ℜ", "6.5"))
    b.append(p("Điều này cho thấy có thể tính điện cảm tự cảm của một phần tử cảm ứng từ các tính chất của "
               "mạch từ. Biểu diễn ℜ theo các kích thước hình học:"))
    b.append(eq("ℜ = l / (μ·μ<sub>0</sub>·A)", "6.6"))
    b.append(p(
        "trong đó l là tổng chiều dài đường từ thông; μ là độ từ thẩm tương đối của vật liệu mạch từ; μ<sub>0</sub> "
        "là độ từ thẩm của chân không (4π×10<sup>−7</sup> H/m); A là tiết diện của đường từ thông."))
    b.append(p(
        "Cấu hình trên Hình 6-7 trở thành một cảm biến cảm ứng cơ bản nếu cho phép khe hở không khí thay đổi. "
        "Khi đó lõi sắt từ được tách thành hai phần bởi khe hở. Tổng từ trở của mạch bây giờ là tổng từ trở "
        "của lõi và từ trở của khe hở. Độ từ thẩm tương đối của không khí xấp xỉ bằng một, còn của vật liệu sắt "
        "từ vào cỡ vài nghìn, cho thấy sự có mặt của khe hở làm từ trở của mạch tăng mạnh và từ thông giảm "
        "tương ứng. Vì vậy một thay đổi nhỏ của khe hở gây ra một thay đổi đo được của điện cảm. Phần lớn các "
        "đầu đo cảm ứng đều dựa trên những nguyên lý này và được trình bày chi tiết dưới đây."))
    b.append(fig(7, F.fig_6_7()))

    b.append(h2("Đầu đo từ trở biến thiên kiểu thẳng và kiểu quay",
                "Linear and Rotary Variable-Reluctance Transducer"))
    b.append(p(
        "Các đầu đo từ trở biến thiên dựa trên sự thay đổi từ trở của một đường từ thông. Loại đầu đo này đặc "
        "biệt thích hợp cho đo gia tốc, tuy vậy cũng có thể chế tạo để đo dịch chuyển và vận tốc. Chúng có nhiều "
        "dạng khác nhau, mô tả dưới đây."))

    b.append(h3("Cảm biến từ trở biến thiên một cuộn dây kiểu thẳng",
                "The Single-Coil Linear Variable-Reluctance Sensor"))
    b.append(p(
        "Một cảm biến dịch chuyển từ trở biến thiên một cuộn dây điển hình được minh hoạ trên Hình 6-8, gồm ba "
        "phần tử: lõi sắt từ hình vành bán nguyệt, khe hở không khí biến thiên, và một tấm sắt từ. Tổng từ trở "
        "của mạch từ là tổng các từ trở riêng phần:"))
    b.append(eq("ℜ<sub>T</sub> = ℜ<sub>C</sub> + ℜ<sub>G</sub> + ℜ<sub>A</sub>", "6.7"))
    b.append(p(
        "với ℜ<sub>C</sub>, ℜ<sub>G</sub>, ℜ<sub>A</sub> lần lượt là từ trở của lõi, của khe hở không khí và của "
        "phần ứng. Mỗi từ trở này xác định được từ tính chất vật liệu theo công thức 6.6. Trong trường hợp cụ "
        "thể này, từ trở ℜ<sub>T</sub> có thể xấp xỉ:"))
    b.append(eq("ℜ<sub>T</sub> = R/(μ<sub>0</sub>μ<sub>C</sub>r²) + 2d/(μ<sub>0</sub>πr²) + R/(μ<sub>0</sub>"
                "μ<sub>A</sub>rt)", "6.8"))
    b.append(p(
        "Khi lập công thức 6.8, chiều dài đường từ thông trong lõi được lấy là πR, tiết diện được giả thiết đều "
        "và bằng πr². Tổng chiều dài đường từ thông trong không khí là 2d, và giả thiết không có hiệu ứng rìa "
        "hay uốn cong của từ thông qua khe hở, nên tiết diện đường từ thông trong không khí xấp xỉ tiết diện "
        "của lõi. Chiều dài đường từ thông trung tâm trong phần ứng là 2R; việc tính tiết diện thích hợp của "
        "phần ứng là khó, nhưng có thể xấp xỉ bằng 2rt với t là chiều dày phần ứng."))
    b.append(fig(8, F.fig_6_8()))
    b.append(p(
        "Trong công thức 6.8, mọi tham số đều cố định trừ một biến độc lập là khe hở không khí. Vì vậy có thể "
        "rút gọn thành:"))
    b.append(eq("ℜ<sub>T</sub> = ℜ<sub>0</sub> + k·d", "6.9"))
    b.append(p(
        "với ℜ<sub>0</sub> = R/μ<sub>0</sub>r·[1/(μ<sub>C</sub>r) + 1/(μ<sub>A</sub>t)] và k = 2/(μ<sub>0</sub>πr²). "
        "Dùng công thức 6.5 và 6.9, điện cảm viết được là:"))
    b.append(eq("L = n²/(ℜ<sub>0</sub> + kd) = L<sub>0</sub>/(1 + α·d)", "6.10"))
    b.append(p(
        "với L<sub>0</sub> là điện cảm khi khe hở bằng không và α = k/ℜ<sub>0</sub>. Các giá trị L<sub>0</sub> và "
        "α xác định được bằng tính toán: chúng phụ thuộc hình học lõi, độ từ thẩm… như đã giải thích ở trên. "
        "Từ công thức 6.10 thấy rõ quan hệ giữa L và α là phi tuyến. Bất chấp tính phi tuyến ấy, loại cảm biến "
        "một cuộn dây này vẫn có chỗ dùng, chẳng hạn trong đo lực và trong đo lường từ xa. Trong đo lực, mức "
        "thay đổi điện cảm có thể được làm thành thước đo độ lớn của lực tác dụng: cuộn dây thường là một phần "
        "tử của bộ dao động LC, nên tần số ra biến thiên theo lực tác dụng — cuộn dây điều biến tần số của bộ "
        "dao động địa phương."))

    b.append(h3("Cảm biến từ trở vi sai biến thiên", "The Variable-Differential Reluctance Sensor"))
    b.append(p(
        "Vấn đề phi tuyến có thể khắc phục bằng cách sửa hệ một cuộn dây thành cảm biến từ trở vi sai biến thiên "
        "(còn gọi là cảm biến đẩy – kéo), như trên Hình 6-9. Cảm biến này gồm một phần ứng chuyển động giữa hai "
        "lõi giống nhau, cách nhau một khoảng cố định 2d. Khi đó công thức 6.10 viết được cho cả hai cuộn:"))
    b.append(eq("L<sub>1</sub> = L<sub>0</sub>[1 + α(d − x)]<sup>−1</sup>, &nbsp; "
                "L<sub>2</sub> = L<sub>0</sub>[1 + α(d + x)]<sup>−1</sup>", "6.11"))
    b.append(p(
        "Tuy quan hệ giữa L<sub>1</sub> và L<sub>2</sub> vẫn phi tuyến, cảm biến có thể được đưa vào một cầu xoay "
        "chiều để cho đầu ra tuyến tính với những chuyển động nhỏ. Sai số trễ của loại đầu đo này hầu như chỉ "
        "giới hạn ở các chi tiết cơ khí. Chúng đáp ứng được cả phép đo tĩnh và động, có độ phân giải liên tục và "
        "đầu ra lớn, nhưng có thể làm việc thất thường dưới tác dụng của từ trường ngoài. Một cảm biến điển hình "
        "loại này có dải đầu vào 1 cm, điện cảm cuộn 25 mH và điện trở cuộn 75 Ω; điện trở cuộn phải được xét "
        "cẩn thận khi thiết kế mạch dao động. Độ phi tuyến cực đại là 0,5 %."))
    b.append(fig(9, F.fig_6_9()))
    b.append(p(
        "Một cảm biến vi sai thương mại điển hình được trình bày trên Hình 6-10. Lõi sắt nằm giữa hai khung chữ "
        "E. Từ thông do các cuộn sơ cấp sinh ra phụ thuộc từ trở của đường từ, mà từ trở chính là khe hở không "
        "khí. Mọi chuyển động của lõi làm tăng khe hở phía này và giảm khe hở phía kia, khiến từ trở thay đổi "
        "theo nguyên lý đã trình bày và do đó cảm ứng điện áp lớn hơn ở một trong hai cuộn. Chuyển động theo "
        "chiều ngược lại đảo tác dụng, với độ lệch pha 180° xuất hiện tại điểm không. Điện áp ra có thể được sửa "
        "đổi tuỳ yêu cầu xử lý tín hiệu, bằng chỉnh lưu, tách sóng hay lọc. Ở những thiết bị này, hành trình "
        "toàn thang có thể cực nhỏ — vào cỡ vài phần nghìn centimét."))
    b.append(fig(10, F.fig_6_10()))
    b.append(p(
        "Nói chung đầu đo từ trở biến thiên có dải đo nhỏ và được dùng trong những ứng dụng chuyên biệt như đầu "
        "đo áp suất. Lực từ tác dụng lên phần ứng khá lớn và điều này hạn chế nghiêm trọng phạm vi ứng dụng. "
        "Tuy vậy, phần ứng có thể được chế tạo thành màng, nhờ đó thích hợp cho đo áp suất."))

    b.append(h3("Máy phát tốc độ từ trở biến thiên", "Variable-Reluctance Tachogenerators"))
    b.append(p(
        "Một ví dụ khác của cảm biến từ trở biến thiên được trình bày trên Hình 6-11. Những cảm biến này dựa "
        "trên định luật cảm ứng điện từ Faraday, nên cũng có thể gọi là cảm biến điện từ. Về cơ bản, sức điện "
        "động cảm ứng trong cảm biến phụ thuộc vận tốc thẳng hoặc vận tốc góc của chuyển động."))
    b.append(p(
        "Máy phát tốc độ từ trở biến thiên gồm một bánh răng sắt từ gắn trên trục quay, và một cuộn dây quấn "
        "trên nam châm vĩnh cửu, được nối dài bằng một cực từ sắt non. Bánh răng quay rất sát cực từ, làm từ "
        "thông móc vòng cuộn dây thay đổi và cảm ứng một sức điện động trong cuộn. Từ trở của mạch phụ thuộc bề "
        "rộng khe hở giữa bánh răng quay và cực từ: khi răng ở gần cực từ, từ trở cực tiểu và tăng lên khi răng "
        "đi xa. Khi bánh răng quay với vận tốc ω, từ thông có thể biểu diễn:"))
    b.append(eq("Ψ(θ) = A + B·cos(m·θ)", "6.12"))
    b.append(p("với A là từ thông trung bình, B là biên độ biến thiên từ thông và m là số răng. Sức điện động "
               "cảm ứng là:"))
    b.append(eq("E = −dΨ/dt = −(dΨ/dθ)(dθ/dt)", "6.13"))
    b.append(p("hay"))
    b.append(eq("E = B·m·ω·sin(m·ω·t)", "6.14"))
    b.append(fig(11, F.fig_6_11()))
    b.append(p(
        "Cả biên độ và tần số của điện áp sinh ra trên cuộn dây đều tỉ lệ với vận tốc góc của bánh răng. Về "
        "nguyên tắc, có thể tìm vận tốc góc ω từ biên độ hoặc từ tần số của tín hiệu. Trong thực tế, biên độ đo "
        "được có thể chịu ảnh hưởng của hiệu ứng tải và nhiễu điện. Khi xử lý tín hiệu, tần số là lựa chọn ưu "
        "tiên vì dễ dàng chuyển thành tín hiệu số."))
    b.append(p(
        "Máy phát tốc độ từ trở biến thiên thích hợp nhất cho đo vận tốc góc. Chúng cũng được dùng trong đo lưu "
        "lượng thể tích và xác định tổng thể tích dòng chảy của chất lỏng."))

    b.append(h3("Microsyn", "Microsyn"))
    b.append(p(
        "Một ví dụ khác thường gặp của đầu đo từ trở biến thiên là microsyn, như trên Hình 6-12. Trong cách bố "
        "trí này, các cuộn dây được đấu sao cho tại vị trí không của phần tử quay, điện áp cảm ứng ở cuộn 1 và 3 "
        "cân bằng với điện áp cảm ứng ở cuộn 2 và 4. Rôto quay theo chiều kim đồng hồ làm tăng từ trở của cuộn "
        "1 và 3, đồng thời giảm từ trở của cuộn 2 và 4, cho một điện áp ra tổng e<sub>o</sub>. Chuyển động ngược "
        "chiều kim đồng hồ gây tác dụng tương tự ở cuộn 2 và 4 với độ lệch pha 180°. Có thể thu được đầu ra "
        "phân biệt chiều bằng các bộ tách sóng nhạy pha, như trình bày ở mục LVDT của chương này."))
    b.append(fig(12, F.fig_6_12()))
    b.append(p(
        "Đầu đo microsyn được dùng nhiều trong các ứng dụng liên quan đến con quay hồi chuyển. Nhờ microsyn, có "
        "thể phát hiện những chuyển động rất nhỏ, cho tín hiệu ra chỉ ứng với 0,01° thay đổi góc. Độ nhạy của "
        "thiết bị có thể lên tới 5 V cho mỗi độ quay. Độ phi tuyến có thể từ 0,5 % đến 1,0 % toàn thang. Ưu điểm "
        "chính của loại đầu đo này là rôto không có dây quấn và không có vành trượt; mô men phản kháng từ cũng "
        "không đáng kể."))

    b.append(h3("Synchro", "Synchros"))
    b.append(p(
        "Thuật ngữ synchro gắn với một họ thiết bị cơ điện có thể bàn đến dưới nhiều góc khác nhau. Chúng chủ "
        "yếu dùng trong đo góc và thường xuất hiện trong kỹ thuật điều khiển như một bộ phận của hệ servo, máy "
        "công cụ, anten…"))
    b.append(p(
        "Cấu tạo của synchro tương tự động cơ cảm ứng rôto dây quấn, như trên Hình 6-13. Rôto quay làm thay đổi "
        "hỗ cảm giữa cuộn rôto và ba cuộn stato. Ba tín hiệu điện áp từ các cuộn này xác định vị trí góc của "
        "rôto."))
    b.append(fig(13, F.fig_6_13()))
    b.append(p(
        "Synchro được dùng cùng nhiều thiết bị khác, gồm biến áp điều khiển, biến áp Scott T, resolver, bộ tách "
        "sóng nhạy pha, bộ chuyển đổi tương tự – số…"))
    b.append(p(
        "Trong một số trường hợp, một biến áp điều khiển được nối vào đầu ra các cuộn stato sao cho đầu ra của "
        "biến áp tạo ra một sức từ động tổng hợp thẳng hàng với hướng của rôto synchro. Nói cách khác, rôto "
        "synchro đóng vai trò một cuộn dò để phát hiện hướng của trường stato trong biến áp điều khiển; khi trục "
        "của cuộn này thẳng hàng với trường, điện áp lớn nhất được cấp cho biến áp."))
    b.append(p(
        "Trong những trường hợp khác, tín hiệu xoay chiều từ synchro trước hết được đưa vào một biến áp Scott T, "
        "thiết bị này tạo ra các điện áp xoay chiều có biên độ tỉ lệ với sin và cos của góc trục synchro. Cũng có "
        "thể dùng tách sóng nhạy pha để chuyển các tín hiệu ra cho thích hợp với xử lý tín hiệu số."))

    b.append(h3("Cuộn cảm biến thiên tuyến tính", "Linear-Variable Inductor"))
    b.append(p(
        "Có rất ít khác biệt giữa đầu đo từ trở biến thiên và đầu đo điện cảm biến thiên. Về mặt toán học, "
        "nguyên lý của cuộn cảm biến thiên tuyến tính rất giống loại từ trở biến thiên; khác biệt chủ yếu nằm ở "
        "phần thu tín hiệu chứ không ở nguyên lý làm việc. Một cuộn cảm biến thiên tuyến tính điển hình gồm một "
        "lõi sắt di động cung cấp đầu vào cơ và hai cuộn dây tạo thành hai nhánh của một mạng cầu. Ví dụ điển "
        "hình của loại đầu đo này là đầu đo ghép biến thiên, bàn ngay dưới đây."))

    b.append(h3("Đầu đo ghép biến thiên", "Variable-Coupling Transducers"))
    b.append(p(
        "Những đầu đo này gồm một khuôn mang cuộn dây có điểm giữa và một lõi sắt từ, như trên Hình 6-14. Lõi và "
        "hai cuộn có cùng chiều dài l. Khi lõi dịch chuyển, điện cảm của các cuộn thay đổi. Hai điện cảm thường "
        "được đặt thành hai nhánh của một mạch cầu cùng hai điện trở cân bằng bằng nhau, như trên Hình 6-15. "
        "Cầu được kích bằng xoay chiều 5–25 V với tần số 50 Hz – 5 kHz. Ở tần số kích đã chọn, tổng trở của đầu "
        "đo tại điều kiện không được đặt trong khoảng 100–1000 Ω. Các điện trở được chọn có giá trị xấp xỉ tổng "
        "trở của đầu đo. Tải của đầu ra cầu phải ít nhất bằng 10 lần giá trị R. Khi lõi ở vị trí chuẩn, mỗi "
        "cuộn có điện cảm bằng nhau và bằng L. Khi lõi dịch δl, các thay đổi điện cảm +δL và −δL tạo ra một "
        "điện áp ra trên cầu. Với cầu được chế tạo cẩn thận, điện áp ra có thể là hàm tuyến tính của dịch chuyển "
        "trong một dải danh định."))
    b.append(fig(14, F.fig_6_14()))
    b.append(p(
        "Ở một số đầu đo, để giảm tổn hao công suất do đốt nóng điện trở, người ta dùng biến áp có điểm giữa làm "
        "một phần của mạng cầu, như trên Hình 6-15(b). Khi đó mạch trở nên có tính cảm nhiều hơn và phải hết "
        "sức cẩn thận tránh ghép hỗ cảm giữa biến áp với đầu đo."))
    b.append(fig(15, F.fig_6_15()))
    b.append(p(
        "Loại đầu đo này đặc biệt dễ chế tạo: chỉ cần quấn một cuộn dây có điểm giữa trên một khuôn phù hợp. Đầu "
        "đo điện cảm biến thiên bán trên thị trường có hành trình từ khoảng 2 mm đến 500 cm, độ nhạy từ 1 % toàn "
        "thang đến 0,02 % ở những kết cấu hành trình dài đặc biệt. Những thiết bị này còn được gọi là đầu đo "
        "dịch chuyển tuyến tính hay LDT, và có nhiều hình dạng, kích thước khác nhau."))
    b.append(p(
        "Ngoài loại tuyến tính, còn có loại quay với lõi được tạo hình riêng cho ứng dụng góc. Độ phi tuyến của "
        "chúng từ 0,5 % đến 1 % toàn thang trong dải quay 90°, và độ nhạy có thể tới 100 mV mỗi độ quay."))

    b.append(h3("Chiết áp cảm ứng", "Induction Potentiometer"))
    b.append(p(
        "Một phiên bản của cuộn cảm biến thiên kiểu quay là chiết áp cảm ứng trên Hình 6-16. Hai cuộn tập trung "
        "được quấn trên stato và rôto. Cuộn rôto được kích bằng xoay chiều, cảm ứng điện áp sang các cuộn stato. "
        "Biên độ điện áp ra phụ thuộc hỗ cảm giữa hai cuộn, mà hỗ cảm lại phụ thuộc góc quay. Với chiết áp cảm "
        "ứng kiểu cuộn tập trung, biên độ biến thiên theo sin nên chỉ tuyến tính trong vùng quanh vị trí không. "
        "Có thể đạt được phân bố tuyến tính trên 180° bằng các cuộn rải được thiết kế cẩn thận."))
    b.append(fig(16, F.fig_6_16()))
    b.append(p(
        "Chiết áp cảm ứng thương mại tiêu chuẩn làm việc trong dải tần 50–400 Hz. Chúng nhỏ, từ 1 cm đến 6 cm, "
        "và độ nhạy có thể vào cỡ 1 V mỗi độ quay. Tuy dải đo của chiết áp cảm ứng bị giới hạn dưới 60° quay, "
        "vẫn có thể đo dịch chuyển góc từ 0° đến trọn vòng bằng cách bố trí hợp lý một số chiết áp. Như với hầu "
        "hết cảm biến cảm ứng, đầu ra của chiết áp cảm ứng có thể cần bộ tách sóng nhạy pha và các bộ lọc phù "
        "hợp. Trong nhiều trường hợp, người ta dùng thêm các cuộn giả để cải thiện độ tuyến tính và độ chính "
        "xác."))

    b.append(h2("Biến áp vi sai tuyến tính (LVDT)", "Linear Variable-Differential Transformer (LVDT)"))
    b.append(p(
        "Biến áp vi sai tuyến tính LVDT là một đầu đo cảm ứng thụ động có rất nhiều ứng dụng. Nó gồm một cuộn sơ "
        "cấp đặt giữa hai cuộn thứ cấp giống nhau, quấn trên một ống lõi sắt từ, như trên Hình 6-17. Cuộn sơ cấp "
        "được nuôi bằng điện áp xoay chiều tần số cao, 50 Hz – 20 kHz. Hai cuộn thứ cấp được làm giống nhau bằng "
        "cách có cùng số vòng và hình học tương tự; chúng được đấu nối tiếp đối nhau sao cho các điện áp cảm ứng "
        "ra chống lại nhau."))
    b.append(fig(17, F.fig_6_17()))
    b.append(p(
        "Trong nhiều ứng dụng, các đầu ra được đấu đối nhau như trên Hình 6-18(a). Điện áp ra của từng cuộn thứ "
        "cấp v<sub>1</sub> và v<sub>2</sub> tại vị trí không được minh hoạ trên Hình 6-18(b). Tuy vậy, khi đấu "
        "đối nhau, mọi dịch chuyển của lõi khỏi điểm không một lượng x đều làm thay đổi biên độ điện áp ra "
        "v<sub>o</sub> và độ lệch pha α. Dạng sóng ra v<sub>o</sub> theo vị trí lõi được trình bày trên Hình "
        "6-18(c). Khi lõi nằm ở giữa, có sự ghép bằng nhau giữa sơ cấp và các thứ cấp, do đó có một điểm không "
        "hay điểm chuẩn của cảm biến. Chừng nào lõi còn ở gần tâm cụm cuộn dây, đầu ra rất tuyến tính. Dải tuyến "
        "tính của các biến áp vi sai thương mại được ghi rõ, và người ta hiếm khi dùng thiết bị ngoài dải tuyến "
        "tính ấy."))
    b.append(p(
        "Lõi sắt từ hay thanh dẫn từ di chuyển tự do bên trong ống, do đó làm thay đổi hỗ cảm giữa sơ cấp và các "
        "thứ cấp. Với lõi ở giữa, hay ở vị trí chuẩn, các sức điện động cảm ứng ở hai thứ cấp bằng nhau; vì "
        "chúng chống lại nhau nên điện áp ra bằng không. Khi lõi dịch, ví dụ sang trái, nhiều từ thông móc vòng "
        "cuộn bên trái hơn cuộn bên phải, nên điện áp cảm ứng ở cuộn trái lớn hơn. Độ lớn điện áp ra khi đó lớn "
        "hơn tại vị trí không và bằng hiệu hai điện áp thứ cấp; điện áp ra tổng hợp cùng pha với điện áp cuộn "
        "trái. Đầu ra của thiết bị vì thế là một chỉ thị dịch chuyển của lõi. Tương tự, chuyển động ngược lại "
        "sang phải đảo tác dụng, và điện áp ra cùng pha với sức điện động của cuộn phải."))
    b.append(p(
        "Để phân tích toán học hoạt động của LVDT, có thể dùng Hình 6-18(a). Điện áp cảm ứng trên các cuộn thứ "
        "cấp phụ thuộc hỗ cảm giữa sơ cấp và từng cuộn thứ cấp. Giả thiết không có ghép chéo giữa hai thứ cấp, "
        "các điện áp cảm ứng viết được là:"))
    b.append(eq("v<sub>1</sub> = M<sub>1</sub>·s·i<sub>p</sub> &nbsp; và &nbsp; "
                "v<sub>2</sub> = M<sub>2</sub>·s·i<sub>p</sub>", "6.15"))
    b.append(p(
        "với M<sub>1</sub> và M<sub>2</sub> là hỗ cảm giữa sơ cấp và các thứ cấp ứng với một vị trí lõi cố định; "
        "s là toán tử Laplace; i<sub>p</sub> là dòng sơ cấp."))
    b.append(fig(18, F.fig_6_18()))
    b.append(p(
        "Trong trường hợp đấu đối nhau, điện áp ra không tải v<sub>o</sub> khi không có dòng thứ cấp viết được "
        "là:"))
    b.append(eq("v<sub>o</sub> = v<sub>1</sub> − v<sub>2</sub> = (M<sub>1</sub> − M<sub>2</sub>)·s·i<sub>p</sub>",
                "6.16"))
    b.append(p("với"))
    b.append(eq("v<sub>p</sub> = i<sub>p</sub>(R<sub>p</sub> + L<sub>p</sub>·s)", "6.17"))
    b.append(p("Thay i<sub>p</sub> vào công thức 6.15 được hàm truyền của đầu đo:"))
    b.append(eq("v<sub>o</sub>/v<sub>p</sub> = (M<sub>1</sub> − M<sub>2</sub>)·s / (R<sub>p</sub> + "
                "L<sub>p</sub>·s)", "6.18"))
    b.append(p(
        "Tuy nhiên, nếu có dòng do mạch xử lý tín hiệu ra, các phương trình mô tả phải sửa lại:"))
    b.append(eq("v<sub>o</sub> = R<sub>m</sub>·i<sub>s</sub>", "6.19"))
    b.append(p(
        "với i<sub>s</sub> = (M<sub>1</sub> − M<sub>2</sub>)·s·i<sub>p</sub>/(R<sub>s</sub> + R<sub>m</sub> + "
        "L<sub>s</sub>·s), và"))
    b.append(eq("v<sub>p</sub> = i<sub>p</sub>(R<sub>p</sub> + L<sub>p</sub>·s) − "
                "(M<sub>1</sub> − M<sub>2</sub>)·s·i<sub>s</sub>", "6.20"))
    b.append(p("Khử i<sub>p</sub> và i<sub>s</sub> khỏi hai phương trình 6.19 và 6.20, được hàm truyền:"))
    b.append(eq("v<sub>o</sub>/v<sub>p</sub> = (M<sub>1</sub> − M<sub>2</sub>)·s·R<sub>m</sub> / "
                "{ (R<sub>p</sub> + L<sub>p</sub>s)(R<sub>s</sub> + R<sub>m</sub> + L<sub>s</sub>s) + "
                "(M<sub>1</sub> − M<sub>2</sub>)²s² }", "6.21"))
    b.append(p(
        "Đây là một hệ bậc hai; tử số của công thức 6.21 cho thấy góc pha của hệ chuyển từ +90° ở tần số thấp "
        "sang −90° ở tần số cao. Trong ứng dụng thực tế, tần số nguồn được chọn sao cho tại vị trí không của "
        "lõi, góc pha của hệ bằng 0°."))
    b.append(p(
        "Biên độ điện áp ra của các cuộn thứ cấp phụ thuộc vị trí lõi. Với chuyển động chậm của lõi và khi chiều "
        "chuyển động không quan trọng, có thể xử lý trực tiếp đầu ra của từng cuộn thứ cấp. Nhưng với chuyển "
        "động nhanh, cần đổi tín hiệu sang một chiều và phát hiện được chiều dịch chuyển khỏi vị trí không. Có "
        "nhiều cách làm; thông dụng nhất là dùng bộ tách sóng nhạy pha kèm bộ lọc, như trên Hình 6-19(a). Đầu ra "
        "điển hình của bộ tách sóng nhạy pha được minh hoạ trên Hình 6-19(b), theo tương quan với điện áp ra "
        "v<sub>o</sub>, dịch chuyển x và góc pha α."))
    b.append(fig(19, F.fig_6_19()))
    b.append(p(
        "Bộ tách sóng nhạy pha được dùng rộng rãi trong các cảm biến cảm ứng kiểu vi sai. Về cơ bản chúng đổi "
        "đầu ra xoay chiều thành giá trị một chiều và đồng thời chỉ ra chiều dịch chuyển của lõi so với vị trí "
        "không. Một mạch tách sóng nhạy pha điển hình có thể xây dựng trên cơ sở diode như trên Hình 6-20(a). "
        "Cách bố trí này hữu ích cho những dịch chuyển rất chậm, thường dưới 1 hoặc 2 Hz. Trong hình, cầu 1 làm "
        "mạch chỉnh lưu cho thứ cấp 1, cầu 2 làm mạch chỉnh lưu cho thứ cấp 2. Điện áp ra tổng hợp là hiệu hai "
        "đầu ra của hai cầu, như trên Hình 6-20(b). Vị trí lõi xác định được từ biên độ điện áp một chiều, còn "
        "chiều dịch chuyển xác định được từ dấu của điện áp một chiều ấy. Với chuyển động nhanh của lõi, đầu ra "
        "của các cầu diode phải được lọc, sao cho chỉ những tần số của chuyển động lõi đi qua còn mọi tần số do "
        "quá trình điều biến sinh ra đều bị lọc bỏ; một mạch RC đơn giản được thiết kế phù hợp thường là đủ."))
    b.append(fig(20, F.fig_6_20()))
    b.append(p(
        "Trên thị trường có các chip tách sóng nhạy pha, ví dụ AD598 của Analog Devices. Những chip này rất linh "
        "hoạt và dễ dùng để đáp ứng yêu cầu riêng của từng ứng dụng, với nhiều ưu điểm so với thiết bị tách sóng "
        "nhạy pha thông thường: tần số kích có thể chỉnh tới bất kỳ giá trị nào trong khoảng 20 Hz – 20 kHz bằng "
        "cách nối một tụ ngoài giữa hai chân; biên độ điện áp kích đặt được tới 24 V; các bộ lọc bên trong đặt "
        "được theo giá trị mong muốn bằng tụ ngoài; và việc nối tới bộ chuyển đổi tương tự – số trở nên dễ dàng "
        "nhờ đổi đầu ra lưỡng cực thành thang đơn cực."))
    b.append(p(
        "Đáp ứng tần số của LVDT chủ yếu bị giới hạn bởi đặc tính quán tính của thiết bị. Nói chung, tần số của "
        "điện áp đặt vào nên bằng 10 lần đáp ứng tần số mong muốn. LVDT thương mại có nhiều kích thước và được "
        "dùng rộng rãi để đo dịch chuyển trong nhiều ứng dụng, với dải đo từ ±0,25 mm đến ±7,5 cm. Chúng đủ nhạy "
        "để đáp ứng những dịch chuyển nhỏ hơn 0,0005 mm rất nhiều. Dải nhiệt độ làm việc từ −265 °C đến 600 °C; "
        "cũng có loại chịu bức xạ dùng trong lò phản ứng hạt nhân. Với một cảm biến điển hình dải ±25 mm, điện "
        "áp nguồn khuyến nghị là 4–6 V, tần số danh định 5 kHz và độ phi tuyến cực đại 1 % toàn thang. Một số "
        "model thương mại cho điện áp ra 300 mV ứng với 1 mm dịch chuyển của lõi."))
    b.append(p(
        "Một ưu điểm quan trọng của LVDT là không có tiếp xúc vật lý giữa lõi và ống dây, do đó không có ma sát "
        "hay mài mòn. Tuy vậy, luôn tồn tại lực từ hướng kính và hướng trục tác dụng lên lõi. Có thể coi những "
        "lực từ này như những “lò xo từ” luôn tìm cách đưa lõi về vị trí không; đây có thể là yếu tố quyết định "
        "trong một số ứng dụng."))
    b.append(p(
        "Một khó khăn của LVDT là không dễ làm cho hai nửa cuộn thứ cấp hoàn toàn giống nhau: điện cảm, điện trở "
        "và điện dung của chúng có thể khác nhau, gây ra một điện áp vuông pha lớn không mong muốn tại vị trí "
        "cân bằng. Có thể cần thiết bị quấn cuộn chính xác để giảm vấn đề này xuống mức chấp nhận được."))
    b.append(p(
        "Một vấn đề khác liên quan đến việc chỉnh vị trí không. Các hài trong điện áp nguồn và điện dung ký sinh "
        "gây ra những điện áp không nhỏ. Có thể giảm điện áp không bằng nối đất đúng cách — cách này giảm hiệu "
        "ứng điện dung — và bằng cách dùng nguồn có điểm giữa. Với nguồn có điểm giữa, có thể dùng một biến trở "
        "để chỉnh cho điện áp không là nhỏ nhất."))
    b.append(p(
        "LVDT có nhiều ứng dụng, gồm điều khiển động cơ phản lực ở rất gần khí xả và đo vị trí trục cán trong "
        "nhà máy thép tấm nóng. Sau một vài sửa đổi cơ khí, LVDT cũng dùng được để đo lực và áp suất."))

    b.append(h2("Biến áp vi sai lõi quay", "Rotary Variable-Differential Transformer"))
    b.append(p(
        "Một biến thể của biến áp vi sai tuyến tính là biến áp vi sai lõi quay trên Hình 6-21(a) và 6-21(b). Ở "
        "đây cuộn sơ cấp quấn trên trụ giữa của lõi chữ E, còn các cuộn thứ cấp quấn trên hai trụ ngoài. Phần "
        "ứng quay dưới tác dụng của một lực ngoài quanh một điểm tựa phía trên trụ giữa. Khi phần ứng lệch khỏi "
        "vị trí chuẩn hay vị trí cân bằng, từ trở của mạch từ qua một cuộn thứ cấp giảm, đồng thời từ trở qua "
        "cuộn kia tăng. Các sức điện động cảm ứng trong hai cuộn thứ cấp — vốn bằng nhau ở vị trí chuẩn — nay "
        "khác nhau về biên độ và pha do dịch chuyển áp vào. Các sức điện động này được đấu đối nhau và biến áp "
        "làm việc giống hệt một LVDT. Biến áp quay có thể nhạy với rung; nếu cần đầu ra một chiều thì dùng được "
        "mạng tách sóng như với LVDT."))
    b.append(fig(21, F.fig_6_21()))
    b.append(p(
        "Ở hầu hết biến áp vi sai lõi quay, khối lượng rôto rất nhỏ, thường dưới 5 g. Độ phi tuyến của đầu ra từ "
        "±1 % đến ±3 % tuỳ góc quay. Chuyển động theo hướng kính tạo ra một tín hiệu ra nhỏ có thể ảnh hưởng đến "
        "độ nhạy tổng; tuy vậy độ nhạy ngang này thường được giữ dưới 1 % độ nhạy dọc."))

    b.append(h2("Dòng xoáy", "Eddy Current"))
    b.append(p(
        "Các đầu đo cảm ứng dựa trên dòng xoáy chủ yếu là loại đầu dò, chứa hai cuộn dây như trên Hình 6-22. Một "
        "cuộn — gọi là cuộn tích cực — chịu ảnh hưởng của vật dẫn mục tiêu. Cuộn thứ hai — cuộn cân bằng — hoàn "
        "thiện mạch cầu và bù nhiệt. Từ thông từ cuộn tích cực đi vào vật dẫn mục tiêu qua đầu dò. Khi đầu dò "
        "được đưa lại gần mục tiêu, từ thông từ đầu dò móc vòng sang mục tiêu và sinh dòng xoáy trong mục tiêu."))
    b.append(fig(22, F.fig_6_22()))
    b.append(p(
        "Mật độ dòng xoáy lớn nhất ở bề mặt mục tiêu và trở nên rất nhỏ, khoảng ba độ sâu lớp da dưới bề mặt. Độ "
        "sâu lớp da phụ thuộc loại vật liệu và tần số kích. Có thể dùng mục tiêu mỏng hơn, nhưng thường cần tối "
        "thiểu ba độ sâu lớp da để giảm thiểu ảnh hưởng nhiệt. Khi mục tiêu lại gần đầu dò hơn, dòng xoáy mạnh "
        "lên, làm tổng trở cuộn tích cực thay đổi và làm mất cân bằng cầu theo vị trí mục tiêu. Điện áp mất cân "
        "bằng này có thể được tách sóng, lọc và tuyến tính hoá để cho đầu ra một chiều tỉ lệ với dịch chuyển của "
        "mục tiêu. Tần số dao động của cầu có thể tới 1 MHz; tần số cao cho phép dùng mục tiêu mỏng và cho đáp "
        "ứng tần số hệ thống tốt."))
    b.append(p(
        "Đầu dò bán trên thị trường có đường kính toàn thang từ 0,25 đến 30 mm, độ phi tuyến 0,5 % và độ phân "
        "giải cực đại 0,0001 mm. Mục tiêu thường do khách hàng cung cấp, gắn với các phép đo không tiếp xúc trên "
        "chi tiết máy. Với mục tiêu không dẫn điện, phải dán vật liệu dẫn điện đủ dày lên bề mặt bằng keo dán "
        "bán trên thị trường."))
    b.append(p(
        "Vì vật liệu, hình dạng… của mục tiêu ảnh hưởng đến đầu ra, cần hiệu chuẩn hệ thống theo từng mục tiêu cụ "
        "thể. Dải đo khuyến nghị của một đầu dò bắt đầu từ khoảng cách đứng bằng khoảng 20 % dải đo danh định "
        "của đầu dò. Trong một số trường hợp, khoảng cách đứng 10 % được khuyến nghị và hệ thống được hiệu chuẩn "
        "theo chuẩn ấy; có thể dùng khoảng cách lớn hơn 10 % dải đo miễn là dải đo đã hiệu chuẩn giảm đi đúng "
        "mức tương ứng."))
    b.append(p(
        "Mục tiêu phẳng phải có đường kính bằng hoặc lớn hơn đường kính đầu dò. Nếu đường kính mục tiêu nhỏ hơn "
        "đầu dò, đầu ra giảm đáng kể và trở nên không đáng tin. Mục tiêu mặt cong có thể xử sự như mặt phẳng nếu "
        "đường kính lớn hơn khoảng ba đến bốn lần đường kính đầu dò; khi đó mục tiêu thực chất trở thành một mặt "
        "phẳng vô hạn, và cũng cho phép một ít chuyển động ngang mà không ảnh hưởng đầu ra. Mục tiêu có đường "
        "kính chỉ xấp xỉ cảm biến có thể gây hại cho phép đo do chuyển động ngang."))
    b.append(p(
        "Với mục tiêu cong hoặc không đều, phải hiệu chuẩn hệ thống bằng đúng mục tiêu sẽ gặp trong vận hành; "
        "cách này loại trừ được các sai số do mặt cong gây ra. Tuy nhiên, với chuyển động quỹ đạo của trục quay, "
        "có sẵn những hệ nhiều đầu dò đặc biệt. Nếu mục tiêu cong (trục) lớn hơn khoảng 10 lần đường kính cảm "
        "biến, nó xử sự như mặt phẳng vô hạn và không cần hiệu chuẩn đặc biệt. Cần lưu ý đến độ đảo điện do các "
        "yếu tố như độ không đồng nhất về độ cứng…, đặc biệt với mục tiêu sắt từ; mục tiêu phi sắt từ không gặp "
        "vấn đề này."))

    b.append(h2("Che chắn và độ nhạy của cảm biến cảm ứng với nhiễu điện từ",
                "Shielding and Sensitivity of Inductive Sensors to Electromagnetic Interference"))
    b.append(p(
        "Từ trường sinh ra bởi dòng điện trong dây dẫn và mạnh hơn nhiều bởi các cuộn dây. Từ trường của cuộn dây "
        "quan trọng vì ghép từ, nhất là khi trong mạch có hai cuộn trở lên. Có thể kiểm soát ghép từ giữa các "
        "cuộn bằng khoảng cách lớn giữa chúng, bằng hướng và hình dạng cuộn, và bằng che chắn."))
    b.append(p(
        "Cảm biến cảm ứng có nhiều hình dạng và kích thước. Một số có lõi kín như dạng hình xuyến, số khác có lõi "
        "hở và có khe hở không khí giữa lõi và cuộn. Lõi kín thực tế có thể có từ trường ngoài bằng không, trừ "
        "một ít từ thông rò. Ngay cả khi không có lõi kín, hầu hết cảm biến điện cảm biến thiên vẫn có từ trường "
        "ngoài khá hạn chế, nhờ hai bộ cuộn lân cận được đấu ngược chiều nhau để triệt tiêu từ trường ngoài."))
    b.append(p(
        "Cảm biến cảm ứng được làm từ vật dẫn kín. Điều đó có nghĩa là nếu vật dẫn chuyển động trong từ trường, "
        "sẽ có dòng điện chạy; ngược lại, một thay đổi từ trường cũng sinh dòng trong vật dẫn kín đứng yên. Nếu "
        "không có biện pháp thoả đáng, từ trường ngoài có thể móc vòng (gây nhiễu) vào các cuộn cảm biến, sinh "
        "dòng và những đáp ứng không mong muốn."))
    b.append(p(
        "Do nguyên lý vận hành, cảm biến cảm ứng được thiết kế để có độ nhạy cao với thay đổi từ thông. Nhiễu "
        "điện từ bên ngoài và từ trường ngoài có thể ảnh hưởng nghiêm trọng đến tính năng của cảm biến. Đã biết "
        "rằng quanh máy biến áp lực, động cơ điện và đường dây tải điện có những từ trường vừa phải; những từ "
        "trường nhỏ này sinh dòng trong các phần tử của cảm biến cảm ứng. Một cách loại trừ ảnh hưởng ngoài là "
        "che chắn từ cho cảm biến và nối đất thích hợp. Trong che chắn từ, một hay nhiều lớp vỏ bằng vật liệu từ "
        "có độ từ thẩm cao bao quanh phần cần che; có thể dùng nhiều lớp để che chắn rất hoàn chỉnh. Hai đầu mỗi "
        "lớp vỏ được cách điện với nhau để vỏ không trở thành một vòng ngắn mạch kín, nhờ đó chịu được dòng lớn. "
        "Tương tự, khi che nhiều lớp, các lớp cũng được cách điện lẫn nhau."))
    b.append(p(
        "Từ trường xoay chiều cũng được chắn bằng cách đặt những tấm kim loại dẫn điện tốt như đồng hoặc nhôm "
        "trên đường đi của từ thông. Dòng xoáy cảm ứng trong tấm chắn tạo ra một sức từ động ngược có xu hướng "
        "triệt tiêu từ trường gây nhiễu. Kiểu che chắn này đặc biệt hiệu quả ở tần số cao; tuy vậy vẫn phải nối "
        "đất đúng cách."))
    b.append(p(
        "Ở nhiều cảm biến cảm ứng, điện dung ký sinh có thể là vấn đề, nhất là tại vị trí không của lõi di động. "
        "Nếu hiệu ứng điện dung lớn hơn một giá trị nào đó — chẳng hạn 1 % đầu ra toàn thang — có thể giảm nó "
        "bằng nguồn có điểm giữa và nối đất thích hợp."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. P. Bentley, <i>Principles of Measurement Systems</i>, 2nd ed., UK: Longman Scientific and "
        "Technical, 1988.",
        "E. O. Doebelin, <i>Measurement Systems: Application and Design</i>, 4th ed., New York: McGraw-Hill, 1990.",
        "J. P. Holman, <i>Experimental Methods for Engineers</i>, 5th ed., New York: McGraw-Hill, 1989.",
        "W. J. Tompkins and J. G. Webster, <i>Interfacing Sensors to the IBM PC</i>, Englewood Cliffs, NJ: "
        "Prentice-Hall, 1988.",
    ]))
    b.append(note(
        "<b>Phụ lục 6.2 — Danh sách nhà sản xuất.</b> Bản in liệt kê 14 hãng kèm địa chỉ, điện thoại và fax: "
        "Adsen Tech. (La Puente, CA), Dynalco Controls (Ft. Lauderdale, FL), Electro Corporation (Sarasota, FL), "
        "Honeywell (Freeport, IL), Kaman Instruments (Colorado Springs, CO), Kavlico (Moorpark, CA), Lucas "
        "(Hampton, VA), Motion Sensors (Elizabeth City, NC), Rechner Electronics (Niagara Falls, NY), Reed "
        "Switch Developments (Racine, WI), Smith Research &amp; Technology và Smith Systems (Colorado Springs / "
        "Brevard), Standex Electronics (Cincinnati, OH), Turck (Minneapolis, MN), Xolox Sensor Products (Ft. "
        "Wayne, IN). Địa chỉ và số điện thoại trong bản in đã quá cũ để tra cứu trực tiếp; nên tìm theo tên "
        "hãng."))
    b.append(nav(2, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Sixteen figures in sixteen pages, and one idea underneath all of them: a magnetic circuit whose "
        "reluctance depends on position. Everything in section 6.2 is that idea with a different pickup bolted "
        "on — one coil, two coils, a toothed wheel, a rotating armature, a probe looking at eddy currents in "
        "someone else’s metal."))
    b.append(h2("Reluctance is the whole story"))
    b.append(p(
        "Flux is magnetomotive force divided by reluctance, and reluctance is length over permeability times "
        "area. Put an air gap in the path and the reluctance jumps by three orders of magnitude, because mu "
        "drops from a few thousand to one. That is the sensitivity mechanism: a gap that moves a fraction of a "
        "millimetre changes the flux, and therefore the inductance, by something you can measure."))
    b.append(eq("ℜ = l / (μ μ<sub>0</sub> A) &nbsp;→&nbsp; L = n² / ℜ", "6.6"))
    b.append(fig(7, F.fig_6_7(), "en"))
    b.append(h2("Single coil, then differential"))
    b.append(p(
        "The single-coil sensor is simple and nonlinear: L falls off as 1/(1 + αd), which is fine for a force "
        "cell modulating an LC oscillator and poor for a position measurement. The fix is to put two identical "
        "coils either side of the armature and wire them in opposition, so the nonlinearities cancel to first "
        "order over a small range. That is the pattern the rest of the section repeats."))
    b.append(fig(8, F.fig_6_8(), "en"))
    b.append(fig(9, F.fig_6_9(), "en"))
    b.append(h2("The family tree"))
    b.append(table(
        ["Device", "What moves", "Output", "Typical use"],
        [["Single-coil VR", "gap", "inductance", "force, telemetry"],
         ["Differential VR", "armature between two cores", "ac, phase reverses at null", "small displacements, "
          "pressure"],
         ["Tachogenerator", "toothed wheel past a pole", "ac, frequency ∝ speed", "speed, flow totalising"],
         ["Microsyn", "rotor in a four-coil stator", "ac, 180° flip at null", "gyroscopes, 0.01° resolution"],
         ["Synchro", "wound rotor", "three-phase ac", "angle in servos"],
         ["Linear variable inductor", "plunger in a centre-tapped coil", "bridge unbalance", "2 mm – 500 cm "
          "strokes"],
         ["Induction pot", "rotor winding", "ac amplitude ∝ M(θ)", "±60° angle"],
         ["LVDT", "core in primary/secondary stack", "ac, demodulated to dc", "the workhorse"],
         ["RVDT", "armature on an E core", "ac", "limited-angle feedback"],
         ["Eddy current", "target surface", "bridge unbalance", "non-contact, 0.1 µm"]],
        "Table 6.2a · The ten devices in section 6.2, and what each one actually measures."))
    b.append(fig(11, F.fig_6_11(), "en"))
    b.append(fig(12, F.fig_6_12(), "en"))
    b.append(h2("The LVDT, and why it won"))
    b.append(p(
        "Two secondaries in series opposition, a core that slides through both, and a null in the middle. At "
        "null the induced emfs are equal and cancel; move the core and one grows while the other shrinks, so the "
        "output amplitude tracks displacement and the phase flips by 180° as the core crosses the centre. That "
        "phase flip is what lets a phase-sensitive demodulator recover the sign of the displacement, which is "
        "the thing a single coil cannot give you."))
    b.append(fig(17, F.fig_6_17(), "en"))
    b.append(fig(18, F.fig_6_18(), "en"))
    b.append(p(
        "The transfer function is second order once you include the secondary loading, and the numerator puts "
        "the phase at +90° at low frequency and −90° at high frequency. The supply frequency is chosen so the "
        "phase passes through zero at the null position — which is why an LVDT is specified with its carrier "
        "frequency, not just its range."))
    b.append(eq("v<sub>o</sub>/v<sub>p</sub> = (M<sub>1</sub>−M<sub>2</sub>) s R<sub>m</sub> / "
                "{(R<sub>p</sub>+L<sub>p</sub>s)(R<sub>s</sub>+R<sub>m</sub>+L<sub>s</sub>s) + "
                "(M<sub>1</sub>−M<sub>2</sub>)²s²}", "6.21"))
    b.append(fig(19, F.fig_6_19(), "en"))
    b.append(fig(20, F.fig_6_20(), "en"))
    b.append(h2("The two problems the datasheet hides"))
    b.append(p(
        "Sharp makes two admissions worth repeating. First, the two secondaries are never quite identical — "
        "different inductance, resistance and capacitance produce a quadrature voltage at balance that no "
        "amount of careful alignment removes, only precision winding does. Second, the null is never exactly "
        "zero: harmonics in the supply and stray capacitance leave a residual, which is why centre-tapped "
        "excitation and a trim pot exist."))
    b.append(fig(21, F.fig_6_21(), "en"))
    b.append(h2("Eddy currents: measuring someone else’s metal"))
    b.append(p(
        "The probe never touches the target. Its flux induces eddy currents in the target surface, those "
        "currents push back on the active coil, and the bridge reads the push. Three skin depths of target "
        "thickness is the rule; the target must be at least as wide as the probe, or four times the probe "
        "diameter if it is curved, before it behaves like an infinite plane."))
    b.append(fig(22, F.fig_6_22(), "en"))
    b.append(h2("Shielding"))
    b.append(p(
        "An inductive sensor is a closed conductor sitting in a world full of stray fields, so it will pick up "
        "currents from every transformer and motor nearby. Two defences: high-permeability shells (insulated "
        "from each other so they do not form a shorted turn), and conductive sheets whose eddy currents "
        "generate a cancelling mmf. The second works well at high frequency; neither works without proper "
        "grounding."))
    b.append(nav(2, "en"))
    return "".join(b)
