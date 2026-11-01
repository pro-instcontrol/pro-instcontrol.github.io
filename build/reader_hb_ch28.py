# -*- coding: utf-8 -*-
"""Handbook Chapter 28 — Flow Measurement
(Richard Thorn — University of Derby; Adrian Melling, Herbert Köchner,
Reinhard Haak — Universität Erlangen-Nürnberg; Zaki D. Husain,
Donald J. Wass — Daniel Flow Products; David Wadlow — Sensors Research
Consulting; Harold M. Miller — Data Industrial; Halit Eren — Curtin
University of Technology; Hans-Peter Vaterlaus).

The largest chapter in the handbook: 132 source pages, eleven sections,
92 figures, 162 equations and 23 tables. It is translated section by section;
each section is a pair of functions (sec_NN_vi / sec_NN_en) appended to the
two body builders at the bottom, so a later session can add a section without
touching the ones already written.

Run:  python build/reader_hb_ch28.py
"""
import os

import hb28fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch28-flow-measurement"
TITLE_EN = "Flow Measurement"
TITLE_VI = "Đo lưu lượng"
BYLINE = ("Richard Thorn (University of Derby) · Adrian Melling · Herbert Köchner · "
          "Reinhard Haak (Universität Erlangen-Nürnberg) · Zaki D. Husain · "
          "Donald J. Wass (Daniel Flow Products) · David Wadlow (Sensors Research "
          "Consulting) · Harold M. Miller (Data Industrial) · Halit Eren (Curtin "
          "University of Technology) · Hans-Peter Vaterlaus")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch27-acoustic-measurement"
PREV_VI = "ch27-acoustic-measurement"
PREV_T_EN = "Acoustic Measurement"
PREV_T_VI = "Đo âm học"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-28-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


