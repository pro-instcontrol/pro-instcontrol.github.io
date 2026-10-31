# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 9, Output Modes, Equations, Cascade Control
(Wolfgang Altmann, IDC Technologies)."""
import pc9fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 21
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Đầu ra ảo (virtual output)</em> — giá trị bộ điều khiển tính ra, không bị chặn bởi "
            "giới hạn. · "
            "<em>Bão hoà (saturation)</em> — đầu ra ảo vượt giới hạn nhưng đầu ra thật thì không. · "
            "<em>Khởi tạo (initialization)</em> — chế độ mà vòng thứ cấp gửi điểm đặt của nó ngược lên "
            "đầu ra của vòng sơ cấp. · "
            "<em>Bám PV (PV-tracking)</em> — ở MANUAL, điểm đặt được gán bằng PV để sai lệch bằng không. · "
            "<em>Phương trình loại A / B / C</em> — ba cách chia PV và SP cho các khâu P, I, D. · "
            "<em>Ultimate primary</em> — bộ điều khiển trên cùng của một chuỗi cascade.")
    return note(
        "<b>Key terms.</b> <em>Virtual output</em> — the value the controller computes, before the "
        "limit. · <em>Saturation</em> — the virtual output passes the limit while the real output does "
        "not. · <em>Initialization</em> — the mode in which the secondary sends its set point back up to "
        "the primary's output. · <em>PV-tracking</em> — in MANUAL the set point is forced to the PV so "
        "the error is zero. · <em>Equation type A / B / C</em> — three ways of sharing PV and SP between "
        "the P, I and D blocks. · <em>Ultimate primary</em> — the top controller of a cascade chain.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương này là bản lề của cả cuốn sách. Trước nó, mọi bộ điều khiển đều là một hộp đen có hai "
        "đầu vào và một đầu ra. Sau nó, bộ điều khiển có thêm ba thứ: một khối đầu ra có chế độ, một "
        "giới hạn có thể bão hoà hoặc không, và một tập phương trình quyết định PV và SP được chia cho "
        "các khâu P, I, D như thế nào."))
    b.append(p(
        "Ba thứ đó nghe như chi tiết kỹ thuật. Nhưng chúng chính là điều kiện để ghép hai bộ điều khiển "
        "lại thành một hệ cascade — và cascade là kỹ thuật can thiệp có lợi nhất trên một vòng điều "
        "khiển thông thường."))

    b.append(h2("9.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Trình bày được hiểu biết rõ ràng về bộ điều khiển có nhiều đầu ra độc lập;",
        "Phân biệt rõ giữa giới hạn đầu ra có bão hoà và không bão hoà;",
        "Mô tả được khái niệm và chiến lược điều khiển cascade;",
        "Chọn và áp dụng đúng các tuỳ chọn của bộ điều khiển: khởi tạo, bám PV và loại phương trình "
        "điều khiển;",
        "Mô tả được khái niệm cascade với nhiều vòng thứ cấp;",
        "Trình bày được cách chỉnh định toàn bộ các bộ điều khiển trong một hệ cascade."]))

    b.append(h2("9.2 Đầu ra của bộ điều khiển", "Controller Output"))
    b.append(p(
        "Để có thể ghép các bộ điều khiển thành cascade, một số yêu cầu về thiết kế hệ phải được đáp "
        "ứng. Yêu cầu quan trọng nhất xoay quanh phần đầu ra của bộ điều khiển, đặc biệt là bộ điều "
        "khiển SƠ CẤP."))
    b.append(p(
        "Hình 9-1 cho thấy một khối đầu ra điển hình của bộ điều khiển PID, cùng các tín hiệu điều khiển "
        "và tác động của chúng lên giá trị đầu ra cuối cùng. Chức năng của từng phần sẽ được bàn trong "
        "chương này."))
    b.append(fig(1, F.fig_9_1()))

    b.append(h3("9.2.1 Đầu ra của bộ điều khiển đơn lẻ", "Single or Stand-Alone Controller Output"))
    b.append(p("Giá trị đầu ra cuối cùng của một bộ điều khiển đơn lẻ chịu tác động của một trong hai tín hiệu:"))
    b.append(ul([
        "Tín hiệu thứ nhất đến từ chế độ MANUAL, trong đó một giá trị đặt hay giá trị tĩnh có thể được "
        "đưa vào đầu ra bằng tay; giá trị này được coi là “điểm không sống” (live zero). Bản thân bộ "
        "điều khiển không biết giá trị đó là bao nhiêu, và nó có thể nằm bất kỳ đâu trong dải 0 đến "
        "100 % của đầu ra.",
        "Tín hiệu thứ hai là khi bộ điều khiển ở chế độ AUTO và các tác động PID bắt đầu tăng hay giảm "
        "giá trị MANUAL đó ở mỗi chu kỳ quét của hệ."]))

    b.append(h2("9.3 Nhiều đầu ra của bộ điều khiển", "Multiple Controller Outputs"))
    b.append(p(
        "Xem kỹ Hình 9-1 sẽ thấy bộ điều khiển này có thể có hai hay nhiều khối đầu ra, hoàn toàn giống "
        "nhau nhưng cách ly hoàn toàn với nhau."))
    b.append(p(
        "Nếu xét một bộ điều khiển có hai (hay nhiều) khối đầu ra, cho ra các tín hiệu OP1, OP2 đến OPN, "
        "thì tồn tại rất nhiều hoán vị tác động mà cấu hình này có thể thực hiện; những hoán vị quan "
        "trọng nhất được liệt kê dưới đây."))

    b.append(h3("9.3.1 Các cấu hình nhiều đầu ra", "Multiple Controller Output Configurations"))
    b.append(p(
        "Vì mỗi khối đầu ra độc lập với tất cả các khối khác gắn vào cùng bộ điều khiển, giá trị tuyệt "
        "đối của chúng có thể — và thường là — khác nhau. Mặc dù tác động của bộ điều khiển PID liên tục "
        "phản ứng với các giá trị SP và PV ở đầu vào, kết quả của phép tính PID chỉ tác động "
        "(+ / 0 / −) lên một đầu ra cụ thể nếu chế độ của đầu ra đó được đặt là auto hay cascade."))
    b.append(p("Hình 9-2 minh hoạ chiến lược điều khiển đầu ra của một bộ điều khiển đơn hoặc nhiều đầu ra."))
    b.append(fig(2, F.fig_9_2()))
    b.append(p(
        "Giả sử ban đầu OP1 được đặt ở chế độ manual hay initialize và đầu ra của nó được ghép cascade "
        "hay nối tới đầu ra của một bộ điều khiển khác; còn OP2 ở chế độ auto. OP2 sẽ đáp ứng các yêu "
        "cầu thay đổi của PID, nhưng OP1 sẽ đứng yên ở giá trị manual hay giá trị khởi tạo của nó. Chỉ "
        "khi OP1 được đặt sang AUTO hoặc CASCADE — bằng cách thay đổi tín hiệu điều khiển MANUAL hay "
        "INITIALISE — thì OP1 mới bắt đầu đáp ứng các lệnh của PID."))
    b.append(p(
        "Khi đó giá trị OP1 sẽ “bám” giá trị của OP2, mặc dù hai giá trị tuyệt đối có thể rất khác nhau. "
        "Nếu kết quả cộng của PID nói “tăng” một lượng P_N trong một chu kỳ quét, thì OP1 sẽ tăng từ "
        "OP1_N lên OP1_N + P_N và OP2 sẽ tăng từ OP2_N lên OP2_N + P_N. Nghĩa là cả hai đầu ra thay đổi "
        "cùng một độ lớn, nhưng giữ nguyên hiệu số giữa chúng."))

    b.append(h3("9.3.2 Giới hạn của các đầu ra", "Limits of Controller Outputs"))
    b.append(p(
        "Bản thân bộ điều khiển không biết giá trị tuyệt đối cuối cùng ở các khối đầu ra của nó. Hệ quả "
        "là các đầu ra này có thể bị đẩy tới bão hoà ở 0 % hoặc 100 % trong khi bộ điều khiển vẫn tiếp "
        "tục “đẩy” chúng xuống dưới không hoặc lên trên toàn thang."))
    b.append(p(
        "Vì ta có thể không biết hoặc không nhận ra điều đó đang xảy ra, cũng như không biết bằng cách "
        "nào, khi nào và với độ chính xác bao nhiêu các đầu ra quay trở lại dải làm việc, ta phải có khả "
        "năng “chọn” yêu cầu của mình về kiểu tính giới hạn đầu ra cần dùng và lý do."))

    b.append(h2("9.4 Bão hoà và không bão hoà của giới hạn đầu ra",
                "Saturation and Non-Saturation of Output Limits"))
    b.append(p(
        "Có hai kiểu tính giới hạn đầu ra chính. Kiểu thứ nhất, có giới hạn đầu ra, cho phép đầu ra bão "
        "hoà dựa trên điều khiển P và D. Kiểu thứ hai không cho phép bão hoà đầu ra xảy ra trong bất kỳ "
        "trường hợp nào."))

    b.append(h3("9.4.1 Bão hoà của đầu ra", "Saturation of the Output"))
    b.append(p("Nếu đầu ra của bộ điều khiển được phép bão hoà, nó cho phép theo cách sau:"))
    b.append(ol([
        "Bộ điều khiển tính một giá trị đầu ra ẢO, độc lập với mọi giới hạn đầu ra. Giá trị này có thể "
        "cao hơn 100 % hoặc thấp hơn 0 % rất nhiều.",
        "Chỉ đầu ra thật — tức giá trị đầu ra được hiển thị — bị giới hạn bởi các giới hạn đầu ra đã "
        "định trước.",
        "Sau đó đầu ra thật chờ cho đầu ra ảo quay trở lại trong các giới hạn đã định.",
        "Khi đã trong dải giới hạn, đầu ra thật bám chính xác theo giá trị đầu ra ảo.",
        "Các bộ điều khiển lái đầu ra ra hiện trường thường dùng kiểu xử lý giới hạn này."]))

    b.append(h3("9.4.2 Tính giới hạn không bão hoà", "Non Saturation Output-Limit-Calculation"))
    b.append(p(
        "Không bão hoà đầu ra đạt được bằng cách bảo đảm chỉ dùng các giá trị đầu ra thật trong phép "
        "tính. Nếu một phép tính cho ra giá trị đầu ra vượt quá giới hạn đã đặt, giá trị đầu ra sẽ được "
        "gán bằng chính giá trị giới hạn mà nó đã vi phạm. Lần sau, khi bộ điều khiển tính giá trị đầu "
        "ra (ở chu kỳ quét kế tiếp), nó dùng giá trị đầu ra THẬT (đầu ra = giới hạn). Phép tính trước đó "
        "— phép tính vượt giới hạn — đã bị quên hoàn toàn."))
    b.append(p(
        "Hình 9-7 cho thấy khác biệt này bằng số. Cùng một nhiễu dương kéo dài, rồi đảo chiều. Bộ điều "
        "khiển bão hoà vẫn giữ đầu ra thật ở 100 % rất lâu sau khi nhiễu đã đảo chiều, vì đầu ra ảo của "
        "nó đã tích luỹ một lượng dư và phải tiêu hết lượng dư đó trước khi đầu ra thật bắt đầu giảm. "
        "Bộ điều khiển không bão hoà quay đầu ngay lập tức. Hiện tượng thứ nhất chính là windup — và nó "
        "là lý do tồn tại của chống windup trong mọi bộ điều khiển công nghiệp hiện đại."))
    b.append(fig(7, F.fig_9_7()))

    b.append(h3("Bài tập 9 — Bão hoà và không bão hoà của giới hạn đầu ra",
                "Exercise 9 — Saturation and Non Saturation of Output Limits"))
    b.append(p("Minh hoạ mục 9.4."))

    b.append(h2("9.5 Điều khiển cascade", "Cascade Control"))
    b.append(p(
        "Lấy ví dụ về bộ gia nhiệt dòng liệu (feedheater) của ta: nếu thêm một vòng điều khiển nữa chỉ "
        "để điều khiển lưu lượng nhiên liệu, ta sẽ giữ được lưu lượng nhiên liệu không đổi bất chấp thay "
        "đổi áp suất nhiên liệu."))
    b.append(p(
        "Nếu đầu ra (OP) của bộ điều khiển nhiệt độ TC lái điểm đặt (SP) của bộ điều khiển lưu lượng "
        "nhiên liệu FC mới thêm này, thì ta có tình huống là OP của TC điều khiển lưu lượng thật chứ "
        "không chỉ điều khiển vị trí van. Áp suất nhiên liệu trên thực tế sẽ không còn ảnh hưởng gì tới "
        "nhiệt độ đầu ra nữa. Khái niệm này được gọi là ĐIỀU KHIỂN CASCADE."))
    b.append(fig(3, F.fig_9_3()))
    b.append(p(
        "Hình 9-3 là trường hợp tham chiếu: một vòng, một bộ điều khiển, và mọi nhiễu áp suất nhiên liệu "
        "đi thẳng vào nhiệt độ đầu ra. Hình 9-4 là cùng quá trình đó sau khi thêm vòng lưu lượng."))
    b.append(fig(4, F.fig_9_4()))

    b.append(h3("9.5.1 Thuật ngữ trong cascade", "Cascade Control Terms"))
    b.append(p("Để giúp nhận diện bộ điều khiển nào là bộ nào trong một hệ cascade, dùng các thuật ngữ sau:"))
    b.append(ul([
        "Bộ điều khiển có SP do OP của một bộ điều khiển khác lái được gọi là “bộ điều khiển hạ lưu” "
        "(Down Stream Controller, Slave), hoặc thường được gọi là “bộ điều khiển thứ cấp” (Secondary "
        "Controller).",
        "Bộ điều khiển có OP lái SP của một bộ điều khiển thứ cấp được gọi là “bộ điều khiển thượng "
        "lưu” (Up Stream Controller) hay “bộ điều khiển sơ cấp” (Primary Controller, Master)."]))
    b.append(p("<b>Cấu hình cascade nhiều tầng.</b> Nếu hệ cascade có nhiều hơn hai bộ điều khiển:"))
    b.append(ul([
        "Bộ điều khiển ở vị trí thượng lưu cao nhất được gọi là sơ cấp tối hậu (Ultimate Primary).",
        "Bộ điều khiển ở vị trí hạ lưu thấp nhất được gọi là bộ điều khiển thứ cấp tối hậu (Ultimate "
        "Secondary Controller)."]))
    b.append(p(
        "Nếu xem xét các yêu cầu cần thiết để khởi động một hệ điều khiển cascade cho bộ gia nhiệt dòng "
        "liệu bằng tay, ta sẽ hiểu được nguyên lý vận hành của nó. Điều đó, đến lượt mình, cho ta nền "
        "tảng cần thiết để hiểu bám PV, khởi tạo và các loại phương trình khác nhau dùng trong thuật "
        "toán điều khiển liên quan."))

    b.append(h3("9.5.2 Khái niệm bám biến quá trình (PV-Tracking)",
                "The Concept of Process Variable or PV-Tracking"))
    b.append(p(
        "Bám PV hoạt động khi bộ điều khiển thứ cấp (FC) ở CHẾ ĐỘ MANUAL. Bộ điều khiển có thể được cấu "
        "hình để dùng hoặc không dùng bám PV; đó là lựa chọn của người thiết kế hệ."))
    b.append(p(
        "Khái niệm là: người vận hành đặt giá trị OP của bộ điều khiển nhiên liệu bằng tay cho tới khi "
        "tìm được giá trị thích hợp cho quá trình. Ta giả định giá trị đầu ra đó là giá trị tối ưu cho "
        "quá trình, nghĩa là ta đã đặt lưu lượng nhiên liệu ở một giá trị bằng tay đúng để giữ nhiệt độ "
        "đầu ra T2 ở giá trị yêu cầu."))
    b.append(p(
        "Điều này dẫn tới kết luận rằng ở thời điểm đó không cần hiệu chỉnh gì giá trị OP. Vì không thay "
        "đổi OP chính là yêu cầu lý tưởng, nên không được có sai lệch (ERR). Để đạt điều đó, phải giữ "
        "SP bằng PV bằng cách để người vận hành thao tác giá trị OP bằng tay."))
    b.append(p("Do đó, với bám PV chỉ trong chế độ MANUAL: <b>SP = PV</b>. Đây chính là bám PV."))
    b.append(p(
        "Ngay khi chuyển chế độ sang AUTOMATIC, SP giữ nguyên giá trị cuối cùng và trở thành giá trị "
        "tham chiếu đã được tạo ra trước đó bằng thao tác tay lên OP (khi còn ở chế độ MANUAL)."))
    b.append(p(
        "Đầu ra của bộ điều khiển lưu lượng (FC) có một giá trị TUYỆT ĐỐI do người vận hành đặt tại thời "
        "điểm chuyển từ Manual sang Automatic, đủ để giữ van nhiên liệu ở vị trí yêu cầu."))

    b.append(h2("9.6 Khởi tạo một hệ cascade", "Initialization of a Cascade System"))
    b.append(p(
        "Khởi tạo thực chất là một kiểu chế độ manual, trong đó người vận hành không lái giá trị OP của "
        "bộ điều khiển sơ cấp (trong trường hợp này là TC). Thay vào đó, bộ điều khiển nhiên liệu FC "
        "gửi giá trị điểm đặt (SP) của nó ngược lên chuỗi cascade, tới đầu ra của bộ điều khiển sẽ lái "
        "nó (tức SP của FC) khi hệ ở chế độ automatic. Nếu được chọn, bám PV có thể diễn ra ở bộ điều "
        "khiển sơ cấp giống như trong chế độ manual bình thường."))

    b.append(h3("9.6.1 Các bước khởi tạo", "Steps of Initialization"))
    b.append(p("Hãy phân tích tính hữu ích của khởi tạo qua ví dụ bộ gia nhiệt dòng liệu (Hình 9-4)."))
    b.append(ul([
        "Nếu bộ điều khiển lưu lượng nhiên liệu FC ở chế độ manual và giá trị OP của nó được người vận "
        "hành lái cho tới khi đạt nhiệt độ đầu ra T2 mong muốn, thì PV của FC đang có giá trị đúng để "
        "đạt T2 mong muốn. (Ở điểm này, trong vòng đó tồn tại điều kiện vòng hở.)",
        "Nhờ bám PV của bộ điều khiển lưu lượng, giá trị điểm đặt của nó — do người vận hành thao tác — "
        "đang ở giá trị cần thiết để cho đầu ra FC giá trị đúng nhằm duy trì T2 bằng cách thiết lập lưu "
        "lượng đúng.",
        "Giá trị SP của FC đang có đúng giá trị mà đầu ra của bộ điều khiển nhiệt độ TC sẽ yêu cầu ở nó.",
        "Bộ điều khiển lưu lượng, khi ở chế độ manual, gửi ngược giá trị SP của nó về khối đầu ra của "
        "TC. TC cho phép nạp giá trị đó vào khối đầu ra của mình khi nhận được tín hiệu từ FC rằng FC "
        "đang ở cả “chế độ Cascade và Manual”. (Nhận lệnh này theo cách tương tự như chính nó bị đặt ở "
        "chế độ manual.)",
        "Đây được gọi là khởi tạo. Nếu bộ điều khiển sơ cấp TC thực hiện bám PV, thì SP nhiệt độ bám "
        "theo giá trị nhiệt độ thật, tức PV của bộ điều khiển sơ cấp.",
        "Khi người vận hành đã tìm được giá trị OP đúng của FC, mặc định ta đã có giá trị SP đúng cho "
        "lưu lượng: SP = PV.",
        "Nếu đã khớp SP này với giá trị OP của bộ điều khiển sơ cấp, thì ta cũng có SP đúng cho nhiệt độ.",
        "Tất cả việc còn lại là đặt bộ điều khiển thứ cấp sang CHẾ ĐỘ CASCADE; khối đầu ra của bộ điều "
        "khiển sơ cấp liên quan sẽ tự động chuyển sang CHẾ ĐỘ AUTO.",
        "Như vậy ta đã đạt được một chuyển đổi êm (bumpless) từ điều khiển bằng tay sang điều khiển tự "
        "động."]))
    b.append(p(
        "Điểm mấu chốt của toàn bộ thủ tục là ở bước 4: khởi tạo không phải là một phép tính, nó là một "
        "đường dẫn tín hiệu. Giá trị SP của FC đi ngược lên và trở thành giá trị OP của TC. Khi TC "
        "chuyển sang AUTO, đầu ra của nó đã đúng bằng giá trị mà FC đang chờ, nên không có cú nhảy nào. "
        "Nếu thiếu đường dẫn đó, TC sẽ vào AUTO với giá trị OP cũ của nó — có thể là 0 % hoặc 100 % — và "
        "van nhiên liệu sẽ đập một cú."))

    b.append(h2("9.7 Các phương trình liên quan tới cấu hình bộ điều khiển",
                "Equations relating to Controller Configurations"))
    b.append(p(
        "Trong điều khiển cascade, đầu ra của bộ điều khiển này lái điểm đặt của bộ điều khiển thứ cấp, "
        "và về bản chất tất cả các bộ điều khiển đó đều gồm — hoặc có khả năng — tính độc lập các thuật "
        "toán P, I và D dựa trên giá trị sai lệch rút ra từ hai đầu vào: giá trị điểm đặt (SP) và biến "
        "quá trình (PV). Có những trường hợp chỉ cần một số chức năng nhất định trong chuỗi cascade, và "
        "khi đó cần “sắp xếp lại” cách các hàm P, I, D được lái từ các biến PV và SP."))
    b.append(p(
        "Có ba cách làm việc này, được gọi là phương trình bộ điều khiển loại A, B hoặc C. Loại A và "
        "loại C là hai loại được dùng phổ biến hơn cả và có liên hệ với nhau, nên được xét cùng nhau. "
        "Hình 9-5 minh hoạ cách nối dây của một bộ điều khiển, qua đó xác định loại phương trình mà nó "
        "thể hiện."))

    b.append(h3("9.7.1 Phương trình loại A", "Equation Type A"))
    b.append(p("Trong phương trình loại A, mọi điều khiển đều dựa trên số hạng sai lệch (ERR)."))
    b.append(p(
        "Bộ điều khiển dùng phương trình loại A không phân biệt giữa một nhiễu ở đầu vào PV và một thao "
        "tác của người vận hành lên SP. Đây là cách tiêu chuẩn để tính các tác động điều khiển của một "
        "bộ điều khiển PID, và cũng là cách ta đã xét mọi bộ điều khiển trong cuốn sách này từ đầu."))
    b.append(p(
        "Ở những nơi thay đổi PV khá êm, với ít hoặc không có bước nhảy, chúng sẽ không gây ra thay đổi "
        "đột ngột hay mạnh ở đầu ra bộ điều khiển. Thêm nữa, SP của bộ điều khiển thường không bao giờ "
        "hoặc rất ít khi bị dịch chuyển, nên cũng không gây thay đổi nhanh ở đầu ra; ngược lại, người "
        "vận hành có thể lái một van qua toàn bộ dải của nó chỉ bằng một bước thay đổi lớn ở SP. Trong "
        "những tình huống như vậy, có thể coi người vận hành là nhiễu nguy hiểm nhất trong hệ."))
    b.append(p(
        "Do đó, khi cần một chuyển đổi êm — kể cả khi người vận hành thay đổi SP mạnh — ta phải “sắp xếp "
        "lại” cấu trúc của bộ điều khiển để đạt yêu cầu đó. Điều này dẫn tới phương trình loại C."))
    b.append(fig(5, F.fig_9_5()))

    b.append(h3("9.7.2 Phương trình loại C", "Equation Type C"))
    b.append(p(
        "Phương trình loại C cấu hình bộ điều khiển sao cho có thể loại bỏ vấn đề bước nhảy ở đầu ra do "
        "người vận hành thay đổi điểm đặt lớn và nhanh. Phải nhớ rằng trong hầu hết hệ thống, SP của bộ "
        "điều khiển sơ cấp ít khi bị thay đổi nhiều, cả về độ lớn lẫn về số lần. Tuy nhiên khi SP THẬT "
        "SỰ bị thay đổi, cần bảo đảm thay đổi đầu ra thu được càng mềm và càng êm càng tốt, đặc biệt khi "
        "nó đang lái SP của các bộ điều khiển thứ cấp. Một cách hay để làm việc này là tích phân bước "
        "thay đổi:"))
    b.append(eq("bước nhảy SP  ×  1/s  ×  1/s  =  đầu ra dạng dốc", "9.1"))
    b.append(p("Xem Hình 9-6, phương trình C khác phương trình loại A thông thường ở chỗ:"))
    b.append(ul([
        "Các hàm tỉ lệ và vi phân làm việc, qua khối hệ số K_C, trực tiếp từ PV chứ KHÔNG từ số hạng ERR.",
        "Số hạng ERR được dùng riêng cho hàm tích phân, và cũng được rút ra từ PV − SP hoặc SP − PV."]))
    b.append(p(
        "Điều đó có nghĩa là một bước thay đổi ở SP trở thành một đầu ra được tích phân (dạng dốc) từ bộ "
        "điều khiển."))
    b.append(p(
        "Kiểu tính điều khiển này cho ra tác động PID hoàn toàn giống phương trình loại A nếu điểm đặt "
        "là hằng số. Nó giữ nguyên hành vi điều khiển trước các nhiễu thật và giữ nguyên hành vi của "
        "vòng. SP là biến duy nhất được xử lý khác."))
    b.append(fig(6, F.fig_9_6()))

    b.append(h4("Phương trình C và điều khiển P"))
    b.append(p("Khi SP = hằng số — khác biệt là gì?"))
    b.append(eq("∆OP = K · ∆(PV − SP)   [loại A]", "9.2"))
    b.append(eq("∆OP = K · ∆PV           [loại C]", "9.3"))
    b.append(p("Trả lời: không khác biệt, miễn là SP = hằng số."))
    b.append(note(
        "<b>Ghi chú.</b> Thay đổi của ERR, với ERR = ∆(PV − SP), đồng nhất với số hạng ∆PV (thay đổi của "
        "PV). · Tác động P dựa trên PV là như nhau, nhưng SP bị bỏ qua hoàn toàn. · SP thậm chí không "
        "còn là một phần của công thức nữa. · Người vận hành có thể làm gì tuỳ ý với SP, nhưng điều đó "
        "không ảnh hưởng gì tới điều khiển P nếu phương trình loại C đang hoạt động."))

    b.append(h4("Phương trình C và điều khiển I"))
    b.append(p("Sự tồn tại của điều khiển tích phân chính là lý do các phương trình bộ điều khiển này tồn tại, bởi vì:"))
    b.append(ul([
        "Không có khác biệt nào trong điều khiển I giữa các loại phương trình.",
        "Điều khiển I luôn sẵn có cho người vận hành để thực hiện những thay đổi điều khiển êm và không "
        "cú nhảy từ điểm đặt này sang điểm đặt khác.",
        "Điều khiển I sẽ không bao giờ gây ra cú nhảy nào nếu xảy ra thay đổi SP.",
        "Vì SP là ảnh hưởng từ bên ngoài đối với vòng, tích phân trên SP không ảnh hưởng tới tính ổn "
        "định của vòng."]))

    b.append(h4("Phương trình C và điều khiển D"))
    b.append(p("Khi SP = hằng số — khác biệt là gì?"))
    b.append(eq("∆OP = K · T_der · ∆(∆(PV − SP))   [loại A]", "9.4"))
    b.append(eq("∆OP = K · T_der · ∆(∆PV)           [loại C]", "9.5"))
    b.append(p("Trả lời: không khác biệt, miễn là SP = hằng số."))
    b.append(note(
        "<b>Ghi chú.</b> ∆(∆(SP − PV)) đồng nhất với ∆(∆PV) nếu không có thay đổi SP. · Tác động D dựa "
        "trên PV là như nhau, nhưng SP bị bỏ qua hoàn toàn. · Người vận hành có thể làm gì tuỳ ý với SP "
        "vì không ảnh hưởng tới điều khiển D khi phương trình loại C đang hoạt động. · Đây là một ví dụ "
        "nữa về công dụng và lợi ích của thuật toán số gia."))

    b.append(h2("9.8 Ghi chú ứng dụng về việc dùng các loại phương trình",
                "Application Notes on the Use of Equation Types"))
    b.append(p(
        "Phải đánh giá cẩn thận quá trình và chiến lược quá trình trước khi quyết định chọn một loại "
        "phương trình cụ thể. Theo nguyên tắc chung, có thể dùng các loại như sau."))

    b.append(h3("9.8.1 Ứng dụng phương trình loại A", "Application of Equation Type A"))
    b.append(p(
        "Đây là phép tính đa dụng, dùng khi không có lý do đặc biệt nào để dùng loại khác."))
    b.append(note(
        "<b>Ghi chú quan trọng.</b> Phương trình loại A là bắt buộc đối với bộ điều khiển thứ cấp. Nếu "
        "dùng loại C trong một bộ điều khiển thứ cấp, thì điều khiển I sẽ là tác động duy nhất giữa OP "
        "của bộ điều khiển sơ cấp và OP của bộ điều khiển thứ cấp. Điều đó sẽ thêm một độ trễ pha không "
        "cần thiết 90° cho vòng của bộ điều khiển sơ cấp. Kết quả có thể là làm mất ổn định không cần "
        "thiết vòng sơ cấp của một hệ cascade."))

    b.append(h3("9.8.2 Ứng dụng phương trình loại B", "Application of Equation Type B"))
    b.append(p(
        "Các xem xét nguyên tắc về cách thuật toán điều khiển có thể chỉ làm việc trên PV giống như đã "
        "trình bày cho phương trình loại C. Phương trình loại B làm việc như một bộ điều khiển PI trên "
        "sai lệch (ERR = PV − SP) và như một bộ điều khiển D chỉ trên PV."))
    b.append(p(
        "Vì loại B nằm giữa loại A và loại C, việc quyết định dùng loại B là tuỳ ý người sử dụng. Ví "
        "dụ, nếu một bộ điều khiển thứ cấp cần điều khiển D để ổn định vòng thứ cấp, và OP của bộ điều "
        "khiển sơ cấp đã chứa đủ mọi tác động điều khiển cần cho vòng sơ cấp (kể cả điều khiển D), thì "
        "bộ điều khiển thứ cấp có thể dùng loại B là tốt nhất. Trong trường hợp đó, toàn bộ tác động "
        "điều khiển của bộ điều khiển sơ cấp được truyền sang OP của bộ điều khiển thứ cấp thông qua "
        "việc điều khiển bộ điều khiển thứ cấp."))

    b.append(h3("9.8.3 Ứng dụng phương trình loại C", "Application of Equation Type C"))
    b.append(p(
        "Phương trình loại C làm việc như một bộ điều khiển I trên sai lệch (ERR = PV − SP) và như một "
        "bộ điều khiển PD chỉ trên PV. Nó chủ yếu được dùng làm bộ điều khiển sơ cấp tối hậu."))
    b.append(p(
        "Người vận hành không thể gây ra những tác động điều khiển đột ngột dẫn tới các vị trí cực đoan "
        "đột ngột của van và các thiết bị điều khiển khác. Điều này chỉ được đánh giá đầy đủ khi người "
        "ta đã nghe tiếng động do một van lớn đập đột ngột vào vị trí cực đoan. Có thể cảm nhận nó gần "
        "như trong toàn nhà máy như một tiếng nổ lớn. Đó tuyệt đối không phải là cách tốt để kéo dài "
        "tuổi thọ của van."))

    b.append(p("Bảng dưới đây so sánh ba loại phương trình theo cách tính sai lệch cho từng khâu:"))
    b.append(table(
        ["Loại", "Khâu P", "Khâu I", "Khâu D", "Ghi chú sử dụng"],
        [["A", "PV − SP hoặc SP − PV", "PV − SP hoặc SP − PV", "PV − SP hoặc SP − PV",
          "Bộ điều khiển tiêu chuẩn"],
         ["B", "PV − SP hoặc SP − PV", "PV − SP hoặc SP − PV", "PV", "Dùng đặc biệt"],
         ["C", "PV", "PV − SP hoặc SP − PV", "PV", "Bộ điều khiển sơ cấp"]],
        "Bảng 9-1 (bảng 9.1 trong bản gốc). So sánh ba loại phương trình theo cách tính sai lệch."))

    b.append(h2("9.9 Chỉnh định một vòng điều khiển cascade", "Tuning of a Cascade Control Loop"))
    b.append(p("Cách tiếp cận khá đơn giản."))
    b.append(p(
        "Trước tiên, chỉnh định bộ điều khiển thứ cấp tối hậu (bộ điều khiển ở hạ lưu nhất), trong ví dụ "
        "của ta là FC. Sau đó, coi bộ điều khiển đó là một phần của quá trình, chỉnh định bộ điều khiển "
        "thượng lưu kế tiếp (bộ có đầu ra lái điểm đặt của bộ vừa chỉnh). Cứ tiếp tục như vậy, nhớ coi "
        "bộ điều khiển vừa chỉnh là một phần của vòng quá trình, và cuối cùng chỉnh bộ điều khiển sơ "
        "cấp nhất — trong ví dụ của ta là TC."))
    b.append(fig(8, F.fig_9_8()))

    b.append(h3("9.9.1 Bộ điều khiển thứ cấp", "Secondary Controller"))
    b.append(p(
        "Bộ điều khiển thứ cấp hầu hết được dùng làm bộ điều khiển lưu lượng. Các vòng lưu lượng trong "
        "phần lớn trường hợp là ổn định nội tại. Do đó không cần điều khiển D, và hầu hết bộ điều khiển "
        "lưu lượng là bộ điều khiển PI. Việc chỉnh định được làm với sự cân nhắc thoả đáng cho một đáp "
        "ứng điều khiển đủ tốt và mài mòn van ở mức tối thiểu. K phải nhỏ hơn 1 để truyền được toàn dải "
        "OP của bộ điều khiển sơ cấp sang OP của bộ điều khiển thứ cấp."))

    b.append(h3("9.9.2 Bộ điều khiển sơ cấp", "Primary Controller"))
    b.append(p(
        "Bộ điều khiển sơ cấp thường điều khiển một vòng có động học phức tạp hơn và cần xem xét cẩn "
        "thận về ổn định. Ví dụ bộ gia nhiệt dòng liệu cho thấy rõ bộ điều khiển nhiệt độ TC phải gánh "
        "phần lớn độ trễ của quá trình. Do đó trong hầu hết trường hợp, bộ điều khiển sơ cấp là bộ điều "
        "khiển PID."))

    b.append(h3("Bài tập 11 — Điều khiển cascade", "Exercise 11 — Cascade Control"))
    b.append(p("Sẽ cho kinh nghiệm thực hành về các chủ đề của điều khiển cascade."))

    b.append(h2("9.10 Cascade với nhiều vòng thứ cấp", "Cascade Control with Multiple Secondaries"))
    b.append(p(
        "Một chiến lược điều khiển có thể gồm các bộ điều khiển có nhiều phép tính đầu ra. Trong hầu hết "
        "trường hợp, bộ điều khiển có nhiều đầu ra là bộ điều khiển sơ cấp trong một hệ cascade có nhiều "
        "hơn một bộ điều khiển thứ cấp."))
    b.append(fig(9, F.fig_9_9()))

    b.append(h3("9.10.1 Nhiều phép tính đầu ra", "Multiple Output Calculations"))
    b.append(p(
        "Kết quả của phép tính PID ở bộ điều khiển sơ cấp là đầu ra động của bộ điều khiển. Trong các "
        "bộ điều khiển số, đây là giá trị CV được tính cho mỗi khoảng chu kỳ quét và được dùng để tăng "
        "từng đầu ra một cách độc lập."))
    b.append(p(
        "Vì mỗi đầu ra của bộ điều khiển có thể có giá trị tuyệt đối khác nhau ở bất kỳ thời điểm nào, "
        "mỗi đầu ra được tăng riêng rẽ."))
    b.append(p(
        "Trên thực tế, mỗi đầu ra được tính độc lập với các đầu ra khác, với việc khởi tạo, xử lý giới "
        "hạn và xử lý cảnh báo riêng. Vì lượng dữ liệu cho nhiều đầu ra là quá nhiều đối với một màn "
        "hình, thiết bị điều khiển công nghiệp sẽ chỉ hiển thị đầu ra thứ nhất ở màn hình chi tiết "
        "chính và có các màn hình tiếp theo cho dữ liệu bổ sung như nhiều đầu ra. Từ góc độ kỹ thuật, "
        "phải ý thức được điều này để định nghĩa đầu ra quan trọng nhất là đầu ra thứ nhất của bộ điều "
        "khiển. Từ góc độ người vận hành, điều quan trọng là phải biết rằng giá trị đầu ra được hiển "
        "thị nổi bật nhất có thể không phải là đầu ra duy nhất cần theo dõi; nó có thể chỉ là đầu ra "
        "quan trọng nhất."))

    b.append(h3("Bài tập 12 — Cascade một sơ cấp và hai thứ cấp",
                "Exercise 12 — Cascade Control with One Primary and Two Secondaries"))
    b.append(p("Sẽ cho kinh nghiệm thực hành về chủ đề bộ điều khiển có nhiều đầu ra."))

    b.append(quote(
        "Cascade không làm vòng điều khiển nhanh hơn. Nó chỉ làm cho nhiễu bị chặn ở tầng nơi nó xuất "
        "hiện, thay vì để nó đi qua toàn bộ quá trình.",
        "Ý chính của chương"))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This is the hinge chapter of the book. Before it, every controller was a black box with two "
        "inputs and one output. After it, the controller has three more things: an output block with a "
        "mode, a limit that either saturates or does not, and a set of equations that decides how PV and "
        "SP are shared between the P, I and D actions."))
    b.append(p(
        "Those three things sound like plumbing. They are in fact the preconditions for joining two "
        "controllers into a cascade — and a cascade is the single most profitable intervention available "
        "on an ordinary control loop."))

    b.append(h2("One calculation, many outputs"))
    b.append(p(
        "The first idea in the chapter is that the PID calculation is a single number per scan, but the "
        "controller may own several output blocks. Each block keeps its own absolute value, its own "
        "mode, its own limits and its own initialisation. The increment is common; the value is not."))
    b.append(fig(1, F.fig_9_1(), "en"))
    b.append(p(
        "This is what makes a cascade physically possible. The primary controller's output is not a "
        "valve position, it is a number that a secondary controller will treat as a set point. The same "
        "increment therefore has to arrive at both blocks, while the two blocks sit at completely "
        "different absolute levels — one perhaps at 35 % and the other at 72 %."))
    b.append(fig(2, F.fig_9_2(), "en"))

    b.append(h2("Saturation, and the two ways to handle a limit"))
    b.append(p(
        "The chapter's second idea is subtler and is where most commissioning errors live. A controller "
        "does not know its own output value; it only knows the increment it wants to apply. If the "
        "output is already at 100 %, the increment has nowhere to go, and what happens next depends "
        "entirely on how the limit is implemented."))
    b.append(p(
        "Under saturation, the controller keeps a virtual output that is free to exceed the limit. The "
        "real output stays pinned, but the virtual one keeps accumulating. When the disturbance finally "
        "reverses, the controller has to unwind all of that accumulation before the real output moves at "
        "all — which is why a loop that wound up during a start-up can take minutes to come back. Under "
        "non-saturation, the calculation is done on the real value only, the excess is discarded each "
        "scan, and the loop responds as soon as the error reverses."))
    b.append(fig(7, F.fig_9_7(), "en"))
    b.append(p(
        "Figure 9-7 is the picture to keep. Both controllers reach the ceiling at the same moment. The "
        "one that saturates stays there long after the disturbance has turned around, because its "
        "virtual output has to be spent down first. The one that does not saturate comes off the ceiling "
        "immediately. Neither is wrong as an implementation; they are different answers to the question "
        "of whether the controller is allowed to remember what it could not deliver."))

    b.append(h2("Cascade: putting the fast loop inside the slow one"))
    b.append(p(
        "The feed heater example is the canonical one and worth following closely. With temperature "
        "control alone, the valve position is the controller's output, and a change in fuel supply "
        "pressure changes the heat input without the controller knowing anything has happened until the "
        "outlet temperature moves. With a flow loop inserted, the valve is now the flow controller's "
        "business, and the temperature controller asks for a flow rather than a valve position."))
    b.append(fig(3, F.fig_9_3(), "en"))
    b.append(p(
        "The physics that makes this work is the difference in speed. A flow loop settles in a second or "
        "two; a heater's outlet temperature takes minutes. A disturbance that acts on the fast variable "
        "is invisible to the slow controller until it has propagated all the way through the process, by "
        "which time it is a large error. Interposing the fast loop means the disturbance is corrected "
        "before it ever becomes an error in the slow variable. That is the whole of cascade control, and "
        "the rest of the section is bookkeeping needed to make it bumpless."))
    b.append(fig(4, F.fig_9_4(), "en"))

    b.append(h2("PV-tracking and initialisation: the two mechanisms that prevent the bump"))
    b.append(p(
        "A cascade is easy to build and hard to switch on. The difficulty is that when the secondary goes "
        "to automatic, its set point must already equal the value the primary wants to command, and the "
        "primary's output must already equal that same value. Two mechanisms achieve this, and they are "
        "easy to confuse."))
    b.append(p(
        "PV-tracking acts inside one controller: while it is in manual, its set point is forced to equal "
        "its measurement, so the error is zero and the integral does not wind. Initialisation acts "
        "between controllers: the secondary sends its set point back up the chain into the primary's "
        "output block, so that when the primary later goes to automatic it starts from exactly the value "
        "the secondary is already using. The first prevents a bump inside a loop; the second prevents a "
        "bump between loops."))

    b.append(h2("Equation types: who gets to see the set point"))
    b.append(p(
        "The last conceptual section answers a question that rarely gets asked aloud: when the operator "
        "moves the set point, should the proportional and derivative actions see it? Under type A they "
        "do, and a large set-point step produces a proportional jump and a derivative spike in the same "
        "scan. Under type C they do not — P and D act on the measurement only, and the error feeds only "
        "the integral, so a set-point step becomes a ramp."))
    b.append(fig(5, F.fig_9_5(), "en"))
    b.append(p(
        "Figure 9-6 draws the alternative. The difference is not academic: on a large set-point step the "
        "type A controller produces a proportional jump plus a derivative spike in the same scan, which is "
        "a step change commanded into the valve; the type C controller ramps into it instead."))
    b.append(fig(6, F.fig_9_6(), "en"))
    b.append(p(
        "The algebra in the chapter proves that with a constant set point the two types are identical, "
        "which is the important reassurance: choosing type C does not change how the loop rejects "
        "disturbances. It changes only how the loop follows the set point. That is precisely the "
        "distinction a cascade needs, because the primary's set point is a process value and the "
        "secondary's set point is a command."))
    b.append(p(
        "The rule that follows is short and worth memorising. Secondaries must use type A — using type C "
        "there would leave only the integral acting between the primary's output and the secondary's "
        "output, adding ninety degrees of phase lag to the primary loop and destabilising it. The "
        "ultimate primary is the natural home for type C, because that is the controller whose set point "
        "an operator can move, and the one whose output drives a valve that should not be slammed."))

    b.append(h2("Tuning a cascade"))
    b.append(p(
        "Tune from the inside out. The secondary is tuned first, with the primary left in manual, because "
        "the secondary has to be fast and stable before it can be treated as part of the process. Then "
        "the primary is tuned with the secondary in automatic, treating the whole inner loop as one more "
        "lag in the process. Tuning in the other order does not work: the outer loop would be tuned "
        "against a process that changes the moment the inner loop is closed."))
    b.append(fig(8, F.fig_9_8(), "en"))
    b.append(p(
        "The chapter's note that the secondary gain should be below one is easy to miss and matters. If "
        "the secondary's gain is above one, the primary's full output range is not passed through to the "
        "secondary's output, and the cascade loses authority at the extremes exactly when it is needed."))

    b.append(h2("One primary, several secondaries"))
    b.append(p(
        "Section 9.10 is the case that breaks a naive implementation: a control strategy in which the "
        "primary controller owns more than one output calculation. The PID result is the dynamic output of "
        "the primary — the CV computed once per scan — and in a digital controller that single number is "
        "used to increment each output block independently. Because the blocks can sit at different "
        "absolute values at any moment, each has to be incremented separately rather than written."))
    b.append(fig(9, F.fig_9_9(), "en"))
    b.append(p(
        "What this buys is scale without extra logic. One temperature controller can drive three fuel "
        "valves, or a pressure controller can trim two compressors, and the primary never needs to know "
        "how many secondaries it has — the increment is common and each block resolves it into its own "
        "engineering units. What it does not buy is permission to mix quantities: the outputs must all "
        "mean the same thing, or the primary's single increment means something different at each block "
        "and the cascade has no common variable to regulate."))
    return "".join(b)
