# -*- coding: utf-8 -*-
"""Handbook 6.1 — Resistive Displacement Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Cảm biến dịch chuyển điện trở thường được gọi là biến trở hay “pot”. Biến trở là một thiết bị cơ điện "
        "gồm một chổi quét dẫn điện trượt trên một phần tử điện trở cố định, theo vị trí hoặc góc của một trục "
        "bên ngoài. Xem Hình 6-1. Về mặt điện, phần tử điện trở bị “chia” tại đúng điểm tiếp xúc của chổi quét. "
        "Để đo dịch chuyển, biến trở thường được mắc theo cấu hình cầu phân áp như trên Hình 6-2. Đầu ra của "
        "mạch — một hàm của vị trí chổi quét — là một điện áp tương tự, dùng trực tiếp được hoặc số hoá được. "
        "Việc hiệu chuẩn sẽ ánh xạ điện áp ra thành đơn vị dịch chuyển."))
    b.append(p(
        "Bảng 6.1 liệt kê một số thuộc tính cố hữu của biến trở. Mục này trình bày các loại biến trở hiện có, "
        "đặc tính điện và cơ của chúng, cùng những cách thực tế để dùng chúng cho đo lường chính xác. Nguồn "
        "cung cấp và giá điển hình cũng được bàn tới. Linh hoạt, rẻ và dễ dùng, biến trở là lựa chọn phổ biến "
        "cho đo lường chính xác."))
    b.append(fig(1, F.fig_6_1()))

    b.append(table(
        ["Ưu điểm", "Nhược điểm"],
        [["Dễ dùng", "Băng thông hạn chế"],
         ["Giá thấp", "Tải do ma sát"],
         ["Không cần điện tử", "Tải do quán tính"],
         ["Tín hiệu ra biên độ lớn", "Mài mòn"],
         ["Công nghệ đã được khẳng định", "—"]],
        "Bảng 6-1 · Những đặc tính cơ bản của biến trở."))

    b.append(h2("Biến trở chính xác", "Precision Potentiometers"))
    b.append(p(
        "Biến trở có rất nhiều loại, mỗi loại được tối ưu cho một ứng dụng riêng. Đo vị trí đòi hỏi một biến "
        "trở chất lượng cao, được thiết kế để làm việc lâu dài. Cần tránh những loại được xếp vào nhóm biến "
        "trở tinh chỉnh (<i>trimmer</i>), biến trở điều chỉnh dòng, bộ suy giảm, chiết áp âm lượng, núm điều "
        "khiển bảng… mà hãy tìm đúng loại <b>biến trở chính xác</b>."))

    b.append(h3("Các loại biến trở chính xác", "Types of Precision Potentiometers"))
    b.append(p(
        "Biến trở chính xác có ba dạng: quay, chuyển động thẳng và dạng dây cáp. Biến trở dây cáp — còn gọi là "
        "biến trở cáp, biến trở “yo-yo”, đầu đo giãn cáp hay đầu đo kéo dây — đo chiều dài kéo ra của một sợi "
        "cáp có lò xo căng. Biến trở quay có loại một vòng hoặc nhiều vòng, thông dụng là 3, 5 hoặc 10 vòng. "
        "Biến trở chuyển động thẳng có hành trình cực đại từ khoảng 5 mm đến hơn 4 m [1, 2]. Biến trở dây cáp "
        "có thể kéo dài quá 50 m [3]. Nhà sản xuất thường ghi rõ kiểu, kích thước, thành phần phần tử điện trở, "
        "các tham số điện và cơ, cùng phương pháp lắp đặt."))

    b.append(h3("Phần tử điện trở", "Resistive Element"))
    b.append(p(
        "Nói rộng ra, phần tử điện trở của biến trở có thể chia thành loại quấn dây và loại không quấn dây. "
        "Phần tử quấn dây gồm những vòng dây điện trở quấn sát nhau, làm phép đo bị lượng tử hoá thành từng "
        "bậc. Ngược lại, phần tử không quấn dây là một tấm vật liệu điện trở liên tục, về nguyên tắc cho độ "
        "phân giải không giới hạn."))
    b.append(p(
        "Phần tử quấn dây có độ ổn định nhiệt tuyệt vời và khả năng tiêu tán công suất cao. Các vòng dây lượng "
        "tử hoá phép đo theo cỡ và bước dây. Nếu chấp nhận được giới hạn độ phân giải ấy, phần tử quấn dây là "
        "lựa chọn thoả đáng cho đo lường chính xác; tuy vậy, phần tử nhựa dẫn điện hoặc loại lai thường làm "
        "việc tốt hơn và chịu được số chu trình nhiều hơn hẳn. Những loại không quấn dây thông dụng được mô tả "
        "kỹ hơn dưới đây."))
    b.append(p(
        "<b>Phần tử nhựa dẫn điện</b> là một màng nhẵn cho độ phân giải không giới hạn, ma sát thấp, tạp âm "
        "thấp và tuổi thọ làm việc dài. Chúng nhạy với nhiệt độ và các yếu tố môi trường khác, khả năng tiêu "
        "tán công suất thấp; bù lại, đây là lựa chọn xuất sắc cho hầu hết ứng dụng đo lường chính xác."))
    b.append(p(
        "<b>Phần tử lai</b> gồm một lõi quấn dây phủ lớp nhựa dẫn điện, kết hợp hai công nghệ để có được một "
        "số ưu điểm đáng mong của cả hai. Lớp nhựa hạn chế khả năng tiêu tán công suất để đổi lấy tạp âm thấp, "
        "tuổi thọ dài và độ phân giải không giới hạn. Giống loại quấn dây, loại lai có độ ổn định nhiệt tuyệt "
        "vời. Đây là lựa chọn xuất sắc cho đo lường chính xác."))
    b.append(p(
        "<b>Phần tử gốm kim loại</b> (cermet), chế từ hợp kim gốm – kim loại, cho độ phân giải không giới hạn "
        "và mức tạp âm chấp nhận được. Ưu điểm gồm khả năng tiêu tán công suất cao và độ ổn định tuyệt vời "
        "trong điều kiện khắc nghiệt. Loại này hiếm khi được dùng cho đo lường chính xác vì nhựa dẫn điện cho "
        "tạp âm thấp hơn, ma sát thấp hơn và tuổi thọ dài hơn."))
    b.append(p(
        "<b>Phần tử than – nhựa</b> (carbon composition), được ép khuôn từ hỗn hợp than và nhựa, rẻ và rất phổ "
        "biến cho mục đích thông thường, nhưng không dùng cho đo lường chính xác. Chúng cho độ phân giải không "
        "giới hạn và tạp âm thấp, nhưng nhạy với ứng suất môi trường (nhiệt độ, độ ẩm) và bị mài mòn."))
    b.append(p("Bảng 6.2 tóm tắt những đặc tính phân biệt của các phần tử điện trở được ưu tiên dùng cho đo "
               "lường chính xác."))
    b.append(table(
        ["", "Nhựa dẫn điện", "Quấn dây", "Lai"],
        [["Độ phân giải", "Vô cùng nhỏ", "Bị lượng tử hoá", "Vô cùng nhỏ"],
         ["Định mức công suất", "Thấp", "Cao", "Thấp"],
         ["Độ ổn định nhiệt", "Kém", "Tuyệt vời", "Rất tốt"],
         ["Tạp âm", "Rất thấp", "Thấp, nhưng tăng theo thời gian", "Thấp"],
         ["Tuổi thọ", "10<sup>6</sup>–10<sup>8</sup> chu trình",
          "10<sup>5</sup>–10<sup>6</sup> chu trình", "10<sup>6</sup>–10<sup>7</sup> chu trình"]],
        "Bảng 6-2 · Đặc tính của ba loại phần tử điện trở dùng cho biến trở chính xác."))

    b.append(h2("Đặc tính điện", "Electrical Characteristics"))
    b.append(p("Trước khi chọn một biến trở và tích hợp nó vào hệ đo, cần xét những đặc tính điện sau đây."))

    b.append(h3("Đầu nối và điểm rút", "Terminals and Taps"))
    b.append(p(
        "Bảng 6.3 cho thấy cách đánh dấu quy ước trên vỏ biến trở [4, 5]; CW và CCW chỉ chiều quay theo kim "
        "đồng hồ và ngược kim đồng hồ khi nhìn từ mặt trước. Các cách đấu nối thông dụng gồm chân hàn và khoen, "
        "đầu nối liền khối, và dây ra tự do. Ngoài chổi quét và hai đầu mút, biến trở có thể có thêm một hay "
        "nhiều đầu nối cho các điểm rút (<i>tap</i>). Điểm rút cho phép đấu điện tới một điểm xác định trên "
        "phần tử điện trở. Đôi khi người ta nối một điện trở shunt vào điểm rút để sửa dạng hàm ra. Đầu mút và "
        "điểm rút có thể có đặc tính điện khác nhau tuỳ cách chế tạo. Xem [2] để biết thêm."))
    b.append(table(
        ["Đầu nối", "Mã màu có thể gặp", "", "Biến trở quay", "Biến trở chuyển động thẳng"],
        [["1", "Vàng", "Đỏ", "Đen", "CCW — giới hạn ngược chiều kim đồng hồ", "Hết hành trình thu vào"],
         ["2", "Đỏ", "Xanh lá", "Trắng", "Chổi quét", "Chổi quét"],
         ["3", "Xanh lá", "Đen", "Đỏ", "CW — giới hạn theo chiều kim đồng hồ", "Hết hành trình kéo ra"]],
        "Bảng 6-3 · Cách đánh dấu đầu nối trên biến trở. Màu sắc chỉ là quy ước của từng hãng, không phải "
        "chuẩn chung; luôn kiểm tra bằng đồng hồ vạn năng."))

    b.append(h3("Dạng hàm ra (taper)", "Taper"))
    b.append(p(
        "Biến trở có nhiều dạng hàm ra khác nhau, quyết định hình dạng của hàm truyền. Với biến trở tuyến tính, "
        "điện áp ra biến đổi bậc nhất theo chuyển động của chổi quét, như trên Hình 6-2. (Cần phân biệt biến "
        "trở có hàm ra tuyến tính với biến trở chuyển động thẳng, đôi khi cũng được gọi là “biến trở thẳng”.) "
        "Biến trở tuyến tính là loại phổ biến nhất và được dùng rộng rãi trong đo lường và điều khiển. Biến "
        "trở có hàm ra phi tuyến (logarit, sin, cos, tang, bình phương, lập phương) cũng có thể hữu ích, nhất "
        "là khi không có điều khiển bằng máy tính. Hàm ra không chuẩn có thể đặt chế tạo riêng, hoặc có thể "
        "tạo ra bằng điện trở shunt, bằng cách ghép đầu ra của nhiều biến trở cùng trục, hay bằng cách khác "
        "(xem [6, 7]). Tất nhiên, nếu có máy tính thì luôn có thể sửa hàm ra bằng bảng tra hay hàm ánh xạ trong "
        "phần mềm."))

    b.append(h3("Hành trình điện", "Electrical Travel"))
    b.append(p(
        "Hình 6-2 cho thấy đầu ra lí tưởng của biến trở thay đổi thế nào theo vị trí chổi quét. Trong thực tế, "
        "ở mỗi đầu có một vùng nhỏ mà tại đó đầu ra giữ nguyên cho tới khi chổi quét chạm cữ cơ khí. Hành trình "
        "cơ khí là toàn bộ dải chuyển động của chổi quét, còn hành trình điện là dải chuyển động nhỏ hơn một "
        "chút, trên đó đầu ra điện mới “hợp lệ”. Vì vậy, khi dùng biến trở làm cảm biến, điều quan trọng là "
        "phải bảo đảm chuyển động của chổi quét nằm trong giới hạn hành trình điện."))

    b.append(h3("Độ tuyến tính", "Linearity"))
    b.append(p(
        "Độ tuyến tính là mức lệch cực đại của hàm ra so với một đường thẳng lí tưởng. Người ta thường công bố "
        "độ tuyến tính độc lập, trong đó đường thẳng được định nghĩa là đường làm sai số tuyến tính nhỏ nhất "
        "trên một loạt điểm lấy mẫu, không nhất thiết phải đo trên toàn dải của biến trở. Xem Hình 6-3. Các "
        "thước đo tuyến tính khác như tuyến tính theo đầu mút, tuyến tính tuyệt đối và tuyến tính theo điểm "
        "không cũng đôi khi được dùng; xem [8]. Biến trở thường có độ tuyến tính độc lập từ dưới 0,1 % đến "
        "1 %. Khi hàm ra phi tuyến, người ta công bố độ tuân thủ (<i>conformity</i>) vì đây là thuật ngữ tổng "
        "quát hơn, dùng để chỉ mức lệch so với một hàm lí tưởng bất kỳ. Độ tuân thủ và độ tuyến tính thường "
        "được biểu diễn theo phần trăm của đầu ra toàn thang (FSO)."))
    b.append(fig(3, F.fig_6_3()))

    b.append(h3("Tải điện", "Electrical Loading"))
    b.append(p(
        "Tải có thể ảnh hưởng đáng kể đến độ tuyến tính của phép đo, bất kể chất lượng và kết cấu của biến "
        "trở. Hãy xét một biến trở tuyến tính lí tưởng nối với tải có trở kháng vô cùng lớn (như trên Hình "
        "6-2). Vì không có dòng chạy qua tải, đầu ra biến đổi tuyến tính hoàn hảo khi chổi quét chạy dọc "
        "chiều dài biến trở. Nhưng nếu trở kháng tải hữu hạn, tải sẽ rút dòng và làm méo đầu ra như minh hoạ "
        "trên Hình 6-4. Phân tích mạch cho kết quả:"))
    b.append(eq("v<sub>o</sub> / v<sub>r</sub> = (x/x<sub>P</sub>) / "
                "[ 1 + (x/x<sub>P</sub>)(1 − x/x<sub>P</sub>)·(R<sub>P</sub>/R<sub>L</sub>) ]", "6.1"))
    b.append(p(
        "Do đó cần làm cho R<sub>L</sub>/R<sub>P</sub> càng lớn càng tốt để giảm ảnh hưởng của tải (việc này "
        "cũng kéo theo những đánh đổi khác sẽ bàn sau). Người ta thường lấy R<sub>L</sub>/R<sub>P</sub> ≥ 10 "
        "làm nguyên tắc, vì khi đó sai số do tải được giữ dưới 1 % đầu ra toàn thang. Một số nhà sản xuất còn "
        "khuyến nghị một trở kháng tải tối thiểu hoặc dòng chổi quét tối đa nhằm giảm ảnh hưởng của tải và "
        "tránh làm hỏng tiếp điểm chổi quét. Ngoài ra có thể áp dụng thêm các biện pháp sau:"))
    b.append(ul([
        "Dùng nguồn áp đã ổn định, có đầu ra không đổi khi tải thay đổi.",
        "Dùng mạch điều hoà tín hiệu hoặc mạch thu thập dữ liệu có trở kháng vào lớn.",
        "Chỉ dùng một phần hành trình toàn phần của biến trở.",
    ]))
    b.append(fig(4, F.fig_6_4()))

    b.append(h3("Độ phân giải", "Resolution"))
    b.append(p(
        "Độ phân giải xác định mức thay đổi nhỏ nhất của đầu ra có thể tạo ra và phát hiện được. Ở biến trở "
        "quấn dây, chuyển động của chổi quét trên các vòng dây sinh ra đáp ứng lượng tử hoá; do đó độ phân "
        "giải tốt nhất đạt được là r = (1/N)×100 %, với N là số vòng dây. Biến trở không quấn dây cho đáp ứng "
        "liên tục với độ phân giải không giới hạn; biến trở lai cũng thuộc nhóm này. Trong thực tế, độ phân "
        "giải luôn bị giới hạn bởi những yếu tố sau:"))
    b.append(ul([
        "Tạp âm điện — với biến trở quấn dây thường được công bố là “tạp âm”, với loại không quấn dây là “độ "
        "trơn”, cả hai tính theo phần trăm đầu ra toàn thang [10].",
        "Độ ổn định của nguồn áp, vốn có thể đưa thêm tạp âm vào tín hiệu đo.",
        "Độ phân giải của bộ chuyển đổi tương tự – số (ADC), thường tính theo “bit” (ví dụ hành trình 10 mm "
        "số hoá bằng ADC 12 bit cho độ phân giải tốt nhất 10 mm/4096 = 0,0024 mm).",
        "Các hiệu ứng cơ như ma sát tĩnh (stiction).",
    ]))

    b.append(h3("Định mức công suất", "Power Rating"))
    b.append(p(
        "Công suất tiêu tán trên biến trở là P = v<sub>r</sub><sup>2</sup>/R<sub>P</sub>. Vì vậy định mức công "
        "suất quyết định điện áp lớn nhất có thể đặt lên biến trở ở một nhiệt độ cho trước. Điện áp cấp càng "
        "lớn thì đầu ra (và tạp âm) càng lớn nhưng công suất tiêu tán cũng tăng, dẫn tới hiệu ứng nhiệt mạnh "
        "hơn. Nói chung biến trở quấn dây và gốm kim loại tản nhiệt tốt hơn nên có định mức công suất cao nhất."))

    b.append(h3("Hệ số nhiệt", "Temperature Coefficient"))
    b.append(p(
        "Khi nhiệt độ tăng, điện trở của biến trở cũng tăng. Tuy vậy, một biến trở mắc như trên Hình 6-2 vẫn "
        "chia áp tốt như nhau bất kể tổng trở của nó, nên ảnh hưởng nhiệt thường không phải là vấn đề lớn, miễn "
        "là thay đổi điện trở đồng đều và biến trở làm việc trong định mức. Tuy nhiên, điện trở tăng cũng làm "
        "tăng độ phi tuyến do tải, nên hệ số nhiệt có thể trở thành yếu tố quan trọng. Hệ số nhiệt, thường "
        "tính bằng ppm·°C<sup>−1</sup>, có thể biểu diễn là α = (ΔR<sub>P</sub>/R<sub>P</sub>)/Δt, với Δt là "
        "mức thay đổi nhiệt độ và ΔR<sub>P</sub> là mức thay đổi tương ứng của tổng trở. Nói chung biến trở "
        "quấn dây có hệ số nhiệt thấp nhất. Cũng có thể dùng mạch điều hoà tín hiệu bù nhiệt."))

    b.append(h3("Điện trở", "Resistance"))
    b.append(p(
        "Vì biến trở chia áp tốt như nhau bất kể tổng trở, dung sai điện trở thường không phải là vấn đề lớn. "
        "Nhưng tổng trở có ảnh hưởng mạnh đến hiệu ứng tải. Nếu điện trở lớn, dòng qua biến trở nhỏ hơn nên "
        "giảm hiệu ứng nhiệt, nhưng lại làm tăng tải."))

    b.append(h3("Kích thích xoay chiều", "AC Excitation"))
    b.append(p(
        "Biến trở có thể làm việc với nguồn một chiều hoặc xoay chiều. Tuy nhiên, biến trở quấn dây chịu ảnh "
        "hưởng của hiệu ứng điện dung và điện cảm, có thể đáng kể ở tần số trung bình đến cao."))

    b.append(h2("Đặc tính cơ", "Mechanical Characteristics"))
    b.append(p("Những đặc tính cơ sau đây ảnh hưởng đến chất lượng phép đo và độ tin cậy của hệ, nên cần xét "
               "khi chọn biến trở."))

    b.append(h3("Tải cơ", "Mechanical Loading"))
    b.append(p(
        "Biến trở thêm quán tính và ma sát vào các bộ phận chuyển động của hệ mà nó đo, do đó làm tăng lực cần "
        "để dịch chuyển các bộ phận ấy. Hiệu ứng này gọi là tải cơ. Để định lượng tải cơ, nhà sản xuất biến "
        "trở quay thường nêu ba giá trị: mô men quán tính tương đương của các phần quay, mô men động (mô men "
        "chạy) cần để duy trì chuyển động quay của trục, và mô men khởi động cần để bắt đầu quay. Với biến "
        "trở chuyển động thẳng, ba đại lượng tương ứng là khối lượng, lực khởi động và lực động (lực chạy)."))
    b.append(p(
        "Trong những trường hợp cực đoan, tải cơ có thể làm thay đổi xấu đặc tính vận hành của hệ. Khi đưa "
        "biến trở vào thiết kế, cần bảo đảm quán tính thêm vào hệ là không đáng kể, hoặc phải tính đến nó khi "
        "phân tích dữ liệu từ biến trở. Cũng nên xét các giá trị lực/mô men khởi động và chạy, dù chúng thường "
        "nhỏ nhờ dùng ổ trục và phần tử điện trở ma sát thấp."))

    b.append(h3("Hành trình cơ", "Mechanical Travel"))
    b.append(p(
        "Khác với hành trình điện, hành trình cơ là toàn bộ dải chuyển động của chổi quét. Mỗi đầu dải chuyển "
        "động có một cữ cơ khí giới hạn hành trình cơ. Cữ chỉ chịu được tải nhỏ, nên không được dùng làm giới "
        "hạn cơ cho hệ. Nhà sản xuất ghi độ bền dừng tĩnh (với tải tĩnh) và độ bền dừng động (với tải động)."))
    b.append(p(
        "Biến trở quay cũng có loại không có cữ cơ. Trục của loại “hành trình không giới hạn” này có thể quay "
        "liên tục theo cả hai chiều; tuy vậy hành trình điện luôn nhỏ hơn 360° vì có chỗ gián đoạn hay “vùng "
        "chết” nơi phần tử điện trở bắt đầu và kết thúc (xem Hình 6-1). Có thể đo nhiều vòng bằng biến trở "
        "hành trình không giới hạn kết hợp với một bộ đếm: bộ đếm ghi số vòng nguyên, còn biến trở đo phần góc "
        "lẻ."))

    b.append(h3("Nhiệt độ làm việc", "Operating Temperature"))
    b.append(p(
        "Khi làm việc trong dải nhiệt độ quy định, biến trở giữ được độ tuyến tính điện và độ toàn vẹn cơ tốt. "
        "Tuỳ kết cấu, biến trở có thể làm việc từ −65 °C đến 150 °C. Làm việc ngoài giới hạn quy định có thể "
        "gây hỏng vật liệu, hoặc trực tiếp do nhiệt hoặc do biến dạng lệch trục sinh ra bởi nhiệt."))

    b.append(h3("Rung, xóc và gia tốc", "Vibration, Shock, and Acceleration"))
    b.append(p(
        "Rung, xóc và gia tốc đều là nguồn tiềm tàng gây gián đoạn tiếp xúc giữa chổi quét và phần tử điện trở. "
        "Nói chung, một lần mất tiếp xúc được coi là gián đoạn khi kéo dài từ 0,1 ms trở lên [2]. Các giá trị "
        "ghi trong bảng đặc tính tính bằng đơn vị g và phụ thuộc rất nhiều vào phép thử cụ thể. Một số phép "
        "thử đặc trưng dùng rung hình sin, rung ngẫu nhiên, xóc hình sin, xóc răng cưa hoặc gia tốc để kích "
        "thích biến trở. Nhà sản xuất dùng các giải pháp thiết kế cơ để loại bỏ điểm yếu trong đáp ứng động "
        "của biến trở; một kỹ thuật là dùng nhiều chổi quét có tần số riêng khác nhau để giảm gián đoạn tiếp "
        "xúc do rung."))

    b.append(h3("Tốc độ", "Speed"))
    b.append(p(
        "Vượt quá tốc độ tối đa quy định có thể gây mài mòn sớm hoặc cho giá trị không liên tục do hiệu ứng "
        "chổi quét nảy khỏi mặt điện trở. Theo nguyên tắc chung, trục quay càng chậm thì tuổi thọ (tính theo "
        "tổng số chu trình) càng dài. Giới hạn tốc độ phụ thuộc vật liệu. Với biến trở quay, loại quấn dây có "
        "tốc độ tối đa ưu tiên cỡ 100 vòng/phút, còn loại nhựa dẫn điện cho phép tới 2000 vòng/phút. Biến trở "
        "chuyển động thẳng có vận tốc tối đa ưu tiên tới 10 m/s."))

    b.append(h3("Tuổi thọ", "Life"))
    b.append(p(
        "Dù bị mài mòn cơ liên tục, tuổi thọ dự kiến của biến trở vào cỡ một triệu chu trình khi dùng trong "
        "điều kiện phù hợp. Một biến trở màng tốt có thể đạt hàng trăm triệu chu trình. Trong ba loại quấn dây, "
        "lai và nhựa dẫn điện, bề mặt không phẳng của phần tử quấn dây đương nhiên bị mài mòn nhiều nhất nên "
        "tuổi thọ ngắn nhất. Loại lai khắc phục điều này bằng cách phủ một lớp màng dẫn điện nhẵn lên kết cấu "
        "quấn dây. Biến trở nhựa dẫn điện nói chung có tuổi thọ dài nhất nhờ bề mặt phần tử điện trở nhẵn."))

    b.append(h3("Nhiễm bẩn và niêm phong", "Contamination and Seals"))
    b.append(p(
        "Tạp chất lọt vào biến trở có thể làm tăng mài mòn và tăng ma sát giữa chổi quét với phần tử điện trở. "
        "Hậu quả từ tăng tải cơ cho đến hỏng hẳn (kẹt, mất tiếp xúc). May thay, hầu hết nhà sản xuất đều có "
        "biến trở loại kín cho ứng dụng công nghiệp, nơi bụi bẩn và chất lỏng thường không tránh được. Để hỗ "
        "trợ chọn lựa, bảng đặc tính thường ghi kiểu niêm phong vỏ (cơ cấu và vật liệu) cùng khả năng chịu "
        "dung môi tẩy rửa và các chất lỏng thường gặp."))

    b.append(h3("Lệch trục", "Misalignment"))
    b.append(p(
        "Lệch trục trong biến trở có thể làm mòn sớm mặt ổ trục và tăng tải cơ. Một thiết kế tốt giảm thiểu "
        "lệch trục (xem mục Triển khai bên dưới). Nhà sản xuất nêu một số dung sai căn chỉnh. Với biến trở "
        "chuyển động thẳng, độ lệch trục là mức trục có thể lệch khỏi đường tâm; mức trục có thể xoay quanh "
        "đường tâm được ghi là độ xoay trục. Với biến trở quay, độ rơ dọc trục và độ rơ hướng kính mô tả mức "
        "lệch của trục dưới tải hướng kính. Độ đảo trục chỉ mức lệch tâm của đường kính trục khi trục quay dưới "
        "tải hướng kính."))

    b.append(h3("Phương pháp lắp cơ khí", "Mechanical Mounting Methods"))
    b.append(p(
        "Các chi tiết cơ trên vỏ biến trở quyết định phương pháp lắp. Lựa chọn thay đổi theo nhà sản xuất và "
        "theo kiểu biến trở (quay, thẳng, dây cáp). Có thể có đế riêng, lỗ, tai, mặt bích và giá đỡ — đều bắt "
        "bằng vít máy — cùng các vít ren cấy, bắt bằng đai ốc. Biến trở chuyển động thẳng có loại dẫn động "
        "bằng cần đẩy hoặc con trượt, một số có lò xo hồi vị trong hoặc ngoài. Việc lắp thường dùng kẹp di "
        "động, thường do nhà sản xuất cung cấp. Một số biến trở thẳng khác lắp qua vỏ ren. Với biến trở quay, "
        "hai kiểu lắp phổ biến nhất là lắp ống lót và lắp servo. Xem Hình 6-5."))
    b.append(fig(5, F.fig_6_5()))
    b.append(h3("Lắp ống lót", "Bushing mount"))
    b.append(p(
        "Biến trở có một ống ren đồng tâm với trục, xuyên qua lỗ trên tấm lắp và siết bằng đai ốc cùng vòng "
        "hãm. Một tai hoặc chốt lệch trục giữ cho vỏ không xoay. Lắp kiểu ống lót chỉ cần khoan một lỗ; tuy "
        "vậy, độ tự do xoay hạn chế và độ rơ đáng kể trước khi siết làm việc căn chỉnh chính xác trở nên khó "
        "khăn."))
    b.append(h3("Lắp servo", "Servo mount"))
    b.append(p(
        "Biến trở có một vành định vị đồng tâm với trục, được gia công chính xác, ăn khớp vào lỗ doa chính xác "
        "trên tấm lắp. Mặt bích được giữ bằng các kẹp servo bố trí đối xứng, tháo nhanh, hiện có của Timber-Top "
        "Inc. [9] và của các nguồn trong Bảng 6.4. (Những kẹp này còn gọi là kẹp lắp synchro và kẹp lắp động "
        "cơ bước, vì synchro và động cơ bước cũng có kiểu lắp servo.) Lắp servo chính xác và dễ chỉnh, nhưng "
        "phải chịu chi phí gia công chính xác."))

    b.append(h2("Kỹ thuật đo", "Measurement Techniques"))
    b.append(p(
        "Để đo dịch chuyển, biến trở phải được gắn vào các chi tiết và cơ cấu cơ khí. Thông thường vỏ biến trở "
        "lắp lên một khung cố định, còn trục nối với phần tử chuyển động. Chuyển động vào (tức chuyển động cần "
        "đo) có thể nối trực tiếp hoặc gián tiếp với trục biến trở. Nối trực tiếp tuy đơn giản nhưng có những "
        "hạn chế nhất định:"))
    b.append(ul([
        "Chuyển động vào ánh xạ 1:1 thành chuyển động trục.",
        "Chuyển động vào không được vượt quá giới hạn hành trình cơ của biến trở.",
        "Đo góc cần biến trở quay; đo vị trí cần biến trở chuyển động thẳng.",
        "Biến trở phải lắp gần nguồn chuyển động.",
        "Chuyển động vào phải gần như thẳng hàng hoặc đồng tâm hoàn hảo với trục biến trở.",
    ]))
    b.append(p(
        "Hình 6-6 trình bày các cách khắc phục những hạn chế đó. Cơ cấu có lợi về lực sẽ đổi tỉ lệ chuyển động "
        "và điều chỉnh giới hạn hành trình. Cơ cấu đổi giữa chuyển động thẳng và chuyển động quay cho phép bất "
        "kỳ loại biến trở nào đo bất kỳ loại chuyển động nào. Cơ cấu truyền động đưa biến trở ra xa chuyển "
        "động cần đo. Cơ cấu đàn hồi bù lệch trục. Phần lớn các cơ cấu mô tả dưới đây có thể thực hiện bằng "
        "linh kiện của các nguồn trong Bảng 6.4."))
    b.append(fig(6, F.fig_6_6()))
    b.append(p(
        "<b>Bánh răng</b> đổi tỉ lệ ánh xạ giữa chuyển động vào và chuyển động trục biến trở theo tỉ số truyền, "
        "đồng thời dịch trục quay sang mặt phẳng song song hoặc vuông góc tuỳ loại bánh răng (trụ hay côn). "
        "Bánh răng gây ra độ rơ (<i>backlash</i>). <b>Con lăn ma sát</b> là biến thể của bánh răng, không bị "
        "rơ nhưng dễ trượt; tỉ số đường kính con lăn quyết định tỉ lệ ánh xạ."))
    b.append(p(
        "<b>Thanh răng – bánh răng</b> đổi giữa chuyển động thẳng và chuyển động quay. Tỉ lệ do bước thẳng của "
        "thanh răng (khoảng cách răng – răng) so với số răng của bánh răng quyết định. Độ rơ là không tránh "
        "khỏi."))
    b.append(p(
        "<b>Vít me</b> đổi chuyển động quay thành chuyển động thẳng theo nguyên lý trục vít. Một số loại ma sát "
        "thấp (như vít bi) còn đổi được ngược lại, từ thẳng sang quay. Dù theo chiều nào, tỉ lệ do bước vít — "
        "quãng đường đai ốc đi được trong một vòng — quyết định. Vít me cũng bị ảnh hưởng của độ rơ."))
    b.append(p(
        "<b>Tang quấn cáp</b> đổi giữa chuyển động thẳng và quay theo chu vi tang, vì một vòng quay đường kính "
        "D quấn hoặc nhả một đoạn cáp dài πD. Có thể cần một lực ngoài (do lò xo hoặc quả nặng) để duy trì sức "
        "căng cáp."))
    b.append(p(
        "<b>Puly</b> có thể dẫn cáp của biến trở dây cáp qua một đường phức tạp tới nguồn chuyển động. Ánh xạ "
        "là 1:1 trừ khi cách đi dây tạo ra lợi về lực. <b>Puly và đai</b> truyền chuyển động quay với tỉ lệ theo "
        "đường kính tương đối của hai puly; đai đổi giữa chuyển động thẳng và quay (Hình 6-6a). Khoảng trống "
        "giữa hai puly là chỗ đi dây thuận tiện cho các linh kiện khác. Đĩa xích và xích có đặc tính tương tự. "
        "Có sẵn các bộ puly – đai phối hợp làm việc với độ trượt, độ rơ và độ giãn không đáng kể."))
    b.append(p(
        "<b>Cam</b> ánh xạ chuyển động quay thành chuyển động thẳng theo hàm đã “lập trình” vào biên dạng cam; "
        "xem [10]. <b>Cơ cấu thanh truyền</b> có thể được thiết kế để đổi, đổi tỉ lệ và truyền chuyển động; "
        "việc thiết kế và phân tích có thể khá phức tạp và đặc tính ánh xạ thường rất phi tuyến; xem [11]."))
    b.append(p(
        "<b>Trục mềm</b> truyền chuyển động quay giữa hai trục không song song với ánh xạ 1:1, nhưng chịu xoắn "
        "dồn và trễ nếu chuyển động đảo chiều. <b>Ống dẫn cáp</b> (như cáp phanh xe đạp hay cáp Bowden) có thể "
        "dẫn cáp theo đường bất kỳ để nối biến trở với nguồn chuyển động ở xa. Ống phải không nén được và cố "
        "định hai đầu; ánh xạ là 1:1 với một ít độ rơ cơ học, và bôi trơn giúp giảm ma sát."))
    b.append(p(
        "Đặc tính ánh xạ của cơ cấu ảnh hưởng đến độ phân giải và độ chính xác của phép đo. Hãy xét một động "
        "cơ bước quay vít me để dịch đai ốc. Một biến trở chuyển động thẳng có thể đo trực tiếp vị trí đai ốc "
        "với độ phân giải nào đó. Hoặc một biến trở quay nối với vít me có thể đo vị trí với độ phân giải cao "
        "hơn, nếu cơ cấu ánh xạ cùng một quãng đi của đai ốc thành quãng đi của chổi quét lớn hơn nhiều. Cân "
        "nhắc giữa mức tăng độ phân giải và độ không đảm bảo do độ rơ sẽ quyết định cách nào chính xác hơn."))

    b.append(h2("Triển khai", "Implementation"))
    b.append(p(
        "Tích hợp biến trở vào hệ đo đòi hỏi phải xét nhiều vấn đề thiết kế: ảnh hưởng của các đặc tính vật lý "
        "của biến trở, các nguồn sai số, giới hạn không gian và cách đi dây. Phải xét kiểu trục và ổ trục, và "
        "bảo vệ chúng khỏi tải quá mức. Một thiết kế tốt sẽ:"))
    b.append(ul([
        "Cho phép giá lắp biến trở bù được lệch trục nhỏ.",
        "Bảo vệ trục khỏi tải dọc trục, tải ngang và tải uốn (không dùng biến trở làm ổ trục).",
        "Bố trí cữ giới hạn cứng trong dải hành trình của biến trở (không dùng cữ của biến trở).",
        "Bảo vệ biến trở khỏi chất nhiễm bẩn.",
        "Giảm căng cho các mối đấu điện của biến trở.",
    ]))
    b.append(p("Một cách xử lý đầy đủ các vấn đề thiết kế chính xác có trong [12]."))

    b.append(h3("Nối trục biến trở", "Coupling to the Pot"))
    b.append(p(
        "Triển khai thành công còn cần những kỹ thuật thực tế để gắn cơ khí. Đầu kẹp cáp của biến trở dây cáp "
        "thường được bắt vào chi tiết khác bằng vít. Với các loại biến trở khác, kỹ thuật nối một phần do tính "
        "chất của trục quyết định. Trục quay có nhiều kiểu đầu: trơn, một mặt phẳng, hai mặt phẳng, có rãnh, "
        "hoặc khía nhám. Trục chuyển động thẳng thường tận cùng bằng ren, nhưng cũng có loại đầu con lăn (để "
        "bám theo bề mặt) hoặc đầu ổ cầu (để bù lệch trục). Với sự cẩn thận, có thể cắt, khoan, giũa, ren hoá "
        "trục."))
    b.append(p(
        "Trong một ứng dụng đo điển hình, trục biến trở nối với một chi tiết cơ (bánh răng, puly) hoặc với một "
        "trục khác cùng hay khác đường kính. Mối nối tốt cho liên kết dương với trục mà không gây ứng suất cho "
        "cơ cấu của biến trở. Để đạt được điều đó với biến trở quay và thẳng, cần cân bằng giữa căn chỉnh cẩn "
        "thận và khớp nối đàn hồi. Với biến trở dây cáp, việc căn chỉnh không quá khắt khe. Các cách nối hữu "
        "ích gồm:"))
    b.append(p(
        "<b>Khớp nối đàn hồi.</b> Nói chung nên đặt một khớp đàn hồi giữa trục biến trở và mọi trục khác. Khớp "
        "đàn hồi nối hai trục lệch nhau cùng hay khác đường kính. Các hãng trong Bảng 6.4 có khớp kiểu xếp "
        "gấp (bellows), khớp mềm, khớp lò xo, khớp chữ thập cao su, khớp Oldham, khớp lò xo lá, trục mềm và "
        "khớp vạn năng. Mỗi loại có đặc thù riêng ảnh hưởng đến sai số đo; catalogue của hãng cho biết chi tiết."))
    b.append(p(
        "<b>Khớp nối ống.</b> Rẻ hơn khớp đàn hồi, khớp ống cứng nối hai trục cùng hay khác đường kính với yêu "
        "cầu hai trục phải thẳng hàng hoàn hảo. Căn chỉnh hoàn hảo khó đạt ngay từ đầu và không thể duy trì khi "
        "hệ già đi. Căn chỉnh không hoàn hảo làm tăng mài mòn và có nguy cơ hỏng biến trở. Khớp ống có sẵn từ "
        "các hãng trong Bảng 6.4."))
    b.append(p(
        "<b>Lắp ép.</b> Lắp ép đặc biệt tiện khi lỗ của một chi tiết nhựa nhỏ danh nghĩa bằng đường kính trục. "
        "Ép cẩn thận chi tiết lên trục; ma sát giữ chi tiết tại chỗ, nhưng tháo lắp nhiều lần sẽ làm hỏng mối "
        "lắp."))
    b.append(p(
        "<b>Lắp co giãn nhiệt.</b> Chi tiết có lỗ nhỏ hơn đường kính trục một chút có thể được nung để nở ra "
        "vừa lọt qua trục; khi nguội và lỗ co lại sẽ có mối bám chắc."))
    b.append(p(
        "<b>Chốt.</b> Chi tiết nhỏ có may ơ có thể được chốt vào trục. Chốt nên xuyên qua may ơ và ăn một phần "
        "vào trục, và chi tiết phải lắp vừa khít không rơ. Dùng chốt đàn hồi hoặc chốt xoắn kết hợp keo hãm ren "
        "(như Loctite 242)."))
    b.append(p(
        "<b>Vít hãm.</b> Chi tiết nhỏ có may ơ giữ bằng vít hãm. Chi tiết phải lắp vừa khít không rơ. Để tốt "
        "nhất, dùng hai vít hãm trên một trục có các mặt phẳng vuông góc; tạo vết lõm trên trục trơn bằng cách "
        "dùng chính lỗ vít của chi tiết làm mũi khoan dẫn hướng. Bôi keo hãm ren để vít không lỏng ra."))
    b.append(p(
        "<b>Kẹp.</b> Chi tiết nhỏ cũng có loại may ơ chẻ, siết chặt vào trục khi bị kẹp bằng một vòng kẹp "
        "tương ứng. Kẹp cho mối lắp chắc chắn mà không làm xước trục."))
    b.append(p(
        "<b>Keo dán.</b> Keo giữ (như Loctite 609) có thể giữ chi tiết nhỏ trên trục. Làm theo hướng dẫn của "
        "nhà sản xuất để có kết quả tốt nhất."))
    b.append(p(
        "<b>Tiếp xúc bằng lò xo.</b> Một trục có lò xo sẽ duy trì tiếp xúc dương với bề mặt chuyển động ở tốc "
        "độ hợp lý và không có gia tốc đột ngột."))

    b.append(h2("Chi phí và nguồn cung cấp", "Costs and Sources"))
    b.append(p(
        "Biến trở chính xác rẻ so với các công nghệ đo dịch chuyển khác. Bảng 6.5 nêu giá gần đúng của các sản "
        "phẩm có sẵn, mua lẻ một chiếc. Chất lượng cao hơn thường có giá cao hơn; tuy vậy, những biến trở rất "
        "tốt đôi khi được bán với giá hời nhờ sản xuất hàng loạt hoặc do hàng tồn. Các cửa hàng linh kiện điện "
        "tử có biến trở giá rẻ (dưới 20 USD) đủ dùng cho dự án ngắn hạn. Dù giá thế nào, luôn kiểm tra bảng đặc "
        "tính của nhà sản xuất để xác nhận biến trở phù hợp với ứng dụng."))
    b.append(table(
        ["Loại biến trở", "Khoảng giá (USD)"],
        [["Loại quay", "10 – 350"],
         ["Chuyển động thẳng", "20 – 2.000"],
         ["Dây cáp", "250 – 1.000"]],
        "Bảng 6-5 · Giá điển hình khi mua lẻ một chiếc (USD) của biến trở bán sẵn trên thị trường."))
    b.append(p(
        "Bảng 6.6 liệt kê một số nguồn cung cấp biến trở chính xác. Hầu hết nhà sản xuất đều phát hành catalogue "
        "và nhiều hãng có trang web. Ngoài dòng sản phẩm tiêu chuẩn, phần lớn nhà sản xuất nhận chế tạo biến "
        "trở theo yêu cầu cho các ứng dụng khối lượng lớn."))
    b.append(table(
        ["Hãng", "Loại biến trở"],
        [["Betatronix, Inc. · Hauppauge, NY", "Chuyển động thẳng đặc biệt, loại quay"],
         ["BI Technologies Corp. · Fullerton, CA", "Loại quay"],
         ["Bourns, Inc. · Ogden, UT", "Chủ yếu loại quay, một số loại thẳng"],
         ["Celesco Transducer Products, Inc. · Canoga Park, CA", "Dây cáp"],
         ["Data Instruments · Acton, MA", "Chuyển động thẳng, loại quay"],
         ["Duncan Electronics Division (BEI) · Tustin, CA", "Chuyển động thẳng, loại quay"],
         ["Dynamation Transducers Corp. · Holliston, MA", "Chuyển động thẳng, loại quay"],
         ["JDK Controls, Inc. · Grass Valley, CA", "Loại quay, bộ rôto/chổi quét tự lắp"],
         ["Midori America Corp. · Fullerton, CA", "Thẳng, quay, dây cáp; cả từ điện trở"],
         ["New England Instrument · Woonsocket, RI", "Thẳng, quay, phần tử điện trở"],
         ["Novotechnik U.S., Inc. · Marlborough, MA", "Chuyển động thẳng, loại quay"],
         ["Servo Systems Co. · Montville, NJ", "Chuyển động thẳng, loại quay (hàng tồn)"],
         ["SpaceAge Control, Inc. · Palmdale, CA", "Dây cáp"],
         ["Spectrol Electronics Corp. · Ontario, CA", "Loại quay"],
         ["UniMeasure, Inc. · Corvallis, OR", "Dây cáp"],
         ["Axsys Technologies (Vernitron) · St. Petersburg, FL", "Chuyển động thẳng, loại quay"]],
        "Bảng 6-6 · Các nguồn cung cấp biến trở chính xác. Địa chỉ đầy đủ và số điện thoại có trong bản in; "
        "ở đây chỉ giữ tên hãng và nơi đặt trụ sở để tra cứu."))

    b.append(h2("Đánh giá", "Evaluation"))
    b.append(p(
        "Biến trở chính xác là một công nghệ đã chín, thực tế đứng yên trừ những phát triển lẻ tẻ về vật liệu, "
        "vỏ và chế tạo. Những cải tiến gần đây của biến trở — gồm biến trở màng tiếp xúc tạm thời [13] và biến "
        "trở số bán dẫn [14] — không giúp gì cho đo lường chính xác."))
    b.append(p(
        "Cầu phân áp biến thiên là cấu hình truyền thống cho đo lường chính xác. Đầu ra của mạch là một điện "
        "áp một chiều biên độ lớn, không phụ thuộc thay đổi tổng trở của biến trở và rất tương thích với các "
        "mạch và hệ khác. Cũng có thể có các dạng đầu ra khác nếu mắc biến trở thành điện trở biến thiên. Ví "
        "dụ, ghép với một tụ điện, biến trở có thể tạo hằng số thời gian RC phụ thuộc vị trí để điều biến tần "
        "số hay hệ số đầy của một bộ dao động; khi đó độ ổn định và đặc tính xoay chiều của biến trở trở nên "
        "quan trọng."))
    b.append(p(
        "Một công nghệ đo dịch chuyển điện trở thay thế là biến trở từ điện trở, có cả dạng quay và dạng thẳng. "
        "Biến trở từ điện trở dùng một “chổi quét” nam châm vĩnh cửu không tiếp xúc, chạy phía trên một cặp "
        "phần tử từ điện trở. Hai phần tử này, mắc thành cầu phân áp, thay đổi điện trở theo cường độ từ trường "
        "áp vào, và do đó chia áp theo vị trí của nam châm. Đầu ra gần tuyến tính trong một dải chuyển động hạn "
        "chế (ví dụ 90° với loại quay). Biến trở từ điện trở cho độ phân giải không giới hạn và tuổi thọ đặc "
        "biệt dài, nhưng có thể cần mạch bù nhiệt. Xem [15]."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "Bourns, Inc., <i>Electronic Components RC4 Solutions Guide</i>, 1995, 304.",
        "Vernitron Motion Control Group (New York, NY), <i>Precision Potentiometers</i>, Catalog #752, 1993.",
        "UniMeasure, Inc., <i>Position &amp; Velocity Transducers</i>, UniMeasure document No. 400113-27A, "
        "Corvallis, OR.",
        "Instrument Society of America (Research Triangle Park, NC), ISA-S37.12-1977 (R1982) <i>Specifications "
        "and Tests for Potentiometric Displacement Transducers</i>, 1982.",
        "E. C. Jordan (Ed.), <i>Reference Data for Engineers: Radio, Electronics, Computer, and "
        "Communications</i>, 7th ed., Indianapolis: H.W. Sams, 1985, 5–16.",
        "D. C. Greenwood, <i>Manual of Electromechanical Devices</i>, New York: McGraw-Hill, 1965, 297–299.",
        "E. S. Charkey, <i>Electromechanical System Components</i>, New York: Wiley-Interscience, 1972, "
        "302–303.",
        "Variable Resistive Components Institute (Vista, CA), <i>VRCI-P-100A Standard for Wirewound and "
        "Nonwirewound Precision Potentiometers</i>, 1988.",
        "Timber-Top, Inc., P.O. Box 517, Watertown, CT 06795.",
        "J. Angeles and C. S. López-Cajún, <i>Optimization of Cam Mechanisms</i>, Dordrecht: Kluwer Academic, "
        "1991.",
        "P. W. Jensen, <i>Classical and Modern Mechanisms for Engineers and Inventors</i>, New York: Marcel "
        "Dekker, 1991.",
        "A. H. Slocum, <i>Precision Machine Design</i>, Englewood Cliffs, NJ: Prentice Hall, 1992.",
        "Spectra Symbol Inc., data sheet: <i>SoftPot® (Membrane Potentiometer)</i>, Salt Lake City, UT, 1996.",
        "Dallas Semiconductor Corp., <i>Digital Potentiometer Overview</i>, 1997.",
        "Midori America Corp. (Fullerton, CA), <i>Midori Position Sensors 1995 Catalog</i>.",
    ]))
    b.append(nav(1, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "A potentiometer is the cheapest displacement sensor there is, and the one most often misapplied. This "
        "companion page carries the six redrawn figures, the six tables, and the engineering argument behind "
        "them; the full text is in the Vietnamese edition."))
    b.append(h2("What the pot actually is"))
    b.append(p(
        "A resistive element, a wiper that slides on it, and a voltage divider. That is the whole device. Its "
        "virtues are real — no electronics at the sensor, a large output signal, a proven construction — and so "
        "are its costs: friction, inertia, wear, and a bandwidth limited by the mechanics."))
    b.append(fig(1, F.fig_6_1(), "en"))
    b.append(fig(2, F.fig_6_2(), "en"))
    b.append(h2("The one equation that matters"))
    b.append(p(
        "Everything about loading follows from Equation 6.1: the output is not x/xP but x/xP divided by "
        "1 + (x/xP)(1 − x/xP)(RP/RL). The error term vanishes at both ends of travel and peaks at mid-scale, "
        "which is why a pot that reads correctly at 0 % and 100 % can still be 2 % out in the middle. The rule "
        "of thumb — keep RL/RP at 10 or more — holds the peak error to roughly 1 % of full scale."))
    b.append(eq("v<sub>o</sub>/v<sub>r</sub> = (x/x<sub>P</sub>) / "
                "[1 + (x/x<sub>P</sub>)(1 − x/x<sub>P</sub>)(R<sub>P</sub>/R<sub>L</sub>)]", "6.1"))
    b.append(fig(4, F.fig_6_4(), "en"))
    b.append(p(
        "Figure 6.3 shows the other half of the accuracy story: linearity is quoted against a best-fit line, "
        "not against the end points, so a pot with 0.1 % independent linearity can still be several tenths of "
        "a percent away from the terminal-based line a naive calibration would draw."))
    b.append(fig(3, F.fig_6_3(), "en"))
    b.append(h2("Choosing the element"))
    b.append(table(
        ["", "Conductive plastic", "Wirewound", "Hybrid"],
        [["Resolution", "Infinitesimal", "Quantised by the coil", "Infinitesimal"],
         ["Power rating", "Low", "High", "Low"],
         ["Temperature stability", "Poor", "Excellent", "Very good"],
         ["Noise", "Very low", "Low, degrades with time", "Low"],
         ["Life", "10<sup>6</sup>–10<sup>8</sup> cycles", "10<sup>5</sup>–10<sup>6</sup> cycles",
          "10<sup>6</sup>–10<sup>7</sup> cycles"]],
        "Table 6.2 · The three resistive elements worth considering for precision work."))
    b.append(p(
        "The decision rule is short: conductive plastic unless you need to dissipate power or survive heat, "
        "wirewound when you do, hybrid when you want both and can pay for it. Cermet and carbon composition "
        "appear in the chapter only to be ruled out."))
    b.append(h2("Mounting and coupling"))
    b.append(fig(5, F.fig_6_5(), "en"))
    b.append(p(
        "The bushing mount needs a drilled hole and tolerates a sloppy one; the servo mount needs a bored hole "
        "and rewards it with repeatability. Either way the pot must not be used as a bearing — the shaft takes "
        "no thrust, side or bending load, the hard stops live outside the pot, and a compliant coupling absorbs "
        "whatever misalignment the bracket cannot."))
    b.append(fig(6, F.fig_6_6(), "en"))
    b.append(h2("When a mechanism earns its place"))
    b.append(p(
        "Section 6.1 ends with seven mechanisms — gears, rack and pinion, lead screws, drums, cams, belts, "
        "linkages — and the reason to use one is always the same: to trade travel for resolution. A rotary pot "
        "geared to a lead screw sees many turns of wiper travel for one turn of the screw, so its quantisation "
        "is divided by the ratio. Whether that helps depends on whether the backlash you add is smaller than "
        "the resolution you gain. The chapter's own worked comparison makes the point: resolution is not "
        "accuracy, and a mechanism can buy one while selling the other."))
    b.append(nav(1, "en"))
    return "".join(b)
