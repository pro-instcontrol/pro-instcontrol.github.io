# -*- coding: utf-8 -*-
"""Handbook Chapter 99 — Electropneumatic and Electrohydraulic Instruments:
Modeling of Electrohydraulic and Electrohydrostatic Actuators
(M. Pachter and C. H. Houpis — Air Force Institute of Technology).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch99.py
"""
import os

import hb99fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch99-electropneumatic-and-electrohydraulic-instruments"
TITLE_EN = "Electropneumatic and Electrohydraulic Instruments"
TITLE_VI = "Thiết bị điện – khí nén và điện – thuỷ lực"
BYLINE = "M. Pachter · C. H. Houpis · Air Force Institute of Technology"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

PBAR = "P&#772;"          # the differential-pressure symbol of the source


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-99-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t, en=""):
    return '<h4>%s%s</h4>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def table(hd, rows, cap, cls=""):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ nomenclature

NOM = [
    ("A", "diện tích tiết diện của xi lanh", "ram cross-section area"),
    ("a, b, c, d, e, R<sub>h</sub>", "chiều dài các khâu liên kết", "length of linkages"),
    ("x, X", "chuyển vị", "displacement"),
    ("J", "mômen quán tính", "moment of inertia"),
    ("K", "hệ số khuếch đại", "gain"),
    ("U, u", "tốc độ bay", "airspeed"),
    ("q", "tốc độ chúc ngóc", "pitch rate"),
    ("M, z, m", "các đạo hàm ổn định khí động", "aerodynamic stability derivatives"),
    ("P", "áp suất", "pressure"),
    ("δ", "góc lệch", "deflection angle"),
    ("τ", "mômen", "torque"),
    ("Ω, ω", "tốc độ quay rôto", "rotor speed"),
    (PBAR, "chênh áp do bơm và chất lỏng tạo ra", "differential pressure developed by the pump"),
    ("α", "góc tấn của máy bay", "angle of attack of aircraft"),
    ("ρ", "khối lượng riêng không khí", "air density"),
]


def _nom(lang):
    if lang == "vi":
        return table(("Ký hiệu", "Đại lượng"),
                     [[s, d] for s, d, _e in NOM],
                     "Bảng 99.1 · Các ký hiệu dùng trong chương, xếp theo thứ tự chữ cái La-tinh rồi "
                     "đến chữ Hy Lạp.", " nom")
    return table(("Symbol", "Quantity"),
                 [[s, e] for s, _d, e in NOM],
                 "Table 99.1 · Symbols used in this chapter, Latin letters first, then Greek.",
                 " nom")


