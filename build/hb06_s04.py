# -*- coding: utf-8 -*-
"""Handbook 6.4 — Piezoelectric Transducers and Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Hiệu ứng áp điện được Jacques và Pierre Curie phát hiện năm 1880 trên muối Rochelle. Đó là tên gọi khả "
        "năng của một số vật liệu phát ra điện tích tỉ lệ với ứng suất cơ học đặt trực tiếp lên chúng. Những vật "
        "liệu ấy cũng thể hiện hiệu ứng nghịch: chúng biến dạng tỉ lệ với điện trường đặt vào. Một số vật liệu kết "
        "tinh có tính áp điện nhờ cấu trúc tinh thể đặc thù của chúng."))
    b.append(p(
        "Cấu trúc mạng của một tinh thể được mô tả bằng ô đơn vị Bravais [1]. Trong tự nhiên có 230 kiểu đối xứng vi "
        "mô (nhóm không gian), dựa trên các yếu tố đối xứng như phép dịch, tâm nghịch đảo, mặt phẳng gương hay trục "
        "quay. Tổ hợp các yếu tố đối xứng ấy cho ra đối xứng vĩ mô gọi là nhóm điểm. Mọi tinh thể tự nhiên có thể "
        "xếp vào 32 lớp khác nhau (nhóm điểm) theo các yếu tố đối xứng của chúng. 32 nhóm điểm này lại chia thành hai "
        "nhóm con: (1) tinh thể có tâm đối xứng, và (2) tinh thể không có tâm đối xứng. 11 nhóm có tâm đối xứng "
        "không thể hiện tính áp điện. Trong 21 nhóm không có tâm đối xứng, có 20 nhóm thể hiện hiệu ứng áp điện dọc "
        "theo những trục định hướng riêng."))
    b.append(p(
        "Một lớp vật liệu áp điện quan trọng là các chất sắt điện, ở đó hiệu ứng áp điện gắn chặt với phân cực sắt "
        "điện — đại lượng có thể đảo chiều bằng một điện trường đủ mạnh [2, 3]. Để tạo tính áp điện cho vật liệu sắt "
        "điện, thường phải thực hiện quy trình phân cực, tức là tạm thời đặt một điện trường mạnh. Phân cực tương "
        "tự như việc từ hoá một nam châm vĩnh cửu."))

    b.append(h2("Phương trình chủ đạo và các hệ số", "Governing equations and coefficients"))
    b.append(p(
        "Phương trình hiện tượng luận mô tả biến dạng của một tinh thể cách điện chịu đồng thời ứng suất đàn hồi và "
        "ứng suất điện được viết là:"))
    b.append(eq("x<sub>ij</sub> = s<sub>ijkl</sub> X<sub>kl</sub> + d<sub>mij</sub> E<sub>m</sub> + "
                "M<sub>mnij</sub> E<sub>m</sub> E<sub>n</sub>", "6.55"))
    b.append(p(
        "trong đó x<sub>ij</sub> là các thành phần biến dạng đàn hồi, s<sub>ijkl</sub> là tenxơ tuân thủ đàn hồi, "
        "X<sub>kl</sub> là các thành phần ứng suất, d<sub>mij</sub> là các thành phần tenxơ áp điện, "
        "M<sub>mnij</sub> là tenxơ điện giảo, và E<sub>m</sub>, E<sub>n</sub> là các thành phần điện trường."))
    b.append(p(
        "Bỏ qua các hiệu ứng bậc hai (điện giảo) và giả thiết vật liệu không chịu ứng suất (X<sub>kl</sub> = 0), "
        "biến dạng đàn hồi là:"))
    b.append(eq("x<sub>ij</sub> = d<sub>mij</sub> E<sub>m</sub>", "6.56"))
    b.append(p(
        "Phương trình 6.56 là định nghĩa toán học của hiệu ứng áp điện nghịch, trong đó biến dạng cảm ứng tỉ lệ "
        "trực tiếp với luỹ thừa bậc một của điện trường. Hiệu ứng áp điện thuận — tương đương về mặt nhiệt động — "
        "cho bởi:"))
    b.append(eq("P<sub>m</sub> = d<sub>mij</sub> X<sub>ij</sub>", "6.57"))
    b.append(p(
        "trong đó P<sub>m</sub> là thành phần phân cực điện. Sự khác nhau giữa hiệu ứng thuận và nghịch được minh "
        "hoạ trên Hình 6-38. Hiệu ứng nghịch mô tả chức năng chấp hành của vật liệu áp điện, khi một điện trường "
        "được điều khiển sẽ thay đổi chính xác hình dạng của vật liệu. Chức năng cảm nhận được mô tả bằng hiệu ứng "
        "thuận, khi một ứng suất được điều khiển trên vật liệu áp điện sinh ra điện tích tỉ lệ với ứng suất ấy."))
    b.append(fig(38, F.fig_6_38(), "vi"))
    b.append(p(
        "Tenxơ hạng ba d<sub>mij</sub> có thể được đơn giản hoá bằng ký hiệu ma trận [1] thành d<sub>ij</sub>, một "
        "tenxơ hạng hai. Ở dạng này, d<sub>ij</sub> được gọi đơn giản là hệ số điện tích áp điện, có đơn vị coulomb "
        "trên newton (C·N⁻¹) hoặc mét trên vôn (m·V⁻¹). Một bộ môđun khác cũng dùng để đặc trưng vật liệu áp điện "
        "là các hệ số điện áp áp điện g<sub>ij</sub>, định nghĩa theo ký hiệu ma trận là:"))
    b.append(eq("E<sub>i</sub> = g<sub>ij</sub> X<sub>j</sub>", "6.58"))
    b.append(p(
        "trong đó E<sub>i</sub> là thành phần điện trường sinh ra do ứng suất X<sub>j</sub>. Hai hệ số "
        "d<sub>ij</sub> và g<sub>ij</sub> liên hệ với nhau qua:"))
    b.append(eq("g<sub>ij</sub> = d<sub>ij</sub> / (ε<sub>ii</sub> ε<sub>0</sub>)", "6.59"))
    b.append(p(
        "trong đó ε<sub>ii</sub> là hằng số điện môi (độ thẩm điện tương đối) và ε<sub>0</sub> là độ thẩm điện của "
        "chân không (8,854 × 10⁻¹² F·m⁻¹). Một tính chất then chốt khác của vật liệu áp điện là hệ số liên kết cơ–"
        "điện k, định nghĩa là:"))
    b.append(eq("k² = năng lượng cơ thu được / năng lượng điện đưa vào", "6.60"))
    b.append(p("hoặc"))
    b.append(eq("k² = năng lượng điện thu được / năng lượng cơ đưa vào", "6.61"))
    b.append(p(
        "Giá trị k biểu diễn hiệu suất chuyển đổi một dạng năng lượng sang dạng kia của vật liệu áp điện. Vì "
        "chuyển đổi năng lượng không bao giờ trọn vẹn, k² luôn nhỏ hơn một, nên k luôn nhỏ hơn 1."))
    b.append(p(
        "Hai tham số quan trọng cuối cùng của vật liệu áp điện (sắt điện) là điểm Curie (T<sub>0</sub>) và nhiệt độ "
        "Curie (T<sub>c</sub>). Điểm Curie là nhiệt độ mà trên đó vật liệu mất tính sắt điện và tính áp điện. Nhiệt "
        "độ Curie được định nghĩa bằng định luật Curie–Weiss:"))
    b.append(eq("ε = C / (T − T<sub>c</sub>) &nbsp; với T &gt; T<sub>c</sub>", "6.62"))
    b.append(p(
        "trong đó ε là hằng số điện môi của vật liệu, C là hằng số Curie–Weiss và T là nhiệt độ. Đó là nhiệt độ mà "
        "tại đó vật liệu có xu hướng đạt hằng số điện môi cao nhất. Nhiệt độ Curie luôn thấp hơn điểm Curie (thường "
        "trong khoảng 10 °C)."))

    # ---------------------------------------------------------------- materials
    b.append(h2("Vật liệu áp điện", "Piezoelectric materials"))
    b.append(h3("Đơn tinh thể", "Single crystals"))
    b.append(p(
        "Một số vật liệu đơn tinh thể đã thể hiện tính áp điện. Những vật liệu này chiếm ưu thế ở một số ứng dụng "
        "nhất định, như bộ dao động ổn định tần số trong đồng hồ và rađa, và các linh kiện sóng âm bề mặt trong bộ "
        "lọc truyền hình và mạch tương quan tín hiệu tương tự. Danh sách vật liệu áp điện đơn tinh thể gồm thạch "
        "anh, niobat liti và tantalat liti, amôni đihiđrô sunphat, liti sunphat monohyđrat và muối Rochelle. Gần "
        "đây người ta phát hiện một số đơn tinh thể sắt điện gốc relaxor như chì kẽm niobat và chì magiê niobat, "
        "cùng các dung dịch rắn của chúng với chì titanat, có tính chất áp điện vượt trội so với các vật liệu áp "
        "điện khác."))
    b.append(p(
        "Thạch anh, tức SiO₂ kết tinh, có d₁₁ nhỏ (|2,3 × 10⁻¹²| C·N⁻¹) [1]. Thạch anh tay phải phát điện tích dương "
        "khi bị nén và điện tích âm khi bị kéo. Hệ số liên kết k của thạch anh cũng rất nhỏ, điển hình khoảng 0,1 "
        "[4]. Ngoài ra hằng số điện môi ε của thạch anh nhỏ (khoảng 4) [5]. Tuy vậy điểm Curie tương đối cao "
        "(T<sub>0</sub> ≈ 573 °C) [5], nên thạch anh ổn định trong các ứng dụng nhiệt độ cao. Dù tính chất áp điện "
        "thấp, thạch anh rất phong phú, rẻ, và đã có được vị trí vững chắc trong các ứng dụng giá thành thấp hoặc "
        "nhiệt độ cao."))
    b.append(p(
        "Tính áp điện của niobat liti (LiNbO₃) và tantalat liti (LiTaO₃) được nghiên cứu lần đầu vào giữa thập niên "
        "1960 [2]. Dưới biến dạng trượt, d₁₅ của LiNbO₃ và LiTaO₃ lần lượt là 73 và 26 (× 10⁻¹² C·N⁻¹). Cả hai có ε "
        "khoảng 40. Nếu cắt đúng hướng, chúng có hệ số liên kết k lần lượt 0,65 và 0,4. Ngoài ra điểm Curie của cả "
        "hai đều rất cao (T<sub>0</sub> ≈ 1210 °C với LiNbO₃ và 620 °C với LiTaO₃). Cả LiNbO₃ và LiTaO₃ đều thường "
        "được dùng trong các bộ phát hiện hồng ngoại."))
    b.append(p(
        "Muối Rochelle (KNaC₄H₄O₆·H₂O) được phát hiện có tính áp điện lần đầu năm 1880 [2]. Các giá trị d₃₁ và k₃₁ "
        "lần lượt là 275 × 10⁻¹² C·N⁻¹ và 0,65. Hằng số điện môi tương đối khoảng 350. Muối Rochelle có hai điểm "
        "Curie (T<sub>0</sub> thấp ≈ 18 °C và T<sub>0</sub> cao ≈ 24 °C). Nó tan mạnh trong nước, và vẫn còn được "
        "dùng rộng rãi trong các đầu đo điện thanh."))
    b.append(p(
        "Chì kẽm niobat Pb(Zn<sub>1/3</sub>Nb<sub>2/3</sub>)O₃ và chì magiê niobat Pb(Mg<sub>1/3</sub>Nb<sub>2/3</sub>)O₃ "
        "là những vật liệu relaxor điển hình, đặc trưng bởi cực đại của hằng số điện môi theo nhiệt độ rộng và phụ "
        "thuộc tần số. Các dung dịch rắn của chúng với chì titanat PbTiO₃ đã cho thấy tính chất áp điện tuyệt vời "
        "khi định hướng theo phương [001] [6]. Trong dung dịch rắn Pb(Zn<sub>1/3</sub>Nb<sub>2/3</sub>)O₃–PbTiO₃ "
        "đã đạt được hệ số điện tích áp điện d₃₃ tới 25 × 10⁻¹⁰ C·N⁻¹, hệ số liên kết k lớn hơn 0,9 và biến dạng "
        "cực lớn 1,7 %. Các đơn tinh thể relaxor này hiện đang được nghiên cứu ráo riết và cho thấy nhiều hứa hẹn "
        "cho các thế hệ đầu đo và cảm biến áp điện tương lai."))
    b.append(p(
        "Những loại vật liệu áp điện khác lại chiếm lĩnh thị trường đầu đo. Đó là gốm áp điện, polymer áp điện và "
        "vật liệu composite của gốm áp điện với polymer trơ. Phần còn lại của mục này tập trung vào các vật liệu áp "
        "điện phi đơn tinh thể."))

    b.append(h3("Gốm áp điện", "Piezoelectric ceramics"))
    b.append(p(
        "Trong gốm đa tinh thể với các hạt phân cực, tính ngẫu nhiên của các hạt — như sơ đồ trên Hình 6-39(a) — "
        "cho ra một vật liệu không có tính áp điện. Tính áp điện được tạo ra bằng cách “phân cực” gốm. Bằng việc "
        "đặt một điện trường một chiều mạnh ở nhiệt độ vừa dưới điểm Curie, phân cực tự phát trong mỗi hạt được "
        "định hướng theo chiều điện trường đặt vào, như sơ đồ trên Hình 6-39(b). Dù không bao giờ có thể định "
        "hướng hoàn toàn mọi đômen trong gốm theo trục phân cực do những hạn chế về đối xứng, gốm vẫn có một phân "
        "cực tổng dọc theo trục phân cực."))
    b.append(fig(39, F.fig_6_39(), "vi"))
    b.append(p(
        "Lớp gốm áp điện lớn nhất được tạo từ các ôxít hỗn hợp chứa bát diện O²⁻ dùng chung đỉnh. Kiểu cấu trúc "
        "lớn nhất, xây từ các bát diện ôxy dùng chung đỉnh, là họ perovskite, sẽ được bàn ở mục sau."))

    b.append(h3("Perovskite", "Perovskites"))
    b.append(p(
        "Perovskite là tên gọi một nhóm vật liệu có công thức tổng quát ABO₃, cùng cấu trúc với khoáng canxi "
        "titanat (CaTiO₃). Gốm áp điện có cấu trúc này gồm bari titanat (BaTiO₃), chì titanat (PbTiO₃), chì "
        "zirconat titanat (PbZr<sub>x</sub>Ti<sub>1−x</sub>O₃, hay PZT), chì lantan zirconat titanat "
        "[Pb<sub>1−x</sub>La<sub>x</sub>(Zr<sub>y</sub>Ti<sub>1−y</sub>)<sub>1−x/4</sub>O₃, hay PLZT] và chì magiê "
        "niobat [PbMg<sub>1/3</sub>Nb<sub>2/3</sub>O₃, hay PMN]. Dưới đây bàn về một số gốm trong đó."))
    b.append(p(
        "Hiệu ứng áp điện trong BaTiO₃ được phát hiện vào thập niên 1940 [4], và nó trở thành gốm áp điện đầu tiên "
        "được phát triển. Nó thay thế muối Rochelle vì ổn định hơn, có dải nhiệt độ làm việc rộng hơn và dễ chế "
        "tạo. Điểm Curie T<sub>0</sub> khoảng 130 °C. Trên 130 °C, pha lập phương không áp điện là pha ổn định, ở "
        "đó tâm điện tích dương (Ba²⁺ và Ti⁴⁺) trùng với tâm điện tích âm (O²⁻) — Hình 6-40(a). Khi làm nguội dưới "
        "điểm Curie, một cấu trúc tứ giác hình thành — Hình 6-40(b) — ở đó tâm điện tích dương dịch khỏi vị trí các "
        "ion O²⁻, dẫn tới sự hình thành các lưỡng cực điện. Bari titanat có hằng số điện môi tương đối ε₃₃ bằng "
        "1400 khi chưa phân cực và 1900 khi đã phân cực [2, 4]. Các hệ số d₁₅ và d₃₃ của BaTiO₃ lần lượt là 270 và "
        "191 × 10⁻¹² C·N⁻¹. Hệ số k của BaTiO₃ xấp xỉ 0,5. Hằng số điện môi lớn ở nhiệt độ phòng của bari titanat "
        "đã khiến nó được dùng rộng rãi trong các tụ nhiều lớp."))
    b.append(fig(40, F.fig_6_40(), "vi"))
    b.append(p(
        "Chì titanat PbTiO₃, được báo cáo là sắt điện lần đầu năm 1950 [4], có cấu trúc tương tự BaTiO₃ nhưng điểm "
        "Curie cao hơn đáng kể (T<sub>0</sub> = 490 °C). Chì titanat nguyên chất khó chế tạo ở dạng khối. Khi làm "
        "nguội qua điểm Curie, các hạt trải qua chuyển pha từ lập phương sang tứ giác, dẫn tới biến dạng lớn và gốm "
        "bị nứt. Biến dạng tự phát này có thể giảm bằng cách thêm các chất pha tạp như Ca, Sr, Ba, Sn và W. PbTiO₃ "
        "pha canxi [7] có hằng số điện môi tương đối ε₃₃ bằng 200, d₃₃ bằng 65 × 10⁻¹² C/N và k khoảng 0,5. Việc "
        "thêm canxi làm điểm Curie hạ xuống 225 °C. Ứng dụng chính của chì titanat là thủy âm và phao âm."))
    b.append(p(
        "Chì zirconat titanat (PZT) là dung dịch rắn hai cấu tử của PbZrO₃ (cấu trúc trực thoi phản sắt điện) và "
        "PbTiO₃ (cấu trúc perovskite tứ giác sắt điện) [2–4]. Nó có cấu trúc perovskite, với các ion Zr⁴⁺ và Ti⁴⁺ "
        "chiếm vị trí B của cấu trúc ABO₃ một cách ngẫu nhiên. Tại biên pha hình thái (MPB) phân chia pha tứ giác và "
        "trực thoi, PZT thể hiện tính chất áp điện tuyệt vời. Ở nhiệt độ phòng, MPB nằm tại tỉ lệ Zr/Ti bằng 52/48, "
        "cho ra một loại gốm áp điện cực kỳ dễ phân cực. PZT áp điện tại MPB thường được pha tạp nhiều loại ion để "
        "tạo ra cái được gọi là PZT “cứng” và “mềm”."))
    b.append(p(
        "PZT cứng được pha tạp bằng các ion acceptor, như K⁺ hoặc Na⁺ ở vị trí A, hay Fe³⁺, Al³⁺ hoặc Mn³⁺ ở vị trí "
        "B. Việc pha tạp này làm giảm tính chất áp điện và khiến PZT khó phân cực hoặc khử phân cực hơn. Tính chất "
        "áp điện điển hình của PZT cứng gồm [5, 7]: điểm Curie T<sub>0</sub> bằng 365 °C, ε₃₃ bằng 1700–1750 (đã "
        "phân cực), hệ số điện tích áp điện d₃₃ từ 360 đến 370 × 10⁻¹² C·N⁻¹ và hệ số liên kết khoảng 0,7."))
    b.append(p(
        "PZT mềm được pha tạp bằng các ion donor như La³⁺ ở vị trí A, hoặc Nb⁵⁺ hay Sb⁵⁺ ở vị trí B. Nó có tính "
        "chất áp điện rất cao và dễ phân cực hoặc khử phân cực. Tính chất áp điện điển hình của PZT mềm gồm [5, 7]: "
        "điểm Curie T<sub>0</sub> bằng 210 °C, hằng số điện môi tương đối ε₃₃ bằng 3200–3400 (đã phân cực), d₃₃ từ "
        "580 đến 600 × 10⁻¹² C·N⁻¹ và hệ số liên kết k₃₃ bằng 0,7."))

    b.append(h3("Chế tạo gốm áp điện", "Processing of piezoelectric ceramics"))
    b.append(p(
        "Tính chất cơ–điện của gốm áp điện chịu ảnh hưởng lớn từ điều kiện chế tạo. Từng bước của quy trình đều "
        "phải được kiểm soát cẩn thận để cho ra sản phẩm tốt nhất. Hình 6-41 là lưu đồ quy trình chế tạo oxit điển "
        "hình cho gốm áp điện. Nguyên liệu thô có độ tinh khiết cao được cân chính xác theo tỉ lệ mong muốn, rồi "
        "được trộn cơ học hoặc hoá học. Trong bước nung sơ bộ, các pha rắn phản ứng để tạo ra pha áp điện. Sau khi "
        "nung, hỗn hợp rắn được nghiền thành hạt mịn. Việc tạo hình được thực hiện bằng nhiều kỹ thuật gia công gốm "
        "khác nhau, gồm ép bột, đúc băng, đúc trượt hoặc đùn."))
    b.append(fig(41, F.fig_6_41(), "vi"))
    b.append(p(
        "Trong bước tạo hình, người ta thường thêm các chất hữu cơ vào bột gốm để cải thiện tính chảy và tính liên "
        "kết. Các chất hữu cơ này được loại bỏ trong một bước đốt chất kết dính ở nhiệt độ thấp (500 đến 600 °C). "
        "Sau khi đốt, kết cấu gốm được thiêu kết tới mật độ tối ưu ở nhiệt độ cao. Với các loại gốm áp điện chứa "
        "chì (PbTiO₃, PZT, PLZT), việc thiêu kết được thực hiện trong chén nung kín với khí quyển PbO được tối ưu "
        "hoá. Lý do là các loại gốm này bị mất chì ở nhiệt độ trên 800 °C. Như đã nói ở trên (Hình 6-39), tính "
        "ngẫu nhiên của các hạt gốm cho ra một vật liệu không áp điện. Bằng cách mạ điện cực lên gốm và đặt một "
        "điện trường một chiều mạnh ở nhiệt độ cao, gốm được phân cực. Tới đây, gốm áp điện đã sẵn sàng cho các "
        "bước gia công tinh và đặc trưng hoá cuối cùng."))

    b.append(h3("Polymer áp điện", "Piezoelectric polymers"))
    b.append(p(
        "Tính áp điện của polymer được báo cáo lần đầu năm 1969 [8]. Tính chất này bắt nguồn từ các vùng kết tinh "
        "hình thành trong polymer khi đông đặc từ trạng thái nóng chảy. Khi polymer được kéo hoặc giãn, các vùng ấy "
        "trở nên phân cực và có thể được phân cực bằng cách đặt một điện trường cao. Các polymer áp điện được biết "
        "đến rộng rãi nhất là polyvinyliden florua [9, 10], còn gọi là PVDF; copolymer polyvinyliden florua – "
        "trifloroetylen, hay P(VDF-TrFE) [9, 10]; và các nylon có số lẻ nguyên tử cacbon, như Nylon-11 [11]."))
    b.append(p(
        "Tính chất cơ–điện của polymer áp điện thấp hơn đáng kể so với gốm áp điện. Giá trị d₃₃ của PVDF và "
        "P(VDF-TrFE) xấp xỉ 33 (× 10⁻¹² C·N⁻¹), và hằng số điện môi ε nằm trong khoảng 6 đến 12 [12, 13]. Cả hai "
        "đều có hệ số liên kết k bằng 0,20 và điểm Curie T<sub>0</sub> xấp xỉ 100 °C. Với Nylon-11, ε khoảng 2 [11], "
        "còn k khoảng 0,11."))

    b.append(h3("Composite gốm áp điện / polymer", "Piezoelectric ceramic/polymer composites"))
    b.append(p(
        "Như đã nêu, một số vật liệu đơn tinh thể, gốm và polymer thể hiện tính áp điện. Ngoài các vật liệu khối, "
        "người ta cũng đã tạo ra composite của gốm áp điện với polymer. Bảng 6.7 [14] tóm tắt ưu và nhược điểm của "
        "mỗi loại vật liệu. Gốm rẻ hơn và dễ chế tạo hơn polymer hay composite. Chúng cũng có hằng số điện môi tương "
        "đối cao và liên kết cơ–điện tốt. Tuy vậy, chúng có trở kháng âm cao nên kém phù hợp về mặt âm học với nước "
        "— môi trường mà chúng thường phát hoặc thu tín hiệu. Ngoài ra, vì cứng và giòn, gốm khối không thể tạo hình "
        "trên mặt cong, hạn chế tính linh hoạt trong thiết kế đầu đo. Cuối cùng, chúng có mức tạp âm cao gắn với các "
        "mode cộng hưởng."))
    b.append(p(
        "Polymer áp điện phù hợp âm học với nước, rất dẻo và có ít mode giả. Tuy vậy, ứng dụng của các polymer này bị "
        "hạn chế bởi liên kết cơ–điện thấp, hằng số điện môi thấp và giá chế tạo cao. Composite gốm áp điện/polymer "
        "đã cho thấy tính chất vượt trội so với vật liệu một pha. Như Bảng 6.7 cho thấy, chúng kết hợp liên kết "
        "cao, trở kháng thấp, ít mode giả và hằng số điện môi trung bình. Ngoài ra chúng dẻo và giá vừa phải."))
    b.append(table(
        ["Thông số", "Gốm", "Polymer", "Composite gốm/polymer"],
        [
            ["Trở kháng âm", "Cao (−)", "Thấp (+)", "Thấp (+)"],
            ["Hệ số liên kết", "Cao (+)", "Thấp (−)", "Cao (+)"],
            ["Mode giả", "Nhiều (−)", "Ít (+)", "Ít (+)"],
            ["Hằng số điện môi", "Cao (+)", "Thấp (−)", "Trung bình (+)"],
            ["Tính dẻo", "Cứng (−)", "Dẻo (+)", "Dẻo (+)"],
            ["Giá", "Rẻ (+)", "Đắt (−)", "Trung bình (+)"],
        ],
        caption="Bảng 6.7 — Ưu điểm (+) và nhược điểm (−) của gốm áp điện, polymer và composite. "
                "Theo T. R. Gururaja, Amer. Ceram. Soc. Bull., 73, 50, 1994."))

    # ---------------------------------------------------------------- suppliers
    b.append(h2("Nhà cung cấp vật liệu áp điện", "Suppliers of piezoelectric materials"))
    b.append(p(
        "Bảng 6.8 liệt kê một số nhà cung cấp vật liệu áp điện, địa chỉ và việc họ cung cấp gốm, polymer hay "
        "composite áp điện. Phần lớn trong số họ chế tạo vật liệu theo ứng dụng cụ thể."))
    b.append(table(
        ["Tên", "Địa chỉ", "Gốm", "Polymer", "Composite"],
        [
            ["AMP Sensors", "950 Forge Ave., Morristown, PA 19403<br>Tel: (610) 650-1500 · Fax: (610) 650-1509",
             "✓", "", ""],
            ["Krautkramer Branson", "50 Industrial Park Rd., Lewistown, PA 17044<br>"
             "Tel: (717) 242-0327 · Fax: (717) 242-2606", "✓", "", ""],
            ["Materials Systems, Inc.", "531 Great Road, Littleton, MA 01460<br>"
             "Tel: (508) 486-0404 · Fax: (508) 486-0706", "✓", "", ""],
            ["Morgan Matroc, Inc.", "232 Forbes Rd., Bedford, OH 44146<br>"
             "Tel: (216) 232-8600 · Fax: (216) 232-8731", "✓", "", ""],
            ["Sensor Technology Ltd.", "20 Stewart Rd., P.O. Box 97, Collingwood, Ontario, Canada<br>"
             "Tel: +1 (705) 444-1440 · Fax: +1 (705) 444-6787", "✓", "", ""],
            ["Staveley Sensors, Inc.", "91 Prestige Park Circle, East Hartford, CT 06108<br>"
             "Tel: (860) 289-5428 · Fax: (860) 289-3189", "✓", "", ""],
            ["Valpey-Fisher Corporation", "75 South Street, Hopkinton, MA 01748<br>"
             "Tel: (508) 435-6831 · Fax: (508) 435-5289", "✓", "", ""],
            ["Vermon U.S.A.", "6288 SR 103 North Bldg. 37, Lewistown, PA 17044<br>"
             "Tel: (717) 248-6838 · Fax: (717) 248-7066", "✓", "", ""],
            ["TRS Ceramics, Inc.", "2820 E. College Ave., State College, PA 16801<br>"
             "Tel: (814) 238-7485 · Fax: (814) 238-7539", "✓", "", ""],
        ],
        caption="Bảng 6.8 — Nhà cung cấp vật liệu và cảm biến áp điện. Danh sách nguyên văn theo bản gốc năm 1999."))

    # ---------------------------------------------------------------- measurement
    b.append(h2("Đo hiệu ứng áp điện", "Measurements of piezoelectric effect"))
    b.append(p(
        "Nhiều phương pháp khác nhau đã được đề xuất để đặc trưng tính chất áp điện của vật liệu. Kỹ thuật cộng "
        "hưởng đo các tần số đặc trưng khi một mẫu thử được cắt đúng hình dạng (thường là gốm) được kích thích bằng "
        "một điện trường biến thiên hình sin. Ở mức gần đúng bậc nhất, hành vi của mẫu áp điện gần tần số cộng "
        "hưởng cơ bản có thể biểu diễn bằng một mạch tương đương như trên Hình 6-42(a). Hành vi điện kháng của mẫu "
        "theo tần số được biểu diễn trên Hình 6-42(b). Bằng cách đo các tần số đặc trưng của mẫu, có thể tính được "
        "các hằng số vật liệu, trong đó có các hệ số áp điện. Các phương trình dùng cho việc tính toán tính chất "
        "cơ–điện được mô tả trong Tiêu chuẩn IEEE về áp điện [15]."))
    b.append(fig(42, F.fig_6_42(), "vi"))
    b.append(p(
        "Ví dụ đơn giản nhất của phép đo áp điện bằng kỹ thuật cộng hưởng liên quan tới một thanh gốm áp điện "
        "(điển hình đường kính 6 mm, dài 15 mm) được phân cực dọc theo chiều dài. Có thể chứng minh rằng hệ số liên "
        "kết k₃₃ được biểu diễn theo các tần số cộng hưởng nối tiếp f<sub>s</sub> và song song f<sub>p</sub>:"))

    b.append(eq("k₃₃² = (π/2)(f<sub>s</sub>/f<sub>p</sub>) · tan[ (π/2)(f<sub>p</sub> − f<sub>s</sub>)/f<sub>p</sub> ]",
                "6.63"))
    b.append(p(
        "Hệ số áp điện dọc d₃₃ được tính từ k₃₃, độ tuân thủ đàn hồi s₃₃<sup>E</sup> và hằng số điện môi tần số "
        "thấp ε₃₃<sup>X</sup>:"))
    b.append(eq("d₃₃ = k₃₃ (ε₃₃<sup>X</sup> s₃₃<sup>E</sup>)<sup>1/2</sup>", "6.64"))
    b.append(p(
        "Tương tự, có thể suy ra các hệ số liên kết cơ–điện và môđun áp điện khác bằng cách dùng các mode rung khác "
        "nhau của mẫu. Nhược điểm của kỹ thuật cộng hưởng là phép đo bị giới hạn ở những tần số xác định bởi cộng "
        "hưởng cơ–điện. Kỹ thuật này chủ yếu dùng để đánh giá nhanh tính chất áp điện của các mẫu gốm, vì kích "
        "thước mẫu có thể dễ dàng điều chỉnh cho những điều kiện cộng hưởng cụ thể."))
    b.append(p(
        "Các kỹ thuật dưới cộng hưởng thường được dùng để đánh giá tính chất áp điện của vật liệu ở những tần số "
        "thấp hơn nhiều so với tần số cộng hưởng cơ bản của mẫu. Chúng bao gồm cả việc đo điện tích áp điện dưới "
        "tác dụng của lực cơ học bên ngoài (hiệu ứng thuận) lẫn việc đo dịch chuyển do điện trường gây ra (hiệu ứng "
        "nghịch). Trong trường hợp sau, dịch chuyển nhỏ hơn nhiều so với khi cộng hưởng; tuy vậy vẫn có thể đo được "
        "bằng tenxơ kế, cảm biến điện dung, cảm biến LVDT (biến áp vi sai biến thiên tuyến tính) hoặc bằng giao thoa "
        "quang học [16, 17]."))
    b.append(p(
        "Một phương pháp trực tiếp được dùng rộng rãi để đánh giá khả năng cảm nhận của vật liệu áp điện ở tần số "
        "đủ thấp. Có thể đặt biến dạng cơ học theo những mode khác nhau như giãn theo chiều dày, giãn ngang, trượt "
        "theo chiều dày và trượt theo mặt, để thu được các thành phần khác nhau của tenxơ áp điện. Trong trường hợp "
        "đơn giản nhất, các điện cực kim loại được đặt trên hai mặt chính của đầu đo áp điện, vuông góc với chiều "
        "phân cực (chiều phân cực sắt điện), và lực cơ học được đặt dọc theo chiều ấy (Hình 6-38(b)). Khi đó điện "
        "tích sinh ra trên hai bản điện cực dưới tải cơ học tỉ lệ với hệ số áp điện dọc d₃₃ của vật liệu."))
    b.append(p(
        "Để liên hệ điện áp ra của đầu đo với điện tích áp điện, cần xét mạch tương đương (Hình 6-43(a)). Mạch gồm "
        "bộ phát điện tích Q = d₃₃F, điện trở rò của đầu đo R<sub>s</sub>, điện dung đầu đo C<sub>s</sub>, điện "
        "dung của dây nối C<sub>c</sub>, cùng điện trở và điện dung lối vào của khuếch đại R<sub>a</sub> và "
        "C<sub>a</sub>. Ở đây F là lực đặt lên đầu đo (kéo hoặc nén). Tất cả các điện trở và điện dung trên Hình "
        "6-43(a) có thể được gộp lại như trên Hình 6-43(b). Bộ phát điện tích có thể chuyển thành bộ phát dòng điện "
        "I theo:"))
    b.append(fig(43, F.fig_6_43(), "vi"))
    b.append(eq("I = dQ/dt = d₃₃ · dF/dt", "6.65"))
    b.append(p(
        "Giả thiết khuếch đại không lấy dòng, điện áp ra V tại một tần số ω cho trước tính được là:"))
    b.append(eq("V = (d₃₃ F / C) · (jωτ)/(1 + jωτ)", "6.66"))
    b.append(p(
        "trong đó τ = RC là hằng số thời gian phụ thuộc mọi điện trở và điện dung của mạch. Ở tần số đủ cao, đáp "
        "ứng đo được không phụ thuộc tần số và có thể dễ dàng đánh giá d₃₃ từ phương trình 6.66 nếu biết điện dung "
        "tương đương C. Vì C được quyết định bởi các điện dung song song của mẫu, dây nối và khuếch đại (thường "
        "không biết chính xác), người ta thường thêm vào mạch một tụ chuẩn lớn hơn nhiều so với mọi điện dung liên "
        "quan. Tuy vậy, theo phương trình 6.66, độ nhạy của mạch giảm mạnh khi C giảm. Nếu τ không đủ lớn, tần số "
        "cắt thấp không cho phép đo áp điện trong điều kiện gần tĩnh hoặc tần số thấp."))
    b.append(p(
        "Để khắc phục khó khăn khi dùng khuếch đại điện áp cho phép đo áp điện, người ta đề xuất cái được gọi là "
        "khuếch đại điện tích. Mạch lý tưởng hoá của khuếch đại điện tích nối với đầu đo áp điện được trình bày trên "
        "Hình 6-44. Lưu ý rằng ở đây dùng một khuếch đại thuật toán lối vào FET với một tụ C<sub>f</sub> trong mạch "
        "hồi tiếp. Giả thiết dòng và điện áp vào của khuếch đại thuật toán không đáng kể, có thể liên hệ điện tích "
        "trên đầu đo với điện áp ra:"))
    b.append(fig(44, F.fig_6_44(), "vi"))
    b.append(eq("V = − Q/C<sub>f</sub> = − d₃₃ F / C<sub>f</sub>", "6.67"))
    b.append(p(
        "Phương trình 6.67 cho đáp ứng không phụ thuộc tần số, trong đó điện áp ra chỉ do hệ số áp điện d₃₃ và điện "
        "dung đã biết C<sub>f</sub> quyết định. Đáng tiếc là ưu điểm này khó đạt được trên thực tế, vì ngay cả một "
        "dòng vào nhỏ của khuếch đại cũng sẽ nạp tụ hồi tiếp, dẫn tới bão hoà khuếch đại. Vì vậy người ta thêm một "
        "điện trở song song R<sub>f</sub> vào mạch (đường nét đứt trên Hình 6-44) để ngăn việc nạp ấy. Nếu tính đến "
        "mạch RC của vòng hồi tiếp, điện áp ra sẽ có dạng của phương trình 6.66, nghĩa là trở nên phụ thuộc tần số. "
        "Khi ấy hằng số thời gian τ được quyết định bởi các tham số của vòng hồi tiếp và không phụ thuộc điện dung "
        "của đầu đo, của dây nối hay của lối vào khuếch đại. Đây là một ưu điểm quan trọng của khuếch đại điện tích "
        "khi so với khuếch đại điện áp thông thường."))

    # ---------------------------------------------------------------- applications
    b.append(h2("Ứng dụng", "Applications"))
    b.append(p(
        "Hiệu ứng áp điện thuận và nghịch ở một số vật liệu đã dẫn tới việc dùng chúng làm đầu đo cơ–điện. Đầu đo "
        "cơ–điện chuyển năng lượng điện thành năng lượng cơ và ngược lại. Những đầu đo này được dùng ở chế độ thụ "
        "động hoặc chủ động. Ở chế độ thụ động (cảm biến), đầu đo chỉ thu tín hiệu. Khi ấy tính chất áp điện thuận "
        "của vật liệu được khai thác để thu điện áp từ một ứng suất bên ngoài. Các ứng dụng ở chế độ thụ động gồm "
        "thủy âm hay thiết bị nghe dưới nước, micro, đầu đọc máy hát, bộ đánh lửa ga, tenxơ kế động và cảm biến rung "
        "động. Ở chế độ chủ động (chấp hành), đầu đo dùng tính chất áp điện nghịch để thay đổi kích thước và phát "
        "một tín hiệu âm vào môi trường. Các ứng dụng ở chế độ chủ động gồm đánh giá không phá huỷ, máy dò cá và dò "
        "độ sâu, máy in phun mực, cơ cấu vi định vị, bơm vi lượng và chẩn đoán hình ảnh siêu âm y tế. Thường thì "
        "cùng một đầu đo được dùng cho cả chức năng cảm biến lẫn chấp hành."))
    b.append(p(
        "Dưới đây nêu hai ví dụ về cảm biến áp điện. Ví dụ thứ nhất là đầu đo gốm, liên hệ biến dạng của cảm biến áp "
        "điện với điện áp ra qua hiệu ứng áp điện thuận. Gốm áp điện có môđun Young cao; do đó cần lực lớn để tạo "
        "biến dạng trong đầu đo đủ cho một đáp ứng điện đo được. Độ mềm của cảm biến áp điện có thể tăng mạnh bằng "
        "cách làm các dải dài hoặc tấm mỏng bằng vật liệu và gắn chúng như công xôn hay màng. Dịch chuyển ở đầu tự do "
        "của công xôn sẽ làm dầm uốn, dẫn tới ứng suất cơ học trong vật liệu áp điện và điện tích trên các điện cực. "
        "Một kết cấu phổ biến của bộ uốn áp điện được trình bày trên Hình 6-45(a). Hai dầm phân cực ngược chiều "
        "được gắn với nhau, một điện cực chung ở giữa và hai điện cực ở hai mặt ngoài. Khi bimorph uốn, dầm trên "
        "giãn còn dầm dưới nén, dẫn tới điện tích áp điện cùng dấu ở hai dầm mắc nối tiếp. Ở mức gần đúng bậc nhất, "
        "điện tích Q xuất hiện trên các điện cực tỉ lệ với dịch chuyển ∆l ở đầu bimorph theo phương trình 6.68 [18]:"))
    b.append(fig(45, F.fig_6_45(), "vi"))
    b.append(eq("Q = (3/8) · e₃₁ · (H w / L) · ∆l", "6.68"))
    b.append(p(
        "trong đó H, w và L lần lượt là độ dày, chiều rộng và chiều dài của bimorph, còn e₃₁ là hệ số áp điện ngang "
        "liên hệ phân cực điện với biến dạng trong vật liệu áp điện đã biến dạng. Có thể đo điện tích này bằng "
        "khuếch đại điện áp (Hình 6-43) hoặc bằng khuếch đại điện tích (Hình 6-44)."))
    b.append(p(
        "Trong một số ứng dụng, có thể cải thiện các tham số của cảm biến áp điện bằng cách dùng polymer sắt điện "
        "thay cho đơn tinh thể và gốm áp điện. Dù tính chất cơ–điện của polymer kém hơn gốm áp điện, hằng số điện "
        "môi thấp của chúng cho đáp ứng điện áp cao hơn, vì chúng có hệ số g áp điện lớn hơn. Ngoài ra polymer bền "
        "cơ học hơn và có thể chế tạo thành các lớp mỏng (xuống tới vài micrômét). Một ví dụ dùng bimorph polymer "
        "làm cảm biến áp suất được trình bày trên Hình 6-45(b). Một màng tròn gồm hai lớp polymer phân cực ngược "
        "được kẹp ở mép vào một vành cứng, tạo thành một micro. Điện áp xuất hiện trên các điện cực tỉ lệ với áp "
        "suất đặt vào p theo phương trình 6.69 [19]:"))
    b.append(eq("V = − (3/16) · (d₃₁/ε₃₃) · (D²/h²) · (1 − ν) · p", "6.69"))
    b.append(p(
        "trong đó D và h lần lượt là đường kính và độ dày của màng, ν là hệ số Poisson. Giá trị d₃₁/ε₃₃ cao của cảm "
        "biến polymer là lợi thế để có đáp ứng điện áp lớn hơn. Theo phương trình 6.66, lợi thế này chỉ hiện thực "
        "được nếu dùng khuếch đại có trở kháng vào cao đặt sát đầu đo để giảm ảnh hưởng của dây nối."))

    # ---------------------------------------------------------------- glossary
    b.append(h2("Định nghĩa các thuật ngữ", "Defining terms"))
    b.append('<dl class="glossary">')
    for term, body in [
        ("Đầu đo áp điện",
         "Thiết bị chuyển năng lượng điện đưa vào thành năng lượng cơ và ngược lại nhờ hiệu ứng áp điện."),
        ("Hệ số liên kết",
         "Hằng số vật liệu mô tả khả năng của vật liệu áp điện chuyển năng lượng điện thành năng lượng cơ và "
         "ngược lại."),
        ("Hệ số áp điện",
         "Hằng số vật liệu dùng để mô tả liên kết tuyến tính giữa các tham số điện và cơ của vật liệu áp điện."),
        ("Chất sắt điện",
         "Nhóm con của vật liệu áp điện có mômen lưỡng cực tổng (phân cực sắt điện) có thể đảo chiều bằng một "
         "điện trường đủ mạnh."),
        ("Phân cực",
         "Quá trình định hướng phân cực sắt điện theo một chiều duy nhất (chiều phân cực)."),
        ("Composite áp điện",
         "Vật liệu chứa hai hay nhiều thành phần có tính chất áp điện khác nhau."),
        ("Khuếch đại điện tích",
         "Khuếch đại thuật toán dùng để chuyển điện tích vào thành điện áp ra nhờ một tụ trong mạch hồi tiếp."),
    ]:
        b.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    b.append("</dl>")

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. F. Nye, <i>Physical Properties of Crystals</i>, Oxford: Oxford University Press, 1985.",
        "Y. Xu, <i>Ferroelectric Materials and Their Applications</i>, Amsterdam: North-Holland, 1991.",
        "L. E. Cross, “Ferroelectric ceramics: tailoring properties for specific applications,” in N. Setter and "
        "E. L. Colla (ed.), <i>Ferroelectric Ceramics: Tutorial Reviews, Theory, Processing, and Applications</i>, "
        "Basel: Birkhäuser, 1993.",
        "B. Jaffe, W. R. Cook, Jr., and H. Jaffe, <i>Piezoelectric Ceramics</i>, Marietta, OH: R. A. N., 1971.",
        "<i>The User’s Guide to Ultrasound &amp; Optical Products</i>, Hopkinton, MA: Valpey-Fisher Corporation, "
        "1996.",
        "S.-E. Park and T. R. Shrout, “Relaxor based ferroelectric single crystals with high piezoelectric "
        "performance,” Proc. of the 8th US–Japan Seminar on Dielectric and Piezoelectric Ceramics, October 15–18, "
        "Plymouth, MA, 1997, 235.",
        "<i>Piezoelectric Products</i>, Sensor Technology Limited, Collingwood, Ontario, Canada, 1991.",
        "H. Kawai, “The piezoelectricity of poly(vinylidene fluoride),” <i>Japan. J. Appl. Phys.</i>, 8, 975, 1969.",
        "L. F. Brown, “Ferroelectric polymers: current and future ultrasonic applications,” Proc. 1992 IEEE "
        "Ultrasonics Symposium, IEEE, New York, 1992, 539.",
        "T. Furukawa, “Recent advances in ferroelectric polymers,” <i>Ferroelectrics</i>, 104, 229, 1990.",
        "L. F. Brown, J. I. Scheinbeim, and B. A. Newman, “High frequency dielectric and electromechanical "
        "properties of ferroelectric nylons,” Proc. 1994 IEEE Ultrasonics Symposium, IEEE, New York, 1995, 337.",
        "<i>Properties of Raytheon Polyvinylidene Fluoride (PVDF)</i>, Raytheon Research Division, Lexington, MA, "
        "1990.",
        "<i>Standard and Custom Piezo Film Components</i>, Atochem Sensors Inc., Valley Forge, PA, 1991.",
        "T. R. Gururaja, “Piezoelectric transducers for medical ultrasonic imaging,” <i>Amer. Ceram. Soc. Bull.</i>, "
        "73, 50, 1994.",
        "<i>IEEE Standards on Piezoelectricity</i>, IEEE Std. 176, 1978.",
        "W. Y. Pan and L. E. Cross, “A sensitive double beam laser interferometer for studying high-frequency "
        "piezoelectric and electrostrictive strains,” <i>Rev. Sci. Instrum.</i>, 60, 2701, 1989.",
        "A. L. Kholkin, Ch. Wuethrich, D. V. Taylor, and N. Setter, “Interferometric measurements of electric "
        "field-induced displacements in piezoelectric thin films,” <i>Rev. Sci. Instrum.</i>, 67, 1935, 1996.",
        "A. J. Moulson and J. M. Herbert, <i>Electroceramics: Materials, Properties, Applications</i>, London: "
        "Chapman and Hall, 1990.",
        "J. M. Herbert, <i>Ferroelectric Transducers and Sensors</i>, New York: Gordon and Breach, 1982.",
    ]))
    b.append(nav(4, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Section 6.4 is the chapter’s materials-science entry. The other sections describe devices; this one "
        "describes why the material inside the device behaves the way it does, and the answer is crystal "
        "symmetry. Of the 32 crystallographic point groups, 11 have a centre of symmetry and cannot be "
        "piezoelectric; of the remaining 21, twenty show the effect. That single fact explains almost everything "
        "downstream — why quartz is weak but stable, why PZT at the morphotropic boundary is strong but "
        "temperature-limited, and why a poled ceramic is not the same material as an unpoled one."))

    b.append(h2("Two effects, one tensor", "Hai hiệu ứng, một tenxơ"))
    b.append(fig(38, F.fig_6_38(), "en"))
    b.append(p(
        "The same third-rank tensor d<sub>mij</sub> describes both directions. Written as a matrix d<sub>ij</sub> it "
        "carries units of C·N⁻¹ or, equivalently, m·V⁻¹ — the equivalence is the point: a material that produces "
        "charge per newton also produces strain per volt, and the two numbers are the same number. The voltage "
        "coefficient g<sub>ij</sub> = d<sub>ij</sub>/(ε<sub>ii</sub>ε<sub>0</sub>) then says something practical: "
        "a low-permittivity material gives a large voltage for the same charge, which is exactly why polymer "
        "sensors beat ceramics on voltage output despite much weaker d coefficients."))

    b.append(h2("What the numbers say", "Các con số nói gì"))
    b.append(table(
        ["Material", "d₃₃ (×10⁻¹² C·N⁻¹)", "k", "ε", "T₀ (°C)", "Note"],
        [
            ["Quartz", "2.3 (d₁₁)", "0.1", "≈4", "573", "Weak but stable to high temperature"],
            ["LiNbO₃", "73 (d₁₅)", "0.65", "≈40", "1210", "Very high Curie point; IR detectors"],
            ["LiTaO₃", "26 (d₁₅)", "0.4", "≈40", "620", "Same family, weaker"],
            ["Rochelle salt", "275 (d₃₁)", "0.65", "≈350", "18 / 24", "Two Curie points; water-soluble"],
            ["BaTiO₃", "191", "0.5", "1400–1900", "130", "First practical ceramic; multilayer capacitors"],
            ["PbTiO₃ (Ca-doped)", "65", "0.5", "200", "225", "Hydrophones, sonobuoys"],
            ["PZT hard", "360–370", "0.7", "1700–1750", "365", "Acceptor-doped; hard to depole"],
            ["PZT soft", "580–600", "0.7", "3200–3400", "210", "Donor-doped; easy to pole"],
            ["PVDF / P(VDF-TrFE)", "≈33", "0.20", "6–12", "≈100", "Flexible, acoustically matched to water"],
            ["Nylon-11", "—", "0.11", "≈2", "—", "Odd-numbered nylon"],
        ],
        caption="Table 6.4a — The materials of section 6.4 side by side. d-values are as printed in the source; "
                "d₁₁, d₁₅ and d₃₁ are not comparable with d₃₃."))
    b.append(p(
        "Two entries deserve a second look. PZT at the morphotropic phase boundary (Zr/Ti = 52/48 at room "
        "temperature) sits between a tetragonal ferroelectric and an orthorhombic antiferroelectric, and the "
        "boundary is where the piezoelectric coefficients peak — which is why essentially all commercial "
        "piezoceramics are PZT near that composition. And the relaxor single crystals (PZN–PT, PMN–PT) are in a "
        "different league altogether: d₃₃ around 25 × 10⁻¹⁰ C·N⁻¹, k above 0.9, and strains of 1.7 %, an order of "
        "magnitude beyond PZT."))

    b.append(h2("Poling, and why it is not optional", "Phân cực — và vì sao không thể bỏ qua"))
    b.append(fig(39, F.fig_6_39(), "en"))
    b.append(p(
        "A ceramic fresh out of the kiln is a mass of randomly oriented polar grains and has no net "
        "polarization — it is not piezoelectric. Poling, a strong dc field applied just below the Curie "
        "temperature, rotates the domains toward the field. Symmetry prevents full alignment, so the ceramic "
        "keeps only a fraction of the single-crystal response, but it keeps it permanently until the material is "
        "driven above its Curie point or depoled by a reversed field. This is the same logic as magnetizing a "
        "permanent magnet, and the same fragility applies."))
    b.append(fig(40, F.fig_6_40(), "en"))

    b.append(h2("Processing decides the properties", "Chế tạo quyết định tính chất"))
    b.append(fig(41, F.fig_6_41(), "en"))
    b.append(p(
        "The flow chart is not decoration. Lead loss above 800 °C is why PZT must be sintered in a sealed "
        "crucible with a PbO atmosphere; the cubic-to-tetragonal transition on cooling is why pure PbTiO₃ "
        "cracks itself apart and needs Ca, Sr, Ba, Sn or W doping; and the binder burnout at 500–600 °C is what "
        "stops residual organics from bloating the ceramic during sintering. Each of these is a place where a "
        "process choice becomes an electromechanical property."))

    b.append(h2("Measuring d₃₃", "Đo d₃₃"))
    b.append(fig(42, F.fig_6_42(), "en"))
    b.append(p(
        "The resonance method is fast and needs only a rod of known dimensions: drive it, find f<sub>s</sub> and "
        "f<sub>p</sub>, and equation 6.63 gives k₃₃, from which 6.64 gives d₃₃. Its limitation is built in — you "
        "can only measure at the frequencies the sample’s own geometry selects. Below resonance, the direct "
        "method applies a known force and measures the charge, which is where the equivalent circuits of Figures "
        "6.43 and 6.44 come in."))
    b.append(fig(43, F.fig_6_43(), "en"))
    b.append(p(
        "The voltage amplifier of 6.43 has a fatal flaw for piezoelectric work: its output depends on C, and C "
        "includes the cable capacitance, which is neither small nor known. Adding a large standard capacitor "
        "fixes the uncertainty but destroys the sensitivity. The charge amplifier of 6.44 removes the problem by "
        "holding the inverting input at virtual ground, so the cable capacitance is bootstrapped out and "
        "V = −Q/C<sub>f</sub>, depending only on d₃₃ and a capacitor you chose yourself."))
    b.append(fig(44, F.fig_6_44(), "en"))
    b.append(note(
        "Why R<sub>f</sub> is not optional. The ideal charge amplifier integrates the amplifier’s own input bias "
        "current along with the signal, and after a few seconds the output sits against a rail. The shunt "
        "resistor gives that current a dc path, at the cost of turning the response into the high-pass form of "
        "equation 6.66. The time constant is now set by R<sub>f</sub>C<sub>f</sub> alone — independent of the "
        "transducer and the cable — which is the practical advantage over a voltage amplifier even though the "
        "response is no longer flat to dc."))

    b.append(h2("The two canonical sensors", "Hai kết cấu tiêu biểu"))
    b.append(fig(45, F.fig_6_45(), "en"))
    b.append(p(
        "The bimorph of 6.45(a) solves a mechanical problem rather than an electrical one. Piezoceramics have "
        "high Young’s modulus, so a bulk block under a reasonable force produces almost no strain and therefore "
        "almost no charge. Making the material long and thin and mounting it as a cantilever trades force for "
        "displacement: a small tip movement now bends the beam enough to strain the ceramic. Two beams poled in "
        "opposite directions, cemented with a common centre electrode, double the charge, because the upper "
        "beam stretches while the lower compresses and the two series-connected outputs add."))
    b.append(p(
        "The polymer diaphragm of 6.45(b) solves the opposite problem. PVDF has a much smaller d₃₁ than PZT, but "
        "a much smaller ε as well, and g = d/ε therefore comes out larger — so for the same pressure the "
        "polymer film delivers more volts. That, plus mechanical flexibility and the ability to be made a few "
        "micrometres thick, is why polymer film dominates microphone and hydrophone diaphragms even though "
        "ceramic dominates actuators. The catch is stated in the text: the advantage only survives if the "
        "amplifier has a high input impedance and sits close to the transducer, because a long cable will "
        "divide the signal away before it is measured."))

    b.append(h2("Reading the tables", "Đọc các bảng"))
    b.append(p(
        "Table 6.7 is the section’s most useful page. Ceramic wins on coupling and cost, loses on acoustic "
        "impedance and flexibility; polymer wins on impedance and flexibility, loses on coupling and cost; the "
        "composite is the compromise that medical imaging settled on, because a 1–3 composite of PZT rods in an "
        "epoxy matrix gives ceramic-level coupling with polymer-level impedance. Table 6.8 is a 1999 supplier "
        "list and the contact details are historical, but the pattern — small specialist firms, not the large "
        "instrument houses — still holds."))
    b.append(nav(4, "en"))
    return "".join(b)
