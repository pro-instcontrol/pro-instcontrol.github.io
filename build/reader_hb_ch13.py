# -*- coding: utf-8 -*-
"""Handbook Chapter 13 — Volume Measurement (Rene G. Aarnink, Hessel Wijkstra).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch13.py
"""
import os

import hb13fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch13-volume-measurement"
TITLE_EN = "Volume Measurement"
TITLE_VI = "Đo thể tích"
BYLINE = "Rene G. Aarnink · Hessel Wijkstra · University Hospital Nijmegen"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch12-area-measurement"
PREV_VI = "ch12-area-measurement"
PREV_T_EN = "Area Measurement"
PREV_T_VI = "Đo diện tích"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-13-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Đối với các hình dạng hình học đơn giản, thể tích có thể tính được bằng phương pháp giải tích: "
        "đo các kích thước của vật cần đo rồi áp dụng công thức thể tích tương ứng cho hình dạng đó. Các "
        "công thức này có trong sách giáo khoa hình học, giải tích cũng như các sách tra cứu như <i>Handbook "
        "of Mathematical Science</i> của CRC Press."))
    b.append(p(
        "Thể tích cũng có thể đo bằng phương pháp thay thế chất lỏng. Vật có thể tích cần đo được đặt vào "
        "một bình chứa đã đầy chất lỏng, sau đó đo thể tích ban đầu và thể tích cuối. Thể tích vật bằng "
        "thể tích cuối trừ đi thể tích ban đầu. Kỹ thuật này đặc biệt hữu ích cho các vật có hình dạng "
        "không đều đặn."))
    b.append(p(
        "Chất lỏng còn có thể dùng để đo thể tích các hốc bên trong vật: đổ đầy hốc bằng một chất lỏng, "
        "sau đó đo thể tích chất lỏng sau khi lấy nó ra khỏi hốc."))
    b.append(p(
        "Phần còn lại của chương tập trung vào bài toán cụ thể hơn là đo thể tích trong các ứng dụng y "
        "khoa. Thông tin định lượng về thể tích rất quan trọng đối với bác sĩ lâm sàng trong chẩn đoán nhiều "
        "bệnh và dị thường, đồng thời giúp hiểu rõ hơn sinh lý bệnh. Dữ liệu thể tích dùng trong các ứng "
        "dụng như theo dõi tim mạch, chẩn đoán bệnh tuyến tiền liệt, theo dõi khi ghép tạng, phẫu thuật cắt "
        "bỏ khối u, đo lưu lượng máu, phẫu thuật tạo hình, theo dõi trẻ sinh non, phân tích thành tích thể "
        "thao, v.v. Do phổ ứng dụng rộng, nhiều kỹ thuật đo thể tích đã được phát triển — một số dùng xác "
        "định lượng máu đến cơ quan (động), một số dùng xác định kích thước vật (tĩnh); chúng có thể xâm "
        "lấn hoặc không xâm lấn, dựa trên đo trực tiếp hoặc gián tiếp. Mỗi kỹ thuật có ưu nhược riêng, và "
        "chính ứng dụng sẽ quyết định chọn phương pháp nào."))
    b.append(p(
        "Một trong những kỹ thuật sớm nhất để đo (sự thay đổi) thể tích cơ thể là <b>plethysmography</b> "
        "(đo thể tích bằng buồng kín), nguyên thủy do Glisson (1622) và Swammerdam (1737) phát triển để "
        "chứng minh sự co đẳng thể tích của cơ cô lập. Kỹ thuật gồm bao quanh cơ quan hoặc mô bằng một "
        "hộp cứng chứa nước hoặc khí. Sự thay thế chất lỏng hoặc thay đổi áp suất khí biểu thị sự thay đổi "
        "thể tích mô do dòng chảy vào của động mạch. Có hai loại plethysmography chính, phân biệt theo kỹ "
        "thuật đo sự thay đổi thể tích: <b>thể tích kế</b> (đo thể tích trực tiếp bằng thay thế — gồm kiểu "
        "nước và kiểu khí) và <b>điện trở kế</b> (cảm biến strain-gage, cảm ứng và trở kháng). Điều kiện "
        "vật lý khi đo sẽ quyết định chọn phương pháp plethysmography nào."))
    b.append(p(
        "Những tiến bộ trong chụp ảnh y khoa mở ra khả năng trích xuất phi xâm lấn các thông tin chẩn đoán "
        "định lượng hữu ích. Ảnh được xây dựng trên lưới các phần tử ảnh (pixel) phản ánh cường độ ảnh "
        "tại vị trí đó. Hầu hết ảnh y khoa là phép chiếu hai chiều của vật ba chiều. Các phương thức hình "
        "ảnh phổ biến nhất hiện nay là siêu âm, cộng hưởng từ hạt nhân (MRI), tia X và cắt lớp vi tính (CT). "
        "<b>Siêu âm</b> dựa trên truyền và phản xạ sóng âm tần số cao; <b>cộng hưởng từ</b> dựa trên tương "
        "tác giữa mô-men từ của hạt nhân và từ trường; <b>cắt lớp vi tính (CT)</b> dùng nguồn X-quang "
        "quay, quét qua mặt cắt và tái tạo ảnh từ các phép đo truyền qua."))
    b.append(p(
        "Những kỹ thuật này hiển thị các mặt cắt ngang có thể dùng ước tính kích thước thành phần. Một "
        "cách ước tính thể tích vật trong là giả định hình dạng rồi áp dụng công thức với các kích thước "
        "như dài, cao, rộng. Cách chính xác hơn là <b>phương pháp tích phân mặt cắt bước</b> (step-section "
        "planimetry) — một ứng dụng lâm sàng của tích phân số: ghi các mặt cắt ngang của vật với một khoảng "
        "(cố định), xác định diện tích vật trong mỗi mặt cắt, rồi tính tổng thể tích bằng cách nhân đóng góp "
        "của mỗi mặt cắt với khoảng cách và cộng lại."))
    b.append(p(
        "Thể tích một vùng chứa chất lỏng có thể tính nếu thêm một lượng chất chỉ thị đã biết vào và đo "
        "nồng độ sau khi nó phân tán đều khắp chất lỏng. Việc chọn chất chỉ thị tuỳ thuộc ứng dụng và có "
        "thể dựa trên nhiệt độ, màu sắc hoặc tính phóng xạ."))
    b.append(p(
        "Cuối cùng, (sự thay đổi) thể tích cũng có thể đo trực tiếp bằng <b>đo thể tích thay thế nước</b> — "
        "một phương pháp nhạy nhưng tốn thời gian để đo thể tích một chi; nó không thích hợp cho bệnh nhân "
        "ngay sau phẫu thuật."))

    # ---- 13.1
    b.append(h2("13.1 Nguyên lý plethysmography", "Plethysmography Theory"))
    b.append(p(
        "Lưu lượng chảy vào có thể đo bằng cách chặn dòng chảy ra, rồi đo sự thay đổi thể tích do dòng "
        "chảy vào trong một khoảng thời gian xác định. Plethysmography cho phép xác định sự thay đổi thể "
        "tích một cách khá chính xác. Một thể tích kế thay thế trực tiếp dùng một buồng cứng thường chứa "
        "nước, đặt chi hoặc đoạn chi vào đó. Loại này, đôi khi gọi là <b>plethysmography buồng</b> (chamber "
        "plethysmography), dùng được hai cách: đo chuỗi xung động tỉ lệ với thay đổi thể tích từng nhịp "
        "tim (plethysmography động mạch hay rheography); và đo tổng lượng máu chảy vào chi hoặc ngón tay "
        "bằng <b>tắc tĩnh mạch</b> — bơm một vòng băng ép đặt phía trên chi, ép tới áp suất vừa trên áp "
        "suất tĩnh mạch 5–8 kPa (40–60 mm Hg), khiến máu động mạch vào được vùng đó nhưng máu tĩnh mạch "
        "không thể ra, làm thể tích chi tăng mỗi nhịp tim một lượng bằng thể tích máu vào trong nhịp đó."))

    b.append(h3("Plethysmography khí/nước hay buồng", "Air/Water Plethysmography or Chamber Plethysmography"))
    b.append(p(
        "<b>Plethysmography khí</b> dùng quan hệ giữa sự thay đổi thể tích của một khí trong hệ kín và áp "
        "suất, nhiệt độ tương ứng [1]. Quan hệ giữa áp suất và thể tích được mô tả bởi định luật Boyle:"))
    b.append(eq("P<sub>i</sub> V<sub>i</sub> = P<sub>f</sub> V<sub>f</sub>", "13.1"))
    b.append(p(
        "với P<sub>i</sub>, V<sub>i</sub> là áp suất và thể tích ban đầu, P<sub>f</sub>, V<sub>f</sub> là áp "
        "suất và thể tích cuối, đo ở nhiệt độ không đổi. Sự thay thế chất lỏng hay nén khí là phép đo trực "
        "tiếp lưu lượng máu hay thể tích ban đầu. Thiết bị plethysmograph khí dùng sự thay đổi áp suất "
        "trong một vòng băng ép quấn quanh đoạn chi do thay đổi thể tích gây ra. Bơm vòng băng tới khoảng "
        "60 mm Hg, dòng chảy vào động mạch gây những tăng áp suất nhỏ, được theo dõi qua chu kỳ tim (xem "
        "Hình 13.1). Lưu lượng máu đo được bằng cách so sánh thay đổi áp suất với thay đổi do rút một lượng "
        "khí đã biết khỏi hệ thống. Phép đo thứ hai dùng thay đổi thể tích ở các áp suất khác nhau giữa "
        "tâm thu và tâm trương, so sánh độ lệch đỉnh với độ lệch do rút lượng khí đã biết. Trong "
        "plethysmography đoạn, hai vòng băng được dùng: vòng thứ nhất tạo tắc tĩnh mạch, vòng thứ hai ép "
        "tới áp suất loại trừ dòng máu từ những phần không nên đưa vào phép đo."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Kỹ thuật cũng dùng cho <b>plethysmography toàn thân</b> [2] — phương pháp phổ biến đo thể tích "
        "tồn dư (residual volume), dung tích chức năng còn lại (FRC) và tổng dung tích phổi, các tham số "
        "thường xác định trong nghiệm pháp chức năng hô hấp [3]. Bệnh nhân ngồi trong một hộp kín, hít "
        "thở tới một thể tích nhất định (thường là FRC — thể tích còn lại sau khi thở ra bình thường), rồi "
        "một cửa chớp đóng ống thở lại trong khi bệnh nhân cố thở qua ống đã đóng. Ngực nở ra làm giảm thể "
        "tích khí trong hộp, tăng áp suất. Trước hết, thay đổi thể tích ngực được định lượng bằng định luật "
        "Boyle với áp suất và thể tích ban đầu của hộp cùng áp suất hộp sau khi nở. Thay đổi thể tích hộp "
        "bằng thay đổi thể tích ngực. Một phép đo thứ hai dùng thể tích ban đầu của ngực (chưa biết) và áp "
        "suất ban đầu tại miệng, cùng thể tích hít vào (thể tích ngực chưa biết cộng thay đổi thể tích thu "
        "được ở phép đo đầu) với áp suất miệng khi gắng hít. Giải định luật Boyle cho thể tích chưa biết "
        "thu được thể tích khí ban đầu trong phổi khi đóng cửa chớp — thường là thể tích cuối thì thở ra "
        "bình thường hay FRC."))
    b.append(p(
        "Các phương pháp thay thế để đo thay đổi thể tích bằng plethysmography đã được đưa ra nhằm khắc "
        "phục nhược điểm của plethysmography buồng như giá thành, độ phức tạp và tính vụng về khi dùng. "
        "Những lựa chọn quan trọng là plethysmography strain-gage (cảm biến điện trở đàn hồi), trở kháng, "
        "cảm ứng và quang điện."))

    b.append(h3("Plethysmography điện", "Electrical Plethysmography"))
    b.append(h3("Plethysmography strain-gage", "Strain-Gage Plethysmography"))
    b.append(p(
        "Năm 1953, Whitney mô tả thiết bị strain-gage cảm biến điện trở đàn hồi [4]. Thiết bị này định "
        "lượng sự thay đổi điện trở của gage khi nó bị giãn do vật (ví dụ đoạn chi) phình to. Gage thường "
        "là một ống đàn hồi nhỏ chứa thuỷ ngân hoặc chất điện ly/dẫn điện, hai đầu bịt bằng nút đồng hay "
        "điện cực tiếp xúc với cột dẫn, nối với mạch cầu Wheatstone."))
    b.append(p(
        "Để minh hoạ nguyên lý, đặt một gage dài l<sub>0</sub> vòng quanh đoạn chi có tiết diện tròn bán "
        "kính r<sub>0</sub>, nên l<sub>0</sub> = 2π r<sub>0</sub>. Khi chi phình, độ dài mới l<sub>1</sub> = "
        "2π r<sub>1</sub>, với r<sub>1</sub> là bán kính mới. Độ tăng độ dài gage là δl = 2π(r<sub>1</sub> − "
        "r<sub>0</sub>), còn thay đổi tiết diện δA = π(r<sub>1</sub><sup>2</sup> − "
        "r<sub>0</sub><sup>2</sup>):"))
    b.append(eq("δA = π (r<sub>1</sub><sup>2</sup> − r<sub>0</sub><sup>2</sup>)", "13.2"))
    b.append(p(
        "Vì (r<sub>1</sub> − r<sub>0</sub>) thường nhỏ, số hạng (r<sub>1</sub> − r<sub>0</sub>)<sup>2</sup> "
        "bỏ qua được, và δA viết được thành 2π r<sub>0</sub>(r<sub>1</sub> − r<sub>0</sub>). Chia cho "
        "A = π r<sub>0</sub><sup>2</sup> ta có:"))
    b.append(eq("δA / A = 2 (r<sub>1</sub> − r<sub>0</sub>) / r<sub>0</sub>", "13.3"))
    b.append(p("Mà δV/V = δA/A và δl/l<sub>0</sub> = δr/r<sub>0</sub>, nên:"))
    b.append(eq("δV / V = δA / A = 2 δl / l<sub>0</sub>", "13.4"))
    b.append(p(
        "Như vậy phần trăm tăng thể tích thu được bằng đo độ dài gage ban đầu và độ thay đổi độ dài. Trong "
        "thực hành, sự thay đổi độ dài gage được ghi trong thời gian ngắn để khắc phục áp suất ngược tích "
        "tụ trong chi do tắc tĩnh mạch, và kết quả thường biểu diễn bằng mililit trên phút trên 100 g mô, "
        "tức lưu lượng thể tích = 2 (δl / l<sub>0</sub>) · (100 / t), với δl là tăng độ dài gage trong thời "
        "gian t. Để đo δl/t, gage được hiệu chuẩn bằng cách tháo khỏi chi, kéo giãn trên một đế đo cho tới "
        "khi bút ghi về mức không — đó là độ dài l<sub>0</sub>; sau đó kéo giãn chính xác từng lượng để "
        "hiệu chuẩn đầu ra và tính lưu lượng thể tích."))

    b.append(h3("Plethysmography trở kháng", "Impedance Plethysmography"))
    b.append(p(
        "Nguyên lý vật lý của plethysmography trở kháng là sự biến thiên điện trở của một đoạn mô qua chu "
        "kỳ tim do độ dẫn thay đổi, gây bởi dòng chảy vào động mạch trong khi thoát tĩnh mạch bị tắc. Nếu "
        "đoạn chi coi như hình trụ dài l và thể tích V, trở kháng Z của phần đó viết được:"))
    b.append(eq("Z = ρ l<sup>2</sup> / V", "13.5"))
    b.append(p(
        "với ρ là điện trở suất riêng của mô tạo nên hình trụ. Máu vào đoạn mô trong chu kỳ tim đưa vào "
        "một trở kháng song song Z<sub>b</sub> = Z<sub>0</sub> Z<sub>1</sub> / (Z<sub>0</sub> − Z<sub>1</sub>), "
        "với Z<sub>0</sub> là trở kháng ban đầu, Z<sub>1</sub> là giá trị mới. Một thay đổi thể tích nhỏ "
        "δV liên hệ với thay đổi điện trở nhỏ δZ:"))
    b.append(eq("δV / V = − δZ / Z", "13.6"))
    b.append(p("khi giả sử các thay đổi thể tích rất nhỏ [5]. Do đó δV viết được:"))
    b.append(eq("δV = − V (δZ / Z<sub>0</sub>)", "13.7"))
    b.append(p(
        "Các tham số Z<sub>0</sub> và δZ lấy từ sơ đồ trở kháng. Nếu lấy ρ = 150 Ω·cm (điện trở suất riêng "
        "mô mềm), có thể xác định thay đổi thể tích. Hai kỹ thuật chính đo trở kháng mô: một dùng hai điện "
        "cực đo cả sụt áp và dòng — bất lợi là phân bố dòng quanh điện cực không biết, nên thể tích chính "
        "xác của mô bị thẩm vấn cũng không xác định. Năm 1974, Kubicek và cộng sự [6] dùng <b>bốn điện "
        "cực</b>: hai điện cực ngoài cấp tín hiệu xoay chiều biên độ nhỏ tần số cao, hai điện cực trong đo "
        "hiệu điện thế giữa hai điểm trên cùng bề mặt (xem Hình 13.2 và 13.3)."))
    b.append(fig(2, F.fig(2)))
    b.append(fig(3, F.fig(3)))

    b.append(h3("Plethysmography cảm ứng", "Inductive Plethysmography"))
    b.append(p(
        "Để đo thay đổi thể tích khi hô hấp, người ta phát triển hệ dựa trên plethysmography cảm ứng — "
        "thiết bị cảm ứng hô hấp (respiratory inductive plethysmograph) ra đời năm 1978. Hai cuộn dây "
        "được gắn: một quấn quanh lồng ngực, một quanh bụng. Khi hô hấp, đường kính mặt cắt các cuộn thay "
        "đổi, làm thay đổi cảm kháng. Chuyển các cảm kháng thành điện áp tỉ lệ, thu được đại lượng đo sự "
        "thay đổi thể tích khi hô hấp. Việc chuyển đổi nhờ các bộ dao động có tần số phụ thuộc tụ cố định "
        "và cảm kháng mỗi cuộn; tần số dao động đổi thành điện áp tỉ lệ rồi ghi lại. Sau hiệu chuẩn trên "
        "bệnh nhân, hệ dùng cho đo thể tích hô hấp [9]."))
    b.append(p(
        "Hai phương pháp hiệu chuẩn chung dựa trên phương trình:"))
    b.append(eq("V<sub>T</sub> = V<sub>RC</sub> + V<sub>AB</sub>", "13.8"))
    b.append(p(
        "với V<sub>RC</sub> và V<sub>AB</sub> là đóng góp của lồng ngực (RC) và ổ bụng (AB) vào thể tích "
        "thở (tidal volume) V<sub>T</sub>. Hiệu chuẩn thực hiện bằng xác định hằng số hiệu chuẩn trong một "
        "phép đo đẳng thể tích, hoặc bằng phương pháp hồi quy các sai biệt thay đổi cảm kháng do tư thế "
        "hay trạng thái ngủ khác nhau [10]. Khi đã hiệu chuẩn, thiết bị cảm ứng hô hấp theo dõi phi xâm "
        "lấn sự thay đổi thể tích lồng ngực và kiểu thở."))

    # ---- 13.2
    b.append(h2("13.2 Tích phân số với hình ảnh", "Numerical Integration with Imaging"))
    b.append(p(
        "Với các phương thức hình ảnh y khoa, đường kính vật có thể xác định phi xâm lấn. Áp dụng các "
        "đường kính này vào công thức tính thể tích thích hợp sẽ ước tính được kích thước vật. Ví dụ, thể "
        "tích tuyến tiền liệt V<sub>p</sub> xấp xỉ bằng công thức ellipsoid:"))
    b.append(eq("V<sub>p</sub> = (π / 6) H W L", "13.9"))
    b.append(p(
        "với H cao, W rộng, L dài (Hình 13.4). Nhiều biến thể công thức đã được đề xuất để ước tính thể "
        "tích tuyến tiền liệt [12, 13]; các công thức tính thể tích thất cũng dựa trên biến thể của công "
        "thức trên. Bằng cách hiển thị các ảnh mặt cắt ngang của vật 3-D (ví dụ một cơ quan), thể tích cũng "
        "tính được bằng tích phân diện tích cơ quan qua một chuỗi ảnh (Hình 13.5). Với siêu âm, đã có báo "
        "cáo về tuyến tiền liệt, tim, bàng quang và thận. Kỹ thuật tích phân dùng thuật toán phân đoạn trên "
        "chuỗi ảnh — theo hướng ngang với khoảng giao cắt cố định, hoặc theo hướng xuyên tâm với ảnh ở "
        "góc giao cắt cố định."))
    b.append(fig(4, F.fig(4)))
    b.append(p("Với vật xác định bởi hàm f(x, y, z), thể tích tính được từ:"))
    b.append(eq("V = &int;<sub>z₁</sub><sup>z₂</sup> &int;<sub>y₁</sub><sup>y₂</sup> "
                "&int;<sub>x₁</sub><sup>x₂</sup> f(x, y, z) dx dy dz", "13.10"))
    b.append(p(
        "Bằng tích phân số, phép tính tích phân xấp xỉ bằng tổ hợp tuyến tính các giá trị của hàm dưới "
        "tích. Trước hết minh hoạ trường hợp một chiều:"))
    b.append(eq("&int;<sub>a</sub><sup>b</sup> f(x) dx &asymp; w₁ f(x₁) + w₂ f(x₂) + … + w<sub>n</sub> f(x<sub>n</sub>)", "13.11"))
    b.append(p(
        "với x₁…x<sub>n</sub> là n điểm chọn trong đoạn [a, b] và w₁…w<sub>n</sub> là các trọng số tương "
        "ứng. Xấp xỉ này cũng viết thành tổng Riemann:"))
    b.append(eq("&int;<sub>a</sub><sup>b</sup> f(x) dx &asymp; &Sigma;<sub>i=1</sub><sup>n</sup> "
                "w<sub>i</sub> f(&xi;<sub>i</sub>)", "13.12"))
    b.append(p("Với tính thể tích, tổng Riemann mở rộng sang ba chiều:"))
    b.append(eq("V &asymp; &Sigma; (x<sub>i+1</sub> − x<sub>i</sub>)"
                "(y<sub>j+1</sub> − y<sub>j</sub>)(z<sub>k+1</sub> − z<sub>k</sub>) f(p<sub>ijk</sub>)", "13.13"))
    b.append(p(
        "Trường hợp ba chiều này thu gọn bằng cách coi (x<sub>i+1</sub> − x<sub>i</sub>)(y<sub>j+1</sub> − "
        "y<sub>j</sub>) f(p<sub>ijk</sub>) là diện tích S<sub>k</sub> của mặt cắt hai chiều tại vị trí "
        "z<sub>k</sub>, còn (z<sub>k+1</sub> − z<sub>k</sub>) không đổi với mọi k và bằng h — khoảng giao "
        "cắt:"))
    b.append(eq("V &asymp; h &Sigma;<sub>k=0</sub><sup>n−1</sup> S(a + k h)", "13.14"))
    b.append(p(
        "với a là vị trí mặt cắt đầu, n số mặt cắt, h bước (h = (b − a)/n, b là vị trí mặt cắt cuối). Có "
        "ba dạng xấp xỉ tuỳ vị trí mặt cắt. Dạng thứ nhất là <b>quy tắc hình chữ nhật</b> (13.14). "
        "<b>Quy tắc điểm giữa</b>:"))
    b.append(eq("V &asymp; h &Sigma;<sub>k=0</sub><sup>n−1</sup> S(a + (k + ½) h)", "13.15"))
    b.append(p(
        "<b>Quy tắc hình thang</b> tương tự quy tắc hình chữ nhật nhưng lấy trung bình tổng Riemann bên "
        "phải và bên trái:"))
    b.append(eq("V<sub>T</sub> = h [ ½ f(a) + f(a + h) + … + f(a + (n−1) h) + ½ f(b) ]", "13.16"))
    b.append(p(
        "Quy tắc hình thang và điểm giữa chính xác với hàm tuyến tính và hội tụ ít nhất nhanh như "
        "n<sup>−2</sup> nếu hàm dưới tích có đạo hàm bậc hai liên tục [14]."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Một số tham số liên quan đến độ chính xác của xấp xỉ tích phân thể tích bằng tổng Riemann: số "
        "mặt cắt n (tổng hội tụ với n<sup>−2</sup> — càng nhiều mặt cắt càng chính xác); và việc chọn vị "
        "trí mặt cắt đầu (trong phân tích lý thuyết khoảng tích thường xác định rõ, nhưng <i>in vivo</i> "
        "mặt cắt đầu thường kém xác định, nên cón thể bỏ sót mặt cắt). Hiệu ứng nữa là lấy mặt cắt xiên — "
        "không vuông góc với trục đo khoảng giao cắt. Giả sử mọi mặt cắt S<sub>k</sub> xác định chính xác."))
    b.append(p(
        "Ảnh hưởng của các tham số này kiểm tra được trong mô hình lý thuyết có thể tích/bề mặt biết "
        "trước. Hình 13.6 trình bày mô hình tuyến tiền liệt hai chiều — một hàm ellipsoid trục dài 50 mm, "
        "trục ngắn 40 mm, mô tả toán học:"))
    b.append(eq("y = f(x) = &plusmn; y<sub>0</sub> &radic;(1 − (x − x<sub>m</sub>)² / x<sub>0</sub>²)", "13.17"))
    b.append(p(
        "với x<sub>0</sub> nửa đường kính ellipse theo x (25 mm), y<sub>0</sub> nửa đường kính theo y (20 "
        "mm), (x<sub>m</sub>, y<sub>m</sub>) tâm ellipse. Nghiệm phân tích của tích để lấy diện tích mô "
        "hình này là π x<sub>0</sub> y<sub>0</sub>. Hình 13.7 cho kết quả khi đổi bước h từ 4 mm đến 16 mm "
        "(tương ứng 13 đến 3 mặt cắt) theo vị trí mặt cắt đầu (chọn ngẫu nhiên giữa toạ độ đầu hàm và toạ "
        "độ đó cộng bước h), các mặt cắt vuông góc trục dài. Nghiên cứu [15] kết luận: khi tỉ lệ bước h "
        "trên đường kính dài nhất không quá khoảng 6%, sai số ước tính thể tích dưới 5% — một chỉ dẫn tốt "
        "về khoảng giao cắt nên dùng cho xấp xỉ tích phân số, dù ứng dụng lâm sàng có thể thêm sai số do "
        "chuyển động."))
    b.append(fig(6, F.fig(6)))
    b.append(fig(7, F.fig(7)))

    # ---- 13.3
    b.append(h2("13.3 Phương pháp pha loãng chất chỉ thị", "Indicator Dilution Methods"))
    b.append(p(
        "Nguyên lý lý thuyết pha loãng chất chỉ thị để xác định thể tích khí hay chất lỏng do Stewart và "
        "Hamilton phát triển, dựa trên: nếu nồng độ một chất chỉ thị phân tán đều trong một thể tích chưa "
        "biết được xác định, và thể tích chất chỉ thị đã biết, thì thể tích chưa biết xác định được. Với "
        "mô hình một dòng vào và một dòng ra, mọi đầu vào rốt cuộc thoát qua kênh ra, và lưu lượng thể tích "
        "dùng nhận biết thể tích chảy. Mô tả bằng hai phương trình, phương trình thứ hai dùng kết quả thứ "
        "nhất để tìm thể tích [16]:"))
    b.append(eq("F = I<sub>i</sub> / (&int;<sub>0</sub><sup>∞</sup> C(t) dt)", "13.18"))
    b.append(eq("Volume = F · t<sub>m</sub>", "13.19"))
    b.append(p(
        "với F = lưu lượng, I<sub>i</sub> = lượng chất chỉ thị tiêm, C(t) = nồng độ theo thời gian, Vol = "
        "thể tích chảy, t<sub>m</sub> = thời gian trung bình đi qua. Giá trị tích phân nồng độ theo thời "
        "gian lấy từ đường cong nồng độ–thời gian (Hình 13.8) bằng planimetry và xấp xỉ tổng Riemann "
        "(13.13); cần loại bỏ ảnh hưởng tái tuần hoàn chất chỉ thị. Chất chỉ thị thích hợp nếu phát hiện và "
        "đo được, còn lại trong tuần hoàn ít nhất một vòng đầu mà không gây hại; loại bỏ sau đó là ưu điểm. "
        "Các phẩm nhuộm như Coomassie blue, indocyanine green từng dùng (hấp thụ đỉnh tại bước sóng nhất "
        "định); đồng vị phóng xạ như albumin huyết thanh người đánh dấu I cũng dùng; hiện nay dùng dung "
        "dịch muối lạnh đã trở nên thường quy đo cung lượng tim tại khoa hồi sức."))
    b.append(fig(8, F.fig(8)))
    b.append(h3("Nhiệt pha loãng (Thermodilution)", "Thermodilution"))
    b.append(p(
        "Để đo cung lượng tim, một bolus lạnh (độ chênh nhiệt độ ít nhất 10°C) được tiêm vào tâm nhĩ phải, "
        "sự thay đổi nhiệt độ máu trong động mạch phổi phát hiện bằng thermistor đáp ứng nhanh. Sau khi "
        "ghi đường cong nhiệt độ–thời gian, lưu lượng máu tính bằng phương trình Stewart–Hamilton đã sửa "
        "đổi [17]:"))
    b.append(eq("V<sub>i</sub> SW<sub>i</sub> SH<sub>i</sub> (T<sub>b</sub> − T<sub>i</sub>) = "
                "F &int; (T<sub>b</sub> − T(t)) dt", "13.20"))
    b.append(p("Dòng mô tả bởi:"))
    b.append(eq("F = K (T<sub>b</sub> − T<sub>i</sub>) / &int; (T<sub>b</sub> − T(t)) dt", "13.21"))
    b.append(p("với hằng số tính toán K:"))
    b.append(eq("K = V<sub>i</sub> SW<sub>i</sub> SH<sub>i</sub> C / (SW<sub>b</sub> SH<sub>b</sub>)", "13.22"))
    b.append(p(
        "Hằng số này người dùng nhập vào máy tính. T<sub>i</sub> thường đo ở đầu gần đường tiêm, nên cần "
        "hệ số hiệu chỉnh C để sửa hao hụt muối lạnh trong catheter do thể tích chết; mặt khác hiệu ứng "
        "hâm nóng dung dịch khi đi qua máu cũng phải sửa và phụ thuộc tốc độ tiêm, độ dài ngâm catheter và "
        "độ chênh nhiệt độ, khiến C < 1 [17]."))
    b.append(h3("Kỹ thuật hạt nhân phóng xạ", "Radionuclide Techniques"))
    b.append(p(
        "Chụp ảnh hạt nhân phóng xạ là kỹ thuật phi xâm lấn phổ biến đánh giá chức năng và bệnh tim, so "
        "sánh được với X-quang nhưng dùng bức xạ phát từ trong cơ thể để tạo ảnh. Nó hữu ích thu phân suất "
        "tống máu (ejection fraction) và thể tích thất trái. Như nhiệt pha loãng, tiêm một lượng nhỏ chất "
        "chỉ thị ngoại vi — ở đây là đồng vị phóng xạ (dược phẩm phóng xạ). Tuỳ radionuclide, phát ra "
        "alpha, beta, gamma, X; chỉ gamma/X phát hiện được bằng đầu dò ngoài cơ thể, năng lượng photon tối "
        "thiểu > 50 keV. Dùng máy đếm photon (Gamma camera) có collimator ghi phóng xạ. Hai kỹ thuật "
        "thường dùng: phương pháp qua một lần (first pass) và ghi động (dynamic) [11]."))
    b.append(p(
        "<b>First pass:</b> tiêm bolus radionuclide vào tĩnh mạch (cảnh ngoài hoặc cubital), camera đặt "
        "góc trước-trái lệch để tách thất phải/trái. Trừ bức xạ nền, xác định vùng quan tâm trên thất "
        "trái, tạo đường cong hoạt độ–thời gian. Đỉnh thứ hai thuộc hoạt động thất trái; hiệu chỉnh nền "
        "thu phân suất tống máu:"))
    b.append(eq("EF = (c<sub>d</sub> − c<sub>s</sub>) / (c<sub>d</sub> − c<sub>b</sub>)", "13.23"))
    b.append(p(
        "với c<sub>d</sub> đếm cuối tâm trương, c<sub>s</sub> cuối tâm thu, c<sub>b</sub> nền [18]. Phương "
        "pháp đếm cho kết quả chính xác đánh giá EF và thể tích thất trái. <b>Ghi động:</b> thu thập kích "
        "bởi tín hiệu khác (thường ECG) để căn chỉnh co thất trái qua nhiều chu kỳ; ước tính thể tích tâm "
        "thu/tâm trương và tính EF, cũng thu được biên độ/pha tống máu — áp dụng cả cho não, phổi, gan, "
        "thận, mạch máu."))
    b.append(h3("Pha loãng khí", "Gas Dilution"))
    b.append(p(
        "Pha loãng khí đo thể tích phổi vì kỹ thuật chuẩn (spirometry) chỉ đo khí hít/thở ra theo thời "
        "gian, không đánh giá được thể tích phổi tuyệt đối. Bệnh nhân nối với spirometer chứa nồng độ khí "
        "biết trước (ví dụ heli), thở vài phút để đều nồng độ heli trong phổi và spirometer. Theo bảo toàn "
        "vật chất, nồng độ phần trăm nhân thể tích trước bằng sau: C₁·V₁ = C₂·(V₁ + V₂); rút thể tích sau "
        "rồi trừ thể tích spirometer thu thể tích phổi."))

    # ---- 13.4
    b.append(h2("13.4 Đo thể tích thay thế nước", "Water Displacement Volumetry"))
    b.append(p(
        "Thể tích một chi như tay hay chân đo được bằng bể nước (Hình 13.9). Ưu điểm là đo trực tiếp vật "
        "có hình dạng không đều. Lâm sàng, đo thể tích chân hữu ích theo dõi mức độ phù hoặc tụ máu sau "
        "phẫu thuật/chấn thương. Kaulesar Sukul và cộng sự [19] mô tả một bể hai ống tràn: đổ đầy tới ống "
        "tràn dưới rồi đóng nó; bệnh nhân hạ chân xuống, đo lượng tràn ống trên; tổng thể tích bằng thể "
        "tích giao tới ống trên cộng hiệu thể tích giữa hai ống tràn ("))
    b.append(p(
        "Nhược điểm: vấn đề vệ sinh, tốn thời gian, không thích hợp đo chi bệnh nhân ngay sau phẫu thuật. "
        "Do đó người ta tìm phương pháp thay thế, trong đó <b>mô hình đĩa</b> rất hứa hẹn. Chia chân thành "
        "các đĩa dày h (ví dụ 3 cm) như Hình 13.10; tổng thể tích bằng tổng thể tích từng đĩa:"))
    b.append(eq("V = &Sigma;<sub>i=1</sub><sup>n</sup> π r<sub>i</sub><sup>2</sup> h "
                "= &Sigma;<sub>i=1</sub><sup>n</sup> C<sub>i</sub><sup>2</sup> h / (4π)", "13.24"))
    b.append(p(
        "với C<sub>i</sub> chu vi đĩa tại vị trí i, bán kính giả định r<sub>i</sub>. Nghiên cứu so sánh "
        "phương pháp thay thế nước và mô hình đĩa cho kết quả tương tự; nhờ dễ áp dụng, mô hình đĩa là lựa "
        "chọn để đo thể tích chi. Với chân dài 75 cm và bước 3 cm, tỉ lệ dài/bước là 25; theo [15] tỉ lệ "
        "này có thể giảm vẫn giữ độ chính xác > 95% — đĩa cao 10 cm đủ đo thể tích chân chính xác ít nhất "
        "95%, dù có thể cần khoảng cách đĩa nhỏ hơn để theo dõi chính xác thay đổi phù."))
    b.append(fig(9, F.fig(9)))
    b.append(fig(10, F.fig(10)))

    # ---- 13.5
    b.append(h2("13.5 Thiết bị và thí nghiệm", "Equipment and Experiments"))
    b.append(p(
        "Bảng 13.1 tóm tắt các phương pháp đo thể tích và ứng dụng, làm điểm xuất phát đánh giá thiết bị "
        "hiện có."))
    b.append(table(
        ["Kỹ thuật", "Ứng dụng", "Hãng", "Sản phẩm", "Giá (US$)"],
        [["Spirometry", "Thể tích phổi", "Nellcor Puritan Bennett (Renaissance), Morgan Science, "
          "Spirometrics, CDX Corporation", "Spiro 110S", "—"],
         ["Plethysmography toàn thân", "Thể tích phổi", "Morgan Science, ACI Medical Inc.", "—", "25.000"],
         ["Pha loãng khí", "Thể tích phổi", "Equilibrated Biosystems Inc. (Melville)", "—", "—"],
         ["Nhiệt pha loãng", "Tim", "Abbott Critical Care System, Baxter, American Edwards Laboratories",
          "—", "—"],
         ["Plethysmography strain-gage", "Cung lượng tim", "Parks Medical Electronics", "—", "—"],
         ["Plethysmography trở kháng", "Nghiên cứu tưới máu, theo dõi ngoại trú",
          "Vitalog, RJL Systems (Detroit), Codman and Shurtleff Inc., Randolph, Electrodiagnostic "
          "Instrument Inc. (Burbank)", "—", "—"],
         ["Plethysmography cảm ứng", "Thể tích phổi", "SensorMedics BV", "RespiTrace plus, SomnoStar PT",
          "15.000"],
         ["Ảnh hạt nhân phóng xạ", "Tim, cơ quan ngoại vi", "Schering", "—", "—"]],
        "Bảng 13.1 · Các kỹ thuật đo thể tích, ứng dụng và thiết bị tương ứng."))

    # ---- 13.6
    b.append(h2("13.6 Đánh giá", "Evaluation"))
    b.append(p(
        "Plethysmography là phương pháp dễ dàng, phi xâm lấn để đánh giá bệnh mạch, rối loạn cung lượng "
        "tim hay rối loạn phổi. Các hệ đo trực tiếp sự thay đổi thể tích đã phát triển, nhưng các tính "
        "chất vật lý cũng được đưa vào làm thước đo gián tiếp sự thay đổi thể tích; mỗi hệ có ưu nhược "
        "riêng."))
    b.append(p(
        "Với plethysmography buồng, kiểu chứa nước ổn định hơn với thay đổi nhiệt độ nhưng có thể gặp vấn "
        "đề nhiệt nếu nhiệt độ nước khác biệt đáng kể với đoạn chi; hiệu ứng thuỷ tĩnh của nước có thể "
        "thay đổi dòng máu; vỏ cao su giữa chi và nước ảnh hưởng tiết mồ hôi — phép đo vướng víu, ít dùng "
        "khi tập hay sau vận động. Kiểu thay thế khí có vấn đề trôi do hệ số nở lớn, dù có hệ tự bù; nhiệt "
        "độ cơ thể plethysmograph có thể gây biến thiên áp suất trong hộp kín [20]."))
    b.append(p(
        "Trong plethysmography trở kháng, dùng sự thay đổi trở kháng mô do chủ yếu thay đổi độ dẫn của "
        "đường dòng mỗi nhịp máu. Có ba lý thuyết giải thích: máu vào đoạn cơ thể làm hạ trở kháng đoạn "
        "đó; đường kính tăng làm tăng tiết diện đường dẫn nên hạ điện trở; và áp suất lên điện cực mỗi "
        "nhịp thay đổi trở kháng giao tiếp da–điện cực. Khó khăn chính là liên hệ trở kháng đầu ra với "
        "thể tích tuyệt đối — nhưng phát hiện mạch động mạch, đo tần số mạch, xác định thời gian tới của "
        "mạch tại một điểm tuần hoàn ngoại vi đều xử lý tốt; nó cũng đo được thay đổi thể tích máu theo "
        "thời gian. Nhạy cảm với chuyển động là vấn đề, đang nghiên cứu giảm bằng cấu hình/cách đặt điện "
        "cực khác, nhiều cảm biến hay tần số khác [21]."))
    b.append(p(
        "Cohen và cộng sự thiết kế một plethysmograph cảm ứng giá thấp để đo thông khí phổi phi xâm lấn "
        "[22], gián tiếp theo dõi thông khí bằng đo tiết diện ngang ngực và bụng qua các dải đàn hồi chứa "
        "dây, xác định cảm kháng từ tần số bộ dao động điều khiển bởi cuộn cảm."))
    b.append(p(
        "Thiết bị mới dùng các tính chất khác để thu tri thức định lượng — ví dụ <b>plethysmography âm "
        "học</b> đo thể tích cơ thể qua tần số cộng hưởng của bộ cộng hưởng Helmholtz (tần số tỉ lệ nghịch "
        "với căn bậc hai thể tích khí; vật đặt vào làm tăng tần số). Nghiên cứu đo mật độ trẻ sinh non kết "
        "luận thiết bị này đo được tổng thể tích cơ thể trẻ sinh non [23]."))
    b.append(p(
        "Thêm nữa, đo thể tích bằng phương thức hình ảnh chẩn đoán đã vững chắc trong lâm sàng (siêu âm "
        "tuyến tiền liệt, siêu âm tim). Bên cạnh bước giao cắt và chọn bước đầu, xác định chính xác bề "
        "mặt trong từng mặt cắt rất quan trọng. Dù chủ yếu làm thủ công, đã có nỗ lực tự động phát hiện "
        "bề mặt [24–27] — mở ra hệ đo tự động tuyến tiền liệt, tim, gan, v.v."))
    b.append(h3("Các thuật ngữ định nghĩa", "Defining Terms"))
    b.append('<dl class="glossary">'
             '<dt>Plethysmography</dt><dd>Kỹ thuật đo sự thay đổi thể tích của cơ quan hay mô bằng cách '
             'bao quanh nó trong một buồng cứng chứa nước hoặc khí, theo dõi sự thay thế chất lỏng hoặc '
             'thay đổi áp suất khí.</dd>'
             '<dt>Plethysmography buồng (Chamber plethysmography)</dt><dd>Loại đo thể tích trực tiếp '
             'bằng thay thế, dùng buồng cứng thường chứa nước đặt chi vào; đo được cả xung động theo '
             'nhịp tim và tổng lượng máu vào khi tắc tĩnh mạch.</dd>'
             '<dt>Tắc tĩnh mạch (Venous occlusion)</dt><dd>Kỹ thuật bơm một vòng băng ép phía trên chi '
             'tới áp suất trên áp suất tĩnh mạch 40–60 mm Hg, cho máu động mạch vào nhưng ngăn máu tĩnh '
             'mạch ra, nhờ đó đo lưu lượng vào.</dd>'
             '<dt>Strain-gage plethysmography</dt><dd>Thiết bị cảm biến điện trở đàn hồi; độ giãn ống '
             'dẫn (thuỷ ngân/điện ly) vòng quanh chi tỉ lệ với thay đổi thể tích, theo định luật '
             'Whitney (13.2)–(13.4).</dd>'
             '<dt>Impedance plethysmography</dt><dd>Đo sự thay đổi điện trở của đoạn mô qua chu kỳ tim '
             'do dòng chảy vào động mạch; dùng bốn điện cực (Kubicek 1974) để tách dòng và áp (Hình '
             '13.2, 13.3).</dd>'
             '<dt>Inductive plethysmography</dt><dd>Đo thay đổi thể tích hô hấp bằng hai cuộn dây quấn '
             'quanh ngực và bụng; sự thay đổi cảm kháng đổi thành điện áp tỉ lệ (13.8).</dd>'
             '<dt>Step-section planimetry</dt><dd>Phương pháp tích phân số lâm sàng: ghi các mặt cắt ngang '
             'với khoảng cố định, xác định diện tích từng mặt cắt rồi nhân khoảng giao cắt và cộng lại '
             '(13.14).</dd>'
             '<dt>Pha loãng chất chỉ thị (Indicator dilution)</dt><dd>Nguyên lý Stewart–Hamilton: biết '
             'lượng chất chỉ thị và nồng độ phân tán đều, suy ra thể tích chưa biết qua lưu lượng và thời '
             'gian trung bình (13.18)–(13.19).</dd>'
             '<dt>Mô hình đĩa (Disk model)</dt><dd>Chia chi thành các lát dày h, coi mỗi lát là đĩa tròn '
             'bán kính từ chu vi, tổng thể tích V = Σ π r² h (13.24).</dd>'
             '</dl>')
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>A. J. Comerota, R. N. Harada, A. R. Eze, and M. L. Katz, Air plethysmography: a clinical '
             'review, <i>Int. Angiology</i>, 14, 45–52, 1995.</li>'
             '<li>A. B. Dubois et al., A rapid plethysmographic method for measuring thoracic gas volume, '
             '<i>J. Clin. Invest.</i>, 35, 322–326, 1956.</li>'
             '<li>J. B. West, <i>Respiratory Physiology — The Essentials</i>, Baltimore: Williams and '
             'Wilkins, 1987.</li>'
             '<li>J. R. Whitney, The measurement of volume changes in human limbs, <i>J. Physiol.</i>, '
             '121, 1–27, 1953.</li>'
             '<li>J. Nyboer, S. Bagno, and L. F. Nims, The Impedance Plethysmograph: An Electrical Volume '
             'Recorder, National Research Council, Rep. No. 149, 1943.</li>'
             '<li>W. G. Kubicek et al., The Minnesota impedance cardiograph — Theory and applications, '
             '<i>Biomed. Eng.</i>, 9, 410–416, 1974.</li>'
             '<li>R. Shankar and J. G. Webster, Noninvasive measurement of compliance of human leg '
             'arteries, <i>IEEE Trans. Biomed. Eng.</i>, 38, 62–67, 1993.</li>'
             '<li>N. Verschoor et al., The lowering of stroke volume measured by impedance cardiography, '
             '<i>Physiol. Meas.</i>, 17, 29–35, 1996.</li>'
             '<li>M. A. Cohn et al., A transducer for non-invasive monitoring of respiration, in '
             '<i>ISAM 1977</i>, London: Academic Press, 1978, 119–128.</li>'
             '<li>J. A. Adams, Respiratory inductive plethysmography, in <i>Infant Respiratory Function '
             'Testing</i>, New York: Wiley-Liss, 1996, 139–164.</li>'
             '<li>S. Webb, <i>The Physics of Medical Imaging</i>, Bristol: IOP Publishing, 1988.</li>'
             '<li>M. K. Terris and T. A. Stamey, Determination of prostate volume by transrectal '
             'ultrasound, <i>J. Urol.</i>, 145, 984–987, 1991.</li>'
             '<li>R. G. Aarnink et al., Formula-derived prostate volume determination, <i>Eur. Urol.</i>, '
             '29, 399–402, 1996.</li>'
             '<li>P. J. Davis and P. Rabinowitz, <i>Methods of Numerical Integration</i>, San Diego: '
             'Academic Press, 1975.</li>'
             '<li>R. G. Aarnink et al., Planimetric volumetry of the prostate: how accurate is it?, '
             '<i>Physiol. Meas.</i>, 16, 141–150, 1995.</li>'
             '<li>E. D. Trautman and R. S. Newbower, The development of indicator-dilution techniques, '
             '<i>IEEE Trans. Biomed. Eng.</i>, 31, 800–807, 1984.</li>'
             '<li>A. Rubini et al., Cardiac output measurement by the thermodilution method, <i>Intensive '
             'Care Med.</i>, 21, 154–158, 1995.</li>'
             '<li>S. Jang et al., Cardiac ejection fraction and volume measurements using dynamic cardiac '
             'phantoms and radionuclide imaging, <i>IEEE Trans. Nucl. Sci.</i>, 41, 2845–2849, 1994.</li>'
             '<li>D. M. K. S. Kaulesar Sukul et al., Direct and indirect methods for the quantification '
             'of leg volume, <i>J. Biomed. Eng.</i>, 15, 477–480, 1993.</li>'
             '<li>P. Saucez et al., Thermal behavior of the constant volume body plethysmograph, '
             '<i>IEEE Trans. Biomed. Eng.</i>, 42, 269–277, 1995.</li>'
             '<li>J. Rosell et al., Reduction of motion artifacts using a two-frequency impedance '
             'plethysmograph and adaptive filtering, <i>IEEE Trans. Biomed. Eng.</i>, 42, 1044–1048, '
             '1995.</li>'
             '<li>K. P. Cohen et al., Design of an inductive plethysmograph for ventilation measurement, '
             '<i>Physiol. Meas.</i>, 15, 217–229, 1994.</li>'
             '<li>O. S. Valerio Jimenez et al., Pre-term infant volume measurements by acoustic '
             'plethysmography, <i>J. Biomed. Eng.</i>, 15, 91–98, 1993.</li>'
             '<li>R. G. Aarnink et al., A practical clinical method for contour determination in '
             'ultrasonographic prostate images, <i>Ultrasound Med. Biol.</i>, 20, 705–717, 1994.</li>'
             '<li>C. H. Chu et al., Detecting left ventricular endocardial and epicardial boundaries by '
             'digital two-dimensional echocardiography, <i>IEEE Trans. Med. Im.</i>, 7, 81–90, 1988.</li>'
             '<li>J. Feng et al., Epicardial boundary detection using fuzzy reasoning, <i>IEEE Trans. '
             'Med. Im.</i>, 10, 187–199, 1991.</li>'
             '<li>S. Lobregt and M. A. Viergever, A discrete contour model, <i>IEEE Trans. Med. Im.</i>, '
             '14, 12–24, 1995.</li>'
             '</ol>')
    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(p(
        "Anonymous, AARC Clinical Practice Guideline; Static lung volume, <i>Respir. Care</i>, 39, "
        "830–836, 1994."))
    b.append(p(
        "Anonymous, AARC Clinical Practice Guideline; Body plethysmography, <i>Respir. Care</i>, 39, "
        "1184–1190, 1994."))
    b.append(p(
        "E. F. Bernstein (ed.), <i>Noninvasive Diagnostic Techniques in Vascular Disease</i>, 3rd ed., "
        "St. Louis: Mosby, 1985."))
    b.append(p(
        "P. J. Davis and P. Rabinowitz, <i>Methods of Numerical Integration</i>, London: Academic "
        "Press, 1975."))
    b.append(p(
        "H. Feigenbaum, <i>Echocardiography</i>, 5th ed., Philadelphia: Lee &amp; Febiger, 1993."))
    b.append(p(
        "W. N. McDicken, <i>Diagnostic Ultrasonics: Principles and Use of Instruments</i>, 3rd ed., "
        "London: Crosby Lockwood Staples, 1991."))
    b.append(p(
        "J. Nyboer, <i>Electrical Impedance Plethysmography</i>, Springfield, IL: Charles Thomas, 1959."))
    b.append(p(
        "S. Webb, <i>The Physics of Medical Imaging</i>, Bristol: IOP Publishing, 1988."))
    b.append(p(
        "J. B. West, <i>Respiratory Physiology — The Essentials</i>, Baltimore: Williams and Wilkins, "
        "1987."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 12</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 13. All ten figures are "
        "redrawn as vectors — the air-plethysmograph occlusion trace, the two impedance electrode "
        "layouts, the prostate ellipsoid, the step-section planimetry, the ellipsoid theoretical model, "
        "the step-size error plot, the indicator time-concentration curve, the water-overflow schematic, "
        "and the leg disk model — plus Table 13.1 of techniques and equipment. The prose of the "
        "translation is not repeated here."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "The chapter opens with the simple cases — analytic formulae for regular solids, fluid "
        "displacement for irregular objects, and filling a cavity with fluid to measure its volume — then "
        "turns to medical volume: plethysmography, imaging-based integration, indicator dilution, and "
        "water displacement. Plethysmography surrounds the organ with a rigid chamber of water or air; "
        "the displaced fluid or changed air pressure marks the volume change from arterial in-flow. In "
        "venous occlusion (cuff at 40–60 mm Hg) arterial blood enters but venous blood cannot leave, so "
        "the limb grows each beat by the volume that entered (Figure 13.1)."))
    b.append(p(
        "Air plethysmography rests on Boyle's law, P<sub>i</sub> V<sub>i</sub> = P<sub>f</sub> V<sub>f</sub> "
        "(13.1): the cuff pressure change over the cardiac cycle is compared against removing known "
        "amounts of air. Whole-body plethysmography (the patient in an airtight box) uses the same law "
        "twice — first the box volume change equals the chest volume change, then the unknown FRC is "
        "solved from the mouth-pressure measurements."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Electrical plethysmography avoids the chamber. The strain-gage (Whitney, 1953) wraps an elastic "
        "mercury or electrolyte tube around the limb; its stretch δl gives the volume change because "
        "δV/V = 2 δl/l<sub>0</sub> (13.2)–(13.4), and flow rate is 2(δl/l<sub>0</sub>)·(100/t) ml·min⁻¹·"
        "(100 g)⁻¹. Impedance plethysmography uses Z = ρ l²/V (13.5); a small volume change δV relates to "
        "δZ by δV/V = −δZ/Z (13.6)–(13.7). The four-electrode scheme of Kubicek (1974) drives current "
        "through the outer pair and measures voltage across the inner pair (Figures 13.2, 13.3), which "
        "removes the unknown current distribution near the electrodes. Inductive plethysmography (1978) "
        "wraps coils on rib cage and abdomen; the changing cross-section changes inductance, converted to "
        "proportional voltage, so tidal volume V<sub>T</sub> = V<sub>RC</sub> + V<sub>AB</sub> (13.8)."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Section 13.2 is the numerical heart of the chapter. For an ellipsoid prostate, V<sub>p</sub> = "
        "(π/6) H W L (13.9); more generally V = ∭ f(x,y,z) dx dy dz (13.10). The integral is approximated "
        "by a linear combination of integrand values — the quadrature (13.11) and its Riemann-sum form "
        "(13.12). In three dimensions this becomes the sum over cells (13.13), and if each section's area "
        "S<sub>k</sub> is taken at a fixed intersection distance h, it collapses to the rectangular rule "
        "V ≈ h Σ S(a + k h) (13.14), with h = (b−a)/n. The midpoint (13.15) and trapezoidal (13.16) rules "
        "are exact for linear functions and converge at least as n<sup>−2</sup>. Figure 13.5 is the "
        "step-section planimetry in practice, and Figures 13.6–13.7 show the spheroid model used to test "
        "how step size and first-section position drive the error: when the step is no more than about 6% "
        "of the longest diameter, volume error stays under 5% [15]."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(fig(6, F.fig(6), "en"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "Section 13.3 is the Stewart–Hamilton indicator-dilution principle: if a known mass I<sub>i</sub> "
        "of indicator is dispersed uniformly in an unknown volume, the flow is F = I<sub>i</sub> / "
        "∫C(t)dt (13.18) and the volume is F·t<sub>m</sub> (13.19). The area under the time-concentration "
        "curve (Figure 13.20) is found by planimetry and the Riemann sum; recirculation must be removed. "
        "Thermodilution injects a cold bolus and recovers flow from a modified Stewart–Hamilton equation "
        "(13.20)–(13.22), with the user-supplied constant K accounting for specific weights, specific "
        "heats, and a catheter correction factor C < 1. Radionuclide imaging (first-pass and dynamic, "
        "ECG-gated) yields ejection fraction EF = (c<sub>d</sub>−c<sub>s</sub>)/(c<sub>d</sub>−c<sub>b</sub>) "
        "(13.23). Gas dilution (helium, conservation of mass) recovers absolute lung volume that "
        "spirometry cannot."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Section 13.4, water-displacement volumetry, directly measures irregular limbs with an overflow "
        "tank (Figure 13.9) but is slow, hygiene-prone, and unsuitable immediately post-operative. The "
        "disk model (Figure 13.10) divides the leg into disks of thickness h and sums V = Σ π r² h = "
        "Σ C² h/(4π) (13.24), where C is each disk's circumference; it matches water displacement in "
        "accuracy and, at a 10 cm disk height, already exceeds 95% [15, 19], so it is the method of choice "
        "for extremities."))
    b.append(p(
        "Table 13.1 (below) summarises the techniques, their clinical applications, representative "
        "companies and products, and list prices where the chapter gives them — whole-body plethysmography "
        "at about $25,000 and the inductive RespiTrace plus / SomnoStar PT at about $15,000 stand out."))
    b.append(table(
        ["Technique", "Application", "Companies", "Products", "Price (U.S.$)"],
        [["Spirometry", "Lung volume", "Nellcor Puritan Bennett (Renaissance), Morgan Science, "
          "Spirometrics, CDX Corporation", "Spiro 110S", "—"],
         ["Whole-body plethysmography", "Lung volume", "Morgan Science, ACI Medical Inc.", "—", "25,000"],
         ["Gas dilution", "Lung volume", "Equilibrated Biosystems Inc. (Melville)", "—", "—"],
         ["Thermodilution", "Heart", "Abbott Critical Care System, Baxter, American Edwards Laboratories",
          "—", "—"],
         ["Strain-gage plethysmography", "Cardiac output", "Parks Medical Electronics", "—", "—"],
         ["Impedance plethysmography", "Perfusion / ambulatory monitoring",
          "Vitalog, RJL Systems (Detroit), Codman and Shurtleff Inc., Randolph, Electrodiagnostic "
          "Instrument Inc. (Burbank)", "—", "—"],
         ["Inductive plethysmograph", "Lung volume", "SensorMedics BV", "RespiTrace plus, SomnoStar PT",
          "15,000"],
         ["Radionuclide imaging", "Heart, peripheral organs", "Schering", "—", "—"]],
        "Table 13.1 · Volume measuring techniques, applications, and equipment."))
    b.append(p(
        "Section 13.6 weighs the methods. Chamber plethysmography (water-filled) is temperature-stable "
        "but brings hydrostatic and sweating artifacts and is cumbersome around exercise; the air type "
        "drifts with its high expansion coefficient. Impedance plethysmography reliably detects pulsations "
        "and pulse-transit times but cannot be tied to an absolute volume, and is motion-sensitive — an "
        "active research area. A low-cost inductive design monitors ventilation via chest/abdomen bands, "
        "and acoustic plethysmography measures total body volume of preterm infants through a Helmholtz "
        "resonator whose frequency rises as the infant displaces air. Imaging-based planimetry is now "
        "routine for prostate and heart, and automated contour detection (references [24]–[27]) points "
        "toward fully automated organ volumetry."))
    b.append(p(
        "The defining-terms list is worth keeping: plethysmography measures volume change inside a rigid "
        "air/water chamber; venous occlusion isolates arterial in-flow; the strain-gage, impedance and "
        "inductive variants are the electrical alternatives; step-section planimetry and the disk model "
        "are the numerical/geometric stand-ins for water displacement; and indicator dilution recovers an "
        "unknown volume from a known mass and a measured concentration curve."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 12</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 13 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 13 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 13 “Đo thể tích” của Rene G. Aarnink và Hessel Wijkstra — "
            "plethysmography (khí/nước, buồng, strain-gage, trở kháng, cảm ứng), tích phân số với ảnh, "
            "pha loãng chất chỉ thị, đo thể tích thay thế nước, kèm 10 hình và Bảng 13.1." if vi else
            "Companion to Chapter 13 of the CRC Measurement Handbook — volume measurement by "
            "plethysmography (air/water, chamber, strain-gage, impedance, inductive), numerical "
            "integration with imaging, indicator dilution, and water displacement, with all ten figures.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 13' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 13' % BASE_EN)
    meta = ("Chương 13 · theo Ch13.pdf (CRC Press, 1999) · 10 hình, 1 bảng, 27 phương trình" if vi
            else "Chapter 13 · 10 figures, 1 table, 27 equations")
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
