# -*- coding: utf-8 -*-
"""Handbook Chapter 3 — Static and Dynamic Characteristics of Instrumentation.

Writes the full Vietnamese translation and the English figure companion.
Run:  python build/reader_hb_ch03.py
"""
import os

import hbfig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch03-static-and-dynamic-characteristics-of-instrumentation"
TITLE_EN = "Static and Dynamic Characteristics of Instrumentation"
TITLE_VI = "Đặc tính tĩnh và động của thiết bị đo"
BYLINE = "Peter H. Sydenham · University of South Australia"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi", anchor=True):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-3-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


# ------------------------------------------------------------------ VI body
def body_vi():
    b = []
    b.append('<div class="note"><b>Thuật ngữ chính.</b> '
             '<em>Đại lượng đo (measurand)</em> · <em>Độ phân giải (discrimination)</em> · '
             '<em>Độ chụm (precision)</em> · <em>Độ lặp lại (repeatability)</em> · '
             '<em>Độ tái lập (reproducibility)</em> · <em>Độ chính xác (accuracy)</em> · '
             '<em>Hàm truyền (transfer function)</em> · <em>Độ nhạy (sensitivity)</em> · '
             '<em>Độ trôi (drift)</em> · <em>Trễ (hysteresis)</em> · <em>Khe hở (backlash)</em> · '
             '<em>Bão hoà (saturation)</em> · <em>Bias</em> · <em>Sai số phi tuyến</em> · '
             '<em>Hàm kích thích (forcing function)</em> · <em>Hằng số thời gian (τ)</em> · '
             '<em>Tỉ số tắt dần (ζ)</em> · <em>Tần số riêng (ωₙ)</em> · '
             '<em>Hiệu chuẩn (calibration)</em>. '
             'Tiêu đề mỗi mục giữ kèm tên tiếng Anh để đối chiếu với bản gốc.</div>')

    b.append('<p class="lead">Chương này đặt nền cho mọi chương sau: một phép đo chỉ có nghĩa khi ta biết '
             'thiết bị đo trả lời thế nào ở trạng thái tĩnh (độ nhạy, offset, trôi, trễ, bão hoà, phi tuyến) '
             'và ở trạng thái động (bậc zero, bậc một, bậc hai, hằng số thời gian, tắt dần, cộng hưởng). '
             'Ba khái niệm hay bị dùng lẫn — độ phân giải, độ chụm và độ chính xác — được tách rõ ngay từ đầu, '
             'và chương kết thúc bằng hiệu chuẩn, cầu nối giữa lý thuyết và con số tin được.</p>')

    b.append(h2("Dẫn nhập", "Introduction"))
    b.append(p("Trước khi có thể đi sâu vào đặc tính tĩnh và đặc tính biến đổi theo thời gian của phép đo, "
               "cần dựng một khung để hiểu quá trình liên quan, đồng thời xác lập những từ chính dùng để mô tả "
               "các khái niệm khi ta đi tiếp."))
    b.append(p("<b>Đo lường</b> (measurement) là quá trình diễn giải thông tin có liên quan về một hệ quan tâm, "
               "dựa trên năng lực tư duy của con người để xác định cái được coi là kiến thức mới thu được. "
               "Thông tin này có thể nhằm điều khiển hành vi của hệ (như trong ứng dụng kỹ thuật) hoặc nhằm "
               "hiểu thêm về hệ (như trong nghiên cứu khoa học)."))
    b.append(p("Đơn vị cơ bản cần để tạo ra kiến thức gọi là <b>dữ liệu</b> (data), thu được nhờ những cụm vật lý "
               "gọi là <b>cảm biến</b> (sensor) dùng để quan sát hay cảm nhận các biến của hệ. Hai từ "
               "<em>thông tin</em> và <em>kiến thức</em> thường được dùng thay nhau để chỉ thực thể có được sau khi "
               "dữ liệu từ một hay nhiều cảm biến đã được xử lý thành hiểu biết có ý nghĩa hơn. Từng biến được "
               "cảm nhận gọi là <b>đại lượng đo</b> (measurand)."))
    b.append(p("Cách quan sát rõ ràng nhất là dùng các giác quan của con người: nhìn, sờ, nghe. Cách này thường "
               "đủ hoặc có khi là cách duy nhất. Tuy nhiên trong nhiều trường hợp người ta dùng cảm biến do con "
               "người tạo ra để tăng cường hay thay thế các giác quan tự nhiên. Số lượng và chủng loại cảm biến "
               "thực sự rất lớn. Ví dụ cảm biến nhân tạo là những cảm biến dùng để đo nhiệt độ, áp suất hay chiều "
               "dài. Quá trình cảm nhận thường được gọi là <b>chuyển đổi</b> (transduction), thực hiện bằng "
               "<b>bộ chuyển đổi</b> (transducer). Những cụm cảm biến nhân tạo này, khi được ghép với phương tiện "
               "xử lý dữ liệu thành kiến thức, thường được gọi là <b>thiết bị đo</b> (measuring instrumentation)."))
    b.append(p("Mức độ hoàn hảo của một phép đo chỉ có thể xác định nếu mục tiêu của phép đo được định nghĩa "
               "không sai lệch. Hơn nữa, không thể chế tạo thiết bị đo hoạt động hoàn hảo. Chỉ với hai lý do đó, "
               "thiết bị đo không thể cho đặc tính cảm nhận lý tưởng và phải được chọn cho phù hợp với sai số "
               "cho phép trong từng tình huống cụ thể."))
    b.append(p("Đo lường là quá trình ánh xạ các biến đang thực sự xảy ra thành các giá trị tương đương. Sai lệch "
               "so với ánh xạ hoàn hảo gọi là <b>sai số</b> (error): kết quả ta nhận được không đúng chính xác "
               "bằng cái đang được đo. Một lượng sai số nhất định là chấp nhận được miễn là nó dưới mức không "
               "đảm bảo mà ta có thể chấp nhận trong tình huống cụ thể."))
    b.append(p("Ví dụ, xét hai nhu cầu khác nhau khi đo đại lượng thời gian. Để đi họp đúng giờ, độ không đảm bảo "
               "cần thiết khoảng 1 phút trong 24 giờ. Trong điều khiển vệ tinh quỹ đạo, độ không đảm bảo về thời "
               "gian phải nhỏ tới mili giây trong nhiều năm. Thiết bị cho trường hợp đầu giá vài đô-la và chính là "
               "chiếc đồng hồ ta đeo; thiết bị cho trường hợp sau giá hàng nghìn đô-la và to bằng một chiếc va-li."))
    b.append(p("Ta thường ghi các giá trị đại lượng đo như thể chúng là những thực thể không đổi, nhưng chúng "
               "thường thay đổi giá trị khi thời gian trôi. Những biến thiên “động” này xảy ra hoặc do chính đại "
               "lượng đo thay đổi, hoặc do thiết bị đo cần thời gian để bám theo thay đổi của đại lượng đo — khi đó "
               "nó có thể đưa vào một sai số không chấp nhận được."))
    b.append(p("Ví dụ, khi dùng nhiệt kế đo thân nhiệt một người, ta muốn biết người đó có ở giá trị thường được "
               "mong đợi không, và nếu không thì tìm các thay đổi theo thời gian như dấu hiệu về sức khoẻ. "
               "Hình 3-1 cho thấy biểu đồ nhiệt độ của một bệnh nhân. Rõ ràng nếu nhiệt kế cho sai số khi dùng thì "
               "có thể đi đến kết luận sai. Sai số có thể do nhiệt kế được hiệu chuẩn không đúng, hoặc do không "
               "tính đến đáp ứng động của chính nhiệt kế."))
    b.append(fig(1, hbfig.fig_3_1()))
    b.append(p("Vì vậy, thiết bị đo chỉ cho thông tin đủ đúng nếu ta hiểu các đặc tính tĩnh và động của cả đại "
               "lượng đo lẫn thiết bị đo. Đến lượt mình, điều đó cho phép ta quyết định xem sai số phát sinh có đủ "
               "nhỏ để chấp nhận hay không."))
    b.append(p("Ví dụ, xét một bộ khuếch đại tín hiệu trong một hệ âm thanh. Người ta thường công bố nó có hệ số "
               "khuếch đại sau phản hồi, khi áp vào bộ khuếch đại cơ bản, chẳng hạn bằng 10. Giá trị khuếch đại "
               "thực tế phụ thuộc tần số của tín hiệu vào, thường giảm khi tần số tăng. Đáp ứng tần số của bộ "
               "khuếch đại cơ bản — trước khi được cấu hình với phản hồi, thứ làm thay đổi rõ rệt đáp ứng và hạ hệ "
               "số khuếch đại để có hoạt động ổn định — được biểu diễn bằng đồ thị hệ số khuếch đại theo tần số "
               "vào. Hình 3-2 cho một ví dụ về hệ số khuếch đại vòng hở của bộ khuếch đại cơ bản. Việc không có hệ "
               "số khuếch đại đồng đều trên cả dải tần gây ra sai số — đầu ra âm thanh không còn là biểu diễn đủ "
               "trung thực của đầu vào."))
    b.append(fig(2, hbfig.fig_3_2()))

    b.append(h2("Ba khái niệm phải tách rời", "Discrimination, Precision, Accuracy"))
    b.append(p("Trước khi đi sâu hơn vào đặc tính tĩnh và động của thiết bị đo, cần hiểu sự khác nhau về nghĩa "
               "giữa một số thuật ngữ cơ bản dùng để mô tả kết quả của hoạt động đo."))
    b.append(p("Những thuật ngữ đúng được quy định trong các tài liệu gọi là tiêu chuẩn. Có nhiều bộ thuật ngữ đo "
               "lường đã được tiêu chuẩn hoá nhưng chúng không thống nhất với nhau. Sẽ thấy rằng sách về thiết bị "
               "đo và các bản công bố đặc tính thiết bị thường dùng thuật ngữ theo những cách khác nhau. Người "
               "dùng thông tin đo cần luôn cẩn trọng để chắc rằng các phát biểu được hiểu đúng."))
    b.append(p("Ba khái niệm đồng hành về một phép đo cần hiểu rõ là <b>độ phân giải</b> (discrimination), "
               "<b>độ chụm</b> (precision) và <b>độ chính xác</b> (accuracy). Ba từ này thường bị dùng lẫn cho "
               "nhau — điều hoàn toàn sai, vì chúng bao hàm những khái niệm rất khác nhau, như sẽ được giải thích "
               "dưới đây."))
    b.append(p("Khi thực hiện một phép đo, gia số nhỏ nhất có thể phân biệt được gọi là <b>độ phân giải</b> "
               "(discrimination). (Dù hiện nay được tuyên bố chính thức là dùng sai, thuật ngữ <em>resolution</em> "
               "vẫn xuất hiện trong sách và báo cáo với nghĩa discrimination.) Cần biết độ phân giải của một phép "
               "đo vì nó cho biết quá trình cảm nhận có đủ mịn để phát hiện những thay đổi nhỏ của đại lượng đo hay "
               "không."))
    b.append(p("Dù độ phân giải đạt yêu cầu, giá trị nhận được khi lặp lại một phép đo hiếm khi giống hệt nhau mỗi "
               "lần đo trong điều kiện đại lượng đo không đổi. Đó là vì trong hệ thực luôn phát sinh sai số. Độ tản "
               "mát của tập giá trị nhận được cho biết <b>độ chụm</b> của tập phép đo. Từ <em>precision</em> không "
               "phải là từ mô tả một phẩm chất của phép đo và bị dùng sai theo nghĩa đó. Hai thuật ngữ nên dùng ở "
               "đây là: <b>độ lặp lại</b> (repeatability), mô tả biến thiên của một tập phép đo thực hiện trong "
               "khoảng thời gian rất ngắn; và <b>độ tái lập</b> (reproducibility), cùng khái niệm nhưng áp dụng cho "
               "các phép đo thực hiện trong khoảng thời gian dài. Vì các thuật ngữ này mô tả kết quả của một tập "
               "giá trị, cần nêu được một giá trị duy nhất mô tả kết quả tổng thể của tập. Việc này được làm bằng "
               "phương pháp thống kê, cho phép tính “giá trị trung bình” của tập và độ tản mát kèm theo, gọi là "
               "<b>phương sai</b> (variance)."))
    b.append(p("<b>Độ chính xác</b> (accuracy) của một phép đo được trình bày sâu hơn ở phần khác nên ở đây chỉ "
               "cần giới thiệu. Độ chính xác là mức độ gần nhau giữa một phép đo và giá trị được định nghĩa là giá "
               "trị thật. Khái niệm này sẽ rõ hơn khi xét ví dụ minh hoạ dưới đây, vì ví dụ gộp cả ba thuật ngữ vào "
               "một góc nhìn duy nhất về một phép đo điển hình."))
    b.append(p("Xét tình huống một xạ thủ bắn tên vào bia như Hình 3-3(a). Bia có một điểm giữa — hồng tâm. Mục "
               "tiêu của một kết quả hoàn hảo là đưa mọi mũi tên vào hồng tâm. Các vòng quanh hồng tâm cho phép ta "
               "lập các thước đo số cho thành tích bắn kém hoàn hảo hơn."))
    b.append(p("<b>Độ phân giải</b> là khoảng cách mà tại đó ta vừa có thể phân biệt vị trí của một mũi tên với "
               "mũi khác khi chúng rất gần nhau. Với một mũi tên, chính độ dày của lỗ đâm quyết định độ phân giải. "
               "Hai vị trí gần nhau của hai mũi tên trong Hình 3-3(a) không dễ tách ra. Dùng tên mảnh hơn sẽ cho "
               "phép phân biệt chi tiết mịn hơn."))
    b.append(p("<b>Độ lặp lại</b> được xác định bằng cách đo độ tản mát giá trị của một tập mũi tên bắn vào bia "
               "trong thời gian ngắn. Độ tản mát càng nhỏ thì xạ thủ càng chụm. Xạ thủ ở Hình 3-3(a) chụm hơn xạ "
               "thủ ở Hình 3-3(b)."))
    b.append(p("Nếu xạ thủ quay lại bắn mỗi ngày trong thời gian dài, kết quả có thể không giống nhau mỗi lần so "
               "với một buổi bắn ngắn. Trung bình và phương sai của các giá trị khi đó được gọi là <b>độ tái "
               "lập</b> của thành tích xạ thủ."))
    b.append(p("Còn lại là <b>độ chính xác</b>. Con số này mô tả giá trị trung bình của các phát bắn nằm ở đâu so "
               "với vị trí hồng tâm. Tập ở Hình 3-3(b) chính xác hơn tập ở Hình 3-3(a) vì trung bình gần hồng tâm "
               "hơn (nhưng kém chụm hơn!)."))
    b.append(p("Thoạt nhìn có thể tưởng ba khái niệm độ phân giải, độ chụm và độ chính xác có quan hệ chặt với "
               "nhau theo nghĩa một phép đo tốt hơn luôn là phép đo có cả ba khía cạnh cao nhất trong khả năng chi "
               "phí. Không phải vậy. Chúng cần được đặt cho phù hợp với yêu cầu của ứng dụng."))
    b.append(p("Giờ ta đã có thể khảo sát những thuật ngữ thường gặp dùng để mô tả các khía cạnh của đặc tính tĩnh "
               "và động của thiết bị đo."))
    b.append(fig(3, hbfig.fig_3_3()))

    # ---------------------------------------------------------------- 3.1
    b.append(h2("3.1 Đặc tính tĩnh của hệ thiết bị đo", "Static Characteristics of Instrument Systems"))
    b.append(h3("Quan hệ vào/ra", "Output/Input Relationship"))
    b.append(p("Hệ thiết bị đo thường được xây từ sự nối tiếp các khối chức năng phân biệt được. Cụm vật lý thực "
               "tế có thể không trông như vậy nhưng có thể phân tách thành một sơ đồ đại diện gồm các khối nối với "
               "nhau. Hình 3-4 là sơ đồ khối của một cảm biến độ ẩm. Cảm biến được kích hoạt bởi một tham số vật lý "
               "vào và cung cấp tín hiệu ra cho khối tiếp theo, khối này xử lý tín hiệu thành trạng thái thích hợp "
               "hơn."))
    b.append(fig(4, hbfig.fig_3_4()))
    b.append(p("Do đó một thực thể chung then chốt là quan hệ giữa đầu vào và đầu ra của khối. Như đã nêu, mọi tín "
               "hiệu đều có đặc tính thời gian, nên phải xét hành vi của khối theo cả trạng thái tĩnh và trạng thái "
               "động."))
    b.append(p("Hành vi của riêng chế độ tĩnh và của chế độ tĩnh–động kết hợp có thể tìm được nhờ một mô hình toán "
               "học thích hợp cho mỗi khối. Mô tả toán học đáp ứng hệ dễ lập và dễ dùng nếu mọi phần tử đều hành xử "
               "như hệ tuyến tính và phép cộng tín hiệu có thể thực hiện theo cách cộng tuyến tính. Nếu tồn tại phi "
               "tuyến trong các phần tử thì việc đưa ra một giải thích toán học dễ theo dõi trở nên khó hơn nhiều — "
               "có khi hoàn toàn không thực tế. May thay, mô tả tổng quát đáp ứng của hệ thiết bị đo thường có thể "
               "được bao quát đầy đủ bằng cách xử lý tuyến tính."))
    b.append(p("Tỷ số ra/vào của toàn bộ chuỗi khối nối tiếp 1, 2, 3, … được cho bởi:"))
    b.append(eq("[ra/vào]<sub>tổng</sub> = [ra/vào]<sub>1</sub> × [ra/vào]<sub>2</sub> × "
                "[ra/vào]<sub>3</sub> …", ""))
    b.append(p("Tỷ số ra/vào của một khối bao gồm cả đặc tính tĩnh và động được gọi là <b>hàm truyền</b> "
               "(transfer function) và được ký hiệu <i>G</i>."))
    b.append(p("Phương trình của <i>G</i> có thể viết thành hai phần nhân với nhau. Một phần biểu diễn hành vi tĩnh "
               "của khối, tức giá trị của nó sau khi mọi hiệu ứng quá độ (biến thiên theo thời gian) đã ổn định về "
               "trạng thái cuối. Phần kia cho biết giá trị đó đáp ứng thế nào khi khối ở trạng thái động. Phần tĩnh "
               "được gọi là <b>đặc tính truyền</b> (transfer characteristic) và thường là tất cả những gì cần biết "
               "để mô tả khối."))
    b.append(p("Đáp ứng tĩnh và động của chuỗi khối đơn giản là tích của tất cả các khối riêng lẻ. Vì mỗi khối có "
               "phần tĩnh và phần động riêng, các phương trình chuỗi có thể được sắp xếp lại để tách phần tĩnh khỏi "
               "phần động, rồi nhân tập tĩnh với tập động ta được đáp ứng tổng thể ở trạng thái tĩnh và động. Điều "
               "này được thể hiện qua chuỗi phương trình 3.1 đến 3.4."))
    b.append(eq("G<sub>tổng</sub> = G<sub>1</sub> × G<sub>2</sub> × G<sub>3</sub> …", "3.1"))
    b.append(eq("= [tĩnh × động]<sub>1</sub> × [tĩnh × động]<sub>2</sub> × [tĩnh × động]<sub>3</sub> …", "3.2"))
    b.append(eq("= [tĩnh]<sub>1</sub> × [tĩnh]<sub>2</sub> × [tĩnh]<sub>3</sub> … × [động]<sub>1</sub> × "
                "[động]<sub>2</sub> × [động]<sub>3</sub> …", "3.3"))
    b.append(eq("= [tĩnh]<sub>tổng</sub> × [động]<sub>tổng</sub>", "3.4"))
    b.append(p("Một ví dụ sẽ làm rõ điều này. Một nhiệt kế thuỷ ngân trong ống thuỷ tinh được đặt vào miệng bệnh "
               "nhân. Chỉ thị từ từ dâng dọc ống thuỷ tinh để đạt giá trị cuối là thân nhiệt của người đó. Sự dâng "
               "chậm này do thuỷ ngân cần thời gian để nóng lên và giãn nở trong ống. <b>Độ nhạy tĩnh</b> được "
               "biểu diễn bằng số vạch chia trên một độ và đó là tất cả những gì quan tâm trong ứng dụng này. "
               "<b>Đặc tính động</b> là một hàm biến thiên theo thời gian, ổn định về 1 sau khi hiệu ứng quá độ qua "
               "đi. Trong ứng dụng này đó chỉ là điều phiền toái nhưng phải được tính đến bằng cách chờ đủ lâu "
               "trước khi đọc. Sẽ đọc phải giá trị sai nếu đọc trước khi quá độ ổn định."))
    b.append(p("Ở đây ta chỉ xét bản chất của đặc tính tĩnh của một chuỗi; đáp ứng động được xét sau."))
    b.append(p("Nếu cảm biến là tầng đầu của chuỗi, giá trị tĩnh của độ lợi ở tầng đó gọi là <b>độ nhạy</b> "
               "(sensitivity). Khi cảm biến không ở đầu vào, nó được gọi là <b>hệ số khuếch đại</b> hay "
               "<b>độ lợi</b> (gain). Nó có thể nhận giá trị nhỏ hơn 1, khi đó gọi là <b>suy giảm</b> (attenuation)."))
    b.append(p("Đôi khi giá trị tức thời của tín hiệu thay đổi nhanh, nhưng khía cạnh đo lường lại là tĩnh. Điều "
               "này xảy ra khi dùng tín hiệu xoay chiều trong một số dạng thiết bị đo, nơi biên độ của dạng sóng — "
               "chứ không phải tần số — là đại lượng quan tâm. Ở đây giá trị tĩnh được gọi là <b>đặc tính truyền ở "
               "trạng thái xác lập</b> (steady state transfer characteristic)."))
    b.append(p("Độ nhạy có thể tìm từ đồ thị tín hiệu vào và ra, trong đó nó là độ dốc của đồ thị. Đồ thị như vậy, "
               "xem Hình 3-5, cho biết nhiều điều về hành vi tĩnh của khối."))
    b.append(fig(5, hbfig.fig_3_5()))
    b.append(p("Giá trị cắt trên trục <i>y</i> là <b>giá trị lệch</b> (offset), tức đầu ra khi đầu vào được đặt "
               "bằng zero. Offset thường không phải là tình huống mong muốn và được xem là một đại lượng sai số. "
               "Khi nó được đặt một cách có chủ ý, nó được gọi là <b>bias</b>."))
    b.append(p("Dải trên trục <i>x</i>, từ zero đến một giá trị cực đại an toàn khi dùng, được gọi là <b>dải</b> "
               "(range) hay <b>span</b> và thường được biểu diễn bằng vùng giữa điểm 0 % và 100 %. Tỷ số giữa span "
               "mà đầu ra sẽ bao phủ với dải đầu vào tương ứng được gọi là <b>dải động</b> (dynamic range). Đây có "
               "thể là thuật ngữ dễ gây nhầm vì nó không mô tả hành vi động theo thời gian. Nó đặc biệt hữu ích khi "
               "mô tả năng lực của những thiết bị như cảm biến lưu lượng — một tấm orifice đơn giản chỉ có thể xử "
               "lý dải động 3 đến 4, trong khi phương pháp laser Doppler bao được tới 10<sup>7</sup>."))

    b.append(h3("Trôi", "Drift"))
    b.append(p("Giờ cần xét một vấn đề lớn của đặc tính thiết bị đo: <b>độ trôi</b> (instrument drift). Nó do các "
               "biến đổi xảy ra trong các bộ phận của thiết bị theo thời gian. Nguồn chính là thay đổi cấu trúc hoá "
               "học và thay đổi ứng suất cơ học. Trôi là hiện tượng phức tạp mà hiệu ứng quan sát được là độ nhạy "
               "và giá trị offset thay đổi. Nó cũng có thể làm thay đổi độ chính xác của thiết bị khác nhau ở các "
               "biên độ tín hiệu khác nhau."))
    b.append(p("Mô tả chi tiết về trôi không hề dễ, nhưng có thể làm việc thoả đáng với các giá trị đơn giản hoá, "
               "lấy trung bình của một tập quan sát, thường được công bố theo cách bảo thủ. Đồ thị (a) trong "
               "Hình 3-6 cho thấy trôi ổn định điển hình của một lò xo đo trong cân. Hình 3-6(b) cho thấy một bộ "
               "khuếch đại điện tử có thể ổn định thế nào sau khi bật."))
    b.append(fig(6, hbfig.fig_3_6()))
    b.append(p("Trôi cũng do biến thiên các tham số môi trường như nhiệt độ, áp suất và độ ẩm tác động lên các "
               "linh kiện. Chúng được gọi là <b>tham số ảnh hưởng</b> (influence parameters). Một ví dụ là sự thay "
               "đổi điện trở của một điện trở — điện trở này là phần tử then chốt đặt độ lợi cho một bộ khuếch đại "
               "điện tử — khi nhiệt độ làm việc thay đổi."))
    b.append(p("Đáng tiếc, hiệu ứng quan sát được của trôi do tham số ảnh hưởng thường giống với trôi theo thời "
               "gian. Việc thử nghiệm thích hợp các khối như bộ khuếch đại điện tử cho phép tách hai loại này ở một "
               "mức nào đó. Ví dụ, chỉ thay đổi nhiệt độ của bộ khuếch đại trong thời gian ngắn sẽ nhanh chóng cho "
               "thấy sự phụ thuộc nhiệt của nó."))
    b.append(p("Trôi do tham số ảnh hưởng được vẽ đồ thị gần giống trôi theo thời gian. Hình 3-6(c) cho thấy trôi "
               "của một bộ khuếch đại khi nhiệt độ thay đổi. Lưu ý nó phụ thuộc đáng kể vào nhiệt độ làm việc, hàm ý "
               "rằng các thiết kế tốt nhất được chế tạo để làm việc ở nhiệt độ mà hiệu ứng là nhỏ nhất."))
    b.append(p("Xét kỹ các nguyên nhân trôi theo thời gian và theo tham số ảnh hưởng cho thấy chúng liên quan với "
               "nhau và thường không thể tách rời. Người thiết kế thiết bị đo thường có thể bù các hiệu ứng này, "
               "nhưng chi phí làm việc đó tăng mạnh khi mức sai số có thể chấp nhận giảm."))

    b.append(h3("Trễ và khe hở", "Hysteresis and Backlash"))
    b.append(p("Quan sát kỹ quan hệ ra/vào của một khối đôi khi sẽ thấy kết quả khác nhau khi tín hiệu đổi chiều "
               "chuyển động. Hệ cơ khí thường cho thấy một khác biệt nhỏ về chiều dài khi đảo chiều lực tác dụng. "
               "Hiệu ứng tương tự xuất hiện khi đảo chiều từ trường trong vật liệu từ. Đặc tính này gọi là "
               "<b>trễ</b> (hysteresis). Hình 3-7 là đồ thị tổng quát của quan hệ ra/vào cho thấy một vòng kín xuất "
               "hiện. Hiệu ứng thường nhỏ đi khi biên độ các lần vượt giảm, và đây là một cách để chấp nhận hiệu "
               "ứng. Nó có mặt trong hầu hết vật liệu. Người ta đã phát triển các vật liệu đặc biệt có trễ thấp cho "
               "ứng dụng của chúng — lá thép từ của máy biến áp và dây lò xo đồng hồ là những ví dụ."))
    b.append(fig(7, hbfig.fig_3_7()))
    b.append(p("Khi hiện tượng này do một cơ cấu gây ra thay đổi đột ngột, chẳng hạn do độ rơ của một mối nối cơ "
               "khí, nó dễ phát hiện và được gọi là <b>khe hở</b> (backlash)."))

    b.append(h3("Bão hoà", "Saturation"))
    b.append(p("Đến đây thảo luận chỉ giới hạn ở các mức tín hiệu nằm trong dải biên độ chấp nhận được. Các khối "
               "thực đôi khi có mức tín hiệu vào lớn hơn mức cho phép. Ở đây xét các sai số chiếm ưu thế phát sinh — "
               "bão hoà và méo chuyển tiếp."))
    b.append(p("Như đã nêu, thuộc tính mang tin của tín hiệu có thể nằm ở giá trị tức thời của tín hiệu hoặc ở một "
               "đặc tính nào đó của tín hiệu xoay chiều biến thiên nhanh. Nếu dạng tín hiệu không được khuếch đại "
               "trung thực, đầu ra sẽ không có cùng độ tuyến tính và đặc tính."))
    b.append(p("Độ lợi của một khối thường giảm khi biên độ tín hiệu tăng. Một tín hiệu vào biên độ thay đổi, như "
               "tín hiệu tuyến tính tăng đều ở Hình 3-8, sẽ được khuếch đại khác nhau tuỳ theo đường cong "
               "độ lợi/biên độ của khối. Trong các bộ khuếch đại điện tử không bù, biên độ lớn thường được khuếch "
               "đại ít hơn so với ở các điểm giữa."))
    b.append(fig(8, hbfig.fig_3_8()))
    b.append(p("Ở mức tín hiệu vào rất thấp có thể phát sinh hai hiệu ứng không mong muốn. Thứ nhất, tín hiệu nhỏ "
               "thường được khuếch đại nhiều hơn so với mức giữa. Đặc tính sai số thứ hai phát sinh trong bộ khuếch "
               "đại điện tử vì các phần tử bán dẫn có một vùng chết, trong đó không có đầu ra cho đến khi vượt một "
               "ngưỡng nhỏ. Hiệu ứng này gây <b>méo chuyển tiếp</b> (crossover distortion) trong bộ khuếch đại."))
    b.append(p("Nếu tín hiệu là dạng sóng xoay chiều, xem Hình 3-9, thì các mức khác nhau trong một chu kỳ có thể "
               "không được khuếch đại như nhau. Hình 3-9(a) cho thấy điều xảy ra khi các phần tử khuếch đại điện tử "
               "cơ bản chỉ có thể khuếch đại một cực tính của tín hiệu. Tín hiệu được gọi là bị <b>chỉnh lưu</b>. "
               "Hình 3-9(b) cho thấy hiệu ứng khi tín hiệu quá lớn và đỉnh không được khuếch đại. Đây gọi là "
               "<b>bão hoà</b> hay <b>cắt đỉnh</b> (clipping). (Như nhiều hiệu ứng vật lý, hiệu ứng này đôi khi được "
               "cố ý dùng trong mạch, ví dụ dùng như cách đơn giản để biến tín hiệu sin thành xung vuông.) Méo "
               "chuyển tiếp thể hiện ở Hình 3-9(c) khi tín hiệu chuyển từ cực tính âm sang dương."))
    b.append(fig(9, hbfig.fig_3_9()))
    b.append(p("Khi tín hiệu vào nhỏ, như trong dùng cảm biến nhạy, cần dạng phân tích gọi là <b>hành vi tín hiệu "
               "nhỏ</b> để làm rõ méo dạng. Nếu tín hiệu tương đối lớn, như khi xét tín hiệu số, người ta dùng "
               "<b>phân tích tín hiệu lớn</b>. Khó khăn thiết kế nảy sinh khi tín hiệu bao dải động rộng vì không dễ "
               "tính đến mọi hiệu ứng khác nhau trong một thiết kế duy nhất."))

    b.append(h3("Bias", "Bias"))
    b.append(p("Đôi khi tình huống xử lý tín hiệu điện tử đòi hỏi tín hiệu vào được xử lý ở mức điện áp hay dòng "
               "trung bình cao hơn bình thường. Ở đây một giá trị dc được cộng vào tín hiệu vào để nâng mức lên "
               "trạng thái cao hơn như Hình 3-10. Nhu cầu này gặp khi chỉ một cực tính tín hiệu có thể được khuếch "
               "đại bởi một phần tử bán dẫn. Nâng đều mức của toàn bộ dạng sóng đưa mọi phần vào vùng tuyến tính hợp "
               "lý của bộ khuếch đại, cho phép tái tạo trung thực hơn. Nếu không dùng bias ở đây thì nửa chu kỳ dưới "
               "sẽ không được khuếch đại, kết quả là chỉ nửa trên xuất hiện ở đầu ra."))
    b.append(fig(10, hbfig.fig_3_10()))

    b.append(h3("Sai số phi tuyến", "Error of Nonlinearity"))
    b.append(p("Lý tưởng, người ta thường mong muốn tồn tại quan hệ tuyến tính chặt giữa tín hiệu vào và ra trong "
               "bộ khuếch đại. Tuy nhiên thiết bị thực luôn có một mức không tuân thủ nào đó, gọi là <b>phi "
               "tuyến</b> (nonlinearity). Nếu một khối thiết bị đo có độ lợi không đổi với mọi mức tín hiệu vào thì "
               "đồ thị quan hệ vào–ra là một đường thẳng; quan hệ khi đó được gọi là <b>tuyến tính</b>."))
    b.append(p("<b>Độ tuyến tính</b> (linearity) là thuật ngữ chung mô tả mức độ gần nhau giữa đáp ứng thực và "
               "đường lý tưởng đó. Cách mô tả sai số đúng ở đây là <b>sai số phi tuyến</b> (error of nonlinearity). "
               "Lưu ý không phải mọi đáp ứng đều cần tuyến tính; một đáp ứng phổ biến khác tuân theo quan hệ "
               "logarit."))
    b.append(p("Mô tả chi tiết sai số này không dễ vì sẽ cần nêu giá trị sai số tại mọi điểm của đồ thị. Thực tế đã "
               "tìm ra cách nêu vắn tắt bằng cách công bố độ lệch lớn nhất so với lý tưởng dưới dạng tỷ số với giá "
               "trị 100 %."))
    b.append(p("Khó khăn nảy sinh khi biểu diễn sai số phi tuyến vì có nhiều cách biểu diễn. Hình 3-11 cho thấy bốn "
               "trường hợp thường gặp. Khác biệt nằm ở cách lập đường thẳng lý tưởng (gọi là “khớp tốt nhất”). "
               "Hình 3-11(a) đặt đường theo phương pháp trung bình thống kê thường được tính là khớp bình phương "
               "nhỏ nhất; các dạng tính khớp đường khác cũng được dùng. Cách này cho sai số tính được nhỏ nhất "
               "trong các kiểu khớp nhưng có thể không phù hợp với cách tầng đang xét được sử dụng. Có những lựa "
               "chọn khác, có thể hợp lý hơn. Hình 3-11(b) buộc đường khớp tốt nhất đi qua điểm zero. Hình 3-11(c) "
               "đặt đường giữa điểm 0 % và 100 % mong đợi. Còn một lựa chọn nữa: đường lý thuyết không nhất thiết "
               "thuộc các trường hợp trên nhưng là vị trí lý tưởng, Hình 3-11(d)."))
    b.append(fig(11, hbfig.fig_3_11()))
    b.append(p("Vì vậy trong thực tế, độ tuyến tính của hệ thiết bị đo có thể được biểu diễn theo nhiều cách. Thực "
               "hành chứng nhận tốt đòi hỏi phải nêu phương pháp xác định sai số cùng với kết quả số, nhưng điều này "
               "thường không được làm. Cũng lưu ý sai số nêu là trường hợp xấu nhất và một phần của đáp ứng có thể "
               "tuyến tính hơn nhiều."))
    b.append(p("Mô tả đặc tính thiết bị đo không phải việc đơn giản. Để làm đầy đủ sẽ cần những phát biểu rất chi "
               "tiết ghi lại đặc tính tại từng điểm. Điều đó thường quá cồng kềnh, nên ngành thiết bị đo đã phát "
               "triển nhiều cách nêu ngắn gọn đủ làm hướng dẫn về đặc tính. Hướng dẫn này thường là một phát biểu "
               "bảo thủ."))
    b.append(p("Còn nhiều bộ mô tả khác cho chế độ tĩnh của thiết bị đo. Bạn đọc được giới thiệu đến nhiều tài liệu "
               "tiêu chuẩn về thuật ngữ thiết bị đo; ví dụ xem Tài liệu tham khảo [3]."))

    # ---------------------------------------------------------------- 3.2
    b.append(h2("3.2 Đặc tính động của hệ thiết bị đo", "Dynamic Characteristics of Instrument Systems"))
    b.append(h3("Xử lý trạng thái động", "Dealing with Dynamic States"))
    b.append(p("Kết quả đo hiếm khi tĩnh theo thời gian. Chúng có thành phần động phải hiểu để diễn giải đúng kết "
               "quả. Ví dụ, vết ghi trên máy ghi biểu đồ bút mực sẽ phụ thuộc tốc độ mà bút có thể bám theo thay đổi "
               "tín hiệu vào."))
    b.append(p("Để đánh giá đúng thiết kế thiết bị đo và cách dùng, giờ cần hiểu sâu các dạng đáp ứng động thường "
               "gặp nhất và xây dựng cơ sở mô hình hoá toán học cho phép phát biểu ngắn gọn về đáp ứng."))
    b.append(p("Nếu quan hệ truyền của một khối tuân theo quy luật tuyến tính thì có thể dùng một phương pháp toán "
               "học tổng quát để mô tả động. Đáng tiếc, chưa tìm được phương pháp toán đơn giản nào mô tả mọi dạng "
               "đáp ứng thiết bị một cách đơn giản và thống nhất. Nếu hành vi là phi tuyến thì mô tả bằng mô hình "
               "toán trở nên rất khó và có thể không thực tế. Tuy vậy có thể nghiên cứu hành vi hệ phi tuyến như các "
               "đoạn tuyến tính nối tiếp nhau. Ở đây máy tính số được dùng hiệu quả để mô hình hoá hệ bất kỳ, miễn "
               "người dùng sẵn lòng bỏ thời gian lập mô hình thoả đáng."))
    b.append(p("Giờ có thể giới thiệu phần toán dùng để mô tả hệ động tuyến tính. Nó cho hiểu biết quý về hành vi "
               "mong đợi của thiết bị đo, và thường thấy rằng đáp ứng có thể được xấp xỉ là tuyến tính."))
    b.append(p("Đáp ứng mô hình hoá ở đầu ra của một khối, <i>G</i><sub>kết quả</sub>, nhận được bằng cách nhân "
               "biểu thức toán của tín hiệu vào <i>G</i><sub>đầu vào</sub> với hàm truyền của khối đang xét "
               "<i>G</i><sub>đáp ứng</sub>, như phương trình 3.5."))
    b.append(eq("G<sub>kết quả</sub> = G<sub>đầu vào</sub> × G<sub>đáp ứng</sub>", "3.5"))
    b.append(p("Để đi tiếp, cần hiểu các hàm vào thường gặp và các dạng đặc tính khối khác nhau. Bắt đầu với nhóm "
               "thứ nhất: các <b>hàm kích thích</b> (forcing functions)."))

    b.append(h3("Hàm kích thích", "Forcing Functions"))
    b.append(p("Trước hết hãy hiểu các dạng tín hiệu vào dùng để thử nghiệm. Các tín hiệu thường dùng nhất ở "
               "Hình 3-12. Mỗi loại có những đặc tính thử nghiệm quý khác nhau. Ví dụ, sóng sin là cơ sở phân tích "
               "mọi dạng sóng phức vì chúng có thể được tạo thành từ tổ hợp nhiều sóng sin, mỗi sóng có đáp ứng "
               "riêng cộng lại cho ra mọi dạng sóng khác. Hàm bậc thang có công dụng trực giác rõ vì quá độ vào "
               "kiểu này thường gặp. Hàm dốc được dùng để tạo đầu vào thực tế hơn cho những hệ không thể có thay "
               "đổi bậc thang tức thời, chẳng hạn khi cố dịch chuyển một khối lượng lớn bằng một lực hữu hạn. Hàm "
               "kích thích cũng được chọn vì chúng dễ mô tả bằng biểu thức toán đơn giản, nhờ đó phân tích toán "
               "tương đối thuận lợi."))
    b.append(fig(12, hbfig.fig_3_12()))

    b.append(h3("Xây dựng phương trình đặc trưng", "Characteristic Equation Development"))
    b.append(p("Hành vi của một khối thể hiện tính tuyến tính được biểu diễn toán học ở dạng tổng quát như phương "
               "trình 3.6."))
    b.append(eq("a<sub>2</sub> d²y/dt² + a<sub>1</sub> dy/dt + a<sub>0</sub> y = x(t)", "3.6"))
    b.append(p("Ở đây các hệ số a<sub>2</sub>, a<sub>1</sub> và a<sub>0</sub> là hằng số phụ thuộc khối cụ thể đang "
               "xét. Vế trái của phương trình được gọi là <b>phương trình đặc trưng</b> (characteristic equation). "
               "Nó đặc trưng cho các tính chất bên trong của khối và không bị thay đổi bởi cách dùng khối."))
    b.append(p("Tổ hợp cụ thể giữa hàm kích thích vào và phương trình đặc trưng của khối cùng quyết định đáp ứng ra "
               "tổng hợp. Các kết nối quanh khối, như phản hồi từ ra về vào, có thể làm thay đổi đáng kể hành vi "
               "tổng thể: tuy vậy các hệ như thế không được xét trong mục này vì thuộc lĩnh vực hệ điều khiển phản "
               "hồi."))
    b.append(p("Nghiệm của hành vi tổng hợp nhận được bằng phương pháp biến đổi Laplace để có đáp ứng ra trong miền "
               "thời gian hoặc miền tần số phức. Những phương pháp toán này có thể chưa quen với bạn đọc, nhưng đó "
               "không phải khó khăn nghiêm trọng vì các trường hợp thường gặp nhất trong thực tế đã được ghi chép "
               "đầy đủ theo cách dễ hiểu, quá trình toán đã được thực hiện để cho kết quả dùng được mà không cần "
               "cùng trình độ toán. Có thể tìm giải thích sâu hơn ở [1] hoặc bất kỳ giáo trình nào về phân tích hệ "
               "năng lượng. Ở đây chỉ đủ chỗ cho phần giới thiệu; phần này gắn với [1], Chương 17, để bạn đọc tra "
               "cứu mô tả đầy đủ hơn khi cần."))
    b.append(p("Bước tiếp theo để hiểu hành vi khối là khảo sát bản chất phương trình 3.6 khi số hạng đạo hàm trong "
               "biểu thức tăng lên, các phương trình 3.7 đến 3.10."))
    b.append(eq("a<sub>0</sub> y = x(t) &nbsp;&nbsp;— bậc zero", "3.7"))
    b.append(eq("a<sub>1</sub> dy/dt + a<sub>0</sub> y = x(t) &nbsp;&nbsp;— bậc một", "3.8"))
    b.append(eq("a<sub>2</sub> d²y/dt² + a<sub>1</sub> dy/dt + a<sub>0</sub> y = x(t) &nbsp;&nbsp;— bậc hai", "3.9"))
    b.append(eq("a<sub>n</sub> dⁿy/dtⁿ + … + a<sub>1</sub> dy/dt + a<sub>0</sub> y = x(t) "
                "&nbsp;&nbsp;— bậc n", "3.10"))
    b.append(p("Lưu ý mỗi bậc có tên riêng. Trường hợp bậc zero thường không được xét trong sách vì không có số hạng "
               "phụ thuộc thời gian nên được xem là tầm thường. Nó là bộ khuếch đại (hay suy giảm) hàm kích thích "
               "với độ lợi a<sub>0</sub>. Nó có băng thông vô hạn mà không thay đổi hằng số khuếch đại."))
    b.append(p("Bậc cao nhất thường cần xét trong phân tích thiết bị đo sơ bộ là lớp bậc hai. Hệ bậc cao hơn có xảy "
               "ra trong thực tế và cần phân tích không thể tóm gọn ở đây. Việc nghiên cứu chúng cũng cần chuyên môn "
               "sâu. Có thể dùng công cụ phân tích hệ có máy tính hỗ trợ để khảo sát đáp ứng của hệ."))
    b.append(p("Một bước nữa là viết lại các phương trình sau biến đổi Laplace sang miền tần số. Ta được tập phương "
               "trình ra/vào 3.11 đến 3.14."))
    b.append(eq("Y(s)/X(s) = 1", "3.11"))
    b.append(eq("Y(s)/X(s) = 1/(1 + τ<sub>1</sub>s)", "3.12"))
    b.append(eq("Y(s)/X(s) = 1/[(1 + τ<sub>1</sub>s)(1 + τ<sub>2</sub>s)]", "3.13"))
    b.append(eq("Y(s)/X(s) = 1/[(1 + τ<sub>1</sub>s)(1 + τ<sub>2</sub>s) … (1 + τ<sub>n</sub>s)]", "3.14"))
    b.append(p("Các số hạng τ<sub>1</sub>, …, τ<sub>n</sub> được gọi là <b>hằng số thời gian</b> (time constants). "
               "Chúng là những tham số then chốt của đặc tính hệ."))

    b.append(h3("Đáp ứng của các loại hệ tuyến tính", "Response of the Different Linear Systems Types"))
    b.append(p("Hạn chế về dung lượng không cho phép khảo sát chi tiết mọi lựa chọn. Một số được chọn trình bày để "
               "cho thấy chúng được phân tích và báo cáo thế nào, từ đó dẫn đến việc người làm thiết bị đo có thể "
               "dùng một số đồ thị chuẩn trong nghiên cứu đặc tính các khối."))

    b.append(h3("Khối bậc zero", "Zero-Order Blocks"))
    b.append(p("Để khảo sát đáp ứng của một khối, nhân dạng miền tần số của phương trình đặc trưng với phương trình "
               "của hàm kích thích đã chọn."))
    b.append(p("Đây là trường hợp thú vị vì phương trình 3.7 cho thấy khối bậc zero không có số hạng phụ thuộc tần "
               "số (không có số hạng đạo hàm theo thời gian), nên đầu ra với mọi đầu vào chỉ có thể cùng dạng thời "
               "gian với đầu vào. Cái có thể thay đổi là biên độ, cho bởi hệ số a<sub>0</sub>. Cũng không xảy ra "
               "dịch thời gian (dịch pha) của dạng sóng ra so với vào như có thể xảy ra với khối bậc cao hơn."))
    b.append(p("Đây là đáp ứng thường mong muốn ở thiết bị đo vì nghĩa là khối không làm thay đổi đáp ứng thời gian. "
               "Tuy nhiên không phải luôn như vậy, vì trong hệ thống, các khối thiết kế thường được chọn vì khả năng "
               "thay đổi dạng thời gian của tín hiệu theo cách đã biết."))
    b.append(p("Dù hơi hiển nhiên, Hình 3-13 — một cảm biến biến dạng điện trở — được nêu để minh hoạ hành vi bậc "
               "zero."))
    b.append(fig(13, hbfig.fig_3_13()))

    b.append(h3("Khối bậc một", "First-Order Blocks"))
    b.append(p("Ở đây phương trình 3.8 là phương trình đặc trưng liên quan. Có số hạng phụ thuộc thời gian nên cần "
               "phân tích để thấy loại khối này hành xử thế nào trong điều kiện động. Đáp ứng ra khác nhau với mỗi "
               "loại hàm kích thích áp vào. Giới hạn dung lượng chỉ cho phép giới thiệu các trường hợp thường gặp "
               "nhất — đầu vào bậc thang và sóng sin. Ở đây cũng chỉ có thể phác phương pháp phân tích và đưa các đồ "
               "thị chuẩn hoá vẽ hành vi tổng quát."))
    b.append(p("Đáp ứng bậc thang của hệ bậc một nhận được bằng cách nhân phương trình 3.12 với phương trình miền "
               "tần số của một bậc thang biên độ <i>A</i>. Kết quả sau đó được biến đổi ngược về miền thời gian bằng "
               "biến đổi Laplace để có biểu thức đầu ra y(t):"))
    b.append(eq("y(t) = A·K (1 − e<sup>−t/τ</sup>)", "3.15"))
    b.append(p("trong đó <i>A</i> là biên độ bậc thang, <i>K</i> là độ lợi tĩnh của khối bậc một, <i>t</i> là thời "
               "gian theo đơn vị nhất quán, và τ là hằng số thời gian gắn với chính khối."))
    b.append(p("Đây là kết quả gọn gàng vì phương trình 3.15 bao quát đáp ứng bậc thang của mọi khối bậc một, nhờ "
               "đó có thể vẽ đồ thị theo dạng chuẩn hoá như Hình 3-14. Dạng của đáp ứng luôn cùng một kiểu. Điều "
               "này nghĩa là đáp ứng bậc thang của hệ bậc một có thể được mô tả là “một bậc thang biên độ AK với "
               "hằng số thời gian τ”."))
    b.append(fig(14, hbfig.fig_3_14()))
    b.append(p("Nếu đầu vào là sóng sin, đáp ứng ra khác hẳn; nhưng một lần nữa sẽ thấy có nghiệm tổng quát cho mọi "
               "tình huống loại này. Như trước, phương trình hàm kích thích vào được nhân với phương trình đặc trưng "
               "của khối bậc một và dùng biến đổi Laplace để trở về miền thời gian. Sau khi sắp xếp thành hai phần, "
               "ta được:"))
    b.append(eq("y(t) = A·K·e<sup>−t/τ</sup> + [A·K/√(1 + ω²τ²)] · sin(ωt + φ)", "3.16"))
    b.append(p("trong đó ω là tần số góc của tín hiệu (rad/s), φ = tan<sup>−1</sup>(−ωτ), <i>A</i> là biên độ sóng "
               "sin vào, <i>K</i> là độ lợi của khối bậc một, <i>t</i> là thời gian theo đơn vị nhất quán, và τ là "
               "hằng số thời gian gắn với khối."))
    b.append(p("Số hạng đầu tiên là quá độ thời gian ngắn, thường được bỏ qua, tắt rất nhanh về zero, để lại đầu ra "
               "xác lập là tham số thường được quan tâm. Nghiên cứu phần xác lập tốt nhất là vẽ nó theo dạng chuẩn "
               "hoá, như đã làm ở Hình 3-15."))
    b.append(fig(15, hbfig.fig_3_15()))
    b.append(p("Các đồ thị này cho thấy biên độ đầu ra luôn giảm khi tần số tín hiệu vào tăng và luôn có tác dụng "
               "trễ pha giữa vào và ra, có thể từ 0 đến 90° nhưng không bao giờ vượt quá 90°. Mức độ của các hiệu "
               "ứng này phụ thuộc các hệ số cụ thể của khối và tín hiệu vào. Phải hiểu rõ các hiệu ứng này khi diễn "
               "giải kết quả đo vì có thể phát sinh sai số đáng kể khi dùng hệ bậc một trong chuỗi thiết bị đo."))

    b.append(h3("Khối bậc hai", "Second-Order Blocks"))
    b.append(p("Nếu có số hạng vi phân bậc hai, đáp ứng của khối khác hẳn, lại đáp ứng theo cách khá ngoạn mục với "
               "những đặc điểm có thể mong muốn hoặc không."))
    b.append(p("Như trước, để có đáp ứng ra, nhân hàm đặc trưng của khối với hàm kích thích đã chọn. Tuy nhiên để "
               "kết quả có ý nghĩa hơn, trước hết thực hiện một số phép thay thế đơn giản."))
    b.append(p("Các bước bắt đầu bằng việc biến đổi phương trình vi phân bậc hai 3.6 sang dạng Laplace:"))
    b.append(eq("X(s) = a<sub>2</sub>s²Y(s) + a<sub>1</sub>sY(s) + a<sub>0</sub>Y(s)", "3.17"))
    b.append(p("Sau đó sắp xếp lại để được:"))
    b.append(eq("G(s) = Y(s)/X(s) = (1/a<sub>0</sub>) · 1/[(a<sub>2</sub>/a<sub>0</sub>)s² + "
                "(a<sub>1</sub>/a<sub>0</sub>)s + 1]", "3.18"))
    b.append(p("Các hệ số khi đó có thể được biểu diễn bằng các tham số đặc tính hệ như sau."))
    b.append(eq("tần số riêng góc: &nbsp; ω<sub>n</sub> = √(a<sub>0</sub>/a<sub>2</sub>)", "3.19"))
    b.append(eq("tỉ số tắt dần: &nbsp; ζ = a<sub>1</sub> / (2√(a<sub>0</sub>·a<sub>2</sub>))", "3.20"))
    b.append(eq("độ lợi tĩnh: &nbsp; K = 1/a<sub>0</sub>", "3.21"))
    b.append(p("Ba biến này có ý nghĩa thực tế, như sẽ thấy khi vẽ các đáp ứng khác nhau."))
    b.append(p("Dùng các biến đã biến đổi này, phương trình đặc trưng có thể được viết lại thành hai dạng sẵn sàng "
               "cho việc khảo sát hành vi đầu ra với đầu vào bậc thang và sóng sin, như:"))
    b.append(eq("G(s) = K / [(1/ω<sub>n</sub>²)s² + (2ζ/ω<sub>n</sub>)s + 1]", "3.22"))
    b.append(eq("G(s) = K / (τ²s² + 2ζτs + 1)", "3.23"))
    b.append(p("Giờ đã sẵn sàng xét hành vi của hệ bậc hai với các hàm kích thích khác nhau."))
    b.append(p("Trước hết xét đầu vào bậc thang. Sau khi lập tích của hàm kích thích và hàm đặc trưng, dạng miền "
               "thời gian có thể được vẽ như Hình 3-16."))
    b.append(fig(16, hbfig.fig_3_16()))
    b.append(p("Điều này cho thấy rõ đáp ứng phụ thuộc mạnh vào giá trị tỉ số tắt dần ζ. Nếu nhỏ hơn 1, nó thể hiện "
               "dao động tắt dần về giá trị cuối. Nếu lớn hơn 1, đáp ứng đi tới giá trị cuối mà không dao động. "
               "Trạng thái thường được ưa dùng là tỉ số tắt dần bằng 1, <b>tắt dần tới hạn</b> (critical damping). "
               "Việc chọn đáp ứng phụ thuộc mạnh vào ứng dụng, vì mọi mức tỉ số tắt dần đều có chỗ dùng trong thực "
               "tế, từ cần một dao động không bao giờ tắt (tắt dần zero) đến thái cực kia là tốc độ thay đổi rất từ "
               "từ."))
    b.append(p("Phân tích tương tự được dùng để xem hệ bậc hai đáp ứng thế nào với đầu vào sóng sin. Hai đồ thị đáp "
               "ứng nhận được ở Hình 3-17: một cho đáp ứng biên độ, một cho thấy pha dịch thế nào khi tần số thay "
               "đổi."))
    b.append(fig(17, hbfig.fig_3_17()))
    b.append(p("Kết quả bất ngờ nhất thấy ở điểm độ lợi tăng tới vô cùng với trạng thái tắt dần zero. Đây gọi là "
               "<b>cộng hưởng</b> (resonance) và xảy ra ở tần số riêng của khối với trạng thái tắt dần zero. Cộng "
               "hưởng có thể là đặc điểm mong muốn, như khi phát hiện một tần số cụ thể trong mạch thu tần số vô "
               "tuyến, hoặc rất không mong muốn, như khi một hệ cơ khí cộng hưởng, có thể đến mức phá huỷ."))
    b.append(p("Có thể thấy nó chủ yếu được điều khiển bởi tỉ số tắt dần. Cũng lưu ý pha của hệ bậc hai trải từ 0 "
               "đến 180°. Điều này có hệ quả quan trọng nếu khối là phần của một vòng phản hồi, vì khi tần số tăng, "
               "dịch pha từ khối sẽ chuyển từ phản hồi âm ổn định (nhỏ hơn 90°) sang phản hồi dương (lớn hơn 90°), "
               "gây dao động không mong muốn."))
    b.append(p("Chi tiết hơn về các tình huống khác, gồm cách xử lý bậc cao hơn, các khối nối tiếp cùng loại và đầu "
               "vào dốc, được trình bày ở [1]."))

    # ---------------------------------------------------------------- 3.3
    b.append(h2("3.3 Hiệu chuẩn phép đo", "Calibration of Measurements"))
    b.append(p("Ta đã giới thiệu khái niệm độ chính xác khi thực hiện một phép đo và việc độ không đảm bảo vốn có "
               "trong mọi phép đo phải được giữ đủ nhỏ. Quá trình và thiết bị dùng để xác định xem một phép đo có đủ "
               "chính xác không được gọi là <b>hiệu chuẩn</b> (calibration). Việc này được thực hiện bằng cách so "
               "sánh kết quả của một phép đo với một phương pháp có đặc tính đo được thừa nhận chung là ít không "
               "đảm bảo hơn kết quả nhận được. Sai số phát sinh trong chính thiết bị và quá trình hiệu chuẩn, và "
               "trong phép so sánh, nhất thiết phải nhỏ hơn mức yêu cầu. Điều này nghĩa là hiệu chuẩn thường là một "
               "quá trình tốn kém. Thực hiện hiệu chuẩn tốt cần chuyên môn chuyên sâu."))
    b.append(p("Phương pháp và thiết bị hiệu chuẩn thiết bị đo rất đa dạng. Một ví dụ minh hoạ cho khái niệm so sánh "
               "nằm sau tất cả chúng là việc hiệu chuẩn lưu lượng kế, được vẽ sơ đồ ở Hình 3-18."))
    b.append(fig(18, hbfig.fig_3_18()))
    b.append(p("Nhờ một bình tràn, bình trên cung cấp dòng nước không đổi vì nước đến từ một độ cao không đổi. Lưu "
               "lượng kế cần hiệu chuẩn được đặt trên ống phía sau."))
    b.append(p("Dòng phía sau hoặc được chuyển vào bình cân, hoặc quay về nguồn cấp. Để thực hiện một phép đo, trước "
               "hết cho nước chảy về nguồn cấp. Vào lúc bắt đầu khoảng thử, nước được chuyển nhanh và chính xác vào "
               "bình. Sau một khoảng thời gian xác định, nước lại được đưa về nguồn cấp. Như vậy bình đã nhận một "
               "lượng nước xác định trong một khoảng thời gian chảy xác định. Sau đó tính toán để ra lượng nước chảy "
               "trong một đơn vị thời gian, tức lưu lượng. Lưu lượng kế đã chỉ một giá trị lưu lượng không đổi trong "
               "suốt thời gian đó. Giá trị này được so với phương pháp cân để ra sai số. Suy nghĩ một chút sẽ thấy "
               "nhiều nguồn sai số trong thiết bị thử, chẳng hạn nhiệt độ của nước quyết định thể tích chảy qua nên "
               "phải được tính đến trong các phép tính."))
    b.append(p("Cũng sẽ rõ rằng việc hiệu chuẩn này có thể không được thực hiện trong cùng điều kiện như khi thiết bị "
               "đo thường được dùng. Nghệ thuật, khoa học và những khó khăn vốn có khi thực hiện hiệu chuẩn chất "
               "lượng cho cảm biến nhiệt độ đã được trình bày kỹ [2]."))
    b.append(p("Hiệu chuẩn thiết bị đo là việc bắt buộc, vì không có nó kết quả đo có thể gây hiểu nhầm và dẫn đến "
               "những hậu quả tốn kém. Thực hiện hiệu chuẩn tốt làm tăng chi phí vận hành cho việc đo nhưng nó giống "
               "như mua bảo hiểm. Nếu đầu tư đó được làm đúng, nó sẽ giúp giảm nhẹ các tổn thất về sau. Ví dụ, một "
               "máy trộn xi măng tự động được hiệu chuẩn sai đã được dùng để làm bê tông cho khung kết cấu của một "
               "toà nhà nhiều tầng. Phải mất vài ngày thử cường độ bê tông mới phát hiện máy trộn đã mất hiệu chuẩn "
               "một ngày, với kết quả là bê tông đã đổ cho ba tầng không đủ cường độ. Đến lúc đó, đã đổ thêm nhiều "
               "tầng lên trên. Các tầng khiếm khuyết phải được thay hoàn toàn với chi phí lớn. Đầu tư thêm nguồn lực "
               "cho quá trình hiệu chuẩn sẽ bảo đảm máy trộn làm việc đúng."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>P. H. Sydenham, <em>Handbook of Measurement Science</em>, Vol. 2, Chichester, U.K.: John Wiley &amp; Sons, 1983.</li>'
             '<li>J. V. Nicholas and D. R. White, <em>Traceable Temperatures</em>, Chichester, U.K.: John Wiley &amp; Sons, 1994.</li>'
             '<li>British Standard Institution, <em>PD 6461: Vocabulary of Metrology</em>, London: BSI, 1995.</li>'
             '</ol>')
    b.append('<div class="chapter-nav">'
             '<a href="%sch02-operational-modes-of-instrumentation/"><span class="k">← Chương 2</span>'
             'Các chế độ vận hành của thiết bị đo</a>'
             '<a href="%sch04-measurement-accuracy/" style="text-align:right;"><span class="k">Chương 4 →</span>'
             'Độ chính xác của phép đo</a></div>' % (BASE_VI, BASE_VI))
    return "".join(b)


# ------------------------------------------------------------------ EN body
def body_en():
    figs = [(1, hbfig.fig_3_1()), (2, hbfig.fig_3_2()), (3, hbfig.fig_3_3()), (4, hbfig.fig_3_4()),
            (5, hbfig.fig_3_5()), (6, hbfig.fig_3_6()), (7, hbfig.fig_3_7()), (8, hbfig.fig_3_8()),
            (9, hbfig.fig_3_9()), (10, hbfig.fig_3_10()), (11, hbfig.fig_3_11()), (12, hbfig.fig_3_12()),
            (13, hbfig.fig_3_13()), (14, hbfig.fig_3_14()), (15, hbfig.fig_3_15()), (16, hbfig.fig_3_16()),
            (17, hbfig.fig_3_17()), (18, hbfig.fig_3_18())]
    b = []
    b.append('<div class="note"><b>What this page is.</b> A figure companion to Chapter 3. The full text lives in '
             '<code>Ch03.pdf</code> in the library catalogue and is not republished here; the eighteen figures are '
             'redrawn as vectors, numbered and captioned as in the book, so they stay readable on a phone. The '
             'complete Vietnamese translation of this chapter is '
             '<a href="%s%s/">here</a>.</div>' % (BASE_VI, CSLUG))
    b.append('<p class="lead">Chapter 3 is the measurement-theory chapter of the handbook. It separates the three '
             'concepts that are routinely confused — discrimination (the smallest distinguishable increment), '
             'precision (the spread of repeated readings, i.e. repeatability and reproducibility) and accuracy '
             '(closeness to the true value) — then treats the static characteristics of a block (input/output '
             'slope, offset, span and dynamic range, drift, hysteresis and backlash, saturation and crossover '
             'distortion, bias, and the error of nonlinearity in its four best-fit conventions) and the dynamic '
             'characteristics (forcing functions, the characteristic equation, and the zero-, first- and '
             'second-order responses with their time constant, damping ratio and resonance). It closes with '
             'calibration, illustrated by a gravimetric flow-meter rig.</p>')
    b.append('<h2>Chapter outline</h2><ul class="toc-list">'
             '<li><span class="n">3.1</span><span class="t">Static Characteristics of Instrument Systems</span></li>'
             '<li><span class="n">·</span><span class="t">Output/Input Relationship · Drift · Hysteresis and '
             'Backlash · Saturation · Bias · Error of Nonlinearity</span></li>'
             '<li><span class="n">3.2</span><span class="t">Dynamic Characteristics of Instrument Systems</span></li>'
             '<li><span class="n">·</span><span class="t">Forcing Functions · Characteristic Equation · Zero-, '
             'First- and Second-Order Blocks</span></li>'
             '<li><span class="n">3.3</span><span class="t">Calibration of Measurements</span></li>'
             '<li><span class="n">·</span><span class="t">References</span></li></ul>')
    b.append('<h2>Figures</h2><p style="color:#888;font-size:.82rem">Redrawn from the Vietnamese edition '
             '(Figures 3-1 to 3-18).</p>')
    for n, f in figs:
        b.append(fig(n, f, lang="en"))
    b.append('<div class="chapter-nav">'
             '<a href="%sch02-operational-modes-of-instrumentation/"><span class="k">← Chapter 2</span>'
             'Operational Modes of Instrumentation</a>'
             '<a href="%sch04-measurement-accuracy/" style="text-align:right;"><span class="k">Chapter 4 →</span>'
             'Measurement Accuracy</a></div>'
             % (BASE_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 3 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 3 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 3 “Static and Dynamic Characteristics of Instrumentation” của "
            "Peter H. Sydenham — độ phân giải, độ chụm, độ chính xác; đặc tính tĩnh (độ nhạy, offset, trôi, trễ, "
            "bão hoà, phi tuyến); đặc tính động (bậc zero, bậc một, bậc hai) và hiệu chuẩn." if vi else
            "Figure companion to Chapter 3 of the CRC Measurement Handbook — static and dynamic characteristics "
            "of instrumentation, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 3'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 3' % BASE_EN)
    meta = ("Chương 3 · theo Ch03.pdf (CRC Press, 1999) · 18 hình" if vi
            else "Chapter 3 · 18 figures")
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
