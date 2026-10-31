# -*- coding: utf-8 -*-
"""Handbook Chapter 17 — Acceleration, Vibration, and Shock Measurement (Halit Eren).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch17.py
"""
import os

import hb17fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch17-acceleration-vibration-shock-measurement"
TITLE_EN = "Acceleration, Vibration, and Shock Measurement"
TITLE_VI = "Đo gia tốc, rung động và xung kích"
BYLINE = "Halit Eren · Curtin University of Technology"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch16-velocity-measurement"
PREV_VI = "ch16-velocity-measurement"
PREV_T_EN = "Velocity Measurement"
PREV_T_VI = "Đo vận tốc"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-17-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Gia tốc được đo bởi các gia tốc kế như một thông số quan trọng cho đo chuyển động tuyệt đối nói chung, "
        "cũng như cảm biến rung động và xung kích. Gia tốc kế có mặt trên thị trường với rất nhiều dải đo và chủng "
        "loại nhằm đáp ứng các yêu cầu ứng dụng đa dạng. Chúng được chế tạo nhỏ gọn, nhẹ, bền chắc và bám sát để "
        "hoạt động được trong môi trường khắc nghiệt. Chúng có thể cấu hình như cảm biến chủ động (active) hoặc bị "
        "động (passive). Gia tốc kế chủ động (ví dụ áp điện) cho đầu ra mà không cần nguồn nuôi ngoài, trong khi "
        "gia tốc kế bị động chỉ thay đổi tính chất điện (ví dụ điện dung) và đòi hỏi nguồn điện ngoài. Trong ứng "
        "dụng, việc chọn loại chủ động hay bị động rất quan trọng, bởi cảm biến chủ động không đo được các chế độ "
        "tĩnh hay một chiều (dc). Với các phép đo tĩnh thực sự, nhất thiết phải dùng cảm biến bị động. Nhìn chung, "
        "gia tốc kế được ưu tiên hơn cảm biến dịch chuyển và vận tốc vì những lý do sau:"))
    b.append(p(
        "1. Chúng có dải tần rộng, từ không đến những giá trị rất cao. Gia tốc tĩnh đo được dễ dàng."))
    b.append(p(
        "2. Gia tốc thường được cần đến hơn, bởi các lực phá hoại thường liên quan đến gia tốc thay vì vận tốc hay "
        "dịch chuyển."))
    b.append(p(
        "3. Các quá trình quá độ (transient) và xung kích đo được dễ dàng, dễ hơn so với cảm biến dịch chuyển hay "
        "vận tốc."))
    b.append(p(
        "4. Dịch chuyển và vận tốc thu được bằng cách tích phân đơn giản gia tốc qua mạch điện tử. Tích phân được "
        "ưa chuộng hơn vi phân."))
    b.append(p(
        "Gia tốc kế có thể phân loại theo nhiều cách: loại lệch (deflection) hay loại triệt tiêu sai lệch (null-"
        "balance), cơ khí hay điện, động lực hay quán tính. Đa số gia tốc kế công nghiệp thuộc loại lệch hoặc loại "
        "triệt tiêu sai lệch. Loại dùng cho đo rung động và xung kích thường là loại lệch, còn loại dùng đo chuyển "
        "động phương tiện, máy bay… phục vụ dẫn đường có thể là một trong hai. Nhìn chung, loại triệt tiêu sai lệch "
        "được dùng khi cần độ chính xác cực cao. Số lớn gia tốc kế thực tế thuộc loại lệch; cấu hình chung được "
        "trình bày ở Hình 17.1. Có nhiều loại gia tốc kế lệch khác nhau; dù nguyên lý hoạt động tương tự, chúng "
        "chỉ khác ở những chi tiết nhỏ như phần tử lò xo, kiểu giảm chấn và kiểu cảm biến chuyển động tương đối. "
        "Các loại này cư xử như hệ bậc hai; phân tích toán học chi tiết sẽ có ở các phần sau."))
    b.append(fig(1, F.fig(1)))
    b.append(p(
        "Gia tốc kế có thể phân loại là động lực, nghĩa là hoạt động dựa trên đo lực cần thiết để giữ một khối lượng "
        "địa chấn (seismic mass) bám theo chuyển động của đế được gia tốc, như loại lò xo-giữ-khối. Loại khác là "
        "gia tốc kế quán tính (kinematic), dựa trên việc tính thời gian khối thử (proof mass) không bị ràng buộc "
        "chuyển từ các điểm đã đánh dấu trên đế được gia tốc; loại này chỉ thấy trong những ứng dụng rất đặc thù như "
        "tàu vũ trụ liên hành tinh và đo trọng lực (gravimetry). Về mặt thực tế, gia tốc kế còn phân loại cơ khí "
        "hay điện, tuỳ thuộc lực khôi phục hay cơ cấu đo khác dựa trên tính chất cơ học (ví dụ định luật chuyển "
        "động, biến dạng lò xo hay động lực học chất lưu…) hay trên lực điện từ."))
    b.append(p(
        "Hiệu chuẩn gia tốc kế là cần thiết trong đo gia tốc, rung động và xung kích. Phương pháp hiệu chuẩn có "
        "thể chia chung thành tĩnh và động. Hiệu chuẩn tĩnh tiến hành ở một hoặc vài mức gia tốc không đổi. Ví dụ "
        "dùng bàn nghiêng (tilting table), thành phần thẳng đứng của gia tốc rơi tự do được dùng mà không chọn được "
        "độ lớn. Ngược lại, dùng máy ly tâm (centrifuge) tạo ra gia tốc không đổi theo tốc độ quay, và độ lớn có "
        "thể chọn trong dải rộng từ 0 đến trên 50.000 g. Hiệu chuẩn động thường dùng bộ kích rung điện động "
        "(electrodynamic shaker) dao động hình sin với tần số và biên độ thay đổi, được ổn định ở các mức hiệu "
        "chuẩn. Đây là phương pháp tuyệt đối gồm đo dịch chuyển bằng giao thoa kế laser và đồng hồ tần số chính "
        "xác; bộ kích phải được khuếch đại công suất để cho đầu ra sin méo nhỏ nhất. Cục Tiêu chuẩn Quốc gia "
        "(National Bureau of Standards) dùng phương pháp này làm chuẩn tham chiếu. Gia tốc kế chính xác, phần lớn "
        "loại áp điện, được hiệu chuẩn bằng phương pháp tuyệt đối rồi dùng làm chuẩn làm việc. Một phương pháp "
        "ưa dùng là hiệu chuẩn lưng-đối-lưng (back-to-back), trong đó mẫu thử được gắn trực tiếp lên chuẩn làm "
        "việc, chuẩn lại gắn trên bộ kích rung điện động."))
    b.append(p(
        "Trước khi đi vào chi tiết từng loại gia tốc kế, các đặc điểm chung như động lực học, vận tốc, khoảng cách, "
        "tần số đáp ứng xung kích… sẽ được giới thiệu ở phần sau."))

    # ---- 17.1
    b.append(h2("17.1 Động lực học gia tốc kế: Đáp ứng tần số, giảm chấn, tỉ số giảm chấn và tính tuyến tính",
                "Accelerometer Dynamics: Frequency Response, Damping, Damping Ratio, and Linearity"))
    b.append(p(
        "Phần này quan tâm đến những tính chất vật lý của đo gia tốc, rung động và xung kích mà gia tốc kế thường "
        "dùng. Cần hiểu đầy đủ động lực học gia tốc kế liên quan đến đặc tính của gia tốc, rung động và xung kích. "
        "Rung động có thể là tuần hoàn, ngẫu nhiên dừng (stationary random), ngẫu nhiên không dừng (nonstationary "
        "random) hoặc quá độ."))
    b.append(h3("Rung động tuần hoàn", "Periodic Vibrations"))
    b.append(p(
        "Trong rung động tuần hoàn, chuyển động của vật lặp lại theo kiểu dao động. Nó có thể biểu diễn bằng dạng "
        "sóng sin:"))
    b.append(eq("x(t) = X_peak · sin(ω t)", "17.1"))
    b.append(p(
        "với x(t) = dịch chuyển theo thời gian, ω = 2πf = tần số góc, X_peak = dịch chuyển cực đại so với một điểm "
        "tham chiếu. Vận tốc của vật là tốc độ thay đổi theo thời gian của dịch chuyển:"))
    b.append(eq("u(t) = dx/dt = ω X_peak · cos(ω t) ,  U_peak = ω X_peak", "17.2"))
    b.append(p(
        "Gia tốc của vật là tốc độ thay đổi theo thời gian của vận tốc:"))
    b.append(eq("a(t) = du/dt = −ω² X_peak · sin(ω t) ,  A_peak = ω² X_peak = ω U_peak", "17.3"))
    b.append(p(
        "Từ các phương trình trên, thấy rằng dạng cơ bản và chu kỳ rung động giữ nguyên trong gia tốc, vận tốc và "
        "dịch chuyển. Nhưng vận tốc sớm pha 90° so với dịch chuyển và gia tốc sớm pha thêm 90° so với vận tốc. Biên "
        "độ của ba đại lượng liên hệ theo hàm của tần số, như ở Hình 17.2. Trong tự nhiên, rung động có thể tuần "
        "hoàn nhưng không nhất thiết là sin. Nếu tuần hoàn nhưng không sin, chúng có thể biểu diễn bằng tổ hợp của "
        "nhiều đường sin thuần qua phân tích Fourier:"))
    b.append(eq("x(t) = X₀ + X₁ sin(ω₁t + φ₁) + X₂ sin(ω₂t + φ₂) + … + Xₙ sin(ωₙt + φₙ)", "17.4"))
    b.append(p(
        "với ω₁…ωₙ = tần số (rad/s), X₀…Xₙ = biên độ cực đại tương ứng, φ₁…φₙ = góc pha. Số hạng có thể vô hạn: càng "
        "nhiều phần tử thì xấp xỉ càng tốt. Các phần tử này tạo nên phổ tần số. Rung động có thể biểu diễn trong "
        "miền thời gian hoặc miền tần số, cả hai đều rất hữu ích trong phân tích. Chẳng hạn, Hình 17.3 cho đáp "
        "ứng thời gian của khối lượng địa chấn một gia tốc kế trước một kích thích đế có dạng xung chữ nhật."))
    b.append(fig(2, F.fig(2)))
    b.append(fig(3, F.fig(3)))
    b.append(h3("Rung động ngẫu nhiên dừng", "Stationary Random Vibrations"))
    b.append(p(
        "Rung động ngẫu nhiên thường gặp trong tự nhiên, tạo nên những chu trình chuyển động không đều đặn không "
        "bao giờ lặp lại y hệt. Về lý thuyết, cần một bản ghi thời gian vô hạn dài để mô tả đầy đủ; tuy nhiên có "
        "thể dùng phương pháp thống kê và lý thuyết xác suất qua các mẫu đại diện. Các công cụ toán học như phân "
        "bố xác suất, mật độ xác suất, phổ tần số, tương quan chéo và tự tương quan, biến đổi Fourier số (DFT), "
        "biến đổi Fourier nhanh (FFT), phân tích tự phổ, giá trị RMS và lọc số là một số kỹ thuật có thể dùng."))
    b.append(h3("Quá độ và xung kích", "Transients and Shocks"))
    b.append(p(
        "Thường phải đo những rung động xảy ra đột ngột, thời gian ngắn. Xung kích và rung động quá độ có thể mô tả "
        "theo lực, gia tốc, vận tốc hay dịch chuyển. Như trường hợp ngẫu nhiên quá độ và xung kích, người ta dùng "
        "phương pháp thống kê và biến đổi Fourier trong phân tích."))
    b.append(h3("Rung động ngẫu nhiên không dừng", "Nonstationary Random Vibrations"))
    b.append(p(
        "Ở đây, tính chất thống kê của rung động biến thiên theo thời gian. Có thể dùng các phương pháp như trung "
        "bình thời gian và các kỹ thuật thống kê khác. Đa số gia tốc kế nói ở đây có thể xem và phân tích như những "
        "thiết bị địa chấn gồm khối lượng, lò xo và giảm chấn, như Hình 17.1. Chỉ xét hệ khối-lò xo, nếu hệ cư xử "
        "tuyến tính và bất biến theo thời gian, phương trình vi phân bậc hai cơ bản cho chuyển động của riêng khối "
        "lượng dưới tác dụng của một lực viết được:"))
    b.append(eq("m ẍ + c ẋ + k x = f(t)", "17.5"))
    b.append(p(
        "với f(t) = lực, m = khối lượng, c = hằng số vận tốc (tức cản nhớt), k = hằng số lò xo. Tuy nhiên, trong "
        "gia tốc kế địa chấn, đế của cụm cũng chuyển động. Do đó, phương trình 17.5 được tổng quát hoá xét đến "
        "chuyển động của đế. Gọi z = x₂ − x₁ = chuyển động tương đối giữa khối và đế, x₁ = dịch chuyển của đế, x₂ "
        "= dịch chuyển của khối, θ = góc giữa trục cảm biến và trọng trường, phương trình 17.5 sửa lại thành:"))
    b.append(eq("m z̈ + c ż + k z = m g cosθ − m ẍ₁", "17.6"))
    b.append(p(
        "Để tạo cơ sở cho phân tích tiếp, xét trường hợp đơn giản, nghiệm đầy đủ của phương trình 17.5 thu được "
        "bằng nguyên lý xếp chồng. Nguyên lý này phát biểu: nếu có những tác động chồng chất đồng thời lên một vật, "
        "hiệu ứng tổng cộng bằng tổng các hiệu ứng của từng tác động riêng. Phương trình 17.5 thực chất mô tả một "
        "hệ bậc hai, có thể viết trong miền Laplace:"))
    b.append(eq("X(s)/F(s) = 1 / (m s² + c s + k)", "17.7"))
    b.append(eq("X(s)/F(s) = K / (s² + 2 ζ ωₙ s + ωₙ²)", "17.8"))
    b.append(p(
        "với s = toán tử Laplace, K = 1/k = độ nhạy tĩnh, ωₙ = √(k/m) = tần số tới hạn không giảm chấn (rad/s), "
        "ζ = c/(2√(km)) = tỉ số giảm chấn. Như thấy, trong đặc tính gia tốc kế, các tham số quan trọng là độ nhạy "
        "tĩnh, tần số tự nhiên và tỉ số giảm chấn, vốn là hàm của khối lượng, vận tốc và hằng số lò xo. Gia tốc kế "
        "được thiết kế với những đặc tính khác nhau bằng cách chọn hợp lý các tham số này. Sau khi đáp ứng được biểu "
        "diễn dưới dạng 17.7 và 17.8, có thể phân tích tiếp trong miền thời gian hoặc miền tần số. Đáp ứng thời "
        "gian của hệ bậc hai điển hình với đầu vào bậc thang đơn vị cho ở Hình 17.4. Đồ thị Bode của đáp ứng biên "
        "độ và pha trình bày ở Hình 17.5."))
    b.append(fig(4, F.fig(4)))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Hệ mà một kết cấu đơn chuyển động theo nhiều hướng gọi là hệ nhiều bậc tự do (multi-degree-of-freedom). "
        "Khi đó gia tốc trở thành hàm của các chiều: d²x/dt², d²y/dt² và d²z/dt². Vì thế, trong thử rung động đa "
        "kênh, phải dùng nhiều cảm biến để tạo các điểm đo một trục, hai trục hay ba trục. Toán học, một hệ tuyến "
        "tính nhiều bậc tự do mô tả bằng một tập hợp các phương trình vi phân bậc hai ghép nhau; khi vẽ đáp ứng "
        "tần số, nó thường cho một đỉnh cộng hưởng trên mỗi bậc tự do."))
    b.append(p(
        "Thường phải đo gia tốc và rung động của những tấm mỏng hay khối lượng nhỏ. Gắn một gia tốc kế có khối "
        "lượng tương đương lên tấm mỏng hay mẫu thử nhỏ có thể gây “tải khối lượng” (mass loading). Bởi gia tốc "
        "phụ thuộc vào khối lượng, đặc tính rung động của mẫu bị tải có thể bị thay đổi, dẫn đến đo sai. Trong "
        "những trường hợp đó, phải diễn giải đúng kết quả thiết bị đo. Một số kỹ thuật thực nghiệm cũng có sẵn để "
        "hiệu chỉnh kết quả thử bằng cách tiến hành lặp lại các phép thử với việc lần lượt thêm các khối lượng nhỏ "
        "đã biết và quan sát sự khác biệt."))

    # ---- 17.2
    b.append(h2("17.2 Gia tốc kế điện – cơ cân bằng lực (servo)",
                "Electromechanical Force-Balance (Servo) Accelerometers"))
    b.append(p(
        "Gia tốc kế điện – cơ, thực chất là loại servo hay triệt tiêu sai lệch (null-balance), dựa trên nguyên lý "
        "phản hồi. Trong các thiết bị này, khối lượng nhạy gia tốc được giữ rất sát vị trí trung hoà hay điểm dịch "
        "chuyển không bằng cách cảm nhận dịch chuyển và phản hồi lại dịch chuyển đó. Một lực từ tỉ lệ thuận được "
        "sinh ra để chống lại chuyển động của khối lệch khỏi vị trí trung hoà, nhờ đó khôi phục vị trí trung hoà — "
        "cũng như một lò xo cơ trong gia tốc kế thông thường. Ưu điểm của cách này là tính tuyến tính tốt hơn và "
        "loại bỏ hiệu ứng trễ (hysteresis) so với lò xo cơ. Ngoài ra, trong một số trường hợp có thể cung cấp giảm "
        "chấn điện, vốn ít nhạy với biến thiên nhiệt độ hơn."))
    b.append(p(
        "Một đặc điểm rất quan trọng của loại triệt tiêu sai lệch là khả năng thử nghiệm đặc tính tĩnh và động của "
        "thiết bị bằng cách đưa các lực thử kích thích bằng điện vào hệ. Tính năng tự kiểm tra từ xa này rất tiện "
        "trong những thử nghiệm phức tạp và đắt đỏ, nơi cực kỳ quan trọng là hệ phải hoạt động đúng trước khi thử "
        "bắt đầu. Chúng cũng hữu ích trong các hệ điều khiển gia tốc, vì giá trị gia tốc tham chiếu có thể đưa vào "
        "bằng một dòng tỉ lệ từ nguồn ngoài. Chúng thường dùng cho đo chuyển động nói chung và giám sát rung động "
        "tần số thấp. Chúng được áp dụng cụ thể cho những phép đo đòi hỏi độ chính xác cao hơn các gia tốc kế dùng "
        "lò xo cơ làm bộ chuyển đổi lực–dịch chuyển."))
    b.append(p(
        "Có một số loại gia tốc kế điện – cơ khác nhau: loại cuộn-dây–nam-châm, loại cảm ứng…"))
    b.append(h3("Gia tốc kế loại cuộn dây – nam châm", "Coil-and-Magnetic Type Accelerometers"))
    b.append(p(
        "Các gia tốc kế này dựa trên định luật Ampère: “một dây dẫn mang dòng đặt trong từ trường chịu một lực tỉ "
        "lệ với dòng, chiều dài dây dẫn trong từ trường, mật độ từ trường và sin của góc giữa dây dẫn và từ "
        "trường.” Hình 17.6 minh hoạ một dạng gia tốc kế dùng nguyên lý trên. Cuộn dây nằm trong khe hình trụ giới "
        "hạn bởi nam châm vĩnh cửu và đường trở từ mềm bằng sắt. Nó được đỡ bởi một cánh tay trên một ổ bi ma sát "
        "tối thiểu để tạo thành khối lượng địa chấn nhạy gia tốc. Một cơ cấu pick-off cảm nhận dịch chuyển của "
        "cuộn dây dưới tác dụng gia tốc và làm cho cuộn dây được cấp một dòng một chiều qua bộ điều khiển servo "
        "thích hợp để khôi phục hay duy trì điều kiện triệt tiêu (null)."))
    b.append(fig(6, F.fig(6)))
    b.append(p(
        "Giả sử gia tốc hướng xuống với từ trường hướng kính (90°) và dùng định luật Ampère, lực tác động lên "
        "cuộn dây viết được:"))
    b.append(eq("F = m a = i l B", "17.9"))
    b.append(p("hay dòng điện:"))
    b.append(eq("i = m a / (l B)", "17.10"))
    b.append(p(
        "với B = mật độ từ thông hiệu dụng, l = tổng chiều dài hiệu dụng của dây dẫn trong từ trường. Dòng trong "
        "mạch khôi phục tỉ lệ thẳng với gia tốc, với điều kiện: (1) hiệu ứng phản ứng phần ứng (armature reaction) "
        "không đáng kể và được bù trừ hoàn toàn bởi cuộn bù đối nghịch với cuộn chuyển động, và (2) độ lợi của hệ "
        "servo đủ lớn để ngăn cuộn dây dịch khỏi vùng từ trường không đổi."))
    b.append(p(
        "Trong các gia tốc kế này, kết cấu từ phải được che chắn đầy đủ để hệ không nhạy với nhiễu ngoài hay từ "
        "trường Trái Đất. Cũng vậy, khi có gia tốc, sẽ có sự tăng nhiệt do tổn hao i²R. Ảnh hưởng của các tổn hao "
        "i²R lên đặc tính được xác định bởi thiết kế nhiệt và tính truyền nhiệt của gia tốc kế. Trong nhiều ứng "
        "dụng, phải đặc biệt cẩn thận chọn gia tốc kế thích hợp sao cho sự tăng nhiệt do những gia tốc bất ngờ "
        "không ảnh hưởng quá mức đến hệ số tỉ lệ (scale factor) hay điều kiện độ lệch (bias)."))
    b.append(h3("Gia tốc kế loại servo quay đơn giản", "A Simplified Rotational Servo"))
    b.append(p(
        "Một bản đơn giản hoá của một gia tốc kế servo loại quay cho ở Hình 17.7. Gia tốc a của vỏ thiết bị gây "
        "một lực quán tính F lên khối lượng nhạy m, có xu hướng làm nó xoay trên ổ hay giá đàn hồi (flexure). Góc "
        "xoay θ từ vị trí trung hoà được cảm biến bằng pick-off cảm ứng và được khuếch đại, tách sóng điều biến "
        "(demodulate) và lọc để sinh một dòng iₐ tỉ lệ trực tiếp với chuyển động lệch khỏi null. Dòng này chạy "
        "qua một điện trở ổn định chính xác R để sinh tín hiệu điện áp ra và được áp vào một cuộn dây treo trong "
        "từ trường. Dòng qua cuộn dây sinh mômen từ lên cuộn, có tác dụng đưa khối lượng trở về trung hoà. Dòng "
        "cần để sinh mômen từ vừa khớp mômen quán tính do gia tốc tỉ lệ trực tiếp với gia tốc a. Do đó, điện áp ra "
        "e₀ trở thành thước đo gia tốc a. Vì một dịch chuyển θ khác không là cần thiết để sinh dòng iₐ, khối lượng "
        "không được trả về null hoàn toàn, nhưng rất gần không do bộ khuếch đại độ lợi cao. Phân tích sơ đồ khối "
        "cho thấy:"))
    b.append(eq("e₀ / eₐ = (K_p K_c R / K_s) · (Kₐ s²) / (s² + 2 ζ ωₙₗ s + ωₙₗ²)", "17.11"))
    b.append(p("sắp xếp lại:"))
    b.append(eq("a = (K_s / (K_p K_c Kₐ R)) · (s² + 2 ζ ωₙₗ s + ωₙₗ²) / (ωₙₗ²) · e₀", "17.12"))
    b.append(p(
        "Bằng cách thiết kế độ lợi bộ khuếch đại, Kₐ làm đủ lớn sao cho K_c K_p Kₐ a / K_s ≫ 1,0; khi đó:"))
    b.append(eq("a ≈ (K_s / (K_p K_c Kₐ R)) · (1 / ωₙₗ²) · e₀  =  (1 / (Kₘ R)) · e₀", "17.13"))
    b.append(p(
        "với Kₘ = K_p K_c Kₐ / (K_s ωₙₗ²). Phương trình 17.14 (tức 17.13) cho thấy độ nhạy phụ thuộc vào m, r, R "
        "và K_c, tất cả đều có thể làm hằng định. Ở đây, phản hồi độ lợi cao rất có ích để chuyển yêu cầu về độ "
        "chính xác và ổn định từ các linh kiện cơ sang một số ít tham số đã chọn thoả mãn dễ dàng. Như mọi hệ "
        "phản hồi, độ lợi không thể tuỳ ý cao vì bất ổn động lực; tuy nhiên có thể đạt độ lợi đủ cao để có đặc "
        "tính tốt. Tài liệu tham khảo [3] (Doebelin, 1990) trình bày rất đầy đủ chủ đề này."))
    b.append(fig(7, F.fig(7)))
    b.append(h3("Gia tốc kế loại cảm ứng", "Induction Type Accelerometers"))
    b.append(p(
        "Quan hệ tích có hướng (cross-product) của dòng, từ trường và lực tạo cơ sở cho các gia tốc kế điện từ "
        "cảm ứng, vốn thực chất là máy phát chứ không phải động cơ. Một loại thiết bị, cốc-và-nam-châm (cup-and-"
        "magnet), gồm một phần tử con lắc (pendulous) với pick-off và bộ điều khiển servo dẫn động một khớp nối "
        "tachometer và một nam châm vĩnh cửu cùng vành trở từ, đặt sát với một xi lanh dẫn điện gắn vào phần tử "
        "con lắc. Một lực cản tỉ lệ tốc độ thu được nhờ hiệu ứng cảm ứng điện từ giữa nam châm và vật dẫn. Pick-off "
        "cảm nhận độ lệch con lắc dưới gia tốc và làm cho bộ điều khiển servo quay rôto theo hướng kéo phần tử "
        "con lắc về null. Ở trạng thái xác lập, tốc độ động cơ là thước đo gia tốc tác động lên thiết bị. Vận "
        "hành servo ổn định đạt được nhờ một mạng dẫn đầu thời gian (time-lead network) để bù trễ quán tính của "
        "tổ hợp động cơ–nam châm. Độ chính xác của loại servo gia tốc kế cuối cùng bị giới hạn bởi tính nhất quán "
        "và ổn định của hệ số tỉ lệ của thiết bị ghép nối và cặp nam-châm–cốc theo thời gian và nhiệt độ."))
    b.append(p(
        "Một gia tốc kế khác dựa trên loại cảm ứng là sinh mômen cảm ứng dòng điện xoáy (eddy current). Cơ cấu sinh "
        "lực của gia tốc kế cảm ứng gồm một từ trường ổn định, thường do nam châm vĩnh cửu cung cấp, xuyên vuông "
        "góc qua một tấm dẫn đều. Chuyển động của tấm dẫn tương đối với từ trường đáp ứng gia tốc sinh ra một "
        "suất điện động trong mỗi mạch của vật dẫn, theo định luật Faraday. Trong loại cảm ứng, các dòng điện xoáy "
        "bị giam trong tấm dẫn, làm hệ thực chất là một khớp nối cản (drag coupling)."))
    b.append(p(
        "Một thiết bị thương mại điển hình dựa trên nguyên lý servo gia tốc kế có thể có giá treo flexure thạch "
        "anh vi gia công, pick-off góc điện dung vi sai, màng khí ép (air squeeze film) cộng với bù servo cho "
        "giảm chấn hệ. Trong các model có mặt, một đơn vị dải 30 g có ngưỡng và độ phân giải 1 µg, đáp ứng tần số "
        "phẳng trong 0,05% ở 10 Hz và 2% ở 100 Hz, tần số tự nhiên 500 Hz, tỉ số giảm chấn 0,3 đến 0,8, và độ "
        "nhạy trục ngang (cross-axis) 0,1%. Ví dụ, nếu dòng ra khoảng 1,3 mA/g và một điện trở đọc 250 Ω cho "
        "khoảng ±10 V toàn thang ở 30 g. Các gia tốc kế này tốt về độ chính xác, dùng trong nhiều ứng dụng như "
        "hệ điều khiển máy bay và tên lửa, đo góc nghiêng, uốn trục bánh xe trong hệ cân bằng…"))

    # ---- 17.3
    b.append(h2("17.3 Gia tốc kế áp điện", "Piezoelectric Accelerometers"))
    b.append(p(
        "Gia tốc kế áp điện được dùng rộng rãi cho đo gia tốc, xung kích và rung động nói chung. Chúng cơ bản là "
        "bộ chuyển đổi chuyển động với tín hiệu ra lớn và kích thước khá nhỏ. Chúng có tần số tự nhiên rất cao "
        "nên thích hợp cho ứng dụng tần số cao và đo xung kích. Các thiết bị này dùng một khối lượng tiếp xúc "
        "trực tiếp với phần tử áp điện (hay tinh thể), như Hình 17.8. Khi một chuyển động biến thiên tác động, "
        "tinh thể chịu một kích thích lực biến thiên (F = ma), sinh ra một điện tích q tỉ lệ xuất hiện trên nó."))
    b.append(fig(8, F.fig(8)))
    b.append(eq("q = dᵢⱼ F = dᵢⱼ m a", "17.17"))
    b.append(p(
        "với q = điện tích sinh ra, dᵢⱼ = hệ số áp điện của vật liệu. Như phương trình 17.17, đầu ra từ vật liệu "
        "áp điện phụ thuộc vào tính chất cơ học dᵢⱼ của nó. Hai tinh thể áp điện thường dùng là gốm chì-zirconat "
        "titanat (PZT) và thạch anh. Cả hai đều là vật liệu tự sinh (self-generating) và sinh điện tích lớn so "
        "với kích thước. Hằng số biến dạng áp điện của PZT gấp khoảng 150 lần thạch anh. Kết quả, PZT nhạy hơn "
        "và nhỏ hơn thạch anh. Trong gia tốc kế, hằng số lò xo cơ cho các phần tử áp điện cao, và khối lượng quán "
        "tính gắn vào chúng nhỏ. Vì thế chúng hữu dụng cho tần số cao. Hình 17.9 minh hoạ đáp ứng tần số điển "
        "hình của thiết bị PZT. Vì gia tốc kế áp điện có trở kháng cơ thấp, ảnh hưởng của chúng lên chuyển động "
        "đa số kết cấu là không đáng kể. Chúng cũng được chế tạo bền chắc và đầu ra ổn định theo thời gian và môi "
        "trường."))
    b.append(fig(9, F.fig(9)))
    b.append(p(
        "Toán học, hàm truyền của chúng xấp xỉ một hệ bậc ba:"))
    b.append(eq("e₀(s)/a(s) = K_q (s² + 2 ζ ωₙ s + ωₙ²) / ((τ s + 1)(s² + 2 ζ ωₙ s + ωₙ²))", "17.18"))
    b.append(p(
        "với K_q = hằng số áp điện liên quan đến điện tích (C·cm), τ = hằng số thời gian của tinh thể. Đáng lưu "
        "ý là bản thân tinh thể không có hằng số thời gian τ, nhưng hằng số thời gian này quan sát được khi gia "
        "tốc kế được nối vào một mạch điện (ví dụ mạch RC). Đáp ứng tần số thấp bị giới hạn bởi đặc tính áp điện "
        "τs/(τs+1), còn đáp ứng tần số cao liên quan đến đáp ứng cơ học. Hệ số giảm chấn ζ rất nhỏ, thường dưới "
        "0,01 hay gần không. Đáp ứng tần số thấp chính xác đòi hỏi τ lớn, thường đạt bằng cách dùng bộ khuếch "
        "đại điện áp trở kháng cao. Ở tần số rất thấp, hiệu ứng nhiệt có thể ảnh hưởng mạnh đến đặc tính vận hành."))
    b.append(p(
        "Trong gia tốc kế áp điện, có hai cấu hình thiết kế cơ bản: loại nén (compression) và loại ứng suất cắt "
        "(shear stress). Ở loại nén, tinh thể được giữ bằng một phần tử tiền tải (preload) nên rung động làm biến "
        "thiên ứng suất theo chế độ nén. Ở loại cắt, rung động đơn giản làm biến dạng tinh thể theo chế độ cắt. "
        "Loại nén có tỉ lệ khối-lượng/độ-nhạy khá tốt và do đó thể hiện đặc tính tốt hơn. Nhưng, vì vỏ đóng vai "
        "trò bộ phận nguyên khối của hệ lò xo–khối, nó có thể sinh ra những giao tiếp giả (spurious interfaces) "
        "trong đầu ra nếu bị kích ở tần số tự nhiên riêng. Mạch vi điện tử cho phép thiết kế gia tốc kế áp điện "
        "tích hợp bộ khuếch đại điện tích và các mạch điều kiện tín hiệu khác vào trong vỏ thiết bị. Cách bố trí "
        "này cho phép gia tốc kế nhạy hơn, đáp ứng tần số cao hơn và nhỏ hơn, nhờ đó hạ chi phí ban đầu và thực "
        "hiện."))
    b.append(p(
        "Gia tốc kế áp điện có mặt với dải thông số rất rộng và do nhiều hãng sản xuất. Ví dụ, thông số của một "
        "gia tốc kế xung kích có thể có 0,004 pC/g về độ nhạy và tần số tự nhiên tới 250.000 Hz, trong khi một "
        "đơn vị thiết kế cho đo địa chấn mức thấp có 1000 pC/g về độ nhạy và chỉ 7000 Hz tần số tự nhiên. Chúng "
        "được chế tạo nhỏ đến 3 × 3 mm với khối lượng khoảng 0,5 g cả cáp. Chúng có dải nhiệt độ tuyệt vời, một "
        "số được thiết kế sống sót trong môi trường bức xạ mạnh của lò phản ứng hạt nhân. Tuy nhiên, gia tốc kế "
        "áp điện có xu hướng độ nhạy trục ngang lớn hơn các loại khác; khoảng 2% đến 4%. Trong một số trường "
        "hợp, độ nhạy trục ngang lớn có thể dùng khi lắp đặt để định hướng đúng thiết bị. Các gia tốc kế này có "
        "thể gắn bằng chốt ren, bằng xi măng hay sáp dán, hoặc bằng nam châm."))

    # ---- 17.4
    b.append(h2("17.4 Gia tốc kế áp điện trở", "Piezoresistive Accelerometers"))
    b.append(p(
        "Gia tốc kế áp điện trở thực chất là các điện trở strain gage bán dẫn với hệ số gage lớn. Hệ số gage cao "
        "thu được vì điện trở suất vật liệu phụ thuộc chủ yếu vào ứng suất chứ không chỉ vào kích thước. Độ nhạy "
        "tăng là then chốt trong đo rung động vì nó cho phép thu nhỏ gia tốc kế. Đa số gia tốc kế áp điện trở "
        "dùng hai hoặc bốn gage chủ động bố trí trong một cầu Wheatstone. Các điện trở chính xác phụ được dùng "
        "như một phần của mạch, mắc nối tiếp với đầu vào để điều khiển độ nhạy, cân bằng và bù trừ hiệu ứng "
        "nhiệt độ. Cấu tạo cơ khí của một gia tốc kế áp điện trở cho ở Hình 17.10."))
    b.append(fig(10, F.fig(10)))
    b.append(p(
        "Trong một số ứng dụng, cần có các chặn quá tải (overload stops) để bảo vệ gage khỏi các tín hiệu biên "
        "độ lớn. Các thiết bị này hữu dụng để thu thông tin rung động ở tần số thấp (ví dụ dưới 1 Hz). Thực tế, "
        "cảm biến áp điện trở là những thiết bị đo gia tốc tĩnh thực sự. Đặc tính điển hình có thể là 100 mV/g về "
        "độ nhạy, 0 đến 750 Hz về dải tần, 2500 Hz tần số cộng hưởng, 25 g dải biên độ, 2000 g định mức xung "
        "kích, 0 đến 95°C dải nhiệt độ, tổng khối lượng khoảng 25 g."))

    # ---- 17.5
    b.append(h2("17.5 Gia tốc kế điện dung vi sai", "Differential-Capacitance Accelerometers"))
    b.append(p(
        "Gia tốc kế điện dung vi sai dựa trên nguyên lý điện dung thay đổi tỉ lệ với gia tốc tác dụng. Chúng có "
        "nhiều hình dạng và kích thước khác nhau. Trong một loại, khối lượng địa chấn của gia tốc kế làm phần tử "
        "di động của một dao động điện, như Hình 17.11. Khối lượng địa chấn được đỡ bởi một cụm dầm song song "
        "đàn hồi từ đế. Hệ được đặc trưng có một tần số danh định xác định khi không bị xáo trộn. Nếu thiết bị "
        "bị gia tốc, tần số biến thiên trên và dưới giá trị danh định tuỳ theo hướng gia tốc."))
    b.append(fig(11, F.fig(11)))
    b.append(p(
        "Khối lượng địa chấn mang một điện cực đặt đối diện với một số điện cực cố định trên đế, tạo nên các tụ "
        "điện biến thiên. Các điện cực cố định được ghép điện trở trong đường phản hồi của một bộ khuếch đại đảo "
        "(phase-inverting) băng rộng. Độ lợi bộ khuếch đại được chọn sao cho duy trì dao động trong dải biến thiên "
        "điện dung do gia tốc tác dụng. Giá trị điện dung C của mỗi tụ biến thiên cho bởi:"))
    b.append(eq("C = k ε S / h", "17.19"))
    b.append(p(
        "với k = hằng số điện môi, ε = điện dung của chân không, S = diện tích điện cực, h = khe hở biến thiên. "
        "Gọi độ lớn khe hở tại gia tốc không là h₀, giá trị h khi có gia tốc a viết được:"))
    b.append(eq("h = h₀ + m a / K", "17.20"))
    b.append(p("với m = khối lượng thử và K là hằng số lò xo. Suy ra:"))
    b.append(eq("C = k ε S / (h₀ + m a / K)", "17.21"))
    b.append(p("Nếu tần số dao động của mạch kiểu điện trở–điện dung cho bởi:"))
    b.append(eq("f = 1 / (2π R C)", "17.22"))
    b.append(p("thế C vào 17.21 được:"))
    b.append(eq("f = (1 / (2π R k ε S)) · (h₀ + m a / K)", "17.23"))
    b.append(p("gọi lượng không đổi (1/(2π R k ε S)) là B và viết lại:"))
    b.append(eq("f = B h₀ + (B m a) / K", "17.24"))
    b.append(p(
        "Số hạng đầu vế phải biểu thị tần số thiên lệch (bias) cố định f₀, số hạng thứ hai là sự thay đổi tần số "
        "do gia tốc, sao cho biểu thức viết thành:"))
    b.append(eq("f = f₀ + fₐ", "17.25"))
    b.append(p(
        "Nếu tần số ra được so với một nguồn tần số không đổi độc lập f₀, có thể xác định fₐ."))
    b.append(p(
        "Một ví dụ thường dùng của gia tốc kế loại điện dung dựa trên một màng mỏng có các flexure xoắn ốc tạo "
        "lò xo, khối lượng thử và bản chuyển động cần thiết cho tụ vi sai, như Hình 17.12. Chuyển động của bản "
        "giữa các điện cực bơm khí song song với bề mặt bản và qua các lỗ trên bản để cung cấp giảm chấn màng "
        "ép (squeeze film). Vì độ nhớt khí ít nhạy nhiệt độ hơn dầu, tỉ số giảm chấn mong muốn 0,7 hầu như không "
        "đổi quá 15%. Một họ các thiết bị như vậy sẵn có, với dải toàn thang từ ±0,2 g (đáp ứng phẳng 4 Hz) đến "
        "±1000 g (3000 Hz), độ nhạy trục ngang dưới 1%, và đầu ra toàn thang ±1,5 V. Kích thước thiết bị điển "
        "hình khoảng 25 mm³ với khối lượng 50 g."))
    b.append(fig(12, F.fig(12)))

    # ---- 17.6
    b.append(h2("17.6 Gia tốc kế điện trở strain gage", "Strain-Gage Accelerometers"))
    b.append(p(
        "Gia tốc kế strain gage dựa trên tính chất điện trở của vật dẫn. Nếu một vật dẫn bị kéo hay nén, điện trở "
        "nó thay đổi vì hai lý do: thay đổi kích thước và thay đổi tính chất cơ bản của vật liệu gọi là áp điện "
        "trở (piezoresistance). Điều này chỉ ra rằng điện trở suất ρ của vật dẫn phụ thuộc vào ứng suất cơ học "
        "tác dụng lên nó. Sự phụ thuộc biểu thị qua hệ số gage:"))
    b.append(eq("ΔR/R = ΔL/L + 2ν(ΔL/L) + (dρ/ρ)/(dL/L)", "17.26"))
    b.append(p(
        "với 1 = thay đổi điện trở do chiều dài, 2ν = thay đổi điện trở do tiết diện, (dρ/ρ)/(dL/L) = thay đổi "
        "điện trở do áp điện trở. Trong đo gia tốc, có thể chọn điện trở strain gage từ các loại khác nhau gồm "
        "gage dây kim loại không dán, gage dây kim loại dán, gage lá kim loại dán, gage màng kim loại mỏng bay "
        "hơi, gage bán dẫn dán, gage bán dẫn khuếch tán… Nhưng thường gage dây kim loại dán và không dán tìm "
        "ứng dụng rộng hơn trong gia tốc kế. Thỉnh thoảng dùng gage bán dẫn dán, gọi là cảm biến áp điện trở, "
        "nhưng chịu độ nhạy nhiệt độ cao, phi tuyến và một số khó khăn lắp đặt. Dù vậy, những năm gần đây chúng "
        "tìm được lĩnh vực ứng dụng mới cùng sự phát triển công nghệ vi cơ (micromachine transducer)."))
    b.append(p(
        "Gia tốc kế strain gage không dán dùng dây strain làm cảm biến lò xo và cảm biến chuyển động, dùng bố "
        "trí tương tự Hình 17.10. Chúng hữu dụng cho đo chuyển động và rung động nói chung từ tần số thấp đến "
        "trung bình. Chúng có dải và đặc tính rộng, điển hình ±5 g đến ±200 g toàn thang, tần số tự nhiên 17 Hz "
        "đến 800 Hz, điện áp kích 10 V xoay chiều hoặc một chiều, đầu ra toàn thang ±20 mV đến ±50 mV, độ phân "
        "giải dưới 0,1%, sai số dưới 1% toàn thang, và độ nhạy trục ngang dưới 2%. Tỉ số giảm chấn (dùng dầu "
        "silicone) là 0,6 đến 0,8 ở nhiệt độ phòng. Các thiết bị này nhỏ và nhẹ, thường khối lượng dưới 25 g."))
    b.append(p(
        "Gia tốc kế strain gage dán thường dùng một khối lượng đỡ bởi một dầm flexure mỏng. Các strain gage được "
        "dán lên dầm để đạt độ nhạy tối đa, bù nhiệt độ và nhạy với cả gia tốc trục ngang lẫn góc. Đặc tính của "
        "chúng tương tự gia tốc kế strain gage không dán nhưng có kích thước và khối lượng lớn hơn. Thường dùng "
        "dầu silicone để giảm chấn. Strain gage bán dẫn được dùng rộng rãi làm cảm biến strain trong gia tốc kế "
        "loại dầm-cantilever/khối-lượng. Chúng cho đầu ra cao (0,2 V đến 0,5 V toàn thang). Điển hình, một đơn "
        "vị gia tốc ±25 g có đáp ứng phẳng từ 0 Hz đến 750 Hz, tỉ số giảm chấn 0,7, khối lượng 28 g, nhiệt độ "
        "vận hành –18°C đến +93°C. Một model ba trục ±20.000 g có đáp ứng phẳng từ 0 kHz đến 15 kHz, tỉ số giảm "
        "chấn 0,01, dải bù nhiệt 0°C đến 45°C, kích thước 13 × 10 × 13 mm và khối lượng 10 g."))

    # ---- 17.7
    b.append(h2("17.7 Gia tốc kế địa chấn", "Seismic Accelerometers"))
    b.append(p(
        "Các gia tốc kế này dùng một khối lượng địa chấn treo bằng lò xo hay đòn bẩy trong một khung cứng. Sơ "
        "đồ nguyên lý của một thiết bị điển hình ở Hình 17.1. Khung mang khối lượng địa chấn được gắn chắc vào "
        "nguồn rung động cần đo. Khi hệ rung, khối lượng có xu hướng giữ nguyên vị trí để chuyển động được ghi "
        "nhận như dịch chuyển tương đối giữa khối và khung. Dịch chuyển này được cảm nhận bởi một bộ chuyển đổi "
        "thích hợp và tín hiệu ra được xử lý tiếp. Dù vậy, khối lượng địa chấn không đứng yên tuyệt đối; nhưng "
        "với những tần số đã chọn, nó có thể đóng vai trò vị trí tham chiếu một cách thoả đáng."))
    b.append(p(
        "Bằng cách chọn hợp lý tổ hợp khối lượng, lò xo và giảm chấn, thiết bị địa chấn có thể dùng cho đo gia "
        "tốc hoặc dịch chuyển. Nhìn chung, khối lượng lớn và lò xo mềm thích hợp cho đo rung động và dịch chuyển, "
        "trong khi khối lượng tương đối nhỏ và lò xo cứng dùng trong gia tốc kế. Phương trình sau viết bằng định "
        "luật II Newton mô tả đáp ứng của cụm địa chấn như Hình 17.1:"))
    b.append(eq("m ẍ₂ + c ẋ₂ + k x₂ = m g cosθ + m ẍ₁", "17.27"))
    b.append(p(
        "với x₁ = dịch chuyển khung rung, x₂ = dịch chuyển khối địa chấn, c = hằng số vận tốc, k = hằng số lò "
        "xo. Lấy m ẍ₁ từ hai vế và sắp xếp lại được:"))
    b.append(eq("m z̈ + c ż + k z = m g cosθ − m ẍ₁", "17.28"))
    b.append(p(
        "với z = x₂ − x₁ là chuyển động tương đối giữa khối và đế, θ = góc giữa trục cảm biến và trọng trường. "
        "Trong 17.27, giả sử lực giảm chấn trên khối lượng địa chấn chỉ tỉ lệ với vận tốc. Nếu một chuyển động "
        "dao động điều hoà tác dụng lên thiết bị sao cho:"))
    b.append(eq("x₁(t) = x₁₀ sin(ω₁ t)", "17.29"))
    b.append(p("viết a₁ = m x₁₀ ω₁² biến đổi 17.28 thành:"))
    b.append(eq("m z̈ + c ż + k z = m g cosθ + m a₁ sin(ω₁ t)", "17.30"))
    b.append(p(
        "Phương trình 17.30 có nghiệm quá độ và xác lập. Nghiệm xác lập của phương trình vi phân 17.30 xác định "
        "được, và sắp xếp lại thành:"))
    b.append(eq("z = (m g / k) cosθ + (m a₁ / k) · sin(ω₁ t − φ) / √((1 − r²)² + (2 ζ r)²)", "17.31"))
    b.append(p("với:"))
    b.append(eq("r = ω₁ / ωₙ ,  φ = tan⁻¹(2 ζ r / (1 − r²)) ,  ωₙ = √(k/m) ,  ζ = c / (2√(km))", "17.32"))
    b.append(p(
        "Đồ thị phương trình 17.32, (x₁ − x₂)₀/x₀ theo tỉ số tần số ω₁/ωₙ, minh hoạ ở Hình 17.13. Hình này cho "
        "thấy biên độ ra bằng biên độ vào khi c/c_c = 0,7 và ω₁/ωₙ > 2. Đầu ra trở thành hàm tuyến tính thực sự "
        "của đầu vào ở những tỉ số tần số cao. Để đặc tính hệ thoả đáng, hằng số thiết bị c/c_c và ωₙ phải được "
        "tính toán cẩn thận hoặc lấy từ hiệu chuẩn. Như vậy có thể dự đoán độ chính xác đo期待 cho các tần số "
        "quan tâm. Tài liệu [1] (McConnell) trình bày đầy đủ phân tích này."))
    b.append(fig(13, F.fig(13)))
    b.append(p(
        "Nếu thiết bị địa chấn có tần số tự nhiên thấp và dùng cảm biến dịch chuyển đo chuyển động tương đối z, "
        "thì đầu ra tỉ lệ với dịch chuyển của vỏ thiết bị. Nếu dùng cảm biến vận tốc đo chuyển động tương đối, "
        "tín hiệu tỉ lệ với vận tốc của thiết bị. Điều này đúng với tần số cao hơn đáng kể tần số tự nhiên của "
        "thiết bị. Ngược lại, nếu thiết bị có tần số tự nhiên cao và dùng cảm biến dịch chuyển, đầu ra đo được tỉ "
        "lệ với gia tốc:"))
    b.append(eq("k z = m ẍ₁", "17.33"))
    b.append(p(
        "Phương trình này đúng vì dịch chuyển x₂ trở nên không đáng kể so với x₁. Trong các thiết bị này, gia tốc "
        "vào a₀ có thể tính đơn giản bằng cách đo (x₁ − x₂)₀. Nhìn chung, trong đo gia tốc, người ta thấy đặc "
        "tính không thoả mãn ở tỉ số tần số trên 0,4. Vì thế, trong những ứng dụng đó, tần số gia tốc phải giữ "
        "thấp hơn hẳn tần số tự nhiên của thiết bị. Điều này thực hiện bằng cách chế tạo thiết bị có tần số tự "
        "nhiên thấp qua chọn lò xo mềm và khối lượng lớn."))
    b.append(p(
        "Thiết bị địa chấn được chế tạo theo nhiều cách. Hình 17.14 minh hoạ dùng một biến trở con chạy (poten-"
        "tiometer) để cảm nhận dịch chuyển tương đối giữa khung và khối địa chấn. Ở đa số thiết bịbiến trở, thiết "
        "bị được đổ đầy chất lỏng nhớt tương tác liên tục với khung và khối địa chấn để giảm chấn. Các gia tốc "
        "kế này có tần số vận hành thấp (dưới 100 Hz) và chủ yếu dùng cho gia tốc biến thiên chậm và rung động "
        "tần số thấp. Một họ thiết bị điển hình có nhiều model, bao phủ dải ±1 g đến ±50 g toàn thang. Tần số tự "
        "nhiên từ 12 Hz đến 89 Hz, và tỉ số giảm chấn ζ giữ được giữa 0,5 đến 0,8 dùng giảm chấn lỏng bù nhiệt. "
        "Điện trởbiến trở chọn trong dải 1000 Ω đến 10.000 Ω, với độ phân giải tương ứng 0,45% đến 0,25% toàn "
        "thang. Độ nhạy trục ngang dưới ±1%. Độ chính xác tổng thể ±1% toàn thang hoặc thấp hơn ở nhiệt độ "
        "phòng. Kích thước khoảng 50 mm³; khối lượng khoảng 1/2 kg."))
    b.append(fig(14, F.fig(14)))
    b.append(p(
        "Bộ biến áp vi sai lõi biến thiên (LVDT) cung cấp một cách tiện lợi khác để đo dịch chuyển tương đối "
        "giữa khối địa chấn và vỏ gia tốc kế. Các thiết bị này có tần số tự nhiên cao hơnbiến trở, tới 300 Hz. Vì "
        "LVDT có điện trở chuyển động thấp hơn, nó cho độ phân giải tốt hơn. Một họ thiết bị gia tốc kế biến áp "
        "vi sai giảm chấn lỏng điển hình có đặc tính: dải toàn thang từ ±2 g đến ±700 g, tần số tự nhiên 35 Hz "
        "đến 620 Hz, phi tuyến 1% toàn thang, đầu ra toàn thang khoảng 1 V với kích LVDT 10 V ở 2000 Hz, tỉ số "
        "giảm chấn 0,6 đến 0,7, điện áp dư tại null dưới 1%, và trễ (hysteresis) dưới 1% toàn thang; kích thước "
        "50 mm³, khối lượng khoảng 120 g."))
    b.append(p(
        "Điện trở strain gage cũng dùng cho cảm biến dịch chuyển của khối địa chấn như Hình 17.15. Ở đây, khối "
        "địa chấn được gắn trên một dầm cantilever thay vì lò xo. Các strain gage điện trở được dán hai bên dầm "
        "để cảm nhận biến dạng do dịch chuyển rung của khối. Giảm chấn hệ do một chất lỏng nhớt lấp đầy vỏ. Đầu "
        "ra của strain gage nối với một mạch cầu thích hợp. Tần số tự nhiên của hệ khoảng 300 Hz; tần số tự "
        "nhiên thấp do cần một dầm cantilever đủ lớn để gắn các strain gage. Các loại thiết bị địa chấn khác "
        "dùng cảm biến áp điện và khối địa chấn được bàn chi tiết trong phần dành riêng cho gia tốc kế áp "
        "điện."))
    b.append(fig(15, F.fig(15)))
    b.append(p(
        "Thiết bị rung động địa chấn bị ảnh hưởng nghiêm trọng bởi thay đổi nhiệt độ. Thiết bị dùng cảm biến dịch "
        "chuyển trở biến thiên sẽ cần các hệ số hiệu chỉnh cho sự thay đổi điện trở do nhiệt độ. Giảm chấn của "
        "thiết bị cũng có thể bị ảnh hưởng bởi sự thay đổi độ nhớt chất lỏng do nhiệt. Ví dụ, độ nhớt dầu "
        "silicone, thường dùng trong các thiết bị này, phụ thuộc mạnh vào nhiệt độ. Một cách loại bỏ ảnh hưởng "
        "nhiệt độ là dùng một điện trở gia nhiệt trong chất lỏng để duy trì nhiệt độ không đổi bất kể nhiệt độ "
        "xung quanh."))

    # ---- 17.8
    b.append(h2("17.8 Loại quán tính, dầm cantilever và cấu hình khối treo",
                "Inertial Types, Cantilever, and Suspended-Mass Configuration"))
    b.append(p(
        "Có một số gia tốc kế quán tính khác nhau, gồm con lắc quay (gyropendulum), rôto phản lực (reaction-"
        "rotor), dây rung (vibrating string) và cân bằng lực ly tâm (centrifugal-force-balance). Ở nhiều loại, "
        "lực cần để giữ khối lượng trong bối cảnh gia tốc được cung cấp bởi một hệ quán tính. Một thiết bị loại "
        "dây rung, Hình 17.16, dùng một khối thử được đỡ dọc trục bởi một cặp dây rung ngang có tiết diện đều, "
        "chiều dài và khối lượng bằng nhau. Tần số rung của dây được đặt ở vài nghìn chu kỳ/giây. Khối thử được "
        "đỡ theo hướng kính sao cho gia tốc vuông góc với dây không ảnh hưởng đến sức căng dây. Khi có gia tốc "
        "dọc trục cảm biến, một sức căng vi sai xuất hiện trên hai dây, làm thay đổi tần số rung. Từ định luật "
        "II Newton, các tần số viết được:"))
    b.append(eq("f₁ = (1 / 2 l) √(T₁ / mₛ) ,  f₂ = (1 / 2 l) √(T₂ / mₛ)", "17.34"))
    b.append(p(
        "với T là sức căng, mₛ và l là khối lượng và chiều dài dây. Lượng (T₁ − T₂) tỉ lệ với m a, với a là gia "
        "tốc dọc trục dây. Một biểu thức cho hiệu của các bình phương tần số:"))
    b.append(eq("f₁² − f₂² = (T₁ − T₂) / (4 l² mₛ) = (m a) / (4 l² mₛ)", "17.35"))
    b.append(p("suy ra:"))
    b.append(eq("f₁² − f₂² = (m a) / (4 [mₛ l²])", "17.36"))
    b.append(p(
        "Tổng các tần số (f₁ + f₂) có thể giữ không đổi bằng cách servo sức căng dây với tham chiếu tần số của "
        "một dao động chuẩn. Khi đó, hiệu các tần số trở nên tỉ lệ tuyến tính với gia tốc. Trong một số phiên "
        "bản, tính chất dạng dầm của các phần tử rung được dùng bằng cách kẹp chúng tại các nút (nodal points) "
        "tương ứng với mode rung cơ bản của dầm. Những phiên bản cải tiến dẫn đến gia tốc kế loại dầm "
        "cantilever như bàn sau."))
    b.append(fig(16, F.fig(16)))
    b.append(p(
        "Trong gia tốc kế loại dầm cantilever, một dầm nhỏ gắn trên khối được đặt áp mặt rung, và một cơ cấu "
        "thích hợp cho phép thay đổi chiều dài dầm. Chiều dài dầm được chỉnh sao cho tần số tự nhiên của nó bằng "
        "tần số mặt rung — từ đó có điều kiện cộng hưởng. Những biến thể nhỏ của bố trí dầm cantilever đang tìm "
        "ứng dụng mới trong vi gia tốc kế."))
    b.append(p(
        "Trong một loại cấu hình khối treo khác, người ta dùng một con lắc được gắn xoay quanh một trục thẳng "
        "đứng. Các pick-off được bố trí cho con lắc và tốc độ trục. Hệ được servo điều khiển để giữ ở vị trí "
        "null. Gia tốc trọng trường được cân bằng bởi gia tốc ly tâm. Tốc độ trục tỉ lệ với căn bậc hai của giá "
        "trị gia tốc cục bộ."))
    b.append(p(
        "Tất cả các gia tốc kế quán tính lực nói trên có đặc tính của những thiết bị tuyệt đối. Tức là, hệ số tỉ "
        "lệ của chúng có thể xác định trước chỉ bằng cách thiết lập khối lượng, chiều dài và thời gian, không "
        "phải điện áp, độ cứng lò xo…"))

    # ---- 17.9
    b.append(h2("17.9 Gia tốc kế phản hồi lực tĩnh điện", "Electrostatic Force Feedback Accelerometers"))
    b.append(p(
        "Gia tốc kế tĩnh điện dựa trên định luật Coulomb giữa hai điện cực mang điện. Chúng đo điện áp theo lực "
        "cần để duy trì một điện cực di động có diện tích, khối lượng và khoảng cách biết trước so với một điện "
        "cực cố định. Trường giữa các điện cực cho bởi:"))
    b.append(eq("E = Q / (k ε S)", "17.37"))
    b.append(p(
        "với E là cường độ hay gradient thế (dV/dx), Q điện tích, S diện tích vật dẫn, k hằng số điện môi của "
        "không gian ngoài vật dẫn. Dùng biểu thức này, có thể chỉ ra lực trên một đơn vị diện tích của vật dẫn "
        "mang điện (đơn vị N/m²):"))
    b.append(eq("F = S · Q² / (2 k ε S²) = k ε E² S / 2", "17.38"))
    b.append(p(
        "Trong một gia tốc kế loại phản hồi lực tĩnh điện (cấu trúc tương tự Hình 17.10), một điện cực khối "
        "lượng m và diện tích S được gắn trên một cánh tay đòn nhẹ để di chuyển tương đối với các điện cực cố "
        "định. Khoảng cách danh định h giữa điện cực đòn và cố định được duy trì bằng một hệ servo cân bằng lực "
        "có khả năng thay đổi thế điện cực đáp ứng tín hiệu từ pick-off cảm nhận sự thay đổi tương đối của "
        "khe."))
    b.append(p(
        "Xét một điện cực di động và một điện cực tĩnh, giả sử điện cực di động giữ ở thế thiên áp V₁ và điện cực "
        "tĩnh ở thế V₂, cường độ điện trường E trong khe biểu thị:"))
    b.append(eq("E = (V₁ − V₂) / h", "17.39"))
    b.append(p("nên lực hút tìm được:"))
    b.append(eq("F = k ε S (V₁ − V₂)² / (2 h²)", "17.40"))
    b.append(p(
        "Khi có gia tốc, nếu V₂ được chỉnh để giữ điện cực di động ở vị trí null, biểu thức liên hệ gia tốc và "
        "thế điện:"))
    b.append(eq("a = F / m = k ε (V₁ − V₂)² / (2 m h²)", "17.41"))
    b.append(p(
        "Thiết bị mô tả đến đây chỉ đo gia tốc một hướng, và đầu ra có tính bậc hai (quadratic); tức là:"))
    b.append(eq("V₁ − V₂ = √D · √a", "17.42"))
    b.append(p(
        "với D = hằng số tỉ lệ. Đầu ra có thể tuyến tính hoá bằng nhiều cách; ví dụ, phương pháp bình phương "
        "phần tư (quarter-square). Nếu bộ điều khiển servo áp một thế –V₂ lên điện cực cố định kia, lực hút giữa "
        "điện cực này và điện cực di động trở thành:"))
    b.append(eq("a = F / m = k ε (V₁ + V₂)² / (2 m h²)", "17.43"))
    b.append(p(
        "và phương trình cân bằng lực của điện cực di động khi thiết bị chịu gia tốc hướng xuống a là:"))
    b.append(eq("m a = F − F' = (k ε S / (2 h² m)) · (V₁ + V₂)² − (k ε S / (2 h² m)) · (V₁ − V₂)²", "17.44"))
    b.append(p("suy ra:"))
    b.append(eq("a = (k ε S / (h² m)) · (4 V₁ V₂)", "17.45"))
    b.append(p(
        "Do đó, nếu thế thiên áp V₁ giữ không đổi và độ lợi vòng điều khiển đủ cao sao cho sự biến thiên khe "
        "không đáng kể, gia tốc trở thành hàm tuyến tính của điện áp ra V₂ từ bộ điều khiển. Khó khăn chính "
        "trong cơ giới hoá gia tốc kế lực tĩnh điện là cường độ điện trường tương đối cao cần để có lực thoả "
        "đáng. Cũng vậy, cần những ổ trục cực tốt. Giảm chấn có thể cung cấp bằng điện, hoặc bằng độ nhớt của "
        "khí quyển trong không gian liên điện cực nếu khe h đủ nhỏ. Ưu điểm chính của gia tốc kế tĩnh điện gồm "
        "đơn giản cơ khí cực độ, yêu cầu công suất thấp, không có nguồn gây sai số trễ (hysteresis) nội tại, "
        "hệ số nhiệt độ bằng không, và dễ che chắn khỏi nhiễu trường."))

    # ---- 17.10
    b.append(h2("17.10 Vi gia tốc kế (microaccelerometers)", "Microaccelerometers"))
    b.append(p(
        "Vào cuối thập niên 1970, người ta thấy rõ công nghệ xử lý vi mạch (IC) cơ bản phẳng có thể sửa đổi để "
        "chế tạo các kết cấu cơ – điện ba chiều, gọi là vi gia công (micromachining). Gia tốc kế và cảm biến áp "
        "suất là những cảm biến IC đầu tiên. Gia tốc kế đầu tiên phát triển năm 1979. Từ đó công nghệ tiến triển "
        "liên tục đến mức một dải rất đa dạng các gia tốc kế sẵn có. Đa số cảm biến dùng vi gia công khối "
        "(bulk micromachining) hơn là vi gia công bề mặt (surface micromachining). Trong vi gia công khối, các "
        "flexure, dầm cộng hưởng và mọi thành phần trọng yếu của gia tốc kế được làm từ khối silicon nguyên "
        "khối để khai thác đầy đủ tính chất cơ học của silicon đơn tinh thể. Với thiết kế và quy trình màng phù "
        "hợp, vi gia công khối cho một gia tốc kế cực kỳ ổn định và bền chắc."))
    b.append(p(
        "Sự ăn mòn chọn lọc nhiều lớp màng mỏng lắng đọng, hay vi gia công bề mặt, cho phép chế tạo các cấu "
        "trúc vi mô di động trên các bản silicon. Với vi gia công bề mặt, các lớp vật liệu kết cấu được đặt và "
        "tạo hình, như Hình 17.17. Các kết cấu này tạo bằng polysilicon và một vật liệu hy sinh (sacrificial) "
        "như silicon dioxide. Vật liệu hy sinh đóng vai trò lớp đệm trung gian và bị ăn mòn đi để tạo ra một "
        "kết cấu tự do (free-standing). Công nghệ gia công bề mặt cũng cho phép các kết cấu nhỏ hơn và phức tạp "
        "hơn được xây dựng nhiều lớp trên một đế đơn."))
    b.append(fig(17, F.fig(17)))
    b.append(p(
        "Nguyên lý vận hành của vi gia tốc kế rất tương tự gia tốc kế loại cân bằng lực điện dung hay loại dầm "
        "rung đã bàn. Tuy nhiên, kỹ thuật chế tạo có thể khác nhau tuỳ hãng. Nhìn chung, gia tốc kế dầm rung "
        "(vibrating beam) được ưu tiên vì đặc tính khe khí tốt hơn và đặc tính độ lệch (bias) cải thiện. Gia tốc "
        "kế dầm rung, còn gọi là bộ chuyển đổi lực cộng hưởng dầm, được làm sao cho một gia tốc dọc trục vào đặt "
        "dầm rung ở chế độ căng. Do đó tần số cộng hưởng của dầm rung tăng hoặc giảm theo gia tốc tác dụng. Một "
        "kết cấu dầm cơ khí ghép, còn gọi là nĩa tuning hai đầu (DETF — double-ended tuning fork), ở Hình "
        "17.18."))
    b.append(fig(18, F.fig(18)))
    b.append(p(
        "Trong DETF, một dao động điện áp điện dung ghép năng lượng vào hai dầm rung để giữ chúng dao động ở tần "
        "số cộng hưởng. Hai dầm rung lệch pha 180° để triệt tiêu lực phản ứng tại các đầu. Hiệu ứng triệt tiêu "
        "động lực của thiết kế DETF ngăn năng lượng thất thoát qua đầu dầm. Vì thế bộ cộng hưởng DETF cân bằng "
        "động lực có hệ số phẩm (Q) cao, dẫn đến một mạch dao động ổn định. Tín hiệu gia tốc là đầu ra từ dao "
        "động dưới dạng sóng vuông điều chế tần số có thể dùng cho giao tiếp số. Tần số cộng hưởng của hệ phải "
        "cao hơn hẳn mọi gia tốc vào, và điều này giới hạn dải đo được. Trong một gia tốc kế vi cơ quân dụng "
        "điển hình, các đặc tính cho:"))
    b.append(table(
        ["Thông số", "Giá trị"],
        [["Dải đo", "±1200 g"],
         ["Độ nhạy", "1,11 Hz/g"],
         ["Băng thông", "2500 Hz"],
         ["Tần số DETF không tải", "9952 Hz"],
         ["Tần số tại +1200 g", "11221 Hz"],
         ["Tần số tại −1200 g", "8544 Hz"],
         ["Độ nhạy nhiệt độ", "5 mg/°C"],
         ["Kích thước", "đường kính 6 mm × dài 4,3 mm"],
         ["Khối lượng", "khoảng 9 g"],
         ["Thời gian bật", "< 60 s"],
         ["Nuôi", "+9 đến +16 V DC"],
         ["Đầu ra danh định", "sóng vuông 9000 Hz"]],
        "Bảng 17.1 · Thông số điển hình của một gia tốc kế vi cơ quân dụng (theo nguồn Ch17)."))
    b.append(p(
        "Vi gia công bề mặt cũng dùng để chế tạo gia tốc kế ứng dụng riêng, như túi khí (air-bag) trong ô tô. "
        "Trong một loại, một tụ vi sai ba lớp được tạo bởi các lớp xen kẽ polysilicon và thuỷ tinh phosphosilicat "
        "(PSG) trên một bản dày 0,38 mm và dài 100 mm. Bản silicon làm đế cho kết cấu cơ khí. Lớp giữa hình võng "
        "người (trampoline) được treo bởi bốn cánh đỡ. Kết cấu di động này là khối lượng địa chấn của gia tốc "
        "kế. Các lớp polysilicon trên và dưới là các bản cố định cho tụ vi sai. Thuỷ tinh bị ăn mòn hy sinh bằng "
        "axit flohydric."))

    # ---- 17.11
    b.append(h2("17.11 Độ nhạy trục ngang", "Cross-Axis Sensitivity"))
    b.append(p(
        "Một kết cấu rung có thể chịu những dạng rung khác nhau như nén, xoắn, ngang…; hoặc sự tổ hợp của tất "
        "cả những rung động này xảy ra đồng thời, làm phân tích và đo lường khó khăn và phức tạp. Đã bàn rằng "
        "các phương trình vi phân chi phối chuyển động rung của một kết cấu phụ thuộc vào số bậc tự do, có thể "
        "mô tả như hàm của toạ độ không gian f(x,y,z,t). Ví dụ, rung ngang của kết cấu có thể là phương trình "
        "vi phân bậc bốn. May mắn, đa số đo gia tốc và rung động nói chung đơn giản, thuộc loại nén hoặc xoắn. "
        "Chúng dễ biểu diễn bằng phương trình vi phân bậc hai như ở phần đáp ứng tần số. Tuy nhiên, trong đo "
        "lường, đa số gia tốc kế bị ảnh hưởng bởi rung ngang và độ nhạy của chúng có thể đóng vai trò chính yếu "
        "trong độ chính xác đo."))
    b.append(p(
        "Độ nhạy ngang, còn gọi là độ nhạy trục ngang (cross-axis sensitivity), của một gia tốc kế là đáp ứng "
        "của nó với gia tốc trong mặt phẳng vuông góc với trục chính, như Hình 17.19. Độ nhạy trục ngang "
        "thường biểu thị bằng phần trăm độ nhạy trục chính và phải càng thấp càng tốt. Không có một giá trị "
        "duy nhất cho độ nhạy trục ngang, mà nó biến thiên tuỳ hướng. Hướng có độ nhạy cực tiểu thường do nhà "
        "sản xuất cung cấp. Việc đo độ nhạy trục ngang cực đại là một phần quy trình hiệu chuẩn từng chiếc và "
        "luôn phải dưới 3% đến 4%. Nếu có mức rung ngang cao, có thể dẫn đến kết quả tổng thể sai lệch. Trong "
        "trường hợp đó, phải có những bố trí riêng để xác lập mức và thành phần tần số của rung trục ngang. Độ "
        "nhạy trục ngang của các gia tốc kế điển hình được nhắc trong các phần liên quan: 2% đến 3% cho loại áp "
        "điện và dưới 1% ở đa số loại khác."))
    b.append(fig(19, F.fig(19)))

    # ---- 17.12
    b.append(h2("17.12 Lựa chọn, dải toàn thang và khả năng quá tải",
                "Selection, Full-Scale Range, and Overload Capability"))
    b.append(p(
        "Phải hết sức cẩn trọng lựa chọn gia tốc kế đúng để đáp ứng yêu cầu ứng dụng cụ thể. Thoạt nhìn, có vẻ "
        "một kho tàng gia tốc kế lớn đến rối rắm; tuy nhiên chúng có thể phân loại thành hai nhóm chính. Nhóm "
        "thứ nhất là các gia tốc kế đa dụng với các độ nhạy, tần số, toàn thang và dải quá tải khác nhau, cùng "
        "các tuỳ chọn kết nối cơ và điện khác nhau. Nhóm thứ hai là các loại đặc chủng có đặc tính nhắm đến một "
        "ứng dụng cụ thể. Khi quyết định loại ứng dụng (đa dụng hay đặc chủng) và gia tốc kế dùng, cần xem xét "
        "các đặc tính: đáp ứng quá độ hay độ nhạy trục ngang; dải tần; độ nhạy, khối lượng và dải động; đáp "
        "ứng trục ngang; và điều kiện môi trường như nhiệt độ, nhiễu cáp…"))
    b.append(h3("Dải tần", "The Frequency Range"))
    b.append(p(
        "Đo gia tốc thường giới hạn ở phần tuyến tính của đường đáp ứng. Đáp ứng bị giới hạn ở tần thấp cũng "
        "như tần cao bởi các cộng hưởng tự nhiên. Quy tắc thực tế, giới hạn tần số trên cho phép đặt bằng một "
        "phần ba tần số cộng hưởng của gia tốc kế sao cho rung động đo được dưới 1 dB về tính tuyến tính. Cần "
        "lưu ý dải tần hữu dụng của gia tốc kế cao hơn đáng kể, tức đến 1/2 hay 2/3 tần số cộng hưởng. Tần số "
        "đo có thể đặt cao hơn trong những ứng dụng chấp nhận tính tuyến tính thấp hơn (ví dụ 3 dB), như giám "
        "sát điều kiện bên trong máy móc vì độ lặp lại quan trọng hơn tính tuyến tính. Giới hạn tần số đo thấp "
        "do hai yếu tố: thứ nhất là tần số cắt thấp của bộ tiền khuếch đại đi kèm; thứ hai là ảnh hưởng của dao "
        "động nhiệt độ môi trường mà gia tốc kế có thể nhạy."))
    b.append(h3("Độ nhạy, khối lượng và dải động", "The Sensitivity, Mass, and Dynamic Range"))
    b.append(p(
        "Lý tưởng, độ nhạy đầu cuối càng cao càng tốt; nhưng phải thoả hiệp giữa độ nhạy với tần số, dải, khả "
        "năng quá tải và kích thước. Khối lượng gia tốc kế trở nên quan trọng khi dùng trên vật thử nhỏ và nhẹ. "
        "Gia tốc kế không được tải lên phần kết cấu, vì khối lượng thêm có thể thay đổi đáng kể mức và tần số "
        "hiện diện tại các điểm đo và làm mất hiệu lực kết quả. Quy tắc chung, khối lượng gia tốc kế không "
        "được lớn hơn một phần mười khối lượng hiệu dụng của phần hay kết cấu được gắn để đo. Dải động của gia "
        "tốc kế phải khớp với mức gia tốc cao hay thấp của vật đo. Gia tốc kế đa dụng có thể tuyến tính đến "
        "5000 g đến 10.000 g, vốn đã sâu vào dải đa số xung kích cơ học. Gia tốc kế đặc chủng đo được đến "
        "100.000 g."))
    b.append(p(
        "Một điểm quan trọng trong ứng dụng thực: nếu giảm chấn cơ là vấn đề, giảm chấn khí được ưu tiên hơn "
        "giảm chấn dầu, vì giảm chấn dầu cực kỳ nhạy với thay đổi độ nhớt. Nếu các phần tử ổn định nhiệt độ, "
        "giảm chấn điện có thể đủ."))
    b.append(h3("Đáp ứng quá độ", "The Transient Response"))
    b.append(p(
        "Xung kích được đặc trưng là sự giải phóng năng lượng đột ngột dưới dạng các xung thời gian ngắn với "
        "nhiều hình dạng và thời gian lên (rise time) khác nhau. Chúng có biên độ lớn và nội dung tần số rộng. "
        "Trong ứng dụng liên quan đo quá độ và xung kích, tính tuyến tính tổng thể của hệ đo có thể bị giới hạn "
        "ở tần cao và tần thấp bởi những hiện tượng gọi tương ứng là dịch zero (zero shift) và rung (ringing). "
        "Dịch zero do cả phi tuyến pha trong tiền khuếch đại và gia tốc kế không trở về trạng thái xác lập sau "
        "khi chịu xung kích lớn. Ringing do các thành phần tần số cao của kích thích gần tần số cộng hưởng ngăn "
        "gia tốc kế trở về trạng thái xác lập. Để tránh sai số đo do các hiệu ứng này, tần số vận hành của hệ "
        "đo phải giới hạn trong dải tuyến tính."))
    b.append(h3("Dải toàn thang và khả năng quá tải", "Full-Scale Range and Overload Capability"))
    b.append(p(
        "Đa số gia tốc kế có thể đo gia tốc theo cả hai chiều dương và âm. Chúng cũng được thiết kế để chịu được "
        "khả năng quá tải. Các thảo luận thích đáng về dải toàn thang và khả năng quá tải có trong các phần "
        "liên quan. Nhà sản xuất thường cung cấp thông tin về hai đặc tính này."))
    b.append(h3("Điều kiện môi trường", "Environmental Conditions"))
    b.append(p(
        "Khi lựa chọn và thực hiện gia tốc kế, cần xem xét các điều kiện môi trường như dải nhiệt độ, quá độ "
        "nhiệt, nhiễu cáp, hiệu ứng từ trường, độ ẩm, nhiễu âm… Nhà sản xuất cũng cung cấp thông tin về điều "
        "kiện môi trường."))

    # ---- 17.13
    b.append(h2("17.13 Điều kiện tín hiệu", "Signal Conditioning"))
    b.append(p(
        "Các bộ điều kiện tín hiệu thông thường thích hợp để ghép gia tốc kế với máy tính hay các thiết bị khác "
        "cho xử lý tín hiệu tiếp. Cần thận trọng cung cấp tải điện phù hợp cho gia tốc kế tự sinh. Nhìn chung, "
        "các tín hiệu thô sinh ra được khuếch đại và lọc thích đáng bởi các mạch trong vỏ gia tốc kế do nhà "
        "sản xuất cung cấp. Tuy nhiên, cảm biến áp điện và áp điện trở đòi hỏi những bộ điều kiện tín hiệu đặc "
        "biệt với một số đặc tính như bàn sau. Cũng đưa ra ví dụ mạch điều kiện tín hiệu cho vi gia tốc kế."))
    b.append(h3("Điều kiện tín hiệu cho gia tốc kế áp điện", "Signal Conditioning Piezoelectric Accelerometers"))
    b.append(p(
        "Gia tốc kế áp điện cung cấp rất ít năng lượng cho bộ điều kiện tín hiệu. Nó có trở nguồn điện dung "
        "cao. Mạch tương đương của một gia tốc kế áp điện có thể xem như một tụ chủ động tự nạp khi được tải cơ "
        "học. Cấu hình các phần tử điều kiện tín hiệu ngoài phụ thuộc mạch tương đương đã chọn. Thiết kế bộ "
        "khuếch đại điện tích (charge amplifier) là cách tiếp cận phổ biến nhất vì độ lợi hệ và đáp ứng tần số "
        "thấp được xác định rõ. Đặc tính mạch độc lập với chiều dài và điện dung cáp của gia tốc kế."))
    b.append(p(
        "Bộ khuếch đại điện tích gồm một điện áp ra của bộ đổi điện tích sinh ra do tín hiệu điện tích vào trả "
        "về qua tụ phản hồi để giữ điện áp vào gần mức không, như Hình 17.20. Một điểm quan trọng về bộ khuếch "
        "đại điện tích là độ nhạy của chúng có thể được chuẩn hoá. Về cơ bản chúng đổi điện tích vào thành điện "
        "áp trước rồi mới khuếch đại điện áp này. Với sự phản hồi kiểu cơ bản, đầu vào bộ khuếch đại được giữ "
        "về cơ bản ở không volta; do đó nó trông như một mạch ngắn với đầu vào. Điện áp ra bộ đổi điện tích sinh "
        "ra do tín hiệu điện tích vào được trả về qua tụ phản hồi để giữ điện áp đầu vào gần không. Nhờ vậy, "
        "điện tích vào được lưu trong tụ phản hồi, sinh một điện áp trên nó bằng giá trị điện tích vào chia "
        "cho điện dung tụ phản hồi. Hàm truyền đầy đủ của mạch mô tả quan hệ giữa điện áp ra và độ lớn gia tốc "
        "vào xác định được:"))
    b.append(eq("E₀ = Sₐ a₀ · (1 + jω Cₐ/C_f) / ((1 + 1/G)(1 + jω R_f C_f))", "17.46"))
    b.append(p(
        "với E₀ = điện áp ra bộ đổi điện tích (V), a₀ = độ lớn gia tốc (m/s²), Sₐ = độ nhạy gia tốc kế (mV/g), "
        "Cₐ = điện dung gia tốc kế (F), C_c = điện dung cáp (F), C_f = điện dung vòng phản hồi (F), R_f = điện "
        "trở vòng phản hồi, G = độ lợi vòng hở bộ khuếch đại. Trong đa số ứng dụng, vì C_f được chọn lớn so với "
        "(Cₐ + C_c)/(1 + G), độ lợi hệ trở nên độc lập với chiều dài cáp. Khi đó, mẫu số rút gọn cho một hệ bậc "
        "nhất với tần số cắt:"))
    b.append(eq("f_{−3 dB} = 1 / (2π R_f C_f)", "17.47"))
    b.append(p(
        "với độ dốc 10 dB/một thập kỷ. Về thực tế, đáp ứng tần số thấp của hệ này là hàm của các linh kiện điện "
        "tử xác định rõ và không biến thiên theo chiều dài cáp. Đây là một đặc điểm quan trọng khi đo rung "
        "động tần số thấp. Nhiều gia tốc kế được chế tạo tích hợp tiền khuếch đại và các mạch điều kiện tín hiệu "
        "khác trong cùng vỏ với bộ chuyển đổi. Một số tiền khuếch đại gia tốc kế gồm cả bộ tích phân để đổi đầu "
        "ra tỉ lệ gia tốc thành tín hiệu tỉ lệ vận tốc hay dịch chuyển. Để suy giảm nhiễu và tín hiệu rung "
        "nằm ngoài dải tần quan tâm, đa số tiền khuếch đại trang bị một dải bộ lọc thông cao và thông thấp. Điều "
        "này tránh nhiễu điện hay tín hiệu trong phần tuyến tính của dải tần gia tốc kế. Tuy vậy, đáng nói là "
        "những thiết bị này thường có hai hằng số thời gian, ngoài và trong. Sự pha trộn hai hằng số này có thể "
        "gây vấn đề, nhất là ở tần số thấp. Hằng số thời gian trong thường do nhà sản xuất cố định trong thiết "
        "kế chế tạo. Cần đặc biệt lưu ý xử lý ảnh hưởng của hằng số thời gian ngoài trong nhiều ứng dụng chủ "
        "yếu bằng cách quan sát trở kháng ghép."))
    b.append(fig(20, F.fig(20)))
    b.append(h3("Điều kiện tín hiệu cho cảm biến áp điện trở", "Signal Conditioning of Piezoresistive Transducers"))
    b.append(p(
        "Cảm biến áp điện trở nhìn chung có đầu ra biên độ cao, trở ra thấp và nhiễu nội thấp. Đa số cảm biến "
        "này thiết kế cho kích điện áp không đổi. Chúng thường được hiệu chuẩn cho kích dòng không đổi để độc "
        "lập với ảnh hưởng ngoài. Nhiều cảm biến áp điện trở cấu hình như thiết bị cầu đầy đủ (full-bridge). "
        "Một số có bốn nhánh áp điện trở chủ động và, cùng với hai điện trở chính xác cố định, cho phép hiệu "
        "chuẩn shunt trong bộ điều kiện tín hiệu, như Hình 17.21."))
    b.append(fig(21, F.fig(21)))
    b.append(h3("Vi gia tốc kế", "Microaccelerometers"))
    b.append(p(
        "Trong vi gia tốc kế, mạch điều kiện tín hiệu được tích hợp trong cùng chip với cảm biến, như Hình "
        "17.22. Một ví dụ điển hình của mạch điều kiện tín hiệu ở dạng sơ đồ khối cho Hình 17.23. Trong loại "
        "gia tốc kế này, hệ điện tử thực chất là một mạch dao động điều khiển bằng thạch anh và tín hiệu ra của "
        "dao động là một tín hiệu gia tốc điều chế tần số. Một số mạch cung cấp đầu ra sóng vuông có đệm có "
        "thể giao tiếp số trực tiếp. Trong trường hợp này, nhu cầu chuyển đổi tương tự–số (ADC) được loại bỏ, "
        "nhờ đó loại bỏ một trong những nguồn lỗi chính. Ở các loại gia tốc kế khác, các mạch điều kiện tín "
        "hiệu như ADC vẫn được giữ trong chip."))
    b.append(fig(22, F.fig(22)))
    b.append(fig(23, F.fig(23)))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>K. G. McConnell, <i>Vibration Testing: Theory and Practice</i>, New York: John Wiley &amp; Sons, 1995.</li>'
             '<li><i>Machine Vibration: Dynamics and Control</i>, London: Springer, 1992–1996.</li>'
             '<li>E. O. Doebelin, <i>Measurement Systems: Application and Design</i>, 4th ed., New York: McGraw-Hill, 1990.</li>'
             '<li>R. Frank, <i>Understanding Smart Sensors</i>, Boston: Artech House, 1996.</li>'
             '</ol>')
    b.append(p(
        "Chương kết thúc bằng danh sách các nhà sản xuất (Allied Signal, Bokam Engineering, CEC Vibration "
        "Products, Dytran, Endevco, Kistler, Metrix, PCB Piezotronics, Setra, Silicon Microstructures, SKF, "
        "Wilcoxon Research…) — không dịch vì chỉ là thông tin thương mại."))

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 16</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is the English companion to the Vietnamese translation of Chapter 17, “Acceleration, "
        "Vibration, and Shock Measurement” by Halit Eren. All twenty-three figures are redrawn as vectors, "
        "and the governing equations (17.1–17.47) are reproduced. The translation prose is not repeated here."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Accelerometers measure a general absolute-motion parameter — acceleration — and are also the sensor "
        "of choice for vibration and shock. They come as active (self-generating, e.g. piezoelectric) or "
        "passive (changing capacitance, needing external power); only passive types measure true static (dc) "
        "acceleration. They are preferred over displacement/velocity sensors because of their wide frequency "
        "range (down to dc), because destructive forces track acceleration, because transients/shocks are easy "
        "to capture, and because velocity and displacement are obtained by integration. They classify as "
        "deflection or null-balance, dynamic or kinematic, mechanical or electrical. Figure 17.1 shows the "
        "generic deflection-type seismic accelerometer. Calibration is static (tilting table, centrifuge up to "
        ">50,000 g) or dynamic (electrodynamic shaker + laser interferometer; back-to-back working standard)."))
    b.append(p(
        "Section 17.1 develops the dynamics. Periodic motion is sinusoidal: x(t)=X_peak·sin(ωt) (Eq. 17.1), "
        "u(t)=ω X_peak·cos(ωt) with U_peak=ω X_peak (Eq. 17.2), and a(t)=−ω² X_peak·sin(ωt) with A_peak=ω² "
        "X_peak=ω U_peak (Eq. 17.3); velocity leads displacement by 90°, acceleration leads velocity by "
        "another 90°. Non-sinusoidal periodic motion expands by Fourier series (Eq. 17.4). Random, transient "
        "and nonstationary vibrations are handled statistically (DFT/FFT, spectra, RMS). The seismic "
        "mass–spring–damper obeys m ẍ + c ẋ + k x = f(t) (Eq. 17.5) and, including base motion, m z̈ + c ż + "
        "k z = m g cosθ − m ẍ₁ (Eq. 17.6). In Laplace form: X(s)/F(s)=1/(m s²+c s+k)=K/(s²+2ζωₙ s+ωₙ²) "
        "(Eqs. 17.7–17.8) with ωₙ=√(k/m), ζ=c/(2√(km)). Figures 17.2–17.5 show the log a/v/x relation, the "
        "single-DOF pulse response, the unit-step responses for various ζ, and the Bode gain/phase plots. "
        "Multi-degree-of-freedom systems show one resonance peak per DOF; mass loading on light test pieces "
        "must be corrected."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Section 17.2 — electromechanical force-balance (servo) accelerometers. The displacement of a "
        "seismic mass is sensed and a proportional magnetic force restores the null, giving better linearity "
        "and no hysteresis than a mechanical spring, plus electrical self-test. Coil-and-magnetic types follow "
        "Ampère’s law F=m a=i l B (Eqs. 17.9–17.10); Figure 17.6 shows the basic coil/magnet unit. A "
        "rotational servo (Figure 17.7) yields e₀/eₐ=(K_p K_c R/K_s)·Kₐ s²/(s²+2ζωₙₗ s+ωₙₗ²) (Eq. 17.11), "
        "which for high loop gain reduces to a≈e₀/(Kₘ R) (Eqs. 17.12–17.13) — accuracy shifts from mechanical "
        "parts to a few stable parameters. Induction types (cup-and-magnet, eddy-current torque) are "
        "essentially generators; a typical instrument offers 1 µg threshold, 500 Hz natural frequency, ζ=0.3–"
        "0.8, 0.1% cross-axis, ±10 V at 30 g."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "Section 17.3 — piezoelectric accelerometers. Compression or shear crystals under a proof mass give "
        "q=dᵢⱼ F=dᵢⱼ m a (Eq. 17.17); PZT has ~150× quartz’s strain constant. The transfer function is "
        "third-order (Eq. 17.18) with very small damping (ζ<0.01); low-frequency response needs large "
        "time-constant τ via a high-impedance amplifier. Figures 17.8–17.9 show the compression element and "
        "typical PZT frequency response. They cover 0.004 pC/g (250 kHz) to 1000 pC/g (7 kHz), down to 3×3 mm "
        "and 0.5 g, but have 2–4% cross-axis sensitivity."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "Section 17.4 — piezoresistive accelerometers use semiconductor strain gages (large gage factor) in a "
        "Wheatstone bridge, are true static devices, useful below 1 Hz (Figure 17.10). Section 17.5 — "
        "differential-capacitance accelerometers: C=kεS/h (Eq. 17.19), h=h₀+m a/K (Eq. 17.20), giving f=f₀+fₐ "
        "(Eqs. 17.21–17.25); a diaphragm version (Figure 17.12) uses squeeze-film air damping (ζ≈0.7 stable "
        "within 15%). Figures 17.11–17.12."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(fig(11, F.fig(11), "en"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "Section 17.6 — strain-gage accelerometers: ΔR/R=ΔL/L+2ν(ΔL/L)+(dρ/ρ)/(dL/L) (Eq. 17.26); bonded or "
        "unbonded wire, or semiconductor on a cantilever. Section 17.7 — seismic accelerometers. Newton’s "
        "law gives m ẍ₂+c ẋ₂+k x₂=m g cosθ+m ẍ₁ (Eq. 17.27) and, for relative motion, m z̈+c ż+k z=m g "
        "cosθ−m ẍ₁ (Eq. 17.28); with x₁(t)=x₁₀ sin(ω₁ t) it becomes m z̈+c ż+k z=m g cosθ+m a₁ sin(ω₁ t) "
        "(Eq. 17.30) with z=(m g/k)cosθ+(m a₁/k)·sin(ω₁t−φ)/√((1−r²)²+(2ζr)²) (Eq. 17.31), r=ω₁/ωₙ, "
        "φ=tan⁻¹(2ζr/(1−r²)) (Eq. 17.32). At high ω₁/ωₙ the output is linear and k z=m ẍ₁ (Eq. 17.33). Figures "
        "17.13–17.15 show the displacement curve, the potentiometer version, and the strain-gage cantilever."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p(
        "Section 17.8 — inertial types. A vibrating-string accelerometer (Figure 17.16) has f₁=(1/2l)√(T₁/mₛ), "
        "f₂=(1/2l)√(T₂/mₛ) (Eq. 17.34) and f₁²−f₂²=m a/(4 l² mₛ) (Eqs. 17.35–17.36); the sum is held "
        "constant by servo so the difference is linear in a. Cantilever and suspended-mass (centrifugal "
        "balance) variants follow. All are absolute instruments — scale factors set by mass, length, time."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "Section 17.9 — electrostatic force-feedback accelerometers. Coulomb’s law gives E=Q/(kεS) (Eq. 17.37) "
        "and F=kεE²S/2 (Eq. 17.38). With E=(V₁−V₂)/h, F=kεS(V₁−V₂)²/(2h²) (Eqs. 17.39–17.40); the acceleration "
        "is a=kε(V₁−V₂)²/(2m h²) (Eq. 17.41), a quadratic relation V₁−V₂=√D·√a (Eq. 17.42). A second "
        "electrode linearizes it to a=(kεS/h²m)·(4V₁V₂) (Eqs. 17.43–17.45). Advantages: mechanical simplicity, "
        "low power, no hysteresis, zero tempco, easy shielding."))
    b.append(p(
        "Section 17.10 — microaccelerometers. Bulk micromachining (from single-crystal silicon) and surface "
        "micromachining (sacrificial-layer etching, Figure 17.17) build 3-D structures. Vibrating-beam / "
        "double-ended tuning fork (DETF) devices (Figure 17.18) keep two beams 180° out of phase for a high-Q "
        "resonator; the acceleration appears as an FM square wave. A typical military unit: ±1200 g, 1.11 "
        "Hz/g, 2500 Hz bandwidth, DETF 9952 Hz unloaded, 8544 Hz at −1200 g, 11221 Hz at +1200 g, 9 g, 6 mm "
        "× 4.3 mm, 9000 Hz square-wave output."))
    b.append(fig(17, F.fig(17), "en"))
    b.append(fig(18, F.fig(18), "en"))
    b.append(p(
        "Section 17.11 — cross-axis sensitivity (Figure 17.19) is the response to acceleration perpendicular "
        "to the main axis, expressed as % of main-axis sensitivity; it varies with direction and must stay "
        "below 3–4% (2–3% for piezoelectric, <1% for most others). Sections 17.12 and 17.13 cover selection "
        "(frequency range ≈ ⅓ of resonance for <1 dB; mass ≤ 1/10 of test mass; dynamic range to 10,000 g, "
        "specials to 100,000 g; transient zero-shift and ringing limits) and signal conditioning. "
        "Piezoelectric types use a charge amplifier (Figure 17.20) with E₀=Sₐ a₀(1+jωCₐ/C_f)/((1+1/G)(1+jωR_f "
        "C_f)) (Eq. 17.46), rolling off at f_{−3dB}=1/(2πR_f C_f) (Eq. 17.47), independent of cable length. "
        "Piezoresistive types use a full-bridge with shunt calibration (Figure 17.21). Microaccelerometers "
        "integrate conditioning on-chip (Figures 17.22–17.23), often outputting a buffered FM square wave that "
        "needs no ADC."))
    b.append(fig(19, F.fig(19), "en"))
    b.append(fig(20, F.fig(20), "en"))
    b.append(fig(21, F.fig(21), "en"))
    b.append(fig(22, F.fig(22), "en"))
    b.append(fig(23, F.fig(23), "en"))
    b.append(p(
        "The chapter lists four references (McConnell on vibration testing, Doebelin’s Measurement Systems, "
        "Springer’s Machine Vibration, and Frank’s Understanding Smart Sensors) plus a manufacturer list — "
        "reproduced in the Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 16</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 17 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 17 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 17 “Đo gia tốc, rung động và xung kích” của Halit Eren — động lực "
            "học gia tốc kế, các loại servo, áp điện, áp điện trở, điện dung vi sai, strain-gage, địa chấn, "
            "quán tính, tĩnh điện, vi gia tốc kế, độ nhạy trục ngang và điều kiện tín hiệu, với 23 hình và "
            "phương trình 17.1–17.47." if vi else
            "Companion to Chapter 17 of the CRC Measurement Handbook — acceleration, vibration, and shock "
            "measurement, with all twenty-three figures and equations 17.1–17.47.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 17' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 17' % BASE_EN)
    meta = ("Chương 17 · theo Ch17.pdf (CRC Press, 1999) · 23 hình, 4 tài liệu tham khảo" if vi
            else "Chapter 17 · 23 figures, 4 references")
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
