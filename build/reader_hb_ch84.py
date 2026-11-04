# -*- coding: utf-8 -*-
"""Handbook Chapter 84 — Applied Intelligence Processing (Xử lý thông minh ứng dụng).
Run:  python build/reader_hb_ch84.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch84-applied-intelligence-processing'
CH_NO = 84
TITLE_EN = 'Applied Intelligence Processing'
TITLE_VI = 'Xử lý thông minh ứng dụng'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương 84 do Peter H. Sydenham và Rodney Pratt (University of South Australia) biên soạn, có phạm vi khác với các chương xử lý tín hiệu thông thường: tác giả không trình bày thuật toán lọc hay biến đổi, mà đặt câu hỏi <b>tri thức được đưa vào phép đo như thế nào</b>. Chương đi từ phương pháp thuật toán, tổng quan phương pháp trí tuệ ứng dụng, phép ánh xạ, lý thuyết quyết định, năm họ phương pháp AI, đến bài toán còn khó nhất là hiệu chuẩn chính các hệ xử lý thông minh.'))
    b.append(p('Thông điệp trung tâm: một hệ thống đo không chỉ tạo ra con số, mà tạo ra một <i>khẳng định</i> kèm mức độ tin cậy. Vì vậy cần phân biệt rõ phép tính tất định (algorithmic) với suy luận (intelligence), và phải có cách kiểm chứng cái sau.'))
    b.append(h2('84.1 Mở đầu', '84.1 Introduction'))
    b.append(p("Các phép đo hiện đại tạo ra nhiều kênh dữ liệu hơn khả năng diễn giải của người vận hành. 'Xử lý thông minh' chỉ việc đưa tri thức về miền đo, về thiết bị và về mục đích sử dụng vào chuỗi xử lý, để hệ thống tự chọn phép biến đổi, tự gắn nhãn trạng thái và tự báo mức tin cậy. Tác giả nhấn mạnh rằng thuật ngữ này không đồng nghĩa với mạng nơ-ron: đó là một lớp phương pháp cạnh tranh với các thuật toán tất định."))
    b.append(h2('84.2 Tổng quan phương pháp thuật toán', '84.2 Overview of Algorithmic Methods'))
    b.append(p('Phương pháp thuật toán gồm các phép biến đổi được định nghĩa đầy đủ trước: hiệu chuẩn đa điểm, bù nhiệt độ, lọc tuyến tính, tích phân, biến đổi Fourier, ước lượng bình phương nhỏ nhất. Ưu điểm là kết quả lặp lại, dễ truy vết, dễ chứng minh độ không đảm bảo và dễ được cơ quan đo lường chấp nhận. Giới hạn xuất hiện khi mối quan hệ giữa tín hiệu và đại lượng cần đo không thể viết gọn thành công thức, hoặc khi tri thức chỉ tồn tại dưới dạng kinh nghiệm của chuyên gia.'))
    b.append(h2('84.3 Tổng quan phương pháp trí tuệ ứng dụng', '84.3 Overview of Applied Intelligence Methods'))
    b.append(p('Nhóm này gồm hệ chuyên gia (luật và khung), logic mờ, thuật toán di truyền, mạng nơ-ron nhân tạo và các hệ lai. Điểm chung là <b>học hoặc suy luận từ ví dụ</b> thay vì giải công thức cho trước, nhờ đó xử lý được nhiễu, phi tuyến và tri thức mơ hồ. Đổi lại, kết quả phụ thuộc vào tập mẫu huấn luyện, khó giải thích và — theo tác giả — khó hiệu chuẩn theo nghĩa đo lường học.'))
    b.append(h2('84.4 Phép ánh xạ, xét tổng quát', '84.4 Mapping, in General'))
    b.append(p('Mọi hệ xử lý thông minh đều thực hiện một phép ánh xạ từ không gian quan sát (vector đặc trưng x) sang không gian kết luận (nhãn, giá trị ước lượng hoặc hành động). Vấn đề then chốt là ánh xạ có <b>được định nghĩa đủ</b> trên toàn miền hoạt động hay không: vùng ngoài tập huấn luyện là vùng nội suy/ngoại suy mù, nơi hệ vẫn trả về một kết quả trông có vẻ hợp lệ nhưng không còn căn cứ.'))
    b.append(eq('f : X → Y ,   x = (x₁, x₂, …, x_n) ↦ y   (kèm ước lượng độ tin cậy c(y))', '84.1'))
    b.append(p('Vì vậy thiết kế phải bắt đầu từ việc phân vùng miền đo, xác định các biến nhiễu, quyết định mức chi tiết của không gian kết luận và quy định hành vi khi đầu vào nằm ngoài miền đã biết (từ chối kết luận, chuyển về thuật toán tất định, hoặc báo cần hiệu chuẩn lại).'))
    b.append(h2('84.5 Cơ sở lý thuyết quyết định', '84.5 Basics of Decision Theory'))
    b.append(h3('Các quy tắc về quá trình ra quyết định', 'Rules about a Decision-Making Process'))
    b.append(p('Lý thuyết quyết định hình thức hoá việc chọn hành động khi có bất định: tập trạng thái thật của hệ, tập quan sát, hàm mất mát (loss) khi quyết sai, và quy tắc quyết định tối thiểu hoá rủi ro Bayes. Ngưỡng chấp nhận không nên đặt cảm tính mà phải suy từ chi phí tương đối của hai loại sai: báo sót (miss) và báo nhầm (false alarm).'))
    b.append(eq('R(a|x) = Σ L(a, s)·P(s|x) ,   chọn a* = argmin_a R(a|x)', '84.2'))
    b.append(h3('Trích xuất tham số', 'Extracting Parameters'))
    b.append(p("Trước khi ra quyết định phải rút từ tín hiệu các tham số có ý nghĩa vật lý: giá trị trung bình, độ lệch, xu hướng, thành phần phổ, hệ số hình dạng, hay các đặc trưng thống kê bậc cao. Tác giả lưu ý rằng chính bước này thường quyết định kết quả hơn cả bộ phân loại: một đặc trưng không bất biến với nhiệt độ hay nguồn nuôi sẽ khiến hệ 'học' sai quy luật."))
    b.append(h3('Hai ví dụ về phương pháp hỗ trợ quyết định', 'Two Examples of Decision Assistance Methods'))
    b.append(p("Ví dụ thứ nhất là hệ chẩn đoán thiết bị: từ vector đặc trưng rung động, hệ luật đưa ra danh sách nguyên nhân có xếp hạng kèm giải thích, để chuyên gia xác nhận. Ví dụ thứ hai là hệ phân loại tín hiệu / nhận dạng trạng thái quy trình, nơi đầu ra không phải một con số đo mà là nhãn 'bình thường / cảnh báo / lỗi' kèm xác suất. Cả hai đều minh hoạ nguyên tắc: hệ hỗ trợ, không thay thế, trách nhiệm đo lường của con người."))
    b.append(h2('84.6 Các phương pháp AI chính', '84.6 Principal AI Methods'))
    b.append(table(['Phương pháp', 'Biểu diễn tri thức', 'Điểm mạnh', 'Điểm yếu'], [['Lý thuyết đo lường', 'Cấu trúc hình thức', 'Nền tảng độ tin cậy', 'Khó áp cho hệ phức tạp'], ['Hệ luật / khung', 'Luật IF–THEN, frame', 'Giải thích được', 'Bùng nổ luật, bảo trì'], ['Logic mờ', 'Hàm thuộc, luật mờ', 'Xử lý mơ hồ, ngôn ngữ', 'Hiệu chuẩn hàm thuộc'], ['Thuật toán di truyền', 'Quần thể, fitness', 'Tối ưu không gradient', 'Không bảo đảm hội tụ'], ['Mạng nơ-ron', 'Trọng số học được', 'Xấp xỉ phi tuyến tốt', 'Hộp đen, cần nhiều mẫu']], 'Bảng 84.1 · Năm họ phương pháp AI theo chương 84.'))
    b.append(p("<b>Lý thuyết đo lường</b> cung cấp khung hình thức để nói về giá trị, độ không đảm bảo và khả năng truy vết — thứ mà các phương pháp học thường thiếu. <b>Hệ luật và khung</b> mã hoá kinh nghiệm chuyên gia, ưu điểm là giải thích được từng kết luận. <b>Logic mờ</b> thay ngưỡng cứng bằng hàm thuộc, thích hợp với mô tả bằng ngôn ngữ ('hơi nóng', 'rung khá mạnh'). <b>Thuật toán di truyền</b> tối ưu cấu trúc hoặc tham số khi không có đạo hàm. <b>Mạng nơ-ron</b> học ánh xạ phi tuyến trực tiếp từ mẫu."))
    b.append(h2('84.7 Bài toán hiệu chuẩn của xử lý thông minh', '84.7 Problems in Calibration of AI Processing Methods'))
    b.append(p("Đây là đóng góp quan trọng nhất của chương. Một thiết bị đo thông thường được hiệu chuẩn bằng cách đưa vào các giá trị chuẩn biết trước và đối chiếu đầu ra. Với hệ học máy, chính tập huấn luyện đóng vai trò 'chuẩn', nhưng nó thường không truy vết được về chuẩn quốc gia, không bao phủ hết miền đo và có thể chứa sai lệch hệ thống. Hệ quả là không có cách nào gán độ không đảm bảo đo lường cho đầu ra theo nghĩa GUM."))
    b.append(p('Tác giả nêu các vấn đề cụ thể: phân biệt <b>huấn luyện</b> với <b>hiệu chuẩn</b>, sự trôi của khái niệm (concept drift) khi thiết bị già hoá hoặc quy trình đổi, nhu cầu tập kiểm chứng độc lập và được gán nhãn bởi phương pháp khác, tính bất biến của đặc trưng với điều kiện môi trường, và yêu cầu hệ phải biết <b>từ chối</b> kết luận khi nằm ngoài miền đã học. Khuyến nghị là giữ một đường đo tất định song song làm đối chứng, và coi đầu ra AI như một phép đo có điều kiện kèm mức tin cậy, không phải chân lý.'))
    b.append(p('Kết luận thực hành: trước khi đưa AI vào một chuỗi đo chịu trách nhiệm pháp lý hoặc an toàn, phải trả lời được bốn câu — chuẩn nào đã dùng để gán nhãn, miền nào được bao phủ, sai số khi từ chối hoặc nhầm là bao nhiêu, và ai chịu trách nhiệm khi đầu ra sai.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Chương 84 không dạy thuật toán lọc mà đặt nền tảng cho việc dùng tri thức trong đo lường: phân biệt phương pháp thuật toán tất định và suy luận thông minh; mọi hệ đều là một phép ánh xạ f: X → Y cần xác định miền hiệu lực; quyết định phải tối thiểu rủi ro Bayes R(a|x) = ΣL·P(s|x); năm họ AI là lý thuyết đo lường, hệ luật/khung, logic mờ, thuật toán di truyền và mạng nơ-ron. Vấn đề mở lớn nhất là hiệu chuẩn: huấn luyện không phải hiệu chuẩn, và cần đường đo tất định đối chứng cùng khả năng từ chối kết luận ngoài miền học.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 84. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Peter H. Sydenham and Rodney Pratt (University of South Australia), Applied Intelligence Processing (CRC, 1999). The chapter is not a signal-processing algorithm catalogue: it asks how knowledge enters a measurement. It contrasts deterministic algorithmic methods (calibration, compensation, filtering, least squares) with applied-intelligence methods that learn or infer from examples, treats every intelligent system as a mapping f: X → Y whose domain of validity must be defined and outside which outputs must be refused, introduces decision theory with Bayes risk R(a|x) = sum L(a,s)P(s|x) and the miss/false-alarm cost trade-off, parameter extraction as the step that dominates classifier performance, and two decision-assistance examples. Five principal AI methods are reviewed: measurement theory, rule-/frame-based systems, fuzzy logic, genetic algorithms and artificial neural networks. The closing section argues that training is not calibration: learned systems lack traceability to standards, suffer concept drift, need independent validation sets and features invariant to environment, and should run alongside a deterministic reference path with an explicit confidence measure.'))
    b.append(eq('f : X → Y ,   x = (x₁, x₂, …, x_n) ↦ y   (kèm ước lượng độ tin cậy c(y))', '84.1'))
    b.append(eq('R(a|x) = Σ L(a, s)·P(s|x) ,   chọn a* = argmin_a R(a|x)', '84.2'))
    b.append(table(['Method', 'Knowledge representation', 'Strength', 'Weakness'], [['Measurement theory', 'Formal structure', 'Confidence foundation', 'Hard for complex systems'], ['Rule/frame systems', 'IF–THEN rules, frames', 'Explainable', 'Rule explosion, maintenance'], ['Fuzzy logic', 'Membership functions', 'Handles vagueness', 'Membership calibration'], ['Genetic algorithms', 'Population, fitness', 'Gradient-free search', 'No convergence guarantee'], ['Neural networks', 'Learned weights', 'Nonlinear approximation', 'Black box, data hungry']], 'Table 84.1 · The five AI method families of Chapter 84.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE,
                                body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
