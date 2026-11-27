# -*- coding: utf-8 -*-
"""Chapter 4, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 107-112 (PDF pp. 128-133).

Covers Section 4.2 (release of liquid below its atmospheric boiling
point): the liquid-orifice and jet-trajectory relations, Eqs. 4.13-4.21
and 4.23-4.26, Table 4.2 and Fig. 4.3. Equation 4.22 is absent from the
printed sequence and the gap is flagged rather than filled. The
integration module owns the page shell, sources and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, p, note, eq, fig, table
import mcmillanfig04_a as F


# Table 4.2 - boiling-point column plus the five ambient-temperature columns.
_T42_HEAD_VI = ["Nhiệt độ sôi của chất lỏng (°C)",
                "T<sub>a</sub> = 32 °C", "T<sub>a</sub> = 40 °C",
                "T<sub>a</sub> = 60 °C", "T<sub>a</sub> = 80 °C",
                "T<sub>a</sub> = 100 °C"]
_T42_HEAD_EN = ["Liquid boiling point (°C)",
                "T<sub>a</sub> = 32 °C", "T<sub>a</sub> = 40 °C",
                "T<sub>a</sub> = 60 °C", "T<sub>a</sub> = 80 °C",
                "T<sub>a</sub> = 100 °C"]
_T42_ROWS = [
    ["35 °C", "0.96", "1", "1", "1", "1"],
    ["40 °C", "0.76", "1", "1", "1", "1"],
    ["50 °C", "0.54", "0.72", "1", "1", "1"],
    ["60 °C", "0.38", "0.56", "1", "1", "1"],
    ["70 °C", "0.26", "0.42", "0.72", "1", "1"],
    ["80 °C", "0.18", "0.3", "0.56", "1", "1"],
    ["90 °C", "0.13", "0.2", "0.42", "0.72", "1"],
    ["100 °C", "0.092", "0.14", "0.3", "0.56", "1"],
    ["110 °C", "0.062", "0.1", "0.2", "0.42", "0.72"],
    ["120 °C", "0.042", "0.072", "0.14", "0.3", "0.56"],
    ["130 °C", "0.028", "0.058", "0.1", "0.2", "0.42"],
    ["140 °C", "0.018", "0.027", "0.072", "0.14", "0.3"],
    ["150 °C", "0.01", "0.018", "0.058", "0.1", "0.2"],
]


def body_vi():
    b = []
    b.append(h3("4.2 Phát thải chất lỏng dưới điểm sôi khí quyển",
                "4.2 Release of liquid below its atmospheric boiling point"))
    b.append(p("Chất lỏng thoát ra từ một lỗ tiết khi còn dưới điểm sôi khí quyển sẽ "
               "tạo thành tia phun, hoặc thành sương mù chất lỏng nếu áp suất thượng "
               "lưu đủ cao. Công thức cổ điển cho dòng chất lỏng qua lỗ tiết hay đầu "
               "phun là:"))
    b.append(eq("G = C a [2 σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> kg/s"))
    b.append(p("trong đó G = lượng phát thải theo khối lượng, kg/s; a = diện tích lỗ "
               "tiết, m²; P = áp suất thượng lưu, N/m²; C = hệ số lưu lượng; "
               "σ<sub>l</sub> = mật độ chất lỏng ở điều kiện khí quyển, kg/m³. "
               "Như trước đây, C có giá trị lớn nhất khoảng 0,8, nên phương trình trở "
               "thành:"))
    b.append(eq("G = 1.13 a [σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> kg/s", "4.13"))
    b.append(p("Nếu không tạo sương mù thì không có khu vực nguy hiểm đáng kể bao "
               "quanh điểm rò (trừ khi chất lỏng được chứa giữ ngay tại chỗ rò). Tia "
               "chất lỏng thoát khỏi lỗ tiết và tạo vũng khi chạm sàn hoặc mặt đất. "
               "Thời gian tia bay tới mặt đất có thể tính từ các định luật chuyển động "
               "của Newton. Với tia phun ở góc Φ tính từ phương ngang, dùng "
               "v = u + a t với vận tốc thẳng đứng cuối bằng không tại đỉnh:"))
    b.append(p("Thay Φ bằng góc phát thải tính từ phương ngang, g = 9,81 m/s² là "
               "gia tốc trọng trường và t<sub>1</sub> là thời gian tới đỉnh của tia:"))
    b.append(eq("v sin Φ − g t<sub>1</sub> = 0"))
    b.append(eq("t<sub>1</sub> = v sin Φ/g"))
    b.append(p("Dùng hệ thức v² = u² + 2gS, với S là độ cao đỉnh tia tính từ điểm "
               "phát thải:"))
    b.append(eq("(v sin Φ)<sup>2</sup> − 2 g S = 0"))
    b.append(eq("S = (v sin Φ)<sup>2</sup>/2g"))
    b.append(p("Nếu điểm phát thải ở độ cao h thì tổng độ cao là [h + (v sin Φ)²/2g]; "
               "từ S = u t + 0,5 g t² với u = 0:"))
    b.append(eq("[h + (v sin Φ)<sup>2</sup>/2g] = 0.5 g t<sub>2</sub><sup>2</sup>"))
    b.append(eq("t = [(2gh + v<sup>2</sup> sin<sup>2</sup>Φ)<sup>0.5</sup> + v sin Φ]/g"))
    b.append(p("Với thành phần vận tốc nằm ngang là v cos Φ và bỏ qua ma sát không "
               "khí, quãng đường tia đi được là:"))
    b.append(eq("X = v cos Φ [(2gh + v<sup>2</sup> sin<sup>2</sup>Φ)<sup>0.5</sup> + v sin Φ]/g m", "4.14"))
    b.append(p("Khi tia nằm ngang, sin Φ = 0 và cos Φ = 1, phương trình rút "
               "gọn thành:"))
    b.append(eq("X = (2 v<sup>2</sup> h/g)<sup>0.5</sup> m", "4.15"))
    b.append(p("Nên dùng phương trình rút gọn này bất cứ khi nào không xác định được "
               "hướng tia: các phương trình là lý tưởng hóa và tia thực khó có thể "
               "lý tưởng, nên kết quả chỉ là ước lượng. Do nhiễu loạn của tia không "
               "đạt tới lỗ tiết lý tưởng, giá trị nằm ngang trong đa số trường hợp "
               "sẽ lớn hơn quãng đường thực xảy ra. Nếu không đúng như vậy, phải lấy "
               "đạo hàm Phương trình 4.14 để tìm góc cho quãng đường cực đại rồi đưa "
               "góc đó trở lại Phương trình 4.14."))
    b.append(p("Khi tia hướng xuống dưới góc nằm ngang, phương trình trở thành:"))
    b.append(eq("X = v cos Φ [(v sin Φ − 2gh)<sup>0.5</sup> − v sin Φ]/g m", "4.16"))
    b.append(p("Từ Phương trình 4.13 chia cho σ<sub>l</sub> a, vận tốc phát thải là:"))
    b.append(eq("Velocity = 1.13 [(P − 10<sup>5</sup>)/σ<sub>l</sub>]<sup>0.5</sup> m/s", "4.17"))
    b.append(p("Tại điểm tia chạm đất sẽ hình thành vũng; nếu không được chứa giữ cơ "
               "lý, vũng lớn dần cho đến khi tốc độ bay hơi từ mặt vũng bằng tốc độ "
               "rò từ lỗ tiết. Tốc độ bay hơi từ vũng được cho bởi:"))
    b.append(eq("G = A k<sub>g</sub> Δp M kg/s", "4.18"))
    b.append(p("trong đó G = tốc độ hóa hơi, kg/s; A = diện tích vũng, m²; Δp = "
               "áp suất riêng phần của hơi trên mặt chất lỏng, tính theo phần của áp "
               "suất khí quyển; k<sub>g</sub> = hệ số truyền khối tổng. Dùng Phương "
               "trình 4.4 để đổi sang tốc độ hóa hơi theo thể tích:"))
    b.append(eq("Q = 8.2 A k<sub>g</sub> Δp T/10<sup>2</sup> m<sup>3</sup>/s", "4.19"))
    b.append(p("Áp suất riêng phần của hơi trên chất lỏng còn gọi là áp suất hơi; dưới "
               "điểm sôi nó là một phần của áp suất khí quyển, đồng thời cho biết tỷ "
               "lệ hơi trên không khí. Khi chưa biết giá trị này, thường có thể ước "
               "lượng bằng Bảng 4.2, trong đó áp suất hơi (riêng phần) được tính "
               "thành phần của áp suất khí quyển:"))
    b.append(table(_T42_HEAD_VI, _T42_ROWS,
                   "Bảng 4.2 · Áp suất hơi (áp suất riêng phần) của chất lỏng ở các "
                   "nhiệt độ môi trường khác nhau"))
    b.append(note("<b>Ghi chú 1.</b> Các giá trị trong bảng chỉ là xấp xỉ. "
                  "<b>Ghi chú 2.</b> T<sub>a</sub> là nhiệt độ môi trường. "
                  "<b>Ghi chú 3.</b> Số liệu điển hình cho các hydrocarbon; các vật "
                  "liệu khác nhìn chung có giá trị thấp hơn."))
    b.append(note("<b>Lưu ý về áp suất riêng phần.</b> Các số liệu này lấy từ chuyên "
                  "khảo của Lippincott và Lyman. Nếu biết áp suất riêng phần thực tế "
                  "thì phải dùng giá trị đó, vì phép ước lượng đơn giản cho kết quả "
                  "cao hơn giá trị thực — đúng với cách ước lượng dùng xuyên suốt "
                  "cuốn sách."))
    b.append(p("Hệ số truyền khối k<sub>g</sub> được tìm từ công thức sau, trong đó "
               "β là số Schmidt (độ nhớt động học chia cho độ khuếch tán của hơi "
               "trong không khí), R là số Reynolds và G<sub>m</sub> là lưu lượng khối "
               "lượng của không khí, kg-mol/s:"))
    b.append(eq("k<sub>g</sub> = 3.6 × 10<sup>−2</sup> G<sub>m</sub>/(β<sup>0.67</sup> R<sup>0.2</sup> M)", "4.20"))
    b.append(p("Công thức kinh điển cho số Reynolds là R = v d σ/τ, với v = "
               "vận tốc không khí, d = kích thước đặc trưng, σ = mật độ không "
               "khí và τ = độ nhớt tuyệt đối của không khí:"))
    b.append(eq("R = v d σ/τ"))
    b.append(p("Dùng độ nhớt động học ν&#770; (m²/s), công thức rút gọn thành:"))
    b.append(eq("R = v d/ν&#770;"))
    b.append(p("Lấy vận tốc gió là 2 m/s và độ nhớt động học của không khí là "
               "1,5 × 10<sup>−5</sup> m²/s:"))
    b.append(eq("R = 1.33 d 10<sup>5</sup>", "4.21"))
    b.append(note("<b>Ghi chú về số hiệu.</b> Bản in chuyển trực tiếp từ Phương trình "
                  "4.21 sang Phương trình 4.23; không có Phương trình 4.22 trong "
                  "nguồn. Khoảng trống này được giữ nguyên ở đây và không có công "
                  "thức nào được bịa ra để lấp vào."))
    b.append(p("Vì R là thông số duy nhất thay đổi đáng kể theo kích thước vũng, "
               "k<sub>g</sub> = 2 × 10<sup>−3</sup>/R<sup>0.2</sup>, và "
               "khối lượng hơi thoát từ vũng theo Phương trình 4.18 là:"))
    b.append(eq("K<sub>g</sub> = 2 × 10<sup>−3</sup>/R<sup>0.2</sup>"))
    b.append(eq("G = 2 × 10<sup>−3</sup> A Δp M/R<sup>0.2</sup> kg/s"))
    b.append(p("Hình 4.3 cho giá trị R<sup>0.2</sup> ứng với các kích thước vũng khác "
               "nhau; đây là nơi giá trị R<sup>0.2</sup> được đưa vào theo kích thước "
               "vũng. Tốc độ hóa hơi này phải bằng tốc độ phát thải chất lỏng theo "
               "Phương trình 4.13 nếu vũng không bị giới hạn cơ lý:"))
    b.append(fig(3, F.fig_f403()))
    b.append(p("Cân bằng giữa tốc độ hóa hơi và tốc độ rò chất lỏng:"))
    b.append(eq("1.13 a [σ<sub>l</sub>(P − 10<sup>5</sup>)]<sup>0.5</sup> = 2 × 10<sup>−3</sup> A Δp M/R<sup>0.2</sup> kg/s"))
    b.append(p("từ đó có diện tích vũng:"))
    b.append(eq("A = 5.65 × 10<sup>2</sup> a [σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> R<sup>0.2</sup>/( Δp M) m<sup>2</sup>", "4.23"))
    b.append(p("Phương trình xác định phạm vi khu vực nguy hiểm cũng là phương trình "
               "thực nghiệm:"))
    b.append(eq("X = [625 Q/(LEL(mixture) × source length)]<sup>1.14</sup> m", "4.24"))
    b.append(p("Từ Phương trình 4.19, thể tích khí thoát ra là:"))
    b.append(eq("Q<sub>g</sub> = 1.64 × 10<sup>−4</sup> A Δp T/R<sup>0.2</sup> m<sup>3</sup>/s"))
    b.append(p("Tổng thể tích hỗn hợp rời khỏi mép vũng Q<sub>m</sub> gồm thể tích "
               "không khí cộng với thể tích khí:"))
    b.append(eq("m = Q<sub>a</sub> + Q<sub>g</sub> m<sup>3</sup>/s", "4.25"))
    b.append(p("Phần trăm khí trong hỗn hợp rời khỏi vũng và giới hạn nổ dưới hiệu "
               "dụng của hỗn hợp đó là:"))
    b.append(eq("Q<sub>g</sub> × 100/(Q<sub>a</sub> + Q<sub>g</sub>) %"))
    b.append(eq("LEL<sub>m</sub> = LEL<sub>g</sub> (Q<sub>g</sub> + Q<sub>a</sub>)/Q<sub>g</sub> %"))
    b.append(p("Chiều dài nguồn bằng nửa chu vi vũng, tức πd/2, hay theo diện tích "
               "là 1.77 A<sup>0.5</sup>. Lấy thể tích không khí chảy qua vũng là Q<sub>a</sub> "
               "như ở trên và thay vào Phương trình 4.24:"))
    b.append(eq("X = [625(Q<sub>a</sub> + Q<sub>g</sub>) Q<sub>g</sub>/(LEL(Q<sub>a</sub> + Q<sub>g</sub>) × 1.77 A<sup>0.5</sup>)]<sup>1.14</sup>"))
    b.append(eq("X = [353 × Q<sub>g</sub>/(LEL × A<sup>0.5</sup>)]<sup>1.14</sup>"))
    b.append(p("Thay công thức của Q<sub>g</sub> vào, với 625/1.77 cho 353:"))
    b.append(eq("X = [353 × 1.64 × 10<sup>−4</sup> × A<sup>0.5</sup> Δp T/(LEL<sub>g</sub> R<sup>0.2</sup>)]<sup>1.14</sup>"))
    b.append(eq("X = [5.8 A<sup>0.5</sup> Δp T/(LEL<sub>g</sub> R<sup>0.2</sup>)]<sup>1.14</sup> m", "4.26"))
    b.append(p("trong đó LEL<sub>g</sub> = giới hạn nổ dưới của hơi, %; A = diện tích "
               "vũng, m²; Δp = áp suất riêng phần theo phần của khí quyển; T = "
               "nhiệt độ, K; R = số Reynolds của dòng không khí. Phương trình cho "
               "phạm vi nằm ngang tính từ mép vũng và cũng được dùng cho phạm vi thẳng "
               "đứng."))
    b.append(p("Còn lại vấn đề sương mù chất lỏng, rất khó lượng hóa. Người ta đã "
               "ghi nhận sương mù hình thành ở áp suất thấp tới 3 × 10<sup>5</sup> "
               "N/m², nên không thể giả định rằng mọi rò chất lỏng ở áp suất trên áp "
               "suất tới hạn (2 × 10<sup>5</sup> N/m²) đều không tạo sương mù. "
               "Vì vậy, trừ khi có biện pháp ngăn tạo sương mù, chỉ còn cách giả định "
               "trường hợp xấu nhất: toàn bộ lượng rò hóa hơi, dùng Phương trình 4.4 "
               "để xác định thể tích hơi tương đương, rồi dùng Phương trình 4.6 và "
               "4.7 để xác định phạm vi khu vực nguy hiểm quanh điểm rò. Kết quả thường "
               "nặng hơn nhiều so với thực tế, nhưng nếu không có bằng chứng rõ ràng "
               "về mức độ tạo sương mù dễ cháy và giới hạn bắt cháy của nó thì khó có "
               "cách xử lý khác."))
    b.append(note("<b>Lưu ý về hình ảnh nguồn.</b> Số mũ của áp suất trong câu về sương "
                  "mù khá mờ trong ảnh quét; giá trị 3 × 10<sup>5</sup> N/m² được "
                  "ghi nhận ở đây theo cách đọc được, và sự mơ hồ của hình ảnh được "
                  "nêu rõ thay vì được giải quyết im lặng."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("4.2 Release of liquid below its atmospheric boiling point",
                "4.2 Release of liquid below its atmospheric boiling point"))
    b.append(p("A liquid released below its atmospheric boiling point from an "
               "orifice takes the form of a jet, or of a mist where the upstream "
               "pressure is sufficiently high. The classic formula for flow from "
               "an orifice or nozzle is:"))
    b.append(eq("G = C a [2 σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> kg/s"))
    b.append(p("where G = mass release, kg/s; a = orifice area, m²; P = upstream "
               "pressure, N/m²; C = discharge coefficient; σ<sub>l</sub> = "
               "liquid density at atmospheric conditions, kg/m³. As before, C has a "
               "maximum value of around 0.8, so the equation becomes:"))
    b.append(eq("G = 1.13 a [σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> kg/s", "4.13"))
    b.append(p("If no mist forms, no significant hazardous area surrounds the leak "
               "(unless the liquid is further contained around the point of "
               "leakage). A liquid jet exits the orifice and forms a pool where it "
               "reaches the floor or ground. The time taken for the jet to reach "
               "the ground can be calculated using Newton's laws of motion. For a "
               "jet released at an angle Φ above the horizontal, using v = u + a t "
               "with the final vertical velocity zero at the apex:"))
    b.append(p("Here Φ is the angle of release above the horizontal, g = 9.81 "
               "m/s² is the acceleration due to gravity and t<sub>1</sub> is the "
               "time to the apex of the jet:"))
    b.append(eq("v sin Φ − g t<sub>1</sub> = 0"))
    b.append(eq("t<sub>1</sub> = v sin Φ/g"))
    b.append(p("Using v² = u² + 2gS, where S is the vertical distance to the apex "
               "above the release point:"))
    b.append(eq("(v sin Φ)<sup>2</sup> − 2 g S = 0"))
    b.append(eq("S = (v sin Φ)<sup>2</sup>/2g"))
    b.append(p("If the initial release is at height h, the total height becomes "
               "[h + (v sin Φ)²/2g]; from S = u t + 0.5 g t² with u = 0:"))
    b.append(eq("[h + (v sin Φ)<sup>2</sup>/2g] = 0.5 g t<sub>2</sub><sup>2</sup>"))
    b.append(eq("t = [(2gh + v<sup>2</sup> sin<sup>2</sup>Φ)<sup>0.5</sup> + v sin Φ]/g"))
    b.append(p("With the horizontal velocity component v cos Φ, and neglecting "
               "the friction of the air through which the jet moves, the distance "
               "travelled is:"))
    b.append(eq("X = v cos Φ [(2gh + v<sup>2</sup> sin<sup>2</sup>Φ)<sup>0.5</sup> + v sin Φ]/g m", "4.14"))
    b.append(p("Where the jet is horizontal, sin Φ = 0 and cos Φ = 1, which "
               "simplifies the equation to:"))
    b.append(eq("X = (2 v<sup>2</sup> h/g)<sup>0.5</sup> m", "4.15"))
    b.append(p("It is recommended that this simplified equation be used wherever "
               "the jet release direction is not specified: the equations are "
               "idealized, an actual release is unlikely to be ideal, and the "
               "result is only an estimate. Because of turbulence in a jet which "
               "is not an ideal orifice, the horizontal figure will in most cases "
               "be larger than what practically occurs. Where this is not so, "
               "Equation 4.14 should be differentiated for a maximum and the angle "
               "giving that maximum introduced into Equation 4.14."))
    b.append(p("Where the jet is directed at an angle below the horizontal, the "
               "equation changes to:"))
    b.append(eq("X = v cos Φ [(v sin Φ − 2gh)<sup>0.5</sup> − v sin Φ]/g m", "4.16"))
    b.append(p("From Equation 4.13 divided by σ<sub>l</sub> a, the release "
               "velocity is:"))
    b.append(eq("Velocity = 1.13 [(P − 10<sup>5</sup>)/σ<sub>l</sub>]<sup>0.5</sup> m/s", "4.17"))
    b.append(p("At the point where the jet lands a pool forms and, if not physically "
               "contained, grows until the evaporation rate from its surface "
               "equals the release rate from the leak orifice. The evaporation "
               "rate from a pool is given by:"))
    b.append(eq("G = A k<sub>g</sub> Δp M kg/s", "4.18"))
    b.append(p("where G = vaporization rate, kg/s; A = pool area, m²; Δp = "
               "partial pressure of vapour over the liquid as a fraction of "
               "atmospheric pressure; k<sub>g</sub> = overall mass-transfer "
               "coefficient. Using Equation 4.4 to convert to a volume "
               "vaporization rate:"))
    b.append(eq("Q = 8.2 A k<sub>g</sub> Δp T/10<sup>2</sup> m<sup>3</sup>/s", "4.19"))
    b.append(p("The partial pressure of vapour above a liquid is also known as its "
               "vapour pressure; below boiling point it is a fraction of "
               "atmospheric pressure, which also indicates the ratio of vapour to "
               "air. Where this is not known, an estimate can often be made using "
               "Table 4.2, which gives vapour (partial) pressure as a fraction of "
               "atmospheric pressure:"))
    b.append(table(_T42_HEAD_EN, _T42_ROWS,
                   "Table 4.2 · Vapour (partial) pressure of liquids at various "
                   "ambient temperatures"))
    b.append(note("<b>Note 1.</b> The values in the table are approximate only. "
                  "<b>Note 2.</b> T<sub>a</sub> is ambient temperature. "
                  "<b>Note 3.</b> Figures are typical for hydrocarbons. Other "
                  "materials are likely to be lower in general."))
    b.append(note("<b>Partial-pressure note.</b> These figures are derived from a "
                  "monograph by Lippincott and Lyman. If the partial pressure is "
                  "known, however, it should be used, as the simplification gives "
                  "answers higher than the actual figure, in accordance with the "
                  "estimation procedure used throughout this book."))
    b.append(p("The mass-transfer coefficient k<sub>g</sub> can be found from the "
               "following formula, where β is the Schmidt number (kinematic "
               "viscosity divided by the diffusivity of the vapour in air), R is "
               "the Reynolds number and G<sub>m</sub> is the mass flow of air, "
               "kg-mol/s:"))
    b.append(eq("k<sub>g</sub> = 3.6 × 10<sup>−2</sup> G<sub>m</sub>/(β<sup>0.67</sup> R<sup>0.2</sup> M)", "4.20"))
    b.append(p("The classic formula for Reynolds number is R = v d σ/τ, "
               "where v is the air velocity, d the characteristic dimension, "
               "σ the density of air and τ the absolute viscosity of "
               "air:"))
    b.append(eq("R = v d σ/τ"))
    b.append(p("Using the kinematic viscosity ν&#770; (m²/s) this simplifies to:"))
    b.append(eq("R = v d/ν&#770;"))
    b.append(p("Taking the wind velocity as 2 m/s and the kinematic viscosity of "
               "air as 1.5 × 10<sup>−5</sup> m²/s:"))
    b.append(eq("R = 1.33 d 10<sup>5</sup>", "4.21"))
    b.append(note("<b>Numbering note.</b> The printed text passes directly from "
                  "Equation 4.21 to Equation 4.23; no Equation 4.22 appears in the "
                  "source. The gap is preserved here and no equation has been "
                  "invented to fill it."))
    b.append(p("As R is the only parameter subject to significant change with pool "
               "size, k<sub>g</sub> = 2 × 10<sup>−3</sup>/R<sup>0.2</sup>, "
               "and the mass of vapour released from the pool using Equation 4.18 "
               "is:"))
    b.append(eq("K<sub>g</sub> = 2 × 10<sup>−3</sup>/R<sup>0.2</sup>"))
    b.append(eq("G = 2 × 10<sup>−3</sup> A Δp M/R<sup>0.2</sup> kg/s"))
    b.append(p("Figure 4.3 gives values of R<sup>0.2</sup> for various pool sizes, "
               "which is how R<sup>0.2</sup> is read for the pool in question. This "
               "must equal the release rate of liquid from Equation 4.13 if the "
               "pool size is not restricted physically:"))
    b.append(fig(3, F.fig_f403()))
    b.append(p("The balance between vaporization and liquid release is:"))
    b.append(eq("1.13 a [σ<sub>l</sub>(P − 10<sup>5</sup>)]<sup>0.5</sup> = 2 × 10<sup>−3</sup> A Δp M/R<sup>0.2</sup> kg/s"))
    b.append(p("which gives the pool area:"))
    b.append(eq("A = 5.65 × 10<sup>2</sup> a [σ<sub>l</sub> (P − 10<sup>5</sup>)]<sup>0.5</sup> R<sup>0.2</sup>/( Δp M) m<sup>2</sup>", "4.23"))
    b.append(p("The equation for the extent of the hazardous area is again "
               "empirical:"))
    b.append(eq("X = [625 Q/(LEL(mixture) × source length)]<sup>1.14</sup> m", "4.24"))
    b.append(p("From Equation 4.19 the volume release of gas is:"))
    b.append(eq("Q<sub>g</sub> = 1.64 × 10<sup>−4</sup> A Δp T/R<sup>0.2</sup> m<sup>3</sup>/s"))
    b.append(p("The total volume of mixture leaving the pool edge, Q<sub>m</sub>, "
               "is the volume of air plus the gas volume:"))
    b.append(eq("m = Q<sub>a</sub> + Q<sub>g</sub> m<sup>3</sup>/s", "4.25"))
    b.append(p("The percentage gas in the mixture leaving the pool, and the "
               "effective lower explosive limit of that mixture, are:"))
    b.append(eq("Q<sub>g</sub> × 100/(Q<sub>a</sub> + Q<sub>g</sub>) %"))
    b.append(eq("LEL<sub>m</sub> = LEL<sub>g</sub> (Q<sub>g</sub> + Q<sub>a</sub>)/Q<sub>g</sub> %"))
    b.append(p("The source length is half the perimeter of the pool, πd/2, or "
               "expressed as area 1.77 A<sup>0.5</sup>. Taking the volume of air "
               "flowing over the pool as Q<sub>a</sub> as given above and "
               "substituting in Equation 4.24:"))
    b.append(eq("X = [625(Q<sub>a</sub> + Q<sub>g</sub>) Q<sub>g</sub>/(LEL(Q<sub>a</sub> + Q<sub>g</sub>) × 1.77 A<sup>0.5</sup>)]<sup>1.14</sup>"))
    b.append(eq("X = [353 × Q<sub>g</sub>/(LEL × A<sup>0.5</sup>)]<sup>1.14</sup>"))
    b.append(p("Substituting the equation for Q<sub>g</sub>, with 625/1.77 giving "
               "353:"))
    b.append(eq("X = [353 × 1.64 × 10<sup>−4</sup> × A<sup>0.5</sup> Δp T/(LEL<sub>g</sub> R<sup>0.2</sup>)]<sup>1.14</sup>"))
    b.append(eq("X = [5.8 A<sup>0.5</sup> Δp T/(LEL<sub>g</sub> R<sup>0.2</sup>)]<sup>1.14</sup> m", "4.26"))
    b.append(p("where LEL<sub>g</sub> = lower explosive limit of the vapour, %; A = "
               "pool area, m²; Δp = partial pressure as a fraction of "
               "atmosphere; T = temperature, K; R = Reynolds number for airflow. "
               "The above equation gives the horizontal extent of hazardous area "
               "from the edge of the pool and should also be used for the vertical "
               "extent."))
    b.append(p("There remains the problem of mist, which is very difficult to "
               "quantify. Mists have been shown to form at pressures as low as "
               "3 × 10<sup>5</sup> N/m², so it cannot be assumed that no mist "
               "will be formed from any leak of liquid above the critical pressure "
               "(2 × 10<sup>5</sup> N/m²). Thus the only method is to assume "
               "the worst case unless precautions are taken to avoid mist "
               "production: the entire leak should be assumed to evaporate, "
               "Equation 4.4 used to determine the vapour equivalent, and "
               "Equations 4.6 and 4.7 used to determine the extent of the "
               "hazardous area around the point of leakage. This will generally "
               "produce a result much more onerous than what will actually occur, "
               "but unless clear evidence of the extent of formation of a "
               "flammable mist and its ignition limits is available in a "
               "particular case, it is hard to see how any alternative action can "
               "be taken."))
    b.append(note("<b>Source-image note.</b> The exponent in the mist-pressure "
                  "figure is faint in the page render; the value 3 × 10<sup>5</sup> "
                  "N/m² is recorded as read here, and the image ambiguity is "
                  "flagged rather than silently resolved."))
    return "".join(b)
