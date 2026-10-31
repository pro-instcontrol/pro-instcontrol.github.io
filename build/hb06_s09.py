# -*- coding: utf-8 -*-
"""Handbook 6.9 — Magnetic Displacement Sensors (David S. Nyce)."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Nhiều loại thiết bị đo dịch chuyển thẳng và dịch chuyển góc dựa vào trường điện từ và tính chất từ của "
        "vật liệu trong hoạt động của phần tử cảm biến cơ bản của chúng. Một số thiết bị có thể không được gọi là "
        "cảm biến từ theo cách thông thường, mà được đặt tên theo kỹ thuật cảm biến riêng của chúng. Các cảm biến "
        "từ trình bày ở đây dùng một nam châm vĩnh cửu, hoặc một nam châm điện nuôi bằng dòng xoay chiều hay một "
        "chiều. Cùng với nhiều loại vật liệu khác nhau dùng để cảm nhận từ trường, tổ hợp ấy được sắp xếp để thu "
        "được một đáp ứng chỉ ra dịch chuyển góc hoặc dịch chuyển thẳng. Hoặc cảm biến được làm cho hoạt động nhờ "
        "một từ trường, hoặc các tính chất của cảm biến được khai thác nhờ việc dùng một từ trường. Các loại cảm "
        "biến từ được trình bày trong mục này gồm từ giảo, từ điện trở, hiệu ứng Hall và bộ mã hoá từ."))
    b.append(p(
        "Một số phiên bản của synchro/resolver và các cảm biến liên quan cũng thoả mãn những yêu cầu ấy, nhưng "
        "được trình bày ở mục 6.10 nên không nằm trong mục này. Cảm biến tiệm cận cảm ứng đo dịch chuyển trong một "
        "dải rất hẹp và được đề cập ở mục 6.2. LVDT cũng thoả mãn các yêu cầu này nhưng cũng thuộc mục 6.2."))
    b.append(p(
        "Một khía cạnh quan trọng của cảm biến từ là chúng dùng phần tử cảm biến không tiếp xúc. Không có liên kết "
        "hay khớp nối cơ khí nào giữa phần đứng yên và phần chuyển động của cảm biến. Ở một số thiết bị cảm nhận "
        "một nam châm hay một lõi vị trí, cảm biến thậm chí có thể được thiết kế để cho phép lấy nam châm hay lõi "
        "ra khỏi phần tử cảm biến khi không cần đọc số. Không tiếp xúc nghĩa là tuổi thọ của phần tử cảm biến không "
        "bị giới hạn bởi một số chu trình hữu hạn vì mài mòn do ma sát. Điều này quan trọng trong một số máy móc "
        "công nghiệp. Các cảm biến trình bày ở đây đều dùng kỹ thuật cảm biến không tiếp xúc."))
    b.append(p(
        "Dịch chuyển là sự thay đổi vị trí, chứ không phải vị trí tuyệt đối. Tuy nhiên trong thực tiễn công nghiệp, "
        "cảm biến dịch chuyển thường được gắn nhãn là gia số hoặc tuyệt đối. Cảm biến gia số chỉ ra lượng thay đổi "
        "giữa vị trí hiện tại và một vị trí trước đó. Nếu thông tin mô tả vị trí hiện tại bị mất, do mất nguồn hay "
        "một nhiễu loạn khác, hệ thống phải được đặt lại. Trong khi đặt lại, cảm biến phải nằm ở một vị trí quy "
        "chiếu. Bộ mã hoá từ có thể được thiết kế để đọc theo kiểu gia số hoặc tuyệt đối. Bộ mã hoá quang, "
        "inductosyn và synchro/resolver cũng là những loại cảm biến dịch chuyển có thể thiết kế theo kiểu gia số "
        "hoặc tuyệt đối, nhưng được trình bày ở các chương khác."))
    b.append(p(
        "Phần lớn cảm biến vị trí dịch chuyển mô tả trong mục này đọc theo kiểu tuyệt đối. Chúng cung cấp một số "
        "đọc khoảng cách hay góc tính từ một mốc cố định, chứ không phải từ một vị trí trước đó. Có thể trừ hai số "
        "đọc liên tiếp để có một chỉ thị gia số. Cảm biến tuyệt đối chỉ ra vị trí hiện tại mà không cần biết vị trí "
        "trước đó. Nó không bao giờ phải được đặt lại về một vị trí quy chiếu để suy ra vị trí đo. Cảm biến dịch "
        "chuyển đọc tuyệt đối cũng thường được gọi là cảm biến vị trí."))
    b.append(p(
        "Các loại cảm biến từ sẽ được mô tả ở đây theo công nghệ được dùng, chứ không theo ứng dụng. Mức hữu ích "
        "tương đối của chúng cho phép đo thẳng hay đo góc sẽ được chỉ ra với từng loại. Công nghệ cảm biến từ không "
        "tiếp xúc dùng cho phép đo dịch chuyển gồm từ giảo, từ điện trở, hiệu ứng Hall và bộ mã hoá từ."))

    # ------------------------------------------------------------ terminology
    b.append(h2("Thuật ngữ từ trường", "Magnetic field terminology"))
    b.append(p(
        "<b>Cường độ từ trường</b> (H), hay lực từ hoá: lực làm sinh ra từ thông trong một vật liệu. H được đo bằng "
        "A·m⁻¹."))
    b.append(p(
        "<b>Cảm ứng từ</b> (B): lượng từ thông sinh ra do lực từ hoá đặt vào. B được đo bằng N/(A·m)."))
    b.append(p(
        "<b>Độ từ thẩm</b> (µ): khả năng của một vật liệu nâng đỡ các đường sức từ. Độ từ thẩm của một vật liệu "
        "bằng tích của độ từ thẩm tương đối của vật liệu ấy với độ từ thẩm của chân không. Độ từ thẩm tương đối "
        "của hầu hết vật liệu không chứa sắt gần bằng một. Trong chân không, cảm ứng từ liên hệ với cường độ từ "
        "trường theo công thức:"))
    b.append(eq("B = µ₀ · H"))
    b.append(p(
        "trong đó µ₀ là độ từ thẩm của chân không, có giá trị 4π × 10⁻⁷ H·m⁻¹. Trong các vật liệu khác, cảm ứng từ "
        "tại một điểm liên hệ với cường độ từ trường tại cùng điểm ấy theo:"))
    b.append(eq("B = µ · H"))
    b.append(p("với"))
    b.append(eq("µ = µ₀ · µ<sub>r</sub>"))
    b.append(p("và µ<sub>r</sub> là độ từ thẩm tương đối [1]."))
    b.append(p(
        "<b>Độ trễ</b>: hiện tượng trong đó trạng thái của một hệ không tuân theo một cách thuận nghịch những thay "
        "đổi của một tham số bên ngoài [2]. Trong một cảm biến dịch chuyển, đó là hiệu số giữa các số đọc thu được "
        "tại một điểm cho trước khi tiến tới điểm ấy từ phía tăng và từ phía giảm của thang đo. Hình 6-80 là một đồ "
        "thị đầu ra – đầu vào điển hình."))
    b.append(fig(80, F.fig_6_80()))
    b.append(p(
        "<b>Độ trễ từ</b>: được mô tả bằng vòng trễ trên Hình 6-81. Khi đặt một vật liệu sắt từ vào một từ trường "
        "xoay chiều, cảm ứng từ (B) chậm pha so với lực từ hoá (H) đã sinh ra nó. Diện tích dưới vòng trễ là tổn "
        "hao trễ trên mỗi chu kỳ, lớn với nam châm vĩnh cửu và nhỏ với các vật liệu từ có độ từ thẩm cao, tổn hao "
        "thấp [3]."))
    b.append(fig(81, F.fig_6_81()))
    b.append(p("<b>Bão hoà từ</b>: giới hạn trên của khả năng dẫn từ thông của vật liệu sắt từ."))
    b.append(p(
        "<b>Đường cong từ hoá</b>: cho biết lượng lực từ hoá cần thiết để một vật liệu sắt từ trở nên bão hoà. Đó là "
        "một đồ thị với B là tung độ và H là hoành độ (còn gọi là đường cong B–H). Đường cong từ hoá của một vật "
        "liệu cụ thể sẽ trông giống Hình 6-81, có thêm các dấu chia độ và đường cong được chỉnh để mô tả đặc tính "
        "của vật liệu ấy."))

    # ------------------------------------------------------------ magnetostrictive
    b.append(h2("Cảm biến từ giảo", "Magnetostrictive sensors"))
    b.append(p(
        "Cảm biến dịch chuyển từ giảo dùng một phần tử sắt từ để phát hiện vị trí của một nam châm vị trí dịch dọc "
        "theo chiều dài của nó. Nam châm vị trí được gắn vào chi tiết mà ta cần cảm nhận vị trí, còn thân cảm biến "
        "đứng yên, xem Hình 6-82. Nam châm vị trí di chuyển dọc vùng đo mà không tiếp xúc với phần tử cảm biến."))
    b.append(fig(82, F.fig_6_82()))
    b.append(p(
        "Những vật liệu sắt từ như sắt và niken thể hiện tính chất gọi là từ giảo. Việc đặt một từ trường lên "
        "những vật liệu này gây ra một biến dạng trong cấu trúc tinh thể, dẫn tới thay đổi kích thước và hình dạng "
        "của vật liệu. Vật liệu có từ giảo dương sẽ giãn ra khi bị từ hoá. Ngược lại, với từ giảo âm, vật liệu co "
        "lại khi bị từ hoá [4]."))
    b.append(p(
        "Các vật liệu sắt từ dùng trong cảm biến dịch chuyển từ giảo là những kim loại chuyển tiếp như sắt, niken "
        "và coban. Ở những kim loại này, lớp vỏ điện tử 3d chưa được lấp đầy hoàn toàn, điều đó cho phép hình thành "
        "mô men từ (các lớp vỏ gần hạt nhân đã đầy và không đóng góp vào mô men từ). Khi spin điện tử bị từ trường "
        "làm quay, tương tác giữa spin điện tử và quỹ đạo điện tử làm năng lượng điện tử thay đổi. Mạng tinh thể "
        "biến dạng để các điện tử ở bề mặt có thể chuyển về những trạng thái năng lượng thấp hơn [5]."))
    b.append(p(
        "Đáp ứng vật lý này của một vật liệu sắt từ là do sự có mặt của các mô men từ, và có thể hiểu bằng cách coi "
        "vật liệu như một tập hợp những nam châm vĩnh cửu tí hon gọi là đô men. Mỗi đô men gồm nhiều nguyên tử. Khi "
        "vật liệu chưa bị từ hoá, các đô men sắp xếp ngẫu nhiên. Tuy nhiên khi vật liệu bị từ hoá, các đô men định "
        "hướng với trục của chúng gần như song song với nhau. Tương tác của một từ trường bên ngoài với các đô men "
        "gây ra hiệu ứng từ giảo. Xem Hình 6-83. Hiệu ứng này có thể được tối ưu bằng cách điều khiển trật tự đô "
        "men thông qua chọn hợp kim, ủ nhiệt, biến dạng nguội và cường độ từ trường."))
    b.append(fig(83, F.fig_6_83()))
    b.append(p(
        "Trong khi việc đặt một từ trường gây ra biến dạng vật lý như mô tả ở trên, điều ngược lại cũng đúng: việc "
        "gây ứng suất làm thay đổi các tính chất từ (độ từ thẩm, độ cảm từ). Hiện tượng này gọi là hiệu ứng Villari."))
    b.append(p(
        "Trong cảm biến từ giảo, những biến dạng đều theo chiều dài như trên Hình 6-83 ít hữu ích. Thông thường "
        "người ta quay vectơ từ hoá bằng một từ trường nhỏ để tạo ra một biến dạng cục bộ, dùng hiệu ứng Wiedemann. "
        "Đó là một xoắn cơ học xuất hiện tại một điểm dọc một dây từ giảo khi cho một dòng điện chạy qua dây trong "
        "khi dây chịu một từ trường dọc trục. Hiện tượng xoắn xảy ra tại vị trí của từ trường dọc trục, thường do "
        "một nam châm vĩnh cửu nhỏ gọi là nam châm vị trí tạo ra."))
    b.append(p(
        "Trong một cảm biến dịch chuyển, một dây hoặc ống sắt từ gọi là ống dẫn sóng được dùng làm phần tử cảm biến, "
        "xem Hình 6-84. Cảm biến đo khoảng cách giữa nam châm vị trí và bộ thu. Để bắt đầu một phép đo, một xung "
        "dòng I (gọi là xung dò) được đưa vào ống dẫn sóng. Việc này làm xuất hiện tức thời một từ trường bao quanh "
        "ống trên toàn chiều dài của nó."))
    b.append(fig(84, F.fig_6_84()))
    b.append(p(
        "Trong một cảm biến vị trí từ giảo, dòng điện là một xung có độ dài khoảng 1 đến 2 µs. Một sóng cơ dạng "
        "xoắn được phát ra tại vị trí nam châm nhờ hiệu ứng Wiedemann. Các phần của sóng ấy lan theo cả hai chiều "
        "về phía và ra xa bộ thu. Phần sóng lan dọc ống dẫn sóng về phía bộ thu được phát hiện khi nó tới bộ thu. "
        "Phép đo thời gian từ lúc đặt xung dòng (lúc sóng xoắn được phát ra tại nam châm vị trí) cho tới lúc bộ thu "
        "phát hiện được nó chính là vị trí của nam châm vị trí. Tốc độ của sóng thường vào khoảng 3000 m·s⁻¹. Phần "
        "sóng lan ra xa bộ thu có thể trở thành tín hiệu nhiễu sau khi phản xạ ở đầu ống. Vì thế nó được một phần "
        "tử giảm chấn làm tắt dần khi tới đầu ống đối diện với bộ thu. Việc giảm chấn thường được thực hiện bằng "
        "cách gắn một trong nhiều cấu hình vật liệu đàn hồi khác nhau vào đầu ống dẫn sóng. Đoạn ống nằm trong "
        "phần tử giảm chấn không dùng được để xác định vị trí, và vì thế được gọi là “vùng chết”."))
    b.append(p(
        "Kết quả đo thời gian có thể được đệm và dùng trực tiếp làm đầu ra của cảm biến, hoặc được xử lý bên trong "
        "cảm biến để cho ra nhiều kiểu đầu ra khác nhau, gồm điện áp hay dòng điện tương tự, điều chế độ rộng xung, "
        "CANbus, SSI, HART, Profibus, v.v. Cảm biến vị trí từ giảo có thể được chế tạo ngắn chỉ 1 cm hoặc dài hơn "
        "30 m. Độ phân giải của các sản phẩm do MTS Systems Corp. chế tạo mịn tới 1 µm. Có thể đạt hệ số nhiệt 2 "
        "đến 5 ppm·°C⁻¹. Cảm biến vốn ổn định, vì phép đo dựa vào các tính chất vật lý của vật liệu làm ống dẫn "
        "sóng. Cảm biến dài trở nên rất hiệu quả về chi phí, bởi cùng một khối điện tử có thể điều khiển các cảm "
        "biến có chiều dài khác nhau; chỉ ống dẫn sóng và vỏ của nó phải kéo dài thêm để làm cảm biến dài hơn."))
    b.append(p(
        "Dây từ giảo có thể thẳng với cảm biến đo thẳng, hoặc được tạo hình để đo chuyển động cong hay chuyển động "
        "quay. Cảm biến cong thường được dùng để đo chuyển động góc hoặc phi tuyến trong các ứng dụng công nghiệp, "
        "tuy cảm biến từ giảo kiểu quay chưa thực sự phổ biến."))

    # ------------------------------------------------------------ magnetoresistive
    b.append(h2("Cảm biến từ điện trở", "Magnetoresistive sensors"))
    b.append(p(
        "Trong hầu hết vật liệu từ, điện trở giảm khi có một từ trường tác dụng và hướng từ hoá vuông góc với dòng "
        "điện chạy qua (dòng điện luôn tồn tại mỗi khi ta đo điện trở), xem Hình 6-85. Điện trở giảm khi cảm ứng từ "
        "tăng, cho tới khi vật liệu đạt bão hoà từ. Tốc độ giảm điện trở nhỏ dần khi vật liệu tới gần bão hoà. "
        "Lượng thay đổi điện trở vào cỡ 1% ở nhiệt độ phòng (0,3% với sắt, 2% với niken). Khi từ trường song song "
        "với dòng điện, điện trở tăng theo cường độ từ trường. Độ nhạy lớn nhất khi từ trường vuông góc với dòng "
        "điện. Đây là những tính chất của hiện tượng gọi là từ điện trở (MR). Hiệu ứng MR là do sự kết hợp của hai "
        "thành phần: sự giảm vận tốc tiến của hạt tải vì hạt tải bị buộc phải chuyển động ngang cũng như tiến, và "
        "sự giảm diện tích tiết diện hiệu dụng của vật dẫn vì hạt tải bị dồn về một phía [6]."))
    b.append(fig(85, F.fig_6_85()))
    b.append(p(
        "Khi một nam châm vị trí được đưa lại gần một phần tử cảm biến MR đơn lẻ, thay đổi điện trở đạt cực đại khi "
        "nam châm đi qua gần tâm của phần tử, rồi giảm dần cho tới khi nam châm đã đi qua khỏi phần tử. Điện trở "
        "thay đổi theo hệ thức"))
    b.append(eq("ρ = V / (n · v)", "6.111"))
    b.append(note(
        "Nguyên bản in công thức này dưới dạng “điện trở suất = điện áp / (nồng độ hạt tải × vận tốc hạt tải)”. Đó "
        "là dạng Drude quen thuộc ρ = E/(n·e·v), ở đây viết gọn lại thành ρ = V/(n·v) để nhấn mạnh rằng điện trở "
        "phụ thuộc vào cả nồng độ lẫn vận tốc hạt tải — và chính từ trường làm thay đổi cả hai, nên điện trở mới "
        "biến thiên theo từ trường."))
    b.append(p(
        "Bằng cách dùng nhiều phần tử MR bố trí dọc theo một đường, có thể chế tạo một thiết bị đo dịch chuyển dài "
        "hơn. Tín hiệu từ chuỗi cảm biến được giải mã để tìm ra những phần tử nào đang chịu ảnh hưởng của nam châm. "
        "Sau đó các số đọc riêng lẻ được dùng để xác định vị trí nam châm chính xác hơn. Có thể chế tạo được những "
        "cảm biến có hiệu năng tương đối cao. Độ nhạy nhiệt của các phần tử MR cần được bù, và cảm biến càng dài "
        "thì càng chứa nhiều phần tử cảm biến riêng lẻ. Vì thế cảm biến dài khó chế tạo hơn và đắt hơn."))
    b.append(p(
        "Vật liệu MR dị hướng có khả năng thay đổi điện trở trong khoảng 1% hoặc 2%. Có thể tăng hiệu ứng MR của "
        "một khối vật dẫn bằng cách làm nó thành composite gồm hai hay nhiều lớp vật liệu có mức từ điện trở khác "
        "nhau. Những cấu trúc đa lớp bằng vật liệu đặc biệt (đôi khi hơn 10 lớp) đã cho phép phát triển các vật "
        "liệu thể hiện hiệu ứng từ điện trở lớn hơn nhiều và bão hoà ở từ trường đặt vào lớn hơn. Hiện tượng này "
        "được đặt tên là từ điện trở khổng lồ (GMR). Một số cảm biến thương mại dựa trên GMR hiện đã có mặt. Các "
        "phần tử GMR có thể được bố trí thành một cầu bốn phần tử để có độ nhạy cao hơn. Trong cách bố trí ấy, hai "
        "phần tử được che chắn khỏi từ trường đặt vào, hai phần tử còn lại nhạy với từ trường ấy. Cũng có thể tăng "
        "độ nhạy bằng cách tích hợp các bộ tập trung từ thông lên những phần tử nhạy. Trong một mạch cầu, điện áp "
        "đầu ra có thể biến thiên hơn 5% điện áp nguồn [7]. Cảm biến quay có thể được chế tạo bằng cách gắn một "
        "mảnh cực từ lên một trục quay. Một hay nhiều nam châm vĩnh cửu và mảnh cực từ được sắp xếp để làm từ "
        "trường quanh phần tử MR thay đổi theo dịch chuyển góc."))
    b.append(p(
        "Người ta đang tiếp tục nghiên cứu vật liệu MR nhằm cải thiện độ nhạy bằng cách hạ cường độ từ trường cần "
        "thiết và tăng lượng thay đổi điện trở. Mức hiệu năng MR cao hơn kế tiếp được gọi là từ điện trở khổng lồ "
        "cực đại (CMR). CMR chưa thực dụng cho cảm biến công nghiệp vì những hạn chế nghiêm trọng về dải nhiệt độ "
        "làm việc."))
    b.append(p(
        "Tuy hiện nay MR, GMR và CMR còn bị hạn chế khi dùng trong cảm biến dịch chuyển bởi chi phí, nhiệt độ và "
        "các ràng buộc chế tạo, rất nhiều nghiên cứu đang được tiến hành. Biết đâu mức tiếp theo lại là từ điện trở "
        "“khổng lồ vô địch” (HMR)?"))
    b.append(quote("Biết đâu mức tiếp theo lại là từ điện trở “khổng lồ vô địch” (HMR)?",
                   "David S. Nyce, mục 6.9"))

    # ------------------------------------------------------------ Hall
    b.append(h2("Cảm biến hiệu ứng Hall", "Hall effect sensors"))
    b.append(p(
        "Hiệu ứng Hall là một tính chất thể hiện trong một vật dẫn chịu ảnh hưởng của từ trường. Một hiệu điện thế "
        "V<sub>H</sub>, gọi là điện áp Hall, xuất hiện trên vật dẫn khi một từ trường được đặt vuông góc với dòng "
        "điện. Chiều của nó vuông góc với cả từ trường lẫn dòng điện. Độ lớn của điện áp Hall tỉ lệ với cả cảm ứng "
        "từ lẫn dòng điện. Từ trường gây ra một gradien nồng độ hạt tải trên bề rộng vật dẫn. Số hạt tải ở một bên "
        "vật dẫn nhiều hơn bên kia chính là nguyên nhân của hiệu điện thế V<sub>H</sub>. Hình 6-86 là một biểu diễn "
        "bằng hình vẽ. Biên độ của điện áp thay đổi theo dòng điện và từ trường theo [8]:"))
    b.append(eq("V<sub>H</sub> = K<sub>H</sub> · β · I / z", "6.112"))
    b.append(p("trong đó V<sub>H</sub> là điện áp Hall; K<sub>H</sub> là hằng số Hall; β là cảm ứng từ; I là dòng "
               "điện chạy qua vật dẫn; z là bề dày của vật dẫn."))
    b.append(fig(86, F.fig_6_86()))
    b.append(p(
        "Cảm biến dùng hiệu ứng Hall thường được chế tạo bằng vật liệu bán dẫn, đem lại ưu điểm là cho phép lắng "
        "đọng mạch xử lý tín hiệu ngay trên cùng vật liệu ấy. Có thể dùng vật liệu bán dẫn loại p hoặc loại n, với "
        "chiều dòng điện tương ứng. Đầu ra lớn nhất đạt được khi hằng số Hall lớn, điều này đòi hỏi độ linh động "
        "hạt tải cao. Điện trở suất thấp sẽ hạn chế điện áp nhiễu nhiệt, cho một tỉ số tín hiệu trên nhiễu (SNR) "
        "hữu ích hơn. Những điều kiện này được tối ưu khi dùng bán dẫn loại n [6]."))
    b.append(p(
        "Có thể chế tạo một cảm biến dịch chuyển bằng một phần tử cảm biến Hall và một nam châm di động, với đầu "
        "ra tỉ lệ với khoảng cách giữa hai thứ. Có thể bố trí hai nam châm với một cảm biến Hall như trên Hình 6-87 "
        "để thu được cường độ từ trường gần bằng không khi cảm biến nằm cách đều hai nam châm. Những cấu hình một "
        "linh kiện Hall như thế có dải tuyến tính rất hẹp. Cảm biến dịch chuyển dải dài hơn có thể được chế tạo "
        "bằng nhiều cảm biến Hall rải dọc một đế mang. Một nam châm được cho di chuyển sát dọc theo đế ấy. Khi nam "
        "châm tới gần rồi đi ra xa từng phần tử Hall, các cảm biến tương ứng sẽ có đầu ra tăng hoặc giảm. Đầu ra "
        "của cả cụm cảm biến được suy ra bằng cách đọc đầu ra riêng của những cảm biến gần nam châm nhất, đồng "
        "thời giải mã xem đang đọc những cảm biến nào. Phương pháp này có thể cho ra những cảm biến dịch chuyển "
        "hiệu năng tương đối cao, dài tới vài mét. Cảm biến càng dài càng khó chế tạo và càng đắt vì số cảm biến "
        "phải ghép kênh càng nhiều. Có thể chế tạo cảm biến dịch chuyển góc cũng như dịch chuyển thẳng bằng cách "
        "sắp xếp cơ khí các phần tử cảm biến để làm từ trường biến thiên theo đầu vào góc hay đầu vào thẳng mong "
        "muốn."))
    b.append(fig(87, F.fig_6_87()))

    # ------------------------------------------------------------ magnetic encoders
    b.append(h2("Bộ mã hoá từ", "Magnetic encoders"))
    b.append(p(
        "Bộ mã hoá từ dùng một băng hoặc một đĩa môi trường từ trên đó thông tin số được lưu. Thông tin này được "
        "ghi ngay tại vị trí mà nó mô tả, dưới dạng một tập hợp các vùng đã từ hoá và chưa từ hoá. Một bộ mã hoá "
        "từ gồm phần tử cảm biến ấy, cùng một hay nhiều đầu đọc, mạch điện tử và một vỏ cơ khí có trục vào và các "
        "bạc lót. Với cảm biến đo thẳng, trục vào chuyển động ra vào. Trục có các vòng gạt để ngăn vật liệu lạ xâm "
        "nhập, và các bạc lót được thiết kế để chịu tải ngang. Cảm biến đo góc có trục quay, kèm các bạc lót chịu "
        "được tải dọc trục và tải ngang. Môi trường được mã hoá được thực hiện dưới dạng một băng trong cảm biến "
        "đo thẳng, hoặc một đĩa trong cảm biến đo góc."))
    b.append(p(
        "Khi một đầu đọc đi qua phía trên vùng được mã hoá, nó thu nhận các biến thiên từ và đọc thông tin vị trí. "
        "Thông tin ấy — các số 1 và 0 — thường được mã hoá thành nhiều rãnh song song để biểu diễn các chữ số nhị "
        "phân của thông tin vị trí. Mã nhị phân tiêu chuẩn gây ra một vấn đề cho bộ mã hoá: có những con số đòi "
        "hỏi nhiều bit phải đổi cùng lúc để chỉ ra một bước tăng đơn vị của con số được biểu diễn. Nếu mọi bit đang "
        "đổi không được căn chỉnh hoàn hảo với nhau, sẽ xuất hiện những số đọc sai tức thời. Để tránh vấn đề này, "
        "người ta dùng một biến thể đặc biệt của mã nhị phân gọi là “mã Gray”. Xem Bảng 6.25. Một bước tăng đơn vị "
        "của con số được biểu diễn chỉ làm đổi 1 bit trong mã Gray."))
    b.append(table(
        ["Số hệ 10", "Nhị phân “tự nhiên”", "Mã Gray", "Mã BCD (hàng chục / hàng đơn vị)"],
        [["0", "0000", "0000", "0000 0000"],
         ["1", "0001", "0001", "0000 0001"],
         ["2", "0010", "0011", "0000 0010"],
         ["3", "0011", "0010", "0000 0011"],
         ["4", "0100", "0110", "0000 0100"],
         ["5", "0101", "0111", "0000 0101"],
         ["6", "0110", "0101", "0000 0110"],
         ["7", "0111", "0100", "0000 0111"],
         ["8", "1000", "1100", "0000 1000"],
         ["9", "1001", "1101", "0000 1001"],
         ["10", "1010", "1111", "0001 0000"]],
        "Bảng 6.25 · Mã Gray so với mã nhị phân tự nhiên và mã BCD. Hai cột cuối cho thấy vì sao mã Gray lại quan "
        "trọng với bộ mã hoá: chỉ một bit đổi giữa hai số liên tiếp."))
    b.append(p(
        "Đầu đọc gồm một lõi sắt từ quấn cuộn dây vào và cuộn dây ra. Một xung đọc được đưa vào cuộn vào, và thông "
        "tin được đọc trên cuộn ra. Nếu lõi nằm trên một vùng đã từ hoá của môi trường từ thì lõi bị bão hoà, không "
        "có xung ra, và ta được một mức logic 0 [9]. Nếu lõi nằm trên một vùng chưa từ hoá khi xung đọc được đưa "
        "vào thì có một xung ra và tạo ra mức logic 1. Một cách bố trí khác thực dụng cho bộ mã hoá góc nhưng không "
        "thực dụng cho bộ mã hoá thẳng là dùng một nam châm vĩnh cửu nhiều cực hình vành khuyên. Nam châm này quay "
        "qua một cặp cảm biến để cho ra một số đọc gia số với các đầu ra sin và cosin (gọi là đầu ra “vuông pha”. "
        "Xem Hình 6-88). Dạng sóng có thể là xung vuông, sin hoặc tam giác. Hai đầu ra A và B được dùng để chỉ ra "
        "lượng dịch chuyển và chiều dịch chuyển. Số lần chuyển tiếp hay số “xung đếm” tỉ lệ với độ lớn dịch "
        "chuyển. Chiều dịch chuyển (tức dấu + hoặc –) có thể được tìm ra bằng cách so sánh hai pha. Chẳng hạn trên "
        "Hình 6-88, tại thời điểm pha A chuyển từ mức logic 0 lên 1, trạng thái của pha B sẽ chỉ ra chiều chuyển "
        "động. Mức logic 0 trên pha B có thể ứng với chiều dương; mức logic 1 ứng với chiều âm."))
    b.append(fig(88, F.fig_6_88()))
    b.append(p(
        "Bộ mã hoá từ có thể là gia số hoặc tuyệt đối. Ở cấu hình gia số, những xung cách đều được mã hoá trên môi "
        "trường từ và được đọc từ một hay nhiều rãnh. Các xung được một bộ đếm lên/xuống thu lại, và đầu ra của bộ "
        "đếm biểu diễn vị trí. Đầu ra vuông pha có thể được mã hoá để cho biết chiều dịch chuyển như mô tả ở trên. "
        "Mốc không được đặt bằng cách đặt lại bộ đếm. Bộ mã hoá từ tuyệt đối có mã số biểu diễn vị trí được mã "
        "hoá trực tiếp ngay tại vị trí ấy. Không cần bộ đếm. Mã Gray có thể được diễn giải để cho ra vị trí theo "
        "đơn vị kỹ thuật. Đôi khi người ta dùng cách mã hoá phi tuyến như sin hoặc cosin. Bảng 6.26 liệt kê một số "
        "cảm biến và nhà sản xuất."))
    b.append(table(
        ["Công nghệ", "Nhà sản xuất", "Mô tả", "Giá"],
        [
            ["Từ giảo", "MTS Systems Corp.<br>Cary, NC &amp; Đức",
             "Dài tới 20 m; độ phân giải 2 µm; CAN, SSI, Profibus, HART", "150 – 3000 USD"],
            ["", "Balluff<br>Đức",
             "Dài tới 3,5 m; độ phân giải 20 µm; đầu đo không có giao diện chuẩn", "400 – 2300 USD"],
            ["Từ điện trở", "Nonvolatile Electronics<br>Eden Prairie, MN",
             "Cảm biến GMR có bộ tập trung từ thông và vỏ che", "2,50 – 6,00 USD"],
            ["", "Midori America<br>Fullerton, CA",
             "Cảm biến từ điện trở loại quay; loại thẳng tới 30 mm", "64 – 500 USD<br>67 – 200 USD"],
            ["Hiệu ứng Hall", "Optec Technology, Inc.<br>Carrollton, TX",
             "Đo vị trí thẳng", "5 – 50 USD"],
            ["", "Spectec<br>Emigrant, MT",
             "Cảm biến tiêu chuẩn và theo yêu cầu", "khoảng 90 USD"],
            ["Bộ mã hoá từ", "Heidenhain<br>Schaumburg, IL",
             "Bộ mã hoá quay và bộ mã hoá thẳng", "300 – 2000 USD"],
            ["", "Sony Precision Technology America<br>Orange, CA",
             "Bộ mã hoá quay và bộ mã hoá thẳng", "100 – 2000 USD"],
        ],
        "Bảng 6.26 · Cảm biến và nhà sản xuất. Giá theo thời giá năm 1999."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "O. Esbach, <i>Handbook of Engineering Fundamentals</i>, New York: John Wiley &amp; Sons, 1975, 957.",
        "R. Lerner and G. Trigg, <i>Encyclopedia of Physics</i>, New York: VCH Publishers, 1990, 529.",
        "P. Neelakanta, <i>Handbook of Electromagnetic Materials</i>, Boca Raton, FL: CRC Press, 1995, 333.",
        "D. S. Nyce, Magnetostriction-based linear position sensors, <i>Sensors</i>, 11(4), 22, 1994.",
        "R. Philippe, <i>Electrical and Magnetic Properties of Materials</i>, Norwood, MA: Artech House, 1988.",
        "H. Burke, <i>Handbook of Magnetic Phenomena</i>, New York: Van Nostrand Reinhold, 1986.",
        "Nonvolatile Electronics Inc., NVSB series datasheet, March 1996.",
        "J. R. Carstens, <i>Electrical Sensors and Transducers</i>, Englewood Cliffs, NJ: Regents/Prentice-Hall, "
        "1992, 125.",
        "H. Norton, <i>Handbook of Transducers</i>, Englewood Cliffs, NJ: Prentice-Hall, 1989, 106–112.",
    ]))

    b.append(h2("Đọc thêm", "Further information"))
    b.append(ul([
        "B. D. Cullity, <i>Introduction to Magnetic Materials</i>, Reading, MA: Addison-Wesley, 1972.",
        "D. Craik, <i>Magnetism Principles and Applications</i>, New York: John Wiley &amp; Sons, 1995.",
        "P. Lorrain and D. Corson, <i>Electromagnetic Fields and Waves</i>, San Francisco: W. H. Freeman, 1962.",
        "R. Boll, <i>Soft Magnetic Materials</i>, London: Heyden &amp; Son, 1977.",
        "H. Olson, <i>Dynamical Analogies</i>, New York: D. Van Nostrand, 1943.",
        "D. Askeland, <i>The Science and Engineering of Materials</i>, Boston: PWS-Kent Publishing, 1989.",
        "R. Rose, L. Shepard and J. Wulff, <i>The Structure and Properties of Materials</i>, New York: John Wiley "
        "&amp; Sons, 1966.",
        "J. Shackelford, <i>Introduction to Materials Science for Engineers</i>, New York: Macmillan, 1985.",
        "D. Jiles, <i>Introduction to Magnetism and Magnetic Materials</i>, London: Chapman and Hall, 1991.",
        "F. Mazda, <i>Electronics Engineer’s Reference Book</i>, 6th ed., London: Butterworth, 1989.",
        "E. Herceg, <i>Handbook of Measurement and Control</i>, New Jersey: Schaevitz Engineering, 1976.",
    ]))
    b.append(nav(9, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Four sensing principles share this section, and they are more different than the heading suggests. "
        "Magnetostriction measures a time of flight along a wire; magnetoresistance and the Hall effect measure a "
        "field at a point; magnetic encoders read a code. What they have in common is only that the quantity "
        "carried between the moving part and the fixed part is a magnetic field — and that is the reason all four "
        "are non-contacting."))
    b.append(p(
        "The distinction between displacement and position is worth holding on to. Displacement is a change; "
        "position is a coordinate. Most of the sensors in this section actually report position from a fixed datum "
        "and let you subtract consecutive readings to get displacement, which is why the author calls them position "
        "sensors rather than displacement sensors. Only the incremental encoder is genuinely a displacement device, "
        "and it is the only one that needs to be re-zeroed after a power loss."))

    b.append(h2("Two curves you must know how to read", "Hai đường cong phải biết đọc"))
    b.append(fig(80, F.fig_6_80(), "en"))
    b.append(p(
        "Figure 6.80 is the practical one: hysteresis as a specification. The two branches are the same sensor "
        "approached from below and from above, and their separation is what you will see when a machine reverses "
        "direction and the reading does not come back to where it was. It is quoted as a percentage of full scale "
        "because it is a property of the whole chain — sensing element, conditioning, and mechanics."))
    b.append(fig(81, F.fig_6_81(), "en"))
    b.append(p(
        "Figure 6.81 is the material one. The loop area is energy lost per cycle, which matters enormously in a "
        "transformer core and hardly at all in a position sensor; what matters here is the shape near the origin. "
        "Remanence B_r is how much flux stays when you remove the field — that is what makes a permanent magnet a "
        "permanent magnet. Coercivity H_c is how hard it is to push that flux back to zero, and it is the single "
        "number that separates a soft magnetic core (low H_c, easy to magnetise and demagnetise, used for "
        "waveguides and read-head cores) from a hard magnetic material (high H_c, used for the position magnet "
        "itself)."))

    b.append(h2("Magnetostriction: a sensor built on a time of flight", "Từ giảo: cảm biến dựa trên thời gian bay"))
    b.append(fig(82, F.fig_6_82(), "en"))
    b.append(p(
        "The magnetostrictive sensor is the most interesting device in this section because nothing in it moves "
        "except a sound wave. A current pulse is sent down a wire; at the position magnet, the combination of that "
        "axial field and the circumferential field of the current produces a local twist — the Wiedemann effect — "
        "and the twist runs both ways along the wire. The time it takes to reach the pickup at the far end is the "
        "distance, divided by about 3000 m/s."))
    b.append(fig(83, F.fig_6_83(), "en"))
    b.append(fig(84, F.fig_6_84(), "en"))
    b.append(p(
        "Three numbers explain the whole product category. First, 3000 m/s is roughly nine microseconds per metre "
        "round trip, so a one-metre sensor answers in under 20 µs and the electronics, not the wave, sets the "
        "update rate. Second, the resolution of 1 µm comes from timing, not from the wavelength: a 1 µm change "
        "shifts the arrival by about 0.3 ns, which is well inside what a fast comparator can resolve against a "
        "repeated pulse. Third, the temperature coefficient of 2–5 ppm/°C is a property of the wire — the speed of "
        "sound in the alloy — not of the electronics, which is why these sensors hold their calibration."))
    b.append(p(
        "The damping element is the part everyone forgets and nobody should. Without it, the wave travelling away "
        "from the pickup reflects off the far end and comes back as a second arrival, which the timing circuit will "
        "happily measure as a second, phantom magnet. The dead zone is simply the length of wire buried in the "
        "damper, and it is why a magnetostrictive sensor cannot measure right up to its own end cap."))

    b.append(h2("Magnetoresistance and the Hall effect", "Từ điện trở và hiệu ứng Hall"))
    b.append(fig(85, F.fig_6_85(), "en"))
    b.append(p(
        "Magnetoresistance is a small effect — one per cent at room temperature — and the section is honest about "
        "it. That one per cent is why a single MR element makes a poor position sensor and why the useful "
        "configurations are either a bridge of four elements or a long string of elements with decoding. The "
        "interesting development is GMR: by stacking alternating magnetic and non-magnetic layers a few atoms "
        "thick, the resistance change rises by an order of magnitude or more, and the effect saturates at higher "
        "fields. That is what made the read head in a hard disk drive possible, and it is the same physics that "
        "gives you a practical magnetic position sensor."))
    b.append(fig(86, F.fig_6_86(), "en"))
    b.append(p(
        "The Hall effect is the opposite trade: a large, easily conditioned output from a device that measures the "
        "field at one point and nothing else. That is why Hall sensors dominate in cheap angular position sensing "
        "and in brushless motor commutation, and why they are poor at long linear travel — you need hundreds of "
        "them, multiplexed, with a decoding scheme that knows which one is talking. The formula V_H = K_H β I / z "
        "says the output scales with current and inversely with thickness, which is why a Hall plate is made as "
        "thin as the process allows."))
    b.append(fig(87, F.fig_6_87(), "en"))
    b.append(p(
        "The two-magnet arrangement in Figure 6.87 is a neat trick: put the sensor where the fields cancel and you "
        "get a bipolar output that crosses zero at a known position, with good linearity near the crossing and a "
        "well-defined sign either side. It is the magnetic equivalent of a Wheatstone bridge null — you are "
        "measuring a difference of two nearly equal quantities, so the common-mode part of the field cancels."))

    b.append(h2("Magnetic encoders and the Gray code", "Bộ mã hoá từ và mã Gray"))
    b.append(p(
        "The Gray code appears twice in this chapter — in the optical section and here — and for the same reason. "
        "Any absolute encoder that reads several parallel tracks at once has a transition where all the bits change "
        "together, and at that instant the reading is whatever the mechanical tolerances allow it to be. Gray code "
        "removes the problem at the source by making consecutive words differ in exactly one bit. Table 6.25 is "
        "worth reading column by column: the natural binary column changes several bits at every step, the Gray "
        "column never changes more than one, and the BCD column shows why a decimal display needs a different code "
        "entirely."))
    b.append(fig(88, F.fig_6_88(), "en"))
    b.append(p(
        "The read head itself is a small transformer with a saturable core. A read pulse into the primary produces "
        "an output pulse only if the core is not already saturated by the recorded medium — so a magnetised area "
        "reads as 0 and an unmagnetised area as 1. It is a destructive-looking scheme that is in fact entirely "
        "non-destructive: the read pulse is far too weak to alter the recording."))
    b.append(table(
        ["Technology", "Manufacturer", "Description", "Price"],
        [
            ["Magnetostrictive", "MTS Systems Corp.<br>Cary, NC &amp; Germany",
             "Lengths to 20 m; 2 µm resolution; CAN, SSI, Profibus, HART", "$150 – $3000"],
            ["", "Balluff<br>Germany",
             "Lengths to 3.5 m; 20 µm resolution; no standard interfaces in head", "$400 – $2300"],
            ["Magnetoresistive", "Nonvolatile Electronics<br>Eden Prairie, MN",
             "GMR sensors with flux concentrator and shield", "$2.50 – $6.00"],
            ["", "Midori America<br>Fullerton, CA",
             "Rotary MR sensors; linear MR up to 30 mm", "$64 – $500<br>$67 – $200"],
            ["Hall effect", "Optec Technology, Inc.<br>Carrollton, TX",
             "Linear position", "$5 – $50"],
            ["", "Spectec<br>Emigrant, MT",
             "Standard and custom sensors", "approx. $90"],
            ["Magnetic encoder", "Heidenhain<br>Schaumburg, IL",
             "Rotary and linear encoders", "$300 – $2000"],
            ["", "Sony Precision Technology America<br>Orange, CA",
             "Rotary and linear encoders", "$100 – $2000"],
        ],
        "Table 6.26 · Sensors and manufacturers. Prices are as of 1999."))
    b.append(nav(9, "en"))
    return "".join(b)
