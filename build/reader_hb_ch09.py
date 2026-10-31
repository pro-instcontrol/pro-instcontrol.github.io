# -*- coding: utf-8 -*-
"""Handbook Chapter 9 — Distance (W. John Ballantyne, Spar Aerospace).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch09.py
"""
import os

import hb9fig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch09-distance"
TITLE_EN = "Distance"
TITLE_VI = "Đo khoảng cách"
BYLINE = "W. John Ballantyne · Spar Aerospace Ltd."
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-9-%d">%s<figcaption class="figcap">%s</figcaption>'
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
        "Các công cụ và kỹ thuật đo khoảng cách có lẽ là một trong những cuộc tìm tòi sáng tạo lâu dài "
        "nhất của loài người. Thang trên Hình 9-1 minh hoạ dải khoảng cách mênh mông mà khoa học và kỹ "
        "thuật quan tâm đo [1]. Chương này chỉ bàn tới các phương pháp đo một đoạn tương đối nhỏ trong "
        "dải đó — từ xentimét tới kilômét. Ngay trong đoạn hẹp ấy, cũng khó có thể liệt kê hết, chứ "
        "chưa nói tới mô tả hết, mọi cách tiếp cận đo khoảng cách đã từng được nghĩ ra. Tuy vậy, số ít "
        "công nghệ được điểm qua ở đây cũng sẽ có ích cho nhiều nhóm bạn đọc."))

    b.append(fig(1, hb9fig.fig_9_1()))

    b.append(p(
        "Đo khoảng cách, ở mức cơ bản nhất, là xác định độ dài của một đoạn thẳng một chiều nối hai "
        "điểm trong không gian ba chiều. Thường người ta cần cả một tập hợp các phép đo khoảng cách, để "
        "từ đó giải ra hình dạng, hướng, hoặc sự thay đổi vị trí của một vật. Vì thế không chỉ phải "
        "quan tâm tới việc đo khoảng cách, mà còn tới phân bố không gian và phân bố thời gian của "
        "chúng. Trong chương này, thuật ngữ “đo xa” dùng cho các hệ thực hiện phép đo đơn lẻ từ cảm "
        "biến tới đích; “ảnh khoảng cách” dùng cho các hệ thu một bản đồ hay lưới dày các phép đo "
        "khoảng cách phân bố trong không gian; và “theo dõi vị trí” dùng cho các hệ ghi lại lịch sử "
        "thời gian của phép đo khoảng cách tới một hay nhiều đích."))

    # ------------------------------------------------------------ 9.1
    b.append(h2("9.1 Phân biệt cơ bản giữa các kỹ thuật đo khoảng cách",
                "Basic Distinctions Between Range Measurement Techniques"))

    b.append(p(
        "Có thể phân loại các thiết bị đo khoảng cách theo một số khác biệt cơ bản. Từ những lớp lớn "
        "ấy có thể rút ra các tổng quát hoá, nhờ đó việc so sánh và chọn lựa trở nên dễ dàng hơn. Các "
        "mục dưới đây nêu những cơ sở phân loại nền tảng."))

    b.append(p(
        "<strong>Tiếp xúc hay không tiếp xúc.</strong> Một cách phổ biến để đo khoảng cách tới một điểm "
        "trên vật là dùng một thiết bị cơ khí đã hiệu chuẩn, đồng thời nối điểm đã chọn với một vị trí "
        "quy chiếu. Thước dây, căn lá, hay đồng hồ so đều có thể coi là ví dụ về một thiết bị đo tiếp "
        "xúc đơn giản. Trên thị trường có các thiết bị cơ – điện cho phép người dùng “số hoá” vị trí "
        "của từng điểm rời rạc trên một mặt ba chiều: một đầu dò gắn trên giá quay ở cuối một cơ cấu "
        "định vị X-Y-Z hoặc một tay khớp được dùng để chạm vào điểm cần đo, và thông tin cảm nhận về "
        "các vị trí tịnh tiến hoặc các góc khớp cho ra một ước lượng vị trí chính xác. Phương pháp cơ "
        "khí dựa trên tiếp xúc được dùng rộng rãi trong công nghiệp và có thể rất chính xác. Chẳng hạn, "
        "một số máy đo toạ độ (CMM) đạt độ lặp lại 1 µm."))

    b.append(p(
        "Nhược điểm chính của các cách tiếp cận cơ khí là chúng thường bị giới hạn ở khoảng cách và "
        "không gian làm việc tối đa vài mét. Đó là do những định luật tỉ lệ nền tảng của kết cấu cơ "
        "khí: khi yêu cầu vươn tới khoảng cách lớn hơn, khối lượng và các yêu cầu về dung sai cơ khí "
        "của máy khiến thiết kế trở nên bất khả thi. Ngoài ra, cách tiếp cận cơ khí quá chậm để thực "
        "hiện nhiều phép đo liên tiếp nhanh, trong khi ảnh khoảng cách hay theo dõi vị trí thường đòi "
        "hỏi đúng điều đó, vì phép đo liên quan tới những tập dữ liệu lớn phân bố theo không gian hoặc "
        "thời gian."))

    b.append(p(
        "Các kỹ thuật không tiếp xúc để đo xa, tạo ảnh khoảng cách và theo dõi vị trí thì nhiều và đa "
        "dạng. Besl [2] điểm lại và so sánh một số kỹ thuật trong đó. Ở dải xentimét tới mét, phần lớn "
        "không đạt được độ chính xác của máy CMM; nhưng ở thang lớn hơn và với khối lượng dữ liệu lớn, "
        "chúng trở thành nhu cầu thực tiễn. Phần còn lại của chương này chỉ bàn tới các cách tiếp cận "
        "không tiếp xúc."))

    b.append(p(
        "<strong>Chủ động hay bị động.</strong> Phép đo khoảng cách không tiếp xúc có thể chia thành kỹ "
        "thuật chủ động và bị động. Kỹ thuật chủ động dùng một dạng năng lượng được điều khiển (trường "
        "hoặc sóng) nối một vị trí quy chiếu đã biết với vị trí đích chưa biết. Nguồn năng lượng "
        "thường gắn với vị trí quy chiếu, nhưng trong một số trường hợp đích, hoặc cả đích lẫn quy "
        "chiếu, có thể là phía chủ động. Kỹ thuật bị động dựa vào một nguồn năng lượng có sẵn bên "
        "ngoài (chẳng hạn ánh sáng mặt trời, hoặc tương phản nhiệt độ giữa đích và nền) để làm cho đích "
        "có thể phát hiện được."))

    b.append(p(
        "Cách tiếp cận chủ động thường đơn giản hoá bài toán đo khoảng cách, vì nó cho phép kiểm soát "
        "nhiều hơn đối với vô số yếu tố có thể ảnh hưởng tới phép đo. Chẳng hạn, việc chọn dạng năng "
        "lượng và mức công suất của nguồn chủ động có thể giảm thiểu ảnh hưởng của những biến không "
        "kiểm soát được như ánh sáng môi trường, thời tiết và điều kiện khí quyển. Hơn nữa, cách tiếp "
        "cận chủ động cho cơ hội định vị phép đo một cách chọn lọc theo không gian và thời gian, loại "
        "bỏ khả năng nhầm lẫn về việc điểm đích nào đã được đo tại một thời điểm cho trước. Ngược lại, "
        "các hệ bị động (chẳng hạn đo xa lập thể) đôi khi mắc phải cái gọi là “bài toán tương ứng” — "
        "làm sao xác định được liệu một điểm đích quan sát từ hai hay nhiều góc nhìn, hoặc ở hai hay "
        "nhiều thời điểm, có thực sự là cùng một điểm vật lý hay không."))

    b.append(p(
        "Một ứng dụng phổ biến của cách tiếp cận chủ động là đo khoảng cách “xuyên qua” những vật liệu "
        "mà cơ khí hay quang học không xuyên qua được. Ví dụ có chẩn đoán hình ảnh y học, nơi nhiều "
        "dạng năng lượng định hướng (siêu âm, tia X) được dùng để dựng bản đồ bề mặt hoặc bản đồ khối "
        "của các cơ quan và xương; có sonar, vốn xuyên nước tốt hơn ánh sáng; và có radar xuyên đất, "
        "có thể phát hiện vật thể cùng độ sâu của chúng dưới mặt đất."))

    b.append(p(
        "Cách tiếp cận bị động, tuy không cho cùng mức độ kiểm soát và linh hoạt, lại có những ưu điểm "
        "nhất định. Thứ nhất, vì không phát năng lượng, sự tồn tại của chúng không thể bị một hệ phát "
        "hiện từ xa khác nhận ra — một đặc tính rất quan trọng trong ứng dụng quân sự. Thứ hai, hệ bị "
        "động thường thu được nhiều phép đo khoảng cách tới nhiều điểm nhanh hơn, vì chúng không bị "
        "giới hạn bởi tốc độ có thể hướng nguồn năng lượng tới từng điểm đích như phần lớn hệ chủ động. "
        "Chẳng hạn, một hệ đo xa lập thể thu được đồng thời mọi điểm đích phân giải được trong trường "
        "nhìn, trong khi một hệ quét laser, radar hay sonar lại thu từng điểm một theo trình tự. Cuối "
        "cùng, việc không có nguồn năng lượng định hướng là một sự đơn giản hoá có thể giảm đáng kể "
        "kích thước, giá thành và độ phức tạp phần cứng của thiết bị — dù phải đổi bằng độ phức tạp xử "
        "lý tín hiệu tăng lên."))

    b.append(p(
        "<strong>Thời gian bay, tam giác đạc, hay dựa trên trường.</strong> Có rất nhiều lớp và biến "
        "thể thiết bị đo xa không tiếp xúc, nhưng trừ vài ngoại lệ, chúng đều dựa trên một trong ba "
        "nguyên lý cơ bản sau:"))

    b.append("<ol>"
             "<li>Năng lượng lan truyền với một tốc độ đã biết và hữu hạn (chẳng hạn tốc độ ánh sáng, "
             "tốc độ âm thanh trong không khí).</li>"
             "<li>Năng lượng lan truyền theo đường thẳng qua một môi trường đồng nhất.</li>"
             "<li>Trường năng lượng thay đổi một cách liên tục, giảm đơn điệu và dự đoán được theo "
             "khoảng cách tới nguồn.</li>"
             "</ol>")

    b.append(p(
        "Các kỹ thuật gắn với ba hiện tượng nền tảng ấy lần lượt được gọi là thời gian bay, tam giác "
        "đạc, và dựa trên trường."))

    b.append(p(
        "<strong>Thời gian bay.</strong> Hệ thời gian bay (TOF) có thể thuộc loại “khứ hồi” (tức là "
        "dội, phản xạ) hoặc loại “một chiều” (tức là đích hợp tác, đích chủ động). Hệ khứ hồi thực chất "
        "đo thời gian để một mẫu năng lượng phát ra đi từ nguồn quy chiếu tới một đích phản xạ một phần "
        "rồi trở về. Tuỳ theo dùng tần số vô tuyến, tần số ánh sáng hay năng lượng âm thanh, các thiết "
        "bị này mang những tên như radar, lidar và sonar. Hệ một chiều phát tín hiệu ở đầu quy chiếu và "
        "thu ở đầu đích, hoặc ngược lại. Phải có một dạng mốc đồng bộ nào đó ở cả hai đầu để xác lập "
        "thời gian bay."))

    b.append(p(
        "Một đặc tính của nhiều hệ TOF là khả năng phân giải khoảng cách của chúng chỉ dựa trên khoảng "
        "thời gian ngắn nhất mà chúng phân giải được, chứ không dựa trên khoảng cách tuyệt đối đang "
        "đo. Nghĩa là, dù vật ở gần hay xa, sai số của phép đo về cơ bản là không đổi."))

    b.append(p(
        "<strong>Tam giác đạc.</strong> Kỹ thuật tam giác đạc đã được người xưa biết đến và thực hành. "
        "Nó dựa trên ý tưởng: nếu biết độ dài một cạnh của tam giác và hai góc của nó, có thể tính được "
        "độ dài các cạnh còn lại. Cạnh đã biết là “đường đáy”. Từ hai đầu đường đáy kẻ các đường ngắm "
        "tới điểm đích như trên Hình 9-2. Nếu xác định được các góc tạo bởi những đường này với đường "
        "đáy, khoảng cách được tính là:"))

    b.append(eq("R = b · sin α₁ · sin α₂ / sin(α₂ − α₁)", "9.1"))

    b.append(fig(2, hb9fig.fig_9_2()))

    b.append(note(
        "Công thức 9.1 in trong bản gốc là R = b·sin α₁·sin α₂/sin(α₂ − α₁). Đọc Hình 9-2 theo đúng "
        "chú thích của nó — α₁ và α₂ là hai góc tại hai đầu đường đáy, mỗi góc đo so với chính đường "
        "đáy — thì góc thứ ba của tam giác là π − α₁ − α₂. Định lý sin cho cạnh từ trạm trái tới đích "
        "là R = b·sin α₂/sin(α₁ + α₂), và khoảng cách vuông góc từ đường đáy tới đích là "
        "h = b·sin α₁·sin α₂/sin(α₁ + α₂). Tử số in trong sách đúng là tử số của h; mẫu số thì phải "
        "là sin(α₁ + α₂) chứ không phải sin(α₂ − α₁). Chỗ sai kiểm tra được ngay: mẫu số in trong "
        "sách triệt tiêu khi α₁ = α₂, tức khi đích nằm trên đường trung trực của đường đáy — lúc đó "
        "khoảng cách thật vẫn hữu hạn, bằng b/(2·tan α₁). Bản dịch giữ nguyên dạng in của phương "
        "trình và ghi chú sai lệch ở đây thay vì tự sửa."))

    b.append(p(
        "Trắc địa cổ điển là một kỹ thuật đo xa bị động dựa trên công thức trên. Người trắc địa dùng "
        "một dụng cụ ngắm chính xác để ngắm một đích từ hai vị trí cách nhau một đường đáy đã biết. Tài "
        "liệu [3] lưu ý rằng có thể tính khoảng cách tới một ngôi sao gần bằng cách quan sát nó qua "
        "một dụng cụ ngắm ở những khoảng thời gian sáu tháng và dùng đường kính quỹ đạo Trái Đất quanh "
        "Mặt Trời làm đường đáy. Đo xa lập thể, tức việc so sánh độ chênh (thị sai) giữa các đặc điểm "
        "chung trong ảnh của hai camera, là một dạng khác của tam giác đạc bị động. Đáng chú ý là thị "
        "giác người ước lượng khoảng cách bằng nhiều đầu mối khác nhau, nhưng hai trong số quan trọng "
        "nhất — thị giác lập thể và thị sai chuyển động — về bản chất đều dựa trên tam giác đạc [4]."))

    b.append(p(
        "Kỹ thuật tam giác đạc chủ động dùng một nguồn sáng chiếu (thường là laser) để tạo một cạnh của "
        "tam giác, và trục nhìn của một phương tiện thu quang học để tạo cạnh thứ hai. Khoảng cách giữa "
        "bộ chiếu và bộ thu là đường đáy."))

    b.append(p(
        "Một vấn đề nền tảng với mọi cách tiếp cận dựa trên tam giác đạc là khả năng ước lượng khoảng "
        "cách của chúng giảm theo bình phương khoảng cách đang đo. Có thể đối chiếu điều này với các "
        "cách tiếp cận TOF, vốn có sai số hầu như không đổi trên suốt dải làm việc. Hình 9-3 minh hoạ "
        "một cách khái niệm rằng tồn tại một khoảng cách “giao nhau”, từ đó kỹ thuật TOF trở nên thích "
        "hợp hơn kỹ thuật tam giác đạc."))

    b.append(fig(3, hb9fig.fig_9_3()))

    b.append(p(
        "<strong>Cách tiếp cận dựa trên trường.</strong> Trong khi kỹ thuật TOF và tam giác đạc chủ "
        "động khai thác hiện tượng lan truyền sóng của một dạng năng lượng nhất định, cách tiếp cận "
        "dựa trên trường lại tận dụng tính chất phân bố trong không gian của một dạng năng lượng. Cường "
        "độ của bất kỳ trường năng lượng nào cũng thay đổi theo khoảng cách tới nguồn. Hơn nữa, trường "
        "thường mang đặc tính vectơ, tức là có hướng. Vì vậy, nếu biết vị trí của bộ tạo trường và biết "
        "đặc trưng không gian của trường mà nó sinh ra là dự đoán được, thì các phép đo trường từ xa "
        "chứa thông tin có thể dùng để suy ra khoảng cách tới nguồn."))

    b.append(p(
        "Một khác biệt thú vị giữa cách tiếp cận dựa trên trường và cách tiếp cận dựa trên sóng là: "
        "tuy dùng trường năng lượng, cách thứ nhất không dựa vào sự lan truyền và chuyển hoá năng lượng "
        "(cùng những tổn thất đi kèm). Nghĩa là nó có thể dùng những trường tĩnh, như trường do một "
        "nam châm hay một điện tích tĩnh sinh ra. Những trường như vậy mã hoá thông tin vị trí ngay "
        "trong hình dạng của chúng. Âm thanh và ánh sáng, dù mang bản chất sóng, cũng có thể được khai "
        "thác theo cách tương tự như trường tĩnh, nhờ cường độ phụ thuộc khoảng cách của chúng."))

    b.append(p(
        "Kỹ thuật dựa trên trường phải đối mặt với một số vấn đề cơ bản giới hạn phạm vi ứng dụng. Thứ "
        "nhất, đặc trưng của phần lớn trường khai thác được trên thực tế thường chịu ảnh hưởng của các "
        "vật hay vật liệu ở gần, và không phải lúc nào cũng bảo đảm được rằng những ảnh hưởng đó sẽ "
        "giữ nguyên. Thứ hai, sự biến thiên của trường trong không gian rất phi tuyến (thường là nghịch "
        "đảo bình phương hoặc nghịch đảo lập phương), hàm ý rằng độ nhạy của phép đo chịu ảnh hưởng "
        "mạnh của việc ở gần hay xa nguồn. Bất chấp những lo ngại đó, đã có những thiết bị được phát "
        "triển và có mặt trên thị trường, hoạt động rất tốt trong đúng những tình huống mà chúng nhắm "
        "tới [7]."))

    # ---- form of energy
    b.append(h3("Dạng năng lượng", "Form of Energy"))

    b.append(p(
        "Như đã bàn ở trên, mọi thiết bị đo xa chủ động không tiếp xúc đều dùng một dạng năng lượng "
        "nào đó. Điều này đúng bất kể áp dụng nguyên lý thời gian bay, tam giác đạc hay dựa trên "
        "trường. Các mục dưới đây mô tả những dạng năng lượng được dùng và một vài tổng quát hoá về "
        "hiệu quả của từng dạng trong các tình huống khác nhau."))

    b.append(p(
        "<strong>Âm thanh.</strong> Các hệ đo xa dựa trên năng lượng âm thanh thường thuộc loại TOF "
        "xung – dội và dùng tần số sóng mang trong dải gọi là “siêu âm” (vượt ngưỡng nghe). Ngoài việc "
        "không nghe thấy được (một lợi ích hiển nhiên), tần số siêu âm còn dễ hội tụ thành chùm định "
        "hướng hơn và dễ phát, dễ thu bằng đầu đo áp điện. Tín hiệu siêu âm lan truyền được trong không "
        "khí, nhưng truyền xa hiệu quả hơn nhiều trong chất lỏng như nước, nơi tỉ số mật độ trên độ "
        "nhớt cao hơn dẫn tới vận tốc sóng lớn hơn và suy hao trên một đơn vị chiều dài nhỏ hơn. Kỹ "
        "thuật đo xa siêu âm (hay SONAR, viết tắt của SOund NAvigation and Ranging) được phát triển đầu "
        "tiên cho các ứng dụng dưới biển, nơi âm thanh vượt trội hơn hẳn năng lượng điện từ (kể cả ánh "
        "sáng) về quãng đường truyền được dưới nước [5]. Các hệ sonar xách tay giá rẻ được ngư dân câu "
        "cá thể thao dùng rộng rãi làm “máy dò cá” [6]."))

    b.append(p(
        "Tần số thường dùng trong các ứng dụng đo xa bằng âm thanh là vài chục kilôhéc tới vài trăm "
        "kilôhéc. Một sự đánh đổi cơ bản khi chọn tần số siêu âm là: tần số cao có thể tạo thành chùm "
        "hẹp hơn, do đó đạt phân giải ngang cao hơn, nhưng lại tắt nhanh hơn theo khoảng cách. Có thể "
        "lưu ý rằng chùm hẹp tới mức dùng được cho ảnh khoảng cách (dưới 10°) thì hiệu quả trong môi "
        "trường lỏng, nhưng suy giảm quá nhanh để dùng được trong không khí. Điều thú vị là, tuy năng "
        "lượng âm thanh suy giảm trong không khí nhanh hơn trong nước, vẫn có thể tạo ra những tín hiệu "
        "tầm ngắn hữu ích trong không khí với mức công suất tương đối thấp, vì mật độ không khí nhỏ hơn "
        "nhiều nên với cùng biên độ sóng, đầu đo chỉ cần tạo lực động nhỏ hơn."))

    b.append(p(
        "Khi so sánh năng lượng âm thanh với năng lượng điện từ cho các kỹ thuật TOF, cần nhớ rằng âm "
        "thanh, khác với ánh sáng, không chỉ lan truyền với tốc độ thấp hơn nhiều mà còn biến thiên tốc "
        "độ lớn hơn đáng kể, tuỳ theo loại và trạng thái của môi trường truyền. Vì vậy, những yếu tố "
        "như độ ẩm và áp suất không khí sẽ ảnh hưởng tới độ chính xác của thiết bị đo xa TOF. Với ứng "
        "dụng dưới nước, độ mặn và độ sâu ảnh hưởng tới phép đo. Tốc độ âm thanh thấp hơn còn có tác "
        "động bất lợi lên tốc độ thu các mẫu khoảng cách. Chẳng hạn, một đích cách 10 m cần ít nhất "
        "60 ms để đo qua môi trường không khí. Với một mẫu đơn lẻ thì có vẻ không lâu, nhưng nó trở "
        "thành vấn đề nếu ứng dụng cần lấy nhiều mẫu, như trong theo dõi chuyển động hay cảm nhận "
        "tránh va chạm."))

    b.append(p(
        "<strong>Từ trường tĩnh.</strong> Từ trường tĩnh hoặc giả tĩnh (tức tần số thấp) chỉ được dùng "
        "trong cách tiếp cận dựa trên trường. Một ưu điểm của loại trường này là chúng dễ và rẻ để tạo "
        "ra, bằng nam châm vĩnh cửu hoặc cuộn dây điện. Vì trường tĩnh không truyền năng lượng, đích "
        "không thể là bị động — chúng phải chủ động cảm nhận các tính chất của trường tại đúng vị trí "
        "của mình. Nhiều công nghệ cảm nhận khác nhau có thể được dùng để đo hướng và cường độ của một "
        "từ trường, trong đó có từ kế kiểu cổng từ thông, kiểu hiệu ứng Hall, và kiểu từ giảo. Một danh "
        "mục đầy đủ về các công nghệ này được nêu trong [7]."))

    b.append(p(
        "<strong>Tần số vô tuyến.</strong> Các hệ đo xa TOF kiểu dội dựa trên dải phổ điện từ có bước "
        "sóng khoảng từ 1 m tới 1 mm được gọi là RADAR (RAdio Detection And Ranging). Sóng vô tuyến có "
        "thể dùng để phát hiện ở khoảng cách xa trong nhiều điều kiện khí quyển khác nhau. Như với sóng "
        "âm, có những đánh đổi cần giải quyết khi chọn tần số. Sóng dài lan truyền tốt hơn trên quãng "
        "xa, nhưng sóng ngắn có thể được hội tụ thành chùm hẹp, cho khả năng phân biệt ngang tốt hơn. "
        "Một ứng dụng thú vị của radar tầm ngắn là radar xuyên đất, dùng để định vị và tạo ảnh các vật "
        "thể dưới bề mặt [8]. Ở đây sự đánh đổi giữa tần số và cự ly đặc biệt gay gắt, vì phải cân bằng "
        "giữa khả năng tạo ảnh hợp lý (chùm hẹp) và độ xuyên sâu tốt (sóng dài)."))

    b.append(p(
        "Một ví dụ về hệ TOF một chiều (bộ thu chủ động) dùng tần số vô tuyến là hệ định vị toàn cầu "
        "(GPS). Khoảng cách giữa một bộ thu trên mặt đất và mỗi một trong số nhiều vệ tinh đang bay "
        "được xác định nhờ các vệ tinh được trang bị bộ phát và một đồng hồ Cesium rất chính xác để "
        "đồng bộ. Mô tả tốt về GPS và việc dùng nó trong dẫn đường phương tiện có trong [9]."))

    b.append(p(
        "<strong>Tần số ánh sáng.</strong> Vượt ra ngoài phần vô tuyến của phổ điện từ là các tần số "
        "hồng ngoại, khả kiến và tử ngoại. Những tần số này có thể được tạo ra bằng laser và được thu "
        "bằng các linh kiện quang nhạy bán dẫn, và hữu ích cho cả đo xa TOF lẫn tam giác đạc chủ động. "
        "Kỹ thuật TOF kiểu dội được gọi là LIDAR (LIght Detection And Ranging), theo đúng cách đặt tên "
        "đã nêu ở trên."))

    b.append(p(
        "Tuy tần số ánh sáng suy giảm mạnh hơn tần số vô tuyến khi đi qua mây và sương, chúng có thể có "
        "độ rộng chùm rất hẹp, cho phép phân giải ngang và độ chọn lọc đích vượt trội."))

    # ---- coherent
    b.append(h3("Phát hiện kết hợp hay không kết hợp", "Coherent or Noncoherent Detection"))

    b.append(p(
        "Các thiết bị TOF kiểu dội, dù là sonar, radar hay lidar, có thể được phân loại thêm theo việc "
        "cách phát hiện đo trực tiếp thời gian bay (không kết hợp) hay khai thác một tính chu kỳ cố "
        "hữu trong năng lượng phát ra để xác định quãng đường bay (kết hợp)."))

    b.append(p(
        "Kỹ thuật không kết hợp gặp bài toán định thời những khoảng rất ngắn. Với sóng âm, đây không "
        "phải thách thức nghiêm trọng, vì một mét khứ hồi tương ứng với 6 ms; nhưng với ánh sáng và "
        "sóng vô tuyến thì có phần khó hơn, vì quãng đó chỉ tương ứng 6 ns. Độ chính xác của phát hiện "
        "không kết hợp thường dựa vào việc lấy trung bình nhiều phép đo lặp lại."))

    b.append(p(
        "Phát hiện kết hợp đạt được bằng cách trộn một phần tín hiệu phát ra với tín hiệu phản xạ để "
        "tạo ra tín hiệu thứ ba chỉ ra lượng trễ pha. Các tín hiệu ở đây là sóng liên tục (CW) chứ "
        "không phải xung. Kỹ thuật phát hiện kết hợp được phân thành điều chế biên độ (AMCW) hoặc điều "
        "chế tần số (FMCW)."))

    b.append(p(
        "Một vấn đề cơ bản của kỹ thuật phát hiện kết hợp là không phân biệt được các bội số nguyên của "
        "bước sóng điều chế cơ bản. Mọi hệ phát hiện kết hợp đều phải dùng kỹ thuật để giải cái gọi là "
        "“khoảng nhập nhằng”. Kỹ thuật không kết hợp không gặp vấn đề này."))

    # ---- ranging / imaging / tracking
    b.append(h3("Đo xa, ảnh khoảng cách, hay theo dõi vị trí",
                "Ranging, Range Imaging, or Position Tracking"))

    b.append(p(
        "Thiết bị đo xa thường được hướng tới một đích để cho ra một số đọc khoảng cách duy nhất. Một "
        "ví dụ phổ biến của phép đo xa đơn giản là cảm biến hồi tiếp dùng trong máy ảnh tự lấy nét. Hiện "
        "có nhiều thiết bị đo xa chủ động dựa trên nguyên lý TOF (radar, sonar, lidar) và tam giác đạc "
        "chủ động."))

    b.append(p(
        "Thiết bị tạo ảnh khoảng cách dùng cùng nguyên lý với thiết bị đo xa, chỉ khác là chúng có thêm "
        "một dạng quét nào đó để tạo ra một mảng các mẫu khoảng cách phân bố trong không gian. Đôi khi "
        "động tác quét được thực hiện bằng những phương tiện nội tại của cảm biến (chẳng hạn gương quay "
        "và gương gật, hoặc anten mảng pha), nhờ đó vị trí quy chiếu giữ nguyên. Trong trường hợp này, "
        "dữ liệu được ghi ở dạng cực (khoảng cách, góc tà, phương vị) như trên Hình 9-4. Trong những "
        "trường hợp khác, cảm biến có thể chỉ quét một trục bên trong, còn chiều quét thứ hai được thực "
        "hiện bằng cách di chuyển vị trí cảm biến theo một mẫu định trước. Không hiếm khi người ta còn "
        "ghi lại “cường độ”, tức năng lượng trở về, gắn với một mẫu khoảng cách. Bản đồ cường độ có "
        "thể được trình bày như một ảnh “thang xám” và, giống như một bức ảnh đen trắng, thường chứa "
        "thông tin bổ sung hữu ích cho việc diễn giải cảnh. Ảnh khoảng cách có thể được dùng để tạo ra "
        "các biểu diễn đồ hoạ ba chiều của cảnh và vật thể. Một ứng dụng phổ biến của ảnh khoảng cách "
        "là lập bản đồ địa hình từ trên không."))

    b.append(fig(4, hb9fig.fig_9_4()))

    b.append(p(
        "Thiết bị theo dõi vị trí được dùng để đo sự thay đổi vị trí và hướng của một vật theo thời "
        "gian. Những vấn đề cơ bản trong theo dõi vị trí là việc giành được và bám lấy những điểm đích "
        "cụ thể. Có thể tránh được những vấn đề này bằng cách dùng đích chủ động, và phần lớn hệ hiện có "
        "trên thị trường đều thuộc loại này."))

    # ------------------------------------------------------------ 9.2
    b.append(h2("9.2 Giới hạn hiệu năng của hệ đo xa",
                "Performance Limits of Ranging Systems"))

    b.append(p(
        "Đặc tính hiệu năng của các hệ đo xa hiện có rất khác nhau, cũng như yêu cầu của những ứng "
        "dụng mà chúng được thiết kế cho. Các mục dưới đây điểm lại những phạm trù hiệu năng cơ bản "
        "nhất và những vấn đề kỹ thuật của giới hạn hiệu năng."))

    b.append(p(
        "<strong>Độ chính xác khoảng cách.</strong> Như minh hoạ trên Hình 9-3, kỹ thuật TOF và tam "
        "giác đạc chủ động khác nhau về bản chất ở đặc trưng sai số theo khoảng cách. Các hệ dựa trên "
        "tam giác đạc chủ động hiện có đạt độ lặp lại và độ chính xác tốt hơn các hệ TOF trong dải dưới "
        "1 m, nhưng hiếm khi được dùng ở khoảng cách vài mét. Hymarc Ltd. và Perceptron Inc. mỗi bên "
        "đều cung cấp hệ tam giác đạc laser với độ chính xác 3σ lần lượt là 25 mm và 50 mm [10, 11]."))

    b.append(p(
        "Về nguyên tắc, hệ TOF có thể đạt độ chính xác sánh ngang tam giác đạc chủ động, nhưng kỹ thuật "
        "phát hiện hứa hẹn nhất — một biến thể của giao thoa kế laser, vốn giải được bài toán khoảng "
        "nhập nhằng [12] — vẫn chưa xuất hiện trên thị trường thương mại."))

    b.append(p(
        "<strong>Độ sâu trường.</strong> Độ sâu trường là khoảng khoảng cách mà trong đó một hệ đo xa "
        "đặt cố định có thể đo được mà không phải thay đổi cấu hình. Độ sâu trường lớn thường là một "
        "đặc tính quan trọng trong ứng dụng thực tiễn. Chẳng hạn, nếu khoảng cách tới đích biết trước "
        "rất mơ hồ thì độ sâu trường lớn là điều mong muốn."))

    b.append(p(
        "Các cách tiếp cận tam giác đạc quang học bị động như lập thể ảnh và đo ảnh thường có độ sâu "
        "trường hạn chế, vì chúng dựa vào tạo ảnh kiểu camera, vốn bị giới hạn cố hữu bởi độ sâu tiêu "
        "cự. Hệ TOF định thời khoảng có độ sâu trường tuyệt vời, vì chúng không dựa nhiều vào tạo ảnh "
        "quang học, ngoài việc tập trung năng lượng trở về lên bộ thu. Một số hệ tam giác đạc chủ động "
        "có dựa vào tạo ảnh quang học của vệt laser chiếu tới, nhưng thiết kế của Hymarc Ltd. lấy lại "
        "được độ sâu trường lớn bằng cách nghiêng dãy thu so với mặt phẳng thấu kính [13]."))

    b.append(p(
        "<strong>Cự ly tối đa.</strong> Mọi hệ đo xa, tạo ảnh khoảng cách hay theo dõi vị trí chủ động "
        "đều có một khoảng cách tối đa thực tế mà nó đo được. Đó là vì năng lượng được điều khiển — dù "
        "lan truyền như sóng hay thiết lập như trường — đều phải loang ra trước khi tới bộ thu. Sự loang "
        "này tất yếu tăng theo khoảng cách, và mọi bộ thu, bất kể đo dạng năng lượng nào, đều cần một "
        "lượng tối thiểu nào đó để vượt qua “nền nhiễu” cố hữu của mình."))

    b.append(p(
        "“Phương trình cự ly radar cổ điển” được giới thiệu trong nhiều sách về radar (chẳng hạn "
        "[14]). Jelalian [15] chỉ ra rằng phương trình này áp dụng được cả cho lidar, vì suy cho cùng "
        "lidar chỉ dùng một phiên bản tần số cao hơn của sóng điện từ. Thực tế, cùng ý tưởng đó cũng "
        "áp dụng cho sonar và cho các hệ tam giác đạc chủ động. Phương trình tính công suất của tín "
        "hiệu thu được như sau:"))

    b.append(eq(
        "P<sub>R</sub> = [P<sub>T</sub>G<sub>T</sub>/(4πR²)] × [ρA/(4πR²)] × "
        "[πD²/4] × η<sub>atm</sub>η<sub>sys</sub>", "9.2"))

    b.append(p("trong đó P<sub>R</sub> là công suất tại bộ thu; P<sub>T</sub> là công suất phát; "
               "G<sub>T</sub> là độ lợi của bộ phát; R là khoảng cách tới đích; ρ là độ phản xạ của "
               "đích; A là diện tích hiệu dụng của đích; D là đường kính khẩu độ thu; "
               "η<sub>atm</sub> là hệ số truyền qua của khí quyển; và η<sub>sys</sub> là hệ số truyền "
               "qua của hệ."))

    b.append(p(
        "Phương trình 9.2 áp dụng khi diện tích đích nhỏ hơn vệt chân của chùm tới, thường đúng với đo "
        "xa bằng radar và sonar. Tuy nhiên, với các hệ dùng laser, chùm tương đối hẹp thường có nghĩa "
        "là vệt laser nhỏ so với đích. Với một chùm phát loang theo góc khối θ<sub>T</sub>, diện tích "
        "vùng được chiếu sáng là:"))

    b.append(eq("σ<sub>spot</sub> = πR²θ<sub>T</sub>²", "9.3"))

    b.append(p(
        "Định nghĩa độ lợi bộ phát dựa trên ý niệm so sánh độ rộng chùm theo góc khối với một bộ phát "
        "vô hướng:"))

    b.append(eq("G<sub>T</sub> = 4π/θ<sub>T</sub>²", "9.4"))

    b.append(p(
        "Có thể thay phương trình 9.4 cho G<sub>T</sub> và phương trình 9.3 cho biến s trong phương "
        "trình 9.2 để được phương trình cự ly cho trường hợp vệt sáng nhỏ:"))

    b.append(eq(
        "P<sub>R</sub> = [P<sub>T</sub>/R²] × [ρ/4] × [πD²/4] × η<sub>atm</sub>η<sub>sys</sub>", "9.5"))

    b.append(p(
        "Ý nghĩa của phương trình này chủ yếu nằm ở sự phụ thuộc 1/R². Bất kỳ hệ đo xa nào làm việc "
        "bằng cách cho năng lượng dội lại từ một đích phản xạ tán xạ đều gặp suy giảm tín hiệu nghiêm "
        "trọng khi khoảng cách tăng. Với một bộ thu có nền nhiễu cố định, cách duy nhất để cải thiện cự "
        "ly tối đa là tăng công suất phát hoặc tăng diện tích thu. Trên thực tế, có những ràng buộc "
        "thiết kế giới hạn cả hai biện pháp này. Chẳng hạn, công suất laser đôi khi phải bị giới hạn vì "
        "lý do an toàn cho mắt, còn tăng diện tích thu có thể kéo theo tăng thể tích đóng gói của cảm "
        "biến theo tỉ lệ."))

    b.append(p(
        "<strong>Phân giải ngang.</strong> Trong các ứng dụng tạo ảnh khoảng cách, nhìn chung người ta "
        "muốn dùng độ rộng chùm hẹp nhất có thể để phân biệt tốt các chi tiết bề mặt đích. Laser, nhờ "
        "bước sóng ngắn, có thể được chuẩn trực quang học để tạo ra chùm hẹp hơn nhiều so với nguồn vô "
        "tuyến. Tuy vậy, ngay cả laser cũng không thể tạo ra chùm hẹp tuỳ ý. Bạn đọc quan tâm có thể "
        "tham khảo [13] để có thảo luận về lan truyền chùm Gauss và lấy nét tối ưu. Về cơ bản có hai "
        "cách chiếu ánh sáng laser. Có thể “hội tụ” chùm để tạo vệt nhỏ nhất có thể tại một điểm xác "
        "định bên trong dải đo, khi đó chùm sẽ loang ra khi khoảng cách tới điểm đó tăng; hoặc có thể "
        "lấy nét ở vô cực hay một điểm rất xa để giảm thiểu độ loang trên suốt dải đo. Cách thứ nhất "
        "cho phân giải ngang cao hơn tại khoảng cách lấy nét, nhưng kéo theo hạn chế độ sâu trường "
        "thực tế. Cách thứ hai đánh đổi kích thước vệt để lấy độ sâu trường lớn hơn."))

    b.append(p(
        "<strong>Tốc độ thu nhận.</strong> Tốc độ mà một cảm biến đo xa có thể thu các mẫu khoảng cách "
        "là quan trọng khi vật đích đang thay đổi hình dạng hoặc vị trí, hoặc khi mật độ mẫu yêu cầu "
        "của một ảnh khoảng cách rất cao. Có vài yếu tố tiềm tàng có thể giới hạn tốc độ thu mẫu: lượng "
        "thời gian bộ thu cần để tích phân tín hiệu trở về yếu tới một mức đủ (thời gian tích phân); "
        "hằng số thời gian của bất kỳ phép lọc hay lấy trung bình nào phải thực hiện để có được tín "
        "hiệu “sạch” ở mức chấp nhận được (thời gian làm trơn); tốc độ có thể chuyển các mẫu qua các "
        "tầng xử lý tín hiệu (thời gian truyền); và giới hạn vận tốc của cơ cấu quét cơ khí (băng thông "
        "quét). Tốc độ thu nhận rất khác nhau: từ vài chục héc cho thiết bị đo xa bằng âm thanh tới vài "
        "chục kilôhéc cho một số hệ dùng laser."))

    b.append(p(
        "Đáng lưu ý rằng nhìn chung có sự đánh đổi giữa tốc độ thu nhận, độ chính xác và cự ly tối đa. "
        "Một số hệ cho phép điều khiển các tham số cơ bản để sự đánh đổi này có thể được tối ưu cho một "
        "ứng dụng cụ thể. Bạn đọc nên biết rằng tài liệu kỹ thuật có thể không nói rõ liệu các con số "
        "hiệu năng công bố cho ba chỉ tiêu này có cùng đúng khi dùng đồng thời hay không."))

    # ------------------------------------------------------------ 9.3
    b.append(h2("9.3 Ví dụ chọn lọc về hệ đo xa, tạo ảnh khoảng cách và theo dõi chuyển động",
                "Selected Examples of Ranging, Range Imaging, and Motion Tracking Systems"))

    b.append(p(
        "Các mục dưới đây điểm qua một số ví dụ chọn lọc về những hệ cảm biến đo xa, tạo ảnh khoảng "
        "cách và theo dõi vị trí cụ thể. Danh sách này hoàn toàn không đầy đủ, nhưng đưa ra một mẫu hợp "
        "lý của các công nghệ hiện có."))

    b.append(h3("Cảm biến đo xa và tạo ảnh khoảng cách bằng tam giác đạc chủ động dùng laser",
                "Laser-Based Active Triangulation Ranging and Range Imaging Sensors"))

    b.append(p(
        "<strong>Cơ bản về tam giác đạc chủ động.</strong> Hình 9-5 minh hoạ hình học tam giác đạc chủ "
        "động cơ bản. Trong cái gọi là mô hình “camera lỗ kim” này, những khía cạnh thực tế như thấu "
        "kính cho chiếu và thu, gương cho quét, đều được bỏ đi cho rõ ràng. Có thể chứng minh bằng các "
        "tam giác đồng dạng rằng khoảng cách tỉ lệ nghịch với độ lệch của vệt sáng được tạo ảnh:"))

    b.append(eq("R = b·f/u", "9.6"))

    b.append(p("trong đó R là khoảng cách tới vật; b là độ dài đường đáy; f là khoảng cách từ thấu "
               "kính tới bộ thu; và u là vị trí vệt sáng phát hiện được trong mặt phẳng ảnh."))

    b.append(fig(5, hb9fig.fig_9_5()))

    b.append(p(
        "Độ nhạy của phép đo khoảng cách, tức mức thay đổi của u theo R, là:"))

    b.append(eq("|du/dR| = b·f/R²", "9.7"))

    b.append(p(
        "Ý nghĩa của phương trình 9.7 là hiệu năng ước lượng khoảng cách được dự kiến sẽ giảm khi "
        "khoảng cách tăng. Cải thiện độ chính xác đạt được bằng cách tăng đường đáy hoặc tăng khoảng "
        "cách từ thấu kính tới bộ thu (tức tiêu cự)."))

    b.append(p(
        "<strong>Nguyên lý quét đồng bộ.</strong> Việc quét ngang một cảm biến đo xa tam giác đạc chủ "
        "động được thực hiện bằng một kỹ thuật thanh nhã và hiệu quả, phát triển tại Hội đồng Nghiên cứu "
        "Quốc gia Canada và nay được Hymarc Ltd. tiếp thị dưới tên “HYSCAN” [10]. Một gương dao động hai "
        "mặt đồng thời lái chùm sáng phát ra ở một mặt và hướng ánh sáng thu được tới quang hệ tạo ảnh "
        "vệt ở mặt đối diện. Bằng cách quét đồng bộ cả chùm sáng lẫn trục của hệ thu, thay vì chỉ quét "
        "chùm như cách làm thông thường, người ta đạt được những cải thiện hiệu năng đáng kể. Hình 9-6 "
        "là minh hoạ sơ đồ của cách tiếp cận này. Cũng cần lưu ý rằng mặt phẳng bộ thu được nghiêng so "
        "với mặt phẳng thấu kính. Đặc điểm này làm tăng độ sâu tiêu cự để hiệu năng đo xa đạt cực đại "
        "trên toàn khối đo. Cảm biến Hyscan tạo ra một đường quét một trục, tức cái gọi là “quét "
        "tuyến”. Ảnh khoảng cách đầy đủ hai chiều thu được bằng cách dịch chuyển cảm biến trên bề mặt "
        "đích theo một mẫu chuyển động có kiểm soát."))

    b.append(fig(6, hb9fig.fig_9_6()))

    b.append(p(
        "<strong>Nguyên lý mặt phẳng sáng.</strong> Perceptron Inc. cung cấp một hệ quét tuyến tương "
        "tự dưới tên “TriCam” [11]. Trong trường hợp này, laser không bị quét. Thay vào đó, chùm sáng "
        "được biến đổi thành một mặt phẳng hội tụ nhờ các thấu kính trụ. Một bộ thu hai chiều được dùng "
        "để tạo ra các prôfin khoảng cách thông qua việc phân tích sự biến dạng của đường laser khi cảm "
        "biến được dịch chuyển trên bề mặt vật."))

    b.append(h3("Cảm biến tạo ảnh khoảng cách lidar dùng laser",
                "Laser-Based Lidar Range Imaging Sensors"))

    b.append(p(
        "<strong>Lidar điều chế biên độ (phát hiện theo pha).</strong> Perceptron Inc. cũng cung cấp "
        "một lidar quét dưới tên “LASAR”, có thể tạo ra những ảnh khoảng cách phân giải cao trên một "
        "khối đo lớn. Thiết bị dùng một laser hồng ngoại gần, được chiếu qua một kính viễn vọng chuẩn "
        "trực để tạo một vệt trên bề mặt đầu tiên mà nó gặp. Vệt này được quét trên một trường nhìn lập "
        "trình được theo mẫu raster nhờ một gương đa giác quay và một “gương gật” dao động. Một phần ánh "
        "sáng tán xạ ngược được thu lại và hướng đi nhờ một mặt kề của gương đa giác. Ánh sáng laser "
        "phát ra được điều chế biên độ tại một tần số chuẩn bằng cách điều khiển công suất cấp cho "
        "nguồn laser diode. Tín hiệu trở về, tuy yếu hơn tín hiệu phát đi nhiều bậc độ lớn, được so pha "
        "để xác định khoảng cách ứng với một phương vị và góc tà cụ thể. Cường độ của năng lượng trở về "
        "cũng được ghi lại. Tài liệu bán hàng của Perceptron công bố khối đo tối đa 60° × 72° × 40 m, "
        "độ phân giải lưới ảnh khoảng cách 1024 × 2048 pixel và tốc độ thu nhận tối đa 360.000 pixel/s. "
        "Sơ đồ khối của hệ LASAR™ được trình bày trên Hình 9-7. Chi tiết về cách tiếp cận kỹ thuật của "
        "Perceptron có thể tìm trong [16]."))

    b.append(fig(7, hb9fig.fig_9_7()))

    b.append(p(
        "<strong>Lidar cộng hưởng (phát hiện theo tần số).</strong> Acuity Research Inc. đã phát triển "
        "một cảm biến đo xa TOF dùng laser dựa trên một ý tưởng đơn giản nhưng hiệu quả. Bộ thu điều "
        "khiển đầu ra của laser sao cho khi không có tín hiệu thì laser được bật, còn khi có tín hiệu "
        "thì laser tắt. Thời gian truyền hữu hạn của chuyến đi khứ hồi của ánh sáng biến cách bố trí "
        "này thành một bộ cộng hưởng hai trạng thái, với chu kỳ tỉ lệ với khoảng cách tới đích. Thay vì "
        "đo chu kỳ — vốn cực ngắn và khó định thời — người ta đo tần số bằng các kỹ thuật đếm thông "
        "thường, với số chu kỳ nhiều bao nhiêu cũng được, miễn đủ để đạt độ chính xác yêu cầu. Thiết bị "
        "mang tên AccuRange 4000 cũng có phiên bản quét tuyến 360° thích hợp cho ứng dụng dẫn đường rô "
        "bốt di động [17]. Chi tiết về cách tiếp cận kỹ thuật có thể tìm trong [18]."))

    b.append(h3("Theo dõi vị trí bằng đích chủ động",
                "Position Tracking with Active Targets"))

    b.append(p(
        "Cách tiếp cận dùng đích chủ động không thuận tiện trong một số ứng dụng, nhưng lại là cách "
        "tuyệt vời để theo dõi đồng thời sự thay đổi vị trí của nhiều điểm đích. Đích chủ động là một "
        "cách né “bài toán tương ứng” đã nêu ở trên. Hai hệ được giới thiệu ở đây rất đáng để so sánh: "
        "một dùng năng lượng ánh sáng và tam giác đạc, một dùng cách tiếp cận dựa trên từ trường. Cả "
        "hai đều được dùng để theo dõi và ghi lại theo thời gian chuyển động của con người, của rô bốt "
        "và của các vật chuyển động khác."))

    b.append(p(
        "<strong>Tam giác đạc với đích chủ động.</strong> Hệ “OPTOTRAK” do Northern Digital Ltd. cung "
        "cấp [19] dùng các diode phát sáng hồng ngoại (LED) làm đích. Các LED được ghép kênh sao cho hệ "
        "camera mỗi lần chỉ nhìn thấy một cái, nhờ đó tránh được bài toán tương ứng. Dạng đo xa lập thể "
        "độc đáo ở đây dựa trên ba bộ thu tuyến tính có thấu kính, biến ánh sáng điểm của LED thành một "
        "vạch hội tụ. Hình học tam giác đạc được đơn giản hoá trên Hình 9-8. Từ hình học này có thể chỉ "
        "ra rằng vị trí đích (x<sub>p</sub>, y<sub>p</sub>, z<sub>p</sub>) xác định được từ các đầu ra "
        "của bộ thu u<sub>trái</sub>, u<sub>phải</sub> và v như sau:"))

    b.append(eq("x<sub>p</sub> = b(u<sub>phải</sub> + u<sub>trái</sub>)/2(u<sub>phải</sub> − "
                "u<sub>trái</sub>)", "9.8"))
    b.append(eq("y<sub>p</sub> = b·v/(u<sub>phải</sub> − u<sub>trái</sub>)", "9.9"))
    b.append(eq("z<sub>p</sub> = f·b/(u<sub>phải</sub> − u<sub>trái</sub>)", "9.10"))

    b.append(p(
        "trong đó f và b lần lượt là khoảng cách từ thấu kính tới bộ thu và khoảng cách đường đáy. Trên "
        "thực tế, ánh xạ từ không gian ảnh sang không gian vật phức tạp hơn nhiều so với các phương "
        "trình 9.8 tới 9.10, và liên quan tới một mô hình camera với hơn 60 tham số được xác định qua "
        "một quá trình hiệu chuẩn."))

    b.append(fig(8, hb9fig.fig_9_8()))

    b.append(p(
        "OPTOTRACK cho tốc độ lấy mẫu cao, khối đo lớn và độ chính xác cao so với nhiều hệ theo dõi vị "
        "trí khác."))

    b.append(p(
        "<strong>Theo dõi vị trí bằng từ trường.</strong> Một cảm biến theo dõi vị trí và hướng dựa "
        "trên một bộ phát lưỡng cực từ ba trục và một bộ thu vòng từ ba trục đã được Polhemus Inc. phát "
        "triển [20]. Các trường phát ra là dòng xoay chiều để dễ phát hiện (tức ghép kiểu biến áp) và "
        "được ghép kênh theo thời gian để trường của từng trục có thể phân biệt được với các trục khác. "
        "Khoảng cách giữa bộ phát và bộ thu được xác định bằng cách khai thác quan hệ 1/R³ giữa cường "
        "độ trường và khoảng cách tới nguồn. Hướng của bộ thu được xác định bằng cách khai thác tính "
        "định hướng của từ trường và độ nhạy hướng của bộ thu vòng dây."))

    b.append(p(
        "Một vấn đề liên quan tới việc dùng trường xoay chiều là sự méo hình dạng trường xảy ra khi có "
        "các vật kim loại, và ảnh hưởng kéo theo lên độ chính xác của cảm biến. Những méo này sinh ra "
        "từ dòng xoáy trong kim loại dẫn điện. Ascension Technology Corp. đã phát triển một biến thể "
        "của cảm biến Polhemus dựa trên từ trường một chiều. Quá độ chuyển mạch do ghép kênh theo thời "
        "gian có tạo ra hiệu ứng dòng xoáy, nhưng nó được để tắt hẳn trước khi thực hiện phép đo. Chi "
        "tiết về kỹ thuật một chiều có trong [21]."))

    b.append(p(
        "Một khác biệt quan trọng giữa công nghệ theo dõi quang học và công nghệ theo dõi từ là: loại "
        "thứ nhất đòi hỏi đường ngắm không bị chắn tới các đích, còn loại thứ hai thì không. Điều này "
        "cho các hệ theo dõi từ một lợi thế trong một số ứng dụng. Mặt khác, đặc trưng phân bố trường "
        "1/R³ của theo dõi từ hàm ý mất độ nhạy cực mạnh theo khoảng cách, trong khi tam giác đạc quang "
        "học có đặc trưng 1/R ôn hoà hơn. Điều này phần nào giải thích vì sao khối đo và độ chính xác "
        "của các hệ tam giác đạc quang học nói chung tốt hơn nhiều so với các hệ từ."))

    # ------------------------------------------------------------ 9.4
    b.append(h2("9.4 Một mẫu sản phẩm thương mại về đo xa, tạo ảnh khoảng cách và theo dõi chuyển động",
                "A Sampling of Commercial Products"))

    b.append(p(
        "Bảng 9-1 chứa thông tin thu thập từ tài liệu của các nhà cung cấp. Khi so sánh các chỉ tiêu, "
        "cần lưu ý rằng điều kiện thử nghiệm, tiêu chuẩn và cách diễn giải có thể khác nhau đáng kể. Do "
        "đó các chỉ tiêu này chỉ nên được dùng như một chỉ dẫn thô."))

    b.append(table(
        ["Lớp", "Tên thương mại", "Nguyên lý", "Đặc điểm", "Liên hệ"],
        [["Đo xa (tiếp xúc)", "MicroScribe-3DX", "Tay máy có đầu dò",
          "Khối làm việc cầu 50 in., độ chính xác 0,3 mm", "Immersion Corp. (408) 467-1900, "
          "info@immerse.com"],
         ["Đo xa (không tiếp xúc)", "LASERVISION", "TOF, laser",
          "Cự ly 50 m, độ chính xác 4,9 mm ở 15 m, có thước thuỷ điện tử tích hợp",
          "ZIRCON Corp., (408) 866-8600"],
         ["Tạo ảnh khoảng cách (quét tuyến)", "HYSCAN", "Tam giác đạc chủ động dùng laser",
          "Độ sâu trường 40 mm, bề rộng dải 70 mm, độ chính xác 0,025 mm, 10.000 điểm/s",
          "Hymarc Ltd., (613) 727-1584, info@hymarc.com"],
         ["Tạo ảnh khoảng cách (quét tuyến)", "TriCam", "Tam giác đạc chủ động dùng laser",
          "Độ sâu trường 120 mm, bề rộng dải 60 mm, độ chính xác 0,05 mm",
          "Perceptron Inc., (810) 478-7710, inquiry@perceptron.com"],
         ["Tạo ảnh khoảng cách (quét tuyến)", "ALTM 1020", "TOF laser, định thời khoảng",
          "Cự ly 330–1000 m, độ chính xác 15 cm, dải quét 20°", "Optech Inc., (416) 661-5904"],
         ["Tạo ảnh khoảng cách (quét diện)", "Rangecam 7000", "Tam giác đạc dùng laser hoặc đèn chớp",
          "Dùng camera CCD tiêu chuẩn và bộ chiếu mặt phẳng sáng", "Range Vision Inc., (604) 473-9411"],
         ["Tạo ảnh khoảng cách (quét diện)", "LASAR", "TOF, lidar điều chế biên độ",
          "Cự ly 2–40 m, trường nhìn tối đa 60 × 70°, 360.000 mẫu/s",
          "Perceptron Inc., (810) 478-7710"],
         ["Theo dõi vị trí", "OPTOTRAK", "Tam giác đạc với đích chủ động",
          "Tới 255 đích, độ chính xác dưới milimét, 5000 mẫu 3 bậc tự do/s",
          "Northern Digital Inc., (519) 884-5142"],
         ["Theo dõi vị trí", "Flock of Birds", "Dựa trên từ trường",
          "Tới 30 đích vị trí/hướng, độ chính xác khoảng 10 mm, 144 mẫu 6 bậc tự do/s",
          "Ascension Technology Corp. (802) 860-6440"]],
        "Bảng 9-1 · Sản phẩm và nhà cung cấp thiết bị đo xa, tạo ảnh khoảng cách và theo dõi vị trí. "
        "Thông tin thu thập từ tài liệu quảng cáo năm 1995 của các hãng; giữ nguyên như bản gốc để làm "
        "mốc lịch sử.", " prod"))

    # ------------------------------------------------------------ references
    b.append(reflist([
        "R. Resnick và D. Halliday, <em>Physics (Part 1)</em>, New York: John Wiley &amp; Sons, 1966, tr. 4.",
        "P. J. Besl, “Range imaging sensors,” General Motors Research Publication GMR-6090, General "
        "Motors Research Laboratories, Warren, MI, tháng 3, 1988.",
        "R. Resnick và D. Halliday, <em>Physics (Part 1)</em>, New York: John Wiley &amp; Sons, 1966, tr. 3.",
        "D. F. McAllister (chủ biên), <em>Stereo Computer Graphics and Other True 3D Technologies</em>, "
        "Princeton, NJ: Princeton University Press, 1993, ch. 4.",
        "L. E. Kinsler và A. R. Frey, <em>Fundamentals of Acoustics</em>, 2nd ed., New York: John Wiley "
        "&amp; Sons, 1962, ch. 9 và 15.",
        "W. Diedrich, “Foundations of reading sonar,” <em>The In-Fisherman</em>, tháng 4–5, 42–56, 1996.",
        "E. B. Blood, “Device for quantitatively measuring the relative position and orientation of two "
        "bodies in the presence of metals utilizing direct current magnetic fields,” Bằng phát minh Hoa "
        "Kỳ 4.945.305, 31/7/1990.",
        "W. J. Steinway và C. R. Barrett, “Development status of a stepped-frequency ground penetrating "
        "radar,” trong <em>Underground and Obscured Object Imaging and Detection</em>, SPIE Proceedings, "
        "vol. 1942, Orlando, FL, tháng 4, 1993, 34–43.",
        "J. Borenstein, H. R. Everett và L. Feng, <em>Where am I? Sensors and Methods for Autonomous "
        "Mobile Robot Positioning</em>, ấn bản 1995, báo cáo của Đại học Michigan cho Chương trình Phát "
        "triển Công nghệ Rô bốt thuộc Bộ Năng lượng Hoa Kỳ, Ann Arbor, MI, 1995, ch. 3.",
        "Hymarc Ltd., 1995, <em>Product Information, Hyscan 3D Laser Digitizing Systems</em>, Ottawa, "
        "Ontario, Canada.",
        "Perceptron Inc., 1995, <em>Product Information, TriCam Non-Contact Measurement Solutions</em>, "
        "Farmington Hills, MI.",
        "F. E. Goodwin, “Frequency Modulated Laser Radar,” Bằng phát minh Hoa Kỳ 4.830.486, 16/5/1989.",
        "F. Blais, M. Rioux và J.-A. Beraldin, “Practical considerations for a design of a high precision "
        "3D laser scanner system,” SPIE vol. 959, <em>Optomechanical and Electro-Optical Design of "
        "Industrial Systems</em>, 1988.",
        "D. K. Barton, <em>Radar System Analysis</em>, Englewood Cliffs, NJ: Prentice-Hall, 1964, ch. 4.",
        "A. V. Jelalian, <em>Laser Radar Systems</em>, Artech House, 1992, ch. 1.",
        "E. S. Cameron, R. P. Srumski và J. K. West, “Lidar Scanning System,” Bằng phát minh Hoa Kỳ "
        "5.006.721, 9/4/1991.",
        "Acuity Research Inc., 1995, <em>Product Information, Accurange 4000</em>, Menlo Park, CA.",
        "R. R. Clark, “Scanning rangefinder with range to frequency conversion,” Bằng phát minh Hoa Kỳ "
        "5.309.212, 3/5/1994.",
        "Northern Digital Inc., 1990, <em>Product Literature, OPTOTRACK 3D Motion Measurement System</em>, "
        "Waterloo, Ontario, Canada.",
        "F. H. Raab, E. B. Blood, T. O. Steiner và H. R. Jones, “Magnetic position and orientation "
        "tracking system,” <em>IEEE Trans. Aerospace Electronic Systems</em>, vol. AES-15, số 5, tháng "
        "9, 1979.",
        "E. B. Blood, “Device for quantitatively measuring the relative position and orientation of two "
        "bodies in the presence of metals utilizing direct current magnetic fields,” Bằng phát minh Hoa "
        "Kỳ 4.945.305, 31/7/1990.",
    ]))

    b.append(note(
        "<strong>Ghi chú của người dịch.</strong> "
        "(1) Công thức 9.1 in trong bản gốc không khớp với hình vẽ kèm theo — xem ghi chú đặt ngay sau "
        "phương trình. "
        "(2) Tài liệu [7] và [21] trong bản gốc là cùng một bằng phát minh của E. B. Blood, in hai lần "
        "ở hai vị trí khác nhau trong danh mục; bản dịch giữ nguyên cả hai để đánh số không lệch so "
        "với phần thân chương. "
        "(3) Bảng 9-1 trong bản gốc là ảnh chụp thị trường năm 1995, có số điện thoại và địa chỉ thư "
        "điện tử. Bản dịch giữ nguyên toàn bộ, kể cả các số liệu đã lỗi thời, vì giá trị của bảng nằm "
        "ở chỗ nó ghi lại đúng trạng thái thị trường mà tác giả đang mô tả. "
        "(4) Chín hình trong chương đều là hình vẽ lại bằng SVG của người dịch; các đường cong trên "
        "Hình 9-3 được tính từ chính các quan hệ mà mục 9.2 nêu, không phải phác thảo bằng tay."))

    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Ballantyne's chapter is really an argument disguised as a survey. The taxonomy in 9.1 — contact "
        "or not, active or passive, time-of-flight or triangulation or field — is not a filing system "
        "for products. It is a set of axes along which a design decision has to be made, and each axis "
        "trades one kind of capability for another. Read that way, the chapter is far more useful than "
        "its 1999 product table suggests."))

    b.append(fig(1, hb9fig.fig_9_1(), "en"))

    b.append(p(
        "The scale figure is the first clue about what the chapter is really claiming. Thirty orders of "
        "magnitude of measurable distance, and this chapter covers six of them — centimetres to "
        "kilometres. That is the range a robot arm or a surveying instrument actually needs, and it is "
        "also the range where the three principles are all competitive. Below a millimetre, contact and "
        "interferometry dominate; above a kilometre, only time-of-flight survives."))

    b.append(p(
        "The active/passive distinction is the one most often misread. Active systems are not better; "
        "they are more controllable. The author's point about the correspondence problem is the real "
        "content: a passive stereo system has to solve, for every frame, which point in the left image "
        "is the same physical point as which point in the right image. An active system that "
        "time-multiplexes its targets — one LED lit at a time, as OPTOTRAK does — makes that problem "
        "disappear entirely. That is why almost every commercial motion tracker uses active targets, "
        "and it is a design lesson that generalises well beyond ranging."))

    b.append(fig(2, hb9fig.fig_9_2(), "en"))

    b.append(p(
        "The triangulation formula deserves a careful look, because the printed version and the drawn "
        "geometry do not agree. Read Figure 9-2 the way its own caption reads it — α₁ and α₂ measured "
        "at the two ends of the baseline, each against the baseline itself — and the third angle of the "
        "triangle is π − α₁ − α₂. The sine rule then gives the side from the left station to the target "
        "as R = b sin α₂ / sin(α₁ + α₂), and the perpendicular distance from the baseline to the target "
        "as h = b sin α₁ sin α₂ / sin(α₁ + α₂). The printed numerator, b sin α₁ sin α₂, is exactly the "
        "numerator of h; the printed denominator, sin(α₂ − α₁), should be sin(α₁ + α₂). The slip is "
        "easy to demonstrate rather than merely assert: the printed denominator vanishes whenever "
        "α₁ = α₂, that is, for a target on the perpendicular bisector of the baseline, where the true "
        "range is plainly finite and equal to b/(2 tan α₁). So this is not a small-angle approximation "
        "quietly standing in for an exact result — it is a sign error that manufactures a singularity "
        "at the one geometry every surveyor eventually sets up. Keep the corrected form in mind when "
        "you read the rest of the chapter, because the accuracy argument in 9.2 inherits the geometry."))

    b.append(p(
        "The time-of-flight versus triangulation comparison is the chapter's central quantitative claim, "
        "and it is worth restating plainly: TOF error is set by the shortest interval the electronics "
        "can resolve, so it is flat with distance; triangulation error is set by geometry, so it grows "
        "as R². There is therefore always a crossover range, and it is a design parameter, not a law of "
        "nature — you move it by changing the baseline or the clock."))

    b.append(fig(3, hb9fig.fig_9_3(), "en"))
    b.append(fig(4, hb9fig.fig_9_4(), "en"))

    b.append(p(
        "The radar range equation section looks like boilerplate until you notice what it is doing. "
        "Substituting the spot area (9.3) and the transmitter gain (9.4) into the general form (9.2) "
        "collapses the 1/R⁴ into 1/R². That collapse is the whole reason laser ranging works at all: "
        "for a target larger than the illuminated spot, doubling the range costs you only a factor of "
        "four, not sixteen. It also explains the design pressure the author notes — you cannot buy range with "
        "aperture indefinitely, because D² appears in the numerator but packaging volume goes as D³."))

    b.append(p(
        "Active triangulation is where the chapter becomes concrete, and the two commercial systems it "
        "describes are still the two archetypes. Hymarc's synchronized scanning is a genuinely clever "
        "piece of optomechanics: instead of sweeping the beam and leaving the detector fixed, it sweeps "
        "both, using the two faces of one oscillating mirror. The effect is that the triangulation "
        "triangle stops changing shape as the beam scans, so the spot stays on the detector array "
        "instead of walking off it. Tilting the array relative to the lens plane then extends the depth "
        "of focus over the whole measuring volume — the Scheimpflug condition, applied to a scanner."))

    b.append(fig(5, hb9fig.fig_9_5(), "en"))
    b.append(fig(6, hb9fig.fig_9_6(), "en"))

    b.append(p(
        "Perceptron's LASAR takes the other route: keep the geometry simple and put the intelligence in "
        "the modulation. Amplitude-modulate the laser at a reference frequency, compare the phase of "
        "the return against that reference, and the range falls out — with the same ambiguity problem "
        "the chapter flags for all coherent detection, since a phase measurement cannot distinguish R "
        "from R plus a whole modulation wavelength. The polygon mirror handles azimuth, the nodding "
        "mirror elevation, and the raster is built from the two rates."))

    b.append(fig(7, hb9fig.fig_9_7(), "en"))

    b.append(p(
        "The magnetic tracker comparison at the end is the most quotable part of the chapter, and it is "
        "a clean lesson in how a physical law becomes an engineering limit. A dipole field falls as "
        "1/R³; optical triangulation falls as 1/R. Over a metre, that is a factor of a hundred in "
        "signal for the same starting point. No amount of electronics recovers it. That single exponent "
        "is why optical trackers have large working volumes and magnetic ones do not — and why magnetic "
        "trackers, despite needing no line of sight, remain niche."))

    b.append(fig(8, hb9fig.fig_9_8(), "en"))

    b.append(h2("What has changed since 1999"))
    b.append(table(
        ["Then", "Now"],
        [["AM lidar with a polygon mirror and a nodding mirror",
          "MEMS mirrors and solid-state optical phased arrays; no moving parts"],
         ["Avalanche photodiodes and analogue phase detectors",
          "SPAD arrays with per-pixel time-to-digital conversion"],
         ["Triangulation scanners at 10,000 points/s",
          "Structured-light and ToF cameras at megapixel rates and consumer prices"],
         ["Magnetic trackers at 1/R³, ~10 mm accuracy",
          "The same physics, largely displaced by optical and inertial fusion"],
         ["A vendor table with phone numbers and email addresses",
          "A web search; the table is now a historical snapshot, not a buying guide"]],
        "Table 9-2 · What has moved since the chapter was written. The 1/R² and 1/R³ exponents have "
        "not."))

    b.append(p(
        "What survives is the taxonomy and the crossover argument. Every time-of-flight sensor shipping "
        "today still trades resolution against clock speed; every triangulation sensor still trades "
        "range against baseline; every field-based sensor still fights the inverse-cube law. The parts "
        "changed. The arithmetic did not."))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 9 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 9 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 9 “Distance” của W. John Ballantyne — phân loại các kỹ thuật đo "
            "khoảng cách, giới hạn hiệu năng, và các hệ thương mại, với mười phương trình, tám hình và "
            "bảng sản phẩm." if vi else
            "Companion to Chapter 9 of the CRC Measurement Handbook — the taxonomy of distance "
            "measurement, its performance limits, and the systems that implement it, with the full "
            "Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 9'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 9' % BASE_EN)
    meta = ("Chương 9 · theo Ch09.pdf (CRC Press, 1999) · 18 trang gốc · 8 hình, 1 bảng" if vi
            else "Chapter 9 · 18 source pages · 8 figures, 1 table")
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
