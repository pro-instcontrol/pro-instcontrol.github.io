# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 12, Long Process Dead-Time in Closed Loop
Control and the Smith Predictor (Wolfgang Altmann, IDC Technologies)."""
import pc12fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 9
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Thời gian chết (dead time)</em> — khoảng thời gian từ khi thay đổi biến điều khiển đến "
            "khi PV bắt đầu đáp ứng. · "
            "<em>Thời gian chết dài</em> — lớn hơn 20 % tổng thời gian để PV ổn định ở giá trị mới. · "
            "<em>Giảm chỉnh (de-tune)</em> — làm bộ điều khiển chậm lại để nó không bù quá mức. · "
            "<em>Mô hình không trễ</em> — phần động học của quá trình, không kể thời gian chết. · "
            "<em>PV dự báo (PV*)</em> — tín hiệu phản hồi đã sửa, không còn thời gian chết. · "
            "<em>Smith Predictor</em> — chiến lược dùng mô hình để đưa thời gian chết ra ngoài vòng kín.")
    return note(
        "<b>Key terms.</b> <em>Dead time</em> — the interval between a change in the manipulated variable "
        "and the first movement of the PV. · <em>Long dead time</em> — more than 20 per cent of the total "
        "time the PV takes to settle at its new value. · <em>De-tuning</em> — slowing the controller down "
        "so it cannot over-compensate. · <em>Undelayed model</em> — the process dynamics without the dead "
        "time. · <em>Predicted PV (PV*)</em> — the corrected feedback signal with the dead time removed. · "
        "<em>Smith predictor</em> — the strategy that uses a model to move the dead time outside the loop.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chín chương vừa qua đã dạy cách điều khiển một quá trình phản ứng nhanh. Chương này nói về điều "
        "xảy ra khi quá trình không phản ứng ngay: khi có một khoảng thời gian — có khi tới mười phút — "
        "mà trong đó bộ điều khiển đã hành động nhưng chưa thể biết hành động của mình có đúng hay "
        "không."))
    b.append(p(
        "Đó không phải một khó khăn định lượng mà là một khó khăn về bản chất. Trong mười phút ấy, mọi "
        "vòng phản hồi đều đang bay mù. Chương này trình bày cách một kỹ sư giỏi nhất có thể làm — giảm "
        "tốc độ bộ điều khiển — và sau đó trình bày ý tưởng của O.J.M. Smith năm 1957: nếu không quan sát "
        "được quá trình, hãy dựng một mô hình của nó và quan sát mô hình."))

    b.append(h2("12.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Trình bày được cách dùng đúng một mô phỏng quá trình để dự báo biến quá trình;",
        "Trình bày được cách xử lý đúng các vòng điều khiển có thời gian chết dài;",
        "Liệt kê được các thủ tục chỉnh định cho vòng điều khiển có thời gian chết dài."]))

    b.append(h2("12.2 Thời gian chết của quá trình", "Process Deadtime"))
    b.append(p(
        "Khắc phục thời gian chết trong một vòng điều khiển phản hồi có thể là một trong những bài toán "
        "khó nhất đối với người thiết kế hệ điều khiển. Điều này đặc biệt đúng nếu thời gian chết lớn hơn "
        "20 % tổng thời gian cần để PV ổn định ở giá trị mới sau một thay đổi điểm đặt."))
    b.append(p(
        "Ta đã thấy rằng một hệ điều khiển có ít hoặc không có thời gian chết cho ta một bộ thuật toán "
        "đơn giản và dễ áp dụng; khi áp dụng đúng, chúng cho ra những đặc tính vòng rất ổn định. Tiếc "
        "thay, nếu khoảng thời gian từ lúc biến điều khiển (đầu ra bộ điều khiển) thay đổi đến lúc phát "
        "hiện được sự thay đổi của PV là quá lớn, thì bất kỳ nỗ lực nào nhằm tác động lên biến quá trình "
        "trước khi thời gian chết trôi qua đều sẽ tất yếu gây ra vận hành không ổn định cho vòng điều "
        "khiển."))
    b.append(p(
        "Hình 12-1 minh hoạ các thời gian chết khác nhau và quan hệ của chúng với thời gian phản ứng của "
        "PV."))
    b.append(fig(1, F.fig_12_1()))
    b.append(p(
        "Điều đáng chú ý trong hình này là thời gian chết <em>không</em> làm thay đổi hình dạng đường "
        "cong. Ba đường có cùng một hằng số thời gian; chúng chỉ bị đẩy sang phải những khoảng khác "
        "nhau. Nói cách khác, thời gian chết không làm quá trình chậm hơn — nó làm quá trình <b>trả lời "
        "muộn hơn</b>. Đó là hai chuyện khác nhau, và sự khác nhau ấy chính là toàn bộ vấn đề của "
        "chương này."))
    b.append(p(
        "Một quá trình chậm thì bộ điều khiển có thể chờ. Một quá trình trả lời muộn thì bộ điều khiển "
        "không biết là phải chờ — nó thấy sai lệch, nó hành động, và nó thấy sai lệch vẫn còn nguyên. "
        "Không có thông tin nào cho nó biết rằng hành động trước đó đã bắt đầu có tác dụng."))

    b.append(h2("12.3 Một ví dụ về thời gian chết của quá trình",
                "An Example of Process Deadtime"))
    b.append(p(
        "Thời gian chết của quá trình xuất hiện trong hầu như mọi loại quá trình, do phép đo PV nằm cách "
        "xa cơ cấu chấp hành — cả về mặt vật lý lẫn về mặt thời gian — so với cơ cấu chấp hành được điều "
        "khiển bởi biến điều khiển."))
    b.append(p(
        "Một ví dụ là việc vận chuyển vật liệu trên mặt đất từ một phễu nạp tới một quá trình cuối nằm "
        "cách đó một quãng. Phần tới hạn của vận hành là phát hiện lượng vật liệu đến cuối hành trình — "
        "tức cuối băng tải — và từ đó thực hiện hai chức năng:"))
    b.append(ul([
        "“Báo” cho quá trình đang chạy biết có bao nhiêu vật liệu đang tới, và",
        "Điều chỉnh tốc độ nạp của phễu ở đầu kia của băng."]))
    b.append(p(
        "Hình 12-2 minh hoạ bài toán này. Bộ điều khiển đang đo trọng lượng vật liệu đến; trong hành "
        "trình từ phễu cấp, lượng vật liệu ấy đã bị hao hụt do rơi vãi khỏi băng tải. Ngoài ra lượng vật "
        "liệu đọng trên băng cũng thay đổi do mức (hay cột áp) vật liệu trong phễu thay đổi."))
    b.append(fig(2, F.fig_12_2()))
    b.append(p(
        "Thời gian chết có thể được tính rất đơn giản bằng tích của tốc độ băng với khoảng cách giữa phễu "
        "nạp — nơi tác động của biến điều khiển (đầu ra bộ điều khiển) xảy ra — và PV, tức vị trí đặt cân "
        "băng:"))
    b.append(eq("L = d / v", "12.1"))
    b.append(p(
        "Trong ví dụ này, bộ điều khiển đo trọng lượng trên mét trên phút của vật liệu đến, so với SP và "
        "tạo ra một đầu ra — nhưng bây giờ nó phải chờ hết khoảng thời gian chết, trong ví dụ này khoảng "
        "10 phút, trước khi thấy kết quả của thay đổi ấy ở giá trị MV. Nếu bộ điều khiển mong đợi một kết "
        "quả trước khi thời gian chết trôi qua mà không thấy gì, nó sẽ cho rằng thay đổi vừa rồi không có "
        "tác dụng và sẽ tiếp tục tăng đầu ra cho tới khi PV cảm nhận được rằng đã có thay đổi. Đến lúc "
        "ấy thì đã quá muộn: bộ điều khiển đã bù quá mức, và giờ hoặc cấp quá nhiều hoặc cấp quá ít vật "
        "liệu."))
    b.append(p(
        "Độ lớn của sai số tạo thành sẽ phụ thuộc vào độ nhạy của hệ thống và vào chênh lệch giữa thời "
        "gian chết giả định và thời gian chết thực. Nghĩa là, nếu hệ thống rất nhạy (hệ số khuếch đại "
        "cao và đáp ứng nhanh được chỉnh vào nó) thì những thay đổi nhỏ của PV sẽ gây ra những dịch "
        "chuyển lớn ở phễu nạp. Và nếu thời gian chết giả định ngắn hơn nhiều so với thời gian chết thực "
        "thì bộ điều khiển sẽ thay đổi đầu ra (MV) lâu hơn nữa trước khi cảm nhận được thay đổi của PV."))

    b.append(h3("12.3.1 Khắc phục thời gian chết của quá trình", "Overcoming Process Deadtime"))
    b.append(p(
        "Việc khắc phục những vấn đề này phụ thuộc — ở mức độ lớn — vào yêu cầu vận hành của quá trình. "
        "Giải pháp dễ nhất là “giảm chỉnh” bộ điều khiển xuống một tốc độ đáp ứng chậm hơn. Khi đó bộ "
        "điều khiển sẽ không bù quá mức, trừ khi thời gian chết quá dài."))
    b.append(p(
        "Khâu tích phân (mode I) của bộ điều khiển rất nhạy với thời gian chết, vì trong suốt khoảng thời "
        "gian PV không phản ứng ấy (một số hạng ERR vẫn tồn tại) khâu tích phân đang mải “dốc” giá trị "
        "đầu ra."))
    b.append(p(
        "Ziegler và Nichols xác định rằng cách tốt nhất để “giảm chỉnh” một bộ điều khiển nhằm xử lý một "
        "thời gian chết D phút là giảm hằng số thời gian tích phân T<sub>INT</sub> đi một hệ số D² và "
        "giảm hằng số tỉ lệ đi một hệ số D."))
    b.append(p(
        "Hằng số thời gian vi phân T<sub>DER</sub> không bị ảnh hưởng bởi thời gian chết, vì nó chỉ xuất "
        "hiện sau khi PV bắt đầu dịch chuyển."))
    b.append(fig(3, F.fig_12_3()))
    b.append(p(
        "Hình 12-3 cho thấy cơ chế gây ra vấn đề, và qua đó cho thấy vì sao cách chữa ấy lại có tác dụng. "
        "Trong suốt thời gian chết, bộ điều khiển thấy sai lệch không đổi nên khâu tích phân tiếp tục "
        "dốc đầu ra. Khi PV cuối cùng nhúc nhích, nó đã đi quá xa. Giảm chỉnh làm chậm đúng cái dốc ấy "
        "— đó là toàn bộ nội dung của quy tắc Ziegler–Nichols ở trên."))
    b.append(p(
        "Tuy vậy, nếu ta có thể cho bộ điều khiển biết khoảng thời gian chết, và cho nó sự kiên nhẫn để "
        "chờ và bằng lòng cho tới khi thời gian chết trôi qua, thì việc giảm chỉnh và biến toàn bộ quá "
        "trình thành rất ì ạch sẽ không còn cần thiết nữa."))
    b.append(p("Đó chính là điều mà Smith Predictor cố gắng thực hiện."))
    b.append(note(
        "<b>Một lưu ý về con số.</b> Quy tắc “giảm T<sub>INT</sub> đi D² và giảm K đi D” là một quy tắc rất "
        "mạnh. Với một thời gian chết 10 phút tính theo phút (D = 10), nó đòi hỏi giảm T<sub>INT</sub> đi "
        "100 lần — nghĩa là bộ điều khiển gần như mất hoàn toàn khâu tích phân. Trong thực hành người ta "
        "thường áp dụng quy tắc này theo đơn vị thời gian chết chuẩn hoá (D tính theo đơn vị của hằng số "
        "thời gian quá trình), chứ không phải theo phút tuyệt đối. Cần kiểm tra đơn vị trước khi áp "
        "dụng."))

    b.append(h2("12.4 Mô hình Smith Predictor", "The Smith Predictor Model"))
    b.append(p(
        "Năm 1957, O.J.M. Smith thuộc Đại học California tại Berkeley đề xuất chiến lược điều khiển dự báo "
        "như trình bày dưới đây. Hình 12-4 minh hoạ mô hình toán học của bộ dự báo, gồm:"))
    b.append(ul([
        "Một vòng phản hồi thông thường;",
        "Một vòng thứ hai, hay vòng trong, đưa thêm hai số hạng vào đường phản hồi."]))
    b.append(fig(4, F.fig_12_4()))

    b.append(h3("12.4.1 Giải thích số hạng thứ nhất (PV không nhiễu)",
                "First Term Explanation (Disturbance Free PV)"))
    b.append(p(
        "Số hạng thứ nhất là một <b>ước lượng</b> về việc PV sẽ ra sao khi không có bất kỳ nhiễu quá trình "
        "nào. Nó được tạo ra bằng cách cho đầu ra bộ điều khiển đi qua một mô hình được thiết kế để biểu "
        "diễn chính xác hành vi của quá trình mà không tính đến bất kỳ nhiễu tải nào. Mô hình này gồm hai "
        "phần tử mắc nối tiếp."))
    b.append(ol([
        "Phần tử thứ nhất biểu diễn toàn bộ hành vi của quá trình không quy cho thời gian chết. Nó "
        "thường được tính như một phương trình vi phân hay phương trình sai phân thông thường, bao gồm "
        "ước lượng của mọi hệ số khuếch đại và hằng số thời gian của quá trình.",
        "Phần tử thứ hai không biểu diễn gì khác ngoài thời gian chết, và chỉ đơn giản là một độ trễ "
        "thời gian: cái gì vào thì ra muộn hơn, không thay đổi."]))

    b.append(h3("12.4.2 Giải thích số hạng thứ hai (PV dự báo)",
                "Second Term Explanation (Predicted PV)"))
    b.append(p(
        "Số hạng thứ hai được đưa vào đường phản hồi là một ước lượng về việc PV sẽ ra sao khi không có cả "
        "nhiễu lẫn thời gian chết."))
    b.append(p(
        "Nó được tạo ra bằng cách cho đầu ra bộ điều khiển đi qua phần tử thứ nhất của mô hình (các hệ số "
        "khuếch đại và hằng số thời gian) nhưng <b>không</b> đi qua phần tử trễ."))
    b.append(p(
        "Như vậy nó dự báo PV không nhiễu sẽ ra sao một khi thời gian chết đã trôi qua."))
    b.append(p(
        "Hai số hạng này nghe có vẻ trùng lặp, nhưng chúng trả lời hai câu hỏi khác nhau. Số hạng thứ "
        "nhất trả lời: “nếu không có nhiễu, PV bây giờ là bao nhiêu?” — nó vẫn còn trễ, vì nó đi qua phần "
        "tử trễ. Số hạng thứ hai trả lời: “nếu không có nhiễu và không có trễ, PV sẽ là bao nhiêu?” — nó "
        "đi trước thời gian. Hiệu của chúng chính là phần PV sẽ thay đổi trong khoảng thời gian chết sắp "
        "tới, và đó là con số mà bộ điều khiển cần."))

    b.append(h2("12.5 Smith Predictor trong sử dụng lý thuyết",
                "The Smith Predictor in Theoretical Use"))
    b.append(p(
        "Hình 12-5 cho thấy Smith Predictor ở cấu hình thực dụng, hay đúng như nó được dùng thật."))
    b.append(fig(5, F.fig_12_5()))
    b.append(p(
        "Nó cho thấy một ước lượng của PV (gồm cả nhiễu lẫn thời gian chết) được tạo ra bằng cách cộng "
        "các nhiễu ước lượng trở lại vào PV không nhiễu. Kết quả là một hệ điều khiển phản hồi với thời "
        "gian chết nằm <b>ngoài</b> vòng."))
    b.append(p(
        "Về bản chất, Smith Predictor làm việc để điều khiển biến phản hồi đã sửa (PV dự báo có tính cả "
        "nhiễu) thay vì PV thật:"))
    b.append(eq(
        "PV* = PV + G<sub>m</sub>(s)·u − G<sub>m</sub>(s)·e<sup>−L<sub>m</sub>s</sup>·u", "12.2"))
    b.append(p(
        "Nếu nó làm được điều đó, và nếu mô hình quá trình mô phỏng chính xác chính quá trình, thì bộ "
        "điều khiển sẽ đồng thời kéo PV thật về giá trị SP, bất kể thay đổi SP hay nhiễu tải."))
    b.append(p(
        "Cần nhấn mạnh vì sao cấu trúc này lại có sức mạnh đến thế. Phương trình đặc tính của vòng kín "
        "khi có mô hình hoàn hảo trở thành:"))
    b.append(eq("1 + G<sub>c</sub>(s)·G<sub>m</sub>(s) = 0", "12.3"))
    b.append(p(
        "Số hạng e<sup>−Ls</sup> đã biến mất khỏi phương trình đặc tính. Nghĩa là vòng kín không còn "
        "chứa thời gian chết nữa, và bộ điều khiển có thể được chỉnh định mạnh như thể quá trình không "
        "có trễ. Đó chính là ý nghĩa của câu “thời gian chết nằm ngoài vòng”: nó vẫn tồn tại trong quá "
        "trình thật, nhưng nó không còn tham gia vào việc quyết định tính ổn định."))

    b.append(h2("12.6 Smith Predictor trong thực tế", "The Smith Predictor in Reality"))
    b.append(p(
        "Trong thực tế có rất nhiều chỗ cho sai số lọt vào cái “lý tưởng dự báo” này. Chỉ một sai lệch "
        "nhỏ nhất giữa các giá trị động học của quá trình và của mô hình cũng có thể khiến bộ điều khiển "
        "tạo ra một đầu ra điều khiển thành công biến phản hồi đã sửa, nhưng lại đẩy PV thật vào hư vô, "
        "không bao giờ trở lại."))
    b.append(fig(6, F.fig_12_6()))
    b.append(p(
        "Hình 12-6 cho thấy điều đó bằng số. Chỉ khi thời gian chết của mô hình đúng bằng của quá trình "
        "thì PV mới về đúng điểm đặt. Mô hình ngắn quá thì PV vọt lố rồi đậu ở một mức cao hơn; mô hình "
        "dài quá thì PV vọt lố rồi tụt xuống dưới. Cả hai trường hợp đều <em>ổn định</em> — và chính vì "
        "ổn định nên chúng nguy hiểm: không có dao động nào để người vận hành nhận ra là có gì đó sai, "
        "chỉ có một sản phẩm sai đều đặn."))
    b.append(p(
        "Có rất nhiều biến thể của nguyên lý Smith Predictor, nhưng thời gian chết — đặc biệt là thời gian "
        "chết dài — vẫn là một bài toán điều khiển đặc biệt khó điều khiển và giải quyết."))
    b.append(quote(
        "Một mô hình sai không làm hệ mất ổn định. Nó làm hệ ổn định ở một giá trị sai — và đó là kiểu "
        "hỏng hóc khó phát hiện nhất trong điều khiển.",
        "Hệ quả của mục 12.6"))

    b.append(h2("12.7 Một bài tập về bù thời gian chết", "An Exercise in Deadtime Compensation"))
    b.append(p(
        "Ta đã thấy rằng nếu thời gian chết dài là một phần trong hành vi của quá trình, thì chất lượng "
        "điều khiển trở nên thấp đến mức không thể chấp nhận. Vấn đề chính nằm ở chỗ: phản ứng với một "
        "thay đổi MV không được PV nhìn thấy cho tới khi thời gian chết trôi qua. Trong khoảng thời gian "
        "đó, cả người vận hành lẫn bộ điều khiển tự động đều không biết thay đổi MV đã tác động lên quá "
        "trình như thế nào."))
    b.append(p(
        "Bài tập Mười bốn minh hoạ các khái niệm của bù thời gian chết, dựa trên cách bố trí ở Hình 12-5."))
    b.append(p(
        "Vì không có cách nào tách thời gian chết của quá trình ra khỏi phần động học của quá trình để "
        "tìm hiểu quá trình sẽ hành xử ra sao khi không có thời gian chết, ta dùng các giá trị do một mô "
        "phỏng quá trình cung cấp."))
    b.append(p(
        "Mô phỏng quá trình được chia làm hai phần như thấy ở Hình 12-4 và Hình 12-5; hai phần này được "
        "mô tả ở mục 12.4.1 và 12.4.2."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Ở mục 12.6, bản PDF gốc in “readmits” — rõ ràng là lỗi "
        "quét của từ “dead times”; bản dịch đọc theo nghĩa đúng của câu. Ngoài ra bản gốc viết “a factor "
        "of D2” ở mục 12.3.1, gần như chắc chắn là D² (bình phương), và bản dịch giữ nguyên cách hiểu đó "
        "kèm lưu ý về đơn vị ở trên."))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Nine chapters have taught how to control a process that reacts promptly. This chapter is about "
        "what happens when it does not: when there is an interval — sometimes ten minutes — during which "
        "the controller has acted but cannot yet know whether the action was right."))
    b.append(p(
        "That is not a quantitative difficulty but a qualitative one. For those ten minutes every "
        "feedback loop is flying blind. The chapter sets out the best a good engineer can do — slow the "
        "controller down — and then sets out O.J.M. Smith's 1957 idea: if you cannot observe the process, "
        "build a model of it and observe the model."))

    b.append(h2("Dead time does not slow a process; it delays its answer", "§ 12.2"))
    b.append(p(
        "The chapter's threshold is worth remembering: dead time becomes a serious problem above about "
        "20 per cent of the total time the PV takes to settle after a set-point change. Below that, "
        "ordinary tuning handles it."))
    b.append(fig(1, F.fig_12_1(), "en"))
    b.append(p(
        "Figure 12-1 makes a point that is easy to miss. The three curves share one time constant; dead "
        "time has not changed their shape at all, only shifted them right. Dead time does not make a "
        "process slower — it makes it <em>answer later</em>. A slow process can be waited for. A process "
        "that answers late gives the controller no way to know it should wait: it sees an error, acts, "
        "and sees the same error still there, with nothing to tell it that the previous action has "
        "already begun to work."))

    b.append(h2("The conveyor: dead time you can measure with a tape", "§ 12.3"))
    b.append(p(
        "The chapter's example is a conveyor belt, and it is a good one because the dead time is not an "
        "abstraction — it is distance divided by belt speed, and you can walk along and measure both."))
    b.append(fig(2, F.fig_12_2(), "en"))
    b.append(p(
        "The failure mechanism is described precisely: the controller compares the arriving weight with "
        "the set point, generates an output, and then waits about ten minutes for a result. If no result "
        "appears, it concludes its last change did nothing and increases the output further. By the time "
        "the PV finally responds, it has over-compensated — too much material or too little."))
    b.append(p(
        "The magnitude of that error depends on two things the chapter names explicitly. The first is "
        "loop sensitivity: a high-gain, fast-tuned loop moves the hopper a long way for a small PV "
        "change, so its over-compensation is larger. The second is the error in the assumed dead time: if "
        "the controller believes the dead time is shorter than it is, it keeps changing its output for "
        "longer before it expects to see anything. Both are arguments for knowing the dead time "
        "accurately, not merely approximately."))

    b.append(h2("De-tuning: the honest cure", "§ 12.3.1"))
    b.append(p(
        "The straightforward fix is to slow the controller down until it stops over-compensating. The "
        "chapter explains why this works by pointing at the integrator: during the dead time the error "
        "persists, so the integral term keeps ramping the output. Slowing the ramp is exactly what "
        "de-tuning does."))
    b.append(fig(3, F.fig_12_3(), "en"))
    b.append(p(
        "Figure 12-3 shows the mechanism in two panels. Above, the output ramps up throughout the dead "
        "time because the controller has no evidence that anything has happened. Below, the PV eventually "
        "moves — and overshoots badly, because the output has been ramping the whole time."))
    b.append(p(
        "The Ziegler–Nichols rule the chapter quotes — reduce the integral time by a factor of D² and the "
        "proportional constant by a factor of D — is worth reading with care about units. Applied "
        "literally with D in minutes, a ten-minute dead time would demand a hundredfold reduction in "
        "integral time, which effectively removes the integrator altogether. In practice the rule is "
        "applied with D normalised against the process time constant. The derivative term, as the chapter "
        "notes, is untouched: it only acts after the PV starts to move."))
    b.append(p(
        "De-tuning works, and it is honest about what it costs: the whole process becomes sluggish. That "
        "cost is what motivates the predictor."))

    b.append(h2("The Smith predictor: observing a model instead", "§ 12.4"))
    b.append(p(
        "The structure has an ordinary feedback loop plus an inner loop that introduces two extra terms "
        "into the feedback path. The first is an estimate of what the PV would be with no disturbances at "
        "all — produced by running the controller output through a model made of two series elements, the "
        "process dynamics and a pure delay. The second is an estimate of what the PV would be with "
        "neither disturbances nor dead time — the same model, but with the delay element omitted."))
    b.append(fig(4, F.fig_12_4(), "en"))
    b.append(p(
        "The two terms look redundant and are not. The first answers: with no disturbance, where is the "
        "PV <em>now</em>? It still carries the delay. The second answers: with no disturbance and no "
        "delay, where would the PV be? It runs ahead. Their difference is how much the PV is going to "
        "move during the dead time that has not yet elapsed — which is precisely the number the "
        "controller needs."))
    b.append(fig(5, F.fig_12_5(), "en"))
    b.append(p(
        "Figure 12-5 is the version that matters, because it shows two loops coexisting. On the left is "
        "the loop that physically exists, with its delay. On the right is the loop the controller is "
        "actually regulating — a model with the delay removed. The controller drives the PV of the right "
        "panel; if the model is right, the real PV follows as a consequence."))
    b.append(eq(
        "PV* = PV + G<sub>m</sub>(s)·u − G<sub>m</sub>(s)·e<sup>−L<sub>m</sub>s</sup>·u", "12.2"))
    b.append(p(
        "The reason this is so powerful is visible in the characteristic equation. With a perfect model, "
        "the closed-loop poles satisfy:"))
    b.append(eq("1 + G<sub>c</sub>(s)·G<sub>m</sub>(s) = 0", "12.3"))
    b.append(p(
        "The delay term has vanished. The loop no longer contains the dead time, and the controller can "
        "be tuned as aggressively as if the process had none. That is the precise sense in which the dead "
        "time has been moved outside the loop: it still exists in the plant, but it no longer takes part "
        "in deciding stability."))

    b.append(h2("Why a wrong model is worse than no model", "§ 12.6"))
    b.append(p(
        "The chapter's warning is blunt — the slightest mismatch between the process dynamics and the "
        "model can produce an output that successfully manipulates the modified feedback variable while "
        "driving the actual PV into nihilism, never to return."))
    b.append(fig(6, F.fig_12_6(), "en"))
    b.append(p(
        "Figure 12-6 puts numbers on it. Only when the model's dead time matches the process does the PV "
        "reach set point. A model that is too short leaves the PV high; one that is too long lets it fall "
        "below. Both cases settle — and that is exactly what makes them dangerous. There is no "
        "oscillation for an operator to notice, no alarm to raise. The controller is perfectly happy, "
        "because the variable it is regulating is at set point. The variable that matters is not."))
    b.append(quote(
        "A wrong model does not destabilise the loop. It stabilises it at the wrong value — which is the "
        "hardest failure to notice in control.",
        "The consequence of section 12.6"))
    b.append(p(
        "There are many variants on the Smith principle, and the chapter is right to end without "
        "pretending otherwise: dead time, especially long dead time, remains one of the genuinely hard "
        "problems of the field. The predictor does not solve it. It converts a problem the controller "
        "cannot see into a problem the engineer can measure — the accuracy of a model — and that is a "
        "real improvement, because a model can be checked against the plant and a blind loop cannot."))
    return "".join(b)
