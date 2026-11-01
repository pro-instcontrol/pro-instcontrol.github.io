# -*- coding: utf-8 -*-
"""Handbook Chapter 21 — Density Measurement (Halit Eren, Curtin University of Technology).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch21.py
"""
import os

import hb21fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch21-density-measurement"
TITLE_EN = "Density Measurement"
TITLE_VI = "Đo khối lượng riêng"
BYLINE = "Halit Eren · Curtin University of Technology"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch20-mass-and-weight-measurement"
PREV_VI = "ch20-mass-and-weight-measurement"
PREV_T_EN = "Mass and Weight Measurement"
PREV_T_VI = "Đo khối lượng và trọng lượng"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-21-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


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


def wl(items):
    """Compact 'where ...' symbol list."""
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ol(items):
    """Numbered block used for the source's inline enumerations."""
    return ('<p style="font-size:.94rem;color:#333;line-height:1.85;margin:-.3rem 0 1.2rem">'
            + "<br>".join("%d. %s" % (i + 1, t) for i, t in enumerate(items)) + "</p>")


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
        "Khối lượng riêng là một phần quan trọng của đo lường và thiết bị đo. Các phép đo khối lượng "
        "riêng được thực hiện vì ít nhất hai lý do quan trọng: (1) để xác định khối lượng và thể tích "
        "của sản phẩm, và (2) để xác định chất lượng của sản phẩm. Trong nhiều ứng dụng công nghiệp, "
        "phép đo khối lượng riêng chính là yếu tố xác định giá trị của sản phẩm."))
    b.append(p(
        "Khối lượng riêng được định nghĩa là khối lượng của một thể tích xác định của một chất trong "
        "những điều kiện xác định. Tuy vậy, phải hết sức thận trọng khi đo, vì khối lượng riêng thay "
        "đổi theo áp suất và nhiệt độ. Mức thay đổi ở chất khí lớn hơn nhiều so với chất lỏng."))
    b.append(p(
        "Trong nhiều ứng dụng hiện đại, khối lượng riêng của sản phẩm được xác định bằng các kỹ thuật "
        "lấy mẫu. Trong đo lường có hai khái niệm cơ bản: đo khối lượng riêng tĩnh và đo khối lượng "
        "riêng động (trên đường ống). Trong mỗi khái niệm có nhiều phương pháp khác nhau, dựa trên những "
        "nguyên lý vật lý khác nhau. Trong nhiều trường hợp, chính ứng dụng và đặc tính của quá trình "
        "quyết định phương pháp phù hợp nhất. Nói chung, các phương pháp tĩnh đã được phát triển tốt, "
        "chi phí thấp hơn và chính xác hơn. Các bộ lấy mẫu động đắt tiền, được tự động hoá cao và dùng "
        "các thiết bị xử lý tín hiệu dựa trên vi xử lý. Tuy vậy, ngày nay nhiều phương pháp tĩnh cũng đã "
        "được vi tính hoá, mang lại các tính năng dễ dùng, linh hoạt và tự hiệu chuẩn."))
    b.append(p(
        "Không có một kỹ thuật đo khối lượng riêng nào dùng được một cách phổ quát. Phải dùng các phương "
        "pháp khác nhau cho các sản phẩm và vật liệu khác nhau. Trong nhiều trường hợp, khối lượng riêng "
        "được chuẩn hoá theo các điều kiện tham chiếu."))
    b.append(p(
        "Khối lượng riêng của một chất được xác định bằng cách chia khối lượng riêng của chất đó cho "
        "khối lượng riêng của một chất chuẩn thu được trong cùng điều kiện. Tỉ số không thứ nguyên này "
        "gọi là tỉ trọng (specific gravity — SG), còn được gọi là khối lượng riêng tương đối. Tỉ trọng "
        "của chất lỏng và chất khí ở điều kiện tham chiếu được cho bởi:"))
    b.append(eq("SG (lỏng) = (khối lượng riêng chất lỏng) / (khối lượng riêng của nước)", "21.1"))
    b.append(eq("SG (khí) = (khối lượng riêng chất khí) / (khối lượng riêng của không khí)", "21.2"))
    b.append(p(
        "Các bộ điều kiện thường được chấp nhận là nhiệt độ và áp suất thường (normal temperature and "
        "pressure — NTP) và nhiệt độ và áp suất tiêu chuẩn (standard temperature and pressure — STP). "
        "NTP thường được lấy là 0,00 °C và áp suất 760 mmHg; còn ở 15,00 °C hoặc 15,56 °C và 101,325 kPa "
        "người ta chấp nhận giá trị tương ứng với STP."))

    # ---- 21.1
    b.append(h2("21.1 Khối lượng riêng của chất rắn", "Solid Density"))
    b.append(p(
        "Nếu duy trì được tính đồng nhất thì việc xác định khối lượng riêng của chất rắn là một việc đơn "
        "giản. Khi đã biết thể tích của vật rắn và khối lượng của nó, có thể tìm khối lượng riêng bằng "
        "tỉ số cơ bản: khối lượng riêng = khối lượng/thể tích (kg m⁻³)."))
    b.append(p(
        "Tuy nhiên, trong nhiều ứng dụng, chất rắn có các thành phần khác nhau và được tạo nên từ những "
        "vật liệu khác nhau với các tỉ lệ khác nhau. Thể tích của chúng cũng thường xuyên thay đổi. "
        "Trong những trường hợp này, người ta dùng các phương pháp động, chẳng hạn loại hấp thụ phóng "
        "xạ, siêu âm và các kỹ thuật khác. Một số phương pháp này được mô tả dưới đây."))

    # ---- 21.2
    b.append(h2("21.2 Khối lượng riêng của chất lưu", "Fluid Density"))
    b.append(p(
        "Việc đo khối lượng riêng của chất lưu phức tạp hơn nhiều so với chất rắn. Với khối lượng riêng "
        "của chất lưu, có rất nhiều kỹ thuật khác nhau. Điều này chủ yếu do sự phức tạp của các quá "
        "trình, sự thay đổi khối lượng riêng của chất lưu trong quá trình, và những đặc tính đa dạng của "
        "quá trình cũng như của bản thân chất lưu. Một số phương pháp được thiết kế riêng và chỉ áp dụng "
        "cho những trường hợp đặc biệt. Số khác rất giống nhau về nguyên lý và công nghệ, và áp dụng "
        "được cho nhiều loại chất lưu khác nhau. Hiện nay, ngoài các phương pháp thông thường, còn có "
        "nhiều kỹ thuật mới lạ và đặc biệt đang được phát triển và nghiên cứu rộng rãi. Ví dụ, các tỉ "
        "trọng kế dựa trên nguyên lý điện từ [1] có thể được đưa vào như một phần của hệ thống thiết bị "
        "đo thông minh."))
    b.append(p(
        "Chất lưu có thể chia thành chất lỏng và chất khí. Trong phép đo khối lượng riêng của chất khí "
        "cần hết sức thận trọng và cần thêm những xem xét bổ sung. Ví dụ, khí lý tưởng chứa số phân tử "
        "bằng nhau trong cùng điều kiện và cùng thể tích; do đó có thể dùng khối lượng phân tử trong "
        "phép đo khối lượng riêng."))
    b.append(p(
        "Tùy theo ứng dụng, khối lượng riêng của chất lưu có thể được đo ở cả dạng tĩnh và dạng động. "
        "Nói chung, các phép đo khối lượng riêng tĩnh của chất lưu đã được phát triển tốt, chính xác và "
        "có độ phân giải cao hơn phần lớn các kỹ thuật động. Bình tỉ trọng và lực đẩy là những ví dụ về "
        "kỹ thuật tĩnh có thể được điều chỉnh để bao phủ những dải khối lượng riêng nhỏ với độ phân giải "
        "và độ chính xác cao. Ngày nay, nhiều nhà sản xuất cung cấp các thiết bị động mà trước đây vẫn "
        "được coi là tĩnh. Ngoài ra, nhiều thiết bị đo khối lượng riêng tĩnh đã được vi tính hoá và đi "
        "kèm phần cứng, phần mềm phù hợp. Nói chung, các phép đo kiểu tĩnh được dùng trong điều kiện "
        "phòng thí nghiệm, còn các phương pháp động được dùng cho những phép đo thời gian thực khi đặc "
        "tính của chất lưu thay đổi theo thời gian."))
    b.append(p(
        "Trong chương này, phần thảo luận tập trung vào những thiết bị đo khối lượng riêng hiện đại được "
        "ứng dụng phổ biến. Các thiết bị này gồm:"))
    b.append(ol([
        "Tỉ trọng kế dùng bình tỉ trọng (pycnometric densitometers)",
        "Tỉ trọng kế kiểu lực đẩy (buoyancy-type densitometers)",
        "Tỉ trọng kế thuỷ tinh (hydrometers)",
        "Tỉ trọng kế cân thuỷ tĩnh (hydrostatic weighing densitometers)",
        "Tỉ trọng kế kiểu cân (balance-type densitometers)",
        "Tỉ trọng kế kiểu cột (column-type densitometers)",
        "Tỉ trọng kế phần tử rung (vibrating element densitometers)",
        "Tỉ trọng kế phóng xạ (radioactive densitometers)",
        "Tỉ trọng kế khúc xạ và chiết suất (refractometer and index of refraction densitometers)",
        "Tỉ trọng kế Coriolis (Coriolis densitometers)",
        "Tỉ trọng kế kiểu hấp thụ (absorption-type densitometers)",
    ]))

    # ---- pycnometric
    b.append(h3("Tỉ trọng kế dùng bình tỉ trọng", "Pycnometric Densitometers"))
    b.append(p(
        "Bình tỉ trọng (pycnometer) là thiết bị tĩnh. Chúng được chế tạo dưới dạng bình có thể tích cố "
        "định, có thể đổ đầy chất lỏng mẫu. Khối lượng riêng của chất lưu được xác định bằng cách cân "
        "mẫu. Phiên bản đơn giản nhất gồm một bình có dạng chai với nút đậy dài chứa một lỗ mao quản, như "
        "trên Hình 21.1. Mao quản được dùng để xác định chính xác thể tích chất lỏng, nhờ đó đạt độ phân "
        "giải cao khi đổ đầy bình. Trước tiên cân bình rỗng, rồi cân bình đầy nước cất đã khử khí để xác "
        "định thể tích của bình. Sau đó đổ đầy chất lưu của quá trình vào bình và cân lại. Khối lượng "
        "riêng được xác định bằng cách chia khối lượng cho thể tích. Tỉ trọng của chất lỏng được tìm từ "
        "tỉ số giữa khối lượng chất lưu và khối lượng nước. Khi dùng bình tỉ trọng, để có độ chính xác "
        "tốt phải hết sức thận trọng trong khi đo: bình phải được làm sạch sau mỗi lần đo, nhiệt độ phải "
        "giữ không đổi, và phải dùng cân chính xác. Trong một số trường hợp, để bảo đảm đổ đầy bình tỉ "
        "trọng, người ta dùng hai ống mao quản. Hai mao quản bằng thuỷ tinh được bố trí sao cho chất lỏng "
        "có thể được đẩy vào bình dưới điều kiện chân không; sau đó việc đổ đầy tới đúng vạch chia trên "
        "mao quản được thực hiện chính xác."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Bình tỉ trọng phải nhẹ, đủ bền để chứa mẫu, và phải không nhiễm từ để việc cân được chính xác, "
        "loại trừ các ảnh hưởng từ trường của môi trường. Phải dùng những cân có độ phân giải rất cao để "
        "phát hiện những chênh lệch nhỏ về trọng lượng của chất khí và chất lỏng. Mặc dù nhiều bình tỉ "
        "trọng được làm bằng thuỷ tinh, chúng cũng được làm bằng kim loại để đủ bền cho các phép đo khối "
        "lượng riêng của chất khí và chất lỏng ở áp suất cực cao. Trong nhiều trường hợp, bình tỉ trọng "
        "kim loại là cần thiết để lấy mẫu trực tiếp từ đường ống của một số quá trình khắc nghiệt."))
    b.append(p("Bình tỉ trọng có cả ưu điểm và nhược điểm. Ưu điểm là nếu dùng đúng cách thì chúng chính "
               "xác, và có thể dùng cho cả phép đo khối lượng riêng lẫn tỉ trọng. Nhược điểm gồm:"))
    b.append(ol([
        "Phải hết sức thận trọng để có kết quả chính xác.",
        "Mẫu phải được lấy ra ngoài đường ống, kéo theo độ trễ về kết quả. Điều này gây khó khăn khi "
        "liên hệ mẫu với vật liệu thực sự tồn tại trong quá trình.",
        "Bình tỉ trọng có độ chính xác cao thì đắt tiền. Chúng đòi hỏi cân chính xác và điều kiện phòng "
        "thí nghiệm được kiểm soát. Phải dùng các kỹ thuật chuyên dụng để lấy mẫu trong các quá trình áp "
        "suất cao và trong điều kiện khắc nghiệt, chẳng hạn các công trình ngoài khơi.",
        "Hiệu năng tốt của chúng có thể phụ thuộc vào tay nghề của người vận hành.",
    ]))

    # ---- buoyancy
    b.append(h3("Tỉ trọng kế kiểu lực đẩy", "Buoyancy-Type Densitometers"))
    b.append(p(
        "Phương pháp lực đẩy về cơ bản dùng nguyên lý Ác-si-mét. Một quả chìm (sinker) có khối lượng và "
        "thể tích đã biết, được treo bằng một sợi dây mảnh, được nhúng hoàn toàn trong chất lỏng mẫu. Một "
        "cân lực chính xác được dùng để đo lực đỡ quả chìm. Khi đã biết khối lượng, thể tích và trọng "
        "lượng đỡ quả chìm, có thể tính được khối lượng riêng của chất lỏng. Tuy nhiên, cần hiệu chính "
        "một số yếu tố: sức căng bề mặt trên sợi dây treo, hệ số giãn nở khối của quả chìm, và nhiệt độ "
        "của quá trình. Tỉ trọng kế kiểu lực đẩy cho kết quả chính xác và được dùng để hiệu chuẩn các bộ "
        "chuyển đổi khối lượng riêng chất lỏng khác."))
    b.append(p(
        "Một phiên bản tiên tiến của kỹ thuật lực đẩy là hệ thống treo từ. Quả chìm được bao kín hoàn "
        "toàn trong một bình áp lực, nhờ đó loại bỏ được sai số do sức căng bề mặt. Công dụng của chúng "
        "cũng có thể mở rộng cho những ứng dụng như đo tỉ trọng ở áp suất hơi thấp và đo khối lượng riêng "
        "của các chất lưu nguy hiểm."))

    # ---- hydrometers
    b.append(h3("Tỉ trọng kế thuỷ tinh", "Hydrometers"))
    b.append(p(
        "Tỉ trọng kế thuỷ tinh (hydrometer) là thiết bị được dùng phổ biến nhất để đo khối lượng riêng "
        "của chất lỏng. Chúng được dùng phổ biến đến mức các thông số kỹ thuật và quy trình sử dụng được "
        "quy định trong các tiêu chuẩn quốc gia và quốc tế, chẳng hạn ISO 387. Nguyên lý lực đẩy là kỹ "
        "thuật hoạt động chính. Thể tích của một khối lượng cố định được chuyển thành một khoảng cách "
        "tuyến tính nhờ một ống thuỷ tinh kín hình bầu có thân dài mang thang chia, như trên Hình 21.2. "
        "Bầu được dằn bằng chì viên và nhựa thông, khối lượng của phần dằn phụ thuộc dải khối lượng "
        "riêng của chất lỏng cần đo. Chỉ cần thả bầu vào chất lỏng và đọc khối lượng riêng trên thang. "
        "Thang được chia theo đơn vị khối lượng riêng như kg m⁻³. Tuy nhiên, nhiều nhà sản xuất cung cấp "
        "các thang thay thế, chẳng hạn tỉ trọng, độ API, độ Brix, độ Brine… Tỉ trọng kế thuỷ tinh có thể "
        "được hiệu chuẩn cho các dải khác nhau về sức căng bề mặt và nhiệt độ. Có thể hiệu chính theo "
        "nhiệt độ về một nhiệt độ đặt trước như 15 °C, 20 °C hoặc 25 °C. ISO 387 bao phủ dải khối lượng "
        "riêng từ 600 kg m⁻³ đến 2000 kg m⁻³."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p("Tỉ trọng kế thuỷ tinh có một số ưu điểm và nhược điểm. Ưu điểm gồm:"))
    b.append(ol([
        "Chi phí tương đối thấp và dễ sử dụng",
        "Độ phân giải tốt trong một dải hẹp",
        "Có thể truy xuất tới các chuẩn quốc gia và quốc tế",
    ]))
    b.append(p("Nhược điểm gồm:"))
    b.append(ol([
        "Dải đo hẹp; do đó cần nhiều chiếc để bao phủ một dải đáng kể.",
        "Chúng làm bằng thuỷ tinh và dễ vỡ. Các phiên bản bằng kim loại và nhựa không chính xác bằng.",
        "Chất lưu phải là mẫu lấy ngoài đường ống, không đại diện cho đúng điều kiện của quá trình. Có "
        "loại tỉ trọng kế chịu áp cho hydrocarbon có áp suất hơi thấp, nhưng như vậy lại nảy sinh yêu cầu "
        "phải xác định chính xác cả áp suất.",
        "Nếu cần độ chính xác tốt thì chúng khó dùng, vì phải hiệu chính sức căng bề mặt và nhiệt độ. Với "
        "chất lưu đục có thể cần hiệu chính thêm.",
    ]))

    # ---- hydrostatic
    b.append(h3("Tỉ trọng kế cân thuỷ tĩnh", "Hydrostatic Weighing Densitometers"))
    b.append(p(
        "Thiết bị phổ biến nhất dùng phương pháp cân thuỷ tĩnh gồm một ống chữ U được đỡ trên các khớp "
        "nối mềm ở hai đầu. Một ví dụ điển hình được trình bày trên Hình 21.3. Tổng trọng lượng của ống "
        "thay đổi tùy theo khối lượng riêng của chất lưu chảy qua ống. Cần đo chính xác sự thay đổi trọng "
        "lượng này, và có nhiều phương pháp được dùng để làm việc đó. Các thiết bị thương mại phổ biến "
        "nhất dùng hệ thống cân lực. Các khớp nối là bellows bằng thép không gỉ. Trong một số trường hợp, "
        "cao su hoặc PTFE được dùng, tùy theo đặc tính của chất lưu quá trình và độ chính xác yêu cầu. "
        "Do bellows nên có các giới hạn về nhiệt độ và áp suất, và kết cấu của hệ thống có thể gây ra độ "
        "lệch số đọc. Thiết bị phải được gắn chắc trên một mặt phẳng nằm ngang để có độ chính xác tối ưu."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p("Ưu điểm của phương pháp này gồm:"))
    b.append(ol([
        "Cho số đọc liên tục và có thể hiệu chuẩn chính xác.",
        "Chắc chắn, có thể dùng cho chất lỏng hai pha như bùn, dung dịch đường, bột…",
    ]))
    b.append(p("Nhược điểm của các thiết bị này gồm:"))
    b.append(ol([
        "Phải lắp đặt nằm ngang trên một nền vững chắc. Các thiết bị này không đủ linh hoạt để thích ứng "
        "với mọi quá trình; do đó quá trình phải được thiết kế xoay quanh thiết bị.",
        "Chúng cồng kềnh và khó sử dụng.",
        "Chúng không phù hợp để đo khối lượng riêng của chất khí.",
    ]))

    # ---- balance type
    b.append(h3("Tỉ trọng kế kiểu cân", "Balance-Type Densitometers"))
    b.append(p(
        "Tỉ trọng kế kiểu cân phù hợp để đo khối lượng riêng của chất lỏng và chất khí. Các nhà sản xuất "
        "cung cấp nhiều loại khác nhau; bốn loại được dùng phổ biến nhất được thảo luận dưới đây."))

    b.append(h4("Bình dòng cân bằng", "Balanced-Flow Vessel"))
    b.append(p(
        "Một bình có thể tích cố định như trên Hình 21.4 được dùng cho các phép đo. Trong khi chất lỏng "
        "chảy liên tục qua bình, bình được cân tự động bằng một cân nhạy — hệ thống cân lò xo hoặc bộ "
        "truyền cân lực khí nén. Vì đã biết thể tích và trọng lượng của chất lỏng, khối lượng riêng hoặc "
        "tỉ trọng có thể được tính dễ dàng và chia thang theo đơn vị tương ứng. Trong quá trình thiết "
        "kế, phải hết sức chú ý tới các khớp nối mềm ở hai đầu."))
    b.append(fig(4, F.fig(4), "vi"))

    b.append(h4("Phao cân bằng xích", "Chain Balanced Float"))
    b.append(p(
        "Trong hệ thống này, một quả chìm tự định tâm, có thể tích cố định, chìm trong chất lỏng, được "
        "dùng để đo khối lượng riêng, như minh hoạ trên Hình 21.5. Quả chìm nằm hoàn toàn dưới mặt chất "
        "lỏng. Ở trạng thái cân bằng, quả chìm làm việc không có ma sát và không bị ảnh hưởng bởi bẩn bám "
        "trên bề mặt. Ở điều kiện ổn định, quả chìm chiếm một vị trí ổn định. Trọng lượng hiệu dụng của "
        "xích tác dụng lên quả chìm thay đổi tùy theo vị trí của quả chìm, mà vị trí này lại là hàm của "
        "khối lượng riêng chất lỏng. Quả chìm chứa một lõi biến áp bằng kim loại truyền sự thay đổi vị "
        "trí để một cuộn thu đo được. Hiệu điện thế vi sai — một hàm của độ dịch chuyển của quả chìm — "
        "được hiệu chuẩn thành đại lượng đo sự thay đổi của tỉ trọng. Một cầu nhiệt điện trở được dùng để "
        "bù ảnh hưởng của nhiệt độ lên khối lượng riêng."))
    b.append(fig(5, F.fig(5), "vi"))

    b.append(h4("Cân tỉ trọng khí", "Gas Specific Gravity Balance"))
    b.append(p(
        "Một cột khí cao được cân bằng đáy nổi của bình. Trọng lượng này được chuyển thành chuyển động "
        "của một kim chỉ thị chạy trên một thang chia theo đơn vị khối lượng riêng hoặc tỉ trọng. Phương "
        "pháp này có thể dùng cho mọi phép đo khối lượng riêng của chất khí."))

    b.append(h4("Cân khí kiểu lực đẩy", "Buoyancy Gas Balance"))
    b.append(p(
        "Trong thiết bị này, một phao (displacer) được gắn trên một đòn cân trong một bình, như trên "
        "Hình 21.6. Phao được cân bằng trong không khí, và số đọc trên áp kế được ghi lại tại đúng áp "
        "suất cân bằng. Sau đó không khí được thay bằng khí, và áp suất được điều chỉnh cho tới khi lập "
        "lại đúng trạng thái cân bằng đó. Tỉ số giữa áp suất của không khí và áp suất của khí chính là "
        "khối lượng riêng của khí so với không khí. Phương pháp này thường được áp dụng trong điều kiện "
        "phòng thí nghiệm và không phù hợp cho các phép đo liên tục."))
    b.append(fig(6, F.fig(6), "vi"))

    # ---- column type
    b.append(h3("Tỉ trọng kế kiểu cột", "Column-Type Densitometers"))
    b.append(p(
        "Có một số phiên bản khác nhau của phương pháp cột. Một ví dụ điển hình là phương pháp cột chuẩn, "
        "được minh hoạ trên Hình 21.7. Người ta dùng một cột chất lỏng mẫu và một cột nước có chiều cao "
        "đã biết, lấy từ các ống sục khí tương ứng. Một thiết bị đo chênh áp so sánh các chênh lệch áp "
        "suất, vốn tỉ lệ với khối lượng riêng tương đối của chất lỏng và của nước. Bằng cách thay đổi độ "
        "sâu nhúng của các ống, có thể đạt được một dải đo rộng. Cả hai cột phải được giữ ở cùng nhiệt độ "
        "để tránh phải hiệu chính ảnh hưởng của nhiệt độ."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p(
        "Một phương pháp đo khối lượng riêng đơn giản hơn và được dùng rộng rãi hơn đạt được bằng cách "
        "lắp đặt hai ống sục khí như minh hoạ trên Hình 21.8. Các ống được đặt trong chất lưu mẫu sao cho "
        "miệng của một ống cao hơn miệng ống kia. Áp suất cần để sục khí vào chất lưu từ cả hai ống bằng "
        "áp suất của chất lưu tại miệng các ống sục khí. Miệng của một ống cao hơn ống kia và khoảng cách "
        "giữa các miệng ống là cố định; do đó chênh lệch áp suất bằng trọng lượng của cột chất lỏng giữa "
        "hai miệng ống. Vì vậy phép đo chênh áp tương đương với trọng lượng của một thể tích chất lỏng "
        "không đổi, và có thể thực hiện việc hiệu chuẩn có quan hệ trực tiếp với khối lượng riêng của "
        "chất lỏng. Phương pháp này chính xác tới 0,1 % đến 1 % tỉ trọng. Nó phải được dùng với những "
        "chất lỏng không kết tinh hoặc không lắng cặn trong buồng đo trong quá trình đo."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Một phiên bản khác là kiểu nén dải đo (range suppression type), có thêm một buồng giảm áp không "
        "đổi như trên Hình 21.9. Buồng này được mắc nối tiếp với phía áp thấp để tạo thuận lợi cho việc "
        "chia thang và cho số đọc khối lượng riêng chính xác."))
    b.append(fig(9, F.fig(9), "vi"))

    # ---- vibrating element
    b.append(h3("Tỉ trọng kế phần tử rung", "Vibrating Element Densitometers"))
    b.append(p(
        "Nếu một vật chứa chất lưu hoặc được bao quanh bởi chất lưu được kích cho cộng hưởng ở tần số "
        "riêng của nó, thì tần số dao động của vật sẽ thay đổi khi đặc tính và điều kiện của chất lưu "
        "thay đổi. Tần số riêng tỉ lệ thuận với độ cứng của vật và tỉ lệ nghịch với tổng khối lượng của "
        "vật và của chất lưu. Nó cũng phụ thuộc hình dạng, kích thước và tính đàn hồi của vật liệu, ứng "
        "suất dư, khối lượng và sự phân bố khối lượng của vật. Về cơ bản, dao động của vật có thể được "
        "coi tương đương với chuyển động của một khối lượng gắn vào một lò xo cơ khí. Do đó có thể viết "
        "biểu thức cho tần số như sau:"))
    b.append(eq("f = √( K / (M + k·ρ) )", "21.3"))
    b.append(wl(["trong đó <b>K</b> là độ cứng của hệ",
                 "<b>M</b> là khối lượng của bộ chuyển đổi",
                 "<b>k</b> là hằng số của hệ",
                 "<b>ρ</b> là khối lượng riêng của chất lưu"]))
    b.append(p(
        "Một yếu tố chung cho mọi loại tỉ trọng kế phần tử rung là bài toán kích phần tử dao động và duy "
        "trì cộng hưởng riêng của nó. Có hai kiểu bộ kích cho mục đích này."))

    b.append(h4("Bộ kích từ", "Magnetic Drives"))
    b.append(p(
        "Việc kích từ phần tử rung và thu nhận dao động thường được thực hiện bằng các cụm cuộn dây nhỏ. "
        "Tín hiệu thu được bởi các cảm biến được khuếch đại và đưa trở lại làm tín hiệu kích để duy trì "
        "các lực kích thích lên vật rung của thiết bị."))
    b.append(p(
        "Để có được chế độ kích ổn định, cảm biến của phần tử rung có thể được làm bằng vật liệu không "
        "nhiễm từ. Trong trường hợp đó, người ta gắn thêm các phần ứng từ nhỏ."))
    b.append(p(
        "Ưu điểm chính của hệ thống kích và thu bằng từ là chúng là phương pháp không tiếp xúc. Chúng "
        "dùng các cuộn dây đồng thông thường và đáng tin cậy trong dải nhiệt độ từ −200 °C đến +200 °C."))

    b.append(h4("Bộ kích áp điện", "Piezoelectric Drives"))
    b.append(p(
        "Có nhiều loại vật liệu áp điện đáp ứng được yêu cầu kích các phần tử rung. Những vật liệu này có "
        "đặc tính nhiệt độ tốt giống như loại kích từ. Chúng còn có ưu điểm là giá thành thấp. Chúng có "
        "trở kháng cao, khiến mạch điều kiện tín hiệu tương đối dễ thiết kế. Chúng không cần cảm biến từ."))
    b.append(p(
        "Các bộ kích áp điện được gắn cơ khí lên phần tử rung bằng keo dán. Do đó phải chú ý đặt giá đỡ "
        "một cách cẩn thận để giảm ứng suất mà phần tử áp điện phải chịu do ứng suất nhiệt và ứng suất áp "
        "suất trong khi thiết bị làm việc."))
    b.append(p(
        "Nhiều loại tỉ trọng kế khác nhau đã được phát triển dựa trên hiện tượng này. Ba loại thương mại "
        "chính được giới thiệu dưới đây."))

    b.append(h4("Tỉ trọng kế ống rung", "Vibrating Tube Densitometers"))
    b.append(p(
        "Các thiết bị này phù hợp cho chất lỏng có độ nhớt cao hoặc cho ứng dụng với bùn. Nguyên lý hoạt "
        "động của tỉ trọng kế ống rung dựa trên dao động ngang của ống, như trên Hình 21.10. Ống và các "
        "cơ cấu kích được ràng buộc dao động trong một mặt phẳng. Khi chất lỏng chuyển động bên trong "
        "ống, khối lượng riêng của toàn bộ khối chất lỏng được đo. Chiều dài ống xấp xỉ 20 lần đường kính "
        "ống."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Một vấn đề thiết kế lớn của phương pháp ống rung là mâu thuẫn giữa việc hạn chế phần tử rung "
        "trong một chiều dài hữu hạn và việc cố định chính xác các nút. Phải đặc biệt chú ý tránh mọi sự "
        "trao đổi năng lượng dao động ra ngoài ống cảm biến. Ống đơn có nhược điểm là gây cản trở dòng "
        "chảy, do đó có một số tổn thất áp suất. Ngược lại, ống đôi gây cản trở rất nhỏ (Hình 21.11) và "
        "dễ kiểm tra, vệ sinh. Kích thước nhỏ gọn là một ưu điểm rõ rệt khác. Trong một số tỉ trọng kế, "
        "ống đôi được thiết kế để đạt cân bằng động tốt, với hai ống dao động ngược pha. Các nút của "
        "chúng được cố định ở hai đầu, thể hiện độ nhạy cực đại với khuyết điểm khi lắp đặt, với kẹp giữ "
        "và với tải khối lượng."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(p(
        "Các vấn đề thiết kế chính của cảm biến ống rung là giảm thiểu ảnh hưởng của lớp đệm ở hai đầu và "
        "khắc phục ảnh hưởng của áp suất và nhiệt độ. Bellows được dùng ở hai đầu ống cảm biến để cách ly "
        "cảm biến khỏi dao động bên ngoài. Bellows cũng giảm thiểu tải ở hai đầu do giãn nở khác nhau và "
        "do ứng suất khi lắp đặt."))
    b.append(p(
        "Chất lưu chảy qua ống; do đó không cần cân bằng áp suất. Tuy vậy, trong một số ứng dụng, áp suất "
        "gây ứng suất lên ống, dẫn tới thay đổi độ cứng. Một số nhà sản xuất cải biến ống để giảm thiểu "
        "ảnh hưởng của áp suất. Trong những trường hợp này, chỉ cần hiệu chính khi bắt buộc phải có độ "
        "chính xác cao. Có thể giảm sự thay đổi mô-đun Young theo nhiệt độ xuống gần bằng không bằng vật "
        "liệu Ni-span-C, miễn là tính ăn mòn của chất lưu cho phép. Thông thường các nhà sản xuất cung "
        "cấp hệ số hiệu chính áp suất và nhiệt độ cho sản phẩm của mình."))
    b.append(p(
        "Theo thông lệ, mỗi tỉ trọng kế phần tử rung được hiệu chuẩn so với các thiết bị khác như một "
        "chuỗi chuyển chuẩn. Phương pháp lực đẩy thường được dùng cho mục đích hiệu chuẩn. Các hệ số nhiệt "
        "độ và áp suất thường được tìm bằng cách cho bộ chuyển đổi làm việc qua một dải nhiệt độ và áp "
        "suất trên một chất lỏng có đặc tính đã biết rõ. Trước khi hiệu chuẩn, các tỉ trọng kế ống rung "
        "được đưa qua một chu trình đốt nóng – vận hành (burn-in) theo chương trình để ổn định chúng với "
        "nhiệt độ và áp suất."))

    b.append(h4("Tỉ trọng kế trụ rung", "Vibrating Cylinder Densitometers"))
    b.append(p(
        "Một trụ thành mỏng có tỉ lệ chiều dài : đường kính là 3 : 1, được cố định ở hai đầu cứng. Độ dày "
        "thành trụ thay đổi từ 25 µm đến 300 µm, tùy theo dải khối lượng riêng và loại chất lưu được "
        "dùng. Trụ có thể được kích dao động theo mode vòng (hoop mode) bằng các bộ kích từ gắn bên trong "
        "hoặc bên ngoài trụ."))
    b.append(p(
        "Để có đặc tính từ tốt, trụ được làm bằng vật liệu từ chống ăn mòn. Thép như FV520 thường được "
        "dùng cho mục đích này. Những vật liệu như vậy có đặc tính chống ăn mòn tốt; đáng tiếc là do đặc "
        "tính nhiệt đàn hồi kém nên chúng cần hiệu chính nhiệt độ nhiều."))
    b.append(p(
        "Các hợp kim niken–sắt như Ni-span-C thường được dùng để tránh ảnh hưởng của nhiệt độ. Sau khi "
        "được xử lý đúng, hợp kim Ni-span-C có mô-đun Young gần bằng không. Vì trụ được nhúng hoàn toàn "
        "trong chất lưu nên không có hệ số áp suất."))
    b.append(p(
        "Sự thay đổi tần số cộng hưởng được xác định bởi tải khối lượng cục bộ của chất lưu tiếp xúc với "
        "trụ. Đường cong tần số theo khối lượng riêng là phi tuyến và có dạng parabol, do đó cần tuyến "
        "tính hoá để có đầu ra thực dụng. Dải tần số cộng hưởng thay đổi từ 2 kHz đến 5 kHz, tùy theo dải "
        "khối lượng riêng của thiết bị. Các trụ cần được chế tạo chính xác nên rất đắt khi chế tạo. Mỗi "
        "thiết bị cần được hiệu chuẩn riêng cho các nhiệt độ và khối lượng riêng khác nhau để phù hợp với "
        "ứng dụng cụ thể. Với ứng dụng đo khối lượng riêng của chất khí, người ta dùng các chất khí có "
        "đặc tính đã biết rõ (ví dụ argon hoặc nitơ tinh khiết) để hiệu chuẩn. Trong trường hợp này, thiết "
        "bị được đặt trong môi trường khí có nhiệt độ và áp suất được kiểm soát. Các đường cong hiệu "
        "chuẩn đạt được bằng cách lặp lại nhiều lần cho phù hợp yêu cầu của từng khách hàng cho từng ứng "
        "dụng cụ thể. Với chất lỏng, thiết bị được hiệu chuẩn bằng các chất lỏng có khối lượng riêng đã "
        "biết, hoặc được hiệu chuẩn so với một chuẩn khác (ví dụ bình tỉ trọng hoặc tỉ trọng kế kiểu lực "
        "đẩy)."))
    b.append(p(
        "Tỉ trọng kế trụ rung có hệ số áp suất bằng không và rất lý tưởng cho các sản phẩm khí hoá lỏng "
        "hoặc chất lỏng tinh luyện. Do khe hở giữa trụ và vỏ tương đối nhỏ, chúng cần được vệ sinh định "
        "kỳ. Chúng không phù hợp với chất lỏng hoặc bùn có độ nhớt cao."))

    b.append(h4("Tỉ trọng kế nĩu rung", "Tuning Fork Densitometers"))
    b.append(p(
        "Các tỉ trọng kế này dùng tần số riêng của những nĩu rung có khối lượng nhỏ, như trên Hình 21.12. "
        "Trong một số trường hợp, chất lưu được đưa vào một buồng nhỏ đặt các nĩu được kích bằng cơ điện; "
        "trong trường hợp khác, nĩu được nhúng trực tiếp vào chất lỏng. Mỗi ứng dụng đều cần hiệu chuẩn."))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(p("Ưu điểm của các tỉ trọng kế phần tử rung gồm:"))
    b.append(ol([
        "Phù hợp cho cả chất lỏng và chất khí với độ chính xác hợp lý.",
        "Có thể được thiết kế cho các phép đo thời gian thực.",
        "Dễ giao tiếp vì chúng làm việc trên cơ sở tần số và vốn đã là tín hiệu số.",
        "Tương đối chắc chắn và dễ lắp đặt.",
        "Có các phiên bản lập trình được và đã vi tính hoá. Các phiên bản lập trình được tự động thực hiện "
        "mọi hiệu chính. Chúng cung cấp đầu ra là khối lượng riêng thực, khối lượng riêng ở điều kiện "
        "tham chiếu, khối lượng riêng tương đối, tỉ trọng, nồng độ, hàm lượng chất rắn…",
    ]))
    b.append(p("Nhược điểm gồm:"))
    b.append(ol([
        "Chúng không liên hệ trực tiếp với các phép đo sơ cấp; do đó phải được hiệu chuẩn.",
        "Tất cả đều gặp khó khăn khi đo chất lỏng đa pha.",
    ]))

    # ---- radioactive
    b.append(h3("Tỉ trọng kế phóng xạ", "Radioactive Densitometers"))
    b.append(p(
        "Khi các đồng vị phóng xạ phân rã, chúng phát ra bức xạ dưới dạng hạt hoặc sóng. Hiện tượng vật lý "
        "này có thể được dùng cho mục đích đo khối lượng riêng. Ví dụ, tia γ được cho đi qua mẫu và tốc độ "
        "đến của chúng được đo bằng các đầu dò dựa trên ion hoá hoặc nhấp nháy [2]. Nói chung, tốc độ hấp "
        "thụ khối lượng của tia γ không phụ thuộc thành phần vật liệu; do đó có thể lập trình chúng cho "
        "một dải vật liệu rộng. Các tỉ trọng kế dựa trên phương pháp bức xạ có thể đạt độ chính xác tới "
        "±0,0001 g mL⁻¹. Nhiều thiết bị trong số này có khả năng tự chẩn đoán và có thể bù trôi do nguồn "
        "phân rã, nhờ đó chỉ ra được các vấn đề về tín hiệu."))
    b.append(p(
        "Nếu tia γ có cường độ J₀ xuyên qua một vật liệu có khối lượng riêng ρ và độ dày d thì cường độ "
        "bức xạ sau khi đi qua vật liệu có thể được biểu diễn bằng:"))
    b.append(eq("J = J₀ · e^( −n·ρ·d )", "21.4"))
    b.append(wl(["trong đó <b>n</b> là hệ số hấp thụ khối lượng"]))
    b.append(p(
        "Độ chính xác của phép đo khối lượng riêng phụ thuộc độ chính xác của phép đo cường độ bức xạ và "
        "chiều dài đường đi d. Đường đi dài hơn qua vật liệu cho tín hiệu phát hiện mạnh hơn."))
    b.append(p(
        "Để vận hành chính xác, có nhiều cách bố trí vị trí tương đối của nguồn phát và đầu dò, một số "
        "được minh hoạ trên Hình 21.13 và 21.14. Nói chung, nguồn được đặt trong một hộp chì kẹp lên "
        "thành ống hoặc thành bình. Trong nhiều ứng dụng, đầu dò cũng được kẹp lên thành."))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p("Ưu điểm của việc dùng phương pháp phóng xạ gồm:"))
    b.append(ol([
        "Cảm biến không tiếp xúc với mẫu; do đó không cản trở đường đi của chất lỏng.",
        "Có thể đo chất lỏng đa pha.",
        "Có các dạng lập trình được và dễ giao tiếp.",
        "Phù hợp nhất trong những ứng dụng khó, chẳng hạn khai khoáng và công nghiệp quá trình nặng.",
    ]))
    b.append(p("Nhược điểm gồm:"))
    b.append(ol([
        "Cần có nguồn phóng xạ; do đó khó xử lý.",
        "Để có độ chính xác hợp lý cần một chiều dài đường đi tối thiểu.",
        "Có thể có hằng số thời gian dài, khiến chúng không phù hợp trong một số ứng dụng.",
        "Chúng chỉ phù hợp để đo khối lượng riêng của chất rắn và chất lỏng.",
    ]))

    # ---- refractometer
    b.append(h3("Tỉ trọng kế khúc xạ và chiết suất", "Refractometer and Index of Refraction Densitometers"))
    b.append(p(
        "Khúc xạ kế về bản chất là những thiết bị quang học làm việc theo nguyên lý khúc xạ của ánh sáng "
        "truyền trong môi trường lỏng. Tùy theo đặc tính của mẫu, có thể đo chiết suất theo nhiều cách "
        "khác nhau (ví dụ kỹ thuật góc tới hạn, kỹ thuật chuẩn trực và kỹ thuật dịch chuyển). Thông "
        "thường người ta dùng một đầu cảm biến đặt trên đường ống, trong đó một cửa sổ cảm biến (thường "
        "gọi là lăng kính) được làm ướt bởi sản phẩm cần đo. Trong một số phiên bản, đầu dò cảm biến phải "
        "được lắp bên trong đường ống hoặc trong bồn, bình chứa. Chúng hiệu quả nhất trong các ứng dụng "
        "quá trình kiểu phản ứng, nơi diễn ra việc pha trộn và trộn lẫn chất lỏng. Ví dụ, khúc xạ kế có "
        "thể đo chính xác hàm lượng chất rắn hoà tan."))
    b.append(p(
        "Có thể dùng đi-ốt hồng ngoại, laser và các nguồn sáng khác. Tuy nhiên, kỹ thuật đo này không được "
        "khuyến nghị cho các ứng dụng trong quá trình có chất rắn lơ lửng, độ đục cao, khí cuốn theo, màu "
        "đậm, độ trong và độ mờ kém, hoặc tốc độ dòng chảy cực cao. Số đọc được tự động hiệu chính theo "
        "sự thay đổi nhiệt độ của quá trình. Mạch xử lý có thể bao gồm các đầu ra tín hiệu điều chỉnh được "
        "về cả tần số và độ rộng xung."))
    b.append(p(
        "Một phiên bản khác của khúc xạ kế là tỉ trọng kế kiểu chiết suất. Ví dụ, với các cảm biến vị trí "
        "nhạy, chiết suất của chất lỏng cần đo được xác định bằng cách đo độ dịch ngang của một chùm tia "
        "laser. Khi chùm tia laser tới ô đo dưới một góc tới, như trên Hình 21.15, trục của chùm tia ló ra "
        "bị dịch đi bởi thành ô đo và bởi chất lỏng bên trong. Độ dịch ngang có thể được xác định chính "
        "xác bằng các cảm biến vị trí nhạy. Để có độ nhạy cực đại, các thiết bị cần được hiệu chuẩn với sự "
        "trợ giúp của giao thoa kế."))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(p(
        "Khúc xạ kế thường được dùng để kiểm soát việc pha tạp các chất lỏng thông dụng (ví dụ dầu ăn, "
        "rượu vang và xăng). Chúng cũng được ứng dụng trong công nghiệp bột giấy và giấy, thực phẩm và đồ "
        "uống, đường, sữa và các ngành hoá chất khác."))

    # ---- coriolis
    b.append(h3("Tỉ trọng kế Coriolis", "Coriolis Densitometers"))
    b.append(p(
        "Các hệ thống đo khối lượng riêng kiểu Coriolis tương tự phương pháp ống rung nhưng có thay đổi "
        "đôi chút về thiết kế. Chúng gồm một cảm biến và một bộ truyền xử lý tín hiệu. Mỗi cảm biến gồm "
        "một hoặc hai ống dẫn chất lưu đặt trong một vỏ cảm biến. Chúng được chế tạo với nhiều kích thước "
        "và hình dạng khác nhau [3]. Các ống cảm biến được neo chắc tại điểm vào và điểm ra của chất lưu, "
        "và được kích dao động ở đầu tự do, như trên Hình 21.16. Cảm biến hoạt động bằng cách áp dụng định "
        "luật thứ hai của Newton về chuyển động (F = ma)."))
    b.append(p(
        "Bên trong vỏ, các ống được kích dao động ở tần số riêng bằng các cuộn kích và một mạch hồi tiếp. "
        "Tần số cộng hưởng của cụm lắp ráp này là hàm của hình học phần tử, vật liệu chế tạo và khối lượng "
        "của cụm ống. Khối lượng ống gồm hai phần: khối lượng của bản thân ống và khối lượng chất lưu bên "
        "trong ống. Khối lượng của ống là cố định với một cảm biến cho trước. Khối lượng chất lưu trong "
        "ống bằng khối lượng riêng của chất lưu nhân với thể tích. Vì thể tích ống không đổi, tần số dao "
        "động có thể liên hệ trực tiếp với khối lượng riêng của chất lưu. Do đó, với một hình học ống và "
        "một vật liệu chế tạo cho trước, khối lượng riêng của chất lưu có thể được xác định bằng cách đo "
        "tần số cộng hưởng của dao động. Cảm biến nhiệt độ được dùng để khắc phục ảnh hưởng của sự thay "
        "đổi mô-đun đàn hồi của ống. Khối lượng riêng của chất lưu được tính bằng một quan hệ tuyến tính "
        "giữa khối lượng riêng với chu kỳ dao động của ống và các hằng số hiệu chuẩn."))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(p(
        "Nhiều nhà sản xuất cung cấp các thiết bị ngoại vi chuyên dụng dựa trên vi xử lý cho nhiều loại "
        "phép đo khác nhau. Tuy vậy, mọi thiết bị ngoại vi đo khối lượng riêng đều dùng tần số riêng của "
        "cảm biến kết hợp với nhiệt độ của cảm biến để tính khối lượng riêng trực tuyến của chất lưu quá "
        "trình. Các phương tiện truyền thông, giao tiếp tuỳ chọn và phần mềm phù hợp cũng được cung cấp."))

    # ---- absorption
    b.append(h3("Tỉ trọng kế kiểu hấp thụ", "Absorption-Type Densitometers"))
    b.append(p(
        "Kỹ thuật hấp thụ cũng được dùng để đo khối lượng riêng trong những ứng dụng cụ thể. Tia X, ánh "
        "sáng khả kiến, ánh sáng tử ngoại và hấp thụ âm là những ví dụ điển hình của phương pháp này. Về "
        "bản chất, độ suy giảm và độ dịch pha của một chùm tia được tạo ra khi đi qua mẫu được cảm nhận và "
        "liên hệ với khối lượng riêng của mẫu. Phần lớn các tỉ trọng kế kiểu hấp thụ được thiết kế riêng "
        "cho những ứng dụng có đặc tính đặc thù. Hai ví dụ điển hình là: (1) hấp thụ tử ngoại hoặc hấp thụ "
        "tia X được dùng để xác định khối lượng riêng cục bộ của các lắng đọng thuỷ ngân trong đèn phóng "
        "điện hồ quang, và (2) cảm biến khối lượng riêng siêu âm được dùng cho những phép đo khối lượng "
        "riêng khó, chẳng hạn đo khối lượng riêng của bùn. Ví dụ, bùn vôi là một vật liệu rất khó xử lý. "
        "Nó có xu hướng lắng mạnh và bám lên mọi thiết bị mà nó tiếp xúc. Một cảm biến điều khiển khối "
        "lượng riêng bằng siêu âm có thể được nhúng hoàn toàn vào bùn đang được khuấy, nhờ đó tránh được "
        "các vấn đề bám và tắc. Vì độ suy giảm của chùm siêu âm tỉ lệ với lượng chất rắn lơ lửng, tín hiệu "
        "điện thu được tỉ lệ với tỉ trọng của bùn. Những thiết bị như vậy có thể đạt độ chính xác tới "
        "0,01 %. Thiết bị siêu âm đo phần trăm chất rắn lơ lửng trong bùn bằng cách cho một giá trị xấp xỉ "
        "gần đúng của tỉ trọng."))

    # ---- references
    b.append(h2("Tài liệu tham khảo", "References"))
    refs = [
        "H. Eren, Particle concentration characteristics and density measurements of slurries using "
        "electromagnetic flowmeters, <i>IEEE Trans. Instr. Meas.</i>, 44, 783–786, 1995.",
        "<i>Micro Motion Product Catalogue</i>, Mount Prospect, IL: Fisher-Rosemount, 1995.",
        "Kay-Ray, <i>Solution for Process Measurement</i>, Mount Prospect, IL: Fisher-Rosemount, 1995.",
    ]
    b.append('<ol class="refs">' + "".join("<li>%s</li>" % r for r in refs) + "</ol>")

    b.append(note(
        "<b>Phụ lục — Danh sách nhà sản xuất.</b> Bản gốc có một phụ lục liệt kê địa chỉ và số điện thoại "
        "của 13 nhà sản xuất thiết bị đo khối lượng riêng: ABB K-Flow, American Density Materials, Anton "
        "Paar U.S.A., Arco Instrument Company, Cambridge Applied Systems, Dynatron (Automation Products), "
        "Kay-Ray/Sensall (Fisher-Rosemount), McGee Engineering, Porous Materials, Princo Instruments, "
        "Quantachrome, Tricor Systems và X-rite. Phần địa chỉ bưu chính và số điện thoại của ấn bản 1999 "
        "đã được lược bỏ vì đây là thông tin thương mại đã lạc hậu; tên các hãng được giữ lại để tra cứu."))

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 20</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Density matters in instrumentation for two reasons: determining the mass and volume of a product, "
        "and establishing its quality. Density is the mass of a given volume of a substance under fixed "
        "conditions, and it varies with pressure and temperature — far more so for gases. Measurements are "
        "either static or dynamic (on-line); static methods are better developed, cheaper and more "
        "accurate, dynamic samplers are expensive and highly automated. No single technique is universal: "
        "specific gravity (SG) is the dimensionless ratio of a substance's density to that of a standard "
        "— water for liquids (Eq. 21.1), air for gases (Eq. 21.2) — usually quoted at NTP or STP."))
    b.append(p(
        "Solid density is simple when the material is uniform: density = mass/volume. Where solids have "
        "mixed constituents and changing volumes, dynamic methods such as radioactive absorption and "
        "ultrasonics are used. Fluid density is far more complex, and the chapter covers eleven device "
        "families: pycnometric, buoyancy, hydrometer, hydrostatic weighing, balance-type, column-type, "
        "vibrating element, radioactive, refractometer/index-of-refraction, Coriolis and absorption type."))
    b.append(h2("21.1 Solid Density", "Khối lượng riêng của chất rắn"))
    b.append(p(
        "Once the volume and mass of a uniform solid are known the density follows directly from the basic "
        "ratio, in kg m⁻³. When the material is inhomogeneous or its volume changes, dynamic techniques are "
        "required."))
    b.append(h2("21.2 Fluid Density", "Khối lượng riêng của chất lưu"))
    b.append(p(
        "Pycnometers (Figure 21.1) are static fixed-volume vessels: the bottle is weighed empty, then full "
        "of distilled aerated water to establish its volume, then full of the process fluid. A capillary in "
        "the stopper fixes the exact volume. Twin capillaries allow vacuum filling. They must be light, "
        "strong and nonmagnetic, and high-resolution balances are needed. Advantages: accurate and usable "
        "for both density and SG. Disadvantages: operator skill matters, the sample must be taken off-line, "
        "and high-precision units are expensive."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Buoyancy densitometers use Archimedes' principle: a sinker of known mass and volume on a fine wire "
        "is fully immersed and a precision force balance measures the supporting force, with corrections for "
        "surface tension on the wire, the sinker's cubic expansion coefficient and process temperature. They "
        "are accurate enough to calibrate other liquid density transducers; the magnetic-suspension version "
        "encloses the sinker in a pressure vessel and eliminates surface-tension error."))
    b.append(p(
        "Hydrometers (Figure 21.2) are the most common liquid densitometers and are covered by standards such "
        "as ISO 387. A sealed ballasted bulb with a long graduated stem converts the volume of a fixed mass "
        "into a linear distance; the scale reads in kg m⁻³ or in SG, °API, Brix, Brine. ISO 387 covers "
        "600–2000 kg m⁻³. They are cheap, have good resolution over a small span and are traceable, but the "
        "span is small, glass is fragile, the sample is off-line, and good precision needs surface-tension "
        "and temperature corrections."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Hydrostatic weighing (Figure 21.3) weighs a pivoted U-tube on flexible end couplings, usually "
        "stainless bellows, with a force balance. It reads continuously and handles two-phase liquids such as "
        "slurries, sugar solutions and powders, but must be mounted horizontally on a solid base, is bulky, "
        "and cannot measure gases."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Balance-type densitometers come in four common forms. The balanced-flow vessel (Figure 21.4) weighs "
        "a fixed-volume vessel through which liquid flows continuously, using a spring balance or pneumatic "
        "force-balance transmitter. The chain balanced float (Figure 21.5) suspends a self-centering "
        "fixed-volume plummet entirely below the surface; the chain force depends on plummet position, a "
        "transformer core transmits position to a pickup coil, and a resistance thermometer bridge "
        "compensates temperature. The gas specific gravity balance weighs a tall gas column against the "
        "floating bottom of the vessel. The buoyancy gas balance (Figure 21.6) balances a displacer in air, "
        "then in gas at adjusted pressure; the pressure ratio gives SG relative to air — a laboratory method, "
        "not for continuous measurement."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "Column densitometers use bubbler tubes. The reference column version (Figure 21.7) compares a known "
        "head of sample liquid against water with a differential-pressure transmitter; both columns must be "
        "at the same temperature. The two-tube version (Figure 21.8) fixes the mouths at different heights, "
        "so the differential pressure equals the weight of the liquid column between them and can be "
        "calibrated directly against density — accurate to 0.1%–1% SG, but only for liquids that neither "
        "crystallize nor settle. The suppression type (Figure 21.9) adds a constant pressure-drop chamber in "
        "series with the low-pressure side for better scaling and accuracy."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "Vibrating element densitometers exploit the shift in natural frequency as fluid properties change: "
        "f = √(K/(M + kρ)) (Eq. 21.3), where K is system stiffness, M transducer mass, k a system constant "
        "and ρ fluid density. Elements are driven magnetically (noncontact copper coils, reliable from "
        "−200 °C to +200 °C) or piezoelectrically (low cost, high impedance, no magnetic sensors, but bonded "
        "with adhesive so mounting strain matters). The vibrating tube (Figure 21.10) suits viscous liquids "
        "and slurries, with length about 20 diameters; twin tubes (Figure 21.11) vibrate in antiphase, block "
        "the flow far less and are easy to clean. The vibrating cylinder is a thin-walled 3:1 cylinder in a "
        "hoop mode, 25–300 µm wall, giving zero pressure coefficient — ideal for liquefied gases and refined "
        "liquids, but costly and unsuitable for viscous fluids. The tuning fork (Figure 21.12) uses low-mass "
        "forks, either in a small chamber or directly in the liquid, and always needs calibration. "
        "Advantages: work for liquids and gases, real-time, inherently digital, robust, programmable "
        "versions that output live and reference density, relative density, SG and concentration. "
        "Disadvantages: no direct link to primary measurements, and problems with multiphase liquids."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(fig(11, F.fig(11), "en"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "Radioactive densitometers pass γ rays through the sample and count arrivals with ion or "
        "scintillation detectors: J = J₀e^(−nρd) (Eq. 21.4), with n the mass absorption coefficient. Mass "
        "absorption is largely independent of composition, accuracy reaches ±0.0001 g mL⁻¹, and many units "
        "self-diagnose and compensate source decay. A longer path gives a stronger signal, so the pipe is "
        "either enlarged (Figure 21.13) or elongated (Figure 21.14), with the shielded source and usually the "
        "detector clamped to the wall. Advantages: non-contacting, works on multiphase liquids, programmable, "
        "suited to mining and heavy process industries. Disadvantages: a radioactive source must be handled, "
        "a minimum path length is needed, time constants can be long, and it suits only solids and liquids."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))
    b.append(p(
        "Refractometers are optical instruments using refraction in liquid media, typically with an in-line "
        "sensing window (prism) wetted by the product; they excel in blending and mixing applications and can "
        "measure dissolved solids. They are not recommended for suspended solids, high turbidity, entrained "
        "air, heavy colour, poor transparency or very high flow rates. The index-of-refraction version "
        "(Figure 21.15) measures the lateral displacement of a laser beam crossing the cell at an angle; "
        "position-sensitive detectors read the displacement, and interferometers are used for maximum "
        "sensitivity. Applications include adulteration control of edible oils, wines and gasoline, plus "
        "pulp and paper, food and beverage, sugar, dairy and chemicals."))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p(
        "Coriolis densitometers (Figure 21.16) resemble vibrating tubes: one or two flow tubes in a sensor "
        "housing, anchored at inlet and outlet and driven at the free end, using F = ma. The resonant "
        "frequency depends on geometry, material and tube-assembly mass, and the fluid mass equals density "
        "times the constant tube volume, so frequency relates directly to density. Temperature sensors "
        "compensate the change in elastic modulus, and density is computed from a linear relationship with "
        "tube period and calibration constants. Absorption densitometers use X-ray, visible, UV or sonic "
        "attenuation and phase shift — for example UV/X-ray for local mercury deposit density in arc discharge "
        "lamps, and ultrasonic sensors for slurries such as lime, where the probe can be fully immersed in "
        "agitated slurry to avoid coating, reaching 0.01% accuracy."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "The chapter closes with 3 references and an appendix listing 13 manufacturers, reproduced in the "
        "Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 20</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 21 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 21 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 21 “Đo khối lượng riêng” của Halit Eren (Curtin University of "
            "Technology) — khối lượng riêng và tỉ trọng, khối lượng riêng của chất rắn và chất lưu, và 11 "
            "họ thiết bị đo: bình tỉ trọng, lực đẩy, tỉ trọng kế thuỷ tinh, cân thuỷ tĩnh, kiểu cân, kiểu "
            "cột, phần tử rung, phóng xạ, khúc xạ, Coriolis và hấp thụ, với 16 hình và 4 phương trình." if vi
            else
            "Companion to Chapter 21 of the CRC Measurement Handbook — density measurement: specific "
            "gravity, solid and fluid density, and eleven densitometer families from pycnometers to "
            "Coriolis and absorption types.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 21' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 21' % BASE_EN)
    meta = ("Chương 21 · theo Ch21.pdf (CRC Press, 1999) · 16 hình, 4 phương trình, 3 tài liệu tham khảo" if vi
            else "Chapter 21 · 16 figures, 4 equations, 3 references")
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
