# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 10, Concepts and Applications of
Feedforward Control (Wolfgang Altmann, IDC Technologies)."""
import pc10fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 8
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Điều khiển theo hướng (feedforward)</em> — tác động lên biến điều khiển dựa trên nhiễu "
            "đo được, trước khi sai lệch xuất hiện. · "
            "<em>Nhiễu đo được (measured disturbance)</em> — đại lượng gây nhiễu mà ta có cảm biến để "
            "đọc trực tiếp. · "
            "<em>Khâu bù lead/lag</em> — khối có hàm truyền (1 + T<sub>lead</sub>s)/(1 + αT<sub>lead</sub>s), "
            "dùng để làm hai tốc độ phản ứng bằng nhau. · "
            "<em>Khớp thời gian (time matching)</em> — làm cho đáp ứng của tác động điều khiển trùng với "
            "đáp ứng của nhiễu. · "
            "<em>Phần dư (residual offset)</em> — sai lệch còn lại sau khi bù, không bao giờ bằng không. · "
            "<em>Hàm toán (math function)</em> — phép tính biến đầu vào thành đầu ra của khối theo hướng.")
    return note(
        "<b>Key terms.</b> <em>Feedforward</em> — acting on the manipulated variable from a measured "
        "disturbance, before any error exists. · <em>Measured disturbance</em> — a disturbing quantity "
        "the plant has an instrument to read directly. · <em>Lead/lag compensator</em> — a block with "
        "transfer function (1 + T<sub>lead</sub>s)/(1 + αT<sub>lead</sub>s), used to make two reaction "
        "speeds equal. · <em>Time matching</em> — making the control action's response coincide with the "
        "disturbance's. · <em>Residual offset</em> — the error left after compensation, which is never "
        "zero. · <em>Math function</em> — the calculation that turns the block's input into its output.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương này ngắn — chỉ tám trang gốc — nhưng nó đặt vào tay người đọc một ý tưởng khác hẳn mọi "
        "chương trước đó. Từ chương 4 tới chương 9, mọi bộ điều khiển đều làm việc theo cùng một lô-gíc: "
        "đo PV, so với SP, lấy hiệu, rồi hành động. Sai lệch phải có trước, hành động có sau. Điều khiển "
        "theo hướng đảo ngược trật tự đó."))
    b.append(p(
        "Nó không chờ sai lệch. Nó đọc đại lượng gây ra sai lệch — nhiễu — và hành động ngay trên nhiễu "
        "ấy. Nếu làm đúng, PV không bao giờ lệch, nên vòng phản hồi không có gì để sửa. Đó là lý do "
        "chương này tồn tại, và cũng là lý do nó khó: để hành động trước, ta phải biết trước."))

    b.append(h2("10.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này và làm xong các bài tập liên quan, học viên phải có khả năng:"))
    b.append(ul([
        "Mô tả được khái niệm và chiến lược của điều khiển theo hướng;",
        "Xây dựng và trình bày rõ ràng được các thủ tục chỉnh định cho điều khiển theo hướng."]))

    b.append(h2("10.2 Ứng dụng và định nghĩa điều khiển theo hướng",
                "Application and Definition of Feedforward Control"))
    b.append(p(
        "Nếu trong một hệ điều khiển phản hồi mà PV hoặc thời gian trễ của quá trình thay đổi lớn và ngẫu "
        "nhiên, thì tác động phản hồi trở nên rất kém hiệu quả khi cố sửa những biến thiên quá mức ấy. "
        "Những biến thiên đó thường đẩy quá trình ra khỏi vùng làm việc của nó, và bộ điều khiển phản hồi "
        "hầu như không có cơ hội sửa chính xác hoặc nhanh chóng trở về giá trị SP."))
    b.append(p(
        "Kết quả là độ chính xác và tiêu chuẩn chất lượng của quá trình trở nên không thể chấp nhận. "
        "Điều khiển theo hướng được dùng để phát hiện và sửa những nhiễu ấy <em>trước khi</em> chúng có "
        "cơ hội đi vào và làm rối loạn đặc tính của vòng kín."))
    b.append(quote(
        "Điều khiển theo hướng không tính đến biến quá trình; nó phản ứng với cảm biến hay phép đo các "
        "nhiễu đã biết hoặc bị nghi ngờ, khiến nó trở thành một kiểu điều khiển bù trừ và khớp, làm cho "
        "tác động của nhiễu và tác động của điều khiển phản hồi trở nên bằng nhau.",
        "Altmann, mục 10.2"))
    b.append(p(
        "Câu đó chứa đựng toàn bộ chương này. Ba ý cần tách ra. Thứ nhất, khối theo hướng <b>không nhận "
        "PV</b> — nếu nó nhận PV thì nó đã là một khâu phản hồi. Thứ hai, nó nhận <b>nhiễu</b>. Thứ ba, "
        "việc nó làm là <b>làm hai tác động bằng nhau</b>: tác động mà nhiễu sắp gây ra lên PV, và tác "
        "động mà bộ điều khiển gây ra để chống lại. Khi hai tác động ấy bằng nhau về độ lớn và trùng nhau "
        "về thời gian, PV đứng yên."))
    b.append(p("Khác biệt giữa điều khiển theo hướng và điều khiển phản hồi có thể tóm như sau:"))
    b.append(ul([
        "Điều khiển theo hướng chủ yếu được thiết kế và dùng để <b>ngăn</b> sai số — tức các nhiễu quá "
        "trình — đi vào hoặc làm rối loạn một vòng điều khiển trong hệ thống.",
        "Điều khiển phản hồi được dùng để <b>sửa</b> những sai số do nhiễu quá trình gây ra, sau khi "
        "chúng đã được phát hiện bên trong một hệ điều khiển vòng kín. Những sai số ấy có thể được dự "
        "báo trước và sửa trước bằng điều khiển theo hướng, trước khi chúng làm hỏng các tham số của "
        "vòng điều khiển."]))
    b.append(p(
        "Chính yếu tố thứ hai ấy — khả năng sửa trước khi sai lệch hình thành — khiến điều khiển theo "
        "hướng trở thành một khái niệm rất hấp dẫn. Tiếc thay, để nó vận hành an toàn và hiệu quả, cần "
        "có hiểu biết vững chắc cả về quá trình lẫn về bản chất của mọi nhiễu liên quan."))
    b.append(p(
        "Hình 10-1 cho thấy vì sao. Cùng một nhiễu bậc thang tác động vào cùng một quá trình. Đường xanh "
        "là trường hợp chỉ có phản hồi: PV lệch sâu, rồi bộ điều khiển mới kéo nó về. Đường đỏ là trường "
        "hợp có thêm khối theo hướng: khối này đọc nhiễu ngay khi nó xuất hiện và bù trước, nên PV gần "
        "như không lệch. Khác biệt không nằm ở chất lượng bộ điều khiển — cùng một bộ điều khiển — mà "
        "nằm ở <em>thời điểm</em> thông tin có mặt."))
    b.append(fig(1, F.fig_10_1()))

    b.append(h2("10.3 Điều khiển theo hướng bằng tay", "Manual Feedforward Control"))
    b.append(p(
        "Điều khiển theo hướng là một khái niệm hoàn toàn khác với điều khiển phản hồi. Một ví dụ bằng "
        "tay được minh hoạ trong Hình 10-2. Ở đây, khi một nhiễu đi vào quá trình, nó được người vận "
        "hành phát hiện và đo. Dựa trên hiểu biết của mình về quá trình, người vận hành thay đổi biến "
        "điều khiển một lượng sao cho tác động của nhiễu đo được lên hệ thống là nhỏ nhất."))
    b.append(fig(2, F.fig_10_2()))
    b.append(p(
        "Dạng điều khiển theo hướng này dựa rất nhiều vào người vận hành và hiểu biết của họ về vận hành "
        "quá trình. Tuy vậy, nếu người vận hành phạm sai lầm hoặc không thể lường trước một nhiễu, thì "
        "biến được điều khiển sẽ lệch khỏi giá trị mong muốn; và nếu theo hướng là cơ chế điều khiển duy "
        "nhất, thì sẽ tồn tại một sai số không được sửa."))
    b.append(p(
        "Hình 10-2 vẽ đúng cấu trúc ấy và cũng vẽ đúng chỗ hổng của nó. Không có vòng phản hồi nào trong "
        "sơ đồ — mũi tên từ PV đi xuống “NGƯỜI VẬN HÀNH” là mắt người, không phải một vòng kín tự động. "
        "Người vận hành nhìn PV, nhưng không có gì bắt buộc họ phải hành động, và không có gì kiểm tra "
        "hành động của họ có đúng hay không. Sai số do người gây ra sẽ tồn tại vĩnh viễn."))
    b.append(p(
        "Điểm này quan trọng vì nó là mầm của toàn bộ phần còn lại. Một khối theo hướng, dù tự động hay "
        "bằng tay, đều là một phép <b>dự báo</b>. Mọi dự báo đều sai ở một mức nào đó. Nếu không có cơ "
        "chế nào phát hiện cái sai ấy, thì sai số của dự báo trở thành sai số vĩnh viễn của quá trình. "
        "Đó là lý do, như sẽ thấy ở mục 10.6, điều khiển theo hướng thuần tuý hầu như không tồn tại một "
        "mình."))

    b.append(h2("10.4 Điều khiển theo hướng tự động", "Automatic Feedforward Control"))
    b.append(p(
        "Hình 10-3 minh hoạ khái niệm điều khiển theo hướng tự động. Những nhiễu <em>sắp</em> đi vào quá "
        "trình được phát hiện và đo. Bộ điều khiển theo hướng sau đó thay đổi giá trị biến điều khiển "
        "(đầu ra) của mình dựa trên các phép đo ấy, so với giá trị điểm đặt riêng của nó."))
    b.append(fig(3, F.fig_10_3()))
    b.append(p(
        "Chú ý điểm rẽ nhánh trong sơ đồ: tín hiệu nhiễu tách làm hai. Một nhánh đi thẳng vào quá trình "
        "— đó là nhiễu vật lý, không gì chặn được. Nhánh kia đi vào khối theo hướng, được biến đổi thành "
        "một lượng bù, rồi cộng vào đầu ra của bộ điều khiển. Hai nhánh phải đến đích cùng một lúc và "
        "ngược dấu nhau; nếu lệch thời điểm, phần bù đến sớm thì gây nhiễu mới, đến muộn thì vô ích."))
    b.append(p(
        "Bộ điều khiển theo hướng phải có khả năng thực hiện cả một dải phép tính, từ tác động on-off "
        "đơn giản đến những phương trình rất phức tạp. Những phép tính ấy phải kể đến mọi tác động chính "
        "xác mà nhiễu sẽ gây ra lên biến được điều khiển."))
    b.append(p(
        "Điều khiển theo hướng, dù là một khái niệm rất hấp dẫn, đặt ra yêu cầu cao với cả người thiết "
        "kế hệ thống lẫn người vận hành: cả hai đều phải phân tích được bằng toán học và hiểu được tác "
        "động của nhiễu lên quá trình đang xét. Hệ quả là điều khiển theo hướng thường được dành cho "
        "những vòng quan trọng hoặc tới hạn trong nhà máy."))
    b.append(p(
        "Điều khiển theo hướng thuần tuý hiếm khi gặp; thường gặp hơn là nó được nhúng bên trong một "
        "vòng phản hồi, nơi nó hỗ trợ chức năng của bộ điều khiển phản hồi bằng cách làm giảm tác động "
        "của những nhiễu quá trình quá mức. Chương 11 (Kết hợp điều khiển phản hồi và theo hướng) sẽ xét "
        "khái niệm và ứng dụng của điều khiển theo hướng khi nó được ghép với một hệ phản hồi kiểu "
        "cascade."))
    b.append(note(
        "Cần nhớ rằng điều khiển theo hướng chủ yếu được thiết kế để làm giảm hoặc loại bỏ tác động của "
        "những thay đổi <em>cả về thời gian phản ứng của quá trình lẫn về độ lớn của bất kỳ thay đổi nào "
        "trong biến quá trình đo được</em>. Hai thứ đó khác nhau: thứ nhất là quá trình phản ứng nhanh hay "
        "chậm, thứ hai là quá trình phản ứng mạnh hay yếu. Một khối theo hướng chỉ bù được độ lớn mà "
        "không khớp được thời gian thì sẽ bù sai thời điểm — và như đã nói, bù sai thời điểm thì tệ hơn "
        "không bù."))

    b.append(h2("10.5 Ví dụ về các bộ điều khiển theo hướng", "Examples of Feedforward Controllers"))
    b.append(p(
        "Như đã bàn ở trên, bộ điều khiển theo hướng có thể được yêu cầu thực hiện từ điều khiển đơn giản "
        "(on-off) đến những phép tính toán học bậc cao. Do yêu cầu rất đa dạng, chúng có thể được coi là "
        "những <b>khối chức năng điều khiển</b>. Chúng có thể trải từ điều khiển on-off đơn giản đến "
        "lead/lag (các hàm vi phân và tích phân) và các khối định thời. Dải chức năng của chúng gần như "
        "không giới hạn, vì hầu hết các hệ thống cho phép “lập trình” chúng như những hàm toán học phần "
        "mềm."))
    b.append(p("Bốn yêu cầu cơ bản cho việc cấu thành một bộ điều khiển theo hướng là:"))
    b.append(ul([
        "Một <b>ĐẦU VÀO</b> nhận biết được (lấy từ nhiễu đo được);",
        "Một <b>ĐIỂM ĐẶT</b> hay điểm gốc và điểm điều khiển;",
        "Một <b>HÀM TOÁN</b> tác động lên các giá trị ĐẦU VÀO và ĐIỂM ĐẶT;",
        "Một <b>ĐẦU RA</b> là kết quả của hàm toán ấy."]))
    b.append(fig(4, F.fig_10_4()))
    b.append(p(
        "Về bản chất, tác động của bộ điều khiển có thể được mô tả hoàn toàn bằng hàm toán học mà nó thực "
        "hiện. Đây không phải một cách nói hoa mỹ — nó có hệ quả thực hành. Nếu tác động của khối được "
        "xác định hoàn toàn bởi hàm toán, thì việc thiết kế khối chính là việc chọn hàm ấy; và việc kiểm "
        "tra khối chính là việc kiểm tra hàm ấy cho ra đúng kết quả trên một tập đầu vào đã biết. Không "
        "có trạng thái ẩn, không có bộ nhớ tích luỹ, không có windup. Một khối theo hướng thuần tuý là "
        "một hàm, không phải một hệ động học."))
    b.append(p(
        "Chính vì thế mà bốn thành phần trên là đủ. Không có thành phần thứ năm nào kiểu “trạng thái tích "
        "phân” hay “chế độ vận hành”, bởi khối không có gì để tích luỹ. Điều này cũng giải thích vì sao "
        "một khối theo hướng có thể được kiểm tra ngoài tuyến hoàn toàn: đưa vào một dải giá trị nhiễu, "
        "đọc ra đầu ra, so với tính toán độc lập."))

    b.append(h2("10.6 Khớp thời gian như một dạng điều khiển theo hướng",
                "Time Matching as Feedforward Control"))
    b.append(p(
        "Hình 10-5 trình bày một ứng dụng của điều khiển theo hướng, trong đó thời gian để quá trình phản "
        "ứng theo một chiều (CẤP NHIỆT) khác với thời gian để quá trình trở về trạng thái ban đầu (NGUỘI "
        "ĐI). Nếu đường cong phản ứng (tức hành vi động học của phản ứng) của nhiễu quá trình không bằng "
        "với tác động điều khiển, thì phải làm cho chúng bằng nhau."))
    b.append(fig(5, F.fig_10_5()))
    b.append(p(
        "Hình vẽ cho thấy vì sao điều này lại quan trọng. Một bộ gia nhiệt có hằng số thời gian cấp nhiệt "
        "ngắn hơn nhiều so với hằng số thời gian nguội đi — nhiệt vào nhanh, nhiệt ra chậm. Nếu khối theo "
        "hướng bù theo tốc độ cấp nhiệt trong khi nhiễu lại tác động theo tốc độ nguội, thì lượng bù sẽ "
        "đến quá sớm ở giai đoạn đầu và quá muộn ở giai đoạn sau. Kết quả là PV vọt lên rồi mới hồi, hoặc "
        "hồi chậm hơn cả khi không có bù."))
    b.append(p(
        "Ta thường dùng các <b>khâu bù lead/lag</b> làm công cụ để đạt được hành vi động học bằng nhau. "
        "Chúng bù cho sự khác nhau về tốc độ phản ứng. Sơ đồ khối của nguyên lý bù này được trình bày "
        "trong Hình 10-6."))
    b.append(fig(6, F.fig_10_6()))
    b.append(p(
        "Khâu lead/lag có hàm truyền:"))
    b.append(eq(
        "G(s) = (1 + T<sub>lead</sub>·s) / (1 + α·T<sub>lead</sub>·s)", "10.1"))
    b.append(p(
        "với α là tỉ số giữa hằng số thời gian trễ và hằng số thời gian vượt. Khi một bước nhảy đơn vị "
        "vào khâu này, đầu ra là:"))
    b.append(eq(
        "y(t) = 1 + (1/α − 1)·e<sup>−t/(α·T<sub>lead</sub>)</sup>", "10.2"))
    b.append(p(
        "Với α &lt; 1, số hạng (1/α − 1) dương, nên đầu ra vọt lên giá trị 1/α ngay tại thời điểm bước "
        "nhảy rồi tắt dần về 1. Đó chính là hình dạng trong Hình 10-6: một đỉnh, rồi tự tắt. Ý nghĩa vật "
        "lý của nó rất rõ — khâu tạo ra một cú đẩy thêm ngay lập tức, đúng bằng lượng cần để bắt kịp một "
        "quá trình phản ứng nhanh, rồi rút lui dần khi quá trình chậm hơn đã đuổi kịp."))
    b.append(p(
        "Chọn α chính là chọn mức độ “đẩy thêm”. α càng nhỏ thì đỉnh càng cao và cú đẩy càng mạnh, nhưng "
        "khâu cũng càng nhạy với nhiễu tần số cao trên đường đo. Với α = 0,4 như trong hình, đỉnh là 2,5 "
        "— tức khâu đẩy thêm 150 % trong khoảnh khắc đầu. Đó là lý do khâu lead/lag phải được đặt sau một "
        "bộ lọc, hoặc phải chấp nhận rằng tín hiệu nhiễu đo được cần sạch."))
    b.append(p(
        "Một vấn đề đặc biệt quan trọng là hiện tượng <b>trôi</b> của PV. Ta có thể cẩn thận đến mấy "
        "trong việc đánh giá nhiễu, nhưng không bao giờ đạt tới tình trạng bù hoàn hảo tuyệt đối. Luôn có "
        "những yếu tố không được tính đến. Điều này gây ra sự trôi của PV, và PV trôi thì phải được sửa "
        "bằng tay định kỳ, hoặc phải thêm một bộ điều khiển phản hồi bổ sung."))
    b.append(fig(8, F.fig_10_8()))
    b.append(p(
        "Hình 10-8 vẽ đúng cái trôi ấy. Đường đỏ là khối theo hướng làm việc một mình: nó bù được phần "
        "lớn nhiễu, nhưng phần còn lại thì ở lại mãi. Đường xanh là cùng khối ấy cộng thêm một vòng phản "
        "hồi chậm: vòng phản hồi không cần nhanh, vì khối theo hướng đã xử lý phần nhanh; nó chỉ cần đủ "
        "kiên nhẫn để gom phần dư. Đây là kiến trúc thực tế của gần như mọi hệ điều khiển theo hướng công "
        "nghiệp."))
    b.append(p(
        "Hình 10-7 trình bày một ví dụ được thiết kế cẩn thận, có tính đến mọi biến lớn và đo được có "
        "thể. Điều khiển theo hướng ở đây dùng phép tính lưu lượng khối cho lưu lượng đầu vào, và dùng "
        "một bộ điều khiển lưu lượng nhiên liệu để tránh ảnh hưởng của thay đổi áp suất nhiên liệu."))
    b.append(fig(7, F.fig_10_7()))
    b.append(p(
        "Cấu trúc của nó đáng để đọc chậm. Lưu lượng dòng liệu vào được đo bằng FT, rồi được quy đổi ngay "
        "thành nhiệt lượng cần cấp:"))
    b.append(eq(
        "Q<sub>cần</sub> = ṁ · c<sub>p</sub> · (T<sub>đặt</sub> − T<sub>vào</sub>)", "10.3"))
    b.append(p(
        "Đại lượng Q này trở thành điểm đặt cho vòng điều khiển lưu lượng nhiên liệu. Chú ý hai điều. "
        "Thứ nhất, nhiệt lượng cần cấp phụ thuộc vào <em>hiệu</em> nhiệt độ, không phải nhiệt độ đặt — nên "
        "khi nhiệt độ dòng vào thay đổi, lượng bù phải thay đổi theo, và đó là lý do TT xuất hiện trong "
        "sơ đồ chứ không chỉ FT. Thứ hai, đầu ra của khối tính toán không lái trực tiếp van nhiên liệu mà "
        "lái <em>điểm đặt của một bộ điều khiển lưu lượng</em>. Nhờ vậy, thay đổi áp suất nhiên liệu — một "
        "nhiễu thứ hai, không đo được ở đâu cả — bị vòng lưu lượng hấp thụ, và khối theo hướng không phải "
        "biết đến nó."))
    b.append(p(
        "Đó là một nguyên tắc thiết kế đáng nhớ: mỗi khối theo hướng chỉ nên bù <em>một</em> nhiễu. Nhiễu "
        "thứ hai thì để cho một vòng phản hồi nhanh bên trong lo. Cố bù cả hai bằng một khối duy nhất sẽ "
        "cho ra một hàm toán không thể kiểm chứng và không thể chỉnh định."))

    b.append(h2("Kết chương: hai cơ chế, không thay thế nhau", "Two mechanisms, not substitutes"))
    b.append(p(
        "Toàn bộ chương này có thể gói trong một câu: phản hồi sửa cái <em>đã</em> sai, theo hướng ngăn "
        "cái <em>sắp</em> sai. Không cơ chế nào thay thế được cơ chế kia, và một hệ thống tốt cần cả "
        "hai — theo hướng để giữ PV khỏi lệch, phản hồi để xoá phần dư mà theo hướng không bao giờ xoá "
        "hết."))
    b.append(fig(9, F.fig_10_9()))
    b.append(p(
        "Cái giá của việc thêm theo hướng cũng cần nói rõ. Nó đòi hỏi một cảm biến cho mỗi nhiễu muốn bù, "
        "một mô hình toán cho mỗi quan hệ nhiễu–PV, và một người hiểu cả hai để chỉnh định. Nó cũng đòi "
        "hỏi mô hình phải được cập nhật khi quá trình thay đổi — một khối theo hướng được chỉnh cho một "
        "bộ gia nhiệt sạch sẽ bù sai đi khi bộ gia nhiệt ấy bị đóng cáu. Đổi lại, nó là cơ chế duy nhất "
        "trong cuốn sách này có thể giữ PV đứng yên trong khi nhiễu đang tác động."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Trong bản PDF gốc, chú thích các hình bị đặt lệch một "
        "trang so với vị trí được nhắc trong văn bản: mục 10.6 nhắc “Figure 10.4” ở trang 245 nhưng chú "
        "thích Figure 10.4 lại nằm ở trang 246, sau chú thích Figure 10.3. Ngoài ra hình “Time Matching” "
        "được đánh số 10.3 trong bản gốc nhưng nội dung lại thuộc mục 10.6. Ở bản dịch này các hình được "
        "đánh số lại theo đúng thứ tự xuất hiện trong bài, nên số hiệu không trùng với bản gốc."))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Feedforward is the only strategy in this book that acts before an error exists. Every controller "
        "from chapter 4 onwards has followed the same logic: measure the PV, compare it with the SP, take "
        "the difference, act. The error has to exist first. Feedforward inverts that order — it reads the "
        "quantity that is <em>about to cause</em> the error and acts on it directly. Get it right and the "
        "PV never moves, so the feedback loop has nothing to correct."))
    b.append(p(
        "That inversion is also why the chapter is hard. To act in advance you have to know in advance: "
        "which disturbances are coming, how large they will be, and how the process will respond to each. "
        "The book states the price plainly — a sound knowledge is required both of the process and the "
        "nature of all relevant disturbances — and it is worth taking seriously, because a feedforward "
        "block tuned from a wrong model is worse than no block at all."))

    b.append(h2("The definition, unpacked", "§ 10.2"))
    b.append(p(
        "The chapter's own definition is a single sentence, and it rewards being taken apart. Feedforward "
        "control does not take the process variable into account; it reacts to the measurement of known "
        "or suspected disturbances, making it a compensating and matching control that makes the impact "
        "of the disturbance and of the feedback control equal."))
    b.append(p(
        "Three claims sit inside that sentence. The block does not see the PV — if it did, it would be a "
        "feedback element wearing a different name. It does see the disturbance. And what it does with "
        "the disturbance is make two effects equal: the effect the disturbance is about to have on the "
        "PV, and the effect the controller has in opposing it. Equal in magnitude and coincident in time. "
        "That is the whole specification, and both halves of it matter."))
    b.append(fig(1, F.fig_10_1(), "en"))
    b.append(p(
        "Figure 10-1 is the argument in one picture. The same step disturbance, the same process, the "
        "same controller. Blue has feedback only: the PV dives, and the controller then hauls it back. "
        "Red has a feedforward block as well: the block reads the disturbance as it arrives and "
        "compensates immediately, so the PV barely moves. Nothing about the controller changed between "
        "the two traces. What changed is when the information was available."))

    b.append(h2("Manual feedforward: the concept with the loop removed", "§ 10.3"))
    b.append(p(
        "The book's first example is a human being. An operator notices a disturbance, estimates it from "
        "process knowledge, and moves the manipulated variable by an amount that will minimise its "
        "effect. Figure 10-2 draws this honestly, including the gap: there is no feedback path in the "
        "diagram, and the line from PV down to the operator box is an eye, not a loop."))
    b.append(fig(2, F.fig_10_2(), "en"))
    b.append(p(
        "What makes this example more than a teaching device is the failure mode it exposes. The operator "
        "sees the PV but nothing compels them to act, and nothing checks whether the action was right. "
        "If they misjudge the disturbance, the error stays. Every feedforward block, automatic or manual, "
        "is a prediction, and every prediction is wrong by some amount. Without a mechanism that detects "
        "the error in the prediction, that error becomes a permanent offset in the process. Section 10.6 "
        "is where the book confronts this, and it is the most important passage in the chapter."))

    b.append(h2("Automatic feedforward: the same idea with a calculation in place of a person",
                "§ 10.4"))
    b.append(p(
        "Figure 10-3 replaces the operator with a block, and adds the detail the manual picture could "
        "not show: the disturbance signal splits. One branch goes into the process — that is the physical "
        "disturbance, and nothing stops it. The other goes into the feedforward block, is converted into "
        "a compensating quantity, and is summed into the controller's output. The two branches have to "
        "arrive at the same instant and with opposite signs. Compensation that arrives early is a new "
        "disturbance; compensation that arrives late is decoration."))
    b.append(fig(3, F.fig_10_3(), "en"))
    b.append(p(
        "This is where the book's warning about the designer and the operator both needing to understand "
        "the mathematics comes from, and it is why feedforward is reserved for important or critical "
        "loops. The cost of a feedforward block is not the block. It is the instrument on the "
        "disturbance, the model that relates the disturbance to the PV, and the person who can maintain "
        "both."))

    b.append(h2("Four parts, and nothing else", "§ 10.5"))
    b.append(p(
        "The chapter's list of what a feedforward block must contain is short: a recognisable input "
        "derived from the measured disturbance, a set point or point of origin, a math function operating "
        "on the two, and an output which is the result. Figure 10-4 draws it."))
    b.append(fig(4, F.fig_10_4(), "en"))
    b.append(p(
        "The claim that follows — that the controller's action can be described purely by the "
        "mathematical function it performs — is not rhetorical. It has a practical consequence. If the "
        "block's action is fully determined by its function, then designing the block is choosing the "
        "function, and testing the block is checking that the function returns the right answer over a "
        "known range of inputs. There is no hidden state, no accumulated integral, no windup. A pure "
        "feedforward block is a function, not a dynamical system."))
    b.append(p(
        "That is precisely why four parts are enough and why there is no fifth part of the kind a PID "
        "controller needs. A PID has state because it remembers; a feedforward block has none because it "
        "does not. The same fact makes the block testable offline, which is a considerable engineering "
        "advantage: sweep the disturbance input, read the output, compare against an independent "
        "calculation."))

    b.append(h2("Time matching: when equal magnitude is not enough", "§ 10.6"))
    b.append(p(
        "A heater does not heat and cool at the same rate. Figure 10-5 shows the consequence: the "
        "reaction curve for adding heat has one time constant, the curve for losing it has another, and "
        "a compensation sized for one is mistimed for the other. The book's phrasing is exact — if the "
        "reaction curve of the disturbance is not equal to the control action, it has to be made equal."))
    b.append(fig(5, F.fig_10_5(), "en"))
    b.append(p(
        "The tool for making them equal is the lead/lag block, and its step response explains why it "
        "works:"))
    b.append(eq(
        "G(s) = (1 + T<sub>lead</sub>·s) / (1 + α·T<sub>lead</sub>·s)", "10.1"))
    b.append(eq(
        "y(t) = 1 + (1/α − 1)·e<sup>−t/(α·T<sub>lead</sub>)</sup>", "10.2"))
    b.append(p(
        "With α below one the block overshoots to 1/α at the instant of the step and then decays back to "
        "one. That is the shape in Figure 10-6: a spike, then a settling. Physically it is an extra push "
        "delivered immediately, exactly enough to keep pace with a fast reaction, withdrawn gradually as "
        "the slower reaction catches up. Choose α and you have chosen the size of the push; with α = 0.4 "
        "the block pushes 150 per cent harder for an instant, which is also why a lead term needs a "
        "filter or a clean measurement in front of it."))
    b.append(fig(6, F.fig_10_6(), "en"))

    b.append(h2("The drift that no amount of care removes", "§ 10.6"))
    b.append(p(
        "The chapter's most valuable paragraph is the shortest. We can be as careful as we want with our "
        "evaluation of the disturbances, but we never reach absolute perfect compensation; there are "
        "always factors not accounted for. The PV drifts, and the drift has to be corrected by hand or by "
        "adding feedback."))
    b.append(fig(8, F.fig_10_8(), "en"))
    b.append(p(
        "Figure 10-8 is that sentence as a graph. Red is feedforward alone: it removes most of the "
        "disturbance and leaves a residue that never goes away. Blue is the same block with a slow "
        "feedback loop added. The feedback does not need to be fast, because the feedforward block "
        "already handled the fast part; it only needs to be patient enough to collect the residue. That "
        "combination — fast feedforward, slow feedback — is the architecture of essentially every "
        "industrial feedforward scheme, and it is why pure feedforward is rare in practice."))

    b.append(h2("The worked example: a feed heater", "§ 10.6"))
    b.append(p(
        "Figure 10-7 is the chapter's one fully engineered case, and it repays slow reading because it "
        "encodes two design rules. Inlet flow is measured, converted straight into a heat demand, and "
        "that demand becomes the set point of a fuel flow loop:"))
    b.append(eq(
        "Q<sub>required</sub> = ṁ · c<sub>p</sub> · (T<sub>set</sub> − T<sub>in</sub>)", "10.3"))
    b.append(fig(7, F.fig_10_7(), "en"))
    b.append(p(
        "The first rule is in the formula. Heat demand depends on the temperature <em>difference</em>, "
        "not on the set point alone, so the inlet temperature has to be measured too. A feedforward "
        "block that reads only the flow is correct only while the inlet temperature happens to be "
        "constant. That is why the temperature transmitter appears in the diagram at all."))
    b.append(p(
        "The second rule is in the topology. The calculation's output does not drive the fuel valve; it "
        "drives the set point of a fuel flow controller, which drives the valve. Fuel supply pressure is "
        "a second disturbance, unmeasured and unmeasurable in any useful place, and the flow loop absorbs "
        "it without the feedforward block ever knowing it exists."))
    b.append(quote(
        "Each feedforward block should compensate exactly one disturbance. A second disturbance belongs "
        "to a fast inner feedback loop, not to the same block.",
        "The design rule Figure 10-7 illustrates"))
    b.append(p(
        "Trying to compensate both with one block produces a math function nobody can verify and nobody "
        "can tune. Splitting them produces two elements that can each be tested on their own — which is "
        "the whole reason the four-part structure of section 10.5 is worth insisting on."))

    b.append(h2("What the chapter is really teaching", "Closing"))
    b.append(p(
        "The chapter's closing comparison fits in a sentence: feedback corrects what has already gone "
        "wrong, feedforward prevents what is about to. Neither substitutes for the other. A good system "
        "has both — feedforward to keep the PV from moving, feedback to erase the residue that "
        "feedforward can never erase."))
    b.append(fig(9, F.fig_10_9(), "en"))
    b.append(p(
        "The cost side deserves equal billing. Feedforward demands an instrument for every disturbance "
        "you want to compensate, a model for every disturbance-to-PV relationship, and a person who "
        "understands both well enough to tune and maintain them. It also demands that the model be "
        "updated when the process changes: a block tuned for a clean heat exchanger compensates wrongly "
        "once the exchanger fouls, and it will compensate wrongly in a way that is invisible, because "
        "the feedback loop keeps the PV on set point and hides the error. In exchange, it is the only "
        "mechanism in this book capable of holding the PV still while a disturbance is acting."))
    return "".join(b)
