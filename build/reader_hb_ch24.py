# -*- coding: utf-8 -*-
"""Handbook Chapter 24 — Torque and Power Measurement
(Ivan J. Garshelis, Magnova, Inc.).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch24.py
"""
import os

import hb24fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch24-torque-and-power-measurement"
TITLE_EN = "Torque and Power Measurement"
TITLE_VI = "Đo mômen xoắn và công suất"
BYLINE = "Ivan J. Garshelis · Magnova, Inc."
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch23-force-measurement"
PREV_VI = "ch23-force-measurement"
PREV_T_EN = "Force Measurement"
PREV_T_VI = "Đo lực"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-24-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Mômen xoắn, tốc độ và công suất là những đại lượng cơ học đặc trưng gắn với hiệu năng chức "
        "năng của máy quay. Khả năng đo chính xác các đại lượng này là điều kiện thiết yếu để xác định "
        "hiệu suất của một máy và để thiết lập những chế độ vận hành vừa an toàn vừa thuận lợi cho tuổi "
        "thọ dài và độ tin cậy cao. Đo trực tuyến các đại lượng này cho phép điều khiển theo thời gian "
        "thực, giúp bảo đảm tính ổn định của chất lượng sản phẩm, và có thể đưa ra những dấu hiệu sớm về "
        "các sự cố sắp xảy ra. Đo mômen xoắn và công suất được dùng khi thử nghiệm các thiết kế tiên "
        "tiến của máy mới và khi phát triển các chi tiết máy mới. Đo mômen xoắn cũng là cơ sở đã được "
        "khẳng định để điều khiển và kiểm tra độ siết chặt của nhiều loại mối ghép ren. Chương này trình "
        "bày các khái niệm cơ bản cùng các phương pháp và thiết bị đang được dùng để đo mômen xoắn và "
        "công suất; việc đo tốc độ, hay chính xác hơn là vận tốc góc, được trình bày ở một chương khác "
        "trong sổ tay này [1]."))

    # ------------------------------------------------------------ 24.1
    b.append(h2("24.1 Những khái niệm cơ bản", "Fundamental Concepts"))

    b.append(h3("24.1.1 Dịch chuyển, vận tốc và gia tốc góc",
                "Angular Displacement, Velocity, and Acceleration"))
    b.append(p(
        "Khái niệm chuyển động quay có thể được hình thức hóa một cách dễ dàng: mọi điểm trong một vật "
        "rắn đang quay đều chuyển động trong những mặt phẳng song song hoặc trùng nhau, đồng thời luôn "
        "giữ khoảng cách không đổi tới một đường thẳng gọi là trục. Trong một vật rắn tuyệt đối, mọi "
        "điểm cũng luôn giữ khoảng cách không đổi với nhau. Chuyển động quay được nhận biết như sự thay "
        "đổi vị trí góc của một điểm quy chiếu trên vật, tức là dịch chuyển góc Δθ của điểm đó trong một "
        "khoảng thời gian Δt nào đó. Chuyển động của điểm ấy, và do đó của toàn bộ vật, được đặc trưng "
        "bởi chiều quay theo chiều kim đồng hồ (CW) hay ngược chiều kim đồng hồ (CCW) và bởi vận tốc "
        "góc ω = Δθ/Δt. Nếu trong khoảng thời gian Δt vận tốc góc thay đổi một lượng Δω, vật đang có "
        "gia tốc góc α = Δω/Δt. Khi góc đo bằng radian và thời gian bằng giây, đơn vị của ω là radian "
        "trên giây (rad s<sup>−1</sup>) và của α là radian trên giây bình phương (rad s<sup>−2</sup>). "
        "Vận tốc góc thường được gọi là tốc độ quay và được đo bằng số vòng quay hoàn chỉnh trên phút "
        "(rpm) hoặc trên giây (rps)."))

    b.append(h3("24.1.2 Lực, mômen xoắn và cân bằng", "Force, Torque, and Equilibrium"))
    b.append(p(
        "Chuyển động quay, cũng như chuyển động nói chung, được điều khiển bởi các lực theo các định "
        "luật Newton. Vì một lực chỉ trực tiếp ảnh hưởng tới thành phần chuyển động nằm trên đường tác "
        "dụng của nó, nên các lực — hoặc các thành phần lực — tác dụng trong bất kỳ mặt phẳng nào chứa "
        "trục đều không tạo ra xu hướng quay quanh trục đó. Chuyển động quay chỉ có thể được khởi tạo, "
        "thay đổi vận tốc hoặc kết thúc bởi một lực tiếp tuyến F<sub>t</sub> tác dụng tại một khoảng "
        "cách hướng tâm hữu hạn l tính từ trục. Hiệu quả của những lực như vậy tăng theo cả "
        "F<sub>t</sub> lẫn l; do đó tích của chúng, được gọi là mômen, chính là đại lượng tác động gây "
        "ra chuyển động quay. Mômen lấy đối với trục quay tạo thành một mômen xoắn. Hình 24.1(a) biểu "
        "diễn một lực F tác dụng lệch một góc β so với tiếp tuyến tại điểm P, cách trục một khoảng l "
        "(cánh tay đòn). Mômen xoắn T được xác định từ thành phần tiếp tuyến của F như sau:"))
    b.append(eq("T = (F cos β) l = F<sub>t</sub> l", "24.1"))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Hiệu ứng tổng hợp, gọi là hợp lực mômen, của một số bất kỳ mômen xoắn tác dụng tại những vị trí "
        "khác nhau dọc theo một vật được tìm từ tổng đại số của chúng, trong đó các mômen có xu hướng "
        "làm vật quay theo chiều CW và CCW được gán dấu ngược nhau. Lực, và do đó mômen xoắn, phát "
        "sinh từ tiếp xúc vật lý với các vật rắn khác, từ tương tác chuyển động với chất lưu, hoặc từ "
        "các trường lực hấp dẫn (kể cả quán tính), điện hoặc từ. Nguồn của mỗi mômen xoắn như vậy phải "
        "chịu một mômen phản lực có độ lớn bằng nó nhưng hướng ngược lại. Với lực đo bằng newton và "
        "khoảng cách đo bằng mét, Phương trình 24.1 cho thấy đơn vị của mômen xoắn là newton mét "
        "(N·m)."))
    b.append(p(
        "Một mômen tổng hợp khác không sẽ khiến vật có một gia tốc góc tỉ lệ với nó, xác định bằng cách "
        "áp dụng định luật thứ hai của Newton:"))
    b.append(eq("T = I α", "24.2"))
    b.append(p(
        "trong đó I, có đơn vị kilôgam mét bình phương (kg·m<sup>2</sup>), là mômen quán tính của vật "
        "đối với trục (tức mômen quán tính cực của vật). Phương trình 24.2 áp dụng được cho mọi vật, "
        "bất kể trạng thái chuyển động của nó. Khi α = 0, Phương trình 24.2 cho thấy T cũng bằng không; "
        "khi ấy vật được gọi là ở trạng thái cân bằng. Để một vật ở trạng thái cân bằng, phải có hoặc "
        "nhiều hơn một mômen tác dụng, hoặc không có mômen nào cả."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Trong bản PDF gốc, Phương trình 24.2 bị lỗi trích xuất và hiện "
        "ra dưới dạng chuỗi ký tự rời rạc; dạng chuẩn của định luật thứ hai Newton cho chuyển động quay "
        "là T = Iα, và đó là dạng được trình bày ở đây. Các Phương trình 24.3–24.5 cũng bị phân mảnh "
        "tương tự trong bản gốc và đã được phục dựng theo dạng chuẩn của sức bền vật liệu."))

    b.append(h3("24.1.3 Ứng suất, độ cứng và biến dạng", "Stress, Rigidity, and Strain"))
    b.append(p(
        "Bất kỳ phần nào của một vật rắn đang cân bằng cũng đều cân bằng; do đó, như một điều kiện cho "
        "sự cân bằng của phần ấy, mọi mômen tác dụng lên nó từ các nguồn bên ngoài phải được cân bằng "
        "bởi những mômen nội lực có độ lớn bằng và hướng ngược lại, đến từ các phần kề cận của vật. "
        "Mômen nội lực được truyền giữa các phần kề cận nhờ tác dụng tập thể của các ứng suất trên mặt "
        "cắt chung của chúng. Trong một vật rắn có mặt cắt tròn (ví dụ một trục điển hình), ứng suất "
        "tiếp τ biến thiên tuyến tính từ không tại trục tới giá trị cực đại tại bề mặt. Ứng suất tiếp "
        "τ<sub>m</sub> tại bề mặt của một trục có đường kính d đang truyền mômen xoắn T được xác định "
        "từ:"))
    b.append(eq("τ<sub>m</sub> = 16T / (π d<sup>3</sup>)", "24.3"))
    b.append(p(
        "Vật liệu thực không phải là tuyệt đối cứng mà có một môđun độ cứng G, biểu thị tỉ số hữu hạn "
        "giữa τ và biến dạng trượt γ. Vì vậy, biến dạng cực đại trong một trục tròn đặc cũng xuất hiện "
        "tại bề mặt của nó và có thể được xác định từ:"))
    b.append(eq("γ<sub>m</sub> = τ<sub>m</sub> / G = 16T / (π d<sup>3</sup> G)", "24.4"))
    b.append(p(
        "Hình 24.1(b) biểu diễn sự thể hiện của biến dạng trượt dưới dạng một dịch chuyển góc giữa các "
        "mặt cắt cách nhau theo phương trục. Trên chiều dài L, trục tròn đặc được vẽ ở hình sẽ bị mômen "
        "xoắn làm xoắn một góc φ xác định từ:"))
    b.append(eq("φ = 32 L T / (π d<sup>4</sup> G)", "24.5"))

    b.append(h3("24.1.4 Công, năng lượng và công suất", "Work, Energy, and Power"))
    b.append(p(
        "Nếu trong thời gian tác dụng của một mômen xoắn T, vật quay được một góc θ, thì một công cơ "
        "học:"))
    b.append(eq("W = T θ", "24.6"))
    b.append(p(
        "được thực hiện. Nếu mômen xoắn tác dụng cùng chiều CW hoặc CCW với dịch chuyển, công được coi "
        "là thực hiện <i>lên</i> vật; ngược lại, công do vật thực hiện. Công thực hiện lên vật làm vật "
        "tăng tốc, do đó thể hiện thành sự gia tăng động năng (KE = Iω<sup>2</sup>/2). Công do vật thực "
        "hiện làm vật giảm tốc, kèm theo sự giảm động năng tương ứng. Nếu vật không tăng tốc, mọi công "
        "thực hiện lên nó tại một vị trí phải được nó thực hiện tại một vị trí khác. Công và năng lượng "
        "đều được đo bằng đơn vị gọi là jun (J). Phương trình 24.6 cho thấy 1 J tương đương với "
        "1 N·m·rad, và vì radian là một tỉ số không thứ nguyên nên đại lượng này ≡ 1 N·m. Để tránh nhầm "
        "lẫn với mômen xoắn, nên định lượng công cơ học bằng đơn vị m·N, hoặc tốt hơn nữa là bằng J."))
    b.append(p(
        "Tốc độ thực hiện công được gọi là công suất, P. Nếu một mômen xoắn T tác dụng trong một khoảng "
        "thời gian nhỏ Δt, trong đó có một dịch chuyển góc Δθ, thì công bằng TΔθ được thực hiện với tốc "
        "độ TΔθ/Δt. Thay Δθ/Δt bằng ω, công suất được xác định đơn giản như sau:"))
    b.append(eq("P = T ω", "24.7"))
    b.append(p(
        "Đơn vị của công suất suy ra từ định nghĩa của nó và được đặt một tên riêng là oát (W). "
        "1 W = 1 J s<sup>−1</sup> = 1 m·N s<sup>−1</sup>. Trong lịch sử, công suất còn được đo bằng mã "
        "lực (Hp), với 1 Hp = 746 W. Các vật quay thực chất truyền công suất giữa những vị trí mà tại đó "
        "các mômen xoắn từ nguồn bên ngoài được tác dụng."))

    # ------------------------------------------------------------ 24.2
    b.append(h2("24.2 Bố trí thiết bị đo mômen xoắn và công suất",
                "Arrangements of Apparatus for Torque and Power Measurement"))
    b.append(p(
        "Các Phương trình 24.1 đến 24.7 diễn đạt những cơ sở vật lý cho việc đo mômen xoắn và công "
        "suất. Hình 24.2 minh họa một bố trí đo tổng quát. Thiết bị thực tế được chọn để đáp ứng những "
        "mục đích đo cụ thể. Nói chung, một mômen xoắn dẫn động phát sinh bên trong một thiết bị tại "
        "một vị trí (B trên Hình 24.2) được chống lại bởi một mômen xoắn đối kháng do một thiết bị khác "
        "phát triển tại một vị trí khác (F). Mômen xoắn dẫn động (từ, ví dụ, một động cơ điện, một động "
        "cơ xăng, một tuabin hơi, sức người, v.v.) được nối qua các phần tử nối C, vùng truyền D và các "
        "khớp nối bổ sung E, tới thiết bị được dẫn động (một máy phát điện, một bơm, một máy công cụ, "
        "những mối ghép ren đã ăn khớp, v.v.), nơi mômen xoắn đối kháng được đáp ứng tại F. Mômen xoắn "
        "tại B hoặc tại F là đại lượng cần đo. Những mômen xoắn này có thể được xác định một cách gián "
        "tiếp từ một đại lượng vật lý có tương quan, ví dụ dòng điện hoặc áp suất chất lưu gắn với hoạt "
        "động của thiết bị dẫn động hay được dẫn động, hoặc một cách trực tiếp hơn bằng cách đo mômen "
        "phản lực tại A hoặc G, hay mômen xoắn được truyền qua D. Từ quan hệ nhân quả giữa mômen xoắn "
        "và chuyển động quay, có thể suy ra rằng phần lớn mối quan tâm về mômen xoắn được truyền sẽ "
        "liên quan tới các vật quay."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Trong chừng mực mà khung của các thiết bị dẫn động và được dẫn động cùng các bệ lắp của chúng "
        "vào “đất” là tuyệt đối cứng, phản lực tại A sẽ bằng mômen xoắn tại B ở mọi thời điểm, cũng như "
        "phản lực tại G sẽ bằng mômen xoắn tại F. Trong những điều kiện cân bằng, các đẳng thức này "
        "không phụ thuộc vào độ mềm dẻo của bất kỳ phần tử nào. Cũng trong những điều kiện cân bằng, và "
        "trừ những mômen xoắn ký sinh thường là nhỏ (do, ví dụ, ma sát ổ trục và lực cản không khí trên "
        "các bề mặt chuyển động nhanh), mômen xoắn dẫn động tại B sẽ bằng mômen xoắn đối kháng tại F."))
    b.append(p(
        "Mômen phản lực tại A hoặc G thường được xác định, bằng cách dùng Phương trình 24.1, từ các phép "
        "đo những lực tác dụng tại những khoảng cách đã biết do thiết bị ấn định. Mômen xoắn được truyền "
        "được xác định từ các phép đo, trên một phần tử thích hợp trong vùng D, các đại lượng "
        "τ<sub>m</sub>, γ<sub>m</sub> hoặc φ, rồi áp dụng Phương trình 24.3, 24.4 hoặc 24.5 (hay những "
        "biểu thức tương tự cho các phần tử có mặt cắt không phải tròn đặc [2]). Việc hiệu chuẩn — tức "
        "đo ứng suất, biến dạng hoặc góc xoắn do tác dụng của một mômen xoắn đã biết — làm cho việc "
        "biết bất kỳ chi tiết nào về phần tử trong vùng D trở nên không cần thiết. Khi α ≠ 0 và đo được, "
        "T cũng có thể được xác định từ Phương trình 24.2. Phương pháp này chỉ đòi hỏi những phép đo "
        "quan sát không xâm nhập, nên đặc biệt hữu ích để xác định các mômen xoắn chuyển tiếp; ví dụ "
        "những mômen gắn với các sự kiện đốt cháy trong động cơ đốt trong nhiều xi lanh [3]."))
    b.append(p(
        "Các Phương trình 24.6 và 24.7 chỉ áp dụng được trong khi quay, bởi vì khi không có chuyển động "
        "thì không có công nào được thực hiện và việc truyền công suất bằng không. Phương trình 24.6 có "
        "thể được dùng để xác định mômen xoắn trung bình từ các phép đo nhiệt lượng của nhiệt sinh ra "
        "(bằng công cơ học W) trong một số vòng quay đã được cộng dồn (≡ θ/2π). Phương trình 24.7 được "
        "áp dụng thường xuyên trong đo công suất, trong đó T được xác định bằng những phương pháp dựa "
        "trên Phương trình 24.1, 24.3, 24.4 hoặc 24.5, còn ω được đo bằng bất kỳ phương tiện thích hợp "
        "nào [4]."))
    b.append(p(
        "F, T và φ đôi khi được đo bằng những phương pháp cơ học đơn giản. Ví dụ, một “cờ lê lực” thường "
        "được dùng để siết có điều khiển các mối ghép ren. Trong những dụng cụ này, mômen xoắn được chỉ "
        "thị bằng vị trí của một kim chạy trên một thang chia đã hiệu chuẩn, phản ứng lại độ võng đàn "
        "hồi của một phần tử lò xo — trong trường hợp đơn giản nhất là độ uốn của cán cờ lê [5]. Tổng "
        "quát hơn, người ta dùng những dụng cụ, với các tên gọi khác nhau là cảm biến hay đầu đo, để "
        "biến đại lượng mong muốn (liên quan tới mômen xoắn hoặc tốc độ) thành một tín hiệu điện tỉ lệ "
        "tuyến tính với nó. (Cảm biến lực còn được gọi là load cell.) Việc xác định P thông thường nhất "
        "đòi hỏi nhân hai tín hiệu từ hai cảm biến riêng biệt của T và ω. Một đầu đo, trong đó biên độ "
        "của một tín hiệu duy nhất tỉ lệ với công suất đang được truyền dọc theo một trục, cũng đã được "
        "mô tả [6]."))

    # ------------------------------------------------------------ 24.3
    b.append(h2("24.3 Các công nghệ đầu đo mômen xoắn", "Torque Transducer Technologies"))
    b.append(p(
        "Nhiều tương tác vật lý khác nhau có tác dụng biến F, τ, γ hoặc φ thành những tín hiệu điện tỉ "
        "lệ. Mỗi tương tác đòi hỏi một phần nào đó theo phương trục của trục máy phải được dành riêng "
        "cho chức năng cảm nhận mômen xoắn. Hình 24.3 cho thấy những đặc điểm điển hình của các vùng "
        "cảm nhận ứng với bốn công nghệ cảm nhận đang được dùng hiện nay."))
    b.append(fig(3, F.fig(3), "vi"))

    b.append(h3("24.3.1 Biến dạng bề mặt", "Surface Strain"))
    b.append(p(
        "Hình 24.3(a) minh họa một vùng cảm nhận được cấu hình để biến biến dạng bề mặt "
        "(γ<sub>m</sub>) thành một tín hiệu điện tỉ lệ với mômen xoắn được truyền. Biến dạng bề mặt trở "
        "thành cơ sở then chốt để đo cả lực lẫn mômen xoắn sau khi E. E. Simmons, Jr. và Arthur C. Ruge "
        "phát minh ra gage biến dạng dây dán năm 1938 [7]. Một gage biến dạng hiện đại chỉ đơn giản là "
        "một dây dẫn điện được kéo dài, thường được tạo thành dạng rắn bò (serpentine) trong một lá kim "
        "loại hoặc màng rất mỏng, được dán lên một đế cách điện mỏng. Đế này được gắn, thường bằng keo "
        "dán, lên bề mặt của phần tử chịu tải. Biến dạng được cảm nhận như sự thay đổi điện trở của "
        "gage. Những thay đổi này nói chung quá nhỏ để đo chính xác một cách trực tiếp, nên thông "
        "thường người ta dùng hai đến bốn gage bố trí trong một mạch cầu Wheatstone. Tính độc lập với "
        "tải dọc trục và tải uốn cũng như với các biến thiên nhiệt độ đạt được bằng cách dùng một cầu "
        "bốn gage gồm hai cặp gage biến dạng tương thích đặt đối xứng qua đường kính, mỗi gage định "
        "hướng theo một phương biến dạng chính. Trong các trục tròn (và những hình dạng khác dùng để "
        "truyền mômen xoắn), các biến dạng chính kéo và nén xuất hiện theo những góc 45° so với trục. "
        "Các biến dạng giới hạn, xác định từ Phương trình 24.4 (với τ<sub>m</sub> bằng giới hạn tỉ lệ "
        "trượt của vật liệu trục), hiếm khi vượt quá vài phần trên 10<sup>3</sup>. Cách làm điển hình "
        "là tăng độ mềm dẻo của vùng cảm nhận (ví dụ bằng cách giảm đường kính của nó, hoặc dùng những "
        "mặt cắt rỗng hay có hình dạng đặc biệt) để đạt được biến dạng giới hạn tại giá trị cao nhất "
        "của mômen xoắn cần đo. Điều này làm cực đại hóa độ nhạy của phép đo."))

    b.append(h3("24.3.2 Góc xoắn", "Twist Angle"))
    b.append(p(
        "Nếu trục đủ mảnh (ví dụ L > 5d) thì φ, tại những giá trị giới hạn của τ<sub>m</sub> ứng với các "
        "vật liệu trục điển hình, có thể vượt quá 1°, đủ để phân giải với độ chính xác thích hợp cho "
        "những phép đo mômen xoắn thực tiễn (φ tại τ<sub>m</sub> có thể tìm được bằng cách biến đổi các "
        "Phương trình 24.3, 24.4 và 24.5). Hình 24.3(b) cho thấy một bố trí phổ biến, trong đó mômen "
        "xoắn được xác định từ sự khác biệt về pha răng–khe giữa hai bánh răng “có răng” giống hệt nhau "
        "gắn ở hai đầu đối diện của một “thanh xoắn” mềm dẻo. Độ dịch pha của các tín hiệu điện tuần "
        "hoàn từ hai “đầu thu” tỉ lệ với dịch chuyển ngoại vi của những đặc điểm nổi bật trên hai bánh "
        "răng, và do đó tỉ lệ với góc xoắn của thanh xoắn, và vì vậy tỉ lệ với mômen xoắn. Những đặc "
        "điểm này được chọn sao cho có thể cảm nhận được bằng bất kỳ kỹ thuật không tiếp xúc nào trong "
        "một loạt các kỹ thuật từ, quang hoặc điện dung. Với những đầu thu tinh vi hơn, vị trí góc "
        "tương đối của hai bánh răng hiện ra dưới dạng biên độ của một tín hiệu điện duy nhất, nhờ đó "
        "cho phép đo mômen xoắn ngay cả trên một trục đứng yên (ví dụ [13–15]). Trong những kết cấu "
        "khác nữa, người ta dùng một biến áp dịch chuyển biến thiên gắn trên trục, hoặc một loại thiết "
        "bị điện có liên quan, để cung cấp những tín hiệu đầu ra độc lập với tốc độ và tỉ lệ với φ."))

    b.append(h3("24.3.3 Ứng suất", "Stress"))
    b.append(p(
        "Ngoài biến dạng đàn hồi, những ứng suất mà nhờ đó mômen xoắn được truyền còn thể hiện qua sự "
        "thay đổi tính chất từ của vật liệu trục sắt từ. “Tương tác từ đàn hồi” này [8] tạo ra một cơ sở "
        "vốn không tiếp xúc để đo mômen xoắn. Hiện nay có hai loại đầu đo mômen xoắn từ đàn hồi (đôi khi "
        "được gọi là từ giảo) đang được dùng: loại 1 lấy tín hiệu đầu ra từ những biến thiên do mômen "
        "xoắn gây ra trong từ dẫn của mạch từ; loại 2 tạo ra một từ trường để đáp lại mômen xoắn. Đầu "
        "đo loại 1 thường dùng các kết cấu “nhánh”, “chéo” hoặc “solenoid” [9]. Trong các thiết kế nhánh "
        "và chéo, mômen xoắn được phát hiện như sự mất cân bằng của từ thẩm dọc theo những đường xoắn "
        "ốc 45° trực giao (các phương ứng suất chính) trên bề mặt trục hoặc trên bề mặt của một vật liệu "
        "được gắn thêm vào trục. Trong các kết cấu solenoid, mômen xoắn được phát hiện nhờ sự khác biệt "
        "về từ thẩm theo phương trục của hai vùng bề mặt kề nhau, đã được tạo sẵn những trục từ “dễ” đối "
        "xứng (thường dọc theo các phương ứng suất chính 45°). Trong khi các cảm biến kiểu nhánh và kiểu "
        "chéo dễ được thu nhỏ [10], những biến thiên cục bộ về tính chất từ của bề mặt trục điển hình "
        "lại hạn chế độ chính xác của chúng. Các thiết kế solenoid, được minh họa trên Hình 24.3(c), "
        "tránh được cạm bẫy này bằng cách lấy trung bình một cách hiệu quả những biến thiên ấy. Đầu đo "
        "loại 2 nói chung được chế tạo với một vành bằng vật liệu hoạt động từ đàn hồi gắn cứng vào "
        "trục. Vành này được từ hóa trong quá trình chế tạo đầu đo, thường với mỗi nửa theo phương trục "
        "được phân cực theo một chiều chu vi ngược nhau, như chỉ ra bằng các mũi tên liền trên Hình "
        "24.3(d) [11]. Khi mômen xoắn được tác dụng, các từ độ nghiêng vào những phương xoắn ốc (các mũi "
        "tên đứt nét), làm xuất hiện các cực từ tại vách đômen trung tâm và (với cực tính ngược lại) "
        "tại các mặt đầu của vành. Mômen xoắn được xác định từ tín hiệu đầu ra của một hoặc nhiều cảm "
        "biến từ trường (ví dụ linh kiện Hall, từ điện trở hoặc cổng từ thông) được gắn sao cho cảm nhận "
        "được cường độ và cực tính của từ trường xuất hiện trong không gian gần vành."))

    # ------------------------------------------------------------ 24.4
    b.append(h2("24.4 Kết cấu, vận hành và ứng dụng đầu đo mômen xoắn",
                "Torque Transducer Construction, Operation, and Application"))
    b.append(p(
        "Mặc dù một vùng cảm nhận mômen xoắn có thể được tạo ra trực tiếp trên một trục mong muốn, "
        "thông thường hơn là lắp một đầu đo mômen xoắn kiểu môđun đã được chế tạo sẵn vào đường truyền "
        "động. Các đầu đo loại này có sẵn với dải định mức từ 0,001 N·m đến 200 000 N·m. Những mô tả "
        "nguyên lý hoạt động cùng các chỉ dẫn lắp đặt và vận hành chi tiết có thể tìm thấy trong catalogue "
        "và tài liệu của các nhà chế tạo khác nhau [12–20]. Tên thương mại thường nhận diện loại đầu đo "
        "cụ thể; ví dụ Torquemeters [13] chỉ một họ mô hình gage biến dạng không tiếp xúc; Torkducer® "
        "[18] nhận diện một dòng đầu đo từ đàn hồi loại 1; Torqstar™ [12] nhận diện một dòng đầu đo từ "
        "đàn hồi loại 2; Torquetronic [16] là một lớp đầu đo dùng cảm biến góc xoắn kiểu quấn vòng; và "
        "TorXimitor™ [20] nhận diện các đầu đo gage biến dạng không tiếp xúc dựa trên quang điện tử. "
        "Nhiều thiết bị trong số này có những nét tương đồng chung vượt lên trên công nghệ cảm nhận cụ "
        "thể cũng như dải định mức của chúng. Hình 24.4 minh họa nhiều đặc điểm chung ấy."))
    b.append(fig(4, F.fig(4), "vi"))

    b.append(h3("24.4.1 Những xem xét cơ khí", "Mechanical Considerations"))
    b.append(p(
        "Tốc độ vận hành cực đại biến thiên rất rộng; các giới hạn trên phụ thuộc vào kích thước, "
        "nguyên lý hoạt động, loại ổ trục, chế độ bôi trơn và cân bằng động của cụm quay. Ổ bi, được bôi "
        "trơn bằng mỡ, dầu hoặc sương dầu, là loại điển hình. Những mômen xoắn ký sinh gắn với chất bôi "
        "trơn và phớt của ổ trục hạn chế độ chính xác của các phép đo mômen xoắn ở vùng thấp của thang "
        "đo. (Các mẫu có định mức rất nhỏ không có ổ trục [15].) Bôi trơn cưỡng bức có thể cho phép vận "
        "hành tới 80 000 rpm [16]. Vận hành tốc độ cao đòi hỏi phải xem xét cẩn thận ảnh hưởng của ứng "
        "suất ly tâm lên đại lượng được cảm nhận cũng như các dải tốc độ tới hạn (gây dao động). Những "
        "dao động xoắn gắn với cộng hưởng của độ đàn hồi trục (đặc trưng bởi hằng số lò xo của nó) với "
        "quán tính quay của các khối lượng được nối vào có thể làm hỏng phép đo, làm hỏng đầu đo do "
        "những dao động vượt quá mômen xoắn quá tải định mức của nó, và thậm chí có thể nguy hiểm về "
        "mặt vật lý."))
    b.append(p(
        "Vỏ đầu đo hoặc trôi nổi trên các ổ trục của trục máy, hoặc được gắn cứng. Những vỏ trôi nổi tự "
        "do được giữ không cho quay bằng những phương tiện “mềm” như một dây cáp, một lò xo hoặc một "
        "giá đỡ mềm dẻo, hoặc bằng một đặc điểm ngoại vi lệch tâm tì đơn giản vào một bề mặt cố định. "
        "Trong những lắp đặt trôi nổi tự do, các trục của trục dẫn động và trục được dẫn động phải được "
        "căn chỉnh cẩn thận. Những khớp nối “mềm” cứng vững về xoắn ở mỗi đầu trục được dùng để dung "
        "sai những lệch góc và/hoặc lệch hướng tâm nhỏ. Cách khác, việc dùng hai khớp nối mềm ở một đầu "
        "sẽ cho phép nối trực tiếp đầu kia. Những vỏ được gắn cứng được trang bị chân đế hoặc tai lắp "
        "tương tự những thứ có trên khung của động cơ điện. Các mẫu trôi nổi tự do đôi khi được gắn "
        "cứng bằng những tấm chuyển tiếp bắt vít vào vỏ. Việc gắn cứng được ưa chuộng khi khó hoặc không "
        "thực tế để căn chỉnh các trục dẫn động và được dẫn động, ví dụ khi các máy dẫn động hoặc được "
        "dẫn động được thay đổi thường xuyên. Những vỏ được gắn cứng đòi hỏi phải dùng hai khớp nối mềm "
        "ở cả hai đầu trục."))
    b.append(p(
        "Những đầu đo kiểu môđun được thiết kế cho các ứng dụng không quay hoặc quay hạn chế không cần "
        "ổ trục. Để bảo đảm rằng toàn bộ mômen xoắn tác dụng ở các đầu đều được cảm nhận, điều quan "
        "trọng trong những đầu đo mômen xoắn kiểu “phản lực” như vậy là chỉ giới hạn việc gắn vỏ vào "
        "trục ở một phía của vùng cảm nhận mà thôi. Dù quay hay đứng yên, các đầu trục bên ngoài nói "
        "chung đều bao gồm những chi tiết nối mômen xoắn như mặt phẳng, rãnh then, then hoa, mặt côn, "
        "mặt bích, đầu vuông đực/cái, v.v."))

    b.append(h3("24.4.2 Những xem xét điện", "Electrical Considerations"))
    b.append(p(
        "Về bản chất, đầu đo cần một lượng công suất điện đầu vào hay kích thích nào đó. Tín hiệu đầu ra "
        "“thô” của thiết bị cảm nhận thực tế nói chung cũng cần được “xử lý điều kiện” thành một mức và "
        "một dạng thức thích hợp để hiển thị trên một đồng hồ số hoặc tương tự, hay để đáp ứng những yêu "
        "cầu đầu vào của thiết bị thu thập dữ liệu. Việc kích thích và xử lý tín hiệu được cung cấp bởi "
        "những mạch điện tử được thiết kế phù hợp với đặc tính của công nghệ cảm nhận cụ thể. Ví dụ, các "
        "cầu gage biến dạng thường được cấp nguồn 10 V đến 20 V (một chiều hoặc xoay chiều) và có đầu ra "
        "trong khoảng 1,5 mV đến 3,0 mV trên mỗi vôn kích thích tại tải định mức. Việc nâng những tín "
        "hiệu milivôn này lên những mức dùng được hơn đòi hỏi các bộ khuếch đại có hệ số khuếch đại từ "
        "100 trở lên. Với kích thích xoay chiều, còn cần thêm các bộ dao động và bộ tách sóng (hoặc bộ "
        "chỉnh lưu). Những phần tử mạch loại này là bình thường khi các phần tử cảm ứng được dùng hoặc "
        "như một phần cần thiết của cảm biến, hoặc đơn giản để thực hiện những kết cấu không tiếp xúc."))
    b.append(p(
        "Gage biến dạng, biến áp vi sai và những công nghệ cảm nhận có liên quan đòi hỏi các linh kiện "
        "điện phải được gắn trên phần tử chịu mômen xoắn. Việc đưa công suất điện tới và lấy tín hiệu "
        "đầu ra từ những linh kiện này trên các trục quay đòi hỏi những phương pháp đặc biệt. Cách trực "
        "tiếp và phổ biến nhất là dùng những phương tiện dẫn điện, trong đó các chổi than (thường bằng "
        "than chì bạc) tì vào những vòng trượt (bằng bạc). Tuổi thọ hữu ích được kéo dài bằng cách tạo "
        "phương tiện nâng các chổi than ra khỏi các vòng quay khi không thực hiện phép đo. Một số phương "
        "pháp “không tiếp xúc” cũng được dùng. Ví dụ, công suất có thể được cấp qua ghép cảm ứng giữa "
        "các cuộn dây biến áp đứng yên và quay [12–15], bằng cách chiếu sáng những pin quang điện gắn "
        "trên trục [20], hoặc thậm chí bằng những pin gắn chặt vào trục [21] (bị lực ly tâm hạn chế ở "
        "những tốc độ tương đối thấp). Tín hiệu đầu ra được lấy ra khỏi trục qua các biến áp quay, qua "
        "các LED điều chế tần số (hồng ngoại) [19, 20], hoặc qua đo từ xa bằng tần số vô tuyến (FM) "
        "[21]. Ở những nơi chuyển động quay của trục bị hạn chế không quá vài vòng quay toàn phần, như "
        "trong cơ cấu lái, cơ cấu chấp hành van hoặc các cơ cấu dao động, việc đi dây cứng cho cả mạch "
        "công suất lẫn mạch tín hiệu thường là thích hợp. Cáp mềm dẻo giảm thiểu những mômen xoắn ngẫu "
        "sinh và đem lại tuổi thọ phục vụ dài và tin cậy. Mọi xem xét về đi dây như vậy đều được tránh "
        "khi dùng các công nghệ hoặc kết cấu không tiếp xúc."))

    b.append(h3("24.4.3 Giá cả và các tùy chọn", "Costs and Options"))
    b.append(p(
        "Giá của các đầu đo mômen xoắn phản ánh dải rộng lớn của các định mức sẵn có, các cấp hiệu năng, "
        "các loại, các kiểu, những tính năng tùy chọn và phụ kiện. Nói chung, giá của bất kỳ một loại nào "
        "đều tăng khi định mức tăng. Các loại phản lực có giá khoảng một nửa so với các mẫu quay có cùng "
        "định mức. Một đầu đo gage biến dạng điển hình kiểu chân đế, định mức 565 N·m, với vòng trượt "
        "hoặc biến áp quay và cảm biến tốc độ tích hợp, có độ phi tuyến và độ trễ quy định đều trong "
        "phạm vi ±0,1%, có giá khoảng 4000 USD (năm 1997). Thiết bị đo đi kèm, cung cấp việc kích thích "
        "đầu đo, xử lý điều kiện và đầu ra tương tự cùng hiển thị số mômen xoắn và tốc độ, có giá khoảng "
        "2000 USD. Một đầu đo từ đàn hồi tương đương với độ chính xác ±0,5% có giá khoảng 1300 USD. Các "
        "đầu đo định mức cao dùng cho chế độ tốc độ cực cao với những tùy chọn bôi trơn thích hợp có thể "
        "có giá trên 50 000 USD. Các đầu đo từ đàn hồi loại 2, được sản xuất hàng loạt cho ứng dụng lái "
        "trợ lực ô tô, có giá xấp xỉ 10 USD."))

    # ------------------------------------------------------------ 24.5
    b.append(h2("24.5 Thiết bị đo công suất", "Apparatus for Power Measurement"))
    b.append(p(
        "Máy quay tồn tại dưới vô số loại cụ thể và có thể vận hành ở những mức công suất từ những phần "
        "nhỏ của oát đến vài chục megawatt, một dải trải rộng hơn 10<sup>8</sup>. Thiết bị đo công suất "
        "cũng tồn tại trong một dải loại và kích cỡ rộng tương tự. Công suất cơ học chảy từ một nguồn "
        "dẫn động tới một tải. Công suất này có thể được xác định trực tiếp bằng cách áp dụng Phương "
        "trình 24.7, đơn giản bằng việc đo, ngoài ω, mômen xoắn đầu ra của nguồn dẫn động hoặc mômen "
        "xoắn đầu vào của tải, tùy theo thiết bị nào là đối tượng cần thử (DUT). Khi DUT là một nguồn "
        "dẫn động, người ta thường phải đo trên toàn dải tốc độ và mômen xoắn phục vụ của nó. Do đó "
        "thiết bị thử phải đóng vai một tải điều khiển được và có khả năng hấp thụ công suất được cấp "
        "ra. Tương tự, khi DUT là một bơm, một quạt hay một loại tải khác, hoặc một thiết bị mà chức "
        "năng chỉ là thay đổi tốc độ và mômen xoắn (ví dụ một hộp số), thì thiết bị thử phải bao gồm một "
        "nguồn dẫn động có khả năng cấp công suất trên toàn dải mômen xoắn và tốc độ định mức của DUT. "
        "Công suất cơ học cũng có thể được xác định gián tiếp bằng cách chuyển hóa thành (hoặc từ) một "
        "dạng năng lượng khác (ví dụ nhiệt hoặc điện) và đo những đại lượng nhiệt lượng hoặc điện có "
        "liên quan. Xét đến dải rộng của những phương pháp và thiết bị sẵn có để đo chính xác cả mômen "
        "xoắn lẫn tốc độ, các phương pháp gián tiếp chỉ nên được xem xét khi những hoàn cảnh đặc biệt "
        "làm cho các phương pháp trực tiếp trở nên khó khăn."))
    b.append(p(
        "Dynamometer là tên riêng dành cho thiết bị đo công suất bao gồm phương tiện hấp thụ và/hoặc "
        "dẫn động, và trong đó mômen xoắn được xác định từ các phản lực trên một phần đứng yên (stato). "
        "Một dynamometer hiệu quả có thể được lắp ghép thuận tiện bằng cách gắn DUT theo cách cho phép "
        "đo mômen phản lực trên khung của nó. Hình 24.5 cho thấy một thiết bị được thiết kế để tạo thuận "
        "lợi cho những phép đo như vậy. Các mẫu thương mại (Torque Table® [12]) có định mức đỡ được các "
        "DUT nặng từ 222 N đến 4900 N, với định mức mômen xoắn từ 1,3 N·m đến 226 N·m. Người ta cũng "
        "dùng những “ống mômen” [4] hoặc những cách bố trí gắn DUT khác. Ngoài khả năng có những cộng "
        "hưởng đàn hồi/quay, các hệ thống này không bị hạn chế về tốc độ. Tổng quát hơn, và đặc biệt "
        "đối với máy móc lớn, dynamometer bao gồm một máy dẫn động hoặc hấp thụ chuyên dụng. Những "
        "dynamometer như vậy được phân loại theo chức năng thành hấp thụ hoặc dẫn động (đôi khi gọi là "
        "kiểu động cơ kéo). Một dynamometer vạn năng có thể hoạt động như một nguồn dẫn động hoặc như "
        "một thiết bị hấp thụ."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Thuật ngữ <i>dynamometer</i> được giữ nguyên trong bản dịch này "
        "vì tiếng Việt chưa có cách gọi thống nhất: “băng thử”, “máy đo công suất” và “lực kế” đều được "
        "dùng, nhưng mỗi cách gọi đều che khuất một phần nghĩa. Cần phân biệt dynamometer (thiết bị đo "
        "công suất, thường gồm cả phần hấp thụ hoặc dẫn động) với <i>load cell</i> (cảm biến lực) và với "
        "<i>brake</i> (phanh — một kiểu dynamometer hấp thụ). Trong bản PDF gốc, dải định mức mômen xoắn "
        "của Torque Table® bị in lỗi thứ tự thành “1.3 N·m 226 to N·m”; trị số đúng là 1,3 N·m đến "
        "226 N·m như đã trình bày ở trên."))

    b.append(h3("24.5.1 Dynamometer hấp thụ", "Absorption Dynamometers"))
    b.append(p(
        "Dynamometer hấp thụ, thường được gọi là phanh bởi vì hoạt động của chúng dựa trên việc tạo ra "
        "một mômen xoắn cản điều khiển được, biến công cơ học thành nhiệt. Mômen xoắn cản, khác với mômen "
        "xoắn chủ động, chỉ có thể tác dụng để kìm hãm chứ không thể khởi tạo chuyển động quay. Độ tăng "
        "nhiệt bên trong một dynamometer được kiểm soát bằng cách mang nhiệt năng đi, thường bằng cách "
        "truyền cho một chất lưu chuyển động, điển hình là không khí hoặc nước. Mômen xoắn cản được tạo "
        "ra bởi những quá trình tiêu tán vốn có như: ma sát giữa các bề mặt cọ xát, lực cắt hoặc sự rối "
        "của chất lỏng nhớt, dòng điện, hoặc từ trễ. Gaspard Riche de Prony (1755–1839), năm 1821 [22], "
        "đã phát minh một dạng phanh ma sát rất hữu ích để đáp ứng nhu cầu thử nghiệm những động cơ hơi "
        "nước đang trở nên phổ biến thời ấy. Những phanh thuộc loại này thường được dùng cho mục đích "
        "giảng dạy, vì chúng thể hiện những nguyên lý chung và những xem xét vận hành chính yếu của mọi "
        "loại dynamometer hấp thụ. Hình 24.6 cho thấy dạng cơ bản và những đặc điểm kết cấu của một "
        "phanh prony. Công suất mà bình thường sẽ được trục của động cơ dẫn động truyền cho tải được "
        "(vì mục đích đo) chuyển hóa thay vào đó thành nhiệt, thông qua công thực hiện bởi các lực ma sát "
        "giữa những khối ma sát và vành bánh đà. Việc điều chỉnh độ siết của các bu lông kẹp làm thay "
        "đổi mômen xoắn cản do ma sát theo yêu cầu. Nhiệt được lấy đi khỏi mặt trong của vành bằng những "
        "bố trí (không được vẽ) dùng dòng nước chảy liên tục hoặc sự bay hơi của nước. Không cần biết độ "
        "lớn của các lực ma sát, cũng không cần biết bán kính của bánh đà (những điều mà Prony đã nhận "
        "ra), bởi vì trong khi mômen xoắn cản có xu hướng làm quay cả bộ thiết bị bị kẹp, nó lại được "
        "giữ đứng yên bởi mômen phản lực bằng và ngược chiều F·r. Lực F tại đầu cánh tay đòn có bán kính "
        "r (một kích thước cố định của thiết bị) được theo dõi bằng một cái cân hoặc một load cell. Công "
        "suất được xác định từ các Phương trình 24.1 và 24.7 là P = F·r·ω = F·r·2πN/60, trong đó N tính "
        "bằng rpm."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Những lực hãm không đều gắn với hệ số ma sát dao động nói chung làm cho ma sát trượt trở thành "
        "một cách kém cỏi để tạo mômen xoắn cản. Tuy vậy, vì chúng dễ chế tạo, những biến thể tùy nghi "
        "của phanh prony, thường chỉ dùng dây thừng trần hoặc những thanh gỗ chèn được nối bằng dây hoặc "
        "đai, vẫn được dùng trong phòng thí nghiệm hoặc ở bất cứ nơi nào cần thực hiện những phép đo "
        "công suất không đòi hỏi cao hoặc không thường xuyên. Những kết cấu phanh prony tinh vi hơn được "
        "dùng trong các dynamometer độc lập có bình nước làm mát tự kèm, với kích cỡ tới 746 kW "
        "(1000 Hp), vận hành tới 3600 rpm với mômen xoắn tới 5400 N·m [23]. Có sẵn cả mẫu cố định và "
        "mẫu di động, chúng được dùng để thử những động cơ điện lớn cũng như động cơ và hộp số trên các "
        "xe nông nghiệp. Phanh prony cho phép đặt mômen xoắn cản toàn phần xuống tới tốc độ bằng không."))
    b.append(p(
        "William Froude (1810–1879) [24] đã phát minh một phanh nước (1877) không phụ thuộc vào ma sát "
        "trượt. Mômen xoắn cản bên trong một phanh Froude được phát triển giữa rôto và stato nhờ động "
        "lượng mà rôto truyền cho nước chứa trong vỏ phanh. Chuyển động quay của rôto buộc nước tuần "
        "hoàn giữa những hốc hình chén được đúc trên các mặt đối diện của cả rôto lẫn stato. Rôto được "
        "đỡ trong stato bằng các ổ trục, những ổ này cũng định vị trí theo phương trục của nó. Các phớt "
        "kiểu mê cung ngăn rò rỉ nước đồng thời giảm thiểu ma sát và mài mòn. Vỏ stato được đỡ trong "
        "khung dynamometer theo kiểu giá đỡ bằng các ổ trục chốt. Mômen xoắn ngăn không cho stato quay "
        "được đo bằng các phản lực theo cách gần giống như với phanh prony. Mômen xoắn cản được điều "
        "chỉnh bằng một van, điều khiển hoặc áp suất ngược trong đường ống xả nước [25], hoặc lưu lượng "
        "vào [26], và đôi khi (để cho phép thay đổi mômen xoắn rất nhanh) bằng hai van điều khiển cả "
        "hai [27]. Trong mọi trường hợp, năng lượng được hấp thụ đều được mang đi bởi dòng nước chảy "
        "liên tục. Những loại phanh nước gắn trên giá đỡ khác, tuy bề ngoài tương tự, lại có kết cấu "
        "bên trong khác biệt đáng kể và dựa trên những nguyên lý khác để tạo mômen xoắn cản (ví dụ rôto "
        "trơn tạo lực cản nhớt nhờ lực cắt và sự rối). Tuy vậy, mọi dynamometer thủy lực đều cố ý hoạt "
        "động như những bơm ly tâm kém hiệu quả. Bất kể thiết kế bên trong và cách đặt van, mômen xoắn "
        "cản cực đại đều thấp ở tốc độ thấp (bằng không khi đứng yên) nhưng có thể tăng nhanh, điển "
        "hình là biến thiên theo bình phương tốc độ quay. Sự hiện diện không thể loại trừ của một lượng "
        "nước nào đó, cùng với lực cản gió, đặt một giới hạn dưới phụ thuộc tốc độ cho mômen xoắn cản "
        "điều khiển được. Trong bất kỳ thiết kế nào, mài mòn và dao động do xâm thực đặt những giới hạn "
        "trên cho tốc độ và mức công suất. Dynamometer thủy lực có sẵn trong một dải định mức rộng từ "
        "300 kW đến 25 000 kW, với một số mẫu xách tay có định mức thấp tới 75 kW [26]. Chiếc lớn nhất "
        "từng được chế tạo [27], hấp thụ tới khoảng 75 000 kW (100 000 Hp), đã được dùng để thử các hệ "
        "động lực đẩy cho tàu ngầm hạt nhân. Tốc độ cực đại tương ứng với tốc độ vận hành của những động "
        "cơ sơ cấp mà chúng được chế tạo để thử, và do đó nói chung giảm khi định mức tăng. Thiết bị thử "
        "động cơ tuabin khí và động cơ hàng không tốc độ cao có thể vận hành tới 30 000 rpm [25]."))
    b.append(p(
        "Năm 1855, Jean B. L. Foucault (1819–1868) [22] đã chứng minh việc chuyển hóa công cơ học thành "
        "nhiệt bằng cách quay một đĩa đồng giữa các cực của một nam châm điện. Phương tiện đơn giản này "
        "để tạo mômen xoắn cản, dựa trên dòng xoáy, từ khoảng năm 1935 đã được khai thác rộng rãi trong "
        "các dynamometer. Hình 24.7 cho thấy những đặc điểm thiết yếu của loại phanh này. Chuyển động "
        "quay của một rôto thép có răng hoặc có nan hoa trong một từ trường đồng nhất về không gian, "
        "được tạo ra bởi dòng điện một chiều qua các cuộn dây trong stato, cảm ứng những dòng điện tuần "
        "hoàn cục bộ (dòng xoáy) trong những phần dẫn điện (bằng đồng) của stato. Những lực điện từ giữa "
        "rôto — vốn được từ hóa bởi từ trường đồng nhất — và từ trường phát sinh từ các dòng xoáy, tạo "
        "ra mômen xoắn cản. Mômen xoắn này, và do đó công suất cơ học đầu vào, được điều khiển bằng cách "
        "điều chỉnh dòng kích thích trong các cuộn dây stato. Công suất điện đầu vào nhỏ hơn 1% định "
        "mức. Dynamometer thực chất là một máy phát bị ngắn mạch bên trong, bởi vì công suất gắn với tổn "
        "thất điện trở của các dòng xoáy được sinh ra bị tiêu tán ngay trong máy. Bị nung nóng bởi dòng "
        "các dòng điện này, stato phải được làm mát, đôi khi (ở những máy định mức nhỏ hơn) bằng không "
        "khí do quạt gió cấp [23], nhưng thường hơn là bằng dòng nước chảy liên tục [25, 27, 28]. Trong "
        "các phanh dòng xoáy kiểu khe khô (loại được vẽ trên Hình 24.7), dòng nước chỉ giới hạn trong "
        "những đường dẫn bên trong stato. Những máy lớn hơn thường thuộc kiểu nước trong khe, trong đó "
        "nước còn tuần hoàn quanh rôto [28]. Nước tiếp xúc với rôto đang chuyển động thực chất hoạt động "
        "như trong một phanh nước, thêm một thành phần phi điện từ vào tổng mômen xoắn cản, do đó đặt "
        "một giới hạn dưới cho mômen xoắn điều khiển được. Lực cản gió đặt giới hạn cho giá trị nhỏ nhất "
        "của mômen xoắn điều khiển được ở các kiểu khe khô. Vì mômen xoắn cản được tạo ra bởi chuyển "
        "động của rôto, nó bằng không khi đứng yên với mọi giá trị dòng kích thích. Ban đầu tăng nhanh, "
        "gần như tuyến tính theo tốc độ, mômen xoắn cuối cùng tiến tới một giá trị bão hòa bị giới hạn "
        "bởi dòng điện. Như ở những máy gắn trên giá đỡ khác, mômen xoắn cần thiết để ngăn stato quay "
        "được đo bằng phản lực tác dụng tại một khoảng cách cố định đã biết tính từ trục quay. Các phanh "
        "dòng xoáy mẫu tiêu chuẩn có định mức từ dưới 1 kW [23, 27] đến trên 2000 kW [27, 28], với tốc "
        "độ cực đại từ 12 000 rpm ở các mẫu định mức nhỏ hơn đến 3600 rpm ở các mẫu lớn nhất. Những mẫu "
        "đặc biệt có định mức 3000 Hp (2238 kW) tại tốc độ tới 25 000 rpm đã được chế tạo [28]."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p(
        "Phanh từ trễ [29] tạo mômen xoắn cản nhờ những lực hút/đẩy từ giữa các cực từ được thiết lập "
        "trong một kết cấu stato dạng lưới bởi dòng điện qua cuộn dây trường, và những cực từ được tạo "
        "ra trong một rôto “cốc kéo” bởi gradient trường của stato. Chuyển động quay của rôto thép đặc "
        "biệt qua hình ảnh trường không gian do stato thiết lập dẫn tới sự đảo chiều có chu kỳ của cực "
        "tính các từ độ cục bộ của nó. Năng lượng gắn với những lần đảo chiều này (tỉ lệ với diện tích "
        "vòng từ trễ của vật liệu rôto) được chuyển hóa thành nhiệt bên trong cốc kéo. Độ tăng nhiệt "
        "được kiểm soát bằng làm mát cưỡng bức bằng không khí từ một quạt gió hoặc một nguồn khí nén. "
        "Cũng như với phanh dòng xoáy, mômen xoắn cản của những thiết bị này được điều khiển bằng dòng "
        "kích thích. Ngược với phanh dòng xoáy, mômen xoắn cản định mức vẫn có sẵn xuống tới tốc độ bằng "
        "không. (Hiệu ứng dòng xoáy điển hình chỉ thêm khoảng 1% vào mômen xoắn cản cho mỗi 1000 rpm.) "
        "Nhờ các bộ phận quay có bề mặt nhẵn, phanh từ trễ có mômen xoắn ký sinh thấp và do đó bao được "
        "một dải động cao tới 200 : 1. Các mẫu tiêu chuẩn có sẵn với định mức công suất liên tục tới "
        "6 kW (12 kW khi dùng hai phanh nối tiếp được làm mát bằng hai quạt). Định mức gián đoạn của mỗi "
        "thiết bị (cho 5 phút hoặc ít hơn) là 7 kW. Một số mẫu định mức thấp được làm mát bằng đối lưu; "
        "mẫu nhỏ nhất có định mức liên tục chỉ 7 W (35 W trong 5 phút). Tốc độ cực đại nằm trong khoảng "
        "từ 30 000 rpm với mẫu nhỏ nhất đến 10 000 rpm với mẫu lớn nhất. Mômen xoắn được đo bằng một "
        "cầu gage biến dạng trên một cánh tay đòn đỡ stato của máy."))

    b.append(h3("24.5.2 Dynamometer dẫn động và dynamometer vạn năng",
                "Driving and Universal Dynamometers"))
    b.append(p(
        "Máy phát điện, cả xoay chiều lẫn một chiều, đem lại một phương tiện khác để tạo mômen xoắn cản "
        "điều khiển được, và chúng dễ dàng được chuyển thành phục vụ dynamometer bằng cách đỡ kết cấu "
        "stato của chúng trên giá đỡ kiểu cũi. Hơn nữa, những máy điện thuộc các loại này còn có thể "
        "vận hành ở chế độ động cơ kéo, trong đó chúng có thể cấp một mômen xoắn chủ động điều khiển "
        "được. Khi được cấu hình để vận hành chọn lựa ở chế độ dẫn động hoặc hấp thụ, máy sẽ đóng vai "
        "một dynamometer vạn năng. Với máy điện một chiều ở chế độ hấp thụ, công suất phát ra thường "
        "được tiêu tán trong một dãy điện trở làm mát bằng đối lưu. Làm mát máy bằng quạt gió thường là "
        "đủ, vì phần lớn công suất cơ học đầu vào được tiêu tán ở bên ngoài. Tuy vậy, toàn bộ công suất "
        "cơ học đầu vào vẫn được hạch toán đầy đủ bằng tích của mômen phản lực và tốc độ quay. Ở chế độ "
        "động cơ kéo, mômen xoắn và tốc độ được điều khiển bằng cách điều chỉnh cả dòng kích từ lẫn dòng "
        "phần ứng. Các máy điện xoay chiều hiện đại dùng những bộ biến đổi nguồn tái sinh để cho phép "
        "công suất hãm được trả về lưới điện. Ở chế độ động cơ kéo, tốc độ được điều khiển bằng những "
        "bộ nghịch lưu biến tần thể rắn, công suất lớn. Kết cấu bên trong là của một động cơ cảm ứng ba "
        "pha đơn giản, không có chổi than, vòng trượt hay vành góp. Việc không có dây quấn rôto cho phép "
        "vận hành ở tốc độ cao hơn so với máy điện một chiều. Dynamometer vạn năng là những máy “bốn "
        "góc phần tư”, một thuật ngữ chỉ khả năng của chúng tạo ra mômen xoắn cùng chiều hoặc ngược "
        "chiều với vận tốc quay của chính chúng. Khả năng độc đáo này cho phép giảm mômen xoắn cản hiệu "
        "dụng xuống bằng không tại bất kỳ tốc độ nào. Dynamometer vạn năng [25, 28] có sẵn trong một dải "
        "định mức tương đối hẹp (56 đến 450 kW), với những dải mômen xoắn (110 đến 1900 N·m) và tốc độ "
        "(4500 đến 13 500 rpm) tương ứng, phản ánh ứng dụng chính của chúng trong việc phát triển động "
        "cơ ô tô. Những dynamometer chuyên dụng để thử hộp số và các bộ phận khác của hệ truyền động xe "
        "đặt DUT vào giữa một động cơ diesel hoặc một động cơ điện sơ cấp và một phanh thủy lực hoặc "
        "phanh dòng xoáy [30]."))

    b.append(h3("24.5.3 Độ chính xác của phép đo", "Measurement Accuracy"))
    b.append(p(
        "Độ chính xác của phép đo công suất (xem thảo luận trong [4]) nói chung bị giới hạn bởi phép đo "
        "mômen xoắn (±0,25% đến ±1%), vì tốc độ quay có thể được đo với hầu như bất kỳ độ chính xác mong "
        "muốn nào. Sai số mômen xoắn có thể phát sinh từ việc tác dụng những mômen xoắn ngoại lai (tức "
        "không được chỉ thị) từ các mối nối ống và cáp, từ lực cản gió của các bộ phận bên ngoài, và từ "
        "việc hiệu chuẩn sai load cell. Ma sát không được phát hiện trong các ổ trục chốt của dynamometer "
        "kiểu giá đỡ có thể làm hỏng độ chính xác của phép đo mômen xoắn. Lý tưởng thì những ổ trục "
        "chống ma sát được bôi trơn tốt không đóng góp đáng kể vào mômen xoắn kìm hãm. Tuy nhiên trong "
        "thực tế, vùng tiếp xúc không thay đổi của các viên bi hoặc các phần tử lăn khác trên các rãnh ổ "
        "làm cho chúng dễ bị rỗ (brinelling — một dạng lõm) do những lực phát sinh từ dao động, từ trọng "
        "lượng không được đỡ của các thiết bị gắn kèm, hoặc thậm chí do vô tình trong khi căn chỉnh máy "
        "được nối vào. Vấn đề có thể được giảm nhẹ bằng cách quay định kỳ các rãnh ổ (chủ yếu là rãnh "
        "ngoài). Trong một số kết cấu ổ lồng trong ổ, các rãnh giữa được một động cơ điện quay liên tục "
        "với tốc độ thấp, trong khi những kết cấu khác tránh được vấn đề bằng cách đỡ stato trên các ổ "
        "trục nâng bằng dầu thủy tĩnh [28]."))

    b.append(h3("24.5.4 Giá cả", "Costs"))
    b.append(p(
        "Dải rộng của các mức mômen xoắn, tốc độ và công suất, cùng với sự khác biệt về mức độ tinh vi "
        "của thiết bị đo đi kèm, được phản ánh trong dải giá của dynamometer rất rộng. Những hệ thống treo "
        "kiểu được minh họa trên Hình 24.5 (mà người dùng phải tự cấp máy quay) có giá 4000 đến 6000 USD, "
        "tăng theo định mức [12]. Một phanh nước xách tay 100 Hp (74,6 kW) được trang bị một load cell "
        "gage biến dạng và một thiết bị hiển thị số cho mômen xoắn, tốc độ và công suất có giá 4500 USD, "
        "hoặc 8950 USD với thiết bị thu thập dữ liệu tinh vi hơn [26]. Dynamometer thủy lực loại cố định "
        "(và một số loại có thể vận chuyển [23]) có giá từ 113 USD/kW ở các cỡ nhỏ hơn [25], xuống "
        "35 USD/kW với loại lớn nhất [27]. Chi phí vận chuyển, lắp đặt và thiết bị đo có thể làm tăng "
        "đáng kể những khoản này. Dynamometer dòng xoáy có giá từ chỉ 57 USD/kW đến gần 700 USD/kW, tùy "
        "theo định mức, loại hệ thống điều khiển và thiết bị đo [24, 25, 28]. Phanh từ trễ có cảm biến "
        "tốc độ tích hợp có giá từ 3300 đến 14 000 USD tùy theo định mức [29]. Các bộ điều khiển tương "
        "thích, từ loại điều khiển bằng tay đến loại lập trình hoàn toàn cho điều khiển thử nghiệm bằng "
        "PC và thu thập dữ liệu qua giao diện IEEE-488, có giá biến thiên từ 500 đến 4200 USD. Tính linh "
        "hoạt và hiệu năng cao của dynamometer vạn năng xoay chiều được phản ánh qua mức giá tương đối "
        "cao của chúng, từ 670 đến 2200 USD/kW [25, 28]."))

    # ------------------------------------------------------------ refs
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "[1] C. P. Pinney and W. E. Baker, “Velocity Measurement,” in <i>The Measurement, "
        "Instrumentation and Sensors Handbook</i>, J. G. Webster, ed., Boca Raton, FL: CRC Press, 1999.",
        "[2] S. Timoshenko, <i>Strength of Materials</i>, 3rd ed., New York: Robert E. Kreiger, Part I, "
        "281–290; Part II, 235–250, 1956.",
        "[3] S. J. Citron, “On-line engine torque and torque fluctuation measurement for engine control "
        "utilizing crankshaft speed fluctuations,” U.S. Patent No. 4,697,561, 1987.",
        "[4] <i>Supplement to ASME Performance Test Codes, Measurement of Shaft Power</i>, "
        "ANSI/ASME PTC 19.7-1980 (Reaffirmed 1988).",
        "[5] See, for example, the catalog of torque wrench products of Consolidated Devices, Inc., "
        "19220 San Jose Ave., City of Industry, CA 91748.",
        "[6] I. J. Garshelis, C. R. Conto, and W. S. Fiegel, “A single transducer for non-contact "
        "measurement of the power, torque and speed of a rotating shaft,” SAE Paper No. 950536, 1995.",
        "[7] C. C. Perry and H. R. Lissner, <i>The Strain Gage Primer</i>, 2nd ed., New York: "
        "McGraw-Hill, 1962, p. 9. (This book covers all phases of strain gage technology.)",
        "[8] B. D. Cullity, <i>Introduction to Magnetic Materials</i>, Reading, MA: Addison-Wesley, "
        "1972, Section 8.5, 266–274.",
        "[9] W. J. Fleming, “Magnetostrictive torque sensors — comparison of branch, cross and "
        "solenoidal designs,” SAE Paper No. 900264, 1990.",
        "[10] Y. Nonomura, J. Sugiyama, K. Tsukada, M. Takeuchi, K. Itoh, and T. Konomi, “Measurements "
        "of engine torque with the intra-bearing torque sensor,” SAE Paper No. 870472, 1987.",
        "[11] I. J. Garshelis, “Circularly magnetized non-contact torque sensor and method for "
        "measuring torque using same,” U.S. Patent 5,351,555, 1994 and 5,520,059, 1996.",
        "[12] Lebow® Products, Siebe plc., 1728 Maplelawn Road, Troy, MI 48099, <i>Transducer Design "
        "Fundamentals/Product Listings</i>, Load Cell and Torque Sensor Handbook No. 710, 1997; also "
        "Torqstar™ and Torque Table®.",
        "[13] S. Himmelstein &amp; Co., 2490 Pembroke, Hoffman Estates, IL 60195, <i>MCRT® Non-Contact "
        "Strain Gage Torquemeters</i> and <i>Choosing the Right Torque Sensor</i>.",
        "[14] Teledyne Brown Engineering, 513 Mill Street, Marion, MA 02738-0288.",
        "[15] Staiger, Mohilo &amp; Co. GmbH, Baumwasenstrasse 5, D-7060 Schorndorf, Germany (in the "
        "U.S.: Schlenker Enterprises Ltd., 5143 Electric Ave., Hillside, IL 60162), <i>Torque "
        "Measurement</i>.",
        "[16] Torquemeters Ltd., Ravensthorpe, Northampton NN6 8EH, England (in the U.S.: Torquetronics "
        "Inc., P.O. Box 100, Allegheny, NY 14707), <i>Power Measurement</i>.",
        "[17] Vibrac Corporation, 16 Columbia Drive, Amherst, NH 03031, <i>Torque Measuring "
        "Transducer</i>.",
        "[18] GSE, Inc., 23640 Research Drive, Farmington Hills, MI 48335-2621, Torkducer®.",
        "[19] Sensor Developments Inc., P.O. Box 290, Lake Orion, MI 48361-0290, 1996 Catalog.",
        "[20] Bently Nevada Corporation, P.O. Box 157, Minden, NV 89423, TorXimitor™.",
        "[21] Binsfield Engineering Inc., 4571 W. MacFarlane, Maple City, MI 49664.",
        "[22] C. C. Gillispie, ed., <i>Dictionary of Scientific Biography</i>, Vol. XI, New York: "
        "Charles Scribner’s Sons, 1975.",
        "[23] AW Dynamometer, Inc., P.O. Box 428, Colfax, IL 61728, <i>Traction dynamometers: Portable "
        "and stationary dynamometers for motors, engines, vehicle power take-offs</i>.",
        "[24] Roy Porter, ed., <i>The Biographical Dictionary of Scientists</i>, 2nd ed., New York: "
        "Oxford University Press, 1994.",
        "[25] Froude-Consine Inc., 39201 Schoolcraft Rd., Livonia, MI 48150, <i>F Range Hydraulic "
        "Dynamometers, AG Range Eddy Current Dynamometers, AC Range Dynamometers</i>.",
        "[26] Go-Power Systems, 1419 Upfield Drive, Carrollton, TX 75006, <i>Portable Dynamometer "
        "System, Go-Power Portable Dynamometers</i>.",
        "[27] Zöllner GmbH, Postfach 6540, D-2300 Kiel 14, Germany (in the U.S. and Canada: Roland "
        "Marine Inc., 90 Broad St., New York, NY 10004), <i>Hydraulic Dynamometers Type P, High Dynamic "
        "Hydraulic Dynamometers</i>.",
        "[28] Dynamatic Corporation, 3122 14th Ave., Kenosha, WI 53141-1412, <i>Eddy Current "
        "Dynamometer — Torque Measuring Equipment, Adjustable Frequency Dynamometer</i>.",
        "[29] Magtrol, Inc., 70 Gardenville Parkway, Buffalo, NY 14224-1322, <i>Hysteresis Absorption "
        "Dynamometers</i>.",
        "[30] Hicklin Engineering, 3001 NW 104th St., Des Moines, IA 50322, Transdyne™ (transmission "
        "test systems, brake and towed chassis dynamometers).",
    ]))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Torque, speed and power are the mechanical variables that define the functional performance of "
        "rotating machinery. Measuring them accurately is essential both for establishing a machine’s "
        "efficiency and for fixing operating regimes that are safe and conducive to long, reliable "
        "service. On-line measurement enables real-time control, helps hold product quality consistent "
        "and gives early warning of impending problems. Torque and power measurements are used in "
        "testing new machine designs and in developing new components, and torque measurement is also "
        "the established basis for controlling and verifying the tightness of threaded fasteners. This "
        "chapter covers the underlying concepts and the methods and apparatus in current use; speed, or "
        "more precisely angular velocity, is treated elsewhere in this handbook [1]."))

    b.append(h2("24.1 Fundamental Concepts", "Những khái niệm cơ bản"))
    b.append(h3("24.1.1 Angular Displacement, Velocity and Acceleration",
                "Dịch chuyển, vận tốc và gia tốc góc"))
    b.append(p(
        "Every point of a rotating rigid body moves in parallel or coincident planes while keeping a "
        "fixed distance from a line called the axis, and in a perfectly rigid body the points also keep "
        "fixed distances from one another. Rotation is perceived as the change of angular position of a "
        "reference point — its angular displacement Δθ over a time interval Δt — and the motion of that "
        "point, hence of the whole body, is characterised by its sense (clockwise or counterclockwise) "
        "and by its angular velocity ω = Δθ/Δt. A change Δω of that velocity in Δt is an angular "
        "acceleration α = Δω/Δt. With angles in radians and time in seconds, ω is in rad s<sup>−1</sup> "
        "and α in rad s<sup>−2</sup>; angular velocity is often called rotational speed and quoted in "
        "revolutions per minute (rpm) or per second (rps)."))

    b.append(h3("24.1.2 Force, Torque and Equilibrium", "Lực, mômen xoắn và cân bằng"))
    b.append(p(
        "Rotation obeys Newton’s laws like any other motion. A force acts directly only on the component "
        "of motion along its line of action, so forces or force components lying in any plane that "
        "contains the axis produce no tendency to rotate about it. Rotation can be started, altered or "
        "stopped only by a tangential force F<sub>t</sub> acting at a finite radial distance l from the "
        "axis; the effect grows with both F<sub>t</sub> and l, so their product — the moment — is the "
        "activating quantity, and a moment about the rotational axis is a torque. Figure 24.1(a) shows "
        "a force F at an angle β to the tangent at a point P a distance l from the axis; the torque is "
        "the tangential component times the moment arm, T = (F cos β)l = F<sub>t</sub>l (Equation "
        "24.1), which with newtons and metres gives the unit N·m."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "The resultant of any number of torques applied at different places along a body is their "
        "algebraic sum, torques tending to rotate it clockwise and counterclockwise taking opposite "
        "signs. Forces, and therefore torques, arise from contact with other solids, from motional "
        "interaction with fluids, or from gravitational (including inertial), electric or magnetic "
        "fields, and the source of each torque experiences an equal and opposite reaction torque. A "
        "non-zero resultant torque produces a proportional angular acceleration, T = Iα (Equation "
        "24.2), where I in kg·m<sup>2</sup> is the polar moment of inertia of the body about the axis; "
        "the relation holds whatever the state of motion. When α = 0 the torque is zero and the body is "
        "in equilibrium, which requires either no applied torque or more than one."))
    b.append(p(
        "<i>Translator’s note.</i> In the source PDF, Equations 24.2–24.5 are broken up by the text "
        "extraction into disconnected fragments; they have been restored here to the standard forms of "
        "Newton’s second law for rotation and of elementary strength of materials, which the source’s "
        "own symbol sequence and prose confirm."))

    b.append(h3("24.1.3 Stress, Rigidity and Strain", "Ứng suất, độ cứng và biến dạng"))
    b.append(p(
        "Any portion of a body in equilibrium is itself in equilibrium, so torques applied to it from "
        "outside must be balanced by equal and opposite internal torques from the adjoining material, "
        "transmitted by the collective action of stresses over the common cross-section. In a solid "
        "round section the shear stress τ rises linearly from zero on the axis to a maximum at the "
        "surface, and for a shaft of diameter d carrying torque T the surface value is τ<sub>m</sub> = "
        "16T/πd<sup>3</sup> (Equation 24.3). Real materials are not perfectly rigid: their modulus of "
        "rigidity G fixes the finite ratio of τ to shear strain γ, so the maximum strain is also at the "
        "surface, γ<sub>m</sub> = τ<sub>m</sub>/G = 16T/πd<sup>3</sup>G (Equation 24.4). Shear strain "
        "appears as an angular displacement between axially separated cross-sections (Figure 24.1(b)); "
        "over a length L the shaft twists through φ = 32LT/πd<sup>4</sup>G (Equation 24.5)."))

    b.append(h3("24.1.4 Work, Energy and Power", "Công, năng lượng và công suất"))
    b.append(p(
        "If the body rotates through an angle θ while a torque T acts, the mechanical work is W = Tθ "
        "(Equation 24.6). Work is done <i>on</i> the body when the torque acts in the same sense as the "
        "displacement, and <i>by</i> the body otherwise; work on the body accelerates it and appears as "
        "kinetic energy Iω<sup>2</sup>/2, work by it decelerates it. A body that is not accelerating "
        "passes on at one place what is done on it at another. Work and energy are measured in joules; "
        "since a radian is dimensionless, 1 J = 1 N·m·rad ≡ 1 N·m, and to avoid confusion with torque "
        "it is better to express mechanical work in m·N or, preferably, in J. Power is the rate of doing "
        "work: a torque T acting through Δθ in Δt delivers TΔθ/Δt, and replacing Δθ/Δt by ω gives the "
        "simple P = Tω (Equation 24.7). The unit is the watt, 1 W = 1 J s<sup>−1</sup> = 1 m·N "
        "s<sup>−1</sup>, with the historical horsepower at 1 Hp = 746 W. Rotating bodies transmit power "
        "between the places where external torques are applied."))

    b.append(h2("24.2 Arrangements of Apparatus", "Bố trí thiết bị đo"))
    b.append(p(
        "Equations 24.1 to 24.7 are the physical basis of torque and power measurement, and Figure 24.2 "
        "shows the generalised arrangement. A driving torque generated inside a device at B is resisted "
        "by an opposing torque developed by another device at F; the drive — an electric motor, a "
        "gasoline engine, a steam turbine, muscular effort — is coupled through members C, a "
        "transmitting region D and further couplings E to the driven device, be it a generator, a pump, "
        "a machine tool or a set of mated threaded fasteners, where the resisting torque is met. The "
        "torque at B or F is what is to be measured, either indirectly through a correlated quantity "
        "such as a current or a fluid pressure, or more directly by measuring the reaction torque at A "
        "or G or the transmitted torque through D. Because torque and rotation are cause and effect, "
        "most interest in transmitted torque concerns rotating bodies."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "In so far as the frames of both machines and their mountings to earth are perfectly rigid, the "
        "reaction at A equals the torque at B at every instant, and the reaction at G equals the torque "
        "at F; under equilibrium these equalities are independent of the compliance of any member. Also "
        "under equilibrium, and apart from usually minor parasitic torques from bearing friction and "
        "air drag on fast-moving surfaces, the driving torque at B equals the resisting torque at F. "
        "Reaction torque at A or G is usually obtained from forces measured at distances fixed by the "
        "apparatus, using Equation 24.1. Transmitted torque is obtained by measuring τ<sub>m</sub>, "
        "γ<sub>m</sub> or φ on a suitable member in region D and applying Equation 24.3, 24.4 or 24.5, "
        "or analogous expressions for sections other than solid round ones [2]; calibration against a "
        "known torque then makes any detail of the member in D unnecessary. When α is non-zero and "
        "measurable, T follows from Equation 24.2 — a method needing only non-invasive observation, and "
        "therefore especially useful for transitory torques such as those of individual firing events "
        "in a multicylinder engine [3]."))
    b.append(p(
        "Equations 24.6 and 24.7 apply only while the body rotates, since without motion no work is done "
        "and no power is transferred. Equation 24.6 gives the average torque from calorimetric "
        "measurement of the heat generated over a totalised number of revolutions, and Equation 24.7 is "
        "the routine basis of power measurement, with T from Equations 24.1, 24.3, 24.4 or 24.5 and ω "
        "measured by any suitable means [4]. F, T and φ are sometimes measured mechanically: the torque "
        "wrench used to tighten fasteners indicates torque by a needle over a calibrated scale driven by "
        "the elastic deflection of a spring member, in the simplest case the bending of the handle [5]. "
        "More generally, sensors or transducers convert the wanted quantity into a linearly proportional "
        "electrical signal — force sensors are also called load cells. Determining P usually requires "
        "multiplying the signals of separate T and ω sensors, though a transducer whose single signal "
        "amplitude is proportional to the power transmitted along a shaft has also been described [6]."))

    b.append(h2("24.3 Torque Transducer Technologies", "Các công nghệ đầu đo mômen xoắn"))
    b.append(p(
        "Several physical interactions convert F, τ, γ or φ into proportional electrical signals, and "
        "each requires some axial portion of the shaft to be dedicated to sensing. Figure 24.3 shows the "
        "typical sensing regions of four technologies in present use."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(h3("24.3.1 Surface Strain", "Biến dạng bề mặt"))
    b.append(p(
        "Figure 24.3(a) converts surface strain into a signal proportional to transmitted torque. "
        "Surface strain became the key basis for force and torque measurement after E. E. Simmons, Jr. "
        "and Arthur C. Ruge invented the bonded wire strain gage in 1938 [7]. A modern gage is simply a "
        "long electrical conductor, usually formed in a serpentine pattern in a very thin foil or film "
        "and bonded to a thin insulating carrier, which is cemented to the surface of the load-carrying "
        "member; strain is sensed as a change of resistance. Those changes are too small to measure "
        "directly, so two to four gages are arranged in a Wheatstone bridge, and independence from axial "
        "and bending loads and from temperature is obtained with a four-gage bridge of two diametrically "
        "opposite matched pairs, each aligned with a principal strain direction — which in round shafts "
        "lies at 45° to the axis. Limiting strains, from Equation 24.4 with τ<sub>m</sub> at the shear "
        "proportional limit, rarely exceed a few parts in 10<sup>3</sup>, so practice is to increase the "
        "compliance of the sensing region — smaller diameter, hollow or specially shaped sections — so "
        "that the limiting strain is reached at the highest torque to be measured, which maximises "
        "sensitivity."))
    b.append(h3("24.3.2 Twist Angle", "Góc xoắn"))
    b.append(p(
        "If the shaft is slender enough (L > 5d) the twist at limiting τ<sub>m</sub> can exceed 1°, "
        "enough to be resolved accurately for practical measurement. Figure 24.3(b) shows the common "
        "arrangement in which torque is found from the difference in tooth-space phasing between two "
        "identical toothed wheels on opposite ends of a compliant torsion bar. The phase displacement of "
        "the periodic signals from the two pickups is proportional to the peripheral displacement of the "
        "salient features, hence to the twist of the bar and so to the torque; the features are chosen "
        "to be sensible by non-contacting magnetic, optical or capacitive means. With more elaborate "
        "pickups the relative angular position appears as the amplitude of a single signal, which allows "
        "torque measurement even on a stationary shaft [13–15]; in other constructions a shaft-mounted "
        "variable-displacement transformer or similar device gives speed-independent output "
        "proportional to φ."))
    b.append(h3("24.3.3 Stress", "Ứng suất"))
    b.append(p(
        "Besides elastic strain, the stresses that transmit torque show up as changes in the magnetic "
        "properties of ferromagnetic shafts. This magnetoelastic interaction [8] gives an inherently "
        "non-contacting basis for torque measurement, and two kinds of transducer are in use: Type 1 "
        "derives its output from torque-induced changes in the permeance of a magnetic circuit, Type 2 "
        "creates a magnetic field in response to torque. Type 1 transducers use branch, cross or "
        "solenoidal constructions [9]. Branch and cross designs detect torque as an imbalance of "
        "permeability along orthogonal 45° helical paths — the principal stress directions — on the "
        "shaft surface or on an added material; solenoidal designs detect differences in axial "
        "permeability between two adjacent surface regions pre-endowed with symmetrical easy axes. "
        "Branch and cross sensors miniaturise readily [10] but local variations of surface magnetic "
        "properties limit their accuracy; the solenoidal design of Figure 24.3(c) averages those "
        "variations out. Type 2 transducers carry a ring of magnetoelastically active material rigidly "
        "attached to the shaft, magnetised during manufacture with each axial half polarised "
        "circumferentially in the opposite direction, as the solid arrows of Figure 24.3(d) show [11]. "
        "Torque tilts the magnetisations into helical directions (dashed arrows), developing poles at "
        "the central domain wall and, of opposite polarity, at the ring end faces; the torque follows "
        "from one or more field sensors — Hall, magnetoresistive or flux gate — placed to sense the "
        "intensity and polarity of the field near the ring."))

    b.append(h2("24.4 Construction, Operation and Application",
                "Kết cấu, vận hành và ứng dụng"))
    b.append(p(
        "Although a sensing region can be created on the shaft itself, it is more usual to install a "
        "pre-assembled modular transducer in the driveline, available with capacities from 0.001 N·m to "
        "200,000 N·m; principle descriptions and installation instructions are found in manufacturers’ "
        "catalogues [12–20]. Trade names often identify the type: Torquemeters [13] for a family of "
        "non-contacting strain gage models, Torkducer® [18] for Type 1 magnetoelastic transducers, "
        "Torqstar™ [12] for Type 2, Torquetronic [16] for wrap-around twist angle sensors and "
        "TorXimitor™ [20] for optoelectronic non-contacting strain gage transducers. Many share generic "
        "features that transcend both the sensing technology and the range, and Figure 24.4 illustrates "
        "them."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(h3("24.4.1 Mechanical Considerations", "Những xem xét cơ khí"))
    b.append(p(
        "Maximum speeds vary widely, limited by size, principle, bearing type, lubrication and dynamic "
        "balance. Grease-, oil- or oil-mist-lubricated ball bearings are typical, and the parasitic "
        "torques of lubricants and seals limit accuracy at the low end of the range (minute-capacity "
        "units have no bearings at all [15]). Forced lubrication allows operation to 80,000 rpm [16]. "
        "High-speed operation demands careful thought about centrifugal stresses acting on the sensed "
        "quantity and about critical, vibration-inducing speed ranges; torsional oscillations from "
        "resonance between shaft elasticity and the inertia of coupled masses can corrupt the "
        "measurement, damage the transducer through excursions above its overload rating, and even be "
        "dangerous."))
    b.append(p(
        "Housings either float on the shaft bearings or are rigidly mounted. Floating housings are "
        "restrained from rotating by soft means — a cable, a spring, a compliant bracket, or an "
        "eccentric feature resting against a fixed surface — and in such installations the axes of "
        "driving and driven shafts must be carefully aligned, torsionally rigid flexible couplings at "
        "each end absorbing small angular and radial misalignment; two flexible couplings at one end "
        "allow the other end to be coupled directly. Rigidly mounted housings carry feet or lugs like "
        "those of a motor frame, sometimes through adapter plates on a floating model, and are preferred "
        "where alignment is difficult or impractical, as when machines are changed often; they require "
        "dual flexible couplings at both ends. Modular transducers for zero or limited rotation need no "
        "bearings, and in such reaction-type units the housing must be attached to the shaft on one "
        "side of the sensing region only, so that all the applied torque is sensed. Whether rotating or "
        "stationary, the shaft ends generally carry coupling details — flats, keyways, splines, tapers, "
        "flanges, square drives."))
    b.append(h3("24.4.2 Electrical Considerations", "Những xem xét điện"))
    b.append(p(
        "Transducers need excitation, and the raw output of the sensing device needs conditioning to a "
        "level and format suited to a meter or to data acquisition. Both are supplied by circuits "
        "matched to the sensing technology: strain gage bridges are typically powered at 10–20 V dc or "
        "ac and give 1.5–3.0 mV per volt of excitation at rated load, so amplifiers of gain 100 or more "
        "are needed, and ac excitation also calls for oscillators and demodulators. Components must be "
        "mounted on the torqued member, and getting power in and signals out of a rotating shaft needs "
        "special means. The most direct is conductive — silver-graphite brushes on silver slip rings, "
        "with a lift-off mechanism to extend life when not measuring. Non-contacting methods include "
        "inductive coupling between stationary and rotating windings [12–15], illumination of "
        "shaft-mounted photovoltaic cells [20], or batteries strapped to the shaft [21], limited by "
        "centrifugal force to low speeds; signals leave through rotary transformers, frequency-modulated "
        "infrared LEDs [19, 20] or FM telemetry [21]. Where rotation is limited to a few turns, as in "
        "steering gear, valve actuators or oscillating mechanisms, hard wiring of both power and signal "
        "is often suitable, and flexible cabling minimises incidental torque and gives long life. "
        "Non-contacting technologies avoid all of this."))
    b.append(h3("24.4.3 Costs and Options", "Giá cả và các tùy chọn"))
    b.append(p(
        "Prices reflect the wide range of capacities, performance ratings, types, styles, options and "
        "accessories, and rise with capacity within a type; reaction types cost about half of similarly "
        "rated rotating units. A foot-mounted 565 N·m strain gage transducer with slip rings or rotary "
        "transformers and an integral speed sensor, specified to ±0.1% nonlinearity and hysteresis, cost "
        "about $4000 in 1997, with about $2000 more for compatible excitation, conditioning and display "
        "instrumentation. A comparable magnetoelastic transducer at ±0.5% costs about $1300, high "
        "capacity units for extreme speed with appropriate lubrication can exceed $50,000, and Type 2 "
        "magnetoelastic transducers mass-produced for automotive power steering cost about $10."))

    b.append(h2("24.5 Apparatus for Power Measurement", "Thiết bị đo công suất"))
    b.append(p(
        "Rotating machinery spans power levels from fractions of a watt to tens of megawatts — a range "
        "of more than 10<sup>8</sup> — and power-measuring apparatus spans a corresponding range of "
        "types and sizes. Mechanical power flows from a driver to a load and can be found directly from "
        "Equation 24.7 by measuring ω together with the output torque of the driver or the input torque "
        "of the load, whichever is the device under test. When the DUT is a driver, measurement is "
        "usually needed over its full range of speed and torque, so the test apparatus must act as a "
        "controllable load able to absorb the delivered power; when the DUT is a pump, fan, gearbox or "
        "other load, the apparatus must include a driver able to supply the DUT’s full rated range. "
        "Power can also be found indirectly by converting it to or from another form of energy and "
        "measuring the calorimetric or electrical quantities, but given the ready availability of "
        "accurate torque and speed measurement, indirect methods are worth considering only where "
        "special circumstances make direct ones difficult."))
    b.append(p(
        "Dynamometer is the special name for power-measuring apparatus that includes absorbing and/or "
        "driving means and in which torque is determined from reaction forces on a stationary part, the "
        "stator. An effective dynamometer is easily assembled by mounting the DUT so that the reaction "
        "torque on its frame can be measured; Figure 24.5 shows a device built for that purpose, and "
        "commercial models (Torque Table® [12]) rated to support 222 N to 4900 N are available with "
        "torque capacities from 1.3 N·m to 226 N·m. Torque tubes [4] and other mounting arrangements "
        "are also used; apart from possible rotational or elastic resonances such systems have no speed "
        "limit. More generally, and especially for large machinery, dynamometers incorporate a "
        "specialised driving or absorbing machine, classified by function as absorbing or driving "
        "(sometimes motoring), a universal dynamometer being able to serve as either."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "<i>Translator’s note.</i> The term <i>dynamometer</i> is retained here because Vietnamese usage "
        "is not settled: “băng thử”, “máy đo công suất” and “lực kế” are all found, and each obscures "
        "part of the meaning. It should be distinguished from the load cell and from the brake, which is "
        "one kind of absorbing dynamometer. The source also prints the Torque Table® torque range out of "
        "order as “1.3 N·m 226 to N·m”; the correct range is 1.3 to 226 N·m."))
    b.append(h3("24.5.1 Absorption Dynamometers", "Dynamometer hấp thụ"))
    b.append(p(
        "Absorption dynamometers, often called brakes because they work by creating a controllable drag "
        "torque, convert mechanical work into heat. A drag torque, unlike an active torque, can only "
        "restrain rotation, never initiate it, and the temperature rise is controlled by carrying the "
        "heat away, usually to a moving fluid, typically air or water. Drag is produced by inherently "
        "dissipative processes: friction between rubbing surfaces, shear or turbulence in a viscous "
        "liquid, the flow of electric current, or magnetic hysteresis. Gaspard Riche de Prony "
        "(1755–1839) invented in 1821 [22] a highly useful friction brake for testing the steam engines "
        "then becoming prevalent, and brakes of that kind are still used for instruction because they "
        "embody the principles and operating considerations of all absorption dynamometers."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "Figure 24.6 shows a prony brake. The power that the engine shaft would deliver to its load is "
        "converted instead into heat by friction between the blocks and the flywheel rim, the clamping "
        "bolts setting the drag torque and water flow or evaporation removing heat from the inside of "
        "the rim. Neither the friction force nor even the flywheel radius need be known — a fact Prony "
        "recognised — because the drag torque, which tends to rotate the clamped apparatus, is held by "
        "the equal and opposite reaction F·r at the end of a torque arm of fixed radius r, where F is "
        "read by a scale or load cell; the power is P = Frω = Fr2πN/60 with N in rpm. Fluctuating "
        "friction makes rubbing a poor way to generate drag, yet prony brakes are so easily built that "
        "ad hoc versions using bare ropes or wooden cleats serve in laboratories and wherever "
        "undemanding or infrequent measurements are wanted. Refined versions form standalone "
        "dynamometers with self-contained cooling tanks up to 746 kW (1000 Hp), to 3600 rpm and "
        "5400 N·m [23], stationary or mobile, used for testing large electric motors and the engines and "
        "transmissions of agricultural vehicles. They can impose full drag torque down to zero speed."))
    b.append(p(
        "William Froude (1810–1879) [24] invented a water brake (1877) that does not rely on rubbing "
        "friction: drag is developed between rotor and stator by the momentum the rotor imparts to the "
        "water in the casing, forcing it to circulate between cup-like pockets cast into facing "
        "surfaces of both. The rotor runs in bearings that also fix its axial position, labyrinth seals "
        "prevent leakage with minimal drag and wear, and the stator casing sits in the frame on trunnion "
        "bearings in cradle fashion, its restraining torque measured by reaction forces much as in the "
        "prony brake. Drag is set by a valve controlling outlet back pressure [25], inlet flow [26], or "
        "both, the last allowing very rapid changes [27], and the absorbed energy leaves with the "
        "continuous water flow. Other cradle-mounted water brakes look similar but differ internally and "
        "rely on other principles, smooth rotors developing viscous drag by shear and turbulence; all "
        "hydraulic dynamometers nevertheless function deliberately as inefficient centrifugal pumps. "
        "Whatever the internal design and valve setting, maximum drag is low at low speed — zero at "
        "standstill — and rises rapidly, typically as the square of speed, while the irreducible "
        "presence of some water plus windage sets a speed-dependent lower limit on controllable torque; "
        "cavitation erosion and vibration set the upper limits of speed and power. Capacities run from "
        "300 kW to 25,000 kW, with portable units as small as 75 kW [26]; the largest ever built [27], "
        "absorbing about 75,000 kW (100,000 Hp), tested nuclear submarine propulsion systems. Maximum "
        "speed matches that of the prime mover being tested and therefore falls as capacity rises, "
        "high-speed gas turbine and aerospace test equipment reaching 30,000 rpm [25]."))
    b.append(p(
        "In 1855 Jean B. L. Foucault (1819–1868) [22] demonstrated the conversion of mechanical work "
        "into heat by rotating a copper disk between the poles of an electromagnet, and this eddy "
        "current means of generating drag has been widely exploited in dynamometers since about 1935. "
        "Figure 24.7 shows the essentials: a toothed or spoked steel rotor turns in a spatially uniform "
        "field from dc-excited stator coils, inducing locally circulating currents in conductive copper "
        "portions of the stator, and the electromagnetic forces between the magnetised rotor and the "
        "field of those eddy currents create the drag. Torque, and hence input power, is controlled by "
        "the stator excitation current, with electrical input below 1% of rated capacity: the machine is "
        "effectively a short-circuited generator, since the resistive loss of the eddy currents is "
        "dissipated within it."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "The heated stator must be cooled, sometimes by blower air in smaller machines [23] but more "
        "often by continuous water flow [25, 27, 28]. In dry gap brakes, the type of Figure 24.7, water "
        "is confined to passages in the stator; larger machines are often of the water-in-gap type, "
        "where water also circulates around the rotor [28], acting as in a water brake and adding a "
        "non-electromagnetic component that sets a lower limit to controllable torque, while in dry gap "
        "types windage sets that limit. Since drag arises from rotor motion it is zero at standstill for "
        "any excitation, rising rapidly and approximately linearly with speed before approaching a "
        "current-limited saturation, and the restraining torque is again measured by a reaction force at "
        "a fixed known distance from the axis. Standard eddy current brakes run from below 1 kW [23, 27] "
        "to over 2000 kW [27, 28], at up to 12,000 rpm in the smaller units and 3600 rpm in the largest, "
        "with special units of 3000 Hp (2238 kW) at 25,000 rpm having been built [28]. Hysteresis brakes "
        "[29] develop drag through the attraction and repulsion between poles established in a "
        "reticulated stator by the field coil and those created in a drag cup rotor by the stator field "
        "gradients; rotation cyclically reverses the local magnetisation of the special steel rotor, and "
        "the energy of those reversals, proportional to the area of the material’s hysteresis loop, is "
        "converted to heat in the cup and removed by blower or compressed air. As with eddy current "
        "brakes the drag is set by the excitation current, but unlike them rated drag is available down "
        "to zero speed (eddy current effects typically add only 1% per 1000 rpm), and their smooth "
        "rotating surfaces give low parasitic torque and a dynamic range as high as 200:1. Continuous "
        "ratings reach 6 kW (12 kW with two tandem brakes and two blowers), intermittent ratings 7 kW "
        "for 5 minutes or less, some low-capacity units are convection cooled, the smallest rated at "
        "7 W continuous (35 W for 5 minutes), and maximum speeds run from 30,000 rpm to 10,000 rpm. "
        "Torque is measured by a strain gage bridge on a moment arm supporting the stator."))

    b.append(h3("24.5.2 Driving and Universal Dynamometers", "Dynamometer dẫn động và vạn năng"))
    b.append(p(
        "Electric generators, ac and dc, offer another controllable drag and are readily adapted to "
        "dynamometer service by cradle-mounting their stators; such machines can also motor, delivering "
        "a controllable active torque, and when they can be selected to drive or absorb they serve as a "
        "universal dynamometer. In the absorbing mode a dc machine dissipates the generated power in a "
        "convection-cooled resistor bank, blower air cooling the machine being usually adequate since "
        "most of the mechanical input is dissipated externally — though all of it is still accounted for "
        "by the product of reaction torque and speed. In the motoring mode torque and speed are set by "
        "the field and armature currents. Modern ac machines use regenerative converters to return "
        "braking power to the line and high-power solid-state inverters for speed control, their "
        "internal construction being that of a plain three-phase induction motor without brushes, slip "
        "rings or commutator, so that the absence of rotor windings allows higher speeds than dc "
        "machines. Universal dynamometers are four-quadrant machines — able to produce torque with or "
        "against their rotation — which allows the effective drag to be reduced to zero at any speed. "
        "They are available over a relatively narrow range, 56 to 450 kW with 110 to 1900 N·m and 4500 "
        "to 13,500 rpm, reflecting their principal use in automotive engine development; special "
        "dynamometers for transmissions and other driveline components insert the DUT between a diesel "
        "or electric prime mover and a hydraulic or eddy current brake [30]."))
    b.append(h3("24.5.3 Measurement Accuracy", "Độ chính xác của phép đo"))
    b.append(p(
        "Power measurement accuracy is generally limited by the torque measurement, ±0.25% to ±1%, since "
        "speed can be measured to almost any desired accuracy. Torque errors arise from extraneous "
        "torques applied through hose and cable connections, from windage of external parts and from "
        "miscalibration of the load cell, and undetected friction in the trunnion bearings of cradled "
        "machines compromises accuracy. Ideally well-lubricated antifriction bearings contribute nothing "
        "to the restraining torque, but in practice the unchanging contact region of the rolling "
        "elements on their races makes them prone to brinelling from vibration, from the unsupported "
        "weight of attached devices, or even inadvertently during alignment; the problem is alleviated "
        "by periodically rotating the races, chiefly the outer ones, and in some bearing-in-bearing "
        "constructions the central races are continuously rotated slowly by a motor, while others "
        "support the stator on hydrostatic oil-lift bearings [28]."))
    b.append(h3("24.5.4 Costs", "Giá cả"))
    b.append(p(
        "The wide range of torque, speed and power levels, together with the varying sophistication of "
        "the instrumentation, is reflected in a very wide spread of prices. Suspension systems of the "
        "kind in Figure 24.5, for which the user supplies the rotating machine, cost $4000 to $6000 and "
        "rise with capacity [12]. A 100 Hp (74.6 kW) portable water brake with a strain gage load cell "
        "and a digital readout of torque, speed and power costs $4500, or $8950 with more sophisticated "
        "data acquisition [26]. Stationary and some transportable hydraulic dynamometers cost from "
        "$113/kW in the smaller sizes [25] down to $35/kW for the very largest [27], with "
        "transportation, installation and instrumentation adding significantly. Eddy current "
        "dynamometers cost from as little as $57/kW to nearly $700/kW depending on capacity, control "
        "system and instrumentation [24, 25, 28]; hysteresis brakes with integral speed sensors cost "
        "$3300 to $14,000 according to capacity [29], with compatible controllers from manual to fully "
        "programmable for PC test control and IEEE-488 data acquisition at $500 to $4200. The "
        "flexibility and high performance of ac universal dynamometers show in their comparatively high "
        "prices of $670 to $2200/kW [25, 28]."))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "[1] C. P. Pinney and W. E. Baker, “Velocity Measurement,” in <i>The Measurement, "
        "Instrumentation and Sensors Handbook</i>, J. G. Webster, ed., Boca Raton, FL: CRC Press, 1999.",
        "[2] S. Timoshenko, <i>Strength of Materials</i>, 3rd ed., New York: Robert E. Kreiger, Part I, "
        "281–290; Part II, 235–250, 1956.",
        "[3] S. J. Citron, “On-line engine torque and torque fluctuation measurement for engine control "
        "utilizing crankshaft speed fluctuations,” U.S. Patent No. 4,697,561, 1987.",
        "[4] <i>Supplement to ASME Performance Test Codes, Measurement of Shaft Power</i>, "
        "ANSI/ASME PTC 19.7-1980 (Reaffirmed 1988).",
        "[5] See, for example, the torque wrench catalogue of Consolidated Devices, Inc., 19220 San Jose "
        "Ave., City of Industry, CA 91748.",
        "[6] I. J. Garshelis, C. R. Conto, and W. S. Fiegel, “A single transducer for non-contact "
        "measurement of the power, torque and speed of a rotating shaft,” SAE Paper No. 950536, 1995.",
        "[7] C. C. Perry and H. R. Lissner, <i>The Strain Gage Primer</i>, 2nd ed., New York: "
        "McGraw-Hill, 1962, p. 9.",
        "[8] B. D. Cullity, <i>Introduction to Magnetic Materials</i>, Reading, MA: Addison-Wesley, "
        "1972, Section 8.5, 266–274.",
        "[9] W. J. Fleming, “Magnetostrictive torque sensors — comparison of branch, cross and "
        "solenoidal designs,” SAE Paper No. 900264, 1990.",
        "[10] Y. Nonomura, J. Sugiyama, K. Tsukada, M. Takeuchi, K. Itoh, and T. Konomi, “Measurements "
        "of engine torque with the intra-bearing torque sensor,” SAE Paper No. 870472, 1987.",
        "[11] I. J. Garshelis, “Circularly magnetized non-contact torque sensor and method for "
        "measuring torque using same,” U.S. Patent 5,351,555, 1994 and 5,520,059, 1996.",
        "[12] Lebow® Products, Siebe plc., Troy, MI, Load Cell and Torque Sensor Handbook No. 710, "
        "1997; also Torqstar™ and Torque Table®.",
        "[13] S. Himmelstein &amp; Co., Hoffman Estates, IL, <i>MCRT® Non-Contact Strain Gage "
        "Torquemeters</i>.",
        "[14] Teledyne Brown Engineering, Marion, MA.",
        "[15] Staiger, Mohilo &amp; Co. GmbH, Schorndorf, Germany, <i>Torque Measurement</i>.",
        "[16] Torquemeters Ltd., Northampton, England, <i>Power Measurement</i>.",
        "[17] Vibrac Corporation, Amherst, NH, <i>Torque Measuring Transducer</i>.",
        "[18] GSE, Inc., Farmington Hills, MI, Torkducer®.",
        "[19] Sensor Developments Inc., Lake Orion, MI, 1996 Catalog.",
        "[20] Bently Nevada Corporation, Minden, NV, TorXimitor™.",
        "[21] Binsfield Engineering Inc., Maple City, MI.",
        "[22] C. C. Gillispie, ed., <i>Dictionary of Scientific Biography</i>, Vol. XI, New York: "
        "Charles Scribner’s Sons, 1975.",
        "[23] AW Dynamometer, Inc., Colfax, IL, <i>Traction dynamometers</i>.",
        "[24] Roy Porter, ed., <i>The Biographical Dictionary of Scientists</i>, 2nd ed., New York: "
        "Oxford University Press, 1994.",
        "[25] Froude-Consine Inc., Livonia, MI, <i>F Range Hydraulic, AG Range Eddy Current and AC Range "
        "Dynamometers</i>.",
        "[26] Go-Power Systems, Carrollton, TX, <i>Portable Dynamometer System</i>.",
        "[27] Zöllner GmbH, Kiel, Germany, <i>Hydraulic Dynamometers Type P</i>.",
        "[28] Dynamatic Corporation, Kenosha, WI, <i>Eddy Current Dynamometer — Torque Measuring "
        "Equipment</i>.",
        "[29] Magtrol, Inc., Buffalo, NY, <i>Hysteresis Absorption Dynamometers</i>.",
        "[30] Hicklin Engineering, Des Moines, IA, Transdyne™ transmission test systems.",
    ]))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 24 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 24 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 24 “Đo mômen xoắn và công suất” của Ivan J. Garshelis "
            "(Magnova, Inc.) — các khái niệm cơ bản về chuyển động quay, ứng suất và công suất, bố trí "
            "thiết bị đo, bốn công nghệ đầu đo mômen xoắn (biến dạng bề mặt, góc xoắn, ứng suất từ đàn "
            "hồi loại 1 và loại 2), kết cấu và xem xét cơ–điện của đầu đo, cùng các dynamometer hấp thụ "
            "(phanh prony, phanh nước Froude, phanh dòng xoáy, phanh từ trễ) và dynamometer vạn năng, "
            "với 7 hình và 7 phương trình." if vi
            else
            "Companion to Chapter 24 of the CRC Measurement Handbook — torque and power measurement: "
            "rotational kinematics, torque, stress and strain, work and power; apparatus arrangements; "
            "surface strain, twist angle and magnetoelastic sensing; transducer construction, electrical "
            "considerations and costs; and absorption dynamometers (prony brake, Froude water brake, "
            "eddy current, hysteresis) plus driving and universal dynamometers.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 24' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 24' % BASE_EN)
    meta = ("Chương 24 · theo Ch24.pdf (CRC Press, 1999) · 7 hình, 7 phương trình, 30 tài liệu tham khảo"
            if vi else
            "Chapter 24 · 7 figures, 7 equations, 30 references")
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
