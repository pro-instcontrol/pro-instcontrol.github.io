# -*- coding: utf-8 -*-
"""Chapter 4, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 119-124 (PDF pp. 140-145).

Covers Section 4.4 (equation-selection summaries 4.4.1-4.4.3), Section 4.5
(Equations 4.31-4.35 and the poorly ventilated area model), Section 4.5.1
(Example 6, printed under the heading BS/EN 10079-10) and Section 4.6
(Conclusion). Equations 4.1-4.30 belong to modules A-D and are referenced
by number only.

The integration module owns the page shell, page sources, references, note
terms, end matter and the h2 heading; this file defines only the two body
functions. Printed grouping, units and worked numbers are retained and
flagged in notes rather than silently corrected. No ventilation table and
no Figures 4.4/4.5 are printed in this chapter, so none are created here.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, eq


def body_vi():
    b = []
    b.append(h3("4.4 Tóm tắt cách dùng các phương trình",
                "4.4 Summary of use of equations"))
    b.append(p("Các phương trình nêu trên được dùng như sau."))
    b.append(h4("4.4.1 Phát thải khí và hơi",
                "4.4.1 Gas and vapour releases"))
    b.append(p("Trước hết xác định lượng phát thải theo khối lượng của khí hoặc "
               "hơi bằng Phương trình 4.1 nếu áp suất phát thải lớn hơn "
               "2 × 10<sup>5</sup> N/m², ngược lại dùng Phương trình 4.3. "
               "Sau đó đổi lượng này sang thể tích bằng Phương trình 4.4. Nếu "
               "áp suất phát thải lớn hơn 2 × 10<sup>5</sup> N/m² thì tính "
               "phạm vi khu vực nguy hiểm bằng Phương trình 4.6; nếu áp suất nhỏ "
               "hơn 2 × 10<sup>5</sup> N/m² thì dùng Phương trình 4.7. "
               "Trong mọi trường hợp, nhân kết quả với 1,5 nếu nguồn phát thải "
               "nằm trong vòng 1,5 m tính từ mặt đất."))
    b.append(p("Nếu áp suất phát thải lớn hơn 2 × 10<sup>5</sup> N/m² "
               "nhưng có vật cản nằm trong khoảng cách tính được theo Phương "
               "trình 4.6, trước hết tính hàm lượng khí trong hỗn hợp bằng "
               "Phương trình 4.8, rồi tính khối lượng phân tử của hỗn hợp bằng "
               "Phương trình 4.9 với khối lượng phân tử của không khí lấy bằng "
               "29. Tổng thể tích hỗn hợp khí/không khí tại vật cản được tính "
               "bằng Phương trình 4.10. Giờ có thể tính giới hạn nổ dưới của "
               "hỗn hợp khi pha thêm không khí bằng Phương trình 4.12, rồi tính "
               "khoảng cách phân tán theo gió bằng Phương trình 4.7 có xét ảnh "
               "hưởng của mặt đất. Cộng kết quả này với khoảng cách từ nguồn "
               "phát thải đến vật cản để được phạm vi khu vực nguy hiểm từ điểm "
               "rò theo hướng vật cản."))
    b.append(h4("4.4.2 Phát thải chất lỏng dưới điểm sôi khí quyển",
                "4.4.2 Liquid releases below boiling point"))
    b.append(p("Lượng chất lỏng phát thải được tính bằng Phương trình 4.13. "
               "Quãng đường tia chất lỏng đi được tính bằng Phương trình 4.15 "
               "nếu phát thải hướng lên trên phương ngang, hoặc Phương trình "
               "4.16 nếu hướng xuống dưới phương ngang; nếu không rõ quỹ đạo thì "
               "dùng Phương trình 4.15. Trong cả hai trường hợp cần tính vận tốc "
               "phát thải bằng Phương trình 4.17. Dùng Phương trình 4.19 để tính "
               "tốc độ bay hơi, rồi Phương trình 4.23 để tính diện tích vũng "
               "chất lỏng. Cuối cùng, Phương trình 4.26 cho phép tính phạm vi "
               "khu vực nguy hiểm phía trên và vượt quá mép vũng."))
    b.append(p("Khi đó khu vực nguy hiểm thường được xác định bằng khoảng cách "
               "ngang từ chỗ rò đến tâm vũng cộng với bán kính vũng, cộng với "
               "phần phạm vi vượt quá vũng; theo phương thẳng đứng chỉ lấy phần "
               "phạm vi vượt quá vũng. Cách này không xét đến sương mù chất "
               "lỏng; nếu có sương mù thì coi như hơi và xử lý theo quy trình "
               "tại Mục 4.4.1."))
    b.append(h4("4.4.3 Phát thải chất lỏng ở nhiệt độ cao hơn điểm sôi khí quyển",
                "4.4.3 Liquid releases above boiling point"))
    b.append(p("Trước hết cần tính lượng chất lỏng bay hơi trong đường rò bằng "
               "Phương trình 4.29; từ đó tính lượng hơi trong hỗn hợp thoát ra "
               "bằng Phương trình 4.27 và mật độ của hỗn hợp khí/lỏng thoát ra "
               "bằng Phương trình 4.30, rồi tính khối lượng hỗn hợp phát thải "
               "bằng Phương trình 4.28. Lượng hơi ngay ngoài lỗ rò, gồm phần "
               "bay ra và phần bay hơi đột thời (flash), được tính lại bằng "
               "Phương trình 4.27 nhưng ở áp suất khí quyển; phạm vi khu vực "
               "nguy hiểm tạo thành được tính bằng Phương trình 4.6 có xét ảnh "
               "hưởng của mặt đất. Giá trị này được nhân thêm hệ số 1,5 vì khả "
               "năng hình thành sương mù."))
    b.append(p("Phần chất lỏng còn lại được giả định tới mặt đất; điểm tới được "
               "tính như đối với chất lỏng dưới điểm sôi, dùng Phương trình "
               "4.15 hoặc 4.16 tùy hướng tia. Bay hơi xảy ra ngay khi chạm mặt "
               "đất và phạm vi khu vực nguy hiểm được tính như đối với khí/hơi "
               "bằng Phương trình 4.7, nhân kết quả với 1,5 do ảnh hưởng của "
               "mặt đất. Như vậy khu vực nguy hiểm gồm vùng quanh lỗ rò do bay "
               "hơi tại chỗ và vùng ở mặt đất có phạm vi từ lỗ rò bằng quãng "
               "đường tia đi được cộng với bán kính vùng bay hơi tại mặt đất; "
               "chiều cao của vùng này chính là bán kính nói trên."))
    b.append(h3("4.5 Phát thải trong khu vực thông gió kém",
                "4.5 Releases in areas which are not well ventilated"))
    b.append(p("Tất cả phép tính nêu trên đều giả định gió tới mọi vị trí với "
               "tốc độ khoảng 2 m/s. Ở khu vực thông gió kém, chẳng hạn trong "
               "nhà, gió đó không tồn tại dạng tương tự mà được thay bằng thông "
               "gió nhân tạo trong hầu hết trường hợp. Thêm vào đó, thể tích kín "
               "giới hạn thông gió tự nhiên là hữu hạn. Vì vậy các phép tính "
               "trên phải coi là đáng ngờ trừ khi thông gió ở mọi ngóc ngách của "
               "không gian kín được coi là tương đương thông gió tự nhiên. Trong "
               "BS/EN 60079-10<sup>3</sup> (dự kiến thay thế BS 5345 Part 2) có "
               "nỗ lực xác định tổng quát hơn phạm vi và thời gian tồn lưu của "
               "khí quyển nổ; các phương trình dưới đây dựa trên nỗ lực đó."))
    b.append(p("Lưu lượng không khí tối thiểu cần để pha loãng một phát thải vật "
               "liệu dễ cháy xuống dưới giới hạn nổ dưới được cho bởi Phương "
               "trình 4.31 nguyên văn: Q<sub>a</sub> = 0,12 × G<sub>f</sub> "
               "× T<sub>a</sub><sup>2</sup>/T<sub>o</sub> × M × "
               "LEL m<sup>3</sup>/s, trong đó Q<sub>a</sub> là lưu lượng không "
               "khí tối thiểu lý thuyết cần thiết (m³/s), T<sub>a</sub> là nhiệt "
               "độ môi trường (K), G<sub>f</sub> là tốc độ phát thải khối lượng "
               "lớn nhất của vật liệu dễ cháy (kg/s), M là khối lượng phân tử và "
               "LEL là giới hạn nổ dưới (% v/v)."))
    b.append(eq("Q<sub>a</sub> = 0.12 × G<sub>f</sub> × "
                "T<sub>a</sub><sup>2</sup>/T<sub>o</sub> × M × "
                "LEL m<sup>3</sup>/s", "4.31"))
    b.append(p("Phương trình rút gọn là Q<sub>a</sub> = 0,03 × "
               "G<sub>f</sub> × T<sub>a</sub><sup>2</sup>/M × LEL "
               "m<sup>3</sup>/s, chính là dạng dùng trong Ví dụ 6."))
    b.append(note("<b>Lưu ý về Phương trình 4.31.</b> Cách nhóm và đơn vị được "
                  "giữ nguyên như bản in: dạng đầy đủ có "
                  "T<sub>a</sub><sup>2</sup>/T<sub>o</sub> và thừa số M × "
                  "LEL với đơn vị m³/s. Ví dụ 6 lại tính 0,03 × 0,475 "
                  "× 295²/(28 × 2,7), tức LEL nằm ở mẫu số, nên cách "
                  "nhóm trong bản in là không rõ ràng. Không dạng nào được sửa "
                  "lặng lẽ."))
    b.append(p("Nếu Q<sub>a</sub> có thể liên hệ với số lần thay không khí quanh "
               "nguồn phát thải (tức vận tốc dòng khí), một phép tính tiếp theo "
               "xác định kích thước khí quyển nổ quanh đám khí: V<sub>m</sub> = "
               "Q<sub>a</sub>/C m³. Do mức độ bất định, cần thêm hai hệ số an "
               "toàn: một cho độ bất định của LEL và một cho độ bất định của "
               "dòng khí lý tưởng. Kết quả là Phương trình 4.32."))
    b.append(eq("V<sub>m</sub> = Q<sub>a</sub> f/(C k) m<sup>3</sup>", "4.32"))
    b.append(p("Ở đây V<sub>m</sub> là thể tích khí quyển nổ, Q<sub>a</sub> là "
               "lưu lượng không khí tại nguồn rò, C là số lần thay không khí mỗi "
               "giây dựa trên dòng khí quanh nguồn phát thải, và f là hiệu quả "
               "thông gió: f = 1/2–4/5 (1 cho dòng khí lý tưởng, 2–4 cho các "
               "cấp trung gian, 5 cho dòng khí bị cản trở nhiều nhất). Hệ số an "
               "toàn áp dụng cho LEL là k = 0,25 đối với phát thải liên tục và "
               "cấp sơ cấp, và k = 0,5 đối với phát thải cấp thứ cấp."))
    b.append(note("<b>Lưu ý về Phương trình 4.32.</b> Bản in cho đơn vị của "
                  "V<sub>m</sub> là m³/s, rõ ràng là lỗi gõ thay cho thể tích; "
                  "bản trình bày dùng m³ và sự khác biệt được ghi chú ở đây thay "
                  "vì sửa lặng lẽ."))
    b.append(p("Trong trường hợp khu vực kín (xác định được), C được tính theo "
               "Phương trình 4.33, với V<sub>o</sub> là thể tích không gian kín."))
    b.append(eq("C = Q<sub>a</sub>/V<sub>o</sub>", "4.33"))
    b.append(note("<b>Lưu ý về Phương trình 4.33.</b> Phương trình được in kèm "
                  "đơn vị m³, rõ ràng là lỗi gõ của tần suất thay không khí; "
                  "không gắn đơn vị trong bản trình bày. Phương trình chỉ áp "
                  "dụng cho không gian kín (xác định được)."))
    b.append(p("Đối với trường hợp ngoài trời, một phương trình khác được suy "
               "từ Phương trình 4.32. Một thể tích không khí không bị giới hạn "
               "ngoài trời khoảng 1000 m³ (giả định hình tròn vì đó là trường "
               "hợp xấu nhất) được quét sạch trong khoảng 6 giây, cho "
               "C = 1/6 = 0,16; suy ra Phương trình 4.34."))
    b.append(eq("V<sub>m</sub> = Q<sub>a</sub>/(0.16 k) m<sup>3</sup>", "4.34"))
    b.append(p("Do bản chất của dòng khí ngoài trời, Phương trình 4.34 có khả "
               "năng cho thể tích khí quyển nổ bi quan (quá lớn). Chuỗi phương "
               "trình cũng gồm Phương trình 4.35, dùng để tính thời gian phân "
               "tán sau khi phát thải kết thúc, với LEL là giới hạn nổ dưới (%) "
               "và UL là nồng độ tối đa (% v/v)."))
    b.append(eq("t = (f/C) Ln (LEL k/UL) s", "4.35"))
    b.append(note("<b>Lưu ý về Phương trình 4.35.</b> Cách nhóm in 'Ln (LEL kUL)' "
                  "không rõ ràng; dạng trình bày theo cách đọc của Ví dụ 6 trong "
                  "bản tóm tắt là Ln(0,5 × 2,7/100). Logarit này âm và sách "
                  "báo cáo giá trị tuyệt đối của nó là 27 s."))
    b.append(p("Để hỗ trợ dùng phương trình khi thông gió kém (trong nhà, không "
               "bổ sung thông gió), văn bản hướng dẫn độc giả đến 'Bảng 4.1', "
               "được cho là lấy từ một bảng trong sách hướng dẫn của Viện Dịch "
               "vụ Tòa nhà<sup>7</sup>, dùng để tính nhiệt độ gia nhiệt cần "
               "thiết cho một tòa nhà dựa trên tổn thất do thông gió tự nhiên."))
    b.append(note("<b>Bất thường về số bảng trong Mục 4.5.</b> Không có bảng "
                  "thông gió nào được in trong chương này: Bảng 4.1 là bảng vật "
                  "liệu dễ cháy của BS 5345 dài mười trang. Viện dẫn in được giữ "
                  "lại như một tham chiếu nguồn; không có bảng thông gió nào "
                  "được tạo ra hay gán nhầm vào đó."))
    b.append(h4("4.5.1 Ví dụ phát thải khí dùng công thức BS/EN 10079-10<sup>3</sup>",
                "4.5.1 Example of gas release using BS/EN 10079-10<sup>3</sup> formulae"))
    b.append(note("<b>Lỗi ở tiêu đề.</b> Tiêu đề in là BS/EN 10079-10<sup>3</sup>; "
                  "phần nội dung và Tài liệu tham khảo 3 ghi BS/EN 60079-10. Số "
                  "in được giữ nguyên trong tiêu đề và được ghi chú tại đây."))
    b.append(p("<b>Ví dụ 6.</b> Phát thải ethylene đã thảo luận trong Ví dụ 1 "
               "xảy ra trong nhà, tại một tòa nhà thông gió tốt (f = 1). Văn bản "
               "nêu tốc độ phát thải khối lượng 0,55 kg/s; phép thay số ngay sau "
               "đó dùng 0,475 kg/s."))
    b.append(p("Dùng Phương trình 4.31 cho lưu lượng không khí cần tại chỗ rò: "
               "Q<sub>a</sub> = 0,03 × 0,475 × 295²/(28 × 2,7) "
               "= <b>16,4 m³/s</b>."))
    b.append(p("Giá trị này được dùng trong Phương trình 4.34 để cho thể tích "
               "lớn nhất của khí quyển dễ cháy trong không gian kín, được thông "
               "gió với tốc độ như một không gian hở được gió quét: Q<sub>m</sub> "
               "= 16,4/0,16 × 0,5 = <b>205 m³</b>."))
    b.append(p("Thể tích này cho khu vực nguy hiểm tổng thể lớn hơn thực tế "
               "ngoài trời (ước tính từ 20 m đến 45 m theo hướng dòng thông gió "
               "từ nguồn rò), vì thể tích đó không phải hình cầu. Vì vậy Phương "
               "trình 4.34 chỉ áp dụng cho không gian kín hữu hạn có điều kiện "
               "thông gió tương tự, không áp dụng cho trường hợp ngoài trời."))
    b.append(p("Áp dụng Phương trình 4.35 cho thời gian tồn lưu sau khi phát "
               "thải kết thúc: t = (1/0,16) Ln(0,5 × 2,7/100) = "
               "<b>27 s</b>. Con số này lại rất cao đối với vị trí ngoài trời "
               "nhưng thực tế hơn trong nhà, nơi thể tích tổng bị giới hạn."))
    b.append(note("<b>Ghi chú lỗi in trong Ví dụ 6.</b> Tốc độ phát thải nêu là "
                  "0,55 kg/s mâu thuẫn với giá trị 0,475 kg/s được thay vào (Ví "
                  "dụ 1 cho 0,03 kg/s). Kết quả thể tích được ký là Q<sub>m</sub> "
                  "trong sách, nhưng đó là đại lượng V<sub>m</sub> của Phương "
                  "trình 4.34; phép thay in 16,4/0,16 × 0,5 cho 205 m³ chỉ "
                  "khi đọc mẫu số là 0,16 × 0,5. Logarit ở Phương trình "
                  "4.35 là âm và giá trị tuyệt đối được báo cáo là 27 s. Tất cả "
                  "con số in được giữ nguyên."))
    b.append(h3("4.6 Kết luận", "4.6 Conclusion"))
    b.append(p("Chương này chứa một bộ tính toán tương đối đầy đủ để xác định "
               "phạm vi khu vực nguy hiểm. Những phép tính cho khu vực ngoài "
               "trời đối với hơi và chất lỏng đã được dùng rộng rãi trong nhiều "
               "năm và về cơ bản phù hợp với các phán đoán chủ quan trong nhiều "
               "quy chuẩn, vì thế có uy tín nhất định. Tuy nhiên, các công thức "
               "trong Mục 4.4 là mới hơn."))
    b.append(p("Cho đến khi được dùng trong thời gian đáng kể và có đủ dữ liệu "
               "tích lũy, các công thức này cần được dùng hết sức thận trọng. "
               "Ban đầu nên dùng chúng chỉ như phép tính thước đo (ví dụ, xác "
               "định liệu thời gian tồn lưu trong một tình huống cụ thể có làm "
               "nguồn phát thải cấp thứ cấp tạo ra Vùng 1 trong nhà hay không). "
               "Nhấn mạnh rằng không có ý cho rằng chúng không chính xác, mà chỉ "
               "cần tích lũy kinh nghiệm cho các kỹ sư thực hành. Bộ công thức "
               "này cũng khó dùng hơn trong trường hợp phát thải chất lỏng, đặc "
               "biệt khi chất lỏng ở dưới điểm sôi."))
    b.append(p("Cuối cùng, Bảng 4.1 được đưa vào (Fig. 4.5 từ BS 5345 Part 2<sup>1</sup>) "
               "và cung cấp một số thông tin cần thiết để dùng các phương pháp "
               "tính trong chương này. Bảng cũng có hai cột mang tên 'Group' và "
               "'Temperature Class' liên quan đến hiệu năng thiết bị và sẽ được "
               "mô tả chi tiết hơn trong Chương 7; chúng được liệt kê ở đây để "
               "xác định mối liên hệ giữa khí quyển nổ hình thành và loại thiết "
               "bị nên dùng."))
    b.append(note("<b>Bất thường về bảng/hình trong Mục 4.6.</b> Văn bản viện "
                  "dẫn 'Fig. 4.5 from BS 5345 Part 2' là nguồn của Bảng 4.1, "
                  "nhưng không có Hình 4.4 hay 4.5 nào được in trong chương này. "
                  "Viện dẫn được giữ nguyên như một tham chiếu nguồn; không tạo "
                  "hình nào như vậy."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("4.4 Summary of use of equations",
                "4.4 Summary of use of equations"))
    b.append(p("The foregoing equations are used as follows."))
    b.append(h4("4.4.1 Gas and vapour releases",
                "4.4.1 Gas and vapour releases"))
    b.append(p("First determine the mass release of gas or vapour using "
               "Equation 4.1 if the release pressure is greater than "
               "2 × 10<sup>5</sup> N/m², and Equation 4.3 otherwise. Then "
               "convert this to a volume using Equation 4.4. If the release "
               "pressure is greater than 2 × 10<sup>5</sup> N/m² calculate "
               "the extent of the hazardous area using Equation 4.6; if it is "
               "less than 2 × 10<sup>5</sup> N/m² use Equation 4.7. In all "
               "cases multiply the result obtained by 1.5 if the release is "
               "within 1.5 m of the ground."))
    b.append(p("If the release is at a pressure greater than 2 × "
               "10<sup>5</sup> N/m² but there is an obstruction within the "
               "distance calculated using Equation 4.6, calculate the amount of "
               "gas in the mixture using Equation 4.8 and then the molecular "
               "weight of the mixture using Equation 4.9, taking the molecular "
               "weight of air as 29. The total volume of the gas/air mixture at "
               "the obstruction follows from Equation 4.10. The lower explosive "
               "limit of the mixture when further mixed with air can now be "
               "calculated using Equation 4.12, after which the wind-dispersal "
               "distance is calculated using Equation 4.7 taking account of "
               "ground proximity. This is added to the distance between the "
               "release and the obstruction to give the extent of the hazardous "
               "area from the release point in the direction of the obstruction."))
    b.append(h4("4.4.2 Liquid releases below boiling point",
                "4.4.2 Liquid releases below boiling point"))
    b.append(p("The mass of liquid released is calculated using Equation 4.13. "
               "The distance travelled by the jet of liquid is calculated using "
               "Equation 4.15 if the release is above the horizontal, or "
               "Equation 4.16 if it is below the horizontal; if the release "
               "trajectory is not known, use Equation 4.15. In both cases it is "
               "necessary to calculate the release velocity using Equation "
               "4.17. Using Equation 4.19 calculate the vaporization rate and "
               "then Equation 4.23 will permit calculation of the pool area. "
               "Finally, using Equation 4.26, the extent of the hazardous area "
               "above and beyond the pool edge can be calculated."))
    b.append(p("The hazardous area can then normally be defined as the "
               "horizontal distance from the leak to the pool centre, plus the "
               "pool radius, plus the extent beyond the pool; vertically it is "
               "just the extent beyond the pool. This takes no account of "
               "mists: if these are present they should be assumed to be vapour "
               "and treated using the procedure in Section 4.4.1."))
    b.append(h4("4.4.3 Liquid releases above boiling point",
                "4.4.3 Liquid releases above boiling point"))
    b.append(p("It is first necessary to calculate the amount of liquid "
               "vaporizing in the leak path using Equation 4.29 and, from this, "
               "the amount of vapour in the emerging mixture using Equation "
               "4.27 and the mixture density of the gas/liquid mixture emerging "
               "from the release using Equation 4.30, after which the mass of "
               "mixture released can be calculated using Equation 4.28. The "
               "mass of vapour immediately outside the leak, due to that "
               "released and that flashing off immediately, is calculated using "
               "Equation 4.27 again but at atmospheric pressure; the extent of "
               "the hazardous area thus formed is calculated using Equation 4.6 "
               "taking account of ground proximity. This figure is multiplied "
               "by a further factor of 1.5 because of the likelihood of mist "
               "formation."))
    b.append(p("The remaining liquid is assumed to reach the ground; the point "
               "at which it does so is calculated as for liquids below their "
               "boiling points, using Equations 4.15 or 4.16 as appropriate. "
               "Vaporization is expected immediately contact is made with the "
               "ground, and the extent of the hazardous area is calculated as "
               "for gas/vapour using Equation 4.7 with the result multiplied by "
               "1.5 because of ground proximity. The hazardous areas are thus "
               "around the leak due to vaporization at the leak, and at ground "
               "level with an extent from the leak of the distance travelled by "
               "the jet plus the radius of the area created by vaporization at "
               "ground level. The height of this will be the radius created by "
               "ground-level vaporization."))
    b.append(h3("4.5 Releases in areas which are not well ventilated",
                "4.5 Releases in areas which are not well ventilated"))
    b.append(p("All of the foregoing calculations depend upon wind reaching all "
               "parts at around 2 m/s. In poorly ventilated areas, such as "
               "indoors, this wind does not exist in the same form and is "
               "replaced by artificial ventilation in most circumstances. In "
               "addition, the enclosed volume that limits the natural "
               "ventilation is not unlimited. Thus all of the foregoing "
               "calculations must be considered suspect unless the ventilation "
               "in all nooks and crannies of the enclosure can be considered "
               "equivalent to natural ventilation. In BS/EN 60079-10<sup>3</sup>, "
               "which will replace BS 5345 Part 2, there is an attempt to define "
               "more globally the extents of and persistence of explosive "
               "atmospheres; the following equations are based upon that."))
    b.append(p("The minimum flow of air needed to dilute a given release of "
               "flammable material to below its lower explosive limit is given "
               "by Equation 4.31 as printed: Q<sub>a</sub> = 0.12 × "
               "G<sub>f</sub> × T<sub>a</sub><sup>2</sup>/T<sub>o</sub> "
               "× M × LEL m<sup>3</sup>/s, where Q<sub>a</sub> is the "
               "theoretical minimum air flow rate required (m³/s), T<sub>a</sub> "
               "is ambient temperature (K), G<sub>f</sub> is the maximum mass "
               "release rate of flammable material (kg/s), M is molecular "
               "weight and LEL is the lower explosive limit (% v/v)."))
    b.append(eq("Q<sub>a</sub> = 0.12 × G<sub>f</sub> × "
                "T<sub>a</sub><sup>2</sup>/T<sub>o</sub> × M × "
                "LEL m<sup>3</sup>/s", "4.31"))
    b.append(p("This simplifies to Q<sub>a</sub> = 0.03 × G<sub>f</sub> "
               "× T<sub>a</sub><sup>2</sup>/M × LEL m<sup>3</sup>/s, "
               "the form used in Example 6."))
    b.append(note("<b>Equation 4.31 caveat.</b> The grouping and units are "
                  "reproduced as printed: the full form carries "
                  "T<sub>a</sub><sup>2</sup>/T<sub>o</sub> and a factor M × "
                  "LEL with the unit m³/s. Example 6 instead evaluates "
                  "0.03 × 0.475 × 295²/(28 × 2.7), that is with "
                  "LEL in the denominator, so the printed grouping is ambiguous. "
                  "Neither form has been silently corrected."))
    b.append(p("If Q<sub>a</sub> can be related to the number of air changes "
               "around the source of release (i.e. the airflow velocity), a "
               "further calculation determines the size of the explosive "
               "atmosphere around the gas cloud: V<sub>m</sub> = Q<sub>a</sub>/C "
               "m³. Because of the degree of uncertainty, two safety factors "
               "need to be added, one for the uncertainty in LEL and another "
               "for the uncertainty in ideal airflow; this gives Equation 4.32."))
    b.append(eq("V<sub>m</sub> = Q<sub>a</sub> f/(C k) m<sup>3</sup>", "4.32"))
    b.append(p("Here V<sub>m</sub> is the volume of explosive atmosphere, "
               "Q<sub>a</sub> is the airflow at the leak source, C is the number "
               "of air changes per second based on airflow around the source of "
               "release, and f is the effectiveness of ventilation: "
               "f = 1/2–4/5 (1 for ideal airflow, 2–4 for intermediate grades, 5 "
               "for the most obstructed airflow). The safety factor applied to "
               "the LEL is k = 0.25 for continuous and primary grades of release "
               "and k = 0.5 for secondary grades."))
    b.append(note("<b>Equation 4.32 caveat.</b> The printed unit for "
                  "V<sub>m</sub> is m³/s, which is a typo for a volume; the "
                  "display uses m³ and the discrepancy is recorded here rather "
                  "than changed silently."))
    b.append(p("In the case of an enclosed (defined) area, C can be calculated "
               "from Equation 4.33, where V<sub>o</sub> is the volume of the "
               "enclosed space."))
    b.append(eq("C = Q<sub>a</sub>/V<sub>o</sub>", "4.33"))
    b.append(note("<b>Equation 4.33 caveat.</b> The equation is printed with the "
                  "unit m³, evidently a typo for an air-change rate; no unit is "
                  "attached in the display. It relates to defined (enclosed) "
                  "spaces only."))
    b.append(p("For the open-air situation a further equation is derived from "
               "Equation 4.32. An unrestricted volume of air outdoors of around "
               "1000 m³ (assumed circular, as that is the worst case) is swept "
               "with air in around 6 seconds, giving C = 1/6 = 0.16; hence "
               "Equation 4.34."))
    b.append(eq("V<sub>m</sub> = Q<sub>a</sub>/(0.16 k) m<sup>3</sup>", "4.34"))
    b.append(p("Due to the nature of airflow in outdoor conditions, Equation "
               "4.34 is likely to give a pessimistic (overlarge) volume of "
               "explosive atmosphere. The series also includes Equation 4.35, "
               "intended to allow the calculation of dispersion time after the "
               "release has stopped, where LEL is the lower explosive limit (%) "
               "and UL is the maximum concentration (% v/v)."))
    b.append(eq("t = (f/C) Ln (LEL k/UL) s", "4.35"))
    b.append(note("<b>Equation 4.35 caveat.</b> The printed grouping 'Ln (LEL "
                  "kUL)' is ambiguous; the form shown follows the brief's "
                  "reading of Example 6, Ln(0.5 × 2.7/100). That logarithm "
                  "is negative and the book reports its magnitude as 27 s."))
    b.append(p("To assist in the use of this equation where ventilation is poor "
               "(indoors, where no extra ventilation is added), the text directs "
               "the reader to 'Table 4.1', said to be derived from a table in "
               "the guide book of the Building Services Institute<sup>7</sup> "
               "used to calculate the heating needed for a building from losses "
               "due to natural ventilation."))
    b.append(note("<b>Table-number anomaly in Section 4.5.</b> No ventilation "
                  "table is printed in this chapter: Table 4.1 is the ten-page "
                  "BS 5345 flammable-materials table. The printed cross-reference "
                  "is kept as a reference only; no ventilation table has been "
                  "invented or mapped to it."))
    b.append(h4("4.5.1 Example of gas release using BS/EN 10079-10<sup>3</sup> formulae",
                "4.5.1 Example of gas release using BS/EN 10079-10<sup>3</sup> formulae"))
    b.append(note("<b>Heading typo.</b> The printed heading reads BS/EN "
                  "10079-10<sup>3</sup>; the body text and Reference 3 give "
                  "BS/EN 60079-10. The printed number is retained in the heading "
                  "and flagged here."))
    b.append(p("<b>Example 6.</b> The ethylene release discussed in Example 1 "
               "occurs indoors in a building which is well ventilated (f = 1). "
               "The text states a mass release rate of 0.55 kg/s; the "
               "substitution that follows uses 0.475 kg/s."))
    b.append(p("Using Equation 4.31 for the airflow required at the leak: "
               "Q<sub>a</sub> = 0.03 × 0.475 × 295²/(28 × 2.7) "
               "= <b>16.4 m³/s</b>."))
    b.append(p("This value is used in Equation 4.34 to give the maximum volume "
               "of flammable atmosphere in the enclosed space, ventilated at "
               "the same rate as an open space ventilated by the wind: "
               "Q<sub>m</sub> = 16.4/0.16 × 0.5 = <b>205 m³</b>."))
    b.append(p("This volume gives a larger overall hazardous area than would "
               "actually exist outdoors (estimated at between 20 m and 45 m in "
               "the direction of ventilation flow from the leakage source), "
               "because the volume is not a sphere. Equation 4.34 therefore "
               "applies only to enclosed finite spaces where the ventilation "
               "conditions are similar, not to the outdoor situation."))
    b.append(p("Applying Equation 4.35 gives the persistence time after the "
               "release ends: t = (1/0.16) Ln(0.5 × 2.7/100) = "
               "<b>27 s</b>. Again this is a very high figure for an outside "
               "location but more realistic indoors, where the overall volume "
               "is more limited."))
    b.append(note("<b>Printed-error note for Example 6.</b> The stated mass "
                  "release of 0.55 kg/s conflicts with the 0.475 kg/s "
                  "substituted (Example 1 itself gave 0.03 kg/s). The volume "
                  "result is labelled Q<sub>m</sub> in the book but is the "
                  "quantity V<sub>m</sub> of Equation 4.34; the printed "
                  "substitution 16.4/0.16 × 0.5 yields 205 m³ only when "
                  "the denominator is read as 0.16 × 0.5. The logarithm in "
                  "Equation 4.35 is negative and its magnitude is reported as "
                  "27 s. All printed figures are retained."))
    b.append(h3("4.6 Conclusion", "4.6 Conclusion"))
    b.append(p("This chapter contains a relatively comprehensive set of "
               "calculations for determining the extents of hazardous areas. "
               "Those concerned with outdoor areas for vapours and for liquids "
               "have been extensively used for several years and basically "
               "agree with the subjective judgements found in several codes, "
               "and thus have some pedigree. The formulae in Section 4.4, "
               "however, are newer."))
    b.append(p("Until they have been in use for a considerable time and "
               "evidence has amassed, they should be used with extreme care. It "
               "is suggested that initially they be used as yardstick "
               "calculations only (for example, to determine whether the "
               "persistence time in a particular circumstance would cause a "
               "secondary source of release to produce a Zone 1 indoors). It is "
               "stressed that there is no intent to suggest that they are not "
               "accurate, but merely that experience must be accumulated by "
               "practising engineers. This set of formulae will also be more "
               "difficult to use in cases of liquid release, particularly where "
               "the liquid is below its boiling point."))
    b.append(p("Finally, Table 4.1 is included (Fig. 4.5 from BS 5345 Part 2<sup>1</sup>) "
               "and gives some of the information necessary to use the "
               "calculative methods in this chapter. The table also includes "
               "columns titled 'Group' and 'Temperature Class', which refer to "
               "apparatus performance and are described in more detail in "
               "Chapter 7; they are listed here to identify the relationship "
               "between the explosive atmospheres occurring and the type of "
               "apparatus that should be used."))
    b.append(note("<b>Table/figure anomaly in Section 4.6.</b> The text cites "
                  "'Fig. 4.5 from BS 5345 Part 2' as the source of Table 4.1, but "
                  "no Figure 4.4 or 4.5 is printed in this chapter. The citation "
                  "is kept verbatim as a source reference; no such figure has "
                  "been created."))
    return "".join(b)
