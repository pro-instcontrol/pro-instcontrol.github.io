# -*- coding: utf-8 -*-
"""Handbook Chapter 20 — Mass and Weight Measurement
(Mark Fritz and Emil Hazarian, Denver Instrument Company).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch20.py
"""
import os

import hb20fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch20-mass-and-weight-measurement"
TITLE_EN = "Mass and Weight Measurement"
TITLE_VI = "Đo khối lượng và trọng lượng"
BYLINE = "Mark Fritz và Emil Hazarian · Denver Instrument Company"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch19-frequency-measurement"
PREV_VI = "ch19-frequency-measurement"
PREV_T_EN = "Frequency Measurement"
PREV_T_VI = "Đo tần số"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-20-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
    """Compact definition block: 'where ...' symbol list."""
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


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
        "Khối lượng và trọng lượng thường được dùng lẫn cho nhau; tuy vậy, chúng khác nhau. Khối lượng "
        "là đại lượng định lượng của quán tính của một vật ở trạng thái nghỉ. Như một đại lượng vật lý, "
        "khối lượng là tích của khối lượng riêng và thể tích. Trọng lượng, hay lực trọng trường, là lực "
        "mà Trái Đất hút một vật. Lực trọng trường được xác định bằng tích của khối lượng và gia tốc "
        "trọng trường."))
    b.append(eq("M = V × D", "20.1"))
    b.append(wl(["trong đó <b>M</b> = khối lượng",
                 "<b>V</b> = thể tích",
                 "<b>D</b> = khối lượng riêng"]))
    b.append(note(
        "Trong hầu hết các sách, ký hiệu của khối lượng riêng là chữ Hy Lạp ρ."))
    b.append(eq("W = M × G", "20.2"))
    b.append(wl(["trong đó <b>W</b> = trọng lượng",
                 "<b>G</b> = gia tốc trọng trường"]))
    b.append(p(
        "Vật thể hiện đơn vị khối lượng được gọi là các quả cân (weights); điều này càng làm tăng sự "
        "nhầm lẫn giữa khối lượng và trọng lượng. Trong Hệ Đơn vị Quốc tế (SI) — hệ đo lường mét đã "
        "được hiện đại hóa — đơn vị của khối lượng gọi là kilôgam và đơn vị của lực gọi là niutơn. Ở "
        "Hệ đo lường thông dụng Hoa Kỳ, đơn vị khối lượng gọi là slug và đơn vị lực gọi là pound. Khi "
        "dùng các đơn vị thông dụng Hoa Kỳ, người ta dùng pound để chỉ khối lượng của một vật, bởi vì "
        "tại Hoa Kỳ pound đã được định nghĩa theo kilôgam từ năm 1893."))

    # ---- 20.1
    b.append(h2("20.1 Thiết bị cân", "Weighing Instruments"))
    b.append(p(
        "Cân là một trong những phép đo cổ nhất mà con người biết đến, có từ trước khi có chữ viết. "
        "Cân hai đĩa có tay đòn bằng nhau có lẽ là thiết bị đầu tiên được dùng để cân. Đó là một dụng "
        "cụ đơn giản gồm hai đĩa treo trên một thanh đòn, cách đều một điểm tựa ở giữa. Quả chuẩn được "
        "đặt trên một đĩa và vật cần đo được đặt trên đĩa thứ hai; khi thanh đòn nằm ngang thì vật chưa "
        "biết bằng quả chuẩn. Phương pháp đo này đến nay vẫn còn được dùng rộng rãi trên khắp thế giới. "
        "Hình 20.1 giới thiệu một cân hai đĩa tay đòn bằng nhau của Ainsworth."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Cân là dụng cụ đo dùng để xác định khối lượng của một vật bằng cách đo lực mà vật tác dụng lên "
        "giá đỡ của nó trong trường hấp dẫn của Trái Đất. Người ta đặt một quả chuẩn đã biết giá trị lên "
        "một đĩa của cân, rồi thêm vật liệu chưa biết vào đĩa thứ hai cho đến khi lực hấp dẫn tác dụng "
        "lên vật chưa biết bằng lực hấp dẫn tác dụng lên quả chuẩn. Điều này có thể biểu diễn bằng toán "
        "học như sau:"))
    b.append(eq("S × G = U × G", "20.3"))
    b.append(wl(["trong đó <b>S</b> = khối lượng của quả chuẩn",
                 "<b>G</b> = gia tốc trọng trường",
                 "<b>U</b> = khối lượng của vật chưa biết"]))
    b.append(p(
        "Vì khoảng cách giữa hai đĩa rất ngắn, người ta giả định các lực hấp dẫn tác dụng lên chúng bằng "
        "nhau. Một giả định khác là hai cánh tay đòn của cân bằng nhau."))
    b.append(p(
        "Do lực hấp dẫn bằng nhau nên có thể giản ước nó khỏi phương trình, và quả chuẩn với vật chưa "
        "biết được coi là bằng nhau. Điều này dẫn tới một trong những đặc điểm của cân tay đòn bằng nhau "
        "cũng như của các thiết bị cân khác: cần có một bộ quả chuẩn bao trùm mọi giá trị đo khả dĩ. Cân "
        "chỉ có thể chỉ ra hai vật có bằng nhau hay không, và có khả năng hạn chế trong việc xác định hai "
        "vật chênh nhau bao nhiêu."))
    b.append(p(
        "Thử nghiệm đầu tiên nhằm tạo ra cân đọc trực tiếp có lẽ là sự ra đời của cân một đĩa kiểu thay "
        "thế (single pan substitution balance). Về nguyên tắc, cân thay thế giống cân tay đòn bằng nhau. "
        "Vật cần đo được đặt lên đĩa cân; bên trong cân có một loạt quả cân đã hiệu chuẩn, có thể thêm "
        "vào phía chuẩn của cân nhờ các mặt số và hệ đòn. Các quả cân này được thêm bớt bằng hệ cơ khí "
        "của cân để cân bằng với rất nhiều mức tải khác nhau. Chênh lệch rất nhỏ giữa bộ quả cân và tải "
        "được đọc trên một thang quang học."))
    b.append(p(
        "Cân lò xo có lẽ là thiết bị rẻ nhất để thực hiện các phép đo khối lượng. Một lần nữa, lực hấp "
        "dẫn lại được dùng làm chuẩn. Cân được bố trí sao cho vật chưa biết được treo vào lò xo và lực "
        "hấp dẫn có thể tác dụng tự do lên vật. Độ đàn hồi của lò xo được giả định là tuyến tính và lực "
        "cần để kéo giãn nó được ghi trên thang. Khi lực hấp dẫn và lực đàn hồi của lò xo cân bằng nhau, "
        "lực được đọc trên thang — thang này đã được hiệu chuẩn theo đơn vị khối lượng. Có thể tăng phạm "
        "vi đo bằng cách tăng độ cứng của lò xo; tuy nhiên, khi độ cứng của lò xo tăng thì độ phân giải "
        "của cân giảm. Sự giảm độ phân giải này hạn chế cân lò xo ở mức tải tương đối nhỏ, không quá vài "
        "kilôgam. Có hai loại lò xo được dùng: lò xo xoắn ốc và lò xo công-xôn."))
    b.append(p(
        "Cân xoắn (torsion balance) là một dạng cải tiến chính xác của nguyên lý lò xo, dùng để xác định "
        "khối lượng một cách gián tiếp. Lực thẳng đứng do tải sinh ra tạo một mô-men xoắn trên một dây "
        "hoặc một thanh. Mô-men này gây ra một góc lệch. Chừng nào cân còn làm việc trong vùng tuyến "
        "tính, góc lệch tỉ lệ với mô-men; do đó góc lệch cũng tỉ lệ với tải đặt vào. Khi hằng số xoắn của "
        "lò xo đã được hiệu chuẩn, góc lệch có thể được đọc theo đơn vị khối lượng. Khác với các cân lò "
        "xo thô sơ, có thể chế tạo cân xoắn có khả năng đo tới vùng microgam. Phần tử xoắn có thể là một "
        "dải, một dây hoặc một sợi."))
    b.append(p(
        "Cân đòn (beam balance) có lẽ là bước tiến tiếp theo về độ chính xác và giá thành. Cân đòn dùng "
        "cùng nguyên lý hoạt động như cân tay đòn bằng nhau; tuy nhiên, nó thường chỉ có một đĩa và thanh "
        "đòn được đặt lệch. Một bộ quả trượt được gắn trên thanh đòn. Khi các quả trượt dịch ra phía "
        "ngoài, chúng có thêm lợi thế cơ học nhờ khoảng cách tới điểm tựa của cân không bằng nhau. Các "
        "quả trượt dịch dọc thanh đòn cho đến khi cân ở trạng thái cân bằng. Trên thanh đòn có các vị trí "
        "khấc được đánh dấu tương ứng với lực do các quả trượt tác dụng. Bằng cách cộng các lực chỉ ra "
        "bởi vị trí của từng quả trượt, ta xác định được khối lượng của vật liệu chưa biết. Cân đòn có "
        "nhiều mức chính xác và phạm vi cân khác nhau: có loại cân đòn đo tới miligam, và có loại cân "
        "đòn lớn được chế tạo với phạm vi cân dùng để cân ô tô tải và toa tàu. Một lần nữa, nhược điểm "
        "là khi tải tăng thì độ phân giải giảm. Hình 20.2 là một ví dụ về cân đòn hai đĩa."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Bước tiến tiếp theo về giá thành và độ chính xác là load cell biến trở lực căng (strain gage "
        "load cell). Biến trở lực căng là một phần tử dây dẫn có điện trở, thay đổi điện trở khi chiều "
        "dài của phần tử dây thay đổi. Cảm biến được dán chặt lên một trụ thép, trụ này ngắn lại khi bị "
        "nén hoặc dài ra khi bị kéo. Vì cảm biến được dán chặt vào trụ, chiều dài của dây sẽ dài ra hoặc "
        "co lại cùng với trụ. Điện trở tỉ lệ với chiều dài của phần tử dây của cảm biến. Bằng cách đo "
        "điện trở của biến trở lực căng, có thể xác định được tải trên load cell. Điện trở được mạch "
        "điện tử trong thiết bị chỉ thị chuyển thành số đọc theo đơn vị khối lượng."))
    b.append(p(
        "Load cell hoàn lực là lõi của một cân điện tử, được thể hiện trên Hình 20.3. Load cell hoàn lực "
        "dùng nguyên lý của cân tay đòn bằng nhau; tuy nhiên, trong đa số trường hợp điểm tựa được đặt "
        "lệch nên nó không còn là cân tay đòn bằng nhau nữa, vì một phía được thiết kế để có lợi thế cơ "
        "học. Phía này của cân được gắn với một cuộn dây điện từ, và cuộn dây được treo trong một từ "
        "trường. Phía còn lại vẫn được nối với đĩa cân. Gắn trên thanh đòn là một bộ phát hiện điểm "
        "không, gồm một quang đi-ốt và một đi-ốt phát sáng (LED), dùng để xác định khi nào cân ở trạng "
        "thái cân bằng. Khi đặt tải lên đĩa cân, cân ra khỏi trạng thái cân bằng. Mạch LED – quang đi-ốt "
        "phát hiện cân không còn cân bằng, và dòng điện trong cuộn dây được tăng lên để đưa cân trở lại "
        "trạng thái cân bằng. Dòng điện này sau đó được đo trên một điện trở cảm biến chính xác, được "
        "chuyển thành số đọc theo đơn vị khối lượng và hiển thị trên màn hình số."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Một biến thể của loại vừa nêu là thế hệ mới của cân công nghiệp, cân phòng thí nghiệm và thiết "
        "bị so sánh khối lượng (mass comparator). Thiết bị so sánh khối lượng không còn được gọi là cân "
        "nữa, vì chúng luôn thực hiện một phép so sánh giữa khối lượng đã biết (quả chuẩn) và khối lượng "
        "chưa biết. Các thiết bị cân này dùng nguyên lý bù lực điện từ kết hợp với các khớp nối mềm thay "
        "cho các khớp dao cạnh truyền thống. Một số ưu điểm gồm khả năng giao tiếp với máy tính và đặc "
        "tính không cần bảo trì vì không có chi tiết chuyển động."))
    b.append(p(
        "Một phương pháp đo khác được dùng trong kỹ thuật cân là dây rung (vibrating cord). Một dây hoặc "
        "sợi có chiều dài đã biết, dao động theo phương ngang, được căng bởi lực F. Tần số dao động thay "
        "đổi tỉ lệ thuận với tải F. Hiệu ứng áp điện cũng được dùng trong kỹ thuật cân: các thiết bị cân "
        "loại này dựa trên sự xuất hiện của một điện áp trên bề mặt tinh thể khi tinh thể chịu tải. Cân "
        "dùng hiệu ứng con quay hồi chuyển cũng được sử dụng; thiết bị đo này dùng tín hiệu ra của một "
        "tế bào hồi chuyển động học, tương tự như tần số. Cũng đã biết các loại cân trong đó lực trọng "
        "trường của tải làm thay đổi khoảng cách chuẩn của các bộ chuyển đổi điện dung hoặc điện cảm. "
        "Ngoài ra còn tồn tại các loại cân dựa trên sự thay đổi tính phóng xạ của một vật theo khối lượng "
        "của nó trong những điều kiện nhất định."))

    # ---- 20.2
    b.append(h2("20.2 Kỹ thuật cân", "Weighing Techniques"))
    b.append(p(
        "Khi yêu cầu độ chính xác tương đối thấp, việc đọc trực tiếp các giá trị khối lượng hoặc trọng "
        "lượng trên thiết bị cân là đủ. Trừ cân tay đòn bằng nhau và một số cân xoắn, hầu hết thiết bị "
        "cân hiện đại đều có khả năng đọc trực tiếp. Với phần lớn giao dịch thương mại và các thí nghiệm "
        "khoa học đơn giản, số đọc trực tiếp này sẽ cho kết quả chấp nhận được."))
    b.append(p(
        "Với cân tay đòn bằng nhau, cân sẽ có một kim chỉ và một thang chia. Khi cần độ chính xác tương "
        "đối thấp, kim và thang được dùng để chỉ khi cân gần đạt trạng thái cân bằng; điều này cũng đúng "
        "khi dùng cân xoắn. Tuy vậy, các cân tay đòn bằng nhau có phạm vi nhỏ (ví dụ 30 g) hoặc lớn (ví "
        "dụ 900 kg) cũng được dùng cho các ứng dụng độ chính xác cao. Chỉ có thế hệ cân điện tử mới là "
        "ngang bằng hoặc tốt hơn về độ chính xác, đồng thời có thêm các tính năng khác."))
    b.append(p(
        "Cân là một quá trình đơn giản đến mức dễ gây nhầm lẫn. Phần lớn mọi người đã thực hiện và sử "
        "dụng các phép đo cân trong phần lớn cuộc đời mình. Ai cũng đã ra chợ mua thực phẩm bán theo "
        "trọng lượng, đã tự cân mình nhiều lần, và phần lớn chúng ta đã làm các phép đo trọng lượng hoặc "
        "khối lượng ở trường. Còn gì đơn giản hơn? Đặt một vật lên đĩa hoặc bàn cân rồi đọc kết quả."))
    b.append(p(
        "Đáng tiếc, quá trình cân rất dễ mắc sai số. Có sai số do khuyết điểm của thiết bị cân; sai số do "
        "độ lệch (bias) của các quả chuẩn được dùng; sai số do phương pháp cân; sai số do người vận hành; "
        "và sai số do các yếu tố môi trường. Với cân tay đòn bằng nhau, bất kỳ sự khác biệt nào giữa "
        "chiều dài hai cánh tay đòn đều dẫn tới một độ lệch trong kết quả đo. Gần như mọi thiết bị cân "
        "đều có một mức sai số nào đó do tính phi tuyến nhỏ của thiết bị. Mọi quả chuẩn đều có một mức độ "
        "lệch và độ không đảm bảo nhất định. Khối lượng là đại lượng cơ bản duy nhất trong Hệ Đơn vị "
        "Quốc tế (SI) được định nghĩa gắn với một hiện vật vật lý. Nguyên mẫu quốc tế của kilôgam được "
        "lưu giữ tại Sèvres (Pháp), dưới sự bảo quản của Văn phòng Cân đo Quốc tế. Mọi phép đo khối lượng "
        "đều bắt nguồn từ chuẩn quốc tế này. Theo thỏa thuận quốc tế, nguyên mẫu quốc tế của kilôgam là "
        "chính xác; tuy nhiên, trong hơn một thế kỷ qua, giá trị của nó đã thay đổi. Điều người ta không "
        "biết là độ lớn và chiều của sự thay đổi đó. Cuối cùng, các yếu tố môi trường như nhiệt độ, áp "
        "suất khí quyển và độ ẩm cũng có thể ảnh hưởng tới quá trình cân."))
    b.append(p(
        "Có nhiều kỹ thuật cân được dùng để giảm sai số trong quá trình cân. Kỹ thuật đơn giản nhất là "
        "cân thay thế (substitution weighing). Kỹ thuật thay thế được dùng để loại bỏ một số sai số do "
        "thiết bị cân gây ra. Kỹ thuật thay thế đơn là kỹ thuật trong đó một quả chuẩn đã biết và một "
        "vật chưa biết đều được cân trên cùng một thiết bị. Thiết bị cân chỉ được dùng để xác định chênh "
        "lệch giữa quả chuẩn và vật chưa biết. Trước tiên, cân quả chuẩn và ghi lại chỉ thị của thiết bị "
        "(với cân tay đòn bằng nhau, thêm các quả tare vào đĩa thứ hai để đưa cân về trạng thái cân "
        "bằng). Sau đó lấy quả chuẩn ra khỏi thiết bị và đặt vật chưa biết vào đúng vị trí đó; lại ghi "
        "lại chỉ thị của thiết bị. Lấy chỉ thị thứ hai trừ chỉ thị thứ nhất, ta được chênh lệch giữa quả "
        "chuẩn và vật chưa biết. Cộng chênh lệch này vào giá trị đã biết của quả chuẩn để tính giá trị "
        "của vật chưa biết. Một biến thể của kỹ thuật này là dùng một quả cân nhỏ đã biết giá trị để dịch "
        "chuyển thiết bị cân đi một lượng nhỏ; lượng dịch chuyển sau đó được chia cho giá trị đã biết của "
        "quả cân nhỏ để hiệu chuẩn số đọc của thiết bị. Kết quả cân của phép đo này được tính như sau:"))
    b.append(eq("U = S + (O₂ − O₁) × SW / (O₃ − O₂)", "20.4"))
    b.append(wl(["trong đó <b>U</b> = giá trị của vật chưa biết",
                 "<b>S</b> = giá trị đã biết của quả chuẩn",
                 "<b>SW</b> = quả cân độ nhạy nhỏ dùng để hiệu chuẩn các khoảng chia của cân",
                 "<b>O₁</b> = quan sát thứ nhất (quả chuẩn)",
                 "<b>O₂</b> = quan sát thứ hai (vật chưa biết)",
                 "<b>O₃</b> = quan sát thứ ba (vật chưa biết + SW)"]))
    b.append(p(
        "Các kỹ thuật này loại bỏ phần lớn sai số do thiết bị cân gây ra, và là đủ khi kết quả tới vài "
        "phần mười gam được coi là chấp nhận được."))
    b.append(p(
        "Nếu cần kết quả tốt hơn vài phần mười gam, các yếu tố môi trường bắt đầu gây ra sai số đáng kể "
        "trong quá trình cân. Sự khác biệt về khối lượng riêng giữa quả chuẩn và vật chưa biết, cùng với "
        "khối lượng riêng của không khí, kết hợp lại gây ra những sai số đáng kể trong quá trình cân."))
    b.append(p(
        "Chính lực đẩy Ác-si-mét gây ra sự nhầm lẫn trong cân. Cái được gọi là “khối lượng thực” (true "
        "mass) của một vật là khối lượng được xác định trong chân không. Các thuật ngữ “khối lượng "
        "thực” và “khối lượng trong chân không” cùng chỉ một khái niệm khối lượng quán tính, tức khối "
        "lượng theo nghĩa Newton. Trong đời sống thực tế, các phép đo được thực hiện trong môi trường "
        "không khí xung quanh; do đó các vật tham gia quá trình đo tuân theo nguyên lý Ác-si-mét, bị nâng "
        "lên bởi một lực bằng trọng lượng của thể tích không khí bị chúng chiếm chỗ. Để áp dụng hiệu "
        "chính lực đẩy cho phép đo, cần đưa vào thuật ngữ “khối lượng biểu kiến” (apparent mass). “Khối "
        "lượng biểu kiến” của một vật được định nghĩa theo “nhiệt độ chuẩn” và “khối lượng riêng chuẩn "
        "của không khí”, theo quy ước được chọn là 20°C và 1,2 mg cm⁻³. Vì dùng các giá trị quy ước này, "
        "“khối lượng biểu kiến” còn được gọi là “khối lượng quy ước” (conventional mass). Vật liệu tham "
        "chiếu là đồng thau (8,4 g cm⁻³) hoặc thép không gỉ (8,0 g cm⁻³), tương ứng ta có “khối lượng "
        "biểu kiến so với đồng thau” và “khối lượng biểu kiến so với thép không gỉ”. Loại sau được ưu "
        "tiên dùng khi báo cáo “khối lượng biểu kiến” của một vật."))
    b.append(p(
        "Báo cáo hiệu chuẩn của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST) báo cáo khối lượng "
        "theo ba cách: khối lượng thực, khối lượng biểu kiến so với đồng thau, và khối lượng biểu kiến so "
        "với thép không gỉ. Khối lượng quy ước được định nghĩa là khối lượng của một vật có khối lượng "
        "riêng 8,0 g cm⁻³, ở 20°C, trong không khí có khối lượng riêng 1,2 mg cm⁻³. Tuy nhiên, phần lớn "
        "các phép cân khoa học liên quan tới các vật liệu có khối lượng riêng khác 8,0 g cm⁻³. Điều này "
        "dẫn tới những sai số đo đáng kể."))
    b.append(p(
        "Ví dụ, xét trường hợp một nhà hóa học cân 1 lít nước. Trước tiên nhà hóa học cân một quả chuẩn "
        "khối lượng, một quả cân 1 kg làm bằng thép không gỉ; sau đó cân nước. Quả chuẩn 1 kg làm bằng "
        "thép không gỉ có khối lượng riêng 8,0 g cm⁻³ sẽ có thể tích 125 cm³. Cùng khối lượng đó của "
        "nước sẽ có thể tích xấp xỉ 1000 cm³ (thể tích = khối lượng/khối lượng riêng). Quả chuẩn sẽ "
        "chiếm chỗ 125 cm³ không khí, tạo ra lực đẩy 150 mg (125 cm³ × 1,2 mg cm⁻³). Tuy nhiên, nước sẽ "
        "chiếm chỗ 1000 cm³ không khí, tạo ra lực đẩy 1200 mg (1000 cm³ × 1,2 mg cm⁻³). Như vậy nhà hóa "
        "học đã đưa vào phép đo một sai số đáng kể do không tính tới khối lượng riêng khác nhau và lực "
        "đẩy của không khí."))
    b.append(p(
        "Dùng 1,2 mg cm⁻³ cho khối lượng riêng của không khí là phù hợp với các phép đo thực hiện gần "
        "mực nước biển; cần lưu ý rằng khối lượng riêng của không khí giảm theo độ cao. Ví dụ, khối lượng "
        "riêng của không khí ở Denver, Colorado, xấp xỉ 0,98 mg cm⁻³. Vì vậy, để có các phép đo khối "
        "lượng chính xác, phải đo khối lượng riêng của không khí tại thời điểm đo nếu muốn giảm các sai "
        "số môi trường trong phép đo."))
    b.append(p(
        "Khối lượng riêng của không khí có thể được tính tới một giá trị chấp nhận được bằng các phương "
        "trình sau:"))
    b.append(eq("ρ_A ≈ [ 0,0034848 / (t + 273,15) ] × ( P − 0,0037960 × U × e_s )", "20.5"))
    b.append(wl(["trong đó <b>ρ_A</b> = khối lượng riêng của không khí, tính bằng mg cm⁻³",
                 "<b>t</b> = nhiệt độ, tính bằng °C",
                 "<b>P</b> = áp suất khí quyển, tính bằng pascal",
                 "<b>U</b> = độ ẩm tương đối, tính bằng phần trăm",
                 "<b>e_s</b> = áp suất hơi bão hòa"]))
    b.append(eq("e_s ≈ 1,7526 × 10¹¹ × e^( −5315,56 / (t + 273,15) )", "20.6"))
    b.append(wl(["trong đó <b>e</b> ≈ 2,7182818 (cơ số logarit tự nhiên)",
                 "<b>t</b> = nhiệt độ, tính bằng °C"]))
    b.append(p(
        "Để áp dụng hiệu chính lực đẩy của không khí cho kỹ thuật thay thế đơn, dùng các công thức sau:"))
    b.append(eq("M_u = [ M_s (1 − ρ_A/ρ_s) + ((O₂ − O₁)/(O₃ − O₂)) × M_sw (1 − ρ_A/ρ_sw) ] "
                "/ (1 − ρ_A/ρ_u)", "20.7"))
    b.append(wl(["trong đó <b>M_u</b> = khối lượng của vật chưa biết (trong chân không)",
                 "<b>M_s</b> = khối lượng của quả chuẩn (trong chân không)",
                 "<b>M_sw</b> = khối lượng của quả cân độ nhạy",
                 "<b>ρ_A</b> = khối lượng riêng của không khí",
                 "<b>ρ_s</b> = khối lượng riêng của quả chuẩn",
                 "<b>ρ_u</b> = khối lượng riêng của vật chưa biết",
                 "<b>ρ_sw</b> = khối lượng riêng của quả cân độ nhạy",
                 "<b>O₁</b> = quan sát thứ nhất (quả chuẩn)",
                 "<b>O₂</b> = quan sát thứ hai (vật chưa biết)",
                 "<b>O₃</b> = quan sát thứ ba (vật chưa biết + SW)"]))
    b.append(eq("CM = M_u (1 − 0,0012/ρ_u) / 0,99985", "20.8"))
    b.append(wl(["trong đó <b>CM</b> = khối lượng quy ước",
                 "<b>M_u</b> = khối lượng của vật chưa biết trong chân không",
                 "<b>ρ_u</b> = khối lượng riêng của vật chưa biết"]))
    b.append(p(
        "Khi cần các phép đo rất chính xác, kỹ thuật thay thế kép (double substitution) kết hợp với hiệu "
        "chính lực đẩy của không khí sẽ cho kết quả chấp nhận được với gần như mọi ứng dụng khoa học. Kỹ "
        "thuật thay thế kép tương tự kỹ thuật thay thế đơn có dùng quả cân độ nhạy; điểm khác là trong "
        "kỹ thuật thay thế kép, quả cân độ nhạy được cân cùng với cả quả chuẩn và vật chưa biết. Ưu điểm "
        "chính của kỹ thuật này so với thay thế đơn là mọi sự trôi của thiết bị cân đều được tính đến. Vì "
        "độ chính xác của kỹ thuật cân này, chỉ nên dùng nó trên các cân chính xác hoặc thiết bị so sánh "
        "khối lượng. Như với thay thế đơn, đặt quả chuẩn lên đĩa cân và đọc lần thứ nhất; sau đó lấy quả "
        "chuẩn ra, đặt vật chưa biết lên đĩa cân và đọc lần thứ hai. Bước thứ ba là thêm quả cân độ nhạy "
        "nhỏ vào đĩa cùng với vật chưa biết và đọc lần thứ ba; sau đó lấy vật chưa biết ra, đưa quả chuẩn "
        "trở lại đĩa cùng với quả cân độ nhạy và đọc lần thứ tư. Khối lượng được tính theo công thức sau:"))
    b.append(eq("M_u = [ M_s (1 − ρ_A/ρ_s) + ½[(O₂ − O₁) + (O₄ − O₃)] × M_sw (1 − ρ_A/ρ_sw) "
                "/ (O₃ − O₂) ] / (1 − ρ_A/ρ_u)", "20.9"))
    b.append(wl(["trong đó <b>M_u</b> = khối lượng của vật chưa biết (trong chân không)",
                 "<b>M_s</b> = khối lượng của quả chuẩn (trong chân không)",
                 "<b>M_sw</b> = khối lượng của quả cân độ nhạy",
                 "<b>ρ_A</b> = khối lượng riêng của không khí",
                 "<b>ρ_s</b> = khối lượng riêng của quả chuẩn",
                 "<b>ρ_u</b> = khối lượng riêng của vật chưa biết",
                 "<b>ρ_sw</b> = khối lượng riêng của quả cân độ nhạy",
                 "<b>O₁</b> = quan sát thứ nhất (quả chuẩn)",
                 "<b>O₂</b> = quan sát thứ hai (vật chưa biết)",
                 "<b>O₃</b> = quan sát thứ ba (vật chưa biết + quả cân độ nhạy)",
                 "<b>O₄</b> = quan sát thứ tư (quả chuẩn + quả cân độ nhạy)"]))
    b.append(eq("CM = M_u (1 − 0,0012/ρ_u) / 0,99985", "20.10"))
    b.append(wl(["trong đó <b>CM</b> = khối lượng quy ước",
                 "<b>M_u</b> = khối lượng của vật chưa biết trong chân không",
                 "<b>ρ_u</b> = khối lượng riêng của vật chưa biết"]))
    b.append(p(
        "Để đạt được các mức chính xác cao nhất, người ta đã phát triển những sơ đồ cân tiên tiến. Các "
        "sơ đồ cân tiên tiến này kết hợp cân dư thừa (redundant weighing), bù trôi, kiểm tra thống kê và "
        "nhiều quả chuẩn. Sơ đồ đơn giản nhất trong số đó là sơ đồ ba-trong-một. Nó dùng hai quả chuẩn để "
        "hiệu chuẩn một quả cân chưa biết. Ở dạng đơn giản nhất, người ta thực hiện ba phép thay thế kép. "
        "Phép thứ nhất so sánh quả chuẩn thứ nhất với quả cân chưa biết; phép thay thế kép thứ hai so "
        "sánh quả chuẩn thứ nhất với quả chuẩn thứ hai, được gọi là quả chuẩn kiểm tra; và phép so sánh "
        "thứ ba, cũng là phép cuối cùng, so sánh quả chuẩn thứ hai (tức quả chuẩn kiểm tra) với quả cân "
        "chưa biết. Các phép so sánh này cho kết quả như sau:"))
    b.append('<p style="font-size:.92rem;color:#333;line-height:1.85;margin:-.3rem 0 1.2rem">'
             + "<br>".join([
                 "<b>O₁</b> = số đọc khi quả chuẩn ở trên cân",
                 "<b>O₂</b> = số đọc khi vật chưa biết ở trên cân",
                 "<b>O₃</b> = số đọc khi vật chưa biết và quả cân độ nhạy ở trên cân",
                 "<b>O₄</b> = số đọc khi quả chuẩn và quả cân độ nhạy ở trên cân",
                 "<b>O₅</b> = số đọc khi quả chuẩn ở trên cân",
                 "<b>O₆</b> = số đọc khi quả chuẩn kiểm tra ở trên cân",
                 "<b>O₇</b> = số đọc khi quả chuẩn kiểm tra và quả cân độ nhạy ở trên cân",
                 "<b>O₈</b> = số đọc khi quả chuẩn và quả cân độ nhạy ở trên cân",
                 "<b>O₉</b> = số đọc khi quả chuẩn kiểm tra ở trên cân",
                 "<b>O₁₀</b> = số đọc khi vật chưa biết ở trên cân",
                 "<b>O₁₁</b> = số đọc khi vật chưa biết và quả cân độ nhạy ở trên cân",
                 "<b>O₁₂</b> = số đọc khi quả chuẩn kiểm tra và quả cân độ nhạy ở trên cân",
             ]) + "</p>")
    b.append(p("Các chênh lệch đo được tính bằng các công thức sau:"))
    b.append(eq("a = ½[(O₁ − O₂) + (O₄ − O₃)] × M_sw / (O₃ − O₂) × (1 − ρ_A/ρ_sw)", "20.11"))
    b.append(eq("b = ½[(O₅ − O₆) + (O₈ − O₇)] × M_sw / (O₇ − O₆) × (1 − ρ_A/ρ_sw)", "20.12"))
    b.append(eq("c = ½[(O₉ − O₁₀) + (O₁₂ − O₁₁)] × M_sw / (O₁₁ − O₁₀) × (1 − ρ_A/ρ_sw)", "20.13"))
    b.append(wl(["trong đó <b>a</b> = chênh lệch giữa quả chuẩn và vật chưa biết",
                 "<b>b</b> = chênh lệch giữa quả chuẩn và quả chuẩn kiểm tra",
                 "<b>c</b> = chênh lệch giữa quả chuẩn kiểm tra và vật chưa biết",
                 "<b>M_sw</b> = khối lượng của quả cân độ nhạy",
                 "<b>ρ_A</b> = khối lượng riêng của không khí, tính theo phương trình 20.5 và 20.6",
                 "<b>ρ_sw</b> = khối lượng riêng của quả cân độ nhạy"]))
    b.append(p("Chênh lệch đo được theo bình phương tối thiểu của vật chưa biết được tính từ:"))
    b.append(eq("d_u = (2a − b − c) / 3", "20.14"))
    b.append(p(
        "Dùng chênh lệch đo được theo bình phương tối thiểu, khối lượng của vật chưa biết được tính như "
        "sau:"))
    b.append(eq("U = [ S (1 − ρ_A/ρ_S) + d_u ] / (1 − ρ_A/ρ_U)", "20.15"))
    b.append(wl(["trong đó <b>U</b> = khối lượng của vật chưa biết",
                 "<b>S</b> = khối lượng của quả chuẩn",
                 "<b>d_u</b> = chênh lệch đo được theo bình phương tối thiểu của vật chưa biết",
                 "<b>ρ_A</b> = khối lượng riêng của không khí, tính theo phương trình 20.5 và 20.6",
                 "<b>ρ_S</b> = khối lượng riêng của quả chuẩn",
                 "<b>ρ_U</b> = khối lượng riêng của vật chưa biết"]))
    b.append(p("Khối lượng quy ước của vật chưa biết nay được tính như sau:"))
    b.append(eq("C_U = U (1 − 0,0012/ρ_U) / 0,99985", "20.16"))
    b.append(wl(["trong đó <b>C_U</b> = khối lượng quy ước",
                 "<b>U</b> = khối lượng của vật chưa biết",
                 "<b>ρ_U</b> = khối lượng riêng của vật chưa biết"]))
    b.append(p(
        "Chênh lệch đo được theo bình phương tối thiểu nay được tính cho quả chuẩn kiểm tra:"))
    b.append(eq("d_CS = (2b − a − c) / 3", "20.17"))
    b.append(p(
        "Dùng chênh lệch đo được theo bình phương tối thiểu, khối lượng của quả chuẩn kiểm tra được tính "
        "từ:"))
    b.append(eq("CS = [ S (1 − ρ_A/ρ_S) + d_CS ] / (1 − ρ_A/ρ_CS)", "20.18"))
    b.append(wl(["trong đó <b>CS</b> = khối lượng của quả chuẩn kiểm tra",
                 "<b>S</b> = khối lượng của quả chuẩn",
                 "<b>d_CS</b> = chênh lệch đo được theo bình phương tối thiểu của quả chuẩn kiểm tra",
                 "<b>ρ_A</b> = khối lượng riêng của không khí, tính theo phương trình 20.5 và 20.6",
                 "<b>ρ_S</b> = khối lượng riêng của quả chuẩn",
                 "<b>ρ_CS</b> = khối lượng riêng của quả chuẩn kiểm tra"]))
    b.append(p(
        "Khối lượng của quả chuẩn kiểm tra phải nằm trong các giới hạn kiểm soát dành cho quả chuẩn kiểm "
        "tra. Nếu nằm ngoài các giới hạn kiểm soát, phép đo phải được lặp lại."))
    b.append(p("Độ lệch chuẩn ngắn hạn của quá trình nay được tính:"))
    b.append(eq("σ_ngắn hạn = 0,577 × | a − b + c |", "20.19"))
    b.append(p(
        "Độ lệch chuẩn ngắn hạn được chia cho độ lệch chuẩn ngắn hạn gộp (pooled) lịch sử để tính thống "
        "kê F:"))
    b.append(eq("F = độ lệch chuẩn ngắn hạn / độ lệch chuẩn ngắn hạn gộp lịch sử"))
    b.append(p(
        "Thống kê F phải nhỏ hơn giá trị thu được từ phân bố t (student) ở mức tin cậy 99% với số bậc tự "
        "do của độ lệch chuẩn gộp lịch sử. Nếu phép kiểm này không đạt, phép đo được coi là mất kiểm soát "
        "thống kê và phải được lặp lại."))
    b.append(p(
        "Bằng cách đo một quả chuẩn kiểm tra, tính độ lệch chuẩn ngắn hạn của quá trình và so sánh chúng "
        "với các kết quả lịch sử, người ta đạt được độ tin cậy cao đối với giá trị tính được của vật "
        "chưa biết."))
    b.append(p(
        "Có nhiều sơ đồ cân khác nhau và đều hợp lệ; sơ đồ ba-trong-một (ba quả cân bằng nhau) và sơ đồ "
        "bốn quả cân bằng nhau là những sơ đồ có thể tính toán dễ dàng mà không cần dùng máy tính. Các "
        "phòng hiệu chuẩn sơ cấp — cả tư nhân và nhà nước — đang dùng các phép so sánh chéo nhiều lần "
        "này, tức những phương pháp hiệu chuẩn khối lượng hiện đại nhất theo Chương trình Đảm bảo Đo "
        "lường Khối lượng (Mass Measurement Assurance Program), với chương trình máy tính Mass Code do "
        "Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ cung cấp. Thảo luận đầy đủ về các sơ đồ này có thể "
        "tìm thấy trong NBS Technical Note 952."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Các phương trình 20.11–20.19 được trình bày theo đúng dạng của "
        "bản gốc. Dấu của các chênh lệch a, b, c phụ thuộc quy ước lấy hiệu (chuẩn trừ vật, hay vật trừ "
        "chuẩn); chương trình Mass Code của NIST xử lý thống nhất quy ước này, nên khi tính toán thực tế "
        "cần lấy đúng quy ước của phần mềm. Ngoài ra, các công thức hiệu chính lực đẩy trong bản gốc được "
        "viết cho khối lượng tính bằng gam và khối lượng riêng của không khí tính bằng mg cm⁻³; cần đổi "
        "đơn vị nhất quán trước khi thay số."))

    # ---- references
    b.append(h2("Tài liệu tham khảo", "References"))
    refs = [
        "J. K. Taylor and H. V. Oppermann, <i>Handbook for the Quality Assurance of Metrological "
        "Measurements</i>, NBS Handbook 145, Washington, D.C.: U.S. Department of Commerce, National "
        "Bureau of Standards, 1986.",
        "L. V. Judson, <i>Weights and Measures Standards of the United States, A Brief History</i>, NBS "
        "Special Publication 447, Washington, D.C.: Department of Commerce, National Bureau of "
        "Standards, 1976.",
        "P. E. Pontius, <i>Mass and Mass Values</i>, NBS Monograph 133, Washington, D.C.: Department of "
        "Commerce, National Bureau of Standards, 1974.",
        "K. B. Jaeger and R. S. Davis, <i>A Primer for Mass Metrology</i>, NBS Special Publication 700-1, "
        "Washington, D.C.: Department of Commerce, National Bureau of Standards, 1984.",
        "J. M. Cameron, M. C. Croarkin, and R. C. Raybold, <i>Designs for the Calibration of Standards of "
        "Mass</i>, NBS Technical Note 952, Washington, D.C.: Department of Commerce, National Bureau of "
        "Standards, 1977.",
        "G. L. Harris (Ed.), <i>Selective Publications for the Advanced Mass Measurements Workshop</i>, "
        "NISTIR 4941, Washington, D.C.: Department of Commerce, National Institute of Standards and "
        "Technology, 1992.",
        "Metron Corporation, <i>Physical Measurements</i>, NAVAIR 17-35QAL-2, California: U.S. Navy, 1976.",
        "R. S. Cohen, <i>Physical Science</i>, New York: Holt, Rinehart and Winston, 1976.",
        "D. B. Prowse, <i>The Calibration of Balances</i>, CSIRO Division of Applied Physics, Australia, "
        "1995.",
        "E. Hazarian, Techniques of mass measurement, <i>Southern California Edison Mass Seminar "
        "Notebook</i>, Los Angeles, CA, 1994.",
        "E. Hazarian, Analysis of mechanical convertors of electronic balances, <i>Measurement Sci. "
        "Conf.</i>, Anaheim, CA, 1993.",
        "B. N. Taylor, <i>Guide for the use of the International System of Units (SI)</i>, NIST SP811, "
        "1995.",
    ]
    b.append('<ol class="refs">' + "".join("<li>%s</li>" % r for r in refs) + "</ol>")

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 19</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Mass and weight are often used interchangeably but are different. Mass is a quantitative measure "
        "of the inertia of a body at rest; as a physical quantity it is the product of density and volume. "
        "Weight, or weight force, is the force with which a body is attracted toward the Earth, and equals "
        "the product of mass and the acceleration of gravity."))
    b.append(p(
        "The embodiment of units of mass are called weights, which adds to the confusion. In SI the unit of "
        "mass is the kilogram and the unit of force is the newton; in U.S. customary units mass is the "
        "slug and force is the pound. Because the pound has been defined in terms of the kilogram since "
        "1893, Americans use the pound to designate mass."))
    b.append(h2("20.1 Weighing Instruments", "Thiết bị cân"))
    b.append(p(
        "Weighing is one of the oldest measurements, predating written history. The equal-arm balance — two "
        "pans suspended equidistant from a central pivot — was probably the first weighing instrument: the "
        "standard goes in one pan, the unknown in the other, and the beam is level when they are equal. "
        "Figure 20.1 shows an Ainsworth FV series equal-arm balance. A balance determines mass by measuring "
        "the force the object exerts on its support in the Earth's gravitational field, so S·G = U·G; "
        "because the pans are close together and the arms are equal, G cancels and the standard equals the "
        "unknown. Hence the need for a complete set of standards — the balance can only indicate equality, "
        "and only weakly how large a difference is."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "The single-pan substitution balance was probably the first attempt at direct reading: calibrated "
        "weights inside the balance are added to the standard side with dials and levers, and the small "
        "residual is read on an optical scale. The spring scale is the least expensive device: the "
        "elasticity of the spring is assumed linear, the extension force is marked in mass units, and "
        "capacity grows with spring stiffness — but resolution falls as stiffness rises, limiting spring "
        "scales to a few kilograms. Spiral and cantilevered springs are both used. The torsion balance is "
        "a precise adaptation: the vertical load produces a torque on a band, wire or string, and the "
        "angular deflection is proportional to the load, so a calibrated torsion constant lets the "
        "deflection be read as mass — down to the microgram region. The beam balance (Figure 20.2) uses "
        "the same principle but with one pan and an offset beam; sliding weights gain mechanical advantage "
        "as they move outward, and notched positions along the beam mark the force each weight applies. "
        "Beam balances span milligram range to truck and train scales, again with resolution falling as "
        "load rises."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Next in cost and accuracy is the strain gage load cell: a resistive wire element bonded to a steel "
        "cylinder changes resistance as the cylinder shortens or lengthens, and the resistance is "
        "converted to a mass readout by the readout electronics. The force restorative load cell (Figure "
        "20.3) is the heart of an electronic balance: the fulcrum is offset, one side carries a coil "
        "suspended in a magnetic field and the other side the pan; an LED/photodiode null detector senses "
        "departure from equilibrium and the coil current is increased until balance is restored. That "
        "current, measured across a precision sense resistor, becomes the displayed mass. Industrial "
        "scales, laboratory balances and mass comparators now use electromagnetic force compensation with "
        "joint flexures instead of knife edges — computer interfacing and no moving parts. Other methods "
        "include the vibrating cord (frequency proportional to tension), the piezoelectric effect, "
        "gyroscopic cells, capacitive and inductive converters whose reference distance changes with load, "
        "and radioactivity changes as a function of mass."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(h2("20.2 Weighing Techniques", "Kỹ thuật cân"))
    b.append(p(
        "For low accuracy, reading mass or weight directly from the instrument is adequate; except for "
        "equal-arm and some torsion balances, most modern instruments read directly. Errors come from "
        "instrument imperfections, bias in the standards, the weighing method, the operator and the "
        "environment. Mass is the only SI base quantity still defined by a physical artifact — the "
        "international prototype of the kilogram kept at Sèvres under the custody of the International "
        "Bureau of Weights and Measures — and its value has drifted over the past century by an unknown "
        "amount and direction."))
    b.append(p(
        "Substitution weighing removes most instrument errors. In single substitution a standard and an "
        "unknown are both weighed on the same device and only their difference is used: U = S + (O₂ − O₁) × "
        "SW/(O₃ − O₂). This is adequate to a few tenths of a gram; beyond that, air buoyancy dominates. "
        "True mass is the mass in vacuum; in air every object is lifted by a force equal to the weight of "
        "the displaced air, so apparent (conventional) mass is defined at 20 °C and 1.2 mg cm⁻³ with brass "
        "(8.4 g cm⁻³) or stainless steel (8.0 g cm⁻³) as reference. NIST reports true mass, apparent mass "
        "vs brass and apparent mass vs stainless steel. A chemist weighing 1 L of water illustrates the "
        "problem: a 1 kg stainless standard displaces 125 cm³ (150 mg of buoyancy) while the water "
        "displaces 1000 cm³ (1200 mg) — a significant uncorrected error. Air density falls with altitude "
        "(Denver ≈ 0.98 mg cm⁻³), so it must be measured; Equations 20.5 and 20.6 give ρ_A and e_s, "
        "Equations 20.7 and 20.8 give the single-substitution buoyancy correction and the conventional "
        "mass, and Equations 20.9 and 20.10 the double-substitution equivalents, which also absorb "
        "instrument drift."))
    b.append(p(
        "For the highest accuracy, advanced designs add redundant weighing, drift compensation, statistical "
        "checks and multiple standards. The simplest is the three-in-one design — two standards calibrate "
        "one unknown through three double substitutions (standard vs unknown, standard vs check standard, "
        "check standard vs unknown), giving twelve readings O₁…O₁₂. Equations 20.11–20.13 give the "
        "differences a, b, c; 20.14–20.16 the least-squares difference, mass and conventional mass of the "
        "unknown; 20.17–20.18 the same for the check standard, which must fall inside its control limits; "
        "and 20.19 the short-term standard deviation, whose ratio to the historical pooled value is the "
        "F-statistic, to be compared with the 99% t-value. Private and government primary calibration "
        "laboratories use these intercomparisons under the Mass Measurement Assurance Program with NIST's "
        "Mass Code; full discussion is in NBS Technical Note 952."))
    b.append(p("The chapter closes with 12 references, reproduced in the Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 19</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 20 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 20 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 20 “Đo khối lượng và trọng lượng” của Mark Fritz và Emil Hazarian "
            "(Denver Instrument Company) — phân biệt khối lượng và trọng lượng, các loại cân (tay đòn "
            "bằng nhau, thay thế, lò xo, xoắn, đòn, load cell biến trở lực căng, load cell hoàn lực), kỹ "
            "thuật cân thay thế đơn và kép, hiệu chính lực đẩy của không khí, khối lượng quy ước, và sơ "
            "đồ cân ba-trong-một với kiểm soát thống kê, với 3 hình và 19 phương trình." if vi else
            "Companion to Chapter 20 of the CRC Measurement Handbook — mass and weight measurement: "
            "balances and load cells, substitution weighing, air-buoyancy correction, conventional mass "
            "and the three-in-one weighing design.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 20' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 20' % BASE_EN)
    meta = ("Chương 20 · theo Ch20.pdf (CRC Press, 1999) · 3 hình, 19 phương trình, 12 tài liệu tham khảo" if vi
            else "Chapter 20 · 3 figures, 19 equations, 12 references")
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
