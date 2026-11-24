# -*- coding: utf-8 -*-
"""Book 7, Chapter 5, Section A — Valve Sizing Made Easy (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), PDF pp. 30-35,
printed pp. 23-28. Covers the Cv definition, the two limitations of the basic
equation, choked flow, the liquid and gas/steam sizing formulas, the special
case, "Other Methods", and the worked example ending "when in doubt, use a
full-trim size". No figures and no tables in this span.
"""
from cvp_common import eq, h2, h3, ol, p, ul

PAGES_SRC = 6
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valve Sizing Made Easy"
TITLE_VI = "Định cỡ van dễ dàng"


def body_vi():
    b = []
    b.append(h2("Định cỡ van", "Valve Sizing"))
    b.append(p("Hoạt động này có thể được định nghĩa là chọn đúng kích cỡ van cho công việc, "
               "hoặc trong những trường hợp kích cỡ van đã được định sẵn, là chọn đúng kích "
               "cỡ bộ trim (lõi van)."))
    b.append(p("Đừng đọc tiếp nếu bạn có một máy tính đã được lập trình đầy đủ các phương "
               "trình ANSI/ISA-75.01.01 [1]. Nhưng mặt khác, có thể bạn muốn biết mình đang "
               "làm gì, hoặc ít nhất là muốn kiểm tra lại kết quả của máy tính."))
    b.append(p("Để giúp việc này dễ dàng, khoảng 60 năm trước, một ai đó thông minh đã phát "
               "minh ra hệ số định cỡ van (C<sub>v</sub>), gộp diện tích dòng chảy của lỗ "
               "van, hệ số co thắt và hệ số tổn thất áp lực thành một; như sau:"))
    b.append(eq("C<sub>v</sub> = q / √(ΔP/G<sub>f</sub>) = "
                "q √(G<sub>f</sub>/ΔP)", "5-1"))
    b.append(eq("q = C<sub>v</sub> √(ΔP/G<sub>f</sub>) = "
                "C<sub>v</sub> (ΔP/G<sub>f</sub>)<sup>0.5</sup>", "5-2"))
    b.append(p("Trong đó:"))
    b.append(ul([
        "q = lưu lượng tính bằng gallon Mỹ mỗi phút",
        "G<sub>f</sub> = trọng lượng riêng của chất lỏng ở một nhiệt độ cho trước (nước ở "
        "60°F có G<sub>f</sub> bằng 1)",
        "ΔP = áp suất đầu vào trừ áp suất đầu ra, tính bằng psi",
    ]))
    b.append(p("Do đó, một C<sub>v</sub> bằng lưu lượng một gallon Mỹ mỗi phút của nước ở "
               "60°F và với độ giảm áp qua van là 1 psi. Bây giờ cùng một van sẽ cho chảy "
               "10 gpm ở độ giảm áp 100 psi, vì lưu lượng tỷ lệ thuận với căn bậc hai của "
               "ΔP, tuân theo các định luật của cơ học chất lỏng. Nên ghi nhớ phương "
               "trình này vì bạn sẽ dùng nó trong ít nhất 80% số bài toán định cỡ chất "
               "lỏng. Tiếc là không phải mọi thứ trong cuộc sống đều đơn giản như vậy; vì "
               "thế, chúng ta phải thừa nhận hai hạn chế khi dùng các phương trình trên."))
    b.append(p("Thứ nhất, các phương trình này chỉ áp dụng cho dòng chảy rối, tức là số "
               "Reynolds trên khoảng 5000. Tuy nhiên, bạn có thể bỏ qua giới hạn này khi "
               "C<sub>v</sub> yêu cầu lớn hơn 0.1 và khi độ nhớt động học thấp hơn 40 "
               "centistokes (90% chất lỏng là như vậy). Sẽ còn nói thêm về chủ đề này ở "
               "phần sau của chương — chỉ nên đọc nếu bạn điều khiển nhựa đường hoặc các "
               "chất dính tương tự và polyme."))
    b.append(p("Thứ hai, trong một số điều kiện, những hiện tượng kỳ lạ xảy ra bên trong van "
               "dường như bịt kín các đường dòng. Điều thực sự xảy ra là ở một tỷ lệ nhất "
               "định giữa độ giảm áp và áp suất đầu vào, được xác định bởi hệ số phục hồi "
               "áp suất (F<sub>L</sub><sup>2</sup>), dòng chảy bị nghẽn tại lỗ van. "
               "(F<sub>L</sub> ban đầu được gọi là hệ số dòng chảy tới hạn [2], C<sub>f</sub>, "
               "và được dùng như vậy.) Với chất lỏng, điều này do một phần chất lỏng hóa hơi "
               "gây ra (xem thêm Chương 15, “Cavitation”), còn với khí, đó là sự xuất hiện "
               "của vận tốc âm thanh. Điều này sẽ không đáng kể nếu không phải vì hiện tại "
               "lưu lượng không còn phụ thuộc vào áp suất hạ lưu (P<sub>2</sub>). Bây giờ "
               "lưu lượng chỉ có thể tăng nếu bạn dùng áp suất đầu vào cao hơn. Xem Chương 6."))
    b.append(p("Để tránh những sai sót đáng xấu hổ, bước đầu tiên là xác định xem bạn có "
               "dòng chảy tới hạn (nghẽn) hay không bằng các phương trình sau (điều này "
               "cũng giúp phát hiện các vấn đề về cavitation hay tiếng ồn mà bạn có thể "
               "phải lo tâm)."))
    b.append(p("Lưu ý, hãy dùng (F<sub>Lp</sub>/F<sub>p</sub>)<sup>2</sup> thay cho "
               "F<sub>L</sub><sup>2</sup> trong các phương trình sau bất cứ khi nào van "
               "được lắp giữa hai đoạn thu nhỏ đường ống; F<sub>Lp</sub> là hệ số phục hồi "
               "áp suất áp dụng khi van được lắp giữa các đoạn thu nhỏ."))
    b.append(eq("F<sub>Lp</sub> = F<sub>L</sub> / √{1 + "
                "(F<sub>L</sub><sup>2</sup> C<sub>v</sub><sup>2</sup>)/(0.1 d<sup>4</sup>) "
                "[1 − (d/D)<sup>4</sup>]}", "5-3"))
    b.append(p("Ở đây d = kích cỡ van (in), D = kích cỡ đường ống (in) và F<sub>p</sub> = "
               "hệ số hình học đường ống."))
    b.append(p("Về F<sub>p</sub>, hệ số hình học đường ống, xem mục “Pipe Reducers” trong "
               "chương này."))

    b.append(h2("Đối với dịch vụ chất lỏng", "For Liquid Service"))
    b.append(p("Dòng dưới tới hạn (Subcritical Flow) — xảy ra khi ΔP nhỏ hơn "
               "F<sub>L</sub><sup>2</sup> (P<sub>1</sub> − P<sub>v</sub>). Dòng tới "
               "hạn (Critical Flow) — xảy ra khi ΔP lớn hơn F<sub>L</sub><sup>2</sup> "
               "(P<sub>1</sub> − P<sub>v</sub>)."))
    b.append(p("Lưu lượng thể tích (Volumetric Flow)"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = q √(G<sub>f</sub>/ΔP), "
                "q = C<sub>v</sub> √(ΔP/G<sub>f</sub>)<br>"
                "Tới hạn: C<sub>v</sub> = q/[F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))], "
                "q = C<sub>v</sub> F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))", "5-4"))
    b.append(p("Lưu lượng theo trọng lượng (Flow by Weight)"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = W/[500 √(G<sub>f</sub>ΔP)], "
                "W = 500 C<sub>v</sub> √(G<sub>f</sub>ΔP)<br>"
                "Tới hạn: C<sub>v</sub> = W/[500 F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))], "
                "W = 500 C<sub>v</sub> F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))", "5-5"))
    b.append(p("Trong đó:"))
    b.append(ul([
        "G<sub>f</sub> = trọng lượng riêng ở nhiệt độ dòng chảy (nước = 1 ở 60°F)",
        "P<sub>1</sub> = áp suất đầu vào tuyệt đối, psia",
        "P<sub>2</sub> = áp suất đầu ra tuyệt đối, psia",
        "ΔP = P<sub>1</sub> − P<sub>2</sub>",
        "P<sub>c</sub> = áp suất tại điểm tới hạn nhiệt động, psia — nước = 3206 psia",
        "P<sub>v</sub> = áp suất hơi của chất lỏng ở nhiệt độ dòng chảy, psia — nước = "
        "0.4 psia ở 70°F",
        "q = lưu lượng chất lỏng, US gpm",
        "W = lưu lượng tính bằng pound mỗi giờ",
    ]))
    b.append(h3("Trường hợp đặc biệt", "Special Case"))
    b.append(p("Khi áp suất đầu ra thấp hơn hoặc bằng áp suất hơi, hãy dùng "
               "ΔP<sub>s</sub> thay cho ΔP trong các phương trình lưu lượng "
               "thể tích và lưu lượng theo trọng lượng."))
    b.append(eq("ΔP<sub>s</sub> = P<sub>1</sub> − "
                "[0.96 − 0.28 (P<sub>v</sub>/P<sub>c</sub>)] P<sub>v</sub>"))

    b.append(h2("Đối với dịch vụ khí và hơi", "For Gas and Steam Service"))
    b.append(p("Dù nghe có vẻ lạ, phương trình C<sub>v</sub> cơ bản cũng có thể áp dụng "
               "cho khí và hơi. Điểm khác biệt ở đây là mật độ của khí thay đổi theo "
               "ΔP và, vì đó là một quá trình dần dần, mối quan hệ với lưu lượng "
               "không còn là tuyến tính mà là đường cong. Để ghi nhận công lao của mình, "
               "Ủy ban Định cỡ của Hiệp hội Tự động hóa Quốc tế (ISA) dành cho "
               "ANSI/ISA-75.01.01 đã nỗ lực rất nhiều để dự đoán chính xác hình dạng của "
               "đường cong này với sự trợ giúp của hệ số giãn nở [3], Y, trong đó:"))
    b.append(eq("Y = 1 − X/(3 F<sub>k</sub> X<sub>T</sub>)", "5-6"))
    b.append(p("Lưu ý rằng Y không thể vượt quá 1 và không thể nhỏ hơn 0.67, bởi vì giá "
               "trị sau đúng bằng mật độ của khí, tức là 67% mật độ đầu vào khi van bị "
               "nghẽn (khi lưu lượng đạt vận tốc âm thanh trong lỗ van)."))
    b.append(p("<sup>1</sup> Có bằng chứng cho thấy số C<sub>v</sub> ở một số kiểu van "
               "nhất định, chẳng hạn van góc, một số van quay và van cầu hai cổng, khác "
               "nhau giữa chất lỏng và khí, nhưng chúng ta sẽ bỏ qua điều này."))
    b.append(p("Trong phương trình trên:"))
    b.append(ul([
        "X = ΔP/P<sub>1</sub> (Lưu ý: P<sub>1</sub> hoặc P<sub>2</sub> luôn là áp "
        "suất tuyệt đối, tức là psi thước đo cộng 14.7.)",
        "F<sub>k</sub> = tỷ lệ nhiệt dung riêng k của khí (không khí = 1.4), "
        "F<sub>k</sub> = k của khí/1.4",
        "X<sub>T</sub> = tỷ lệ giảm áp (đây là ΔP/P<sub>1</sub> mà tại đó lưu "
        "lượng không còn tăng nữa)",
    ]))
    b.append(p("Lưu ý rằng X<sub>T</sub> bao gồm một phần tăng lưu lượng sau khi bắt đầu "
               "dòng chảy nghẽn, do sự thay đổi kích thước của tia chảy (vena contracta)."))
    b.append(p("Bây giờ hệ số lưu lượng cần thiết trở thành:"))
    b.append(eq("C<sub>v</sub> = q √(G<sub>g</sub> T<sub>1</sub> Z) / "
                "[1360 Y √(X P<sub>1</sub>)]", "5-7"))
    b.append(p("Hoặc"))
    b.append(eq("q = 1360 C<sub>v</sub> Y √(X P<sub>1</sub> / "
                "(G<sub>g</sub> T<sub>1</sub> Z))", "5-8"))
    b.append(p("Trong đó:"))
    b.append(ul([
        "q = lưu lượng tính bằng feet khối tiêu chuẩn mỗi giờ (SCFH)",
        "G<sub>g</sub> = trọng lượng riêng của khí (không khí = 1), cũng là tỷ lệ giữa "
        "khối lượng phân tử của khí và của không khí (không khí = 28.9)",
        "T<sub>1</sub> = nhiệt độ tuyệt đối phía trên, °R (°F + 460)",
        "Z = hệ số nén (Bỏ qua nếu áp suất của bạn không bao giờ vượt quá 2000 psia; "
        "nếu không, hãy tra cứu bảng trong sổ tay.)",
    ]))
    b.append(p("Giờ, nếu điều này bắt đầu vượt quá khả năng của máy tính cầm tay, bạn có "
               "thể bỏ qua tất cả những điều trên và dùng phiên bản đơn giản sau [4]. "
               "(Hình phạt là sai số định cỡ tối đa ≈ 8% tại điểm chuyển tiếp từ dòng "
               "không nghẽn sang dòng nghẽn và không đáng để bận tâm.) Người ta cũng "
               "khuyên bạn nên dùng các phương trình đơn giản này để kiểm tra xem kết "
               "quả do máy tính đưa ra có ít nhất nằm trong khoảng hợp lý hay không."))
    b.append(p("Dòng dưới tới hạn (Subcritical Flow) — khi ΔP nhỏ hơn "
               "F<sub>L</sub><sup>2</sup> (P<sub>1</sub>/2). Dòng tới hạn (Critical "
               "Flow) — khi ΔP lớn hơn F<sub>L</sub><sup>2</sup> (P<sub>1</sub>/2)."))
    b.append(p("Lưu lượng thể tích (Volumetric Flow)"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = q √(G<sub>g</sub> T)/"
                "[963 √(ΔP (P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Tới hạn: C<sub>v</sub> = q √(G<sub>g</sub> T)/"
                "(834 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("Lưu lượng theo trọng lượng (Flow by Weight)"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = W/[32.2 √(G<sub>g</sub> ΔP "
                "(P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Tới hạn: C<sub>v</sub> = W/(28 F<sub>L</sub> G<sub>g</sub> P<sub>1</sub>)"))
    b.append(p("Đối với hơi bão hòa"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = W/[21 √(ΔP(P<sub>1</sub> + "
                "P<sub>2</sub>))]<br>"
                "Tới hạn: C<sub>v</sub> = W/(18.3 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("Đối với hơi quá nhiệt"))
    b.append(eq("Dưới tới hạn: C<sub>v</sub> = W (1 + T<sub>sh</sub>/1000)<sup>0.7</sup>/"
                "[21 √(ΔP(P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Tới hạn: C<sub>v</sub> = W (1 + T<sub>sh</sub>/1000)<sup>0.7</sup>/"
                "(18.3 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("Trong đó:"))
    b.append(ul([
        "C<sub>v</sub> = hệ số van",
        "F<sub>L</sub> = hệ số phục hồi áp suất",
        "G<sub>g</sub> = trọng lượng riêng của khí (không khí = 1.0)",
        "P<sub>1</sub> = áp suất tuyệt đối phía thượng lưu, psia",
        "P<sub>2</sub> = áp suất tuyệt đối phía hạ lưu, psia",
        "ΔP = độ giảm áp P<sub>1</sub> − P<sub>2</sub>, psi",
        "q = lưu lượng khí ở 14.7 psia và 60°F, SCFH",
        "T = nhiệt độ dòng chảy, °R (460 + °F)",
        "T<sub>sh</sub> = độ quá nhiệt của hơi, °F",
        "W = lưu lượng, pound mỗi giờ",
    ]))
    b.append(p("Lưu ý: Khi van được lắp giữa các đoạn thu nhỏ, hãy dùng C<sub>v</sub> "
               "F<sub>p</sub> thay cho C<sub>v</sub> trong bảng năng lực (xem mục "
               "“Pipe Reducers” trong chương này)."))

    b.append(h2("Các phương pháp khác", "Other Methods"))
    b.append(eq("C<sub>v</sub> = C<sub>g</sub>/(40 F<sub>L</sub>) = "
                "C<sub>s</sub>/(2 F<sub>L</sub>);   X<sub>T</sub> = "
                "0.84 F<sub>L</sub><sup>2</sup>/F<sub>k</sub>;   "
                "F<sub>L</sub> = F<sub>k</sub>/F<sub>C</sub>"))
    b.append(p("Lưu ý: X<sub>T</sub> không liên hệ chặt chẽ với F<sub>L</sub>. Trong khi "
               "X<sub>T</sub> cho bạn lưu lượng khí tối đa (có thể xảy ra ở tỷ lệ áp suất "
               "lỗ van P<sub>1</sub>/P<sub>0</sub> từ 3:1 trở lên, tức là trên vận tốc "
               "âm thanh), thì F<sub>L</sub><sup>2</sup> cho biết sự bắt đầu của vận tốc "
               "âm thanh, tức là nơi P<sub>1</sub>/P<sub>orifice</sub> ≈ 2, và "
               "P<sub>1</sub>/P<sub>2,sonic</sub> = P<sub>1</sub>/(P<sub>1</sub> − "
               "0.5 F<sub>L</sub><sup>2</sup> P<sub>1</sub>)."))

    b.append(h2("Điều kiện dòng chảy đúng là gì?", "What Are the Right Flow Conditions?"))
    b.append(p("Dùng máy tính và định cỡ số C<sub>v</sub> đến năm chữ số thập phân thì "
               "rất tốt, nhưng chỉ khi bạn có đúng điều kiện công nghệ. Trước hết, van "
               "nên được định cỡ để điều khiển lưu lượng tối đa mà quá trình được thiết "
               "kế. Nhưng chính xác thì đó là gì? Còn các điều kiện khẩn cấp thì sao? "
               "Mặt khác, nếu van bị hỏng ở trạng thái mở (fail open), lưu lượng kết quả "
               "có vượt quá khả năng của van xả áp hạ lưu không? Rồi lại, áp suất đầu vào "
               "đúng là bao nhiêu? Bạn có dùng áp suất cột của bơm từ đường cong do nhà "
               "sản xuất công bố không? (Nếu có, hãy dùng áp suất cột tương ứng với lưu "
               "lượng tối đa mà van phải cho qua, và đừng bỏ qua cột tĩnh tại vị trí của "
               "bơm.) Độ tổn thất áp hay độ giảm áp qua một bộ trao đổi nhiệt đặt cạnh "
               "van là bao nhiêu? Còn tổn thất đường ống thì sao? Tất cả những câu hỏi "
               "này chỉ gợi được những câu trả lời mơ hồ từ các kỹ sư thiết kế quá trình "
               "của bạn. Họ không biết câu trả lời và phải dựa vào dữ liệu từ các nhà "
               "cung cấp khác. Kết quả thường là đoán mò với rất nhiều hệ số an toàn được "
               "chèn thêm. Vì vậy, đừng quá lo lắng về độ chính xác của các phương trình "
               "định cỡ. Trong 99 trường hợp trên 100, van vẫn quá lớn so với công việc "
               "(xem Chương 8 về trim tỷ lệ phần trăm bằng nhau). 1% còn lại bị thiếu kích "
               "cỡ là do ai đó mắc lỗi dấu thập phân trong phép tính C<sub>v</sub>."))
    b.append(p("Nếu bạn muốn khôn khéo và tiết kiệm năng lượng cùng tiền bạc cho công ty, "
               "hãy để nhân viên công nghệ yêu cầu bạn cung cấp độ giảm áp của van khi họ "
               "thiết kế hệ thống (xem Chương 18, “The ABC Method for Gases”). Giờ bạn "
               "đang ngồi ghế lái. Đây là những quy tắc ngón tay cái được suy luận khoa "
               "học mà bạn nên ghi nhớ: khi định cỡ ΔP cho van, hãy dùng giá trị lớn "
               "hơn giữa 5% tổng áp suất hệ thống (tức là cột tĩnh cộng cột bơm ở lưu "
               "lượng tối đa, áp suất nồi hơi, v.v.) và 5 psi đối với van điều khiển kiểu "
               "quay, hoặc 10 psi đối với van cầu."))
    b.append(p("Bạn có thể tự hỏi tại sao tôi chọn 5 psi cho van điều khiển kiểu quay. "
               "Tình cờ là lưu lượng (cả chất lỏng lẫn khí) tạo ra bởi độ giảm áp 5 psi "
               "qua một van điều khiển mở hoàn toàn có C<sub>v</sub> chia cho bình "
               "phương đường kính van bằng 172, chính là mức mà một đường ống (cùng kích "
               "cỡ với van) có thể chở, với vận tốc đường ống tối đa thông thường là "
               "15 ft/s cho chất lỏng hoặc 150 ft/s cho khí [5] (xem Hình 5-1). Giá trị "
               "ΔP cao hơn bắt buộc phải dùng van nhỏ hơn kích cỡ đường ống, khi "
               "cần đoạn thu nhỏ hoặc khi chọn trim giảm.<sup>3</sup> Dù sao, bạn đang "
               "vứt bỏ tiền cho công suất bơm, máy nén hoặc nồi hơi nếu gán quá nhiều độ "
               "giảm áp cho van (xem Chương 18)."))
    b.append(p("<sup>2</sup> Ví dụ, van bướm ở góc mở 60°.<br>"
               "<sup>3</sup> Ví dụ, nếu van bướm 4 inch được lắp trong đường ống 6 inch, "
               "thì ở 17 × d<sup>2</sup> = 272 C<sub>v</sub>, độ giảm áp của van tăng từ "
               "5 psi lên 25 psi với vận tốc chất lỏng 15 ft/s trong đường ống 6 inch."))
    b.append(p("Tất nhiên, mẹo trên có thể dùng ngược lại. Bạn có thể được yêu cầu thay "
               "thế một van giảm áp hơi cũ, từ năm 1948. Mọi hồ sơ đều bị mất, và điều "
               "duy nhất bạn biết là áp suất nồi hơi cùng kích cỡ van và ống. Giả sử áp "
               "suất nồi hơi là 95 psig (110 psia) và kích cỡ ống là 1½ in. Trước tiên, "
               "tra cứu lưu lượng tối đa của một ống hơi 1½ inch ở, chẳng hạn, 100 psig. "
               "Bạn sẽ thấy khoảng 1800 lb/h (xem Bảng A-2 trong Phụ lục A, "
               "“References—Tables and Figures”). Tiếp theo, giả sử dòng chảy bị nghẽn, "
               "tức là P<sub>2</sub> nhỏ hơn một nửa P<sub>1</sub>. (Dù sao, người ta "
               "cũng không mấy quan tâm đến tiết kiệm năng lượng vào năm 1948.) Bây giờ "
               "hãy tính C<sub>v</sub> cần thiết, khoảng 10.5. Cứ thoải mái chọn một van "
               "cầu 1½-inch có C<sub>v</sub> định mức khoảng 22. Điều tệ nhất có thể xảy "
               "ra là áp suất đầu ra là 80 psig thay vì dưới 50 psig. Không sao cả. Lúc "
               "này C<sub>v</sub> cần thiết là 16, vẫn ổn. Vì vậy, khi còn nghi ngờ, hãy "
               "dùng kích cỡ trim đầy đủ nếu điều kiện dòng chảy chưa biết, trừ các ứng "
               "dụng đặc biệt chẳng hạn như điều khiển pH."))
    b.append(p("<b>Ghi chú nguồn.</b> Nhiều công thức trong nguyên bản bị OCR làm méo "
               "(đặc biệt là (5-3), (5-4), (5-5), (5-7) và (5-8) cùng các phương trình "
               "không đánh số); bản dịch dựng lại theo dạng ký hiệu chuẩn của ISA. Một số "
               "hệ số trong phương trình rút gọn (32.2, 28, 18.3, 0.7) được giữ theo "
               "nguyên bản dù glyph bị lỗi."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Định cỡ van", "Valve Sizing"))
    b.append(p("This activity can be defined as picking the right size valve for the job "
               "or, in instances where a valve size is predestined, the correct trim size."))
    b.append(p("Do not read on if you have a computer fully programmed with ANSI/"
               "ISA-75.01.01 equations [1]. But then again, you may want to know what you "
               "are doing, or if nothing else, you may want to double-check the computer "
               "results."))
    b.append(p("To help matters, about 60 years ago some clever soul invented a valve "
               "sizing coefficient (C<sub>v</sub>), which combined the flow area of the "
               "valve orifice, the contraction coefficient, and the head loss coefficient "
               "in one; thus,"))
    b.append(eq("C<sub>v</sub> = q / √(ΔP/G<sub>f</sub>) = "
                "q √(G<sub>f</sub>/ΔP)", "5-1"))
    b.append(eq("q = C<sub>v</sub> √(ΔP/G<sub>f</sub>) = "
                "C<sub>v</sub> (ΔP/G<sub>f</sub>)<sup>0.5</sup>", "5-2"))
    b.append(p("where"))
    b.append(ul([
        "q = the flow rate in US gallons per minute",
        "G<sub>f</sub> = the specific gravity of a liquid at a given temperature (water "
        "at 60°F has a G<sub>f</sub> of 1)",
        "ΔP = inlet minus outlet pressure in psi",
    ]))
    b.append(p("Therefore, one C<sub>v</sub> equals the flow of one US gallon per minute "
               "of water at 60°F and under a pressure drop across the valve of 1 psi. Now "
               "the same valve will flow 10 gpm at a pressure drop of 100 psi because the "
               "flow is proportional to the square root of ΔP, thus following the "
               "laws of fluid mechanics. It is worthwhile to memorize this equation "
               "because you will use it on at least 80% of all sizing problems for "
               "liquids. Unfortunately, not all in life is so simple; therefore, we must "
               "recognize two limitations in the use of the abovementioned equations."))
    b.append(p("First, they only apply to turbulent flow, that is, Reynolds numbers above "
               "about 5000. However, you can ignore this limit on required C<sub>v</sub> "
               "numbers above 0.1 and when the kinematic viscosity is below 40 "
               "centistokes (90% of all liquids are). There will be more on this subject "
               "later in this chapter—required reading only if you control tar or equally "
               "sticky substances and polymers."))
    b.append(p("Second, in some conditions funny things occur inside the valve that seem "
               "to block the flow passages. What really happens is that at a certain "
               "ratio of pressure drop to inlet pressure defined by a pressure recovery "
               "factor (F<sub>L</sub><sup>2</sup>), the flow becomes choked at the orifice. "
               "(F<sub>L</sub> originally was called the critical flow factor [2], "
               "C<sub>f</sub>, and was used as such.) In the case of liquids, this is "
               "caused by the evaporation of some of the liquid (also see Chapter 15, "
               "“Cavitation”), and in the case of gases, the onset of sonic velocity. "
               "This would be inconsequential was it not for the fact that now the flow "
               "is independent of the downstream pressure (P<sub>2</sub>). Now the "
               "flowing quantity can only increase if you use a higher inlet pressure. "
               "See Chapter 6."))
    b.append(p("To avoid embarrassing errors, the first step is to determine whether you "
               "have critical (choked) flow or not using the following equations (this "
               "also helps to discover any cavitation or noise problems you may have to "
               "worry about)."))
    b.append(p("Note, use (F<sub>Lp</sub>/F<sub>p</sub>)<sup>2</sup> instead of "
               "F<sub>L</sub><sup>2</sup> in the following equations whenever you have a "
               "valve between pipe reducers; F<sub>Lp</sub> is the pressure recovery "
               "factor that applies when valves are installed between reducers."))
    b.append(eq("F<sub>Lp</sub> = F<sub>L</sub> / √{1 + "
                "(F<sub>L</sub><sup>2</sup> C<sub>v</sub><sup>2</sup>)/(0.1 d<sup>4</sup>) "
                "[1 − (d/D)<sup>4</sup>]}", "5-3"))
    b.append(p("Here d = valve size (in), D = pipe size (in), and F<sub>p</sub> = the "
               "piping geometry factor."))
    b.append(p("For F<sub>p</sub>, the piping geometry factor, see the “Pipe Reducers” "
               "section in this chapter."))

    b.append(h2("Đối với dịch vụ chất lỏng", "For Liquid Service"))
    b.append(p("Subcritical Flow — occurs when ΔP is less than F<sub>L</sub>"
               "<sup>2</sup> (P<sub>1</sub> − P<sub>v</sub>). Critical Flow — "
               "occurs when ΔP is more than F<sub>L</sub><sup>2</sup> "
               "(P<sub>1</sub> − P<sub>v</sub>)."))
    b.append(p("Volumetric Flow"))
    b.append(eq("Subcritical: C<sub>v</sub> = q √(G<sub>f</sub>/ΔP), "
                "q = C<sub>v</sub> √(ΔP/G<sub>f</sub>)<br>"
                "Critical: C<sub>v</sub> = q/[F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))], "
                "q = C<sub>v</sub> F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))", "5-4"))
    b.append(p("Flow by Weight"))
    b.append(eq("Subcritical: C<sub>v</sub> = W/[500 √(G<sub>f</sub>ΔP)], "
                "W = 500 C<sub>v</sub> √(G<sub>f</sub>ΔP)<br>"
                "Critical: C<sub>v</sub> = W/[500 F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))], "
                "W = 500 C<sub>v</sub> F<sub>L</sub> √(G<sub>f</sub>"
                "(P<sub>1</sub> − P<sub>v</sub>))", "5-5"))
    b.append(p("where"))
    b.append(ul([
        "G<sub>f</sub> = specific gravity at flowing temperature (water = 1 at 60°F)",
        "P<sub>1</sub> = absolute inlet pressure, psia",
        "P<sub>2</sub> = absolute outlet pressure, psia",
        "ΔP = P<sub>1</sub> − P<sub>2</sub>",
        "P<sub>c</sub> = pressure at thermodynamic critical point, psia — water = 3206 psia",
        "P<sub>v</sub> = vapor pressure of liquid at flowing temperature, psia — water = "
        "0.4 psia at 70°F",
        "q = liquid flow rate, US gpm",
        "W = flow in pounds per hour",
    ]))
    b.append(h3("Trường hợp đặc biệt", "Special Case"))
    b.append(p("When outlet pressure is lower than or equal to vapor pressure, use "
               "ΔP<sub>s</sub> in place of ΔP in the volumetric flow and flow "
               "by weight equations."))
    b.append(eq("ΔP<sub>s</sub> = P<sub>1</sub> − "
                "[0.96 − 0.28 (P<sub>v</sub>/P<sub>c</sub>)] P<sub>v</sub>"))

    b.append(h2("Đối với dịch vụ khí và hơi", "For Gas and Steam Service"))
    b.append(p("Surprising as it may sound, the basic C<sub>v</sub> equation can also be "
               "applied to gases and steam. The difference here is that the density of "
               "the gas changes with ΔP, and, because this is a gradual process, "
               "the relationship to flow is no longer linear but curved. To its credit, "
               "the International Society of Automation (ISA) Sizing Committee for "
               "ANSI/ISA-75.01.01 has labored hard to predict the exact shape of this "
               "curve with the aid of an expansion factor [3], Y, where"))
    b.append(eq("Y = 1 − X/(3 F<sub>k</sub> X<sub>T</sub>)", "5-6"))
    b.append(p("Note that Y cannot exceed 1 and that it cannot be less than 0.67 because "
               "the latter is exactly the density of the gas, that is, 67% of the inlet "
               "density when the valve is choked (when it sees sonic velocity in the "
               "valve orifice)."))
    b.append(p("<sup>1</sup> There is evidence that the C<sub>v</sub> number on certain "
               "valve types, such as angle valves, certain rotary valves, and "
               "double-ported globe valves, is different between liquid and gases, but we "
               "shall ignore this."))
    b.append(p("In the preceding equation,"))
    b.append(ul([
        "X = ΔP/P<sub>1</sub> (Note: P<sub>1</sub> or P<sub>2</sub> is always "
        "absolute pressure, that is, gauge psi plus 14.7.)",
        "F<sub>k</sub> = the ratio of the specific heat k of a gas (air = 1.4), "
        "F<sub>k</sub> = k of gas/1.4",
        "X<sub>T</sub> = pressure drop ratio (this is the ΔP/P<sub>1</sub> at which "
        "there is no longer any flow increase)",
    ]))
    b.append(p("Note that X<sub>T</sub> includes some flow increase after the onset of "
               "choked flow due to changes in the size of the flowing jet (vena contracta)."))
    b.append(p("Now the required flow coefficient becomes:"))
    b.append(eq("C<sub>v</sub> = q √(G<sub>g</sub> T<sub>1</sub> Z) / "
                "[1360 Y √(X P<sub>1</sub>)]", "5-7"))
    b.append(p("Or"))
    b.append(eq("q = 1360 C<sub>v</sub> Y √(X P<sub>1</sub> / "
                "(G<sub>g</sub> T<sub>1</sub> Z))", "5-8"))
    b.append(p("where"))
    b.append(ul([
        "q = flow in standard cubic feet per hour (SCFH)",
        "G<sub>g</sub> = gas specific gravity (air = 1), also ratio of molecular weight "
        "of gas to that of air (air = 28.9)",
        "T<sub>1</sub> = absolute upstream temperature °R (°F + 460)",
        "Z = compressibility factor (Ignore this if your pressure never exceeds 2000 "
        "psia; otherwise, consult handbook tables.)",
    ]))
    b.append(p("Now, if this begins to tax the capabilities of your handheld calculator, "
               "you may ignore all the above and use the simplified version that follows "
               "[4]. (The penalty is a maximum sizing error of ≈ 8% at the transition "
               "from nonchoked to choked flow and not worth the trouble.) It is also "
               "strongly recommended that you use these simplified equations to make sure "
               "your computer-generated answers are at least in the ballpark."))
    b.append(p("Subcritical Flow — when ΔP is less than F<sub>L</sub><sup>2</sup> "
               "(P<sub>1</sub>/2). Critical Flow — when ΔP is more than "
               "F<sub>L</sub><sup>2</sup> (P<sub>1</sub>/2)."))
    b.append(p("Volumetric Flow"))
    b.append(eq("Subcritical: C<sub>v</sub> = q √(G<sub>g</sub> T)/"
                "[963 √(ΔP (P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Critical: C<sub>v</sub> = q √(G<sub>g</sub> T)/"
                "(834 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("Flow by Weight"))
    b.append(eq("Subcritical: C<sub>v</sub> = W/[32.2 √(G<sub>g</sub> ΔP "
                "(P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Critical: C<sub>v</sub> = W/(28 F<sub>L</sub> G<sub>g</sub> P<sub>1</sub>)"))
    b.append(p("For Saturated Steam"))
    b.append(eq("Subcritical: C<sub>v</sub> = W/[21 √(ΔP(P<sub>1</sub> + "
                "P<sub>2</sub>))]<br>"
                "Critical: C<sub>v</sub> = W/(18.3 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("For Superheated Steam"))
    b.append(eq("Subcritical: C<sub>v</sub> = W (1 + T<sub>sh</sub>/1000)<sup>0.7</sup>/"
                "[21 √(ΔP(P<sub>1</sub> + P<sub>2</sub>))]<br>"
                "Critical: C<sub>v</sub> = W (1 + T<sub>sh</sub>/1000)<sup>0.7</sup>/"
                "(18.3 F<sub>L</sub> P<sub>1</sub>)"))
    b.append(p("where"))
    b.append(ul([
        "C<sub>v</sub> = valve coefficient",
        "F<sub>L</sub> = pressure recovery factor",
        "G<sub>g</sub> = gas specific gravity (air = 1.0)",
        "P<sub>1</sub> = absolute upstream pressure, psia",
        "P<sub>2</sub> = absolute downstream pressure, psia",
        "ΔP = pressure drop P<sub>1</sub> − P<sub>2</sub>, psi",
        "q = gas flow rate at 14.7 psia and 60°F, SCFH",
        "T = flow temperature, °R(460 + °F)",
        "T<sub>sh</sub> = steam superheat, °F",
        "W = flow rate, pounds per hour",
    ]))
    b.append(p("Note: When a valve is installed between reducers, use C<sub>v</sub> "
               "F<sub>p</sub> instead of C<sub>v</sub> in capacity tables (see the "
               "“Pipe Reducers” section in this chapter)."))

    b.append(h2("Các phương pháp khác", "Other Methods"))
    b.append(eq("C<sub>v</sub> = C<sub>g</sub>/(40 F<sub>L</sub>) = "
                "C<sub>s</sub>/(2 F<sub>L</sub>);   X<sub>T</sub> = "
                "0.84 F<sub>L</sub><sup>2</sup>/F<sub>k</sub>;   "
                "F<sub>L</sub> = F<sub>k</sub>/F<sub>C</sub>"))
    b.append(p("Note: X<sub>T</sub> is not strictly related to F<sub>L</sub>. While "
               "X<sub>T</sub> gives you the maximum gas flow (which may happen at orifice "
               "pressure ratios P<sub>1</sub>/P<sub>0</sub> of 3:1 or more, that is, above "
               "sonic velocity), F<sub>L</sub><sup>2</sup> tells you the onset of sonic "
               "velocity, that is, where P<sub>1</sub>/P<sub>orifice</sub> ≈ 2, and "
               "P<sub>1</sub>/P<sub>2 sonic</sub> = P<sub>1</sub>/(P<sub>1</sub> − "
               "0.5 F<sub>L</sub><sup>2</sup> P<sub>1</sub>)."))

    b.append(h2("Điều kiện dòng chảy đúng là gì?", "What Are the Right Flow Conditions?"))
    b.append(p("Using a computer and sizing the C<sub>v</sub> number to the fifth place "
               "after the decimal point is all well and good, but only if you have the "
               "right process conditions. First, the valve should be sized to control the "
               "maximum flow rate your process is designed for. But what is this exactly? "
               "How about emergency conditions? On the other hand, should the valve fail "
               "open, would the resultant flow be more than the downstream pressure "
               "relief valve could handle? Then again, what is the correct inlet "
               "pressure? Can you use the head pressure of the pump from the "
               "manufacturer's published curve? (If you do, use the head pressure "
               "corresponding to the maximum flow the valve has to pass, and do not ignore "
               "the static head at the pump's location.) What is the head loss or pressure "
               "drop across a heat exchanger next to the valve? How about line losses? "
               "All these are questions that beg only vague responses from your process "
               "design people. They do not know the answers and have to rely on the input "
               "from other vendors. The result is usually guesswork with ample safety "
               "factors thrown in. Therefore, do not be too concerned about the accuracy "
               "of sizing equations. Ninety-nine out of one hundred times, the valve is "
               "too large for the job anyhow (see Chapter 8 on equal percentage trim). The "
               "remaining 1% that is undersized comes about because someone made a decimal "
               "point error in the C<sub>v</sub> calculation."))
    b.append(p("If you want to be clever and save your company energy and money in the "
               "bargain, have the process people ask you for the valve pressure drop when "
               "they design the system (see Chapter 18, “The ABC Method for Gases”). Now "
               "you are in the driver's seat. Here are the scientifically derived rules "
               "of thumb you should memorize: For ΔP valve sizing, use the higher of "
               "5% of the total system pressure (i.e., static head plus pump head at "
               "maximum flow, boiler pressure, etc.), or 5 psi for rotary control valves, "
               "or 10 psi for globe valves."))
    b.append(p("You may wonder why I picked 5 psi for rotary control valves. It just so "
               "happens that the flow rate (either liquid or gas) generated by a 5 psi "
               "pressure drop through a wide-open control valve with a C<sub>v</sub> "
               "divided by the valve diameter squared of 172 is all that a pipe (the same "
               "size as the valve) can handle, allowing for the customary maximum line "
               "velocities of 15 ft/s for liquids or 150 ft/s for gases [5] (see Figure "
               "5-1). Higher ΔP values mandate a valve smaller than the pipe size "
               "where reducers are required or when reduced trim is selected.<sup>3</sup> "
               "In any case, you are throwing away dollars for pump, compressor, or boiler "
               "horsepowers if you assign too much pressure drop to the valve (see Chapter "
               "18)."))
    b.append(p("<sup>2</sup> A butterfly valve at 60° opening, for example.<br>"
               "<sup>3</sup> For example, if a 4-inch butterfly valve is installed in a "
               "6-inch pipe, then at 17 × d<sup>2</sup> = 272 C<sub>v</sub>, the valve "
               "pressure drop increases from 5 psi to 25 psi with 15 ft/s fluid velocity "
               "in the 6-inch pipe."))
    b.append(p("Of course, the abovementioned trick can be used in reverse. You may be "
               "requested to replace an old steam reducing valve, vintage 1948. All the "
               "records are lost, and the only thing you know is the boiler pressure and "
               "the valve and pipe size. Assume the boiler pressure is 95 psig (110 psia) "
               "and the pipe size is 1½ in. First, look up the maximum flow rate of a "
               "1½-inch steam pipe at, say, 100 psig pressure. You will find it to be "
               "approximately 1800 lb/h (see Table A-2 in Appendix A, “References—Tables "
               "and Figures”). Next, assume the flow to be choked, that is, P<sub>2</sub> "
               "is less than one-half P<sub>1</sub>. (In any case, people did not care much "
               "about energy savings in 1948.) Now calculate the C<sub>v</sub> required, "
               "which is about 10.5. Go ahead and select a 1½-inch globe valve with a "
               "rated C<sub>v</sub> of about 22. The worst that can happen is that the "
               "outlet pressure is 80 psig instead of below 50 psig. No problem. Now the "
               "C<sub>v</sub> required is 16, which is still OK. Therefore, when in doubt, "
               "use a full-trim size if flow conditions are unknown, except in special "
               "applications such as pH control."))
    b.append(p("<b>Source note.</b> Many formulas in the source are mangled by OCR "
               "(notably (5-3), (5-4), (5-5), (5-7) and (5-8) plus the unnumbered "
               "expressions); the rendering reconstructs them in standard ISA notation. "
               "Several coefficients in the simplified equations (32.2, 28, 18.3, 0.7) are "
               "kept as printed even though the glyphs are corrupt."))
    return "".join(b)
