# -*- coding: utf-8 -*-
"""Handbook Chapter 25 — Tactile Sensing
(R. E. Saad, A. Bonen, K. C. Smith, B. Benhabib — University of Toronto).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch25.py
"""
import os

import hb25fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch25-tactile-sensing"
TITLE_EN = "Tactile Sensing"
TITLE_VI = "Cảm biến xúc giác"
BYLINE = "R. E. Saad · A. Bonen · K. C. Smith · B. Benhabib · University of Toronto"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch24-torque-and-power-measurement"
PREV_VI = "ch24-torque-and-power-measurement"
PREV_T_EN = "Torque and Power Measurement"
PREV_T_VI = "Đo mômen xoắn và công suất"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-25-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ol(items):
    return ('<ol style="margin:-.3rem 0 1.2rem 1.3rem;line-height:1.85;font-size:.95rem">'
            + "".join("<li>%s</li>" % i for i in items) + "</ol>")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Robot trong môi trường công nghiệp thực hiện những công việc lặp đi lặp lại như cấp phôi cho "
        "máy, lắp ráp chi tiết, sơn và hàn. Chỉ trong một số ít trường hợp, những tay máy tự động này "
        "mới có thể điều chỉnh hành động của mình dựa trên thông tin cảm biến. Mặc dù cho đến nay phần "
        "lớn công trình nghiên cứu trong lĩnh vực cảm biến robot đều tập trung vào thị giác máy tính, "
        "cảm biến tiếp xúc lại là một đặc tính quan trọng không kém đối với robot và cũng đã nhận được "
        "sự quan tâm nhất định. Không có khả năng cảm nhận xúc giác, robot không thể được kỳ vọng sẽ "
        "nắm bắt vật thể một cách hiệu quả. Trong bối cảnh đó, cảm biến xúc giác cho robot là trọng tâm "
        "của chương này."))

    # ------------------------------------------------------------ 25.1
    b.append(h2("25.1 Phân loại cảm biến", "Sensing Classification"))
    b.append(p(
        "Cảm biến robot có thể được phân thành hai loại: không tiếp xúc hoặc tiếp xúc [1]. Cảm biến "
        "không tiếp xúc liên quan đến tương tác giữa robot và môi trường thông qua một hiện tượng vật "
        "lý nào đó, như sóng âm hoặc sóng điện từ, tương tác mà không cần tiếp xúc. Những loại cảm biến "
        "robot quan trọng nhất thuộc kiểu không tiếp xúc là cảm biến thị giác và cảm biến tiệm cận. "
        "Ngược lại, cảm biến tiếp xúc hàm ý việc đo lường tương tác tổng quát xảy ra khi cơ cấu chấp "
        "hành cuối của robot được đưa vào tiếp xúc với một vật thể. Cảm biến tiếp xúc lại được phân "
        "thành cảm biến lực và cảm biến xúc giác."))
    b.append(p(
        "Cảm biến lực được định nghĩa là việc đo các hiệu ứng cơ học toàn cục của tiếp xúc, trong khi "
        "cảm biến xúc giác hàm ý việc phát hiện một loạt các tham số cục bộ bị ảnh hưởng bởi tiếp xúc. "
        "Trong số những hiệu ứng dựa trên tiếp xúc ấy, đáng kể nhất là ứng suất tiếp xúc, sự trượt, "
        "truyền nhiệt và độ cứng."))
    b.append(p(
        "Các tính chất của một vật thể được nắm giữ có thể rút ra từ cảm biến xúc giác được phân thành "
        "hai loại: hình học và động lực học [2]. Trong số các tính chất hình học có sự hiện diện, vị "
        "trí tương đối so với cơ cấu chấp hành cuối, hình dạng và kích thước, và điều kiện bề mặt "
        "[3–7]. Trong số các tham số động lực học gắn với việc nắm giữ có: phân bố lực, sự trượt, độ "
        "đàn hồi và độ cứng, và ma sát [8–12]."))
    b.append(p(
        "Cảm biến xúc giác đòi hỏi những bộ chuyển đổi tinh vi; tuy vậy, chỉ riêng sự sẵn có của các bộ "
        "chuyển đổi ấy chưa phải là điều kiện đủ để cảm biến xúc giác thành công. Còn cần phải điều "
        "khiển chính xác các phương thức mà qua đó cảm biến xúc giác tương tác với những vật thể được "
        "khảo sát (bao gồm lực tiếp xúc, cũng như vị trí và định hướng của cơ cấu chấp hành cuối) "
        "[13–15]. Điều này dẫn đến cảm biến xúc giác chủ động, đòi hỏi mức độ phức tạp cao trong việc "
        "thu thập và xử lý dữ liệu xúc giác [16]."))

    # ------------------------------------------------------------ 25.2
    b.append(h2("25.2 Các hiệu ứng cơ học của tiếp xúc", "Mechanical Effects of Contact"))
    b.append(p(
        "Cảm biến xúc giác thông thường liên quan đến việc một vật rắn ấn lõm lớp phủ mềm dẻo của một "
        "dãy cảm biến xúc giác [17], Hình 25.1. Sự ấn lõm của một lớp mềm dẻo do tiếp xúc có thể được "
        "phân tích từ hai quan điểm khác nhau về mặt khái niệm [1]. Quan điểm thứ nhất là việc đo ứng "
        "suất tiếp xúc thực tế (phân bố lực) trong lớp, thường liên quan đến việc điều khiển các nhiệm "
        "vụ thao tác. Quan điểm thứ hai là biên dạng võng của lớp, thường quan trọng cho việc nhận dạng "
        "các đặc trưng hình học của vật thể. Tùy theo cách tiếp cận được chọn, phải dùng những thuật "
        "toán xử lý và điều khiển khác nhau."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Tồn tại một quan hệ xác định giữa hình dạng cục bộ của một vật tiếp xúc và một tập biến dạng "
        "(hoặc dịch chuyển) dưới bề mặt; tuy nhiên, quan hệ này khá phức tạp. Do đó, cần dùng Lý thuyết "
        "Đàn hồi và Cơ học Tiếp xúc để mô hình hóa tương tác cảm biến–vật thể [18], và dùng Phân tích "
        "Phần tử Hữu hạn (FEA) như một công cụ thực tiễn để có được mô hình tiêu biểu hơn của cảm biến "
        "[19]."))
    b.append(p(
        "Nói chung, việc nghiên cứu cảm biến xúc giác gồm hai bước: (1) <i>phân tích thuận</i>, liên "
        "quan đến việc thu thập dữ liệu từ cảm biến (những thay đổi về ứng suất hoặc biến dạng, gây ra "
        "bởi sự ấn lõm của một vật thể lên bề mặt mềm dẻo của bộ chuyển đổi); và (2) <i>bài toán "
        "ngược</i>, thường liên quan đến việc khôi phục phân bố lực hoặc, trong một số trường hợp, khôi "
        "phục hình dạng của vật ấn."))

    b.append(h3("25.2.1 Lý thuyết giản lược cho cảm biến xúc giác",
                "Simplified Theory for Tactile Sensing"))
    b.append(p(
        "Để đơn giản, bài toán xúc giác hai chiều tổng quát ở đây được rút gọn thành bài toán một "
        "chiều. Hình 25.2 trình bày một bộ chuyển đổi một chiều gồm một lớp mềm dẻo, đồng nhất, đẳng "
        "hướng và tuyến tính chịu một ứng suất pháp q<sub>v</sub>(x) tạo ra bởi sự ấn lõm của một vật "
        "thể."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Nhằm mục đích mô hình hóa, người ta giả thiết lớp mềm dẻo là một nửa không gian đàn hồi. Sự "
        "đơn giản hóa này cho ta các phương trình dạng đóng để phân tích và tránh phải lập một bài toán "
        "phức tạp hơn, trong đó phải kể đến ảnh hưởng của các điều kiện biên tại x<sub>min</sub> và "
        "x<sub>max</sub>. Người ta đã chứng minh rằng việc mô hình hóa cảm biến bằng một nửa không gian "
        "đàn hồi là một xấp xỉ hợp lý cho trường hợp thực [18]. Với những điều kiện ấy, có thể chứng "
        "minh rằng biến dạng pháp, tại độ sâu y = d, do ứng suất pháp q<sub>v</sub>(y) gây ra, được cho "
        "bởi [20]:"))
    b.append(eq("ε<sub>z</sub>(x) = ∫<sub>−∞</sub><sup>∞</sup> q<sub>v</sub>(x − x<sub>0</sub>) "
                "h<sub>z</sub>(x<sub>0</sub>, d) dx<sub>0</sub>", "25.1"))
    b.append(p(
        "trong đó ε<sub>z</sub> là biến dạng tại x và z = d do ứng suất pháp trên bề mặt gây ra, và"))
    b.append(eq("h<sub>z</sub>(x) = − 2d(1 + ν)[d<sup>2</sup>(1 − ν) − νx<sup>2</sup>] ⁄ "
                "[πrE(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>]", "25.2"))
    b.append(p(
        "E và ν tương ứng là môđun đàn hồi và hệ số Poisson của lớp mềm dẻo. Khi nhận được Phương trình "
        "25.2, người ta giả thiết rằng phép phân tích được thực hiện trong điều kiện biến dạng phẳng. "
        "Cần lưu ý rằng có thể thực hiện một phép phân tích tương tự cho ứng suất hoặc biến dạng tiếp "
        "xúc."))
    b.append(p("Dịch chuyển pháp tại bề mặt, w, được cho bởi:"))
    b.append(eq("w(x) = ∫<sub>−∞</sub><sup>∞</sup> q<sub>v</sub>(x − x<sub>0</sub>) "
                "k(x<sub>0</sub>) dx<sub>0</sub>", "25.3"))
    b.append(p("trong đó"))
    b.append(eq("k(x) = [−2(1 − ν<sup>2</sup>) ⁄ (πE)] log|x ⁄ x<sub>a</sub>|", "25.4"))
    b.append(p(
        "Điểm kỳ dị tại x = 0 là điều dự kiến được, do tính kỳ dị của ứng suất tại điểm đó. Lưu ý rằng "
        "k(x) là biến dạng của bề mặt khi một tải trọng kỳ dị 1 N được tác dụng tại x = 0. Hằng số "
        "x<sub>a</sub> phải được chọn sao cho tại x = x<sub>a</sub>, biến dạng bằng không. Trong trường "
        "hợp này, biến dạng bằng không phải xảy ra tại x → ∞ (lưu ý rằng ta đã giả thiết cảm biến được "
        "mô hình hóa bằng một nửa không gian đàn hồi), nghĩa là x<sub>a</sub> → ∞. Bài toán này gắn với "
        "biến dạng hai chiều của một nửa không gian đàn hồi. Để loại bỏ khó khăn này, phải kể đến các "
        "điều kiện biên của bộ chuyển đổi (tức là phải phân tích một bộ chuyển đổi hữu hạn), điều mà "
        "nói chung đòi hỏi dùng FEA."))
    b.append(p(
        "Vì việc đo biến dạng (hoặc ứng suất) thường được thực hiện bằng một số rời rạc các phần tử cảm "
        "nhận, nên Phương trình 25.2 phải được rời rạc hóa (Hình 25.3). Tương ứng, phân bố lực phải được "
        "tái dựng tại những vị trí rời rạc như trên Hình 25.3. Gọi Δx<sub>q</sub> là khoảng cách giữa "
        "các điểm mà tại đó phân bố lực phải được tái dựng từ các phép đo biến dạng (hoặc ứng suất) do "
        "các phần tử cảm nhận biến dạng (hoặc ứng suất) phân bố đều với khoảng Δx<sub>p</sub> tại "
        "z = d thực hiện. Cũng giả thiết, dù điều đó không cần thiết, rằng Δx<sub>q</sub> = "
        "Δx<sub>p</sub> = Δx và rằng các lực được tác dụng tại những vị trí ngay phía trên các phần tử "
        "cảm nhận. Giờ đây có thể định nghĩa <i>vectơ mẫu biến dạng (ứng suất)</i>, ζ, với các thành "
        "phần ζ<sub>i</sub> = ε<sub>x</sub>(x<sub>i</sub>), i = 1, 2, …, n, và <i>vectơ phân bố lực</i>, "
        "F, với các thành phần f<sub>i</sub> = q<sub>v</sub>(x<sub>j</sub>), j = 1, 2, …, n. Khi đó, dạng "
        "rời rạc của Phương trình 25.1 được cho bởi:"))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(eq("ζ = <b>T</b>F", "25.5"))
    b.append(p(
        "trong đó các phần tử của ma trận T được cho bởi T<sub>ij</sub> = k<sub>v</sub>(x<sub>i</sub> − "
        "x<sub>j</sub>), i = 1, 2, …, n và j = 1, 2, …, n [23]. Có thể nhận được một quan hệ tương tự "
        "Phương trình 25.5 bằng cách rời rạc hóa Phương trình 25.3. Trong trường hợp tổng quát, khi "
        "Δx<sub>q</sub> ≠ Δx<sub>p</sub>, T không phải là ma trận vuông. Hơn nữa, trong trường hợp tổng "
        "quát, vectơ F gồm cả thành phần thẳng đứng lẫn thành phần tiếp tuyến."))
    b.append(p(
        "Các Phương trình 25.1 và 25.3 biểu diễn bài toán thuận thông thường, còn Phương trình 25.5 biểu "
        "diễn phiên bản rời rạc của bài toán thuận. Bài toán ngược, trong phần lớn trường hợp, là việc "
        "khôi phục biên dạng lực tác dụng từ các phép đo biến dạng, ứng suất hoặc độ võng. (Lưu ý rằng "
        "dịch chuyển bề mặt cũng có thể được dùng để khôi phục hình dạng của vật ấn.)"))
    b.append(p(
        "Trong [20], người ta đã chỉ ra rằng bài toán ngược là đặt không chỉnh, vì các toán tử h và k "
        "trong Phương trình 25.1 và 25.3 tương ứng là những toán tử có điều kiện xấu. Do đó, bài toán "
        "ngược dễ bị ảnh hưởng bởi nhiễu. Để giải bài toán này, phải dùng các kỹ thuật chính quy hóa "
        "[20]."))
    b.append(p(
        "Người ta đã chứng minh rằng, để tránh hiện tượng chồng phổ (aliasing) khi xác định biến dạng "
        "(ứng suất) liên tục tại độ sâu d bằng một bộ chuyển đổi rời rạc, các phần tử phải cách nhau "
        "một phần mười độ dày của lớp mềm dẻo. Tuy nhiên, người ta đã thu được kết quả tốt, không bị "
        "chồng phổ nhiều, khi cho các phần tử cảm nhận cách nhau một khoảng bằng đúng độ sâu của cảm "
        "biến [18]."))

    b.append(h3("25.2.2 Yêu cầu đối với cảm biến xúc giác",
                "Requirements for Tactile Sensors"))
    b.append(p(
        "Năm 1980, Harmon đã tiến hành một khảo sát nhằm xác định các chỉ tiêu kỹ thuật chung cho cảm "
        "biến xúc giác [21]. Những chỉ tiêu ấy về sau đã được nhiều nhà thiết kế cảm biến xúc giác dùng "
        "làm hướng dẫn:"))
    b.append(ol([
        "Độ phân giải không gian 1 đến 2 mm",
        "Kích thước dãy từ 5 × 10 đến 10 × 20 điểm",
        "Độ nhạy 0,5 × 10<sup>−2</sup> đến 1 × 10<sup>−2</sup> N cho mỗi phần tử cảm nhận lực (tactel)",
        "Dải động 1000:1",
        "Ứng xử ổn định và không có hiện tượng trễ",
        "Tần số lấy mẫu 100 Hz đến 1 kHz",
        "Đáp ứng đơn điệu, tuy không nhất thiết phải tuyến tính",
        "Giao diện mềm dẻo, chắc chắn và rẻ tiền",
    ]))
    b.append(p(
        "Trong khi các tính chất (5), (7) và (8) ở trên phải áp dụng cho bất kỳ cảm biến thực tiễn nào, "
        "những tính chất còn lại chỉ là gợi ý, đặc biệt về số phần tử của dãy và độ phân giải không "
        "gian. Những phát triển về cảm biến xúc giác tiếp sau [21] đã xác định thêm những phẩm chất "
        "mong muốn khác, đó là độ tin cậy, tính môđun hóa, tốc độ và khả năng hỗ trợ đa cảm biến [16]."))

    # ------------------------------------------------------------ 25.3
    b.append(h2("25.3 Các công nghệ cho cảm biến xúc giác",
                "Technologies for Tactile Sensing"))
    b.append(p(
        "Các công nghệ gắn với cảm biến xúc giác khá đa dạng: những khảo sát toàn diện về hiện trạng "
        "các công nghệ chuyển đổi xúc giác cho robot đã được trình bày trong [2, 3, 16, 17]. Một số "
        "công nghệ trong đó sẽ được thảo luận vắn tắt."))

    b.append(h3("25.3.1 Điện trở", "Resistive"))
    b.append(p(
        "Phương pháp chuyển đổi được chú ý nhiều nhất trong thiết kế cảm biến xúc giác là phương pháp "
        "dựa trên sự thay đổi điện trở của một vật liệu dẫn điện dưới áp suất tác dụng. Một cấu hình "
        "cơ bản của đầu đo điện trở được trình bày trên Hình 25.4. Mỗi điện trở, với giá trị thay đổi "
        "theo độ lớn của lực, đại diện cho một ô điện trở của bộ chuyển đổi. Nhiều loại vật liệu khác "
        "nhau đã được dùng để chế tạo ô cơ bản này."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Elastomer dẫn điện là một trong những vật liệu điện trở đầu tiên được dùng để phát triển cảm "
        "biến xúc giác. Chúng là những loại cao su cách điện, gốc tự nhiên hoặc gốc silicone, được làm "
        "dẫn điện bằng cách thêm các hạt vật liệu dẫn điện hoặc bán dẫn (ví dụ bạc hoặc carbon). Những "
        "thay đổi điện trở suất của elastomer dưới áp suất về cơ bản được tạo ra bởi hai cơ chế vật lý "
        "khác nhau. Trong cách thứ nhất, sự thay đổi điện trở suất của elastomer dưới áp suất gắn với "
        "biến dạng làm thay đổi mật độ hạt bên trong nó. Hai thiết kế tiêu biểu thuộc loại này được nêu "
        "trong [22, 23]. Trong cách thứ hai, trong khi điện trở khối của elastomer chỉ thay đổi chút ít "
        "khi bị nén, thiết kế lại cho phép tăng diện tích tiếp xúc giữa elastomer và một điện cực, và "
        "tương ứng là sự thay đổi điện trở tiếp xúc. Một thiết kế tiêu biểu thuộc loại này được nêu "
        "trong [24]. Trong [25], một cảm biến xúc giác mới hơn được báo cáo, có cả hai chức năng cảm "
        "nhận lực ba trục và cảm nhận trượt. Trong trường hợp thứ nhất, chức năng cảm nhận áp suất đạt "
        "được nhờ dùng các dãy đầu đo áp suất đo sự thay đổi điện trở tiếp xúc giữa một màng polyimide "
        "đã được xử lý đặc biệt và một đế điện trở."))
    b.append(p(
        "Các phần tử áp điện trở cũng đã được dùng trong một số cảm biến xúc giác. Công nghệ này hiện "
        "đặc biệt hấp dẫn vì, nhờ vi gia công, các phần tử áp điện trở có thể được tích hợp cùng với "
        "các mạch xử lý tín hiệu trên một chip duy nhất [26]. Một dãy cảm biến áp suất silic 32 × 32 "
        "phần tử, tích hợp các mạch xử lý CMOS để phát hiện phân bố áp suất có độ phân giải cao, đã "
        "được báo cáo trong [8]. Dãy cảm biến gồm một dãy các ô áp suất tổ chức theo ma trận x–y với "
        "bước ô 250 µm. Các mạch xử lý CMOS được tạo thành xung quanh dãy trên cùng một chip. Việc chế "
        "tạo dãy cảm biến được thực hiện bằng một quy trình CMOS 3 mm kết hợp với các kỹ thuật vi gia "
        "công silic. Kích thước màng liên quan là 50 µm × 50 µm. Kích thước tổng thể của chip dãy cảm "
        "biến là 10 mm × 10 mm."))
    b.append(p(
        "Trên Hình 25.4, một cấu trúc mạch để quét một dãy 3 × 3 phần tử áp điện trở được trình bày. Ý "
        "tưởng cơ bản lần đầu được đề xuất trong [24] và đã được nhiều nhà nghiên cứu khác nhau áp dụng "
        "trong nhiều dịp. Dùng phương pháp này, những thay đổi điện trở được chuyển thành điện áp ở đầu "
        "ra. Với các kết nối như trên Hình 25.4, điện trở R<sub>21</sub> có thể được xác định từ:"))
    b.append(eq("V<sub>0</sub> = (R<sub>f</sub> ⁄ R<sub>21</sub>) V<sub>cc</sub>", "25.6"))
    b.append(p(
        "trong đó V<sub>0</sub> là điện áp ra, V<sub>cc</sub> là điện áp phân cực, và R<sub>f</sub> là "
        "điện trở hồi tiếp của tầng khuếch đại đầu ra."))
    b.append(p(
        "Một vấn đề với cấu hình trên Hình 25.4 là khó phát hiện những thay đổi nhỏ của điện trở do "
        "điện trở nội của bộ dồn kênh cũng như những thay đổi điện áp của nguồn nuôi, những yếu tố có "
        "ảnh hưởng lớn tới đầu ra. Những phương pháp khác được dùng để quét các dãy đầu đo điện trở được "
        "tóm tắt trong [3]."))
    b.append(p(
        "Khi các áp điện trở và mạch điện được chế tạo trên cùng một đế silic, dãy cảm biến có thể được "
        "trang bị một mạch chuyển mạch phức tạp, nằm ngay cạnh các phần tử cảm nhận, cho phép độ phân "
        "giải tốt hơn trong các phép đo [9]."))

    b.append(h3("25.3.2 Điện dung", "Capacitive"))
    b.append(p(
        "Cảm biến xúc giác thuộc loại này liên quan đến việc đo điện dung, đại lượng thay đổi dưới tải "
        "tác dụng. Điện dung của một tụ điện bản song song phụ thuộc vào khoảng cách giữa hai bản và "
        "diện tích của chúng. Một cảm biến dùng lớp cách điện elastomer giữa hai bản cho độ mềm dẻo sao "
        "cho điện dung sẽ thay đổi theo tải pháp tác dụng, Hình 25.5(a)."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Hình 25.5(b) trình bày cấu hình cơ bản của một cảm biến xúc giác điện dung. Các giao điểm của "
        "hàng và cột dải dẫn điện tạo thành các tụ điện. Mỗi điện dung riêng lẻ có thể được xác định "
        "bằng cách đo điện áp ra tương ứng tại hàng và cột được chọn. Để giảm xuyên âm và nhiễu điện "
        "từ, các hàng và cột không được nối được nối đất. Hình 25.5(c) trình bày một mạch tương đương "
        "khi cảm biến được cấu hình để đo điện dung tạo thành tại giao điểm của hàng i và cột j, "
        "C<sub>ij</sub>. R<sub>d</sub> là điện trở vào của bộ phát hiện và C<sub>d</sub> biểu diễn ảnh "
        "hưởng của các điện dung ký sinh, bao gồm điện dung vào của khuếch đại phát hiện, điện dung ký "
        "sinh do các hàng và cột không được chọn, và điện dung do cáp nối bộ chuyển đổi với bộ phát "
        "hiện đóng góp. Vì điện dung ký sinh do các hàng và cột không được chọn thay đổi theo lực tác "
        "dụng, nên điện dung ký sinh do cáp được thiết kế để chiếm ưu thế [18]."))
    b.append(p("Độ lớn điện áp tại đầu vào của bộ phát hiện, |V<sub>d</sub>|, được cho bởi:"))
    b.append(eq("|V<sub>d</sub>| = C<sub>ij</sub>R<sub>d</sub>ω |V<sub>s</sub>| ⁄ "
                "√(1 + [ωR<sub>d</sub>(C<sub>ij</sub> + C<sub>d</sub>)]<sup>2</sup>)", "25.7"))
    b.append(p("Giả thiết rằng C<sub>d</sub> » C<sub>ij</sub> và ω đủ lớn,"))
    b.append(eq("|V<sub>d</sub>| ≅ (C<sub>ij</sub> ⁄ C<sub>d</sub>) |V<sub>s</sub>|", "25.8"))
    b.append(p(
        "Khi một tải được tác dụng lên bộ chuyển đổi, tụ điện bị biến dạng như trên Hình 25.5(a). Nhằm "
        "mục đích mô hình hóa, người ta giả thiết tụ điện bản chỉ chịu nén. Khi không có tải tác dụng, "
        "điện dung do phần tử ở hàng i và cột j, C<sup>0</sup><sub>ij</sub>, được cho bởi:"))
    b.append(eq("C<sup>0</sup><sub>ij</sub> = ε wl ⁄ h<sub>0</sub>", "25.9"))
    b.append(p(
        "trong đó ε là hằng số điện môi, w và l tương ứng là chiều rộng và chiều dài của tụ điện bản, và "
        "h<sub>0</sub> là khoảng cách giữa hai bản khi không có tải tác dụng. Điện áp tại đầu vào của bộ "
        "phát hiện trong trường hợp riêng này được ký hiệu là V<sub>d0</sub>; khi đó từ Phương trình "
        "25.8 ta có:"))
    b.append(eq("V<sub>d0</sub> ≅ (C<sup>0</sup><sub>ij</sub> ⁄ C<sub>d</sub>) |V<sub>s</sub>|", "25.10"))
    b.append(p("Khi một tải được tác dụng, tụ điện chịu nén và điện dung được cho bởi:"))
    b.append(eq("C<sub>ij</sub> = ε wl ⁄ (h<sub>0</sub> − Δh)", "25.11"))
    b.append(p("Biến dạng trong trường hợp này được cho bởi:"))
    b.append(eq("ζ<sub>z</sub> ≡ Δh ⁄ h<sub>0</sub>", "25.12"))
    b.append(p(
        "trong đó Δh là dịch chuyển của bản kim loại phía trên và Δh « h<sub>0</sub>. Biến dạng có thể "
        "được đo bằng:"))
    b.append(eq("(|V<sub>d</sub>| − |V<sub>d0</sub>|) ⁄ |V<sub>d</sub>| = "
                "(C<sub>ij</sub> − C<sup>0</sup><sub>ij</sub>) ⁄ C<sub>ij</sub> = "
                "1 − C<sup>0</sup><sub>ij</sub> ⁄ C<sub>ij</sub> = "
                "1 − (h<sub>0</sub> − Δh) ⁄ h<sub>0</sub> = Δh ⁄ h<sub>0</sub> ≡ ζ<sub>z</sub>", "25.13"))
    b.append(p(
        "Do đó, biến dạng tại mỗi tactel có thể được xác định bằng cách đo độ lớn của V<sub>d</sub> và "
        "V<sub>d0</sub> cho từng phần tử."))
    b.append(p(
        "Lưu ý rằng sự có mặt của một lực tiếp tuyến sẽ làm hai bản dịch chuyển tương đối theo phương "
        "tiếp tuyến và làm thay đổi diện tích hiệu dụng của các bản tụ. Một cảm biến áp suất điện dung "
        "lý tưởng có thể định lượng những khía cạnh cơ bản của sự chạm bằng cách cảm nhận các lực pháp, "
        "và có thể phát hiện trượt bằng cách đo các lực tiếp tuyến. Tuy nhiên, việc phân biệt hai loại "
        "lực ấy ở đầu ra của một phần tử cảm nhận duy nhất là một nhiệm vụ khó và đòi hỏi một bộ chuyển "
        "đổi phức tạp hơn bộ chuyển đổi trình bày trên Hình 25.5(a) [27]."))
    b.append(p(
        "Các thiết bị điện dung trên nền silic được vi gia công đặc biệt hấp dẫn nhờ tiềm năng đạt độ "
        "chính xác cao và độ trôi thấp. Một cảm biến với 1024 phần tử và độ phân giải không gian 0,5 mm "
        "đã được báo cáo trong [28]. Một số cấu trúc khả dĩ để thực hiện các đầu đo xúc giác điện dung "
        "mật độ cao trên silic đã được báo cáo trong [29]. Một đầu đo hình ngón tay dạng trụ đã được "
        "báo cáo trong [18]."))
    b.append(p(
        "Ưu điểm của các đầu đo điện dung gồm: dải động rộng, đáp ứng tuyến tính và độ bền vững. Nhược "
        "điểm chính của chúng là dễ bị ảnh hưởng bởi nhiễu, nhạy với nhiệt độ, và việc điện dung giảm "
        "theo kích thước vật lý, cuối cùng giới hạn độ phân giải không gian. Nghiên cứu đang tiến triển "
        "theo hướng phát triển các mạch xử lý điện tử để đo những điện dung nhỏ bằng khuếch đại điện "
        "tích [30], và phát triển các cấu trúc điện dung mới [29]."))

    b.append(h3("25.3.3 Áp điện", "Piezoelectric"))
    b.append(p(
        "Một vật liệu được gọi là áp điện nếu, khi chịu một ứng suất hoặc biến dạng, nó sinh ra điện. "
        "Hiệu ứng áp điện dọc xảy ra khi điện được sinh ra theo cùng hướng với ứng suất, Hình 25.6. "
        "Trên Hình 25.6(a), một ứng suất pháp σ (= F/A) được tác dụng dọc theo Hướng 3 và các điện tích "
        "được sinh ra trên những bề mặt vuông góc với Hướng 3. Hiệu ứng áp điện ngang xảy ra khi điện "
        "được sinh ra theo hướng vuông góc với ứng suất."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p("Điện áp V sinh ra giữa hai điện cực do ứng suất σ được cho bởi:"))
    b.append(eq("V = d<sub>33</sub> (h ⁄ ε) σ", "25.14"))
    b.append(wl([
        "trong đó d<sub>33</sub> = hằng số áp điện gắn với hiệu ứng áp điện dọc",
        "ε = hằng số điện môi",
        "h = độ dày của vật liệu áp điện",
    ]))
    b.append(p(
        "Vì vật liệu áp điện là chất cách điện, nên từ quan điểm điện, bộ chuyển đổi trên Hình 25.6(a) "
        "có thể được coi là một tụ điện. Do đó,"))
    b.append(eq("V = Q ⁄ C = (Q ⁄ εA) h", "25.15"))
    b.append(wl([
        "trong đó Q = điện tích cảm ứng bởi ứng suất σ",
        "C = điện dung của tụ điện bản song song",
        "A = diện tích của mỗi điện cực",
    ]))
    b.append(p("So sánh Phương trình 25.14 và 25.15 dẫn đến:"))
    b.append(eq("Q = d<sub>33</sub> σA", "25.16"))
    b.append(p(
        "Từ đó kết luận rằng lực tác dụng lên vật liệu áp điện có thể được xác định bằng cách tìm điện "
        "tích Q. Khuếch đại điện tích thường được dùng để xác định Q. Cấu hình cơ bản của một khuếch "
        "đại điện tích được trình bày trên Hình 25.6(b). Điện tích sinh ra trong bộ chuyển đổi được "
        "chuyển sang tụ C<sub>f</sub> và điện áp ra V<sub>o</sub> được cho bởi:"))
    b.append(eq("V<sub>o</sub> = − Q ⁄ C<sub>f</sub>", "25.17"))
    b.append(p(
        "Mạch phải xả định kỳ tụ hồi tiếp C<sub>f</sub> để tránh bão hòa khuếch đại do các điện tích ký "
        "sinh sinh ra bởi điện áp và dòng điện lệch không của khuếch đại thuật toán. Điều này đạt được "
        "nhờ một khóa như trên Hình 25.6(b) hoặc nhờ một điện trở song song với C<sub>f</sub>."))
    b.append(p(
        "Vật liệu áp điện được dùng rộng rãi nhất trong việc thực hiện các đầu đo xúc giác là "
        "PVF<sub>2</sub>. Nó thể hiện hiệu ứng áp điện lớn nhất trong số mọi vật liệu đã biết. Tính mềm "
        "dẻo, kích thước nhỏ, độ nhạy và đầu ra điện lớn của nó mang lại nhiều ưu điểm cho các ứng dụng "
        "cảm biến nói chung và cảm biến xúc giác nói riêng. Có thể tìm thấy các ví dụ về cảm biến xúc "
        "giác được thực hiện bằng công nghệ này trong [1, 31]."))
    b.append(p(
        "Ưu điểm chính của công nghệ áp điện là dải động rộng và độ bền. Đáng tiếc, đáp ứng của các vật "
        "liệu hiện có không kéo dài xuống tới dòng một chiều, và do đó không thể đo trực tiếp các tải "
        "ổn định. Ngoài ra, vật liệu PVF<sub>2</sub> tạo ra một đầu ra điện tích dễ bị nhiễu điện và "
        "phụ thuộc nhiệt độ."))
    b.append(p(
        "Khả năng đo hiện tượng quá độ bằng vật liệu áp điện gần đây đã khuyến khích một số nhà nghiên "
        "cứu dùng hiệu ứng áp điện để phát hiện các dao động cho thấy sự trượt sắp xảy ra, sự xuất hiện "
        "tiếp xúc, sự thay đổi cục bộ độ cong của da, và để ước lượng ma sát và độ cứng của vật thể "
        "[7, 10, 11]. Nếu bộ chuyển đổi áp điện trên Hình 25.6(a) được nối với một khuếch đại thuật "
        "toán có đầu vào FET, được cấu hình như một bộ chuyển đổi dòng điện sang điện áp như trên Hình "
        "25.7, thì điện áp ra được cho bởi:"))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(eq("V<sub>o</sub> = (dQ ⁄ dt) R<sub>f</sub> = A R<sub>f</sub> d<sub>33</sub> "
                "(dσ ⁄ dt)", "25.18"))
    b.append(p(
        "trong đó R<sub>f</sub> là điện trở hồi tiếp. Tương ứng, cấu hình mạch này tạo ra phương tiện để "
        "đo những thay đổi của ứng suất tiếp xúc. Có thể tìm thấy một giải thích chi tiết về ứng xử của "
        "cảm biến này trong [7]."))

    b.append(h3("25.3.4 Quang", "Optical"))
    b.append(p(
        "Những phát triển gần đây về công nghệ sợi quang và camera bán dẫn đã dẫn đến nhiều thiết kế cảm "
        "biến xúc giác mới lạ [32, 33]. Một số thiết kế trong đó dùng những màng mềm dẻo có gắn một mặt "
        "phản xạ, Hình 25.8. Ánh sáng được đưa vào cảm biến qua một cáp sợi quang. Một hình nón sáng "
        "rộng lan ra khỏi sợi quang, phản xạ trở lại từ màng và được thu bởi một sợi quang thứ hai. Khi "
        "một lực ngoài tác dụng lên elastomer, nó làm giảm khoảng cách giữa mặt phản xạ của màng và các "
        "sợi quang, h. Do đó, ánh sáng thu được bởi sợi thu thay đổi như một hàm của h, Hình 25.8(b). "
        "Để khôi phục khoảng cách một cách đơn trị từ cường độ sáng, cần một hàm đơn điệu. Điều này có "
        "thể đạt được bằng cách thiết kế bộ chuyển đổi sao cho nó hoạt động với h > h<sub>min</sub>, "
        "trong đó h<sub>min</sub> được chỉ ra trên Hình 25.8(b). (Vùng h > h<sub>min</sub> được ưu tiên "
        "hơn vùng h < h<sub>min</sub> vì lý do dải động.)"))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Một hiệu ứng quang khác có thể được dùng là phản xạ toàn phần bị phá vỡ [5, 34]. Với kỹ thuật "
        "này, một màng cao su đàn hồi phủ lên một tấm thủy tinh (tấm dẫn sáng) mà không chạm vào nó; ánh "
        "sáng đi vào cạnh bên của tấm thủy tinh bị phản xạ toàn phần bởi các mặt trên và mặt dưới rồi "
        "lan truyền dọc theo tấm, Hình 25.9."))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(p("Điều kiện để xảy ra phản xạ toàn phần là:"))
    b.append(eq("n<sub>2</sub> sin α ≤ n<sub>1</sub>", "25.19"))
    b.append(wl([
        "trong đó n<sub>1</sub> = chiết suất của môi trường bao quanh tấm dẫn sáng (trong trường hợp này "
        "là không khí, n<sub>1</sub> ≅ 1)",
        "n<sub>2</sub> = chiết suất của tấm dẫn sáng",
        "α = góc tới tại mặt phân cách thủy tinh–không khí",
    ]))
    b.append(p(
        "Các vật thể tiếp xúc với màng đàn hồi làm nó biến dạng và tạo ra sự tiếp xúc giữa phần dưới của "
        "màng và mặt trên của tấm dẫn sáng, phá vỡ phản xạ toàn phần. Do đó, ánh sáng trong tấm dẫn sáng "
        "bị tán xạ tại vị trí tiếp xúc. Ánh sáng thoát ra qua mặt dưới của tấm dẫn sáng có thể được phát "
        "hiện bởi một dãy photodiode, một cảm biến bán dẫn, hoặc cách khác là được vận chuyển ra khỏi bộ "
        "chuyển đổi bằng sợi quang [3]. Ảnh phát hiện được lưu trong máy tính để phân tích tiếp. Một "
        "màng cao su có bề mặt phẳng cho ảnh nhị phân (tiếp xúc hoặc không tiếp xúc) có độ phân giải "
        "cao [5]. Nếu tấm cao su được đúc với bề mặt có vân (Hình 25.9), thì thu được một đầu ra tỉ lệ "
        "với diện tích tiếp xúc và do đó có thể phát hiện các lực tác dụng [3]. Lực cắt cũng có thể "
        "được phát hiện bằng những thiết kế đặc biệt [35]. Các cảm biến dựa trên phản xạ toàn phần bị "
        "phá vỡ có thể được đúc thành hình ngón tay [5] và có khả năng tạo ra những ảnh xúc giác có độ "
        "phân giải rất cao. Những cảm biến như vậy có bán trên thị trường. Một phiên bản thu nhỏ được "
        "cải tiến của một cảm biến tương tự đã được đề xuất trong [34]."))
    b.append(p(
        "Những loại bộ chuyển đổi quang khác dùng các thiết bị “chắn sáng”. Một trong số ít cảm biến xúc "
        "giác có bán trên thị trường dùng loại bộ chuyển đổi này [36]. Trong một trong hai thiết kế "
        "hiện có, bề mặt của bộ chuyển đổi được làm bằng một vật liệu mềm dẻo, có một lưới các chốt dài "
        "ở mặt dưới. Khi lực tác dụng lên bề mặt mềm dẻo, các chốt ở mặt dưới chuyển động cơ học theo "
        "phương pháp tuyến với bề mặt, chắn đường đi của ánh sáng giữa một cặp bộ phát–bộ phát hiện "
        "quang. Độ lớn của chuyển động quyết định lượng ánh sáng tới được bộ thu quang. Tương ứng, lực "
        "tác dụng càng lớn thì lượng ánh sáng được bộ thu quang thu càng ít, Hình 25.10. Những vấn đề "
        "chính của thiết bị đặc thù này gắn với hiện tượng từ biến, hiện tượng trễ và sự thay đổi nhiệt "
        "độ. Sơ đồ này cũng đòi hỏi hiệu chuẩn riêng cho từng cặp bộ phát–bộ phát hiện quang."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Sợi quang cũng đã được dùng trực tiếp làm bộ chuyển đổi trong thiết kế cảm biến xúc giác. Việc "
        "dùng chúng dựa trên hai tính chất của cáp sợi quang: (1) nếu một sợi bị uốn một lượng đáng kể, "
        "thì góc tới tại thành sợi có thể giảm đủ để ánh sáng thoát ra khỏi lõi [37]; và (2) nếu hai sợi "
        "đi sát nhau và cả hai đều có bề mặt nhám, thì ánh sáng có thể truyền giữa hai sợi. Sự ghép "
        "sáng giữa các sợi kề nhau là một hàm của khoảng cách giữa chúng [3]."))
    b.append(p(
        "Một ví dụ về cảm biến xúc giác sợi quang, với cơ chế cảm nhận dựa trên sự tăng suy hao ánh sáng "
        "do uốn vi mô trong các sợi quang, được trình bày trên Hình 25.11 [37]. Bộ chuyển đổi gồm một "
        "dãy sợi quang hai chiều bốn lớp, được chế tạo bằng cách dùng hai lớp sợi quang làm cấu trúc gợn "
        "sóng, qua đó các uốn vi mô được cảm ứng trong hai lớp sợi hoạt động vuông góc nhau. Mỗi sợi "
        "hoạt động dùng một LED làm bộ phát và một photodiode PIN làm bộ phát hiện. Khi một vật thể được "
        "ấn tiếp xúc với bộ chuyển đổi, một phân bố ánh sáng được phát hiện tại mỗi bộ phát hiện. Phân "
        "bố ánh sáng này liên quan đến lực tác dụng và hình dạng của vật thể. Dùng những thuật toán "
        "phức tạp và cảm nhận chủ động (di chuyển vật thể tương đối so với bộ chuyển đổi), có thể thu "
        "được thông tin về vị trí, định hướng, kích thước và đường bao của vật thể [37]. Tuy nhiên, việc "
        "khôi phục các biên dạng lực tác dụng đã không được báo cáo trong [37]."))
    b.append(fig(11, F.fig(11), "vi"))

    b.append(h3("25.3.5 Quang đàn hồi", "Photoelastic"))
    b.append(p(
        "Một công nghệ đang nổi lên trong cảm biến xúc giác quang là việc phát triển các đầu đo quang "
        "đàn hồi. Khi một tia sáng lan truyền vào một môi trường bất đẳng hướng quang, nó tách thành hai "
        "tia phân cực tuyến tính vuông góc với nhau và lan truyền với vận tốc khác nhau. Sự tách một "
        "tia thành hai tia có phân cực vuông góc nhau này là kết quả của một tính chất vật lý của vật "
        "liệu kết tinh, được gọi là <i>lưỡng chiết quang</i>, hay đơn giản là <i>lưỡng chiết</i>. Hướng "
        "mà ánh sáng lan truyền với vận tốc lớn hơn được gọi là <i>trục nhanh</i>; hướng mà nó lan "
        "truyền chậm hơn được gọi là <i>trục chậm</i>. Một số vật liệu đẳng hướng quang — như thủy tinh, "
        "celluloid, bakelite và nói chung là các chất dẻo trong suốt — trở nên lưỡng chiết khi chịu một "
        "trường ứng suất. Hiệu ứng lưỡng chiết chỉ tồn tại trong thời gian tác dụng tải. Do đó, hiện "
        "tượng này được gọi là lưỡng chiết tạm thời hay nhân tạo, hoặc thông dụng hơn là hiện tượng "
        "quang đàn hồi."))
    b.append(p(
        "Hình 25.12(a) trình bày một đầu đo quang đàn hồi được đề xuất trong [38]. Nó gồm một dầm hai "
        "lớp được đỡ hoàn toàn, với một mặt phản xạ kẹp ở giữa. Các lực pháp tuyến đường được tác dụng "
        "lên mặt trên của dầm tại những tactel rời rạc, cách đều nhau một khoảng s dọc theo dầm. Lớp "
        "mềm dẻo phía trên dùng để bảo vệ gương, còn lớp phía dưới là lớp quang đàn hồi."))
    b.append(p(
        "Ánh sáng đơn sắc phân cực tròn, tới dọc theo trục z, chiếu sáng mặt dưới của bộ chuyển đổi. Ánh "
        "sáng lan truyền song song với trục z, đi qua lớp quang đàn hồi, rồi phản xạ trở lại từ gương. "
        "Nếu không có lực tác dụng lên bộ chuyển đổi, ánh sáng quay về là phân cực tròn, vì vật liệu "
        "quang đàn hồi không bị ứng suất là đẳng hướng. Nếu có lực tác dụng, ứng suất được cảm ứng "
        "trong lớp quang đàn hồi, làm vật liệu trở nên lưỡng chiết. Điều này tạo ra một hiệu pha nhất "
        "định giữa các thành phần của điện trường gắn với sự lan truyền của sóng ánh sáng. Hai hướng "
        "phân cực nằm trong mặt phẳng vuông góc với hướng lan truyền (trong trường hợp này là mặt phẳng "
        "x–y). Hệ quả của hiệu ứng này là ánh sáng ra bị phân cực elip, tạo ra một phân bố hiệu pha, p, "
        "giữa ánh sáng vào và ánh sáng ra tại mỗi điểm trong mặt phẳng x–y. Phân bố hiệu pha mang thông "
        "tin về phân bố lực tác dụng lên bộ chuyển đổi."))
    b.append(p(
        "Kính phân cực là một phương pháp thực tiễn để quan sát sự biến thiên không gian của cường độ "
        "sáng (các vân) do tác dụng của phân bố hiệu pha cảm ứng. Kính phân cực có thể là tuyến tính "
        "hoặc tròn, tùy theo sự phân cực của ánh sáng yêu cầu. Chúng cũng có thể được đặc trưng là loại "
        "phản xạ hoặc loại truyền qua, tùy theo việc đầu đo quang đàn hồi phản xạ hay truyền ánh sáng."))
    b.append(p(
        "Một kính phân cực tròn kiểu phản xạ, được trình bày trên Hình 25.12(b), được dùng để chiếu sáng "
        "bộ chuyển đổi trên Hình 25.12(a). Ánh sáng vào được phân cực tuyến tính và được hướng tới đầu "
        "đo quang đàn hồi nhờ một bộ tách chùm. Trước khi tới bộ chuyển đổi, ánh sáng được phân cực tròn "
        "bởi một bản phần tư bước sóng. Ánh sáng ra bị phân cực elip khi có lực tác dụng. Ánh sáng này "
        "được hướng tới một bộ phát hiện, đi qua bản phần tư bước sóng, bộ tách chùm và một bộ phân "
        "tích. Cuối cùng, nó được phát hiện bởi một camera nối với một bộ thu khung hình nối với một máy "
        "tính, để xử lý dữ liệu tiếp. Ánh sáng chiếu sáng camera gồm một tập hợp các vân, từ đó phải "
        "khôi phục phân bố lực tác dụng lên bộ chuyển đổi. Một kỹ thuật khôi phục lực từ các vân được "
        "mô tả trong [38]. Một mô hình của bộ chuyển đổi dùng FEA được báo cáo trong [39]."))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(p(
        "Một trong những ứng dụng sớm nhất của quang đàn hồi vào cảm biến xúc giác có từ giai đoạn phát "
        "triển bàn tay khéo léo Utah/MIT [40]. Các nhà nghiên cứu đã đề xuất dùng hiện tượng quang đàn "
        "hồi làm phương pháp chuyển đổi để khôi phục biên dạng lực tác dụng lên các ngón tay của bàn "
        "tay. Họ giới hạn ứng dụng của mình vào việc phát triển một đầu đo một điểm chạm, dù họ khẳng "
        "định rằng có thể thực hiện một dãy các thiết bị như vậy. Tuy nhiên, việc chế tạo một dãy lớn "
        "các thiết bị của họ sẽ khó khăn. Để khắc phục khó khăn này, một nhóm nghiên cứu khác đã đề "
        "xuất một bộ chuyển đổi khác [41]. Mặc dù một mô hình giải tích đã được phát triển cho cảm biến, "
        "một phương pháp hệ thống để khôi phục biên dạng lực hai chiều từ phân bố cường độ sáng đã "
        "không được báo cáo. Do đó, cảm biến chủ yếu được dùng để nghiên cứu phép phân tích thuận, cụ "
        "thể là quan sát phân bố cường độ sáng ứng với những vật thể chạm khác nhau được đưa vào tiếp "
        "xúc với cảm biến. Cảm biến này cuối cùng có thể được dùng để xác định một số tính chất hình học "
        "đơn giản của một vật thể đang chạm."))
    b.append(p(
        "Một cảm biến xúc giác được báo cáo trong [42] có khả năng phát hiện sự trượt. Cường độ sáng ra "
        "(hình ảnh vân) được thu bởi một camera giao tiếp với một máy tính. Khi một vật thể di chuyển "
        "qua bề mặt của bộ chuyển đổi, phân bố cường độ sáng thay đổi. Một phép phân tích trực tiếp các "
        "vân được dùng để phát hiện chuyển động của vật thể được nắm giữ; một kỹ thuật đặc biệt đã được "
        "báo cáo để tối ưu hóa quá trình so sánh nhằm phát hiện những khác biệt giữa hai hình ảnh vân "
        "xuất hiện do sự trượt của vật thể tiếp xúc với cảm biến [42]. Cần lưu ý rằng phép phân tích các "
        "vân như vậy không đòi hỏi phải khôi phục biên dạng lực tác dụng."))
    b.append(p(
        "Quang đàn hồi mang lại một số tính chất hấp dẫn cho việc phát triển cảm biến xúc giác: độ "
        "tuyến tính tốt, sự tương thích với các công nghệ cảm nhận dựa trên thị giác, và độ phân giải "
        "không gian cao gắn với công nghệ sau, điều có thể dẫn đến việc phát triển các thiết bị tạo ảnh "
        "xúc giác độ phân giải cao cần cho nhận dạng vật thể và thao tác tinh. Ngoài ra, cảm biến quang "
        "đàn hồi tương thích với công nghệ sợi quang, cho phép đặt các thiết bị xử lý điện tử ở xa và "
        "tránh các vấn đề nhiễu."))
    b.append(p(
        "Các công nghệ khác cho cảm biến xúc giác gồm cảm biến âm, cảm biến từ và cảm biến chân không vi "
        "khoang [43, 44]."))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> (1) Trong Phương trình 25.2, bản gốc in mẫu số là "
        "<i>πrE</i>(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>; chữ <i>r</i> ở đây nhiều khả năng là lỗi "
        "in ấn, vì theo thứ nguyên và theo dạng chuẩn của nghiệm Boussinesq cho biến dạng phẳng, mẫu số "
        "phải là <i>πE</i>(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>. Bản dịch giữ nguyên như bản gốc. "
        "(2) Trong mục 25.3.3, bản gốc viết “lực tác dụng lên vật liệu quang đàn hồi” — rõ ràng là lỗi "
        "đánh máy, phải là “vật liệu áp điện”; bản dịch đã sửa lại. (3) Phương trình 25.13 trong bản "
        "gốc in số hạng Δh/h<sub>0</sub> hai lần liên tiếp; bản dịch chỉ giữ một lần. (4) Bản gốc ghi "
        "“quy trình CMOS 3 mm”, gần như chắc chắn phải là 3 µm; bản dịch giữ nguyên như bản gốc."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "[1] P. Dario, Contact sensing for robot active touch, in <i>Robotic Science</i>, M. Brady (ed.), "
        "Cambridge, MA: MIT Press, 1989, chap. 3, 138–163.",
        "[2] P. P. L. Regtien, Tactile imaging, <i>Sensors and Actuators, A</i>, 31, 83–89, 1992.",
        "[3] R. A. Russell, <i>Robot Tactile Sensing</i>, Brunswick, Australia: Prentice-Hall, 1990.",
        "[4] A. D. Berger and P. K. Khosla, Using tactile data for real-time feedback, <i>Int. J. "
        "Robotics Res.</i>, 10(2), 88–102, 1991.",
        "[5] S. Begej, Planar and finger-shaped optical tactile sensors for robotic applications, "
        "<i>IEEE J. Robotics Automation</i>, 4, 472–484, 1988.",
        "[6] R. A. Russell and S. Parkinson, Sensing surface shape by touch, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, Atlanta, GA, 1993, 423–428.",
        "[7] R. D. Howe, A tactile stress rate sensor for perception of fine surface features, <i>IEEE "
        "Int. Conf. Solid-State Sensors Actuators</i>, San Francisco, CA, 1991, 864–867.",
        "[8] S. Sugiyama, K. Kawahata, H. Funabashi, M. Takigawa, and I. Igarashi, A 32 × 32 "
        "(1K)-element silicon pressure-sensor array with CMOS processing circuits, <i>Electron. Commun. "
        "Japan</i>, 75(1), 64–76, 1992.",
        "[9] J. S. Son, E. A. Monteverde, and R. D. Howe, A tactile sensor for localizing transient "
        "events in manipulation, <i>IEEE Int. Conf. Robotics Automation</i>, San Diego, CA, 1994, "
        "471–476.",
        "[10] M. R. Tremblay and M. R. Cutkosky, Estimating friction using incipient slip sensing during "
        "manipulation task, <i>IEEE Int. Conf. Robotics Automation</i>, Atlanta, GA, 1993, 429–434.",
        "[11] S. Omata and Y. Terubuna, New tactile sensor like the human hand and its applications, "
        "<i>Sensors and Actuators, A</i>, 35, 9–15, 1992.",
        "[12] R. Bayrleithner and K. Komoriya, Static friction coefficient determination by force sensing "
        "and its applications, <i>IROS’94</i>, Munich, Germany, 1994, 1639–1646.",
        "[13] M. A. Abidi and R. C. Gonzales, The use of multisensor data for robotic applications, "
        "<i>IEEE Trans. Robotics Automation</i>, 6, 159–177, 1990.",
        "[14] A. A. Cole, P. Hsu, and S. S. Sastry, Dynamic control of sliding by robot hands for "
        "regrasping, <i>IEEE Trans. Robotics Automation</i>, 8, 42–52, 1992.",
        "[15] P. K. Allen and P. Michelman, Acquisition and interpretation of 3-D sensor data from touch, "
        "<i>IEEE Trans. Robotics Automation</i>, 6, 397–404, 1990.",
        "[16] H. R. Nicholls (ed.), <i>Advanced Tactile Sensing for Robotics</i>, Singapore: World "
        "Scientific Publishing, 1992.",
        "[17] J. G. Webster (ed.), <i>Tactile Sensors for Robotics and Medicine</i>, New York: John Wiley "
        "&amp; Sons, 1988.",
        "[18] R. S. Fearing, Tactile sensing mechanism, <i>Int. J. Robotics Res.</i>, 9(3), 3–23, 1990.",
        "[19] T. H. Speeter, Three-dimensional finite element analysis of elastic continua for tactile "
        "sensing, <i>Int. J. Robotics Res.</i>, 11(1), 1–19, 1992.",
        "[20] Y. C. Pati, P. S. Krishnaprasad, and M. C. Peckerar, An analog neural network solution to "
        "the inverse problem of early taction, <i>IEEE Trans. Robotics Automation</i>, 8(2), 196–212, "
        "1992.",
        "[21] L. D. Harmon, Automated tactile sensing, <i>Int. J. Robotics Res.</i>, 1(2), 3–32, 1982.",
        "[22] W. E. Snyder and J. St. Clair, Conductive elastomers as a sensor for industrial parts "
        "handling equipment, <i>IEEE Trans. Instrum. Meas.</i>, 27(1), 94–99, 1991.",
        "[23] M. Shimojo, M. Ishikawa, and K. Kanaya, A flexible high resolution tactile imager with "
        "video signal output, <i>IEEE Int. Conf. Robotics Automation</i>, Sacramento, CA, 1991, 384–391.",
        "[24] W. D. Hillis, A high resolution imaging touch sensor, <i>Int. J. Robotic Res.</i>, 1(2), "
        "33–44, 1982.",
        "[25] Y. Yamada and M. R. Cutkosky, Tactile sensor with 3-axis force and vibration sensing "
        "functions and its applications to detect rotational slip, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, San Diego, CA, 1994, 3550–3557.",
        "[26] K. Njafi and C. H. Mastrangelo, Solid-state microsensors and smart structure, "
        "<i>Ultrasonic Symp.</i>, Baltimore, MD, 1993, 341–350.",
        "[27] F. Zhu and J. W. Spronck, A capacitive tactile sensor for shear and normal force "
        "measurements, <i>Sensors and Actuators, A</i>, 31, 115–120, 1992.",
        "[28] K. Suzuki, K. Najafi, and K. D. Wise, A 1024-element high-performance silicon tactile "
        "imager, <i>IEEE Trans. Electron Devices</i>, 17(8), 1852–1860, 1990.",
        "[29] M. R. Wolffenbuttel and P. L. Regtien, The accurate measurement of a micromechanical force "
        "using force-sensitive capacitances, <i>Conf. Precision Electromagnetic Meas.</i>, Boulder, CO, "
        "1994, 180–181.",
        "[30] M. R. Wolffenbuttel, R. F. Wolffenbuttel, and P. P. L. Regtien, An integrated charge "
        "amplifier for a smart tactile sensor, <i>Sensors and Actuators, A</i>, 31, 101–109, 1992.",
        "[31] E. D. Kolesar, Jr. and C. S. Dyson, Object imaging with piezoelectric robotic tactile "
        "sensor, <i>J. Microelectromechanical Syst.</i>, 4(2), 87–96, 1995.",
        "[32] J. L. Scheiter and T. B. Sheridan, An optical tactile sensor for manipulators, <i>J. Robot "
        "Computer-Integrated Manufacturing</i>, 1, 65–71, 1989.",
        "[33] R. Ristic, B. Benhabib, and A. A. Goldenberg, Analysis and design of a modular "
        "electrooptical tactile sensor, <i>IEEE Trans. Robotics Automation</i>, 5(3), 362–368, 1989.",
        "[34] H. Maekawa, K. K. Tanie, K. Komoriya, M. Kaneko, C. Horiguchi, and T. Sugawara, Development "
        "of a finger shaped tactile sensor and its evaluation by active touch, <i>IEEE Int. Conf. "
        "Robotics Automation</i>, Nice, France, 1992, 1327–1334.",
        "[35] M. Ohka, Y. Mitsurya, S. Takeuchi, and O. Kamekawa, A three-axis optical tactile sensor "
        "(FEM contact analyses and sensing experiments using a large-sized tactile sensor), <i>IEEE Int. "
        "Conf. Robotics Automation</i>, Nagoya, Aichi, Japan, 1995, 817–824.",
        "[36] J. Rebman and K. A. Morris, A tactile sensor with electro-optical transduction, in "
        "<i>Robots Sensors, Tactile and Non-Vision</i>, Vol. 2, A. Pugh (ed.), EFS Publications, 1986, "
        "145–155.",
        "[37] S. R. Emge and C. L. Chen, Two dimensional contour imaging with a fiber optic microbend "
        "tactile sensor array, <i>Sensors and Actuators, B</i>, 3, 31–42, 1991.",
        "[38] R. E. Saad, A. Bonen, K. C. Smith, and B. Benhabib, Distributed-force recovery for a planar "
        "photoelastic tactile sensor, <i>IEEE Trans. Instrum. Meas.</i>, 45, 541–546, 1996.",
        "[39] R. E. Saad, A. Bonen, K. C. Smith, and B. Benhabib, Finite-element analysis for photoelastic "
        "tactile sensors, <i>Proc. IEEE Int. Conf. Industrial Electronics, Control, and "
        "Instrumentation</i>, Orlando, FL, 1995, 1202–1207.",
        "[40] S. C. Jacobsen, J. E. Wood, D. F. Knutti, and B. Biggers, The Utah/MIT dexterous hand: work "
        "in progress, in <i>Robotics Research: The First International Symposium</i>, M. Brady and "
        "R. Paul (eds.), Cambridge: MIT Press, 1983, 601–653.",
        "[41] A. Cameron, R. Daniel, and H. Durrant-Whyte, Touch and motion, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, Philadelphia, PA, 1988, 1062–1067.",
        "[42] S. H. Hopkins, F. Eghtedari, and D. T. Pham, Algorithms for processing data from a "
        "photoelastic slip sensor, <i>Mechatronics</i>, 2(1), 15–28, 1992.",
        "[43] S. Ando and H. Shinoda, Ultrasonic emission tactile sensing, <i>IEEE Trans. Control "
        "Syst.</i>, 15(1), 61–69, 1996.",
        "[44] J. C. Jiang, V. Faynberg, and R. C. White, Fabrication of micromachined silicon tip "
        "transducer for tactile sensing, <i>J. Vacuum Sci. Technol., B</i>, 11, 1962–1967, 1993.",
    ]))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Robots in industrial settings perform repetitive tasks such as machine loading, parts assembly, "
        "painting and welding. Only in rare instances can these autonomous manipulators modify their "
        "actions on the basis of sensory information. Although the vast majority of research in robot "
        "sensing has so far concentrated on computer vision, contact sensing is an equally important "
        "capability and has received some attention as well. Without tactile perception a robot cannot "
        "be expected to grasp objects effectively. Robotic tactile sensing is therefore the focus of "
        "this chapter."))

    b.append(h2("25.1 Sensing Classification", "Phân loại cảm biến"))
    b.append(p(
        "Robotic sensing can be classified as either noncontact or contact [1]. Noncontact sensing "
        "involves interaction between the robot and its environment through some physical phenomenon — "
        "acoustic or electromagnetic waves, for instance — that acts without contact; the most important "
        "sensors of this type are vision and proximity sensors. Contact sensing, on the other hand, "
        "implies measurement of the general interaction that takes place when the robot’s end effector "
        "is brought into contact with an object, and it is further divided into force sensing and "
        "tactile sensing."))
    b.append(p(
        "Force sensing is the measurement of the global mechanical effects of contact, whereas tactile "
        "sensing is the detection of a wide range of local parameters affected by contact. The most "
        "significant of those contact-based effects are contact stresses, slippage, heat transfer and "
        "hardness."))
    b.append(p(
        "The properties of a grasped object that can be derived from tactile sensing fall into geometric "
        "and dynamometric classes [2]. The geometric properties include presence, location relative to "
        "the end effector, shape and dimensions, and surface condition [3–7]; the dynamometric "
        "parameters associated with grasping include force distribution, slippage, elasticity and "
        "hardness, and friction [8–12]."))
    b.append(p(
        "Tactile sensing requires sophisticated transducers, yet the availability of those transducers "
        "alone is not a sufficient condition for successful tactile sensing. The modalities through "
        "which the sensor interacts with the explored objects — contact forces as well as end-effector "
        "position and orientation — must also be controlled accurately [13–15]. This leads to active "
        "tactile sensing, which demands a high degree of complexity in the acquisition and processing of "
        "the tactile data [16]."))

    b.append(h2("25.2 Mechanical Effects of Contact", "Các hiệu ứng cơ học của tiếp xúc"))
    b.append(p(
        "Tactile sensing normally involves a rigid object indenting the compliant cover layer of a "
        "tactile sensor array [17], Figure 25.1. The indentation of a compliant layer by contact can be "
        "analysed from two conceptually different points of view [1]. The first is the measurement of "
        "the actual contact stresses — the force distribution — in the layer, which is usually what "
        "matters for controlling manipulation tasks. The second is the deflection profile of the layer, "
        "which is usually what matters for recognising geometrical object features. Different processing "
        "and control algorithms must be used depending on the approach adopted."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "A definite relationship exists between the local shape of a contacting body and a set of "
        "subsurface strains or displacements, but it is quite complex. It therefore requires the Theory "
        "of Elasticity and Contact Mechanics to model sensor–object interaction [18], and Finite Element "
        "Analysis (FEA) as the practical tool for obtaining a more representative model of the sensor "
        "[19]."))
    b.append(p(
        "The study of tactile sensors generally comprises two steps: (1) the <i>forward analysis</i>, "
        "concerned with acquiring data from the sensor — the changes in stress or strain induced by an "
        "object indenting the compliant surface of the transducer; and (2) the <i>inverse problem</i>, "
        "normally concerned with recovering the force distribution or, in some cases, the shape of the "
        "indentor."))

    b.append(h3("25.2.1 Simplified Theory for Tactile Sensing",
                "Lý thuyết giản lược cho cảm biến xúc giác"))
    b.append(p(
        "For simplicity the general two-dimensional tactile problem is reduced here to a "
        "one-dimensional one. Figure 25.2 shows a one-dimensional transducer consisting of a compliant, "
        "homogeneous, isotropic and linear layer subjected to a normal stress q<sub>v</sub>(x) created by "
        "the indentation of an object."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "For modelling purposes the compliant layer is assumed to be an elastic half-space. This "
        "simplification yields closed-form equations for the analysis and avoids the more complex "
        "problem in which the effect of the boundary conditions at x<sub>min</sub> and x<sub>max</sub> "
        "must be taken into account. Modelling the sensor as an elastic half-space has been shown to be "
        "a reasonable approximation to the real case [18]. Under those conditions the normal strain at a "
        "depth y = d due to the normal stress q<sub>v</sub>(y) is given by [20]:"))
    b.append(eq("ε<sub>z</sub>(x) = ∫<sub>−∞</sub><sup>∞</sup> q<sub>v</sub>(x − x<sub>0</sub>) "
                "h<sub>z</sub>(x<sub>0</sub>, d) dx<sub>0</sub>", "25.1"))
    b.append(p(
        "where ε<sub>z</sub> is the strain at x and z = d due to the normal stress on the surface, and"))
    b.append(eq("h<sub>z</sub>(x) = − 2d(1 + ν)[d<sup>2</sup>(1 − ν) − νx<sup>2</sup>] ⁄ "
                "[πrE(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>]", "25.2"))
    b.append(p(
        "E and ν are respectively the modulus of elasticity and the Poisson coefficient of the compliant "
        "layer. Equation 25.2 assumes that the analysis is performed under planar strain conditions. A "
        "similar analysis can be performed for tangential contact stresses or strains."))
    b.append(p("The normal displacement at the surface, w, is given by:"))
    b.append(eq("w(x) = ∫<sub>−∞</sub><sup>∞</sup> q<sub>v</sub>(x − x<sub>0</sub>) "
                "k(x<sub>0</sub>) dx<sub>0</sub>", "25.3"))
    b.append(p("where"))
    b.append(eq("k(x) = [−2(1 − ν<sup>2</sup>) ⁄ (πE)] log|x ⁄ x<sub>a</sub>|", "25.4"))
    b.append(p(
        "The singularity at x = 0 is expected because the stress itself is singular there. Note that "
        "k(x) is the deformation of the surface when a singular load of 1 N is applied at x = 0. The "
        "constant x<sub>a</sub> should be chosen so that the deformation is zero at x = x<sub>a</sub>. "
        "Here zero deformation should occur as x → ∞ — the sensor being modelled by an elastic "
        "half-space — that is, x<sub>a</sub> → ∞. The problem is associated with the two-dimensional "
        "deformation of an elastic half-space. To eliminate this difficulty the boundary conditions of "
        "the transducer must be taken into account, which means analysing a finite transducer and in "
        "general requires FEA."))
    b.append(p(
        "Since strain (or stress) measurements are usually made by a discrete number of sensing elements, "
        "Equation 25.2 must be discretised (Figure 25.3), and the force distribution must correspondingly "
        "be reconstructed at discrete positions as shown in Figure 25.3. Let Δx<sub>q</sub> be the "
        "distance between the points at which the force distribution is to be reconstructed from strain "
        "(or stress) measurements made by sensing elements uniformly spaced at intervals "
        "Δx<sub>p</sub> at z = d. Assume, although it is not necessary, that "
        "Δx<sub>q</sub> = Δx<sub>p</sub> = Δx and that the forces are applied immediately above the "
        "sensing elements. One can then define the strain (stress) sample vector ζ, whose components are "
        "ζ<sub>i</sub> = ε<sub>x</sub>(x<sub>i</sub>), i = 1, 2, …, n, and the force distribution vector "
        "F, whose components are f<sub>i</sub> = q<sub>v</sub>(x<sub>j</sub>), j = 1, 2, …, n. The "
        "discrete form of Equation 25.1 is then:"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(eq("ζ = <b>T</b>F", "25.5"))
    b.append(p(
        "where the elements of matrix T are T<sub>ij</sub> = k<sub>v</sub>(x<sub>i</sub> − "
        "x<sub>j</sub>), i = 1, 2, …, n and j = 1, 2, …, n [23]. A relation similar to Equation 25.5 can "
        "be obtained by discretising Equation 25.3. In the general case, where Δx<sub>q</sub> ≠ "
        "Δx<sub>p</sub>, T is not square; and in the general case the vector F comprises both vertical "
        "and tangential components."))
    b.append(p(
        "Equations 25.1 and 25.3 represent the regular forward problem, while Equation 25.5 represents "
        "its discretised version. The inverse problem in most cases consists of recovering the applied "
        "force profile from measurements of strain, stress or deflection. (Surface displacement can also "
        "be used to recover the shape of the indentor.)"))
    b.append(p(
        "Reference [20] showed that the inverse problem is ill-posed because the operators h and k of "
        "Equations 25.1 and 25.3 respectively are ill-conditioned; the inverse problem is consequently "
        "susceptible to noise, and regularisation techniques must be used to solve it [20]."))
    b.append(p(
        "It has been proven that, to avoid aliasing when determining the continuous strain (stress) at a "
        "depth d with a discretised transducer, the elements must be separated by one tenth of the "
        "compliant layer’s thickness. Good results without much aliasing were nevertheless obtained with "
        "sensing elements separated by a distance equal to the sensor’s depth [18]."))

    b.append(h3("25.2.2 Requirements for Tactile Sensors",
                "Yêu cầu đối với cảm biến xúc giác"))
    b.append(p(
        "In 1980 Harmon conducted a survey to determine general specifications for tactile sensors [21]. "
        "Those specifications have since been used as guidelines by many tactile sensor designers:"))
    b.append(ol([
        "Spatial resolution of 1 to 2 mm",
        "Array sizes of 5 × 10 to 10 × 20 points",
        "Sensitivity of 0.5 × 10<sup>−2</sup> to 1 × 10<sup>−2</sup> N for each force-sensing element "
        "(tactel)",
        "Dynamic range of 1000:1",
        "Stable behaviour with no hysteresis",
        "Sampling rate of 100 Hz to 1 kHz",
        "Monotonic response, though not necessarily linear",
        "Compliant interface, rugged and inexpensive",
    ]))
    b.append(p(
        "Properties (5), (7) and (8) should apply to any practical sensor; the others are merely "
        "suggestions, particularly as regards the number of array elements and the spatial resolution. "
        "Developments since [21] have identified additional desirable qualities: reliability, "
        "modularity, speed and the availability of multisensor support [16]."))

    b.append(h2("25.3 Technologies for Tactile Sensing", "Các công nghệ cho cảm biến xúc giác"))
    b.append(p(
        "The technologies associated with tactile sensing are quite diverse; extensive surveys of the "
        "state of the art in robotic tactile transduction have been presented in [2, 3, 16, 17]. Some of "
        "them are discussed briefly below."))

    b.append(h3("25.3.1 Resistive", "Điện trở"))
    b.append(p(
        "The transduction method that has received most attention in tactile sensor design concerns the "
        "change in resistance of a conductive material under applied pressure. A basic configuration of "
        "a resistive transducer is shown in Figure 25.4. Each resistor, whose value changes with the "
        "magnitude of the force, represents one resistive cell of the transducer, and a variety of "
        "materials has been used to manufacture the basic cell."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Conductive elastomers were among the first resistive materials used for tactile sensors. They "
        "are insulating natural or silicone-based rubbers made conductive by adding particles of "
        "conductive or semiconductive material such as silver or carbon. The changes in resistivity "
        "under pressure arise from two basically different physical mechanisms. In the first, the change "
        "is associated with deformation that alters the particle density within the elastomer; two "
        "typical designs of this kind are given in [22, 23]. In the second, the bulk resistance of the "
        "elastomer changes only slightly when it is compressed, but the design allows the contact area "
        "between the elastomer and an electrode to increase, and the contact resistance to change "
        "accordingly; a typical design is given in [24]. A newer tactile sensor with both three-axis "
        "force sensing and slippage sensing is reported in [25]; its pressure-sensing function uses "
        "arrays of pressure transducers that measure the change in contact resistance between a "
        "specially treated polyimide film and a resistive substrate."))
    b.append(p(
        "Piezoresistive elements have also been used in several tactile sensors, a technology that is "
        "particularly attractive at present because micromachining allows the piezoresistive elements to "
        "be integrated with the signal-processing circuits on a single chip [26]. A 32 × 32-element "
        "silicon pressure sensor array incorporating CMOS processing circuits for the detection of a "
        "high-resolution pressure distribution was reported in [8]. The array consists of pressure cells "
        "organised as an x–y matrix with a cell spacing of 250 µm, and the CMOS processing circuits are "
        "formed around the array on the same chip. Fabrication used a 3 mm CMOS process combined with "
        "silicon micromachining; the diaphragm size is 50 µm × 50 µm and the overall chip size is "
        "10 mm × 10 mm."))
    b.append(p(
        "Figure 25.4 shows a circuit topology for scanning a 3 × 3 array of piezoresistive elements. The "
        "basic idea was originally proposed in [24] and has been adapted on several occasions by "
        "different researchers. Resistance changes are converted into output voltages; with the "
        "connections shown, the resistance R<sub>21</sub> is determined from:"))
    b.append(eq("V<sub>0</sub> = (R<sub>f</sub> ⁄ R<sub>21</sub>) V<sub>cc</sub>", "25.6"))
    b.append(p(
        "where V<sub>0</sub> is the output voltage, V<sub>cc</sub> the bias voltage and R<sub>f</sub> the "
        "feedback resistance of the output amplifier stage."))
    b.append(p(
        "One problem with the configuration of Figure 25.4 is the difficulty of detecting small changes "
        "in resistance against the internal resistance of the multiplexer and against changes in the "
        "supply voltage, both of which strongly influence the output. Other methods used to scan "
        "resistive transducer arrays are summarised in [3]."))
    b.append(p(
        "When piezoresistors and circuits are fabricated on the same silicon substrate, the array can be "
        "equipped with a complex switching circuit next to the sensing elements that allows better "
        "resolution in the measurements [9]."))

    b.append(h3("25.3.2 Capacitive", "Điện dung"))
    b.append(p(
        "Tactile sensors in this category measure capacitance, which varies under applied load. The "
        "capacitance of a parallel-plate capacitor depends on the separation of the plates and on their "
        "areas; a sensor using an elastomeric separator between the plates provides compliance so that "
        "the capacitance varies with the applied normal load, Figure 25.5(a)."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Figure 25.5(b) shows the basic configuration of a capacitive tactile sensor. The intersections "
        "of rows and columns of conductor strips form capacitors, and each individual capacitance can be "
        "determined by measuring the corresponding output voltage at the selected row and column. To "
        "reduce cross-talk and electromagnetic interference the unselected rows and columns are "
        "grounded. Figure 25.5(c) shows an equivalent circuit for measuring the capacitance formed at "
        "the intersection of row i and column j, C<sub>ij</sub>. R<sub>d</sub> is the input resistance of "
        "the detector and C<sub>d</sub> represents the effects of stray capacitances — the "
        "detector-amplifier input capacitance, the stray capacitance to the unselected rows and columns, "
        "and the capacitance of the cable connecting transducer to detector. Because the stray "
        "capacitance due to the unselected rows and columns changes with the applied forces, the cable "
        "capacitance is designed to predominate [18]."))
    b.append(p("The magnitude of the voltage at the input of the detector, |V<sub>d</sub>|, is given by:"))
    b.append(eq("|V<sub>d</sub>| = C<sub>ij</sub>R<sub>d</sub>ω |V<sub>s</sub>| ⁄ "
                "√(1 + [ωR<sub>d</sub>(C<sub>ij</sub> + C<sub>d</sub>)]<sup>2</sup>)", "25.7"))
    b.append(p("Assuming that C<sub>d</sub> » C<sub>ij</sub> and that ω is sufficiently large,"))
    b.append(eq("|V<sub>d</sub>| ≅ (C<sub>ij</sub> ⁄ C<sub>d</sub>) |V<sub>s</sub>|", "25.8"))
    b.append(p(
        "When a load is applied the capacitor deforms as shown in Figure 25.5(a). For modelling purposes "
        "the plate capacitor is assumed to be under compression only. With no load applied, the "
        "capacitance of the element in the i-th row and j-th column, C<sup>0</sup><sub>ij</sub>, is:"))
    b.append(eq("C<sup>0</sup><sub>ij</sub> = ε wl ⁄ h<sub>0</sub>", "25.9"))
    b.append(p(
        "where ε is the permittivity of the dielectric, w and l the width and length of the plate "
        "capacitor, and h<sub>0</sub> the plate separation with no load. The detector input voltage for "
        "this particular case is V<sub>d0</sub>, so from Equation 25.8:"))
    b.append(eq("V<sub>d0</sub> ≅ (C<sup>0</sup><sub>ij</sub> ⁄ C<sub>d</sub>) |V<sub>s</sub>|", "25.10"))
    b.append(p("With a load applied the capacitor is under compression and the capacitance is:"))
    b.append(eq("C<sub>ij</sub> = ε wl ⁄ (h<sub>0</sub> − Δh)", "25.11"))
    b.append(p("The strain in this case is given by:"))
    b.append(eq("ζ<sub>z</sub> ≡ Δh ⁄ h<sub>0</sub>", "25.12"))
    b.append(p(
        "where Δh is the displacement of the top metal plate and Δh « h<sub>0</sub>. The strain can be "
        "measured by:"))
    b.append(eq("(|V<sub>d</sub>| − |V<sub>d0</sub>|) ⁄ |V<sub>d</sub>| = "
                "(C<sub>ij</sub> − C<sup>0</sup><sub>ij</sub>) ⁄ C<sub>ij</sub> = "
                "1 − C<sup>0</sup><sub>ij</sub> ⁄ C<sub>ij</sub> = "
                "1 − (h<sub>0</sub> − Δh) ⁄ h<sub>0</sub> = Δh ⁄ h<sub>0</sub> ≡ ζ<sub>z</sub>", "25.13"))
    b.append(p(
        "Consequently the strain at each tactel can be determined by measuring the magnitudes of "
        "V<sub>d</sub> and V<sub>d0</sub> for each element."))
    b.append(p(
        "Note that a tangential force would offset the plates tangentially and change the effective area "
        "of the capacitor plates. An ideal capacitive pressure sensor can quantify the basic aspects of "
        "touch by sensing normal forces and can detect slippage by measuring tangential forces; "
        "distinguishing between the two at the output of a single sensing element is, however, a "
        "difficult task and requires a more complex transducer than the one in Figure 25.5(a) [27]."))
    b.append(p(
        "Micromachined silicon-based capacitive devices are especially attractive for their potential "
        "high accuracy and low drift. A sensor with 1024 elements and a spatial resolution of 0.5 mm was "
        "reported in [28]; several possible structures for implementing high-density capacitive tactile "
        "transducers in silicon are reported in [29], and a cylindrical finger-shaped transducer in "
        "[18]."))
    b.append(p(
        "The advantages of capacitive transducers include wide dynamic range, linear response and "
        "robustness; their major disadvantages are susceptibility to noise, sensitivity to temperature, "
        "and the fact that capacitance decreases with physical size, which ultimately limits the spatial "
        "resolution. Research is progressing towards electronic processing circuits for measuring small "
        "capacitances with charge amplifiers [30] and towards new capacitive structures [29]."))

    b.append(h3("25.3.3 Piezoelectric", "Áp điện"))
    b.append(p(
        "A material is called piezoelectric if it produces electricity when subjected to a stress or "
        "deformation. The longitudinal piezoelectric effect occurs when the electricity is produced in "
        "the same direction as the stress, Figure 25.6: in Figure 25.6(a) a normal stress σ (= F/A) is "
        "applied along Direction 3 and charges are generated on the surfaces perpendicular to "
        "Direction 3. A transversal piezoelectric effect occurs when the electricity is produced "
        "perpendicular to the stress."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p("The voltage V generated across the electrodes by the stress σ is given by:"))
    b.append(eq("V = d<sub>33</sub> (h ⁄ ε) σ", "25.14"))
    b.append(wl([
        "where d<sub>33</sub> = piezoelectric constant associated with the longitudinal piezoelectric "
        "effect",
        "ε = permittivity",
        "h = thickness of the piezoelectric material",
    ]))
    b.append(p(
        "Since piezoelectric materials are insulators, the transducer of Figure 25.6(a) can be regarded "
        "as a capacitor from an electrical point of view. Consequently,"))
    b.append(eq("V = Q ⁄ C = (Q ⁄ εA) h", "25.15"))
    b.append(wl([
        "where Q = charge induced by the stress σ",
        "C = capacitance of the parallel capacitor",
        "A = area of each electrode",
    ]))
    b.append(p("Comparing Equations 25.14 and 25.15 leads to:"))
    b.append(eq("Q = d<sub>33</sub> σA", "25.16"))
    b.append(p(
        "The force applied to the piezoelectric material can therefore be determined by finding the "
        "charge Q, and charge amplifiers are usually used for that purpose. The basic configuration of a "
        "charge amplifier is shown in Figure 25.6(b): the charge generated in the transducer is "
        "transferred to the capacitor C<sub>f</sub> and the output voltage is"))
    b.append(eq("V<sub>o</sub> = − Q ⁄ C<sub>f</sub>", "25.17"))
    b.append(p(
        "The circuit must periodically discharge the feedback capacitor C<sub>f</sub> to avoid saturation "
        "of the amplifier by stray charges generated by the offset voltages and currents of the "
        "operational amplifier. This is achieved with a switch, as in Figure 25.6(b), or with a resistor "
        "in parallel with C<sub>f</sub>."))
    b.append(p(
        "The piezoelectric material most widely used in tactile transducers is PVF<sub>2</sub>, which "
        "shows the largest piezoelectric effect of any known material; its flexibility, small size, "
        "sensitivity and large electrical output offer many advantages for sensor applications in "
        "general and tactile sensors in particular. Examples of tactile sensors implemented with this "
        "technology can be found in [1, 31]."))
    b.append(p(
        "The major advantages of piezoelectric technology are its wide dynamic range and durability. "
        "Unfortunately the response of available materials does not extend down to dc, so steady loads "
        "cannot be measured directly; and PVF<sub>2</sub> produces a charge output that is prone to "
        "electrical interference and is temperature dependent."))
    b.append(p(
        "The possibility of measuring transient phenomena with piezoelectric material has recently "
        "encouraged some researchers to use the piezoelectric effect for detecting vibrations that "
        "indicate incipient slip, the occurrence of contact, local change in skin curvature, and for "
        "estimating the friction and hardness of an object [7, 10, 11]. If the piezoelectric transducer "
        "of Figure 25.6(a) is connected to an FET-input operational amplifier configured as a "
        "current-to-voltage converter, as in Figure 25.7, the output voltage is"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(eq("V<sub>o</sub> = (dQ ⁄ dt) R<sub>f</sub> = A R<sub>f</sub> d<sub>33</sub> "
                "(dσ ⁄ dt)", "25.18"))
    b.append(p(
        "where R<sub>f</sub> is the feedback resistor. The circuit accordingly provides the means to "
        "measure changes in the contact stress; a detailed explanation of the behaviour of this sensor "
        "can be found in [7]."))

    b.append(h3("25.3.4 Optical", "Quang"))
    b.append(p(
        "Recent developments in fibre optic technology and solid-state cameras have led to numerous "
        "novel tactile sensor designs [32, 33]. Some of them employ flexible membranes incorporating a "
        "reflecting surface, Figure 25.8. Light is introduced into the sensor through a fibre optic "
        "cable; a wide cone of light propagates out of the fibre, reflects back from the membrane and is "
        "collected by a second fibre. When an external force is applied to the elastomer it shortens the "
        "distance h between the reflective side of the membrane and the fibres, so the light gathered by "
        "the receiving fibre changes as a function of h, Figure 25.8(b). Recovering the distance "
        "unambiguously from the light intensity requires a monotonic function, which is obtained by "
        "designing the transducer to operate for h > h<sub>min</sub>, where h<sub>min</sub> is indicated "
        "in Figure 25.8(b); the region h > h<sub>min</sub> is preferred to h < h<sub>min</sub> for "
        "dynamic-range reasons."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(p(
        "Another optical effect that can be used is frustrated total internal reflection [5, 34]. An "
        "elastic rubber membrane covers, without touching, a glass plate — the waveguide — and light "
        "entering the side edge of the glass is totally reflected by the top and bottom surfaces and "
        "propagates along it, Figure 25.9."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p("The condition for total internal reflection is:"))
    b.append(eq("n<sub>2</sub> sin α ≤ n<sub>1</sub>", "25.19"))
    b.append(wl([
        "where n<sub>1</sub> = index of refraction of the medium surrounding the waveguide (in this case "
        "air, n<sub>1</sub> ≅ 1)",
        "n<sub>2</sub> = index of refraction of the waveguide",
        "α = angle of incidence at the glass–air interface",
    ]))
    b.append(p(
        "Objects in contact with the elastic membrane deform it and induce contact between the bottom of "
        "the membrane and the top surface of the waveguide, disrupting the total internal reflection. The "
        "light in the waveguide is consequently scattered at the contact location. Light escaping through "
        "the bottom surface can be detected by an array of photodiodes, by a solid-state sensor, or "
        "transported away from the transducer by fibres [3]; the detected image is stored in a computer "
        "for further analysis. A rubber membrane with a flat surface yields a high-resolution binary "
        "(contact or noncontact) image [5]; if the rubber sheet is moulded with a textured surface "
        "(Figure 25.9) the output is proportional to the area of contact and the applied forces can "
        "therefore be detected [3]. Shear forces can also be detected with special designs [35]. Sensors "
        "based on frustrated total internal reflection can be moulded into a finger shape [5] and are "
        "capable of forming very high-resolution tactile images; such sensors are commercially "
        "available, and an improved miniaturised version of a similar sensor was proposed in [34]."))
    b.append(p(
        "Other optical transducers use “occluder” devices; one of the few commercially available tactile "
        "sensors uses this kind of transducer [36]. In one of the two available designs the transducer’s "
        "surface is made of a compliant material that has, on its underside, a grid of elongated pins. "
        "When force is applied to the compliant surface the pins undergo a mechanical motion normal to "
        "the surface, blocking the light path of a photoemitter–detector pair. The amount of movement "
        "determines how much light reaches the photoreceiver: the more force applied, the less light is "
        "collected, Figure 25.10. The major problems with this device are creep, hysteresis and "
        "temperature variation, and the scheme also requires individual calibration of each "
        "photoemitter–photodetector pair."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Fibres have also been used directly as transducers. Their use rests on two properties of fibre "
        "optic cables: (1) if a fibre is subjected to a significant amount of bending, the angle of "
        "incidence at the fibre wall can be reduced sufficiently for light to leave the core [37]; and "
        "(2) if two fibres pass close to one another and both have roughened surfaces, light can pass "
        "between them, the coupling being a function of their separation [3]."))
    b.append(p(
        "An example of an optical fibre tactile sensor whose sensing mechanism is based on the increase "
        "of light attenuation due to microbends in the fibres is shown in Figure 25.11 [37]. The "
        "transducer consists of a four-layer, two-dimensional fibre optic array built using two layers of "
        "optical fibres as a corrugation structure, through which microbends are induced in two "
        "orthogonal layers of active fibres. Each active fibre uses an LED as emitter and a PIN "
        "photodiode as detector. When an object is forced into contact with the transducer a light "
        "distribution is detected at each detector, related to the applied force and the shape of the "
        "object. Using complex algorithms and active sensing — moving the object relative to the "
        "transducer — the object’s position, orientation, size and contour can be retrieved [37]; the "
        "recovery of the applied force profiles was, however, not reported."))
    b.append(fig(11, F.fig(11), "en"))

    b.append(h3("25.3.5 Photoelastic", "Quang đàn hồi"))
    b.append(p(
        "An emerging technology in optical tactile sensing is the photoelastic transducer. When a light "
        "ray propagates into an optically anisotropic medium it splits into two rays that are linearly "
        "polarised at right angles to each other and propagate at different velocities. This splitting "
        "results from a physical property of crystalline material called <i>optical birefringence</i>, or "
        "simply <i>birefringence</i>. The direction in which light propagates with the higher velocity is "
        "the <i>fast axis</i>; the one in which it propagates more slowly is the <i>slow axis</i>. Some "
        "optically isotropic materials — glass, celluloid, bakelite and transparent plastics in general — "
        "become birefringent when subjected to a stress field, and the effect lasts only while the loads "
        "are applied. The phenomenon is therefore called temporary or artificial birefringence, or more "
        "commonly the photoelastic phenomenon."))
    b.append(p(
        "Figure 25.12(a) shows a photoelastic transducer proposed in [38]. It consists of a fully "
        "supported two-layer beam with a mirrored surface sandwiched in between. Normal line forces are "
        "applied to the top surface at discrete tactels separated by equal distances s along the beam. "
        "The upper compliant layer protects the mirror; the lower one is the photoelastic layer."))
    b.append(p(
        "Circularly polarised monochromatic light, incident along the z-axis, illuminates the bottom "
        "surface. It propagates parallel to z, passes through the photoelastic layer and reflects back "
        "from the mirror. With no force applied the returning light is circularly polarised, because "
        "unstressed photoelastic material is isotropic. With force applied, stresses are induced in the "
        "photoelastic layer and make the material birefringent, introducing a phase difference between "
        "the components of the electric field associated with the light-wave propagation. The two "
        "directions of polarisation lie in the plane perpendicular to the direction of propagation — the "
        "x–y plane. The output light is consequently elliptically polarised, creating a phase-difference "
        "distribution p between the input and the output light at each point of the x–y plane, and that "
        "distribution carries the information of the force distribution applied to the transducer."))
    b.append(p(
        "A polariscope is a practical way to observe the spatial variation of light intensity — the "
        "fringes — produced by the induced phase-difference distribution. Polariscopes can be linear or "
        "circular depending on the required polarisation, and reflective or transparent depending on "
        "whether the photoelastic transducer reflects or transmits the light."))
    b.append(p(
        "A circular reflective polariscope, shown in Figure 25.12(b), is used to illuminate the "
        "transducer of Figure 25.12(a). The input light is linearly polarised and directed towards the "
        "photoelastic transducer by a beam splitter; before reaching the transducer it is circularly "
        "polarised by a quarter-wave plate. The output light is elliptically polarised when a force is "
        "applied, and is directed towards a detector through the quarter-wave plate, the beam splitter "
        "and an analyser. It is finally detected by a camera linked to a frame grabber connected to a PC "
        "for further data processing. The light illuminating the camera consists of a set of fringes from "
        "which the force distribution applied to the transducer must be recovered; a technique for that "
        "recovery is described in [38], and a model of the transducer using FEA is reported in [39]."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "One of the earlier applications of photoelasticity to tactile sensing dates back to the "
        "development of the Utah/MIT dexterous hand [40]. Those researchers proposed the photoelastic "
        "phenomenon as a transduction method for recovering the force profile applied to the fingers of "
        "the hand, limiting their application to a single-touch transducer although they claimed that an "
        "array of such devices could be implemented; building a large array of their devices would, "
        "however, be difficult. To overcome that difficulty another group proposed a different transducer "
        "[41]. Although an analytical model was developed for the sensor, a systematic method for "
        "recovering the two-dimensional force profile from the light intensity distribution was not "
        "reported, so the sensor was used mainly for forward analysis — observing the light intensity "
        "distribution for different touching objects brought into contact with the sensor. It could "
        "eventually be used for determining some simple geometric properties of a touching object."))
    b.append(p(
        "A tactile sensor reported in [42] is capable of detecting slippage. The output light intensity — "
        "the fringe pattern — is captured by a camera interfaced to a PC. When an object moves across the "
        "surface of the transducer the intensity distribution changes, and direct analysis of the fringes "
        "is used to detect the movement of the grasped object; a special technique was reported to "
        "optimise the comparison for detecting differences between two fringe patterns arising from "
        "slippage of the object in contact with the sensor [42]. Such analysis does not require the "
        "recovery of the applied force profile."))
    b.append(p(
        "Photoelasticity offers several attractive properties for tactile sensors: good linearity, "
        "compatibility with vision-based sensing technologies and the high spatial resolution associated "
        "with them, which could lead to the high-resolution tactile imagers needed for object recognition "
        "and fine manipulation. Photoelastic sensors are also compatible with fibre optic technology, "
        "which allows the electronic processing devices to be located remotely and avoids interference "
        "problems."))
    b.append(p(
        "Other technologies for tactile sensing include acoustic, magnetic and microcavity vacuum sensors "
        "[43, 44]."))

    b.append(note(
        "<b>Translator’s note.</b> (1) Equation 25.2 is printed in the source with the denominator "
        "<i>πrE</i>(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>; the <i>r</i> is very probably a "
        "typographical error, since both the dimensions and the standard Boussinesq plane-strain kernel "
        "require <i>πE</i>(x<sup>2</sup> + d<sup>2</sup>)<sup>2</sup>. It is reproduced here as printed. "
        "(2) In Section 25.3.3 the source reads “the force applied to the photoelastic material”, "
        "evidently a slip for piezoelectric material; it has been corrected. (3) Equation 25.13 is "
        "printed in the source with the term Δh/h<sub>0</sub> repeated; only one occurrence is kept here. "
        "(4) The source’s “3 mm CMOS process” is almost certainly 3 µm; it is left as printed."))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "[1] P. Dario, Contact sensing for robot active touch, in <i>Robotic Science</i>, M. Brady (ed.), "
        "Cambridge, MA: MIT Press, 1989, chap. 3, 138–163.",
        "[2] P. P. L. Regtien, Tactile imaging, <i>Sensors and Actuators, A</i>, 31, 83–89, 1992.",
        "[3] R. A. Russell, <i>Robot Tactile Sensing</i>, Brunswick, Australia: Prentice-Hall, 1990.",
        "[4] A. D. Berger and P. K. Khosla, Using tactile data for real-time feedback, <i>Int. J. "
        "Robotics Res.</i>, 10(2), 88–102, 1991.",
        "[5] S. Begej, Planar and finger-shaped optical tactile sensors for robotic applications, "
        "<i>IEEE J. Robotics Automation</i>, 4, 472–484, 1988.",
        "[6] R. A. Russell and S. Parkinson, Sensing surface shape by touch, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, Atlanta, GA, 1993, 423–428.",
        "[7] R. D. Howe, A tactile stress rate sensor for perception of fine surface features, <i>IEEE "
        "Int. Conf. Solid-State Sensors Actuators</i>, San Francisco, CA, 1991, 864–867.",
        "[8] S. Sugiyama, K. Kawahata, H. Funabashi, M. Takigawa, and I. Igarashi, A 32 × 32 "
        "(1K)-element silicon pressure-sensor array with CMOS processing circuits, <i>Electron. Commun. "
        "Japan</i>, 75(1), 64–76, 1992.",
        "[9] J. S. Son, E. A. Monteverde, and R. D. Howe, A tactile sensor for localizing transient "
        "events in manipulation, <i>IEEE Int. Conf. Robotics Automation</i>, San Diego, CA, 1994, "
        "471–476.",
        "[10] M. R. Tremblay and M. R. Cutkosky, Estimating friction using incipient slip sensing during "
        "manipulation task, <i>IEEE Int. Conf. Robotics Automation</i>, Atlanta, GA, 1993, 429–434.",
        "[11] S. Omata and Y. Terubuna, New tactile sensor like the human hand and its applications, "
        "<i>Sensors and Actuators, A</i>, 35, 9–15, 1992.",
        "[12] R. Bayrleithner and K. Komoriya, Static friction coefficient determination by force sensing "
        "and its applications, <i>IROS’94</i>, Munich, Germany, 1994, 1639–1646.",
        "[13] M. A. Abidi and R. C. Gonzales, The use of multisensor data for robotic applications, "
        "<i>IEEE Trans. Robotics Automation</i>, 6, 159–177, 1990.",
        "[14] A. A. Cole, P. Hsu, and S. S. Sastry, Dynamic control of sliding by robot hands for "
        "regrasping, <i>IEEE Trans. Robotics Automation</i>, 8, 42–52, 1992.",
        "[15] P. K. Allen and P. Michelman, Acquisition and interpretation of 3-D sensor data from touch, "
        "<i>IEEE Trans. Robotics Automation</i>, 6, 397–404, 1990.",
        "[16] H. R. Nicholls (ed.), <i>Advanced Tactile Sensing for Robotics</i>, Singapore: World "
        "Scientific Publishing, 1992.",
        "[17] J. G. Webster (ed.), <i>Tactile Sensors for Robotics and Medicine</i>, New York: John Wiley "
        "&amp; Sons, 1988.",
        "[18] R. S. Fearing, Tactile sensing mechanism, <i>Int. J. Robotics Res.</i>, 9(3), 3–23, 1990.",
        "[19] T. H. Speeter, Three-dimensional finite element analysis of elastic continua for tactile "
        "sensing, <i>Int. J. Robotics Res.</i>, 11(1), 1–19, 1992.",
        "[20] Y. C. Pati, P. S. Krishnaprasad, and M. C. Peckerar, An analog neural network solution to "
        "the inverse problem of early taction, <i>IEEE Trans. Robotics Automation</i>, 8(2), 196–212, "
        "1992.",
        "[21] L. D. Harmon, Automated tactile sensing, <i>Int. J. Robotics Res.</i>, 1(2), 3–32, 1982.",
        "[22] W. E. Snyder and J. St. Clair, Conductive elastomers as a sensor for industrial parts "
        "handling equipment, <i>IEEE Trans. Instrum. Meas.</i>, 27(1), 94–99, 1991.",
        "[23] M. Shimojo, M. Ishikawa, and K. Kanaya, A flexible high resolution tactile imager with "
        "video signal output, <i>IEEE Int. Conf. Robotics Automation</i>, Sacramento, CA, 1991, 384–391.",
        "[24] W. D. Hillis, A high resolution imaging touch sensor, <i>Int. J. Robotic Res.</i>, 1(2), "
        "33–44, 1982.",
        "[25] Y. Yamada and M. R. Cutkosky, Tactile sensor with 3-axis force and vibration sensing "
        "functions and its applications to detect rotational slip, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, San Diego, CA, 1994, 3550–3557.",
        "[26] K. Njafi and C. H. Mastrangelo, Solid-state microsensors and smart structure, "
        "<i>Ultrasonic Symp.</i>, Baltimore, MD, 1993, 341–350.",
        "[27] F. Zhu and J. W. Spronck, A capacitive tactile sensor for shear and normal force "
        "measurements, <i>Sensors and Actuators, A</i>, 31, 115–120, 1992.",
        "[28] K. Suzuki, K. Najafi, and K. D. Wise, A 1024-element high-performance silicon tactile "
        "imager, <i>IEEE Trans. Electron Devices</i>, 17(8), 1852–1860, 1990.",
        "[29] M. R. Wolffenbuttel and P. L. Regtien, The accurate measurement of a micromechanical force "
        "using force-sensitive capacitances, <i>Conf. Precision Electromagnetic Meas.</i>, Boulder, CO, "
        "1994, 180–181.",
        "[30] M. R. Wolffenbuttel, R. F. Wolffenbuttel, and P. P. L. Regtien, An integrated charge "
        "amplifier for a smart tactile sensor, <i>Sensors and Actuators, A</i>, 31, 101–109, 1992.",
        "[31] E. D. Kolesar, Jr. and C. S. Dyson, Object imaging with piezoelectric robotic tactile "
        "sensor, <i>J. Microelectromechanical Syst.</i>, 4(2), 87–96, 1995.",
        "[32] J. L. Scheiter and T. B. Sheridan, An optical tactile sensor for manipulators, <i>J. Robot "
        "Computer-Integrated Manufacturing</i>, 1, 65–71, 1989.",
        "[33] R. Ristic, B. Benhabib, and A. A. Goldenberg, Analysis and design of a modular "
        "electrooptical tactile sensor, <i>IEEE Trans. Robotics Automation</i>, 5(3), 362–368, 1989.",
        "[34] H. Maekawa, K. K. Tanie, K. Komoriya, M. Kaneko, C. Horiguchi, and T. Sugawara, Development "
        "of a finger shaped tactile sensor and its evaluation by active touch, <i>IEEE Int. Conf. "
        "Robotics Automation</i>, Nice, France, 1992, 1327–1334.",
        "[35] M. Ohka, Y. Mitsurya, S. Takeuchi, and O. Kamekawa, A three-axis optical tactile sensor "
        "(FEM contact analyses and sensing experiments using a large-sized tactile sensor), <i>IEEE Int. "
        "Conf. Robotics Automation</i>, Nagoya, Aichi, Japan, 1995, 817–824.",
        "[36] J. Rebman and K. A. Morris, A tactile sensor with electro-optical transduction, in "
        "<i>Robots Sensors, Tactile and Non-Vision</i>, Vol. 2, A. Pugh (ed.), EFS Publications, 1986, "
        "145–155.",
        "[37] S. R. Emge and C. L. Chen, Two dimensional contour imaging with a fiber optic microbend "
        "tactile sensor array, <i>Sensors and Actuators, B</i>, 3, 31–42, 1991.",
        "[38] R. E. Saad, A. Bonen, K. C. Smith, and B. Benhabib, Distributed-force recovery for a planar "
        "photoelastic tactile sensor, <i>IEEE Trans. Instrum. Meas.</i>, 45, 541–546, 1996.",
        "[39] R. E. Saad, A. Bonen, K. C. Smith, and B. Benhabib, Finite-element analysis for photoelastic "
        "tactile sensors, <i>Proc. IEEE Int. Conf. Industrial Electronics, Control, and "
        "Instrumentation</i>, Orlando, FL, 1995, 1202–1207.",
        "[40] S. C. Jacobsen, J. E. Wood, D. F. Knutti, and B. Biggers, The Utah/MIT dexterous hand: work "
        "in progress, in <i>Robotics Research: The First International Symposium</i>, M. Brady and "
        "R. Paul (eds.), Cambridge: MIT Press, 1983, 601–653.",
        "[41] A. Cameron, R. Daniel, and H. Durrant-Whyte, Touch and motion, <i>IEEE Int. Conf. Robotics "
        "Automation</i>, Philadelphia, PA, 1988, 1062–1067.",
        "[42] S. H. Hopkins, F. Eghtedari, and D. T. Pham, Algorithms for processing data from a "
        "photoelastic slip sensor, <i>Mechatronics</i>, 2(1), 15–28, 1992.",
        "[43] S. Ando and H. Shinoda, Ultrasonic emission tactile sensing, <i>IEEE Trans. Control "
        "Syst.</i>, 15(1), 61–69, 1996.",
        "[44] J. C. Jiang, V. Faynberg, and R. C. White, Fabrication of micromachined silicon tip "
        "transducer for tactile sensing, <i>J. Vacuum Sci. Technol., B</i>, 11, 1962–1967, 1993.",
    ]))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 25 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 25 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 25 “Cảm biến xúc giác” của R. E. Saad, A. Bonen, K. C. Smith và "
            "B. Benhabib (Đại học Toronto) — phân loại cảm biến tiếp xúc, lý thuyết giản lược về ứng "
            "suất và biến dạng trong lớp mềm dẻo, yêu cầu kỹ thuật của cảm biến xúc giác, và năm công "
            "nghệ chuyển đổi: điện trở, điện dung, áp điện, quang và quang đàn hồi, với 12 hình và 19 "
            "phương trình." if vi
            else
            "Companion to Chapter 25 of the CRC Measurement Handbook — tactile sensing: sensing "
            "classification, the mechanical effects of contact, the simplified one-dimensional elastic "
            "half-space theory, requirements for tactile sensors, and five transduction technologies — "
            "resistive, capacitive, piezoelectric, optical and photoelastic.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 25' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 25' % BASE_EN)
    meta = ("Chương 25 · theo Ch25.pdf (CRC Press, 1999) · 12 hình, 19 phương trình, 44 tài liệu tham "
            "khảo" if vi else
            "Chapter 25 · 12 figures, 19 equations, 44 references")
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
