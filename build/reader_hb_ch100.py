# -*- coding: utf-8 -*-
"""Handbook Chapter 100 — Explosion-Proof Instruments
(Sam S. Khalilieh, P.E. — Earth Tech).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch100.py
"""
import os

import hb100fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch100-explosion-proof-instruments"
TITLE_EN = "Explosion-Proof Instruments"
TITLE_VI = "Thiết bị đo chống nổ"
BYLINE = "Sam S. Khalilieh, P.E. · Earth Tech"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-100-%d">%s<figcaption class="figcap">%s</figcaption>'
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


def ol(items):
    return ('<ol style="margin:-.3rem 0 1.2rem 1.3rem;line-height:1.85;font-size:.95rem">'
            + "".join("<li>%s</li>" % i for i in items) + "</ol>")


def table(hd, rows, cap, cls=""):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ tables data

T1001 = [
    ("450", "842", "T1"), ("300", "572", "T2"), ("280", "536", "T2A"),
    ("260", "500", "T2B"), ("230", "446", "T2C"), ("215", "419", "T2D"),
    ("200", "392", "T3"), ("180", "356", "T3A"), ("165", "329", "T3B"),
    ("160", "320", "T3C"), ("135", "275", "T4"), ("120", "248", "T4A"),
    ("100", "212", "T5"), ("85", "185", "T6"),
]


def _t1001(lang):
    if lang == "vi":
        hd = ("Nhiệt độ lớn nhất (°C)", "(°F)", "Ký hiệu")
        cap = ("Bảng 100.1 · Nhiệt độ bề mặt lớn nhất trong mọi điều kiện vận hành. Nhiệt độ bề mặt "
               "của thiết bị điện khi làm việc không được vượt quá giới hạn của mối nguy hiện hữu. "
               "In lại theo NFPA 70-1996, National Electrical Code®, © 1995 NFPA, Quincy, MA 02269.")
    else:
        hd = ("Maximum temperature (°C)", "(°F)", "Identification")
        cap = ("Table 100.1 · Maximum surface temperature under all operating conditions. Surface "
               "temperature of electric apparatus during operation must not exceed the limits of the "
               "hazard present. Reprinted with permission from NFPA 70-1996, the National Electrical "
               "Code®, © 1995 NFPA, Quincy, MA 02269.")
    return hd, [list(r) for r in T1001], cap


def _t1002(lang):
    if lang == "vi":
        hd = ("Cấp", "Nhóm", "Chất tiêu biểu")
        rows = [
            ["I — Khí và hơi", "A", "Axetilen"],
            ["", "B", "Hyđrô"],
            ["", "C", "Ví dụ: êtylen"],
            ["", "D", "Ví dụ: mêtan"],
            ["II — Bụi cháy được", "E", "Bụi kim loại"],
            ["", "F", "Bụi than"],
            ["", "G", "Bụi ngũ cốc"],
            ["III — Xơ sợi", "—", "Xơ sợi dễ bắt lửa"],
        ]
        cap = ("Bảng 100.2 · Phân loại khu vực theo NEC. Division 1 là nơi mối nguy hiện hữu trong "
               "điều kiện vận hành bình thường; Division 2 là nơi mối nguy chỉ xuất hiện trong điều "
               "kiện vận hành bất thường. Cấp xác định dạng vật chất, nhóm xác định loại hơi hoặc bụi "
               "cụ thể.")
    else:
        hd = ("Class", "Group", "Typical substance")
        rows = [
            ["I — Gases and vapours", "A", "Acetylene"],
            ["", "B", "Hydrogen"],
            ["", "C", "e.g., ethylene"],
            ["", "D", "e.g., methane"],
            ["II — Combustible dusts", "E", "Metal dust"],
            ["", "F", "Coal dust"],
            ["", "G", "Grain dust"],
            ["III — Fibres", "—", "Easily ignitable fibres"],
        ]
        cap = ("Table 100.2 · Area classification based on the NEC. Division 1 is where the hazard is "
               "present under normal operating conditions; Division 2 is where it is present only "
               "under abnormal conditions. The Class fixes the physical form, the Group the specific "
               "vapour or dust.")
    return hd, rows, cap


def _t1003(lang):
    if lang == "vi":
        hd = ("Thiết bị trường", "Rào an toàn")
        rows = [
            ["V<sub>max</sub>", "≥ V<sub>oc</sub>"],
            ["I<sub>max</sub>", "≥ I<sub>sc</sub>"],
            ["C<sub>i</sub>", "≤ C<sub>a</sub> (điện dung cho phép lớn nhất)"],
            ["L<sub>i</sub>", "≤ L<sub>a</sub> (điện cảm cho phép lớn nhất)"],
        ]
        cap = ("Bảng 100.3 · So sánh các giá trị thực thể của thiết bị trường và của rào an toàn. "
               "Bốn bất đẳng thức này là toàn bộ nội dung của phép ghép thực thể.")
    else:
        hd = ("Field device", "Safety barrier")
        rows = [
            ["V<sub>max</sub>", "≥ V<sub>oc</sub>"],
            ["I<sub>max</sub>", "≥ I<sub>sc</sub>"],
            ["C<sub>i</sub>", "≤ C<sub>a</sub> (maximum allowed capacitance)"],
            ["L<sub>i</sub>", "≤ L<sub>a</sub> (maximum allowed inductance)"],
        ]
        cap = ("Table 100.3 · Comparison of the entity values of a field device and a safety barrier. "
               "These four inequalities are the whole of the entity match.")
    return hd, rows, cap


