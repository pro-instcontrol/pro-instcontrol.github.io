# -*- coding: utf-8 -*-
"""Handbook 6.10 — Synchro/Resolver Displacement Sensors (Hyatt & Dayton)."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def _ol(items, start=1):
    return '<ol start="%d">%s</ol>' % (start, "".join("<li>%s</li>" % i for i in items))


def body_vi():
    b = []
    b.append(p(
        "Phần lớn đầu đo vị trí điện từ dựa trên công nghệ biến áp. Biến áp làm việc bằng cách kích thích cuộn sơ "
        "cấp bằng một điện áp biến thiên liên tục và cảm ứng một điện áp trong cuộn thứ cấp nhờ đặt nó trong từ "
        "trường biến thiên do cuộn sơ cấp tạo ra. Đây là những thiết bị chỉ dùng dòng xoay chiều, khiến mọi cảm "
        "biến vị trí ghép từ đều là cảm biến ghép biến áp xoay chiều. Chúng có tính cảm ứng tự nhiên vì được cấu "
        "thành từ các cuộn dây quấn. Bằng cách thay đổi mức ghép từ cuộn sơ cấp (được kích thích) sang cuộn thứ cấp "
        "(được ghép) theo dịch chuyển thẳng hoặc dịch chuyển quay, có thể tạo ra một tín hiệu tương tự biểu diễn "
        "dịch chuyển ấy. Sự thay đổi mức ghép này đạt được bằng cách di chuyển một trong hai cuộn dây, hoặc một "
        "phần tử lõi tạo đường dẫn từ thông giữa hai cuộn."))
    b.append(p(
        "Một trong những dạng đơn giản nhất của đầu đo vị trí điện từ là LVDT, đã được mô tả ở mục 6.2 về cảm biến "
        "cảm ứng. Nếu dịch chuyển của lõi trong một thiết bị kiểu LVDT được đổi từ thẳng sang quay, thiết bị trở "
        "thành RVDT — biến áp vi sai biến thiên kiểu quay."))

    # ------------------------------------------------- induction potentiometers
    b.append(h2("Cảm biến kiểu pot cảm ứng", "Induction potentiometers"))
    b.append(p(
        "Người thiết kế linh kiện có thể “tăng cường” đầu ra, tăng độ chính xác và đạt được dải góc rộng hơn một "
        "chút nếu đặt dây quấn lên cả roto như trên Hình 6-89. Nhược điểm của cách làm này là (1) thêm dây quấn, "
        "(2) cần thêm không gian vật lý, (3) chênh lệch theo nhiệt độ lớn hơn, và (4) độ lệch pha lớn hơn do có "
        "thêm dây quấn."))
    b.append(p(
        "Ưu điểm của thiết kế kiểu pot cảm ứng là độ nhạy lớn hơn (nhiều vôn trên mỗi độ hơn), nhờ đó tỉ số tín "
        "hiệu/nhiễu tốt hơn và trong phần lớn trường hợp độ chính xác cũng cao hơn."))
    b.append(fig(89, F.fig_6_89()))

    # ------------------------------------------------------------- resolvers
    b.append(h2("Resolver", "Resolvers"))
    b.append(p(
        "Nếu tấm thép hai khe trong stato ở Hình 6-89 được thay bằng một tấm thép nhiều khe (xem Hình 6-90), và hai "
        "bộ dây quấn được thiết kế thành những cụm cuộn đồng tâm rồi phân bố trong từng phần tư của lõi ghép, thì "
        "có thể tạo ra trên một cuộn thứ cấp một xấp xỉ gần đúng của sóng sin, và trên bộ cuộn kia một xấp xỉ gần "
        "đúng của sóng cosin. Những biến áp quay có thiết kế như vậy được gọi là resolver. Dùng tấm thép roto nhiều "
        "khe và phân bố dây quấn trong roto có thể cải thiện dạng sóng sin–cosin thêm nữa."))
    b.append(fig(90, F.fig_6_90()))
    b.append(p(
        "Resolver điều biến biên độ tín hiệu kích thích xoay chiều đặt trên dây quấn roto theo tỉ lệ với sin và "
        "cosin của góc quay cơ khí. Thông tin điện sin–cosin đo được trên các cuộn stato có thể dùng làm dữ liệu vị "
        "trí và vận tốc. Theo nghĩa đó, resolver là một bộ phát hàm lượng giác tương tự. Phần lớn resolver có hai "
        "cuộn sơ cấp đặt vuông góc nhau trong stato, và hai cuộn thứ cấp cũng vuông góc nhau đặt trên roto (xem "
        "Hình 6-91)."))
    b.append(fig(91, F.fig_6_91()))
    b.append(p(
        "Nếu cuộn roto R1–R3 được kích thích bằng điện áp đầu vào định mức (xem Hình 6-92), biên độ đầu ra trên "
        "cuộn stato S2–S4 sẽ tỉ lệ với sin của góc roto θ, còn biên độ đầu ra trên cuộn stato thứ hai S1–S3 sẽ tỉ "
        "lệ với cosin của θ (xem Hình 6-93). Đây thường được gọi là chế độ “bộ phát điều khiển”, và được dùng với "
        "hầu hết bộ chuyển đổi resolver–số hiện đại."))
    b.append(fig(92, F.fig_6_92()))
    b.append(p(
        "Ở chế độ bộ phát điều khiển, mốc điện có thể được định nghĩa là vị trí của roto so với stato tại đó điện "
        "áp trên S2–S4 là cực tiểu khi cuộn roto R1–R3 được kích thích bằng điện áp định mức. Các điểm triệt sẽ "
        "xuất hiện trên S2–S4 tại những vị trí 0° và 180°, và trên S1–S3 tại những vị trí 90° và 270°."))
    b.append(fig(93, F.fig_6_93()))
    b.append(p(
        "Nếu cuộn stato S1–S3 được kích thích bằng điện áp đầu vào định mức và cuộn stato S2–S4 cũng được kích "
        "thích bằng điện áp đầu vào định mức nhưng lệch pha điện đúng 90°, thì điện áp cảm nhận trên cuộn roto "
        "R1–R3 không thay đổi về biên độ hay tần số so với tín hiệu tham chiếu đầu vào. Nó là tổng của cả hai đầu "
        "vào. Tuy vậy, nó thay đổi về pha thời gian so với điện áp đầu vào định mức một góc đúng bằng góc của trục "
        "so với một điểm “không” quy chiếu (xem Hình 6-94). Đây là đầu ra “tương tự pha”, và thiết bị được gọi là "
        "“bộ biến áp điều khiển”. Bằng cách đo độ lệch thời gian giữa điểm qua zero của dạng sóng điện áp tham "
        "chiếu và điểm qua zero của dạng sóng điện áp đầu ra, có thể tính được góc pha — chính là dịch chuyển góc "
        "vật lý của trục ra."))
    b.append(fig(94, F.fig_6_94()))
    b.append(p(
        "Vì resolver là thiết bị tương tự và các đầu ra liên tục suốt 360°, độ phân giải lý thuyết của resolver là "
        "vô hạn. Tuy nhiên tồn tại những điểm không rõ ràng trong điện áp đầu ra, gây ra bởi các biến thiên nội tại "
        "trong quá trình biến đổi điện áp từ sơ cấp sang thứ cấp suốt 360° quay. Những điểm không rõ ràng này dẫn "
        "tới sai số khi xác định vị trí góc thật. Các loại tín hiệu sai số gặp trong resolver được trình bày trên "
        "Hình 6-95."))
    b.append(fig(95, F.fig_6_95()))
    b.append(p(
        "Theo quy luật, đường kính tấm thép stato càng lớn thì độ chính xác càng tốt và độ phân giải tuyệt đối của "
        "thiết bị càng cao. Đó là hàm của số cực từ có thể bố trí được trong thiết bị, mà số cực lại là hàm trực "
        "tiếp của số khe trên tấm thép stato và roto. Với các thiết bị đa tốc độ (xem phần về đa tốc độ bên dưới), "
        "độ phân giải tăng theo bội số của tốc độ. Với phần lớn dải góc, resolver đa tốc độ có thể vượt khả năng "
        "định vị của bất kỳ linh kiện nào khác trong cùng tầm kích thước, khối lượng và giá."))

    # ------------------------------------------------- operating parameters
    b.append(h2("Tham số vận hành và chỉ tiêu kỹ thuật của resolver",
                "Operating parameters and specifications"))
    b.append(p(
        "Có bảy tham số chức năng xác định hoạt động của resolver ở chế độ tương tự. Đó là (1) độ chính xác, (2) "
        "biên độ điện áp vận hành, (3) tần số vận hành, (4) độ lệch pha của điện áp đầu ra so với điện áp đầu vào "
        "tham chiếu, (5) dòng điện tiêu thụ tối đa cho phép, (6) tỉ số biến đổi giữa điện áp ra và điện áp vào, và "
        "(7) điện áp không. Mặc dù trở kháng chi phối các tham số chức năng, nó là đại lượng trong suốt đối với "
        "người dùng. Thiết kế tấm thép và cuộn dây thường được triển khai nhằm cực tiểu hoá điện áp không và dòng "
        "điện vào, còn trở kháng là hệ quả trực tiếp của thiết kế nội tại của resolver. Quy trình sau có thể dùng "
        "để đo bảy giá trị ấy với hầu hết resolver."))

    b.append(h3("Thiết bị cần cho việc kiểm tra resolver", "Equipment needed for testing resolvers"))
    b.append(ul([
        "Một giá đỡ chia độ cơ khí có khả năng định vị trục resolver với độ chính xác góc lớn hơn độ chính xác "
        "định mức của resolver một bậc độ lớn.",
        "Một máy phát tín hiệu xoay chiều có khả năng phát tới 24 V<sub>rms</sub> ở 10 kHz.",
        "Một vôn kế góc pha (PAV) có khả năng đo các thành phần điện áp “cùng pha” và “vuông pha”, phục vụ việc xác "
        "định tỉ số biến đổi, điện áp không, cũng như góc pha giữa điện áp ra và điện áp vào tham chiếu.",
        "Một điện trở 1 Ω dùng để đo dòng điện vào bằng PAV.",
        "Một chỉ thị vị trí góc (API) dùng cùng với giá đỡ chia độ để đo độ chính xác của resolver.",
    ]))
    b.append(_ol([
        "Dùng các thiết bị trên với giá đỡ chia độ ở vị trí 0°, gắn resolver lên giá đỡ và khoá trục resolver lại.",
        "Đặt điện trở 1 Ω nối tiếp với dây R1 (đỏ/trắng) của resolver.",
        "Nối các dây roto của resolver, R1 (đỏ/trắng) và R3 (vàng/trắng) (xem Hình 6-91), vào máy phát tín hiệu "
        "sóng sin, rồi đặt điện áp và tần số theo đúng giá trị thiết kế của resolver.",
        "Nối các đầu của máy phát tín hiệu sóng sin vào đầu vào tham chiếu của vôn kế góc pha (PAV).",
        "Nối các dây ra của resolver S2 (vàng) và S4 (xanh) vào các đầu vào của PAV, và đặt PAV ở chế độ đo tổng "
        "điện áp ra.",
        "Xoay giá đỡ chia độ về vị trí 0°.",
        "Xoay vỏ resolver trong khi theo dõi tổng điện áp ra trên PAV cho tới khi thu được số đọc điện áp cực "
        "tiểu. Ghi lại giá trị này. Đó là điện áp không của resolver.",
        "Xoay giá đỡ chia độ về vị trí 90°.",
        "Đổi chế độ hiển thị của PAV sang hiển thị góc pha giữa điện áp tham chiếu và điện áp trên các dây S2–S4. "
        "Ghi lại số đọc góc pha này.",
        "Đổi chế độ hiển thị của PAV sang hiển thị tổng điện áp ra của resolver.",
        "Ghi lại điện áp này.",
        "Tính tỉ số biến đổi bằng cách chia số đọc ở bước 11 cho biên độ điện áp tham chiếu đầu vào.",
        "Nối các dây vào của PAV song song với điện trở 1 Ω và ghi lại tổng điện áp trên màn hiển thị của PAV. Vì "
        "số đọc này lấy trên một điện trở 1 Ω, nó cũng chính là tổng dòng điện.",
        "Ngắt resolver và máy phát tín hiệu khỏi PAV.",
        "Nối các đầu của máy phát tín hiệu sóng sin vào đầu vào tham chiếu của chỉ thị vị trí góc (API).",
        "Nối các dây stato S1 (đỏ), S3 (đen), S2 (vàng) và S4 (xanh) lần lượt vào các đầu vào S1, S3, S2 và S4 "
        "của API.",
        "Kiểm tra độ chính xác của resolver bằng cách ghi lại số hiển thị trên API tại mỗi 20° suốt 360° quay cơ "
        "khí trên giá đỡ chia độ. Ghi lại toàn bộ các giá trị.",
    ]))

    # ------------------------------------------------------- resolver benefits
    b.append(h2("Ưu điểm của resolver", "Resolver benefits"))
    b.append(p(
        "Người thiết kế hệ thống điều khiển chuyển động ngày nay có nhiều công nghệ để chọn làm thiết bị phản hồi. "
        "Sự phổ biến của động cơ một chiều không chổi than làm nổi bật nhu cầu về thông tin vị trí roto để chuyển "
        "mạch các cuộn dây — một ứng dụng then chốt của các sản phẩm cảm biến. Bộ mã hoá quang được dùng rộng rãi "
        "nhờ dễ ghép nối với các bộ điều khiển hiện đại, nhưng có một số giới hạn cố hữu về dải nhiệt độ, khả năng "
        "chịu va đập và rung, và khả năng chống nhiễm bẩn. Resolver là thiết bị chắc chắn hơn nhiều nhờ kết cấu và "
        "vật liệu của nó, và có thể ghép với các bộ chuyển đổi R→S dạng mô-đun đáp ứng mọi yêu cầu về hiệu năng và "
        "làm việc tin cậy trong những môi trường công nghiệp và hàng không khắc nghiệt nhất."))
    b.append(p(
        "Tín hiệu kích thích E<sub>x</sub> đưa vào resolver được ghép biến áp thành các đầu ra sin và cosin (vuông "
        "pha), tương ứng bằng E<sub>x</sub> sin θ và E<sub>x</sub> cos θ. Bộ chuyển đổi resolver–số (trình bày trên "
        "Hình 6-98) tính góc:"))
    b.append(eq("θ = arctan (E<sub>x</sub> sin θ / E<sub>x</sub> cos θ)", "6.113"))
    b.append(p(
        "Ở dạng theo tỉ số này, đầu ra của cuộn sin được chia cho đầu ra của cuộn cosin, và mọi nhiễu xâm nhập có "
        "độ lớn xấp xỉ như nhau trên cả hai cuộn đều bị triệt tiêu. Điều này tạo ra một đặc tính chống nhiễu cố hữu "
        "có lợi cho người dùng resolver. Đặc tính ấy cũng mang lại mức bù nhiệt đáng kể."))

    # ------------------------------------------------------------ multispeed
    b.append(h2("Thiết bị đa tốc độ", "Multispeed units"))
    b.append(p(
        "Quan hệ đối với thiết bị đa tốc độ là: tốc độ (2×, 3×, …) chỉ ra số chu kỳ sin đầy đủ mà đầu ra resolver "
        "hoàn thành về mặt điện trong 360° quay cơ khí. Với đầu ra điện 2×, chu kỳ sin đầy đủ của resolver 2× xảy "
        "ra trong 180° thay vì 360°. Đầu ra của resolver 2× được trình bày trên Hình 6-96. Một chu kỳ 3× đầy đủ "
        "được hoàn thành trong 120°. Số tốc độ được chọn để dùng là hàm của yêu cầu hệ thống. Tăng số cặp cực từ "
        "trên roto và stato tạo ra thiết bị đa tốc độ. Mỗi tốc độ có một vài tổ hợp dây quấn và khe. Tổ hợp tối ưu "
        "được nhà thiết kế resolver chọn dựa trên yêu cầu của hệ thống."))
    b.append(fig(96, F.fig_6_96()))

    # ------------------------------------------------------------ applications
    b.append(h2("Ứng dụng", "Applications"))
    b.append(p(
        "Resolver thường được dùng cùng với động cơ, và do có thiết kế tương đồng cố hữu (dây quấn đồng trên các "
        "tấm thép ghép), khả năng chịu môi trường của chúng khá giống nhau. Chúng rất thích hợp để thiết kế vào các "
        "ứng dụng công nghiệp nơi bụi và chất lỏng trong không khí có thể che khuất tín hiệu của bộ mã hoá quang. "
        "Máy NC, máy quấn cuộn, máy ép và bàn định vị là những nơi resolver phát huy ưu thế. Khả năng chịu va đập "
        "và rung cố hữu khiến resolver đặc biệt phù hợp với các nền tảng chuyển động, và độ tin cậy của chúng trong "
        "những điều kiện ấy là trợ giúp đáng kể cho người thiết kế robot, cổng trục và dây chuyền chuyển tải trong "
        "công nghiệp ô tô."))
    b.append(p(
        "Độ nhạy với nhiệt luôn là vấn đề đối với người thiết kế hệ thống điều khiển chuyển động. Resolver dùng để "
        "cảm nhận vị trí van trong các ứng dụng nhiệt độ cao như động cơ máy bay, lọc hoá dầu và chế biến hoá chất "
        "đã liên tục chứng minh được độ tin cậy của mình."))
    b.append(p(
        "Đưa thiết bị tới những vị trí chính xác với điều khiển êm và chính xác có thể là một thách thức thực sự "
        "trong môi trường nhiễu điện từ của nhà máy công nghiệp hiện đại. Nhiễu điện từ dẫn và bức xạ từ thiết bị "
        "lân cận, cùng những biến thiên điện áp đầu vào kèm xung dòng không mong muốn trên đường dây nguồn, có thể "
        "tước mất tính toàn vẹn tín hiệu của các hệ thống số. Resolver tương tự vẫn tiếp tục làm việc mà không mất "
        "thông tin hay gián đoạn tín hiệu. Việc số hoá tín hiệu có thể được thực hiện tại một giao diện từ xa trong "
        "điều kiện được kiểm soát tốt hơn so với trên sàn nhà máy. Chỉ những vật liệu bền chắc mới làm việc tốt "
        "trong môi trường khắc nghiệt."))

    # ---------------------------------------------------------------- synchros
    b.append(h2("Synchro", "Synchros"))
    b.append(p(
        "Từ thời Thế chiến thứ hai, synchro đã được dùng trong các hệ định vị tương tự để cung cấp dữ liệu và điều "
        "khiển vị trí vật lý của các thiết bị cơ khí như ăng-ten radar, kim chỉ thị trên thiết bị đo, và cơ cấu "
        "điều khiển hoả lực trong thiết bị quân sự. Thuật ngữ “synchro” định nghĩa một đầu đo vị trí điện từ có một "
        "bộ ba cuộn dây ra ba pha, được bố trí cách nhau 120° cả về điện lẫn về cơ khí, thay cho khoảng cách 90° "
        "gặp ở resolver. Ở chế độ sơ cấp trên roto, synchro được kích thích bằng một tín hiệu xoay chiều một pha "
        "trên roto. Khi roto quay 360°, ba sóng sin điều biên trên ba pha của đầu ra có một tập biên độ rời rạc ứng "
        "với mỗi vị trí góc. Bằng cách diễn giải các biên độ ấy, có thể lập một bảng để giải mã chính xác vị trí "
        "quay."))
    b.append(p(
        "Trong phần lớn ứng dụng, resolver đã thay thế synchro nhờ sự tinh vi của các bộ chuyển đổi resolver–số "
        "bán sẵn trên thị trường. Làm việc với một cặp sin và cosin đơn giản hơn và cần ít phép biến đổi, giải mã "
        "hơn so với dùng ba tín hiệu lệch nhau 120°. Nếu muốn chuyển đầu ra của synchro sang dạng resolver, có thể "
        "dùng một thiết bị gọi là biến áp Scott “T”. Trong phần lớn bộ xử lý synchro–số, bước đầu tiên là chuyển "
        "tín hiệu sang dạng resolver bằng một thiết bị Scott “T”."))

    # ------------------------------------------------------------ modular
    b.append(h2("Một giải pháp dạng mô-đun", "A modular solution"))
    b.append(p(
        "Resolver không chổi than là một thiết bị phản hồi khép kín, khác với bộ mã hoá quang, cung cấp một tín "
        "hiệu tương tự với độ phân giải vô hạn. Không chỉ có thể chuyển tín hiệu đầu ra thành thông tin vị trí số "
        "chính xác, nó còn cung cấp một tín hiệu vận tốc chính xác, nhờ đó loại bỏ nhu cầu dùng một máy đo tốc độ "
        "riêng. Độ tin cậy được nâng cao khi dùng cùng một resolver cho cả phản hồi tốc độ lẫn chuyển mạch. Số lượng "
        "chi tiết có thể giảm bớt, và có thể loại bỏ sự phức tạp của việc dùng các linh kiện hiệu ứng Hall để tạo "
        "tín hiệu định thời cho chuyển mạch."))
    b.append(p(
        "Cách tiếp cận dạng mô-đun cho phép người thiết kế dễ dàng chọn một resolver đơn tốc độ hay đa tốc độ cùng "
        "phần điện tử phù hợp, đáp ứng gần như mọi mức độ phân giải và chính xác mong muốn. Resolver được thiết kế "
        "theo các cỡ khung thông dụng nhất: 8, 11, 15 và 21. Các mẫu có vỏ dùng ổ bi cấp động cơ chất lượng cao. Các "
        "mẫu công nghiệp hạng nặng được bao trong vỏ nhôm sơn đen chắc chắn, với kiểu lắp mặt bích, mặt trước hoặc "
        "kiểu servo, và dùng đầu nối kiểu MS."))

    b.append(h3("Giải pháp thiết kế hợp lý cho việc mã hoá góc trục",
                "The sensible design alternative for shaft angle encoding"))
    b.append(p(
        "Yêu cầu về phản hồi vận tốc và vị trí đóng vai trò quan trọng trong các hệ điều khiển chuyển động ngày "
        "nay. Với sự phát triển của các bộ chuyển đổi resolver–số đơn khối giá thấp, một hệ dựa trên resolver cung "
        "cấp cho kỹ sư thiết kế những khối cấu thành để xử lý nhiều loại ứng dụng khác nhau. Kích thước nhỏ, thiết "
        "kế chắc chắn và khả năng đạt độ chính xác rất cao trong điều kiện khắc nghiệt khiến resolver trở thành đầu "
        "đo lý tưởng cho việc cảm nhận vị trí tuyệt đối. Những thiết bị này cũng rất phù hợp cho các môi trường cực "
        "kỳ khắc nghiệt như va đập và rung cơ khí liên tục, độ ẩm, sương dầu, dung dịch làm mát và dung môi. Cảm "
        "nhận vị trí tuyệt đối so với cảm nhận vị trí gia số là điều bắt buộc khi làm việc trong môi trường có khả "
        "năng mất nguồn. Mỗi khi được cấp nguồn, một hệ tuyệt đối có khả năng đọc ngay vị trí của mình; điều này "
        "loại bỏ nhu cầu về một điểm khởi đầu “về gốc” hay quy chiếu."))

    b.append(h3("Bộ chuyển đổi resolver–số", "Resolver-to-digital converters"))
    b.append(p(
        "Một bộ chuyển đổi resolver–số đơn khối chỉ cần sáu linh kiện thụ động bên ngoài để đặt băng thông và tốc độ "
        "theo dõi tối đa. Băng thông điều khiển mức độ nhanh mà bộ chuyển đổi phản ứng với một thay đổi lớn về vị "
        "trí trên đầu ra resolver. Bộ chuyển đổi cũng có thể được lập trình để cung cấp 10, 12, 14 hoặc 16 bit dữ "
        "liệu song song. Một hệ dựa trên resolver có thể mang lại khả năng động học cao và độ phân giải cao cho các "
        "hệ điều khiển chuyển động ngày nay, nơi cần phản hồi chính xác cho cả vị trí lẫn vận tốc."))

    # ------------------------------------------------------------- closed loop
    b.append(h2("Phản hồi vòng kín", "Closed loop feedback"))
    b.append(p(
        "Trong một mô hình servo vòng kín điển hình như trên Hình 6-97, cảm biến vị trí đóng vai trò quan trọng "
        "bằng việc liên tục cập nhật thông tin vị trí và vận tốc. Việc chọn chiến lược điều khiển máy thường dựa "
        "trên hiệu năng, tổng chi phí ứng dụng và mức độ quen thuộc với công nghệ. Độ chính xác của hệ được quyết "
        "định bởi độ phân giải nhỏ nhất của thiết bị cảm nhận vị trí. Một bộ chuyển đổi resolver–số ở chế độ 16 bit "
        "có 2<sup>16</sup> (65.536) số đếm trên mỗi vòng quay, tương đương độ phân giải 20 giây cung. Độ chính xác "
        "tổng thể của bộ chuyển đổi resolver–số là ±2,3 phút cung. Một chỉ tiêu độ chính xác định nghĩa sai số lớn "
        "nhất khi đạt tới một vị trí mong muốn. Độ chính xác của hệ phải nhỏ hơn dung sai của phép đo mong muốn. Một "
        "đặc tính quan trọng của bộ chuyển đổi resolver–số là độ lặp lại. Với chỉ tiêu độ lặp lại ±1 LSB (bit có "
        "nghĩa nhỏ nhất) ở chế độ 16 bit, thiết bị cho một phép đo chính xác khi xác định vị trí từ điểm này sang "
        "điểm khác. Chẳng hạn, khi đi từ điểm A sang điểm B rồi trở lại A, bộ chuyển đổi ở chế độ 16 bit sẽ chính "
        "xác trong phạm vi 20 giây cung so với vị trí ban đầu. Đường cong sai số của bộ chuyển đổi resolver–số lặp "
        "lại trong phạm vi ±1 LSB. Sự kết hợp giữa resolver chính xác cao (±20 giây cung) với bộ chuyển đổi "
        "resolver–số mang lại thông tin vị trí tuyệt đối chính xác để phản hồi chính xác cho điều khiển chuyển "
        "động."))
    b.append(fig(97, F.fig_6_97()))

    # ------------------------------------------------------------- type II
    b.append(h2("Vòng servo Type II", "Type II servo loop"))
    b.append(p(
        "Tốc độ động cơ được theo dõi nhờ tín hiệu ra vận tốc do bộ chuyển đổi resolver–số tạo ra. Tín hiệu này là "
        "một điện áp một chiều tỉ lệ với tốc độ, dương khi góc tăng và âm khi góc giảm, với chỉ tiêu độ tuyến tính "
        "điển hình 0,25% và sai số đảo chiều điển hình 0,75%. Việc xử lý sai số được thực hiện theo kỹ thuật theo "
        "dõi Type II tiêu chuẩn của ngành công nghiệp với các bộ chuyển đổi resolver–số (xem Hình 6-98)."))
    b.append(p(
        "Sai số một chiều được tích phân, tạo ra một điện áp vận tốc điều khiển một bộ dao động điều khiển bằng "
        "điện áp (VCO). VCO này là một bộ tích phân gia số (đầu vào điện áp không đổi cho đầu ra tốc độ vị trí), "
        "và cùng với bộ tích phân vận tốc tạo thành một vòng phản hồi servo Type II tắt dần tới hạn. Thông tin này "
        "cho phép động cơ duy trì tốc độ không đổi dưới tải thay đổi khi được ghép nối với một bộ điều khiển logic "
        "khả trình (PLC). Kiến trúc dựa trên PLC được dùng cho các ứng dụng điều khiển đòi hỏi nhiều vào/ra. PLC là "
        "một lựa chọn chi phí thấp cho những nhà phát triển quen với ngôn ngữ lập trình logic bậc thang của nó. Việc "
        "tích hợp chuyển động, vào/ra, giao diện người vận hành và truyền thông thường được hỗ trợ qua các bảng "
        "mạch phụ cắm vào backplane."))
    b.append(fig(98, F.fig_6_98()))
    b.append(p(
        "Các ứng dụng cụ thể đòi hỏi những biên dạng riêng để điều khiển tốc độ và gia tốc của động cơ nhằm thực "
        "hiện nhiệm vụ đặt ra. Bằng cách giảm gia tốc và giảm tốc xảy ra trong mỗi lần vận hành, có thể hạ chi phí "
        "và dùng những động cơ hiệu suất cao hơn. Các ứng dụng công nghiệp bao gồm:"))
    b.append(ul([
        "Định vị trục vít me bi",
        "Chuyển mạch động cơ",
        "Định vị trong robot",
        "Hệ thị giác máy",
        "Bàn X–Y",
        "Cắm linh kiện",
        "Điều khiển video từ xa",
        "Dẫn hướng băng vật liệu",
        "Máy gắp và đặt",
    ]))

    # ------------------------------------------------- conversion detail
    b.append(h2("Chuyển đổi resolver–số", "Resolver-to-digital conversion"))
    b.append(p(
        "Đối với một bộ chuyển đổi resolver–số, thông tin từ resolver được đưa tới một bộ điều hoà resolver bán dẫn "
        "làm giảm biên độ tín hiệu xuống còn sin và cosin 2 V<sub>rms</sub>; biên độ của tín hiệu này tỉ lệ với sin "
        "của θ (góc cần số hoá), và biên độ của tín hiệu kia tỉ lệ với cosin của θ. (Các biên độ được nói tới ở đây "
        "dĩ nhiên là biên độ sóng mang tại tần số tham chiếu, nghĩa là sóng cosin thực chất là cos θ cos ωt; nhưng "
        "số hạng sóng mang cos ωt sẽ được bỏ qua trong phần thảo luận này vì nó sẽ bị loại bỏ trong bộ tách sóng, và "
        "dù sao nó cũng không chứa dữ liệu.) Một mạch chọn góc phần tư trong bộ biến áp điều khiển cho phép chọn "
        "góc phần tư chứa θ, và tự động đặt các cực tính của sin θ và cos θ cho phù hợp với ý nghĩa tính toán."))
    b.append(p(
        "Các đầu ra sin θ, cos θ của bộ chọn góc phần tư sau đó được đưa vào các bộ nhân sin và bộ nhân cosin, cũng "
        "nằm trong bộ biến áp điều khiển. Các bộ nhân này là những mạng điện trở được lập trình bằng số. Hàm truyền "
        "của mỗi mạng được quyết định bởi một đầu vào số (đóng mở các điện trở đã được chia tỉ lệ), sao cho giá trị "
        "tức thời của đầu ra là tích của giá trị tức thời của đầu vào tương tự với sin (hoặc cosin) của góc được mã "
        "hoá bằng số. Nếu giá trị tức thời của đầu vào tương tự của bộ nhân sin là cos θ, và “từ” được mã hoá bằng "
        "số đưa tới bộ nhân sin là φ, thì mã đầu ra là cos θ sin φ. Như vậy hai đầu ra của các bộ nhân là:"))
    b.append(ul([
        "Từ bộ nhân sin: cos θ sin φ",
        "Từ bộ nhân cosin: sin θ cos φ",
    ]))
    b.append(p(
        "Các đầu ra này được đưa tới một bộ trừ dùng khuếch đại thuật toán, tại điểm nối hiệu như trên hình, sao "
        "cho đầu vào đưa tới bộ tách sóng là:"))
    b.append(eq("sin θ cos φ − cos θ sin φ = sin (θ − φ)", "6.114"))
    b.append(p(
        "Vế phải của đồng nhất thức lượng giác này cho thấy đầu ra của điểm nối hiệu biểu diễn một sóng sin tại "
        "tần số sóng mang với biên độ tỉ lệ với sin của hiệu giữa θ (góc cần số hoá) và φ (góc được lưu dưới dạng "
        "số trong bộ đếm lên/xuống). Điểm này chính là tín hiệu sai số xoay chiều, được đưa ra dưới ký hiệu (e). Bộ "
        "tách sóng cũng nhận điện áp tham chiếu, đã được cách ly khỏi nguồn tham chiếu và được chia tỉ lệ thích "
        "hợp bởi bộ điều hoà tham chiếu. Đầu ra của bộ tách sóng khi đó là một mức một chiều tương tự, tỉ lệ với "
        "sin(θ − φ) — nói cách khác, tỉ lệ với sin của “sai số” giữa vị trí góc thực của resolver và góc được mã "
        "hoá bằng số φ, tức đầu ra của bộ đếm. Điểm sai số một chiều này đôi khi được đưa ra dưới ký hiệu (D), còn "
        "nếu thêm một bộ phát hiện ngưỡng sẽ có một cờ tự kiểm tra (BIT). Khi tín hiệu sai số xoay chiều vượt quá "
        "100 LSB, cờ BIT sẽ chỉ ra một lỗi theo dõi. Tín hiệu sai số góc này sau đó được đưa vào bộ xử lý sai số và "
        "VCO. Mạch này thực chất gồm một bộ tích phân tương tự mà đầu ra (tích phân theo thời gian của sai số) điều "
        "khiển tần số của một bộ dao động điều khiển bằng điện áp (VCO). VCO tạo ra các xung nhịp được bộ đếm "
        "lên/xuống đếm. “Chiều” của sai số (φ quá cao hay quá thấp) được xác định bởi cực tính của (φ), và được dùng "
        "để tạo một tín hiệu điều khiển bộ đếm (U), quyết định bộ đếm tăng lên hay giảm xuống. Cuối cùng, cần lưu ý "
        "rằng bộ đếm lên/xuống, giống như mọi bộ đếm, về mặt chức năng là một bộ tích phân gia số; do đó bộ chuyển "
        "đổi theo dõi tự nó cấu thành một cơ cấu servo vòng kín (liên tục cố gắng triệt tiêu sai số về không) với "
        "hai bộ tích phân mắc nối tiếp. Đây được gọi là vòng servo “Type II”, có những ưu điểm rõ rệt so với vòng "
        "Type I hay Type 0."))
    b.append(p(
        "Để thấy được giá trị của ứng xử servo Type II ở bộ chuyển đổi theo dõi này, trước hết hãy xét trường hợp "
        "trục không chuyển động. Bỏ qua các sai lệch, các trôi và sai số lượng tử hoá không tránh khỏi, sai số phải "
        "bằng không (θ = φ), và đầu ra số biểu diễn đúng góc trục thực của resolver. Bây giờ cho trục resolver "
        "chuyển động và để nó tăng tốc đều từ dθ/dt = 0 tới dθ/dt = V. Trong quá trình tăng tốc, một sai số sẽ xuất "
        "hiện vì bộ chuyển đổi không thể phản ứng tức thời với sự thay đổi vận tốc góc. Tuy nhiên, vì VCO được điều "
        "khiển bởi một bộ tích phân mà đầu ra là tích phân của sai số, độ trễ càng lớn (giữa θ và φ) thì bộ đếm "
        "càng được yêu cầu đuổi theo nhanh hơn. Khi vận tốc trở nên không đổi ở giá trị V, VCO sẽ ổn định ở một tốc "
        "độ đếm tương ứng chính xác với tốc độ thay đổi của θ theo đơn vị thời gian, và tức thời θ = φ. Do đó dφ/dt "
        "sẽ luôn bám theo dθ/dt mà không có sai số vận tốc hay sai số vị trí; sai số duy nhất chỉ là sai số tức thời "
        "(quá độ) trong khi tăng tốc hoặc giảm tốc. Hơn nữa, thông tin do bộ chuyển đổi theo dõi tạo ra luôn "
        "“mới”, được cập nhật liên tục và luôn sẵn có ở đầu ra của bộ đếm. Vì dθ/dt bám theo vận tốc đầu vào, nó có "
        "thể được đưa ra như một tín hiệu vận tốc — một điện áp một chiều tỉ lệ với tốc độ quay, có độ tuyến tính đủ "
        "tốt trong các bộ chuyển đổi hiện đại để loại bỏ nhu cầu dùng máy đo tốc độ trong nhiều hệ thống."))

    # ---------------------------------------------------------- bandwidth
    b.append(h2("Tối ưu hoá băng thông", "Bandwidth optimization"))
    b.append(p(
        "Khi dùng một bộ chuyển đổi đơn khối giá thấp cho phản hồi vị trí và vận tốc, điều quan trọng là phải hiểu "
        "đáp ứng động đối với một đầu vào thay đổi. Khi cân nhắc nên đặt băng thông cho bộ chuyển đổi ở mức nào, "
        "phải tính đến một vài tham số. Khả năng bám theo đáp ứng bậc thang và các gia tốc sẽ quyết định băng thông "
        "cần chọn. Băng thông của bộ chuyển đổi resolver–số càng thấp thì khả năng chống nhiễu càng lớn; nhiễu tần "
        "số cao sẽ bị loại bỏ. Quan hệ giữa tốc độ theo dõi tối đa và băng thông quyết định thời gian xác lập cho "
        "các bậc thang nhỏ và lớn. Với một bậc thang nhỏ, băng thông quyết định thời gian xác lập của bộ chuyển "
        "đổi. Với một bậc thang lớn, tốc độ vuốt vận tốc tối đa và băng thông cùng nhau quyết định thời gian xác "
        "lập."))
    b.append(p(
        "Các bộ chuyển đổi resolver–số ngày nay còn có khả năng mô phỏng đầu ra của một bộ mã hoá quang gia số. "
        "Bằng cách cung cấp các đầu ra A, B và Zero Index, có thể thay bộ mã hoá bằng một resolver cùng bộ chuyển "
        "đổi resolver–số mà không phải thay đổi phần cứng giao diện hiện có."))

    # ------------------------------------------------------- lag and settling
    b.append(h2("Xác định sai số trễ vị trí do gia tốc", "Determining position lag error due to acceleration"))
    b.append(p(
        "Khi thay đổi băng thông và tốc độ theo dõi tối đa, có thể xác định hằng số gia tốc (K<sub>a</sub>) và thời "
        "gian xác lập với bậc thang lớn."))
    b.append(note(
        "<b>Ví dụ.</b> Độ phân giải: 16 bit · Băng thông: 100 Hz · Tham chiếu: 1000 Hz · Theo dõi tối đa: 10 "
        "vòng/giây."))
    b.append(eq("BW = (π / 2) · A", "6.115"))
    b.append(p(
        "Nếu băng thông bằng 100 Hz thì A = 222, và K<sub>a</sub> = A² = 49.284 °·s⁻². Độ trễ tính bằng độ trong "
        "khi có gia tốc là:"))
    b.append(eq("LAG = gia tốc / K<sub>a</sub>", "6.116"))
    b.append(p(
        "Ví dụ: với gia tốc 19.000 °·s⁻² và K<sub>a</sub> = 49.284 °·s⁻², độ trễ bằng 19.000 / 49.284 = 0,38°. Ở "
        "chế độ 16 bit, 1 LSB = 0,0055°. Gia tốc ứng với độ trễ 1 LSB (16 bit) bằng K<sub>a</sub> × 0,0055 = "
        "49.284 × 0,0055 = 270 °·s⁻²."))

    b.append(h3("Thời gian xác lập với bậc thang lớn", "Large step settling time"))
    b.append(p(
        "Để xác định thời gian xác lập cho đáp ứng với một bậc thang lớn (179°), phải tính đến tốc độ theo dõi tối "
        "đa và băng thông."))
    b.append(note(
        "<b>Ví dụ.</b> Bậc thang 179° với BW 100 Hz và theo dõi tối đa 10 vòng/giây. Theo dõi tối đa 10 vòng/giây "
        "= 3600 °·s⁻¹. Vậy 179 / 3600 = 49 ms."))
    b.append(p(
        "Sau đó phải cộng thêm thời gian xác lập do giới hạn băng thông; thời gian này xấp xỉ 11 hằng số thời gian "
        "(ở chế độ 16 bit). Hằng số thời gian bằng 1/A; với A = 222 thì 1/A = 4,5 ms, và 11 hằng số thời gian bằng "
        "45 ms."))
    b.append(table(
        ["Độ phân giải (bit)", "Số đếm trên mỗi vòng", "Số hằng số thời gian"],
        [["10", "1024", "7"],
         ["12", "4096", "8"],
         ["14", "16384", "10"],
         ["16", "65536", "11"]],
        "Bảng · Số hằng số thời gian theo độ phân giải."))
    b.append(p(
        "Do đó thời gian xác lập xấp xỉ cho một bậc thang lớn sẽ là 94 ms. Đây là một giá trị gần đúng. Synchro và "
        "resolver được dùng trong rất nhiều điều kiện động khác nhau; hiểu được cách bộ chuyển đổi phản ứng với "
        "những thay đổi đầu vào này sẽ cho phép tối ưu hoá băng thông và tốc độ theo dõi tối đa cho từng ứng dụng. "
        "Bảng 6.27 của nguyên bản liệt kê các nhà cung cấp resolver và synchro."))
    b.append(table(
        ["Công ty", "Địa điểm", "Điện thoại", "Loại resolver"],
        [
            ["API Harowe", "West Chester, PA", "(800) 566-5274",
             "Loại không chổi than không khung, có vỏ và hạng nặng"],
            ["Admotec, Inc.", "Norwich, VT", "(802) 649-5800", "Resolver rôto đặc Rotasyn"],
            ["Neotech, Inc.", "Hatfield, PA", "(215) 822-5520", "Loại có vỏ, dùng chổi than và không chổi than"],
            ["Vernitron Corp.", "San Diego, CA", "(800) 777-3393",
             "Loại không chổi than, phân đoạn, dùng chổi than và có vỏ"],
            ["Servo Systems", "Montville, NJ", "(973) 335-1007", "Loại dùng chổi than và không chổi than"],
            ["American Electronics", "Fullerton, CA", "(714) 871-3020", "Loại có vỏ"],
            ["Computer Conversions", "East Northport, NY", "(516) 261-3300", "Loại chống nổ và loại chuyên dụng"],
            ["Poltron Corp.", "Gaithersburg, MD", "(301) 208-6597", "Resolver"],
            ["Tamagawa Trading Co.", "Tokyo, Nhật Bản", "011-81-37-383-175",
             "Loại không khung không chổi than và loại có vỏ"],
            ["MPC Products", "Skokie, IL", "(800) 323-4302", "Resolver có vỏ"],
            ["Transicoil, Inc.", "Trooper, PA", "(800) 323-7115", "Resolver có vỏ, không chổi than và có chổi than"],
            ["Litton Poly-Scientific", "Blacksburg, VA", "(800) 336-2112",
             "Resolver dùng chổi than và không chổi than"],
            ["Kearfott Guidance &amp;<br>Navigation Corp.", "Wayne, NJ", "(973) 785-6000",
             "Resolver dùng chổi than và không chổi than"],
            ["Novatronics, Inc.", "Stratford, Ontario, Canada", "(519) 271-3880", "Resolver"],
            ["Muirhead Vactric", "Lake Zurich, IL", "(847) 726-0270", "Resolver"],
        ],
        "Bảng 6.27 · Danh sách nhà cung cấp resolver và synchro."))

    b.append(h2("Thông tin thêm", "Further information"))
    b.append(refs([
        "<i>Synchro/Resolver Conversion Handbook</i>, 4th ed., Bohemia NY: ILC Data Device Corp., 1994.",
        "Analog Devices, Inc., <i>Analog-Digital Conversion Handbook</i>, 3rd ed., Englewood Cliffs, NJ: "
        "Prentice-Hall, 1986.",
        "<i>Synchro &amp; Resolver Conversion</i>, East Molesey, UK: Memory Devices Ltd., 1980.",
    ]))
    b.append(quote(
        "Resolver là một thiết bị tương tự, và các đầu ra của nó liên tục suốt 360° — về lý thuyết độ phân giải là "
        "vô hạn. Nhưng cái làm nên một cảm biến không phải là độ phân giải lý thuyết, mà là mức độ trung thực của "
        "phép biến đổi từ sơ cấp sang thứ cấp trên suốt một vòng quay.",
        "Robert M. Hyatt, Jr. &amp; David Dayton"))
    b.append(nav(10, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Every sensor in this section is a transformer with a movable part. That single sentence explains almost "
        "everything else about them: why they need an ac excitation, why the output is an amplitude-modulated "
        "carrier rather than a voltage, why they are so rugged, and why the electronics that follow them are where "
        "the real engineering happens."))
    b.append(p(
        "The induction potentiometer is the simplest step up from an RVDT: put windings on the rotor as well and you "
        "get more volts per degree. The section is refreshingly honest that this is a trade — four named penalties "
        "for one named benefit — and the benefit is signal-to-noise, not accuracy in the abstract."))

    b.append(h2("Two modes that are easy to confuse", "Hai chế độ dễ nhầm lẫn"))
    b.append(p(
        "A resolver can be wired two ways, and the difference matters more than the wiring diagram suggests. In the "
        "control-transmitter mode you excite the rotor and read two stator windings; the outputs are sine and cosine "
        "of the shaft angle, and the amplitude carries the information. In the control-transformer mode you excite "
        "the two stator windings 90° apart and read the rotor; the amplitude is now constant and the phase carries "
        "the information."))
    b.append(p(
        "That is why the same physical device can be described as an amplitude sensor in one paragraph and a phase "
        "sensor in the next. Figure 6.92 and Figure 6.94 are the two modes; Figure 6.93 is the sine/cosine output "
        "that most modern converter chips expect. Almost every resolver-to-digital converter on the market works in "
        "control-transmitter mode, because a sine and a cosine are easier to manipulate than a phase difference."))

    b.append(h2("Why resolvers outlived synchros", "Vì sao resolver còn, synchro mất"))
    b.append(p(
        "Synchros were the World War II solution: three windings at 120°, a table of amplitudes per position, and "
        "a lot of decoding. They worked, and they flew in radar and fire control. But three phases at 120° are "
        "awkward arithmetic compared with a sine and a cosine, and the converter industry noticed. The Scott “T” "
        "transformer exists precisely to turn a synchro into a resolver before anything else happens — it is the "
        "adapter that let a generation of synchro hardware survive into the resolver era."))
    b.append(p(
        "The lesson generalises: the winning standard is rarely the most elegant sensor, it is the one with the "
        "cheapest arithmetic downstream."))

    b.append(h2("The ratiometric trick", "Mẹo theo tỉ số"))
    b.append(p(
        "Equation 6.113 divides the sine output by the cosine output before taking the arctangent. This is not a "
        "mathematical convenience, it is the whole reason a resolver survives in a factory. Any noise injected "
        "equally into both windings — a ground loop, a temperature drift in the excitation, a common-mode pickup "
        "from a nearby drive — appears in numerator and denominator alike and cancels. What does not cancel is "
        "noise that reaches one winding and not the other, which is why the wiring and shielding of the two pairs "
        "matter so much."))
    b.append(p(
        "The same division is why the specification sheet can claim a large degree of temperature compensation "
        "without any temperature sensor at all."))

    b.append(h2("Reading the type II loop", "Đọc vòng lặp Type II"))
    b.append(p(
        "Figure 6.98 looks complicated and is in fact one idea repeated. Two multipliers form sin θ cos φ and "
        "cos θ sin φ; their difference is sin(θ − φ); everything after that exists only to drive φ towards θ. The "
        "demodulator turns the carrier into a dc error, the integrator turns the error into a rate command, the VCO "
        "turns the rate command into pulses, and the up/down counter turns pulses into φ."))
    b.append(p(
        "Two integrators in series — the analog integrator and the counter — make this a type II loop, and the "
        "consequence is worth stating plainly: at constant velocity the loop has no position error and no velocity "
        "error. The only error is transient, during acceleration. That is what lets a converter with a 100 Hz "
        "bandwidth track a shaft spinning at ten revolutions per second, and it is why the lag calculation in "
        "equation 6.116 has acceleration in the numerator and nothing else."))
    b.append(p(
        "The price of type II is settling time. A large step has to be slewed at the maximum tracking rate and then "
        "allowed to settle for roughly eleven time constants in 16-bit mode. The worked example — 49 ms of slew plus "
        "45 ms of settling, about 94 ms — is the number that decides whether a given machine tool can use this "
        "converter or needs a faster one."))

    b.append(h2("The numbers worth remembering", "Những con số đáng nhớ"))
    b.append(p(
        "Sixteen bits is 65,536 counts per revolution, which is 20 arc seconds of resolution. The converter's own "
        "accuracy is ±2.3 arc minutes — six times coarser than its resolution, and the distinction between the two "
        "is the one people get wrong. Resolution is the smallest step the output can take; accuracy is how far that "
        "step may be from the truth. Repeatability of ±1 LSB is the third number, and for point-to-point motion it "
        "is often the only one that matters."))
    b.append(p(
        "The velocity output deserves a mention of its own. A dc voltage proportional to rate, 0.25% linearity and "
        "0.75% reversal error, is good enough to replace a tachometer in many systems — which is why a resolver "
        "often does double duty for feedback and for commutation, and why the section can claim a lower parts count "
        "than an encoder plus Hall sensors."))
    b.append(table(
        ["Company", "Location", "Phone", "Types of resolvers"],
        [
            ["API Harowe", "West Chester, PA", "(800) 566-5274",
             "Brushless frameless, housed, &amp; heavy-duty units"],
            ["Admotec, Inc.", "Norwich, VT", "(802) 649-5800", "Rotasyn solid rotor resolvers"],
            ["Neotech, Inc.", "Hatfield, PA", "(215) 822-5520", "Housed brush &amp; brushless units"],
            ["Vernitron Corp.", "San Diego, CA", "(800) 777-3393",
             "Brushless, segment, brushed, &amp; housed units"],
            ["Servo Systems", "Montville, NJ", "(973) 335-1007", "Brushed &amp; brushless units"],
            ["American Electronics", "Fullerton, CA", "(714) 871-3020", "Housed units"],
            ["Computer Conversions", "East Northport, NY", "(516) 261-3300",
             "Explosion proof &amp; specialty units"],
            ["Poltron Corp.", "Gaithersburg, MD", "(301) 208-6597", "Resolvers"],
            ["Tamagawa Trading Co.", "Tokyo, Japan", "011-81-37-383-175",
             "Brushless frameless &amp; housed units"],
            ["MPC Products", "Skokie, IL", "(800) 323-4302", "Housed resolvers"],
            ["Transicoil, Inc.", "Trooper, PA", "(800) 323-7115", "Housed brushless &amp; brushed resolvers"],
            ["Litton Poly-Scientific", "Blacksburg, VA", "(800) 336-2112",
             "Brushed and brushless resolvers"],
            ["Kearfott Guidance &amp;<br>Navigation Corp.", "Wayne, NJ", "(973) 785-6000",
             "Brushed &amp; brushless resolvers"],
            ["Novatronics, Inc.", "Stratford, Ontario, Canada", "(519) 271-3880", "Resolvers"],
            ["Muirhead Vactric", "Lake Zurich, IL", "(847) 726-0270", "Resolvers"],
        ],
        "Table 6.27 · List of resolver and synchro suppliers."))
    b.append(nav(10, "en"))
    return "".join(b)
