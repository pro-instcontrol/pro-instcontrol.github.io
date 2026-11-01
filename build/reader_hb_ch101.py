# -*- coding: utf-8 -*-
"""Handbook Chapter 101 — Measurement and Identification of Brush, Brushless,
and dc Stepping Motors (Stuart Schweid, Robert Lofthus — Xerox Corporation;
John McInroy — University of Wyoming).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch101.py
"""
import os

import hb101fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch101-measurement-and-identification-of-stepping-motors"
TITLE_EN = "Measurement and Identification of Brush, Brushless, and dc Stepping Motors"
TITLE_VI = "Đo và nhận diện động cơ bước chổi than, không chổi than và một chiều"
BYLINE = ("Stuart Schweid · Robert Lofthus (Xerox Corporation) · "
          "John McInroy (University of Wyoming)")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-101-%d">%s<figcaption class="figcap">%s</figcaption>'
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


# ================================================================ Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Có rất nhiều hệ thống, ví dụ robot, mà khả năng tự di chuyển hoặc di chuyển vật khác chính là "
        "mục đích tồn tại của chúng. Lại có vô số hệ thống khác, ví dụ máy in điện liệu, trong đó "
        "chuyển động không phải là kết quả mong muốn mà chỉ là điều kiện cần để hoàn thành mục tiêu "
        "chính. Tất cả những hệ thống này đều cần một hoặc nhiều “động cơ sơ cấp” (prime mover) — bộ "
        "phận trực tiếp hay gián tiếp tạo ra mọi chuyển động trong hệ."))

    # ------------------------------------------------------------ 101.1
    b.append(h2("101.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Các ứng dụng này có những yêu cầu rất khác nhau về loại chuyển động và độ chính xác của "
        "chuyển động. Có ứng dụng, như đồ chơi trẻ em, vẫn hoạt động tốt với yêu cầu chuyển động không "
        "chính xác. Ngược lại, có ứng dụng như in ấn đòi hỏi điều khiển chuyển động rất chính xác."))
    b.append(p(
        "Tuỳ theo loại chuyển động cần thiết, có thể chọn động cơ sơ cấp từ một vài ứng viên. Những "
        "loại động cơ phổ biến nhất là động cơ một chiều có chổi than, động cơ một chiều không chổi "
        "than và động cơ bước lai. Hệ thống bao gồm động cơ sơ cấp có thể được điều khiển đơn thuần "
        "theo thời gian (tức là vòng hở), hoặc theo cả thời gian lẫn trạng thái của hệ (tức là vòng "
        "kín)."))
    b.append(p(
        "Hệ vòng kín cần một cơ cấu nào đó để đo “trạng thái” của hệ. Với hệ chuyển động, đó thường là "
        "một hay nhiều cảm biến đo vị trí và/hoặc vận tốc. Ngoài ra, với nhiều kỹ thuật điều khiển — "
        "cụ thể là các bộ điều khiển tuyến tính — còn có lợi nếu có một mô hình của hệ được điều khiển. "
        "Mô hình có thể được dùng cùng vô số kỹ thuật thiết kế để cải thiện đáng kể đáp ứng động của "
        "hệ."))
    b.append(p(
        "Chương này mô tả các chế độ vận hành chính của những động cơ sơ cấp vừa nêu và trình bày chi "
        "tiết một phương pháp đo đáp ứng vòng hở của một hệ chuyển động ứng viên."))

    # ------------------------------------------------------------ 101.2
    b.append(h2("101.2 Động cơ bước lai", "Hybrid Stepping Motors"))
    b.append(p(
        "Động cơ bước lai là thiết bị hữu ích, cho khả năng định vị khá chính xác ngay trong vòng hở — "
        "chế độ vận hành phổ biến nhất của chúng. Chúng làm việc tốt ở chế độ vòng hở vì vẫn nằm trong "
        "một bước (một gia số vị trí được lệnh) chừng nào động cơ còn đủ mômen để chống lại mọi mômen "
        "ngoài do hệ tác dụng."))
    b.append(p(
        "Vì động cơ làm việc ở vòng hở, nó được chọn trước (a priori) để bảo đảm cung cấp đủ mômen cần "
        "thiết nhằm giữ trong bước. Mômen cực đại cần để vận hành hệ là hàm của quán tính hệ, biên dạng "
        "gia tốc của hệ, mômen ngoài tác dụng lên hệ, v.v. Sau khi xác định mômen cực đại cần thiết ở "
        "mọi tốc độ, có thể chọn động cơ từ đường đặc tính mômen – tốc độ của nó. Đường mômen – tốc độ "
        "mô tả mômen cực đại có thể chịu được ở mỗi tốc độ mà không bị trượt bước theo lệnh (gọi là "
        "“mất bước”). Động cơ có đường mômen – tốc độ nằm trên mức mômen yêu cầu của hệ ở mọi tốc độ sẽ "
        "đủ cho ứng dụng. Hình 101.1 cho thấy một đường mômen – tốc độ điển hình."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Động cơ bước lai có nhiều cuộn dây (gần như luôn là hai cuộn); khi được chuyển mạch theo một "
        "trình tự định trước, chúng làm động cơ quay. Khi động cơ làm việc ở chế độ gọi là “bước đủ” "
        "(full stepping), lệnh dòng cho mỗi cuộn có biên độ không đổi nhưng đổi cực (dương hoặc âm). "
        "Cần lưu ý rằng việc quy ước chiều dòng nào là “dương” hoàn toàn tuỳ ý. Ở chế độ này, động cơ "
        "chỉ có bốn lần cấp điện riêng biệt cho cuộn dây để hoàn thành một vòng quay, mặc dù những cách "
        "bố trí cơ khí khéo léo cho phép tăng mạnh số bước mỗi vòng: thường là 200, nhưng có thể tới "
        "800."))
    b.append(p(
        "Với hai cuộn dây riêng biệt (gọi là A và B), có bốn cách tổ hợp cấp điện cho cuộn: A+B+, "
        "A+B−, A−B−, A−B+. Nếu các tổ hợp dòng cuộn này được lệnh cho động cơ theo đúng trình tự vừa "
        "nêu, động cơ sẽ quay."))

    b.append(h3("Bộ khuếch đại chặt dòng", "Chopping Current Amplifiers"))
    b.append(p(
        "Như đã nói, chuyển động của động cơ bước đòi hỏi phải đặt vào cuộn dây một dòng có biên độ xác "
        "định. Vì lý do kinh tế, phần lớn hệ thống chỉ có nguồn áp (V<sub>ss</sub>) chứ không có nguồn "
        "dòng. “Bộ chặt dòng” (current chopper) là một bộ khuếch đại chuyển mạch vòng kín giá rẻ, có "
        "nhiệm vụ điều chỉnh dòng vào cuộn dây động cơ. Nó lợi dụng việc cuộn dây động cơ có điện cảm "
        "đáng kể. Hai cuộn dây của động cơ có phương trình động học [1]:"))
    b.append(eq("dI<sub>A</sub>/dt = (V<sub>A</sub> − I<sub>A</sub>R<sub>A</sub> − "
                "K<sub>b</sub>ω sin θ) / L<sub>A</sub>", "101.1"))
    b.append(eq("dI<sub>B</sub>/dt = (V<sub>B</sub> − I<sub>B</sub>R<sub>B</sub> − "
                "K<sub>b</sub>ω cos θ) / L<sub>B</sub>", "101.1"))
    b.append(p(
        "trong đó I là dòng trong cuộn dây (A), R là điện trở của cuộn (Ω), L là điện cảm của cuộn (H), "
        "V là điện áp đặt lên cuộn (V), K<sub>b</sub> là hằng số mômen của động cơ (Nm/A), ω là vận tốc "
        "động cơ (rad/s) và θ là vị trí động cơ (rad điện)."))
    b.append(p(
        "Cứ mỗi khoảng t<sub>s</sub> (với t<sub>s</sub> rất nhỏ, cỡ 10 µs), bộ chặt dòng đặt vào cuộn "
        "dây động cơ hoặc V<sub>ss</sub> hoặc −V<sub>ss</sub>, tuỳ theo dòng mong muốn (I<sub>M</sub>) "
        "lớn hơn hay nhỏ hơn dòng đo được (tức dòng thực) trong cuộn:"))
    b.append(eq("nếu I<sub>A</sub> &lt; I<sub>M</sub> thì V<sub>A</sub> = V<sub>ss</sub>, "
                "ngược lại V<sub>A</sub> = −V<sub>ss</sub>", "101.2"))
    b.append(eq("nếu I<sub>B</sub> &lt; I<sub>M</sub> thì V<sub>B</sub> = V<sub>ss</sub>, "
                "ngược lại V<sub>B</sub> = −V<sub>ss</sub>", "101.2"))
    b.append(p(
        "Yêu cầu thông thường là (V<sub>ss</sub>t<sub>s</sub>/L) phải nhỏ so với I<sub>M</sub>, nhờ đó "
        "dải dao động chặt dòng nhỏ so với dòng mong muốn. Hơn nữa, hệ cơ bao gồm động cơ thường có "
        "tính chất thông thấp, nên hầu như không đáp ứng với các thành phần biên độ nhỏ, tần số rất "
        "cao có trong dòng cuộn dây động cơ."))

    b.append(h3("Vi bước", "Microstepping"))
    b.append(p(
        "Một chế độ vòng hở phổ biến khác của động cơ bước là vi bước. Ở chế độ vi bước, vị trí tham "
        "chiếu được lệnh có thể nằm giữa các vị trí “bước đủ” của động cơ. Dòng được lệnh cho vị trí "
        "tham chiếu θ<sub>ref</sub> là:"))
    b.append(eq("I<sub>A</sub> = I<sub>M</sub> cos θ<sub>ref</sub>", "101.3"))
    b.append(eq("I<sub>B</sub> = I<sub>M</sub> sin θ<sub>ref</sub>", "101.3"))
    b.append(p(
        "trong đó θ<sub>ref</sub> là vị trí điện mong muốn của động cơ (cứ bốn bước đủ thì "
        "θ<sub>ref</sub> đi hết một vòng điện). Với ứng dụng vận tốc không đổi:"))
    b.append(eq("θ<sub>ref</sub> = N ω<sub>d</sub> t", "101.4"))
    b.append(p(
        "trong đó N là số vòng điện trên một vòng cơ của động cơ (bằng một phần tư số bước mỗi vòng) và "
        "ω<sub>d</sub> là vận tốc mong muốn (rad/s)."))

    b.append(h3("Điều khiển vòng kín", "Closed-Loop Control"))
    b.append(p(
        "Ngoài các cách dùng vòng hở, gần đây một số nhà nghiên cứu đã đưa ra phương pháp vận hành các "
        "động cơ này theo kiểu vòng kín. Khó khăn chính là động cơ bước lai là thiết bị phi tuyến, nên "
        "vô số kỹ thuật thiết kế của lý thuyết điều khiển tuyến tính không thể áp dụng trực tiếp. "
        "Hamman và Balas [1] dùng mô hình bậc bốn để tuyến tính hoá hệ quanh mỗi bước. Cách này hữu ích "
        "khi cần thay đổi đáp ứng không tắt dần của động cơ bước đối với một thay đổi vị trí được lệnh. "
        "Schweid [2] đề xuất một sơ đồ cho phép có đáp ứng quá độ tốt trong các ứng dụng vận tốc không "
        "đổi nhưng dùng trọn mô hình bậc bốn. Với hệ có bộ chặt dòng, mô hình bậc hai là đủ. Khi đó có "
        "thể áp dụng luật điều khiển sau [3–5]:"))
    b.append(eq("I<sub>A</sub> = I<sub>M</sub> cos θ<sub>ref</sub> − "
                "I<sub>C</sub> sin θ<sub>ref</sub>", "101.5"))
    b.append(eq("I<sub>B</sub> = I<sub>M</sub> sin θ<sub>ref</sub> + "
                "I<sub>C</sub> sin θ<sub>ref</sub>", "101.5"))
    b.append(p(
        "Các dòng trong phương trình 101.5 làm tuyến tính hoá mô hình động cơ bước, cho phép áp dụng "
        "những kỹ thuật điều khiển thông dụng như điều khiển PID [6]. Giá trị I<sub>M</sub> được dùng "
        "như thành phần vòng hở để vi bước động cơ, còn I<sub>C</sub> là số hạng phản hồi giúp cải "
        "thiện đáp ứng động."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản in của phương trình 101.5 cho số hạng thứ hai của dòng "
        "I<sub>B</sub> là <i>sin</i> θ<sub>ref</sub>, giống hệt số hạng thứ nhất. Muốn cặp dòng này trực "
        "giao — điều kiện để chúng tuyến tính hoá mô hình — số hạng thứ hai phải là "
        "<i>cos</i> θ<sub>ref</sub>. Bản dịch giữ nguyên như bản in và nêu ra ở đây thay vì tự sửa."))

    b.append(h3("Đo vị trí", "Position Measurement"))
    b.append(p(
        "Muốn thực hiện điều khiển vòng kín phải có cách đo vị trí của động cơ. Thêm một ràng buộc nữa: "
        "phép đo vị trí này phải thẳng hàng với kết cấu động cơ, không được lệch pha so với nó. Lý do "
        "là sơ đồ điều khiển ở phương trình 101.5 cần nhân dòng lệnh I<sub>C</sub> với sin và cos của "
        "vị trí động cơ. Một cách thực hiện là gắn lên động cơ một bộ mã hoá gia số có xung chỉ số. Sau "
        "đó, việc hiệu chuẩn sẽ xác định vị trí tương đối của xung chỉ số so với trục động cơ và dùng "
        "quan hệ này cho mọi phép đo vị trí về sau."))
    b.append(p(
        "Một sơ đồ khác dùng sức điện động cảm ứng của hai cuộn dây để ước lượng vị trí. Một số động cơ "
        "được chế tạo thêm các cuộn cảm biến phụ, giúp đo trực tiếp các đại lượng này. Từ phương trình "
        "101.2, có thể tìm sức điện động cảm ứng của cả hai cuộn:"))
    b.append(eq("V<sub>emfA</sub> = K<sub>b</sub>ω sin θ = V<sub>A</sub> − I<sub>A</sub>R<sub>A</sub> − "
                "L<sub>A</sub> dI<sub>A</sub>/dt", "101.6"))
    b.append(eq("V<sub>emfB</sub> = K<sub>b</sub>ω cos θ = V<sub>B</sub> − I<sub>B</sub>R<sub>B</sub> − "
                "L<sub>B</sub> dI<sub>B</sub>/dt", "101.6"))
    b.append(p("và vị trí có thể tìm được từ:"))
    b.append(eq("θ = −atan(V<sub>emfA</sub> / V<sub>emfB</sub>)", "101.7"))
    b.append(p(
        "Tuy nhiên, ở phần lớn động cơ, V<sub>emfA</sub> và V<sub>emfB</sub> không đo được trực tiếp. "
        "Dù vậy, vẫn có thể ước lượng rất tốt vị trí trong hệ vận tốc không đổi bằng cách xấp xỉ các "
        "tín hiệu sức điện động cảm ứng thông qua phép đo điện áp cuộn dây đã qua lọc thông thấp. Dưới "
        "đây trình bày một phương pháp được phát triển tại Xerox và đã có bằng sáng chế Hoa Kỳ "
        "(U.S. 5378975). Lấy biến đổi Laplace của phương trình 101.6 ta được:"))
    b.append(eq("V<sub>emfA</sub>(s) = V<sub>A</sub>(s) − (R<sub>A</sub> + sL<sub>A</sub>)"
                "I<sub>A</sub>(s)", "101.8"))
    b.append(eq("V<sub>emfB</sub>(s) = V<sub>B</sub>(s) − (R<sub>B</sub> + sL<sub>B</sub>)"
                "I<sub>B</sub>(s)", "101.8"))
    b.append(p(
        "Lọc cả hai vế bằng bộ lọc tương tự thông thấp có đặc tính khớp với động học của cuộn dây, ta "
        "được:"))
    b.append(eq("V<sub>filtA</sub>(s) = V<sub>A</sub>(s)/(1 + sL<sub>A</sub>/R<sub>A</sub>) − "
                "R<sub>A</sub>I<sub>A</sub>(s)", "101.9"))
    b.append(eq("V<sub>filtB</sub>(s) = V<sub>B</sub>(s)/(1 + sL<sub>B</sub>/R<sub>B</sub>) − "
                "R<sub>B</sub>I<sub>B</sub>(s)", "101.9"))
    b.append(p(
        "Các đại lượng V<sub>filtA</sub> và V<sub>filtB</sub> dễ có được bằng cách lọc thông thấp điện "
        "áp cuộn dây qua một mạch RC đơn giản rồi trừ đi số hạng IR. Việc trừ rất dễ thực hiện vì dòng "
        "là đại lượng đã biết (thực ra nó được lệnh), còn điện trở thì dễ đo."))
    b.append(p(
        "Giả sử hai cuộn giống nhau: L = L<sub>A</sub> = L<sub>B</sub>, R = R<sub>A</sub> = "
        "R<sub>B</sub>, và động cơ quay với vận tốc không đổi θ = Nω<sub>d</sub>t, khi đó các điện áp "
        "sức điện động cảm ứng là hình sin. Bản đã qua lọc thông thấp của chúng là:"))
    b.append(eq("V<sub>filtA</sub>(s) = |H(Nω<sub>d</sub>)| K<sub>b</sub> sin(Nω<sub>d</sub>t + φ)",
                "101.10"))
    b.append(eq("V<sub>filtB</sub>(s) = |H(Nω<sub>d</sub>)| K<sub>b</sub> cos(Nω<sub>d</sub>t + φ)",
                "101.10"))
    b.append(p(
        "trong đó |H(Nω<sub>d</sub>)| là đáp ứng biên độ của bộ lọc thông thấp tại tần số đầu vào "
        "Nω<sub>d</sub>, và φ = −atan(Nω<sub>d</sub>L/R) là dịch pha do việc lọc gây ra. Chia hai phương "
        "trình 101.10 cho nhau rồi lấy arctang ta được:"))
    b.append(eq("θ = atan(−V<sub>filtA</sub>(t) / V<sub>filtB</sub>(t)) + "
                "atan(Nω<sub>d</sub>L/R)", "101.11"))
    b.append(p(
        "Toàn bộ phần suy dẫn và phân tích có trong tài liệu tham khảo [7]. Ngoài ra, tài liệu [7] còn "
        "trình bày một kỹ thuật lọc Kalman để cải thiện ước lượng vận tốc từ ước lượng vị trí. Điều này "
        "là cần thiết vì đạo hàm (hay sai phân) của phép đo vị trí rất nhạy với nhiễu."))

    # ------------------------------------------------------------ 101.3
    b.append(h2("101.3 Động cơ một chiều có chổi than và không chổi than",
                "dc Brush and Brushless Motors"))
    b.append(p(
        "Động cơ servo một chiều là cơ cấu chấp hành lâu đời nhất và có lẽ được dùng nhiều nhất cho các "
        "hệ servo. Tên gọi bắt nguồn từ việc đặt một điện áp không đổi (một chiều) lên động cơ sẽ làm "
        "động cơ chuyển động. Trong một dải tuyến tính, các động cơ này có mômen tỉ lệ với dòng chạy "
        "trong cuộn dây. Nhược điểm chính của động cơ một chiều có chổi than là chổi than — bộ phận "
        "thực hiện chuyển mạch cơ khí. Chổi than là chi tiết hỏng đầu tiên của động cơ, làm giảm mạnh "
        "độ tin cậy của động cơ một chiều có chổi than so với các cơ cấu chấp hành khác."))
    b.append(p(
        "Một loại động cơ khác hoạt động tương tự động cơ một chiều có chổi than là động cơ một chiều "
        "không chổi than (đặt điện áp một chiều vào, nó sẽ quay). Tuy vậy, cách chuyển mạch của nó khác "
        "hẳn. Trong khi động cơ một chiều thực hiện chuyển mạch bằng cơ khí nhờ chổi than, động cơ một "
        "chiều không chổi than dùng cảm biến Hall để điều khiển việc chuyển mạch bằng điện tử. Nhờ đó, "
        "động cơ một chiều không chổi than có tuổi thọ và độ tin cậy cao hơn nhiều."))

    b.append(h3("Bộ khuếch đại công suất điều chế độ rộng xung",
                "Pulse Width–Modulated Power Amplifier"))
    b.append(p(
        "Trong nhiều hệ thống sử dụng, động cơ một chiều cần có điện áp thay đổi ở đầu vào để tạo ra "
        "biên dạng vị trí hay vận tốc mong muốn. Tuy nhiên, nhiều hệ trong số đó chỉ có một nguồn nuôi "
        "duy nhất V<sub>ss</sub>. Thay vì dùng bộ khuếch đại công suất tương tự vừa đắt vừa kém hiệu "
        "quả, người ta dùng bộ khuếch đại điều chế độ rộng xung (PWM). Bộ khuếch đại PWM chỉ có thể cấp "
        "cho động cơ V<sub>ss</sub> hoặc −V<sub>ss</sub> (hoặc bằng 0 ở một số thiết kế). Các mức điện "
        "áp khác nhau đạt được bằng cách thay đổi tỉ lệ phần trăm tương đối thời gian cấp V<sub>ss</sub> "
        "và −V<sub>ss</sub> cho động cơ ở một tần số cố định cao. Điện áp trung bình đặt lên động cơ là "
        "hàm tuyến tính của tỉ lệ tương đối này, tức chu kỳ làm việc. Động cơ cũng nhận các hài bậc cao "
        "của tín hiệu chuyển mạch — những bội nguyên của tần số cơ bản của xung vuông. Tuy vậy, phần lớn "
        "động cơ có ít nhất hai cực (một cực điện và một cực cơ) chậm hơn hẳn tần số chuyển mạch, nên "
        "suy giảm mạnh mọi ảnh hưởng có thể có của các hài này lên chuyển động. Hình 101.2 cho thấy một "
        "bộ khuếch đại PWM được đặt để cấp 12 V cho động cơ."))
    b.append(fig(2, F.fig(2)))

    b.append(h3("Đo động học của hệ thống", "Measuring the System Dynamics"))
    b.append(p(
        "Với những hệ có yêu cầu chuyển động vừa phải hoặc khắt khe, động cơ một chiều có chổi than và "
        "không chổi than được vận hành theo kiểu vòng kín. Muốn làm việc ở vòng kín, cần đo được vị trí "
        "hoặc vận tốc. Máy đo tốc độ (tachometer) thường được dùng để đo tốc độ quay: nó cho ra điện áp "
        "tỉ lệ với tốc độ của phần tử quay. Nếu cần đo vị trí, có thể dùng bộ mã hoá gia số. Bộ mã hoá "
        "gia số tạo ra xung số tại những điểm vị trí cách đều nhau. Ví dụ, bộ mã hoá 1000 vạch/vòng sẽ "
        "tạo ra một dạng xung số có 1000 sườn lên (và 1000 sườn xuống) trong một vòng quay."))
    b.append(p(
        "Khi đã xác định được toàn bộ hệ (kể cả các cảm biến phản hồi), có thể xây dựng thuật toán điều "
        "khiển phản hồi. Trong thiết kế nhiều thuật toán bù — đặc biệt là các bộ bù tuyến tính như phản "
        "hồi trạng thái hay PID — một trong những việc quan trọng nhất là có mô hình tốt về động học "
        "của hệ."))
    b.append(p(
        "Có nhiều cách tạo mô hình. Một trong những cách phổ biến nhất là lập phương trình trạng thái "
        "của hệ từ các phương trình vật lý. Cách này đòi hỏi biết mọi tham số của hệ. Có những tham số "
        "rất khó đo và nhà chế tạo không cung cấp. Một ví dụ là hằng số xoắn của một trục cao su cứng "
        "trong hệ."))
    b.append(p(
        "Kể cả khi đã biết mọi tham số, vẫn nên có một phương pháp đo đáp ứng của hệ. Phương pháp đó cho "
        "cách kiểm chứng mô hình, hoặc cho người thiết kế biết rằng mô hình không mô tả chính xác hệ."))
    b.append(p(
        "Dưới đây trình bày một phương pháp cho phép thu thập dữ liệu vào/ra của một hệ. Dữ liệu này sau "
        "đó có thể dùng để khớp một đường đáp ứng tần số hoặc một mô hình hàm truyền của hệ. Các máy "
        "phân tích tín hiệu như HP3562A có khả năng khớp đường cong như vậy một cách chính xác. Ngoài "
        "ra, nếu dữ liệu được thu thập rời rạc, có sẵn các công cụ phần mềm thương mại như MATLAB để "
        "ước lượng mô hình ở dạng tham số (ví dụ không gian trạng thái/hàm truyền) hoặc phi tham số (ví "
        "dụ đáp ứng tần số). Tuy quy trình này được mô tả cho hệ động cơ, nó dễ dàng áp dụng cho hầu hết "
        "hệ tuyến tính."))
    b.append(p(
        "Giả sử có một hệ vòng kín điển hình như trên Hình 101.3. Có vài trở ngại khiến việc xác định "
        "hàm truyền vòng hở hay vòng kín của hệ này trở nên khó khăn, trong đó có việc không đo được "
        "một số ngõ ra và không điều khiển/thay đổi được một số ngõ vào."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Để lấy đáp ứng tần số của một hệ, cần kích thích hệ bằng một tín hiệu vào đã biết và đo đáp "
        "ứng gây ra. Muốn vậy phải có một ngõ vào điều khiển được — tức ngõ vào có thể tác động từ bên "
        "ngoài. Với hệ trên Hình 101.3, các ngõ vào điều khiển được chỉ có mômen tác dụng lên trục động "
        "cơ và tín hiệu tham chiếu."))
    b.append(p(
        "Muốn thay đổi mômen ngoài phải gắn cơ khí một phanh đã hiệu chuẩn hoặc một động cơ khác. Việc "
        "này không chỉ cồng kềnh mà còn có thể làm thay đổi động học của hệ, vì nó đưa thêm quán tính "
        "vào đúng cái hệ đang được đo. Trong nhiều hệ, tín hiệu tham chiếu là xung vuông số (vì phần tử "
        "phản hồi là bộ mã hoá gia số, cũng tạo ra dạng xung tương tự), nên nếu muốn tác động trực tiếp "
        "lên tham chiếu thì phải có bộ chuyển đổi điện áp – tần số. Bộ chuyển đổi này có thể mang theo "
        "động học riêng và làm sai lệch dữ liệu đo."))
    b.append(p(
        "Ngoài một ngõ vào điều khiển được, còn phải có một ngõ ra đo được. Trong nhiều hệ servo, ngõ ra "
        "đo được chỉ là điện áp phần ứng động cơ và vị trí/vận tốc. Điện áp phần ứng có thể là tín hiệu "
        "PWM và cần được lọc để thành điện áp tương tự. Với bộ mã hoá gia số, ngõ ra là xung vuông số do "
        "bộ mã hoá tạo ra: cần bộ chuyển đổi tần số – điện áp để có ngõ ra tương tự. Bộ chuyển đổi này "
        "cũng có thể mang theo động học riêng và làm sai lệch dữ liệu đo."))
    b.append(p(
        "Xét hệ được mô tả trên Hình 101.4. Bộ cộng đặt thêm vào hệ có ưu điểm là có thể chèn ở bất kỳ "
        "điểm nào thuận tiện cho việc đo — nó không còn bị giới hạn ở ngõ vào hay ngõ ra nguyên thuỷ "
        "của hệ."))
    b.append(fig(4, F.fig(4)))
    b.append(p(
        "Với bộ điều khiển tương tự, ngõ vào và ngõ ra của bộ cộng là các điện áp tương tự, nên rất dễ "
        "điều khiển và đo. Nút cộng có thể được thực hiện dễ dàng bằng một mạch cộng dùng op-amp đơn "
        "giản. Mạch này không đưa thêm động học đáng kể nào vào hệ ban đầu, và do đó không làm lệch dữ "
        "liệu đo."))
    b.append(p(
        "Khi đo đáp ứng của hệ, phải loại bỏ các thành phần biến thiên theo thời gian của những ngõ vào "
        "khác: tham chiếu vận tốc và mômen ngoài T<sub>d</sub> tác dụng lên hệ. Người thiết kế phải đặt "
        "tham chiếu vận tốc ở một giá trị không đổi. Mômen ngoài tác dụng lên hệ thường rất ít khi điều "
        "khiển được, và nó sẽ đưa nhiễu vào phép đo. Để bảo đảm tỉ số tín hiệu trên nhiễu (SNR) lớn, "
        "ngõ vào tham chiếu thay thế (tín hiệu z(t)) nên được đặt càng lớn càng tốt."))
    b.append(p(
        "Ngõ vào tham chiếu thay thế z(t) có thể kích thích hệ bằng tín hiệu sin quét, tín hiệu ngẫu "
        "nhiên hoặc bất kỳ tín hiệu mong muốn nào khác. Trong quá trình kích thích, người ta ghi lại "
        "theo thời gian các nút khác của bộ cộng, y(t) và x(t). Hàm truyền giữa Y và X là:"))
    b.append(eq("Y(s)/X(s) = −G<sub>c</sub>(s) K<sub>amp</sub>(s) G<sub>m</sub>(s)", "101.12"))
    b.append(eq("−Y(s)/X(s) = G<sub>c</sub>(s) K<sub>amp</sub>(s) G<sub>m</sub>(s)", "101.12"))
    b.append(p(
        "Số hạng thứ hai, theo định nghĩa, chính là hàm truyền vòng hở của hệ. Như trước, MATLAB hoặc "
        "một máy phân tích tín hiệu có thể khớp tham số hoặc phi tham số hàm truyền này từ chuỗi dữ "
        "liệu."))
    b.append(p(
        "Cần lưu ý rằng kỹ thuật này đòi hỏi hệ phải đang làm việc ở chế độ vòng kín trong suốt quá "
        "trình thu thập dữ liệu. Thông thường G<sub>c</sub> được đặt là bộ điều khiển tỉ lệ với hệ số "
        "bảo đảm ổn định toàn hệ. Để thu dữ liệu tốt, nên đặt hệ số tỉ lệ càng lớn càng tốt."))
    b.append(p(
        "Trường hợp hệ điều khiển bằng số hoặc bằng vi xử lý có thể xử lý tương tự, chỉ cần sửa đổi đôi "
        "chút. Xét hệ trên Hình 101.5, trong đó vi xử lý đóng vai trò bộ điều khiển của hệ. Ở đây, bộ "
        "cộng có thể được thực hiện ngay bên trong vi xử lý bằng một lệnh cộng. Vấn đề trở thành đưa dữ "
        "liệu vào và ra khỏi vi xử lý. Đưa dữ liệu vào vi xử lý đòi hỏi thêm một bộ chuyển đổi tương tự "
        "– số (ADC). Trong sơ đồ khối, quá trình ADC được biểu diễn bằng khối A<sub>f</sub>. Khối "
        "A<sub>f</sub> cho phép biểu diễn mọi động học vốn có trong thiết kế ADC (đặc biệt là hệ số "
        "khuếch đại). Ngõ ra của vi xử lý có thể là tín hiệu PWM số. Tín hiệu này có thể cần được lọc "
        "thông thấp để tạo điện áp tương tự cho máy phân tích tín hiệu đang thu dữ liệu. Bộ lọc thông "
        "thấp được biểu diễn bằng khối P<sub>f</sub> trên Hình 101.5; nó thường là một mạch RC đơn giản "
        "có tần số cắt thấp hơn nhiều so với tần số tín hiệu PWM."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Với điều kiện ω<sub>ref</sub> không đổi và mômen ngoài T<sub>d</sub> không đáng kể, hàm truyền "
        "giữa Z<sub>a</sub>(s) và X<sub>a</sub>(s) trên Hình 101.5 là:"))
    b.append(eq("Z<sub>a</sub>(s)/X<sub>a</sub>(s) = (1 + G<sub>c</sub>(s) S<sub>H</sub>(s) "
                "K<sub>amp</sub>(s) G<sub>m</sub>(s)) / (A<sub>f</sub>(s) S<sub>H</sub>(s) "
                "P<sub>f</sub>(s)) ≡ O(s)", "101.13"))
    b.append(p(
        "Khi G<sub>c</sub> = 0, Z<sub>a</sub>(s)/X<sub>a</sub>(s) = 1/(A<sub>f</sub>(s)"
        "S<sub>H</sub>(s)P<sub>f</sub>(s)) ≡ C(s), và (O(s) − C(s))/C(s) = G<sub>c</sub>(s)"
        "S<sub>H</sub>(s)K<sub>amp</sub>(s)G<sub>m</sub>(s); đây chính là hàm truyền vòng hở của hệ."))
    b.append(p(
        "Có một cách trực tiếp hơn nếu không dùng máy phân tích logic mà dùng một gói nhận dạng hệ thống "
        "chạy bằng phần mềm như MATLAB để khớp dữ liệu. Tín hiệu kích thích z có thể được lưu sẵn thành "
        "một tập dữ liệu trong bảng tra ở bộ nhớ vi xử lý, hoặc được sinh ra theo thời gian thực bằng "
        "bất kỳ thuật toán sinh số ngẫu nhiên nào hoặc thuật toán khác. Dữ liệu Y và X tại bộ cộng bên "
        "trong có thể thu được nhờ máy phân tích logic hoặc bộ mô phỏng (emulator) nếu các giá trị y(k) "
        "(giá trị của y tại chu kỳ lấy mẫu thứ k) và x(k) được ghi ra bus ngoài ở mỗi chu kỳ lấy mẫu. "
        "Với cấu hình này, không cần DAC cũng không cần ADC, và cũng không cần tổ hợp toán học nào của "
        "hai hàm truyền khác nhau để có hàm truyền vòng hở mong muốn. Hàm truyền giữa Y(z) và X(z) là:"))
    b.append(eq("Y(z)/X(z) = −G<sub>c</sub>(z) S<sub>H</sub>(z) K<sub>amp</sub>(z) G<sub>m</sub>(z)",
                "101.14"))
    b.append(eq("−Y(z)/X(z) = G<sub>c</sub>(z) S<sub>H</sub>(z) K<sub>amp</sub>(z) G<sub>m</sub>(z)",
                "101.14"))
    b.append(p(
        "Một lần nữa, đây chính là hàm truyền vòng hở của hệ, thu được chỉ với một ít phần mềm bổ sung "
        "và một máy phân tích logic. Như trước, tập dữ liệu vào/ra có thể được đưa vào bất kỳ thuật "
        "toán nhận dạng hệ thống nào để khớp hàm truyền."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "E. Hamman, “Closed-loop control of a DC stepping motor using state space techniques,” luận văn "
        "thạc sĩ, Rensselaer Polytechnic Institute, Troy, NY, 1983.",
        "S. Schweid, “Velocity control of DC stepping motors utilizing state space theory, "
        "quasilinearization and reduced order estimation/control,” luận văn thạc sĩ, Rensselaer "
        "Polytechnic Institute, Troy, NY, 1985.",
        "J. Tal, L. Antignini, P. Gandel và N. Veignat, “Damping a two-phase step motor with velocity "
        "coils,” Incremental Motion Control Systems and Devices Symposium, Champaign, IL, 1985, "
        "305–309.",
        "D. Reignier, “Very accurate positioning system for high speed, high acceleration motion "
        "control,” Power Conversion and Intelligent Motion, 13, 52–62, tháng 6, 1987.",
        "D. Reignier, “Damping circuit and rotor encoder cut disc magnet step motor overshoot, "
        "settling time and resonances,” Power Conversion and Intelligent Motion, 14, 64–69, tháng 4, "
        "1988.",
        "S. Schweid, J. McInroy và R. Lofthus, “Closed loop low-velocity regulation of hybrid stepping "
        "motors amidst torque disturbances,” IEEE Trans. Ind. Electron., 42, 316–324, 1995.",
        "R. Lofthus, S. Schweid, J. McInroy và Y. Ota, “Processing back EMF signals of hybrid step "
        "motors,” Control Eng. Practice, 3(10), 1–10, 1995.",
    ]))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []
    b.append(p(
        "Many systems — robots, for instance — exist precisely because they can move themselves or "
        "other objects. A great many more, xerographic printers among them, do not want the motion for "
        "its own sake: the motion is simply a condition of doing the main job. Every one of these "
        "systems needs one or more prime movers, the parts that directly or indirectly create all of "
        "the motion in the system."))

    b.append(h2("101.1 Introduction"))
    b.append(p(
        "These applications differ widely in the kind of motion they need and in how precisely it must "
        "be produced. A child's toy works well enough with imprecise motion; printing demands very "
        "precise motion control. Depending on what is required, a prime mover can be chosen from a "
        "small set of candidates — dc brush motors, dc brushless motors and hybrid stepping motors — "
        "and the system around it can be controlled either as a function of time alone (open loop) or "
        "as a function of both time and system state (closed loop)."))
    b.append(p(
        "A closed-loop system needs some way of measuring the state of the system; for motion systems "
        "that usually means one or more sensors of position and/or velocity. For many control "
        "techniques — linear controllers in particular — it also helps to have a model of the plant, "
        "which can then be used with the usual design methods to improve the dynamic response "
        "substantially. This chapter describes the main modes of operation of those prime movers and "
        "then sets out, in detail, a method for measuring the open-loop response of a candidate motion "
        "system."))

    b.append(h2("101.2 Hybrid Stepping Motors"))
    b.append(p(
        "Hybrid stepping motors give fairly accurate positioning in open loop, which is how they are "
        "most often used. They succeed there because they stay within a commanded step as long as they "
        "have enough torque to resist whatever external torque the system applies. Since the motor "
        "runs open loop, it must be chosen a priori to supply that torque: the peak torque the system "
        "needs follows from its inertia, its acceleration profile and the external torque upon it. "
        "Once the torque required at every speed is known, a motor is picked from its torque–speed "
        "curve, which gives the greatest torque that can be tolerated at each speed without losing a "
        "step. A motor whose curve stays above the requirement at all speeds will do."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "A hybrid stepping motor has several coils — almost always two — which turn the rotor when "
        "they are commutated in a fixed sequence. In “full stepping” the current command to each "
        "winding is constant in magnitude and varies only in polarity; which direction counts as "
        "positive is entirely arbitrary. In that mode the motor needs only four separate energisations "
        "of the winding per revolution, although clever mechanical arrangements raise the number of "
        "steps per revolution far above that — typically 200, and as many as 800."))
    b.append(p(
        "With two windings, A and B, the four possible energisations are A+B+, A+B−, A−B− and A−B+. "
        "Command them to the motor in that order and it turns."))

    b.append(h3("Chopping Current Amplifiers"))
    b.append(p(
        "The stepper needs a current of a particular amplitude in its winding, but for economic reasons "
        "most systems provide a voltage supply (V<sub>ss</sub>) rather than a current source. A current "
        "chopper is a low-cost closed-loop switching amplifier that regulates the winding current, "
        "exploiting the significant inductance of the winding. The two windings obey:"))
    b.append(eq("dI<sub>A</sub>/dt = (V<sub>A</sub> − I<sub>A</sub>R<sub>A</sub> − "
                "K<sub>b</sub>ω sin θ) / L<sub>A</sub>", "101.1"))
    b.append(eq("dI<sub>B</sub>/dt = (V<sub>B</sub> − I<sub>B</sub>R<sub>B</sub> − "
                "K<sub>b</sub>ω cos θ) / L<sub>B</sub>", "101.1"))
    b.append(p(
        "where I is the winding current (A), R the winding resistance (Ω), L the winding inductance "
        "(H), V the applied voltage (V), K<sub>b</sub> the torque constant (Nm/A), ω the motor velocity "
        "(rad/s) and θ the motor position (electrical rad). Every t<sub>s</sub> — a very short "
        "interval, of order 10 µs — the chopper applies either V<sub>ss</sub> or −V<sub>ss</sub> to the "
        "winding, according to whether the desired current I<sub>M</sub> is above or below the measured "
        "one:"))
    b.append(eq("if I<sub>A</sub> &lt; I<sub>M</sub> then V<sub>A</sub> = V<sub>ss</sub>, "
                "else V<sub>A</sub> = −V<sub>ss</sub>", "101.2"))
    b.append(eq("if I<sub>B</sub> &lt; I<sub>M</sub> then V<sub>B</sub> = V<sub>ss</sub>, "
                "else V<sub>B</sub> = −V<sub>ss</sub>", "101.2"))
    b.append(p(
        "The usual requirement is that V<sub>ss</sub>t<sub>s</sub>/L be small against I<sub>M</sub>, so "
        "that the chopping ripple is small against the wanted current; and because the mechanical "
        "system is low-pass by nature, it barely responds to the small-amplitude, high-frequency "
        "components that remain."))

    b.append(h3("Microstepping"))
    b.append(p(
        "Microstepping lets the commanded reference position fall between the full-step positions. The "
        "commanded currents for a reference position θ<sub>ref</sub> are:"))
    b.append(eq("I<sub>A</sub> = I<sub>M</sub> cos θ<sub>ref</sub>", "101.3"))
    b.append(eq("I<sub>B</sub> = I<sub>M</sub> sin θ<sub>ref</sub>", "101.3"))
    b.append(p(
        "where θ<sub>ref</sub> is the desired electrical position (four full steps carry it through one "
        "electrical revolution). For constant-velocity work:"))
    b.append(eq("θ<sub>ref</sub> = N ω<sub>d</sub> t", "101.4"))
    b.append(p(
        "with N the number of electrical revolutions per mechanical revolution — a quarter of the steps "
        "per revolution — and ω<sub>d</sub> the desired velocity (rad/s)."))

    b.append(h3("Closed-Loop Control"))
    b.append(p(
        "Hybrid stepping motors can also be run closed loop, but they are nonlinear devices, so the "
        "linear design toolbox does not apply directly. Hamman and Balas [1] linearise about each step "
        "with a fourth-order model, which is useful for reshaping the undamped response to a commanded "
        "change of position. Schweid [2] proposes a scheme giving good transients at constant velocity "
        "while using the full fourth-order model. Where current choppers are fitted, a second-order "
        "model suffices, and the following control law can be applied [3–5]:"))
    b.append(eq("I<sub>A</sub> = I<sub>M</sub> cos θ<sub>ref</sub> − "
                "I<sub>C</sub> sin θ<sub>ref</sub>", "101.5"))
    b.append(eq("I<sub>B</sub> = I<sub>M</sub> sin θ<sub>ref</sub> + "
                "I<sub>C</sub> sin θ<sub>ref</sub>", "101.5"))
    b.append(p(
        "These currents linearise the motor model, so ordinary techniques such as PID control can be "
        "used [6]. I<sub>M</sub> is the open-loop component that microsteps the motor; I<sub>C</sub> is "
        "a feedback term that buys an improved dynamic response."))
    b.append(note(
        "<b>Translator's note.</b> The printed equation 101.5 gives the second term of "
        "I<sub>B</sub> as <i>sin</i> θ<sub>ref</sub>, identical to the first. For the pair to be "
        "orthogonal — the condition that makes it linearise the model — that term has to be "
        "<i>cos</i> θ<sub>ref</sub>. The translation keeps the print and flags the point rather than "
        "silently correcting it."))

    b.append(h3("Position Measurement"))
    b.append(p(
        "Closed-loop control needs a position measurement, and that measurement must be aligned with "
        "the motor's construction rather than offset from it, because the law of equation 101.5 "
        "multiplies the command current I<sub>C</sub> by the sine and cosine of the motor position. One "
        "way is an incremental encoder with an index pulse on the motor; a calibration then fixes the "
        "position of the index relative to the shaft, and that relationship serves for all later "
        "measurements."))
    b.append(p(
        "Another scheme estimates position from the back emf of the two coils. Some motors are built "
        "with extra sensing coils that make those signals easy to measure. From equation 101.2:"))
    b.append(eq("V<sub>emfA</sub> = K<sub>b</sub>ω sin θ = V<sub>A</sub> − I<sub>A</sub>R<sub>A</sub> − "
                "L<sub>A</sub> dI<sub>A</sub>/dt", "101.6"))
    b.append(eq("V<sub>emfB</sub> = K<sub>b</sub>ω cos θ = V<sub>B</sub> − I<sub>B</sub>R<sub>B</sub> − "
                "L<sub>B</sub> dI<sub>B</sub>/dt", "101.6"))
    b.append(p("and the position follows from:"))
    b.append(eq("θ = −atan(V<sub>emfA</sub> / V<sub>emfB</sub>)", "101.7"))
    b.append(p(
        "In most motors those two signals cannot be measured directly, but at constant velocity an "
        "excellent estimate is still available by approximating them from low-pass-filtered coil "
        "voltages. A method developed at Xerox, patented as U.S. 5378975, is described here. Taking the "
        "Laplace transform of equation 101.6:"))
    b.append(eq("V<sub>emfA</sub>(s) = V<sub>A</sub>(s) − (R<sub>A</sub> + sL<sub>A</sub>)"
                "I<sub>A</sub>(s)", "101.8"))
    b.append(eq("V<sub>emfB</sub>(s) = V<sub>B</sub>(s) − (R<sub>B</sub> + sL<sub>B</sub>)"
                "I<sub>B</sub>(s)", "101.8"))
    b.append(p(
        "Filtering both sides with low-pass filters matched to the coil dynamics gives:"))
    b.append(eq("V<sub>filtA</sub>(s) = V<sub>A</sub>(s)/(1 + sL<sub>A</sub>/R<sub>A</sub>) − "
                "R<sub>A</sub>I<sub>A</sub>(s)", "101.9"))
    b.append(eq("V<sub>filtB</sub>(s) = V<sub>B</sub>(s)/(1 + sL<sub>B</sub>/R<sub>B</sub>) − "
                "R<sub>B</sub>I<sub>B</sub>(s)", "101.9"))
    b.append(p(
        "Both quantities are easy to obtain: low-pass the coil voltage with a simple RC network and "
        "subtract the IR term. The subtraction is easy because the current is a known input — it is "
        "commanded — and the resistance is easily measured."))
    b.append(p(
        "Assume matched coils, L = L<sub>A</sub> = L<sub>B</sub> and R = R<sub>A</sub> = R<sub>B</sub>, "
        "and constant velocity θ = Nω<sub>d</sub>t; the back emf voltages are then sinusoidal, and "
        "their filtered versions are:"))
    b.append(eq("V<sub>filtA</sub>(s) = |H(Nω<sub>d</sub>)| K<sub>b</sub> sin(Nω<sub>d</sub>t + φ)",
                "101.10"))
    b.append(eq("V<sub>filtB</sub>(s) = |H(Nω<sub>d</sub>)| K<sub>b</sub> cos(Nω<sub>d</sub>t + φ)",
                "101.10"))
    b.append(p(
        "where |H(Nω<sub>d</sub>)| is the magnitude response of the filter at the input frequency and "
        "φ = −atan(Nω<sub>d</sub>L/R) the phase shift the filtering introduces. Dividing the two and "
        "taking the inverse tangent:"))
    b.append(eq("θ = atan(−V<sub>filtA</sub>(t) / V<sub>filtB</sub>(t)) + "
                "atan(Nω<sub>d</sub>L/R)", "101.11"))
    b.append(p(
        "The full derivation is in reference [7], which also adds Kalman filtering to improve the "
        "velocity estimate obtained from position — necessary because differentiating a position "
        "measurement is very sensitive to noise."))

    b.append(h2("101.3 dc Brush and Brushless Motors"))
    b.append(p(
        "The dc servomotor is the oldest and probably the most widely used servo actuator. Its name "
        "comes from the fact that a constant (dc) voltage makes it move, and over a linear range its "
        "torque is proportional to winding current. Its chief disadvantage is the brush, which does the "
        "mechanical commutation; brushes are the first part to fail, which limits the reliability of "
        "the dc brush motor against other actuators."))
    b.append(p(
        "The dc brushless motor behaves similarly — a dc voltage turns it — but commutates very "
        "differently. Where the brushed motor switches mechanically, the brushless motor uses Hall "
        "effect sensors to switch electronically, and so achieves far greater life and reliability."))

    b.append(h3("Pulse Width–Modulated Power Amplifier"))
    b.append(p(
        "Many systems need a varying voltage at the motor terminals to produce the required position or "
        "velocity profile, yet have only a single supply V<sub>ss</sub>. Rather than an analog power "
        "amplifier — expensive and inefficient — a pulse width–modulated (PWM) amplifier is used. It "
        "can deliver only V<sub>ss</sub>, −V<sub>ss</sub> (or zero in some designs); intermediate "
        "voltages come from varying the relative percentage of time each is applied at a high fixed "
        "frequency, and the mean voltage is a linear function of that duty cycle. The motor also sees "
        "the higher harmonics of the switched waveform, at integer multiples of the square-wave "
        "frequency, but most motors have at least two poles — one electrical, one mechanical — far "
        "slower than the switching frequency, and these attenuate any effect they might have on "
        "motion. Figure 101.2 shows a PWM amplifier set to deliver 12 V from a 24 V rail."))
    b.append(fig(2, F.fig(2), "en"))

    b.append(h3("Measuring the System Dynamics"))
    b.append(p(
        "Where motion requirements are moderate or stringent, dc brush and brushless motors run closed "
        "loop, which needs a measure of position or velocity. A tachometer is commonly used for "
        "rotational speed, outputting a voltage proportional to it; where position is needed, an "
        "incremental encoder produces a digital pulse at equal position intervals — a 1000 "
        "line/revolution encoder gives 1000 rising (and 1000 falling) edges per revolution."))
    b.append(p(
        "Once the full system, feedback sensors included, is known, a feedback control algorithm can be "
        "developed. In the design of most compensation algorithms — linear compensators such as state "
        "feedback or PID especially — one of the most important tasks is to have a good model of the "
        "system dynamics."))
    b.append(p(
        "There are several ways to get one. The commonest is to write the state equations from the "
        "physical equations, which requires every parameter to be known; some are hard to measure and "
        "are not supplied by the manufacturer — the torsional constant of a hard rubber roll, say. Even "
        "with every parameter known it is still worth having a way of measuring the response, because "
        "that either validates the model or tells the designer it is not an accurate representation of "
        "the system."))
    b.append(p(
        "The method below collects input/output data which can then be fitted to a frequency response "
        "or a transfer function. Signal analyzers such as the HP3562A do that curve fitting accurately; "
        "and if the data are collected discretely, packages such as MATLAB estimate a model in "
        "parametric (state space, transfer function) or nonparametric (frequency response) form. The "
        "procedure is written for motor systems but applies to most linear systems."))
    b.append(p(
        "Take a typical closed-loop system as in Fig. 101.3. Several obstacles make its open- or "
        "closed-loop transfer function hard to obtain: some outputs cannot be measured, and some inputs "
        "cannot be controlled or modified."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "To acquire a frequency response, perturb the system with a known input and measure the "
        "response; that needs a controllable input, one that can be manipulated from outside. In Fig. "
        "101.3 the only controllable inputs are the torque on the motor shaft and the reference "
        "command."))
    b.append(p(
        "Changing the external torque means attaching a calibrated brake or another motor. That is "
        "cumbersome, and it alters the dynamics by adding inertia to the very system being measured. In "
        "many systems the reference is a digital square wave — the feedback element is an incremental "
        "encoder and produces a similar wave — so manipulating it directly needs a voltage-to-frequency "
        "converter, whose own dynamics can corrupt the data."))
    b.append(p(
        "A measurable output must also be available. In many servo systems the only measurable outputs "
        "are armature voltage and position/velocity. The armature voltage may be a PWM signal needing "
        "filtering to an analog voltage; an incremental encoder output is a digital square wave needing "
        "a frequency-to-voltage converter. Either converter may bring dynamics that corrupt the data."))
    b.append(p(
        "Consider instead the system of Fig. 101.4. The summing junction added to it can be placed at "
        "any point convenient for measurement, so it is no longer limited to the unaugmented inputs or "
        "outputs of the system."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "With analog controllers the junction's inputs and outputs are analog voltages, easily "
        "controlled and measured; a simple op-amp adder implements it, adding no appreciable dynamics "
        "to the original system and therefore not skewing the data."))
    b.append(p(
        "When the response is to be measured, the time-varying contributions of the other inputs — the "
        "velocity reference and the external torque T<sub>d</sub> — must be eliminated. The velocity "
        "reference is simply held constant. The external torque is usually beyond control and will "
        "inject noise, so to secure a large signal-to-noise ratio the alternative reference z(t) should "
        "be made as large as possible."))
    b.append(p(
        "z(t) can be a swept sine, a random input or anything else. During the stimulation, time "
        "records of the other junction nodes, y(t) and x(t), are collected. The transfer function "
        "between Y and X is:"))
    b.append(eq("Y(s)/X(s) = −G<sub>c</sub>(s) K<sub>amp</sub>(s) G<sub>m</sub>(s)", "101.12"))
    b.append(eq("−Y(s)/X(s) = G<sub>c</sub>(s) K<sub>amp</sub>(s) G<sub>m</sub>(s)", "101.12"))
    b.append(p(
        "The second term is, by definition, the open-loop transfer function. As before, MATLAB or a "
        "signal analyzer fits it parametrically or nonparametrically from the record. Note that the "
        "system must be running closed loop while the data are collected, with G<sub>c</sub> a "
        "proportional controller at a value that keeps the whole system stable — and, for good data, as "
        "large as that allows."))
    b.append(p(
        "A digital or microprocessor-controlled system is handled similarly, with small modifications. "
        "In Fig. 101.5 a microprocessor is the controller, so the summing junction is just an add "
        "instruction inside it, and the problem becomes getting data in and out. Getting data in needs "
        "an ADC, represented by the block A<sub>f</sub>, which also carries any dynamics inherent in "
        "the converter — gain especially. The microprocessor output may be a digital PWM signal that "
        "needs low-pass filtering to give the analyzer an analog voltage; that filter is P<sub>f</sub>, "
        "typically a simple RC network whose cutoff is far below the PWM frequency."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "With ω<sub>ref</sub> static and T<sub>d</sub> minimal, the transfer function between "
        "Z<sub>a</sub>(s) and X<sub>a</sub>(s) in Fig. 101.5 is:"))
    b.append(eq("Z<sub>a</sub>(s)/X<sub>a</sub>(s) = (1 + G<sub>c</sub>(s) S<sub>H</sub>(s) "
                "K<sub>amp</sub>(s) G<sub>m</sub>(s)) / (A<sub>f</sub>(s) S<sub>H</sub>(s) "
                "P<sub>f</sub>(s)) ≡ O(s)", "101.13"))
    b.append(p(
        "When G<sub>c</sub> = 0, Z<sub>a</sub>(s)/X<sub>a</sub>(s) = 1/(A<sub>f</sub>(s)"
        "S<sub>H</sub>(s)P<sub>f</sub>(s)) ≡ C(s), and (O(s) − C(s))/C(s) = G<sub>c</sub>(s)"
        "S<sub>H</sub>(s)K<sub>amp</sub>(s)G<sub>m</sub>(s) — the open-loop transfer function."))
    b.append(p(
        "A more direct route opens up if a software system-identification package such as MATLAB is "
        "used instead of a logic analyzer. The stimulus z can be stored as a lookup table in "
        "microprocessor memory or generated in real time by any random-number or other algorithm; y(k) "
        "and x(k) at the internal junction can be captured by a logic analyzer or emulator if they are "
        "written to an external bus every sample period. Neither a DAC nor an ADC is then needed, and "
        "no combination of two transfer functions is required to reach the open-loop one. The transfer "
        "function between Y(z) and X(z) is:"))
    b.append(eq("Y(z)/X(z) = −G<sub>c</sub>(z) S<sub>H</sub>(z) K<sub>amp</sub>(z) G<sub>m</sub>(z)",
                "101.14"))
    b.append(eq("−Y(z)/X(z) = G<sub>c</sub>(z) S<sub>H</sub>(z) K<sub>amp</sub>(z) G<sub>m</sub>(z)",
                "101.14"))
    b.append(p(
        "Again this is the open-loop transfer function, obtained with minimal extra software and a "
        "logic analyzer, and again the input/output set can be handed to any identification algorithm."))

    b.append(h2("References"))
    b.append(refs([
        "E. Hamman, “Closed-loop control of a DC stepping motor using state space techniques,” "
        "Master's thesis, Rensselaer Polytechnic Institute, Troy, NY, 1983.",
        "S. Schweid, “Velocity control of DC stepping motors utilizing state space theory, "
        "quasilinearization and reduced order estimation/control,” Master's thesis, Rensselaer "
        "Polytechnic Institute, Troy, NY, 1985.",
        "J. Tal, L. Antignini, P. Gandel and N. Veignat, “Damping a two-phase step motor with velocity "
        "coils,” Incremental Motion Control Systems and Devices Symposium, Champaign, IL, 1985, "
        "305–309.",
        "D. Reignier, “Very accurate positioning system for high speed, high acceleration motion "
        "control,” Power Conversion and Intelligent Motion, 13, 52–62, June 1987.",
        "D. Reignier, “Damping circuit and rotor encoder cut disc magnet step motor overshoot, "
        "settling time and resonances,” Power Conversion and Intelligent Motion, 14, 64–69, April "
        "1988.",
        "S. Schweid, J. McInroy and R. Lofthus, “Closed loop low-velocity regulation of hybrid stepping "
        "motors amidst torque disturbances,” IEEE Trans. Ind. Electron., 42, 316–324, 1995.",
        "R. Lofthus, S. Schweid, J. McInroy and Y. Ota, “Processing back EMF signals of hybrid step "
        "motors,” Control Eng. Practice, 3(10), 1–10, 1995.",
    ]))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 101 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 101 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 101 “Đo và nhận diện động cơ bước chổi than, không chổi than "
            "và một chiều” của Stuart Schweid, Robert Lofthus và John McInroy — động cơ bước lai, bộ "
            "chặt dòng, vi bước, điều khiển vòng kín, đo vị trí bằng sức điện động cảm ứng, bộ "
            "khuếch đại PWM và phương pháp đo động học hệ thống, với 5 hình và 14 phương trình." if vi
            else
            "Companion to Chapter 101 of the CRC Measurement Handbook — hybrid stepping motors, "
            "chopping current amplifiers, microstepping, closed-loop control, position measurement "
            "from back emf, PWM amplifiers and a method for measuring system dynamics, with 5 figures "
            "and 14 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 101' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 101' % BASE_EN)
    meta = ("Chương 101 · theo Ch101.pdf (CRC Press, 1999) · 5 hình, 14 phương trình" if vi else
            "Chapter 101 · 5 figures, 14 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 101)))
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
