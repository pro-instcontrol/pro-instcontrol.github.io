# -*- coding: utf-8 -*-
"""Handbook Chapter 19 — Frequency Measurement (Michael A. Lombardi, NIST).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch19.py
"""
import os

import hb19fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch19-frequency-measurement"
TITLE_EN = "Frequency Measurement"
TITLE_VI = "Đo tần số"
BYLINE = "Michael A. Lombardi · National Institute of Standards and Technology (NIST)"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch18-time-measurement"
PREV_VI = "ch18-time-measurement"
PREV_T_EN = "Time Measurement"
PREV_T_VI = "Đo thời gian"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-19-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def table(head, rows, cap):
    th = "".join("<th>%s</th>" % c for c in head)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % (th, tr, cap))


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Tần số là tốc độ xuất hiện của một biến cố lặp lại. Nếu T là chu kỳ của một biến cố lặp lại "
        "thì tần số f = 1/T. Hệ Đơn vị Quốc tế (SI) quy định chu kỳ luôn biểu diễn bằng giây (s) và tần số "
        "luôn biểu diễn bằng hertz (Hz). Tần số của tín hiệu điện thường được đo bằng kilohertz (kHz) "
        "hoặc megahertz (MHz), với 1 kHz = 1.000 (10³) chu kỳ/giây và 1 MHz = 1 triệu (10⁶) chu kỳ/giây."))
    b.append(p(
        "Tần số trung bình trong một khoảng thời gian có thể đo rất chính xác. Khoảng thời gian là một "
        "trong bốn chuẩn đo lường cơ bản (ba chuẩn còn lại là độ dài, khối lượng và nhiệt độ). Trong bốn "
        "chuẩn này, khoảng thời gian (và tần số) có thể đo với độ phân giải cao nhất và độ không đảm bảo "
        "nhỏ nhất. Ở một số lĩnh vực đo lường, 1 phần triệu (1 × 10⁻⁶) đã được coi là thành tựu lớn; trong "
        "đo lường tần số, các phép đo 1 phần tỷ (1 × 10⁻⁹) là thường ngày, và cả 1 phần nghìn tỷ "
        "(1 × 10⁻¹²) cũng phổ biến."))
    b.append(p(
        "Thiết bị tạo ra một tần số đã biết gọi là chuẩn tần số (frequency standard). Những thiết bị này "
        "phải được hiệu chuẩn để luôn nằm trong dung sai mà ứng dụng của người dùng yêu cầu. Phần này bắt "
        "đầu bằng tổng quan về hiệu chuẩn tần số."))

    # ---- 19.1
    b.append(h2("19.1 Tổng quan về đo tần số và hiệu chuẩn",
                "Overview of Frequency Measurements and Calibration"))
    b.append(p(
        "Hiệu chuẩn tần số đo hiệu năng của các chuẩn tần số. Chuẩn tần số đang được hiệu chuẩn gọi là "
        "thiết bị cần kiểm (device under test — DUT). Trong đa số trường hợp, DUT là bộ dao động thạch anh, "
        "rubidi hoặc xêzi. Để thực hiện hiệu chuẩn, DUT phải được so với một chuẩn hay tham chiếu. Chuẩn "
        "phải vượt trội DUT theo một tỉ số xác định để phép hiệu chuẩn hợp lệ. Tỉ số này gọi là tỉ số không "
        "đảm bảo thử nghiệm (test uncertainty ratio — TUR). TUR 10:1 là mong muốn, nhưng không phải lúc nào "
        "cũng đạt được. Nếu dùng TUR nhỏ hơn (ví dụ 5:1) thì phép hiệu chuẩn sẽ mất nhiều thời gian hơn."))
    b.append(p(
        "Khi hiệu chuẩn xong, nhà đo lường phải nêu được đầu ra của DUT gần tần số danh định (nameplate) "
        "tới đâu. Tần số danh định được ghi trên đầu ra bộ dao động. Ví dụ, một DUT có đầu ra ghi “5 MHz” "
        "được kỳ vọng tạo ra tần số 5 MHz. Phép hiệu chuẩn đo hiệu giữa tần số thực và tần số danh định; "
        "hiệu này gọi là độ lệch tần số (frequency offset). Có xác suất cao rằng độ lệch tần số sẽ nằm "
        "trong một dải giá trị nhất định, gọi là độ không đảm bảo tần số. Người dùng quy định một độ lệch "
        "tần số và một yêu cầu không đảm bảo đi kèm mà DUT phải đạt hoặc vượt. Trong nhiều trường hợp, người "
        "dùng dựa trên chỉ tiêu của nhà sản xuất; trong trường hợp khác, họ có thể “nới” yêu cầu và dùng "
        "chỉ tiêu ít khắt khe hơn. Khi DUT đạt chỉ tiêu, nó đã được hiệu chuẩn thành công. Nếu không đạt, "
        "nó trượt hiệu chuẩn và bị sửa chữa hoặc loại khỏi sử dụng."))
    b.append(p(
        "Chuẩn dùng để hiệu chuẩn phải có khả năng truy xuất (traceable). Định nghĩa của Tổ chức Tiêu chuẩn "
        "hoá Quốc tế (ISO) về truy xuất là:"))
    b.append('<blockquote class="quote">Tính chất của kết quả một phép đo hay giá trị của một chuẩn, nhờ '
             'đó nó có thể liên hệ tới những tham chiếu đã nêu, thường là chuẩn quốc gia hay quốc tế, '
             'thông qua một chuỗi so sánh không đứt đoạn, tất cả đều có độ không đảm bảo đã nêu [1].'
             '</blockquote>')
    b.append(p(
        "Tại Hoa Kỳ, “chuỗi so sánh không đứt đoạn” phải truy ngược về Viện Tiêu chuẩn và Công nghệ Quốc "
        "gia (NIST). Ở một số lĩnh vực hiệu chuẩn, truy xuất được thiết lập bằng cách gửi chuẩn tới NIST "
        "(hoặc một phòng thí nghiệm truy xuất NIST) để hiệu chuẩn, hoặc gửi một bộ vật liệu tham chiếu cho "
        "người dùng. Cả hai cách đều không thực tế khi hiệu chuẩn tần số. Bộ dao động nhạy với điều kiện môi "
        "trường thay đổi, đặc biệt với việc bật/tắt. Nếu một bộ dao động được hiệu chuẩn rồi tắt đi, phép "
        "hiệu chuẩn có thể không còn giá trị khi bật lại. Ngoài ra, rung động và thay đổi nhiệt độ khi vận "
        "chuyển cũng có thể làm thay đổi kết quả. Vì những lý do này, các phòng thí nghiệm nên hiệu chuẩn "
        "tại chỗ."))
    b.append(p(
        "May mắn thay, có thể dùng chuẩn chuyển tiếp (transfer standard) để đưa một tham chiếu tần số từ "
        "chuẩn quốc gia tới phòng hiệu chuẩn. Chuẩn chuyển tiếp là thiết bị nhận và xử lý tín hiệu vô tuyến "
        "cung cấp tần số truy xuất NIST. Tín hiệu vô tuyến chính là mối liên kết trở về chuẩn quốc gia. Có "
        "nhiều loại tín hiệu, gồm các đài NIST WWV và WWVB, và tín hiệu dẫn đường vô tuyến từ LORAN-C và "
        "GPS. Mỗi tín hiệu cung cấp truy xuất NIST ở một mức không đảm bảo đã biết. Khả năng dùng chuẩn "
        "chuyển tiếp là lợi thế to lớn: nó cho phép hiệu chuẩn truy xuất đồng thời tại nhiều nơi miễn là mỗi "
        "nơi có một máy thu vô tuyến; nó cũng loại bỏ việc di chuyển chuẩn tần số từ nơi này sang nơi khác."))
    b.append(p(
        "Khi đã có một chuẩn chuyển tiếp truy xuất, bước tiếp theo là xây dựng quy trình kỹ thuật dùng để "
        "hiệu chuẩn, gọi là phương pháp hiệu chuẩn. Phòng thí nghiệm phải định nghĩa và ghi lại phương pháp, "
        "và lý tưởng là xây dựng một hệ đo tự động hoá quy trình. ISO/IEC Guide 25 nêu rằng phòng thí nghiệm "
        "phải dùng phương pháp và quy trình thích hợp cho mọi phép hiệu chuẩn và thử nghiệm, phù hợp với độ "
        "chính xác yêu cầu; và nên chọn những phương pháp đã công bố trong tiêu chuẩn quốc tế/quốc gia, của "
        "các tổ chức kỹ thuật có uy tín, hoặc trong tài liệu khoa học liên quan [2,3]. Vì vậy, phòng hiệu "
        "chuẩn nên tự động hoá quá trình hiệu chuẩn tần số bằng một phương pháp được ghi chép và thiết lập "
        "tốt; điều này giúp đảm bảo mỗi phép hiệu chuẩn đều có chất lượng cao nhất quán, và là điều kiện "
        "thiết yếu nếu phòng muốn đăng ký ISO hoặc được công nhận."))

    # ---- 19.2
    b.append(h2("19.2 Các chỉ tiêu: độ không đảm bảo tần số và độ ổn định",
                "The Specifications: Frequency Uncertainty and Stability"))
    b.append(p(
        "Phần này xem xét hai chỉ tiêu chính của một phép hiệu chuẩn tần số: độ không đảm bảo và độ ổn định."))
    b.append(h3("Độ không đảm bảo tần số", "Frequency Uncertainty"))
    b.append(p(
        "Như đã nêu, hiệu chuẩn tần số đo xem DUT có đạt hay vượt yêu cầu không đảm bảo của nó hay không. "
        "Theo ISO, độ không đảm bảo là “tham số gắn với kết quả một phép đo, đặc trưng cho sự phân tán của "
        "các giá trị có thể gán hợp lý cho đại lượng đo” [1]. Khi hiệu chuẩn tần số, đại lượng đo là một "
        "DUT được kỳ vọng tạo ra một tần số cụ thể. Ví dụ, DUT có đầu ra ghi 5 MHz được kỳ vọng tạo ra tần "
        "số 5 MHz. Dĩ nhiên DUT thực tế tạo ra tần số không đúng hẳn 5 MHz. Sau khi hiệu chuẩn, ta có thể "
        "nêu độ lệch tần số và độ không đảm bảo đi kèm."))
    b.append(p(
        "Đo độ lệch tần số đòi hỏi so sánh DUT với một tham chiếu, thường bằng cách so pha giữa tần số do "
        "DUT tạo ra và tần số do tham chiếu tạo ra. Có vài phương pháp hiệu chuẩn (bàn sau) cho phép xác "
        "định điều này. Khi đã biết lượng lệch pha và khoảng đo, ta có thể ước lượng độ lệch tần số của "
        "DUT. Khoảng đo là khoảng thời gian thực hiện các phép so pha. Độ lệch tần số được ước lượng như "
        "sau, với ∆t là lượng lệch pha và T là khoảng đo:"))
    b.append(eq("f_offset = − Δt / T", "19.1"))
    b.append(p("Nếu đo được +1 µs lệch pha trong khoảng đo 24 h, phương trình trở thành:"))
    b.append(eq("f_offset = − (1 µs) / (86.400 s) = −1,16 × 10⁻¹¹", "19.2"))
    b.append(p(
        "Độ lệch tần số càng nhỏ thì DUT càng gần tạo ra cùng tần số với tham chiếu. Một bộ dao động tích "
        "luỹ +1 µs lệch pha mỗi ngày có độ lệch tần số khoảng −1 × 10⁻¹¹ so với tham chiếu. Bảng 19.1 liệt "
        "kê các giá trị độ lệch gần đúng cho một số đơn vị lệch pha và khoảng đo tiêu chuẩn."))
    b.append(table(
        ["Khoảng đo", "Lệch pha", "Độ lệch tần số"],
        [["1 s", "±1 ms", "±1,00 × 10⁻³"],
         ["1 s", "±1 µs", "±1,00 × 10⁻⁶"],
         ["1 s", "±1 ns", "±1,00 × 10⁻⁹"],
         ["1 h", "±1 ms", "±2,78 × 10⁻⁷"],
         ["1 h", "±1 µs", "±2,78 × 10⁻¹⁰"],
         ["1 h", "±1 ns", "±2,78 × 10⁻¹³"],
         ["1 ngày", "±1 ms", "±1,16 × 10⁻⁸"],
         ["1 ngày", "±1 µs", "±1,16 × 10⁻¹¹"],
         ["1 ngày", "±1 ns", "±1,16 × 10⁻¹⁴"]],
        "Bảng 19.1 · Giá trị độ lệch tần số ứng với các lượng lệch pha cho trước."))
    b.append(p(
        "Các giá trị trong Bảng 19.1 có thể đổi sang đơn vị tần số (Hz) nếu biết tần số danh định. Ví dụ, "
        "xét bộ dao động có tần số danh định 5 MHz cao hơn tần số đúng 1,16 × 10⁻¹¹. Để tìm độ lệch tần số "
        "tính bằng hertz, nhân tần số danh định với giá trị không thứ nguyên:"))
    b.append(eq("(5 × 10⁶ Hz) × (1,16 × 10⁻¹¹) = 5,80 × 10⁻⁵ Hz", "19.3"))
    b.append(p("Tần số danh định là 5 MHz, tức 5.000.000 Hz. Do đó tần số thực do chuẩn tạo ra là:"))
    b.append(eq("5.000.000 Hz + 0,0000580 Hz = 5.000.000,0000580 Hz", "19.4"))
    b.append(p(
        "Để phân tích độ không đảm bảo đầy đủ, khoảng đo phải đủ dài để đảm bảo đang đo độ lệch tần số của "
        "DUT chứ không phải các nguồn khác đóng góp đáng kể. Nói cách khác, phải chắc rằng ∆t thực sự là "
        "thước đo lệch pha của DUT so với tham chiếu, không bị nhiễu từ tham chiếu hay hệ đo làm nhiễm. Đây "
        "là lý do TUR 10:1 là mong muốn; với TUR 10:1, nhiều hệ hiệu chuẩn tần số có thể đo độ lệch 1 × "
        "10⁻¹⁰ trong 1 s [4]."))
    b.append(p(
        "Dĩ nhiên TUR 10:1 không phải lúc nào cũng đạt được, và phương trình đơn giản cho độ lệch tần số "
        "(19.1) thường quá đơn giản. Khi dùng chuẩn chuyển tiếp như máy thu LORAN-C hay GPS, nhiễu đường "
        "vô tuyến đóng góp vào lệch pha. Vì vậy, thường dùng khoảng đo ít nhất 24 h khi hiệu chuẩn tần số "
        "bằng chuẩn chuyển tiếp. Khoảng này được chọn vì thay đổi trễ đường truyền giữa nguồn và máy thu "
        "thường biến thiên có chu kỳ và triệt tiêu khi lấy trung bình qua 24 h. Ngoài lấy trung bình, người "
        "ta còn dùng thuật toán khớp đường cong và các phương pháp thống kê khác để cải thiện ước lượng độ "
        "không đảm bảo và thể hiện mức tin cậy của phép đo [5]. Hình 19.1 cho hai đồ thị so pha đơn giản "
        "giữa DUT và tần số tham chiếu. Độ lệch tần số là hàm tuyến tính; đồ thị trên không thấy biến thiên "
        "về tính tuyến tính, cho thấy TUR 10:1 hoặc tốt hơn. Đồ thị dưới có biến thiên nhỏ, có thể nghĩa là "
        "TUR dưới 10:1 và một phần không đảm bảo do tham chiếu đóng góp."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Tóm lại, độ lệch tần số cho biết DUT tạo tần số danh định chính xác tới đâu. Lưu ý rằng thuật ngữ "
        "độ chính xác (hay độ chính xác tần số) thường xuất hiện trên bảng chỉ tiêu thay cho độ lệch tần số, "
        "vì hai thuật ngữ gần tương đương. Độ không đảm bảo tần số cho biết giới hạn (trên và dưới) của độ "
        "lệch tần số đo được. Thông thường dùng phép thử độ không đảm bảo 2σ, nghĩa là có 95,4% xác suất độ "
        "lệch tần số nằm trong giới hạn đã nêu trong khoảng đo. Hãy coi độ lệch tần số là kết quả của một "
        "phép đo tại một thời điểm, và độ không đảm bảo tần số là sự phân tán có thể có của các giá trị "
        "trong một khoảng đo."))
    b.append(h3("Độ ổn định", "Stability"))
    b.append(p(
        "Trước khi bàn về độ ổn định, cần phân biệt độ lệch tần số với độ ổn định. Độ lệch tần số đo mức "
        "một bộ dao động tạo đúng tần số danh định hay mức nó được chỉnh đúng; nó không cho biết chất lượng "
        "nội tại của bộ dao động. Ví dụ, một bộ dao động chất lượng cao nhưng cần chỉnh có thể tạo tần số "
        "lệch lớn; một bộ chất lượng thấp có thể được chỉnh tốt và (tạm thời) tạo tần số rất gần danh định. "
        "Ngược lại, độ ổn định cho biết một bộ dao động giữ được cùng một tần số tốt tới đâu trong một "
        "khoảng thời gian; nó không cho biết tần số “đúng” hay “sai”, chỉ cho biết tần số có giữ nguyên "
        "không. Một bộ dao động lệch tần số lớn vẫn có thể rất ổn định. Kể cả khi chỉnh bộ dao động tới gần "
        "tần số đúng hơn, độ ổn định thường không đổi. Hình 19.2 minh hoạ điều này bằng hai tín hiệu dao "
        "động có cùng tần số giữa t₁ và t₂, nhưng rõ ràng tín hiệu 1 không ổn định và dao động tần số giữa "
        "t₂ và t₃."))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Độ ổn định được định nghĩa là ước lượng thống kê các dao động tần số của một tín hiệu trong một "
        "khoảng thời gian. Độ ổn định ngắn hạn thường chỉ dao động trong khoảng dưới 100 s. Độ ổn định dài "
        "hạn có thể chỉ khoảng đo trên 100 s, nhưng thường chỉ những khoảng dài hơn 1 ngày. Một bảng chỉ "
        "tiêu điển hình có thể liệt kê ước lượng độ ổn định cho các khoảng 1, 10, 100 và 1000 s [6, 7]."))
    b.append(p(
        "Ước lượng độ ổn định có thể thực hiện trong miền tần số hoặc miền thời gian, nhưng miền thời gian "
        "được dùng rộng rãi hơn. Để ước lượng độ ổn định trong miền thời gian, phải bắt đầu từ một tập các "
        "phép đo độ lệch tần số yᵢ gồm các phép đo riêng lẻ y₁, y₂, y₃… Khi có tập dữ liệu này, cần xác định "
        "độ phân tán (dispersion) của yᵢ như thước đo nhiễu của bộ dao động. Độ phân tán của yᵢ càng lớn thì "
        "tín hiệu ra của bộ dao động càng kém ổn định. Thông thường dùng thống kê cổ điển như độ lệch chuẩn "
        "(hay phương sai, bình phương của độ lệch chuẩn) để đo độ phân tán. Phương sai đo độ trải số học "
        "của một tập dữ liệu quanh giá trị trung bình. Tuy nhiên, phương sai chỉ dùng được với dữ liệu dừng "
        "(stationary), nơi kết quả phải độc lập thời gian; điều này giả định nhiễu là trắng, tức công suất "
        "phân bố đều trên băng tần đo. Dữ liệu bộ dao động thường không dừng vì chứa nhiễu phụ thuộc thời "
        "gian do độ lệch tần số đóng góp. Với dữ liệu dừng, trung bình và phương sai sẽ hội tụ về giá trị "
        "nhất định khi số phép đo tăng. Với dữ liệu không dừng, trung bình và phương sai không bao giờ hội "
        "tụ; thay vào đó có một trung bình động thay đổi mỗi khi thêm phép đo mới."))
    b.append(p(
        "Vì những lý do này, người ta dùng một thống kê phi cổ điển để ước lượng độ ổn định trong miền thời "
        "gian, thường gọi là phương sai Allan (Allan variance); nhưng vì nó thực chất là căn bậc hai của "
        "phương sai, tên đúng của nó là độ lệch Allan (Allan deviation). Theo khuyến nghị của IEEE, độ lệch "
        "Allan được các nhà sản xuất chuẩn tần số dùng làm chỉ tiêu chuẩn cho độ ổn định. Phương trình của "
        "độ lệch Allan là:"))
    b.append(eq("σ_y(τ) = √( (1 / (2(M − 1))) · Σᵢ₌₁^{M−1} (yᵢ₊₁ − yᵢ)² )", "19.5"))
    b.append(p(
        "với M là số giá trị trong chuỗi yᵢ, và dữ liệu cách đều nhau theo các đoạn dài τ giây. Lưu ý rằng "
        "trong khi độ lệch cổ điển lấy mỗi phép đo trừ đi trung bình rồi mới bình phương và cộng lại, độ "
        "lệch Allan lại trừ đi điểm dữ liệu trước đó. Vì độ ổn định là thước đo dao động tần số chứ không "
        "phải độ lệch tần số, việc lấy hiệu các điểm dữ liệu liên tiếp nhằm loại bỏ nhiễu phụ thuộc thời "
        "gian do độ lệch tần số đóng góp. Cũng lưu ý rằng các giá trị y trong phương trình không chỉ trung "
        "bình của tập dữ liệu, mà ngụ ý rằng các phép đo riêng lẻ trong tập được lấy bằng cách lấy trung "
        "bình."))
    b.append(p(
        "Bảng 19.2 cho thấy cách ước lượng độ ổn định. Cột đầu là một chuỗi phép đo pha ghi ở khoảng 1 s. "
        "Mỗi phép đo lớn hơn phép trước, cho thấy DUT lệch tần số so với tham chiếu và độ lệch này gây ra "
        "lệch pha. Bằng cách lấy hiệu các phép đo pha thô, thu được các lệch pha ở cột hai. Cột ba chia "
        "lệch pha (∆t) cho khoảng đo 1 s để có độ lệch tần số. Vì lệch pha khoảng 4 ns/s, DUT có độ lệch "
        "tần số khoảng 4 × 10⁻⁹. Các giá trị ở cột ba tạo thành chuỗi dữ liệu yᵢ. Hai cột cuối là hiệu bậc "
        "nhất của yᵢ và bình phương của hiệu bậc nhất. Vì tổng các bình phương bằng 2,2 × 10⁻²¹, phương "
        "trình (với τ = 1 s) trở thành:"))
    b.append(table(
        ["Pha (ns)", "Lệch pha ∆t (ns)", "Độ lệch tần số ∆t/1 s (yᵢ)", "Hiệu bậc nhất (yᵢ₊₁ − yᵢ)", "Bình phương hiệu"],
        [["3321,44", "—", "—", "—", "—"],
         ["3325,51", "4,07", "4,07 × 10⁻⁹", "—", "—"],
         ["3329,55", "4,04", "4,04 × 10⁻⁹", "−3 × 10⁻¹¹", "9 × 10⁻²²"],
         ["3333,60", "4,05", "4,05 × 10⁻⁹", "+1 × 10⁻¹¹", "1 × 10⁻²²"],
         ["3337,65", "4,05", "4,06 × 10⁻⁹", "+2 × 10⁻¹¹", "4 × 10⁻²²"],
         ["3341,69", "4,04", "4,04 × 10⁻⁹", "−2 × 10⁻¹¹", "4 × 10⁻²²"],
         ["3345,74", "4,05", "4,05 × 10⁻⁹", "+1 × 10⁻¹¹", "1 × 10⁻²²"],
         ["3349,80", "4,06", "4,06 × 10⁻⁹", "+1 × 10⁻¹¹", "1 × 10⁻²²"],
         ["3353,85", "4,05", "4,05 × 10⁻⁹", "−1 × 10⁻¹¹", "1 × 10⁻²²"],
         ["3357,89", "4,04", "4,04 × 10⁻⁹", "−1 × 10⁻¹¹", "1 × 10⁻²²"]],
        "Bảng 19.2 · Dùng phép đo pha để ước lượng độ ổn định (dữ liệu ghi ở khoảng 1 s)."))
    b.append(eq("σ_y(1 s) = √( (2,2 × 10⁻²¹) / (2 × 9) ) = 1,17 × 10⁻¹¹", "19.6"))
    b.append(p(
        "Dùng cùng dữ liệu, có thể tính độ lệch Allan cho τ = 2 s bằng cách lấy trung bình các cặp giá trị "
        "kề nhau rồi dùng các trung bình mới làm giá trị dữ liệu. Với τ = 4 s, lấy trung bình mỗi nhóm bốn "
        "giá trị kề nhau. Cần thu thêm dữ liệu cho thời gian lấy trung bình dài hơn. Hãy nhớ rằng mức tin "
        "cậy của ước lượng độ ổn định cải thiện khi thời gian lấy trung bình tăng. Trong ví dụ trên, có tám "
        "mẫu cho ước lượng τ = 1 s, nhưng chỉ có hai mẫu cho ước lượng τ = 4 s. Mức tin cậy của ước lượng "
        "(1σ) có thể ước lượng gần đúng là:"))
    b.append(eq("độ tin cậy ≈ (1 / √M) × 100%", "19.7"))
    b.append(p(
        "Trong ví dụ với M = 9, biên sai số là 33%. Chỉ với hai mẫu, ước lượng có thể sai tới 70%. Với 10⁴ "
        "mẫu, biên sai số giảm còn 1%."))
    b.append(p(
        "Một đồ thị độ lệch Allan mẫu cho ở Hình 19.3, cho thấy độ ổn định cải thiện khi khoảng đo dài hơn. "
        "Một phần cải thiện là do nhiễu hệ đo ít đóng góp hơn khi khoảng đo dài hơn. Tuy nhiên, đến một lúc "
        "nào đó bộ dao động sẽ đạt sàn nhấp nháy (flicker floor), và về thực tế không thu thêm lợi ích bằng "
        "lấy trung bình. Sàn nhấp nháy là điểm mà các quá trình nhiễu trắng bắt đầu bị các quá trình không "
        "dừng như trôi tần số chi phối. Hầu hết bộ dao động thạch anh và rubidi đạt sàn nhấp nháy ở khoảng "
        "đo 10³ s hoặc ngắn hơn, nhưng bộ xêzi có thể chưa đạt sàn tới 10⁵ s (hơn 1 ngày). Hình 19.3 cho "
        "đồ thị độ lệch Allan mẫu của một bộ dao động thạch anh ổn định khoảng 5 × 10⁻¹² tại 100 s và đang "
        "tiến tới sàn nhấp nháy [8–10]."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Đừng nhầm độ ổn định với độ lệch tần số khi đọc bảng chỉ tiêu. Ví dụ, DUT có độ lệch tần số 1 × "
        "10⁻⁸ vẫn có thể đạt độ ổn định 1 × 10⁻¹² trong 1000 s; nghĩa là tần số ra của DUT ổn định dù không "
        "đặc biệt gần tần số danh định. Để làm rõ điểm này, Hình 19.4 là biểu diễn đồ hoạ quan hệ giữa độ "
        "lệch tần số (độ chính xác) và độ ổn định."))
    b.append(fig(4, F.fig(4)))

    # ---- 19.3
    b.append(h2("19.3 Chuẩn tần số", "Frequency Standards"))
    b.append(p(
        "Mọi chuẩn tần số đều có một thiết bị bên trong tạo ra biến cố tuần hoàn lặp lại, gọi là bộ cộng "
        "hưởng (resonator). Bộ cộng hưởng phải được nuôi bằng một nguồn năng lượng; gộp lại, nguồn năng "
        "lượng và bộ cộng hưởng tạo thành bộ dao động. Có hai loại bộ dao động chính dùng làm chuẩn tần số: "
        "bộ dao động thạch anh và bộ dao động nguyên tử."))
    b.append(h3("Bộ dao động thạch anh", "Quartz Oscillators"))
    b.append(p(
        "Bộ dao động tinh thể thạch anh xuất hiện trong thập niên 1920 và nhanh chóng thay thế thiết bị quả "
        "lắc làm chuẩn thời gian và tần số của phòng thí nghiệm [11]. Ngày nay, hơn 10⁹ bộ dao động thạch "
        "anh được chế tạo hằng năm cho các ứng dụng từ đồng hồ đeo tay, đồng hồ rẻ tiền đến mạng viễn thông "
        "và hệ theo dõi vũ trụ [12]. Tuy vậy, các phòng hiệu chuẩn và chuẩn thường chỉ hiệu chuẩn những loại "
        "thạch anh đắt hơn, như loại nằm trong thiết bị điện tử (như máy đếm tần số) hoặc loại thiết kế "
        "thành đơn vị độc lập. Giá một bộ dao động thạch anh chất lượng cao từ vài trăm đến vài nghìn USD."))
    b.append(p(
        "Tinh thể thạch anh trong bộ dao động có thể là thạch anh tự nhiên hoặc tổng hợp, nhưng mọi thiết bị "
        "hiện đại đều dùng vật liệu tổng hợp. Tinh thể đóng vai trò bộ cộng hưởng cơ học tạo điện áp dao "
        "động nhờ hiệu ứng áp điện: khi áp điện áp, tinh thể giãn ra hoặc co lại. Tinh thể có tần số cộng "
        "hưởng xác định bởi kích thước vật lý và loại tinh thể. Không có hai tinh thể nào hoàn toàn giống "
        "nhau hay tạo đúng cùng một tần số. Tần số ra của bộ dao động thạch anh là tần số cộng hưởng cơ bản "
        "hoặc bội của nó. Hình 19.5 là sơ đồ mạch đơn giản hoá các phần tử cơ bản của bộ dao động thạch "
        "anh; bộ khuếch đại cung cấp năng lượng cần để duy trì dao động."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Bộ dao động thạch anh nhạy với các tham số môi trường như nhiệt độ, độ ẩm, áp suất và rung động "
        "[12, 13]. Khi tham số môi trường thay đổi, tần số cộng hưởng cơ bản cũng thay đổi. Có vài kiểu "
        "thiết kế thạch anh nhằm giảm vấn đề môi trường. Bộ dao động tinh thể điều khiển bằng lò (OCXO) "
        "bao tinh thể trong một buồng điều nhiệt gọi là lò. Khi bật OCXO lần đầu, nó trải qua giai đoạn "
        "“khởi động” trong khi nhiệt độ tinh thể và lò ổn định; trong thời gian này hiệu năng thay đổi liên "
        "tục cho tới khi đạt nhiệt độ vận hành bình thường. Nhiệt độ trong lò sau đó giữ không đổi kể cả khi "
        "nhiệt độ bên ngoài thay đổi. Một giải pháp khác là bộ dao động tinh thể bù nhiệt (TCXO): tín hiệu "
        "ra từ cảm biến nhiệt đặc biệt (thermistor) tạo điện áp hiệu chỉnh đưa vào phần tử phản kháng biến "
        "thiên theo điện áp (varactor); varactor tạo thay đổi tần số bằng và ngược với thay đổi do nhiệt độ. "
        "Kỹ thuật này không tốt bằng điều khiển bằng lò nhưng rẻ hơn nhiều, nên TCXO thường dùng trong thiết "
        "bị nhỏ, thường là xách tay, khi không cần hiệu năng cao trên dải nhiệt rộng. Kiểu thứ ba là bộ dao "
        "động tinh thể bù bằng vi xử lý (MCXO): dùng vi xử lý và bù nhiệt bằng kỹ thuật số; MCXO nằm giữa "
        "TCXO và OCXO cả về giá lẫn hiệu năng."))
    b.append(p(
        "Mọi bộ dao động thạch anh đều bị lão hoá (aging), định nghĩa là “sự thay đổi tần số có hệ thống "
        "theo thời gian do những thay đổi bên trong bộ dao động”. Lão hoá thường quan sát được như một thay "
        "đổi gần tuyến tính của tần số cộng hưởng. Lão hoá có thể dương hoặc âm, và đôi khi thấy đảo chiều. "
        "Thường tần số cộng hưởng giảm, có thể cho thấy tinh thể đang to ra. Lão hoá có nhiều nguyên nhân: "
        "nhiễm bẩn tinh thể do lắng đọng vật liệu lạ, thay đổi mạch dao động, hoặc thay đổi vật liệu hay cấu "
        "trúc tinh thể. Chuyển động rung của tinh thể cũng góp phần gây lão hoá. Bộ dao động thạch anh chất "
        "lượng cao lão hoá với tốc độ 5 × 10⁻⁹ mỗi năm hoặc thấp hơn."))
    b.append(p(
        "Bất chấp vấn đề nhiệt độ và lão hoá, OCXO tốt nhất có thể đạt độ lệch tần số nhỏ tới 1 × 10⁻¹⁰. "
        "Các bộ rẻ hơn cho kết quả kém hơn. Bộ dao động nhỏ có lò (như loại dùng làm thời gốc trong máy đếm "
        "tần số) điển hình lệch tần số ±1 × 10⁻⁹ và chỉ tốn vài trăm USD. Loại thạch anh rẻ nhất (trong "
        "đồng hồ đeo tay và mạch điện tử) tốn dưới 1 USD; nhưng vì không có điều khiển nhiệt, chúng lệch "
        "tần số khoảng ±1 × 10⁻⁶ trong trường hợp tốt nhất và có thể lệch tới ±1 × 10⁻⁴. Vì độ lệch tần số "
        "của bộ dao động thạch anh thay đổi đáng kể theo thời gian dài, có thể cần chỉnh định kỳ để giữ tần "
        "số trong dung sai. Ví dụ, ngay cả thạch anh tốt nhất cũng cần chỉnh định kỳ để giữ tần số trong "
        "±1 × 10⁻¹⁰. Ngược lại, bộ dao động thạch anh có độ ổn định ngắn hạn tuyệt vời; một OCXO có thể ổn "
        "định tới 1 × 10⁻¹² tại 1 s. Giới hạn độ ổn định ngắn hạn chủ yếu do nhiễu từ linh kiện điện tử "
        "trong mạch dao động."))
    b.append(h3("Bộ dao động nguyên tử", "Atomic Oscillators"))
    b.append(p(
        "Bộ dao động nguyên tử dùng các mức năng lượng lượng tử hoá trong nguyên tử và phân tử làm nguồn "
        "tần số cộng hưởng. Các định luật cơ học lượng tử quy định năng lượng của một hệ liên kết chỉ nhận "
        "những giá trị rời rạc. Trường điện từ có thể nâng nguyên tử lên mức năng lượng cao hơn, hoặc nguyên "
        "tử ở mức cao có thể rơi xuống mức thấp bằng cách phát năng lượng điện từ. Tần số cộng hưởng (f) của "
        "bộ dao động nguyên tử là hiệu hai mức năng lượng chia cho hằng số Planck (h) [14]:"))
    b.append(eq("f = (E₂ − E₁) / h", "19.8"))
    b.append(p(
        "Mọi bộ dao động nguyên tử đều là chuẩn nội tại (intrinsic standard), vì tần số của chúng vốn dĩ "
        "bắt nguồn từ một hiện tượng tự nhiên cơ bản. Có ba loại chính: chuẩn rubidi, chuẩn xêzi và maser "
        "hydro. Cả ba đều chứa một bộ dao động thạch anh nội bộ được khoá theo tần số cộng hưởng do nguyên "
        "tử tương ứng tạo ra. Khoá bộ dao động thạch anh theo tần số nguyên tử có lợi: phần lớn yếu tố làm "
        "suy giảm hiệu năng dài hạn của thạch anh biến mất, vì tần số cộng hưởng nguyên tử ít nhạy với điều "
        "kiện môi trường hơn nhiều so với tần số cộng hưởng thạch anh. Kết quả là độ ổn định dài hạn và độ "
        "không đảm bảo của bộ dao động nguyên tử tốt hơn nhiều so với thạch anh, nhưng độ ổn định ngắn hạn "
        "không đổi."))
    b.append(h3("Bộ dao động rubidi", "Rubidium Oscillators"))
    b.append(p(
        "Bộ dao động rubidi là thành viên giá thấp nhất của nhóm nguyên tử, có lẽ cho tỉ lệ giá/hiệu năng "
        "tốt nhất trong mọi bộ dao động. Chúng hoạt động tốt hơn nhiều so với thạch anh và rẻ hơn nhiều so "
        "với xêzi."))
    b.append(p(
        "Bộ dao động rubidi hoạt động ở tần số cộng hưởng của nguyên tử rubidi (⁸⁷Rb), tức 6.834.682.608 "
        "Hz. Tần số này được tổng hợp từ một tần số thạch anh thấp hơn (thường 5 MHz), và tần số thạch anh "
        "được lái bởi cộng hưởng rubidi. Kết quả là nguồn tần số rất ổn định với độ ổn định ngắn hạn của "
        "thạch anh nhưng độ ổn định dài hạn tốt hơn nhiều. Vì ổn định hơn thạch anh, rubidi có thể giữ trong "
        "dung sai với ít lần chỉnh hơn. Giá ban đầu của bộ rubidi (điển hình 3.000 đến 8.000 USD) cao hơn "
        "thạch anh, nhưng vì ít cần chỉnh nên chi phí lao động giảm; do đó về lâu dài, sở hữu rubidi có thể "
        "rẻ hơn thạch anh."))
    b.append(p(
        "Độ lệch tần số của bộ rubidi sau khởi động từ 5 × 10⁻¹⁰ đến 5 × 10⁻¹². Duy trì tần số trong "
        "±1 × 10⁻¹¹ có thể làm thường ngày với rubidi nhưng không thực tế với cả thạch anh tốt nhất. Hiệu "
        "năng của một bộ rubidi được bảo dưỡng tốt có thể tiến gần hiệu năng của xêzi, mà rubidi nhỏ hơn, "
        "đáng tin cậy hơn và rẻ hơn nhiều."))
    b.append(h3("Bộ dao động xêzi", "Cesium Oscillators"))
    b.append(p(
        "Bộ dao động xêzi là chuẩn tần số sơ cấp vì giây SI dựa trên tần số cộng hưởng của nguyên tử xêzi "
        "(¹³³Cs), tức 9.192.631.770 Hz. Nghĩa là một bộ xêzi hoạt động đúng phải rất gần tần số danh định "
        "mà không cần chỉnh, và không có thay đổi tần số do lão hoá. Thang thời gian mà mọi nước lớn theo, "
        "Giờ Phối hợp Quốc tế (UTC), chủ yếu bắt nguồn từ việc lấy trung bình hiệu năng của một tập lớn bộ "
        "dao động xêzi."))
    b.append(p(
        "Bộ dao động xêzi là “con ngựa thồ” trong hầu hết hệ phân phối thời gian và tần số hiện đại. Chuẩn "
        "tần số sơ cấp của Hoa Kỳ là bộ xêzi NIST-7 với độ không đảm bảo tần số khoảng ±5 × 10⁻¹⁵. Bộ xêzi "
        "bán trên thị trường khác nhau về chất lượng, nhưng độ không đảm bảo tần số vẫn phải ±5 × 10⁻¹² "
        "hoặc thấp hơn."))
    b.append(p(
        "Hai nhược điểm lớn của bộ xêzi là độ tin cậy và giá thành. Độ tin cậy là vấn đề lớn: thành phần "
        "chính của bộ xêzi, gọi là ống chùm tia (beam tube), có tuổi thọ khoảng 3 đến 10 năm. Ống chùm tia "
        "cần để tạo tần số cộng hưởng của nguyên tử xêzi, rồi tần số này được dùng để điều khiển một bộ dao "
        "động thạch anh. Khi ống chùm tia hỏng, bộ xêzi hoạt động như một bộ thạch anh không được điều khiển. "
        "Vì vậy, bộ xêzi cần được giám sát liên tục để chắc rằng nó vẫn cung cấp tần số bắt nguồn từ xêzi. "
        "Giá cũng là vấn đề lớn: giá mua ban đầu từ 30.000 đến 80.000 USD và chi phí bảo trì cao; chi phí "
        "thay ống chùm tia chiếm một phần đáng kể giá toàn bộ bộ dao động. Phòng thí nghiệm dùng xêzi cần dự "
        "trù không chỉ giá mua ban đầu mà cả chi phí bảo trì sau đó."))
    b.append(h3("Maser hydro", "Hydrogen Masers"))
    b.append(p(
        "Maser hydro là chuẩn tần số thương mại tinh xảo và đắt nhất. Ít maser được chế tạo và hầu hết "
        "thuộc các đài thiên văn hay phòng chuẩn quốc gia. Từ “maser” là viết tắt của Microwave Amplification "
        "by Stimulated Emission of Radiation. Maser lấy tần số từ tần số cộng hưởng của nguyên tử hydro, tức "
        "1.420.405.752 Hz. Có hai loại maser hydro. Loại thứ nhất, maser chủ động (active), dao động tự phát "
        "và một bộ dao động thạch anh được khoá pha theo dao động chủ động này. Loại thứ hai, maser bị động "
        "(passive), khoá tần số một bộ thạch anh theo tham chiếu nguyên tử; kỹ thuật “bị động” cũng được "
        "rubidi và xêzi dùng. Vì maser chủ động lấy tần số ra trực tiếp hơn từ cộng hưởng nguyên tử, chúng "
        "có độ ổn định ngắn hạn tốt hơn maser bị động. Tuy vậy, cả hai loại maser đều có độ ổn định ngắn hạn "
        "tốt hơn xêzi. Dù vậy, độ không đảm bảo tần số của maser vẫn lớn hơn xêzi vì hoạt động của nó phụ "
        "thuộc tới hạn vào một tập điều kiện môi trường phức tạp. Dù hiệu năng tuyệt vời, giá maser hydro vẫn "
        "rất cao, điển hình 200.000 USD hoặc hơn [15, 16]."))
    b.append(p("Bảng 19.3 tóm tắt đặc tính của các loại bộ dao động khác nhau."))
    b.append(table(
        ["Loại", "Thạch anh (TCXO)", "Thạch anh (MCXO)", "Thạch anh (OCXO)", "Rubidi", "Xêzi", "Maser H"],
        [["Chuẩn sơ cấp", "Không", "Không", "Không", "Không", "Có", "Không"],
         ["Chuẩn nội tại", "Không", "Không", "Không", "Có", "Có", "Có"],
         ["Tần số cộng hưởng", "Cơ học (thay đổi)", "Cơ học (thay đổi)", "Cơ học (thay đổi)", "6,834682608 GHz", "9,19263177 GHz", "1,420405752 GHz"],
         ["Nguyên nhân hỏng chính", "Không", "Không", "Không", "Đèn rubidi (15 năm)", "Ống chùm xêzi (3–10 năm)", "Cạn hydro (7 năm +)"],
         ["Công suất (W)", "0,05", "0,04", "0,6", "20", "30", ">100"],
         ["Độ ổn định σ_y(τ), τ = 1 s", "1 × 10⁻⁹", "3 × 10⁻¹⁰", "1 × 10⁻¹²", "5 × 10⁻¹¹–5 × 10⁻¹²", "5 × 10⁻¹¹–5 × 10⁻¹²", "≈1 × 10⁻¹²"],
         ["Lão hoá/năm", "5 × 10⁻⁷", "3 × 10⁻⁸", "5 × 10⁻⁹", "2 × 10⁻¹⁰", "Không", "≈1 × 10⁻¹³"],
         ["Lệch tần sau khởi động", "1 × 10⁻⁶", "1 × 10⁻⁸", "1 × 10⁻⁸–1 × 10⁻¹⁰", "5 × 10⁻¹⁰–5 × 10⁻¹²", "5 × 10⁻¹²–1 × 10⁻¹⁴", "1 × 10⁻¹²–1 × 10⁻¹³"],
         ["Thời gian khởi động", "&lt;10 s–1 × 10⁻⁶", "&lt;10 s–1 × 10⁻⁸", "&lt;5 min–1 × 10⁻⁸", "&lt;5 min–5 × 10⁻¹⁰", "30 min–5 × 10⁻¹²", "24 h–1 × 10⁻¹²"],
         ["Giá", "100 USD", "1.000 USD", "2.000 USD", "3.000–8.000 USD", "30.000–80.000 USD", "200.000–300.000 USD"]],
        "Bảng 19.3 · Tóm tắt các loại bộ dao động."))

    # ---- 19.4
    b.append(h2("19.4 Chuẩn chuyển tiếp", "Transfer Standards"))
    b.append(p(
        "Tóm tắt lại: hiệu chuẩn tần số so sánh DUT với một tham chiếu. DUT thường là bộ dao động thạch "
        "anh, rubidi hoặc xêzi. Tham chiếu là một bộ dao động hiệu năng cao hơn DUT hoặc một chuẩn chuyển "
        "tiếp nhận tín hiệu vô tuyến. Mọi chuẩn chuyển tiếp đều nhận một tín hiệu có bộ xêzi ở nguồn, và tín "
        "hiệu này cung cấp cho người dùng tần số bắt nguồn từ xêzi. Điều này có lợi cho nhiều người dùng vì "
        "bộ xêzi đắt cả khi mua lẫn khi bảo trì, và không phải phòng hiệu chuẩn nào cũng đủ khả năng. Kể cả "
        "khi đã có bộ xêzi, phòng vẫn cần kiểm tra hiệu năng của nó; cách thực tế duy nhất là so xêzi với "
        "một chuẩn chuyển tiếp."))
    b.append(p(
        "Chuẩn chuyển tiếp cũng cung cấp truy xuất. Hầu hết chuẩn chuyển tiếp nhận tín hiệu truy xuất về "
        "chuẩn tần số quốc gia do NIST duy trì. Một số tín hiệu, như tín hiệu từ các đài HF WWV và WWVH và "
        "đài LF WWVB, có truy xuất vì được NIST điều khiển trực tiếp. Tín hiệu khác, như LORAN-C và GPS, có "
        "truy xuất vì tham chiếu của chúng được so sánh định kỳ với NIST. Một số tín hiệu phát từ ngoài Hoa "
        "Kỳ cũng được coi là có truy xuất, vì NIST so sánh chuẩn tần số của mình với chuẩn của nước khác."))
    b.append(p(
        "Khi dùng chuẩn chuyển tiếp phải chấp nhận một số thoả hiệp. Kể cả khi tín hiệu vô tuyến được tham "
        "chiếu tới một tần số gần hoàn hảo, hiệu năng của nó bị suy giảm khi truyền dọc đường giữa máy phát "
        "và máy thu. Ví dụ, xét một phòng thí nghiệm có chuẩn tần số gắn giá tạo tín hiệu 5 MHz. Nhà đo "
        "lường cần dùng tín hiệu này trên bàn làm việc nên chạy một đoạn cáp đồng trục từ chuẩn tới bàn. Tín "
        "hiệu bị trễ khi truyền từ chuẩn tới bàn, nhưng vì cáp có độ dài cố định nên trễ là hằng số. Trễ "
        "hằng số không làm thay đổi tần số: tần số vào một đầu cáp về cơ bản bằng tần số ra đầu kia. Nhưng "
        "nếu độ dài cáp liên tục thay đổi thì sao? Điều này thường làm tần số dao động. Qua thời gian dài, "
        "các dao động sẽ triệt tiêu khi lấy trung bình, nhưng độ ổn định tần số ngắn hạn vẫn rất kém. Đây "
        "chính là điều xảy ra khi dùng chuẩn chuyển tiếp: “cáp” thực chất là đường vô tuyến có thể dài hàng "
        "nghìn km, độ dài liên tục thay đổi và dường như tạo ra dao động tần số, dù nguồn tần số (một bộ "
        "xêzi) không đổi. Điều này khiến chuẩn chuyển tiếp không thích hợp làm tham chiếu khi đo độ ổn định "
        "ngắn hạn. Tuy nhiên, chuẩn chuyển tiếp rất thích hợp để đo độ không đảm bảo tần số, vì có thể giảm "
        "thiểu và thậm chí loại bỏ tác động của các dao động này nếu lấy trung bình đủ lâu; cuối cùng sẽ thu "
        "lại được hiệu năng của bộ xêzi."))
    b.append(p(
        "Một số tín hiệu vô tuyến có biến thiên đường truyền mạnh đến mức không thích hợp cho hiệu chuẩn tần "
        "số mức cao. Ví dụ, xét tín hiệu từ WWV ở Fort Collins, CO — một đài HF phát trên 2,5; 5; 10; 15 và "
        "20 MHz. WWV được tham chiếu tới chuẩn tần số quốc gia tại NIST, nhưng khi tới máy thu, phần lớn "
        "hiệu năng tiềm năng đã mất. Hầu hết người dùng sóng ngắn nhận sóng trời (phần tín hiệu đi lên tầng "
        "điện ly rồi phản xạ về Trái Đất). Vì độ cao tầng điện ly liên tục thay đổi, trễ đường truyền cũng "
        "liên tục thay đổi, thường tới 500–1000 µs. Vì đường biến thiên nhiều như vậy, lấy trung bình chỉ cải "
        "thiện hạn chế; do đó, dù WWV có truy xuất NIST, độ không đảm bảo tần số của nó chỉ đạt ±1 × 10⁻⁷ "
        "khi lấy trung bình 1 ngày."))
    b.append(p(
        "Tín hiệu vô tuyến khác có đường ổn định hơn và độ không đảm bảo thấp hơn nhiều. Các đài LF (như "
        "WWVB của NIST và LORAN-C) có thể cung cấp truy xuất NIST với độ không đảm bảo tần số ±1 × 10⁻¹² "
        "mỗi ngày. Đường LF ổn định hơn nhiều so với HF, nhưng vẫn có thay đổi trễ khi độ cao tầng điện ly "
        "thay đổi lúc mặt trời mọc và lặn. Hiện nay, tín hiệu được dùng rộng rãi nhất bắt nguồn từ các vệ "
        "tinh GPS, có ưu điểm là đường không bị vật cản giữa máy phát và máy thu; độ không đảm bảo tần số "
        "của GPS khoảng ±5 × 10⁻¹³/ngày. WWVB, LORAN-C và GPS được mô tả trong ba phần tiếp theo."))
    b.append(p(
        "Bảng 19.4 cho thấy một số chuẩn chuyển tiếp sẵn có và mức truy xuất NIST mà chúng cung cấp khi lấy "
        "trung bình với khoảng đo ít nhất 24 h [17]."))
    b.append(table(
        ["Chuẩn chuyển tiếp", "Độ không đảm bảo tần số qua 24 h (so với NIST)"],
        [["Máy thu HF (WWV và WWVH)", "±1 × 10⁻⁷"],
         ["Máy thu LF (LORAN-C và WWVB)", "±1 × 10⁻¹²"],
         ["Máy thu GPS", "±5 × 10⁻¹³"]],
        "Bảng 19.4 · Mức truy xuất do các chuẩn chuyển tiếp khác nhau cung cấp."))
    b.append(h3("WWVB", "WWVB"))
    b.append(p(
        "Nhiều nước phát tín hiệu thời gian và tần số trong băng LF 30 kHz–300 kHz, cũng như băng VLF 3 "
        "kHz–30 kHz. Vì một phần tín hiệu LF là sóng đất đi theo độ cong Trái Đất, độ ổn định đường của "
        "những tín hiệu này chấp nhận được cho nhiều ứng dụng. Một đài như vậy là WWVB do NIST vận hành. "
        "WWVB phát trên 60 kHz từ cùng địa điểm với WWV ở Fort Collins, CO. Tín hiệu hiện phủ phần lớn Bắc "
        "Mỹ, và việc tăng công suất (6 dB, dự kiến 1998) sẽ mở rộng vùng phủ và cải thiện tỉ số tín hiệu/tạp "
        "trong nước Mỹ."))
    b.append(p(
        "Dù ổn định hơn nhiều so với đường HF, độ dài đường WWVB chịu ảnh hưởng của điều kiện môi trường dọc "
        "đường và biến thiên ngày đêm, theo mùa. Độ dài đường quan trọng vì một phần tín hiệu đi dọc mặt đất "
        "(sóng đất), phần khác phản xạ từ tầng điện ly (sóng trời). Đường sóng đất ổn định hơn nhiều so với "
        "sóng trời. Nếu đường tương đối ngắn (dưới 1000 km), máy thu có thể bám liên tục sóng đất vì nó luôn "
        "đến trước. Với đường dài hơn, nhận được hỗn hợp sóng đất và sóng trời; trên đường rất dài, sóng đất "
        "có thể yếu đến mức chỉ nhận được sóng trời, khi đó đường kém ổn định hơn nhiều."))
    b.append(p(
        "Đặc tính đường LF khác nhau ở các thời điểm trong ngày. Ban ngày và ban đêm, máy thu có thể phân "
        "biệt sóng đất và sóng trời, độ ổn định đường có thể chỉ biến thiên vài trăm nano giây. Tuy nhiên, "
        "nếu đang nhận một phần sóng trời, sẽ có dịch pha ngày đêm lúc mặt trời mọc và lặn. Ví dụ, khi đường "
        "chuyển từ tối hoàn toàn sang sáng hoàn toàn, tầng điện ly hạ xuống và đường ngắn lại; độ dài đường "
        "sau đó ổn định cho tới khi máy phát hoặc máy thu vào bóng tối, lúc đó tầng điện ly nâng lên và đường "
        "dài ra. Máy thu WWVB có vài ưu điểm khi dùng làm chuẩn chuyển tiếp: giá thấp, dễ dùng, và tín hiệu "
        "nhận được truy xuất trực tiếp NIST. Với máy thu và ăng-ten tốt, có thể đạt độ không đảm bảo tần số "
        "±1 × 10⁻¹² khi lấy trung bình 1 ngày [18]."))
    b.append(h3("LORAN-C", "LORAN-C"))
    b.append(p(
        "LORAN-C là hệ dẫn đường vô tuyến hoạt động trong băng LF. Phần lớn hệ thống do Bộ Giao thông Hoa Kỳ "
        "(DOT) vận hành, nhưng một số trạm do chính phủ khác vận hành. Hệ gồm các nhóm trạm gọi là chuỗi; mỗi "
        "chuỗi có một trạm chủ và từ hai đến năm trạm phụ. Các trạm công suất cao, điển hình 275–800 kW, "
        "phát trên sóng mang 100 kHz dùng băng 90–110 kHz."))
    b.append(p(
        "Vì mọi chuỗi LORAN-C dùng cùng tần số sóng mang, các chuỗi phát xung để có thể nhận diện từng trạm. "
        "Mỗi chuỗi phát một nhóm xung gồm xung từ mọi trạm riêng lẻ, ở một Khoảng Lặp Nhóm (GRI) riêng. Ví "
        "dụ, chuỗi 7980 phát xung mỗi 79,8 ms. Khi rời máy phát, xung bức xạ theo mọi hướng: sóng đất đi "
        "song song mặt đất, sóng trời đi lên và phản xạ từ tầng điện ly. Hình dạng xung được thiết kế để máy "
        "thu phân biệt sóng đất và sóng trời và khoá vào sóng đất ổn định hơn. Hầu hết máy thu bám sóng đất "
        "bằng cách theo dõi chu kỳ thứ ba của xung — chu kỳ này đến sớm trong xung (nên biết là sóng đất) và "
        "có biên độ lớn hơn chu kỳ thứ nhất và thứ hai (nên dễ giữ khoá). Nhìn chung, máy thu trong vòng "
        "1500 km từ máy phát có thể bám cùng chu kỳ sóng đất vô hạn và tránh nhận sóng trời. Biến thiên trễ "
        "đường sóng đất thường khá nhỏ (dưới 500 ns/ngày). Tuy nhiên, nếu độ dài đường vượt 1500 km, máy thu "
        "có thể mất khoá và nhảy sang chu kỳ khác của sóng mang; mỗi lần nhảy gây bước pha 10 µs, bằng chu "
        "kỳ của 100 kHz."))
    b.append(p(
        "Máy thu LORAN-C thương mại thiết kế làm chuẩn chuyển tiếp có giá khoảng 3.000–10.000 USD, thường "
        "cung cấp vài đầu ra tần số khác nhau (thường 10 MHz, 1 Hz và xung GRI). Máy thu dẫn đường LORAN-C "
        "được sản xuất hàng loạt và rẻ nhưng không cung cấp đầu ra tần số; tuy vậy, đôi khi có thể tìm và "
        "khuếch đại xung GRI trên bo mạch để dùng làm tần số tham chiếu."))
    b.append(h3("Hiệu năng LORAN-C", "LORAN-C Performance"))
    b.append(p(
        "Độ không đảm bảo tần số của LORAN-C bị suy giảm do biến thiên đường vô tuyến. Độ lớn biến thiên phụ "
        "thuộc cường độ tín hiệu, khoảng cách máy thu–máy phát, thời tiết và điều kiện khí quyển, và chất "
        "lượng máy thu cùng ăng-ten. Hình 19.6 cho thấy kiểu biến thiên đường thường gặp: một phép so pha "
        "100 s giữa chuỗi LORAN-C 8970 thu tại Boulder, CO và chuẩn tần số quốc gia NIST. Tín hiệu 8970 phát "
        "từ trạm chủ ở Dana, IN, cách Boulder khoảng 1512 km. Độ lệch tần số giữa chuẩn NIST và chuẩn xêzi ở "
        "máy phát LORAN-C sẽ tạo dịch pha dưới 1 ns mỗi 100 s; do đó đồ thị chỉ thể hiện nhiễu đường LORAN-C, "
        "tức hiệu thời điểm đến của xung GRI do biến thiên đường. Biên độ nhiễu đường này khoảng 200 ns."))
    b.append(fig(6, F.fig(6)))
    b.append(p(
        "Biến thiên đường khiến độ ổn định ngắn hạn của LORAN-C kém. Tuy nhiên, vì biến thiên đường triệt "
        "tiêu theo thời gian, độ ổn định dài hạn tốt hơn nhiều. Nghĩa là có thể dùng LORAN-C để hiệu chuẩn "
        "gần như mọi chuẩn tần số nếu lấy trung bình đủ lâu. Chuẩn tần số càng tốt thì càng mất lâu để đạt "
        "TUR gần 10:1. Ví dụ, bộ thạch anh có độ không đảm bảo 1 × 10⁻⁷ có thể hiệu chuẩn trong 100 s: nó "
        "tích luỹ 10 µs dịch pha trong 100 s, che khuất hoàn toàn nhiễu đường ở Hình 19.6. Nhưng bộ rubidi "
        "có độ không đảm bảo 1 × 10⁻¹¹ chỉ tích luỹ 1 ns dịch pha trong 100 s, tức khoảng 1 µs mỗi ngày. Vì "
        "vậy, khuyến nghị khoảng đo ít nhất 24 h khi dùng LORAN-C hiệu chuẩn bộ dao động nguyên tử. Hình "
        "19.7 cho kết quả hiệu chuẩn 96 h một bộ xêzi bằng LORAN-C; đường đậm là ước lượng bình phương nhỏ "
        "nhất của độ lệch tần số. Dù nhiễu đường hiện rõ, độ dốc của đường cho thấy bộ xêzi thấp tần số "
        "khoảng 3,4 × 10⁻¹²."))
    b.append(fig(7, F.fig(7)))
    b.append(h3("Hệ Định vị Toàn cầu (GPS)", "Global Positioning System (GPS)"))
    b.append(p(
        "GPS là hệ dẫn đường vô tuyến do Bộ Quốc phòng Hoa Kỳ (DOD) phát triển và vận hành, gồm một chòm 24 "
        "vệ tinh bay quanh Trái Đất (21 chính và 3 dự phòng). Mỗi vệ tinh mang bốn chuẩn tần số nguyên tử "
        "(hai rubidi và hai xêzi) được tham chiếu tới Đài Thiên văn Hải quân Hoa Kỳ (USNO) và truy xuất "
        "NIST. 24 vệ tinh bay trên sáu mặt phẳng cố định nghiêng 55° so với xích đạo, mỗi vệ tinh ở độ cao "
        "20.200 km với chu kỳ 11 h 58 min, nghĩa là một vệ tinh đi qua cùng một nơi sớm hơn 4 min mỗi ngày. "
        "Vì các vệ tinh liên tục bay quanh Trái Đất, GPS phải dùng được ở bất cứ đâu trên bề mặt."))
    b.append(p(
        "Mỗi vệ tinh GPS phát trên hai sóng mang L1 (1575,42 MHz) và L2 (1227,6 MHz), phát dạng sóng trải "
        "phổ gọi là mã tạp giả ngẫu nhiên (PRN). Có hai loại mã PRN: mã thu thập thô (C/A) với tốc độ chip "
        "1023 chip/ms, và mã chính xác (P) với tốc độ 10230 chip/ms. Mã C/A lặp mỗi mili giây; mã P chỉ lặp "
        "mỗi 267 ngày nhưng vì lý do thực tế được đặt lại mỗi tuần. Mã C/A phát trên L1, mã P phát trên cả "
        "L1 và L2 [19, 20]."))
    b.append(p(
        "Vì an ninh quốc gia, DOD khởi động chương trình Giảm độ chính xác có chọn lọc (SA) năm 1990, cố ý "
        "tăng độ không đảm bảo định vị và thời gian của GPS bằng cách thêm khoảng 300 ns nhiễu vào cả mã C/A "
        "và P. Tín hiệu thu được phân phối qua Dịch vụ Định vị Tiêu chuẩn (SPS), dành cho dùng toàn cầu và "
        "miễn phí cho ai có máy thu GPS. Dịch vụ Định vị Chính xác (PPS) chỉ dành cho người dùng được quân "
        "đội Hoa Kỳ cấp phép, cần máy thu đặc biệt dùng logic mật mã để loại bỏ SA. Vì PPS bị hạn chế, gần "
        "như mọi người dùng GPS dân sự đều dùng SPS."))
    b.append(h3("Thiết bị thu GPS", "GPS Receiving Equipment"))
    b.append(p(
        "Vào thời điểm viết (1996), máy thu GPS đã phổ biến trên thị trường điện tử tiêu dùng, một số mẫu có "
        "giá 200 USD hoặc thấp hơn. Tuy nhiên, máy thu phù hợp làm chuẩn chuyển tiếp hiếm hơn nhiều và đắt "
        "hơn. Giá máy thu từ dưới 100 USD cho bo mạch thời gian OEM đến 20.000 USD hoặc hơn cho mẫu tinh vi "
        "nhất, thường phụ thuộc chất lượng bộ dao động thời gốc. Mẫu giá thấp có thời gốc chất lượng thấp, "
        "phải liên tục lái theo tín hiệu GPS; mẫu giá cao có thời gốc tốt hơn (một số có rubidi bên trong) "
        "và có thể bỏ qua nhiều biến thiên đường GPS vì bộ dao động cho phép chúng trôi trong khoảng lâu hơn "
        "[21]."))
    b.append(p(
        "Hầu hết máy thu GPS cung cấp đầu ra 1 xung mỗi giây (1 pps). Một số còn cung cấp đầu ra 1 kHz (bắt "
        "nguồn từ mã C/A) và ít nhất một đầu ra tần số chuẩn (1, 5 hoặc 10 MHz). Để dùng, chỉ cần lắp ăng-ten, "
        "nối với máy thu và bật máy. Ăng-ten thường là hình nón hay đĩa nhỏ (đường kính khoảng 15 cm) lắp "
        "ngoài trời nơi có tầm nhìn bầu trời rõ ràng. Khi bật, máy thu tìm kiếm bầu trời để biết vệ tinh nào "
        "đang trên đường chân trời và nhìn thấy từ vị trí ăng-ten, rồi tính toạ độ ba chiều (miễn có bốn vệ "
        "tinh trong tầm nhìn) và bắt đầu tạo tín hiệu tần số. Máy thu đơn giản nhất chỉ có một kênh và quan "
        "sát nhiều vệ tinh bằng sơ đồ tuần tự chuyển nhanh; mẫu tinh vi hơn bám song song và gán một kênh "
        "riêng cho mỗi vệ tinh. Những máy thu này thường bám 5–12 vệ tinh cùng lúc (hơn 8 chỉ có trong "
        "trường hợp hiếm). Bằng cách lấy trung bình dữ liệu từ nhiều vệ tinh, máy thu có thể loại bỏ một "
        "phần tác động của SA và giảm độ không đảm bảo tần số."))
    b.append(h3("Hiệu năng GPS", "GPS Performance"))
    b.append(p(
        "GPS có nhiều ưu điểm kỹ thuật so với LORAN-C: tín hiệu thường dễ thu hơn, thiết bị thường rẻ hơn, "
        "và vùng phủ lớn hơn nhiều. Ngoài ra, hiệu năng của GPS vượt LORAN-C. Tuy vậy, như mọi chuẩn chuyển "
        "tiếp, độ ổn định ngắn hạn của máy thu GPS kém (tệ hơn do SA) và làm kéo dài thời gian hiệu chuẩn. "
        "Như với LORAN-C, khuyến nghị khoảng đo ít nhất 24 h khi hiệu chuẩn chuẩn tần số nguyên tử bằng GPS."))
    b.append(p(
        "Để minh hoạ, Hình 19.8 cho một phép so sánh 100 s giữa GPS và một bộ xêzi. Bộ xêzi có độ lệch tần "
        "số khoảng 1 × 10⁻¹³, nên dịch pha tích luỹ trong 100 s dưới 1 ns; do đó nhiễu trên đồ thị là do "
        "biến thiên đường GPS và SA. Hình 19.9 cho phép so sánh 1 tuần giữa một máy thu GPS và cùng bộ xêzi "
        "đó. Biên độ dữ liệu là 550 ns; đường đậm là ước lượng bình phương nhỏ nhất của độ lệch tần số. Dù "
        "nhiễu đường GPS vẫn hiện rõ, có thể thấy xu hướng tuyến tính do độ lệch tần số của xêzi, tức bộ "
        "xêzi thấp tần số khoảng 5 × 10⁻¹³."))
    b.append(fig(8, F.fig(8)))
    b.append(fig(9, F.fig(9)))

    # ---- 19.5
    b.append(h2("19.5 Các phương pháp hiệu chuẩn", "Calibration Methods"))
    b.append(p(
        "Tóm tắt lại: chuẩn tần số thường được hiệu chuẩn bằng cách so với một tần số tham chiếu truy xuất. "
        "Phần này bàn cách thực hiện phép so sánh đó. Trước hết, hãy xem tín hiệu điện do chuẩn tần số tạo "
        "ra. Tín hiệu này có thể có vài dạng, như ở Hình 19.10. Đường đứt nét biểu thị điện áp nguồn (5–15 V "
        "với CMOS), đường đậm liền biểu thị điện áp ra."))
    b.append(fig(10, F.fig(10)))
    b.append(p(
        "Nếu tần số ra là sóng sin dao động, nó có thể trông như Hình 19.11. Tín hiệu này tạo một chu kỳ "
        "(2π radian pha) trong một chu kỳ. Hệ hiệu chuẩn tần số so một tín hiệu như ở Hình 19.11 với một tín "
        "hiệu tham chiếu chất lượng cao hơn, rồi đo và ghi lại thay đổi pha giữa hai tín hiệu. Nếu hai tần "
        "số hoàn toàn bằng nhau, quan hệ pha của chúng sẽ không đổi. Vì hai tần số không hoàn toàn bằng nhau, "
        "quan hệ pha sẽ thay đổi; bằng cách đo tốc độ thay đổi, có thể xác định độ lệch tần số của DUT. "
        "Trong điều kiện bình thường, pha thay đổi có trật tự và dự đoán được. Tuy nhiên, các yếu tố bên "
        "ngoài như mất điện, hỏng linh kiện hoặc sai sót con người có thể gây thay đổi pha đột ngột, gọi là "
        "bước pha. Hệ hiệu chuẩn đo tổng lượng dịch pha (do độ lệch tần số của DUT hoặc do bước pha) trong "
        "một khoảng đo cho trước."))
    b.append(fig(11, F.fig(11)))
    b.append(p(
        "Hình 19.12 cho một phép so pha giữa hai tần số sin. Sóng trên là tín hiệu từ DUT, sóng dưới là tín "
        "hiệu từ tham chiếu. Các đường thẳng đứng được vẽ qua điểm mà mỗi sóng qua zero. Phần dưới của hình "
        "cho các “cột” chỉ độ lớn hiệu pha giữa hai tín hiệu. Nếu quan hệ pha đang thay đổi, hiệu pha sẽ "
        "tăng hoặc giảm, cho thấy DUT lệch tần số (cao hoặc thấp) so với tham chiếu. Phương trình 19.1 ước "
        "lượng độ lệch tần số. Ở Hình 19.12, cả ∆t và T tăng cùng tốc độ và các cột hiệu pha rộng dần, cho "
        "thấy DUT có độ lệch tần số không đổi."))
    b.append(fig(12, F.fig(12)))
    b.append(p(
        "Có vài loại hệ hiệu chuẩn dùng để so pha. Loại đơn giản nhất là đếm và hiển thị trực tiếp tần số ra "
        "của DUT bằng một thiết bị gọi là máy đếm tần số. Phương pháp này có nhiều ứng dụng nhưng không thích "
        "hợp để đo thiết bị hiệu năng cao: DUT được so với thời gốc của máy đếm (thường là TCXO), và độ không "
        "đảm bảo của hệ bị giới hạn bởi hiệu năng thời gốc, thường khoảng 1 × 10⁻⁸. Một số máy đếm cho phép "
        "dùng thời gốc ngoài để cải thiện kết quả. Hạn chế lớn nhất là máy đếm hiển thị tần số bằng hertz và "
        "có độ phân giải hữu hạn; phát hiện thay đổi nhỏ về tần số có thể mất nhiều ngày hoặc nhiều tuần, "
        "khiến khó hoặc không thể dùng phương pháp này để chỉnh bộ dao động chính xác hay đo độ ổn định "
        "[22]. Vì vậy, hầu hết hệ hiệu chuẩn hiệu năng cao thu dữ liệu chuỗi thời gian để ước lượng cả độ "
        "không đảm bảo tần số lẫn độ ổn định. Sau đây bàn cách so pha bằng hai phương pháp khác nhau: phương "
        "pháp khoảng thời gian và phương pháp hiệu thời gian trộn kép [9, 10]."))
    b.append(p(
        "Phương pháp khoảng thời gian dùng một thiết bị gọi là bộ đếm khoảng thời gian (TIC) để đo khoảng "
        "thời gian giữa hai tín hiệu. TIC có đầu vào cho hai tín hiệu điện: một tín hiệu khởi động bộ đếm, "
        "tín hiệu kia dừng nó. Nếu hai tín hiệu cùng tần số, khoảng thời gian sẽ không đổi; nếu khác tần số, "
        "khoảng thời gian sẽ thay đổi, tuy thường rất chậm. Bằng cách xem tốc độ thay đổi, có thể hiệu chuẩn "
        "thiết bị — hệt như có hai đồng hồ: đọc mỗi ngày sẽ biết một đồng hồ nhanh hay chậm bao nhiêu so với "
        "đồng kia. Cần hai phép đo khoảng thời gian mới cho thông tin hữu ích; lấy phép đo thứ hai trừ phép "
        "đầu, có thể biết đã được hay mất thời gian."))
    b.append(p(
        "Các TIC khác nhau về chỉ tiêu và chi tiết thiết kế, nhưng đều có vài phần cơ bản: thời gốc "
        "(timebase), cổng chính (main gate) và cụm đếm. Thời gốc cung cấp các xung cách đều dùng để đo khoảng "
        "thời gian; nó thường là bộ dao động thạch anh nội bộ có thể khoá pha theo tham chiếu ngoài, và phải "
        "ổn định vì sai số thời gốc ảnh hưởng trực tiếp tới phép đo. Cổng chính điều khiển thời điểm bắt đầu "
        "và kết thúc đếm. Các xung qua cổng được đưa tới cụm đếm, hiển thị trên mặt trước TIC hoặc đọc bằng "
        "máy tính; sau đó bộ đếm có thể được đặt lại (hoặc arm) để bắt đầu phép đo mới. Đầu vào dừng và khởi "
        "động thường có điều khiển mức đặt giới hạn biên độ (mức trigger) mà tại đó bộ đếm đáp ứng tín hiệu "
        "vào; nếu đặt mức trigger không đúng, TIC có thể dừng hoặc khởi động khi phát hiện nhiễu hay tín "
        "hiệu không mong muốn và cho kết quả không hợp lệ."))
    b.append(p(
        "Hình 19.13 minh hoạ cách TIC đo khoảng giữa hai tín hiệu. Đầu vào A là xung khởi động, đầu vào B là "
        "xung dừng. TIC bắt đầu đo khi tín hiệu khởi động đạt mức trigger và dừng khi tín hiệu dừng đạt mức "
        "trigger; khoảng thời gian được đo bằng cách đếm chu kỳ từ thời gốc. Các phép đo do TIC tạo ra có đơn "
        "vị thời gian: mili giây, micro giây, nano giây… Những phép đo này gán một giá trị cho hiệu pha giữa "
        "tham chiếu và DUT."))
    b.append(fig(13, F.fig(13)))
    b.append(p(
        "Chỉ tiêu quan trọng nhất của TIC là độ phân giải, tức mức độ xác định được một phép đo. Ví dụ, TIC "
        "có độ phân giải 10 ns có thể cho số đọc 3340 ns hoặc 3350 ns, nhưng không cho 3345 ns; muốn đo mịn "
        "hơn cần độ phân giải cao hơn. Trong thiết kế TIC đơn giản, độ phân giải bị giới hạn bởi chu kỳ của "
        "tần số thời gốc; ví dụ TIC có thời gốc 10 MHz bị giới hạn ở 100 ns nếu không phân giải được khoảng "
        "nhỏ hơn một chu kỳ. Để cải thiện, một số nhà thiết kế nhân tần số thời gốc để có nhiều chu kỳ hơn "
        "và do đó độ phân giải cao hơn: nhân lên 100 MHz cho độ phân giải 10 ns, và đã có máy đếm 1 ns dùng "
        "thời gốc 1 GHz. Tuy nhiên, cách phổ biến hơn để tăng độ phân giải là phát hiện phần lẻ của chu kỳ "
        "thời gốc bằng nội suy (interpolation), không bị giới hạn bởi số chu kỳ nguyên; nội suy đã khiến TIC "
        "1 ns trở nên phổ biến, và TIC 10 ps đã có [23]."))
    b.append(p(
        "Một hệ đo khoảng thời gian cho ở Hình 19.14. Hệ này dùng TIC để đo và ghi hiệu giữa hai tín hiệu. "
        "Phải dùng tín hiệu khởi động và dừng tần số thấp (thường 1 Hz). Vì bộ dao động thường tạo tần số "
        "như 1, 5, 10 MHz, giải pháp là dùng bộ chia tần để đưa về tần số thấp hơn. Bộ chia tần có thể là "
        "thiết bị độc lập, mạch nhỏ hoặc chỉ một chip. Hầu hết chip chia tần chia theo bội số của 10, nên "
        "thường gặp mạch chia cho nghìn, triệu… Ví dụ, chia tín hiệu 1 MHz cho 10⁶ được 1 Hz. Dùng tín hiệu "
        "tần số thấp giảm vấn đề tràn trên/dưới của bộ đếm và giúp tránh sai số khi tín hiệu khởi động và "
        "dừng quá gần nhau (TIC có thể sai khi đo khoảng dưới 100 ns)."))
    b.append(fig(14, F.fig(14)))
    b.append(p(
        "Phương pháp khoảng thời gian có lẽ là phương pháp phổ biến nhất hiện nay, với nhiều ưu điểm: giá "
        "thấp, thiết kế đơn giản, hiệu năng tuyệt vời khi đo độ không đảm bảo hay độ ổn định tần số dài hạn. "
        "Tuy nhiên, có hai vấn đề hạn chế hiệu năng khi đo độ ổn định ngắn hạn. Thứ nhất, sau khi TIC hoàn "
        "tất một phép đo, dữ liệu phải được xử lý trước khi bộ đếm đặt lại và chuẩn bị cho phép đo tiếp; "
        "trong khoảng trễ này (dead time), một phần thông tin bị mất. Dead time ít thành vấn đề hơn với TIC "
        "hiện đại nhờ phần cứng và phần mềm nhanh hơn rút ngắn thời gian xử lý. Vấn đề đáng kể hơn khi đo "
        "độ ổn định ngắn hạn là các bộ chia tần thông dụng nhạy với thay đổi nhiệt độ và thường không ổn định "
        "tới ±1 ns; dùng bộ chia ổn định hơn làm tăng giá hệ thống [10, 22]."))
    b.append(p(
        "Một hệ phức tạp hơn, phù hợp hơn để đo độ ổn định ngắn hạn, dùng phương pháp Hiệu Thời gian Trộn "
        "Kép (Dual Mixer Time Difference — DMTD), ở Hình 19.15. Phương pháp này dùng một bộ tổng hợp tần số "
        "và hai bộ trộn song song. Bộ tổng hợp được khoá theo bộ dao động tham chiếu và tạo tần số thấp hơn "
        "tần số ra của DUT. Tần số tổng hợp sau đó được trộn (heterodyne) với cả tần số tham chiếu lẫn đầu "
        "ra của DUT để tạo hai tần số phách. Hai tần số phách lệch pha một lượng tỉ lệ với chênh lệch thời "
        "gian giữa DUT và tham chiếu. Một bộ dò điểm không xác định điểm qua zero của mỗi chu kỳ phách. Một "
        "bộ đếm sự kiện (hay scaler) tích luỹ hiệu pha thô giữa các bộ dao động bằng cách đếm số chu kỳ "
        "nguyên; một TIC cung cấp độ phân giải mịn cần để đếm phần lẻ chu kỳ. Hệ thu được phù hợp hơn nhiều "
        "để đo độ ổn định ngắn hạn so với hệ đo khoảng thời gian: tổ hợp bộ dao động, bộ tổng hợp và bộ trộn "
        "thực hiện cùng chức năng như bộ chia nhưng nhiễu giảm, thường xuống ±5 ps hoặc thấp hơn."))
    b.append(fig(15, F.fig(15)))
    b.append(p(
        "Các biến thể khác của những phương pháp hiệu chuẩn này cũng được dùng và có thể hợp lệ như nhau cho "
        "một ứng dụng cụ thể [9, 10, 21, 22]. Hãy nhớ rằng một phương pháp hiệu chuẩn được định nghĩa và ghi "
        "chép tốt là bắt buộc với phòng thí nghiệm muốn đăng ký ISO hoặc tuân thủ một chương trình công nhận "
        "phòng thí nghiệm."))

    # ---- 19.6
    b.append(h2("19.6 Những phát triển tương lai", "Future Developments"))
    b.append(p(
        "Trong những năm tới, hiệu năng của chuẩn tần số sẽ tiếp tục cải thiện. Một hướng hứa hẹn là chuẩn "
        "đài phun xêzi (cesium-fountain), hoạt động bằng cách làm lạnh nguyên tử xêzi bằng laser rồi ném "
        "chúng thẳng đứng qua một hốc vi ba; tần số cộng hưởng được phát hiện khi nguyên tử đi lên và rơi "
        "xuống dưới tác dụng trọng lực. Nhiều phòng thí nghiệm đang nghiên cứu ý tưởng này, hứa hẹn giảm độ "
        "không đảm bảo tần số so với chuẩn chùm tia xêzi hiện có [24]. Về lâu dài, một chuẩn ion bị bẫy có "
        "thể đem lại cải thiện vài bậc độ lớn; chuẩn này lấy tần số cộng hưởng từ các dịch chuyển năng lượng "
        "có hệ thống trong một số ion được giữ bất động trong bẫy điện từ, với độ không đảm bảo tần số có "
        "thể nhỏ tới ±1 × 10⁻¹⁸ [25]. Ngoài ra, các công cụ thống kê mới có thể cải thiện khả năng ước lượng "
        "độ ổn định của bộ dao động, đặc biệt ở dài hạn [26]."))
    b.append(p(
        "Tương lai của chuẩn chuyển tiếp sẽ ngày càng dựa nhiều vào máy thu vệ tinh, và hiệu năng của chúng "
        "sẽ tiếp tục cải thiện. Các hệ đặt trên mặt đất như LORAN-C dự kiến sẽ bị loại bỏ dần [27]. Độ không "
        "đảm bảo tần số của máy thu GPS sẽ cải thiện khi chương trình SA được ngừng vào đầu thế kỷ sau [28]."))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>International Organization for Standardization (ISO), <i>International Vocabulary of Basic and General Terms in Metrology (VIM)</i>, Geneva, 1993.</li>'
             '<li>ISO/IEC Guide 25, <i>General Requirements for the Competence of Calibration and Testing Laboratories</i>, ISO, 1990.</li>'
             '<li>ANSI/NCSL Z540-1-1994, <i>Calibration Laboratories and Measuring and Test Equipment — General Requirements</i>, ANSI, 1994.</li>'
             '<li>M. A. Lombardi, An introduction to frequency calibration. Part I, <i>Cal Lab Int. J. Metrol.</i>, January–February, 17–28, 1996.</li>'
             '<li>B. N. Taylor and C. E. Kuyatt, Guidelines for evaluating and expressing the uncertainty of NIST measurement results, NIST Tech. Note 1297, 1994.</li>'
             '<li>IEEE, <i>IEEE Standard Definitions of Physical Quantities for Fundamental Frequency and Time Metrology</i>, IEEE 1139, Piscataway, NJ, 1988.</li>'
             '<li>D. W. Allan et al., <i>Standard Terminology for Fundamental Frequency and Time Metrology</i>, NIST Tech. Note 1337, 1990, 139–145.</li>'
             '<li>J. Jesperson, Introduction to the time domain characterization of frequency standards, <i>Proc. 25th PTTI Meeting</i>, 1991, 83–102.</li>'
             '<li>S. R. Stein, Frequency and time — their measurement and characterization, in <i>Precision Frequency Control</i>, Vol. 2, Academic Press, 1985, 191–232.</li>'
             '<li>D. A. Howe, D. W. Allan, and J. A. Barnes, Properties of signal sources and measurement methods, <i>Characterization of Clocks and Oscillators</i>, NIST Tech. Note 1337, 1990, 14–60.</li>'
             '<li>W. A. Marrison, The evolution of the quartz crystal clock, <i>Bell Systems Tech.</i>, 27(3), 510–588, 1948.</li>'
             '<li>J. R. Vig, <i>Introduction to Quartz Frequency Standards</i>, Army Research and Development Technical Report, SLCET-TR-92-1, 1992.</li>'
             '<li>F. L. Walls and J. Gagnepain, Environmental sensitivities of quartz oscillators, <i>IEEE Trans. Ultrason., Ferroelectr., Freq. Control</i>, 39, 241–249, 1992.</li>'
             '<li>W. M. Itano and N. F. Ramsey, Accurate measurement of time, <i>Sci. Am.</i>, 269(1), 56–65, 1993.</li>'
             '<li>L. Lewis, An introduction to frequency standards, <i>Proc. IEEE</i>, 79(7), 927–935, 1991.</li>'
             '<li>J. Vanier and C. Audoin, <i>The Quantum Physics of Atomic Frequency Standards</i>, Adam Hilger, Bristol, 2 vols., 1989.</li>'
             '<li>M. A. Lombardi, An introduction to frequency calibration. Part II, <i>Cal Lab Int. J. Metrology</i>, March–April, 28–34, 1996.</li>'
             '<li>R. Beehler and M. A. Lombardi, <i>NIST Time and Frequency Services</i>, NIST Special Publ. 432, 1991.</li>'
             '<li>B. Hoffmann-Wellenhof, H. Lichtenegger, and J. Collins, <i>GPS: Theory and Practice</i>, 3rd ed., Springer-Verlag, 1994.</li>'
             '<li>ARINC Research Corporation, <i>NAVSTAR Global Positioning System: User’s Overview</i>, NAVSTAR GPS Joint Program Office, Los Angeles, YEE-82-009D, 1991.</li>'
             '<li>T. N. Osterdock and J. A. Kusters, Using a new GPS frequency reference in frequency calibration operations, <i>IEEE Int. Freq. Control Symp.</i>, 1993, 33–39.</li>'
             '<li>R. J. Hesselberth, Precise frequency measurement and calibration, <i>Proc. Natl. Conf. Stan. Lab.</i>, 1988, 47-1–47-7.</li>'
             '<li>V. S. Zhang, D. D. Davis, and M. A. Lombardi, High resolution time interval counter, <i>PTTI Conf.</i>, 1994, 191–200.</li>'
             '<li>A. Clairon et al., A cesium fountain frequency standard: preliminary results, <i>IEEE Trans. Instrum. Meas.</i>, 44(2), 128–131, 1995.</li>'
             '<li>W. M. Itano, Atomic ion frequency standards, <i>Proc. IEEE</i>, 79(7), 936–942, 1991.</li>'
             '<li>D. A. Howe, An extension of the Allan variance with increased confidence at long term, <i>IEEE Int. Freq. Control Symp.</i>, 1995, 321–330.</li>'
             '<li>U.S. Dept. of Transportation, <i>Federal Radionavigation Plan</i>, DOT-VNTSC-RSPA-95-1, DOD-4650.5, 1994.</li>'
             '<li>G. Gibbons, A national GPS policy, <i>GPS World</i>, 7(5), 48–50, 1996.</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 18</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is the English companion to the Vietnamese translation of Chapter 19, “Frequency "
        "Measurement” by Michael A. Lombardi (NIST). All fifteen figures are redrawn as vectors and the four "
        "tables (19.1–19.4) and equations 19.1–19.8 are reproduced. The Vietnamese prose is not repeated "
        "here."))
    b.append(p(
        "Frequency is the rate of a repetitive event, f = 1/T, in hertz. Frequency calibration compares a "
        "device under test (DUT — usually a quartz, rubidium or cesium oscillator) against a reference that "
        "outperforms it by a test uncertainty ratio (TUR), preferably 10:1. The result states the DUT’s "
        "frequency offset and uncertainty relative to its nameplate frequency; the reference must be "
        "traceable to NIST through an unbroken chain, delivered in practice by transfer standards (WWV/WWVB, "
        "LORAN-C, GPS) because oscillators are disturbed by shipping and power cycling."))
    b.append(p(
        "Section 19.2 — uncertainty and stability. Frequency offset f_offset = −Δt/T (Eq. 19.1); +1 µs over "
        "24 h gives −1.16 × 10⁻¹¹ (Eq. 19.2); a 5 MHz oscillator high by 1.16 × 10⁻¹¹ is off by 5.80 × 10⁻⁵ "
        "Hz (Eqs. 19.3–19.4). Table 19.1 tabulates offset vs phase deviation and measurement period. Figure "
        "19.1 shows two phase-comparison graphs (clean = TUR ≥ 10:1; wavy = TUR < 10:1). A 2σ test means a "
        "95.4% probability the offset stays within limits. Stability is how well the frequency is held, not "
        "whether it is right (Figure 19.2); the time-domain statistic is the Allan deviation σ_y(τ) = "
        "√[(1/2(M−1))Σ(yᵢ₊₁−yᵢ)²] (Eq. 19.5), worked through in Table 19.2 (Eq. 19.6, σ_y(1s)=1.17×10⁻¹¹). "
        "Confidence ≈ 1/√M × 100% (Eq. 19.7). Figure 19.3 shows an Allan-deviation graph flattening at the "
        "flicker floor; Figure 19.4 relates accuracy and stability."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Section 19.3 — frequency standards. Quartz oscillators (Figure 19.5) use the piezoelectric effect; "
        "OCXO/TCXO/MCXO trade temperature performance for cost, and aging is a systematic drift (high-quality "
        "units age at 5 × 10⁻⁹/year). Atomic oscillators lock a quartz to an atomic resonance, "
        "f = (E₂−E₁)/h (Eq. 19.8): rubidium (6.834682608 GHz ⁸⁷Rb, 5×10⁻¹⁰…5×10⁻¹², $3–8k), cesium "
        "(9.192631770 GHz ¹³³Cs, primary standard, NIST-7 ±5×10⁻¹⁵, $30–80k, beam-tube life 3–10 y), and "
        "hydrogen maser (1.420405752 GHz, best short-term stability, >$200k). Table 19.3 compares all types."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Section 19.4 — transfer standards. Radio-path variation limits short-term stability but averages out "
        "for uncertainty. Table 19.4 gives traceability: HF (WWV) ±1×10⁻⁷, LF (WWVB, LORAN-C) ±1×10⁻¹², GPS "
        "±5×10⁻¹³ over 24 h. WWVB (60 kHz) and LORAN-C (100 kHz, groundwave third-cycle tracking, TOC pulses) "
        "are described; Figures 19.6–19.7 show LORAN-C path noise (±200 ns) and a 96 h cesium calibration "
        "(cesium low by 3.4×10⁻¹²). GPS: 24 satellites, L1/L2, C/A and P codes, SA ~300 ns; Figures 19.8–19.9 "
        "show 100 s (<1 ns) and 1-week (550 ns range, cesium low by 5×10⁻¹³) comparisons."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "Section 19.5 — calibration methods. Oscillator outputs come as sine, square, pulse or clipped sine "
        "(Figure 19.10); one sine cycle is 2π of phase (Figure 19.11). A phase comparison with a changing "
        "phase relationship gives the offset (Figure 19.12). A frequency counter is simple but limited by "
        "its timebase. The time-interval method uses a TIC (Figures 19.13–19.14): start/stop inputs, "
        "timebase, main gate and counter; resolution is improved by interpolation (1 ns common, 10 ps "
        "available). Dead time and divider instability limit short-term stability. The Dual Mixer Time "
        "Difference method (Figure 19.15) mixes the DUT and reference with a synthesizer to produce beat "
        "frequencies, then uses a zero-crossing detector, event counter and TIC — reducing noise to ±5 ps or "
        "less. Section 19.6 — future: cesium fountains, trapped-ion standards (±1×10⁻¹⁸), satellite-based "
        "transfer, LORAN-C phase-out, GPS improvement when SA ends."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(fig(11, F.fig(11), "en"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p("The chapter closes with 28 references, reproduced in the Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 18</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 19 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 19 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 19 “Đo tần số” của Michael A. Lombardi (NIST) — tổng quan hiệu "
            "chuẩn tần số, độ không đảm bảo và độ ổn định (Allan deviation), chuẩn tần số thạch anh và "
            "nguyên tử, chuẩn chuyển tiếp (WWVB, LORAN-C, GPS), và các phương pháp hiệu chuẩn (TIC, DMTD), "
            "với 15 hình và 4 bảng." if vi else
            "Companion to Chapter 19 of the CRC Measurement Handbook — frequency measurement: calibration, "
            "uncertainty and stability, quartz/atomic standards, transfer standards and calibration methods.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 19' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 19' % BASE_EN)
    meta = ("Chương 19 · theo Ch19.pdf (CRC Press, 1999) · 15 hình, 4 bảng, 28 tài liệu tham khảo" if vi
            else "Chapter 19 · 15 figures, 4 tables, 28 references")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en()))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
