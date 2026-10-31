# -*- coding: utf-8 -*-
"""Handbook Chapter 14 — Angle Measurement (Robert J. Sandberg, University of Wisconsin).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch14.py
"""
import os

import hb14fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch14-angle-measurement"
TITLE_EN = "Angle Measurement"
TITLE_VI = "Đo góc"
BYLINE = "Robert J. Sandberg · University of Wisconsin"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch13-volume-measurement"
PREV_VI = "ch13-volume-measurement"
PREV_T_EN = "Volume Measurement"
PREV_T_VI = "Đo thể tích"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-14-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Một <b>góc</b> được định nghĩa là hình được tạo bởi hai đường thẳng hoặc hai mặt phẳng cắt nhau. "
        "Các đường hay mặt phẳng đó có thể là thực — như các cạnh và bề mặt của một vật — hoặc được định "
        "nghĩa — như đường nối từ một người quan sát đến hai ngôi sao xa."))
    b.append(p(
        "Đơn vị đo góc là độ (<b>°</b>, 1° = 1/360 của một đường tròn) và radian (rad, 1 rad = 1/(2π) của "
        "một đường tròn). Một radian bằng 57,29578°, còn góc nhỏ có thể biểu diễn bằng milliradian "
        "(1·10⁻³ rad). Một độ lại được chia thành 60 <b>phút</b> (′), và 1 phút chia thành 60 <b>giây</b> "
        "(″). Một giây góc, dù rất nhỏ so với chi tiết gia công, lại rất có ý nghĩa ở quy mô lớn — ví dụ 1″ "
        "góc xấp xỉ 30 m trên một đại hoàn môn của Trái Đất, còn góc kẹp 1″ tương ứng khoảng 9 km trên bề "
        "mặt Mặt Trăng khi quan sát từ Trái Đất lúc gần nhất."))
    b.append(p(
        "Nhiều thuật ngữ được dùng để mô tả góc trong các lĩnh vực khác nhau. Bảng 14.1 liệt kê một số thuật "
        "ngữ cùng định nghĩa cơ bản. Nhiều thiết bị và dụng cụ dùng để đo hoặc cài đặt góc; các đoạn dưới "
        "mô tả sự đa dạng của trang thiết bị. Xem Bảng 14.2 để biết một phần các hãng sản xuất/cung cấp, và "
        "Bảng 14.3 để biết các mẫu cụ thể cùng giá xấp xỉ của dụng cụ đo góc."))
    b.append(h3("Bảng 14.1 · Các thuật ngữ định nghĩa liên quan đến góc", "Defining Terms Relating to Angles"))
    b.append('<dl class="glossary">'
             '<dt>Góc (Angle)</dt><dd>Hình được tạo bởi hai đường thẳng hoặc hai mặt phẳng cắt nhau.</dd>'
             '<dt>Góc nhọn (Acute angle)</dt><dd>Góc nhỏ hơn 90°.</dd>'
             '<dt>Phương vị (Azimuth)</dt><dd>Góc nằm ngang đo dọc theo đường chân trời Trái Đất, giữa một '
             'mốc tham chiếu cố định (thường là hướng Nam) và một vật.</dd>'
             '<dt>Độ nghiêng ngang (Bank)</dt><dd>Sự dốc theo hướng ngang (lateral inclination).</dd>'
             '<dt>Đường tròn (Circle)</dt><dd>Đường cong phẳng khép kín mà mọi điểm đều cách đều tâm.</dd>'
             '<dt>Độ dốc âm (Declination = declivity)</dt><dd>Một độ dốc âm.</dd>'
             '<dt>Độ (Degree)</dt><dd>Bằng 1/360 của một đường tròn.</dd>'
             '<dt>Goniometer</dt><dd>Dụng cụ đo góc (từ tiếng Hy Lạp <i>gonio</i>).</dd>'
             '<dt>Độ dốc (Incline = Slope = Bias = Slant = Gradient = Grade)</dt><dd>Độ lệch, dương hoặc âm, '
             'so với phương nằm ngang được trọng lực xác định.</dd>'
             '<dt>Vĩ độ (Latitude)</dt><dd>Góc đo theo hướng bắc hoặc nam từ xích đạo trên một kinh tuyến '
             'đến một điểm trên Trái Đất.</dd>'
             '<dt>Độ lệch dọc (Lean = List = Tilt)</dt><dd>Độ lệch khỏi phương thẳng đứng do trọng lực xác '
             'định.</dd>'
             '<dt>Kinh độ (Longitude)</dt><dd>Góc giữa kinh tuyến gốc (qua Greenwich, Anh) và kinh tuyến của '
             'một địa điểm trên Trái Đất; góc này dương khi dịch chuyển về phía tây.</dd>'
             '<dt>Milliradian</dt><dd>Góc bằng 1/1000 rad.</dd>'
             '<dt>Phút (Minute)</dt><dd>Góc bằng 1/60 độ.</dd>'
             '<dt>Góc xiên (Oblique angle)</dt><dd>Góc tù hoặc góc nhọn.</dd>'
             '<dt>Góc tù (Obtuse angle)</dt><dd>Góc lớn hơn 90°.</dd>'
             '<dt>Phần tư (Quadrant)</dt><dd>Một phần tư đường tròn (90°).</dd>'
             '<dt>Radian</dt><dd>Góc subtended bởi một cung tròn có độ dài bằng bán kính đường tròn đó; 1 '
             'radian = 57,29578°.</dd>'
             '<dt>Độ nghiêng cắt (Rake)</dt><dd>Độ lệch tính bằng độ so với phương vuông góc (90°) với một '
             'đường hay mặt phẳng.</dd>'
             '<dt>Vuông (Right angle)</dt><dd>Góc 90°.</dd>'
             '<dt>Độ dốc dương (Rise)</dt><dd>Một độ dốc dương.</dd>'
             '<dt>Giây (Second)</dt><dd>Góc bằng 1/60 phút (1/3600 độ).</dd>'
             '<dt>Thẳng (Straight)</dt><dd>Góc bằng 180°.</dd>'
             '<dt>Độ côn (Taper)</dt><dd>Sự thay đổi đường kính hoặc chiều dày trên một đơn vị chiều dài '
             'trục.</dd>'
             '<dt>Độ xoắn (Twist)</dt><dd>Góc xoay trên một đơn vị chiều dài trục, như trong nòng súng hay '
             'ren ốc.</dd>'
             '</dl>')

    # ---- 14.1
    b.append(h2("14.1 Thước cữ góc (Angle Gage Blocks)", "Angle Gage Blocks"))
    b.append(p(
        "Thước cữ góc có dạng tam giác vuông, làm bằng thép tôi cứng và mài phẳng, dày khoảng 7 mm và dài "
        "60 mm. Chúng được cung cấp thành bộ gồm các khối có góc nhọn lần lượt 1, 2, 3, 4, 5, 6, 7, 8, 9, "
        "10, 15, 20 hoặc 30°. Các khối này dùng kết hợp để cài đặt hay đo vật theo bước 1°. Một số bộ khác "
        "có các khối bước nhỏ đến 1″. Thước cữ góc đặc biệt có thể chế tạo ở bất kỳ góc nhọn nào với sự trợ "
        "giúp của thanh sine và thước cữ độ dày."))
    b.append(p(
        "Thước cữ góc cung cấp phương pháp bền, đơn giản và rẻ để đo và cài đặt góc — ví dụ định vị chi tiết "
        "trong ê tô hay đồ gá trước một nguyên công gia công như phay, khoan hay mài. Vì không điều chỉnh "
        "được và làm bằng thép tôi cứng, độ chính xác của chúng có thể đánh giá bằng cách quan sát trực "
        "tiếp tình trạng bề mặt: hãy tìm dấu hiệu mòn, sứt mẻ hay vết lõm trước khi dùng."))

    # ---- 14.2
    b.append(h2("14.2 Thước đo độ dốc (Clinometers)", "Clinometers"))
    b.append(p(
        "Clinometer là thiết bị điện tử đo góc thẳng đứng so với mức trọng lực. Nó có dạng hình chữ nhật, "
        "mỗi cạnh vuông góc 90° với cạnh kề. Với dải đọc ít nhất ±45°, hình dạng này cho phép đo đến "
        "trọn vẹn 360°. Điểm không nổi (floating zero) có thể đặt ở bất đâu, và đạt được độ phân giải đến "
        "±0,01°. Một số mẫu còn đổi sang đơn vị inch trên foot, % độ dốc, và mm trên mét (mm·m⁻¹)."))
    b.append(p(
        "Clinometer dùng được mọi nơi cần đo góc của một bề mặt so với trọng lực hay so với bề mặt khác. "
        "Độ chính xác và độ phân giải cao đạt được dễ dàng, nhưng nên định kỳ kiểm tra hiệu chuẩn so với "
        "một mặt phẳng biết trước và một góc biết trước. Các bề mặt xa nhau hay có vật cản giữa chúng "
        "không gây khó khăn cho clinometer."))

    # ---- 14.3
    b.append(h2("14.3 Máy soi quang học (Optical Comparator)", "Optical Comparator"))
    b.append(p(
        "Máy soi quang học đo góc, cùng các kích thước hay hình dạng khác, bằng cách đối chiếu ảnh (thường "
        "phóng đại) của vật với một lưới chuẩn (reticle) được chia theo đơn vị đo mong muốn. Máy cầm tay "
        "được đặt trực tiếp lên vật cần đo, và mắt người vận hành đưa lên khoảng cách thích hợp phía trên "
        "máy để ảnh phóng đại rõ nét. Một số mẫu có nguồn sáng chạy pin hay lưới điện. Lưới chuẩn của các "
        "thiết bị cầm tay thường chia theo bước 1°."))
    b.append(p(
        "Máy soi phóng chiếu (projection-type) có dạng để bàn hay đứng sàn, làm cho xem theo chùm ngang "
        "hoặc dọc. Chúng dùng nguồn sáng cường độ cao và hệ quang học phóng đại để hiển thị ảnh vật lên "
        "màn kính mờ phía sau có khắc cả vạch góc lẫn vạch tuyến tính. Ảnh hiển thị là kết quả của ánh "
        "sáng chiếu qua vật (gọi là shadow graph) hoặc phản xạ từ bề mặt vật; phương pháp dùng tuỳ thuộc "
        "hình dạng và chất lượng bề mặt vật. Độ phóng đại của hệ quang học dao động từ 10× đến 100×, với "
        "đường kính màn từ 0,3 m đến 1 m. Các máy này hữu ích để đo hình dạng mặt cắt của chi tiết sau khi "
        "gia công tinh, phục vụ kiểm soát chất lượng hay sao chép. Như tên gọi, ảnh phóng chiếu có thể chồng "
        "lên một mặt nạ hay bản vẽ đường bao đặt trực tiếp trên màn hình để dễ dàng xác định độ lệch so với "
        "hình dạng yêu cầu. Chúng là thiết bị nặng, không xách tay, đòi hỏi bảo trì khá cao và dùng tốt "
        "nhất trong phòng tối."))

    # ---- 14.4
    b.append(h2("14.4 Thước đo góc (Protractor)", "Protractor"))
    b.append(p(
        "Thước đo góc là dụng cụ dùng đo và vẽ góc. Thước đọc trực tiếp thường chia bước 1° và có dạng bán "
        "nguyệt hoặc hình tròn. Các mẫu đơn giản nhất làm liền khối bằng kim loại hay nhựa. Các mẫu khác "
        "có lưỡi hay kim chỉ xoay quanh tâm của vòng chia độ. Thước chính xác hơn được trang bị thước phụ "
        "(vernier) cho phép chỉ thị góc đến 5′ cung. Xem Hình 14.1 để biết cách đọc thước phụ đó."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Nguyên tắc đọc: nếu vạch 0 của du xích nằm bên phải vạch 0 của thước chính thì dùng cạnh phải của "
        "du xích; tìm vạch du xích trùng khớp nhất với một vạch thước chính, đếm số vạch từ 0 đến đó (mỗi "
        "vạch ứng 5′). Số độ chỉ bởi vạch thước chính ngay bên trái vạch 0 du xích; số phút cộng thêm bằng "
        "5 lần số vạch du xích đã đếm. (Trong ví dụ, vạch thứ tư trùng nhất, ứng 20′.)"))

    # ---- 14.5
    b.append(h2("14.5 Thanh sine (Sine Bar)", "Sine Bar"))
    b.append(p(
        "Thanh sine là dụng cụ dùng đo góc chính xác hoặc định vị chi tiết trước khi mài và các nguyên công "
        "gia công khác. Nó gồm một thanh thép tiện, tôi cứng và mài phẳng, gắn hai thanh trụ thép tôi cứng "
        "mài phẳng có cùng đường kính. Trục mỗi thanh trụ được đặt rất chính xác song song với thanh kia và "
        "với mặt trên của thanh."))
    b.append(p(
        "Thanh sine dùng kèm thước cữ chính xác đặt dưới một trong hai thanh trụ, nâng đầu đó lên một khoảng "
        "H (xem Hình 14.2) bằng sin của góc cần đo nhân khoảng cách D giữa hai thanh trụ. Khoảng cách chuẩn "
        "giữa hai thanh trụ là 250 mm (5 in.) hoặc 500 mm (10 in.). Phương trình chủ đạo khi dùng thanh "
        "sine là:"))
    b.append(eq("sin A = H / D"))
    b.append(fig(2, F.fig(2)))
    b.append(p(
        "Chi tiết được định vị bằng thanh sine thường được kẹp chặt nhờ một ê tô chính xác. Ê tô có thể "
        "kẹp trực tiếp vào chi tiết, hoặc — khi dùng thanh sine có lỗ ren trên mặt — kẹp vào cạnh thanh "
        "sine, còn chi tiết bắt bulông lên mặt thanh."))

    # ---- 14.6
    b.append(h2("14.6 Mâm sine (Sine Plate)", "Sine Plate"))
    b.append(p(
        "Một biến thể của thanh sine là mâm sine. Mâm sine gồm ba thành phần của thanh sine cộng thêm một "
        "tấm đáy và các dải hông dùng khoá tấm ở vị trí mong muốn. Thêm vào đó, một trong hai thanh trụ "
        "thép mài được bố trí làm bản lề giữa tấm trên và tấm dưới. Khi dùng mâm sine, chi tiết được khoá "
        "vào tấm trên bằng bulông hay kẹp, còn tấm dưới khoá vào bàn máy công cụ bằng kẹp hay bàn từ."))
    b.append(p(
        "Mâm sine kép (compound sine plate) là hai hướng, cho phép đo và cài đặt góc trong hai mặt phẳng "
        "vuông góc nhau (góc kép thực sự)."))

    # ---- 14.7
    b.append(h2("14.7 Đo độ côn (Taper)", "Taper"))
    b.append(p(
        "Một phương pháp chính xác để đo lỗ côn được mô tả trong Hình 14.3. Người ta dùng một cặp quả cầu "
        "thép có đường kính phù hợp với kích thước lỗ và góc côn. Phương pháp này cũng đo được góc giữa hai "
        "mặt phẳng kề nhau, dùng quả cầu hay chốt cỡ."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Chọn hai quả cầu (với lỗ) hoặc chốt cỡ (với rãnh) vừa khít với kích thước lỗ cần đo. Khoảng cách "
        "giữa hai quả cầu hay chốt càng lớn càng cho độ chính xác tốt. Vị trí các quả cầu xác định được và "
        "các hệ thức hình học trên hình được áp dụng để tính góc côn."))

    # ---- tables 14.2 / 14.3
    b.append(h2("14.8 Thiết bị, hãng sản xuất và giá", "Equipment, Manufacturers and Prices"))
    b.append(h3("Bảng 14.2 · Một phần các hãng sản xuất và cung cấp thiết bị đo góc", "Partial List of Manufacturers"))
    b.append(table(
        ["Hãng", "Địa chỉ"],
        [["Flexbar Machine Corporation (đại diện Erich Preissr & Co., Tây Đức)", "250 Gibbs Road, Islandia, NY 11722-2697 — Tel: (800) 879-7575"],
         ["Fred V. Fowler Co., Inc.", "66 Rowe Street, P.O. Box 299, Newton, MA 02166 — Tel: (617) 332-7004"],
         ["L. S. Starrett Company", "121 Crescent Street, Athol, MA 01331 — Tel: xem nhà phân phối địa phương"],
         ["Brown &amp; Sharpe Mfg. Co.", "931 Oakton Street, Elk Grove Village, IL 60007 — Tel: (312) 593-5950"],
         ["Swiss Precision Instruments, Inc. (SPI)", "2206 Lively Blvd., SPI Elk Grove Village, IL 60007 — Tel: (708) 981-1300"],
         ["Edmund Scientific Co.", "101 East Gloucester Pike, Barrington, NJ 08007-1380 — Tel: (609) 573-6250"]],
        "Bảng 14.2 · Một phần các hãng sản xuất và cung cấp thiết bị đo góc."))
    b.append(h3("Bảng 14.3 · Các dụng cụ đo hay chỉ thị góc", "Instruments and Devices Used to Measure or Indicate Angles"))
    b.append(table(
        ["Loại", "Hãng", "Model", "Mô tả", "Giá xấp xỉ"],
        [["Thanh sine", "Flexbar", "16292", "5 in. × 15/16 in. rộng", "$130.00"],
         ["Thanh sine", "Flexbar", "16293", "10 in. × 1 in. rộng", "—"],
         ["Thanh sine", "Flexbar", "16294", "5 in. × 2 in. rộng", "—"],
         ["Thanh sine", "Flexbar", "12202", "5 in. × 1 in. rộng, kinh tế", "$30.00"],
         ["Thanh sine", "Fowler", "52-455-010", "5 in. tâm–tâm, 15/16 in. rộng", "—"],
         ["Thanh sine", "Fowler", "52-455-015", "10 in. tâm–tâm, 1 in. rộng", "—"],
         ["Thanh sine", "Fowler", "52-455-030", "2,5 in. tâm–tâm, 1 in. rộng", "—"],
         ["Thanh sine", "SPI", "30-712-4", "10 in. tâm–tâm, trạm giữa vạn năng", "$3048.00"],
         ["Thanh sine", "SPI", "98-379-1", "5 in. tâm–tâm, 1 in. rộng, sai số giữa cuộn = 0,0003 in.", "$31.00"],
         ["Thanh sine", "SPI", "30-091-3", "10 in. tâm–tâm, 1 in. rộng, sai số giữa cuộn = 0,0001 in.", "$203.00"],
         ["Thanh sine", "Brown &amp; Sharpe", "598-291-121-1", "5 in. tâm–tâm, 1 in. rộng", "—"],
         ["Thanh sine", "Brown &amp; Sharpe", "598-293-121-1", "10 in. tâm–tâm, 1 1/8 in. rộng", "—"],
         ["Mâm sine", "Flexbar", "14612", "5 in. tâm–tâm, 6 × 3 × 2 in.", "$320.00"],
         ["Mâm sine", "Flexbar", "14615", "10 in. tâm–tâm, 12 × 6 × 2 5/8 in.", "$1000.00"],
         ["Mâm sine", "Fowler", "57-374-001", "5 in. tâm–tâm, 6 × 3 × 2 in.", "—"],
         ["Mâm sine", "Fowler", "57-374-004", "10 in. tâm–tâm, 12 × 6 × 2 5/8 in.", "—"],
         ["Mâm sine", "SPI", "77-026-3", "10 in. tâm–tâm, 12 × 6 × 2 5/8 in.", "$872.00"],
         ["Mâm sine", "Brown &amp; Sharpe", "599-925-10", "10 in. tâm–tâm, 12 × 6 × 2 3/8 in.", "—"],
         ["Mâm sine kép", "Flexbar", "14616", "5 in. tâm–tâm, 6 × 6 × 3 1/8 in.", "$1100.00"],
         ["Mâm sine kép", "Fowler", "57-375-001", "5 in. tâm–tâm, 6 × 6 × 3 1/8 in.", "—"],
         ["Mâm sine kép", "SPI", "7-072-7", "5 in. tâm–tâm, 6 × 6 × 3 1/8 in.", "$926.00"],
         ["Mâm sine kép", "Brown &amp; Sharpe", "599-926-5", "5 in. tâm–tâm, 6 × 6 × 3 1/2 in.", "—"],
         ["Máy tính góc", "Flexbar", "19860", "3 trục, kèm thước đo góc du xích", "$3750.00"],
         ["Thước đo góc trực tiếp", "Flexbar", "16337", "Đầu chữ nhật, 0–180°", "$25.00"],
         ["Thước đo góc trực tiếp", "Starrett", "RP1224W", "Chỉ đầu, lắp lưỡi 12/18/24 in.", "—"],
         ["Thước đo góc trực tiếp", "Starrett", "C183", "Đầu chữ nhật, 0–180°, lưỡi 6 in.", "—"],
         ["Thước đo góc trực tiếp", "SPI", "30-393-3", "Đầu chữ nhật, 0–180°", "$23.00"],
         ["Thước đo góc trực tiếp", "SPI", "31-804-8", "Chỉ đầu, lắp lưỡi 12/18/24 in.", "$39.00"],
         ["Thước đo góc du xích", "Flexbar", "16339", "360°, đọc 1′, có kính lúp, lưỡi 12 &amp; 6 in.", "$400.00"],
         ["Thước đo góc du xích", "Flexbar", "16338", "360°, đọc 5′", "$75.00"],
         ["Thước đo góc du xích", "Starrett", "C364DZ", "Lưỡi 12 in., 0–90° qua 360°, chia 5′", "—"],
         ["Thước đo góc du xích", "SPI", "30-395-8", "Lưỡi 6 in., 0–90° qua 360°, chia 5′", "$65.00"],
         ["Thước đo góc du xích", "SPI", "30-390-9", "Lưỡi 6 &amp; 12 in., 0–90° qua 360°, chia 1′, có lúp", "$540.00"],
         ["Thước đo góc du xích", "Brown &amp; Sharpe", "599-490-8", "Lưỡi 8 in., 0–90° qua 360°, lúp tuỳ chọn", "—"],
         ["Thước đo góc số (clinometer)", "Flexbar", "17557", "±45°, phân giải 0,1°", "$260.00"],
         ["Thước đo góc số (clinometer)", "Flexbar", "17556", "±60°, phân giải 0,01°, xuất SPC", "$450.00"],
         ["Thước đo góc số (clinometer)", "Fowler", "54-635-600", "±45°, phân giải 0,01°, có RS232", "—"],
         ["Thước đo góc số (clinometer)", "SPI", "31-040-9", "±45°, phân giải 0,01° (0 đến –10°) / 0,1° (10–90°)", "$329.00"],
         ["Thước đo góc mặt số nghiêng", "SPI", "30-150-7", "Lưỡi 8 in., mặt số Ø1 3/8 in., đọc đến 5′", "$527.30"],
         ["Thước đo góc mặt số nghiêng", "Brown &amp; Sharpe", "599-4977-8", "Lưỡi 8 in., đọc độ và 5′", "—"],
         ["Thước vuông tham chiếu", "SPI", "30-392-5", "Góc cố định 90°", "$55.00"],
         ["Máy soi quang học (phóng)", "Fowler", "53-912-000", "Màn Ø12 in., lens 10/20/25×, chùm ngang, đèn rọi mặt", "—"],
         ["Máy soi quang học (phóng)", "Starrett", "HB350", "Màn Ø14 in., lens 10/20/25/31,25/50×, chùm ngang", "—"],
         ["Máy soi quang học (phóng)", "Starrett", "VB300", "Màn Ø12 in., lens 10×–100×, chùm dọc", "—"],
         ["Máy soi quang học (phóng)", "Starrett", "HS1000", "Màn Ø40 in., lens 10×–100×, chùm ngang", "—"],
         ["Máy soi quang học (phóng)", "SPI", "40-350-1", "Màn Ø14 in., lens 10/20/50×, chùm ngang", "$2995.00"],
         ["Máy soi quang học (cầm tay)", "SPI", "40-145-3", "Phóng đại 10×, túi áo", "$57.50"],
         ["Máy soi quang học (cầm tay)", "SPI", "40-140-6", "Phóng đại 7×, túi áo, có đèn", "$62.50"],
         ["Máy soi quang học (cầm tay)", "Edmund Scientific", "A2046", "Phóng đại 6×, túi áo, lưới 360° chia 1°", "$58.75"],
         ["Tấm góc (Angle Plate)", "Fowler", "52-456-000", "Bộ 2, thép dày 9/32 in., 30·60·90° &amp; 45·45·90°", "—"],
         ["Tấm góc (Angle Plate)", "SPI", "98-463", "Bộ 2, thép dày 5/16 in., 30·60·90° &amp; 45·45·90°", "$32.00"],
         ["Khối định vị góc", "SPI", "70-997-2", "0–60°, du xích 10′ (cài chi tiết trong ê tô)", "$122.00"],
         ["Thước cữ góc lá", "Fowler", "52-470-180", "18 lá, thép lá, 1…10, 14, 14,5, 15, 20, 25, 30, 35, 45°", "—"],
         ["Thước cữ góc lá", "SPI", "31-375-9", "Bộ 18 lá, 5°–90° bước 5°, sai số 5′", "$49.60"],
         ["Thước cữ góc khối", "Starrett", "Ag18.TR", "Bộ 18 khối, ghép bước 1′, sai số 1′", "—"],
         ["Thước cữ góc khối", "Starrett", "AG16.LM", "Bộ 16 khối, ghép bước 1′, sai số 1/4′", "—"],
         ["Thước cữ góc khối", "SPI", "30-140-8", "Bộ 10 khối: 1,2,3,4,5,10,15,20,25,30°; sai số –0,0001′/in.", "$170.00"]],
        "Bảng 14.3 · Các dụng cụ đo hay chỉ thị góc (một phần), kèm model, mô tả và giá xấp xỉ."))

    # ---- further info
    b.append(h2("Thông tin thêm", "Further Information"))
    b.append(p(
        "Thông tin thêm về chủ đề này có trong các catalogue của hãng dưới dạng in và trực tuyến. Một tài "
        "liệu tham khảo khác là <i>Machinery's Handbook</i>, ấn bản 25, Industrial Press Inc., 200 Madison "
        "Avenue, New York, NY 10016-4078, 1996."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 13</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 14. The three figures of the "
        "source (14.1 vernier protractor, 14.2 sine bar, 14.3 two-ball taper measurement) are redrawn as "
        "vectors, and the large equipment tables (14.2, 14.3) are reproduced. The translation prose is not "
        "repeated here."))
    b.append(p(
        "An angle is the figure formed by two intersecting lines or planes. The units are degrees (1/360 of a "
        "circle) and radians (1/2π of a circle; 1 radian = 57.29578°). A degree splits into 60 minutes (′), "
        "and a minute into 60 seconds (″) — a second of arc is tiny for machined parts but ~30 m on a great "
        "circle of the Earth and ~9 km on the Moon seen from Earth. Table 14.1 lists the defining terms "
        "(acute/obtuse/right angle, azimuth, latitude, longitude, taper, twist, goniometer, and so on)."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Section 14.4 is the protractor. A direct-reading protractor is graduated in 1°; precise ones carry "
        "a vernier reading to 5′ of arc. Reading it (Figure 14.1): if the vernier zero is right of the main "
        "zero, use the right side of the vernier, find the vernier line best aligned with a main-scale line, "
        "count lines from zero (each = 5′), and add that to the degrees shown by the main-scale mark just "
        "left of the vernier zero. In the example the fourth line aligns, so add 20′."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Section 14.5 is the sine bar — a hardened, ground steel bar with two equal cylindrical rolls whose "
        "axes are parallel to each other and to the bar's top face. Gage blocks under one roll raise that end "
        "by H, and the governing relation is sin A = H/D (Figure 14.2), where D is the roll-center distance "
        "(250 mm / 5 in. or 500 mm / 10 in.). The workpiece is usually clamped in a precision vice. Section "
        "14.6 extends this to the sine plate (a bottom plate and side straps, one roll acting as a hinge); a "
        "compound sine plate sets true compound angles in two orthogonal planes. Section 14.7 measures a "
        "taper (Figure 14.3) with two balls (or gage pins) of known diameter: measure the depth to the top "
        "of each ball from a common reference, and with the known radii apply the geometry to recover the "
        "taper half-angle φ."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Section 14.1 (angle gage blocks) and 14.2 (clinometers) cover the simpler setting/measuring aids: "
        "right-triangle steel blocks in sets of 1°–30° (or 1″ steps) for durable, cheap angle setup, and "
        "electronic clinometers giving ±0.01° resolution against gravity over a ±45° (full 360°) range, with "
        "floating zero. Section 14.3 describes optical comparators — hand-held units with a calibrated "
        "reticle and projection models (10×–100× magnification, 0.3–1 m screens) that overlay a part's "
        "silhouette on a mask for quality control, best used in a darkened room."))
    b.append(p(
        "Tables 14.2 and 14.3 (below) list manufacturers and specific models with approximate prices — "
        "sine bars from about $30 to a $3,048 universal bench center, sine and compound plates from $320 to "
        "$1,100, protractors from $23 (direct) to $540 (vernier with magnifier), digital inclinometers "
        "around $260–$450, projection comparators near $3,000, and angle-gage sets from ~$50. These give the "
        "practical buying context for the techniques described."))
    b.append(table(
        ["Type", "Maker", "Model", "Description", "Price"],
        [["Sine bar", "Flexbar", "16292", "5 in. × 15/16 in. wide", "$130.00"],
         ["Sine bar", "SPI", "98-379-1", "5 in., accuracy between rolls 0.0003 in.", "$31.00"],
         ["Sine bar", "SPI", "30-091-3", "10 in., accuracy between rolls 0.0001 in.", "$203.00"],
         ["Sine bar", "SPI", "30-712-4", "10 in., universal bench center", "$3048.00"],
         ["Sine plate", "Flexbar", "14612", "5 in. C-C, 6×3×2 in.", "$320.00"],
         ["Sine plate", "SPI", "77-026-3", "10 in. C-C, 12×6×2 5/8 in.", "$872.00"],
         ["Compound sine plate", "Flexbar", "14616", "5 in. C-C, 6×6×3 1/8 in.", "$1100.00"],
         ["Angle computer", "Flexbar", "19860", "3-axis with vernier protractors", "$3750.00"],
         ["Protractor, direct", "Flexbar", "16337", "Rectangular head, 0–180°", "$25.00"],
         ["Protractor, vernier", "Flexbar", "16339", "360°, 1′ reading w/ magnifier", "$400.00"],
         ["Protractor, digital", "SPI", "31-040-9", "±45°, 0.01° (0 to −10°)", "$329.00"],
         ["Protractor, dial bevel", "SPI", "30-150-7", "8 in. blade, reads to 5′", "$527.30"],
         ["Optical comparator (proj.)", "SPI", "40-350-1", "14 in. screen, horizontal beam", "$2995.00"],
         ["Optical comparator (hand)", "SPI", "40-145-3", "10× pocket style", "$57.50"],
         ["Angle gage blocks", "SPI", "30-140-8", "10 blocks 1–30°, 0.0001′/in.", "$170.00"]],
        "Table 14.3 (condensed) · instruments and devices used to measure or indicate angles."))
    b.append(p(
        "Further reading: company catalogs (print and Web), and <i>Machinery's Handbook</i>, 25th ed., "
        "Industrial Press Inc., New York, 1996."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 13</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 14 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 14 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 14 “Đo góc” của Robert J. Sandberg — thước cữ góc, clinometer, "
            "máy soi quang học, thước đo góc, thanh/mâm sine (sin A = H/D), đo độ côn, kèm 3 hình và Bảng "
            "14.1–14.3." if vi else
            "Companion to Chapter 14 of the CRC Measurement Handbook — angle measurement by gage blocks, "
            "clinometers, optical comparators, protractors, sine bars/plates (sin A = H/D), and tapers, "
            "with all three figures and Tables 14.1–14.3.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 14' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 14' % BASE_EN)
    meta = ("Chương 14 · theo Ch14.pdf (CRC Press, 1999) · 3 hình, 3 bảng, phương trình sin A = H/D" if vi
            else "Chapter 14 · 3 figures, 3 tables, sine relation sin A = H/D")
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
