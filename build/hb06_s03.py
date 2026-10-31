# -*- coding: utf-8 -*-
"""Handbook 6.3 — Capacitive Sensors: Displacement."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Cảm biến điện dung được dùng rất rộng rãi trong công nghiệp và trong nghiên cứu khoa học. Nguyên lý "
        "chung của chúng là sự thay đổi điện dung khi có biến thiên vật lý. Phạm vi ứng dụng rất đa dạng — từ đo "
        "độ ẩm, độ ẩm vật liệu cho tới đo dịch chuyển. Có trường hợp các nguyên lý tác động và cảm nhận cơ bản "
        "giống nhau lại phục vụ những ứng dụng hoàn toàn khác nhau; cũng có trường hợp cùng một ứng dụng lại có "
        "thể dùng những nguyên lý khác nhau. Ví dụ, micro điện dung dựa trên sự thay đổi khoảng cách giữa hai bản "
        "cực dưới tác dụng của áp suất âm thanh, nhờ đó biến tín hiệu âm thanh thành biến thiên điện dung. Ngược "
        "lại, một chỉ báo mức kiểu điện dung lại lợi dụng sự thay đổi hằng số điện môi tương đối giữa hai bản "
        "cực. Tuy vậy, cảm biến điện dung được biết đến nhiều nhất gắn với việc đo dịch chuyển — chuyển động quay "
        "hoặc chuyển động tịnh tiến — và đó là nội dung được trình bày dưới đây. Các ứng dụng khác như đo độ ẩm "
        "sẽ được bàn ở phần sau của mục này."))

    # ---------------------------------------------------------------- 6.3.1
    b.append(h2("Cảm biến dịch chuyển điện dung", "Capacitive displacement sensors"))
    b.append(p(
        "Đo khoảng cách hay dịch chuyển là một khía cạnh quan trọng của rất nhiều hệ thống công nghiệp, khoa học "
        "và kỹ thuật. Dịch chuyển, về bản chất, là vectơ biểu diễn sự thay đổi vị trí của một vật hay một điểm so "
        "với một điểm quy chiếu. Cảm biến dịch chuyển điện dung đáp ứng được yêu cầu của những ứng dụng cần độ "
        "tuyến tính cao và dải đo rộng — từ vài centimét cho tới vài nanomét."))
    b.append(p(
        "Phần tử cảm nhận cơ bản của một cảm biến dịch chuyển điển hình chỉ gồm hai điện cực đơn giản có điện dung "
        "C. Điện dung là hàm của khoảng cách d (cm) giữa hai điện cực, diện tích bề mặt A (cm²) của điện cực và "
        "hằng số điện môi ε (8,85 × 10⁻¹² F·m⁻¹ đối với không khí) của chất điện môi nằm giữa hai điện cực. Do đó:"))
    b.append(eq("C = f(d, A, ε)", "6.22"))
    b.append(p(
        "Có ba cách cơ bản để thực hiện một cảm biến dịch chuyển điện dung: thay đổi d, thay đổi A, hoặc thay đổi "
        "ε. Ba cách này được trình bày lần lượt dưới đây."))

    b.append(h3("Cảm biến biến thiên khoảng cách", "Variable-distance sensors"))
    b.append(p(
        "Một cảm biến điện dung chế từ hai bản phẳng song song, cách nhau một khoảng biến thiên x, được minh hoạ "
        "trên Hình 6-23. Bỏ qua hiệu ứng viền, điện dung của kết cấu này viết được là:"))
    b.append(fig(23, F.fig_6_23(), "vi"))
    b.append(eq("C(x) = ε<sub>r</sub> ε<sub>0</sub> A / x", "6.23"))
    b.append(p(
        "trong đó ε = hằng số điện môi hay độ thẩm điện; ε<sub>r</sub> = hằng số điện môi tương đối (trong không "
        "khí và chân không ε<sub>r</sub> ≈ 1); ε<sub>0</sub> = 8,854188 × 10⁻¹² F·m⁻¹ là hằng số điện môi của chân "
        "không; x = khoảng cách giữa hai bản, tính bằng mét; A = diện tích hiệu dụng của bản, tính bằng m²."))
    b.append(p(
        "Điện dung của đầu đo này phi tuyến theo khoảng cách x, có đặc tính truyền dạng hyperbolic. Độ nhạy của "
        "điện dung theo sự thay đổi khoảng cách bản cực là:"))
    b.append(eq("dC/dx = − ε<sub>r</sub> ε<sub>0</sub> A / x²", "6.24"))
    b.append(p(
        "Phương trình 6.24 cho thấy độ nhạy tăng khi x giảm. Tuy vậy, từ hai phương trình 6.23 và 6.24 suy ra rằng "
        "phần trăm thay đổi của C tỉ lệ với phần trăm thay đổi của x. Có thể viết:"))
    b.append(eq("dC/C = − dx/x", "6.25"))
    b.append(p(
        "Loại cảm biến này thường dùng để đo những dịch chuyển nhỏ, tăng dần, mà không cần tiếp xúc với vật thể."))

    b.append(h3("Cảm biến biến thiên diện tích", "Variable-area sensors"))
    b.append(p(
        "Một cách khác là cảm nhận dịch chuyển bằng sự thay đổi diện tích bề mặt của các điện cực trong một tụ "
        "phẳng, như minh hoạ trên Hình 6-24. Khi ấy điện dung sẽ là:"))
    b.append(fig(24, F.fig_6_24(), "vi"))
    b.append(eq("C = ε<sub>r</sub> ε<sub>0</sub> (A − w·x) / d", "6.26"))
    b.append(p(
        "trong đó w = chiều rộng; w·x = phần diện tích bị giảm đi do bản cực dịch chuyển. Khi ấy đầu ra của đầu đo "
        "tuyến tính theo dịch chuyển x. Loại cảm biến này thường được thực hiện dưới dạng tụ quay để đo dịch "
        "chuyển góc. Kết cấu tụ quay cũng được dùng làm đầu đo ra để đo điện áp — đó là các vôn kế điện dung."))

    b.append(h3("Cảm biến biến thiên chất điện môi", "Variable-dielectric sensors"))
    b.append(p(
        "Trong một số trường hợp, có thể cảm nhận dịch chuyển nhờ chuyển động tương đối của chất điện môi nằm giữa "
        "hai bản cực, như trên Hình 6-25. Phương trình tương ứng là:"))
    b.append(fig(25, F.fig_6_25(), "vi"))
    b.append(eq("C = ε<sub>0</sub> w [ ε<sub>2</sub>(l − x) + ε<sub>1</sub> x ] / d", "6.27"))
    b.append(p(
        "trong đó ε<sub>1</sub> = độ thẩm điện tương đối của chất điện môi; ε<sub>2</sub> = độ thẩm điện của vật "
        "liệu dịch chuyển (ví dụ chất lỏng). Trong trường hợp này đầu ra của đầu đo cũng tuyến tính. Loại đầu đo "
        "này chủ yếu được dùng dưới dạng hai trụ đồng tâm để đo mức chất lưu trong bồn chứa. Chất lưu không dẫn "
        "điện đóng vai trò chất điện môi. Nội dung này sẽ được bàn tiếp ở phần đo mức."))

    b.append(h3("Cảm biến điện dung vi sai", "Differential capacitive sensors"))
    b.append(p(
        "Một phần tính phi tuyến của cảm biến điện dung có thể khử được nhờ kết cấu vi sai. Về bản chất, đây là "
        "các tụ ba cực, như trên Hình 6-26. Những biến thể nhỏ trong kết cấu tìm thấy rất nhiều ứng dụng khác "
        "nhau, trong đó có đo hiệu áp. Ở một số phiên bản, bản giữa di chuyển theo biến vật lý so với hai bản cố "
        "định. Ở phiên bản khác, bản giữa cố định còn hai bản ngoài được phép di chuyển. Đầu ra lấy từ bản giữa "
        "bằng không tại vị trí danh định và tăng lên khi bản giữa dịch sang trái hoặc sang phải. Dải đo bằng hai "
        "lần khoảng cách d. Với một dịch chuyển d, ta có:"))
    b.append(fig(26, F.fig_6_26(), "vi"))
    b.append(eq("δC = C<sub>1</sub> − C<sub>2</sub> = 2 ε<sub>r</sub> ε<sub>0</sub> l w δd / (d² − δd²)", "6.28"))
    b.append(p("và"))
    b.append(eq("C<sub>1</sub> + C<sub>2</sub> = 2 ε<sub>r</sub> ε<sub>0</sub> l w d / (d² − δd²)", "6.29"))
    b.append(p("do đó xấp xỉ:"))
    b.append(eq("δC/C = δd/d", "6.30"))
    b.append(p(
        "Điều này cho thấy đáp ứng của thiết bị tuyến tính hơn đáp ứng của kiểu hai bản cực. Tuy vậy, trên thực tế "
        "vẫn còn thấy một ít phi tuyến do khuyết tật trong kết cấu. Vì vậy đầu ra của loại cảm biến này vẫn cần "
        "được xử lý cẩn thận, như sẽ trình bày ở phần xử lý tín hiệu."))
    b.append(p(
        "Ở một số cảm biến điện dung vi sai, hai hốc cầu được mài vào hai đĩa thuỷ tinh, rồi được mạ vàng để tạo "
        "thành hai bản cực cố định của một tụ vi sai. Một màng thép không gỉ mỏng được kẹp giữa hai đĩa và đóng "
        "vai trò bản cực di động. Khi áp suất đặt lên hai cửa bằng nhau, màng ở vị trí trung hoà và đầu ra cân "
        "bằng trên một cầu đo tương ứng. Nếu một áp suất lớn hơn áp suất kia, màng võng tỉ lệ và cho ra tín hiệu "
        "theo hiệu áp. Với hiệu áp ngược dấu, pha đổi 180°. Có thể thu được đầu ra một chiều nhạy với chiều dịch "
        "chuyển bằng cách tách sóng nhạy pha thông thường và lọc thích hợp. Chi tiết xử lý tín hiệu được trình "
        "bày ở cuối chương này. Nói chung, tụ vi sai có độ tuyến tính tốt hơn kiểu một tụ đơn."))

    b.append(h3("Cảm biến vị trí điện dung thông minh tích hợp",
                "Integrated-circuit smart capacitive position sensors"))
    b.append(p(
        "Hình 6-27 trình bày một cảm biến dịch chuyển điện dung vi cơ điển hình. Cảm biến gồm hai điện cực có "
        "điện dung C<sub>x</sub>. Vì hệ đơn giản, việc xác định điện dung giữa hai điện cực là chuyện dễ. Điện cực "
        "nhỏ hơn được bao quanh bởi một điện cực bảo vệ để C<sub>x</sub> không phụ thuộc vào chuyển động ngang và "
        "chuyển động quay của hệ song song với mặt điện cực. Tuy vậy, việc dùng điện cực bảo vệ lại đưa vào những "
        "sai lệch tương đối của điện dung C<sub>x</sub> giữa hai điện cực. Điều này chỉ đúng một phần nếu kích "
        "thước điện cực bảo vệ nhỏ hơn:"))
    b.append(fig(27, F.fig_6_27(), "vi"))
    b.append(eq("δ &lt; exp(−πx/d)", "6.31"))
    b.append(p(
        "trong đó x là chiều rộng của vành bảo vệ và d là khoảng cách giữa hai điện cực. Vì sai lệch này gây ra "
        "phi tuyến, yêu cầu δ nhỏ hơn 100 ppm. Một dạng sai lệch khác cũng tồn tại giữa điện cực nhỏ và vành bảo "
        "vệ xung quanh, đặc biệt với các khe hở:"))
    b.append(eq("δ &lt; exp(−πd/s)", "6.32"))
    b.append(p(
        "trong đó s là chiều rộng của khe. Khi chiều rộng khe s nhỏ hơn 1/3 khoảng cách giữa hai điện cực, sai "
        "lệch này bỏ qua được."))
    b.append(p(
        "Về xử lý tín hiệu, hệ dùng khái niệm ba tín hiệu. Tụ C<sub>x</sub> được nối vào một khuếch đại thuật toán "
        "mắc đảo và một bộ dao động. Nếu chuyển động bên ngoài là tuyến tính, khi tính đến các tụ ký sinh và hiệu "
        "ứng lệch không, có thể viết phương trình sau:"))
    b.append(eq("M<sub>x</sub> = m·C<sub>x</sub> + M<sub>off</sub>", "6.33"))
    b.append(p(
        "trong đó m là độ lợi chưa biết và M<sub>off</sub> là độ lệch chưa biết. Bằng cách đo một tụ chuẩn "
        "C<sub>ref</sub>, đo độ lệch M<sub>off</sub> và cho m = 0, có thể khử được hai tham số m và "
        "M<sub>off</sub>. Kết quả đo cuối cùng của vị trí, Pos, được định nghĩa là:"))
    b.append(eq("Pos = (M<sub>x</sub> − M<sub>off</sub>) / (M<sub>ref</sub> − M<sub>off</sub>)", "6.34"))
    b.append(p("Khi ấy điện dung cảm biến C<sub>x</sub> rút gọn thành:"))
    b.append(eq("C<sub>x</sub> = ε<sub>0</sub> A<sub>x</sub> / (d<sub>0</sub> + ∆d)", "6.35"))
    b.append(p(
        "trong đó A<sub>x</sub> là diện tích điện cực, d<sub>0</sub> là khoảng cách ban đầu giữa hai điện cực, ε là "
        "hằng số điện môi và ∆d là dịch chuyển cần đo. Với các điện cực chuẩn, điện dung chuẩn tìm được là:"))
    b.append(eq("C<sub>ref</sub> = ε<sub>0</sub> A<sub>ref</sub> / d<sub>ref</sub>", "6.36"))
    b.append(p(
        "với A<sub>ref</sub> là diện tích và d<sub>ref</sub> là khoảng cách. Thay hai phương trình 6.35 và 6.36 vào "
        "6.33 và 6.34 thu được:"))
    b.append(eq("Pos = a<sub>1</sub> (∆d/d<sub>0</sub>) + a<sub>0</sub>", "6.37"))
    b.append(p(
        "Pos là một giá trị biểu diễn vị trí nếu các hằng số ổn định a<sub>1</sub> và a<sub>0</sub> chưa biết. Hằng "
        "số a<sub>1</sub> = A<sub>ref</sub>/A<sub>x</sub> trở thành hằng số ổn định chừng nào còn có sự ăn khớp cơ "
        "khí tốt giữa diện tích các điện cực. Hằng số a<sub>0</sub> = (A<sub>ref</sub> d<sub>0</sub>)/(A<sub>x</sub> "
        "d<sub>ref</sub>) cũng là hằng số ổn định khi d<sub>0</sub> và d<sub>ref</sub> cố định. Các hằng số này "
        "thường được xác định bằng hiệu chuẩn lặp lại trong một khoảng thời gian nhất định. Trong nhiều ứng dụng, "
        "có thể bỏ qua các lần hiệu chuẩn này nếu cảm biến dịch chuyển là một phần của hệ lớn hơn mà ở đó đã có "
        "hiệu chuẩn tổng thể. Hiệu chuẩn tổng thể ấy thường loại bỏ được yêu cầu xác định riêng a<sub>1</sub> và "
        "a<sub>0</sub>."))
    b.append(p(
        "Độ chính xác của loại hệ này có thể nhỏ tới 1 µm trên dải 1 mm. Tổng thời gian đo tốt hơn 0,1 s. Dải điện "
        "dung từ 1 pF đến 50 fF. Bạn đọc quan tâm nên xem tài liệu [4] ở cuối mục này."))

    # ---------------------------------------------------------------- 6.3.2
    b.append(h2("Cảm biến áp suất điện dung", "Capacitive pressure sensors"))
    b.append(p(
        "Một cảm biến áp suất điện dung hai bản thường dùng gồm một bản kim loại cố định và một màng mỏng đàn hồi, "
        "như trên Hình 6-28. Màng tròn phẳng được kẹp ở chu vi và bị uốn thành mặt cong bởi áp suất P tác dụng. "
        "Độ võng thẳng đứng y của hệ tại bán kính r bất kỳ cho bởi:"))
    b.append(fig(28, F.fig_6_28(), "vi"))
    b.append(eq("y = 3(1 − ν²) (a² − r²)² P / (16 E t³)", "6.38"))
    b.append(p(
        "trong đó a = bán kính màng; t = độ dày màng; E = môđun Young; ν = hệ số Poisson. Sự biến dạng của màng "
        "làm giảm khoảng cách trung bình giữa hai bản cực. Do đó, độ tăng điện dung ∆C tính được là:"))
    b.append(eq("∆C/C = (1 − ν²) a⁴ P / (16 E t³ d)", "6.39"))
    b.append(p(
        "trong đó d là khoảng cách ban đầu giữa hai bản và C là điện dung khi áp suất bằng không."))
    b.append(p(
        "Một loại cảm biến khác là cảm biến áp suất điện dung vi sai trên Hình 6-29. Điện dung C<sub>1</sub> và "
        "C<sub>2</sub> của cảm biến thay đổi so với bản giữa cố định khi áp suất P<sub>1</sub> và P<sub>2</sub> tác "
        "dụng. Do đó đầu ra của cảm biến tỉ lệ với (P<sub>1</sub> − P<sub>2</sub>). Tín hiệu được xử lý bằng một "
        "trong các kỹ thuật trình bày ở phần “Xử lý tín hiệu” của chương này."))
    b.append(fig(29, F.fig_6_29(), "vi"))

    # ---------------------------------------------------------------- 6.3.3
    b.append(h2("Gia tốc kế và đầu đo lực kiểu điện dung",
                "Capacitive accelerometers and force transducers"))
    b.append(p(
        "Trong những năm gần đây, gia tốc kế vi cơ kiểu điện dung, như minh hoạ trên Hình 6-30, ngày càng phổ "
        "biến. Các gia tốc kế này dùng khối chứng làm một bản cực của tụ và dùng bản kia làm đế. Khi cảm biến được "
        "gia tốc, khối chứng có xu hướng dịch chuyển; do đó điện áp trên tụ thay đổi. Sự thay đổi điện áp này "
        "tương ứng với gia tốc tác dụng."))
    b.append(fig(30, F.fig_6_30(), "vi"))
    b.append(p(
        "Trên Hình 6-30, gọi F(x) là lực dương theo chiều tăng của x. Bỏ qua mọi tổn hao (do ma sát, điện trở…), "
        "cân bằng năng lượng của hệ có thể viết cho một dịch chuyển vô cùng nhỏ dx, với năng lượng điện dE<sub>e</sub> "
        "và năng lượng trường dE<sub>f</sub> của điện trường giữa hai điện cực, là:"))
    b.append(eq("dE<sub>m</sub> + dE<sub>e</sub> = dE<sub>f</sub>", "6.40"))
    b.append(p("trong đó:"))
    b.append(eq("dE<sub>m</sub> = F(x) dx", "6.41"))
    b.append(p("Ngoài ra,"))
    b.append(eq("dE<sub>e</sub> = d(QV) = Q dV + V dQ", "6.42"))
    b.append(p(
        "Nếu giữ điện áp cấp V trên tụ không đổi thì dV = 0. Vì Q = V·C(x), lực Coulomb cho bởi:"))
    b.append(eq("F(x) = − ½ V² dC/dx", "6.43"))
    b.append(p(
        "Như vậy, nếu điện cực di động hoàn toàn tự do, nó sẽ chiếm vị trí tại đó điện dung là lớn nhất; và nếu C "
        "là hàm tuyến tính của x thì lực F(x) trở nên độc lập với x."))
    b.append(p(
        "Gia tốc kế silic kiểu điện dung có mặt trên thị trường với rất nhiều chỉ tiêu kỹ thuật. Một cảm biến nhẹ "
        "điển hình có dải tần 0 đến 1000 Hz và dải động gia tốc từ ±2 g đến ±500 g."))

    # ---------------------------------------------------------------- 6.3.4
    b.append(h2("Đo mức chất lỏng bằng điện dung", "Capacitive liquid level measurement"))
    b.append(p(
        "Mức của một chất lỏng không dẫn điện có thể xác định bằng kỹ thuật điện dung. Phương pháp nói chung dựa "
        "trên sự khác nhau giữa hằng số điện môi của chất lỏng và của khí hoặc không khí phía trên nó. Hai trụ kim "
        "loại đồng tâm được dùng làm tụ, như trên Hình 6-31. Chiều cao chất lỏng h được đo so với tổng chiều cao l. "
        "Cần có biện pháp thích hợp để bảo đảm khoảng không giữa hai điện cực trụ được chất lỏng lấp đầy tới đúng "
        "mức như phần còn lại của bồn. Điều kiện vận hành thông thường đòi hỏi khoảng cách giữa hai điện cực, "
        "s = r<sub>2</sub> − r<sub>1</sub>, phải nhỏ hơn nhiều so với bán kính điện cực trong r<sub>1</sub>. Hơn "
        "nữa, chiều cao bồn phải lớn hơn nhiều so với r<sub>2</sub>. Khi thoả các điều kiện ấy, điện dung xấp xỉ "
        "bằng:"))
    b.append(fig(31, F.fig_6_31(), "vi"))
    b.append(eq("C = 2π ε<sub>0</sub> [ ε<sub>l</sub> h + ε<sub>g</sub> (l − h) ] / ln(r<sub>2</sub>/r<sub>1</sub>)", "6.44"))
    b.append(p(
        "trong đó ε<sub>l</sub> và ε<sub>g</sub> lần lượt là hằng số điện môi của chất lỏng và của khí (hoặc không "
        "khí). Mẫu số của phương trình trên chỉ chứa các số hạng liên quan tới hệ cố định, nên chúng gộp lại thành "
        "một hằng số duy nhất. Một ứng dụng điển hình là đo lượng xăng trong bình trên máy bay. Hằng số điện môi "
        "của phần lớn các hợp chất thường có trong xăng xấp xỉ 2, còn của không khí xấp xỉ 1. Với tình huống này, "
        "kỳ vọng có sự thay đổi tuyến tính của điện dung theo mức xăng. Có thể đạt độ chính xác khá cao nếu giữ "
        "mẫu số thật nhỏ, nhờ đó làm nổi bật chênh lệch mức. Các cảm biến này thường tích hợp một cầu đo xoay "
        "chiều."))

    # ---------------------------------------------------------------- 6.3.5
    b.append(h2("Cảm biến độ ẩm và độ ẩm vật liệu", "Capacitive humidity and moisture sensors"))
    b.append(p(
        "Độ thẩm điện của không khí trong khí quyển, của một số khí và của nhiều vật liệu rắn là hàm của hàm lượng "
        "ẩm và nhiệt độ. Thiết bị đo độ ẩm kiểu điện dung dựa trên sự thay đổi độ thẩm điện của chất điện môi nằm "
        "giữa hai bản tụ. Nhược điểm chính của loại cảm biến này là chỉ cần một thay đổi tương đối nhỏ về độ ẩm "
        "đã tạo ra điện dung đủ lớn để phát hiện nhạy."))
    b.append(p(
        "Cảm biến độ ẩm điện dung có dải động rộng, từ 0,1 ppm tới điểm bão hoà. Chúng có thể làm việc trong môi "
        "trường bão hoà ẩm trong thời gian dài — một đặc tính mà nhiều cảm biến độ ẩm khác không chịu được. Khả "
        "năng làm việc chính xác và tin cậy của chúng trải trên một dải nhiệt độ và áp suất rộng. Cảm biến độ ẩm "
        "điện dung cũng có độ trễ nhỏ và độ ổn định cao, yêu cầu bảo trì tối thiểu. Những đặc điểm ấy khiến chúng "
        "khả dụng với nhiều điều kiện vận hành đặc thù và lý tưởng cho những hệ mà trong quá trình vận hành có "
        "những điều kiện không lường trước."))
    b.append(p(
        "Có nhiều loại cảm biến độ ẩm điện dung. Ở đây xin giới thiệu các loại nhôm, tantali, silic và polymer."))

    b.append(h3("Cảm biến độ ẩm điện dung kiểu nhôm", "Aluminium-oxide type"))
    b.append(p(
        "Phần lớn cảm biến độ ẩm điện dung là loại ôxít nhôm. Ở loại này, nhôm có độ tinh khiết cao được ôxy hoá "
        "bằng phương pháp hoá học để tạo một lớp cách điện đã được nạp sẵn, gồm ôxít nhôm ngậm nước một phần, "
        "đóng vai trò chất điện môi. Một màng vàng dẫn điện nhưng thấm nước được lắng lên lớp ôxít, thường bằng "
        "phương pháp lắng đọng chân không, tạo thành điện cực thứ hai của tụ."))
    b.append(p(
        "Ở một loại khác, cảm biến nhôm – ôxít nhôm có cấu trúc lỗ như trên Hình 6-32. Lớp ôxít với cấu trúc lỗ "
        "của nó tạo thành vật liệu cảm nhận tích cực. Hơi ẩm trong không khí tới được các lỗ sẽ làm giảm điện trở "
        "và tăng điện dung. Có thể hiểu sự giảm điện trở là do tăng độ dẫn qua lớp ôxít. Có thể hiểu sự tăng điện "
        "dung là do tăng hằng số điện môi. Đại lượng được đo có thể là điện trở, điện dung hoặc tổng trở. Ở độ ẩm "
        "cao nên đo bằng điện dung, vì trong vùng này sự thay đổi điện trở là rất nhỏ, gần như triệt tiêu."))
    b.append(fig(32, F.fig_6_32(), "vi"))
    b.append(p(
        "Ngoài kiểu kết cấu đầu đo minh hoạ ở đây, còn có nhiều kiểu khác với một số cải biến đáng kể cho những "
        "tính chất riêng — chẳng hạn tăng độ nhạy hay đáp ứng nhanh hơn. Tuy phần lớn các cải biến ấy dẫn tới thay "
        "đổi kích thước hình học hoặc hình thức bên ngoài, vật liệu cảm nhận của đầu đo — ôxít nhôm — vẫn giữ "
        "nguyên."))
    b.append(p(
        "Ở một số phiên bản, lớp ôxít được tạo thành từ những lỗ hình ống song song, xếp theo mạng lục giác và "
        "vuông góc với mặt phẳng của lớp đế. Các lỗ này dừng lại ngay trước lớp nhôm, tạo thành một đáy lỗ rất "
        "mỏng. Nước hấp thụ trong các ống ấy liên hệ trực tiếp với hàm lượng ẩm của khí tiếp xúc với chúng. Bản "
        "chất xốp của lớp ôxít tạo diện tích lớn cho việc hấp thụ hơi nước. Ở độ ẩm thấp, điện dung hoàn toàn do "
        "chất điện môi hỗn hợp hình thành giữa ôxít, hơi nước và không khí. Tuy vậy, ở độ ẩm cao hơn, những đường "
        "dẫn song song qua lượng nước đã hấp thụ được hình thành dọc theo bề mặt lỗ. Gần điểm bão hoà, điện trở "
        "bề mặt lỗ này trở nên không đáng kể, nghĩa là điện dung đo được thực chất là điện dung giữa đáy lỗ rất "
        "mỏng và lõi nhôm."))

    b.append(h3("Cảm biến độ ẩm điện dung kiểu tantali", "Tantalum type"))
    b.append(p(
        "Ở một số phiên bản cảm biến độ ẩm điện dung, một trong hai bản cực gồm một lớp tantali lắng trên đế thuỷ "
        "tinh. Sau đó thêm một lớp điện môi polymer, rồi tới bản cực thứ hai làm bằng một lớp crôm mỏng. Lớp crôm "
        "chịu ứng suất kéo lớn đến mức nứt thành cấu trúc khảm mịn, cho phép các phân tử nước đi vào chất điện "
        "môi. Ứng suất trong crôm cũng làm polymer nứt thành cấu trúc khảm. Một cảm biến loại này có dải đầu vào "
        "0 % đến 100 % độ ẩm tương đối (RH). Điện dung là 375 pF tại 0 % RH và độ nhạy tuyến tính 1,7 pF cho mỗi "
        "% RH. Sai số thường nhỏ hơn 2 % do phi tuyến và 1 % do độ trễ."))

    b.append(h3("Cảm biến độ ẩm điện dung kiểu silic", "Silicon type"))
    b.append(p(
        "Ở những cảm biến độ ẩm điện dung khác, silic được dùng làm chất điện môi. Kết cấu và nguyên lý làm việc "
        "của cảm biến độ ẩm silic rất giống loại ôxít nhôm. Một số cảm biến kiểu silic cũng dùng đế nhôm và một "
        "lớp vàng màng mỏng làm hai điện cực. Chất điện môi silic có diện tích bề mặt rất lớn, nghĩa là độ nhạy "
        "vẫn tương đối lớn ngay cả khi diện tích cảm nhận rất nhỏ. Đây là đặc điểm quan trọng trong xu thế thu nhỏ "
        "thiết bị ngày càng tăng. Cả hai loại cảm biến nay thường gặp dưới dạng phần tử hình tấm rất nhỏ, đặt trên "
        "một giá cơ khí có dây dẫn nối ra. Việc tạo silic xốp là một quá trình anốt hoá rất đơn giản và, vì không "
        "cần thiết bị phức tạp, thiết bị có thể chế tạo với giá thành tương đối thấp. Ngoài ra, bằng cách điều "
        "khiển các điều kiện tạo thành, có thể dễ dàng sửa đổi cấu trúc silic xốp để thiết bị phù hợp với từng "
        "ứng dụng cụ thể."))
    b.append(p(
        "Ở cả hai loại cảm biến độ ẩm điện dung silic và ôxít nhôm, bán kính các lỗ trong chất điện môi được chọn "
        "sao cho phù hợp riêng với phân tử nước. Phần lớn các chất nhiễm bẩn tiềm tàng đều quá lớn để làm bẩn chất "
        "điện môi. Tuy vậy, chất nhiễm bẩn có thể chặn dòng hơi nước đi vào vật liệu cảm biến, do đó ảnh hưởng tới "
        "độ chính xác của thiết bị. Ví dụ, trong những dòng khí nhiễm bụi, có thể bố trí một rào cản vật lý đơn "
        "giản như nắp thiêu kết bằng kim loại hoặc bằng nhựa cho đầu cảm biến. Nhiều cảm biến được cung cấp kèm "
        "một dạng vỏ bảo vệ nào đó."))

    b.append(h3("Cảm biến độ ẩm điện dung kiểu polymer", "Polymer type"))
    b.append(p(
        "Ở một số cảm biến, chất điện môi là vật liệu polymer có khả năng hấp thụ phân tử nước. Việc hấp thụ hơi "
        "nước của vật liệu làm thay đổi hằng số điện môi của tụ. Với thiết kế cẩn thận, có thể làm cho điện dung "
        "tỉ lệ trực tiếp với phần trăm độ ẩm tương đối của khí hoặc khí quyển xung quanh."))
    b.append(p(
        "Nói chung, một đặc điểm then chốt quan trọng của cảm biến độ ẩm điện dung là độ ổn định hoá học. Thường "
        "phải đo độ ẩm trong một mẫu không khí có chứa hơi nhiễm bẩn (ví dụ cacbon mônôxít), hoặc phép đo được "
        "thực hiện trên một mẫu khí khác không khí (ví dụ benzen đã hoá hơi). Hiệu năng của các cảm biến này, đặc "
        "biệt là loại silic, không bị nhiều loại khí ấy ảnh hưởng. Hydrocacbon, cacbon đioxit, cacbon mônôxít và "
        "các CFC không gây nhiễu. Tuy vậy, bản chất ion của chất điện môi ôxít nhôm khiến nó nhạy với một số khí "
        "phân cực mạnh và ăn mòn như amôniắc, lưu huỳnh triôxít và clo. Silic là vật liệu trơ; tính chất ổn định "
        "của nó khiến các khí phân cực ấy chỉ ảnh hưởng tới phần tử cảm biến ở mức độ nhỏ hơn nhiều."))

    b.append(h3("Cảm biến độ ẩm vật liệu dạng hạt", "Capacitive moisture sensors"))
    b.append(p(
        "Phép đo độ ẩm bằng điện dung dựa trên sự thay đổi độ thẩm điện của các vật liệu điện môi dạng hạt hoặc "
        "dạng bột như lúa mì và các loại ngũ cốc có chứa nước. Thông thường cảm biến gồm một buồng trụ lớn (ví dụ "
        "sâu 150 mm và đường kính 100 mm), như trên Hình 6-33. Buồng được nạp đầy mẫu cần thử. Sự biến thiên điện "
        "dung theo hàm lượng nước được xử lý. Tụ được ghép vào một mạch dao động làm việc ở tần số thích hợp."))
    b.append(fig(33, F.fig_6_33(), "vi"))
    b.append(p(
        "Cảm biến độ ẩm điện dung phải được hiệu chuẩn cho từng loại vật liệu, vì bản thân các vật liệu có độ thẩm "
        "điện khác nhau. Cần nhiệt độ chính xác vì hằng số điện môi có thể phụ thuộc mạnh vào nhiệt độ. Phần lớn "
        "các thiết bị này được chế tạo để làm việc trong dải nhiệt độ 0 °C đến 50 °C, có các mạch bù nhiệt chặt "
        "chẽ hỗ trợ. Sau khi đã hiệu chuẩn cho một ứng dụng cụ thể, chúng phù hợp để đo độ ẩm trong dải 0 % đến "
        "40 %."))

    # ---------------------------------------------------------------- 6.3.6
    b.append(h2("Xử lý tín hiệu", "Signal processing"))
    b.append(p(
        "Nói chung, đầu thu kiểu điện dung đòi hỏi mạch điện tương đối phức tạp so với nhiều loại cảm biến khác, "
        "nhưng bù lại chúng có ưu điểm là đơn giản về cơ khí. Chúng cũng nhạy, với hiệu ứng tải cơ khí tối thiểu. "
        "Về xử lý tín hiệu, các cảm biến này thường được ghép vào mạch cầu xoay chiều hoặc mạch dao động. Trên "
        "thực tế, cảm biến điện dung không phải là điện dung thuần mà có kèm điện trở biểu diễn tổn hao trong chất "
        "điện môi. Điều này có thể ảnh hưởng quan trọng tới thiết kế mạch, đặc biệt với mạch dao động. Dưới đây "
        "trình bày một số mạch xử lý tín hiệu."))

    b.append(h3("Khuếch đại thuật toán và khuếch đại điện tích",
                "Operational amplifiers and charge amplifiers"))
    b.append(p(
        "Một cách khử tính phi tuyến của quan hệ giữa biến vật lý (ví dụ cảm biến hai bản dịch chuyển) và điện "
        "dung C là dùng khuếch đại thuật toán, như trên Hình 6-34. Trong mạch này, nếu trở kháng vào của khuếch "
        "đại thuật toán lớn, đầu ra không bị bão hoà và điện áp vào nhỏ, thì có thể viết:"))
    b.append(fig(34, F.fig_6_34(), "vi"))
    b.append(eq("(1/C<sub>f</sub>) ∫ i<sub>f</sub> dt = e<sub>ex</sub> − e<sub>ai</sub>", "6.45"))
    b.append(eq("(1/C<sub>x</sub>) ∫ i<sub>x</sub> dt = e<sub>ai</sub> − 0 = 0", "6.46"))
    b.append(eq("i<sub>f</sub> + i<sub>x</sub> = 0", "6.47"))
    b.append(p("Biến đổi các phương trình này thu được:"))
    b.append(eq("e<sub>0</sub> = − (C<sub>x</sub>/C<sub>f</sub>) e<sub>ex</sub>", "6.48"))
    b.append(p("Thay giá trị của C<sub>x</sub> vào:"))
    b.append(eq("e<sub>0</sub> = − (ε<sub>r</sub> ε<sub>0</sub> A / (C<sub>f</sub> x)) e<sub>ex</sub>", "6.49"))
    b.append(note(
        "Ghi chú của người dịch. Nguyên văn ở đây viết rằng phương trình 6.49 cho thấy “điện áp ra tỉ lệ trực "
        "tiếp với khoảng cách bản x”, và do đó “tuyến tính với mọi biến thiên chuyển động”. Điều ấy chỉ đúng với "
        "cảm biến biến thiên diện tích, nơi C<sub>x</sub> tỉ lệ thuận với x. Với cảm biến biến thiên khoảng cách "
        "như chính phương trình 6.49 viết, đầu ra tỉ lệ nghịch với x, tức là vẫn giữ dạng hyperbolic của phương "
        "trình 6.23. Giá trị đúng đắn của mạch khuếch đại điện tích là ở chỗ nó làm đầu ra tuyến tính theo điện "
        "dung C<sub>x</sub>, chứ không phải theo khoảng cách."))
    b.append(p(
        "Tuy vậy, một mạch thực tế cần có một điện trở song song với C<sub>f</sub> để hạn chế độ trôi đầu ra. Trị "
        "số điện trở này phải lớn hơn trở kháng của C<sub>f</sub> tại tần số thấp nhất mà ta quan tâm. Ngoài ra, "
        "vì trở kháng của đầu đo được giả định là thuần điện dung, độ lợi hiệu dụng không phụ thuộc tần số. Một "
        "mạch khuếch đại điện tích thực dụng được mô tả trên Hình 6-35. Trong trường hợp này, điện trở hồi tiếp "
        "hiệu dụng R<sub>ef</sub> cho bởi:"))
    b.append(fig(35, F.fig_6_35(), "vi"))
    b.append(eq("R<sub>ef</sub> = R<sub>3</sub> + R<sub>1</sub>R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>)", "6.50"))
    b.append(p(
        "Có thể giảm đáng kể độ trôi đầu ra bằng cách chọn các điện trở thích hợp. Độ chính xác của mạch này còn "
        "có thể nâng cao bằng cách ghép tầng hai hay nhiều khuếch đại. Bằng cách ấy cũng đạt được cải thiện đáng "
        "kể về tỉ số tín hiệu trên tạp âm. Ở lối vào đảo, việc dùng điện trở R<sub>4</sub> là cần thiết vì dòng "
        "phân cực."))

    b.append(h3("Điều chế độ rộng xung", "Pulse width modulation"))
    b.append(p(
        "Như trường hợp một số cảm biến dịch chuyển rung động kiểu điện dung, đầu ra của cảm biến có thể là một "
        "sóng điều biên như trên Hình 6-36. Sau khi chỉnh lưu, giá trị trung bình của sóng này cho khoảng cách "
        "trung bình giữa hai bản. Biên độ rung động quanh vị trí trung bình ấy có thể tách ra bằng một bộ tách "
        "sóng và một mạch lọc thông thấp. Đầu ra của mạch lọc thông thấp là chỉ thị trực tiếp của rung động, và "
        "dạng sóng có thể quan sát trên dao động ký."))
    b.append(fig(36, F.fig_6_36(), "vi"))
    b.append(note(
        "Ghi chú của người dịch. Tiêu đề mục này trong nguyên bản là “Pulse Width Modulation”, nhưng nội dung bên "
        "dưới lại mô tả điều biên và Hình 6-36. Kỹ thuật điều chế độ rộng xung thực sự được trình bày ở mục kế "
        "tiếp, “Tuyến tính hoá xung vuông”. Tiêu đề được giữ nguyên để bản dịch khớp với bản gốc."))

    b.append(h3("Tuyến tính hoá xung vuông", "Square wave linearization"))
    b.append(p(
        "Một kỹ thuật tuyến tính hoá khác, được áp dụng cho đầu đo áp suất điện dung và gia tốc kế, là điều chế độ "
        "rộng xung. Đầu đo gồm hai tụ vi sai như trên Hình 6-37. Điện áp trên hai tụ, e<sub>1</sub> và "
        "e<sub>2</sub>, đảo qua đảo lại với tần số kích thích cao (ví dụ 400 kHz) giữa mức điện áp kích thích và "
        "đất. Hệ được bố trí sao cho điện áp ra là hiệu trung bình của e<sub>1</sub> và e<sub>2</sub>. Tại vị trí "
        "không, e<sub>1</sub> = e<sub>2</sub>, đầu ra là một sóng vuông đối xứng có giá trị trung bình bằng không. "
        "Khi vị trí tương đối của các bản thay đổi do rung động, giá trị trung bình của điện áp ra lệch khỏi không "
        "và trở nên dương hoặc âm tuỳ theo chiều dịch chuyển. Do đó, điện áp ra viết được là:"))
    b.append(fig(37, F.fig_6_37(), "vi"))
    b.append(eq("e<sub>0</sub> = − e<sub>ex</sub> (C<sub>1</sub> − C<sub>2</sub>) / (C<sub>1</sub> + C<sub>2</sub>)", "6.51"))
    b.append(p("Thay:"))
    b.append(eq("C<sub>1</sub> = C<sub>0</sub>(1 − x<sub>i</sub>/x<sub>0</sub>) &nbsp; và &nbsp; "
                "C<sub>2</sub> = C<sub>0</sub>(1 + x<sub>i</sub>/x<sub>0</sub>)", ""))
    b.append(p("thu được"))
    b.append(eq("e<sub>0</sub> = − e<sub>ex</sub> · x<sub>i</sub>/x<sub>0</sub>", "6.52"))
    b.append(p("Như vậy đầu ra tỉ lệ trực tiếp với biến x<sub>i</sub>."))

    b.append(h3("Tuyến tính hoá bằng hồi tiếp", "Feedback linearization"))
    b.append(p(
        "Cũng có thể tuyến tính hoá một đầu đo điện dung bằng một hệ hồi tiếp điều chỉnh biên độ dòng điện tụ sao "
        "cho dòng ấy giữ không đổi ở một giá trị chuẩn với mọi dịch chuyển. Việc này được thực hiện bằng cách lấy "
        "từ bộ tách sóng một tín hiệu một chiều tỉ lệ với dòng điện tụ, so sánh dòng này với dòng chuẩn, rồi điều "
        "chỉnh biên độ điện áp của bộ dao động kích thích cho tới khi hai dòng bằng nhau. Nếu dòng điện tụ được "
        "giữ không đổi bất kể chuyển động của tụ, thì biên độ điện áp liên hệ tuyến tính với x theo:"))
    b.append(eq("e = K x<sub>i</sub>", "6.53"))
    b.append(p("trong đó"))
    b.append(eq("K = i<sub>c</sub> / (ω<sub>0</sub> C<sub>0</sub>)", "6.54"))

    b.append(h3("Mạch dao động", "Oscillator circuits"))
    b.append(p(
        "Trong nhiều ứng dụng, có thể đo sự thay đổi điện dung của đầu đo điện dung bằng một cầu xoay chiều thích "
        "hợp như cầu Wien hay cầu Schering. Tuy vậy, trong phần lớn trường hợp, người ta dùng những phiên bản cải "
        "biến của cầu đo làm mạch dao động để xử lý tín hiệu điện dung. Đầu đo được đấu thành một phần của mạch "
        "dao động, làm thay đổi tần số dao động. Sự thay đổi tần số này được chia thang để trở thành thước đo độ "
        "lớn của biến vật lý."))
    b.append(p(
        "Là một phần của mạch dao động, đầu đo điện dung có đáp ứng tần số tuyệt vời và có thể đo cả hiện tượng "
        "tĩnh lẫn động. Nhược điểm của nó gồm độ nhạy với biến thiên nhiệt độ và khả năng xuất hiện tín hiệu thất "
        "thường hoặc méo dạng do chiều dài dây dẫn lớn. Ngoài ra, thiết bị thu nhận có thể cồng kềnh và phức tạp, "
        "và thường bao gồm một bộ dao động tần số cố định thứ hai để trộn tần. Tần số hiệu tạo ra theo cách ấy có "
        "thể đọc bằng một thiết bị ra thích hợp như máy đếm điện tử."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. P. Bentley, <i>Principles of Measurement Systems</i>, 2nd ed., United Kingdom: Longman Scientific "
        "and Technical, 1988.",
        "E. O. Doebelin, <i>Measurement Systems: Application and Design</i>, 4th ed., New York: McGraw-Hill, 1990.",
        "J. P. Holman, <i>Experimental Methods for Engineers</i>, 5th ed., New York: McGraw-Hill, 1989.",
        "F. T. Noth and G. C. M. Meijer, “A Low-Cost, Smart Capacitive Position Sensor,” <i>IEEE Trans. Instrum. "
        "Meas.</i>, 41, 1041–1044, 1992.",
    ]))

    b.append(h2("Phụ lục mục 6.3 — Danh sách nhà sản xuất",
                "Appendix to Section 6.3 — List of manufacturers"))
    b.append(table(
        ["Nhà sản xuất", "Địa chỉ", "Liên hệ"],
        [
            ["ANALITE Inc.", "24-T Newtown Plaza, Plainview, NY 11803", "Tel: (800) 229-3357"],
            ["FSI/FORK Standards Inc.", "668 Western Avenue, Lombard, IL 60148-2097", "Tel: (708) 932-9380"],
            ["Gordon Engineering Corp.", "67 Del Mar Drive, Brookfield, CT 06804", "Tel: (203) 775-4501"],
            ["Hecon Corp.", "15-T Meridian Rd., Eatontown, NJ 07724", "Tel: (800) 524-1669"],
            ["Kistler Instrumentation Corp.", "Amherst, NY 14228-2171",
             "Tel: (716) 691-5100 · Fax: (716) 691-5226"],
            ["Locon Sensor Systems, Inc.", "1750 S. Eber Road, P.O. Box 789, Holland, OH 43526",
             "Tel: (419) 865-7651 · Fax: (419) 865-7756"],
            ["Rechner Electronic Industries Inc.", "8651 Buffalo Avenue, Box 7, Niagara Falls, NY 14304",
             "Tel: (800) 544-4106"],
            ["RDP Electrosense, Inc.", "2216-Dept. B, Pottstown, PA", "Tel: (800) 334-5838"],
        ],
        caption="Danh sách nguyên văn theo bản gốc năm 1999; thông tin liên hệ có thể đã thay đổi."))
    b.append(nav(3, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Section 6.3 is the capacitive counterpart to the resistive and inductive families of 6.1 and 6.2. It "
        "covers three sensing geometries — variable gap, variable area, variable dielectric — plus the "
        "differential three-terminal arrangement that removes most of the gap sensor’s hyperbolic "
        "nonlinearity, and then a long tail of applications that reuse the same physics: pressure, "
        "acceleration, level, humidity, grain moisture."))
    b.append(p(
        "What makes the section worth reading closely is that the same equation, C = εA/d, gives a linear "
        "sensor or a hopeless one depending entirely on which of the three quantities moves. Move the area and "
        "you get linearity for free. Move the gap and you get a hyperbola that has to be linearised "
        "electronically — and every one of the circuits in the last part of the section exists to do exactly "
        "that."))

    b.append(h2("The three geometries", "Ba kết cấu cơ bản"))
    b.append(table(
        ["Geometry", "Capacitance", "Response in x", "Where it is used"],
        [
            ["Variable gap", "C = ε<sub>r</sub>ε<sub>0</sub>A/x", "Hyperbolic, C ∝ 1/x",
             "Non-contacting measurement of small increments; proximity probes"],
            ["Variable area", "C = ε<sub>r</sub>ε<sub>0</sub>(A − wx)/d", "Linear",
             "Rotating capacitors for angle; capacitive voltmeters"],
            ["Variable dielectric", "C = ε<sub>0</sub>w[ε<sub>2</sub>(l−x) + ε<sub>1</sub>x]/d", "Linear",
             "Concentric cylinders for tank level"],
            ["Differential", "δC/C = δd/d", "Linear to first order",
             "Three-terminal cells; differential pressure capsules"],
        ],
        caption="Table 6.2a — Which quantity moves decides whether the sensor is linear."))
    b.append(fig(23, F.fig_6_23(), "en"))
    b.append(p(
        "The differential arrangement deserves the emphasis the section gives it. By taking the difference of "
        "two gaps that move in opposition, the 1/(d − δd) and 1/(d + δd) terms expand into a ratio in which the "
        "leading nonlinearity cancels: δC/C = δd/d exactly to first order. The range is twice the nominal "
        "separation, the output is zero at the centre, and the sign of the displacement appears as a 180° phase "
        "reversal — which is why a phase-sensitive demodulator, not a rectifier, is the right detector."))
    b.append(fig(26, F.fig_6_26(), "en"))

    b.append(h2("The numbers worth remembering", "Những con số cần nhớ"))
    b.append(ul([
        "<b>Smart capacitive position sensor</b> (Fig. 6.27): 1 µm accuracy over a 1 mm range, total measuring "
        "time better than 0.1 s, capacitance range 1 pF down to 50 fF. The guard ring has to keep the relative "
        "deviation below 100 ppm, which is what the two exponential criteria (6.31) and (6.32) enforce.",
        "<b>Capacitive accelerometers</b>: 0–1000 Hz bandwidth, ±2 g to ±500 g dynamic range for a typical "
        "lightweight part.",
        "<b>Tantalum humidity sensor</b>: 375 pF at 0 % RH, 1.7 pF per % RH, error under 2 % from nonlinearity "
        "and 1 % from hysteresis over 0–100 % RH.",
        "<b>Grain moisture</b>: chamber roughly 150 mm deep by 100 mm diameter, operated 0–50 °C with tight "
        "temperature compensation, calibrated per material, useful over 0–40 % moisture.",
        "<b>Gasoline level</b>: ε<sub>r</sub> ≈ 2 for the hydrocarbons in gasoline against ≈ 1 for air, which "
        "is what makes a linear capacitance-versus-level reading possible in an aircraft tank.",
    ]))
    b.append(fig(27, F.fig_6_27(), "en"))

    b.append(h2("Why the signal conditioning is the hard part",
                "Vì sao phần xử lý tín hiệu mới là chỗ khó"))
    b.append(p(
        "A capacitive sensor is mechanically trivial — two plates and a gap — and electrically awkward. The "
        "capacitances are picofarads or less, comparable with cable capacitance; the sensor is not a pure "
        "capacitance but carries a loss resistance through the dielectric; and at the low end the impedance is "
        "so high that stray pickup dominates. The section’s four techniques are four different answers to that:"))
    b.append(ul([
        "The <b>charge amplifier</b> holds the inverting input at virtual ground, so cable capacitance is "
        "bootstrapped out and the output becomes proportional to C<sub>x</sub> rather than to the voltage "
        "across it.",
        "<b>Amplitude demodulation</b> recovers the mean gap from a modulated carrier, then a low-pass filter "
        "recovers the vibration about that mean.",
        "<b>Square-wave linearisation</b> drives two differential capacitors with antiphase square waves and "
        "averages the difference, which converts the ratio (C₁ − C₂)/(C₁ + C₂) directly into a signed dc level.",
        "<b>Feedback linearisation</b> servos the excitation amplitude until the capacitor current is constant, "
        "making the voltage amplitude linear in x.",
    ]))
    b.append(fig(34, F.fig_6_34(), "en"))
    b.append(p(
        "Only the first of these four is a true lineariser of the gap sensor; the others linearise something "
        "else and are worth keeping straight. The charge amplifier makes e₀ proportional to C<sub>x</sub>. The "
        "square-wave circuit makes e₀ proportional to the normalised difference (C₁ − C₂)/(C₁ + C₂), which is "
        "the quantity the differential geometry already made linear in δd. The feedback loop makes e₀ "
        "proportional to x by holding the current constant, so the nonlinearity is absorbed into the excitation "
        "amplitude instead of the output."))
    b.append(fig(37, F.fig_6_37(), "en"))
    b.append(note(
        "Translator’s note. The source’s claim that equation 6.49 makes the output “directly proportional to "
        "the plate separation x” holds only for the variable-area geometry, where C<sub>x</sub> ∝ x. For the "
        "variable-gap sensor the same equation gives e₀ ∝ 1/x, still hyperbolic. The genuine contribution of "
        "the charge amplifier is linearity in C<sub>x</sub>, not in x. The heading “Pulse Width Modulation” in "
        "the source also precedes a passage on amplitude modulation; the real PWM material is under “Square "
        "wave linearization”."))

    b.append(h2("Where the physics is reused", "Vật lý ấy được dùng lại ở đâu"))
    b.append(p(
        "Pressure, acceleration, level and humidity are all the same capacitor with a different thing moving. "
        "In the pressure sensor the diaphragm is one plate and its centre deflection goes as (a² − r²)², so the "
        "mean deflection — and hence ∆C/C — is one third of the centre value. In the accelerometer the proof "
        "mass is the plate and the Coulomb force F = −½V²dC/dx is what pulls it; with a constant supply the "
        "force is independent of x when C is linear in x, which is why the electrode shape is chosen to make it "
        "so. In the level sensor the dielectric boundary moves; in the humidity sensor the dielectric absorbs "
        "water and changes its permittivity."))
    b.append(fig(28, F.fig_6_28(), "en"))
    b.append(fig(30, F.fig_6_30(), "en"))
    b.append(fig(31, F.fig_6_31(), "en"))
    b.append(fig(32, F.fig_6_32(), "en"))
    b.append(p(
        "The humidity variants are a study in materials rather than circuits. Aluminium oxide is an ionic "
        "dielectric: sensitive, cheap, and vulnerable to ammonia, sulphur trioxide and chlorine. Porous silicon "
        "is inert and can be anodised cheaply, and its pore size can be tuned so contaminants are too large to "
        "enter. Tantalum with a cracked chromium overlayer gets the water in through the cracks. All three rely "
        "on the same trick — pores sized for a water molecule — and all three fail the same way when dust "
        "blocks the pores, which is why sintered metal or plastic hoods appear in the practical advice."))

    b.append(h2("Reading the appendix", "Đọc phần phụ lục"))
    b.append(p(
        "The manufacturer list is reproduced verbatim from the 1999 edition. Treat the telephone numbers as "
        "historical: the useful information is the shape of the market — small specialist firms making "
        "proximity probes and capacitance bridges, not the large instrument houses."))
    b.append(nav(3, "en"))
    return "".join(b)
