# -*- coding: utf-8 -*-
"""Book 5, Chapter 14 — Application of the Inherent Safety Index for
Computerized Process Synthesis (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 103–117.  The chapter covers
classical process synthesis (Figure 10, Hurme & Järveläinen 1995; Figure 11,
Heikkilä et al. 1996), synthesis by optimization (MINLP vs GA, Figure 12),
the genetic method with the ISI as fitness (14.4) and two case studies —
butene separation (Table 30, Equation 11, Figure 13) and emulsion
polymerization (Table 31, Figure 14).
"""

from isd_common import eq, fig, h2, h3, note, ol, p, table
import isdfig as F

PAGES_SRC = 15           # source pages 103–117
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "The ISI in Computerized Process Synthesis"
TITLE_VI = "Ứng dụng chỉ số an toàn nội tại trong tổng hợp quá trình trên máy tính"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 14.</b> tổng hợp quá trình (process "
                "synthesis) · luật cơ sở (rule base) · MINLP — lập trình phi "
                "tuyến số nguyên hỗn hợp · giải thuật di truyền (GA) · quần "
                "thể / lai ghép (crossover) / đột biến (mutation) · hàm thích "
                "nghi (fitness function) — chính là chỉ số an toàn nội tại · "
                "tải hơi cột (vapor load) · chưng cất trích ly (extractive "
                "distillation) · trùng hợp nhũ (emulsion polymerization) · "
                "bán liên tục (semibatch) · đĩa nổ (rupture disk) · bể dập "
                "(quench tank).")
    return ("<b>Key terms.</b> process synthesis · rule base · MINLP — mixed "
            "integer nonlinear programming · genetic algorithm (GA) · "
            "population / crossover / mutation · fitness function — here the "
            "Inherent Safety Index itself · column vapor load · extractive "
            "distillation · emulsion polymerization · semibatch · rupture "
            "disk · quench tank.")


_D = '<span style="color:#bbb">—</span>'

# Source Table 30 (p. 110): feed compositions and relative volatilities.
_T30 = [
    ("propane", "1.47", _D, _D, _D),
    ("1-butene", "14.75", "2.45", "2.0", "2.35"),
    ("n-butane", "50.29", "1.18", "1.17", "1.25"),
    ("2-butenes", "27.58", "1.03", "1.70", "1.35"),
    ("n-pentane", "5.90", "2.50", "2.1", "3.0"),
]

# Source Table 31 (p. 114): main phases and systems of an emulsion
# polymerization process (Kroschwitz, 1986).  Asterisk = considered.
_STAR = '<span style="color:#1f5f8b">*</span>'
_T31 = [
    "1. Dỡ nguyên liệu · Raw material unloading",
    "2. Lưu trữ nguyên liệu · Raw material storage",
    "3. Hệ cấp và tiền xử lý%s · Feed and pretreatment systems%s" % (_STAR, _STAR),
    "4. Lò phản ứng trùng hợp%s · Polymerization reactor%s" % (_STAR, _STAR),
    "5. Hệ truyền nhiệt lò phản ứng%s · Reactor heat transfer system%s" % (_STAR, _STAR),
    "6. Hệ an toàn lò phản ứng%s · Reactor safety systems%s" % (_STAR, _STAR),
    "7. Hoàn thiện · Finishing operations",
    "8. Thu hồi monome · Monomer recovery",
    "9. Xử lý xả%s · Vent treatment%s" % (_STAR, _STAR),
    "10. Lưu trữ và xử lý latex · Latex storage and handling",
]

_T31_EN = [
    "1. Raw material unloading",
    "2. Raw material storage",
    "3. Feed and pretreatment systems*",
    "4. Polymerization reactor*",
    "5. Reactor heat transfer system*",
    "6. Reactor safety systems*",
    "7. Finishing operations",
    "8. Monomer recovery",
    "9. Vent treatment*",
    "10. Latex storage and handling",
]


