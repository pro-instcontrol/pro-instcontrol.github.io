# -*- coding: utf-8 -*-
"""Handbook Chapter 5 — Measurement Standards (DeWayne B. Sharp).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch05.py
"""
import os

import hbfig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch05-measurement-standards"
TITLE_EN = "Measurement Standards"
TITLE_VI = "Chuẩn đo lường"
BYLINE = "DeWayne B. Sharp · Shape of Things"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-5-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


def quote(text, src):
    return ('<div class="pullquote"><p>%s</p><span class="src">%s</span></div>' % (text, src))


def term(name, body, vim="", note=""):
    v = ('<span class="vim">[%s]</span>' % vim) if vim else ""
    n = ('<div class="note">%s</div>' % note) if note else ""
    return "<dt>%s%s</dt><dd>%s%s</dd>" % (name, v, body, n)


def gpara(t):
    """A prose aside inside the glossary: <dl> may only contain div-wrapped groups."""
    return '<div class="gloss-aside"><p>%s</p></div>' % t


def glossary(entries):
    return '<dl class="glossary">%s</dl>' % "".join(entries)


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chuẩn đo lường là những thiết bị, vật mẫu, quy trình, dụng cụ, hệ thống, giao thức hay quá trình "
        "được dùng để định nghĩa (hoặc hiện thực hoá) các đơn vị đo, và mọi phép đo ở cấp thấp hơn — kém "
        "chính xác hơn — đều phụ thuộc vào chúng. Cũng có thể nói rằng một chuẩn đo lường lưu giữ, hiện "
        "thân hoặc cung cấp một đại lượng vật lý nào đó làm cơ sở cho việc đo đại lượng ấy. Một định nghĩa "
        "khác: chuẩn là hiện thân vật lý của một đơn vị đo, nhờ đó giá trị được gán cho nó được xác định, "
        "và người ta có thể so sánh với nó để hiệu chuẩn. Nói chung, chuẩn không độc lập với điều kiện môi "
        "trường vật lý; nó chỉ là hiện thân đúng của đơn vị trong những điều kiện xác định. Còn một cách "
        "định nghĩa nữa: chuẩn là một đại lượng hay thứ nguyên đã biết, dùng làm mốc để so sánh các đơn vị "
        "đo khác."))

    # ---- 5.1
    b.append(h2("5.1 Bối cảnh lịch sử", "A Historical Perspective"))
    b.append(p(
        "Nhiều chuẩn thời kỳ đầu dựa trên cơ thể con người: chiều dài bàn tay, bề rộng ngón cái, khoảng "
        "cách giữa hai đầu ngón tay duỗi ra, chiều dài bàn chân, một số bước chân… Ban đầu, khi các nhóm "
        "người còn nhỏ, những chuẩn như vậy đủ tiện lợi và đủ đồng nhất để làm cơ sở cho phép đo."))
    b.append(p(
        "Người có lý để áp đặt một chuẩn duy nhất chính là người cai trị đất nước — vì thế đến nay thanh đo "
        "12 inch hay các thanh đo ngắn khác của chúng ta vẫn còn được gọi là <i>ruler</i>, nghĩa là “thước” "
        "mà cũng là “kẻ trị vì”. Việc thiết lập chuẩn đo lường vì thế trở thành đặc quyền của vua hay hoàng "
        "đế, và quyền ấy về sau được mọi chính phủ tiếp nhận."))
    b.append(p(
        "Lịch sử đầy những ví dụ cho thấy tầm quan trọng của phép đo và chuẩn. Trong một báo cáo gửi Quốc "
        "hội Hoa Kỳ năm 1821, John Quincy Adams viết: “Cân và đo có thể được xếp vào hàng những thứ thiết "
        "yếu đối với mỗi cá nhân trong xã hội loài người.” Những người lập quốc Hoa Kỳ coi trọng chúng đến "
        "mức Hiến pháp Hoa Kỳ ghi rõ Quốc hội có quyền ấn định các chuẩn thống nhất về cân và đo. Nhu cầu "
        "về cân, đo (tức chuẩn) có từ thuở lịch sử được ghi chép sớm nhất và thậm chí còn được nhắc đến "
        "trong Cựu Ước của Kinh Thánh. Ban đầu, chúng được quy định tại địa phương để phục vụ những nhu cầu "
        "hẹp của thương mại, trao đổi, phân chia đất đai và đánh thuế."))
    b.append(p(
        "Vì chuẩn do chính quyền địa phương hay vùng miền định nghĩa, những khác biệt nảy sinh và thường "
        "gây trở ngại cho thương mại cũng như cho nghiên cứu khoa học buổi đầu. Sự phát triển nhanh của "
        "khoa học vào cuối thế kỷ 17 làm lộ rõ một loạt khiếm khuyết nghiêm trọng của hệ đơn vị đương thời; "
        "đến năm 1790, điều đó khiến Quốc hội Pháp chỉ thị cho Viện Hàn lâm Khoa học Pháp “suy ra một chuẩn "
        "bất biến cho mọi phép đo và mọi trọng lượng”. Viện Hàn lâm đề xuất một hệ đơn vị — hệ mét — định "
        "nghĩa đơn vị độ dài theo chu vi Trái Đất, còn đơn vị thể tích và khối lượng được dẫn ra từ đơn vị "
        "độ dài. Ngoài ra, họ đề nghị mọi bội số của mỗi đơn vị đều là bội số của 10."))
    b.append(p(
        "Năm 1875, Hoa Kỳ cùng 16 quốc gia khác ký “Hiệp ước Mét”, thiết lập một bộ đơn vị đo chung. Hiệp "
        "ước cũng lập ra Văn phòng Cân đo Quốc tế (gọi tắt là BIPM), đặt tại ngoại ô Sèvres của Paris. Cơ "
        "quan này là nơi lưu giữ trên toàn thế giới mọi đơn vị làm nên hệ thống cân đo quốc tế phức tạp của "
        "chúng ta. Chính nhờ hệ thống này mà ngày nay vẫn duy trì được sự tương thích giữa những phép đo "
        "thực hiện cách nhau hàng nghìn dặm."))
    b.append(p(
        "Hệ đơn vị do BIPM thiết lập dựa trên mét và kilôgam thay vì yard và pound. Nó được gọi là "
        "<i>Système International d’Unités</i> (SI), tức Hệ đơn vị Quốc tế. Hệ này được dùng trong gần như "
        "toàn bộ công việc khoa học ở Hoa Kỳ và là hệ đơn vị đo duy nhất ở hầu hết các nước trên thế giới "
        "ngày nay."))
    b.append(p(
        "Tuy vậy, ngay cả một hệ đơn vị chung cũng không bảo đảm được sự thống nhất của kết quả đo. Mấu "
        "chốt của vấn đề nằm ở đó. Ta buộc phải đo, và buộc phải biết mình đã đo chính xác đến đâu (nói "
        "đúng hơn: với độ không đảm bảo nào). Muốn biết điều đó thì phải có chuẩn. Quan trọng hơn nữa, mọi "
        "người phải nhất trí về giá trị của các chuẩn ấy và cùng dùng những chuẩn ấy."))
    b.append(p(
        "Khi trình độ khoa học nâng cao, cơ sở của hệ đo lường thay đổi mạnh mẽ. Những chuẩn sớm nhất dựa "
        "trên cơ thể người, sau đó người ta cố gắng dựa chúng vào các hiện tượng “tự nhiên”. Có thời, cơ sở "
        "của độ dài được cho là một phân số của chu vi Trái Đất, nhưng nó lại được “duy trì” bằng một thanh "
        "bạch kim–iridi. Thời gian được duy trì bằng đồng hồ quả lắc nhưng lại được định nghĩa bằng một "
        "phân số của ngày… Ngày nay, mét không còn được định nghĩa bằng một vật mẫu nữa. Mét là quãng đường "
        "ánh sáng đi được trong một phân số thời gian được định nghĩa chính xác. Vì tốc độ ánh sáng trong "
        "chân không nay được định nghĩa là một hằng số tự nhiên với trị số xác định (299.792.458 m/s), nên "
        "định nghĩa đơn vị độ dài không còn độc lập với định nghĩa đơn vị thời gian."))
    b.append(p(
        "Trước năm 1960, giây được định nghĩa là 1/86.400 của một ngày Mặt Trời trung bình. Từ 1960 đến "
        "1967, giây được định nghĩa theo đơn vị thời gian hàm ý trong phép tính lịch thiên văn: “Giây là "
        "phân số 1/31.556.925,9747 của năm chí tuyến tại ngày 0 tháng Giêng, lúc 12 giờ theo giờ lịch thiên "
        "văn.” Với sự ra đời của bộ dao động thạch anh và sau đó là đồng hồ nguyên tử, người ta tìm được "
        "những cách định nghĩa giây tốt hơn. Điều này lại cho phép hiểu rõ hơn về các hiện tượng tự nhiên "
        "mà trước đó không thể nào hiểu được. Chẳng hạn, nay đã biết Trái Đất không quay quanh trục một "
        "cách đều đặn; thực tế nó đang chậm dần một cách thất thường. Vì giây được duy trì bằng đồng hồ "
        "nguyên tử, người ta buộc phải thêm “giây nhuận” định kỳ để ngày Mặt Trời không dần lệch đi so với "
        "thời gian dùng hằng ngày. Người ta đã quyết định rằng một chuẩn tần số không đổi là lựa chọn tốt "
        "hơn một độ dài ngày không đổi."))

    # ---- 5.2
    b.append(h2("5.2 Chuẩn là gì?", "What Are Standards?"))
    b.append(p(
        "Một khó khăn với khái niệm chuẩn là có nhiều loại. Ngoài “chuẩn đo lường”, còn có “chuẩn thực hành” "
        "hay “chuẩn giao thức” do các tổ chức tiêu chuẩn hoá khác nhau ban hành, như Tổ chức Tiêu chuẩn hoá "
        "Quốc tế (ISO), Uỷ ban Kỹ thuật Điện Quốc tế (IEC), Viện Tiêu chuẩn Quốc gia Hoa Kỳ (ANSI) và Hội "
        "đồng Tiêu chuẩn Canada (SCC). Xem Hình 5-1."))
    b.append(fig(1, hbfig.fig_5_1()))

    b.append(h3("Chuẩn thực hành (chuẩn giao thức)", "Standards of Practice (Protocol Standards)"))
    b.append(p(
        "Những chuẩn này quy định từ kích thước và đặc tính điện của một viên pin đèn pin đến hình dạng ren "
        "của một con vít máy, từ kích thước và hình dạng tấm phiếu đục lỗ IBM đến các Yêu cầu Bảo đảm Chất "
        "lượng đối với Thiết bị Đo. Có thể định nghĩa chúng là những tài liệu mô tả các thao tác và quá "
        "trình phải thực hiện để đạt một kết cục nhất định. Người châu Âu gọi chúng là “giao thức” "
        "(<i>protocol</i>) để tránh nhầm lẫn với chuẩn vật lý."))

    b.append(h3("Đo lường pháp định", "Legal Metrology"))
    b.append(p(
        "Việc áp dụng chuẩn đo lường vào kiểm soát các giao dịch hằng ngày trong buôn bán và thương mại được "
        "gọi là đo lường pháp định; ở Hoa Kỳ, nó thường được gọi là “cân và đo”. Trên bình diện quốc tế, "
        "theo thoả thuận quốc tế, việc phối hợp giữa các nước về các vấn đề đo lường pháp định do một cơ "
        "quan bán chính thức đảm nhận — Tổ chức Đo lường Pháp định Quốc tế (OIML)."))
    b.append(p(
        "Trong nội bộ Hoa Kỳ, Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) chịu trách nhiệm về tính thống "
        "nhất trong nước đối với các vấn đề đo lường pháp định, thông qua Văn phòng Cân và Đo của mình. "
        "Việc cưỡng chế thực tế thuộc trách nhiệm của từng bang trong 50 bang và các lãnh thổ; đến lượt "
        "mình, các bang thường phân quyền cưỡng chế xuống các quận hạt và, trong một số trường hợp, xuống "
        "các thành phố lớn."))

    b.append(h3("Đo lường pháp y", "Forensic Metrology"))
    b.append(p(
        "Đo lường pháp y là việc áp dụng phép đo — và do đó là chuẩn đo lường — vào việc giải quyết và "
        "phòng ngừa tội phạm. Nó được thực hành trong các phòng thí nghiệm của cơ quan thực thi pháp luật "
        "trên khắp thế giới. Hoạt động đo lường pháp y trên toàn cầu do Interpol (Tổ chức Cảnh sát Hình sự "
        "Quốc tế, cơ quan điều phối hoạt động cảnh sát của các quốc gia thành viên) phối hợp. Trong nội bộ "
        "Hoa Kỳ, Cục Điều tra Liên bang (FBI), một cơ quan thuộc Bộ Tư pháp, là đầu mối của phần lớn hoạt "
        "động đo lường pháp y."))

    b.append(h3("Vật liệu chuẩn được chứng nhận", "Standard Reference Materials"))
    b.append(p(
        "Một loại chuẩn nữa cần nhắc ở đây là vật liệu chuẩn được chứng nhận (SRM). SRM là những lượng xác "
        "định của một chất hoặc những vật mẫu nhỏ đã được chứng nhận về thành phần, độ tinh khiết, nồng độ "
        "hay một đặc tính khác hữu ích cho việc hiệu chuẩn các thiết bị đo và quy trình đo thường dùng trong "
        "kiểm soát quá trình đối với chính chất ấy. SRM là chuẩn hiệu chuẩn thiết yếu trong phép đo tỉ lượng "
        "(<i>stoichiometry</i>) — tức đo lường học của hoá học."))
    b.append(p(
        "Ở Hoa Kỳ, Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST), thông qua Chương trình Vật liệu Chuẩn, "
        "cung cấp để bán hơn 1.300 loại SRM. Chúng trải từ quặng đến kim loại và hợp kim tinh khiết; cũng "
        "bao gồm nhiều loại khí và hỗn hợp khí, nhiều chất hoá sinh và hợp chất hữu cơ. Trong số các vật mẫu "
        "dạng thiết bị có kính lọc quang với đặc tính chính xác và đèn chuẩn với đặc tính phát xạ đã biết."))

    # ---- 5.3
    b.append(h2("5.3 Nền tảng khái niệm của phép đo", "A Conceptual Basis of Measurements"))
    b.append(p("Câu nói nổi tiếng của Lord Kelvin có lẽ vẫn đáng được nhắc lại ở đây:"))
    b.append(quote(
        "Tôi thường nói rằng khi bạn có thể đo được điều mình đang nói tới, và có thể diễn đạt nó bằng những "
        "con số, thì bạn đã biết được điều gì đó về nó; nhưng khi bạn không thể đo được, không thể diễn đạt "
        "nó bằng những con số, thì hiểu biết của bạn chỉ thuộc loại mỏng manh và không thoả đáng; đó có thể "
        "là khởi đầu của hiểu biết, nhưng trong tư tưởng bạn hầu như chưa tiến được tới giai đoạn khoa học, "
        "dù vấn đề là gì đi nữa. Vậy nên, nếu khoa học là phép đo, thì không có đo lường học sẽ không có khoa "
        "học.",
        "William Thomson (Lord Kelvin), 6 tháng 5, 1886"))
    b.append(p(
        "Câu nói của Lord Kelvin đã được trích dẫn nhiều đến mức gần như thành sáo ngữ, nhưng nhìn vào Hình "
        "5-2 sẽ thấy một hệ thứ bậc thú vị. Để đạt được chất lượng, hay “làm đúng mọi việc”, cần phải đưa ra "
        "một số quyết định. Không thể ra quyết định đúng nếu không có dữ liệu số tốt làm cơ sở. Đến lượt "
        "mình, những dữ liệu số ấy phải đến từ phép đo; và nếu thực sự cần quyết định “đúng” thì chúng phải "
        "dựa trên những con số “đúng”. Cách duy nhất để có dữ liệu số “tốt” là thực hiện phép đo chính xác "
        "bằng những dụng cụ đã được hiệu chuẩn và được sử dụng đúng cách. Cuối cùng, nếu việc so sánh những "
        "phép đo ấy với các phép đo thực hiện ở nơi khác, thời điểm khác là quan trọng, thì dụng cụ phải "
        "được hiệu chuẩn bằng những chuẩn có liên kết truy xuất."))
    b.append(fig(2, hbfig.fig_5_2()))

    # ---- 5.4
    b.append(h2("5.4 Sự cần thiết của chuẩn", "The Need for Standards"))
    b.append(p(
        "Chuẩn định nghĩa các đơn vị và thang đo đang được dùng, đồng thời cho phép so sánh những phép đo "
        "thực hiện ở thời điểm và địa điểm khác nhau. Chẳng hạn, người mua dầu nhiên liệu được tính tiền "
        "theo một đơn vị thể tích chất lỏng. Ở Hoa Kỳ đó là gallon; nhưng ở hầu hết nơi khác trên thế giới "
        "đó là lít. Người mua cần biết rằng lượng đặt hàng thực sự được nhận đủ, và nhà máy lọc dầu cũng "
        "mong được trả tiền cho đúng lượng đã giao. Cả hai bên đều quan tâm đến phép đo thể tích chính xác, "
        "và do đó cần thống nhất về đơn vị, điều kiện và phương pháp đo sẽ dùng."))
    b.append(p(
        "Người cần đo khối lượng không thể mượn chuẩn gốc được lưu giữ ở Pháp, cũng không thể mượn chuẩn "
        "quốc gia của Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) ở Hoa Kỳ. Họ phải dùng những chuẩn cấp "
        "thấp hơn, có thể được kiểm tra dựa vào các chuẩn quốc gia hay quốc tế ấy. Những dụng cụ đo thông "
        "dụng hằng ngày, như cân, có thể được kiểm tra (hiệu chuẩn) định kỳ dựa vào các chuẩn khối lượng "
        "cấp làm việc để xác nhận độ chính xác. Đến lượt mình, các chuẩn cấp làm việc này lại được hiệu "
        "chuẩn dựa vào những chuẩn khối lượng cấp cao hơn. Chuỗi hiệu chuẩn hay kiểm tra này được gọi là "
        "“truy xuất nguồn gốc” (<i>traceability</i>). Một chuỗi truy xuất hợp lệ phải kèm theo phát biểu về "
        "độ không đảm bảo ở mọi bước."))

    # ---- 5.5
    b.append(h2("5.5 Các loại chuẩn", "Types of Standards"))
    b.append(h3("Chuẩn cơ bản hay chuẩn gốc", "Basic or Fundamental Standards"))
    b.append(p(
        "Trong hệ SI có bảy đơn vị đo cơ bản, mọi đơn vị khác đều dẫn ra từ chúng. Tất cả các đơn vị, trừ "
        "một, đều được định nghĩa theo giá trị đơn vị của chúng. Ngoại lệ duy nhất là đơn vị khối lượng: nó "
        "được định nghĩa là 1.000 gam (g) hay 1 kilôgam (kg). Đơn vị này cũng đặc biệt ở chỗ hiện là đơn vị "
        "duy nhất còn dựa trên một vật mẫu. Kilôgam của Hoa Kỳ, và do đó mọi chuẩn khối lượng khác, đều dựa "
        "trên một khối trụ bạch kim–iridi cụ thể được lưu giữ tại BIPM ở Pháp. Nếu Kilôgam Nguyên mẫu Quốc "
        "tế ấy thay đổi thì mọi chuẩn khối lượng khác trên thế giới sẽ sai."))
    b.append(p(
        "Bảy đơn vị cơ bản được liệt kê trong Phụ lục 1, Bảng 1. Định nghĩa của chúng nằm trong Phụ lục 1, "
        "Bảng 2."))

    b.append(h3("Chuẩn dẫn xuất", "Derived Standards"))
    b.append(p(
        "Mọi đơn vị khác đều dẫn ra từ bảy đơn vị cơ bản nói trong Phụ lục 1, Bảng 1. Chuẩn đo lường là "
        "những thiết bị thể hiện đơn vị chuẩn SI trong một phép đo. (Chẳng hạn, có thể dùng một diode zener "
        "cùng một bộ khuếch đại so sánh và một nguồn nuôi để cấp một điện áp đã biết nhằm hiệu chuẩn một "
        "vôn kế số. Bộ đó có thể đóng vai trò chuẩn đo lường cho điện áp và được dùng làm mốc tham chiếu "
        "trong phép đo.)"))
    b.append(p(
        "Phụ lục 1, Bảng 3 liệt kê những đơn vị dẫn xuất SI thông dụng nhất, cùng các đơn vị cơ sở dùng để "
        "định nghĩa đơn vị dẫn xuất ấy. Ví dụ, đơn vị tần số là hertz, được định nghĩa là nghịch đảo của "
        "thời gian; nghĩa là 1 hertz (1 Hz) bằng một chu kỳ mỗi giây."))

    b.append(h3("Hệ đảm bảo đo lường", "The Measurement Assurance System"))
    b.append(p(
        "Hình 5-3 minh hoạ mối tương quan giữa các phạm trù chuẩn khác nhau trên khắp thế giới. Tuy hình vẽ "
        "chi tiết hơn cho cơ cấu của Hoa Kỳ, những cơ cấu tương tự cũng tồn tại ở các quốc gia khác. Thực "
        "vậy, có nhiều tổ chức khu vực giúp gắn kết các phép đo thực hiện ở những nơi khác nhau trên thế "
        "giới với nhau."))
    b.append(fig(3, hbfig.fig_5_3()))

    # ---- 5.6
    b.append(h2("5.6 Số, thứ nguyên và đơn vị", "Numbers, Dimensions, and Units"))
    b.append(p(
        "Một phép đo bao giờ cũng được biểu diễn như bội số (hoặc ước số) của một lượng đơn vị nào đó. "
        "Nghĩa là cần cả một trị số và một đơn vị. Nếu đại lượng được đo là dòng điện thì nó có thể được "
        "biểu diễn bằng một số miliampe, thậm chí microampe. Người ta dễ coi sự tồn tại của các đơn vị đang "
        "dùng là đương nhiên, bởi tên của chúng đã thành một phần không thể thiếu của vốn từ."))

    # ---- 5.7
    b.append(h2("5.7 Thừa số bội", "Multiplication Factors"))
    b.append(p(
        "Vì trong nhiều trường hợp dùng nguyên đơn vị là bất tiện, người ta đã định nghĩa một bộ thừa số "
        "bội có thể dùng kèm với đơn vị để đưa giá trị đang đo về một độ lớn hợp lý hơn. Sẽ rất khó nếu phải "
        "diễn đạt những khoảng cách lớn bằng mét; vì thế người ta dùng kilômét cho khoảng cách dài hơn. "
        "Khoảng cách ngắn được nêu bằng milimét, micromét, nanomét… Xem Phụ lục 1, Bảng 4."))

    # ---- Defining terms
    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(p(
        "Phần lớn các định nghĩa trong danh mục này được lấy từ <i>Từ vựng Quốc tế về các Thuật ngữ Cơ bản và "
        "Chung trong Đo lường học</i>, do ISO xuất bản năm 1993 (VIM). Những định nghĩa ấy được chỉ ra bằng "
        "số hiệu trong VIM đặt trong ngoặc vuông. Các định nghĩa còn lại không nhằm đại diện cho một cơ quan "
        "chính thức nào mà là những định nghĩa được chấp nhận rộng rãi, đưa vào để giúp hiểu tài liệu này. "
        "Những định nghĩa chi tiết và chặt chẽ hơn có thể tìm trong các tài liệu khác của ANSI, IEC, ISO và "
        "NIST. Những từ đặt trong ngoặc đơn “(…)” có thể bỏ khỏi thuật ngữ nếu việc bỏ đi khó gây nhầm lẫn."))

    g = []
    g.append(term(
        "Độ chính xác của phép đo", "Mức độ gần nhau giữa kết quả của một phép đo và giá trị thật của đại "
        "lượng được đo.", "3.5",
        "<b>Ghi chú.</b> 1. Độ chính xác là một khái niệm định tính. 2. Không nên dùng thuật ngữ “độ xác "
        "thực” (<i>precision</i>) để chỉ độ chính xác; độ xác thực chỉ hàm ý khả năng lặp lại."))
    g.append(gpara(
        "Cần lưu ý rằng nói một dụng cụ “chính xác đến 5 %” (cách nói thông dụng) là sai. Sẽ chẳng ai thấy "
        "hữu ích một dụng cụ mà thực tế chỉ chính xác 5 % số lần đo. Điều người ta muốn nói khi phát biểu như "
        "vậy là độ không chính xác của dụng cụ nhỏ hơn 5 %, tức nó chính xác hơn 95 %. Đáng tiếc, phát biểu "
        "này gần như cũng mơ hồ không kém “chính xác đến 5 %”. Một dụng cụ chỉ chính xác 95 % số lần đo thì "
        "không hữu ích; nhưng đó không phải điều mà “độ chính xác 5 %” hàm ý. Điều được hàm ý là: (gần như) "
        "mọi lúc, chỉ thị của nó nằm trong phạm vi 5 % quanh giá trị “thật”."))
    g.append(term(
        "Hiệu chuẩn", "Một tập hợp các thao tác nhằm thiết lập, trong những điều kiện xác định, quan hệ giữa "
        "các giá trị đại lượng do một dụng cụ hay hệ thống đo chỉ ra — hoặc các giá trị do một vật mẫu hay "
        "vật liệu chuẩn thể hiện — với các giá trị tương ứng do chuẩn hiện thực hoá.", "6.11",
        "<b>Ghi chú.</b> 1. Kết quả hiệu chuẩn cho phép hoặc gán giá trị đại lượng được đo cho các chỉ thị, "
        "hoặc xác định các số hiệu chỉnh so với chỉ thị. 2. Hiệu chuẩn cũng có thể xác định các tính chất đo "
        "lường khác, như ảnh hưởng của các đại lượng ảnh hưởng. 3. Kết quả hiệu chuẩn có thể được ghi thành "
        "văn bản, đôi khi gọi là giấy chứng nhận hiệu chuẩn hay báo cáo hiệu chuẩn."))
    g.append(term(
        "Phòng thí nghiệm hiệu chuẩn", "Một không gian làm việc được trang bị thiết bị kiểm tra, môi trường "
        "được kiểm soát và nhân sự đã qua đào tạo, lập ra nhằm duy trì vận hành đúng và độ chính xác của "
        "thiết bị đo và kiểm tra. Phòng hiệu chuẩn thường thực hiện nhiều lần hiệu chuẩn thường quy, thường "
        "theo kiểu dây chuyền sản xuất."))
    g.append(term(
        "Vật liệu chuẩn được chứng nhận (CRM)", "Một vật liệu chuẩn kèm theo giấy chứng nhận, trong đó một "
        "hay nhiều giá trị tính chất được chứng nhận bằng một quy trình đã thiết lập được tính truy xuất tới "
        "một hiện thực chính xác của đơn vị dùng để biểu diễn các giá trị tính chất ấy, và mỗi giá trị được "
        "chứng nhận đều kèm một độ không đảm bảo ở mức tin cậy đã nêu.", "6.14",
        "<b>Ghi chú.</b> 1. Định nghĩa vật liệu chuẩn được nêu ở mục khác trong từ vựng này. 2. CRM thường "
        "được chế tạo theo lô, các giá trị tính chất được xác định trong giới hạn độ không đảm bảo đã nêu "
        "bằng cách đo trên các mẫu đại diện cho toàn bộ lô. 3. Các tính chất được chứng nhận đôi khi được "
        "hiện thực hoá một cách tiện lợi và đáng tin khi vật liệu được đưa vào một thiết bị chế tạo riêng — "
        "ví dụ một chất đã biết điểm ba đưa vào một ống điểm ba, một tấm kính đã biết mật độ quang đưa vào "
        "một kính lọc truyền qua, các hạt cầu có cỡ hạt đồng đều gắn trên một lam kính hiển vi. Những thiết "
        "bị như vậy cũng có thể coi là CRM. 4. Mọi CRM đều nằm trong định nghĩa “chuẩn đo lường” nêu trong "
        "VIM. 5. Một số vật liệu chuẩn và CRM có những tính chất, vì không thể tương quan với một cấu trúc "
        "hoá học đã thiết lập hoặc vì lý do khác, không thể xác định bằng những phương pháp đo vật lý và hoá "
        "học được định nghĩa chính xác. Những vật liệu đó gồm một số vật liệu sinh học như vắc-xin mà Tổ "
        "chức Y tế Thế giới đã gán cho một đơn vị quốc tế. Định nghĩa này, kể cả các ghi chú, lấy từ ISO "
        "Guide 30:1992."))
    g.append(term(
        "Đơn vị (đo) dẫn xuất nhất quán", "Một đơn vị đo dẫn xuất có thể biểu diễn như tích các luỹ thừa "
        "của các đơn vị cơ sở với hệ số tỉ lệ bằng một (1).", "1.10",
        "<b>Ghi chú.</b> Tính nhất quán chỉ xác định được đối với các đơn vị cơ sở của một hệ cụ thể. Một "
        "đơn vị có thể nhất quán với hệ này mà không nhất quán với hệ khác."))
    g.append(term(
        "Hệ đơn vị (đo) nhất quán", "Một hệ đơn vị đo trong đó mọi đơn vị dẫn xuất đều nhất quán.", "1.11"))
    g.append(term(
        "Bảo quản chuẩn (đo)", "Một tập hợp các thao tác cần thiết để giữ các đặc tính đo lường của một "
        "chuẩn đo trong những giới hạn thích hợp.", "6.12",
        "<b>Ghi chú.</b> Các thao tác thường gồm hiệu chuẩn định kỳ, lưu giữ trong điều kiện phù hợp và giữ "
        "gìn cẩn thận khi sử dụng."))
    g.append(term(
        "Chuẩn liên phòng", "Một thiết bị đi lại giữa các phòng thí nghiệm với mục đích duy nhất là liên hệ "
        "độ lớn của đơn vị vật lý mà các chuẩn lưu giữ tại mỗi phòng thí nghiệm thể hiện."))
    g.append(term(
        "Chuẩn (đo) quốc tế", "Một chuẩn được một thoả thuận quốc tế công nhận để làm cơ sở quốc tế cho việc "
        "gán giá trị cho các chuẩn khác của đại lượng liên quan.", "6.2"))
    g.append(term(
        "Hệ đơn vị Quốc tế (SI)", "Hệ đơn vị nhất quán được Đại hội Cân đo Toàn thể (CGPM) thông qua và "
        "khuyến nghị.", "1.12",
        "<b>Ghi chú.</b> Hiện nay SI dựa trên bảy đơn vị cơ sở sau: mét, kilôgam, giây, ampe, kenvin, mol "
        "và candela."))
    g.append(term(
        "Đại lượng được đo", "Một đại lượng cụ thể là đối tượng của phép đo.", "2.6",
        "<b>Ví dụ.</b> Áp suất hơi của một mẫu nước nhất định ở 20 °C. <b>Ghi chú.</b> Việc xác định đại "
        "lượng được đo có thể cần nêu rõ các đại lượng như thời gian, nhiệt độ và áp suất."))
    g.append(term(
        "Phép đo", "Một tập hợp các thao tác nhằm mục đích xác định giá trị của một đại lượng.", "2.1",
        "<b>Ghi chú.</b> Các thao tác có thể được thực hiện tự động."))
    g.append(term(
        "Phương pháp đo", "Một chuỗi thao tác logic, được mô tả một cách tổng quát, dùng khi thực hiện phép "
        "đo.", "2.4",
        "<b>Ghi chú.</b> Phương pháp đo có thể được phân loại theo nhiều cách, chẳng hạn: phương pháp thay "
        "thế, phương pháp vi sai, phương pháp chỉ không."))
    g.append(term(
        "Đo lường học", "Khoa học về phép đo.", "2.2",
        "<b>Ghi chú.</b> Đo lường học bao gồm mọi khía cạnh, cả lý thuyết lẫn thực hành, liên quan đến phép "
        "đo, bất kể độ không đảm bảo của chúng và bất kể chúng xuất hiện trong lĩnh vực khoa học hay công "
        "nghệ nào."))
    g.append(term(
        "Chuẩn (đo) quốc gia", "Một chuẩn được một quyết định quốc gia công nhận để làm cơ sở, trong một "
        "nước, cho việc gán giá trị cho các chuẩn khác của đại lượng liên quan.", "6.3"))
    g.append(term(
        "Chuẩn tham chiếu quốc gia", "Một chuẩn được lưu giữ tại các phòng thí nghiệm quốc gia như Viện Tiêu "
        "chuẩn và Công nghệ Quốc gia (NIST) ở Gaithersburg, Maryland; Hội đồng Nghiên cứu Quốc gia (NRC) ở "
        "Ottawa, Canada; Phòng thí nghiệm Vật lý Quốc gia (NPL) ở Teddington, Anh; Viện Vật lý – Kỹ thuật "
        "Liên bang (PTB) ở Braunschweig, Đức; và là chuẩn pháp định của quốc gia tương ứng."))
    g.append(term(
        "Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST)", "Phòng thí nghiệm chuẩn quốc gia của Hoa Kỳ, chịu "
        "trách nhiệm duy trì các chuẩn vật lý làm cơ sở cho mọi phép đo ở Hoa Kỳ."))
    g.append(term(
        "Chuẩn gốc", "Một chuẩn được chỉ định hoặc được thừa nhận rộng rãi là có phẩm chất đo lường cao "
        "nhất và có giá trị được chấp nhận mà không cần tham chiếu tới chuẩn khác cùng đại lượng.", "6.4",
        "<b>Ghi chú.</b> Khái niệm chuẩn gốc có giá trị như nhau đối với đại lượng cơ bản và đại lượng dẫn "
        "xuất."))
    g.append(term(
        "Nguyên lý đo", "Nền tảng khoa học của một phép đo.", "2.3",
        "<b>Ví dụ.</b> Hiệu ứng nhiệt điện áp dụng cho phép đo nhiệt độ; hiệu ứng Josephson áp dụng cho phép "
        "đo hiệu điện thế; hiệu ứng Doppler áp dụng cho phép đo vận tốc; hiệu ứng Raman áp dụng cho phép đo "
        "số sóng của dao động phân tử."))
    g.append(term(
        "Chuẩn tham chiếu", "Một chuẩn, nói chung có phẩm chất đo lường cao nhất hiện có tại một địa điểm hay "
        "trong một tổ chức, mà từ đó các phép đo thực hiện ở đó được dẫn ra.", "6.6"))
    g.append(term(
        "Vật liệu chuẩn", "Một vật liệu hay chất mà một hoặc nhiều giá trị tính chất đủ đồng nhất và được "
        "xác lập đủ tốt để dùng cho việc hiệu chuẩn một thiết bị, đánh giá một phương pháp đo, hoặc gán giá "
        "trị cho vật liệu khác.", "6.13",
        "<b>Ghi chú.</b> Vật liệu chuẩn có thể ở dạng khí tinh khiết hay hỗn hợp, lỏng hoặc rắn. Ví dụ: nước "
        "để hiệu chuẩn nhớt kế, saphia làm chất chuẩn nhiệt dung trong nhiệt lượng kế, và các dung dịch dùng "
        "để hiệu chuẩn trong phân tích hoá học. Định nghĩa này, kể cả ghi chú, lấy từ ISO Guide 30:1992."))
    g.append(term(
        "Độ lặp lại (của kết quả đo)", "Mức độ gần nhau giữa kết quả của những phép đo liên tiếp cùng một "
        "đại lượng, thực hiện trong cùng điều kiện đo.", "3.6",
        "<b>Ghi chú.</b> 1. Những điều kiện ấy gọi là điều kiện lặp lại. 2. Điều kiện lặp lại bao gồm: cùng "
        "quy trình đo; cùng người quan sát; cùng dụng cụ đo, dùng trong cùng điều kiện; cùng địa điểm; lặp "
        "lại trong một khoảng thời gian ngắn. 3. Độ lặp lại có thể biểu diễn định lượng bằng độ phân tán đặc "
        "trưng của các kết quả."))
    g.append(term(
        "Độ tái lập (của kết quả đo)", "Mức độ gần nhau giữa kết quả của những phép đo cùng một đại lượng "
        "thực hiện trong những điều kiện đo đã thay đổi.", "3.7",
        "<b>Ghi chú.</b> 1. Một phát biểu hợp lệ về độ tái lập đòi hỏi phải nêu rõ những điều kiện đã thay "
        "đổi. 2. Các điều kiện thay đổi bao gồm: nguyên lý đo; phương pháp đo; người quan sát; dụng cụ đo; "
        "chuẩn tham chiếu; địa điểm; điều kiện sử dụng; thời gian. 3. Độ tái lập có thể biểu diễn định lượng "
        "bằng độ phân tán đặc trưng của các kết quả. 4. “Kết quả” ở đây thường được hiểu là kết quả đã hiệu "
        "chỉnh."))
    g.append(term(
        "Chuẩn thứ cấp", "Một chuẩn có giá trị được gán bằng cách so sánh với một chuẩn gốc của cùng đại "
        "lượng.", "6.5"))
    g.append(term(
        "Phòng thí nghiệm chuẩn", "Một không gian làm việc được trang bị thiết bị và chuẩn, môi trường được "
        "kiểm soát đúng mức và nhân sự đã qua đào tạo, lập ra nhằm duy trì tính truy xuất của các chuẩn và "
        "thiết bị đo mà tổ chức chủ quản sử dụng. Phòng thí nghiệm chuẩn thường thực hiện ít phép đo hơn "
        "nhưng chuyên sâu hơn và có độ chính xác cao hơn so với phòng hiệu chuẩn."))
    g.append(term(
        "Dung sai", "Trong đo lường học: các giới hạn của khoảng giá trị (tức độ không đảm bảo) áp dụng cho "
        "một dụng cụ đo đang hoạt động đúng chức năng."))
    g.append(term(
        "Truy xuất nguồn gốc", "Thuộc tính của kết quả một phép đo hay giá trị của một chuẩn, nhờ đó nó có "
        "thể được liên hệ với những mốc tham chiếu đã nêu — thường là chuẩn quốc gia hay quốc tế — thông qua "
        "một chuỗi so sánh không gián đoạn, mọi mắt đều có độ không đảm bảo đã nêu.", "6.10",
        "<b>Ghi chú.</b> 1. Khái niệm này thường được diễn đạt bằng tính từ “có thể truy xuất”. 2. Chuỗi so "
        "sánh không gián đoạn được gọi là chuỗi truy xuất."))
    g.append(gpara(
        "Dù ISO đã công bố (và chấp nhận) định nghĩa nêu trên, nhiều người hành nghề cố làm cho thuật ngữ "
        "này có nghĩa hơn. Họ cho rằng định nghĩa nên đưa vào khía cạnh bằng chứng phải được trình ra một "
        "cách liên tục, để khắc phục ý nghĩ rằng một khi đã đạt được tính truy xuất hợp lệ thì nó tồn tại "
        "mãi mãi. Một định nghĩa tương tự như sau sẽ đáp ứng yêu cầu đó:"))
    g.append(quote(
        "Truy xuất nguồn gốc là một đặc tính của một lần hiệu chuẩn hay một phép đo. Một phép đo hay một "
        "lần hiệu chuẩn chỉ được coi là có thể truy xuất khi mỗi dụng cụ và mỗi chuẩn, trong một hệ thứ bậc "
        "kéo ngược về chuẩn quốc gia (hoặc quốc tế), đều đã được hiệu chuẩn đúng và kết quả được ghi nhận "
        "đầy đủ, kể cả các phát biểu về độ không đảm bảo, một cách liên tục. Hồ sơ phải cung cấp thông tin "
        "cần thiết để chứng minh rằng mọi lần hiệu chuẩn trong chuỗi hiệu chuẩn đều được thực hiện thoả đáng.",
        "Cách phát biểu lại của giới hành nghề"))
    g.append(term(
        "Chuẩn chuyển tiếp", "Một chuẩn dùng làm trung gian để so sánh các chuẩn.", "6.8",
        "<b>Ghi chú.</b> Nên dùng thuật ngữ “thiết bị chuyển tiếp” khi vật trung gian không phải là chuẩn."))
    g.append(term(
        "Chuẩn lưu động", "Một chuẩn, đôi khi có kết cấu đặc biệt, nhằm mục đích vận chuyển giữa các địa "
        "điểm.", "6.9",
        "<b>Ví dụ.</b> Một chuẩn tần số caesi xách tay chạy pin."))
    g.append(term(
        "Độ không đảm bảo đo", "Một tham số gắn với kết quả của một phép đo, đặc trưng cho độ phân tán của "
        "các giá trị có thể được gán một cách hợp lý cho đại lượng được đo.", "3.9",
        "<b>Ghi chú.</b> 1. Tham số đó có thể là, ví dụ, một độ lệch chuẩn (hoặc một bội số cho trước của "
        "nó), hay nửa độ rộng của một khoảng có mức tin cậy đã nêu. 2. Độ không đảm bảo đo nói chung gồm "
        "nhiều thành phần. Một số thành phần có thể được đánh giá từ phân bố thống kê của kết quả một loạt "
        "phép đo và có thể đặc trưng bằng độ lệch chuẩn thực nghiệm. Các thành phần khác — cũng có thể đặc "
        "trưng bằng độ lệch chuẩn — được đánh giá từ những phân bố xác suất giả định dựa trên kinh nghiệm "
        "hoặc thông tin khác. 3. Cần hiểu rằng kết quả đo là ước lượng tốt nhất về giá trị của đại lượng "
        "được đo, và mọi thành phần độ không đảm bảo (kể cả những thành phần do hiệu ứng hệ thống, như các "
        "thành phần gắn với số hiệu chỉnh và với chuẩn tham chiếu) đều đóng góp vào độ phân tán. Định nghĩa "
        "này là của <i>Hướng dẫn Biểu diễn Độ không đảm bảo đo</i>, nơi lý lẽ của nó được trình bày chi tiết "
        "(xem đặc biệt mục 2.2.4 và phụ lục D)."))
    g.append(term(
        "Giá trị (của một đại lượng)", "Độ lớn của một đại lượng cụ thể, nói chung được biểu diễn bằng một "
        "đơn vị đo nhân với một số.", "1.18",
        "<b>Ví dụ.</b> Chiều dài một thanh: 5,34 m hay 534 cm. Khối lượng một vật: 0,152 kg hay 152 g. Lượng "
        "chất của một mẫu nước (H₂O): 0,012 mol hay 12 mmol. <b>Ghi chú.</b> 1. Giá trị của một đại lượng có "
        "thể dương, âm hoặc bằng không. 2. Giá trị của một đại lượng có thể được biểu diễn theo nhiều cách. "
        "3. Giá trị của các đại lượng có thứ nguyên bằng một thường được biểu diễn bằng số thuần. 4. Một đại "
        "lượng không thể biểu diễn bằng đơn vị đo nhân với một số có thể được biểu diễn bằng cách tham chiếu "
        "tới một thang tham chiếu quy ước, hoặc tới một quy trình đo, hoặc cả hai."))
    g.append(term(
        "Chuẩn làm việc", "Một chuẩn được dùng thường xuyên để hiệu chuẩn hoặc kiểm tra vật mẫu, dụng cụ đo "
        "hay vật liệu chuẩn.", "6.7",
        "<b>Ghi chú.</b> 1. Chuẩn làm việc thường được hiệu chuẩn dựa vào một chuẩn tham chiếu. 2. Chuẩn làm "
        "việc dùng thường xuyên để bảo đảm một phép đo đang được thực hiện đúng cách được gọi là chuẩn kiểm "
        "tra."))
    b.append(glossary(g))

    # ---- references
    b.append(h2("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>NIST Special Publication 250 Appendix, Fee Schedule, U.S. Dept of Commerce, Technology '
             'Administration, National Institute of Standards and Technology, Calibration Program, Bldg. 820, '
             'Room 232, Gaithersburg, MD, 20899-0001.</li>'
             '<li>B. N. Taylor, NIST Special Publication 811, 1995 edition, <i>Guide for the Use of the '
             'International System of Units (SI)</i>, U.S. Department of Commerce, National Institute of '
             'Standards and Technology, Gaithersburg, MD, 20899-0001, 1995.</li>'
             '<li>H. A. Klein, <i>The Science of Measurement: A Historical Survey</i>, New York: Dover '
             'Publications, Inc., 1974.</li>'
             '<li>B. N. Taylor and C. E. Kuyatt, <i>Guidelines for Evaluating and Expressing the Uncertainty of '
             'NIST Measurement Results</i>, NIST Technical Note 1297 (1994 ed.).</li>'
             '<li>R. C. Cochrane, <i>Measures for Progress — History of the National Bureau of Standards</i>, '
             'United States Department of Commerce (1966), Library of Congress Catalog Card Number: '
             '65-62472.</li>'
             '<li><i>NIST Standard Reference Material Catalog</i>, NIST Special Publication 260, NIST CODEN: '
             'XNBSAV. Available from the Superintendent of Documents, Washington, D.C. 20402.</li>'
             '<li><i>International Vocabulary of Basic and General Terms in Metrology</i>, ISO, 1993.</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%sch04-measurement-accuracy/"><span class="k">← Chương 4</span>Độ chính xác của phép '
             'đo</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 5. It carries the three figures "
        "redrawn as vectors, a map of the argument, and the glossary index; the prose — a history of standards "
        "from body measures to the caesium second, the four kinds of standards, the traceability hierarchy, and "
        "the VIM definitions — is in the translation itself."))

    b.append(h2("Figure 5.1 · Who writes which standards"))
    b.append(p(
        "Sharp opens §5.2 by warning that “standard” names several different objects, and the first figure is "
        "the org chart that keeps them apart: treaty-level bodies (CGPM, CIPM, BIPM) at the top for the units "
        "themselves, ISO/IEC/ANSI/SCC for standards of practice, OIML for legal metrology, and Interpol and the "
        "FBI for forensic metrology."))
    b.append(fig(1, hbfig.fig_5_1(), "en"))

    b.append(h2("Figure 5.2 · The quality chain"))
    b.append(p(
        "The Lord Kelvin quotation — “when you can measure what you are speaking about… you know something "
        "about it” — is old enough to be trite, so §5.3 turns it into a chain of dependencies: quality needs "
        "decisions, decisions need numerical data, data needs measurements, measurements need calibrated "
        "instruments, and instruments that can be compared across time and place need traceable standards. "
        "Break any link and the whole argument collapses, which is why the chapter treats traceability as the "
        "load-bearing element rather than a formality."))
    b.append(fig(2, hbfig.fig_5_2(), "en"))

    b.append(h2("Figure 5.3 · The measurement assurance system"))
    b.append(p(
        "The third figure is the one worth studying closely, because it is where the abstract hierarchy becomes "
        "an institution. The US branch runs from the President through the Department of Commerce to NIST and "
        "down to working standards and instruments; the treaty branch runs from the Treaty of the Meter through "
        "CIPM and its consultative committees (CCE for electricity, CCT for thermometry) to the BIPM; other "
        "nations plug in through their national laboratories. Every arrow in the diagram is a comparison with a "
        "stated uncertainty — that is what makes the chain a chain and not just a list of organisations."))
    b.append(fig(3, hbfig.fig_5_3(), "en"))

    b.append(h2("The four kinds of standards"))
    b.append('<div class="table-wrap"><table class="tbl"><thead><tr>'
             '<th>Kind</th><th>What it fixes</th><th>Who controls it</th></tr></thead><tbody>'
             '<tr><td>Measurement standard</td><td>The size of a unit — the metre, the kilogram, the volt</td>'
             '<td>CGPM / CIPM / BIPM, realised by NIST and the other national laboratories</td></tr>'
             '<tr><td>Standard of practice (protocol)</td><td>Dimensions, interfaces, procedures — a battery '
             'can, a screw thread, QA requirements for measuring equipment</td>'
             '<td>ISO, IEC, ANSI, SCC</td></tr>'
             '<tr><td>Legal metrology</td><td>The rules of trade measurement — what a gallon or a litre means '
             'at the pump</td><td>OIML internationally; NIST Office of Weights and Measures, then the states '
             'and counties, in the US</td></tr>'
             '<tr><td>Standard reference material</td><td>The composition or property of a substance — ores, '
             'alloys, gases, biochemicals</td><td>NIST’s SRM Program, over 1,300 items</td></tr>'
             '</tbody></table></div>'
             '<p style="font-size:.84rem;color:#888;font-style:italic">Table 5.1 · The four senses of '
             '“standard” that §5.2 separates.</p>')

    b.append(h2("The seven base units and the one that is still an artifact"))
    b.append(p(
        "§5.5 makes a point that dates the chapter precisely: six of the seven SI base units are defined by "
        "their unitary value, but the kilogram is defined as 1,000 g and is “the only unit currently based on "
        "an artifact” — a platinum/iridium cylinder at the BIPM. If the International Prototype Kilogram were "
        "to change, every mass standard in the world would be wrong. (The 2019 redefinition, which fixed the "
        "Planck constant, retired that last artifact; Sharp could not know it when this was written, and the "
        "translation keeps his text as it stands.) The metre has already made the same journey: it is now the "
        "distance light travels in a stated fraction of a second, so the definition of length is no longer "
        "independent of the definition of time."))

    b.append(h2("Glossary index"))
    b.append(p(
        "The “Defining Terms” section is the most reusable part of the chapter — thirty-two entries, most of "
        "them lifted verbatim from the 1993 VIM with their clause numbers. The translation carries all of them; "
        "the VIM numbers are given here so the entries can be cited directly."))
    b.append('<div class="table-wrap"><table class="tbl"><thead><tr><th>Term</th><th>VIM</th>'
             '<th>Term</th><th>VIM</th></tr></thead><tbody>'
             '<tr><td>Accuracy of measurement</td><td>3.5</td><td>Measurement</td><td>2.1</td></tr>'
             '<tr><td>Calibration</td><td>6.11</td><td>Method of measurement</td><td>2.4</td></tr>'
             '<tr><td>Calibration laboratory</td><td>—</td><td>Metrology</td><td>2.2</td></tr>'
             '<tr><td>Certified reference material</td><td>6.14</td><td>National standard</td><td>6.3</td></tr>'
             '<tr><td>Coherent derived unit</td><td>1.10</td><td>National reference standard</td><td>—</td></tr>'
             '<tr><td>Coherent system of units</td><td>1.11</td><td>NIST</td><td>—</td></tr>'
             '<tr><td>Conservation of a standard</td><td>6.12</td><td>Primary standard</td><td>6.4</td></tr>'
             '<tr><td>Interlaboratory standard</td><td>—</td><td>Principle of measurement</td><td>2.3</td></tr>'
             '<tr><td>International standard</td><td>6.2</td><td>Reference standard</td><td>6.6</td></tr>'
             '<tr><td>International System of Units</td><td>1.12</td><td>Reference material</td><td>6.13</td></tr>'
             '<tr><td>Measurand</td><td>2.6</td><td>Repeatability</td><td>3.6</td></tr>'
             '<tr><td>Reproducibility</td><td>3.7</td><td>Standards laboratory</td><td>—</td></tr>'
             '<tr><td>Secondary standard</td><td>6.5</td><td>Tolerance</td><td>—</td></tr>'
             '<tr><td>Traceability</td><td>6.10</td><td>Uncertainty of measurement</td><td>3.9</td></tr>'
             '<tr><td>Transfer standard</td><td>6.8</td><td>Value of a quantity</td><td>1.18</td></tr>'
             '<tr><td>Traveling standard</td><td>6.9</td><td>Working standard</td><td>6.7</td></tr>'
             '</tbody></table></div>'
             '<p style="font-size:.84rem;color:#888;font-style:italic">Table 5.2 · Glossary entries and their '
             'VIM clause numbers. A dash means the term is Sharp’s own, not taken from the VIM.</p>')

    b.append('<div class="chapter-nav">'
             '<a href="%sch04-measurement-accuracy/"><span class="k">← Chapter 4</span>Measurement Accuracy</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 5 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 5 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 5 “Measurement Standards” của DeWayne B. Sharp — lịch sử chuẩn từ "
            "thân thể người tới giây caesi, bốn loại chuẩn, chuỗi truy xuất và hệ đảm bảo đo lường, cùng "
            "toàn bộ danh mục định nghĩa theo VIM 1993." if vi else
            "Companion to Chapter 5 of the CRC Measurement Handbook — measurement standards, traceability and "
            "the VIM glossary, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 5'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 5' % BASE_EN)
    meta = ("Chương 5 · theo Ch05.pdf (CRC Press, 1999) · 3 hình, 2 bảng" if vi
            else "Chapter 5 · 3 figures, 2 tables")
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
