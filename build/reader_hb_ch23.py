# -*- coding: utf-8 -*-
"""Handbook Chapter 23 — Force Measurement
(M. A. Elbestawi, McMaster University).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch23.py
"""
import os

import hb23fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch23-force-measurement"
TITLE_EN = "Force Measurement"
TITLE_VI = "Đo lực"
BYLINE = "M. A. Elbestawi · McMaster University"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch22-strain-measurement"
PREV_VI = "ch22-strain-measurement"
PREV_T_EN = "Strain Measurement"
PREV_T_VI = "Đo biến dạng"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-23-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ol(items):
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
        "Lực, một đại lượng vectơ, có thể được định nghĩa là một tác động sẽ gây ra gia tốc hoặc một "
        "phản ứng nhất định của một vật. Chương này trình bày các phương pháp có thể dùng để xác định "
        "độ lớn của các lực đó."))

    b.append(h2("23.1 Những xem xét chung", "General Considerations"))
    b.append(p(
        "Việc xác định hay đo lực phải tuân theo những xem xét sau: nếu các lực tác dụng lên một vật "
        "không gây ra gia tốc nào, chúng phải hợp thành một hệ lực cân bằng. Hệ đó khi ấy được coi là ở "
        "trạng thái cân bằng tĩnh. Các lực mà một vật chịu được có thể chia thành hai loại: nội lực, "
        "khi các hạt riêng lẻ của vật tác dụng lên nhau, và ngoại lực trong trường hợp còn lại. Nếu một "
        "vật được các vật khác đỡ trong khi chịu tác dụng của lực, sẽ xuất hiện biến dạng và/hoặc dịch "
        "chuyển tại các điểm đỡ hoặc điểm tiếp xúc. Các nội lực sẽ phân bố khắp vật cho tới khi thiết "
        "lập được cân bằng, và khi đó vật được gọi là ở trạng thái kéo, nén hoặc trượt. Khi xét một vật "
        "tại một mặt cắt xác định, rõ ràng là mọi nội lực đều tác dụng thành cặp, hai lực bằng nhau và "
        "ngược chiều, trong khi ngoại lực tác dụng đơn lẻ."))

    b.append(h2("23.2 Định luật Hooke", "Hooke's Law"))
    b.append(p(
        "Cơ sở của việc đo lực bắt nguồn từ ứng xử vật lý của một vật dưới tác dụng của ngoại lực. Vì "
        "vậy, việc ôn lại ngắn gọn ứng xử cơ học của vật liệu là hữu ích. Khi một kim loại chịu tải kéo "
        "một trục, nén một trục hoặc trượt đơn (Hình 23.1), nó sẽ ứng xử đàn hồi cho tới khi ứng suất "
        "pháp (S) hoặc ứng suất tiếp (τ) đạt một giá trị tới hạn, sau đó nó biến dạng dẻo [1]. Trong "
        "miền đàn hồi, các nguyên tử bị dịch chuyển tạm thời nhưng trở về vị trí cân bằng khi bỏ tải. "
        "Ứng suất (S hoặc τ) và biến dạng (e hoặc γ) trong miền đàn hồi được định nghĩa như chỉ ra trên "
        "Hình 23.2."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Hệ số Poisson (ν) là tỉ số giữa biến dạng ngang (e₂) và biến dạng dọc (e₁) khi kéo hoặc nén. "
        "Trong miền đàn hồi, ν nằm trong khoảng 1/4 đến 1/3 đối với kim loại. Quan hệ giữa ứng suất và "
        "biến dạng trong miền đàn hồi được cho bởi định luật Hooke:"))
    b.append(eq("ν = − e₂ / e₁", "23.1"))
    b.append(eq("S = E · e &nbsp;&nbsp;(kéo hoặc nén)", "23.2"))
    b.append(eq("τ = G · γ &nbsp;&nbsp;(trượt đơn)", "23.3"))
    b.append(p(
        "trong đó E và G lần lượt là mô đun đàn hồi Young và mô đun đàn hồi trượt. Một thay đổi nhỏ của "
        "thể tích riêng (ΔVol/Vol) có thể liên hệ với biến dạng đàn hồi, và với một vật liệu đẳng hướng "
        "(cùng tính chất theo mọi phương) được biểu diễn như sau:"))
    b.append(eq("ΔVol / Vol = e (1 − 2ν)", "23.4"))
    b.append(p("Mô đun khối (K = nghịch đảo của độ nén được) được định nghĩa như sau:"))
    b.append(eq("K = − Δp / (ΔVol / Vol)", "23.5"))
    b.append(p(
        "trong đó Δp là áp suất tác dụng tại một điểm cụ thể. Với một chất rắn đàn hồi chịu nén một "
        "trục (S):"))
    b.append(eq("ΔVol / Vol = − (S / E) (1 − 2ν)", "23.6"))
    b.append(p(
        "Như vậy, một chất rắn đàn hồi là nén được chừng nào ν còn nhỏ hơn 1/2, điều thường đúng với kim "
        "loại. Định luật Hooke (phương trình 23.2) cho kéo một trục có thể được tổng quát hóa cho trạng "
        "thái đàn hồi ba chiều."))
    b.append(p(
        "Lý thuyết đàn hồi đã được thiết lập vững chắc và được dùng làm cơ sở cho các kỹ thuật đo lực. "
        "Lưu ý rằng việc đo lực trong các ứng dụng kỹ thuật khác nhau rất đặc thù cho từng ứng dụng, và "
        "cần thận trọng khi chọn các kỹ thuật đo nêu dưới đây."))

    b.append(h3("Các phương pháp cơ bản để đo lực", "Basic Methods of Force Measurement"))
    b.append(p("Một lực chưa biết có thể được đo bằng các cách sau:"))
    b.append(ol([
        "Cân bằng lực chưa biết với một khối lượng chuẩn thông qua một hệ đòn bẩy.",
        "Đo gia tốc của một khối lượng đã biết.",
        "Cân bằng nó với một lực từ sinh ra do tương tác giữa một cuộn dây mang dòng điện và một nam "
        "châm.",
        "Phân bố lực trên một diện tích xác định để tạo ra áp suất, rồi đo áp suất đó.",
        "Chuyển lực tác dụng thành biến dạng của một phần tử đàn hồi.",
    ]))
    b.append(p(
        "Các phương pháp nêu trên để đo lực dẫn tới nhiều kiểu thiết kế thiết bị đo khác nhau. Thách "
        "thức của việc đo lực chủ yếu nằm ở thiết kế cảm biến. Những điều cơ bản của thiết kế cảm biến "
        "có thể quy về hai bài toán:"))
    b.append(ol([
        "Các ràng buộc hình học hoặc vật lý sơ cấp, do ứng dụng của thiết bị cảm biến lực quy định.",
        "Cách thức chuyển lực thành một dạng tín hiệu khả dụng (chẳng hạn tín hiệu điện tử hoặc dịch "
        "chuyển chia độ).",
    ]))
    b.append(p(
        "Các mục còn lại sẽ thảo luận các loại thiết bị dùng để chuyển lực thành tín hiệu, và cuối cùng "
        "minh họa một số ví dụ ứng dụng các thiết bị này để đo lực."))

    b.append(h2("23.3 Cảm biến lực", "Force Sensors"))
    b.append(p(
        "Cảm biến lực là cần thiết để hiểu một cách cơ bản về đáp ứng của một hệ. Ví dụ, lực cắt sinh ra "
        "trong một quá trình gia công có thể được theo dõi để phát hiện hỏng dụng cụ, hoặc để chẩn đoán "
        "nguyên nhân hỏng khi điều khiển các thông số quá trình, và để đánh giá chất lượng bề mặt tạo "
        "ra. Cảm biến lực được dùng để theo dõi lực va đập trong công nghiệp ô tô. Các nhiệm vụ thao tác "
        "và lắp ráp bằng robot được điều khiển bằng cách phát hiện các lực sinh ra tại cơ cấu tác động "
        "cuối. Đo lực trực tiếp hữu ích trong việc điều khiển nhiều hệ cơ khí."))
    b.append(p(
        "Một số loại cảm biến lực dựa trên việc đo độ võng do lực gây ra. Kỹ thuật này cần độ võng tương "
        "đối lớn (thường vài micromet) mới khả thi. Tính chất đàn hồi tuyệt vời của lò xo xoắn ốc khiến "
        "chúng có thể được dùng thành công làm cảm biến lực, biến tải cần đo thành độ võng. Quan hệ giữa "
        "lực và độ võng trong miền đàn hồi được thể hiện bằng định luật Hooke. Các cảm biến lực dùng "
        "phần tử gage biến dạng hoặc tinh thể áp điện (thạch anh) tích hợp vi điện tử là phổ biến. Cả "
        "lực xung và lực biến đổi chậm đều có thể được theo dõi bằng các cảm biến này."))
    b.append(p(
        "Trong các kỹ thuật đo lực hiện có, có thể định nghĩa một nhóm con tổng quát là load cell. Load "
        "cell nói chung gồm một kết cấu ngoài cứng vững, một môi trường dùng để đo lực tác dụng, và "
        "gage đo. Load cell được dùng để cảm nhận các lực lớn, tĩnh hoặc biến đổi chậm với độ võng nhỏ, "
        "và là phương tiện cảm nhận lực tương đối chính xác. Độ chính xác điển hình vào cỡ 0,1% giá trị "
        "đọc toàn thang. Có thể dùng nhiều chiến lược khác nhau để đo lực, phụ thuộc mạnh vào thiết kế "
        "load cell. Ví dụ, Hình 23.3 minh họa các loại load cell khác nhau có thể dùng để cảm nhận lực "
        "lớn với chi phí tương đối thấp. Load cell thủy lực dùng một kết cấu ngoài rất cứng với một "
        "khoang bên trong chứa đầy chất lỏng. Khi đặt tải, áp suất dầu tăng lên và có thể đọc trên một "
        "đồng hồ chính xác."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Các kỹ thuật cảm nhận khác cũng có thể được dùng để theo dõi lực, như đầu đo áp điện cho đáp "
        "ứng nhanh hơn với tải biến đổi, phương pháp khí nén, gage biến dạng, v.v. Kỹ thuật cảm nhận phù "
        "hợp cần được xem xét đặc biệt dựa trên các điều kiện yêu cầu để theo dõi."))

    b.append(h3("Load cell gage biến dạng", "Strain Gage Load Cell"))
    b.append(p(
        "Load cell gage biến dạng gồm một kết cấu biến dạng đàn hồi khi chịu lực và một mạng gage biến "
        "dạng tạo ra tín hiệu điện tỉ lệ với biến dạng đó. Ví dụ là các load cell kiểu dầm và kiểu vòng."))

    b.append(h4("Gage biến dạng", "Strain Gages"))
    b.append(p(
        "Gage biến dạng dùng một đoạn dây gage để tạo ra điện trở mong muốn (thường khoảng 120 Ω) dưới "
        "dạng một cuộn phẳng. Cuộn này sau đó được gắn (dán) giữa hai tấm cách điện mỏng bằng giấy hoặc "
        "nhựa. Gage như vậy không thể dùng trực tiếp để đo độ võng. Trước hết nó phải được gắn đúng cách "
        "lên một chi tiết cần đo biến dạng. Sau khi dán gage lên chi tiết, chúng được sấy ở khoảng 195°F "
        "(90°C) để loại ẩm. Phủ lớp sáp hoặc nhựa lên cụm sẽ bảo vệ cơ học phần nào. Điện trở giữa chi "
        "tiết thử và bản thân gage phải ít nhất 50 MΩ. Tổng diện tích của tất cả các dây dẫn phải giữ "
        "nhỏ để keo có thể dễ dàng truyền lực cần thiết làm biến dạng dây. Khi chi tiết chịu ứng suất, "
        "biến dạng sinh ra làm biến dạng gage và diện tích mặt cắt ngang của nó giảm đi. Điều này làm "
        "tăng điện trở suất của gage và dễ dàng xác định được. Để đo các biến dạng rất nhỏ, cần đo những "
        "thay đổi nhỏ của điện trở trên một đơn vị điện trở (ΔR/R). Thay đổi điện trở của một gage dán "
        "thường nhỏ hơn 0,5%. Có nhiều kích cỡ gage và hình dạng lưới khác nhau, và các ví dụ điển hình "
        "được chỉ ra trên Hình 23.4."))
    b.append(p(
        "Việc dùng gage biến dạng để đo lực đòi hỏi xem xét cẩn thận về độ cứng vững và môi trường. Do "
        "thiết kế của chúng, các gage biến dạng có chiều dài ngắn hơn nói chung có tần số đáp ứng cao "
        "hơn (ví dụ: 660 kHz với gage dài 0,2 mm và 20 kHz với gage dài 60 mm). Các xem xét về môi "
        "trường tập trung chủ yếu vào nhiệt độ của gage. Ai cũng biết rằng điện trở là một hàm của nhiệt "
        "độ, và do đó gage biến dạng nhạy với sự thay đổi nhiệt độ. Vì vậy, nếu biết rằng nhiệt độ của "
        "gage sẽ thay đổi do bất kỳ ảnh hưởng nào, cần bù nhiệt độ để bảo đảm phép đo lực chính xác."))
    b.append(p(
        "Cầu Wheatstone (Hình 23.5) thường được dùng để đo bậc độ lớn nhỏ này. Trên Hình 23.5, không có "
        "dòng điện chạy qua điện kế (G) nếu bốn điện trở thỏa mãn một điều kiện nhất định. Để minh họa "
        "cách cầu Wheatstone hoạt động [3], một thang điện áp đã được vẽ tại các điểm C và D của Hình "
        "23.5. Giả sử R₁ là một gage dán và ban đầu phương trình 23.7 được thỏa mãn. Nếu bây giờ R₁ bị "
        "kéo giãn sao cho điện trở của nó tăng thêm một đơn vị (+ΔR), điện áp tại điểm D sẽ tăng từ 0 "
        "lên cộng một đơn vị điện áp (+ΔV), và sẽ có một hiệu điện áp một đơn vị giữa C và D, gây ra "
        "dòng điện chạy qua C. Nếu R₄ cũng là một gage dán, và cùng lúc R₁ thay đổi +ΔR thì R₄ thay đổi "
        "−ΔR, điện áp tại D sẽ chuyển tới +2ΔV. Ngoài ra, nếu cùng lúc đó R₂ thay đổi −ΔR và R₃ thay đổi "
        "+ΔR, thì điện áp tại điểm C sẽ chuyển tới −2ΔV, và hiệu điện áp giữa C và D lúc này sẽ là "
        "4ΔV. Rõ ràng là mặc dù có thể dùng một gage duy nhất, độ nhạy có thể tăng gấp bốn lần nếu hai "
        "gage được dùng ở trạng thái kéo trong khi hai gage khác ở trạng thái nén."))
    b.append(eq("R₁ / R₄ = R₂ / R₃", "23.7"))
    b.append(p(
        "Cấu hình lưới của gage biến dạng điện trở lá kim loại được tạo bằng quá trình khắc quang. Gage "
        "ngắn nhất hiện có là 0,20 mm; dài nhất là 102 mm. Điện trở gage tiêu chuẩn là 120 Ω và 350 Ω. "
        "Một gage biến dạng có thay đổi điện trở ΔR/R liên hệ với biến dạng theo phương của các đường "
        "lưới bằng biểu thức trong phương trình 23.8, trong đó S_g là hệ số gage hay hằng số hiệu chuẩn "
        "của gage."))
    b.append(eq("ΔR / R = S_g · ε", "23.8"))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(fig(5, F.fig(5), "vi"))

    b.append(h4("Load cell kiểu dầm", "Beam-Type Load Cell"))
    b.append(p(
        "Load cell kiểu dầm thường được dùng để đo các tải nhỏ [3]. Một dầm công xôn đơn giản (xem Hình "
        "23.6(a)) với bốn gage biến dạng, hai trên mặt trên và hai trên mặt dưới (đều định hướng dọc "
        "theo trục dầm), được dùng làm phần tử đàn hồi (cảm biến) cho load cell. Các gage được đấu vào "
        "một cầu Wheatstone như trên Hình 23.6(b). Tải P tạo ra một mômen M = Px tại vị trí gage (x), "
        "dẫn tới các biến dạng sau:"))
    b.append(eq("ε₁ = − ε₂ = ε₃ = − ε₄ = M / (Ebh²/6) = Px / (Ebh²/6)", "23.9"))
    b.append(p(
        "trong đó b là chiều rộng mặt cắt ngang của dầm và h là chiều cao mặt cắt ngang của dầm. Như "
        "vậy, đáp ứng của các gage biến dạng thu được từ phương trình 23.10."))
    b.append(eq("ΔR₁/R₁ = − ΔR₂/R₂ = ΔR₃/R₃ = − ΔR₄/R₄ = S_g · 6Px / (Ebh²)", "23.10"))
    b.append(p(
        "Điện áp ra E_o từ cầu Wheatstone, do tác dụng của tải P, thu được từ phương trình 23.11. Nếu "
        "giả thiết bốn gage biến dạng trên dầm là giống hệt nhau, thì phương trình 23.11 đúng."))
    b.append(eq("E_o = 6 · S_g · P · x · E_i / (E · b · h²)", "23.11"))
    b.append(p(
        "Dải đo và độ nhạy của một load cell kiểu dầm phụ thuộc vào hình dạng mặt cắt ngang của dầm, vị "
        "trí điểm đặt tải, và độ bền mỏi của vật liệu làm dầm."))
    b.append(fig(6, F.fig(6), "vi"))

    b.append(h4("Load cell kiểu vòng", "Ring-Type Load Cell"))
    b.append(p(
        "Load cell kiểu vòng dùng một vòng đo (proving ring) (xem Hình 23.7) làm phần tử đàn hồi. Phần "
        "tử vòng có thể được thiết kế để bao một dải tải rất rộng bằng cách thay đổi đường kính D, chiều "
        "dày t, hoặc chiều sâu w của vòng. Có thể dùng gage biến dạng hoặc một biến áp vi sai biến thiên "
        "tuyến tính (LVDT) làm cảm biến."))
    b.append(p(
        "Tải P tỉ lệ tuyến tính với điện áp ra E_o. Độ nhạy của load cell kiểu vòng với cảm biến LVDT "
        "phụ thuộc vào hình học của vòng (R, t và w), vật liệu làm vòng (E), và đặc tính của LVDT (S và "
        "E_i). Dải đo của một load cell kiểu vòng được quyết định bởi độ bền của vật liệu dùng làm "
        "vòng."))
    b.append(fig(7, F.fig(7), "vi"))

    b.append(h3("Phương pháp áp điện", "Piezoelectric Methods"))
    b.append(p(
        "Một vật liệu áp điện thể hiện hiện tượng gọi là hiệu ứng áp điện. Hiệu ứng này phát biểu rằng "
        "khi các tinh thể đàn hồi không đối xứng bị biến dạng bởi một lực, một điện thế sẽ được tạo ra "
        "trong mạng tinh thể bị méo. Hiệu ứng này là thuận nghịch. Nghĩa là, nếu đặt một điện thế giữa "
        "các mặt của tinh thể, nó sẽ thay đổi kích thước vật lý của mình [4]. Các phần tử thể hiện tính "
        "chất áp điện đôi khi được gọi là phần tử điện hẹp (electrorestrictive)."))
    b.append(p(
        "Độ lớn và cực tính của các điện tích bề mặt cảm ứng tỉ lệ với độ lớn và chiều của lực tác dụng "
        "[4]:"))
    b.append(eq("Q = d · F", "23.12"))
    b.append(p(
        "trong đó d là độ nhạy điện tích (một hằng số với một tinh thể cho trước) của tinh thể, tính "
        "bằng C/N. Lực F gây ra một thay đổi chiều dày Δt mét của tinh thể:"))
    b.append(eq("Δt = F / (a · Y)", "23.13"))
    b.append(p("trong đó a là diện tích tinh thể, t là chiều dày tinh thể, và Y là mô đun Young."))
    b.append(eq("Y = ứng suất / biến dạng = (F/a) / (Δt/t) = F · t / (a · Δt)", "23.14"))
    b.append(p(
        "Điện tích tại các điện cực tạo ra một điện áp E₀ = Q/C, trong đó C là điện dung tính bằng fara "
        "giữa các điện cực và C = εa/t, với ε là hằng số điện môi tuyệt đối."))
    b.append(eq("E_o = dF / C = d · t · F / (ε · a)", "23.15"))
    b.append(p(
        "Độ nhạy điện áp g = d/ε, tính bằng vôn mét trên niutơn, có thể thu được như sau:"))
    b.append(eq("E_o = g · t · F / a = g · t · P", "23.16"))
    b.append(p(
        "Các vật liệu áp điện được dùng là thạch anh, tourmaline, muối Rochelle, amoni dihydro photphat "
        "(ADP), lithi sulfat, bari titanat, và chì zirconat titanat (PZT) [4]. Thạch anh và các tinh "
        "thể áp điện tự nhiên khác phân cực tự nhiên. Tuy nhiên, các vật liệu áp điện tổng hợp, như gốm "
        "bari titanat, được chế tạo bằng cách nung các tinh thể nhỏ dưới áp suất rồi đặt vật liệu thu "
        "được vào một điện trường một chiều mạnh [4]. Sau đó, tinh thể được phân cực dọc theo trục mà "
        "lực sẽ tác dụng, để thể hiện tính chất áp điện. Các phần tử áp điện nhân tạo không bị hạn chế "
        "bởi cấu trúc tinh thể và có thể được đúc thành bất kỳ kích thước và hình dạng nào. Hướng phân "
        "cực được chỉ định trong quá trình sản xuất chúng."))
    b.append(p(
        "Các chế độ hoạt động khác nhau của một thiết bị áp điện dạng bản phẳng được chỉ ra trên Hình "
        "23.8 [4]. Bằng cách dán hai tinh thể với nhau sao cho các trục điện của chúng vuông góc, có "
        "thể đặt mômen uốn hoặc mômen xoắn lên đầu đo áp điện và tạo ra một điện áp ra (Hình 23.9) [4]. "
        "Dải lực có thể đo bằng đầu đo áp điện là từ 1 đến 200 kN, với tỉ số 2 × 10⁵."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản gốc viết “with a ratio of 2 × 10⁵” mà không nói rõ là tỉ số "
        "nào; theo ngữ cảnh đây là tỉ số giữa lực lớn nhất và lực nhỏ nhất trong dải đo động, tức dải "
        "động của đầu đo. Ngoài ra Hình 23.8 trong bản gốc chỉ ghi “các chế độ hoạt động” mà không nêu "
        "ký hiệu; ba chế độ được vẽ lại ở đây theo đúng ba hệ số liên kết áp điện của một bản phẳng: d₃₃ "
        "(nén dọc trục phân cực), d₃₁ (nén ngang trục phân cực) và d₁₅ (trượt trên mặt bản)."))
    b.append(p(
        "Tinh thể áp điện cũng có thể được dùng để đo sự thay đổi tức thời của lực (lực động). Một bản "
        "thạch anh mỏng có thể được dùng làm bộ dao động điện tử. Tần số của các dao động này sẽ bị chi "
        "phối bởi tần số riêng của bản mỏng. Bất kỳ méo dạng nào của bản do một ngoại lực gây ra đều "
        "làm thay đổi tần số dao động. Do đó, có thể đo một lực động bằng sự thay đổi tần số của bộ "
        "dao động."))

    b.append(h3("Phương pháp điện trở", "Resistive Method"))
    b.append(p(
        "Phương pháp điện trở dựa trên thực tế là khi diện tích tiếp xúc bội giữa các hạt bán dẫn (thường "
        "là cacbon) và khoảng cách giữa các hạt thay đổi, tổng điện trở cũng thay đổi. Thiết kế các đầu "
        "đo như vậy tạo ra dịch chuyển rất nhỏ khi đặt lực. Một đầu đo có thể gồm 2 đến 60 đĩa cacbon "
        "mỏng gắn giữa một điện cực cố định và một điện cực di động. Khi đặt lực lên điện cực di động và "
        "các đĩa cacbon xích lại gần nhau 5 đến 250 µm mỗi mặt tiếp xúc, hàm truyền của điện trở theo "
        "lực tác dụng gần như hyperbol, nghĩa là rất phi tuyến. Thiết bị cũng bị trễ lớn và trôi, cùng "
        "với độ nhạy ngang cao."))
    b.append(p(
        "Để giảm trễ và trôi, người ta dùng vòng thay cho đĩa. Các vòng được gắn trên một lõi cứng cách "
        "điện và được tạo ứng suất trước. Điều này gần như loại bỏ hoàn toàn sai số do độ nhạy ngang. "
        "Tần số riêng của lõi cao và có thể lên tới 10 kHz. Dải đo khả dĩ của một đầu đo như vậy là từ "
        "0,1 kg đến 10 kg. Độ chính xác và độ nhạy tuyến tính của đầu đo này rất kém."))

    b.append(h3("Phương pháp cảm ứng", "Inductive Method"))
    b.append(p(
        "Phương pháp cảm ứng dựa trên thực tế là sự thay đổi ứng suất cơ học của một vật liệu sắt từ làm "
        "độ từ thẩm của nó thay đổi. Các thay đổi từ thông được chuyển thành điện áp cảm ứng trong các "
        "cuộn thu khi có chuyển động. Hiện tượng này được gọi là hiệu ứng Villari hay từ giảo. Nó được "
        "biết là đặc biệt mạnh trong các hợp kim niken–sắt."))
    b.append(p(
        "Các đầu đo dùng hiệu ứng Villari gồm một cuộn dây quấn trên một lõi vật liệu từ giảo. Lực cần "
        "đo được đặt lên lõi này, tạo ứng suất và làm thay đổi độ từ thẩm và độ tự cảm của lõi. Sự thay "
        "đổi này có thể được theo dõi và dùng để xác định lực."))
    b.append(p(
        "Dải áp dụng của loại đầu đo này là một hàm của diện tích mặt cắt ngang của lõi. Độ chính xác "
        "của thiết bị được quyết định bởi quá trình hiệu chuẩn. Đầu đo này có độ tuyến tính kém và bị "
        "trễ. Độ từ thẩm của một vật liệu từ giảo tăng khi nó chịu xoắn thuần, bất kể chiều. Đáp ứng "
        "tần số phẳng thu được trên một dải rộng từ 150 Hz đến 15.000 Hz."))

    b.append(h3("Phương pháp piezotransistor", "Piezotransistor Method"))
    b.append(p(
        "Các thiết bị dùng hiệu ứng ứng suất dị hướng được gọi là piezotransistor. Trong hiệu ứng này, "
        "nếu mặt trên của một điốt p–n chịu ứng suất cục bộ, sẽ xảy ra một thay đổi thuận nghịch đáng "
        "kể của dòng điện chạy qua tiếp giáp. Các transistor này thường là loại silic phi phẳng, với một "
        "tiếp giáp phát–gốc. Tiếp giáp này được nối cơ học với một màng đặt trên mặt trên của một vỏ "
        "kim loại kiểu TO điển hình [4]. Khi đặt áp suất hoặc lực lên màng, một điện tích được tạo ra. "
        "Nên dùng các thiết bị đo lực này ở nhiệt độ không đổi, vì vật liệu bán dẫn cũng thay đổi tính "
        "chất điện theo nhiệt độ. Đặc tính hấp dẫn của piezotransistor là chúng chịu được quá tải 500%."))

    b.append(h3("Dynamometer đa thành phần dùng tinh thể thạch anh làm phần tử cảm nhận",
                "Multicomponent Dynamometers Using Quartz Crystals"))

    b.append(h4("Hiệu ứng áp điện trong thạch anh", "The Piezoelectric Effects in Quartz"))
    b.append(p(
        "Đối với đo lực, hiệu ứng áp điện trực tiếp được sử dụng. Hiệu ứng dọc trực tiếp đo lực nén; "
        "hiệu ứng trượt trực tiếp đo lực trượt theo một phương. Ví dụ, nếu một đĩa thạch anh tinh thể "
        "(SiO₂) cắt vuông góc với trục tinh thể học x chịu một lực nén, nó sẽ tạo ra một điện tích, "
        "danh định 2,26 pC/N. Nếu một đĩa thạch anh tinh thể được cắt vuông góc với trục tinh thể học y, "
        "nó sẽ tạo ra một điện tích (4,52 pC/N) nếu chịu lực trượt theo một phương cụ thể. Các lực đặt "
        "theo các phương khác sẽ không tạo ra tín hiệu nào [5]."))
    b.append(p(
        "Một bộ khuếch đại điện tích được dùng để chuyển điện tích do phần tử tinh thể thạch anh tạo ra "
        "thành một điện áp tỉ lệ. Dải của bộ khuếch đại điện tích theo hệ số chuyển đổi của nó được "
        "quyết định bởi một tụ hồi tiếp. Việc điều chỉnh về đơn vị cơ học được thực hiện bằng các bộ "
        "khuếch đại thuật toán bổ sung có độ lợi biến đổi."))

    b.append(h4("Thiết kế dynamometer đa thành phần dùng thạch anh",
                "The Design of Quartz Multicomponent Dynamometers"))
    b.append(p(
        "Phần tử chính để thiết kế dynamometer đa thành phần là đầu đo lực ba thành phần (Hình 23.10). "
        "Nó chứa một cặp đĩa thạch anh cắt X cho thành phần lực pháp tuyến và một cặp đĩa thạch anh cắt "
        "Y (nhạy trượt) cho mỗi thành phần lực trượt."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Dynamometer ba thành phần có thể được dùng để đo lực cắt trong quá trình gia công. Bốn đầu đo "
        "lực ba thành phần được kẹp giữa một bản đế và một bản trên được chỉ ra trên Hình 23.10. Đầu đo "
        "lực chịu một tải trước vì lực trượt được truyền qua ma sát. Bốn đầu đo lực chịu sự thay đổi "
        "mạnh của tải, phụ thuộc vào loại và vị trí đặt lực. Việc đưa lực vào theo kiểu nhô ra tạo ra "
        "lực kéo cho một số đầu đo, do đó làm giảm tải trước. Uốn của bản trên dynamometer gây ra ứng "
        "suất uốn và ứng suất trượt. Dải đo của một dynamometer không chỉ phụ thuộc vào các lực riêng "
        "lẻ mà còn phụ thuộc vào các ứng suất uốn riêng lẻ."))

    b.append(h4("Đo tín hiệu truyền bằng telemetry", "Measuring Signals Transmitted by Telemetry"))
    b.append(p(
        "Hình 23.11 chỉ ra hệ đo lực mới được thiết kế RCD (dynamometer lực cắt quay). Một cảm biến "
        "hình vành khuyên (1) được lắp trong một ổ côn góc dốc (2) và một vòng đế (3), cho phép cảm nhận "
        "ba thành phần lực Fx, Fy và Fz tại lưỡi cắt cũng như mômen Mz. Nguyên lý hoạt động vật lý của "
        "ô đo này dựa trên hiệu ứng áp điện trong các bản thạch anh. Các bản thạch anh trong cảm biến "
        "được căn chỉnh sao cho độ nhạy chéo cực đại giữa các thành phần lực là 1%. Do thiết kế cứng "
        "vững của cảm biến, tần số riêng của hệ đo lực nằm trong khoảng 1200 Hz đến 3000 Hz và dải đo "
        "bao tối đa 10 kN [6]."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(p(
        "Các điện tích tỉ lệ với lực sinh ra trên bề mặt các bản thạch anh được chuyển thành điện áp "
        "bởi bốn bộ khuếch đại điện tích thu nhỏ (7) kiểu lai. Các tín hiệu này sau đó được lọc bằng "
        "mạch điện chuyên dụng để tránh hiệu ứng chồng phổ, và được số hóa với độ phân giải 8 bit dùng "
        "tốc độ lấy mẫu cao (điều chế mã xung). Các tín hiệu số được truyền bằng một đơn vị telemetry "
        "gồm một môđun thu và phát, một ăng ten trên đỉnh hệ đo lực quay (8), cũng như một ăng ten cố "
        "định (9) trên vỏ chắn của đầu phay hai trục (10). Các linh kiện điện, bộ khuếch đại điện tích "
        "và môđun phát được gắn trên chu vi của hệ đo lực [6]."))
    b.append(p(
        "Lực cắt và mômen đo được số hóa bằng hệ đo lực mô tả ở trên. Chúng được điều chế trên một sóng "
        "mang FM và được truyền từ bộ phát quay tới bộ thu cố định. Các tín hiệu được truyền đi được đưa "
        "tới một bộ điều kiện biến đo bên ngoài."))

    b.append(h4("Đo lực động", "Measuring Dynamic Forces"))
    b.append(p(
        "Mọi hệ cơ khí có thể được coi, ở mức gần đúng đầu tiên, như một bộ dao động tắt yếu gồm một lò "
        "xo và một khối lượng. Nếu một hệ cơ khí có nhiều hơn một tần số riêng, phải xét tần số thấp "
        "nhất. Chừng nào tần số thử còn dưới 10% tần số riêng của đầu đo chuẩn (dùng để hiệu chuẩn), sai "
        "khác giữa độ nhạy động thu được và độ nhạy từ hiệu chuẩn tĩnh sẽ nhỏ hơn 1%. Các xem xét trên "
        "giả thiết tín hiệu lực hình sin. Việc hiệu chuẩn tĩnh một đầu đo chuẩn cũng có giá trị cho mục "
        "đích hiệu chuẩn động nếu tần số thử thấp hơn nhiều (ít nhất 10 lần) so với tần số riêng của "
        "hệ."))

    b.append(h3("Đầu đo lực kiểu điện dung", "Capacitive Force Transducer"))
    b.append(p(
        "Một đầu đo dùng biến thiên điện dung có thể được dùng để đo lực. Lực được hướng lên một màng "
        "mà độ võng đàn hồi của nó được phát hiện bằng biến thiên điện dung. Có thể chế tạo một đầu đo "
        "lực rất nhạy vì đầu đo điện dung cảm nhận chính xác các độ võng rất nhỏ. Một mạch điện tử "
        "chuyển các biến thiên điện dung thành biến thiên điện áp một chiều [7]."))
    b.append(p(
        "Cảm biến điện dung minh họa trên Hình 23.12 gồm hai bản kim loại cách nhau một khe không khí. "
        "Điện dung C giữa các cực được cho bởi biểu thức:"))
    b.append(eq("C = ε₀ · ε_r · A / h", "23.17"))
    b.append(wl([
        "C = điện dung, tính bằng fara (F)",
        "ε₀ = hằng số điện môi của chân không",
        "ε_r = hằng số điện môi tương đối của chất cách điện",
        "A = diện tích chồng lấn của hai bản",
        "h = chiều dày khe giữa hai bản",
    ]))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Trong bản gốc, Hình 23.12 được in kèm dòng “Photo not available” "
        "(không có ảnh). Hình ở đây được vẽ lại theo đúng mô tả trong phần chữ: hai bản kim loại song "
        "song, một màng đàn hồi chịu lực, khe không khí dày h và diện tích chồng lấn A."))
    b.append(p(
        "Độ nhạy của cảm biến kiểu điện dung vốn thấp. Về lý thuyết, giảm khe h sẽ làm tăng độ nhạy; "
        "tuy nhiên có những điều kiện điện và cơ thực tế ngăn cản việc đạt độ nhạy cao. Một ưu điểm "
        "chính của đầu đo điện dung là việc dịch chuyển một bản so với bản kia chỉ cần một lực cực nhỏ. "
        "Ưu điểm thứ hai là độ ổn định, và độ nhạy của cảm biến không bị ảnh hưởng bởi áp suất hay "
        "nhiệt độ của môi trường."))

    b.append(h3("Điện trở cảm nhận lực (polymer dẫn điện)",
                "Force Sensing Resistors (Conductive Polymers)"))
    b.append(p(
        "Điện trở cảm nhận lực (FSR) dựa trên thực tế là một số thiết bị màng dày polymer có điện trở "
        "giảm khi lực tác dụng tăng. Một điện trở cảm nhận lực gồm hai phần. Phần thứ nhất là một vật "
        "liệu điện trở phủ lên một màng. Phần thứ hai là một bộ tiếp điểm đan răng lược phủ lên một "
        "màng khác. Hình 23.13 chỉ ra cấu hình này. Vật liệu điện trở hoàn thành mạch điện giữa hai bộ "
        "dây dẫn trên màng kia. Khi đặt lực lên cảm biến này, tiếp xúc giữa các tiếp điểm trở nên tốt "
        "hơn; do đó độ dẫn điện tăng. Trên một dải lực rộng, hóa ra độ dẫn điện gần như là một hàm "
        "tuyến tính của lực. Hình 23.14 chỉ ra điện trở của cảm biến như một hàm của lực. Cần lưu ý "
        "rằng có ba vùng khả dĩ để cảm biến hoạt động. Bước chuyển đột ngột đầu tiên xảy ra ở đâu đó "
        "quanh 10 g lực. Trong vùng này, điện trở thay đổi rất nhanh. Ứng xử này hữu ích khi thiết kế "
        "công tắc dùng điện trở cảm nhận lực."))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p(
        "Không nên dùng FSR để đo lực chính xác vì các bộ phận cảm biến có thể chênh nhau 15% đến 25% về "
        "điện trở. Tuy nhiên, FSR ít trễ và được coi là rẻ hơn nhiều so với các thiết bị cảm nhận khác. "
        "So với piezofilm, FSR ít nhạy với rung và nhiệt hơn nhiều."))

    b.append(h3("Cảm biến lực từ điện trở", "Magnetoresistive Force Sensors"))
    b.append(p(
        "Nguyên lý của cảm biến lực từ điện trở dựa trên thực tế là kim loại, khi được làm lạnh tới nhiệt "
        "độ thấp, thể hiện sự thay đổi điện trở suất khi chịu một từ trường. Bitmut nói riêng khá nhạy "
        "về mặt này. Trong thực tế, các thiết bị này bị hạn chế nghiêm trọng vì độ nhạy cao với thay "
        "đổi nhiệt độ môi trường."))

    b.append(h3("Cảm biến lực từ đàn hồi", "Magnetoelastic Force Sensors"))
    b.append(p(
        "Các thiết bị đầu đo từ đàn hồi hoạt động dựa trên hiệu ứng Joule; nghĩa là một vật liệu sắt từ "
        "bị thay đổi kích thước khi chịu một từ trường. Nguyên lý hoạt động như sau: ban đầu, một xung "
        "dòng được đặt lên dây dẫn trong ống dẫn sóng. Điều này tạo ra một từ trường theo chu vi quanh "
        "ống dẫn sóng trên toàn chiều dài của nó. Có một từ trường khác sinh ra bởi nam châm vĩnh cửu, "
        "chỉ tồn tại ở nơi có nam châm. Từ trường này có một thành phần dọc. Hai từ trường này hợp thành "
        "vectơ tạo nên một từ trường xoắn ốc gần nam châm, và đến lượt nó làm ống dẫn sóng chịu một biến "
        "dạng xoắn rất nhỏ chỉ tại vị trí nam châm. Hiệu ứng xoắn này được gọi là hiệu ứng Wiedemann "
        "[8]."))
    b.append(p(
        "Các đầu đo lực từ đàn hồi có đáp ứng tần số cao (cỡ 20 kHz). Một số vật liệu thể hiện từ đàn hồi "
        "gồm kim loại Monel, Permalloy, Cekas, Alfer, và một số hợp kim niken–sắt. Nhược điểm của các "
        "đầu đo này gồm: (1) ứng suất quá lớn và lão hóa có thể gây ra thay đổi vĩnh viễn, (2) trôi "
        "điểm không và thay đổi độ nhạy do nhạy với nhiệt độ, và (3) sai số trễ."))

    b.append(h3("Cân xoắn", "Torsional Balances"))
    b.append(p(
        "Các thiết bị cân bằng dùng độ võng của một lò xo cũng có thể được dùng để xác định lực. Cân "
        "xoắn là thiết bị đo lực kiểu cân đòn với hai tay đòn bằng nhau. Chúng gồm các dải thép nằm "
        "ngang thay cho trục quay và ổ trục. Nguyên lý hoạt động dựa trên việc đặt lực lên một trong hai "
        "tay đòn, làm lệch lò xo xoắn (trong giới hạn thiết kế) tỉ lệ với lực tác dụng. Loại thiết bị "
        "này nhạy với trễ và sai số nhiệt nên không được dùng cho các phép đo chính xác."))

    b.append(h3("Cảm biến xúc giác", "Tactile Sensors"))
    b.append(p(
        "Cảm biến xúc giác thường được hiểu là một kỹ thuật cảm nhận sự chạm. Không thể coi cảm biến xúc "
        "giác là cảm biến chạm đơn giản, nơi chỉ thực hiện rất ít phép đo lực rời rạc. Trong cảm nhận xúc "
        "giác, một “phân bố” lực được đo bằng một mảng dày đặc các cảm biến lực."))
    b.append(p(
        "Cảm nhận xúc giác quan trọng trong cả thao tác nắm giữ và nhận dạng vật thể. Việc nắm giữ một "
        "vật phải được thực hiện một cách ổn định để vật không bị trượt hoặc bị hỏng. Nhận dạng vật thể "
        "bao gồm nhận biết hình dạng, vị trí và hướng của sản phẩm, cũng như xác định các tính chất bề "
        "mặt và khuyết tật. Lý tưởng nhất, các nhiệm vụ này cần hai loại cảm nhận [9]:"))
    b.append(ol([
        "Cảm nhận liên tục các lực tiếp xúc",
        "Cảm nhận biên dạng biến dạng bề mặt",
    ]))
    b.append(p(
        "Hai loại dữ liệu này nói chung liên hệ với nhau qua các quan hệ ứng suất–biến dạng của cảm biến "
        "xúc giác. Kết quả là đạt được cảm nhận gần như liên tục và biến đổi được của các lực xúc giác "
        "(cảm nhận biên dạng võng xúc giác)."))

    b.append(h4("Yêu cầu đối với cảm biến xúc giác", "Tactile Sensor Requirements"))
    b.append(p(
        "Những tiến bộ đáng kể trong cảm nhận xúc giác đang diễn ra trong lĩnh vực robot. Các ứng dụng "
        "gồm kiểm tra tự động biên dạng bề mặt, xử lý vật liệu hoặc chuyển chi tiết, lắp ráp chi tiết, "
        "và nhận dạng và kiểm tra chi tiết trong các ứng dụng sản xuất và các nhiệm vụ thao tác tinh. "
        "Một số ứng dụng này có thể chỉ cần cảm nhận chạm (lực–mômen) đơn giản nếu các chi tiết được "
        "nắm giữ đã được định hướng đúng và nếu đã có đủ thông tin về quá trình."))
    b.append(p(
        "Đương nhiên, mục tiêu thiết kế chính của các thiết bị cảm nhận xúc giác là mô phỏng khả năng của "
        "ngón tay người [9]. Các chỉ tiêu kỹ thuật điển hình của một cảm biến xúc giác công nghiệp gồm:"))
    b.append(ol([
        "Độ phân giải không gian khoảng 2 mm",
        "Độ phân giải lực (độ nhạy) khoảng 2 g",
        "Lực chạm cực đại khoảng 1 kg",
        "Thời gian đáp ứng thấp, 5 ms",
        "Trễ thấp",
        "Độ bền trong các điều kiện làm việc cực kỳ khó khăn",
        "Không nhạy với thay đổi điều kiện môi trường (nhiệt độ, bụi, độ ẩm, rung, v.v.)",
        "Khả năng theo dõi trượt",
    ]))

    b.append(h4("Cảm biến mảng xúc giác", "Tactile Array Sensor"))
    b.append(p(
        "Cảm biến mảng xúc giác (Hình 23.15) gồm một mẫu đều các phần tử cảm nhận để đo phân bố áp suất "
        "trên đầu ngón tay của một robot. Mảng 8 × 8 phần tử với bước 2 mm theo mỗi phương cung cấp 64 "
        "phần tử nhạy lực. Bảng 23.1 nêu một số đặc tính của các cảm biến mảng xúc giác đời đầu. Cảm "
        "biến gồm hai lớp dây đồng đặt chéo nhau, ngăn cách bằng các dải cao su silicon mỏng. Cảm biến "
        "tạo thành một lớp mỏng, mềm dẻo, có thể dễ dàng gắn lên nhiều hình dạng và kích cỡ đầu ngón "
        "tay khác nhau. Toàn bộ mảng được máy tính lấy mẫu."))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(table(
        ["Tham số thiết bị", "4 × 4", "8 × 8", "16 × 16"],
        [["Bước ô (mm)", "4,00", "2,00", "1,00"],
         ["Điện dung khi không tải (fF)", "6,48", "1,62", "0,40"],
         ["Lực phá hủy (N)", "18,90", "1,88", "0,19"],
         ["Điện dung tuyến tính cực đại (fF)", "4,80", "1,20", "0,30"],
         ["Điện áp ra cực đại (V)", "1,20", "0,60", "0,30"],
         ["Độ phân giải cực đại (bit)", "9,00", "8,00", "8,00"],
         ["Thời gian đọc (truy cập) (µs)", "—", "&lt;20", "—"]],
        "Bảng 23.1 · Tóm tắt một số đặc tính của các cảm biến mảng xúc giác đời đầu. "
        "Nguồn: © IEEE 1985."))
    b.append(p(
        "Một mảng cảm biến xúc giác điển hình có thể gồm nhiều phần tử cảm nhận. Mỗi phần tử hay taxel "
        "(Hình 23.16) được dùng để cảm nhận các lực hiện có. Vì cảm biến xúc giác được triển khai trong "
        "các ứng dụng cần độ nhạy tương tự cảm giác chạm của người, một elastomer được dùng để mô phỏng "
        "da người. Elastomer nói chung là một vật liệu dẫn điện có độ dẫn điện thay đổi cục bộ khi đặt "
        "áp suất. Bản thân cảm biến gồm ba lớp: một lớp phủ bảo vệ, một tấm elastomer dẫn điện, và một "
        "bản mạch in. Bản mạch in gồm hai hàng, mỗi hàng hai “hồng tâm” (bullseye), mỗi hồng tâm có vòng "
        "trong và vòng ngoài dẫn điện, tạo nên các taxel của cảm biến. Các vòng ngoài được nối với nhau "
        "và với một transistor chọn cột. Các vòng trong được nối với các điốt (D) trên Hình 23.16. Khi "
        "cột trong mảng được chọn, dòng điện chạy qua các điốt, qua elastomer, rồi qua một transistor "
        "xuống đất. Như vậy, nói chung không thể chỉ kích hoạt một taxel, vì áp suất đặt vào gây biến "
        "dạng cục bộ ở các taxel lân cận. Tình trạng này được gọi là nhiễu chéo và được loại bỏ bằng "
        "các điốt [10]."))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(p(
        "Tín hiệu của cảm biến mảng xúc giác được dùng để cung cấp thông tin về động học tiếp xúc. Có "
        "thể thu được một số tham số đặc trưng, như vị trí tiếp xúc, hình dạng vật thể và phân bố áp "
        "suất."))
    b.append(p(
        "Bố trí chung của một hệ mảng cảm biến có thể thấy trên Hình 23.17. Một ví dụ là ngón tay cảm "
        "nhận tiếp xúc và lực. Ngón tay xúc giác này có bốn cảm biến tiếp xúc làm bằng các dải polymer "
        "áp điện trên bề mặt đầu ngón, cung cấp thông tin tiếp xúc động. Một cảm biến lực bằng gage biến "
        "dạng cung cấp thông tin lực nắm tĩnh."))
    b.append(fig(17, F.fig(17), "vi"))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "[1] M. C. Shaw, <i>Metal Cutting Principles</i>, Oxford: Oxford Science Publications: Clarendon "
        "Press, 1989.",
        "[2] E. O. Doebelin, <i>Measurement Systems, Application and Design</i>, 4th ed., New York: "
        "McGraw-Hill, 1990.",
        "[3] J. W. Dally, W. F. Riley, and K. G. McConnel, <i>Instrumentation for Engineering "
        "Measurements</i>, New York: John Wiley &amp; Sons, 1984.",
        "[4] P. H. Mansfield, <i>Electrical Transducers for Industrial Measurement</i>, London: The "
        "Butterworth Group, 1973.",
        "[5] K. H. Martini, “Multicomponent dynamometers using quartz crystals as sensing elements,” "
        "<i>ISA Trans.</i>, 22(1), 1983.",
        "[6] G. Spur, S. J. Al-Badrawy, and J. Stirnimann, “Measuring the cutting force in five-axis "
        "milling,” translated paper “Zerspankraftmessung bei der fünfachsigen Fräsbearbeitung,” "
        "<i>Zeitschrift für wirtschaftliche Fertigung und Automatisierung</i> 9/93, Carl Hanser, München; "
        "Kistler Piezo-Instrumentation, 20.162e 9.94.",
        "[7] C. L. Nachtigal, <i>Instrumentation and Control, Fundamentals and Applications</i>, Wiley "
        "Series in Mechanical Engineering Practice, New York: Wiley Interscience, John Wiley &amp; Sons, "
        "1990.",
        "[8] C. W. DeSilva, <i>Control Sensors and Actuators</i>, Englewood Cliffs, NJ: Prentice-Hall, "
        "1989.",
        "[9] J. W. Gardner, <i>Microsensors Principles and Applications</i>, New York: John Wiley &amp; "
        "Sons, 1995.",
        "[10] W. Stadler, <i>Analytical Robotics and Mechatronics</i>, New York: McGraw-Hill, 1995.",
    ]))

    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(wl([
        "C. P. Wright, <i>Applied Measurement Engineering, How to Design Effective Mechanical Measurement "
        "Systems</i>, Englewood Cliffs, NJ: Prentice-Hall, 1995.",
        "E. E. Herceg, <i>Handbook of Measurement and Control</i>, Pennsauken, NJ: Schavitz Engineering, "
        "1972.",
        "D. M. Considine, <i>Encyclopedia of Instrumentation and Control</i>, New York: McGraw-Hill, 1971.",
        "H. N. Norton, <i>Sensor and Analyzer Handbook</i>, Englewood Cliffs, NJ: Prentice Hall, 1982.",
        "S. M. Sze, <i>Semiconductor Sensors</i>, New York: John Wiley &amp; Sons, 1994.",
        "B. Lindberg and B. Lindstrom, “Measurements of the segmentation frequency in the chip formation "
        "process,” <i>Ann. CIRP</i>, 32(1), 1983.",
        "J. Tlusty and G. C. Andrews, “A critical review of sensors for unmanned machining,” "
        "<i>Ann. CIRP</i>, 32(2), 1983.",
    ]))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Force is a vector quantity: an action that causes acceleration or a definite reaction of a body. "
        "This chapter surveys the ways the magnitude of such forces can be determined. Measurement rests "
        "on a few principles — balancing an unknown force against a standard mass through levers, "
        "measuring the acceleration of a known mass, equalising it with a magnetic force from a "
        "current-carrying coil and a magnet, spreading it over a known area to make a pressure and "
        "measuring that pressure, or converting it into the deformation of an elastic element — and the "
        "engineering difficulty lies almost entirely in the sensor design."))

    b.append(h2("23.1 General Considerations", "Những xem xét chung"))
    b.append(p(
        "If the forces on a body produce no acceleration they must form a system in equilibrium, and the "
        "body is in static equilibrium. Forces are internal where the particles of the body act on one "
        "another, external otherwise. A supported body under load deforms or displaces at its supports; "
        "the internal forces redistribute until equilibrium is reached, and the body is then in tension, "
        "compression or shear. Across any section the internal forces act in equal and opposite pairs, "
        "whereas external forces act singly."))

    b.append(h2("23.2 Hooke's Law", "Định luật Hooke"))
    b.append(fig(1, F.fig(1), "en"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Loaded in uniaxial tension, uniaxial compression or simple shear, a metal behaves elastically up "
        "to a critical normal or shear stress and then deforms plastically; in the elastic region the "
        "atoms are displaced temporarily and return when the load is removed. Poisson's ratio is the "
        "ratio of transverse to direct strain and lies between 1/4 and 1/3 for metals. Hooke's law gives "
        "stress proportional to strain, with the Young's modulus in tension or compression and the shear "
        "modulus in shear. The fractional change of specific volume follows from the elastic deformation "
        "and, for an isotropic material, equals the direct strain times (1 − 2ν); the bulk modulus is the "
        "pressure change divided by that fractional volume change. An elastic solid is therefore "
        "compressible as long as ν is below 1/2, which is normally true of metals. The uniaxial form "
        "generalises to three dimensions, and the well-established theory of elasticity underpins every "
        "force-measuring technique below. Note that force measurement is highly application specific and "
        "the choice of technique deserves care."))

    b.append(h3("Basic Methods of Force Measurement", "Các phương pháp cơ bản để đo lực"))
    b.append(p(
        "Five routes are available: balance the unknown force against a standard mass through a lever "
        "system; measure the acceleration of a known mass; equalise it with the magnetic force between a "
        "current-carrying coil and a magnet; spread it over a known area to generate a pressure and "
        "measure that pressure; or convert it into the deformation of an elastic element. These routes "
        "produce a wide variety of instruments, and the sensor design reduces to two problems — the "
        "geometric and physical constraints imposed by the application, and the means of turning force "
        "into a workable signal such as an electronic voltage or a graduated displacement."))

    b.append(h2("23.3 Force Sensors", "Cảm biến lực"))
    b.append(p(
        "Force sensors reveal how a system responds. Cutting forces in machining are monitored to detect "
        "tool failure, to diagnose its causes while controlling process parameters, and to judge surface "
        "quality; impact forces are monitored in the automotive industry; robotic handling and assembly "
        "are controlled by sensing the forces at the end effector. Some sensors measure the deflection a "
        "force produces, which needs deflections of several micrometres to be practical — the excellent "
        "elastic properties of helical springs make them successful here, with Hooke's law relating load "
        "to deflection. Sensors using strain gages or piezoelectric quartz crystals with built-in "
        "microelectronics are common and handle both impulsive and slowly varying forces."))
    b.append(p(
        "Load cells form a general subgroup: a rigid outer structure, a medium that responds to the "
        "applied force, and the measuring gage. They sense large, static or slowly varying forces with "
        "little deflection and are relatively accurate, typically to about 0.1% of full scale. Figure "
        "23.3 shows several types that sense large forces at modest cost; the hydraulic cell, for "
        "instance, uses a very stiff outer structure with an internal cavity filled with fluid, so that "
        "applying a load raises the oil pressure, which is read on an accurate gage. Piezoelectric "
        "transducers give faster response to varying loads, and pneumatic methods and strain gages cover "
        "other conditions."))
    b.append(fig(3, F.fig(3), "en"))

    b.append(h3("Strain Gage Load Cell", "Load cell gage biến dạng"))
    b.append(p(
        "A strain gage load cell pairs a structure that deforms elastically under load with a strain gage "
        "network that produces a signal proportional to that deformation; beam and ring types are the "
        "common examples."))

    b.append(h4("Strain Gages", "Gage biến dạng"))
    b.append(p(
        "A strain gage is a length of gage wire wound as a flat coil to give the wanted resistance, "
        "usually about 120 Ω, cemented between two thin insulating sheets of paper or plastic. It cannot "
        "measure deflection directly: it must first be bonded to the member to be strained, after which "
        "the assembly is baked at about 195°F (90°C) to drive off moisture and coated with wax or resin "
        "for mechanical protection. The resistance between the test member and the gage must be at least "
        "50 MΩ, and the total conductor area must stay small so the cement can transmit the force needed "
        "to deform the wire. As the member is stressed the gage deforms and its cross-section shrinks, "
        "raising its resistivity in a way that is easily measured. Very small strains require measuring "
        "small fractional resistance changes, ΔR/R, and the change for a bonded gage is usually under "
        "0.5%. Many gage sizes and grid shapes exist (Figure 23.4)."))
    b.append(p(
        "Rigidity and environment both demand care. Shorter gages have higher response frequencies — "
        "660 kHz for a 0.2 mm gage against 20 kHz for a 60 mm gage — and because resistance is a function "
        "of temperature, any temperature variation at the gage calls for temperature compensation if the "
        "force measurement is to stay accurate."))
    b.append(p(
        "A Wheatstone bridge (Figure 23.5) measures this small magnitude. No current flows through the "
        "galvanometer when the four resistances satisfy Equation 23.7. Stretching a single bonded gage R₁ "
        "by +ΔR moves the voltage at D from zero to +ΔV and drives a current through C; if R₄ is also a "
        "bonded gage changing by −ΔR at the same time, D moves to +2ΔV; and if R₂ changes by −ΔR and R₃ "
        "by +ΔR, C moves to −2ΔV and the difference between C and D becomes 4ΔV. A single gage works, but "
        "sensitivity rises fourfold when two gages are in tension while two others are in compression."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "The metal-foil grid is formed by photo-etching. The shortest gage available is 0.20 mm and the "
        "longest 102 mm; standard resistances are 120 Ω and 350 Ω. The fractional resistance change is "
        "related to the strain along the grid lines by the gage factor, Equation 23.8."))

    b.append(h4("Beam-Type Load Cell", "Load cell kiểu dầm"))
    b.append(p(
        "Beam-type load cells suit low-level loads. A simple cantilever with four strain gages — two on "
        "the top surface and two on the bottom, all oriented along the beam axis — is the elastic member, "
        "wired into a Wheatstone bridge as in Figure 23.6(b). A load P produces a moment M = Px at the "
        "gage location x and hence the strains of Equation 23.9, where b is the cross-section width and h "
        "its height. The gage response follows from Equation 23.10, and the bridge output voltage from "
        "Equation 23.11 when the four gages are identical. Range and sensitivity depend on the "
        "cross-section shape, on where the load is applied, and on the fatigue strength of the beam "
        "material."))
    b.append(fig(6, F.fig(6), "en"))

    b.append(h4("Ring-Type Load Cell", "Load cell kiểu vòng"))
    b.append(p(
        "Ring-type load cells use a proving ring as the elastic element. Varying the diameter D, the "
        "thickness t or the depth w covers a very wide load range, and either strain gages or a linear "
        "variable-differential transformer can serve as the sensor. The load is linearly proportional to "
        "the output voltage; with an LVDT the sensitivity depends on the ring geometry (R, t and w), on "
        "the ring material (E) and on the LVDT characteristics (S and E_i), while the range is set by the "
        "strength of the ring material."))
    b.append(fig(7, F.fig(7), "en"))

    b.append(h3("Piezoelectric Methods", "Phương pháp áp điện"))
    b.append(p(
        "In a piezoelectric material, deforming an asymmetrical elastic crystal develops a potential "
        "within the distorted lattice, and the effect is reversible: a potential applied across the "
        "crystal changes its dimensions. Such elements are sometimes called electrorestrictive. The "
        "magnitude and polarity of the induced surface charge are proportional to the magnitude and "
        "direction of the applied force, with d the charge sensitivity in C/N (Equation 23.12). The force "
        "also produces a thickness change Δt (Equation 23.13) in terms of the crystal area a, thickness t "
        "and Young's modulus Y, which is just the elastic definition of Y (Equation 23.14). The charge at "
        "the electrodes gives a voltage E₀ = Q/C, with C = εa/t for absolute permittivity ε (Equation "
        "23.15), so the voltage sensitivity g = d/ε in volt metres per newton yields Equation 23.16."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "The materials used are quartz, tourmaline, Rochelle salt, ammonium dihydrogen phosphate, lithium "
        "sulphate, barium titanate and lead zirconate titanate. Quartz and other natural piezoelectric "
        "crystals are naturally polarised, whereas synthetic materials such as barium titanate ceramic "
        "are made by baking small crystallites under pressure and then placing the result in a strong dc "
        "field, after which the crystal is polarised along the axis on which force will be applied. "
        "Artificial elements escape the limits of crystal structure, can be moulded to any size and "
        "shape, and have their polarisation direction fixed during production. Figure 23.8 shows the "
        "modes of a simple plate and Figure 23.9 how two crystals bonded with perpendicular electrical "
        "axes respond to bending or torque. Piezoelectric transducers cover 1 to 200 kN."))
    b.append(p(
        "Piezoelectric crystals also measure instantaneous change of force. A thin quartz plate used as "
        "an electronic oscillator has a frequency dominated by its natural frequency, and any distortion "
        "of the plate by an external force alters that frequency — so a dynamic force can be read from "
        "the frequency shift."))

    b.append(h3("Resistive Method", "Phương pháp điện trở"))
    b.append(p(
        "The resistive method exploits the change of total resistance when the multiple contact area "
        "between semiconducting particles, usually carbon, and their separation change. Such transducers "
        "give a very small displacement under load: two to sixty thin carbon disks between a fixed and a "
        "movable electrode, moving together by 5 to 250 µm per interface, produce a resistance-versus-"
        "force transfer function that is roughly hyperbolic and therefore highly nonlinear, with large "
        "hysteresis and drift and high transverse sensitivity. Replacing the disks with prestressed rings "
        "on an insulated rigid core almost eliminates transverse sensitivity and raises the resonant "
        "frequency to as much as 10 kHz over a 0.1 to 10 kg range, though accuracy and linearity remain "
        "poor."))

    b.append(h3("Inductive Method", "Phương pháp cảm ứng"))
    b.append(p(
        "The inductive method uses the change of permeability that follows a change of mechanical stress "
        "in a ferromagnetic material — the Villari effect, or magnetostriction, particularly strong in "
        "nickel–iron alloys. A coil wound on a magnetostrictive core is stressed by the force to be "
        "measured, changing the core permeability and inductance in a way that can be monitored. The "
        "applicable range is a function of core cross-section and accuracy is set by calibration; "
        "linearity is poor and hysteresis present. Permeability rises under pure torsion regardless of "
        "direction, and the frequency response is flat from 150 Hz to 15,000 Hz."))

    b.append(h3("Piezotransistor Method", "Phương pháp piezotransistor"))
    b.append(p(
        "Devices using anisotropic stress effects are called piezotransistors: a localised stress on the "
        "upper surface of a p–n diode produces a significant reversible change in junction current. They "
        "are usually silicon non-planar transistors with an emitter–base junction mechanically connected "
        "to a diaphragm on the upper surface of a TO-type can; pressure or force on the diaphragm "
        "produces a charge. Constant temperature is advisable because semiconductor properties vary with "
        "temperature, and the attraction of the device is that it survives a 500% overload."))

    b.append(h3("Multicomponent Dynamometers Using Quartz Crystals",
                "Dynamometer đa thành phần dùng tinh thể thạch anh"))
    b.append(p(
        "Force measurement uses the direct piezoelectric effect: the direct longitudinal effect measures "
        "compressive force and the direct shear effect measures shear force in one direction. A quartz "
        "disk cut normal to the crystallographic x-axis and loaded in compression yields a charge of "
        "nominally 2.26 pC/N; one cut normal to the y-axis yields 4.52 pC/N when loaded in shear in one "
        "specific direction, and forces in other directions generate no output. A charge amplifier "
        "converts the charge to a proportional voltage, its range set by a feedback capacitor, with "
        "additional variable-gain operational amplifiers scaling to mechanical units."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "The building block of a multicomponent dynamometer is the three-component force transducer of "
        "Figure 23.10: a pair of X-cut quartz disks for the normal component and a pair of Y-cut, "
        "shear-sensitive disks for each shear component. Four such transducers sandwiched between a base "
        "plate and a top plate measure cutting forces in machining. They carry a preload because shear is "
        "transmitted by friction, and each sees a drastic change of load depending on the type and "
        "position of force application: an overhanging introduction of force develops tension in some "
        "transducers and so reduces the preload, while bending of the top plate adds bending and shearing "
        "stresses. Measuring ranges therefore depend not only on the individual forces but on the "
        "individual bending stresses."))
    b.append(fig(11, F.fig(11), "en"))
    b.append(p(
        "Figure 23.11 shows the rotating cutting force dynamometer. A ring-shaped sensor (1) sits in a "
        "steep-angle taper socket (2) and a base ring (3), sensing the three force components at the "
        "cutting edge and the moment Mz. The quartz plates are aligned so that maximum cross-sensitivity "
        "between components is 1%; the rigid design puts the resonant frequencies between 1200 and "
        "3000 Hz over ranges up to 10 kN. Four miniature hybrid charge amplifiers (7) convert the charges "
        "to voltages, which are filtered against aliasing and digitised at 8-bit resolution with a high "
        "sampling rate. A telemetry unit — receiver and transmitter module, an antenna at the top of the "
        "rotating system (8) and a fixed antenna (9) on the splash cover of the two-axis milling head "
        "(10) — carries the signals out, modulated on an FM carrier, to an external conditioning unit."))
    b.append(p(
        "Any mechanical system can be treated to first approximation as a weakly damped oscillator of a "
        "spring and a mass; where it has more than one resonant frequency the lowest matters. As long as "
        "the test frequency stays below 10% of the resonant frequency of the reference transducer used "
        "for calibration, the dynamic sensitivity differs from the static calibration by less than 1%, "
        "assuming a sinusoidal force signal. A static calibration of the reference transducer remains "
        "valid for dynamic work when the test frequency is at least ten times lower than the system's "
        "resonant frequency."))

    b.append(h3("Capacitive Force Transducer", "Đầu đo lực kiểu điện dung"))
    b.append(p(
        "A capacitive transducer measures force by directing it onto a membrane whose elastic deflection "
        "is detected as a change of capacitance; because capacitive sensing resolves very small "
        "deflections accurately, a highly sensitive force transducer is possible, with an electronic "
        "circuit converting capacitance change into dc voltage change. The sensor of Figure 23.12 is two "
        "metal plates separated by an air gap, with capacitance given by Equation 23.17 in terms of the "
        "permittivity of free space, the relative permittivity of the insulator, the overlapping area and "
        "the gap thickness. Sensitivity is inherently low: theory says a smaller gap h raises it, but "
        "practical electrical and mechanical conditions prevent high sensitivity. The main advantages are "
        "that moving one plate relative to the other needs an extremely small force, and that stability "
        "is good — sensitivity is not influenced by ambient pressure or temperature."))
    b.append(fig(12, F.fig(12), "en"))

    b.append(h3("Force Sensing Resistors (Conductive Polymers)",
                "Điện trở cảm nhận lực (polymer dẫn điện)"))
    b.append(p(
        "Force sensing resistors exploit the fact that certain polymer thick-film devices decrease in "
        "resistance as applied force increases. One part is a resistive material applied to a film, the "
        "other a set of interdigitated contacts on a second film; the resistive material completes the "
        "circuit between the two sets of conductors, and force improves the connection so conductivity "
        "rises. Over a wide range the conductivity is approximately linear in force. There are three "
        "operating regions, with the first abrupt transition near 10 g of force, where resistance changes "
        "very rapidly — useful when designing switches. FSRs should not be used for accurate force "
        "measurement, since parts may vary 15% to 25% in resistance from one to another, but they show "
        "little hysteresis, cost far less than other sensing devices, and are far less sensitive to "
        "vibration and heat than piezofilm."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))

    b.append(h3("Magnetoresistive Force Sensors", "Cảm biến lực từ điện trở"))
    b.append(p(
        "Magnetoresistive sensors rest on the change of resistivity that metals show in an applied "
        "magnetic field when cooled to low temperature, bismuth being particularly sensitive. In practice "
        "they are severely limited by their high sensitivity to ambient temperature change."))

    b.append(h3("Magnetoelastic Force Sensors", "Cảm biến lực từ đàn hồi"))
    b.append(p(
        "Magnetoelastic transducers work on the Joule effect, a ferromagnetic material changing dimension "
        "in a magnetic field. A current pulse in the conductor within the waveguide sets up a "
        "circumferential field along its whole length; the permanent magnet adds a field with a "
        "longitudinal component only where the magnet sits. The two combine vectorially into a helical "
        "field near the magnet, which twists the waveguide minutely at that point alone — the Wiedemann "
        "effect. Frequency response is high, of the order of 20 kHz, and materials showing the effect "
        "include Monel, Permalloy, Cekas, Alfer and a number of nickel–iron alloys. The drawbacks are "
        "that excessive stress and ageing may cause permanent change, that zero drift and sensitivity "
        "change follow from temperature sensitivity, and that hysteresis errors occur."))

    b.append(h3("Torsional Balances", "Cân xoắn"))
    b.append(p(
        "Balancing devices using the deflection of a spring can also determine force. Torsional balances "
        "are equal-arm scale devices built with horizontal steel bands instead of pivots and bearings: a "
        "force applied to one arm deflects the torsional spring within its design limits in proportion to "
        "the applied force. Susceptible to hysteresis and temperature error, they are not used for "
        "precise measurement."))

    b.append(h3("Tactile Sensors", "Cảm biến xúc giác"))
    b.append(p(
        "Tactile sensors are usually understood as a touch-sensing technique, but they are not simple "
        "touch sensors making a few discrete force measurements: in tactile sensing a force distribution "
        "is measured with a closely spaced array of force sensors. Tactile sensing matters both for "
        "grasping and for object identification. Grasping must be stable so the object neither slips nor "
        "is damaged, and identification covers shape, location and orientation as well as surface "
        "properties and defects. Ideally the task needs two kinds of sensing — continuous sensing of "
        "contact forces and sensing of the surface deformation profile — related through the "
        "stress–strain relations of the sensor, which yields almost continuous variable sensing of "
        "tactile forces."))

    b.append(h4("Tactile Sensor Requirements", "Yêu cầu đối với cảm biến xúc giác"))
    b.append(p(
        "Tactile sensing is advancing rapidly in robotics, for automated inspection of surface profiles, "
        "material handling and parts transfer, assembly, and parts identification and gaging, as well as "
        "fine manipulation; some of these need only simple touch or force–torque sensing where parts are "
        "properly oriented and process information is already available. The design objective has been to "
        "mimic the human finger. Typical specifications for an industrial tactile sensor are a spatial "
        "resolution of about 2 mm, force resolution of about 2 g, maximum touch force of about 1 kg, "
        "response time of 5 ms, low hysteresis, durability under extremely difficult working conditions, "
        "insensitivity to temperature, dust, humidity and vibration, and the ability to monitor slip."))

    b.append(h4("Tactile Array Sensor", "Cảm biến mảng xúc giác"))
    b.append(p(
        "Tactile array sensors consist of a regular pattern of sensing elements measuring the pressure "
        "distribution across a robot fingertip. An 8 × 8 array at 2 mm spacing in each direction provides "
        "64 force-sensitive elements, and Table 23.1 outlines the characteristics of early arrays. The "
        "sensor is two crossed layers of copper strips separated by strips of thin silicone rubber, "
        "forming a thin compliant layer easily attached to a variety of fingertip shapes and sizes, and "
        "the whole array is sampled by computer."))
    b.append(fig(15, F.fig(15), "en"))
    b.append(table(
        ["Device parameter", "4 × 4", "8 × 8", "16 × 16"],
        [["Cell spacing (mm)", "4.00", "2.00", "1.00"],
         ["Zero-pressure capacitance (fF)", "6.48", "1.62", "0.40"],
         ["Rupture force (N)", "18.90", "1.88", "0.19"],
         ["Max. linear capacitance (fF)", "4.80", "1.20", "0.30"],
         ["Max. output voltage (V)", "1.20", "0.60", "0.30"],
         ["Max. resolution (bit)", "9.00", "8.00", "8.00"],
         ["Readout (access) time (µs)", "—", "&lt;20", "—"]],
        "Table 23.1 · Summary of some of the characteristics of early tactile array sensors. "
        "Source: © IEEE 1985."))
    b.append(p(
        "A typical array has several sensing elements, each called a taxel (Figure 23.16). Because "
        "tactile sensors are deployed where a semblance of human touch is wanted, an elastomer mimics "
        "human skin — generally a conductive material whose conductivity changes locally under pressure. "
        "The sensor has three layers: a protective covering, a sheet of conductive elastomer, and a "
        "printed circuit board. The board carries two rows of two bullseyes, each with conductive inner "
        "and outer rings forming the taxels; outer rings are connected together and to a column-select "
        "transistor, inner rings to the diodes D of Figure 23.16. Once the column is selected, current "
        "flows through the diodes, through the elastomer and thence through a transistor to ground. "
        "Excitation of a single taxel is generally impossible because applied pressure deforms "
        "neighbouring taxels too; this crosstalk is eliminated by the diodes."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "Array signals provide information about contact kinematics — contact location, object shape and "
        "pressure distribution. Figure 23.17 shows the general layout of an intelligent sensor array "
        "system, exemplified by a contact and force sensing finger: four contact sensors of piezoelectric "
        "polymer strips on the fingertip surface supply dynamic contact information, while a strain gage "
        "force sensor supplies static grasp force information."))
    b.append(fig(17, F.fig(17), "en"))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 23 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 23 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 23 “Đo lực” của M. A. Elbestawi (McMaster University) — điều kiện "
            "cân bằng, định luật Hooke, năm phương pháp đo lực cơ bản, load cell gage biến dạng kiểu dầm "
            "và kiểu vòng, cầu Wheatstone, phương pháp áp điện và piezotransistor, dynamometer thạch anh "
            "ba thành phần, đầu đo điện dung, điện trở cảm nhận lực, cảm biến từ điện trở và từ đàn hồi, "
            "cân xoắn và cảm biến xúc giác, với 17 hình, 1 bảng và 17 phương trình." if vi
            else
            "Companion to Chapter 23 of the CRC Measurement Handbook — force measurement: equilibrium, "
            "Hooke's law, the five basic methods, strain-gage beam and ring load cells, the Wheatstone "
            "bridge, piezoelectric and piezotransistor methods, quartz multicomponent dynamometers, "
            "capacitive, FSR, magnetoresistive and magnetoelastic sensors, and tactile arrays.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 23' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 23' % BASE_EN)
    meta = ("Chương 23 · theo Ch23.pdf (CRC Press, 1999) · 17 hình, 1 bảng, 17 phương trình, "
            "10 tài liệu tham khảo" if vi
            else "Chapter 23 · 17 figures, 1 table, 17 equations, 10 references")
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
