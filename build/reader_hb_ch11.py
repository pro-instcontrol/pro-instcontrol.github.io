# -*- coding: utf-8 -*-
"""Handbook Chapter 11 — Level Measurement (Detlef Brumbi, Krohne Messtechnik).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch11.py
"""
import os

import hb11fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch11-level-measurement"
TITLE_EN = "Level Measurement"
TITLE_VI = "Đo mức"
BYLINE = "Detlef Brumbi · Krohne Messtechnik GmbH"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch10-position-location-altitude"
PREV_VI = "ch10-position-location-altitude"
PREV_T_EN = "Position, Location, Altitude Measurement"
PREV_T_VI = "Đo vị trí, định vị và độ cao"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-11-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Mức được định nghĩa là chiều cao chất đầy của một chất lỏng hay vật liệu rời, ví dụ trong một "
        "bồn chứa hay một hồ chứa. Nói chung người ta đo vị trí mặt thoáng so với một mặt phẳng quy "
        "chiếu, thường là đáy bồn. Nếu mặt sản phẩm không phẳng — khi có bọt, sóng, xoáy, hoặc với vật "
        "liệu rời hạt thô — mức thường được định nghĩa là chiều cao trung bình trên một vùng diện tích "
        "xác định."))
    b.append(p(
        "Có nhiều phương pháp cổ điển và hiện đại để đo mức sản phẩm trong bồn công nghệ và bồn tồn trữ "
        "thuộc các ngành hoá chất, dầu khí, dược phẩm, cấp nước và thực phẩm; trong bồn di động trên xe "
        "và trên tàu; và cả trong những hồ chứa tự nhiên như biển, đập, hồ và đại dương. Chiều cao bồn "
        "điển hình vào khoảng 0,5 m đến 40 m."))
    b.append(p(
        "Có thể phân biệt hai nhiệm vụ khác nhau: (1) đo mức liên tục (chỉ báo mức, LI), và (2) công tắc "
        "mức (LS) — ví dụ để phát hiện một ngưỡng cảnh báo nhằm chống tràn. Hình 11.1 trình bày các "
        "chế độ làm việc chính của phép đo mức. Mọi hệ đo liên tục đều có thể dùng như một công tắc lập "
        "trình được. Nhiều thiết bị đo mức được lắp trên nóc bồn và chủ yếu đo khoảng cách d giữa vị trí "
        "lắp đặt và mặt sản phẩm. Mức L sau đó được tính ra, với chiều cao bồn h được coi là không đổi, "
        "như trên Hình 11.1 và như biểu thức:"))
    b.append(eq("L = h − d", "11.1"))
    b.append(p(
        "Các ví dụ dưới đây chủ yếu mô tả phép đo chất lỏng, nhưng phần lớn phương pháp cũng áp dụng "
        "được cho vật liệu rời. Trọng tâm của chương là những thông tin chung về nguyên lý đo. Phần mô "
        "tả tập trung vào các phương pháp được thực hành phổ biến nhất; những nguyên lý khác được nhắc "
        "đến sơ lược hơn. Bạn đọc muốn thảo luận chi tiết hơn có thể tham khảo [1–5]."))

    # ---- 11.1
    b.append(h2("11.1 Đo bằng các hiệu ứng của khối lượng riêng",
                "Measurements Using the Effects of Density"))
    b.append(p(
        "Mọi phương pháp mô tả trong mục này đều có điểm chung: sản phẩm trong bồn tác động thông qua "
        "khối lượng riêng ρ của nó, hoặc (1) tạo lực nổi lên một vật rắn nhúng trong chất lỏng, hoặc "
        "(2) gây ra một lực do trọng lượng của nó."))

    b.append(h3("Phao chìm", "Displacer"))
    b.append(p(
        "Phao chìm đo lực nổi của một vật rắn nhúng một phần trong chất lỏng. Sự thay đổi trọng lượng "
        "được đo. Hình 11.2 minh hoạ các đại lượng dùng cho những tính toán này. Tiết diện A của vật "
        "được giả thiết không đổi trên suốt chiều dài b của nó. Trọng lực F<sub>G</sub> theo gia tốc "
        "trọng trường g và khối lượng m là:"))
    b.append(eq("F<sub>G</sub> = g m = ρ<sub>A</sub> g A b", "11.2"))
    b.append(p(
        "Lực nổi F<sub>B</sub> tính cho phần chiều dài L<sub>d</sub> bị nhúng, phần còn lại của vật "
        "nằm trong không khí:"))
    b.append(eq("F<sub>B</sub> = ρ<sub>L</sub> g A L<sub>d</sub> + ρ<sub>A</sub> g A (b − "
                "L<sub>d</sub>)", "11.3"))
    b.append(fig(1, F.fig_11_1()))
    b.append(p(
        "Hợp hai phương trình 11.2 và 11.3 cho lực tổng hợp cần đo bằng một phương pháp thích hợp (xem "
        "Chương 23 của sổ tay này):"))
    b.append(eq("F<sub>R</sub> = F<sub>G</sub> − F<sub>B</sub>", "11.4"))
    b.append(p("Kết quả cho mức L<sub>d</sub>, tính tới mép dưới của phao chìm, là:"))
    b.append(eq("L<sub>d</sub> = F<sub>R</sub> / [g A (ρ<sub>A</sub> − ρ<sub>L</sub>)]", "11.5"))
    b.append(fig(2, F.fig_11_2()))
    b.append(p(
        "Khối lượng riêng của vật phải lớn hơn khối lượng riêng của chất lỏng; nếu không, phạm vi làm "
        "việc của phép đo bị giới hạn (chỉ tới khi phao chìm nổi lên mặt chất lỏng). Trong một biến thể "
        "khác, một thiết bị đo kiểu servo kéo phao chìm lên xuống để phát hiện mặt phân cách giữa không "
        "khí và chất lỏng, hoặc giữa hai chất lỏng khác nhau, bằng cách đo sự thay đổi lực nổi. Hình "
        "11.3 trình bày một kết cấu đặc biệt: một quả cầu nhỏ thể tích V gắn vào sợi dây mảnh do động "
        "cơ bước kéo, được cho dao động cộng hưởng. Lực tổng hợp F đo được từ tần số cộng hưởng f của "
        "đoạn dây giữa hai điểm A và B:"))
    b.append(eq("F = 4 ρ<sub>W</sub> A<sub>W</sub> l² f²", "11.6"))
    b.append(p("trong đó l là chiều dài đoạn dây giữa A và B, ρ<sub>W</sub> là khối lượng riêng của "
               "dây, A<sub>W</sub> là tiết diện dây. Khối lượng riêng của môi trường xung quanh "
               "ρ<sub>L</sub> tính được là:"))
    b.append(eq("F = gV (ρ<sub>D</sub> − ρ<sub>L</sub>) ⇔ ρ<sub>L</sub> = ρ<sub>D</sub> − F/(gV)", "11.7"))
    b.append(fig(3, F.fig_11_3()))

    b.append(h3("Phao nổi", "Float"))
    b.append(p(
        "Phao nổi giống phao chìm, nhưng nổi trên mặt chất lỏng nhờ lực đẩy Ác-si-mét. Vì vậy khối "
        "lượng riêng của phao phải nhỏ hơn khối lượng riêng của chất lỏng. Hình 11.4(a) trình bày "
        "nguyên lý làm việc. Vị trí của phao được (1) quan sát bằng mắt, hoặc (2) truyền ra một chỉ "
        "báo bên ngoài hay một bộ truyền góc. Nói chung phao được ghép từ tính với bộ truyền. Hình "
        "11.4(b) trình bày một công tắc mức dùng rơ-le lưỡi gà ghép từ với phao. Một cảm biến tuyến "
        "tính kiểu từ giảo cũng có thể xác định vị trí phao; xem Chương 6, Mục 9 của sổ tay này."))
    b.append(fig(4, F.fig_11_4()))
    b.append(p(
        "Nếu phao rất dẹt, người ta gọi nó là “tấm cảm nhận”. Tấm này được dẫn hướng bằng cơ khí — ví "
        "dụ bằng một vòng điều khiển servo — trên mặt chất lỏng cho tới khi phát hiện lực nâng. Với vật "
        "liệu rời, những phao thẳng đứng có hình dạng đặc biệt tỏ ra hữu ích."))

    b.append(h3("Đo bằng áp suất", "Pressure Gages"))
    b.append(p(
        "Ở đáy bồn có một áp suất thuỷ tĩnh p do trọng lượng sản phẩm gây ra, cộng thêm áp suất khí "
        "quyển p₀:"))
    b.append(eq("p = p₀ + ρ<sub>L</sub> g L ⇔ L = (p − p₀)/(ρ<sub>L</sub> g)", "11.8"))
    b.append(p(
        "Các áp kế ở đáy bồn đo áp suất này. Trong bồn công nghệ có áp suất khí quyển thay đổi, người "
        "ta thực hiện phép đo hiệu áp bằng cách lấy hiệu giữa áp suất ở đáy và áp suất ở nóc bồn, phía "
        "trên chất lỏng. Hình 11.5(a) trình bày một kết cấu như vậy với cảm biến hiệu áp. Về kỹ thuật "
        "đo áp suất, xem Chương 26, Mục 1 của sổ tay này. Vì phép đo bằng áp suất thuỷ tĩnh tỉ lệ với "
        "khối lượng riêng, nếu khối lượng riêng thay đổi thì sẽ phát sinh sai số mức; xem phương trình "
        "11.8. Đo áp suất sơ cấp thực chất là một phép đo khối lượng. Hình 11.5(b) trình bày một bố trí "
        "thẳng đứng với ba cảm biến; các phép đo p₁ và p₂ dùng để bù ảnh hưởng của khối lượng riêng "
        "ρ<sub>L</sub> và tính ra mức:"))
    b.append(eq("ρ<sub>L</sub> = (p₂ − p₁)/(g l) ⇒ L = l (p₂ − p₀)/(p₂ − p₁)", "11.9"))
    b.append(fig(5, F.fig_11_5()))
    b.append(p(
        "Một hệ có kết cấu như vậy thường được gọi là “đo mức bồn bằng thuỷ tĩnh” (HTG). Hình 11.5(c) "
        "trình bày một bố trí khác, gọi là “ống sục bong bóng”, trong đó áp suất đáy được truyền lên "
        "nóc bồn. Cách này thường được dùng khi không thể lắp cảm biến ở đáy bồn. Nó đòi hỏi bồn phải "
        "cân bằng được áp suất nhờ việc sục khí trơ liên tục."))

    b.append(h3("Phương pháp cân", "Balance Method"))
    b.append(p(
        "Ở đây người ta đơn giản đo trọng lượng F của toàn bộ bồn, phụ thuộc vào mức L:"))
    b.append(eq("F = F₀ + ρ<sub>L</sub> g A L", "11.10"))
    b.append(p(
        "trong đó F₀ là trọng lượng của bồn rỗng và A là tiết diện, được giả thiết không đổi trên suốt "
        "chiều cao bồn. Muốn đo trọng lực một cách chính xác, cần tách toàn bộ bồn ra khỏi kết cấu "
        "một cách cơ khí. Với phép đo chính xác, phải tính tới lực nổi của không khí:"))
    b.append(eq("F = F₀ + (ρ<sub>L</sub> − ρ<sub>A</sub>) g A L ⇔ "
                "L = (F − F₀)/[(ρ<sub>L</sub> − ρ<sub>A</sub>) g A]", "11.11"))
    b.append(p(
        "Về kỹ thuật đo trọng lượng, xem Chương 20 của sổ tay này. Phương pháp này có nhược điểm "
        "nghiêm trọng khi bồn không nằm trong nhà. Ở ngoài trời, gió và trọng lượng tuyết, mưa có thể "
        "gây sai số."))

    # ---- 11.2
    b.append(h2("11.2 Đo bằng thời gian bay", "Time-of-Flight Measurements"))
    b.append(p(
        "Một cách đo mức gián tiếp là đánh giá thời gian bay của một sóng truyền qua khoảng không phía "
        "trên chất lỏng hoặc vật liệu rời. Đây trước hết là một phép đo khoảng cách; mức sau đó được "
        "tính ra tương ứng. Nhu cầu ngày càng tăng của công nghiệp đối với các hệ đo mức liên tục không "
        "xâm nhập đã góp phần thúc đẩy mạnh mẽ việc phát triển các công nghệ dùng thời gian bay [7]."))

    b.append(h3("Nguyên lý cơ bản", "Basic Principle"))
    b.append(p(
        "Dù dùng những loại sóng vật lý khác nhau (âm hay điện từ), nguyên lý của mọi phương pháp này "
        "đều như nhau: một tín hiệu đã điều chế được phát đi dưới dạng sóng về phía sản phẩm, bị phản "
        "xạ tại mặt sản phẩm và được một cảm biến thu lại — trong nhiều trường hợp chính là bộ phát "
        "(ví dụ đầu đo áp điện siêu âm hoặc anten radar). Hình 11.6 minh hoạ nguyên lý làm việc. Hệ đo "
        "đánh giá thời gian bay t của tín hiệu:"))
    b.append(eq("t = 2d / v", "11.12"))
    b.append(p(
        "trong đó v là tốc độ truyền của sóng. Người ta có thể tạo một xung không điều chế, một chuỗi "
        "xung có điều chế như trên Hình 11.6(b), hoặc những dạng đặc biệt khác. Bảng 11.1 liệt kê các "
        "tính chất chính của ba loại sóng được ưa dùng cho đo mức bằng thời gian bay."))
    b.append(table(
        ["Nguyên lý", "Tốc độ sóng", "Tần số sóng mang", "Bước sóng", "Thời gian chuỗi xung"],
        [["Siêu âm", "340 m s⁻¹", "50 kHz", "7 mm", "1 ms"],
         ["Radar", "300.000 km s⁻¹", "10 GHz", "3 cm", "1 ns"],
         ["Laser", "300.000 km s⁻¹", "300 THz", "1 µm", "1 ns"]],
        "Bảng 11.1 · Tính chất của các loại sóng dùng cho phép đo thời gian bay."))
    b.append(p(
        "Những khoảng thời gian rất ngắn, chỉ vài nanôgiây, của kỹ thuật đo radar và laser đòi hỏi phải "
        "dùng phép giãn thời gian bằng lấy mẫu (xem Chương 85 của sổ tay này) hoặc những phương pháp "
        "đánh giá đặc biệt (xem dưới đây)."))

    b.append(h3("Siêu âm", "Ultrasonic"))
    b.append(p(
        "Sóng siêu âm là sóng âm dọc có tần số trên 20 kHz. Sóng siêu âm cần một môi trường truyền; với "
        "phép đo mức, môi trường đó là khoảng không phía trên sản phẩm cần đo. Âm truyền trong không "
        "khí với tốc độ khoảng 340 m s⁻¹; nhưng giá trị này phụ thuộc mạnh vào nhiệt độ và thành phần "
        "của khí, và cả vào áp suất của khí (xem Chương 6, Mục 7 của sổ tay này). Trong chân không, "
        "sóng siêu âm không truyền được. Trong thực tế, tỉ số phản xạ tại mặt sản phẩm gần như 100 % "
        "(ví dụ tại chuyển tiếp khí/lỏng hoặc khí/rắn). Đầu đo áp điện (xem Chương 26, Mục 3 của sổ "
        "tay này) được dùng làm bộ phát và bộ thu sóng siêu âm, với một màng ghép nối với khí quyển. "
        "Cảm biến được lắp như trên Hình 11.1(b), dạng tín hiệu như trên Hình 11.6(b). Về nguyên tắc, "
        "cũng có thể đo mức bằng âm thanh nghe được (16 Hz đến 20 kHz) hoặc bằng sóng hạ âm dưới 16 Hz."))
    b.append(p(
        "Một cách làm khác là cho sóng truyền ngay trong chất lỏng, bằng một cảm biến lắp ở đáy bồn. "
        "Khi đó phải biết tốc độ âm trong chất lỏng, có tính tới sự phụ thuộc vào nhiệt độ và loại chất "
        "lỏng. Phương pháp này tương tự máy dò độ sâu bằng tiếng vang trên tàu. Về kỹ thuật đánh giá "
        "thời gian bay của siêu âm, xem Chương 6, Mục 7 của sổ tay này."))

    b.append(h3("Vi ba", "Microwaves"))
    b.append(p(
        "Vi ba nói chung được hiểu là sóng điện từ có tần số trên 2 GHz và bước sóng dưới 15 cm. Vì mục "
        "đích kỹ thuật, người ta dùng tần số vi ba tới tối đa 120 GHz; trong thực tế, dải quanh 10 GHz "
        "(băng X) được ưa chuộng."))
    b.append(fig(6, F.fig_11_6()))
    b.append(p(
        "Phép đo thời gian bay bằng vi ba thường được thực hiện theo nguyên lý radar [8, 9]. Thuật ngữ "
        "“RADAR” nói chung được hiểu là phương pháp dùng sóng điện từ ngắn để phát hiện vật thể ở xa và "
        "xác định vị trí, chuyển động của chúng; đó là từ viết tắt của RAdio Detection And Ranging. "
        "Hình 11.7 trình bày những dạng anten được ưa dùng. Chúng thường được ghép trong một đầu đo "
        "kiểu compact, như trên Hình 11.8. Với hệ đo mức, góc bức xạ nhỏ là điều mong muốn để càng hạn "
        "chế càng tốt những phản xạ gây nhiễu từ thành bồn hay các chi tiết bên trong bồn. Diện tích "
        "khẩu độ càng lớn thì góc bức xạ càng nhỏ và độ lợi anten càng cao. Cân bằng công suất được "
        "cho bởi phương trình radar tổng quát:"))
    b.append(eq("P<sub>R</sub> = P<sub>T</sub> G<sub>T</sub> R G<sub>R</sub> / D²", "11.13"))
    b.append(p(
        "trong đó P<sub>R</sub> là công suất thu, P<sub>T</sub> là công suất phát, G<sub>T</sub> là độ "
        "lợi anten phát, R là hệ số phản xạ của mục tiêu, G<sub>R</sub> là độ lợi anten thu, và "
        "D² là tổn hao truyền tới và từ mặt sản phẩm, do mật độ công suất giảm và do ảnh hưởng của khí "
        "quyển."))
    b.append(p(
        "Hệ số phản xạ R của mặt sản phẩm phụ thuộc vào hằng số điện môi tương đối ε<sub>r</sub> của "
        "chất lỏng hay vật liệu rời:"))
    b.append(eq("R = [(√ε<sub>r</sub> − 1)/(√ε<sub>r</sub> + 1)]²", "11.14"))
    b.append(fig(7, F.fig_11_7()))
    b.append(p(
        "Trong các tình huống đo mức, vùng phản xạ lớn đến mức cắt ngang toàn bộ tiết diện chùm tia; "
        "vì thế D² gần như tỉ lệ với bình phương khoảng cách d². Do đó công suất thu cũng giảm theo "
        "d², như đã dẫn ra trong [8]:"))
    b.append(eq("P<sub>R</sub> ∝ 1/d²", "11.15"))
    b.append(fig(8, F.fig_11_8()))
    b.append(p(
        "Điều này không còn đúng nếu sóng truyền trong một ống dẫn sóng điện từ, ví dụ một ống thẳng "
        "đứng cắm xuống chất lỏng, gọi là giếng tĩnh. Khi đó sóng truyền gần như không tổn hao."))
    b.append(p(
        "Một phương pháp khác dùng sóng điện từ là cho sóng truyền trong một sợi cáp. Hình 11.9(a) "
        "minh hoạ cách làm việc với một sợi cáp thả xuống chất lỏng hoặc vật liệu rời. Ở mỗi vị trí mà "
        "hằng số điện môi của môi trường xung quanh thay đổi, một phần sóng bị phản xạ. Phương pháp này "
        "cũng dùng được cho phép đo mặt phân cách. Hình 11.9 trình bày tín hiệu trong một ứng dụng với "
        "sản phẩm hai pha. Phương pháp này được gọi là “phản xạ miền thời gian” (TDR)."))

    b.append(h3("Laser và ánh sáng", "Laser/Light"))
    b.append(p(
        "Laser và diode phát quang tạo ra sóng điện từ có bước sóng rất ngắn (dưới 2 µm), cũng dùng được "
        "cho phép đo thời gian bay, tương tự các phương pháp vi ba đã mô tả. Tín hiệu laser được ưa "
        "dùng là (1) những xung ngắn dưới 1 ns, hoặc (2) laser có cường độ điều biên với tần số vài "
        "mêgahertz. Muốn biết thêm về nguyên lý làm việc của laser và các phương pháp giao thoa, xem "
        "Chương 6, Mục 5 của sổ tay này."))
    b.append(fig(9, F.fig_11_9()))
    b.append(p(
        "Hệ laser rất chính xác, có thể đạt độ chính xác tốt hơn 1 mm. Vì chùm laser rất hẹp, hệ đo "
        "mức kiểu này có thể lắp đặt mà không chịu ảnh hưởng của các chi tiết bên trong bồn. Một số "
        "nhược điểm thực tế của đo mức bằng laser là: (1) nó hoạt động như mắt người nhìn mặt sản phẩm, "
        "nên sẽ hỏng nếu có bụi, khói…; (2) nó nhạy với bẩn trên các cảm biến quang; và (3) thiết bị "
        "đắt tiền."))

    b.append(h3("Các phương pháp đánh giá thường dùng", "Commonly Used Evaluation Methods"))
    b.append(p(
        "Nhờ những ưu điểm lớn của phép đo thời gian bay không tiếp xúc, trong vài năm gần đây một số "
        "phương pháp điển hình đã được đánh giá cho việc đo mức, chủ yếu trong kỹ thuật radar [8]."))

    b.append(h3("Radar sóng liên tục điều tần", "Frequency-Modulated Continuous Wave Radar"))
    b.append(p(
        "Vì thời gian bay trong những ứng dụng đo mức điển hình rất ngắn (độ phân giải 1 mm đòi hỏi độ "
        "phân giải thời gian 7 ps), rất khó đánh giá thông tin trực tiếp trong miền thời gian. Bằng "
        "cách điều chế tín hiệu vi ba, độ trễ thời gian được chuyển sang miền tần số, thu được những "
        "tín hiệu tần số thấp. Về thông tin chung của phép điều chế, xem Chương 81 của sổ tay này."))
    b.append(p(
        "Vì thế radar sóng liên tục điều tần (FMCW) đã trở thành kỹ thuật chủ đạo. Radar FMCW dùng một "
        "tín hiệu vi ba được điều tần tuyến tính; tần số phát tăng tuyến tính trong một khoảng thời "
        "gian T. Hiệu tần số trong khoảng ấy được gọi là độ quét tần số F."))
    b.append(p(
        "Hình 11.10 trình bày nguyên lý radar FMCW. Do độ trễ thời gian trong quá trình truyền sóng, "
        "tần số phát đã thay đổi, nên hiệu giữa tần số phát tức thời và tần số thu là một tín hiệu tần "
        "số thấp. Tần số f của tín hiệu đó (thường tới vài kilôhertz) tỉ lệ với khoảng cách tới vật "
        "phản xạ d (xem Hình 11.6); như vậy ở phương pháp này, độ trễ t được chuyển thành tần số f:"))
    b.append(eq("f = (F/T) t = (F/T)(2d/c) ⇔ d = f c T / (2F)", "11.16"))
    b.append(p(
        "Trong phương trình 11.16, c là tốc độ ánh sáng và F/T là tốc độ quét; xem Hình 11.10. Hình "
        "11.11 trình bày sơ đồ khối mạch cơ bản của một hệ radar FMCW. Vì tần số tín hiệu thu được "
        "thấp, việc xử lý tín hiệu tiếp theo đơn giản về mặt kỹ thuật và rất chính xác. Thông thường "
        "việc đánh giá được thực hiện bằng xử lý tín hiệu số. Muốn biết thêm về kỹ thuật xử lý tín "
        "hiệu bằng phân tích phổ, xem Chương 83 của sổ tay này."))
    b.append(fig(10, F.fig_11_10()))
    b.append(fig(11, F.fig_11_11()))

    b.append(h3("Thời gian bay xuyên qua sản phẩm", "Time-of-Flight Through Product"))
    b.append(p(
        "Một cách khác là đo thời gian truyền của sóng xuyên qua một chất lỏng hấp thụ yếu hoặc vật "
        "liệu rời có hằng số điện môi ε<sub>r</sub> thấp, thay vì đo thời gian truyền trong không khí. "
        "Trong trường hợp phản xạ từ mặt phân cách giữa không khí và mặt trên của sản phẩm yếu, một "
        "phần tín hiệu đi xuyên qua chất lỏng và bị phản xạ lần thứ hai tại đáy bồn hoặc tại mặt phân "
        "cách giữa hai chất lỏng (ví dụ dầu trên nước)."))
    b.append(p("Hình 11.12 minh hoạ kỹ thuật này. Việc đánh giá được thực hiện theo bốn bước sau:"))
    b.append('<ol class="num-list">'
             '<li>Trong khi vi ba truyền trong khoảng không trên mặt sản phẩm có chiều cao d với tốc '
             'độ ánh sáng c, vi ba truyền trong môi trường (hằng số điện môi tương đối '
             'ε<sub>r</sub>, chiều cao L) với tốc độ chậm hơn v.</li>'
             '<li>Vì thế phản xạ r₂ từ đáy bồn hiện ra bị dịch xuống dưới, và chiều cao bồn biểu '
             'kiến h<sub>v</sub> lớn hơn chiều cao thực h.</li>'
             '<li>Thời gian truyền trong môi trường là t₁ = L/v, trong khi với cùng khoảng cách ấy '
             'trong bồn rỗng thì là t₀ = L/c. Do đó tỉ số giữa “bề dày lớp” biểu kiến '
             '(h<sub>v</sub> − d) và chiều cao chất đầy thực (h − d) tương ứng với tỉ số tốc độ '
             'truyền sóng:</li>'
             '</ol>')
    b.append(eq("(h<sub>v</sub> − d)/(h − d) = c/v = √ε<sub>r</sub>", "11.17"))
    b.append(p("4. Khi biết ε<sub>r</sub>, h và h<sub>v</sub>, khoảng cách d và từ đó mức L được tính "
               "chính xác:"))
    b.append(eq("L = h − d = (h<sub>v</sub> − h)/(√ε<sub>r</sub> − 1)", "11.18"))
    b.append(fig(12, F.fig_11_12()))
    b.append(p(
        "Bằng phương pháp này người ta đạt được một phép đo mức trực tiếp — không phải phép đo khoảng "
        "cách. Nó thậm chí dùng được khi tín hiệu r₁ từ mặt sản phẩm không còn đo được nữa. Việc đánh "
        "giá tín hiệu phản xạ từ đáy bồn được gọi là “dò đáy bồn”, và được dùng trong hệ radar đo mức "
        "của Krohne trên Hình 11.8."))

    # ---- 11.3
    b.append(h2("11.3 Đo mức bằng cách phát hiện các tính chất vật lý",
                "Level Measurements by Detecting Physical Properties"))
    b.append(p(
        "Để đo mức, người ta có thể phát hiện những tham số vật lý khác nhau rõ rệt giữa khoảng không "
        "và sản phẩm; ví dụ độ dẫn điện, độ nhớt, hoặc độ suy giảm của một loại bức xạ nào đó. Có thể "
        "dùng hai kiểu: (1) đo liên tục bằng một cảm biến tích phân, hoặc (2) đóng cắt bằng một phép "
        "đo điểm khi cảm biến tiếp xúc với sản phẩm."))

    b.append(h3("Tính chất điện", "Electrical Properties"))
    b.append(p(
        "Cảm biến phải tiếp xúc trực tiếp hoặc gián tiếp với sản phẩm để phát hiện tính chất điện của "
        "nó. Với phép đo liên tục, chỉ một phần của cảm biến xâm nhập cần tiếp xúc với sản phẩm để phát "
        "hiện sự khác biệt về hằng số điện môi hoặc độ dẫn điện."))

    b.append(h3("Điện dung", "Capacitive"))
    b.append(p(
        "Trong phần lớn ứng dụng, một điện cực thanh được bố trí thẳng đứng trong bồn. Điện cực có thể "
        "(1) không có cách điện nếu chất lỏng không dẫn điện, hoặc (2) có cách điện. Thành bồn kim "
        "loại đóng vai trò điện cực quy chiếu. Kết quả phụ thuộc vào hằng số điện môi ε₂ của sản phẩm. "
        "Hình 11.13(a) trình bày một điện cực lắp đồng tâm trong một bồn hình trụ. Với cấu hình đối "
        "xứng tròn xoay như vậy, điện dung C của một điện cực có cách điện thay đổi theo mức L như "
        "sau:"))
    b.append(eq("C = 2π ε₀ L / [(1/ε₁) ln(d₂/d₁) + (1/ε₂) ln(d₃/d₂)]", "11.19"))
    b.append(p(
        "trong đó ε₀ là hằng số điện môi của chân không (8,85 × 10⁻¹² As V⁻¹m⁻¹); ε₁ và ε₂ lần lượt là "
        "hằng số điện môi tương đối của vật liệu cách điện và của chất lỏng. Nếu bản thân chất lỏng dẫn "
        "điện mạnh, phương trình 11.19 rút gọn thành:"))
    b.append(eq("C = 2π ε₀ ε₁ L / ln(d₂/d₁) ⇔ L = C ln(d₂/d₁) / (2π ε₀ ε₁)", "11.20"))
    b.append(fig(13, F.fig_11_13()))
    b.append(p("Nếu điện cực không có cách điện, phương trình sau đây đúng:"))
    b.append(eq("C = 2π ε₀ ε₂ L / ln(d₃/d₁) ⇔ L = C ln(d₃/d₁) / (2π ε₀ ε₂)", "11.21"))
    b.append(p(
        "Khi được bố trí nằm ngang, như trên Hình 11.13(b), một cảm biến điện dung có thể làm công tắc "
        "mức. Về phép đo điện của điện dung, xem Chương 6.3 của sổ tay này. Để đo chính xác hơn với "
        "chất lỏng dẫn điện, phương pháp đo trở kháng phức tỏ ra hữu ích."))

    b.append(h3("Độ dẫn điện", "Conductive"))
    b.append(p(
        "Điện trở của chất lỏng giữa hai điện cực được đo với (1) một đường dây dạng dải có hai điện "
        "cực song song tương tự Hình 11.9(a), hoặc (2) một điện cực thanh với thành bồn kim loại làm "
        "điện cực quy chiếu, tương tự Hình 11.13(a) nhưng không có lớp cách điện."))

    b.append(h3("Suy giảm bức xạ", "Radiation Attenuation"))
    b.append(p(
        "Mọi bức xạ (ví dụ tia gamma, sóng siêu âm, sóng điện từ) đều bị suy giảm ở một mức nào đó "
        "trong mọi môi trường. Nói chung, độ suy giảm trong chất lỏng hay vật liệu rời cao hơn trong "
        "chất khí. Hiệu ứng này được dùng để đo mức hoặc các ngưỡng mức mà không cần cảm biến tiếp xúc "
        "trực tiếp."))

    b.append(h3("Phóng xạ", "Radiometric"))
    b.append(p(
        "Cường độ I của tia gamma bị chất lỏng làm suy giảm theo hệ số tắt dần α của nó:"))
    b.append(eq("I = I₀ exp(−α d)", "11.22"))
    b.append(p(
        "Nguồn có thể là vật liệu phóng xạ Co-60 hoặc Cs-137, với chu kỳ bán rã lần lượt là 5,23 năm "
        "và 29,9 năm. Bộ phát và bộ thu có thể có dạng (1) một nguồn điểm phát tia theo mọi hướng, "
        "(2) một thanh phát tia theo hướng vuông góc dọc theo một đường, hoặc (3) một dãy gồm nhiều "
        "nguồn điểm xếp thành hàng. Mọi tổ hợp giữa bộ phát điểm/thanh/dãy với bộ thu điểm/thanh/dãy "
        "đều có thể. Hình 11.14 trình bày hai cấu hình khác nhau. Phải tuân thủ các quy định về bảo vệ "
        "bức xạ. Một đồng hồ thời gian thực trong hệ phải bù sự giảm cường độ (suất liều) I theo thời "
        "gian t, dựa trên chu kỳ bán rã T<sub>H</sub> của vật liệu được dùng:"))
    b.append(eq("I = I₀ 2<sup>−t/T<sub>H</sub></sup>", "11.23"))
    b.append(p(
        "Muốn biết thêm về các phương pháp phát hiện bức xạ, xem Chương 66 của sổ tay này. Nhựa nhấp "
        "nháy và ống đếm được ưa dùng cho việc đo mức kiểu phóng xạ. Đặc tuyến mức–cường độ là phi "
        "tuyến, nên thiết bị cần được hiệu chuẩn tại chỗ. Mengelkamp [10] mô tả kỹ thuật phóng xạ chi "
        "tiết hơn."))
    b.append(fig(14, F.fig_11_14()))

    b.append(h3("Công tắc siêu âm", "Ultrasonic Switch"))
    b.append(p(
        "Một đường truyền siêu âm ngắn có thể dùng để phát hiện những sản phẩm làm tắt dần sóng sonar. "
        "Ví dụ, phương pháp này áp dụng được để phát hiện bùn nhão hoặc xác định mặt phân cách giữa hai "
        "chất lỏng khác nhau. Khi ghép với một hệ servo, có thể đo biên dạng độ suy giảm siêu âm theo "
        "chiều đứng. Một ứng dụng khác dùng cảm biến không tiếp xúc lắp ở mặt ngoài thành bình; nó đo "
        "trở kháng âm qua thành bình, đại lượng thay đổi tuỳ theo có chất lỏng hay chất khí ở phía sau "
        "thành."))

    b.append(h3("Công tắc vi ba", "Microwave Switch"))
    b.append(p(
        "Chất lỏng và chất rắn trong nhiều trường hợp làm tắt dần vi ba, đôi khi hấp thụ hoàn toàn. Một "
        "nguồn vi ba không điều chế đơn giản cùng một bộ thu đi kèm là đủ để đóng cắt mức."))

    b.append(h3("Hàng rào quang điện", "Photoelectric Barrier"))
    b.append(p(
        "Một hàng rào quang điện có thể làm công tắc mức cho những chất lỏng không trong suốt, cũng "
        "như phần lớn chất rắn. Nhưng trong bồn kín không trong suốt, việc ghép các phần tử quang điện "
        "vào thành bồn trong phần lớn trường hợp là không thể."))

    b.append(h3("Nhiệt và cơ", "Thermal and Mechanical"))
    b.append(p(
        "Với một số ứng dụng đặc biệt, cảm biến mức dựa vào tính chất toả nhiệt và độ nhớt khác nhau "
        "của các môi trường."))

    b.append(h3("Nhiệt", "Thermal"))
    b.append(p(
        "Một điện trở tự gia nhiệt có hệ số nhiệt độ cao được nhúng vào chất lỏng. Sự toả nhiệt làm "
        "nhiệt độ giảm đi đôi chút ở vùng mà chất lỏng phủ lên cảm biến. Vì thế sự thay đổi điện trở "
        "gần như tuyến tính với mức. Phương pháp này thường được dùng trong ứng dụng ô tô. Trong một số "
        "ứng dụng với chất lỏng đã được gia nhiệt (ví dụ nồi phản ứng hoá học), một cảm biến nhiệt độ "
        "đơn giản có thể làm công tắc mức bằng cách phát tín hiệu khi chất lỏng tiếp xúc và làm nóng "
        "cảm biến."))

    b.append(h3("Độ nhớt", "Viscosity"))
    b.append(p(
        "Hiệu ứng của độ nhớt — vốn lớn hơn nhiều ở chất lỏng so với chất khí — làm tắt dần chuyển động "
        "của một vật. Những cảm biến mức này đo mức độ tắt dần của một âm thoa khi nhúng vào chất lỏng. "
        "Thông thường nó chỉ được dùng như một công tắc mức điểm. Hình 11.15 trình bày một “âm thoa” "
        "như vậy, được gọi theo hình dạng điển hình với hai hoặc ba cánh rung. Mạch điện tử tích hợp "
        "đánh giá tổn hao công suất hoặc độ dịch tần của hệ cộng hưởng cơ. Với vật liệu rời, một cảm "
        "biến có cánh quay sẽ dừng lại khi tiếp xúc với sản phẩm là hữu ích."))
    b.append(fig(15, F.fig_11_15()))

    # ---- 11.4
    b.append(h2("11.4 Thiết bị", "Instruments"))
    b.append(p(
        "Bảng 11.2 liệt kê những kỹ thuật đo mức thông dụng nhất cùng phạm vi ứng dụng, độ chính xác "
        "đạt được và giá trung bình tương ứng. Giá nêu ra là cho những ứng dụng công nghiệp điển hình "
        "và có thể dao động rất rộng, tuỳ thuộc vật liệu chế tạo, phạm vi đo, yêu cầu về độ chính xác, "
        "yêu cầu về chứng nhận… Bảng 11.3 cung cấp thông tin liên hệ của các nhà chế tạo thiết bị đo "
        "mức. Phần lớn những công ty này chế tạo nhiều loại thiết bị, dùng các công nghệ khác nhau nêu "
        "trong Bảng 11.2. Danh sách này không đầy đủ; ngoài ra còn có những công ty nhỏ hơn cung cấp "
        "thiết bị cho những phép đo mức chuyên dụng."))
    b.append(table(
        ["Kỹ thuật", "Phạm vi ứng dụng", "Độ chính xác đạt được", "Giá TB"],
        [["Phao chìm / phao nổi", "Liên tục, chất lỏng", "1 mm", "2.000 $"],
         ["Công tắc phao", "Chất lỏng", "10 mm", "500 $"],
         ["Áp suất", "Liên tục, chất lỏng", "10 mm", "2.000 $"],
         ["Siêu âm", "Liên tục, lỏng và rắn", "5 mm", "2.500 $"],
         ["Radar", "Liên tục, lỏng và rắn", "1 mm", "3.000 $"],
         ["TDR", "Liên tục, lỏng và rắn", "3 mm", "2.500 $"],
         ["Laser", "Liên tục, lỏng và rắn", "0,1 mm", "10.000 $"],
         ["Phóng xạ", "Liên tục, lỏng và rắn", "10 mm", "5.000 $"],
         ["Điện dung", "Công tắc, chất lỏng", "10 mm", "500 $"],
         ["Độ nhớt", "Công tắc, chất lỏng", "10 mm", "500 $"]],
        "Bảng 11.2 · Các kỹ thuật đo mức ưu tiên và giá cho ứng dụng công nghiệp."))
    b.append(table(
        ["Nhà chế tạo", "Địa chỉ", "Điện thoại"],
        [["Berthold Systems, Inc.", "101 Corporation Drive, Aliquippa, PA 15001", "(508) 378-1900"],
         ["Bindicator", "1915 Dove Street, Port Huron, MI 48061", "(810) 987-2700"],
         ["Danfoss Instrumark International", "485 Sinclair Frontage Road, Milpitas, CA 95035",
          "(408) 262-0717"],
         ["Drexelbrook Engineering Company", "205 Keith Valley Road, Horsham, PA 19044",
          "(215) 674-1234"],
         ["Eckardt", "10707 Addington Street, Houston, TX 77043", "(713) 722-286"],
         ["Endress &amp; Hauser Instruments", "2350 Endress Place, Greenwood, IN 46143",
          "(317) 535-7138"],
         ["Enraf, Inc.", "500 Century Plaza Drive, Suite 120, Houston, TX 77073", "(713) 443-4291"],
         ["The Foxboro Company", "38 Neponset Avenue, Foxboro, MA 02035", "(508) 543-8750"],
         ["Krohne America Inc.", "7 Dearborn Road, Peabody, MA 01960", "(508) 535-1720"],
         ["MTS Systems Corporation, Sensors Division", "3001 Sheldon Drive, Cary, NC 27513",
          "(919) 677-0100"],
         ["Milltronics", "709 Stadium Drive, Arlington, TX 76011", "(800) 569-2130"],
         ["Rosemount, Inc., Measurement Division", "8200 Market Boulevard, Chanhassen, MN 55317",
          "(612) 949-7000"],
         ["Saab Tank Control", "10235 West Little York, Suite 258, Houston, TX 7740",
          "(713) 849-2092"],
         ["TN Technologies, Inc.", "2555 North Interstate 35, P.O. Box 800, Round Rock, TX 78680",
          "(512) 388-9100"],
         ["Vega HiTech Technologies, Inc.", "P.O. Box 535, Newtown, PA 18940", "(215) 968-1795"],
         ["Whessoe Varec, Inc.", "10800 Valley View Street, Cypress, CA 90630", "(714) 761-1300"],
         ["Yokogawa Corporation of America", "2 Dart Road, Newnan, GA 30265", "(404) 253-7000"]],
        "Bảng 11.3 · Các công ty chế tạo thiết bị đo mức."))

    # ---- references
    b.append(h2("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>D. M. Considine, <i>Process Instruments and Control Handbook</i>, 2nd ed., New York: '
             'McGraw-Hill, 1974.</li>'
             '<li>E. B. Jones, <i>Instrument Technology</i>, Vol. 1, <i>Measurement of Pressure, Level '
             'and Temperature</i>, London: Butterworth &amp; Co., 1974.</li>'
             '<li>Verein Deutscher Ingenieure, Verband Deutscher Elektrotechniker (VDI/VDE), '
             '<i>Füllstandmessung von Flüssigkeiten und Feststoffen</i> (Level Measurement of Liquids '
             'and Solids), VDI/VDE 3519, Part 1, Berlin: Beuth, 1984.</li>'
             '<li>VDI/VDE, <i>Füllstandmessung von Flüssigkeiten und Feststoffen</i>, VDI/VDE 3519, '
             'Part 2, Berlin: Beuth, 1984.</li>'
             '<li>K. W. Bonfig (ed.), <i>Technische Füllstandsmessung und Grenzstandkontrolle</i>, '
             'Ehningen: Expert, 1990.</li>'
             '<li>Krohne Messtechnik, <i>Technical Data Sheets of Level Measurement Products</i>, '
             'Duisburg: Krohne, 1996.</li>'
             '<li>K. Blundy, “Radar systems — setting a practical approach”, <i>Control &amp; '
             'Instrumentation</i>, July 1996.</li>'
             '<li>D. Brumbi, <i>Fundamentals of Radar Techniques for Level Gauging</i>, Duisburg: '
             'Krohne, 1995.</li>'
             '<li>D. Brumbi, “Measuring process and storage tank level with radar technology”, '
             '<i>Int. Radar Conf. IEEE</i>, 256–260, 1995.</li>'
             '<li>H. Mengelkamp, radiometric level techniques (cited in the source chapter).</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 10</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 11. It carries all fifteen "
        "figures redrawn as vectors, the two tables of instruments and prices, and the argument the "
        "chapter makes about which physical effect each family of instruments actually exploits. The "
        "prose of the translation — the displacer algebra, the radar equation, the FMCW ramp, the "
        "capacitance of a concentric probe — is not repeated here."))

    b.append(h2("Level is a distance, measured backwards"))
    b.append(p(
        "Brumbi opens with a definition that looks trivial and is not: level is the filling height, and "
        "almost every instrument on the market measures something else and converts. A radar on the roof "
        "measures d, the distance from the flange to the product, and the level is L = h − d with the "
        "tank height h held constant. Everything that goes wrong with level measurement in practice "
        "goes wrong in that subtraction: h is not constant when the roof sags, d is not the distance to "
        "the surface when the beam reflects off a agitator blade, and the surface is not a plane when "
        "the product foams."))
    b.append(fig(1, F.fig_11_1(), "en"))
    b.append(p(
        "The figure is worth reading as a taxonomy rather than a sketch. Four mounting positions, and "
        "each one implies a different error budget. (a) contacts the product, so it inherits its "
        "temperature, its corrosivity and its coating behaviour. (b) touches nothing, so it inherits "
        "only the vapour space — but it also inherits everything that floats in that space. (c) is "
        "intrusive, which is the only way to measure a dielectric property. (d) is a switch, and a "
        "switch is not a cheap level transmitter: it answers a different question, and §11.3 is "
        "entirely about devices that answer that different question."))

    b.append(h2("Density first: the buoyancy family"))
    b.append(p(
        "§11.1 is the oldest technology in the chapter and still the one that survives in the nastiest "
        "service, because a displacer has no window, no antenna and no electronics in contact with the "
        "process. The algebra is three lines: weight F_G = ρ_A g A b, buoyancy F_B on the dipped length "
        "plus the dry remainder, and the resultant F_R = F_G − F_B, which collapses to "
        "F_R = g A L_d (ρ_A − ρ_L). The instrument measures F_R and solves for L_d."))
    b.append(fig(2, F.fig_11_2(), "en"))
    b.append(p(
        "Two consequences follow from that last expression and neither is obvious from the text alone. "
        "First, the body must be denser than the liquid, or the instrument floats and the range ends "
        "early — which is why displacers are long, thin and heavy rather than short and fat. Second, "
        "the sensitivity dF_R/dL is g A (ρ_A − ρ_L), so a displacer sized for a light hydrocarbon loses "
        "most of its span when the same tank is filled with water. The device is not mis-calibrated; it "
        "is answering a question whose scale factor changed."))
    b.append(fig(3, F.fig_11_3(), "en"))
    b.append(p(
        "Figure 11.3 is the clever variant. Instead of measuring a force with a strain gauge, it hangs "
        "a small ball on a wire, drives the wire at resonance and reads the frequency. For a stretched "
        "string f = (1/2l)√(F/ρ_W A_W), so F = 4 ρ_W A_W l² f² — a force-to-frequency conversion with "
        "no analogue electronics in the loop and a resolution set by the clock, not by the amplifier. "
        "The same wire can then be stepped up and down to find interfaces, which makes one instrument "
        "do level, interface and density."))
    b.append(fig(4, F.fig_11_4(), "en"))
    b.append(p(
        "Floats are the mirror image: the body is lighter than the liquid, so it rides the surface and "
        "the output is a position rather than a force. The two drawings in Figure 11.4 are the two ways "
        "that position is read out — mechanically, through a cable over a pulley to a counterweight, or "
        "magnetically, through the wall of a guide tube to a reed contact. The reed version is the one "
        "that survives: no packing gland, no cable to stretch, and stacking several reeds in the tube "
        "gives a coarse but genuinely continuous indication."))
    b.append(fig(5, F.fig_11_5(), "en"))
    b.append(p(
        "Hydrostatic measurement is the third member of the family and the one with the most instructive "
        "failure mode. p = p₀ + ρ_L g L is exact; the problem is that ρ_L is not a constant. §11.1 "
        "offers three answers, and the three panels of Figure 11.5 are those three answers. (a) vents "
        "the low side of a differential cell to the roof, which removes barometric pressure but not "
        "density. (b) puts a second sensor a fixed distance up the tank, so that ρ_L = (p₂ − p₁)/g l is "
        "measured rather than assumed, and the level follows from the ratio of two pressure differences "
        "— hydrostatic tank gaging, the standard method for custody transfer. (c) solves a different "
        "problem: when the bottom of the tank is inaccessible, a bubble tube purges inert gas down a "
        "pipe and reads the back pressure at the inlet, so the sensor sits on the roof and only the "
        "pipe touches the product."))
    b.append(p(
        "The balance method closes §11.1 and is included mainly to be dismissed. Weighing the whole "
        "tank gives L = (F − F₀)/[(ρ_L − ρ_A) g A] exactly, and gives nonsense outdoors, where wind and "
        "the weight of snow and rain load the load cells. It is the right method for a small day tank "
        "indoors and the wrong one for a field storage tank, and the chapter says so in one sentence."))

    b.append(h2("Time of flight: one equation, three carriers"))
    b.append(p(
        "§11.2 is the modern half of the chapter and it rests on t = 2d/v. Everything else is a choice "
        "of carrier — 340 m/s of sound, 3×10⁸ m/s of light — and every consequence follows from that "
        "ratio. Table 11.1 is the whole argument in three rows."))
    b.append(table(
        ["Principle", "Wave velocity", "Carrier frequency", "Wavelength", "Burst time"],
        [["Ultrasonic", "340 m s⁻¹", "50 kHz", "7 mm", "1 ms"],
         ["Radar", "300,000 km s⁻¹", "10 GHz", "3 cm", "1 ns"],
         ["Laser", "300,000 km s⁻¹", "300 THz", "1 µm", "1 ns"]],
        "Table 11.1 · Properties of the wave types used for time-of-flight level measurement."))
    b.append(p(
        "Read the last column against the first. A 1 mm resolution needs a 6 µs round trip in air and a "
        "7 ps round trip in a radar beam — six orders of magnitude apart. That single number explains "
        "why ultrasonic instruments count pulses with a microcontroller and radar instruments need "
        "either equivalent-time sampling or, more usually, a modulation scheme that moves the "
        "measurement into the frequency domain."))
    b.append(fig(6, F.fig_11_6(), "en"))
    b.append(p(
        "Figure 11.6 is the geometry and the timing that every later figure reuses. Note what the "
        "drawing makes explicit and the text only implies: the beam is a cone, not a line, so the echo "
        "comes back from an area rather than a point. That area is why a small radiation angle matters "
        "— a wide cone sees the tank wall, the agitator and the filling stream as well as the surface."))
    b.append(fig(7, F.fig_11_7(), "en"))
    b.append(p(
        "The three antennas in Figure 11.7 are three answers to the same requirement: put as much "
        "aperture as possible into a flange-sized hole. The horn is the cheap answer and the one that "
        "collects condensation. The dielectric rod is the answer for small tanks and corrosive vapours, "
        "because the radiating element is inert plastic rather than a metal cavity. The Cassegrain is "
        "the answer when the beam must be narrow enough to miss an agitator — a subreflector lets the "
        "effective aperture exceed the flange diameter, at the cost of a surface that must be kept "
        "clean."))
    b.append(fig(8, F.fig_11_8(), "en"))
    b.append(p(
        "Figure 11.8 is the packaging: microwave circuit, signal processing, microprocessor, display, "
        "supply and output, all above the flange in one housing. It is worth noting how much of that "
        "list is not microwave engineering. The RF chain is a handful of components; the rest is the "
        "same digital hardware that any transmitter carries, which is why radar level instruments "
        "became affordable in the 1990s rather than the 1970s."))
    b.append(p(
        "The radar equation P_R = P_T G_T R G_R / D² is then simplified twice in the text, and both "
        "simplifications matter. First, R depends only on the permittivity of the product, "
        "R = [(√ε_r − 1)/(√ε_r + 1)]², so a product with ε_r ≈ 2 returns about 3 % of the incident "
        "power while a product with ε_r ≈ 80 returns about 64 %. That is the entire explanation for why "
        "radar works beautifully on water and badly on dry cement. Second, because the reflecting area "
        "fills the beam, D² scales as d², so P_R falls as 1/d² rather than 1/d⁴ — the reason a tank "
        "radar reaches 40 m with a fraction of a milliwatt."))
    b.append(fig(9, F.fig_11_9(), "en"))
    b.append(p(
        "Figure 11.9 is the guided-wave case, and it is the clearest drawing in the chapter. A pulse is "
        "launched down two wires; every change in permittivity reflects part of it. The surface gives "
        "the first echo, the interface between two liquids the second, the end of the line the third. "
        "Because the end of the line is a known distance away, it serves as the reference that "
        "calibrates the velocity — which is how TDR keeps its accuracy when the vapour above the "
        "product changes composition."))
    b.append(fig(10, F.fig_11_10(), "en"))
    b.append(fig(11, F.fig_11_11(), "en"))
    b.append(p(
        "Figures 11.10 and 11.11 are the FMCW pair, and they are the heart of the chapter. The trick is "
        "to stop trying to time a 7 ps round trip and instead sweep the transmitter linearly in "
        "frequency. A delayed echo then arrives at a frequency that is offset from the current "
        "transmit frequency by Δf = (F/T)·t, a few kilohertz — easily counted. The distance follows "
        "directly: d = f c T / (2F). Figure 11.11 shows why the block diagram is more than a mixer: the "
        "VCO has to be linear, so its instantaneous frequency is measured against a DRO and the "
        "microprocessor closes a loop on the sweep. Everything expensive in an FMCW radar is in that "
        "linearity, not in the antenna."))
    b.append(fig(12, F.fig_11_12(), "en"))
    b.append(p(
        "Figure 11.12 is the odd one out and the most elegant idea in the chapter. If the reflection "
        "from the surface is weak, let the wave go through the product and reflect off the bottom "
        "instead. The echo comes back late, because the wave travels at c/√ε_r in the liquid, so the "
        "bottom appears to be further away than it is: (h_v − d)/(h − d) = √ε_r, and therefore "
        "L = (h_v − h)/(√ε_r − 1). The measurement is now a direct level measurement rather than a "
        "distance measurement, and it still works when the surface echo is unusable. Krohne sell this "
        "as “tank bottom tracing”."))

    b.append(h2("Physical properties: the switch business"))
    b.append(p(
        "§11.3 changes the question. Instead of measuring a height continuously, it asks whether the "
        "product is present at one point, and it answers by detecting a property that differs sharply "
        "between gas and liquid: permittivity, conductivity, radiation attenuation, thermal "
        "conductivity, viscosity. Most of these devices are switches, and a switch is a legitimate "
        "instrument — an overfill protection loop needs a switch, not a transmitter."))
    b.append(fig(13, F.fig_11_13(), "en"))
    b.append(p(
        "The capacitive probe is the one worth doing the algebra for. For a concentric geometry the "
        "capacitance is a sum of two cylindrical condensers in series — the insulation and the product "
        "— which is Equation 11.19. The two limiting cases are the useful ones: a conductive product "
        "shorts out the second term and leaves C proportional to L through the insulation alone "
        "(11.20), while a bare electrode in a conductive liquid is really a conductivity cell, which is "
        "why 11.21 has ε₂ rather than ε₁ in it."))
    b.append(fig(14, F.fig_11_14(), "en"))
    b.append(p(
        "Radiometric gaging is the only method in the chapter that works through a blind wall, and "
        "Figure 11.14 shows the two configurations that matter: a point source with a rod detector, "
        "which gives a continuous profile, and a source array with a point detector, which gives a "
        "cheaper average. The exponential I = I₀ exp(−αd) is linearised in practice by calibrating in "
        "place, and the 2^(−t/T_H) term is not optional — a Cs-137 source loses 2,3 % of its activity a "
        "year, and an instrument that ignores that will drift out of tolerance without anything "
        "failing."))
    b.append(fig(15, F.fig_11_15(), "en"))
    b.append(p(
        "The vibrating fork closes the section and is the most-sold level switch in the world. A piezo "
        "bender drives the fork at resonance; when the paddles are immersed, the viscosity of the "
        "product damps the vibration and the electronics see the change in drive power or in resonant "
        "frequency. It is a point switch, it is insensitive to foam, and it is the reason §11.3 exists "
        "at all: a great many level measurements in a plant are really the question “is there anything "
        "here?”, and a fork answers it for the price of a pressure gauge."))

    b.append(h2("What the price table actually says"))
    b.append(p(
        "Table 11.2 is a 1999 price list, so the absolute numbers are stale — but the ordering is not, "
        "and the ordering is the point."))
    b.append(table(
        ["Technique", "Range", "Attainable accuracy", "Avg. price"],
        [["Displacer / float", "Continuous, liquids", "1 mm", "$2,000"],
         ["Float switch", "Liquids", "10 mm", "$500"],
         ["Pressure", "Continuous, liquids", "10 mm", "$2,000"],
         ["Ultrasonic", "Continuous, liquids and solids", "5 mm", "$2,500"],
         ["Radar", "Continuous, liquids and solids", "1 mm", "$3,000"],
         ["TDR", "Continuous, liquids and solids", "3 mm", "$2,500"],
         ["Laser", "Continuous, liquids and solids", "0.1 mm", "$10,000"],
         ["Radiometric", "Continuous, liquids and solids", "10 mm", "$5,000"],
         ["Capacitive", "Switch, liquids", "10 mm", "$500"],
         ["Viscosity", "Switch, liquids", "10 mm", "$500"]],
        "Table 11.2 · Priority level measurement techniques and prices for industrial applications."))
    b.append(p(
        "Two readings. Accuracy costs money roughly as a logarithm: 10 mm is $500, 1 mm is $3,000, "
        "0,1 mm is $10,000 — and the last step buys a laser, which fails in dust. Contactless costs a "
        "premium over contact: radar at $3,000 against a displacer at $2,000 for the same 1 mm. And the "
        "three switch technologies all sit at $500, which is the real message of the table: if the "
        "question is yes/no, the answer is cheap, and the expensive part of the specification is "
        "deciding that the question really is yes/no."))

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 10</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 11 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 11 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 11 “Level Measurement” của Detlef Brumbi — đo mức bằng lực nổi, "
            "bằng áp suất thuỷ tĩnh, bằng thời gian bay (siêu âm, radar FMCW, TDR, laser), bằng điện "
            "dung và bằng suy giảm bức xạ, kèm bảng giá và danh sách nhà chế tạo." if vi else
            "Companion to Chapter 11 of the CRC Measurement Handbook — level measurement by buoyancy, "
            "hydrostatics, time of flight (ultrasonic, FMCW radar, TDR, laser), capacitance and "
            "radiation attenuation, with all fifteen figures.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 11' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 11' % BASE_EN)
    meta = ("Chương 11 · theo Ch11.pdf (CRC Press, 1999) · 15 hình, 3 bảng, 23 phương trình" if vi
            else "Chapter 11 · 15 figures, 3 tables, 23 equations")
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
