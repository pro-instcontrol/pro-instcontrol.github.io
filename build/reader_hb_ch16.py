# -*- coding: utf-8 -*-
"""Handbook Chapter 16 — Velocity Measurement (Charles P. Pinney, William E. Baker).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch16.py
"""
import os

import hb16fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch16-velocity-measurement"
TITLE_EN = "Velocity Measurement"
TITLE_VI = "Đo vận tốc"
BYLINE = "Charles P. Pinney · Pinney Technologies, Inc. · William E. Baker · University of New Mexico"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch15-tilt-measurement"
PREV_VI = "ch15-tilt-measurement"
PREV_T_EN = "Tilt Measurement"
PREV_T_VI = "Đo độ nghiêng"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-16-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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
        "Vận tốc tuyến tính của một vật — hay đúng hơn của một hạt — được định nghĩa là tốc độ thay đổi theo "
        "thời gian của vị trí vật. Nó là một đại lượng vector, tức có cả hướng và độ lớn, và hướng đó trùng với "
        "hướng của sự thay đổi vị trí. Độ lớn của vận tốc gọi là tốc độ (speed), biểu thị vật chuyển động nhanh "
        "nhường nào; đó chính là điều đồng hồ tốc độ (speedometer) trên ô tô chỉ ra, nên tên gọi này rất hợp lý. "
        "Vận tốc tuyến tính luôn được đo thông qua — hoặc so với — một vật tham chiếu. Đồng hồ tốc độ cho biết ta "
        "đang chuyển động nhanh thế nào so với mặt đất. Thông thường, “vận tốc” chỉ cần nói đến vận tốc tuyến "
        "tính. Các đơn vị phổ biến là mét trên giây và dặm trên giờ, nhưng bất kỳ tổ hợp độ dài trên thời gian "
        "nào cũng đúng."))
    b.append(p(
        "Vận tốc góc (hay vận tốc quay) của một vật được định nghĩa là tốc độ thay đổi theo thời gian của vị trí "
        "góc, đo lường vật quay nhanh đến mức nào; nó hoàn toàn tương tự vận tốc tuyến tính nhưng cho chuyển "
        "động quay. Đơn vị thường dùng là vòng trên phút (rpm), dù bất kỳ đơn vị góc nào trên một đơn vị thời "
        "gian đều dùng được. Vận tốc góc cũng là vector, hướng của nó trùng với hướng của trục mà vật quay quanh. "
        "Ví dụ một ô tô dừng ở đèn đỏ với động cơ nổ máy: vận tốc góc của trục khuỷu có độ lớn (tốc độ quay) "
        "khoảng 800 rpm và một hướng gắn với hướng trục khuỷu chỉ. Trục quay của vật có thể chuyển động chứ "
        "không nhất thiết cố định — như khi ô tô vào cua. Vận tốc lăn, ngáp (yaw) hay chúc (pitch) của máy bay "
        "được cho theo các tốc độ quay quanh mỗi trục quay, tương tự trục khuỷu."))
    b.append(p(
        "Thông thường, vật tham chiếu để đo vận tốc tuyến hoặc góc được hiểu ngầm từ ngữ cảnh bài toán và thường "
        "không nêu rõ; phương pháp đo chính là cái xác định tham chiếu đó. Các ứng dụng đo vận tốc gồm: (1) điều "
        "khiển tốc độ cấp phôi kim loại vào máy công cụ — cấp quá nhanh gây mòn nhanh hoặc hỏng máy, quá chậm "
        "làm giảm năng suất; (2) đo tốc độ tiếp cận của dụng cụ robot tới đích; (3) giám sát tốc độ máy phát "
        "điện trong nhà máy điện; (4) radar sân bay đo tốc độ máy bay tiếp cận bằng hiệu ứng Doppler; (5) đo "
        "tốc độ bánh xe ô tô để phản hồi cho hệ phanh chống bó cứng (ABS)."))

    # ---- 16.2
    b.append(h2("16.2 Đo vận tốc tuyến tính", "Measurement of Linear Velocity"))
    b.append(p(
        "Việc đo vận tốc khác các đại lượng khác ở chỗ không có nhiều loại và hãng cảm biến để chọn cho một "
        "bài toán. Thường người ta phải vận dụng hiểu biết về đo các đại lượng khác và sự sáng tạo để phát triển "
        "một phương pháp đo phù hợp. Vận tốc thường thu được bằng cách vi phân vị trí hoặc tích phân gia tốc. "
        "Các phương trình nền tảng được cho dưới đây. Hình 16.1 biểu diễn vị trí của một vật theo thời gian khi "
        "nó chuyển động trên một đường thẳng đứng (phương y). Đại lượng cần đo có thể là vận tốc trung bình, và "
        "độ lớn của nó được định nghĩa như sau:"))
    b.append(eq("v_tb = (y₂ − y₁) / (t₂ − t₁)", "16.1"))
    b.append(p(
        "cho khoảng thời gian t₁ đến t₂. Khi khoảng thời gian thu nhỏ, tốc độ trung bình trở thành tốc độ tức "
        "thời V_y, và định nghĩa trở thành độ dốc của đường cong vị trí–thời gian:"))
    b.append(fig(1, F.fig(1)))
    b.append(eq("V_y = dy / dt   (giới hạn Δt → 0)", "16.2"))
    b.append(p(
        "Chỉ số dưới chỉ thành phần y. Khi gắn với hướng đã biết, tốc độ này trở thành vận tốc. Vì gia tốc là "
        "tốc độ thay đổi theo thời gian của vận tốc, tốc độ vật cũng có thể cho bởi:"))
    b.append(eq("V_y(t) = V_y(tᵢ) + ∫_{tᵢ}^{t} a_y(t) dt", "16.3"))
    b.append(p(
        "với a_y(t) là gia tốc phương y (cho Hình 16.1) và V_y(tᵢ) là tốc độ tại thời tᵢ. Mỗi phương trình trên "
        "có thể làm cơ sở cho một phép đo vận tốc. Lưu ý: với chuyển động nhiều hơn một chiều, sẽ có nhiều hơn "
        "một thành phần và các phương trình tương ứng cho các chiều khác (x, y); song việc đo vận tốc luôn thực "
        "hiện theo từng thành phần riêng biệt."))
    b.append(p(
        "Thuận tiện khi chia các kỹ thuật đo vận tốc thành hai lớp: một gọi là “phương pháp có tham chiếu”, "
        "một là “cảm biến địa chấn hay quán tính”. Phương pháp có tham chiếu là phép đo có bộ phận lắp trên cả "
        "vật chuyển động và khung tham chiếu. Cảm biến địa chấn không cần tiếp xúc với khung tham chiếu, nhưng "
        "chúng cho tốc độ so với tốc độ của cảm biến tại thời điểm bắt đầu thử; chuyển động ban đầu phải xác "
        "định từ các xét đo khác và cộng vào tốc độ tương đối."))

    b.append(h3("Đo dựa trên tham chiếu", "Reference-Based Measurement"))
    b.append(p(
        "Dùng phương trình (16.1), một giá trị vận tốc trung bình theo một phương của vật xác định được từ quãng "
        "đường đi được theo phương đó và thời gian cần thiết. Xác định tốc độ miệng nòng đạn là một ví dụ: bố trí "
        "hai đầu dò cách nhau một khoảng đã biết và ghi lại thời gian cạnh đạn đi qua giữa chúng là cách làm phổ "
        "biến. Đầu dò thường là cảm biến tiệm cận (xem đo vị trí), chùm tia laser hay ánh sáng chuẩn trực có diode "
        "cảm biến, và tiếp điểm đóng (hoặc mở) do vật chuyển động. Đo khoảng thời gian dùng bộ đếm điện tử hoặc "
        "hiển thị đầu ra lên oscilloscope. Khi thiết kế, phải cẩn thận giảm thiểu ảnh hưởng của vật đi qua cửa sổ "
        "lên vị trí và đáp ứng của cảm biến — ví dụ áp lực từ luồng phụt nòng có thể làm dịch chuyển cảm biến trên "
        "giá đỡ, làm sai khoảng cách giữa chúng trong lúc đo, trong khi ngoại hình vẫn không đổi nên người thử "
        "không hay biết."))
    b.append(p(
        "Dùng chuỗi đầu dò cách đều nhau xác định được tốc độ trung bình tại một dãy vị trí. Một biến thể là chiếu "
        "sáng đường chuyển động bằng đèn chớp nhấp nháy tần số biết trước và dùng ảnh phơi sáng để có một bức "
        "ảnh vật ở một dãy vị trí; biết tỉ lệ chiều dài và tần số chớp, tính được tốc độ trung bình tại dãy vị trí. "
        "Nếu mặt phẳng chuyển động trùng mặt phẳng ảnh, hai thành phần vận tốc xác định được. Một biến thể khác "
        "dùng camera ghi hình chuyển động và thời base của video làm thang thời gian — camera tốc độ cao tới "
        "12.000 khung/giây mở rộng dải vận tốc, và ghi số hóa giúp đo khoảng cách dễ và chính xác hơn."))
    b.append(p(
        "Một biến thể khác là dùng loại cảm biến vị trí nào đó ghi hàm vị trí–thời gian của vật rồi vi phân hàm "
        "này để có tốc độ–thời gian. Cảm biến vị trí đã bàn ở chương trước; chọn cảm biến thích hợp rất quan "
        "trọng — tầm đo, độ phân giải và tải khối lượng là các tham số cần lưu ý. Vì vi phân dữ liệu thực nghiệm "
        "là một quá trình sinh nhiễu, phải đặc biệt giảm nhiễu điện trong dữ liệu vị trí đến mức tối thiểu; hàm "
        "tốc độ–thời gian tính ra cũng có thể cần làm trơn để giảm nhiễu do số hóa."))
    b.append(p(
        "Một loại cảm biến vận tốc dựa trên máy phát tuyến tính. Khi cuộn dây cắt các đường sức từ quanh nam châm, "
        "một điện áp cảm ứng sinh trong cuộn, phụ thuộc quan hệ:"))
    b.append(eq("e_i ∝ B · L · V", "16.4"))
    b.append(p(
        "với e_i = điện áp cảm ứng, B = cảm ứng từ, L = chiều dài dây trong cuộn, V = tốc độ cuộn dây so với "
        "nam châm. Quan hệ này làm cơ sở cho cảm biến vận tốc tuyến tính (LVT); sơ đồ một loại cho ở Hình 16.2. "
        "Các hãng sản xuất gồm Trans-Tek Inc. (Ellington, CN), Robinson-Halpern Products (Valley Forge, PA), và "
        "Macro Sensors, Div. of Howard A. Schaevitz Technologies (Pennsauken, NJ). Dải dịch chuyển làm việc từ "
        "0,5 in đến 24 in, độ nhạy điển hình từ 40 mV/ips đến 600 mV/ips."))
    b.append(fig(2, F.fig(2)))
    b.append(h3("Chuyển từ tuyến tính sang quay", "Conversion of Linear to Rotational Velocity"))
    b.append(p(
        "Một máy phát một chiều quay (bàn ở phần sau) cũng đo được vận tốc tuyến tính bằng cách gắn một bánh "
        "răng thẳng (rack) trên vật chuyển động và để bánh răng này dẫn động máy phát qua bộ bánh răng thẳng "
        "(pinion). Đó chính là nguyên lý mà đồng hồ tốc độ ô tô dùng để đổi vận tốc tuyến tính thành kim chỉ vận "
        "tốc góc trên bảng điều khiển."))
    b.append(h3("Dịch chuyển Doppler", "Doppler Shift"))
    b.append(p(
        "Dịch chuyển Doppler là sự thay đổi biểu kiến của tần số sóng khi nguồn và người quan sát chuyển động "
        "tương đối với nhau. Hiện tượng áp dụng cho mọi loại sóng — âm thanh, ánh sáng, vi ba... Nó được quan "
        "sát đầu tiên với sóng âm và mang tên nhà toán học vật lý người Áo Christian Doppler (1803–1853), người "
        "đầu tiên công bố bài báo về nó cho sóng ánh sáng năm 1842."))
    b.append(note(
        "<b>Lưu ý người dịch — lỗi nguồn:</b> đoạn gốc viết “tần số tăng khi nguồn và người quan sát tiến lại "
        "gần nhau (<i>red shift</i>) và giảm khi họ rời xa nhau (<i>blue shift</i>)”. Điều này <b>ngược</b> với "
        "vật lý chuẩn: tiến lại gần làm tần số tăng (dịch xanh — <i>blue shift</i>), rời xa làm tần số giảm (dịch "
        "đỏ — <i>red shift</i>). Chính đoạn sau của chương cũng mâu thuẫn với lỗi này: tiếng còi tàu vọng lại cao "
        "hơn khi tàu đến gần rồi trầm xuống khi tàu đi xa — đó mới là đúng. Định nghĩa <i>blue shift = tiến lại, "
        "red shift = rời xa</i> mới chính xác."))
    b.append(p(
        "Radar — viết tắt của “radio detection and ranging” — là kỹ thuật khác phát hiện vị trí, chuyển động và "
        "bản chất của vật từ xa nhờ sóng vô tuyến phản xạ từ bề mặt nó. Radar xung dùng một anten định hướng để "
        "phát và thu; nó phát các xung sóng điện từ (thường là vi ba) một phần bị phản xạ bởi vật cản trên đường "
        "chùm. Anten chỉ nối với máy phát lúc phát và với máy thu lúc thu, chuyển đổi trong một phần triệu giây "
        "giữa các xung. Khoảng cách vật tới nguồn radar xác định bằng thời gian tín hiệu đi tới đích và về; hướng "
        "vật xác định từ hướng phát xung. Radar xung chủ yếu dùng cho hàng không, hàng hải quân sự và quân sự. "
        "Trong radar Doppler (sóng liên tục), hai anten dùng — một phát, một thu. Vì thời gian tín hiệu liên tục "
        "đi tới đích và về không đo được, radar Doppler không xác định được khoảng cách; vận tốc vật xác định qua "
        "hiệu ứng Doppler: tiến lại gần thì tần số trả về lớn hơn, rời xa thì nhỏ hơn, đứng yên thì bằng tần số "
        "phát. Một ứng dụng là bản tin thời tiết buổi tối: radar đo được sự xoáy gió trong giông và nhận diện "
        "lốc xoáy tiềm tàng. Hệ VORAD của Eaton là hệ lắp trên xe để an toàn, phát hiện khi có sự tiếp cận nguy "
        "hiểm với xe khác và tự phanh trong tình huống khẩn cấp."))
    b.append(h3("Phương pháp giao thoa ánh sáng", "Light Interference Methods"))
    b.append(p(
        "Đo vận tốc có thể thực hiện bằng nguyên lý giao thoa ánh sáng. Hình 16.3 trình bày bố cục Michelson "
        "dùng những năm 1890 để biểu diễn giao thoa ánh sáng. Một chùm đơn sắc được chẻ làm hai; một chùm hướng "
        "tới gương đứng yên, chùm kia tới vật tiêu chuẩn chuyển động. Người quan sát thấy hai chùm chồng chất. Khi "
        "gương chuyển một hướng, sự cộng hai sóng sẽ luân phiên tăng cường và triệt tiêu. Lượng chuyển động cho "
        "một chu kỳ biến thiên cường độ ánh sáng chính là bước sóng ánh sáng dùng. Tần số các chuyển sáng–tối tỉ "
        "lệ với vận tốc vật tiêu chuẩn. Đo giao thoa cho độ chính xác rất cao — ví dụ 1 m ứng với 1.650.763,73 "
        "đếm vân với ánh sáng cam do krypton-86 phát."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Nguyên lý này cần tinh chỉnh để tiện dụng — ví dụ dùng laser làm nguồn sáng. Một nhà cung cấp thương mại "
        "loại này, gọi là Laser Doppler Vibrometer, là Polytec PI (Costa Mesa, CA). Nguyên lý cơ bản cho vận tốc "
        "song song chùm laser, nhưng Polytec PI cũng có thiết bị dùng ánh sáng tán xạ cho phép đo vận tốc trong "
        "mặt phẳng (in-plane), gọi là laser surface velocimeter."))
    b.append(h3("Hệ VISAR", "VISAR System"))
    b.append(p(
        "Một ứng dụng giao thoa khác cho đo hồ sơ vận tốc–thời gian là thiết bị gọi là VISAR — “velocity "
        "interference system for any reflector”. Các hệ giao thoa trước đó đòi hỏi bề mặt phản chiếu đánh bóng "
        "cao và rất ít nghiêng trong thử; VISAR hoạt động được với bề mặt phản chiếu gương hoặc tán xạ, và khá "
        "không nhạy với độ nghiêng bề mặt. Nó phát triển cho nghiên cứu sóng xung kích và đo được tốc độ rất cao. "
        "Tài liệu [3] mô tả chi tiết nguyên lý. Tín hiệu từ VISAR sinh bởi photodiode hay linh kiện nhạy sáng "
        "khác, về bản chất là đo tốc độ biến thiên vân. Cần xử lý thêm dữ liệu để có tốc độ. Độ nhạy qui định "
        "bằng “vân trên mét/giây”, điển hình 100 m/s đến 4000 m/s mỗi vân. Các VISAR đầu tiên là thiết bị phòng "
        "thí nghiệm lắp từng phần; nay có thiết bị thương mại — Valyn International (Albuquerque, NM) chế tạo "
        "VISAR và linh kiện. Hình 16.4 là sơ đồ thử nghiệm; thiết bị đo tốc độ từ 100 m/s đến 10 km/s trở lên. "
        "Tầm đo chuẩn (độ sâu trường ảnh) của VISAR là 12 mm, nhưng có hệ đo trên 10 m. Ứng dụng: vận tốc đạn "
        "trong nòng, vận tốc tấm bay (flyer plate), vận tốc lá kim (flying foil), phương trình trạng thái Hugoniot, "
        "và đáp ứng kết cấu với tải xung kích."))
    b.append(fig(4, F.fig(4)))

    b.append(h3("Thiết bị địa chấn", "Seismic Devices"))
    b.append(p(
        "Các thiết bị phần trước đòi hỏi một mối liên kết nào đó giữa tham chiếu và vật chuyển động; thiết bị địa "
        "chấn không cần điều đó. Nó là cảm biến dựa trên một khối lượng gắn với đế cảm biến bằng lò xo tuyến "
        "tính, thường có giảm chấn nhớt; đế gắn vào bề mặt cần đo chuyển động, còn chuyển động của khối lượng địa "
        "chấn so với đế được ghi bằng cảm biến chuyển động. Hình 16.5 trình bày các bộ phận chính. Dùng phương "
        "trình chuyển động của khối lượng địa chấn cho phép xác định chuyển động của đế từ hàm chuyển động tương "
        "đối."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Nếu cảm biến chuyển động trong thiết bị địa chấn đo độ dịch chuyển của khối so với đế, đầu ra của nó tỉ "
        "lệ với gia tốc của đế trong một dải tần nhất định và gọi là gia tốc kế. Đo gia tốc bằng loại này (hoặc "
        "các gia tốc kế khác) cho phép xác định hàm vận tốc–thời gian bằng tích phân qua phương trình (16.3), "
        "với a_y(t) lấy từ đầu ra gia tốc kế. Sự đơn giản của ý tưởng này rõ ràng, và vì tích phân là quá trình "
        "làm trơn, nhiễu do số hóa gặp ở phương pháp “vi phân vị trí” không xuất hiện. Tuy nhiên các sai số "
        "khác có thể lọt vào. Thứ nhất, tốc độ ban đầu V_y(tᵢ) phải biết tại thời bắt đầu; vì nó cộng vào độ "
        "tăng tốc độ, một sai số ở đây sẽ là hằng số trên mọi giá trị. Thứ hai, một độ lệch (zero shift) hay "
        "thiên áp trong tín hiệu gia tốc kế sẽ bị coi là gia tốc không đổi, sinh sai số tăng tuyến tính theo "
        "thời gian — độ lệch này có thể từ đặc tính điện/nhiệt của mạch, hoặc từ gia tốc trọng trường 1 g khi "
        "đo va chạm sau rơi tự do. Thứ ba, nếu thành phần tần số của gia tốc nằm ngoài băng thông dùng được của "
        "gia tốc kế và mạch ghi, sẽ có lỗi gia tốc; tần số cắt thấp phụ thuộc thiết bị ghi và mạch, tần số cắt "
        "cao phụ thuộc tần số tự nhiên và giảm chấn của gia tốc kế cũng như băng thông từng thiết bị. Thứ tư, "
        "lý thuyết gia tốc kế dựa trên kích thích điều hòa, trong khi nhiều ứng dụng đo vận tốc lại là quá trình "
        "transient; hai yếu tố này kết hợp gây dữ liệu gia tốc kế không chính xác (ví dụ rung (ringing) làm sai "
        "tốc độ tính ra), nặng hơn với gia tốc kế giảm chấn nhẹ. Khi buộc dùng phương pháp này, cần một dãy "
        "thử kiểm tra để đánh giá độ chính xác cho hệ cụ thể."))
    b.append(p(
        "Một biến thể là đặt mạch tích phân analog trong gia tốc kế và thực hiện tích phân bằng mạch; khi đó đầu "
        "ra “cảm biến vận tốc” tỉ lệ với độ thay đổi tốc độ. Loại này chịu mọi nguồn lỗi trên; một hãng là "
        "Wilcoxon Research (Gaithersburg, MD). Nếu cảm biến điện cơ trong thiết bị địa chấn cho đầu ra tỉ lệ với "
        "tốc độ giữa hai đầu, thì đầu ra cảm biến địa chấn tỉ lệ với tốc độ của nó trong khung tham chiếu quán "
        "tính (so với mặt đất) với tần số kích thấp cao hơn hẳn chu kỳ tự nhiên của khối lượng. Vì vậy dùng cảm "
        "biến vận tốc tuyến tính làm cảm biến chuyển động trong thiết bị địa chấn biến nó thành “cảm biến vận "
        "tốc địa chấn” — còn gọi là seismometer, geophone, vibrometer hay cảm biến vận tốc. Tần số tự nhiên và "
        "giảm chấn chọn theo ứng dụng; như gia tốc kế, băng thông dùng được phụ thuộc hai đặc tính này. Giới hạn "
        "tần số thấp phụ thuộc độ chính xác cần; phương trình điều khiển (Doebelin [3]) cho thấy nếu cần độ "
        "chính xác 5%, tần số dữ liệu thấp nhất phải gấp 4,6 lần tần số tự nhiên của cảm biến, còn tần số cao "
        "không bị giới hạn — càng cao càng chính xác. Seismometer dùng ghi và nghiên cứu động đất, có thể rất "
        "lớn; chu kỳ tự nhiên 10–50 s, giảm chấn thường chọn 0,7 tới hạn để mở rộng dải tần. Geophone dùng "
        "phổ biến cho logging giếng dầu; chu kỳ tự nhiên khoảng 10 s. Các hãng: Teledyne Brown Engineering và "
        "GeoSpace Corp. (Houston, TX)."))

    # ---- 16.3
    b.append(h2("16.3 Vận tốc góc", "Velocity: Angular"))
    b.append(p(
        "Đo vận tốc góc thường áp dụng cho máy móc quay như bơm, động cơ, máy phát. Đơn vị quen thuộc nhất là "
        "vòng/phút (rpm). Hầu hết trường hợp, đo rpm liên quan đến sinh một chuỗi xung hay sóng sin có tần số "
        "tỉ lệ với vận tốc góc. Các công nghệ dùng chuỗi xung và sóng gồm máy phát tacho một chiều và xoay "
        "chiều, cảm biến quang, cảm biến từ trở biến thiên, cảm biến từ quay, cảm biến hiệu ứng Wiegand, "
        "phương pháp chớp (stroboscopy)... Các đo này lấy theo đế của vật đo — là đo tương đối vì đo chuyển "
        "động giữa hai vật. Một lớp bài toán khác là vật chuyển động hay quán tính; ở đây đo chuyển động tuyệt "
        "đối, cần một tham chiếu cố định (thường là Trái Đất), hoặc tham chiếu phổ quát cho đo thiên văn — "
        "thường là thiết bị con quay (gyroscope)."))

    b.append(h3("Tương đối: Tachometer", "Relative: Tachometer"))
    b.append(h3("Máy phát tacho điện (một chiều và xoay chiều)", "Electrical (dc and ac) Tachometer Generator"))
    b.append(p(
        "Một máy phát quay sinh tín hiệu điện áp tỉ lệ với vận tốc quay trục vào. Máy phát một chiều sinh một "
        "mức điện áp tỉ lệ với tốc độ, như Hình 16.6. Máy phát xoay chiều sinh điện áp xoay chiều có tần số "
        "tỉ lệ với tốc độ quay, như Hình 16.7. Trong động cơ hai pha đơn giản, điện áp xoay chiều đặt vào một "
        "pha và đo ở pha kia. Tần số làm việc điển hình 60 Hz và 400 Hz; tần số mang này nên gấp 5–10 lần tần "
        "số đáp ứng cần của máy phát tacho xoay chiều. Chiều chuyển động xác định bởi pha tín hiệu — hai chiều "
        "ngược nhau lệch 180°. Máy phát một chiều cơ bản ở Hình 16.8."))
    b.append(fig(6, F.fig(6)))
    b.append(fig(7, F.fig(7)))
    b.append(fig(8, F.fig(8)))
    b.append(p(
        "Các nguồn máy phát tacho: GE Company (Fairfield, CT); Kollmorgen Motion Technologies Group (Radford, "
        "VA); Sierracin/Magnedyne (Vista, CA); Micro Mo Electronics (Clearwater, FL)."))
    b.append(h3("Loại đếm xung", "Counter Types"))
    b.append(p(
        "Cả một lớp kỹ thuật đo vận tốc góc dùng xung sinh bởi tương tác điện cơ; điểm chung là bộ đổi xung "
        "thành điện áp cho đầu ra tỉ lệ vận tốc."))
    b.append(h3("Cảm biến từ quay", "Rotating Magnet Sensors"))
    b.append(p(
        "Cảm biến tốc độ thụ động đổi chuyển động cơ thành điện áp xoay chiều không cần nguồn ngoài. Các cảm "
        "biến từ tự cấp này sinh từ trường, khi ở gần vật sắt chuyển động thì sinh điện áp. Khi lắp gần một mục "
        "tiêu sắt (như răng bánh răng trên trục), tần số điện áp ra tỉ lệ với tốc độ quay; bộ đổi tần số–điện "
        "áp chuyển tín hiệu thành điện áp, rồi đổi điện áp thành vận tốc thực. Ứng dụng: tốc độ hộp số, tốc độ động "
        "cơ, quá/tốc độ, tốc độ bánh xe, tốc độ trục bơm, đồng bộ nhiều động cơ, phản hồi điều khiển tốc độ, "
        "vị trí trục khuỷu/thời điểm động cơ, tốc độ ngoại vi máy tính. Đặc tuyến điển hình cho cảm biến từ ở "
        "Hình 16.9. Các hãng: Smith Systems (Brevard, NC); Optek Technology (Carrolton, TX); Allied-Signal "
        "(Morristown, NJ); Baluff (Florence, KY)."))
    b.append(fig(9, F.fig(9)))
    b.append(h3("Cảm biến quang", "Optical Sensors"))
    b.append(p(
        "Phương pháp quang phát hiện vận tốc góc dùng bộ phát và bộ thu ánh sáng; cặp diode phát quang (LED) "
        "với diode nhạy sáng là bố cục phổ biến nhất. Một đĩa có rãnh đặt trên trục quay; mỗi rãnh cho ánh "
        "sáng qua, đầu dò sinh một chuỗi xung có tần số tỉ lệ vận tốc góc. Hình 16.10 minh họa. Phải xét ảnh "
        "hưởng của nguồn sáng ngoài. Các hãng: Scientific Technologies (Fremont, CA); Banner Engineering Corp. "
        "(Minneapolis, MN); Aromat Corp. (New Providence, NJ)."))
    b.append(fig(10, F.fig(10)))
    b.append(h3("Hiệu ứng Hall", "Hall Effect"))
    b.append(p(
        "Hiệu ứng Hall mô tả hiệu điện thế phát sinh dọc theo chiều rộng của vật dẫn có dòng chạy. E.H. Hall "
        "dùng hiệu ứng này năm 1879 để xác định dấu của hạt tải dòng trong vật dẫn. Thiết bị hiệu ứng Hall đang "
        "thâm nhập nhiều ứng dụng cảm biến; điển hình là cảm biến tốc độ bánh xe cho phanh ABS ô tô. Cảm biến "
        "bánh răng hiệu ứng Hall Allegro ATS632LSC (Hình 16.11) là một IC/magneto tối ưu hóa; nó gồm một vỏ "
        "nhựa chịu nhiệt giữ một nam châm samarium–coban phức hợp, một IC hiệu ứng Hall tự hiệu chuẩn và bộ "
        "điều áp. Nguyên lý mạch ở Hình 16.12."))
    b.append(fig(11, F.fig(11)))
    b.append(fig(12, F.fig(12)))
    b.append(h3("Hiệu ứng Wiegand", "Wiegand Effect"))
    b.append(p(
        "Hiệu ứng Wiegand dùng cho cảm biến tiếp cận, tachymetry, mã hoá trục quay và đo tốc độ trong các ứng "
        "dụng như: đánh chỉ mục từ xa cho đồng hồ nước/khí/điện và hệ đo từ xa; đo tốc độ trục động cơ và máy "
        "móc; tachometer, đồng hồ tốc độ và các thiết bị đếm quay. Công nghệ này dùng tính chất từ đặc biệt của "
        "dây sắt từ đường kính nhỏ được xử lý riêng. Bằng cách làm đảo đột ngột từ trường của dây, một xung "
        "điện áp sắc nét sinh ra — gọi là xung Wiegand. Cảm biến dùng hiệu ứng này chỉ cần vài linh kiện đơn "
        "giản để sinh xung điện áp sắc nét khi từ trường ứng dụng thay đổi. Chúng gồm một đoạn dây Wiegand ngắn, "
        "một cuộn cảm và các từ trường xen kẽ thường từ nam châm vĩnh cửu. Ưu điểm chính: không cần nguồn "
        "ngoài, hai dây, không tiếp xúc, tốc độ xung 20 kHz, xung điện áp mức cao, dải nhiệt rộng (−40°C đến "
        "+125°C). Khi từ trường xen kẽ đủ mạnh tác dụng, từ thông lõi dây đảo cực rồi nghịch đảo, sinh xung "
        "Wiegand (Hình 16.13); tác động từ trường sinh điện áp cảm ứng qua cuộn thu/~10 µs. Các từ trường này "
        "thường từ nam châm gắn trên thiết bị quay hay di chuyển, hoặc từ đầu đọc tĩnh và dây Wiegand động, "
        "hoặc từ trường xoay chiều."))
    b.append(fig(13, F.fig(13)))

    b.append(h3("Tuyệt đối: Cảm biến tốc độ góc", "Absolute: Angular Rate Sensors"))
    b.append(h3("Con quay (Gyroscopes)", "Gyroscopes"))
    b.append(p(
        "Nhiều thiết bị đo tốc độ góc tuyệt đối thuộc nhóm con quay. Con quay cơ khí gồm một khối lượng quay "
        "(thường là đĩa/bánh xe) lắp trên đế sao cho trục nó tự do quay một hoặc nhiều hướng và giữ nguyên hướng "
        "bất chấp chuyển động của đế. Cần phân biệt con quay vận tốc góc và con quay tích phân tốc độ: con quay "
        "vận tốc góc đo chuyển động và làm tín hiệu vào hệ ổn định; con quay tích phân tốc độ là cơ sở cho hệ "
        "dẫn đường quán tính chính xác, cho phép một mặt phẳng ổn định giữ attitude tham chiếu. Chúng có thể "
        "rất phức tạp; ba con quay thường ghép với ba gia tốc kế tích phân kép để đo chuyển động tuyệt đối của "
        "phương tiện. Ricardo Dao (Humphrey Inc.) có bài so sánh năm công nghệ trong Measurements & Control "
        "[14]; tóm tắt dưới đây."))
    b.append(h3("Khối lượng quay", "Spinning mass"))
    b.append(p(
        "Con quay truyền thống gồm một bánh xe quay trong khung có khớp gập (gimbaled). Nguyên lý bảo toàn "
        "mômen động lượng là công cụ đo."))
    b.append(h3("Dòng chất lưu (Fluidic)", "Fluidic"))
    b.append(p(
        "Một chùm khí heli phụt qua hai sợi vonfram mỏng [14]; hai sợi đóng vai trò hai nhánh cầu Wheatstone. "
        "Khi đứng yên, luồng khí làm mát hai sợi bằng nhau và cầu cân bằng, đầu ra không. Khi có chuyển động "
        "góc, một sợi gặp luồng lớn hơn, sợi kia nhỏ hơn; điện trở hai sợi đổi và cầu mất cân bằng, sinh điện "
        "áp tỉ lệ vận tốc góc. Một bơm (tinh thể áp điện hình đĩa tròn kích bằng mạch ngoài) tuần hoàn khí "
        "heli thành luồng laminar tốc độ cao qua hai sợi cảm biến song song."))
    b.append(h3("Rung áp điện", "Piezoelectric vibration"))
    b.append(p(
        "Nhiều cảm biến vận tốc góc dùng phần tử thạch anh vi cơ (micromachined). Dù hình dạng khác nhau, "
        "nguyên lý vận hành tương tự: phần tử thạch anh rung ở tần số tự nhiên; chuyển động góc sinh một rung "
        "thứ cấp, khi giải điều biến thì tỉ lệ với dao động góc. Họ sản phẩm QRS và GyroChip™ dùng một nĩa "
        "thạch anh rung kép để cảm nhận vận tốc góc [15,16]. Dùng hiệu ứng Coriolis, chuyển động quay quanh "
        "trục dọc cảm biến sinh một điện áp một chiều tỉ lệ tốc độ quay. Hình 16.14: cảm biến gồm một nĩa "
        "thạch anh hai đầu vi cơ và kết cấu đỡ, all được gia công hóa học từ một tấm thạch anh đơn tinh thể "
        "án áp điện (giống tinh thể đồng hồ). Mỗi chân truyền động có một lực Coriolis tác dụng:"))
    b.append(eq("F = 2 m · Ω × V_r", ""))
    b.append(p(
        "với m là khối lượng chân, V_r vận tốc hướng kính tức thời, Ω tốc độ vào. Lực này vuông góc với cả tốc "
        "độ vào và vận tốc hướng kính. Hai chân truyền động chuyển ngược chiều, lực sinh ra vuông góc mặt phẳng "
        "nĩa và ngược chiều, tạo một mômen tỉ lệ tốc độ quay vào. Vì V_r là sin, mômen cũng sin cùng tần số "
        "chân truyền động và cùng pha với V_r. Chân thu đáp ứng mômen dao động bằng cách lắc ra/vào mặt phẳng, "
        "sinh tín hiệu tại bộ khuếch đại thu; sau giải điều biến thành tín hiệu một chiều tỉ lệ góc quay. Tín "
        "hiệu GyroChip™ đảo dấu khi tốc độ vào đảo — nhờ mômen Coriolis đảo pha khi đổi chiều quay; và nó chỉ "
        "cảm nhận được tốc độ không thực sự (zero rate) quanh trục đối xứng nĩa."))
    b.append(fig(14, F.fig(14)))
    b.append(h3("Hiệu ứng từ thuỷ động lực học (MHD)", "MHD effect"))
    b.append(p(
        "Cảm biến tốc độ góc từ thuỷ động lực học đo dao động góc trong dải 1 Hz–1000 Hz; dùng nơi có xung "
        "kích mạnh và tốc độ góc cao (10–250 rad/s). Nó không đo được vận tốc không đổi (dc). Nguyên lý ở Hình "
        "16.15 [17,18]: một nam châm vĩnh cửu gắn trên vỏ cảm biến; khi vỏ quay, sinh từ trường chuyển động (B). "
        "Bên trong có chất lỏng dẫn điện; khi vỏ quay, chất lỏng theo quán tính đứng yên (định luật Newton I), "
        "tạo chuyển động tương đối (U) giữa từ trường và dòng dẫn. Theo định luật Faraday, chuyển động này sinh "
        "điện áp (E) qua dòng dẫn tỉ lệ vận tốc tương đối. Vì chất lỏng bị ràng buộc chuyển động trên đường "
        "tròn, tín hiệu điện áp tỉ lệ vận tốc góc quanh trục tâm; do ràng buộc này, cảm biến không nhạy chuyển "
        "động tuyến tính. Điện áp được khuếch đại qua biến áp hay bộ khuếch đại để ra thiết bị đo."))
    b.append(fig(15, F.fig(15)))
    b.append(h3("Sợi quang / laser", "Fiber optic/laser"))
    b.append(p(
        "Một chùm sáng hướng vòng quanh trục quay; độ lệch pha của chùm quang hay laser được phát hiện để đo "
        "vận tốc góc. Nguyên lý tương tự dịch chuyển Doppler."))
    b.append(h3("Gia tốc kế hiệu và tích phân", "Differenced and integrated accelerometers"))
    b.append(p(
        "Một mảng gia tốc kế có thể đo chuyển động góc. Đầu ra các gia tốc kế được hiệu khi chúng thẳng hàng, "
        "hoặc cộng khi lắp ngược chiều; phép hiệu loại bỏ thành phần chuyển động tuyến tính. Như Hình 16.16, "
        "độ lớn tín hiệu hiệu (a₁, a₂) chia cho khoảng cách l giữa hai cảm biến cho gia tốc góc; gia tốc góc "
        "tích phân theo thời gian cho vận tốc góc. Cần xét cùng các vấn đề như khi tích phân ở phần tuyến tính; "
        "giả thiết có kết cấu lắp cứng giữa hai gia tốc kế. Kỹ thuật này thường áp dụng cho thử va chạm hình "
        "nhân trạng (ATD) trong thử nghiệm an toàn ô tô và hệ thống thoát hiểm hàng không."))
    b.append(eq("ω = (1/l) · ∫ (a₁ − a₂) dt", ""))
    b.append(fig(16, F.fig(16)))

    # ---- 16.4
    b.append(h2("16.4 Kết luận", "Conclusion"))
    b.append(p(
        "Nhưng, như Poincaré [20] đã nói, không có cách nào xác định được vận tốc tuyệt đối. Sự đo vận tốc "
        "luôn liên hệ với một tham chiếu — và tham chiếu đó, dù là mặt đất, một trục quay, một vì sao hay một "
        "khung quán tính, đều do phương pháp đo và ngữ cảnh quyết định."))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>J. W. Dally, W. F. Riley, and K. G. McConnell, <i>Instrumentation for Engineering Measurements</i>, New York: John Wiley &amp; Sons, 1984.</li>'
             '<li>A. Hudson and R. Nelson, <i>University Physics</i>, New York: Harcourt Brace Jovanovitch, 1982.</li>'
             '<li>E. O. Doebelin, <i>Measurement Systems</i>, 4th ed., New York: McGraw-Hill, 1990.</li>'
             '<li>Trans-Tek, Inc., [Online], 1998. Available http://transtekinc.com/lvt.htm</li>'
             '<li>L. M. Barker and R. E. Hollenbach, Laser interferometer for measuring high velocities of any reflecting surface, <i>J. Appl. Phys.</i>, 43(11), 1972.</li>'
             '<li>Valyn International, [Online], 1998. Available www.valynvisar.com</li>'
             '<li>L. C. Rodman, J. H. Bell, and R. D. Mehta, A 3-component laser-doppler velocimeter data acquisition and reduction system, NASA contractor report; NASA CR-177390.</li>'
             '<li>E. A. Loew, <i>Direct and Alternating Currents</i>, 3rd edition, New York: McGraw-Hill, 1946.</li>'
             '<li>P. Emerald, Low duty cycle operation of hall effect sensors for circuit power conservation, <i>Sensors</i>, 15(3), 1998.</li>'
             '<li>Allegro MicroSystems, Inc., [Online], 1998. Available http://www.allegromicro.com/</li>'
             '<li>The Hall effect sensor: basic principles of operation and application, <i>Sensors</i>, May 1988.</li>'
             '<li>J. B. Scarborough, <i>The Gyroscope: Theory and Applications</i>, New York: Interscience, 1958.</li>'
             '<li>R. F. Deimel, <i>Mechanics of the Gyroscope: The Dynamics of Rotation</i>, New York: Dover Publications, 1950.</li>'
             '<li>E. Dao, Fluidic angular rate sensors, <i>Measurements &amp; Control</i>, February 1994, 126-131.</li>'
             '<li>Systron Donner Inertial Division, [Online], 1998. Available http://www.systron.com</li>'
             '<li>S. Orloski and B. Zimmerman, Dead reckoning in an emergency vehicle location system using a quartz rotation sensor and GPS, <i>Proc. Sensor Expo</i>, Chicago, IL, September 1995, Peterborough, NH: Helmers Publishing, 1995.</li>'
             '<li>G. Kulikovskiy and G. A. Lyubimov, <i>Magnetohydrodynamics</i>, Reading, MA: Addison-Wesley, 1965.</li>'
             '<li>Applied Technology Associates, [Online], 1998. Available http://www.aptec.com/bus-opp.html</li>'
             '<li>G. Unger et al., NASA’s first in-space optical gyroscope: a technology experiment on the X-ray timing Explorer spacecraft, NASA technical memorandum; 109242.</li>'
             '<li>R.P. Feynman, R.B. Leighton, and M. Sands, <i>The Feynman Lectures on Physics</i>, Reading, MA: Addison-Wesley, 1963, 15-5.</li>'
             '</ol>')

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 15</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This chapter is a companion to the Vietnamese translation of Chapter 16 on velocity measurement. All "
        "sixteen figures are redrawn as vectors, and the governing equations (16.1–16.4, the Coriolis force, "
        "and the differenced-accelerometer relation) are reproduced. The translation prose is not repeated here."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Linear velocity is the time rate of change of position — a vector whose magnitude is speed. Angular "
        "velocity is the analogous rate for rotation; the reference frame is set by the measurement method. "
        "The chapter opens with the kinematic definitions: average speed over t₁–t₂ is v_avg = (y₂−y₁)/(t₂−t₁) "
        "(Eq. 16.1), and in the limit the instantaneous velocity is V_y = dy/dt (Eq. 16.2), the slope of the "
        "position–time curve. Because acceleration is the rate of change of velocity, speed follows from "
        "integration: V_y(t) = V_y(tᵢ) + ∫ a_y(t) dt (Eq. 16.3). Figure 16.1 shows the position–time graph and "
        "the secant whose slope is v_avg."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Reference-based methods measure both the moving object and the reference frame. Examples: two spaced "
        "pickups (muzzle velocity), stroboscopic photography, high-speed video, and differentiating a "
        "displacement record (noisy). A linear velocity transducer is essentially a linear generator: a coil "
        "cutting the field of a permanent magnet induces e_i ∝ B·L·V (Eq. 16.4), shown in Figure 16.2. A dc "
        "tach-generator on a rack-and-pinion converts linear to angular speed; the same principle drives an "
        "automobile speedometer."))
    b.append(p(
        "The Doppler shift — an apparent frequency change when source and observer move relative to each other "
        "— works for sound, light, or microwaves. Radar and laser-Doppler vibrometers exploit it; VISAR uses "
        "interferometry on any reflecting surface for very high speeds. Figures 16.3 (Michelson interferometer) "
        "and 16.4 (VISAR fiber-optic setup) illustrate the optical methods. Note the chapter text mislabels the "
        "shifts (calling approach a “red shift”); the correct convention is blue shift on approach, red shift "
        "on recession — consistent with its own train-whistle example."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Seismic devices need no link to a reference frame. A spring-suspended seismic mass in a housing gives, "
        "via a secondary transducer, an output proportional to base acceleration over a band — an accelerometer. "
        "Integrating acceleration (Eq. 16.3) yields velocity, avoiding the noise of differentiation but "
        "introducing sensitivity to the unknown initial speed, bias/zero-shift, and bandwidth limits. A "
        "velocity-proportional output (geophone, vibrometer) results when the motion transducer itself is a "
        "linear velocity transducer; the usable low-frequency limit for 5% accuracy is 4.6× the natural "
        "frequency. Figure 16.5 shows the seismic instrument."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Angular velocity is usually measured as a pulse train or sine wave whose frequency is proportional to "
        "rotational speed. Relative methods (with respect to the body’s base) include dc/ac tach-generators "
        "(Figures 16.6–16.8), rotating-magnet sensors (Figure 16.9), optical slotted-disk sensors (Figure "
        "16.10), Hall-effect gear-tooth sensors (Figures 16.11–16.12), and Wiegand-effect sensors (Figure "
        "16.13). Absolute methods use gyroscopes: spinning mass, fluidic, the piezoelectric Coriolis tuning "
        "fork (Figure 16.14, force F = 2m·Ω×V_r), the magnetohydrodynamic sensor (Figure 16.15), fiber-optic, "
        "and differenced-and-integrated accelerometers (Figure 16.16, ω = (1/l)∫(a₁−a₂)dt). The chapter closes "
        "with Poincaré’s observation that absolute velocity cannot be determined."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(fig(7, F.fig(7), "en"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(fig(10, F.fig(10), "en"))
    b.append(fig(11, F.fig(11), "en"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))
    b.append(fig(15, F.fig(15), "en"))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "The chapter lists 20 references (Dally/Riley/McConnell, Doebelin, Barker &amp; Hollenbach on laser "
        "interferometry, Valyn on VISAR, Allegro on Hall sensors, Deimel and Scarborough on gyroscopes, Dao on "
        "fluidic rate sensors, Kulikovskiy &amp; Lyubimov on MHD, and Feynman’s Lectures) — reproduced in the "
        "Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 15</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 16 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 16 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 16 “Đo vận tốc” của Charles P. Pinney và William E. Baker — vận tốc "
            "tuyến tính (tham chiếu, Doppler, giao thoa, VISAR, địa chấn) và vận tốc góc (tachometer, cảm "
            "biến từ/quang/Hall/Wiegand, con quay Coriolis/MHD), với 16 hình và phương trình 16.1–16.4." if vi else
            "Companion to Chapter 16 of the CRC Measurement Handbook — velocity measurement, linear and angular, "
            "with all sixteen figures and equations 16.1–16.4.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 16' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 16' % BASE_EN)
    meta = ("Chương 16 · theo Ch16.pdf (CRC Press, 1999) · 16 hình, 20 tài liệu tham khảo" if vi
            else "Chapter 16 · 16 figures, 20 references")
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
