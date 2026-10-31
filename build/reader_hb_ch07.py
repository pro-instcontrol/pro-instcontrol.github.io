# -*- coding: utf-8 -*-
"""Handbook Chapter 7 — Thickness Measurement (Brasunas, Cushman, Lakew).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch07.py
"""
import os

import hb7fig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch07-thickness-measurement"
TITLE_EN = "Thickness Measurement"
TITLE_VI = "Đo chiều dày"
BYLINE = "John C. Brasunas · G. Mark Cushman · Brook Lakew · NASA/Goddard"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-7-%d">%s<figcaption class="figcap">%s</figcaption>'
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
        if isinstance(r, str):                      # a group header row
            body.append('<tr class="grp"><td colspan="%d">%s</td></tr>' % (len(headers), r))
        else:
            body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p class="tblcap">%s</p>' % (cls, th, "".join(body), caption))


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Người ta có thể đo chiều dày trên rất nhiều thang. Thiên hà là một đĩa xoắn dày khoảng 100 Em "
        "(10²⁰ m). Hệ Mặt Trời giống một cái bánh kếp dày khoảng 1 Tm (10¹² m). Vành Sao Thổ dày khoảng "
        "10 km. Gần nhà hơn, khí quyển Trái Đất là một vỏ cầu dày khoảng 40 km; thời tiết diễn ra trong "
        "tầng đối lưu, dày khoảng 12 km. Lớp vỏ ngoài cùng của phần Trái Đất rắn là vỏ lục địa, dày "
        "khoảng 35 km. Đại dương có độ sâu trung bình 3,9 km. Ở Nam Cực, những vật thể mới được phát "
        "hiện, được cho là vi hoá thạch chỉ điểm sự sống cổ trên Sao Hoả, dày dưới 100 nm. Còn trong môi "
        "trường nhân tạo, công nghiệp phải xử lý chiều dày từ mét cho các công trình xây dựng, tới "
        "milimét trên dây chuyền lắp ráp, tới micromét và nanomét cho ngành bán dẫn, quang học và lớp "
        "phủ."))

    b.append(fig(1, hb7fig.fig_7_1()))

    b.append(p(
        "Cách quen thuộc nhất để đo chiều dày có lẽ là phương pháp cơ học, như thước hay thước cặp. "
        "Những cách khác đôi khi được huy động vì một trong các lý do sau: không tiếp cận được cả hai "
        "mặt của vật; kích thước quá lớn hoặc quá nhỏ so với thước cặp; vật quá dễ vỡ, quá nóng hoặc quá "
        "lạnh để tiếp xúc trực tiếp; hoặc vật đang chuyển động trên dây chuyền — và nó thậm chí có thể "
        "không phải vật rắn."))

    b.append(p(
        "Chiều dày cũng có thể là một hàm của vị trí, vì vật có thể đã được chế tạo với chiều dày không "
        "đều — cố ý hoặc không — hoặc chiều dày đã trở nên không đều theo thời gian do ăn mòn, nứt hay "
        "một dạng xuống cấp nào khác. Chiều dày cũng có thể đang thay đổi theo thời gian do cố ý nuôi "
        "dày hoặc ăn mòn chọn lọc, ví dụ với màng mỏng. Từ đó suy ra rằng, nói một cách tổng quát hơn, "
        "đo chiều dày có thể đòi hỏi đo địa hình hay biên dạng độ cao của hai mặt rồi lấy hiệu của "
        "chúng. Cách khác, bản thân kỹ thuật đo có thể cho ra một số đọc liên hệ trực tiếp với hiệu ấy. "
        "Bảng 7.1 liệt kê một số trong nhiều kỹ thuật dùng để xác định chiều dày, cùng dải hữu dụng và "
        "vài nhận xét về độ chính xác và/hoặc độ chụm."))

    b.append(fig(2, hb7fig.fig_7_2()))

    b.append(table(
        ["Kỹ thuật", "Dải đo", "Nhận xét"],
        ["Cơ học",
         ["Thước cặp, panme", "1 µm – 100 mm", "độ chính xác ±3 µm"],
         ["Đồng hồ điện tử: LVDT", "0 – 1 m", "độ chụm tuỳ mức nhiễu"],
         ["Đo khí nén", "tối thiểu 50 nm", "—"],
         "Quang học: lấy nét, che bóng, so sánh",
         ["Kính hiển vi", "tối thiểu 5 µm", "chính xác khoảng 1 %"],
         ["Bộ so sánh, máy chiếu", "25 – 250 nm", "—"],
         ["Thước cặp laser", "100 µm – 100 mm", "độ chụm 6 µm hoặc tốt hơn"],
         ["Cân", "tuỳ diện tích", "—"],
         ["Đo điện dung", "từ dưới 1 µm tới khoảng 1 cm", "—"],
         ["Đo cảm ứng (dòng xoáy)", "0 – 1,5 mm", "độ chụm 2,5 µm"],
         ["Cảm ứng từ", "0 – 4 mm", "chính xác 10 %"],
         ["Đầu đo Hall", "0 – 10 mm", "chính xác 1 – 3 %"],
         "Trường xa / thời gian bay",
         ["Sonar, siêu âm", "0,5 – 250 mm", "chính xác 25 µm"],
         ["Radar", "0,1 km tới vài trăm km", "—"],
         ["Lidar", "10 m – 5 km", "—"],
         ["Công nghệ THz", "—", "—"],
         "Trường xa / cộng hưởng",
         ["Siêu âm cộng hưởng", "—", "—"],
         ["Giao thoa kế: phổ và không gian", "1 nm – 100 µm", "chính xác khoảng λ/50"],
         ["Ellipsometry", "0,3 nm – 10 µm", "chính xác 0,1 nm"],
         "Trường xa / hấp thụ, tán xạ, phát xạ",
         ["Tán xạ ngược tia gamma", "tới 25 mm", "độ chụm 0,5 %"],
         ["Truyền qua tia beta", "2 µm – 1 mm", "độ chụm 0,2 %"],
         ["Tán xạ ngược tia beta", "100 nm – 50 µm", "độ chụm 3 – 20 %"],
         ["Huỳnh quang tia X", "0 – 30 µm", "—"],
         ["Hấp thụ hồng ngoại", "tuỳ vật liệu", "—"],
         ["Kỹ thuật quét: kính hiển vi đầu dò quét", "—", "độ chụm tốt hơn 0,1 nm"],
         ["Kỹ thuật phá huỷ: điện phân", "15 nm – 50 µm", "—"]],
        "Bảng 7.1 · Các kỹ thuật đo chiều dày, theo cách phân loại của nguyên bản."))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> Chương này trong bản gốc <b>không có hình nào</b> — chỉ có ba "
        "bảng. Toàn bộ mười sáu hình trong bản dịch là hình do người dịch vẽ để minh hoạ nguyên lý mà "
        "văn bản mô tả; mọi đường cong đều tính từ công thức được nêu ngay trong hình hoặc trong chú "
        "thích, không phải phác tay. Những chỗ nguyên bản chỉ nói định tính — ví dụ “tín hiệu tắt dần "
        "theo hàm mũ” — hình vẽ buộc phải chọn một dạng hàm cụ thể, và dạng ấy được ghi rõ trong hình để "
        "người đọc biết đó là mô hình chứ không phải số liệu đo."))

    b.append(quote(
        "Đo chiều dày, nói cho cùng, là đo một khoảng cách mà một trong hai đầu không nhìn thấy được.",
        "Ý chính của §7.1"))

    # ---- 7.1
    b.append(h2("7.1 Mô tả các kỹ thuật đo đã chín muồi", "The Relatively Mature Techniques"))
    b.append(p(
        "Những mô tả dưới đây cũng sẽ nhắc tới một số nhà cung cấp, địa chỉ của họ nằm ở Bảng 7.2. Thông "
        "tin nhà cung cấp bổ sung, kèm giá hoặc mã model cụ thể, nằm ở Bảng 7.3. Hai từ “gage” và "
        "“gauge” được dùng lẫn nhau, không phân biệt."))

    b.append(table(
        ["Nhà cung cấp", "Địa chỉ", "Nhà cung cấp", "Địa chỉ"],
        [["Bomem", "Quebec, Canada", "Ono Sokki", "Addison, IL"],
         ["Brown & Sharpe", "North Kingstown, RI", "Oxford Instruments", "Concord, MA"],
         ["CMI International", "Elk Grove Village, IL", "Panametrics", "Waltham, MA"],
         ["Conductus", "Sunnyvale, CA", "Park Scientific Instruments", "Sunnyvale, CA"],
         ["deFelsko", "Ogdensburg, NY", "Penny + Giles", "Attleboro, MA"],
         ["Digilab", "Cambridge, MA", "Perkin Elmer", "Norwalk, CT"],
         ["Digital Instruments", "Santa Barbara, CA", "Phase-Shift Technology", "Tucson, AZ"],
         ["Electromatic", "Cedarhurst, NY", "Rudolf Instruments", "Fairfield, NJ"],
         ["Fischer", "Windsor, CT", "Scantron", "qua Micro Photonics"],
         ["Hewlett Packard", "Englewood, CO", "Schaevitz", "Pennsauken, NJ"],
         ["Kta-Tator", "Pittsburgh, PA", "Sentech", "qua Micro Photonics"],
         ["Magnetic Analysis Corp.", "Mount Vernon, NY", "SolveTech", "Claymont, DE"],
         ["Mattson", "Madison, WI", "Starrett", "Athol, MA"],
         ["Measurex", "Cupertino, CA", "Stresstel", "Scotts Valley, CA"],
         ["Micro Photonics", "Allentown, PA", "Transicoil Inc.", "Valley Forge, PA"],
         ["Midac", "Costa Mesa, CA", "Trans-Tek", "Ellington, CT"],
         ["Mitutoyo", "Plymouth, MI", "Willrich Precision Instrument Co.", "Cresskill, NJ"],
         ["Moore Products Co.", "Spring House, PA", "J.A. Woolam Co., Inc.", "Lincoln, NE"],
         ["NDC Systems", "Irwindale, CA", "Wyko", "Tucson, AZ"],
         ["Nicolet", "Madison, WI", "Zygo", "Middlefield, CT"]],
        "Bảng 7.2 · Địa chỉ nhà cung cấp. Địa chỉ và tên gọi là của năm 1999; nhiều hãng trong số này "
        "đã sáp nhập hoặc đổi tên từ đó."))

    # 7.1.1
    b.append(h3("Cơ khí", "Mechanical"))
    b.append(p(
        "Công cụ nền tảng để đo chiều dày là dụng cụ có vạch chia thẳng [1, 2]. Đây là phương tiện cơ "
        "học duy nhất cho phép đo trực tiếp. Những khoảng chia đại diện cho các khoảng cách đã biết được "
        "dùng làm so sánh trực tiếp với khoảng cách chưa biết. Dụng cụ gồm thanh, thước, thước cuộn — "
        "gọi chung là <i>ruler</i>; thước cặp, dùng một cơ cấu tiếp xúc cưỡng bức để căn chỉnh tốt hơn "
        "các biên của khoảng cách; và panme, thường chính xác hơn nhờ kết hợp thang thẳng với thang "
        "vòng. Độ chính xác của thước cặp có thể tăng bằng du xích hoặc bằng đầu dò tuyến tính."))
    b.append(p(
        "Đồ gá cố định thường dùng để đo vật theo kiểu đạt/không đạt. Một vật có hình học cố định (chiều "
        "dài, lỗ côn, ren…) được so với một chi tiết mẫu, thường để kiểm tra chi tiết. Các biến thể gồm: "
        "<i>thước mẫu</i> — vật đại diện cho kích thước danh nghĩa của chi tiết; <i>thước giới hạn</i> — "
        "vật đại diện cho điều kiện giới hạn của dung sai; và <i>căn mẫu</i> (gage block, còn gọi là "
        "Johansson block) — vật có chiều dài cố định dùng làm chuẩn tham chiếu kích thước. Đồng hồ so "
        "dùng để cảm nhận dịch chuyển so với một mặt chuẩn và hiển thị độ lệch so với mặt ấy; màn hiển "
        "thị có thể được ghép điện tử để khuếch đại và/hoặc hiển thị."))
    b.append(fig(3, hb7fig.fig_7_3()))
    b.append(p(
        "Dải đo của một dụng cụ có thể được mở rộng nếu có nhiều bản sao của vật cần đo. Ví dụ, chiều "
        "dày một tờ giấy có thể đo bằng một cái thước đơn giản nếu xếp 500 tờ lại. (Nhà cung cấp: Brown "
        "& Sharpe, Starrett, Mitutoyo. Xem thêm [3].)"))

    # 7.1.2
    b.append(h3("Đồng hồ điện tử", "Electronic Gages"))
    b.append(p(
        "Biến áp vi sai tuyến tính (LVDT) dùng nhiều biến áp hình xuyến để cảm nhận dịch chuyển dọc trục "
        "của một lõi sắt gắn với đầu đo — gắn trực tiếp, hoặc qua một khớp khác như đòn bẩy. Dịch chuyển "
        "này tương quan trực tiếp với khoảng cách mà phần điện tử phía sau hiển thị. Như vậy LVDT thay "
        "thế cho thước có vạch hay panme, nhưng có số đọc bằng điện. (Nhà cung cấp: Penny + Giles; "
        "Schaevitz; Transicoil Inc.; Trans-Tek.)"))
    b.append(fig(4, hb7fig.fig_7_4()))

    # 7.1.3
    b.append(h3("Đo khí nén", "Pneumatic Gaging"))
    b.append(p(
        "Đồng hồ đo khí nén có khí nén thoát ra qua các lỗ phun của đầu đo. Chênh lệch tốc độ khí, hoặc "
        "áp suất ngược, là một hàm của khoảng cách giữa đầu đo và chi tiết. Trong phương pháp trực tiếp "
        "hay tia hở, khí nén gặp áp suất ngược do trở lực mà chi tiết đo tạo ra. Kịch bản điển hình là "
        "đầu đo và chi tiết có hình học tương tự nhau — ví dụ một đầu đo hình trụ nằm trong một lỗ đã "
        "gia công. Đặt hai đầu đo ở hai phía của một tấm phẳng thì có thể suy ra chiều dày. Trong phương "
        "pháp gián tiếp hay tiếp xúc, khí nén đẩy một chi tiết tiếp xúc đặt trực tiếp lên vật. Có thể đo "
        "được dung sai nhỏ tới 50 nm. (Nhà cung cấp: Willrich Precision Instrument Co.; Moore Products "
        "Co.)"))
    b.append(fig(5, hb7fig.fig_7_5()))

    # 7.1.4
    b.append(h3("Quang học: lấy nét, che bóng, so sánh", "Optical: Focusing, Shadowing, Comparing"))
    b.append(p(
        "Nhóm này gồm kính hiển vi, có thể xác định chiều dày bằng cách so với một chuẩn đã biết, hoặc "
        "bằng cách lấy nét lần lượt lên mặt trước và mặt sau của mẫu rồi ghi nhận hiệu vị trí lấy nét. "
        "Bộ so sánh chiếu lên màn những gì có thể quan sát qua kính hiển vi. Thước cặp laser thu kích "
        "thước bằng cách đo bóng của một chùm laser. (Nhà cung cấp: NDC Systems cho thước cặp laser; "
        "Scantron cho máy đo biên dạng laser.)"))

    # 7.1.5
    b.append(h3("Cân", "Weighing"))
    b.append(p(
        "Cho một tấm vật liệu đã biết khối lượng riêng, trước hết đo diện tích bằng một hệ video đã hiệu "
        "chuẩn. Sau đó chỉ cần một phép cân là quy đổi được thành ước lượng chiều dày:"))
    b.append(eq("d = m / (ρ · A)"))
    b.append(p(
        "Như thường thấy với kỹ thuật này và với hầu hết các kỹ thuật tiếp theo, ước lượng chiều dày đòi "
        "hỏi phải biết một tính chất khác của vật liệu cần đo — ở đây là khối lượng riêng. Đó là cái giá "
        "phải trả cho sự đơn giản: kỹ thuật càng ít phụ thuộc vào vật liệu thì càng phức tạp về thiết bị."))

    # 7.1.6
    b.append(h3("Đo điện dung", "Capacitive Gaging"))
    b.append(p(
        "Đo điện dung được thực hiện bằng cách đưa một vật liệu phi kim vào một điện trường đã biết. Biết "
        "diện tích bản cực của đầu đo và hằng số điện môi của vật liệu, có thể xác định được chiều dày. "
        "Có thể đạt tới mức dưới micromét. (Nhà cung cấp: Ono Sokki; SolveTech.)"))
    b.append(fig(6, hb7fig.fig_7_6()))

    # 7.1.7
    b.append(h3("Đo cảm ứng (cảm nhận dòng xoáy)", "Inductive Gaging (Eddy Current Sensing)"))
    b.append(p(
        "Nguyên lý ở đây là dòng xoay chiều trong một cuộn dây cảm ứng ra dòng xoáy trong một tấm dẫn "
        "điện ở gần [4, 5]. Những dòng xoáy này có thể được cảm nhận bằng một cuộn thu, có thể chính là "
        "cuộn kích hoặc một cuộn thứ hai. Sự có mặt của dòng xoáy biểu hiện ra như một thay đổi của độ "
        "tự cảm biểu kiến và/hoặc của tổn hao trong cuộn thu. Kỹ thuật này thích hợp với kim loại không "
        "sắt, và đặc biệt nhạy với những biến thiên chiều dày do khuyết tật như nứt hay ăn mòn."))
    b.append(p(
        "Có một trường hợp riêng mà người ta thường đo chiều dày chứ không đo biến thiên: chiều dày của "
        "một lớp phủ phi dẫn trên một nền dẫn điện không sắt. Lớp phủ tạo ra một khe hở (lift-off) giữa "
        "cuộn kích và dòng xoáy, do đó ảnh hưởng lên tín hiệu dòng xoáy. Dải của kỹ thuật này vào khoảng "
        "1 mm. Hãng Fischer có một thiết bị đo chiều dày lớp phủ mặt đường mới rải tới độ sâu 40 cm, "
        "bằng cách chôn một tấm dẫn điện bên dưới mặt đường. (Nhà cung cấp: Fischer; deFelsko; CMI "
        "International.)"))
    b.append(fig(7, hb7fig.fig_7_7()))

    # 7.1.8
    b.append(h3("Cảm ứng từ", "Magnetic Induction"))
    b.append(p(
        "Kỹ thuật này cũng dùng để đo chiều dày lớp phủ, ở đây là lớp phủ phi từ trên một nền sắt từ. "
        "Lớp phủ phi từ tạo ra một khe hở (lift-off) giữa nền sắt từ và đầu dò. Một cách đo khe hở — và "
        "do đó đo chiều dày — là đo lực cần thiết để kéo bật một đầu dò nam châm ra. Một cách khác là "
        "ghép từ nền sắt từ với lõi một biến áp, với một khe hở giữa nền và lõi. Kỹ thuật này có dải "
        "khoảng 4 mm."))
    b.append(fig(8, hb7fig.fig_7_8()))
    b.append(p(
        "Hãng CMI International có một tài liệu giới thiệu khá hữu ích, so sánh ưu nhược điểm của các "
        "cách đo chiều dày lớp phủ bằng dòng xoáy, cảm ứng từ, tán xạ ngược beta, điện trở vi lượng và "
        "huỳnh quang tia X; việc chọn kỹ thuật phụ thuộc, cùng nhiều thứ khác, vào vật liệu cần kiểm "
        "tra. (Nhà cung cấp: Fischer; CMI International; Electromatic; deFelsko.)"))

    # 7.1.9
    b.append(h3("Đầu đo Hall", "Hall Effect Gage"))
    b.append(p(
        "Cảm biến này đo chiều dày vật liệu không sắt với độ chính xác 1 % bằng cách kẹp vật cần đo giữa "
        "một đầu dò nam châm ở một phía và một bi thép nhỏ làm bia ở phía kia [6]. Nó đo được tới 10 mm. "
        "Cảm biến Hall được dùng để đo từ trường như một phép đo một chiều; các phép đo Hall xoay chiều "
        "có thể thực hiện chính xác hơn vì chúng loại bỏ được độ lệch và ít nhiễu hơn. (Nhà cung cấp: "
        "Panametrics.)"))
    b.append(fig(9, hb7fig.fig_7_9()))

    # 7.1.10
    b.append(h3("Trường xa / thời gian bay: siêu âm, radar, lidar",
                "Far-Field / Time-of-Flight"))
    b.append(p(
        "Dùng nguyên lý sonar của thập niên 1940 và công nghệ vi xử lý ngày nay, sóng siêu âm tần số cao "
        "(1–20 MHz) có thể được dùng để đo chiều dày bằng cách phát các xung âm qua vật liệu và đo thời "
        "gian truyền của tín hiệu phản xạ [5, 7]. Biết vận tốc âm trong vật liệu, có thể đo được vật liệu "
        "dày từ 0,5 mm tới 250 mm, thường chính xác tới 25 µm. Môi trường truyền gồm kim loại, thuỷ "
        "tinh, gốm, chất lỏng, cao su, sợi thuỷ tinh, nhựa và bê tông."))
    b.append(fig(10, hb7fig.fig_7_10()))
    b.append(p(
        "Siêu âm cũng dùng được để đo mô sống, như vẫn thường làm trong nông nghiệp và y học. Lớp mỡ của "
        "bò và lợn có thể ảnh hưởng tới giá bán. Độ sâu bỏng da có thể định hướng cách điều trị. Độ sâu "
        "của dị vật trong cơ thể có ích cho vi phẫu. Việc xác định chiều dày bằng siêu âm đã mở rộng "
        "sang các ứng dụng định vị bằng tiếng vang đa chiều, như ảnh hoá và kính hiển vi âm học có thể "
        "phân giải tới mức dưới micromét."))
    b.append(p(
        "Những nguyên lý đứng sau siêu âm cũng áp dụng cho sóng điện từ. Ở dải gigahertz, nó được gọi là "
        "radar. Radar có thể dùng để ước lượng chiều dày các lớp khí quyển, ví dụ các lớp mây. Phiên bản "
        "dùng ánh sáng của radar, gọi là lidar, có thể dùng để đo chiều dày các lớp hơi nước ở tầng thấp "
        "của khí quyển. (Nhà cung cấp siêu âm: KTa-Tator; deFelsko; Stresstel; Magnetic Analysis Corp.; "
        "Panametrics; Electromatic.)"))

    # 7.1.11
    b.append(h3("Trường xa / cộng hưởng: siêu âm, giao thoa, ellipsometry",
                "Far-Field / Resonance"))
    b.append(p(
        "Ý tưởng ở đây là: khi sóng — chẳng hạn siêu âm — đập vào một bản phẳng song song, sẽ có công "
        "suất phản xạ từ cả mặt trước lẫn mặt sau; tuỳ theo chiều dày bản là một số lẻ hay số chẵn lần "
        "một phần tư bước sóng, hai chùm phản xạ sẽ giao thoa tăng cường hoặc triệt tiêu. Nếu quét tần "
        "số, khoảng cách tần số giữa các cực đại và cực tiểu liên tiếp có thể liên hệ với chiều dày bản, "
        "miễn là biết chiết suất. Vì các mode riêng — mode cộng hưởng — của một vật phụ thuộc vào tính "
        "chất và kích thước của vật, biết tính chất thì cho phép ước lượng kích thước từ các tần số "
        "cộng hưởng."))
    b.append(p(
        "So với siêu âm thời gian bay, siêu âm cộng hưởng ít phổ biến hơn nhiều. Nó đã được dùng để đặc "
        "trưng bê tông, và rất nhạy với khuyết tật — như bất cứ ai đã từng nghe một cái chuông bị nứt "
        "đều biết. Kỹ thuật cộng hưởng phổ biến hơn nhiều với bức xạ khả kiến [8], hồng ngoại hoặc vi "
        "ba [4]."))
    b.append(p(
        "Giao thoa kế phổ thích hợp để đặc trưng chiều dày của những đế trong suốt có bề mặt khá phẳng "
        "và đủ song song với nhau. Cách làm thông thường là đo phổ truyền qua bằng một máy quang phổ, ví "
        "dụ máy quang phổ biến đổi Fourier (FTS). Các cực đại và cực tiểu liên tiếp ở đây được gọi là "
        "hiệu ứng Fabry–Perot, và sự xuất hiện của chúng trong một phổ được gọi là kênh hoá "
        "(channeling)."))
    b.append(fig(11, hb7fig.fig_7_11()))
    b.append(p(
        "Cũng có thể đo chiều dày bằng giao thoa kế không gian, thực chất là một cách đo địa hình bề "
        "mặt. Một ví dụ là hiện tượng vân tròn Newton, xuất hiện khi bề mặt cần kiểm tra tiếp xúc với "
        "một tấm phẳng quang học. Dùng một tấm phẳng quang học trong suốt, cho ánh sáng đơn sắc — ví dụ "
        "đèn thuỷ ngân — truyền qua tấm rồi tới mặt phân cách giữa tấm và bề mặt mẫu. Nếu bề mặt mẫu có "
        "biến thiên độ cao, hai chùm phản xạ từ tấm phẳng và từ bề mặt mẫu sẽ xen kẽ giữa giao thoa tăng "
        "cường và triệt tiêu, tạo ra các vân hay các vòng."))
    b.append(fig(12, hb7fig.fig_7_12()))
    b.append(p(
        "Độ nhạy không bị giới hạn ở thang bước sóng λ: với đủ độ ổn định và đủ tỉ số tín hiệu trên "
        "nhiễu, có thể đo tới 1/1000 vân. Với những nguồn có độ dài kết hợp lớn hơn, như laser, bề mặt "
        "mẫu và tấm phẳng quang học không cần tiếp xúc trực tiếp."))
    b.append(p(
        "Một cách quang học khác để đo chiều dày là ellipsometry [9], thường dùng để đo tính chất của "
        "màng mỏng trong suốt dày từ vài phần mười nanomét tới vài trăm nanomét. Cách này áp dụng được "
        "cho cả kim loại, miễn là kim loại đủ mỏng để trong suốt một phần. Bằng cách đo sự thay đổi "
        "trạng thái phân cực của ánh sáng tới không vuông góc, có thể suy ra đồng thời cả chiều dày lẫn "
        "chiết suất của lớp mỏng. Có thể thu thêm thông tin — ví dụ tính chất của nhiều lớp — bằng cách "
        "thay đổi góc tới và quan sát ở nhiều bước sóng."))
    b.append(p(
        "Khả năng ước lượng đồng thời cả chiều dày lẫn chiết suất là một ưu điểm quan trọng của kỹ thuật "
        "này, vì chiết suất của một vật liệu ở dạng màng mỏng thường không giống giá trị khối, và thật "
        "ra có thể là một thuộc tính của chính điều kiện lắng đọng. (Nhà cung cấp FTS: Bomem; Digilab; "
        "Mattson; Midac; Nicolet; Perkin-Elmer. Giá hệ FTS có thể từ khoảng 15.000 USD tới trên 100.000 "
        "USD tuỳ ứng dụng. Nhà cung cấp giao thoa kế không gian: Zygo; Wyko; Phase-Shift Technology. Nhà "
        "cung cấp ellipsometer: J.A. Woollam Co., Inc.; Rudolf Instruments; Sentech. Giá một ellipsometer "
        "có thể từ 10.000 USD cho hệ thủ công một bước sóng tới 200.000 USD cho hệ tự động đa bước "
        "sóng. Nhà cung cấp cộng hưởng vi ba: Hewlett-Packard.)"))

    # 7.1.12
    b.append(h3("Trường xa / hấp thụ, tán xạ, phát xạ: beta, gamma, tia X, hồng ngoại",
                "Far-Field / Absorption, Scattering, Emission"))
    b.append(p(
        "Những kỹ thuật này dựa vào sự tắt (tán xạ hoặc hấp thụ) hay sự phát xạ của photon hoặc của các "
        "hạt có khối lượng (electron, proton, neutron) khi chúng đi qua vật liệu cần đo. Thông thường, "
        "độ tắt hoặc độ phát xạ phụ thuộc hàm mũ vào chiều dày; sự phụ thuộc trở thành tuyến tính nếu "
        "độ hấp thụ đủ thấp. Những kỹ thuật này — đặc biệt là tán xạ ngược tia gamma và truyền qua tia "
        "beta — được dùng để đo liên tục các vật liệu dạng cuộn đang chuyển động (giấy, kim loại, vải) "
        "trên dây chuyền. Hấp thụ hồng ngoại cũng thích hợp nếu độ ẩm được kiểm soát."))
    b.append(fig(13, hb7fig.fig_7_13()))
    b.append(p(
        "Tán xạ ngược beta và huỳnh quang tia X [10] được dùng để đo lớp phủ. Trong huỳnh quang tia X, "
        "khi bị chiếu tia X, một số nguyên tố phát huỳnh quang — tức phát xạ — tia X ở những bước sóng "
        "đặc trưng. Cường độ phát xạ này liên hệ với chiều dày. Những kỹ thuật hấp thụ/phát xạ này đôi "
        "khi thích hợp hơn siêu âm thời gian bay để đo kích thước những vật có hình dạng phức tạp. (Nhà "
        "cung cấp đồng hồ gamma: NDC Systems. Hấp thụ tia X: Measurex. Huỳnh quang tia X: Fischer; NDC "
        "Systems; CMI International. Tán xạ ngược beta: Fischer; Electromatic; CMI International; "
        "Measurex. Hấp thụ hồng ngoại: NDC Systems. Giá các hệ này tuỳ ứng dụng; một hệ điển hình có thể "
        "có giá 500.000 USD.)"))

    # 7.1.13
    b.append(h3("Kỹ thuật phá huỷ", "Destructive Techniques"))
    b.append(p(
        "Hãng Fischer bán một hệ thống hoà tan lớp phủ vào một chất điện phân rồi sau đó lắng đọng lại "
        "lớp phủ đã hoà tan bằng điện phân. Điện tích cần cho việc lắng đọng liên hệ với chiều dày lớp "
        "phủ."))

    b.append(table(
        ["Hãng", "Model", "Giá (USD, 1999)", "Mô tả"],
        [["KTa-Tator", "TI-12", "1.595", "đồng hồ siêu âm đa dụng, dải 0,75 – 75 mm"],
         ["NDC Systems", "6100TC", "49.300", "đồng hồ gamma tán xạ ngược cho cuộn rộng 60 in, dải 25 mm"],
         ["NDC Systems", "—", "66.600", "đồng hồ truyền qua beta, cho sản phẩm dạng cuộn liên tục"],
         ["Panametrics", "25DL", "2.200 – 3.800", "đồng hồ siêu âm một phần tử, dải 50 mm"],
         ["Panametrics", "26DL Plus", "1.400 – 2.500", "đồng hồ siêu âm hai phần tử, dải 250 mm"],
         ["Panametrics", "8000", "6.500", "đồng hồ từ Hall, cho vật liệu không sắt, dải 6 mm"],
         ["DeFelsko", "Positest 1000-N", "1.995",
          "cảm biến dòng xoáy, hiển thị trên Apple Newton, đo tới 1,5 mm lớp không dẫn trên nền dẫn"],
         ["Magnetic Analysis", "nhiều loại", "1.500 – 100.000", "đồng hồ siêu âm thời gian bay"],
         ["Fischer", "Deltascope MP2C", "1.200",
          "đồng hồ cảm ứng từ, đo lớp phủ phi từ trên nền sắt từ"],
         ["Fischer", "IsoScope MP1C", "1.200",
          "đồng hồ dòng xoáy, đo lớp phủ không dẫn trên nền dẫn không sắt"],
         ["Fischer", "Fischerscope MMS", "6.500", "hệ tán xạ ngược beta đo chiều dày lớp phủ"],
         ["Fischer", "Fischerscope X-Ray 1020 video", "34.000",
          "hệ huỳnh quang tia X đo chiều dày lớp phủ"],
         ["Fischer", "Couloscope Sx", "2.500 + phụ kiện",
          "hệ điện phân, phá huỷ, đo chiều dày lớp phủ"],
         ["J.A. Woollam Co. Inc.", "M-44", "tuỳ ứng dụng",
          "ellipsometer quang phổ đa bước sóng, góc thay đổi"],
         ["Rudolf Instruments", "431A31WL633", "10.100", "ellipsometer thủ công, bước sóng HeNe"],
         ["Rudolf Instruments", "444A12", "34.000", "ellipsometer tự động, bước sóng HeNe"],
         ["Hewlett Packard", "HP8712C", "13.500",
          "máy phân tích mạng vector RF, đo đáp ứng tần số truyền/phản xạ tới 1,3 GHz, tuỳ chọn 3 GHz"],
         ["Stresstel", "T-Mike", "995", "hệ siêu âm hai phần tử, lập trình được"],
         ["Stresstel", "TM1D", "1.795", "hệ siêu âm một phần tử"],
         ["Measurex", "DMC480", "tuỳ ứng dụng", "đồng hồ tia X đo chiều dày tốc độ cao"],
         ["Bomem", "dòng MB", "20.000 trở lên",
          "máy quang phổ biến đổi Fourier, phân giải 1 cm⁻¹"],
         ["Park Scientific Instruments", "Autoprobe CP", "65.000",
          "kính hiển vi đầu dò quét trong khí quyển"],
         ["Park Scientific Instruments", "Autoprobe VP2", "130.000",
          "kính hiển vi đầu dò quét siêu chân không"],
         ["Digital Instruments", "Nanoscope IIIa/D3000", "90.000",
          "kính hiển vi đầu dò quét cho mẫu nhỏ"]],
        "Bảng 7.3 · Dụng cụ đo chiều dày. Giá là giá niêm yết năm 1999, chưa quy đổi; đây là một bảng "
        "chụp nhanh thị trường chứ không phải bảng giá hiện hành."))

    # ---- 7.2
    b.append(h2("7.2 Hướng phát triển của việc đo chiều dày", "Future Directions"))

    b.append(h3("Về những kỹ thuật đã nêu", "Concerning the Techniques Above"))
    b.append(p(
        "Với cảm biến điện dung, Trung tâm Nghiên cứu Langley của NASA đang phát triển những cảm biến "
        "dựa trên các mẫu dây dẫn kẹp giữa các lớp cách điện. Sự có mặt của băng trên các dây dẫn làm "
        "thay đổi điện dung, cho một cách cảm nhận lớp băng bám trên cánh máy bay."))
    b.append(p(
        "Với cảm nhận dòng xoáy, một hạn chế là cuộn cảm phi siêu dẫn đáp ứng tốt nhất với kích thích "
        "tần số cao, và hoàn toàn không đáp ứng với từ trường một chiều. Điều này giới hạn kỹ thuật ở "
        "tần số khá cao, và do đó ở độ xuyên nông, vì độ sâu da càng nông khi tần số càng tăng. Một khả "
        "năng là dùng SQUID (thiết bị giao thoa lượng tử siêu dẫn) làm cảm biến, vì SQUID có lẽ là cảm "
        "biến nhạy nhất với từ trường một chiều và tần số thấp. Một nhược điểm của SQUID từng là phải "
        "dùng heli lỏng để làm lạnh chất siêu dẫn nhiệt độ thấp; với sự sẵn có gần đây của chất siêu dẫn "
        "nhiệt độ cao (HTS, trên 90 K) và nay là SQUID HTS, có thể làm lạnh bằng nitơ lỏng hoặc bằng "
        "máy làm lạnh cơ một cấp."))
    b.append(p(
        "Trong lĩnh vực giao thoa kế không gian, công trình ở Phòng thí nghiệm Quốc gia Lawrence "
        "Livermore thay bề mặt chuẩn bằng một sợi đơn mode, trong một quá trình gọi là giao thoa kế nhiễu "
        "xạ dịch pha. Độ chính xác đo được công bố là 1,44 nm rms, với mục tiêu 0,1 nm rms. (Nhà cung "
        "cấp SQUID HTS: Conductus.)"))

    b.append(h3("Công nghệ THz", "THz Technology"))
    b.append(p(
        "Với sự sẵn có của laser xung femto giây, Bell Labs đã nghiên cứu một kỹ thuật dùng xung 100 fs "
        "để kích một anten trong dải 0,1 THz tới 3,0 THz. Các xung terahertz được cho truyền qua vật liệu "
        "cần kiểm tra, được thu nhận, rồi dạng xung nhận được đem phân tích để rút ra thông tin về thành "
        "phần cấu tạo. Kỹ thuật này cũng có thể cung cấp thông tin về chiều dày."))
    b.append(fig(16, hb7fig.fig_7_16()))

    b.append(h3("Kính hiển vi đầu dò quét cỡ nanomet", "Nanoscale Scanning Probe Microscopy"))
    b.append(p(
        "Kính hiển vi đầu dò quét (SPM) được dùng trong rất nhiều ngành, gồm khoa học bề mặt cơ bản, "
        "phân tích độ nhám bề mặt thường quy, và ảnh hoá ba chiều ngoạn mục — từ các nguyên tử silic tới "
        "những gờ cỡ micromét trên bề mặt một tế bào sống [11]. Kính hiển vi đầu dò quét là một công cụ "
        "tạo ảnh có dải động rộng, trùm lên cả lãnh địa của kính hiển vi quang học lẫn kính hiển vi điện "
        "tử. Nó cũng là một máy đo biên dạng với độ phân giải 3D chưa từng có. Trong một số trường hợp, "
        "SPM còn đo được các tính chất vật lý như độ dẫn bề mặt, phân bố điện tích tĩnh, ma sát cục bộ, "
        "từ trường và mô đun đàn hồi. Vì thế ứng dụng của SPM rất đa dạng."))
    b.append(p(
        "Kính hiển vi quét xuyên hầm (STM), thuỷ tổ của họ SPM, dùng một mũi dò dẫn điện nhọn với một "
        "điện áp phân cực đặt giữa mũi dò và mẫu. Khi mũi dò cách mẫu trong vòng 1 nm, electron từ mẫu "
        "bắt đầu xuyên hầm qua khe 1 nm vào mũi dò. Nếu đảo chiều phân cực, hiện tượng xuyên hầm xảy ra "
        "theo chiều ngược lại, vào mẫu. Dòng xuyên hầm là một hàm của khoảng cách. Cả mũi dò lẫn mẫu đều "
        "phải là chất dẫn điện hoặc bán dẫn."))
    b.append(fig(15, hb7fig.fig_7_15()))
    b.append(p(
        "Kính hiển vi lực nguyên tử (AFM) dùng một mũi nhọn nhỏ ở đầu một dầm công xôn. Lực giữa mũi dò "
        "và mẫu làm dầm công xôn uốn, và độ uốn này được chuyển thành tín hiệu. Mũi dò hoặc mẫu có thể "
        "được quét trên một diện tích lớn, tạo ra một bản đồ địa hình. AFM dùng được trên chất cách điện "
        "lẫn chất dẫn điện."))
    b.append(fig(14, hb7fig.fig_7_14()))
    b.append(p(
        "AFM hoạt động ở hai chế độ: tiếp xúc và không tiếp xúc. Ở chế độ tiếp xúc, mũi dò được đưa tới "
        "trong khoảng 200 pm — cỡ độ dài một liên kết hoá học. Đám mây electron của mũi dò và của nguyên "
        "tử mẫu tương tác, cho ra một lực đẩy. Vì thế chế độ tiếp xúc còn được gọi là chế độ đẩy. Có thể "
        "đạt độ phân giải thẳng đứng khoảng 50 pm. Ở chế độ không tiếp xúc, người ta dùng một dầm công "
        "xôn rung trong vùng hút của tương tác van der Waals. Dầm công xôn thường cách bề mặt mẫu từ "
        "2 nm tới 20 nm và chịu tổng lực nhỏ. Do đó AFM không tiếp xúc kém nhạy hơn, nên phải dùng những "
        "hệ đo xoay chiều nhạy. Bù lại, lực nhỏ có ưu điểm là không làm nhiễm bẩn bề mặt mẫu, và được "
        "ưu tiên cho các ứng dụng liên quan tới phiến silic và mô mềm hoặc đàn hồi."))
    b.append(p(
        "Ở chế độ không tiếp xúc, dầm công xôn được cho cộng hưởng với biên độ nhỏ. Khi mũi dò tới gần "
        "bề mặt mẫu, lực tổng hợp làm thay đổi hằng số lò xo, và điều đó chuyển thành một độ lệch của "
        "tần số cộng hưởng. Sự thay đổi cộng hưởng — hoặc biên độ dao động — này phản ánh những thay đổi "
        "của địa hình mẫu."))
    b.append(p(
        "Chế độ tiếp xúc gián đoạn là sự kết hợp của chế độ không tiếp xúc và chế độ tiếp xúc, và thích "
        "hợp nhất với những mẫu mềm, dính hoặc dễ vỡ. Chế độ tiếp xúc có thể làm hỏng mũi dò và mẫu do "
        "lực ma sát hoặc lực cắt, và/hoặc tạo ra các hiện tượng giả do mũi dò dính vào bề mặt. Chế độ "
        "không tiếp xúc cho biên độ thấp hơn và do đó độ phân giải thấp hơn; hơn nữa, những đơn lớp khí "
        "hấp phụ trên bề mặt, như hơi nước, có thể gây ra kết quả sai. Chế độ tiếp xúc gián đoạn tránh "
        "được những cạm bẫy ấy bằng cách đặt mũi dò tiếp xúc với bề mặt để có độ phân giải cao, rồi nhấc "
        "mũi dò lên để tránh kéo lê và/hoặc tránh lực ngang. Dầm công xôn được cho cộng hưởng nhờ một "
        "tinh thể áp điện (50 kHz tới 500 kHz trong không khí, 5 kHz tới 40 kHz trong chất lỏng), thắng "
        "được lực dính giữa mũi dò và mẫu."))
    b.append(p(
        "Trong kính hiển vi lực từ (MFM), chế độ không tiếp xúc được dùng với một mũi dò phủ màng sắt "
        "từ. Cả tương tác từ lẫn tương tác van der Waals đều có mặt, nhưng ở khoảng cách mũi dò – mẫu "
        "lớn hơn thì lực từ chiếm ưu thế. Quét nhiều lần theo hàm của khoảng cách mũi dò – mẫu cho phép "
        "tách riêng lực từ và thông tin địa hình. Cấu trúc đômen từ được phân giải tới 50 nm bằng kỹ "
        "thuật này. Ứng dụng hiện nay của MFM gồm thiết bị lưu trữ dữ liệu, ảnh hoá cấu trúc vi từ, phân "
        "tích mạch tích hợp, ảnh hoá vi khuẩn từ tính và địa vật lý từ."))
    b.append(p(
        "Kính hiển vi lực ngang (LFM) được dùng để tạo biên dạng những thay đổi của ma sát bề mặt "
        "và/hoặc biến thiên độ cao. Mũi dò bị lệch theo phương ngang, cho thấy một kiểu xoắn nào đó. "
        "Phần điện tử đo độ uốn của dầm công xôn. Để phân biệt hai hiệu ứng, phải thu ảnh LFM và ảnh AFM "
        "đồng thời."))
    b.append(p(
        "Kính hiển vi phát hiện pha, hay tạo ảnh pha, là một mở rộng của AFM tiếp xúc gián đoạn. Nó dùng "
        "độ trễ pha giữa tần số kích (của dầm công xôn) và tần số tín hiệu ra, tạo ra một bản đồ các "
        "tính chất cơ học đặc thù như độ dính, độ đàn hồi và ma sát. Có thể nhận dạng tạp chất, vật liệu "
        "composite, và các vùng cứng hoặc có độ dính bề mặt thấp ở thang nanomét."))
    b.append(p(
        "Các kỹ thuật bổ sung gồm: <i>kính hiển vi điều biến lực</i>, trong đó một tín hiệu tuần hoàn "
        "được đặt lên dầm công xôn, tạo ra bản đồ mô đun đàn hồi và/hoặc tạp chất của mẫu; <i>kính hiển "
        "vi lực tĩnh điện</i>, trong đó một mũi dò tích điện được quét trên mẫu, làm lộ ra các đômen "
        "tích điện cục bộ và tạo ra bản đồ mật độ hạt tải; <i>kính hiển vi điện dung quét</i>, trong đó "
        "một mũi dò tích điện giữ ở khoảng cách không đổi tới mẫu tạo ra bản đồ thông tin liên quan tới "
        "điện dung, như chiều dày vật liệu điện môi và phân bố hạt tải dưới bề mặt (tức biên dạng pha "
        "tạp của bán dẫn cấy ion); và <i>kính hiển vi quét nhiệt</i>, trong đó mũi dò ở chế độ không "
        "tiếp xúc cùng một dầm công xôn lưỡng kim được dùng để lập bản đồ độ dẫn nhiệt của mẫu. (Nhà "
        "cung cấp: Park Scientific Instruments; Digital Instruments; Oxford Instruments.)"))

    b.append(quote(
        "Mỗi kỹ thuật trong chương này đánh đổi một thứ khác để lấy chiều dày: quyền tiếp cận cả hai "
        "mặt, quyền tiếp xúc, hoặc quyền biết trước một tính chất của vật liệu.",
        "Tổng hợp từ §7.1"))

    b.append('<h2>Thư mục <span class="en">References</span></h2>')
    b.append('<ol class="ref-list">'
             '<li>R. E. Green (ed.), <i>Machinery’s Handbook</i>, 24th ed., New York: Industrial Press, 1992.</li>'
             '<li>F. T. Farago and M. A. Curtis, <i>Handbook of Dimensional Measurement</i>, 3rd ed., New '
             'York: Industrial Press, 1994.</li>'
             '<li>T. Busch, <i>Fundamentals of Dimensional Metrology</i>, 2nd ed., Albany, NY: Delmar '
             'Publishers, 1989.</li>'
             '<li>R. C. McMaster, P. McIntire, and M. L. Mester (eds.), <i>Nondestructive Testing '
             'Handbook</i>, Vol. 4, 2nd ed., American Society for Nondestructive Testing, 1986.</li>'
             '<li>D. E. Bray and D. McBride, <i>Nondestructive Testing Techniques</i>, New York: John Wiley '
             '& Sons, 1992.</li>'
             '<li>M. Giannini and A. deChiara, <i>Wall Thickness Gaging in the Blow Mold Industry</i>, '
             'phát hành bởi Panametrics.</li>'
             '<li>A. S. Birks, R. E. Green, and P. McIntire (eds.), <i>Nondestructive Testing Handbook</i>, '
             'Vol. 7, 2nd ed., American Society for Nondestructive Testing, 1991.</li>'
             '<li>D. Malacara, <i>Optical Shop Testing</i>, New York: John Wiley & Sons, 1978.</li>'
             '<li>J. A. Woollam and P. G. Snyder, <i>Variable Angle Spectroscopic Ellipsometry</i>, VASE, '
             'phát hành bởi J.A. Woollam Co.</li>'
             '<li>H. H. Behncke, “Coating thickness measurement by the X-ray fluorescence method,” '
             '<i>Metal Finishing</i>, tháng 5, tr. 33–39, 1984.</li>'
             '<li>R. Howland and L. Benatar, <i>A Practical Guide to Scanning Probe Microscopy</i>, Park '
             'Scientific Instruments, 1993.</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%sch06-displacement-measurement/"><span class="k">← Chương 6</span>Đo dịch chuyển, '
             'thẳng và góc</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This is the shortest chapter in the handbook’s measurement section and, in a sense, the widest: "
        "it spans thirty orders of magnitude. The authors open by walking the reader from a galaxy a "
        "hundred exametres thick down to Martian microfossils under a hundred nanometres, then narrow to "
        "the band industry actually occupies — metres on a construction site, millimetres on an assembly "
        "line, micrometres and nanometres in the solid-state, optical and coatings trades."))

    b.append(fig(1, hb7fig.fig_7_1(), "en"))

    b.append(p(
        "The organising idea is not the instrument but the constraint. A caliper works when both faces "
        "are reachable, the object is the right size, and it can be touched. Every other technique in the "
        "chapter exists because one of those three conditions fails."))

    b.append(fig(2, hb7fig.fig_7_2(), "en"))

    b.append(p(
        "The chapter then divides the mature techniques by the physics they exploit, and the division is "
        "worth taking seriously because it predicts what each one is good for. Contact instruments "
        "compare against a graduated scale. Field instruments — capacitive, inductive, magnetic, Hall — "
        "infer thickness from how a field is disturbed by the material in its path, which means they need "
        "a property of the material as a co-input. Time-of-flight instruments measure a duration. "
        "Resonance instruments measure a frequency. Absorption and emission instruments measure an "
        "intensity. Each choice of observable fixes the accuracy, the range, and the failure mode."))

    b.append(h2("The hidden co-input"))
    b.append(p(
        "The single most useful observation in the chapter is buried in one sentence about weighing: "
        "estimating thickness requires knowing some other property of the material — in that case, the "
        "density. The same is true, in different guises, of almost every indirect method. Capacitive "
        "gauging needs the dielectric constant. Ultrasonic time-of-flight needs the sound velocity. "
        "Eddy-current and magnetic methods need to know whether the substrate is ferrous. Ellipsometry "
        "needs the refractive index — and the chapter makes the sharp point that the refractive index of "
        "a thin film is often not the bulk value at all, but a property of the deposition conditions. "
        "That is why ellipsometry’s ability to solve for thickness and index together is not a "
        "convenience but the whole reason the technique survives."))

    b.append(p(
        "Read this way, the table of techniques is really a table of what you must already know before "
        "you can measure. The techniques that need the least prior knowledge — mechanical contact and "
        "time-of-flight ultrasound, which only needs the sound speed — are the ones with the widest "
        "deployment. The ones that need the most — beta backscatter, X-ray fluorescence — buy their "
        "independence from geometry at the price of a calibration standard matched to the material."))

    b.append(fig(3, hb7fig.fig_7_3(), "en"))

    b.append(h2("Why the micrometer still wins"))
    b.append(p(
        "A micrometer reads to 0.01 mm with no electronics, no calibration certificate and no material "
        "assumptions: a 0.5 mm screw pitch divided into fifty thimble graduations. The arithmetic is "
        "entirely visible to the operator, which is why the instrument has survived a century of "
        "electronic competition in exactly the places where a wrong number is expensive. The electronic "
        "equivalents — the LVDT and its descendants — replace the scale with a differential transformer "
        "and gain range, speed and the ability to log, but they inherit the same geometry: something must "
        "still touch both faces."))

    b.append(fig(4, hb7fig.fig_7_4(), "en"))

    b.append(h2("Three ways to avoid touching the far side"))
    b.append(p(
        "Once contact is impossible, the techniques split three ways. The first keeps a single-sided "
        "probe and reads a field: pneumatic backpressure, capacitance, eddy current, magnetic pull-off, "
        "the Hall sandwich. The second sends something through the material and times it: ultrasound, "
        "radar, lidar. The third sends something through and measures how much comes back or gets "
        "through: beta, gamma, X-ray fluorescence, infrared absorption."))

    b.append(fig(5, hb7fig.fig_7_5(), "en"))

    b.append(p(
        "The pneumatic gauge is the cleanest illustration of a design principle that recurs throughout "
        "instrumentation: the most sensitive operating point is not the obvious one. Backpressure falls "
        "as the square of the gap, so the slope dP/dg peaks at g = g₀/√3, not at contact. A gauge head "
        "set to touch the work would be operating exactly where it can see nothing."))

    b.append(fig(6, hb7fig.fig_7_6(), "en"))

    b.append(p(
        "Capacitance and eddy current are the same story in different currencies. Capacitance goes as "
        "1/d, so sensitivity climbs steeply as the layer thins — which is why the technique lives below a "
        "micrometre. Eddy current sees the coating as lift-off, and lift-off response dies exponentially, "
        "which is why the same physics that reaches 1.5 mm on a coating cannot see through a plate. "
        "Magnetic pull-off is worse still: force falls as the fourth power of gap, a thousandfold within "
        "two millimetres."))

    b.append(fig(7, hb7fig.fig_7_7(), "en"))
    b.append(fig(8, hb7fig.fig_7_8(), "en"))
    b.append(fig(9, hb7fig.fig_7_9(), "en"))

    b.append(h2("Time, frequency, intensity"))
    b.append(p(
        "Pulse-echo ultrasound is the workhorse of the second family, and its arithmetic is the whole "
        "method: half the round-trip time times the sound speed. In steel at 5,900 m/s, two microseconds "
        "is 5.9 mm. Everything else — transducer frequency, coupling, the choice between single and dual "
        "element — is engineering in service of resolving that interval."))

    b.append(fig(10, hb7fig.fig_7_10(), "en"))

    b.append(p(
        "The resonance family converts thickness into a frequency spacing. A plane-parallel slab "
        "transmits alternating maxima and minima as the optical path difference passes through whole and "
        "half wavelengths; the spacing in wavenumber is 1/(2nd), so the slab thickness falls straight out "
        "once the index is known. The same physics, done spatially rather than spectrally, gives Newton’s "
        "rings — and the chapter’s remark that a thousandth of a fringe is measurable is the reason "
        "optical flats remain the reference standard for flatness."))

    b.append(fig(11, hb7fig.fig_7_11(), "en"))
    b.append(fig(12, hb7fig.fig_7_12(), "en"))

    b.append(p(
        "Absorption and emission methods are the only ones in the chapter that work on a moving web "
        "without touching it at all, which is why the paper, plastics and metals industries run gamma and "
        "beta gauges on the line. Their shape is set by the exponential: backscatter saturates, so it is a "
        "thin-layer method; transmission never saturates, so it is a plate method."))

    b.append(fig(13, hb7fig.fig_7_13(), "en"))

    b.append(h2("The nanoscale end"))
    b.append(p(
        "Section 7.2 turns to what was, in 1999, the frontier. The scanning probe microscope is the only "
        "instrument in the chapter that measures thickness by measuring topography directly at atomic "
        "scale — and the tunnelling current’s exponential dependence on gap is what makes it possible. "
        "With a 4 eV barrier the current drops tenfold every 1.1 Å; a 0.1 Å change in gap is a factor of "
        "two in current, which is comfortably measurable. That is the entire basis of STM’s vertical "
        "resolution."))

    b.append(fig(15, hb7fig.fig_7_15(), "en"))

    b.append(p(
        "The atomic force microscope replaces the tunnelling current with a force, which lets it work on "
        "insulators. Its three modes are not three instruments but three operating points on one "
        "force-distance curve: repulsive contact on the left, the attractive van der Waals tail on the "
        "right, and the intermittent regime in between that avoids both the shear damage of contact and "
        "the contamination sensitivity of non-contact."))

    b.append(fig(14, hb7fig.fig_7_14(), "en"))

    b.append(p(
        "The chapter closes with terahertz time-domain spectroscopy, then a genuinely new capability: a "
        "100 fs pulse occupies 0.1 to 3 THz, a band where many non-conducting materials are transparent "
        "enough to see through and where the pulse carries both dielectric information and thickness."))

    b.append(fig(16, hb7fig.fig_7_16(), "en"))

    b.append(h2("What has changed since 1999"))
    b.append(table(
        ["Then", "Now"],
        [["Vendor tables with street prices and postal addresses",
          "A web search; the tables in 7.2 and 7.3 are a market snapshot, not a buying guide"],
         ["Eddy current limited to high frequency by the skin effect",
          "HTS SQUIDs and giant magnetoresistive sensors extend the low-frequency end"],
         ["Spatial interferometry at 1.44 nm rms, goal 0.1 nm",
          "Routine in semiconductor metrology; the goal was met and passed"],
         ["Terahertz as a laboratory curiosity",
          "Commercial thickness gauges for paint, foam and composite layup"],
         ["Scanning probe microscopy at $65,000–$130,000",
          "Bench-top AFMs an order of magnitude cheaper, plus a family of derived modes"]],
        "Table 7.4 · What has moved since the chapter was written. The physics has not; the "
        "instrumentation has."))

    b.append(p(
        "The Vietnamese translation keeps all three source tables in full, including the 1999 prices, "
        "because they document the state of the market the authors were describing. All sixteen figures "
        "are drawn by the translator — the source chapter has none — and each one states the relation it "
        "was computed from."))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 7 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 7 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 7 “Thickness Measurement” của Brasunas, Cushman và Lakew — "
            "mười ba kỹ thuật đo chiều dày từ thước cặp tới kính hiển vi đầu dò quét, ba bảng tra cứu "
            "và mười sáu hình minh hoạ nguyên lý." if vi else
            "Companion to Chapter 7 of the CRC Measurement Handbook — thickness measurement from calipers "
            "to scanning probe microscopy, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 7'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 7' % BASE_EN)
    meta = ("Chương 7 · theo Ch07.pdf (CRC Press, 1999) · 10 trang gốc · 16 hình, 3 bảng" if vi
            else "Chapter 7 · 10 source pages · 16 figures, 3 tables")
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
