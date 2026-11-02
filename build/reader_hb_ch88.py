# -*- coding: utf-8 -*-
"""Handbook Chapter 88 — Sensor Networks and Communication.

Robert M. Crovella (NVIDIA Corporation)

Writes the full Vietnamese translation and the English companion.
Figures: hb88fig.py (88.1–88.5). Figure 88.4 is printed as a figure on the
page but its content is a table, so it is emitted as one and keeps the figure
number. Every value in it was re-read from the 200 dpi page raster — the page
has no text layer under the table, so the extract could not supply it.
Run:  python build/reader_hb_ch88.py
"""
import os

import hb88fig as F88
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch88-sensor-networks-and-communication"
TITLE_EN = "Sensor Networks and Communication"
TITLE_VI = "Mạng cảm biến và truyền thông"
BYLINE = "Robert M. Crovella"
BYLINE_EN = "Robert M. Crovella"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, lang="vi"):
    if num == 4:
        return F88.fig_88_4(lang)
    svg, cap_vi, cap_en, _av, _ae = getattr(F88, "fig_88_%d" % num)()
    return ('<figure class="figure" id="fig-88-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def note(t):
    return '<div class="note">%s</div>' % t


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def ul(items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)


def _glossary(items):
    o = ['<dl class="glossary">']
    for term, body in items:
        o.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    o.append("</dl>")
    return "".join(o)


def _sup(inner):
    """A superscript that is not <sup> — inline-styled span keeps the CSS cascade."""
    return ('<span style="font-size:.72em;vertical-align:.42em;line-height:0">%s</span>'
            % inner)


# ================================================================ NOTE
def _transnote(lang="vi"):
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch.</b> Chương này dịch từ bản in Ch88.pdf của CRC Press "
            "(1999). Bản trích văn bản lấy từ lớp văn bản của file PDF đã làm hỏng ký hiệu ở "
            "đúng một chỗ — công thức (88.1) hiện ra thành “T N =- () - 21 1”. Đối chiếu với "
            "trang in thì đó là <i>T</i> = 2<sup>(N−1)</sup> − 1, và bản dịch dùng đúng dạng in. "
            "Xin lưu ý rằng công thức in ra không trùng với số cạnh của một đồ thị đầy đủ "
            "<i>N</i>(<i>N</i>−1)/2: hai giá trị chỉ bằng nhau khi <i>N</i> = 2 và <i>N</i> = 3 "
            "(cùng bằng 2 và 3), còn từ <i>N</i> = 4 trở đi thì lệch nhau (7 so với 6; 15 so với "
            "10). Nguyên bản in công thức nào thì ở đây giữ nguyên công thức đó, không sửa. "
            "Hình 88.4 trên trang in mang số hiệu hình nhưng nội dung là một bảng so sánh, nên "
            "ở đây được trình bày bằng một bảng thật (vẫn giữ số hiệu hình) để đọc được trên "
            "màn hình hẹp. Mọi ô của bảng được đọc lại trực tiếp từ ảnh trang 200 dpi vì vùng "
            "bảng không có lớp văn bản. Chú thích dưới bảng in rằng “UP = unshielded pair”, "
            "trong khi cách viết thông dụng hiện nay là UTP; bản dịch giữ nguyên như bản in. "
            "Cuối cùng, chú thích “* Tối đa 400 m giữa hai trạm” đi kèm con số 25,6 km của "
            "Interbus-S: hai con số chỉ ăn khớp nếu hiểu 25,6 km là tổng chiều dài của nhiều "
            "đoạn nối tiếp, mỗi đoạn không quá 400 m. Thuật ngữ: <i>station</i> dịch là “trạm” "
            "(một nút mạng, không phải một địa điểm vật lý), <i>media</i> là “môi trường truyền”, "
            "<i>signaling</i> là “tín hiệu hoá”, <i>arbitration</i> là “trọng tài”, "
            "<i>code book</i> là “sổ mã”.")
    return note(
        "<b>Translator’s note.</b> Translated from the CRC Press print of Ch88.pdf (1999). The "
        "PDF’s text layer corrupts exactly one symbol: equation (88.1) extracts as “T N =- () - "
        "21 1”, which on the page is <i>T</i> = 2<sup>(N−1)</sup> − 1, and that is what is "
        "reproduced here. Note that the printed formula does not equal the edge count of a "
        "complete graph, <i>N</i>(<i>N</i>−1)/2: the two agree only at <i>N</i> = 2 and "
        "<i>N</i> = 3 (both giving 2 and 3) and diverge from <i>N</i> = 4 onward (7 against 6; "
        "15 against 10). The formula is left exactly as printed rather than corrected. Figure "
        "88.4 is numbered as a figure on the page but its content is a comparison table, so it "
        "is rendered here as a real table (keeping the figure number) so that it stays readable "
        "on a narrow screen; every cell was re-read from the 200 dpi page raster because the "
        "table area has no text layer. The note under the printed table says “UP = unshielded "
        "pair”, where current usage would write UTP; it is left as printed. Finally, the note "
        "“* Maximum 400 m between stations” accompanies Interbus-S’s 25.6 km: the two only "
        "reconcile if 25.6 km is the total length of many chained segments, none longer than "
        "400 m. Terminology: <i>station</i> is a network node, not a physical site; "
        "<i>media</i> is the transmission medium.")


