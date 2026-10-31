# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 8, Tuning of PID Controllers
(Wolfgang Altmann, IDC Technologies)."""
import pc8fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 31
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Đường cong phản ứng (reaction curve)</em> — ghi lại đáp ứng của PV khi đầu ra bị bước "
            "một lượng trong chế độ MANUAL. · "
            "<em>Độ trễ hiệu dụng L</em> — thời gian từ lúc bước tới lúc PV thay đổi thấy được. · "
            "<em>N</em> — độ dốc cực đại của PV, tính bằng % mỗi phút. · "
            "<em>LTC</em> — hằng số thời gian vòng. · "
            "<em>P_u, K_u</em> — chu kỳ và hệ số khuếch đại tới hạn, đo ở dao động liên tục. · "
            "<em>Tỉ số tắt P</em> — tỉ số biên độ hai đỉnh liên tiếp của dao động tắt dần.")
    return note(
        "<b>Key terms.</b> <em>Reaction curve</em> — the recorded PV response to a step in the "
        "controller output, taken in MANUAL. · <em>Effective lag L</em> — the time from the step to the "
        "first visible change in PV. · <em>N</em> — the maximum slope of PV, in per cent per minute. · "
        "<em>LTC</em> — loop time constant. · <em>P-u, K-u</em> — the ultimate period and ultimate "
        "gain, measured at continuous cycling. · <em>Decay ratio P</em> — the ratio of two successive "
        "peak amplitudes of a damped oscillation.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương này là chương dài nhất và cũng là chương thực dụng nhất của phần điều khiển. Nó trả "
        "lời một câu hỏi mà mọi kỹ thuật viên đều phải trả lời ít nhất một lần trong đời: đặt ba con số "
        "vào bộ điều khiển bằng cách nào?"))
    b.append(p(
        "Altmann trình bày bốn phương pháp, và điều đáng chú ý là ông không nói phương pháp nào "
        "<em>đúng</em>. Ông nói mỗi phương pháp cần một thứ khác nhau — một đường cong phản ứng, một "
        "điểm uốn, một chu kỳ dao động — và mỗi phương pháp cho một bộ số hơi khác nhau. Việc của người "
        "chỉnh định là biết mình đang có thứ gì trong tay và chấp nhận mức bất định đi kèm."))

    b.append(h2("8.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Áp dụng được các thủ tục chỉnh định vòng hở và vòng kín;",
        "Tính được các hằng số chỉnh định theo Ziegler &amp; Nichols và theo Pessen;",
        "Trình bày được cách chỉnh tinh (fine-tuning) một hệ điều khiển vòng kín."]))

    b.append(h2("8.2 Mục đích của việc chỉnh định", "Objectives of Tuning"))
    b.append(p(
        "Khi chỉnh định một bộ điều khiển trong hệ vòng kín, mục đích thường có nhiều và đôi khi mâu "
        "thuẫn nhau. Danh sách dưới đây gồm những mục đích quan trọng nhất:"))

    b.append(h3("Cực tiểu hoá tích phân sai lệch", "Minimisation of the Integral of the Error"))
    b.append(p(
        "Mục đích ở đây là giữ cho diện tích bao bởi hai đường — đường SP và đường PV — nhỏ nhất. Đây "
        "là mục tiêu của việc chỉnh định theo các phương pháp do Ziegler và Nichols phát triển, như "
        "minh hoạ trên Hình 8-1."))
    b.append(fig(1, F.fig_8_1()))

    b.append(h3("Cực tiểu hoá tích phân bình phương sai lệch", "Minimisation of the Integral of the Error Squared"))
    b.append(p(
        "Như Hình 8-2 cho thấy, có thể có trường hợp diện tích sai lệch nhỏ nhưng độ lệch của PV so với "
        "SP trong một khoảng thời gian đầu lại không chấp nhận được. Trong những trường hợp đó phải cho "
        "trọng số đặc biệt đối với độ lớn của độ lệch giữa PV và SP. Vì trọng số tỉ lệ với độ lớn của "
        "độ lệch, ta nhân trọng số với sai lệch; kết quả là bình phương sai lệch (bình phương sai lệch "
        "= sai lệch × trọng số). Nhiều bộ điều khiển hiện đại có chức năng tự chỉnh liên tục làm việc "
        "theo nguyên tắc này."))
    b.append(fig(2, F.fig_8_2()))

    b.append(h3("Điều khiển nhanh", "Fast Control"))
    b.append(p(
        "Trong hầu hết trường hợp, điều khiển nhanh là yêu cầu nguyên tắc từ góc độ vận hành; tuy nhiên "
        "điều này chủ yếu đạt được bằng cách cho bộ điều khiển làm việc với hệ số khuếch đại cao, và "
        "điều đó khá thường xuyên dẫn tới mất ổn định hoặc kéo dài thời gian xác lập do ảnh hưởng của "
        "các nhiễu quá trình. Cần đạt được sự cân bằng cẩn thận giữa khâu tỉ lệ (K_C) với các giá trị "
        "đặt của hằng số thời gian tích phân T_INT và đặc biệt là hằng số thời gian vi phân T_DER."))

    b.append(h3("Mài mòn thiết bị được điều khiển ở mức tối thiểu", "Minimum Wear and Tear of Controlled Equipment"))
    b.append(p(
        "Ví dụ, một van hay một hệ servo không nên bị dịch chuyển thường xuyên, nhanh hay tới các vị trí "
        "cực đoan một cách không cần thiết. Đặc biệt phải xét tới ảnh hưởng của nhiễu, của các nhiễu quá "
        "trình quá mức và của việc điều khiển nhanh đến mức không thực tế."))
    b.append(p(
        "Việc PV “săn” liên tục quanh SP có thể khiến một phần dao động đó — với tỉ lệ tuỳ theo hệ số "
        "khuếch đại của bộ điều khiển — xuất hiện trên đầu ra bộ điều khiển. Trong nhiều trường hợp điều "
        "này làm cơ cấu chấp hành bị dẫn động “rung”, và hiện tượng đó rất thường bị hiểu nhầm là do "
        "“nhiễu”, trong khi nguyên nhân thật là hệ số khuếch đại của bộ điều khiển — và do đó là của cả "
        "vòng — bị đặt quá cao trong một nỗ lực “tăng tốc” đáp ứng của quá trình (xem §8.2.1)."))

    b.append(h3("Không quá điều chỉnh khi khởi động", "No Overshoot at Start Up"))
    b.append(p(
        "Thời điểm nguy hiểm nhất đối với quá điều chỉnh là lúc khởi động hệ thống. Nếu điều khiển một "
        "bồn hở, ta không muốn bồn tràn vì mức bị quá điều chỉnh. Nghiêm trọng hơn, nếu là bồn kín, ta "
        "không muốn bồn nổ. Những xem xét tương tự có ở mọi nơi có nguy hiểm. Một ví dụ là trường hợp "
        "bồn có áp suất tối đa cho phép mà trong bất kỳ tình huống nào cũng không được vượt quá."))
    b.append(note(
        "<b>Lưu ý.</b> Khởi động <em>không</em> đồng nghĩa với thay đổi điểm đặt. Khi chuyển từ MANUAL "
        "sang AUTO, sai lệch có thể rất lớn nhưng nó <em>không</em> xuất hiện dưới dạng một bước nhảy, "
        "nên khâu vi phân không bị kích. Đó là lý do hai tình huống này cần hai bộ công thức khác nhau."))

    b.append(h3("Giảm thiểu ảnh hưởng của các nhiễu đã biết", "Minimizing the Effect of Known Disturbances"))
    b.append(p(
        "Nếu đo được nhiễu, ta có cơ hội xử lý nó trước khi ảnh hưởng của nó trở nên rõ ràng. Xem phần "
        "Điều khiển theo hướng (Feedforward Control) để có ví dụ về cách tiếp cận vấn đề này."))

    b.append(h2("8.3 Phương pháp đường cong phản ứng (Ziegler-Nichols)",
                "Reaction Curve Method (Ziegler Nichols)"))
    b.append(p(
        "Phương pháp chỉnh định theo đường cong phản ứng dựa trên việc tạo một bước thay đổi ở đầu ra "
        "bộ điều khiển và ghi lại đáp ứng của quá trình. Có thể coi đây là cách tiếp cận VÒNG HỞ, vì bộ "
        "điều khiển KHÔNG được dùng vào việc gì ngoài việc thay đổi giá trị OP (trong chế độ MANUAL) để "
        "tạo cho quá trình bước thay đổi cần thiết ở MV."))
    b.append(p("Các đại lượng cần ghi lại là:"))
    b.append(ul([
        "Độ trễ hiệu dụng (effective lag): sau bước thay đổi bao lâu thì PV mới có thay đổi thấy được;",
        "Thời gian phản ứng của quá trình: tốc độ thay đổi cực đại, biểu diễn qua độ thay đổi của PV;",
        "Thời gian để PV đạt 63,2 % giá trị cực đại của nó."]))
    b.append(p(
        "Có nhiều biến thể của phương pháp chỉnh định này; tất cả đều dùng kết quả từ đường cong phản "
        "ứng. Ba biến thể phổ biến nhất được bàn ở các mục tiếp theo, sau phần trình bày cách tạo ra "
        "đường cong phản ứng của hệ."))

    b.append(h3("8.3.1 Thủ tục lấy đường cong phản ứng vòng hở",
                "The Procedure to Obtain an OPEN LOOP Reaction Curve"))
    b.append(h4("Ghi lại đáp ứng của PV"))
    b.append(p(
        "Nối một thiết bị ghi vào tín hiệu đầu vào (PV) của bộ điều khiển. Thiết bị ghi lý tưởng phải "
        "hiển thị được hai kênh: PV từ hệ thống vào bộ điều khiển, và chuyển động SP của bộ điều khiển."))
    b.append(p(
        "Bản ghi phải được vẽ theo trục tung 0–100 % PV và trục hoành đủ nhanh, chia độ bằng phút và "
        "PHẦN LẺ của phút (không phải bằng giây). Nếu dùng máy ghi giấy, phải điều chỉnh được thang "
        "đứng sao cho độ thay đổi của PV trải rộng nhất có thể trên băng giấy — điều này cần thiết cho "
        "độ chính xác của phép đo."))

    b.append(h4("Chế độ của bộ điều khiển"))
    b.append(p(
        "Đặt bộ điều khiển ở CHẾ ĐỘ MANUAL; điều này bảo đảm ta có một vòng hở, trong đó tác động của "
        "bộ điều khiển không ảnh hưởng gì khi PV thay đổi. Lý do là ta không quan tâm tới hành vi của bộ "
        "điều khiển mà chỉ quan tâm tới đặc tính phản ứng của quá trình."))

    b.append(h4("Thay đổi quá trình"))
    b.append(p(
        "Khi tạo một bước thay đổi ở giá trị đầu ra của bộ điều khiển, quá trình sẽ có một phản ứng "
        "tương ứng, xuất hiện dưới dạng thay đổi theo thời gian của PV. Đó là đặc tính phản ứng của quá "
        "trình. Phải có đủ hiểu biết về quá trình để biết có thể thay đổi đầu ra bao nhiêu mà không gây "
        "nguy hiểm cho chính quá trình."))

    b.append(h4("Lấy và phân tích đường cong phản ứng"))
    b.append(p(
        "Quan sát bản ghi phản ứng của quá trình. Đường cong cần có là Hình 8-3, trên đó ta quan sát và "
        "đo các tham số cần thiết để tính các thành phần P, I và D của bộ điều khiển; tuỳ phương pháp "
        "phân tích được chọn mà cần một số hoặc tất cả các tham số sau:"))
    b.append(ul([
        "Thời điểm giá trị SP bị thay đổi (độ lớn của thay đổi này KHÔNG quan trọng, chỉ cần càng lớn "
        "càng tốt miễn là quá trình không bị ảnh hưởng xấu);",
        "Thời gian (tính bằng phút và phần lẻ của phút) trôi qua trước khi thấy thay đổi rõ rệt ở PV; "
        "đại lượng này đo bằng L, tức độ trễ hiệu dụng;",
        "Điểm uốn (POI) trên đường cong PV;",
        "Điểm mà PV đã thay đổi 63,2 % (không nhất thiết trùng với POI), để tính LTC — hằng số thời "
        "gian vòng."]))
    b.append(fig(3, F.fig_8_3()))

    b.append(p(
        "Không thể tính các hằng số chỉnh định trước khi phân tích đường cong bằng vài xem xét thông "
        "thường. Độ trễ hiệu dụng L sẽ là ảnh hưởng và thành phần chính của giá trị thời gian tích phân "
        "T_INT. Độ dốc, tức tốc độ thay đổi của quá trình, ký hiệu N, sẽ là yếu tố chính ảnh hưởng tới "
        "giá trị hệ số khuếch đại K_C, vì nó biểu diễn chính hệ số khuếch đại hay độ nhạy của quá trình."))
    b.append(p(
        "Còn lại là hằng số thời gian vi phân T_DER; vì nó được đưa vào để bù tác dụng gây mất ổn định "
        "của khâu tích phân, phải tồn tại một quan hệ giữa T_DER và T_INT."))
    b.append(p(
        "Ziegler và Nichols đã xây dựng các công thức chỉnh định tối ưu có tính tới và liên hệ các giá "
        "trị P, I, D với nhau. Việc chỉnh định tối ưu theo các công thức này nhằm cực tiểu hoá tích phân "
        "của sai lệch (diện tích sai lệch nhỏ nhất)."))
    b.append(p(
        "Các công thức đó không tính tới độ lớn của sai lệch. Các hằng số chỉnh định tối ưu luôn dựa "
        "trên giả thiết quá trình có thời gian chết nhỏ và đặc tính trễ bậc một."))
    b.append(p(
        "Như đã nói ở đầu mục này, có ba biến thể của phương pháp; các mục 8.4, 8.5 và 8.6 mô tả chi "
        "tiết từng biến thể."))

    b.append(h2("8.4 Phương pháp chỉnh định vòng hở Ziegler-Nichols (1)",
                "Ziegler Nichols Open Loop Tuning Method (1)"))
    b.append(p(
        "Từ Hình 8-4, phải xác định giá trị độ trễ hiệu dụng L — thời gian tính bằng phút thập phân cho "
        "tới khi quan sát thấy tốc độ thay đổi rõ rệt — và giá trị N, tức độ dốc của PV tại điểm có tốc "
        "độ thay đổi cực đại. Từ hai giá trị này có thể tính các hằng số chỉnh định cho bộ điều khiển P, "
        "PI và PID theo các công thức Ziegler-Nichols sau đây."))

    b.append(h3("8.4.1 Thuật toán điều khiển P", "Ziegler Nichols P Control Algorithm"))
    b.append(p(
        "Cần lưu ý rằng các tổ hợp chế độ điều khiển khác nhau cho các hằng số chỉnh định khác nhau, và "
        "giữa chúng tồn tại một quan hệ được lặp lại xuyên suốt các chế độ trình bày ở đây."))
    b.append(eq("K_c = OP% / (N%/phút × L phút)", "8.1"))

    b.append(h3("8.4.2 Thuật toán điều khiển PI", "Ziegler Nichols PI Control Algorithm"))
    b.append(p(
        "Nếu cần có tác động tích phân, hệ số khuếch đại của bộ điều khiển được giảm 10 %, và hằng số "
        "thời gian tích phân — đưa vào để giúp loại bỏ giá trị offset giữa SP và PV trong số hạng ERR — "
        "được đặt bằng 3 lần khoảng trễ L (tính bằng phút). Vì đầu ra tích phân được cộng với đầu ra tỉ "
        "lệ nằm trong hệ số khuếch đại K_C, có thể giảm K_C một chút, làm vòng điều khiển ổn định hơn. "
        "Phần đầu ra bị mất do việc giảm đó sẽ được bù dần, trong thời gian tích phân T_INT, nhờ tác "
        "động tích phân."))
    b.append(eq("K_c = 0,9 × OP% / (N%/phút × L phút)", "8.2"))
    b.append(eq("T_int = 3 × L  (phút)", "8.3"))

    b.append(h3("8.4.3 Thuật toán điều khiển PID", "Ziegler Nichols PID Control Algorithm"))
    b.append(p(
        "Tiếp theo, nếu cần thêm trợ giúp để ổn định vòng, ta đưa vào điều khiển vi phân. Khi đó hệ số "
        "khuếch đại của bộ điều khiển được tăng 20 %. Thời gian tích phân được làm nhanh hơn (hay ngắn "
        "hơn) 33 %, và hằng số thời gian vi phân nhanh hơn (hay ngắn hơn) bốn lần so với thời gian tích "
        "phân. Nói cách khác, quan hệ giữa T_INT và T_DER là 4:1."))
    b.append(eq("K_c = 1,2 × OP% / (N%/phút × L phút)", "8.4"))
    b.append(eq("T_int = 2 × L  (phút)", "8.5"))
    b.append(eq("T_der = 0,5 × L  (phút)", "8.6"))
    b.append(fig(4, F.fig_8_4()))

    b.append(h3("8.4.4 Ví dụ về các thuật toán P, I, D vòng hở Ziegler-Nichols",
                "Examples of Ziegler Nichols P, I and D OPEN LOOP Control Algorithms"))
    b.append(p("Thay các giá trị sau:"))
    b.append(ul(["OP% = ∆OP = 12,5 %", "N = 35 % mỗi phút", "L = 0,65 phút"]))
    b.append(p("Các giá trị đặt cho P, I và D được tóm tắt như sau:"))

    b.append(table(
        ["Chế độ", "K_C", "T_INT (phút)", "T_DER (phút)"],
        [["P", "12,5 / (35 × 0,65) = 0,549", "—", "—"],
         ["PI", "0,9 × 0,549 = 0,495", "3 × 0,65 = 1,95", "—"],
         ["PID", "1,2 × 0,549 = 0,659", "2 × 0,65 = 1,30", "0,5 × 0,65 = 0,325"]],
        "Bảng 8-1. Kết quả số của ví dụ §8.4.4 với OP% = 12,5 %, N = 35 %/phút, L = 0,65 phút."))

    b.append(p(
        "Điều đáng chú ý trong bảng này không phải các con số mà là cấu trúc: cùng một phép chia "
        "OP/(N·L) xuất hiện ở cả ba dòng, chỉ khác hệ số 1 – 0,9 – 1,2. Đó là lý do Ziegler-Nichols dễ "
        "nhớ và cũng là lý do nó dễ bị dùng sai: nó chỉ cần hai con số, nên người ta hay quên rằng hai "
        "con số đó phải được đo trên một quá trình đang ở trạng thái làm việc thật."))

    b.append(h2("8.5 Phương pháp vòng hở Ziegler-Nichols (2) dùng POI",
                "Ziegler-Nichols Open Loop Method (2) using POI"))
    b.append(p(
        "Phiên bản này của phương pháp xác định hệ số khuếch đại và các thời gian tích phân, vi phân "
        "dùng cùng một đường cong đáp ứng nhưng được lấy theo cách hơi khác ví dụ trước. Nó được dùng "
        "khi quá trình được điều khiển bằng van."))
    b.append(p("Để lấy đường cong quá trình, dùng thủ tục sau:"))
    b.append(ol([
        "Đưa quá trình tới điểm đặt mong muốn ở chế độ MANUAL.",
        "Thay đổi VỊ TRÍ VAN một lượng nhỏ ∆V (%). Lượng thay đổi phải đủ lớn để tạo đáp ứng đo được, "
        "nhưng không đủ lớn để đẩy quá trình ra khỏi dải làm việc bình thường. Thay đổi van 5 % là điểm "
        "khởi đầu tốt.",
        "Đo ∆C (%) và L trên đường cong đáp ứng của quá trình."]))
    b.append(p(
        "POI (điểm uốn) được xác định trên đường cong PV (điểm có tốc độ thay đổi cực đại); vẽ một "
        "đường tiếp tuyến qua điểm đó, kéo xuống qua trục hoành và tiếp tục cho tới khi cắt trục tung "
        "(thời điểm giá trị SP bị thay đổi)."))
    b.append(fig(5, F.fig_8_5()))
    b.append(p("Từ đó tính được các hằng số PG_U và T_U sau:"))
    b.append(eq("PG_u = 2 × ∆V / ∆C", "8.7"))
    b.append(eq("T_u = 4 × L", "8.8"))
    b.append(p("Các giá trị đặt cho bộ điều khiển được xác định theo bảng dưới đây:"))

    b.append(table(
        ["Bộ điều khiển", "P", "PI", "PD (xem ghi chú)", "PID"],
        [["Hệ số khuếch đại K_C", "0,5 PG_U", "0,45 PG_U", "0,71 PG_U", "0,6 PG_U"],
         ["Thời gian tích phân T_INT", "—", "0,83 T_U", "—", "0,5 T_U"],
         ["Thời gian vi phân T_DER", "—", "—", "0,51 T_U", "0,125 T_U"]],
        "Bảng 8-2 (bảng 8.1 trong bản gốc). Các giá trị đặt của phương pháp vòng hở (2)."))
    b.append(note(
        "<b>GHI CHÚ.</b> Các giá trị đặt cho bộ điều khiển PD <em>không</em> xuất phát từ bài báo gốc "
        "của Ziegler-Nichols."))

    b.append(p(
        "Cần lưu ý rằng quan hệ giữa hệ số khuếch đại và các thời gian tích phân/vi phân ở phương pháp "
        "này giống với phương pháp trước. Cụ thể:"))
    b.append(ul([
        "Hệ số khuếch đại K_C ở chế độ P bằng 0,5; ở chế độ PI bằng 0,45; ở chế độ PID bằng 0,6 — tức "
        "các tỉ số là 1 : 0,9 : 1,2.",
        "Ở chế độ PID, tỉ số T_INT : T_DER lại là 4:1 (0,5 : 0,125)."]))
    b.append(p(
        "Dùng phương pháp này, độ dốc hay tốc độ thay đổi thường dễ đánh giá hơn nhiều trên băng ghi "
        "giấy."))

    b.append(h2("8.6 Phương pháp hằng số thời gian vòng (LTC)", "Loop Time Constant (LTC) Method"))
    b.append(p(
        "Phương pháp chỉnh định này, cũng như hai ví dụ trước, dùng đường cong phản ứng và áp dụng được "
        "khi hệ có đáp ứng trễ bậc một, xác định bởi một phương trình vi phân tuyến tính bậc một:"))
    b.append(eq("τ · dc/dt + c = K·r", "8.9"))
    b.append(p("hoặc:"))
    b.append(eq("(1/K) · dc/dt + τ · c = r", "8.10"))
    b.append(p(
        "trong đó: c là đầu ra; r là đầu vào; K là hệ số khuếch đại; τ là hằng số thời gian."))
    b.append(p(
        "Quan sát một đường cong đáp ứng bậc một sẽ thấy nó luôn giảm dần tốc độ: tốc độ đáp ứng đạt "
        "cực đại ngay ở thời điểm đầu và liên tục giảm từ đó. Nếu hệ tiếp tục thay đổi với tốc độ đáp "
        "ứng cực đại — tốc độ tại gốc toạ độ — thì nó sẽ đạt giá trị cuối cùng (100 %) trong đúng một "
        "hằng số thời gian (thời gian T_INT)."))
    b.append(fig(6, F.fig_8_6()))
    b.append(p(
        "Hình 8-6 minh hoạ một đường cong bậc một tạo ra từ đầu vào bậc thang. Đường cong này cho giá "
        "trị bằng số của độ thay đổi: trong khoảng thời gian đầu (trong trường hợp của ta là hằng số "
        "thời gian tích phân đặt bởi T_INT), độ thay đổi bằng 63,2 %. Trong khoảng thời gian thứ hai, "
        "63,2 % của 36,8 % còn lại sẽ xảy ra, và cứ tiếp tục như vậy ở mỗi khoảng thời gian. Về lý "
        "thuyết đáp ứng không bao giờ đạt 100 %, nhưng nó tiệm cận tới đó."))
    b.append(p(
        "Bằng cách đo cả thời gian chết của vòng và hằng số thời gian của vòng — thời gian từ lúc PV "
        "thay đổi thấy được tới lúc đạt 63,2 %, như Hình 8-7 — có thể xác định:"))
    b.append(eq("PG = 1 / K_quá_trình   (vòng hở)", "8.11"))
    b.append(eq("IG = LTC", "8.12"))
    b.append(eq("DG = 0,25 × IG", "8.13"))
    b.append(fig(7, F.fig_8_7()))

    b.append(h3("Bài tập 7 — Bài tập chỉnh định vòng hở", "Exercise 7 — Openloop Tuning Exercise"))
    b.append(p("Để biết thêm về chủ đề chỉnh định vòng hở."))

    b.append(h2("8.7 Vấn đề trễ nghịch gặp phải khi chỉnh định vòng hở",
                "Hysteresis Problems that may be encountered in Open Loop Tuning"))
    b.append(p(
        "Trong thực tế vận hành, làm chỉnh định vòng hở với bước càng lớn càng tốt, trên toàn dải làm "
        "việc bình thường và theo cả hai chiều, là việc nên làm. Nghĩa là sau khi tạo một bước TĂNG 20 % "
        "và ghi lại đáp ứng của hệ, đưa đầu ra trở về giá trị ban đầu và lại ghi đáp ứng của hệ."))
    b.append(p(
        "Trong hầu hết hệ thống, đáp ứng tăng và đáp ứng giảm sẽ khác nhau. Nếu khác biệt chỉ vài phần "
        "trăm (dưới 5–6 %), lấy giá trị trung bình của hai lần ghi và áp dụng kết quả đó cho thuật toán "
        "chỉnh định đang dùng."))
    b.append(p(
        "Nếu khác biệt lớn, chỉnh định theo một trong hai đáp ứng có thể dẫn tới mất ổn định hoặc điều "
        "khiển kém khi quá trình đáp ứng theo chiều còn lại — chiều KHÔNG dùng để chỉnh định. Khi đó cần "
        "thiết kế lại chính hệ quá trình, hoặc đưa vào các thuật toán hiệu chỉnh, để giảm độ trễ nghịch "
        "xuống mức chấp nhận được."))
    b.append(p(
        "Một ví dụ về cách khắc phục vấn đề này được trình bày ở Chương 11 “Kết hợp điều khiển phản hồi "
        "và điều khiển theo hướng”, mục 11.5, nơi bàn về việc hiệu chỉnh chênh lệch thời gian giữa việc "
        "gia nhiệt và làm nguội một nồi hơi."))
    b.append(p(
        "Bản thân bộ điều khiển PID không thể đặt hay chỉnh định để giảm bớt loại vấn đề này."))

    b.append(h2("8.8 Phương pháp dao động liên tục (Ziegler-Nichols)",
                "Continuous Cycling Method (Ziegler Nichols)"))
    b.append(p(
        "Phương pháp chỉnh định này yêu cầu xác định giá trị tới hạn của hệ số khuếch đại bộ điều khiển "
        "(K_C) sao cho vòng điều khiển dao động liên tục. Điều đó xảy ra khi tổng hệ số khuếch đại của "
        "vòng (K_LOOP) bằng một. Giá trị hệ số khuếch đại bộ điều khiển (K_C) khi đó được gọi là hệ số "
        "khuếch đại tới hạn (K_U)."))
    b.append(p(
        "Mục 5.5 và 5.5.1 của Chương 5 trình bày các yêu cầu để một hệ được coi là ổn định."))
    b.append(p(
        "Ở đây phải nhớ rằng vòng được tạo thành từ nhiều phần tử, tất cả đều đóng góp vào tổng hệ số "
        "khuếch đại của vòng (K_LOOP), và phần tử duy nhất ta chỉnh được thường là hệ số khuếch đại của "
        "bộ điều khiển (K_C)."))
    b.append(p("Xét một vòng điều khiển lưu lượng chất lỏng cơ bản gồm:"))
    b.append(ol([
        "Một lưu lượng kế venturi có đầu ra 4–20 mA, đưa tới",
        "Một bộ điều khiển PID, bộ này lại có đầu ra 4–20 mA đưa tới",
        "Một cơ cấu chấp hành van, cơ cấu này làm thay đổi lưu lượng của",
        "Quá trình."]))
    b.append(p(
        "Khi tích hệ số khuếch đại của cả bốn phần tử này bằng một, hệ sẽ mất ổn định khi có nhiễu quá "
        "trình (một thay đổi điểm đặt). Nó sẽ dao động ở tần số riêng của mình, tần số này do độ trễ và "
        "thời gian đáp ứng của quá trình quyết định, và nguyên nhân là hệ số khuếch đại vòng đã bằng một."))
    b.append(p("Ví dụ, nếu hệ nói trên có các đặc tính khuếch đại sau:"))
    b.append(ul(["Hệ số khuếch đại venturi = 0,75",
                 "Hệ số khuếch đại van điều khiển = 1,12",
                 "Hệ số khuếch đại quá trình = 0,98"]))
    b.append(p("thì hệ số khuếch đại QUÁ TRÌNH (theo cách bộ điều khiển “nhìn thấy”) được tính là:"))
    b.append(eq("K_P = 0,75 × 1,12 × 0,98 = 0,8232", "8.14"))
    b.append(p(
        "Với K_P bằng 0,8232, để K_LOOP bằng 1 thì K_C phải bằng 1/0,8232 = 1,215, cho:"))
    b.append(eq("K_LOOP = 0,75 × 1,12 × 0,98 × 1,215 = 1", "8.15"))
    b.append(p(
        "Để chỉ quan sát đặc tính động học của quá trình, không được dùng điều khiển tích phân hay vi "
        "phân trong quá trình xác định K_C nhằm đạt tổng hệ số khuếch đại vòng K_LOOP bằng một (không "
        "để bộ điều khiển đưa vào một dịch pha “làm hỏng” phép đo)."))
    b.append(p(
        "Sau đó có thể đo tần số dao động (chu kỳ của một chu kỳ dao động); đây là chu kỳ tới hạn P_U."))
    b.append(p(
        "Ngoài ra, ta biết giá trị cuối cùng của K_C là hệ số khuếch đại tới hạn của bộ điều khiển "
        "(K_U). Giá trị này, khi nhân với (những) hệ số khuếch đại quá trình chưa biết, sẽ cho hệ số "
        "khuếch đại vòng K_LOOP bằng 1. Từ đó có thể ổn định vòng bằng cách giảm giá trị K_C."))

    b.append(h3("8.8.1 Các bước của chỉnh định vòng kín (phương pháp dao động liên tục)",
                "The Stages of Obtaining Closed Loop Tuning (Continuous Cycling Method)"))
    b.append(ol([
        "<b>Đưa bộ điều khiển về chỉ có điều khiển P.</b> Để tránh bộ điều khiển ảnh hưởng tới việc "
        "đánh giá động học của quá trình, không được để điều khiển tích phân hay vi phân hoạt động. Đặt "
        "T_INT = 999 và T_DER = 0.",
        "<b>Chọn điều khiển P tác động lên ERR = (SP − PV).</b> Bảo đảm điều khiển P làm việc với cả "
        "thay đổi PV lẫn thay đổi SP. Điều này cho phép ta thay đổi số hạng ERR, và do đó thay đổi đầu "
        "ra bộ điều khiển, bằng cách thay đổi giá trị SP.",
        "<b>Đưa bộ điều khiển sang chế độ AUTOMATIC.</b> Cần có vòng kín để đạt được dao động liên tục "
        "ở giá trị hệ số khuếch đại tới hạn.",
        "<b>Tạo một bước thay đổi điểm đặt.</b> Để quan sát PV xác lập thế nào sau nhiễu, thay đổi giá "
        "trị SP để mô phỏng một nhiễu. Trước khi tạo bước thay đổi SP, bảo đảm quá trình đang ổn định "
        "và chỉ còn những dao động động học nhỏ.",
        "<b>Hành động dựa trên quan sát.</b> Nếu các dao động xuất hiện mà tắt nhanh (hoặc hoàn toàn "
        "không có dao động), tăng giá trị K_C. Mức tăng K_C phụ thuộc vào tốc độ và độ lớn thay đổi "
        "của PV do lần thay đổi SP vừa rồi. Sau đó lặp lại bước 4, đưa điểm đặt trở về giá trị ban đầu.",
        "<b>Kết thúc thủ tục chỉnh định.</b> Khi đã có dao động liên tục của quá trình, đo chu kỳ và "
        "giá trị K_C đạt được. Thời gian đó là chu kỳ tới hạn P_U, giá trị K_C là hệ số khuếch đại tới "
        "hạn K_U. GIẢM GIÁ TRỊ K_C ĐI 50 % ĐỂ DỪNG DAO ĐỘNG VÀ ĐƯA SP VỀ GIÁ TRỊ BAN ĐẦU ĐỂ ỔN ĐỊNH "
        "QUÁ TRÌNH."]))
    b.append(note(
        "<b>Cảnh báo.</b> Khi dao động xuất hiện và có dấu hiệu tăng biên độ, phải dừng ngay bài thử và "
        "giảm K_C để quá trình ổn định lại. Tổng hệ số khuếch đại vòng khi đó đã lớn hơn 1, nên nó đã "
        "khuếch đại chính bước thay đổi SP. Lặp lại bài thử với mức tăng K_C thận trọng hơn."))

    b.append(h3("8.8.2 Tính các hằng số chỉnh định", "Calculation of Tuning Constants (Continuous Cycling Method)"))
    b.append(p(
        "Các chế độ điều khiển P, PI và PID cho các hằng số chỉnh định khác nhau. Tuy nhiên cần lưu ý "
        "rằng chính những quan hệ đã gặp ở phương pháp đường cong phản ứng lại xuất hiện ở đây."))
    b.append(table(
        ["Bộ điều khiển", "P", "PI", "PID"],
        [["Hệ số khuếch đại K_C", "0,5 K_U", "0,45 K_U", "0,6 K_U"],
         ["Thời gian tích phân T_INT", "—", "P_U / 1,2", "P_U / 2"],
         ["Thời gian vi phân T_DER", "—", "—", "P_U / 8"]],
        "Bảng 8-3 (bảng 8.2 trong bản gốc). Các giá trị đặt của phương pháp dao động liên tục."))
    b.append(note(
        "<b>GHI CHÚ.</b> Phương pháp này KHÔNG cho giá trị nào cho điều khiển PD, nhưng nếu cần có thể "
        "áp dụng các tỉ số dùng cho chỉnh định vòng hở."))

    b.append(h3("Bài tập 8 — Bài tập chỉnh định vòng kín", "Exercise 8 — Closedloop Tuning Exercise"))
    b.append(p("Để biết thêm về chủ đề chỉnh định vòng kín."))

    b.append(h2("8.9 Phương pháp chỉnh định theo dao động tắt dần", "Damped Cycling Tuning Method"))
    b.append(p(
        "Phương pháp này là một biến thể của phương pháp dao động liên tục. Nó được dùng khi dao động "
        "liên tục gây nguy hiểm cho quá trình, nhưng một dao động tắt dần ở mức nào đó là chấp nhận "
        "được."))

    b.append(h3("8.9.1 Phương pháp chỉnh định", "Tuning Method"))
    b.append(ol([
        "<b>Đưa bộ điều khiển về chỉ có điều khiển P.</b> Để tránh bộ điều khiển ảnh hưởng tới việc "
        "đánh giá động học của quá trình, không được để điều khiển I hay D hoạt động.",
        "<b>Điều khiển P trên ERR = (SP − PV).</b> Bảo đảm điều khiển P làm việc với cả thay đổi PV lẫn "
        "thay đổi SP, để có thể thay đổi số hạng ERR bằng cách thay đổi SP.",
        "<b>Đưa bộ điều khiển sang chế độ AUTOMATIC.</b> Cần vòng kín để có dao động tắt dần.",
        "<b>Tạo bước thay đổi điểm đặt.</b> Một bước thay đổi SP tạo ra nhiễu và ta quan sát PV xác lập "
        "thế nào. Trước khi thay đổi SP, quá trình phải ổn định, chỉ còn những dao động nhỏ.",
        "<b>Hành động dựa trên quan sát.</b> Nếu dao động tắt nhanh (hoặc không có), tăng K_C; mức tăng "
        "phụ thuộc tốc độ và độ lớn thay đổi của PV ở lần trước. Lặp lại bước 4, đưa SP về giá trị ban "
        "đầu. Khi dao động xuất hiện và có dấu hiệu tăng biên độ, dừng ngay và giảm K_C."]))
    b.append(p(
        "Khi đã có dao động tắt dần như Hình 8-8, ghi lại giá trị K_C — nay ký hiệu là K_D. Sau đó kết "
        "thúc bài thử bằng cách giảm K_C. K_D được dùng để xác định hệ số khuếch đại ở phần sau của bài "
        "tập này."))
    b.append(fig(8, F.fig_8_8()))

    b.append(h3("8.9.2 Tính toán", "Calculations"))
    b.append(p(
        "Bằng cách đo và chia biên độ của quá điều chỉnh thứ nhất cho biên độ của quá điều chỉnh thứ "
        "hai, ta tìm được tỉ số tắt P:"))
    b.append(eq("P = tỉ số tắt = (quá điều chỉnh 1) / (quá điều chỉnh 2)", "8.16"))
    b.append(p("Khoảng thời gian (phút) giữa hai điểm đo này cho giá trị P_d, chu kỳ tắt dần."))
    b.append(p("Sau đó tính tỉ số tắt δ từ:"))
    b.append(eq("A = (1/2π) × ln(P)", "8.17"))
    b.append(p("và:"))
    b.append(eq("δ = A / √(A² + 1)", "8.18"))
    b.append(p(
        "Trong hầu hết trường hợp, tỉ số tắt δ khoảng 0,5 là chấp nhận được đối với một dao động tắt dần."))
    b.append(p("Tiếp theo cần tính R_d từ:"))
    b.append(eq("R_d = P_u / P = √(1 − δ²)", "8.19"))
    b.append(p("Từ đó có công thức cho T_INT và T_DER:"))
    b.append(eq("PI:  T_int = 1,2 × (P_d × R_d)", "8.20"))
    b.append(eq("PID: T_int = 2 × (P_d × R_d)", "8.21"))
    b.append(eq("PID: T_der = (P_d × R_d) / 8", "8.22"))
    b.append(p(
        "Tiếp theo phải chuyển sự chú ý sang việc tính giá trị đặt hệ số khuếch đại của bộ điều khiển "
        "(K_C). Một số tài liệu hướng dẫn nói rằng K_C được xác định bằng “phán đoán tốt của người vận "
        "hành”, nhưng đó là cách làm rất may rủi."))
    b.append(p(
        "Vì ta đã có giá trị hệ số khuếch đại bộ điều khiển (K_D) dùng để tạo ra đáp ứng dao động tắt "
        "dần phục vụ việc đánh giá các hằng số thời gian tích phân và vi phân, có thể dùng nó để tìm ra "
        "giá trị K_U."))
    b.append(p("Trước tiên cần tính tỉ số quá điều chỉnh, là kết quả của:"))
    b.append(eq("tỉ số quá điều chỉnh = quá điều chỉnh / thay đổi xác lập", "8.23"))
    b.append(p("Sau đó tính K_U từ:"))
    b.append(eq("K_u = K_d / (tỉ số quá điều chỉnh)", "8.24"))
    b.append(p(
        "Có được giá trị K_U sẽ cho phép dùng các công thức vòng kín Ziegler-Nichols, đó là:"))
    b.append(ul(["Điều khiển P: K_C = 0,5 × K_U",
                 "Điều khiển PI: K_C = 0,45 × K_U",
                 "Điều khiển PID: K_C = 0,6 × K_U"]))

    b.append(h3("8.9.3 Đáp ứng bậc thang", "Step Responses"))
    b.append(p(
        "Hình 8-9 cho một cách biểu diễn đồ thị để lấy trực tiếp tỉ số tắt từ phần trăm quá điều chỉnh "
        "xuất hiện ở PV do một bước thay đổi tạo ra ở đầu ra bộ điều khiển, theo hệ thức: "))
    b.append(eq("%OS = 100 × exp(−πδ / √(1 − δ²))", "8.25"))
    b.append(fig(9, F.fig_8_9()))
    b.append(p(
        "Hình 8-10 dùng để xác định chu kỳ tới hạn P_U từ chu kỳ dao động tắt dần P, phục vụ việc dùng "
        "số liệu dao động tắt dần với công thức chỉnh định PID của phương pháp dao động liên tục "
        "Ziegler-Nichols (theo J. P. Stiekema, IDC 1997)."))
    b.append(eq("R_d = P_u / P = √(1 + (ln(OS)/π)²)", "8.26"))
    b.append(fig(10, F.fig_8_10()))

    b.append(h2("8.10 Chỉnh định không quá điều chỉnh khi khởi động (Pessen)",
                "Tuning for No Overshoot on Start Up (Pessen)"))
    b.append(p(
        "Phương pháp này là một biến thể của phương pháp dao động liên tục, dùng khi không cho phép có "
        "quá điều chỉnh, kể cả trong trường hợp cực đoan là lúc khởi động quá trình. “Khởi động” ở đây "
        "có nghĩa là chuyển từ điều khiển MANUAL sang AUTOMATIC."))
    b.append(p(
        "Một tình huống khởi động cực đoan tồn tại khi điểm đặt và PV rất khác nhau lúc chuyển từ "
        "MANUAL sang AUTOMATIC. Khác với thay đổi điểm đặt, việc chuyển từ MANUAL sang AUTOMATIC không "
        "tạo ra một bước nhảy trong ERR; do đó thay đổi này không ảnh hưởng trực tiếp tới điều khiển P "
        "hay D."))
    b.append(p(
        "Ví dụ áp dụng thủ tục chỉnh định theo Pessen là một bồn kín có thể nổ, hoặc một bồn hở có thể "
        "tràn."))
    b.append(p(
        "Các bước chỉnh định vòng kín cho trường hợp không quá điều chỉnh giống các bước của phương "
        "pháp dao động liên tục (xem §8.8.1)."))
    b.append(p("Các công thức Pessen xây dựng cho trường hợp này như sau:"))
    b.append(p("<b>Điều khiển PID:</b>"))
    b.append(ul(["K_C = 0,2 × K_U", "T_int = P_U / 3", "T_der = P_U / 2"]))

    b.append(h2("8.11 Chỉnh định có quá điều chỉnh nhỏ khi khởi động (Pessen)",
                "Tuning for Some Overshoot on Start Up (Pessen)"))
    b.append(p(
        "Phương pháp này là một biến thể của phương pháp dao động liên tục, dùng khi không muốn có quá "
        "điều chỉnh trong chế độ điều khiển điều biến bình thường, nhưng chấp nhận một ít quá điều "
        "chỉnh lúc khởi động."))
    b.append(p(
        "Các bước chỉnh định vòng kín cho trường hợp có quá điều chỉnh nhỏ giống các bước của phương "
        "pháp dao động liên tục (xem §8.8.1)."))

    b.append(h3("8.11.1 Các hằng số chỉnh định", "The Tuning Constants"))
    b.append(p("<b>Điều khiển PID:</b>"))
    b.append(ul(["K_C = 0,33 × K_U", "T_int = P_U / 2", "T_der = P_U / 3"]))

    b.append(h2("8.12 Tóm tắt các thuật toán chỉnh định vòng kín quan trọng",
                "Summary of Important Closed Loop Tuning Algorithms"))
    b.append(table(
        ["", "Dao động liên tục", "Pessen — quá điều chỉnh nhỏ", "Pessen — không quá điều chỉnh"],
        [["K_C", "0,6 × K_U", "0,33 × K_U", "0,2 × K_U"],
         ["T_INT", "P_U / 2", "P_U / 2", "P_U / 3"],
         ["T_DER", "P_U / 8", "P_U / 3", "P_U / 2"]],
        "Bảng 8-4 (bảng 8.3 trong bản gốc). Ba bộ giá trị đặt vòng kín."))

    b.append(p(
        "Ba cột của bảng này là ba điểm trên cùng một trục đánh đổi. Đi từ trái sang phải, hệ số khuếch "
        "đại giảm từ 0,6 xuống 0,33 rồi 0,2 lần K_U, còn thời gian vi phân tăng từ P_U/8 lên P_U/3 rồi "
        "P_U/2. Nói cách khác: càng muốn ít quá điều chỉnh, càng phải nhường độ nhanh cho khâu vi phân "
        "và càng phải hạ hệ số khuếch đại. Không có bộ số nào vừa nhanh nhất vừa không quá điều chỉnh."))

    b.append(h2("8.13 Phương trình PID: độ lợi phụ thuộc và độc lập",
                "PID Equations: Dependent and Independent Gains"))
    b.append(p(
        "Phương trình PID tổng quát áp dụng cho các hệ số (PLC) là tổng của bốn số hạng:"))
    b.append(eq("OP = tỉ lệ + tích phân + vi phân + giá trị Bias (Manual)", "8.27"))
    b.append(p(
        "Phương trình này có thể được biểu diễn theo hai cách: ISA (Instrument Society of America) — "
        "độ lợi phụ thuộc — hoặc độ lợi độc lập."))
    b.append(p(
        "Trong phương trình độ lợi độc lập, như tên gọi, cả ba số hạng PID hoạt động độc lập. Trong "
        "phương trình ISA, một thay đổi ở số hạng tỉ lệ cũng ảnh hưởng tới số hạng tích phân và vi phân."))
    b.append(fig(11, F.fig_8_11()))

    b.append(h3("8.13.1 Phương trình ISA", "ISA Equation"))
    b.append(p(
        "Phương trình ISA có tính tương tác. Nghĩa là nó chứa các số hạng phụ thuộc: nếu hệ số khuếch "
        "đại bộ điều khiển K_C thay đổi thì số hạng tích phân và vi phân cũng thay đổi."))
    b.append(eq("CV = K_c [ E + (1/T_int)∫₀ᵗ E dt + T_der · dE/dt ] + Bias", "8.28"))
    b.append(p("hoặc:"))
    b.append(eq("CV = K_c [ E + (1/T_int)∫₀ᵗ E dt + T_der · (PV_(n−1) − PV)/dt ] + Bias", "8.29"))
    b.append(p("trong đó:"))
    b.append(ul([
        "CV — đầu ra;",
        "K_c — hằng số hệ số khuếch đại bộ điều khiển (không thứ nguyên);",
        "T_int — hằng số thời gian tích phân (phút mỗi lần lặp);",
        "T_der — hằng số thời gian vi phân (phút);",
        "dt — thời gian giữa hai lần lấy mẫu (phút);",
        "Bias — giá trị bù theo hướng hoặc bù đầu ra;",
        "E — sai lệch, bằng PV − SP hoặc SP − PV;",
        "PV — biến quá trình;",
        "PV_(n−1) — giá trị PV của lần lấy mẫu trước;",
        "E_(n−1) — giá trị sai lệch của lần lấy mẫu trước."]))

    b.append(h3("8.13.2 Phương trình độ lợi độc lập", "Independent Gains Equation"))
    b.append(p(
        "Phương trình này không tương tác. Do đó các số hạng P, I và D được chỉnh độc lập với nhau."))
    b.append(eq("CV = K_p·E + K_i∫₀ᵗ E dt + K_d · dE/dt + Bias", "8.30"))
    b.append(p("hoặc:"))
    b.append(eq("CV = K_p·E + K_i∫₀ᵗ E dt + K_d · (PV_(n−1) − PV)/dt + Bias", "8.31"))
    b.append(p("trong đó:"))
    b.append(ul([
        "CV — đầu ra;",
        "K_p — hằng số hệ số khuếch đại tỉ lệ (không thứ nguyên);",
        "K_i — hằng số hệ số khuếch đại tích phân (1/giây);",
        "K_d — hằng số hệ số khuếch đại vi phân (giây);",
        "dt — thời gian giữa hai lần lấy mẫu (giây);",
        "Bias, E, PV, PV_(n−1), E_(n−1) — như trên."]))

    b.append(p("Có thể so sánh các hằng số ISA và độ lợi độc lập như sau:"))
    b.append(table(
        ["Hằng số ISA", "Hằng số độ lợi độc lập"],
        [["Hệ số khuếch đại bộ điều khiển K_C (không thứ nguyên)",
          "Hệ số khuếch đại tỉ lệ K_P (không thứ nguyên)"],
         ["Số hạng reset T_INT (phút mỗi lần lặp)",
          "Hệ số khuếch đại tích phân K_i (nghịch giây)"],
         ["Số hạng rate T_DER (phút)",
          "Số hạng vi phân K_d (giây)"]],
        "Bảng 8-5. Đối chiếu hằng số ISA và hằng số độ lợi độc lập."))

    b.append(p("Để chuyển từ số hạng ISA sang số hạng độ lợi độc lập:"))
    b.append(eq("K_p = K_c   (không thứ nguyên)", "8.32"))
    b.append(eq("K_i = K_c / (T_int × 60 giây/phút)", "8.33"))
    b.append(eq("K_d = K_c × T_der × 60 giây", "8.34"))

    b.append(p(
        "Ví dụ trên một bộ điều khiển Allen-Bradley, với tham số 1 là độ lợi phụ thuộc ISA và 0 là độ "
        "lợi độc lập:"))
    b.append(table(
        ["Tham số", "ISA (độ lợi phụ thuộc)", "Độ lợi độc lập"],
        [["Điểm đặt", "SP (đã chia thang)", "SP"],
         ["Hệ số khuếch đại tỉ lệ", "K_C (bước 0,01)", "K_P (bước 0,01)"],
         ["Thời gian reset", "T1 (bước 0,01 phút/lần lặp)", "K_I (bước 0,001 /giây)"],
         ["Tốc độ vi phân", "T2 (bước 0,01 phút)", "K_D (bước 0,01 giây)"],
         ["Chu kỳ cập nhật vòng", "bước 0,01 giây", "bước 0,01 giây"],
         ["Vi phân theo", "0: PV, 1: sai lệch", "0: PV, 1: sai lệch"]],
        "Bảng 8-6. Bảng tham số của một bộ điều khiển PLC thương phẩm."))

    b.append(p("Ví dụ với K_C = 2,2; T_INT = 0,8 phút; T_DER = 0,2 phút:"))
    b.append(eq("K_c = 220   →   K_p = K_c = 220", "8.35"))
    b.append(eq("T_i = 80   →   K_i = K_c / (T_i × 60) × 1000 = 2,2/(0,8 × 60) × 1000 = 45,8", "8.36"))
    b.append(eq("T_d = 20   →   K_d = K_c × T_d × 60 × 100 = 2,2 × 0,2 × 60 × 100 = 2640", "8.37"))
    b.append(p("Ứng dụng dải tỉ lệ PB %:"))
    b.append(eq("PB% = 100 / K_c = 100 / 2,2 = 45,5 %", "8.38"))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bảng 8-6 và ba phép tính trên giữ nguyên hệ số chia thang của "
        "bộ điều khiển gốc (100 cho K_c và K_d, 1000 cho K_i) vì đó là các bước lượng tử của từng tham "
        "số, không phải hệ số vật lý. Bỏ chúng đi sẽ làm ví dụ mất đúng cái giá trị thực dụng: nó cho "
        "thấy cùng một bộ số chỉnh định được lưu dưới hai dạng khác nhau thế nào."))

    b.append(p(
        "Điểm cần mang theo khỏi mục này không phải các công thức chuyển đổi, mà là câu hỏi phải đặt ra "
        "trước khi nhập số: bộ điều khiển đang chờ độ lợi phụ thuộc hay độc lập? Nếu nhập một bộ số "
        "Ziegler-Nichols (vốn được xây dựng cho dạng phụ thuộc) vào một bộ điều khiển độc lập mà không "
        "chuyển đổi, vòng sẽ chạy nhưng không giống bất kỳ dự đoán nào — và người chỉnh định sẽ kết luận "
        "sai rằng phương pháp Ziegler-Nichols không dùng được."))
    b.append(quote(
        "Ba con số chỉ có nghĩa khi biết chúng đang được hiểu theo phương trình nào.",
        "Ý chính của §8.13"))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This is the longest chapter in the control book and the most practical one, and it answers the "
        "question every technician has to answer at least once: how do you arrive at the three numbers "
        "you type into the controller?"))
    b.append(p(
        "Altmann presents four methods and, notably, does not say which one is correct. Each needs "
        "something different from you — a reaction curve, a point of inflection, a period of "
        "oscillation — and each returns a slightly different set of numbers. The technician's job is to "
        "know what evidence is in hand and to accept the uncertainty that comes with it."))

    b.append(h2("What tuning is actually for"))
    b.append(p(
        "The chapter opens with a list of objectives rather than a list of formulas, and the list is "
        "worth reading as a set of competing claims rather than as a checklist. Minimising the integral "
        "of the error asks for speed. Minimum wear asks for stillness. No overshoot at start-up asks for "
        "caution. You cannot have all three, and every tuning method in the chapter is a different "
        "answer to which one to sacrifice."))
    b.append(fig(1, F.fig_8_1(), "en"))
    b.append(p(
        "The distinction between IAE and ISE is the clearest example of the trade being made explicit. "
        "IAE counts every per cent of error for the same amount, however long it lasts. ISE counts a "
        "large error far more heavily than a small one, so a controller tuned to ISE will accept a long "
        "slow tail in exchange for never being badly wrong at the start. Modern self-tuning controllers "
        "work on ISE precisely because a plant cares much more about a two-metre excursion than about a "
        "two-hour one."))
    b.append(fig(2, F.fig_8_2(), "en"))

    b.append(h2("The reaction curve is an experiment, not a measurement"))
    b.append(p(
        "The open-loop methods all rest on one recording: put the controller in manual, step the "
        "output, and watch the process answer. It is worth being explicit that this is an experiment "
        "with consequences. The step must be large enough to be visible above noise and small enough "
        "not to upset the plant, and the chapter's instruction to record it on a chart calibrated in "
        "minutes and fractions of minutes is not pedantry — a strip chart calibrated in seconds makes "
        "the effective lag look ten times larger than it is, and the integral time that follows is "
        "wrong by the same factor."))
    b.append(fig(3, F.fig_8_3(), "en"))
    b.append(p(
        "Three numbers come off that recording and they divide the labour cleanly. The effective lag L "
        "sets the integral time, because L is the delay the integral has to survive. The maximum slope N "
        "sets the gain, because N is the process's own sensitivity expressed in the controller's units. "
        "And because derivative exists to offset what integral destabilises, the derivative time is "
        "always defined as a fraction of the integral time — a quarter of it, in every Ziegler-Nichols "
        "variant in this chapter."))
    b.append(fig(4, F.fig_8_4(), "en"))

    b.append(h2("Method (2), and why the tangent matters"))
    b.append(p(
        "The second open-loop variant is the one to use when the final control element is a valve, "
        "because it works from a valve step rather than an output step. The tangent through the point of "
        "inflection is extended back to the vertical axis, and where it lands gives ∆C — the apparent "
        "change the process would have made if it had responded at its maximum rate from the start. "
        "Dividing the valve step by that apparent change gives PG-u, a gain that already contains the "
        "valve's own characteristic."))
    b.append(fig(5, F.fig_8_5(), "en"))
    b.append(p(
        "The gain ratios in Table 8-2 are the same 1 : 0.9 : 1.2 as in method (1), which is the "
        "chapter's quiet argument that these are not independent discoveries but one relationship "
        "expressed three ways."))

    b.append(h2("The first-order curve and the loop time constant"))
    b.append(p(
        "The third open-loop variant is the only one that asks the process to actually be first order. "
        "That assumption buys a great deal of simplicity: the curve reaches 63.2 % of its final change "
        "in one time constant, and 63.2 % of what remains in each one after that. The tangent at the "
        "origin reaches 100 % in exactly one time constant, which is why the time constant can be read "
        "off the chart without solving anything."))
    b.append(fig(6, F.fig_8_6(), "en"))
    b.append(p(
        "The LTC method then sets the three gains directly: proportional gain is the reciprocal of the "
        "process gain, integral gain equals the loop time constant, derivative gain is a quarter of it. "
        "It is the least fashionable of the four methods and the fastest to apply, and on a genuinely "
        "first-order loop it is as good as anything else in the chapter."))
    b.append(fig(7, F.fig_8_7(), "en"))

    b.append(h2("Hysteresis: when the process answers differently in each direction"))
    b.append(p(
        "Section 8.7 is two pages long and saves more plant time than any other section. If you step the "
        "output up and then step it back down, most real processes will not retrace the same path. A "
        "valve with stiction, a heat exchanger with fouling on one side, a boiler whose heating and "
        "cooling lags differ — all produce a loop that behaves differently in each direction."))
    b.append(p(
        "The instruction is to do both directions and compare. Under five or six per cent difference, "
        "average the two. Above that, tuning to either direction means the loop is mistuned for the "
        "other half of its life, and no amount of PID tuning will fix it — the fix belongs in the "
        "process, which is why the chapter sends the reader forward to the feedforward discussion in "
        "Chapter 11."))

    b.append(h2("Closed loop: finding the edge of stability on purpose"))
    b.append(p(
        "The continuous cycling method is the one everybody knows and the one that frightens everybody, "
        "because it deliberately drives the loop to the edge of instability and measures the period "
        "there. The gain that produces sustained oscillation is K-u; the period is P-u. Everything else "
        "is arithmetic."))
    b.append(p(
        "Two details in the procedure are load-bearing. First, integral and derivative must be disabled "
        "— T-int at 999, T-der at zero — because both add phase shift and the whole point is to measure "
        "the process's phase, not the controller's. Second, the instruction after a growing oscillation "
        "is to stop immediately and reduce the gain, not to watch how far it goes. A loop that is "
        "amplifying is a loop whose gain is above one, and the amplitude grows until something "
        "mechanical gives."))
    b.append(fig(8, F.fig_8_8(), "en"))

    b.append(h2("Damped cycling: the same measurement without the danger"))
    b.append(p(
        "Where continuous cycling is unacceptable — a column, a reactor, anything with a trip — the "
        "damped variant gets the same information from a decaying oscillation instead. You record the "
        "gain that produced a decay, K-d, and the ratio of the first two peaks, and from those you "
        "recover the ultimate gain and period by calculation rather than by observation."))
    b.append(fig(9, F.fig_8_9(), "en"))
    b.append(p(
        "The two charts that carry the arithmetic are worth understanding rather than just using. Figure "
        "8-9 is the exact second-order relation between overshoot and damping ratio; a decay ratio of "
        "one half corresponds to δ near 0.22, and the usual working target of δ around 0.5 corresponds "
        "to about 16 % overshoot. Figure 8-10 converts the same information into the ratio of ultimate "
        "to damped period, which is what the tuning formulas actually need."))
    b.append(fig(10, F.fig_8_10(), "en"))

    b.append(h2("Pessen: buying no-overshoot with gain"))
    b.append(p(
        "Pessen's two variants are not new measurements, only different fractions of the same K-u and "
        "P-u. What they buy is a guarantee at start-up, which is the one moment when a loop transferring "
        "from manual to automatic can be arbitrarily far from its set point. The cost is visible in the "
        "table: gain drops from 0.6 to 0.2 of K-u, and the loop becomes slow enough that disturbances "
        "during normal running are corrected lazily."))
    b.append(p(
        "The chapter's note that start-up is not the same as a set-point change is the reason these "
        "formulas exist at all. A set-point step produces a step in the error and therefore a derivative "
        "kick; a manual-to-auto transfer does not, because the error was already there. Tuning for "
        "start-up is therefore tuning for a large standing error, not for a transient."))

    b.append(h2("Dependent and independent gains: the trap at the keyboard"))
    b.append(p(
        "The last section looks like housekeeping and is in fact where a great many tuning exercises go "
        "wrong. The ISA form has one gain multiplying the whole bracket, so changing it changes all "
        "three actions at once. The independent form has three separate gains, and changing one changes "
        "only that action. The same physical loop described in the two forms needs two different sets of "
        "numbers."))
    b.append(fig(11, F.fig_8_11(), "en"))
    b.append(p(
        "The conversion is simple arithmetic — K-p equals K-c, K-i equals K-c over T-int in seconds, "
        "K-d equals K-c times T-der in seconds — but the arithmetic is only correct if you know which "
        "form the controller is expecting. Enter a Ziegler-Nichols set, which is derived for the "
        "dependent form, into a controller expecting independent gains, and the loop will run; it just "
        "will not behave like anything the method predicted. The usual conclusion at that point is that "
        "the method does not work, when the method was never given a chance."))
    return "".join(b)
