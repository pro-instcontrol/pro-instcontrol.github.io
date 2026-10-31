# -*- coding: utf-8 -*-
"""Handbook Chapter 10 — Position, Location, Altitude Measurement.

Five sections, eight co-authors, forty-three figures and four tables — the
largest chapter in this batch. Writes the Vietnamese translation and the
English companion.
Run:  python build/reader_hb_ch10.py
"""
import os

import hb10fig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch10-position-location-altitude"
TITLE_EN = "Position, Location, Altitude Measurement"
TITLE_VI = "Đo vị trí, định vị và độ cao"
BYLINE = ("Dimitris E. Manolakis · Mark A. Stedham · Partha P. Banerjee · Seiji Nishifuji · "
          "Shogo Tanaka · Halit Eren · C. C. Fung · Jacob Fraden")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-10-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap))


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


def note(text):
    return '<div class="note">%s</div>' % text


def table(headers, rows, caption, cls=""):
    th = "".join("<th>%s</th>" % h for h in headers)
    body = []
    for r in rows:
        if isinstance(r, str):
            body.append('<tr class="grp"><td colspan="%d">%s</td></tr>' % (len(headers), r))
        else:
            body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p class="tblcap">%s</p>' % (cls, th, "".join(body), caption))


def reflist(items, title="Tài liệu tham khảo"):
    out = ['<h3 class="refs-h">%s</h3><ol class="reflist">' % title]
    for it in items:
        out.append("<li>%s</li>" % it)
    out.append("</ol>")
    return "".join(out)


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []

    b.append(p(
        "Chương này gộp năm mảng đo lường mà bề ngoài có vẻ rời rạc — độ cao máy bay, tư thế "
        "phương tiện, dẫn đường quán tính, định vị vệ tinh và phát hiện người trong phòng — nhưng "
        "chúng chia sẻ đúng một bài toán: xác định vị trí của một vật trong không gian ba chiều, "
        "hoặc xác định hướng của nó, từ những phép đo gián tiếp và có nhiễu. Cách giải thì khác "
        "nhau tuỳ theo vật gắn trên máy bay, trên tàu, trên vệ tinh hay đứng yên trong một căn "
        "phòng; nhưng cấu trúc toán học thì gần như giống hệt: một phương trình đo phi tuyến, một "
        "ma trận Jacobian, và một thuật toán bình phương tối thiểu lặp để giải ngược ra ẩn số. "
        "Đọc cả năm mục liền nhau sẽ thấy rõ điều đó rõ hơn là đọc từng mục riêng lẻ."))

    b.append(p(
        "Một điểm cần lưu ý ngay từ đầu: trong chương này, “altitude” và “height” không đồng nghĩa. "
        "Độ cao khí áp (pressure altitude) là đại lượng mà máy đo khí áp trên khoang đưa ra, còn độ "
        "cao hình học (geometric height) là khoảng cách thật tới mặt biển. Hai thứ này khác nhau, "
        "và phần lớn nội dung kỹ thuật của mục 10.1 là về việc đo cái thứ hai bằng radar hoặc bằng "
        "vệ tinh, để kiểm tra cái thứ nhất."))

    # ------------------------------------------------------------ 10.1
    b.append(h2("10.1 Đo độ cao", "Altitude Measurement"))
    b.append(p("<em>Dimitris E. Manolakis · Viện Công nghệ Giáo dục, Hy Lạp</em>"))

    b.append(p(
        "Việc giám sát chính xác độ cao bay của máy bay là yêu cầu bắt buộc để có thể giảm phân "
        "cách thẳng đứng xuống mức tối thiểu cho phép. Mối quan tâm ở đây tập trung vào việc đo "
        "khoảng cách giữa mặt phẳng bay của máy bay và mặt biển. Khoảng cách này có thể được ước "
        "lượng ngay trên khoang nhờ khí áp kế, hoặc được đo — trên khoang hay tại trạm mặt đất — "
        "bằng các hệ thống sóng vô tuyến điện tử. Chỉ thị của nhóm thiết bị thứ nhất được gọi là "
        "độ cao khí áp, hay gọn hơn là độ cao (altitude); còn chỉ thị của nhóm thứ hai được gọi là "
        "độ cao hình học, hay gọn hơn là độ cao thật (height)."))

    b.append(p(
        "Thông tin độ cao tại các trung tâm kiểm soát không lưu (ATC) dựa trên phép đo độ cao khí "
        "áp mà hệ thống phát đáp trên máy bay gửi đi sau khi nhận được một lệnh hỏi thích hợp — gọi "
        "là lệnh hỏi mode C — do radar giám sát thứ cấp phát ra. Thực chất, thông tin độ cao ấy là "
        "một phép đo áp suất khí quyển được chuyển thành chỉ thị độ cao nhờ một công thức biểu diễn "
        "quan hệ áp suất – độ cao. Khi một mức bay được cấp cho máy bay, điều đó thực sự có nghĩa "
        "là phi công phải bay trên một mặt đẳng áp. Tuy nhiên, hệ thống đo cao có thể mắc những sai "
        "số hệ thống (độ lệch) khác nhau với từng máy bay, và những sai số ấy ảnh hưởng đáng kể tới "
        "an toàn. Vì vậy, hiệu năng của hệ thống đo cao cũng như hiệu năng giữ độ cao của máy bay "
        "đều phải được giám sát bằng một hệ thống radar hoặc vệ tinh độc lập."))

    b.append(p(
        "Các hệ radar hay vệ tinh xác định vị trí của một vật thông qua những thuật toán nhận đầu "
        "vào là cự ly, hiệu cự ly, tổng cự ly, hoặc cự ly và phương vị, rồi ước lượng vectơ vị trí "
        "của vật bằng những kỹ thuật thích hợp như tam giác đạc hay đa giác đạc. Các phép đo radar "
        "sơ cấp bị hai loại sai số làm nhiễm bẩn: sai số ngẫu nhiên và sai số hệ thống. Ảnh hưởng "
        "của sai số ngẫu nhiên có thể giảm bớt bằng các bộ lọc khử nhiễu thích hợp, chẳng hạn lọc "
        "Kalman. Loại sai số thứ hai thường được loại bỏ bằng cách hiệu chuẩn dụng cụ nếu có thể; "
        "nếu không, phải nghĩ ra thuật toán thích hợp để dự phòng cho nó."))

    b.append(p(
        "Việc ước lượng có thể được thực hiện tại trạm mặt đất hoặc trên khoang máy bay, tuỳ theo "
        "nơi thu thập và xử lý dữ liệu. Trong trường hợp sau, ước lượng vị trí thẳng đứng phải được "
        "truyền xuống trung tâm ATC thích hợp. Ngoài ra, việc ước lượng có thể làm ngoại tuyến hoặc "
        "trực tuyến. Các phương pháp hay hệ thống đặt dưới mặt đất gồm: Hệ đo độ chính xác dẫn đường "
        "(NAMS), phương pháp ước lượng độ cao bằng một radar kiểm soát không lưu duy nhất, phương "
        "pháp dùng một radar giám sát thứ cấp (SSR) cộng một radar đẳng hướng, Hệ giám sát độ cao tự "
        "động đồng bộ kép (DAMS), và các phương pháp dùng nhiều SSR rồi ước lượng độ cao bằng đa giác "
        "đạc, bằng phép đo giả cự ly, hoặc bằng phép đo hiệu cự ly. Các phương pháp đo độ cao trên "
        "khoang lại suy ra ước lượng của mình bằng đa giác đạc từ tín hiệu của Thiết bị đo khoảng "
        "cách (DME) hoặc của Hệ định vị toàn cầu (GPS)."))

    b.append(h3("Ước lượng độ cao từ mặt đất", "Ground-Based Height Estimation"))

    b.append(p(
        "Các radar dùng để thu những phép đo gốc là radar giám sát sơ cấp hoặc thứ cấp. Radar sơ cấp "
        "phát một tín hiệu rồi quét chờ sự trở về của tín hiệu phản xạ. Cự ly tới vật phản xạ được "
        "suy ra từ khoảng thời gian giữa lúc phát và lúc thu. Với radar thứ cấp, radar phát một lệnh "
        "hỏi tới máy bay — tới mọi máy bay hoặc tới một máy bay được chọn — và máy bay thích hợp trả "
        "lời qua bộ phát đáp của mình. Cự ly tới máy bay được tính từ khoảng thời gian giữa lúc phát "
        "tín hiệu và lúc tín hiệu tới, có tính tới thời gian trễ danh định của bộ phát đáp. Phần lớn "
        "các phương pháp ước lượng độ cao máy bay đều dùng thiết bị SSR vì nó hiệu quả về chi phí, "
        "tín hiệu trả lời của bộ phát đáp mạnh hơn tín hiệu phản xạ về radar sơ cấp, và hệ thống vận "
        "hành đáng tin cậy hơn ở những vùng có mật độ bay cao."))

    b.append(p(
        "Mọi sai số hệ thống trong radar sơ cấp và trong thiết bị mặt đất của SSR đều có thể sửa "
        "được bằng hiệu chuẩn. Tuy nhiên, vấn đề gặp phải với SSR là nó kéo thời gian trễ của bộ phát "
        "đáp vào quá trình đo cự ly. Do đó, bất kỳ sai số hệ thống nào trong thời gian trễ ấy đều gây "
        "ra sai số lệch cự ly khác nhau với từng máy bay, và phải dùng những phương pháp thích hợp để "
        "dự phòng cho nó trong bước xử lý dữ liệu đo tiếp theo."))

    b.append(h4("Hệ đo độ chính xác dẫn đường (NAMS)",
                "Navigation Accuracy Measurement System"))

    b.append(p(
        "Nagaoka đã đề xuất một hệ ước lượng độ cao kiểu ngoại tuyến [1–3]. Hệ gồm một radar hàng "
        "hải sơ cấp đặt bên dưới một đường bay, đo cự ly R và góc hạ β. Hình 10-1 trình bày hình học "
        "của hệ. Ăng ten quay quanh một trục thẳng đứng và quét vùng không gian phía trên với tốc độ "
        "một vòng trong 3 s. Nguyên lý được khai thác để suy ra ước lượng độ cao là: cự ly thay đổi "
        "khi máy bay đi qua vùng thu thập dữ liệu. Tốc độ thay đổi của cự ly chủ yếu là hàm của độ "
        "cao bay z, và thứ yếu là hàm của góc hạ. Từ Hình 10-1 dễ dàng suy ra quan hệ giữa các đại "
        "lượng trên với vị trí x dọc theo trục x tại thời điểm t:"))

    b.append(eq("R(t)² = x(t)² + R′(t)² = x(t)² + z²/cos²β", "10.1"))

    b.append(p(
        "Ký hiệu x₀ là vị trí của máy bay tại thời điểm t₀. Giả thiết máy bay bay thẳng và bằng, "
        "nghĩa là vận tốc Vx, góc hạ và độ cao h đều không đổi trong suốt thời gian thu thập dữ "
        "liệu. Các đại lượng trên và phép đo cự ly tại thời điểm tᵢ liên hệ với nhau qua phương "
        "trình 10.2:"))

    b.append(eq("Rᵢ = fᵢ(q) = √[(x₀ + Vx(tᵢ − t₀))² + z²/cos²β]", "10.2"))

    b.append(p("trong đó q là vectơ các ẩn số, q = [x₀, Vx, z]<sup>T</sup>."))

    b.append(p(
        "Các phép đo Rᵢ và β được thu tại các thời điểm t₀, t₁, …, tₙ, và tập hợp của chúng được "
        "viết gọn thành một hàm vectơ của các ẩn số bằng phương trình ma trận sau:"))

    b.append(eq("R = f(q)", "10.3"))

    b.append(p(
        "Phương trình 10.3 là phi tuyến. Vì vậy phải dùng một phương pháp bình phương tối thiểu phi "
        "tuyến, chẳng hạn phương pháp lặp Gauss–Newton, để ước lượng vectơ ẩn. Gọi q̂<sub>k</sub> là "
        "ước lượng tại vòng lặp thứ k. Khi đó ước lượng kế tiếp là:"))

    b.append(eq("q̂<sub>k+1</sub> = q̂<sub>k</sub> + (F<sup>T</sup>F)<sup>−1</sup>F<sup>T</sup>"
                "[R − f(q̂<sub>k</sub>)]", "10.4"))

    b.append(p("trong đó F là ma trận đạo hàm riêng (Jacobian), tức là:"))

    b.append(eq("F = ∂f/∂q", "10.5"))

    b.append(fig(1, hb10fig.fig_10_1()))

    b.append(p(
        "Giả thiết những vận tốc và mức bay điển hình, đồng thời tính tới độ mở chùm quạt của ăng "
        "ten và tốc độ quay, người ta xác định được rằng thời gian quan sát xấp xỉ 1 phút và số phép "
        "đo xấp xỉ 20. Độ lệch chuẩn của sai số ước lượng độ cao là σ<sub>z</sub> = 10 m khi độ lệch "
        "chuẩn của sai số đo cự ly và góc hạ lần lượt là σ<sub>R</sub> = 10 m và σ<sub>β</sub> = "
        "0,08°."))

    b.append(p(
        "Hệ đã được phát triển và đang vận hành tại Viện Dẫn đường Điện tử Tokyo, Nhật Bản. Để ước "
        "lượng và dự phòng các sai số hệ thống trong phép đo góc hạ và cự ly, người ta đã đề xuất "
        "thực hiện 40 chuyến bay thực nghiệm phía trên vùng phủ của radar. Giả thiết cơ bản của hệ "
        "NAMS (rằng máy bay bay ở độ cao không đổi) không thể được chính NAMS kiểm chứng. Vì thế cần "
        "một SSR để xác nhận rằng chuyến bay thực sự được thực hiện trên cùng một mức, thông qua các "
        "lệnh hỏi mode C [3]."))

    b.append(h4("Ước lượng độ cao bằng một radar kiểm soát không lưu duy nhất",
                "Height Estimation with a Single Air-Traffic Control Radar"))

    b.append(p(
        "Nagaoka tại Viện Dẫn đường Điện tử Tokyo đã khảo sát khả năng suy ra ước lượng độ cao bằng "
        "một phương pháp rất đơn giản và rẻ tiền [4]. Ý tưởng là dùng một radar thường dùng cho kiểm "
        "soát không lưu. Ăng ten radar quay quanh một trục nằm ngang với chu kỳ 4 s và đo cự ly R cùng "
        "phương vị β, như trình bày trên Hình 10-2."))

    b.append(p("Gọi (x, y, z) là vị trí ba chiều của máy bay. Góc phương vị được định nghĩa là:"))

    b.append(eq("β = cos<sup>−1</sup>[y/√(x² + y²)]", "10.6"))

    b.append(fig(2, hb10fig.fig_10_2()))

    b.append(p("Như vậy, quan hệ giữa các phép đo và các ẩn số là:"))

    b.append(eq("R = √(z² + x² + y²) = √[z² + (y/cos β)²]", "10.7"))

    b.append(p(
        "Nguyên lý đo giống như của hệ NAMS, tức là trong khoảng thời gian máy bay đi qua vùng thu "
        "thập dữ liệu, cự ly thay đổi theo cả vị trí ngang lẫn độ cao. Khi giả thiết bay thẳng và "
        "bằng, các ẩn số là độ cao z, vị trí ban đầu trên trục y là y₀, và vận tốc Vy. Biểu thức "
        "liên hệ các phép đo Rᵢ, βᵢ với vectơ ẩn q = [y₀, Vy, z]<sup>T</sup> tại thời điểm tᵢ là:"))

    b.append(eq("Rᵢ = √[z² + (y₀ + Vy(tᵢ − t₀))²/cos²βᵢ] = fᵢ(q)", "10.8"))

    b.append(p(
        "Các phép đo được thu khi máy bay bay gần radar ở khoảng cách 30 km. Vùng thu thập dữ liệu "
        "vào khoảng 15 km, thời gian quan sát là 1 phút và tổng số lần quét là 15. Toàn bộ tập phép "
        "đo được biểu diễn thành một hàm ma trận phi tuyến có dạng phương trình 10.3, nghĩa là "
        "R = f(q) với R ký hiệu vectơ phép đo. Vectơ ẩn được ước lượng bằng một phương pháp bình "
        "phương tối thiểu phi tuyến giống như của hệ NAMS trong phương trình 10.4."))

    b.append(p(
        "Hiệu năng của hệ được đánh giá bằng mô phỏng Monte Carlo. Độ chính xác tốt nhất đạt được là "
        "σ<sub>z</sub> = 100 m với giả thiết sai số độ lệch chuẩn của phép đo cự ly và phương vị là "
        "σ<sub>R</sub> = 100 m và σ<sub>β</sub> = 0,06°. Phương pháp có thể dùng radar sơ cấp hoặc "
        "thứ cấp. Tuy nhiên, với radar thứ cấp, phương pháp buộc phải tính tới độ trễ hệ thống của "
        "bộ phát đáp."))

    b.append(h4("Ước lượng độ cao bằng một SSR và một radar đẳng hướng (SSROR)",
                "Height Estimation with one SSR and One Omni Radar"))

    b.append(p(
        "Manolakis và cộng sự đã khảo sát khả năng ước lượng độ cao bay bằng một hệ gồm một SSR tiêu "
        "chuẩn cộng thêm một radar thứ cấp được trang bị ăng ten đẳng hướng đặt cách xa SSR; do đó hệ "
        "này có thể được gọi là SSROR [5]. Hình 10-3 trình bày một cấu hình hình học điển hình của "
        "hệ. SSR đo phương vị θ và cự ly nghiêng R<sub>s</sub>, được chuyển thành cự ly ngang R nhờ "
        "các bảng tra hiệu chỉnh. Radar đẳng hướng đo cự ly R<sub>a</sub>. Gọi (x, y, z), "
        "(x<sub>a</sub>, y<sub>a</sub>, z<sub>a</sub>) và (0, 0, 0) lần lượt là toạ độ của máy bay, "
        "của radar đẳng hướng và của SSR. Khi đó từ Hình 10-3 suy ra hàm độ cao lý thuyết:"))

    b.append(eq("z = f(R<sub>a</sub>, x, y) = z<sub>a</sub> + [R<sub>a</sub>² − (x − x<sub>a</sub>)² "
                "− (y − y<sub>a</sub>)²]<sup>1/2</sup>", "10.9"))
    b.append(eq("x = R sin θ", "10.10"))
    b.append(eq("y = R cos θ", "10.11"))

    b.append(p(
        "Tuy nhiên, độ cao thu được qua công thức trên sẽ bị lệch vì độ lệch hệ thống của thời gian "
        "trễ bộ phát đáp so với giá trị danh định có ảnh hưởng tới các phép đo cự ly. Vì độ lệch này "
        "không thể loại bỏ bằng hiệu chuẩn, phải áp dụng một thuật toán thích hợp để dự phòng cho "
        "nó. Cách tiếp cận được đề xuất là mở rộng vectơ ẩn bằng cách đưa thêm số hạng độ lệch. Gọi "
        "b là độ lệch trong các phép đo cự ly. Các phép đo bị lệch R<sub>b</sub> và "
        "R<sub>ab</sub> của R và R<sub>a</sub> lần lượt được biểu diễn là:"))

    b.append(eq("R<sub>b</sub> = R + b cos φ", "10.12"))
    b.append(eq("R<sub>ab</sub> = R<sub>a</sub> + b", "10.13"))

    b.append(p("trong đó φ là góc ngẩng. Gọi s là bình phương độ cao:"))

    b.append(eq("s = (z − z<sub>a</sub>)²", "10.14"))

    b.append(p(
        "và s<sub>b</sub> là đại lượng tương ứng suy ra từ các phép đo cự ly (bị lệch). Khi đó, sau "
        "một số phép biến đổi các phương trình trên, thu được quan hệ sau:"))

    b.append(eq("s<sub>b</sub> = s + b·a", "10.15"))
    b.append(eq("a = 2[R<sub>a</sub> − cos φ(R − x sin θ − y cos θ)]", "10.16"))

    b.append(p(
        "Số hạng a là hệ số nhân của độ lệch, được xác định bởi hình học tương đối của hệ. Phương "
        "trình 10.15 là một quan hệ tuyến tính giữa phép đo s<sub>b</sub> với hai ẩn s và b. Hình "
        "10-4 cho thấy ảnh hưởng của độ lệch thay đổi thế nào khi máy bay đi qua vùng giám sát. Dạng "
        "của nó chủ yếu do độ cao bay quyết định. Do đó, có thể ước lượng đồng thời cả độ cao lẫn độ "
        "lệch bằng cách thu dữ liệu trong suốt khoảng thời gian máy bay lưu lại vùng giám sát. "
        "Phương trình đo tại thời điểm tᵢ là:"))

    b.append(eq("s<sub>bi</sub> = sᵢ + b·aᵢ + eᵢ", "10.17"))

    b.append(p(
        "trong đó eᵢ biểu diễn ảnh hưởng của các sai số đo ngẫu nhiên; vì thế nó có thể được gọi là "
        "sai số phương trình. Giả thiết bay bằng, sᵢ = s, và tập dữ liệu thu được được biểu diễn "
        "bằng phương trình ma trận tuyến tính sau:"))

    b.append(eq("s<sub>b</sub> = A q + e", "10.18"))

    b.append(p(
        "trong đó s<sub>b</sub> = [s<sub>b0</sub>, s<sub>b1</sub>, …, s<sub>bn</sub>]<sup>T</sup>, "
        "A là ma trận có cột thứ nhất toàn số 1 và cột thứ hai là [a₀, a₁, …, a<sub>n</sub>], "
        "e = [e₀, e₁, …, e<sub>n</sub>]<sup>T</sup>, và q = [s, b]<sup>T</sup>."))

    b.append(p(
        "Ước lượng tốt nhất q̂ của q, cực tiểu hoá tổng bình phương có trọng số "
        "e<sup>T</sup>We, là:"))

    b.append(eq("q̂ = (A<sup>T</sup>WA)<sup>−1</sup>A<sup>T</sup>Ws<sub>b</sub>", "10.19"))

    b.append(p("trong đó W là ma trận trọng số, được định nghĩa là nghịch đảo của ma trận hiệp "
               "phương sai của sai số phương trình:"))

    b.append(eq("W = E{ee<sup>T</sup>}<sup>−1</sup>", "10.20"))

    b.append(p("với ký hiệu E{ } chỉ phép lấy kỳ vọng toán học. Như vậy ước lượng của độ cao hình "
               "học là:"))

    b.append(eq("z = √ŝ = √q̂<sub>s</sub>", "10.21"))

    b.append(p(
        "Trong trường hợp bay không bằng, người ta dùng một vectơ ẩn mở rộng gồm độ lệch b, độ cao "
        "ban đầu z₀ và vận tốc thẳng đứng Vz [6]. Tuy nhiên khi đó phương trình đo là phi tuyến theo "
        "các ẩn số, nên phải dùng một thuật toán bình phương tối thiểu phi tuyến lặp."))

    b.append(p(
        "Hiệu năng của hệ là hàm của: (1) sai số độ lệch chuẩn của phép đo cự ly và phương vị, "
        "σ<sub>R</sub> và σ<sub>θ</sub>; (2) vận tốc máy bay, vốn ảnh hưởng tới số lần quét; (3) tốc "
        "độ quét của radar đẳng hướng; và (4) các số hạng hình học như mức bay và khoảng cách giữa "
        "hai radar. Với giả thiết σ<sub>R</sub> = 70 m, σ<sub>θ</sub> = 0,08°, độ lệch chuẩn của sai "
        "số ước lượng độ cao sẽ nằm trong khoảng 50 m tới 100 m khi các nhân tố còn lại nhận những "
        "giá trị hợp lý."))

    b.append(fig(3, hb10fig.fig_10_3()))
    b.append(fig(4, hb10fig.fig_10_4()))

    b.append(h4("Hệ giám sát độ cao tự động đồng bộ kép (DAMS)",
                "Dual Synchronized Autonomous Monitoring System"))

    b.append(p(
        "Công trình nghiên cứu được thực hiện tại Phòng thí nghiệm Hàng không Quốc gia NLR, Hà Lan "
        "[7]. Hệ gồm hai radar hàng hải sơ cấp. Mỗi radar có một ăng ten quay. Hai ăng ten quét cùng "
        "một thể tích nhưng theo hai hướng khác nhau — đó là vùng 3 km × 10 km phía trên vị trí đặt "
        "hệ. Vùng giám sát sơ cấp là 3 km × 3 km. Hai ăng ten (A và B) cách nhau 2,5 m, được đồng bộ "
        "cơ khí và quét mỗi 2,5 s một lần. Các bộ trích dữ liệu của chúng cho ra các phép đo cự ly "
        "nghiêng và góc ngẩng, (R<sub>A</sub>, φ<sub>A</sub>) và (R<sub>B</sub>, φ<sub>B</sub>), cho "
        "từng radar. Phần mềm bám quỹ đạo suy ra ước lượng vị trí và quỹ đạo máy bay ở chế độ ngoại "
        "tuyến. Tại mỗi lần quét, có sẵn một tổ hợp bốn phép đo (R<sub>A</sub>, φ<sub>A</sub>, "
        "R<sub>B</sub>, φ<sub>B</sub>) để dùng vào việc ước lượng vectơ ẩn q = [x₀, y₀, z₀, Vx, Vy, "
        "Vz]<sup>T</sup>. Một hệ toạ độ Descartes địa phương được dùng để thực hiện các phép tính. "
        "Cuối cùng, có 16 phương trình để giải cho 6 ẩn số bằng phương pháp bình phương tối thiểu có "
        "trọng số. Trọng số của mỗi phép đo là biên độ đo được của xung radar. Phần toán học của bộ "
        "bám quỹ đạo không được trình bày trong [7]. Tuy vậy, một cách tiếp cận có thể là như sau. "
        "Nếu định nghĩa một hệ toạ độ sao cho radar A ở gốc (0, 0, 0) và radar B ở (x<sub>B</sub>, "
        "0, 0), thì các phép đo thu được tại thời điểm quét tᵢ có thể được biểu diễn là:"))

    b.append(eq("R<sub>Ai</sub>² = xᵢ² + yᵢ² + zᵢ² = (x₀ + Vx(tᵢ − t₀))² + (y₀ + Vy(tᵢ − t₀))² + "
                "(z₀ + Vz(tᵢ − t₀))²", "10.22a"))
    b.append(eq("φ<sub>Ai</sub> = tan<sup>−1</sup>[zᵢ/√(xᵢ² + yᵢ²)]", "10.22b"))
    b.append(eq("R<sub>Bi</sub>² = (xᵢ − x<sub>B</sub>)² + yᵢ² + zᵢ²", "10.22c"))
    b.append(eq("φ<sub>Bi</sub> = tan<sup>−1</sup>{zᵢ/√[(xᵢ − x<sub>B</sub>)² + yᵢ²]}", "10.22d"))

    b.append(p(
        "Lưu ý rằng x<sub>B</sub> có giá trị nhỏ (2,5 m) so với độ lớn của các đại lượng khác; do đó "
        "có thể bỏ qua nó. Tập phương trình trên tại bốn thời điểm khác nhau cho ra 16 phương trình, "
        "có thể giải bằng một phương pháp bình phương tối thiểu phi tuyến như phương pháp lặp "
        "Gauss–Newton trình bày trong phương trình 10.4."))

    b.append(p(
        "Độ lệch chuẩn của sai số ước lượng độ cao sẽ nhỏ hơn 15 m trong vùng giám sát sơ cấp, và "
        "30 m ở rìa vùng, khi độ lệch chuẩn của phép đo cự ly và góc ngẩng nhỏ hơn 10 m và 0,1°."))

    b.append(h4("Đo độ cao bằng đa giác đạc bốn trạm", "Height Measurement by Quadrilateration"))

    b.append(p(
        "Rice đề xuất một hệ gồm bốn trạm thu SSR đồng bộ Sᵢ, i = 0, 1, 2, 3, sử dụng các phát xạ "
        "SSR từ bộ phát đáp trên máy bay và ước lượng độ cao bằng đa giác đạc [8]. Hình 10-5 trình "
        "bày một cấu hình điển hình của hệ gồm N trạm SSR. Một trong số đó là trạm chủ động, nghĩa "
        "là trạm này có cả bộ hỏi lẫn bộ thu. Gọi (x, y, z) và (xᵢ, yᵢ, zᵢ) là toạ độ Descartes của "
        "máy bay và của trạm Sᵢ. Gọi Rᵢ là cự ly từ trạm Sᵢ tới máy bay, c là tốc độ ánh sáng, và "
        "T<sub>s</sub> là thời điểm phát tín hiệu từ bộ phát đáp trên máy bay. Các trạm đo thời điểm "
        "tới (TOA) Tᵢ, i = 0, 1, 2, 3, của tín hiệu phát đáp tại mỗi vị trí. Các quan hệ sau đây "
        "đúng:"))

    b.append(eq("Tᵢ = T<sub>s</sub> + Rᵢ/c,  i = 0, 1, 2, 3", "10.23"))
    b.append(eq("Rᵢ² = (x − xᵢ)² + (y − yᵢ)² + (z − zᵢ)²,  i = 0, 1, 2, 3", "10.24"))

    b.append(p(
        "Hệ tám phương trình trên có thể giải cho các ẩn số. Các ẩn số mà Rice dùng là (R₀, R₁, R₂, "
        "R₃, x, y, z, T<sub>s</sub>)<sup>T</sup>. Tuy nhiên, một cách tương đương là thay Rᵢ trong "
        "phương trình 10.23, khi đó nó trở thành:"))

    b.append(eq("fᵢ(q) = T<sub>s</sub> + (1/c)√[(x − xᵢ)² + (y − yᵢ)² + (z − zᵢ)²],  "
                "i = 0, 1, 2, 3", "10.25"))

    b.append(p(
        "trong đó q = [x, y, z, T<sub>s</sub>]<sup>T</sup> là vectơ ẩn. Như vậy chỉ còn bốn phương "
        "trình phi tuyến cần giải cho q. Một phương pháp thích hợp, chẳng hạn, là phương pháp "
        "Newton–Raphson, vốn xấp xỉ nghiệm một cách lặp đi lặp lại qua công thức sau:"))

    b.append(eq("q<sub>k+1</sub> = q<sub>k</sub> + F(q<sub>k</sub>)<sup>−1</sup>"
                "[T − f(q<sub>k</sub>)]", "10.26"))

    b.append(p("trong đó T = [T₀, T₁, T₂, T₃]<sup>T</sup> là vectơ phép đo và F là ma trận Jacobian:"))

    b.append(eq("F = ∂f/∂q", "10.27"))

    b.append(p(
        "Lưu ý rằng thời điểm phát lệnh hỏi cũng như thời gian trễ danh định của bộ phát đáp đều "
        "không tham gia vào các phép đo. Các đại lượng được đo chỉ là các TOA tại vị trí các trạm. "
        "Do đó ước lượng độ cao không bị ảnh hưởng bởi bất kỳ độ lệch nào của bộ phát đáp."))

    b.append(fig(5, hb10fig.fig_10_5()))

    b.append(p(
        "Công trình nghiên cứu lý thuyết và thực nghiệm được thực hiện tại Trung tâm Nghiên cứu GEC "
        "Marconi, Vương quốc Anh. Cách bố trí trạm tối ưu là đặt ba trạm cách đều nhau trên một "
        "đường tròn và trạm thứ tư ở giữa. Bán kính đường tròn điển hình là 35 km. Cùng độ lớn đó "
        "cũng đúng cho cự ly đo. Phương pháp có thể được thực hiện ở chế độ trực tuyến hoặc ngoại "
        "tuyến. Với chế độ thứ nhất, tại các trạm phải có bộ phát để truyền các phép đo TOA của mình "
        "tới trung tâm giám sát độ cao. Suy giảm độ chính xác theo phương thẳng đứng (VDOP) là một "
        "chỉ số hiệu năng, được định nghĩa bằng tỉ số:"))

    b.append(eq("VDOP = σ<sub>z</sub>/σ<sub>rte</sub>", "10.28"))

    b.append(p(
        "trong đó σ<sub>rte</sub> là độ lệch chuẩn của các sai số định thời tương đối. VDOP biểu "
        "diễn ảnh hưởng của hình học tương đối lên hiệu năng của hệ. VDOP của hệ này đạt giá trị "
        "điển hình là 3."))

    b.append(h4("Ước lượng độ cao bằng SSR và giả cự ly",
                "Height Estimation with SSRs and Pseudoranges"))

    b.append(p(
        "Cách tiếp cận này được Nagaoka tại Viện Dẫn đường Điện tử Tokyo khảo sát [9]. Hệ gồm N trạm "
        "thu SSR; xem Hình 10-5. Một trong số đó, chẳng hạn S₀, phải là trạm chủ động để phát lệnh "
        "hỏi tới máy bay. Thời điểm phát lệnh hỏi T<sub>t</sub> và thời điểm tín hiệu tới các trạm "
        "thu Tᵢ, i = 0, 1, …, N − 1, đều được đo. Như vậy thu được N phép đo giả cự ly rᵢ, với "
        "rᵢ = c(Tᵢ − T<sub>t</sub>). Gọi T<sub>D</sub> là độ trễ của bộ phát đáp và D là khoảng cách "
        "tương ứng với độ trễ ấy, D = cT<sub>D</sub>. Khi đó, với mỗi phép đo giả cự ly rᵢ, quan hệ "
        "sau đây đúng:"))

    b.append(eq("rᵢ = D + Rᵢ = D + √[(x − xᵢ)² + (y − yᵢ)² + (z − zᵢ)²],  i = 0, 1, …, N − 1",
                "10.29"))

    b.append(p(
        "trong đó q = [x, y, z, D]<sup>T</sup> là vectơ ẩn. Tập N phép đo ρ = [ρ₀, ρ₁, …, "
        "ρ<sub>N−1</sub>]<sup>T</sup>, với N ≥ 4, và vectơ ẩn liên hệ với nhau qua phương trình "
        "10.30."))

    b.append(eq("ρ = f(q)", "10.30"))

    b.append(p(
        "Vectơ ẩn q có thể thu được từ nghiệm của phương trình 10.30 bằng một phương pháp bình "
        "phương tối thiểu có trọng số phi tuyến. Như vậy ước lượng tốt nhất của q được tính lặp:"))
    b.append(eq("q̂<sub>k+1</sub> = q̂<sub>k</sub> + (F<sup>T</sup>F)<sup>−1</sup>F<sup>T</sup>"
                "[ρ − f(q̂<sub>k</sub>)]", "10.31"))

    b.append(p("trong đó F là ma trận Jacobian:"))
    b.append(eq("F = ∂f/∂q", "10.32"))

    b.append(p(
        "Ước lượng q không còn sai số hệ thống do độ trễ bộ phát đáp, bởi vì việc ước lượng không "
        "dựa trên độ trễ danh định mà dựa trên độ trễ thực tế — vốn là một trong các tham số cần ước "
        "lượng, bên cạnh các tham số còn lại là ba toạ độ vị trí của máy bay x, y, z."))

    b.append(p(
        "Cách bố trí trạm mà Nagaoka đề xuất, khi có bốn trạm, là một tam giác đều tạo bởi ba trạm, "
        "còn trạm thứ tư đặt ở tâm. VDOP, được định nghĩa là tỉ số σ<sub>z</sub>/σ<sub>R</sub> (với "
        "σ<sub>R</sub> là sai số quan sát), có giá trị điển hình là 4 khi máy bay ở phía trên tâm với "
        "độ cao bằng bán kính đường đáy. VDOP tăng lên khi máy bay bay cao hơn và xa hơn, và khi bán "
        "kính đường đáy nhỏ đi."))

    b.append(h4("Đo độ cao bằng SSR và hiệu cự ly",
                "Height Measurement with SSRs and Range Differences"))

    b.append(p(
        "Cách tiếp cận này được Manolakis và Lefas đề xuất [10, 11]. Hệ gồm N − 1 trạm thu SSR Sᵢ, "
        "i = 1, …, N − 1, và một trạm, chẳng hạn S₀, vừa là bộ thu vừa là bộ hỏi; xem Hình 10-5. Các "
        "trạm thu tín hiệu trả lời và đo hiệu thời điểm tới (TDOA) giữa một trạm chuẩn, chẳng hạn "
        "S₀, với trạm Sᵢ. Một tập N − 1 phép đo TDOA, hay tương đương là hiệu cự ly (RD), được thu "
        "mỗi khi bộ phát đáp gửi tín hiệu trả lời. Ước lượng độ cao suy ra từ tập phép đo này không "
        "bị ảnh hưởng bởi sai số hệ thống nào của độ trễ bộ phát đáp, vì sai số ấy vốn đã bị trừ đi "
        "ngay trong các phép đo được dùng. Hệ này có thể được gọi là khối giám sát độ cao theo hiệu "
        "cự ly (RDHMU). Các hệ suy ra vị trí dựa trên loại phép đo này được gọi là hệ TDOA, hệ RD "
        "hay hệ hyperbol."))

    b.append(p(
        "Gọi τᵢ là TDOA giữa trạm Sᵢ và S₀, và dᵢ là phép đo RD tương ứng, dᵢ = cτᵢ. Quan hệ sau đây "
        "đúng:"))

    b.append(eq("dᵢ = Rᵢ − R₀ = √[(x − xᵢ)² + (y − yᵢ)² + (z − zᵢ)²] − "
                "√[(x − x₀)² + (y − y₀)² + (z − z₀)²],  i = 1, …, N − 1", "10.33"))

    b.append(p("trong đó q = [x, y, z]<sup>T</sup> là vectơ vị trí máy bay cần tìm. Vectơ các phép "
               "đo RD d = [d₁, d₂, …, d<sub>N−1</sub>] được biểu diễn là:"))

    b.append(eq("d = f(q)", "10.34"))

    b.append(p(
        "Một phương pháp thường được dùng để giải q trong phương trình phi tuyến này là phương pháp "
        "chuỗi Taylor, hay tương đương là phương pháp lặp Gauss–Newton. Ước lượng tốt nhất của q "
        "được xấp xỉ lặp:"))
    b.append(eq("q̂<sub>k+1</sub> = q̂<sub>k</sub> + (F<sup>T</sup>F)<sup>−1</sup>F<sup>T</sup>"
                "[d − f(q̂<sub>k</sub>)]", "10.35"))

    b.append(p("trong đó F là ma trận Jacobian:"))
    b.append(eq("F = ∂f/∂q", "10.36"))

    b.append(p(
        "Với trường hợp bốn trạm, cách bố trí tốt nhất là một tam giác đều với trạm thứ tư ở tâm. "
        "Độ lệch chuẩn của sai số ước lượng độ cao σ<sub>z</sub> sẽ là 15 m khi bán kính đường đáy "
        "là 6 km, độ cao bay là 9 km, và σ<sub>TDOA</sub> là 10 ns."))

    b.append(p(
        "Công trình kiểm chứng nguyên lý và phát triển hệ thống cho một HMU dựa trên khái niệm đo "
        "TDOA các tín hiệu SSR đã được thực hiện tại Roke Manor Research Ltd., Vương quốc Anh [12]."))

    # ---- onboard
    b.append(h3("Ước lượng độ cao trên khoang", "Onboard Derived Height Estimation"))

    b.append(h4("Đo độ cao bằng thiết bị đo khoảng cách (DME)",
                "Height Measurement with Distance Measuring Equipment"))

    b.append(p(
        "Cách tiếp cận này để suy ra độ cao hình học ngay trên khoang máy bay bằng thiết bị DME "
        "được Rekkas và cộng sự công bố lần đầu [13], còn những kỹ thuật hiệu quả và tổng quát hơn "
        "thì do Manolakis đề xuất [14, 15]. Dùng thiết bị hỏi DME, người ta đo trên khoang khoảng "
        "cách tới ba trạm DME mặt đất (xem Hình 10-6). Ba trạm này nằm bên dưới một đường bay. Độ "
        "cao sau đó được tính từ vectơ phép đo cự ly R = [R₁, R₂, R₃]<sup>T</sup> bằng đa giác đạc. "
        "Một nghiệm chính xác và hiệu quả của phương trình đo phi tuyến đã được rút ra trong [15]. "
        "Cụ thể, độ cao được tính từ công thức dạng đóng:"))

    b.append(eq("z = g(R) = [−b(R) + √(b(R)² − 4a·d(R))]/(2a)", "10.37"))

    b.append(p("trong đó b(R) và d(R) là những hàm kiểu đa thức đơn giản sau:"))

    b.append(eq("b(R) = b₀ + b₁R₁ + b₂R₂² + b₃R₃²", "10.38"))
    b.append(eq("d(R) = d₀₀ + d₀₁R₁ + d₀₂R₂² + d₀₃R₃² + d₁₁R₁⁴ + d₂₂R₂⁴ + d₃₃R₃⁴ + d₁₂R₁²R₂² + "
                "d₁₃R₁²R₃² + d₂₃R₂²R₃²", "10.39"))

    b.append(p(
        "Các hệ số a, bᵢ, d<sub>ij</sub> được định nghĩa giải tích trong phần Phụ lục của [15]. Một "
        "khía cạnh quan trọng của các hệ số này là chúng được xác định hoàn toàn bởi toạ độ của các "
        "trạm mặt đất (xᵢ, yᵢ, zᵢ), vốn là cố định. Do đó các hệ số chỉ được tính một lần vào lúc "
        "máy bay đi vào vùng thu thập dữ liệu. Sau đó, mỗi khi có một tập phép đo cự ly mới, độ cao "
        "được tính từ các phương trình trên bằng cách dùng các phép đo cự ly và các hệ số đã lưu. "
        "Định nghĩa tỉ số σ<sub>z</sub>/σ<sub>R</sub> là VDOP của kỹ thuật này, với σ<sub>R</sub> là "
        "độ lệch chuẩn của sai số đo cự ly. VDOP bằng 1 trong trường hợp các trạm tạo thành một tam "
        "giác đều nội tiếp đường tròn bán kính 10 km và máy bay ở phía trên tâm tam giác với độ cao "
        "8 km."))

    b.append(fig(6, hb10fig.fig_10_6()))

    b.append(h4("Ước lượng vị trí thẳng đứng bằng hệ định vị toàn cầu (GPS)",
                "Estimation of Vertical Position with GPS"))

    b.append(p(
        "Việc nghiên cứu và phát triển GPS do Bộ Quốc phòng Hoa Kỳ điều phối. Một hệ tương tự khác "
        "là Hệ dẫn đường vệ tinh toàn cầu (GLONASS) do Liên Xô cũ phát triển. GPS là một hệ vệ tinh "
        "cung cấp cho người dùng thông tin định thời và cự ly chính xác. Hệ này được cung cấp cho "
        "người dùng dân sự với độ chính xác giảm bớt. Nhiều hãng, chủ yếu ở Hoa Kỳ, sản xuất máy thu "
        "GPS. Gọi (x, y, z) và (xᵢ, yᵢ, zᵢ) là toạ độ của người dùng và của vệ tinh sᵢ. Máy thu GPS "
        "của người dùng suy ra phép đo giả cự ly Dᵢ, và phương trình đo tương ứng là:"))

    b.append(eq("Dᵢ = Rᵢ + cT<sub>b</sub> = √[(x − xᵢ)² + (y − yᵢ)² + (z − zᵢ)²] + b = fᵢ(q)", "10.40"))

    b.append(p(
        "trong đó T<sub>b</sub> là độ lệch đồng hồ của người dùng, và q = [x, y, z, b]<sup>T</sup> là "
        "vectơ ẩn có chứa số hạng độ lệch b. Như vậy, để ước lượng vị trí ba chiều của máy bay, cần "
        "ít nhất bốn phép đo giả cự ly; do đó phải thấy được bốn vệ tinh từ máy thu. Tập N phép đo "
        "giả cự ly D = [D₁, D₂, …, D<sub>N</sub>]<sup>T</sup> xác định phương trình đo dạng ma trận "
        "sau:"))

    b.append(eq("D = f(q)", "10.41"))

    b.append(p("phương trình này được giải cho q bằng phương pháp lặp bình phương tối thiểu "
               "Gauss–Newton, tức là:"))

    b.append(eq("q̂<sub>k+1</sub> = q̂<sub>k</sub> + (A<sup>T</sup>WA)<sup>−1</sup>A<sup>T</sup>W"
                "[D − f(q̂<sub>k</sub>)]", "10.42"))

    b.append(p("trong đó A là ma trận đạo hàm riêng:"))
    b.append(eq("A = ∂f/∂q", "10.43"))

    b.append(p(
        "Các phần tử a<sub>xi</sub>, a<sub>yi</sub>, a<sub>zi</sub> của ma trận đạo hàm riêng A là các "
        "cosin chỉ hướng từ máy thu tới vệ tinh sᵢ. Ma trận trọng số là nghịch đảo của ma trận hiệp "
        "phương sai của các sai số đo giả cự ly, W<sup>−1</sup> = E(δD δD<sup>T</sup>). Trọng số nói "
        "chung được dùng để tính tới hiệu năng có thể khác nhau của từng vệ tinh, dù thường người ta "
        "giả thiết mọi vệ tinh có cùng hiệu năng, nghĩa là W = I. VDOP, được định nghĩa là "
        "σ<sub>z</sub>/σ<sub>D</sub>, phụ thuộc vào hình học, và hình học này biến đổi liên tục ngay "
        "cả khi máy thu đứng yên, bởi vì các vệ tinh không phải địa tĩnh mà chuyển động trên những "
        "quỹ đạo hoàn thành một vòng quay trong 12 giờ. Giá trị trung bình toàn cầu của VDOP vào "
        "khoảng 2 [16]. Các giá trị VDOP điển hình nằm trong khoảng 1,5 tới 7, tuỳ thuộc vùng đặt "
        "máy thu và thời điểm trong ngày. Sai số cự ly của dịch vụ định vị chính xác (chỉ dành cho "
        "người dùng quân sự Hoa Kỳ) được quy định nhỏ hơn 6 m (độ lệch chuẩn). Với dịch vụ định vị "
        "tiêu chuẩn, thường dành cho người dùng dân sự, sai số cự ly quy định gấp đôi (12 m, độ lệch "
        "chuẩn), còn sẽ vào khoảng 40 m khi Bộ Quốc phòng bật chế độ suy giảm chọn lọc. Các sai số "
        "cự ly đo được thực tế lại nhỏ hơn các giá trị quy định. Cụ thể, với ba điều kiện vận hành "
        "nêu trên, các giá trị sai số cự ly tương ứng đo được là 2,3 m, 6 m và 20 m [17]. Nhân độ "
        "lệch chuẩn của sai số cự ly với VDOP sẽ cho độ lệch chuẩn của sai số ước lượng độ cao."))

    b.append(p(
        "Để dự phòng sai số do Bộ Quốc phòng cố ý đưa vào, phương pháp GPS vi phân (DGPS) đã được "
        "phát triển. Một trạm đặt tại vị trí đã biết chính xác thu tín hiệu vệ tinh, tự tính vị trí "
        "của mình trên cơ sở các phép đo giả cự ly, so sánh vị trí ấy với vị trí đã biết để ước lượng "
        "sai số chứa trong tín hiệu vệ tinh, và cuối cùng phát các số hiệu chỉnh thích hợp tới những "
        "máy thu lân cận. Độ chính xác đạt được vào cỡ vài mét."))

    b.append(h3("Các vấn đề đặc biệt", "Special Topics"))

    b.append(p(
        "Việc phân tích hiệu năng của các hệ ước lượng tham số khác nhau thường chỉ giới hạn ở phân "
        "tích phương sai, và sai số ước lượng thường được giả thiết có kỳ vọng bằng không. Tuy "
        "nhiên, người ta đã chứng minh rằng trong tất cả các hệ nêu trên, sai số ước lượng không có "
        "kỳ vọng bằng không, do tính phi tuyến của phương trình đo. Một khía cạnh quan trọng khác là "
        "có những trường hợp không thể thu được nghiệm do hình học tương đối giữa máy bay và các "
        "trạm dẫn tới sai số lớn. Trong những trường hợp ấy, các vòng lặp liên tiếp dùng để giải hệ "
        "phương trình phi tuyến có thể không hội tụ. Và ngay cả sau khi hội tụ, nghiệm cũng không "
        "nhất thiết là nghiệm “tốt nhất” hay “đúng”."))

    b.append(h4("Độ lệch cố hữu", "Inherent Bias"))

    b.append(p(
        "Tính phi tuyến của các hệ, cộng với sai số ngẫu nhiên của phép đo, gây ra những ước lượng "
        "bị lệch một cách cố hữu, dù bản thân các đại lượng được đo là không lệch. Lấy ví dụ trường "
        "hợp ước lượng độ cao bằng các phép đo DME. Hàm g(R) trong phương trình 10.37, vốn xác định "
        "độ cao z, là phi tuyến. Ngoài ra, các phép đo cự ly sẽ bị nhiễm bẩn bởi các sai số ngẫu "
        "nhiên có kỳ vọng bằng không. Gọi R<sub>m</sub> là vectơ phép đo có nhiễu và z<sub>m</sub> là "
        "độ cao suy ra từ g(R<sub>m</sub>), nghĩa là từ hàm đo khi nó nhận đầu vào là các phép đo có "
        "nhiễu. Khai triển g(R<sub>m</sub>) thành chuỗi Taylor quanh các giá trị thực của cự ly R₁, "
        "R₂, R₃ tới số hạng bậc hai rồi lấy kỳ vọng, ta suy ra rằng kỳ vọng của z<sub>m</sub> sẽ "
        "không phải là giá trị thực z, mà lệch đi một lượng b<sub>z</sub>, gọi là độ lệch cố hữu. "
        "Cụ thể, với trường hợp DME, độ lệch cố hữu được tính là:"))

    b.append(eq("b<sub>z</sub> = E[z<sub>m</sub>] − z = ½(∂²g/∂R₁² σ₁² + ∂²g/∂R₂² σ₂² + "
                "∂²g/∂R₃² σ₃²)", "10.44"))

    b.append(p(
        "Hình 10-7 cho thấy độ lệch cố hữu sinh ra trong hệ DME. Độ lệch cố hữu càng lớn khi độ lớn "
        "của các sai số đo và tính phi tuyến của hệ càng mạnh. Sai số lệch này sinh ra một cách cố "
        "hữu trong mọi thuật toán ước lượng vị trí và phải được tính tới khi cần ước lượng vị trí "
        "chính xác. Ước lượng độ cao bị lệch cũng đã được báo cáo trong [18] cho hệ SSROR, trong "
        "[10] cho RDHMU, và trong [3] cho hệ NAMS."))

    b.append(fig(7, hb10fig.fig_10_7()))

    b.append(h4("Sự tồn tại và tính duy nhất của nghiệm vị trí",
                "Existence and Uniqueness of Position Fix"))

    b.append(p(
        "Ở một số hệ có những trường hợp kỳ dị mà tại đó không thể xác định được vị trí. Điều này đã "
        "được Abel và Chafee báo cáo cho hệ GPS trong [19], nơi người ta chỉ ra rằng với một số hình "
        "học tương đối giữa vệ tinh và máy bay, không thể giải được phương trình liên quan, hoặc có "
        "nhiều hơn một nghiệm. Cũng vậy, với RDHMU, Manolakis và Lefas đã chỉ ra rằng có những cách "
        "bố trí trạm mà tại đó không thể suy ra ước lượng độ cao khi máy bay ở những vùng xác định "
        "[11]. Chẳng hạn, với trường hợp bốn trạm, khi tứ giác do các trạm tạo thành nội tiếp một "
        "đường tròn, không thể ước lượng độ cao khi máy bay ở phía trên tâm. Cũng thế, khi tứ giác "
        "là một hình chữ nhật hoặc một hình thang cân, không thể suy ra nghiệm vị trí khi máy bay ở "
        "phía trên đường thẳng đi qua trung điểm hai cạnh song song. Từ góc độ toán học, sự kỳ dị "
        "này được biểu hiện bằng tính kỳ dị của ma trận Jacobian; do đó không thể nghịch đảo ma trận "
        "này như thuật toán ước lượng vị trí đòi hỏi. Trong trường hợp ấy thuật toán phân kỳ khỏi độ "
        "cao thực và cuối cùng sụp đổ. Lưu ý rằng ước lượng độ cao vẫn đạt được ở mọi nơi trừ đúng "
        "điểm kỳ dị ấy. Tuy nhiên, khi máy bay ở gần vùng kỳ dị, dù vẫn thu được nghiệm vị trí, "
        "nghiệm ấy không thực sự đáng tin vì bị ảnh hưởng bởi sai số lớn; chẳng hạn VDOP có thể lớn "
        "hơn 600 ở những vùng gần vùng kỳ dị."))

    b.append(p(
        "Bảng 10-1 liệt kê các viện và công ty hoặc nghiên cứu và phát triển những nguyên mẫu khối "
        "giám sát độ cao, hoặc cung cấp các hệ thống liên quan trên thị trường."))

    b.append(table(
        ["Hệ thống", "Công ty / Viện"],
        [["Hệ đo độ chính xác dẫn đường (NAMS)",
          "Viện Nghiên cứu Dẫn đường Điện tử, Bộ Giao thông<br>6-38-1 Shinkawa, Mitaka, Tokyo 181, "
          "Nhật Bản<br>ĐT: +81 422 413171 · Fax: 81-422-413176"],
         ["Khối giám sát độ cao DAMS",
          "Phòng thí nghiệm Hàng không Quốc gia NLR<br>Anthony Fokkerweg 2, 1059 CM Amsterdam, "
          "Hà Lan<br>ĐT: +31 (0)20 511 3113 · Fax: +31 (0)20 511 3210"],
         ["Kỹ thuật SSR và đa giác đạc bốn trạm",
          "GEC-Marconi Electronics Ltd., Marconi Research Laboratories<br>West Hanningfield Road, "
          "Great Baddow, Chelmsford, Essex, Anh"],
         ["Kỹ thuật SSR và TDOA (RDHMU)",
          "Roke Manor Research Ltd.<br>Roke Manor, Romsey, Hampshire SO51 0ZN, Anh<br>"
          "ĐT: +44(0)794 833000 · Fax: +44(0)794 833433"],
         ["Nhà cung cấp GPS",
          "Trimble Navigation, 585 North Mary Avenue, Sunnyvale, CA 94086<br>"
          "ĐT: (408) 730-2900<br>Trimble Navigation Europe Ltd., 79-81 High Str., West Malling, "
          "Kent ME19 6NA, Anh · ĐT: +44(0)732 849242"],
         ["Nhà cung cấp GPS",
          "Rockwell International, Digital Communication Division, 4311 Jamboree Road, Newport "
          "Beach, CA 92660-3095<br>ĐT: (714) 221-4600 · Fax: (714) 221-6375<br>"
          "Rockwell Semiconductor Systems, Berkshire Court, Western Road, Bracknell, Berkshire "
          "RG12 1RE, Anh · ĐT: +44(0)1344 48644"]],
        "Bảng 10-1 · Các hệ giám sát độ cao và những công ty, viện phát triển, cung cấp chúng. "
        "Thông tin giữ nguyên như bản gốc năm 1999, kể cả số điện thoại và fax, để làm mốc lịch sử.",
        " prod"))

    b.append(reflist([
        "S. Nagaoka, E. Yoshioka và P. T. Muto, “Radar estimation of the height of a cruising "
        "aircraft,” <em>J. Navigation</em>, 32(3), 352–356, 1979.",
        "S. Nagaoka, E. Yoshioka và P. T. Muto, “A simple radar for navigation accuracy "
        "measurements,” <em>J. Navigation</em>, 34(3), 462–469, 1981.",
        "S. Nagaoka, “Possibility of detecting a non-level-flight aircraft by the navigation "
        "accuracy measurement system (NAMS),” ICAO, Review of the General Concept of Separation "
        "Panel, kỳ họp 7, Montreal, RGCSP-WP/180, 30/10/1990.",
        "S. Nagaoka, “Height estimation of a cruising aircraft via a radar for air traffic "
        "control,” <em>Electronics and Communications in Japan</em>, Part 1 (Communications), "
        "71(11), 95–105, 1988.",
        "D. E. Manolakis, C. C. Lefas, G. S. Stavrakakis và C. M. Rekkas, “Computation of aircraft "
        "geometric height under radar surveillance,” <em>IEEE Trans. Aerosp. &amp; Electr. "
        "Systems</em>, AES-28(1), 241–248, 1992.",
        "D. E. Manolakis, “Computation of aircraft geometric height under radar surveillance for "
        "non level flights,” <em>Int. J. Systems Sci.</em>, 25(4), 619–627, 1994.",
        "J. Brugman, J. Verpoorte và A. J. L. Willekens, <em>DAMS Height Monitoring Unit — Phase "
        "One</em>, Report CR 92328 C, NLR, Hà Lan, 1992.",
        "D. E. Rice, “Height measurement by quadrilateration,” <em>The Marconi Review</em>, XLVI, "
        "(228), 1–17, 1983.",
        "S. Nagaoka, “Possibility of geometric height measurement by using secondary surveillance "
        "radars,” ICAO, Review of the General Concept of Separation Panel, kỳ họp 7, Montreal, "
        "RGCSP-WP/181, 30/10/1990.",
        "D. E. Manolakis và C. C. Lefas, “Aircraft geometric height computation using secondary "
        "surveillance radar range differences,” <em>IEEE Proc. — Radar, Sonar and Navigation</em>, "
        "141(2), 119–124, 1994.",
        "D. E. Manolakis và C. C. Lefas, “Station arrangement effects on ground referenced height "
        "computation by using time differences,” <em>Navigation, J. Inst. Navigation</em>, 42(2), "
        "409–420, 1995.",
        "L. G. Hopkins, D. Sherry và D. C. Rickard, <em>Geometric Height Monitor Unit (HMU) "
        "Programme — Final Report on Phase 1, Proof of Principles</em>, Roke Manor Research Ltd., "
        "Report No. 72/91/R161|U, Roke Manor, Anh, 1991.",
        "C. M. Rekkas, C. C. Lefas và N. J. Krikelis, “Improving the accuracy of aircraft absolute "
        "altitude estimation using DME measurements,” <em>Int. J. Systems Sci.</em>, 21(7), "
        "1381–1392, 1990.",
        "D. E. Manolakis, “Efficient solution and performance analysis of 3-D position estimation "
        "by trilateration,” <em>IEEE Trans. Aerosp. &amp; Electr. Systems</em>, AES-32(4), "
        "1239–1248, 1996.",
        "D. E. Manolakis và A. I. Dounis, “Advances in aircraft height computation using distance "
        "measuring equipment,” <em>IEEE Proc. — Radar, Sonar and Navigation</em>, 143(1), 47–52, "
        "1996.",
        "J. L. Leva, “Relationship between navigation vertical error, VDOP, and pseudorange error "
        "in GPS,” <em>IEEE Trans. Aerosp. &amp; Electr. Systems</em>, AES-30(4), 1138–1142, 1994.",
        "B. W. Parkinson, “History and operation of NAVSTAR, the Global Positioning System,” "
        "<em>IEEE Trans. Aerosp. &amp; Electr. Systems</em>, AES-30(4), 1145–1161, 1994.",
        "D. E. Manolakis, C. C. Lefas và A. I. Dounis, “Inherent bias in height computation "
        "employing mixed type radar data,” <em>IEEE Trans. Aerosp. &amp; Electr. Systems</em>, "
        "AES-30(4), 1045–1049, 1994.",
        "J. S. Abel và J. W. Chaffee, “Existence and uniqueness of GPS solutions,” <em>IEEE Trans. "
        "Aerosp. &amp; Electr. Systems</em>, AES-27(6), 952–956, 1991.",
    ]))

    # ------------------------------------------------------------ 10.2
    b.append(h2("10.2 Đo tư thế", "Attitude Measurement"))
    b.append(p("<em>Mark A. Stedham · Partha P. Banerjee · Seiji Nishifuji · Shogo Tanaka</em>"))

    b.append(p(
        "Trong nhiều tình huống thực tiễn, việc xác định và đo tư thế của một phương tiện cụ thể là "
        "điều quan trọng — chẳng hạn một con tàu, một máy bay, một thiết bị cơ khí như cần trục nâng, "
        "hay một tàu vũ trụ. Vì lý do đó, rất nhiều cảm biến tư thế đã được phát triển nhờ những tiến "
        "bộ về máy tính và công nghệ bán dẫn. Mục này trước hết giới thiệu các loại cảm biến tư thế "
        "cùng nguyên lý hoạt động của chúng, sau đó trình bày một số phương pháp đo và xác định tư "
        "thế, bao gồm các ứng dụng cho tàu thuỷ và cần trục nâng, cho máy bay, và cho tàu vũ trụ."))

    b.append(h3("Cảm biến tư thế cho tàu thuỷ, máy bay và cần trục nâng",
                "Attitude Sensors for Ships, Aircraft, and Crane Lifters"))

    b.append(p(
        "Có nhiều loại con quay hồi chuyển; tương ứng với cơ chế đo vật lý được dùng, chúng có thể "
        "được phân thành: con quay hai bậc tự do và con quay một bậc tự do dùng hiện tượng tiến động, "
        "con quay rung dùng lực Coriolis, và con quay quang dùng hiệu ứng Sagnac. Trong số đó, con "
        "quay hai bậc tự do có lịch sử lâu đời nhất. Nó gồm một rô to quay tốc độ cao quanh một trục "
        "quay được đỡ bởi hai trục trực giao. Loại con quay này thường được phân thành con quay tự "
        "do, con quay thẳng đứng (VG), hoặc con quay định hướng (DG)."))

    b.append(p(
        "Con quay một bậc tự do chỉ có một trục ra ngoài trục quay. Tuỳ theo đặc điểm thiết kế, có "
        "hai loại: con quay tốc độ và con quay tích phân tốc độ. Gần với các con quay kiểu quay này "
        "là một loại khác gọi là con quay tĩnh điện, dùng một quả cầu quay tốc độ cao trong một hốc "
        "chân không. Nhờ tính chất không có ma sát, con quay tĩnh điện có độ chính xác cao nhất "
        "trong số các con quay hiện có. Ngoài ra còn có các con quay không rô to. Loại thứ nhất là "
        "con quay rung dùng lực Coriolis làm nguyên lý đo. Loại thứ hai là con quay quang. Trong các "
        "con quay quang có hai kiểu: con quay vòng laser và con quay sợi quang. Cả hai đều dựa trên "
        "hiệu ứng Sagnac trong cơ chế đo. Hiệu năng của con quay được đánh giá bằng tốc độ trôi của "
        "nó, và hiệu năng của các loại con quay khác nhau được trình bày trong Bảng 10-2 để tham "
        "khảo, kèm theo công dụng chính của chúng."))

    b.append(p(
        "Gần đây, cùng với sự phát triển của công nghệ máy tính, nhiều loại con quay ba trục đã được "
        "phát triển, có thể đo không chỉ các góc nghiêng mà cả vận tốc góc và gia tốc theo ba trục "
        "bằng cách kết hợp một số con quay với gia tốc kế. Gia tốc kế thường được ghép với con quay "
        "để tạo ra các hệ dẫn đường bay và dẫn đường tàu biển, cũng như các cảm biến tư thế cho những "
        "vật động như cần trục nâng. Ví dụ gồm hệ quy chiếu tư thế và hướng (AHRS), hệ dẫn đường "
        "quán tính (INS), khối đo quán tính (IMU), và la bàn con quay (GC), cùng các VG và DG đã bàn "
        "ở trên [1]."))

    b.append(p(
        "Nguyên lý của một gia tốc kế kiểu servo được giải thích dưới đây (xem Hình 10-8). Ngay khi "
        "độ lệch của thanh dầm do gia tốc α gây ra được bộ thu độ lệch phát hiện, dòng điện i được "
        "bộ khuếch đại servo sinh ra, tạo một mô men giữ thanh dầm ở trục chính của cảm biến. Vì mô "
        "men và dòng điện sinh ra mô men tỉ lệ với α, nên có thể đo gia tốc qua dòng điện. Quá trình "
        "đo tạo thành một hệ kín, nhờ đó cảm biến không chỉ bền vững trước nhiễu mà còn đạt độ chính "
        "xác đo cao (xem Bảng 10-3)."))

    b.append(table(
        ["Loại con quay", "Bậc tự do", "Đại lượng được đo", "Độ chính xác (° h⁻¹)"],
        [["Con quay tự do", "2", "Góc", "1"],
         ["Con quay thẳng đứng", "2", "Độ lệch khỏi mặt phẳng ngang", "1"],
         ["Con quay định hướng", "2", "Độ lệch khỏi hướng chuẩn", "1"],
         ["Con quay tốc độ", "1", "Vận tốc góc", "10"],
         ["Con quay tích phân tốc độ", "1", "Góc", "0,001–1"],
         ["Con quay vòng laser", "1", "Vận tốc góc", "0,003"],
         ["Con quay sợi quang", "1", "Vận tốc góc", "0,01"],
         ["Con quay tĩnh điện", "2", "Góc", "0,00001–0,01"]],
        "Bảng 10-2 · Hiệu năng của các loại con quay khác nhau.", " prod"))

    b.append(fig(8, hb10fig.fig_10_8()))

    b.append(p(
        "Tương tự, một cảm biến độ nghiêng là một cảm biến quán tính khác, đo góc nghiêng để cung "
        "cấp thông tin tư thế (xem Hình 10-9). Nguyên lý của cảm biến độ nghiêng kiểu servo giống "
        "nguyên lý của gia tốc kế kiểu servo, chỉ khác là thanh dầm trong gia tốc kế được thay bằng "
        "một con lắc treo từ điểm đỡ trong cảm biến. Khi đặt cảm biến trên một mặt nghiêng tĩnh có "
        "góc nghiêng β, con lắc lệch một góc β so với trục chính của cảm biến, với giả thiết cảm biến "
        "không chịu lực nào khác ngoài trọng lực. Tuy nhiên cảm biến có thể sinh một mô men "
        "T<sub>c</sub> = mgl·sin β ≈ mglβ để giữ con lắc ở trục chính, và khi đó góc nghiêng β có "
        "thể được đo chính xác nhờ mô men ấy (và do đó nhờ dòng điện sinh ra mô men), trong đó m và "
        "l lần lượt là khối lượng con lắc và khoảng cách từ điểm treo tới khối tâm của nó. Cần lưu ý "
        "rằng một cảm biến như vậy về bản chất được thiết kế để đo góc nghiêng của những mặt nghiêng "
        "tĩnh. Do đó, khi áp dụng cho những mặt nghiêng động, các gia tốc sẽ ảnh hưởng tới mô men và "
        "làm cảm biến mất độ tin cậy. Một hệ cảm nhận tư thế thông minh khắc phục được khó khăn ấy "
        "sẽ được giới thiệu ở phần sau. Dù ứng dụng chỉ giới hạn ở những mặt nghiêng tĩnh với góc "
        "nghiêng rất nhỏ, một cảm biến độ nghiêng kiểu điện môi dùng các điện cực và một bọt khí giữ "
        "trong chất điện phân vẫn có thể đạt độ chính xác cao vào cỡ 10⁻⁴°."))

    b.append(table(
        ["Thông số", "Giá trị"],
        [["Dải đo", "±5 g"],
         ["Độ phân giải", "Nhỏ hơn 5 µg (một chiều)"],
         ["Độ nhạy", "2 V g⁻¹"],
         ["Điện trở ra", "560 Ω"],
         ["Dòng mô men", "3,5 mA g⁻¹"],
         ["Căn chỉnh vỏ", "Nhỏ hơn ±1°"],
         ["Đáp tuyến tần số", "450 Hz (±3 dB)"],
         ["Dải nhiệt độ", "−25 tới +70 °C"],
         ["Nguồn nuôi", "±15 V (một chiều)"],
         ["Dòng tiêu thụ", "Nhỏ hơn 15 mA"],
         ["Kích thước", "28,4 mm × 24,5 mm"],
         ["Khối lượng", "46 g (kể cả cáp 10 g)"]],
        "Bảng 10-3 · Đặc tính kỹ thuật của một gia tốc kế kiểu servo. Ghi chú: g là gia tốc trọng "
        "trường; số liệu theo mẫu TA-25D-05 của TOKIMEC.", " prod"))

    b.append(fig(9, hb10fig.fig_10_9()))

    b.append(h3("Cảm biến tư thế cho ứng dụng tàu vũ trụ",
                "Attitude Sensors for Spacecraft Applications"))

    b.append(p(
        "Việc đo tư thế tàu vũ trụ thường cần hai cảm biến trở lên để phát hiện các nguồn quy chiếu "
        "cần thiết nhằm thoả mãn yêu cầu về tư thế. Việc chọn dùng cảm biến nào chủ yếu chịu ảnh "
        "hưởng của hướng mà tàu vũ trụ thường hướng tới, cũng như yêu cầu độ chính xác của việc xác "
        "định tư thế [2]. Bảng 10-4 tóm tắt một số tham số hiệu năng của các cảm biến này cùng những "
        "nhà sản xuất điển hình."))

    b.append(table(
        ["Cảm biến", "Độ chính xác", "Khối lượng (kg)", "Nhà cung cấp điển hình"],
        [["IMU", "1 tới 5 × 10⁻⁶ g", "3 tới 25",
          "Northrop Grumman, Bendix, Kearfott, Honeywell, Hamilton Standard, Litton, Teledyne"],
         ["Cảm biến Mặt Trời", "10⁻² tới 3°", "0,5 tới 2", "Adcole, TRW, Ball Aerospace"],
         ["Cảm biến đường chân trời", "10⁻¹ tới 1°", "2 tới 5",
          "Barnes, Ithaco, Lockheed Martin, Lockheed Barnes"],
         ["Cảm biến sao", "10⁻³ tới 10⁻²°", "3 tới 7",
          "Ball Aerospace, Bendix, Honeywell, Hughes"],
         ["Từ kế", "0,5 tới 3°", "~1", "Schonstedt, Develco"]],
        "Bảng 10-4 · Các cảm biến xác định tư thế tàu vũ trụ. Trích từ Larson, W. J. và Wertz, J. R. "
        "(chủ biên), <em>Space Mission Analysis and Design</em>, Torrance, CA: Microcosm Inc. và "
        "Dordrecht, Hà Lan: Kluwer Academic Publishers, 1992, tr. 360.", " prod"))

    b.append(p(
        "Khối đo quán tính nói chung gồm các con quay ghép với các gia tốc kế, cùng nhau đo cả "
        "chuyển động quay lẫn chuyển động tịnh tiến. Các IMU này có thể được gắn trên giá treo các "
        "đăng (chuyển động quanh một điểm các đăng, độc lập với tàu vũ trụ), hoặc là hệ gắn cứng "
        "(gắn chặt vào thân tàu), khi đó phải dùng phần mềm phức tạp để chuyển đầu ra của cảm biến "
        "thành các phép đo trong hệ quy chiếu. IMU có xu hướng bị trôi con quay và các sai số lệch "
        "khác, và khi dùng để đo tư thế tàu vũ trụ, chúng thường được dùng kèm một hoặc nhiều cảm "
        "biến sẽ bàn dưới đây."))

    b.append(p(
        "Cảm biến Mặt Trời phát hiện ánh sáng khả kiến từ Mặt Trời, đo góc giữa bức xạ Mặt Trời và "
        "tế bào quang điện của đầu dò. Mặt Trời là nguồn quy chiếu tư thế thường được chọn vì nó là "
        "vật sáng nhất trên bầu trời cho tới nay, với tổng bức xạ trên một đơn vị diện tích là "
        "1353 W m⁻² tại khoảng cách của Trái Đất [3]. Ngoài ra, nó thường được chấp nhận như một "
        "nguồn điểm hợp lệ cho hầu hết ứng dụng tư thế, với bán kính góc 0,25° tại khoảng cách của "
        "Trái Đất. Có thể đạt độ chính xác đo cao hơn bằng cách xác định khối tâm của nó. Dù cảm "
        "biến Mặt Trời khá chính xác (0,01° tới 3,0°), chúng vẫn cần trường nhìn quang đãng, và đôi "
        "khi bị che tối trong những giai đoạn nhật thực do cả Trái Đất lẫn Mặt Trăng [4]. Ngoài ra, "
        "những thiết bị nhạy cảm (như thiết bị tạo ảnh) phải được bảo vệ khỏi bức xạ mạnh của ánh "
        "nắng trực tiếp. Khi có Mặt Trời, góc giữa nó và trục chính của cảm biến được gọi là góc Mặt "
        "Trời."))

    b.append(p(
        "Với tàu vũ trụ trên quỹ đạo gần Trái Đất, Trái Đất là vật sáng thứ hai trên bầu trời và "
        "chiếm tới 40% bầu trời. Cảm biến đường chân trời Trái Đất phát hiện mặt phân cách giữa rìa "
        "Trái Đất (hay cạnh Trái Đất) và nền không gian. Cảm biến đường chân trời có thể phát hiện "
        "cạnh khả kiến của Trái Đất (cảm biến suất phản chiếu), cạnh hồng ngoại, hoặc ánh sáng khí "
        "quyển. Cạnh hồng ngoại là ranh giới giữa Trái Đất ấm và nền không gian lạnh. Ánh sáng khí "
        "quyển là một vùng của khí quyển quanh Trái Đất mà tàu vũ trụ nhìn thấy được khi nó ở phía "
        "ban đêm của Trái Đất. Độ chính xác của cảm biến đường chân trời nằm trong khoảng 0,1° tới "
        "1,0°. Muốn chính xác hơn thì phải mô hình hoá Trái Đất như một ellipsoid dẹt [4]. Một số "
        "vấn đề gắn với việc phát hiện suất phản chiếu gồm: hiệu ứng méo hình của khí quyển Trái "
        "Đất; việc nhầm đường ranh giới ngày/đêm thành cạnh thật của Trái Đất; và độ biến thiên đáng "
        "kể của suất phản chiếu Trái Đất trong vùng khả kiến (khác nhau giữa đất liền, biển và "
        "băng)."))

    b.append(p(
        "Phần lớn cảm biến dùng để phát hiện đường chân trời Trái Đất là cảm biến quét có trường nhìn "
        "hẹp, đo khoảng thời gian giữa các lần cắt đường chân trời. Nói chung, mỗi chu kỳ quét của "
        "cảm biến có hai lần cắt đường chân trời: lần thứ nhất khi cảm biến quét từ nền không gian "
        "vào Trái Đất, tiếp theo là lần thứ hai khi cảm biến quét từ Trái Đất trở ra không gian. Tổ "
        "hợp các thời điểm cắt đường chân trời, tốc độ quét và độ cao của tàu vũ trụ cho phép tính "
        "bán kính góc biểu kiến của Trái Đất. Bán kính góc biểu kiến sẽ nhỏ hơn bán kính góc thực "
        "(hay vật lý) nếu tàu vũ trụ nghiêng đi khỏi vectơ thiên đỉnh. Vectơ thiên đỉnh được định "
        "nghĩa là vectơ nối tâm tàu vũ trụ với tâm Trái Đất. Để thấy hiệu ứng này, cần tính bán kính "
        "vật lý ρ của Trái Đất, mà với một độ cao h cho trước của tàu vũ trụ (tính bằng kilômét), "
        "được cho bởi ρ = sin⁻¹[6371/(6371 + h)]. Nếu cảm biến đường chân trời hướng đúng thiên đỉnh, "
        "thì bán kính góc biểu kiến do cảm biến đo sẽ khớp với bán kính vật lý tính theo quan hệ "
        "trên. Tuy nhiên, nếu cảm biến hướng ra khỏi thiên đỉnh, các thời điểm cắt đường chân trời sẽ "
        "sớm hơn so với khi hướng đúng thiên đỉnh. Điều này dẫn tới một bán kính góc biểu kiến nhỏ "
        "hơn bán kính vật lý một lượng tỉ lệ với góc giữa trục cảm biến và vectơ thiên đỉnh. Góc này "
        "được gọi là góc thiên đỉnh."))

    b.append(p(
        "Cảm biến sao được dùng khi yêu cầu độ chính xác cực cao. Độ chính xác cao này (0,003° tới "
        "0,01°) chủ yếu nhờ vào bản chất nguồn điểm và vị trí cố định chính xác của các ngôi sao "
        "trong không gian. Cảm biến sao có thể được phân thành bộ bám sao hoặc bộ lập bản đồ sao. Bộ "
        "bám sao dùng trường nhìn rộng để tìm một ngôi sao có độ sáng xác định. Bộ lập bản đồ sao "
        "tương tự bộ bám sao, chỉ khác là nó quét qua nhiều ngôi sao, ghi lại vị trí tương đối và "
        "khoảng cách góc giữa chúng. Bằng cách so sánh dữ liệu ghi được với dữ liệu từ một danh mục "
        "sao (cơ sở dữ liệu), có thể thu được định hướng chính xác của tàu vũ trụ. Góc giữa đường "
        "ngắm tới sao và trục chính của cảm biến được gọi là góc sao."))

    b.append(p(
        "Tuy nhiên, độ chính xác của cảm biến sao phải trả bằng chi phí cao hơn. Cảm biến sao nói "
        "chung nặng hơn và tiêu thụ nhiều điện năng hơn các loại cảm biến tư thế khác. Ngoài ra, cảm "
        "biến sao khá nhạy với các nguồn sáng lạc, như ánh nắng phản xạ từ tàu vũ trụ hoặc từ Trái "
        "Đất, và ánh nắng tán xạ từ các hạt bụi và khí thải động cơ phản lực [4]. Phần lớn chúng dựa "
        "vào che chắn quang học để giảm ảnh hưởng của ánh sáng lạc."))

    b.append(p(
        "Cảm biến từ (gọi là từ kế) đo cả độ lớn lẫn hướng của từ trường Trái Đất. Độ lệch về định "
        "hướng giữa từ trường đo được và từ trường thật được chuyển thành việc xác định tư thế. Độ "
        "chính xác của từ kế (0,5° tới 3,0°) thường kém hơn các loại cảm biến khác vì có sự không "
        "chắc chắn về từ trường thật của Trái Đất, vốn có xu hướng thay đổi hay dịch chuyển theo "
        "thời gian. Ngoài ra, từ trường Trái Đất giảm khi độ cao tăng, và từ kế nói chung bị giới "
        "hạn ở độ cao khoảng 6000 km. Vì lý do đó, từ kế thường được dùng kèm một trong những loại "
        "cảm biến khác đã bàn để cải thiện độ chính xác đo [2]."))

    b.append(h3("Đo tư thế tự động trực tuyến cho tàu thuỷ và cần trục nâng",
                "Automatic On-Line Attitude Measurement for Ships and Crane Lifters"))

    b.append(p(
        "Với việc đo tư thế trực tuyến cho tàu thuỷ và cần trục nâng, điều đầu tiên nghĩ tới là dùng "
        "con quay. Tuy nhiên, vì chúng thường bị trôi, có thể không đạt được phép đo tư thế chính "
        "xác nếu chỉ dùng con quay. Theo đó, người ta dùng những hệ đo tư thế trực tuyến không dùng "
        "con quay mà dùng gia tốc kế kiểu servo và cảm biến độ nghiêng. Triết lý của các hệ đo được "
        "giới thiệu ở đây là tận dụng tối đa động lực học của đối tượng và của cảm biến, rồi áp dụng "
        "lọc Kalman hoặc lọc thích nghi để đạt độ chính xác đo cao."))

    b.append(h4("Đo tư thế tàu thuỷ", "Attitude Measurement for Ships"))

    b.append(p(
        "Việc đo chính xác tư thế con tàu theo thời gian thực là cực kỳ quan trọng khi cần khảo sát "
        "chính xác địa hình đáy biển bằng sonar [5, 6]. Nó cũng là yêu cầu của những con tàu hiệu "
        "năng cao như tàu đệm khí, xét từ góc độ khử dao động do sóng. Việc đo tư thế con tàu "
        "thường có thể quy về việc đo chuyển động nhấp nhô, lắc ngang và lắc dọc của tàu. Với phép "
        "đo như vậy, người ta đã dùng một cảm biến nhấp nhô, có đầu ra là tích phân hai lần đầu ra "
        "của một gia tốc kế hướng thẳng đứng cùng với một con quay. Tuy nhiên, vì giá trị ban đầu "
        "của độ dịch chuyển nhấp nhô và vận tốc của nó là chưa biết, đầu ra sẽ chứa một độ lệch tăng "
        "dần theo thời gian, và độ chính xác của cảm biến suy giảm đáng kể. Từ góc độ đó, người ta "
        "đưa ra một hệ đo trực tuyến kiểu gắn cứng, xử lý thoả đáng đầu ra của hai cảm biến độ "
        "nghiêng kiểu servo và một gia tốc kế gắn trên tàu [7]."))

    b.append(h4("Vị trí các cảm biến và đầu ra", "Location of Sensors and Outputs"))

    b.append(p(
        "Hai cảm biến độ nghiêng kiểu servo và một gia tốc kế kiểu servo được đặt trên boong (tại "
        "điểm A) cách O — giao điểm của trục lắc ngang và trục lắc dọc — một khoảng thẳng đứng L "
        "(xem Hình 10-10). Hai cảm biến độ nghiêng được đặt sao cho đo được lần lượt góc lắc ngang và "
        "góc lắc dọc. Gia tốc kế được đặt hướng lên theo boong để thu thông tin về chuyển động nhấp "
        "nhô. Vì cảm biến độ nghiêng vốn được phát triển để đo góc nghiêng của những mặt nghiêng "
        "tĩnh, con lắc cứng bên trong cảm biến chịu ảnh hưởng đáng kể của gia tốc con tàu, ngoài "
        "gia tốc trọng trường. Áp dụng phương trình chuyển động Lagrange [8, 9] cho các con lắc cứng "
        "và tính mô men cần thiết để giữ độ lệch của chúng khỏi các trục chính gần như bằng không, "
        "ta thu được đầu ra của cảm biến [7]:"))

    b.append(eq("z₁(t) = θ(t) − (L/g)·θ̈(t) + v₁(t)", "10.45"))
    b.append(eq("z₂(t) = p(t) − (L/g)·p̈(t) + v₂(t)", "10.46"))

    b.append(p(
        "trong đó z₁(t), z₂(t), θ(t), p(t) và g lần lượt là đầu ra của hai cảm biến độ nghiêng, góc "
        "lắc ngang, góc lắc dọc và gia tốc trọng trường (v₁(t) và v₂(t) là nhiễu của các đầu ra, kể "
        "cả sai số xấp xỉ khi rút ra các đầu ra ấy)."))

    b.append(p("Mặt khác, đầu ra của gia tốc kế được biểu diễn là:"))

    b.append(eq("z₃(t) = (g + α(t))·cos θ(t)·cos p(t) + v₃(t)", "10.47"))

    b.append(p("trong đó α(t) và v₃(t) lần lượt biểu diễn gia tốc nhấp nhô và nhiễu của gia tốc kế."))

    b.append(fig(10, hb10fig.fig_10_10()))

    b.append(h4("Động lực học của các tín hiệu tư thế", "Dynamics of Attitude Signals"))

    b.append(p(
        "Ai cũng biết rằng mỗi chuyển động nhấp nhô, lắc ngang và lắc dọc ở vùng biển ven bờ đều có "
        "hai sóng trội trong một khoảng thời gian ngắn. Đó là một sóng hình sin có chu kỳ dài (trong "
        "khoảng 6 s tới 10 s) và một sóng hình sin có chu kỳ ngắn (trong khoảng 2 s tới 3 s) [10–12]. "
        "Vì vậy, mỗi tín hiệu trong một khoảng ngắn được mô hình hoá bằng một sóng tổ hợp của hai "
        "sóng hình sin trội ấy. Với chuyển động nhấp nhô (trong một khoảng ngắn), độ dịch chuyển được "
        "mô hình hoá bằng:"))

    b.append(eq("x(t) = a₁sin(ω₁t + φ₁) + a₂sin(ω₂t + φ₂)", "10.48"))

    b.append(p(
        "với các tham số {aᵢ}, {φᵢ} và {ωᵢ} chưa biết. Từ phương trình vi phân bậc bốn mà x(t) thoả "
        "mãn, ta thu được phương trình động học tuyến tính [7]:"))

    b.append(eq("ẋ(t) = Ax(t),  A = [0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1; −ω₁²ω₂², 0, "
                "−(ω₁² + ω₂²), 0]", "10.49"))

    b.append(p(
        "trong đó x(t) ≡ (x₁, x₂, x₃, x₄)<sup>T</sup>, với x<sub>n</sub> = d<sup>n−1</sup>x/"
        "dt<sup>n−1</sup> (n = 1, …, 4). Mặt khác, các góc lắc ngang và lắc dọc có thể được mô hình "
        "hoá bằng:"))

    b.append(eq("x(t) = a₁sin(ω₁t + φ₁) + a₂sin(ω₂t + φ₂) + b", "10.50"))

    b.append(p(
        "bởi vì thường có một số độ lệch gắn với chúng. Từ phương trình vi phân bậc năm mà phương "
        "trình 10.50 thoả mãn, ta thu được biểu diễn biến trạng thái tương tự của mô hình như phương "
        "trình 10.49. Trong thực tế, các tín hiệu nhấp nhô, lắc ngang và lắc dọc có nhiều sóng hình "
        "sin không trội bên cạnh những sóng trội. Vì vậy, phương trình 10.49 được sửa đổi bằng cách "
        "đưa vào một nhiễu Gauss trắng w(t) có kỳ vọng bằng không và phương sai σ² thích hợp như "
        "sau:"))

    b.append(eq("ẋ(t) = Ax(t) + Γw(t)", "10.51"))

    b.append(p(
        "trong đó Γ = (0, 1, 0, 0)<sup>T</sup> cho chuyển động nhấp nhô và Γ = (0, 1, 0, 0, "
        "0)<sup>T</sup> cho chuyển động lắc ngang và lắc dọc. Bậc của mô hình càng cao thì độ chính "
        "xác đo càng tốt. Nếu chỉ xét việc đo trực tuyến các tín hiệu, phương trình 10.51 là đủ."))

    b.append(h4("Đo tư thế trực tuyến", "On-Line Attitude Measurement"))

    b.append(p(
        "Các phương trình quan sát 10.45 và 10.46 được biểu diễn bằng vectơ trạng thái x(t) riêng của "
        "chúng. Các phương trình quan sát ở dạng rời rạc là:"))

    b.append(eq("y<sub>k</sub> = Hx<sub>k</sub> + v<sub>k</sub>", "10.52"))

    b.append(p(
        "trong đó H = [1, 0, −L/g, 0, 0], và y<sub>k</sub>, x<sub>k</sub>, v<sub>k</sub> lần lượt ký "
        "hiệu y(t), x(t) và v(t) của các tín hiệu tương ứng tại thời điểm lấy mẫu thứ k [7, 9]. Dạng "
        "rời rạc của phương trình động học 10.51 là:"))

    b.append(eq("x<sub>k+1</sub> = Fx<sub>k</sub> + w<sub>k</sub>", "10.53"))

    b.append(p("trong đó"))
    b.append(eq("F ≡ Φ(ΔT),  Φ(t) ≡ L<sup>−1</sup>{(sI − A)<sup>−1</sup>}", "10.54"))

    b.append(p(
        "Ở đây L<sup>−1</sup> và ΔT lần lượt ký hiệu phép biến đổi Laplace ngược và chu kỳ lấy mẫu. "
        "Nhiễu chuyển tiếp rời rạc w<sub>k</sub> trở thành nhiễu Gauss trắng có kỳ vọng bằng không và "
        "hiệp phương sai:"))

    b.append(eq("W = σ²∫₀<sup>ΔT</sup>Φ(ΔT − τ)ΓΓ<sup>T</sup>Φ<sup>T</sup>(ΔT − τ)dτ", "10.55"))

    b.append(p(
        "Như vậy việc đo góc lắc ngang và lắc dọc có thể quy về bài toán ước lượng trạng thái của "
        "các hệ động học rời rạc tuyến tính (phương trình 10.52 và 10.53), nếu các tần số góc ω₁ và "
        "ω₂ đã biết và v<sub>k</sub> được giả thiết có tính chất Gauss trắng. Việc ước lượng trạng "
        "thái được thực hiện bằng lọc Kalman [7, 13]. Tuy nhiên, khó khăn khi triển khai bộ lọc là "
        "giá trị chính xác của hai tần số góc chưa biết trước và còn biến thiên theo thời gian. Để "
        "khắc phục, người ta đặt ra những ứng viên thích hợp {(ω₁<sup>i</sup>, ω₂<sup>i</sup>); "
        "1 ≤ i ≤ M} cho các tham số {ω₁, ω₂} và dùng một tập hợp bộ lọc Kalman song song. Khi đó ước "
        "lượng cuối cùng thu được là kỳ vọng có điều kiện của các ước lượng trạng thái như sau:"))

    b.append(eq("x̂<sub>k/k</sub> ≡ Σ<sub>i=1..M</sub> p<sub>k</sub><sup>i</sup> "
                "x̂<sub>k/k</sub><sup>i</sup>", "10.56"))

    b.append(p(
        "trong đó x̂<sub>k/k</sub><sup>i</sup> là ước lượng trạng thái x̂<sub>k/k</sub> ứng với ứng "
        "viên thứ i, Ω<sup>i</sup> = (ω₁<sup>i</sup>, ω₂<sup>i</sup>), và p<sub>k</sub><sup>i</sup> "
        "là xác suất hậu nghiệm có điều kiện của ứng viên thứ i, được tính theo định lý Bayes:"))

    b.append(eq("p<sub>k</sub><sup>i</sup> = p(y<sub>k</sub>|Ω<sup>i</sup>, Y<sup>k−1</sup>)"
                "·p<sub>k−1</sub><sup>i</sup> / Σ<sub>j=1..M</sub> "
                "p(y<sub>k</sub>|Ω<sup>j</sup>, Y<sup>k−1</sup>)·p<sub>k−1</sub><sup>j</sup>", "10.57"))

    b.append(p(
        "Ở đây p(y<sub>k</sub>|Ω<sup>i</sup>, Y<sup>k−1</sup>) biểu diễn hàm mật độ xác suất Gauss có "
        "điều kiện của y<sub>k</sub> với điều kiện Ω<sup>i</sup> và Y<sup>k−1</sup>; {y<sub>j</sub>; "
        "j ≤ k − 1}, với kỳ vọng và phương sai được tính đệ quy [7]."))

    b.append(p(
        "Hệ đo được đề xuất có thể tự động và thích nghi chọn ứng viên phù hợp nhất theo thời gian. "
        "Nhờ đó nó cho phép đo trực tuyến chính xác góc lắc ngang và lắc dọc, những đại lượng có tần "
        "số góc trội biến thiên theo thời gian. Thành phần thứ nhất, thứ hai và thứ ba của ước lượng "
        "cuối cùng x̂<sup>o</sup><sub>k/k</sub> lần lượt biểu diễn ước lượng độ dịch chuyển, vận tốc "
        "và gia tốc. Như vậy hệ được đề xuất có ưu điểm là đo được không chỉ độ dịch chuyển mà cả vận "
        "tốc và gia tốc của ba tín hiệu. Để cải thiện độ chính xác đo góc lắc ngang và lắc dọc, nên "
        "đặt các cảm biến độ nghiêng gần giao điểm O của trục lắc ngang và trục lắc dọc."))

    b.append(p(
        "Cuối cùng, động lực học của chuyển động nhấp nhô được cho bởi phương trình 10.51, tương tự "
        "như của chuyển động lắc ngang và lắc dọc. Thay các ước lượng θ̂(t) và p̂(t) thu được ở trên "
        "vào phương trình 10.47 rồi trừ đi ảnh hưởng của gia tốc trọng trường, ta rút ra được một "
        "phương trình quan sát tuyến tính cho α(t):"))

    b.append(eq("y<sub>k</sub> = [z₃(t) − g·cos θ̂(t)·cos p̂(t)]<sub>t=kΔT</sub> = "
                "H<sub>k</sub>x<sub>k</sub> + v<sub>k</sub>", "10.58"))

    b.append(p(
        "trong đó H<sub>k</sub> = [0, 0, cos θ̂(t)·cos p̂(t), 0]<sub>t=kΔT</sub> và v<sub>k</sub> = "
        "v₃(kΔT). Như vậy việc đo trực tuyến chuyển động nhấp nhô cũng được thực hiện bằng đúng thủ "
        "tục đã mô tả ở trên. Vị trí các trục lắc ngang và lắc dọc đã được giả thiết là biết trước; "
        "tuy nhiên, ngay cả khi chúng chưa biết, hệ đo tư thế mô tả ở trên vẫn hiệu quả, miễn là ta "
        "đưa thêm các ứng viên về vị trí các trục bên cạnh các tần số góc."))

    b.append(h4("Đo tư thế cần trục nâng", "Attitude Measurement for Crane Lifters"))

    b.append(h4("Động lực học của các tín hiệu tư thế", "Dynamics of Attitude Signals"))

    b.append(p(
        "Hình 10-11 trình bày sơ đồ minh hoạ một hệ cần trục nâng. Một trong những cách dễ nhất để đo "
        "tư thế của bộ nâng là đặt một camera phân giải cao ở đáy xe con và bám một dấu mốc trên đỉnh "
        "bộ nâng. Tuy nhiên cách này làm tăng chi phí và cả khó khăn bảo trì. Hơn nữa, đôi khi sơ đồ "
        "ấy không hoạt động vì bóng tối và phản xạ ánh sáng. Như đã nói ở trên, với những con quay "
        "không cho phép đo đủ chính xác, người ta dùng một gia tốc kế kiểu servo có độ nhạy cao để "
        "trích ra các tín hiệu tư thế. Tuy nhiên, khi đặt cảm biến trên bộ nâng, có thêm một tín hiệu "
        "dao động thứ cấp bên cạnh tín hiệu sơ cấp, do bộ nâng được treo tự do và do kết cấu của nó. "
        "Dù biên độ nhỏ, tín hiệu thứ cấp có tần số cao hơn và vì thế có độ lớn đáng kể trên đầu ra "
        "cảm biến. Tín hiệu quan trọng cho các ứng dụng thực tiễn, như điều khiển tư thế bộ nâng, là "
        "tín hiệu sơ cấp, vốn có biên độ lớn hơn với tần số góc thấp hơn ω = √(g/ℓ) (g là gia tốc "
        "trọng trường; ℓ là độ dài dây từ điểm treo sơ cấp tới khối tâm của ròng rọc). Nếu ta tìm "
        "cách làm suy giảm tín hiệu dao động thứ cấp bằng cách cho đầu ra đi qua một bộ lọc thông "
        "thấp, thì độ trễ pha cũng bị đưa vào tín hiệu dao động sơ cấp, và tín hiệu không còn dùng "
        "được để điều khiển tư thế bộ nâng một cách chính xác nữa."))

    b.append(p(
        "Vì những lý do trên, chúng tôi đưa ra một hệ đo tự trị đo cả dao động sơ cấp lẫn thứ cấp "
        "bằng cách mô hình hoá hệ cần trục nâng thành một con lắc kép rồi áp dụng lọc Kalman [14]. "
        "Động lực học của hệ xe con – bộ nâng được rút ra bằng phương trình chuyển động Lagrange "
        "[8, 9]."))

    b.append(eq("(d/dt)(∂T/∂ẋ) − ∂T/∂x + ∂V/∂x = u − aẋ", "10.59"))
    b.append(eq("(d/dt)(∂T/∂θ̇<sub>i</sub>) − ∂T/∂θ<sub>i</sub> + ∂V/∂θ<sub>i</sub> = 0,  i = 1, 2",
                "10.60"))

    b.append(p(
        "trong đó T và V lần lượt biểu diễn động năng và thế năng của hệ xe con – bộ nâng, còn "
        "θ₁, θ₂ lần lượt là các góc mà con lắc sơ cấp và con lắc thứ cấp tạo với đường thẳng đứng. "
        "Các biến còn lại x, u và a lần lượt biểu diễn vị trí xe con, lực dẫn động, và hệ số ma sát "
        "giữa xe con với đường ray. Xét rằng θ<sub>i</sub>, θ̇<sub>i</sub> (1 ≤ i ≤ 2) là nhỏ, phương "
        "trình động học của hệ xe con – bộ nâng có thể được viết là [14]:"))

    b.append(eq("ẋ(t) = Ax(t) + bu(t)", "10.61"))

    b.append(p(
        "trong đó x(t) là vectơ trạng thái x(t) = (x, ẋ, θ₁, θ̇₁, θ₂, θ̇₂)<sup>T</sup>. Tính tới các "
        "sai số xấp xỉ khi rút ra phương trình 10.61, sức cản không khí, ma sát trong các dây, và "
        "những dao động vi mô tại các điểm nối khác, việc đưa vào các nhiễu Gauss trắng wᵢ(t) "
        "(1 ≤ i ≤ 3) có kỳ vọng bằng không và phương sai thích hợp cho phương trình động học 10.61 "
        "là hợp lý, giống như ở phương trình 10.49, cụ thể là [14]:"))

    b.append(eq("ẋ(t) = Ax(t) + bu(t) + Γw(t)", "10.62"))

    b.append(p("trong đó"))
    b.append(eq("Γ = [0, 1, 0, 0, 0, 0; 0, 0, 0, 1, 0, 0; 0, 0, 0, 0, 0, 1]<sup>T</sup>,  "
                "w(t) = [w₁(t), w₂(t), w₃(t)]<sup>T</sup>", "10.62a"))

    b.append(fig(11, hb10fig.fig_10_11()))

    b.append(h4("Đầu ra của cảm biến và phép đo tư thế trực tuyến",
                "Sensor Outputs and On-Line Attitude Measurement"))

    b.append(p(
        "Khi một gia tốc kế kiểu servo được đặt trên bộ nâng (theo hướng dao động) tại vị trí cách "
        "điểm treo thứ cấp một khoảng ℓ′₂, đầu ra của cảm biến trở thành [14]:"))

    b.append(eq("y(t) ≅ −ẍ − ℓ′₁θ̈₁ − ℓ′₂θ̈₂ − g·θ₂", "10.63"))

    b.append(p(
        "trong đó ℓ′₁ là khoảng cách giữa điểm treo sơ cấp và điểm treo thứ cấp (xem Hình 10-12). "
        "Thay phương trình 10.61 vào phương trình 10.63 sẽ cho một đầu ra biểu diễn theo vectơ trạng "
        "thái x(t), giống như ở phương trình 10.52. Dùng một bộ mã hoá quay để đo vị trí và vận tốc "
        "của xe con, rồi kết hợp ba đầu ra cảm biến này với phương trình động học 10.62 và áp dụng "
        "lọc Kalman, ta có thể ước lượng vectơ trạng thái theo thời gian thực. Với cách tiếp cận "
        "này, có thể đo chính xác cả độ dịch chuyển góc lẫn vận tốc góc của các dao động θ₁, θ₂ của "
        "hai con lắc."))

    b.append(fig(12, hb10fig.fig_10_12()))

    b.append(h3("Xác định tư thế máy bay", "Aircraft Attitude Determination"))

    b.append(p(
        "Việc xác định tư thế máy bay đòi hỏi đo các góc quanh ba trục thân máy bay độc lập. Các góc "
        "ấy là góc lắc ngang, góc chúc ngóc và góc hướng. Ngày nay có hai phương tiện chính để đo "
        "các góc này; phương pháp thứ nhất dùng VG để đo góc lắc ngang và góc chúc ngóc, và một DG để "
        "đo góc hướng. Phương pháp thứ hai, thông dụng hơn hiện nay, dùng một IMU để xác định tư thế "
        "đầy đủ ba trục, ghép với một khí áp kế đo độ cao để hiệu chỉnh sai số trôi thẳng đứng của "
        "IMU. Cả hai phương pháp được mô tả dưới đây."))

    b.append(h4("Phân tích con quay thẳng đứng và con quay định hướng",
                "Vertical and Directional Gyro Analysis"))

    b.append(p(
        "VG là một con quay hai bậc tự do với trục quay được gắn danh định theo phương thẳng đứng. Nó "
        "dùng hai cảm biến lực riêng được gắn danh định nằm ngang trên giá trong. Hai góc mà VG đo — "
        "góc lắc ngang và góc chúc ngóc — cần những phân tích gần như đồng nhất [1]. Xét tình huống "
        "trình bày trên Hình 10-13, mô tả một máy bay có góc lắc ngang φ so với phương thẳng đứng "
        "địa phương. Góc lắc ngang cảm nhận được φ<sub>s</sub> được cho bởi hiệu giữa góc lắc ngang "
        "thực và sai số trôi lắc ngang của con quay φ<sub>Δ</sub>:"))

    b.append(eq("φ<sub>s</sub> = φ − φ<sub>Δ</sub>", "10.64"))

    b.append(p(
        "Để bù sai số trôi này, con quay dùng một cảm biến lực riêng, chẳng hạn một thiết bị bọt "
        "điện phân, vốn cảm nhận được sai số trôi. Thiết bị hiệu chỉnh này cảm nhận hiệu góc giữa "
        "vectơ lực riêng f tác dụng lên trục lắc ngang của máy bay và trục con quay, như trình bày "
        "trên Hình 10-13. Như vậy:"))

    b.append(eq("φ = tan<sup>−1</sup>(f<sub>φ</sub>/f<sub>v</sub>) − φ<sub>Δ</sub> ≅ "
                "f<sub>φ</sub>/f<sub>v</sub> − φ<sub>Δ</sub>", "10.65"))

    b.append(p(
        "trong đó f<sub>φ</sub> là thành phần nằm ngang theo phương ngang của f, và f<sub>v</sub> = "
        "lực hấp dẫn là thành phần thẳng đứng. Một phân tích tương tự cho góc chúc ngóc θ cho:"))
    b.append(eq("θ<sub>s</sub> = θ − θ<sub>Δ</sub>", "10.66"))
    b.append(eq("θ = tan<sup>−1</sup>(f<sub>θ</sub>/f<sub>v</sub>) − θ<sub>Δ</sub> ≅ "
                "f<sub>θ</sub>/f<sub>v</sub> − θ<sub>Δ</sub>", "10.67"))

    b.append(p(
        "trong đó f<sub>θ</sub> là thành phần nằm ngang theo phương dọc của f. Tiếp theo, định nghĩa "
        "vectơ mô men động lượng của con quay là:"))

    b.append(eq("H<sub>VG</sub> = [−J<sub>x</sub>φ̇<sub>Δ</sub>, −J<sub>y</sub>θ̇<sub>Δ</sub>, h]",
                "10.68"))

    b.append(p(
        "trong đó J<sub>x</sub> và J<sub>y</sub> là mô men quán tính của cảm biến và h là mô men động "
        "lượng quay của con quay. Ngoài ra, định nghĩa vectơ vận tốc góc của các trục giá trong là:"))

    b.append(eq("ω<sub>VG</sub> = [φ̇<sub>Δ</sub>, θ̇<sub>Δ</sub>, 0]", "10.69"))

    b.append(p("Cuối cùng, định nghĩa vectơ mô men của các đăng là:"))

    b.append(eq("Q<sub>VG</sub> = [Q<sub>cx</sub> + Q<sub>dx</sub>, Q<sub>cy</sub> + Q<sub>dy</sub>, "
                "0]", "10.70"))

    b.append(p("trong đó"))
    b.append(eq("Q<sub>cx</sub> = k<sub>c</sub>θ<sub>B</sub> = mô men điều khiển lắc ngang của các "
                "đăng", "10.71a"))
    b.append(eq("Q<sub>cy</sub> = k<sub>c</sub>φ<sub>B</sub> = mô men điều khiển chúc ngóc của các "
                "đăng", "10.71b"))
    b.append(eq("Q<sub>dx</sub> = −k<sub>d</sub>(φ̇ + φ̇<sub>Δ</sub>) = mô men nhiễu lắc ngang của "
                "các đăng (cộng mô men ngẫu nhiên)", "10.71c"))
    b.append(eq("Q<sub>dy</sub> = −k<sub>d</sub>(θ̇ + θ̇<sub>Δ</sub>) = mô men nhiễu chúc ngóc của "
                "các đăng (cộng mô men ngẫu nhiên)", "10.71d"))

    b.append(p(
        "và k<sub>c</sub>, k<sub>d</sub> là những hệ số tỉ lệ hằng gắn với từng thành phần mô men. "
        "Dùng các vectơ định nghĩa trong phương trình 10.68 tới 10.70, phương trình chuyển động của "
        "con quay được cho bởi:"))

    b.append(eq("(∂/∂t)(H<sub>VG</sub>) + ω<sub>VG</sub> × H<sub>VG</sub> = Q<sub>VG</sub>", "10.72"))

    b.append(p(
        "Lấy biến đổi Laplace của khai triển phương trình 10.72, với giả thiết J<sub>x</sub> ≅ "
        "J<sub>y</sub> = J, ta thu được phương trình chuyển động của con quay trong miền Laplace:"))

    b.append(eq("[J<sub>x</sub>s² + k<sub>c</sub> − hs, k<sub>c</sub>(s) + h; hs, J<sub>y</sub>s² + "
                "k<sub>c</sub>]·[φ(s); θ(s)] ≅ [k<sub>c</sub>φ<sub>B</sub>(s) + k<sub>d</sub>s·φ(s); "
                "k<sub>c</sub>θ<sub>B</sub>(s) + k<sub>d</sub>s·θ(s)] + [mô men ngẫu nhiên; "
                "mô men ngẫu nhiên]", "10.73"))

    b.append(p(
        "Với chế độ làm việc bình thường của con quay, J<sub>x</sub> ≅ J<sub>y</sub> ≅ 0 và "
        "k<sub>d</sub>/h ≪ 1; do đó có thể bỏ qua các nhân tố này trong phương trình 10.73. Khi ấy, "
        "giải cho các góc lắc ngang và chúc ngóc mong muốn dưới những giả thiết ấy cho [1]:"))

    b.append(eq("φ<sub>s</sub> = φ + (k<sub>c</sub>/(hω<sub>c</sub>))[f<sub>φ</sub>/g − "
                "φ̇<sub>Δ</sub>/ω<sub>c</sub>]", "10.74"))
    b.append(eq("θ<sub>s</sub> = θ + (k<sub>c</sub>/(hω<sub>c</sub>))[f<sub>θ</sub>/g − "
                "θ̇<sub>Δ</sub>/ω<sub>c</sub>]", "10.75"))

    b.append(p(
        "DG là một con quay hai bậc tự do với trục quay được gắn danh định nằm ngang và hướng theo "
        "phương bắc từ. Nó dùng một cảm biến lực riêng duy nhất gắn trên giá trong [1]. DG đo góc "
        "thứ ba cần thiết của máy bay, góc hướng, thường được ký hiệu là ψ. Góc hướng cảm nhận được "
        "ψ<sub>s</sub> được cho bởi hiệu giữa góc hướng thực ψ (góc giữa trục z của máy bay và phương "
        "bắc thật) với sai số trôi góc hướng của con quay ψ<sub>Δ</sub> (góc giữa trục con quay và "
        "phương bắc thật):"))

    b.append(eq("ψ<sub>s</sub> = ψ − ψ<sub>Δ</sub>", "10.76"))

    b.append(p("Định nghĩa vectơ mô men động lượng của con quay là:"))
    b.append(eq("H<sub>DG</sub> = [−J<sub>y</sub>θ̇<sub>Δ</sub>, −J<sub>z</sub>ψ̇<sub>Δ</sub>, h]",
                "10.77"))

    b.append(p("và vectơ vận tốc góc của các trục giá trong là:"))
    b.append(eq("ω<sub>DG</sub> = [θ̇<sub>Δ</sub>, ψ̇<sub>Δ</sub>, 0]", "10.78"))

    b.append(p("và vectơ mô men của các đăng là"))
    b.append(eq("Q<sub>DG</sub> = [Q<sub>cy</sub> + Q<sub>dy</sub>, Q<sub>cz</sub> + "
                "Q<sub>dz</sub>, 0]", "10.79"))

    b.append(p("Ở đây các thành phần của vectơ mô men được cho bởi:"))
    b.append(eq("Q<sub>cy</sub> = −k<sub>c</sub>(M<sub>Δ</sub> − ψ<sub>Δ</sub>)", "10.80a"))
    b.append(eq("Q<sub>cz</sub> = −k<sub>c</sub>θ<sub>B</sub>", "10.80b"))
    b.append(eq("Q<sub>dy</sub> = −k<sub>d</sub>(θ̇ + θ̇<sub>Δ</sub>) + mô men ngẫu nhiên", "10.80c"))
    b.append(eq("Q<sub>dz</sub> = −k<sub>d</sub>(ψ̇ + ψ̇<sub>Δ</sub>) + mô men ngẫu nhiên", "10.80d"))

    b.append(p(
        "trong đó M<sub>Δ</sub> = sai số hướng của la bàn từ (so với phương bắc thật). Do đó, phương "
        "trình chuyển động của DG trong miền Laplace được cho là:"))

    b.append(eq("[J<sub>y</sub>s² + k<sub>c</sub> − hs, k<sub>c</sub>; hs, J<sub>z</sub>s² + "
                "k<sub>c</sub>]·[θ(s); ψ(s)] ≅ [k<sub>c</sub>M<sub>Δ</sub>(s) + k<sub>d</sub>s·θ(s); "
                "k<sub>c</sub>θ<sub>B</sub>(s) + k<sub>d</sub>s·ψ(s)] + [mô men ngẫu nhiên; "
                "−k·mô men ngẫu nhiên]", "10.81"))

    b.append(p("Phép đo góc hướng mong muốn của DG do đó được cho là [1]:"))
    b.append(eq("ψ<sub>s</sub> = ψ + (k<sub>c</sub>/(hω<sub>c</sub>))[M<sub>Δ</sub> − "
                "ψ̇<sub>Δ</sub>/ω<sub>c</sub>]", "10.82"))

    b.append(p(
        "Như đã chỉ ra trong Bảng 10-2, độ chính xác của cả VG lẫn DG đều vào khoảng 1°. Có thể đạt "
        "được sự cải thiện hơn hai bậc độ lớn nhờ dùng các khối đo quán tính, sẽ được mô tả tiếp "
        "theo."))

    b.append(h4("Khối đo quán tính (IMU)", "Inertial Measurement Units"))

    b.append(p(
        "Khối đo quán tính gồm các con quay và các gia tốc kế, cùng nhau cung cấp phép đo tư thế đầy "
        "đủ ba trục. Phần lớn được gắn trên những bệ các đăng ổn định, giữ được phương ngang địa "
        "phương nhờ các thiết bị tạo mô men. Một IMU trên máy bay không thể đo chính xác phương thẳng "
        "đứng địa phương, do lực riêng tác dụng lên máy bay có một thành phần nằm ngang vì máy bay "
        "đang chuyển động. Ngoài ra, vì phương tiện chuyển động so với hệ quy chiếu quán tính, không "
        "thể xác định chính xác cực từ của Trái Đất [1]."))

    b.append(p(
        "Những vấn đề (sai số) này được giảm tới mức tối thiểu bằng cách căn chỉnh IMU sao cho nằm "
        "đúng phương ngang và hướng đúng phương bắc trong khi máy bay đứng yên. Khi bệ bắt đầu "
        "chuyển động, có thể liên tục căn chỉnh lại IMU bằng cách cảm nhận sự thay đổi hướng của "
        "phương thẳng đứng và phương bắc, rồi tác dụng những mô men thích hợp lên bệ để giữ nó căn "
        "chỉnh đúng. Việc căn chỉnh lại này được thực hiện bằng cách tích phân hai đầu ra trực giao "
        "của các gia tốc kế để xác định các thành phần vận tốc ngang. Dữ liệu này, kết hợp với tốc "
        "độ quay của Trái Đất, cho ra tốc độ thay đổi mong muốn của phương thẳng đứng địa phương và "
        "phương bắc thật tại vĩ độ và kinh độ hiện tại của phương tiện. Thực hiện tích phân lần thứ "
        "hai các đầu ra cảm biến sẽ cho ước lượng vị trí tương đối."))

    b.append(p(
        "Phân tích trong Bryson và cộng sự [1] đã chỉ ra rằng góc chúc ngóc (biến thiên vị trí ngang "
        "của bệ) được cho bởi đầu ra cảm biến IMU là:"))

    b.append(eq("θ(t) = −(ε/ω<sub>s</sub>)(t − sin ω<sub>s</sub>t) − (b/g)", "10.83"))

    b.append(p(
        "trong đó ε = sai số tốc độ trôi con quay, b = sai số cảm biến lực riêng, và ω<sub>s</sub> ≡ "
        "tần số Schuler = √(g/R) [g = lực hấp dẫn, R = bán kính Trái Đất]. Như vậy, giá trị hiệu dụng "
        "của góc chúc ngóc của bệ trở thành:"))

    b.append(eq("θ<sub>rms</sub> = [(ε/ω<sub>s</sub>)² + (b/g)²]<sup>1/2</sup>", "10.84"))

    b.append(p(
        "Dùng những giá trị điển hình cho ε (>0,015° h⁻¹), ω<sub>s</sub> (>0,71° h⁻¹) và b (>0,01) "
        "cho ra sai số góc chúc ngóc hiệu dụng θ<sub>rms</sub> = 0,01°. Như vậy rõ ràng là trong điều "
        "kiện vận hành bình thường, IMU cho độ chính xác cảm biến tốt hơn VG và DG hai bậc độ lớn."))

    b.append(fig(13, hb10fig.fig_10_13()))

    b.append(h3("Xác định tư thế tàu vũ trụ", "Spacecraft Attitude Determination"))

    b.append(p(
        "Phần lớn kỹ thuật xác định tư thế tàu vũ trụ dựa vào việc tìm định hướng của một trục duy "
        "nhất trong không gian (chẳng hạn trục z của tàu) cộng với góc quay của tàu quanh trục ấy. "
        "Điều đó cho một nghiệm tư thế đầy đủ ba trục. Để làm được vậy, phải dùng những nguồn quy "
        "chiếu bên ngoài tàu vũ trụ. Cụ thể, việc xác định tư thế đầy đủ ba trục cần ít nhất hai "
        "phép đo vectơ bên ngoài. Những nguồn quy chiếu thường dùng cho các phép đo vectơ bên ngoài "
        "ấy gồm Mặt Trời, Trái Đất, Mặt Trăng, các ngôi sao, các hành tinh và từ trường Trái Đất. "
        "Ngoài ra, IMU cũng được dùng để cung cấp những phép đo tư thế cần thiết."))

    b.append(fig(14, hb10fig.fig_10_14()))

    b.append(h4("Phương pháp xác định tư thế", "Attitude Determination Methodology"))

    b.append(p(
        "Bước đầu tiên trong việc xác định tư thế là xác định các góc giữa trục chính của tàu vũ trụ "
        "và hai (hoặc nhiều hơn) nguồn quy chiếu tư thế. Chẳng hạn, giả sử một tàu vũ trụ dùng Mặt "
        "Trời và Trái Đất làm quy chiếu tư thế. Hai góc trong trường hợp này được gọi là góc Mặt Trời "
        "β<sub>S</sub> và góc thiên đỉnh Γ<sub>N</sub>. Vì tại thời điểm này ngay cả định hướng của "
        "một trục duy nhất của tàu cũng chưa biết, các góc ấy xác lập hai hình nón mà vectơ tư thế A "
        "phải nằm trên đó. Vì vectơ tư thế phải nằm trên cả hai hình nón, nó phải nằm dọc theo giao "
        "tuyến của hai hình nón [4] (xem Hình 10-14). Hai vectơ, cụ thể là A₁ và A₂, sinh ra từ giao "
        "tuyến của hai hình nón này có thể được xác định bằng phương pháp sau đây do Grubin rút ra "
        "[15]. Gọi S là vectơ Mặt Trời, E là vectơ thiên đỉnh của tàu, và A là vectơ tư thế mong "
        "muốn, mỗi vectơ được định nghĩa trong không gian Descartes như sau:"))

    b.append(eq("S = (S<sub>x</sub>, S<sub>y</sub>, S<sub>z</sub>)", "10.85"))
    b.append(eq("E = (E<sub>x</sub>, E<sub>y</sub>, E<sub>z</sub>)", "10.86"))
    b.append(eq("A = (A<sub>x</sub>, A<sub>y</sub>, A<sub>z</sub>)", "10.87"))

    b.append(p("Gọi các vectơ S, E và N xác định một bộ vectơ đơn vị cơ sở với:"))
    b.append(eq("N = (S × E)/|S × E| = (N<sub>x</sub>, N<sub>y</sub>, N<sub>z</sub>)", "10.88"))

    b.append(p("Nếu đưa vào một bộ hệ số tỉ lệ thích hợp như sau:"))
    b.append(eq("I<sub>x</sub> = [cos β − (S·E)cos Γ]/(1 − (S·E)²)<sup>1/2</sup>", "10.89a"))
    b.append(eq("I<sub>y</sub> = [cos Γ − (S·E)cos β]/(1 − (S·E)²)<sup>1/2</sup>", "10.89b"))
    b.append(eq("I<sub>z</sub> = ±√(1 − I<sub>x</sub>cos β − I<sub>y</sub>cos Γ)", "10.89c"))

    b.append(p("thì hai vectơ tư thế khả dĩ A₁ và A₂ được tìm thấy là:"))
    b.append(eq("A<sub>1,2</sub> = (I<sub>x</sub>S<sub>x</sub> ± I<sub>y</sub>E<sub>x</sub> ± "
                "I<sub>z</sub>N<sub>x</sub>, I<sub>x</sub>S<sub>y</sub> ± I<sub>y</sub>E<sub>y</sub> "
                "± I<sub>z</sub>N<sub>y</sub>, I<sub>x</sub>S<sub>z</sub> ± I<sub>y</sub>E<sub>z</sub> "
                "± I<sub>z</sub>N<sub>z</sub>)", "10.90"))

    b.append(p(
        "Trong các phương trình 10.88 tới 10.90, S × E biểu diễn tích vectơ Descartes, và S · E biểu "
        "diễn tích vô hướng Descartes. Biểu thức dưới căn trong phương trình 10.89c có thể âm, do đó "
        "sinh ra những giá trị ảo cho I<sub>z</sub> mỗi khi hai hình nón không cắt nhau. Những trường "
        "hợp như vậy thường được quy cho sai số cảm biến hoặc dao động nhiễu ngẫu nhiên. Khi ấy, có "
        "thể cộng một độ lệch cảm biến định trước vào cả hai cảm biến để “mở rộng” góc của các hình "
        "nón, nhờ đó buộc hai hình nón phải cắt nhau."))

    b.append(p(
        "Cần lưu ý rằng với hầu hết ứng dụng xác định tư thế tàu vũ trụ, hệ toạ độ chính được dùng là "
        "hệ toạ độ thiên cầu. Hệ toạ độ này có trục z trùng với trục cực của Trái Đất, và trục x "
        "trùng với giao tuyến của mặt phẳng xích đạo Trái Đất với mặt phẳng quỹ đạo Trái Đất quanh "
        "Mặt Trời (tức là trùng với điểm phân vernal). Trong hệ toạ độ này, mọi vectơ được coi là "
        "vectơ đơn vị và hai phép đo chính mô tả vị trí của một vectơ là xích kinh và xích vĩ, ký "
        "hiệu lần lượt là Ω và Δ. Như vậy, vectơ Mặt Trời S và vectơ thiên đỉnh Trái Đất E dùng trong "
        "phương trình 10.85 và 10.86 nói chung sẽ được cho dưới dạng xích kinh và xích vĩ, có thể "
        "chuyển sang toạ độ Descartes qua tập biến đổi sau:"))

    b.append(eq("x = cos Ω·cos Δ;  y = sin Ω·cos Δ;  z = sin Δ", "10.91a"))
    b.append(eq("Ω = tan<sup>−1</sup>(y/x);  Δ = sin<sup>−1</sup>(z)", "10.91b"))

    b.append(p(
        "Bước cuối cùng trong việc đo tư thế ba trục là xác định nghiệm tư thế nào là đúng, A₁ hay "
        "A₂, rồi đo góc quay quanh trục ấy. Hai nghiệm tư thế nhập nhằng có thể được phân giải bằng "
        "cách so sánh với thông tin tư thế biết trước, nếu có, hoặc bằng phương pháp lấy trung bình "
        "vết [4]. Lấy trung bình vết là phương pháp vẽ từng nghiệm tư thế trên một đồ thị xích kinh "
        "– xích vĩ rồi chọn vùng tập trung dày nhất làm nghiệm đúng, như minh hoạ trên Hình 10-15. Vì "
        "tư thế được giả thiết thay đổi chậm hơn tốc độ lấy mẫu của cảm biến tư thế, trong những "
        "khoảng thời gian ngắn dữ liệu của nghiệm đúng thường tạo thành một “cụm” quanh tư thế đúng; "
        "còn dữ liệu của nghiệm sai thường tản mát hơn nhiều."))

    b.append(fig(15, hb10fig.fig_10_15()))

    b.append(p(
        "Khi đã thu được vectơ tư thế đúng, có thể tìm định hướng của hai trục trực giao còn lại "
        "bằng cách đo góc quay, hay góc pha, của tàu vũ trụ quanh trục ưu tiên. Có thể dùng bất kỳ "
        "phép đo cảm biến nào cung cấp góc pha này. Một ví dụ về kỹ thuật ấy là hệ xác định tư thế "
        "dùng thấu kính vòng toàn cảnh (PALADS), được mô tả ở mục tiếp theo. Hệ tạo ảnh này dùng một "
        "thấu kính “ba chiều” độc đáo, cho phép phát hiện đồng thời hai (hoặc nhiều hơn) nguồn quy "
        "chiếu [16]. Thông tin này, kết hợp với định hướng của trục đơn, xác định duy nhất tư thế ba "
        "trục."))

    b.append(p(
        "Ba góc rút ra ở trên, thường được gọi là góc Euler, xác định định hướng của ba trục tàu vũ "
        "trụ so với hệ quy chiếu đã chọn. Một cách xử lý hình thức hơn cho nghiệm tư thế thường đòi "
        "hỏi phải chỉ rõ các thành phần của ma trận tư thế 3 × 3, ký hiệu A. Mỗi thành phần của ma "
        "trận tư thế xác định quan hệ góc giữa một trục cho trước của tàu và một trục của hệ quy "
        "chiếu. Có nhiều phương pháp tính ma trận tư thế A (xem [4]); phương pháp được ưu tiên phụ "
        "thuộc vào ứng dụng cụ thể trước mắt."))

    b.append(h3("PALADS"))
    b.append(p(
        "Thành phần chính của PALADS là thấu kính vòng toàn cảnh (PAL), một thấu kính đơn làm từ "
        "thuỷ tinh có chiết suất cao với một số phần của thấu kính được phủ một mặt phản xạ. Do đó nó "
        "dựa vào cả khúc xạ lẫn phản xạ khi tạo ảnh (Hình 10-16). Thấu kính này độc đáo ở chỗ nó tạo "
        "ảnh một trường vật thể ba chiều lên một mặt phẳng ảnh hai chiều, trong khi một thấu kính "
        "“bình thường” chỉ có khả năng tạo ảnh không gian vật hai chiều lên mặt phẳng ảnh. Sự kết "
        "hợp của thuỷ tinh chiết suất cao với các mặt phản xạ cho PAL một trường nhìn mở rộng từ "
        "khoảng 65° tới 110° tính từ trục quang. Trường nhìn 45° này bao trùm toàn bộ 360° quanh "
        "trục quang [17]. Mọi tia sáng xuất phát từ ngoài trường nhìn 45° sẽ không tạo thành một "
        "phần của ảnh. Có thể gắn PAL vào bất kỳ hệ tạo ảnh chất lượng cao nào nhờ một thấu kính "
        "truyền thích hợp. Với cấu hình hiện tại, hệ tạo ảnh PALADS dùng một thiết bị ghép điện tích "
        "(CCD) Sony XC-73, một camera video đen trắng ghép với PAL qua một thấu kính truyền Nikon "
        "f/1,4."))

    b.append(fig(16, hb10fig.fig_10_16()))

    b.append(p(
        "Trường nhìn bán cầu mà PALADS cung cấp cho phép một cảm biến duy nhất phát hiện nhiều nguồn "
        "quy chiếu tư thế, chẳng hạn Trái Đất và Mặt Trời hoặc Mặt Trăng. Vị trí của mỗi nguồn quy "
        "chiếu trên mặt phẳng ảnh tương ứng với một góc phương vị – độ cao duy nhất giữa trục quang "
        "của PAL và nguồn quy chiếu. Vì PAL có trường nhìn 360° quanh trục quang, nó có thể phát hiện "
        "đồng thời nhiều nguồn quy chiếu. Các điểm dữ liệu gắn với từng nguồn được trích ra khỏi mặt "
        "phẳng ảnh bằng các kỹ thuật xử lý ảnh số. Như vậy dễ thấy rằng một ảnh duy nhất từ PALADS "
        "(chứa hai hay nhiều nguồn quy chiếu) cung cấp đủ dữ liệu góc cần thiết để xác định tư thế ba "
        "trục của tàu vũ trụ."))

    b.append(reflist([
        "A. E. Bryson, <em>Control of Spacecraft and Aircraft</em>, ch. 10, Princeton, NJ: Princeton "
        "University Press, 1994.",
        "W. J. Larson và J. R. Wertz (chủ biên), <em>Space Mission Analysis and Design</em>, ch. 11, "
        "Torrance, CA: Microcosm Inc. và Dordrecht, Hà Lan: Kluwer Academic Publishers, 1992.",
        "NASA Technical Memorandum NASA TM X-64757, <em>Terrestrial Environment (Climatic) Criteria "
        "Guidelines for Use in Aerospace Vehicle Development (1973 Revision)</em>, Marshall Space "
        "Flight Center, AL, 1973.",
        "J. R. Wertz (chủ biên), <em>Spacecraft Attitude Determination and Control</em>, ch. 11 và "
        "12, Hà Lan: Reidel Publishing Company, 1980.",
        "R. D. Angelari, “A deterministic and random error model for a multibeam hydrographic sonar "
        "system,” <em>Proc. OCEANS’78, The Ocean Challenge</em>, 1978, 48–53.",
        "C. de Moustier, T. Hylas và J. C. Phillips, “Modifications and improvements to the Sea Beam "
        "system on board R/V Thomas Washington,” <em>Proc. OCEANS’88 — A Partnership of Marine "
        "Interests</em>, 1988, 372–378.",
        "S. Tanaka và S. Nishifuji, “Automatic on-line measurement of ship’s attitude by use of a "
        "servo-type accelerometer and inclinometers,” <em>IEEE Trans. Instrum. Meas.</em>, 45, "
        "209–217, 1996.",
        "D. G. Shultz và J. L. Melsa, <em>State Functions and Linear Control Systems</em>, New York: "
        "McGraw-Hill, 1967.",
        "Y. Takahashi, M. J. Rabins và D. M. Auslander, <em>Control and Dynamic Systems</em>, "
        "Reading, MA: Addison-Wesley, 1971.",
        "S. Tanaka và S. Nishifuji, “On-line sensing system of dynamic ship’s attitude by use of "
        "servo-type accelerometers,” <em>IEEE J. Oceanic Eng.</em>, 20, 339–346, 1995.",
        "S. Tanaka, “On automatic attitude measurement system for ships using servo-type "
        "accelerometers” (tiếng Nhật), <em>Trans. SICE</em>, 27, 861–869, 1991.",
        "D. E. Cartwright và M. S. Longuet-Higgins, “The statistical distribution of the maxima of a "
        "random function,” <em>Proc. Roy. Soc. London</em>, Ser. A, 237, 212–232, 1956.",
        "R. E. Kalman, “A new approach to linear filtering and prediction problems,” <em>Trans. "
        "ASME, J. Basic Eng.</em>, 82, 35–45, 1960.",
        "S. Tanaka, S. Kouno và H. Hayashi, “Automatic measurement and control of attitude for crane "
        "lifters” (tiếng Nhật), <em>Trans. SICE</em>, 32(1), 97–105, 1996.",
        "C. Grubin, “Simple algorithm for intersecting two conical surfaces,” <em>J. Spacecraft "
        "Rockets</em>, 14(4), 251–252, 1977.",
        "M. A. Stedham và P. P. Banerjee, “The panoramic annular lens attitude determination "
        "system,” <em>SPIE Proceedings, Space Guidance, Control, and Tracking II</em>, Orlando, FL, "
        "17–18/4/1995.",
        "J. A. Gilbert, D. R. Matthys và P. Greguss, “Optical measurements through panoramic imaging "
        "systems,” <em>Proc. Int. Conf. Hologram Interferometry and Speckle Metrology</em>, "
        "Baltimore, MD, 4–7/11/1990.",
    ]))

    # ------------------------------------------------------------ 10.3
    b.append(h2("10.3 Dẫn đường quán tính", "Inertial Navigation"))
    b.append(p("<em>Halit Eren · C. C. Fung</em>"))

    b.append(h3("Nguyên lý", "The Principles"))
    b.append(p(
        "Nghĩa nguyên thuỷ của từ “navigation” là “lái tàu”. Vào thời cổ, khi người ta còn dùng "
        "thuyền buồm, dẫn đường là quá trình lái con tàu theo một nguồn thông tin định hướng nào đó "
        "và điều chỉnh buồm để khống chế tốc độ. Mục tiêu là đưa con tàu từ vị trí A tới vị trí B an "
        "toàn. Ngày nay, dẫn đường là một tổ hợp của khoa học và công nghệ. Thuật ngữ không còn bó "
        "hẹp trong việc điều khiển một con tàu trên mặt biển; nó được áp dụng cho đất liền, trên "
        "không, mặt biển, dưới nước và trong không gian."))

    b.append(p(
        "Khái niệm cơ cấu hoá một bộ dẫn đường quán tính được Schuler đề xuất lần đầu tại Đức năm "
        "1923. Hệ dẫn đường mà ông đề nghị dựa trên một con lắc có chiều dài bằng bán kính Trái Đất. "
        "Tuy vậy, hệ dẫn đường quán tính đầu tiên dựa trên gia tốc lại do Boykow đề xuất năm 1938. "
        "Tên lửa A-4 của Đức, vào giai đoạn cuối Thế chiến thứ hai, đã dùng một hệ dẫn đường quán "
        "tính dựa trên các con quay kiểu dụng cụ bay để điều khiển và ổn định tư thế. Trong hệ đó, "
        "các gia tốc kế tích phân kiểu con quay – con lắc gắn lên thân đảm nhận việc xác định vận tốc "
        "dọc theo quỹ đạo. Hệ tự dẫn đường quán tính đầu tiên hoạt động hoàn chỉnh ở Hoa Kỳ là XN-1, "
        "phát triển năm 1950 để dẫn tên lửa C-47. Hiện nay, các hệ dẫn đường quán tính đã phát triển "
        "đầy đủ cả về lý thuyết lẫn công nghệ. Chúng có mặt trong rất nhiều ứng dụng, cho phép chọn "
        "đúng thiết bị theo tiêu chí chi phí, độ chính xác, giao diện người dùng, độ phủ toàn cầu, độ "
        "trễ thời gian, tính tự trị…"))

    b.append(p(
        "Dẫn đường quán tính là kỹ thuật dùng một hệ tự thân để đo chuyển động của phương tiện và "
        "xác định xem nó đã đi được bao xa kể từ điểm xuất phát. Gia tốc là một đại lượng vectơ, gồm "
        "độ lớn và hướng. Một gia tốc kế đơn lẻ chỉ đo được độ lớn chứ không đo được hướng; thông "
        "thường nó đo thành phần gia tốc dọc theo một đường hay một hướng định trước. Thông tin về "
        "hướng thường do con quay hồi chuyển cung cấp, vì con quay tạo ra hệ quy chiếu cho các gia "
        "tốc kế. Khác với những phương pháp định vị khác phải dựa vào các mốc bên ngoài, một hệ dẫn "
        "đường quán tính (INS) gọn nhẹ và tự thân, vì nó không cần liên lạc với bất kỳ trạm hay mốc "
        "nào khác. Chính tính chất này cho phép phương tiện dẫn đường được trong một vùng lãnh thổ "
        "chưa ai biết."))

    b.append(p(
        "Có thể mô tả dẫn đường quán tính như quá trình điều khiển chuyển động của xe, tên lửa, tàu "
        "thuỷ, máy bay, rô-bốt… từ điểm này tới điểm khác, quy chiếu theo một trục chuẩn. Vị trí hiện "
        "thời của phương tiện xác định được bằng “tính vị trí theo quãng đường đã đi” (dead reckoning) "
        "so với một vị trí gốc đã biết trước. Trên mặt Trái Đất, hệ quy chiếu thông dụng là Bắc – "
        "Đông – Xuống, gọi là các trục cố định Trái Đất. Một phương tiện như máy bay hay tàu biển lại "
        "có bộ trục cục bộ của riêng nó: lắc ngang (roll), chúi (pitch) và hướng (yaw), như trên "
        "Hình 10-17."))

    b.append(fig(17, hb10fig.fig_10_17()))

    b.append(p(
        "Các cảm biến quán tính của INS có thể được gắn theo cách để chúng luôn nằm ngang và luôn "
        "hướng về một phương cố định. Hệ này dựa vào một bộ gimbal và các cảm biến gắn trên ba trục "
        "để theo dõi góc ở mọi thời điểm; đó là kiểu INS dựa trên bệ dẫn đường. Hình 10-18 phác hoạ "
        "một bệ ba trục. Một kiểu INS khác là hệ gắn cứng (strapdown), loại bỏ hẳn gimbal: con quay "
        "và gia tốc kế được gắn chặt lên kết cấu phương tiện, và các phép đo được thực hiện theo bộ "
        "trục cục bộ lắc ngang – chúi – hướng. Con quay đo chuyển động góc trên ba trục trong những "
        "khoảng thời gian ngắn, ví dụ 100 mẫu mỗi giây; máy tính sau đó dùng thông tin này để phân "
        "giải đầu ra của các gia tốc kế về hệ trục dẫn đường. Hình 10-19 là sơ đồ khối của hệ gắn "
        "cứng."))

    b.append(fig(18, hb10fig.fig_10_18()))
    b.append(fig(19, hb10fig.fig_10_19()))

    b.append(p(
        "Tác động điều khiển dựa trên việc cảm nhận gia tốc của phương tiện theo những hướng không "
        "gian đã biết, bằng các dụng cụ hiện thực hoá các định luật chuyển động của Newton. Tích phân "
        "bậc nhất của gia tốc cảm nhận được cho vận tốc, tích phân bậc hai cho vị trí. Một INS điển "
        "hình gồm một bộ con quay, một bộ gia tốc kế và các khối xử lý tín hiệu thích hợp. Nguyên lý "
        "của hệ có thể đơn giản, nhưng để chế tạo một hệ thực dụng lại đòi hỏi một nền tảng công nghệ "
        "tinh vi. Độ chính xác của hệ không phụ thuộc độ cao, địa hình hay các biến vật lý khác, mà "
        "gần như chỉ bị giới hạn bởi độ chính xác của chính các linh kiện trong hệ."))

    b.append(p(
        "INS truyền thống chủ yếu dựa vào con quay và gia tốc kế cơ khí, nhưng ngày nay có nhiều loại "
        "khác nhau: con quay quang học, con quay rung áp điện, con quay cộng hưởng chủ động và thụ "
        "động… Các con quay và gia tốc kế chế tạo bằng công nghệ vi cơ cũng đang tạo ảnh hưởng quan "
        "trọng lên các hệ dẫn đường quán tính hiện đại. Dưới đây trình bày vắn tắt nguyên lý hoạt "
        "động của các loại con quay và gia tốc kế phù hợp cho dẫn đường quán tính."))

    b.append(p(
        "Những tiến bộ lớn của INS qua các năm gắn với sự ra đời của con quay tĩnh điện (ESG) và con "
        "quay la-de. Trong ESG, rô-to quay với tốc độ trên 200 × 10<sup>3</sup> vòng/phút trong môi "
        "trường gần chân không. Rô-to được treo bằng trường tĩnh điện, nên không chịu ma sát ổ trục "
        "và các mô-men ngẫu nhiên do giá đỡ cơ khí gây ra. Nhờ vậy, hoạt động của nó đạt hiệu năng "
        "vượt trội so với các loại khác, gần với hiệu năng của một con quay lý thuyết. Dù không hệ "
        "nào dám nhận là hoàn hảo, ESG cần cập nhật ít thường xuyên hơn nhiều so với các con quay cơ "
        "khí khác."))

    b.append(h3("Con quay hồi chuyển", "Gyroscopes"))
    b.append(p(
        "Có hai nhóm lớn: (1) con quay cơ khí và (2) con quay quang học. Trong mỗi nhóm lại có nhiều "
        "loại khác nhau. Ở đây chỉ mô tả vài kiểu cơ bản để minh hoạ nguyên lý hoạt động; thông tin "
        "chi tiết có thể tìm trong các tài liệu dẫn ở cuối chương."))

    b.append(h4("Con quay cơ khí", "Mechanical gyroscopes"))
    b.append(p(
        "Con quay cơ khí đầu tiên do Foucault chế tạo năm 1852: một bánh xe đặt trong gimbal, đứng "
        "yên trong không gian nhờ động lượng góc trong khi bệ quay quanh nó. Chúng hoạt động trên cơ "
        "sở bảo toàn động lượng góc, bằng cách cảm nhận sự đổi hướng của một vectơ động lượng góc. Có "
        "nhiều loại khác nhau:"))
    b.append(
        '<ol class="plain">'
        "<li><b>Con quay một bậc tự do:</b> gồm con quay tốc độ, con quay tích phân tốc độ, con quay "
        "bánh đà rô-to quay, con quay điện tử và con quay hạt.</li>"
        "<li><b>Con quay hai bậc tự do:</b> gồm kiểu gimbal ngoài, kiểu hai trục nổi, kiểu rô-to tự "
        "do hình cầu, kiểu treo bằng điện và kiểu rô-to tự do đệm khí.</li>"
        "<li><b>Con quay rung:</b> gồm con quay âm thoa, dây rung, vỏ rung, cộng hưởng bán cầu và "
        "trụ rung.</li>"
        "<li><b>Con quay động lượng tuyến tính liên tục:</b> dùng một dòng chảy ổn định của chất "
        "lỏng, plasma hoặc êlectron, vốn có xu hướng giữ nguyên vectơ vận tốc đã thiết lập khi bệ "
        "quay. Một ví dụ điển hình dựa trên một cặp nhiệt kế dây nóng vi sai để phát hiện độ dịch "
        "ngang biểu kiến của cột không khí đang chảy.</li>"
        "</ol>")

    b.append(p(
        "Nguyên lý hoạt động của mọi con quay cơ khí đều dựa trên bảo toàn động lượng góc, như trên "
        "Hình 10-20. Động lượng góc quan trọng vì nó tạo ra một trục quy chiếu. Theo định luật thứ "
        "hai của Newton, động lượng góc của một vật sẽ không đổi trừ khi có mô-men tác dụng lên nó. "
        "Tốc độ biến thiên của động lượng góc bằng độ lớn của mô-men, dưới dạng vectơ:"))
    b.append(eq("<i>T</i> = d<i>H</i>/d<i>t</i>", "10.92"))
    b.append(p("trong đó <i>H</i> là động lượng góc (<i>H</i> = mô-men quán tính × vận tốc góc = "
               "<i>I</i>ω)."))

    b.append(p(
        "Nếu mô-men tác dụng quanh chính trục quay, nó làm thay đổi vận tốc góc:"))
    b.append(eq("<i>T</i> = <i>I</i>α = <i>I</i> dω/d<i>t</i>", "10.93"))
    b.append(p("trong đó <i>I</i> là mô-men quán tính quanh trục quay và α là gia tốc góc."))

    b.append(p(
        "Nếu mô-men trực giao với trục quay, nó không thể làm đổi độ lớn của vectơ vận tốc góc, "
        "nhưng có thể làm đổi hướng theo đúng chiều của mô-men <i>T</i>; khi đó:"))
    b.append(eq("d<i>H</i> = <i>H</i> dθ", "10.94"))
    b.append(p("với θ là góc quay."))

    b.append(p("Do đó, từ các phương trình 10.94 và 10.92:"))
    b.append(eq("<i>T</i> = d<i>H</i>/d<i>t</i> = <i>H</i> dθ/d<i>t</i> = <i>H</i>Ω", "10.95"))
    b.append(p(
        "trong đó Ω là tốc độ tiến động, tức vận tốc góc của bánh xe quay quanh trục vuông góc với "
        "mặt phẳng tạo bởi trục quay và mô-men vào. Nói chung, trục quay luôn có xu hướng tự sắp "
        "thẳng theo mô-men vào bên ngoài. Các phương trình này có thể được khai triển để mô tả nguyên "
        "lý hoạt động của con quay cơ khí nếu kể thêm động lượng góc theo các hướng x, y, z, hiện "
        "tượng chương động, gia tốc Coriolis, chiều của các mô-men và lực tuyến tính ảnh hưởng khác… "
        "Ở đây, hoạt động của con quay bánh đà quen thuộc sẽ được mô tả làm cơ sở cho các thảo luận "
        "tiếp theo về hệ dẫn đường quán tính."))

    b.append(fig(20, hb10fig.fig_10_20()))

    b.append(p(
        "Hình 10-21 là một ví dụ về con quay bánh đà hai trục. Trong loại này, một rô-to dẫn động "
        "bằng điện được treo trên một cặp ổ trục chính xác, ma sát thấp, đặt ở hai đầu trục rô-to. "
        "Các ổ trục rô-to được đỡ bởi một vòng tròn gọi là vòng gimbal trong; vòng này lại quay trên "
        "một bộ ổ trục thứ hai gắn vào vòng gimbal ngoài. Chuyển động quay của gimbal trong xác định "
        "trục nằm ngang của con quay, vuông góc với trục quay của rô-to. Vòng gimbal ngoài được gắn "
        "vào khung dụng cụ bằng bộ ổ trục thứ ba, xác định trục thẳng đứng của con quay, vuông góc "
        "với cả trục ngang lẫn trục quay. Kiểu treo này có tính chất luôn giữ nguyên phương trục quay "
        "đã định trước trong không gian quán tính."))

    b.append(fig(21, hb10fig.fig_10_21()))

    b.append(p(
        "Các phương trình mô tả con quay hai bậc tự do có thể viết được nhờ các phương trình 10.92 "
        "đến 10.95. Mô-men đối với một hệ quy chiếu quán tính viết là:"))
    b.append(eq("<i>T</i> = d<b>H</b><sub>I</sub>/d<i>t</i>", "10.96"))
    b.append(p("Nếu lấy Trái Đất làm hệ quy chiếu chuyển động, thì:"))
    b.append(eq("d<b>H</b><sub>I</sub>/d<i>t</i> = d<b>H</b><sub>E</sub>/d<i>t</i> + "
                "<b>ω</b><sub>IE</sub> × <b>H</b>", "10.97"))
    b.append(p(
        "Nếu bản thân con quay được gắn lên một phương tiện (ví dụ máy bay) đang chuyển động so với "
        "Trái Đất, thì:"))
    b.append(eq("d<b>H</b><sub>E</sub>/d<i>t</i> = d<b>H</b><sub>B</sub>/d<i>t</i> + "
                "<b>ω</b><sub>EB</sub> × <b>H</b>", "10.98"))
    b.append(p(
        "Nếu vỏ con quay được gắn lên một bệ sao cho nó có thể quay tương đối với bệ, thì:"))
    b.append(eq("d<b>H</b><sub>B</sub>/d<i>t</i> = d<b>H</b><sub>C</sub>/d<i>t</i> + "
                "<b>ω</b><sub>BC</sub> × <b>H</b>", "10.99"))
    b.append(p("Cuối cùng, gimbal trong có thể quay tương đối với vỏ, nên:"))
    b.append(eq("d<b>H</b><sub>C</sub>/d<i>t</i> = d<b>H</b><sub>G</sub>/d<i>t</i> + "
                "<b>ω</b><sub>GC</sub> × <b>H</b>", "10.100"))
    b.append(p("Thay các phương trình 10.97 đến 10.100 vào phương trình 10.96 được:"))
    b.append(eq("<i>T</i> = d<b>H</b><sub>G</sub>/d<i>t</i> + (<b>ω</b><sub>GC</sub> + "
                "<b>ω</b><sub>BC</sub> + <b>ω</b><sub>EB</sub> + <b>ω</b><sub>IE</sub>) × <b>H</b>",
                "10.101"))
    b.append(p("Nhưng:"))
    b.append(eq("<b>ω</b><sub>GC</sub> + <b>ω</b><sub>BC</sub> + <b>ω</b><sub>EB</sub> + "
                "<b>ω</b><sub>IE</sub> = <b>ω</b><sub>IG</sub>", "10.102"))
    b.append(p("Do đó,"))
    b.append(eq("<i>T</i> = d<b>H</b><sub>G</sub>/d<i>t</i> + <b>ω</b><sub>IG</sub> × <b>H</b>",
                "10.103"))
    b.append(p(
        "Bằng cách chế tạo con quay cẩn thận và giữ vận tốc quay của rô-to không đổi, có thể làm cho "
        "<b>H</b><sub>G</sub> bằng không. Khi đó định luật của con quay viết là:"))
    b.append(eq("<i>T</i> = <b>ω</b><sub>IG</sub> × <b>H</b>", "10.104"))
    b.append(p(
        "Điều này có nghĩa: nếu đặt một mô-men ngoài <i>T</i> lên con quay, gimbal trong sẽ tiến động "
        "tương đối với hệ quy chiếu quán tính với vận tốc ω sao cho phương trình 10.104 được thoả "
        "mãn."))

    b.append(p(
        "Trong phần lớn các thiết kế (ví dụ con quay tốc độ), gimbal được bọc kín trong chất lỏng và "
        "chất lỏng được làm nổi trong vỏ, nhằm giảm tải cho các ổ trục gimbal và tạo tắt dần nhớt. "
        "Một bộ thu nhận (pick-off) cảm nhận độ lệch của gimbal qua các biến áp vị trí và điều khiển "
        "một hệ servo, trong đó động cơ servo dẫn động vỏ để giữ pick-off ở điểm không."))

    b.append(h4("Con quay quang học", "Optical gyroscopes"))
    b.append(p(
        "Con quay quang học dựa trên tính chất quán tính của ánh sáng thay vì các định luật chuyển "
        "động của Newton. Chúng hoạt động theo hiệu ứng Sagnac, hiệu ứng tạo ra độ dịch vân giao thoa "
        "tỉ lệ với tốc độ quay. Trong trường hợp này, hai sóng ánh sáng lan truyền ngược chiều nhau "
        "trên một đường tròn bán kính <i>R</i>, xuất phát từ nguồn <i>S</i>. Hình 10-22 minh hoạ một "
        "bố trí điển hình. Khi con quay đứng yên, hai chùm tới đầu thu cùng lúc và không ghi được "
        "lệch pha nào. Giả sử nguồn quay với vận tốc ω sao cho ánh sáng đi ngược chiều quay trở về "
        "nguồn sớm hơn ánh sáng đi cùng chiều. Như vậy, mọi chuyển động quay của hệ quanh trục quay "
        "đều làm quãng đường của chùm đi cùng chiều dài ra và quãng đường của chùm đi ngược chiều "
        "ngắn lại. Hai chùm giao thoa tạo thành hình vân, có thể ghi vị trí vân hoặc cảm nhận độ "
        "lệch pha của hai chùm. Độ lệch pha này có dấu và tỉ lệ với vận tốc góc. Thông thường, đầu "
        "thu quang được dùng để đo độ dịch pha."))

    b.append(fig(22, hb10fig.fig_10_22()))

    b.append(p(
        "Có thể phân con quay quang thành hai loại: thụ động hay chủ động, và cộng hưởng hay không "
        "cộng hưởng. Trong cảm biến con quay thụ động, pha Sagnac được đo bằng một phương tiện bên "
        "ngoài; còn trong con quay chủ động, pha Sagnac gây ra một sự thay đổi tần số bên trong con "
        "quay, tỉ lệ trực tiếp với tốc độ quay."))

    b.append(p(
        "Giao thoa kế Sagnac là nền tảng của con quay sợi quang giao thoa (IFOG); Hình 10-22 vẽ một "
        "con quay sợi quang điển hình. Tuy nhiên, loại con quay được dùng rộng rãi nhất là con quay "
        "vòng cộng hưởng chủ động dùng la-de (RLG), được ứng dụng nhiều trong dẫn đường máy bay. Hai "
        "loại con quay cộng hưởng thụ động — con quay sợi quang cộng hưởng (RFOG) và con quay vi "
        "quang (MOG) — là những thiết bị giá rẻ hơn, thường dùng và có thể so sánh được với RLG."))

    b.append(h3("Gia tốc kế", "Accelerometers"))
    b.append(p(
        "Trong dẫn đường quán tính, gia tốc tuyệt đối được đo theo ba thành phần vuông góc với nhau "
        "của vectơ gia tốc toàn phần. Tích phân hai lần các tín hiệu gia tốc này cho độ dịch chuyển "
        "so với một vị trí gốc đã biết. Chi tiết về gia tốc và gia tốc kế được trình bày ở phần khác "
        "của sách này (xem mục Gia tốc, rung và xung kích). Gia tốc kế được cấu tạo từ ba phần tử cơ "
        "bản: khối thử (proof mass), cơ cấu treo và cơ cấu thu nhận. Một số gia tốc kế còn cần bộ "
        "sinh lực điện hoặc từ và các vòng servo thích hợp. Gia tốc kế không chỉ đo gia tốc thực của "
        "phương tiện mà còn phản ứng với các lực phản ứng của trọng trường. Gia tốc trọng trường là "
        "một hàm của vị trí — cụ thể là của vĩ độ và độ cao — và được các máy tính bù trừ."))

    b.append(p(
        "Loại gia tốc kế được dùng phổ biến nhất trong các hệ dẫn đường là kiểu con lắc. Có thể phân "
        "chúng thành:"))
    b.append(
        '<ol class="plain">'
        "<li>Gia tốc kế con lắc thông dụng</li>"
        "<li>Gia tốc kế kiểu Q-flex</li>"
        "<li>Gia tốc kế vi cơ (một ví dụ điển hình về gia tốc kế vi cơ hiện đại cho ở Hình 10-23)</li>"
        "</ol>")
    b.append(p(
        "Gia tốc trên ba trục được đo bằng các gia tốc kế đặt đúng vị trí. Vì gia tốc kế có sai số, "
        "các số đọc phải được bù bằng cách loại bỏ độ lệch cố định hoặc bằng cách áp hệ số tỉ lệ. Các "
        "sai số có thể là hàm của nhiệt độ làm việc, rung động hoặc xung kích. Phép đo thời gian phải "
        "chính xác, vì trong quá trình tích phân để xác định vị trí, thời gian xuất hiện ở bậc hai. "
        "Cũng phải tính đến chuyển động quay của Trái Đất và bù trừ thoả đáng các hiệu ứng trọng "
        "trường."))

    b.append(fig(23, hb10fig.fig_10_23()))

    b.append(h3("Sai số và ổn định", "Errors and Stabilization"))
    b.append(h4("Sai số", "Errors"))
    b.append(p(
        "Nói chung, dẫn đường quán tính là một quá trình giá trị đầu, trong đó vị trí của vật đang "
        "dẫn đường được xác định bằng cách cộng dồn những quãng đường đã đi theo những hướng đã "
        "biết. Mọi sai số trong hệ đều làm cho vị trí mong muốn bị biểu diễn sai, dẫn tới trượt mục "
        "tiêu. Nhược điểm lớn của một hệ dẫn đường quán tính là sai số có xu hướng tăng theo thời "
        "gian. Sai số của vị trí suy ra có nhiều nguyên nhân: hiểu biết không hoàn hảo về điều kiện "
        "xuất phát, sai số tính toán, và chủ yếu là sai số do con quay và gia tốc kế sinh ra."))

    b.append(p(
        "Nếu sai số tích luỹ theo thời gian trở nên quá lớn, có thể dùng các phương tiện hỗ trợ bên "
        "ngoài (ví dụ LORAN, OMEGA) để đặt lại hoặc cập nhật hệ. Muốn dùng tối ưu dữ liệu từ các "
        "phương tiện hỗ trợ, phải tính đến hình học của lần cập nhật cũng như độ chính xác của lần "
        "cập nhật so với độ chính xác của hệ quán tính. Ví dụ, bộ lọc Kalman là một trong những thủ "
        "tục tính toán hay được áp dụng để kết hợp tối ưu dữ liệu từ nhiều nguồn khác nhau."))

    b.append(p("Có thể phân sai số thành các loại lớn như sau:"))
    b.append(
        '<ol class="plain">'
        "<li><b>Sai số hướng của hệ:</b> một góc lệch trong hướng đi của một vật chuyển động với vận "
        "tốc nào đó có thể gây sai số nghiêm trọng. Ví dụ, một phương tiện chạy với vận tốc "
        "500 km/h theo đúng hướng nhưng mắc sai số hướng ban đầu 0,1° sẽ lệch khỏi mục tiêu khoảng "
        "873 m sau 1 h hành trình.</li>"
        "<li><b>Sai số tỉ lệ:</b> sai số trong hệ số tỉ lệ có thể tích luỹ. Để giảm thiểu, người ta "
        "dùng một hệ số tỉ lệ, là tỉ số giữa biến thiên tín hiệu vào và tín hiệu ra. Hệ số này đơn "
        "giản là chuyển đầu ra của con quay (số đếm mỗi giây đối với RLG) thành góc quay tương ứng. "
        "Một số dụng cụ có thể có hệ số tỉ lệ khác nhau cho đầu vào dương và âm, gọi là bất đối xứng "
        "hệ số tỉ lệ. (Hệ số tỉ lệ đo bằng ° h<sup>–1</sup> mA<sup>–1</sup>, "
        "° h<sup>–1</sup> Hz<sup>–1</sup> hoặc g Hz<sup>–1</sup>.)</li>"
        "<li><b>Sai số phi tuyến và sai số tổ hợp:</b> trong phần lớn trường hợp, hệ số tỉ lệ không "
        "phải hằng số mà có thể chứa các số hạng bậc hai hoặc cao hơn liên hệ tín hiệu ra với tín "
        "hiệu vào. Có thể dùng các kỹ thuật thống kê để giảm thiểu các sai số này.</li>"
        "<li><b>Sai số độ lệch (bias):</b> độ lệch điểm không, hay sai số độ lệch, là do vẫn tồn tại "
        "một mức tín hiệu ra nào đó khi đầu vào bằng không. Sai số độ lệch có trong gia tốc kế, con "
        "quay, các lệch trục nghiêng…</li>"
        "<li><b>Sai số trôi ngẫu nhiên và bước ngẫu nhiên:</b> trong một số trường hợp, đầu ra của "
        "thiết bị có thể thay đổi do nhiễu bên trong cảm biến, như tiếng ồn ổ bi trong con quay cơ "
        "khí. Những nhiễu này có thể liên quan tới thay đổi nhiệt độ, lão hoá… Nhiễu trắng trong con "
        "quay quang có thể gây tích luỹ dài hạn sai số góc, gọi là bước ngẫu nhiên (random walk).</li>"
        "<li><b>Sai số vùng chết, ngưỡng, độ phân giải và trễ:</b> những sai số này gắn với cách hoạt "
        "động vốn có của gia tốc kế và con quay. Chúng có thể do ma sát tĩnh, do cần một đầu vào tối "
        "thiểu mới có đầu ra, do đầu ra tối thiểu đo được, và do tính không lặp lại của biến thiên "
        "đầu ra theo biến thiên đầu vào.</li>"
        "</ol>")
    b.append(p(
        "Cần nói rõ rằng danh sách này hoàn toàn không đầy đủ. Phân tích sai số chi tiết có thể tìm "
        "trong các tài liệu được dẫn."))

    b.append(h4("Ổn định", "Stabilization"))
    b.append(p(
        "Các cảm biến dẫn đường quán tính phải giữ được góc trong những giới hạn định trước, bất "
        "chấp các nhiễu do vật đang chuyển động gây ra. Yêu cầu về độ chính xác đòi hỏi hệ phải cung "
        "cấp thông tin tin cậy và ổn định dù có rung động và các yếu tố nhiễu khác. Một cách đạt được "
        "sự ổn định là dùng bệ ổn định. Các bệ này được thiết kế để giữ gia tốc kế và con quay nằm "
        "ngang chính xác và định hướng theo phương vị. Trong một số trường hợp, bệ được dẫn động "
        "quanh trục của nó bằng khuếch đại servo và động cơ điện. Thông thường, đầu ra của các gia "
        "tốc kế tích phân hai lần được dùng trực tiếp để điều khiển tốc độ tiến động của con quay "
        "trục ngang. Các bộ thu nhận nhạy trên con quay, được nuôi bằng tín hiệu sai số, dùng để giữ "
        "bệ ổn định ở trạng thái mong muốn trước các mô-men nhiễu. Hoạt động của một hệ điển hình "
        "được trình bày dưới dạng sơ đồ khối trên Hình 10-24."))

    b.append(fig(24, hb10fig.fig_10_24()))

    b.append(p(
        "Khác với kiểu có bệ, trong một hệ gắn cứng, con quay và gia tốc kế được gắn chặt lên kết "
        "cấu phương tiện để chúng chuyển động cùng phương tiện. Gia tốc kế và con quay được chế tạo "
        "để đo gia tốc và góc tới các giá trị lớn nhất dự kiến. Khi phương tiện di chuyển, các giá "
        "trị đo được truyền thường xuyên về máy tính. Máy tính dùng các giá trị này để phân giải số "
        "đọc về bộ trục dẫn đường và suy ra các kết luận trên bộ trục thân."))

    b.append(h3("Dẫn đường quán tính cho xe", "Vehicular Inertial Navigation"))
    b.append(p(
        "Trong dẫn đường phương tiện hiện đại, bản đồ số hoá và thiết bị thông tin di động được tích "
        "hợp cùng các hệ dẫn đường quán tính và/hoặc điện tử khác. Những năm gần đây, theo sau sự "
        "phổ biến của các hệ GPS giá rẻ, dẫn đường cho xe thu hút nhiều quan tâm nhờ thị trường tiềm "
        "năng lớn, cả cho xe tiêu dùng lẫn xe thương mại."))

    b.append(p(
        "Các hệ dẫn đường ô-tô dựa trên tính vị trí theo quãng đường, khớp bản đồ, định vị vệ tinh và "
        "các công nghệ dẫn đường khác. Các hệ bản đồ thông minh đạt độ chính xác tương đối cao bằng "
        "cách khớp quỹ đạo tính theo quãng đường với hình học đường sá đã mã hoá trong bản đồ số. "
        "Việc này cũng được dùng cho các chức năng khác như tìm tuyến và gán mã địa lý. Các hệ dẫn "
        "đường dựa trên vệ tinh đạt độ chính xác tuyệt đối cao nhờ sự hỗ trợ của tính vị trí theo "
        "quãng đường."))

    b.append(p("Năng lực và chức năng của hệ dẫn đường ô-tô phụ thuộc vào việc:"))
    b.append(
        '<ul class="plain">'
        "<li>Chọn công nghệ cần thiết</li>"
        "<li>Tích hợp toàn hệ thống</li>"
        "<li>Giải quyết giao diện với người lái</li>"
        "<li>Cung cấp cơ sở dữ liệu bản đồ</li>"
        "<li>Phối hợp thông tin di động</li>"
        "</ul>")
    b.append(p(
        "Bản đồ số và thông tin di động kết hợp lại mới đem lại ích lợi và hiệu quả trọn vẹn. Các hệ "
        "dẫn đường được tăng cường mạnh khi đi cùng bản đồ số lưu trữ và thông tin liên lạc hữu "
        "hiệu."))

    b.append(p(
        "Tính hữu dụng của một hệ dẫn đường gắn với độ chính xác xác định vị trí. Có nhiều phương "
        "pháp với độ chính xác khác nhau:"))
    b.append(h4("Tính vị trí theo quãng đường", "Dead-reckoning"))
    b.append(p(
        "Đây là quá trình xác định vị trí phương tiện so với một vị trí ban đầu bằng cách tích phân "
        "các gia số quãng đường và hướng đi đã đo. Các thiết bị gồm đồng hồ đo quãng, đồng hồ đo "
        "quãng vi sai và la bàn từ. Con quay và hệ quán tính tỏ ra chỉ có ứng dụng hạn chế trong môi "
        "trường ô-tô khắc nghiệt. Tuy vậy, dù mắc phải tích luỹ sai số, các hệ tính vị trí theo quãng "
        "đường vẫn là những hệ dẫn đường quán tính được dùng rộng rãi, đặc biệt trong rô-bốt và ứng "
        "dụng phương tiện. Ngay cả hệ dẫn đường chính xác nhất cũng cần được khởi tạo lại định kỳ và "
        "hiệu chuẩn liên tục bằng máy tính."))

    b.append(h4("Định vị vô tuyến", "Radiolocation"))
    b.append(p(
        "Trong định vị vô tuyến, hệ định vị toàn cầu (GPS) được dùng rộng rãi. Tuy vậy, LORAN đang "
        "trở nên phổ biến như một phương tiện theo dõi vị trí xe trên bộ từ một điểm trung tâm. Nhưng "
        "độ chính xác khiêm tốn của nó hạn chế việc áp dụng toàn cầu cho dẫn đường ô-tô."))

    b.append(h4("Khớp bản đồ", "Map Matching"))
    b.append(p(
        "Các khái niệm trí tuệ nhân tạo được áp dụng để khớp quỹ đạo xe tính theo quãng đường, vốn "
        "được lưu trong máy tính. Trong khớp bản đồ, các đặc trưng toán học cảm nhận được của quỹ "
        "đạo xe được liên kết liên tục với những đặc trưng đã mã hoá trong cơ sở dữ liệu bản đồ. Nhờ "
        "vậy, vị trí tính theo quãng đường có thể được khởi tạo lại tự động ở mỗi chỗ rẽ, ngăn sai "
        "số tích luỹ."))
    b.append(p(
        "Ứng dụng đầu tiên của công nghệ khớp bản đồ là Hệ điều khiển tuyến tự động (ARCS), dùng một "
        "đồng hồ đo quãng vi sai để tính vị trí theo quãng đường. Ở một hệ khác, hệ khớp bản đồ Etak, "
        "một la bàn cổng từ trạng thái rắn được dùng cùng đồng hồ đo quãng vi sai để tính quỹ đạo "
        "nhằm khớp với bản đồ số hoá và ảnh hàng không. Chi tiết thêm về các công nghệ này có trong "
        "các tài liệu dẫn ở cuối chương."))
    b.append(p(
        "Trong một hệ khớp bản đồ, chừng nào các đường phố và sự liên thông đường sá còn được định "
        "nghĩa chính xác, quá trình sẽ nhận ra vị trí so với mạng đường theo đúng cách người lái "
        "nhìn thấy. Phần lớn thiết bị tính vị trí theo quãng đường bán trên thị trường đủ vững để hỗ "
        "trợ khớp bản đồ khi hoạt động trong một mạng đường đã định nghĩa. Tuy nhiên, cần độ chính "
        "xác tính theo quãng đường tốt thì mới khởi tạo lại được bằng khớp bản đồ khi quay về mạng "
        "đường sau khi đi ra ngoài đường."))

    b.append(h4("Beacon cận vị", "Proximity Beacon"))
    b.append(p(
        "Cách tiếp cận này dùng các máy phát tầm ngắn đặt ở những vị trí chiến lược; việc thu được "
        "tín hiệu đã mã hoá vị trí của chúng cho phép suy ra vị trí tức thời của xe đang thu. Có "
        "nhiều biến thể; một số phiên bản có thông tin hai chiều với xe được trang bị. Thông thường, "
        "người lái nhập mã điểm đến trên bảng điều khiển của xe để tự động truyền tới trạm bên đường "
        "khi xe tới gần một giao lộ đã được trang bị. Trạm bên đường, có thể nối mạng với hệ quản lý "
        "giao thông, phân tích mã điểm đến và phát chỉ dẫn tuyến tới màn hình trên bảng xe. Các hệ "
        "beacon cận vị đang được thử nghiệm ở Đức và Nhật Bản. Một trong những hệ phổ biến nhất là "
        "ALI-SCOUT, dùng kỹ thuật tính vị trí theo quãng đường và khớp bản đồ giữa các beacon để tải "
        "về bản đồ và dữ liệu giao thông cập nhật ở Berlin."))
    b.append(p(
        "Cách giải quyết giao diện giữa hệ dẫn đường trên xe và người vận hành phải tính đến các yếu "
        "tố công thái học và an toàn, cũng như các yêu cầu chức năng. Nhờ nghiên cứu ráo riết, đặc "
        "biệt trong công nghiệp hàng không, việc hiển thị thông tin cho người vận hành là một lĩnh "
        "vực đã phát triển tốt. Trong một hệ nổi tiếng của châu Âu, CARIN của Philips, một màn hình "
        "bản đồ CRT màu được dùng để chỉ vị trí xe so với cảnh vật xung quanh. Nhiều hệ khác dùng "
        "thông điệp hình ảnh ngắn, đồ hoạ tượng trưng và giọng nói."))
    b.append(p(
        "Vai trò tiềm năng lớn của thông tin dữ liệu trong dẫn đường ô-tô tương lai là cung cấp cập "
        "nhật hiện thời (đường mới, đường đóng, đường vòng…) cho cơ sở dữ liệu bản đồ trên xe, đồng "
        "thời cung cấp thông tin thời gian thực về điều kiện giao thông để sinh tuyến trên xe."))

    b.append(h3("Máy bay", "Aircraft"))
    b.append(p(
        "Phương tiện dẫn đường chính cho máy bay dân dụng bay trong vùng trời của phần lớn các nước "
        "phát triển là hệ VOR/DME. VOR (Very high frequency Omni Range — dải toàn hướng tần số rất "
        "cao) và DME (Distance Measuring Equipment — thiết bị đo khoảng cách) cho phép xác định trên "
        "khoang phương vị của máy bay so với phương Bắc tại trạm mặt đất cố định, và cự ly nghiêng "
        "tới trạm. Chi tiết thêm có trong các tài liệu dẫn ở cuối chương."))
    b.append(p(
        "Nhiều máy bay thương mại được trang bị các hệ dẫn đường quán tính (INS) chính xác, không "
        "chỉ để dẫn đường mà còn để ổn định máy bay ở mọi thời điểm. Các con quay và gia tốc kế đặt "
        "đúng chỗ cấp tín hiệu điều khiển độ ổn định của máy bay, như trên Hình 10-25. Nhiều INS "
        "trên máy bay dùng một bệ ổn định bằng con quay, trên đó gắn các gia tốc kế. Bệ được căn "
        "chỉnh theo hướng mong muốn trước khi cất cánh. Do sai số căn chỉnh và các nhiễu ngẫu nhiên "
        "trong bay như trôi con quay, sai số hệ số tỉ lệ và sai số độ lệch của gia tốc kế, sai số "
        "trong hướng mong muốn tăng dần theo thời gian. Các sai số này cần được bù định kỳ bằng "
        "thông tin bên ngoài, ví dụ các hệ dẫn đường Omega."))

    b.append(fig(25, hb10fig.fig_10_25()))

    b.append(p(
        "Omega là một hệ dẫn đường 10 kHz đến 14 kHz, vốn được dự kiến chủ yếu để cập nhật các hệ "
        "dẫn đường quán tính trên tàu ngầm, nhờ tần số rất thấp xuyên xuống dưới mặt biển. Nó cũng "
        "được nhiều máy bay hàng không tổng hợp và quân sự dùng vì phủ toàn cầu. Một số hãng hàng "
        "không (ví dụ American Airlines) đã trang bị đầu thu Omega cho toàn bộ đội bay. Lực lượng "
        "Tuần duyên Hoa Kỳ duy trì hai trạm Omega, các nước khác duy trì thêm sáu trạm. Mỗi trạm phát "
        "tám âm hình sin liên tiếp với chu kỳ lặp 10 s. Bốn âm là âm dẫn đường chung cho mọi trạm; "
        "bốn âm còn lại nhận dạng duy nhất trạm đó. Mỗi trạm có một đồng hồ xê-di được hiệu chuẩn "
        "trong phạm vi 1 µs bằng cách trao đổi đồng hồ nguyên tử xách tay với các trạm Omega khác và "
        "với Đài thiên văn Hải quân Hoa Kỳ."))
    b.append(p(
        "Các hệ GPS cho mọi phương tiện trên hoặc gần Trái Đất một độ chính xác dẫn đường chưa từng "
        "có. Một số hãng hàng không quốc tế được trang bị đầu thu GPS–Glonass giới hạn. Nhiều thí "
        "nghiệm đang tiến hành nhằm cân đối chi phí và độ chính xác của các tổ hợp khác nhau giữa "
        "thiết bị quán tính, Omega, Loran, GPS và Transit. Người ta thiết kế các đầu thu trên không "
        "kết hợp những thiết bị trợ dẫn cùng làm việc trong một dải tần chung (ví dụ GPS, DME, JTID "
        "và IFF)."))
    b.append(p(
        "Các vệ tinh thông tin “Marec” của INMARSAT phục vụ giao thông đường biển nhưng được cấu "
        "hình để phục vụ giao thông hàng không bằng cách liên lạc trực tiếp với máy bay với giá "
        "khoảng 10 USD mỗi cuộc gọi."))

    b.append(h3("Dưới nước", "Underwater"))
    b.append(p(
        "Hệ dẫn đường quán tính trên tàu (SINS) được phát triển ban đầu để đáp ứng yêu cầu định vị "
        "chính xác của tàu ngầm mang tên lửa đạn đạo vào cuối thập niên 1950 và đầu thập niên 1960. "
        "Lần triển khai đầu tiên là trên tàu George Washington của Hoa Kỳ năm 1960; ngày nay SINS "
        "được dùng trên tàu ngầm, tàu sân bay và các chiến hạm mặt nước khác. Khi giá thành và kích "
        "thước tiếp tục giảm, hệ này cũng được triển khai trên tàu hải quân cũng như tàu thương "
        "mại. Một hướng phát triển khác của INS cho ứng dụng dưới nước là lĩnh vực phương tiện lặn "
        "tự hành (AUV). Dưới đây mô tả một số sản phẩm như vậy."))
    b.append(p(
        "AUV được dùng rộng rãi cho mục đích quân sự và dân sự. Ví dụ ứng dụng: lập bản đồ, giám sát, "
        "thăm dò đại dương, khảo sát và khai khoáng — tất cả đều đòi hỏi xác định vị trí chính xác. "
        "Các tính năng mong muốn của những hệ như vậy là: công suất thấp, độ chính xác cao, thể tích "
        "nhỏ, khối lượng nhẹ và giá thành thấp. Hai ví dụ điển hình là họ LN do Litton Guidance and "
        "Control Systems sản xuất và hệ do Harbor Branch Oceanographic Institution Inc. (HBOI) phát "
        "triển. Dưới đây mô tả vắn tắt thông số của một số hệ này để làm ví dụ về INS dưới nước."))

    b.append(h4("Hệ Litton LN-100", "The Litton LN-100 System"))
    b.append(p(
        "LN-100 của Litton là một ví dụ về INS gắn cứng. Hệ LN-100 gồm ba con quay Zero-Lock (ZLG) "
        "của Litton, một bộ ba gia tốc kế Litton A4, bộ nguồn, các mạch điện tử hỗ trợ và một máy "
        "tính JIWAG chuẩn 80960. Máy tính một bảng mạch này thực hiện toàn bộ các chức năng điều "
        "khiển, dẫn đường và giao diện."))

    b.append(h4("Hệ HBOI", "The HBOI System"))
    b.append(p(
        "Hệ HBOI được phát triển cùng Kearfott Guidance and Navigation (KGN) và dùng một con quay "
        "vòng la-de nguyên khối (MRLG), các cảm biến chuyển động, đầu vào GPS và khối điều khiển. "
        "Khối đo quán tính dựa trên con quay vòng la-de ba trục T16-B của Kearfott và ba gia tốc "
        "kế."))

    b.append(h3("Rô-bốt", "Robotics"))
    b.append(p(
        "Gắn bó chặt chẽ với phương tiện lặn tự hành, rô-bốt di động tự hành cũng dùng INS rộng rãi "
        "như một hệ dẫn đường tự thân, độc lập. Ứng dụng điển hình là khai khoáng, thăm dò địa hình "
        "chưa biết và lập quỹ đạo ngoại tuyến. Có nhiều hệ dẫn đường quán tính bán trên thị trường "
        "phù hợp để dùng hiệu quả về chi phí cho dẫn đường rô-bốt, trong đó có: la bàn con quay, con "
        "quay tốc độ, gyrochip, con quay rung áp điện, con quay vòng la-de, con quay sợi quang giao "
        "thoa và các loại khác. Dưới đây trình bày ba hệ phổ biến."))

    b.append(h4("Hệ định vị phương vị mô-đun Honeywell (MAPS)",
                "The Honeywell Modular Azimuth Position System (MAPS)"))
    b.append(p(
        "Hệ H-726 Modular Azimuth Position System (MAPS) của Honeywell là ví dụ điển hình về một hệ "
        "dẫn đường quán tính cho phương tiện trên bộ. Hệ gồm một khối tham chiếu động (DRU) cung cấp "
        "thông tin đã xử lý từ cụm cảm biến quán tính, một khối điều khiển hiển thị (CDU) dùng làm "
        "giao diện người – máy, và một cảm biến chuyển động phương tiện (VMS) theo dõi thông tin "
        "hướng và quãng đường của xe. Cụm cảm biến quán tính gồm ba con quay vòng la-de Honeywell "
        "GG1342 và ba gia tốc kế Sundstrand QA2000, gắn để đo chuyển động theo ba trục cục bộ. Bộ xử "
        "lý quán tính chuyển thông tin sang bộ xử lý dẫn đường, nơi phân giải thông tin chuyển động "
        "của xe từ VMS. CDU cung cấp chọn chế độ, hiển thị dữ liệu, thông tin điểm mốc và giao diện "
        "vận hành chung."))

    b.append(h4("Con quay sợi quang Hitachi", "Hitachi Fiber-Optic Gyroscopes"))
    b.append(p(
        "Các sản phẩm của Hitachi đáng chú ý vì tương đối rẻ và được thiết kế cho ứng dụng ô-tô. Con "
        "quay sợi quang giao thoa vòng hở (IFOG) HOFG-4FT đã nhận giải “Sản phẩm mới có ý nghĩa công "
        "nghệ nhất của năm” năm 1993, và hiện được lắp trên một mẫu xe thương mại của Toyota. Các "
        "mẫu IFOG tiếp theo là HOFG-X, HOFG-1 và HGA-D. HOFG-1 được dùng rộng rãi trong rô-bốt di "
        "động công nghiệp. Đầu ra của hệ có thể ở dạng nối tiếp theo chuẩn RS-232 hoặc dạng tín hiệu "
        "tương tự. Thông số của HOFG-1 gồm dải đo ±60° s<sup>–1</sup>, tốc độ cập nhật 15 ms và độ "
        "tuyến tính ±0,5%. Yêu cầu nguồn là 10 đến 16 V một chiều và 0,5 A."))

    b.append(reflist([
        "K. R. Britting, <em>Inertial Navigation Systems Analysis</em>, New York: Wiley-Interscience, "
        "1971.",
        "M. Kayton, <em>Navigation — Land, Sea, Air and Space</em>, New York: IEEE Press, 1990.",
        "A. Lawrance, <em>Modern Inertial Technology — Navigation, Guidance, and Control</em>, "
        "New York: Springer-Verlag, 1993.",
    ]))

    b.append(h4("Phụ lục — Danh mục nhà chế tạo và cung cấp",
                "Appendix — List of Manufacturers/Suppliers"))
    b.append(note(
        "Bản gốc của mục 10.3 có một phụ lục liệt kê địa chỉ đường phố, số điện thoại và số fax của "
        "các nhà chế tạo, nhà cung cấp. Ở đây chỉ giữ tên và nơi đặt trụ sở, vì thông tin liên lạc "
        "chi tiết trong bản gốc đã quá cũ để còn dùng được."))
    b.append(table(
        ["Nhà chế tạo / cung cấp", "Trụ sở"],
        [
            ("Aerodata Co.", "Massapequa, NY"),
            ("AGV Products, Inc.", "Charlotte, NC"),
            ("American GNC Corporation", "Chatsworth, CA"),
            ("Astronautics Co.", "Milwaukee, WI"),
            ("Cybermotion, Inc.", "Salem, VA"),
            ("First State Map Co.", "Wilmington, CT"),
            ("Hitachi Cable America, Inc.", "White Plains, NY"),
            ("Honeywell, Inc. — Technology Center", "Minneapolis, MN"),
            ("Ketema Inc.", "El Cajon, CA"),
            ("NASA Goddard Space Flight Center — Robotics Branch", "Greenbelt, MD"),
            ("Naval Command Control Center — RDT&amp;E Division", "San Diego, CA"),
            ("Navigation Science Co.", "Westlake Village, CA"),
            ("Navigations Technologies Corp.", "Sunnyvale, CA"),
            ("NSC", "Thousand Oaks, CA"),
            ("Romarc Co.", "Plumsteadville, PA"),
            ("Schwartz Electro-Optics, Inc.", "Orlando, FL"),
            ("Siemens Co.", "New York, NY"),
            ("Southern Avionics Co.", "Beaumont, TX"),
            ("Sperry Marine Inc.", "Charlottesville, VA"),
            ("Systron Donner Inertial Division — BEI Electronics", "Concord, CA"),
            ("Trackor Inc.", "Austin, TX"),
            ("Warren-Knight Inst. Co.", "Philadelphia, PA"),
        ],
        "Bảng PL-10.3. Các nhà chế tạo và cung cấp thiết bị dẫn đường quán tính, theo phụ lục của "
        "mục 10.3."))

    # ------------------------------------------------------------ 10.4
    b.append(h2("10.4 Dẫn đường vệ tinh và định vị vô tuyến",
                "Satellite Navigation and Radiolocation"))
    b.append(p("<em>Halit Eren · C. C. Fung</em>"))

    b.append(p(
        "Có thể phân các hệ dẫn đường điện tử hiện đại theo tầm hoạt động, phạm vi, sai số và chi "
        "phí. Theo tầm, người ta chia thành tầm ngắn, tầm trung và tầm xa, trong đó ranh giới chính "
        "xác khá mơ hồ. Theo phạm vi, hệ có thể là tự thân hoặc được hỗ trợ từ bên ngoài, và có thể "
        "hoạt động ở chế độ chủ động (có phát) hoặc thụ động (không phát)."))
    b.append(p(
        "Các hệ tầm ngắn gồm radiobeacon, radar và Decca. Các hệ tầm trung gồm Decca và một số loại "
        "radar tăng tầm. Các hệ tầm xa gồm Loran-C, Consol và Omega. Tất cả những hệ này đều dựa trên "
        "phát tần số vô tuyến (RF) chủ động, và — trừ radar — đều được hỗ trợ từ bên ngoài đối với "
        "vật đang được dẫn đường. Ngoài ra còn một nhóm hệ khác gọi là hệ dẫn đường tiên tiến, mà ví "
        "dụ điển hình là các hệ dẫn đường vệ tinh Transit, Glonass và Hệ định vị toàn cầu (GPS)."))
    b.append(p(
        "Việc sử dụng sóng vô tuyến điện từ là điểm chung của mọi hệ dẫn đường bàn tới ở đây. Hiểu "
        "được cách chúng xử sự trong khí quyển Trái Đất là điều rất quan trọng trong thiết kế, chế "
        "tạo và sử dụng mọi loại thiết bị dẫn đường — từ vệ tinh tới những đầu thu cầm tay đơn "
        "giản."))
    b.append(p(
        "Khi một sóng vô tuyến FM được tạo ra trong khí quyển Trái Đất, sóng lan ra ngoài. Sóng có "
        "thể bị hấp thụ hoặc bị phản xạ từ bề mặt các vật liệu mà nó gặp. Sự hấp thụ và tán xạ sóng "
        "điện từ xảy ra vì nhiều lý do, một trong số đó là do kích thích êlectron trong các phân tử "
        "của môi trường lan truyền. Cách xử sự của một sóng điện từ phụ thuộc tần số và bước sóng "
        "tương ứng. Hình 10-26 vẽ phổ tần số của sóng điện từ. Ở đầu thấp của phổ là sóng âm thanh; "
        "sóng vô tuyến từ 5 kHz đến 300 GHz; ở đầu cao là ánh sáng khả kiến và nhiều loại tia khác "
        "nhau."))

    b.append(fig(26, hb10fig.fig_10_26()))

    b.append(p(
        "Để dùng trong thực tế, phổ sóng vô tuyến được chia thành tám băng tần: tần số rất thấp "
        "(VLF) dưới 30 kHz, tần số thấp (LF) 30 kHz đến 300 kHz, tần số trung (MF) 300 kHz đến "
        "3 MHz, tần số cao (HF) 3 MHz đến 30 MHz, tần số rất cao (VHF) 30 MHz đến 300 MHz, tần số "
        "cực cao (UHF) 300 MHz đến 3 GHz, tần số siêu cao (SHF) 3 GHz đến 30 GHz, và tần số cực kỳ "
        "cao (EHF) 30 GHz đến 300 GHz."))
    b.append(p(
        "Để dễ nhận biết, các tần số trên 1 GHz được chia tiếp bằng các ký hiệu chữ: băng L "
        "(1–2 GHz), băng S (2–4 GHz), băng C (4–8 GHz), băng X (8–12,5 GHz) và băng K "
        "(12,5–40 GHz). Vì sự hấp thụ mạnh sóng radar xảy ra gần tần số cộng hưởng của hơi nước ở "
        "22,2 GHz, băng K được chia thành băng K thấp (12,5–18 GHz) và băng K cao (26,5–40 GHz). Phần "
        "lớn radar dẫn đường làm việc ở băng X và S, còn nhiều radar điều khiển hoả lực làm việc "
        "trong dải băng K."))

    b.append(p(
        "Sóng vô tuyến được phát dưới dạng sóng liên tục hoặc sóng điều chế. Một sóng mang (CW) được "
        "điều chế để mang thông tin theo ba dạng cơ bản: điều biên, điều tần và điều xung, như trên "
        "Hình 10-27. Điều biên (AM) làm thay đổi biên độ của sóng mang theo một tín hiệu điều chế. "
        "Trong điều tần (FM), tần số của sóng mang bị thay đổi theo tần số của sóng điều chế. FM được "
        "dùng trong phát thanh thương mại và phần tiếng của truyền hình. Điều xung khác AM và FM ở "
        "chỗ thường không có sóng điều chế áp đặt; sóng liên tục được bẻ thành những đoạn rất ngắn "
        "hay “xung”, cách nhau bằng những khoảng lặng không phát gì. Kiểu này được dùng trong các hệ "
        "dẫn đường vệ tinh, radar tìm kiếm mặt biển và các thiết bị trợ dẫn vô tuyến tầm xa như "
        "Loran."))

    b.append(fig(27, hb10fig.fig_10_27()))

    b.append(p(
        "Khi một sóng điện từ gặp vật cản, xảy ra nhiễu xạ, biểu hiện ở việc thu tín hiệu yếu trong "
        "vùng “bóng”. Hai sóng tác dụng lên cùng một điểm cũng gây giao thoa. Mức giao thoa phụ thuộc "
        "quan hệ pha và tần số. Ví dụ, hai sóng cùng tần số lệch pha 180° sẽ cho điểm không tại điểm "
        "đó. Ngoài ra, trong những điều kiện nhất định, một phần năng lượng điện từ của sóng vô "
        "tuyến có thể phản xạ trở lại phía mặt đất để tạo thành tầng điện ly. Tầng điện ly là một "
        "lớp hạt mang điện nằm cách mặt đất khoảng 90 đến 400 km; sóng phản xạ như vậy gọi là sóng "
        "trời."))

    b.append(p(
        "Trong nghiên cứu lan truyền sóng vô tuyến, có bốn tầng điện ly quan trọng, như trên "
        "Hình 10-28. Tầng D nằm ở khoảng 60–90 km và hình thành vào ban ngày. Tầng E ở khoảng 110 km, "
        "tồn tại qua đêm với cường độ giảm. Tầng F1 nằm giữa 175 km và 200 km, chỉ xuất hiện ban "
        "ngày. Tầng F2 nằm giữa 250 km và 400 km; mạnh nhất vào ban ngày nhưng về đêm lại hợp nhất "
        "với tầng F1 thành một tầng F yếu. Các tầng điện ly biến thiên, dường như theo chu kỳ ngày, "
        "chu kỳ mùa và chu kỳ vết đen Mặt Trời. Các tầng có thể dẫn điện rất tốt, hoặc có thể cản "
        "hoàn toàn việc truyền sóng, tuỳ theo tần số của sóng, góc tới, độ cao và cường độ trên các "
        "tầng khác nhau tại thời điểm phát. Nói chung, các tần số trong băng MF và HF là thích hợp "
        "nhất cho phản xạ tầng điện ly cả ngày lẫn đêm."))

    b.append(fig(28, hb10fig.fig_10_28()))

    b.append(p(
        "Do điện trở của vỏ Trái Đất lớn hơn của khí quyển, phần thấp của sóng vô tuyến song song với "
        "mặt đất bị làm chậm lại, khiến sóng bị bẻ cong về phía Trái Đất. Sóng kiểu này gọi là sóng "
        "đất. Sóng đất tồn tại vì chúng dùng bề mặt Trái Đất làm vật dẫn. Chúng xuất hiện ở tần số "
        "thấp, vì LF gây bẻ cong nhiều hơn cho phù hợp với hình dạng Trái Đất. Tầm xa cuối cùng của "
        "sóng đất phụ thuộc các hiệu ứng hấp thụ. Đôi khi, trong tầng khí quyển thấp, hiện tượng dẫn "
        "sóng bề mặt xảy ra nhờ phản xạ nhiều lần, kéo dài tầm của sóng đất vượt xa giới hạn thường "
        "lệ. Hiện tượng này gắn với tần số vô tuyến và radar cao hơn, và phổ biến ở các vĩ độ nhiệt "
        "đới. Các dạng xử sự của sóng phát ở nhiều góc khác nhau được minh hoạ trên Hình 10-28."))

    b.append(h3("Độ chính xác của một điểm định vị điện tử", "Accuracy of Electronic Fix"))
    b.append(p(
        "Có nhiều hiệu ứng ngẫu nhiên ảnh hưởng tới độ chính xác của một phép xác định vị trí điện "
        "tử: nhiễu loạn khí quyển dọc đường truyền, sai số trong máy phát và máy thu, đồng hồ, mạch "
        "điện tử thiếu chính xác, sai số con quay… Kết quả là một loạt vị trí xác định tại cùng một "
        "thời điểm và cùng một nơi thường tạo thành một cụm điểm quanh vị trí thật. Có hai thước đo "
        "thường dùng để mô tả độ chính xác. Thứ nhất là sai số vòng tròn khả dĩ (CEP) — một vòng tròn "
        "vẽ quanh vị trí thật mà chu vi của nó bao 50% tổng số vị trí chỉ thị. Thứ hai, thông dụng "
        "hơn, là sai số bình phương trung bình (rms):"))
    b.append(eq("rms = √( (1/<i>N</i>) · Σ<sub><i>n</i>=1</sub><sup><i>N</i></sup> "
                "<i>E</i><sub><i>n</i></sub><sup>2</sup> )", "10.105"))
    b.append(p(
        "trong đó <i>E</i> là khoảng cách giữa vị trí thực và vị trí dự đoán, <i>N</i> là số vị trí "
        "dự đoán."))
    b.append(p(
        "Một vòng tròn, như trên Hình 10-29, có bán kính bằng một giá trị rms được kỳ vọng chứa 68% "
        "tổng số vị trí chỉ thị. Một vòng tròn khác có bán kính bằng 2 rms phải chứa 95% tổng số vị "
        "trí chỉ thị, với tán xạ hay sai số đẳng hướng."))

    b.append(fig(29, hb10fig.fig_10_29()))

    b.append(p(
        "Trong các hệ dẫn đường điện tử, có ba loại độ chính xác quan trọng: (1) độ chính xác dự "
        "đoán hay tuyệt đối — độ chính xác của một vị trí so với toạ độ địa lý của Trái Đất; (2) độ "
        "chính xác lặp lại — độ chính xác mà người dùng có thể quay lại một vị trí đã được xác định "
        "toạ độ trước đó bằng cùng hệ dẫn đường; và (3) độ chính xác tương đối — độ chính xác mà "
        "người dùng có thể đo vị trí của mình so với vị trí của một người dùng khác của cùng hệ, tại "
        "cùng thời điểm."))

    b.append(h3("Các hệ dẫn đường vô tuyến", "Radionavigation Systems"))
    b.append(p(
        "Vào thập niên 1930, các kỹ thuật tìm hướng vô tuyến được cải thiện cùng thiết bị tốt hơn đã "
        "dẫn tới việc hình thành những hệ gọi là radiobeacon. Các hệ này gồm những máy phát vô tuyến "
        "nhỏ đặt ở những nơi cố định, cung cấp phương vị vô tuyến dùng được trong mọi điều kiện thời "
        "tiết. Việc xác định vị trí bằng các beacon này được gọi là dẫn đường vô tuyến. Sự tinh luyện "
        "liên tục của công nghệ điện tử và hiểu biết tốt hơn về lan truyền sóng điện từ đã dẫn tới "
        "sự phát triển tiếp theo của radar và các hệ dẫn đường vô tuyến tầm xa hơn."))
    b.append(p(
        "Về bản chất, radiobeacon là những máy phát đơn lẻ, phát sóng liên tục ở công suất thấp, "
        "thường được điều chế bằng các ký tự mã Morse nghe được để nhận dạng. Tín hiệu phát được thu "
        "bằng một đầu thu trên khoang có gắn bộ tìm hướng vô tuyến (RDF) để xử lý tiếp."))

    b.append(h3("Các hệ định vị vô tuyến tầm ngắn và tầm trung",
                "Short- and Medium-Range Radiolocation Systems"))
    b.append(p(
        "Phần lớn các hệ dẫn đường tầm ngắn đến tầm trung được thiết kế để cung cấp hoặc một phương "
        "vị tới một trạm phát cố định, như trường hợp radiobeacon, hoặc một cự ly và phương vị từ "
        "máy phát tới một thiết bị trợ dẫn tự nhiên hay nhân tạo, như trường hợp radar."))

    b.append(h3("Các hệ dẫn đường hypebol tầm xa", "Long-Range Hyperbolic Navigation Systems"))
    b.append(p(
        "Các hệ dẫn đường điện tử tầm xa dựa trên các hệ hypebol. Trong những hệ này, đường vị trí "
        "cho ra theo từng đoạn hypebol chứ không phải theo các đường hướng tâm. Đường nối trạm chủ "
        "và trạm thứ cấp phát cùng một tín hiệu đồng thời gọi là đường đáy (baseline). Các đường "
        "hypebol biểu diễn quỹ tích mọi điểm mà xung của trạm chủ và trạm thứ cấp tới với một hiệu "
        "thời gian xác định. Điều này được minh hoạ trên Hình 10-30. Mọi thay đổi vị trí của máy thu "
        "ở gần đường đáy đều ứng với một thay đổi tương đối lớn của hiệu thời gian thu xung."))

    b.append(fig(30, hb10fig.fig_10_30()))

    b.append(p(
        "Trong thực tế, các trạm thứ cấp phát xung theo những khoảng cố định, gọi là độ trễ mã hoá, "
        "sau khi đã nhận được xung từ trạm chủ. Hiện nay, các hệ hypebol dùng chuẩn thời gian nguyên "
        "tử để điều hoà việc phát của cả trạm chủ lẫn trạm thứ cấp, nhằm tăng độ chính xác của hệ "
        "bằng cách loại bỏ sai số thời gian ngẫu nhiên do điều kiện khí quyển."))
    b.append(p(
        "Ở một số hệ, thay cho xung ngắn, người ta truyền sóng liên tục mà sườn trước của mỗi chu "
        "kỳ biểu diễn một khoảng thời gian và khoảng cách cho trước. Các hypebol tương ứng khi đó "
        "biểu diễn quỹ tích những điểm có hiệu pha không đổi, gọi là các đường đẳng pha. Khoảng không "
        "gian giữa các hypebol gọi là làn. Vị trí của máy thu trong một làn được xác định bằng độ "
        "lệch pha giữa tín hiệu trạm chủ và trạm thứ cấp. Một nhược điểm của hệ này là không thể phân "
        "biệt làn này với làn khác chỉ bằng so pha. Do đó, các làn phải hoặc được đếm khi đi qua kể "
        "từ một vị trí cố định, hoặc phải được nhận dạng bằng cách khác. Để có độ chính xác tốt, cự "
        "ly của người dùng tới các trạm hiếm khi được vượt quá khoảng sáu lần chiều dài đường đáy."))

    b.append(h4("Radiobeacon", "Radiobeacons"))
    b.append(p(
        "Phần lớn tín hiệu radiobeacon bị giới hạn dưới 320 km (200 dặm), đa số không thu được quá "
        "khoảng 32 km (20 dặm). Thường thì các radiobeacon trong một khu vực được nhóm trên một tần "
        "số chung, sao cho mỗi máy phát chỉ phát trong một đoạn của kế hoạch chia thời gian. Phương "
        "vị vô tuyến tới vị trí máy phát được xác định bằng một máy thu có gắn bộ tìm hướng vô tuyến "
        "(RDF). Có loại RDF giá vừa phải, vận hành bằng tay, và cũng có vài mẫu tự động hoàn toàn đắt "
        "hơn. Theo lệ thường, phương vị RDF chỉ được coi là chính xác trong phạm vi ±2° — ví dụ ở cự "
        "ly dưới 200 km (120 dặm) tới máy phát trong điều kiện thuận lợi — và ±5° đến 10° khi điều "
        "kiện bất lợi."))
    b.append(p(
        "Thông tin về vị trí, tầm hoạt động và thủ tục sử dụng radiobeacon có trong nhiều ấn phẩm, ví "
        "dụ ấn phẩm số 117 của DMAHTC, <em>The Radio Navigation Aids</em>. Phương vị radiobeacon đúng "
        "được vẽ trên hải đồ Mercator để ước lượng vị trí. Vì có thể thiếu chính xác, radiobeacon "
        "không được dùng phổ quát. Những người đi biển như thuyền nhỏ và tàu buôn không được trang bị "
        "hệ khác thì dùng radiobeacon."))

    b.append(h4("Loran-C", "Loran-C"))
    b.append(p(
        "Loran được phát triển từ thập niên 1940, là một trong những hệ đầu tiên hiện thực hoá một "
        "hệ hypebol tầm xa cho cả tàu thuỷ lẫn máy bay. Hệ dùng trạm chủ và trạm tớ phát sóng vô "
        "tuyến tuần tự trong nửa trên của băng MF, với tần số 1850 kHz đến 1950 kHz. Loran-A có vùng "
        "phủ sóng đất tới 700–1250 km tính từ đường đáy vào ban ngày, và tới 2200 km vào ban đêm. Nó "
        "là hệ dẫn đường điện tử được dùng rộng rãi nhất cho tới năm 1970. Về sau, một hệ dùng xung "
        "đồng bộ cho cả phép đo hiệu thời gian lẫn so pha được phát triển, gọi là Loran-C. Loran-C "
        "được cấu hình để hoạt động theo kiểu chuỗi, gồm nhiều hơn một trạm tớ, thường bố trí thành "
        "tam giác."))
    b.append(p(
        "Mọi trạm trong hệ đều phát tín hiệu trên một tần số sóng mang chung ở giữa băng LF, "
        "100 kHz ± 10 kHz. Tầm sóng đất khoảng 1900 km. Sóng trời một lần phản xạ có tầm khoảng "
        "3600 km, và tín hiệu hai lần phản xạ đã được ghi nhận ở cách trạm mặt đất khoảng 6250 km. "
        "Sóng trời một lần phản xạ xuất hiện cả ngày lẫn đêm, còn sóng trời hai lần phản xạ chỉ hình "
        "thành ban đêm. Các chuỗi Loran-C hiện nay có đường đáy dài 1500 km đến 2300 km. Độ chính "
        "xác của hệ thay đổi từ khoảng ±200 m rms gần đường đáy tới ±600 m rms ở gần giới hạn tầm "
        "xa nhất. Các kỹ thuật vi phân dùng những năm gần đây đã tăng độ chính xác. Tần số thấp và "
        "công suất lớn của máy phát cho phép sóng đất xuyên qua lớp bề mặt nước biển, giúp tàu ngầm "
        "đang lặn thu được tín hiệu."))
    b.append(p(
        "Để giảm yêu cầu công suất lớn, người ta dùng tín hiệu nhiều xung. Tín hiệu nhiều xung của "
        "mỗi trạm chủ và các trạm thứ cấp đi kèm được phát theo một trình tự định trước, như trên "
        "Hình 10-31. Tám trong số chín xung cách nhau 1 ms, xung thứ chín cách 2 ms. Xung của trạm "
        "chủ và trạm thứ cấp sau khi tích phân được so sánh tại một điểm lấy mẫu đúng 30 µs kể từ "
        "sườn trước của chúng."))

    b.append(fig(31, hb10fig.fig_10_31()))

    b.append(p(
        "Các đầu thu Loran-C hoàn toàn tự động, phù hợp cho ứng dụng hàng hải, xe trên bộ và máy "
        "bay. Phần lớn đầu thu cho số đọc trực tiếp vĩ độ/kinh độ dưới dạng số, chính xác tới một "
        "phần mười phút cung. Chúng cũng có các tính năng phụ như chọn điểm đến, hướng và tốc độ "
        "trên mặt đất… Sau khi được khởi tạo, đầu thu tự chọn chuỗi tốt nhất và các xung chủ/tớ "
        "thích hợp nhất. Trên thế giới có 13 chuỗi Loran-C. Mỗi chuỗi dùng một tốc độ lặp xung (PRR) "
        "và khoảng lặp xung (PRI) cơ bản khác nhau. PRI cụ thể dùng cho một chuỗi gọi là khoảng lặp "
        "nhóm (GRI), thường gọi là tốc độ (rate). Hệ này mở rộng mạnh từ thập niên 1970 và thu hút "
        "nhiều người dùng. Nó có mặt trên tàu thuỷ, máy bay và cả xe trên bộ. Xe trên bộ được trang "
        "bị các hệ tự động định vị phương tiện (AVLS). Trong một ứng dụng ở Hoa Kỳ, hệ AVLS được "
        "tích hợp với hệ thống điện thoại khẩn cấp của thành phố và một hệ điều phối có máy tính hỗ "
        "trợ để kiểm soát vị trí các xe khẩn cấp như xe cứu thương và xe cứu hoả."))
    b.append(p(
        "Tuy vậy, những tiến bộ của các hệ định vị toàn cầu dựa trên vệ tinh (GPS) đòi hỏi phải chấm "
        "dứt Loran-C trong tương lai rất gần. Tuy nhiên, việc tắt hẳn hệ có thể không xảy ra ngay, vì "
        "số người dùng hiện tại của hệ rất lớn."))

    b.append(h4("Decca", "Decca"))
    b.append(p(
        "Decca giống Loran-C ở chỗ mỗi chuỗi gồm một trạm chủ và ba trạm tớ bố trí theo hình sao, "
        "với góc khoảng 120° giữa các đường đáy. Nó dùng sóng liên tục không điều chế thay cho sóng "
        "xung của Loran. Lưới hypebol đặc trưng được hình thành bằng so pha tín hiệu trạm chủ và "
        "trạm tớ. Mọi trạm phát trong băng LF, giữa 70 kHz và 130 kHz. Tầm danh định khoảng 400 km cả "
        "ngày lẫn đêm. Hệ rất chính xác trong phạm vi hoạt động. Tín hiệu do mỗi trạm phát đều là "
        "hoạ ba của một tần số cơ bản duy nhất."))
    b.append(p(
        "Có rất nhiều loại đầu thu cho hệ Decca, kể cả nhật ký bay tự động cho máy bay. Nói chung, "
        "hệ gồm bốn đầu thu riêng biệt, mỗi cái có thể đặt để thu một trong bốn tín hiệu do một "
        "chuỗi phát đi. Việc nhận dạng làn được thực hiện nhờ một tín hiệu do mỗi trạm chủ và trạm "
        "tớ phát, cứ 20 s một lần, kéo dài 0,6 s. Nhờ vài lần ngắt tín hiệu ngắn và việc phát đồng "
        "thời các hoạ ba, các vùng và các làn được nhận dạng một cách chính xác."))

    b.append(h4("Consol", "Consol"))
    b.append(p(
        "Consol chỉ giới hạn ở vùng Đông và Bắc Đại Tây Dương. Đây là một hệ hypebol có đường đáy "
        "cực ngắn, đến mức tạo thành một hình hypebol bị suy biến. Hệ dùng ba tháp đặt cách nhau ba "
        "bước sóng. Tần số làm việc nằm trong băng MF, giữa 250 kHz và 370 kHz. Tầm của hệ khoảng "
        "1900 km ban ngày và 2400 km ban đêm. Tầm tối thiểu khoảng 40 km ở gần các trạm. Một tháp "
        "phát sóng liên tục, các tháp khác phát sóng lệch pha 180° theo một chu kỳ khoá. Tín hiệu "
        "được điều chế bằng chấm và gạch, sao cho đầu thu xác định vị trí bằng cách đếm chúng và in "
        "lên lưới Consol."))

    b.append(h4("Omega", "Omega"))
    b.append(p(
        "Omega là một hệ dẫn đường hypebol phủ toàn thế giới chỉ với tám trạm phát, cách nhau 7500 km "
        "đến 9500 km. Hệ phát trên các tần số trong băng VLF, từ 10 kHz đến 14 kHz, với công suất "
        "10 kW. Tại bất kỳ vị trí nào trên Trái Đất đều thu được tín hiệu của ít nhất ba và thường "
        "là bốn trạm."))
    b.append(p(
        "Dải tần 10 kHz đến 14 kHz được chọn riêng để tận dụng vài đặc tính lan truyền thuận lợi: "
        "(1) dùng bề mặt Trái Đất và tầng điện ly như một ống dẫn sóng; (2) cho phép tàu ngầm đang "
        "lặn thu được tín hiệu; và (3) tạo được các đường đáy dài 7500 km đến 9500 km."))
    b.append(p(
        "Tần số cơ bản mà cả tám trạm phát là 10,2 kHz. Mỗi trạm phát bốn tín hiệu dẫn đường cùng một "
        "tín hiệu thời gian, với các chuẩn tần số nguyên tử bảo đảm mọi trạm được giữ đồng pha chính "
        "xác. Hai sóng liên tục đồng pha nhưng truyền ngược chiều nhau tạo ra một loạt làn Omega. "
        "Trong mỗi làn, phép đo hiệu pha sẽ chạy từ 0° đến 360° khi máy thu dịch qua, như trên "
        "Hình 10-32. Hai làn Omega hợp thành một chu kỳ, cho bước sóng 25 km và làn 12 km, mở rộng "
        "dần khi khoảng cách tới đường đáy tăng. Các làn được nhận dạng nhờ ba tín hiệu khác do mỗi "
        "trạm phát theo kiểu ghép kênh. Độ chính xác của các điểm định vị Omega là trong phạm vi "
        "±1,5 km rms ban ngày và ±3 km rms ban đêm. Các kỹ thuật vi phân có thể giảm mạnh sai số "
        "này."))

    b.append(fig(32, hb10fig.fig_10_32()))

    b.append(p(
        "Đầu thu Omega là những bộ hoàn toàn tự động, cho số đọc trực tiếp vĩ độ/kinh độ với giá "
        "khoảng 1000 USD cho ứng dụng hàng hải và hàng không. Tuy vậy, vì độ chính xác của hệ không "
        "bằng các hệ khác, chúng chủ yếu được dùng làm hệ dự phòng."))

    b.append(h4("Radar", "Radar"))
    b.append(p(
        "Từ này bắt nguồn từ “radio detection and ranging” (phát hiện và đo cự ly bằng vô tuyến). Nó "
        "hoạt động theo nguyên lý phản xạ cơ bản: xác định thời gian để một xung RF đi từ nguồn phát "
        "tới mục tiêu rồi trở về dưới dạng sóng dội. Phần lớn sóng điện từ cao tần của radar tìm kiếm "
        "mặt nước và radar dẫn đường được một ăng ten parabol tạo thành chùm, như trên Hình 10-33. "
        "Ăng ten thu được quay để quét toàn bộ vùng xung quanh, và phương vị tới mục tiêu được xác "
        "định bằng hướng của ăng ten tại đúng thời điểm sóng dội trở về. Một radar tiêu chuẩn gồm "
        "năm bộ phận: máy phát, bộ điều chế, ăng ten, máy thu và bộ chỉ thị. Chúng hoạt động theo "
        "kiểu điều xung."))
    b.append(p(
        "Radar là thiết bị cực kỳ quan trọng cho các ứng dụng kiểm soát không lưu. Ngày nay, các hệ "
        "radar beacon trên không đã phát triển tốt trong các hệ cảnh báo giao thông và tránh va chạm "
        "(TCAS). Trong hệ này, mỗi máy bay liên tục phát một tín hiệu hỏi, được mọi máy bay lân cận "
        "có trang bị thích hợp thu nhận. Tín hiệu kích hoạt một bộ phát đáp trên máy bay mục tiêu; bộ "
        "này phát đi một số thông tin về vị trí ba chiều và nhận dạng."))

    b.append(fig(33, hb10fig.fig_10_33()))

    b.append(h3("Các hệ chuyển tiếp vệ tinh", "Satellite Relay Systems"))
    b.append(p(
        "Dùng vệ tinh là một công nghệ đã phát triển cao và được khai thác rộng khắp thế giới. Trong "
        "hai thập kỷ qua, nó đã chuyển từ bản chất gần như thử nghiệm sang cung cấp thường xuyên "
        "những dịch vụ mới. Các hệ tận dụng đặc tính riêng của quỹ đạo vệ tinh địa tĩnh (GSO). Việc "
        "thiết kế hệ vệ tinh đã được hiểu rõ, nhưng công nghệ vẫn còn năng động. Vệ tinh hữu ích cho "
        "dịch vụ thông tin đường dài, cho dịch vụ xuyên đại dương hoặc qua địa hình khó, và cho dịch "
        "vụ điểm–đa điểm như phân phối truyền hình."))
    b.append(p(
        "Việc phân bổ tần số cho vệ tinh do Liên minh Viễn thông Quốc tế (ITU) quản lý. Ở Hoa Kỳ, Uỷ "
        "ban Truyền thông Liên bang (FCC) thực hiện phân bổ và ấn định tần số cho các ứng dụng vệ "
        "tinh phi chính phủ. FCC đặt ra một số điều kiện về chế tạo và bảo trì vệ tinh trên quỹ "
        "đạo."))
    b.append(p(
        "Có nhiều hệ vệ tinh do các tổ chức và quốc gia khác nhau vận hành, chủ yếu phát triển cho "
        "thông tin và truyền dữ liệu, trong đó có: Iridium của Motorola, Globalstar của Loral "
        "Corporation, Intelsat, loạt CS của Nhật Bản, Turksat của Thổ Nhĩ Kỳ, Aussat của Ô-xtrây-li-a, "
        "Galaxy và Satcom của Hoa Kỳ, Anik của Ca-na-đa, TDF của Pháp… Một số hệ vệ tinh thông tin "
        "thích hợp cho mục đích dẫn đường. Tuy nhiên, số hệ vệ tinh được thiết kế riêng cho dẫn "
        "đường thì ít. Những hệ được thiết lập vững chắc và dễ tiếp cận nhất với người dùng dân sự "
        "và thương mại là GPS của Hoa Kỳ và Glonass của Nga."))
    b.append(p(
        "Thế hệ vệ tinh đầu tiên là hệ vệ tinh Hải quân (Navsat), đi vào hoạt động tháng 1 năm 1964 "
        "sau khi phóng thành công vệ tinh Transit đầu tiên vào quỹ đạo cực. Hệ được tuyên bố mở cho "
        "sử dụng tư nhân và thương mại năm 1967. Tên gọi dân sự của hệ là Hệ dẫn đường vệ tinh "
        "Transit, hay gọn là Transit. Về sau, hệ này tiến hoá thành hệ Navsat GPS hiện đại, sẽ được "
        "bàn chi tiết. Phần lớn các nguyên lý hoạt động trình bày ở đây được hệ GPS kế thừa."))
    b.append(p(
        "Hệ Transit gồm các vệ tinh đang hoạt động cùng vài vệ tinh dự phòng trên quỹ đạo, một mạng "
        "trạm theo dõi mặt đất, một trung tâm tính toán, một trạm “bơm” dữ liệu, tín hiệu thời gian "
        "của đài thiên văn hải quân, và các tổ hợp đầu thu – máy tính. Vệ tinh Transit chạy trên quỹ "
        "đạo cực tròn, cao khoảng 1075 km, chu kỳ quay khoảng 107 phút. Do Trái Đất quay bên dưới vệ "
        "tinh, mọi vị trí trên Trái Đất đều nằm trong tầm của mỗi vệ tinh ít nhất hai lần một ngày, "
        "cách nhau 12 h. Theo thiết kế ban đầu, nếu có ít nhất năm vệ tinh hoạt động tại một thời "
        "điểm, khoảng thời gian trung bình giữa hai cơ hội định vị sẽ từ khoảng 95 phút gần xích đạo "
        "xuống còn khoảng 35 phút hoặc ít hơn ở trên 70° vĩ Bắc và Nam."))
    b.append(p(
        "Hệ Transit dựa trên độ dịch Doppler của hai tần số 150 MHz và 400 MHz, được mỗi vệ tinh phát "
        "đồng thời khi nó chuyển động trên quỹ đạo với vận tốc tiếp tuyến khoảng 7,5 km/s. Hai tần số "
        "được dùng để đầu thu có thể bù trừ ảnh hưởng của tầng điện ly và khúc xạ khí quyển lên tín "
        "hiệu vệ tinh tới. Mỗi tần số được điều chế bằng một tín hiệu dữ liệu lặp lại kéo dài 2 "
        "phút, mang thời gian vệ tinh hiện thời, các tham số quỹ đạo và thông tin khác. Trong đầu "
        "thu, một tín hiệu Doppler duy nhất được tạo ra bằng cách xử lý hai tín hiệu vệ tinh phát. Vẽ "
        "tần số của tín hiệu này theo thời gian sẽ được một đường cong đặc trưng như trên Hình "
        "10-34. Vì tần số tín hiệu phát bị nén lại khi vệ tinh tới gần — theo đúng tỉ lệ hình chiếu "
        "của vectơ vận tốc mà đầu thu nhìn thấy — đường cong bắt đầu tại thời điểm <i>T</i><sub>1</sub> "
        "với tần số cao hơn tần số phát vài chu kỳ."))

    b.append(fig(34, hb10fig.fig_10_34()))

    b.append(p(
        "Các trạm theo dõi ghi lại quan sát Doppler và số đọc bộ nhớ thu được trong mỗi lần vệ tinh "
        "đi qua để chuyển về trung tâm tính toán. Dữ liệu cập nhật về vị trí quỹ đạo và thời gian "
        "được chuyển từ trung tâm tính toán tới một trạm “bơm”, rồi phát lên vệ tinh theo từng cụm "
        "mỗi 12 h một lần. Bức điện bơm dài 15 s chứa đủ dữ liệu cho 16 h phát liên tiếp, mỗi lần 2 "
        "phút, mô tả vị trí quỹ đạo hiện thời của vệ tinh."))
    b.append(p(
        "Độ chính xác của hệ phụ thuộc độ chính xác tính quỹ đạo vệ tinh, ảnh hưởng của khúc xạ tầng "
        "điện ly, độ chính xác xác định tốc độ và hướng của đầu thu. Trong điều kiện tối ưu, hệ có "
        "thể cho các điểm định vị với sai số rms cực đại khoảng 35 m cho đầu thu đứng yên ở bất kỳ "
        "đâu trên Trái Đất. Tuy vậy, nếu một vị trí được đo trong vài tuần, có thể đạt độ chính xác "
        "tốt hơn 1 m. Tín hiệu thời gian phát dưới dạng một “tiếng bíp” ở cuối mỗi chu kỳ phát 2 phút "
        "trùng với phút chẵn của Giờ Phối hợp Quốc tế, nên có thể dùng để kiểm tra đồng hồ."))
    b.append(p(
        "Còn những hệ vệ tinh khác, đã có hoặc đang trong giai đoạn quy hoạch, phù hợp cho dẫn đường. "
        "Một số hệ như: vệ tinh Marec làm việc ở VHF, thuộc tổ hợp liên chính phủ INMARSAT; Geostar "
        "tư nhân cung cấp dịch vụ cho công nghiệp dầu khí; và nhiều hệ khác cung cấp dịch vụ thông "
        "tin liên lục địa, dẫn đường và cả cảm nhận vị trí, ví dụ SATCOM, ARINC’s, Avsat, Starfix…"))

    b.append(h3("Bộ phát đáp", "Transponders"))
    b.append(p(
        "Bộ phát đáp là những bộ chuyển đổi, đáp lại tín hiệu tới bằng cách sinh ra thông điệp trả "
        "lời thích hợp. Những tiến bộ công nghệ gần đây đã cho phép cấu hình bộ phát đáp nhờ xử lý "
        "tín hiệu trên khoang mạnh và tinh vi. Điều này nâng cao năng lực nhờ cải thiện ngân quỹ "
        "đường truyền, nhờ điều chỉnh giản đồ ăng ten và nhờ đưa tài nguyên vệ tinh phục vụ theo yêu "
        "cầu — gọi là khái niệm “tổng đài trên trời”."))
    b.append(p(
        "Sự quan tâm tăng lên đối với thăm dò biển sâu đã đưa các bộ phát đáp âm học lên hàng đầu như "
        "một công cụ dẫn đường quan trọng. Chúng cung cấp thông tin vị trí ba chiều cho các phương "
        "tiện và thiết bị lặn."))
    b.append(p(
        "Một số bộ phát đáp dựa trên tín hiệu radar, đáp lại khi bị radar chiếu tới. Bộ phát đáp được "
        "lập trình để nhận dạng bạn hay thù, hoặc trong một số trường hợp chỉ đơn giản thông báo cho "
        "trạm mặt đất về vị trí máy bay."))
    b.append(p(
        "Bộ phát đáp được dùng để cảnh báo khẩn cấp. Vệ tinh Hoa Kỳ và Ca-na-đa mang bộ phát đáp "
        "Sarsat, vệ tinh Nga mang bộ phát đáp Cospas. Chúng cũng được dùng làm thiết bị cảnh báo "
        "trong các hệ tránh va chạm trên máy bay và xe trên bộ."))

    b.append(h3("Các hệ dẫn đường vệ tinh toàn cầu", "Global Satellite Navigation Systems"))
    b.append(h4("Hệ GPS", "The GPS System"))
    b.append(p(
        "Các hệ dẫn đường vệ tinh toàn cầu là thế hệ vệ tinh thứ hai, tiến hoá chủ yếu từ Hệ định vị "
        "toàn cầu của Hải quân. Chúng cung cấp năng lực xác định vị trí ba chiều liên tục (vĩ độ, "
        "kinh độ và độ cao), khác với thông tin hai chiều định kỳ của hệ Transit. Hai mươi bốn vệ "
        "tinh hoạt động, như trên Hình 10-35, hợp thành hệ. Quỹ đạo mỗi vệ tinh là đường tròn, cao "
        "khoảng 2200 km, nghiêng một góc 55° so với trục Trái Đất."))
    b.append(note(
        "Con số 2200 km trong bản gốc là lỗi ấn loát: quỹ đạo GPS thực tế ở độ cao khoảng 20 200 km, "
        "tức bán kính quỹ đạo chừng 26 560 km, chu kỳ 11 h 58 min. Nếu quả thật chỉ 2200 km thì 24 vệ "
        "tinh không thể phủ liên tục toàn cầu như mô tả ở đoạn dưới."))

    b.append(fig(35, hb10fig.fig_10_35()))

    b.append(p(
        "Việc xác định vị trí bằng hệ GPS dựa trên khả năng của đầu thu xác định chính xác khoảng "
        "cách tới các vệ tinh GPS đang ở trên đường chân trời của người dùng tại thời điểm định vị. "
        "Nếu biết chính xác khoảng cách tới hai vệ tinh như vậy và biết độ cao, thì xác định được vị "
        "trí. Để làm được điều đó, đầu thu cần biết chính xác thời điểm tín hiệu được phát và thời "
        "điểm nó được thu. Nếu biết tốc độ lan truyền qua khí quyển, có thể tính được cự ly tương "
        "ứng. Các cự ly đo được gọi là giả cự ly. Ngày nay, thông thường tín hiệu được thu từ ít "
        "nhất bốn vệ tinh, cho phép tính điểm định vị chính xác. Sai số thời gian cộng với sai số tốc "
        "độ lan truyền dẫn tới sai số cự ly chung cho mọi đầu thu GPS. Thời gian là tham số thứ tư "
        "được đầu thu đánh giá nếu thu được ít nhất bốn vệ tinh tại một thời điểm. Nếu thu được vệ "
        "tinh thứ năm, có thể đánh giá thêm một ma trận sai số."))
    b.append(p(
        "Mỗi vệ tinh GPS phát đồng thời trên hai tần số để xác định và loại bỏ ảnh hưởng của tầng "
        "điện ly và khí quyển. Các tần số Navstar là 1575,42 MHz và 1227,6 MHz, được gọi là L1 và L2 "
        "trong băng L của dải UHF. Cả hai tín hiệu đều được điều chế bằng thông điệp dẫn đường 30 s, "
        "phát ở 50 bit/s. 18 s đầu của mỗi khung 30 s chứa dữ liệu lịch thiên (ephemeris) của chính "
        "vệ tinh đó, xác định vị trí vệ tinh như một hàm của thời gian. 12 s còn lại là dữ liệu niên "
        "lịch (almanac), xác định quỹ đạo và trạng thái hoạt động của mọi vệ tinh trong hệ. Đầu thu "
        "GPS lưu và dùng dữ liệu lịch thiên để xác định giả cự ly, dùng dữ liệu niên lịch để giúp "
        "chọn bốn vệ tinh tốt nhất cho dữ liệu vị trí tại mỗi thời điểm. Tuy vậy, triết lý “bốn vệ "
        "tinh tốt nhất” đã dần bị triết lý “nhìn thấy tất cả” thay thế."))
    b.append(p(
        "Các tín hiệu dẫn đường L1 và L2 còn được điều chế bằng hai chuỗi nhị phân bổ sung: mã C/A "
        "để thu nhận dẫn đường thô, và mã P để đo cự ly chính xác. Tín hiệu L1 được điều chế bằng cả "
        "mã C/A lẫn mã P, còn L2 chỉ bằng mã P. Chỉ dùng mã C/A thường cho độ chính xác vị trí khoảng "
        "20 m rms. Tuy nhiên, mã P không dành cho người dùng dân sự. Mã P được đặt lại tên thành mã "
        "Y, chỉ giải mã được bằng các đầu thu chính xác cao có quyền truy cập thông tin mã hoá trong "
        "thông điệp vệ tinh. Dù vậy, cũng phải công bằng mà nói rằng giới dân sự đã tìm ra cách hưởng "
        "lợi từ tín hiệu P/Y mà không thực sự biết mã, tuy với tỉ số tín hiệu trên nhiễu thấp hơn. "
        "Hơn nữa, mã C/A bị làm suy giảm bằng cách chèn các sai số ngẫu nhiên, khiến độ chính xác vị "
        "trí bị giới hạn ở 50 m rms cho giá trị ngang và 70 m cho giá trị thẳng đứng. Dự kiến các "
        "sai số này sẽ được dỡ bỏ vào năm 2006. Người dùng dân sự được dùng cái gọi là Dịch vụ định "
        "vị tiêu chuẩn (SPS) chính xác tới 50 m rms, còn người dùng quân sự Hoa Kỳ và NATO dùng Dịch "
        "vụ định vị chính xác (PPS)."))
    b.append(note(
        "Đây là đoạn viết năm 1999. Trên thực tế, cơ chế làm suy giảm có chủ ý nói trên — gọi là "
        "Selective Availability — đã được tắt ngày 2 tháng 5 năm 2000, sớm hơn mốc 2006 nêu trong "
        "bản gốc, và độ chính xác dân sự tức thì nhảy lên cỡ 10–15 m."))

    b.append(p(
        "Để nâng cao độ chính xác của SPS, có thể áp dụng các kỹ thuật vi phân cho cả tín hiệu GPS đã "
        "mã hoá, như trên Hình 10-36. Vì đầu thu tham chiếu đặt ở một vị trí đã biết, nó có thể tính "
        "được các cự ly đúng từ các giả cự ly tại mọi thời điểm. Hiệu giữa giả cự ly đo được và cự ly "
        "tính được cho ra các hệ số hiệu chỉnh. Có thể đạt độ chính xác dưới 1 m trong các phép đo "
        "cả khi đứng yên lẫn khi chuyển động. Gần đây, các đầu thu vi phân trở nên phổ biến, cho độ "
        "chính xác trong dải dưới xentimét. Chúng ngày càng rẻ và đang được ứng dụng ở nhiều lĩnh "
        "vực như máy bay, phương tiện giao thông thông dụng, ô-tô, khảo sát địa chất, thể thao định "
        "hướng, nông nghiệp…"))

    b.append(fig(36, hb10fig.fig_10_36()))

    b.append(p(
        "Hiện có ba kiểu đầu thu GPS cơ bản được thiết kế và chế tạo để phục vụ các nhóm người dùng "
        "khác nhau: kiểu tuần tự chậm, kiểu tuần tự nhanh và kiểu bám liên tục. Loại ít phức tạp "
        "nhất và rẻ nhất cho phần lớn ứng dụng là kiểu tuần tự chậm, chỉ dùng một kênh đo để thu mã "
        "C/A trên L1 của từng vệ tinh theo trình tự, mỗi 1,2 s một lần, thỉnh thoảng ngắt để thu dữ "
        "liệu lịch thiên và niên lịch. Sau khi nhận dữ liệu, việc tính toán hoàn tất trong 5 s, nên "
        "hệ phù hợp cho việc định vị khi đứng yên hoặc gần như đứng yên."))
    b.append(p(
        "Đầu thu tuần tự nhanh có hai kênh: một kênh đo giả cự ly liên tục, kênh kia thu dữ liệu lịch "
        "thiên và niên lịch. Kiểu này dùng cho các ứng dụng động lực trung bình như xe trên bộ."))
    b.append(p(
        "Đầu thu bám liên tục dùng nhiều kênh (ít nhất năm) để theo dõi, tính và xử lý giả cự ly tới "
        "nhiều vệ tinh đang dùng đồng thời, nhờ đó đạt độ chính xác cao nhất có thể và phù hợp cho "
        "các ứng dụng động lực cao như máy bay và tên lửa. Các đầu thu nhiều kênh song song ngày nay "
        "hiệu quả về chi phí đến mức các kiểu khác có khả năng sẽ biến mất."))
    b.append(p(
        "Một số công ty sản xuất đầu thu GPS rất tinh vi. Các đầu thu GPS EURONAV hoạt động trên hai "
        "và năm kênh cho ứng dụng quân sự. Chúng có các tính năng như thời gian chính xác, giao diện "
        "với dụng cụ bay số, giao diện RS-422, đầu vào đo cao kế, tự khởi tạo…"))
    b.append(p(
        "Nhiều nhà chế tạo cung cấp các chức năng quản lý vệ tinh thực hiện bằng phần mềm với những "
        "tính năng khác nhau. Ví dụ, với các đầu thu NAVSTAR GPS của Bộ Quốc phòng, ba yêu cầu chức "
        "năng được hiện thực: (1) quản lý cơ sở dữ liệu niên lịch, lịch thiên và dữ liệu hiệu chỉnh "
        "tất định của vệ tinh; (2) tính vị trí và vận tốc vệ tinh chính xác cho phần mềm dẫn đường "
        "dùng; (3) dùng dữ liệu vị trí vệ tinh và vị trí đầu thu để định kỳ tính chòm bốn vệ tinh có "
        "hình học tối ưu cho dẫn đường. Các đầu thu của Bộ Quốc phòng được chia theo ba chức năng: "
        "Quản lý vệ tinh (SM), Quản lý cơ sở dữ liệu vệ tinh (SDBM), Vị trí – vận tốc – gia tốc vệ "
        "tinh (SVPVA) và Chọn vệ tinh (SS)."))
    b.append(p(
        "Dẫn đường vi phân cũng được áp dụng khi một bộ người dùng đang dẫn đường tương đối so với "
        "một bộ người dùng khác qua một đường truyền dữ liệu. Trong một số trường hợp, một người "
        "dùng đã ở tại đích vào một thời điểm trước đó và đang dẫn đường tương đối so với toạ độ đo "
        "được tại điểm ấy. Giá trị thật của điểm định vị của đầu thu này được so với giá trị đo được, "
        "và hiệu của chúng trở thành các hiệu chỉnh vi phân. Các hiệu chỉnh này được truyền tới các "
        "bộ người dùng trong khu vực theo thời gian thực, hoặc được ghi lại để dùng sau phi vụ, sao "
        "cho các điểm định vị không còn độ lệch gắn với GPS."))
    b.append(p(
        "Dẫn đường vi phân và các hệ GPS có mặt trong dẫn đường trên đường bay cho hàng không dân "
        "dụng và thương mại, trong ứng dụng quân sự, trong dẫn đường tàu thuỷ đặc biệt ở vùng nước "
        "nông, trong giữ vị trí máy bay, trong thăm dò địa chấn – địa vật lý, trong khảo sát đất "
        "đai, trong điều khiển phương tiện giao thông và giao thông, v.v."))

    b.append(h4("Glonass", "The Glonass"))
    b.append(p(
        "Có một số hệ dẫn đường vệ tinh khác tương tự GPS của Hoa Kỳ, ví dụ Glonass của Nga. Glonass "
        "gồm 24 vệ tinh chạy trên quỹ đạo tròn ở độ cao 1500 km so với mặt đất. Độ chính xác của hệ "
        "khoảng 10 m rms. Vệ tinh Glonass phát chi tiết vị trí của chính nó và một mốc thời gian. Các "
        "tần số sóng mang nằm trong băng L, khoảng 1250 MHz (L2) và 1600 MHz (L1). Chỉ tần số L1 "
        "mang mã C/A dân sự. Các sóng mang vô tuyến mà Glonass dùng được chia kênh trong các băng "
        "1240–1260 MHz và 1597–1617 MHz, với khoảng cách kênh 0,4375 MHz ở các tần số thấp hơn và "
        "0,5625 MHz ở các tần số cao hơn. Số kênh là 24. Thông điệp dữ liệu Glonass được định dạng "
        "thành các khung 3000 bit, kéo dài 30 s. Dữ liệu lịch thiên được phát dưới dạng một bộ toạ độ "
        "vị trí, vận tốc và gia tốc trong một hệ toạ độ Descartes gắn với Trái Đất, gốc tại tâm Trái "
        "Đất (ECEF). Dữ liệu lịch thiên mới có mỗi nửa giờ và có giá trị cho mười lăm phút tiếp theo. "
        "Dữ liệu được phát ở tốc độ 50 baud và được chồng lên một mã giả ngẫu nhiên (PRN). Mã độ "
        "chính xác thấp có độ dài 511 bit, so với 1023 bit của Navstar. Độ chính xác của Glonass "
        "ngang với hệ GPS. Glonass và GPS dùng các hệ quy chiếu toạ độ và hệ thời gian khác nhau, và "
        "các hệ này đang được phối hợp với nhau."))
    b.append(note(
        "Tương tự trường hợp GPS ở trên, độ cao 1500 km trong bản gốc cũng là lỗi ấn loát: quỹ đạo "
        "Glonass thực tế ở khoảng 19 100 km, chu kỳ 11 h 15 min."))

    b.append(h4("Starfix", "The Starfix"))
    b.append(p(
        "Một hệ dựa trên vệ tinh đáng chú ý khác — được tài trợ tư nhân, tự phát triển, tự phóng và "
        "tự duy trì — là hệ định vị Starfix. Hệ này được thiết kế chủ yếu cho khảo sát dầu khí. Hệ "
        "gồm một trạm chủ sinh dữ liệu lịch thiên vệ tinh, và bốn vệ tinh trên quỹ đạo địa đồng bộ. "
        "Hệ được cho là có độ chính xác 2,5 m rms."))

    b.append(reflist([
        "M. Kayton, <em>Navigation — Land, Sea, Air and Space</em>, New York: IEEE Press, 1990.",
        "A. F. Inglis, <em>Electronic Communication Handbook</em>, New York: McGraw-Hill, 1988.",
        "J. Everet, <em>VSATs — Very Small Aperture Terminals</em>, IEEE Telecommunication Series 28, "
        "London: Peter Peregrinus Ltd., 1992.",
        "A. Leick, <em>GPS Satellite Surveying</em>, New York: John Wiley &amp; Sons, 1990.",
        "B. R. Elbert, <em>The Satellite Communication Applications Handbook</em>, Boston: Artech "
        "House, 1997.",
    ]))

    b.append(h4("Phụ lục — Danh mục nhà chế tạo và cung cấp",
                "Appendix — List of Manufacturers/Suppliers"))
    b.append(table(
        ["Nhà chế tạo / cung cấp", "Trụ sở"],
        [
            ("Advanced Videotech Co.", "Huntington Valley, PA"),
            ("AlliedSignal", "Morristown, NJ"),
            ("American GNC Corp.", "Chatsworth, CA"),
            ("Astroguide", "Lasalle, IL"),
            ("Colombia Elect. Int. Inc.", "Somis, CA"),
            ("Comstream", "San Diego, CA"),
            ("GE Co.", "Fairfield, CT"),
            ("Orbitron", "Spring Green, WI"),
            ("STI", "Hayward, CA"),
        ],
        "Bảng PL-10.4. Các nhà chế tạo và cung cấp thiết bị dẫn đường vệ tinh, theo phụ lục của "
        "mục 10.4."))

    # ------------------------------------------------------------ 10.5
    b.append(h2("10.5 Phát hiện hiện diện", "Occupancy Detection"))
    b.append(p("<em>Jacob Fraden</em>"))

    b.append(p(
        "Cảm biến hiện diện phát hiện sự có mặt của người trong một vùng được giám sát. Đầu dò "
        "chuyển động chỉ đáp lại những vật đang chuyển động. Khác biệt giữa hai loại là ở chỗ cảm "
        "biến hiện diện sinh tín hiệu bất kể vật đứng yên hay không, còn đầu dò chuyển động thì chỉ "
        "nhạy chọn lọc với vật đang chuyển động. Ứng dụng của những cảm biến này gồm an ninh, giám "
        "sát, quản lý năng lượng (điều khiển đèn điện), an toàn cá nhân, thiết bị gia dụng thân "
        "thiện, đồ chơi tương tác, sản phẩm mới lạ… Tuỳ ứng dụng, sự có mặt của con người có thể được "
        "phát hiện qua bất kỳ phương tiện nào gắn với một thuộc tính hay hành vi nào đó của cơ thể "
        "người [1]. Ví dụ, một đầu dò có thể nhạy với trọng lượng cơ thể, nhiệt, âm thanh, hằng số "
        "điện môi… Hiện nay, những loại đầu dò sau được dùng để cảm nhận sự hiện diện và chuyển động "
        "của người:"))

    b.append(
        '<ol class="plain">'
        "<li><b>Cảm biến áp suất không khí:</b> phát hiện thay đổi áp suất không khí do mở cửa ra "
        "vào.</li>"
        "<li><b>Điện dung:</b> phát hiện điện dung của cơ thể người.</li>"
        "<li><b>Âm học:</b> phát hiện âm thanh do người tạo ra.</li>"
        "<li><b>Quang điện:</b> phát hiện vật chuyển động cắt ngang chùm sáng.</li>"
        "<li><b>Quang điện tử:</b> phát hiện biến thiên độ rọi hoặc tương phản quang học trong vùng "
        "được bảo vệ.</li>"
        "<li><b>Công tắc thảm áp lực:</b> các dải dài nhạy áp lực đặt trên sàn dưới thảm để phát hiện "
        "trọng lượng của kẻ xâm nhập.</li>"
        "<li><b>Đầu dò ứng suất:</b> ten-xơ biến dạng nhúng trong dầm sàn, cầu thang và các kết cấu "
        "khác.</li>"
        "<li><b>Cảm biến công tắc:</b> tiếp điểm điện nối với cửa và cửa sổ.</li>"
        "<li><b>Công tắc từ:</b> phiên bản không tiếp xúc của cảm biến công tắc.</li>"
        "<li><b>Đầu dò rung:</b> phản ứng với rung của tường hoặc kết cấu công trình khác; cũng có "
        "thể gắn lên cửa hay cửa sổ để phát hiện chuyển động.</li>"
        "<li><b>Đầu dò vỡ kính:</b> cảm biến phản ứng với những rung đặc trưng do kính vỡ tạo "
        "ra.</li>"
        "<li><b>Đầu dò chuyển động hồng ngoại:</b> thiết bị nhạy với sóng nhiệt phát ra từ vật nóng "
        "hoặc lạnh đang chuyển động.</li>"
        "<li><b>Đầu dò vi ba:</b> cảm biến chủ động đáp lại tín hiệu điện từ vi ba phản xạ từ "
        "vật.</li>"
        "<li><b>Đầu dò siêu âm:</b> tương tự vi ba, chỉ khác là dùng sóng siêu âm thay cho bức xạ "
        "điện từ.</li>"
        "<li><b>Đầu dò chuyển động bằng video:</b> thiết bị video so sánh một ảnh tĩnh lưu trong bộ "
        "nhớ với ảnh hiện thời của vùng được bảo vệ.</li>"
        "<li><b>Đầu dò hệ la-de:</b> tương tự đầu dò quang điện, chỉ khác là dùng chùm sáng hẹp và "
        "các tổ hợp gương phản xạ.</li>"
        "<li><b>Đầu dò ma sát điện:</b> cảm biến có khả năng phát hiện điện tích tĩnh do vật chuyển "
        "động mang theo.</li>"
        "</ol>")

    b.append(p(
        "Một trong những điều gây bực bội nhất khi phát hiện hiện diện hay xâm nhập là báo động giả. "
        "Cụm “dương tính giả” nghĩa là hệ báo có xâm nhập trong khi không có. Trong một số ứng dụng "
        "không trọng yếu, nơi báo động giả thỉnh thoảng mới xảy ra — ví dụ một món đồ chơi hay một "
        "công tắc chuyển động điều khiển đèn trong phòng — điều này có thể không nghiêm trọng: đèn sẽ "
        "bật nhầm trong một thời gian ngắn, khó gây hại gì. Ở các hệ khác, đặc biệt những hệ dùng cho "
        "mục đích an ninh, báo động giả tuy nói chung không nguy hiểm bằng báo động âm (bỏ sót xâm "
        "nhập) nhưng lại có thể trở thành vấn đề nghiêm trọng. Khi chọn cảm biến cho ứng dụng trọng "
        "yếu, phải xét tới độ tin cậy, tính chọn lọc và khả năng chống nhiễu của nó. Một thực hành "
        "tốt thường được áp dụng là tạo một tổ hợp nhiều cảm biến với các mạch giao diện đối xứng; "
        "điều này có thể cải thiện đáng kể độ tin cậy của hệ, nhất là khi có nhiễu truyền dẫn từ bên "
        "ngoài. Một cách hiệu quả khác để giảm báo động nhầm là dùng các cảm biến hoạt động theo "
        "nguyên lý vật lý khác nhau [2]; ví dụ, kết hợp đầu dò điện dung với đầu dò hồng ngoại là "
        "một tổ hợp hiệu quả, vì chúng tiếp nhận những loại nhiễu truyền dẫn khác nhau."))

    b.append(h3("Cảm biến siêu âm", "Ultrasonic Sensors"))
    b.append(p(
        "Đầu dò siêu âm dựa trên việc phát sóng tới vật và thu sóng âm phản xạ. Sóng siêu âm là sóng "
        "cơ học, phủ một dải tần vượt xa khả năng của tai người, tức trên 20 kHz. Tuy nhiên, những "
        "tần số này lại khá dễ cảm nhận với các loài vật nhỏ như chó, mèo, gặm nhấm và côn trùng. "
        "Thật vậy, đầu dò siêu âm chính là cơ quan định vị sinh học của dơi và cá heo."))
    b.append(p(
        "Khi sóng tới đập vào một vật, một phần năng lượng bị phản xạ. Trong nhiều trường hợp thực "
        "tế, năng lượng siêu âm bị phản xạ theo kiểu tán xạ: bất kể năng lượng tới từ hướng nào, nó "
        "đều bị phản xạ gần như đều trong một góc khối rộng, có thể tới 180°. Nếu vật chuyển động, "
        "tần số sóng phản xạ sẽ khác tần số sóng phát. Đó là hiệu ứng Doppler (xem dưới đây). Để tạo "
        "ra bất kỳ sóng cơ học nào, kể cả siêu âm, cần có chuyển động của một bề mặt. Chuyển động này "
        "tạo ra sự nén và giãn của môi trường, có thể là chất khí (không khí), chất lỏng hoặc chất "
        "rắn. Loại thiết bị kích thích phổ biến nhất có thể tạo chuyển động bề mặt trong dải siêu âm "
        "là biến tử áp điện làm việc ở cái gọi là chế độ động cơ [3]. Tên gọi này hàm ý thiết bị áp "
        "điện chuyển trực tiếp năng lượng điện thành năng lượng cơ."))

    b.append(h3("Đầu dò chuyển động vi ba", "Microwave Motion Detectors"))
    b.append(p(
        "Đầu dò vi ba là một lựa chọn hấp dẫn so với các đầu dò khác khi cần phủ diện tích lớn và làm "
        "việc trong dải nhiệt độ rộng dưới tác động của nhiễu mạnh (ví dụ gió, tiếng ồn âm học, sương "
        "mù, bụi, ẩm…). Nguyên lý hoạt động của đầu dò vi ba dựa trên việc bức xạ sóng điện từ tần số "
        "vô tuyến (RF) về phía vùng được bảo vệ. Các tần số phổ biến nhất là 10,525 GHz (băng X) và "
        "24,125 GHz (băng K). Những bước sóng này đủ dài (λ = 3 cm ở băng X) để đi qua tự do phần lớn "
        "các chất gây nhiễu như bụi trong không khí, và đủ ngắn để bị các vật lớn hơn phản xạ."))
    b.append(p(
        "Phần vi ba của đầu dò gồm một bộ dao động Gunn, một ăng ten và một đi-ốt trộn. Bộ dao động "
        "Gunn là một đi-ốt gắn trong một hốc cộng hưởng nhỏ, chính xác; khi cấp nguồn, nó dao động ở "
        "tần số vi ba. Bộ dao động sinh ra sóng điện từ, một phần được hướng qua một cửa sập vào ống "
        "dẫn sóng và ăng ten hội tụ, rồi ăng ten hướng bức xạ về phía vật. Đặc tính hội tụ của ăng "
        "ten do ứng dụng quyết định. Theo lệ thường, giản đồ định hướng của ăng ten càng hẹp thì ăng "
        "ten càng nhạy (hệ số khuếch đại cao hơn). Một lệ thường khác là ăng ten chùm hẹp lớn hơn "
        "nhiều, còn ăng ten góc rộng có thể khá nhỏ. Công suất bức xạ điển hình của máy phát là "
        "10 mW đến 20 mW."))
    b.append(p(
        "Ăng ten phát tần số <i>f</i><sub>0</sub>, được xác định bởi bước sóng λ<sub>0</sub>:"))

    b.append(eq("<i>f</i><sub>0</sub> = <i>c</i><sub>0</sub>/λ<sub>0</sub>", "10.106"))
    b.append(p(
        "trong đó <i>c</i><sub>0</sub> là tốc độ ánh sáng. Khi mục tiêu chuyển động lại gần hoặc ra "
        "xa ăng ten phát, tần số của bức xạ phản xạ sẽ thay đổi. Như vậy, nếu mục tiêu đi ra xa với "
        "vận tốc <i>v</i>, tần số phản xạ sẽ giảm, và sẽ tăng với mục tiêu đang tới gần. Đây là hiệu "
        "ứng Doppler, đặt theo tên nhà khoa học Áo Christian Johann Doppler (1803–1853). Hiệu ứng này "
        "được phát hiện đầu tiên với âm thanh, nhưng cũng áp dụng cho bức xạ điện từ. Tuy nhiên, khác "
        "với sóng âm — vốn có thể lan truyền với tốc độ phụ thuộc chuyển động của nguồn âm — sóng "
        "điện từ lan truyền với tốc độ ánh sáng, một hằng số tuyệt đối. Tần số của sóng điện từ phản "
        "xạ có thể dự đoán được bằng thuyết tương đối:"))
    b.append(eq("<i>f</i><sub>r</sub> = <i>f</i><sub>0</sub> · √( (1 − <i>v</i>/<i>c</i><sub>0</sub>)"
                " / (1 + <i>v</i>/<i>c</i><sub>0</sub>) )", "10.107"))
    b.append(p(
        "Tuy nhiên, trong thực tế, đại lượng (<i>v</i>/<i>c</i><sub>0</sub>)<sup>2</sup> rất nhỏ so "
        "với đơn vị, nên có thể bỏ qua. Khi đó, phương trình cho tần số sóng phản xạ trở nên đồng "
        "nhất với phương trình của sóng âm:"))
    b.append(eq("<i>f</i><sub>r</sub> ≈ <i>f</i><sub>0</sub> (1 − <i>v</i>/<i>c</i><sub>0</sub>)",
                "10.108"))
    b.append(p(
        "Do hiệu ứng Doppler, sóng phản xạ có tần số <i>f</i><sub>r</sub> khác đi. Một đi-ốt trộn kết "
        "hợp tần số bức xạ (tham chiếu) với tần số phản xạ và, vì là linh kiện phi tuyến, sinh ra một "
        "tín hiệu chứa nhiều hoạ ba của cả hai tần số."))
    b.append(p("Tần số Doppler trong bộ trộn tính được từ:"))
    b.append(eq("Δ<i>f</i> = <i>f</i><sub>r</sub> − <i>f</i><sub>0</sub> = "
                "<i>f</i><sub>0</sub> · (<i>v</i>/<i>c</i><sub>0</sub>) / "
                "(1 + <i>v</i>/<i>c</i><sub>0</sub>)", "10.109"))
    b.append(p("và vì <i>c</i><sub>0</sub>/<i>v</i> ≫ 1, sau khi thay phương trình 10.106 thì:"))
    b.append(eq("Δ<i>f</i> ≈ <i>v</i>/λ<sub>0</sub>", "10.110"))
    b.append(p(
        "Như vậy, tần số tín hiệu ở đầu ra bộ trộn tỉ lệ tuyến tính với vận tốc của mục tiêu chuyển "
        "động. Ví dụ, nếu một người đi bộ về phía đầu dò với vận tốc 0,6 m/s, tần số Doppler cho đầu "
        "dò băng X là Δ<i>f</i> = 0,6/0,03 = 20 Hz."))
    b.append(p(
        "Phương trình 10.110 chỉ đúng cho chuyển động theo phương pháp tuyến. Khi mục tiêu chuyển "
        "động theo góc Θ so với đầu dò, tần số Doppler là:"))
    b.append(eq("Δ<i>f</i> ≈ (<i>v</i>/λ<sub>0</sub>) cos Θ", "10.111"))

    b.append(h3("Radar xung công suất cực nhỏ (MIR)", "Micropower Impulse Radar"))
    b.append(p(
        "Năm 1993, Phòng thí nghiệm Quốc gia Lawrence Livermore phát triển radar xung công suất cực "
        "nhỏ (MIR), một cảm biến đo cự ly không tiếp xúc, giá rẻ [3]. Nguyên lý hoạt động của MIR về "
        "cơ bản giống một hệ radar xung thông thường, nhưng có vài khác biệt đáng kể. MIR gồm một bộ "
        "sinh nhiễu mà đầu ra của nó kích hoạt một bộ sinh xung. Mỗi xung có độ dài ngắn cố định, "
        "trong khi việc lặp các xung là ngẫu nhiên, theo sự kích hoạt của bộ sinh nhiễu. Các xung "
        "được giãn cách ngẫu nhiên với nhau theo một dạng giống nhiễu Gauss. Có thể nói các xung được "
        "điều chế tần số xung (PFM) bằng nhiễu trắng với chỉ số cực đại 20%. Đến lượt mình, các xung "
        "vuông góc gây điều biên (AM) cho một máy phát vô tuyến. Máy phát vô tuyến tạo ra những cụm "
        "ngắn tín hiệu vô tuyến cao tần lan từ ăng ten phát ra không gian xung quanh. Sóng điện từ "
        "phản xạ từ các vật và lan trở về radar. Chính bộ sinh xung đã điều chế máy phát cũng đóng "
        "mở (với một độ trễ định trước) máy thu vô tuyến, để chỉ cho đầu ra của MIR hoạt động trong "
        "một cửa sổ thời gian xác định. Một lý do nữa để đóng mở máy thu là giảm mức tiêu thụ công "
        "suất của nó. Các xung phản xạ được thu, được giải điều chế (khôi phục dạng xung vuông từ "
        "tín hiệu vô tuyến), và độ trễ thời gian so với xung phát được đo. Vì các xung được giãn "
        "cách ngẫu nhiên, thực tế có thể cho bất kỳ số lượng hệ MIR giống nhau nào hoạt động trong "
        "cùng một không gian mà không cần phân chia tần số (tức là chúng làm việc ở cùng tần số sóng "
        "mang trong cùng một băng thông). Xác suất các cụm xung từ những máy phát gây nhiễu chồng "
        "lên nhau là nhỏ, và nếu có chồng thì mức nhiễu cũng giảm đáng kể nhờ mạch lấy trung bình."))

    b.append(h3("Đầu dò hiện diện điện dung", "Capacitive Occupancy Detectors"))
    b.append(p(
        "Là một môi trường dẫn điện có hằng số điện môi cao, cơ thể người tạo ra một điện dung ghép "
        "với môi trường xung quanh. Điện dung này phụ thuộc mạnh vào các yếu tố như kích thước cơ "
        "thể, quần áo, vật liệu, loại vật xung quanh, thời tiết… Dải ghép dù rộng đến đâu, điện dung "
        "vẫn có thể thay đổi từ vài picôfara đến vài nanôfara. Khi một người chuyển động, điện dung "
        "ghép thay đổi, nhờ đó có thể phân biệt vật tĩnh với vật động. Trên thực tế, mọi vật đều tạo "
        "ra một mức ghép điện dung nào đó với nhau. Nếu một người (hay bất cứ thứ gì, theo nghĩa đó) "
        "đi vào vùng lân cận những vật mà điện dung ghép giữa chúng với nhau đã được xác lập trước, "
        "một giá trị điện dung mới xuất hiện giữa các vật đó do có vật xâm nhập [3]. Hình 10-37 cho "
        "thấy điện dung giữa một bản thử và đất bằng <i>C</i><sub>1</sub>. Khi một người đi vào vùng "
        "lân cận bản thử, người đó tạo thành hai tụ điện bổ sung: một giữa bản thử và cơ thể người, "
        "gọi là <i>C</i><sub>a</sub>, và một giữa cơ thể người với đất, gọi là <i>C</i><sub>b</sub>. "
        "Khi đó, điện dung tổng <i>C</i> giữa bản thử và đất trở nên lớn hơn một lượng Δ<i>C</i>."))

    b.append(eq("<i>C</i> = <i>C</i><sub>1</sub> + Δ<i>C</i> = <i>C</i><sub>1</sub> + "
                "<i>C</i><sub>a</sub><i>C</i><sub>b</sub>/(<i>C</i><sub>a</sub> + "
                "<i>C</i><sub>b</sub>)", "10.112"))

    b.append(fig(37, hb10fig.fig_10_37()))

    b.append(p(
        "Với thiết bị thích hợp, hiện tượng này có thể dùng để phát hiện hiện diện [3]. Điều cần làm "
        "là đo điện dung giữa một bản thử (đầu dò) và một bản chuẩn (đất). Hình 10-38 minh hoạ sơ đồ "
        "mạch phát hiện biến thiên của điện dung đầu dò <i>C</i><sub>p</sub> [4]. Điện dung này được "
        "nạp từ một nguồn điện áp chuẩn <i>V</i><sub>ref</sub> qua một cổng do transistor "
        "<i>Q</i><sub>1</sub> tạo ra khi điện áp ra của bộ dao động điều khiển xuống thấp. Khi điện "
        "áp này lên cao, transistor <i>Q</i><sub>1</sub> đóng trong khi <i>Q</i><sub>2</sub> mở. Điện "
        "dung đầu dò <i>C</i><sub>p</sub> phóng qua một bộ hút dòng không đổi cấu tạo bằng transistor "
        "<i>Q</i><sub>3</sub>. Tụ <i>C</i><sub>1</sub> lọc các gai điện áp trên transistor. Điện áp "
        "trung bình <i>e</i><sub>p</sub> biểu diễn giá trị của tụ <i>C</i><sub>p</sub>. Khi một kẻ "
        "xâm nhập tới gần đầu dò, điện dung của đầu dò tăng, làm điện áp trên <i>C</i><sub>1</sub> "
        "dâng lên. Biến thiên điện áp này đi qua tụ <i>C</i><sub>2</sub> tới đầu vào của một bộ so "
        "sánh có ngưỡng cố định <i>V</i><sub>T</sub>. Bộ so sánh cho ra tín hiệu "
        "<i>V</i><sub>out</sub> khi điện áp vào vượt giá trị ngưỡng."))

    b.append(fig(38, hb10fig.fig_10_38()))

    b.append(p(
        "Khi một cảm biến hiện diện (tiệm cận) kiểu điện dung được dùng gần hoặc trên một thiết bị "
        "kim loại, độ nhạy của nó có thể giảm nghiêm trọng do ghép điện dung giữa điện cực và các "
        "phần kim loại của thiết bị. Một cách hiệu quả để giảm điện dung ký sinh đó là dùng các màn "
        "chắn được dẫn động (driven shield) [3]."))

    b.append(h3("Đầu dò ma sát điện", "Triboelectric Detectors"))
    b.append(p(
        "Bất kỳ vật nào cũng có thể tích luỹ điện tĩnh trên bề mặt. Những điện tích xuất hiện tự "
        "nhiên này sinh ra từ hiệu ứng ma sát điện, tức quá trình tách điện tích do vật chuyển động, "
        "do ma sát của sợi vải, do nhiễu động không khí, do điện khí quyển… Thông thường, không khí "
        "chứa các ion dương hoặc âm có thể bị hút vào cơ thể người, làm thay đổi điện tích của cơ "
        "thể. Trong điều kiện tĩnh lý tưởng, một vật không tích điện — điện tích khối của nó bằng "
        "không. Trên thực tế, bất kỳ vật nào, ít nhất là tạm thời, cách ly với đất đều có thể biểu "
        "hiện một mức mất cân bằng điện tích khối nào đó. Nói cách khác, nó trở thành vật mang điện "
        "tích, và các điện tích ấy trở thành nguồn điện trường. Điện trường, hay đúng hơn là các biến "
        "thiên của nó, có thể được phát hiện bằng một mạch điện tử có một điện cực thu đặc biệt ở đầu "
        "vào [3, 5]. Điện cực này làm tăng ghép điện dung giữa đầu vào mạch với môi trường, rất giống "
        "các đầu dò điện dung mô tả ở trên. Điện cực có thể được chế tạo dưới dạng một bề mặt dẫn "
        "điện cách ly tốt với đất."))
    b.append(p(
        "Nếu một vật mang điện (người hoặc động vật) đổi vị trí — đi ra xa, hoặc một vật mang điện "
        "mới đi vào vùng lân cận điện cực — điện trường tĩnh bị nhiễu loạn. Cường độ điện trường phụ "
        "thuộc điều kiện khí quyển và bản chất các vật. Ví dụ, một người mặc quần áo nhân tạo khô đi "
        "trên thảm mang điện tích mạnh gấp hàng triệu lần một kẻ xâm nhập ướt vừa từ ngoài mưa "
        "vào."))
    b.append(p(
        "Cần lưu ý rằng khác với đầu dò chuyển động kiểu điện dung — vốn là cảm biến chủ động — đầu "
        "dò ma sát điện là thụ động, tức là nó không phát hay truyền tín hiệu nào. Có vài nguồn nhiễu "
        "khả dĩ có thể gây phát hiện nhầm ở đầu dò ma sát điện, nghĩa là đầu dò có thể bị nhiễu truyền "
        "dẫn tác động và cho báo động giả. Trong các nguồn nhiễu có tín hiệu đường dây điện 60 Hz "
        "hoặc 50 Hz, điện trường do đài phát thanh, thiết bị điện công suất lớn, sét… sinh ra. Phần "
        "lớn các nhiễu này tạo ra điện trường phân bố quanh đầu dò khá đều và có thể bù trừ được bằng "
        "cách dùng mạch đầu vào vi sai có tỉ số triệt tín hiệu đồng pha lớn."))

    b.append(h3("Đầu dò chuyển động quang điện tử", "Optoelectronic Motion Detectors"))
    b.append(p(
        "Đầu dò chuyển động quang điện tử dựa trên bức xạ điện từ trong dải quang, cụ thể là các bước "
        "sóng từ 0,4 µm đến 20 µm. Dải này bao trùm vùng khả kiến, vùng hồng ngoại gần và một phần "
        "vùng hồng ngoại xa. Các đầu dò này chủ yếu dùng để chỉ thị chuyển động của người và động "
        "vật. Chúng hoạt động ở cự ly tới vài trăm mét và, tuỳ nhu cầu cụ thể, có thể có trường nhìn "
        "hẹp hoặc rộng."))
    b.append(p(
        "Phần lớn các vật (trừ vật rất nóng) chỉ bức xạ sóng điện từ trong vùng hồng ngoại trung và "
        "hồng ngoại xa. Do đó, các đầu dò chuyển động dùng ánh sáng khả kiến và hồng ngoại gần buộc "
        "phải dựa vào một nguồn sáng bổ sung để chiếu sáng vật. Ánh sáng được cơ thể vật phản xạ về "
        "phía bộ hội tụ để phát hiện tiếp. Nguồn chiếu sáng như vậy có thể là ánh sáng Mặt Trời hoặc "
        "ánh sáng hồng ngoại gần vô hình từ một nguồn hồng ngoại gần bổ sung (một đèn chiếu)."))
    b.append(p(
        "Các lĩnh vực ứng dụng chính của đầu dò chuyển động quang điện tử là trong các hệ an ninh "
        "(phát hiện kẻ xâm nhập), trong quản lý năng lượng (bật tắt đèn) và trong cái gọi là nhà "
        "“thông minh”, nơi chúng có thể điều khiển nhiều thiết bị như máy điều hoà, quạt làm mát, dàn "
        "âm thanh… Chúng cũng được dùng trong rô-bốt, đồ chơi và các sản phẩm mới lạ. Ưu điểm quan "
        "trọng nhất của một đầu dò chuyển động quang điện tử là đơn giản và rẻ."))

    b.append(h4("Cấu trúc cảm biến", "Sensor Structures"))
    b.append(p(
        "Cấu trúc chung của một đầu dò chuyển động quang điện tử được vẽ trên Hình 10-39(A). Bất kể "
        "dùng phần tử cảm quang nào, các bộ phận sau là thiết yếu: một bộ hội tụ (thấu kính hoặc "
        "gương hội tụ), một phần tử phát hiện ánh sáng và một bộ so sánh ngưỡng. Một đầu dò chuyển "
        "động quang điện tử giống một máy ảnh. Các bộ phận hội tụ của nó tạo ảnh của trường nhìn trên "
        "một mặt phẳng tiêu. Không có màn trập cơ khí như ở máy ảnh, nhưng thay cho phim là một phần "
        "tử nhạy sáng. Phần tử này chuyển ánh sáng đã hội tụ thành tín hiệu điện. Thấu kính hội tụ "
        "tạo ảnh của cảnh vật xung quanh trên mặt phẳng tiêu, nơi đặt phần tử nhạy sáng. Nếu khu vực "
        "không có người, ảnh là tĩnh và tín hiệu ra của phần tử ổn định. Khi một “kẻ xâm nhập” vào "
        "phòng và tiếp tục di chuyển, ảnh của người đó trên mặt phẳng tiêu cũng di chuyển. Tại một "
        "thời điểm nào đó, cơ thể kẻ xâm nhập dịch đi một góc α và ảnh chồng lên phần tử. Đây là điểm "
        "quan trọng cần hiểu: việc phát hiện chỉ xảy ra đúng lúc ảnh của vật hoặc trùng với bề mặt "
        "đầu dò, hoặc rời khỏi nó. Nghĩa là không chồng lên nhau thì không phát hiện. Giả sử cơ thể "
        "kẻ xâm nhập tạo ra một ảnh có quang thông khác với cảnh nền tĩnh, phần tử nhạy sáng đáp lại "
        "bằng một điện áp lệch <i>V</i>. Nói cách khác, để gây được phát hiện, một ảnh chuyển động "
        "phải có một mức tương phản quang học nào đó so với cảnh xung quanh."))
    b.append(p(
        "Hình 10-39(B) cho thấy tín hiệu ra được so với hai ngưỡng trong một bộ so sánh cửa sổ. Mục "
        "đích của bộ so sánh là chuyển tín hiệu tương tự <i>V</i> thành hai mức lôgic: 0 — không phát "
        "hiện chuyển động, và 1 — phát hiện có chuyển động."))

    b.append(fig(39, hb10fig.fig_10_39()))

    b.append(p(
        "Để tăng diện tích phủ, có thể đặt một dãy đầu dò trên mặt phẳng tiêu của một gương hội tụ "
        "hoặc thấu kính. Mỗi đầu dò riêng lẻ phủ một trường nhìn hẹp, còn khi kết hợp chúng bảo vệ "
        "được vùng lớn hơn. Mọi đầu dò trong dãy phải hoặc được ghép kênh, hoặc được nối với nhau "
        "theo cách khác để tạo ra một tín hiệu phát hiện tổng hợp; nghĩa là chúng có thể được làm "
        "thành một dạng cảm biến phức hợp. Một giải pháp thay thế là dùng một hệ hội tụ nhiều phần "
        "tử."))

    b.append(h4("Dạng cảm biến phức hợp", "Complex Sensor Shape"))
    b.append(p(
        "Nếu diện tích bề mặt của đầu dò đủ lớn để phủ trọn một góc nhìn, có thể chia nó bằng quang "
        "học thành những phần tử nhỏ hơn, tạo ra một tương đương của dãy nhiều đầu dò. Để chia diện "
        "tích bề mặt thành nhiều phần, có thể tạo hình phần tử cảm quang theo một dạng kỳ dị, như "
        "dạng răng lược trên Hình 10-40(A) hoặc dạng lưới song song trên Hình 10-40(B). Mỗi phần của "
        "phần tử cảm quang hoạt động như một đầu dò ánh sáng riêng."))
    b.append(p(
        "Các đầu dò mắc song song hoặc nối tiếp sinh ra một tín hiệu ra tổng hợp, ví dụ điện áp "
        "<i>v</i>, khi ảnh của vật di chuyển dọc theo bề mặt phần tử, lần lượt cắt qua các vùng nhạy "
        "và không nhạy. Kết quả là một tín hiệu <i>v</i> xen kẽ ở các đầu cực của đầu dò. Mỗi vùng "
        "nhạy và không nhạy phải đủ lớn để chồng lấp với phần lớn ảnh của vật. Một giải pháp thay thế "
        "cho dạng cảm biến phức hợp là dùng một mặt nạ làm méo ảnh như trên Hình 10-40(C); tuy vậy, "
        "giải pháp này đòi hỏi diện tích bề mặt cảm biến lớn hơn."))

    b.append(fig(40, hb10fig.fig_10_40()))

    b.append(h4("Phần tử hội tụ dạng mắt ghép", "Facet Focusing Element"))
    b.append(p(
        "Một cách hiệu quả về chi phí để mở rộng trường nhìn trong khi vẫn dùng đầu dò diện tích nhỏ "
        "là dùng nhiều bộ hội tụ. Một gương hội tụ hay một thấu kính có thể được chia thành một dãy "
        "gương hoặc thấu kính nhỏ hơn gọi là các mắt ghép, giống như mắt của con ruồi. Mỗi mắt ghép "
        "tạo ra ảnh riêng của nó, dẫn tới nhiều ảnh, như trên Hình 10-41. Khi vật chuyển động, các "
        "ảnh cũng di chuyển ngang qua phần tử, tạo ra tín hiệu xen kẽ. Bằng cách kết hợp nhiều mắt "
        "ghép, có thể tạo ra bất kỳ hình mẫu phát hiện mong muốn nào trong trường nhìn, cả trên mặt "
        "phẳng ngang lẫn mặt phẳng đứng. Vị trí của thấu kính ghép, các tiêu cự, số lượng và bước của "
        "các mắt ghép (khoảng cách giữa trục quang của hai mắt ghép kề nhau) có thể tính được trong "
        "từng trường hợp bằng cách áp dụng các quy tắc quang hình học [3]. Trong dải hồng ngoại xa "
        "(cảm biến bức xạ nhiệt), người ta gần như chỉ dùng thấu kính Fresnel ghép bằng polyêtylen, "
        "nhờ giá thành thấp và hiệu suất tương đối cao."))
    b.append(p(
        "Với phần khả kiến của phổ quang, có thể chế tạo một đầu dò chuyển động đơn giản, rất rẻ mà "
        "vẫn hiệu quả cho các ứng dụng không đòi hỏi cao như điều khiển đèn hay đồ chơi tương tác, "
        "bằng quang trở đơn giản và thấu kính lỗ kim [3, 6, 7]."))

    b.append(fig(41, hb10fig.fig_10_41()))

    b.append(h3("Đầu dò chuyển động hồng ngoại xa", "Far-Infrared Motion Detectors"))
    b.append(p(
        "Một đầu dò chuyển động cảm nhận bức xạ điện từ do bất kỳ vật nào tự phát ra sẽ làm việc "
        "trong dải quang của bức xạ nhiệt, còn gọi là hồng ngoại xa (FIR). Những đầu dò như vậy đáp "
        "lại trao đổi nhiệt bức xạ giữa phần tử cảm nhận và vật chuyển động. Nguyên lý phát hiện "
        "chuyển động bằng nhiệt dựa trên lý thuyết vật lý về phát xạ sóng điện từ của mọi vật có "
        "nhiệt độ trên không độ tuyệt đối (xem Chương 32, Mục 6, về nhiệt kế hồng ngoại)."))
    b.append(p(
        "Đối với phát hiện chuyển động bằng hồng ngoại, điều thiết yếu là nhiệt độ bề mặt của một vật "
        "phải khác nhiệt độ của các vật xung quanh, để tồn tại một tương phản nhiệt. Mọi vật phát bức "
        "xạ nhiệt từ bề mặt, và cường độ bức xạ ấy tuân theo định luật Stefan–Boltzmann. Nếu vật nóng "
        "hơn môi trường, bức xạ nhiệt của nó dịch về phía bước sóng ngắn hơn và cường độ mạnh hơn. "
        "Nhiều vật cần phát hiện chuyển động là phi kim, nên chúng bức xạ năng lượng nhiệt khá đều "
        "trong một bán cầu. Hơn nữa, các vật điện môi nói chung có độ phát xạ cao. Da người là một "
        "trong những bề mặt phát xạ tốt nhất, với độ phát xạ trên 90%, còn phần lớn vải cũng có độ "
        "phát xạ cao, từ 0,74 đến 0,95 [3]. Dưới đây mô tả hai loại đầu dò chuyển động hồng ngoại xa: "
        "loại thứ nhất dùng cảm biến hồng ngoại thụ động (PIR), loại thứ hai dùng phần tử hồng ngoại "
        "xa chủ động (AFIR)."))

    b.append(h4("Đầu dò chuyển động PIR", "PIR Motion Detectors"))
    b.append(p(
        "Những đầu dò này trở nên rất phổ biến cho các hệ an ninh và quản lý năng lượng. Phần tử cảm "
        "nhận PIR phải nhạy với bức xạ hồng ngoại xa trong dải phổ từ 4 µm đến 20 µm, nơi tập trung "
        "phần lớn công suất nhiệt do người phát ra. Có ba loại phần tử cảm nhận có thể dùng cho đầu "
        "dò này: nhiệt trở, cột nhiệt và hoả điện; tuy vậy, phần tử hoả điện gần như được dùng độc "
        "quyền cho phát hiện chuyển động nhờ đơn giản, rẻ, độ nhạy cao và dải động rộng. Hiệu ứng "
        "hoả điện được mô tả ở Chương 32, Mục 7, về nhiệt kế hoả điện. Ở đây bàn cách dùng hiệu ứng "
        "ấy trong thiết kế cảm biến thực tế."))
    b.append(p(
        "Một vật liệu hoả điện sinh ra điện tích khi có dòng năng lượng nhiệt chạy qua nó. Một cách "
        "đơn giản hoá, có thể mô tả đó như một hiệu ứng bậc hai của giãn nở nhiệt (Hình 10-42). Vì "
        "mọi vật liệu hoả điện cũng là áp điện, nhiệt hấp thụ làm mặt trước của phần tử cảm nhận giãn "
        "ra. Ứng suất do nhiệt sinh ra sau đó tạo một điện tích áp điện trên các điện cực của phần "
        "tử. Điện tích này biểu hiện thành điện áp giữa các điện cực lắng trên hai mặt đối diện của "
        "vật liệu. Đáng tiếc là tính chất áp điện của phần tử cũng có tác dụng tiêu cực. Nếu cảm "
        "biến chịu một ứng suất cơ học rất nhỏ do bất kỳ ngoại lực nào, nó cũng sinh ra điện tích, và "
        "trong phần lớn trường hợp không thể phân biệt được với điện tích do sóng nhiệt hồng ngoại "
        "gây ra. Các nguồn nhiễu cơ học như vậy là gió, rung của toà nhà, âm thanh lớn…"))

    b.append(fig(42, hb10fig.fig_10_42()))

    b.append(p(
        "Để tách điện tích do nhiệt khỏi điện tích do áp điện, cảm biến hoả điện thường được chế tạo "
        "theo dạng đối xứng (Hình 10-43(A)). Hai phần tử giống nhau được đặt bên trong vỏ cảm biến. "
        "Các phần tử được nối với mạch điện tử sao cho sinh ra tín hiệu ngược pha khi chịu những đầu "
        "vào cùng pha. Ý tưởng là: các nhiễu sinh ra, ví dụ, bởi hiệu ứng áp điện hay các tín hiệu "
        "nhiệt ký sinh, tác động đồng thời (cùng pha) lên cả hai điện cực và do đó bị triệt tiêu ở "
        "đầu vào mạch, trong khi bức xạ nhiệt biến thiên cần phát hiện chỉ bị một phần tử hấp thụ tại "
        "một thời điểm, nên không bị triệt tiêu."))
    b.append(p(
        "Một cách chế tạo cảm biến vi sai là lắng hai cặp điện cực lên cả hai mặt của một phần tử hoả "
        "điện. Mỗi cặp tạo thành một tụ điện có thể được nạp hoặc bởi nhiệt, hoặc bởi ứng suất cơ "
        "học. Các điện cực ở mặt trên của cảm biến được nối với nhau thành một điện cực liên tục, "
        "trong khi hai điện cực đáy được tách rời, tạo ra các tụ điện mắc ngược chiều nối tiếp. Tuỳ "
        "phía đặt điện cực, tín hiệu ra sẽ có cực tính dương hoặc âm khi có dòng nhiệt vào. Trong một "
        "số ứng dụng, cần hình mẫu điện cực cảm nhận phức tạp hơn (ví dụ để tạo các vùng phát hiện "
        "định trước), nên cần nhiều hơn một cặp điện cực. Khi đó, để triệt tín hiệu cùng pha tốt hơn "
        "(triệt chế độ chung), cảm biến vẫn phải có số cặp điện cực chẵn, với vị trí các cặp xen kẽ "
        "nhau để đối xứng hình học tốt hơn. Đôi khi cách nối xen kẽ như vậy được gọi là điện cực răng "
        "lược."))
    b.append(p(
        "Một phần tử cảm nhận vi sai phải được gắn sao cho cả hai phần của cảm biến sinh ra cùng một "
        "tín hiệu khi chịu cùng những yếu tố bên ngoài. Tại mọi thời điểm, bộ phận quang học phải hội "
        "tụ ảnh nhiệt của một vật lên bề mặt chỉ một phần của cảm biến, phần được một cặp điện cực "
        "duy nhất chiếm giữ. Phần tử chỉ sinh điện tích trên cặp điện cực đang chịu dòng nhiệt. Khi "
        "ảnh nhiệt dịch từ điện cực này sang điện cực kia, dòng <i>i</i> chạy từ phần tử cảm nhận vào "
        "điện trở phân cực <i>R</i> (Hình 10-43(B)) thay đổi từ không, sang dương, rồi về không, sang "
        "âm, rồi lại về không (phần dưới của Hình 10-43(A)). Một transistor JFET <i>Q</i> được dùng "
        "làm bộ biến đổi trở kháng. Giá trị của điện trở <i>R</i> phải rất lớn. Ví dụ, dòng xoay "
        "chiều điển hình do phần tử sinh ra khi đáp lại một người đang đi là cỡ 1 pA "
        "(10<sup>–12</sup> A). Nếu muốn có điện áp ra <i>v</i> = 50 mV ở một cự ly cụ thể, thì theo "
        "định luật Ohm, giá trị điện trở là <i>R</i> = <i>v</i>/<i>i</i> = 50 GΩ "
        "(5 × 10<sup>10</sup> Ω). Một điện trở như vậy không thể nối trực tiếp vào một mạch điện tử "
        "thông thường; do đó transistor <i>Q</i> đóng vai trò bộ theo điện áp (hệ số khuếch đại xấp "
        "xỉ bằng một). Trở kháng ra điển hình của nó cỡ vài kilôôm."))

    b.append(fig(43, hb10fig.fig_10_43()))

    b.append(p(
        "Dòng ra <i>i</i> của cảm biến PIR có thể tính được trên cơ sở định luật Stefan–Boltzmann "
        "như sau [3]:"))
    b.append(eq("<i>i</i> ≈ (<i>P</i>·<i>a</i>)/(<i>h</i>·<i>c</i>) · "
                "(π σ γ Δ<i>T</i> · <i>T</i><sub>a</sub><sup>3</sup>) / <i>L</i><sup>2</sup>", "10.113"))
    b.append(p(
        "trong đó Δ<i>T</i> = (<i>T</i><sub>b</sub> – <i>T</i><sub>a</sub>) là gradient nhiệt độ giữa "
        "vật và môi trường xung quanh; <i>P</i> là hệ số hoả điện; σ là hằng số Stefan–Boltzmann; "
        "<i>a</i> là diện tích thấu kính; γ là hệ số truyền qua của thấu kính; <i>h</i> là độ dày và "
        "<i>c</i> là nhiệt dung riêng của phần tử hoả điện; <i>L</i> là khoảng cách tới vật."))
    b.append(note(
        "Bản gốc của các phương trình 10.113 và 10.114 bị lỗi quét nặng: các ký hiệu bị đảo thứ tự "
        "và mất dấu. Hai công thức trên đây được phục dựng lại theo đúng phần diễn giải ngay sau đó "
        "trong nguyên bản, chứ không phải chép nguyên văn từ bản quét."))
    b.append(p(
        "Có thể rút ra vài kết luận từ phương trình 10.113. Phần đầu của phương trình (tỉ số thứ "
        "nhất) đặc trưng cho đầu dò, phần còn lại liên quan tới vật. Dòng hoả điện <i>i</i> tỉ lệ "
        "trực tiếp với hiệu nhiệt độ (tương phản nhiệt) giữa vật và môi trường xung quanh. Nó cũng "
        "tỉ lệ với diện tích bề mặt của vật hướng về đầu dò. Đóng góp của nhiệt độ môi trường "
        "<i>T</i><sub>a</sub> không mạnh như có thể tưởng từ luỹ thừa bậc ba của nó: nhiệt độ môi "
        "trường phải nhập bằng kenvin, nên các biến thiên của nó trở nên tương đối nhỏ so với thang "
        "đo. Phần tử cảm nhận càng mỏng thì đầu dò càng nhạy. Diện tích thấu kính cũng ảnh hưởng trực "
        "tiếp tới độ lớn tín hiệu. Ngược lại, dòng hoả điện không phụ thuộc diện tích của cảm biến, "
        "miễn là thấu kính hội tụ được toàn bộ ảnh lên phần tử cảm nhận."))

    b.append(h4("Đầu dò chuyển động AFIR", "AFIR Motion Detectors"))
    b.append(p(
        "Đầu dò chuyển động AFIR là một lớp cảm biến nhiệt mới, có nguyên lý hoạt động dựa trên việc "
        "cân bằng công suất nhiệt cấp cho phần tử cảm nhận [8, 9]. Khác với một đầu dò chuyển động "
        "thụ động — vốn hấp thụ bức xạ nhiệt từ một vật nóng hơn — đầu dò chuyển động AFIR là chủ "
        "động, tức là nó bức xạ sóng nhiệt ra môi trường xung quanh. Nhiệt độ bề mặt của cảm biến "
        "(<i>T</i><sub>s</sub>) được giữ cao hơn môi trường một chút. Phần tử được kết hợp với một hệ "
        "hội tụ rất giống đầu dò PIR; tuy vậy, chức năng của hệ đó ngược với các đầu dò thụ động: bộ "
        "phận hội tụ trong đầu dò AFIR chiếu ảnh nhiệt của phần tử cảm nhận ấm ra môi trường xung "
        "quanh. Cảm biến AFIR có ưu điểm đáng kể so với PIR: miễn nhiễm với nhiều loại nhiễu (như "
        "nhiễu tần số vô tuyến và hiệu ứng vi âm)."))
    b.append(p("Điện áp ra của đầu dò chuyển động AFIR có thể mô tả bằng phương trình sau [3]:"))
    b.append(eq("Δ<i>V</i> ≈ −(<i>R</i>/<i>V</i><sub>0</sub>) · "
                "(π σ γ <i>a</i> · Δ<i>T</i> · <i>T</i><sub>a</sub><sup>3</sup>) / "
                "<i>L</i><sup>2</sup>", "10.114"))
    b.append(p(
        "trong đó <i>R</i> là điện trở của bộ gia nhiệt cho cảm biến và <i>V</i><sub>0</sub> là điện "
        "áp gia nhiệt. Dấu trừ cho biết với những vật chuyển động ấm hơn, điện áp ra giảm. Có sự "
        "tương đồng rõ ràng giữa hai phương trình 10.113 và 10.114; tuy vậy, độ nhạy (tầm phát hiện) "
        "của cảm biến AFIR có thể điều khiển dễ dàng bằng cách thay đổi <i>R</i> hoặc "
        "<i>V</i><sub>0</sub>. Để có độ nhạy tốt hơn, mức tăng nhiệt so với môi trường có thể giữ ở "
        "mức khá thấp. Trên thực tế, phần tử chỉ được gia nhiệt cao hơn môi trường khoảng 0,2 °C."))

    b.append(reflist([
        "S. Blumenkrantz, <em>Personal and Organizational Security Handbook</em>, Government Data "
        "Publications, Washington, D.C., 1989.",
        "P. Ryser và G. Pfister, “Optical fire and security technology: sensor principles and "
        "detection intelligence,” <em>Transducers ’91, Int. Conf. Solid-State Sensors and "
        "Actuators</em>, 1991, tr. 579–583.",
        "J. Fraden, <em>Handbook of Modern Sensors</em>, 2nd ed., Woodburg, NY: AIP Press, 1997.",
        "N. M. Calvin, “Capacitance proximity sensor,” bằng sáng chế Hoa Kỳ số 4 345 167, 1982.",
        "J. Fraden, “Apparatus and method for detecting movement of an object,” bằng sáng chế Hoa Kỳ "
        "số 5 019 804, 1991.",
        "J. Fraden, “Motion discontinuance detection system and method,” bằng sáng chế Hoa Kỳ số "
        "4 450 351, 1984.",
        "J. Fraden, “Toy including motion-detecting means for activating same,” bằng sáng chế Hoa Kỳ "
        "số 4 479 329, 1984.",
        "J. Fraden, “Active infrared motion detector and method for detecting movement,” bằng sáng "
        "chế Hoa Kỳ số 4 896 039, 1990.",
        "J. Fraden, “Active far infrared detectors,” trong <em>Temperature. Its Measurement and "
        "Control in Science and Industry</em>, Vol. 6, Woodburg, NY: American Institute of Physics, "
        "1992, Phần 2, tr. 831–836.",
    ]))

    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Chapter 10 is five monographs stapled together by an editor who noticed they were all about "
        "the same thing. An altimeter, an attitude reference, an inertial navigator, a satellite fix "
        "and a burglar alarm have almost nothing in common as hardware. They have everything in common "
        "as mathematics: each one measures a quantity that is only indirectly related to what you want, "
        "each one inverts that relation, and each one spends most of its engineering budget on the "
        "error analysis of the inversion. That is the thread worth following, and it is the thread the "
        "chapter itself never quite names."))

    b.append(h2("One inversion, five costumes"))
    b.append(p(
        "Write the measurement as <i>m</i> = <i>f</i>(<b>x</b>) + <b>n</b>, where <b>x</b> is the state "
        "you want, <i>m</i> is what the instrument reports, and <b>n</b> is everything you cannot "
        "control. If <i>f</i> is linear and square, the inversion is a matrix inverse and the whole "
        "problem is conditioning. If <i>f</i> is nonlinear and over-determined — which is the normal "
        "case — the inversion is a Gauss–Newton iteration on the Jacobian, and the covariance of the "
        "answer is (JᵀWJ)⁻¹. Every one of the five sections lands on that same expression."))

    b.append(p(
        "Section 10.1 does it with ranges: three or more slant ranges to known ground stations, "
        "linearised about a first guess, iterated until the residual stops shrinking. Section 10.2 does "
        "it with gravity: a triad of servo accelerometers reads the direction of the local vertical, "
        "and the attitude angles are recovered from the components. Section 10.3 does it by "
        "integration instead of algebra — twice, because acceleration integrates to velocity and "
        "velocity integrates to position. Section 10.4 does it with pseudoranges and a fourth unknown "
        "that is not a coordinate at all. Section 10.5 does it with a threshold, which is the degenerate "
        "case: <i>f</i> is a step function and the inversion is a single comparison."))

    b.append(fig(17, hb10fig.fig_10_17(), "en"))
    b.append(fig(19, hb10fig.fig_10_19(), "en"))

    b.append(p(
        "The platform-versus-strapdown distinction in 10.3 is worth reading as a statement about where "
        "the inversion happens. A gimballed platform performs the coordinate transformation in metal: "
        "the gyros hold a frame, the accelerometers stay level, and the computer receives acceleration "
        "already resolved into navigation axes. A strapdown system performs the same transformation in "
        "software, at 100 Hz or more, and pays for it with dynamic range — the accelerometers now see "
        "the full gravity vector plus all the manoeuvre acceleration, and the gyros must resolve rates "
        "spanning five or six decades. What strapdown bought was not accuracy. It bought the removal of "
        "a precision mechanical assembly from the bill of materials, and that is why every modern "
        "system is strapdown."))

    b.append(h2("The error ladder: t, t², t³"))
    b.append(p(
        "The single most useful quantitative idea in the chapter is buried in 10.3 under a list of six "
        "error categories. Sort those categories by how they propagate and a clean ladder appears."))

    b.append(table(
        ["Error source", "Physical effect", "Position error grows as"],
        [["Accelerometer bias <i>b</i>", "velocity error <i>b·t</i>", "½ <i>b t</i>²"],
         ["Gyro drift ε (free integration)", "tilt ε·<i>t</i> → horizontal acceleration <i>g</i>ε<i>t</i>",
          "⅙ <i>g</i> ε <i>t</i>³"],
         ["Gyro drift ε (Schuler-tuned)", "bounded tilt ≈ ε/ω<sub>s</sub>", "≈ <i>R</i> ε/ω<sub>s</sub>, "
          "oscillating"],
         ["Scale-factor error <i>k</i>", "velocity error <i>k·v</i>", "<i>k</i> · distance travelled"],
         ["Initial heading error δψ", "cross-track velocity <i>v</i>·δψ", "<i>v</i> δψ · <i>t</i>"],
         ["Timing error in the integration", "velocity error ∝ <i>t</i>·δ<i>t</i>", "quadratic in "
          "<i>t</i>"]],
        "Table 10-5 · How inertial error sources propagate. The exponents, not the coefficients, are the "
        "engineering content."))

    b.append(p(
        "The cubic term is the one that kills free-integration systems, and it is worth putting a number "
        "on it. Take a gyro drifting at 0.01° h⁻¹ — a good but unremarkable ring-laser grade — which is "
        "4.85 × 10⁻⁸ rad s⁻¹. Left to integrate freely for one hour, the tilt reaches 1.7 × 10⁻⁴ rad, the "
        "implied horizontal acceleration error is 1.7 × 10⁻³ m s⁻², and the position error is "
        "⅙ · 9.81 · 4.85 × 10⁻⁸ · (3600)³ ≈ 3.7 km. Nothing has failed. The arithmetic has simply been "
        "cubed."))

    b.append(p(
        "Schuler's 1923 insight, which the chapter mentions in one sentence and then drops, is the fix. "
        "If the platform's level loop is tuned to a period of 2π√(<i>R</i>/<i>g</i>) = 84.4 minutes — the "
        "period of a pendulum whose length is the Earth's radius — then a constant gyro drift no longer "
        "integrates into a growing tilt. It produces a bounded tilt of ε/ω<sub>s</sub> and a position "
        "error that oscillates instead of diverging. The 84-minute Schuler oscillation is visible in "
        "every inertial navigation trace ever plotted, and it is the reason a 0.01° h⁻¹ gyro can support "
        "a transatlantic flight while the free-integration arithmetic above says it cannot."))

    b.append(fig(22, hb10fig.fig_10_22(), "en"))

    b.append(p(
        "The optical gyros that replaced the spinning mass trade the same currency in a different "
        "denomination. The Sagnac phase shift for a coil of <i>N</i> turns, area <i>A</i>, at rotation "
        "rate Ω is Δφ = 8π<i>N A</i>Ω/(λ<i>c</i>). Put numbers in: a 10 cm diameter coil with 1000 "
        "turns, at 1550 nm, sensing the Earth's rotation rate of 7.29 × 10⁻⁵ rad s⁻¹, gives "
        "Δφ ≈ 3 × 10⁻⁵ rad — about 31 microradians, which is small but entirely measurable with a "
        "photodiode and a good phase detector. Scale the coil up and the shift scales with area, not "
        "with mass; that is why a fibre gyro can be made accurate by winding more fibre, while a "
        "spinning-mass gyro can only be made accurate by machining better bearings."))

    b.append(h2("Geometry is destiny"))
    b.append(p(
        "Section 10.4 contains the other idea that generalises: the accuracy of a radiolocation fix is "
        "not a property of the transmitter, it is a property of where you are standing relative to the "
        "transmitters. The rms circle of Figure 10-29 looks like a statement about noise, but the "
        "interesting number is how that circle deforms as the geometry degenerates. Two ranges give two "
        "circles and their two intersections; as the two stations and the receiver approach collinearity, "
        "the intersections merge and the fix runs away along the line. Three ranges give three circles "
        "that should meet at a point and instead enclose a small triangle — the residual of the "
        "least-squares solution, and a direct measure of how much to trust the answer."))

    b.append(fig(29, hb10fig.fig_10_29(), "en"))
    b.append(fig(30, hb10fig.fig_10_30(), "en"))

    b.append(p(
        "The hyperbolic systems make the same point in a form that is easier to see. A time-difference "
        "measurement defines a hyperbola, not a circle, and the family of hyperbolas for one station "
        "pair fans out from the baseline. Near the baseline the hyperbolas are crowded and a small "
        "position change produces a large time-difference change — high sensitivity, good accuracy. Far "
        "out along the baseline extension the hyperbolas spread apart and the same timing error becomes "
        "a large position error. The chapter's rule of thumb that the user should stay within about six "
        "baseline lengths is exactly this geometric dilution, stated as a number instead of a gradient. "
        "The same quantity appears in GPS under the name DOP, and it is the reason a fix taken with four "
        "satellites clustered in one part of the sky is worse than a fix taken with four satellites "
        "spread across it, even though the signal-to-noise ratio is identical."))

    b.append(h2("One equation, two industries"))
    b.append(p(
        "The Doppler relation Δ<i>f</i> ≈ <i>v</i>/λ₀ appears twice in this chapter, in contexts that "
        "share nothing but the physics. In 10.4 it is the basis of the Transit satellite fix: the "
        "satellite moves at 7.5 km s⁻¹, the received frequency sweeps through a few tens of kilohertz as "
        "it passes, and the shape of that sweep against time locates the receiver on a cone about the "
        "satellite's track. In 10.5 the same equation is the basis of a microwave burglar alarm: a "
        "person walking at 0.6 m s⁻¹ toward an X-band detector at 3 cm wavelength produces a 20 Hz beat "
        "note, which is exactly the frequency a cheap audio amplifier likes to work at."))

    b.append(fig(34, hb10fig.fig_10_34(), "en"))

    b.append(p(
        "The difference between the two applications is entirely in what you do with the sign and the "
        "geometry. Transit needs the full time history, because the curve's shape — its inflection "
        "point, its asymptotes — carries the range and the closest-approach distance. The motion "
        "detector needs only the existence of a nonzero beat, because its question is binary. That is "
        "why the detector costs a few dollars and the satellite fix costs a few thousand: same "
        "equation, different amount of information extracted from it."))

    b.append(h2("GPS: the fourth unknown"))
    b.append(p(
        "The elegant move in the GPS design is not the satellites, the codes, or the frequencies. It is "
        "that the receiver's own clock error is promoted to an unknown. Four pseudoranges give four "
        "equations in four unknowns — <i>x</i>, <i>y</i>, <i>z</i> and the clock bias — and the "
        "solution is exact. A quartz oscillator good to a microsecond would otherwise contribute 300 m "
        "of range error; treating that error as a coordinate to be solved for converts a hardware "
        "problem into an arithmetic one. Add a fifth satellite and the system becomes over-determined, "
        "which is what allows receiver-autonomous integrity monitoring: the fifth residual does not "
        "have to be small, it only has to be consistent."))

    b.append(fig(35, hb10fig.fig_10_35(), "en"))
    b.append(fig(36, hb10fig.fig_10_36(), "en"))

    b.append(p(
        "Dual frequency is the same trick applied to the atmosphere. Ionospheric delay goes as "
        "1/<i>f</i>², so two carriers widely separated in frequency give two different delays for the "
        "same path, and the difference between them determines the delay without any model of the "
        "ionosphere at all. That is why L1 and L2 are where they are, and it is why the correction "
        "works even during a geomagnetic storm, when every model fails. The differential technique of "
        "Figure 10-36 extends the logic to everything the two receivers share: a reference station at a "
        "known point measures the total error — ionosphere, troposphere, ephemeris, clock — and "
        "broadcasts it as a scalar correction. What it cannot remove is the part of the error that is "
        "not shared, which is why DGPS accuracy degrades with distance from the reference station and "
        "why the sub-centimetre figures quoted in the chapter require carrier-phase processing rather "
        "than code ranging."))

    b.append(h2("What the chapter could not know"))
    b.append(p(
        "This is a 1999 text describing a 1997 state of the art, and three of its forward-looking "
        "statements did not survive contact with the next decade. It is worth being explicit about "
        "them, because a reader who takes the chapter at face value will build the wrong mental model "
        "of what is still running."))

    b.append(table(
        ["The chapter says", "What happened"],
        [["Omega is an operational worldwide system maintained by the U.S. Coast Guard and others",
          "Omega was switched off on 30 September 1997 — before the book was printed"],
         ["Transit is the established satellite navigation system; GPS evolved from it",
          "Transit was decommissioned on 31 December 1996, for the same reason"],
         ["Selective Availability limits civil accuracy to 50 m and is \"intended to be lifted by the "
          "year 2006\"",
          "SA was switched off on 2 May 2000; civil accuracy jumped to 10–15 m overnight"],
         ["Loran-C will be terminated in the very near future because of GPS",
          "It survived; the U.S. chains closed in 2010, and eLoran is being rebuilt as a GPS backup "
          "precisely because GPS turned out to be jammable"],
         ["GPS satellites orbit \"about 2200 km high\"",
          "20 200 km. At 2200 km a 12-hour orbit is not physically possible"],
         ["Glonass satellites orbit 1500 km above the ground",
          "19 100 km, for the same reason"],
         ["The \"best four satellites\" philosophy is giving way to all-in-view",
          "Correct, and it went much further: modern receivers track every satellite in every "
          "constellation simultaneously"]],
        "Table 10-6 · Seven statements in the chapter, checked against what followed. The physics in "
        "the chapter is sound; the inventory is not."))

    b.append(p(
        "The two orbital altitudes are worth flagging as a specific kind of error, because it is the "
        "kind that survives editing. Both are off by roughly a factor of ten, and both would be caught "
        "by Kepler's third law in one line: a 12-hour period requires a semi-major axis of 26 560 km, "
        "which is an altitude of 20 200 km, full stop. A 2200 km orbit has a period of about 2 hours. "
        "The chapter's own Figure 10-35 shows six orbital planes with four satellites each, which is "
        "the real constellation and is inconsistent with its own text. When a figure and a sentence "
        "disagree, believe the figure."))

    b.append(h2("Occupancy: detecting a change, or detecting a body"))
    b.append(p(
        "Section 10.5 opens with a distinction that most of the industry still gets wrong. An "
        "occupancy sensor reports a body; a motion sensor reports a change. Almost every cheap product "
        "on the market is the second and is sold as the first, which is why the lights go out while you "
        "are sitting still reading."))
    b.append(p(
        "The reason is structural, not a manufacturing defect. A passive infrared detector is a "
        "pyroelectric device, and a pyroelectric device responds to the rate of change of its own "
        "temperature, not to its temperature. A stationary warm body produces a steady heat flux, the "
        "element's temperature stabilises, the polarisation stops changing, and the output returns to "
        "zero. The detector is working perfectly. It is answering a different question from the one the "
        "occupant is asking. To detect a stationary person you need a measurement of an absolute "
        "quantity that a body perturbs — dielectric loading, acoustic path length, weight on the floor, "
        "the CO₂ concentration in the room — and that is exactly what the seventeen-item list at the "
        "head of 10.5 is: a list of physical quantities a human body disturbs."))

    b.append(fig(39, hb10fig.fig_10_39(), "en"))

    b.append(p(
        "The dual-element PIR of Figure 10-43 is the best piece of engineering in the chapter, and it "
        "is worth spelling out why. A pyroelectric element is also piezoelectric, because the same "
        "non-centrosymmetric crystal structure that allows a spontaneous polarisation also allows a "
        "stress-induced one. So the element cannot distinguish \"I was heated\" from \"I was pushed\". "
        "Wind, footfall, a door slam and a warm body all produce the same charge. The fix is symmetry: "
        "two identical elements wired in series opposition, and an optical system that focuses the "
        "thermal image onto one element at a time. A common-mode disturbance — the room warming up, the "
        "whole housing being flexed — reaches both elements equally and cancels at the amplifier input. "
        "A moving body reaches one element and then the other, producing a bipolar pulse that no "
        "common-mode signal can imitate. The sensor is not made more sensitive; it is made deaf to "
        "everything that is not a moving target. That is the same strategy as a differential "
        "accelerometer, a bridge strain gauge, and a common-mode-rejecting front end on any instrument "
        "in this handbook, and it is the single most transferable idea in section 10.5."))

    b.append(fig(38, hb10fig.fig_10_38(), "en"))
    b.append(fig(43, hb10fig.fig_10_43(), "en"))

    b.append(p(
        "The capacitive detector of Figure 10-38 shows the alternative and its cost. It measures an "
        "absolute quantity — the capacitance from a probe plate to earth, loaded by a nearby body — so "
        "it does detect a stationary person. But the quantity it measures is a few picofarads sitting "
        "on top of tens of picofarads of stray capacitance to everything else in the room, and the "
        "signal is a small fraction of that. Hence the driven shield the chapter mentions in one line: "
        "the only way to measure a small capacitance in a hostile environment is to make the "
        "environment not matter, by driving the guard electrode at the same potential as the probe so "
        "that no current flows through the stray path. It is the same principle as a guard ring on a "
        "PCB, and it is the difference between a sensor that works in a laboratory and one that works "
        "next to a filing cabinet."))

    b.append(h2("The through-line"))
    b.append(p(
        "Read end to end, the chapter is a catalogue of ways to answer \"where is it?\" and \"is "
        "anyone there?\" with indirect measurements. The instruments differ by six orders of magnitude "
        "in cost and by nine in range. The method does not: build a model of what the sensor should "
        "read, invert it, characterise the residual, and then arrange the geometry so that the residual "
        "is small where you need the answer. The radar altimeter, the ring-laser gyro, the GPS "
        "pseudorange and the burglar alarm are the same calculation wearing different clothes."))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 10 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 10 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 10 “Position, Location, Altitude Measurement” của tám tác giả — "
            "đo độ cao, đo tư thế, dẫn đường quán tính, dẫn đường vệ tinh và định vị vô tuyến, phát "
            "hiện hiện diện — với bốn mươi ba hình, bốn bảng và 114 phương trình." if vi else
            "Companion to Chapter 10 of the CRC Measurement Handbook — altitude, attitude, inertial "
            "navigation, satellite navigation and occupancy detection, read as five versions of one "
            "inverse problem, with a corrected inventory of what still exists.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 10'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 10' % BASE_EN)
    meta = ("Chương 10 · theo Ch10.pdf (CRC Press, 1999) · 73 trang gốc · 43 hình, 4 bảng, 8 tác giả" if vi
            else "Chapter 10 · 73 source pages · 43 figures, 4 tables, 8 co-authors")
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
