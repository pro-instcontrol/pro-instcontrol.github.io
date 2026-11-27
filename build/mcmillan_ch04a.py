# -*- coding: utf-8 -*-
"""Chapter 4, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 87-89 and 100-102
(PDF pp. 108-110, 121-123).

Covers the chapter opening and the theory of 4.1: the choked-flow
mass-release equation, Eqs. 4.1-4.4 (pp. 88-89), the resumed changeover
and dispersion text (pp. 100-102) with Eqs. 4.5-4.7, and Fig. 4.1.
The ten-page Table 4.1 is a printed insert; a bilingual lead-in closes
this module and the integration module inserts the table immediately
after it. Section 4.1.1, Eqs. 4.8-4.12 and Fig. 4.2 belong to module B.
The integration module owns the page shell, sources and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, p, note, eq, fig
import mcmillanfig04_a as F


def body_vi():
    b = []
    b.append(h2("4 — Tính toán tốc độ phát thải và phạm vi khu vực nguy hiểm",
                "4 — Calculation of release rates and the extents of hazardous areas"))
    b.append(p("Từ giả định đến phạm vi: cách tiếp cận toán học cho phát thải ngoài trời"))
    b.append(p("Phương pháp xác định tốc độ phát thải và phạm vi của các vùng khí quyển nổ "
               "(khu vực nguy hiểm) do một hoặc nhiều điểm rò tạo ra từ lâu đã là đề tài "
               "tranh luận và được xem là một lĩnh vực khó của công nghệ. Có nhiều trường "
               "phái tư tưởng, vì vậy không thể chọn được một phương pháp được mọi bên "
               "liên quan tín nhiệm. Hệ quả là không có phương pháp nào được thỏa thuận "
               "ở cấp quốc gia hay quốc tế, và những người làm công tác này phải tự chọn "
               "một quy trình phù hợp trong số các quy phạm ngành và các quy phạm chuyên "
               "ngành khác nhau. Đã có nhiều nỗ lực đưa cơ sở tính toán vào các quy phạm "
               "quốc gia và quốc tế, nhưng bất đồng về độ chính xác gần như luôn dẫn đến "
               "thất bại trong việc đưa chúng vào. Dù vậy, những người phân loại khu vực "
               "nguy hiểm luôn phải dùng một hình thức ước lượng hoặc tính toán nào đó để "
               "biện minh cho các khu vực họ chỉ định trong từng trường hợp cụ thể; và cần "
               "nhớ rằng, miễn là kết quả tương tự như những gì đã ghi nhận trong đánh giá "
               "chủ quan — vốn trước đây là khả năng duy nhất — thì việc dùng một dạng tính "
               "toán hạn chế như mô tả trong chương này là có thể chấp nhận được."))
    b.append(p("Như sẽ thấy, chương này không quan tâm đến độ chính xác tuyệt đối mà chỉ "
               "đến một phép đo lường ước lượng; mọi giả định đưa ra đều nhằm tạo ra các "
               "ước tính cao hơn, chứ không phải thấp hơn. Khó khăn gặp phải trong mọi "
               "phương pháp phân loại khu vực là thiếu thông tin thực nghiệm về sự trộn "
               "của phát thải với không khí khi các phát thải đó là tai nạn thay vì có chủ "
               "đích. Điều này gây vấn đề cả cho cách tiếp cận chủ quan lẫn cho việc chứng "
               "minh phương pháp toán học là hoàn toàn hợp lệ."))
    b.append(p("Phần lớn toán học đã tồn tại từ trước đến nay dựa trên tính toán dòng chảy "
               "chất lỏng từ các lỗ tiết được thiết kế đặc biệt để bảo đảm lưu lượng lớn "
               "nhất với nỗ lực nhỏ nhất — chẳng hạn các tình huống mà dòng chảy hay sự "
               "trộn được yêu cầu vì lý do vận hành, chứ không phải do rò rỉ không mong "
               "muốn. Nỗ lực nghiêm túc cuối cùng nhằm đưa ra cách tiếp cận toán học diễn "
               "ra trong quá trình xây dựng BS 5345 phần 2 (1975–82); dù một bộ công thức "
               "tương đối toàn diện dựa trên lý thuyết cổ điển và thực nghiệm đã được đề "
               "xuất, những người tham gia không cảm thấy có thể giới thiệu cách tiếp cận "
               "này trong một tài liệu quốc gia, chủ yếu vì khả năng bị lạm dụng bởi những "
               "người không đủ chuyên môn hoặc việc họ không nhận ra các giới hạn của "
               "công thức. Tuy nhiên, cách tiếp cận này đã được dùng trong ít nhất một "
               "quy phạm của công ty và, nhìn chung, cho kết quả ở mức độ tin cậy hợp lý, "
               "về sau không có dấu hiệu nào cho thấy nó không đầy đủ."))
    b.append(p("Bộ quy phạm quốc tế mới nhất, BS/EN 60079-10, dự kiến thay thế BS 5345 phần 2 "
               "trong tương lai gần, cũng như các phiên bản trước đó, đã không giải quyết "
               "hiệu quả việc xác định phạm vi khu vực nguy hiểm ngoài trời bằng toán học, "
               "dù nó chứa một quan hệ toán học cơ bản. Tuy nhiên, cách tiếp cận chủ quan "
               "của bộ quy phạm này đưa ra một số thước đo để đối chiếu các lời giải toán "
               "học; và vì bộ quy phạm này được hầu hết các quốc gia phát triển trên thế "
               "giới tín nhiệm, nó có thể dùng để hỗ trợ các cách tiếp cận toán học trong "
               "chương này. Điều đó hữu ích vì, bất chấp khó khăn trong việc đưa ra cách "
               "tiếp cận làm hài lòng mọi người, công tác phân loại khu vực vẫn phải được "
               "tiến hành."))
    b.append(p("Vì các lý do trên, các cách tiếp cận toán học mô tả trong chương này được "
               "đưa vào cuốn sách. Việc sử dụng các quan hệ toán học này phải hết sức thận "
               "trọng và chỉ bởi những người đủ chuyên môn để nhận ra các giới hạn của "
               "chúng. Không có bằng chứng nào cho thấy các phép tính được mô tả, khi dùng "
               "có chuyên môn, làm gì khác hơn là xác định các khu vực nguy hiểm ít nhất lớn "
               "như mức cần thiết. Điều đó là vì chúng phần lớn dựa trên các phát thải lý "
               "tưởng từ đầu phun, thay vì các điểm rò tai nạn xảy ra do hỏng các bộ phận "
               "chứa giữ như đầu nối cáp và gioăng, hoặc, trong trường hợp các tài liệu IEC "
               "mới, vì nhiều hệ số an toàn đã được đưa vào. Cơ sở của cách tiếp cận toán "
               "học này đến từ các nguồn như Perry và công trình của Sutton và Katau, dựa "
               "trên sự kết hợp giữa động lực chất lỏng, thuyết động học của chất khí và "
               "các phép đo thực tế. Hầu hết các công thức sau đó được báo cáo trong Tài "
               "liệu nháp 79/27013 của Viện Tiêu chuẩn Anh năm 1979 và tạo thành đề xuất "
               "về một cách tiếp cận tính toán đã không được chấp nhận như đã trình bày "
               "ở trên."))

    b.append(h3("4.1 Phát thải khí và hơi", "4.1 Releases of gas and vapour"))
    b.append(p("Sự phát thải khí hoặc hơi từ một lỗ tiết hay đầu phun được cho bởi phương "
               "trình sau đây, được chấp nhận rộng rãi:"))
    b.append(eq("G = C<sub>d</sub> a P [(δ M/(R T)) "
                "(2/(δ+1))<sup>(δ+1)/(δ−1)</sup>]<sup>0.5</sup> kg/s"))
    b.append(p("trong đó G = lượng phát thải theo khối lượng, kg/s; a = diện tích mặt cắt "
               "ngang của điểm rò, m²; P = áp suất thượng lưu, N/m²; C<sub>d</sub> = hệ số "
               "lưu lượng; δ = tỷ số nhiệt dung riêng C<sub>p</sub>/C<sub>v</sub>; M = khối "
               "lượng phân tử; R = hằng số khí (8312 m·kg/(kg-mol·K)); T = nhiệt độ tuyệt "
               "đối của chất phát thải, K."))
    b.append(p("Tỷ số nhiệt dung riêng (nhiệt dung riêng ở áp suất không đổi chia cho nhiệt "
               "dung riêng ở thể tích không đổi) có giá trị khoảng 1,4 hoặc thấp hơn đối với "
               "đại đa số khí và hơi dễ cháy, như Bảng 4.1 cho thấy. Nếu thay giá trị 1,4 vào "
               "δ thì phương trình lượng phát thải được đơn giản hóa. Thêm vào đó, hệ số "
               "lưu lượng C<sub>d</sub> có giá trị lớn nhất khoảng 0,8 trong điều kiện lý "
               "tưởng, cho phép đơn giản hóa hơn nữa, và phương trình cuối cùng trở thành:"))
    b.append(eq("G = 0.006 a P (M/T)<sup>0.5</sup> kg/s", "4.1"))
    b.append(p("Tuy nhiên, phương trình này chỉ đúng nếu áp suất thượng lưu lớn hơn một bội "
               "số xác định của áp suất hạ lưu (trong trường hợp của chúng ta là áp suất "
               "khí quyển); bội số đó gọi là tỷ số áp suất tới hạn, được cho bởi phương "
               "trình sau:"))
    b.append(eq("P/P<sub>a</sub> = [(δ + 1)/2]<sup>δ/(δ−1)</sup>", "4.2"))
    b.append(p("Với giá trị 1,4 cho δ, tỷ số tới hạn là 1,9 và, làm tròn lên, có thể coi "
               "Phương trình 4.1 chỉ đúng khi áp suất tuyệt đối thượng lưu vượt quá "
               "2 × 10⁵ N/m². Khi điều đó không đúng, ảnh hưởng của áp suất khí quyển trở "
               "nên đáng kể và phương trình lượng phát thải trở thành:"))
    b.append(eq("G = C<sub>d</sub> a [2 σ (P − P<sub>a</sub>)]<sup>0.5</sup> kg/s"))
    b.append(p("trong đó σ = mật độ khí ở áp suất khí quyển và nhiệt độ phát thải. Mật độ "
               "của khí hoặc hơi có thể được biểu diễn qua khối lượng phân tử và thể tích "
               "mol (22,4 m³/kg-mol), cho một phương trình dễ nhận biết hơn như sau:"))
    b.append(eq("G = 3.95 a [M (P − 10<sup>5</sup>)/T]<sup>0.5</sup> kg/s", "4.3"))
    b.append(p("Kết quả của Phương trình 4.1 và 4.3 có thể, nếu cần, được chuyển sang thể "
               "tích phát thải bằng phương trình sau:"))
    b.append(eq("V = V<sub>o</sub> G T/(T<sub>o</sub> M) m<sup>3</sup>/s"))
    b.append(p("trong đó V<sub>o</sub> = thể tích mol, 22,4 m³/kg-mol; T<sub>o</sub> = điểm "
               "nóng chảy của nước đá (273 K). Phương trình này rút gọn thành:"))
    b.append(eq("V = 0.082 G T/M m<sup>3</sup>/s", "4.4"))

    b.append(p("Vì một số giả định đã được đưa ra và vì điểm chuyển từ phương trình này "
               "sang phương trình khác (từ Phương trình 4.1 sang Phương trình 4.3), kết "
               "quả của hai phương trình sẽ khác nhau, nhưng chỉ khác dưới 5 % tại điểm "
               "chuyển tiếp, dẫn đến một sai biệt nhỏ về phạm vi khu vực nguy hiểm xác "
               "định được. Sự chuyển tiếp từ Phương trình 4.1 sang 4.3 diễn ra khá nhanh "
               "tại 2 × 10⁵ N/m²; và vì sai biệt nhỏ tại áp suất tới hạn, dùng một trong "
               "hai phương trình ở áp suất tương ứng với tỷ số áp suất tới hạn cho kết quả "
               "chấp nhận được về khối lượng khí phát thải, xét theo bản chất của bài toán "
               "này. Tuy nhiên, nên dùng Phương trình 4.3 cho đến và bao gồm cả áp suất "
               "2 × 10⁵ N/m²."))
    b.append(p("Việc tính toán phạm vi khu vực nguy hiểm phụ thuộc vào vận tốc không khí tại "
               "điểm rò và lượng không khí sẵn có; nếu không có đủ không khí, điểm rò sẽ "
               "liên tục làm tăng lượng khí hoặc hơi dễ cháy trong không khí tại mỗi điểm "
               "và tăng dần phạm vi khu vực nguy hiểm trong suốt thời gian rò cho đến khi "
               "đạt trạng thái cân bằng. Vì vậy, các phương pháp tính toán mô tả trong "
               "chương này (ngoại trừ những phương trình cho trong 4.4) chỉ đúng nói chung "
               "ở những khu vực thông gió rất tốt và có nhiều không khí không bị giới hạn. "
               "Điều này có xu hướng giới hạn việc áp dụng các phương trình tính phạm vi "
               "khu vực nguy hiểm ở các khu vực ngoài trời hoặc các khu vực có mức thông "
               "gió tương tự."))
    b.append(p("Nếu vận tốc phát thải của khí dễ cháy cao so với vận tốc gió hay thông gió "
               "điển hình trong các tình huống trên, chính phát thải cung cấp toàn bộ năng "
               "lượng cần thiết để trộn và đạt đến mức pha loãng yêu cầu; nhưng nếu vận tốc "
               "phát thải thấp, sự trộn sẽ do điều kiện gió địa phương quyết định. Ở châu "
               "Âu, người ta thường coi gió có vận tốc khoảng 0,5–2 m/s. Do bản chất của "
               "phát thải, diện tích mặt cắt ngang hiệu dụng của tia khí thường nhỏ hơn "
               "diện tích lỗ tiết, và vận tốc phát thải cao hơn mức tưởng tượng ban đầu; "
               "hiệu ứng này đã được tính đến khi suy ra Phương trình 4.1 và 4.3."))
    b.append(p("Một vấn đề khác là khí hoặc hơi giãn nở ngay sau khi rời khỏi lỗ rò. Có thể "
               "coi rằng tại áp suất thượng lưu bằng hoặc cao hơn áp suất tới hạn, vận tốc "
               "phát thải chứng minh được là ít nhất bằng vận tốc âm thanh của chính khí "
               "hoặc hơi đó trong điều kiện hiện tại. Chất phát thải giãn gần như tức thời "
               "và rời lỗ với vận tốc xấp xỉ vận tốc âm thanh, được cho bởi phương trình "
               "sau:"))
    b.append(eq("v<sub>s</sub> = [δ R T/M]<sup>0.5</sup> m/s"))
    b.append(eq("v<sub>s</sub> = 108 (T/M)<sup>0.5</sup> m/s", "4.5"))
    b.append(p("Quãng đường tia khí hoặc hơi đi được trước khi trộn với không khí làm hỗn "
               "hợp giảm xuống dưới giới hạn nổ dưới (LEL), trong trường hợp tia ở vận tốc "
               "âm thanh, được cho bởi phương trình sau:"))
    b.append(eq("X = [2 × 10<sup>4</sup> d/(E M)] × "
                "[σ<sub>v</sub>/σ<sub>a</sub>]<sup>0.5</sup> m"))
    b.append(p("trong đó E = giới hạn nổ dưới (LEL), tính theo phần trăm thể tích; "
               "σ<sub>v</sub> = mật độ khí hoặc hơi ở áp suất và nhiệt độ môi trường, "
               "kg/m³; σ<sub>a</sub> = mật độ không khí ở áp suất và nhiệt độ môi trường, "
               "kg/m³; d = đường kính lỗ tiết đã hiệu chỉnh cho sự sụt áp xuống môi trường "
               "tại điểm phát thải. Với giả thiết vận tốc âm thanh như đã thảo luận, "
               "đường kính lỗ hiệu chỉnh được cho bởi:"))
    b.append(eq("d = [4G/(π σ<sub>v</sub> v<sub>s</sub>)]<sup>0.5</sup> m"))
    b.append(p("Thay v<sub>s</sub> từ Phương trình 4.5 và dùng 1,2 kg/m³ làm mật độ không "
               "khí ở áp suất và nhiệt độ môi trường, quãng đường tới LEL được biểu diễn "
               "như sau:"))
    b.append(eq("X = 2.1 × 10<sup>3</sup> [G/(E<sup>2</sup> M<sup>1.5</sup> T<sup>0.5</sup>)]<sup>0.5</sup> m", "4.6"))
    b.append(p("Phương trình trên vẫn đúng miễn là vận tốc tia tại thời điểm phát thải đủ "
               "cao so với vận tốc gió điển hình đã nêu (0,5–2 m/s). Khi không đúng, dòng "
               "khí hay hơi không còn là yếu tố chi phối và sự phân tán trở nên phụ thuộc "
               "ngày càng nhiều vào điều kiện khí quyển tại điểm rò. Trong trường hợp cực "
               "đoan, phát thải gần như không có vận tốc riêng, việc tính phân tán khó "
               "khăn hơn và phạm vi khu vực nguy hiểm được suy ra từ công thức thực nghiệm "
               "sau, được đưa ra bằng thí nghiệm:"))
    b.append(eq("X = 10.8 [G T/(M E)]<sup>0.55</sup> m", "4.7"))
    b.append(p("Phương trình này chỉ dùng được khi áp suất thượng lưu sao cho vận tốc phát "
               "thải không cao hơn đáng kể so với vận tốc gió (chẳng hạn hơn 20 lần) và chỉ "
               "đúng khi áp suất đó thấp hơn đáng kể áp suất tới hạn; nếu không, phạm vi "
               "khu vực nguy hiểm tạo ra sẽ quá lớn. Điểm chuyển tiếp không phải là một "
               "điểm xác định mà diễn ra dần dần, và khó xác định vì thay đổi theo từng "
               "loại khí. Hình 4.1 cung cấp một đường cong chuyển tiếp được làm mượt giữa "
               "Phương trình 4.6 và 4.7, cho một lời giải dùng được."))
    b.append(fig(1, F.fig_f401()))
    b.append(note("<b>Lưu ý về chú thích Hình 4.1.</b> Văn bản in trên trang 102 đảo ngược "
                  "đường cong 2 và 3 (gán đường 2 cho khối lượng phân tử 10 và đường 3 cho "
                  "khối lượng phân tử 1). Chú thích in ngay trong hình là chuẩn xác và đã "
                  "được dùng khi vẽ lại hình này: đường 1 là phân tán do gió ở mọi áp suất, "
                  "đường 2 = khối lượng phân tử 1, đường 3 = khối lượng phân tử 10, đường 4 "
                  "= khối lượng phân tử 100."))
    b.append(p("Cách dùng hình như sau: tính lượng phát thải theo khối lượng tại áp suất "
               "tới hạn, dùng kết quả đó để tính phạm vi khu vực nguy hiểm theo Phương "
               "trình 4.7, rồi nhân kết quả với hệ số lấy từ Hình 4.1 cho áp suất thực tế "
               "và chất khí hoặc hơi đang xét. Nên dùng Phương trình 4.3 để tính lượng phát "
               "thải (dù không bắt buộc), vì các giả định khi suy ra công thức cho giá trị "
               "khối lượng cao hơn một chút. Đường 1 cho tỷ số giữa phạm vi ở một áp suất "
               "bất kỳ đến 10⁷ N/m² và phạm vi tại áp suất tới hạn khi phân tán do gió; các "
               "đường 2, 3, 4 cho tỷ số tương tự khi phân tán bằng chính năng lượng của tia, "
               "với khối lượng phân tử lần lượt 1, 10 và 100. Các đường này dùng Phương "
               "trình 4.1 và 4.6 ở trên áp suất tới hạn, còn dưới áp suất đó là ước tính "
               "của hiệu ứng hỗn hợp giữa phân tán nội năng và phân tán do gió; kết quả "
               "thường là đánh giá cao hơn, nhất là với chất có khối lượng phân tử lớn."))
    b.append(p("Bảng 4.1 sau đây là bảng vật liệu dễ cháy gồm mười trang, trích từ BS 5345 "
               "phần 1 (1989), với các dữ liệu cần thiết cho các phép tính trên."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("4 — Calculation of release rates and the extents of hazardous areas",
                "4 — Calculation of release rates and the extents of hazardous areas"))
    b.append(p("From assumptions to extents: the mathematical approach to outdoor releases"))
    b.append(p("Methods for determining release rates and the extents of areas of explosive "
               "atmosphere (hazardous areas) created by any given leak or leaks have long "
               "been the subject of discussion and are recognised as a difficult area of "
               "technology. There are several schools of thought and, as a result, it has "
               "proved impossible to settle upon a method which has the full confidence of "
               "all relevant interests. This has resulted in the lack of any nationally or "
               "internationally agreed method, so those involved are left to select a "
               "procedure acceptable to them from a variety of industry-based and other "
               "sectorial codes. Several attempts have been made to include bases for "
               "calculative procedures in national and international codes, but "
               "disagreements as to their accuracy have almost always resulted in a "
               "failure to agree on their inclusion. Nonetheless, those involved in the "
               "classification of hazardous areas have always had to use some form of "
               "estimation or calculation to justify the hazardous areas which they "
               "specify in each particular case; and it must be remembered that, provided "
               "the methods used produce results similar to those recorded in subjective "
               "assessment — which in the past was the only possibility — the use of a "
               "limited form of calculation as described in this chapter may be justified."))
    b.append(p("As will be seen, this chapter is not concerned with absolute accuracy but "
               "merely with a gauging operation, and the assumptions made are all aimed at "
               "giving overestimates rather than underestimates. The problem experienced "
               "in any method of area classification is the lack of information from "
               "experimentation on the mixing of releases with air when such releases are "
               "accidental rather than deliberate. This causes problems both in the "
               "subjective approach to area classification and in proving that the "
               "mathematical approach is totally valid."))
    b.append(p("Most of the mathematics which has existed for some time is based upon "
               "calculation of fluid flow from orifices specially designed to ensure the "
               "maximum flow for minimum effort — situations where flow or mixing is "
               "required for operational reasons rather than as a result of an unwanted "
               "leak. The last serious attempt to produce a mathematical approach was "
               "during the production of BS 5345 Part 2 (1975–82) and, although a "
               "relatively comprehensive set of formulae based upon classical theory and "
               "experimentation was proposed, those involved did not feel able to "
               "recommend the approach in a national document, principally because of the "
               "possibility of misuse by those not sufficiently expert or failure of such "
               "people to identify the limitations of such formulae. The approach was, "
               "however, used in at least one company code and, in general, gave results "
               "with a reasonable level of confidence which have since given no indication "
               "of inadequacy."))
    b.append(p("The latest international code, BS/EN 60079-10, which is expected to replace "
               "BS 5345 Part 2 in the relatively near future, has, in common with all its "
               "predecessors, failed to effectively approach the determination of outdoor "
               "hazardous area extents by mathematical means, although it does contain a "
               "basic mathematical relationship. Its subjective approach does, however, "
               "give some yardsticks against which mathematically produced solutions can "
               "be measured; and as this code has the confidence of most of the world's "
               "developed countries, it can serve to support the mathematical approaches "
               "included in this chapter. This is helpful because, notwithstanding the "
               "difficulty in producing an approach which will satisfy everyone, there "
               "remains the necessity to carry out the business of area classification."))
    b.append(p("For the above reasons the mathematical approaches described in this chapter "
               "are included in this book. The use of these mathematical relationships "
               "must, however, be carefully approached and only by those sufficiently "
               "expert to identify their limitations. There is no evidence that the "
               "calculations described do anything but define hazardous areas at least as "
               "large as is necessary when expertly used. This is because they are largely "
               "based on ideal releases from nozzles rather than the accidental leaks which "
               "occur due to failure of such containment elements as glands and gaskets or, "
               "in the case of those in the new IEC document, because of the many safety "
               "factors added. The basis for this mathematical approach comes from sources "
               "such as Perry and work done by Sutton and Katau based on a combination of "
               "fluid dynamics, kinetic theory of gases and practical measurements. Most "
               "of these latter formulae were reported in British Standards Institution "
               "Draft Document 79/27013 in 1979 and constituted the proposal for a "
               "calculative approach which was not adopted as earlier described."))

    b.append(h3("4.1 Releases of gas and vapour", "4.1 Releases of gas and vapour"))
    b.append(p("The release of gas or vapour from an orifice or nozzle is given by the "
               "following equation, which is widely accepted:"))
    b.append(eq("G = C<sub>d</sub> a P [(δ M/(R T)) "
                "(2/(δ+1))<sup>(δ+1)/(δ−1)</sup>]<sup>0.5</sup> kg/s"))
    b.append(p("where G = mass release, kg/s; a = cross-sectional area of the leak, m²; "
               "P = upstream pressure, N/m²; C<sub>d</sub> = coefficient of discharge; "
               "δ = ratio of specific heats C<sub>p</sub>/C<sub>v</sub>; M = molecular "
               "weight; R = gas constant (8312 m·kg/(kg-mol·K)); T = absolute temperature "
               "of the released gas, K."))
    b.append(p("The ratio of specific heats (specific heat at constant pressure divided by "
               "the specific heat at constant volume) has a value of around 1.4 or less for "
               "the vast majority of flammable gases and vapours, as shown by Table 4.1. If "
               "the value 1.4 is substituted for δ the mass release equation can be "
               "simplified. In addition, the coefficient of discharge C<sub>d</sub> has a "
               "maximum value of around 0.8 in ideal circumstances, allowing further "
               "simplification, and the final equation becomes:"))
    b.append(eq("G = 0.006 a P (M/T)<sup>0.5</sup> kg/s", "4.1"))
    b.append(p("This equation is, however, only valid if the upstream pressure is greater "
               "than a specific multiple of the downstream pressure (atmospheric pressure "
               "in our case), which multiple is called the critical pressure ratio. This "
               "ratio is given by the following equation:"))
    b.append(eq("P/P<sub>a</sub> = [(δ + 1)/2]<sup>δ/(δ−1)</sup>", "4.2"))
    b.append(p("Using the value of 1.4 for δ the critical ratio is 1.9 and so, rounding up, "
               "Equation 4.1 can be assumed to be valid only when the absolute upstream "
               "pressure exceeds 2 × 10⁵ N/m². Where this is not so the effects of "
               "atmospheric pressure become significant and the mass release equation "
               "becomes:"))
    b.append(eq("G = C<sub>d</sub> a [2 σ (P − P<sub>a</sub>)]<sup>0.5</sup> kg/s"))
    b.append(p("where σ = density of the gas at atmospheric pressure and release "
               "temperature. The density of the gas or vapour can be expressed in terms of "
               "the molecular weight and the molar volume (22.4 m³/kg-mol), giving a more "
               "recognisable equation as follows:"))
    b.append(eq("G = 3.95 a [M (P − 10<sup>5</sup>)/T]<sup>0.5</sup> kg/s", "4.3"))
    b.append(p("The results of Equations 4.1 and 4.3 can, if required, be converted into "
               "volume release by use of the following equation:"))
    b.append(eq("V = V<sub>o</sub> G T/(T<sub>o</sub> M) m<sup>3</sup>/s"))
    b.append(p("where V<sub>o</sub> = molar volume, 22.4 m³/kg-mol; T<sub>o</sub> = melting "
               "point of ice (273 K). This equation simplifies to:"))
    b.append(eq("V = 0.082 G T/M m<sup>3</sup>/s", "4.4"))

    b.append(p("Because several assumptions have been made and because of the point of "
               "change from one equation to the other (Equation 4.1 to Equation 4.3), the "
               "results of the two equations will be seen to vary, but only by less than "
               "5 per cent at the point of changeover, resulting in a small variation in "
               "the actual hazardous area defined. The changeover from Equation 4.1 to "
               "Equation 4.3 is quite rapid at 2 × 10⁵ N/m² and, because of the small "
               "variation produced at critical pressure, utilizing either equation at the "
               "pressure related to the critical pressure ratio produces an acceptable "
               "result for mass of gas released in view of the type of exercise in which we "
               "are involved. It is, however, recommended that Equation 4.3 is used up to "
               "and including pressures of 2 × 10⁵ N/m²."))
    b.append(p("Calculation of the extents of hazardous areas is dependent upon the "
               "velocity of air at the point of leakage and the quantity of air which is "
               "available; if sufficient air is not available, the leak will steadily "
               "increase the amount of flammable gas or vapour in air at any point and "
               "progressively increase the extent of the hazardous area throughout the "
               "period of leakage until equilibrium is reached. Therefore, the calculative "
               "methods described in this chapter (with the exception of those given in "
               "4.4) are generally only valid in areas which are very well ventilated and "
               "where a large amount of unconfined air is available. This tends to limit "
               "the application of the equations given for calculating the extent of "
               "hazardous areas to outdoor areas or other areas with similar levels of "
               "ventilation."))
    b.append(p("If the release velocity of the flammable gas is high compared to the typical "
               "wind or ventilation velocity in the circumstances described above, the "
               "release provides all the necessary energy for the mixing needed to achieve "
               "the required dilution; but if the release velocity is low, mixing will be "
               "due to the local wind conditions. In Europe these are normally considered "
               "to be of the order of 0.5–2 m/s. Because of the nature of release the "
               "effective cross-sectional area of the gas jet is normally less than the "
               "orifice cross-sectional area and the release velocity is higher than might "
               "at first be thought; this effect is, of course, taken care of in the "
               "derivation of Equations 4.1 and 4.3."))
    b.append(p("A further problem is that the gas or vapour expands as soon as it leaves "
               "the leak orifice. It can be assumed that at, and above, an upstream "
               "pressure equal to the critical pressure the release velocity can be "
               "demonstrated to be at least sonic — the velocity of sound in the gas or "
               "vapour in question in the prevailing conditions. The gas or vapour will "
               "expand almost instantly on release and will leave the release orifice at "
               "around the speed of sound, which velocity is given by the following "
               "equation:"))
    b.append(eq("v<sub>s</sub> = [δ R T/M]<sup>0.5</sup> m/s"))
    b.append(eq("v<sub>s</sub> = 108 (T/M)<sup>0.5</sup> m/s", "4.5"))
    b.append(p("The distance which the jet of gas or vapour will travel before mixing with "
               "air causes the resultant mixture to fall below the lower explosive limit "
               "(LEL) in circumstances where the jet is at sonic velocity, and is given by "
               "the following equation:"))
    b.append(eq("X = [2 × 10<sup>4</sup> d/(E M)] × "
                "[σ<sub>v</sub>/σ<sub>a</sub>]<sup>0.5</sup> m"))
    b.append(p("where E = lower explosive limit (LEL), in volume per cent; σ<sub>v</sub> = "
               "gas or vapour density at ambient pressure and temperature, kg/m³; "
               "σ<sub>a</sub> = density of air at ambient pressure and temperature, kg/m³; "
               "d = diameter of the release orifice corrected for pressure drop to ambient "
               "at release. Assuming, as previously discussed, sonic velocity, the "
               "corrected orifice diameter is given by:"))
    b.append(eq("d = [4G/(π σ<sub>v</sub> v<sub>s</sub>)]<sup>0.5</sup> m"))
    b.append(p("Substituting for v<sub>s</sub> from Equation 4.5 and using 1.2 kg/m³ as the "
               "density of air at ambient pressure and temperature, the distance to the "
               "LEL can be expressed as:"))
    b.append(eq("X = 2.1 × 10<sup>3</sup> [G/(E<sup>2</sup> M<sup>1.5</sup> T<sup>0.5</sup>)]<sup>0.5</sup> m", "4.6"))
    b.append(p("The above equation remains valid as long as the jet velocity on release is "
               "sufficiently high in relation to the typical wind speed specified earlier "
               "(0.5–2 m/s). Where this is not so the flow of gas or vapour ceases to be "
               "the dominant factor and its dispersal becomes more and more reliant on the "
               "atmospheric conditions local to the release. In the ultimate circumstance "
               "where the release has virtually no velocity of its own, it becomes more "
               "difficult to calculate dispersal and the extent of the hazardous area is "
               "derived from the following empirical formula produced by experimentation:"))
    b.append(eq("X = 10.8 [G T/(M E)]<sup>0.55</sup> m", "4.7"))
    b.append(p("This equation can only be used where the upstream pressure is such that the "
               "release velocity is not considerably higher than the wind velocity (say "
               "more than 20 times) and will not be valid unless that pressure is "
               "significantly less than the critical pressure, or the extent of hazardous "
               "area produced will be excessively large. The changeover will not be at a "
               "specific point but will be progressive, and is difficult to determine as "
               "it varies from gas to gas. Fig. 4.1 provides a smoothed changeover between "
               "Equations 4.6 and 4.7, giving an acceptable usable solution."))
    b.append(fig(1, F.fig_f401()))
    b.append(note("<b>Note on the Fig. 4.1 legend.</b> The printed prose on p.102 swaps "
                  "curves 2 and 3 (assigning molecular weight 10 to curve 2 and molecular "
                  "weight 1 to curve 3). The legend printed inside the figure is "
                  "authoritative and has been followed in the redraw: curve 1 gives wind "
                  "dispersion at all pressures, curve 2 = molecular weight 1, curve 3 = "
                  "molecular weight 10, curve 4 = molecular weight 100."))
    b.append(p("The figure is used as follows: calculate the mass release at the critical "
               "pressure, use the result to calculate the extent of the hazardous area with "
               "Equation 4.7, then multiply that result by the factor read from Fig. 4.1 "
               "for the actual pressure and the gas or vapour in question. It is considered "
               "best, although not essential, to use Equation 4.3 for the mass release, "
               "because its assumptions give a slightly higher value. Curve 1 gives the "
               "ratio of the extent at any pressure up to 10⁷ N/m² to that at the critical "
               "pressure where dispersion is by wind, while curves 2, 3 and 4 give the "
               "corresponding ratio where dispersion is by the energy of the jet alone, "
               "for molecular weights 1, 10 and 100 respectively. These curves use "
               "Equations 4.1 and 4.6 above the critical pressure; below it they estimate "
               "the mixed effect of partial internal-energy dispersion and partial wind "
               "dispersion, and will generally overestimate, particularly for gases and "
               "vapours with high molecular weights."))
    b.append(p("Table 4.1, the ten-page flammable-materials table from BS 5345 Part 1 "
               "(1989), follows and supplies the data required for the calculations above."))
    return "".join(b)