def defs(items):
    """Defining-terms block. Rendered as a two-column table so it inherits the
    reader's existing .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


def table(hd, rows, cap, cls="tbl"):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ table data

def _t281(lang):
    """Table 28.1 — transposed so eleven columns become four."""
    if lang == "vi":
        hd = ("Chỉ tiêu", "Tấm orifice", "Ống Venturi", "Vòi phun")
        cap = ("Bảng 28.1 · Tính năng và phạm vi ứng dụng của các lưu lượng kế chênh áp thông dụng. "
               "Độ chính xác là số liệu khi chưa hiệu chuẩn; hiệu chuẩn tại chỗ sau khi lắp có thể "
               "cải thiện đáng kể.")
        rows = [
            ["Độ chính xác điển hình (chưa hiệu chuẩn)", "±2 %", "±2 %", "±2 %"],
            ["Dải đo điển hình", "3:1", "3:1", "3:1"],
            ["Đường kính ống điển hình (mm)", "10–1000", "25–500", "25–250"],
            ["Tổn thất áp suất vĩnh viễn", "Cao", "Thấp", "Cao"],
            ["Giá thành tương đối", "Thấp", "Cao", "Trung bình"],
            ["Khí sạch", "Có", "Có", "Có"],
            ["Khí bẩn", "Không", "Có thể", "Có thể"],
            ["Chất lỏng sạch", "Có", "Có", "Có"],
            ["Bùn / huyền phù", "Không", "Có thể", "Không"],
            ["Hơi nước", "Có", "Có thể", "Có"],
        ]
    else:
        hd = ("Performance", "Orifice plate", "Venturi tube", "Nozzle")
        cap = ("Table 28.1 · Performance and application areas of the common differential pressure "
               "flowmeters. Accuracy figures are uncalibrated; calibrating in place after "
               "installation improves them substantially.")
        rows = [
            ["Typical uncalibrated accuracy", "±2 %", "±2 %", "±2 %"],
            ["Typical range", "3:1", "3:1", "3:1"],
            ["Typical pipe diameter (mm)", "10–1000", "25–500", "25–250"],
            ["Permanent pressure loss", "High", "Low", "High"],
            ["Comparative cost", "Low", "High", "Medium"],
            ["Clean gas", "Yes", "Yes", "Yes"],
            ["Dirty gas", "No", "Maybe", "Maybe"],
            ["Clean liquid", "Yes", "Yes", "Yes"],
            ["Slurry", "No", "Maybe", "No"],
            ["Steam", "Yes", "Maybe", "Yes"],
        ]
    return hd, rows, cap


def _t282(lang):
    if lang == "vi":
        hd = ("Công ty", "Địa chỉ · điện thoại")
        cap = "Bảng 28.2 · Một số hãng cung cấp lưu lượng kế chênh áp."
        rows = [
            ["ABB Kent-Taylor", "Oldens Lane, Stonehouse, Gloucestershire GL10 3TA, Anh · "
             "+44 1453 826661 · fax +44 1453 826358"],
            ["Daniel Industries Inc.", "9720 Katy Road, P.O. Box 19097, Houston, TX 77224 · "
             "(713) 467-6000 · fax (713) 827-3880"],
            ["Hartmann &amp; Braun (UK) Ltd.", "Bush Beach Engineering Division, Stanley Green "
             "Trading Estate, Cheadle Hulme, Cheshire SK8 6RN, Anh · +44 161 4858151"],
            ["ISA Controls Ltd.", "Hackworth Industrial Park, Shildon, County Durham DL4 1LH, "
             "Anh · +44 1388 773065"],
            ["Perry Equipment Corporation", "Wolters Industrial Park, P.O. Box 640, Mineral "
             "Wells, TX 76067 · (817) 325-2575"],
        ]
    else:
        hd = ("Company", "Address · telephone")
        cap = "Table 28.2 · A selection of companies that supply differential pressure flowmeters."
        rows = [
            ["ABB Kent-Taylor", "Oldens Lane, Stonehouse, Gloucestershire GL10 3TA, England · "
             "+44 1453 826661 · fax +44 1453 826358"],
            ["Daniel Industries Inc.", "9720 Katy Road, P.O. Box 19097, Houston, TX 77224 · "
             "(713) 467-6000 · fax (713) 827-3880"],
            ["Hartmann &amp; Braun (UK) Ltd.", "Bush Beach Engineering Division, Stanley Green "
             "Trading Estate, Cheadle Hulme, Cheshire SK8 6RN, England · +44 161 4858151"],
            ["ISA Controls Ltd.", "Hackworth Industrial Park, Shildon, County Durham DL4 1LH, "
             "England · +44 1388 773065"],
            ["Perry Equipment Corporation", "Wolters Industrial Park, P.O. Box 640, Mineral "
             "Wells, TX 76067 · (817) 325-2575"],
        ]
    return hd, rows, cap


def _t283(lang):
    if lang == "vi":
        hd = ("Tỉ số đường kính β", "Một cút 90°", "Hai cút 90° cùng mặt phẳng",
              "Hai cút 90° khác mặt phẳng", "Van cầu mở hoàn toàn", "Hạ lưu lưu lượng kế")
        cap = ("Bảng 28.3 · Chiều dài ống thẳng tối thiểu cần có giữa các phụ kiện và tấm orifice "
               "hoặc ống Venturi (theo ISO 5167-1) để bảo đảm mặt cắt đo có phân bố dòng chảy phát "
               "triển đầy đủ. Mọi giá trị là bội số của đường kính ống.")
    else:
        hd = ("Diameter ratio β", "Single 90° bend", "Two 90° bends, same plane",
              "Two 90° bends, different planes", "Globe valve fully open",
              "Downstream of the flowmeter")
        cap = ("Table 28.3 · Minimum straight lengths of pipe required between various fittings and "
               "an orifice plate or Venturi tube (as recommended in ISO 5167-1) so that a fully "
               "developed flow profile exists in the measurement section. All lengths are multiples "
               "of the pipe diameter.")
    rows = [["0.2", "10", "14", "34", "18", "4"],
            ["0.4", "14", "18", "36", "20", "6"],
            ["0.6", "18", "26", "48", "26", "7"],
            ["0.8", "46", "50", "80", "44", "8"]]
    return hd, rows, cap


def _t284(lang):
    if lang == "vi":
        hd = ("Tổ chức", "Tiêu chuẩn", "Nội dung")
        cap = "Bảng 28.4 · Các tiêu chuẩn liên quan đến đo lưu lượng bằng chênh áp."
        rows = [
            ["ANSI (New York)", "ANSI/ASHRAE 41.8",
             "Phương pháp đo lưu lượng chất lỏng trong ống bằng lưu lượng kế orifice"],
            ["ANSI (New York)", "ANSI/ASME MFC-7M", "Đo lưu lượng khí bằng vòi phun Venturi tới hạn"],
            ["ANSI (New York)", "ANSI/ASME MFC-14M", "Đo lưu lượng bằng lưu lượng kế orifice nhỏ, chính xác"],
            ["API (Washington)", "API 2530",
             "Sổ tay tiêu chuẩn đo dầu khí, Ch. 14 §3 — đo khí thiên nhiên bằng orifice"],
            ["ASME (New York)", "ASME MFC-3M", "Đo lưu lượng trong ống bằng orifice, vòi phun và Venturi"],
            ["ASME (New York)", "ASME MFC-8M",
             "Dòng chảy trong ống kín — đấu nối truyền tín hiệu áp giữa thiết bị sơ cấp và thứ cấp"],
            ["BSI (London)", "BS 1042", "Đo lưu lượng chất lưu trong ống kín"],
            ["ISO (Genève)", "ISO 2186", "Đấu nối truyền áp giữa phần tử sơ cấp và thứ cấp"],
            ["ISO (Genève)", "ISO TR 3313", "Đo dòng chảy dao động bằng orifice, vòi phun hoặc Venturi"],
            ["ISO (Genève)", "ISO 5167-1", "Đo lưu lượng bằng các thiết bị chênh áp"],
            ["ISO (Genève)", "ISO 9300", "Đo lưu lượng khí bằng vòi phun Venturi tới hạn"],
        ]
    else:
        hd = ("Body", "Standard", "Scope")
        cap = "Table 28.4 · Standards related to differential pressure flow measurement."
        rows = [
            ["ANSI (New York)", "ANSI/ASHRAE 41.8",
             "Standard methods of measurement of flow of liquids in pipes using orifice flowmeters"],
            ["ANSI (New York)", "ANSI/ASME MFC-7M", "Measurement of gas flow by critical flow Venturi nozzles"],
            ["ANSI (New York)", "ANSI/ASME MFC-14M", "Measurement of fluid flow using small bore precision orifice meters"],
            ["API (Washington)", "API 2530",
             "Manual of Petroleum Measurement Standards, Ch. 14 §3 — orifice metering of natural gas"],
            ["ASME (New York)", "ASME MFC-3M", "Measurement of fluid flow in pipes using orifice, nozzle and Venturi"],
            ["ASME (New York)", "ASME MFC-8M",
             "Fluid flow in closed conduits — connections for pressure signal transmission"],
            ["BSI (London)", "BS 1042", "Measurement of fluid flow in closed conduits"],
            ["ISO (Genève)", "ISO 2186", "Connections for pressure transmission between primary and secondary elements"],
            ["ISO (Genève)", "ISO TR 3313", "Measurement of pulsating fluid flow by orifice plates, nozzles or Venturi tubes"],
            ["ISO (Genève)", "ISO 5167-1", "Measurement of fluid flow by means of pressure differential devices"],
            ["ISO (Genève)", "ISO 9300", "Measurement of gas flow by means of critical flow Venturi nozzles"],
        ]
    return hd, rows, cap


# ================================================================ 28.1

def sec_28_1_vi():
    b = []
    b.append(h2("28.1 Lưu lượng kế chênh áp", "Differential Pressure Flowmeters"))
    b.append(p("Richard Thorn — Đại học Derby."))
    b.append(p(
        "Đo lưu lượng là việc xảy ra hằng ngày. Từ việc đổ xăng cho ô tô đến việc biết vòi phun "
        "trong vườn đang tiêu bao nhiêu nước, đều cần một lưu lượng kế. Cũng khó hình dung một "
        "ngành công nghiệp nào mà ở đó lưu lượng kế không đóng vai trò nào. Thị trường lưu lượng kế "
        "thế giới được ước khoảng 2.500 triệu USD năm 1995 và dự kiến còn tăng đều trong thời gian "
        "tới. Giá trị sản phẩm được đo bằng các thiết bị này cũng rất lớn: chỉ riêng ở Anh, năm "
        "1994, giá trị dầu thô khai thác ước khoảng 15 tỷ USD."))
    b.append(p(
        "Với quy mô thị trường và giá trị sản phẩm như vậy, khá ngạc nhiên là độ chính xác và năng "
        "lực của nhiều lưu lượng kế lại kém so với các thiết bị đo những biến quá trình thông dụng "
        "khác như áp suất và nhiệt độ. Ví dụ, lưu lượng kế tấm orifice — được dùng thương mại từ đầu "
        "những năm 1900 và có độ chính xác điển hình ±2 % giá trị đọc — vẫn là loại duy nhất được "
        "hầu hết các nước cho phép dùng để đo đối chiếu tài chính khí thiên nhiên. Dù những kỹ thuật "
        "mới như lưu lượng kế Coriolis ngày càng phổ biến, ngành đo lưu lượng vốn bảo thủ và vẫn bị "
        "chi phối bởi các kỹ thuật truyền thống; xem [1] để có tổng quan về phát triển gần đây."))
    b.append(p(
        "Hơn 40 % mọi phép đo chất lỏng, khí và hơi trong công nghiệp vẫn được thực hiện bằng các "
        "loại <b>lưu lượng kế chênh áp</b> thông dụng, tức tấm orifice, ống Venturi và vòi phun. "
        "Nguyên lý của chúng dựa trên quan sát của Bernoulli: nếu đặt một chỗ thắt hình vành khuyên "
        "trong đường ống thì vận tốc chất lưu qua chỗ thắt tăng lên; vận tốc tăng làm áp suất tĩnh "
        "tại tiết diện đó giảm xuống, tạo ra chênh áp hai bên phần tử. Chênh lệch giữa áp suất thượng "
        "lưu và hạ lưu của vật cản này liên hệ với lưu lượng chất lưu qua chỗ thắt, và do đó qua "
        "đường ống. Một lưu lượng kế chênh áp gồm hai phần tử cơ bản: một vật cản gây sụt áp "
        "(<b>phần tử tạo chênh áp</b>) và một cách đo sụt áp đó (<b>đầu dò chênh áp</b>)."))
    b.append(p(
        "Một ưu điểm lớn của tấm orifice, ống Venturi hay vòi phun là có thể dự báo độ bất định của "
        "phép đo mà không cần hiệu chuẩn, miễn là thiết bị được chế tạo và lắp đặt theo một trong các "
        "tiêu chuẩn quốc tế áp dụng cho chúng. Ngoài ra loại lưu lượng kế này đơn giản, không có bộ "
        "phận chuyển động nên đáng tin cậy. Nhược điểm chính là dải đo hẹp (điển hình 3:1), tổn thất "
        "áp suất vĩnh viễn trên đường ống (có thể làm tăng chi phí bơm), và nhạy với ảnh hưởng lắp "
        "đặt (có thể giảm thiểu bằng các đoạn ống thẳng trước và sau lưu lượng kế). Tổng hợp các ưu "
        "điểm này vẫn rất khó vượt qua; tuy còn hạn chế nhưng chúng đã được nghiên cứu kỹ và trong "
        "phần lớn tình huống có thể bù được. Trừ khi cần độ chính xác rất cao hoặc ứng dụng buộc "
        "phải dùng thiết bị không xâm nhập, lưu lượng kế chênh áp vẫn nên được xem xét. Bất chấp "
        "những dự báo về sự cáo chung, chắc chắn nó còn là phương pháp đo lưu lượng phổ biến trong "
        "nhiều năm nữa."))

    b.append(h3("Nguyên lý quan trọng của dòng chảy trong ống", "Important Principles of Fluid Flow in Pipes"))
    b.append(p(
        "Có một số nguyên lý cần hiểu trước khi dùng lưu lượng kế chênh áp một cách tin cậy: phân "
        "biệt chảy tầng và chảy rối, ý nghĩa của số Reynolds, và tầm quan trọng của mặt cắt phân bố "
        "vận tốc."))
    b.append(p(
        "Chuyển động của chất lưu trong ống có thể xếp vào ba loại: chảy tầng, chảy quá độ và chảy "
        "rối. Trong <b>chảy tầng</b>, chất lưu di chuyển thành các lớp song song (gọi là đường dòng) "
        "không trộn vào nhau khi đi theo chiều dòng. Nếu chảy rối, chất lưu không đi thành lớp song "
        "song mà chuyển động hỗn loạn, chỉ có chuyển động trung bình là song song với trục ống. Nếu "
        "chảy <b>quá độ</b> thì cả hai loại có thể cùng tồn tại ở những điểm khác nhau trên tuyến, "
        "hoặc dòng có thể chuyển đổi qua lại giữa hai loại."))
    b.append(p(
        "Năm 1883, Osborne Reynolds thực hiện một loạt thí nghiệm kinh điển tại Đại học Manchester, "
        "chứng minh rằng đặc tính dòng chảy dự báo được bằng một số không thứ nguyên, nay gọi là số "
        "Reynolds. Số Reynolds Re là tỉ số giữa lực quán tính trong dòng (ρ v̄ D) và lực nhớt (η):"))
    b.append(eq("Re = ρ v̄ D ⁄ η", "28.1"))
    b.append(p(
        "trong đó ρ là khối lượng riêng của chất lưu, v̄ là vận tốc trung bình, <i>D</i> là đường "
        "kính ống và η là độ nhớt động lực của chất lưu."))
    b.append(p(
        "Nếu Re nhỏ hơn 2000, lực nhớt chiếm ưu thế và dòng là chảy tầng. Nếu Re lớn hơn 4000, lực "
        "quán tính chiếm ưu thế và dòng là chảy rối. Nếu Re nằm giữa 2000 và 4000, dòng là quá độ và "
        "có thể ở một trong hai chế độ. Số Reynolds chủ yếu tính từ tính chất chất lưu, không kể đến "
        "các yếu tố như độ nhám ống, cút và van — những thứ cũng ảnh hưởng tới đặc tính dòng. Tuy "
        "vậy, nó vẫn là chỉ dẫn tốt cho loại dòng có thể gặp trong hầu hết tình huống."))
    b.append(p(
        "Vận tốc chất lưu trên một mặt cắt ống không hằng số mà phụ thuộc loại dòng. Trong chảy tầng, "
        "mặt cắt vận tốc là parabol vì lực nhớt lớn làm chất lưu đi chậm hơn gần thành ống; khi đó "
        "vận tốc ở tâm ống gấp đôi vận tốc trung bình trên mặt cắt. Mặt cắt chảy tầng không phụ thuộc "
        "độ nhám thành ống. Trong chảy rối, lực quán tính chiếm ưu thế, ảnh hưởng thành ống ít hơn và "
        "mặt cắt vận tốc phẳng hơn, với vận tốc ở tâm khoảng 1,2 lần vận tốc trung bình. Mặt cắt "
        "chính xác của dòng rối phụ thuộc độ nhám thành ống và số Reynolds."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Hình 28.1 cho mặt cắt dòng “phát triển đầy đủ” của chảy tầng và chảy rối — tức mặt cắt thu "
        "được ở cuối một ống rất dài, khi mọi thay đổi do cút và phụ kiện đã không còn. Để tin được "
        "vào tính năng của lưu lượng kế chênh áp, cả đặc tính lẫn mặt cắt vận tốc của dòng qua lưu "
        "lượng kế đều phải ổn định và đã biết."))

    b.append(h3("Phương trình Bernoulli", "Bernoulli’s Equation"))
    b.append(p(
        "Phương trình Bernoulli xác lập quan hệ giữa vận tốc <i>v</i>, áp suất <i>p</i> và độ cao "
        "<i>h</i> so với một mốc cố định của chất lưu chảy qua ống có tiết diện thay đổi, và là điểm "
        "xuất phát để hiểu nguyên lý lưu lượng kế chênh áp. Với ống thuôn, đặt nghiêng như Hình "
        "28.2, phương trình Bernoulli phát biểu:"))
    b.append(eq("p₁ ⁄ (ρg) + v₁² ⁄ (2g) + h₁ = p₂ ⁄ (ρg) + v₂² ⁄ (2g) + h₂", "28.2"))
    b.append(p(
        "Như vậy tổng của cột áp (<i>p</i>/ρ<i>g</i>), cột vận tốc (<i>v</i>/2<i>g</i>) và cột vị trí "
        "(<i>h</i>) là hằng số dọc theo một đường dòng. Thuật ngữ “cột” được dùng phổ biến vì mỗi số "
        "hạng đều có đơn vị mét. Phương trình 28.2 giả thiết chất lưu không ma sát (độ nhớt bằng 0) "
        "và có khối lượng riêng không đổi (không nén được). Chi tiết về cách suy ra và ý nghĩa của "
        "phương trình Bernoulli có trong hầu hết sách giáo trình cơ học chất lưu đại học (ví dụ [2])."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Phương trình Bernoulli dùng được để chỉ ra cách một chỗ thắt trong ống đo lưu lượng. Xét "
        "đoạn ống ở Hình 28.3. Vì ống nằm ngang nên <i>h</i>₁ = <i>h</i>₂, và phương trình 28.2 rút "
        "gọn thành:"))
    b.append(eq("(p₁ − p₂) ⁄ ρ = (v₂² − v₁²) ⁄ 2", "28.3"))
    b.append(p("Nguyên lý bảo toàn khối lượng đòi hỏi:"))
    b.append(eq("v₁ A₁ ρ = v₂ A₂ ρ", "28.4"))
    b.append(p("Sắp xếp lại 28.4 và thay <i>v</i>₂ vào 28.3, ta được:"))
    b.append(eq("Q = v₁ A₁ = [A₂ ⁄ √(1 − (A₂ ⁄ A₁)²)] · √(2(p₁ − p₂) ⁄ ρ)", "28.5"))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Điều này cho thấy lưu lượng thể tích <i>Q</i> xác định được bằng cách đo độ giảm áp "
        "(<i>p</i>₁ − <i>p</i>₂) qua chỗ thắt trên đường ống — nguyên lý cơ bản của mọi lưu lượng kế "
        "chênh áp. Phương trình 28.5 có các hạn chế: nó giả thiết chất lưu không nén được (hợp lý với "
        "hầu hết chất lỏng) và không có độ nhớt (cho mặt cắt vận tốc phẳng). Những giả thiết này phải "
        "được bù khi dùng 28.5 cho đo lưu lượng thực tế."))

    b.append(h3("Các lưu lượng kế chênh áp thông dụng", "Common Differential Pressure Flowmeters"))
    b.append(h3("Tấm orifice", "The Orifice Plate"))
    b.append(p(
        "Tấm orifice là loại lưu lượng kế chênh áp đơn giản và rẻ nhất. Nó chỉ là một tấm có khoan "
        "lỗ với kích thước và vị trí xác định, kẹp giữa hai mặt bích trên đường ống (Hình 28.4). "
        "Vận tốc chất lưu tăng khi qua lỗ làm phát sinh sụt áp hai bên tấm. Sau khi qua chỗ thắt, "
        "dòng còn co tiếp cho tới một đường kính nhỏ nhất gọi là vena contracta."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Nếu dùng 28.5 để tính lưu lượng từ độ sụt áp đo được trên tấm orifice thì sẽ có sai số, vì "
        "<i>A</i>₂ đúng ra phải là diện tích vena contracta — đại lượng dĩ nhiên chưa biết. Ngoài ra "
        "rối giữa vena contracta và thành ống gây tổn thất năng lượng mà phương trình không kể đến."))
    b.append(p(
        "Để khắc phục các vấn đề khi áp dụng 28.5 vào thực tế, người ta thêm hai hệ số hiệu chỉnh xác "
        "định bằng thực nghiệm. Sau một vài biến đổi, 28.5 viết được thành:"))
    b.append(eq("Q = [C ⁄ √(1 − β⁴)] · ε · (π ⁄ 4) d² · √(2(p₁ − p₂) ⁄ ρ)", "28.6"))
    b.append(p(
        "trong đó ρ là khối lượng riêng của chất lưu thượng lưu tấm orifice, <i>d</i> là đường kính "
        "lỗ trên tấm, và β = <i>d</i>/<i>D</i> là tỉ số đường kính, với <i>D</i> là đường kính trong "
        "của ống thượng lưu."))
    b.append(p(
        "Hai hệ số thực nghiệm là <i>C</i> — hệ số lưu lượng — và ε — hệ số giãn nở. <i>C</i> chịu "
        "ảnh hưởng của tỉ số đường kính, số Reynolds, độ nhám ống, độ sắc của cạnh vào và vị trí lấy "
        "chênh áp; tuy vậy với hình học cố định, người ta đã chỉ ra rằng <i>C</i> chỉ phụ thuộc số "
        "Reynolds, nên xác định được cho từng ứng dụng. ε dùng để kể đến tính nén được của chất lưu. "
        "Cả <i>C</i> lẫn ε đều xác định được từ công thức và bảng trong các tài liệu được quốc tế "
        "công nhận, gọi là tiêu chuẩn. Các tiêu chuẩn này không chỉ quy định <i>C</i> và ε mà cả "
        "hình học và điều kiện lắp đặt của tấm orifice cạnh vuông, ống Venturi và vòi phun, và thực "
        "chất là cẩm nang thiết kế cho các loại lưu lượng kế chênh áp thông dụng nhất. Khuyến nghị "
        "lắp đặt nhằm bảo đảm trong tiết diện đo của lưu lượng kế tồn tại dòng rối phát triển đầy "
        "đủ. Tiêu chuẩn thông dụng ở châu Âu là ISO 5167-1 [3], còn ở Mỹ là API 2530 [4]. Giữa hai "
        "tiêu chuẩn có những khác biệt (ví dụ chiều dài tối thiểu của đoạn ống thẳng thượng lưu), "
        "nhưng đang có nỗ lực hài hoà chúng."))
    b.append(p(
        "Phương trình 28.6 cho thấy có lẽ ưu điểm lớn nhất của tấm orifice: có thể tin cậy dự báo "
        "tính năng đo mà không cần hiệu chuẩn, nếu thiết bị được chế tạo, lắp đặt và vận hành theo "
        "một tiêu chuẩn quốc tế. Ngoài ra thiết bị rẻ, không có bộ phận chuyển động, đáng tin cậy và "
        "dùng được cho hầu hết khí sạch, chất lỏng và hơi."))
    b.append(p(
        "Nhược điểm chính của tấm orifice là dải đo hẹp và nhạy với nhiễu loạn dòng. Vì lưu lượng tỉ "
        "lệ với căn bậc hai của chênh áp đo được, dải đo của một tổ hợp một tấm / một bộ truyền "
        "chênh áp chỉ khoảng 3:1. Tỉ số đường kính cần thiết (còn gọi là tỉ số beta) phụ thuộc lưu "
        "lượng cực đại cần đo và dải của đầu dò chênh áp sẵn có; việc chọn cỡ tấm orifice được trình "
        "bày trong hầu hết sách trong danh mục đọc thêm, và ngày nay có cả chương trình máy tính hỗ "
        "trợ. Có thể mở rộng dải đo bằng cách chuyển thang; các cách thực hiện được mô tả trong [5]. "
        "Phương trình 28.6 giả thiết mặt cắt dòng phát triển đầy đủ và ổn định, nên việc lắp đặt là "
        "then chốt, đặc biệt là đủ đoạn ống thẳng thượng lưu. Mòn cạnh vào của tấm có thể làm thay "
        "đổi nghiêm trọng độ chính xác, vì vậy thiết bị này thường chỉ dùng với chất lưu sạch."))
    b.append(p(
        "Chỉ một loại tấm orifice — loại cạnh vuông đồng tâm — được các tiêu chuẩn đề cập. Tuy vậy "
        "còn các loại khác, được thiết kế cho ứng dụng riêng. Một ví dụ là tấm orifice lệch tâm, "
        "thích hợp với chất lưu bẩn. Chi tiết các loại khác có trong [6]."))

    b.append(h3("Ống Venturi", "The Venturi Tube"))
    b.append(p(
        "Ống Venturi cổ điển (hay Herschel) là loại lưu lượng kế chênh áp lâu đời nhất, lần đầu dùng "
        "năm 1887. Như Hình 28.5, chỗ thắt được đưa vào dòng một cách từ từ hơn nhiều so với tấm "
        "orifice. Dòng qua ống Venturi vì thế gần với dự báo lý thuyết của 28.5 hơn, nên hệ số lưu "
        "lượng <i>C</i> gần 1 hơn nhiều, điển hình 0,95. Ngoài ra tổn thất áp suất vĩnh viễn của ống "
        "Venturi thấp hơn, nhưng chênh áp cũng thấp hơn so với tấm orifice cùng tỉ số đường kính. "
        "Thiết kế trơn nhẵn khiến ống Venturi ít nhạy với xói mòn hơn tấm orifice, do đó thích hợp "
        "hơn với khí hoặc chất lỏng bẩn. Nó cũng ít nhạy với nhiễu thượng lưu nên cần đoạn ống thẳng "
        "thượng lưu ngắn hơn tấm orifice hay vòi phun tương đương. Như với tấm orifice và vòi phun, "
        "thiết kế, lắp đặt và sử dụng ống Venturi được nhiều tiêu chuẩn quốc tế đề cập."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Nhược điểm chính của ống Venturi là kích thước và giá thành. Nó khó chế tạo hơn và do đó "
        "đắt hơn tấm orifice. Vì ống Venturi điển hình dài cỡ 6 đường kính, với cỡ ống lớn nó trở "
        "nên cồng kềnh, kéo theo việc duy trì các đoạn ống thượng và hạ lưu cũng thành vấn đề."))

    b.append(h3("Vòi phun", "The Nozzle"))
    b.append(p(
        "Vòi phun (Hình 28.6) kết hợp một số ưu điểm tốt nhất của tấm orifice và ống Venturi. Nó gọn, "
        "mà nhờ miệng vào cong lại có hệ số lưu lượng gần 1. Có nhiều kiểu vòi phun; loại thông dụng "
        "nhất ở châu Âu là vòi phun ISA-1932, còn ở Mỹ là vòi phun bán kính dài ASME. Cả hai đều "
        "được các tiêu chuẩn quốc tế đề cập."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Miệng vào trơn nhẵn khiến vòi phun đắt hơn tấm orifice vì độ cong của miệng vào thay đổi "
        "theo tỉ số đường kính, tuy vẫn rẻ hơn ống Venturi. Thiết bị không có cạnh sắc để bị xói mòn "
        "và làm lệch chuẩn, nên rất hợp với chất lưu bẩn và mài mòn. Vòi phun cũng thường dùng cho "
        "ứng dụng vận tốc cao, nhiệt độ cao như đo hơi nước."))
    b.append(p(
        "Một biến thể của vòi phun là vòi phun tới hạn (hay vòi phun Venturi dòng tới hạn), được dùng "
        "cả làm chuẩn hiệu chuẩn để kiểm tra lưu lượng kế khí lẫn làm chuẩn chuyển giao trong so sánh "
        "liên phòng thí nghiệm [7]."))

    b.append(h3("Các lưu lượng kế chênh áp khác", "Other Differential Pressure Flowmeters"))
    b.append(p(
        "Còn nhiều loại lưu lượng kế chênh áp khác, gồm nêm phân đoạn, V-cone, khuỷu và ống Dall. "
        "Mỗi loại có ưu điểm riêng so với tấm orifice, ống Venturi và vòi phun trong những ứng dụng "
        "cụ thể. Ví dụ nêm phân đoạn dùng được với dòng có số Reynolds thấp, và ống Dall có tổn thất "
        "áp suất vĩnh viễn thấp hơn ống Venturi. Tuy vậy chưa loại nào được tiêu chuẩn quốc tế đề "
        "cập, nên phải hiệu chuẩn mới xác định được độ chính xác. Thông tin thêm về những loại này "
        "và các loại ít gặp khác có trong [8]."))

    b.append(h3("Tính năng và ứng dụng", "Performance and Applications"))
    b.append(p(
        "Bảng 28.1 trình bày đặc tính tính năng và vùng ứng dụng chính của tấm orifice cạnh vuông, "
        "ống Venturi và vòi phun. So với các loại lưu lượng kế khác trên thị trường, các lưu lượng kế "
        "chênh áp này chỉ có độ chính xác trung bình, điển hình ±2 % giá trị đọc; dĩ nhiên có thể cải "
        "thiện nếu hiệu chuẩn sau khi lắp. Tuy trong một số tình huống chúng dùng được với khí hoặc "
        "chất lỏng bẩn, thường chỉ chịu được một lượng nhỏ thành phần thứ hai trước khi sai số đo trở "
        "nên lớn. Khi tính chi phí và tính năng của một lưu lượng kế chênh áp phải kể cả phần tử sơ "
        "cấp lẫn đầu dò chênh áp. Dù tấm orifice là phần tử sơ cấp rẻ nhất, chi phí phụ kiện để gắn "
        "nó vào đường ống — nhất là khi cần tháo ra trong lúc đang vận hành — có thể đáng kể."))
    b.append(table(*_t281("vi")))
    b.append(p(
        "Chọn lưu lượng kế nào tốt nhất cho một ứng dụng cụ thể có thể rất khó. Các yếu tố chính ảnh "
        "hưởng là tính năng yêu cầu, tính chất chất lưu cần đo, yêu cầu lắp đặt, môi trường sử dụng "
        "và dĩ nhiên là giá thành. Có hai tiêu chuẩn hỗ trợ chọn lưu lượng kế: BS 1042 mục 1.4 — "
        "hướng dẫn dùng các lưu lượng kế chênh áp tiêu chuẩn [9]; và BS 7405 — nguyên tắc rộng hơn về "
        "chọn lưu lượng kế [10]."))
    b.append(p(
        "Vì cả ba loại có độ chính xác tương đương, một cách chọn là xét xem có lý do chính đáng nào "
        "để không dùng lưu lượng kế rẻ nhất và dùng được với dải cỡ ống rộng nhất — tấm orifice. Khi "
        "tổn thất áp suất vĩnh viễn là quan trọng thì nên xét ống Venturi, dù giá cao của nó thường "
        "chỉ hợp lý khi đo lưu lượng lớn. Với ứng dụng nhiệt độ cao hoặc vận tốc cao nên xét vòi "
        "phun, vì trong điều kiện đó nó dự báo được tốt hơn tấm orifice. Với chất lưu bẩn nên xét ống "
        "Venturi hoặc vòi phun thay cho tấm orifice, việc chọn giữa hai loại tuỳ giá thành và yêu cầu "
        "tổn thất áp suất."))
    b.append(table(*_t282("vi")))

    b.append(h3("Lắp đặt", "Installation"))
    b.append(p(
        "Lắp đặt đúng là điều kiện thiết yếu để dùng tốt lưu lượng kế chênh áp, vì độ bất định dự báo "
        "trong quan hệ lưu lượng – chênh áp ở 28.6 giả thiết một dòng ổn định có mặt cắt vận tốc rối "
        "phát triển đầy đủ đi qua lưu lượng kế. Các tiêu chuẩn có khuyến nghị chi tiết về chiều dài "
        "ống thẳng tối thiểu trước và sau lưu lượng kế để bảo đảm mặt cắt dòng phát triển đầy đủ. Cần "
        "đoạn ống thẳng sau lưu lượng kế vì nhiễu do một van hay cút có thể lan ngược lên thượng lưu "
        "và cũng ảnh hưởng tới lưu lượng kế đã lắp. Bảng 28.3 nêu ví dụ yêu cầu lắp đặt lấy từ ISO "
        "5167-1. Nếu không thể bố trí đủ chiều dài ống thẳng trước và sau lưu lượng kế thì phải hiệu "
        "chuẩn lưu lượng kế tại chỗ sau khi lắp."))
    b.append(table(*_t283("vi")))
    b.append(p(
        "Vấn đề lớn khác khi lắp đặt là sự có mặt của dòng xoáy. Tình trạng này làm méo mặt cắt vận "
        "tốc một cách rất khó dự báo và dĩ nhiên là không mong muốn. Nên tránh những tình huống tạo "
        "xoáy, như hai cút 90° trong các mặt phẳng khác nhau. Nếu không tránh được thì có thể khử xoáy "
        "bằng cách đặt một bộ điều hoà dòng (còn gọi là bộ nắn thẳng dòng) giữa nguồn xoáy và lưu "
        "lượng kế. Có rất nhiều kiểu điều hoà dòng, một số vừa khử xoáy vừa chỉnh lại mặt cắt vận "
        "tốc bị méo [11]. Vì cản trở dòng, mọi bộ điều hoà dòng đều gây tổn thất áp suất không phục "
        "hồi được, và nói chung tổn thất này tăng theo năng lực (và độ phức tạp) của bộ."))

    b.append(h3("Đo chênh áp", "Differential Pressure Measurement"))
    b.append(p(
        "Ngoài phần tử tạo chênh áp, phần tử chính khác của lưu lượng kế chênh áp là đầu dò đo sụt áp "
        "qua phần tử đó. Chọn và lắp đặt đúng đầu dò chênh áp góp phần quan trọng quyết định độ chính "
        "xác của phép đo lưu lượng."))
    b.append(p(
        "Các yếu tố chính cần xét khi chọn đầu dò chênh áp cho một ứng dụng đo lưu lượng là dải chênh "
        "áp cần bao, độ chính xác yêu cầu, áp suất cực đại của đường ống, và loại cùng dải nhiệt độ "
        "của chất lưu cần đo."))
    b.append(p(
        "Hầu hết đầu dò chênh áp hiện đại gồm một capsule áp trong đó dùng kỹ thuật điện dung, tenzơ "
        "hay dây cộng hưởng để phát hiện dịch chuyển của màng. Với các kỹ thuật này, độ chính xác "
        "điển hình ±0,1 % toàn thang đo là khả thi; xem Chương 26, Mục 1 để biết thêm về đầu dò áp "
        "suất. Đầu dò thường là một phần của bộ gọi là bộ truyền (transmitter), chuyển các phép đo "
        "chênh áp, áp tĩnh và nhiệt độ môi trường thành tín hiệu ra tương tự hoặc số được chuẩn hoá. "
        "Bộ truyền “thông minh” dùng một vi xử lý cục bộ để điều chế tín hiệu từ từng cảm biến và "
        "tính lưu lượng thể tích hoặc khối lượng. Những thiết bị này cấu hình được từ xa, và nhờ “trí "
        "tuệ” tích hợp mà có nhiều chức năng chẩn đoán và bảo trì."))
    b.append(p(
        "Về lắp đặt, bộ truyền nên đặt càng gần phần tử tạo chênh áp càng tốt; điều này giúp đáp ứng "
        "động nhanh và giảm vấn đề do rung của ống nối. Vị trí điểm lấy áp cũng quan trọng. Nếu đo "
        "dòng chất lỏng trong ống ngang thì điểm lấy áp nên ở bên hông ống để không bị bẩn bít hay "
        "đọng bọt khí. Với dòng khí ngang, nếu khí sạch thì điểm lấy áp nên đặt thẳng đứng; nếu đo "
        "hơi hoặc khí bẩn thì điểm lấy áp nên ở bên hông ống. Những hướng dẫn chung này cho thấy phải "
        "hết sức cẩn thận khi lắp bộ truyền chênh áp nếu muốn tránh sai số lớn. Chi tiết thêm về lắp "
        "đặt bộ truyền chênh áp xem ISO 2186 [12]."))

    b.append(h3("Tiêu chuẩn", "Standards"))
    b.append(p(
        "Các tiêu chuẩn quốc tế quy định thiết kế, lắp đặt và sử dụng tấm orifice, ống Venturi và vòi "
        "phun, đồng thời cho phép tính độ chính xác mà không cần hiệu chuẩn, có lẽ là lý do chính "
        "khiến loại lưu lượng kế này vẫn được dùng. Bảng 28.4 nêu chi tiết các tiêu chuẩn thông dụng "
        "nhất liên quan đến lưu lượng kế chênh áp. Giữa các tiêu chuẩn vẫn còn những điểm không nhất "
        "quán. Ví dụ ISO 5167-1 nói rằng trước một bộ điều hoà dòng phải có ít nhất 22 đường kính ống "
        "thẳng và sau nó ít nhất 20 đường kính — điều này dường như mâu thuẫn với một công dụng của "
        "bộ điều hoà dòng là rút ngắn đoạn ống thẳng cần có thượng lưu lưu lượng kế."))
    b.append(table(*_t284("vi")))
    b.append(p(
        "Bất chấp những điểm không nhất quán và khác biệt thỉnh thoảng gặp, các tiêu chuẩn này là "
        "những quy tắc được quốc tế chấp nhận để lắp đặt và sử dụng tấm orifice cạnh vuông, ống "
        "Venturi và vòi phun."))

    b.append(h3("Phát triển tương lai", "Future Developments"))
    b.append(p(
        "Dù đã có rất nhiều dữ liệu công bố về lưu lượng kế chênh áp, vẫn cần nghiên cứu tiếp để hiểu "
        "rõ hơn ảnh hưởng của điều kiện dòng và hình học lưu lượng kế lên độ chính xác khi chưa hiệu "
        "chuẩn. Ví dụ, gần đây đã có công trình nhằm xây dựng một công thức cải tiến cho hệ số lưu "
        "lượng của tấm orifice [13]."))
    b.append(p(
        "Đo lưu lượng đa pha là lĩnh vực ngày càng quan trọng. Ngoài việc phát triển kỹ thuật đo mới, "
        "nhiều người đang tìm cách dùng lưu lượng kế truyền thống để đo dòng đa pha; xem [14] để có "
        "tổng quan tốt về việc dùng lưu lượng kế chênh áp cho đo đa pha."))
    b.append(p(
        "Sự phát triển của bộ truyền chênh áp “thông minh” đã khắc phục hạn chế của lưu lượng kế "
        "chênh áp trong một số ứng dụng — ví dụ chúng được dùng để tuyến tính hoá và mở rộng dải đo. "
        "Những tiến bộ trên sẽ giúp bảo đảm lưu lượng kế chênh áp còn phổ biến trong thời gian tới, "
        "bất chấp cạnh tranh ngày càng tăng từ các loại thiết bị mới."))

    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(defs([
        ("Lưu lượng kế chênh áp",
         "Lưu lượng kế dùng độ sụt áp qua một chỗ thắt hình vành khuyên đặt trên đường ống để đo lưu "
         "lượng. Các loại thông dụng dùng tấm orifice, ống Venturi hoặc vòi phun làm phần tử sơ cấp."),
        ("Tấm orifice",
         "Phần tử sơ cấp gồm một tấm mỏng khoan một lỗ tròn."),
        ("Ống Venturi",
         "Phần tử sơ cấp gồm miệng vào thu dần, đoạn giữa hình trụ và miệng ra loe dần."),
        ("Vòi phun",
         "Phần tử sơ cấp gồm miệng vào thu dần nối với một đoạn hình trụ."),
        ("Bộ truyền chênh áp",
         "Phần tử thứ cấp đo chênh áp qua phần tử sơ cấp và chuyển thành tín hiệu điện."),
    ]))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "1. R. A. Furness, Flowmetering: evolution or revolution, <i>Measurement and Control</i>, "
        "27 (8), 15–18, 1994.",
        "2. B. S. Massey, <i>Mechanics of Fluids</i>, 6th ed., London: Chapman and Hall, 1989.",
        "3. ISO 5167-1, <i>Measurement of Fluid Flow by Means of Pressure Differential Devices — "
        "Part 1: Orifice plates, nozzles and Venturi tubes inserted in circular cross-section "
        "conduits running full</i>, Geneva, 1991.",
        "4. API 2530, <i>Manual of Petroleum Measurement Standards, Chapter 14 — Natural Gas Fluids "
        "Measurement, Section 3 — Orifice Metering of Natural Gas and Other Related Hydrocarbon "
        "Fluids</i>, Washington, 1985.",
        "5. E. L. Upp, <i>Fluid Flow Measurement</i>, Houston: Gulf Publishing, 1993.",
        "6. H. S. Bean, <i>Fluid Meters: Their Theory and Application</i>, 6th ed., New York: ASME, 1983.",
        "7. P. H. Wright, The application of sonic (critical flow) nozzles in the gas industry, "
        "<i>Flow Meas. Instrum.</i>, 4 (2), 67–71, 1993.",
        "8. D. W. Spitzer, <i>Industrial Flow Measurement</i>, 2nd ed., Research Triangle Park, NC: "
        "ISA, 1990.",
        "9. BS 1042, <i>Measurement of Fluid Flow in Closed Conduits — Part 1: Pressure differential "
        "devices — Section 1.4: Guide to the use of devices specified in Sections 1.1 and 1.2</i>, "
        "London, 1992.",
        "10. BS 7405, <i>Guide to the Selection and Application of Flowmeters for Measurement of "
        "Fluid Flow in Closed Conduits</i>, London, 1991.",
        "11. E. M. Laws and A. K. Ouazzane, Compact installations for differential pressure flow "
        "measurement, <i>Flow Meas. Instrum.</i>, 5 (2), 79–85, 1994.",
        "12. ISO 2186, <i>Fluid Flow in Closed Conduits — Connections for Pressure Signal "
        "Transmissions Between Primary and Secondary Elements</i>, Geneva, 1973.",
        "13. M. J. Reader-Harris, J. A. Slattery and E. P. Spearman, The orifice plate discharge "
        "coefficient equation — further work, <i>Flow Meas. Instrum.</i>, 6 (2), 101–114, 1995.",
        "14. F. C. Kinghorn, Two-phase flow measurement using differential pressure meters, "
        "<i>Multi-Phase Flow Measurement Short Course</i>, London, 17–18 June 1985.",
    ]))
    return "".join(b)


def sec_28_1_en():
    b = []
    b.append(h2("28.1 Differential Pressure Flowmeters", "Lưu lượng kế chênh áp"))
    b.append(p("Richard Thorn — University of Derby."))
    b.append(p(
        "Flow measurement is an everyday event. Whether you are filling a car with petrol or wanting "
        "to know how much water the garden sprinkler is consuming, a flowmeter is required. It is "
        "equally hard to think of an industrial sector in which a flowmeter of one type or another "
        "plays no part. The world market in flowmeters was estimated at $2,500 million in 1995 and is "
        "expected to grow steadily for the foreseeable future. The value of the product measured is "
        "also very large: in the U.K. alone the crude oil produced in 1994 was worth an estimated "
        "$15 billion."))
    b.append(p(
        "Given that size, it is somewhat surprising that the accuracy and capability of many "
        "flowmeters are poor compared with instruments used for other common process variables such "
        "as pressure and temperature. The orifice plate flowmeter, first used commercially in the "
        "early 1900s and typically accurate to ±2 % of reading, is still the only flowmeter approved "
        "by most countries for fiscal measurement of natural gas. Although newer techniques such as "
        "Coriolis meters have become increasingly popular, the industry is conservative and still "
        "dominated by traditional techniques; see [1] for a review of recent developments."))
    b.append(p(
        "Over 40 % of all liquid, gas and steam measurements in industry are still made with the "
        "common <b>differential pressure flowmeters</b>: the orifice plate, Venturi tube and nozzle. "
        "Their operation rests on Bernoulli's observation that if an annular restriction is placed in "
        "a pipeline the velocity through the restriction increases; the increase lowers the static "
        "pressure at that section and creates a pressure difference across the element. The "
        "difference between upstream and downstream pressure is related to the rate of flow through "
        "the restriction, and therefore through the pipe. A differential pressure flowmeter has two "
        "basic elements: an obstruction causing the pressure drop (a <b>differential producer</b>) and "
        "a means of measuring that drop (a <b>differential pressure transducer</b>)."))
    b.append(p(
        "One major advantage of the orifice plate, Venturi tube or nozzle is that the measurement "
        "uncertainty can be predicted without calibration, provided the device is manufactured and "
        "installed in accordance with one of the international standards covering it. The device is "
        "also simple, has no moving parts and is therefore reliable. The main disadvantages are the "
        "limited range (typically 3:1), the permanent pressure drop in the pipeline (which can raise "
        "pumping costs), and sensitivity to installation effects (minimized by straight lengths of "
        "pipe before and after the meter). The combination of advantages is still hard to beat, and "
        "the limitations have been well investigated and can mostly be compensated. Unless very high "
        "accuracy is needed, or a nonintrusive device is essential, the differential flowmeter should "
        "be considered. Despite predictions of its demise it will remain a common method for many "
        "years."))

    b.append(h3("Important Principles of Fluid Flow in Pipes", "Nguyên lý quan trọng của dòng chảy trong ống"))
    b.append(p(
        "Several principles must be understood before a differential pressure flowmeter can be used "
        "with confidence: the difference between laminar and turbulent flow, the meaning of Reynolds "
        "number, and the importance of the velocity profile."))
    b.append(p(
        "Fluid motion in a pipe is laminar, transitional or turbulent. In <b>laminar flow</b> the "
        "fluid travels as parallel layers (streamlines) that do not mix as they move along. In "
        "turbulent flow the fluid does not travel in parallel layers but moves haphazardly, only the "
        "average motion being parallel to the pipe axis. In <b>transitional</b> flow both types may "
        "be present at different points, or the flow may switch between them."))
    b.append(p(
        "In 1883 Osborne Reynolds showed at the University of Manchester that the flow character can "
        "be predicted with a dimensionless number, now the Reynolds number: the ratio of inertia "
        "forces (ρ v̄ D) to viscous forces (η)."))
    b.append(eq("Re = ρ v̄ D ⁄ η", "28.1"))
    b.append(p(
        "where ρ is the fluid density, v̄ the mean velocity, <i>D</i> the pipe diameter and η the "
        "dynamic viscosity."))
    b.append(p(
        "Below Re = 2000 viscous forces dominate and the flow is laminar; above 4000 inertia forces "
        "dominate and it is turbulent; between 2000 and 4000 the flow is transitional and either mode "
        "may be present. The number is computed mainly from fluid properties and ignores pipe "
        "roughness, bends and valves, which also affect the flow, but it remains a good guide in most "
        "situations."))
    b.append(p(
        "Velocity across a pipe section is not constant. In laminar flow the profile is parabolic, "
        "because large viscous forces slow the fluid near the walls; the velocity at the centre is "
        "twice the average, and the profile is unaffected by wall roughness. In turbulent flow "
        "inertia dominates, wall effects are less, and the profile is flatter, with the centre "
        "velocity about 1.2 times the mean; the exact profile depends on wall roughness and Reynolds "
        "number."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Figure 28.1 shows the fully developed profiles for laminar and turbulent flow — those "
        "obtained at the end of a very long pipe, where changes due to bends and fittings have "
        "disappeared. For confidence in a differential pressure flowmeter, both the character and the "
        "velocity profile of the flow through it must be stable and known."))

    b.append(h3("Bernoulli’s Equation", "Phương trình Bernoulli"))
    b.append(p(
        "The Bernoulli equation relates fluid velocity <i>v</i>, pressure <i>p</i> and height "
        "<i>h</i> above a fixed point for flow through a pipe of varying cross-section, and is the "
        "starting point for the differential pressure flowmeter. For the inclined, tapered pipe of "
        "Figure 28.2:"))
    b.append(eq("p₁ ⁄ (ρg) + v₁² ⁄ (2g) + h₁ = p₂ ⁄ (ρg) + v₂² ⁄ (2g) + h₂", "28.2"))
    b.append(p(
        "The sum of pressure head (<i>p</i>/ρ<i>g</i>), velocity head (<i>v</i>/2<i>g</i>) and "
        "potential head (<i>h</i>) is constant along a streamline. The term “head” is used because "
        "each has the unit of metres. Equation 28.2 assumes a frictionless fluid of constant density; "
        "derivations are in any undergraduate fluid dynamics text (e.g. [2])."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "The equation shows how a restriction can measure flow rate. For the section of Figure 28.3 "
        "the pipe is horizontal, so <i>h</i>₁ = <i>h</i>₂ and 28.2 reduces to:"))
    b.append(eq("(p₁ − p₂) ⁄ ρ = (v₂² − v₁²) ⁄ 2", "28.3"))
    b.append(p("Conservation of mass requires:"))
    b.append(eq("v₁ A₁ ρ = v₂ A₂ ρ", "28.4"))
    b.append(p("Rearranging 28.4 and substituting for <i>v</i>₂ in 28.3:"))
    b.append(eq("Q = v₁ A₁ = [A₂ ⁄ √(1 − (A₂ ⁄ A₁)²)] · √(2(p₁ − p₂) ⁄ ρ)", "28.5"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "The volumetric flow rate <i>Q</i> therefore follows from the pressure drop across the "
        "restriction — the basic principle of every differential pressure flowmeter. Equation 28.5 "
        "has limitations: the fluid is assumed incompressible (reasonable for most liquids) and "
        "inviscid (giving a flat profile). Both assumptions must be compensated in practical "
        "measurement."))

    b.append(h3("Common Differential Pressure Flowmeters", "Các lưu lượng kế chênh áp thông dụng"))
    b.append(h3("The Orifice Plate", "Tấm orifice"))
    b.append(p(
        "The orifice plate is the simplest and cheapest differential pressure flowmeter: a plate with "
        "a hole of specified size and position, clamped between flanges (Figure 28.4). The rise in "
        "velocity through the hole develops a pressure drop across the plate. Downstream the jet "
        "keeps contracting to a minimum diameter, the vena contracta."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Using 28.5 on the measured drop would give an error, because <i>A</i>₂ should strictly be "
        "the vena contracta area, which is unknown. Turbulence between the vena contracta and the "
        "wall also causes an energy loss the equation ignores."))
    b.append(p(
        "Two empirically determined correction factors are therefore added. After some "
        "reorganization 28.5 becomes:"))
    b.append(eq("Q = [C ⁄ √(1 − β⁴)] · ε · (π ⁄ 4) d² · √(2(p₁ − p₂) ⁄ ρ)", "28.6"))
    b.append(p(
        "where ρ is the density upstream of the plate, <i>d</i> the hole diameter, and β = "
        "<i>d</i>/<i>D</i> the diameter ratio with <i>D</i> the upstream internal pipe diameter."))
    b.append(p(
        "The two factors are <i>C</i>, the discharge coefficient, and ε, the expansibility factor. "
        "<i>C</i> depends on diameter ratio, Reynolds number, pipe roughness, the sharpness of the "
        "leading edge and the tapping positions; for a fixed geometry it has been shown to depend "
        "only on Reynolds number, so it can be determined for a given application. ε accounts for "
        "compressibility. Both come from equations and tables in internationally recognized "
        "standards, which specify not only <i>C</i> and ε but the geometry and installation "
        "conditions for the square-edged orifice plate, Venturi tube and nozzle — effectively a "
        "design guide for the commonest differential pressure meters. Installation recommendations "
        "aim to ensure fully developed turbulent flow in the measurement section. The commonest "
        "standard in Europe is ISO 5167-1 [3]; in the U.S., API 2530 [4]. The two differ in places "
        "(for example the minimum upstream straight length), and work is under way to resolve this."))
    b.append(p(
        "Equation 28.6 illustrates perhaps the greatest strength of the orifice plate: performance "
        "can be predicted without calibration if the device is manufactured, installed and operated "
        "to a standard. It is also cheap, has no moving parts, is reliable, and meters most clean "
        "gases, liquids and steam."))
    b.append(p(
        "Its main disadvantages are limited range and sensitivity to flow disturbance. Because flow "
        "rate goes as the square root of the measured drop, one plate with one transmitter covers "
        "only about 3:1. The required diameter (beta) ratio depends on the maximum flow and the range "
        "of the available transducer; sizing is covered in most of the further reading, and computer "
        "programs are available. Range can be extended by switching, as described in [5]. Equation "
        "28.6 assumes a fully developed, stable profile, so installation is critical — particularly "
        "sufficient upstream straight pipe. Wear of the leading edge can severely alter accuracy, so "
        "the device is normally used only with clean fluids."))
    b.append(p(
        "Only the square-edged concentric plate is covered by the standards; other types exist for "
        "specific applications. One example is the eccentric orifice plate, suited to dirty fluids. "
        "Details are in [6]."))

    b.append(h3("The Venturi Tube", "Ống Venturi"))
    b.append(p(
        "The classical or Herschel Venturi tube is the oldest differential pressure flowmeter, first "
        "used in 1887. As Figure 28.5 shows, the restriction is introduced far more gradually than an "
        "orifice plate. The flow is closer to that predicted by 28.5, so the discharge coefficient is "
        "much nearer unity, typically 0.95. The permanent pressure loss is lower, but so is the "
        "differential pressure for the same diameter ratio. The smooth design makes it less sensitive "
        "to erosion and therefore better suited to dirty gases or liquids, and less sensitive to "
        "upstream disturbance, so it needs shorter upstream straight lengths than an equivalent "
        "orifice plate or nozzle. Design, installation and use are covered by international "
        "standards."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Its main disadvantages are size and cost. It is harder and therefore more expensive to "
        "manufacture than an orifice plate, and being typically six diameters long it becomes "
        "cumbersome in larger pipe sizes, with the associated maintenance of upstream and downstream "
        "lengths also a problem."))

    b.append(h3("The Nozzle", "Vòi phun"))
    b.append(p(
        "The nozzle (Figure 28.6) combines some of the best features of the orifice plate and the "
        "Venturi tube. It is compact and, because of its curved inlet, has a discharge coefficient "
        "close to unity. Several designs exist; the commonest in Europe is the ISA-1932 nozzle, "
        "while in the U.S. the ASME long radius nozzle is more popular. Both are covered by "
        "international standards."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "The smooth inlet makes the nozzle more expensive than an orifice plate, since the inlet "
        "curvature changes with diameter ratio, though it is cheaper than a Venturi tube. There are "
        "no sharp edges to erode and shift the calibration, so it suits dirty and abrasive fluids, "
        "and it is commonly used for high-velocity, high-temperature duty such as steam metering."))
    b.append(p(
        "A variation is the sonic (critical flow Venturi) nozzle, used both as a calibration standard "
        "for testing gas meters and as a transfer standard in interlaboratory comparisons [7]."))

    b.append(h3("Other Differential Pressure Flowmeters", "Các lưu lượng kế chênh áp khác"))
    b.append(p(
        "Many other types exist, including the segmental wedge, V-cone, elbow and Dall tube, each "
        "with advantages over the orifice plate, Venturi tube and nozzle for specific applications. "
        "The segmental wedge, for example, handles low Reynolds number flows, and a Dall tube has a "
        "lower permanent loss than a Venturi. None is yet covered by international standards, so "
        "calibration is needed to establish accuracy. Further information is in [8]."))

    b.append(h3("Performance and Applications", "Tính năng và ứng dụng"))
    b.append(p(
        "Table 28.1 gives the performance and main application areas of the square-edged orifice "
        "plate, Venturi tube and nozzle. Against other meters on the market these are only moderately "
        "accurate, typically ±2 % of reading, though calibrating after installation improves this. "
        "Although they can sometimes handle dirty gases or liquids, usually only small amounts of a "
        "second component can be tolerated before large errors appear. When costing a differential "
        "pressure flowmeter both the primary element and the transmitter must be counted; the orifice "
        "plate is the cheapest primary element, but the fitting needed to mount it — particularly if "
        "on-line removal is required — can be significant."))
    b.append(table(*_t281("en")))
    b.append(p(
        "Choosing the best meter for a given application can be very difficult. The main factors are "
        "the required performance, the properties of the fluid, the installation requirements, the "
        "environment and, of course, cost. Two standards help: BS 1042 Section 1.4, a guide to the "
        "standard differential pressure flowmeters [9], and BS 7405 on the wider principles of "
        "flowmeter selection [10]."))
    b.append(p(
        "Since all three have similar accuracy, one strategy is to ask whether there is any good "
        "reason not to use the cheapest meter that covers the widest range of pipe sizes — the "
        "orifice plate. Where permanent pressure loss matters the Venturi tube should be considered, "
        "though its high cost is usually only justified for large quantities. For high-temperature or "
        "high-velocity duty the nozzle should be considered, being more predictable than the plate "
        "there. For dirty fluids either the Venturi tube or the nozzle should be preferred, the "
        "choice between them depending on cost and pressure-loss requirements."))
    b.append(table(*_t282("en")))

    b.append(h3("Installation", "Lắp đặt"))
    b.append(p(
        "Correct installation is essential, because the predicted uncertainty of 28.6 assumes a "
        "steady flow with a fully developed turbulent profile through the meter. Standards contain "
        "detailed recommendations for minimum straight lengths before and after the meter; lengths "
        "are needed downstream too because disturbances from a valve or bend can travel upstream and "
        "affect the installed meter. Table 28.3 gives examples taken from ISO 5167-1. If the "
        "recommended lengths cannot be fitted, the meter must be calibrated once installed."))
    b.append(table(*_t283("en")))
    b.append(p(
        "The other major installation problem is a rotating flow, or swirl. It distorts the velocity "
        "profile unpredictably and is obviously undesirable. Situations that create swirl, such as "
        "two 90° bends in different planes, should be avoided; if that is impossible, a flow "
        "conditioner (flow straightener) between the source of swirl and the meter will remove it. "
        "Many designs exist, some of which both remove swirl and correct a distorted profile [11]. "
        "Because they obstruct the flow, all conditioners produce an unrecoverable pressure loss, "
        "which generally grows with their capability and complexity."))

    b.append(h3("Differential Pressure Measurement", "Đo chênh áp"))
    b.append(p(
        "Apart from the producer, the other main element is the transducer measuring the drop across "
        "it. Correct selection and installation of the transducer plays an important part in "
        "determining the accuracy of the flow measurement."))
    b.append(p(
        "The main factors to consider are the differential pressure range, the accuracy required, the "
        "maximum pipeline pressure, and the type and temperature range of the fluid."))
    b.append(p(
        "Most modern transducers consist of a pressure capsule in which capacitance, strain gage or "
        "resonant wire techniques detect the movement of a diaphragm, giving a typical accuracy of "
        "±0.1 % of full scale; see Chapter 26, Section 1 for pressure transducers. The transducer is "
        "usually part of a transmitter, which converts differential pressure, static pressure and "
        "ambient temperature into a standardized analog or digital output. “Smart” transmitters use a "
        "local microprocessor to condition the sensor signals and compute volumetric or mass flow; "
        "they can be configured remotely and offer a wide range of diagnostic and maintenance "
        "functions."))
    b.append(p(
        "The transmitter should sit as close to the producer as possible, which helps dynamic "
        "response and reduces problems from vibrating impulse lines. Tapping position also matters. "
        "For liquid in a horizontal pipe the tappings should be at the side, so they cannot be "
        "blocked by dirt or filled with air bubbles. For horizontal gas flow, vertical tappings suit "
        "clean gas; for steam or dirty gas they should be at the side. These guidelines show that "
        "considerable care is needed if large errors are to be avoided; see ISO 2186 [12]."))

    b.append(h3("Standards", "Tiêu chuẩn"))
    b.append(p(
        "The international standards specifying design, installation and use of the orifice plate, "
        "Venturi tube and nozzle — and allowing accuracy to be calculated without calibration — are "
        "probably the main reason this type of meter is still used. Table 28.4 details the commonest. "
        "Inconsistencies remain: ISO 5167-1, for instance, states that any flow conditioner should be "
        "preceded by at least 22 diameters of straight pipe and followed by at least 20, which seems "
        "to contradict one purpose of a conditioner — reducing the upstream straight length needed."))
    b.append(table(*_t284("en")))
    b.append(p(
        "Despite the occasional inconsistency, the standards are the internationally accepted rules "
        "for installing and using the square-edged orifice plate, Venturi tube and nozzle."))

    b.append(h3("Future Developments", "Phát triển tương lai"))
    b.append(p(
        "Despite the vast published data on differential pressure flowmeters, research continues into "
        "the effect of flow conditions and meter geometry on uncalibrated accuracy — work has recently "
        "been done on an improved discharge-coefficient equation for the orifice plate [13]."))
    b.append(p(
        "Multiphase metering is of increasing importance. Besides new techniques, many are "
        "investigating how traditional meters can handle multiphase flow; a good review of "
        "differential pressure meters for this duty is in [14]."))
    b.append(p(
        "“Smart” differential pressure transmitters have overcome the limitations of these meters in "
        "some applications — being used, for example, to linearize and extend their range. These "
        "developments should ensure the continued popularity of the differential pressure flowmeter, "
        "despite competition from newer instruments."))

    b.append(h3("Defining Terms", "Định nghĩa thuật ngữ"))
    b.append(defs([
        ("Differential pressure flowmeter",
         "A flowmeter in which the pressure drop across an annular restriction in the pipeline "
         "measures the flow rate. The commonest use an orifice plate, Venturi tube or nozzle as the "
         "primary device."),
        ("Orifice plate",
         "Primary device consisting of a thin plate with a circular aperture cut in it."),
        ("Venturi tube",
         "Primary device consisting of a converging inlet, a cylindrical mid-section and a diverging "
         "outlet."),
        ("Nozzle",
         "Primary device consisting of a convergent inlet connected to a cylindrical section."),
        ("Differential pressure transmitter",
         "Secondary device that measures the differential pressure across the primary device and "
         "converts it into an electrical signal."),
    ]))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "1. R. A. Furness, Flowmetering: evolution or revolution, <i>Measurement and Control</i>, "
        "27 (8), 15–18, 1994.",
        "2. B. S. Massey, <i>Mechanics of Fluids</i>, 6th ed., London: Chapman and Hall, 1989.",
        "3. ISO 5167-1, <i>Measurement of Fluid Flow by Means of Pressure Differential Devices — "
        "Part 1</i>, Geneva, 1991.",
        "4. API 2530, <i>Manual of Petroleum Measurement Standards, Chapter 14, Section 3</i>, "
        "Washington, 1985.",
        "5. E. L. Upp, <i>Fluid Flow Measurement</i>, Houston: Gulf Publishing, 1993.",
        "6. H. S. Bean, <i>Fluid Meters: Their Theory and Application</i>, 6th ed., New York: ASME, 1983.",
        "7. P. H. Wright, The application of sonic (critical flow) nozzles in the gas industry, "
        "<i>Flow Meas. Instrum.</i>, 4 (2), 67–71, 1993.",
        "8. D. W. Spitzer, <i>Industrial Flow Measurement</i>, 2nd ed., Research Triangle Park, NC: "
        "ISA, 1990.",
        "9. BS 1042, <i>Measurement of Fluid Flow in Closed Conduits — Part 1, Section 1.4</i>, "
        "London, 1992.",
        "10. BS 7405, <i>Guide to the Selection and Application of Flowmeters</i>, London, 1991.",
        "11. E. M. Laws and A. K. Ouazzane, Compact installations for differential pressure flow "
        "measurement, <i>Flow Meas. Instrum.</i>, 5 (2), 79–85, 1994.",
        "12. ISO 2186, <i>Fluid Flow in Closed Conduits — Connections for Pressure Signal "
        "Transmissions</i>, Geneva, 1973.",
        "13. M. J. Reader-Harris, J. A. Slattery and E. P. Spearman, The orifice plate discharge "
        "coefficient equation — further work, <i>Flow Meas. Instrum.</i>, 6 (2), 101–114, 1995.",
        "14. F. C. Kinghorn, Two-phase flow measurement using differential pressure meters, "
        "<i>Multi-Phase Flow Measurement Short Course</i>, London, 17–18 June 1985.",
    ]))
    return "".join(b)


# ================================================================ build

SECTIONS_VI = [sec_28_1_vi]
SECTIONS_EN = [sec_28_1_en]


def body_vi():
    out = ['<p class="lede">Chương này trình bày mười một họ lưu lượng kế — từ tấm orifice chênh áp '
           'cổ điển tới lưu lượng kế Coriolis — cùng nguyên lý, cách chế tạo, lắp đặt và sai số của '
           'từng loại. Đây là chương dài nhất trong sổ tay: 132 trang gốc, 92 hình, 162 phương trình '
           'và 23 bảng.</p>']
    for f in SECTIONS_VI:
        out.append(f())
    return "".join(out)


def body_en():
    out = ['<p class="lede">This chapter covers eleven families of flowmeter — from the classical '
           'differential pressure orifice plate to the Coriolis meter — with the principle, '
           'construction, installation and error sources of each. It is the longest chapter in the '
           'handbook: 132 source pages, 92 figures, 162 equations and 23 tables.</p>']
    for f in SECTIONS_EN:
        out.append(f())
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 28 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 28 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 28 “Đo lưu lượng” của Richard Thorn và cộng sự — "
            "lưu lượng kế chênh áp, biến diện tích, thể tích, tuabin, cánh quạt, điện từ, siêu âm, "
            "xoáy, nhiệt và Coriolis, cùng nguyên lý, lắp đặt và hiệu chuẩn." if vi
            else
            "Companion to Chapter 28 of the CRC Measurement Handbook — differential pressure, "
            "variable area, positive displacement, turbine, impeller, electromagnetic, ultrasonic, "
            "vortex, thermal and Coriolis flowmeters, with their principles, installation and "
            "calibration.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 28' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 28' % BASE_EN)
    meta = ("Chương 28 · theo Ch28.pdf (CRC Press, 1999) · đang dịch: 1/11 mục" if vi else
            "Chapter 28 · in progress: 1 of 11 sections")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 28)))
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
