# -*- coding: utf-8 -*-
"""Handbook 6.12 — Optical Beam Deflection Sensing (Grover C. Wetsel)."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Việc đo cường độ ánh sáng phản xạ và truyền qua một mẫu đã là nguồn thông tin về cấu trúc vật chất trong "
        "hơn một thế kỷ. Trong những thập kỷ gần đây, người ta nhận ra rằng việc đo <i>vị trí</i> của một chùm sáng "
        "đã tán xạ từ một mẫu lại là một phương tiện quan trọng và linh hoạt để đặc trưng hoá vật liệu và chuyển "
        "động của các thiết bị. Sự sẵn có của một chùm sáng được chuẩn trực tốt từ laser chắc chắn là yếu tố then "
        "chốt trong sự phát triển các kỹ thuật và ứng dụng cảm biến lệch chùm tia quang (OBD); tuy nhiên, sự phát "
        "triển và tính sẵn có của nhiều loại đầu dò cảm nhận vị trí (PSD) cũng là những yếu tố quan trọng không "
        "kém. Độ lệch chùm tia quang có thể do chùm laser lan truyền qua một gradient chiết suất gây ra, hoặc do "
        "phản xạ từ một bề mặt bị dịch chuyển. Một PSD cung cấp tín hiệu điện là hàm của vị trí chùm laser trên đầu "
        "dò."))
    b.append(p(
        "Trong mục này, các ứng dụng của cảm biến lệch chùm tia quang được điểm lại, lý thuyết hoạt động của ba loại "
        "cảm biến OBD thông dụng nhất được triển khai, và những đặc tính vận hành điển hình của các thiết bị được "
        "trình bày. Ưu nhược điểm của các PSD khác nhau cũng được thảo luận."))

    b.append(fig(113, F.fig_6_113()))
    b.append(p(
        "Sơ đồ của cấu hình cảm biến OBD cơ bản được minh hoạ trên Hình 6-113. Trong trường hợp này, dịch chuyển u "
        "của bề mặt làm vị trí của chùm phản xạ trên PSD chuyển từ điểm P sang điểm P′; sự thay đổi vị trí này tạo "
        "ra một thay đổi điện áp đầu ra của PSD. Điện áp ra V của phần điện tử PSD có thể được hiệu chuẩn theo dịch "
        "chuyển thực u bằng cách đo V theo u với những dịch chuyển đã biết."))
    b.append(p(
        "Cảm biến OBD đã được dùng trong nhiều ứng dụng khác nhau, bao gồm quang phổ lệch chùm tia quang quang "
        "nhiệt (PTOBD) [1], đo tuyệt đối suy giảm quang [2], tạo ảnh PTOBD cấu trúc bề mặt và dưới bề mặt [3], "
        "quang phổ dịch chuyển quang nhiệt [4], hiển vi lực nguyên tử [5], và đặc trưng hoá vật liệu [6]. Phương "
        "pháp này cũng đã được dùng như một cách đo chuyển động bề mặt đơn giản, nhạy và chính xác cho các bộ biến "
        "đổi quét của kính hiển vi quét xuyên hầm [7] và cho tạo ảnh bằng đầu dò siêu âm [8]."))

    # --------------------------------------------------------------- Theory
    b.append(h2("Lý thuyết", "Theory"))
    b.append(p(
        "Ba loại thiết bị cơ bản dùng cho cảm biến OBD là: (1) một photodetector đặt sau một màn chắn có mép sắc "
        "(lưỡi dao); (2) một mảng nhỏ các photodetector được ngăn cách bởi những vùng không nhạy tương đối hẹp "
        "(hai ô, bốn ô); và (3) một cảm biến vị trí bán dẫn liên tục (một hoặc hai chiều). Đặc tính cảm nhận của "
        "một thiết bị được quyết định bởi tác động của dịch chuyển chùm sáng lên phân bố công suất trên "
        "photodetector. Vì chùm laser thường được dùng trong cảm biến OBD, phần phân tích dựa trên giả thiết rằng "
        "phân bố không gian của cường độ (I) trong mặt phẳng vuông góc với phương lan truyền có tính đối xứng trục "
        "với biến thiên xuyên tâm dạng Gauss."))

    # ------------------------------------------------------------ Knife edge
    b.append(h3("Đầu dò quang sau lưỡi dao", "Knife-edge photodetector"))
    b.append(p(
        "Những nét cơ bản của một PSD được thể hiện bằng một photodetector bị che bởi một lưỡi dao nửa vô hạn, "
        "y &lt; 0, như trên Hình 6-114. Như có thể dự đoán từ tính đối xứng của bố trí và được chứng minh bằng toán "
        "học, độ nhạy lệch đạt cực đại khi chùm chưa lệch nằm đúng tâm trên mép lưỡi dao. Trong hệ quy chiếu của "
        "chùm đã bị dịch chuyển, cường độ ánh sáng tới được photodetector do dịch chuyển (u) của tâm chùm được cho "
        "bởi:"))
    b.append(fig(114, F.fig_6_114()))
    b.append(eq("I(r′) = (aP / π) · e<sup>−ar′²</sup>", "6.126"))
    b.append(p(
        "trong đó P là tổng công suất chùm tới, a = 2/r₁², r₁ là bán kính chùm Gauss, và r′² = x′² + y′². Theo các "
        "toạ độ (x, y) của chùm chưa lệch, toạ độ vuông góc của chùm đã lệch là x′ = x và y′ = y − u. Công suất "
        "P<sub>d</sub> trên đầu dò do đó được cho bởi:"))
    b.append(eq("P<sub>d</sub> = (P / 2) · [1 + erf (u / r₁)]", "6.127"))
    b.append(p(
        "trong đó erf là hàm sai số. Chỉ cần nhìn vào phương trình 6.127 cũng thấy rằng những đặc tính cốt lõi của "
        "cảm biến vị trí này được quyết định bởi tỉ số u/r₁. Đáp ứng chuẩn hoá P<sub>d</sub>/P được vẽ trên Hình "
        "6-115 theo u/r₁. Khi u = r₁ thì P<sub>d</sub> = 97,7% P."))
    b.append(fig(115, F.fig_6_115()))
    b.append(p("Độ nhạy lệch được cho bởi độ dốc của phương trình 6.127:"))
    b.append(eq("dP<sub>d</sub> / du = (P / (r₁√π)) · e<sup>−(u/r₁)²</sup>", "6.128"))
    b.append(p("Định nghĩa độ nhạy của cảm biến vị trí ở chế độ tín hiệu nhỏ (đơn vị m⁻¹):"))
    b.append(eq("α<sub>KE</sub> ≡ (1/P) · (dP<sub>d</sub>/du)|<sub>u = 0</sub> = 1 / (r₁√π)", "6.129"))
    b.append(p(
        "Khi đó công suất quang tới được photodetector với tín hiệu nhỏ là:"))
    b.append(eq("P<sub>d</sub> ≅ P/2 + α<sub>KE</sub> P u = P [1/2 + α<sub>KE</sub> u]", "6.130"))
    b.append(p(
        "Tín hiệu của photodetector sẽ tuyến tính theo dịch chuyển nếu u ≤ 0,387 r₁. Dòng quang điện là:"))
    b.append(eq("I = K P<sub>d</sub> ≅ K P [1/2 + α<sub>KE</sub> u]", "6.131"))
    b.append(p(
        "trong đó K là độ nhạy của photodetector, tính bằng A/W. Điện áp của cảm biến vị trí thu được nhờ một bộ "
        "khuếch đại trở kháng truyền có hệ số khuếch đại Z:"))
    b.append(eq("V = K Z P<sub>d</sub> ≅ K Z P [1/2 + α<sub>KE</sub> u]", "6.132"))
    b.append(note(
        "<b>Về con số 0,387.</b> Hệ số này không phải một hằng số hình học mà là kết quả của một tiêu chí sai số. "
        "Nếu lấy khai triển tuyến tính ở phương trình 6.130 và so với nghiệm chính xác 6.127, độ lệch tương đối "
        "đạt khoảng 1,5% tại u = 0,387 r₁ — tức là người ta chọn điểm mà tại đó phép xấp xỉ tuyến tính bắt đầu "
        "sai đáng kể. Muốn dải tuyến tính rộng hơn thì phải chấp nhận sai số lớn hơn, hoặc phải hiệu chuẩn theo "
        "đường cong nghịch đảo của hàm erf."))

    # ---------------------------------------------------------------- Bicell
    b.append(h3("Đầu dò hai ô", "Bicell detector"))
    b.append(p(
        "Độ lệch của một chùm Gauss ban đầu nằm đúng tâm trong khe không nhạy của một đầu dò hai ô được minh hoạ "
        "trên Hình 6-116. Công suất tới nửa trên của đầu dò hai ô được cho bởi:"))
    b.append(fig(116, F.fig_6_116()))
    b.append(eq("P₂ = (P / 2) · [1 − erf ((y₁ − u) / r₁)]", "6.133"))
    b.append(p("Công suất tới nửa dưới của đầu dò hai ô được cho bởi:"))
    b.append(eq("P₁ = (P / 2) · [1 − erf ((y₂ + u) / r₁)]", "6.134"))
    b.append(p(
        "Dòng quang điện từ mỗi đầu dò của bicell được biến đổi thành điện áp bằng những bộ khuếch đại trở kháng "
        "truyền giống nhau: V₂ = K Z P₂ và V₁ = K Z P₁; sau đó một bộ khuếch đại hiệu được dùng để tạo ra điện áp "
        "tín hiệu của bicell:"))
    b.append(eq("V = V₂ − V₁ = K Z (P₂ − P₁) = (K Z P / 2) · [erf ((y₂ + u)/r₁) − erf ((y₁ − u)/r₁)]", "6.135"))
    b.append(p(
        "Đáp ứng chuẩn hoá 2V/(K Z P) được vẽ trên Hình 6-117 theo u/r₁ với y₁ = y₂ = r₁/10."))
    b.append(fig(117, F.fig_6_117()))
    b.append(p(
        "Giả sử chùm nằm đúng tâm trong khe, y₁ = y₂; khi đó với những dịch chuyển nhỏ ta thu được:"))
    b.append(eq("V ≅ K Z P · (2u / (r₁√π)) · e<sup>−(y₁/r₁)²</sup>", "6.136"))
    b.append(p("Độ nhạy tín hiệu nhỏ là:"))
    b.append(eq("α<sub>BC</sub> ≡ (1 / (K Z P)) · (dV/du)|<sub>u = 0</sub> = (2 / (r₁√π)) · e<sup>−(y₁/r₁)²</sup>",
                "6.137"))
    b.append(p(
        "Đại lượng này đạt cực trị khi r₁ = √2·y₁, và độ nhạy tối ưu khi đó là 0,484/y₁."))
    b.append(note(
        "<b>Một chi tiết số học đáng lưu ý.</b> Nguyên bản ghi điều kiện tối ưu là r₁ = 2y₁, nhưng giá trị "
        "0,484/y₁ lại ứng với r₁ = √2·y₁. Lấy đạo hàm phương trình 6.137 theo r₁ và cho bằng không: "
        "−r₁⁻² + 2y₁²r₁⁻⁴ = 0, tức r₁² = 2y₁². Thay r₁ = √2·y₁ vào 6.137 được "
        "(2/(√2·y₁√π))·e<sup>−1/2</sup> = 0,484/y₁, đúng bằng con số trong nguyên bản; còn nếu thay r₁ = 2y₁ thì "
        "chỉ được 0,439/y₁. Như vậy điều kiện tối ưu là r₁ ≈ 1,41 y₁, và hai con số trong nguyên bản lệch nhau ở "
        "chỗ này."))

    # ------------------------------------------------------------ Continuous
    b.append(h3("Cảm biến vị trí liên tục", "Continuous position sensor"))
    b.append(p(
        "Thông tin vị trí trong một cảm biến vị trí liên tục (còn gọi là photodiode hiệu ứng bên) được suy ra từ "
        "đường đi chia đôi của các electron sinh ra bởi photon tới hai điện cực mặt sau của thiết bị. Với một "
        "thiết bị đồng nhất, dòng tới một điện cực chỉ phụ thuộc khoảng cách từ trọng tâm chùm sáng tới điện cực "
        "ấy; trong một thiết bị lý tưởng, các dòng sẽ bằng nhau khi chùm nằm tại tâm điện của thiết bị."))
    b.append(p(
        "Xét phân tích của một PSD liên tục một chiều. Tín hiệu dòng từ mỗi điện cực được biến đổi thành tín hiệu "
        "điện áp bằng một bộ khuếch đại trở kháng truyền có hệ số khuếch đại Z. Sau đó các bộ khuếch đại thuật "
        "toán được dùng để tạo tín hiệu tổng V<sub>s</sub> = K P Z A<sub>s</sub> và tín hiệu hiệu "
        "V<sub>d</sub> = K P Z A<sub>d</sub> α u, trong đó A<sub>s</sub> và A<sub>d</sub> lần lượt là hệ số khuếch "
        "đại của bộ khuếch đại tổng và bộ khuếch đại hiệu. Độ nhạy của cảm biến vị trí, α, khi đó được cho bởi:"))
    b.append(eq("α ≡ V<sub>d</sub> A<sub>s</sub> / (u V<sub>s</sub> A<sub>d</sub>)", "6.138"))
    b.append(p(
        "đại lượng này được xác định bằng cách đo V<sub>d</sub> và V<sub>s</sub> theo u. Cần chú ý rằng α ở đây có "
        "đơn vị nghịch đảo chiều dài, giống α<sub>KE</sub> và α<sub>BC</sub> ở hai mục trước: cả ba loại đầu dò "
        "đều được đặc trưng bởi cùng một đại lượng, chỉ khác nhau ở cách hiện thực và ở độ lớn đạt được. Với PSD "
        "liên tục, việc lấy tỉ số V<sub>d</sub>/V<sub>s</sub> có tác dụng triệt tiêu sự phụ thuộc vào công suất "
        "chùm và vào độ nhạy quang K — một lợi thế mà hai loại đầu dò kia không có nếu chỉ dùng một kênh."))

    # ------------------------------------------------------- Characterisation
    b.append(h2("Đặc trưng hoá các PSD", "Characterization of PSDs"))
    b.append(p(
        "Những đặc tính PSD trình bày dưới đây được đo bằng cách gắn thiết bị lên một bàn dịch chuyển có encoder "
        "quang dẫn động bằng một động cơ áp điện [9]; độ chính xác vị trí là ±0,1 µm. Một chùm laser He–Ne đã được "
        "suy giảm thích hợp được chiếu vuông góc tới PSD trong khi PSD dịch chuyển qua chùm. Điện áp tổng và điện "
        "áp hiệu của PSD được đo bằng các vôn kế số GP–IB theo dịch chuyển; các phép đo dịch chuyển và điện áp của "
        "PSD đều được điều khiển bằng máy tính."))
    b.append(p(
        "Hoạt động của một PSD lưỡi dao có thể được đánh giá bằng tín hiệu từ một phía của một bicell, cũng như từ "
        "một photodetector đặt sau một lưỡi dao. Điện áp ra của bộ khuếch đại trở kháng truyền ứng với dòng tín "
        "hiệu từ một ô của bicell United Detector Technology [10] (UDT) SPOT2D được vẽ theo dịch chuyển trên Hình "
        "6-118. Số liệu được vẽ dưới dạng điện áp ô đã chuẩn hoá theo u/r₁. Vì tín hiệu từ một ô của bicell tương "
        "đương với một đầu dò lưỡi dao, có thể so sánh số liệu này với Hình 6-115. Số liệu phù hợp ở mức hợp lý với "
        "u/r₁ &lt; 1 và một khớp tốt nhất cho phép suy ra r₁ = 0,4 mm; sự không phù hợp với u/r₁ ≥ 1 tương ứng với "
        "việc chùm laser đi dần ra ngoài mép ngoài của ô."))
    b.append(fig(118, F.fig_6_118()))
    b.append(p(
        "Hoạt động của một PSD hai ô được đánh giá bằng số liệu trên Hình 6-119, vẽ điện áp hiệu theo dịch chuyển "
        "cho UDT SPOT2D. Những sai lệch so với đường cong lý thuyết trên Hình 6-117 ở u ≤ 0,4 mm và u ≥ 1,1 mm là "
        "do chùm đi ra ngoài các mép của bicell. Vùng tuyến tính của PSD nằm quanh điểm làm việc tĩnh tối ưu "
        "(V₁ − V₂ = 0); một khớp bình phương tối thiểu của một đường thẳng cho độ dốc A₁₂ = 4,88 mV µm⁻¹ đối với "
        "thiết bị này."))
    b.append(fig(119, F.fig_6_119()))
    b.append(p(
        "Với số liệu trên Hình 6-118 và 6-119, P = 0,37 mW và Z = 5 kΩ; như vậy giá trị thực nghiệm của độ nhạy "
        "được xác định là K<sub>exp</sub> = 0,65 A W⁻¹. Khe danh định của bicell SPOT2D có kích thước sao cho "
        "y₁ = 63,5 µm; do đó, dùng giá trị y₁ này và r₁ = 0,4 mm trong phương trình 6.137, độ nhạy tính được của "
        "bicell là 3,8 × 10³ m⁻¹. Giá trị thực nghiệm của độ nhạy được tính từ A₁₂, K<sub>exp</sub>, P và Z là "
        "4,1 × 10³ m⁻¹."))
    b.append(note(
        "<b>Kiểm tra lại phép tính 3,8 × 10³ m⁻¹.</b> Nếu thay trực tiếp r₁ = 0,4 mm và y₁ = 63,5 µm vào phương "
        "trình 6.137, kết quả là (2/(0,4.10⁻³ · √π))·e<sup>−(0,15875)²</sup> ≈ 2,75 × 10³ m⁻¹, không phải "
        "3,8 × 10³ m⁻¹. Con số 3,8 × 10³ chỉ tái lập được khi dùng bán kính 1/e là r₁/√2 ≈ 0,283 mm thay cho r₁ "
        "trong mẫu số và trong số hạng mũ: khi đó (2/(0,283.10⁻³·√π))·e<sup>−0,0504</sup> ≈ 3,79 × 10³ m⁻¹. Đây là "
        "một nhầm lẫn thường gặp giữa bán kính 1/e² và bán kính 1/e của chùm Gauss, và nó cũng giải thích vì sao "
        "giá trị tính được lại thấp hơn giá trị thực nghiệm chứ không cao hơn. Dù lấy cách nào, kết luận định "
        "lượng vẫn không đổi: độ nhạy tính được và độ nhạy đo được chỉ lệch nhau trong khoảng 10–30%, tuỳ theo "
        "định nghĩa bán kính chùm được dùng."))
    b.append(p(
        "Việc đánh giá hoạt động của trục x trên một PSD liên tục hai trục UDT SC10 được minh hoạ trên các Hình "
        "6-120 đến 6-122. PSD được định hướng sao cho trục y thẳng đứng; như vậy, về mặt lý thuyết, "
        "V<sub>dy</sub> là hằng số khi PSD dịch chuyển, trừ gần các mép của thiết bị 10 mm × 10 mm. Như trên Hình "
        "6-120, V<sub>sx</sub> gần như không đổi trừ gần các mép của thiết bị; điều này có nghĩa là độ nhạy quang "
        "(K) không thay đổi nhiều theo vị trí chùm laser trên đầu dò này. Sự biến thiên của V<sub>dx</sub> theo "
        "dịch chuyển được trình bày trên Hình 6-121; PSD này có một dải tuyến tính rộng. Độ tuyến tính của các PSD "
        "liên tục thường có thể được cải thiện bằng cách dùng tỉ số V<sub>dx</sub>/V<sub>sx</sub>, như trên Hình "
        "6-122; độ nhạy của PSD này được xác định từ khớp bình phương tối thiểu trên phần tuyến tính của đặc tuyến "
        "là 183 m⁻¹."))
    b.append(fig(120, F.fig_6_120()))
    b.append(fig(121, F.fig_6_121()))
    b.append(fig(122, F.fig_6_122()))
    b.append(p(
        "Một lớp PSD mới hơn được đại diện bởi PSD liên tục một trục Sitek [11] 1L10, thiết bị này thường tuyến "
        "tính hơn. Một ví dụ về đặc tuyến V<sub>d</sub>/V<sub>s</sub> theo u được trình bày trên Hình 6-123. Độ nhạy "
        "được xác định từ khớp bình phương tối thiểu trên phần tuyến tính của đặc tuyến là 307 m⁻¹."))
    b.append(fig(123, F.fig_6_123()))

    # --------------------------------------------------------------- Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Một PSD cấu thành từ một photodetector có lưỡi dao chắn là đơn giản, có độ nhạy chỉ phụ thuộc bán kính "
        "chùm laser, và có thời gian đáp ứng do photodetector quyết định. Do đó, với những phép đo dịch chuyển nhỏ "
        "cần thời gian lên nhanh, loại PSD này là lựa chọn ưu tiên."))
    b.append(p(
        "Độ nhạy cực đại của một bicell lớn hơn khoảng 20% so với một photodetector lưỡi dao. Nó có ưu điểm là "
        "kích thước nhỏ và kinh tế. Thời gian lên danh định của UDT SPOT2D vào cỡ 10 ns. Hơn nữa, có thể dễ dàng "
        "đạt được phép đo hai trục bằng một quadcell, với một sự gia tăng thời gian lên do điện dung của đầu dò "
        "tăng."))
    b.append(p(
        "Những nhược điểm do chùm laser nhỏ và dịch chuyển nhỏ gây ra được khắc phục bằng các PSD liên tục. Vì "
        "những thiết bị này thường lớn hơn nhiều (có loại đường kính vài inch), chúng thường có thời gian lên dài "
        "hơn các PSD khác. Tuy vậy, Sitek 1L10 với dải hoạt động tuyến tính 10 mm có tần số nửa công suất trên đo "
        "được là 3 MHz."))
    b.append(p(
        "Trong những ứng dụng mà tín hiệu ra của PSD phải tỉ lệ tuyến tính với dịch chuyển của chùm, người ta dùng "
        "các bộ khuếch đại thuật toán chia tương tự để lấy V<sub>d</sub>/V<sub>s</sub> theo thời gian thực nhằm mở "
        "rộng dải tuyến tính của thiết bị. Đáng tiếc là đáp ứng tần số của những bộ khuếch đại này thường lại "
        "chính là yếu tố giới hạn đáp ứng tần số của cả hệ PSD. Trong những trường hợp đáp ứng tần số cao là quan "
        "trọng, thường có thể chỉ dùng V<sub>d</sub> nếu cẩn thận làm việc trong vùng tuyến tính của thiết bị. Với "
        "những dịch chuyển tĩnh lớn, cỡ bằng kích thước đầu dò, có thể ghi V<sub>d</sub> và V<sub>s</sub> bằng hệ "
        "thu thập dữ liệu điều khiển bằng máy tính, khớp đặc tuyến hiệu chuẩn bằng số với một đa thức, rồi sau đó "
        "mọi điện áp từ đầu dò đều có thể được quy về vị trí chùm."))
    b.append(p(
        "Những giới hạn nhiễu trong cảm biến OBD đến từ laser, từ bản chất của bề mặt phản xạ và từ PSD. Nên ưu "
        "tiên những laser có độ ổn định biên độ tốt, nhưng đây không phải là đóng góp nhiễu quan trọng khi dùng "
        "V<sub>d</sub>/V<sub>s</sub> để suy ra dịch chuyển. Ngược lại, độ ổn định hướng của chùm laser lại quan "
        "trọng. Nếu bề mặt phản xạ là bề mặt của một vật rắn điển hình thì nhiễu đưa vào khi phản xạ là không đáng "
        "kể; điều này có thể không đúng với một gương phản xạ kiểu màng mỏng (pellicle), nơi chuyển động Brown của "
        "bề mặt có thể đáng kể. Những giới hạn nhiễu của PSD là những giới hạn thông thường gắn với photodetector "
        "và các bộ khuếch đại."))

    b.append(h3("So sánh ba loại đầu dò", "Comparing the three detector types"))
    b.append(table(
        ["Tiêu chí", "Lưỡi dao", "Hai ô / bốn ô", "PSD liên tục"],
        [["Độ nhạy", "1/(r₁√π)", "≈ 0,484/y₁ (lớn hơn ~20%)", "183–307 m⁻¹ (thiết bị thương mại)"],
         ["Thời gian lên", "Do photodetector quyết định", "≈ 10 ns (SPOT2D)", "Dài hơn; 1L10 đạt 3 MHz"],
         ["Kích thước", "Nhỏ", "Nhỏ, kinh tế", "Lớn (đường kính vài inch)"],
         ["Dải tuyến tính", "u ≤ 0,387 r₁", "Quanh điểm V₁ − V₂ = 0", "Rộng, cỡ kích thước thiết bị"],
         ["Khử công suất chùm", "Không", "Không (nếu chỉ dùng V)", "Có, nhờ tỉ số V<sub>d</sub>/V<sub>s</sub>"],
         ["Hai trục", "Không", "Có, với quadcell", "Có, với PSD hai trục"]],
        "Bảng tổng hợp của người dịch, dựng từ phần Tóm tắt và các phương trình 6.129, 6.137, 6.138 của nguyên "
        "bản. Cột độ nhạy không so sánh trực tiếp được giữa các cột vì mỗi loại có tham số hình học riêng."))

    # ------------------------------------------------------------ References
    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "A. C. Boccara, D. Fournier, and J. Badoz, <i>Appl. Phys. Lett.</i>, 30, 933, 1983.",
        "G. C. Wetsel, Jr. and S. A. Stotts, <i>Appl. Phys. Lett.</i>, 42, 931, 1983.",
        "e.g.: D. Fournier and A. C. Boccara, <i>Scanned Image Microscopy</i>, E. A. Ash, Ed., London: Academic "
        "Press, 1980, 347–351; J. C. Murphy and L. C. Aamodt, <i>Appl. Phys. Lett.</i>, 39, 519, 1981; "
        "G. C. Wetsel, Jr. and F. A. McDonald, <i>Appl. Phys. Lett.</i>, 41, 926, 1982.",
        "M. A. Olmstead, S. Kohn, N. M. Amer, D. Fournier, and A. C. Boccara, <i>Appl. Phys. A</i>, 132, 68, 1983.",
        "G. Meyer and N. M. Amer, <i>Appl. Phys. Lett.</i>, 53, 1045, 1988.",
        "J. C. Murphy and G. C. Wetsel, Jr., <i>Mater. Evaluation</i>, 44, 1224, 1986.",
        "G. C. Wetsel, Jr., S. E. McBride, R. J. Warmack, and B. Van de Sande, <i>Appl. Phys. Lett.</i>, 55, 528, "
        "1989.",
        "S. E. McBride and G. C. Wetsel, Jr., Surface-displacement imaging using optical beam deflection, "
        "<i>Review of Progress in Quantitative Nondestructive Evaluation</i>, Vol. 9A, D. O. Thompson and "
        "D. E. Chimenti, (Eds.), New York: Plenum, 1990, 909–916.",
        "Burleigh Instruments, Inc., Fishers, NY 14453.",
        "United Detector Technology, 12525 Chadron Ave., Hawthorne, CA 90250.",
        "On-Trak Photonics Inc., 20321 Lake Forest Dr., Lake Forest, CA 92630.",
    ]))
    b.append(quote(
        "Độ nhạy của một đầu dò lưỡi dao chỉ phụ thuộc vào bán kính chùm laser — đó là lý do nó vẫn là lựa chọn "
        "đúng cho những dịch chuyển nhỏ cần đo nhanh, sau hơn ba thập kỷ.",
        "Grover C. Wetsel, Jr."))
    b.append(nav(12, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Optical beam deflection is the oldest trick in this chapter dressed in modern clothes: you do not measure "
        "the displacement, you measure where a light beam ends up after the displacement has moved it. The "
        "transducer is geometry. The measurement problem is reduced to finding the centroid of a spot of light, "
        "and that is a problem the detector industry solved very well — which is why this section can spend most "
        "of its length on three transfer functions rather than on hardware."))
    b.append(p(
        "The three detector types are worth reading as a single argument rather than three descriptions. Each "
        "trades one property for another, and the trade is always the same shape: sensitivity against range, and "
        "speed against size."))

    b.append(fig(113, F.fig_6_113(), "en"))
    b.append(p(
        "The configuration in Figure 6.113 is the one to keep in mind. A surface moves by u, the reflected beam "
        "moves by roughly 2u on the detector, and the detector converts position to voltage. The factor of two "
        "between surface motion and spot motion is an optical lever, and it is the reason these sensors are so "
        "sensitive: you are not measuring a displacement, you are measuring an amplified version of it. Calibrate "
        "V against u once and the instrument is done."))
    b.append(p(
        "Applications listed in the text — photothermal spectroscopy, absolute attenuation measurement, "
        "subsurface imaging, atomic force microscopy, ultrasonic transducer characterisation — all share one "
        "property: something small moves, and it moves fast. That is the niche OBD occupies."))

    b.append(h2("The knife edge: sensitivity set by the beam alone", "Lưỡi dao: độ nhạy do chùm quyết định"))
    b.append(fig(114, F.fig_6_114(), "en"))
    b.append(p(
        "A photodetector behind a half-infinite screen is the simplest possible position sensor, and it has the "
        "cleanest result in the section. Starting from a Gaussian intensity distribution, equation 6.126, the "
        "power on the detector integrates to equation 6.127:"))
    b.append(eq("P<sub>d</sub> = (P / 2) · [1 + erf (u / r₁)]", "6.127"))
    b.append(p(
        "Everything follows from that one line. The response depends on u only through the ratio u/r₁, so the "
        "sensitivity of the device is set by the beam radius and by nothing else — not by the detector area, not "
        "by the wavelength, not by the electronics. Differentiating at the origin gives equation 6.129, "
        "α<sub>KE</sub> = 1/(r₁√π): a tighter beam is a more sensitive sensor, with no lower limit except the "
        "diffraction that produced the beam in the first place."))
    b.append(fig(115, F.fig_6_115(), "en"))
    b.append(p(
        "The price of that simplicity is range. The erf curve is only straight near the origin, and the text puts "
        "the limit at u ≤ 0.387 r₁ — about 1.5 % departure from linearity. Beyond that you are reading a "
        "transcendental function with a linear calibration, which is a quiet way of being wrong. Note also that "
        "P<sub>d</sub> = 97.7 % P at u = r₁: the sensor saturates within one beam radius of the null point, so the "
        "usable range is a fraction of the beam diameter, not a multiple of it."))
    b.append(p(
        "The chain from power to voltage is then three multiplications, equations 6.131 and 6.132: photodetector "
        "responsivity K converts power to current, transimpedance gain Z converts current to voltage, and the "
        "result is V ≅ KZP[1/2 + α<sub>KE</sub>u]. That KZP product is the scale factor you will find in every "
        "data sheet, and it is also the term that drifts when the laser power drifts — which is why the "
        "ratiometric trick of the continuous sensor matters."))

    b.append(h2("The bicell: twice the slope, half the range", "Hai ô: độ dốc gấp đôi, dải bằng nửa"))
    b.append(fig(116, F.fig_6_116(), "en"))
    b.append(p(
        "Split the detector in two, leave a narrow insensitive gap, and subtract. Equations 6.133 and 6.134 give "
        "the power on each half; equation 6.135 differences them into a single voltage. The subtraction is the "
        "whole point: the common-mode term P/2 cancels, so the output is proportional to the difference of two "
        "error functions and passes through zero when the beam is centred in the gap. A null at the operating "
        "point is a much better place to work than a half-power point, because the sign of the displacement is "
        "unambiguous and the offset is defined by geometry rather than by calibration."))
    b.append(fig(117, F.fig_6_117(), "en"))
    b.append(p(
        "The small-signal slope, equation 6.137, is α<sub>BC</sub> = (2/(r₁√π))·exp[−(y₁/r₁)²]. Two factors are at "
        "work: the 2 from the subtraction, and the exponential penalty for putting the gap off-centre in the "
        "beam. If the gap is wide relative to the beam you lose signal exponentially; if it is narrow the two "
        "cells are nearly the same detector and you lose the difference. The optimum sits at r₁ = √2·y₁, giving "
        "0.484/y₁ — about 20 % more sensitivity than a knife edge with the same beam, which is exactly the figure "
        "the summary quotes."))
    b.append(note(
        "<b>A note on the printed optimum.</b> The source text states the optimum condition as r₁ = 2y₁ and the "
        "optimum sensitivity as 0.484/y₁, but these two statements are not consistent. Differentiating equation "
        "6.137 with respect to r₁ gives r₁² = 2y₁², i.e. r₁ = √2·y₁, and substituting that value reproduces "
        "0.484/y₁ exactly; substituting r₁ = 2y₁ gives 0.439/y₁ instead. The correct condition is r₁ ≈ 1.41 y₁."))

    b.append(h2("The continuous PSD: range bought with speed", "PSD liên tục: đổi tốc độ lấy dải đo"))
    b.append(p(
        "A lateral-effect photodiode does not split the beam; it lets the photogenerated charge divide between two "
        "back electrodes according to where the centroid of the spot sits. The current to each electrode is a "
        "linear function of centroid position over almost the whole die, so the linear range becomes a property of "
        "the device size rather than of the beam size. That is the trade: a 10 mm die gives you 10 mm of range, "
        "and the capacitance that comes with a 10 mm die gives you a slower detector."))
    b.append(p(
        "Equation 6.138 defines the sensitivity ratiometrically, α = V<sub>d</sub>A<sub>s</sub>/(uV<sub>s</sub>"
        "A<sub>d</sub>). Dividing the difference signal by the sum signal removes K, removes P, and removes most "
        "of the drift that plagues the two previous types. It is the same idea as a ratiometric LVDT or a "
        "ratiometric bridge: measure the ratio, not the level. The cost is an analog divider, and the divider is "
        "usually the slowest element in the chain — which is why the text warns that the divider, not the "
        "detector, often sets the bandwidth."))

    b.append(h2("What the characterisation numbers actually show", "Những con số đặc trưng thực sự cho thấy gì"))
    b.append(fig(118, F.fig_6_118(), "en"))
    b.append(p(
        "The measured single-cell response of the SPOT2D bicell, Figure 6.118, fits the knife-edge theory for "
        "u/r₁ &lt; 1 and departs above it. The departure is not a failure of the theory; it is the beam walking off "
        "the outside edge of the cell, and the fact that the fit yields r₁ = 0.4 mm is the useful output of the "
        "exercise. A sensor you can characterise with one free parameter is a sensor you can trust."))
    b.append(fig(119, F.fig_6_119(), "en"))
    b.append(p(
        "The bicell difference voltage, Figure 6.119, is linear over roughly 0.4 mm to 1.1 mm with a slope of "
        "A₁₂ = 4.88 mV/µm. Combining that slope with P = 0.37 mW, Z = 5 kΩ and K<sub>exp</sub> = 0.65 A/W gives an "
        "experimental sensitivity of 4.1 × 10³ m⁻¹, against 3.8 × 10³ m⁻¹ calculated from equation 6.137. The "
        "agreement is good enough to confirm the model and not good enough to hide the fact that the calculated "
        "value is sensitive to which beam radius you call r₁ — using the 1/e radius instead of the 1/e² radius "
        "reproduces the printed 3.8 × 10³ exactly."))
    b.append(fig(120, F.fig_6_120(), "en"))
    b.append(fig(121, F.fig_6_121(), "en"))
    b.append(fig(122, F.fig_6_122(), "en"))
    b.append(p(
        "The SC10 series, Figures 6.120 to 6.122, tells the story of a large-area device. The sum voltage is flat "
        "across the die, which means the optical responsivity does not vary with spot position — a precondition "
        "for the ratiometric method to work. The difference voltage is linear over a broad range but with visible "
        "curvature near the edges. The ratio V<sub>dx</sub>/V<sub>sx</sub> straightens it, and the least-squares "
        "slope of that ratio is 183 m⁻¹."))
    b.append(fig(123, F.fig_6_123(), "en"))
    b.append(p(
        "The Sitek 1L10 gives 307 m⁻¹ over a 10 mm range and is visibly straighter. That combination — larger "
        "sensitivity and larger range at the same time — is the reason the newer class of devices displaced the "
        "older ones, and it is a reminder that in position sensing the figure of merit is not sensitivity alone "
        "but sensitivity times usable range."))

    b.append(h2("The summary, read as a decision table", "Phần tóm tắt, đọc như một bảng quyết định"))
    b.append(p(
        "The closing summary is a decision procedure. Small displacement, fast risetime: knife edge, because its "
        "response time is the photodetector's and nothing else. Small displacement, need two axes or a null: "
        "bicell or quadcell, accepting the extra capacitance. Large displacement, don't care about speed: "
        "continuous PSD, because range scales with die size. And if the laser power drifts, use the ratio and "
        "accept the divider's bandwidth."))
    b.append(p(
        "The noise paragraph deserves more attention than it usually gets. Amplitude noise from the laser is "
        "largely cancelled by the ratiometric readout; beam-pointing noise is not, and it enters directly as a "
        "position error, which is why a stable mount matters more than a stable laser. And the remark about "
        "pellicle reflectors is a warning worth heeding: a thin membrane has Brownian motion of its own, and an "
        "OBD sensor with sub-nanometre resolution will measure it whether you wanted to or not."))
    b.append(nav(12, "en"))
    return "".join(b)
