# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 6, Digital Control Principles
(Wolfgang Altmann, IDC Technologies)."""
import pc6fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 16
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Bộ lấy mẫu (sampler)</em> — khối thay cho bộ điều khiển liên tục, thực hiện thuật toán "
            "rời rạc theo chu kỳ. · "
            "<em>Thời gian quét (scan time)</em> — khoảng giữa hai lần tính liên tiếp. · "
            "<em>Thuật toán số gia (incremental algorithm)</em> — chỉ tính lượng thay đổi của đầu ra, "
            "không tính giá trị tuyệt đối. · "
            "<em>Khởi tạo (initialization)</em> — nạp giá trị đầu ra từ khối đích để tránh cú nhảy. · "
            "<em>Khâu lead</em> — vi phân có lọc, dùng thay cho vi phân lý tưởng trong thiết bị thực.")
    return note(
        "<b>Key terms.</b> <em>Sampler</em> — the block that replaces the continuous controller and runs "
        "the discrete algorithm once per scan. · <em>Scan time</em> — the interval between successive "
        "calculations. · <em>Incremental algorithm</em> — computes only the change in output, never its "
        "absolute value. · <em>Initialization</em> — loading the output from the downstream block so "
        "there is no bump. · <em>Lead</em> — filtered derivative, used instead of ideal differentiation.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương này là bản nháp kỹ thuật của mọi thứ đi sau nó. Trước khi bàn tới việc chỉnh định, "
        "cascade hay điều khiển theo hướng, phải trả lời một câu hỏi hẹp hơn nhiều: một bộ điều khiển "
        "số thực sự tính cái gì, bao lâu một lần, và tại sao nó không được phép biết giá trị tuyệt đối "
        "của đầu ra?"))
    b.append(p(
        "Câu trả lời của Altmann là câu trả lời của người viết tài liệu huấn luyện cho kỹ thuật viên nhà "
        "máy: không đi từ lý thuyết điều khiển xuống, mà đi từ sơ đồ khối trong cuốn hướng dẫn của hãng "
        "lên. Vì thế chương nói về khâu lead chứ không nói về nghiệm của phương trình đặc trưng, và nói "
        "về đơn vị của hằng số thời gian theo số lần quét chứ không nói về biến đổi z."))

    b.append(h2("6.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Nhận diện và mô tả dạng toán học của những khối cấu thành quan trọng nhất dùng trong điều "
        "khiển công nghiệp;",
        "Mô tả các nguyên lý áp dụng trong những bộ điều khiển số dựa trên máy tính;",
        "Chỉ ra được thế nào là một chương trình thời gian thực."]))
    b.append(p(
        "Để hiểu rõ nhất các thuật toán điều khiển dùng trong công nghiệp, nên xem xét những khối cấu "
        "thành trước đã."))

    b.append(h2("6.2 Số và tương tự: nhắc lại định nghĩa", "Digital vs Analog"))
    b.append(p(
        "Khi chọn loại hệ điều khiển cần dùng, phải xem xét những lựa chọn tồn tại giữa hệ số và hệ "
        "tương tự. Hệ số tương thích với máy tính, hệ điều khiển phân tán (DCS), bộ điều khiển lập "
        "trình được (PLC) và các bộ điều khiển số."))

    b.append(h3("6.2.1 Định nghĩa tương tự", "Analog Definition"))
    b.append(p(
        "Là những đại lượng hay cách biểu diễn biến thiên trên một dải liên tục. Những biến này có thể "
        "nhận vô số giá trị, trong khi cách biểu diễn số của chính những biến ấy chỉ giới hạn ở những "
        "trạng thái hay giá trị xác định. Hệ tương tự biểu diễn giá trị chính xác hơn, nhưng phải trả "
        "giá: nhiễu cảm ứng hay nhiễu cộng thêm, và khó truyền đi chính xác — đó là hai trong những vấn "
        "đề lớn nhất của loại hệ này."))

    b.append(h3("6.2.2 Định nghĩa số", "Digital Definition"))
    b.append(p(
        "Đây là thuật ngữ dùng để chỉ một đại lượng có những mức rời rạc thay vì một dải liên tục."))

    b.append(h2("6.3 Tác động trong vòng điều khiển số", "Action in Digital Control Loops"))
    b.append(p(
        "Vòng điều khiển số khác vòng điều khiển liên tục — người anh em tương tự của nó — ở chỗ bộ "
        "điều khiển liên tục được thay bằng một <b>bộ lấy mẫu</b>. Đó là một dạng máy tính thực hiện "
        "thuật toán điều khiển rời rạc và lưu lại từng kết quả riêng."))
    b.append(p(
        "Tác động dựa trên việc so sánh hiệu giữa (những) giá trị đã lấy mẫu trước đó với giá trị hiện "
        "tại, rồi sinh ra một đầu ra dùng để tăng hoặc giảm giá trị đầu ra cuối cùng của bộ điều khiển, "
        "kết hợp với bất kỳ chức năng số nào khác đang có (P, hoặc P + I, hoặc P + I + D…)."))

    b.append(h2("6.4 Nhận diện các hàm trong miền tần số", "Identifying Functions in the Frequency Domain"))
    b.append(p(
        "Vì các thuật toán điều khiển thường được viết dưới dạng f(s) — tức một hàm trong miền tần số — "
        "nên ta sẽ xem lại những biểu thức ấy. Đoạn này không nhằm đi vào lý thuyết biến đổi Laplace, "
        "mà chỉ cung cấp hiểu biết tối thiểu về những biểu thức cần thiết để hiểu thành phần của hầu hết "
        "các thuật toán điều khiển. Dưới đây là một bản nhắc lại nhanh và đơn giản."))

    b.append(h3("6.4.1 Nhắc lại khái niệm Laplace", "Laplace Conceptual Revision"))
    b.append(p(
        "Nguyên lý của một phép biến đổi là biến một bài toán khó thành một bài toán dễ hơn, hoặc một "
        "dạng tiện xử lý hơn. Khi đã có kết quả của phép biến đổi, có thể làm phép biến đổi ngược để "
        "xác định nghiệm của bài toán ban đầu. Ví dụ: logarit là một phép biến đổi biến bài toán nhân và "
        "chia thành bài toán cộng và trừ."))
    b.append(p(
        "Biến đổi Laplace làm chức năng tương tự trong việc giải phương trình vi phân. Biến đổi Laplace "
        "của một <b>phương trình vi phân thường tuyến tính</b> cho ra một <b>phương trình đại số tuyến "
        "tính</b>. Phương trình này thường dễ giải hơn nhiều so với phương trình vi phân tương ứng. Khi "
        "đã tìm được nghiệm trong miền Laplace, có thể xác định nghiệm trong miền thời gian tương ứng "
        "bằng phép biến đổi ngược."))
    b.append(p(
        "Hàm Laplace của một hàm miền thời gian f(t) được ký hiệu là F(s) và định nghĩa như sau:"))
    b.append(eq("F(s) = ℒ[f(t)] = ∫₀<sup>∞</sup> f(t)·e<sup>−st</sup> dt"))
    b.append(p("trong đó: ℒ[f(t)] là ký hiệu của phép biến đổi Laplace đặt trong ngoặc; biến s là một "
               "biến phức (s = a + jb) do phép biến đổi đưa vào. Mọi hàm phụ thuộc thời gian trong miền "
               "thời gian đều trở thành hàm của s trong miền Laplace (miền s)."))
    b.append(p(
        "Ví dụ sau minh hoạ một bộ tích phân như một khối tích phân với đầu vào hàm bậc thang: hàm "
        "1/s trong miền tần số được biểu diễn như một phép tính tích phân, và tích phân của 1/s cho ra "
        "1/s². Phụ lục A trình bày một số cặp biến đổi Laplace."))

    b.append(h3("6.4.2 Các khối cơ bản thường dùng", "Common Building Blocks"))
    b.append(p("Những khối được dùng phổ biến nhất là:"))
    b.append(ul([
        "<b>T·s</b> — khối vi phân với hằng số thời gian vi phân;",
        "<b>1/(T·s)</b> — khối tích phân với hằng số thời gian tích phân;",
        "<b>1/(1 + T·s)</b> — khâu trễ bậc một với hằng số thời gian trễ."]))
    b.append(p(
        "Có thể làm việc với những khối này nhờ các định lý biến đổi sơ đồ khối, còn gọi là đại số sơ đồ "
        "khối. Một ví dụ là việc xây dựng thuật toán lead. Thuật toán lead là đạo hàm của thuật toán lag, "
        "trong đó hằng số thời gian vi phân (T<sub>der</sub>) phải lớn hơn đáng kể so với hằng số thời "
        "gian trễ (T<sub>lag</sub>):"))
    b.append(eq("LEAD = DERIVATIVE × LAG = s·T<sub>der</sub> / (1 + s·T<sub>lag</sub>)"))
    b.append(p(
        "Tiếp cận bài toán theo chiều ngược lại, ta sẽ phân tích những thuật toán điều khiển đang có "
        "bằng cách dựng sơ đồ khối từ các khối trên, rồi xem xét cách những khối ấy được hiện thực "
        "trong máy tính số."))
    b.append(p(
        "Hình 6-1 là sơ đồ khối của một bộ điều khiển <b>thực</b>, đúng như loại được dùng làm bộ điều "
        "khiển thứ cấp cuối cùng — bộ điều khiển tại hiện trường — điều khiển trực tiếp biến thực của "
        "quá trình."))
    b.append(fig(1, F.fig_6_1()))
    b.append(p("Công thức theo f(s) cho thuật toán điều khiển dựa trên sơ đồ khối ở Hình 6-1 có thể "
               "viết là:"))
    b.append(eq("OP = K · [(1 + T<sub>int</sub>·s) / (T<sub>int</sub>·s)] · [(1 + T<sub>der</sub>·s) / "
                "(1 + α·T<sub>der</sub>·s)]"))
    b.append(p(
        "với K là hệ số khuếch đại của bộ điều khiển; T<sub>int</sub> là hằng số thời gian tích phân; "
        "T<sub>der</sub> là hằng số thời gian vi phân (lead = α lần lag); và alpha α là hệ số, bằng 8 "
        "cho các ứng dụng huấn luyện. Các bộ điều khiển công nghiệp dùng giá trị từ 8 tới 12 cho 1/α."))
    b.append(fig(2, F.fig_6_2()))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Công thức in trong bản gốc ở trang này <b>là bản scan bị lỗi</b>: "
        "các phân số bị đảo thứ tự ký tự (“Tint s 1+ Tint s * 1 der 1 * T s Tder s OP K +α + =”), nên "
        "không đọc được nguyên văn. Dạng viết lại ở trên là dạng chuẩn của bộ điều khiển thực không "
        "tương tác — PI nối tiếp với một khâu lead — và khớp với sơ đồ khối Hình 6-1 vốn còn đọc được. "
        "Độc giả nào đối chiếu với bản in nên kiểm tra lại chỗ này."))

    b.append(h3("6.4.3 Thuật toán trong miền tần số", "Algorithms in the Frequency Domain"))
    b.append(p(
        "Thuật toán viết trong miền tần số không thể hiện bất kỳ hằng số tĩnh nào. Vì thế các thuật toán "
        "phải được tính độc lập với mọi hằng số. Ví dụ về một hằng số như vậy là vị trí khởi đầu bằng "
        "tay của giá trị OP."))
    b.append(p(
        "Điều này trùng với yêu cầu là mọi phép tính điều khiển động đều phải độc lập với giá trị tuyệt "
        "đối của OP. Yêu cầu ấy có là vì giá trị OP phải được sửa từ phía đích — bộ điều khiển thứ cấp — "
        "nếu đích có khả năng khởi tạo. Ta sẽ xem lại khởi tạo trong chương về điều khiển cascade."))
    b.append(p(
        "Nếu không có khởi tạo, giá trị OP do chính thuật toán điều khiển tính ra (chế độ tự động). Mỗi "
        "lần chuyển từ trạng thái khởi tạo sang chế độ tự động, giá trị OP phải được chấp nhận đúng như "
        "nó đang có. Nếu không sẽ có một “cú nhảy” của OP khi chuyển từ trạng thái bằng tay ban đầu sang "
        "chế độ tự động, và cú nhảy ấy có thể gây xáo trộn quá trình."))

    b.append(h2("6.5 Nhu cầu của điều khiển số", "The Need for Digital Control"))
    b.append(p(
        "Có yêu cầu phải sửa giá trị OP từ những phép tính độc lập khác nhau, như khởi tạo và điều "
        "khiển tự động; vì thế không phép tính nào trong hai phép ấy được phép nắm quyền kiểm soát giá "
        "trị tuyệt đối của OP. Những phép tính này chỉ được phép tăng hoặc giảm một giá trị OP đang có. "
        "Chúng không xác định giá trị tuyệt đối của OP. Do đó giá trị tuyệt đối của OP chỉ phản ánh giá "
        "trị của phía đích."))

    b.append(h3("6.5.1 Thuật toán số gia", "Incremental Algorithms"))
    b.append(p(
        "Chẳng hạn, giá trị OP có thể phản ánh đúng vị trí thực của van, và không phép tính nào được "
        "phép áp một giá trị tuyệt đối lên OP. Chỉ những thay đổi — nghĩa là dịch chuyển của vị trí van — "
        "mới được phép."))
    b.append(p(
        "Cách tiếp cận này dùng cái gọi là <b>thuật toán số gia</b>, trong đó các phép tính điều khiển "
        "tính <b>lượng thay đổi</b> chứ không tính <b>giá trị tuyệt đối</b>. Khi nguyên lý này đã được "
        "thiết lập, có thể dùng nó để tính điều khiển PID thành ba phần riêng: phép tính P, phép tính I "
        "và phép tính D; mỗi phần chỉ tăng (hoặc giảm) giá trị OP mà không cần biết các phép tính mode "
        "điều khiển khác. Mỗi phép tính chỉ đơn thuần tăng (hoặc giảm) OP và không quan tâm tới giá trị "
        "tuyệt đối của OP."))
    b.append(fig(3, F.fig_6_3()))
    b.append(p(
        "Nguyên lý tính OP theo số gia cho điều khiển tự động, dựa trên sơ đồ khối ở Hình 6-2 (bộ điều "
        "khiển lý tưởng):"))
    b.append(eq("OP<sub>n</sub> = OP<sub>n−1</sub> + ΔOP<sub>P</sub> + ΔOP<sub>I</sub> + ΔOP<sub>D</sub>"))
    b.append(p("và dựa trên sơ đồ khối ở Hình 6-1 (bộ điều khiển thực):"))
    b.append(eq("OP<sub>n</sub> = OP<sub>n−1</sub> + ΔOP<sub>p</sub> + ΔOP<sub>i</sub>"))
    b.append(p("trong đó OP<sub>n</sub> là giá trị đầu ra sau lần quét hiện tại; OP<sub>n−1</sub> là giá "
               "trị đầu ra sau lần quét trước; ΔOP<sub>P</sub> là lượng thay đổi đầu ra do tác động tỉ "
               "lệ yêu cầu; ΔOP<sub>I</sub> là lượng thay đổi do tác động tích phân; và "
               "ΔOP<sub>D</sub> là lượng thay đổi do tác động vi phân."))
    b.append(p(
        "Nếu đang ở chế độ điều khiển cascade và có khởi tạo, điểm đặt của bộ điều khiển thứ cấp sẽ dẫn "
        "động đầu ra của bộ điều khiển sơ cấp:"))
    b.append(eq("OP = SP<sub>S</sub>"))
    b.append(p("với SP<sub>S</sub> là điểm đặt của bộ điều khiển thứ cấp."))
    b.append(note(
        "<b>Chú ý.</b> Chữ D (hoặc ký hiệu delta Δ in nghiêng) được dùng làm tiền tố cho tên tham số để "
        "chỉ sự thay đổi của tham số từ phép tính này sang phép tính sau, như DERR, DOP hay DPV. Khoảng "
        "thời gian từ phép tính này tới phép tính sau gọi là <b>thời gian quét</b>. Khi biểu diễn đầy đủ "
        "giá trị của tham số thì không dùng tiền tố, như ERR, OP hay PV."))

    b.append(h2("6.6 Tính toán theo chu kỳ quét", "Scanned Calculations"))
    b.append(p("Máy tính số không thể thực hiện đồng thời một loạt phép tính có liên quan với nhau. Vì "
               "thế người ta thực hiện một chuỗi phép tính lặp lại."))
    b.append(ul([
        "Nếu khoảng lặp giữa các phép tính là không đổi, ta gọi đó là <b>thời gian quét cố định</b>.",
        "Thời gian quét cố định được dùng trong mọi bộ điều khiển thiết kế cho điều khiển liên tục "
        "(điều biến).",
        "Nếu thời gian quét không cố định, như ở một số bộ điều khiển lập trình được (PLC), thì phải "
        "tính thời gian quét cho từng lần quét của hệ máy tính.",
        "Điều này đặc biệt quan trọng, vì mọi hằng số thời gian dùng cho phép tính thực tế (lặp lại) "
        "đều phải dùng theo đơn vị lần quét."]))
    b.append(p("Tóm lại, với các phép tính theo chu kỳ quét:"))
    b.append(ul([
        "Mọi hằng số thời gian đều tính theo <b>đơn vị lần quét</b>.",
        "Mọi hằng số thời gian phải lớn hơn thời gian quét rất nhiều, để bảo đảm phép tính số tương "
        "đương — hoặc xấp xỉ tốt — với phép tính tương tự."]))

    b.append(h2("6.7 Điều khiển tỉ lệ", "Proportional Control"))
    b.append(p("Hãy so sánh công thức tổng quát đã nêu với công thức dùng cho điều khiển P dạng số gia:"))
    b.append(eq("OP = K · ERR + MANUAL"))
    b.append(p("Lấy đạo hàm:"))
    b.append(eq("dOP/dt = K · dERR/dt"))
    b.append(p(
        "Chú ý rằng ta đã mất hằng số MANUAL. Điều đó làm thuật toán này trở thành một phép tính động "
        "thuần tuý. Nếu phản ứng của quá trình là không đáng kể trong khoảng giữa hai lần quét, có thể "
        "đơn giản hoá phép tính thành một phép tính hiệu với khoảng là thời gian quét:"))
    b.append(eq("ΔOP = K · ΔERR"))
    b.append(p("ΔERR là lượng thay đổi của sai lệch từ lần quét trước tới lần quét hiện tại. ERR trong "
               "một phương trình hiệu tương đương với ∫ERR dt trong một phương trình vi phân."))

    b.append(h2("6.8 Điều khiển tích phân", "Integral Control"))
    b.append(p("So sánh công thức tổng quát với công thức dùng cho điều khiển I dạng số gia:"))
    b.append(eq("OP = (K / T<sub>INT</sub>) ∫₀<sup>T</sup> ERR dt"))
    b.append(p("Lấy đạo hàm:"))
    b.append(eq("dOP/dt = (K / T<sub>INT</sub>) · ERR"))
    b.append(p("Nếu phản ứng của quá trình là không đáng kể giữa hai lần quét, có thể đơn giản hoá thành "
               "phép tính hiệu với khoảng là thời gian quét:"))
    b.append(eq("ΔOP = (K / T<sub>INT</sub>) · ERR"))
    b.append(p("trong đó T<sub>INT</sub>[đơn vị quét] = T<sub>INT</sub>[phút] × 60 / SCAN[giây]."))
    b.append(note(
        "<b>Chú ý.</b> T<sub>INT</sub> phải tính theo đơn vị lần quét (hay số lần quét), không phải theo "
        "phút hay giây. Ví dụ, nếu khoảng lặp phép tính (thời gian quét) là 0,5 giây và "
        "T<sub>INT</sub> là 1,5 phút, tức 90 giây, thì T<sub>INT</sub> theo đơn vị quét là 180. Nói cách "
        "khác, T<sub>INT</sub> là 180 đơn vị, mỗi đơn vị dài 0,5 giây."))

    b.append(h2("6.9 Điều khiển vi phân", "Derivative Control"))
    b.append(p("So sánh công thức tổng quát với công thức dùng cho điều khiển D dạng số gia:"))
    b.append(eq("OP = K · T<sub>DER</sub> · (dERR/dt)"))
    b.append(p("Lấy đạo hàm:"))
    b.append(eq("dOP/dt = K · T<sub>DER</sub> · (d²ERR/dt²)"))
    b.append(p("Nếu phản ứng của quá trình là không đáng kể giữa hai lần quét, có thể đơn giản hoá thành "
               "phép tính hiệu với khoảng là thời gian quét:"))
    b.append(eq("ΔOP = K · T<sub>DER</sub> · Δ(ΔERR)"))
    b.append(p("trong đó T<sub>DER</sub>[đơn vị quét] = (T<sub>DER</sub>[phút] × 60) / SCAN[giây]."))
    b.append(note(
        "<b>Chú ý.</b> T<sub>DER</sub> phải tính theo đơn vị lần quét (hay số lần quét). Δ(ΔERR) là "
        "lượng thay đổi của lượng thay đổi sai lệch, từ lần quét trước tới lần quét hiện tại. Δ(ΔERR) "
        "trong một phương trình hiệu tương đương với d²ERR/dt² trong một phương trình vi phân."))

    b.append(h2("6.10 Khâu lead thay cho điều khiển vi phân", "Lead Function as Derivative Control"))
    b.append(p(
        "Thuật toán thực dùng cho bộ điều khiển tại hiện trường không dùng cách tiếp cận lý tưởng và đơn "
        "giản nhất về mặt toán học. Thay vì một tác động vi phân định nghĩa thuần toán học, bộ điều "
        "khiển tại hiện trường dùng một <b>thuật toán lead</b> cho điều khiển vi phân. Sơ đồ khối ở "
        "Hình 6-5; công thức theo f(s) cho bộ điều khiển tại hiện trường dùng thuật toán lead như sau:"))
    b.append(fig(4, F.fig_6_4()))
    b.append(p("tức là: độ lợi × lead × điều khiển PI."))
    b.append(p("Phần LEAD, đóng vai trò điều khiển vi phân, được giải thích chi tiết ở Hình 6-5 dưới đây:"))
    b.append(fig(5, F.fig_6_5()))
    b.append(p(
        "Nếu xét α·T·s = (1/8)·T·s, điều đó có nghĩa khâu vi phân mạnh gấp 8 lần bộ lọc thông thấp. Cách "
        "làm này giữ tác động bất lợi của nhiễu lên thành phần vi phân ở mức tối thiểu chấp nhận được."))

    b.append(h2("6.11 Ví dụ dạng số gia (Siemens S5-100V)", "Example of Incremental Form"))
    b.append(fig(6, F.fig_6_6()))
    b.append(p("Lượng thay đổi đầu ra cho tác động tỉ lệ:"))
    b.append(eq("ΔOP<sub>P</sub> = K × (XW<sub>K</sub> − XW<sub>K−1</sub>) · R"))
    b.append(p("Lượng thay đổi đầu ra cho tác động tích phân:"))
    b.append(eq("ΔOP<sub>I</sub> = K · T<sub>INT</sub> · XW<sub>K</sub>"))
    b.append(p("Lượng thay đổi đầu ra cho tác động vi phân:"))
    b.append(eq("ΔOP<sub>D</sub> = K · T<sub>DER</sub> · [(XW<sub>K</sub> − XW<sub>K−1</sub>) − "
                "(XW<sub>K−1</sub> − XW<sub>K−2</sub>)]"))
    b.append(eq("= K · T<sub>DER</sub> · (XW<sub>K</sub> − 2XW<sub>K−1</sub> + XW<sub>K−2</sub>)"))
    b.append(p("Do đó toàn bộ số gia của đầu ra là:"))
    b.append(eq("ΔΨ<sub>K</sub> = K[(XW<sub>K</sub> − XW<sub>K−1</sub>)·R + T<sub>INT</sub>·XW<sub>K</sub> "
                "+ T<sub>DER</sub>(XW<sub>K</sub> − 2XW<sub>K−1</sub> + XW<sub>K−2</sub>)]"))
    b.append(p(
        "Ký hiệu Ψ ở đây là đầu ra của bộ điều khiển — tương đương OP trong phần còn lại của chương. "
        "Điểm đáng chú ý của dạng này là nó chỉ cần giữ ba mẫu gần nhất của biến vào: XW<sub>K</sub>, "
        "XW<sub>K−1</sub> và XW<sub>K−2</sub>. Không có bộ nhớ dài hạn nào, không có tích phân tích luỹ "
        "nào phải bảo toàn qua thời gian — đó chính là ưu điểm vận hành của thuật toán số gia, và cũng "
        "là lý do nó chịu được việc khởi động lại bộ điều khiển mà không sinh ra cú nhảy."))

    b.append(quote(
        "Một bộ điều khiển số không tính đầu ra. Nó tính xem đầu ra nên dịch đi bao nhiêu.",
        "Ý chính của §6.5"))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This is the shortest chapter in the control book and the one that dates fastest, yet it contains "
        "the idea everything else depends on: a digital controller does not compute an output, it "
        "computes how far the output should move."))
    b.append(p(
        "That distinction sounds like bookkeeping. It is not. Once the output is an accumulated sum of "
        "increments rather than a value owned by one algorithm, several things become possible at once: "
        "initialisation from a downstream block, bumpless transfer between manual and automatic, cascade "
        "where the secondary's set point drives the primary's output, and a restart that does not disturb "
        "the plant. All of them fall out of the same decision."))

    b.append(h2("The two controller forms"))
    b.append(p(
        "The chapter draws the same controller twice. Figure 6-1 is the field controller: proportional, "
        "integral, and a derivative term that is not a differentiator but a lead — a differentiator "
        "followed by a first-order lag with a time constant α times smaller."))
    b.append(fig(1, F.fig_6_1(), "en"))
    b.append(p(
        "Figure 6-2 is the ideal form, the one in the textbooks, where the three terms sit in parallel "
        "and the derivative is exact. The difference matters because an exact differentiator has "
        "unbounded gain at high frequency: it will differentiate the noise on a 4–20 mA signal just as "
        "faithfully as the process variable, and the result is a valve that hunts."))
    b.append(fig(2, F.fig_6_2(), "en"))

    b.append(h2("The lead filter, and why α is 8 to 12"))
    b.append(p(
        "A lead block is a differentiator in series with a lag. Above the lag's corner frequency the "
        "differentiation stops and the gain flattens out at α. That single number — 8 to 12 in industrial "
        "equipment — is the whole design of derivative action in a real controller. It says: differentiate "
        "fast enough to see the process move, but stop differentiating before you reach the noise."))
    b.append(fig(5, F.fig_6_5(), "en"))
    b.append(p(
        "Put the other way round: α is the ratio of how much derivative you would like to how much "
        "derivative you can afford. A controller with α = 8 gives up a factor of eight of high-frequency "
        "gain in exchange for a derivative term that is usable on real wiring."))

    b.append(h2("Scan time is a unit, not a delay"))
    b.append(p(
        "The most practically important section is the shortest. Every time constant in the discrete "
        "algorithm has to be expressed in units of the scan, not in seconds: T_INT in scans is "
        "T_INT in minutes times 60 divided by the scan in seconds. A 1.5-minute integral time on a "
        "0.5-second scan is 180 — not 90, and not 1.5."))
    b.append(p(
        "The second rule is a design constraint: every time constant must be far greater than the scan "
        "time, or the difference equation stops approximating the differential equation it came from. A "
        "rule of thumb that appears throughout the literature is ten samples per time constant; below "
        "that, the discrete controller's phase lag starts to eat the stability margin the tuning was "
        "supposed to provide."))
    b.append(p(
        "This is also where fixed-scan and variable-scan controllers part company. A modulating "
        "controller runs a fixed scan, so the constants can be pre-computed once. A PLC's scan varies "
        "with program length and I/O count, so the constants must be recomputed every scan — and a "
        "chapter that assumes a fixed scan will mislead anyone implementing PID in a PLC."))

    b.append(h2("Increments, and the figures that follow"))
    b.append(fig(3, F.fig_6_3(), "en"))
    b.append(p(
        "Figure 6-3 shows what the incremental form actually computes: at each scan the controller looks "
        "at how much the error changed since the last scan, multiplies by the gain, and adds the result "
        "to whatever the output already is. The output never appears as an absolute number inside the "
        "algorithm. It is read from the destination, nudged, and written back."))
    b.append(p(
        "The Siemens S5 example in Figure 6-6 is worth reading as an implementation rather than as "
        "arithmetic. Three differences are formed — first difference for proportional, second difference "
        "for derivative, the sample itself for integral — each scaled and summed into one increment. The "
        "controller holds three samples of the input and nothing else. That is why it can be restarted "
        "mid-shift without a bump: there is no accumulated state to lose."))
    b.append(fig(6, F.fig_6_6(), "en"))

    b.append(h2("What has changed since 1999"))
    b.append(p(
        "The arithmetic has not. What has changed is where it runs. In 1999 the incremental form was the "
        "native idiom of a DCS or a PLC function block, and the ideal parallel form was what you got in a "
        "standalone controller. Today almost every loop is executed inside a PLC or a DCS with a fixed "
        "task, and the ideal form is routinely implemented with an internal anti-windup and a derivative "
        "filter — which is to say, the field controller of Figure 6-1 has won, and the textbook form of "
        "Figure 6-2 survives mainly as a way of explaining it."))
    b.append(p(
        "The Vietnamese translation reconstructs two formulas that the source PDF renders as scrambled "
        "character strings, and flags both in a translator's note. The block diagrams those formulas "
        "describe are legible in the original, so the reconstruction is checkable against them."))
    return "".join(b)
