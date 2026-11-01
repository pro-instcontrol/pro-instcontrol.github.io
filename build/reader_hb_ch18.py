# -*- coding: utf-8 -*-
"""Handbook Chapter 18 — Time Measurement (Michael A. Lombardi, NIST).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch18.py
"""
import os

import hb18fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch18-time-measurement"
TITLE_EN = "Time Measurement"
TITLE_VI = "Đo thời gian"
BYLINE = "Michael A. Lombardi · National Institute of Standards and Technology (NIST)"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch17-acceleration-vibration-shock-measurement"
PREV_VI = "ch17-acceleration-vibration-shock-measurement"
PREV_T_EN = "Acceleration, Vibration, and Shock Measurement"
PREV_T_VI = "Đo gia tốc, rung động và xung kích"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-18-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Phép đo thời gian chia thành hai loại chung. Loại thứ nhất là đo thời điểm trong ngày "
        "(time-of-day). Thời điểm trong ngày được ghi bằng một biểu thức duy nhất gồm năm, tháng, ngày, "
        "giờ, phút, giây… cho tới đơn vị nhỏ nhất mà ta chọn. Khi hỏi câu thường ngày “Mấy giờ rồi?”, ta "
        "đang hỏi một phép đo thời điểm trong ngày."))
    b.append(p(
        "Loại thứ hai (và là loại mà các nhà đo lường hay nói tới hơn) là đo khoảng thời gian (time "
        "interval). Đo khoảng thời gian đòi hỏi đo khoảng trôi qua giữa hai biến cố. Khoảng thời gian là "
        "một trong bốn chuẩn đo lường cơ bản (ba chuẩn còn lại là độ dài, khối lượng và nhiệt độ). Trong "
        "bốn chuẩn cơ bản này, khoảng thời gian có thể đo được với độ phân giải cao nhất và độ không đảm "
        "bảo (uncertainty) nhỏ nhất."))
    b.append(p(
        "Việc giữ thời gian (timekeeping) bao gồm cả hai loại phép đo. Trước hết, phải tìm một biến cố "
        "tuần hoàn lặp lại với tốc độ không đổi. Ví dụ, quả lắc trong đồng hồ có thể đung đưa với tốc độ "
        "một lần mỗi giây. Khi đã biết quả lắc đung đưa mỗi giây một lần, ta có thể lấy giây làm đơn vị cơ "
        "bản của khoảng thời gian. Từ đó xây dựng một hệ giữ thời gian, hay một thang thời gian (time "
        "scale). Thang thời gian là cách sắp xếp các biến cố một cách rõ ràng, không nhập nhằng. Nó được "
        "tạo bằng cách đo một đơn vị thời gian nhỏ (như giây) rồi đếm số giây đã trôi qua để lập nên những "
        "khoảng thời gian dài hơn như phút, giờ, ngày. Thiết bị thực hiện việc đếm gọi là đồng hồ (clock)."))
    b.append(p(
        "Có nhiều loại biến cố tuần hoàn có thể làm nền tảng cho nhiều loại đồng hồ. Hãy tiếp tục bằng "
        "việc xem xét sự tiến hoá của đồng hồ và kỹ thuật giữ thời gian."))

    # ---- 18.1
    b.append(h2("18.1 Sự tiến hoá của đồng hồ và kỹ thuật giữ thời gian",
                "The Evolution of Clocks and Timekeeping"))
    b.append(p(
        "Mọi đồng hồ đều có vài đặc điểm chung. Mỗi đồng hồ có một thiết bị tạo ra biến cố tuần hoàn đã "
        "nói ở trên, gọi là bộ cộng hưởng (resonator). Với đồng hồ quả lắc, quả lắc chính là bộ cộng hưởng. "
        "Dĩ nhiên bộ cộng hưởng cần một nguồn năng lượng, chẳng hạn dây cót hay động cơ, trước khi nó có "
        "thể đung đưa. Gộp lại, nguồn năng lượng và bộ cộng hưởng tạo thành một bộ dao động (oscillator). "
        "Một phần khác của đồng hồ đếm các “nhịp đung đưa” của bộ dao động và đổi chúng thành đơn vị thời "
        "gian như giờ, phút, giây, hoặc nhỏ hơn như mili giây (ms), micro giây (µs) và nano giây (ns). "
        "Cuối cùng, một phần của đồng hồ phải hiển thị hoặc ghi lại kết quả."))
    b.append(p(
        "Độ không đảm bảo tần số của bộ cộng hưởng liên hệ trực tiếp với độ không đảm bảo về thời gian "
        "của đồng hồ. Mối quan hệ này cho ở Bảng 18.1."))
    b.append(table(
        ["Độ không đảm bảo tần số", "Khoảng đo", "Độ không đảm bảo thời gian"],
        [["±1,00 × 10⁻³", "1 s", "±1 ms"],
         ["±1,00 × 10⁻⁶", "1 s", "±1 µs"],
         ["±1,00 × 10⁻⁹", "1 s", "±1 ns"],
         ["±2,78 × 10⁻⁷", "1 h", "±1 ms"],
         ["±2,78 × 10⁻¹⁰", "1 h", "±1 µs"],
         ["±2,78 × 10⁻¹³", "1 h", "±1 ns"],
         ["±1,16 × 10⁻⁸", "1 ngày", "±1 ms"],
         ["±1,16 × 10⁻¹¹", "1 ngày", "±1 µs"],
         ["±1,16 × 10⁻¹⁴", "1 ngày", "±1 ns"]],
        "Bảng 18.1 · Quan hệ giữa độ không đảm bảo tần số và độ không đảm bảo thời gian."))
    b.append(p(
        "Qua lịch sử, những người chế tạo đồng hồ luôn tìm những nguồn tần số ổn định hơn để làm bộ cộng "
        "hưởng. Ngay từ khoảng 3500 trước Công nguyên, người ta đã giữ thời gian bằng cách quan sát bóng "
        "của một vật dịch chuyển giữa lúc mặt trời mọc và lặn. Đồng hồ đơn giản này gọi là đồng hồ mặt "
        "trời (sundial), và tần số cộng hưởng chính là chuyển động biểu kiến của mặt trời. Về sau, đồng hồ "
        "nước, đồng hồ cát và nến đã chia độ cho phép chia ngày thành những đơn vị thời gian nhỏ hơn. Đầu "
        "thế kỷ 14, đồng hồ cơ bắt đầu xuất hiện. Các mẫu đầu dùng cơ cấu verge và foliet làm bộ cộng hưởng "
        "và có độ không đảm bảo khoảng 15 phút/ngày (≈1 × 10⁻²). Một bước đột phá lớn xảy ra năm 1656, khi "
        "nhà khoa học Hà Lan Christiaan Huygens chế tạo chiếc đồng hồ quả lắc đầu tiên. Quả lắc — một cơ "
        "cấu có chu kỳ dao động “tự nhiên” — đã được Galileo Galilei nghiên cứu từ năm 1582, nhưng Huygens "
        "là người đầu tiên phát minh bộ hồi (escapement) giữ cho quả lắc tiếp tục đung đưa. Độ không đảm "
        "bảo của đồng hồ Huygens dưới 1 phút/ngày (≈7 × 10⁻⁴), về sau giảm còn khoảng 10 s/ngày "
        "(≈1 × 10⁻⁴). Huygens sau đó phát triển cụm lò xo và bánh cân bằng mà ngày nay vẫn còn thấy trong "
        "một số đồng hồ đeo tay."))
    b.append(p(
        "Công nghệ quả lắc tiếp tục hoàn thiện cho đến thế kỷ 20. Đến năm 1761, John Harrison đã chế tạo "
        "một đồng hồ hàng hải (marine chronometer) dùng bộ hồi lò xo và bánh cân bằng. Một trong những "
        "chiếc đồng hồ của Harrison chỉ chạy nhanh 54 s trong chuyến đi 5 tháng tới Jamaica, tức khoảng "
        "1/3 s/ngày (≈4 × 10⁻⁶). Giới hạn thực tế của đồng hồ cơ đạt được năm 1921, khi W. H. Shortt trình "
        "diễn một chiếc đồng hồ với hai quả lắc — một con “nô” và một con “chủ”. Quả lắc nô kéo kim đồng "
        "hồ, giải phóng quả lắc chủ khỏi những nhiệm vụ cơ học có thể làm nhiễu tính đều đặn của nó. Đồng "
        "hồ Shortt có độ không đảm bảo chỉ vài giây mỗi năm (≈1 × 10⁻⁷) và trở thành chuẩn tham chiếu của "
        "các phòng thí nghiệm [1,2]."))
    b.append(p(
        "Năm 1927, Joseph W. Horton và Warren A. Marrison thuộc Bell Laboratories chế tạo chiếc đồng hồ đầu "
        "tiên dựa trên bộ dao động tinh thể thạch anh. Đến thập niên 1940, đồng hồ thạch anh đã thay thế "
        "quả lắc Shortt làm chuẩn sơ cấp của phòng thí nghiệm. Đồng hồ thạch anh hoạt động nhờ tính áp "
        "điện của tinh thể thạch anh: khi cho dòng điện chạy qua tinh thể thạch anh, nó cộng hưởng ở một "
        "tần số không đổi. Không có bánh răng hay bộ hồi làm nhiễu tần số cộng hưởng, đồng hồ thạch anh dễ "
        "dàng vượt trội đồng hồ quả lắc. Có thể đạt độ không đảm bảo ±100 µs/ngày (≈1 × 10⁻⁹), và bộ dao "
        "động thạch anh được dùng rộng rãi trong đồng hồ đeo tay, đồng hồ treo tường, đồng hồ để bàn và "
        "mạch điện tử [2–4]."))
    b.append(p(
        "Tần số cộng hưởng của thạch anh phụ thuộc vào một dao động cơ học là hàm của kích thước và hình "
        "dạng tinh thể. Không có hai tinh thể nào hoàn toàn giống nhau hay tạo ra đúng cùng một tần số. "
        "Bộ dao động thạch anh cũng nhạy với các tham số môi trường như nhiệt độ, độ ẩm, áp suất và rung "
        "động [5]. Những nhược điểm này khiến đồng hồ thạch anh chưa đủ cho nhiều ứng dụng và dẫn tới sự "
        "phát triển của bộ dao động nguyên tử."))

    # ---- 18.2
    b.append(h2("18.2 Bộ dao động nguyên tử", "Atomic Oscillators"))
    b.append(p(
        "Bộ dao động nguyên tử dùng các mức năng lượng lượng tử hoá trong nguyên tử và phân tử làm nguồn "
        "tần số cộng hưởng. Các định luật cơ học lượng tử quy định rằng năng lượng của một hệ liên kết, "
        "như nguyên tử, chỉ nhận những giá trị rời rạc nhất định. Một trường điện từ có thể nâng nguyên "
        "tử từ mức năng lượng này lên mức cao hơn. Hoặc một nguyên tử ở mức năng lượng cao có thể rơi "
        "xuống mức thấp hơn bằng cách phát ra năng lượng điện từ. Tần số cộng hưởng (f) của bộ dao động "
        "nguyên tử là hiệu hai mức năng lượng chia cho hằng số Planck (h):"))
    b.append(eq("f = (E₂ − E₁) / h", "18.1"))
    b.append(p(
        "Thời gian được giữ bằng cách quan sát và đếm các tần số mà tại đó năng lượng điện từ được phát ra "
        "hay hấp thụ bởi nguyên tử. Về bản chất, nguyên tử đóng vai trò một quả lắc mà các dao động của nó "
        "được đếm để đánh dấu sự trôi qua của thời gian [3]."))
    b.append(p(
        "Có ba loại bộ dao động nguyên tử chính. Loại rẻ nhất và phổ biến nhất là bộ dao động rubidi, dựa "
        "trên cộng hưởng 6,835 GHz của Rb87. Giá bộ dao động rubidi khoảng 2.000 đến 8.000 USD. Chúng rất "
        "phù hợp cho ứng dụng cần một bộ dao động nhỏ, hiệu năng cao với thời gian khởi động cực nhanh. Độ "
        "không đảm bảo tần số của bộ dao động rubidi khoảng ±5 × 10⁻¹⁰ đến ±5 × 10⁻¹²."))
    b.append(p(
        "Loại thứ hai, chùm tia xêzi (cesium beam), là chuẩn sơ cấp cho hầu hết dịch vụ đo thời gian chính "
        "xác. Như sẽ thấy ở §18.3, tần số cộng hưởng của xêzi (9,1926 GHz) được dùng để định nghĩa giây "
        "SI. Chuẩn tần số sơ cấp của Hoa Kỳ là một bộ dao động xêzi tên NIST-7 với độ không đảm bảo tần "
        "số khoảng ±5 × 10⁻¹⁵. Bộ dao động xêzi bán trên thị trường khác nhau về chất lượng, nhưng độ không "
        "đảm bảo tần số phải ít nhất ±5 × 10⁻¹². Giá bộ dao động xêzi cao, khoảng 30.000 đến 80.000 USD."))
    b.append(p(
        "Loại thứ ba, maser hydro, dựa trên tần số cộng hưởng 1,42 GHz của nguyên tử hydro. Dù hiệu năng "
        "của maser hydro ở một số mặt vượt xêzi, chúng không được dùng rộng rãi do giá cao. Ít chiếc được "
        "chế tạo, và hầu hết thuộc các phòng thí nghiệm chuẩn quốc gia. Giá maser hydro thường vượt "
        "200.000 USD [2,3,6]."))
    b.append(p("Bảng 18.2 tóm tắt sự tiến hoá của thiết kế và hiệu năng đồng hồ."))
    b.append(table(
        ["Loại đồng hồ", "Bộ cộng hưởng", "Năm [TL]", "Độ KĐB thời gian điển hình (24 h)",
         "Độ KĐB tần số điển hình (24 h)"],
        [["Đồng hồ mặt trời", "Chuyển động biểu kiến của mặt trời", "3500 TCN", "—", "—"],
         ["Bộ hồi verge", "Cơ cấu verge và foliet", "Thế kỷ 14", "±15 phút", "±1 × 10⁻²"],
         ["Quả lắc", "Quả lắc", "1656", "±10 s", "±7 × 10⁻⁴"],
         ["Đồng hồ Harrison", "Quả lắc", "1761", "±400 ms", "±4 × 10⁻⁶"],
         ["Quả lắc Shortt", "Hai quả lắc, nô và chủ", "1921", "±10 ms", "±1 × 10⁻⁷"],
         ["Tinh thể thạch anh", "Tinh thể thạch anh", "1927 [4]", "±100 µs", "±1 × 10⁻⁹"],
         ["Buồng khí rubidi", "Cộng hưởng nguyên tử Rb (6834,682608 MHz)", "1958 [7]", "±1 µs", "±1 × 10⁻¹¹"],
         ["Chùm tia xêzi", "Cộng hưởng nguyên tử Cs (9192,63177 MHz)", "1952 [8]", "±10 ns", "±1 × 10⁻¹³"],
         ["Maser hydro", "Cộng hưởng nguyên tử H (1420,405752 MHz)", "1960 [9]", "±10 ns", "±1 × 10⁻¹³"]],
        "Bảng 18.2 · Sự tiến hoá của thiết kế và hiệu năng đồng hồ."))

    # ---- 18.3
    b.append(h2("18.3 Thang thời gian và định nghĩa giây của SI",
                "Time Scales and the SI Definition of the Second"))
    b.append(p(
        "Như đã thấy, độ không đảm bảo của mọi đồng hồ phụ thuộc vào tính không đều đặn của một loại "
        "chuyển động tuần hoàn nào đó. Bằng cách định lượng chuyển động tuần hoàn này, ta có thể định "
        "nghĩa giây — đơn vị cơ bản của khoảng thời gian trong Hệ Đơn vị Quốc tế (SI). Vì các chuẩn thời "
        "gian nguyên tử rõ ràng vượt trội những chuẩn tiền nhiệm, chúng được dùng để định nghĩa giây SI. "
        "Từ năm 1971, nguyên tử xêzi được dùng để định nghĩa giây:"))
    b.append('<blockquote class="quote">Khoảng thời gian của 9.192.631.770 chu kỳ bức xạ tương ứng với '
             'chuyển dịch giữa hai mức siêu tinh tế của trạng thái cơ bản của nguyên tử xêzi-133.'
             '</blockquote>')
    b.append(p(
        "Thời gian nguyên tử quốc tế (TAI) là một thang thời gian nguyên tử tuân theo định nghĩa giây SI "
        "càng sát càng tốt. TAI được duy trì bởi Cục Cân đo Quốc tế (BIPM) tại Sèvres, Pháp. Tính đến năm "
        "1996, nó được tạo bằng cách lấy trung bình dữ liệu thu từ khoảng 250 chuẩn nguyên tử của phòng "
        "thí nghiệm và thương mại đặt tại hơn 40 phòng thí nghiệm khác nhau. Hầu hết các chuẩn này dựa "
        "trên xêzi, dù số maser hydro đóng góp đang tăng. Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) và "
        "Đài Thiên văn Hải quân Hoa Kỳ (USNO) là hai trong nhiều phòng thí nghiệm đóng góp cho TAI."))
    b.append(p(
        "Trước khi các thang thời gian nguyên tử được chấp nhận, người ta dùng các thang thời gian thiên "
        "văn. Những thang này dựa trên ngày mặt trời trung bình, tức một vòng quay của Trái Đất quanh "
        "trục. Cho đến năm 1956, giây mặt trời trung bình giữ vai trò giây SI. Giây mặt trời trung bình "
        "được định nghĩa là 1/86.400 của ngày mặt trời trung bình, với 86.400 là số giây trong ngày. Giây "
        "mặt trời trung bình này là nền tảng cho Giờ Quốc tế (Universal Time — UT). Một số biến thể của UT "
        "đã được định nghĩa:"))
    b.append(p(
        "<b>UT0:</b> thang thời gian mặt trời trung bình nguyên thuỷ, dựa trên chuyển động quay của Trái "
        "Đất quanh trục. UT0 ban đầu được giữ bằng đồng hồ quả lắc. Khi có những đồng hồ tốt hơn dựa trên "
        "bộ dao động thạch anh, các nhà thiên văn nhận thấy sai số trong UT0 do chuyển động cực (polar "
        "motion), dẫn tới thang UT1."))
    b.append(p(
        "<b>UT1:</b> thang thời gian thiên văn được dùng rộng rãi nhất; UT1 là phiên bản cải tiến của UT0, "
        "hiệu chỉnh sự dịch chuyển kinh độ của trạm quan sát do chuyển động cực. Vì tốc độ quay của Trái "
        "Đất không đều, UT1 không hoàn toàn dự đoán được và có độ không đảm bảo ±3 ms mỗi ngày."))
    b.append(p(
        "<b>UT2:</b> chủ yếu mang ý nghĩa lịch sử; UT2 là phiên bản làm trơn của UT1, hiệu chỉnh những sai "
        "lệch đã biết trong chuyển động quay của Trái Đất do mômen động lượng của lõi, manti, đại dương và "
        "khí quyển."))
    b.append(p(
        "Giây lịch thiên (ephemeris second) giữ vai trò giây SI từ 1956 đến 1971. Nó là một phân số của "
        "năm chí tuyến (tropical year), tức khoảng giữa hai điểm phân xuân hằng năm vào khoảng 21 tháng 3. "
        "Năm chí tuyến được định nghĩa là 31.556.925,9747 giây lịch thiên. Việc xác định thời điểm chính "
        "xác của điểm phân rất khó, và điều này giới hạn độ không đảm bảo của Giờ Lịch thiên (ET) ở mức "
        "±50 ms trong khoảng 9 năm. ET chủ yếu được các nhà thiên văn dùng làm biến thời gian độc lập cho "
        "lịch thiên hành tinh. Năm 1984, ET được thay bằng Giờ Trái Đất (Terrestrial Time — TT), bằng TAI + "
        "32,184 s. Độ không đảm bảo của TT là ±10 µs [10, 11]."))

    # ---- 18.4
    b.append(h2("18.4 Giờ Phối hợp Quốc tế (UTC)", "Coordinated Universal Time (UTC)"))
    b.append(p(
        "Từ ngày 1 tháng 1 năm 1972, mọi phòng thí nghiệm quốc gia và dịch vụ phát thời gian đều phân phối "
        "Giờ Phối hợp Quốc tế (UTC), khác TAI một số nguyên giây. Hiệu giữa UTC và TAI tăng lên khi các "
        "giây nhuận (leap second) được chèn vào UTC. Khi cần, giây nhuận được thêm vào thang UTC vào ngày "
        "30 tháng 6 hoặc 31 tháng 12. Mục đích của chúng là giữ thời gian nguyên tử (UTC) trong khoảng "
        "±0,9 s so với thời gian thiên văn (UT1). Nhiều dịch vụ thời gian phát một hiệu chỉnh DUT1, tức "
        "giá trị hiện tại của UT1 trừ UTC. Bằng cách áp hiệu chỉnh này vào UTC, ta thu được UT1."))
    b.append(p(
        "Giây nhuận xảy ra ít hơn một lần mỗi năm một chút, vì UT1 hiện đang thay đổi khoảng 800 ms mỗi "
        "năm so với UTC. Giây nhuận đầu tiên được đưa vào ngày 30 tháng 6 năm 1972. Cho đến nay, mọi giây "
        "nhuận đều dương, điều này cho thấy giây mặt trời trung bình (do chuyển động quay Trái Đất xác "
        "định) dài hơn giây nguyên tử (do xêzi xác định). UTC chạy nhanh hơn UT1 vì hai lý do. Lý do thứ "
        "nhất và quan trọng nhất là định nghĩa giây nguyên tử khiến nó hơi ngắn hơn giây mặt trời trung "
        "bình. Lý do thứ hai là tốc độ quay của Trái Đất nhìn chung đang giảm. Khi thêm một giây nhuận "
        "dương vào UTC, trình tự biến cố là:"))
    b.append(eq("23 h 59 m 59 s → 23 h 59 m 60 s → 0 h 0 m 0 s"))
    b.append(p(
        "Việc chèn giây nhuận tạo ra một phút dài 61 s. Điều này thực chất “dừng” thang UTC trong 1 s để "
        "UT1 có cơ hội đuổi kịp. Trừ khi xảy ra một thay đổi đột ngột, không lường trước trong tốc độ quay "
        "của Trái Đất, các giây nhuận trong tương lai sẽ tiếp tục là dương [10, 11]."))

    # ---- 18.5
    b.append(h2("18.5 Giới thiệu về truyền thời gian", "Introduction to Time Transfer"))
    b.append(p(
        "Nhiều ứng dụng đòi hỏi những đồng hồ ở các vị trí khác nhau được đặt cùng thời gian (đồng bộ — "
        "synchronization) hoặc chạy cùng tốc độ (đồng tần — syntonization). Một ứng dụng phổ biến là truyền "
        "thời gian từ một vị trí và đồng bộ đồng hồ ở vị trí khác. Việc này cần một đầu ra xung 1 xung mỗi "
        "giây (1 pps) tham chiếu UTC. Khi đã có xung đúng giờ, ta biết thời điểm đến của mỗi giây và có thể "
        "đồng tần một đồng hồ cục bộ bằng cách cho nó chạy cùng tốc độ. Tuy nhiên, vẫn phải biết thời điểm "
        "trong ngày trước khi đồng bộ đồng hồ. Ví dụ, là 12:31:38 hay 12:31:48? Để có thời điểm trong ngày, "
        "ta cần một mã thời gian (time code) tham chiếu UTC. Mã thời gian cung cấp giờ, phút, giây UTC, và "
        "thường cung cấp cả thông tin ngày tháng như tháng, ngày, năm."))
    b.append(p(
        "Tóm lại, đồng bộ cần hai thứ: một xung đúng giờ và một mã thời gian. Nhiều tín hiệu truyền thời "
        "gian đáp ứng cả hai yêu cầu. Các tín hiệu này xuất phát từ một đồng hồ UTC tham chiếu một hay "
        "nhiều bộ dao động xêzi. Tín hiệu thời gian từ đồng hồ này sau đó được phân phối (hay truyền) tới "
        "người dùng. Thời gian có thể truyền qua nhiều môi trường khác nhau, gồm cáp đồng trục, sợi quang, "
        "tín hiệu vô tuyến (ở nhiều chỗ trong phổ), đường điện thoại và mạng máy tính. Trước khi bàn các "
        "tín hiệu truyền thời gian sẵn có, hãy xem xét các phương pháp truyền thời gian."))
    b.append(h3("Các phương pháp truyền thời gian", "Time Transfer Methods"))
    b.append(p(
        "Yếu tố đóng góp lớn nhất vào độ không đảm bảo truyền thời gian là trễ đường truyền (path delay), "
        "tức độ trễ sinh ra khi tín hiệu đi từ máy phát (nguồn) đến máy thu (đích). Để minh hoạ vấn đề trễ "
        "đường truyền, hãy xét tín hiệu thời gian phát từ một đài phát thanh. Giả sử tín hiệu gần như hoàn "
        "hảo tại nguồn, với độ không đảm bảo ±100 ns so với UTC. Nếu đặt một trạm thu cách đó 1000 km, ta "
        "cần tính thời gian tín hiệu đi tới trạm. Sóng vô tuyến truyền với tốc độ ánh sáng (≈3,3 µs/km). Do "
        "đó, khi tới trạm, tín hiệu đã trễ 3,3 ms. Ta có thể bù trễ đường truyền này bằng cách chỉnh đồng "
        "hồ 3,3 ms. Đây gọi là hiệu chỉnh đường truyền (calibrating the path)."))
    b.append(p(
        "Luôn có giới hạn về mức độ hiệu chỉnh được một đường truyền. Ví dụ, để tìm độ dài đường truyền, "
        "ta cần toạ độ của cả máy thu lẫn máy phát, và phần mềm tính trễ. Dù vậy, ta vẫn giả định tín hiệu "
        "đi theo đường ngắn nhất giữa máy phát và máy thu. Dĩ nhiên điều này không đúng. Sóng vô tuyến có "
        "thể phản xạ qua lại giữa Trái Đất và tầng điện ly, và đi xa hơn nhiều so với khoảng cách giữa các "
        "ăng-ten. Một ước lượng trễ đường truyền tốt đòi hỏi biết các biến ảnh hưởng tới truyền sóng vô "
        "tuyến: mùa trong năm, thời điểm trong ngày, vị trí mặt trời, chỉ số mặt trời… Ngay cả khi đó, ước "
        "lượng trễ đường truyền vẫn không chính xác đến mức có thể khó khôi phục thời gian với độ không "
        "đảm bảo ±1 ms (tệ hơn 10.000 lần so với thời gian phát đi) [12, 13]."))
    b.append(p(
        "Những người thiết kế hệ truyền thời gian đã phát triển nhiều cách sáng tạo để đối phó vấn đề trễ "
        "đường truyền. Các phương pháp tinh vi hơn có đường truyền tự hiệu chỉnh (self-calibrating), tự "
        "động bù trễ đường truyền. Các hệ truyền thời gian có thể chia thành năm loại chung:"))
    b.append(p(
        "<b>1. Phương pháp một chiều (người dùng hiệu chỉnh đường truyền):</b> đây là loại đơn giản và phổ "
        "biến nhất, một hệ một chiều trong đó người dùng chịu trách nhiệm hiệu chỉnh đường truyền (nếu "
        "cần). Như minh hoạ ở Hình 18.1, tín hiệu từ máy phát đến máy thu bị môi trường làm trễ τ_ab. Để "
        "có kết quả tốt nhất, người dùng phải ước lượng τ_ab và hiệu chỉnh đường truyền bằng cách bù trễ."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Thường người dùng hệ một chiều chỉ cần độ không đảm bảo thời gian ±1 s, nên không cố hiệu chỉnh "
        "đường truyền. Ví dụ, người dùng một chương trình phát tần số cao (HF) có thể đồng bộ đồng hồ ở "
        "mức 1 s mà không cần bận tâm tới hiệu ứng trễ đường truyền."))
    b.append(p(
        "<b>2. Phương pháp một chiều (đường truyền tự hiệu chỉnh):</b> đây là biến thể của phương pháp một "
        "chiều đơn giản ở Hình 18.1. Tuy nhiên, hệ truyền thời gian (chứ không phải người dùng) chịu trách "
        "nhiệm ước lượng và loại bỏ trễ τ_ab."))
    b.append(p(
        "Một trong hai kỹ thuật thường được dùng để giảm độ lớn τ_ab. Kỹ thuật thứ nhất là ước lượng thô "
        "τ_ab rồi phát thời gian sớm đi một lượng tương ứng. Ví dụ, nếu biết τ_ab sẽ ít nhất 20 ms với mọi "
        "người dùng, ta có thể phát thời gian sớm 20 ms. Việc đẩy sớm tín hiệu thời gian này sẽ giảm độ "
        "không đảm bảo cho mọi người dùng. Với người dùng có τ_ab ≈ 20 ms, nó sẽ loại bỏ gần như toàn bộ "
        "độ không đảm bảo do trễ đường truyền."))
    b.append(p(
        "Một kỹ thuật tinh vi hơn là tính τ_ab bằng phần mềm. Có thể tính và áp một hiệu chỉnh cho τ_ab nếu "
        "biết toạ độ của cả máy phát lẫn máy thu. Nếu máy phát đứng yên, có thể dùng một hằng số cho vị trí "
        "máy phát. Nếu máy phát chuyển động (ví dụ vệ tinh), nó phải phát toạ độ của mình cùng với tín hiệu "
        "thời gian. Toạ độ máy thu phải do máy thu tính (trong trường hợp hệ dẫn đường vô tuyến) hoặc do "
        "người dùng nhập. Sau đó, một máy thu điều khiển bằng phần mềm có thể tính khoảng cách giữa máy "
        "phát và máy thu và bù trễ đường truyền bằng cách hiệu chỉnh τ_ab. Ngay cả khi dùng phương pháp "
        "này, độ không đảm bảo vẫn xuất hiện do sai số vị trí của máy phát hoặc máy thu và do biến thiên "
        "tốc độ truyền dọc đường."))
    b.append(p(
        "Cả hai kỹ thuật có thể minh hoạ bằng dịch vụ thời gian vệ tinh GOES (bàn sau). Vì các vệ tinh GOES "
        "ở quỹ đạo địa tĩnh, tín hiệu mất khoảng 245 ms đến 275 ms để đi từ Trái Đất lên vệ tinh rồi về "
        "một người dùng ngẫu nhiên trên Trái Đất. Để bù trễ này, thời gian do đồng hồ trạm mặt đất giữ được "
        "đẩy sớm 260 ms. Điều này loại bỏ phần lớn τ_ab. Độ không đảm bảo thời gian cho một người dùng trên "
        "Trái Đất khi đó vào khoảng ±15 ms. Vệ tinh cũng gửi toạ độ của nó cùng thông tin thời gian. Nếu "
        "dùng máy thu điều khiển bằng vi xử lý và biết toạ độ máy thu, máy thu có thể ước lượng τ_ab tốt "
        "hơn, điển hình trong khoảng ±100 µs."))
    b.append(p(
        "<b>3. Phương pháp common-view:</b> phương pháp common-view gồm một máy phát chuẩn (R) và hai máy "
        "thu (A và B). Máy phát nằm trong “tầm nhìn chung” của cả hai máy thu. Cả hai máy thu so sánh tín "
        "hiệu nhận đồng thời với đồng hồ cục bộ và ghi dữ liệu (Hình 18.2). Máy thu A nhận tín hiệu qua "
        "đường τ_ra và so sánh chuẩn với đồng hồ cục bộ (R − Clock A). Máy thu B nhận tín hiệu qua đường "
        "τ_rb và ghi (R − Clock B). Hai máy thu sau đó trao đổi và lấy hiệu dữ liệu. Các sai số của hai "
        "đường (τ_ra và τ_rb) chung với chuẩn sẽ triệt tiêu, và độ không đảm bảo do trễ đường truyền gần "
        "như bị loại bỏ. Kết quả phép đo là (Clock A − Clock B) − (τ_ra − τ_rb)."))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Cần nhớ rằng kỹ thuật common-view không đồng bộ đồng hồ theo thời gian thực. Dữ liệu phải được "
        "trao đổi với người dùng khác, và kết quả có thể chỉ biết được rất lâu sau khi các phép đo hoàn "
        "tất."))
    b.append(p(
        "<b>4. Phương pháp hai chiều:</b> phương pháp hai chiều đòi hỏi hai người dùng cùng phát và thu qua "
        "cùng một môi trường tại cùng thời điểm (Hình 18.3). Trạm A và B đồng thời trao đổi tín hiệu thời "
        "gian qua cùng môi trường và so sánh tín hiệu nhận với đồng hồ của mình. Trạm A ghi A − (B + τ_ba) "
        "và trạm B ghi B − (A + τ_ab), với τ_ba là trễ đường truyền từ A đến B, và τ_ab là trễ đường truyền "
        "từ A đến B. Hiệu giữa hai tập số đọc cho 2(A − B) − (τ_ba − τ_ab). Nếu đường truyền thuận nghịch "
        "(τ_ab = τ_ba), thì hiệu A − B được biết hoàn hảo vì đường giữa A và B đã được đo. Khi triển khai "
        "đúng bằng vệ tinh hoặc liên kết sợi quang, phương pháp hai chiều vượt trội mọi phương pháp truyền "
        "thời gian khác và có thể đạt độ không đảm bảo ±1 ns."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Truyền thời gian hai chiều có nhiều ứng dụng tiềm năng trong mạng viễn thông. Tuy nhiên, khi dùng "
        "môi trường không dây, có một số hạn chế làm giảm tính hữu dụng. Nó có thể đòi hỏi thiết bị đắt "
        "tiền và giấy phép chính phủ để người dùng được phát. Và giống phương pháp common-view, phương pháp "
        "hai chiều đòi hỏi người dùng trao đổi dữ liệu. Nhưng vì người dùng có thể phát, có thể gộp dữ liệu "
        "với thông tin thời gian và tính kết quả theo thời gian thực."))
    b.append(p(
        "<b>5. Phương pháp loop-back (vòng hồi):</b> giống phương pháp hai chiều, phương pháp loop-back đòi "
        "hỏi máy thu gửi thông tin trở lại máy phát. Ví dụ, tín hiệu thời gian được gửi từ máy phát (A) "
        "tới máy thu (B) qua đường τ_ab. Máy thu (B) sau đó dội hay phản xạ tín hiệu trở lại máy phát (A) "
        "qua đường τ_ba. Máy phát cộng hai trễ đường truyền (τ_ab + τ_ba) để có trễ khứ hồi, rồi chia cho "
        "2 để ước lượng trễ một chiều. Sau đó máy phát đẩy sớm tín hiệu thời gian đi một lượng bằng trễ "
        "một chiều ước lượng."))
    b.append(p(
        "Một số yếu tố góp phần gây độ không đảm bảo cho phương pháp loop-back. Một là không phải lúc nào "
        "cũng biết tín hiệu từ A đến B có đi cùng đường với tín hiệu từ B đến A hay không. Nói cách khác, "
        "ta không thể giả định đường truyền thuận nghịch. Ngay cả khi có đường thuận nghịch, ta không dùng "
        "cùng đường tại cùng thời điểm. Đầu tiên máy phát gửi dữ liệu tới máy thu, rồi máy thu gửi dữ liệu "
        "trở lại máy phát. Trong khoảng giữa hai lần truyền, đường truyền có thể đã thay đổi, và những thay "
        "đổi này góp vào độ không đảm bảo."))
    b.append(p(
        "Phương pháp loop-back có thể không thực tế qua môi trường không dây vì việc gửi thông tin trở lại "
        "máy phát đòi hỏi một máy phát vô tuyến, giấy phép phát sóng… Tuy nhiên, khi môi trường là đường "
        "điện thoại hay kết nối mạng, có thể triển khai phương pháp loop-back hoàn toàn bằng phần mềm."))
    b.append(h3("Mã thời gian", "Time Codes"))
    b.append(p(
        "Mã thời gian là một thông điệp chứa thông tin thời điểm trong ngày, cho phép người dùng đặt đồng hồ "
        "về đúng thời điểm. Hướng dẫn của Liên minh Viễn thông Quốc tế (ITU) nêu rằng mọi mã thời gian nên "
        "phân phối giờ, phút, giây UTC cùng một hiệu chỉnh DUT1 [14]."))
    b.append(p(
        "Mã thời gian được phát ở nhiều định dạng khác nhau (gồm nhị phân, thập phân mã hoá nhị phân [BCD] "
        "và ASCII) và rất ít được chuẩn hoá. Tuy vậy, có những chuẩn để phân phối lại mã thời gian trong "
        "một cơ sở. Những mã thời gian chuẩn này được Nhóm Thiết bị Đo Khoảng (Inter-Range Instrumentation "
        "Group — IRIG) tạo ra lần đầu năm 1956 và đến nay vẫn được các nhà sản xuất thiết bị dùng rộng rãi. "
        "IRIG định nghĩa một số mã thời gian, nhưng phổ biến nhất có lẽ là IRIG-B. Các mã IRIG cho phép nhà "
        "sản xuất chế tạo thiết bị tương thích. Ví dụ, một máy thu vệ tinh có đầu ra IRIG-B có thể điều "
        "khiển một màn hình thời điểm lớn nhận đầu vào IRIG-B, hoặc cung cấp tham chiếu thời gian cho một "
        "máy chủ mạng đọc được IRIG-B."))
    b.append(p(
        "Các định dạng mã thời gian IRIG là mã nối tiếp, điều biến độ rộng, có thể dùng ở dạng dịch mức "
        "một chiều (dc level shift) hoặc điều biên (AM). Ví dụ, IRIG-B có chu kỳ khung 1 s và có thể truyền "
        "dưới dạng đường bao điều biến dịch mức một chiều hoặc sóng mang 1000 Hz được điều biến. Dữ liệu "
        "thời gian BCD và nhị phân trực tiếp (ngày, giờ, phút, giây) được chứa trong khung 1 s. Bộ giải mã "
        "IRIG-B đơn giản chỉ lấy dữ liệu mã hoá và cho độ phân giải 1 s. Các bộ giải mã khác đếm chu kỳ "
        "sóng mang và cho độ phân giải thời gian bằng chu kỳ 1000 Hz (1 ms). Những bộ giải mã tiên tiến hơn "
        "khoá pha một bộ dao động theo mã thời gian và cho độ phân giải chỉ bị giới hạn bởi tỉ số tín "
        "hiệu/tạp của tín hiệu mã thời gian (điển hình ±2 µs)."))

    # ---- 18.6
    b.append(h2("18.6 Tín hiệu truyền thời gian qua vô tuyến", "Radio Time Transfer Signals"))
    b.append(p(
        "Nhiều loại máy thu nhận mã thời gian phát qua vô tuyến. Giá thành biến thiên rộng, từ dưới 500 USD "
        "đến 15.000 USD hoặc hơn. Đồng hồ vô tuyến có nhiều dạng. Một số là thiết bị độc lập (hay gắn "
        "giá) có màn hình thời gian số; chúng thường có giao diện máy tính như RS-232 hay IEEE-488. Số "
        "khác là bo mạch cắm trực tiếp vào bus máy tính. Khi chọn đồng hồ vô tuyến, hãy chắc chắn tín hiệu "
        "dùng được trong khu vực và có thể lắp loại ăng-ten thích hợp."))
    b.append(p(
        "Khi xem xét tín hiệu thời gian vô tuyến, cần nhớ rằng các giá trị độ không đảm bảo nêu ra chỉ áp "
        "cho tín hiệu thô. Có thêm những trễ trước khi tín hiệu được máy thu xử lý và dùng để đồng bộ đồng "
        "hồ. Ví dụ, có trễ cáp giữa ăng-ten và máy thu; có trễ thiết bị do phần cứng và trễ xử lý do phần "
        "mềm. Nếu không biết, những trễ này có thể gây sai số đồng bộ. Tùy ứng dụng, sai số đồng bộ có thể "
        "quan trọng hoặc không. Tuy nhiên, chúng phải được đo và tính đến khi phân tích độ không đảm bảo "
        "của một hệ thời gian."))
    b.append(h3("Tín hiệu vô tuyến HF (gồm WWV và WWVH)", "HF Radio Signals (including WWV and WWVH)"))
    b.append(p(
        "Các chương trình phát thanh tần số cao (HF) hay sóng ngắn thường được dùng để truyền thời gian ở "
        "mức hiệu năng vừa. Những đài này phổ biến vì vài lý do: chúng phủ sóng toàn cầu, hoạt động với "
        "máy thu giá rẻ, và cung cấp thông báo bằng âm thanh để ta có thể “nghe” thời gian. Để dùng tín hiệu "
        "thời gian HF, cần một radio sóng ngắn. Nhiều loại radio sóng ngắn sẵn có, từ máy xách tay đơn giản "
        "dưới 100 USD đến máy thu thông tin giá vài nghìn USD. Một vài hãng chế tạo máy thu thời gian HF "
        "chuyên dụng tự động tìm tín hiệu tốt nhất bằng cách quét nhiều tần số khác nhau; một số có giao "
        "diện máy tính tích hợp (thường RS-232) để đặt đồng hồ máy tính."))
    b.append(p(
        "Có nhiều đài tần số và thời gian HF trên khắp thế giới, gồm các đài do NIST vận hành là WWV và "
        "WWVH. WWV ở gần Fort Collins, CO, còn WWVH ở đảo Kauai, HI. Cả hai đài phát tín hiệu thời gian và "
        "tần số liên tục trên 2,5; 5; 10 và 15 MHz. WWV còn phát trên 20 MHz. Mọi tần số mang cùng chương "
        "trình, và ít nhất một tần số nên dùng được mọi lúc. Cũng có thể nghe hai đài qua điện thoại: gọi "
        "(303) 499-7111 cho WWV và (808) 335-4363 cho WWVH."))
    b.append(p(
        "Phần âm thanh của chương trình WWV/WWVH gồm các xung giây (tiếng tích tắc) tạo bởi tín hiệu điều "
        "biên hai bên (double-sideband) 100% trên mỗi sóng mang RF. Xung đầu tiên của mỗi giờ là xung 800 ms "
        "tần số 1500 Hz. Xung đầu tiên của mỗi phút là xung 800 ms tần số 1000 Hz ở WWV và 1200 Hz ở WWVH. "
        "Các xung giây còn lại là những cụm âm ngắn (xung 5 ms tần số 1000 Hz ở WWV và 1200 Hz ở WWVH) nghe "
        "như tiếng tích tắc đồng hồ. Mọi xung đều xảy ra ở đầu mỗi giây. Xung giây thứ 29 và thứ 59 bị bỏ. "
        "Mỗi tiếng tích tắc được đặt trước 10 ms im lặng và theo sau 25 ms im lặng để tránh nhiễu từ các "
        "đài thời gian khác và dễ nghe tiếng tích tắc hơn. Đầu mỗi phút, một giọng nói thông báo giờ và "
        "phút UTC hiện tại. WWV dùng giọng nam, WWVH dùng giọng nữ."))
    b.append(p(
        "Ngoài âm thanh, một mã thời gian cũng được gửi trên sóng mang phụ 100 Hz. Mã thời gian là phiên "
        "bản sửa đổi của IRIG-H, được gửi mỗi phút một lần ở định dạng BCD với tốc độ 1 bit/giây (bps). "
        "Trong 1 phút, đủ bit được gửi để biểu diễn phút, giờ và ngày trong năm, hiệu chỉnh DUT1, và chỉ "
        "báo Giờ mùa hè (DST). Thông tin thời gian mã hoá chỉ thời điểm ở đầu khung 1 phút."))
    b.append(p(
        "WWV và WWVH phù hợp nhất để đồng bộ ở mức 1 s (hoặc phân số của giây). Độ không đảm bảo thực tế "
        "phụ thuộc khoảng cách người dùng tới máy phát, nhưng phải dưới 30 ms. Dù có thể đạt độ không đảm "
        "bảo ±1 ms với đường truyền được hiệu chỉnh tốt, vẫn có những tín hiệu khác dễ dùng hơn và đáng "
        "tin cậy hơn ở mức 1 ms [15]."))
    b.append(h3("Tín hiệu vô tuyến LF (gồm WWVB và LORAN-C)", "LF Radio Signals (including WWVB and LORAN-C)"))
    b.append(p(
        "Trước khi có tín hiệu vệ tinh, tín hiệu tần số thấp (LF) là phương pháp được chọn để truyền thời "
        "gian. Dù việc dùng tín hiệu LF đã giảm, chúng vẫn có một ưu điểm lớn — thường thu được trong nhà "
        "mà không cần ăng-ten ngoài. Điều này khiến chúng lý tưởng cho nhiều ứng dụng điện tử tiêu dùng."))
    b.append(p(
        "Nhiều nước có dịch vụ thời gian trong băng LF từ 30 kHz đến 300 kHz, cũng như băng VLF (tần số rất "
        "thấp) từ 3 kHz đến 30 kHz. Những tín hiệu này thiếu băng thông cần để cung cấp thông báo bằng "
        "giọng nói, nhưng thường cung cấp một xung đúng giờ và/hoặc một mã thời gian. Như với tín hiệu HF, "
        "người dùng phải hiệu chỉnh đường truyền để có kết quả tốt nhất. Tuy nhiên, vì một phần tín hiệu LF "
        "là sóng đất (groundwave) đi theo độ cong Trái Đất, ước lượng trễ đường truyền tốt dễ hơn nhiều. "
        "Hai ví dụ tín hiệu LF dùng để truyền thời gian là WWVB và LORAN-C. WWVB phát mã thời gian nhị phân "
        "trên sóng mang 60 kHz. LORAN-C phát xung đúng giờ ở 100 kHz nhưng không có mã thời gian."))
    b.append(h3("WWVB", "WWVB"))
    b.append(p(
        "WWVB là đài vô tuyến LF (60 kHz) do NIST vận hành từ cùng địa điểm với WWV gần Fort Collins, CO. "
        "Tín hiệu hiện phủ phần lớn Bắc Mỹ, và việc tăng công suất (6 dB, dự kiến năm 1998) sẽ mở rộng "
        "vùng phủ và cải thiện tỉ số tín hiệu/tạp trong nước Mỹ."))
    b.append(p(
        "Dù ổn định hơn nhiều so với đường HF, đường WWVB chịu ảnh hưởng của độ dài đường truyền và của "
        "biến thiên ngày đêm và theo mùa. Độ dài đường truyền quan trọng vì một phần tín hiệu đi dọc mặt "
        "đất (sóng đất), phần khác phản xạ từ tầng điện ly (sóng trời). Đường sóng đất ổn định hơn và dễ "
        "ước lượng hơn nhiều so với đường sóng trời. Nếu đường tương đối ngắn (dưới 1000 km), máy thu "
        "thường có thể bám liên tục sóng đất vì nó luôn đến trước. Nếu độ dài đường tăng, sẽ nhận được hỗn "
        "hợp sóng đất và sóng trời. Và trên đường rất dài, sóng đất có thể yếu đến mức chỉ còn nhận được "
        "sóng trời; khi đó đường trở nên kém ổn định hơn nhiều."))
    b.append(p(
        "Thời điểm trong ngày cũng quan trọng. Ban ngày, máy thu có thể phân biệt sóng đất và sóng trời, và "
        "độ ổn định đường có thể chỉ biến thiên vài micro giây. Tuy nhiên, nếu đang nhận một phần sóng "
        "trời, sẽ có dịch pha ngày đêm (diurnal phase shift) lúc mặt trời mọc và lặn. Ví dụ, khi đường "
        "chuyển từ tối hoàn toàn sang sáng hoàn toàn, tầng điện ly hạ xuống. Điều này làm ngắn đường giữa "
        "máy phát và máy thu, và trễ đường giảm cho tới khi toàn bộ đường ở trong ánh sáng. Trễ đường sau "
        "đó ổn định cho tới khi máy phát hoặc máy thu vào bóng tối. Khi đó tầng điện ly nâng lên, làm tăng "
        "trễ đường."))
    b.append(p(
        "Mã thời gian WWVB được đồng bộ với sóng mang 60 kHz và phát mỗi phút một lần. Mã được gửi ở định "
        "dạng BCD. Bit được gửi bằng cách dịch công suất sóng mang. Công suất sóng mang giảm 10 dB ở đầu "
        "mỗi giây. Nếu công suất đầy đủ được phục hồi 200 ms sau, đó là bit 0. Nếu phục hồi 500 ms sau, đó "
        "là bit 1. Các dấu tham chiếu và mã định vị được gửi bằng cách phục hồi công suất đầy đủ 800 ms "
        "sau. Mã thời gian cung cấp thông tin năm, ngày, giờ, phút, giây, hiệu chỉnh DUT1, và thông tin về "
        "Giờ mùa hè, năm nhuận và giây nhuận [15]."))
    b.append(h3("LORAN-C", "LORAN-C"))
    b.append(p(
        "LORAN-C là hệ dẫn đường vô tuyến đặt trên mặt đất. Phần lớn hệ thống do Bộ Giao thông Hoa Kỳ (DOT) "
        "vận hành, nhưng một số trạm do chính phủ nước ngoài vận hành. Hệ gồm các nhóm trạm (gọi là chuỗi). "
        "Mỗi chuỗi có một trạm chủ và từ hai đến năm trạm phụ. Các trạm công suất cao, điển hình 275 đến "
        "1800 kW, phát trên sóng mang 100 kHz dùng băng thông từ 90 kHz đến 110 kHz."))
    b.append(p(
        "Vì có nhiều chuỗi LORAN-C dùng cùng tần số sóng mang, các chuỗi phát xung để có thể nhận diện từng "
        "trạm. Mỗi chuỗi phát một nhóm xung gồm xung từ mọi trạm riêng lẻ. Nhóm xung được gửi ở một Khoảng "
        "Lặp Nhóm (Group Repetition Interval — GRI) riêng. Ví dụ, chuỗi 7980 phát xung mỗi 79,8 ms. Bằng "
        "cách tìm các nhóm xung cách nhau đúng khoảng này, máy thu có thể nhận diện chuỗi 7980."))
    b.append(p(
        "Khi đã nhận diện một trạm cụ thể trong chuỗi, hình dạng xung cho phép máy thu định vị và bám một "
        "chu kỳ sóng đất cụ thể của sóng mang. Nhìn chung, máy thu trong vòng 1500 km từ máy phát có thể "
        "bám cùng chu kỳ sóng đất vô hạn và tránh nhận sóng trời. Vì máy thu phân biệt được sóng đất và "
        "sóng trời, dịch pha ngày đêm thường khá nhỏ (dưới 500 ns). Tuy nhiên, nếu độ dài đường vượt "
        "1500 km, máy thu có thể mất khoá và “nhảy” sang chu kỳ khác của sóng mang. Mỗi lần nhảy chu kỳ gây "
        "sai số thời gian 10 µs, bằng chu kỳ của 100 kHz."))
    b.append(p(
        "LORAN-C không cung cấp mã thời gian, nhưng có thể cung cấp xung đúng giờ tham chiếu UTC. Điều này "
        "khả thi vì thời điểm đến của một nhóm xung trùng với giây UTC theo một chu kỳ đều đặn. Thời điểm "
        "trùng này (time of coincidence — TOC) xảy ra mỗi 4 đến 16 phút, tùy chuỗi đang bám. Để có đầu ra "
        "1 pps đồng bộ, cần một máy thu thời gian có khả năng TOC và một ước lượng trễ đường truyền tốt. "
        "Cũng cần một bảng TOC cho chuỗi đang bám (có sẵn từ Đài Thiên văn Hải quân Hoa Kỳ). Khi đồng hồ "
        "LORAN-C đã được đặt đúng giờ, nó có thể tạo đầu ra 1 pps với độ không đảm bảo ±500 ns [12, 16]."))
    b.append(h3("Vệ tinh môi trường địa tĩnh (GOES)",
                "Geostationary Operational Environmental Satellite (GOES)"))
    b.append(p(
        "NIST cung cấp mã thời gian liên tục qua các vệ tinh GOES (Geostationary Operational Environmental "
        "Satellite). Các vệ tinh này do Cục Đại dương và Khí quyển Quốc gia (NOAA) vận hành. Dịch vụ phủ "
        "toàn bộ Tây Bán cầu."))
    b.append(p(
        "Hai vệ tinh được dùng để phát thời gian. GOES/East ở kinh độ 75° Tây phát trên sóng mang 468,8375 "
        "MHz. GOES/West ở kinh độ 135° Tây phát trên sóng mang 468,825 MHz. Các vệ tinh ở quỹ đạo địa tĩnh "
        "36.000 km trên xích đạo. Đồng hồ chủ GOES được đồng bộ với UTC(NIST) và đặt tại cơ sở của NOAA ở "
        "Wallops Island, VA. Các vệ tinh đóng vai trò bộ phát đáp (transponder) chuyển tiếp tín hiệu từ "
        "đồng hồ chủ."))
    b.append(p(
        "Mã thời gian GOES gồm năm, ngày trong năm, giờ, phút, giây, hiệu chỉnh DUT1, thông tin vị trí vệ "
        "tinh, và chỉ báo Giờ mùa hè cùng giây nhuận. Mã thời gian được xen kẽ với các thông điệp NOAA dùng "
        "để liên lạc với hệ thu thập dữ liệu thời tiết. Một thông điệp 50 bit được gửi mỗi 0,5 s, nhưng chỉ "
        "4 bit đầu (một từ BCD) chứa thông tin thời gian. Một khung mã thời gian đầy đủ gồm 60 từ BCD và "
        "mất 30 s để nhận."))
    b.append(p(
        "Bằng cách dùng thông tin vị trí vệ tinh, thiết bị thu GOES có thể đo và bù trễ đường truyền nếu "
        "biết toạ độ máy thu. Độ không đảm bảo thời gian của dịch vụ GOES là ±100 µs [15]."))
    b.append(h3("Hệ Định vị Toàn cầu (GPS)", "Global Positioning System (GPS)"))
    b.append(p(
        "Hệ Định vị Toàn cầu (GPS) là hệ dẫn đường vô tuyến do Bộ Quốc phòng Hoa Kỳ (DOD) phát triển và vận "
        "hành. Nó gồm một chòm 24 vệ tinh bay quanh Trái Đất (21 vệ tinh chính và 3 vệ tinh dự phòng trên "
        "quỹ đạo). 24 vệ tinh bay quanh Trái Đất trên sáu mặt phẳng cố định nghiêng 55° so với xích đạo. "
        "Mỗi vệ tinh ở độ cao 20.200 km và có chu kỳ quỹ đạo 11 h 58 min, nghĩa là một vệ tinh sẽ đi qua "
        "cùng một nơi trên Trái Đất sớm hơn 4 min mỗi ngày. Vì các vệ tinh liên tục bay quanh Trái Đất, GPS "
        "phải dùng được ở bất cứ đâu trên bề mặt Trái Đất."))
    b.append(p(
        "Mỗi vệ tinh GPS phát trên hai sóng mang: L1 ở 1575,42 MHz và L2 ở 1227,6 MHz. Mỗi vệ tinh phát một "
        "dạng sóng trải phổ gọi là mã tạp giả ngẫu nhiên (PRN) trên L1 và L2, và mỗi vệ tinh được nhận diện "
        "bằng mã PRN mà nó phát. Có hai loại mã PRN. Loại thứ nhất là mã thu thập thô (C/A) với tốc độ chip "
        "1023 chip mỗi mili giây. Loại thứ hai là mã chính xác (P) với tốc độ chip 10230 chip mỗi mili "
        "giây. Mã C/A lặp lại mỗi mili giây. Mã P chỉ lặp lại mỗi 267 ngày, nhưng vì lý do thực tế được đặt "
        "lại mỗi tuần. Mã C/A phát trên L1, mã P phát trên cả L1 và L2."))
    b.append(p(
        "Vì lý do an ninh quốc gia, DOD khởi động chương trình Giảm độ chính xác có chọn lọc (Selective "
        "Availability — SA) năm 1990. SA cố ý làm tăng độ không đảm bảo định vị và thời gian của GPS bằng "
        "cách thêm khoảng 300 ns nhiễu vào cả mã C/A và mã P. Tín hiệu thu được phân phối qua Dịch vụ Định "
        "vị Tiêu chuẩn (SPS). SPS dành cho dùng toàn cầu và ai có máy thu GPS cũng dùng miễn phí. Dịch vụ "
        "Định vị Chính xác (PPS) chỉ dành cho người dùng được quân đội Hoa Kỳ cấp phép. Người dùng PPS cần "
        "máy thu đặc biệt dùng logic mật mã để loại bỏ tác động của SA. Vì PPS bị hạn chế, gần như mọi "
        "người dùng GPS dân sự đều dùng SPS."))
    b.append(h3("Dùng GPS ở chế độ một chiều", "Using GPS in One-Way Mode"))
    b.append(p(
        "GPS có tỉ lệ giá/hiệu năng tốt nhất trong mọi hệ truyền thời gian hiện nay. Máy thu có giá từ dưới "
        "500 USD cho bo mạch thời gian OEM, đến 20.000 USD hoặc hơn cho các mẫu tinh vi nhất. Giá thường "
        "phụ thuộc chất lượng bộ dao động thời gốc của máy thu. Mẫu giá thấp có thời gốc chất lượng thấp, "
        "phải liên tục được lái để bám tín hiệu GPS. Máy thu giá cao có thời gốc tốt hơn (một số có bộ dao "
        "động rubidi bên trong) và có thể bỏ qua nhiều biến thiên đường truyền GPS vì bộ dao động cho phép "
        "chúng “trôi” trong khoảng lâu hơn."))
    b.append(p(
        "Để dùng hầu hết máy thu, chỉ cần lắp ăng-ten, nối ăng-ten với máy thu và bật máy. Ăng-ten thường là "
        "một hình nón hay đĩa nhỏ (đường kính thường khoảng 15 cm) và phải lắp ngoài trời nơi có tầm nhìn "
        "bầu trời rõ ràng, không vật cản. Khi bật, máy thu thực hiện tìm kiếm bầu trời để biết vệ tinh nào "
        "đang trên đường chân trời và nhìn thấy từ vị trí ăng-ten. Máy thu sau đó thu hai khối dữ liệu (gọi "
        "là almanac và ephemeris) từ các vệ tinh tìm thấy. Khi xong, nó có thể tính toạ độ ba chiều (vĩ độ, "
        "kinh độ, độ cao) miễn là bốn vệ tinh trong tầm nhìn. Máy thu sau đó có thể bù trễ đường truyền và "
        "đồng bộ xung đúng giờ của mình."))
    b.append(p(
        "Nếu ăng-ten có tầm nhìn bầu trời rõ ràng, ít nhất bốn vệ tinh luôn trong tầm nhìn và máy thu luôn "
        "tính được vị trí. Máy thu GPS đơn giản nhất chỉ có một kênh và quan sát nhiều vệ tinh bằng sơ đồ "
        "tuần tự chuyển nhanh giữa các vệ tinh. Mẫu tinh vi hơn có khả năng bám song song và gán một kênh "
        "riêng cho mỗi vệ tinh trong tầm nhìn. Những máy thu này thường bám 5 đến 12 vệ tinh cùng lúc (dù "
        "hơn 8 chỉ có trong trường hợp hiếm). Bằng cách lấy trung bình dữ liệu từ nhiều vệ tinh, máy thu có "
        "thể loại bỏ một phần tác động của SA và giảm độ không đảm bảo thời gian."))
    b.append(h3("Hiệu năng GPS ở chế độ một chiều", "GPS Performance in One-Way Mode"))
    b.append(p(
        "Hầu hết máy thu thời gian GPS cung cấp xung đúng giờ 1 pps. GPS cũng phát ba mẩu thông tin thời "
        "gian: số tuần kể từ khi bắt đầu giờ GPS (5 tháng 1 năm 1980); giây hiện tại trong tuần hiện tại; "
        "và số giây nhuận kể từ khi bắt đầu giờ GPS. Dùng hai mẩu đầu, máy thu GPS có thể khôi phục giờ GPS. "
        "Thêm thông tin giây nhuận, máy thu khôi phục được UTC. Giờ GPS khác UTC ở số giây nhuận đã xảy ra "
        "kể từ ngày 5 tháng 1 năm 1980."))
    b.append(p(
        "Hầu hết máy thu GPS xuất UTC ở định dạng thời điểm truyền thống: tháng, ngày, năm, giờ, phút, giây. "
        "Bảng 18.3 liệt kê các chỉ tiêu độ không đảm bảo UTC cho cả SPS và PPS."))
    b.append(table(
        ["Dịch vụ", "Độ KĐB (ns) phân vị 50", "Độ KĐB (ns) 1σ", "Độ KĐB (ns) 2σ"],
        [["SPS", "±115", "±170", "±340"],
         ["PPS", "±68", "±100", "±200"]],
        "Bảng 18.3 · Độ không đảm bảo thời gian của GPS ở chế độ một chiều."))
    b.append(p(
        "Vì gần như mọi máy thu GPS chỉ dùng được SPS, hàng đầu của bảng là đáng quan tâm nhất. Nó cho thấy "
        "có 50% xác suất một xung đúng giờ từ GPS nằm trong ±115 ns so với UTC. Độ không đảm bảo 1σ của "
        "GPS (~68% xác suất) là ±170 ns, và 2σ (95%) là ±340 ns. Để đạt các độ không đảm bảo ở Bảng 18.3, "
        "phải hiệu chỉnh trễ máy thu và ăng-ten, và ước lượng sai số đồng bộ. Vì lý do này, một số nhà sản "
        "xuất thiết bị GPS nêu độ không đảm bảo thời gian ±1 µs. Chỉ tiêu này dễ đáp ứng, kể cả khi trễ máy "
        "thu và ăng-ten được ước lượng thô hoặc bỏ qua. Các nhà sản xuất khác dùng kỹ thuật lấy trung bình "
        "hay thuật toán cố “loại bỏ” SA; họ có thể nêu chỉ tiêu ±100 ns hoặc thấp hơn [17, 18]."))
    b.append(h3("Dùng GPS ở chế độ common-view", "Using GPS in Common-View Mode"))
    b.append(p(
        "Chế độ common-view được dùng để đồng bộ hay so sánh các chuẩn thời gian hoặc thang thời gian tại "
        "hai hay nhiều vị trí. GPS common-view là phương pháp BIPM dùng để thu dữ liệu từ các phòng thí "
        "nghiệm đóng góp cho TAI."))
    b.append(p(
        "Truyền thời gian common-view cần một máy thu GPS thiết kế đặc biệt có thể đọc một lịch bám. Lịch "
        "này cho máy thu biết khi nào bắt đầu đo và bám vệ tinh nào. Một người dùng khác ở vị trí khác dùng "
        "cùng lịch và thực hiện phép đo đồng thời từ cùng vệ tinh. Lịch bám phải được thiết kế để chọn các "
        "vệ tinh nhìn thấy bởi cả hai người dùng ở góc ngẩng hợp lý."))
    b.append(p(
        "Mỗi trạm đo hiệu giữa đồng hồ cục bộ và vệ tinh. Thường các phép đo được thực hiện trong một lần "
        "vệ tinh đi qua kéo dài dưới 15 phút. Các phép đo riêng lẻ ở mỗi trạm là ước lượng của (Clock A − "
        "GPS) và (Clock B − GPS). Nếu trừ hai kết quả này, đồng hồ GPS triệt tiêu và còn lại ước lượng của "
        "(Clock A − Clock B). Vì sai số đồng hồ GPS (gồm cả SA) không ảnh hưởng tới kết quả, độ không đảm "
        "bảo của GPS common-view có thể nhỏ tới ±5 ns [19]."))
    b.append(p(
        "Dù common-view quan trọng cho so sánh thời gian quốc tế, nó không thực tế với người dùng bình "
        "thường vì vài lý do. Thứ nhất, nó đòi hỏi trao đổi dữ liệu với người dùng khác. Thứ hai, common-view "
        "không cung cấp dữ liệu liên tục, mà chỉ trong các lần so sánh kéo dài dưới 15 phút. Và cuối cùng, "
        "common-view không hoạt động theo thời gian thực; ta không biết độ không đảm bảo thời gian cho tới "
        "sau khi trao đổi dữ liệu."))
    b.append(p("Bảng 18.4 tóm tắt các tín hiệu truyền thời gian vô tuyến khác nhau."))
    b.append(table(
        ["Tín hiệu truyền thời gian vô tuyến", "Hiệu năng không hiệu chỉnh đường truyền",
         "Giới hạn hệ thống điển hình", "Cần gì để đạt giới hạn hiệu năng"],
        [["HF (WWV/WWVH)", "−30 ms (trễ phụ thuộc khoảng cách tới máy phát)", "±1 ms",
          "Ước lượng trễ đường truyền, mô hình truyền sóng"],
         ["Vệ tinh GOES", "±16 ms", "±100 µs", "Máy thu hiệu chỉnh trễ đường truyền"],
         ["WWVB", "−10 ms (trễ phụ thuộc khoảng cách tới máy phát)", "±100 µs",
          "Ước lượng trễ đường truyền, biết trễ thiết bị và ăng-ten"],
         ["LORAN-C", "±10 µs", "±500 ns",
          "Ước lượng trễ đường truyền, máy thu có TOC, bảng TOC, biết trễ thiết bị và ăng-ten"],
         ["GPS (một chiều)", "±340 ns", "±100 ns",
          "Máy thu GPS thương mại lấy trung bình nhiều vệ tinh; biết trễ thiết bị và ăng-ten"],
         ["GPS (common-view)", "±20 ns", "±5 ns",
          "Máy thu common-view, lịch bám, một người dùng/phòng thí nghiệm trao đổi dữ liệu; biết trễ thiết bị và ăng-ten"]],
        "Bảng 18.4 · Hiệu năng của các tín hiệu truyền thời gian vô tuyến."))
    b.append(p(
        "Bảng 18.5 liệt kê một số nhà sản xuất đồng hồ vô tuyến, gồm đồng hồ dùng tín hiệu HF, WWVB hay "
        "LF khác, LORAN-C, GPS và GPS common-view (GPS-CV). Nhiều loại thiết bị sẵn có cho nhiều ứng dụng; "
        "liên hệ nhà sản xuất để biết chi tiết."))
    b.append(table(
        ["Nhà sản xuất", "Địa điểm", "Loại máy thu"],
        [["Absolute Time", "San Jose, CA", "GPS"],
         ["Arbiter", "Paso Robles, CA", "GPS"],
         ["Allen Osborne", "Westlake Village, CA", "GPS, GPS-CV"],
         ["Ashtech", "Sunnyvale, CA", "GPS"],
         ["Austron", "Austin, TX", "LORAN, GPS, GPS-CV"],
         ["Bancomm", "San Jose, CA", "GPS"],
         ["Chrono-Log", "Havertown, PA", "HF, GPS"],
         ["Datum", "Anaheim, CA", "GPS"],
         ["Efratom", "Irvine, CA", "GPS"],
         ["ESE", "El Segundo, CA", "GPS"],
         ["Franklin Instrument", "Warminster, PA", "LF"],
         ["Frequency and Time Systems", "Beverly, MA", "GPS"],
         ["Garmin", "Lenexa, KS", "GPS"],
         ["Heath", "Benton Harbor, MI", "HF"],
         ["Hewlett-Packard", "Santa Clara, CA", "GPS"],
         ["Macrodyne", "Clifton Park, NY", "GPS"],
         ["Magellan", "San Dimas, CA", "GPS"],
         ["Motorola", "Northbrook, IL", "GPS"],
         ["Odetics", "Anaheim, CA", "GPS"],
         ["Rockwell", "Newport Beach, CA", "GPS"],
         ["Spectracom", "East Rochester, NY", "LF, GPS"],
         ["Spectrum Geophysical", "West Covina, CA", "GPS"],
         ["Stanford Research", "Sunnyvale, CA", "LORAN"],
         ["Stanford Telecomm", "Santa Clara, CA", "GPS"],
         ["Telecom Solutions", "San Jose, CA", "GPS"],
         ["Tracor", "Austin, TX", "LF"],
         ["Trak Systems", "Tampa, FL", "GPS"],
         ["Trimble", "Sunnyvale, CA", "GPS"],
         ["True Time", "Santa Rosa, CA", "HF, LF, GPS"]],
        "Bảng 18.5 · Các nguồn đồng hồ vô tuyến (theo nguồn Ch18)."))

    # ---- 18.7
    b.append(h2("18.7 Tín hiệu truyền thời gian cho máy tính", "Computer Time Transfer Signals"))
    b.append(p(
        "Một trong những bài toán truyền thời gian phổ biến nhất là đồng bộ đồng hồ máy tính. Đồng hồ vô "
        "tuyến như mô tả ở phần trước thường được dùng để giữ thời gian cho máy tính. Tuy nhiên, dùng dịch "
        "vụ thời gian qua điện thoại hoặc Internet thường tiện lợi và rẻ hơn mua đồng hồ vô tuyến [20]."))
    b.append(h3("Dịch vụ đặt giờ qua điện thoại (quay số)", "Dial-Up Time Setting Services"))
    b.append(p(
        "Dịch vụ thời gian quay số cho phép máy tính đồng bộ đồng hồ bằng một đường điện thoại thường. Để "
        "minh hoạ cách các dịch vụ này hoạt động, hãy xem Dịch vụ Thời gian Máy tính Tự động (ACTS) của "
        "NIST, ra mắt năm 1988."))
    b.append(p(
        "ACTS cần một máy tính, một modem và phần mềm đơn giản. Khi máy tính kết nối với ACTS qua điện "
        "thoại, nó nhận một mã thời gian ASCII. Thông tin trong mã này dùng để đồng bộ đồng hồ máy tính. "
        "ACTS dùng được ở tốc độ modem tới 9600 baud với 8 bit dữ liệu, 1 bit stop và không parity. Để nhận "
        "mã thời gian đầy đủ, phải kết nối ở 1200 baud hoặc cao hơn. Mã thời gian đầy đủ được truyền mỗi "
        "giây một lần và chứa nhiều thông tin hơn mã 300 baud (truyền mỗi 2 s). Bảng 18.6 mô tả mã thời "
        "gian ACTS đầy đủ."))
    b.append(table(
        ["Mã", "Ý nghĩa"],
        [["JJJJJ", "Ngày Julius biến đổi (MJD) — năm chữ số cuối của Ngày Julius, là số ngày kể từ 1 tháng 1 năm 4713 TCN."],
         ["YR-MO-DA", "Năm, tháng, ngày."],
         ["HH:MM:SS", "Giờ, phút, giây. Thời gian luôn truyền theo UTC; phải áp một độ lệch để có giờ địa phương."],
         ["TT", "Mã hai chữ số chỉ Hoa Kỳ đang ở Giờ chuẩn (ST) hay Giờ mùa hè (DST), và khi nào ST/DST sắp tới. Mã bằng 00 khi ST, 50 khi DST; trong tháng đổi giờ, số này giảm 1 mỗi ngày cho tới khi đổi."],
         ["L", "Mã một chữ số chỉ có thêm hay bớt giây nhuận vào nửa đêm ngày cuối tháng hiện tại: 0 = không, 1 = thêm giây nhuận dương, 2 = bớt một giây."],
         ["DUT1", "Hiệu hiện tại giữa UT1 và UTC; cộng vào UTC để có UT1. Hiệu chỉnh từ −0,8 đến 0,8 s."],
         ["msADV", "Mã năm chữ số hiển thị số mili giây NIST đẩy sớm mã thời gian. Mặc định 45,0 ms, nhưng đổi theo trễ đường thực nếu OTM được dội về NIST."],
         ["UTC(NIST)", "Nhãn cho biết đang nhận UTC từ NIST."],
         ["<OTM>", "Một ký tự gửi ở cuối mỗi mã thời gian; ban đầu là dấu sao (*), đổi thành dấu thăng (#) nếu ACTS đã hiệu chỉnh đường truyền thành công."]],
        "Bảng 18.6 · Mã thời gian của Dịch vụ Thời gian Máy tính Tự động (ACTS)."))
    b.append(p(
        "Ký tự cuối trong mã thời gian là dấu đúng giờ (on-time marker — OTM). Các giá trị trong mã thời "
        "gian chỉ thời điểm đến của OTM. Nói cách khác, nếu mã ghi 12:45:45, nghĩa là 12:45:45 khi OTM "
        "đến. Để bù trễ đường truyền giữa NIST và người dùng, ACTS gửi OTM sớm 45 ms. Mức đẩy sớm 45 ms "
        "được chọn dựa trên thực nghiệm với modem 1200 baud: 8 ms để gửi OTM ở 1200 baud, 7 ms cho thời "
        "gian truyền giữa NIST và một người dùng điển hình, và 30 ms cho trễ xử lý modem."))
    b.append(p(
        "Đẩy sớm OTM 45 ms luôn giảm bớt trễ đường truyền. Tuy nhiên, ACTS có thể hiệu chỉnh đường truyền "
        "thực bằng phương pháp loop-back. Phương pháp loop-back được thực hiện nếu phần mềm của người dùng "
        "gửi OTM trở lại ACTS sau khi nhận. Mỗi lần OTM được gửi về, ACTS đo trễ đường khứ hồi, chia đôi để "
        "có trễ một chiều. Sau ba lần đo nhất quán, ACTS đẩy sớm OTM đúng bằng trễ một chiều. Ví dụ, nếu "
        "trễ một chiều là 50,4 ms, ACTS gửi OTM sớm 50,4 ms (thay vì 45 ms). Khi đó đường truyền đã được "
        "hiệu chỉnh, và OTM đổi từ dấu sao sang dấu thăng (#). Nếu dùng tuỳ chọn loop-back, độ không đảm "
        "bảo của ACTS là ±5 ms [21]."))
    b.append(p(
        "Một số dịch vụ quay số tương tự ACTS liệt kê ở Bảng 18.7. Các dịch vụ này đều truyền mã thời gian "
        "ở dạng ASCII, nhưng dùng vài định dạng khác nhau. Do thiếu chuẩn hoá, phần mềm truy cập nhiều "
        "dịch vụ phải hiểu được vài định dạng mã thời gian khác nhau."))
    b.append(table(
        ["Tổ chức", "Địa điểm", "Số điện thoại"],
        [["Viện Vật lý và Đo lường Liên bang (PTB)", "Đức", "011-49-53-1-512038"],
         ["Hội đồng Nghiên cứu Quốc gia (NRC)", "Canada", "(613) 745-3900, Ottawa; (416) 445-9408, Toronto"],
         ["Trung tâm Đo lường Quốc gia (CENAM)", "Mexico", "011-52-42-110505"],
         ["Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST)", "Boulder, CO", "(303) 494-4774"],
         ["Đài Thiên văn Quốc gia Rio de Janeiro (ONRJ)", "Brazil", "011-55-21-580-0677"],
         ["Đại học Kỹ thuật Graz (TUG)", "Áo", "011-433-16472366"],
         ["Phòng Thí nghiệm Viễn thông (TL)", "Đài Loan, Trung Quốc", "011-886-3-424-5490"],
         ["Đài Thiên văn Hải quân Hoa Kỳ (USNO)", "Washington, D.C.", "(202) 762-1594"]],
        "Bảng 18.7 · Các dịch vụ đặt giờ qua điện thoại quay số."))
    b.append(h3("Dịch vụ đặt giờ qua mạng", "Network Time Setting Services"))
    b.append(p(
        "Máy tính nối Internet có thể được đồng bộ mà không tốn phí dịch vụ quay số. Các máy chủ thời gian "
        "Internet cung cấp mức chuẩn hoá cao hơn dịch vụ quay số. Một số giao thức thời gian chuẩn được "
        "định nghĩa trong loạt tài liệu RFC (Request for Comments), có thể tải từ nhiều trang Internet. Bốn "
        "giao thức thời gian chính là Time Protocol, Daytime Protocol, Network Time Protocol (NTP) và "
        "Simple Network Time Protocol (SNTP). Bảng 18.8 tóm tắt các giao thức và cổng gán của chúng, tức "
        "cổng mà máy chủ thời gian “lắng nghe” yêu cầu từ máy khách [22–26]."))
    b.append(table(
        ["Giao thức", "Tài liệu", "Định dạng", "Cổng gán"],
        [["Time Protocol", "RFC-868",
          "Số nhị phân 32 bit không định dạng, chứa thời gian bằng số giây UTC kể từ 1/1/1900.", "Cổng 37, tcp/ip, udp/ip"],
         ["Daytime Protocol", "RFC-867",
          "Định dạng chính xác không quy định trong chuẩn; chỉ yêu cầu mã thời gian gửi dạng ký tự ASCII, thường giống mã của dịch vụ quay số như ACTS.",
          "Cổng 13, tcp/ip, udp/ip"],
         ["Network Time Protocol (NTP)", "RFC-1305",
          "Máy chủ đáp mỗi truy vấn bằng gói dữ liệu định dạng NTP, gồm dấu thời gian 64 bit (giây UTC kể từ 1/1/1900, độ phân giải 200 ps, độ không đảm bảo 1–50 ms). Phần mềm NTP chạy nền liên tục trên máy khách, định kỳ nhận cập nhật.",
          "Cổng 123, udp/ip"],
         ["Simple Network Time Protocol (SNTP)", "RFC-1769",
          "Một phiên bản NTP không đổi đặc tả nhưng đơn giản hoá vài đặc điểm thiết kế; dành cho máy không “cần hoặc không đáng” dùng toàn bộ hiệu năng NTP.",
          "Cổng 123, udp/ip"]],
        "Bảng 18.8 · Các giao thức thời gian Internet."))
    b.append(p(
        "NIST vận hành Dịch vụ Thời gian Mạng phân phối thời gian theo định dạng Time, Daytime và NTP từ "
        "nhiều máy chủ [27]. Máy tính nhỏ (PC) thường dùng Daytime Protocol. Máy tính lớn và máy trạm "
        "thường dùng NTP, và phần mềm NTP thường được cài kèm hệ điều hành. Mã thời gian Daytime rất giống "
        "ACTS. Như ACTS, mã Daytime được gửi sớm (50 ms), nhưng máy chủ không hiệu chỉnh đường truyền. Tuy "
        "vậy, độ không đảm bảo thời gian ở hầu hết vị trí vào khoảng ±50 ms."))
    b.append(p(
        "Phần mềm truy cập các dịch vụ thời gian quay số và mạng khác nhau có sẵn cho mọi hệ điều hành "
        "chính. Ta thường tải được bản dùng thử (shareware) từ Internet hoặc dịch vụ trực tuyến khác."))

    # ---- 18.8
    b.append(h2("18.8 Những phát triển tương lai", "Future Developments"))
    b.append(p(
        "Cả việc thực hiện giây SI lẫn hiệu năng các kỹ thuật truyền thời gian sẽ tiếp tục được cải thiện. "
        "Một hướng phát triển hứa hẹn là việc dùng ngày càng nhiều các chuẩn đài phun xêzi (cesium "
        "fountain). Các thiết bị này hoạt động bằng cách làm lạnh nguyên tử bằng laser rồi ném chúng lên "
        "theo phương thẳng đứng; tần số cộng hưởng được phát hiện khi nguyên tử đi lên và rơi xuống dưới "
        "tác dụng trọng lực. Nhiều phòng thí nghiệm đang nghiên cứu ý tưởng này, hứa hẹn cải thiện đáng kể "
        "so với chuẩn chùm tia xêzi hiện có [28]. Về lâu dài, một chuẩn ion bị bẫy có thể đem lại cải thiện "
        "vài bậc độ lớn. Chuẩn này lấy tần số cộng hưởng từ các dịch chuyển năng lượng có hệ thống trong "
        "một số ion nhất định; độ không đảm bảo tần số của thiết bị như vậy cuối cùng có thể đạt ±1 × 10⁻¹⁸ "
        "[29]."))
    b.append(p(
        "Tương lai của truyền thời gian sẽ ngày càng dựa nhiều hơn vào các hệ dựa trên vệ tinh. Các hệ đặt "
        "trên mặt đất như LORAN-C dự kiến sẽ bị loại bỏ dần [30]. Độ không đảm bảo thời gian của GPS sẽ cải "
        "thiện nếu chương trình SA được ngừng (như dự kiến) vào đầu thế kỷ sau [31]. GLONASS, đối tác Nga "
        "của GPS, có thể được dùng rộng rãi hơn [32]. Và trong tương lai gần, một dịch vụ truyền thời gian "
        "từ các vệ tinh địa tĩnh INMARSAT có thể sẵn có; dịch vụ này dùng công nghệ tương tự GPS nhưng hứa "
        "hẹn hiệu năng tốt hơn."))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>J. Jesperson and J. Fitz-Randolph, <i>From Sundials to Atomic Clocks: Understanding Time and Frequency</i>, Nat. Bur. of Stan. Monograph 155, 1977.</li>'
             '<li>C. Hackman and D. B. Sullivan, Resource letter TFM-1: time and frequency measurement, <i>Am. J. Phys.</i>, 63(4), 306–317, 1995.</li>'
             '<li>W. M. Itano and N. F. Ramsey, Accurate measurement of time, <i>Sci. Am.</i>, 269(1), 56–65, 1993.</li>'
             '<li>W. A. Marrison, The evolution of the quartz crystal clock, <i>Bell Systems Tech. J.</i>, 27(3), 510–588, 1948.</li>'
             '<li>F. L. Walls and J. Gagnepain, Environmental sensitivities of quartz oscillators, <i>IEEE Trans. Ultrason., Ferroelectr., Freq. Control</i>, 39, 241–249, 1992.</li>'
             '<li>L. Lewis, An introduction to frequency standards, <i>Proc. IEEE</i>, 79(7), 927–935, 1991.</li>'
             '<li>P. L. Bender, E. C. Beaty, and A. R. Chi, Optical detection of narrow Rb87 hyperfine absorption lines, <i>Phys. Rev. Lett.</i>, 1(9), 311–313, 1958.</li>'
             '<li>J. Sherwood, H. Lyons, R. McCracken, and P. Kusch, High frequency lines in the hfs spectrum of cesium, <i>Bull. Am. Phys. Soc.</i>, 27, 43, 1952.</li>'
             '<li>H. Goldenberg, D. Kleppner, and N. Ramsey, Atomic hydrogen maser, <i>Phys. Rev. Lett.</i>, 5, 361–362, 1960.</li>'
             '<li>P. K. Seidelmann, ed., <i>Explanatory Supplement to the Astronomical Almanac</i>, Mill Valley, CA: University Science Books, 1992.</li>'
             '<li>T. J. Quinn, The BIPM and the accurate measurement of time, <i>Proc. IEEE</i>, 79(7), 894–905, 1991.</li>'
             '<li>G. Kamas and M. A. Lombardi, <i>Time and Frequency Users Manual</i>, Natl. Inst. of Stan. Special Publ. 559, 1991.</li>'
             '<li>D. B. Sullivan and J. Levine, Time generation and distribution, <i>Proc. IEEE</i>, 79(7), 906–914, 1991.</li>'
             '<li>Radiocommunication Study Group 7, <i>Time Signals and Frequency Standard Emissions</i>, ITU-R, TF Series, 1994.</li>'
             '<li>R. Beehler and M. A. Lombardi, <i>NIST Time and Frequency Services</i>, Natl. Inst. of Stan. Special Publication 432, 1991.</li>'
             '<li>G. Hefley, <i>The Development of LORAN-C Navigation and Timing</i>, Natl. Bur. of Stan. Monograph 129, 1972.</li>'
             '<li>B. Hoffmann-Wellenhof, H. Lichtenegger, and J. Collins, <i>GPS: Theory and Practice</i>, 3rd ed., New York: Springer-Verlag, 1994.</li>'
             '<li>ARINC Research Corporation, <i>NAVSTAR Global Positioning System: User’s Overview</i>, NAVSTAR GPS Joint Program Office, Los Angeles, YEE-82-009D, March 1991.</li>'
             '<li>W. Lewandowski, G. Petit, and C. Thomas, Precision and accuracy of GPS time transfer, <i>IEEE Trans. Instrum. Meas.</i>, 42(2), 474–479, 1993.</li>'
             '<li>M. A. Lombardi, Keeping time on your PC, <i>BYTE Magazine</i>, 18(11), 57–62, 1993.</li>'
             '<li>J. Levine, M. Weiss, D. D. Davis, D. W. Allan, and D. B. Sullivan, The NIST automated computer time service, <i>Natl. Inst. of Stan. J. Res.</i>, 94, 311–321, 1989.</li>'
             '<li>D. L. Mills, Internet time synchronization: the network time protocol, <i>IEEE Trans. Comm.</i>, 39, 1482–1493, 1991.</li>'
             '<li>D. L. Mills, <i>Network Time Protocol (Version 3) Specification, Implementation, and Analysis</i>, RFC 1305, University of Delaware, March 1992.</li>'
             '<li>D. L. Mills, <i>Simple Network Time Protocol (SNTP)</i>, RFC 1769, University of Delaware, March 1995.</li>'
             '<li>J. Postel, <i>Daytime Protocol</i>, RFC 867, USC/Information Sciences Institute, May 1983.</li>'
             '<li>J. Postel and K. Harrenstien, <i>Time Protocol</i>, RFC 868, USC/Information Sciences Institute, May 1983.</li>'
             '<li>J. Levine, The NIST Internet Time Service, <i>Proc. 25th Annu. PTTI Meeting</i>, 1993, 505–511.</li>'
             '<li>A. Clairon, P. Laurent, G. Santarelli, S. Ghezali, S. N. Lea, and M. Bahoura, A cesium fountain frequency standard: preliminary results, <i>IEEE Trans. Instrum. Meas.</i>, 44, 128–131, 1995.</li>'
             '<li>W. M. Itano, Atomic ion frequency standards, <i>Proc. IEEE</i>, 79, 936–942, 1991.</li>'
             '<li>U.S. Dept. of Transportation, <i>Federal Radionavigation Plan</i>, DOT-VNTSC-RSPA-95-1, DOD-4650.5, 1994.</li>'
             '<li>G. Gibbons, A national GPS policy, <i>GPS World</i>, 7(5), 48–50, 1996.</li>'
             '<li>P. Daly, N. B. Koshelyaevsky, W. Lewandowski, G. Petit, and C. Thomas, Comparison of GLONASS and GPS time transfers, <i>Metrologia</i>, 30(2), 89–94, 1993.</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 17</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is the English companion to the Vietnamese translation of Chapter 18, “Time "
        "Measurement” by Michael A. Lombardi (NIST). All three figures are redrawn as vectors and the eight "
        "tables (18.1–18.8) and equation 18.1 are reproduced. The Vietnamese prose is not repeated here."))
    b.append(p(
        "Time measurements fall into two categories: time-of-day (a labelled instant: year, month, day, "
        "hour, minute, second) and time interval (the elapsed time between two events). Time interval is one "
        "of the four basic measurement standards and can be measured with the highest resolution and lowest "
        "uncertainty. Timekeeping needs a periodic event (resonator), an energy source, a counter and a "
        "display — together a clock, and the resulting ordered scheme a time scale."))
    b.append(p(
        "Section 18.1 — the evolution of clocks. Every clock has a resonator (the pendulum, the quartz "
        "crystal, the atom), an energy source, a counter and a display. Table 18.1 relates frequency "
        "uncertainty to timing uncertainty over 1 s, 1 h and 1 day. From sundials (3500 BC) through verge "
        "escapements (14th c., ±15 min/day), Huygens’s pendulum (1656, <1 min/day), Harrison’s marine "
        "chronometer (1761, ~1/3 s/day), the Shortt two-pendulum clock (1921, a few s/year) to the quartz "
        "crystal clock (1927, ±100 µs/day), each advance sought a more stable resonator. Quartz relies on a "
        "size-dependent mechanical vibration, is sensitive to environment, and so gave way to atomic "
        "oscillators. Table 18.2 summarises the evolution."))
    b.append(p(
        "Section 18.2 — atomic oscillators use quantised energy levels: the resonance frequency is "
        "f=(E₂−E₁)/h (Eq. 18.1). Three types: rubidium (6.835 GHz Rb87, ±5×10⁻¹⁰…±5×10⁻¹², $2–8k), cesium "
        "beam (9.1926 GHz, defines the SI second; NIST-7 ±5×10⁻¹⁵; commercial ≥±5×10⁻¹², $30–80k), and the "
        "hydrogen maser (1.42 GHz, best performance but >$200k). Section 18.3 — the SI second is the "
        "duration of 9,192,631,770 periods of the Cs-133 hyperfine transition; TAI is the atomic scale kept "
        "by BIPM (≈250 standards from >40 labs). Before atomic time, astronomical scales were used: the "
        "mean solar second (1/86,400 of a mean solar day) underlies Universal Time — UT0, UT1 (±3 ms/day), "
        "UT2 (smoothed). The ephemeris second (1956–1971) was a fraction of the tropical year; ET was "
        "replaced by TT = TAI + 32.184 s (±10 µs)."))
    b.append(p(
        "Section 18.4 — UTC differs from TAI by an integer number of seconds; leap seconds (on 30 June or "
        "31 December) keep UTC within ±0.9 s of UT1. A positive leap second produces a 61-second minute "
        "(23:59:59 → 23:59:60 → 00:00:00); DUT1 = UT1 − UTC is broadcast. Section 18.5 — time transfer "
        "needs an on-time 1 pps pulse and a time code. The dominant error is path delay (~3.3 µs/km). Five "
        "methods: (1) one-way, user-calibrated (Figure 18.1); (2) one-way, self-calibrating (advance the "
        "signal or compute τ_ab in software); (3) common-view (Figure 18.2); (4) two-way (Figure 18.3); "
        "(5) loop-back. IRIG-B time codes (1 s frame, BCD, dc-level or 1000 Hz AM) are the de-facto "
        "redistribution standard."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Section 18.6 — radio time signals. HF (WWV/WWVH on 2.5/5/10/15/20 MHz) gives worldwide coverage "
        "with cheap receivers, a voice announcement and a 100 Hz IRIG-H time code, best to ~1 s (<30 ms). LF "
        "(WWVB 60 kHz, LORAN-C 100 kHz) can often be received indoors; WWVB sends a BCD code by 10 dB "
        "carrier-power drops, LORAN-C gives on-time pulses at a TOC (no code, ±500 ns). GOES satellites "
        "relay a 50-bit/0.5 s time code (±100 µs with path correction). GPS: 24 satellites in six planes, "
        "L1 1575.42 MHz / L2 1227.6 MHz, C/A and P PRN codes, Selective Availability (SA) adds ~300 ns. "
        "One-way SPS: ±115 ns (50%), ±170 ns (1σ), ±340 ns (2σ) — Table 18.3; common-view GPS reaches ±5 ns. "
        "Tables 18.4 and 18.5 summarise signal performance and radio-clock makers."))
    b.append(p(
        "Section 18.7 — computer time. Dial-up ACTS sends an ASCII time code with an on-time marker advanced "
        "45 ms (loop-back calibration to ±5 ms); Table 18.6 decodes the ACTS code and Table 18.7 lists "
        "dial-up services. Network services use the Time (port 37), Daytime (port 13), NTP and SNTP "
        "(port 123) protocols — Table 18.8. Section 18.8 — future developments: cesium fountains (laser-"
        "cooled, tossed atoms) and trapped-ion standards (potentially ±1×10⁻¹⁸); satellite-based transfer "
        "will dominate, LORAN-C phased out, GPS improving if SA ends, GLONASS and INMARSAT emerging."))
    b.append(p(
        "The chapter closes with 32 references, reproduced in the Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 17</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 18 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 18 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 18 “Đo thời gian” của Michael A. Lombardi (NIST) — sự tiến hoá "
            "đồng hồ, bộ dao động nguyên tử, thang thời gian và giây SI, UTC, truyền thời gian (một chiều, "
            "common-view, hai chiều, loop-back), tín hiệu vô tuyến HF/LF/GOES/GPS và dịch vụ thời gian máy "
            "tính, với 3 hình và 8 bảng." if vi else
            "Companion to Chapter 18 of the CRC Measurement Handbook — time measurement: clocks, atomic "
            "oscillators, time scales, UTC, time transfer, radio and computer time services.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 18' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 18' % BASE_EN)
    meta = ("Chương 18 · theo Ch18.pdf (CRC Press, 1999) · 3 hình, 8 bảng, 32 tài liệu tham khảo" if vi
            else "Chapter 18 · 3 figures, 8 tables, 32 references")
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
