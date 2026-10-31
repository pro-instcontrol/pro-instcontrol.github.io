# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 5, Stability and Control Modes of
Closed Loops (Wolfgang Altmann, IDC Technologies)."""
import pc5fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 23
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Ổn định (stability)</em> — vòng kín không có dao động duy trì. · "
            "<em>Tần số tới hạn (critical frequency)</em> — tần số mà tại đó độ lệch pha vòng đạt 180°. · "
            "<em>K<sub>LOOP</sub></em> — hệ số khuếch đại tổng của vòng, bằng K<sub>C</sub> × K<sub>P</sub>. · "
            "<em>Sai lệch tĩnh (offset)</em> — sai lệch còn lại khi vòng đã xác lập. · "
            "<em>Dải tỉ lệ PB (proportional band)</em> — phần trăm thay đổi của PV làm đầu ra đi hết toàn dải. · "
            "<em>T<sub>INT</sub></em> — hằng số thời gian tích phân. · "
            "<em>T<sub>DER</sub></em> — hằng số thời gian vi phân. · "
            "<em>MANUAL</em> — giá trị nền của đầu ra, còn gọi là “manual reset”.")
    return note(
        "<b>Key terms.</b> <em>Stability</em> — the closed loop shows no sustained oscillation. · "
        "<em>Critical frequency</em> — the frequency at which the loop phase shift reaches 180°. · "
        "<em>K<sub>LOOP</sub></em> — the total loop gain, K<sub>C</sub> × K<sub>P</sub>. · "
        "<em>Offset</em> — the error left standing once the loop has settled. · "
        "<em>Proportional band</em> — the percentage of PV change that drives the output through its full "
        "range. · <em>T<sub>INT</sub></em> — the integral time constant. · "
        "<em>T<sub>DER</sub></em> — the derivative time constant. · "
        "<em>MANUAL</em> — the output bias, historically called “manual reset”.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Chương trước đã dựng xong cơ chế: đo sai lệch, tính tác động, tác động lên van. Chương này hỏi "
        "câu hỏi khó hơn — vòng kín đó có đứng yên được không, và ba chế độ P, I, D đóng góp gì vào việc "
        "giữ nó đứng yên. Toàn bộ chương được viết quanh một ví dụ duy nhất là lò gia nhiệt nguyên liệu "
        "trước tháp chưng cất, vì chính ví dụ đó chứa đủ cả độ trễ, thời gian chết và bốn loại nhiễu."))

    # ---------------------------------------------------------------- 5.1
    b.append(h2("5.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học xong chương này và làm các bài thực hành liên quan, sinh viên có thể:"))
    b.append(ul([
        "Chỉ ra ổn định là gì, và về mặt toán học thì nguyên nhân nào gây ra mất ổn định;",
        "Mô tả chức năng và cách dùng của điều khiển tỉ lệ, tích phân, vi phân và các tổ hợp của chúng;",
        "Chỉ ra những vấn đề nào trong điều khiển vòng kín do đâu mà có, và cách khắc phục.",
    ]))

    # ---------------------------------------------------------------- 5.2
    b.append(h2("5.2 Quá trình công nghiệp trong thực tế", "The Industrial Process in Practice"))
    b.append(p("Chương trước đã trình bày nguyên lý cơ bản của điều khiển vòng kín. Một tác động điều khiển "
               "được tính ra dựa trên độ lệch của PV so với giá trị mong muốn do SP đặt ra "
               "(ERR = PV − SP)."))
    b.append(p("Nhưng phải xét quá trình công nghiệp theo đúng cách nó vận hành ngoài đời thực. Ví dụ dùng "
               "xuyên suốt chương này là một <b>lò gia nhiệt nguyên liệu</b> — thiết bị làm nóng dòng nguyên "
               "liệu trước khi cấp vào tháp chưng cất. Xem <b>Hình 5-1</b>."))
    b.append(fig(1, F.fig_5_1(), "vi"))
    b.append(p("Mục tiêu của hệ là giữ nhiệt độ ra (T2) không đổi. Biến điều khiển là vị trí van nhiên liệu."))
    b.append(p("Cần lưu ý rằng vì lý do kinh tế và môi trường, điều khiển giới hạn chéo (cross limiting) của "
               "quá trình cháy thường là bắt buộc để giảm thiểu lượng carbon monoxide sinh ra. Trong ví dụ "
               "này, để đơn giản, ta bỏ qua hoàn toàn điều khiển giới hạn chéo và tác động trực tiếp lên vị "
               "trí van."))
    b.append(p("Ví dụ điều khiển lò gia nhiệt này sẽ là nơi ta soi vào các hệ quả thực tế của tính ổn định, "
               "của các chế độ điều khiển khác nhau, của các chiến lược điều khiển và của các bài thực hành. "
               "Vì vậy trước hết hãy xem kỹ đặc tính động học cơ bản và những nhiễu thường gặp nhất tác động "
               "lên hệ điều khiển này."))

    # ---------------------------------------------------------------- 5.3
    b.append(h2("5.3 Đặc tính động học của lò gia nhiệt", "Dynamic Behavior of the Feed Heater"))
    b.append(p("Có hai loại trễ lớn ảnh hưởng tới đặc tính động học của hệ lò này: trễ điều khiển và trễ do "
               "nhiễu."))

    b.append(h3("5.3.1 Trễ điều khiển", "Control Lag"))
    b.append(p("Giữa việc định vị van nhiên liệu và nhiệt độ ra luôn tồn tại một độ trễ. Lý do chính có thể "
               "thấy ngay: sau khi vị trí van nhiên liệu thay đổi, không phải toàn bộ nguyên liệu đang nằm "
               "trong lò được nung nóng cùng một lúc. Phần nguyên liệu nằm gần cửa ra sẽ rời lò ngay sau "
               "khi van đổi vị trí; phần khác ra muộn hơn. Đáp ứng điều khiển còn kèm theo một khoảng thời "
               "gian chết nhỏ."))

    b.append(h3("5.3.2 Trễ do nhiễu", "Disturbance Lags"))
    b.append(p("Tác động của nhiễu lên nhiệt độ ra cũng có tính trễ. Mỗi nhiễu có hằng số thời gian trễ "
               "riêng. Hầu hết nhiễu cũng kèm một khoảng thời gian chết nhỏ."))
    b.append(note(
        "<b>Ghi chú.</b> Không có khác biệt đo được giữa hai khâu trễ bậc cao — một khâu có thời gian chết "
        "nhỏ và một khâu không có. Nói cách khác, khi bậc của khâu trễ đã đủ lớn thì một khoảng chết nhỏ "
        "thêm vào không còn phân biệt được bằng phép đo thực nghiệm, và cũng không cần phân biệt: cả hai "
        "đều cho cùng một đáp ứng."))

    # ---------------------------------------------------------------- 5.4
    b.append(h2("5.4 Các nhiễu chính của lò gia nhiệt", "Major Disturbances of the Feed Heater"))
    b.append(p("Có bốn nhiễu CHÍNH có thể và sẽ được coi là tới hạn đối với vận hành ổn định của hệ:"))

    b.append(h3("5.4.1 Thay đổi áp suất dòng nhiên liệu", "Fuel Flow Pressure Changes"))
    b.append(p("Áp suất tăng làm lưu lượng nhiên liệu tăng, kéo nhiệt độ ra (T2) lên, và ngược lại."))

    b.append(h3("5.4.2 Thay đổi lưu lượng nguyên liệu", "Feed Flow Changes"))
    b.append(p("Vì lò phục vụ một quá trình khác ở phía hạ lưu (không dự đoán được), không có cách nào giữ "
               "lưu lượng nguyên liệu cố định. Lưu lượng này phụ thuộc hoàn toàn vào nhu cầu vật liệu của "
               "quá trình phía sau. Lưu lượng nguyên liệu tăng (do quá trình hạ lưu yêu cầu) làm nhiệt độ ra "
               "giảm, và ngược lại."))

    b.append(h3("5.4.3 Thay đổi áp suất đầu vào", "Feed Inlet Pressure Changes"))
    b.append(p("Nếu nguyên liệu ở dạng khí thì đây là vấn đề quan trọng. Cần biết lưu lượng khối lượng chứ "
               "không phải lưu lượng thể tích của dòng nguyên liệu. Khi áp suất tăng, lưu lượng khối lượng "
               "tăng, dẫn tới nhiệt độ ra giảm, và ngược lại."))

    b.append(h3("5.4.4 Thay đổi nhiệt độ đầu vào", "Feed Inlet Temperature Changes"))
    b.append(p("Nhiệt độ đầu vào càng cao thì càng phải gia nhiệt ít đi. Nhiệt độ đầu vào tăng làm nhiệt độ "
               "ra tăng, và ngược lại."))
    b.append(note(
        "<b>Đọc bốn nhiễu này theo dấu.</b> Hai nhiễu đầu (áp suất nhiên liệu, lưu lượng nguyên liệu) tác "
        "động theo chiều ngược nhau lên cùng một biến điều khiển, nên chúng không thể bù trừ lẫn nhau bằng "
        "một hệ số cố định. Đây chính là lý do vòng kín là bắt buộc: chỉ có phản hồi từ T2 mới phân biệt "
        "được “nhiệt độ giảm vì ít nhiên liệu” với “nhiệt độ giảm vì nhiều nguyên liệu hơn”."))

    # ---------------------------------------------------------------- 5.5
    b.append(h2("5.5 Tính ổn định", "Stability"))
    b.append(p("Một hệ điều khiển vòng kín là ổn định khi không có dao động duy trì. Không được lẫn lộn "
               "giữa vấn đề này với các hiệu ứng khác nhau mà nhiễu, tín hiệu nhiễu điện và mất ổn định gây "
               "ra cho hệ. Một tín hiệu ồn và bị nhiễu có thể hiện ra như một xu hướng dao động; nhưng không "
               "bao giờ được nhầm nó với mất ổn định của vòng."))
    b.append(p("Tiêu chuẩn ổn định gồm hai điều kiện:"))
    b.append(ul([
        "Hệ số khuếch đại vòng (K<sub>LOOP</sub>) tại <em>tần số tới hạn</em> nhỏ hơn 1;",
        "Độ lệch pha vòng tại <em>tần số tới hạn</em> nhỏ hơn 180°.",
    ]))

    b.append(h3("5.5.1 Hệ số khuếch đại vòng tại tần số tới hạn",
                "Loop Gain for Critical Frequency"))
    b.append(p("Xét trường hợp tổng hệ số khuếch đại của vòng, đối với một tín hiệu có tần số mà tại đó tổng "
               "độ lệch pha vòng bằng 180°. Nếu hệ số khuếch đại của vòng đối với tín hiệu đó nhỏ hơn 1 thì "
               "biên độ tín hiệu đang tắt dần. Hai khả năng còn lại là:"))
    b.append(ul([
        "Dao động duy trì, giữ nguyên biên độ (K<sub>LOOP</sub> = 1);",
        "Dao động duy trì và tăng dần, tức là xấu đi (K<sub>LOOP</sub> &gt; 1).",
    ]))

    b.append(h3("5.5.2 Độ lệch pha vòng tại tần số tới hạn",
                "Loop Phase Shift for Critical Frequency"))
    b.append(p("Xét trường hợp tổng độ lệch pha của vòng, đối với một tín hiệu có tần số mà tại đó tổng hệ "
               "số khuếch đại vòng bằng 1. Một tín hiệu có độ lệch pha 180° sẽ sinh ra dao động nếu hệ số "
               "khuếch đại vòng lớn hơn 1. Trường hợp này được minh họa trên <b>Hình 5-2</b>."))
    b.append(fig(2, F.fig_5_2(), "vi"))
    b.append(note(
        "<b>Ghi chú.</b><br>"
        "• Tăng hệ số khuếch đại hoặc tăng độ lệch pha làm vòng kín mất ổn định, nhưng làm nó đáp ứng nhanh "
        "và nhạy hơn.<br>"
        "• Giảm hệ số khuếch đại hoặc giảm độ lệch pha làm vòng kín ổn định hơn, nhưng đổi lại nó trở nên "
        "ì ạch hơn.<br>"
        "• Hệ số khuếch đại vòng K<sub>LOOP</sub> quyết định giá trị OFFSET của bộ điều khiển;<br>"
        "&nbsp;&nbsp;và offset thay đổi khi điểm đặt thay đổi."))
    b.append(quote(
        "Mọi tham số chỉnh định đều là một cuộc mặc cả giữa tốc độ đáp ứng và biên độ an toàn. Không có "
        "điểm nào cho cả hai cùng tốt hơn.",
        "Nguyên tắc chung của chương này"))

    # ---------------------------------------------------------------- 5.6
    b.append(h2("5.6 Điều khiển tỉ lệ", "Proportional Control"))
    b.append(p("Đây là phương thức điều khiển chủ yếu. Bộ điều khiển tự động phải hiệu chỉnh đầu ra OP của "
               "mình bằng một tác động <em>tỉ lệ với ERR</em>. Việc hiệu chỉnh bắt đầu từ một giá trị OP có "
               "sẵn tại thời điểm bắt đầu chế độ tự động."))

    b.append(h3("5.6.1 Sai lệch tỉ lệ và giá trị MANUAL", "Proportional Error and Manual Value"))
    b.append(p("Giá trị khởi đầu đó gọi là <b>MANUAL</b>. Trước đây người ta gọi nó là “MANUAL RESET”. Muốn "
               "có một hiệu chỉnh tự động — nghĩa là hiệu chỉnh tính từ mốc MANUAL — thì luôn cần một giá "
               "trị ERR khác không. Không có ERR thì không có hiệu chỉnh, và đầu ra quay về đúng giá trị "
               "MANUAL. Vì thế, để duy trì tác động hiệu chỉnh, luôn phải còn lại một sai lệch “dư” nhỏ."))
    b.append(p("Sai lệch dư này gọi là <b>OFFSET</b> — sai lệch tĩnh."))
    b.append(ul([
        "<b>ERR₀</b> là giá trị sai lệch sẽ có nếu hoàn toàn không có điều khiển;",
        "<b>K<sub>C</sub></b> là hệ số khuếch đại dùng để định cỡ tác động điều khiển dựa trên ERR;",
        "<b>K<sub>LOOP</sub></b> là hệ số khuếch đại tổng của vòng, bằng tích của HỆ SỐ KHUẾCH ĐẠI BỘ ĐIỀU "
        "KHIỂN (K<sub>C</sub>) và HỆ SỐ KHUẾCH ĐẠI QUÁ TRÌNH (K<sub>P</sub>).",
    ]))
    b.append(p("Hằng số chỉnh định duy nhất của điều khiển tỉ lệ là K<sub>C</sub>. K<sub>C</sub> càng lớn thì "
               "việc điều khiển hệ càng khó, càng nhạy (độ ổn định giảm)."))
    b.append(p("Khi K<sub>C</sub> lớn hơn, giá trị OFFSET nhỏ đi. Nếu hệ số khuếch đại quá lớn, ta sẽ gặp "
               "vấn đề ổn định. Các quan hệ dưới đây suy ra từ những điều vừa nói."))

    b.append(h3("5.6.2 Các quan hệ tỉ lệ", "Proportional Relationships"))
    b.append(eq("OP = K<sub>C</sub> × ERR + MANUAL", "5.1"))
    b.append(eq("K<sub>LOOP</sub> = K<sub>C</sub> × K<sub>P</sub>", "5.2"))
    b.append(eq("OFFSET = ERR₀ / (K<sub>LOOP</sub> + 1)", "5.3"))
    b.append(p("Ba quan hệ trên đủ để suy ra sai lệch tĩnh khi vòng đã xác lập. Xuất phát từ định nghĩa:"))
    b.append(eq("ERR = SP − PV"))
    b.append(eq("OP = K<sub>C</sub> × ERR"))
    b.append(eq("PV = ERR × K<sub>LOOP</sub>"))
    b.append(p("Thay vào định nghĩa sai lệch:"))
    b.append(eq("ERR = SP − ERR × K<sub>LOOP</sub>"))
    b.append(eq("⇒ ERR (1 + K<sub>LOOP</sub>) = SP"))
    b.append(p("Tại trạng thái xác lập:"))
    b.append(eq("ERR = SP / (1 + K<sub>LOOP</sub>)", "5.4"))
    b.append(p("Số hạng sai lệch (ERR) được định nghĩa là “Error = Indicated − Ideal”, tức là giá trị chỉ thị "
               "trừ giá trị lý tưởng, và được tạo ra như sau:"))
    b.append(eq("ERR(t) = SP(t) − PV(t)"))
    b.append(p("Công thức này cho thấy điểm đặt SP có thể biến thiên theo thời gian, tuy rằng trong phần lớn "
               "bài toán điều khiển quá trình, SP được giữ không đổi trong những khoảng thời gian dài. Với "
               "bộ điều khiển tỉ lệ, đầu ra tỉ lệ với tín hiệu sai lệch này:"))
    b.append(eq("OP<sub>C</sub>(t) = P + K<sub>C</sub> · E(t)", "5.5"))
    b.append(p("trong đó OP<sub>C</sub> là đầu ra của bộ điều khiển, P là giá trị nền của đầu ra (giá trị khởi "
               "đầu MANUAL), K<sub>C</sub> là hệ số khuếch đại của bộ điều khiển (thường không có đơn vị), và "
               "E là giá trị sai lệch. Từ đây ta có thể đánh giá một loạt khái niệm của điều khiển tỉ lệ."))

    b.append(h3("5.6.3 Đánh giá các khái niệm của điều khiển tỉ lệ",
                "Evaluation of Proportional Control Concepts"))
    b.append(ul([
        "Hệ số khuếch đại của bộ điều khiển (K<sub>C</sub>) có thể được chỉnh sao cho đầu ra OP<sub>C</sub> "
        "thay đổi nhạy với chênh lệch giữa SP và PV đúng như mong muốn.",
        "Dấu của K<sub>C</sub> có thể chọn (+ hoặc −) để OP<sub>C</sub> tăng hoặc giảm khi độ lệch ERR tăng.",
    ]))
    b.append(p("Trong bộ điều khiển tỉ lệ, giá trị MANUAL — tức giá trị khởi đầu của đầu ra — là chỉnh được. "
               "Vì đầu ra bằng đúng giá trị MANUAL khi sai lệch bằng không (SP = PV), người ta chỉnh MANUAL "
               "sao cho đầu ra của bộ điều khiển (và do đó biến điều khiển MV) nằm đúng tại giá trị xác lập "
               "danh định của nó."))
    b.append(p("Ví dụ, nếu đầu ra của bộ điều khiển điều khiển một van, MANUAL được chỉnh sao cho lưu lượng "
               "qua van bằng đúng giá trị xác lập danh định khi ERR = 0."))
    b.append(p("Sau đó hệ số khuếch đại K<sub>C</sub> được chỉnh. Với các bộ điều khiển thông dụng, K<sub>C</sub> "
               "là đại lượng không thứ nguyên, nghĩa là số hạng MANUAL và số hạng ERR có cùng đơn vị đo."))
    b.append(p("<b>Nhược điểm của bộ điều khiển tỉ lệ</b> là chúng không thể loại bỏ sai lệch xác lập xuất "
               "hiện sau khi điểm đặt thay đổi hoặc sau một thay đổi tải kéo dài."))

    b.append(h3("5.6.4 Dải tỉ lệ", "Proportional Band"))
    b.append(p("Dải tỉ lệ của bộ điều khiển thường được định nghĩa theo phần trăm: là tỉ số giữa giá trị đầu "
               "vào (PV) và một thay đổi toàn dải (100 %) của giá trị đầu ra (MV). Quan hệ giữa nó với hệ số "
               "khuếch đại K<sub>C</sub> là:"))

    b.append(eq("PB = (100 / K<sub>C</sub>) × 1", "5.6"))
    b.append(eq("Tỉ lệ: ΔMV = K<sub>C</sub> × ΔPV"))
    b.append(eq("Dải tỉ lệ %: ΔPV / ΔMV = 1 / K<sub>C</sub> khi ΔMV = 100 %"))
    b.append(fig(3, F.fig_5_3(), "vi"))
    b.append(p("Như trên <b>Hình 5-3</b>, nếu dải tỉ lệ PB của bộ điều khiển đặt ở 100 % (K<sub>C</sub> = 1) "
               "thì một thay đổi toàn dải của PV, từ 0 đến 100 %, sẽ làm MV thay đổi từ 0 đến 100 % — tức "
               "toàn bộ hành trình của van."))
    b.append(p("Nếu PB đặt ở 20 % (K<sub>C</sub> = 5) thì PV chỉ cần đi từ 40 % đến 60 % là MV đã đi hết từ "
               "0 đến 100 %, với cùng kết quả là van chạy từ đóng hoàn toàn sang mở hoàn toàn."))
    b.append(p("Tương tự, PB = 500 % (K<sub>C</sub> = 0,2) sẽ cho MV chỉ thay đổi từ 40 % đến 60 % khi PV đi "
               "từ 0 đến 100 %."))
    b.append(p("Vậy giá trị phần trăm PB cao cho đáp ứng kém nhạy hơn, còn giá trị phần trăm thấp cho đáp "
               "ứng nhạy hơn."))

    # ---------------------------------------------------------------- 5.7
    b.append(h2("5.7 Điều khiển tích phân", "Integral Control"))
    b.append(p("Tác động tích phân được dùng để điều khiển về phía không còn OFFSET ở tín hiệu ra. Nghĩa là "
               "nó điều khiển về phía KHÔNG CÒN SAI LỆCH (ERR = 0). Điều khiển tích phân thường được dùng "
               "để hỗ trợ điều khiển tỉ lệ; tổ hợp của cả hai gọi là điều khiển PI."))

    b.append(h3("5.7.1 Công thức tích phân và tỉ lệ – tích phân",
                "Integral and Proportional-plus-Integral Formula"))
    b.append(p("Công thức cho điều khiển I:"))
    b.append(eq("OP = (K / T<sub>INT</sub>) ∫ ERR dt", "5.7"))
    b.append(p("Công thức cho điều khiển PI:"))
    b.append(eq("OP = (K / T<sub>INT</sub>) ∫ ERR dt + K · ERR + MANUAL", "5.8"))
    b.append(p("trong đó T<sub>INT</sub> là hằng số thời gian tích phân."))
    b.append(p("Vì điều khiển tích phân lấy tích phân sai lệch theo thời gian, tác động điều khiển càng lớn "
               "khi sai lệch còn tồn tại càng lâu. Việc tích phân sai lệch diễn ra cho đến khi không còn sai "
               "lệch nữa. Mọi tác động tích phân đều kèm một độ trễ pha 90°; độ lệch pha này có tác dụng "
               "làm mất ổn định. Vì lý do đó, rất hiếm khi dùng điều khiển I mà không có điều khiển P."))

    b.append(h3("5.7.2 Tác động tích phân", "Integral Action"))
    b.append(p("Hãy ôn lại vài nguyên lý giải tích và lượng giác liên quan đến phép tính tích phân, đặc biệt "
               "là tích phân của một sóng sin. <b>Hình 5-4</b> cho thấy độ trễ pha do phép tích phân gây ra "
               "trên một sóng sin. Hiệu ứng y hệt cũng xuất hiện khi dùng tác động tích phân trong một hệ "
               "điều khiển vòng kín."))
    b.append(fig(4, F.fig_5_4(), "vi"))
    b.append(p("Tác động tích phân cộng thêm vào độ trễ pha vốn có. Đỉnh của sóng sin sau khi lấy tích phân "
               "rơi đúng vào lúc sóng sin bắt đầu quay trở lại."))
    b.append(fig(5, F.fig_5_5(), "vi"))
    b.append(p("Nếu coi giá trị của số hạng ERR là không đổi (“xác lập”), thì sau khi hoàn tất mỗi hằng số "
               "thời gian T<sub>INT</sub>, đầu ra tích phân sẽ tăng thêm một lượng bằng ERR × K<sub>C</sub>, "
               "theo dạng một đường dốc đều như trên <b>Hình 5-5</b>."))

    b.append(h3("5.7.3 Tác động tích phân trong thực tế", "Integral Action in Practice"))
    b.append(p("Trong thực tế, khi đầu ra tích phân tăng lên và đi qua quá trình, PV sẽ tiến về giá trị SP và "
               "số hạng ERR sẽ giảm về độ lớn. Điều này làm giảm tốc độ thay đổi trong mỗi khoảng thời gian "
               "tích phân, dẫn tới dạng đáp ứng “cong” bậc một quen thuộc như trên <b>Hình 5-6</b>."))
    b.append(fig(6, F.fig_5_6(), "vi"))
    b.append(p("Nếu tốc độ thay đổi — tức giá trị đặt trên T<sub>INT</sub> — quá nhỏ, cộng với độ trễ pha 90° "
               "của tác động tích phân, thì dao động có thể xuất hiện. Về bản chất, đó là việc áp dụng một "
               "hiệu chỉnh quá mức <em>về mặt thời gian</em> lên giá trị của số hạng offset."))
    b.append(p("Nếu điều này xảy ra với một hệ điều khiển vòng kín trong công nghiệp, ta có một vấn đề ổn "
               "định."))
    b.append(quote(
        "Điều khiển tích phân loại bỏ OFFSET bằng cái giá là tính ổn định.",
        "Kết luận của mục 5.7"))
    b.append(p("Kết luận rút ra là phải rất thận trọng khi dùng điều khiển tích phân cho một hệ vòng kín vốn "
               "đã có xu hướng mất ổn định."))

    # ---------------------------------------------------------------- 5.8
    b.append(h2("5.8 Điều khiển vi phân", "Derivative Control"))
    b.append(p("Mục đích duy nhất của điều khiển vi phân là <em>thêm tính ổn định</em> cho một hệ điều khiển "
               "vòng kín."))
    b.append(p("Độ lớn của tác động vi phân (điều khiển D) tỉ lệ với tốc độ thay đổi (tức độ nhanh) của PV."))
    b.append(p("Vì tốc độ thay đổi của nhiễu điện có thể rất lớn, dùng điều khiển D để tăng tính ổn định cho "
               "vòng điều khiển đồng nghĩa với việc khuếch đại nhiễu. Bản thân điều khiển D không có mục "
               "đích gì riêng, nên nó luôn được dùng kết hợp với điều khiển P hoặc PI, tạo thành điều khiển "
               "PD hoặc PID. Khi cần tác động vi phân thì phần lớn người ta dùng PID."))

    b.append(h3("5.8.1 Công thức vi phân", "Derivative Formula"))
    b.append(p("Công thức cho điều khiển D:"))
    b.append(eq("OP = K · T<sub>DER</sub> · (dERR / dt)", "5.9"))
    b.append(p("trong đó T<sub>DER</sub> là hằng số thời gian vi phân."))
    b.append(p("Một lần nữa, dùng các nguyên lý giải tích và lượng giác liên quan đến phép tính vi phân — đặc "
               "biệt là trường hợp lấy vi phân một sóng sin — ta rút ra được những nguyên lý sau."))
    b.append(fig(7, F.fig_5_7(), "vi"))
    b.append(p("<b>Hình 5-7</b> cho thấy độ vượt pha do phép vi phân gây ra trên một sóng sin. Hiệu ứng y hệt "
               "cũng xuất hiện khi dùng tác động vi phân trong một hệ điều khiển vòng kín."))
    b.append(p("Tác động vi phân có thể loại bỏ một phần hoặc toàn bộ độ trễ pha đang có. Về lý thuyết, điều "
               "này đạt được nhờ đầu ra của hàm vi phân lập tức tiến tới một giá trị vô cùng lớn ngay khi "
               "thấy ERR thay đổi."))

    b.append(h3("5.8.2 Tác động vi phân trong thực tế", "Derivative Action in Practice"))
    b.append(p("Trong thực tế, đầu ra sẽ nhảy tới một giá trị bằng khoảng 8 lần độ thay đổi của ERR. Sau đó "
               "đầu ra giảm dần, mất 63,2 % biên độ sau mỗi đơn vị thời gian vi phân, như trên "
               "<b>Hình 5-8</b>."))
    b.append(fig(8, F.fig_5_8(), "vi"))
    b.append(fig(9, F.fig_5_9(), "vi"))
    b.append(p("Như <b>Hình 5-9</b>, điều khiển vi phân không có chức năng gì khi đứng một mình: khi sai lệch "
               "đã ổn định, đầu ra vi phân bằng không và không còn tác động nào được tạo ra."))

    b.append(h3("5.8.3 Tóm tắt quan hệ chức năng của tích phân và vi phân",
                "Summary of Integral and Derivative Functional Relationships"))
    b.append(p("Có thể coi phép tích phân như việc nạp một tụ điện từ một nguồn áp không đổi, qua một điện "
               "trở. Điện áp trên tụ tăng từ 0 theo dạng hàm mũ, vì chênh lệch giữa điện áp nguồn và điện áp "
               "tụ giảm dần theo thời gian."))
    b.append(p("Tác động vi phân về bản chất là phép đảo ngược của ví dụ tích phân. Lấy một tụ điện đã nạp "
               "đầy và xả nó qua một điện trở sẽ cho một suy giảm hàm mũ, vì chênh lệch điện áp trên tụ giảm "
               "từ giá trị cực đại về không."))
    b.append(p("Thoạt nhìn, có vẻ như hai hàm tích phân và vi phân — vì là đảo ngược của nhau — sẽ triệt tiêu "
               "lẫn nhau. Nhưng phải nhớ rằng số hạng ERR là đại lượng động và luôn thay đổi."))
    b.append(p("Giữa T<sub>INT</sub> và T<sub>DER</sub> và thời gian của quá trình hay vòng (T<sub>PROC</sub>) "
               "có một tỉ lệ khá chặt. Các quan hệ này được trình bày ở chương tám (Các thủ tục chỉnh định "
               "hệ thống)."))

    # ---------------------------------------------------------------- 5.9
    b.append(h2("5.9 Các chế độ tỉ lệ, tích phân và vi phân",
                "Proportional, Integral and Derivative Modes"))
    b.append(p("Phần lớn các bộ điều khiển được thiết kế để làm việc như bộ điều khiển PID."))

    b.append(h3("5.9.1 Bật/tắt chức năng tích phân và vi phân",
                "Enabling/Disabling Integral and Derivative Functions"))
    b.append(ul([
        "Nếu không muốn có tác động vi phân, đặt T<sub>DER</sub> (hằng số thời gian vi phân) bằng 0.",
        "Nếu không muốn có tác động tích phân, đặt T<sub>INT</sub> (hằng số thời gian tích phân) bằng một "
        "giá trị lớn, ví dụ 999 phút.",
    ]))
    b.append(p("Phần lớn các bộ điều khiển chỉ làm việc như bộ điều khiển I khi K được đặt bằng 0. Trong "
               "trường hợp đó, một hệ số khuếch đại đơn vị bằng 1 được áp dụng riêng cho tác động tích phân. "
               "Khái niệm bộ điều khiển PID được thể hiện trên <b>Hình 5-10</b>."))
    b.append(fig(10, F.fig_5_10(), "vi"))
    b.append(p("Ở chương tám, “Chỉnh định bộ điều khiển trong điều khiển vòng kín”, ta sẽ xem lại các phương "
               "pháp thông dụng nhất để chỉnh định bộ điều khiển P, PI và PID. Ở giai đoạn này, cần nhận thức "
               "được phép cân bằng cần thiết để tối ưu hóa tác động điều khiển."))

    # ---------------------------------------------------------------- 5.10
    b.append(h2("5.10 I.S.A và “Allen Bradley”", "I.S.A versus “Allen Bradley”"))
    b.append(p("Các hàm PID, khi xét trong một hệ số (PLC), tương ứng với một quá trình mà ở đó đầu ra của bộ "
               "điều khiển được thiết kế để lái biến quá trình (PV) về phía giá trị điểm đặt (SP). Chênh lệch "
               "giữa PV và SP là giá trị sai lệch của hệ, và các hàm PID tác động lên chính giá trị đó. Sai "
               "lệch càng lớn thì tín hiệu ra càng lớn."))
    b.append(p("ISA (Instrument Society of America — Hiệp hội Thiết bị Đo lường Hoa Kỳ) có một bộ quy tắc làm "
               "cho các hàm P, I và D phụ thuộc lẫn nhau; ví dụ hệ PLC Allen Bradley thì làm việc được với cả "
               "hai kiểu: hệ số khuếch đại phụ thuộc (ISA) hoặc độc lập."))
    b.append(p("Chương tám (Chỉnh định bộ điều khiển PID) sẽ minh họa sự khác nhau này."))
    b.append(note(
        "<b>Vì sao chuyện này lại quan trọng.</b> Với kiểu phụ thuộc (ISA), K<sub>C</sub> là hệ số khuếch đại "
        "chung và T<sub>INT</sub>, T<sub>DER</sub> là thời gian; đổi K<sub>C</sub> sẽ đổi luôn cả độ lớn của "
        "tác động tích phân và vi phân. Với kiểu độc lập, mỗi nhánh có hệ số khuếch đại riêng, nên chỉnh một "
        "tham số không kéo theo hai tham số kia. Cùng một bộ số {K<sub>C</sub>, T<sub>INT</sub>, "
        "T<sub>DER</sub>} đem áp vào hai kiểu sẽ cho hai đáp ứng khác nhau — đây là lý do phổ biến nhất khiến "
        "một vòng “chạy tốt trên máy này mà hỏng trên máy kia”."))

    # ---------------------------------------------------------------- 5.11
    b.append(h2("5.11 Quan hệ và tương tác giữa P, I và D",
                "P, I and D Relationships and Related Interactions"))
    b.append(p("Điều khiển P là phương thức điều khiển chủ yếu và phải đảm nhận phần lớn công việc. Điều khiển "
               "I được thêm vào một cách thận trọng, chỉ để loại bỏ OFFSET mà điều khiển P để lại. Điều khiển "
               "D có mặt chỉ vì tính ổn định: phải chỉnh sao cho hiệu ứng ổn định của nó lớn hơn hiệu ứng mất "
               "ổn định của điều khiển I."))
    b.append(p("Trong những trường hợp không có xu hướng mất ổn định, người ta không dùng điều khiển D. Đa số "
               "ứng dụng lưu lượng thuộc nhóm này."))

    # ---------------------------------------------------------------- 5.12
    b.append(h2("5.12 Ứng dụng của các chế độ điều khiển quá trình",
                "Applications of Process Control Modes"))

    b.append(h3("5.12.1 Chế độ tỉ lệ (P)", "Proportional Mode (P)"))
    b.append(p("Dạng điều khiển cơ bản nhất. Dùng được khi sai lệch tĩnh còn lại ở đầu ra là hằng và chấp "
               "nhận được. Mức độ tác động thay đổi theo hệ số khuếch đại K<sub>C</sub>."))

    b.append(h3("5.12.2 Chế độ tỉ lệ – tích phân (PI)", "Proportional and Integral Mode (PI)"))
    b.append(p("Có thể thêm điều khiển tích phân vào điều khiển tỉ lệ để loại bỏ sai lệch tĩnh khỏi đầu ra. "
               "Dùng được khi không có vấn đề ổn định, ví dụ trong một vòng điều khiển lưu lượng “chặt” "
               "(đáp ứng nhanh, ít trễ)."))

    b.append(h3("5.12.3 Chế độ tỉ lệ – tích phân – vi phân (PID)",
                "Proportional, Integral and Derivative Mode (PID)"))
    b.append(p("Đây là bộ điều khiển ba số hạng đầy đủ, dùng ở nơi xuất hiện mất ổn định do việc dùng chế độ "
               "tích phân. Hàm vi phân khuếch đại nhiễu, và điều này phải được tính đến khi dùng đủ cả ba số "
               "hạng."))

    b.append(h3("5.12.4 Chế độ tỉ lệ – vi phân (PD)", "Proportional and Derivative Mode (PD)"))
    b.append(p("Chế độ này dùng khi quá trình có vấn đề quá nhiều về độ trễ hoặc quán tính."))

    b.append(h3("5.12.5 Chế độ tích phân (I)", "Integral Mode (I)"))
    b.append(p("Chế độ này gần như chỉ dùng cho bộ điều khiển sơ cấp trong cấu hình nối tầng (cascade). Mục "
               "đích là ngăn đầu ra của bộ điều khiển sơ cấp tạo ra một “bước nhảy” khi điểm đặt của bộ điều "
               "khiển bị thay đổi."))
    b.append(table(
        ["Chế độ", "Ký hiệu", "Dùng khi", "Cái giá phải trả"],
        [["Tỉ lệ", "P", "Sai lệch tĩnh hằng và chấp nhận được; quá trình ít trễ",
          "Luôn còn offset; offset đổi khi SP đổi"],
         ["Tỉ lệ – tích phân", "PI", "Cần khử offset; vòng “chặt” như lưu lượng, áp suất",
          "Thêm 90° trễ pha, giảm biên độ ổn định"],
         ["Tỉ lệ – tích phân – vi phân", "PID", "Có mất ổn định do khâu I gây ra; quá trình nhiều trễ",
          "Khuếch đại nhiễu điện; khó chỉnh định hơn"],
         ["Tỉ lệ – vi phân", "PD", "Quá trình quán tính lớn, nhiều trễ, không cần khử offset",
          "Không bao giờ khử được offset"],
         ["Tích phân", "I", "Bộ điều khiển sơ cấp trong cấu hình nối tầng",
          "Chậm; một mình thì không ổn định"]],
        "Bảng 5-1 · Năm tổ hợp chế độ điều khiển và trường hợp sử dụng tương ứng."))

    # ---------------------------------------------------------------- 5.13
    b.append(h2("5.13 Đầu ra điển hình của bộ điều khiển PID",
                "Typical PID Controller Outputs"))
    b.append(p("Ba chế độ không phải ba lựa chọn ngang nhau, mà là ba cách xử lý cùng một sai lệch. "
               "<b>Hình 5-11</b> cho thấy chúng khác nhau ở đâu khi cùng nhận một bậc thang điểm đặt."))
    b.append(fig(11, F.fig_5_11(), "vi"))
    b.append(p("Chế độ P đi lên nhanh rồi dừng lại ở một khoảng cách phía dưới điểm đặt — khoảng cách đó "
               "chính là sai lệch tĩnh, và nó không tự mất đi. Chế độ PI đi lên chậm hơn nhưng cuối cùng "
               "chạm đúng điểm đặt. Chế độ PID đi lên nhanh nhất và ít vọt lố nhất, nhưng chỉ khi "
               "T<sub>DER</sub> được chọn đúng; nếu không, chính khâu vi phân lại là thứ gây ra vọt lố."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản gốc có năm bài thực hành (Exercise 2 đến Exercise 6) nằm rải "
        "trong chương này; chúng gắn với bộ thiết bị mô phỏng kèm theo giáo trình và không có nội dung lý "
        "thuyết riêng nên không được dịch ở đây. Phần lý thuyết của chương — từ mục 5.1 đến 5.13 — đã được "
        "dịch đầy đủ."))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "The previous chapter built the mechanism: measure the error, compute an action, apply it to the "
        "valve. This chapter asks the harder question — will that closed loop stand still, and what do the "
        "three modes P, I and D contribute to keeping it still. The whole chapter is written around one "
        "example, a feed heater ahead of a distillation column, because that example carries all of it at "
        "once: lag, dead time and four separate disturbances."))

    b.append(h2("Stability is a phase problem, not an amplitude problem"))
    b.append(p("The textbook condition for stability is usually stated as two inequalities — loop gain below "
               "one at the critical frequency, phase shift below 180° — and it is easy to read that as a "
               "statement about gain. It is not. Gain only decides what happens at the frequency where the "
               "loop already inverts its own signal. A loop with a gain of fifty is perfectly stable if its "
               "phase never reaches 180° inside the band where it has any authority; a loop with a gain of "
               "0.9 will ring forever if the phase crosses 180° exactly where the gain is 0.9."))
    b.append(p("This is why dead time is so much more dangerous than lag. A first-order lag can never produce "
               "more than 90° of phase shift, no matter how slow it is; you can stack two of them and still "
               "stay below 180°. A dead time produces phase shift proportional to frequency and unbounded: "
               "180° is reached at some frequency always, and what you control is only whether the gain has "
               "fallen below one by then. Every tuning rule in the literature is, at bottom, a way of "
               "guessing where that crossing happens without having to measure it."))

    b.append(h2("Why proportional control can never finish the job"))
    b.append(p("A proportional controller is a spring. Push the process away from the set point and the "
               "controller pushes back harder the further it is pushed, which is exactly what a spring does. "
               "But a spring only exerts force when it is displaced. If the loop must hold a steady load — a "
               "constant flow of feed that needs a constant flow of fuel — the controller must hold a steady "
               "output, and a steady output requires a steady non-zero input. The error is not a defect of "
               "the tuning; it is the price of the force."))
    b.append(p("Equation 5.4 makes the trade explicit: the offset is inversely proportional to one plus the "
               "loop gain. You can buy it down by raising gain, but you buy it with stability, and the "
               "exchange rate worsens as the dead time grows. For a loop with a lot of dead time, getting "
               "the offset below one percent may require a gain that leaves no margin at all. That is the "
               "point at which integral action stops being optional."))

    b.append(h2("Integral action: the slow, patient cure that can kill the patient"))
    b.append(p("Integral action is the only mechanism in the controller that knows about the past. It "
               "accumulates error and keeps pushing until the accumulation stops, which means it can only "
               "stop pushing when the error is exactly zero. That is its virtue and its danger in one "
               "sentence: it will remove an offset no proportional band can remove, and it will keep pushing "
               "through the moment when the process has already arrived and the controller has not noticed."))
    b.append(p("The 90° of phase lag is the mechanism of the danger. Add 90° from the integral term to 90° "
               "from the process lag and you are at 180° with nothing else in the loop. This is why the rule "
               "“never use I without P” is not a stylistic preference: the proportional term supplies the "
               "restoring force that stops the integrator from overrunning, and without it the loop has no "
               "damping at all."))
    b.append(p("Integral windup is the same problem in its most common industrial form. When the output "
               "saturates — the valve is fully open and the temperature is still low — the integrator "
               "continues to accumulate an error it cannot do anything about. When the process finally "
               "arrives, the accumulated total has to be unwound before the output starts falling, and the "
               "overshoot is proportional to how long the saturation lasted. Every modern controller "
               "therefore limits the integrator, either by freezing it at the output clamp or by "
               "back-calculating from it."))

    b.append(h2("Derivative: expensive, noisy, and sometimes indispensable"))
    b.append(p("Derivative action is the only term that looks forward, and it does so by extrapolating the "
               "current slope. On a clean signal this is exactly the lead the loop needs: the controller "
               "starts backing off before the variable arrives, which is the only way to get a fast response "
               "without overshoot. On a real signal, the slope is dominated by whatever noise is sitting on "
               "the measurement, and the derivative of noise is enormous. The result is a controller that "
               "twitches the valve continuously and wears out the packing."))
    b.append(p("Hence the standard practice: derivative is used on temperature and composition loops, where "
               "the measurement is smooth and the process is slow, and it is not used on flow and pressure "
               "loops, where the measurement is fast and noisy and the process has almost no lag to "
               "compensate. The mode is not a measure of sophistication. A flow loop with derivative turned "
               "on is a worse loop, not a better one."))

    b.append(h2("Tuning is a negotiation, not a calculation"))
    b.append(p("The three constants are not independent, and no formula produces them from first principles. "
               "What every tuning method does is pick a point on a curve of trade-offs: speed against "
               "robustness, offset against oscillation, disturbance rejection against set-point tracking. "
               "Two engineers can tune the same loop to the same numbers and get different behaviour, "
               "because the plant changed between the two visits — a fouled heat exchanger, a worn valve "
               "trim, a different feed."))
    b.append(p("The practical consequence is that a loop should be tuned for the worst condition it will "
               "actually meet, not the cleanest one available on commissioning day, and that the tuning "
               "should be recorded along with the date and the plant condition it was done under. A tuning "
               "constant without that context is a number without a meaning."))
    return "\n".join(b)