# ================================================================ Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Trong một hệ điều khiển, đầu ra của bộ điều khiển — còn gọi là bộ san bằng hay bộ bù — vốn "
        "tác động lên các tín hiệu lệnh và tín hiệu phản hồi, bao giờ cũng được đưa tới một cơ cấu chấp "
        "hành. Cơ cấu này là phần tử công suất nằm ở một vị trí then chốt tại đầu vào của đối tượng "
        "điều khiển, và ở mức độ đáng kể, nó quyết định chất lượng của toàn bộ hệ điều khiển. Vì thế, "
        "không thể nói quá tầm quan trọng của việc mô hình hoá chính xác phần tử chấp hành, nếu muốn "
        "đạt được và duy trì chất lượng điều khiển mong muốn trên toàn dải làm việc."))
    b.append(p(
        "Những yếu tố như đặc tính trễ pha của cơ cấu chấp hành, sự thay đổi tham số theo thời gian "
        "sử dụng, nhiễu cảm biến và kịch bản vận hành — trong bối cảnh điều khiển bay người ta gọi là "
        "<i>điều kiện bay</i> — cần được xét một cách tường minh ngay trong quá trình thiết kế. Để có "
        "một hệ điều khiển bền vững, tức là hệ đã tính đến tất cả những yếu tố ấy, cần hiểu rõ và có "
        "một mô hình chính xác của phần tử chấp hành. Chương này trình bày quá trình mô hình hoá cơ "
        "cấu chấp hành ấy."))

    # ---------------------------------------------------------------- 99.1
    b.append(h2("99.1 Giới thiệu", "99.1 Introduction"))
    b.append(p(
        "Các yêu cầu về tỉ lệ công suất trên khối lượng đã đẩy thiết kế cơ cấu chấp hành đi qua bốn "
        "thế hệ: khí nén, thuỷ lực, điện – thuỷ lực, và gần đây nhất, trong ứng dụng điều khiển bay, "
        "là cấu hình <i>điện – thuỷ tĩnh</i>. Quan điểm được dùng xuyên suốt chương này là: bản thân "
        "cơ cấu chấp hành đã là một hệ điều khiển phản hồi theo đúng nghĩa của nó. Theo cách nhìn đó, "
        "cơ cấu chấp hành gồm bốn phần: một phần tử “khuếch đại” (van servo), một phần tử công suất "
        "(xi lanh lực), một cảm biến chuyển vị của cơ cấu, và một bộ điều khiển — sẽ bàn kỹ hơn ở phần "
        "sau."))
    b.append(p(
        "Hơn nữa, cần đặt hệ con chấp hành vào đúng bối cảnh của toàn hệ điều khiển, ví dụ một hệ điều "
        "khiển bay. Trước hết chương xét một cơ cấu chấp hành thuỷ lực tương đối đơn giản. Sau đó "
        "trọng tâm chuyển sang công nghệ cơ cấu chấp hành điện – thuỷ tĩnh (EHA) hiện đại: trong ứng "
        "dụng điều khiển bay, công nghệ này cho khả năng sống sót chiến đấu cao và dễ bảo trì hơn, vì "
        "mọi phần tử đều được bố trí cụm lại ngay tại cơ cấu chấp hành. Do EHA không cần những tuyến "
        "ống thuỷ lực dài, thời gian và trang thiết bị bảo trì cần thiết đều giảm, đồng thời diện tích "
        "phơi ra trước hoả lực đối phương cũng thu hẹp đáng kể. Ngoài ra, khi thiết kế toàn hệ điều "
        "khiển còn phải tính đến hỏng hóc của cơ cấu chấp hành do nhiều nguyên nhân khác nhau và do "
        "lão hoá. Một hệ điều khiển bền vững có dùng cơ cấu chấp hành chỉ có thể được thiết kế khi có "
        "mô hình chính xác của cơ cấu ấy, đủ để thoả mãn các chỉ tiêu chất lượng của hệ. EHA và ứng "
        "dụng điều khiển bay của nó được dùng làm “phương tiện” để trình bày quá trình mô hình hoá."))

    b.append(h3("Yêu cầu mô hình hoá cơ cấu chấp hành",
                "Actuator modeling requirements"))
    b.append(p(
        "Khi phải thay một cơ cấu chấp hành trong hệ điều khiển bằng một cơ cấu “mua sẵn” vì những lý "
        "do vừa nêu, tính bền vững của toàn hệ điều khiển không được phép thay đổi do việc thay thế "
        "ấy. Vì vậy quá trình thiết kế cơ cấu chấp hành gồm ba bước:"))
    b.append('<ol style="margin:-.3rem 0 1.2rem 1.3rem;line-height:1.85;font-size:.95rem">'
             '<li>Xây dựng một mô hình toán học chính xác cho cơ cấu chấp hành.</li>'
             '<li>Phân tích độ nhạy của hệ điều khiển cơ cấu chấp hành. Bước này phải bao gồm độ nhạy '
             'với sự thay đổi của tải, hiệu suất các khâu, các tham số vật lý của đối tượng và nhiễu '
             'của cảm biến trên cơ cấu.</li>'
             '<li>Xác định một tập thay đổi hợp lý của đối tượng, dựa trên kết quả phân tích độ nhạy; '
             'tập này là đầu vào bắt buộc để thiết kế một hệ điều khiển cơ cấu chấp hành bền vững, '
             'thoả mãn các chỉ tiêu đề ra khi có những thay đổi đã dự báo.</li>'
             '</ol>')

    # ---------------------------------------------------------------- 99.2
    b.append(h2("99.2 Mô hình hoá cơ cấu chấp hành thuỷ lực",
                "99.2 Hydraulic actuator modeling"))
    b.append(p(
        "Trước hết xét việc mô hình hoá một cơ cấu chấp hành thuần thuỷ lực dùng trong hệ điều khiển "
        "bay không hồi tiếp. Với cách ký hiệu trên Hình 99.1, ta có các hệ thức:"))
    b.append(eq("x<sub>1</sub> = δ<sub>ec</sub>·a", "99.1a"))
    b.append(eq("(x<sub>v</sub> − x<sub>f</sub>)/(b + c) = (x<sub>v</sub> − x<sub>1</sub>)/c", "99.1b"))
    b.append(fig(1, F.fig(1)))
    b.append(p("từ đó suy ra"))
    b.append(eq("x<sub>v</sub>b + x<sub>f</sub>c = x<sub>1</sub>(b + c)", "99.2"))
    b.append(p(
        "Từ các hệ thức này ta dựng được sơ đồ khối trên Hình 99.2a. Tiếp theo, dùng các quan hệ"))
    b.append(eq("dx<sub>p</sub>/dt = Q/A,&nbsp;&nbsp; Q = Kx<sub>v</sub>,&nbsp;&nbsp; "
                "δ<sub>e</sub> = x<sub>p</sub>/(d + e),&nbsp;&nbsp; x<sub>f</sub> = e·δ<sub>e</sub>",
                "99.3"))
    b.append(p(
        "ta thu được sơ đồ khối của một hệ điều khiển phản hồi điển hình, vẽ trên Hình 99.2b, mô tả "
        "đúng cơ cấu chấp hành thuỷ lực không hồi tiếp đang xét. Sơ đồ này được rút gọn thành sơ đồ "
        "trên Hình 99.2c, và cho ta hàm truyền bậc một của cơ cấu chấp hành:"))
    b.append(fig(2, F.fig(2)))
    b.append(eq("G(s) = δ<sub>e</sub>(s)/δ<sub>ec</sub>(s) = K/(τs + 1)", "99.4"))
    b.append(p(
        "trong đó hệ số khuếch đại K = a(b + c)/(ce), hằng số thời gian τ = Ab(d + e)/(cK<sub>e</sub>) "
        "của cơ cấu chấp hành, và 0,025 &lt; τ &lt; 0,1 s. Với lệnh vào dạng bậc thang, đáp ứng thời "
        "gian điển hình của cơ cấu chấp hành được vẽ trên Hình 99.3."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Mô hình hoá động học van ở mức chi tiết hơn sẽ dẫn tới những mô hình cơ cấu chấp hành thuỷ "
        "lực bậc cao. Ví dụ, hàm truyền của cơ cấu chấp hành đang dùng trên máy bay F-16 là bậc bốn "
        "[1], và đáp ứng tần số của nó được so sánh với xấp xỉ bậc một trên Hình 99.4. Quả thực, trong "
        "thiết kế hệ điều khiển bền vững cần dùng đầy đủ mô hình động học bậc cao của cơ cấu chấp "
        "hành. Như Hình 99.4 cho thấy, mô hình bậc một rút gọn bám rất sát mô hình bậc cao ở dải tần "
        "thấp. Đáng tiếc là ở những tần số cao hơn — đúng dải mà cơ cấu chấp hành sẽ làm việc — lại "
        "tồn tại một sai lệch pha đáng kể, bởi các tần số ấy nằm trong băng thông của những bộ bù điều "
        "khiển bền vững (“khuếch đại cao”) hiện đại."))
    b.append(fig(4, F.fig(4)))
    b.append(p(
        "Bước phát triển tiếp theo của cơ cấu chấp hành là việc cơ giới hoá vòng phản hồi bằng điện "
        "tử, tức kỹ thuật “điều khiển bay bằng dây điện”. Điều này được minh hoạ trên Hình 99.5: cơ "
        "cấu chấp hành dùng một van điều khiển bằng điện (nam châm điện), một chiết áp đo góc lệch "
        "của cánh lái (tức chuyển vị của cơ cấu), còn phần tử công suất của nó — xi lanh lực — là một "
        "xi lanh thuỷ lực."))
    b.append(fig(5, F.fig(5)))

    # ---------------------------------------------------------------- 99.3
    b.append(h2("99.3 Mô hình hoá cơ cấu chấp hành EHA",
                "99.3 EHA actuator modeling"))
    b.append(p(
        "Cơ cấu chấp hành EHA kiểu mới (xem, ví dụ, tài liệu [2]) cho khả năng bảo trì và khả năng "
        "sống sót cao, bởi mọi phần tử của cơ cấu đều được bố trí cụm tại chỗ và không cần một bơm "
        "thuỷ lực trung tâm cùng toàn bộ hệ đường ống áp suất cao kèm theo. Trước hết, chương trình "
        "bày việc mô hình hoá từng mô-đun của EHA."))

    b.append(h3("Động cơ", "Motor"))
    b.append(p(
        "Động cơ điện, với rôto có mômen quán tính J<sub>m</sub> và giảm chấn cơ điện B<sub>m</sub> "
        "(xem Hình 99.6), chịu sự thay đổi của mômen ra, kéo theo dao động của tốc độ quay rôto "
        "Ω<sub>m</sub>. Vì mômen do tải sinh ra chống lại mômen do động cơ sinh ra, nên sự thay đổi "
        "của mômen tải cũng có thể gây ra dao động. Quan hệ đó được viết là"))
    b.append(eq("τ<sub>e</sub>(s) = τ<sub>cmd</sub>(s) − τ<sub>load</sub>(s)", "99.5"))
    b.append(p(
        "trong đó τ<sub>load</sub> là mômen tải do chênh áp của chất lỏng trong bơm gây ra. Kết quả là "
        "một hàm truyền bậc một"))
    b.append(eq("Ω<sub>m</sub>(s)/τ<sub>e</sub>(s) = 1/(J<sub>m</sub>s + b<sub>m</sub>)", "99.6"))
    b.append(fig(6, F.fig(6)))

    b.append(h3("Bơm và chất lỏng", "Pump and fluid"))
    b.append(p(
        "Động cơ điện có tỉ số mômen trên khối lượng hữu hạn, do mật độ từ thông sinh ra là hữu hạn "
        "và bị giới hạn [3]. Các hệ thuỷ lực áp suất cao, với áp suất hệ thống 2000 đến 5000 psi, có "
        "thể sinh ra lực lớn, cho phép kết cấu gọn hơn và tỉ số mômen trên khối lượng cao hơn động cơ "
        "điện. Nói chung, hệ thuỷ lực áp suất cao cứng hơn trước tải so với động cơ điện. Vì thế EHA "
        "dùng một động cơ một chiều để bơm chất lỏng áp suất cao vào buồng xi lanh. Động cơ một chiều "
        "bên trong EHA biến điện năng thành cơ năng; chính bơm mới là khâu biến cơ năng ấy thành thuỷ "
        "năng. Thuỷ năng, khi tác động lên pittông, lại được biến thành cơ năng đủ để dịch chuyển tải, "
        "ví dụ những cánh lái lớn của máy bay."))
    b.append(p(
        "Lưu lượng Q<sub>m</sub> do bơm sinh ra tỉ lệ với tốc độ động cơ, nghĩa là"))
    b.append(eq("Q<sub>m</sub>(s) = (D<sub>m</sub>/2π)·Ω<sub>m</sub>(s)", "99.7"))
    b.append(p(
        "trong đó D<sub>m</sub> là hằng số dung tích riêng của bơm. Lưu lượng chất lỏng thuỷ lực phụ "
        "thuộc chủ yếu vào hai yếu tố: sự thay đổi thể tích buồng và sự thay đổi áp suất do tính nén "
        "được của chất lỏng [4]. Thể tích buồng thay đổi khi pittông dịch chuyển trong buồng với tốc "
        "độ dx<sub>p</sub>/dt. Lưu lượng do thay đổi thể tích buồng được viết là ±Adx<sub>p</sub>/dt. "
        "Các hiệu ứng động học chất lỏng thứ cấp gồm tính nén được, rò rỉ trong và rò rỉ ngoài. Những "
        "hiệu ứng thứ cấp này được mô hình hoá bằng một phương trình bậc một như sau:"))
    b.append(eq("δQ(s) = Q<sub>m</sub>(s) − AsX<sub>p</sub> = [K<sub>s</sub>s + C<sub>l</sub>]P(s)",
                "99.8"))
    b.append(p("và dẫn tới hàm truyền"))
    b.append(eq("P(s)/δQ(s) = 1/(K<sub>s</sub>s + C<sub>l</sub>)", "99.9"))

    b.append(h3("Pittông và cánh lái điều khiển",
                "Piston and flight control surface"))
    b.append(h4("Cơ sở của pittông và cánh lái", "Fundamentals"))
    b.append(p(
        "Áp suất do bơm và chất lỏng tạo ra tác động lên tiết diện pittông (xem Hình 99.7), làm xi "
        "lanh lực duỗi ra hoặc thu vào. Lực này lại sinh ra một mômen qua bản lề để làm lệch cánh lái. "
        "Mômen ấy phải thắng hai thành phần tải: quán tính của cánh lái và tải khí động. Quán tính "
        "cánh lái chủ yếu do cánh có kích thước và khối lượng xác định. Tải khí động chỉ xuất hiện khi "
        "bay, lúc áp suất không khí trên mặt cánh lái tạo ra các lực khí động tác dụng lên nó. Tải khí "
        "động được quyết định bởi ba yếu tố: diện tích mặt cánh lái, mức tải khí động — đại lượng thay "
        "đổi theo độ cao và tốc độ bay — và góc tương đối giữa cánh với dòng gió. Góc giữa cánh và "
        "dòng gió phụ thuộc góc lệch của cánh và góc tấn của máy bay."))
    b.append(h4("Động lực học pittông và cánh lái", "Dynamics"))
    b.append(p(
        "Độ lớn của F<sub>A</sub> tác dụng lên pittông bằng " + PBAR + "A, trong đó " + PBAR + " là "
        "chênh áp do bơm và chất lỏng tạo ra, còn A là diện tích bề mặt pittông. Như vậy lực do bơm và "
        "chất lỏng sinh ra được viết là"))
    b.append(eq("F<sub>A</sub> = " + PBAR + "A", "99.10"))
    b.append(p(
        "Động lực học của pittông, với khối lượng pittông M<sub>p</sub> và giảm chấn pittông "
        "B<sub>p</sub>, được mô tả bằng mô hình bậc hai:"))
    b.append(eq("F<sub>A</sub> − F<sub>P</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]X<sub>p</sub>",
                "99.11"))
    b.append(p(
        "Mômen tác dụng lên cánh lái do sự mất cân bằng lực này được mô tả bằng"))
    b.append(eq("τ<sub>R</sub> = (K<sub>h</sub>/R<sub>h</sub>)(X<sub>p</sub> − X<sub>L</sub>)", "99.12"))
    b.append(p(
        "trong đó K<sub>h</sub> là hằng số độ cứng của bản lề và R<sub>h</sub> là chiều dài tay đòn bản "
        "lề. Quán tính của cánh ổn định tác động ngược lại mômen do cơ cấu chấp hành sinh ra, sao cho"))
    b.append(eq("τ<sub>R</sub> − τ<sub>L</sub> = [J<sub>L</sub>s² + B<sub>L</sub>s]θ<sub>L</sub>",
                "99.13"))
    b.append(p(
        "trong đó τ<sub>L</sub> là mômen do tải khí động và quán tính cánh ổn định tạo ra. Các biến "
        "J<sub>L</sub> và B<sub>L</sub> biểu thị đặc trưng khối lượng của cánh lái."))
    b.append(fig(7, F.fig(7)))
    b.append(h4("Mô hình khớp bản lề cứng", "Stiff hinge joint model"))
    b.append(p(
        "Các phương trình 99.11 đến 99.13 mô tả một mô hình động lực học tải khá phức tạp. Có thể giảm "
        "độ phức tạp ấy nếu coi liên kết giữa cơ cấu chấp hành và cánh lái là cứng. Đây là một giả "
        "thiết hợp lý, vì tần số riêng của bản lề trong một hệ truyền động được thiết kế tốt lớn hơn "
        "nhiều so với băng thông của cơ cấu chấp hành mà ta quan tâm. Khi đó động lực học của pittông "
        "và của tải vẫn được viết là"))
    b.append(eq("F<sub>A</sub> − F<sub>P</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]X<sub>p</sub>",
                "99.14"))
    b.append(p("và"))
    b.append(eq("τ<sub>R</sub> − τ<sub>L</sub> = [J<sub>L</sub>s² + B<sub>L</sub>s]θ<sub>L</sub>",
                "99.15"))
    b.append(p("Chia phương trình 99.15 cho R<sub>h</sub> ta được"))
    b.append(eq("τ<sub>R</sub>/R<sub>h</sub> − τ<sub>L</sub>/R<sub>h</sub> = "
                "[(J<sub>L</sub>s² + B<sub>L</sub>s)/R<sub>h</sub>]θ<sub>L</sub>", "99.16"))
    b.append(p(
        "Giả thiết cụm bản lề là cứng, tức F<sub>R</sub> ≈ F<sub>P</sub>. Khi đó, cộng phương trình "
        "99.14 với phương trình 99.16 ta được"))
    b.append(eq("F<sub>A</sub> − τ<sub>L</sub>/R<sub>h</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]"
                "X<sub>p</sub> + [(J<sub>L</sub>s² + B<sub>L</sub>s)/R<sub>h</sub>]θ<sub>L</sub>",
                "99.17"))
    b.append(p("trong đó τ<sub>L</sub> được định nghĩa là"))
    b.append(eq("τ<sub>L</sub> = (Load<sub>aero</sub>)θ<sub>L</sub>", "99.18"))
    b.append(p(
        "Vì tính cứng của khớp hàm ý X<sub>p</sub> = X<sub>L</sub> và θ<sub>L</sub> = "
        "X<sub>p</sub>/R<sub>h</sub>, phương trình 99.17 được rút gọn tiếp thành"))
    b.append(eq("F<sub>e</sub> = F<sub>A</sub> − τ<sub>L</sub>/R<sub>h</sub> = "
                "{[(M<sub>p</sub> + J<sub>L</sub>/R<sub>h</sub>²)s² + "
                "(B<sub>p</sub> + B<sub>L</sub>/R<sub>h</sub>²)s]}X<sub>p</sub>", "99.19"))
    b.append(p("hay, viết dưới dạng hàm truyền:"))
    b.append(eq("X<sub>p</sub>(s)/F<sub>e</sub>(s) = 1/{s[(M<sub>p</sub> + J<sub>L</sub>/R<sub>h</sub>²)s"
                " + (B<sub>p</sub> + B<sub>L</sub>/R<sub>h</sub>²)]}", "99.20"))
    b.append(p(
        "Phương trình 99.20 biểu diễn một mô hình rút gọn của động lực học tải. Mô hình thiết kế rút "
        "gọn và đầy đủ của EHA thuần, không có bộ điều khiển, được vẽ trên Hình 99.8, dựa trên mô hình "
        "của từng phần tử thành phần."))
    b.append(fig(8, F.fig(8)))

    b.append(h3("Mômen bản lề", "Hinge moments"))
    b.append(p(
        "Các tải khí động nói trên mô tả mômen chống lại chuyển động của pittông. Như vậy, tải do dòng "
        "không khí chảy trên và dưới cánh lái sinh ra tác dụng một mômen lên cụm bản lề, và mômen ấy "
        "lại tạo áp suất ngược lên pittông. Mômen bản lề được mô hình hoá như sau:"))
    b.append(eq("τ<sub>L</sub> = q&#772;S<sub>t</sub>R<sub>h</sub>[C<sub>hα</sub>"
                "(α(s)/θ<sub>L</sub>(s)) + C<sub>hδ</sub>]θ<sub>L</sub>", "99.21"))
    b.append(p(
        "trong đó S<sub>t</sub> là diện tích mặt cánh lái, q&#772; là áp suất động, còn "
        "C<sub>hα</sub> và C<sub>hδ</sub> là các hệ số mômen bản lề của cánh lái theo góc tấn và theo "
        "góc lệch δ. Áp suất động của tải khí động là một hàm của tốc độ bay U<sub>0</sub> và khối "
        "lượng riêng không khí ρ [2], được viết là"))
    b.append(eq("q&#772; = ½ρU<sub>0</sub>²", "99.22"))
    b.append(p(
        "Khối lượng riêng không khí trong khí quyển tiêu chuẩn giảm theo hàm mũ khi độ cao tăng. Áp "
        "suất động q&#772; tăng khi số Mach tăng và độ cao giảm. Với những máy bay tiêm kích hiện đại "
        "có toàn bộ đuôi chuyển động được, khi đó C<sub>hα</sub> ≈ C<sub>hδ</sub>, mômen bản lề được "
        "mô hình hoá bằng"))
    b.append(eq("τ<sub>L</sub> = q&#772;S<sub>t</sub>R<sub>h</sub>C<sub>hδ</sub>"
                "[α(s)/θ<sub>L</sub>(s) + 1]θ<sub>L</sub>", "99.23"))

    b.append(h3("Xấp xỉ chu kỳ ngắn của máy bay",
                "Aircraft short period approximation"))
    b.append(p(
        "Nếu coi tốc độ bay tới của máy bay là không đổi (tức nhiễu tốc độ u ≈ 0), có thể bỏ qua "
        "phương trình lực theo trục X, vì nó không đóng góp đáng kể vào dao động chu kỳ ngắn [5]. "
        "Nhờ vậy, ta rút ra được xấp xỉ chu kỳ ngắn của kênh dọc máy bay — phần liên quan trực tiếp "
        "đến động lực học cơ cấu chấp hành — và viết nó dưới dạng"))
    b.append(eq("[α̇&nbsp; q̇]<sup>T</sup> = [[z<sub>α</sub>&nbsp; z<sub>q</sub>], "
                "[m<sub>α</sub>&nbsp; m<sub>q</sub>]]·[α&nbsp; q]<sup>T</sup> + "
                "[z<sub>δ</sub>&nbsp; M<sub>δ</sub>]<sup>T</sup>[δ<sub>e</sub>]", "99.24"))
    b.append(p("Hệ này cho một hàm truyền pha cực tiểu bậc hai dạng:"))
    b.append(eq("α(s)/δ(s) = −K(s + a)/[(s + b)(s + c)]", "99.25"))
    b.append(fig(9, F.fig(9)))
    b.append(p(
        "Trong dải tần quan tâm, xấp xỉ chu kỳ ngắn bám rất sát mô hình trạng thái đầy đủ. Điều này "
        "thấy rõ trên Hình 99.9: đường liền biểu diễn đáp ứng tần số của mô hình trạng thái đầy đủ, "
        "còn các dấu chấm biểu diễn đáp ứng tần số của mô hình chu kỳ ngắn; đặc tính pha và đặc tính "
        "suy giảm của hai mô hình khớp nhau chặt ở tần số cao. Như hình vẽ cũng cho thấy, xấp xỉ này "
        "không còn đúng với những tần số dưới 0,5 rad/giây, vì ở đó chế độ dọc chậm — gọi là "
        "<i>phugoid</i> — bắt đầu có tác dụng."))

    b.append(h3("Lý thuyết phản hồi định lượng (QFT)",
                "Quantitative Feedback Theory (QFT)"))
    b.append(p(
        "Các bộ bù bền vững theo QFT [3,6] là công cụ lý tưởng để đạt được đáp ứng mong muốn từ một "
        "cơ cấu chấp hành. Trong lý thuyết điều khiển, tính từ “bền vững” hàm ý rằng hệ được điều "
        "khiển — ở đây là cơ cấu chấp hành — vẫn ổn định trên toàn bộ miền làm việc, kháng được nhiễu "
        "và chỉ bị suy giảm chất lượng ở mức tối thiểu so với các chỉ tiêu đề ra. Một hệ điều khiển "
        "phản hồi thiết kế theo QFT, dùng phản hồi đầu ra, bảo đảm đầu ra bám theo giá trị đầu vào bất "
        "chấp bất định tham số hay nhiễu. Với một hệ phản hồi có hệ số khuếch đại bằng một và mô hình "
        "đối tượng bất định, đầu ra có thể thay đổi tuỳ theo trạng thái của đối tượng; nhưng với một "
        "hệ điều khiển phản hồi QFT bền vững, đầu ra sẽ ít thay đổi hơn nhiều. Tuy vậy, hệ khuếch đại "
        "bằng một không điều khiển được đáp ứng bám, nên buộc phải thêm một bộ lọc trước."))
    b.append(p(
        "Bất định của đối tượng (cụ thể là của cơ cấu chấp hành) có thể do dung sai chế tạo. Ví dụ, "
        "một chi tiết A được quy định dài 10 ± 0,1 mm. Trong một lô sản xuất lớn, chiều dài chi tiết A "
        "có thể nằm bất kỳ đâu trong khoảng 9,9 đến 10,1 mm. Khoảng dung sai ấy có thể đủ lớn để tạo ra "
        "những thay đổi nhận thấy được ở mô hình đối tượng. Bất định cũng có thể do môi trường, cụ thể "
        "là do điều kiện làm việc của hệ (cơ cấu chấp hành). Ví dụ, các tham số của mô hình máy bay "
        "thay đổi rất nhiều theo độ cao và tốc độ bay. Cuối cùng, chất lượng của nhiều chi tiết suy "
        "giảm theo thời gian, làm phát sinh thêm một nguồn bất định nữa."))
    b.append(p(
        "Mô thức thiết kế QFT tính đến ngay những thay đổi của đối tượng trong quy trình thiết kế. Đó "
        "là một kỹ thuật thiết kế tuyến tính, dùng để thiết kế bộ điều khiển tuyến tính bền vững cho "
        "các hệ điều khiển tuyến tính hoặc phi tuyến [3,6] — ở đây là hệ điều khiển cơ cấu chấp hành. "
        "Chừng nào mọi yêu cầu thiết kế QFT còn được thoả mãn, đáp ứng đầu ra còn được bảo đảm nằm "
        "trong các biên chất lượng. Bước đầu tiên của quy trình thiết kế là xác lập các biên bám trên "
        "và dưới. Nhiễu lớn nhất cho phép dùng để xác định biên nhiễu. Góc dự trữ pha, dự trữ "
        "khuếch đại hoặc giá trị đỉnh lớn nhất dùng để xác lập biên ổn định. Các biên này hợp lại "
        "định ra giới hạn chất lượng của hệ. Bước tiếp theo là phân tích hệ để xác định những tham số "
        "sẽ gây ra thay đổi đáng kể ở đối tượng. Hệ — vốn thường chỉ được mô hình hoá bằng một hàm "
        "truyền đối tượng duy nhất trong các phương pháp thiết kế khác — nay được mô hình hoá đầy đủ "
        "hơn thành một <i>tập</i> hàm truyền đối tượng. Những thay đổi ấy tạo thành một miền đóng "
        "trên giản đồ Nichols (biên độ – pha), gọi là <i>mẫu</i> (template); mẫu càng lớn thì mức bất "
        "định của đối tượng càng cao. Mẫu ở những tần số khác nhau có kích thước và hình dạng khác "
        "nhau."))
    b.append(p(
        "Một khía cạnh quan trọng nhất của việc mô hình hoá là phân tích kỹ lưỡng đối tượng chấp hành "
        "thuần, nhằm tìm ra các nguồn gây thay đổi. Với ứng dụng máy bay, ba nguồn thay đổi lớn nhất "
        "là dao động của tải khí động trên cánh lái, mômen của động cơ và áp suất chất lỏng của bơm "
        "thuỷ lực."))

    # ---------------------------------------------------------------- 99.5
    b.append(h2("99.4 Thiết kế bộ bù cho cơ cấu chấp hành",
                "99.4 Actuator compensator design"))
    b.append(p(
        "Các bộ bù QFT, vốn được thiết kế trong miền tần số, đặc biệt thích hợp cho hệ điều khiển cơ "
        "cấu chấp hành. Bộ bù QFT xử lý các đầu vào của nó — chuyển vị đặt của cơ cấu chấp hành và vị "
        "trí hiện thời đo được của cơ cấu — rồi sinh ra một tín hiệu lệnh cấp cho, ví dụ, van nam "
        "châm điện trong một cơ cấu chấp hành thuỷ lực, hoặc một dòng điện cấp cho động cơ một chiều "
        "trong EHA. Để tiến hành thiết kế bộ bù QFT cho cơ cấu chấp hành, sơ đồ khối trên Hình 99.7 "
        "được chuyển thành cấu trúc vòng trong và vòng ngoài chuẩn của QFT như trên Hình 99.10 "
        "[2,3,6]. Với bài toán thiết kế này, nhiễu ngoài d<sub>2</sub>(t) có thể bỏ qua, tức "
        "d<sub>2</sub>(t) = 0, còn nhiễu d<sub>1</sub>(t) mô tả một sai lệch đo có thể có. Vòng trong "
        "điều khiển tốc độ góc của động cơ, còn vòng ngoài điều khiển góc lệch của cánh. Vì việc bám "
        "ở vòng trong ít quan trọng hơn — chức năng của nó là giảm mức bất định cho vòng ngoài — nên "
        "bộ lọc trước của vòng trong có thể đặt bằng một, và yêu cầu về chất lượng bám được giao toàn "
        "bộ cho bộ lọc trước F<sub>Θ</sub> của vòng ngoài."))
    b.append(fig(10, F.fig(10)))

    # ---------------------------------------------------------------- 99.6
    b.append(h2("99.5 Kết luận", "99.5 Conclusion"))
    b.append(p(
        "Chương này đã trình bày việc mô hình hoá một hệ thứ bậc các cơ cấu chấp hành thuỷ lực. Trọng "
        "tâm là mô hình hoá các EHA hiện đại, với mô hình động học của từng phần tử con được xây dựng "
        "cẩn thận. Cách tiếp cận ở đây là tiếp cận hệ thống đối với việc mô hình hoá và thiết kế cơ "
        "cấu chấp hành, trong đó cấu trúc phản hồi được nhấn mạnh. Chương cũng chỉ rõ rằng, do các "
        "tương tác phản hồi phức tạp cùng tác động, việc mô hình hoá cơ cấu chấp hành một cách đúng "
        "đắn đòi hỏi phải xét nó trong toàn bộ bối cảnh của hệ điều khiển mà nó sẽ được dùng. Vì thế "
        "mà ở đây ứng dụng hàng không được chọn làm đối tượng trình bày. Đồng thời, cơ cấu chấp hành "
        "được nhìn không phải như một bộ phận của hệ điều khiển, mà như một hệ điều khiển theo đúng "
        "nghĩa của nó. Nhờ vậy có thể chứng minh rằng những khâu liên kết phản hồi cơ khí đơn giản "
        "vốn đảm nhiệm vai trò phần tử điều khiển của cơ cấu chấp hành hoàn toàn có thể được thay "
        "bằng một bộ bù điện tử đầy đủ, linh hoạt hơn, chất lượng cao hơn và bền vững hơn."))
    b.append(p(
        "Về các thiết bị và cảm biến điện – khí nén, đây là những phần tử then chốt trong các hệ điều "
        "khiển lưu lượng chất lỏng và/hoặc chất khí, ví dụ trong công nghiệp hoá chất. Trong hàng "
        "không, cảm biến điện – khí nén được dùng để đo tốc độ bay, độ cao, góc tấn và góc trượt bên "
        "của máy bay; các chức năng này được bố trí chung trong máy tính dữ liệu khí động (ADC). Ngày "
        "nay, cảm biến hiện đại dùng tác động phản hồi để nâng cao độ chính xác, và vì thế việc thiết "
        "kế các thiết bị và cảm biến điện – khí nén hiện đại về mặt quan điểm cũng tương tự như thiết "
        "kế EHA. Thông tin chi tiết về cơ cấu chấp hành và cảm biến có thể tìm trong các tài liệu "
        "tham khảo 4 và 7."))

    # ---------------------------------------------------------------- symbols
    b.append(h2("Ký hiệu", "Nomenclature"))
    b.append(_nom("vi"))

    # ---------------------------------------------------------------- notes
    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "Bản in gốc có một số lỗi ấn loát đã được sửa trong bản dịch này. (1) Ký hiệu chênh áp do bơm "
        "tạo ra trong phương trình 99.10 bị lỗi font khi in; ở đây giữ nguyên dạng " + PBAR +
        " như trên Hình 99.8. (2) Dòng ký hiệu “J moment of inertia; o, ovin” trong phần Nomenclature "
        "là chữ bị hỏng, phải đọc là “ω, ω<sub>m</sub>”. (3) Trong mục Mômen bản lề, chữ q vừa dùng "
        "cho tốc độ chúc ngóc vừa dùng cho áp suất động; bản dịch phân biệt hai đại lượng bằng "
        "q&#772; cho áp suất động. (4) Phương trình 99.24 in thiếu dấu ngoặc của vectơ trạng thái; "
        "bản dịch trình bày lại dưới dạng vectơ thu gọn."))

    # ---------------------------------------------------------------- refs
    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "O. R. Reynolds, M. Pachter, and C. H. Houpis, “Full envelope flight control system design "
        "using quantitative feedback theory,” <i>AIAA J. Guidance Control Dyn.</i>, 19, 1023–1029, 1996.",
        "K. H. Kang, <i>Electro-Hydrostatic Actuator Controller Design Using Quantitative Feedback "
        "Theory</i>, MS thesis, Graduate School of Engineering, Air Force Institute of Technology, "
        "Wright-Patterson AFB, OH, December 1994, AFIT/GE/ENG/94D-18.",
        "C. H. Houpis, M. Pachter, S. Rasmussen, and R. Sating, <i>Quantitative Feedback Theory for "
        "the Engineer</i>, Wright Laboratory Technical Report, WL-TR-95-3061, Wright Laboratory, "
        "Wright-Patterson AFB, OH, June 1995.",
        "C. W. de Silva, <i>Control Sensors and Actuators</i>, Englewood Cliffs, NJ: Prentice-Hall, 1989.",
        "J. H. Blakelock, <i>Automatic Control of Aircraft and Missiles</i>, New York: John Wiley &amp; "
        "Sons, 1991.",
        "J. J. D’Azzo and C. H. Houpis, <i>Linear Control System Analysis and Design — Conventional "
        "and Modern</i>, 4th ed., New York: McGraw-Hill, 1988.",
        "E. H. J. Pallet and S. Coyle, <i>Automatic Flight Control</i>, Oxford, U.K., Blackwell, 1993.",
    ]))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []
    b.append(p(
        "In a control system the output of the controller — also called the equalizer or compensator — "
        "which acts on the command and feedback signals, is invariably sent to an actuator. The "
        "actuator is a power element critically positioned at the plant input and, to a large extent, "
        "it determines the performance of the overall control system. The importance of modelling the "
        "actuation element accurately, so that the desired control performance is achieved and held "
        "over the operating range, can therefore hardly be overstated."))
    b.append(p(
        "Items such as the actuator's phase-lag characteristics, parameter variation and ageing, "
        "sensor noise and the operating scenario — in a flight-control context, the <i>flight "
        "conditions</i> — must be considered explicitly during design. A robust control system, one "
        "that accounts for all of these, requires a good understanding and an accurate model of the "
        "actuation element. This chapter sets out the actuator modelling process."))

    b.append(h2("99.1 Introduction"))
    b.append(p(
        "Power-to-weight considerations have driven actuator design through four generations: "
        "pneumatic, hydraulic, electrohydraulic and, most recently in flight-control applications, "
        "electrohydrostatic. The point of view taken throughout this chapter is that the actuator "
        "element already constitutes a feedback control system in its own right. On that reading the "
        "actuator comprises an “amplifier” element (the servo valve), a power element (the ram), an "
        "actuator displacement sensor, and a controller about which more is said below."))
    b.append(p(
        "It is equally important that the actuator subsystem be seen in the context of the complete "
        "control system — a flight-control system, say. A relatively simple hydraulic actuator is "
        "considered first; the focus then shifts to the modern electrohydrostatic actuator (EHA), "
        "which in flight control offers a high degree of combat survivability and easier "
        "maintainability because its components are collocated with the actuator. Since the EHA needs "
        "no long hydraulic lines, the maintenance time and equipment required are reduced, and the "
        "profile exposed to hostile fire shrinks substantially. Actuator failures from various causes "
        "and from ageing must also enter the design of the overall system. A robust control system "
        "built around an actuator demands an accurate actuator model if it is to meet its performance "
        "specification; the EHA and its flight-control application are used here as the vehicle for "
        "presenting the modelling process."))
    b.append(h3("Actuator modeling requirements"))
    b.append(p(
        "When an actuator has to be replaced in a control system, for the reasons just cited, by an "
        "off-the-shelf unit, the robustness of the overall system must be unaffected by the "
        "replacement. The actuator design process therefore entails:"))
    b.append('<ol style="margin:-.3rem 0 1.2rem 1.3rem;line-height:1.85;font-size:.95rem">'
             '<li>Derivation of an accurate mathematical model for the actuator.</li>'
             '<li>Sensitivity analyses on the actuator control system, covering sensitivity to '
             'variations in load, component efficiencies, physical plant parameters and actuator '
             'sensor noise.</li>'
             '<li>Identification of a reasonable set of plant variations, based on the sensitivity '
             'analysis, which is required for designing a robust actuator control system that will '
             'meet the specification in the presence of the predicted variations.</li>'
             '</ol>')

    b.append(h2("99.2 Hydraulic actuator modeling"))
    b.append(p(
        "The modelling of a purely hydraulic actuator employed in an irreversible flight-control "
        "system is presented first. With the notation of Fig. 99.1 the following relationships hold:"))
    b.append(eq("x<sub>1</sub> = δ<sub>ec</sub>·a", "99.1a"))
    b.append(eq("(x<sub>v</sub> − x<sub>f</sub>)/(b + c) = (x<sub>v</sub> − x<sub>1</sub>)/c", "99.1b"))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p("which yield"))
    b.append(eq("x<sub>v</sub>b + x<sub>f</sub>c = x<sub>1</sub>(b + c)", "99.2"))
    b.append(p("From these equations Fig. 99.2a is obtained. Next, the relationships"))
    b.append(eq("dx<sub>p</sub>/dt = Q/A,&nbsp;&nbsp; Q = Kx<sub>v</sub>,&nbsp;&nbsp; "
                "δ<sub>e</sub> = x<sub>p</sub>/(d + e),&nbsp;&nbsp; x<sub>f</sub> = e·δ<sub>e</sub>",
                "99.3"))
    b.append(p(
        "are used to yield the block diagram of a typical feedback control system (Fig. 99.2b), which "
        "represents the irreversible hydraulic actuator under consideration. That diagram simplifies "
        "to Fig. 99.2c, which yields the first-order transfer function of the actuator:"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(eq("G(s) = δ<sub>e</sub>(s)/δ<sub>ec</sub>(s) = K/(τs + 1)", "99.4"))
    b.append(p(
        "where the gain K = a(b + c)/(ce), the actuator time constant τ = Ab(d + e)/(cK<sub>e</sub>), "
        "and 0.025 &lt; τ &lt; 0.1 s. For a step command, a typical actuator time response is shown in "
        "Fig. 99.3."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "More detailed dynamic modelling of the valve leads to higher-order hydraulic actuator models. "
        "The transfer function of the actuator currently used on the F-16 is of fourth order [1], and "
        "its frequency response is compared with the first-order approximation in Fig. 99.4. The "
        "full-blown high-order model should indeed be used in robust control design. As Fig. 99.4 "
        "shows, the simplified first-order model fits the high-order one well at low frequency; "
        "unfortunately a significant phase difference appears at the higher frequencies where the "
        "actuator will actually operate, for those frequencies lie inside the bandwidth of modern "
        "robust (“high-gain”) compensators."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "The next step in actuator development is the electronic, fly-by-wire mechanisation of the "
        "feedback loop, shown in Fig. 99.5: the actuator employs a solenoid-controlled valve, a "
        "potentiometer that measures the control-surface deflection (actuator displacement), and a "
        "hydraulic cylinder as the power element, the ram."))
    b.append(fig(5, F.fig(5), "en"))

    b.append(h2("99.3 EHA actuator modeling"))
    b.append(p(
        "The novel EHA actuator (see, e.g., Reference 2) offers a high degree of maintainability and "
        "survivability because all its elements are collocated and no central hydraulic pump with the "
        "attendant high-pressure plumbing is needed. The modelling of the EHA modules is outlined "
        "first."))
    b.append(h3("Motor"))
    b.append(p(
        "Electric motors, with rotor moment of inertia J<sub>m</sub> and electromechanical damping "
        "B<sub>m</sub> (Fig. 99.6), are subject to variations in output torque and consequent "
        "fluctuations in rotor speed Ω<sub>m</sub>. Since the load torque counteracts the torque the "
        "motor generates, perturbation may also come from variations in load torque:"))
    b.append(eq("τ<sub>e</sub>(s) = τ<sub>cmd</sub>(s) − τ<sub>load</sub>(s)", "99.5"))
    b.append(p(
        "where τ<sub>load</sub> is the load torque due to the differential pressure of the fluid in "
        "the pump. This gives a first-order transfer function"))
    b.append(eq("Ω<sub>m</sub>(s)/τ<sub>e</sub>(s) = 1/(J<sub>m</sub>s + b<sub>m</sub>)", "99.6"))
    b.append(fig(6, F.fig(6), "en"))
    b.append(h3("Pump and fluid"))
    b.append(p(
        "Electric motors have a limited torque-to-mass ratio, because the magnetic flux density that "
        "can be generated is finite and limited [3]. High-pressure hydraulic systems, at 2000 to 5000 "
        "psi, can generate large forces and so yield more compact arrangements and higher "
        "torque-to-mass ratios than electric motors; in general they are also stiffer against the "
        "load. The EHA therefore uses a dc motor to pump high-pressure fluid into the piston chamber. "
        "The dc motor inside the EHA converts electric power into mechanical power; the pump converts "
        "that mechanical power into hydraulic power; and the hydraulic power, acting on the piston, is "
        "converted back into mechanical power capable of moving the load — large flight-control "
        "surfaces, for instance."))
    b.append(p(
        "The flow rate Q<sub>m</sub> generated by the pump is proportional to motor speed:"))
    b.append(eq("Q<sub>m</sub>(s) = (D<sub>m</sub>/2π)·Ω<sub>m</sub>(s)", "99.7"))
    b.append(p(
        "where D<sub>m</sub> is the pump displacement constant. The flow rate depends primarily on two "
        "things: the change in chamber volume and the change in pressure due to fluid compressibility "
        "[4]. Chamber volume changes as the piston moves through the chamber at speed "
        "dx<sub>p</sub>/dt, and the flow due to that change is ±Adx<sub>p</sub>/dt. Secondary fluid "
        "effects — compressibility, internal leakage and external leakage — are modelled by a "
        "first-order equation:"))
    b.append(eq("δQ(s) = Q<sub>m</sub>(s) − AsX<sub>p</sub> = [K<sub>s</sub>s + C<sub>l</sub>]P(s)",
                "99.8"))
    b.append(p("which gives the transfer function"))
    b.append(eq("P(s)/δQ(s) = 1/(K<sub>s</sub>s + C<sub>l</sub>)", "99.9"))

    b.append(h3("Piston and flight control surface"))
    b.append(h4("Fundamentals"))
    b.append(p(
        "The pressure developed by the pump and fluid acts on the piston surface (Fig. 99.7), causing "
        "the ram to extend or retract. That force generates a torque through a hinge which deflects "
        "the control surface. The torque has to overcome two load components: control-surface inertia "
        "and aerodynamic load. Surface inertia follows from the surface having a certain size and "
        "mass. The aerodynamic load occurs only in flight, when air pressure over the surface applies "
        "aerodynamic forces to it, and it is fixed by three factors: the surface area of the control "
        "surface, the aerodynamic loading — which varies with altitude and airspeed — and the relative "
        "angle of the surface to the wind. That angle depends on the surface deflection and on the "
        "aircraft angle of attack."))
    b.append(h4("Dynamics"))
    b.append(p(
        "The magnitude of F<sub>A</sub> acting on the piston is " + PBAR + "A, where " + PBAR + " is "
        "the differential pressure developed by the pump and fluid and A the piston area. The force "
        "created by pump and fluid is therefore"))
    b.append(eq("F<sub>A</sub> = " + PBAR + "A", "99.10"))
    b.append(p(
        "The piston dynamics, with piston mass M<sub>p</sub> and damping B<sub>p</sub>, follow a "
        "second-order model:"))
    b.append(eq("F<sub>A</sub> − F<sub>P</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]X<sub>p</sub>",
                "99.11"))
    b.append(p(
        "The torque acting on the control surface because of this force imbalance is described by"))
    b.append(eq("τ<sub>R</sub> = (K<sub>h</sub>/R<sub>h</sub>)(X<sub>p</sub> − X<sub>L</sub>)", "99.12"))
    b.append(p(
        "where K<sub>h</sub> is the hinge stiffness constant and R<sub>h</sub> the hinge length. The "
        "stabilator inertia acts against the torque the actuator generates, so that"))
    b.append(eq("τ<sub>R</sub> − τ<sub>L</sub> = [J<sub>L</sub>s² + B<sub>L</sub>s]θ<sub>L</sub>",
                "99.13"))
    b.append(p(
        "where τ<sub>L</sub> is the torque created by aerodynamic load and stabilator inertia, and "
        "J<sub>L</sub> and B<sub>L</sub> represent the mass properties of the control surface."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(h4("Stiff hinge joint model"))
    b.append(p(
        "Equations 99.11 to 99.13 represent a rather complex model of load dynamics. The complexity "
        "drops if the linkage between actuator and control surface is considered rigid — a valid "
        "assumption, since the natural frequency of the hinge in a well-designed actuation system is "
        "much greater than the actuator bandwidth of concern. The piston and load dynamics are then "
        "still expressed as"))
    b.append(eq("F<sub>A</sub> − F<sub>P</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]X<sub>p</sub>",
                "99.14"))
    b.append(p("and"))
    b.append(eq("τ<sub>R</sub> − τ<sub>L</sub> = [J<sub>L</sub>s² + B<sub>L</sub>s]θ<sub>L</sub>",
                "99.15"))
    b.append(p("Dividing Eq. 99.15 by R<sub>h</sub> yields"))
    b.append(eq("τ<sub>R</sub>/R<sub>h</sub> − τ<sub>L</sub>/R<sub>h</sub> = "
                "[(J<sub>L</sub>s² + B<sub>L</sub>s)/R<sub>h</sub>]θ<sub>L</sub>", "99.16"))
    b.append(p(
        "Assuming rigidity of the hinge assembly, F<sub>R</sub> ≈ F<sub>P</sub>. Adding Eqs. 99.14 "
        "and 99.16 then gives"))
    b.append(eq("F<sub>A</sub> − τ<sub>L</sub>/R<sub>h</sub> = [M<sub>p</sub>s² + B<sub>p</sub>s]"
                "X<sub>p</sub> + [(J<sub>L</sub>s² + B<sub>L</sub>s)/R<sub>h</sub>]θ<sub>L</sub>",
                "99.17"))
    b.append(p("where τ<sub>L</sub> is defined as"))
    b.append(eq("τ<sub>L</sub> = (Load<sub>aero</sub>)θ<sub>L</sub>", "99.18"))
    b.append(p(
        "Since rigidity implies X<sub>p</sub> = X<sub>L</sub> and θ<sub>L</sub> = "
        "X<sub>p</sub>/R<sub>h</sub>, Eq. 99.17 reduces further to"))
    b.append(eq("F<sub>e</sub> = F<sub>A</sub> − τ<sub>L</sub>/R<sub>h</sub> = "
                "{[(M<sub>p</sub> + J<sub>L</sub>/R<sub>h</sub>²)s² + "
                "(B<sub>p</sub> + B<sub>L</sub>/R<sub>h</sub>²)s]}X<sub>p</sub>", "99.19"))
    b.append(p("or, in transfer-function form,"))
    b.append(eq("X<sub>p</sub>(s)/F<sub>e</sub>(s) = 1/{s[(M<sub>p</sub> + J<sub>L</sub>/R<sub>h</sub>²)s"
                " + (B<sub>p</sub> + B<sub>L</sub>/R<sub>h</sub>²)]}", "99.20"))
    b.append(p(
        "Equation 99.20 is a simplified model of the load dynamics. A complete simplified design model "
        "of the bare EHA, without the controller, is shown in Fig. 99.8 using the individual component "
        "models."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(h3("Hinge moments"))
    b.append(p(
        "The aerodynamic loads described above are the torque opposing piston motion. Load generated "
        "by the air flowing above and below the control surface applies a torque to the hinge "
        "assembly, which in turn adds back-pressure to the piston. The hinge moment is modelled as"))
    b.append(eq("τ<sub>L</sub> = q&#772;S<sub>t</sub>R<sub>h</sub>[C<sub>hα</sub>"
                "(α(s)/θ<sub>L</sub>(s)) + C<sub>hδ</sub>]θ<sub>L</sub>", "99.21"))
    b.append(p(
        "where S<sub>t</sub> is the surface area of the control surface, q&#772; the dynamic pressure, "
        "and C<sub>hα</sub> and C<sub>hδ</sub> the hinge-moment coefficients with respect to angle of "
        "attack and to surface deflection δ. The dynamic pressure q&#772; is a function of airspeed "
        "U<sub>0</sub> and air density ρ [2]:"))
    b.append(eq("q&#772; = ½ρU<sub>0</sub>²", "99.22"))
    b.append(p(
        "Air density in a standard atmosphere drops exponentially with altitude, and q&#772; rises as "
        "the Mach number rises and altitude falls. For modern fighters with all-movable tails, where "
        "C<sub>hα</sub> ≈ C<sub>hδ</sub>, the hinge moment is modelled by"))
    b.append(eq("τ<sub>L</sub> = q&#772;S<sub>t</sub>R<sub>h</sub>C<sub>hδ</sub>"
                "[α(s)/θ<sub>L</sub>(s) + 1]θ<sub>L</sub>", "99.23"))
    b.append(h3("Aircraft short period approximation"))
    b.append(p(
        "If the aircraft forward speed is taken as constant (speed perturbations u ≈ 0), the X-force "
        "equation can be neglected, since it does not contribute significantly to the short-period "
        "oscillation [5]. The short-period approximation of the longitudinal channel — the part "
        "relevant to actuator dynamics — is then extracted and written as"))
    b.append(eq("[α̇&nbsp; q̇]<sup>T</sup> = [[z<sub>α</sub>&nbsp; z<sub>q</sub>], "
                "[m<sub>α</sub>&nbsp; m<sub>q</sub>]]·[α&nbsp; q]<sup>T</sup> + "
                "[z<sub>δ</sub>&nbsp; M<sub>δ</sub>]<sup>T</sup>[δ<sub>e</sub>]", "99.24"))
    b.append(p("This yields a second-order minimum-phase transfer function of the form"))
    b.append(eq("α(s)/δ(s) = −K(s + a)/[(s + b)(s + c)]", "99.25"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "For the frequency range of interest the short-period approximation closely resembles the full "
        "state model. In Fig. 99.9 the solid line is the full-model frequency response and the dots "
        "the short-period response: phase and attenuation match closely at high frequency. As the "
        "figure also shows, the approximation is not valid below 0.5 rad/s, where the slow "
        "longitudinal mode — the phugoid — takes effect."))
    b.append(h3("Quantitative Feedback Theory (QFT)"))
    b.append(p(
        "Robust QFT compensators [3,6] are ideal for obtaining the desired response from an actuator. "
        "Robust, in control theory, means the system under control — here the actuator — stays stable "
        "throughout its operating envelope, rejects disturbances and degrades the performance "
        "specification as little as possible. A QFT-designed feedback system using output feedback "
        "ensures that the output tracks the input despite parametric uncertainty or disturbance. The "
        "output of a unity-gain feedback system with uncertain plant models can vary with plant "
        "condition; the output of a robust QFT system varies far less. A unity-gain system, however, "
        "cannot control the tracking response, which is why a prefilter is included."))
    b.append(p(
        "Plant — specifically actuator — uncertainty may come from manufacturing tolerances. Component "
        "A, say, is specified as 10 ± 0.1 mm long; over a large production run its length may lie "
        "anywhere between 9.9 and 10.1 mm, and that tolerance range can be wide enough to produce "
        "noticeable variations in the plant model. Uncertainty may also come from the environment, "
        "specifically the operating conditions: aircraft model parameters, for instance, vary widely "
        "with altitude and airspeed. Finally, the performance of components decays over time, adding "
        "one more element of uncertainty."))
    b.append(p(
        "The QFT design paradigm accounts for plant variation inside the design procedure. It is a "
        "linear technique for designing a linear robust controller for linear or nonlinear systems "
        "[3,6] — here the actuator control system. So long as every QFT design requirement is met, "
        "the output responses are guaranteed to conform to the specification boundaries. The first "
        "step is to establish the upper and lower tracking boundaries; the maximum allowable "
        "disturbance fixes the disturbance boundary, and the phase margin, gain margin or maximum "
        "peak value fixes the stability boundary. Together these boundaries set the performance limit "
        "of the system. The next step is to analyse the system and identify the parameters that cause "
        "noticeable plant variation. The system — often modelled as a single plant transfer function "
        "in other design methods — is now modelled more completely as a <i>set</i> of plant transfer "
        "functions. The variations form a closed region on the Nichols magnitude-and-phase chart "
        "called the template; larger templates mean a higher degree of plant uncertainty, and "
        "templates at different frequencies differ in size and shape."))
    b.append(p(
        "A most important aspect of modelling is the thorough analysis of the bare actuator plant, in "
        "order to find the sources of variation. For an aircraft application the three largest sources "
        "are fluctuations in aerodynamic load on the control surfaces, motor torque, and hydraulic "
        "pump fluid pressure."))

    b.append(h2("99.4 Actuator compensator design"))
    b.append(p(
        "QFT compensators, designed in the frequency domain, are ideally suited to the actuator "
        "control system. The compensator processes its inputs — the commanded actuator displacement "
        "and the measured current actuator position — and generates a commanded signal to, say, the "
        "solenoid valve of a hydraulic actuator or a current for the dc motor of the EHA. To proceed "
        "with the design, the block diagram of Fig. 99.7 is transformed into the standard inner and "
        "outer QFT loop structure of Fig. 99.10 [2,3,6]. For this design problem the external "
        "disturbance d<sub>2</sub>(t) can be ignored, d<sub>2</sub>(t) = 0, while d<sub>1</sub>(t) "
        "models a possible measurement bias. The inner loop controls the angular rate of the motor, "
        "the outer loop the surface deflection. Since tracking in the inner loop matters less — its "
        "function is to reduce the uncertainty level of the outer loop — the inner prefilter can be "
        "set to unity and the tracking requirement is relegated to the prefilter F<sub>Θ</sub> of the "
        "outer loop."))
    b.append(fig(10, F.fig(10), "en"))

    b.append(h2("99.5 Conclusion"))
    b.append(p(
        "The modelling of a hierarchy of hydraulic actuators has been presented, with emphasis on "
        "modern EHAs and carefully developed dynamic models of their subcomponents. A systems approach "
        "to actuator modelling and design is taken, and the feedback structure is highlighted. Because "
        "of the complex feedback interactions at work, proper actuator modelling requires considering "
        "the actuator in the full context of the control system in which it is employed; hence the "
        "aerospace application. At the same time the actuator is viewed not as a component of a "
        "control system but as a control system in its own right. It follows that the simple "
        "mechanical feedback linkages which once fulfilled the role of the controlling element can be "
        "replaced by a more flexible, high-performance, robust, full-blown electronic actuator "
        "compensator."))
    b.append(p(
        "As for electropneumatic instruments and sensors, they are critical elements in systems where "
        "the flow of liquids or gases is controlled, as in the chemical industries. In aerospace, "
        "electropneumatic sensors measure airspeed, altitude, and the angle of attack and sideslip of "
        "the aircraft; these functions are collocated in the air data computer (ADC). Modern sensors "
        "use feedback action for accuracy enhancement, so the design of modern electropneumatic "
        "instruments and sensors is conceptually similar to the design of EHAs. Detailed information "
        "on actuators and sensors may be found in References 4 and 7."))

    b.append(h2("Nomenclature"))
    b.append(_nom("en"))

    b.append(h2("Translator's note"))
    b.append(note(
        "A few printing defects in the source have been repaired here. (1) The differential-pressure "
        "symbol of Eq. 99.10 was lost to a font fault; it is restored as " + PBAR + ", matching "
        "Fig. 99.8. (2) The nomenclature line “J moment of inertia; o, ovin” is corrupted type and "
        "should read “ω, ω<sub>m</sub>”. (3) In the hinge-moment section the letter q denotes both "
        "pitch rate and dynamic pressure; this translation distinguishes the latter as q&#772;. "
        "(4) Eq. 99.24 was printed without the brackets of the state vector; it is set out here in "
        "compact vector form."))

    b.append(h2("References"))
    b.append(refs([
        "O. R. Reynolds, M. Pachter, and C. H. Houpis, “Full envelope flight control system design "
        "using quantitative feedback theory,” <i>AIAA J. Guidance Control Dyn.</i>, 19, 1023–1029, 1996.",
        "K. H. Kang, <i>Electro-Hydrostatic Actuator Controller Design Using Quantitative Feedback "
        "Theory</i>, MS thesis, Graduate School of Engineering, Air Force Institute of Technology, "
        "Wright-Patterson AFB, OH, December 1994, AFIT/GE/ENG/94D-18.",
        "C. H. Houpis, M. Pachter, S. Rasmussen, and R. Sating, <i>Quantitative Feedback Theory for "
        "the Engineer</i>, Wright Laboratory Technical Report, WL-TR-95-3061, Wright Laboratory, "
        "Wright-Patterson AFB, OH, June 1995.",
        "C. W. de Silva, <i>Control Sensors and Actuators</i>, Englewood Cliffs, NJ: Prentice-Hall, 1989.",
        "J. H. Blakelock, <i>Automatic Control of Aircraft and Missiles</i>, New York: John Wiley &amp; "
        "Sons, 1991.",
        "J. J. D’Azzo and C. H. Houpis, <i>Linear Control System Analysis and Design — Conventional "
        "and Modern</i>, 4th ed., New York: McGraw-Hill, 1988.",
        "E. H. J. Pallet and S. Coyle, <i>Automatic Flight Control</i>, Oxford, U.K., Blackwell, 1993.",
    ]))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 99 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 99 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 99 “Thiết bị điện – khí nén và điện – thuỷ lực” của M. Pachter "
            "và C. H. Houpis — mô hình hoá cơ cấu chấp hành thuỷ lực, động cơ, bơm và chất lỏng, "
            "pittông và cánh lái, mômen bản lề, xấp xỉ chu kỳ ngắn, cùng lý thuyết phản hồi định "
            "lượng QFT, với 10 hình và 26 phương trình." if vi
            else
            "Companion to Chapter 99 of the CRC Measurement Handbook — modelling of hydraulic, "
            "electrohydraulic and electrohydrostatic actuators: motor, pump and fluid, piston and "
            "control surface, hinge moments, the short-period approximation and quantitative feedback "
            "theory, with 10 figures and 26 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 99' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 99' % BASE_EN)
    meta = ("Chương 99 · theo Ch99.pdf (CRC Press, 1999) · 10 hình, 26 phương trình" if vi else
            "Chapter 99 · 10 figures, 26 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 99)))
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
