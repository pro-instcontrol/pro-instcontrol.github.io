# -*- coding: utf-8 -*-
"""Handbook Chapter 97 — PID Control (F. Greg Shinskey, Process Control
Consultant).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch97.py
"""
import os

import hb97fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch97-pid-control"
TITLE_EN = "PID Control"
TITLE_VI = "Điều khiển PID"
BYLINE = "F. Greg Shinskey · Process Control Consultant"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-97-%d">%s<figcaption class="figcap">%s</figcaption>'
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


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def dt(term, definition):
    return p("<b>%s:</b> %s" % (term, definition))


# ================================================================ Vietnamese

def body_vi():
    b = []

    b.append(h2("97.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Điều khiển quá trình giữ vai trò thiết yếu trong việc chế tạo an toàn những sản phẩm có chất "
        "lượng đúng nhu cầu thị trường, đồng thời bảo vệ môi trường. Lưu lượng, áp suất và nhiệt độ "
        "trong đường ống và bình chứa, lượng tồn trữ chất lỏng và chất rắn, và chất lượng sản phẩm — "
        "tất cả đều là những ví dụ về biến đo phải được điều khiển để đạt các mục tiêu trên. Có nhiều "
        "phương tiện để điều khiển các biến này, nhưng họ bộ điều khiển PID từ trước tới nay vẫn đảm "
        "nhận phần lớn trách nhiệm ấy, và nhờ tính đơn giản và độ tin cậy, nó sẽ tiếp tục đảm nhận "
        "trong tương lai."))
    b.append(p(
        "Từ viết tắt PID là tên của ba chế độ điều khiển chính, mỗi chế độ thể hiện một quan hệ toán "
        "học giữa biến được điều khiển c và biến điều khiển m do đầu ra bộ điều khiển tác động. "
        "Chế độ tỉ lệ liên hệ sự thay đổi của m với sự thay đổi của c qua một hệ số khuếch đại tỉ lệ. "
        "Chế độ tích phân làm đầu ra thay đổi với tốc độ liên hệ với độ lệch của c so với giá trị "
        "mong muốn của nó — gọi là giá trị đặt hay giá trị tham chiếu r. Cuối cùng, chế độ đạo hàm "
        "làm đầu ra thay đổi theo đạo hàm thời gian, tức tốc độ thay đổi, của c. Điều đáng chú ý là "
        "các quan hệ toán học này thực ra chỉ được xác lập <i>sau khi</i> người ta đã chế tạo ra các "
        "bộ điều khiển để giải các bài toán điều khiển quá trình. Chế độ tích phân ban đầu được gọi "
        "là <i>đặt lại tự động</i>, còn chế độ đạo hàm được gọi là <i>đặt lại siêu cao</i> hay "
        "<i>tác động trước</i> [1]."))

    # ---------------------------------------------------------------- 97.2
    b.append(h2("97.2 Vòng hở và vòng kín", "Open and Closed Loops"))
    b.append(p(
        "Hình 97.1 mô tả đối tượng và bộ điều khiển bằng các khối chức năng mắc thành một vòng. Đầu "
        "vào của đối tượng là biến điều khiển m và biến tải q, thường là tốc độ dòng vật chất hay "
        "năng lượng đi vào hoặc đi ra khỏi đối tượng. Tải có thể là một biến đơn lẻ hoặc một tổ hợp "
        "các biến, có thể độc lập, có thể là biến điều khiển, hoặc do một bộ điều khiển khác điều "
        "khiển. Nếu độc lập thì tải thường không đo được, và giá trị của nó được suy ra từ mức đầu ra "
        "bộ điều khiển cần thiết để giữ biến được điều khiển ở giá trị đặt. Nhiễu u được vẽ là tác "
        "động trực tiếp lên biến được điều khiển, thường gây ra bởi chảy rối cục bộ trong các phép đo "
        "lưu lượng, áp suất và mức chất lỏng, hoặc bởi tính không đồng nhất của các dòng mà thành "
        "phần của chúng được đo."))
    b.append(fig(1, F.fig(1)))

    b.append(h3("Đáp ứng vòng hở", "Open-Loop Responses"))
    b.append(p(
        "Khi không có điều khiển tự động, biến được điều khiển chịu tác động của những thay đổi tải "
        "và của những điều chỉnh bằng tay lên m mà người vận hành thực hiện không liên tục. Những tác "
        "động này làm c thay đổi theo cả hàm xác lập lẫn hàm động học xuất hiện trên Hình 97.1:"))
    b.append(eq("c = K<sub>p</sub>(m g<sub>m</sub> − q g<sub>q</sub>) + u", "97.1"))
    b.append(p(
        "trong đó K<sub>p</sub> là hệ số khuếch đại xác lập, g<sub>m</sub> và g<sub>q</sub> lần lượt là "
        "các vectơ hệ số khuếch đại động trên đường đi của biến điều khiển và của tải, còn u là mức "
        "nhiễu. Các vectơ này có cả biên độ và góc pha, và cả hai đều là hàm của tần số hay chu kỳ "
        "của tín hiệu đi qua. Trong vòng hở, những thay đổi của m thường là các bước nhảy do người "
        "vận hành tạo ra, nhưng thay đổi của q có thể có dạng bất kỳ — bước nhảy, hàm dốc, biến thiên "
        "ngẫu nhiên hay dao động chu kỳ — tuỳ nguồn gây nhiễu. Bước nhảy dễ tạo ra bằng tay và chứa "
        "mọi tần số từ không đến vô cùng; vì vậy chúng rất hữu ích để đánh giá đáp ứng của vòng và "
        "kiểm tra hiệu quả của bộ điều khiển. Nhiễu được đặc trưng bởi những biến thiên ngẫu nhiên "
        "trong một dải tần số nằm trên băng thông của vòng điều khiển."))
    b.append(p(
        "Các phần tử động học thường gồm thời gian chết và các khâu trễ. Tuy nhiên, mức chất lỏng là "
        "<i>tích phân</i> của hiệu giữa lưu lượng vào và lưu lượng ra [2]; trong trường hợp đó "
        "K<sub>p</sub> trên Hình 97.1 được thay bằng một khâu tích phân. Khi ấy mọi chênh lệch giữa "
        "lưu lượng vào và lưu lượng ra đều bị tích phân, làm mức chất lỏng tiếp tục dâng lên hoặc hạ "
        "xuống cho tới khi chạm giới hạn của bình. Quá trình này không có khả năng tự cân bằng, và do "
        "đó không thể để vòng hở vô thời hạn."))

    b.append(h3("Đáp ứng vòng kín", "Closed-Loop Responses"))
    b.append(p("Trong vòng kín, c đáp ứng với tải và với giá trị đặt như sau:"))
    b.append(eq("c = (r g<sub>q</sub>)/[1 + 1/(K<sub>p</sub>g<sub>m</sub>K<sub>c</sub>g<sub>c</sub>)] "
                "− (q g<sub>q</sub>)/[g<sub>m</sub>K<sub>c</sub>g<sub>c</sub> + 1/K<sub>p</sub>] + u",
                "97.2"))
    b.append(p(
        "trong đó K<sub>c</sub> là hệ số khuếch đại tỉ lệ của bộ điều khiển, g<sub>c</sub> là hệ số "
        "khuếch đại động của các chế độ tích phân và đạo hàm, còn g<sub>r</sub> là hệ số khuếch đại "
        "động của bộ lọc lệnh đặt. Với đối tượng tự cân bằng điển hình ở vòng hở, sau một bước nhảy "
        "tải thì c sẽ đi theo một đường hàm mũ, như đường gạch trên Hình 97.2. Nếu vòng được đóng "
        "lại, bộ điều khiển có thể tác động lên m để đưa c trở về r theo đường liền trên Hình 97.2 — "
        "một quỹ đạo tối ưu có tích phân trị tuyệt đối của sai số (IAE) giữa c và r là nhỏ nhất. "
        "Sườn lên của đường cong phụ thuộc g<sub>q</sub>, còn sườn xuống phụ thuộc g<sub>m</sub> và "
        "các thông số đặt của PID. Nếu các thông số PID được tối ưu cho đáp ứng tải thì chúng thường "
        "làm c vượt quá một thay đổi của giá trị đặt r, như đường gạch trên Hình 97.3. Nếu sau đó "
        "chỉnh lại thông số PID để giảm độ vọt của đáp ứng lệnh đặt thì đáp ứng tải lại bị kéo dài. "
        "Một giải pháp được ưa chuộng hơn là chèn một bộ lọc trễ–sớm vào đường lệnh đặt, và bộ lọc "
        "ấy cho đường liền trên Hình 97.3."))
    b.append(fig(2, F.fig(2)))
    b.append(fig(3, F.fig(3)))

    # ---------------------------------------------------------------- 97.3
    b.append(h2("97.3 Chọn chế độ", "Mode Selection"))
    b.append(p(
        "Họ bộ điều khiển PID gồm P, I, PI, PD và hai loại PID. Mỗi loại có ưu điểm và hạn chế riêng, "
        "và do đó có phạm vi ứng dụng ưu tiên riêng. Dưới đây trình bày từng loại kèm một ứng dụng."))

    b.append(h3("Điều khiển tỉ lệ", "Proportional Control"))
    b.append(p(
        "Trong bộ điều khiển tỉ lệ, độ lệch giữa c và r phải thay đổi thì đầu ra mới thay đổi:"))
    b.append(eq("m = b ± K<sub>c</sub>(r − c)", "97.3"))
    b.append(p(
        "trong đó b là một giá trị nền điều chỉnh được, còn gọi là “đặt lại bằng tay”, và dấu của độ "
        "lệch được chọn sao cho có phản hồi âm. Một số bộ điều khiển cho phép điều chỉnh hệ số khuếch "
        "đại tỉ lệ dưới dạng <i>dải tỉ lệ</i> phần trăm P, với K<sub>c</sub> = 100/P. Nếu m phải "
        "chuyển sang một giá trị xác lập khác vì tải hay giá trị đặt thay đổi thì độ lệch cũng sẽ "
        "thay đổi. Vì vậy bộ điều khiển tỉ lệ luôn để lại một <i>sai lệch tĩnh</i> giữa c và r mỗi "
        "khi m khác b, và chỉ có thể khử sai lệch ấy bằng cách đặt lại b bằng tay. Điều khiển tỉ lệ "
        "được khuyến nghị cho mức chất lỏng, nơi có thể đặt K<sub>c</sub> khá lớn mà không mất ổn "
        "định và không phải chịu thiệt hại kinh tế nào vì sai lệch tĩnh."))
    b.append(p(
        "Điều khiển tỉ lệ mức chất lỏng thực ra là lựa chọn ưu tiên khi biến điều khiển là lưu lượng "
        "ra khỏi bình, và dòng ấy lại là nguyên liệu cấp cho một quá trình hạ nguồn quan trọng. Đặt "
        "K<sub>c</sub> hơi lớn hơn 1,0 sẽ giữ được mức trong bình với mọi tốc độ dòng vào, đồng thời "
        "làm tốc độ thay đổi của lưu lượng ra là nhỏ nhất. Ứng dụng này được gọi là <i>điều khiển "
        "mức trung bình hoá</i> [2]."))

    b.append(h3("Điều khiển tích phân", "Integral Control"))
    b.append(p(
        "Chế độ tích phân khử sai lệch tĩnh bằng cách làm đầu ra thay đổi với tốc độ tỉ lệ với độ "
        "lệch:"))
    b.append(eq("dm/dt = C ± (r − c)/I", "97.4"))
    b.append(p(
        "trong đó t là thời gian, d là toán tử vi phân, I là thông số thời gian tích phân; C là hằng "
        "số tích phân, tức giá trị đầu của đầu ra bộ điều khiển khi đưa sang chế độ tự động. Một số "
        "bộ điều khiển cho phép điều chỉnh thời gian tích phân dưới dạng hệ số khuếch đại tích phân, "
        "hay “tốc độ đặt lại”, 1/I, với đơn vị là nghịch đảo thời gian, tức “số lần lặp trên phút”. "
        "Phép tích phân tạo ra một độ trễ pha 90° giữa đầu vào và đầu ra, làm tăng thời gian đáp ứng "
        "và chu kỳ dao động của vòng. Bộ điều khiển tích phân <i>không</i> dùng được cho mức chất "
        "lỏng, vì hai khâu tích phân mắc nối tiếp tạo thành một vòng kín không ổn định [2]. Công dụng "
        "của nó chỉ giới hạn ở việc tối ưu hoá giá trị đặt của những vòng kín khác vốn đã ổn định "
        "[2]."))

    b.append(h3("Điều khiển PI", "PI Control"))
    b.append(p("Bộ điều khiển PI kết hợp chế độ tỉ lệ và chế độ tích phân:"))
    b.append(eq("m = C ± K<sub>c</sub>[r − c + (1/I)∫(r − c)dt]", "97.5"))
    b.append(p(
        "Độ lệch và tích phân của nó được cộng theo kiểu vectơ, tạo ra một độ trễ pha nằm trong "
        "khoảng từ 0 đến 90°. Sự kết hợp này vừa cho ổn định vừa khử được sai lệch tĩnh, khiến nó "
        "trở thành bộ điều khiển thông dụng nhất trong các ngành chế biến chất lỏng. Nó được dùng gần "
        "như phổ biến tuyệt đối, kể cả trong những ứng dụng mà các bộ điều khiển khác phù hợp hơn."))

    b.append(h3("Điều khiển PD", "PD Control"))
    b.append(p(
        "Thêm tác động đạo hàm vào bộ điều khiển tỉ lệ sẽ bổ sung đáp ứng theo tốc độ thay đổi của "
        "biến được điều khiển:"))
    b.append(eq("m = b ± K<sub>c</sub>(r − c − D dc/dt)", "97.6"))
    b.append(p(
        "trong đó D là thông số thời gian đạo hàm. Tác động đạo hàm nên chỉ tác động lên c như đã chỉ "
        "ra, mà không tác động lên giá trị đặt, vì làm vậy chỉ khiến độ vọt của đáp ứng lệnh đặt tăng "
        "thêm. Một hàm đạo hàm thuần có hệ số khuếch đại động tăng không giới hạn theo tần số — để "
        "tránh mất ổn định ngay bên trong bộ điều khiển, người ta thường hạn chế nó ở khoảng 10 bằng "
        "cách lọc. Cách này cho một sự kết hợp tối ưu giữa độ nhanh nhạy và khả năng chống nhiễu. "
        "Tuy vậy, hệ số khuếch đại cao ở tần số cao vẫn khuếch đại nhiễu trong các phép đo lưu lượng "
        "và mức chất lỏng đủ mạnh để không cho phép dùng chế độ đạo hàm trên những vòng ấy; các phép "
        "đo nhiệt độ thường không có nhiễu, nên có thể dùng chế độ này có lợi ở đó. Độ sớm pha do "
        "chế độ đạo hàm tạo ra làm giảm chu kỳ dao động và thời gian xác lập của vòng, đồng thời cải "
        "thiện độ ổn định."))
    b.append(p(
        "Bộ điều khiển PD được khuyến nghị cho các quá trình gián đoạn, nơi vận hành bắt đầu với c "
        "nằm xa r và kết thúc lý tưởng ở c = r với các dòng đều bằng không. Bộ điều khiển PD phải "
        "được đặt nền cho trạng thái đầu ra cuối cùng này, với D được điều chỉnh để khử độ vọt — đối "
        "với quá trình không tải thì độ vọt ấy là thường trực [2]."))

    b.append(h3("Bộ điều khiển PID", "PID Controllers"))
    b.append(p(
        "Trong một bộ điều khiển PID được chỉnh đúng, độ sớm pha của tác động đạo hàm bù nhiều hơn "
        "mức độ trễ pha của khâu tích phân, dẫn tới một độ sớm pha ròng và thường chỉ còn khoảng một "
        "nửa IAE so với bộ điều khiển PI áp dụng cho cùng quá trình. Có hai loại bộ điều khiển PID "
        "được dùng phổ biến, khác nhau ở cách kết hợp các chế độ [3]. Các bộ điều khiển thời kỳ đầu "
        "kết hợp tác động PD và PI <i>nối tiếp</i>, tức nhân các hàm ấy với nhau thay vì cộng chúng. "
        "Những bộ điều khiển PID <i>tương tác</i> này vẫn còn thông dụng, kể cả khi được thực hiện "
        "bằng kỹ thuật số. Các bộ điều khiển <i>không tương tác</i> kết hợp chế độ tích phân và chế "
        "độ đạo hàm song song, cho một biểu thức PID thuần về mặt toán học hơn:"))
    b.append(eq("m = C ± K<sub>c</sub>[r − c − (1/I)∫(r − c)dt − D dc/dt]", "97.7"))
    b.append(p(
        "Bộ điều khiển tương tác cũng có thể được mô tả bằng đúng dạng ấy, nhưng hệ số của từng số "
        "hạng thì khác [3]. Thời gian tích phân hiệu dụng của bộ điều khiển tương tác là I + D, thời "
        "gian đạo hàm hiệu dụng của nó là 1/(1/I + 1/D), và hệ số khuếch đại tỉ lệ của nó được nhân "
        "thêm 1 + D/I. Như vậy, kết quả chính của sự tương tác giữa các chế độ là buộc phải dùng "
        "những thông số PID khác nhau cho hai bộ điều khiển khi áp dụng lên cùng một quá trình."))
    b.append(p(
        "Sơ đồ khối của một bộ điều khiển PID tương tác thương mại được trình bày trên Hình 97.4, "
        "với các hàm truyền mô tả bằng biến đổi Laplace mà toán tử s của nó tương đương với toán tử "
        "vi phân d/dt. Phép tích phân đạt được nhờ phản hồi dương đầu ra qua một khâu trễ bậc một có "
        "hằng số thời gian đặt bằng thời gian tích phân. Tín hiệu phản hồi f được lấy <i>sau</i> các "
        "giới hạn trên và dưới, và có thể thay bằng một hằng số hay một biến khác để dừng tích phân; "
        "khi ấy bộ điều khiển hành xử như bộ PD có nền từ xa. Tính năng này cực kỳ có giá trị trong "
        "việc ngăn hiện tượng dồn tích phân (<i>reset windup</i>) — hiện tượng xảy ra mỗi khi một bộ "
        "điều khiển có tác động tích phân còn ở chế độ tự động trong lúc vòng đang hở, và dẫn tới độ "
        "vọt lớn khi vòng được đóng lại [3]. Phần lớn các bộ điều khiển không tương tác thiếu tính "
        "năng này."))
    b.append(p(
        "Tác động đạo hàm kết hợp một khâu vi phân Ds với một khâu trễ (bộ lọc) có hằng số thời gian "
        "αD, trong đó α biểu thị nghịch đảo của giới hạn hệ số khuếch đại ở tần số cao, thường bằng "
        "10. Hình 97.4 cũng cho thấy một bộ lọc trễ–sớm cho lệnh đặt, có hằng số thời gian trễ bằng "
        "thời gian tích phân I và thời gian sớm bằng G<sub>r</sub>I, tạo ra hệ số khuếch đại "
        "G<sub>r</sub> đối với một bước nhảy của giá trị đặt. Hệ số này điều chỉnh được từ 0 đến 1, "
        "với 1 là khử hẳn bộ lọc và 0 là áp đặt một khâu trễ bậc một. Tác dụng của khâu trễ này "
        "tương đương với việc loại bỏ tác động tỉ lệ khỏi r trong các phương trình 97.5 và 97.7 — "
        "một tính năng tuỳ chọn ở một số bộ điều khiển PID. Việc điều chỉnh hệ số khuếch đại cho độ "
        "linh hoạt cao hơn trong việc tối ưu đáp ứng lệnh đặt như trên Hình 97.3; G<sub>r</sub> được "
        "đặt khoảng 0,3 cho các quá trình trội trễ như quá trình mô tả trên Hình 97.2 và 97.3, và "
        "gần bằng 1 cho các quá trình trội thời gian chết [3]."))
    b.append(fig(4, F.fig(4)))

    # ---------------------------------------------------------------- 97.4
    b.append(h2("97.4 Phần cứng bộ điều khiển", "Controller Hardware"))
    b.append(p(
        "Các bộ điều khiển tỉ lệ kiểu khí nén được dùng lần đầu vào đầu thế kỷ này, với chức năng "
        "tích phân rồi chức năng đạo hàm được bổ sung vào khoảng năm 1930. Bộ điều khiển khí nén vẫn "
        "được dùng trong các khu vực nguy hiểm, ở những mỏ khí xa xôi nơi chúng hoạt động nhờ chính "
        "khí, và cho những nhiệm vụ đơn giản như điều hoà nhiệt độ trong các toà nhà. Bộ điều khiển "
        "tương tự điện tử bắt đầu thay thế bộ điều khiển khí nén vào cuối những năm 1950, nhưng các "
        "chức năng của chúng được thực hiện bằng bộ vi xử lý số từ khoảng năm 1980. Điều khiển số "
        "khởi đầu trên máy tính lớn vào những năm 1960, còn ngày nay nó có mặt trong các bộ điều "
        "khiển logic khả trình (PLC), máy tính cá nhân (PC) và các hệ điều khiển phân tán (DCS)."))

    b.append(h3("Bộ điều khiển khí nén", "Pneumatic Controllers"))
    b.append(p(
        "Những bộ điều khiển khí nén đơn giản nhất là các bộ điều khiển tỉ lệ dùng để điều khiển hệ "
        "thống sưởi, thông gió và điều hoà không khí (HVAC) trong các toà nhà. Tuy vậy, cũng có "
        "những bộ điều khiển PID hoàn chỉnh với chức năng tương tự như trên Hình 97.4, dùng cho "
        "những nhiệm vụ đòi hỏi cao như điều khiển nhiệt độ các lò phản ứng toả nhiệt gián đoạn và "
        "điều chỉnh lưu lượng, áp suất trên các giàn khoan dầu ngoài khơi. Có cả loại gắn bảng điều "
        "khiển lẫn loại vỏ chịu thời tiết dùng để lắp đặt tại hiện trường. Phần lớn đều có trạm "
        "chuyển đổi tự động–bằng tay với khả năng chuyển đổi không đột biến giữa hai chế độ vận "
        "hành. Hạn chế chính của chúng là tốc độ đáp ứng bị giới hạn bởi đường truyền (chiều dài "
        "vượt quá 30 m không thích hợp cho điều khiển lưu lượng và áp suất) và thiếu năng lực tính "
        "toán (vốn cần cho việc mô tả đặc tính phi tuyến và tự chỉnh định)."))

    b.append(h3("Bộ điều khiển điện tử", "Electronic Controllers"))
    b.append(p(
        "Những bộ điều khiển điện tử đầu tiên bắt chước các bộ điều khiển khí nén nhưng khử được độ "
        "trễ truyền dẫn. Về sau, người ta bổ sung khả năng chuyển đổi tự động–bằng tay và chỉnh định từ "
        "xa, rồi bộ vi xử lý đem lại cho các bộ điều khiển này các chức năng tính toán và logic, điều "
        "chỉnh và mô tả đặc tính tín hiệu, cùng các tính năng tự chỉnh định và tự chỉnh. Thậm chí có "
        "loại nhiều bộ điều khiển trong cùng một trạm để thực hiện các hệ tầng nối và hệ bù trước. "
        "Băng thông của bộ điều khiển tương tự điện tử mở rộng tới 10 Hz, và ở một số thiết bị còn "
        "xa hơn. Bộ điều khiển số thực hiện các phép tính một cách ngắt quãng chứ không liên tục; "
        "phần lớn bị giới hạn ở tần số làm việc 10 Hz, và khi kết hợp với lọc số thì điều đó dẫn tới "
        "một thời gian chết hiệu dụng 0,1 s, làm băng thông giảm xuống còn khoảng 1,3 Hz."))
    b.append(p(
        "Bộ điều khiển điện tử được dùng rộng rãi tại hiện trường và chuyên dụng cho việc điều khiển "
        "từng thiết bị riêng lẻ như bơm, máy sấy, trạm xử lý nước thải — bất cứ nơi nào chỉ cần vài "
        "vòng điều khiển. Một số bộ điều khiển có khả năng truyền thông ngang hàng để hoà vào mạng, "
        "và phần lớn có thể trao đổi với máy tính cá nhân, nơi dữ liệu được hiển thị trên một giao "
        "diện đồ hoạ. Việc cấu hình (chọn thang đo, chế độ điều khiển, cảnh báo và các chức năng "
        "khác) có thể thực hiện qua các phím trên mặt máy hoặc qua PC."))

    b.append(h3("Bộ điều khiển số", "Digital Controllers"))
    b.append(p(
        "Trong khi bộ điều khiển số độc lập tiến hoá từ các mẫu tương tự điện tử thì bộ điều khiển "
        "số tập trung lại bắt nguồn từ máy tính số. Máy tính lớn được dùng đầu tiên cho điều khiển "
        "số trực tiếp (DDC), trong đó van do máy tính tác động, và cho điều khiển giám sát, trong đó "
        "máy tính đặt vị trí các giá trị đặt của những bộ điều khiển tương tự. Dần dần máy tính mini "
        "và bộ vi xử lý thay thế máy tính lớn, với các chức năng được phân tán cho các mô-đun vào–ra "
        "hiện trường, trạm làm việc, mô-đun điều khiển, v.v., trong những cụm và những cấu hình khác "
        "nhau gọi là DCS. PC được dùng cho một số trạm làm việc, và thậm chí cho điều khiển trực "
        "tiếp ở một số nhà máy."))
    b.append(p(
        "Ở những nơi nhiều vòng được điều khiển bởi một bộ xử lý duy nhất, khoảng thời gian giữa hai "
        "lần lấy mẫu có thể là 0,5 s hoặc lâu hơn. Người dùng có xu hướng cứ mở rộng mãi những chức "
        "năng đòi hỏi ở bộ xử lý, và do đó kéo dài thêm khoảng thời gian giữa hai lần lấy mẫu. Điều "
        "này làm giảm băng thông của các bộ điều khiển DCS xuống những giá trị quá thấp so với yêu "
        "cầu của điều khiển buồng đốt và máy nén. Một số thuật toán PID số tạo ra đầu ra gia số Δm, "
        "đòi hỏi phải có một khâu tích phân ở phía sau để tạo ra m. Những bộ điều khiển này không có "
        "tác động tỉ lệ hay PD vì chúng không có giá trị nền cố định b, mà chỉ có một hằng số tích "
        "phân C dễ bị thay đổi mỗi khi bộ điều khiển được vận hành bằng tay."))
    b.append(p(
        "PLC ban đầu là thiết bị thay thế cho logic rơ-le. Về sau các vòng PID được bổ sung, và chúng "
        "thường hoạt động nhanh hơn nhiều (ví dụ 100 Hz) so với các bộ điều khiển số khác. Tuy nhiên, "
        "nhiều loại có thuật toán phi tiêu chuẩn và thiếu những chức năng của các bộ điều khiển PID "
        "khác, như điều khiển tỉ lệ và PD, bảo vệ chống dồn tích phân, lọc đạo hàm, lọc lệnh đặt, mô "
        "tả đặc tính phi tuyến và tự chỉnh định."))

    # ---------------------------------------------------------------- 97.5
    b.append(h2("97.5 Chỉnh định bộ điều khiển", "Tuning Controllers"))
    b.append(p(
        "Một bộ điều khiển chỉ hiệu quả đúng bằng mức độ chỉnh định của nó: việc điều chỉnh các thông số "
        "PID sao cho phù hợp với các tham số quá trình nhằm tối ưu đáp ứng tải và đáp ứng lệnh đặt "
        "như mô tả trên Hình 97.2 và 97.3. Việc chỉnh định là cần thiết khi bộ điều khiển lần đầu được "
        "đưa vào vận hành trên một vòng, và có thể phải làm lại nếu các tham số quá trình thay đổi "
        "đáng kể theo thời gian, theo tải, theo giá trị đặt, v.v. Chỉnh định đòi hỏi phải tạo ra một "
        "nhiễu loạn ở vòng hở hoặc vòng kín rồi diễn giải đáp ứng thu được. Tự chỉnh định về cơ bản là "
        "tự động hoá các thủ tục thủ công, còn tự chỉnh có thể nhận ra và sửa chữa một đáp ứng không "
        "đạt yêu cầu mà không cần thử nghiệm."))

    b.append(h3("Chỉnh định bằng tay", "Manual Tuning"))
    b.append(p(
        "Ziegler và Nichols [1] đã xây dựng những phương pháp chỉnh định hiệu quả đầu tiên, và chúng "
        "vẫn còn được dùng tới ngày nay. Phương pháp vòng hở của họ cho đầu ra bộ điều khiển nhảy "
        "bước để tạo ra một đáp ứng như đường gạch trên Hình 97.2. Thời gian chết (độ trễ) biểu kiến "
        "trong đáp ứng và độ dốc lớn nhất của đường cong sau đó được chuyển thành các thông số thích "
        "hợp cho bộ điều khiển PI và PID bằng những công thức đơn giản. Phương pháp vòng hở chính "
        "xác nhất đối với các quá trình trội trễ, nhưng phương pháp vòng kín lại áp dụng được rộng "
        "hơn. Phương pháp vòng kín dựa trên việc tạo ra một dao động đều bằng cách điều chỉnh hệ số "
        "khuếch đại của bộ điều khiển khi chỉ có chế độ tỉ lệ của nó tác động (D đặt bằng 0 và I đặt "
        "ở mức lớn nhất). Chu kỳ của dao động và hệ số khuếch đại của bộ điều khiển sau đó được dùng "
        "để tính các thông số PID thích hợp."))
    b.append(p(
        "Phương pháp vòng hở đã được mở rộng cho các quá trình khác [3], nhưng vẫn bị hạn chế bởi độ "
        "chính xác của kết quả thử bước. Việc tinh chỉnh phải thực hiện với vòng đã đóng: khi độ lệch "
        "bằng không, đưa bộ điều khiển sang chế độ bằng tay, cho đầu ra nhảy bước rồi chuyển ngay "
        "sang chế độ tự động — cách này mô phỏng một thay đổi tải ở vòng kín. Đáp ứng thu được phải "
        "giống đường liền trên Hình 97.2, với đỉnh thứ nhất đối xứng, tiếp theo là một độ vọt nhẹ và "
        "một dao động tắt tốt. Nếu độ vọt quá lớn thì nên tăng thời gian I và/hoặc D; nếu có vọt "
        "xuống dưới thì nên giảm chúng. (Để đơn giản hoá việc chỉnh định bộ điều khiển PID, có thể dịch "
        "chuyển I và D cùng nhau, giữ tỉ số I/D khoảng 4 đối với bộ điều khiển không tương tác và "
        "khoảng 3 đối với bộ điều khiển tương tác.) Nếu tắt quá nhẹ thì hạ hệ số khuếch đại tỉ lệ; "
        "nếu hồi phục chậm (tạo ra đỉnh thứ nhất không đối xứng) thì nâng hệ số khuếch đại tỉ lệ. "
        "Không nên cho giá trị đặt nhảy bước để thử nghiệm, trừ khi đáp ứng lệnh đặt là quan trọng, "
        "như với các bộ điều khiển lưu lượng."))

    b.append(h3("Tự chỉnh định", "Autotuning"))
    b.append(p(
        "Một số bộ điều khiển tự chỉnh định dùng phép thử bước ở vòng hở, thực hiện các quy tắc "
        "Ziegler–Nichols. Một xung đơn cho kết quả nhận dạng chính xác hơn, và một xung kép (doublet) "
        "còn tốt hơn nữa [3]. Một phương pháp vòng kín thay việc tạo dao động bằng khâu tỉ lệ bằng "
        "việc tạo dao động bằng rơ-le, trong đó đầu ra chuyển giữa giới hạn trên và giới hạn dưới mỗi "
        "khi c vượt qua r [3]. Chu kỳ của dao động thu được được dùng để đặt I và D, còn biên độ của "
        "nó so với khoảng cách giữa hai giới hạn đầu ra được dùng để đặt K<sub>c</sub>. Hạn chế chính "
        "của các phương pháp tự chỉnh định bằng bước và bằng rơ-le là chúng chỉ dùng hai đặc trưng của "
        "đáp ứng để nhận dạng một quá trình phức tạp. Các thông số PID ước lượng được có thể không "
        "khớp lắm với quá trình cụ thể, dẫn tới mất ổn định ở một số vòng và chậm chạp ở những vòng "
        "khác. Chức năng tự chỉnh định không thể tự giám sát hiệu quả công việc của mình, trong khi tự "
        "chỉnh thì làm được."))

    b.append(h3("Tự chỉnh", "Self-Tuning"))
    b.append(p(
        "Bộ điều khiển tự chỉnh không cần thử nghiệm quá trình mà chỉ quan sát đáp ứng vòng kín của "
        "nó đối với những thay đổi giá trị đặt và tải với các thông số PID hiện hành. Sau đó nó thực "
        "hiện việc tinh chỉnh như mô tả ở trên để đưa độ vọt, độ tắt hoặc tính đối xứng của đường "
        "cong đáp ứng lại gần mức tối ưu hơn. Việc này có thể cần vài lần lặp nếu các thông số PID "
        "còn xa mức tối ưu, nhưng cuối cùng có thể hội tụ về đáp ứng tối ưu và điều chỉnh lại khi "
        "các tham số quá trình thay đổi. Khi không có nhiễu loạn thử nghiệm thì vẫn có thể nhận dạng "
        "sai, đặc biệt với một nhiễu loạn hình sin, khi ấy việc nới lỏng có thể xảy ra trong khi siết "
        "chặt lại sẽ cho điều khiển tốt hơn."))

    # ---------------------------------------------------------------- terms
    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(dt("Điều khiển mức trung bình hoá (<i>averaging level control</i>)",
                "cho phép mức chất lỏng trong bình thay đổi nhằm giảm thiểu những thay đổi của lưu "
                "lượng ra."))
    b.append(dt("Đáp ứng vòng kín (<i>closed-loop response</i>)",
                "đáp ứng của biến được điều khiển đối với những thay đổi của giá trị đặt hoặc của "
                "tải khi bộ điều khiển ở chế độ tự động."))
    b.append(dt("Tác động đạo hàm (<i>derivative action</i>)",
                "sự thay đổi của đầu ra bộ điều khiển để đáp lại tốc độ thay đổi của biến được điều "
                "khiển."))
    b.append(dt("Hệ số khuếch đại động (<i>dynamic gain</i>)",
                "tỉ số giữa thay đổi ở đầu ra của một hàm và thay đổi ở đầu vào của nó, đại lượng này "
                "biến thiên theo thời gian hoặc theo tần số của đầu vào."))
    b.append(dt("Tác động tích phân (<i>integral action</i>)",
                "tốc độ thay đổi của đầu ra bộ điều khiển để đáp lại độ lệch giữa biến được điều "
                "khiển và giá trị đặt."))
    b.append(dt("Tải (<i>load</i>)",
                "một biến hoặc một tổ hợp biến có ảnh hưởng lên biến được điều khiển."))
    b.append(dt("Biến điều khiển (<i>manipulated variable</i>)",
                "biến được bộ điều khiển thay đổi nhằm làm dịch chuyển biến được điều khiển."))
    b.append(dt("Nhiễu (<i>noise</i>)",
                "một nhiễu loạn có dải tần số quá cao để bộ điều khiển có thể tác động lên."))
    b.append(dt("Sai lệch tĩnh (<i>offset</i>)",
                "độ lệch xác lập giữa biến được điều khiển và giá trị đặt."))
    b.append(dt("Đáp ứng vòng hở (<i>open-loop response</i>)",
                "đáp ứng của biến được điều khiển đối với các đầu vào của quá trình khi không có tác "
                "động điều khiển."))
    b.append(dt("Tác động tỉ lệ (<i>proportional action</i>)",
                "sự thay đổi của đầu ra bộ điều khiển đáp lại trực tiếp một thay đổi của biến được "
                "điều khiển."))
    b.append(dt("Dải tỉ lệ (<i>proportional band</i>)",
                "phần trăm thay đổi của biến được điều khiển cần thiết để làm đầu ra bộ điều khiển "
                "chạy hết thang."))
    b.append(dt("Tự cân bằng (<i>self-regulation</i>)",
                "tính chất của một quá trình mà nhờ đó một thay đổi của biến được điều khiển tác động "
                "lên dòng vào hoặc dòng ra của quá trình theo cách làm giảm bớt những thay đổi tiếp "
                "theo của chính biến ấy."))
    b.append(dt("Chỉnh định (<i>tuning</i>)",
                "việc điều chỉnh các thông số đặt của một bộ điều khiển nhằm tác động lên hiệu năng "
                "của nó."))
    b.append(dt("Dồn tích phân (<i>windup</i>)",
                "hiện tượng bão hoà khâu tích phân của bộ điều khiển, khiến biến được điều khiển sau "
                "đó vượt quá giá trị đặt."))

    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "Mục lục của bản gốc in nhầm “Self-Turning” cho mục 97.5, trong khi tiêu đề mục và toàn bộ "
        "phần thân bài đều viết “Self-Tuning” (tự chỉnh); bản dịch giữ theo cách viết đúng. Ngoài ra, "
        "trong phương trình 97.2 bản gốc in hai phân số chồng; ở đây chúng được trình bày lại bằng "
        "dấu gạch chéo trong ngoặc vuông cho phù hợp với khuôn khổ trình bày của bản dịch, nội dung "
        "toán học không đổi."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. G. Ziegler and N. B. Nichols, “Optimum settings for automatic controllers,” "
        "<i>Trans. ASME</i>, November 1942, 759–768.",
        "F. G. Shinskey, <i>Process Control Systems</i>, 4th ed., New York: McGraw-Hill, 1996, "
        "22–25, 25–28, 192–194, 388–390.",
        "F. G. Shinskey, <i>Feedback Controllers for the Process Industries</i>, New York: "
        "McGraw-Hill, 1994, 68–70, 176–178, 157–164, 148–151, 155–156.",
    ]))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []

    b.append(h2("97.1 Introduction"))
    b.append(p(
        "Process control plays an essential role in the safe manufacture of quality products at market "
        "demand, while protecting the environment. Flow rates, pressures and temperatures within pipes "
        "and vessels, inventories of liquids and solids, and product quality are all examples of "
        "measured variables that must be controlled to meet those objectives. Several means are "
        "available for controlling these variables, but the PID family of controllers has historically "
        "carried the major share of this responsibility and, because of their simplicity and "
        "reliability, will continue to do so."))
    b.append(p(
        "The acronym PID stands for the three principal modes of the controller, each of which bears a "
        "mathematical relationship between the controlled variable c and the manipulated variable m "
        "driven by the controller output. The proportional mode relates changes in m to changes in c "
        "through a proportional gain. The integral mode moves the output at a rate related to the "
        "deviation of c from its desired value, known as the set point or reference r. The derivative "
        "mode moves the output in response to the time derivative, or rate of change, of c. "
        "Interestingly, these mathematical relationships were actually determined <i>after</i> "
        "controllers had already been created to solve process-control problems. The integral mode was "
        "initially called <i>automatic reset</i>, and the derivative mode <i>hyper-reset</i> or "
        "<i>pre-act</i> [1]."))

    b.append(h2("97.2 Open and Closed Loops"))
    b.append(p(
        "Figure 97.1 describes the process and controller in functional blocks connected in a loop. "
        "Inputs to the process are the manipulated variable m and the load q, usually rates of flow of "
        "material or energy into or out of the process. The load may be a single variable or an "
        "aggregate, either independent or manipulated, or controlled by another controller. If "
        "independent it is often unmeasured, its value being inferred from the level of controller "
        "output required to maintain the controlled variable at set point. Noise u is shown affecting "
        "the controlled variable directly, typically caused by local turbulence in flow, pressure and "
        "liquid-level measurements, or by nonuniformity of streams whose composition is measured."))
    b.append(fig(1, F.fig(1), "en"))

    b.append(h3("Open-Loop Responses"))
    b.append(p(
        "In the absence of automatic control, the controlled variable is subject to variations in the "
        "load and to manual adjustments to m intermittently introduced by operators. These cause "
        "variations in c following both the steady-state and dynamic functions appearing in Fig. 97.1:"))
    b.append(eq("c = K<sub>p</sub>(m g<sub>m</sub> − q g<sub>q</sub>) + u", "97.1"))
    b.append(p(
        "where K<sub>p</sub> is the steady-state gain, g<sub>m</sub> and g<sub>q</sub> are the "
        "dynamic-gain vectors in the manipulated and load paths respectively, and u is the noise level. "
        "The vectors have both magnitude and phase angle, which are functions of the frequency or "
        "period of the signal passing through. In the open loop, variations in m are likely to be steps "
        "introduced by operators, but variations in q could take any form — steps, ramps, random "
        "variations or cycles — depending on the source of the disturbance. Steps are easily introduced "
        "manually and contain all the frequencies from zero to infinity; consequently they are useful "
        "for evaluating loop response and testing the effectiveness of controllers. Noise is typified "
        "by random variations in a frequency range above the bandwidth of the control loop."))
    b.append(p(
        "The dynamic elements typically consist of deadtime and lags. However, liquid level is the "
        "<i>integral</i> of the difference between inflow and outflow [2], in which case K<sub>p</sub> "
        "in Fig. 97.1 is replaced by an integrator. Any difference between inflow and outflow will then "
        "be integrated, causing liquid level to continue rising or falling until the vessel limit is "
        "reached. This process has no self-regulation, and therefore cannot be left indefinitely in an "
        "open loop."))

    b.append(h3("Closed-Loop Responses"))
    b.append(p("In the closed loop, c responds to load and set point as follows:"))
    b.append(eq("c = (r g<sub>q</sub>)/[1 + 1/(K<sub>p</sub>g<sub>m</sub>K<sub>c</sub>g<sub>c</sub>)] "
                "− (q g<sub>q</sub>)/[g<sub>m</sub>K<sub>c</sub>g<sub>c</sub> + 1/K<sub>p</sub>] + u",
                "97.2"))
    b.append(p(
        "where K<sub>c</sub> is the proportional gain of the controller, g<sub>c</sub> the dynamic gain "
        "of its integral and derivative modes, and g<sub>r</sub> that of its set-point filter. For the "
        "typical self-regulating process in the open loop, c will take an exponential path following a "
        "step change in load, as shown by the dashed curve in Fig. 97.2. If the loop is closed, the "
        "controller can move m to return c to r along the solid curve in Fig. 97.2, an optimum "
        "trajectory having a minimum integrated absolute error (IAE) between c and r. The leading edge "
        "of the curve depends on g<sub>q</sub> and the trailing edge on g<sub>m</sub> and the PID "
        "settings. If the PID settings are optimized for load response they will usually cause c to "
        "overshoot a change in set point r, as shown by the dashed curve in Fig. 97.3. If the PID "
        "settings are then readjusted to reduce set-point overshoot, load response is extended. A "
        "preferred solution is to insert a lead–lag filter in the set-point path, which produces the "
        "solid curve in Fig. 97.3."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))

    b.append(h2("97.3 Mode Selection"))
    b.append(p(
        "The family of PID controllers includes P, I, PI, PD and two PID controllers. Each has its own "
        "advantages and limitations, and therefore its preferred range of applications. Each is "
        "outlined below along with an application."))

    b.append(h3("Proportional Control"))
    b.append(p("In a proportional controller, the deviation between c and r must change for the output "
               "to change:"))
    b.append(eq("m = b ± K<sub>c</sub>(r − c)", "97.3"))
    b.append(p(
        "where b is an adjustable bias, also known as “manual reset,” and the sign of the deviation is "
        "selected to provide negative feedback. Some controllers have proportional gain adjustable as "
        "percent proportional band P, where K<sub>c</sub> = 100/P. If m must move to a different "
        "steady-state value because of a change in load or set point, the deviation will also change. "
        "The proportional controller therefore allows a steady-state <i>offset</i> between c and r "
        "whenever m does not equal b, which can only be eliminated by manually resetting b. "
        "Proportional control is recommended for liquid level, where K<sub>c</sub> can be set quite "
        "high without loss of stability and there is no economic penalty for offset."))
    b.append(p(
        "Proportional control of liquid level is actually preferred when manipulating the flow leaving "
        "a tank as the feed to a critical downstream process. Setting K<sub>c</sub> slightly above 1.0 "
        "will keep the level in the tank for all rates of inflow, while minimizing the rate of change "
        "of outflow. This application is called <i>averaging level control</i> [2]."))

    b.append(h3("Integral Control"))
    b.append(p("The integral mode eliminates offset by driving the output at a rate proportional to the "
               "deviation:"))
    b.append(eq("dm/dt = C ± (r − c)/I", "97.4"))
    b.append(p(
        "where t is time, d is the differential operator, I is the integral time setting and C is the "
        "constant of integration, i.e. the initial value of the controller output when placed on "
        "automatic. Some controllers have integral time adjusted as integral gain, or “reset rate,” "
        "1/I in inverse time as “repeats per minute.” Integration produces a phase lag of 90° between "
        "input and output, which increases the response time and period of oscillation of the loop. The "
        "integral controller <i>cannot</i> be used for liquid level, because two integrators in series "
        "form an unstable closed loop [2]. Its use is limited to optimizing the set points of other "
        "closed loops that are already stable [2]."))

    b.append(h3("PI Control"))
    b.append(p("The PI controller combines the proportional and integral modes:"))
    b.append(eq("m = C ± K<sub>c</sub>[r − c + (1/I)∫(r − c)dt]", "97.5"))
    b.append(p(
        "The deviation and its integral are added vectorially, producing a phase lag falling between "
        "0 and 90°. This combination provides stability with elimination of offset, making it the most "
        "common controller used in the fluid-processing industries. It is used almost universally, even "
        "in those applications where other controllers are better suited."))

    b.append(h3("PD Control"))
    b.append(p("The addition of derivative action to a proportional controller adds response for the "
               "rate of change of the controlled variable:"))
    b.append(eq("m = b ± K<sub>c</sub>(r − c − D dc/dt)", "97.6"))
    b.append(p(
        "where D is the derivative time setting. Derivative action is preferably applied only to c as "
        "indicated, and not to the set point, which would only increase set-point overshoot. A pure "
        "derivative function has a dynamic gain increasing indefinitely with frequency — to avoid "
        "instability within the controller it is usually limited to about 10 by filtering. This "
        "provides an optimum combination of responsiveness and noise rejection. Still, the "
        "high-frequency gain amplifies noise in flow and liquid-level measurements enough to prevent "
        "the use of the derivative mode on those loops; temperature measurements are usually noise-free, "
        "allowing it to be used to advantage there. The phase lead provided by the derivative mode "
        "reduces the period of oscillation and settling time of a loop, and improves stability."))
    b.append(p(
        "PD controllers are recommended for batch processes, where operation begins with c away from r "
        "and ends ideally with c = r and flows at zero. The PD controller must be biased for this final "
        "output state, with D adjusted to eliminate overshoot, which for a zero-load process is "
        "permanent [2]."))

    b.append(h3("PID Controllers"))
    b.append(p(
        "The phase lead of derivative action more than offsets the phase lag of integral in a properly "
        "adjusted PID controller, resulting in a net phase lead and typically half the IAE of a PI "
        "controller applied to the same process. There are two types of PID controllers in common use, "
        "which differ in the way the modes are combined [3]. Early controllers combined PD and PI "
        "action in series, multiplying those functions rather than adding them. These <i>interacting</i> "
        "PID controllers remain in common use, even implemented digitally. <i>Noninteracting</i> "
        "controllers combine the integral and derivative modes in parallel, producing a more "
        "mathematically pure PID expression:"))
    b.append(eq("m = C ± K<sub>c</sub>[r − c − (1/I)∫(r − c)dt − D dc/dt]", "97.7"))
    b.append(p(
        "The interacting controller can be described in the same form, but the coefficients of the "
        "individual terms are different [3]. The effective integral time of the interacting controller "
        "is I + D, its effective derivative time is 1/(1/I + 1/D), and its proportional gain is "
        "augmented by 1 + D/I. Thus the principal result of mode interaction is to require different "
        "PID settings for the two controllers applied to the same process."))
    b.append(p(
        "A block diagram of a commercial interacting PID controller appears in Fig. 97.4, with transfer "
        "functions described in Laplace transforms whose operator s is equivalent to the differential "
        "operator d/dt. Integration is achieved by positive feedback of the output through a "
        "first-order lag set at the integral time. The feedback signal f is taken downstream of the "
        "high and low limits, and may be replaced with a constant or other variable to stop "
        "integration, in which case the controller behaves as PD with remote bias. This feature is "
        "extremely valuable in preventing <i>reset windup</i>, which occurs whenever a controller with "
        "integral action remains in automatic while the loop is open, and results in a large overshoot "
        "when the loop is then closed [3]. Most noninteracting controllers lack this feature."))
    b.append(p(
        "Derivative action combines a differentiator Ds with a lag (filter) of time constant αD, where "
        "α represents the inverse of the high-frequency gain limit of typically 10. Figure 97.4 also "
        "shows a lead–lag set-point filter having a lag time constant of integral time I and a lead "
        "time of G<sub>r</sub>I, which produces a gain of G<sub>r</sub> to a step in set point. This "
        "gain is adjustable from 0 to 1, with 1 eliminating the filter and 0 imposing a first-order "
        "lag. The effect of this lag is equivalent to eliminating proportional action from r in "
        "Eqs. 97.5 and 97.7, an optional feature in some PID controllers. The gain adjustment offers "
        "more flexibility in optimizing set-point response as in Fig. 97.3; G<sub>r</sub> is set around "
        "0.3 for lag-dominant processes such as those described in Figs. 97.2 and 97.3, and closer to 1 "
        "for deadtime-dominant processes [3]."))
    b.append(fig(4, F.fig(4), "en"))

    b.append(h2("97.4 Controller Hardware"))
    b.append(p(
        "Pneumatic proportional controllers were first used early in this century, with integral and "
        "then derivative functions added around 1930. Pneumatic controllers are still in use in "
        "hazardous areas, in remote gas fields where they are operated by gas, and for simple tasks "
        "such as regulating temperatures in buildings. Electronic analog controllers began to replace "
        "pneumatic controllers in the late 1950s, but their functions were implemented using digital "
        "microprocessors beginning around 1980. Digital control began in mainframes in the 1960s, but "
        "is now available in programmable logic controllers (PLC), personal computers (PC) and "
        "distributed control systems (DCS)."))

    b.append(h3("Pneumatic Controllers"))
    b.append(p(
        "The simplest pneumatic controllers are proportional units used to control heating, ventilating "
        "and air-conditioning (HVAC) in buildings. However, complete PID controllers with functionality "
        "similar to that shown in Fig. 97.4 are also available, used for such demanding tasks as "
        "temperature control of batch exothermic reactors and regulation of flows and pressures on "
        "offshore oil platforms. Panel-mounted units are available as well as weatherproof models for "
        "field installation. Most have auto–manual transfer stations with bumpless transfer between the "
        "two modes of operation. Their principal limitations are a speed of response limited by "
        "transmission lines (lengths beyond 30 m are unsuitable for flow and pressure control) and a "
        "lack of computing capability (required for nonlinear characterization and automatic tuning)."))

    b.append(h3("Electronic Controllers"))
    b.append(p(
        "The first electronic controllers mimicked their pneumatic counterparts while eliminating "
        "transmission lags. Eventually remote auto–manual transfer and remote tuning were added, and "
        "microprocessors brought these controllers calculation and logic functions, signal conditioning "
        "and characterization, and auto- and self-tuning features as well. Multiple controllers are "
        "even available in a single station for implementing cascade and feedforward systems. The "
        "bandwidth of electronic analog controllers extends to 10 Hz, and in some units even further. "
        "Digital controllers execute their calculations intermittently rather than continuously; most "
        "are limited to 10 Hz operation, which with digital filtering results in an effective deadtime "
        "of 0.1 s, reducing bandwidth to about 1.3 Hz."))
    b.append(p(
        "Electronic controllers are used extensively in field locations and dedicated to the control of "
        "individual units such as pumps, dryers and wastewater-treatment facilities — wherever only a "
        "few loops are required. Peer-to-peer communication is available in some controllers for "
        "incorporation into networks, and most can communicate with personal computers where data can "
        "be displayed on a graphic interface. Configuration (selection of scales, control modes, alarms "
        "and other functions) can be done either via keys on the controller faceplate or through a PC."))

    b.append(h3("Digital Controllers"))
    b.append(p(
        "While the stand-alone digital controller evolved from electronic analog models, centralized "
        "digital controllers originated with digital computers. Mainframe computers were first used for "
        "direct digital control (DDC), where valves were manipulated by the computer, and for "
        "supervisory control, where the computer positioned the set points of analog controllers. "
        "Gradually minicomputers and microprocessors replaced the mainframe, with functions becoming "
        "distributed among field input–output modules, workstations and control modules, in clusters "
        "and other configurations, as DCS. PCs are used for some workstations, and even for direct "
        "control in some plants."))
    b.append(p(
        "Where many loops are controlled by a single processor, the interval between samples is likely "
        "to be 0.5 s or even longer. Users tend to keep expanding the functions demanded of the "
        "processor, thereby extending the interval between samples. This reduces the bandwidth of DCS "
        "controllers to values too low for combustion and compressor controls. Some digital PID "
        "algorithms produce an incremental output Δm, requiring an integrator downstream to produce m. "
        "These are not available in proportional or PD action because they have no fixed bias b, only a "
        "constant of integration C which is subject to change whenever the controller is operated "
        "manually."))
    b.append(p(
        "The PLC was originally a replacement for relay logic. Eventually PID loops were added, which "
        "generally operate much faster (e.g. 100 Hz) than other digital controllers. However, many have "
        "nonstandard algorithms and lack the functionality of other PID controllers, such as "
        "proportional and PD control, windup protection, derivative filtering, set-point filtering, "
        "nonlinear characterization and autotuning."))

    b.append(h2("97.5 Tuning Controllers"))
    b.append(p(
        "A controller is only as effective as its tuning: the adjustment of the PID settings relative "
        "to the process parameters to optimize load and set-point response as described in Figs. 97.2 "
        "and 97.3. Tuning is required when the controller is first commissioned on a loop, and may have "
        "to be repeated if process parameters change appreciably with time, load or set point. Tuning "
        "requires the introduction of a disturbance in either the open or the closed loop, and "
        "interpretation of the resulting response. Autotuning essentially automates manual procedures, "
        "whereas self-tuning can recognize and correct an unsatisfactory response without testing."))

    b.append(h3("Manual Tuning"))
    b.append(p(
        "Ziegler and Nichols [1] developed the first effective tuning methods, and these are still used "
        "today. Their open-loop method steps the controller output to produce a response like the "
        "broken curve in Fig. 97.2. The apparent deadtime (delay) in the response and the steepest "
        "slope of the curve are then converted into appropriate settings for PI and PID controllers "
        "using simple formulas. The open-loop method is most accurate for lag-dominant processes, but "
        "the closed-loop method is more broadly applicable. It is based on inducing a uniform cycle by "
        "adjusting the gain of a controller with only its proportional mode effective (D set to 0 and I "
        "at maximum). The period of the cycle and the controller gain are then used to calculate "
        "appropriate PID settings."))
    b.append(p(
        "The open-loop method has been extended to other processes [3], but remains limited by the "
        "accuracy of step-test results. Fine tuning must be done with the loop closed: with the "
        "deviation zero, place the controller in manual, step the output, and immediately transfer to "
        "automatic — this simulates a closed-loop load change. The resulting response should appear "
        "like the solid curve in Fig. 97.2, having a first peak that is symmetrical, followed by a "
        "slight overshoot and a well-damped cycle. If the overshoot is excessive, the I and/or D times "
        "should be increased; in the case of undershoot they should be decreased. (To simplify tuning "
        "of PID controllers, I and D can be moved together, keeping the I/D ratio at about 4 for "
        "noninteracting controllers and 3 for interacting controllers.) If damping is light, lower the "
        "proportional gain; if recovery is slow (producing an unsymmetrical first peak), raise the "
        "proportional gain. The set point should not be stepped for test purposes unless set-point "
        "response is important, as for flow controllers."))

    b.append(h3("Autotuning"))
    b.append(p(
        "Some autotuning controllers use a step test in the open loop, implementing Ziegler–Nichols "
        "rules. A single pulse produces more accurate identification, and a doublet pulse is better "
        "still [3]. A closed-loop method replaces proportional cycling with relay cycling, where the "
        "output switches between high and low limits as c crosses r [3]. The period of the resulting "
        "cycle is used to set I and D, and its amplitude relative to the distance between output limits "
        "to set K<sub>c</sub>. The principal limitation of the step and relay autotuning methods is that "
        "only two response features are used to identify a complex process. The estimated PID settings "
        "may not fit the specific process particularly well, resulting in instability in some loops and "
        "sluggishness in others. The autotuning function cannot monitor the effectiveness of its work, "
        "as self-tuning does."))

    b.append(h3("Self-Tuning"))
    b.append(p(
        "A self-tuning controller need not test the process, but simply observes its closed-loop "
        "response to set-point and load changes with its current PID settings. It then performs "
        "fine-tuning as described above to bring the overshoot, damping or symmetry of the response "
        "curve closer to optimum. This may require several iterations if the PID settings are far from "
        "optimum, but can eventually converge on optimum response, and readjust as necessary whenever "
        "process parameters change. Without a test disturbance, mischaracterization is possible, "
        "especially for a sinusoidal disturbance, where detuning may result when tightening would give "
        "better control."))

    b.append(h2("Defining Terms"))
    b.append(dt("Averaging level control",
                "allowing the liquid level in a tank to vary in an effort to minimize changes in its "
                "outflow."))
    b.append(dt("Closed-loop response",
                "the response of a controlled variable to changes in set point or load with the "
                "controller in the automatic mode."))
    b.append(dt("Derivative action",
                "the change in controller output responding to a rate of change in the controlled "
                "variable."))
    b.append(dt("Dynamic gain",
                "the ratio of the change in output from a function to a change in its input, which "
                "varies with time or with the frequency of the input."))
    b.append(dt("Integral action",
                "the rate of change of controller output responding to a deviation between the "
                "controlled variable and set point."))
    b.append(dt("Load", "a variable or aggregate of variables which affects the controlled variable."))
    b.append(dt("Manipulated variable",
                "a variable changed by the controller to move the controlled variable."))
    b.append(dt("Noise", "a disturbance having a frequency range too high for the controller to affect."))
    b.append(dt("Offset", "steady-state deviation between the controlled variable and set point."))
    b.append(dt("Open-loop response",
                "the response of a controlled variable to process inputs in the absence of control "
                "action."))
    b.append(dt("Proportional action",
                "the change in controller output responding directly to a change in the controlled "
                "variable."))
    b.append(dt("Proportional band",
                "the percentage change in the controlled variable required to drive the controller "
                "output full scale."))
    b.append(dt("Self-regulation",
                "the property of a process through which a change in the controlled variable affects "
                "either the flow into or out of a process in such a way as to reduce further changes in "
                "the controlled variable."))
    b.append(dt("Tuning", "adjusting the settings of a controller to affect its performance."))
    b.append(dt("Windup",
                "saturation of the integral mode of a controller which results in the controlled "
                "variable subsequently overshooting the set point."))

    b.append(h2("Translator's note"))
    b.append(note(
        "The source's table of contents prints “Self-Turning” for Section 97.5, while the section "
        "heading and the body text both read “Self-Tuning”; this translation follows the correct "
        "spelling. In Eq. 97.2 the original sets two stacked fractions; they are rendered here with "
        "bracketed slashes to match the layout convention of this translation, with no change to the "
        "mathematics."))

    b.append(h2("References"))
    b.append(refs([
        "J. G. Ziegler and N. B. Nichols, “Optimum settings for automatic controllers,” "
        "<i>Trans. ASME</i>, November 1942, 759–768.",
        "F. G. Shinskey, <i>Process Control Systems</i>, 4th ed., New York: McGraw-Hill, 1996, "
        "22–25, 25–28, 192–194, 388–390.",
        "F. G. Shinskey, <i>Feedback Controllers for the Process Industries</i>, New York: "
        "McGraw-Hill, 1994, 68–70, 176–178, 157–164, 148–151, 155–156.",
    ]))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 97 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 97 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 97 “Điều khiển PID” của F. Greg Shinskey — vòng hở và vòng "
            "kín, chọn chế độ P/I/PI/PD/PID, phần cứng khí nén, điện tử và số, cùng các phương pháp "
            "chỉnh định bằng tay, tự chỉnh định và tự chỉnh, với 4 hình và 7 phương trình." if vi
            else
            "Companion to Chapter 97 of the CRC Measurement Handbook — open and closed loops, "
            "P/I/PI/PD/PID mode selection, pneumatic, electronic and digital hardware, and manual, "
            "autotuning and self-tuning methods, with 4 figures and 7 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 97' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 97' % BASE_EN)
    meta = ("Chương 97 · theo Ch97.pdf (CRC Press, 1999) · 4 hình, 7 phương trình" if vi else
            "Chapter 97 · 4 figures, 7 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 97)))
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
