# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 11, Combined Feedback and Feedforward
Control (Wolfgang Altmann, IDC Technologies)."""
import pc11fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 7
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Điều khiển kết hợp</em> — vừa theo hướng vừa phản hồi trên cùng một vòng. · "
            "<em>Bộ cộng (summer)</em> — khối cộng tín hiệu theo hướng với đầu ra của bộ điều khiển sơ "
            "cấp. · "
            "<em>Phép tính tăng dần (incremental)</em> — bộ cộng chỉ cộng thêm độ lệch, không gán lại "
            "toàn bộ vị trí van. · "
            "<em>Khởi tạo (initialization)</em> — nạp trước đầu ra của TC bằng tổng tín hiệu theo hướng "
            "và điểm đặt của FC. · "
            "<em>Cân bằng nhiệt</em> — quan hệ F1·C·(T2 − T1) = F·h quyết định lượng nhiên liệu cần cấp.")
    return note(
        "<b>Key terms.</b> <em>Combined control</em> — feedforward and feedback acting on the same loop. "
        "· <em>Summer</em> — the block that adds the feedforward signal to the primary controller's "
        "output. · <em>Incremental calculation</em> — the summer adds a deviation rather than "
        "re-assigning the whole valve position. · <em>Initialisation</em> — pre-loading the TC's output "
        "with the feedforward signal plus the FC's set point. · <em>Heat balance</em> — the relation "
        "F1·C·(T2 − T1) = F·h that fixes the fuel demand.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương trước kết thúc bằng một câu phán xử: điều khiển theo hướng một mình thì luôn còn phần "
        "dư, vì mô hình bù không bao giờ hoàn hảo. Chương này là câu trả lời cho phần dư đó. Nó không "
        "đưa ra một cơ chế thứ ba nào mới — nó chỉ ghép hai cơ chế đã có, và dành phần lớn độ dài cho "
        "những chi tiết mà việc ghép ấy sinh ra: bộ cộng, khởi tạo, và thứ tự chỉnh định."))
    b.append(p(
        "Đây là chương ngắn nhất của phần điều khiển trong sách, và cũng là chương thực dụng nhất. Mọi "
        "thứ trong đây đều là việc phải làm trên một hệ thống thật, vào một buổi sáng vận hành thử."))

    b.append(h2("11.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Trình bày được khái niệm và chiến lược của điều khiển kết hợp phản hồi và theo hướng;",
        "Trình bày được cách xây dựng các thủ tục chỉnh định cho điều khiển kết hợp phản hồi và theo "
        "hướng."]))

    b.append(h2("11.2 Khái niệm theo hướng", "The Feedforward Concept"))
    b.append(p(
        "Chương 10 đã trình bày các khái niệm của điều khiển theo hướng và chỉ ra một vấn đề nó để lại: "
        "PV trôi khỏi giá trị SP của hệ thống. Nguyên nhân duy nhất là vì PV <b>không</b> được tính đến "
        "trong điều khiển theo hướng; nếu có tính đến thì nó đã trở thành một hệ điều khiển phản hồi "
        "(vòng kín) rồi."))
    b.append(p(
        "Xem xét khái niệm theo hướng cho thấy nó thường được dùng để làm giảm tác động của nhiễu lên "
        "một quá trình. Điều này đạt được bằng cách phát hiện và đo một nhiễu quá trình rồi thay đổi "
        "một biến điều khiển liên quan <em>trước khi</em> nhiễu có tác động bất lợi lên chính quá trình."))
    b.append(p(
        "Cần nhớ rằng nhiễu quá trình bao gồm mọi thứ từ những thay đổi bất ngờ về:"))
    b.append(ul([
        "<b>độ lớn</b> của áp suất, lưu lượng, nhiệt độ và bất kỳ đại lượng vật lý nào khác gắn với quá "
        "trình;",
        "hoặc những thay đổi về <b>thời gian</b> của bất kỳ đáp ứng nào của quá trình."]))
    b.append(p(
        "Đại lượng thứ hai — THỜI GIAN — rất hay bị bỏ qua như một thứ có thể cần được sửa trong môi "
        "trường quá trình. Điều này được minh hoạ ở hình khớp thời gian của chương 10 (Hình 10-5 của bản "
        "dịch này, tức Figure 10.3 trong bản gốc), nơi ta dùng điều khiển theo hướng để làm cho thời "
        "gian cấp nhiệt và thời gian nguội đi của một hệ bộ gia nhiệt dòng liệu trở nên bằng nhau."))
    b.append(fig(1, F.fig_11_1()))
    b.append(p(
        "Việc này phải làm cho các đáp ứng của quá trình — cả về độ lớn lẫn về thời gian — trở nên giống "
        "nhau, bất kể PV đi theo chiều nào. Nếu đạt được điều đó thì việc chỉnh định hệ thống trở nên dễ "
        "hơn, và kết quả là điều khiển ổn định và chính xác hơn."))
    b.append(p(
        "Câu cuối đó đáng để dừng lại, vì nó là lý do kỹ thuật thật sự khiến người ta bỏ công khớp thời "
        "gian. Một vòng điều khiển chỉ có một bộ tham số. Nếu quá trình cư xử khác nhau khi PV tăng và "
        "khi PV giảm — nóng lên nhanh, nguội đi chậm — thì bộ tham số ấy chỉ có thể tối ưu cho một trong "
        "hai chiều. Chiều còn lại sẽ hoặc chậm chạp, hoặc dao động. Khớp được hai chiều thì một bộ tham "
        "số đủ dùng cho cả hai, và đó chính là điều kiện để chỉnh định có ý nghĩa."))

    b.append(h2("11.3 Khái niệm phản hồi", "The Feedback Concept"))
    b.append(p(
        "Chương 5 đã trình bày các khái niệm điều khiển vòng kín và tính ổn định liên quan tới hệ phản "
        "hồi. Nói chung, người ta chấp nhận rằng một hệ phản hồi làm việc chính xác và hiệu quả hơn nếu "
        "cả nhiễu quá trình lẫn thời gian trễ (thời gian lag) đều được giữ ở mức tối thiểu. Từ đó có thể "
        "thấy điều khiển theo hướng có thể được dùng để đạt được chính yêu cầu mà điều khiển phản hồi "
        "đang đặt ra."))
    b.append(p(
        "Nếu ta kết hợp một hệ theo hướng được cấu hình chính xác với một hệ phản hồi được chỉnh định "
        "tốt, kết quả phải trở thành một hệ điều khiển gần như vận hành tối ưu."))
    b.append(quote(
        "Hai cơ chế không cạnh tranh nhau; chúng chia nhau hai nửa khác nhau của cùng một vấn đề. Theo "
        "hướng xử lý nhiễu <em>trước</em> khi nó vào vòng; phản hồi xử lý mọi thứ còn lại <em>sau</em> "
        "khi nó đã vào.",
        "Tóm ý mục 11.3"))
    b.append(p(
        "Cần nói rõ một điều mà câu “gần như tối ưu” ở trên có thể che lấp: kết hợp hai cơ chế không làm "
        "hệ thống trở nên dễ thiết kế hơn, mà khó hơn. Một hệ chỉ có phản hồi thì chỉ có một bộ tham số "
        "phải lo. Một hệ kết hợp có thêm mô hình theo hướng, thêm bộ cộng, thêm trạng thái khởi tạo — và "
        "mỗi thứ đó đều có thể sai theo cách riêng của nó."))

    b.append(h2("11.4 Kết hợp điều khiển phản hồi và theo hướng",
                "Combining Feedback and Feedforward Control"))
    b.append(p(
        "Hình 11-2 minh hoạ một khái niệm trong đó ta kết hợp cả hai phương pháp điều khiển vào hệ điều "
        "khiển bộ gia nhiệt dòng liệu."))
    b.append(fig(2, F.fig_11_2()))
    b.append(p(
        "Chương 9 (“Các mode đầu ra, phương trình vận hành và điều khiển cascade”) và chương 10 (“Khái "
        "niệm và ứng dụng điều khiển theo hướng”) đã bao quát phần lớn các khía cạnh phải xét khi dùng "
        "điều khiển phản hồi và theo hướng. Ở đây ta sẽ tập trung vào tác động của <b>bộ cộng</b> và một "
        "vài khía cạnh chỉnh định của hệ điều khiển kết hợp."))
    b.append(p(
        "Nhìn Hình 11-2 theo hai nửa. Nửa trên là chuỗi theo hướng: FT đo lưu lượng vào, khối tính toán "
        "quy đổi nó thành nhiệt lượng cần cấp, khâu lead/lag khớp thời gian, và kết quả đi vào bộ cộng. "
        "Nửa dưới là vòng phản hồi: TT đo nhiệt độ ra, TC so với điểm đặt và đưa hiệu chỉnh lên bộ cộng. "
        "Hai nửa gặp nhau ở đúng một điểm, và điểm đó là biến điều khiển duy nhất của hệ: lưu lượng nhiên "
        "liệu."))

    b.append(h2("11.5 Bộ cộng phản hồi — theo hướng", "Feedback - Feedforward Summer"))
    b.append(p(
        "Tham chiếu Hình 11-2, ta thấy chỉ có <b>một</b> biến điều khiển là lưu lượng nhiên liệu, nhưng "
        "lại có hai khái niệm điều khiển kết hợp. Điều khiển theo hướng dựa trên lưu lượng khối — cân "
        "bằng nhiệt:"))
    b.append(eq(
        "F<sub>1</sub>·C·(T<sub>2</sub> − T<sub>1</sub>) = F·h", "11.1"))
    b.append(p(
        "và điều khiển phản hồi kiểu cascade dường như <em>tranh nhau</em> quyền dùng biến điều khiển duy "
        "nhất ấy, là lưu lượng nhiên liệu."))
    b.append(p(
        "Tuy vậy, nếu nhớ lại khái niệm bù trừ chi phối điều khiển theo hướng, thì đầu ra của điều khiển "
        "theo hướng (từ khối lead/lag) thường được đưa thẳng vào <b>điểm đặt</b> của bộ điều khiển lưu "
        "lượng nhiên liệu FC. Vào giá trị đến từ điều khiển theo hướng đó, ta phải <b>cộng thêm</b> giá "
        "trị đầu ra của bộ điều khiển sơ cấp (bộ điều khiển nhiệt độ TC)."))
    b.append(p(
        "Cần nhớ rằng đây là những phép tính <b>tăng dần</b> (incremental) chứ <b>không</b> phải tuyệt "
        "đối. Đó không phải một chi tiết kỹ thuật nhỏ. Nếu cả hai bộ điều khiển đều đòi một vị trí van "
        "tuyệt đối trong dải 0–100 %, chúng sẽ tranh nhau quyền ghi vào cùng một con số, và kết quả phụ "
        "thuộc vào việc chu kỳ quét nào chạy sau cùng — một hành vi không xác định. Nếu một bên đặt giá "
        "trị gốc và bên kia chỉ thêm một hiệu chỉnh, thì chỉ còn một lệnh duy nhất và nó có thể dự đoán "
        "được."))
    b.append(fig(3, F.fig_11_3()))
    b.append(p(
        "Hình 11-4 cho thấy vì sao giá trị gốc ấy lại quan trọng đến thế. Từ (11.1) suy ra lượng nhiên "
        "liệu cần cấp:"))
    b.append(eq(
        "F = F<sub>1</sub>·C·(T<sub>2</sub> − T<sub>1</sub>) / h", "11.2"))
    b.append(p(
        "Quan hệ này tuyến tính theo lưu lượng vào và tuyến tính theo độ tăng nhiệt độ. Vì thế mà một "
        "khối theo hướng chỉ cần hai phép nhân — và cũng vì thế mà nó có một giới hạn cứng: khi ΔT lớn, "
        "van nhiên liệu hết dư địa từ rất sớm. Với ΔT = 60 °C, dòng vào chỉ cần đạt 67 % là đã cần 100 % "
        "nhiên liệu. Ở điểm đó khối theo hướng không còn gì để bù, và mọi thứ phải trông vào vòng phản "
        "hồi."))
    b.append(fig(4, F.fig_11_4()))

    b.append(h2("11.6 Khởi tạo hệ điều khiển kết hợp phản hồi và theo hướng",
                "Initialization of a Combined Feedback and Feedforward Control System"))
    b.append(p(
        "Vì ta có sự kết hợp của điều khiển theo hướng, điều khiển phản hồi và điều khiển cascade, nên "
        "phương pháp khởi tạo là quan trọng."))
    b.append(p("Giá trị dùng để KHỞI TẠO ĐẦU RA (OP) CỦA BỘ ĐIỀU KHIỂN SƠ CẤP (TC) được tính bằng TỔNG của:"))
    b.append(ol([
        "Giá trị của TÍN HIỆU THEO HƯỚNG từ khối lead/lag, và (+);",
        "Giá trị ĐIỂM ĐẶT của bộ điều khiển thứ cấp (FC)."]))
    b.append(eq(
        "OP<sub>TC</sub>(khởi tạo) = FF<sub>lead/lag</sub> + SP<sub>FC</sub>", "11.3"))
    b.append(p(
        "Khi nhiệt độ dòng vào dao động và lưu lượng dòng vào thay đổi (các biến F1 và T1), và tuỳ theo "
        "chiều (lên hay xuống) của những thay đổi ấy, đầu ra của khối lead/lag sẽ thay đổi theo thuật "
        "toán hàm và các hằng số thời gian lead/lag cấu thành nên điều khiển theo hướng."))
    b.append(p(
        "Độ lớn và tốc độ thay đổi của tín hiệu này phải tương thích với mọi biến thiên của F1 và T1, sao "
        "cho chúng có ảnh hưởng tối thiểu hoặc không ảnh hưởng gì lên nhiệt độ đầu ra T2."))
    b.append(p(
        "Khối cộng phải được coi là một phần của khối đầu ra của bộ điều khiển sơ cấp (TC)."))
    b.append(fig(5, F.fig_11_5()))
    b.append(p(
        "Hình 11-5 cho thấy cái giá của việc khởi tạo sai. Khi TC chuyển từ MANUAL sang AUTO, đầu ra của "
        "nó phải đã bằng đúng giá trị mà hệ đang dùng. Nếu nó được nạp bằng tổng ở (11.3), việc chuyển "
        "chế độ không gây xáo trộn gì — đường xanh phẳng. Nếu nó được nạp bằng 0, bộ điều khiển bắt đầu "
        "từ một giá trị thấp hơn thực tế, quá trình nguội đi, và phải mất một quãng mới kéo lại được — "
        "đường đỏ. Trong một nhà máy thật, cú giật đó chính là một lô sản phẩm hỏng."))
    b.append(note(
        "Câu “khối cộng phải được coi là một phần của khối đầu ra của TC” là câu dễ bỏ qua nhất trong "
        "chương, và nó có hệ quả thực hành rõ ràng. Nếu bộ cộng nằm <em>ngoài</em> khối đầu ra, thì giới "
        "hạn của TC và giới hạn của bộ cộng là hai giới hạn khác nhau, và một trong hai có thể bão hoà "
        "trong khi cái kia vẫn tiếp tục tích luỹ. Đặt nó vào trong khối đầu ra thì chỉ còn một giới hạn, "
        "một phép chống windup, và một giá trị hiển thị đúng bằng giá trị thực sự tác động ra hiện "
        "trường."))

    b.append(h2("11.7 Các khía cạnh chỉnh định", "Tuning Aspects"))
    b.append(p(
        "Vì điều khiển phản hồi mạnh có xu hướng mất ổn định, nên tránh nó nếu có thể. Do đó, nếu điều "
        "khiển theo hướng đã làm phần lớn công việc điều khiển cần thiết và điều khiển phản hồi chỉ có "
        "mặt để xoá sự trôi của PV, thì làm như sau:"))
    b.append(ol([
        "Chỉnh định bộ điều khiển thứ cấp được dùng bởi cả điều khiển phản hồi lẫn điều khiển theo hướng;",
        "Chỉnh định điều khiển theo hướng;",
        "Chỉnh định điều khiển phản hồi bằng các công thức do Ziegler và Nichols xây dựng;",
        "Sau đó đánh giá tốc độ trôi của PV."]))
    b.append(p(
        "Nếu sự trôi của biến quá trình là không đáng kể, hãy giảm hệ số K của bộ điều khiển sơ cấp, dựa "
        "trên hiểu biết về quá trình và phán đoán cá nhân."))
    b.append(fig(6, F.fig_11_6()))
    b.append(p(
        "Cần nhớ rằng trong trường hợp này, điều khiển phản hồi chỉ là phần bổ sung cho điều khiển theo "
        "hướng, và <b>không được</b> đưa vào bất kỳ dạng dao động hay mất ổn định nào."))
    b.append(fig(7, F.fig_11_7()))
    b.append(p(
        "Hình 11-7 vẽ ba kết cục có thể có của cùng một lần chỉnh định. Đường đỏ là khi để khối theo "
        "hướng làm việc một mình: PV ổn định ở một mức thấp hơn điểm đặt và nằm lại đó. Đường vàng là khi "
        "phản hồi được đẩy quá mạnh: hệ dao động, và dù dao động có tắt dần thì nó vẫn là một hệ thống "
        "không nên đưa vào vận hành. Đường xanh là kết cục đúng: PV về điểm đặt êm, không vọt lố, nhờ "
        "phản hồi chỉ làm đúng phần việc của nó."))
    b.append(p(
        "Bước 4 trong danh sách trên — đánh giá tốc độ trôi — là bước hay bị bỏ nhất, vì nó không phải "
        "một thao tác mà là một quan sát. Nhưng nó chính là bước quyết định: nếu PV trôi chậm, nghĩa là "
        "khối theo hướng đang làm tốt phần lớn công việc và TC có thể yếu đi; nếu PV trôi nhanh, nghĩa "
        "là mô hình bù đang sai ở đâu đó và giảm K sẽ chỉ làm hỏng thêm. Giảm K là một phần thưởng cho "
        "một khối theo hướng tốt, không phải một cách chữa cho một khối theo hướng tồi."))

    b.append(h3("Bài tập 13 — Điều khiển kết hợp theo hướng và phản hồi",
                "Exercise 13 — Combined Feedforward and Feedback Control"))
    b.append(p(
        "Bài tập 13 sẽ đem lại kinh nghiệm thực hành về điều khiển kết hợp phản hồi và theo hướng."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Công thức ở mục 11.5 bị quét hỏng trong bản PDF gốc: "
        "dòng chữ đọc thành “equating as [ (T2 − T1) h F1 C and F =” — các ký hiệu bị đảo thứ tự và mất "
        "dấu. Công thức đúng là cân bằng nhiệt F<sub>1</sub>·C·(T<sub>2</sub> − T<sub>1</sub>) = F·h, "
        "với F<sub>1</sub> là lưu lượng khối dòng vào, C là nhiệt dung riêng, T<sub>2</sub> − "
        "T<sub>1</sub> là độ tăng nhiệt độ, F là lưu lượng nhiên liệu và h là nhiệt trị của nhiên liệu. "
        "Ngoài ra mục 11.2 nhắc tới “figure 10.3” của chương trước; ở bản dịch này hình đó đã được đánh "
        "số lại thành Hình 10-5."))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "The previous chapter ended with a verdict: feedforward alone always leaves a residue, because "
        "the compensating model is never perfect. This chapter is the answer to that residue. It "
        "introduces no third mechanism — it simply joins the two that already exist, and spends most of "
        "its short length on the details the joining creates: the summer, the initialisation, and the "
        "tuning order."))
    b.append(p(
        "It is the shortest control chapter in the book and the most practical. Everything in it is "
        "something to be done on a real system, on a commissioning morning."))

    b.append(h2("Disturbances come in two currencies", "§ 11.2"))
    b.append(p(
        "The chapter's list of what counts as a process disturbance is worth reading twice, because the "
        "second item is the one engineers forget. A disturbance is an unexpected change in the magnitude "
        "of a physical quantity — pressure, flow, temperature — or a change in the <em>time</em> of any "
        "of the process's responses."))
    b.append(fig(1, F.fig_11_1(), "en"))
    b.append(p(
        "Figure 11-1 puts the two side by side. On the left, the disturbance's magnitude changes and one "
        "curve shows it. On the right, the magnitude is identical in both curves but the process reacts "
        "with two different time constants — a heater that has just been cleaned versus one that has "
        "fouled, a line that is empty versus one that is full."))
    b.append(p(
        "The engineering consequence is the one the chapter states almost in passing: make the responses "
        "equal in magnitude <em>and</em> in time, and tuning becomes easier. That is not a slogan. A "
        "control loop has one set of tuning constants. If the process heats quickly and cools slowly, "
        "those constants can be optimal for one direction only; the other direction will be sluggish or "
        "unstable. Equalising the two directions is what makes a single set of constants meaningful, and "
        "the lead/lag block from the previous chapter is the tool that does it."))

    b.append(h2("The argument for combining", "§ 11.3"))
    b.append(p(
        "Feedback works best when disturbances and lag times are small — chapter 5 established that. "
        "Feedforward exists precisely to make them small. Put the two statements together and the "
        "conclusion is almost forced: an accurately configured feedforward block in front of a well-tuned "
        "feedback loop should approach optimal operation."))
    b.append(quote(
        "The two mechanisms do not compete; they divide the same problem. Feedforward handles the "
        "disturbance before it enters the loop, feedback handles everything that is left after it has.",
        "The thesis of section 11.3"))
    b.append(p(
        "One caution belongs with that optimism. Combining the two does not make a system easier to "
        "design — it makes it harder. A feedback-only loop has one set of constants to worry about. A "
        "combined system adds a model, a summer, and an initialisation state, and each of those can be "
        "wrong in its own way, independently of the others."))

    b.append(h2("The scheme, read in two halves", "§ 11.4"))
    b.append(fig(2, F.fig_11_2(), "en"))
    b.append(p(
        "Figure 11-2 is best read as two halves that meet at one point. The upper half is the feedforward "
        "chain: FT measures the inlet flow, a calculation converts it into a heat demand, lead/lag "
        "matches its timing, and the result enters the summer. The lower half is the feedback loop: TT "
        "measures the outlet temperature, the TC compares it with its set point, and its correction "
        "enters the same summer. The two halves meet at exactly one place, and that place is the system's "
        "only manipulated variable — the fuel flow."))
    b.append(p(
        "Chapters 9 and 10 covered most of what those two halves need. What is left is the junction, and "
        "the chapter is right to spend its remaining space there."))

    b.append(h2("One valve, two masters", "§ 11.5"))
    b.append(p(
        "The chapter sets up the problem honestly: there is one manipulated variable and two control "
        "concepts that both want it. The mass-flow feedforward, from the heat balance, and the cascaded "
        "feedback would appear to compete."))
    b.append(eq(
        "F<sub>1</sub>·C·(T<sub>2</sub> − T<sub>1</sub>) = F·h", "11.1"))
    b.append(p(
        "They do not compete, and the reason is a structural one rather than a tuning one. The "
        "feedforward output goes to the <em>set point</em> of the fuel flow controller, not to the valve. "
        "The primary controller's output is <em>added</em> to that set point. One supplies a baseline, "
        "the other supplies a correction, and the fuel flow loop sees a single number."))
    b.append(fig(3, F.fig_11_3(), "en"))
    b.append(p(
        "The sentence that matters most in the whole chapter is the one that follows: these are "
        "incremental and not absolute calculations. It is worth spelling out why. If both controllers "
        "computed an absolute valve position between 0 and 100 per cent, they would be writing to the "
        "same variable, and the result would depend on which task ran last — behaviour that cannot be "
        "reasoned about, tested, or trusted. With a baseline and an increment, the sum is deterministic "
        "and each contributor can be checked on its own."))
    b.append(eq(
        "F = F<sub>1</sub>·C·(T<sub>2</sub> − T<sub>1</sub>) / h", "11.2"))
    b.append(fig(4, F.fig_11_4(), "en"))
    b.append(p(
        "Figure 11-4 shows what the heat balance costs in range. Fuel demand is linear in inlet flow and "
        "linear in temperature rise, so the feedforward block is only two multiplications — and it has a "
        "hard ceiling. At a 60 °C rise the valve is fully open at 67 per cent of design flow. Beyond that "
        "point the block has nothing left to give and the feedback loop carries the whole burden, which "
        "is exactly the situation a designer needs to know about before commissioning rather than after."))

    b.append(h2("Initialisation: the value nobody sets", "§ 11.6"))
    b.append(p(
        "The initialisation rule is one line long: the primary controller's output is pre-loaded with the "
        "sum of the lead/lag signal and the secondary controller's set point."))
    b.append(eq(
        "OP<sub>TC</sub>(init) = FF<sub>lead/lag</sub> + SP<sub>FC</sub>", "11.3"))
    b.append(fig(5, F.fig_11_5(), "en"))
    b.append(p(
        "Figure 11-5 shows the cost of getting it wrong. With the correct pre-load, the switch from "
        "manual to automatic changes nothing — the blue trace is flat. Loaded with zero instead, the "
        "controller starts from a value well below what the plant is actually using, the process cools, "
        "and the integral has to earn back the difference — the red trace. On a real plant that dip is a "
        "batch of off-specification product."))
    b.append(p(
        "The chapter's last sentence on the subject — that the summing block should be considered part of "
        "the primary controller's output block — is the one most often skipped, and it has a concrete "
        "consequence. If the summer sits outside the output block, the TC and the summer have separate "
        "limits, and one can saturate while the other keeps accumulating. Put it inside, and there is one "
        "limit, one anti-windup mechanism, and one displayed value that equals what actually reaches the "
        "field."))

    b.append(h2("Tuning order, and the reward for a good model", "§ 11.7"))
    b.append(p(
        "The prescribed order is four steps: secondary controller, then the feedforward block, then the "
        "primary by Ziegler–Nichols, then an assessment of how fast the PV drifts. The order is not "
        "arbitrary — the secondary has to be fast and stable before the feedforward block can be judged, "
        "and the feedforward block has to be right before the primary's tuning means anything."))
    b.append(fig(6, F.fig_11_6(), "en"))
    b.append(p(
        "The fourth step is the one people skip, because it is an observation rather than an action. It "
        "is also the decisive one. Slow drift means the feedforward block is doing most of the work and "
        "the primary can safely be weakened. Fast drift means the model is wrong somewhere, and reducing "
        "K will only make it worse. Reducing K is a reward for a good feedforward block, not a cure for a "
        "bad one."))
    b.append(fig(7, F.fig_11_7(), "en"))
    b.append(p(
        "Figure 11-7 draws the three outcomes of one tuning session. Red is feedforward alone: the PV "
        "settles below set point and stays there. Gold is feedback pushed too hard: the loop oscillates, "
        "and a decaying oscillation is still a loop nobody should run. Blue is the intended result — the "
        "PV returns to set point smoothly, with no overshoot, because feedback is doing only its own "
        "share of the work."))
    return "".join(b)