# ================================================================ 88.1
def body_vi():
    b = []
    b.append(_transnote("vi"))

    b.append(h2("88.1 Giới thiệu", "Introduction"))

    b.append(h3("Mạng truyền thông là gì?", "What Is a Communication Network?"))
    b.append(p(
        "Một mạng truyền thông cung cấp một hệ thống để nhiều người dùng có thể chia sẻ một "
        "đường truyền (hay môi trường truyền) duy nhất nhằm trao đổi thông tin. Hệ thống điện "
        "thoại là một ví dụ về một hệ thống chứa đựng nhiều mạng truyền thông, và — như một ví "
        "dụ trừu tượng — có thể coi cả hệ thống ấy là một mạng truyền thông duy nhất. Mạng "
        "truyền thông được dùng phổ biến trong nhiều ngành và nhiều ứng dụng để đưa ra một "
        "phương tiện kinh tế cho phép nhiều người dùng ở cách xa nhau trao đổi thông tin."))

    b.append(h3("Cảm biến thường và cảm biến có mạng",
                "Ordinary Sensors vs. Networked Sensors"))
    b.append(p(
        "Định nghĩa chức năng của một cảm biến là ánh xạ hay chuyển đổi một đại lượng đo (ví dụ "
        "đại lượng không gian, cơ học, điện từ, v.v.) thành một đại lượng hay tín hiệu khác — "
        "thường là tín hiệu điện. Tín hiệu này sau đó có thể được đưa tới một hệ thống đo hay "
        "xử lý để thu thập và phân tích, hoặc làm đầu vào trực tiếp cho một quá trình được điều "
        "khiển nào đó. Trong trường hợp này, đại lượng đo được biểu diễn dưới dạng một tín hiệu "
        "điện. Hệ thống đo phải xử lý tín hiệu ấy một cách riêng lẻ, và tín hiệu cũng có thể bị "
        "làm hỏng bởi nhiều nguồn khác nhau, chẳng hạn nhiễu điện từ trong trường hợp tín hiệu "
        "điện."))
    b.append(p(
        "Trong những ứng dụng cần một số thiết bị cảm biến, và/hoặc những thiết bị cảm biến ấy "
        "phân tán về mặt địa lý (hoặc ở xa hệ thống đo và phân tích), người thiết kế ứng dụng có "
        "thể muốn dùng một mạng truyền thông để chuyển dữ liệu cảm biến từ điểm đo tới hệ thống "
        "đo và phân tích. Những ứng dụng như vậy thường bao gồm một loại máy tính số nào đó đặt "
        "tại điểm đo và phân tích, hoặc là một phần của hệ thống điều khiển. Hình 88.1 trình bày "
        "một sơ đồ khối tiêu biểu của một hệ cảm biến/mạng, cho thấy quan hệ giữa các thành phần "
        "khác nhau."))
    b.append(fig(1, "vi"))
    b.append(p(
        "Cảm biến có mạng có thể được tách thành hai thành phần: những thành phần thực hiện chức "
        "năng đo, và những thành phần thực hiện chức năng truyền thông. Trong một số trường hợp, "
        "hai chức năng này có thể được thiết kế thành một khối duy nhất, sao cho bản thân “cảm "
        "biến” đã bao hàm năng lực truyền thông. Trong những trường hợp khác, một cảm biến thông "
        "thường có thể được nối với một khối chuyển đổi, khối này chuyển tín hiệu ra của cảm "
        "biến thường thành một dạng thích hợp cho mạng, và quản lý việc đưa thông tin ấy lên "
        "mạng."))

    b.append(h3("Vì sao dùng cảm biến có mạng?", "Why Use Networked Sensors?"))
    b.append(p(
        "Truyền thông mạng kết hợp với công nghệ cảm biến có thể đem lại nhiều lợi ích cho một "
        "ứng dụng, cũng như cho người thiết kế cảm biến. Lợi ích rõ ràng nhất của một mạng là "
        "đơn giản hoá việc đi dây để truyền tín hiệu từ nơi này sang nơi khác. Với một hệ có "
        "<i>N</i> người dùng, số dây hay cáp <i>T</i> cần thiết để nối riêng rẽ từng người dùng "
        "với từng người dùng khác được cho bởi Công thức 88.1:"))
    b.append(eq("<i>T</i> = 2" + _sup("(<i>N</i>−1)") + " − 1", "88.1"))
    b.append(p(
        "với giả thiết mỗi dây hay cáp có thể mang thông tin theo cả hai chiều giữa hai người "
        "dùng được nối bởi dây cáp ấy. Với nhiều hơn một vài người dùng, số cáp <i>T</i> cần để "
        "có một kết nối riêng giữa từng cặp người dùng là lớn. Cảm biến thường được nối tới một "
        "hệ đo và phân tích trung tâm, và có thể chỉ cần trao đổi với hệ trung tâm ấy. Trong "
        "trường hợp này, số dây hay cáp riêng lẻ cần dùng bằng số cảm biến (<i>N</i> − 1). Ngay "
        "cả với số cáp nhỏ hơn ấy, việc đi dây cho một số lượng lớn cảm biến trong một số ứng "
        "dụng vẫn có thể rất phức tạp. Một mạng có thể giảm tổng số cáp cần thiết xuống một con "
        "số nhỏ hơn nhiều. Thực tế, trong một mạng cảm biến, toàn bộ cảm biến và hệ đo và phân "
        "tích trung tâm đều có thể được nối vào một sợi cáp duy nhất."))
    b.append(p(
        "Một lợi ích gián tiếp của việc dùng mạng có thể nằm ở cách nó xử lý tín hiệu cảm biến. "
        "Bởi vì phần lớn các mạng hiện đại mang tính số, tín hiệu tương tự của cảm biến thường "
        "phải được số hoá trước khi có thể truyền trên mạng. Với một cảm biến có mạng, việc số "
        "hoá thường được thực hiện bởi mạch điện nằm tương đối gần cảm biến. Kết quả là tín hiệu "
        "tương tự chỉ đi một quãng đường ngắn trước khi được chuyển thành tín hiệu số. Điều này "
        "có lợi theo hai cách. Thứ nhất, tín hiệu tương tự sẽ không bị suy giảm hay xuống cấp "
        "nhiều do tổn hao điện gắn với việc mang tín hiệu đi một quãng đường dài. Thứ hai, khi "
        "đã ở dạng số, “tín hiệu” có thể được làm cho tương đối miễn nhiễm với các tác động của "
        "méo dạng hay xuống cấp do nhiễu điện từ (EMI). Mặc dù truyền số vẫn chịu tác động của "
        "EMI, các giao thức và hệ truyền hiện đại có thể được thiết kế rất vững vàng, nhờ dùng "
        "kiểu tín hiệu hoá chống được EMI cũng như dùng các kỹ thuật điều khiển lỗi. Kết quả là "
        "tác động của suy giảm và nhiễu loạn về cơ bản có thể bị loại bỏ nhờ truyền số tín hiệu."))
    b.append(p(
        "Một lợi ích nữa của việc dùng mạng là khả năng truyền đạt một phạm vi thông tin rộng "
        "hơn nhiều — theo cả hai chiều — so với một sợi cáp đơn mang một tín hiệu cảm biến. Với "
        "nhiều mạng hiện đại thích hợp cho các ứng dụng cảm biến có mạng, một bộ vi xử lý được "
        "dùng tại cảm biến để quản lý việc xử lý tín hiệu cảm biến và việc truyền nó lên mạng. "
        "Nhưng nói chung không có lý do gì để giới hạn bộ vi xử lý ấy vào đúng một chức năng "
        "này. Sự kết hợp giữa mạng và bộ vi xử lý tạo ra một nền tảng mà trên đó nhiều chức "
        "năng và tính năng bổ sung có thể được đưa vào cảm biến có mạng. Ví dụ, tín hiệu của "
        "một cảm biến có thể cần được áp một hàm hiệu chuẩn hay hiệu chỉnh nào đó trước khi dùng "
        "được trong các phép tính. Có thể có lợi nếu nạp vào cảm biến có mạng (qua chính mạng) "
        "một bộ tham số hay hệ số hiệu chỉnh, rồi để bộ vi xử lý hiệu chỉnh hay hiệu chuẩn đầu "
        "ra của cảm biến trước khi truyền nó lên mạng. Cảm biến có thể dễ dàng được thiết kế để "
        "có nhiều chức năng cảm biến, chẳng hạn nhiệt độ và áp suất. Mỗi tín hiệu có thể được xử "
        "lý riêng và truyền riêng trên mạng, không cần thêm kết nối nào. Cảm biến có thể được "
        "thiết kế để lưu một số loại thông tin nhất định, chẳng hạn tên nhà sản xuất, hoặc một "
        "số tham số hiệu chuẩn do nhà sản xuất xác định tại thời điểm chế tạo. Thông tin này sau "
        "đó có thể được đọc ra qua mạng và dùng cho nhiều mục đích khác nhau. Một cảm biến thậm "
        "chí có thể được thiết kế để có những chức năng “thông minh”, chẳng hạn khả năng tự cảm "
        "nhận môi trường của mình và xác định khi nào một số tham số đã bị vượt (ví dụ dải nhiệt "
        "độ làm việc), hoặc phát một thông điệp đặc biệt chứa “cảnh báo” khi mức tín hiệu cảm "
        "biến vượt một ngưỡng nào đó. Sự kết hợp giữa mạng và bộ vi xử lý dẫn tới vô số chức "
        "năng và tính năng có thể được thêm vào công nghệ cảm biến cơ bản."))

    b.append(h3("Những vấn đề tiềm ẩn của cảm biến có mạng",
                "Potential Problems with Networked Sensors"))
    b.append(p(
        "Cảm biến có mạng nói chung sẽ đòi hỏi mạch điện phức tạp hơn so với cảm biến tương "
        "đương không nối mạng. Một nhược điểm của việc chuyển đổi tương tự–số (A/D) và truyền số "
        "tín hiệu là hiệu ứng lượng tử hoá theo thời gian và theo mức mà việc chuyển đổi A/D có "
        "thể gây ra trên tín hiệu tương tự. Những hiệu ứng này có thể được giảm nhẹ nhờ các bộ "
        "chuyển đổi A/D tốc độ cao hiện đại (để giảm thiểu hiệu ứng lượng tử hoá thời gian, tức "
        "hiệu ứng lấy mẫu) với khả năng chuyển đổi ở độ phân giải cao (nghĩa là dùng nhiều bit "
        "số để biểu diễn mức tín hiệu tương tự). Những nhược điểm này không phải riêng của cảm "
        "biến có mạng, mà là của các giá trị cảm biến đã được số hoá và của điều khiển số, dù có "
        "dùng mạng hay không. Cuối cùng, khả năng mang thông tin của mạng (băng thông) phải được "
        "xét đến trong bất kỳ hệ truyền thông nào. Đặt một số lượng lớn cảm biến lên một mạng "
        "duy nhất có thể làm quá tải khả năng mang thông tin của mạng, gây ra trễ do xếp hàng "
        "khi nhận tín hiệu cảm biến và, trong một số trường hợp, mất dữ liệu."))

    # ------------------------------------------------------------ 88.2
    b.append(h2("88.2 Các khái niệm truyền thông và mạng",
                "Communication and Networking Concepts"))
    b.append(p(
        "Để có thể chọn được một công nghệ mạng thích hợp, cần hiểu một số thuật ngữ cơ bản để "
        "các tính năng và năng lực của nhiều loại mạng và công nghệ khác nhau có thể được phân "
        "loại và so sánh."))

    b.append(h3("Trạm", "Station"))
    b.append(p(
        "Một trạm biểu thị một phần tử truyền thông đơn lẻ trên một hệ mạng. Mỗi người dùng của "
        "mạng phải truy nhập năng lực truyền thông của mạng thông qua một trạm. Mỗi trạm thường "
        "có một cách hiện thực nào đó của mô hình tham chiếu mạng liên kết các hệ mở (OSI) để "
        "làm phương tiện sử dụng hệ mạng."))

    b.append(h3("Truy nhập môi trường", "Media Access"))
    b.append(p(
        "Truy nhập môi trường là cách thức mà từng trạm xác định khi nào nó được phép phát, hay "
        "“dùng” môi trường truyền. Điều khiển truy nhập môi trường (MAC) là một chức năng "
        "thường được thực hiện ở tầng liên kết dữ liệu của mô hình tham chiếu OSI. Một số "
        "phương pháp điều khiển truy nhập môi trường nổi tiếng gồm đa truy nhập có cảm nhận sóng "
        "mang và phát hiện xung đột (CSMA/CD) và chuyển thẻ bài. Các hệ CSMA/CD (như Ethernet) "
        "cho phép mọi trạm trên mạng truy nhập bình đẳng. Mỗi trạm phải “nghe” mạng để xác định "
        "những khoảng không hoạt động trước khi phát. Bất kỳ trạm nào muốn dùng mạng đều có thể "
        "bắt đầu phát miễn là mạng đang không hoạt động vào lúc nó kiểm tra. Nếu nhiều trạm cùng "
        "cố phát đồng thời, một xung đột xảy ra. Xung đột được mọi trạm đang phát phát hiện, và "
        "tất cả đều phải ngay lập tức ngừng phát, mỗi trạm chờ một khoảng thời gian được chọn "
        "ngẫu nhiên trước khi lại cố dùng mạng. Ví dụ, mạng vùng điều khiển (CAN) dùng một biến "
        "thể của CSMA/CD để truy nhập môi trường. Các hệ chuyển thẻ bài có một “thẻ bài” lôgic "
        "được trao đổi giữa các trạm qua các thông điệp mạng. Trạm đang giữ thẻ bài có quyền "
        "phát. Mọi trạm khác chỉ được phép nhận thông điệp. Những trạm muốn phát mà không có thẻ "
        "bài phải chờ cho tới khi trạm đang giữ thẻ bài chuyển nó đi. Một phương pháp điều khiển "
        "truy nhập môi trường thường dùng khác là chủ–tớ. Theo phương pháp này, một trạm trên "
        "mạng (được chỉ định là chủ) nói chung phụ trách và khởi phát mọi liên lạc. Các tớ chỉ "
        "đáp lại chủ, và chỉ đáp lại khi chủ khởi phát liên lạc với chúng bằng cách gửi một "
        "thông điệp tới tớ. Profibus-FMS (xem dưới đây) là một ví dụ về giao thức dùng cả "
        "chuyển thẻ bài (trong một số trường hợp) và chủ–tớ (trong một số trường hợp khác) để "
        "điều khiển truy nhập môi trường."))

    b.append(h3("Băng thông", "Bandwidth"))
    b.append(p(
        "Băng thông có thể có nhiều định nghĩa khác nhau. Với các hệ truyền thông số, băng "
        "thông mô tả năng lực của hệ trong việc vận chuyển dữ liệu số từ nơi này sang nơi khác. "
        "Thuật ngữ này có thể được áp cho năng lực thô của tầng vật lý và tầng liên kết dữ liệu "
        "trong việc vận chuyển dữ liệu thông điệp (băng thông thô, gắn chặt với khái niệm tốc độ "
        "bit), hoặc có thể được áp cho tốc độ hiệu dụng mà ở đó thông tin có ý nghĩa với người "
        "dùng được vận chuyển (băng thông hiệu dụng). Băng thông của một hệ cho trước nói chung "
        "tỉ lệ nghịch với khoảng cách nút-tới-nút trong trường hợp xấu nhất. Phạm vi mạng càng "
        "nhỏ thì băng thông của nó càng có thể cao."))

    b.append(h3("Định địa chỉ", "Addressing"))
    b.append(p(
        "Định địa chỉ là một khái niệm gán những định danh nói chung là duy nhất cho mỗi trạm "
        "trong một hệ mạng. Định danh này (địa chỉ) sau đó có thể được mạng dùng cho nhiều mục "
        "đích, gồm việc xác định nguồn và/hoặc đích của thông điệp, hoặc trọng tài truy nhập "
        "một môi trường truyền thông được chia sẻ. Một khái niệm định địa chỉ hay định danh khác "
        "gán những định danh duy nhất không phải cho các trạm mà cho những mẩu dữ liệu hay tín "
        "hiệu riêng biệt sẽ được mạng mang đi. Các trạm sau đó dùng một định danh tuỳ theo loại "
        "dữ liệu mà chúng sẽ truyền. Nhiều — nhưng không phải tất cả — phương pháp mạng đòi hỏi "
        "phải thiết lập một địa chỉ tường minh cho mỗi trạm mạng."))

    b.append(h3("Trọng tài", "Arbitration"))
    b.append(p(
        "Trọng tài là một chức năng gắn chặt với MAC. Một số mạng dùng trọng tài để định nghĩa "
        "thủ tục được tuân theo khi nhiều trạm cùng muốn dùng mạng một lúc."))

    b.append(h3("Tín hiệu hoá", "Signaling"))
    b.append(p(
        "Tín hiệu hoá nói tới cách biểu diễn vật lý thực tế (ví dụ điện, quang hay cách khác) "
        "của dữ liệu khi nó được mang trên môi trường truyền. Ví dụ, trong một số mạng, các phần "
        "tử dữ liệu có thể được biểu diễn bằng những mức điện áp hay dạng sóng nhất định trên "
        "môi trường truyền. Trong các mạng khác, các phần tử dữ liệu có thể được biểu diễn bằng "
        "sự có mặt của những bước sóng ánh sáng nhất định trong môi trường truyền. Việc gán mọi "
        "phần tử dữ liệu có thể biểu diễn được (ví dụ 0/1 hay đóng/ngắt) với những cách biểu "
        "diễn tín hiệu tương ứng trong môi trường truyền chính là sơ đồ hay phương pháp tín hiệu "
        "hoá. Một phương pháp tín hiệu hoá quan trọng khi dùng dây điện làm môi trường truyền là "
        "tín hiệu hoá vi sai. Tín hiệu hoá vi sai biểu diễn một phần tử dữ liệu cụ thể (1 hoặc "
        "0) bằng hai trạng thái khác nhau trên một cặp dây. Việc xác định phần tử dữ liệu đòi "
        "hỏi đo hiệu điện áp giữa hai dây, chứ không phải mức điện áp tuyệt đối trên một trong "
        "hai dây. Các phần tử dữ liệu khác nhau sau đó được biểu diễn bằng hiệu điện áp (có dấu) "
        "giữa hai dây. Ví dụ, RS-485 biểu diễn phần tử dữ liệu số 1 bằng mức tín hiệu 5 V trên "
        "dây thứ nhất và mức 0 V trên dây thứ hai, còn số 0 bằng mức 0 V trên dây thứ nhất và "
        "mức 5 V trên dây thứ hai. Một trong những lợi ích chính của tín hiệu hoá vi sai là có "
        "thể xác định dữ liệu đang được truyền mà không cần biết điện thế mốc đất của bên phát. "
        "Điều này cho phép bên phát và bên thu làm việc tin cậy ngay cả khi chúng có điện thế "
        "đất khác nhau (trong giới hạn cho phép) — một chuyện thường gặp trong các hệ truyền "
        "thông."))

    b.append(h3("Mã hoá", "Encoding"))
    b.append(p(
        "Mã hoá nói tới quá trình chuyển thông tin có ý nghĩa với người dùng thành các phần tử "
        "dữ liệu hay nhóm phần tử dữ liệu để hệ mạng vận chuyển. Sổ mã nói tới tập hợp mọi quan "
        "hệ giữa thông tin có ý nghĩa với người dùng và dữ liệu được mạng mang đi. Mã hoá có thể "
        "xảy ra ở nhiều mức trong mô hình tham chiếu OSI, khi thông tin có ý nghĩa với người "
        "dùng được biến đổi dần cho tới khi trở thành một thông điệp mạng thực sự, do tầng liên "
        "kết dữ liệu tạo ra. Giải mã là quá trình ngược lại, theo đó một thông điệp mạng được "
        "chuyển dịch dần trở lại thành thông tin có ý nghĩa với người dùng."))

    b.append(h3("Điều chế", "Modulation"))
    b.append(p(
        "Điều chế theo nghĩa cổ điển nói tới một kỹ thuật tín hiệu hoá trong đó dữ liệu hay "
        "thông tin được dùng để điều khiển một tổ hợp nào đó của tần số, pha và/hoặc biên độ của "
        "một tín hiệu mang. Tín hiệu mang đưa thông tin tới một bộ thu ở xa, nơi nó sẽ được giải "
        "điều chế để lấy lại thông tin. Các hệ mạng có điều chế nằm ngoài phạm vi của chương "
        "này."))

    b.append(h3("Thông điệp", "Message"))
    b.append(p(
        "Thông điệp là đơn vị thông tin cơ bản, không chia nhỏ được, được trao đổi giữa các "
        "trạm. Thông tin có ý nghĩa với người dùng sẽ được mô hình tham chiếu mạng OSI nhóm "
        "thành một hay nhiều thông điệp."))

    b.append(h3("Ghép kênh", "Multiplexing"))
    b.append(p(
        "Ghép kênh nói tới khả năng dùng môi trường truyền trong một mạng để mang nhiều thông "
        "điệp hay nhiều dòng thông tin “đồng thời”. Các hệ ghép kênh cho phép nhiều kênh truyền "
        "thông cùng dùng một sợi dây hay một môi trường truyền vật lý. Mỗi thông điệp hay dòng "
        "thông tin có thể có nguồn và đích khác nhau."))
    b.append(p(
        "Ghép kênh có thể được thực hiện bằng nhiều cách. Ghép kênh phân chia theo thời gian "
        "(TDM) bao gồm việc chia quyền truy nhập môi trường truyền thành một chuỗi các lượng tử "
        "thời gian. Trong mỗi lượng tử thời gian, môi trường truyền mang một thông điệp hay dòng "
        "thông tin riêng. Cách sắp xếp sát nhau của các lượng tử thời gian khiến môi trường mạng "
        "có thể mang nhiều thông điệp “đồng thời”. Ghép kênh phân chia theo mã (CDM) bao gồm "
        "việc tách sổ mã (xem mục Mã hoá) thành các phần. Mỗi phần của sổ mã cung cấp toàn bộ "
        "những thông điệp sẽ được dùng cho một dòng thông tin cụ thể. Do đó, một dòng thông tin "
        "cụ thể trong môi trường mạng được phân biệt bằng toàn bộ những thông điệp thuộc phần sổ "
        "mã của dòng ấy. Ghép kênh phân chia theo tần số (FDM) chia băng thông sẵn có của một "
        "kênh truyền thông thành nhiều dải tần số và gán một dòng thông tin cho mỗi dải tần số."))

    b.append(h3("Giao thức", "Protocols"))
    b.append(p(
        "Giao thức là một phương pháp trao đổi thông tin đã được định nghĩa. Các giao thức "
        "thường được định nghĩa ở nhiều mức trong mô hình tham chiếu mạng OSI, chẳng hạn ở tầng "
        "ứng dụng và ở tầng liên kết dữ liệu. Giao thức được dùng để định nghĩa cách thức các "
        "dịch vụ do một tầng cụ thể cung cấp sẽ được sử dụng, và cách thức các kết quả của những "
        "dịch vụ ấy sẽ được diễn giải."))

    b.append(h3("Dịch vụ", "Service"))
    b.append(p(
        "Một dịch vụ biểu thị một chức năng hay thao tác cụ thể được một tầng cụ thể trong mô "
        "hình tham chiếu mạng OSI hỗ trợ. Ví dụ, một dịch vụ ở tầng ứng dụng có thể được cung "
        "cấp cho việc đọc hay ghi một phần tử dữ liệu chứa trong một thiết bị (hay trạm) khác "
        "trên mạng. Dịch vụ này có thể dùng một dịch vụ ở tầng liên kết dữ liệu, dịch vụ này có "
        "thể được cung cấp để hỗ trợ việc trao đổi một thông điệp với một thiết bị (hay trạm) "
        "khác trên mạng."))

    b.append(h3("Tô-pô", "Topology"))
    b.append(p(
        "Tô-pô nói tới cách bố trí hay sắp xếp vật lý hoặc địa lý của một mạng. Một số kiểu "
        "tô-pô kinh điển thường được bàn tới trong ngữ cảnh mạng, chẳng hạn đường trục/nhánh, "
        "hình sao (hay hình trục), vòng, và chuỗi nối tiếp."))

    b.append(h3("Tốc độ bit", "Bit Rate"))
    b.append(p(
        "Tốc độ bit nói tới tốc độ mà các mẩu thông tin nhị phân (bit) được truyền trên một "
        "mạng cụ thể. Tốc độ bit thô của một mạng nói chung chỉ tốc độ thực tế của việc truyền "
        "bit trên mạng. Tốc độ bit hiệu dụng — hay thông lượng — nói chung chỉ tốc độ mà thông "
        "tin người dùng được truyền. Con số này nhỏ hơn hoặc bằng tốc độ bit thô, tuỳ thuộc vào "
        "tỉ lệ phần trăm số bit được truyền dùng để mang thông tin người dùng. Những bit không "
        "mang thông tin người dùng là phần phụ trội, dùng để mang thông tin giao thức, thông tin "
        "định thời hay thông tin mạng khác."))

    b.append(h3("Song công (bán song công và toàn song công)",
                "Duplex (Half and Full Duplex)"))
    b.append(p(
        "Bán song công nói tới một hệ truyền thông trong đó một trạm có thể hoặc phát thông tin "
        "hoặc nhận thông tin, nhưng không thể làm cả hai cùng lúc. Một mạng toàn song công cho "
        "phép một trạm phát và nhận thông tin đồng thời."))

    b.append(h3("Điều khiển lỗi", "Error Control"))
    b.append(p(
        "Nhiều hệ mạng cung cấp các cơ chế điều khiển lỗi. Điều khiển lỗi có bốn khía cạnh: "
        "phòng ngừa, phát hiện, sửa và cô lập. Phòng ngừa lỗi có thể chỉ đơn giản là che chắn "
        "cho môi trường truyền để giảm thiểu nhiễu loạn điện từ, hoặc có thể phức tạp hơn, chẳng "
        "hạn điều khiển việc lấy mẫu tín hiệu để tối ưu xác suất tín hiệu ở đúng trạng thái khi "
        "được lấy mẫu. Phát hiện lỗi nói chung dựa vào việc phát hiện những vi phạm quy tắc giao "
        "thức ở các mức mạng khác nhau, hoặc những vi phạm của dữ liệu tính toán được thêm vào "
        "một thông điệp cho mục đích điều khiển lỗi. Một số ví dụ về kỹ thuật phát hiện lỗi là "
        "bit chẵn lẻ và kiểm tra dư vòng (CRC). Cả hai phương pháp đều bao gồm việc tính thêm "
        "những bit thông tin dựa trên dữ liệu chứa trong một thông điệp, rồi gắn những bit ấy "
        "vào thông điệp. Ví dụ, một giao thức cụ thể có thể yêu cầu tầng liên kết dữ liệu tính "
        "và gắn một CRC vào thông điệp trước khi phát. Bên nhận thông điệp sau đó cũng có thể "
        "tính CRC và so sánh với CRC đã được gắn vào thông điệp. Nếu có sự khác biệt, thì coi "
        "như đã xảy ra lỗi."))
    b.append(p(
        "Sửa lỗi có thể có nhiều hình thức. Một trong những phương pháp sửa lỗi đơn giản nhất là "
        "yêu cầu tầng liên kết dữ liệu của bên phát phát lại một thông điệp đã bị phát hiện có "
        "lỗi trong khi truyền. Phương pháp này dựa trên giả thiết rằng lỗi do một nhiễu loạn gây "
        "ra và nhiễu loạn ấy khó có thể lặp lại. Một phương pháp sửa lỗi khác bao gồm việc truyền "
        "thêm những bit thông tin bổ sung cùng với thông tin người dùng trong một thông điệp. "
        "Những bit thông tin bổ sung này được bên phát tính toán để cung cấp thông tin dư trong "
        "thông điệp. Khi số lỗi mức bit xảy ra trong khi truyền thông điệp ít hơn một số lượng "
        "nhất định, bên nhận có thể tái tạo chính xác thông tin người dùng ban đầu nhờ thông tin "
        "(bit) dư được cung cấp trong thông điệp. Cô lập lỗi là năng lực của một số mạng trong "
        "việc định vị nguồn lỗi và tách riêng những phần của mạng hoặc những trạm mà ở đó lỗi "
        "đã được định vị. Cô lập lỗi cho phép những phần không có sự cố của mạng tiếp tục liên "
        "lạc ngay cả khi những phần khác của mạng đã xuống cấp tới mức sinh ra lỗi."))

    b.append(h3("Liên mạng", "Internetworking"))
    b.append(p(
        "Có những trường hợp việc liên lạc giữa hai hay nhiều điểm được xử lý tốt nhất bằng "
        "nhiều mạng. Đó có thể là khi một mạng đơn lẻ có những hạn chế khiến nó không thể nối "
        "các điểm ấy lại (ví dụ giới hạn về khoảng cách), hoặc khi cần nhiều mạng vì những lý do "
        "khác (ví dụ để mang những loại dữ liệu khác nhau). Khi nhiều mạng được dùng để cung cấp "
        "liên lạc, có thể nảy sinh nhu cầu chuyển thông điệp hay thông tin trực tiếp từ mạng này "
        "sang mạng kia."))
    b.append(p(
        "Một bộ lặp có thể được dùng khi các mạng cần nối là đồng nhất về mặt lôgic, và mục "
        "đích chỉ là kéo dài chiều dài của mạng hoặc mở rộng năng lực của nó theo cách nào đó. "
        "Bộ lặp nói chung không tác động gì tới thông điệp, mà chỉ đơn giản chuyển mọi thông "
        "điệp từ cáp hay cổng này sang cáp hay cổng khác (tức là một sự thay đổi môi trường "
        "truyền vật lý). Bộ lặp cho phép nối các mạng ở mức tầng vật lý."))
    b.append(p(
        "Một cầu nối tương tự bộ lặp, nhưng cho phép nối các mạng ở mức tầng liên kết dữ liệu. "
        "Nói chung, cầu nối sẽ chuyển mọi thông điệp từ mạng này sang mạng kia bằng cách chuyển "
        "thông điệp ở mức tầng liên kết dữ liệu."))
    b.append(p(
        "Một bộ định tuyến thường có chức năng phân vùng những mạng tương tự nhau. Hai mạng có "
        "thể dựa trên cùng một công nghệ và giao thức, nhưng không đồng nhất về mặt lôgic. Trong "
        "những trường hợp này, một số — nhưng không phải tất cả — thông điệp trên mạng này có "
        "thể cần được mang hay vận chuyển sang mạng kia. Bộ định tuyến có chức năng xác định "
        "những thông điệp nào sẽ được chuyển qua lại dựa trên những quy tắc nhất định. Những "
        "chức năng cho phép định tuyến thông điệp tự động và hiệu quả có thể được đưa vào tầng "
        "3 (tầng mạng) của mô hình tham chiếu mạng OSI, và bộ định tuyến cho phép nối các mạng ở "
        "mức tầng mạng."))
    b.append(p(
        "Một cổng nối có thể có chức năng tương tự bộ định tuyến, hoặc có thể có chức năng nối "
        "những mạng không đồng dạng, nghĩa là những mạng dựa trên công nghệ và/hoặc giao thức "
        "không đồng dạng. Khi hoạt động như một bộ định tuyến, cổng nối thường thực hiện việc "
        "phân biệt của mình ở một mức giao thức cao hơn so với bộ định tuyến. Khi cổng nối nối "
        "những mạng không đồng dạng, nói chung phải thiết kế một bộ quy tắc phức tạp hơn vào "
        "cổng nối để việc chuyển dịch, ánh xạ và định tuyến thông điệp có thể diễn ra bên trong "
        "cổng nối khi nó xác định những thông điệp nào sẽ được chuyển từ mạng này sang mạng kia."))

    b.append(h3("Mô hình tham chiếu mạng ISO/OSI",
                "ISO/OSI Network Reference Model"))
    b.append(p(
        "Sự bùng nổ trong việc sử dụng và trong các loại mạng truyền thông trong vài thập kỷ "
        "qua đã dẫn tới những cách mô tả và xử lý chính xác hơn đối với mạng truyền thông nói "
        "chung. Tổ chức Tiêu chuẩn hoá Quốc tế (ISO) đã công nhận một phương pháp mô tả chính "
        "xác như vậy đối với mạng, gọi là mô hình tham chiếu OSI [1]. Như trình bày trên Hình "
        "88.2, mô hình này phân rã một mạng truyền thông tuỳ ý thành một “chồng” bảy “tầng”. Ở "
        "mỗi tầng, những loại chức năng truyền thông mạng nhất định được mô tả. Người dùng của "
        "hệ truyền thông — thường là một hệ khác cần liên lạc trên mạng — tương tác với tầng 7, "
        "tầng cao nhất. Môi trường truyền thực tế (ví dụ cáp đồng, sợi quang, không gian tự do, "
        "v.v.) được nối với tầng 1, tầng thấp nhất. Phần lớn các mạng truyền thông không hiện "
        "thực đủ mọi tầng trong mô hình tham chiếu. Trong trường hợp này, việc định nghĩa, xử lý "
        "hay đưa một cách hình thức một số tầng của mô hình vào thiết kế mạng thực tế bị bỏ qua. "
        "Các tầng 1, 2 và 7 thường có mặt trong mọi mạng, nhưng những tầng khác chỉ có thể được "
        "đưa vào một cách tường minh hoặc nhận diện được khi chức năng của chúng là một phần "
        "quan trọng của truyền thông mạng. Trong nhiều mạng truyền thông cảm biến, những chức "
        "năng do các tầng 3, 4, 5 và 6 thực hiện bị “thu gọn” thành những phần thêm vào chỉ còn "
        "dấu vết của các chức năng ở tầng 7, tức tầng ứng dụng."))
    b.append(fig(2, "vi"))

    b.append(h3("Tầng vật lý", "Physical Layer"))
    b.append(p(
        "Tầng vật lý là tầng thấp nhất của mô hình. Tầng này chịu trách nhiệm chuyển đổi giữa "
        "cách biểu diễn ký hiệu hay dữ liệu của các thông điệp mạng và cách biểu diễn vật lý "
        "thực tế của dữ liệu trong môi trường mạng. Tầng này quy định hành vi của các mạch điện "
        "được gọi là bên phát và bên thu. Nó cũng định nghĩa các cấu trúc vật lý cho đầu nối."))

    b.append(h3("Tầng liên kết dữ liệu", "Data Link Layer"))
    b.append(p(
        "Tầng liên kết dữ liệu, hay tầng 2, chịu trách nhiệm nhiều chức năng. Tầng này quản lý "
        "việc truy nhập môi trường mạng (MAC), cấu trúc các bit thông tin thành những nhóm được "
        "định nghĩa rõ ràng, nhận diện là “khung” hay thông điệp, xử lý việc nhận diện trạm "
        "nguồn và trạm đích trên mạng, và cung cấp việc truyền không lỗi một thông điệp từ trạm "
        "nguồn tới trạm đích, tất cả theo giao thức của tầng liên kết dữ liệu. Có một số giao "
        "thức tầng liên kết dữ liệu tiêu chuẩn, làm cơ sở cho nhiều mạng truyền thông đang được "
        "dùng rộng rãi. Ví dụ, Ethernet, hay IEEE 802.3, quy định một tầng con MAC làm việc với "
        "tầng Điều khiển liên kết lôgic IEEE 802.2 để tạo thành giao thức tầng liên kết dữ liệu "
        "được dùng trong phần lớn các mạng thông tin văn phòng [2]."))

    b.append(h3("Tầng mạng", "Network Layer"))
    b.append(p(
        "Tầng mạng bao gồm những chức năng liên quan tới việc định tuyến thông điệp, cả trong "
        "một mạng đơn lẻ lẫn giữa nhiều mạng. Tầng này thường dùng việc định địa chỉ dưới nhiều "
        "hình thức như một phần then chốt của các chức năng chỉ đường và định tuyến thông điệp, "
        "cũng như việc tìm kiếm và sử dụng những đường truyền sẵn có."))

    b.append(h3("Tầng giao vận", "Transport Layer"))
    b.append(p(
        "Tầng giao vận cung cấp những chức năng truyền dữ liệu bổ sung mà tầng liên kết dữ liệu "
        "không cung cấp trực tiếp, nhằm bảo đảm việc nhắn tin tin cậy từ đầu tới cuối. Ví dụ, "
        "một số chức năng truyền dữ liệu giữa các trạm có thể cần dùng nhiều thông điệp của tầng "
        "liên kết dữ liệu để hoàn thành một lần truyền thông điệp tin cậy. Việc sinh ra nhiều "
        "thông điệp và việc tháo rời, chuyển giao rồi lắp ghép dữ liệu theo trình tự được tầng "
        "giao vận thực hiện. Tầng giao vận cũng khắc phục những thông điệp bị mất, bị nhân đôi "
        "và bị sai thứ tự."))

    b.append(h3("Tầng phiên", "Session Layer"))
    b.append(p(
        "Tầng phiên cung cấp mức điều khiển và quản lý việc sử dụng mạng và dòng dữ liệu cao hơn "
        "so với những gì các tầng thấp hơn cung cấp, bao gồm việc mở hay thiết lập một kênh "
        "truyền thông, duy trì kênh ấy, và đóng kênh ấy. Tầng này ít khi được hiện thực trong các "
        "hệ đương đại."))

    b.append(h3("Tầng trình diễn", "Presentation Layer"))
    b.append(p(
        "Tầng trình diễn cung cấp những chức năng biến đổi dữ liệu từ các dạng có thể được mạng "
        "vận chuyển sang các dạng mà người dùng truy nhập được, được định nghĩa ở tầng ứng dụng "
        "và được hiểu trong trạm cục bộ."))

    b.append(h3("Tầng ứng dụng", "Application Layer"))
    b.append(p(
        "Tầng ứng dụng, hay tầng 7, cung cấp các dịch vụ truyền thông trực tiếp cho ứng dụng của "
        "người dùng. Việc sử dụng và định dạng những dịch vụ này được tóm tắt trong giao thức "
        "của tầng ứng dụng. Người dùng tương tác với mạng bằng cách gọi những hàm và dịch vụ do "
        "tầng ứng dụng cung cấp, và chuyển dữ liệu tới và từ mạng thông qua những dịch vụ ấy."))

    # ------------------------------------------------------------ 88.3
    b.append(h2("88.3 Các công nghệ mạng", "Network Technologies"))
    b.append(p(
        "Có một phạm vi rộng các công nghệ ở nhiều giai đoạn phát triển và tiêu chuẩn hoá khác "
        "nhau, đề cập tới hầu như mọi mức hay mọi tầng của mô hình tham chiếu mạng ISO/OSI. Một "
        "hay nhiều công nghệ sẵn có có lẽ sẽ phù hợp với hầu như mọi nhu cầu về mạng. Việc phân "
        "tích các công nghệ sẵn có và những hạn chế của chúng cũng sẽ có ích nếu thấy rằng phải "
        "tự thiết kế một phương pháp mạng để đáp ứng một ứng dụng cụ thể. Việc chọn lựa và mô tả "
        "các công nghệ ở đây hoàn toàn không đầy đủ hay trọn vẹn. Những công nghệ được trình bày "
        "được chọn từ một số ngành thường dùng mạng để truyền dữ liệu cảm biến. Hình 88.4 đưa ra "
        "một so sánh các tham số chọn lọc của một tập hợp mạng."))

    b.append(h3("RS-232", "RS-232"))
    b.append(p(
        "RS-232 (ANSI/EIA/TIA-232-E-91) là một phương pháp truyền thông được dùng rộng rãi, đã "
        "được tiêu chuẩn hoá ở nhiều nơi, trong đó có Hiệp hội Công nghiệp Điện tử [3]. RS-232 "
        "biểu diễn các yếu tố của tầng 1 của mô hình OSI, dùng để liên lạc giữa hai trạm (và chỉ "
        "hai mà thôi). RS-232 cung cấp một dây riêng cho việc truyền dữ liệu theo mỗi chiều giữa "
        "hai trạm, và gán cho hai trạm những tên gọi khác nhau — thiết bị đầu cuối dữ liệu (DTE) "
        "và thiết bị truyền thông dữ liệu (DCE) — để có một cách phân biệt trạm nào sẽ dùng dây "
        "nào để phát và nhận. Các mức tín hiệu của RS-232 biểu diễn bit số 1 bằng một điện áp "
        "trong khoảng 5 đến 12 V trên dây, và bit số 0 bằng một điện áp từ âm 5 đến âm 12 V trên "
        "dây. RS-232 thường được hiện thực theo kiểu toàn song công, vì mỗi trạm có thể phát cho "
        "trạm kia đồng thời bằng những dây riêng. RS-232 có thể được làm cho làm việc ở nhiều "
        "tốc độ bit khác nhau, nhưng thường được dùng ở các tốc độ từ 300 bit/s tới 115.200 "
        "bit/s."))

    b.append(h3("RS-485", "RS-485"))
    b.append(p(
        "EIA RS-485 trở thành tiêu chuẩn năm 1983, có nguồn gốc từ tiêu chuẩn RS-422. RS-485 "
        "cung cấp việc truyền dữ liệu vi sai trên một cặp dây giữa 32 trạm trở lên. Giống như "
        "RS-232, tiêu chuẩn này là một đặc tả của tầng 1. RS-485 cung cấp truyền thông bán song "
        "công, vì một trạm không thể đồng thời phát và nhận những dòng dữ liệu độc lập. Mỗi trạm "
        "trong một hệ RS-485 có thể có hoặc một bên phát, hoặc một bên thu, hoặc cả hai (thường "
        "gọi là bộ thu phát). Phần lớn các hiện thực cung cấp một bộ thu phát. Khi một bộ thu "
        "phát đang phát, mọi bộ khác phải đang thu (nghĩa là không phát). Trạm nào được phép "
        "phát vào lúc nào không được quy định trong tiêu chuẩn, và phải do một giao thức ở tầng "
        "cao hơn đảm nhiệm (ví dụ Interbus-S, Profibus-DP). Hình 88.3 cho thấy một dạng sóng "
        "RS-485 mẫu, minh hoạ tính chất vi sai của kiểu tín hiệu hoá."))
    b.append(fig(3, "vi"))

    b.append(h3("Seriplex", "Seriplex"))
    b.append(p(
        "Seriplex® là một hệ ghép kênh nối tiếp, số, do Automated Process Control, Inc. ở "
        "Jackson, MS phát triển. Tập đoàn Square D đã mua lại Automated Process Control và "
        "quyền đối với Seriplex vào năm 1995, và sau đó lập ra Tổ chức Công nghệ Seriplex (STO) "
        "để quản lý giao thức này. Seriplex được thiết kế đặc biệt hiệu quả trong việc xử lý số "
        "lượng lớn các điểm vào và ra số hay đóng/ngắt. Seriplex cung cấp ba dây truyền thông: "
        "một dây cho tín hiệu đồng hồ, một dây cho tín hiệu dữ liệu, và một dây mốc đất. Hệ có "
        "thể được vận hành ở hai chế độ khác nhau (ngang hàng và chủ–tớ). Ở chế độ chủ–tớ, một "
        "trạm được chỉ định là chủ. Chủ đồng bộ hoá mọi việc truyền dữ liệu giữa các trạm bằng "
        "cách lái một dạng sóng số trên đường đồng hồ mà mọi trạm đều nghe và dùng để định thời "
        "các thao tác phát và nhận. Chủ tạo ra một mẫu lặp lại trên đường đồng hồ khiến mọi trạm "
        "phát và/hoặc nhận dữ liệu trong mỗi chu kỳ, hay mỗi lần “quét” mạng. Mỗi trạm được cấp "
        "một địa chỉ, và dùng địa chỉ ấy cùng với tín hiệu đồng hồ để xác định khi nào thì lái "
        "đường dữ liệu (trong trường hợp một điểm vào) hoặc khi nào thì theo dõi đường dữ liệu "
        "để có dữ liệu ra hợp lệ (trong trường hợp một điểm ra). Có những biến thể trong hiện "
        "thực cho phép nhiều tốc độ đồng hồ và tốc độ bit khác nhau (16, 100 và 200 kHz). Những "
        "chi tiết giao thức khác cho phép xử lý các điểm vào và ra tương tự hay nhiều bit (bằng "
        "cách ghép nhiều bit trên những lần quét liên tiếp), phát hiện sự cố bus, dư thừa đầu "
        "vào, và điều khiển lỗi truyền thông nhờ dùng nhiều lần quét mạng. Việc hiện thực giao "
        "thức trong một cảm biến hay thiết bị khác thường đòi hỏi dùng một ASIC Seriplex (mạch "
        "tích hợp chuyên dụng) phải được cấp phép từ STO [4]."))

    b.append(h3("AS-i", "AS-i"))
    b.append(p(
        "Giao diện Cảm biến – Cơ cấu chấp hành, hay AS-i, được một liên doanh chủ yếu gồm các "
        "công ty châu Âu phát triển, với mục tiêu tạo ra một phương pháp chi phí thấp và linh "
        "hoạt để nối cảm biến và cơ cấu chấp hành ở những mức thấp nhất của hệ điều khiển công "
        "nghiệp. Hệ này được quản lý bởi một tổ chức độc lập toàn cầu [5]. Hệ AS-i cung cấp một "
        "cáp hai dây không xoắn để nối các thiết bị với nhau. Thiết bị có thể lấy dòng từ hai "
        "dây ấy (danh định 24 V dc) để cấp nguồn cho mạch điện, và việc truyền thông dữ liệu "
        "được điều chế chồng lên mức dc danh định ở tốc độ bit 167 kHz, dưới sự điều khiển của "
        "bộ chủ. Mỗi trạm dùng một bit chẵn lẻ để phát hiện lỗi. Tương tự Seriplex, một thiết bị "
        "AS-i thường được hiện thực bằng một ASIC chuyên dụng đảm nhiệm việc truyền thông."))

    b.append(h3("Interbus-S", "Interbus-S"))
    b.append(p(
        "Interbus-S do Phoenix Contact phát triển [6] và được Câu lạc bộ Interbus-S điều hành. "
        "Tô-pô của mạng là một vòng, với dữ liệu được dịch chuyển tuần tự từ điểm này sang điểm "
        "khác trên vòng dưới sự điều khiển của một bộ chủ mạng. Mỗi thiết bị trong vòng hoạt "
        "động như một thanh ghi dịch, phát và nhận dữ liệu đồng thời ở 500 kHz. Việc truyền dữ "
        "liệu nối tiếp thực tế giữa các trạm tuân theo RS-485. Các lần truyền của Interbus-S có "
        "kèm một CRC để phát hiện lỗi. Interbus-S (Interbus-S Remote Bus) cũng đã được mở rộng "
        "để bao gồm một giao thức con gọi là Interbus-Sensor Loop (hay Interbus-S Local Bus). "
        "Giao thức con này cung cấp một tầng vật lý thay thế, với một cặp dây xoắn duy nhất mang "
        "cả nguồn lẫn dữ liệu trên cùng những dây ấy, và giảm kích thước tối thiểu của thanh ghi "
        "dịch trong mỗi trạm từ 16 xuống 4 bit. Mỗi hệ vòng cảm biến Interbus có thể hoạt động "
        "như một trạm đơn trên một mạng Interbus-S, hoặc vòng cảm biến có thể được nối trực tiếp "
        "vào một bộ điều khiển hay bộ chủ. Các thiết bị Interbus-S thường được hiện thực bằng "
        "một ASIC chuyên dụng."))
    b.append(fig(4, "vi"))

    b.append(h3("CAN", "CAN"))
    b.append(p(
        "Mạng vùng điều khiển (CAN) là một công nghệ mạng ở tầng liên kết dữ liệu (tầng 2) do "
        "Tập đoàn Robert Bosch phát triển [7], với mục tiêu ứng dụng là mạng trên xe ô tô. Công "
        "nghệ này được tiêu chuẩn hoá trong ISO 11898 [8], được cấp phép cho mọi nhà sản xuất "
        "mạch tích hợp lớn, và được bán rộng rãi — cả dưới dạng những bộ điều khiển CAN riêng "
        "lẫn dưới dạng bộ điều khiển CAN tích hợp với bộ vi xử lý. Kết quả là CAN đã được dùng "
        "trong nhiều ngành khác nhau. Là một công nghệ ở tầng liên kết dữ liệu, nó không phải là "
        "một định nghĩa mạng hoàn chỉnh. Một số lựa chọn tầng vật lý có thể dùng với CAN (ví dụ "
        "cặp dây xoắn, sợi quang, vô tuyến cao tần) và một số đã được tiêu chuẩn hoá (ví dụ ISO "
        "11898). Ngoài ra, một số giao thức tầng ứng dụng đã được phát triển để dùng với CAN, "
        "chẳng hạn DeviceNet, Smart Distributed System (SDS), CANOpen [9] và SAE J1939 [10]. Cả "
        "DeviceNet [11] lẫn Smart Distributed System [12] đều đã phát triển những hệ thống để "
        "tạo ra các mạng thiết bị trường công nghiệp cho xưởng sản xuất, bao gồm cảm biến và cơ "
        "cấu chấp hành."))

    b.append(h3("Vòng dòng 4 đến 20 mA", "4 to 20 mA Current Loop"))
    b.append(p(
        "Vòng dòng 4 đến 20 mA là một phương pháp được dùng rộng rãi để chuyển thông tin từ một "
        "trạm (bên phát) sang một trạm khác (bên thu). Do đó, hệ này chỉ cho phép hai trạm. Một "
        "hệ vòng dòng điển hình gán một dải cảm biến (ví dụ 0 đến 100 °C) cho dải dòng điện từ 4 "
        "đến 20 mA. Giữa bên phát và bên thu tồn tại một vòng (tức hai dây). Bên phát có thể áp "
        "một dòng điện nhất định vào vòng (dùng một nguồn dòng được điều khiển) để bên thu có "
        "thể đo dòng trong vòng (ví dụ bằng cách đặt một điện trở nhỏ nối tiếp với vòng và đo độ "
        "sụt áp trên điện trở ấy). Sau khi đo dòng, bên thu có thể xác định mức hiện thời của "
        "tín hiệu cảm biến trong dải cảm biến đã định. Phương pháp này dùng tín hiệu hoá bằng "
        "dòng điện thay vì bằng điện áp, và do đó tương đối không bị ảnh hưởng bởi những khác "
        "biệt điện thế giữa bên phát và bên thu. Điều này tương tự lợi ích của tín hiệu hoá vi "
        "sai (bằng điện áp), vốn cũng cần hai dây. Một đặc điểm khác của phương pháp này là nó "
        "không mang tính số như nhiều hệ truyền thông cảm biến khác. Giá trị đo có thể biến "
        "thiên liên tục trong dải 4 đến 20 mA, và do đó có thể dễ dàng biểu diễn một dải cảm "
        "biến tương tự, thay vì một tập hợp tín hiệu số. Ngoài ra, tín hiệu là liên tục biến "
        "thiên và luôn sẵn có. Một đặc điểm nữa của phương pháp này là có thể kiểm chứng tính "
        "toàn vẹn của vòng. Chừng nào vòng còn không bị đứt và bên phát còn trong tình trạng "
        "làm việc tốt, dòng trong vòng sẽ không bao giờ xuống dưới 4 mA. Nếu dòng tiến về 0 mA, "
        "thì bên thu có thể xác định rằng có sự cố — có lẽ là một cáp bị đứt. Những hệ này được "
        "dùng rộng rãi trong nhiều ngành điều khiển quá trình (ví dụ lọc dầu) để nối cảm biến "
        "(bên phát) với máy tính điều khiển. Bởi vì một trạm luôn là bên phát và một trạm luôn "
        "là bên thu, đây là một hệ truyền thông một chiều, bán song công."))

    b.append(h3("HART", "HART"))
    b.append(p(
        "HART® là một giao thức xây dựng trên các hệ truyền thông 4 đến 20 mA. Ý tưởng cơ bản là "
        "có thể truyền thêm dữ liệu (ngoài tín hiệu cảm biến cơ bản đang được mang trong vòng "
        "dòng) bằng cách điều chế một tín hiệu chồng lên dòng điện chảy trong vòng. Phương pháp "
        "điều chế thực tế tuân theo sát tiêu chuẩn Bell 202 cho truyền thông modem tương tự trên "
        "đường điện thoại ở 1200 bit/s. Bởi vì một vòng dòng 4 đến 20 mA mang một tín hiệu biến "
        "thiên tương đối chậm, nên dễ dàng tách tín hiệu 4 đến 20 mA khỏi tín hiệu số bằng các "
        "bộ lọc. Tiêu chuẩn Bell 202 dùng khoá dịch tần với pha liên tục giữa hai tần số, với "
        "tối đa 1200 lần dịch mỗi giây, để điều chế các bit số 1 và 0 lên vòng dòng 4 đến 20 mA. "
        "Phương pháp này cho phép truyền thông hai chiều, toàn song công giữa hai trạm, chồng "
        "lên tín hiệu 4 đến 20 mA. Cũng có thể cấu hình truyền thông HART trên một mạng không "
        "mang tín hiệu 4 đến 20 mA, trong trường hợp đó có thể nối tới 15 thiết bị với nhau trên "
        "mạng. HART do Tập đoàn Fisher-Rosemount phát triển, và đã được chuyển giao cho một quỹ "
        "độc lập quản lý [13]. Bởi vì HART tương thích với các hệ điện thoại của Hoa Kỳ, về lý "
        "thuyết nó có thể chạy trên đường điện thoại và do đó có khả năng chạy trên những "
        "khoảng cách dài tuỳ ý."))

    b.append(h3("Profibus", "Profibus"))
    b.append(p(
        "Profibus (PROcess FIeld BUS) là một trong ba mạng được một tiêu chuẩn châu Âu tiêu "
        "chuẩn hoá [14]. Profibus do một tổ chức toàn cầu, PNO, điều hành [15]. Profibus là một "
        "tiêu chuẩn mạng bao trùm, bao gồm ba mạng con trong họ Profibus. Profibus-DP "
        "(Distributed Periphery — ngoại vi phân tán) là biến thể được thiết kế riêng cho việc "
        "truyền thông với các thiết bị trường (cảm biến và cơ cấu chấp hành) ở mức vào/ra của "
        "thiết bị. Profibus-PA (Process Automation — tự động hoá quá trình) là biến thể có nhiều "
        "năng lực hơn, được thiết kế để hỗ trợ nhu cầu của việc nối mạng ở mức thiết bị cho các "
        "ngành quá trình, chẳng hạn lọc dầu. Một trong những năng lực của Profibus-PA là khả "
        "năng được lắp đặt theo kiểu an toàn nội tại, qua đó đem lại mức an toàn cao hơn trong "
        "những môi trường có thể nổ hay nguy hiểm theo cách khác. Profibus-PA thường dùng một "
        "đặc tả tầng vật lý chuyên dụng được tiêu chuẩn hoá trong IEC 1158-2, đặc tả này được "
        "một số hệ mạng dùng cho các ứng dụng tự động hoá quá trình. IEC 1158-2 quy định một "
        "hiện thực cặp dây xoắn hai dây mang cả nguồn lẫn dữ liệu trên cùng hai dây ấy ở 31,25 "
        "kbit/s. Profibus-FMS (Fieldbus Messaging Specification — đặc tả nhắn tin fieldbus) đại "
        "diện cho hiện thực ở mức cao nhất, được dùng để nối các bộ điều khiển với nhau (không "
        "phải thiết bị trường hay thiết bị vào/ra) trong một nhà máy."))
    b.append(p(
        "Các hệ Profibus-DP thường là hệ chủ–tớ, trong đó thường có một bộ chủ mạng duy nhất "
        "(bộ điều khiển chủ) truyền thông với một số thiết bị tớ (các khối vào/ra từ xa và các "
        "thiết bị vào/ra khác). Giao thức cung cấp việc trao đổi thông tin vào/ra theo chu kỳ "
        "cũng như việc trao đổi theo yêu cầu đối với những loại thông tin khác. Profibus-DP có "
        "thể được hiện thực trên nhiều tầng vật lý khác nhau, bao gồm RS-485 và sợi quang, ở "
        "nhiều tốc độ bit khác nhau tới 12 Mbit/s. Các thông điệp Profibus có kèm một CRC để "
        "phát hiện lỗi."))

    b.append(h3("Foundation Fieldbus", "Foundation Fieldbus"))
    b.append(p(
        "Foundation Fieldbus (FF) là một tiêu chuẩn mạng nảy sinh từ một nỗ lực trong các tổ "
        "chức tiêu chuẩn của ngành, đặc biệt là ISA-SP50 [16] và IEC SC65C/WG6 [17], nhằm cung "
        "cấp một giải pháp thay thế cho tiêu chuẩn truyền thông cảm biến tương tự 4 đến 20 mA. "
        "FF cung cấp hai mức nối mạng cơ bản: H1 và H2. H1 là một hệ tốc độ thấp hơn, có thể "
        "cung cấp vận hành an toàn nội tại (IS) và dùng một cặp dây xoắn duy nhất để đưa cả "
        "nguồn lẫn truyền thông dữ liệu tới các thiết bị trường, theo IEC 1158-2. Chạy ở tốc độ "
        "bit 31,25 kbit/s, H1 rất giống Profibus-PA khi chạy trên tầng vật lý theo tiêu chuẩn "
        "IEC 1158-2. Hệ H1 được thiết kế để có thể nối theo thứ bậc “lên trên” tới một hệ H2, hệ "
        "này đóng vai trò bộ chủ. FF H2 có thể chạy ở 1 hoặc 2,5 Mbit/s trên dây cặp xoắn, và "
        "cũng cung cấp một lựa chọn IS ở tốc độ 1 Mbit/s. Hệ H2 có thể đóng vai trò đường trục "
        "mạng trong một môi trường nhà máy, mang dữ liệu giữa nhiều hệ H1 khác nhau."))

    b.append(h3("WorldFIP", "WorldFIP"))
    b.append(p(
        "WorldFIP [18] là một công nghệ khác trong số ba công nghệ đã được tiêu chuẩn hoá trong "
        "tiêu chuẩn châu Âu EN 50 170, chạy trên tầng vật lý IEC 1158-2. Nhiều người ủng hộ "
        "WorldFIP đã đón nhận FF và đóng góp vào việc phát triển tiêu chuẩn ấy. WorldFIP là một "
        "thành viên của FF, và kết quả là FF đã đưa nhiều năng lực của WorldFIP vào. Khi chạy "
        "trên tầng vật lý IEC 1158-2, WorldFIP có năng lực tương tự FF."))

    b.append(h3("LonWorks", "LonWorks"))
    b.append(p(
        "LonWorks® là một công nghệ mạng do Tập đoàn Echelon phát triển và kiểm soát [19]. "
        "LonWorks được thiết kế để trở thành một công nghệ mạng đa dụng, thích hợp cho nhiều "
        "ngành khác nhau. LonWorks đã được áp dụng rộng rãi trong ngành tự động hoá và điều "
        "khiển toà nhà, cũng như nhiều ngành khác. Công nghệ LonWorks cốt lõi cho thiết bị nằm "
        "trong những mạch tích hợp đặc biệt — gọi là chip Neuron® — kết hợp nhiều bộ vi xử lý để "
        "quản lý mạng, quản lý truyền thông, và cung cấp một môi trường điều khiển đa dụng. "
        "Những chip này có sẵn từ Motorola, Inc. và Tập đoàn Toshiba, là những bên được cấp phép "
        "công nghệ LonWorks. Echelon cũng đã công bố khả năng cấp phép giao thức LonTalk® cho "
        "những nhà sản xuất khác để hiện thực trên những bộ vi xử lý khác. Mạng LonWorks có thể "
        "được hiện thực trên nhiều tầng vật lý, bao gồm cặp dây xoắn ở nhiều tốc độ bit và các "
        "lựa chọn không dây ở 4800 bit/s, nhưng phổ biến nhất là một hệ cặp dây xoắn vi sai chạy "
        "ở 78 kbit/s. Phần lớn các chi tiết mạng (giao thức LonTalk) được giấu khỏi người dùng "
        "và được đóng gói thành các hàm trong môi trường điều khiển đa dụng. Người dùng lập "
        "trình (bằng một ngôn ngữ như C) cho chip Neuron của mỗi trạm để nó hoạt động theo một "
        "cách nhất định và truyền những mục dữ liệu khác nhau tới các trạm khác. Sau đó, những "
        "công cụ chuyên dụng được dùng để gắn mọi trạm lại với nhau (xử lý việc định địa chỉ và "
        "những chi tiết mạng khác) nhằm tạo ra một mạng hoạt động được. Hệ này kết hợp tính linh "
        "hoạt với một mức độ dễ hiện thực nhất định, và có thể dễ dàng được áp dụng cho nhiều "
        "ứng dụng khác nhau."))

    # ------------------------------------------------------------ 88.4
    b.append(h2("88.4 Áp dụng truyền thông mạng", "Applying Network Communications"))

    b.append(h3("Che chắn", "Shielding"))
    b.append(p(
        "Nhiều mạng truyền thông đòi hỏi phải che chắn môi trường truyền (cáp). Che chắn là một "
        "vật dẫn điện bao bọc hoàn toàn môi trường truyền (ví dụ cặp dây xoắn) để bảo vệ chống "
        "EMI. Che chắn tạo ra một rào cản dẫn điện để làm suy giảm sóng điện từ bên ngoài vỏ "
        "chắn, và tạo ra một đường dẫn để những dòng điện cảm ứng có thể lưu chuyển và quay về "
        "nguồn, thường thông qua một kết nối mốc đất. Vỏ chắn trong các hệ truyền thông thường "
        "chỉ được nối đất tại một điểm duy nhất. Điểm nối đất duy nhất này ngăn không cho vỏ "
        "chắn tham gia vào một “vòng đất”, tức một đường dẫn thay thế cho dòng điện chảy giữa "
        "hai điểm có hiệu điện thế nối với một mốc đất chung. Vòng đất có thể dẫn tới những vấn "
        "đề nhiễu, và có thể phá hoại nếu những dòng điện lạc đủ lớn, vì mối nối đất của vỏ chắn "
        "thường không được chế tạo để mang dòng lớn."))

    b.append(h3("Môi trường truyền", "Media"))
    b.append(p(
        "Những loại môi trường truyền phổ biến nhất cho các hệ mạng rơi vào ba loại: điện, "
        "quang và điện từ. Môi trường truyền điện dựa trên vật dẫn (ví dụ dây đồng), còn môi "
        "trường truyền quang dựa trên ống dẫn sóng quang, tức sợi quang. Môi trường truyền điện "
        "từ gồm không gian tự do, hay những vật liệu nói chung cho sóng điện từ truyền qua, và "
        "được gọi là các hệ không dây. Trong loại môi trường truyền điện có rất nhiều cấu hình "
        "vật dẫn. Phổ biến nhất là cặp không bọc, cặp xoắn không bọc (UTP), cặp xoắn có vỏ bọc "
        "(STP), và đồng trục (COAX). Những cấu hình vật dẫn này có những tính chất khác nhau "
        "quan trọng đối với việc truyền tín hiệu điện, cũng như mức độ miễn nhiễm khác nhau với "
        "EMI. Theo một quy tắc ngón tay cái, chất lượng của các đặc tính đường truyền (truyền "
        "tín hiệu và miễn nhiễm với EMI) tăng dần theo đúng thứ tự vừa liệt kê. Các hệ cặp dây "
        "xoắn nói chung dễ lắp đặt hơn, trong khi các hệ đồng trục và sợi quang nói chung đòi "
        "hỏi những công cụ và phương pháp kết cuối chuyên dụng hơn. Dĩ nhiên, các hệ không dây "
        "dễ lắp đặt, nhưng vẫn phải chú ý tới môi trường truyền. Những đặc tính của không gian "
        "tự do như khoảng cách và lượng EMI hiện diện phải được xét đến để mạng làm việc tin "
        "cậy."))

    b.append(h3("Tốc độ bit", "Bit Rate"))
    b.append(p(
        "Một số mạng chỉ cung cấp một lựa chọn tốc độ bit, trong khi những mạng khác cung cấp "
        "các lựa chọn tốc độ bit do người dùng chọn. Các lựa chọn tốc độ bit có thể phụ thuộc "
        "vào loại môi trường truyền đã lắp đặt. Theo một quy tắc ngón tay cái, tốc độ bit được "
        "chọn nên là tốc độ bit thấp nhất có thể mà vẫn đáp ứng các yêu cầu của ứng dụng về tốc "
        "độ truyền dữ liệu và băng thông tổng thể. Điều này nói chung đem lại vận hành tin cậy "
        "hơn, và nói chung cho mạng khả năng miễn nhiễm cao hơn với những xuống cấp nhỏ, những "
        "vi phạm đặc tả và EMI."))

    b.append(h3("Tô-pô", "Topologies"))
    b.append(p(
        "Có nhiều kiểu tô-pô mạng thường được dùng. Tô-pô nói tới cách sắp xếp vật lý và cách "
        "nối các trạm bằng môi trường truyền. Một số mạng có thể chạy với nhiều kiểu tô-pô khác "
        "nhau; một số chỉ có thể chạy với một kiểu tô-pô nhất định (ví dụ Interbus-S đòi hỏi "
        "tô-pô vòng). Những kiểu tô-pô phổ biến nhất là chuỗi nối tiếp, đường trục–nhánh, vòng "
        "và hình sao. Có những biến thể của các kiểu này, và những mạng kết hợp hoặc có thể chạy "
        "trên những tô-pô rất đa dạng đôi khi được gọi là mạng dạng tự do, dạng cây hay tô-pô tự "
        "do. Hình 88.5 mô tả bằng hình vẽ một số kiểu tô-pô khác nhau. Trong một số trường hợp, "
        "mạng đòi hỏi những tô-pô nhất định. Đi chệch khỏi những tô-pô ấy có thể gây xuống cấp "
        "trong hoạt động của mạng (ví dụ làm hỏng thông điệp) hoặc làm mạng hỏng."))
    b.append(fig(5, "vi"))

    b.append(h3("Cấu hình", "Configuration"))
    b.append(p(
        "Phần lớn các mạng đều bao gồm một việc gì đó thuộc về cấu hình. Cấu hình là quá trình "
        "nối các trạm lại với nhau và gán cho mỗi trạm những tham số lập trình được nhất định "
        "mà mạng cần để vận hành đúng. Tham số cấu hình phổ biến nhất trong nhiều mạng là địa "
        "chỉ trạm. Một số mạng có thể đòi hỏi phải đặt trước những tham số khác, chẳng hạn tốc "
        "độ truyền thông hay tốc độ bit. Một số mạng có khả năng tự cấu hình, nghĩa là tự động "
        "gán tham số cho các trạm như một phần của quá trình khởi động mạng, không cần người "
        "dùng can thiệp tường minh (ví dụ Interbus-S). Nhiều mạng định nghĩa những công cụ khác "
        "nhau, có thể dựa trên máy tính, để gán tham số cho từng trạm nhằm cấu hình mạng. Trong "
        "những trường hợp khác, các trạm có thể có những công tắc hay phương tiện thủ công khác "
        "để cấu hình những tham số cần thiết cho vận hành mạng."))

    # ------------------------------------------------------------ 88.5
    b.append(h2("88.5 Các chủ đề nâng cao", "Advanced Topics"))

    b.append(h3("Công nghệ không dây", "Wireless Technologies"))
    b.append(p(
        "Nhu cầu nối mạng vẫn hiện diện ngay cả trong những môi trường mà một cáp điện hay cáp "
        "quang không thể dễ dàng được đi tới. Đó có thể do nhiều hạn chế khác nhau, chẳng hạn "
        "khó đi một cáp mới từ toà nhà này sang toà nhà khác, hoặc khó nối tới những cảm biến "
        "đang chuyển động hay đặt trên xe. Có hai loại truyền thông không dây nói chung, dựa "
        "trên phổ tần số điện từ. Nhiều công nghệ không dây dùng phổ hồng ngoại. Những công nghệ "
        "này nói chung có việc truyền bị giới hạn trong những ứng dụng có đường ngắm trực tiếp "
        "giữa các trạm. Ngoài ra, khoảng cách nói chung bị giới hạn ở 100 m trở xuống. Do những "
        "hạn chế này, nói chung không có hạn chế pháp lý nào khi dùng những phổ tần ấy, và các "
        "bộ thu phát hồng ngoại nay đang trở nên sẵn có từ nhiều nhà sản xuất khác nhau."))
    b.append(p(
        "Loại truyền thông không dây nói chung còn lại dựa trên truyền thông cao tần (RF). Ở "
        "phần lớn các nước, việc dùng những phổ tần này bị các cơ quan chính phủ kiểm soát chặt. "
        "Kết quả là việc dùng mạng không dây trong phần lớn những dải tần ấy đòi hỏi giấy phép "
        "đặc biệt. Tuy nhiên, một số dải tần được dành riêng cho truyền thông công cộng công "
        "suất thấp. Trong những dải tần này, thiết bị được phép truyền thông không cần giấy phép "
        "miễn là chúng phát theo những quy tắc nhất định về công suất phát. Các hệ không dây dựa "
        "trên RF nói chung không bị giới hạn ở những ứng dụng đường ngắm, và có thể được thiết "
        "kế để phủ những khoảng cách lớn hơn các hệ dựa trên hồng ngoại."))
    b.append(p(
        "Có thể xem các công nghệ không dây đơn giản là một lựa chọn nữa cho môi trường truyền "
        "của tầng vật lý, tức không gian tự do. Như vậy, trong một số trường hợp có thể xét một "
        "môi trường truyền không dây cho việc hiện thực nhiều giao thức khác nhau. Ví dụ, cả hệ "
        "CAN lẫn hệ LonWorks đều có thể là ứng viên cho việc nối mạng không dây."))

    b.append(h3("Sợi quang", "Fiber Optics"))
    b.append(p(
        "Một lựa chọn môi trường truyền khác ở tầng vật lý là môi trường sợi quang. Môi trường "
        "sợi quang dùng những xung ánh sáng được dẫn theo một ống dẫn sóng hình ống (sợi thuỷ "
        "tinh hay nhựa) để truyền thông tin từ trạm này sang trạm khác. Sợi quang có một số lợi "
        "ích so với cách đi dây đồng truyền thống. Thứ nhất, suy hao ánh sáng trong sợi quang "
        "nói chung nhỏ hơn suy hao của một tín hiệu điện trong dây đồng khoảng một bậc. Thứ "
        "hai, các hệ truyền sợi quang có thể được điều chế (hay tạo xung) ở những tần số cao hơn "
        "nhiều, đem lại băng thông và tốc độ bit tiềm năng lớn hơn môi trường truyền đồng. Cuối "
        "cùng, các hệ sợi quang nói chung miễn nhiễm với những nguồn EMI truyền thống vốn có "
        "thể gây rắc rối cho các hệ môi trường truyền đồng. Cũng có những hạn chế trong các hiện "
        "thực sợi quang hiện nay. Một trong những hạn chế là phải dùng công cụ và kỹ thuật kết "
        "cuối chuyên dụng để nối một cáp sợi quang với một cảm biến hay thiết bị trường. Thứ "
        "hai, các “điểm rẽ” sợi quang không dễ tạo ra. Do đó, phần lớn các hệ sợi quang được "
        "hiện thực theo kiểu điểm-tới-điểm. Khi có nhiều thiết bị trong một mạng, mỗi thiết bị "
        "thường hoạt động như một bộ lặp quang, với một cổng vào sợi quang và một cổng ra sợi "
        "quang."))

    b.append(h3("Những cân nhắc khi thiết kế mạng", "Network Design Considerations"))
    b.append(p(
        "Thiết kế một hệ truyền thông mạng từ đầu có thể là một công việc dài hơi, và không nên "
        "được xét tới trừ khi việc rà soát cẩn thận các công nghệ sẵn có đã không đem lại giải "
        "pháp nào cho những yêu cầu cụ thể của ứng dụng. Người thiết kế phải xét tới một số câu "
        "hỏi nền tảng để định hình năng lực của mạng. Một chủ đề thường được nhắc tới trong lĩnh "
        "vực nối mạng cho các ứng dụng điều khiển là vấn đề tính tất định. Điều này nói tới khả "
        "năng của mạng trong việc hành xử theo một cách dự đoán được dưới bất kỳ tập kích thích "
        "hay điều kiện bên ngoài nào. Nhiều mạng không thể hiện được đặc tính này. Một câu hỏi "
        "khác cần được giải quyết là vấn đề ưu tiên và truy nhập môi trường. Người thiết kế "
        "phải xác định những điều kiện mà theo đó một trạm cụ thể được phép phát, và nếu nhiều "
        "trạm cùng cố phát, thì xác định trạm nào sẽ được ưu tiên phát trước bằng cách nào. Các "
        "phương pháp truy nhập môi trường thường tác động tới khả năng của một mạng trong việc "
        "hành xử theo kiểu tất định."))

    b.append(h3("Tích hợp cảm biến với truyền thông — IEEE P1451",
                "Integrating Sensors with Communications — IEEE P1451"))
    b.append(p(
        "Một phát triển gần đây đáng chú ý trong lĩnh vực mạng cảm biến là một nỗ lực do IEEE "
        "bảo trợ [20] từ uỷ ban TC-9 của tổ chức này, mang tên IEEE P1451. Hoạt động này đang "
        "hướng tới việc phát triển một tiêu chuẩn định nghĩa các giao diện cảm biến (hay đầu "
        "chuyển đổi) với mạng một cách tổng quát. Phần đầu của tiêu chuẩn đề xuất, IEEE "
        "P1451.1, bao gồm những định nghĩa cho giao diện giữa thiết bị và mạng (xem Hình 88.1). "
        "Phần thứ hai, IEEE P1451.2, bao gồm những định nghĩa cho giao diện giữa đầu chuyển đổi "
        "(hay cảm biến) và khối giao diện mạng bên trong thiết bị. P1451.2 bao gồm một định "
        "nghĩa cho tờ dữ liệu điện tử của đầu chuyển đổi, hay TEDS, định nghĩa một tập thông "
        "tin tóm tắt liên quan tới cảm biến, cho phép trao đổi dữ liệu trên mạng một cách tiêu "
        "chuẩn hoá. Tiêu chuẩn đề xuất này có tiềm năng đem lại lợi ích là làm cho việc nối một "
        "cảm biến với nhiều loại mạng trở nên dễ dàng hơn, và cho phép những cảm biến tương tự "
        "từ các nhà sản xuất khác nhau được xử lý theo cùng một cách trên mạng."))

    # ------------------------------------------------------------ glossary
    b.append(h2("Thuật ngữ chương 88", "Chapter 88 terminology"))
    b.append(note(
        "Phần này do người dịch bổ sung, không có trong nguyên bản: đây là những thuật ngữ mà "
        "chính chương 88 định nghĩa rải rác trong mục 88.2, được gom lại thành một bảng để tiện "
        "tra cứu khi đọc. Định nghĩa giữ nguyên nội dung của nguyên bản, chỉ rút gọn câu chữ."))
    b.append(_glossary(_GLOSS_VI))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    b.append(h2("Đọc thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER_VI))
    return "".join(b)


# ================================================================ DATA
_GLOSS_VI = [
    ("Trạm (station)",
     "Một phần tử truyền thông đơn lẻ trên hệ mạng; mỗi người dùng truy nhập mạng qua một "
     "trạm, và mỗi trạm thường hiện thực một phần mô hình tham chiếu OSI."),
    ("Truy nhập môi trường (media access)",
     "Cách thức từng trạm xác định khi nào nó được phép phát trên môi trường truyền chung."),
    ("MAC (media access control)",
     "Chức năng điều khiển truy nhập môi trường, thường được thực hiện ở tầng liên kết dữ liệu "
     "của mô hình OSI."),
    ("CSMA/CD",
     "Đa truy nhập có cảm nhận sóng mang và phát hiện xung đột: mọi trạm nghe mạng trước khi "
     "phát; nếu hai trạm phát đồng thời thì cả hai ngừng ngay và chờ một khoảng ngẫu nhiên. "
     "Ethernet là ví dụ; CAN dùng một biến thể."),
    ("Chuyển thẻ bài (token passing)",
     "Một “thẻ bài” lôgic được trao vòng giữa các trạm; chỉ trạm giữ thẻ mới được phát, các "
     "trạm khác chỉ nhận."),
    ("Chủ–tớ (master–slave)",
     "Một trạm (chủ) khởi phát mọi liên lạc; các trạm tớ chỉ đáp lại khi được chủ gọi. "
     "Profibus-FMS dùng cả chuyển thẻ bài lẫn chủ–tớ."),
    ("Băng thông (bandwidth)",
     "Năng lực vận chuyển dữ liệu số của hệ. Băng thông thô gắn với tốc độ bit của tầng vật lý "
     "và tầng liên kết dữ liệu; băng thông hiệu dụng là tốc độ vận chuyển thông tin có ý nghĩa "
     "với người dùng. Băng thông nói chung tỉ lệ nghịch với khoảng cách nút-tới-nút xấu nhất."),
    ("Định địa chỉ (addressing)",
     "Gán định danh nói chung là duy nhất cho mỗi trạm — hoặc cho từng mẩu dữ liệu — để xác "
     "định nguồn/đích của thông điệp hay để trọng tài truy nhập môi trường."),
    ("Trọng tài (arbitration)",
     "Thủ tục được tuân theo khi nhiều trạm cùng muốn dùng mạng một lúc; gắn chặt với MAC."),
    ("Tín hiệu hoá (signaling)",
     "Cách biểu diễn vật lý (điện, quang…) của dữ liệu khi được mang trên môi trường truyền. "
     "Việc gán mọi phần tử dữ liệu biểu diễn được với cách biểu diễn tín hiệu tương ứng tạo "
     "thành sơ đồ tín hiệu hoá."),
    ("Tín hiệu hoá vi sai (differential signaling)",
     "Biểu diễn một bit bằng hai trạng thái trên một cặp dây; dữ liệu được xác định bằng hiệu "
     "điện áp giữa hai dây chứ không bằng mức tuyệt đối trên một dây. Nhờ vậy bên thu không cần "
     "biết điện thế đất của bên phát. RS-485 là ví dụ."),
    ("Mã hoá / giải mã (encoding / decoding)",
     "Chuyển thông tin có ý nghĩa với người dùng thành các phần tử dữ liệu để mạng vận chuyển, "
     "và quá trình ngược lại."),
    ("Sổ mã (code book)",
     "Tập hợp mọi quan hệ giữa thông tin có ý nghĩa với người dùng và dữ liệu được mạng mang "
     "đi. Ghép kênh phân chia theo mã (CDM) tách sổ mã thành từng phần, mỗi phần cho một dòng "
     "thông tin."),
    ("Điều chế (modulation)",
     "Dùng dữ liệu để điều khiển tổ hợp tần số, pha và/hoặc biên độ của một tín hiệu mang; bên "
     "thu giải điều chế để lấy lại thông tin. Các hệ mạng có điều chế nằm ngoài phạm vi chương "
     "này."),
    ("Thông điệp / khung (message / frame)",
     "Thông điệp là đơn vị thông tin cơ bản, không chia nhỏ được, được trao đổi giữa các trạm. "
     "Tầng liên kết dữ liệu cấu trúc các bit thành những nhóm gọi là khung hay thông điệp."),
    ("Ghép kênh (multiplexing)",
     "Cho nhiều thông điệp hay dòng thông tin cùng dùng một môi trường truyền. TDM chia theo "
     "lượng tử thời gian; CDM chia theo phần của sổ mã; FDM chia băng thông thành các dải tần."),
    ("Giao thức (protocol)",
     "Phương pháp trao đổi thông tin đã được định nghĩa, thường ở nhiều mức của mô hình OSI; "
     "quy định cách sử dụng dịch vụ của một tầng và cách diễn giải kết quả."),
    ("Dịch vụ (service)",
     "Một chức năng hay thao tác cụ thể do một tầng trong mô hình OSI cung cấp."),
    ("Tô-pô (topology)",
     "Cách bố trí vật lý hay địa lý của mạng: chuỗi nối tiếp, đường trục–nhánh, vòng, hình "
     "sao; các biến thể được gọi là mạng dạng tự do, dạng cây hay tô-pô tự do."),
    ("Tốc độ bit thô và hiệu dụng (raw / effective bit rate)",
     "Tốc độ bit thô là tốc độ thực tế truyền bit trên mạng; tốc độ bit hiệu dụng (thông "
     "lượng) là tốc độ truyền thông tin người dùng, nhỏ hơn hoặc bằng tốc độ thô vì phần phụ "
     "trội dành cho giao thức, định thời và thông tin mạng khác."),
    ("Bán song công / toàn song công (half / full duplex)",
     "Bán song công: một trạm hoặc phát hoặc nhận, không đồng thời. Toàn song công: phát và "
     "nhận đồng thời."),
    ("Điều khiển lỗi (error control)",
     "Bốn khía cạnh: phòng ngừa (ví dụ che chắn, điều khiển lấy mẫu), phát hiện (chẵn lẻ, CRC), "
     "sửa (phát lại, hoặc bit dư để bên nhận tái tạo dữ liệu), và cô lập (định vị nguồn lỗi và "
     "tách phần mạng bị lỗi để phần còn lại tiếp tục làm việc)."),
    ("Bộ lặp / cầu nối / bộ định tuyến / cổng nối",
     "Bộ lặp nối ở tầng vật lý và không tác động tới thông điệp; cầu nối nối ở tầng liên kết "
     "dữ liệu; bộ định tuyến phân vùng những mạng tương tự nhưng không đồng nhất về lôgic, "
     "chọn thông điệp để chuyển ở tầng mạng; cổng nối nối những mạng không đồng dạng và phải "
     "chuyển dịch, ánh xạ, định tuyến thông điệp."),
    ("Mô hình tham chiếu OSI",
     "Mô hình của ISO chia mạng thành bảy tầng: 1 vật lý, 2 liên kết dữ liệu, 3 mạng, 4 giao "
     "vận, 5 phiên, 6 trình diễn, 7 ứng dụng. Người dùng tương tác ở tầng 7, môi trường truyền "
     "nối vào tầng 1. Các tầng 1, 2 và 7 thường có mặt trong mọi mạng; trong nhiều mạng cảm "
     "biến, chức năng của các tầng 3–6 bị thu gọn vào tầng 7."),
    ("TEDS",
     "Transducer Electronic Data Sheet — tờ dữ liệu điện tử của đầu chuyển đổi, do IEEE "
     "P1451.2 định nghĩa: một tập thông tin tóm tắt về cảm biến, cho phép trao đổi dữ liệu trên "
     "mạng một cách tiêu chuẩn hoá."),
]

_REFS = [
    "ISO/IEC 7498-1:1994 <i>Information Technology — Open Systems Interconnection — Basic "
    "Reference Model: The Basic Model</i>, International Organization for Standardization "
    "(ISO), 1, rue de Varembé, Case postale 56, CH-1211 Genève 20, Switzerland, [online]. "
    "Available http://www.iso.ch/.",
    "8802-3: 1996 (ISO/IEC) [ANSI/IEEE Std 802.3, 1996 Edition] <i>Information Technology — "
    "Telecommunications and information exchange between systems — Local and metropolitan area "
    "networks — Specific requirements — Part 3: Carrier sense multiple access with collision "
    "detection (CSMA/CD) access method and physical layer specifications</i>, Institute of "
    "Electrical and Electronics Engineers, 445 Hoes Lane, Piscataway, NJ 08855-1331, [online]. "
    "Available http://www.ieee.org/.",
    "ANSI/EIA/TIA-232-E-91, Electronic Industries Association, 2500 Wilson Boulevard, Arlington, "
    "VA 22201-3834, [online]. Available http://www.eia.org/.",
    "<i>Distributed, Intelligent I/O for Industrial Control and Data Acquisition… The SERIPLEX "
    "Control Bus</i>, Bulletin No. 8310PD9501R4/97, Seriplex Technical Organization, P.O. Box "
    "27446, Raleigh, NC 27611-7446, [online]. Available http://www.seriplex.org/.",
    "AS-Interface U.S.A., 5010 East Shea Blvd., Suite C-226, Scottsdale, AZ 85254, [online]. "
    "Available http://www.as-interface.com/.",
    "<i>Interbus-S Protocol Structure</i>, Data Sheet 0005C, Phoenix Contact, P.O. Box 4100, "
    "Harrisburg, PA 17111, [online]. Available http://www.ibsclub.com/.",
    "<i>CAN Specification, Version 2.0</i>, 1991, Robert Bosch GmbH, Postfach 50, D-7000 "
    "Stuttgart 1, Germany.",
    "ISO 11898:1993 <i>Road vehicles — Interchange of digital information — Controller area "
    "network (CAN) for high-speed communication</i>, International Organization for "
    "Standardization (ISO), 1, rue de Varembé, Case postale 56, CH-1211 Genève 20, Switzerland, "
    "[online]. Available http://www.iso.ch/.",
    "<i>CiA Draft Standard 301 (Version 3.0), CANopen Communication Profile for Industrial "
    "Systems</i>, CiA Headquarters, Am Weichselgarten 26, D-91058 Erlangen, Germany, [online]. "
    "Available http://www.can-cia.de/.",
    "<i>SAE J 1939 — Recommended Practice for Serial Control and Communications Vehicle "
    "Network</i>, Society of Automotive Engineers, 400 Commonwealth Drive, Warrendale, PA 15096, "
    "[online]. Available http://www.sae.org/.",
    "<i>DeviceNet Specification v1.4</i>, Open DeviceNet Vendors Association, 8222 Wiles Road, "
    "Suite 287, Coral Springs, FL 33067, [online]. Available http://www.odva.org/.",
    "<i>Smart Distributed System Application Layer Protocol Specification v2.0</i>, 1996, "
    "Honeywell MICRO SWITCH Division, 11 West Spring Street, Freeport, IL 61032, [online]. "
    "Available http://www.sensing.honeywell.com/sds/.",
    "HART Communication Foundation, 9390 Research Boulevard, Suite I-350, Austin, TX 78759 "
    "[online]. Available http://www.ccsi.com/hart/hcfmain.html.",
    "EN 50 170 — Volume 2, CENELEC Central Secretariat, 35, rue de Stassart, B-1050 Brussels, "
    "Belgium.",
    "PROFIBUS Trade Organization U.S.A., 5010 East Shea Blvd., Suite C-226, Scottsdale, AZ "
    "85254-4683, [online]. Available http://www.profibus.com/.",
    "ISA, the International Society for Measurement &amp; Control, P.O. Box 12277, Research "
    "Triangle Park, NC 27709, [online]. Available http://www.isa.org/.",
    "IEC 61158-2(1993-12), <i>Fieldbus standard for use in industrial control systems — Part 2: "
    "Physical layer specification and service definition</i>, International Electrotechnical "
    "Commission, 3, rue de Varembé, PO Box 131, 1211 Geneva 20, Switzerland, [online]. Available "
    "http://www.iec.ch/.",
    "WorldFIP Headquarters, 2, rue de Bone, 92160 Antony, France, [online]. Available "
    "http://www.worldfip.org/.",
    "005-0017-01 Rev C, <i>LonTalk Protocol</i>, Echelon Corporation, 4015 Miranda Avenue, Palo "
    "Alto, CA 94304, [online]. Available http://www.echelon.com/.",
    "P1451.2, <i>Draft Standard for a Smart Transducer Interface for Sensors and Actuators — "
    "Transducer to Microprocessor Communication Protocols and Transducer Electronic Data Sheet "
    "(TEDS) Formats</i>, Institute of Electrical and Electronics Engineers, 445 Hoes Lane, "
    "Piscataway, NJ 08855-1331, [online]. Available http://www.ieee.org/.",
]

_FURTHER_VI = [
    "P. Z. Peebles, Jr., <i>Digital Communications Systems</i>, Englewood Cliffs, NJ: "
    "Prentice-Hall, 1987 — một giáo trình nhập môn tốt về truyền thông.",
    "B. Svacina, <i>Understanding Device Level Buses</i>, Minneapolis, MN: TURCK Inc. (3000 "
    "Campus Dr., Minneapolis, MN 55441), 1996 — một nghiên cứu sâu về mạng truyền thông cho "
    "các thiết bị trường công nghiệp.",
    "J. D. Gibson, chủ biên, <i>The Communications Handbook</i>, Boca Raton, FL: CRC Press, "
    "1997 — gồm những tài liệu gần đây về các kỹ thuật truyền thông.",
]

_FURTHER_EN = [
    "P. Z. Peebles, Jr., <i>Digital Communications Systems</i>, Englewood Cliffs, NJ: "
    "Prentice-Hall, 1987, provides a good general text on communication.",
    "B. Svacina, <i>Understanding Device Level Buses</i>, Minneapolis, MN: TURCK Inc. (3000 "
    "Campus Dr., Minneapolis, MN 55441), 1996, is an in-depth study of the subject of "
    "communication networks for industrial field devices.",
    "J. D. Gibson, Ed., <i>The Communications Handbook</i>, Boca Raton, FL: CRC Press, 1997, "
    "includes recent material on communication techniques.",
]


_GLOSS_EN = [
    ("Station",
     "A single communicating element on a network system; each user reaches the network through "
     "a station, and each station typically implements part of the OSI reference model."),
    ("Media access",
     "The method by which individual stations determine when they are permitted to transmit, or "
     "“use”, the media."),
    ("MAC (media access control)",
     "The media-access control function, usually performed in the data link layer of the OSI "
     "reference model."),
    ("CSMA/CD",
     "Carrier sense multiple access with collision detection: every station listens before "
     "transmitting, and if two transmit at once both stop immediately and wait a random period. "
     "Ethernet is the classic example; CAN uses a variant."),
    ("Token passing",
     "A logical “token” is passed among stations; only the station holding it may transmit, and "
     "all others may only receive."),
    ("Master–slave",
     "One station (the master) originates all communications; slaves respond only when the "
     "master addresses them. Profibus-FMS uses both token passing and master–slave."),
    ("Bandwidth",
     "The capacity of the system to transport digital data. Raw bandwidth is tied to the bit "
     "rate of the physical and data link layers; effective bandwidth is the rate at which "
     "user-meaningful information travels. Bandwidth is generally inversely proportional to the "
     "worst-case node-to-node distance."),
    ("Addressing",
     "Assigning generally unique identifiers to each station — or to individual pieces of data — "
     "to identify the origin and destination of messages or to arbitrate access to a shared "
     "medium."),
    ("Arbitration",
     "The procedure followed when multiple stations wish to use the network simultaneously; "
     "closely related to MAC."),
    ("Signaling",
     "The actual physical (electrical, optical or other) representation of data on the media. "
     "The association of every representable data element with its signal representation is the "
     "signaling scheme."),
    ("Differential signaling",
     "Representing a bit as two states on a pair of wires; the data element is found from the "
     "voltage difference between the wires, not the absolute level on either. The receiver "
     "therefore needs no knowledge of the transmitter’s ground potential. RS-485 is an example."),
    ("Encoding / decoding",
     "Translating user-meaningful information into data elements for the network to carry, and "
     "the reverse process."),
    ("Code book",
     "The set of all relationships between user-meaningful information and the data carried by "
     "the network. Code division multiplexing splits the code book into sections, one per "
     "information stream."),
    ("Modulation",
     "Using data to control some combination of the frequency, phase and/or amplitude of a "
     "carrier signal; the receiver demodulates to recover the information. Modulated network "
     "systems are outside the scope of this chapter."),
    ("Message / frame",
     "A message is the fundamental, indivisible unit of information exchanged between stations. "
     "The data link layer structures bits into groups identified as frames or messages."),
    ("Multiplexing",
     "Letting several messages or information streams share one medium. TDM splits access into "
     "time quanta; CDM splits the code book; FDM splits bandwidth into frequency ranges."),
    ("Protocol",
     "A defined method of information exchange, usually defined at several levels of the OSI "
     "model; it states how a layer’s services are exercised and how their results are "
     "interpreted."),
    ("Service",
     "A specific function or operation supported by a particular layer of the OSI reference "
     "model."),
    ("Topology",
     "The physical or geographic layout of a network: daisy chain, trunkline–branchline, ring, "
     "star. Variants are called free-form, tree or free topology networks."),
    ("Raw and effective bit rate",
     "Raw bit rate is the actual speed of bit transmission on the network; effective bit rate "
     "(throughput) is the speed at which user information travels, less than or equal to the raw "
     "rate because of overhead carrying protocol, timing and other network information."),
    ("Half and full duplex",
     "Half duplex: a station either transmits or receives, not both at once. Full duplex: it "
     "does both simultaneously."),
    ("Error control",
     "Four aspects: prevention (shielding, sampling control), detection (parity, CRC), "
     "correction (retransmission, or redundant bits that let the receiver reconstruct the data), "
     "and isolation (locating the source of errors and cutting off the faulty part so the rest "
     "of the network keeps working)."),
    ("Repeater / bridge / router / gateway",
     "A repeater joins networks at the physical layer and does not affect messages; a bridge "
     "joins at the data link layer; a router partitions similar but not logically identical "
     "networks, choosing messages to pass at the network layer; a gateway joins dissimilar "
     "networks and must translate, map and route messages."),
    ("OSI reference model",
     "ISO’s model decomposing a network into seven layers: 1 physical, 2 data link, 3 network, "
     "4 transport, 5 session, 6 presentation, 7 application. The user interacts with layer 7 and "
     "the medium connects to layer 1. Layers 1, 2 and 7 appear in every network; in many sensor "
     "networks the functions of layers 3–6 collapse into layer 7."),
    ("TEDS",
     "Transducer Electronic Data Sheet, defined by IEEE P1451.2: a summary set of information "
     "about the sensor that allows standardised exchange of data on the network."),
]


# ================================================================ 88 EN
def body_en():
    b = []
    b.append(_transnote("en"))

    b.append(h2("88.1 Introduction"))

    b.append(h3("What Is a Communication Network?"))
    b.append(p(
        "A communication network provides a system by which multiple users may share a single "
        "communication path (or medium) to exchange information. The telephone system is an "
        "example of a system containing many communication networks, which can be considered to "
        "be a single communication network as an abstract example. Communication networks are "
        "commonly used in various industries and applications to provide an economical means to "
        "allow multiple, geographically separated users to exchange information."))

    b.append(h3("Ordinary Sensors vs. Networked Sensors"))
    b.append(p(
        "A definition of the function of a sensor is to map or convert one measured variable "
        "(e.g., spatial, mechanical, electromagnetic, etc.) into another — usually electric — "
        "variable or signal. This signal may then be passed to a measurement or processing "
        "system for capture and analysis, or as a direct input to some controlled process. In "
        "this case, the measured variable is represented as an electric signal. This signal must "
        "be handled individually by the measurement system, and it may also be subject to "
        "corruption from a variety of sources, such as electromagnetic interference in the case "
        "of an electric signal."))
    b.append(p(
        "In applications where a number of sensing devices are needed, and/or where the sensing "
        "devices are distributed geographically (or are distant from the measurement and "
        "analysis system), the application designer may wish to use a communication network to "
        "transmit sensor data from the measurement point to the measurement and analysis system. "
        "Such applications typically involve some sort of digital computing machinery at the "
        "measurement and analysis point, or as part of the control system. Figure 88.1 depicts a "
        "representative block diagram of a sensor/network system showing the relationship of the "
        "various components."))
    b.append(fig(1, "en"))
    b.append(p(
        "Networked sensors can be distinguished into two components: those performing the "
        "measurement function, and those components performing the communication function. In "
        "some cases, these two functions may be designed as a single unit, such that the "
        "“sensor” intrinsically includes communication capability. In other cases, an ordinary "
        "sensor may be connected to a conversion unit, which converts the output signal of the "
        "ordinary sensor into a form suitable for the network, and manages the delivery of this "
        "information on the network."))

    b.append(h3("Why Use Networked Sensors?"))
    b.append(p(
        "Network communication combined with sensor technology can provide several benefits to an "
        "application, as well as to the sensor designer. The most obvious benefit of a network is "
        "the simplification of the wiring for the transmission of the signals from one place to "
        "another. For a system containing <i>N</i> users, the number of wires or cables "
        "<i>T</i> required to individually connect each user with each other user is given by "
        "Equation 88.1:"))
    b.append(eq("<i>T</i> = 2" + _sup("(<i>N</i>−1)") + " − 1", "88.1"))
    b.append(p(
        "assuming each wire or cable can carry information in both directions between the two "
        "users connected by that cable. For more than a few users, the number of cables required "
        "(<i>T</i>) to provide an individual connection between each pair of users is large. "
        "Sensors are often connected to a central measurement and analysis system, and may only "
        "need to communicate with the central system. In this case, the number of individual "
        "wires or cables needed is equal to the number of sensors (<i>N</i> − 1). Even with this "
        "smaller number of cables, the wiring for a large number of sensors in some applications "
        "can be quite complex. A network may be able to reduce the total number of cables "
        "required to a much smaller number. In fact, in a sensor network, all of the sensors and "
        "the central measurement and analysis system can be connected to a single cable."))
    b.append(p(
        "An indirect benefit of networking may be in its handling of the sensor signal. Because "
        "most modern networks are digital in nature, an analog sensor signal typically must be "
        "digitized before it can be transmitted on a network. With a networked sensor, the "
        "digitization will typically be carried out by circuitry in relatively close proximity to "
        "the sensor. As a result, the analog signal will have traveled a short distance before "
        "being converted to a digital signal. This can be a benefit in two ways. The first is "
        "that the analog signal will not suffer as much attenuation or degradation due to "
        "electric losses associated with carrying a signal over a great distance. The second is "
        "that once in digital form, the “signal” can be made relatively immune to the effects of "
        "distortion or degradation due to electromagnetic interference (EMI). Although digital "
        "transmission of signals is still subject to EMI, modern protocols and transmission "
        "systems can be designed to be very robust, using signaling that is resistant to EMI as "
        "well as using error control techniques. As a result, the effect of attenuation and "
        "disturbances can be essentially eliminated by digital transmission of the signal."))
    b.append(p(
        "Another benefit of networking is the ability to communicate a much wider range of "
        "information — in both directions — when compared with a single cable carrying a sensor "
        "signal. With many modern networks suitable for networked sensing applications, a "
        "microprocessor is used at the sensor to manage the handling of the sensor signal and its "
        "transmission on the network. But there is generally no need to limit the microprocessor "
        "to this one function alone. The combination of the network and the microprocessor "
        "provides a platform upon which many additional functions and features can be "
        "incorporated into the networked sensor. For example, the signal of a sensor may need a "
        "certain calibration or correction function applied to it before it can be used in "
        "calculations. It may be beneficial to load into the networked sensor (through the "
        "network) a set of correction parameters or coefficients, and then have the "
        "microprocessor correct or calibrate the output of the sensor before transmitting it to "
        "the network. Sensors can be easily designed to have multiple sensing functions, such as "
        "temperature and pressure, for example. Each signal can be handled separately and "
        "transmitted separately on the network, with no need for additional connections. Sensors "
        "may be designed to store certain types of information, such as the name of the "
        "manufacturer, or certain calibration parameters determined by the manufacturer at the "
        "time of manufacture. This information can then be read out over the network and used "
        "for a variety of purposes. A sensor can even be designed to have “intelligent” "
        "functions, such as the ability to sense its environment and determine when certain "
        "parameters have been exceeded (such as operating temperature range), or report a "
        "special message containing an “alarm” when the sensor signal level exceeds a certain "
        "threshold. The combination of the network and the microprocessor leads to an endless "
        "variety of functions and features that can be added to the basic sensor technology."))

    b.append(h3("Potential Problems with Networked Sensors"))
    b.append(p(
        "Networked sensors will generally require more complex circuitry than equivalent, "
        "nonnetworked sensors. A drawback of analog-to-digital (A/D) conversion and digital "
        "transmission of signals is the time and level quantization effect that A/D conversion "
        "can have on the analog signal. These effects can be mitigated with modern, high-speed "
        "A/D converters (to minimize the effect of time quantization, or the sampling effect) "
        "with the ability to convert in high resolution (i.e., using a large number of digital "
        "bits to represent the analog signal level). These drawbacks are not unique to networked "
        "sensors but rather to digitized sensor values and digital control whether or not it uses "
        "a network. Finally, the capacity of the network to carry information (the bandwidth) "
        "must be considered in any communication system. Putting a large number of sensors on a "
        "single network may overload the information-carrying capability of the network, "
        "resulting in queuing delays in the reception of sensor signals and, in some cases, lost "
        "data."))

    # ------------------------------------------------------------ 88.2
    b.append(h2("88.2 Communication and Networking Concepts"))
    b.append(p(
        "In order to be able to select an appropriate network technology, it is necessary to "
        "understand some basic terminology so that the features and capabilities of various "
        "networks and technologies can be categorized and compared."))

    b.append(h3("Station"))
    b.append(p(
        "A station represents a single communicating element on a network system. Each user of "
        "the network must access the communication capability of the network via a station. Each "
        "station will typically have some implementation of the open systems interconnection "
        "(OSI) network reference model as the means of utilizing the network system."))

    b.append(h3("Media Access"))
    b.append(p(
        "Media access is the method by which individual stations determine when they are "
        "permitted to transmit, or “use” the media. Media access control (MAC) is a function that "
        "is usually performed in the data link layer of the OSI reference model. Some well-known "
        "methods of media access control include carrier sense multiple access with collision "
        "detection (CSMA/CD) and token passing. CSMA/CD systems (such as Ethernet) allow all "
        "stations on a network equal access. Each station must “listen” to the network to "
        "determine periods of inactivity before transmitting. Any station wishing to use the "
        "network may begin transmitting providing the network is inactive when it checks for "
        "activity. If multiple stations attempt to transmit simultaneously, a collision occurs. "
        "This is detected by all transmitting stations, which all must immediately stop "
        "transmitting and each wait a randomly determined period of time, before attempting to "
        "use the network again. Controller area network (CAN), for example, uses a variant of "
        "CSMA/CD for media access. Token-passing systems have a logical “token” which is "
        "exchanged among stations via network messaging. The station that holds the token has "
        "permission to transmit. All other stations are only permitted to receive messages. "
        "Stations wishing to transmit but not having the token must wait until the station "
        "holding the token passes it on. Another commonly used method of media access control is "
        "master–slave. In this method, one station on the network (designated the master) is "
        "generally in charge of, and originates, all communications. Slaves only respond to the "
        "master, and only respond when the master initiates communications with them via sending "
        "a message to the slave. Profibus-FMS (see below) is an example of a protocol which uses "
        "both token passing (in some cases) and master–slave (in some cases) to control media "
        "access."))

    b.append(h3("Bandwidth"))
    b.append(p(
        "Bandwidth may have several different definitions. For digital communication systems, "
        "bandwidth describes the capacity of the system to transport digital data from one place "
        "to another. This term may be applied to the raw capability of the physical and data link "
        "layers to transport message data (raw bandwidth, closely related to the bit rate "
        "concept) or it may be applied to the effective rate at which user-meaningful information "
        "is transported (effective bandwidth). The bandwidth of a given system is generally "
        "inversely proportional to the worst-case node-to-node distance. The smaller the network "
        "span, the higher its bandwidth can be."))

    b.append(h3("Addressing"))
    b.append(p(
        "Addressing is a concept that assigns generally unique identifiers to each station in a "
        "network system. This identifier (the address) can then be used by the network for a "
        "variety of purposes, including identifying the origin and/or destination of messages, or "
        "arbitrating access to a shared communications medium. Another addressing or identifier "
        "concept assigns unique identifiers not to stations, but to unique pieces of data or "
        "signals that will be carried by the network. Stations then use an identifier according "
        "to what type of data they will be transmitting. Many, but not all networking methods "
        "require establishment of an explicit address for each network station."))

    b.append(h3("Arbitration"))
    b.append(p(
        "Arbitration is a function closely related to MAC. Arbitration is used by some networks "
        "to define the procedure followed when multiple stations wish to use the network "
        "simultaneously."))

    b.append(h3("Signaling"))
    b.append(p(
        "Signaling refers to the actual physical (e.g., electrical, optical, or other) "
        "representation of data as it is carried on the media. For example, in some networks, "
        "data elements may be represented by certain voltage levels or waveforms in the media. In "
        "other networks, data elements may be represented by the presence of certain wavelengths "
        "of light in the media. The association of all the representable data elements (e.g., 0/1 "
        "or on/off) with the corresponding signal representations in the media is the signaling "
        "scheme or method. An important signaling method where electric wires are used as the "
        "medium is differential signaling. Differential signaling represents a particular data "
        "element (1 or 0) as two different states on a pair of wires. Determining the data "
        "element requires measuring the voltage difference between the two wires, not the "
        "absolute level of the voltage on either wire. Different data elements are then "
        "represented by the (signed) voltage difference between the two wires. For example, "
        "RS-485 represents a digital 1 data element as a 5-V signal level on the first wire and a "
        "0-V signal level on the second wire, and a digital 0 as a 0-V signal level on the first "
        "wire and 5-V signal level on the second wire. One of the principal benefits of "
        "differential signaling is that it is possible to determine the data being transmitted "
        "without knowing the ground reference potential of the transmitter. This allows the "
        "transmitter and receiver to operate reliably, even when they have different ground "
        "potentials (within limits), which is a common occurrence in communication systems."))

    b.append(h3("Encoding"))
    b.append(p(
        "Encoding refers to the process of translating user-meaningful information into data "
        "elements or groups of data elements to be transported by the network system. A code book "
        "refers to the set of all relationships between user-meaningful information and data "
        "carried by the network. Encoding may occur at several levels within the OSI reference "
        "model, as user-meaningful information is transformed successively until it becomes an "
        "actual network message, produced by the data link layer. Decoding is the reverse "
        "process, whereby a network message is successively translated back into user-meaningful "
        "information."))

    b.append(h3("Modulation"))
    b.append(p(
        "Modulation in a classical sense refers to a signaling technique by which data or "
        "information is used to control some combination of the frequency, phase, and/or "
        "amplitude of a carrier signal. The carrier signal carries the information to a remote "
        "receiver where it will be demodulated to retrieve the information. Modulated network "
        "systems are outside the scope of this chapter."))

    b.append(h3("Message"))
    b.append(p(
        "A message is the fundamental, indivisible unit of information which is exchanged between "
        "stations. User-meaningful information will be grouped into one or more messages by the "
        "OSI network reference model."))

    b.append(h3("Multiplexing"))
    b.append(p(
        "Multiplexing refers to the ability to use the media in a network to carry multiple "
        "messages or information streams “simultaneously.” Multiplexed systems allow several "
        "communication channels to use the same physical wire or media. Each message or "
        "information stream may have different sources and destinations."))
    b.append(p(
        "Multiplexing may be accomplished using a variety of means. Time division multiplexing "
        "(TDM) involves breaking access to the media into a series of time quanta. During each "
        "time quantum, the media carries a separate message or information stream. The close "
        "arrangement of time quanta allows the network media to carry multiple messages "
        "“simultaneously.” Code division multiplexing (CDM) involves the separation of the code "
        "book (see Encoding) into sections. Each section of the code book provides all of the "
        "messages that will be used for a particular information stream. Therefore, a particular "
        "information stream within the network media is distinguished by all of the messages that "
        "belong to the section of the code book for that stream. Frequency division multiplexing "
        "(FDM) divides an available bandwidth of a communication channel into several frequency "
        "ranges, and assigns one information stream to each frequency range."))

    b.append(h3("Protocols"))
    b.append(p(
        "A protocol is a defined method of information exchange. Protocols typically are defined "
        "at several levels within the OSI network reference model, such as at the application "
        "layer and at the data link layer. Protocols are used to define how the services provided "
        "by a particular layer are to be exercised, and how the results of these services are to "
        "be interpreted."))

    b.append(h3("Service"))
    b.append(p(
        "A service represents a specific function or operation that is supported by a particular "
        "layer in the OSI network reference model. For example, an application layer service "
        "might be provided for the reading of or writing to a data element contained in another "
        "device (or station) on the network. This service might make use of a data link layer "
        "service which might be provided for supporting the exchange of a message with another "
        "device (or station) on the network."))

    b.append(h3("Topology"))
    b.append(p(
        "Topology refers to the physical or geographic layout or arrangement of a network. "
        "Certain types of canonical topologies are commonly discussed in the context of networks, "
        "such as trunkline/branchline, star (or hub), ring, and daisy chain."))

    b.append(h3("Bit Rate"))
    b.append(p(
        "Bit rate refers to the speed at which binary pieces of information (bits) are transmitted "
        "on a particular network. The raw bit rate of a network generally refers to the actual "
        "speed of transmission of bits on the network. The effective bit rate — or throughput — "
        "generally refers to the speed at which user information is transmitted. This number is "
        "less than or equal to the raw bit rate, depending on what percentage of the bits "
        "transmitted is used for carrying user information. The bits not carrying user "
        "information are overhead, used to carry protocol, timing, or other network information."))

    b.append(h3("Duplex (Half and Full Duplex)"))
    b.append(p(
        "Half duplex refers to a communication system in which a station can either transmit "
        "information or receive information, but not both simultaneously. A full duplex network "
        "allows a station to transmit information and receive information simultaneously."))

    b.append(h3("Error Control"))
    b.append(p(
        "Many network systems provide mechanisms to control errors. Error control has four "
        "aspects: prevention, detection, correction, and isolation. Error prevention may simply "
        "be shielding for the media to minimize electromagnetic disturbances, or it may be more "
        "complicated, such as signal sampling control to optimize the probability that a signal "
        "will be in the correct state when sampled. Error detection generally depends on "
        "detecting violations of protocol rules at various network levels, or violations of "
        "computed data added to a message for error control purposes. Some examples of error "
        "detection techniques are parity and cyclic redundancy check (CRC). Both methods involve "
        "the computation of additional bits of information based on the data that is contained in "
        "a message, and appending these bits to the message. For example, a particular protocol "
        "may require that the data link layer compute and append a CRC to a message prior to "
        "transmission. The receiver of the message may then also compute the CRC and compare it "
        "to the CRC which has been appended to the message. If a mismatch exists, then it is "
        "assumed an error has occurred."))
    b.append(p(
        "Error correction may take on a variety of forms. One of the simplest methods of error "
        "correction is to require that the data link layer of the transmitter retransmit a message "
        "which has been detected to have an error during transmission. This method is based on "
        "the assumption that the error was caused by a disturbance which is unlikely to occur "
        "again. Another method of error correction involves transmission of additional bits of "
        "information along with the user information in a message. These additional bits of "
        "information are computed by the transmitter to provide redundant information in the "
        "message. When fewer than a certain number of bit-level errors have occurred during the "
        "transmission of the message, the receiver is able to reconstruct the original user "
        "information accurately using the redundant information (bits) supplied within the "
        "message. Error isolation is a capability of some networks to localize the source of "
        "errors and isolate the sections of the network or the stations at which the errors have "
        "been localized. Error isolation allows the fault-free portions of the network to "
        "continue communicating even when other portions of the network have degraded to the "
        "point of generating errors."))

    b.append(h3("Internetworking"))
    b.append(p(
        "There are occasions when communications between two or more points are best handled by "
        "multiple networks. This may be the case when a single network has limitations that "
        "prevent it from tying the points together (e.g., distance limits) or when multiple "
        "networks are required for other reasons (e.g., to carry different types of data). When "
        "multiple networks are used to provide communications, there may be a need to pass "
        "messages or information directly from one network to another."))
    b.append(p(
        "A repeater may be used when the networks to be joined are logically identical, and the "
        "purpose is simply to extend the length of the network or extend its capabilities in some "
        "way. A repeater generally has no effect on messages, and simply carries all messages from "
        "one cable or port to another (i.e., a change of physical media). A repeater allows for "
        "connection of networks at the physical layer level."))
    b.append(p(
        "A bridge is similar to a repeater, but allows for connection of networks at the data "
        "link layer level. Generally, a bridge will pass all messages from one network to "
        "another, by passing messages at the data link layer level."))
    b.append(p(
        "A router usually has the function of partitioning similar networks. Two networks may be "
        "based on the same technologies and protocol, but may not be logically identical. In "
        "these cases, some, but not all, of the messages on one network may need to be carried or "
        "transported to the other network. The router has the function of determining which "
        "messages to pass back and forth based on certain rules. Functions to enable efficient, "
        "automatic routing of messages may be included in layer 3 (the network layer) of the OSI "
        "network reference model, and a router allows for connection of networks at the network "
        "layer level."))
    b.append(p(
        "A gateway may have a function similar to a router, or it may have the function of "
        "joining dissimilar networks, i.e., networks based on dissimilar technologies and/or "
        "protocols. When functioning like a router, a gateway usually performs its discrimination "
        "at a higher protocol level than a router. When a gateway joins dissimilar networks, "
        "generally a more complex set of rules must be designed into the gateway so that message "
        "translation, mapping, and routing can occur within the gateway as it determines which "
        "messages to pass from one network to the other."))

    b.append(h3("ISO/OSI Network Reference Model"))
    b.append(p(
        "The explosion in the use and types of communication networks over the last several "
        "decades has led to more precise descriptions and treatment of communication networks in "
        "general. The International Organization for Standardization (ISO) has recognized one "
        "such method of precise description of networks, called the OSI reference model [1]. As "
        "shown in Figure 88.2, this model decomposes an arbitrary communication network into a "
        "“stack” of seven “layers.” At each layer, certain types of network communication "
        "functions are described. The user of the communication system — usually another system "
        "that needs to communicate on the network — interacts with layer 7, the highest layer. "
        "The actual transmission medium (e.g., copper cable, fiber optic, free space, etc.) is "
        "connected to layer 1, the lowest layer. Most communication networks do not implement all "
        "of the layers in the reference model. In this case, formal definition, treatment, or "
        "inclusion of certain layers of the model in the actual network design are omitted. "
        "Layers 1, 2, and 7 are typically present in all networks, but the other layers may only "
        "be explicitly included or identifiable when their function is an important part of the "
        "network communications. In many sensor communication networks, the functions performed "
        "by layers 3, 4, 5, and 6 are “collapsed” into vestigial additions to the functions of "
        "layer 7, the application layer."))
    b.append(fig(2, "en"))

    b.append(h3("Physical Layer"))
    b.append(p(
        "The physical layer is the lowest layer of the model. This layer is responsible for "
        "converting between the symbolic or data representation of the network messages and the "
        "actual physical representation of data in the network medium. This layer specifies the "
        "behavior of the electric circuits referred to as the transmitter and the receiver. It "
        "also defines physical structures for connectors."))

    b.append(h3("Data Link Layer"))
    b.append(p(
        "The data link layer, or layer 2, is responsible for several functions. This layer "
        "manages access to the network medium (MAC), structures the bits of information into "
        "well-defined groups identified as “frames” or messages, handles identification of source "
        "and destination stations on the network, and provides for error-free transmission of a "
        "message from source to destination stations, all according to the data link layer "
        "protocol. A number of standard data link layer protocols exist, which act as the basis "
        "for many of the communication networks in wide use. Ethernet, or IEEE 802.3, for "
        "example, specifies a MAC sublayer that works with the IEEE 802.2 Logical Link Control "
        "layer to form the data link layer protocol used in the majority of office information "
        "networks [2]."))

    b.append(h3("Network Layer"))
    b.append(p(
        "The network layer encapsulates functions related to routing of messages, both within a "
        "single network and among multiple networks. This layer typically uses addressing in a "
        "variety of forms as a key part of the functions of directing and routing messages, and "
        "the search and usage of the available communication paths."))

    b.append(h3("Transport Layer"))
    b.append(p(
        "The transport layer provides any additional data transfer functions not directly "
        "provided by the data link layer for end-to-end reliable messaging. For example, some "
        "data transfer functions between stations may require the use of multiple data link layer "
        "messages to accomplish a reliable message transfer. The generation of multiple messages "
        "and the sequential disassembly, delivery, and assembly of data is accomplished by the "
        "transport layer. The transport layer also recovers from lost, duplicated and misordered "
        "messages."))

    b.append(h3("Session Layer"))
    b.append(p(
        "The session layer provides for a higher level of control and management of network usage "
        "and data flow than that provided at lower layers, including opening or building up a "
        "communication channel, maintaining the channel, and closing the channel. This layer is "
        "infrequently implemented in contemporary systems."))

    b.append(h3("Presentation Layer"))
    b.append(p(
        "The presentation layer provides functions to transform data from formats that are "
        "transportable by the network to the user-accessible formats that are defined in the "
        "application layer and understood in the local station."))

    b.append(h3("Application Layer"))
    b.append(p(
        "The application layer, or layer 7, provides communication services directly to the user "
        "application. The usage and formatting of these services is summarized in the application "
        "layer protocol. The user interacts with the network by invoking functions and services "
        "provided by the application layer and passing data to and from the network through these "
        "services."))

    # ------------------------------------------------------------ 88.3
    b.append(h2("88.3 Network Technologies"))
    b.append(p(
        "There is a wide range of technologies in various stages of development and "
        "standardization, which address virtually all levels or layers of the ISO/OSI network "
        "reference model. One or more of the available technologies will probably suit almost any "
        "networking need. An analysis of the available technologies and their limitations will "
        "also be beneficial if it is deemed that a networking method must be designed to meet a "
        "particular application. The selection and description of technologies is by no means "
        "complete or exhaustive. The technologies presented are selected from several industries "
        "which make common use of networking to communicate sensor data. Figure 88.4 provides a "
        "comparison of selected parameters for a set of networks."))

    b.append(h3("RS-232"))
    b.append(p(
        "RS-232 (ANSI/EIA/TIA-232-E-91) is a widely used method of communication, which has been "
        "standardized in a variety of places including the Electronics Industry Association [3]. "
        "RS-232 represents elements of layer 1 of the OSI model, for communicating between two "
        "(and only two) stations. RS-232 provides a separate wire for transmission of data in each "
        "direction between the two stations, and gives the two stations different designations — "
        "data terminal equipment (DTE), and data communications equipment (DCE) — so that a "
        "method exists to distinguish which station will use which wire to transmit and receive. "
        "The signal levels for RS-232 represent a digital 1 bit as a voltage in the range of 5 to "
        "12 V on the wire, and a digital 0 bit as a voltage of negative 5 to 12 V on the wire. "
        "RS-232 is typically implemented in a full duplex fashion, since each station can "
        "transmit to the other simultaneously using separate wires. RS-232 can be made to operate "
        "at a variety of bit rates, but typically is used at bit rates from 300 bit/s up to "
        "115,200 bit/s."))

    b.append(h3("RS-485"))
    b.append(p(
        "EIA RS-485 was made a standard in 1983, derived from the RS-422 standard. RS-485 provides "
        "for differential transmission of data on a pair of wires among 32 or more stations. Like "
        "RS-232, the standard is a layer 1 specification. RS-485 provides for half duplex "
        "communication, since a station cannot simultaneously transmit and receive independent "
        "data streams. Each station in an RS-485 system can have either a transmitter or a "
        "receiver, or both (commonly called a transceiver). Most implementations provide a "
        "transceiver. When one transceiver is transmitting, all others should be receiving (i.e., "
        "not transmitting). Which station is allowed to transmit at which time is not specified "
        "in the standard, and must be covered by a higher layer protocol (e.g., Interbus-S, "
        "Profibus-DP). Figure 88.3 shows a sample RS-485 waveform, indicating the differential "
        "nature of the signaling."))
    b.append(fig(3, "en"))

    b.append(h3("Seriplex"))
    b.append(p(
        "Seriplex® is a digital, serial multiplexing system developed by Automated Process "
        "Control, Inc., in Jackson, MS. Square D Corporation purchased Automated Process Control "
        "and the rights to Seriplex in 1995, and subsequently launched Seriplex Technology "
        "Organization (STO) to manage the protocol. Seriplex is designed to be particularly "
        "efficient at handling large numbers of digital or on/off input and output points. "
        "Seriplex provides three communication wires, one for a clock signal, one for a data "
        "signal, and a ground reference. The system can be operated in two different modes "
        "(peer-to-peer and master–slave). In master–slave mode, one station is designated the "
        "master. The master synchronizes all data transmission among stations by driving a "
        "digital waveform on the clock line which all stations listen to and use for timing of "
        "transmit and receive operations. The master generates a repetitive pattern on the clock "
        "line which causes all stations to transmit and/or receive data on each cycle, or “scan” "
        "of the network. Each station is given an address, and uses the address along with the "
        "clock signal to determine when to drive the data line (in the case of an input point) or "
        "when to monitor the data line for valid output data (in the case of an output point). "
        "There are variations possible in implementation which allow for various clock speeds and "
        "bit rates (16, 100, and 200 kHz). Other protocol details allow for the handling of "
        "analog or multibit input and output points (by combining several bits on sequential "
        "scans together), bus fault detection, input redundancy, and communication error control "
        "using multiple scans of the network. Implementing the protocol in a sensor or other "
        "device typically requires using a Seriplex ASIC (Application Specific Integrated "
        "Circuit) which must be licensed from the STO [4]."))

    b.append(h3("AS-i"))
    b.append(p(
        "Actuator Sensor Interface, or AS-i, was developed by a consortium of primarily European "
        "companies interested in developing a low-cost, flexible method for connecting sensors "
        "and actuators at the lowest levels of industrial control systems. The system is managed "
        "by an independent worldwide organization [5]. The AS-i system provides a two-wire, "
        "nontwisted cable for interconnection of devices. Devices may draw current from the two "
        "wires (nominally at 24 V dc) for powering circuitry, and the data communications are "
        "modulated on top of the nominal dc level at a bit rate of 167 kHz, under the control of "
        "the master. A single parity bit per station is used for error detection. Similar to "
        "Seriplex, an AS-i device is typically implemented using a special ASIC which handles the "
        "communication."))

    b.append(h3("Interbus-S"))
    b.append(p(
        "Interbus-S was developed by Phoenix Contact [6] and is controlled by the Interbus-S "
        "Club. The topology of the network is a ring, with data being sequentially shifted from "
        "point to point on the ring under the control of a network master. Each device in the "
        "ring acts as a shift register, transmitting and receiving data simultaneously at "
        "500 kHz. The actual serial data transmission between stations conforms to RS-485. "
        "Interbus-S transmissions include a CRC for error detection. Interbus-S (Interbus-S "
        "Remote Bus) has also been extended to include a subprotocol called Interbus-Sensor Loop "
        "(or Interbus-S Local Bus). This subprotocol provides an alternate physical layer, with a "
        "single twisted pair carrying power and data on the same lines, and a reduction in the "
        "minimum size of the shift register in each station from 16 to 4 bits. Each Interbus "
        "sensor loop system can act as a single station on an Interbus-S network, or the sensor "
        "loop can be connected directly to a controller or master. Interbus-S devices are usually "
        "implemented with a special ASIC."))
    b.append(fig(4, "en"))

    b.append(h3("CAN"))
    b.append(p(
        "Controller Area Network (CAN) is a data link layer (layer 2) network technology "
        "developed by Robert Bosch Corporation [7], with an application target of onboard "
        "automotive networking. The technology is standardized in ISO 11898 [8], licensed to all "
        "major integrated circuit manufacturers, and is widely available — both as separate CAN "
        "controllers as well as CAN controllers integrated with microprocessors. As a result, CAN "
        "has been used in a variety of industries. As a data link layer technology, it is not a "
        "complete network definition. A number of physical layer options are usable with CAN "
        "(e.g., twisted pair, fiber optic, radio frequency wireless) and some have been subject "
        "to standardization (e.g., ISO 11898). Also, a number of application layer protocols have "
        "been developed for use with CAN, such as DeviceNet, Smart Distributed System (SDS), "
        "CANOpen [9], and SAE J1939 [10]. Both DeviceNet [11] and Smart Distributed System [12] "
        "have developed systems for creating networks of industrial field devices for the factory "
        "floor, including sensors and actuators."))

    b.append(h3("4 to 20 mA Current Loop"))
    b.append(p(
        "The 4 to 20 mA current loop is a widely used method for transferring information from "
        "one station (the transmitter) to another station (the receiver). Therefore, this system "
        "allows for only two stations. A typical current loop system assigns a sensing range "
        "(e.g., 0 to 100 °C) to the current range between 4 and 20 mA. A loop exists (i.e., two "
        "wires) between the transmitter and receiver. The transmitter can impress a certain "
        "current in the loop (using a controlled current source) so that the receiver can measure "
        "the current in the loop (e.g., by placing a small resistor in series with the loop and "
        "measuring the voltage drop across the resistor). After measuring the current, the "
        "receiver can then determine the present level of the sensed signal within the defined "
        "sensing range. This method uses current signaling, instead of voltage signaling, and "
        "therefore is relatively unaffected by potential differences between the transmitter and "
        "the receiver. This is similar to the benefit of differential (voltage) signaling, which "
        "also requires two wires. Another characteristic of this method is that it is not "
        "primarily digital in nature, as many other sensor communication systems are. The "
        "measured value can vary continuously in the range of 4 to 20 mA, and therefore can "
        "easily represent an analog sensing range, rather than a set of digital signals. Also, "
        "the signal is continuously variable and available. Another characteristic of this method "
        "is that the integrity of the loop can be verified. As long as the loop is unbroken and "
        "the transmitter is in good working order, the current in the loop should never fall "
        "below 4 mA. If the current approaches 0 mA, then the receiver can determine that a fault "
        "exists — perhaps a broken cable. These systems are widely used in various process "
        "control industries (e.g., oil refining) for connecting sensors (transmitters) with "
        "control computers. Because one station is always the transmitter and one station is "
        "always the receiver, this is a unidirectional, half duplex communication system."))

    b.append(h3("HART"))
    b.append(p(
        "HART® is a protocol which builds upon 4 to 20 mA communication systems. The basic idea "
        "is that additional data (beyond the basic sensor signal being carried in the current "
        "loop) can be transmitted by modulating a signal on top of the current flowing in the "
        "loop. The actual modulation method conforms closely to the Bell 202 standard for analog "
        "modem communications on telephone lines at 1200 bit/s. Because a 4 to 20 mA current loop "
        "carries a relatively slowly varying signal, it is easy to separate the 4 to 20 mA signal "
        "from the digital signal using filters. The Bell 202 standard uses continuous-phase "
        "frequency shift keying between two frequencies at up to 1200 shifts/s to modulate "
        "digital ones and zeros onto the 4 to 20 mA current loop. This method allows for "
        "bidirectional, full duplex communication between the two stations, on top of the 4 to "
        "20 mA signal. It is also possible to configure HART communications on a network that is "
        "not carrying a 4 to 20 mA signal, in which case up to 15 devices can be connected "
        "together on the network. HART was developed by Fisher-Rosemount Corporation, and has "
        "been transferred to an independent foundation for management [13]. Because HART is "
        "compatible with U.S. telephone systems, it can theoretically be run over the telephone "
        "line and is therefore capable of running over arbitrarily long distances."))

    b.append(h3("Profibus"))
    b.append(p(
        "Profibus (PROcess FIeld BUS) is one of three networks standardized by a European "
        "standard [14]. Profibus is under the control of a global organization, PNO [15]. "
        "Profibus is an umbrella network standard which encompasses three subnetworks within the "
        "Profibus family. Profibus-DP (Distributed Periphery) is the variant which is designed "
        "specifically for communication with field devices (sensors and actuators) at the device "
        "I/O level. Profibus-PA (Process Automation) is a variant which has more capabilities "
        "designed to support the needs of device-level networking for process industries, such as "
        "oil refining. One of the capabilities of Profibus-PA is its ability to be installed in "
        "an intrinsically safe way, thus providing a higher degree of safety in environments "
        "which may be explosive or otherwise hazardous. Profibus-PA typically uses a special "
        "physical layer specification standardized under IEC 1158-2, which is used by several "
        "network systems for process automation applications. IEC 1158-2 specifies a two-wire "
        "twisted pair implementation carrying both power and data on the same two wires at "
        "31.25 kbit/s. Profibus-FMS (Fieldbus Messaging Specification) represents the highest "
        "level implementation, which is used to link together controllers (not field or I/O "
        "devices) in a factory."))
    b.append(p(
        "Profibus-DP systems are typically master–slave systems, where usually a single network "
        "master (the host controller) communicates with a number of slave devices (remote I/O "
        "blocks and other I/O devices). The protocol provides for cyclic exchange of I/O "
        "information as well as on-demand exchange of other types of information. Profibus-DP can "
        "be implemented on several different physical layers, including RS-485 and fiber optics, "
        "at various bit rates up to 12 Mbit/s. Profibus messages include a CRC for error "
        "detection."))

    b.append(h3("Foundation Fieldbus"))
    b.append(p(
        "Foundation Fieldbus (FF) is a networking standard which has grown out of an effort "
        "within industry standards organizations, especially ISA-SP50 [16], and IEC SC65C/WG6 "
        "[17], to provide a replacement for the 4 to 20 mA analog sensor communication standard. "
        "FF provides two basic levels of networking: H1 and H2. H1 is a lower-speed system that "
        "can provide intrinsically safe (IS) operation and uses a single twisted pair to deliver "
        "both power and data communications to field devices, according to IEC 1158-2. Running at "
        "a bit rate of 31.25 kbit/s, H1 is very similar to Profibus-PA, when run on the IEC "
        "1158-2 physical layer standard. The H1 system is designed to be able to connect "
        "hierarchically “upward” to an H2 system, which acts as the host. FF H2 can be run at "
        "either 1 or 2.5 Mbit/s on twisted pair wires, and also provides an IS option at the "
        "1 Mbit/s rate. The H2 system can act as a network backbone in a factory environment, "
        "carrying data among various H1 systems."))

    b.append(h3("WorldFIP"))
    b.append(p(
        "WorldFIP [18] is another technology of the three that were standardized in the European "
        "standard EN 50 170, running on the IEC 1158-2 physical layer. Many of the proponents of "
        "WorldFIP have embraced FF, and contributed to the development of that standard. WorldFIP "
        "is a member of the FF, and FF has incorporated many of the capabilities of WorldFIP as a "
        "result. When run on the IEC 1158-2 physical layer, WorldFIP has similar capabilities to "
        "FF."))

    b.append(h3("LonWorks"))
    b.append(p(
        "LonWorks® is a networking technology developed and controlled by the Echelon Corporation "
        "[19]. LonWorks is designed to be a general-purpose networking technology suitable for a "
        "variety of industries. LonWorks has been applied extensively in the building automation "
        "and control industry, as well as a variety of other industries. The core LonWorks "
        "technology for devices is contained in special integrated circuits — called Neuron® "
        "chips — which combine several microprocessors to manage the network, communications, and "
        "provide a general-purpose control environment. These chips are available from Motorola, "
        "Inc., and the Toshiba Corporation, which are licensees of the LonWorks technology. "
        "Echelon has also announced the possibility to license the LonTalk® protocol to other "
        "manufacturers for implementation in other microprocessors. LonWorks networks can be "
        "implemented on a variety of physical layers, including twisted pair at several bit rates "
        "and wireless options at 4800 bit/s, but the most common is a differential twisted pair "
        "system running at 78 kbit/s. Most of the networking details (the LonTalk protocol) are "
        "hidden from the user, and are encapsulated as functions within the general-purpose "
        "control environment. The user programs (using a language like the C programming "
        "language) the Neuron chip for each station to behave in a certain way and communicate "
        "various data items to other stations. Then, specialized tools are used to tie all of the "
        "stations together (handling addressing and other network details) to yield a functioning "
        "network. The system combines flexibility with a certain amount of ease of implementation, "
        "and can easily be applied to a variety of applications."))

    # ------------------------------------------------------------ 88.4
    b.append(h2("88.4 Applying Network Communications"))

    b.append(h3("Shielding"))
    b.append(p(
        "Many communication networks require shielding of the media (the cable). Shielding "
        "constitutes an electric conductor which completely encases the communication media "
        "(e.g., twisted pair) to provide protection against EMI. Shielding provides an electric "
        "conductive barrier to attenuate electromagnetic waves external to the shield, and "
        "provides a conduction path by which induced currents can be circulated and returned to "
        "the source, typically via a ground reference connection. Shields in communication "
        "systems are often grounded at only a single point. This single point of ground prevents "
        "the shield from participating in a “ground loop,” which is an alternative path for "
        "current to flow between two points of potential difference connected to a common ground. "
        "Ground loops can lead to noise problems, and can be destructive if the stray currents "
        "are large enough, since a shield ground is usually not constructed to carry heavy "
        "currents."))

    b.append(h3("Media"))
    b.append(p(
        "The most common media types for network systems fall into three categories: electric, "
        "optical, and electromagnetic. Electric media are based on conductors (e.g., copper "
        "wire), whereas optical media are based on optical waveguides, or fiber optics. "
        "Electromagnetic media consists of free space, or general electromagnetic "
        "wave-permeable materials, and are referred to as wireless systems. Within the category "
        "of electric media are a large variety of conductor configurations. The most common are "
        "unshielded pair, unshielded twisted pair (UTP), shielded twisted pair (STP), and coaxial "
        "(COAX). These conductor configurations have various properties which are significant for "
        "the transmission of electric signals, as well as varying degrees of immunity to EMI. As "
        "a rule of thumb, the quality of the transmission line characteristics (signal "
        "transmission and immunity to EMI) improves in the order listed. Twisted pair systems "
        "are generally easier to install, whereas coaxial and fiber-optic systems generally "
        "require more specialized tools and termination methods. Of course, wireless systems are "
        "easy to install, but attention must still be paid to the media. The characteristics of "
        "the free space such as distance and amount of EMI present must be considered for "
        "reliable operation of the network."))

    b.append(h3("Bit Rate"))
    b.append(p(
        "Some networks provide only one choice of bit rate, whereas others provide "
        "user-selectable options for bit rate. Bit-rate options may be dependent on the type of "
        "media that is installed. As a rule of thumb, the bit rate chosen should be the lowest "
        "possible bit rate that still supports the application requirements for speed of data "
        "transfer and overall bandwidth. This generally results in more reliable operation, and "
        "generally gives the network more immunity to minor degradations, specification "
        "violations, and EMI."))

    b.append(h3("Topologies"))
    b.append(p(
        "There are a variety of network topologies that are commonly used. Topology refers to the "
        "physical arrangement and interconnection of stations by the media. Some networks can be "
        "run using several different topologies; some can only be run with a certain topology "
        "(e.g., Interbus-S requires a ring topology). The most common topologies are daisychain, "
        "trunkline–branchline, ring, and star. Variations on these exist, and networks that "
        "incorporate or can be run on highly varied topologies are sometimes called free-form, "
        "tree, or free topology networks. Figure 88.5 depicts graphically several different types "
        "of topologies. In some cases, networks require certain topologies. Deviating from these "
        "can cause degradation in network behavior (e.g., corruption of messages) or network "
        "failure."))
    b.append(fig(5, "en"))

    b.append(h3("Configuration"))
    b.append(p(
        "Most networks involve some sort of configuration. Configuration is the process of "
        "connecting stations together and assigning certain programmable parameters to each "
        "station required for proper operation of the network. The most common configurable "
        "parameter in many networks is the station address. Some networks may require other "
        "parameters to be preset, such as the communication speed, or bit rate. Some networks "
        "have the capability to autoconfigure, which means to assign parameters automatically to "
        "stations as part of the network start-up process, without explicit user intervention "
        "(e.g., Interbus-S). Many networks define various tools, which may be computer based, to "
        "assign parameters to each station in order to configure the network. In other cases, the "
        "stations may incorporate switches or other manual means to configure the necessary "
        "parameters for network operation."))

    # ------------------------------------------------------------ 88.5
    b.append(h2("88.5 Advanced Topics"))

    b.append(h3("Wireless Technologies"))
    b.append(p(
        "The need for networking is present even in environments where an electrical or optical "
        "cable cannot be easily distributed. This may be due to various limitations, such as "
        "difficulty in running a new cable from one building to another, or connecting to sensors "
        "in motion or on vehicles. There are two general categories of wireless communications, "
        "based on electromagnetic frequency spectra. Various wireless technologies employ the "
        "infrared spectrum. These technologies generally have transmission limited to "
        "applications that have a direct line of sight between stations. Also, the distances are "
        "generally limited to 100 m or less. Because of these limitations, there are generally no "
        "legal restrictions in employing these frequency spectra, and infrared transceivers are "
        "now becoming available from a variety of manufacturers."))
    b.append(p(
        "The other general category of wireless communications is based on radio frequency (RF) "
        "communications. In most countries, use of these spectra is tightly controlled by "
        "governmental agencies. As a result, employing wireless networking in most of these "
        "frequency ranges requires special licensing. However, a number of frequency ranges are "
        "reserved for low-power public communications. Within these frequency ranges, devices are "
        "allowed to communicate in an unlicensed fashion as long as they transmit according to "
        "certain rules about transmitted power output. RF-based wireless systems are generally not "
        "limited to line-of-sight applications, and can be designed to cover greater distances "
        "than infrared-based systems."))
    b.append(p(
        "Wireless technologies can be viewed as simply another choice for the physical layer "
        "media, i.e., free space. As such, it is possible to consider, in some cases, a wireless "
        "media for implementation of a variety of protocols. For example, both CAN and LonWorks "
        "systems could be candidates for wireless networking."))

    b.append(h3("Fiber Optics"))
    b.append(p(
        "Another physical layer media choice is fiber-optic media. Fiber-optic media employs "
        "pulses of light delivered along a tubular waveguide (glass or plastic fiber) to transmit "
        "information from one station to another. Fiber optics enjoy some benefits over "
        "traditional copper wiring. First, attenuation of light within fiber optics is generally "
        "about an order of magnitude less than attenuation of an electric signal within a copper "
        "wire. Second, fiber-optic transmission systems can be modulated (or pulsed) at much "
        "higher frequencies, yielding greater potential bandwidths and bit rates than copper "
        "media. Finally, fiber-optic systems are generally immune to the traditional sources of "
        "EMI that can cause trouble for copper media systems. There are also limitations in "
        "present implementations of fiber-optic systems. One of the limitations is that special "
        "tools and termination techniques must be used to connect a fiber-optic cable to a sensor "
        "or field device. Second, fiber-optic “taps” are not easily created. Therefore, most "
        "fiber-optic systems are implemented in a point-to-point fashion. When multiple devices "
        "are involved in a network, each device usually acts as an optical repeater, with a "
        "fiber-optic input and a fiber-optic output port."))

    b.append(h3("Network Design Considerations"))
    b.append(p(
        "Designing a network communication system from the ground up can be a lengthy "
        "undertaking, and should not be considered unless a careful review of available "
        "technologies has yielded no solutions to the particular requirements of the application. "
        "The designers must take into account a number of fundamental questions to shape the "
        "capability of the network. One topic mentioned frequently in the area of networking for "
        "control applications is the subject of determinism. This refers to the ability of the "
        "network to behave in a predictable fashion under any given set of stimuli, or external "
        "conditions. Many networks do not exhibit this characteristic. Another question to be "
        "resolved is the subject of priority, and media access. The designers must determine the "
        "conditions under which any particular station is allowed to transmit, and if multiple "
        "stations are attempting to transmit, how it will be determined which station will be "
        "given priority to transmit first. Media access methods often impact the ability of a "
        "network to behave in a deterministic fashion."))

    b.append(h3("Integrating Sensors with Communications — IEEE P1451"))
    b.append(p(
        "A recent interesting development in the area of sensor networks is an effort being "
        "sponsored by the IEEE [20] out of its TC-9 committee, called IEEE P1451. This activity "
        "is working toward the development of a standard to define sensor (or transducer) "
        "interfaces to networks generically. The first part of the proposed standard, IEEE "
        "P1451.1, includes definitions for the interface between the device and the network "
        "(refer to Figure 88.1). The second part, IEEE P1451.2, includes definitions for the "
        "interface between the transducer (or sensor) and the network interface block within the "
        "device. P1451.2 includes a definition for a transducer electronic data sheet, or TEDS, "
        "which defines a summary set of information pertinent to the sensor, allowing for "
        "standardized exchange of data on the network. The proposed standard has the potential "
        "benefits to make it easier to connect a sensor to a variety of networks, and to allow "
        "similar sensors from different manufacturers to be handled in a similar fashion on the "
        "network."))

    b.append(h2("Chapter 88 terminology"))
    b.append(note(
        "Added by the translator; this section is not in the original. It gathers the terms that "
        "chapter 88 itself defines across 88.2 into one table for reference while reading. The "
        "definitions keep the original’s content and only compress the wording."))
    b.append(_glossary(_GLOSS_EN))

    b.append(h2("References"))
    b.append(refs(_REFS))

    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER_EN))
    return "".join(b)


# ================================================================ PAGE
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 88 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 88 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 88 “Mạng cảm biến và truyền thông” của Robert M. "
            "Crovella — vì sao dùng cảm biến có mạng, các khái niệm truyền thông và mạng, mô "
            "hình bảy tầng OSI, mười hai công nghệ mạng từ RS-232 tới LonWorks, rồi cách áp "
            "dụng, với 5 hình, 1 bảng và 20 tài liệu tham khảo." if vi
            else
            "Companion to Chapter 88 of the CRC Measurement Handbook — why networked sensors, "
            "the concepts of communication and networking, the seven-layer OSI model, twelve "
            "network technologies from RS-232 to LonWorks, and how to apply them, with 5 figures, "
            "1 table and 20 references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 88' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 88' % BASE_EN)
    meta = ("Chương 88 · theo Ch88.pdf (CRC Press, 1999) · 5 hình, 1 bảng, 1 công thức" if vi
            else "Chapter 88 · 5 figures, 1 table, 1 equation")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 88)))
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