# ================================================================ Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Ở những nơi có thể tồn tại khí quyển nguy hiểm, điện năng phải là mối quan tâm hàng đầu của "
        "mọi kỹ sư và người thiết kế hệ thống. Khí quyển nguy hiểm không chỉ có trong những môi "
        "trường quen thuộc của các cơ sở công nghiệp, hoá chất và môi trường, mà còn ở nhiều nơi khó "
        "ngờ hơn: nơi có bụi, nơi khí có thể tích tụ, và nơi diễn ra các phản ứng tạo thành khí cháy "
        "được. Để giảm thiểu rủi ro ở những khu vực ấy, cần thiết kế những hệ thống điện chuyên biệt "
        "nhằm giảm mối nguy. Phần lớn thiết bị điện được chế tạo theo những tiêu chuẩn cụ thể để giảm "
        "tần suất cháy và thương vong. Đại đa số sự cố thuộc loại này có thể quy cho việc lắp đặt kém "
        "hoặc có khuyết tật, sử dụng sai thiết bị đã được phê duyệt, thiết bị xuống cấp, và những ứng "
        "dụng tình cờ. Khi cộng với một bầu khí quyển cháy nổ, những yếu tố ấy có thể dẫn tới những "
        "điều kiện cực kỳ nguy hiểm. Thiết kế hệ thống điện cho một khu vực nguy hiểm đòi hỏi lập kế "
        "hoạch cẩn thận, nghiên cứu, tính toán kỹ thuật và sự khéo léo trong việc dùng đúng kỹ thuật "
        "bảo vệ, để từ đó phát triển những ứng dụng và những cách phân loại tốt hơn giúp giảm mối "
        "nguy."))

    # ------------------------------------------------------------ 100.1
    b.append(h2("100.1 Giới thiệu", "Introduction"))
    b.append(p(
        "An toàn của con người và thiết bị hiện diện trong khu vực nguy hiểm không bao giờ được coi "
        "là đương nhiên. Năm 1913, một vụ nổ khí mêtan lớn trong một mỏ than ở Glamorganshire, Nam "
        "xứ Wales đã cướp đi sinh mạng của 439 thợ mỏ. Sau nhiều tháng nghiên cứu, một nhóm chuyên "
        "gia và nhà khoa học kết luận rằng vụ nổ do một lượng nhỏ năng lượng điện tích trong mạch "
        "gây ra. Lượng năng lượng nhỏ ấy, cộng với sự hiện diện của một hỗn hợp khí cháy và không "
        "khí, cùng việc thiếu biện pháp bảo vệ thích hợp, đã hoá thành tai hoạ cho các thợ mỏ."))
    b.append(p(
        "Để hiểu những nguy hiểm gắn với thiết bị điện trong khu vực nguy hiểm, trước hết phải hiểu "
        "những điều cơ bản. Về mặt hoá học, oxy hoá, cháy và nổ đều là những phản ứng toả nhiệt, chỉ "
        "khác nhau ở tốc độ phản ứng. Để những phản ứng ấy xảy ra, ba thành phần phải cùng hiện diện "
        "đồng thời với những nồng độ nhất định: (1) nhiên liệu (lỏng, khí hoặc rắn), (2) một lượng "
        "oxy (không khí) đủ lớn, và (3) một nguồn mồi (điện hoặc nhiệt)."))
    b.append(p(
        "Một số nguồn mồi có thể nguy hiểm gồm: (1) bề mặt nóng (cuộn dây động cơ, cáp gia nhiệt, đèn "
        "chiếu sáng), (2) tia lửa và hồ quang điện (khi đóng cắt mạch, khi ngắn mạch), (3) tia lửa cơ "
        "học (ma sát, mài), (4) phóng điện tĩnh (quá trình tách ly có ít nhất một chất có khả năng "
        "tích điện), và (5) bức xạ, nén và sóng xung kích."))
    b.append(p(
        "Khi làm việc với thiết bị điện trong khu vực nguy hiểm, cần hiểu và quen thuộc với những "
        "thuật ngữ sau."))

    b.append(p(
        "<b>1. Điểm chớp cháy (flash point)</b> — nhiệt độ nhỏ nhất, ở áp suất khí quyển bình thường, "
        "mà tại đó một chất dễ cháy hoặc cháy được giải phóng đủ hơi để có thể bị mồi bởi một nguồn "
        "năng lượng. Tuỳ theo điểm chớp cháy (FP), chất lỏng dễ cháy được chia thành bốn cấp nguy "
        "hiểm:"))
    b.append(ol([
        "AI (FP &lt; 21 °C),",
        "AII (21 °C &lt; FP &lt; 55 °C),",
        "AIII (55 °C &lt; FP &lt; 100 °C), và",
        "B (FP &lt; 21 °C khi tan trong nước ở 15 °C).",
    ]))
    b.append(p(
        "<b>2. Nhiệt độ mồi (ignition temperature)</b> — nhiệt độ nhỏ nhất, ở áp suất vận hành bình "
        "thường, mà tại đó một hỗn hợp nguy hiểm tự bốc cháy, không phụ thuộc vào bộ phận gia nhiệt "
        "hay bị gia nhiệt."))
    b.append(p(
        "<b>3. Giới hạn cháy (flammable limits)</b> — giới hạn nổ trên (UEL) là tỉ số nồng độ hơi trên "
        "không khí lớn nhất mà vượt quá nó thì ngọn lửa không lan truyền khi gặp nguồn mồi; khi đó "
        "hỗn hợp được gọi là “quá giàu” để cháy. Giới hạn nổ dưới (LEL) là tỉ số nồng độ hơi trên "
        "không khí nhỏ nhất mà thấp hơn nó thì ngọn lửa không lan truyền khi gặp nguồn mồi; khi đó "
        "hỗn hợp được gọi là “quá nghèo” để nổ. Phải đặc biệt chú ý tới LEL, vì nó cho biết lượng khí "
        "tối thiểu cần thiết để tạo ra một hỗn hợp nguy hiểm. Nói chung giới hạn cháy được biểu diễn "
        "theo phần trăm thể tích, viết tắt là % vol. Cần lưu ý rằng một hỗn hợp nằm giữa UEL và LEL "
        "khi nổ sẽ dữ dội hơn nhiều so với khi hỗn hợp ở gần một trong hai giới hạn."))
    b.append(p(
        "<b>4. Nhiệt độ bề mặt lớn nhất (maximum surface temperature)</b> — nhiệt độ lớn nhất do một "
        "thiết bị điện sinh ra trong điều kiện bình thường hoặc điều kiện sự cố. Nhiệt độ này phải "
        "thấp hơn nhiệt độ mồi nhỏ nhất của bầu khí quyển có thể cháy nổ xung quanh. Thiết bị dùng "
        "trong khu vực nguy hiểm phải được ghi nhãn rõ ràng để chỉ ra cấp, nhóm và nhiệt độ bề mặt "
        "lớn nhất hoặc dải nhiệt độ quy chiếu về nhiệt độ môi trường 40 °C (104 °F). Bảng 100.1 cho "
        "thấy một thiết bị có cấp nhiệt độ T xác định có thể dùng trong môi trường có mọi loại khí "
        "có nhiệt độ mồi cao hơn cấp nhiệt độ T của thiết bị. Để thêm an toàn, nên giữ nhiệt độ bề "
        "mặt lớn nhất không vượt quá 80 % nhiệt độ mồi nhỏ nhất của khí xung quanh. Người đọc được "
        "lưu ý đừng nhầm nhiệt độ làm việc (vận hành) lớn nhất với nhiệt độ bề mặt lớn nhất — nhiệt "
        "độ sau được đo trong điều kiện xấu nhất của thiết bị điện. Một thiết bị điện được thiết kế "
        "làm việc ở nhiệt độ môi trường lớn nhất 70 °C — ngay cả trong điều kiện xấu nhất của dải "
        "nhiệt độ dự kiến — phải có độ tăng nhiệt không vượt quá biên an toàn 10 °C để được xếp cấp "
        "T6, hoặc 5 °C với các cấp T3, T4 và T5 (Bảng 100.1)."))
    hd, rows, cap = _t1001("vi")
    b.append(table(hd, rows, cap))
    b.append(p(
        "<b>5. Khối lượng riêng của hơi (vapour density)</b> — khối lượng của một thể tích hơi nguyên "
        "chất so với khối lượng của một thể tích không khí khô bằng nó, ở cùng áp suất và nhiệt độ "
        "khí quyển bình thường. Đại lượng này được tính bằng tỉ số giữa khối lượng phân tử của khí và "
        "khối lượng phân tử trung bình của không khí (28,96). Khí mêtan (CH<sub>4</sub>) có khối lượng "
        "phân tử 16 và khối lượng riêng hơi 0,6 nên có xu hướng bay lên, trong khi axêtôn "
        "(C<sub>3</sub>H<sub>6</sub>O) có khối lượng phân tử 58 và khối lượng riêng hơi 2 nên có xu "
        "hướng lắng xuống gần mặt đất."))
    b.append(p(
        "Ở Hoa Kỳ, National Electrical Code (NEC) định nghĩa khu vực nguy hiểm là “khu vực mà ở đó có "
        "thể tồn tại mối nguy tiềm ẩn trong điều kiện bình thường hoặc bất thường, do sự hiện diện "
        "của các vật liệu dễ cháy, cháy được hoặc có thể bị mồi” [1]. Định nghĩa chung này được chia "
        "thành các cấp, các division và các nhóm khác nhau để đánh giá đúng mức độ mối nguy, và để "
        "thiết kế cũng như chỉ định những hệ thống điện vận hành an toàn."))
    b.append(p(
        "Nhu cầu phân loại không chỉ quan trọng vì an toàn mà còn vì lý do kinh tế. Áp dụng đúng, kỹ "
        "thuật tốt và kinh nghiệm có thể thu hẹp phạm vi của những khu vực dễ biến động nhất (Cấp I, "
        "Division 1) vào trong những khoảng cách hợp lý quanh các điểm rò rỉ và nguồn mồi tiềm ẩn. "
        "Trong Cấp I, Division 1, chi phí thiết bị và lắp đặt có thể trở thành gánh nặng kinh tế, vì "
        "thiết bị đắt hơn đáng kể và phải qua những thử nghiệm nghiêm ngặt để bảo đảm vận hành đúng "
        "và an toàn trong điều kiện bình thường cũng như bất thường. National Fire Protection "
        "Association (NFPA 497 A &amp; B) [2] và Recommended Practice for Classification of Locations "
        "for Electrical Installations at Petroleum Facilities của American Petroleum Institute "
        "(ANSI/API RP 500) [3] là những nguồn tư liệu rất tốt để xác định ranh giới khu vực nguy "
        "hiểm."))

    # ------------------------------------------------------------ 100.2
    b.append(h2("100.2 Cơ sở của bảo vệ chống nổ", "Fundamentals of Explosion Protection"))
    b.append(p(
        "Việc phân loại một khu vực nguy hiểm trong một cơ sở thường do những người có trình độ cao "
        "thực hiện, gồm kỹ sư hoá học, kỹ sư công nghệ và cán bộ an toàn. Mục tiêu chính của họ là xác "
        "định nơi nào có bầu khí quyển nguy hiểm tiềm ẩn, trong điều kiện nào và trong bao lâu. "
        "Nghiên cứu và thiết kế cẩn thận các hệ thống điện, đặc biệt trong khu vực nguy hiểm, là yếu "
        "tố then chốt để thiết bị điện vận hành an toàn và để ngăn ngừa việc mồi cháy vật liệu dễ "
        "cháy một cách tình cờ."))
    b.append(p(
        "NEC — bộ quy phạm được nhiều bang, cơ quan và công ty chấp nhận làm cơ sở cho công tác kiểm "
        "tra — mô tả những yêu cầu và thủ tục cho hệ thống điện trong khu vực nguy hiểm. Các Điều "
        "500–504 chứa những yêu cầu về thiết bị điện và đi dây cho mọi cấp điện áp, tại những nơi có "
        "thể tồn tại mối nguy cháy hoặc nổ do khí hay hơi dễ cháy, chất lỏng dễ cháy, bụi cháy được, "
        "hoặc xơ sợi hay sợi bay dễ bắt lửa."))
    b.append(p(
        "Bảng 100.2 mô tả các khu vực nguy hiểm theo Cấp, Division và Nhóm. Cấp xác định dạng vật lý "
        "của vật liệu cháy được trộn với các phân tử oxy. Division xác định xác suất tồn tại một hỗn "
        "hợp nhiên liệu cháy nổ với không khí. Nhóm chỉ ra loại hơi hoặc bụi hiện diện. NEC đưa ra "
        "những định nghĩa sau [1].*"))
    hd, rows, cap = _t1002("vi")
    b.append(table(hd, rows, cap))

    b.append(h3("Khu vực Cấp I, Division 1", "Class I, Division 1 Locations"))
    b.append(p(
        "1. Nơi có thể tồn tại nồng độ khí hoặc hơi dễ cháy có thể bị mồi trong điều kiện vận hành "
        "bình thường; nơi những nồng độ ấy có thể tồn tại thường xuyên do sửa chữa, bảo trì hoặc do rò "
        "rỉ; và nơi sự cố hoặc vận hành lỗi của thiết bị hay công nghệ có thể giải phóng nồng độ khí "
        "hoặc hơi dễ cháy có thể bị mồi, đồng thời gây hỏng hóc thiết bị điện cùng lúc."))

    b.append(h3("Khu vực Cấp I, Division 2", "Class I, Division 2 Locations"))
    b.append(ol([
        "Nơi chất lỏng dễ bay hơi hoặc khí dễ cháy được xử lý, chế biến hay sử dụng, nhưng bình "
        "thường chất lỏng, hơi hoặc khí ấy được giữ kín trong các bình kín hoặc hệ kín, chỉ có thể "
        "thoát ra khi bình hay hệ ấy bị vỡ hoặc hỏng bất ngờ, hoặc khi thiết bị vận hành bất thường;",
        "Nơi nồng độ khí hoặc hơi có thể bị mồi thường được ngăn ngừa bằng thông gió cơ khí cưỡng "
        "bức, và nơi chúng có thể trở nên nguy hiểm khi thiết bị thông gió hỏng hoặc vận hành bất "
        "thường;",
        "Nơi liền kề các khu vực Cấp I, Division 1, và nơi nồng độ khí hoặc hơi có thể bị mồi đôi khi "
        "có thể lan tới — trừ khi sự lan truyền ấy được ngăn bằng thông gió áp suất dương từ một "
        "nguồn không khí sạch, với những biện pháp bảo vệ hiệu quả chống hỏng hóc hệ thống thông "
        "gió.",
    ]))

    b.append(h3("Khu vực Cấp II, Division 1", "Class II, Division 1 Locations"))
    b.append(ol([
        "Nơi bụi cháy được có trong không khí ở điều kiện vận hành bình thường với lượng đủ để tạo ra "
        "những hỗn hợp nổ hoặc có thể bị mồi;",
        "Nơi hỏng hóc cơ học hoặc vận hành bất thường của máy móc hay thiết bị có thể tạo ra những hỗn "
        "hợp nổ hoặc có thể bị mồi ấy, đồng thời có thể tạo nguồn mồi do thiết bị điện hỏng cùng lúc, "
        "do tác động của các thiết bị bảo vệ, hoặc do những nguyên nhân khác;",
        "Nơi bụi cháy được có tính dẫn điện có thể hiện diện với lượng nguy hiểm.",
    ]))

    b.append(h3("Khu vực Cấp II, Division 2", "Class II, Division 2 Locations"))
    b.append(p(
        "Nơi bụi cháy được bình thường không có trong không khí với lượng đủ để tạo ra những hỗn hợp "
        "nổ hoặc có thể bị mồi, và sự tích tụ bụi bình thường không đủ để cản trở việc tản nhiệt an "
        "toàn của thiết bị điện, hoặc có thể bị mồi do vận hành bất thường hay hỏng hóc thiết bị "
        "điện."))

    b.append(h3("Khu vực Cấp III, Division 1", "Class III, Division 1 Locations"))
    b.append(p(
        "Nơi xơ sợi dễ bắt lửa hoặc vật liệu sinh ra sợi bay cháy được đang được xử lý, chế tạo hoặc "
        "sử dụng."))

    b.append(h3("Khu vực Cấp III, Division 2", "Class III, Division 2 Locations"))
    b.append(p(
        "Nơi xơ sợi dễ bắt lửa được lưu trữ hoặc xử lý. Lượng và tính chất của vật liệu nguy hiểm là "
        "cơ sở để NEC phân loại các khu vực nguy hiểm. Mỗi khu vực nguy hiểm phải được đánh giá cẩn "
        "thận để xác định cách phân loại thích hợp, nhằm tạo thuận lợi cho quá trình thiết kế và giúp "
        "chỉ định đúng thiết bị."))
    b.append(note(
        "* In lại theo sự cho phép của NFPA 70-1996, National Electrical Code®, © 1995 National Fire "
        "Protection Association, Quincy, MA 02269. Tài liệu in lại này không phải là quan điểm đầy đủ "
        "và chính thức của NFPA về chủ đề được dẫn; chủ đề ấy chỉ được đại diện trọn vẹn bởi toàn văn "
        "của tiêu chuẩn. National Electrical Code® và NEC® là nhãn hiệu đã đăng ký của National Fire "
        "Protection Association, Inc., Quincy, MA 02269."))

    # ------------------------------------------------------------ 100.3
    b.append(h2("100.3 Kiểu vỏ và các yêu cầu", "Enclosure Types and Requirements"))
    b.append(p("Việc chọn đúng kiểu vỏ cho thiết bị điện quan trọng vì hai lý do:"))
    b.append(ol([
        "Bảo vệ con người khỏi việc vô tình chạm vào thiết bị điện được bao kín.",
        "Bảo vệ thiết bị bên trong khỏi tác hại từ bên ngoài.",
    ]))
    b.append(p(
        "Vỏ được ký hiệu bằng một con số chỉ mức độ bảo vệ và điều kiện mà vỏ phù hợp. Trong một số "
        "ứng dụng, vỏ có mục đích kép nên được ký hiệu bằng một số hiệu hai phần, phần nhỏ hơn đứng "
        "trước (ví dụ 7/9). Những kiểu vỏ sau đây, cùng thiết bị được bao trong chúng, đã được đánh "
        "giá theo UL 698 của Underwriters Laboratories, Inc. — <i>Industrial Control Equipment for Use "
        "in Hazardous Locations</i> — và được ghi nhãn để chỉ ra ký hiệu cấp và nhóm."))

    b.append(p(
        "<b>Vỏ kiểu 7</b> — Vỏ kiểu 7 không thông gió, dùng trong nhà, và được phân loại cho Cấp I, "
        "các Nhóm A, B, C, D như định nghĩa ở Bảng 100.2. Các chữ A đến D đôi khi xuất hiện như hậu tố "
        "của ký hiệu kiểu 7 để tạo thành ký hiệu đầy đủ. Theo UL 698, vỏ kiểu 7 phải được thiết kế để "
        "chịu được áp suất nổ bên trong của những loại khí cụ thể, và để ngăn vụ nổ ấy mồi một hỗn "
        "hợp nguy hiểm ở bên ngoài vỏ (thử nghiệm nổ). Ngoài ra, vỏ kiểu 7 chế tạo từ thép tấm phải "
        "chịu được hai lần áp suất nổ bên trong trong 1 phút mà không biến dạng vĩnh viễn, và ba lần "
        "áp suất nổ mà không rách. Nếu chế tạo bằng gang, vỏ phải chịu được bốn lần áp suất nổ mà "
        "không rách hoặc biến dạng. Có thể miễn thử nghiệm này nếu tính toán cho thấy hệ số an toàn "
        "năm trên một với kim loại đúc, hoặc bốn trên một với thép tấm chế tạo. Các thiết bị sinh "
        "nhiệt được bao trong vỏ phải được thiết kế riêng để bề mặt ngoài không đạt tới nhiệt độ có "
        "thể mồi hỗn hợp hơi – không khí cháy nổ ở bên ngoài vỏ (thử nghiệm nhiệt độ)."))
    b.append(p(
        "<b>Vỏ kiểu 8</b> — Vỏ kiểu 8 không thông gió, dùng trong nhà, và dành cho Cấp I, các Nhóm A, "
        "B, C, D như nêu ở Bảng 100.2. Các chữ A đến D xuất hiện như hậu tố của ký hiệu kiểu 8 để tạo "
        "thành ký hiệu đầy đủ. Theo UL 698, thiết bị ngâm dầu phải có khả năng làm việc ở điện áp "
        "định mức và ở điều kiện dòng điện khắc nghiệt nhất khi có mặt các hỗn hợp khí cháy – không "
        "khí, mà không mồi những hỗn hợp ấy."))
    b.append(p(
        "<b>Vỏ kiểu 9</b> — Vỏ kiểu 9 không thông gió, dùng trong nhà, và được phân loại cho Cấp II, "
        "các Nhóm E, F, G như nêu ở Bảng 100.2. Các chữ E, F hoặc G xuất hiện như hậu tố của ký hiệu "
        "kiểu 9 để tạo thành ký hiệu đầy đủ. Theo UL 698, vỏ cùng thiết bị được bao trong nó được "
        "đánh giá theo UL 698 hiện hành tại thời điểm chế tạo. Việc đánh giá này bao gồm xem xét các "
        "yêu cầu về kích thước đối với lỗ trục và các mối nối, vật liệu gioăng, và độ tăng nhiệt "
        "trong điều kiện bị bụi phủ kín. Thiết bị được vận hành ở toàn tải định mức cho tới khi đạt "
        "nhiệt độ cân bằng, rồi được để nguội về nhiệt độ môi trường trong ít nhất 30 giờ, trong khi "
        "liên tục chịu bụi tuần hoàn có tính chất quy định. Không được có bụi lọt vào vỏ (thử nghiệm "
        "chống bụi xâm nhập). Hơn nữa, vỏ kiểu 9 còn phải qua “thử nghiệm nhiệt độ có bụi phủ kín”, "
        "tương tự thử nghiệm tăng nhiệt, chỉ khác là trong lúc thử, dòng bụi tuần hoàn không được "
        "hướng trực tiếp vào thiết bị. Bụi tiếp xúc với vỏ không được bốc cháy hoặc đổi màu vì nhiệt, "
        "và nhiệt độ bề mặt ngoài, quy chiếu về 40 °C (104 °F), không được vượt quá những giá trị quy "
        "định trong điều kiện bình thường hoặc bất thường. Với vỏ có gioăng, gioăng phải làm bằng vật "
        "liệu không cháy, không thoái hoá, chống được sâu bọ và phải được gắn bằng cơ khí. Vỏ kiểu 9 "
        "có thông gió giống vỏ không thông gió, chỉ khác là việc thông gió được thực hiện bằng không "
        "khí cưỡng bức từ một nguồn bên ngoài khu vực nguy hiểm, nhằm tạo áp suất dương bên trong "
        "vỏ. Vỏ cũng phải đạt thử nghiệm thiết kế về nhiệt độ."))
    b.append(p(
        "<b>Vỏ kiểu 10</b> — Vỏ kiểu 10 không thông gió và được thiết kế để đáp ứng những yêu cầu của "
        "U.S. Bureau of Mines liên quan tới bầu khí quyển chứa hỗn hợp mêtan và không khí, có hoặc "
        "không có bụi than."))
    b.append(p(
        "Cần lưu ý rằng vỏ cho ứng dụng nguy hiểm được thiết kế cho những ứng dụng cụ thể và phải được "
        "lắp đặt, bảo trì theo khuyến nghị của nhà chế tạo vỏ, vì bất kỳ việc dùng sai hoặc sửa đổi vỏ "
        "nào cũng có thể làm tổn hại tính toàn vẹn của nó và cuối cùng gây hỏng hóc thảm khốc cho hệ "
        "thống. Mọi vỏ đều phải được nối đất chắc chắn và dán nhãn đúng, kèm một biển cảnh báo nhắc "
        "người vận hành tầm quan trọng của việc cắt điện nguồn vào vỏ trước khi bảo dưỡng."))

    # ------------------------------------------------------------ 100.4
    b.append(h2("100.4 Các phương pháp bảo vệ", "Protection Methodologies"))
    b.append(p(
        "Chọn một kỹ thuật bảo vệ phù hợp cho từng ứng dụng có vẻ phức tạp, vì phải cân nhắc đồng thời "
        "các yếu tố an toàn, độ tin cậy, chi phí và bảo trì. Qua nhiều năm, chỉ một số ít phương pháp "
        "bảo vệ an toàn cho khu vực nguy hiểm được dùng. Tuy khác nhau về ứng dụng và nguyên lý hoạt "
        "động, chúng đều có một điểm chung: loại bỏ một hoặc nhiều thành phần cần thiết cho sự cháy. "
        "Ba phương pháp được dùng rộng rãi nhất là:"))
    b.append(ol(["An toàn nội (intrinsic safety),", "Chống nổ (explosion-proof),",
                 "Thổi rửa và tạo áp suất (purging and pressurization)."]))

    b.append(h3("An toàn nội", "Intrinsic Safety"))
    b.append(p(
        "Nói gọn, an toàn nội (IS) là tất cả về việc ngăn ngừa nổ. IS dựa trên nguyên lý giới hạn mức "
        "năng lượng nhiệt và năng lượng điện trong khu vực nguy hiểm xuống những mức không thể mồi "
        "một hỗn hợp nguy hiểm cụ thể ở nồng độ dễ mồi nhất của nó. IS liên quan tới nhiệt độ mồi nhỏ "
        "nhất và năng lượng điện mồi nhỏ nhất cần để mồi một nhóm cụ thể. Mức năng lượng do một mạch "
        "IS cung cấp là thấp (khoảng 1 W) và chỉ dùng để cấp nguồn cho những thiết bị có nhu cầu năng "
        "lượng thấp. Một mạch IS bao gồm một thiết bị an toàn nội (thiết bị trường), một thiết bị liên "
        "hợp, và một hệ thống dây dẫn liên kết."))
    b.append(p(
        "Việc thiết kế hệ an toàn nội bắt đầu bằng việc nghiên cứu thiết bị trường. Điều này giúp xác "
        "định loại thiết bị liên hợp có thể dùng, sao cho mạch hoạt động đúng trong điều kiện vận hành "
        "bình thường mà vẫn an toàn trong điều kiện sự cố. Thiết bị trường có thể là loại đơn giản, "
        "như đầu đo nhiệt điện trở (RTD), cặp nhiệt điện, công tắc cơ khí, công tắc tiệm cận, điốt "
        "phát quang (LED); hoặc loại không đơn giản, như bộ chuyển đổi tín hiệu, van điện từ và rơle. "
        "Một thiết bị trường được coi và công nhận là “thiết bị đơn giản” nếu các giá trị tích trữ "
        "hoặc sinh năng lượng của nó không vượt quá 1,2 V, 0,1 A, 25 mW (hoặc 20 mJ) trong một hệ an "
        "toàn nội ở điều kiện bình thường hoặc bất thường."))
    b.append(p(
        "Thiết bị đơn giản có thể được nối vào một mạch an toàn nội mà không cần chứng nhận hay phê "
        "duyệt thêm. Việc những thiết bị này không có khả năng tích trữ hoặc sinh ra mức năng lượng "
        "cao không có nghĩa là chúng có thể được lắp trong khu vực nguy hiểm mà không cần sửa đổi gì. "
        "Chúng luôn phải được dùng cùng một thiết bị liên hợp để giới hạn lượng năng lượng trong khu "
        "vực nguy hiểm, vì một sự cố ở bên ngoài khu vực nguy hiểm có thể làm rò vào khu vực nguy "
        "hiểm một mức năng lượng đủ cao. Một thiết bị không đơn giản (ví dụ rơle, bộ chuyển đổi tín "
        "hiệu) có khả năng sinh và tích trữ mức năng lượng vượt các giá trị vừa nêu. Những thiết bị "
        "ấy cần được đánh giá và phê duyệt theo khái niệm thực thể (trình bày ở phần sau) để được "
        "dùng cùng một mạch an toàn nội. Theo khái niệm thực thể, những thiết bị này có các tham số "
        "thực thể sau: V<sub>max</sub> (điện áp lớn nhất cho phép), I<sub>max</sub> (dòng điện lớn "
        "nhất cho phép), C<sub>i</sub> (điện dung nội) và L<sub>i</sub> (điện cảm nội). Trong điều "
        "kiện sự cố, điện áp và dòng điện phải được giữ dưới V<sub>max</sub> và I<sub>max</sub> của "
        "thiết bị để tránh nhiệt thừa hoặc tia lửa — những thứ có thể là tai hoạ trong khu vực nguy "
        "hiểm. C<sub>i</sub> và L<sub>i</sub> cho biết khả năng tích trữ năng lượng của thiết bị dưới "
        "dạng điện dung nội và điện cảm nội, và giá trị của chúng phải nhỏ hơn C<sub>a</sub> và "
        "L<sub>a</sub> của thiết bị liên hợp (Bảng 100.3)."))
    hd, rows, cap = _t1003("vi")
    b.append(table(hd, rows, cap, " entity"))
    b.append(p(
        "Một thiết bị liên hợp (Hình 100.1), còn gọi là rào an toàn, là thiết bị hạn chế năng lượng "
        "cần thiết để bảo vệ một thiết bị trường nằm trong khu vực nguy hiểm khỏi nhận điện áp hoặc "
        "dòng điện quá mức. Thiết bị liên hợp thường được đặt trong một vỏ kín bụi và ẩm (NEMA 4) nằm "
        "trong khu vực không nguy hiểm, càng gần khu vực nguy hiểm càng tốt để giảm hiệu ứng điện "
        "dung của cáp. Nếu đặt trong khu vực nguy hiểm, thiết bị liên hợp phải được đặt trong một vỏ "
        "chống nổ (ví dụ NEMA 7D)."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Hình 100.1 cho thấy ba thành phần chính của một rào an toàn Zener. (Cần lưu ý rằng còn có "
        "những loại rào khác, như loại cách ly và loại lặp.) Các thành phần ấy là:"))
    b.append(ol([
        "Điện trở, có tác dụng giới hạn dòng điện ở một giá trị xác định gọi là dòng ngắn mạch "
        "(I<sub>sc</sub>).",
        "Cầu chì, đóng vai trò thiết bị ngắt hoặc thiết bị bảo vệ trong trường hợp điốt hỏng (cầu chì "
        "sẽ đứt nếu điốt dẫn điện).",
        "Điốt Zener, có tác dụng giới hạn điện áp ở một giá trị xác định gọi là điện áp hở mạch "
        "(V<sub>oc</sub>).",
    ]))
    b.append(p(
        "Điốt Zener có một điểm độc đáo là khả năng dẫn dòng khi phân cực ngược. Khi đặt điện áp lên "
        "điốt Zener theo chiều ngược, một lượng nhỏ dòng điện gọi là dòng rò đi qua. Dòng này vẫn nhỏ "
        "cho tới khi điện áp phân cực vượt quá điện áp đánh thủng Zener. Vượt quá điện áp đánh thủng "
        "làm cho điện trở vốn rất lớn của điốt Zener tụt xuống một giá trị rất nhỏ, nhờ đó dòng điện "
        "tăng vọt. Sự tăng dòng đột ngột ấy buộc điốt Zener trở thành vật dẫn, và do đó chuyển phần "
        "điện áp dư xuống đất. Nếu dòng điện tiếp tục chảy vượt quá trị số định mức của cầu chì, cầu "
        "chì sẽ đứt và mạch bị ngắt hoàn toàn. Hầu hết rào an toàn có ít nhất hai điốt mắc song song "
        "để bảo đảm mức bảo vệ tối đa khi một điốt hỏng (an toàn dự phòng)."))
    b.append(p(
        "Năm 1988, ANSI/UL 913 [5] cho phép dùng rào an toàn nội có cầu chì thay thế được, với điều "
        "kiện: “nếu cầu chì tiếp cận được để thay thế, thì cầu chì trên rào dùng điốt mắc song song có "
        "bảo vệ bằng cầu chì không được phép thay bằng loại có trị số cao hơn”. Các cầu chì được đặt "
        "trong những cụm không thể sửa đổi để tránh nhầm lẫn hoặc dùng sai. Các điốt có trị số công "
        "suất xác định và không được vượt quá. Điốt Zener và cầu chì chịu sự chi phối của một bộ tham "
        "số rất cụ thể, cho phép cầu chì làm việc ở một phần ba trị số công suất của điốt Zener và "
        "tránh hư hại không hồi phục cho điốt. Trị số công suất của điốt Zener được xác định như sau:"))
    b.append(eq("Z<sub>w</sub> = 1,5 × V<sub>oc</sub> × 2 × I<sub>f</sub>"))
    b.append(p("trong đó:"))
    b.append(ol([
        "Z<sub>w</sub> — trị số công suất nhỏ nhất của điốt Zener;",
        "V<sub>oc</sub> — điện áp hở mạch lớn nhất của điốt Zener;",
        "I<sub>f</sub> — trị số dòng định mức của cầu chì.",
    ]))
    b.append(p(
        "Việc chọn rào tốt nhất cho ứng dụng phụ thuộc vào thiết bị trường và đòi hỏi phân tích để bảo "
        "đảm mạch an toàn nội hoạt động đúng trong điều kiện bình thường hoặc bất thường. Ba đặc tính "
        "quan trọng nhất cần xem xét là (1) điện trở nội, (2) điện áp định mức và (3) cực tính của "
        "mạch. Dù chọn rào nào, mỗi rào đều có một điện trở nội (R<sub>i</sub>) giới hạn dòng ngắn "
        "mạch trong điều kiện sự cố. Khi dòng điện đi qua R<sub>i</sub>, nó tạo ra một sụt áp trên rào "
        "mà phải được tính đến (V = IR). Điện áp định mức của rào an toàn phải bằng hoặc cao hơn điện "
        "áp nguồn một cách hợp lý. Chữ “hợp lý” ở đây có ý nghĩa: điện áp nguồn quá cao có thể làm "
        "điốt dẫn điện, đẩy dòng lớn qua cầu chì và làm đứt cầu chì. Dùng nguồn ổn áp có thể giảm "
        "đáng kể những vấn đề gắn với điện áp nguồn quá cao. Để hoàn tất phân tích, phải xác lập cực "
        "tính của mạch. Rào xoay chiều có thể đấu với nguồn dương hoặc âm, còn rào một chiều có thể "
        "được định mức cho chiều dương hoặc chiều âm."))

    b.append(h3("Làm cho thiết bị trường trở thành an toàn nội",
                "Making Field Devices Intrinsically Safe"))
    b.append(p(
        "RTD và cặp nhiệt điện có thể được làm thành an toàn nội bằng cách dùng bộ chuyển đổi nhiệt độ "
        "cách ly (ITC), có tác dụng chuyển một tín hiệu một chiều mức thấp từ thiết bị trường thành "
        "tín hiệu 4–20 mA tỉ lệ. Những ITC này không cần nối đất để mạch IS hoạt động an toàn và đúng. "
        "Do khả năng tích trữ năng lượng, các bộ chuyển đổi tín hiệu được coi là thiết bị không đơn "
        "giản và phải được phê duyệt là an toàn nội. Nếu chúng đã được bên thứ ba phê duyệt thì vẫn "
        "phải xem xét cẩn thận các tham số thực thể của chúng. Các bộ chuyển đổi tín hiệu (4–20 mA) "
        "chuyển những đại lượng vật lý đo được trong khu vực nguy hiểm, như áp suất và lưu lượng, "
        "thành tín hiệu điện có thể truyền tới một bộ điều khiển trong khu vực an toàn. Tuỳ điều kiện, "
        "tín hiệu 4–20 mA có thể được làm thành an toàn nội bằng cách dùng rào loại lặp, có tác dụng "
        "nhân bản tín hiệu ra để khớp với tín hiệu vào. Rào lặp có thể nối đất hoặc không nối đất. Rào "
        "lặp không nối đất được gọi là “rào cách ly bằng biến áp”, vì điện áp hoặc tín hiệu vào được "
        "cách ly hoàn toàn khỏi điện áp hoặc tín hiệu ra nhờ một biến áp. Các đầu vào số, như công tắc "
        "cơ khí và công tắc tiệm cận — vốn là thiết bị đơn giản — có thể được làm thành an toàn nội "
        "bằng cách dùng bộ khuếch đại công tắc. Bộ khuếch đại công tắc chỉ đơn giản là một rơle hoặc "
        "một bộ ghép quang (một rơle tốc độ cao dùng cách ly quang giữa đầu vào và đầu ra), có tác "
        "dụng chuyển một tín hiệu rời rạc (ví dụ đóng/ngắt) từ khu vực nguy hiểm sang khu vực an toàn."))
    b.append(p(
        "Rào an toàn nối đất là những thiết bị thụ động được thiết kế riêng để ngăn năng lượng quá mức "
        "ở khu vực không nguy hiểm tiếp cận khu vực nguy hiểm. Những rào này có thể dùng với hầu hết "
        "thiết bị trường. Để loại rào ấy hoạt động đúng, nhất thiết phải có một mối nối đất vững chắc, "
        "tổng trở thấp (&lt; 1 Ω), nhằm tránh vòng đất và điện áp cảm ứng — những thứ có thể cản trở "
        "hoạt động của hệ thống."))

    b.append(h3("Đường cong mồi", "Ignition Curves"))
    b.append(p(
        "Mọi mạch điện đều có những đặc tính điện nhất định, có thể xếp vào ba loại: điện trở, điện "
        "cảm và điện dung. Ở một mức độ nào đó, mọi mạch đều có cả ba đặc tính này. Tuy vậy, một số "
        "đặc tính có thể nhỏ tới mức tác dụng của chúng không đáng kể so với các đặc tính khác, và vì "
        "thế có những cách gọi “mạch điện trở”, “mạch điện cảm”, “mạch điện dung”. Vì khái niệm IS dựa "
        "trên nguyên lý rằng một dòng điện lớn có thể gây nổ trong khu vực nguy hiểm còn sự thiếu vắng "
        "nó thì không, nên cần xác định những dải dòng điện an toàn và những dải nguy hiểm."))
    b.append(p(
        "Một lượng năng lượng điện như thế nào là nguy hiểm? Câu trả lời nằm ở các đường cong mồi. "
        "Đường cong mồi được công bố trong hầu hết tiêu chuẩn IS, như ANSI/UL 913 [5]. Ba đường cong "
        "được tham chiếu nhiều nhất được trình bày ở Hình 100.2. Các đường cong cho biết lượng năng "
        "lượng cần thiết để mồi những hỗn hợp khí quyển nguy hiểm khác nhau ở nồng độ dễ mồi nhất của "
        "chúng. Nồng độ dễ mồi nhất được xác định bằng cách tính phần trăm thể tích trên không khí nằm "
        "giữa giới hạn nổ trên và giới hạn nổ dưới của một hỗn hợp khí quyển nguy hiểm cụ thể. Trong "
        "ba đường cong được dẫn, những mức năng lượng (điện áp và dòng điện) nằm dưới đường cong của "
        "một nhóm không đủ để mồi nhóm ấy."))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Vì nhiệt độ mồi cụ thể liên quan trực tiếp tới lượng điện áp và dòng điện tiêu thụ, cả "
        "V<sub>oc</sub> và I<sub>sc</sub> của rào an toàn đều phải nhỏ hơn V<sub>max</sub> và "
        "I<sub>max</sub>. Khi thiết kế một hệ an toàn nội, phải tính đến điện trở cáp R (Ω/m), điện "
        "cảm L (µH/m) và điện dung C (pF/m) — những đại lượng vốn phân bố dọc theo chiều dài cáp. Có "
        "thể lấy điện dung và điện cảm từ tài liệu của nhà chế tạo cáp. Nếu không có các tham số này, "
        "có thể dùng một số giá trị mặc định theo NFPA 493/78 (A-4-2): C<sub>c</sub> = 200 pF/m "
        "(60 pF/ft) và L<sub>c</sub> = 0,66 µH/m (0,2 µH/ft). Để xác định chiều dài đi dây lớn nhất "
        "cần thiết nhằm bảo đảm hoạt động đúng, phải tính điện dung và điện cảm."))
    b.append(p(
        "Một cách tiếp cận phổ biến dùng “tham số tập trung”, trong đó điện áp và dòng điện của cả "
        "thiết bị an toàn nội lẫn thiết bị an toàn nội liên hợp được so sánh và ghép theo các phương "
        "trình (100.1) và (100.2). Bất kỳ sai lệch nào so với (100.1) hoặc (100.2) đều có thể làm tổn "
        "hại tính toàn vẹn của hệ thống và tạo ra những điều kiện nguy hiểm. Cũng phải xét và kiểm "
        "chứng các phần phản kháng của hệ để chứng minh rằng thiết bị trường cùng dây dẫn hiện trường "
        "không vượt quá các giá trị C<sub>a</sub> và L<sub>a</sub> của thiết bị liên hợp, như thể hiện "
        "ở các phương trình (100.3) và (100.4). Cách này tuy đơn giản và hiệu quả nhưng có xu hướng "
        "phóng đại hiệu ứng điện dung và điện cảm của dây dẫn, điều có thể thành hạn chế trong một số "
        "ứng dụng."))
    b.append(p(
        "Một cách khác tận dụng quan hệ giữa điện trở và điện cảm của cáp. Có thể dùng cách này nếu tỉ "
        "số L/R của thiết bị liên hợp cao hơn tỉ số L/R tính được của cáp. Trong điều kiện đó, có thể "
        "bỏ qua giá trị D<sub>a</sub> nhỏ hơn (khoảng cách cho phép lớn nhất) và kéo dài chiều dài cáp "
        "tới giá trị D<sub>a</sub> lớn hơn. Cách này linh hoạt hơn khi chiều dài cáp là vấn đề. Hình "
        "100.3 và ví dụ dưới đây minh hoạ các cách ấy."))
    b.append(fig(3, F.fig(3)))
    b.append(p("<b>Phương pháp tham số tập trung:</b>"))
    b.append(eq("V<sub>oc</sub> ≤ V<sub>max</sub>", "100.1"))
    b.append(eq("I<sub>sc</sub> ≤ I<sub>max</sub>", "100.2"))
    b.append(eq("C<sub>c</sub> ≤ C<sub>a</sub> − C<sub>i</sub> = 0,45 µF − 0,30 µF = 0,15 µF", "100.3"))
    b.append(eq("L<sub>c</sub> ≤ L<sub>a</sub> − L<sub>i</sub> = 3,5 mH − 2,0 mH = 1,5 mH", "100.4"))
    b.append(p(
        "Chiều dài lớn nhất của dây dẫn hiện trường, xét theo điện dung và điện cảm, là giá trị nhỏ "
        "hơn của D<sub>a</sub>:"
        "<br>D<sub>a</sub> = 0,15 µF / 150 pF/m = 1000 m"
        "<br>D<sub>a</sub> = 1,5 mH / 2,0 µH/m = 750 m (khoảng cách lớn nhất của dây dẫn hiện trường)."))
    b.append(p(
        "<b>Phương pháp tỉ số L/R:</b> Vì tỉ số L/R của cáp là 41,7 µH/Ω (2 µH/m ÷ 48 Ω/km), nhỏ hơn "
        "tỉ số L/R đã cho của thiết bị liên hợp (60 µH/Ω), nên có thể bỏ qua hiệu ứng điện cảm và tăng "
        "khoảng cách lớn nhất lên 1000 m."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản in có vài chỗ sai đơn vị do chế bản, ở đây đã sửa cho nhất "
        "quán với chính kết quả số mà bản in đưa ra: (a) tham số dây dẫn trong Hình 100.3 là "
        "L = 2,0 µH/m chứ không phải mH/m — với µH/m thì 1,5 mH ÷ 2,0 µH/m = 750 m, đúng như bản in; "
        "(b) tỉ số L/R của cáp là 41,7 µH/Ω, không phải mH/Ω; (c) giá trị mặc định của NFPA 493/78 là "
        "L<sub>c</sub> = 0,66 µH/m (0,2 µH/ft); (d) trong Bảng 100.1, dòng 165 °C/329 °F mang ký hiệu "
        "T3B, không phải T2B (T2B là 260 °C/500 °F và đã có ở dòng trên); (e) xác suất nổ ở phần Ưu "
        "điểm là 10<sup>−18</sup>. Ngoài ra, phương trình Z<sub>w</sub> không được đánh số trong bản "
        "in, và ở đây giữ nguyên như vậy để không lệch các số hiệu (100.1)–(100.4) mà nguyên bản dùng "
        "cho bốn phương trình tham số tập trung."))

    b.append(h3("Chứng nhận và phê duyệt", "Certification and Approval"))
    b.append(p(
        "Tuy các quá trình phê duyệt và chứng nhận góp phần bảo đảm an toàn, việc lập kế hoạch, thiết "
        "kế và tính toán kỹ thuật cẩn thận vẫn là điều cần thiết. Các tiêu chuẩn, thủ tục và thử nghiệm "
        "IS được công nhận trên toàn thế giới. Các cơ quan thử nghiệm gồm Underwriters Laboratories, "
        "Inc. (UL) và Factory Mutual Research Corp. (FM) ở Hoa Kỳ, Canadian Standards Association (CSA) "
        "ở Canada, và Physikalisch-Technische Bundesanstalt (PTB) ở châu Âu. Sản phẩm an toàn nội phù "
        "hợp cho mọi Cấp, Division và Nhóm nêu ở Bảng 100.2. Cần nhấn mạnh rằng sản phẩm an toàn nội "
        "phải được định mức và phân loại cho từng ứng dụng cụ thể (Cấp, Division và Nhóm). Ở Hoa Kỳ, "
        "FM áp dụng hai phương pháp thử nghiệm và phê duyệt thiết bị dùng trong khu vực nguy hiểm:"))
    b.append(ol([
        "<b>Phê duyệt theo vòng (hệ thống):</b> thiết bị an toàn nội được đánh giá cùng với một thiết "
        "bị liên hợp cụ thể và được phê duyệt để lắp đặt theo cách ấy. Mọi thay đổi trong mạch đều "
        "đòi hỏi đánh giá lại và chứng nhận lại (Hình 100.4).",
        "<b>Phê duyệt theo thực thể:</b> thiết bị an toàn nội và thiết bị liên hợp được đánh giá riêng "
        "và mỗi bên được cấp các tham số thực thể điện của mình (Hình 100.5). Việc áp dụng đúng là "
        "ghép các tham số thực thể như ở Bảng 100.3. Khi xem xét tính an toàn của một mạch, điều "
        "then chốt là so sánh các giá trị thực thể của thiết bị an toàn nội với thiết bị liên hợp. "
        "Hầu hết rào an toàn được phê duyệt theo thực thể cho mọi khu vực nguy hiểm.",
    ]))
    b.append(p(
        "Vì hầu hết thiết bị trường có khả năng tích trữ năng lượng, chúng phải có phê duyệt theo vòng "
        "hoặc theo thực thể thì mới bảo đảm kết cấu và hoạt động đúng của một hệ an toàn nội."))
    b.append(fig(4, F.fig(4)))
    b.append(fig(5, F.fig(5)))
    b.append(p("Các kỹ sư IS thường chủ trương dùng thiết bị an toàn nội vì những lý do sau:"))
    b.append(ol([
        "<b>An toàn.</b> Không thể xảy ra nổ trong một hệ an toàn nội dưới bất kỳ điều kiện vận hành "
        "nào. Thiết bị IS làm việc ở mức công suất thấp hơn và ngăn được điện giật, nhiệt năng thừa "
        "và phóng hồ quang — những thứ mà trong các hệ khác và các tình huống khác nhau có thể gây "
        "nguy hiểm.",
        "<b>Độ tin cậy.</b> Các linh kiện và cụm lắp ráp của mạch an toàn nội được thử độ tin cậy "
        "trước khi được dán nhãn và chứng nhận. Hầu hết thiết bị an toàn nội được thiết kế với mạch "
        "chuyên dụng để chống xung và ngăn các gai và quá độ.",
        "<b>Dễ sử dụng và lắp đặt.</b> Hệ an toàn nội có xu hướng nhỏ gọn và không cần những phụ kiện "
        "cồng kềnh, đắt tiền như vỏ, khớp bịt và ống dẫn kim loại cứng — những thứ làm tăng vốn đầu "
        "tư ban đầu.",
        "<b>Kinh tế.</b> Ở một số nơi trên thế giới, các cơ sở có điều kiện nguy hiểm phải mua loại "
        "bảo hiểm trách nhiệm đặc biệt. Khi lắp đặt đúng mạch và thiết bị an toàn nội, xác suất nổ là "
        "10<sup>−18</sup> [8], tức gần như không tồn tại; do đó phí bảo hiểm có xu hướng thấp hơn.",
        "<b>Bảo trì.</b> Thiết bị có thể được hiệu chuẩn và bảo trì mà không cần cắt điện, nhờ đó giảm "
        "thời gian dừng máy.",
    ]))
    b.append(p(
        "Việc đi dây hệ an toàn nội giống như mọi ứng dụng khác, nhưng để bảo đảm một hệ vận hành "
        "đúng, phải tuân thủ nghiêm ngặt một số hướng dẫn về nhận diện và tách ly. Mọi thành phần an "
        "toàn nội — kể cả cầu đấu, dây dẫn và thiết bị an toàn nội — đều phải được đánh dấu và dán "
        "nhãn rõ ràng. Màu quy ước dùng để nhận diện thiết bị an toàn nội là màu xanh lam. Trong một "
        "hệ đi dây hở, dây dẫn an toàn nội phải được tách vật lý khỏi dây dẫn không an toàn nội ít "
        "nhất 50 mm (2 in.), để điện áp cảm ứng không vô hiệu hoá mục đích của IS. Khi dây dẫn an toàn "
        "nội nằm trong một máng, máng phải được dán nhãn “Intrinsically Safe Circuits” (mạch an toàn "
        "nội). Không được đặt dây dẫn an toàn nội chung với dây dẫn không an toàn nội. Khi dùng máng "
        "cáp, có thể dùng một vách ngăn bằng thép tấm nối đất làm phương tiện tách ly được chấp nhận. "
        "Khi dây dẫn an toàn nội và không an toàn nội cùng nằm trong một vỏ, phải duy trì khoảng cách "
        "50 mm (2 in.). Ngoài ra phải có một vách ngăn kim loại nối đất để ngăn sự tiếp xúc của bất kỳ "
        "dây dẫn nào có thể bị lỏng ra."))
    b.append(p(
        "Sự xuống cấp cách điện của dây dẫn an toàn nội thuộc các mạch khác nhau cùng nằm trong một "
        "máng hoặc một vỏ có thể gây hại cho hoạt động của hệ thống. Dây dẫn an toàn nội phải có cấp "
        "cách điện chịu được điện áp thử xoay chiều 550 V hiệu dụng (rms), hoặc hai lần điện áp vận "
        "hành của mạch an toàn nội. Dây dẫn không an toàn nội nằm cùng vỏ với dây dẫn an toàn nội phải "
        "có cấp cách điện chịu được điện áp thử xoay chiều 2U + 1000 V, tối thiểu 1500 V rms, trong đó "
        "U là tổng các giá trị hiệu dụng điện áp của các dây dẫn an toàn nội. Một thực hành phổ biến và "
        "rất được khuyến nghị là dùng những ngăn riêng cho dây dẫn an toàn nội và không an toàn nội."))
    b.append(p(
        "Ngoài việc tách ly vật lý giữa dây dẫn an toàn nội và không an toàn nội, việc bịt kín ống dẫn "
        "và máng chứa dây dẫn an toàn nội là điều thiết yếu để ngăn khí, hơi và bụi đi từ khu vực nguy "
        "hiểm sang khu vực không nguy hiểm. Theo NEC, các khớp bịt không bắt buộc phải chống nổ. Khi "
        "một thiết bị liên hợp được đặt trong vỏ chống nổ ở khu vực nguy hiểm, các khớp bịt phải chống "
        "nổ. Tuy quy phạm không bắt buộc, việc lắp khớp bịt chống nổ trên các ống dẫn chứa dây dẫn an "
        "toàn nội vẫn là một thực hành kỹ thuật tốt, như Hình 100.6 minh hoạ."))
    b.append(fig(6, F.fig(6)))

    b.append(h3("Cơ sở của thiết kế chống nổ", "Explosion-Proof Fundamentals"))
    b.append(p(
        "Thiết kế chống nổ là một khái niệm cơ khí, dựa nhiều vào kết cấu cơ khí của vỏ và vào dung sai "
        "hẹp giữa các mối nối, ren và mặt bích, để chứa, làm nguội và thoát một cách an toàn mọi vụ nổ "
        "bên trong có thể xảy ra. Theo định nghĩa, vỏ chống nổ phải ngăn được việc mồi các khí hoặc "
        "hơi cháy nổ có thể bao quanh nó (chỉ với vỏ kiểu 7 và kiểu 10). Trong khu vực nguy hiểm Cấp I, "
        "Division 1 và 2, các thiết bị phát hồ quang như công tắc, côngtắctơ và bộ khởi động động cơ "
        "phải được đặt trong một vỏ chống nổ được định mức riêng cho khu vực ấy. Trái với niềm tin phổ "
        "biến, vỏ chống nổ không kín hơi và cũng không nên kín hơi. Nói ngắn gọn: một vụ nổ bên trong "
        "vỏ phải được ngăn không cho khởi phát một vụ nổ lớn hơn ở bên ngoài vỏ. Khác với IS, vỏ chống "
        "nổ giải quyết vấn đề áp suất bên trong lớn nhất (xem vỏ NEMA kiểu 7). Hình 100.7 minh hoạ kết "
        "cấu chắc chắn của một bảng điện chống nổ tiêu chuẩn."))
    b.append(p(
        "Ngoài độ bền và độ chắc, vỏ chống nổ còn phải “kín lửa”. Các mối nối hoặc mặt bích phải được "
        "giữ trong dung sai hẹp để cho phép làm nguội khí nóng sinh ra từ các vụ nổ bên trong. Nhờ vậy, "
        "nếu có khí thoát ra bầu khí quyển nguy hiểm bên ngoài thì khí ấy đã đủ nguội để không gây mồi."))
    b.append(p(
        "Vỏ chống nổ có xu hướng cồng kềnh (khiến chúng dễ nhận ra) và nặng, đòi hỏi khớp bịt ống dẫn "
        "và thao tác cẩn thận. Khác với thiết bị an toàn nội, thiết bị chống nổ làm việc ở mức công "
        "suất bình thường — điều cần thiết do nhu cầu công suất cao của một số mạch và thiết bị. Với "
        "thiết bị, lắp đặt và bảo trì đúng, vỏ chống nổ có thể phân phối điện áp và công suất lớn vào "
        "khu vực nguy hiểm một cách an toàn và hiệu quả."))
    b.append(p(
        "Ở nơi có lượng bụi có thể bị mồi, vỏ chứa thiết bị điện phải chống mồi bụi. Những vỏ này phải "
        "ngăn bụi cháy được xâm nhập, đồng thời ngăn hồ quang, tia lửa hoặc nhiệt sinh ra bên trong "
        "mồi lớp bụi bao quanh bên ngoài vỏ. Những vỏ này cũng phải tản nhiệt sinh ra bên trong một "
        "cách hiệu quả, vì nhiều loại bụi sẽ bắt lửa ở nhiệt độ tương đối thấp. Khác với vỏ chống nổ "
        "Cấp I, Division 1 (kiểu 7), vỏ chống mồi bụi Cấp II, Division 1 (kiểu 9) được thiết kế để "
        "ngăn ngừa nổ. Do đó, vỏ chống mồi bụi không cần chắc bằng hoặc có thành dày bằng vỏ chống nổ, "
        "vì sẽ không có vụ nổ bên trong nào."))
    b.append(fig(7, F.fig(7)))

    b.append(h3("Thổi rửa và tạo áp suất", "Purging and Pressurization"))
    b.append(p(
        "Phương pháp này cho phép thiết bị điện vận hành an toàn ở những nơi có điều kiện nguy hiểm và "
        "không thể áp dụng phương pháp nào khác, vì nhu cầu năng lượng cao là bắt buộc và vì kích "
        "thước vật lý thực tế. Điều này đúng với những động cơ lớn và những cụm thiết bị đóng cắt mà "
        "trên thị trường không có loại dành cho Cấp I, Nhóm A và B. Ngoài ra, phương pháp này còn được "
        "dùng khi các bảng điều khiển chứa thiết bị đo và thiết bị điện buộc phải đặt trong khu vực "
        "nguy hiểm. Thổi rửa và tạo áp suất là một phương pháp bảo vệ dựa vào việc cấp liên tục không "
        "khí sạch hoặc khí trơ (ví dụ nitơ) vào vỏ với lưu lượng đủ để giữ thiết bị nguội thích đáng "
        "và tạo áp suất bên trong đủ để ngăn bầu khí quyển cháy được tràn vào vỏ. Tuy vỏ không chống "
        "nổ, chúng phải tương đối kín hơi và phải đủ chắc để làm việc an toàn và đạt yêu cầu. Hệ thống "
        "gồm:"))
    b.append(ol([
        "<b>Nguồn không khí sạch (hoặc khí trơ):</b> việc nghiên cứu và phân tích cẩn thận có tầm quan "
        "trọng quyết định với quá trình này, vì không khí cấp vào phải tương đối không có tạp chất. "
        "Tìm một vị trí an toàn cho cửa hút gió đòi hỏi kỹ năng và sự khéo léo; nên tham khảo ý kiến "
        "một chuyên gia HVAC. Cũng phải xét các yếu tố khác như khối lượng riêng của hơi, vị trí, "
        "hướng gió và môi trường xung quanh. Khi dùng máy nén và quạt thổi để cấp khí nén, phải thận "
        "trọng khi chọn kích thước và vị trí máy nén hoặc quạt, nhằm đáp ứng yêu cầu lưu lượng khí mà "
        "không làm tổn hại mục tiêu chính là an toàn và độ tin cậy.",
        "<b>Thổi rửa:</b> một vỏ đã được tạo áp suất nhưng ngừng làm việc một thời gian có xu hướng "
        "tích tụ hỗn hợp cháy được. Trước khi cấp điện, khí trơ và áp suất dương phải cung cấp một "
        "thể tích không khí sạch ban đầu đủ lớn để giảm thiểu nồng độ của mọi hỗn hợp cháy được có "
        "thể hiện diện. Với những ứng dụng điển hình, lưu lượng bằng bốn lần thể tích bên trong của "
        "vỏ thường là đủ để giảm thiểu nồng độ hỗn hợp cháy có thể tồn tại. Với những ứng dụng khác "
        "thường, phải tính lưu lượng thể tích cẩn thận để bảo đảm quá trình thổi rửa thành công.",
        "<b>Tạo áp suất:</b> quá trình này dùng khái niệm chênh áp giữa bên ngoài và bên trong vỏ để "
        "giữ vật liệu dễ cháy không xâm nhập. Điều đó được thực hiện bằng cách duy trì áp suất bên "
        "trong vỏ cao hơn. Để vận hành an toàn, vỏ được bảo vệ phải liên tục được duy trì ở áp suất "
        "dương ít nhất 25 Pa (0,1 in. nước) [2] so với khí quyển xung quanh trong suốt thời gian thiết "
        "bị được bảo vệ làm việc.",
        "<b>Tín hiệu và cảnh báo:</b> khi mất áp suất dương, các cảnh báo và báo động là thiết yếu. Có "
        "thể dùng ba kiểu tạo áp suất và báo động, tuỳ tính chất điều khiển của vỏ và mức độ nguy "
        "hiểm bên ngoài. Ngoài ra, cần có liên động cửa để ngăn mở vỏ được bảo vệ khi mạch còn có "
        "điện.",
    ]))
    b.append(p("Theo NFPA 496, có ba kiểu tạo áp suất:"))
    b.append(ol([
        "<b>Kiểu X</b> — hạ phân loại bên trong vỏ được bảo vệ từ Division 1 xuống không phân loại. "
        "Trường hợp này thường liên quan tới một nguồn mồi được đặt trong một vỏ kín nằm trong bầu "
        "khí quyển nguy hiểm tiềm ẩn. Kiểu X đòi hỏi một phương tiện cắt (công tắc lưu lượng hoặc áp "
        "suất) để cắt điện hoàn toàn và tự động khỏi vỏ được bảo vệ ngay khi nguồn khí bảo vệ mất "
        "(mất áp suất hoặc mất lưu lượng). Phương tiện cắt ấy phải chống nổ hoặc an toàn nội, vì nó "
        "thường nằm trong khu vực nguy hiểm.",
        "<b>Kiểu Y</b> — hạ phân loại bên trong vỏ được bảo vệ từ Division 1 xuống Division 2. Vỏ được "
        "bảo vệ chứa thiết bị được định mức cho Division 2 và không tạo nguồn mồi; do đó không có mối "
        "nguy tức thời. Kiểu Y đòi hỏi một cảnh báo bằng mắt hoặc bằng âm thanh khi hệ thống hỏng. "
        "Một lưu ý: phải thiết lập các biện pháp bảo vệ để bảo đảm mọi trục trặc trong hệ thống không "
        "làm nhiệt độ bề mặt ngoài của vỏ vượt quá 80 % nhiệt độ mồi của hỗn hợp cháy được hiện diện.",
        "<b>Kiểu Z</b> — hạ phân loại bên trong vỏ được bảo vệ từ Division 2 xuống không phân loại. "
        "Kiểu Z đòi hỏi kích hoạt một cảnh báo bằng mắt hoặc bằng âm thanh nếu phát hiện việc không "
        "duy trì được áp suất dương hoặc lưu lượng bên trong vỏ được bảo vệ.",
    ]))
    b.append(p(
        "Nhận ra và hiểu những nguy hiểm tiềm ẩn gắn với việc dùng điện trong khu vực nguy hiểm là "
        "phần thiết yếu của việc chọn biện pháp bảo vệ tốt nhất. Với hầu hết ứng dụng, khi nhu cầu về "
        "năng lượng khác nhau, kỹ thuật bảo vệ nhiều khả năng sẽ là sự kết hợp của nhiều phương pháp "
        "và công nghệ chuyên dụng. Phân tích và khảo sát được thực hiện đúng cách có vẻ tốn thời gian "
        "và tiền bạc, nhưng với những ai sẵn lòng tuân thủ các hướng dẫn đã được thiết lập và những "
        "thực hành kỹ thuật vững chắc, quá trình ấy sẽ giúp bảo đảm mức tuân thủ cao nhất, đồng thời "
        "tiết kiệm đáng kể và ngăn được thiệt hại tài sản cùng thương tích."))

    # ------------------------------------------------------------ terms
    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(p(
        "<b>Điện cảm (inductance):</b> khả năng của một thiết bị điện tích trữ điện tích (năng lượng). "
        "Một cuộn cảm sẽ giải phóng năng lượng ấy khi mạch bị mở (bị ngắt)."))
    b.append(p(
        "<b>Oxy hoá (oxidation):</b> quá trình trong đó các ion mang điện tích âm (anion) mất điện tử "
        "tại anôt trong một quá trình điện hoá. Để trở nên trung hoà, các anion phải mất điện tử."))
    b.append(p(
        "<b>Đầu đo nhiệt điện trở (RTD):</b> thiết bị đo nhiệt độ dựa trên sự thay đổi điện trở."))
    b.append(p(
        "<b>Điốt Zener:</b> linh kiện bán dẫn phi tuyến, không dẫn dòng ở chế độ phân cực ngược cho tới "
        "khi đạt một điện áp tới hạn. Khi đó nó có thể dẫn dòng ở chế độ phân cực ngược mà không bị "
        "hỏng. Điốt Zener có đặc tính điện áp gần như không đổi trong vùng phân cực ngược (vùng làm "
        "việc thường lệ)."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "NFPA 70 (ANCI C1 — 1996), National Electrical Code 1996, Quincy, MA.",
        "National Fire Protection Association (NFPA), Articles 493, 496, 497, Quincy, MA.",
        "American Petroleum Institute 500 (RP 500), 1st ed., Washington, D.C., June 1991. "
        "Recommended Practice for Classification of Location for Electrical Installation at "
        "Petroleum Facilities.",
        "Elcon Instruments, Inc., Introduction to Intrinsic Safety, 3rd printing, Norcross, 1990.",
        "Underwriters Laboratories, Inc., Pub. UL 913, 4th ed., Northbrook, IL, 1988, Standard for "
        "Intrinsically Safe Apparatus &amp; Associated Apparatus for Use in Class I, II, III, "
        "Division 1 Hazardous Locations.",
        "Underwriters Laboratories, Inc., Pub. UL 508, Industrial Control Equipment.",
        "P. Babiarz, Cooper Industries, Crouse-Hinds, InTech Engineer's Notebook, Syracuse, NY, 1994.",
        "R. Stahl, Inc., RST 49, Comprehensive Applications and Data Catalog, Woburn, MA, 1992.",
        "J. Oudar, “Intrinsic safety,” J. Southern Calif. Meter Assoc., October 1981.",
        "W. Alexander, “Intrinsically safe systems,” InTech, April 1996.",
    ]))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []
    b.append(p(
        "Wherever a hazardous atmosphere can exist, electricity has to be a primary concern of the "
        "engineer and of the system designer. Such atmospheres are not confined to the familiar "
        "surroundings of industrial, chemical and environmental facilities; they occur in many less "
        "obvious places — where dust is present, where gas can accumulate, where reactions form "
        "combustible gases. Minimising the risk in those places means designing purpose-built, "
        "hazard-reducing electrical systems. Most electrical equipment is built to standards aimed at "
        "reducing fires and casualties, and the majority of incidents that do occur can be traced to "
        "poor or defective installation, misuse of approved equipment, deterioration, or accidental "
        "application. Combined with an explosive atmosphere, any of those can produce extremely "
        "dangerous conditions. Designing an electrical system for a hazardous location calls for "
        "careful planning, research, engineering and some ingenuity in applying the right protection "
        "techniques, so that better applications and classifications — and lower hazard — result."))

    b.append(h2("100.1 Introduction"))
    b.append(p(
        "The safety of people and equipment in a hazardous area should never be taken for granted. In "
        "1913 a massive methane explosion in a coal mine in Glamorganshire, South Wales, killed 439 "
        "miners. After months of study, a group of experts and scientists concluded that the "
        "explosion had been caused by a small amount of electrical energy stored in the circuit; that "
        "small energy, together with an explosive gas–air mixture and the absence of proper "
        "protection, proved fatal."))
    b.append(p(
        "Understanding the dangers of electrical equipment in hazardous areas starts with the "
        "basics. Chemically, oxidation, combustion and explosion are all exothermic reactions that "
        "differ only in the speed at which heat is released. For any of them to occur, three "
        "components must be present at once, in the right concentrations: (1) fuel, whether liquid, "
        "gas or solid; (2) enough oxygen, i.e. air; and (3) an ignition source, electrical or "
        "thermal."))
    b.append(p(
        "Potentially hazardous ignition sources include (1) hot surfaces — motor windings, heat-trace "
        "cable, luminaires; (2) electric sparks and arcs, as circuits are made and broken or as short "
        "circuits occur; (3) mechanical sparks from friction and grinding; (4) electrostatic "
        "discharge, a separation process in which at least one chargeable substance is present; and "
        "(5) radiation, compression and shock waves."))
    b.append(p(
        "Working with electrical equipment in hazardous locations requires familiarity with the "
        "following terms."))
    b.append(p(
        "<b>1. Flash point</b> — the lowest temperature at normal atmospheric pressure at which a "
        "combustible or flammable material releases enough vapour to be ignited by an energy source. "
        "By flash point (FP), flammable liquids fall into four hazard classes:"))
    b.append(ol([
        "AI (FP &lt; 21 °C),",
        "AII (21 °C &lt; FP &lt; 55 °C),",
        "AIII (55 °C &lt; FP &lt; 100 °C), and",
        "B (FP &lt; 21 °C when dissolved in water at 15 °C).",
    ]))
    b.append(p(
        "<b>2. Ignition temperature</b> — the lowest temperature at normal operating pressure at "
        "which a dangerous mixture ignites independently of the heating element or the heated "
        "element."))
    b.append(p(
        "<b>3. Flammable limits</b> — the upper explosive limit (UEL) is the highest vapour-to-air "
        "concentration ratio above which flame does not propagate when an ignition source is applied; "
        "such a mixture is “too rich” to burn. The lower explosive limit (LEL) is the lowest ratio "
        "below which flame does not propagate; such a mixture is “too lean” to explode. The LEL "
        "deserves particular attention because it gives the minimum quantity of gas needed to create "
        "a hazardous mixture. Flammable limits are normally quoted in percent by volume, % vol. A "
        "mixture midway between the UEL and the LEL explodes far more violently than one nearer "
        "either limit."))
    b.append(p(
        "<b>4. Maximum surface temperature</b> — the highest temperature a piece of electrical "
        "equipment produces under normal or fault conditions. It must stay below the lowest ignition "
        "temperature of the potentially explosive atmosphere around it. Equipment for hazardous "
        "locations must be marked with its class, group and maximum surface temperature (or range), "
        "referred to a 40 °C (104 °F) ambient. Table 100.1 shows that apparatus of a given T class "
        "may be used wherever the gases present have an ignition temperature above that class. For "
        "extra safety the maximum surface temperature is best kept below 80% of the lowest ignition "
        "temperature of the surrounding gas. Do not confuse maximum working (operating) temperature "
        "with maximum surface temperature, which is measured under the worst conditions of the "
        "apparatus: equipment rated for a 70 °C ambient must show a temperature rise no greater than "
        "a 10 °C safety margin to be classed T6, or 5 °C for T3, T4 and T5 (Table 100.1)."))
    hd, rows, cap = _t1001("en")
    b.append(table(hd, rows, cap))
    b.append(p(
        "<b>5. Vapour density</b> — the weight of a volume of pure vapour compared with the weight of "
        "an equal volume of dry air at the same normal pressure and temperature; numerically the "
        "ratio of the molecular weight of the gas to the average molecular weight of air (28.96). "
        "Methane (CH<sub>4</sub>), molecular weight 16 and vapour density 0.6, tends to rise; acetone "
        "(C<sub>3</sub>H<sub>6</sub>O), molecular weight 58 and vapour density 2, tends to settle near "
        "ground level."))
    b.append(p(
        "In the United States the National Electrical Code (NEC) defines a hazardous area as “an area "
        "where a potential hazard may exist under normal or abnormal conditions because of the "
        "presence of flammable, combustible or ignitable materials” [1]. That general description is "
        "broken down into classes, divisions and groups so that the extent of the hazard can be "
        "assessed properly and safe electrical systems designed and specified."))
    b.append(p(
        "Classification matters for economic as well as safety reasons. Proper application, good "
        "engineering and experience can confine the most volatile areas (Class I, Division 1) to "
        "reasonable distances around potential leaks and ignition sources. Inside Class I, Division 1 "
        "the equipment and installation cost becomes a burden, because the equipment is considerably "
        "more expensive and must pass stringent tests for correct, safe operation under normal and "
        "abnormal conditions. NFPA 497 A &amp; B [2] and ANSI/API RP 500 [3] are excellent sources for "
        "fixing the boundaries of a hazardous area."))

    b.append(h2("100.2 Fundamentals of Explosion Protection"))
    b.append(p(
        "Classifying a hazardous area is usually done by highly qualified people — chemical "
        "engineers, process engineers and safety officers — whose primary objective is to establish "
        "where a potentially hazardous atmosphere exists, under what conditions, and for how long. "
        "Careful study and design of the electrical installation is crucial to safe operation and to "
        "preventing the accidental ignition of flammable materials."))
    b.append(p(
        "The NEC, adopted by many states, agencies and companies as the basis for inspection, sets "
        "out the requirements and procedures for electrical installations in hazardous areas. "
        "Articles 500–504 cover equipment and wiring at all voltages where fire or explosion hazards "
        "may exist because of flammable gases or vapours, flammable liquids, combustible dust, or "
        "ignitable fibres and flyings."))
    b.append(p(
        "Table 100.2 describes hazardous locations by Class, Division and Group. The Class defines the "
        "physical form of the combustible material mixed with oxygen; the Division defines the "
        "probability that an explosive fuel–air mixture is present; the Group indicates the type of "
        "vapour or dust. The NEC gives the following definitions [1].*"))
    hd, rows, cap = _t1002("en")
    b.append(table(hd, rows, cap))

    b.append(h3("Class I, Division 1 Locations"))
    b.append(p(
        "1. Where ignitable concentrations of flammable gases or vapours can exist under normal "
        "operating conditions; may exist frequently because of repair or maintenance operations or "
        "because of leakage; and where breakdown or faulty operation of equipment or processes might "
        "release ignitable concentrations of flammable gases or vapours and cause simultaneous "
        "failure of electrical equipment."))

    b.append(h3("Class I, Division 2 Locations"))
    b.append(ol([
        "Where volatile flammable liquids or flammable gases are handled, processed or used, but "
        "where the liquids, vapours or gases are normally confined within closed containers or closed "
        "systems from which they can escape only on accidental rupture or breakdown of those "
        "containers or systems, or on abnormal operation of equipment;",
        "Where ignitable concentrations of gases or vapours are normally prevented by positive "
        "mechanical ventilation, and where they might become hazardous through failure or abnormal "
        "operation of the ventilating equipment;",
        "Adjacent to Class I, Division 1 locations, where ignitable concentrations of gases or "
        "vapours might occasionally be communicated — unless such communication is prevented by "
        "positive-pressure ventilation from a source of clean air, with effective safeguards against "
        "ventilation failure.",
    ]))

    b.append(h3("Class II, Division 1 Locations"))
    b.append(ol([
        "Where combustible dust is in the air under normal operating conditions in quantities "
        "sufficient to produce explosive or ignitable mixtures;",
        "Where mechanical failure or abnormal operation of machinery or equipment might cause such "
        "mixtures to be produced and might also provide a source of ignition through simultaneous "
        "failure of electrical equipment, operation of protective devices, or other causes;",
        "Where combustible dusts of an electrically conductive nature may be present in hazardous "
        "quantities.",
    ]))

    b.append(h3("Class II, Division 2 Locations"))
    b.append(p(
        "Where combustible dust is not normally in the air in quantities sufficient to produce "
        "explosive or ignitable mixtures, and dust accumulations are normally insufficient to "
        "interfere with the safe dissipation of heat from electrical equipment, or may be ignitable "
        "by abnormal operation or failure of that equipment."))

    b.append(h3("Class III, Division 1 Locations"))
    b.append(p(
        "Where easily ignitable fibres or materials producing combustible flyings are handled, "
        "manufactured or used."))

    b.append(h3("Class III, Division 2 Locations"))
    b.append(p(
        "Where easily ignitable fibres are stored or handled. The quantities and properties of the "
        "hazardous materials are the basis on which the NEC classifies locations; every location must "
        "be evaluated carefully so that the right classification, and therefore the right equipment, "
        "follows."))
    b.append(note(
        "* Reprinted with permission from NFPA 70-1996, the National Electrical Code®, © 1995 National "
        "Fire Protection Association, Quincy, MA 02269. This reprinted material is not the complete "
        "and official position of the NFPA on the referenced subject, which is represented only by "
        "the standard in its entirety. National Electrical Code® and NEC® are registered trademarks "
        "of the National Fire Protection Association, Inc., Quincy, MA 02269."))

    b.append(h2("100.3 Enclosure Types and Requirements"))
    b.append(p("Choosing the right enclosure matters for two reasons:"))
    b.append(ol([
        "Protecting personnel against accidental contact with enclosed electrical equipment.",
        "Protecting the internal equipment against outside harm.",
    ]))
    b.append(p(
        "Enclosures carry a type number indicating the degree of protection and the conditions for "
        "which they are suitable. Some applications need both, and the enclosure is then designated "
        "by a two-part number with the smaller first, e.g. 7/9. The types below, with their enclosed "
        "equipment, have been evaluated to Underwriters Laboratories UL 698, <i>Industrial Control "
        "Equipment for Use in Hazardous Locations</i>, and are marked with the class and group "
        "letters."))
    b.append(p(
        "<b>Type 7</b> — nonventilated, for indoor use, classified for Class I, Groups A, B, C and D "
        "as defined in Table 100.2; the letters A to D sometimes appear as a suffix. Under UL 698 a "
        "Type 7 enclosure must withstand the internal explosion pressure of specific gases and "
        "prevent that explosion from igniting a hazardous mixture outside the enclosure (explosion "
        "test). Sheet-steel Type 7 enclosures must additionally withstand twice the internal "
        "explosion pressure for 1 min without permanent deformation, and three times the pressure "
        "without rupture; cast-iron enclosures must withstand four times the pressure without rupture "
        "or deformation. The test may be waived where calculation shows a safety factor of five to "
        "one for cast metal, or four to one for fabricated steel. Enclosed heat-generating devices "
        "are designed so that external surfaces cannot reach temperatures able to ignite an explosive "
        "vapour–air mixture outside the enclosure (temperature test)."))
    b.append(p(
        "<b>Type 8</b> — nonventilated, for indoor use, for Class I, Groups A, B, C and D as in Table "
        "100.2, with the letters A to D as a suffix. Under UL 698 the oil-immersed equipment must "
        "operate at rated voltage and under the most severe current conditions in the presence of "
        "flammable gas–air mixtures without igniting them."))
    b.append(p(
        "<b>Type 9</b> — nonventilated, for indoor use, classified for Class II, Groups E, F and G as "
        "in Table 100.2, with E, F or G as a suffix. Under UL 698 the enclosure and its equipment are "
        "evaluated to the edition of UL 698 in force at the time of manufacture. That evaluation "
        "reviews the dimensional requirements for shaft openings and joints, the gasket material, and "
        "the temperature rise under a blanket of dust. The device runs at full rated load until "
        "equilibrium temperatures are reached, then cools to ambient over at least 30 h while "
        "continuously subjected to circulating dust of specified properties; no dust may enter the "
        "enclosure (dust penetration test). Type 9 enclosures must also pass the “temperature test "
        "with dust blanket”, like the temperature-rise test except that the circulating dust is not "
        "aimed directly at the device. Dust in contact with the enclosure must not ignite or discolour "
        "from heat, and the exterior surface temperature, based on 40 °C (104 °F), must not exceed the "
        "specified values under normal or abnormal conditions. Where gasketed enclosures are used the "
        "gaskets must be noncombustible, nondeteriorating and vermin-proof, and mechanically attached. "
        "Type 9 ventilated enclosures are as the nonventilated ones except that ventilation is forced "
        "air from outside the hazardous area, producing positive pressure inside the enclosure; the "
        "enclosure must still meet the temperature design test."))
    b.append(p(
        "<b>Type 10</b> — nonventilated, designed to meet the requirements of the U.S. Bureau of Mines "
        "for atmospheres containing mixtures of methane and air, with or without coal dust."))
    b.append(p(
        "Note that enclosures for hazardous applications are designed for specific applications and "
        "must be installed and maintained as the manufacturer recommends: any misapplication or "
        "alteration may jeopardise the integrity of the enclosure and eventually cause catastrophic "
        "failure of the system. Every enclosure should be solidly grounded and properly labelled with "
        "a warning that reminds the operator to de-energise the incoming supply before servicing."))

    b.append(h2("100.4 Protection Methodologies"))
    b.append(p(
        "Choosing a protection technique to suit each application looks complicated, because safety, "
        "reliability, cost and maintenance all have to be weighed. Over the years only a few "
        "methodologies have been used for hazardous areas. They differ in application and in "
        "principle, but they share one aim: to eliminate one or more of the components that "
        "combustion needs. The three most widely used are"))
    b.append(ol(["intrinsic safety,", "explosion-proof construction,",
                 "purging and pressurization."]))

    b.append(h3("Intrinsic Safety"))
    b.append(p(
        "Intrinsic safety (IS) is, simply stated, about preventing explosions. It rests on limiting "
        "the thermal and electrical energy in the hazardous area to levels that cannot ignite a "
        "specific hazardous mixture at its most ignitable concentration. IS is concerned with the "
        "minimum ignition temperature and the minimum ignition energy needed to ignite a given group. "
        "An IS circuit supplies a low energy level (about 1 W) and is used only to power instruments "
        "with a low energy demand. It comprises an intrinsically safe apparatus (the field device), an "
        "associated apparatus, and the interconnecting wiring."))
    b.append(p(
        "Design begins with the field device, because that determines which associated apparatus can "
        "be used so that the circuit works properly under normal conditions yet stays safe under "
        "fault. Field devices may be simple — resistance temperature devices (RTDs), thermocouples, "
        "mechanical switches, proximity switches, light emitting diodes — or nonsimple: transmitters, "
        "solenoid valves, relays. A field device counts as a “simple device” if its energy-storing or "
        "generating values do not exceed 1.2 V, 0.1 A, 25 mW (or 20 mJ) in an intrinsically safe "
        "system under normal or abnormal conditions."))
    b.append(p(
        "A simple device may be connected to an intrinsically safe circuit without further "
        "certification or approval. That it cannot store or generate high energy does not mean it may "
        "be installed in a hazardous area unmodified: it must always be used with an associated "
        "apparatus to limit the energy in the hazardous area, since a fault outside that area can leak "
        "enough energy in. A nonsimple device — a relay or a transmitter — can generate and store "
        "energy above those values and needs evaluation and approval under the entity concept "
        "(described below) before it may be used with an IS circuit. Under that concept such devices "
        "carry the entity parameters V<sub>max</sub> (maximum voltage allowed), I<sub>max</sub> "
        "(maximum current allowed), C<sub>i</sub> (internal capacitance) and L<sub>i</sub> (internal "
        "inductance). Under fault the voltage and current must stay below the apparatus's "
        "V<sub>max</sub> and I<sub>max</sub> to prevent excess heat or sparking, which can be "
        "disastrous in a hazardous area. C<sub>i</sub> and L<sub>i</sub> express the device's ability "
        "to store energy as internal capacitance and inductance, and must be less than the "
        "C<sub>a</sub> and L<sub>a</sub> of the associated apparatus (Table 100.3)."))
    hd, rows, cap = _t1003("en")
    b.append(table(hd, rows, cap, " entity"))
    b.append(p(
        "An associated apparatus (Figure 100.1), also called a safety barrier, is the energy-limiting "
        "device that protects a field device in the hazardous area from excessive voltage or current. "
        "It is normally installed in a dust- and moisture-free enclosure (NEMA 4) in the "
        "nonhazardous area, as close as possible to the boundary so that the capacitance of the cable "
        "is minimised. If it must sit in the hazardous area, it goes in an explosion-proof enclosure "
        "(e.g. NEMA 7D)."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Figure 100.1 shows the three major components of a Zener safety barrier (other kinds exist — "
        "isolation and repeater barriers among them):"))
    b.append(ol([
        "The resistor, which limits current to a specific value, the short-circuit current "
        "(I<sub>sc</sub>).",
        "The fuse, which interrupts the circuit should a diode fail — it blows if the diode conducts.",
        "The Zener diode, which limits voltage to a specific value, the open-circuit voltage "
        "(V<sub>oc</sub>).",
    ]))
    b.append(p(
        "Zener diodes are unusual in conducting under reverse bias. Applied in the reverse direction, "
        "a Zener passes a small leakage current, which stays small until the bias exceeds the Zener "
        "breakdown voltage. Beyond breakdown the inherently high resistance collapses to a very low "
        "value and the current rises abruptly; the diode becomes a conductor and diverts the excess "
        "voltage to ground. If the current continues above the fuse rating the fuse opens and the "
        "circuit is interrupted completely. Most barriers use at least two diodes in parallel so that "
        "one failure still leaves protection (redundant safety)."))
    b.append(p(
        "In 1988 ANSI/UL 913 [5] permitted barriers with replaceable fuses on these terms: “if it is "
        "accessible for replacement, the fuse on a fuse-protected shunt-diode barrier shall not be "
        "replaceable by one of higher rating.” The fuses sit in tamper-proof assemblies to prevent "
        "confusion or misapplication, and the diodes have power ratings that must not be exceeded. "
        "Zener diodes and fuses are governed by a specific set of parameters that let the fuse operate "
        "at one-third the power rating of the diode and avoid irreversible damage to it. The diode's "
        "power rating follows from"))
    b.append(eq("Z<sub>w</sub> = 1.5 × V<sub>oc</sub> × 2 × I<sub>f</sub>"))
    b.append(p("where Z<sub>w</sub> is the minimum power rating of the Zener diode, "
               "V<sub>oc</sub> the maximum Zener open-circuit voltage, and I<sub>f</sub> the fuse "
               "current rating."))
    b.append(p(
        "Selecting the best barrier for an application depends on the field device and requires "
        "analysis to ensure the IS circuit behaves correctly under normal and abnormal conditions. "
        "Three characteristics matter most: (1) internal resistance, (2) rated voltage and (3) circuit "
        "polarity. Whichever barrier is chosen, its internal resistance R<sub>i</sub> limits the "
        "short-circuit current under fault, and the current through R<sub>i</sub> creates a voltage "
        "drop across the barrier that must be accounted for (V = IR). The rated voltage of the barrier "
        "must equal, or reasonably exceed, the supply voltage — “reasonably”, because excessive supply "
        "voltage can make the diode conduct, driving a large current through the fuse and blowing it. "
        "A regulated supply greatly reduces the problems of excessive supply voltage. Completing the "
        "analysis means establishing the polarity: ac barriers can be connected to a positive or a "
        "negative supply, dc barriers are rated for one or the other."))

    b.append(h3("Making Field Devices Intrinsically Safe"))
    b.append(p(
        "RTDs and thermocouples become intrinsically safe through isolated temperature converters "
        "(ITCs), which turn the low dc signal of the field device into a proportional 4–20 mA signal. "
        "These converters need no ground connection for safe, correct operation of the IS circuit. "
        "Because they store energy, transmitters are nonsimple devices and must be approved as "
        "intrinsically safe; where they carry third-party approval their entity parameters still have "
        "to be examined carefully. Transmitters (4–20 mA) convert physical measurements in the "
        "hazardous area — pressure, flow — into electrical signals for a controller in a safe area. "
        "Depending on conditions, a 4–20 mA signal can be made intrinsically safe with a repeater "
        "barrier, which duplicates the output signal to match the input. Repeaters may be grounded or "
        "ungrounded; ungrounded repeaters are known as transformer-isolated barriers, because the "
        "incoming voltage or signal is fully isolated from the outgoing one by a transformer. Digital "
        "inputs — mechanical and proximity switches, both simple devices — become intrinsically safe "
        "through a switch amplifier, which is simply a relay or an optocoupler (a high-speed relay "
        "using optical isolation between input and output) that transfers a discrete on/off signal "
        "from the hazardous to the safe area."))
    b.append(p(
        "Grounded safety barriers are passive devices designed specifically to stop excess energy in a "
        "nonhazardous area from reaching a hazardous one. They suit most field devices, but they only "
        "work properly with a solid, low-impedance (&lt;1 Ω) connection to ground, which prevents the "
        "ground loops and induced voltages that would otherwise hinder the system."))

    b.append(h3("Ignition Curves"))
    b.append(p(
        "Every circuit has electrical characteristics that fall into three categories — resistance, "
        "inductance and capacitance — and to some degree every circuit has all three. One may be so "
        "small that its effect is negligible beside the others, which is why we speak of resistive, "
        "inductive and capacitive circuits. Since IS rests on the principle that a large current can "
        "cause an explosion in a hazardous area and the lack of one cannot, the ranges of current that "
        "are safe and those that are dangerous have to be identified."))
    b.append(p(
        "What is a dangerous amount of electrical energy? The answer lies in the ignition curves, "
        "published in most IS standards, ANSI/UL 913 [5] among them. Three of the most referenced are "
        "shown in Figure 100.2. They give the energy needed to ignite various hazardous atmospheric "
        "mixtures at their most easily ignitable concentration — the concentration found by taking the "
        "volume percentage between the upper and lower explosive limits of that mixture. In all three, "
        "energy levels (voltage and current) below the curve of a group are insufficient to ignite "
        "that group."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Because the ignition temperature is directly related to the voltage and current consumed, "
        "both V<sub>oc</sub> and I<sub>sc</sub> of the barrier must be less than V<sub>max</sub> and "
        "I<sub>max</sub>. Designing an IS system also means accounting for the cable resistance R "
        "(Ω/m), inductance L (µH/m) and capacitance C (pF/m), which are distributed along its length. "
        "Capacitance and inductance can be had from the cable manufacturer's literature; failing that, "
        "default values may be used from NFPA 493/78 (A-4-2): C<sub>c</sub> = 200 pF/m (60 pF/ft) and "
        "L<sub>c</sub> = 0.66 µH/m (0.2 µH/ft). Determining the maximum wiring distance that still "
        "ensures correct operation requires computing the capacitance and inductance."))
    b.append(p(
        "One common approach uses “lumped parameters”, comparing and matching the voltages and currents "
        "of the intrinsically safe apparatus and of the associated apparatus according to Equations "
        "(100.1) and (100.2). Any deviation from either compromises the integrity of the system and "
        "introduces hazardous conditions. The reactive parts of the system must also be verified, to "
        "show that the C<sub>a</sub> and L<sub>a</sub> of the associated apparatus are not exceeded by "
        "the field device plus the field wiring, as in Equations (100.3) and (100.4). Simple and "
        "effective as it is, this method tends to exaggerate the capacitance and inductance of the "
        "wiring, which can be limiting in some applications."))
    b.append(p(
        "Another method exploits the relation between cable resistance and inductance. It applies "
        "where the L/R ratio of the associated apparatus is higher than the calculated L/R ratio of "
        "the cable; under those conditions the smaller D<sub>a</sub> (maximum allowed distance) may be "
        "ignored and the cable extended to the larger D<sub>a</sub>. This is the more flexible method "
        "where cable length is the issue. Figure 100.3 and the example below illustrate both."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p("<b>Lumped-parameter method:</b>"))
    b.append(eq("V<sub>oc</sub> ≤ V<sub>max</sub>", "100.1"))
    b.append(eq("I<sub>sc</sub> ≤ I<sub>max</sub>", "100.2"))
    b.append(eq("C<sub>c</sub> ≤ C<sub>a</sub> − C<sub>i</sub> = 0.45 µF − 0.30 µF = 0.15 µF", "100.3"))
    b.append(eq("L<sub>c</sub> ≤ L<sub>a</sub> − L<sub>i</sub> = 3.5 mH − 2.0 mH = 1.5 mH", "100.4"))
    b.append(p(
        "The maximum length of field wiring, referred to its capacitance and inductance, is the lesser "
        "value of D<sub>a</sub>:"
        "<br>D<sub>a</sub> = 0.15 µF / 150 pF/m = 1000 m"
        "<br>D<sub>a</sub> = 1.5 mH / 2.0 µH/m = 750 m (maximum distance of field wiring)."))
    b.append(p(
        "<b>L/R ratio method:</b> since the cable L/R ratio of 41.7 µH/Ω (2 µH/m ÷ 48 Ω/km) is less "
        "than the given L/R ratio of the associated apparatus (60 µH/Ω), the inductive effect may be "
        "ignored and the maximum distance raised to 1000 m."))
    b.append(note(
        "<b>Translator's note.</b> The printed text carries a few unit slips from typesetting, "
        "corrected here so that they agree with the numbers the text itself derives: (a) the wiring "
        "parameter in Figure 100.3 is L = 2.0 µH/m, not mH/m — with µH/m, 1.5 mH ÷ 2.0 µH/m = 750 m, "
        "exactly as printed; (b) the cable L/R ratio is 41.7 µH/Ω, not mH/Ω; (c) the NFPA 493/78 "
        "default is L<sub>c</sub> = 0.66 µH/m (0.2 µH/ft); (d) in Table 100.1 the 165 °C/329 °F row is "
        "T3B, not T2B (T2B is 260 °C/500 °F and already appears above it); (e) the explosion "
        "probability quoted under Economy is 10<sup>−18</sup>. The Z<sub>w</sub> equation is unnumbered "
        "in the original and is left so here, which keeps the source's numbering of (100.1)–(100.4) "
        "for the four lumped-parameter equations intact."))

    b.append(h3("Certification and Approval"))
    b.append(p(
        "Approval and certification help, but careful planning, design and engineering are still "
        "necessary. IS standards, procedures and tests are recognised worldwide. Testing authorities "
        "include Underwriters Laboratories (UL) and Factory Mutual Research Corp. (FM) in the U.S., "
        "the Canadian Standards Association (CSA) in Canada, and the Physikalisch-Technische "
        "Bundesanstalt (PTB) in Europe. Intrinsically safe products suit all the Classes, Divisions "
        "and Groups of Table 100.2 — but the product must be rated and classified for each specific "
        "application. In the U.S. FM adopted two methods of testing and approving equipment for "
        "hazardous areas:"))
    b.append(ol([
        "<b>Loop (system) approval:</b> an intrinsically safe apparatus is evaluated together with a "
        "specific associated apparatus and approved for installation in that combination. Any change "
        "to the circuit requires re-evaluation and re-certification (Figure 100.4).",
        "<b>Entity approval:</b> the intrinsically safe apparatus and the associated apparatus are "
        "evaluated separately and each is given its own electrical entity parameters (Figure 100.5). "
        "Correct application matches the entity parameters as in Table 100.3. Comparing the entity "
        "values of an intrinsically safe apparatus with those of an associated apparatus is the "
        "crucial step in judging the safety of a circuit. Most safety barriers are entity approved "
        "for all hazardous locations.",
    ]))
    b.append(p(
        "Since most field devices can store energy, they must carry either loop approval or entity "
        "approval for an intrinsically safe system to be correctly built and to operate."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p("IS engineers commonly advocate intrinsically safe equipment for five reasons:"))
    b.append(ol([
        "<b>Safety.</b> No explosion can occur in an intrinsically safe system under any operating "
        "condition. IS equipment runs at lower power levels and prevents shocks, excess thermal "
        "energy and arcing, any of which may be a hazard in other systems and other circumstances.",
        "<b>Reliability.</b> Components and assemblies of IS circuits are tested for reliability "
        "before being labelled and certified, and most IS equipment is designed with special "
        "circuitry for surge suppression and for suppressing spikes and transients.",
        "<b>Ease of handling and installation.</b> IS systems tend to be small and need none of the "
        "expensive, bulky accessories — enclosures, seals, rigid metallic conduit — that raise the "
        "initial investment.",
        "<b>Economy.</b> In some jurisdictions, facilities with hazardous conditions must carry "
        "special liability insurance. With a proper IS installation the probability of explosion is "
        "10<sup>−18</sup> [8], or nearly nonexistent, and premiums tend to be lower.",
        "<b>Maintenance.</b> Equipment can be calibrated and maintained without disconnecting power, "
        "so downtime is shorter.",
    ]))
    b.append(p(
        "Wiring an intrinsically safe system resembles any other installation, but identification and "
        "separation must follow strict rules if the system is to work. All IS components — terminal "
        "blocks, conductors, apparatus — must be explicitly marked and labelled. The conventional "
        "colour for IS equipment is blue. In open wiring, IS conductors must be physically separated "
        "from non-IS conductors by at least 50 mm (2 in.) so that induced voltage cannot defeat the "
        "purpose of IS. Where IS conductors occupy a raceway, the raceway should be labelled "
        "“Intrinsically Safe Circuits”, and IS conductors should never be placed with non-IS ones. "
        "Where a cable tray is used, a grounded sheet-metal partition is an acceptable means of "
        "separation. Where IS and non-IS conductors share an enclosure, a 50 mm (2 in.) separation must "
        "be maintained, and a grounded metal partition must be in place to prevent contact between "
        "conductors that may come loose. Deterioration of the insulation of IS conductors belonging to "
        "different circuits in the same raceway or enclosure can be detrimental to the system. IS "
        "conductors must have an insulation grade able to withstand an ac test voltage of 550 V "
        "root-mean-square (rms), or twice the operating voltage of the IS circuit. Non-IS conductors in "
        "the same enclosure must withstand an ac test voltage of 2U + 1000 V, with a minimum of 1500 V "
        "rms, where U is the sum of the rms voltages of the IS conductors. A widely used and strongly "
        "recommended practice is separate compartments for IS and non-IS conductors."))
    b.append(p(
        "Besides physical separation, sealing the conduits and raceways that carry IS conductors is "
        "essential to stop gases, vapours and dusts passing from hazardous to nonhazardous areas. "
        "Under the NEC, seal-offs need not be explosion-proof; where an associated apparatus is "
        "installed in an explosion-proof enclosure inside a hazardous area, they must be. Code does not "
        "require it, but fitting explosion-proof seal-offs to conduits carrying IS conductors is good "
        "engineering practice, as Figure 100.6 shows."))
    b.append(fig(6, F.fig(6), "en"))

    b.append(h3("Explosion-Proof Fundamentals"))
    b.append(p(
        "Explosion-proof design is a mechanical concept: it leans heavily on the mechanical "
        "construction of the enclosure and on the narrow tolerances between its joints, threads and "
        "flanges to contain, cool and vent any internal explosion safely. By definition, "
        "explosion-proof enclosures must prevent the ignition of explosive gases or vapours that may "
        "surround them (Type 7 and Type 10 only). In Class I, Divisions 1 and 2, arcing devices — "
        "switches, contactors, motor starters — must be enclosed in an explosion-proof enclosure rated "
        "for that area. Contrary to popular belief, explosion-proof enclosures are not, and should not "
        "be, vapour-tight: put succinctly, an explosion inside must be prevented from starting a larger "
        "one outside. Unlike IS, explosion-proof enclosures address the maximum internal pressure (see "
        "NEMA Type 7). Figure 100.7 shows the rugged construction of a standard explosion-proof "
        "panelboard."))
    b.append(p(
        "Besides durability and strength, explosion-proof enclosures must be “flame-tight”: joints and "
        "flanges are held within narrow tolerances so that the hot gases of an internal explosion are "
        "cooled as they escape. Any gas released into the hazardous atmosphere outside is then too "
        "cool to ignite it."))
    b.append(p(
        "Explosion-proof enclosures tend to be bulky — which makes them easy to identify — and heavy, "
        "requiring conduit seals and careful handling. Unlike IS equipment, they operate at normal "
        "power levels, which some circuits and equipment demand. With the right equipment, "
        "installation and maintenance, they can distribute high voltage and power into hazardous areas "
        "safely and effectively."))
    b.append(p(
        "Where ignitable amounts of dust are present, enclosures housing electrical equipment must be "
        "dust-ignition-proof: they must keep combustible dust out while preventing arcs, sparks or "
        "internally generated heat from igniting the dust around the exterior. They must also dissipate "
        "internal heat efficiently, since many dusts ignite at relatively low temperatures. Unlike "
        "Class I, Division 1 explosion-proof enclosures (Type 7), Class II, Division 1 "
        "dust-ignition-proof enclosures (Type 9) are designed to prevent an explosion; they therefore "
        "need not be as strong, or have walls as thick, because there will be no internal explosion."))
    b.append(fig(7, F.fig(7), "en"))

    b.append(h3("Purging and Pressurization"))
    b.append(p(
        "This methodology allows electrical equipment to operate where hazardous conditions exist and "
        "no other method applies, because of imperative high-energy demands and sheer physical size — "
        "large motors and switchgear units, for instance, that are not commercially available for "
        "Class I, Groups A and B. It is also used where control panels housing instruments and "
        "electrical equipment must sit in a hazardous area. Purging and pressurization relies on clean "
        "air or inert gas (nitrogen, say) supplied continuously to the enclosure at enough flow to keep "
        "the equipment adequately cooled and to maintain enough internal pressure to keep combustible "
        "atmospheres out. The enclosures are not explosion-proof, but they must be relatively "
        "vapour-tight and strong enough to perform safely and satisfactorily. The system consists of:"))
    b.append(ol([
        "<b>Clean air (or inert gas) supply.</b> Careful study and analysis matter here, because the "
        "air supplied must be reasonably free of contaminants. Finding a safe location for the intake "
        "takes skill and ingenuity; consulting an HVAC specialist is recommended. Vapour density, "
        "location, wind pattern and the surrounding environment all deserve consideration. Where "
        "compressors and blowers supply the compressed air, the size and location of the compressor or "
        "blower must be chosen to meet the airflow requirement without compromising the main objective "
        "of safety and reliability.",
        "<b>Purging.</b> A pressurized enclosure that has been out of service for a time tends to "
        "collect a combustible mixture. Before energising, inert gas and positive pressure must supply "
        "enough initial clean air volume to minimise the concentration of any combustible mixture "
        "present. For typical applications a flow of four times the internal volume of the enclosure "
        "usually suffices; for unusual ones the volume must be calculated carefully to ensure the "
        "purge succeeds.",
        "<b>Pressurization.</b> This uses the pressure differential between outside and inside to keep "
        "flammable material out, by holding a higher pressure inside. For safe operation the protected "
        "enclosure must be kept at a positive pressure of at least 25 Pa (0.1 in. water) [2] above the "
        "surrounding atmosphere throughout the operation of the protected equipment.",
        "<b>Signals and alarms.</b> Warnings and alarms are essential when positive pressure is lost. "
        "Three types of pressurization and alarm may be used, depending on the nature of the enclosure "
        "controls and the degree of hazard outside. Door interlocks are also required, to prevent the "
        "protected enclosure being opened while the circuit is energised.",
    ]))
    b.append(p("According to NFPA 496 there are three types of pressurization:"))
    b.append(ol([
        "<b>Type X</b> — reduces the classification inside the protected enclosure from Division 1 to "
        "nonclassified. This usually involves a source of ignition in a tight enclosure located in a "
        "potentially hazardous atmosphere. Type X requires a disconnecting means (a flow or pressure "
        "switch) that de-energises the protected enclosure completely and automatically as soon as the "
        "protective gas supply fails, whether pressure or flow is lost. The disconnecting means must "
        "be explosion-proof or intrinsically safe, since it usually sits in the hazardous area.",
        "<b>Type Y</b> — reduces the classification inside the enclosure from Division 1 to Division 2. "
        "The protected enclosure houses equipment rated for Division 2 and provides no source of "
        "ignition, so no immediate hazard is created. Type Y requires a visual or audible alarm on "
        "system failure. A word of caution: safeguards must ensure that any malfunction does not raise "
        "the external surface temperature of the enclosure above 80% of the ignition temperature of "
        "the combustible mixture present.",
        "<b>Type Z</b> — reduces the classification inside the enclosure from Division 2 to "
        "nonclassified. Type Z requires a visual or audible alarm if a failure to maintain positive "
        "pressure or flow inside the protected enclosure is detected.",
    ]))
    b.append(p(
        "Recognising and understanding the dangers of using electricity in hazardous areas is a crucial "
        "part of choosing the best protection. For most applications, where energy demands differ, the "
        "technique will likely combine several methodologies and specialised technologies. Analysis and "
        "investigation done properly look time-consuming and expensive, but for those willing to "
        "follow the established guidelines and sound engineering practice, the process helps secure "
        "the highest level of compliance while yielding substantial savings and preventing property "
        "damage and injury."))

    b.append(h2("Defining Terms"))
    b.append(p(
        "<b>Inductance:</b> the ability of an electrical apparatus to store an electric charge "
        "(energy). An inductor releases that energy when the circuit is opened (broken)."))
    b.append(p(
        "<b>Oxidation:</b> the process in which negatively charged ions (anions) lose electrons at the "
        "anode during an electrochemical process; to become neutral, anions must lose electrons."))
    b.append(p(
        "<b>Resistance temperature device (RTD):</b> a device that measures temperature from the change "
        "in resistance."))
    b.append(p(
        "<b>Zener diode:</b> a nonlinear solid-state device that does not conduct in reverse bias until "
        "a critical voltage is reached, after which it conducts in reverse bias without damage. Zener "
        "diodes have an almost constant voltage characteristic in the reverse-bias (normal) region."))

    b.append(h2("References"))
    b.append(refs([
        "NFPA 70 (ANCI C1 — 1996), National Electrical Code 1996, Quincy, MA.",
        "National Fire Protection Association (NFPA), Articles 493, 496, 497, Quincy, MA.",
        "American Petroleum Institute 500 (RP 500), 1st ed., Washington, D.C., June 1991. "
        "Recommended Practice for Classification of Location for Electrical Installation at "
        "Petroleum Facilities.",
        "Elcon Instruments, Inc., Introduction to Intrinsic Safety, 3rd printing, Norcross, 1990.",
        "Underwriters Laboratories, Inc., Pub. UL 913, 4th ed., Northbrook, IL, 1988, Standard for "
        "Intrinsically Safe Apparatus &amp; Associated Apparatus for Use in Class I, II, III, "
        "Division 1 Hazardous Locations.",
        "Underwriters Laboratories, Inc., Pub. UL 508, Industrial Control Equipment.",
        "P. Babiarz, Cooper Industries, Crouse-Hinds, InTech Engineer's Notebook, Syracuse, NY, 1994.",
        "R. Stahl, Inc., RST 49, Comprehensive Applications and Data Catalog, Woburn, MA, 1992.",
        "J. Oudar, “Intrinsic safety,” J. Southern Calif. Meter Assoc., October 1981.",
        "W. Alexander, “Intrinsically safe systems,” InTech, April 1996.",
    ]))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 100 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 100 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 100 “Thiết bị đo chống nổ” của Sam S. Khalilieh — điểm chớp "
            "cháy, giới hạn nổ, phân loại khu vực nguy hiểm theo NEC, các kiểu vỏ, an toàn nội, "
            "rào Zener, đường cong mồi, phê duyệt theo vòng và theo thực thể, cùng phương pháp thổi "
            "rửa và tạo áp suất, với 7 hình và 3 bảng." if vi
            else
            "Companion to Chapter 100 of the CRC Measurement Handbook — flash point, explosive limits, "
            "NEC area classification, enclosure types, intrinsic safety, Zener barriers, ignition "
            "curves, loop and entity approval, and purging and pressurization, with 7 figures and 3 "
            "tables.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 100' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 100' % BASE_EN)
    meta = ("Chương 100 · theo Ch100.pdf (CRC Press, 1999) · 7 hình, 3 bảng" if vi else
            "Chapter 100 · 7 figures, 3 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 100)))
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
