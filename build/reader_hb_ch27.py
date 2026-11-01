# -*- coding: utf-8 -*-
"""Handbook Chapter 27 — Acoustic Measurement
(Per Rasmussen — G.R.A.S. Sound and Vibration).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch27.py
"""
import os

import hb27fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch27-acoustic-measurement"
TITLE_EN = "Acoustic Measurement"
TITLE_VI = "Đo âm học"
BYLINE = "Per Rasmussen (G.R.A.S. Sound and Vibration)"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch26-pressure-and-sound-measurement"
PREV_VI = "ch26-pressure-and-sound-measurement"
PREV_T_EN = "Pressure and Sound Measurement"
PREV_T_VI = "Đo áp suất và âm thanh"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-27-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


def table(hd, rows, cap):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % ("".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ tables data

_INF = "−∞"

_T271_ROWS = [
    ("10", "+2; " + _INF, "+3; " + _INF, "+5; " + _INF, "+5; " + _INF),
    ("12.5", "+2; " + _INF, "+3; " + _INF, "+5; " + _INF, "+5; " + _INF),
    ("16", "+2; " + _INF, "+3; " + _INF, "+5; " + _INF, "+5; " + _INF),
    ("20", "−2", "−3", "−3", "+5; " + _INF),
    ("25", "−1.5", "−2", "−3", "+5; " + _INF),
    ("31.5", "−1", "−1.5", "−3", "−4"),
    ("40", "−1", "−1.5", "−2", "−4"),
    ("50", "−1", "−1.5", "−2", "−3"),
    ("63", "−1", "−1.5", "−2", "−3"),
    ("80", "−1", "−1.5", "−2", "−3"),
    ("100", "−0.7", "−1", "−1.5", "−3"),
    ("125", "−0.7", "−1", "−1.5", "−2"),
    ("160", "−0.7", "−1", "−1.5", "−2"),
    ("200", "−0.7", "−1", "−1.5", "−2"),
    ("250", "−0.7", "−1", "−1.5", "−2"),
    ("315", "−0.7", "−1", "−1.5", "−2"),
    ("400", "−0.7", "−1", "−1.5", "−2"),
    ("500", "−0.7", "−1", "−1.5", "−2"),
    ("630", "−0.7", "−1", "−1.5", "−2"),
    ("800", "−0.7", "−1", "−1.5", "−2"),
    ("1000", "−0.7", "−1", "−1.5", "−2"),
    ("1250", "−0.7", "−1", "−1.5", "−2.5"),
    ("1600", "−0.7", "−1", "−2", "−3"),
    ("2000", "−0.7", "−1", "−2", "−3"),
    ("2500", "−0.7", "−1", "−2.5", "−4"),
    ("3125", "−0.7", "−1", "−2.5", "−4.5"),
    ("4000", "−0.7", "−1", "−3", "−5"),
    ("5000", "−1", "−1.5", "−3.5", "−6"),
    ("6300", "+1; −1.5", "+1.5; −2", "−4.5", "−6"),
    ("8000", "+1; −2", "+1.5; −3", "−5", "−6"),
    ("10000", "+2; −3", "+2; −4", "+5; " + _INF, "+6; " + _INF),
    ("12500", "+2; −3", "+3; −6", "+5; " + _INF, "+6; " + _INF),
    ("16000", "+2; −3", "+3; " + _INF, "+5; " + _INF, "+6; " + _INF),
]


def _t271(lang):
    if lang == "vi":
        hd = ("Tần số (Hz)", "Kiểu 0 (dB)", "Kiểu 1 (dB)", "Kiểu 2 (dB)", "Kiểu 3 (dB)")
        cap = ("Bảng 27.1 · Yêu cầu của IEC 651 đối với máy đo mức âm. Mỗi ô là dung sai cho phép "
               "quanh đáp tuyến chuẩn tại tần số đó; −∞ nghĩa là không giới hạn phía dưới. Kiểu 0 "
               "chính xác nhất (phòng thí nghiệm), kiểu 1 dùng phổ biến, kiểu 2 cho thiết bị giá rẻ, "
               "kiểu 3 hầu như không dùng vì dung sai quá rộng.")
    else:
        hd = ("Frequency (Hz)", "Type 0 (dB)", "Type 1 (dB)", "Type 2 (dB)", "Type 3 (dB)")
        cap = ("Table 27.1 · IEC 651 sound level meter requirements. Each entry is the tolerance "
               "permitted about the reference response at that frequency; −∞ means unlimited below. "
               "Type 0 is the most accurate (laboratory), Type 1 general purpose, Type 2 for "
               "low-cost instruments, Type 3 effectively unused because the tolerances are too wide.")
    return hd, [list(r) for r in _T271_ROWS], cap


_T272_ROWS = [
    ("20", "19.95", "17.8–22.4"),
    ("25", "25.12", "22.4–28.2"),
    ("31.5", "31.62", "28.2–35.5"),
    ("40", "39.81", "35.5–44.7"),
    ("50", "50.12", "44.7–56.2"),
    ("63", "63.1", "56.2–70.8"),
    ("80", "79.43", "70.8–89.1"),
    ("100", "100.0", "89.1–112"),
    ("125", "125.89", "112–141"),
    ("160", "158.49", "141–178"),
    ("200", "199.53", "178–224"),
    ("250", "251.19", "224–282"),
    ("315", "316.23", "282–355"),
    ("400", "398.11", "355–447"),
    ("500", "501.19", "447–562"),
    ("630", "630.96", "562–708"),
    ("800", "794.33", "708–891"),
    ("1000", "1000.0", "891–1120"),
    ("1250", "1258.9", "1120–1410"),
    ("1600", "1584.9", "1410–1780"),
    ("2000", "1995.3", "1780–2240"),
    ("2500", "2511.9", "2240–2820"),
    ("3150", "3162.3", "2820–3550"),
    ("4000", "3981.1", "3550–4470"),
    ("5000", "5011.9", "4470–5620"),
    ("6300", "6309.6", "5620–7080"),
    ("8000", "7943.3", "7080–8910"),
    ("10000", "10000.0", "8910–11200"),
    ("12500", "12589.3", "11200–14100"),
    ("16000", "15848.9", "14100–17800"),
    ("20000", "19952.6", "17800–22400"),
]


def _t272(lang):
    if lang == "vi":
        hd = ("Tần số danh định (Hz)", "Tần số tâm chính xác (Hz)", "Dải thông (Hz)")
        cap = ("Bảng 27.2 · Tần số phân tích 1/3 octave. Dải 20 Hz – 20 kHz gồm 31 bộ lọc, hoạt động "
               "đồng thời trên cùng tín hiệu vào; tần số tâm chính xác bằng 10^(n/10) và mỗi dải thông "
               "rộng bằng một phần ba octave.")
    else:
        hd = ("Nominal center frequency (Hz)", "Exact center frequency (Hz)", "Passband (Hz)")
        cap = ("Table 27.2 · 1/3-octave analysis frequencies. The 20 Hz – 20 kHz range holds 31 "
               "filters running simultaneously on the same input; exact centre frequencies follow "
               "10^(n/10) and each passband spans one third of an octave.")
    return hd, [list(r) for r in _T272_ROWS], cap


def _t273(lang):
    if lang == "vi":
        hd = ("Điểm đo", "x/r", "y/r", "z/r")
        cap = ("Bảng 27.3 · Toạ độ các điểm đo trên mặt bán cầu bán kính r (theo ISO 3745). Điểm 10 "
               "nằm ngay trên đỉnh; các điểm 1–9 phân bố ở ba cao độ z/r = 0.15, 0.45 và 0.75.")
    else:
        hd = ("Measurement point no.", "x/r", "y/r", "z/r")
        cap = ("Table 27.3 · Coordinates of the measurement points on a hemisphere of radius r "
               "(per ISO 3745). Point 10 sits at the pole; points 1–9 occupy three heights, "
               "z/r = 0.15, 0.45 and 0.75.")
    rows = [
        ["1", "−0.99", "0", "0.15"],
        ["2", "0.5", "−0.86", "0.15"],
        ["3", "0.5", "0.86", "0.15"],
        ["4", "−0.45", "0.77", "0.45"],
        ["5", "−0.45", "−0.77", "0.45"],
        ["6", "0.89", "0", "0.45"],
        ["7", "0.33", "0.57", "0.75"],
        ["8", "−0.66", "0", "0.75"],
        ["9", "0.33", "−0.57", "0.75"],
        ["10", "0", "0", "1.0"],
    ]
    return hd, rows, cap


def _t274(lang):
    if lang == "vi":
        hd = ("Thiết bị", "Loại hiện có", "Giá tham khảo", "Hãng sản xuất")
        cap = ("Bảng 27.4 · Thiết bị đo âm học thông dụng, giá tham khảo và hãng cung cấp (theo văn "
               "bản gốc 1999; giá chỉ mang tính thời điểm).")
        rows = [
            ["Micro đo", "½″ trường tự do<br>½″ áp suất<br>¼″ trường tự do<br>¼″ áp suất",
             "$750–$825", "GRAS Sound &amp; Vibration<br>ACO Pacific<br>B&amp;K<br>The Modal Shop<br>Larson Davies"],
            ["Tiền khuếch đại", "½″ và 0,25 in.", "$600–$850",
             "GRAS Sound &amp; Vibration<br>ACO Pacific<br>B&amp;K<br>The Modal Shop<br>Larson Davies"],
            ["Máy đo mức âm", "SLM kiểu 1 giản đơn", "$800–$2000", "Rion<br>CEL<br>B&amp;K"],
            ["Máy đo mức âm", "SLM cao cấp có phân tích tần số và lưu dữ liệu",
             "$2000–$10.000", "Rion<br>CEL<br>Larson Davies<br>B&amp;K"],
            ["Máy phân tích tần số", "Phân tích thời gian thực / FFT", "$5000–$50.000",
             "Hewlett Packard<br>Norsonic<br>Data Physics<br>01dB"],
            ["Holography âm học vùng gần", "Hệ hoàn chỉnh, thu 16–64 kênh và xử lý sau đo",
             "$100.000–$200.000", "LMS<br>B&amp;K"],
        ]
    else:
        hd = ("Instrumentation", "Types available", "Approx. price", "Manufacturers")
        cap = ("Table 27.4 · Common acoustic instrumentation, approximate prices and suppliers "
               "(from the 1999 source; prices are indicative only).")
        rows = [
            ["Meas. microphones", "½″ free field<br>½″ pressure<br>¼″ free field<br>¼″ pressure",
             "$750–$825", "GRAS Sound &amp; Vibration<br>ACO Pacific<br>B&amp;K<br>The Modal Shop<br>Larson Davies"],
            ["Preamplifiers", "½″ and 0.25 in.", "$600–$850",
             "GRAS Sound &amp; Vibration<br>ACO Pacific<br>B&amp;K<br>The Modal Shop<br>Larson Davies"],
            ["Sound level meters", "Simple type 1 SLM", "$800–$2000", "Rion<br>CEL<br>B&amp;K"],
            ["Sound level meters", "Advanced SLM with frequency analysis and data storage",
             "$2000–$10,000", "Rion<br>CEL<br>Larson Davies<br>B&amp;K"],
            ["Frequency analyzers", "Real-time frequency analyzers / FFT", "$5000–$50,000",
             "Hewlett Packard<br>Norsonic<br>Data Physics<br>01dB"],
            ["Near-field acoustical holography", "Complete system with 16–64 channel acquisition "
             "and postprocessing", "$100,000–$200,000", "LMS<br>B&amp;K"],
        ]
    return hd, rows, cap


def _t275(lang):
    if lang == "vi":
        hd = ("Công ty", "Địa chỉ · điện thoại")
        cap = ("Bảng 27.5 · Các hãng chế tạo thiết bị đo âm học. Brüel &amp; Kjær và Rion được văn bản "
               "gốc liệt kê mà không kèm địa chỉ.")
    else:
        hd = ("Company", "Address · telephone")
        cap = ("Table 27.5 · Companies that make acoustical measurement instruments. Brüel &amp; Kjær "
               "and Rion are listed in the source without a full address.")
    rows = [
        ["G.R.A.S. Sound &amp; Vibration", "Skelstedet 10B, 2950 Vedbaek, Denmark · +45 45 66 40 46"],
        ["Larson Davies Inc.", "1681 West 820 North, Provo, UT 84601 · (801) 375 0177"],
        ["Brüel &amp; Kjær", "—"],
        ["Spectris Technologies Inc.", "2364 Park Central Blvd., Decatur, GA 30035-3987 · (800) 332 2040"],
        ["Rion", "—"],
        ["Scantek, Inc.", "916 Gist Avenue, Silver Springs, MD 20910 · (301) 495 7738"],
        ["LMS International", "Interleuvenlaan 68, B-3001 Leuven, Belgium · +32 16 384 571"],
        ["ACO Pacific, Inc.", "2604 Read Avenue, Belmont, CA 94002 · (415) 595 8588"],
        ["Hewlett-Packard Co.", "P.O. Box 95052-8059, Santa Clara, CA 95052 · (206) 335 2000"],
        ["Norsonic AS", "P.O. Box 24, N-3420 Lierskogen, Norway · +47 32 85 20 80"],
        ["CEL Instruments", "1 Westchester Drive, Milford, NH 03055 · (800) 366 2966"],
        ["The Modal Shop Inc.", "1776 Mentor Avenue, Suite 170, Cincinnati, OH 45212-3521 · (513) 351 9919"],
        ["01dB", "111 rue du 1er Mars, F69100 Villeurbanne, France · +33 4 78 53 96 96"],
    ]
    return hd, rows, cap


# ================================================================ Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Âm thanh thường được định nghĩa là dao động của môi trường rắn, lỏng hoặc khí trong dải tần "
        "mà tai người nghe được, tức khoảng 20 Hz đến 20 kHz. Ở đây định nghĩa được thu hẹp thêm: chỉ "
        "xét dao động trong môi trường lỏng và khí. Khác với môi trường rắn, môi trường lỏng hoặc khí "
        "không truyền được lực cắt, nên sóng âm luôn là sóng dọc — các phần tử dao động theo đúng "
        "phương truyền sóng. Lan truyền sóng trong môi trường khí và lỏng được mô tả bằng ba đại "
        "lượng: áp suất <i>p</i>, vận tốc hạt <i>u</i> và mật độ ρ. Quan hệ giữa chúng được mô tả bởi "
        "phương trình sóng [1], và phương trình này có thể suy ra từ ba phương trình cơ bản: phương "
        "trình Euler (thực chất là định luật hai Newton áp dụng cho chất lưu), phương trình liên tục "
        "và phương trình trạng thái."))
    b.append(p(
        "Về nguyên tắc, phương trình sóng dùng được để mô tả và tính mọi trường âm trong mọi tình "
        "huống, nhưng trên thực tế việc tính toán thường là bất khả thi. Chỉ một số trường hợp đặc "
        "biệt mới cho nghiệm giải tích trực tiếp, và vì thế chúng được quan tâm riêng. Ba trường hợp "
        "hay gặp nhất trong âm học là <b>trường tự do</b>, <b>trường khuếch tán</b> (hay trường vang) "
        "và <b>khoang kín (closed coupler)</b>."))
    b.append(p(
        "Trường tự do về nguyên tắc là một không gian vô hạn, trống rỗng (ngoài môi trường và nguồn), "
        "không có phản xạ; sóng được bức xạ tự do theo mọi hướng. Trên thực tế trường tự do được tạo "
        "trong các phòng không vang (anechoic chamber), nơi mọi bức tường hấp thụ gần như 100 %. "
        "Trường khuếch tán có được trong phòng vang (reverberation room) với các bức tường phản xạ "
        "gần như 100 % và được làm lệch nhau để trường âm có sóng theo mọi hướng. Khoang kín là một "
        "buồng nhỏ, kích thước nhỏ hơn nhiều so với bước sóng. Một trường hợp riêng là ống sóng đứng: "
        "ống có đường kính nhỏ hơn bước sóng, một đầu đặt nguồn âm; với loa thích hợp, có thể coi sóng "
        "trong ống là một chiều, nhờ đó mô tả toán học đơn giản và trường âm tính được."))
    b.append(p(
        "Trên thực tế, đại lượng gần như duy nhất được đo trực tiếp trong âm học là áp suất âm; mọi "
        "đại lượng khác — công suất âm, vận tốc hạt, thời gian vang, hướng tính — đều được suy ra từ "
        "phép đo áp suất. Các phép đo này dùng micro đo trong môi trường khí và hydrophone trong môi "
        "trường lỏng. Micro đo đều thuộc loại condenser để bảo đảm độ chính xác, độ ổn định dài hạn và "
        "độ nhạy. Hydrophone thường là một phần tử áp điện phủ cao su bảo vệ."))
    b.append(p(
        "Dải tần truyền thống 20 Hz – 20 kHz được chọn vì đó là dải tai người nghe được. Ngoài dải này "
        "còn có hạ âm (dưới 20 Hz) và siêu âm (trên 20 kHz). Vì các phương trình cơ bản và nguyên lý "
        "đo là như nhau cho cả hạ âm và siêu âm, nhiều nguyên tắc trong dải 20 Hz – 20 kHz có thể mở "
        "rộng sang các dải đó."))

    # -------------------------------------------------------- 27.1
    b.append(h2("27.1 Phương trình sóng", "The Wave Equation"))
    b.append(p(
        "Sóng âm không lan truyền được trong chân không mà luôn gắn với một môi trường. Để đơn giản, "
        "giả sử môi trường là không khí, dù các phương trình dưới đây cũng đúng cho mọi môi trường khí "
        "và lỏng. Trong môi trường đó có thể đưa ra khái niệm <b>phần tử khí</b> (air particle): một "
        "thể tích khí nhỏ mà tại đó các tham số âm học như áp suất, mật độ… coi như không đổi. Mặt "
        "khác, thể tích này phải đủ lớn để chứa rất nhiều phân tử khí, sao cho nó được coi là môi "
        "trường liên tục chứ không phải một tập hợp phân tử. <b>Phương trình Euler</b> cho phần tử khí "
        "đó là:"))
    b.append(eq("−grad p = ρ₀ (∂v ⁄ ∂t)", "27.1"))
    b.append(p(
        "trong đó <i>p</i> là áp suất, ρ₀ là mật độ và <i>v</i> là vận tốc hạt. Phương trình này chính "
        "là định luật hai Newton (<i>F</i> = <i>ma</i>) áp dụng cho chất lưu: gradient áp suất đóng vai "
        "lực <i>F</i> tác dụng lên phần tử khí, mật độ đóng vai khối lượng <i>m</i>, và đạo hàm theo "
        "thời gian của vận tốc hạt ∂<i>v</i>/∂<i>t</i> đóng vai gia tốc."))
    b.append(p(
        "Phương trình thứ hai cần để suy ra phương trình sóng là <b>phương trình liên tục</b>. Nó chỉ "
        "đơn giản nói rằng nếu đưa thêm khí vào một thể tích nhỏ thì mật độ (hay khối lượng) sẽ tăng. "
        "Về mặt toán học:"))
    b.append(eq("div v = −(1 ⁄ ρ₀) ∂ρ ⁄ ∂t", "27.2"))
    b.append(p(
        "trong đó <i>c</i> là tốc độ âm. Tốc độ âm phụ thuộc thành phần không khí và nhiệt độ. Với "
        "không khí thường ở 0 °C, tốc độ là 314 m s⁻¹; ở 20 °C là 340 m s⁻¹."))
    b.append(p(
        "Phương trình thứ ba là <b>phương trình trạng thái</b>, liên hệ thay đổi áp suất với thay đổi "
        "mật độ — nếu nén một thể tích khí nhỏ thì mật độ tăng:"))
    b.append(eq("∂ρ ⁄ ∂t = (1 ⁄ c²) × ∂p ⁄ ∂t", "27.3"))
    b.append(p(
        "Giờ ta có ba phương trình cho ba ẩn: áp suất, vận tốc hạt và mật độ. Khử vận tốc hạt và mật "
        "độ, ta thu được một phương trình vi phân cho áp suất âm:"))
    b.append(eq("∇²p = (1 ⁄ c²) ∂²p ⁄ ∂t²", "27.4"))
    b.append(p(
        "Đây là <b>phương trình sóng</b> cho sóng âm trong môi trường khí và lỏng. Về nguyên tắc, với "
        "điều kiện biên thích hợp, nó cho phép tính áp suất âm tại bất kỳ điểm nào trong trường âm. "
        "Trên thực tế tuy vậy chỉ tìm được nghiệm trong vài trường hợp đơn giản."))

    # -------------------------------------------------------- 27.2
    b.append(h2("27.2 Sóng âm phẳng", "Plane Sound Waves"))
    b.append(p(
        "Trong không gian tự do, ở khoảng cách lớn so với nguồn, sóng âm xấp xỉ là sóng phẳng: phương "
        "trình sóng chỉ còn phụ thuộc một toạ độ. Nếu mặt sóng truyền theo phương <i>x</i>, nghiệm của "
        "phương trình sóng rút về:"))
    b.append(eq("p = A cos[(ωt − k)(x + φ₀)]", "27.5"))
    b.append(p("trong đó ω là tần số. Tương tự, vận tốc hạt trong trường tự do là:"))
    b.append(eq("v = (A ⁄ ρc) cos[(ωt − k)(x + φ₀)] = p ⁄ (ρc)", "27.6"))
    b.append(p(
        "Nghĩa là trong sóng phẳng, vận tốc hạt bằng áp suất chia cho hằng số ρc, và áp suất với vận "
        "tốc hạt cùng pha. Hằng số ρc là <b>trở kháng âm</b>; với không khí ở 20 °C, mật độ 1,29 kg m⁻³ "
        "và tốc độ âm 340 m s⁻¹ cho trở kháng âm 438,6 kg m⁻² s⁻¹."))
    b.append(p(
        "Sóng phẳng truyền năng lượng theo phương lan truyền. Công suất truyền qua một đơn vị diện "
        "tích là cường độ theo phương truyền (nhiều sách cũ nhầm lẫn dùng cụm “cường độ của âm” cho độ "
        "lớn của áp suất âm). Nói chung cường độ bằng tích của áp suất âm và vận tốc âm; do đó với sóng "
        "phẳng, cường độ <i>I</i> tính từ các phương trình 27.5 và 27.6:"))
    b.append(eq("I = v p = p² ⁄ (ρc)", "27.7"))
    b.append(p(
        "Như vậy với sóng phẳng, cường độ do sóng truyền đi tính được từ áp suất âm; và vì công suất "
        "âm là cường độ trên một đơn vị diện tích, công suất âm bằng cường độ nhân diện tích."))

    # -------------------------------------------------------- 27.3
    b.append(h2("27.3 Sóng cầu", "Spherical Waves"))
    b.append(p(
        "Một nghiệm đơn giản khác của phương trình sóng là bức xạ từ nguồn điểm vào không gian tự do. "
        "Nguồn điểm là một mặt cầu vô cùng nhỏ có bề mặt đập theo phương hướng tâm. Trên thực tế, với "
        "nguồn âm nhỏ (kích thước nguồn nhỏ so với bước sóng), nguồn điểm là xấp xỉ tốt cho nguồn vật "
        "lý thực, khiến nghiệm sóng cầu đặc biệt đáng quan tâm."))
    b.append(p(
        "Phương trình sóng 27.5 được chuyển sang toạ độ cầu <i>r</i>, θ, ψ. Vì nguồn điểm bức xạ đều "
        "theo mọi hướng, nghiệm chỉ phụ thuộc khoảng cách <i>r</i> từ tâm nguồn:"))
    b.append(eq("p = (P₀ ⁄ r) cos(ωt − kr)", "27.8"))
    b.append(p(
        "Có thể thấy áp suất âm tỉ lệ nghịch với khoảng cách tới nguồn. Vận tốc hạt tách thành thành "
        "phần vùng gần <i>v</i><sub>n</sub> và thành phần vùng xa <i>v</i><sub>f</sub>:"))
    b.append(eq("v<sub>f</sub> = (P₀ ⁄ ρc)(1 ⁄ r) cos(ωt − kr)", "27.9"))
    b.append(eq("v<sub>n</sub> = (P₀ ⁄ ωρr²) sin(ωt − kr)", "27.10"))
    b.append(p(
        "Thành phần vùng xa trong 27.9 cùng pha với áp suất trong 27.8, và vận tốc hạt tỉ lệ nghịch "
        "với khoảng cách <i>r</i>. Thành phần vùng gần tỉ lệ nghịch với bình phương khoảng cách nên "
        "tắt rất nhanh khi ra xa nguồn."))
    b.append(p(
        "Như với sóng phẳng, cường độ trong sóng cầu là tích của áp suất và vận tốc hạt. Với thành "
        "phần vùng gần:"))
    b.append(eq("I = v<sub>n</sub> p = (P₀ ⁄ ωρr²) sin(ωt − kr) · (P₀ ⁄ r) cos(ωt − kr) = 0", "27.11"))
    b.append(p(
        "Nghĩa là phần vùng gần của vận tốc hạt không đóng góp vào công suất bức xạ, vì vận tốc hạt "
        "lệch pha 90° so với áp suất. Thành phần vùng xa cho:"))
    b.append(eq("I = v<sub>f</sub> p = (P₀² ⁄ r²ρc) cos²(ωt − kr)", "27.12"))
    b.append(p("Cường độ giảm theo bình phương khoảng cách; kết hợp 27.8 và 27.12:"))
    b.append(eq("I = (P₀² ⁄ r²ρc) cos²(ωt − kr) = p² ⁄ (ρc)", "27.13"))
    b.append(p(
        "đồng nhất với 27.7 cho sóng phẳng. Vậy, như với sóng chạy phẳng, cường độ trong sóng cầu "
        "cũng tính được từ áp suất."))

    # -------------------------------------------------------- 27.4
    b.append(h2("27.4 Phép đo âm học", "Acoustic Measurements"))
    b.append(p(
        "Như thấy từ phương trình sóng, về nguyên tắc toàn bộ trường âm mô tả được chỉ từ các phép đo "
        "áp suất; nghĩa là mọi tham số âm học khác đều suy ra được từ đo áp suất, và trên thực tế áp "
        "suất thường là tham số duy nhất được đo. Đã có vài nỗ lực chế tạo đầu dò đo vận tốc hạt, dựa "
        "trên ví dụ truyền sóng siêu âm, nhưng đầu dò chiếm ưu thế tuyệt đối trong đo âm học vẫn là "
        "micro kiểu condenser, Hình 27.1. Chúng tỏ ra vượt trội về độ ổn định nhiệt, độ ổn định dài "
        "hạn và khả năng chịu va đập. Trong khi micro đo được thiết kế và chế tạo để bảo đảm phép đo "
        "chính xác, xác định rõ, thì rất nhiều loại micro khác phục vụ mục đích khác — ví dụ gắn trong "
        "điện thoại, nơi giá thành là yếu tố quyết định, hoặc thu phòng thu, nơi đánh giá chủ quan quan "
        "trọng hơn tính năng khách quan."))
    b.append(fig(1, F.fig(1), "vi"))

    b.append(h3("27.4.1 Micro condenser", "Condenser Microphones"))
    b.append(p(
        "Micro condenser gồm năm phần tử cơ bản: lưới bảo vệ, vỏ micro, màng, bản cực và cách điện; "
        "xem Hình 27.2. Màng và bản cực tạo thành hai bản song song của một tụ điện không khí. Tụ này "
        "được phân cực bằng điện tích từ nguồn áp ngoài (loại phân cực ngoài) hoặc bằng điện tích được "
        "bơm trực tiếp vào lớp vật liệu cách điện trên bản cực (loại phân cực sẵn). Khi áp suất âm "
        "trong trường dao động, khoảng cách giữa màng và bản cực thay đổi, kéo theo điện dung của tụ "
        "thay đổi. Vì điện tích trên tụ được giữ không đổi, thay đổi điện dung sinh ra điện áp ra trên "
        "cực ra của micro."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Tính năng âm học của micro do các kích thước vật lý quyết định: diện tích màng, khoảng cách "
        "màng–bản cực, độ cứng và khối lượng của màng treo, và thể tích bên trong vỏ micro. Các yếu tố "
        "này quyết định dải tần, độ nhạy và dải động của micro. Độ nhạy của micro là điện áp ra ứng với "
        "một kích thích áp suất cho trước; bản thân nó ít có ý nghĩa cho việc sử dụng micro, trừ mục "
        "đích hiệu chuẩn. Tuy nhiên, độ nhạy (cùng với trở kháng điện của cartridge) cũng quyết định "
        "mức áp suất âm thấp nhất mà micro đo được. Ví dụ, micro có độ nhạy 2,5 mV Pa⁻¹ đo được mức "
        "thấp nhất khoảng 40 dB (so với 20 µPa), trong khi micro có độ nhạy 50 mV Pa⁻¹ đo được xuống "
        "khoảng 15 dB (so với 20 µPa)."))
    b.append(p(
        "Kích thước micro là tham số đầu tiên quyết định độ nhạy: nói chung đường kính màng càng lớn "
        "thì micro càng nhạy. Tuy vậy, không thể tăng độ nhạy vô hạn bằng cách tăng kích thước. Điện "
        "áp phân cực giữa màng và bản cực hút màng và làm nó võng về phía bản cực; khi micro lớn lên, "
        "độ võng tăng và cuối cùng màng sẽ chạm bản cực. Để tránh điều đó có thể tăng khoảng cách "
        "màng–bản cực hoặc giảm điện áp phân cực, nhưng cả hai đều làm giảm độ nhạy. Do đó kích thước "
        "tối ưu của micro đo thực tế dùng tới 20 kHz rất gần ½″ (12,6 mm)."))
    b.append(p(
        "Ngược lại, khi giảm kích thước micro thì dải tần sử dụng được mở rộng; dải tần đạt được một "
        "phần do kích thước micro quyết định. Ở tần số cao, khi bước sóng nhỏ hơn nhiều so với đường "
        "kính màng, màng không còn ứng xử như một pit-tông cứng mà bị “vỡ” (hiện tượng không phá hủy): "
        "các phần khác nhau của màng dao động với biên độ và pha khác nhau, làm đáp tuyến tần số thay "
        "đổi. Để tránh điều này, tần số giới hạn trên được đặt sao cho độ nhạy micro giảm xuống trước "
        "khi màng bắt đầu vỡ. Với micro 0,5 in. điển hình, giới hạn trên nằm trong khoảng 20 kHz đến "
        "40 kHz tuỳ độ căng màng. Nếu màng được căng cứng hơn thì tần số cộng hưởng cao hơn, nhưng độ "
        "nhạy giảm vì độ võng màng ứng với một mức áp suất cho trước nhỏ đi."))
    b.append(p(
        "Đáp tuyến tần số của micro do độ căng màng, khối lượng màng và cản âm trong khe khí giữa "
        "màng và bản cực quyết định. Hệ này biểu diễn được bằng tương tự cơ học của một hệ khối–lò "
        "xo–cản đơn giản như Hình 27.3. Khối lượng trong tương tự là khối lượng màng, lò xo là độ "
        "căng màng: màng căng cứng hơn tương ứng lò xo cứng hơn. Phần tử cản trong tương tự là cản âm "
        "giữa màng và bản cực, điều chỉnh được bằng cách khoan lỗ trên bản cực — không khí dễ thoát "
        "khỏi khe hơn khi màng võng, do đó giảm cản."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Đáp tuyến tần số của mô hình cơ học đơn giản này được cho ở Hình 27.4, cùng ảnh hưởng của "
        "từng tham số. Ở tần số thấp (dưới tần số cộng hưởng), đáp tuyến do độ căng màng quyết định, "
        "và như trên, giảm độ căng thì độ nhạy tăng. Tần số cộng hưởng do độ căng và khối lượng màng "
        "quyết định: tăng độ căng thì tần số cộng hưởng tăng, tăng khối lượng thì tần số cộng hưởng "
        "giảm. Đáp tuyến quanh tần số cộng hưởng do cản âm quyết định: tăng cản thì đáp tuyến giảm."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Dù vật liệu và kỹ thuật lắp ráp đã thay đổi trong những năm gần đây, các kiểu micro cơ bản "
        "vẫn không đổi: micro trường tự do, micro áp suất và micro tới ngẫu nhiên. Chúng được chế tạo "
        "với đặc tính tần số khác nhau, ứng với các yêu cầu khác nhau."))
    b.append(p(
        "<b>Micro áp suất</b> dùng để đo đúng áp suất âm tồn tại trên màng. Ứng dụng điển hình là đo "
        "áp suất âm trong một khoang kín, hoặc như Hình 27.5, đo áp suất âm tại một biên. Trong trường "
        "hợp này micro là một phần của bức tường và đo áp suất ngay trên tường. Đáp tuyến tần số của "
        "micro này cần phẳng trên dải càng rộng càng tốt, có tính đến việc độ nhạy sẽ giảm khi mở rộng "
        "dải tần. Cản âm trong khe giữa màng và bản cực được chỉnh sao cho đáp tuyến phẳng tới và hơi "
        "vượt quá tần số cộng hưởng."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "<b>Micro trường tự do</b> được thiết kế để đo đúng áp suất âm như nó tồn tại <i>trước khi</i> "
        "đưa micro vào trường. Ở tần số cao, sự có mặt của chính micro trong trường làm áp suất thay "
        "đổi: nói chung áp suất quanh cartridge tăng lên do phản xạ và nhiễu xạ. Micro trường tự do "
        "được thiết kế để đặc tính tần số của nó bù lại mức tăng áp này, nhờ đó tín hiệu ra tỉ lệ với "
        "áp suất âm như nó tồn tại trước khi đưa micro vào trường. Micro trường tự do luôn phải hướng "
        "về phía nguồn (góc tới 0°), như Hình 27.6."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Trong tình huống đó, sự có mặt của màng micro trong trường gây tăng áp trước màng, xem Hình "
        "27.7(a), tuỳ bước sóng và đường kính micro. Với micro ½″ điển hình, mức tăng áp cực đại xảy "
        "ra ở 26,9 kHz, nơi bước sóng (λ = 342 m s⁻¹ / 26,9 kHz ≈ 12,7 mm ≈ 0,5 in.) trùng với đường "
        "kính micro. Micro sau đó được thiết kế sao cho độ nhạy giảm đúng bằng mức áp suất âm tăng "
        "trước màng, bằng cách tăng cản âm bên trong cartridge để có đáp tuyến như Hình 27.7(b). Kết "
        "quả là tín hiệu ra, Hình 27.7(c), tỉ lệ với áp suất âm như nó tồn tại trước khi đưa micro vào "
        "trường. Đường cong ở Hình 27.7(a) còn được gọi là “đường hiệu chỉnh trường tự do” của micro, "
        "vì phải cộng đường này vào đáp tuyến của cartridge để có đặc tính âm học của micro trong "
        "trường tự do."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p(
        "Micro trường tự do về nguyên tắc đòi hỏi phải hướng về nguồn và sóng âm truyền về cơ bản "
        "theo một hướng. Trong một số trường hợp — ví dụ đo trong phòng vang hay môi trường phản xạ "
        "mạnh — sóng không có hướng truyền xác định mà tới micro từ mọi hướng cùng lúc. Sóng tới từ "
        "phía trước gây tăng áp như mô tả với micro trường tự do, còn sóng tới từ phía sau bị giảm đi "
        "phần nào do hiệu ứng che của cartridge. Ảnh hưởng tổng hợp của các sóng tới từ nhiều hướng vì "
        "thế phụ thuộc phân bố sóng theo hướng. Với micro đo, một phân bố chuẩn đã được định nghĩa "
        "trên cơ sở thống kê, cho ra micro tới ngẫu nhiên được tiêu chuẩn hoá."))
    b.append(p(
        "Như đã nêu, micro đo có thể là loại phân cực ngoài hoặc loại phân cực sẵn. Loại phân cực "
        "ngoài ổn định và chính xác nhất, nên được ưu tiên cho đo chính xác. Loại phân cực sẵn được ưu "
        "tiên trong một số trường hợp vì không cần nguồn điện áp phân cực ngoài — điển hình khi micro "
        "dùng trên thiết bị cầm tay nhỏ như máy đo mức âm, nơi nguồn nuôi cho điện áp phân cực sẽ làm "
        "tăng quá mức giá thành, khối lượng và mức tiêu thụ pin. Tuy vậy cần nhận rõ rằng micro phân "
        "cực sẵn nói chung kém ổn định hơn nhiều trước thay đổi môi trường so với micro phân cực ngoài."))

    # -------------------------------------------------------- 27.5
    b.append(h2("27.5 Đo mức áp suất âm", "Sound Pressure Level Measurements"))
    b.append(p(
        "Tai người về cơ bản nghe áp suất âm, nhưng độ nhạy thay đổi theo tần số: nhạy nhất trong "
        "khoảng 1 kHz – 5 kHz và giảm ở tần số cao hơn cũng như thấp hơn. Điều này dẫn tới việc phát "
        "triển nhiều hàm cân tần số nhằm mô phỏng độ nhạy của tai. Đáp ứng của tai với tín hiệu biến "
        "thiên theo thời gian và với xung cũng dẫn tới các thiết bị có hàm cân thời gian xác định. "
        "Thiết bị đo kết quả là máy đo mức âm, như định nghĩa trong tiêu chuẩn quốc tế IEC 651, “Sound "
        "Level Meters” [2]. Tiêu chuẩn định nghĩa bốn cấp máy đo mức âm cho các độ chính xác khác nhau "
        "(Bảng 27.1). Kiểu 0 chính xác nhất, dành cho đo chính xác trong phòng thí nghiệm; kiểu 1 được "
        "dùng rộng rãi nhất cho đo thông dụng, xem Hình 27.8. Kiểu 2 dùng khi giá thành là yếu tố quan "
        "trọng; kiểu 3 hầu như không dùng trên thực tế vì dung sai quá rộng khiến kết quả không đáng "
        "tin cậy. Đầu ra của máy đo mức âm về nguyên tắc được coi là đại lượng xấp xỉ cho cảm giác mà "
        "tai người tiếp nhận."))
    b.append(table(*_t271("vi")))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Về chức năng, máy đo mức âm chia thành bốn phần: micro và tiền khuếch đại, bộ lọc cân tần số "
        "A, bộ tách sóng RMS và bộ chỉ thị (Hình 27.9). Micro phải bảo đảm đo đúng áp suất âm trong "
        "dải tần ứng với cấp của máy; tiêu chuẩn cũng đặt yêu cầu về hướng tính của micro. Đáp tuyến "
        "tần số của thiết bị, kể cả bộ lọc cân, được quy định cho sóng tới micro theo hướng chuẩn. Với "
        "sóng tới từ hướng khác, tiêu chuẩn cho phép dung sai rộng hơn ở tần số cao, có tính đến phản "
        "xạ và nhiễu xạ không tránh khỏi ở tần số cao."))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(p(
        "Tiền khuếch đại chuyển tín hiệu ra trở kháng cao của micro thành tín hiệu trở kháng thấp, "
        "nhưng bản thân nó không khuếch đại điện áp, thậm chí có thể có hệ số nhỏ hơn 1. Tín hiệu sau "
        "tiền khuếch đại đi qua bộ lọc cân A — một bộ lọc được tiêu chuẩn hoá, về nguyên tắc mô phỏng "
        "độ nhạy của tai người, nhờ đó kết quả đo tương quan với cảm nhận chủ quan của người nghe "
        "trung bình. Bộ lọc này, với đặc tuyến như Hình 27.10, làm suy giảm tần số thấp và cao và hơi "
        "nhấn vùng giữa 1 kHz – 5 kHz. Còn một số đường cân khác — B, C và D — có thể tương quan tốt "
        "hơn với cảm nhận chủ quan trong trường hợp đặc biệt, như mức rất cao hoặc rất thấp, hoặc "
        "tiếng ồn máy bay."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Tín hiệu sau bộ lọc cân A được đưa qua bộ tách sóng RMS hàm mũ với hằng số thời gian 125 ms "
        "(“fast”) hoặc 1 s (“slow”). Các hằng số này mô phỏng ứng xử của tai khi chịu tín hiệu biến "
        "thiên theo thời gian. Đặc biệt khi kích thích âm tới tai ngắn đi (khoảng 200 ms), âm được "
        "đánh giá chủ quan là nhỏ hơn so với cùng âm đó nghe liên tục; hiệu ứng tương tự có được khi "
        "dùng thời gian lấy trung bình “fast”. Tuy vậy cách này cho độ bất định thống kê của ước lượng "
        "mức cao hơn so với dùng hằng số “slow”, nên “slow” nên được chọn khi tín hiệu âm liên tục. "
        "Các tiêu chuẩn khác mô tả những loại máy đo mức âm đặc biệt như máy đo tích phân hay máy đo "
        "mức âm xung, dành cho mục đích riêng."))

    # -------------------------------------------------------- 27.6
    b.append(h2("27.6 Máy phân tích tần số", "Frequency Analyzers"))
    b.append(p(
        "Máy đo mức âm cho một con số duy nhất cho mức âm trong dải 20 Hz – 20 kHz, nhưng thường người "
        "ta cần thông tin chi tiết hơn về thành phần tần số của tín hiệu. Hai loại máy phân tích tần số "
        "hay dùng trong đo âm học là máy phân tích FFT và máy phân tích bộ lọc thời gian thực. Máy FFT "
        "với độ phân giải tần số rất cao cho rất nhiều thông tin và cho phép tách các hài ở gần nhau "
        "(ví dụ từ một hộp số). Ngược lại, máy phân tích bộ lọc thời gian thực, Hình 27.11, dùng độ "
        "phân giải thô hơn nhiều, thường theo dải 1/3 octave. Việc phân tích được thực hiện bằng một "
        "tập bộ lọc (ngày nay phần lớn là bộ lọc số) có đáp tuyến tần số và thời gian xác định. Đáp "
        "tuyến bộ lọc đã được tiêu chuẩn hoá quốc tế, với tần số tâm và dải thông như Bảng 27.2. Trong "
        "dải 20 Hz – 20 kHz, tập bộ lọc 1/3 octave gồm 31 bộ lọc, đo đồng thời trên tín hiệu vào. Phổ "
        "1/3 octave thu được gần với cảm nhận chủ quan của tai người."))
    b.append(table(*_t272("vi")))
    b.append(fig(11, F.fig(11), "vi"))

    # -------------------------------------------------------- 27.7
    b.append(h2("27.7 Các phép đo dựa trên áp suất", "Pressure-Based Measurements"))
    b.append(p(
        "Kết quả đo áp suất âm chịu ảnh hưởng của nhiều yếu tố: nguồn, điều kiện vận hành nguồn, môi "
        "trường xung quanh, vị trí đo… Tuỳ mục tiêu phép đo, các tham số này được kiểm soát theo cách "
        "khác nhau. Nếu mục tiêu là định lượng phơi nhiễm tiếng ồn tại tai người vận hành trong môi "
        "trường ồn, điều quan trọng là micro phải ở đúng vị trí tai người vận hành và môi trường phải "
        "đúng như môi trường vận hành bình thường. Ngược lại, nếu nhiệm vụ là mô tả nguồn âm như một "
        "máy phát ồn, điều quan trọng là giảm thiểu ảnh hưởng của môi trường lên kết quả đo."))
    b.append(p(
        "Nếu mục đích là mô tả đối tượng đo như một nguồn ồn, thông lệ là nêu công suất âm bức xạ của "
        "nguồn. Đây là tham số tổng thể định lượng toàn bộ bức xạ ồn từ nguồn và ở một mức nào đó độc "
        "lập với môi trường. Công suất âm đo được theo nhiều cách: trong trường tự do, trong phòng "
        "vang, bằng kỹ thuật thay thế, hoặc bằng kỹ thuật cường độ âm. Trường tự do là trường âm trong "
        "đó âm bức xạ tự do theo mọi hướng, không có tường chặn hay phản xạ; thường có được trong "
        "phòng bán không vang (semi-anechoic), nơi mọi tường và trần phủ vật liệu hấp thụ gần 100 %, "
        "chỉ sàn là vật liệu phản xạ. Khi đặt nguồn trong phòng bán không vang, sóng phát ra bức xạ tự "
        "do ra xa nguồn và ở vùng xa có thể coi là sóng phẳng hoặc sóng cầu. Do đó cường độ âm tính "
        "được từ đo áp suất theo phương trình 27.7."))
    b.append(p(
        "Vì nguồn âm thực hiếm khi bức xạ đều theo mọi hướng, người ta lấy trung bình nhiều phép đo "
        "quanh vật thử. Tiêu chuẩn ISO 3745 “Acoustics — Determination of sound power levels of noise "
        "sources — Precision method for anechoic and semi-anechoic rooms” [3] quy định một mảng vị trí "
        "micro trên mặt bán cầu bao quanh vật thử, như Hình 27.12, với toạ độ như Bảng 27.3. Vì mọi "
        "điểm ứng với cùng một diện tích, và công suất âm bằng cường độ nhân diện tích, tổng công suất "
        "âm bức xạ tính được là:"))
    b.append(eq("P = A Σ I<sub>n</sub> = (2πr ⁄ ρc) Σ p<sub>n</sub>²", "27.14"))
    b.append(p(
        "trong đó <i>A</i> là diện tích mặt bán cầu thử có bán kính <i>r</i>, và <i>p</i><sub>n</sub> "
        "là áp suất đo tại điểm thứ <i>n</i>."))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(table(*_t273("vi")))

    # -------------------------------------------------------- 27.8
    b.append(h2("27.8 Đo cường độ âm", "Sound Intensity Measurements"))
    b.append(p(
        "Cách tính công suất âm từ đo áp suất trong 27.14 dựa trên phương trình 27.7. Tuy vậy phương "
        "trình này — cho cường độ từ một phép đo áp suất — chỉ đúng trong trường tự do, theo phương "
        "lan truyền. Nói chung, khi có tiếng ồn nền hoặc có phản xạ từ tường…, không thể tính cường độ "
        "âm từ một phép đo áp suất đơn lẻ. Trong những trường hợp đó vẫn có thể đo trực tiếp cường độ "
        "âm bằng đầu dò cường độ hai micro, Hình 27.13."))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(p("Cường độ âm <i>I</i> là tích của áp suất và vận tốc hạt:"))
    b.append(eq("I = p v", "27.15"))
    b.append(p(
        "Trong khi áp suất <i>p</i> là đại lượng vô hướng, không phụ thuộc hướng, thì vận tốc hạt là "
        "đại lượng vectơ, phụ thuộc hướng. Khi viết vận tốc hạt như trong 27.15, ngầm hiểu vận tốc "
        "theo một hướng xác định và cường độ thu được cũng tính theo hướng đó."))
    b.append(p(
        "Ví dụ, vận tốc hạt <i>v</i> theo phương lan truyền, Hình 27.14(a), cho cường độ bức xạ ra xa "
        "nguồn điểm, còn vận tốc hạt vuông góc với phương lan truyền, Hình 27.14(b), bằng không. Do đó "
        "cường độ tính theo 27.15 sẽ bằng không theo hướng vuông góc với phương lan truyền, dù áp suất "
        "âm như nhau. Nghĩa là năng lượng âm chảy ra xa theo hướng kính từ nguồn điểm và không có năng "
        "lượng chảy theo phương tiếp tuyến."))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p(
        "Đo cường độ âm theo 27.15 đòi hỏi đo cả áp suất âm và vận tốc hạt. Với đầu dò cường độ hai "
        "micro, áp suất tại vị trí giữa hai micro được tính là trung bình áp suất hai micro đo được:"))
    b.append(eq("p = (p₁ + p₂) ⁄ 2", "27.16"))
    b.append(p(
        "Vận tốc hạt khí <i>v</i> theo phương của đầu dò cường độ tính được từ chênh lệch áp suất giữa "
        "hai phép đo:"))
    b.append(eq("v = ∫ (p₂ − p₁) ⁄ (ρΔr) ∂τ", "27.17"))
    b.append(p(
        "trong đó ρ là mật độ không khí và Δ<i>r</i> là khoảng cách giữa hai micro. Cường độ <i>I</i> "
        "thu được bằng cách nhân áp suất với vận tốc:"))
    b.append(eq("I = p v = ((p₁ + p₂) ⁄ 2) ∫ (p₂ − p₁) ⁄ (ρΔr) ∂τ", "27.18"))
    b.append(p(
        "Kỹ thuật đo cường độ là công cụ mạnh để định vị nguồn ồn và xác định công suất âm bức xạ từ "
        "một nguồn, ngay cả khi có mặt các nguồn âm mạnh khác."))

    # -------------------------------------------------------- 27.9
    b.append(h2("27.9 Đo bằng holography âm học vùng gần", "Near-Field Acoustic Holography Measurements"))
    b.append(p(
        "Thuật ngữ <i>holography âm học</i> bắt nguồn từ tương tự với ảnh toàn ký quang học. Ai cũng "
        "biết holography, khác với ảnh thường, cho phép tái tạo đầy đủ hình ảnh của vật. Điều đó có "
        "được nhờ “ghi” cả biên độ lẫn pha của ánh sáng, trong khi ảnh thường chỉ “ghi” biên độ. Tương "
        "tự, với holography âm học, cả biên độ lẫn pha của trường âm được đo trên một mặt phẳng. Các "
        "phép đo này cho mô tả đầy đủ trường âm, trong đó biên độ và pha đều biết tại mọi điểm. Từ đó "
        "có thể tính các đại lượng âm học, gồm phân bố cường độ âm, vận tốc hạt, công suất âm, đồ thị "
        "bức xạ…"))
    b.append(p(
        "Giả thiết cơ bản của holography âm học vùng gần (NAH) là trường âm phân tích được thành hai "
        "kiểu sóng đơn giản: sóng phẳng và sóng tắt dần (evanescent). Sóng phẳng mô tả phần trường âm "
        "lan từ vùng gần ra vùng xa, còn sóng tắt dần mô tả trường âm phức tạp tồn tại trong vùng gần. "
        "Mọi trường âm đều mô tả được như tổ hợp của sóng phẳng và sóng tắt dần với biên độ và hướng "
        "khác nhau."))
    b.append(p(
        "Biên độ và hướng của từng sóng mô tả được bằng tần số không gian hay số sóng của nó. Với một "
        "sóng phẳng truyền theo một hướng, có thể mô tả bằng tần số thời gian cũng như tần số không "
        "gian. Tần số thời gian, Hình 27.15(a), có được khi xét biến thiên áp suất theo thời gian tại "
        "một điểm trong trường, cho tần số theo hertz hoặc radian trên giây. Tương tự, tần số không "
        "gian, Hình 27.15(b), có được khi xét biến thiên áp suất tại một thời điểm: ở thời điểm đó áp "
        "suất khác nhau ở các vị trí khác nhau. Nếu dịch chuyển theo một hướng trong không gian, ta "
        "thấy áp suất biến thiên tương ứng một tần số không gian, đo bằng chu kỳ trên mét hoặc radian "
        "trên mét. Nếu tần số thời gian cho biết áp suất biến thiên theo thời gian tại một điểm nhanh "
        "hay chậm, thì tần số không gian cho biết áp suất biến thiên theo vị trí tại một thời điểm. "
        "Trong ví dụ Hình 27.15(b), phương truyền của sóng phẳng trùng với trục đo tần số không gian."))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(p(
        "Trong trường hợp này, xem lại Hình 27.16(a), quan hệ giữa tần số không gian <i>k</i>₀ (tức số "
        "sóng) và tần số thời gian <i>f</i> do tốc độ âm <i>c</i> quyết định:"))
    b.append(eq("k₀ = 2π ⁄ λ = 2πf ⁄ c = ω ⁄ c", "27.19"))
    b.append(p(
        "trong đó λ là bước sóng. Tuy nhiên, nếu trục đo tần số không gian không trùng phương truyền, "
        "xem ví dụ Hình 27.16(b), quan hệ đơn giản đó không còn đúng: tần số thời gian vẫn như ở Hình "
        "27.16(a) nhưng tần số không gian thấp hơn. Với một tần số thời gian xác định, tần số không "
        "gian vì thế cho thông tin về phương truyền. Do đó, nếu trường âm gồm nhiều sóng phẳng cùng tần "
        "số thời gian nhưng khác phương truyền, điều này thể hiện trong phổ không gian thành nhiều "
        "thành phần tần số không gian."))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(p(
        "Ví dụ, nếu trường âm là tổng của hai sóng, Hình 27.17, trong đó một sóng truyền dọc trục đo "
        "và sóng kia lệch 45° so với sóng thứ nhất, phổ không gian sẽ chứa hai tần số không gian: một "
        "là <i>k</i> ứng với sóng dọc trục, và một là <i>k</i>·cos(45°) ứng với sóng xiên. Tới đây tần "
        "số không gian mới được định nghĩa dọc một trục, tương ứng biến đổi Fourier một chiều. Trong kỹ "
        "thuật NAH, trường âm được lấy mẫu không chỉ dọc một trục mà trên cả một mặt phẳng; do đó dùng "
        "biến đổi Fourier hai chiều, cho phổ tần số không gian hai chiều, nhưng thông tin vẫn như "
        "trước: hướng và biên độ của các kiểu sóng đơn giản."))
    b.append(fig(17, F.fig(17), "vi"))
    b.append(p(
        "Trường âm từ một nguồn điểm không giải thích được bằng sóng phẳng đơn giản như ở Hình 27.16 "
        "và 27.17, vì biên độ giảm theo khoảng cách từ gốc, trong khi sóng phẳng giữ nguyên biên độ "
        "trên toàn mặt. Vì vậy để mô tả hiện tượng vùng gần phải đưa vào sóng tắt dần. Trong phổ "
        "Fourier một chiều, sóng tắt dần nhận ra nhờ tần số không gian lớn hơn <i>k</i>₀ = 2π<i>f</i>/<i>c</i>. "
        "Tương tự, trong phổ tần số không gian hai chiều, sóng tắt dần có tần số không gian hay số "
        "sóng lớn hơn <i>k</i>₀."))
    b.append(p(
        "Từng tần số không gian trong phổ hai chiều ứng với một sóng phẳng hoặc sóng tắt dần đơn giản "
        "trên mặt quét (tức mặt đo). Với mỗi kiểu sóng, dễ dàng tính áp suất trên mặt khác, xem Hình "
        "27.18. Với sóng phẳng chỉ cần dịch pha; với sóng tắt dần phải tính đến thay đổi biên độ, "
        "nhưng về nguyên tắc đây cũng chỉ là một hàm truyền đơn giản áp lên phổ tần số không gian hai "
        "chiều. Bằng cách đó, phổ tần số không gian hai chiều trên mặt mới tính được từ dữ liệu gốc "
        "bằng các phép toán hàm truyền đơn giản; sau đó biến đổi Fourier ngược (hai chiều) để có trường "
        "âm trên mặt mới."))
    b.append(fig(18, F.fig(18), "vi"))
    b.append(p(
        "Nguyên lý tổng thể của NAH được tóm gọn ở Hình 27.19. Trường âm được quét trên một mặt gần "
        "vật đo, cho một mảng phổ thời gian — mỗi vị trí quét một phổ. Xét từng tần số thời gian một, "
        "ta lấy thông tin từ mỗi phổ ứng với tần số đang quan tâm, tạo ra mảng mới chỉ chứa thông tin "
        "về một tần số thời gian. Sau đó áp biến đổi Fourier (hai chiều) lên mảng này để có phổ tần số "
        "không gian hai chiều, rồi biến đổi sang mặt mới bằng các phép toán hàm truyền đơn giản. Khi "
        "đã có phổ hai chiều trên mặt mới, dùng biến đổi Fourier ngược để thu phân bố áp suất mới trên "
        "mặt đó."))
    b.append(fig(19, F.fig(19), "vi"))
    b.append(p(
        "Về nguyên tắc, kỹ thuật NAH đòi hỏi biết mọi phổ chéo giữa mọi vị trí quét: tại mỗi vị trí "
        "phải xác định phổ chéo tới tất cả vị trí khác. Một phép quét đơn giản với <i>N</i> = 1000 vị "
        "trí sẽ cần ½<i>N</i>(<i>N</i> + 1) = 500.500 phổ chéo. Thay vì đo tất cả, hệ thống dùng một "
        "bộ đầu dò quy chiếu để giảm số phổ chéo cần đo. Số đầu dò quy chiếu cần thiết để mô tả đầy đủ "
        "trường âm mà không phải đo toàn bộ dữ liệu do độ phức tạp của trường âm quyết định. Một phép "
        "đo với, ví dụ, bốn đầu dò quy chiếu và 2540 vị trí quét sẽ giảm xuống còn 4<i>N</i> = 4000 "
        "phép đo phổ chéo."))

    # -------------------------------------------------------- 27.10
    b.append(h2("27.10 Hiệu chuẩn", "Calibration"))
    b.append(p(
        "Để có phép đo chính xác và đáng tin cậy, micro và các thiết bị kèm theo phải được hiệu chuẩn "
        "đúng. Hiệu chuẩn micro đo chia thành hai phần: hiệu chuẩn mức và hiệu chuẩn đáp tuyến tần số. "
        "Hiệu chuẩn mức xác lập tín hiệu ra của micro ứng với một tín hiệu vào âm học cho trước tại "
        "một tần số cho trước; đáp tuyến tần số cho tín hiệu ra tại các tần số khác so với tần số hiệu "
        "chuẩn mức. Hiệu chuẩn mức có thể thực hiện bằng nhiều phương pháp với độ chính xác khác nhau."))
    b.append(p(
        "Phương pháp chính xác nhất là hiệu chuẩn thuận nghịch (reciprocity). Phương pháp dựa trên "
        "việc micro condenser là đầu dò thuận nghịch: nó dùng được như micro (chuyển tín hiệu âm thành "
        "tín hiệu điện) và như loa (chuyển tín hiệu điện thành tín hiệu âm). Bằng cách đo quan hệ giữa "
        "ba micro thử được điều khiển vừa làm phát vừa làm thu, ta thu được hệ ba phương trình với ba "
        "độ nhạy micro là ẩn số; giải hệ này cho độ nhạy của cả ba micro. Hiệu chuẩn thuận nghịch rất "
        "chính xác nhưng khá phiền phức, đòi hỏi điều kiện môi trường được kiểm soát tốt, nên ít dùng "
        "trong thực tế."))
    b.append(p(
        "Phương pháp so sánh và phương pháp thay thế về bản chất giống nhau: đều dựa trên đo sai khác "
        "giữa micro thử và micro chuẩn đã biết độ nhạy. Micro chuẩn thường được hiệu chuẩn tại một "
        "phòng thí nghiệm âm học quốc gia được công nhận như NIST, NPL hay PTB, nhờ đó bảo đảm chuỗi "
        "liên kết hiệu chuẩn. Trong phương pháp thay thế, đầu ra âm của một nguồn được đo bằng micro "
        "chuẩn; sau đó thay micro chuẩn bằng micro thử và đo lại. Miễn là nguồn âm ổn định, độ nhạy "
        "của micro thử tính được. Phương pháp so sánh tương tự, chỉ khác là micro chuẩn và micro thử "
        "chịu cùng áp suất âm đồng thời, nên yêu cầu về độ ổn định của nguồn ít khắt khe hơn."))
    b.append(p(
        "Một phương pháp hay dùng để hiệu chuẩn micro là phương pháp pistonphone. Pistonphone, Hình "
        "27.20, là một nguồn âm rất ổn định, tạo mức áp suất âm xác định bên trong một khoang kín. Nó "
        "làm việc nhờ dịch chuyển thể tích, Hình 27.21, với vận tốc xác định, thường ở 250 Hz. Khi "
        "pit-tông đi vào và đi ra, thể tích khoang kín thay đổi và gây biến thiên áp suất. Mức áp suất "
        "thực tế trong pistonphone phụ thuộc thể tích khoang, dịch chuyển thể tích của các pit-tông, "
        "áp suất khí quyển và — ở mức độ ít hơn — các yếu tố khác như độ ẩm, tản nhiệt… Vì dựa trên "
        "một hệ cơ khí tương đối đơn giản, pistonphone rất đáng tin cậy và dễ dùng trong thực tế, với "
        "độ chính xác khoảng 0,1 dB. Pistonphone cũng thường được dùng làm nguồn âm ổn định cho hiệu "
        "chuẩn theo phương pháp so sánh hoặc thay thế."))
    b.append(fig(20, F.fig(20), "vi"))
    b.append(fig(21, F.fig(21), "vi"))
    b.append(p(
        "Bộ hiệu chuẩn áp suất âm (sound pressure calibrator) về cơ bản là một thiết bị hiệu chuẩn so "
        "sánh nhỏ, khép kín. Micro thử được đưa vào một thể tích kín nhỏ và một loa nhỏ phát tín hiệu "
        "đơn tần, thường ở 1 kHz. Mức ra của loa được điều khiển trong một hệ hồi tiếp nhờ tín hiệu từ "
        "micro chuẩn. Miễn là micro chuẩn và độ lợi hồi tiếp ổn định, mức âm tại micro thử được xác "
        "định và độ nhạy tính được. Bộ hiệu chuẩn mức âm thường không dùng để hiệu chuẩn micro chính "
        "xác mà để kiểm tra tại hiện trường tính toàn vẹn của cả hệ đo."))
    b.append(p(
        "Đáp tuyến tần số của micro thường được xác định bằng phương pháp bộ kích thích tĩnh điện "
        "(electrostatic actuator). Một lưới dẫn điện được đặt gần và song song với màng micro. Điện "
        "trường giữa bộ kích thích và màng được tạo bằng điện áp một chiều 800 V đặt lên bộ kích "
        "thích; tín hiệu thử xoay chiều 50–150 V được chồng lên, và lực tĩnh điện đẩy–kéo màng, tương "
        "đương áp suất âm 1–10 Pa. Quét tín hiệu thử qua dải tần quan tâm, ta ghi được đáp tuyến áp "
        "suất của micro thử. Kỹ thuật bộ kích thích tĩnh điện được dùng rộng rãi như một phương pháp "
        "thử tiện lợi và chính xác, cả trong sản xuất lẫn hiệu chuẩn cuối cho micro đo."))
    b.append(p("Thiết bị và hãng sản xuất hiện có được liệt kê ở Bảng 27.4 và 27.5."))
    b.append(table(*_t274("vi")))
    b.append(table(*_t275("vi")))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "1. E. Skudrzyk, <i>The Foundation of Acoustics</i>, New York: Springer-Verlag, 1971.",
        "2. International Electrotechnical Commission, Publication 651: <i>Sound Level Meters</i>, "
        "Genève, Switzerland, IEC, 1971.",
        "3. International Organization for Standardization, Standard 3745 “Acoustics — Determination "
        "of sound power levels of noise sources — Precision method for anechoic and semi-anechoic "
        "rooms”, Genève, Switzerland, ISO, 1981.",
    ]))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []
    b.append(p(
        "Sound is normally defined as vibration of a solid, liquid or gaseous medium in the frequency "
        "range of the human ear, i.e. between about 20 Hz and 20 kHz. Here the definition is further "
        "limited and only vibrations in liquid and gaseous media are considered. In contrast to solid "
        "media, a liquid or gaseous medium cannot transmit shear forces, so sound waves are always "
        "longitudinal waves, in which the particles move in the direction of propagation of the wave. "
        "Wave propagation in gaseous and liquid media can be described by three variables: the pressure "
        "<i>p</i>, the particle velocity <i>u</i> and the density ρ. The relation between these is "
        "described by the wave equation [1], and this can be derived from three basic equations: the "
        "Euler equation (essentially Newton's second law applied to a fluid), the continuity equation "
        "and the state equation."))
    b.append(p(
        "Although the wave equation in principle can be used to describe and calculate all sound waves "
        "in all situations, in practice it will often be impossible to perform the necessary "
        "calculations. In some special cases it is possible to get analytical results directly from the "
        "wave equation, and these cases are therefore of special interest. The cases most often "
        "encountered in acoustics are the <b>free field</b>, the <b>diffuse</b> (or reverberant) "
        "<b>field</b>, and the <b>closed coupler</b>."))
    b.append(p(
        "The free field is, in principle, an infinite, empty (except for the medium and the source) "
        "space with no reflections, where waves radiate freely in all directions. In practice the free "
        "field is implemented in anechoic chambers, where all walls have been made nearly 100 % "
        "absorptive. The diffuse field is obtained in a reverberation room where all walls are in "
        "principle 100 % reflective; at the same time the walls are made non-parallel, and the result "
        "is a sound field with waves in all directions. The closed coupler is a small chamber with "
        "dimensions small compared to the wavelength. A special case is the standing wave tube — a tube "
        "of diameter smaller than the wavelength with a sound source in one end; with a suitable "
        "loudspeaker the propagation can be assumed one-dimensional, which simplifies the mathematics "
        "enough for the field to be calculated."))
    b.append(p(
        "In practice almost the only parameter measured directly in acoustics is the sound pressure, "
        "and all other parameters — sound power, particle velocity, reverberation time, directivity — "
        "are derived from pressure measurements. These are performed with measurement microphones in "
        "gaseous media and hydrophones in liquid media. Measurement microphones are all of the "
        "condenser type to ensure precision, long-term stability and sensitivity. Hydrophones are "
        "usually made with a rubber coating over a sensitive element of piezoelectric material."))
    b.append(p(
        "The traditional 20 Hz to 20 kHz range for acoustic measurements is selected because this is "
        "the range audible to the human ear. Sound waves exist outside this range as infrasound (below "
        "20 Hz) and ultrasound (above 20 kHz). As the basic equations and measurement principles are "
        "the same for both, many of the principles from the 20 Hz to 20 kHz range extend to these "
        "ranges."))

    # -------------------------------------------------------- 27.1
    b.append(h2("27.1 The Wave Equation", "Phương trình sóng"))
    b.append(p(
        "Sound wave propagation cannot take place in a vacuum but is always associated with some kind "
        "of medium. For simplicity, assume this medium is air, although the same equations are valid "
        "for all gaseous and fluid media. In this medium the concept of an <b>air particle</b> can be "
        "introduced: a small volume of air in which acoustical parameters such as pressure and density "
        "can be considered constant. On the other hand the volume must be large enough to include a "
        "very large number of molecules, so that it can be considered a continuous medium and not a "
        "collection of molecules. The <b>Euler equation</b> for such a particle is:"))
    b.append(eq("−grad p = ρ₀ (∂v ⁄ ∂t)", "27.1"))
    b.append(p(
        "where <i>p</i> is the pressure, ρ₀ the density and <i>v</i> the particle velocity. This can "
        "be considered as Newton's second law (<i>F</i> = <i>ma</i>) applied to a fluid: the gradient "
        "of the pressure equals the force <i>F</i> acting on the particle, the density equals the mass "
        "<i>m</i>, and the time-differentiated particle velocity ∂<i>v</i>/∂<i>t</i> equals the "
        "acceleration."))
    b.append(p(
        "The second equation needed is the <b>continuity equation</b>. It simply states that if you "
        "have a small volume of air and bring in some extra air, the density (or the mass) will "
        "increase. Mathematically:"))
    b.append(eq("div v = −(1 ⁄ ρ₀) ∂ρ ⁄ ∂t", "27.2"))
    b.append(p(
        "where <i>c</i> is the sound velocity, which depends on the composition of the air and the "
        "temperature. For normal air at 0 °C the velocity is 314 m s⁻¹, while at 20 °C it is 340 m s⁻¹."))
    b.append(p(
        "The third equation is the <b>state equation</b>, relating pressure changes to changes in "
        "density — if a small volume of air is compressed, the density increases:"))
    b.append(eq("∂ρ ⁄ ∂t = (1 ⁄ c²) × ∂p ⁄ ∂t", "27.3"))
    b.append(p(
        "Now three equations relate the three variables. Eliminating the particle velocity and the "
        "density gives one differential equation for the sound pressure:"))
    b.append(eq("∇²p = (1 ⁄ c²) ∂²p ⁄ ∂t²", "27.4"))
    b.append(p(
        "This is the <b>wave equation</b> for acoustic waves in gaseous and fluid media. In principle "
        "it allows the sound pressure anywhere in a sound field to be calculated, given suitable "
        "boundary conditions. In practice, however, solutions can only be found in a few simple cases."))

    # -------------------------------------------------------- 27.2
    b.append(h2("27.2 Plane Sound Waves", "Sóng âm phẳng"))
    b.append(p(
        "In free space, at great distance from the source, sound waves are approximately plane waves, "
        "so the wave equation depends on only one coordinate. If the wave fronts propagate in the "
        "<i>x</i>-direction, the solution reduces to:"))
    b.append(eq("p = A cos[(ωt − k)(x + φ₀)]", "27.5"))
    b.append(p("where ω is the frequency. Similarly the particle velocity in the free field is:"))
    b.append(eq("v = (A ⁄ ρc) cos[(ωt − k)(x + φ₀)] = p ⁄ (ρc)", "27.6"))
    b.append(p(
        "This means that in a plane wave the particle velocity equals the pressure divided by the "
        "constant ρc, and pressure and particle velocity are in phase. The constant ρc is the "
        "<b>acoustic impedance</b>; for air at 20 °C the density is 1.29 kg m⁻³ and the sound velocity "
        "340 m s⁻¹, giving an acoustic impedance of 438.6 kg m⁻² s⁻¹."))
    b.append(p(
        "The plane wave transmits energy in the direction of propagation. The power transmitted per "
        "unit area is the intensity in the direction of propagation (older textbooks mistakenly used "
        "“the intensity of the sound” for the magnitude of the sound pressure). In general the "
        "intensity is the product of sound pressure and sound velocity, so for the plane wave the "
        "intensity <i>I</i> follows from Equations 27.5 and 27.6:"))
    b.append(eq("I = v p = p² ⁄ (ρc)", "27.7"))
    b.append(p(
        "Thus in the plane wave the transmitted intensity can be calculated from the sound pressure, "
        "and since sound power is intensity per unit area, the sound power is the intensity multiplied "
        "by the area."))

    # -------------------------------------------------------- 27.3
    b.append(h2("27.3 Spherical Waves", "Sóng cầu"))
    b.append(p(
        "Another simple solution describes radiation from a point source into free space. The point "
        "source is an infinitely small sphere whose surface pulsates radially. In practice, for small "
        "sources (dimensions small compared to the wavelength) the point source is a good "
        "approximation to the real physical source, which makes the spherical solution of special "
        "interest."))
    b.append(p(
        "The wave equation is transformed into spherical coordinates <i>r</i>, θ, ψ. As the point "
        "source radiates equally in all directions, the solution depends only on the distance "
        "<i>r</i> from its centre:"))
    b.append(eq("p = (P₀ ⁄ r) cos(ωt − kr)", "27.8"))
    b.append(p(
        "The sound pressure is seen to be inversely proportional to the distance from the source. The "
        "particle velocity splits into a near-field contribution <i>v</i><sub>n</sub> and a far-field "
        "contribution <i>v</i><sub>f</sub>:"))
    b.append(eq("v<sub>f</sub> = (P₀ ⁄ ρc)(1 ⁄ r) cos(ωt − kr)", "27.9"))
    b.append(eq("v<sub>n</sub> = (P₀ ⁄ ωρr²) sin(ωt − kr)", "27.10"))
    b.append(p(
        "The far-field contribution in 27.9 is in phase with the pressure in 27.8, and the particle "
        "velocity is inversely proportional to the distance <i>r</i>. The near-field contribution is "
        "inversely proportional to the square of the distance and therefore dies away rapidly as the "
        "distance increases."))
    b.append(p(
        "As with the plane wave, the intensity in the spherical wave is the product of pressure and "
        "particle velocity. For the near-field contribution:"))
    b.append(eq("I = v<sub>n</sub> p = (P₀ ⁄ ωρr²) sin(ωt − kr) · (P₀ ⁄ r) cos(ωt − kr) = 0", "27.11"))
    b.append(p(
        "That is, the near-field part of the particle velocity does not contribute to the radiated "
        "power, since it is 90° out of phase with the pressure. The far-field contribution gives:"))
    b.append(eq("I = v<sub>f</sub> p = (P₀² ⁄ r²ρc) cos²(ωt − kr)", "27.12"))
    b.append(p("The intensity decreases with the square of the distance; combining 27.8 and 27.12:"))
    b.append(eq("I = (P₀² ⁄ r²ρc) cos²(ωt − kr) = p² ⁄ (ρc)", "27.13"))
    b.append(p(
        "identical to 27.7 for the plane wave. Thus, as for the plane progressive wave, the intensity "
        "in the spherical wave can be calculated from the pressure."))

    # -------------------------------------------------------- 27.4
    b.append(h2("27.4 Acoustic Measurements", "Phép đo âm học"))
    b.append(p(
        "As the wave equation shows, the full acoustic field can in principle be described from "
        "pressure measurements alone, so every other acoustic parameter can be derived from pressure, "
        "and in practice pressure is often the only parameter measured. There have been a few attempts "
        "to make transducers for particle velocity based on, for example, transmission of ultrasonic "
        "waves, but the absolutely dominating transducer for acoustic measurement is the condenser "
        "microphone, Figure 27.1. These have proved superior in temperature stability, long-term "
        "stability and insensitivity to rough handling. While measurement microphones are designed and "
        "produced to ensure well-defined, accurate measurements, a wide range of other microphones "
        "serve other purposes — for incorporation in telephones, where price is decisive, or for "
        "studio recording, where subjective evaluation matters more than objective performance."))
    b.append(fig(1, F.fig(1), "en"))

    b.append(h3("27.4.1 Condenser Microphones", "Micro condenser"))
    b.append(p(
        "The condenser microphone consists basically of five elements: protection grid, casing, "
        "diaphragm, backplate and insulator; see Figure 27.2. Diaphragm and backplate form the parallel "
        "plates of an air capacitor. This capacitor is polarized with a charge from an external voltage "
        "supply (externally polarized type) or by an electric charge injected directly into an "
        "insulating material on the backplate (prepolarized type). When the sound pressure in the "
        "field fluctuates, the distance between diaphragm and backplate changes and so does the "
        "capacitance. As the charge is kept constant, the change in capacitance generates an output "
        "voltage at the microphone terminal."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "The acoustical performance of a microphone is determined by its physical dimensions: diaphragm "
        "area, diaphragm-to-backplate spacing, the stiffness and mass of the suspended diaphragm, and "
        "the internal volume of the casing. These set the frequency range, the sensitivity and the "
        "dynamic range. The sensitivity is the output voltage for a given sound pressure excitation; in "
        "itself it is of little interest except for calibration purposes. However, the sensitivity "
        "(together with the electric impedance of the cartridge) also determines the lowest sound "
        "pressure level that can be measured. For example, a microphone with 2.5 mV Pa⁻¹ reaches about "
        "40 dB (re. 20 µPa), while one with 50 mV Pa⁻¹ reaches about 15 dB (re. 20 µPa)."))
    b.append(p(
        "Size is the first parameter determining sensitivity: in general the larger the diaphragm "
        "diameter, the more sensitive the microphone. There are, however, limits to how sensitive a "
        "microphone can be made by simply enlarging it. The polarization voltage between diaphragm and "
        "backplate attracts the diaphragm and deflects it toward the backplate; as the microphone grows, "
        "the deflection grows until the diaphragm touches the backplate. Increasing the spacing or "
        "decreasing the polarization voltage avoids this, but both reduce sensitivity. Hence the "
        "optimum size of a practical measurement microphone for use up to 20 kHz is very close to ½″ "
        "(12.6 mm)."))
    b.append(p(
        "Conversely, decreasing the size increases the useful frequency range, which is partly set by "
        "the size. At high frequencies, when the wavelength becomes much smaller than the diaphragm "
        "diameter, the diaphragm stops behaving like a rigid piston and “breaks up” (not a destructive "
        "phenomenon): different parts move with different magnitude and phase and the frequency "
        "response changes. To avoid this, the upper limiting frequency is placed so that the "
        "sensitivity drops off before breakup begins. For a typical 0.5 in. microphone this gives an "
        "upper limit between 20 kHz and 40 kHz depending on diaphragm tension. A stiffer diaphragm "
        "raises the resonance but reduces sensitivity, because the deflection for a given sound "
        "pressure level is smaller."))
    b.append(p(
        "The frequency response is determined by diaphragm tension, diaphragm mass and the acoustical "
        "damping in the airgap between diaphragm and backplate. The system is represented by the "
        "mechanical analogy of a mass–spring–damper system, Figure 27.3. The mass represents the "
        "diaphragm mass and the spring its tension, so a stiffer diaphragm is a stiffer spring. The "
        "damping element represents the acoustical damping between diaphragm and backplate, which can "
        "be adjusted by, for example, drilling holes in the backplate: air then escapes the airgap more "
        "easily when the diaphragm deflects, reducing damping."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "The frequency response of this simple mechanical model is given in Figure 27.4 together with "
        "the influence of the different parameters. At low frequencies (below resonance) the response "
        "is set by diaphragm tension, and as described, lowering the tension raises the sensitivity. "
        "The resonant frequency is set by tension and diaphragm mass: more tension, higher resonance; "
        "more mass, lower resonance. The response around resonance is set by the acoustical damping, "
        "where more damping lowers the response."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Although materials and assembly techniques have changed in recent years, the basic microphone "
        "types remain unchanged: free-field, pressure and random-incidence microphones, built with "
        "different frequency characteristics to match different requirements."))
    b.append(p(
        "The <b>pressure microphone</b> measures the actual sound pressure as it exists on the "
        "diaphragm. A typical application is measurement in a closed coupler or, as in Figure 27.5, at "
        "a boundary — the microphone forms part of the wall and measures the pressure on the wall "
        "itself. Its frequency response should be flat over as wide a range as possible, bearing in "
        "mind that sensitivity falls as the range is extended. The acoustical damping in the airgap is "
        "adjusted so that the response is flat up to and a little beyond the resonant frequency."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "The <b>free-field microphone</b> is designed to measure the sound pressure as it existed "
        "before the microphone was introduced into the field. At higher frequencies the presence of the "
        "microphone itself changes the pressure: in general the pressure around the cartridge increases "
        "because of reflections and diffraction. The free-field microphone is designed so that its "
        "frequency characteristics compensate for this increase, so the output is proportional to the "
        "pressure as it existed before insertion. It should always be pointed toward the source (0° "
        "incidence), as in Figure 27.6."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "In that situation the diaphragm in the field causes a pressure increase in front of it, "
        "Figure 27.7(a), depending on wavelength and microphone diameter. For a typical ½″ microphone "
        "the maximum increase occurs at 26.9 kHz, where the wavelength (λ = 342 m s⁻¹ / 26.9 kHz ≈ "
        "12.7 mm ≈ 0.5 in.) coincides with the diameter. The microphone is then designed so that its "
        "sensitivity decreases by the same amount as the pressure rises, by increasing the internal "
        "acoustical damping to obtain a response as in Figure 27.7(b). The result, Figure 27.7(c), is "
        "an output proportional to the pressure as it existed before insertion. The curve in Figure "
        "27.7(a) is also called the “free-field correction curve”, since it must be added to the "
        "cartridge response to obtain the free-field characteristic."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "In principle the free-field microphone must be pointed at the source and the waves must travel "
        "in essentially one direction. In some cases — measuring in a reverberation room or other "
        "highly reflecting surroundings — the waves have no well-defined direction but arrive from all "
        "directions at once. Waves from the front cause a pressure increase as described, while waves "
        "from the back are reduced to some extent by the shadowing effect of the cartridge. The combined "
        "influence therefore depends on the directional distribution of the sound. For measurement "
        "microphones a standard distribution has been defined on statistical grounds, resulting in the "
        "standardized random-incidence microphone."))
    b.append(p(
        "Measurement microphones can be externally polarized or prepolarized. Externally polarized "
        "types are by far the most stable and accurate and should be preferred for precision work. "
        "Prepolarized microphones are preferred in some cases because they need no external "
        "polarization source — typically on small hand-held devices such as sound level meters, where a "
        "polarization supply would add excessively to cost, weight and battery consumption. Still, "
        "prepolarized microphones are in general much less stable to environmental changes than "
        "externally polarized ones."))

    # -------------------------------------------------------- 27.5
    b.append(h2("27.5 Sound Pressure Level Measurements", "Đo mức áp suất âm"))
    b.append(p(
        "The human ear basically hears sound pressure, but its sensitivity varies with frequency: it is "
        "most sensitive between 1 kHz and 5 kHz and falls at higher and lower frequencies. This led to "
        "several frequency weighting functions that attempt to replicate the sensitivity of the ear. "
        "The ear's response to time-varying signals and impulses led to instruments with well-defined "
        "time weighting functions. The resulting instrument is the sound level meter, as defined for "
        "example by IEC International Standard 651, “Sound Level Meters” [2]. The standard defines four "
        "classes for different accuracies (Table 27.1). Type 0 is the most accurate, intended for "
        "precision laboratory measurements; Type 1 is most widely used for general-purpose "
        "measurements, see Figure 27.8. Type 2 is used where low price matters, while Type 3 is not "
        "used in practice because the wide tolerances make results too unreliable. The output of the "
        "sound level meter is in principle assumed to approximate the impression perceived by the "
        "human ear."))
    b.append(table(*_t271("en")))
    b.append(fig(8, F.fig(8), "en"))
    b.append(p(
        "Functionally the sound level meter divides into four parts: microphone and preamplifier, "
        "A-weighting filter, rms detector and display (Figure 27.9). The microphone must ensure correct "
        "measurement of the sound pressure within the frequency range of the given class; the standard "
        "also sets requirements on directivity. The frequency response of the instrument, including the "
        "weighting filter, is specified for waves arriving along the reference direction. For waves "
        "from other directions the standard allows wider tolerances at higher frequencies, "
        "acknowledging the inevitable reflections and diffraction there."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "The preamplifier converts the high-impedance microphone output to a low-impedance signal but "
        "has in itself no voltage gain, or even negative gain. The signal then passes through an "
        "A-weighting filter — a standardized filter that in principle resembles the sensitivity of the "
        "human ear, so that a measurement using it correlates with the subjective response of an "
        "average listener. The filter, with the characteristic of Figure 27.10, attenuates low and high "
        "frequencies and slightly amplifies the 1 kHz to 5 kHz region. Other weighting curves — B, C and "
        "D — may correlate better with subjective response in special cases, such as very high or very "
        "low levels, or aircraft noise."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "The signal then passes through an exponential rms detector with a time constant of either "
        "125 ms (“fast”) or 1 s (“slow”). These time constants simulate the behaviour of the ear under "
        "time-varying signals. Especially when the stimulus duration becomes short (around 200 ms), the "
        "sound is judged subjectively lower than the same sound heard continuously; the same effect is "
        "obtained with “fast” averaging. This, however, gives a higher statistical uncertainty on the "
        "level estimate than “slow”, so “slow” should be chosen for a continuous signal. Other "
        "standards describe special meters such as integrating or impulse sound level meters for "
        "special purposes."))

    # -------------------------------------------------------- 27.6
    b.append(h2("27.6 Frequency Analyzers", "Máy phân tích tần số"))
    b.append(p(
        "While the sound level meter gives a single reading for the 20 Hz to 20 kHz range, more "
        "detailed information about the frequency content is often wanted. Two types of analyser are "
        "common in acoustics: FFT analyzers and real-time filter analyzers. FFT analyzers, with very "
        "high frequency resolution, give a wealth of information and make it possible to separate "
        "closely spaced harmonics (e.g. from a gearbox). In contrast, real-time filter analyzers, "
        "Figure 27.11, use a much coarser resolution, usually 1/3-octave bands. The analysis is "
        "performed by a bank of filters (nowadays mostly digital) with well-defined frequency and time "
        "responses. Filter responses have been internationally standardized, with centre frequencies "
        "and passbands as in Table 27.2. Over 20 Hz to 20 kHz the 1/3-octave bank holds 31 filters "
        "measuring the input simultaneously. The resulting 1/3-octave spectrum resembles the subjective "
        "response of the human ear."))
    b.append(table(*_t272("en")))
    b.append(fig(11, F.fig(11), "en"))

    # -------------------------------------------------------- 27.7
    b.append(h2("27.7 Pressure-Based Measurements", "Các phép đo dựa trên áp suất"))
    b.append(p(
        "The result of sound pressure measurements is influenced by many factors: source, source "
        "operating conditions, surroundings, measurement position, and so on. Depending on the goal "
        "these can be controlled in different ways. If the goal is to quantify the noise exposure at an "
        "operator's ear in a noisy environment, the microphone must be where the operator's ear would "
        "normally be, and the environment must equal the normal operating environment. If instead the "
        "task is to describe the source as a noise-emitting machine, the influence of the environment "
        "must be minimized."))
    b.append(p(
        "If the aim is to describe the object as a noise source, it is customary to state the radiated "
        "sound power — a global parameter quantifying total noise radiation, to a certain extent "
        "independent of the environment. Sound power can be measured in several ways: in a free field, "
        "in a reverberation room, by a substitution technique, or by sound intensity. A free field is "
        "one in which sound radiates freely in all directions with no restricting walls or reflections; "
        "this is most often obtained in a semi-anechoic chamber, where all walls and the ceiling are "
        "covered with nearly 100 % absorptive material and only the floor is reflective. With the "
        "source in the chamber the waves radiate freely away, and in the far field they can be "
        "considered plane or spherical, so the intensity follows from pressure measurements via "
        "Equation 27.7."))
    b.append(p(
        "As real sources seldom radiate equally in all directions, a number of measurements around the "
        "object are averaged. ISO Standard 3745 “Acoustics — Determination of sound power levels of "
        "noise sources — Precision method for anechoic and semi-anechoic rooms” [3] specifies an array "
        "of microphone positions on a hemisphere over the object, as in Figure 27.12, with coordinates "
        "as in Table 27.3. As all points are associated with the same area, and sound power is "
        "intensity times area, the total radiated sound power is:"))
    b.append(eq("P = A Σ I<sub>n</sub> = (2πr ⁄ ρc) Σ p<sub>n</sub>²", "27.14"))
    b.append(p(
        "where <i>A</i> is the area of the test hemisphere of radius <i>r</i> and "
        "<i>p</i><sub>n</sub> the pressure measured at point <i>n</i>."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(table(*_t273("en")))

    # -------------------------------------------------------- 27.8
    b.append(h2("27.8 Sound Intensity Measurements", "Đo cường độ âm"))
    b.append(p(
        "The calculation of sound power from pressure measurements in 27.14 rests on Equation 27.7. "
        "That equation — intensity from a pressure measurement — is valid only in a free field, in the "
        "direction of propagation. In general, with background noise or reflections from walls, it is "
        "not possible to calculate the intensity from a single pressure measurement. In these cases the "
        "intensity can be measured directly with a two-microphone intensity probe, Figure 27.13."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(p("Sound intensity <i>I</i> is the product of pressure and particle velocity:"))
    b.append(eq("I = p v", "27.15"))
    b.append(p(
        "While pressure <i>p</i> is a scalar independent of direction, particle velocity is a vector "
        "quantity, directionally dependent. When the velocity is written as in 27.15 it is implicit "
        "that it refers to a certain direction and that the resulting intensity is calculated in the "
        "same direction."))
    b.append(p(
        "For example, the particle velocity along the propagation direction, Figure 27.14(a), gives "
        "intensity radiated away from the point source, while the velocity perpendicular to it, Figure "
        "27.14(b), is zero. The intensity from 27.15 is therefore zero in the direction perpendicular to "
        "propagation even though the pressure is the same. Sound energy flows radially away from the "
        "point source and none flows tangentially."))
    b.append(fig(14, F.fig(14), "en"))
    b.append(p(
        "Measuring intensity per 27.15 requires both pressure and particle velocity. With the "
        "two-microphone probe the pressure midway between the microphones is the mean of the two:"))
    b.append(eq("p = (p₁ + p₂) ⁄ 2", "27.16"))
    b.append(p(
        "The particle velocity <i>v</i> along the probe axis follows from the pressure difference "
        "between the two measurements:"))
    b.append(eq("v = ∫ (p₂ − p₁) ⁄ (ρΔr) ∂τ", "27.17"))
    b.append(p(
        "where ρ is the density of air and Δ<i>r</i> the spacing. The intensity is then the product of "
        "pressure and velocity:"))
    b.append(eq("I = p v = ((p₁ + p₂) ⁄ 2) ∫ (p₂ − p₁) ⁄ (ρΔr) ∂τ", "27.18"))
    b.append(p(
        "Intensity measurement is a powerful tool to localize noise sources and determine the sound "
        "power radiated by a source, even in the presence of other strong sources."))

    # -------------------------------------------------------- 27.9
    b.append(h2("27.9 Near-Field Acoustic Holography Measurements", "Đo bằng holography âm học vùng gần"))
    b.append(p(
        "The term <i>acoustic holography</i> comes from the analogy with optical holography. It is well "
        "known how holography, as opposed to a normal photograph, allows the full image of an object to "
        "be reconstructed: it “records” both the magnitude and the phase of the light, whereas a "
        "photograph records only magnitude. Similarly, in acoustic holography both magnitude and phase "
        "of the sound field are measured over a plane surface, giving a complete description in which "
        "both are known at all points. Acoustic quantities can then be calculated, including the "
        "intensity distribution, particle velocity, sound power and radiation pattern."))
    b.append(p(
        "The basic assumption behind near-field acoustic holography (NAH) is that the sound field "
        "decomposes into two simple wave types: plane waves and evanescent waves. Plane waves describe "
        "the part propagating away from the near field toward the far field, evanescent waves the "
        "complicated field existing in the near field. Any sound field can be described as a "
        "combination of plane and evanescent waves with different magnitudes and directions."))
    b.append(p(
        "Magnitude and direction of the individual waves are described by their spatial frequencies, "
        "or wavenumbers. For a simple plane wave propagating in a given direction this can be described "
        "by its temporal frequency as well as by its spatial frequency. The temporal frequency, Figure "
        "27.15(a), is obtained by looking at pressure changes with time at a point, giving hertz or "
        "radians per second. The spatial frequency, Figure 27.15(b), is obtained by looking at pressure "
        "changes at a given instant: at that instant the pressure differs from place to place, and "
        "moving in a given direction reveals a certain change corresponding to a spatial frequency, "
        "measured in cycles per metre or radians per metre. As temporal frequency tells how often "
        "pressure changes with time at a point, spatial frequency tells how often it changes with "
        "position at an instant. In the example of Figure 27.15(b) the propagation direction coincided "
        "with the axis along which spatial frequency was measured."))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p(
        "In this case, shown again in Figure 27.16(a), the relation between the spatial frequency "
        "<i>k</i>₀ (the wavenumber) and the temporal frequency <i>f</i> is given by the speed of sound:"))
    b.append(eq("k₀ = 2π ⁄ λ = 2πf ⁄ c = ω ⁄ c", "27.19"))
    b.append(p(
        "where λ is the wavelength. If the measurement axis is not the propagation direction, see "
        "Figure 27.16(b), this simple relation fails: the temporal frequency is as in 27.16(a) but the "
        "spatial frequency is lower. For one particular temporal frequency the spatial frequencies "
        "therefore carry information about propagation directions. Hence if the field is made up of "
        "several plane waves with the same temporal frequency but different directions, this appears in "
        "the spatial spectrum as several spatial frequency components."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "If, for example, the field is the sum of two waves, Figure 27.17, one travelling along the "
        "measurement axis and the other at 45° to it, the spatial spectrum contains two spatial "
        "frequencies: <i>k</i> for the axial wave and <i>k</i>·cos(45°) for the oblique one. So far "
        "spatial frequencies have been defined along a single axis, corresponding to a "
        "one-dimensional Fourier transform. In NAH the field is sampled over a plane, so a "
        "two-dimensional transform is used instead, giving a two-dimensional spatial frequency "
        "spectrum — but the information is the same: direction and magnitude of the simple wave types."))
    b.append(fig(17, F.fig(17), "en"))
    b.append(p(
        "The field of a point source cannot be explained by simple plane waves as in Figures 27.16 and "
        "27.17, since the amplitude decreases with distance from the origin while plane waves keep the "
        "same magnitude over the whole plane. To describe the near-field phenomenon one must introduce "
        "evanescent waves. In the one-dimensional spectrum they are identified as spatial frequencies "
        "above <i>k</i>₀ = 2π<i>f</i>/<i>c</i>; similarly in two dimensions, as wavenumbers above "
        "<i>k</i>₀."))
    b.append(p(
        "Each spatial frequency in the two-dimensional spectrum corresponds to a simple plane or "
        "evanescent wave in the scan plane. For each type it is easy to calculate the pressure in other "
        "planes, see Figure 27.18: for plane waves a simple phase shift suffices; for evanescent waves "
        "the amplitude change must be included, but this too is a simple transfer function applied to "
        "the spectrum. The spectrum in a new plane is thus obtained from the original data by simple "
        "transfer function operations, and an inverse two-dimensional Fourier transform then gives the "
        "sound field in that plane."))
    b.append(fig(18, F.fig(18), "en"))
    b.append(p(
        "The overall principle of NAH is summarized in Figure 27.19. The field is scanned in a plane "
        "close to the object, giving an array of temporal spectra, one per scan position. Taking one "
        "temporal frequency at a time, the information corresponding to that frequency is extracted "
        "from each spectrum, producing a new array holding only that frequency. A two-dimensional "
        "Fourier transform then yields the two-dimensional spatial frequency spectrum, which is "
        "transformed to new planes by simple transfer function operations. An inverse transform finally "
        "gives the pressure distribution in the new plane."))
    b.append(fig(19, F.fig(19), "en"))
    b.append(p(
        "In principle NAH requires all cross-spectra between all scan positions: at each position the "
        "cross-spectra to every other position must be determined. A simple scan with <i>N</i> = 1000 "
        "positions would need ½<i>N</i>(<i>N</i> + 1) = 500,500 cross-spectra. Instead of measuring "
        "them all, the system uses a set of reference transducers to reduce the number. How many "
        "references are needed for a complete description without the full data set is determined by "
        "the complexity of the field: a measurement with, for example, four references and 2540 scan "
        "positions reduces to 4<i>N</i> = 4000 cross-spectrum measurements."))

    # -------------------------------------------------------- 27.10
    b.append(h2("27.10 Calibration", "Hiệu chuẩn"))
    b.append(p(
        "To make accurate and reliable measurements the microphone and connected instruments must be "
        "properly calibrated. Microphone calibration divides into a level calibration and a frequency "
        "response calibration. The level calibration establishes the output for a given acoustic input "
        "at a given frequency; the frequency response gives the output at other frequencies relative to "
        "the calibration frequency. Level calibration can be performed by several methods of differing "
        "accuracy."))
    b.append(p(
        "The most accurate is the reciprocity method. It exploits the fact that a condenser microphone "
        "is a reciprocal transducer: it works as a microphone (acoustic to voltage) and as a loudspeaker "
        "(voltage to acoustic). By measuring the relationship among three test microphones driven as "
        "both transmitters and receivers, one obtains three equations whose unknowns are the three "
        "sensitivities; solving them gives all three. Reciprocity calibration is very accurate but "
        "tedious, needs well-controlled environmental conditions, and is therefore seldom used in "
        "practice."))
    b.append(p(
        "Comparison and substitution methods are essentially identical, both measuring the difference "
        "between the test microphone and a reference of known sensitivity. The reference is often "
        "calibrated at an accredited national acoustical laboratory such as NIST, NPL or PTB, which "
        "ensures traceability. In the substitution method the acoustic output of a source is measured "
        "with the reference; the reference is then replaced by the test microphone and the output "
        "measured again. Provided the source has been stable, the sensitivity of the test microphone "
        "follows. The comparison method is similar except that reference and test microphone are "
        "subjected to the same sound pressure simultaneously, so the stability requirement is less "
        "important."))
    b.append(p(
        "An often-used method is the pistonphone method. The pistonphone, Figure 27.20, is a very "
        "stable source producing a well-defined sound pressure level inside a closed coupler. It works "
        "by volume displacement, Figure 27.21, with a well-defined velocity, usually at 250 Hz: as the "
        "piston moves in and out the cavity volume changes and pressure varies. The actual level "
        "depends on coupler volume, piston volume displacement, barometric pressure and — to a lesser "
        "degree — humidity, heat dissipation and similar factors. Being based on a simple mechanical "
        "system, the pistonphone is very reliable and easy to use, with an accuracy around 0.1 dB. It "
        "also often serves as the stable source for comparison or substitution calibrations."))
    b.append(fig(20, F.fig(20), "en"))
    b.append(fig(21, F.fig(21), "en"))
    b.append(p(
        "A sound pressure calibrator is basically a small self-contained comparison calibration device. "
        "The test microphone is inserted into a small closed volume and a small loudspeaker produces a "
        "single frequency, usually 1 kHz. The loudspeaker output is controlled in a feedback loop using "
        "a signal from a reference microphone. Provided reference and feedback gain are stable, the "
        "level at the test microphone is well-defined and the sensitivity can be determined. Sound "
        "level calibrators are normally not used for accurate microphone calibration but for field "
        "checks of the integrity of a complete measurement system."))
    b.append(p(
        "The frequency response of a microphone is most often determined by the electrostatic actuator "
        "method. A conducting grid is placed close to and parallel with the diaphragm, and an electric "
        "field is established by applying 800 V dc to the actuator. A test signal of 50 to 150 V ac is "
        "superimposed, and the electrostatic forces push and pull the diaphragm, similar to a sound "
        "pressure of 1 to 10 Pa. Sweeping the test signal through the frequencies of interest records "
        "the pressure response. The technique is widely used as a convenient and accurate test method, "
        "both during production and in the final calibration of measurement microphones."))
    b.append(p("Available instrumentation and manufacturers are given in Tables 27.4 and 27.5."))
    b.append(table(*_t274("en")))
    b.append(table(*_t275("en")))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "1. E. Skudrzyk, <i>The Foundation of Acoustics</i>, New York: Springer-Verlag, 1971.",
        "2. International Electrotechnical Commission, Publication 651: <i>Sound Level Meters</i>, "
        "Genève, Switzerland, IEC, 1971.",
        "3. International Organization for Standardization, Standard 3745 “Acoustics — Determination "
        "of sound power levels of noise sources — Precision method for anechoic and semi-anechoic "
        "rooms”, Genève, Switzerland, ISO, 1981.",
    ]))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 27 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 27 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 27 “Đo âm học” của Per Rasmussen (G.R.A.S. Sound and Vibration) "
            "— phương trình sóng, sóng phẳng, sóng cầu, micro condenser, đo mức áp suất âm theo IEC "
            "651, máy phân tích tần số, xác định công suất âm, đo cường độ âm hai micro, holography "
            "âm học vùng gần và hiệu chuẩn, với 21 hình, 19 phương trình và 5 bảng." if vi
            else
            "Companion to Chapter 27 of the CRC Measurement Handbook — the wave equation, plane and "
            "spherical waves, condenser microphones, sound pressure level measurement per IEC 651, "
            "frequency analyzers, sound power determination, two-microphone sound intensity, "
            "near-field acoustic holography and calibration, with 21 figures, 19 equations and "
            "5 tables.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 27' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 27' % BASE_EN)
    meta = ("Chương 27 · theo Ch27.pdf (CRC Press, 1999) · 21 hình, 19 phương trình, 5 bảng" if vi else
            "Chapter 27 · 21 figures, 19 equations, 5 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 27)))
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
