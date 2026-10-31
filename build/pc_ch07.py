# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 7, Real and Ideal P.I.D. Controllers
(Wolfgang Altmann, IDC Technologies)."""
import pc7fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 8
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Bộ điều khiển không tương tác (non-interactive)</em> — dạng lý tưởng, ba khâu P, I, D "
            "tính riêng rồi cộng. · "
            "<em>Bộ điều khiển tương tác (interactive)</em> — dạng thực, PI mắc nối tiếp với khâu lead, "
            "không tách được ba khâu. · "
            "<em>Biến quá trình lý tưởng</em> — biến đã qua mô hình hoá, lọc thống kê và dự đoán, không "
            "đến trực tiếp từ cảm biến. · "
            "<em>Hằng số thời gian lọc PV (T_D)</em> — hằng số của bộ lọc thông thấp đặt trước khâu vi "
            "phân. · "
            "<em>PB</em> — dải tỉ lệ, tính bằng phần trăm.")
    return note(
        "<b>Key terms.</b> <em>Non-interactive controller</em> — the ideal form, where P, I and D are "
        "computed separately and added. · <em>Interactive controller</em> — the real form, where a PI "
        "block is followed by a lead and the three terms cannot be separated. · <em>Ideal process "
        "variable</em> — a variable that has been modelled, statistically filtered and predicted, not "
        "taken raw from a sensor. · <em>PV filter time constant (T_D)</em> — the low-pass placed ahead "
        "of the derivative. · <em>PB</em> — proportional band, in percent.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương trước đã dựng ra hai dạng của cùng một bộ điều khiển và nói rằng dạng thứ hai — khâu "
        "lead — là dạng dùng ngoài hiện trường. Chương này quay lại câu hỏi đó ở một góc khác: không "
        "phải “bộ điều khiển tính gì”, mà “vì sao cùng một luật PID lại phải tồn tại dưới hai dạng, và "
        "khi nào thì dùng dạng nào”."))
    b.append(p(
        "Altmann gọi hai dạng bằng hai cái tên mang tính sử dụng chứ không mang tính toán học: dạng "
        "<em>không tương tác</em> (non-interactive) và dạng <em>tương tác</em> (interactive). Cái tên "
        "không mô tả hình thức của công thức mà mô tả chỗ đứng của thiết bị: bộ điều khiển có nối trực "
        "tiếp với dây tín hiệu ngoài hiện trường hay không. Đó cũng chính là ranh giới quyết định cả "
        "chương."))

    b.append(h2("7.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Chọn đúng thuật toán điều khiển PID cho trường hợp có tương tác với hiện trường và cho trường "
        "hợp tính toán đã được tối ưu trên máy tính;",
        "Phân biệt rõ ràng giữa nhiễu quá trình và mất ổn định của vòng điều khiển — hai hiện tượng "
        "thường trông rất giống nhau;",
        "Liệt kê đúng trình tự các bước để xử lý hai loại vấn đề nhiễu và mất ổn định."]))

    b.append(h2("7.2 So sánh hai loại bộ điều khiển", "Comparative Descriptions of Real and Ideal Controllers"))
    b.append(p(
        "Bộ điều khiển PID lý tưởng không thích hợp để nối trực tiếp với hiện trường, vì vậy nó được "
        "gọi là bộ điều khiển <em>không tương tác</em>. Nó phản ứng rất mạnh với nhiễu điện trên đầu "
        "vào PV nếu chức năng vi phân được bật."))
    b.append(p(
        "Bộ điều khiển PID thực được thiết kế riêng cho việc nối trực tiếp với hiện trường, nên được "
        "gọi là bộ điều khiển <em>tương tác</em>. Nhờ bộ lọc bên trong khâu vi phân, ảnh hưởng của "
        "nhiễu điện trên đầu vào PV giảm đi rất nhiều."))
    b.append(p(
        "Câu “phản ứng rất mạnh với nhiễu” là câu quan trọng nhất của cả chương, và nó không phải một "
        "lời cảnh báo chung chung. Vi phân lý tưởng có hệ số khuếch đại tỉ lệ với tần số, không có "
        "trần: một nhiễu 50 Hz trên dây tín hiệu bị khuếch đại gấp 314 lần so với một nhiễu 0,16 Hz. "
        "Trong khi đó, tín hiệu quá trình thật hiếm khi có nội dung hữu ích ở trên vài phần mười "
        "hertz. Bộ điều khiển lý tưởng không phân biệt được hai thứ đó — nó chỉ thấy độ dốc."))

    b.append(h2("7.3 Mô tả bộ điều khiển IDEAL (không tương tác)",
                "Description of the IDEAL or the Non-Interactive PID Controller"))
    b.append(p(
        "Dạng không tương tác là mô hình PID cổ điển dùng để giảng dạy. Nó giúp học viên hiểu rõ điều "
        "khiển P, I và D, bởi vì:"))
    b.append(p(
        "điều khiển P, điều khiển I và điều khiển D có thể được xem xét độc lập với nhau."))
    b.append(p(
        "Khi đó PID thực chất là tổ hợp của ba tác động điều khiển P, I và D độc lập. Điều này thấy "
        "được trên Hình 7-1."))
    b.append(fig(1, F.fig_7_1()))

    b.append(p(
        "Vì các thuật toán P, I và D được tính độc lập trong bộ điều khiển PID lý tưởng, dạng này được "
        "khuyến nghị khi tồn tại một biến quá trình lý tưởng."))

    b.append(h3("7.3.1 Biến quá trình lý tưởng", "Ideal Process Variables"))
    b.append(p(
        "Biến quá trình lý tưởng là biến không có nhiễu, đã được làm sạch, tinh luyện và tối ưu. Chúng "
        "là kết quả của việc tối ưu hoá trên máy tính, mô hình hoá quá trình, lọc thống kê và các "
        "thuật toán dự đoán giá trị."))
    b.append(p(
        "Loại biến quá trình lý tưởng này không đến từ cảm biến ngoài hiện trường."))
    b.append(p(
        "Trong những trường hợp đó, việc công thức thực tế của thuật toán PID lý tưởng đơn giản là một "
        "lợi thế lớn, như Hình 7-2 dưới đây:"))
    b.append(fig(2, F.fig_7_2()))

    b.append(p(
        "Cần lưu ý rằng “không đến từ cảm biến ngoài hiện trường” không có nghĩa là biến đó không tồn "
        "tại. Nó có nghĩa là giá trị được đưa vào bộ điều khiển đã qua một tầng xử lý: một mô hình mềm "
        "tính nhiệt trị từ thành phần khí, một bộ lọc Kalman ước lượng lưu lượng từ chênh áp, một phép "
        "hồi quy dự đoán điểm sương. Những biến này trơn, liên tục và không có nhiễu tần số cao, nên "
        "vi phân lý tưởng không gây hại. Đó là toàn bộ lý do tồn tại của dạng không tương tác."))

    b.append(h2("7.4 Mô tả bộ điều khiển PID thực (tương tác)",
                "Description of the Real (Interactive) PID Controller"))
    b.append(p(
        "Dạng tương tác là thuật toán PID dùng cho điều khiển trực tiếp ngoài hiện trường. Nghĩa là "
        "một hoặc cả hai đầu của nó — đầu vào (PV) và đầu ra (MV) — được nối trực tiếp với thiết bị "
        "hiện trường hoặc thiết bị quá trình. Nó được thiết kế để chịu được mọi nhiễu điện cảm ứng vào "
        "mạch của nó từ các thiết bị trong nhà máy."))
    b.append(p(
        "Hiểu đầy đủ thuật toán PID tương tác thì khá khó, bởi vì điều khiển P, điều khiển I và điều "
        "khiển D không thể xem xét độc lập với nhau. Do đó PID tương tác không phải chỉ là tổng của "
        "ba tác động P, I và D độc lập."))
    b.append(p("Điều này thấy được trên Hình 7-3 dưới đây:"))
    b.append(fig(3, F.fig_7_3()))

    b.append(p(
        "Vì bộ điều khiển PID tương tác dùng thuật toán lead thay cho vi phân toán học cổ điển, nó phù "
        "hợp nhất với biến quá trình thực (xuất phát từ hiện trường)."))

    b.append(h3("7.4.1 Biến quá trình thực (xuất phát từ hiện trường)", "Real Process Variables (Field Originated)"))
    b.append(p(
        "Biến quá trình thực có nhiễu điện đến từ cảm biến ngoài hiện trường hoặc từ cáp nối."))
    b.append(p(
        "Vì vậy, việc thuật toán PID có sẵn một mức giảm nhiễu nào đó bên trong là một lợi thế lớn."))
    b.append(p("Công thức dưới đây biểu diễn thuật toán PID tương tác:"))
    b.append(fig(4, F.fig_7_4()))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> Công thức in ở trang này trong bản gốc <b>là bản scan bị lỗi</b>: "
        "các phân số bị đảo thứ tự ký tự (“T s + T s / T s T s … der der int 1 int … c … α”), nên không "
        "đọc được nguyên văn. Dạng viết lại ở Hình 7-4 là dạng chuẩn của bộ điều khiển thực: một khâu "
        "PI nối tiếp với một khâu lead, đúng như dòng chú thích còn đọc được trong bản gốc — "
        "“OP = Gain * Lead * PI-Control” — và đúng như sơ đồ khối Hình 7-3. Bản gốc cũng in nhầm số hạng "
        "bậc nhất của mẫu số thành α·T_der·s; dạng chuẩn dùng α·T_der·s + 1, với α là tỉ số giữa hằng "
        "số thời gian vi phân và hằng số thời gian lọc."))

    b.append(h2("7.5 Hàm lead — điều khiển vi phân có lọc",
                "Lead Function — Derivative Control with filter"))
    b.append(p(
        "Đoạn dưới đây trích từ Chương 6 (Các nguyên lý điều khiển số) để nhắc lại phần LEAD đóng vai "
        "trò hàm vi phân."))
    b.append(p(
        "Bộ điều khiển ngoài hiện trường dùng thuật toán lead cho điều khiển vi phân. Sơ đồ khối được "
        "cho trên Hình 7-5."))

    b.append(h3("7.5.1 Thuật toán lead cho điều khiển vi phân (bộ điều khiển PID thực)",
                "Lead Algorithm for Derivative Control (Field or Real PID Controller)"))
    b.append(fig(5, F.fig_7_5()))

    b.append(p(
        "Hình 7-6 cho thấy vì sao khâu lead là câu trả lời đúng cho bài toán nhiễu. Trên thang log-log, "
        "vi phân lý tưởng là một đường thẳng dốc 20 dB mỗi thập kỷ, không có điểm dừng: tần số càng "
        "cao, khuếch đại càng lớn. Khâu lead bám theo đường đó ở vùng tần số thấp — nơi có nội dung "
        "thật của quá trình — rồi nằm ngang ở mức α. Với α = 8, khâu lead bỏ đi 18 dB khuếch đại ở "
        "vùng nhiễu so với vi phân lý tưởng, và đó chính là khoảng cách giữa một vòng điều khiển chạy "
        "được và một van liên tục rung."))
    b.append(fig(6, F.fig_7_6()))

    b.append(h2("7.6 Tác động vi phân và ảnh hưởng của nhiễu",
                "Derivative Action and Effects of Noise"))
    b.append(p(
        "Khác biệt quan trọng nhất giữa bộ điều khiển PID KHÔNG TƯƠNG TÁC và TƯƠNG TÁC là mức ảnh "
        "hưởng khác nhau của nhiễu lên đầu ra bộ điều khiển. Cần nhớ rằng điều khiển vi phân "
        "<em>nhân</em> nhiễu lên."))

    b.append(h3("7.6.1 Giới thiệu về yêu cầu lọc", "Introduction to Filter Requirements"))
    b.append(p(
        "Cả bộ điều khiển PID không tương tác và PID tương tác đều dùng một bộ lọc nhiễu cho nhiễu "
        "quá trình (gọi là hằng số thời gian lọc biến quá trình T_D)."))
    b.append(p(
        "Vì điều khiển vi phân của PID không tương tác không có khả năng tự triệt nhiễu, nhiễu sẽ "
        "luôn là vấn đề lớn, kể cả khi có dùng bộ lọc biến quá trình."))
    b.append(p(
        "Vì điều khiển vi phân của PID tương tác đã có sẵn một mức triệt nhiễu, nhiễu không thành vấn "
        "đề lớn như vậy, và càng ít hơn nếu dùng thêm bộ lọc biến quá trình."))
    b.append(p(
        "Khuyến nghị là nên dùng bộ lọc PV trong mọi trường hợp có sử dụng điều khiển vi phân. Tác giả "
        "đã quan sát nhiều hệ điều khiển vi phân có đầu ra bộ điều khiển chuyển động quá mức chỉ vì "
        "thiếu bộ lọc PV."))
    b.append(p(
        "Loại vấn đề này thường bị nhân viên trong nhà máy hiểu nhầm thành vấn đề ổn định."))
    b.append(p("Do đó một nguyên tắc quan trọng là:"))
    b.append(quote(
        "Phải phân biệt rõ ràng giữa nhiễu và mất ổn định trong các ứng dụng điều khiển công nghiệp.",
        "Nguyên tắc của chương"))
    b.append(p(
        "Như đã bàn ở trên, nhiễu và mất ổn định cần được xử lý bằng những phương pháp khác nhau, vì "
        "chúng là hai vấn đề hoàn toàn khác nhau."))
    b.append(p(
        "Cần nhớ rằng BỘ LỌC BIẾN QUÁ TRÌNH, do tác động TRỄ của nó, làm giảm nhiễu nhưng có thể làm "
        "tăng thêm tính mất ổn định của vòng điều khiển."))

    b.append(p(
        "Hình 7-7 đặt hai hiện tượng cạnh nhau. Bên trái là nhiễu: biên độ không đổi, tần số cao, do "
        "dây dẫn và cảm biến. Bên phải là mất ổn định: biên độ tăng dần theo thời gian, tần số thấp, "
        "do chính vòng kín. Người vận hành nhìn trend thấy cả hai đều “rung” và gọi cả hai là “bộ điều "
        "khiển hỏng”. Nhưng tăng hằng số thời gian lọc sẽ chữa được cái bên trái và làm cái bên phải "
        "tệ hơn."))
    b.append(fig(7, F.fig_7_7()))

    b.append(p(
        "Hình 7-8 lượng hoá cái giá của bộ lọc. Ba đường là đáp ứng của cùng một bậc thang qua ba hằng "
        "số lọc khác nhau. Không có bữa trưa miễn phí nào ở đây: độ trơn của tín hiệu và độ trễ của "
        "tín hiệu là cùng một đại lượng, chỉ đổi đơn vị. Một bộ lọc đủ mạnh để dập nhiễu 5 Hz cũng đủ "
        "trễ để ăn mất biên dự trữ mà việc chỉnh định vừa mang lại."))
    b.append(fig(8, F.fig_7_8()))

    b.append(h3("Bài tập 5 — Nhập môn điều khiển vi phân", "Exercise 5 — Introduction to Derivative Control"))
    b.append(p(
        "Về chủ đề điều khiển D trong bộ điều khiển PID không tương tác và tương tác, và ý nghĩa của "
        "nhiễu."))

    b.append(h2("7.7 Ví dụ về thuật toán PID của bộ điều khiển KENT K90",
                "Example of the KENT K90 Controllers PID Algorithms"))
    b.append(p(
        "Bản gốc trình bày một bộ điều khiển thương phẩm cụ thể — KENT K90 — để cho thấy các hệ số rời "
        "rạc được tính từ những tham số mà người chỉnh định thật sự nhìn thấy: dải tỉ lệ PB, thời gian "
        "tích phân IAT, thời gian vi phân DAT và chu kỳ quét."))
    b.append(p("Điều khiển tỉ lệ:"))
    b.append(eq("K1 = 100 / PB", "7.1"))
    b.append(p("Điều khiển tích phân:"))
    b.append(eq("K2 = (100 / PB) · (chu kỳ quét / IAT)", "7.2"))
    b.append(p("Điều khiển vi phân:"))
    b.append(eq("K3 = (100 / PB) · (DAT / chu kỳ quét)", "7.3"))
    b.append(p("Ba thành phần:"))
    b.append(eq("P = K1 · ERR", "7.4"))
    b.append(eq("I_N = I_(N−1) + K2 · (SP − MV_N) / dải MV", "7.5"))
    b.append(eq("D = K3 · (MV_(N−1) − MV_N) / dải MV", "7.6"))
    b.append(p("Kết quả:"))
    b.append(eq("OP = P + I + D = (100/PB) · [ ERR + (1/IAT)∫ERR dt + DAT · dPV/dt ]", "7.7"))
    b.append(fig(9, F.fig_7_9()))

    b.append(p(
        "Ba chi tiết trong ví dụ này đáng dừng lại, vì chúng không phải chi tiết của riêng KENT."))
    b.append(ol([
        "Hệ số tích phân K2 tỉ lệ nghịch với IAT nhưng tỉ lệ thuận với chu kỳ quét. Đây chính là quy "
        "tắc đổi đơn vị đã nói ở Chương 6: hằng số thời gian tích phân phải được biểu diễn bằng số "
        "lần quét, không phải bằng giây.",
        "Thành phần vi phân lấy hiệu của PV, không lấy hiệu của sai lệch. Đây là cách tránh cú đập "
        "vi phân (derivative kick) khi người vận hành thay đổi điểm đặt: nếu vi phân tác động lên sai "
        "lệch, một bước nhảy của SP sẽ tạo ra một xung vi phân khổng lồ trong đúng một chu kỳ quét.",
        "Cả hai thành phần I và D đều được chia cho dải MV. Đây là cách đưa đầu ra về đơn vị phần "
        "trăm hành trình, để cùng một bộ điều khiển có thể lái những cơ cấu chấp hành có dải khác "
        "nhau mà không phải chỉnh lại hệ số."]))

    b.append(p(
        "Đọc ví dụ này cùng với Hình 7-6 sẽ thấy hai dạng bộ điều khiển không đối lập nhau về mặt kỹ "
        "thuật mà đối lập nhau về mặt hoàn cảnh. KENT K90 là một bộ điều khiển ngoài hiện trường: nó "
        "nhận 4–20 mA từ một cặp nhiệt điện qua một đoạn cáp dài trong nhà máy có nhiều biến tần, nên "
        "nó phải có khâu lead và bộ lọc PV. Một bộ điều khiển trong DCS nhận PV đã qua bộ lọc kỹ thuật "
        "số và mô hình mềm thì có thể dùng dạng lý tưởng mà không gặp vấn đề gì."))
    b.append(quote(
        "Nhiễu không phải thuộc tính của bộ điều khiển. Nó là thuộc tính của đường dây dẫn tới bộ điều "
        "khiển.",
        "Ý chính của §7.6"))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "The previous chapter drew the same controller twice and said that the second drawing — the "
        "lead — is the one that lives in the field. This chapter asks the question from the other side: "
        "not what the controller computes, but why one PID law has to exist in two shapes at all, and "
        "how you decide which shape you are holding."))
    b.append(p(
        "Altmann names the two shapes by where the instrument sits, not by what the algebra looks like. "
        "Non-interactive and interactive describe the wiring, and the wiring is what decides everything "
        "else in the chapter."))

    b.append(h2("Two names for the same law"))
    b.append(p(
        "The ideal form is the teaching model. Three branches, three gains, three time constants, and "
        "the student can point at each one and say what it does. That legibility is not a cosmetic "
        "property: it is why the ideal form survives in textbooks a century after anybody stopped "
        "building it into a panel instrument."))
    b.append(fig(1, F.fig_7_1(), "en"))
    b.append(p(
        "The interactive form is what you get when the same law has to survive a cable. Proportional "
        "and integral are computed together as a PI block, and derivative is not a differentiator at "
        "all but a lead — a differentiator followed by a first-order lag whose time constant is α times "
        "smaller. You can no longer point at a term and say what it does alone, because the three "
        "actions interact: changing the integral time moves the corner frequency of the lead as well."))
    b.append(fig(3, F.fig_7_3(), "en"))

    b.append(h2("What noise actually does to a derivative"))
    b.append(p(
        "The claim in the chapter is that derivative action multiplies noise. It is worth being precise "
        "about the arithmetic, because the precision is what turns the claim into a design rule. An "
        "ideal differentiator has a gain that rises linearly with frequency, without limit. A 50 Hz "
        "component is amplified 314 times more than a 0.16 Hz component. Process signals of interest "
        "rarely carry useful information above a few tenths of a hertz."))
    b.append(fig(6, F.fig_7_6(), "en"))
    b.append(p(
        "The lead flattens that gain at α. With α between 8 and 12, which is what industrial equipment "
        "uses, the derivative stops differentiating somewhere above the corner frequency and the "
        "high-frequency gain settles at a finite number instead of running away. Figure 7-6 puts the "
        "two asymptotes on the same log-log axes; the gap between them at the right-hand edge is the "
        "entire engineering content of the word “filtered”."))

    b.append(h2("Noise and instability are not the same fault"))
    b.append(p(
        "This is the observation I would keep if I could keep only one thing from the chapter. A "
        "controller output that moves too much is diagnosed as instability almost every time, and the "
        "remedy applied is a change of tuning. If the cause was noise, the remedy makes it worse: "
        "slowing the loop down does not remove the noise, it only makes the resulting wander slower and "
        "larger."))
    b.append(fig(7, F.fig_7_7(), "en"))
    b.append(p(
        "The two faults separate cleanly on a trend if you look at the envelope rather than the "
        "amplitude. Noise has a constant envelope and a frequency set by the electrical environment — "
        "mains, variable-speed drives, contactor chatter. Instability has a growing or decaying "
        "envelope and a frequency set by the loop itself, usually well below one hertz. Noise responds "
        "to filtering. Instability responds to tuning. Applying either remedy to the other fault is how "
        "a small problem becomes a shift-long one."))

    b.append(h2("The filter is not free"))
    b.append(p(
        "A PV filter is a first-order lag, and a first-order lag is phase. Adding a filter therefore "
        "spends stability margin to buy noise rejection, and the exchange rate is fixed by physics, not "
        "by the instrument vendor. Every filter time constant you add is a time constant the loop must "
        "now carry on top of the process's own."))
    b.append(fig(8, F.fig_7_8(), "en"))
    b.append(p(
        "The practical rule that follows is to filter no more than the noise requires, and to place the "
        "filter where it does the least harm. Filtering the PV ahead of the derivative is nearly free, "
        "because the derivative is what needs the protection. Filtering the PV ahead of the "
        "proportional term is expensive, because the proportional term is what gives the loop its "
        "speed. Most field controllers offer only the first, which is the right default."))

    b.append(h2("The KENT K90 as an implementation, not an equation"))
    b.append(p(
        "The worked example at the end of the chapter is worth reading as a specimen of how a real "
        "product translates the three tuning constants a technician can see — proportional band, "
        "integral time, derivative time — into three numbers a scan can multiply by. Three details "
        "generalise well beyond KENT."))
    b.append(fig(9, F.fig_7_9(), "en"))
    b.append(ul([
        "The integral gain is proportional to the scan period. Change the scan and every integral time "
        "in the plant silently changes with it — which is the practical reason a controller that runs "
        "on a variable scan needs its constants recomputed each pass.",
        "The derivative is taken on the measurement, not on the error. A step change in set point would "
        "otherwise produce a derivative spike of unbounded height in a single scan, and the valve would "
        "take it.",
        "Both integral and derivative are normalised by the output range, so the same tuning numbers "
        "drive actuators of different spans without rescaling."]))
    b.append(p(
        "The Vietnamese translation reconstructs the algorithm from a scrambled scan: the fraction bars "
        "and subscripts in the source PDF are rendered as a run of characters, so the printed formula "
        "cannot be read literally. The reconstruction follows the two things in the source that are "
        "still legible — the caption line “OP = Gain * Lead * PI-Control” and the block diagram — and "
        "the translator's note on the page says so explicitly rather than silently repairing the text."))
    return "".join(b)
