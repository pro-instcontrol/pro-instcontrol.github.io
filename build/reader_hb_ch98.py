# -*- coding: utf-8 -*-
"""Handbook Chapter 98 — Optimal Control (Halit Eren, Curtin University of
Technology).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch98.py
"""
import os

import hb98fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch98-optimal-control"
TITLE_EN = "Optimal Control"
TITLE_VI = "Điều khiển tối ưu"
BYLINE = "Halit Eren · Curtin University of Technology"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-98-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


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


def mtx(rows):
    """Bracketed matrix for display inside an .eq block."""
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return '<span class="mxw"><table class="mx"><tbody>%s</tbody></table></span>' % body


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def dt(term, definition):
    return p("<b>%s:</b> %s" % (term, definition))


# ================================================================ Vietnamese

def body_vi():
    b = []

    b.append(h2("98.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Điều khiển tối ưu là việc làm cực đại (hoặc cực tiểu) giá trị của một hàm được chọn làm "
        "chỉ tiêu chất lượng hay hàm chi phí của một hệ điều khiển đang vận hành. Lý thuyết điều "
        "khiển tối ưu, theo nghĩa khác, là phần toán học đi tìm những tham số khiến chỉ tiêu chất "
        "lượng ấy đạt giá trị cực trị trong khi vẫn thoả mãn các ràng buộc của hệ."))
    b.append(p(
        "Điều khiển tối ưu được ứng dụng trong nhiều lĩnh vực: vệ tinh và hàng không vũ trụ, máy bay "
        "và tàu vũ trụ, kỹ thuật hoá học, kỹ thuật thông tin, robot và ngành robot, hệ thống điện, "
        "truyền động điện, máy tính và các hệ máy tính, v.v. Trong nhiều ứng dụng, cách ghép nối đơn "
        "giản các thiết bị điều khiển và bộ điều khiển không đem lại chế độ vận hành kinh tế nhất — và "
        "điều khiển tối ưu chính là lời giải cho bài toán đó. Vì vậy, tối ưu hoá có ích khi cần thu "
        "được kết quả tốt nhất từ một quá trình đã biết. Nếu quá trình đang vận hành ở trạng thái "
        "dừng thì tối ưu hoá coi quá trình là dừng và chỉ quan tâm tới các điểm làm việc. Khi quá "
        "trình là dừng, điểm làm việc tối ưu thu được có thể dễ dàng duy trì bằng cách đặt các điểm "
        "đặt định trước và các tham số điều khiển tính sẵn. Tuy nhiên, nếu quá trình thay đổi theo "
        "thời gian thì với mỗi thay đổi đều phải xác định điểm đặt tối ưu mới cho hệ."))
    b.append(p(
        "Hiệu năng của một hệ được tối ưu vì nhiều lý do: nâng cao chất lượng, tăng sản lượng, giảm "
        "phế phẩm, đạt hiệu suất cao hơn, tối đa hoá an toàn, tiết kiệm thời gian và năng lượng, v.v. "
        "Trong nhiều bài toán tối ưu, các điều kiện biên được áp đặt bởi chính hệ thống vì lý do an "
        "toàn vận hành, do khả năng cấp công suất nhỏ nhất và lớn nhất, do giới hạn dung lượng lưu "
        "trữ, do năng lực của máy vận hành, do nhiệt độ, tốc độ, lực, gia tốc — nói chung là vì bất "
        "kỳ lý do vật lý cứng nào khác."))
    b.append(p(
        "Để giải bài toán điều khiển tối ưu có thể dùng nhiều phương pháp khác nhau, tuỳ bản chất bài "
        "toán. Ví dụ, nếu chỉ tiêu chất lượng và các ràng buộc có thể phát biểu dưới dạng hàm đại số "
        "tuyến tính của các biến được điều khiển thì quy hoạch tuyến tính có thể là lựa chọn tốt "
        "nhất; phương pháp đơn hình (simplex) cho một cách giải bài toán quy hoạch tuyến tính khá "
        "tốt. Nếu các phương trình mô tả hệ là phi tuyến thì lời giải có thể phải dùng các kỹ thuật "
        "phi tuyến hoặc tuyến tính hoá bài toán trên từng miền con. Nếu bài toán là xác định giá trị "
        "lớn nhất của một hàm có hai biến trở lên thì có thể dùng phương pháp dốc nhất lên (hoặc dốc "
        "nhất xuống), đôi khi gọi là phương pháp leo dốc hay phương pháp gradient."))
    b.append(p(
        "Các phương pháp leo dốc vẫn được dùng phổ biến và dễ hiểu. Ở đây chúng được trình bày vắn "
        "tắt trước hết để tạo một nền tảng tốt cho việc hiểu đúng lý thuyết điều khiển tối ưu."))
    b.append(p(
        "Hình 98.1 minh hoạ kỹ thuật leo dốc trong vùng có cực tiểu tuyệt đối. Hình này cũng chỉ ra "
        "một cạm bẫy thường gặp trong lý thuyết điều khiển: các cực đại và cực tiểu địa phương. Như "
        "thấy trên hình, dấu của đạo hàm bậc một của hàm đổi dấu khi đạo hàm đi qua điểm cực đại. "
        "Phương pháp này thường bắt đầu từ một điểm ước lượng ban đầu, tại đó đạo hàm bậc một được "
        "coi (được đoán) là bằng không. Điểm này sau đó được dùng để đi theo hướng dốc nhất lên hoặc "
        "dốc nhất xuống, tuỳ trường hợp, tới điểm tiếp theo, cho tới khi tìm được cực đại hoặc cực "
        "tiểu tuyệt đối mà không bị mắc kẹt ở các điểm cực trị địa phương. Có nhiều phương pháp khác "
        "nhau để tìm cực đại hoặc cực tiểu bằng leo dốc, và Hình 98.2 minh hoạ một số ví dụ triển "
        "khai."))
    b.append(fig(1, F.fig(1)))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Ngoài các kỹ thuật leo dốc, còn nhiều phương pháp mới để giải những bài toán điều khiển tối "
        "ưu hiện đại có liên quan tới các siêu không gian (nhiều biến), phức tạp về bản chất và có "
        "ràng buộc ngặt. Nếu có một mô hình toán học tốt của hệ thì có thể dùng các phương pháp tối "
        "ưu hoá để tìm điều kiện tối ưu trên mô hình thay vì tìm tối ưu trên chính quá trình thực. "
        "Điều đó cho thấy sự sẵn có của mô hình quyết định loại phương pháp tối ưu hoá được dùng."))

    # ---------------------------------------------------------------- 98.2
    b.append(h2("98.2 Hàm chi phí", "Cost Function"))
    b.append(p(
        "Khi thiết kế hệ điều khiển tối ưu, có thể đặt ra những quy tắc xác định quyết định điều "
        "khiển, chịu những ràng buộc nhất định, sao cho một độ đo nào đó của sự lệch khỏi trường hợp "
        "lý tưởng là nhỏ nhất. Độ đo đó thường do một chỉ tiêu chất lượng hay hàm chi phí được chọn "
        "cung cấp. Chỉ tiêu chất lượng là một hàm mà giá trị của nó cho biết hiệu năng thực tế của "
        "hệ khớp với hiệu năng mong muốn đến mức nào. Việc chọn đúng chỉ tiêu chất lượng là quan "
        "trọng, vì nó quyết định bản chất và độ phức tạp của bài toán. Nói cách khác, điều khiển tối "
        "ưu là tuyến tính hay phi tuyến, là dừng hay biến thiên theo thời gian, sẽ phụ thuộc vào chỉ "
        "tiêu chất lượng được chọn. Việc chọn chỉ tiêu chất lượng phụ thuộc vào đặc tính kỹ thuật "
        "của hệ, vào khả năng thực hiện được về mặt vật lý, và vào những hạn chế đặt lên tín hiệu "
        "điều khiển sẽ dùng. Nói chung, chọn một chỉ tiêu chất lượng thích hợp là sự thoả hiệp giữa "
        "một đánh giá có ý nghĩa về hiệu năng của hệ và sự sẵn có của những mô tả toán học khả thi."))
    b.append(p(
        "Chỉ tiêu chất lượng do người kỹ sư chọn, sao cho hệ hành xử theo cách mong muốn. Theo định "
        "nghĩa, một hệ mà thiết kế của nó làm cực tiểu chỉ tiêu chất lượng đã chọn là hệ tối ưu. Cần "
        "nhấn mạnh rằng một hệ tối ưu theo một chỉ tiêu chất lượng có thể không tối ưu theo một chỉ "
        "tiêu chất lượng khác. Trong các hệ thực tế, vì độ phức tạp và chi phí triển khai có thể lớn, "
        "đôi khi dùng những luật điều khiển tối ưu xấp xỉ — không gắn cứng vào một chỉ tiêu chất "
        "lượng duy nhất — lại tốt hơn."))
    b.append(p(
        "Trước khi bắt đầu tối ưu hoá bất kỳ hệ nào, cần phát biểu được bài toán: phải có thông tin "
        "về các tham số và các phương trình mô tả hệ, về các ràng buộc, về lớp các vectơ điều khiển "
        "được phép, và về chỉ tiêu chất lượng đã chọn. Sau đó có thể tiến hành tìm nghiệm bằng cách "
        "xác định vectơ điều khiển tối ưu u(k) trong lớp các vectơ được phép. Vectơ điều khiển u(k) "
        "sẽ phụ thuộc vào những yếu tố như bản chất của chỉ tiêu chất lượng, các ràng buộc, các giá "
        "trị đầu của trạng thái, các đầu ra đầu, cũng như trạng thái mong muốn và các đầu ra mong "
        "muốn. Nếu nghiệm giải tích là không thể hoặc quá phức tạp thì có thể dùng các nghiệm tính "
        "toán thay thế."))
    b.append(p(
        "Trong những trường hợp đơn giản, có thể chọn sai số giữa đáp ứng mong muốn và đáp ứng thực "
        "làm chỉ tiêu chất lượng cần cực tiểu. Ví dụ, Hình 98.3 mô tả những cách khác nhau để biểu "
        "diễn sai số giữa đáp ứng thực và đáp ứng mong muốn. Mục tiêu là giữ sai số càng nhỏ càng "
        "tốt. Tích phân theo thời gian của sai số cho biết mức độ nghiêm trọng của sai số. Tuy nhiên, "
        "vì sai số dương và sai số âm triệt tiêu nhau về mặt toán học, nên phải dùng giá trị tuyệt "
        "đối:"))
    b.append(eq("IAE = ∫<sub>0</sub><sup>T</sup> |e(t)| dt", "98.1"))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Trong nhiều trường hợp, dùng bình phương sai số tích phân lại tốt hơn, vì nó tính đến cả "
        "những sai số lớn chứ không chỉ những sai số thông thường:"))
    b.append(eq("ISE = ∫<sub>0</sub><sup>T</sup> e<sup>2</sup>(t) dt", "98.2"))
    b.append(p(
        "Có thể dùng những hàm phụ thuộc thời gian để bắt lấy những sai số xuất hiện muộn về sau, "
        "thay vì chỉ những quá độ thông thường:"))
    b.append(eq("ITAE = ∫<sub>0</sub><sup>T</sup> t|e(t)| dt", "98.3"))
    b.append(p("và"))
    b.append(eq("ITSE = ∫<sub>0</sub><sup>T</sup> t e<sup>2</sup>(t) dt", "98.4"))
    b.append(p(
        "Sai số bình phương trung bình, MSE, cũng hay được dùng, vì chỉ cần sửa đổi chút ít là có thể "
        "đưa vào các kỹ thuật thống kê và phân tích nhiễu ngẫu nhiên:"))
    b.append(eq("MSE = lim<sub>T→∞</sub> (1/T) ∫<sub>0</sub><sup>T</sup> e<sup>2</sup>(t) dt", "98.5"))
    b.append(p(
        "Lý thuyết điều khiển tối ưu hiện đại được xây dựng trong khuôn khổ không gian trạng thái, "
        "và các chỉ tiêu chất lượng phức tạp hơn, bao quát hơn, như trình bày dưới đây."))
    b.append(p(
        "Giả sử lệnh điều khiển của một hệ được biểu diễn dưới dạng vectơ u và trạng thái của hệ được "
        "mô tả bởi x (Từ điển tiếng Anh Oxford định nghĩa <i>trạng thái</i> là điều kiện xét theo "
        "hoàn cảnh, thuộc tính, cấu trúc, hình thức, pha hay tương tự). Hơn nữa, giả sử tốc độ thay "
        "đổi của trạng thái là một hàm của trạng thái x, của lệnh điều khiển u và của thời gian t:"))
    b.append(eq("ẋ = f(x, u, t)&nbsp;&nbsp;&nbsp; x(0) = x<sub>0</sub> đã biết", "98.6"))
    b.append(p(
        "Khi đó cần xác định một luật điều khiển u(x, t) hoặc một quỹ đạo điều khiển u(t) sao cho một "
        "chỉ tiêu chất lượng — hay một phiếm hàm vô hướng —"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> g(x(t), u(t), t) dt", "98.7"))
    b.append(p(
        "đạt giá trị nhỏ nhất trong mọi khả năng khác mà vẫn thoả mãn Eq. 98.6. Đồng thời cũng phải "
        "thoả mãn ràng buộc về quan hệ biên x(T) = x<sub>f</sub>."))
    b.append(p("Một dạng rất thường gặp của J(u) là điều khiển thời gian tối thiểu, trong đó"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> dt = T", "98.8"))
    b.append(p(
        "Nhiều tiêu chuẩn khác cũng được dùng, như nhiên liệu tối thiểu, năng lượng tối thiểu, và "
        "những dạng bậc hai khác:"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> u(t) dt", "98.9"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> u<sup>2</sup>(t) dt", "98.10"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> [q x<sup>2</sup>(t) + r u<sup>2</sup>(t)] dt", "98.11"))
    b.append(p(
        "Một dạng tổng quát của chỉ tiêu chất lượng cho điều khiển tối ưu hệ liên tục được phát biểu "
        "là:"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> g[x(t), u(t), t] dt", "98.12"))
    b.append(p(
        "Chỉ tiêu chất lượng này được cực tiểu hoá với các ràng buộc ở trên, đồng thời x(t) là một "
        "trạng thái chấp nhận được, x(t) ∈ X(t), ∀t ∈ (t<sub>0</sub>, t<sub>f</sub>)."))
    b.append(p(
        "Những biến thể nhỏ của các phương trình 98.9 đến 98.12 dẫn tới phần toán học của các phiên "
        "bản thời gian rời rạc, hay phiên bản số, của điều khiển tối ưu."))

    # ---------------------------------------------------------------- 98.3
    b.append(h2("98.3 Phép biến phân", "Calculus of Variations"))
    b.append(p(
        "Phép biến phân thích hợp để giải các bài toán tối ưu tuyến tính hoặc phi tuyến với điều kiện "
        "biên tuyến tính hoặc phi tuyến. Về cơ bản, đây là một tập hợp nhiều phương pháp giải tích "
        "khác nhau, và mỗi sách trình bày chúng một cách khác nhau. Ở đây chỉ giới thiệu một cách "
        "tiếp cận điển hình — cách dẫn tới những lý thuyết hiện đại tổng quát hơn và được dùng rộng "
        "rãi hơn."))
    b.append(p("Xét một hệ động học vận hành trong khoảng thời gian t<sub>0</sub> &lt; t &lt; "
               "t<sub>f</sub>"))
    b.append(eq("ẋ(t) = f(x(t), u(t), t)&nbsp;&nbsp;&nbsp; với t ∈ (t<sub>0</sub>, t<sub>f</sub>)",
                "98.13"))
    b.append(p("trong đó trạng thái đầu x<sub>0</sub> đã cho."))
    b.append(p(
        "Hệ có n biến trạng thái và m biến điều khiển. Hàm vô hướng cần tối ưu là"))
    b.append(eq("J = k[x(t<sub>f</sub>)] + ∫ L[x, u, t] dt", "98.14"))
    b.append(p("Định nghĩa một hàm vô hướng, chẳng hạn hàm Hamilton:"))
    b.append(eq("H = H[x, u, λ, t] = L[x, u, t] + Σ<sub>i</sub> λ<sub>i</sub> f<sub>i</sub>", "98.15"))
    b.append(p("λ được gọi là nhân tử Lagrange. Cũng định nghĩa một hàm mục tiêu hiệu chỉnh:"))
    b.append(eq("J = k[x(t<sub>1</sub>)] + ∫ H dt", "98.16"))
    b.append(p("nghiệm thu được là tối ưu khi"))
    b.append(eq("λ̇ = −∂H/∂x = −∂L/∂x − Σ<sub>i</sub> λ<sub>i</sub> ∂f<sub>i</sub>/∂x", "98.17"))
    b.append(eq("λ(t<sub>f</sub>) = ∂k/∂x", "98.18"))
    b.append(eq("∂H/∂u = ∂L/∂u + Σ<sub>i</sub> λ<sub>i</sub> ∂f<sub>i</sub>/∂u = 0,"
                "&nbsp;&nbsp; t<sub>0</sub> &lt; t &lt; t<sub>f</sub>", "98.19"))
    b.append(p(
        "Nghiệm của các phương trình 98.17 và 98.19 ở dạng trên rất khó tìm. Tuy vậy, từ những ý "
        "tưởng đó có thể xây dựng được những lý thuyết tổng quát hơn, chẳng hạn nguyên lý cực đại "
        "Pontryagin."))
    b.append(p(
        "Một bước tiến so với phép biến phân là nguyên lý cực đại Pontryagin, cho lời giải dễ hơn và "
        "mở rộng phạm vi áp dụng sang các bài toán điều khiển có ràng buộc. Ở dạng đơn giản nhất, "
        "nguyên lý này có thể giải thích như sau."))
    b.append(p("Cho hệ"))
    b.append(eq("ẋ<sub>i</sub> = f<sub>i</sub>[x, u, t]", "98.20"))
    b.append(p("và một hàm mục tiêu"))
    b.append(eq("J = Σ<sub>i</sub> k<sub>i</sub> x<sub>i</sub>(t<sub>f</sub>)", "98.21"))
    b.append(p("Nguyên lý cực đại phát biểu rằng nếu vectơ điều khiển u là tối ưu thì hàm Hamilton"))
    b.append(eq("H = Σ<sub>i</sub> p<sub>i</sub> f<sub>i</sub>", "98.21a"))
    b.append(p("cũng đạt cực đại theo vectơ điều khiển u trên các khoảng đã cho."))
    b.append(eq("ṗ<sub>i</sub> = −Σ<sub>j</sub> (∂f<sub>j</sub>/∂x<sub>i</sub>) p<sub>j</sub>",
                "98.21b"))
    b.append(eq("p<sub>i</sub>(t<sub>f</sub>) = k<sub>i</sub>", "98.21c"))
    b.append(p(
        "trong đó p là vectơ liên hợp hay vectơ đồng trạng thái, và"))
    b.append(eq("ẋ<sub>i</sub> = ∂H/∂p<sub>i</sub> = f<sub>i</sub>[x, u, t]", "98.21d"))
    b.append(eq("∂H/∂x<sub>i</sub> = −ṗ<sub>i</sub>", "98.21e"))
    b.append(p(
        "Các giá trị đầu của vectơ trạng thái x cung cấp những hằng số còn lại cần thiết để giải hệ "
        "phương trình này nhằm xác định vectơ điều khiển tối ưu. Phương pháp này cũng áp dụng được "
        "cho các hệ có chỉ tiêu chất lượng phức tạp."))
    b.append(p(
        "Một mở rộng khác của phép biến phân là bộ lọc Kalman. Về bản chất, Kalman là một kỹ thuật "
        "lọc tổng quát có thể áp dụng để giải những bài toán như ước lượng tối ưu, dự báo, lọc nhiễu, "
        "điều khiển tối ưu ngẫu nhiên và thiết kế bộ điều khiển tối ưu. Phương pháp này có ưu điểm là "
        "cho ước lượng các biến ngay cả khi có nhiễu, với cả quá trình dừng và quá trình không dừng. "
        "Hầu hết các loại nhiễu khác đều có thể xử lý bằng phương pháp này nếu chuyển được chúng về "
        "dạng Gauss. Kỹ thuật này cũng dùng được cho các hệ có nhiễu cưỡng bức và có nhiều hơn một "
        "nguồn nhiễu. Nói chung, những hệ có hàm mục tiêu bậc hai hoặc có nhiễu Gauss không tương "
        "quan ở đầu vào là phù hợp với kỹ thuật này."))
    b.append(p(
        "Một cách áp dụng bộ lọc Kalman cho một hệ phi tuyến là tìm một ước lượng tốt của hệ rồi dùng "
        "nó để định nghĩa một tập phương trình trạng thái tuyến tính mới, xấp xỉ hệ về dạng tuyến "
        "tính tại một điểm làm việc danh định. Sau đó có thể áp dụng bộ lọc cho tập phương trình "
        "tuyến tính mới."))
    b.append(p(
        "Ứng dụng của bộ lọc Kalman trong các hệ thiết bị đo và cảm biến, cũng như trong những bài "
        "toán điều khiển tối ưu khác, là vô tận. Nó có thể được lập trình dễ dàng trên máy tính số."))

    # ---------------------------------------------------------------- 98.4
    b.append(h2("98.4 Phương trình Riccati", "Riccati Equation"))
    b.append(p(
        "Một số mô hình trong các bài toán tối ưu hoá giống với mô hình của lý thuyết điều khiển "
        "truyền thống và thực tiễn. Trong những mô hình này, biến quá trình và biến điều khiển là "
        "vectơ và bị ràng buộc bởi các phương trình đối tượng tuyến tính. Các hàm chi phí có dạng "
        "chi phí bậc hai. Những hệ như vậy được gọi là hệ phương trình tuyến tính bậc hai, hay hệ "
        "LQ. Lý thuyết và mô hình của hệ LQ đã được phát triển đầy đủ cho cả trường hợp tất định và "
        "trường hợp ngẫu nhiên."))
    b.append(p("Phát biểu bài toán điều khiển tối ưu bậc hai như sau:"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)&nbsp;&nbsp;&nbsp; x(0) = x<sub>0</sub>", "98.22"))
    b.append(p("trong đó"))
    b.append(p(
        "x(k) = vectơ trạng thái (vectơ n phần tử)<br>"
        "u(k) = vectơ điều khiển (vectơ r phần tử)<br>"
        "A = ma trận n × n không suy biến<br>"
        "B = ma trận n × r"))
    b.append(p(
        "Mục tiêu là tìm dãy điều khiển tối ưu u(0), u(1), …, u(N − 1) làm cực tiểu chỉ tiêu chất "
        "lượng bậc hai"))
    b.append(eq("J = ½x*(N)Sx(N) + ½ Σ<sub>k=0</sub><sup>N−1</sup> [x*(k)Qx(k) + u*(k)Ru(k)]",
                "98.23"))
    b.append(p("trong đó x* và u* lần lượt là chuyển vị của các ma trận x và u;"))
    b.append(p(
        "Q = ma trận đối xứng n × n xác định dương hoặc nửa xác định dương<br>"
        "R = ma trận đối xứng r × r xác định dương hoặc nửa xác định dương<br>"
        "S = ma trận đối xứng n × n xác định dương hoặc nửa xác định dương"))
    b.append(p(
        "Các ma trận Q, S và R được chọn để đánh trọng số tầm quan trọng tương đối của các độ đo hiệu "
        "năng do vectơ trạng thái x(k), trạng thái cuối x(N) và vectơ điều khiển u(k) gây ra, tương "
        "ứng, với k = 0, 1, 2, …, N − 1. Trạng thái đầu của hệ là tuỳ ý nhưng trạng thái cuối x(N) có "
        "thể là cố định. Nếu trạng thái cuối là cố định thì có thể bỏ số hạng ½x*(N)Sx(N) ra khỏi "
        "chỉ tiêu chất lượng và áp đặt trạng thái kết thúc x<sub>f</sub>. Nếu trạng thái cuối không "
        "cố định thì số hạng ½x*(N)Sx(N) biểu thị trọng số của độ đo hiệu năng đối với trạng thái "
        "cuối."))
    b.append(p(
        "Có nhiều cách khác nhau để giải các phương trình trên, một trong số đó dùng khái niệm nhân "
        "tử Lagrange. Nhờ nhân tử Lagrange, chỉ tiêu chất lượng có thể được hiệu chỉnh thành"))
    b.append(eq("L = ½x*(N)Sx(N) + Σ<sub>k</sub> {½x*(k)Qx(k) + ½u*(k)Ru(k) "
                "+ λ*(k+1)[Ax(k) + Bu(k) − x(k+1)]}", "98.24"))
    b.append(p(
        "Đã biết rằng cực tiểu hoá hàm L tương đương với cực tiểu hoá chỉ tiêu chất lượng J với "
        "cùng các ràng buộc."))
    b.append(p(
        "Để cực tiểu hoá, cần lấy đạo hàm của L theo các vectơ x(k), u(k) và λ(k) rồi cho các kết "
        "quả bằng không. Đạo hàm riêng của hàm L theo các biến cho ta"))
    b.append(eq("∂L/∂x(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Qx(k) + A*λ(k+1) − λ(k) = 0", "98.25"))
    b.append(eq("∂L/∂x(N) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Sx(N) − λ(N) = 0", "98.26"))
    b.append(eq("∂L/∂u(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Ru(k) − B*λ(k+1) = 0", "98.27"))
    b.append(p("và"))
    b.append(eq("∂L/∂λ(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Ax(k−1) + Bu(k−1) − x(k) = 0", "98.28"))
    b.append(p(
        "Xem xét kỹ các công thức trên cho thấy phương trình cuối cùng chỉ đơn giản là phương trình "
        "trạng thái với k = 1, 2, 3, … N. Đồng thời, giá trị của nhân tử Lagrange có thể xác định từ "
        "Eq. 98.26. Nhân tử Lagrange thường được gọi là đồng vectơ hay vectơ liên hợp."))
    b.append(p("Viết lại các phương trình 98.25 và 98.27"))
    b.append(eq("λ(k) = Qx(k) + A*λ(k+1)", "98.29"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*λ(k+1)", "98.30"))
    b.append(p("phương trình trạng thái 98.22 có thể được viết thành"))
    b.append(eq("x(k+1) = Ax(k) − BR<sup>−1</sup>B*λ(k+1)", "98.31"))
    b.append(p(
        "Để có nghiệm của bài toán cực tiểu hoá, cần giải đồng thời các phương trình 98.29 và 98.31 "
        "như một bài toán biên hai điểm. Nghiệm của hai phương trình này ở dạng trên, cùng các giá "
        "trị tối ưu của vectơ trạng thái và vectơ nhân tử Lagrange, sẽ dẫn tới giá trị của vectơ "
        "điều khiển u(k) làm tối ưu hệ điều khiển hở. Tuy nhiên, với các hệ điều khiển kín thì phải "
        "áp dụng các phép biến đổi Riccati."))
    b.append(eq("u(k) = −K(k)x(k)", "98.32"))
    b.append(p(
        "trong đó K(k) là ma trận phản hồi r × n. Bây giờ có thể thu được phương trình Riccati ở "
        "dạng phản hồi bằng cách giả thiết λ(k) được viết là"))
    b.append(eq("λ(k) = P(k)x(k)", "98.33"))
    b.append(p("trong đó P(k) là ma trận n × n. Thay Eq. 98.33 vào 98.29 và 98.31 cho"))
    b.append(eq("P(k)x(k) = Qx(k) + A*P(k+1)x(k+1)", "98.34"))
    b.append(eq("x(k+1) = Ax(k) − BR<sup>−1</sup>B*P(k+1)x(k+1)", "98.35"))
    b.append(p(
        "Khi viết các phương trình 98.34 và 98.35, nhân tử Lagrange λ(k) đã được khử. Đây là một "
        "bước quan trọng trong việc giải bài toán biên hai điểm. Bằng những biến đổi tiếp theo có "
        "thể chỉ ra rằng"))
    b.append(eq("P(k) = Q + A*P(k+1)A − A*P(k+1)B[R + B*P(k+1)B]<sup>−1</sup>B*P(k+1)A", "98.36"))
    b.append(p("Phương trình 98.36 được gọi là phương trình Riccati."))
    b.append(p("Từ các phương trình 98.26 và 98.33, viết λ(N) = Sx(N) = P(N)x(N) cho"))
    b.append(eq("P(N) = S", "98.37"))
    b.append(p(
        "Do đó, có thể giải phương trình Riccati ngược từ k = N về k = 0, bắt đầu từ những giá trị "
        "đã biết của P(N)."))
    b.append(p(
        "Vectơ điều khiển tối ưu u(k) bây giờ có thể được tính từ các phương trình 98.29, 98.30 và "
        "98.35"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*λ(k+1) = −R<sup>−1</sup>B*(A*)<sup>−1</sup>[P(k) − Q]x(k) "
                "= −K(k)x(k)", "98.38"))
    b.append(p("trong đó"))
    b.append(eq("K(k) = −R<sup>−1</sup>B*(A*)<sup>−1</sup>[P(k) − Q]", "98.39"))
    b.append(p(
        "Đáng chú ý là vectơ điều khiển tối ưu có thể thu được ở những dạng hơi khác nhau bằng những "
        "biến đổi khác nhau của các phương trình trên, chẳng hạn"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*[P<sup>−1</sup>(k+1) + BR<sup>−1</sup>B*]<sup>−1</sup>Ax(k)",
                "98.40"))
    b.append(p(
        "Các phương trình 98.38 và 98.39 cho thấy luật điều khiển tối ưu đòi hỏi phản hồi vectơ "
        "trạng thái với hệ số khuếch đại biến thiên theo thời gian K(k). Hình 98.4 minh hoạ sơ đồ "
        "điều khiển tối ưu của một hệ dựa trên chỉ tiêu chất lượng bậc hai. Trong ứng dụng thực tế, "
        "K(k) biến thiên theo thời gian được tính trước khi quá trình bắt đầu. Một khi đã biết ma "
        "trận trạng thái A, ma trận điều khiển B và các ma trận trọng số Q, R, S thì hệ số khuếch "
        "đại K(k) có thể được tính trước ngoài tuyến để dùng về sau. Vectơ điều khiển u(k) ở mỗi "
        "bước có thể xác định ngay bằng cách nhân trước vectơ trạng thái x(k) với hệ số khuếch đại "
        "đã biết K(k)."))
    b.append(fig(4, F.fig(4)))
    b.append(p(
        "Từ các phương trình trên cũng có thể tính được giá trị nhỏ nhất của chỉ tiêu chất lượng. "
        "Dùng các giá trị đầu"))
    b.append(eq("J<sub>min</sub> = ½x*(0)P(0)x(0)", "98.41"))
    b.append(p(
        "Nghiệm dừng của phương trình Riccati là cần thiết khi xử lý các bài toán điều khiển tối ưu "
        "bất biến theo thời gian (ở chế độ dừng). Có nhiều cách thu được nghiệm Riccati dừng; một ví "
        "dụ được đưa ra dưới đây."))
    b.append(eq("P = Q + A*PA − A*PB(R + B*PB)<sup>−1</sup>B*PA", "98.42"))
    b.append(p("Giá trị dừng của K có thể tìm được là"))
    b.append(eq("K = (R + B*PB)<sup>−1</sup>B*PA", "98.43"))
    b.append(p("và luật điều khiển tối ưu cho chế độ dừng có thể biểu diễn là"))
    b.append(eq("u(k) = −(R + B*PB)<sup>−1</sup>B*PA x(k)", "98.44"))
    b.append(p(
        "Mục này được trình bày cho các hệ điều khiển tối ưu thời gian rời rạc thay vì hệ liên tục, "
        "do việc dùng máy tính và bộ vi xử lý làm công cụ điều khiển ngoài tuyến và trực tuyến đã "
        "trở nên phổ biến rộng rãi gần đây. Vì các nguyên lý là như nhau, nên chỉ cần sửa đổi nhỏ là "
        "có thể mở rộng lời giải cho các hệ thời gian liên tục."))

    # ---------------------------------------------------------------- 98.5
    b.append(h2("98.5 Ma trận phản hồi trạng thái", "State Feedback Matrix"))
    b.append(p(
        "Phương pháp phản hồi trạng thái là một kỹ thuật thiết kế khác, cho phép người thiết kế đặt "
        "các cực của hệ ở bất kỳ đâu cần thiết. Cách tiếp cận này được gọi là phương pháp đặt cực, "
        "trong đó thuật ngữ <i>cực</i> chỉ các cực của hàm truyền vòng kín như trên Hình 98.5. Trong "
        "phương pháp này, giả thiết rằng các biến trạng thái đo được và sẵn sàng cho phản hồi. Nếu "
        "trạng thái sẵn có thì hệ được gọi là tất định: hệ không có nhiễu và các tham số của nó đã "
        "biết đầy đủ. Nếu trạng thái không sẵn có thì có thể chọn những phương pháp như các luật "
        "phản hồi đo lường hay các bộ ước lượng trạng thái."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Trong nhiều ứng dụng, thay vì dùng các biến trạng thái, dùng các ước lượng trạng thái đến "
        "từ một bộ quan sát hoặc một bộ lọc Kalman lại tiện hơn. Trong trường hợp này có ba phương "
        "pháp nổi tiếng: tương đương chắc chắn (<i>certainty equivalence</i>), tách rời "
        "(<i>separation</i>) và điều khiển đối ngẫu (<i>dual control</i>). Tương đương chắc chắn có "
        "ưu điểm đáng kể so với các phương pháp khác vì nó dẫn tới những luật điều khiển tối ưu tất "
        "định như nguyên lý Pontryagin, hoặc tới kỳ vọng có điều kiện của trạng thái như bộ lọc "
        "Kalman. Nó cho một bộ điều khiển thực tiễn, có thể xây dựng như một bộ lọc và một luật tối "
        "ưu mắc nối tiếp."))
    b.append(p(
        "Bộ điều khiển phản hồi trạng thái tương đối dễ triển khai. Ví dụ, trong phương pháp đặt "
        "cực, quan hệ giữa tín hiệu điều khiển phản hồi u và trạng thái x của hệ tuyến tính là"))
    b.append(eq("u(k) = −Kx(k)", "98.45"))
    b.append(p("Trong trường hợp tuyến tính bậc hai, hệ số khuếch đại K biến thiên theo thời gian:"))
    b.append(eq("u(k) = −K(k)x(k)", "98.46"))
    b.append(p("trong đó K là ma trận phản hồi (n × r). Điều này đúng ít nhất trong hai trường hợp."))
    b.append(p(
        "1. Trong các hệ tuyến tính không nhiễu, với bộ điều khiển đặt cực và một bộ quan sát làm bộ "
        "ước lượng trạng thái, thuật toán điều khiển cho hệ"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)<br>y(k) = Cx(k)"))
    b.append(p("là"))
    b.append(eq("x̂(k+1) = (A − GC)x̂(k) + Gy(k) + Bu(k)", "98.47"))
    b.append(eq("u(k) = Kx̂(k)", "98.48"))
    b.append(p(
        "trong đó các trị riêng của (A − GC) và (A + BK) được chọn để thoả mãn các chỉ tiêu thiết kế."))
    b.append(p(
        "2. Trong các hệ tuyến tính chịu ảnh hưởng của nhiễu trắng Gauss, trong đó tín hiệu điều "
        "khiển là tối ưu theo một tiêu chuẩn bậc hai, hệ"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k) + Gv(k)", "98.49"))
    b.append(eq("y(k) = Cx(k) + w(k)", "98.50"))
    b.append(p("có luật điều khiển dạng"))
    b.append(eq("x̂(k+1|k) = Ax̂(k) + Bû(k)", "98.51"))
    b.append(eq("x̂(k+1) = Ax̂(k+1|k) + G(k+1)[y(k+1) − Cx̂(k+1|k)]", "98.52"))
    b.append(eq("û(k) = K(k)x̂(k)", "98.53"))
    b.append(p(
        "trong đó K(k) và G(k) lần lượt là các hệ số khuếch đại tối ưu cho điều khiển tối ưu tất định "
        "và cho bộ lọc Kalman."))
    b.append(p(
        "Trong thực tế, không phải mọi biến trạng thái đều dễ tiếp cận; nói chung chỉ các đầu ra của "
        "hệ là đo được. Vì vậy, khi một thiết kế yêu cầu phản hồi từ các biến trạng thái thì cần "
        "quan sát trạng thái từ thông tin chứa trong đầu ra cũng như trong các biến đầu vào. Phân hệ "
        "thực hiện việc quan sát các biến trạng thái dựa trên thông tin nhận được từ các phép đo đầu "
        "vào và đầu ra được gọi là bộ quan sát trạng thái. Hình 98.6 cho sơ đồ khối của một hệ như "
        "vậy."))
    b.append(fig(6, F.fig(6)))
    b.append(p(
        "Giả sử đã chọn được một hệ số khuếch đại phản hồi trạng thái K sao cho các trị riêng của"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)", "98.54"))
    b.append(eq("u(k) = −K(k)x(k) + r(k)", "98.55"))
    b.append(p(
        "nằm tại λ<sub>1</sub>, λ<sub>2</sub>, … λ<sub>n</sub>. Hơn nữa, giả sử hệ số khuếch đại G "
        "trong bộ quan sát đồng nhất"))
    b.append(eq("x̂(k+1) = (A − GC)x̂(k) + Bu(k) + Gy(k)", "98.56"))
    b.append(p(
        "được chọn sao cho các trị riêng của bộ quan sát là μ<sub>1</sub>, μ<sub>2</sub>, … "
        "μ<sub>n</sub>."))
    b.append(p(
        "Khi dùng ước lượng trạng thái của bộ quan sát x̂(k) thay cho trạng thái x(k), hệ thu được có "
        "số chiều trạng thái 2n, được mô hình hoá bởi"))
    b.append(eq(mtx([["x(k+1)"], ["x̂(k+1)"]]) + " = "
                + mtx([["A", "−BK"], ["GC", "A − GC − BK"]])
                + mtx([["x(k)"], ["x̂(k)"]]) + " + "
                + mtx([["B"], ["B"]]) + " r(k)", "98.57"))
    b.append(p("Một phép biến đổi đồng dạng"))
    b.append(eq(mtx([["x(k)"], ["e(k)"]]) + " = P"
                + mtx([["x(k)"], ["x̂(k)"]]), "98.58"))
    b.append(p("trong đó"))
    b.append(eq("P = " + mtx([["I", "0"], ["I", "−I"]]), "98.59"))
    b.append(p(
        "tương ứng với việc đổi biến sang x(k) và e(k) = x(k) − x̂(k), biến đổi hệ thành"))
    b.append(eq(mtx([["x(k+1)"], ["e(k+1)"]]) + " = "
                + mtx([["A − BK", "BK"], ["0", "A − GC"]])
                + mtx([["x(k)"], ["e(k)"]]) + " + "
                + mtx([["B"], ["0"]]) + " r(k)", "98.60"))
    b.append(p(
        "Hệ này có cùng các trị riêng như hệ ban đầu nhờ bản chất của các phép biến đổi đồng dạng, và "
        "các trị riêng là nghiệm của"))
    b.append(eq("det(λI − (A − BK))(λI − (A − GC)) = 0", "98.61"))
    b.append(p("Điều này đòi hỏi một trong hai điều sau phải đúng"))
    b.append(eq("det(λI − (A − BK)) = 0", "98.62"))
    b.append(eq("det(λI − (A − GC)) = 0", "98.63"))
    b.append(p(
        "Đó cũng chính là các trị riêng của thiết kế bộ điều khiển trạng thái phản hồi đặt cực "
        "λ<sub>1</sub>, λ<sub>2</sub>, … λ<sub>n</sub> và của thiết kế bộ quan sát trạng thái "
        "μ<sub>1</sub>, μ<sub>2</sub>, … μ<sub>n</sub>, tương ứng. Điều đó cho thấy việc dùng bộ "
        "quan sát không làm dịch chuyển các cực đã được thiết kế bởi thuật toán đặt cực."))
    b.append(p(
        "Các thuật toán cho bộ quan sát đặt cực đã được biết rõ và là một phần của nhiều bộ phần mềm "
        "thiết kế điều khiển. Các hệ số khuếch đại Kalman dừng và các hệ số khuếch đại điều khiển "
        "tối ưu cũng thường có sẵn trong những chương trình như vậy. Mã cho bộ lọc Kalman và bộ điều "
        "khiển LQ cũng dễ viết."))
    b.append(p(
        "<b>Ghi chú:</b> để đọc thêm về chủ đề này, xin xem các nguồn trong phần tài liệu tham khảo."))

    # ---------------------------------------------------------------- terms
    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(dt("Phép biến phân (<i>calculus variations</i>)",
                "kỹ thuật có thể dùng để giải các bài toán tối ưu tuyến tính hoặc phi tuyến có điều "
                "kiện biên."))
    b.append(dt("Tính điều khiển được (<i>controllability</i>)",
                "tính chất của một hệ điều khiển sao cho một đầu vào xác định đưa mọi biến trạng thái "
                "từ một trạng thái đầu mong muốn tới một trạng thái cuối mong muốn."))
    b.append(dt("Bộ điều khiển (<i>controller</i>)",
                "phân hệ giúp đạt được đầu ra mong muốn của một đối tượng hay một quá trình."))
    b.append(dt("Hàm chi phí (<i>cost function</i>)",
                "hàm mà giá trị của nó cho biết hiệu năng thực tế của hệ khớp với hiệu năng mong muốn "
                "đến mức nào."))
    b.append(dt("Đồng vectơ (<i>covector</i>)", "nhân tử Lagrange."))
    b.append(dt("Leo dốc (<i>hill climbing</i>)",
                "phương pháp xác định cực đại hoặc cực tiểu tuyệt đối bằng cách dùng một điểm đoán "
                "ban đầu và các đạo hàm của hàm."))
    b.append(dt("Bộ lọc Kalman (<i>Kalman filter</i>)",
                "một thủ tục cung cấp các ước lượng tối ưu của trạng thái."))
    b.append(dt("Nhân tử Lagrange (<i>Lagrange multiplier</i>)",
                "biểu thức toán học hiệu chỉnh chỉ tiêu chất lượng để cho nghiệm tối ưu."))
    b.append(dt("Phương trình tuyến tính bậc hai (<i>linear quadratic equation</i>)",
                "các hàm chi phí ở dạng bậc hai."))
    b.append(dt("Hệ tuyến tính (<i>linear system</i>)",
                "hệ có tính chất chồng chất."))
    b.append(dt("Điều khiển tối ưu (<i>optimal control</i>)",
                "kỹ thuật điều khiển làm cực đại hoặc cực tiểu hàm chi phí của một hệ."))
    b.append(dt("Tối ưu hoá (<i>optimization</i>)",
                "thủ tục thu được hiệu năng lớn nhất hoặc nhỏ nhất."))
    b.append(dt("Chỉ tiêu chất lượng (<i>performance index</i>)", "hàm chi phí."))
    b.append(dt("Phương pháp đặt cực (<i>pole-placement method</i>)",
                "kỹ thuật thiết kế dùng các tính chất vòng kín của hệ."))
    b.append(dt("Phương trình Riccati (<i>Riccati equation</i>)",
                "một tập phương trình biến đổi các phương trình điều khiển để dẫn tới nghiệm tối ưu."))
    b.append(dt("Phương trình trạng thái (<i>state equation</i>)",
                "một tập phương trình vi phân cấp một đồng thời với n biến, dẫn tới nghiệm của các "
                "biến trạng thái."))
    b.append(dt("Mô hình không gian trạng thái (<i>state-space model</i>)",
                "biểu thức toán học của một hệ, gồm các phương trình vi phân cấp một đồng thời và một "
                "phương trình đầu ra."))
    b.append(dt("Các biến trạng thái (<i>state variables</i>)",
                "một tập biến của hệ độc lập tuyến tính sao cho khi đã đặt giá trị thì có thể xác định "
                "được giá trị của mọi biến của hệ về sau."))

    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "Bốn lỗi ấn loát của bản gốc đã được sửa ở đây. (1) Khối phản hồi trên Hình 98.4 in nhầm "
        "chữ <b>G</b> trong khi chú thích hình và phần thân bài đều gọi nó là hệ số khuếch đại "
        "K(k); hình vẽ lại ở đây ghi K(k). (2) Các phương trình 98.7 và 98.12 trùng nội dung trong "
        "bản gốc; cả hai được giữ nguyên như đã in. (3) Ký hiệu dấu hoa thị (*) trong các phương "
        "trình 98.23 đến 98.44 là phép chuyển vị ma trận, không phải phép nhân liên hợp. (4) Các "
        "phương trình 98.17 và 98.19 bị lỗi font trong bản in; chúng được trình bày lại theo dạng "
        "chuẩn của phép biến phân."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "P. Whittle, <i>Optimal Control — Basics and Beyond</i>, John Wiley &amp; Sons, New York, 1996.",
        "F. L. Lewis and V. L. Syrmos, <i>Optimal Control</i>, 2nd ed., John Wiley &amp; Sons, "
        "New York, 1995.",
        "K. Ogata, <i>Discrete-Time Control Systems</i>, Prentice-Hall, Englewood Cliffs, NJ, 1987.",
        "B. C. Kuo, <i>Digital Control Systems</i>, 2nd ed., Harcourt Brace Jovanovich, New York, 1992.",
    ]))

    b.append(h2("Danh sách nhà sản xuất", "List of Manufacturers"))
    b.append(p(
        "Không có nhà sản xuất nào chế tạo bộ điều khiển tối ưu. Hầu hết các bộ phần mềm toán học, "
        "chẳng hạn <b>MATLAB Optimization Toolbox</b>, các thuật toán CAD/CAM, phần lớn các công cụ "
        "phần mềm trí tuệ nhân tạo và mạng nơ-ron, cùng các bộ phần mềm mô phỏng và thiết kế khác, "
        "đều cung cấp lời giải cho các bài toán điều khiển tối ưu. Các công cụ tối ưu hoá cũng là "
        "một phần của những bộ phần mềm thiết kế chuyên dụng cho từng ứng dụng cụ thể, chẳng hạn "
        "FPGA — một ngôn ngữ thiết kế hướng tối ưu hoá theo công nghệ; OPTCON — các thuật toán điều "
        "khiển tối ưu cho mô hình ngẫu nhiên tuyến tính; DISNEL; MIMO; v.v."))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []

    b.append(h2("98.1 Introduction"))
    b.append(p(
        "Optimal control maximizes (or minimizes) the value of a function chosen as the performance "
        "index or cost function of an operational control system. Optimal control theory, on the other "
        "hand, is the mathematics of finding parameters that cause the performance index to take an "
        "extreme value subject to system constraints."))
    b.append(p(
        "Optimal control is applied in many disciplines: satellites and aerospace, aircraft and "
        "spacecraft, chemical engineering, communications engineering, robots and robotics, power "
        "systems, electric drives, computers and computer systems, and so on. In many applications "
        "simple interconnections of control devices and controllers do not provide the most economic "
        "operation, and optimal control offers the solution. Optimization is therefore useful in "
        "obtaining the best results from a known process. If the process is operating under "
        "steady-state conditions, optimization considers the process stationary and is concerned only "
        "with the operating points. When the process is stationary, the resulting optimum operating "
        "point can easily be maintained by setting the predetermined set points and precalculated "
        "control parameters. If the process changes from time to time, however, new optimum set points "
        "must be determined for each change."))
    b.append(p(
        "The performance of a system is optimized for many reasons: improving quality, increasing "
        "production, decreasing waste, obtaining greater efficiency, maximizing safety, saving time and "
        "energy, and so on. In many optimization problems boundary conditions are imposed by the system "
        "itself for safety in operation, for the availability of minimum and maximum power, for "
        "limitations in storage capacity, for the capability of the operating machinery, for "
        "temperature, speed, force, acceleration — indeed, for any other hard physical reason."))
    b.append(p(
        "Many different methods may be used to solve optimal control problems, depending on the nature "
        "of the problem. If the performance index and constraints can be formulated as linear algebraic "
        "functions of the controlled variables, linear programming may be the best route, and simplex "
        "methods provide a good way of solving the linear programming problem. If the equations "
        "describing the system are nonlinear, the solution may involve nonlinear techniques or the "
        "linearization of the problem over subregions. If the problem is to determine the largest value "
        "of a function of two or more variables, the steepest ascent (or descent) method — sometimes "
        "called hill climbing or the gradient method — may be used."))
    b.append(p(
        "Hill-climbing methods are still popular and easy to understand. They are discussed briefly "
        "here, first, to lay a good foundation for a sound understanding of optimal control theory."))
    b.append(p(
        "Figure 98.1 illustrates the hill-climbing technique in the region of the absolute minimum. The "
        "figure also shows a common pitfall in control theory: the local maxima and minima. As can be "
        "seen, the sign of the first derivative of the function changes as the derivative passes "
        "through the maximum point. The method commonly uses an initial estimated point at which the "
        "first derivative is considered (guessed) to be zero. That point is then used, in the direction "
        "of steepest ascent or descent as the case may be, to reach the next point, and so on until the "
        "absolute maximum or minimum is found without being trapped in a local extreme point. There are "
        "many different ways of finding maxima or minima by hill climbing, and Figure 98.2 illustrates "
        "some examples of implementation."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Apart from hill-climbing techniques, many new methods are available for modern optimal control "
        "problems involving hyperspaces (many variables) that are complex in nature and have stringent "
        "constraints. If a good mathematical model of the system is available, optimization methods may "
        "be used to find the optimum conditions on the model instead of seeking optimization on the "
        "actual process. The availability of the model thus determines the type of optimization method "
        "employed."))

    b.append(h2("98.2 Cost Function"))
    b.append(p(
        "In designing optimal control systems, rules may be set for determining the control decisions, "
        "subject to certain constraints, such that some measure of deviation from an ideal case is "
        "minimized. That measure is usually provided by a selected performance index or cost function. "
        "The performance index is a function whose value indicates how well the actual performance of "
        "the system matches the desired performance. Appropriate selection of the performance index is "
        "important, since it determines the nature and complexity of the problem: whether the optimal "
        "control is linear or nonlinear, stationary or time-varying, depends on the selected performance "
        "index. The choice depends on system specifications, physical realizability, and the "
        "restrictions on the controls to be used. In general, choosing an appropriate performance index "
        "involves a compromise between a meaningful evaluation of system performance and the "
        "availability of feasible mathematical descriptions."))
    b.append(p(
        "The performance index is selected by the engineer to make the system behave in a desired "
        "fashion. By definition, a system whose design minimizes the selected performance index is "
        "optimal. It is important to point out that a system optimal for one performance index may not "
        "be optimal under another. In practical systems, because of possible complexity and cost of "
        "implementation, it may be better to employ approximate optimal control laws that are not "
        "rigidly tied to a single performance index."))
    b.append(p(
        "Before starting the optimization of any system it is necessary to formulate the system, having "
        "information on system parameters and describing equations, constraints, the class of allowable "
        "control vectors, and the selected performance indexes. The solution can then proceed by "
        "determining the optimal control vector u(k) within the class of allowable vectors. The control "
        "vector u(k) depends on such factors as the nature of the performance index, the constraints, "
        "the initial values of state and output, and the desired state as well as the desired outputs. "
        "If analytical solutions are impossible or too complicated, alternative computational solutions "
        "may be employed."))
    b.append(p(
        "In simple cases the errors between the desired and actual responses can be chosen as the "
        "performance index to be minimized. Figure 98.3 depicts different descriptions of the error "
        "between actual and desired responses. The aim is to keep the errors as small as possible. The "
        "time integral of the error gives the severity of the error; however, since positive and "
        "negative errors cancel each other mathematically, absolute values must be used:"))
    b.append(eq("IAE = ∫<sub>0</sub><sup>T</sup> |e(t)| dt", "98.1"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "In many cases it is better to use integral squared errors, which take large errors into account "
        "rather than ordinary ones:"))
    b.append(eq("ISE = ∫<sub>0</sub><sup>T</sup> e<sup>2</sup>(t) dt", "98.2"))
    b.append(p(
        "Time-dependent functions can be used to capture errors occurring late in time rather than "
        "ordinary transients:"))
    b.append(eq("ITAE = ∫<sub>0</sub><sup>T</sup> t|e(t)| dt", "98.3"))
    b.append(p("and"))
    b.append(eq("ITSE = ∫<sub>0</sub><sup>T</sup> t e<sup>2</sup>(t) dt", "98.4"))
    b.append(p(
        "Mean square error, MSE, is also commonly used, since a slight modification leads to the "
        "inclusion of statistical techniques and the analysis of random noise:"))
    b.append(eq("MSE = lim<sub>T→∞</sub> (1/T) ∫<sub>0</sub><sup>T</sup> e<sup>2</sup>(t) dt", "98.5"))
    b.append(p(
        "Modern optimal control theory is developed within the state-space framework, and its "
        "performance indexes are more complex and comprehensive, as explained below."))
    b.append(p(
        "Suppose the control command of a system is expressed in vectorial form as u and the state of "
        "the system is described by x (the Oxford English Dictionary defines <i>state</i> as condition "
        "with respect to circumstances, attributes, structure, form, phase or the like). Further "
        "suppose that the rate of change of state is a function of state x, control command u and time "
        "t:"))
    b.append(eq("ẋ = f(x, u, t)&nbsp;&nbsp;&nbsp; x(0) = x<sub>0</sub> known", "98.6"))
    b.append(p(
        "A control law u(x, t), or a control history u(t), is then determined such that a performance "
        "index — a scalar functional —"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> g(x(t), u(t), t) dt", "98.7"))
    b.append(p(
        "takes a minimum value out of all other possibilities while still satisfying Eq. 98.6. A "
        "boundary relationship x(T) = x<sub>f</sub> must also be met as a constraint."))
    b.append(p("A most common form of J(u) is minimum-time control, in which"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> dt = T", "98.8"))
    b.append(p(
        "Many other criteria are used as well, such as minimum fuel, minimum energy and other "
        "quadratic forms:"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> u(t) dt", "98.9"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> u<sup>2</sup>(t) dt", "98.10"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> [q x<sup>2</sup>(t) + r u<sup>2</sup>(t)] dt", "98.11"))
    b.append(p(
        "A general term for the continuous-time performance index that leads to optimal control is "
        "expressed as:"))
    b.append(eq("J(u) = ∫<sub>0</sub><sup>T</sup> g[x(t), u(t), t] dt", "98.12"))
    b.append(p(
        "This performance index is minimized subject to the constraints above, together with x(t) being "
        "an admissible state, x(t) ∈ X(t), ∀t ∈ (t<sub>0</sub>, t<sub>f</sub>)."))
    b.append(p(
        "Slight variations of Eqs. 98.9 to 98.12 lead to the mathematics of the discrete-time, or "
        "digital, versions of optimal control."))

    b.append(h2("98.3 Calculus of Variations"))
    b.append(p(
        "The calculus of variations is suitable for solving linear or nonlinear optimization problems "
        "with linear or nonlinear boundary conditions. Basically it is a collection of many different "
        "analytical methods, discussed differently from book to book. A typical approach, which leads "
        "to the more general and widely used modern theories, is introduced here."))
    b.append(p("Consider a dynamic system operating in the time interval t<sub>0</sub> &lt; t &lt; "
               "t<sub>f</sub>"))
    b.append(eq("ẋ(t) = f(x(t), u(t), t)&nbsp;&nbsp;&nbsp; for t ∈ (t<sub>0</sub>, t<sub>f</sub>)",
                "98.13"))
    b.append(p("where the initial state x<sub>0</sub> is given."))
    b.append(p(
        "The system has n state variables and m control variables. The scalar function to be optimized "
        "is"))
    b.append(eq("J = k[x(t<sub>f</sub>)] + ∫ L[x, u, t] dt", "98.14"))
    b.append(p("Define a scalar, for instance the Hamiltonian:"))
    b.append(eq("H = H[x, u, λ, t] = L[x, u, t] + Σ<sub>i</sub> λ<sub>i</sub> f<sub>i</sub>", "98.15"))
    b.append(p("λ is known as the Lagrange multiplier. Also define a modified objective function:"))
    b.append(eq("J = k[x(t<sub>1</sub>)] + ∫ H dt", "98.16"))
    b.append(p("The resulting solution is optimal when"))
    b.append(eq("λ̇ = −∂H/∂x = −∂L/∂x − Σ<sub>i</sub> λ<sub>i</sub> ∂f<sub>i</sub>/∂x", "98.17"))
    b.append(eq("λ(t<sub>f</sub>) = ∂k/∂x", "98.18"))
    b.append(eq("∂H/∂u = ∂L/∂u + Σ<sub>i</sub> λ<sub>i</sub> ∂f<sub>i</sub>/∂u = 0,"
                "&nbsp;&nbsp; t<sub>0</sub> &lt; t &lt; t<sub>f</sub>", "98.19"))
    b.append(p(
        "The solutions of Eqs. 98.17 and 98.19 in the above form are difficult to obtain. Nevertheless, "
        "more general theories can be developed from these ideas, such as Pontryagin's maximum "
        "principle."))
    b.append(p(
        "An advance over the calculus of variations is Pontryagin's maximum principle, which offers "
        "easier solutions and extends the range of applicability to bounded control problems. In its "
        "simplest form the principle may be explained as follows."))
    b.append(p("Given the system"))
    b.append(eq("ẋ<sub>i</sub> = f<sub>i</sub>[x, u, t]", "98.20"))
    b.append(p("and an objective function"))
    b.append(eq("J = Σ<sub>i</sub> k<sub>i</sub> x<sub>i</sub>(t<sub>f</sub>)", "98.21"))
    b.append(p(
        "The maximum principle states that if the control vector u is optimum, then the Hamiltonian"))
    b.append(eq("H = Σ<sub>i</sub> p<sub>i</sub> f<sub>i</sub>", "98.21a"))
    b.append(p("is also maximized with respect to the control vector u over the given intervals."))
    b.append(eq("ṗ<sub>i</sub> = −Σ<sub>j</sub> (∂f<sub>j</sub>/∂x<sub>i</sub>) p<sub>j</sub>",
                "98.21b"))
    b.append(eq("p<sub>i</sub>(t<sub>f</sub>) = k<sub>i</sub>", "98.21c"))
    b.append(p("where p is the adjoint or co-state vector, and"))
    b.append(eq("ẋ<sub>i</sub> = ∂H/∂p<sub>i</sub> = f<sub>i</sub>[x, u, t]", "98.21d"))
    b.append(eq("∂H/∂x<sub>i</sub> = −ṗ<sub>i</sub>", "98.21e"))
    b.append(p(
        "The initial values of the state vector x provide the remaining constants needed to solve these "
        "equations and determine an optimum control vector. The method also applies to systems with "
        "complex performance indexes."))
    b.append(p(
        "Another extension of the calculus of variations is the Kalman filter. Kalman is essentially a "
        "general filtering technique that can be applied to problems such as optimal estimation, "
        "prediction, noise filtering, stochastic optimal control and the design of optimal controllers. "
        "The method has the advantage of providing estimates of variables in the presence of noise for "
        "both stationary and nonstationary processes. Most other types of noise can be treated by this "
        "method if they can be translated into Gaussian form. The technique can also be employed in "
        "systems with forcing disturbances and more than one noise source. In general, systems with "
        "quadratic objective functions or with uncorrelated Gaussian noise at the input are suitable for "
        "this technique."))
    b.append(p(
        "One way of applying the Kalman filter to a nonlinear system is to find a good estimate of the "
        "system and use it to define a new set of linear state equations that approximates the system in "
        "linear form at a normal operating point. The filter can then be applied to the new set of "
        "linear equations."))
    b.append(p(
        "Applications of the Kalman filter in instrumentation and measurement systems, and in other "
        "optimal control problems, are endless. It is easily programmed on digital computers."))

    b.append(h2("98.4 Riccati Equation"))
    b.append(p(
        "Some models in optimization problems resemble the models of traditional control theory and "
        "practice. In these models the process and control variables are vector-valued and constrained "
        "by linear plant equations, and the cost functions take the form of quadratic costs. Such "
        "systems are termed linear quadratic, or LQ, systems. The theory and models of LQ systems are "
        "well developed in both the deterministic and the stochastic case."))
    b.append(p("Express a quadratic optimal control problem as"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)&nbsp;&nbsp;&nbsp; x(0) = x<sub>0</sub>", "98.22"))
    b.append(p("where"))
    b.append(p(
        "x(k) = state vector (n-vector)<br>"
        "u(k) = control vector (r-vector)<br>"
        "A = n × n nonsingular matrix<br>"
        "B = n × r matrix"))
    b.append(p(
        "The aim is to find the optimal control sequence u(0), u(1), …, u(N − 1) that minimizes the "
        "quadratic performance index"))
    b.append(eq("J = ½x*(N)Sx(N) + ½ Σ<sub>k=0</sub><sup>N−1</sup> [x*(k)Qx(k) + u*(k)Ru(k)]",
                "98.23"))
    b.append(p("where x* and u* are the transposes of the x and u matrices respectively, and"))
    b.append(p(
        "Q = n × n positive definite or positive semidefinite symmetric matrix<br>"
        "R = r × r positive definite or positive semidefinite symmetric matrix<br>"
        "S = n × n positive definite or positive semidefinite symmetric matrix"))
    b.append(p(
        "The matrices Q, S and R are selected to weight the relative importance of the performance "
        "measures caused by the state vectors x(k), the final state x(N) and the control vectors u(k) "
        "respectively, for k = 0, 1, 2, …, N − 1. The initial state of the system is arbitrary, but the "
        "final state x(N) may be fixed. If the final state is fixed, the term ½x*(N)Sx(N) may be "
        "removed from the performance index and the terminal state x<sub>f</sub> imposed. If the final "
        "state is not fixed, the term ½x*(N)Sx(N) represents the weight of the performance measure on "
        "the final state."))
    b.append(p(
        "There are many different ways of solving the above equations, one of which makes use of "
        "Lagrange multipliers. With their aid the performance index may be modified as"))
    b.append(eq("L = ½x*(N)Sx(N) + Σ<sub>k</sub> {½x*(k)Qx(k) + ½u*(k)Ru(k) "
                "+ λ*(k+1)[Ax(k) + Bu(k) − x(k+1)]}", "98.24"))
    b.append(p(
        "It is known that minimization of the function L is equivalent to minimization of the "
        "performance index J under the same constraints."))
    b.append(p(
        "In order to minimize, L must be differentiated with respect to the vectors x(k), u(k) and λ(k), "
        "and the results set to zero. Partial differentiation of L with respect to the variables gives"))
    b.append(eq("∂L/∂x(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Qx(k) + A*λ(k+1) − λ(k) = 0", "98.25"))
    b.append(eq("∂L/∂x(N) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Sx(N) − λ(N) = 0", "98.26"))
    b.append(eq("∂L/∂u(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Ru(k) − B*λ(k+1) = 0", "98.27"))
    b.append(p("and"))
    b.append(eq("∂L/∂λ(k) = 0&nbsp;&nbsp; → &nbsp;&nbsp;Ax(k−1) + Bu(k−1) − x(k) = 0", "98.28"))
    b.append(p(
        "A close inspection of the formulae above shows that the last equation is simply the state "
        "equation for k = 1, 2, 3, … N, and that the value of the Lagrange multiplier can be determined "
        "from Eq. 98.26. The Lagrange multiplier is often termed the covector or the adjoint vector."))
    b.append(p("Rewriting Eqs. 98.25 and 98.27,"))
    b.append(eq("λ(k) = Qx(k) + A*λ(k+1)", "98.29"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*λ(k+1)", "98.30"))
    b.append(p("the state Eq. 98.22 can be expressed as"))
    b.append(eq("x(k+1) = Ax(k) − BR<sup>−1</sup>B*λ(k+1)", "98.31"))
    b.append(p(
        "To obtain the solution of the minimization problem, Eqs. 98.29 and 98.31 must be solved "
        "simultaneously as a two-point boundary-value problem. The solutions of these two equations in "
        "this form, together with the optimal values of the state vector and the Lagrange multiplier "
        "vector, lead to the values of the control vector u(k) that optimize the open-loop control "
        "system. For closed-loop control systems, however, the Riccati transformations must be applied."))
    b.append(eq("u(k) = −K(k)x(k)", "98.32"))
    b.append(p(
        "where K(k) is the r × n feedback matrix. The Riccati equation in feedback form can now be "
        "obtained by assuming that λ(k) is written as"))
    b.append(eq("λ(k) = P(k)x(k)", "98.33"))
    b.append(p("where P(k) is an n × n matrix. Substituting Eq. 98.33 into 98.29 and 98.31 gives"))
    b.append(eq("P(k)x(k) = Qx(k) + A*P(k+1)x(k+1)", "98.34"))
    b.append(eq("x(k+1) = Ax(k) − BR<sup>−1</sup>B*P(k+1)x(k+1)", "98.35"))
    b.append(p(
        "In writing Eqs. 98.34 and 98.35 the Lagrange multiplier λ(k) has been eliminated. This is an "
        "important step in solving two-point boundary-value problems. By further manipulation it is "
        "possible to show that"))
    b.append(eq("P(k) = Q + A*P(k+1)A − A*P(k+1)B[R + B*P(k+1)B]<sup>−1</sup>B*P(k+1)A", "98.36"))
    b.append(p("Equation 98.36 is known as the Riccati equation."))
    b.append(p("From Eqs. 98.26 and 98.33, writing λ(N) = Sx(N) = P(N)x(N) gives"))
    b.append(eq("P(N) = S", "98.37"))
    b.append(p(
        "Hence the Riccati equation can be solved backward from k = N to k = 0, starting from the known "
        "values of P(N)."))
    b.append(p(
        "The optimal control vector u(k) can now be calculated from Eqs. 98.29, 98.30 and 98.35:"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*λ(k+1) = −R<sup>−1</sup>B*(A*)<sup>−1</sup>[P(k) − Q]x(k) "
                "= −K(k)x(k)", "98.38"))
    b.append(p("where"))
    b.append(eq("K(k) = −R<sup>−1</sup>B*(A*)<sup>−1</sup>[P(k) − Q]", "98.39"))
    b.append(p(
        "It is worth noting that the optimal control vector may be obtained in slightly different forms "
        "by different manipulations of the above equations, such as"))
    b.append(eq("u(k) = −R<sup>−1</sup>B*[P<sup>−1</sup>(k+1) + BR<sup>−1</sup>B*]<sup>−1</sup>Ax(k)",
                "98.40"))
    b.append(p(
        "Equations 98.38 and 98.39 indicate that the optimal control law requires feedback of the state "
        "vector with time-varying gain K(k). Figure 98.4 illustrates the optimal control scheme of a "
        "system based on the quadratic performance index. In practical applications the time-varying "
        "K(k) is calculated before the process begins. Once the state matrix A, control matrix B and "
        "weighting matrices Q, R and S are known, the gain K(k) may be precomputed off-line for later "
        "use. The control vector u(k) at each stage can be determined immediately by premultiplying the "
        "state vector x(k) by the known gain K(k)."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "From the above equations the minimum value of the performance index can also be calculated. "
        "Using the initial values"))
    b.append(eq("J<sub>min</sub> = ½x*(0)P(0)x(0)", "98.41"))
    b.append(p(
        "The steady-state solutions of the Riccati equations are necessary when dealing with "
        "time-invariant (steady-state) optimal controls. There are many ways of obtaining steady-state "
        "Riccati solutions; an example is given below."))
    b.append(eq("P = Q + A*PA − A*PB(R + B*PB)<sup>−1</sup>B*PA", "98.42"))
    b.append(p("The steady-state value of K may be found as"))
    b.append(eq("K = (R + B*PB)<sup>−1</sup>B*PA", "98.43"))
    b.append(p("and the optimal control law for steady-state operation may be expressed as"))
    b.append(eq("u(k) = −(R + B*PB)<sup>−1</sup>B*PA x(k)", "98.44"))
    b.append(p(
        "This section has been presented for discrete-time optimal control systems rather than "
        "continuous systems, because computers and microprocessors have recently come into widespread "
        "use as on-line and off-line control tools. Since the principles are the same, the solutions "
        "can easily be extended to continuous-time systems with minor modifications."))

    b.append(h2("98.5 State Feedback Matrix"))
    b.append(p(
        "The state feedback method is another design technique that allows the designer to locate the "
        "poles of the system wherever they are needed. This approach is termed the pole-placement "
        "method, where <i>pole</i> refers to the poles of the closed-loop transfer function as in "
        "Fig. 98.5. The method assumes that the state variables are measurable and available for "
        "feedback. If the state is available the system is said to be deterministic: it is noise free "
        "and its parameters are fully known. If the state is not available, methods such as measurement "
        "feedback laws or state estimators may be selected."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "In many applications, instead of the state variables it is more convenient to use state "
        "estimates coming from an observer or a Kalman filter. In this case three well-known methods "
        "are available: certainty equivalence, separation and dual control. Certainty equivalence has "
        "considerable advantages over the others because it leads to deterministic optimal control laws "
        "such as Pontryagin's principle, or to the conditional mean of the state such as the Kalman "
        "filter. It leads to a practical controller, which may be built as a filter and an optimal law "
        "in cascade."))
    b.append(p(
        "State feedback controllers are relatively easy to implement. For example, in the "
        "pole-placement method the relationship of the feedback control u to the state x for linear "
        "systems is"))
    b.append(eq("u(k) = −Kx(k)", "98.45"))
    b.append(p("In linear quadratic cases the gain K is time varying:"))
    b.append(eq("u(k) = −K(k)x(k)", "98.46"))
    b.append(p("where K is the n × r feedback matrix. This is correct in at least two cases."))
    b.append(p(
        "1. In linear systems with no noise, pole-placement controllers and an observer as the state "
        "estimator, the control algorithms for"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)<br>y(k) = Cx(k)"))
    b.append(p("are"))
    b.append(eq("x̂(k+1) = (A − GC)x̂(k) + Gy(k) + Bu(k)", "98.47"))
    b.append(eq("u(k) = Kx̂(k)", "98.48"))
    b.append(p(
        "where the eigenvalues of (A − GC) and (A + BK) are chosen to meet the design specifications."))
    b.append(p(
        "2. In linear systems influenced by Gaussian white noise, in which the control is optimal "
        "according to a quadratic criterion, the system"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k) + Gv(k)", "98.49"))
    b.append(eq("y(k) = Cx(k) + w(k)", "98.50"))
    b.append(p("has a control law of the form"))
    b.append(eq("x̂(k+1|k) = Ax̂(k) + Bû(k)", "98.51"))
    b.append(eq("x̂(k+1) = Ax̂(k+1|k) + G(k+1)[y(k+1) − Cx̂(k+1|k)]", "98.52"))
    b.append(eq("û(k) = K(k)x̂(k)", "98.53"))
    b.append(p(
        "where K(k) and G(k) are the optimal gains for the deterministic optimal controls and the Kalman "
        "filters respectively."))
    b.append(p(
        "In practice not all the state variables are easily accessible, and in general only the outputs "
        "of the system are measurable. Therefore, when feedback from the state variables is required in "
        "a given design, the states must be observed from information contained in the output as well "
        "as in the input variables. The subsystem that performs this observation of the state variables "
        "from the measurements of inputs and outputs is called the state observer. Figure 98.6 shows the "
        "block diagram of such a system."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p("Suppose a state feedback gain K has been selected so that the eigenvalues of"))
    b.append(eq("x(k+1) = Ax(k) + Bu(k)", "98.54"))
    b.append(eq("u(k) = −K(k)x(k) + r(k)", "98.55"))
    b.append(p(
        "are located at λ<sub>1</sub>, λ<sub>2</sub>, … λ<sub>n</sub>. Furthermore, assume that the "
        "gain G in the identity observer"))
    b.append(eq("x̂(k+1) = (A − GC)x̂(k) + Bu(k) + Gy(k)", "98.56"))
    b.append(p(
        "is chosen such that the eigenvalues of the observer are μ<sub>1</sub>, μ<sub>2</sub>, … "
        "μ<sub>n</sub>."))
    b.append(p(
        "When the observer state estimate x̂(k) is used instead of the state x(k), the resulting system "
        "has state dimension 2n, modelled by"))
    b.append(eq(mtx([["x(k+1)"], ["x̂(k+1)"]]) + " = "
                + mtx([["A", "−BK"], ["GC", "A − GC − BK"]])
                + mtx([["x(k)"], ["x̂(k)"]]) + " + "
                + mtx([["B"], ["B"]]) + " r(k)", "98.57"))
    b.append(p("A similarity transform"))
    b.append(eq(mtx([["x(k)"], ["e(k)"]]) + " = P"
                + mtx([["x(k)"], ["x̂(k)"]]), "98.58"))
    b.append(p("where"))
    b.append(eq("P = " + mtx([["I", "0"], ["I", "−I"]]), "98.59"))
    b.append(p(
        "corresponds to a change of variables to x(k) and e(k) = x(k) − x̂(k), and converts the system "
        "to"))
    b.append(eq(mtx([["x(k+1)"], ["e(k+1)"]]) + " = "
                + mtx([["A − BK", "BK"], ["0", "A − GC"]])
                + mtx([["x(k)"], ["e(k)"]]) + " + "
                + mtx([["B"], ["0"]]) + " r(k)", "98.60"))
    b.append(p(
        "This system has the same eigenvalues as the original because of the nature of the similarity "
        "transforms, and the eigenvalues are the solution of"))
    b.append(eq("det(λI − (A − BK))(λI − (A − GC)) = 0", "98.61"))
    b.append(p("This requires that one of"))
    b.append(eq("det(λI − (A − BK)) = 0", "98.62"))
    b.append(eq("det(λI − (A − GC)) = 0", "98.63"))
    b.append(p(
        "must hold. These are also the eigenvalues of the pole-placement feedback state controller "
        "design, λ<sub>1</sub>, λ<sub>2</sub>, … λ<sub>n</sub>, and of the state observer design, "
        "μ<sub>1</sub>, μ<sub>2</sub>, … μ<sub>n</sub>, respectively. The use of an observer therefore "
        "does not move the poles placed by the pole-placement algorithm."))
    b.append(p(
        "The algorithms for pole-placement observers are well known and form part of many control "
        "design packages. Steady-state Kalman gains and optimal control gains are also commonly "
        "available in such programs, and code for Kalman filters and LQ controllers is easy to write."))
    b.append(p("<b>Note:</b> for further reading on the topic, refer to the sources in the references."))

    b.append(h2("Defining Terms"))
    b.append(dt("Calculus variations",
                "a technique which can be used for solving linear or nonlinear optimization problems "
                "with boundary conditions."))
    b.append(dt("Controllability",
                "property of a control system such that a determined input takes every state variable "
                "from a desired initial state to a desired final state."))
    b.append(dt("Controller", "a subsystem that assists in achieving the desired output of a plant or "
                              "process."))
    b.append(dt("Cost function",
                "a function whose value indicates how well the actual performance of the system "
                "matches the desired performance."))
    b.append(dt("Covector", "Lagrange multiplier."))
    b.append(dt("Hill climbing",
                "a method of determining absolute maxima or minima by using an initial guess point and "
                "the derivatives of the function."))
    b.append(dt("Kalman filter", "a procedure which provides optimal estimates of state."))
    b.append(dt("Lagrange multiplier",
                "a mathematical expression that modifies the performance index to give an optimal "
                "solution."))
    b.append(dt("Linear quadratic equation", "cost functions in quadratic form."))
    b.append(dt("Linear system", "a system that possesses the properties of superposition."))
    b.append(dt("Optimal control",
                "a control technique that maximizes or minimizes the cost function of a system."))
    b.append(dt("Optimization", "the procedure of obtaining maximum or minimum performance."))
    b.append(dt("Performance index", "cost function."))
    b.append(dt("Pole-placement method",
                "a design technique that makes use of the closed-loop properties of the system."))
    b.append(dt("Riccati equation",
                "a set of equations that transform control equations to lead to optimal solutions."))
    b.append(dt("State equation",
                "a set of simultaneous first-order differential equations with n variables leading to "
                "solutions of the state variables."))
    b.append(dt("State-space model",
                "a mathematical expression of a system consisting of simultaneous first-order "
                "differential equations and an output equation."))
    b.append(dt("State variables",
                "a set of linearly independent system variables such that, once their values are set, "
                "they determine the value of all system variables later in time."))

    b.append(h2("Translator's note"))
    b.append(note(
        "Four printing defects in the source have been repaired here. (1) The feedback block of "
        "Fig. 98.4 is printed with the letter <b>G</b> although both the caption and the body text call "
        "it the gain K(k); the redrawn figure labels it K(k). (2) Eqs. 98.7 and 98.12 are duplicated in "
        "the original; both are kept as printed. (3) The asterisk (*) in Eqs. 98.23 to 98.44 denotes "
        "matrix transposition, not conjugate transpose. (4) Eqs. 98.17 and 98.19 are font-corrupted in "
        "the printed page; they are set out here in the standard form of the calculus of variations."))

    b.append(h2("References"))
    b.append(refs([
        "P. Whittle, <i>Optimal Control — Basics and Beyond</i>, John Wiley &amp; Sons, New York, 1996.",
        "F. L. Lewis and V. L. Syrmos, <i>Optimal Control</i>, 2nd ed., John Wiley &amp; Sons, "
        "New York, 1995.",
        "K. Ogata, <i>Discrete-Time Control Systems</i>, Prentice-Hall, Englewood Cliffs, NJ, 1987.",
        "B. C. Kuo, <i>Digital Control Systems</i>, 2nd ed., Harcourt Brace Jovanovich, New York, 1992.",
    ]))

    b.append(h2("List of Manufacturers"))
    b.append(p(
        "There are no manufacturers of optimal controllers. Most mathematical packages, such as "
        "<b>MATLAB Optimization Toolbox</b>, CAD/CAM algorithms, the majority of artificial intelligence "
        "and neural network software tools, and other simulation and design packages, offer solutions "
        "to optimal control problems. Optimization tools are also part of specialized design packages "
        "addressing specific applications, such as FPGA — a language-based design with "
        "technology-specific optimization; OPTCON — optimal control algorithms for linear stochastic "
        "models; DISNEL; MIMO; and so on."))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 98 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 98 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 98 “Điều khiển tối ưu” của Halit Eren — hàm chi phí, các chỉ "
            "tiêu IAE/ISE/ITAE/ITSE, phép biến phân, nguyên lý cực đại Pontryagin, phương trình "
            "Riccati, ma trận phản hồi trạng thái và bộ quan sát trạng thái, với 6 hình và 68 phương "
            "trình." if vi
            else
            "Companion to Chapter 98 of the CRC Measurement Handbook — the cost function, the "
            "IAE/ISE/ITAE/ITSE indices, the calculus of variations, Pontryagin's maximum principle, the "
            "Riccati equation, the state feedback matrix and the state observer, with 6 figures and 68 "
            "equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 98' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 98' % BASE_EN)
    meta = ("Chương 98 · theo Ch98.pdf (CRC Press, 1999) · 6 hình, 68 phương trình" if vi else
            "Chapter 98 · 6 figures, 68 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 98)))
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
