# -*- coding: utf-8 -*-
"""Handbook Chapter 12 — Area Measurement (Charles B. Coulbourn, Wolfgang P. Buerner).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch12.py
"""
import os

import hb12fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch12-area-measurement"
TITLE_EN = "Area Measurement"
TITLE_VI = "Đo diện tích"
BYLINE = "Charles B. Coulbourn · Wolfgang P. Buerner · Los Angeles Scientific Instrumentation Co."
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch11-level-measurement"
PREV_VI = "ch11-level-measurement"
PREV_T_EN = "Level Measurement"
PREV_T_VI = "Đo mức"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-12-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Người ta thường phải đo diện tích của những vùng khép kín trên các bản vẽ ở dạng bản đồ. Những "
        "vùng này có thể có hình dạng đều đặn hoặc không đều đặn, và mô tả một trong các trường hợp sau:"))
    b.append('<ul class="bul">'
             '<li>Diện tích giới hạn bởi các đường bình độ trên bản đồ.</li>'
             '<li>Tiết diện của thể tích tâm trương và tâm thu của các khoang tim.</li>'
             '<li>Đất nông nghiệp hoặc đất rừng trong ảnh chụp từ trên không.</li>'
             '<li>Tiết diện ngang của đường bộ dự kiến và hiện hữu.</li>'
             '<li>Lượng vật liệu dùng trong may mặc.</li>'
             '<li>Các phép đo khoa học.</li>'
             '<li>Bể bơi.</li>'
             '<li>Lượng lớp phủ mặt đất.</li>'
             '</ul>')
    b.append(p(
        "Các dụng cụ dùng cho kiểu đo này gồm có planimeter, bộ ghép máy tính – bộ số hoá (digitizer), "
        "các bộ số hoá có sẵn khả năng đo diện tích, và các tấm trong suốt có in lưới ô vuông để đặt chồng "
        "lên bản vẽ."))

    # ---- 12.1
    b.append(h2("12.1 Nguyên lý", "Theory"))
    b.append(h3("Planimeter", "Planimeter"))
    b.append(p(
        "Planimeter là một bộ tích phân cơ học, gồm có một thanh (cánh tay theo dõi — tracer arm), một "
        "bánh xe đo có trục song song với thanh, và một cơ cấu buộc đầu kia của thanh chuyển động trên "
        "một đường dẫn cố định, như trên Hình 12.1. Đầu đối diện của thanh được trang bị một con trỏ dùng "
        "để theo dấu đường bao của một diện tích. Bánh xe đo, Hình 12.2, được chia thành 1000 vạch hay "
        "nhiều hơn trên mỗi vòng quay. Mỗi vạch tương ứng với một lần đếm. Nó tích luỹ số lần đếm P theo "
        "biểu thức:"))
    b.append(eq("P = (K / πD) &int; sin &phi; ds", "12.1"))
    b.append(p(
        "trong đó K = số lần đếm trên mỗi vòng quay của bánh xe đo, D = đường kính bánh xe đo, &phi; = góc "
        "tạo bởi trục bánh xe đo và hướng di chuyển, và s = đường đi được theo dấu."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Diện tích A được theo dấu có giá trị:"))
    b.append(eq("A = (L P &pi; D) / K", "12.2"))
    b.append(p(
        "trong đó L = chiều dài cánh tay theo dõi, P = số lần đếm tích luỹ (phương trình 12.1). Hình 12.3 "
        "cho thấy một cơ cấu cơ bản gồm bánh xe và thanh xác định diện tích của một hình bình hành. Đường "
        "đi được theo dấu là dọc theo cạnh nghiêng; tuy nhiên, bánh xe chỉ ghi nhận một đại lượng tỉ lệ "
        "với tích số giữa khoảng cách đã đi và sin của góc tạo bởi hướng di chuyển và trục bánh xe đo "
        "(phương trình 12.1). Đó chính là chiều cao của hình bình hành. Tích số giữa chiều cao (số đọc "
        "bánh xe đổi ra khoảng cách) và cạnh đáy (chiều dài thanh) chính là diện tích."))
    b.append(fig(2, F.fig(2)))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Hình 12.4(a) minh hoạ cách một planimeter hoạt động khi đo diện tích của một hình bốn cạnh. Các "
        "Hình 12.4(b), (c), (d) và (e) cho thấy vị trí đầu và cuối của thanh khi từng cạnh của hình được "
        "theo dấu. Áp dụng biểu thức tổng quát cho diện tích dưới một đường cong, A = &int; f(x) dx, cho "
        "từng phần diện tích này ta có:"))
    b.append(eq("A<sub>a</sub> = &int;<sub>x<sub>a</sub></sub><sup>x<sub>1</sub></sup> "
                "[f(x) &minus; f<sub>a</sub>(x)] dx", "12.3"))
    b.append(eq("A<sub>b</sub> = &int;<sub>x<sub>1</sub></sub><sup>x<sub>2</sub></sup> "
                "[f(x) &minus; f<sub>b</sub>(x)] dx", "12.4"))
    b.append(eq("A<sub>c</sub> = &int;<sub>x<sub>2</sub></sub><sup>x<sub>3</sub></sup> "
                "[f(x) &minus; f<sub>c</sub>(x)] dx", "12.5"))
    b.append(eq("A<sub>d</sub> = &int;<sub>x<sub>3</sub></sub><sup>x<sub>4</sub></sup> "
                "[f(x) &minus; f<sub>d</sub>(x)] dx", "12.6"))
    b.append(p(
        "trong đó A<sub>a</sub>, A<sub>b</sub>, A<sub>c</sub> và A<sub>d</sub> là bốn phần diện tích. "
        "Diện tích toàn phần của hình bằng tổng bốn phần diện tích đó. Khi gộp các số hạng của những phần "
        "diện tích này và sắp xếp lại — những số hạng xác định diện tích do đầu trái của thanh theo dấu "
        "thành một nhóm, những số hạng do đầu kia của thanh theo dấu thành nhóm thứ hai, và những số hạng "
        "còn lại thành nhóm thứ ba — ta thu được biểu thức:"))
    b.append(eq("A = A<sub>a</sub> + A<sub>b</sub> + A<sub>c</sub> + A<sub>d</sub>", "12.7"))
    b.append(p(
        "Bốn tích phân đầu mô tả diện tích do đầu trái của thanh theo dấu. Vì đầu này chạy trên một cung, "
        "nên diện tích nó bao kín bằng không. Bốn tích phân cuối mô tả diện tích do đầu phải của thanh theo "
        "dấu — chính là hình bốn cạnh. Tám tích phân còn lại triệt tiêu lẫn nhau vì &int;<sub>a</sub><sup>1</sup> "
        "+ &int;<sub>1</sub><sup>a</sup> = 0, v.v. Như vậy, diện tích toàn phần bằng diện tích do đầu phải "
        "của thanh theo dấu. Lập luận tương tự cũng áp dụng được cho những hình có bất kỳ số cạnh nào và "
        "bất kỳ hình dạng nào."))
    b.append(fig(4, F.fig(4)))

    b.append(h3("Bộ số hoá (Digitizer)", "Digitizer"))
    b.append(p(
        "Bộ số hoá chuyển đổi một vị trí vật lý trên bản đồ thành mã số biểu diễn toạ độ (x, y) của vị trí "
        "đó. Mã số thường được đổi sang định dạng ASCII hoặc nhị phân chuẩn và truyền cho máy tính, tại "
        "đó thực hiện các tính toán để xác định diện tích hay chiều dài. Một số bộ số hoá cũng có thể tính "
        "trực tiếp diện tích và chiều dài mà không cần máy tính."))
    b.append(p(
        "Diện tích A có thể tính bằng các cặp toạ độ xác định đường bao của vùng:"))
    b.append(eq("A = ½ |(x<sub>1</sub>y<sub>2</sub> &minus; x<sub>2</sub>y<sub>1</sub>) + "
                "(x<sub>2</sub>y<sub>3</sub> &minus; x<sub>3</sub>y<sub>2</sub>) + … + "
                "(x<sub>n</sub>y<sub>1</sub> &minus; x<sub>1</sub>y<sub>n</sub>)|", "12.8"))
    b.append(p(
        "trong đó x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, … = các toạ độ x đo được nối tiếp dọc theo "
        "đường bao; y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, … = các toạ độ y tương ứng. Mọi cặp toạ "
        "độ đã số hoá đều phải được dùng trong tính toán, vì các khoảng &Delta;x của dãy dữ liệu này thường "
        "không đều nhau."))
    b.append(p(
        "Trong phương trình 12.8, số hạng cuối cần được xem xét đặc biệt vì nó chứa cả cặp toạ độ đầu và "
        "cặp toạ độ cuối của dãy. Khi tính toán từ dữ liệu lưu trong máy tính, thông tin cần để tính số "
        "hạng cuối đều sẵn có nên không cần hành động gì đặc biệt. Tuy nhiên, khi tính toán bằng một vi xử "
        "lý nhúng bộ nhớ hạn chế, thông thường mỗi số hạng được tính ngay khi các toạ độ được đọc vào. "
        "Trong trường hợp này, một trong hai hành động phải được thực hiện. Thứ nhất, lưu lại cặp toạ độ "
        "đầu, và sau khi đo xong, nhấn một phím để khởi động việc tính số hạng cuối. Đó gọi là “đóng diện "
        "tích” (closing the area). Thứ hai, nếu không lưu cặp toạ độ đầu, để tránh sai số, điểm cuối cùng "
        "phải trùng với điểm đầu, tức x<sub>n</sub> = x<sub>1</sub>, y<sub>n</sub> = y<sub>1</sub>, khiến "
        "số hạng cuối bằng không."))
    b.append(p(
        "Các kiểu bộ số hoá phổ biến hiện nay là bộ bàn (tablet), bộ số hoá siêu âm (sonic) và bộ số hoá "
        "dạng cánh tay (arm). Có lẽ kiểu phổ biến nhất là bàn."))
    b.append(h3("Bộ số hoá dạng bàn (Tablet Digitizer)", "Tablet Digitizer"))
    b.append(p(
        "Bộ số hoá dạng bàn gồm một con trỏ và một mặt làm việc có các dây dẫn ngầm được bố trí thành lưới. "
        "Các dây ngang song song và cách nhau khoảng 12 mm. Các dây dọc cũng song song và cách nhau một "
        "khoảng như vậy. Người ta dùng những kỹ thuật cảm biến khác nhau để xác định vị trí con trỏ so với "
        "các dây lưới."))
    b.append(p(
        "Một kỹ thuật cảm biến dùng các dây lưới làm bằng vật liệu từ giảo — loại vật liệu có tính chất thay "
        "đổi hình dạng rất nhanh khi chịu tác dụng của từ trường. Mỗi bộ dây lưới, cả ngang và dọc, được "
        "kích thích độc lập bởi một dây phát đặt vuông góc với bộ dây đó [1]. Xung truyền trên dây phát "
        "tạo ra từ trường làm thay đổi hình dạng mỗi dây từ giảo, khiến một sóng biến dạng lan truyền dọc "
        "theo dây. Đồng thời, xung khởi động một bộ đếm. Một cuộn dây trong con trỏ cảm nhận sóng biến "
        "dạng và phát tín hiệu dừng bộ đếm. Kết quả đếm do đó tỉ lệ với thời gian lan truyền của sóng biến "
        "dạng. Tích số giữa thời gian lan truyền và vận tốc sóng biến dạng bằng khoảng cách vật lý giữa "
        "dây phát và bộ thu của con trỏ. Vận tốc sóng biến dạng đủ chậm nên mọi sai số trong đo thời gian "
        "đều có thể chấp nhận được."))
    b.append(p(
        "Kỹ thuật cảm biến thứ hai dùng một lưới gồm các dây dẫn và một con trỏ phát tín hiệu cỡ 57,6 kHz "
        "[2]. Các dây lưới dọc được cảm nhận để xác định phân bố biên độ của tín hiệu cảm ứng trong mỗi "
        "dây. Điểm có cường độ tín hiệu lớn nhất xác định vị trí con trỏ dọc theo trục ngang. Các dây lưới "
        "ngang cũng được cảm nhận tương tự để tìm điểm có cường độ lớn nhất xác định vị trí con trỏ dọc "
        "theo trục dọc. Sự ghép giữa con trỏ và lưới có thể thực hiện theo cách điện từ hoặc điện tĩnh [3]."))
    b.append(p(
        "Cũng có thể áp dụng tín hiệu lên các dây lưới và dùng con trỏ làm bộ thu. Trong trường hợp này, "
        "tín hiệu tới mỗi dây lưới phải được mã hoá, hoặc phải áp dụng tuần tự: trước hết cho một bộ dây, "
        "sau đó cho bộ dây kia. Người ta xác định biên độ tín hiệu thu được tại con trỏ dọc theo mỗi trục "
        "để định vị con trỏ."))
    b.append(h3("Bộ số hoá siêu âm (Sonic Digitizer)", "Sonic Digitizers"))
    b.append(p(
        "Bộ số hoá siêu âm gồm một con trỏ và hai hoặc nhiều micrô. Con trỏ, dùng để xác định điểm cần số "
        "hoá, thường chứa một khe tia lửa phát định kỳ một xung năng lượng siêu âm [4]. Trong một số trường "
        "hợp, các micrô được gắn trên một thanh nằm dọc theo cạnh trên của vùng bản vẽ. Ở những trường hợp "
        "khác, chúng được gắn trên một khung chữ L, nằm dọc theo cạnh trên và một cạnh bên của vùng bản vẽ. "
        "Các micrô thu xung siêu âm do con trỏ phát ra. Người ta đo thời gian xung đi từ bộ phát tới mỗi "
        "bộ thu, và tính khoảng cách xiên (slant distance) từ tích số giữa thời gian trễ đó và vận tốc âm. "
        "Toạ độ x và y của con trỏ được tính từ các tầm xiên và vị trí các micrô."))
    b.append(p(
        "Có những điểm không xác định (ambiguity) vì một tập hợp tầm xiên chỉ mô tả hai điểm; tuy nhiên, "
        "điểm không xác định có thể được giải quyết bằng cách dùng thêm micrô, hoặc bằng cách bảo đảm các "
        "điểm không xác định nằm ngoài vùng làm việc. Với các micrô thẳng hàng dọc theo cạnh trên của vùng "
        "làm việc, các điểm không xác định nằm ngoài vùng làm việc; còn khi thẳng hàng dọc theo cạnh trên "
        "và cạnh bên, các điểm không xác định phải được giải quyết bằng thêm micrô."))
    b.append(p(
        "Vận tốc sóng âm đủ chậm nên sai số trong đo thời gian đều có thể chấp nhận được."))
    b.append(h3("Bộ số hoá dạng cánh tay (Arm Digitizer)", "Arm Digitizer"))
    b.append(p(
        "Bộ số hoá dạng cánh tay gồm một đế, hai cánh tay, hai bộ mã hoá quay và một con trỏ. Đế phải được "
        "neo tại một điểm nằm ngoài vùng làm việc, thường là ở mép bàn làm việc của người dùng. Một đầu của "
        "cánh tay, gọi là cánh tay đế (base arm), xoay quanh một trục thẳng đứng tại đế. Đầu kia của cánh "
        "tay đế khớp với một đầu của cánh tay thứ hai, gọi là cánh tay theo dõi (tracer arm), quanh một "
        "trục thẳng đứng. Ở đầu kia của cánh tay theo dõi là con trỏ. Một trong hai bộ mã hoá — bộ mã hoá "
        "đế — phát hiện góc giữa cánh tay đế và cánh tay base arm. Bộ mã hoá kia — bộ mã hoá cánh tay — "
        "phát hiện góc giữa cánh tay đế và cánh tay theo dõi."))
    b.append(p(
        "Để đơn giản hoá chế tạo, mỗi cánh tay được làm cùng chiều dài và, để đủ độ chính xác, mỗi bộ mã "
        "hoá cung cấp hơn 36.000 lần đếm trên mỗi vòng quay. Tín hiệu đầu ra của bộ mã hoá gồm hai sóng "
        "vuông có lệch pha 90°. Các cạnh lên và xuống của mỗi sóng vuông được đếm, và lệch pha 90° cung "
        "cấp hướng đếm."))
    b.append(p(
        "Vì mỗi bộ mã hoá là thiết bị đếm tương đối chứ không phải tuyệt đối, các thanh ghi đếm của mỗi bộ "
        "mã hoá phải được khởi tạo tại một góc đã biết. Thanh ghi đếm của bộ mã hoá cánh tay được đặt bằng "
        "góc xuất hiện khi con trỏ được đưa tới một vị trí đã biết chính xác. Vị trí này gọi là “home”. "
        "Thanh ghi đếm của bộ mã hoá đế được khởi tạo khi người ta thiết lập sự quay của hệ toạ độ x–y. "
        "Sau đó, các bộ mã hoá cộng hoặc trừ vào thanh ghi đếm của chúng khi con trỏ di chuyển."))
    b.append(p(
        "Với chiều dài cánh tay và các góc đã biết chính xác, có thể tính toạ độ x, y của con trỏ. Tuy "
        "nhiên, x và y là tương đối so với một hệ toạ độ có gốc tại trục của đế và có sự quay chưa biết. "
        "Vì vậy người dùng phải chọn một gốc, thường gần góc dưới bên trái của vùng bản vẽ, và hướng của "
        "trục x, thường song song với cạnh dưới của vùng bản vẽ. Thông tin này đủ để bộ xử lý tính toán "
        "phép tịnh tiến và phép quay thích hợp của hệ toạ độ."))
    b.append(h3("Lưới ô vuông đặt chồng (Grid Overlay)", "Grid Overlay"))
    b.append(p(
        "Lưới ô vuông đặt chồng đơn giản là một tấm trong suốt có in một lưới lên đó. Để sử dụng, đặt nó "
        "lên trên bản vẽ hoặc ảnh của vùng cần đo (Hình 12.5). Sau đó đếm số ô nằm trong đường bao của "
        "vùng. Những ô được bao ít nhất một nửa nên được tính. Diện tích cần tìm bằng tích số giữa số ô "
        "đã đếm và diện tích của mỗi ô. Độ chính xác đạt được tuỳ thuộc vào kích thước lưới, độ chính xác "
        "của kích thước lưới và độ chính xác khi đếm."))
    b.append(fig(5, F.fig(5)))

    # ---- 12.2
    b.append(h2("12.2 Thiết bị và thí nghiệm", "Equipment and Experiment"))
    b.append(p(
        "Rất nhiều loại planimeter và bộ số hoá khác nhau được chế tạo tại Mỹ, châu Âu và Nhật Bản. Một "
        "số đại diện của các dụng cụ này được mô tả trong mục này."))
    b.append(p(
        "Một trong những dụng cụ đo diện tích đơn giản nhất và ít tốn kém nhất là planimeter kiểu cực cơ "
        "khí (Hình 12.6). Nó gồm một trọng lượng (neo), hai cánh tay, một bánh xe đo và một con trỏ. Trọng "
        "lượng giữ chặt một đầu của cánh tay cực, cho phép đầu kia quay trên một cung cố định. Đầu quay của "
        "cánh tay cực gắn với một đầu của cánh tay theo dõi và ràng buộc chuyển động của nó theo cung đó. Ở "
        "đầu kia của cánh tay theo dõi là một con trỏ dùng để theo dấu chu vi của một diện tích chưa biết. "
        "Bánh xe đo nằm trong hộp ở một đầu của cánh tay theo dõi. Vị trí của bánh xe đo không quan trọng; "
        "tuy nhiên, trục của nó phải song song với cánh tay theo dõi."))
    b.append(fig(6, F.fig(6)))
    b.append(p(
        "Chiều dài hai cánh tay của planimeter trên Hình 12.6 có thể điều chỉnh được. Chiều dài cánh tay "
        "cực hoàn toàn không ảnh hưởng đến độ chính xác đo, và chỉ điều chỉnh cho thuận tiện. Chiều dài "
        "hiệu dụng của cánh tay theo dõi ảnh hưởng trực tiếp đến kết quả đọc; một cánh tay ngắn cho kết "
        "quả đọc lớn hơn. Bằng cách điều chỉnh chiều dài cánh tay theo dõi, có thể đạt một dải tỉ lệ rất "
        "hạn chế; tuy nhiên, điều này thường không được làm. Thay vào đó, chiều dài cánh tay được điều "
        "chỉnh tuỳ theo kích thước chung của các diện tích cần đo: cánh tay ngắn cho diện tích nhỏ và cánh "
        "tay dài cho diện tích lớn. Một cánh tay ngắn cho số lần đếm trên mỗi đơn vị diện tích lớn hơn, "
        "điều này cần thiết cho các diện tích nhỏ. Việc tỉ lệ thường thực hiện bằng cách nhân kết quả với "
        "một giá trị thích hợp."))
    b.append(p(
        "Để đưa bánh xe đo của planimeter trên Hình 12.6 về không, người ta vặn một bánh xe có rãnh nhỏ "
        "gắn vào trục bánh xe đo. Ở một số modelo khác, người ta nhấn một nút đẩy để đưa bánh xe về không. "
        "Cách sau dễ dùng hơn nhưng nhạy với sự lệch trục."))
    b.append(p(
        "Con trỏ planimeter thường là một thấu kính có một vòng tròn nhỏ khắc ở tâm, dù một số modelo dùng "
        "kim làm con trỏ. Loại con trỏ tốt nhất tuỳ thuộc sở thích cá nhân, dù con trỏ thấu kính phổ biến "
        "hơn nhiều."))
    b.append(p(
        "Hình 12.7 trình bày hai planimeter điện tử có đầu đọc số. Với những planimeter này, người ta có "
        "thể đo cả chiều dài lẫn diện tích. Để đo chiều dài, tháo vỏ bánh xe đo ra, gắn một tay cầm phụ, "
        "và lăn bánh xe dọc theo đường cần đo. Có thể đạt độ chính xác rất cao."))
    b.append(fig(7, F.fig(7)))
    b.append(p(
        "Planimeter ở trên của Hình 12.7 là loại cực. Nó gồm các bộ phận như modelo trên Hình 12.6, ngoại "
        "trừ việc bánh xe đo được gắn với một bộ mã hoá quang nhỏ và trọng lượng được tích hợp vào đầu đọc "
        "số. Bộ mã hoá cung cấp hai đầu ra sóng vuông lệch pha (tức một đầu ra lệch pha 90° so với đầu ra "
        "kia). Cả hai đầu ra đều đưa vào một bộ xử lý đếm các xung và dùng độ lệch pha để xác định hướng "
        "đếm."))
    b.append(p(
        "Bộ xử lý có tính năng tỉ lệ điện tử, chuyển kết quả đọc planimeter sang các đơn vị đo thực như "
        "foot vuông, mét vuông, mẫu Anh (acre) hay héc-ta (hectare). Người ta có thể truyền dữ liệu bộ xử "
        "lý cho máy tính qua một đơn vị giao tiếp phụ (không vẽ)."))
    b.append(p(
        "Planimeter ở dưới của Hình 12.7 là modelo tuyến tính, vì đường đi của đầu bị ràng buộc của cánh "
        "tay theo dõi là một đường thẳng. Đường thẳng này được duy trì bằng một liên kết cứng giữa hai bánh "
        "xe của xe con và trục của chúng. Những planimeter tuyến tính khác dùng hẳn một đường ray để dẫn "
        "đầu bị ràng buộc của cánh tay theo dõi đi theo đường thẳng."))
    b.append(p(
        "Planimeter kiểu cực ở trên Hình 12.8 và planimeter kiểu tuyến tính ở dưới Hình 12.8 đều là các "
        "modelo chạy pin nhỏ gọn. Bánh xe đo được tích hợp vào bộ xử lý, bộ này gắn với cánh tay cực của "
        "planimeter. Chiều dài hiệu dụng của cánh tay theo dõi trên cả hai dụng cụ kéo dài từ trục đầu bị "
        "ràng buộc tới con trỏ — trong trường hợp này là một vòng tròn nhỏ khắc ở tâm một thấu kính. Những "
        "planimeter này cung cấp tính năng tỉ lệ và lấy trung bình nhiều lần đọc một cách điện tử. Chúng "
        "không dùng để đo chiều dài được."))
    b.append(fig(8, F.fig(8)))
    b.append(p(
        "Hình 12.9 trình bày một bộ số hoá dạng cánh tay, có thể dùng như một thiết bị đo diện tích và "
        "chiều dài độc lập, hoặc để số hoá một bản đồ hay bản vẽ. Khi hoạt động như bộ số hoá, nó hiển thị "
        "các toạ độ (x, y) đồng thời truyền chúng cho máy tính. Bộ số hoá có giao tiếp tích hợp và có thể "
        "truyền bằng hơn 24 mã ASCII và nhị phân khác nhau, mỗi mã với một lựa chọn tham số. Nó có thể "
        "được đặt để đo toạ độ x và y theo đơn vị Anh hoặc hệ mét."))
    b.append(p(
        "Ngoài chế độ bộ số hoá, còn có ba chế độ khác để tính và hiển thị diện tích và chiều dài, diện "
        "tích và số lượng vật, hoặc số lượng vật và chiều dài. Các phép đo cũng có thể thực hiện theo đơn "
        "vị Anh hoặc hệ mét. Mọi mục hiển thị đều có thể truyền cho máy tính qua giao tiếp tích hợp."))
    b.append(fig(9, F.fig(9)))
    b.append(p(
        "Bộ số hoá dạng cánh tay còn có những tính năng đặc biệt hữu ích khi dùng ngoài chế độ số hoá. Nó "
        "cung cấp tỉ lệ độc lập trên từng trục, xác định hệ số tỉ lệ thực nghiệm, lập trình bằng phím, tính "
        "toán bốn phép, đổi đơn vị và lấy trung bình. Ngoài ra, bộ số hoá dạng cánh tay có thể gập gọn lại "
        "khi không dùng đến."))
    b.append(p(
        "Bộ số hoá dạng cánh tay dùng được trên cả bề mặt trong suốt lẫn bề mặt làm việc đục thông thường. "
        "Do đó, chúng cũng hữu ích để số hoá hoặc đo diện tích trên các bản đồ hay bản vẽ chiếu ngược từ "
        "phía sau."))
    b.append(p(
        "Bộ số hoá dạng bàn, như loại trên Hình 12.10, là những dụng cụ phổ biến dùng để số hoá bản đồ và "
        "bản vẽ, đồng thời làm bàn phím mở rộng cho một số phần mềm. Khi dùng làm bàn phím mở rộng, người "
        "ta đặt một mẫu có hình các hàm phím lên một vị trí trong vùng làm việc. Chỉ vào một hàm và nhấn "
        "một phím con trỏ sẽ chọn hàm đó. Bàn có giao tiếp tích hợp và một hoặc nhiều mã nhị phân và ASCII. "
        "Thông số giao tiếp trên một số bàn do công tắc DIP điều khiển, trên một số khác do phần mềm máy "
        "tính điều khiển. Con trỏ nhẹ, gồm từ 1 đến 16 phím con trỏ. Bàn có kích thước từ cỡ sổ ghi chép "
        "cho tới 122 cm × 168 cm (48 in × 66 in) hay lớn hơn. Có những modelo có mặt làm việc trong suốt "
        "dùng được với bản đồ và bản vẽ chiếu ngược."))
    b.append(fig(10, F.fig(10)))
    b.append(p(
        "Bàn số hoá có ưu điểm là con trỏ nhẹ, nhưng những bàn lớn lại chiếm nhiều diện tích sàn và khó "
        "di chuyển. Một nhà chế tạo đã khắc phục nhược điểm này bằng cách thiết kế một bàn số hoá có thể "
        "cuộn lại."))
    b.append(p(
        "Cũng như bàn, bộ số hoá siêu âm nhằm mục đích số hoá bản đồ và bản vẽ, và cung cấp bàn phím mở "
        "rộng cho một số gói phần mềm. Chúng có giao tiếp máy tính tích hợp với nhiều mã ASCII và nhị "
        "phân, cùng lựa chọn tham số, thích hợp với nhiều phần mềm khác nhau. Ưu điểm lớn của bộ số hoá siêu "
        "âm là tính cơ động và khả năng hoạt động tốt trên bề mặt trong suốt cần thiết cho các bản đồ và "
        "bản vẽ chiếu ngược."))
    b.append(p(
        "Bảng 12.1 liệt kê các nhà chế tạo planimeter và Bảng 12.2 liệt kê nhiều nhà chế tạo bộ số hoá đồ "
        "hoạ."))
    b.append(table(
        ["Công ty", "Địa chỉ", "Điện thoại"],
        [["Gebruder Haff Gmbh", "Tiroler Strasse 5, D-87459 Pfronten, Germany", "49-8363-9122-0"],
         ["Koizumi Sokki Mfg. Co., Ltd.", "1-132, Midori-Cho, Nagaoka-Shi, Niigata 940-21, Japan", "(0) 258-27-1102"],
         ["Lasico Inc.", "2451 Riverside Drive, Los Angeles, CA 90039", "(213) 662-2128"],
         ["Sokkia Corp.", "9111 Barton St., P.O. Box 2934, Overland Park, KS", "(800) 476-5542"]],
        "Bảng 12.1 · Các công ty chế tạo planimeter."))
    b.append(table(
        ["Công ty", "Địa chỉ", "Điện thoại"],
        [["Altek Corporation", "12210 Plum Orchard St., Silver Spring, MD 20904", "(301) 572-2555"],
         ["Calcomp Technology Inc.", "2411 West La Palma Ave., Anaheim, CA 92801-2589", "(800) 445-6515"],
         ["GTCO Corporation", "7125 Riverwood Drive, Columbia, MD 21046", "(800) 344-4723"],
         ["Lasico Inc.", "2451 Riverside Drive, Los Angeles, CA 90039", "(213) 662-2128"],
         ["Numonics Corporation", "101 Commerce Drive, Box 1005, Montgomeryville, PA 18936", "(215) 362-2766"],
         ["Wacom Technology Corp.", "501 S.E. Columbia Shores Blvd., Suite 300, Vancouver, WA 98661",
          "(360) 750-8882"]],
        "Bảng 12.2 · Các công ty chế tạo bộ số hoá."))

    # ---- 12.3
    b.append(h2("12.3 Đánh giá", "Evaluation"))
    b.append(p(
        "Mỗi dụng cụ đo diện tích nêu trong mục này đều xuất sắc và đã được chứng minh rộng rãi qua sử "
        "dụng. Tuy nhiên, một số dụng cụ phù hợp hơn với một số nhiệm vụ và môi trường vận hành nhất định "
        "so với những dụng cụ khác."))
    b.append(p(
        "Để đo một diện tích nhỏ hơn hình tròn tương đương đường kính khoảng 2 cm, bộ số hoá có lẽ là lựa "
        "chọn tốt nhất. Với những diện tích có độ lớn này, phần tử phân giải của planimeter bắt đầu chiếm "
        "một phần đáng kể của tổng diện tích. Phần tử phân giải của hầu hết bộ số hoá nhỏ hơn đáng kể so "
        "với planimeter, và mọi phép đo luôn là cộng hoặc trừ một phần tử phân giải."))
    b.append(p(
        "Để đo những diện tích tương đương với hình tròn có đường kính từ 2 cm đến 55 cm, cả planimeter "
        "lẫn bộ số hoá đều cho kết quả xuất sắc."))
    b.append(p(
        "Khi đo những diện tích lớn hơn hình tròn tương đương đường kính khoảng 55 cm, người ta vẫn có "
        "thể dùng planimeter; tuy nhiên, phải chia diện tích lớn thành những diện tích nhỏ hơn và đo riêng "
        "từng diện tích nhỏ. Bộ số hoá có thể đo những diện tích lớn hơn đáng kể, nhưng tới một mức nào "
        "đó nó cũng sẽ tới giới hạn. Khi đó, có thể dùng kỹ thuật chia diện tích lớn thành những diện tích "
        "nhỏ mà bộ số hoá xử lý được."))
    b.append(p(
        "Dụng cụ đo diện tích tương lai chắc chắn sẽ tận dụng vi xử lý nhiều hơn nữa để cung cấp thêm các "
        "tính năng như đưa vào hiệu chỉnh độ dốc và độ nghiêng, các phép toán thống kê, và xác định tâm, "
        "mô-men, v.v. Các dụng cụ sẽ trở nên cơ học đơn giản hơn và tin cậy hơn. Những tính năng như tiết "
        "kiệm diện tích văn phòng và tính cơ động sẽ được nhấn mạnh. Thiết bị đo diện tích hoàn hảo sẽ gồm "
        "một con trỏ rời để chỉ điểm và một thiết bị nhỏ giống máy tính cầm tay để thao tác trên kết quả, "
        "hiển thị, lưu trữ và gửi chúng cho máy tính."))
    b.append(p(
        "Máy quét và phần mềm đi kèm cũng sẽ tác động đến lĩnh vực đo diện tích, nhất là khi phạm vi phủ "
        "sóng của chúng tăng lên và giá thành giảm xuống."))
    b.append(h3("Các thuật ngữ định nghĩa", "Defining Terms"))
    b.append('<dl class="glossary">'
             '<dt>Planimeter</dt><dd>Bộ tích phân cơ học dùng để đo diện tích của những vùng khép kín trên '
             'bản đồ, bản vẽ, v.v.</dd>'
             '<dt>Cánh tay cực (Pole arm)</dt><dd>Một trong hai thanh cấu thành planimeter kiểu cực. Một '
             'đầu của cánh tay cực được cố định và đầu kia tự do quay. Chiều dài cánh tay cực không ảnh '
             'hưởng đến kết quả đọc planimeter.</dd>'
             '<dt>Cánh tay theo dõi (Tracer arm)</dt><dd>Thanh của planimeter mang bánh xe đo. Một đầu của '
             'cánh tay theo dõi bị ràng buộc theo một đường cố định, đầu kia theo dấu chu vi của vùng khép '
             'kín đang được đo. Chiều dài cánh tay cực tỉ lệ nghịch với kết quả đọc planimeter.</dd>'
             '<dt>Planimeter kiểu cực (Polar planimeter)</dt><dd>Planimeter có đầu bị ràng buộc của cánh '
             'tay theo dõi đi theo một đường tròn.</dd>'
             '<dt>Planimeter kiểu tuyến tính (Linear planimeter)</dt><dd>Planimeter có đầu bị ràng buộc '
             'của cánh tay theo dõi đi theo một đường thẳng.</dd>'
             '<dt>Bánh xe đo (Measuring wheel)</dt><dd>Bánh xe của planimeter có góc quay tỉ lệ trực tiếp '
             'với diện tích.</dd>'
             '<dt>Bộ số hoá (Digitizer)</dt><dd>Thiết bị chuyển dữ liệu hay hình ảnh sang dạng số. Các bộ '
             'số hoá bàn luận ở đây chuyển hình ảnh sang dạng số và được xếp loại là bộ số hoá đồ hoạ.</dd>'
             '<dt>Con trỏ (Pointer)</dt><dd>Bộ phận của planimeter hay bộ số hoá dùng để đi theo đường '
             'đang được theo dấu.</dd>'
             '<dt>Phần tử phân giải (Resolution element)</dt><dd>Phần tử diện tích nhỏ nhất có thể phân '
             'biệt. Khi nói đến đo diện tích, nó là một diện tích có giá trị 1.</dd>'
             '</dl>')
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>P. A. Santi, J. Fryhofer, and G. Hansen, Electronic planimetry, <i>Byte</i>, March 1980, '
             '113–122.</li>'
             '<li>K. Mandelberg, Anonymous, Internet, 4–96.</li>'
             '<li>E. Jones, ’89 Planning guide-digitizers, <i>Architectural &amp; Engineering</i>, '
             'July 1980, 37–40.</li>'
             '<li>P. E. Maybaum, Digitizing and computer graphics, <i>Keyboard</i>, Sept. 1978, 1–3.</li>'
             '</ol>')
    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(p(
        "F. A. Willers, <i>Mathematische Instrumente</i>, Munchen und Berlin: Verlag von R. Oldenbourg, "
        "1943."))

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 11</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 12. It carries all ten "
        "figures redrawn as vectors — the polar and linear planimeters, the measuring-wheel geometry, the "
        "parallelogram argument, the four-sided trace, the grid overlay, and the three digitizer families "
        "— plus the two manufacturer tables. The prose of the translation is not repeated here."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Planimeters are mechanical integrators. The tracer arm carries a pointer that follows the "
        "boundary of the area; one end of the arm is constrained to a fixed track — a circular arc for the "
        "polar type (Figure 12.1a) and a straight rail for the linear type (12.1b). The measuring wheel "
        "records only the component of motion perpendicular to its axis, so its accumulated count is the "
        "integral of sin φ along the path (Equation 12.1), and the enclosed area is the tracer-arm length "
        "times that count rescaled by the wheel circumference (12.2)."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Figure 12.2 is the heart of the principle: the wheel rotates by an amount proportional to "
        "distance travelled times sin φ, where φ is the angle between the wheel axis and the direction of "
        "travel. Because the wheel only rolls a fraction of the path, the count is a projection, not the "
        "arc length — and that projection, multiplied by the arm length, is exactly the enclosed area. "
        "Figure 12.3 shows the same thing as a parallelogram: base = arm length, height = wheel reading "
        "converted to distance."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "The four-sided trace in Figure 12.4 is the proof. Splitting the figure into four partial areas "
        "(12.3)–(12.6) and regrouping the integrals gives (12.7): the integrals for the constrained end "
        "cancel because that end runs a closed arc (net area zero), and what remains is exactly the area "
        "traced by the free, pointer end. The argument generalises to any number of sides and any shape."))
    b.append(p(
        "The digitizer route replaces the integrator with coordinate capture. Given the ordered (x, y) "
        "boundary points, the area is the shoelace sum (12.8). The subtlety the chapter stresses is the "
        "closing term: the last term ties the first and last points together, which matters for an "
        "embedded processor with little memory — either store the first point and compute the closing term "
        "on a key press, or force the last digitised point to coincide with the first so the term is zero."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Figure 12.5 is the humble grid overlay — place a transparent grid, count squares at least half "
        "inside the boundary, multiply by the square area. Accuracy depends on grid size, grid precision "
        "and counting care. It is the sanity check every other method is implicitly compared against."))
    b.append(p(
        "Three digitizer families are described. The tablet (Figure 12.10) senses the pointer against a "
        "wire grid embedded in the work surface, either by magnetostriction (a strain wave whose "
        "propagation time gives the distance) or by a 57.6 kHz signal whose amplitude profile peaks at the "
        "pointer. The sonic digitizer uses a spark-gap pointer and two or more microphones; the slant "
        "ranges to known microphone positions give x and y, with ambiguities resolved by extra microphones "
        "or by keeping the ambiguous points outside the work area. The arm digitizer (Figure 12.9) is a "
        "two-link arm with a rotary encoder at each joint, each providing more than 36,000 counts per "
        "revolution in quadrature; it reports (x, y) relative to an origin and rotation the user defines."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Section 12.2 is a buyer's guide. The manual polar planimeter (Figure 12.6) is the cheapest and "
        "simplest, preferred for occasional use; arm length is adjustable only for convenience, never for "
        "calibration, and the wheel is zeroed with a knurled wheel or a plunger. The electronic "
        "planimeters (Figure 12.7) add an optical encoder and a digital readout, and convert the reading to "
        "square feet, square metres, acres or hectares. The battery-operated models (Figure 12.8) package "
        "the processor on the pole arm and average multiple readings, but cannot measure length. Table "
        "12.1 lists planimeter makers and Table 12.2 the graphic-digitizer makers."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(table(
        ["Company", "Address", "Phone"],
        [["Gebruder Haff Gmbh", "Tiroler Strasse 5, D-87459 Pfronten, Germany", "49-8363-9122-0"],
         ["Koizumi Sokki Mfg. Co., Ltd.", "1-132, Midori-Cho, Nagaoka-Shi, Niigata 940-21, Japan", "(0) 258-27-1102"],
         ["Lasico Inc.", "2451 Riverside Drive, Los Angeles, CA 90039", "(213) 662-2128"],
         ["Sokkia Corp.", "9111 Barton St., P.O. Box 2934, Overland Park, KS", "(800) 476-5542"]],
        "Table 12.1 · Companies that make planimeters."))
    b.append(table(
        ["Company", "Address", "Phone"],
        [["Altek Corporation", "12210 Plum Orchard St., Silver Spring, MD 20904", "(301) 572-2555"],
         ["Calcomp Technology Inc.", "2411 West La Palma Ave., Anaheim, CA 92801-2589", "(800) 445-6515"],
         ["GTCO Corporation", "7125 Riverwood Drive, Columbia, MD 21046", "(800) 344-4723"],
         ["Lasico Inc.", "2451 Riverside Drive, Los Angeles, CA 90039", "(213) 662-2128"],
         ["Numonics Corporation", "101 Commerce Drive, Box 1005, Montgomeryville, PA 18936", "(215) 362-2766"],
         ["Wacom Technology Corp.", "501 S.E. Columbia Shores Blvd., Suite 300, Vancouver, WA 98661",
          "(360) 750-8882"]],
        "Table 12.2 · Companies that make digitizers."))
    b.append(p(
        "Section 12.3 is the decision rule, and it is the most useful part of the chapter. Below an "
        "equivalent circle of about 2 cm diameter the digitizer wins, because the planimeter's resolution "
        "element becomes a large fraction of the area. Between 2 cm and 55 cm either instrument is "
        "excellent. Above 55 cm the planimeter still works if you subdivide the area into pieces; the "
        "digitizer reaches further but hits the same wall eventually, and then the same subdivision trick "
        "applies. The future the authors foresee — microprocessors for slope and tilt correction, "
        "statistics, centroids and moments — is exactly what every modern tablet and arm digitizer now "
        "does."))
    b.append(p(
        "The defining-terms list is worth keeping: a planimeter is a mechanical integrator; the pole arm "
        "length does not affect the reading while the tracer-arm length is inversely proportional to it; a "
        "polar planimeter has its constrained end follow a circle, a linear one a straight line; the "
        "resolution element is the smallest discernible area, and for area measurement it has a value of 1."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 11</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 12 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 12 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 12 “Đo diện tích” của Charles B. Coulbourn và Wolfgang P. Buerner "
            "— planimeter (kiểu cực, kiểu tuyến tính, cơ khí, điện tử, dùng pin), bộ số hoá (dạng bàn, siêu "
            "âm, dạng cánh tay), lưới ô vuông, kèm hai bảng nhà chế tạo." if vi else
            "Companion to Chapter 12 of the CRC Measurement Handbook — area measurement by planimeter "
            "(polar, linear, mechanical, electronic, battery) and digitizer (tablet, sonic, arm), plus "
            "the grid overlay, with all ten figures.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 12' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 12' % BASE_EN)
    meta = ("Chương 12 · theo Ch12.pdf (CRC Press, 1999) · 10 hình, 2 bảng, 8 phương trình" if vi
            else "Chapter 12 · 10 figures, 2 tables, 8 equations")
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
