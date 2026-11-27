# -*- coding: utf-8 -*-
"""Chapter 4, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 113-119 (PDF pp. 134-140).

Covers Section 4.2.1 (Examples 3 and 4: acetone pool, isoprene pool and
mist), Section 4.3 (release of liquid above its atmospheric boiling point,
Equations 4.27-4.30) and Section 4.3.1 (Example 5: propylene drain line).

Equations 4.13-4.26 belong to module C and are referenced by number only.
The integration module owns the page shell, page sources, references,
note terms, end matter and the h2 heading. Printed numerical
inconsistencies in the three worked examples are preserved and flagged.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, eq


def body_vi():
    b = []
    b.append(h4("4.2.1 Ví dụ về phát thải chất lỏng dưới điểm sôi khí quyển",
                "4.2.1 Example of liquid release below its atmospheric boiling point"))
    b.append(p("<b>Ví dụ 3.</b> Acetone được vận chuyển trong đường ống có các mối "
               "nối mặt bích thông thường ở 22 °C và chịu áp suất đo "
               "10<sup>5</sup> N/m². Một mối nối mặt bích hỏng tạo lỗ tiết "
               "4 × 10<sup>−5</sup> m²; đường ống cao khoảng 3 m so "
               "với mặt đất. Các thông số liên quan của acetone: mật độ chất "
               "lỏng 791 kg/m³; mật độ hơi 2,58 kg/m³; điểm sôi 56 °C; áp "
               "suất riêng phần ở 22 °C là 2,2 × 10<sup>4</sup> N/m² "
               "(0,22 atm); khối lượng phân tử 58; giới hạn nổ dưới (LEL) 2,1 % "
               "trong không khí."))
    b.append(p("Trước hết cần tính tốc độ phát thải chất lỏng từ chỗ rò, dùng "
               "Phương trình 4.13: G = 1,13 × 4 × "
               "10<sup>−5</sup> (791 × 10<sup>5</sup>)<sup>0.5</sup> "
               "= <b>0,4 kg/s</b>. Khi xác định phạm vi khu vực nguy hiểm, "
               "giả định thứ nhất là chất lỏng tới mặt đất mà không bay hơi. "
               "Vận tốc tia lấy từ Phương trình 4.17 và quãng đường từ Phương "
               "trình 4.15, giả định tia nằm ngang."))
    b.append(p("Vận tốc tia = 1,13 (10<sup>5</sup>/791)<sup>0.5</sup> = "
               "<b>12,7 m/s</b>. Quãng đường đi được = (2 × "
               "12,7<sup>2</sup> × 3/9,81)<sup>0.5</sup>; Khoảng cách = "
               "<b>9,93 m (lấy 10 m)</b>."))
    b.append(note("<b>Lưu ý về con số in.</b> Phép tính quãng đường cho "
                  "9,93 m (làm tròn thành 10 m), nhưng câu ngay sau đó lại đặt "
                  "tâm vũng ở 9,85 m từ điểm thẳng đứng bên dưới lỗ rò. Cả hai "
                  "giá trị đều được giữ nguyên như trong bản in."))
    b.append(p("Vũng sẽ hình thành và, nếu không được chứa giữ, lớn dần cho "
               "đến khi tốc độ bay hơi từ mặt vũng bằng tốc độ rò từ lỗ tiết. "
               "Dùng Phương trình 4.23 với giá trị thử R<sup>0.2</sup> = 15: "
               "A = (5,65 × 10<sup>2</sup> × 4 × "
               "10<sup>−5</sup> [791 × 10<sup>5</sup>]<sup>0.5</sup> "
               "× 15)/(0,22 × 58) m². Ở kích thước vũng đó, Hình "
               "4.3 cho R<sup>0.2</sup> khoảng 19; lặp lại phép tính được "
               "<b>A = 299 m²</b> và đường kính vũng <b>d = 22 m</b>."))
    b.append(p("Phạm vi vượt quá mép vũng và phía trên vũng được tính bằng "
               "Phương trình 4.26: X = [(5,8 × 10<sup>−2</sup> "
               "× 17,3 × 0,22 × 295)/(2,1 × "
               "19)]<sup>1.14</sup> = <b>1,75 m (lấy 2 m)</b>."))
    b.append(p("Giả định thứ hai — toàn bộ lượng rò tạo sương mù chất lỏng "
               "— được bỏ qua vì áp suất đẩy rất thấp. Không có khu vực nguy "
               "hiểm đáng kể tại đường ống rò; tính từ điểm trên mặt đất "
               "thẳng đứng bên dưới chỗ rò tồn tại khu vực cao <b>2 m</b> với "
               "bán kính <b>22 m</b> (10 + 10 + 2) theo mọi hướng."))
    b.append(p("<b>Ví dụ 4.</b> Dùng cùng hệ thống vận chuyển và lỗ tiết như "
               "Ví dụ 3, nhưng chở isoprene ở áp suất đo 2 × "
               "10<sup>5</sup> N/m² và nhiệt độ 22 °C. Thông số: mật độ "
               "chất lỏng 680 kg/m³; mật độ hơi 3 kg/m³; điểm sôi 34 °C; "
               "áp suất riêng phần 7,1 × 10<sup>4</sup> N/m² (0,71 atm); "
               "khối lượng phân tử 68; LEL 1 % trong không khí."))
    b.append(p("Cách xử lý ban đầu giống Ví dụ 3: tính tốc độ phát thải chất "
               "lỏng theo Phương trình 4.13, G = 1,13 × 4 × "
               "10<sup>−5</sup> [680 × 2 × "
               "10<sup>5</sup>]<sup>0.5</sup> = <b>0,53 kg/s</b>."))
    b.append(p("Theo Phương trình 4.17 và 4.15: Vận tốc tia = 1,13 "
               "(10<sup>5</sup>/680)<sup>0.5</sup> = <b>13,7 m/s</b>; Quãng "
               "đường đi được = (2 × 13,7<sup>2</sup> × "
               "3/9,81)<sup>0.5</sup> = <b>10,7 m (lấy 11 m)</b>. Tâm vũng "
               "nằm cách điểm thẳng đứng bên dưới lỗ rò 11 m."))
    b.append(p("Với R<sup>0.2</sup> = 15, Phương trình 4.23 cho A = (5,65 "
               "× 10<sup>2</sup> × 4 × "
               "10<sup>−5</sup> [680 × 2 × "
               "10<sup>2</sup>]<sup>0.5</sup> × 15)/(0,71 × 68) = "
               "<b>81,2 m² (lấy 82 m²)</b>. Ở kích thước đó Hình 4.3 cho "
               "R<sup>0.2</sup> khoảng 17; giải lại được <b>A = 93 m²</b>, suy "
               "ra <b>d = 11 m</b>."))
    b.append(note("<b>Lưu ý về lỗi in.</b> Trong phép thay vào tính vận tốc, "
                  "bản in dùng 10<sup>5</sup> thay vì 2 × "
                  "10<sup>5</sup> N/m² nhưng vẫn cho 13,7 m/s; trong phép tính "
                  "diện tích vũng bản in viết [680 × 2 × "
                  "10<sup>2</sup>]<sup>0.5</sup>, rõ ràng là lỗi gõ của "
                  "10<sup>5</sup>. Các giá trị in được giữ nguyên."))
    b.append(p("Phương trình 4.26 cho X = [(5,8 × "
               "10<sup>−2</sup> × 9,6 × 0,71 × "
               "295)/(1 × 17)]<sup>1.14</sup> = <b>9 m</b>. Do vũng và "
               "tia chất lỏng, tồn tại khu vực nguy hiểm cao 9 m trong vòng "
               "tròn bán kính 26 m tính từ điểm trên mặt đất thẳng đứng bên "
               "dưới lỗ rò."))
    b.append(p("Xét đến khả năng tạo sương mù do toàn bộ lượng rò hóa hơi vì "
               "áp suất cao. Vận tốc 13,7 m/s là khá thấp nên gió chi phối sự "
               "phân tán; coi toàn bộ lượng rò hóa hơi và dùng Phương trình "
               "4.7: X = 10,8 [0,53 × 295/(68 × 1)]<sup>0.55</sup> "
               "= <b>17 m</b>. Vì khu vực chạm mặt đất, nhân thêm 1,5: "
               "<b>X = 26 m</b>."))
    b.append(p("Kết quả cuối cùng là bán kính nằm ngang <b>26 m</b> đến độ "
               "cao <b>10 m</b>, với một phần hình cầu bán kính 26 m ở phía "
               "trên; đây là kết quả rất nặng nhưng cần thiết khi không biết "
               "hình học của lỗ rò."))
    b.append(h3("4.3 Phát thải chất lỏng ở nhiệt độ cao hơn điểm sôi khí quyển",
                "4.3 Release of liquid above its atmospheric boiling point"))
    b.append(p("Đây là tình huống 'ngoài trời' thứ ba và cuối cùng, xét vật "
               "liệu dễ cháy ở dạng hơi trong điều kiện môi trường bình thường "
               "nhưng được giữ ở dạng lỏng nhờ áp suất chứa. Khi rò ra, một "
               "phần chất lỏng bay hơi và năng lượng cần cho sự bay hơi đó làm "
               "nhiệt độ của phần còn lại giảm xuống, nên sự bay hơi tiếp theo "
               "chỉ xảy ra khi nhận nhiệt từ môi trường. Người ta giả định "
               "mức nhận nhiệt này không đáng kể trong suốt thời gian tồn tại "
               "của tia, nhưng rất nhanh khi chất lỏng chạm mặt đất; do quãng "
               "đường đi từ điểm rò tới mặt đất rất ngắn, sự bay hơi được coi "
               "là tức thời khi chạm đất."))
    b.append(p("Trước hết cần tính lượng chất lỏng bay hơi đột thời (flash) "
               "tại điểm rò, dù giá trị này thường không cần thiết để tính "
               "khu vực nguy hiểm ngay tại điểm rò. Phần bay hơi phụ thuộc vào "
               "nhiệt dung riêng của vật liệu (lượng nhiệt có thể dùng trước "
               "khi nhiệt độ hạ tới điểm sôi), nhiệt ẩn hóa hơi (nhiệt cần để "
               "hóa hơi) và hiệu giữa điểm sôi với nhiệt độ thực tế của chất "
               "lỏng (lượng nhiệt sẵn có):"))
    b.append(eq("Fraction of liquid vaporizing = [(T<sub>1</sub> − T<sub>b</sub>)/δ] C<sub>l</sub>", "4.27"))
    b.append(p("trong đó T<sub>1</sub> = nhiệt độ phát thải của chất lỏng, K; "
               "T<sub>b</sub> = điểm sôi của chất lỏng, K; δ = nhiệt ẩn "
               "hóa hơi, kJ/kg; C<sub>l</sub> = nhiệt dung riêng của chất "
               "lỏng, kJ/kg/K."))
    b.append(p("Có một vấn đề là sương mù chất lỏng có thể hình thành do bản "
               "chất của phát thải. Khi đó phạm vi khu vực nguy hiểm do phát "
               "thải được nhân với <b>1,5</b>, trừ khi cách làm đó hóa hơi "
               "toàn bộ lượng rò — khi ấy giả định toàn bộ lượng rò hóa hơi."))
    b.append(p("Việc rò chất lỏng cũng phức tạp hơn vì có thể xảy ra bay hơi "
               "ngay trong đường rò nếu đường rò dài, làm giảm lượng vật liệu "
               "thoát ra. Điều này được coi là xảy ra khi chiều dài đường rò "
               "lớn hơn <b>10 lần đường kính hiệu dụng</b> (với lỗ không tròn, "
               "đường kính = [4 × diện tích/π]<sup>0.5</sup>). Ở mức "
               "đó trở lên, phương trình phát thải được chỉnh sửa: giữ nguyên "
               "dạng Phương trình 4.13 nhưng thay áp suất khí quyển bằng "
               "P<sub>c</sub> = <b>0,55 × áp suất hơi bão hòa</b> của "
               "chất lỏng chứa ở nhiệt độ công nghệ. Giá trị này có thể khác "
               "áp suất chứa thực tế nếu có tạo áp bên ngoài, nhưng thường thì "
               "vật liệu được giữ ở dạng lỏng chính nhờ áp suất hơi của nó. "
               "Ngoài ra, mật độ của hỗn hợp lỏng–hơi thoát ra là mật độ tổng "
               "hợp của hai thành phần."))
    b.append(eq("G = 0.8 A [2 σ<sub>m</sub> (P<sub>1</sub> − P<sub>c</sub>)]<sup>0.5</sup> kg/s", "4.28"))
    b.append(p("trong đó A = diện tích tiết diện lỗ rò, m²; σ<sub>m</sub> "
               "= mật độ hỗn hợp thoát ra, kg/m³; P<sub>1</sub> = áp suất "
               "chứa, N/m²; P<sub>c</sub> = 0,55 × áp suất hơi, N/m²."))
    b.append(p("Để tính σ<sub>m</sub>, cần xét điều kiện tại áp suất "
               "P<sub>c</sub>, tức cần có đường cong áp suất hơi của vật liệu. "
               "Từ đó tìm nhiệt độ T<sub>c</sub> tại đó áp suất hơi bằng "
               "P<sub>c</sub>. Phần lượng rò thoát ra dưới dạng hơi khi đó là:"))
    b.append(eq("M<sub>g</sub> = (T<sub>1</sub> − T<sub>c</sub>) C<sub>l</sub> / L", "4.29"))
    b.append(p("trong đó M<sub>g</sub> = phần khối lượng phát thải là hơi; "
               "T<sub>1</sub> = nhiệt độ công nghệ, K; T<sub>c</sub> = nhiệt "
               "độ ứng với P<sub>c</sub>, K; C<sub>l</sub> = nhiệt dung riêng "
               "của chất lỏng, kJ/kg/K; L = nhiệt ẩn hóa hơi, kJ/kg."))
    b.append(p("Từ đó tính mật độ của hỗn hợp:"))
    b.append(eq("σ<sub>m</sub> = 1 / [(M<sub>g</sub>/σ<sub>v</sub>) + ((1 − M<sub>g</sub>)/σ<sub>l</sub>)] kg/m<sup>3</sup>", "4.30"))
    b.append(p("trong đó σ<sub>m</sub> = mật độ hỗn hợp thoát ra; "
               "σ<sub>v</sub> = mật độ hơi ở T<sub>1</sub>; "
               "σ<sub>l</sub> = mật độ chất lỏng ở T<sub>1</sub>. Các "
               "kết quả này cho phép tính vận tốc phát thải cùng lượng chất "
               "lỏng trong tia; tia được xử lý bằng Phương trình 4.14, 4.15 "
               "hoặc 4.16 tùy trường hợp. Lượng chất lỏng tới mặt đất được "
               "giả định bay hơi tức thời và phạm vi khu vực nguy hiểm do hơi "
               "này được tính bằng Phương trình 4.7, có hiệu chỉnh cho nguồn "
               "điểm thấp."))
    b.append(h4("4.3.1 Ví dụ về phát thải chất lỏng ở nhiệt độ cao hơn điểm sôi khí quyển",
                "4.3.1 Example of liquid release above its atmospheric boiling point"))
    b.append(p("<b>Ví dụ 5.</b> Propylene lỏng được chứa trong bình ở 15 °C "
               "và áp suất bằng áp suất hơi của chính nó ở nhiệt độ đó. Chất "
               "lỏng rò xuống một đường thoát có đường kính trong 0,019 m "
               "(diện tích 2,8 × 10<sup>−4</sup> m²) và dài 0,3 m. "
               "Số liệu: áp suất chứa (áp suất hơi) 8,94 × "
               "10<sup>5</sup> N/m²; nhiệt độ công nghệ 288 K; điểm sôi 225 K; "
               "nhiệt độ ứng với P<sub>c</sub> là 267 K; nhiệt ẩn hóa hơi 469 "
               "kJ/kg; nhiệt dung riêng chất lỏng ở 288 K là 2,26 kJ/kg/K; "
               "mật độ chất lỏng 520 kg/m³; mật độ hơi 9,43 kg/m³; khối lượng "
               "phân tử 42; LEL 2 % trong không khí."))
    b.append(p("Do 0,3/0,019 &gt; 10 nên bay hơi xảy ra ngay trong đường rò "
               "và chất thoát ra là hỗn hợp hơi–lỏng. Trước hết tính phần "
               "hóa hơi trong đường rò theo Phương trình 4.29: M<sub>g</sub> = "
               "(288 − 267) × 2,26/469 = <b>0,1</b>."))
    b.append(p("Dùng phân số đó trong Phương trình 4.30: σ<sub>m</sub> = "
               "1/[(0,1/9,43) + (0,9/520)] = <b>81,3 kg/m³</b>."))
    b.append(p("Phần bay hơi đột thời trong và ngay ngoài lỗ rò theo Phương "
               "trình 4.27: (288 − 225) × 2,26/469 = <b>0,304</b>."))
    b.append(p("Áp suất P<sub>c</sub> = 0,55 × 8,94 × "
               "10<sup>5</sup> = <b>4,92 × 10<sup>5</sup> N/m²</b>. Dùng "
               "mật độ hỗn hợp trong Phương trình 4.28: G = 0,8 × 2,8 "
               "× 10<sup>−4</sup> [2 × 81,3 (8,94 × "
               "10<sup>5</sup> − 4,92 × 10<sup>5</sup>)]<sup>0.5</sup> "
               "= <b>1,81 kg/s</b>."))
    b.append(p("Lượng xuất hiện dưới dạng hơi tại miệng lỗ và bay hơi đột "
               "thời ngay sau đó theo Phương trình 4.27: G<sub>v</sub> = 1,81 "
               "(288 − 225) 2,26/469 = <b>0,55 kg/s</b>. Lượng chất "
               "lỏng giả định tới mặt đất: G<sub>l</sub> = 1,81 − 0,55 = "
               "<b>1,26 kg/s</b>."))
    b.append(p("Phần hóa hơi tại lỗ rò được xử lý như hơi và phân tán theo "
               "tia, Phương trình 4.6: X = 2,1 × 10<sup>3</sup> "
               "(0,56/2<sup>2</sup> × 42<sup>1.5</sup> × "
               "288<sup>0.5</sup>)<sup>0.5</sup> = <b>11,5 m (lấy 12 m)</b>. "
               "Do bản chất phát thải, giả định có sương mù và tăng khoảng "
               "cách thêm 50 %: <b>X = 18 m</b>."))
    b.append(p("Lượng chất lỏng tới mặt đất được giả định bay hơi ngay lập "
               "tức nên không tạo vũng; hơi phân tán theo gió, dùng Phương "
               "trình 4.7 và không cộng hệ số sương mù: X = 10,8 (1,29 × "
               "288/(42 × 2))<sup>0.55</sup> = <b>24,5 m</b>."))
    b.append(note("<b>Lưu ý về lỗi in.</b> Phép thay vào Phương trình 4.6 dùng "
                  "0,56 kg/s trong khi giá trị hơi đã tính là 0,55 kg/s; phép "
                  "thay vào Phương trình 4.7 dùng 1,29 kg/s trong khi lượng "
                  "chất lỏng đã tính là 1,26 kg/s. Các con số in được giữ "
                  "nguyên."))
    b.append(p("Kết quả: trong mặt phẳng nằm ngang có khu vực nguy hiểm kéo "
               "dài <b>24,5 m</b> cộng với quãng đường tia đi trước khi chạm "
               "đất; quanh nguồn rò có khu vực nguy hiểm kéo dài <b>18 m</b> "
               "theo mọi hướng phía trên phương ngang, được chiếu thẳng đứng "
               "xuống khu vực nguy hiểm trên mặt đất."))
    return "".join(b)


def body_en():
    b = []
    b.append(h4("4.2.1 Example of liquid release below its atmospheric boiling point",
                "4.2.1 Example of liquid release below its atmospheric boiling point"))
    b.append(p("<b>Example 3.</b> Acetone is transported in a pipe with normal "
               "flanged joints at 22 °C and at a gauge pressure of "
               "10<sup>5</sup> N/m². A failure in one of the flanged joints "
               "presents an orifice of 4 × 10<sup>−5</sup> m²; the "
               "pipe is some 3 m off the ground. Relevant parameters of "
               "acetone are: liquid density 791 kg/m³; vapour density 2.58 "
               "kg/m³; boiling point 56 °C; partial pressure at 22 °C "
               "of 2.2 × 10<sup>4</sup> N/m² (0.22 atm); molecular "
               "weight 58; lower explosive limit (LEL) 2.1 % in air."))
    b.append(p("First calculate the rate of liquid release from the leak "
               "using Equation 4.13: G = 1.13 × 4 × "
               "10<sup>−5</sup> (791 × 10<sup>5</sup>)<sup>0.5</sup> "
               "= <b>0.4 kg/s</b>. In calculating the extents of hazardous "
               "areas, the first assumption is that the liquid reaches the "
               "ground without evaporation. The velocity of the jet is taken "
               "from Equation 4.17 and the distance from Equation 4.15, "
               "assuming the leak to be horizontal."))
    b.append(p("Velocity of jet = 1.13 (10<sup>5</sup>/791)<sup>0.5</sup> = "
               "<b>12.7 m/s</b>. Distance travelled = (2 × "
               "12.7<sup>2</sup> × 3/9.81)<sup>0.5</sup>; Distance = "
               "<b>9.93 m (say 10 m)</b>."))
    b.append(note("<b>Printed-value note.</b> The distance calculation gives "
                  "9.93 m (rounded to 10 m), but the following sentence "
                  "places the centre of the pool at 9.85 m from the point "
                  "vertically below the leak. Both figures are retained as "
                  "printed."))
    b.append(p("A pool will form and, unless physically contained, grow until "
               "the vaporization from its surface equals the leakage rate "
               "from the orifice. Using Equation 4.23 with a trial "
               "R<sup>0.2</sup> = 15: A = (5.65 × 10<sup>2</sup> × "
               "4 × 10<sup>−5</sup> [791 × "
               "10<sup>5</sup>]<sup>0.5</sup> × 15)/(0.22 × 58) "
               "m². At this pool size Figure 4.3 gives R<sup>0.2</sup> around "
               "19; repeating the calculation gives <b>A = 299 m²</b> and a "
               "pool diameter <b>d = 22 m</b>."))
    b.append(p("The extent beyond the edge of, and above, the pool is given "
               "by Equation 4.26: X = [(5.8 × 10<sup>−2</sup> "
               "× 17.3 × 0.22 × 295)/(2.1 × "
               "19)]<sup>1.14</sup> = <b>1.75 m (say 2 m)</b>."))
    b.append(p("The second assumption, that the entire release forms a mist, "
               "can be ignored here because the driving pressure is so low. "
               "There will be no significant hazardous area at the pipe where "
               "the leak occurs; from the point on the ground vertically "
               "below the leak there will be a hazardous area <b>2 m</b> high "
               "to a radius of <b>22 m</b> (10 + 10 + 2) in all directions."))
    b.append(p("<b>Example 4.</b> With the same transmission system and leak "
               "orifice as in Example 3, isoprene is transported at a gauge "
               "pressure of 2 × 10<sup>5</sup> N/m² and a temperature of "
               "22 °C. Relevant parameters: liquid density 680 kg/m³; "
               "vapour density 3 kg/m³; boiling point 34 °C; partial "
               "pressure 7.1 × 10<sup>4</sup> N/m² (0.71 atm); molecular "
               "weight 68; LEL 1 % in air."))
    b.append(p("The initial approach is the same as in Example 3: determine "
               "the mass rate of liquid release using Equation 4.13, G = "
               "1.13 × 4 × 10<sup>−5</sup> [680 × 2 "
               "× 10<sup>5</sup>]<sup>0.5</sup> = <b>0.53 kg/s</b>."))
    b.append(p("From Equations 4.17 and 4.15: Velocity of jet = 1.13 "
               "(10<sup>5</sup>/680)<sup>0.5</sup> = <b>13.7 m/s</b>; Distance "
               "travelled = (2 × 13.7<sup>2</sup> × "
               "3/9.81)<sup>0.5</sup> = <b>10.7 m (say 11 m)</b>. The centre "
               "of the pool is 11 m from the point on the ground vertically "
               "below the leak orifice."))
    b.append(p("With R<sup>0.2</sup> = 15, Equation 4.23 gives A = (5.65 "
               "× 10<sup>2</sup> × 4 × "
               "10<sup>−5</sup> [680 × 2 × "
               "10<sup>2</sup>]<sup>0.5</sup> × 15)/(0.71 × 68) = "
               "<b>81.2 m² (say 82 m²)</b>. At this pool size Figure 4.3 gives "
               "R<sup>0.2</sup> around 17; solving again gives <b>A = 93 "
               "m²</b>, hence <b>d = 11 m</b>."))
    b.append(note("<b>Printed-error note.</b> In the velocity substitution the "
                  "book writes 10<sup>5</sup> instead of 2 × "
                  "10<sup>5</sup> N/m² yet still obtains 13.7 m/s; in the "
                  "pool-area substitution it prints [680 × 2 × "
                  "10<sup>2</sup>]<sup>0.5</sup>, plainly a typo for "
                  "10<sup>5</sup>. The printed values are retained."))
    b.append(p("Equation 4.26 gives X = [(5.8 × 10<sup>−2</sup> "
               "× 9.6 × 0.71 × 295)/(1 × "
               "17)]<sup>1.14</sup> = <b>9 m</b>. Owing to the pool and liquid "
               "jet there is a hazardous area 9 m high within a circle of "
               "radius 26 m from the point on the ground vertically below the "
               "leak orifice."))
    b.append(p("Consider now the possibility of a mist comprising all of the "
               "released liquid because of the pressure. A velocity of 13.7 "
               "m/s is fairly low, so wind will play a large part in "
               "dispersion; assume total vaporization and use Equation 4.7: "
               "X = 10.8 [0.53 × 295/(68 × 1)]<sup>0.55</sup> = "
               "<b>17 m</b>. As the hazardous area touches the ground, "
               "multiply by 1.5: <b>X = 26 m</b>."))
    b.append(p("The final result is a horizontal radius of <b>26 m</b> to a "
               "height of <b>10 m</b>, with a partial sphere of radius 26 m "
               "above it; this is a very onerous result but a necessary one "
               "in the absence of knowledge of the release orifice geometry."))
    b.append(h3("4.3 Release of liquid above its atmospheric boiling point",
                "4.3 Release of liquid above its atmospheric boiling point"))
    b.append(p("This is the final one of the three 'outdoor' scenarios and "
               "addresses a situation where the flammable material would be "
               "a vapour in normal ambient circumstances but is maintained "
               "as a liquid by the containment pressure. On release some of "
               "the liquid evaporates and the energy needed for that "
               "evaporation so lowers the temperature of the remainder that "
               "further evaporation occurs only as it gains heat from its "
               "environment. This gain is assumed insignificant during the "
               "'jet' life but rapid as soon as the liquid contacts the "
               "ground; because the travel distance to the ground is short, "
               "evaporation is taken to be instantaneous on contact."))
    b.append(p("The first necessity is to calculate the amount of liquid that "
               "flashes off as vapour at the point of release, although this "
               "is not normally needed for the hazardous area at the point "
               "of release. The flashing fraction is based upon the heat "
               "capacity of the material (the heat available before the "
               "temperature falls to boiling point), the latent heat of "
               "vaporization (the heat required to vaporize it) and the "
               "difference between the boiling point and the actual "
               "temperature of the liquid:"))
    b.append(eq("Fraction of liquid vaporizing = [(T<sub>1</sub> − T<sub>b</sub>)/δ] C<sub>l</sub>", "4.27"))
    b.append(p("where T<sub>1</sub> = release temperature of liquid, K; "
               "T<sub>b</sub> = boiling point of liquid, K; δ = latent "
               "heat of vaporization, kJ/kg; C<sub>l</sub> = liquid heat "
               "capacity, kJ/kg/K."))
    b.append(p("There is a problem in that mist may be formed by the nature "
               "of the release: the hazardous area created by the release is "
               "then multiplied by <b>1.5</b> to allow for this, unless that "
               "would vaporize the whole of the release, in which case total "
               "vaporization is assumed."))
    b.append(p("The release is also more complicated because vaporization can "
               "take place in the leak path if it is long, reducing the amount "
               "of material released. This is said to occur where the length "
               "of the leak path exceeds <b>10 times the effective diameter</b> "
               "(for a non-circular orifice, diameter = [4 × "
               "area/π]<sup>0.5</sup>). At and above this figure the release "
               "equation is modified: the form of Equation 4.13 is retained "
               "but atmospheric pressure is replaced by P<sub>c</sub> = "
               "<b>0.55 × the saturated vapour pressure</b> of the "
               "contained liquid at process temperature. This may differ from "
               "the actual containment pressure if external pressurization is "
               "used, but normally the material is maintained as a liquid by "
               "its own vapour pressure. In addition, the density of the "
               "released mixture of liquid and vapour is the composite of the "
               "two elements of the mixture."))
    b.append(eq("G = 0.8 A [2 σ<sub>m</sub> (P<sub>1</sub> − P<sub>c</sub>)]<sup>0.5</sup> kg/s", "4.28"))
    b.append(p("where A = cross-sectional area of leak, m²; σ<sub>m</sub> "
               "= density of released mixture, kg/m³; P<sub>1</sub> = "
               "containment pressure, N/m²; P<sub>c</sub> = 0.55 × "
               "vapour pressure, N/m²."))
    b.append(p("To calculate σ<sub>m</sub> it is necessary to investigate "
               "the conditions at P<sub>c</sub>, which requires the vapour "
               "pressure curve for the material. From this a value is obtained "
               "for T<sub>c</sub>, the temperature at which a vapour pressure "
               "of P<sub>c</sub> would be exerted. The fraction of the release "
               "that emerges as vapour is then:"))
    b.append(eq("M<sub>g</sub> = (T<sub>1</sub> − T<sub>c</sub>) C<sub>l</sub> / L", "4.29"))
    b.append(p("where M<sub>g</sub> = fraction of mass release which is vapour; "
               "T<sub>1</sub> = process temperature, K; T<sub>c</sub> = "
               "temperature giving P<sub>c</sub>, K; C<sub>l</sub> = heat "
               "capacity of liquid, kJ/kg/K; L = latent heat of vaporization, "
               "kJ/kg."))
    b.append(p("This allows the density of the mixture to be calculated:"))
    b.append(eq("σ<sub>m</sub> = 1 / [(M<sub>g</sub>/σ<sub>v</sub>) + ((1 − M<sub>g</sub>)/σ<sub>l</sub>)] kg/m<sup>3</sup>", "4.30"))
    b.append(p("where σ<sub>m</sub> = density of released mixture; "
               "σ<sub>v</sub> = density of vapour at T<sub>1</sub>; "
               "σ<sub>l</sub> = density of liquid at T<sub>1</sub>. The "
               "results give the velocity of release together with the amount "
               "of liquid in the jet. This jet can then be treated using "
               "Equations 4.14, 4.15 or 4.16 as appropriate. The amount of "
               "liquid reaching the ground is then assumed to evaporate "
               "instantly, and the extent of the hazardous area due to this "
               "calculated using Equation 4.7, corrected for a low-level "
               "point source."))
    b.append(h4("4.3.1 Example of liquid release above its atmospheric boiling point",
                "4.3.1 Example of liquid release above its atmospheric boiling point"))
    b.append(p("<b>Example 5.</b> Liquid propylene is contained in a vessel at "
               "15 °C and a pressure equal to its own vapour pressure at "
               "that temperature. It leaks down a drain line of 0.019 m bore "
               "(2.8 × 10<sup>−4</sup> m² area) and 0.3 m length. "
               "Basic information: storage pressure (vapour pressure) 8.94 "
               "× 10<sup>5</sup> N/m²; process temperature 288 K; "
               "material boiling point 225 K; temperature giving P<sub>c</sub> "
               "267 K; latent heat of vaporization 469 kJ/kg; heat capacity of "
               "liquid at 288 K 2.26 kJ/kg/K; liquid density 520 kg/m³; vapour "
               "density 9.43 kg/m³; molecular weight 42; LEL 2 % in air."))
    b.append(p("Since 0.3/0.019 &gt; 10, vaporization will take place within "
               "the leak path and the fluid leaking will be a mixture of "
               "vapour and liquid. First calculate the fraction vaporizing in "
               "the leak path from Equation 4.29: M<sub>g</sub> = (288 − "
               "267) × 2.26/469 = <b>0.1</b>."))
    b.append(p("Using this fraction in Equation 4.30: σ<sub>m</sub> = "
               "1/[(0.1/9.43) + (0.9/520)] = <b>81.3 kg/m³</b>."))
    b.append(p("The fraction flashing off as vapour inside and just outside "
               "the release orifice, from Equation 4.27: (288 − 225) "
               "× 2.26/469 = <b>0.304</b>."))
    b.append(p("P<sub>c</sub> = 0.55 × 8.94 × 10<sup>5</sup> = "
               "<b>4.92 × 10<sup>5</sup> N/m²</b>. Using the mixture "
               "density in Equation 4.28: G = 0.8 × 2.8 × "
               "10<sup>−4</sup> [2 × 81.3 (8.94 × "
               "10<sup>5</sup> − 4.92 × 10<sup>5</sup>)]<sup>0.5</sup> "
               "= <b>1.81 kg/s</b>."))
    b.append(p("The amount appearing as vapour at the outside of the orifice "
               "and flashing off immediately afterwards, from Equation 4.27: "
               "G<sub>v</sub> = 1.81 (288 − 225) 2.26/469 = <b>0.55 "
               "kg/s</b>. The liquid assumed to reach the ground: G<sub>l</sub> "
               "= 1.81 − 0.55 = <b>1.26 kg/s</b>."))
    b.append(p("The vapour formed at the orifice behaves as a vapour and is "
               "jet dispersed according to Equation 4.6: X = 2.1 × "
               "10<sup>3</sup> (0.56/2<sup>2</sup> × 42<sup>1.5</sup> "
               "× 288<sup>0.5</sup>)<sup>0.5</sup> = <b>11.5 m (say 12 "
               "m)</b>. Due to the nature of the release some mist is assumed "
               "and the distance is increased by 50 %: <b>X = 18 m</b>."))
    b.append(p("The liquid reaching the ground is assumed to vaporize "
               "immediately, so no pool forms; the vapour is wind dispersed "
               "using Equation 4.7, with no mist allowance: X = 10.8 (1.29 "
               "× 288/(42 × 2))<sup>0.55</sup> = <b>24.5 m</b>."))
    b.append(note("<b>Printed-error note.</b> The substitution in Equation 4.6 "
                  "uses 0.56 kg/s where the calculated vapour rate is 0.55 "
                  "kg/s; the substitution in Equation 4.7 uses 1.29 kg/s where "
                  "the calculated liquid rate is 1.26 kg/s. The printed "
                  "figures are retained."))
    b.append(p("The result is a hazardous area extending <b>24.5 m</b> plus "
               "the distance travelled by the jet before it reaches the "
               "ground in a horizontal plane, and a hazardous area around the "
               "source of release extending <b>18 m</b> in all above-horizontal "
               "directions, projected vertically down to the ground hazard."))
    return "".join(b)
