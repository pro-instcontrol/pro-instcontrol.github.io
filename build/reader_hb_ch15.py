# -*- coding: utf-8 -*-
"""Handbook Chapter 15 — Tilt Measurement (Adam Chrzanowski, James M. Secord).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch15.py
"""
import os

import hb15fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch15-tilt-measurement"
TITLE_EN = "Tilt Measurement"
TITLE_VI = "Đo độ nghiêng"
BYLINE = "Adam Chrzanowski · James M. Secord · University of New Brunswick"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch14-angle-measurement"
PREV_VI = "ch14-angle-measurement"
PREV_T_EN = "Angle Measurement"
PREV_T_VI = "Đo góc"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-15-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Nếu vị trí tương đối của hai điểm được mô tả bởi hướng không gian ba chiều của đường nối chúng, "
        "thì nói chung <b>độ nghiêng</b> (tilt) là lượng góc mà hướng đó đã thay đổi, trong một mặt phẳng "
        "thẳng đứng, so với một hướng trước đó hoặc một hướng tham chiếu. Nếu hướng gốc gần nằm ngang, người "
        "ta thường dùng thuật ngữ “độ nghiêng”; nếu gần thẳng đứng, sự thay đổi thường được coi là “độ dốc” "
        "(inclination). Ở đây, “độ nghiêng” sẽ chỉ cả hai nghĩa. Hai điểm có thể cách nhau một khoảng gọi là "
        "<b>cơ sở</b> (base), hoặc độ nghiêng đo tại một điểm với hướng tham chiếu là hướng của lực hấp dẫn tại "
        "điểm đó. Do đó, cùng một dụng cụ đo độ nghiêng tại một điểm có thể gọi là <b>tiltmeter</b> hoặc "
        "<b>inclinometer</b> (hay clinometer), tuỳ cách diễn giải kết quả."))
    b.append(p(
        "Độ nghiêng góc liên hệ trực tiếp với lượng thay đổi tuyến tính trên chiều dài cơ sở. Vì vậy, độ "
        "nghiêng góc không nhất thiết phải đo trực tiếp mà có thể suy ra từ phép đo cơ học hay đo khác về "
        "lượng thay đổi tuyến tính đó, miễn biết chiều dài cơ sở. Thảo luận sau đây được chia thành: (1) "
        "tiltmeter hay inclinometer (độ nghiêng góc tại một điểm hay trên cơ sở ngắn); (2) thuỷ chuẩn trắc "
        "địa (geodetic leveling — suy từ chênh cao trên cơ sở rất dài); (3) thuỷ chuẩn cân bằng (hydrostatic "
        "leveling — suy từ chênh cao trên cơ sở dài hữu hạn); (4) dây dọi treo và ngược (plumb lines — độ "
        "dốc từ hiệu vị trí ngang trên một cơ sở thẳng đứng)."))

    # ---- 15.1
    b.append(h2("15.1 Tiltmeter hay Inclinometer", "Tiltmeters or Inclinometers"))
    b.append(p(
        "Xét theo nguyên lý hoạt động, tiltmeter có thể chia thành: loại chất lỏng (kể cả kiểu bóng khí "
        "spirit), con lắc thẳng đứng, hoặc con lắc nằm ngang. Dunnicliff [1] có bài tổng quan toàn diện phân "
        "loại theo cách cảm biến độ nghiêng (cơ học, truyền động gia tốc kế, dây rung, hay điện ly). Độ nhạy "
        "chia thành hai nhóm: tiltmeter trắc địa/địa vật lý có độ phân giải 10⁻⁸ rad (0,002″) hay tới 10⁻⁹ rad; "
        "và tiltmeter công trình có độ phân giải từ 0,1″ đến vài giây cung tuỳ dải đo."))
    b.append(p(
        "Nhóm đầu gồm các dụng cụ chủ yếu cho nghiên cứu địa vật lý về hiện tượng thuỷ triều Trái Đất và chuyển "
        "động kiến tạo — ví dụ tiltmeter con lắc ngang Verbaander–Melchior [2] và Zöllner [3,4], cùng "
        "tiltmeter kiểu bóng thuỷ ngân Rockwell Model TM-1 [5]; chúng đòi hỏi lắp đặt cực kỳ ổn định và môi "
        "trường được kiểm soát. Ít công trình cần nhạy cảm đến thế, song đo biến dạng hầm chứa rác thải hạt "
        "nhân có thể là một ứng dụng. Một ví dụ là tiltmeter thuỷ ngân (Model 300) của Auckland Nuclear "
        "Accessory Co. (New Zealand): sự thay đổi điện dung giữa điện cực và mặt thuỷ ngân tỉ lệ với độ nghiêng; "
        "dải 15″, độ phân giải 10⁻⁹ rad (0,0002″), tức chuyển vị thẳng đứng tương đối chỉ 6·10⁻⁷ mm trên cơ sở "
        "587 mm."))
    b.append(p(
        "Nhóm hai có nhiều mẫu tiltmeter chất lỏng hay con lắc giá phải chăng (2000–5000 USD) thoả mãn đa số "
        "nhu cầu công trình. Ngoài ống thuỷ (level vial) đơn, dạng đơn giản nhất là một cơ sở dài vài chục cm "
        "được căn bằng bằng cách đưa bóng khí vào giữa, nhìn trực tiếp hoặc bằng quan sát trùng khớp (coincidence) "
        "hai đầu bóng. Nhìn trực tiếp cho độ phân giải 1/5 vạch (thường 2 mm), nhạy 10″–30″/vạch; quan sát "
        "trùng khớp nâng độ chính xác căn chỉnh lên 0,03 độ nhạy của ống. Độ lệch so với nằm ngang giữa hai "
        "điểm đo xác định bằng đồng hồ so hoặc cá mớm có độ phân giải 0,0005 in (0,02 mm). Huggenberger AG "
        "công bố nhạy 0,3″ (10⁻⁴ gon) trên dải ±21′ cho clinometer có cơ sở 100 mm và căn bóng trùng khớp, gắn "
        "vào cơ sở 1 m để đo ngang hay dọc."))
    b.append(p(
        "Nếu ống thuỷ chứa chất điện ly, việc căn bóng thực hiện bằng điện — ví dụ Electrolevel (British "
        "Aircraft Corp.) dùng nguyên lý bóng khí [6], chuyển động bóng được ba điện cực cảm biến; độ nghiêng "
        "làm thay đổi điện trở vi sai giữa các điện cực, đo bằng cầu Wheatstone, đạt độ phân giải 0,25″ trên "
        "dải vài phút cung. Rank Organization (Anh) [9] làm mức điện tử giảm chấn chất lỏng Talyvel, độ chính "
        "xác ±0,5″ trên dải ±8′. Tương tự là transducer con lắc loại Niveltronic (Tesa S.A., Thuỵ Sĩ; dải "
        "±150″, độ chính xác ±0,2″). Phổ biến nhất là tiltmeter servo-gia tốc kế với con lắc nằm ngang: bền, "
        "bền bỉ, chạy được ở nhiệt độ thấp; điện áp ra tỉ lệ với sin góc nghiêng. Schaevitz Engineering làm "
        "servo-gia tốc kế có mái chèo nằm ngang nhỏ chuyển động theo hướng nghiêng do trọng lực; chuyển động "
        "được cảm biến vị trí đưa vào bộ khuếch đại, dòng ra tác động lên động cơ mô-men tạo mô-men đối nhau, "
        "và dòng động cơ tạo điện áp ra tỉ lệ với sin góc nghiêng."))
    b.append(p(
        "Dải điện áp ra điển hình là ±5 V, ứng với dải nghiêng cực đại và dễ ghép nối nối tiếp. Độ phân giải "
        "góc phụ thuộc dải đo: dải lớn hơn sinh nhiều độ nghiêng trên mỗi đơn vị điện áp, nên tiltmeter độ phân "
        "giải cao có dải đo nhỏ hơn. Thường độ phân giải là 0,02% dải (theo vôn) [10]. Nhiều yếu tố ảnh hưởng "
        "độ chính xác: nhiệt độ đổi kích thước cơ khí và độ nhớt chất lỏng (điện ly) hay dầu giảm chấn (con "
        "lắc), đồng thời đặc tính điện cũng đổi. Bù nhiệt có thể tích hợp vào chế tạo (tăng giá) hoặc thiết kế "
        "phản ứng tuyến tính rồi hiệu chỉnh ca-lip đơn giản. Mẫu rẻ thì bù không tinh xảo, có thể cho đầu ra "
        "phi tuyến và trôi khó预测; do đó cần thử nghiệm và ca-lip kỹ [11]."))
    b.append(p(
        "Bộ bù vòng đứng của kinh vĩ phân tử dùng cùng nguyên lý với một số tiltmeter công trình. Bộ bù lỏng "
        "của kinh vĩ điện tử Kern E2 [12] lặp lại tốt hơn 0,3″ trên dải ±150″, và được đưa vào tiltmeter "
        "NIVEL 20 (1989); hệ thống bù này cũng có trong tổng đài điện tử chính xác Leica TC2002 [13], nên "
        "kinh vĩ cũng dùng làm tiltmeter với độ chính xác tương đương Electrolevel."))
    b.append(p(
        "Tiltmeter có nhiều ứng dụng. Một dãy tiltmeter dọc theo mặt cắt địa hình ở mỏ có thể thay thuỷ chuẩn "
        "trắc địa để xác định sụt lún mặt đất [11] (Hình 15.1). Ví dụ, sụt lún điểm 4 (δh₄) so với điểm 1 ước "
        "tính từ các thay đổi độ nghiêng αᵢ (rad) và khoảng cách đã biết:"))
    b.append(eq("δh₄ = α₁ s₁ + α₂ s₂ + α₃ s₃", "15.1"))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Độ trung thực phụ thuộc mật độ đo dọc mặt cắt và tính liên tục (giả thiết dốc đều giữa các điểm). "
        "Tương tự, hồ sơ biến dạng nhà cao tầng xác định bằng dãy tiltmeter ở các cao độ khác nhau [14]; hồ sơ "
        "lỗ khoan cũng tạo tương tự. Hồ sơ tuyệt đối lỗ khoan sinh ra bằng cách xét chuyển vị ngang theo hướng "
        "định hướng của inclinometer (thường do rãnh dẫn trong ống lồng) tại vị trí thứ i, ở độ sâu sᵢ — nhưng "
        "cần ca-lip inclinometer về không ở vị trí thẳng đứng vì các αᵢ là độ nghiêng so với thẳng đứng."))
    b.append(p(
        "Trong cơ địa kỹ thuật, ứng dụng phổ biến nhất của tiltmeter và inclinometer lỗ khoan là nghiên cứu "
        "ổn định sườn dốc và giám sát đập đất đắp. Inclinometer lưỡng trục hình ngư lôi quét các lỗ khoan khoan "
        "tới tầng ổn định; SINCO và các hãng khác cung cấp inclinometer lỗ khoan đặc chủng (dài 50 cm hay 2 ft) "
        "có bánh dẫn hướng. Lỗ khoan sâu 40 m đo mỗi 50 cm bằng inclinometer độ chính xác chỉ ±100″ cho phép "
        "xác định chuyển vị ngang tại miệng lỗ với độ chính xác ±2 mm. Khi khó tiếp cận hoặc cần thu liên tục "
        "(hay cả hai), tiltmeter/inclinometer để lại tại trạm với hệ viễn đo cho phép truyền về nơi xử lý — ví "
        "dụ trạm giám sát sụt lún mỏ gần Sparwood (CANMET) dùng tới 256 trạm, mỗi trạm nhận 6 cảm biến."))

    # ---- 15.2
    b.append(h2("15.2 Thuỷ chuẩn trắc địa", "Geodetic Leveling"))
    b.append(p(
        "Thuỷ chuẩn trắc địa hay vi phân đo chênh cao giữa hai điểm bằng máy thuỷ bình nghiêng chính xác, "
        "hoặc máy thuỷ bình tự động có bộ bù, với vi phân kế bản song song và mia invar đã hiệu chuẩn. Công "
        "nghệ mới có máy thuỷ bình tự động số dùng cảm biến CCD và mã vạch trên mia [17]. Trong một lần dựng "
        "máy, chênh cao là số đọc mia lùi trừ số đọc mia tới; nhiều lần dựng máy cộng lại thành chênh cao giữa "
        "hai điểm, nhưng sai số tích luỹ theo số lần dựng. Với cự ly ngắm không quá 20 m, thuỷ chuẩn trắc địa "
        "cho chênh cao độ chính xác ±0,1 mm/lần, tương đương ±0,5″ độ nghiêng. Dù truyền thống dùng xác định "
        "cao độ, nó thường giám sát không chỉ lún công trình nhạy cảm mà còn mô tả độ nghiêng bộ phận công "
        "trình qua độ nghiêng giữa các cọc mốc thích hợp [18]."))
    b.append(p(
        "Vì mức tham chiếu tạo bởi đường ngắm quang học qua kính (phóng đại tới 40×), nguồn sai số hệ thống "
        "chính là khúc xạ khí quyển thẳng đứng: gradient nhiệt độ chỉ 1°C/m across đường ngắm uốn đường "
        "ngắm lệch 0,4 mm ở 30 m. Giữ cự ly ngắn giảm hiệu ứng này nhưng lại tăng tích luỹ sai số ngẫu nhiên "
        "với mỗi lần dựng máy. Các sai số nhỏ trong vài lần dựng trở nên lớn khi số lần dựng nhiều (sai số "
        "chia vạch mia, lún máy hay mia)."))
    b.append(p(
        "Có cao độ h₁, h₂ của hai điểm, hay chênh cao đo được Δh₁₂(t) = h₂ − h₁ tại thời t, thì độ nghiêng "
        "T₁₂ = d(Δh)/s₁₂ (s₁₂ là khoảng cách nằm ngang). Sai số tổng: s_T² = s_{dΔh}²/s² + s_s²·(dΔh/s⁴). "
        "Ví dụ hai điểm cách 60 m, chênh cao 0,5 m biết đến ±50 µm, khoảng cách biết đến ±0,01 m, thì độ "
        "nghiêng có độ chính xác ±0,3″. Việc đo chênh cao hay xác định khoảng cách không nhất thiết trực tiếp "
        "giữa hai điểm — thuỷ chuẩn làm theo lộ trình tiện và khoảng cách lấy từ giá trị toạ độ [21]."))
    b.append(eq("T₁₂ = d(Δh) / s₁₂"))

    # ---- 15.3
    b.append(h2("15.3 Thuỷ chuẩn cân bằng", "Hydrostatic Leveling"))
    b.append(p(
        "Nếu hai bình chứa nối nhau (Hình 15.2) được đổ một phần chất lỏng, thì các độ cao h₁ và h₂ liên hệ "
        "qua phương trình thuỷ tĩnh (phương trình Bernoulli [22]):"))
    b.append(eq("P₁ + ρ₁ g h₁ = P₂ + ρ₂ g h₂ = c", "15.2"))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Quan hệ này dùng trong thuỷ chuẩn cân bằng, minh hoạ ở Hình 15.3. Ống khí nối hai bình loại bỏ sai "
        "số do áp suất khí khác nhau tại hai trạm. Nhiệt độ chất lỏng cũng nên không đổi — ví dụ chênh 1,2°C "
        "giữa hai bình gây sai số 0,05 mm trong xác định Δh với h trung bình 0,2 m, t = 20°C. Huggett và cộng "
        "sự [23] chế tạo tiltmeter hai chất lỏng khắc nhiệt, công bố độ phân giải 10⁻⁸–10⁻⁹ rad trên khoảng "
        "cách tới 1 km. Dunnicliff [1] lưu ý đảm bảo không đứt đoạn trong chất lỏng: bọt khí (thường lọt vào "
        "khi đổ ống) gây sai số chênh mực, đặc biệt ở đoạn ống thẳng đứng; đồng thời đường kính trong và hiệu "
        "ứng mao dẫn của ống cũng ảnh hưởng."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Hai ví dụ điển hình: ELWAAG 001 (Đức [24]) tự động hoàn toàn, chân cảm biến dịch chuyển bằng động "
        "cơ bước chạm mặt chất lỏng, độ lệch chuẩn ±0,03 mm trên 40 m; hệ Nivomatic (Telemac/Roctest) dùng "
        "transducer cảm ứng dịch chuyển phao thành tín hiệu tần số, độ chính xác ±0,1 mm trên 24 m. P & S "
        "Enterprises làm mức thuỷ tĩnh xách tay Pellissier H5, độ chính xác ±5 mm trên ống 14 m. Thuỷ chuẩn "
        "cân bằng dùng mạng lưới thiết bị lắp cố định giám sát độ nghiêng công trình lớn — ví dụ hệ DAG của "
        "SIS Geotecnica (Ý) độ chính xác ~±0,01 mm. Các hệ gage lún hai chất lỏng (nước và thuỷ ngân) dùng "
        "giám sát đập [26]. Dụng cụ đo mực trực tiếp bị giới hạn chiều cao bình; thay vào đó đo áp suất chất "
        "lỏng bằng tế bào khí nén hay transducer áp suất."))

    # ---- 15.4
    b.append(h2("15.4 Dây dọi treo và ngược", "Suspended and Inverted Plumb Lines"))
    b.append(p(
        "Hai loại dây dọi cơ học dùng giám sát ổn định công trình thẳng đứng: (1) con lắc treo hay dây dọi "
        "(Hình 15.4a); (2) con lắc nổi hay dây dọi ngược (Hình 15.4b). Ứng dụng điển hình là giám sát đập và "
        "ổn định cọc mốc khảo sát. Dây dọi treo cũng dùng phổ biến trong đo hướng mỏ và giám sát ổn định "
        "giếng mỏ. Độ nghiêng suy từ hiệu vị trí ngang kết hợp với tách thẳng đứng, như thuỷ chuẩn trắc địa. "
        "Hai bàn đọc, mỗi bên ±0,02 mm, với hiệu vị trí 100 mm và tách thẳng đứng 10 m biết ±0,01 m, cho độ "
        "chính xác nghiêng ±2″."))
    b.append(fig(4, F.fig(4)))
    b.append(p(
        "Dây dọi ngược trở thành chuẩn mực ở đập lớn (Hydro Quebec dùng thường quy). Ưu điểm so với dây treo "
        "là giám sát chuyển vị tuyệt đối của công trình so với điểm mỏ neo sâu trong nền đá coi là ổn định; "
        "ở đập, neo phải sâu 30 m hay hơn dưới nền để có chuyển vị tuyệt đối bề mặt. Vấn đề chính là khoan "
        "lỗ thẳng đứng sao cho dây giữ thẳng đứng tự do. Nhiều loại thiết bị ghi nhận chuyển vị điểm so với "
        "dây dọi: cơ học/điện cơ học (±0,2 mm), kính hiển vi dịch chuyển, tự động bằng Telecoordinator "
        "(Huggenberger AG) hay Telependulum (Telemac, bán bởi Roctest) dùng cảm biến proximity cảm ứng, độ "
        "phân giải 0,01 mm. Hệ Automated Vision (Spectron Engineering) dùng camera bán dẫn, độ phân giải ~3 "
        "mm trên dải ~75 mm, lắp tại đập Glen Canyon và Monticello từ 1982 [29]."))
    b.append(p(
        "Hai nguồn sai số thường bị đánh giá thấp: (1) ảnh hưởng luồng khí; (2) dạng xoắn (ủ mềm) của dây. "
        "Nếu dây (Hình 15.5a) có khối lượng quả dọi Q, phơi đoạn dài h trước luồng khí tốc độ v ở cách mỏ neo "
        "H, thì dây lệch một lượng [30]:"))
    b.append(eq("e = f₀ h H / Q", "15.3"))
    b.append(p("với f₀ là lực luồng khí tác dụng trên mỗi đơn vị dài dây, tính gần đúng [30]:"))
    b.append(eq("f₀ = 0,08 d v² Q", "15.4"))
    b.append(p(
        "với d đường kính dây (mm), v (m/s), Q (kg). Ví dụ H = 50 m, h = 5 m, d = 1 mm, Q = 20 kg, v = 1 "
        "m/s thì e = 1 mm. Nguồn sai số thứ hai — dạng xoắn của dây (Hình 15.5b) — ảnh hưởng mọi dây trừ "
        "khi được thẳng hoá đặc chủng hay treo lâu (vài tháng). Nếu dây đổi vị trí (xoay) giữa hai đợt đo, "
        "chuyển vị ghi nhận có sai số cực đại 2r, với r tính từ [30]:"))
    b.append(eq("r = (d / 8) · √(π E R / Q)", "15.5"))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "với E môđun đàn hồi Young (~2·10¹¹ Pa cho thép), R bán kính xoắn tự do của dây không tải (~15 cm "
        "cho dây đến 1,5 mm), d và Q như trên. Với d = 1 mm, R = 15 cm, Q = 196 N (20 kg) thì r = 0,3 mm. "
        "Nếu một dây dọi không xuyên suốt mọi cao độ, có thể kết hợp dây treo và ngược miễn chồng ít nhất tại "
        "một cao độ; lỗ khoan dây dọi ở Hydro Quebec còn dùng lắp dây invar căng để giám sát biến thiên cao "
        "độ (giãn thẳng đứng) [31]."))

    # ---- 15.5
    b.append(h2("15.5 Tích hợp các quan trắc", "Integration of Observations"))
    b.append(p(
        "Các thảo luận trên xét dụng cụ riêng lẻ. Vì nhiều điều tra lặp lại đo lường theo thời gian dài, tính "
        "trung thực và tham chiếu về quan trắc gốc là sống còn. Không nên kỳ vọng thiết bị hành xử nhất quán, "
        "nhất là môi trường biến thiên mạnh (đặc biệt nhiệt độ) và lâu dài. Hai cách đảm bảo tin cậy: (1) thử "
        "nghiệm và ca-lip định kỳ; (2) phân tích quan trắc tích luỹ — mỗi đại lượng là chuỗi thời gian lặp, "
        "hoặc tích hợp các vị trí/loại quan trắc. Công cụ phân tích tích hợp, ca-lip và chuỗi thời gian đã "
        "phát triển [21,32] và áp dụng thành công [15,18,33]. Ca-lip đúng, phân tích xu hướng thống kê nghiêm "
        "ngặt và phân tích tích hợp là công cụ giá trị trong phân tích biến dạng."))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>J. Dunnicliff, <i>Geotechnical Instrumentation for Monitoring Field Performance</i>, New York: John Wiley &amp; Sons, 1988.</li>'
             '<li>P. Melchior, <i>The Tides of the Planet Earth</i>, 2nd ed., Oxford, U.K.: Pergammon Press, 1983.</li>'
             '<li>W. Torge, <i>Geodesy</i>, New York: Walter de Gruyter, 1991.</li>'
             '<li>M. van Ruymbeke, Sur un pendule horizontal équipé d’un capteur de déplacement a capacité variable, <i>Bull. Géodesique</i>, 50, 281–290, 1976.</li>'
             '<li>G. L. Cooper and W. T. Schmars, Selected applications of a biaxial tiltmeter in the ground motion environment, <i>J. Spacecraft Rockets</i>, 11, 530–535, 1974.</li>'
             '<li>M. A. R. Cooper, <i>Modern Theodolites and Levels</i>, London: Crosby Lockwood, 1971.</li>'
             '<li>G. R. Holzhausen, Low-cost, automated detection of precursors to dam failure: Coolidge Dam, Arizona, Assoc. of State Dam Safety Officials, 8th Annu. Conf., San Diego, CA, 1991.</li>'
             '<li>N. H. Egan and G. R. Holzhausen, Evaluating structures using tilt (rotation) measurements, <i>Sensors Expo West Proc.</i>, 1991.</li>'
             '<li>W. Caspary and A. Geiger, Untersuchungen zur Leistungsfähigkeit elektronischer Neigungsmesser, <i>Schriftenreihe Vermessungswesen HSBW</i>, 3, München, Germany, 1978.</li>'
             '<li>A. Chrzanowski, Geotechnical and other non-geodetic methods in deformation measurements, in Y. Bock (ed.), <i>Proc. Deformation Measurements Workshop</i>, MIT, Boston, 1986, 112–153.</li>'
             '<li>A. Chrzanowski, W. Faig, B. Kurz, and A. Makosinski, Development, installation and operation of a subsidence monitoring and telemetry system, Contract report to CANMET, Calgary, Canada, Nov. 1980.</li>'
             '<li>Kern &amp; Co. Ltd., <i>E2 Instruction Manual</i>, Kern &amp; Co. Ltd., Aarau, Germany, 1984.</li>'
             '<li>Leica AG, <i>Wild TC2002 User Manual</i>, Leica AG, Heerbrugg, Germany, 1993.</li>'
             '<li>H. Kahmen, <i>Elektronische Messverfahren in der Geodäsie</i>, Karlsruhe: Herbert Wichmann, 1978.</li>'
             '<li>A. Chrzanowski and M. Y. Fisekci, Application of tiltmeters with a remote data acquisition in monitoring mining subsidence, <i>Proc. 4th Canadian Symp. Mine Surveying</i>, Banff, Alberta, Canada, June 1982.</li>'
             '<li>A. Chrzanowski, A. Makosinski, A. Zielinski, and W. Faig, Highwall Monitoring System, Contract report to Syncrude Canada Limited, April 1988.</li>'
             '<li>H. Ingensand, Wild NA2002, NA3000, Technical paper digital levels, Leica AG, Heerbrugg, Germany, 1993.</li>'
             '<li>A. Chrzanowski and J. M. Secord, The 1989 Integrated Analysis of Deformation Measurements at the Mactaquac Generating Station, Contract Report to N.B. Power, May 1990.</li>'
             '<li>P. Vanicek, R. O. Castle, and E. I. Balazs, Geodetic leveling and its applications, <i>Rev. Geophys. Space Phys.</i>, 18(2), 505–524, 1980.</li>'
             '<li>M. C. Schomaker and R. M. Berry, <i>Geodetic Levelling</i>, NOAA Manual NOS NGS 3, U.S. Dept. of Commerce, NOAA, NOS, Rockville, MD, 1981.</li>'
             '<li>J. M. Secord, Development of the automatic data management and the analysis of integrated deformation measurements, Ph.D. dissertation, Dept. of Geodesy and Geomatics Engineering Tech. Report 176, Univ. of New Brunswick, Fredericton, 1995.</li>'
             '<li>K. Schnädelbach, Neuere Verfahren zur präzisen Längen-und Höhenmessung, <i>Algemeine Vermessungs-Nachrichten</i>, 1/1980.</li>'
             '<li>G. R. Huggett, L. E. Slater, and G. Pavlis, Precision leveling with a two-fluid tiltmeter, <i>Geophys. Res. Lett.</i>, 3(12), 754–756, 1976.</li>'
             '<li>H. Thierbach and W. Barth, Eine neue automatische Präzisionsschlauchwaage, <i>Z. Vermessungswesen</i>, 100, 470–478, 1976.</li>'
             '<li>F. Robotti and T. Rossini, Analysis of differential settlements on monumental structures by means of the DAG automatic measuring device of levels and inclinations, in <i>Land Subsidence</i>, IAHA Pub. No. 151, 1984.</li>'
             '<li>T. H. Hanna, <i>Field Instrumentation in Geotechnical Engineering</i>, Clausthal-Zellerfeld, Germany, Trans Tech Publications, 1985.</li>'
             '<li>E. Meier, A differential pressure tiltmeter for large-scale ground monitoring, <i>Water Power &amp; Dam Construction</i>, 43(1), 38–40, 1991.</li>'
             '<li>L. Dubreuil and R. Hamelin, Le forage vertical des trous de pendules inversés, 2nd Canadian Symp. Mining Surveying Rock Deformation Measurements, Kingston, Ontario, Canada, 1974.</li>'
             '<li>G. Kanegis, Automated vision system installed at Glen Canyon Dam, Spectron Engineering, n.d. [circa 1983].</li>'
             '<li>A. Chrzanowski, E. Derenyi, and P. Wilson, Underground survey measurements — Research for progress, <i>The Canadian Mining and Metallurgical Bulletin</i>, June 1967.</li>'
             '<li>B. Boyer and R. Hamelin, Monitoring Survey: Recent Developments in the Use of Inverted Pendula, Report No. 4, Question 56, XV Congress Int. Commission Large Dams, Lausanne, 1985.</li>'
             '<li>A. Chrzanowski, Y. Q. Chen, P. Romero, and J. Secord, Integration of geodetic and geotechnical deformation surveys in the geosciences, <i>Tectonophysics</i>, 130, 1986.</li>'
             '<li>A. Chrzanowski, Y. Q. Chen, J. Secord, and A. Szostak-Chrzanowski, Problems and solutions in the integrated monitoring and analysis of dam deformations, <i>CISM J. ACSGC</i>, 45(4), 547–560, 1991.</li>'
             '</ol>')

    # ---- appendix: suppliers
    b.append(h3("Phụ lục — Một số nhà cung cấp thiết bị đo độ nghiêng", "Appendix — A Sampling of Possible Suppliers"))
    b.append(table(
        ["Hãng", "Địa chỉ"],
        [["Applied Geomechanics Inc.", "1336 Brommer Street, Santa Cruz, CA 95062, USA"],
         ["Auckland Nuclear Accessory Company Ltd.", "P.O. Box 16066, Auckland 3, New Zealand"],
         ["Eastman Whipstock GmbH", "Gutenbergstrasse 3, 3005 Hannover-Westerfeld, West Germany"],
         ["Geotechnical Instruments Ltd.", "Station House, Old Warwich Road, Leamington Spa, Warwickshire CV31 3HR, England"],
         ["Huggenberger AG", "Holstrasse 176, CH-8040 Zürich, Switzerland"],
         ["IRAD GAGE", "Etna Road, Lebanon, NH 03766, USA"],
         ["Leica AG", "CH-9435 Heerbrugg, Switzerland"],
         ["Measurement Devices Limited", "11211 Richmond Avenue, Suite 106, Building B, Houston, TX 77082, USA"],
         ["Maihak AG", "Semperstrasse 38, D-2000 Hamburg 60, West Germany"],
         ["Roctest Ltée Ltd.", "665 Pine, Montreal, P.Q., Canada J4P 2P4"],
         ["RST Instruments Ltd.", "1780 McLean Avenue, Port Coquitlam, B.C., Canada V3C 4K9"],
         ["Schaevitz Engineering", "P.O. Box 505, Camden, NJ 08101, USA"],
         ["Serata Geomechanics, Inc.", "4124 Lakeside Drive, Richmond, CA 94806, USA"],
         ["SINCO (Slope Indicator Co.)", "3668 Albion Place N., Seattle, WA 98103, USA"],
         ["Soil Instruments Ltd.", "Bell Lane, Uckfield, East Sussex TN22 1Ql, England"],
         ["Solexperts AG", "Postfach 274, CH-8034 Zürich, Switzerland"],
         ["Solinst Canada Ltd.", "2440 Industrial St., Burlington, Ontario, Canada L7P 1A5"],
         ["SIS Geotecnica", "Via Roma, 15, 20090 Segrate (Mi), Italy"],
         ["Spectron Engineering", "800 West 9th Avenue, Denver, CO 80204, USA"],
         ["Spectron Glass and Electronics Inc.", "595 Old Willets Path, Hauppauge, NY 11788, USA"],
         ["Telemac", "2 Rue Auguste Thomas, 92600 Asnieres, France"],
         ["Terrametrics", "16027 West 5th Avenue, Golden, CO 80401, USA"],
         ["P &amp; S Enterprises, Ltd.", "240 South Monaco Pkwy, #302, Denver, CO 80224, USA"],
         ["Edi Meier &amp; Partner", "8408 Winterthur, Switzerland"]],
        "Phụ lục · Một mẫu các nhà cung cấp thiết bị đo độ nghiêng (trích từ chương)."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 14</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 15. All five figures are "
        "redrawn as vectors (15.1 subsidence from tilt, 15.2 hydrostatic equilibrium, 15.3 hydrostatic "
        "leveling, 15.4 suspended/inverted plumb lines, 15.5 air-current and spiral-wire errors), and the "
        "equations (15.1–15.5) plus the suppliers appendix are reproduced. The translation prose is not "
        "repeated here."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Tilt is the angular change of a line joining two points within a vertical plane; because angular "
        "tilt is directly tied to the linear change over the base length, it can be derived from a linear "
        "measurement if the base is known. Section 15.1 reviews tiltmeters/inclinometers by sensing method "
        "(liquid/bubble, vertical or horizontal pendulum; mechanical, accelerometer, vibrating-wire, or "
        "electrolytic transducer). Sensitivity splits into geophysical tiltmeters (10⁻⁸–10⁻⁹ rad) and "
        "engineering ones (0.1″–seconds of arc). Examples: the mercury Model 300 (10⁻⁹ rad over a 587 mm "
        "base), coincidence-viewing clinometers (~0.3″), the Electrolevel (0.25″), the Talyvel and "
        "Niveltronic pendulums, and the popular servo-accelerometer tiltmeters whose output voltage is "
        "proportional to sin(angle). Figure 15.1 shows subsidence from a profile of tilt readings; the "
        "subsidence of point 4 follows equation (15.1), δh₄ = α₁s₁ + α₂s₂ + α₃s₃, with fidelity limited by "
        "measurement density and the uniform-slope assumption."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Section 15.2 is geodetic leveling: precision (or digital) levels give height differences with "
        "±0.1 mm/setup (~0.5″ of tilt) but errors accumulate with setups and are biased by vertical "
        "refraction. Tilt between two benchmarks is T = d(Δh)/s; the precision compounds as shown in the "
        "chapter. Section 15.3 is hydrostatic leveling: two connected vessels satisfy the hydrostatic "
        "relation (15.2), P₁ + ρ₁gh₁ = P₂ + ρ₂gh₂ = c, illustrated in Figures 15.2 and 15.3 where the "
        "measured level difference is Dh₁₂ = r₂ − r₁. Temperature must be kept constant (1.2°C between "
        "containers ⇒ 0.05 mm error), and two-fluid designs cancel the temperature effect. Instruments "
        "cited include the ELWAAG 001 (±0.03 mm/40 m), Nivomatic (±0.1 mm/24 m), and the DAG network "
        "(~±0.01 mm)."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Section 15.4 covers suspended and inverted plumb lines (Figure 15.4): both derive inclination from "
        "a horizontal position difference over a vertical separation. Inverted plumb lines anchor deep in "
        "foundation rock to measure absolute displacement of the surface. Two under-rated error sources are "
        "air currents and the wire's spiral (annealed) shape. An air current of speed v over length h, at "
        "distance H from the anchor, deflects the wire by e = f₀hH/Q (15.3), where f₀ = 0.08 d v² Q (15.4); "
        "with H=50 m, h=5 m, d=1 mm, Q=20 kg, v=1 m/s, e=1 mm. The spiral radius r (15.5), r = (d/8)·√(πER/Q), "
        "means a rotated wire can error by up to 2r — for d=1 mm, R=15 cm, Q=196 N, r=0.3 mm. Section 15.5 "
        "stresses that reliable deformation analysis needs regular calibration and integrated, time-series "
        "statistical treatment of the observations."))
    b.append(p(
        "The chapter closes with 33 references and an appendix listing suppliers of tilt-measuring "
        "instrumentation (Applied Geomechanics, Schaevitz, SINCO, Roctest, Leica, Solinst, and others) — "
        "reproduced in the Vietnamese version."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 14</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 15 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 15 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 15 “Đo độ nghiêng” của Adam Chrzanowski và James M. Secord — "
            "tiltmeter, thuỷ chuẩn trắc địa, thuỷ chuẩn cân bằng, dây dọi treo/ngược, với 5 hình, phương "
            "trình 15.1–15.5 và phụ lục nhà cung cấp." if vi else
            "Companion to Chapter 15 of the CRC Measurement Handbook — tilt measurement by tiltmeters, "
            "geodetic and hydrostatic leveling, and plumb lines, with all five figures and equations 15.1–15.5.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 15' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 15' % BASE_EN)
    meta = ("Chương 15 · theo Ch15.pdf (CRC Press, 1999) · 5 hình, 1 phụ lục, 5 phương trình" if vi
            else "Chapter 15 · 5 figures, 1 appendix, 5 equations")
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
