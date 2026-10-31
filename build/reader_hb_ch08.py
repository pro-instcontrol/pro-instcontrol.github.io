# -*- coding: utf-8 -*-
"""Handbook Chapter 8 — Proximity Sensing for Robotics (Saad, Bonen, Smith, Benhabib).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch08.py
"""
import os

import hb8fig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch08-proximity-sensing-for-robotics"
TITLE_EN = "Proximity Sensing for Robotics"
TITLE_VI = "Cảm biến tiệm cận cho rô bốt"
BYLINE = "R. E. Saad · A. Bonen · K. C. Smith · B. Benhabib · University of Toronto"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-8-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap))


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


def quote(text, src):
    return '<div class="pullquote"><p>%s</p><span class="src">%s</span></div>' % (text, src)


def note(text):
    return '<div class="note">%s</div>' % text


def table(headers, rows, caption, cls=""):
    th = "".join("<th>%s</th>" % h for h in headers)
    body = []
    for r in rows:
        if isinstance(r, str):
            body.append('<tr class="grp"><td colspan="%d">%s</td></tr>' % (len(headers), r))
        else:
            body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p class="tblcap">%s</p>' % (cls, th, "".join(body), caption))


def reflist(items):
    out = ['<h3 class="refs-h">Tài liệu tham khảo</h3><ol class="reflist">']
    for it in items:
        out.append("<li>%s</li>" % it)
    out.append("</ol>")
    return "".join(out)


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Mục tiêu của chương này là điểm lại trình độ hiện tại của các công nghệ cảm biến tiệm cận dùng "
        "cho rô bốt. Trọng tâm được dành cho nhu cầu cảm nhận của các tay máy rô bốt trong bài toán gắp "
        "vật, khác với nhu cầu của rô bốt di động trong bài toán định vị và di chuyển. Bạn đọc muốn xem "
        "phần điểm lại ứng dụng cảm biến tiệm cận cho rô bốt di động xin xem tài liệu [1]."))

    b.append(p(
        "Cảm biến dùng cho rô bốt có thể chia thành ba nhóm: cảm biến tầm trung (nhận dạng vật thể và "
        "ước lượng thô vị trí, hướng), cảm biến tầm ngắn (tiệm cận), và cảm biến tiếp xúc. Các công "
        "trình gần đây [2–6] cho rằng cơ cấu tác động cuối của rô bốt nên được trang bị đồng thời cả cảm "
        "biến tiệm cận tầm ngắn lẫn cảm biến tiếp xúc."))

    b.append(p(
        "Cảm biến tiệm cận phải đo được vị trí và hướng — tức tư thế — của bề mặt vật thể. Dải đo phải "
        "đủ lớn để bù cho những bất định của bước ước lượng tư thế tầm trung, đồng thời vẫn giữ được độ "
        "chính xác đủ để gắp vật một cách hiệu quả."))

    b.append(p(
        "Các đầu đo mà cảm biến tiệm cận hiện nay sử dụng rất khác nhau về mức độ tinh xảo. Tuy vậy, dù "
        "đa dạng đến đâu, bản thân các đầu đo này cùng mạch giao diện điện tử đi kèm — hợp lại thành cảm "
        "biến tiệm cận — hiện vẫn chưa đáp ứng được những yêu cầu khắt khe về độ bền vững của phần lớn "
        "ứng dụng rô bốt công nghiệp. Vẫn còn phải phát triển những thuật toán và kỹ thuật cảm nhận mới "
        "để cải thiện các đặc tính hiện có, và hơn nữa, để điều khiển được cả quá trình cảm nhận lẫn quá "
        "trình gắp."))

    # ------------------------------------------------------------ 8.1
    b.append(h2("8.1 Định nghĩa tiệm cận", "Proximity Definition"))

    b.append(p(
        "Thuật ngữ “tiệm cận”, được định lượng bằng “tư thế” trong chương này, quy về ba tham số hình học "
        "x, u và v như trên Hình 8-1, trong đó:"))

    b.append(fig(1, hb8fig.fig_8_1()))

    b.append("<ul>"
             "<li><strong>x</strong> — khoảng dịch từ gốc hệ quy chiếu của cảm biến, F<sub>p</sub>, tới "
             "một điểm đích trên bề mặt vật thể, đo dọc theo X<sub>p</sub>. Điểm đích này xác định gốc "
             "của hệ quy chiếu bề mặt F<sub>r</sub>.</li>"
             "<li><strong>u</strong> — hướng thẳng đứng của bề mặt vật thể, định nghĩa là phép quay quanh "
             "Y<sub>p</sub> (của hệ đã dịch), qua đó xác định trục Z<sub>r</sub> mới.</li>"
             "<li><strong>v</strong> — hướng nằm ngang của bề mặt vật thể, định nghĩa là phép quay quanh "
             "Z<sub>r</sub>, qua đó xác định trục Y<sub>r</sub>.</li>"
             "</ul>")

    # ------------------------------------------------------------ 8.2
    b.append(h2("8.2 Đặc tính điển hình của cảm biến", "Typical Sensor Characteristics"))

    b.append(p(
        "Theo thông lệ, cảm biến tiệm cận phải đo được khoảng cách tới 50 mm và đo được hướng theo hai "
        "bậc tự do, tương đương một độ nghiêng tổng cộng tới ±30°. Ứng dụng chính mà cảm biến nhắm tới là "
        "đóng vai trò dẫn hướng cho rô bốt. Vì vậy, điều mong muốn là độ nhạy và độ chính xác càng cao "
        "khi tay gắp càng tới gần vật — nghĩa là khi cả hướng tương đối lẫn khoảng cách đều tiến về giá "
        "trị không."))

    b.append(p(
        "Các tín hiệu mà mạch giao diện điện tử nhận được phải được xử lý mà không làm hẹp dải làm việc "
        "yêu cầu của cảm biến. Mạch giao diện cũng phải giảm thiểu ảnh hưởng của nhiễu từ môi trường "
        "xung quanh. Do đó mạch phải dùng các giải pháp nhằm giảm nhiễu nền và khắc phục giới hạn dải "
        "động."))

    b.append(p(
        "Hoạt động của rô bốt không được chậm đi vì cảm biến. Cụ thể, tư thế của vật thường phải được ước "
        "lượng trong khoảng 1 ms đến 10 ms."))

    # ------------------------------------------------------------ 8.3
    b.append(h2("8.3 Các công nghệ cảm biến tiệm cận",
                "Technologies for Proximity Sensing"))

    b.append(p(
        "Cảm biến tiệm cận đã dùng nhiều môi trường truyền khác nhau: sóng âm, từ trường, điện trường và "
        "ánh sáng. Hiện nay, kỹ thuật quang điện có vẻ là phù hợp nhất cho các ứng dụng gắp vật bằng rô "
        "bốt. Loại cảm biến này có kích thước tương đối nhỏ, dải làm việc rộng và hầu như không đặt ra "
        "ràng buộc nào về vật liệu của vật thể. Tuy nhiên, gần đây một số cảm biến tiệm cận siêu âm và "
        "điện dung kiểu mới đã được chế tạo trực tiếp dưới dạng vi mạch tích hợp, cho thấy khả năng tạo "
        "ra cảm biến tiệm cận kích thước rất nhỏ dựa trên các công nghệ này [7, 8]."))

    b.append(p(
        "Dưới đây là mô tả vắn tắt nguyên lý của những công nghệ chủ yếu được cảm biến tiệm cận sử dụng, "
        "trong đó trọng tâm là các đầu đo quang học. Bạn đọc có thể tìm thấy một khảo sát các cảm biến "
        "tiệm cận thương mại có khả năng đo khoảng cách trong tài liệu [6]."))

    # ------------------------------------------------------------ electro-optical
    b.append(h3("Cảm biến quang điện", "Electro-Optical Sensors"))

    b.append(p(
        "Nhiều cảm biến tiệm cận dùng ánh sáng tán xạ trực tiếp từ bề mặt vật đích để xác định khoảng "
        "cách và hướng của vật so với tay gắp. Cơ chế phản xạ ánh sáng có thể được giải thích bằng một "
        "mô hình nêu ra bốn hiện tượng phản xạ khác nhau. Theo mô hình này, ánh sáng phản xạ từ bề mặt "
        "chủ yếu là kết quả của một hoặc nhiều tương tác sau:"))

    b.append("<ol>"
             "<li><em>Phản xạ bề mặt đơn</em> — sóng ánh sáng phản xạ gương một lần trên một vi mặt "
             "phẳng có kích thước lớn hơn bước sóng đáng kể.</li>"
             "<li><em>Phản xạ bề mặt bội</em> — sóng ánh sáng phản xạ gương ít nhất hai lần trên nhiều "
             "vi mặt phẳng.</li>"
             "<li><em>Phản xạ sau khi xuyên nhập</em> — sóng ánh sáng xuyên vào vật liệu, khúc xạ, rồi "
             "phản xạ trở ra dưới dạng ánh sáng tán xạ.</li>"
             "<li><em>Phản xạ góc cạnh</em> — sóng ánh sáng nhiễu xạ từ các mặt phân cách có chi tiết bề "
             "mặt cỡ bước sóng hoặc nhỏ hơn (chẳng hạn từ các góc cạnh của vi mặt phẳng).</li>"
             "</ol>")

    b.append(p(
        "Hiện tượng chủ yếu (1) thường có mặt ở cả điện môi lẫn kim loại. Tuy nhiên, do độ dẫn điện cao "
        "của bề mặt kim loại, phần lớn ánh sáng phản xạ gương ngay tại mặt phân cách giữa kim loại và "
        "không khí, còn phần xuyên vào bề mặt kim loại thì bị hấp thụ. Theo đó, cường độ phản xạ bắt "
        "nguồn từ phản xạ nội trong kim loại thực tế bằng không. Ở điện môi thì ngược lại: một phần lớn "
        "ánh sáng xuyên vào bề mặt rồi phản xạ trở ra thành ánh sáng tán xạ (3). Các hiện tượng thứ cấp "
        "(2) và (4) có mặt ở cả kim loại lẫn điện môi, và cộng thêm vào hệ số phản xạ tán xạ."))

    b.append(p(
        "Các kỹ thuật đo thông dụng trong cảm biến tiệm cận quang học sử dụng một hoặc nhiều thành phần "
        "phản xạ nói trên để xác định tư thế của vật so với đầu đo."))

    # ---- phase modulation
    b.append(p(
        "<strong>Điều chế pha.</strong> Cảm biến tiệm cận điều chế pha (PM) thường gồm hai nguồn sáng và "
        "một hoặc nhiều bộ thu quang. Hai nguồn sáng được điều khiển bằng hai tín hiệu sin có quan hệ pha "
        "90° (Hình 8-2). Điện áp điều khiển các bộ phát, V<sub>em1</sub> và V<sub>em2</sub>, lần lượt có "
        "biên độ a và b:"))

    b.append(eq("V<sub>em1</sub>(t) = a · cos ωt", "8.1"))
    b.append(eq("V<sub>em2</sub>(t) = b · sin ωt", "8.2"))

    b.append(fig(2, hb8fig.fig_8_2()))

    b.append(p(
        "Tín hiệu mà bộ thu nhận được là chồng chập của hai tín hiệu phản xạ, với các suy giảm tương ứng "
        "là A và B:"))

    b.append(eq("V<sub>rec</sub>(t) = A · V<sub>em1</sub> + B · V<sub>em2</sub>", "8.3"))

    b.append(p(
        "Độ suy giảm tín hiệu là hàm của các tham số hình học và điện của cảm biến, của đặc tính phản xạ "
        "bề mặt vật, và của khoảng cách cùng hướng của bề mặt so với cảm biến. Tín hiệu tổng hợp tại bộ "
        "thu do đó là:"))

    b.append(eq("V<sub>rec</sub>(t) = M · sin(ωt + φ)", "8.4"))

    b.append(p(
        "trong đó M là hàm suy giảm tổng hợp, và φ là độ lệch pha tổng hợp."))

    b.append(p(
        "Thông thường người ta chỉ dùng thông tin pha φ, còn biên độ bị bỏ qua hoàn toàn hoặc chỉ dùng "
        "để kiểm tra khả năng có lỗi và độ lớn tiềm tàng của lỗi đó."))

    b.append(p(
        "Một cảm biến tiệm cận dùng kỹ thuật này đã được báo cáo trong [9]. Hình 8-3 cho thấy đầu đo của "
        "nó: sáu nguồn sáng LED và một bộ thu quang (một phototransistor). Cảm biến này đo được khoảng "
        "cách từ hệ quy chiếu của cảm biến tới điểm đích trên bề mặt vật (x), cũng như hướng ngang và "
        "hướng thẳng đứng của bề mặt vật (u, v)."))

    b.append(fig(3, hb8fig.fig_8_3()))

    b.append(p(
        "Một mô hình đơn giản cho cảm biến đã được xây dựng với giả thiết rằng các nguồn sáng (LED) có "
        "độ định hướng thấp, bộ thu quang (phototransistor) có độ định hướng cao, và bề mặt có tính phản "
        "xạ tán xạ. Hình 8-4 trình bày cấu hình cơ bản để đo khoảng cách (x) và hướng (u và v). Bảng 8-1 "
        "cho thấy các tổ hợp tín hiệu điều khiển trên từng LED cần thiết cho phép đo khoảng cách và "
        "hướng."))

    b.append(fig(4, hb8fig.fig_8_4()))

    b.append(p(
        "Để đo khoảng cách x, LED1 và LED3 được điều chế bằng K<sub>1</sub>sin ωt, còn LED2 và LED4 bằng "
        "K<sub>2</sub>cos ωt. Độ sáng mà bộ thu quang nhận được có thể tính được (dùng định luật "
        "Lambert) là:"))

    b.append(eq(
        "L<sub>p</sub> = C [ G<sub>1</sub>·cos(α − v)/(a² + x²) + G<sub>2</sub>·cos(β − v)/(b² + x²) "
        "+ G<sub>3</sub>·cos(α + v)/(a² + x²) + G<sub>4</sub>·cos(β + v)/(b² + x²) ]", "8.5"))

    b.append(p(
        "trong đó G<sub>i</sub> (i = 1, 2, 3, 4) là cường độ của các nguồn sáng, và C là hệ số phản xạ "
        "của bề mặt tại điểm P. Xét trường hợp này: G<sub>1</sub> = G<sub>3</sub> = K<sub>1</sub>sin ωt, "
        "G<sub>2</sub> = G<sub>4</sub> = K<sub>2</sub>cos ωt, cos α = x/√(a² + x²) và cos β = x/√(b² + x²). "
        "Khi đó phương trình 8.5 có thể viết lại thành:"))

    b.append(eq(
        "L<sub>p</sub> = 2Cx [ K<sub>1</sub>·sin ωt/(a² + x²)<sup>3/2</sup> + "
        "K<sub>2</sub>·cos ωt/(b² + x²)<sup>3/2</sup> ] · cos v = M · sin(ωt + φ<sub>x</sub>)", "8.6"))

    b.append(p("Biên độ M và độ lệch pha φ<sub>x</sub> cho bởi:"))

    b.append(eq(
        "M = 2Cx [ K<sub>1</sub>²/(a² + x²)³ + K<sub>2</sub>²/(b² + x²)³ ]<sup>1/2</sup> · cos v", "8.7"))

    b.append(p("và"))

    b.append(eq(
        "φ<sub>x</sub> = tan<sup>−1</sup> { [ K<sub>2</sub>(a² + x²)<sup>3/2</sup> ] / "
        "[ K<sub>1</sub>(b² + x²)<sup>3/2</sup> ] }", "8.8"))

    b.append(p(
        "Từ phương trình 8.8 có thể thấy rằng khoảng cách (x) suy ra được từ φ<sub>x</sub>. Điều quan "
        "trọng là về lý thuyết, phép tính không chịu ảnh hưởng của hệ số phản xạ (C) của bề mặt."))

    b.append(p(
        "Tương tự, các góc hướng u và v có thể thu được bằng cách điều khiển các LED theo Bảng 8-1. Ví "
        "dụ, v có thể xác định bằng cách điều chế LED4 và LED2 lần lượt bằng các tín hiệu "
        "K<sub>1</sub>sin ωt và K<sub>2</sub>cos ωt. Trong trường hợp này, độ lệch pha gắn với độ sáng "
        "của vật tại điểm P là:"))

    b.append(eq(
        "φ<sub>v</sub> = tan<sup>−1</sup> { tan[ K<sub>2</sub>x/(b − v) ] / "
        "tan[ K<sub>1</sub>x/(b + v) ] }", "8.9"))

    b.append(note(
        "Phương trình 8.9 trong bản gốc bị lỗi quét nặng: phần trong dấu ngoặc móc bị đảo thứ tự và mất "
        "dấu. Cách viết trên đây là cách khôi phục hợp lý duy nhất giữ được tính đối xứng với phương "
        "trình 8.8 — tử số ứng với LED2 (hệ số K<sub>2</sub>, phía b − v) và mẫu số ứng với LED4 (hệ số "
        "K<sub>1</sub>, phía b + v). Độc giả nên đối chiếu với bản in gốc trước khi dùng công thức này "
        "để tính toán."))

    b.append(p(
        "Lưu ý rằng để rút v ra từ phương trình 8.9 thì phải biết x. Theo đó, khoảng cách x phải được xác "
        "định trước. Tương ứng, góc hướng (v) sau đó được tính từ độ lệch pha mới φ<sub>v</sub>. Góc u "
        "có thể tính được bằng cách điều chế LED6 và LED5 lần lượt bằng K<sub>1</sub>sin ωt và "
        "K<sub>2</sub>cos ωt, rồi xác định độ lệch pha tương ứng của độ sáng tại điểm P."))

    b.append(p(
        "Kết quả ước lượng tư thế bằng cảm biến này khá tốt và cho thấy sự phù hợp giữa lý thuyết và thực "
        "nghiệm."))

    b.append(p(
        "Trong [10], một thiết bị thí nghiệm cho cảm biến khoảng cách điều chế pha, tương tự cảm biến "
        "trong [9], đã được báo cáo nhằm khảo sát ảnh hưởng của các tham số hình học và điện lên hiệu "
        "năng của cảm biến. Các tham số tối ưu đã thu được cho một số đặc tính hoạt động nhắm tới của cảm "
        "biến."))

    # ---- amplitude modulation
    b.append(p(
        "<strong>Điều chế biên độ.</strong> Ở cảm biến điều chế biên độ (AM), độ lớn ánh sáng phản xạ từ "
        "bề mặt được dùng để xác định tư thế của vật."))

    b.append(fig(5, hb8fig.fig_8_5()))

    b.append(p(
        "Đầu đo AM thường gồm một nguồn sáng và vài bộ thu quang (Hình 8-5). Chúng đã được thiết kế lại "
        "và tối ưu hoá nhiều lần trong thập kỷ qua để đạt độ chính xác đo tốt hơn [11–14]."))

    b.append(p(
        "Nhiều cảm biến tiệm cận AM dùng sợi quang để chiếu sáng và thu ánh sáng từ bề mặt vật. Việc dùng "
        "sợi quang theo cấu hình dẫn Y (Hình 8-6) tạo thuận lợi cho mạch điện nhạy, độ nhiễu thấp làm "
        "việc trong môi trường được che chắn, cách xa các nguồn nhiễu điện từ của rô bốt."))

    b.append(fig(6, hb8fig.fig_8_6()))

    b.append(p(
        "Đầu đo AM chủ yếu dùng các biến thể của đầu đo dẫn Y cơ bản. Có hai tham số quan trọng có thể "
        "thay đổi khi thiết kế dẫn Y: khoảng cách d giữa sợi phát và sợi thu (từ đây gọi lần lượt là bộ "
        "phát và bộ thu), và góc nghiêng ϑ của sợi thu so với mặt phẳng của đầu đo. Bộ phát thường được "
        "đặt vuông góc với mặt phẳng đầu đo do yêu cầu về tính đối xứng, như sẽ giải thích ở phần sau "
        "của mục này."))

    b.append(p(
        "Để thu được đủ lượng ánh sáng phản xạ, phải dùng sợi có đường kính tương đối lớn, thường có lõi "
        "từ 0,3 mm đến 2 mm. Yêu cầu này buộc phải dùng loại sợi nhựa có phẩm cấp tương đối thấp. Tuy "
        "suy hao tới 1 dB·m⁻¹ là phổ biến ở loại sợi nhựa này, mức suy hao đó tương đối không đáng kể với "
        "ứng dụng dẫn Y vì cáp thường dùng rất ngắn. Mặt khác, khẩu độ số (NA) của sợi nhựa lại là một "
        "tham số quan trọng trong thiết kế đầu đo, vì thấu kính hiếm khi được dùng kèm với đầu đo kiểu "
        "AM. Cụ thể, góc thu nhận của sợi là cố định và cho bởi α = 2·sin<sup>−1</sup>(NA)."))

    b.append(p(
        "Với một dẫn Y, cường độ ánh sáng phản xạ từ bề mặt không phải là hàm đơn điệu của khoảng cách. "
        "Do đó khoảng cách làm việc nhỏ nhất của đầu đo (x<sub>min</sub>) thường bị giới hạn ở một giá "
        "trị bảo đảm đáp ứng đơn điệu (Hình 8-7)."))

    b.append(fig(7, hb8fig.fig_8_7()))

    b.append(p(
        "Để đo hướng của bề mặt, có thể dùng một tổ hợp ba sợi đối xứng (Hình 8-8). Trong cấu hình dẫn Y "
        "này, bộ phát nằm ở giữa còn hai bộ thu được đặt đối xứng hai bên [12]. Cường độ ánh sáng mà các "
        "bộ thu nhận được, với đầu đo trên Hình 8-8, được minh hoạ trên Hình 8-9 như hàm của hướng bề "
        "mặt."))

    b.append(fig(8, hb8fig.fig_8_8()))
    b.append(fig(9, hb8fig.fig_8_9()))

    b.append(p(
        "Trong dải làm việc thông thường của đầu đo AM, cường độ ánh sáng tại bộ thu tỉ lệ nghịch với "
        "bình phương khoảng cách. Do đó, về mặt khái niệm, hoàn toàn có thể cấu hình đầu đo sao cho độ "
        "nhạy và độ chính xác của nó tăng lên khi tay gắp tiến gần điểm tiếp xúc — nơi cả khoảng cách "
        "lẫn hướng của bề mặt vật đều bằng không [10, 12]. Tuy nhiên trên thực tế, vì dải động của giao "
        "diện điện tử có hạn, tồn tại một sự đánh đổi giữa độ chính xác mong muốn gần điểm tiếp xúc và "
        "dải làm việc tối đa. Những điều này cùng các yếu tố khác phải được tính đến khi xác lập các đặc "
        "trưng hình học của đầu đo."))

    b.append(p(
        "Một yếu tố quan trọng khác cần tính đến khi thiết kế cảm biến AM là nhu cầu giảm thiểu, càng "
        "nhiều càng tốt, ảnh hưởng của sự thay đổi công suất phát P<sub>o</sub> của nguồn sáng lên phép "
        "đo của đầu đo. Điều này thường dẫn tới việc dùng một cặp bộ thu. Một sơ đồ ước lượng điện áp vi "
        "phân chuẩn hoá (DV) như sau khi đó được áp dụng cho cặp kết quả đo:"))

    b.append(eq(
        "DV = (V<sub>rec1</sub> − V<sub>rec2</sub>) / (V<sub>rec1</sub> + V<sub>rec2</sub>)", "8.10"))

    b.append(p(
        "trong đó V<sub>rec1</sub> và V<sub>rec2</sub> là các điện áp đo được bởi bộ thu 1 và bộ thu 2. "
        "Tuy nhiên, để loại bỏ ảnh hưởng của P<sub>o</sub> lên DV, mỗi bộ thu phải chuyển đổi tuyến tính "
        "cường độ ánh sáng thành điện áp đo tương ứng."))

    b.append(p(
        "Để dùng sơ đồ DV cho phép đo khoảng cách, có thể dùng một cấu hình đầu đo bất đối xứng (Hình "
        "8-10). Tuy vậy cần lưu ý rằng tuy phép đo hướng không bị ảnh hưởng bởi sự thay đổi khoảng cách, "
        "phép đo khoảng cách lại bị ảnh hưởng đáng kể bởi hướng của bề mặt, xem [15]."))

    b.append(fig(10, hb8fig.fig_8_10()))

    b.append(p(
        "Theo đó, khi dùng cảm biến tiệm cận AM với sơ đồ DV, hướng được ước lượng trước, sau đó mới xác "
        "định khoảng cách. Độ chính xác của khoảng cách và góc hướng đo được có thể được cải thiện thêm "
        "bằng một quá trình lặp."))

    b.append(p(
        "Dựa trên những vấn đề và quan sát nêu trên, đầu ra của ba bộ thu trong cảm biến tiệm cận AM cơ "
        "bản (Hình 8-5) có thể được ghép cặp để đo đồng thời cả khoảng cách lẫn hướng: cặp rec1–rec2 dùng "
        "cho phép đo hướng, còn cặp rec1–rec3 dùng cho phép đo khoảng cách."))

    b.append(p(
        "Một cảm biến tiệm cận AM thực nghiệm, có khả năng ước lượng tư thế của vật với độ chính xác "
        "cao, đã được báo cáo trong [14, 16, 17]. Đầu đo gồm một bộ phát đặt vuông góc với đầu đo và tám "
        "phần tử thu nghiêng (Hình 8-11). Các bộ thu của đầu đo này được ghép cặp cho các phép đo riêng "
        "rẽ về khoảng cách cũng như về hướng thẳng đứng hoặc hướng ngang. Tuy nhiên, tư thế của bề mặt "
        "được xác định với độ chính xác cao hơn bằng một kỹ thuật khớp đa thức (thay cho sơ đồ DV mô tả "
        "ở trên), cho ra các quan hệ giữa từng tham số ước lượng riêng lẻ (x, u và v) với cả tám tín hiệu "
        "thu được."))

    b.append(fig(11, hb8fig.fig_8_11()))

    b.append(p(
        "Cảm biến trình bày trong [14], và được vẽ trên Hình 8-11, làm việc trong dải 0 mm đến 50 mm và "
        "±20°. Nó đạt độ chính xác 6,25 µm về khoảng cách và 0,02° về góc trong vùng gần tiếp xúc (dải "
        "0 mm đến 6 mm), khi dùng chiến lược hiệu chuẩn theo nhóm cho các nhóm vật liệu khác nhau. Điều "
        "này hàm ý rằng vật liệu của vật đo thuộc một nhóm hiệu chuẩn, tức nhóm gồm những vật có đặc "
        "trưng bề mặt tương tự nhau, ví dụ kim loại đã qua gia công cắt gọt. Có thể đạt độ chính xác tốt "
        "hơn nếu dùng chiến lược hiệu chuẩn riêng cho từng bề mặt."))

    b.append(p(
        "Một cấu hình tương tự cấu hình trên Hình 8-11 đã được báo cáo trước đó trong [18] cho phép đo "
        "khoảng cách, trong đó hướng của từng cặp bộ thu so với bộ phát, ϑ<sub>1</sub> và "
        "ϑ<sub>3</sub>, được đặt bằng 10°. Tuy nhiên trong trường hợp này, khẩu độ của bộ phát và bộ thu "
        "bị hạn chế nghiêm ngặt bởi một thấu kính chiết suất biến đổi (GRIN) dùng để chuẩn trực. Đường "
        "kính bộ phát lớn hơn đường kính bộ thu nhằm truyền được nhiều ánh sáng hơn. Các kết quả đo của "
        "đầu đo sau đó được xử lý theo hai giai đoạn: (1) DV của tất cả các cặp bộ thu được xử lý độc "
        "lập để cho ra bốn ước lượng khoảng cách; và (2) bốn ước lượng khoảng cách được lấy trung bình "
        "để cho một ước lượng chính xác hơn, loại bỏ các ảnh hưởng bất lợi do sự thay đổi hướng bề mặt."))

    # ---- geometrical
    b.append(p(
        "<strong>Kỹ thuật hình học.</strong> Cảm biến tiệm cận dựa trên kỹ thuật hình học xác định tư thế "
        "của vật bằng cách khảo sát các thuộc tính hình học của chùm sáng tới và chùm sáng phản xạ. Hai "
        "kỹ thuật trong số đó được trình bày ở đây: một dựa trên tam giác đạc, một dựa trên định luật "
        "thấu kính Gauss."))

    b.append(p(
        "Hình 8-12 cho thấy cấu hình cơ bản của một đầu đo tiệm cận đo khoảng cách (x) dựa trên kỹ thuật "
        "tam giác đạc [19, 20]. Đầu đo gồm một nguồn sáng laser và một dãy tuyến tính các bộ thu quang "
        "(R<sub>i</sub>, với i = 1, 2, …, n). Một chùm sáng hẹp chiếu vào điểm P, và các bộ thu nhận ánh "
        "sáng phản xạ từ điểm được chiếu sáng qua một khe truyền sáng. Hình học của đường đi tia sáng "
        "cung cấp thông tin cơ bản để ước lượng khoảng cách (x). Trong khi nguồn sáng chiếu vào bề mặt "
        "vật, dãy bộ thu quang được quét để tìm đường sáng cho tín hiệu ra cực đại. Đường sáng thu được "
        "bằng cách quét này được gọi là đường sáng hiệu dụng [19]. Đó chính là đường được chỉ ra trên "
        "Hình 8-12. Khoảng cách (x) xác định được nhờ phát hiện chính xác vị trí (y<sub>i</sub>) và đo "
        "chính xác các kích thước (h) và (y<sub>o</sub>):"))

    b.append(eq("x/(x + h) = y<sub>o</sub>/y<sub>i</sub>", "8.11"))
    b.append(p("hay"))
    b.append(eq("x = h·y<sub>o</sub>/(y<sub>i</sub> − y<sub>o</sub>)", "8.12"))

    b.append(fig(12, hb8fig.fig_8_12()))

    b.append(p(
        "Trong [26], người ta khẳng định rằng một cảm biến như vậy có các tính chất sau: (1) ảnh hưởng "
        "của độ không đồng đều, độ phản xạ và hướng của vật là không đáng kể; (2) phép đo khoảng cách "
        "không bị ảnh hưởng bởi ánh sáng chiếu từ môi trường và độ chói của vật (ảnh hưởng của chúng "
        "được loại bỏ bằng cách so sánh hai tín hiệu cảm biến thu được ở hai trạng thái bật và tắt liên "
        "tiếp của nguồn sáng); và (3) đầu đo đủ nhỏ để dùng trong bàn tay rô bốt."))

    b.append(p(
        "Một cấu hình cảm biến tiệm cận thực nghiệm dựa trên tam giác đạc, có khả năng đo cả khoảng cách "
        "lẫn hướng, được trình bày trên Hình 8-13 [21]. Cảm biến dùng sáu LED hồng ngoại làm nguồn sáng, "
        "một thấu kính vật và một chip thu dạng dãy diện tích để phát hiện vị trí vệt sáng. Hướng của "
        "các chùm sáng được căn chỉnh để tạo thành một hình nón sáng cố định. Cảm biến này thuộc loại "
        "gọi là bộ phát quét, vì mỗi LED được phát xung tuần tự để thực hiện phép đo. Khi mỗi LED được "
        "phát xung tuần tự, vi mạch của cảm biến phát hiện vị trí vệt sáng do chùm sáng phản xạ từ bề mặt "
        "vật tạo ra. Biết vị trí vệt sáng, cùng với quang hệ của camera và quỹ đạo của từng chùm sáng, "
        "có thể thực hiện một phép tam giác đạc để xác định toạ độ ba chiều của từng vệt sáng trên bề "
        "mặt đích. Với sáu LED ta thu được một tập sáu điểm ba chiều. Sau đó, bằng cách khớp một mặt "
        "phẳng qua các điểm đó, khoảng cách và hướng của bề mặt vật được xấp xỉ."))

    b.append(fig(13, hb8fig.fig_8_13()))

    b.append(p(
        "Một cảm biến tiệm cận kiểu bộ phát quét khác đã được báo cáo trong [22]. Trong trường hợp đó, "
        "một hệ quét cơ khí đã được dùng. Cần lưu ý rằng những vấn đề cố hữu của cảm biến dùng cơ cấu "
        "quét cơ khí gồm độ tin cậy thấp hơn và kích thước tổng thể tăng lên."))

    b.append(p(
        "Một số cảm biến tam giác đạc được báo cáo gần đây có kích thước đủ nhỏ để gắn lên tay gắp [5]. "
        "Tuy vậy chúng vẫn dễ mắc lỗi do méo và do sự tách rời của vệt phản xạ gây ra bởi độ không đồng "
        "đều của bề mặt, và cũng có thể có điểm mù do những gián đoạn gắn với hình dạng của vật được cảm "
        "nhận."))

    b.append(p(
        "Một nhóm khác các cảm biến tiệm cận quang điện dựa trên hình học là những cảm biến dựa trên "
        "định luật thấu kính Gauss [23, 24]. Cấu hình cơ bản của một đầu đo như vậy được trình bày trên "
        "Hình 8-14. Một chùm sáng, trùng với trục quang, tạo một vệt trên bề mặt đích. Ánh sáng tán xạ "
        "từ vệt đó được thấu kính thu lại. Trên Hình 8-14, PN biểu diễn tia giới hạn mà thấu kính còn có "
        "thể thu được. Khoảng cách tới đích (x) có thể tính theo tiêu cự của thấu kính (f) và vị trí ảnh "
        "(w). Áp dụng định luật thấu kính Gauss, khoảng cách x tính được là:"))

    b.append(eq("x = f·w/(w − f)", "8.13"))

    b.append(fig(14, hb8fig.fig_8_14()))

    b.append(p(
        "Một cảm biến tiệm cận (HexEye) dựa trên nguyên lý thấu kính này được trình bày trên Hình 8-15 "
        "[23, 24]. Cảm biến gồm bảy “khối cảm nhận” giống hệt nhau xếp theo một mẫu hình lục giác. Mỗi "
        "khối cảm nhận lại gồm bốn phần chính: một thấu kính vật, một gương nón, sáu dãy thu tuyến tính, "
        "và một nguồn sáng laser diode."))

    b.append(fig(15, hb8fig.fig_8_15()))

    b.append(p(
        "Chùm sáng do nguồn sáng tạo ra tạo một vệt trên bề mặt đích, và quang thông tán xạ từ vệt đó "
        "được thấu kính vật thu lại rồi hội tụ lên các dãy thu trong từng khối cảm nhận. Khoảng cách tới "
        "đích được xác định từ vị trí, kích thước và hình dạng của ảnh được tạo trên từng dãy thu riêng "
        "lẻ của khối."))

    b.append(p(
        "Cảm biến làm việc ở hai chế độ: khoảng cách hoặc hướng. Ở chế độ đo khoảng cách, bảy nguồn sáng "
        "được bật lần lượt từng cái để tạo một vệt sáng trên bề mặt đích, trong khi tất cả các khối cảm "
        "nhận đều thu quang thông tán xạ từ cùng vệt sáng đó. Khối đang hoạt động xác định khoảng cách "
        "theo nguyên lý định luật thấu kính Gauss, còn các khối không hoạt động xác định khoảng cách dựa "
        "trên tam giác đạc. Ở chế độ đo hướng, bảy khối cảm nhận được nhóm thành các khối đo hướng "
        "(OMU). Mỗi OMU gồm ba khối cảm nhận kề nhau quanh khối trung tâm, do đó có tổng cộng sáu OMU "
        "khả dĩ. Hướng cục bộ của bề mặt được ước lượng bằng cách tích phân sáu phép đo hướng."))

    b.append(p(
        "Ánh xạ giữa phân bố ánh sáng trên các dãy bộ thu và khoảng cách tới đích thu được thông qua hiệu "
        "chuẩn. Dùng phân bố ánh sáng (thay vì cường độ ánh sáng như ở cảm biến AM), người ta mong muốn "
        "ánh xạ này độc lập với các đặc tính bề mặt như màu, vật liệu, độ tán xạ và hệ số phản xạ. Tuy "
        "nhiên, đã chỉ ra rằng ánh xạ có thể bị làm hỏng bởi “nhiễu” từ nhiều nguồn, trong đó có các mẫu "
        "phản xạ và ánh sáng môi trường."))

    b.append(p(
        "Dùng định luật thấu kính Gauss có các ưu điểm sau so với nguyên lý tam giác đạc: (1) nguồn sáng "
        "có thể đặt tại tâm thấu kính vật, không chỉ cho phép cảm biến gọn hơn mà còn tối đa hoá lượng "
        "quang thông đi vào thấu kính; và (2) độ nhạy có thể được tối ưu cho một dải khoảng cách đo nhất "
        "định bằng cách điều khiển f."))

    # ---- time of flight
    b.append(p(
        "<strong>Thời gian bay.</strong> Các cảm biến quang điện đo thời gian bay là những hệ kiểu radar. "
        "Tuy nhiên, khác với radar thông thường — vốn phát một xung năng lượng tần số vô tuyến — các cảm "
        "biến này thường dùng một chùm sáng được điều chế. Khoảng cách tới đích được rút ra từ độ lệch "
        "pha đo được của ánh sáng phản xạ. Hai vấn đề gắn với loại cảm biến này là: khó đo khoảng cách "
        "ngắn (đòi hỏi tần số điều chế rất cao), và cần một hệ quét hoặc chuyển mạch cơ khí để có thêm "
        "thông tin (chẳng hạn về hướng) [5, 25]."))

    # ---- photothermal
    b.append(p(
        "<strong>Hiệu ứng quang nhiệt.</strong> Đầu đo dùng hiệu ứng quang nhiệt chiếu một chùm sáng "
        "mạnh vào bề mặt vật. Khoảng cách tới vật được rút ra từ các phép đo sóng nhiệt do ánh sáng bị "
        "vật hấp thụ sinh ra. Sơ đồ phát hiện và xử lý tín hiệu tương tự như ở cảm biến AM. Vì hình "
        "dạng của sóng nhiệt sinh ra tại bề mặt không phụ thuộc vào kết cấu bề mặt, cảm biến quang nhiệt "
        "không mắc phải vấn đề về độ bền vững bề mặt như ở cảm biến AM. Tuy nhiên, cảm biến quang nhiệt "
        "khá chậm và chỉ dùng được với những bề mặt hấp thụ mạnh [26]."))

    # ------------------------------------------------------------ capacitive
    b.append(h3("Cảm biến điện dung", "Capacitive Sensors"))

    b.append(p(
        "Cảm biến điện dung tạo ra và đo những thay đổi của điện trường do một vật điện môi hoặc vật dẫn "
        "nằm trong vùng tiệm cận của nó gây ra."))

    b.append(p(
        "Về cơ bản có hai loại cảm biến tiệm cận điện dung. Một loại dùng nguyên lý tụ điện bản cực song "
        "song, loại kia dùng nguyên lý điện dung rìa [8, 27, 28]. Với cảm biến tiệm cận kiểu bản cực song "
        "song, đầu đo tạo thành một bản cực còn vật cần đo tạo thành bản cực kia. Cấu tạo của một cảm "
        "biến tiệm cận kiểu bản cực song song và đáp ứng điển hình của nó được trình bày trên Hình 8-16 "
        "[8]. Cảm biến tiệm cận kiểu bản cực song song được dùng rộng rãi trong công nghiệp. Tuy nhiên "
        "loại cảm biến này có ba hạn chế chính: (1) vật cần đo phải dẫn điện; (2) quan hệ nghịch giữa khe "
        "hở và điện dung phi tuyến mạnh; và (3) độ nhạy giảm đáng kể khi khe hở lớn."))

    b.append(fig(16, hb8fig.fig_8_16()))

    b.append(p(
        "Loại cảm biến tiệm cận điện dung thứ hai dùng nguyên lý điện dung rìa [8]. Cảm biến có hai điện "
        "cực “sống” và vật cần đo không cần là một phần của hệ cảm biến. Vật đích có thể dẫn điện hoặc "
        "không dẫn điện. Tuy nhiên, phép đo khoảng cách bị ảnh hưởng bởi loại vật liệu của vật. Do đó "
        "phải thực hiện hiệu chuẩn riêng cho từng loại vật liệu."))

    b.append(p(
        "Trong [30], một vi cảm biến điện dung có tính đổi mới đã được trình bày. Nhờ công nghệ vi gia "
        "công, chiều dày điện cực có thể giảm đáng kể và hiệu ứng rìa tăng lên so với các cảm biến điện "
        "dung khác. Kết quả là cảm biến này cho độ nhạy tốt hơn. Có thể chế tạo một dãy các đầu đo như "
        "vậy để đo khoảng cách và hướng của một vật."))

    b.append(p(
        "Cảm biến tiệm cận điện dung có các ưu điểm chung sau: (1) tiêu thụ năng lượng thấp và (2) cấu "
        "tạo đơn giản. Tuy nhiên nhược điểm chính là chúng chịu ảnh hưởng của các tín hiệu bên ngoài và "
        "phải thực hiện kỹ thuật hiệu chuẩn riêng cho từng bề mặt, vì hoạt động của chúng phụ thuộc trực "
        "tiếp vào vật liệu của vật."))

    # ------------------------------------------------------------ ultrasonic
    b.append(h3("Cảm biến siêu âm", "Ultrasonic Sensors"))

    b.append(p(
        "Nguyên lý cơ bản của cảm biến đo xa siêu âm là đo thời gian cần để một sóng âm đi từ bộ phát tới "
        "bề mặt vật rồi trở về bộ thu. Bằng cách dùng nhiều bộ phát và bộ thu như vậy, có thể thu được "
        "thông tin về khoảng cách và hướng của bề mặt."))

    b.append(p(
        "Trong [19], một phương pháp mới được đề xuất để đo các góc hướng của bề mặt vật bằng hiệu pha "
        "của các tín hiệu dội phản xạ. Hình 8-17(a) cho thấy cấu hình của một đầu đo phẳng có n bộ thu, "
        "được đặt cách đều nhau trên một vòng bán kính R quanh bộ phát T. Tồn tại một quan hệ tuyến tính "
        "giữa hiệu độ dài δ của hai đường phản xạ ứng với một cặp bộ thu kề nhau và các độ nghiêng của "
        "vật."))

    b.append(fig(17, hb8fig.fig_8_17()))

    b.append(p(
        "Trên Hình 8-17(b) là quan hệ giữa độ nghiêng của bề mặt đích và δ. Có thể thấy rằng dải đo của "
        "cảm biến có thể được mở rộng khi tăng số bộ thu. Trong [29] cũng chỉ ra rằng có thể mở rộng dải "
        "đo bằng cách giảm R. Tuy nhiên cần lưu ý rằng các phép đo thực hiện với một cảm biến nhỏ có khả "
        "năng kém chính xác hơn."))

    b.append(p(
        "Các kết quả thực nghiệm dùng một đầu đo có sáu bộ thu (R = 30 mm) và tám bộ thu (R = 20 mm) đã "
        "được báo cáo trong [29]. Với đầu đo sáu bộ thu, dải đo của các góc hướng là ±15°; còn với đầu "
        "đo tám bộ thu, dải đo tối đa là ±30°. Với đầu đo sáu bộ thu, góc hướng có thể xác định được với "
        "độ chính xác 0,5° trong dải đo ±15°, và 0,2° khi dải đo bị thu hẹp về ±5°."))

    b.append(p(
        "Một trong những nhược điểm chính của cảm biến tiệm cận siêu âm là kích thước tương đối lớn. Tuy "
        "nhiên, việc chế tạo các cảm biến này bằng vi gia công có thể giải quyết vấn đề đó. Trong [7], "
        "việc phát và thu siêu âm cho cảm biến tiệm cận đã được khảo sát bằng các kết cấu màng cộng "
        "hưởng chế tạo theo công nghệ vi gia công."))

    # ------------------------------------------------------------ magnetic
    b.append(h3("Cảm biến từ", "Magnetic Sensors"))

    b.append(p(
        "Cảm biến kiểu từ tạo ra một từ trường xoay chiều, và sự biến thiên của từ trường này cung cấp "
        "thông tin về vị trí của vật."))

    b.append(p(
        "Những cảm biến từ đơn giản nhất là vi công tắc lưỡi gà hoặc công tắc hiệu ứng Hall. Tuy nhiên, "
        "loại cảm biến được dùng phổ biến nhất trong rô bốt là loại dựa trên nguyên lý cảm ứng điện từ, "
        "nhấn mạnh vào việc sinh dòng xoáy. Nguyên lý cơ bản gồm việc tạo một từ trường bằng các cuộn dây "
        "thích hợp quấn quanh một lõi có độ từ thẩm cao và một bộ dao động có tần số kích thích đủ cao "
        "để giảm thiểu sự xuyên sâu của từ trường vào trong vật liệu dẫn điện. Vấn đề chính của cảm biến "
        "từ là tỉ số kích thước trên dải đo lớn và khó bảo đảm phép đo khoảng cách đáng tin cậy trong "
        "những môi trường từ biến thiên."))

    # ------------------------------------------------------------ table
    b.append(table(
        ["Chế độ", "LED1", "LED2", "LED3", "LED4", "LED5", "LED6"],
        [["Khoảng cách (x)", "sin ωt", "cos ωt", "sin ωt", "cos ωt", "—", "—"],
         ["Hướng (u)", "—", "cos ωt", "—", "sin ωt", "—", "—"],
         ["Hướng (v)", "—", "—", "—", "—", "cos ωt", "sin ωt"]],
        "Bảng 8-1 · Các tổ hợp tín hiệu điều khiển LED. Dấu “—” nghĩa là LED đó không được điều khiển "
        "trong chế độ tương ứng.", " led"))

    # ------------------------------------------------------------ acknowledgments
    b.append(h2("Lời cảm ơn", "Acknowledgments"))
    b.append(p(
        "Các tác giả xin cảm ơn Martin Bonert đã đọc và phê bình cẩn thận chương này. Chúng tôi cũng ghi "
        "nhận sự hỗ trợ tài chính của Hội đồng Nghiên cứu Khoa học Tự nhiên và Kỹ thuật Canada."))

    # ------------------------------------------------------------ references
    b.append(reflist([
        "H. R. Everett, <em>Sensors for Mobile Robots: Theory and Application</em>, Natick, MA: A. K. "
        "Peters, Ltd., 1995.",
        "B. Espiau, “An overview of local environment sensing in robotics applications,” <em>Sensors "
        "and Sensory Systems for Advanced Robots</em>, NATO ASI Series, F43, 125–151, 1988.",
        "W. D. Koenigsberg, “Noncontact distance sensor technology,” <em>SPIE, Intelligent Robots</em>, "
        "449, 519–531, 1988.",
        "Å. Wernersson, B. Boberg, B. Nilsson, J. Nygårds và T. Rydberg, “On sensor feedback for "
        "gripping an object within prescribed posture tolerances,” IEEE Int. Conf. on Robotics and "
        "Automation, Nice, France, 1992, 1654–1660.",
        "A. Bradshaw, “Sensors for mobile robots,” <em>Measurement and Control</em>, 23(2), 48–52, 1990.",
        "R. Volpe và R. Ivlev, “A survey and experimental evaluation of proximity sensors for space "
        "robotics,” IEEE Int. Conf. on Robotics and Automation, 4, 3466–3473, 1994.",
        "O. Brand, H. Baltes và U. Baldenweg, “Ultrasound-transducer using membrane resonators realized "
        "with bipolar IC technology,” IEEE Conf. on Micro Electro Mechanical Systems, Oiso, Japan, "
        "1994, 33–38.",
        "R. C. Luo và Z. Chen, “Modeling and implementation of an innovative micro proximity sensor "
        "using micromachining technology,” Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems, "
        "Yokohama, Japan, 1993, 1709–1716.",
        "R. Masuda, “Multifunctional optical proximity sensor using phase modulation,” <em>J. Robotic "
        "Systems</em>, 3(2), 137–147, 1986.",
        "O. Partaatmadja, B. Benhabib và A. A. Goldenberg, “Analysis and design of a robotic distance "
        "sensor,” <em>J. Robotic Systems</em>, 10, 427–445, 1993.",
        "O. Partaatmadja, B. Benhabib, A. Sun và A. A. Goldenberg, “An electrooptical orientation "
        "sensor for robotics,” <em>IEEE Trans. on Robotics and Automation</em>, 8, 111–119, 1992.",
        "O. Partaatmadja, B. Benhabib, E. Kaizerman và M. Q. Dai, “A two-dimensional orientation "
        "sensor,” <em>J. Robotic Systems</em>, 9, 365–383, 1992.",
        "P. P. L. Regtien, “Accurate optical proximity detector,” IEEE Conf. on Instrumentation and "
        "Measurement Technology, San Jose, CA, 1990, 141–143.",
        "A. Bonen, R. E. Saad, K. C. Smith và B. Benhabib, “Active-sensing via a novel robotic "
        "proximity sensor,” Int. Conf. on Recent Advances in Mechatronics (ICRAM’95), Istanbul, 1995, "
        "1053–1058.",
        "Y. F. Li, “Characteristics and signal processing of a proximity sensor,” <em>Robotica</em>, "
        "12, 335–341, 1994.",
        "A. Bonen, R. E. Saad, K. C. Smith và B. Benhabib, “A novel calibration technique for "
        "electro-optical proximity sensors,” Int. Conf. on Industrial Electronics, Control and "
        "Instrumentation (IECON’95), Orlando, FL, 1995, 1190–1195.",
        "A. Bonen, R. E. Saad, K. C. Smith và B. Benhabib, “A novel optoelectronic interface-circuit "
        "design for sensing applications,” <em>IEEE Trans. Instrum. Meas.</em>, 45, 580–584, 1996.",
        "H. Bukow, “Fiber optic distance sensor for robotic applications,” SME Conf., Sensors, "
        "MS86-938, Detroit, MI, 1986.",
        "T. Okada, “Development of an optical distance sensor for robots,” <em>Int. J. Robotics "
        "Res.</em>, 1, 3–14, 1982.",
        "M. A. Kujoory, “Real-time range and elevation finder,” <em>Proc. IEEE</em>, 72(12), "
        "1821–1822, 1984.",
        "M. Fuhrman và T. Kanade, “Optical proximity sensor using multiple cones of light for measuring "
        "surface shape,” <em>Optical Eng.</em>, 23, 546–553, 1984.",
        "T. Okada và U. Rembold, “Proximity sensor using a spiral-shaped light-emitting mechanism,” "
        "<em>IEEE Trans. on Robotics and Automation</em>, 7, 798–805, 1991.",
        "S. Lee, “Distributed optical proximity sensor system: HexEYE,” IEEE Int. Conf. Robotics and "
        "Automation, 2, 1567–1572, Nice, France, 1992.",
        "S. Lee và J. Desai, “Implementation and evaluation of HexEye: a distributed optical proximity "
        "sensor system,” Proc. IEEE Int. Conf. Robotics and Automation, 3, 2353–2360, Nagoya, Aichi, "
        "Japan, 1995.",
        "S. Shinohara và cs., “Compact and high precision range finder with wide dynamic range using one "
        "sensor head,” IEEE Conf. Instrumentation and Measurement Technology, Atlanta, GA, 1991, "
        "126–130.",
        "M. Ito, K. Hane, F. Matsuda và T. Goto, “Proximity sensing technique using the photothermal "
        "effect,” <em>J. Japan Soc. Precision Eng.</em>, 58, 139–144, 1992.",
        "B. E. Noltingk, “A novel proximity gauge,” <em>J. Scientific Instruments</em>, Series 2, 2, "
        "356–360, 1969.",
        "B. E. Noltingk, A. E. T. Nye và H. J. Turner, “Theory and application of a proximity gauge "
        "using fringing capacitance,” <em>Proc. ACTA IMEKO</em>, 1976, 537–549.",
        "S. Nakajima và Y. Takahashi, “An ultrasonic orientation sensor with distributed receivers,” "
        "<em>Advanced Robotics</em>, 4, 151–168, 1990.",
        "A. Moldoveanu, “Inductive proximity sensors, fundamentals and standards,” <em>Sensors</em>, "
        "10(6), 11–14, 2000.",
    ]))

    # ------------------------------------------------------------ translator's note
    b.append(note(
        "<strong>Ghi chú của người dịch.</strong> "
        "(1) Phương trình 8.9 bị lỗi quét nặng trong bản PDF gốc; cách khôi phục được trình bày ở trên "
        "là suy luận từ tính đối xứng với phương trình 8.8, không phải nguyên văn bản in — xem ghi chú "
        "đặt ngay sau phương trình. "
        "(2) Tài liệu tham khảo [30] trong bản gốc bị cụt: dòng cuối dừng ở “11-14,” mà không có số "
        "trang kết thúc. Ở đây giữ nguyên phần đọc được và bổ sung năm 2000 theo đúng dòng dữ liệu của "
        "tạp chí. "
        "(3) Bảng 8-1 trong bản gốc dùng dấu gạch ngang dài để chỉ các LED không được điều khiển; bản "
        "dịch giữ nguyên quy ước đó. "
        "(4) Mục 8.2 nêu dải hướng ±30° như một yêu cầu chung, còn mục 8.3 nêu ±20° cho một cảm biến cụ "
        "thể trong [14] — đây là hai đối tượng khác nhau, không phải mâu thuẫn. "
        "(5) Toàn bộ mười bảy hình trong chương là hình vẽ lại của người dịch bằng SVG; các đường cong "
        "đáp ứng được tính từ chính các công thức mà chương nêu, không phải phác thảo bằng tay."))

    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a survey written in 1999, and its value today is not the catalogue of "
        "technologies — that has moved — but the argument it makes about where a proximity sensor "
        "sits in a robot's control loop. The authors are explicit: the sensor exists to bridge the "
        "uncertainty left by medium-range pose estimation. That single sentence sets every design "
        "constraint that follows, and it is worth unpacking before the hardware."))

    b.append(p(
        "A robot that has already decided where an object is does not need a proximity sensor. A robot "
        "that has an estimate good to a centimetre and a few degrees needs something that will close "
        "the last fifty millimetres and the last thirty degrees, fast, without touching. So the "
        "specification is not “measure distance” but “measure distance and orientation over the "
        "uncertainty region, at a rate that does not slow the arm.” The chapter's 1–10 ms figure is "
        "a control-loop requirement, not a metrology one: at a typical closing speed the gripper "
        "moves a few tenths of a millimetre in a millisecond, so anything slower than about 10 ms "
        "leaves the estimate stale by the time it is used."))

    b.append(fig(1, hb8fig.fig_8_1(), "en"))

    b.append(p(
        "The pose definition is worth reading carefully, because it is not the usual Euler triple. "
        "x is measured along the sensor's own X axis, and the two angles are applied in a specific "
        "order — u about Y, then v about the resulting Z. That order matters: rotating about Z first "
        "and then about Y gives a different frame for the same physical surface. The chapter is "
        "defining a frame, not a set of independent angles, and any implementation that treats u and "
        "v as interchangeable will produce a systematic error that grows with tilt."))

    b.append(p(
        "The four reflection phenomena are the physical core of the chapter, and they explain why "
        "optical proximity sensing is harder than it looks. Specular reflection from a planar "
        "microfacet returns a beam; diffuse return after penetration scatters; corner reflection "
        "diffracts. Which one dominates depends on the material, the wavelength and the surface "
        "finish — and the sensor has no way of knowing in advance. Every optical technique in the "
        "chapter is, in effect, a strategy for extracting geometry from a return whose amplitude is "
        "contaminated by an unknown mixture of those four."))

    b.append(fig(2, hb8fig.fig_8_2(), "en"))

    b.append(p(
        "Phase modulation is the most elegant answer to that problem, because it throws the amplitude "
        "away. Drive two sources in quadrature, sum the returns, and the phase of the sum depends on "
        "the path difference while the amplitude depends on reflectivity. Equation 8.8 makes the "
        "point exactly: the reflection factor C cancels out of the phase, so a machined aluminium "
        "block and a matt black plastic block at the same distance give the same φ. That is a "
        "genuinely material-independent measurement, and it is rare."))

    b.append(p(
        "The price is that phase alone gives one number, and one number cannot give three pose "
        "parameters. Hence the six-LED head: different LEDs are driven in different combinations to "
        "produce different phase equations, and the system solves them in sequence — x first, then v, "
        "then u. The dependence is explicit in the text: to recover v from equation 8.9 you must "
        "already know x. This is a cascaded estimator, and its error propagates: an error in x "
        "becomes an error in v, which becomes an error in u. The chapter does not say so, but that "
        "cascade is why the reported accuracy degrades with tilt."))

    b.append(fig(3, hb8fig.fig_8_3(), "en"))
    b.append(fig(4, hb8fig.fig_8_4(), "en"))

    b.append(p(
        "Amplitude modulation takes the opposite trade. It keeps the amplitude and normalises it "
        "away by differencing: DV = (V₁ − V₂)/(V₁ + V₂). If both receivers see the same source power "
        "P₀ and both convert light to voltage linearly, P₀ cancels in the ratio. The requirement of "
        "linearity is not a detail — it is the whole scheme. A receiver that compresses at high "
        "illumination will leave a residual P₀ dependence that looks exactly like a distance error."))

    b.append(fig(5, hb8fig.fig_8_5(), "en"))

    b.append(p(
        "The Y-guide is the chapter's best illustration of a general instrumentation principle: the "
        "response of a bifurcated fibre bundle is not monotonic, because the emitter cone and the "
        "receiver acceptance overlap in a way that peaks and then falls. The peak is not a nuisance "
        "to be designed out; it is a hard boundary. Below x_min the same brightness corresponds to "
        "two distances, and no amount of signal processing can tell them apart. Every Y-guide "
        "datasheet's “minimum range” is that ambiguity, drawn as a number."))

    b.append(fig(6, hb8fig.fig_8_6(), "en"))
    b.append(fig(7, hb8fig.fig_8_7(), "en"))

    b.append(p(
        "The symmetric three-fibre constellation converts the same physics into an orientation "
        "measurement. Tilt the surface one way and one receiver gains while the other loses; the "
        "normalised difference is monotonic through zero and, crucially, insensitive to distance "
        "because both receivers sit at the same range. That insensitivity is the mirror image of the "
        "asymmetric pair's behaviour, where distance and tilt are entangled and must be separated by "
        "solving orientation first. The chapter states the asymmetry plainly, and it is the single "
        "most useful design rule in the section."))

    b.append(fig(8, hb8fig.fig_8_8(), "en"))
    b.append(fig(9, hb8fig.fig_8_9(), "en"))
    b.append(fig(10, hb8fig.fig_8_10(), "en"))

    b.append(p(
        "The one-emitter, eight-receiver head in Figure 8.11 is the mature version of the idea, and "
        "its numbers are worth pausing on: 6.25 µm and 0.02° over 0–6 mm, falling to a 50 mm and ±20° "
        "envelope. That is a dynamic range of four orders of magnitude in distance for a device built "
        "from plastic fibre and an LED. It is achieved not by better optics but by abandoning the "
        "closed-form DV scheme for a polynomial fit over all eight signals — a reminder that when the "
        "physics is messy, calibration beats algebra."))

    b.append(fig(11, hb8fig.fig_8_11(), "en"))

    b.append(p(
        "The geometrical family trades the amplitude problem for a geometry problem. Triangulation "
        "reads position on a detector array, so surface reflectivity only affects signal-to-noise, "
        "not the answer — which is why the chapter can claim the method is indifferent to "
        "irregularity and orientation. The cost is the baseline: h and y_o must be known precisely, "
        "and the resolution in x falls as the square of the distance, because a fixed spot "
        "displacement corresponds to a shrinking angle."))

    b.append(fig(12, hb8fig.fig_8_12(), "en"))
    b.append(fig(13, hb8fig.fig_8_13(), "en"))

    b.append(p(
        "The Gaussian-lens family is the neatest of all. Put the source on the optical axis, image the "
        "spot, and x = fw/(w − f) follows from the thin-lens law alone — no baseline, no "
        "triangulation angle, and the source sits at the lens centre where it also maximises collected "
        "flux. The HexEye multiplies that unit seven times and gets two modes from one array: the "
        "active unit measures by the lens law, the passive ones by triangulation, and groups of three "
        "integrate into a local orientation. It is a genuinely elegant architecture, and it is the "
        "one place in the chapter where the sensor is designed as a system rather than a transducer."))

    b.append(fig(14, hb8fig.fig_8_14(), "en"))
    b.append(fig(15, hb8fig.fig_8_15(), "en"))

    b.append(p(
        "The capacitive and ultrasonic sections are short, and both are honest about their limits. "
        "The parallel-plate capacitor is the clearest case in the book of a sensor whose sensitivity "
        "is best where its range is worst: C ∝ 1/d, so resolution is excellent at a tenth of a "
        "millimetre and useless at ten. The fringing variant escapes the conductivity requirement but "
        "inherits a material dependence that forces per-material calibration — which, for a robot "
        "handling unknown objects, is close to disqualifying."))

    b.append(fig(16, hb8fig.fig_8_16(), "en"))

    b.append(p(
        "The ultrasonic ring sensor is the one place where the chapter's own numbers tell a clean "
        "story. Six receivers at R = 30 mm give ±15°; eight at R = 20 mm give ±30°. Smaller ring, "
        "wider range — and the authors note, correctly, that smaller also means less accurate. The "
        "reason is simple: δ scales with R, so shrinking R shrinks the signal that carries the angle. "
        "Range and resolution are bought from the same purse."))

    b.append(fig(17, hb8fig.fig_8_17(), "en"))

    b.append(h2("What has changed since 1999"))
    b.append(table(
        ["Then", "Now"],
        [["Phase modulation solved by cascaded closed-form equations",
          "Same physics, but the cascade is replaced by a single learned or fitted inverse model"],
         ["Plastic fibre bundles, 0.3–2 mm core, 1 dB/m",
          "VCSELs and CMOS SPAD arrays; the fibre is often gone entirely"],
         ["Triangulation with a linear CCD array and a scanned beam",
          "Structured light and time-of-flight cameras at consumer prices"],
         ["6.25 µm over 0–6 mm from a hand-built head",
          "Micrometre-class short-range sensors on a single die"],
         ["HexEye as a research prototype",
          "The architecture survives in distributed optical tactile skins"]],
        "Table 8-2 · What has moved since the chapter was written. The four reflection phenomena, and "
        "the cascade problem, have not."))

    b.append(p(
        "What has not changed is the central difficulty. Every technique here still has to separate "
        "three unknowns — distance, tilt, reflectivity — from a signal that mixes them. Phase "
        "modulation removes reflectivity and cascades the rest. Amplitude modulation normalises "
        "reflectivity and cascades the rest. Triangulation and the lens law sidestep reflectivity "
        "entirely and pay in baseline precision. There is no free measurement; there is only a choice "
        "of which unknown to eliminate first, and the chapter is a careful account of that choice."))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 8 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 8 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 8 “Proximity Sensing for Robotics” của Saad, Bonen, Smith và "
            "Benhabib — cảm biến tiệm cận quang điện, điện dung, siêu âm và từ cho tay máy rô bốt, "
            "mười ba phương trình, mười bảy hình và bảng tổ hợp tín hiệu LED." if vi else
            "Companion to Chapter 8 of the CRC Measurement Handbook — proximity sensing for robotic "
            "grasping, from phase modulation to the HexEye, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 8'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 8' % BASE_EN)
    meta = ("Chương 8 · theo Ch08.pdf (CRC Press, 1999) · 17 trang gốc · 17 hình, 1 bảng" if vi
            else "Chapter 8 · 17 source pages · 17 figures, 1 table")
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