def body_vi():
    b = []

    b.append(h2("14. Ứng dụng chỉ số an toàn nội tại trong tổng hợp quá trình "
                "trên máy tính",
                "14. Application of Inherent Safety Index for Computerized "
                "Process Synthesis"))

    b.append(p("Theo quan điểm cổ điển, tổng hợp quá trình hóa học chỉ dựa trên "
               "các khía cạnh kinh tế và kỹ thuật. Tuy nhiên, nhu cầu đánh giá "
               "an toàn của quá trình ở giai đoạn đầu thiết kế ngày càng tăng, "
               "do quy định của chính phủ và cả lý do kỹ thuật thực tiễn. "
               "<b>Ảnh hưởng đến cấu hình quá trình và an toàn nội tại dễ dàng "
               "hơn nhiều ở giai đoạn thiết kế khái niệm</b> so với các giai "
               "đoạn sau. Vì vậy các khía cạnh an toàn nên được đưa vào tổng "
               "hợp quá trình trên máy tính. ISI đã trình bày có thể được dùng "
               "như một công cụ để đánh giá các phương án được tổng hợp, hoặc "
               "như một <b>hàm mục tiêu</b> trong tổng hợp. Các phương pháp "
               "đánh giá an toàn hiện có (ví dụ Dow F&amp;E Index, Hazop trên "
               "máy tính) phần lớn dành cho các giai đoạn kỹ thuật chi tiết "
               "hơn hoặc cho nhà máy hiện hữu, không áp dụng trực tiếp được "
               "trọn vẹn ở giai đoạn khái niệm vì chúng đòi hỏi thông tin chi "
               "tiết về thiết bị; các phương pháp khác như danh sách kiểm "
               "tra không dễ chuyển thành dạng hàm để tích hợp vào công cụ "
               "thiết kế khác."))
    b.append(p("Tổng hợp quá trình là nhiệm vụ xây dựng cấu hình quá trình cho "
               "một mục đích bằng cách xác định các thao tác/thiết bị được dùng "
               "và cách chúng được nối với nhau. Có hai cách tiếp cận cơ bản: "
               "1) tổng hợp – phân tích – đánh giá cổ điển, và 2) tối ưu hóa "
               "cấu trúc quá trình bằng một hàm mục tiêu phù hợp."))

    # ---- 14.1 ----------------------------------------------------------------
    b.append(h3("14.1 Tổng hợp quá trình cổ điển",
                "14.1 Classical Process Synthesis"))

    b.append(p("Tổng hợp quá trình cổ điển gồm tổng hợp các phương án, phân "
               "tích và đánh giá cuối cùng. Hurme và Järveläinen (1995) đã "
               "trình bày một hệ thống kết hợp tổng hợp và mô phỏng quá trình "
               "gồm một hệ luật tương tác dùng để sinh các phương án quá trình "
               "(Hình 10); các phương án được mô phỏng, tính chi phí và đánh "
               "giá qua phân tích lợi nhuận. Concept hệ thống kết hợp tổng hợp "
               "quá trình, mô phỏng và tính chi phí với ước tính bất định."))
    b.append(fig(1, F.fig_c14_synthesis()))
    b.append(p("Heikkilä và cộng sự (1996) đã mở rộng công trình của Hurme và "
               "Järveläinen (1995) với các khía cạnh môi trường và an toàn "
               "(Hình 11). Các phương án được mô phỏng để xác định cân bằng "
               "vật chất và nhiệt, ước tính tính chất vật lý; sau đó được đánh "
               "giá kinh tế bằng tỷ suất hoàn vốn nội bộ. Tác động môi trường "
               "được ước tính bằng lượng tương đương chất ô nhiễm có xét mức "
               "hại của từng chất thải; rủi ro môi trường cũng gồm các khía "
               "cạnh sức khỏe nghề nghiệp để chọn quá trình <b>lành mạnh hơn "
               "ngay từ bản chất</b>. An toàn nội tại được ước tính bằng chỉ "
               "số an toàn nội tại như trình bày sau đây."))
    b.append(fig(2, F.fig_c14_combined()))
    b.append(p("Quyết định cuối cùng về phương án tốt nhất không phải là lựa "
               "chọn đơn giản, vì ba tham số — hiệu quả chi phí, khía cạnh "
               "môi trường và an toàn nội tại — <b>không thể gộp vào một con "
               "số duy nhất một cách duy nhất</b>: nhà thiết kế có thể đề cao "
               "các tham số khác nhau tùy chính sách công ty và mục tiêu bài "
               "toán. Vì vậy các phương án phải được so sánh dựa trên tất cả "
               "các tiêu chí, ví dụ bằng phương pháp biểu đồ quyết định "
               "(Kepner và Tregoe, 1981) hoặc ma trận so sánh từng cặp của "
               "Saaty (1977)."))
    b.append(p("Các khía cạnh an toàn được xét trong hai pha (Hình 11). Trong "
               "tổng hợp dựa trên luật, một số luật liên quan an toàn được áp "
               "dụng khi chọn khái niệm quá trình — ví dụ \"tách trước các "
               "cấu tử ăn mòn hoặc nguy hiểm\" hay \"tránh dùng các chất không "
               "tương thích hóa học trong cùng một quá trình\". Mọi vấn đề liên "
               "quan an toàn — như lựa chọn nguyên liệu — không được xét trong "
               "pha tổng hợp mà do người dùng đưa vào; việc sinh các luật tổng "
               "hợp phổ quát xét an toàn cũng không dễ. Vì vậy việc phân tích "
               "các thiết kế thay thế bằng chỉ số an toàn nội tại — mô tả khả "
               "cháy, độc tính, điều kiện quá trình v.v. — là quan trọng."))
    b.append(p("Giai đoạn thiết kế khái niệm là <b>giai đoạn then chốt</b> khi "
               "thiết kế nhà máy an toàn nội tại hơn, vì các khái niệm quá "
               "trình thay thế được tạo và phân tích ở giai đoạn này. Điều này "
               "nhấn mạnh nhu cầu đưa công cụ đánh giá an toàn vào thiết kế "
               "sơ bộ: tiết kiệm thời gian và tiền bạc khi cần ít sửa đổi an "
               "toàn đắt giá trong các giai đoạn sau. Công cụ đánh giá an toàn "
               "cần được tích hợp chặt vào môi trường thiết kế sơ bộ hiện có "
               "để sẵn sàng trong thiết kế; các công cụ này cũng hưởng lợi từ "
               "các ngân hàng dữ liệu và chương trình mô phỏng hiện có cho các "
               "tính toán tính chất vật lý và điều kiện pha. ISI cho phép đánh "
               "giá an toàn nội tại của các phương án quá trình trong môi "
               "trường tổng hợp trên máy tính; cách tiếp cận cho phép so sánh "
               "an toàn nội tại linh hoạt và tương tác ở giai đoạn thiết kế "
               "khái niệm."))

    # ---- 14.2 ----------------------------------------------------------------
    b.append(h3("14.2 Tổng hợp quá trình bằng tối ưu hóa",
                "14.2 Process Synthesis by Optimization"))

    b.append(p("Tổng hợp quá trình có thể được xem như một bài toán tối ưu hóa. "
               "Vấn đề là <b>mô hình cần tối ưu hóa thay đổi cùng lúc với cấu "
               "hình quá trình</b>. Vì vậy các cách tối ưu hóa khả thi là "
               "MINLP (mixed integer nonlinear programming) và giải thuật di "
               "truyền. MINLP đã được dùng trong nhiều công trình (ví dụ "
               "Grossmann và Kravanja, 1995): phương pháp nghiêm ngặt nhưng "
               "đòi hỏi thuật toán toán học chuyên dụng, một số vẫn đang được "
               "phát triển. Trong tối ưu di truyền, lời giải được tìm theo "
               "kiểu tiến hóa — khá quen thuộc với kỹ sư thực hành; vấn đề là "
               "yêu cầu mã hóa bài toán thành gen và độ chậm của thuật toán "
               "(nhiều trường hợp không cần thiết được tính do đột biến và lai "
               "ghép), và phương pháp không bảo đảm đạt lời giải tối ưu. GA đã "
               "được dùng cho tổng hợp quá trình tách (Hurme, 1996)."))

    b.append(h3("14.3 Tối ưu hóa di truyền", "14.3 Genetic Optimization"))

    b.append(p("Giải thuật di truyền (GA) là mô hình tính toán của tiến hóa tự "
               "nhiên, dùng các phép toán liên quan di truyền để dẫn dắt quá "
               "trình tối ưu hóa trong không gian tìm kiếm phức tạp. GA làm "
               "việc với các tập cá thể — khi được mã hóa đúng, đại diện cho "
               "các lời giải tiềm năng. Quần thể được xử lý lặp, bắt đầu từ "
               "quần thể ngẫu nhiên, qua các pha <b>đánh giá, lựa chọn, ghép "
               "cặp, lai ghép và đột biến</b> (Hình 12). Lựa chọn dựa trên đánh "
               "giá các cá thể của quần thể bằng một <b>hàm thích nghi</b>. "
               "Chu trình lặp tới điều kiện dừng (ví dụ dung sai sai số). Đặc "
               "tính của GA: các cá thể có đặc điểm chung và độ thích nghi cao "
               "sẽ tăng trưởng theo cấp số nhân. Dù hội tụ không phải luôn được "
               "bảo đảm, GA đã thành công với nhiều bài toán tối ưu khó; GA "
               "không đặt yêu cầu đặc biệt vào bài toán (như tính liên tục), "
               "ngoài việc mã hóa cá thể hợp lý và tồn tại hàm mục tiêu phù hợp "
               "để đánh giá độ thích nghi của từng cá thể. Lựa chọn đúng hàm "
               "thích nghi là quan trọng vì nó dẫn dắt lựa chọn và tối ưu "
               "(Goldberg, 1989)."))
    b.append(fig(3, F.fig_c14_ga()))
    b.append(p("Hurme (1996) đã dùng GA giải bài toán tổng hợp tách hỗn hợp "
               "hydrocarbon, và so sánh GA với phiên bản ngẫu nhiên thuần túy "
               "trong đó lai ghép và đột biến được thay bằng sinh ngẫu nhiên "
               "lời giải mới: không có khác biệt trong các thế hệ đầu nhưng "
               "trở nên rõ rệt sau một số thế hệ — GA đạt lời giải sau mười "
               "thế hệ với khoảng 1100 lời giải khác nhau có thể, trong khi "
               "phiên bản ngẫu nhiên cần hàng chục thế hệ. GA vừa nhanh hơn tối "
               "ưu ngẫu nhiên, vừa không quá nặng về tính toán."))
    b.append(p("Hurme và Heikkilä (1998) đã mở rộng cách tiếp cận GA của Hurme "
               "(1996) với <b>hàm an toàn</b>. Vì mô hình không liên tục, các "
               "phương pháp tối ưu thông thường không dùng được, nên giải thuật "
               "di truyền được sử dụng: cấu trúc quá trình được biểu diễn dưới "
               "dạng chuỗi số nguyên mô tả các thao tác cần thiết và cách chúng "
               "được nối với nhau; <b>chỉ số an toàn nội tại được dùng làm hàm "
               "mục tiêu (độ thích nghi)</b>. Chỉ số được phát triển cho đánh "
               "giá an toàn ở giai đoạn đầu thiết kế; hầu hết các chỉ số thành "
               "phần khá đơn giản để ước tính, trừ chỉ số cấu trúc quá trình "
               "an toàn — được ước tính bằng suy luận dựa trên tình huống với "
               "cơ sở dữ liệu các thiết kế tốt và xấu. Chỉ số này cũng có thể "
               "được dùng làm hàm mục tiêu nếu an toàn nội tại của quá trình "
               "cần được tối đa hóa một cách hệ thống."))

    # ---- 14.4 ----------------------------------------------------------------
    b.append(h3("14.4 Nguyên lý của phương pháp", "14.4 Principle of the Method"))

    b.append(p("Trong cách tiếp cận của Hurme và Heikkilä (1998), an toàn nội "
               "tại là <b>hàm mục tiêu duy nhất</b> được xét trong tổng hợp "
               "quá trình, được ước tính bằng ISI (Heikkilä và cộng sự, 1996) "
               "phát triển cho ước tính an toàn nội tại trong thiết kế khái "
               "niệm. Cấu trúc quá trình được biểu diễn dưới dạng chuỗi số "
               "nguyên (gen) đại diện cho các thao tác cần thiết, loại của "
               "chúng và cách chúng được nối; chỉ số an toàn nội tại là hàm "
               "thích nghi. Các bước cơ bản của giải thuật tối ưu di truyền:"))
    b.append(ol([
        "Sinh quần thể ban đầu gồm các trình tự tách ngẫu nhiên — các trình tự mô tả cả thiết bị được dùng lẫn cách nối.",
        "Chọn ngẫu nhiên các trình tự và sinh lời giải mới bằng lai ghép (vị trí lai ghép cũng chọn ngẫu nhiên); vì lai ghép có thể tạo trình tự bất khả thi, cần thủ tục kiểm tra và sửa lại — loại thủ tục phụ thuộc loại quá trình được tổng hợp.",
        "Đột biến các trình tự tại vị trí chọn ngẫu nhiên.",
        "Đánh giá các trình tự bằng hàm thích nghi dựa trên chỉ số an toàn nội tại.",
        "Chọn các trình tự tốt nhất và loại bỏ các trình tự xấu, thừa để kích thước quần thể giữ không đổi.",
        "Lặp lại các bước 2–6 cho tới khi mức cải thiện thấp hơn dung sai cho trước.",
    ]))

    b.append(h3("14.4.1 Nghiên cứu tình huống — quá trình tách",
                "14.4.1 Case Study; Separation Process"))

    b.append(p("Một bài toán tổng hợp về tinh chế <b>butene</b> được thảo luận "
               "(Hurme và Heikkilä, 1998): mục tiêu là tổng hợp quá trình tách "
               "bằng cách <b>tối đa hóa an toàn nội tại</b>, đo bằng ISI. Trong "
               "quá trình, hỗn hợp propane, 1-butene, n-butane, 2-butene và "
               "n-pentane được tách thành các dòng cấu tử thuần kỹ thuật; cả "
               "chưng cất thường (phương pháp 1) lẫn chưng cất trích ly "
               "(phương pháp 2 và 3) được dùng. Thành phần cấp và độ bay hơi "
               "tương đối của các cấu tử kề nhau theo các phương pháp tách cho "
               "ở Bảng 30."))
    b.append(table(("Cấu tử · Component", "mol-%", "α₁", "α₂", "α₃"), _T30,
              "Bảng 30 · Thành phần cấp và độ bay hơi tương đối trong nghiên "
              "cứu tình huống."))
    b.append(p("Các bài toán tổng hợp tách mang tính tổ hợp cao khi số cấu tử "
               "và phương pháp tách lớn: trong trường hợp đơn giản này — 5 cấu "
               "tử và 3 phương pháp — có <b>1134 lời giải khác nhau</b> "
               "(Hurme, 1996); hai trong số đó cho ở Hình 13 làm ví dụ. Tải "
               "hơi cột (tốc độ dòng hơi đi lên cột) được tính để xác định cỡ "
               "thiết bị xấp xỉ; phương pháp xấp xỉ tính dòng hơi V trong cột "
               "là (Hurme, 1996):"))
    b.append(eq("V = D(R<sub>F</sub>(α − 1) + 1)", "(11)"))
    b.append(p("trong đó R<sub>F</sub> = R / R<sub>min</sub>, V là dòng hơi, D "
               "là tốc độ dòng chưng, F là tốc độ dòng cấp, α là độ bay hơi "
               "tương đối, R là tỷ lệ hoàn lưu, R<sub>min</sub> là hoàn lưu "
               "tối thiểu."))
    b.append(fig(4, F.fig_c14_separations()))
    b.append(p("Các bước của giải thuật di truyền trong bài này: 1) sinh quần "
               "thể ban đầu ngẫu nhiên — trình tự mô tả thứ tự tách các cấu tử "
               "và phương pháp tách được dùng; ví dụ trình tự bên trái Hình 13 "
               "được mô tả bằng chuỗi <b>23 12 14 11</b> — số nguyên đầu là "
               "phương pháp tách, số nguyên sau là cấu tử heavy key của phép "
               "tách trong cột; 2) lai ghép — độ dài lai ghép cố định hai cấu "
               "tử; vì lai ghép có thể tạo trình tự chứa trùng cấu tử, thủ tục "
               "kiểm tra và sửa được cài đặt (kiểm tra mọi cấu tử có trong "
               "trình tự; nếu thiếu, thay bằng cấu tử thiếu); 3) đột biến cả "
               "phương pháp tách lẫn trình tự tại vị trí ngẫu nhiên; 4) đánh "
               "giá bằng hàm thích nghi dựa trên chỉ số an toàn nội tại; 5) "
               "chọn các trình tự tốt nhất, loại xấu/thừa, giữ cỡ quần thể; "
               "6) lặp tới khi cải thiện dưới dung sai."))
    b.append(p("Cỡ quần thể ban đầu là <b>5 trình tự</b>; quần thể lai ghép 2 "
               "trình tự và quần thể đột biến 2 trình tự mỗi thế hệ — tổng số "
               "4 trình tự mới mỗi thế hệ; sau lựa chọn quần thể giữ ở 5. Hàm "
               "thích nghi dựa trên ISI đã được <b>đơn giản hóa</b>: tính chất "
               "an toàn của các chất trong quá trình chỉ khác nhau ít — phần "
               "lớn chỉ số thành phần giống nhau cho mọi cấu hình; loại thiết "
               "bị (chưng cất) giống nhau nên chỉ số an toàn thiết bị hằng số; "
               "cấu trúc quá trình cũng khá giống nhau nên chỉ số cấu trúc "
               "quá trình không được đánh giá và CBR không cần thiết. Tuy "
               "nhiên <b>số cột thay đổi khi dùng chưng cất trích ly</b>, nên "
               "tồn kho chất lỏng trở thành tham số an toàn chính; tồn kho phụ "
               "thuộc cỡ cột. Giả thiết mọi cột được thiết kế cùng vận tốc "
               "hơi bề mặt nên diện tích cột tỷ lệ thuận với dòng hơi; giữ "
               "chất lỏng tỷ lệ với diện tích cột; do đó tổng tồn kho chất "
               "lỏng của quá trình tỷ lệ thuận với tổng dòng hơi của các cột "
               "— được tính theo Phương trình 11 cho từng cột."))
    b.append(p("Giải thuật di truyền đạt lời giải thường trong <b>mười thế "
               "hệ</b> cho bài toán hơn 1100 lời giải; tối ưu ngẫu nhiên sẽ "
               "cần hàng chục thế hệ. Lời giải tốt nhất tìm được là cấu hình "
               "đầu tiên (23 12 14 11) trong Hình 13. Kết quả với hàm mục tiêu "
               "an toàn nội tại <b>hơi khác so với kết quả với hàm mục tiêu kinh tế</b> "
               "(Hurme, 1996): với hàm an toàn, chưng cất đơn giản được ưa "
               "chuộng hơn; ngoại lệ là các trường hợp chưng cất trích ly cải "
               "thiện tách rất mạnh. Lý do: chưng cất đơn giản chỉ cần một cột "
               "cho mỗi phép tách, còn trích ly cần hai cột vì phải tách cả "
               "dung môi — làm tồn kho chất lỏng lớn hơn, nhất là khi dung môi "
               "trích ly rất cháy. Kết quả hợp lý theo lẽ thường: một trong "
               "các nguyên tắc an toàn nội tại là <b>dùng thiết kế đơn giản "
               "hơn và giảm tồn kho</b> để tăng an toàn."))

    b.append(h3("14.4.2 Nghiên cứu tình huống — quá trình trùng hợp nhũ",
                "14.4.2 Case Study; Emulsion Polymerization Process"))

    b.append(p("Là nghiên cứu tình huống thứ hai, một tổng hợp quá trình "
               "<b>trùng hợp nhũ</b> được đưa ra (Hurme và Heikkilä, 1998). "
               "Trong trùng hợp nhũ, các monome không no hoặc dung dịch của "
               "chúng được phân tán trong pha liên tục với sự trợ giúp của "
               "chất nhũ hóa và được trùng hợp; sản phẩm là một phân tán polymer "
               "gọi là <b>latex</b>. Nguyên liệu là hydrocarbon không no rất "
               "cháy và phản ứng tỏa nhiệt — cả hai đều gây rủi ro. Các pha và "
               "hệ thống chính của một nhà máy trùng hợp nhũ liệt kê ở Bảng 31."))
    b.append(table(("Pha / hệ thống · Phase / system", ), _T31,
              "Bảng 31 · Các pha và hệ thống chính của quá trình trùng hợp nhũ "
              "(Kroschwitz, 1986). * được xét."))
    b.append(p("Thông tin về tính chất an toàn, tai nạn, khuyến nghị thiết kế "
               "và thiết kế hiện có của quá trình trùng hợp nhũ được thu thập "
               "từ tài liệu; chỉ các pha đánh dấu sao (*) trong Bảng 31 được "
               "xét. Khoảng <b>50 khuyến nghị thiết kế hoặc tình huống</b> về "
               "chủ đề được tìm thấy; một kho tình huống được hình thành từ "
               "thông tin này cùng một số khuyến nghị thiết kế chung; các tình "
               "huống được đánh giá dựa trên chỉ số cấu trúc quá trình an toàn, "
               "được đưa vào các tình huống trong cơ sở dữ liệu."))
    b.append(p("Các biến chính của các pha quá trình được chọn và mã hóa bằng "
               "số nguyên cho thủ tục tổng hợp — gồm loại thao tác và thiết bị "
               "được dùng và cách nối chúng. <b>14 biến chính</b> được chọn: "
               "1) tiền trộn; 2) tiền gia nhiệt; 3) loại lò phản ứng và chế độ "
               "vận hành; 4) số lò phản ứng; 5) vật liệu chế tạo lò phản ứng; "
               "6) khuấy lò phản ứng; 7) vách ngăn trong lò; 8) hệ truyền nhiệt "
               "lò phản ứng; 9) phương pháp chuyển chất lỏng; 10) vị trí hệ "
               "xả; 11) loại thiết bị xả; 12) phương pháp dừng phản ứng; 13) hệ "
               "thu hồi xả; 14) thiết bị xử lý khí xả."))
    b.append(p("Tối ưu di truyền bắt đầu với quần thể ban đầu cỡ 5 sinh ngẫu "
               "nhiên; thuật toán gồm lai ghép của hai trình tự chọn ngẫu "
               "nhiên và đột biến ngẫu nhiên trên hai trình tự (số đột biến mỗi "
               "trình tự từ bốn ở đầu xuống một ở cuối). Các bước: 1) quần thể "
               "ngẫu nhiên cỡ 5; 2) lai ghép hai trình tự ngẫu nhiên; 3) đột "
               "biến hai trình tự; 4) CBR trên chỉ số cấu trúc quá trình an "
               "toàn; 5) tính độ thích nghi bằng ISI — chỉ xét tồn kho, an toàn "
               "thiết bị, nhiệt phản ứng và cấu hình quá trình; 6) chọn trình "
               "tự tốt nhất giữ quần thể cỡ 5; 7) lặp các bước 2–7 cho tới khi "
               "cải thiện độ thích nghi dưới dung sai. Thủ tục hội tụ trong "
               "<b>dưới 20 thế hệ</b>; cấu hình tối ưu có giá trị ISI là "
               "<b>16</b> (tối ưu bắt đầu điển hình từ giá trị 28–30). Phương "
               "án an toàn nội tại nhất được tổng hợp cho ở Hình 14."))
    b.append(fig(5, F.fig_c14_polymer()))
    b.append(p("Quá trình có giá trị chỉ số an toàn nội tại thấp nhất chứa các "
               "đặc điểm sau: lò phản ứng <b>bán liên tục</b> (thay vì gián "
               "đoạn) làm tồn kho monome trong lò thấp, vì phản ứng bắt đầu "
               "ngay khi monome đầu tiên được cấp; <b>không có bồn tiền trộn</b> "
               "monome — thứ sẽ tăng tồn kho; chỉ dùng <b>một lò phản ứng "
               "lớn</b> thay vì vài lò nhỏ để hệ đơn giản hơn (cấu trúc quá "
               "trình an toàn nội tại hơn); <b>hai khuấy trên cùng một trục</b> "
               "để tăng hiệu quả khuấy khi mực chất lỏng thay đổi; dùng vách "
               "ngăn để tăng hiệu quả khuấy; làm mát bằng cả áo khoác và <b>bộ "
               "ngưng hồi lưu</b>; vật liệu lò là <b>thép tráng bóng</b> có "
               "truyền nhiệt tốt hơn bình tráng thủy tinh; chuyển chất lỏng "
               "toàn/đến lò bằng <b>trọng lực</b> để giảm số bơm (an toàn thiết "
               "bị); hệ xả gồm <b>đĩa nổ</b> — an toàn hơn van xả một mình "
               "trong điều kiện bẩn; xả được dẫn tới <b>bể dập</b> chứa chất "
               "dập để dừng phản ứng và tách pha lỏng khỏi dòng xả — an toàn "
               "hơn bình tách Knock-out hoặc cyclone thường (cấu trúc quá "
               "trình an toàn); khí xả dẫn tới hệ ống đốt sau bể dập; ống đốt "
               "thường được dùng vì công suất lớn hơn hệ thu hồi có kiểm soát "
               "hoặc tháp rửa; việc <b>thêm chất ức chế</b> vào lò cũng có mặt "
               "để dừng phản ứng bằng hóa học — đơn giản nhưng có thể không "
               "phải lúc nào cũng tin cậy được (Hình 14)."))

    b.append(note("Bài học từ hai nghiên cứu tình huống: ISI dùng được làm hàm "
                  "thích nghi trong tối ưu di truyền — thường được đơn giản "
                  "hóa vì nhiều chỉ số thành phần là hằng số giữa các phương "
                  "án; các phương án an toàn nội tại hơn thường trùng với "
                  "thiết kế đơn giản hơn và tồn kho thấp hơn."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("14. Application of Inherent Safety Index for Computerized "
                "Process Synthesis",
                "14. Ứng dụng chỉ số an toàn nội tại trong tổng hợp quá trình"))

    b.append(p("Classically, synthesis of chemical processes is based only on "
               "economic and engineering aspects. There is, however, an "
               "increasing need to evaluate the safety of processes in the "
               "early stage of process design, because of government "
               "regulations and for practical engineering reasons. It is much "
               "easier to affect the process configuration and inherent safety "
               "in the conceptual design phase than in the later phases. "
               "Consequently, safety aspects should be included in "
               "computerized process synthesis. The presented ISI can be used "
               "as a tool to evaluate synthesized alternatives or as an "
               "<b>objective function</b> in synthesis. The existing safety "
               "estimation methods (e.g. Dow F&amp;E Index, computerized "
               "Hazop) are mostly intended for the more detailed engineering "
               "phases or for existing plants, and are not directly applicable "
               "in their full mode in the conceptual phase since they require "
               "detailed information on process equipment; other methods such "
               "as checklists are not easily changed into function form to be "
               "integrated into other design tools."))
    b.append(p("Process synthesis is a task of formulating the process "
               "configuration for a purpose by defining which operations or "
               "equipment are used and how they are connected together. There "
               "are two basic approaches: 1) classical process synthesis, "
               "analysis and evaluation, and 2) optimization of the process "
               "structure using a suitable objective function."))

    # ---- 14.1 ----------------------------------------------------------------
    b.append(h3("14.1 Classical Process Synthesis",
                "14.1 Tổng hợp quá trình cổ điển"))

    b.append(p("Classical process synthesis consists of the synthesis of the "
               "alternatives, their analysis and final evaluation. Hurme and "
               "Järveläinen (1995) presented a combined process synthesis and "
               "simulation system consisting of an interactive rule-based "
               "system used for generating process alternatives (Figure 10); "
               "the alternatives are simulated, costed and evaluated through "
               "profitability analysis. The system concept combines process "
               "synthesis, simulation and costing with uncertainty "
               "estimation."))
    b.append(fig(1, F.fig_c14_synthesis()))
    b.append(p("Heikkilä et al. (1996) expanded the work of Hurme and "
               "Järveläinen (1995) with environmental and safety aspects "
               "(Figure 11). The alternatives are simulated to determine the "
               "material and heat balances and to estimate the physical "
               "properties; then the alternatives are assessed in economic "
               "terms using the internal rate of return. The environmental "
               "effects are estimated by an equivalent amount of pollutant "
               "taking into consideration the harmfulness of the different "
               "effluent substances; environmental risks also include "
               "occupational-health aspects, to choose an inherently "
               "<b>healthier</b> process. The inherent safety is estimated in "
               "terms of the inherent safety index as described later."))
    b.append(fig(2, F.fig_c14_combined()))
    b.append(p("The final decision on the best alternative is not a clear "
               "choice, since the three parameters — cost-efficiency, "
               "environmental aspects and inherent safety — <b>cannot be "
               "merged into a single figure in a unique way</b>: process "
               "designers may emphasize these parameters differently depending "
               "on the company policy and the goal of the problem. "
               "Consequently, the alternatives have to be compared based on "
               "all the criteria, using for example the decision-chart method "
               "(Kepner and Tregoe, 1981) or the pairwise-comparison matrix "
               "presented by Saaty (1977)."))
    b.append(p("Safety aspects are considered in two phases (Figure 11). In "
               "the rule-based synthesis, some safety-related rules are "
               "applied in process-concept selections — such as \"separate "
               "corrosive or hazardous components first\" or \"avoid using "
               "chemically incompatible substances in the same process\". Not "
               "all safety-related matters — such as the selection of raw "
               "materials — are considered in the synthesis phase; they are "
               "given by the user. Also, generating universal synthesis rules "
               "considering safety is not easy. Therefore it is important to "
               "analyse the alternative designs by inherent safety indices, "
               "which describe e.g. flammability, toxicity and process "
               "conditions."))
    b.append(p("The conceptual design phase is <b>the most critical</b> when "
               "designing inherently safer plants, since the alternative "
               "process concepts are created and analysed in this phase. This "
               "emphasizes the need to introduce safety-evaluation tools into "
               "preliminary process design: time and money are saved when "
               "fewer expensive safety modifications are needed during the "
               "later stages of design. The safety evaluation has to be "
               "closely integrated into the existing preliminary process "
               "design environments to be readily available during design; "
               "the safety tools also benefit from the existing databanks and "
               "simulation programs for physical-property and phase-condition "
               "calculations. The ISI allows the evaluation of the inherent "
               "safety of process alternatives in a computerized process "
               "synthesis environment — a flexible and interactive comparison "
               "of alternatives in the conceptual design phase."))

    # ---- 14.2 ----------------------------------------------------------------
    b.append(h3("14.2 Process Synthesis by Optimization",
                "14.2 Tổng hợp quá trình bằng tối ưu hóa"))

    b.append(p("Process synthesis can be considered as an optimization task. "
               "The problem is that <b>the model to be optimized changes at "
               "the same time as the process configuration alters</b>. "
               "Therefore the possible optimization approaches are MINLP "
               "(mixed integer nonlinear programming) and genetic algorithms. "
               "The MINLP approach has been used in many articles (e.g. "
               "Grossmann and Kravanja, 1995): the method is rigorous but "
               "requires a dedicated mathematical algorithm, some of which are "
               "still under development. In genetic optimization the solution "
               "is searched in an evolutionary manner, which as such is quite "
               "familiar to a practising engineer; the problems are the "
               "requirement of coding the problem as genes and the slowness of "
               "the algorithm (many unnecessary cases are calculated due to "
               "mutations and crossovers), and the method does not guarantee "
               "that an optimal solution is reached. GA has already been used "
               "for separation-process synthesis (Hurme, 1996)."))

    b.append(h3("14.3 Genetic Optimization", "14.3 Tối ưu hóa di truyền"))

    b.append(p("Genetic algorithms (GA) are computational models of natural "
               "evolution, which use operations related to genetics to guide "
               "an optimizing process in a complex search space. GAs work with "
               "sets of individuals which, when properly coded, represent "
               "potential solutions. Populations are processed iteratively, "
               "starting from a random population, following the phases of "
               "<b>evaluation, selection, mating, crossover and mutation</b> "
               "(Figure 12). Selection is based on the evaluation of the "
               "individuals of a given population by means of a <b>fitness "
               "function</b>. The cycle is repeated until a termination "
               "condition, such as an error tolerance, is reached. It is "
               "characteristic of GA that individuals characterized by a "
               "common feature and exhibiting a high fitness grow "
               "exponentially. Even though convergence is not always "
               "guaranteed, GAs have been successful in solving difficult "
               "optimization problems; GAs do not pose special requirements on "
               "the problem (such as continuity), except that a proper coding "
               "of individuals and an appropriate objective function for "
               "evaluating the fitness of each individual must be possible. "
               "The proper choice of the fitness function is important since "
               "it guides the selection and optimization procedure (Goldberg, "
               "1989)."))
    b.append(fig(3, F.fig_c14_ga()))
    b.append(p("Hurme (1996) used GA to solve the synthesis problem of "
               "separating a mixture of hydrocarbons, and compared GA with a "
               "pure random version in which the crossover and mutation "
               "operations were replaced by a random generation of new "
               "solutions: there was no difference during the first "
               "generations, but it became significant after some generations "
               "— GA reached the solution after ten generations with about "
               "1100 different possible solutions, while the random version "
               "required tens of generations. GA seems both fast compared to "
               "random optimization and not too computationally intensive."))
    b.append(p("Hurme and Heikkilä (1998) expanded the GA approach of Hurme "
               "(1996) with a <b>safety function</b>. Because the model is "
               "uncontinuous, ordinary optimization methods cannot be used, "
               "but a genetic algorithm is employed instead: the structure of "
               "the process is represented as a string of integers, which "
               "describes the operations required and how they are connected "
               "together, and <b>an inherent safety index is used as the "
               "objective function (i.e. fitness)</b>. The index has been "
               "developed for safety estimations in the early stages of "
               "process design; most of its subindices are quite simple to "
               "estimate, except the subindex for safe process structure, "
               "which is estimated by case-based reasoning using a database of "
               "good and bad design cases. This index can also be used as an "
               "objective function to be optimized, if the inherent process "
               "safety is to be maximized in a systematic way."))

    # ---- 14.4 ----------------------------------------------------------------
    b.append(h3("14.4 Principle of the Method", "14.4 Nguyên lý của phương pháp"))

    b.append(p("In the approach by Hurme and Heikkilä (1998), inherent safety "
               "is the <b>only objective function</b> considered in the "
               "process synthesis. It is estimated by the Inherent Safety "
               "Index (Heikkilä et al., 1996), developed for inherent-safety "
               "estimations in conceptual process design. The structure of the "
               "process is represented as a string of integers (a gene) "
               "representing the required operations, their types and how they "
               "are connected; the inherent safety index is the fitness "
               "function. The basic steps of the genetic optimization "
               "algorithm are:"))
    b.append(ol([
        "Generation of an initial population of random separation sequences — "
        "the sequences describe both which equipment items are used and how "
        "they are connected.",
        "Random selection of sequences and generation of new solutions using a "
        "crossover procedure (the crossover location is also chosen randomly); "
        "since the crossover may result in an impossible sequence, a checking "
        "and revision procedure is required — its type depends on the type of "
        "process synthesized.",
        "Mutation of sequences at a randomly chosen location.",
        "Evaluation of the sequences using the inherent-safety fitness "
        "function.",
        "Selection of the best sequences and removal of the worst and "
        "redundant sequences, so that the population size stays constant.",
        "Repetition of steps 2–6 until the improvement is below the given "
        "tolerance.",
    ]))

    b.append(h3("14.4.1 Case Study; Separation Process",
                "14.4.1 Nghiên cứu tình huống — quá trình tách"))

    b.append(p("A synthesis problem on the purification of <b>butenes</b> is "
               "discussed (Hurme and Heikkilä, 1998): the aim is to synthesize "
               "the separation process by <b>maximizing the inherent "
               "safety</b>, measured as the Inherent Safety Index. In the "
               "process, a mixture of propane, 1-butene, n-butane, 2-butenes "
               "and n-pentane is separated to produce technically pure "
               "component streams; both ordinary distillation (method 1) and "
               "extractive distillations (methods 2 and 3) are used. The feed "
               "composition and the relative volatilities of adjacent "
               "components for the different separation methods are given in "
               "Table 30."))
    b.append(table(("Component", "mol-%", "α₁", "α₂", "α₃"), _T30,
              "Table 30 · Feed compositions and relative volatilities in the "
              "case study."))
    b.append(p("Separation-synthesis problems are highly combinatorial when "
               "the number of components and separation methods is large: in "
               "this simple case of five components and three separation "
               "methods there are <b>1134 different solutions</b> (Hurme, "
               "1996); two of them are shown in Figure 13 as an example. The "
               "column vapor loads (vapor flow rates up the columns) are "
               "calculated to determine the approximate equipment sizes; an "
               "approximate method for calculating the vapor flow V in a "
               "column is (Hurme, 1996):"))
    b.append(eq("V = D(R<sub>F</sub>(α − 1) + 1)", "(11)"))
    b.append(p("where R<sub>F</sub> = R / R<sub>min</sub>, V is the vapor "
               "flow, D the distillate flow rate, F the feed flow rate, α the "
               "relative volatility, R the reflux rate and R<sub>min</sub> the "
               "minimum reflux rate."))
    b.append(fig(4, F.fig_c14_separations()))
    b.append(p("The steps of the genetic algorithm in this problem: 1) an "
               "initial population of random separation sequences is "
               "generated — the sequences describe both the order in which "
               "components are separated and the separation method used; e.g. "
               "the left-hand sequence in Figure 13 is described by the string "
               "<b>23 12 14 11</b> — the first integer is the separation "
               "method and the second the heavy-key component of the split in "
               "the column; 2) crossover — the crossover length is fixed to "
               "two components; since the crossover may result in a sequence "
               "containing some components twice, a checking and revision "
               "procedure is implemented (all components must be included; if "
               "not, the original instance is changed to the missing "
               "component); 3) mutation of both the separation method and the "
               "sequence at a randomly chosen location; 4) evaluation of the "
               "sequences by the inherent-safety fitness function; 5) "
               "selection of the best sequences and removal of the worst and "
               "redundant ones so that the population size stays constant; "
               "6) steps 2–6 are repeated until the improvement is under the "
               "defined tolerance."))
    b.append(p("The initial population size was <b>5 sequences</b>; the "
               "crossover population was 2 sequences and the mutated "
               "population 2 sequences per generation — 4 new sequences per "
               "generation in total; after selection the population size was "
               "kept at 5. The fitness function was based on the inherent "
               "safety index, <b>simplified</b>: there are only minor "
               "differences in the safety properties of the compounds, so most "
               "subindices are the same for all configurations; the equipment "
               "type (distillation) is the same, so the equipment-safety "
               "subindex is constant too; the process structures are quite "
               "similar, so the process-structure subindex was not evaluated "
               "and case-based reasoning was not needed. However, <b>the "
               "number of columns changes if extractive distillation is "
               "used</b>, so the fluid inventory becomes a major safety "
               "parameter; the inventory depends on the column sizes. It was "
               "assumed that all columns are designed for the same superficial "
               "vapor velocity, so the column area is directly proportional to "
               "the vapor flow rate, and the liquid hold-up proportional to "
               "the column area; therefore the total fluid inventory is "
               "considered directly proportional to the total vapor flow of "
               "the columns — calculated by Equation 11 for each column."))
    b.append(p("The genetic algorithm reached the solution usually in <b>ten "
               "generations</b> for this problem of more than 1100 solutions; "
               "a random optimization would require tens of generations. The "
               "best solution found is the first configuration (23 12 14 11) "
               "in Figure 13. The results with the inherent-safety objective "
               "function are <b>somewhat different from those with an "
               "economic objective function</b> (Hurme, 1996): with the "
               "inherent-safety function, simple distillations were favoured "
               "more; the exceptions are cases where extractive distillation "
               "could improve the separation very dramatically. The reason: in "
               "simple distillations only one column is required per split, "
               "but in extractive distillation two columns are needed since "
               "the solvent must also be separated — causing a larger fluid "
               "inventory, especially since the extraction solvent is highly "
               "flammable. The results are well justified by common sense: one "
               "of the principles of inherent safety is to <b>use simpler "
               "designs and reduce inventories</b> to enhance safety."))

    b.append(h3("14.4.2 Case Study; Emulsion Polymerization Process",
                "14.4.2 Nghiên cứu tình huống — quá trình trùng hợp nhũ"))

    b.append(p("As another case study, a process synthesis of an <b>emulsion "
               "polymerization</b> process is given (Hurme and Heikkilä, "
               "1998). In emulsion polymerization, unsaturated monomers or "
               "their solutions are dispersed in a continuous phase with the "
               "aid of an emulsifier and polymerized; the product is a "
               "dispersion of polymers called a <b>latex</b>. The raw "
               "materials are highly flammable unsaturated hydrocarbons and "
               "the reaction is exothermic — both cause a risk. The main "
               "phases and systems of an emulsion polymerization plant are "
               "listed in Table 31."))
    b.append(table(("Phase / system", ), _T31_EN,
              "Table 31 · The main phases and systems of an emulsion "
              "polymerization process (Kroschwitz, 1986). * = considered."))
    b.append(p("Information on the safety properties, accidents, design "
               "recommendations and existing designs of the emulsion "
               "polymerization process was gathered from the literature; only "
               "the phases marked with an asterisk (*) in Table 31 were "
               "considered. About <b>50 design recommendations or cases</b> on "
               "the topic were found; a case base was formed of this "
               "information together with some general design recommendations, "
               "and the cases were evaluated based on the safe process "
               "structure subindex, which was included into the cases in the "
               "database."))
    b.append(p("The main variables in the selected process phases were chosen "
               "and coded with integers for the synthesis procedure — "
               "including the operation and equipment types used and how they "
               "are connected. The <b>14 main variables</b> were: 1) premixing; "
               "2) preheating; 3) reactor type and mode of operation; 4) "
               "number of reactors; 5) reactor construction material; 6) "
               "reactor mixing; 7) baffles in the reactor; 8) reactor heat "
               "transfer system; 9) method of liquid transfers; 10) relief "
               "system location; 11) relief equipment type; 12) reaction "
               "stopping method; 13) relief recovery system; 14) vent "
               "treatment equipment."))
    b.append(p("The genetic optimization was started with an initial "
               "population size of five, generated randomly; the algorithm "
               "included crossover of two randomly selected sequences and "
               "random mutations on two sequences (the number of mutations per "
               "sequence varied from four at the beginning to one at the "
               "end). The steps: 1) a random initial population of 5; 2) "
               "crossover of two randomly selected sequences; 3) mutation of "
               "two sequences; 4) case-based reasoning on the safe process "
               "structure subindex; 5) calculation of the fitness using the "
               "inherent safety index — only inventory, equipment safety, heat "
               "of reaction and process-configuration subindices were "
               "considered; 6) selection of the best sequences so that the "
               "population size stays at five; 7) repetition of steps 2–7 "
               "until the fitness improvement is below the tolerance. The "
               "procedure converged in <b>less than 20 generations</b>; the "
               "optimum configuration had an Inherent Safety Index value of "
               "<b>16</b> (the optimization typically started from a value of "
               "28–30). The inherently safest synthesized alternative is "
               "shown in Figure 14."))
    b.append(fig(5, F.fig_c14_polymer()))
    b.append(p("The process with the lowest inherent-safety index value "
               "contains the following features: a <b>semibatch</b> (instead "
               "of batch) reactor, resulting in a low monomer inventory in the "
               "reactor since the reaction starts immediately when the first "
               "monomers are fed; <b>no premixing tank</b> for the monomers, "
               "which would increase the inventory; only <b>one large "
               "reactor</b> instead of several smaller, to make the system "
               "simpler (an inherently safer process structure); <b>two "
               "mixers on one shaft</b> to increase the mixing efficiency as "
               "the liquid level changes; baffles for the same purpose; "
               "cooling by both the <b>jacket and a reflux condenser</b>; "
               "<b>polished steel</b> reactor construction, which has better "
               "heat-transfer properties than a glass-lined vessel; liquid "
               "transfers to and from the reactor by <b>elevation</b> to "
               "reduce the number of pumps (equipment safety); a relief system "
               "including a <b>rupture disk</b>, safer than a relief valve "
               "alone in fouling conditions; the relief led to a <b>quench "
               "tank</b> containing quench liquid to stop the reaction and "
               "separate the liquid phase from the relief — safer than an "
               "ordinary knock-out drum or cyclone (safe process structure); "
               "the vent led to a flare system after the quench tank; an "
               "ordinary flare is used, since it has a larger capacity than a "
               "controlled collection system or a scrubber; an <b>inhibitor "
               "addition</b> to the reactor is also included to stop the "
               "reaction chemically — a simple but possibly not always "
               "reliable method (Figure 14)."))

    b.append(note("Lessons from the two case studies: the ISI works as a "
                  "fitness function in genetic optimization — usually "
                  "simplified since many subindices are constant across the "
                  "alternatives; the inherently safer alternatives typically "
                  "coincide with simpler designs and lower inventories."))

    return "".join(b)
