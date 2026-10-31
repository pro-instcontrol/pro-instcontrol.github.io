# -*- coding: utf-8 -*-
"""Handbook 6.8 — Optical Encoder Displacement Sensors (J. R. René Mayer)."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Việc phát hiện chuyển động góc và chuyển động thẳng là một chức năng then chốt trong vô số hệ thống như "
        "máy công cụ, robot công nghiệp, nhiều loại thiết bị đo, chuột máy tính, v.v. Tuy chỉ là một trong nhiều kỹ "
        "thuật có thể làm được phép đo ấy, nhưng chính sự dễ dàng ghép nối với các hệ thống số đã khiến chúng trở "
        "nên rất phổ biến."))
    b.append(p(
        "Bộ mã hoá quang dùng để đo vị trí góc hoặc vị trí thẳng. Loại dùng cho phát hiện góc thường được gọi là bộ "
        "mã hoá quay hay bộ mã hoá trục, vì chúng thường phát hiện chuyển động quay của một trục. Bộ mã hoá quang "
        "bao gồm nhiều loại thiết bị, tất cả đều dùng ánh sáng làm phương tiện biến chuyển động thành tín hiệu "
        "điện. Mọi thiết bị đều có hai khối cấu trúc cơ bản: một cách tử chính và một hệ phát hiện. Chính vị trí "
        "tương đối giữa hai khối ấy là đại lượng được phát hiện. Cách tử chính là chuẩn đo. Với phép đo thẳng, cách "
        "tử chính — thường gọi là thang đo — là một hay nhiều tập đường song song có bước không đổi hoặc được mã hoá "
        "đặc biệt, đặt trên một đế. Tương tự, bộ mã hoá quay có một cách tử gồm các đường hướng tâm trên một đĩa."))
    b.append(p(
        "Về nguyên tắc, cả bộ mã hoá thẳng lẫn bộ mã hoá quay đều có thể là loại tuyệt đối hoặc loại gia số, tuy "
        "rằng trên thực tế bộ mã hoá thẳng tuyệt đối dùng nguyên lý quang học khá hiếm và có đặc tính làm việc bị "
        "hạn chế nghiêm trọng (độ chính xác, độ phân giải và/hoặc tốc độ làm việc cực đại). Hình 6-66 trình bày "
        "một cách phân loại đơn giản các bộ mã hoá quang. Cách phân loại này dựa trên bản chất của thông tin được "
        "tạo ra."))
    b.append(fig(66, F.fig_6_66()))
    b.append(p(
        "Bộ mã hoá gia số phát hiện chuyển động so với một điểm chuẩn. Do đó, ở một vị trí xác định, bộ mã hoá "
        "thường cung cấp một dạng tín hiệu chuẩn nào đó để xác lập vị trí quy chiếu. Vị trí hiện thời sau đó được "
        "tăng (hoặc giảm) cho phù hợp. Cũng có thể dùng nhiều dấu chuẩn, trong đó khoảng cách giữa các dấu liên "
        "tiếp là duy nhất, nhờ vậy ngay khi phát hiện được hai dấu liên tiếp là có thể xác lập vị trí tuyệt đối "
        "kể từ đó trở đi. Điểm chuẩn cũng có thể là cơ khí. Nếu mất nguồn hoặc xảy ra lỗi truyền tín hiệu thì vị "
        "trí tuyệt đối bị mất và bộ mã hoá phải quay về một hay nhiều điểm chuẩn để đặt lại bộ đếm. Đáng tiếc là "
        "việc mất xung có thể không được phát hiện cho tới khi quay lại được một điểm chuẩn. Hơn nữa, các sai số "
        "đọc có thể tích luỹ."))
    b.append(p(
        "Ngược lại, bộ mã hoá tuyệt đối tạo ra một tập tín hiệu nhị phân mà từ đó có thể suy ra vị trí tuyệt đối "
        "mà không cần biết lịch sử chuyển động trước đó. Vị trí hiện thời được biết ngay từ lúc bật nguồn. Với bộ "
        "mã hoá quay tuyệt đối, có cả loại một vòng và loại nhiều vòng. Loại nhiều vòng dùng một hệ truyền động cơ "
        "khí bên trong để dẫn động một cách tử thứ hai làm chức năng đếm số vòng."))
    b.append(p(
        "Phần lớn bộ mã hoá gia số dùng tín hiệu vuông pha ở đầu ra để mang thông tin chuyển động. Một số bộ mã "
        "hoá chỉ dùng một tín hiệu xung vuông, phục vụ vị trí theo một chiều. Xung vuông đơn ấy cũng có thể đưa "
        "vào PLC (bộ điều khiển logic khả trình) hoặc một giao diện điện tử khác để biến thành tốc độ hay vòng/phút "
        "nhằm hiển thị tốc độ. Tuy nhiên, hễ cần làm việc hai chiều thì tín hiệu vuông pha là bắt buộc. Tín hiệu "
        "vuông pha có dạng tương tự hoặc dạng số. Dạng tương tự chỉ đơn giản là một tín hiệu sin và một tín hiệu "
        "cosin. Số chu kỳ sin trên một đơn vị thay đổi của đại lượng đo (một vòng hay 360° với bộ mã hoá quay) "
        "quyết định độ phân giải cơ bản của bộ mã hoá trước khi nội suy. Dạng số gồm hai chuỗi xung vuông lệch pha "
        "nhau 90° (thường gọi là độ điện). Độ lệch pha 90° là không thể thiếu để phát hiện chiều chuyển động, nhờ "
        "đó tăng hoặc giảm bộ đếm vị trí cho phù hợp. Ba kỹ thuật quang chính để tạo tín hiệu vuông pha là che hình "
        "học, vân Moiré và nhiễu xạ. Với bộ mã hoá thẳng, độ phân giải cơ bản gắn với quãng đường cách tử phải đi "
        "để bộ mã hoá tạo ra một chu kỳ vuông pha trọn vẹn. Với bộ mã hoá quay, độ phân giải cơ bản thường được mô "
        "tả bằng số chu kỳ vuông pha trên một vòng."))
    b.append(p(
        "Độ phân giải của một hệ bộ mã hoá có thể tăng bằng phương tiện điện tử. Với tín hiệu vuông pha tương tự, "
        "có thể nội suy bên trong mỗi chu kỳ vuông pha. Giới hạn của hệ số nội suy phụ thuộc chất lượng của các tín "
        "hiệu cơ bản (tỉ lệ vạch–khoảng, độ tách pha vuông góc và độ rung pha). Với tín hiệu xung vuông, việc nhân "
        "hai hoặc nhân bốn rất dễ thực hiện. Tuy nhiên, tăng độ phân giải theo cách này không cải thiện độ đúng — "
        "thường được gọi là độ chính xác hay độ tuyến tính — của phép đo."))

    # ------------------------------------------------------------ absolute
    b.append(h2("Bộ mã hoá tuyệt đối", "Absolute encoders"))
    b.append(p(
        "Bộ mã hoá tuyệt đối được phân loại theo kiểu mã dùng. Bốn loại mã chính là Gray, nhị phân (thường đọc "
        "bằng phương pháp quét chữ V), giải mã quang và giả ngẫu nhiên. Mọi bộ mã hoá tuyệt đối đều dùng che hình "
        "học để tạo mã."))

    b.append(h3("Mã nhị phân trực tiếp", "Direct binary"))
    b.append(p(
        "Hình 6-67(a) minh hoạ khái niệm bộ mã hoá quang thẳng tuyệt đối dùng thang đo mã nhị phân trực tiếp. Thang "
        "cố định có n rãnh (ở đây n = 4), mỗi rãnh cho một bit của một số nhị phân trực tiếp. Rãnh thấp nhất (rãnh "
        "thứ nhất tính từ tâm đĩa với bộ mã hoá quay) là chữ số có nghĩa nhất và có trọng số 2<sup>n–1</sup> (ở đây "
        "là 2³), còn rãnh trên cùng là chữ số có nghĩa nhỏ nhất với trọng số 2⁰. Rãnh mang chữ số có nghĩa nhỏ "
        "nhất có 2<sup>n–1</sup> chu kỳ vạch sáng tối, còn rãnh có nghĩa nhất chỉ có 2⁰ hay 1 chu kỳ như vậy. Với "
        "mỗi rãnh, đầu đọc động có một bộ đọc gồm nguồn sáng, mặt nạ và bộ tách sóng quang."))
    b.append(fig(67, F.fig_6_67()))
    b.append(p(
        "Hình 6-67(b) cho thấy đầu ra của bộ tách sóng quang, tức tổng cường độ ánh sáng tới bề mặt nó. Khi mặt "
        "nạ băng qua một vùng trong suốt của cách tử thì đầu ra tăng, rồi lại giảm. Về lý thuyết ta thu được một "
        "sóng tam giác bị cắt đỉnh, và sóng ấy có thể biến đổi dễ dàng thành xung vuông (Hình 6-67(c)) bằng cách "
        "chọn mức ngưỡng thích hợp. Kết quả là mức cao hay 1 ứng với vạch sáng và mức thấp hay 0 ứng với vạch tối. "
        "Vị trí, tính trong hệ thập phân, tương ứng với vị trí đầu đọc trên Hình 6-67 là"))
    b.append(eq("0 × 2³ + 1 × 2² + 1 × 2¹ + 1 × 2⁰ = 7", "6.93"))
    b.append(p(
        "Cấu hình mã vừa mô tả không thích hợp cho sử dụng thực tế, vì có những chuyển tiếp đòi hỏi hai bit trở "
        "lên phải đổi giá trị đồng thời. Chẳng hạn, từ vị trí 7 sang vị trí 8, mọi bit đều đổi giá trị. Trừ khi "
        "việc đổi xảy ra đồng thời, tại một vị trí nào đó sẽ có kết quả đọc sai. Điều đó đòi hỏi thang đo phải "
        "hoàn hảo về hình học, đầu đọc phải căn chỉnh hoàn hảo với thang đo, và mạch điện tử phải được chỉnh hoàn "
        "hảo và ổn định theo thời gian. Người ta giải quyết vấn đề này hoặc bằng phương pháp quét chữ V, hoặc bằng "
        "một loại mã đơn vị khoảng cách như mã Gray."))

    b.append(h3("Quét chữ V", "Vee-scan"))
    b.append(p(
        "Phương pháp quét chữ V dùng một dãy bộ đọc xếp theo hình chữ V để loại bỏ khả năng đọc nhoè của thang nhị "
        "phân trực tiếp. Stephens và cộng sự [1] chỉ ra các điểm đọc mà tại đó phát hiện chuyển tiếp trên Hình "
        "6-68(a). Họ cũng mô tả việc biến đổi các tín hiệu đã qua ngưỡng thành mã nhị phân bằng logic tổ hợp. Ưu "
        "điểm chính là dung sai vị trí của điểm chuyển tiếp ở mỗi bộ đọc chỉ cần bằng ±1/8 chiều dài chu kỳ của "
        "rãnh tương ứng — chẳng hạn ±45° với rãnh có nghĩa nhất của một đĩa mã hoá quay. Hình 6-68(b) cho thấy một "
        "từ nhị phân trực tiếp thu được nhờ tổ hợp logic các kết quả đọc kiểu quét chữ V."))
    b.append(fig(68, F.fig_6_68()))

    b.append(h3("Mã Gray", "Gray code"))
    b.append(p(
        "Dùng quét chữ V đòi hỏi thêm đầu đọc cũng như thêm mạch xử lý. Mã Gray là mã đơn vị khoảng cách, nên chỉ "
        "một bit dữ liệu đổi giữa hai số liên tiếp hay hai vị trí kế nhau. Nhờ vậy khả năng đọc nhoè bị loại bỏ. Mã "
        "Gray có các ưu điểm sau: (1) dễ biến đổi sang mã nhị phân trực tiếp, và (2) các rãnh mịn nhất rộng gấp "
        "đôi rãnh tương ứng của mã nhị phân trực tiếp. Hình 6-69(a) trình bày một thang đo thẳng dùng mã Gray."))
    b.append(fig(69, F.fig_6_69()))
    b.append(p(
        "Hình 6-69(b) trình bày một sơ đồ biến đổi mã Gray sang mã nhị phân, tiến hành như sau: (1) bit có nghĩa "
        "nhất của mã nhị phân bằng bit có nghĩa nhất của số mã Gray; (2) cộng (modul-2) bit có nghĩa nhất của số "
        "nhị phân với bit có nghĩa kế tiếp của số mã Gray để được bit nhị phân kế tiếp; và (3) lặp lại bước (2) "
        "cho tới khi mọi bit của số mã Gray đã được cộng modul-2. Số thu được là số nhị phân tương đương với số mã "
        "Gray. Phép cộng modul-2 tương đương với tác dụng của một cổng XOR. Hình 6-69(c) trình bày một mạch đơn "
        "giản dùng logic tổ hợp để thực hiện biến đổi Gray sang nhị phân. Sente và cộng sự [2] đề nghị dùng một "
        "ROM ngoài để biến đổi mã, trong đó từ mã đầu vào là địa chỉ còn dữ liệu là từ mã đầu ra. Với một ROM 16 "
        "bit dùng cho mã 12 bit, Sente và cộng sự [2] đề nghị dùng 4 bit còn lại để thực hiện tín hiệu chiều. "
        "Stephens và cộng sự [1] mô tả việc dùng quét chữ V với thang mã Gray để có độ bền vững còn tốt hơn."))

    b.append(h3("Mã giả ngẫu nhiên", "Pseudorandom code"))
    b.append(p(
        "Mã hoá giả ngẫu nhiên cho phép chỉ dùng hai rãnh để tạo ra một bộ mã hoá tuyệt đối. Một rãnh chứa mẫu "
        "dùng để nhận diện vị trí hiện thời, rãnh kia dùng để đồng bộ việc đọc rãnh mã hoá và loại bỏ các vấn đề "
        "nhoè. Chuỗi nhị phân giả ngẫu nhiên (PRBS) là một dãy vạch hoặc số nhị phân được tạo ra sao cho mọi dãy n "
        "chữ số liên tiếp đều là duy nhất. Loại mã ấy gọi là mã chuỗi, và nó có tính chất: n – 1 chữ số đầu của "
        "một từ n bit trùng với n – 1 chữ số cuối của từ mã trước đó. Nhờ vậy chúng có thể chồng lấn một phần trên "
        "một rãnh duy nhất. Một PRBS có độ dài 2<sup>n</sup> – 1 được định nghĩa bởi"))
    b.append(eq("X(j),   j = 0, 1, 2, …, 2<sup>n</sup> – 1", "6.94"))
    b.append(p(
        "Mã có thể được tạo ra bằng cách đọc tầng thứ n của một thanh ghi dịch hồi tiếp sau j lần dịch. Thanh ghi "
        "phải được khởi tạo sao cho ít nhất một thanh ghi khác không, và kết nối hồi tiếp thực hiện công thức"))
    b.append(eq("X(0) = X(n) ⊕ c(n–1)·X(n–1) ⊕ … ⊕ c(1)·X(1)", "6.95"))
    b.append(p(
        "trong đó các hệ số c bằng 0 hoặc 1. Các thanh ghi hồi tiếp có c bằng 1 được liệt kê trong Bảng 6.18 với n "
        "từ 4 đến 14. Dưới đây là một PRBS với n = 4, thu được khi khởi tạo mọi thanh ghi bằng 1: 111101011001000. "
        "Với một đĩa mã hoá quay, 15 cung ấy sẽ có bề rộng 24°."))
    b.append(table(
        ["n", "Độ dài", "Chuỗi trực tiếp", "Chuỗi ngược"],
        [["4", "15", "1, 4", "3, 4"],
         ["5", "31", "2, 5", "3, 5"],
         ["6", "63", "1, 6", "5, 6"],
         ["7", "127", "3, 7", "4, 7"],
         ["8", "255", "2, 3, 4, 8", "4, 5, 6, 8"],
         ["9", "511", "4, 9", "5, 9"],
         ["10", "1 023", "3, 10", "7, 10"],
         ["11", "2 047", "2, 11", "9, 11"],
         ["12", "4 095", "1, 4, 6, 12", "6, 8, 11, 12"],
         ["13", "8 191", "1, 3, 4, 13", "9, 10, 12, 13"],
         ["14", "16 383", "1, 6, 10, 14", "4, 8, 13, 14"]],
        "Bảng 6.18 · Các kết nối hồi tiếp của thanh ghi dịch để tạo chuỗi nhị phân giả ngẫu nhiên"))
    b.append(p(
        "Petriu [3, 4] mô tả một cấu hình khả dĩ của đĩa PRBS dùng một rãnh PRBS và một rãnh đồng bộ (Hình 6-70), "
        "cùng phương pháp xử lý để khôi phục vị trí dưới dạng nhị phân tự nhiên. Bảng 6.18 cho cấu hình hồi tiếp "
        "ngược. Thanh ghi dịch được nạp ban đầu bằng bộ n giá trị hiện thời. Sau đó logic ngược được áp dụng lặp "
        "đi lặp lại cho tới khi đạt tới chuỗi ban đầu của PRBS. Tại điểm ấy, bộ đếm n bit biểu diễn giá trị của j. "
        "Với bộ mã hoá quay, (j · 360)/(2<sup>n</sup> – 1) là vị trí góc hiện thời; còn với bộ mã hoá thẳng, vị trí "
        "là j · P với P là chiều dài vạch hay bước của thang đo."))
    b.append(fig(70, F.fig_6_70()))
    b.append(p(
        "Petriu [4] đề nghị dùng n + 1 đầu đọc trên rãnh PRBS để cho phép đọc hai chiều không nhoè. Rãnh đồng bộ có "
        "một dãy 0 và 1 thành những vạch cùng bề rộng với rãnh PRBS và cùng pha. Giữa đầu đọc A trên rãnh đồng bộ "
        "và n + 1 đầu đọc trên rãnh PRBS có một độ dịch P/2, với P là chiều dài vạch. n + 1 vạch được cập nhật "
        "theo một xung kích từ tín hiệu A. Điều này bảo đảm n + 1 đầu đọc nằm gần đúng giữa vạch PRBS. Một đầu đọc "
        "thứ hai, gọi là B, trên rãnh đồng bộ được dịch P/2 so với A. A và B vuông pha, cho phép dùng đồng thời cả "
        "hai để tạo tín hiệu chiều chuyển động. Bộ n giá trị đúng — tức tập con dưới hay tập con trên — được chọn "
        "theo chiều chuyển động rồi biến đổi sang nhị phân tự nhiên bằng hồi tiếp ngược."))
    b.append(p(
        "Petriu [4] cũng đề nghị một cách đơn giản để tăng độ phân giải gấp đôi nhờ thêm vài linh kiện điện tử. Ông "
        "cũng đề xuất một sơ đồ dùng số cung tuỳ ý (không phải 2<sup>n</sup> – 1), nhưng cách này cần thêm một rãnh "
        "thứ ba và vài mạch hiệu chỉnh để xử lý n – 1 vạch cuối của đĩa, vì những vạch ấy không còn là mẫu PRBS "
        "nữa. Tomlinson [5] đề xuất một phương pháp cắt ngắn chuỗi PRBS khác mà không cần rãnh thứ ba. Thay vào "
        "đó, một số mã nhất định bị loại bỏ bằng cách thêm logic vào cả logic hồi tiếp trực tiếp lẫn hồi tiếp "
        "ngược."))
    b.append(p(
        "Ross và Taylor [6], Arsic và Denic [7] đề nghị những cách giảm số đầu đọc bằng cách tích luỹ các kết quả "
        "đọc vào một thanh ghi dịch, sao cho chỉ cần tối thiểu hai đầu đọc là đủ để đọc rãnh PRBS. Tuy nhiên, khi "
        "khởi động, vị trí đúng chưa được biết cho tới khi bộ mã hoá đã dịch chuyển đủ để mọi thanh ghi được cập "
        "nhật. Vì vậy loại bộ mã hoá này không hoàn toàn tuyệt đối: nó không chỉ ra vị trí đúng ngay khi khởi "
        "động. Cuối cùng, Arazi [8] nhắc tới việc dùng một ROM lưu bảng chuyển đổi như một phương án thay cho mạch "
        "logic."))

    b.append(h3("Giải mã quang", "Optical resolving"))
    b.append(p(
        "Phương pháp này có những nét tương đồng với bản đối chứng điện từ của nó và dựa trên việc tạo ra một cặp "
        "tín hiệu sin và cosin cho mỗi vòng quay trục của bộ mã hoá. Độ phân giải và độ chính xác của bộ mã hoá "
        "này phụ thuộc khả năng tạo ra các tín hiệu đúng dạng lý tưởng của chúng, và phụ thuộc năng lực giải mã của "
        "mạch điện tử làm nhiệm vụ biến đổi toạ độ vuông góc sang toạ độ cực để cho ra dữ liệu góc ở đầu ra. Các "
        "phương pháp thực hiện phép biến đổi này tương tự những gì được mô tả trong phần nội suy tín hiệu vuông "
        "pha tương tự. Đĩa mã của một thiết bị như vậy không chứa một dãy đường song song có bước không đổi, mà "
        "dựa vào những rãnh mã đặc biệt có đầu ra tín hiệu dạng tương tự. Điều này có thể thực hiện bằng cách thay "
        "đổi tiết diện của rãnh mã, hoặc bằng cách cho mật độ quang của chúng biến thiên dọc theo vòng quay. Với "
        "trường hợp sau, không cần dùng mặt nạ che."))

    # ------------------------------------------------------------ incremental
    b.append(h2("Bộ mã hoá gia số", "Incremental encoders"))
    b.append(h3("Tín hiệu vuông pha số", "Digital quadrature signals"))
    b.append(p(
        "Hình 6-71 minh hoạ khái niệm bộ mã hoá quang quay kiểu gia số. Đĩa gắn trên trục có một dãy cung tối và "
        "sáng xen kẽ, dài bằng nhau và số lượng bằng nhau. Mã tối–sáng được phát hiện bằng một mặt nạ cố định có "
        "hai cửa sổ A và B, lệch nhau một phần tư chu kỳ. Khi một cung sáng phủ lên cửa sổ thì tạo ra tín hiệu 1, "
        "còn cung tối cho ra 0. Tại chỗ chuyển tiếp sẽ xuất hiện tín hiệu lên hoặc xuống. Những tín hiệu này cần "
        "được xử lý sơ bộ để làm vuông và tránh các vấn đề gắn với chuyển động chậm tại các vị trí chuyển tiếp — "
        "hệ quả là thời gian lên và thời gian xuống dài, trong điều kiện nhiễu thấp. Hai tín hiệu A và B sau khi "
        "làm sạch là hai xung vuông lệch pha 90°, gọi là tín hiệu vuông pha."))
    b.append(fig(71, F.fig_6_71()))
    b.append(p(
        "Vì tín hiệu A và B chỉ có bốn trạng thái khả dĩ, rõ ràng chúng không đủ để phân biệt quá bốn vị trí khác "
        "nhau. Do đó, việc phân biệt vị trí tuyệt đối chỉ có thể thực hiện trong phạm vi một chu kỳ vuông pha. Thay "
        "vào đó, tín hiệu vuông pha được dùng để tăng hoặc giảm một bộ đếm cho ra vị trí thực. Bộ đếm được khởi "
        "tạo (thường là đặt lại) nhờ tín hiệu pha z tạo ra trên một rãnh riêng — rãnh trong cùng trên Hình 6-71. "
        "Cũng có thể có nhiều tín hiệu pha z trên toàn dải của bộ mã hoá, với khoảng cách giữa các dấu pha z được "
        "mã hoá khác nhau. Mã ấy có thể dùng để khởi tạo bộ đếm tại những vị trí khác không."))
    b.append(p(
        "Hình 6-72(a) trình bày một mạch đơn giản của Conner [9] cho một xung đếm trên mỗi chu kỳ của tín hiệu "
        "vuông pha. Thông tin chiều cần thiết để quyết định tăng hay giảm bộ đếm cũng được tạo ra. Cần lưu ý rằng "
        "các trigger Schmitt cung cấp một lượng trễ nào đó và chỉnh lại các sườn lên, sườn xuống từ bộ mã hoá. "
        "Trong môi trường rất nhiễu cần thêm mạch để tăng lượng trễ. Có thể cần xử lý thêm trước khi đưa các tín "
        "hiệu này vào bộ đếm."))
    b.append(fig(72, F.fig_6_72()))
    b.append(p(
        "Lý do là nếu sau một lần đếm có một chuyển động nhỏ ngược chiều mà không phát ra xung đếm ngược, rồi sau "
        "đó lại có chuyển động xuôi chiều, thì chuyển động xuôi ấy tạo ra xung đếm thứ hai tại cùng một vị trí. "
        "Kuzdrall [10] đề nghị một mạch đáng tin cậy hơn trên Hình 6-72(b). Mạch này điều khiển một bộ đếm "
        "74HC193 bằng một xung nhịp xuống và một xung nhịp lên. Cả hai flip-flop bình thường ở trạng thái cao. Hễ "
        "một trong hai chuyển sang trạng thái thấp thì nó sớm được đặt lại nhờ chính đầu ra ấy được dùng làm tín "
        "hiệu Set. Đầu ra thấp ấy chỉ có thể xuất hiện khi pha B thấp và có chuyển tiếp trên A. Tuỳ chiều của "
        "chuyển tiếp đó, một trong hai flip-flop tạo ra trạng thái thấp ngắn, gây ra một lần đếm lên hoặc xuống "
        "thích hợp. Vấn đề gắn với dao động nhỏ quanh một vị trí được giảm bớt, vì các lần đếm lên và xuống xảy ra "
        "tại cùng một vị trí của bộ mã hoá. Venugopal [11] đề nghị mạch trên Hình 6-72(c) cho hiệu quả tương tự. "
        "Một lần đếm chỉ có thể xảy ra khi B thấp và có chuyển tiếp trên A. Tuỳ chiều chuyển tiếp, một trong hai "
        "mạch đơn ổn được kích và cho phép đếm tại đầu vào thích hợp của bộ đếm 74LS193."))
    b.append(p(
        "Trong trường hợp môi trường nhiễu, Holle [12] mô tả một bộ lọc số để làm sạch thêm tín hiệu A và B; bộ "
        "lọc này dùng một số ít cổng logic để tạo thành bộ lọc trễ 4 bit. Wigmore [13] đề xuất các mạch khác cho "
        "việc phát hiện đếm và chiều. Bảng 6.23 và 6.24 liệt kê một số chip thương mại cùng thông tin về nhà cung "
        "cấp. Một số chip cho ra tín hiệu đếm và chiều, hoặc tín hiệu xung nhịp lên và xuống. Một số khác còn tích "
        "hợp cả bộ đếm."))
    b.append(p(
        "Các mạch trên chưa khai thác triệt để thông tin chứa trong tín hiệu vuông pha, vì chỉ một trong bốn sườn "
        "(hay trạng thái) trong một chu kỳ vuông pha được dùng để đếm. Hình 6-73 trình bày một phiên bản chỉnh sửa "
        "đôi chút của mạch chia bốn do Butler [14] đề nghị. Hai thanh ghi dịch 4 bit, ba cổng XOR và một bộ phân "
        "kênh tám kênh tạo ra các tín hiệu đếm lên và đếm xuống. Các thanh ghi dịch có xung nhịp tạo ra một mã 4 "
        "bit cho bộ phân kênh ở mỗi chu kỳ xung nhịp. Để bảo đảm không bỏ sót chuyển tiếp nào của bộ mã hoá, tần "
        "số xung nhịp phải ít nhất bằng 8·N·S, trong đó N là số chu kỳ bộ mã hoá tạo ra trong mỗi vòng quay trục "
        "và S là tốc độ cực đại tính bằng vòng trên giây. Các tín hiệu lên và xuống có thể đưa vào các bộ đếm "
        "74ALS193 mắc nối tiếp. Mạch này phân tích trạng thái hiện thời và trạng thái trước đó của hai kênh A và B "
        "để hoặc đếm lên, hoặc đếm xuống, hoặc phát cờ báo lỗi khi xảy ra một trình tự không hợp lệ."))
    b.append(fig(73, F.fig_6_73()))
    b.append(p(
        "Kuzdrall [10] đề nghị coi một chu kỳ tín hiệu vuông pha như một mã Gray, để hai bit có nghĩa nhỏ nhất của "
        "số đếm thu được bằng cách biến đổi mã Gray sang mã nhị phân như trên Hình 6-72(b). Pha A tạo ra bit 1 của "
        "vị trí nhị phân tự nhiên, còn pha B được XOR với pha A để tạo ra bit có nghĩa nhỏ nhất. Bộ đếm cung cấp "
        "các bit còn lại của vị trí nhị phân tự nhiên. Marty [15] đề nghị một máy trạng thái lưu cả giá trị A và B "
        "hiện thời lẫn các giá trị trước đó bằng các flip-flop kiểu D (tương tự cách của Butler) để tạo thành một "
        "số thập lục phân. Tổng cộng có tám chữ số hex khác nhau, bốn cho mỗi chiều chuyển động. Một bộ giải mã 4 "
        "đường sang 16 đường sau đó đưa vào hai cổng NAND 4 đầu vào để tạo tín hiệu đếm lên hoặc xuống. Cũng như "
        "với Butler, mạch cuối cùng này không phụ thuộc vào trễ lan truyền như mạch của Kuzdrall."))

    b.append(h3("Tín hiệu vuông pha tương tự", "Analog quadrature signals"))
    b.append(p(
        "Một số bộ mã hoá quang cung cấp tín hiệu vuông pha tương tự dưới dạng một tín hiệu sin(θ), gọi là A, và "
        "một tín hiệu cos(θ), gọi là B, trong đó θ là pha (độ điện) trong một chu kỳ của tín hiệu vuông pha. θ "
        "không bằng góc trục mà liên hệ với nó: 360 độ điện của θ ứng với 360/N độ cơ, với N là số chu kỳ tín "
        "hiệu vuông pha tương tự trong một vòng quay trục. Thật vậy, θ vẫn tồn tại với các bộ mã hoá thẳng loại "
        "này. Tuy các tín hiệu ấy có thể được làm vuông rồi đưa vào bộ đếm chia bốn, chúng cũng có thể được xử lý "
        "trực tiếp để có độ phân giải mịn hơn. Ba kỹ thuật chính là (1) nhiều tín hiệu lệch pha, (2) bảng tra, và "
        "(3) bộ xử lý arctang."))

    b.append(h3("Nội suy bằng mạng điện trở", "Interpolation by resistor network"))
    b.append(p(
        "Phương pháp nhiều tín hiệu lệch pha chỉ dựa vào điện tử để tăng tần số của tín hiệu vuông pha số cuối "
        "cùng lên một số nguyên lần. Benzaid và cộng sự [16] đề nghị mạch trên Hình 6-74(a), trong trường hợp cụ "
        "thể này được thiết kế để tăng tần số bốn lần. Sau đó có thể mắc thêm một mạch chia bốn số (không vẽ ở "
        "đây). Hai tín hiệu A và B được tổ hợp để tạo thêm sáu tín hiệu lệch pha: ba tín hiệu lệch π/8, π/4 và "
        "3π/8 so với A, và ba tín hiệu khác lệch tương tự so với B. Kết quả là có tổng cộng tám tín hiệu sin, lệch "
        "pha nhau α = iπ/8 với i = 0, 1, …, 7. Có thể tổng quát hoá: muốn tăng độ phân giải m lần cần 2m tín hiệu "
        "lệch pha nhau α = iπ/2m với i = 0, 1, …, 2m – 1. Các tín hiệu sin lệch pha sau đó được làm vuông bằng các "
        "bộ chuyển mức TTL. Hình 6-74(b) cho thấy các xung vuông thu được. Phép cộng modul-2 các tín hiệu có i "
        "chẵn cho A′, và tương tự các tín hiệu có i lẻ cho B′. Phép cộng modul-2 được thực hiện bằng các cổng "
        "XOR."))
    b.append(fig(74, F.fig_6_74()))
    b.append(p("Phép cộng vectơ hai tín hiệu A và B ban đầu cho ra các tín hiệu lệch pha. Trọng số của A và B được "
               "tính từ các hệ thức lượng giác:"))
    b.append(eq("sin(θ + α) = cos(α)·sin(θ) + sin(α)·cos(θ)", "6.96"))
    b.append(p("và"))
    b.append(eq("cos(θ + α) = –sin(α)·sin(θ) + cos(α)·cos(θ)", "6.97"))
    b.append(p("trong đó sin(θ) = A và cos(θ) = B. Do đó"))
    b.append(eq("sin(θ + α) = cos(α)·A + sin(α)·B", "6.98"))
    b.append(p("và"))
    b.append(eq("cos(θ + α) = –sin(α)·A + cos(α)·B", "6.99"))
    b.append(p(
        "Cần lưu ý rằng biên độ của các tín hiệu lệch pha không quan trọng, vì chính các điểm qua zero của chúng "
        "mới tạo ra sườn xung vuông. Ngoài ra, trong mạch trên Hình 6-74(a), các trọng số đã được chỉnh sửa đôi "
        "chút để đơn giản hoá việc thực hiện, dẫn tới một biến thiên nhỏ của hệ số lấp đầy của A′ và B′. Cũng có "
        "thể tạo các tín hiệu lệch pha bằng bộ chia áp và trigger Schmitt, trong đó các điện trở chia áp có tỉ số "
        "tan(α) [17]. Khi m tăng, độ chính xác đòi hỏi ở các trọng số trở nên ngặt nghèo hơn, và tốc độ của mạch "
        "điện tử xử lý các tín hiệu vuông tần số cao có thể giới hạn giá trị m khả dĩ của phương pháp này."))

    b.append(h3("Nội suy bằng lấy mẫu và xử lý số", "Interpolation by sampling and numerical processing"))
    b.append(p(
        "Một số phương pháp số hoá tín hiệu vuông pha tương tự để thực hiện nội suy số bên trong một chu kỳ của "
        "tín hiệu vuông pha. Những kỹ thuật này cho phép nội suy cao hơn nữa. Các tín hiệu được lấy mẫu định kỳ "
        "trong mạch lấy mẫu–giữ và được số hoá bằng bộ biến đổi tương tự–số (ADC). Một kỹ thuật dùng bảng nội suy, "
        "kỹ thuật kia thực hiện các phép tính arctang."))
    b.append(p(
        "Hagiwara [18] dùng một ADC m bit để số hoá các tín hiệu tương tự A và B thành các số nhị phân D<sub>a</sub> "
        "và D<sub>b</sub>. Hình 6-75(a) cho thấy cách dùng các số nhị phân ấy làm địa chỉ của một lưới, ở đây được "
        "lập với m = 3 thành một lưới 2<sup>m</sup> × 2<sup>m</sup>. Hagiwara sau đó gán một góc pha cho tâm mỗi ô "
        "của ma trận bằng những phép tính arctang đơn giản. Góc được tính so với tâm của lưới. Góc pha này sau đó "
        "được gán cho một trong 2<sup>n</sup> – 1 mã pha theo công thức"))
    b.append(eq("mã pha = phần nguyên của (2<sup>n</sup> · θ) / 2π", "6.100"))
    b.append(p("như trình bày trên Hình 6-75(b)."))
    b.append(fig(75, F.fig_6_75()))
    b.append(p(
        "Mạch đề nghị bao gồm cả phương tiện thực hiện việc tích luỹ các giá trị nội suy để đưa ra vị trí tuyệt đối "
        "của bộ mã hoá. Một biến thể của mạch này cũng được đề nghị, có thể hiệu chỉnh mã pha theo những sai số đã "
        "biết của tín hiệu bộ mã hoá so với vị trí thực của nó. Để đạt mức nội suy cao nhất có thể, Mayer [19] mô "
        "tả một phương pháp dùng bộ tính arctang. Phương pháp này dùng một bộ vi xử lý để thực hiện các phép tính "
        "lượng giác bậc cao trên các tín hiệu tương tự đã số hoá. Trong khi quá trình ấy diễn ra, các tín hiệu "
        "tương tự vẫn liên tục được làm vuông và đưa vào một bộ đếm chia bốn. Hai nguồn thông tin được kết hợp để "
        "cho ra vị trí của bộ mã hoá với độ phân giải rất cao. Tuy nhiên cần lưu ý: dù độ phân giải lý thuyết thu "
        "được chỉ bị giới hạn bởi ADC, trên thực tế chính chất lượng của tín hiệu tương tự so với vị trí vật lý "
        "đang được đo mới là yếu tố giới hạn độ chính xác đạt được."))

    # ------------------------------------------------------------ principles
    b.append(h2("Nguyên lý mã hoá quang", "Encoding principles"))
    b.append(p(
        "Bộ mã hoá quang dùng một trong ba kỹ thuật để tạo tín hiệu điện từ chuyển động tương đối giữa cách tử và "
        "các đầu đọc. Đó là (1) che hình học, (2) hiệu ứng Moiré, và (3) giao thoa laser. Cần lưu ý rằng bộ mã hoá "
        "tuyệt đối chủ yếu dùng che hình học. Che hình học dựa trên lý thuyết quang hình học và coi ánh sáng "
        "truyền theo đường thẳng. Tuy nhiên, khi bước cách tử giảm và độ phân giải của bộ mã hoá tăng, các hiệu "
        "ứng vân Moiré xuất hiện và được dùng để tạo tín hiệu. Khi ấy hiệu ứng nhiễu xạ trở nên không thể bỏ qua, "
        "nhưng ảnh hưởng của chúng có thể được kiểm soát bằng thiết kế cẩn thận. Cuối cùng, với độ phân giải rất "
        "cao, hiệu ứng nhiễu xạ được khai thác trực tiếp để thực hiện phép đo."))

    b.append(h3("Che hình học", "Geometric masking"))
    b.append(p(
        "Che hình học được áp dụng cho cả bộ mã hoá tuyệt đối lẫn gia số. Trường điện từ gắn với sự lan truyền của "
        "ánh sáng khả kiến được đặc trưng bởi những dao động rất nhanh (tần số cỡ 10<sup>14</sup> s⁻¹). Vì thế có "
        "thể kỳ vọng rằng một phép xấp xỉ bậc một tốt cho các định luật lan truyền ánh sáng thu được bằng cách bỏ "
        "qua bước sóng ánh sáng. Khi ấy có thể bỏ qua hiện tượng nhiễu xạ và coi ánh sáng truyền theo đường "
        "thẳng. Hình học khi đó có thể dùng để phân tích ứng xử của ánh sáng. Phép xấp xỉ này đúng mỗi khi tia "
        "sáng truyền qua một cách tử của bộ mã hoá có bước khá thô (chẳng hạn lớn hơn 10 µm)."))
    b.append(fig(76, F.fig_6_76()))
    b.append(p(
        "Hình 6-76 cho thấy một đoạn thang đo của bộ mã hoá đang được một đầu đọc có nhiều khe quét, nhằm đưa nhiều "
        "ánh sáng hơn lên vùng cảm quang. Nguồn sáng được chuẩn trực (các tia được làm song song với nhau sau khi "
        "đã phát ra theo nhiều hướng từ một nguồn nhỏ), đi qua cách tử cố định hay cách tử chỉ mục, rồi lan truyền "
        "qua cách tử động. Với bộ mã hoá gia số, một đầu thứ hai sẽ đọc trên cùng cách tử động nhưng dịch đi n + "
        "1/4 bước để tạo ra tín hiệu thứ hai lệch pha 90°. Khi các khe của hai cách tử thẳng hàng, lượng ánh sáng "
        "tới bộ tách sóng là cực đại. Tương tự, lượng ánh sáng truyền qua là cực tiểu khi hai cách tử lệch pha "
        "180°. Tuỳ thiết kế cách tử — chẳng hạn hệ số lấp đầy của các cung truyền qua và cung chắn sáng — sẽ thu "
        "được những dạng tín hiệu tuần hoàn khác nhau."))
    b.append(p(
        "Nói chung, cần lưu ý rằng bộ mã hoá quang cũng có thể được chế tạo theo kiểu phản xạ thay vì truyền qua. "
        "Ngoài ra, ở một số bộ mã hoá quang tuyệt đối, nguyên lý mã hoá không dựa vào một cách tử sơ cấp theo đúng "
        "nghĩa của từ này, hoặc hệ phát hiện không nhất thiết phải có phần tử che nào."))

    b.append(h3("Vân Moiré", "Moiré fringes"))
    b.append(p(
        "Các phương pháp dùng vân Moiré chủ yếu gắn với bộ mã hoá gia số. Vân Moiré được quan sát khi ánh sáng đi "
        "qua hai mẫu tuần hoàn giống nhau đặt sát nhau và có các đường gần như song song với nhau. Hình 6-77 trình "
        "bày cách tử thẳng và cách tử hướng tâm tạo ra vân Moiré. Xét một cách tử thẳng có hệ số truyền biên độ "
        "dạng sin như Gasvik [20] đề nghị:"))
    b.append(eq("f(x, y) = a + a·cos(2πx / P)", "6.101"))
    b.append(p(
        "trong đó P là bước cách tử, a là biên độ, và x được đo vuông góc với các đường cách tử. Cũng có thể biểu "
        "diễn một cách tử kiểu xung vuông bằng chuỗi Fourier (với cách tử hướng tâm) hoặc bằng tích phân Fourier "
        "(với cách tử thẳng). Khi hai cách tử thẳng a và b được đặt tiếp xúc nhau, hệ số truyền tổng hợp f<sub>c</sub> "
        "là tích các hệ số truyền riêng f<sub>a</sub> và f<sub>b</sub>:"))
    b.append(eq("f<sub>c</sub> = f<sub>a</sub> × f<sub>b</sub>", "6.102"))
    b.append(fig(77, F.fig_6_77()))
    b.append(p("Khi giữa hai cách tử có một độ lệch γ, khoảng cách giữa các vân Moiré là d với"))
    b.append(eq("d = P / [2·sin(γ/2)]", "6.103"))
    b.append(p("và với γ nhỏ thì"))
    b.append(eq("d = P / γ", "6.104"))
    b.append(p(
        "Từ đó suy ra: khi hai cách tử dịch tương đối với nhau một đoạn x′ theo phương vuông góc với các đường của "
        "chúng, pha φ(x′) của vân Moiré tại một vị trí cố định thay đổi một lượng"))
    b.append(eq("φ(x′) = 2πx′ / P", "6.105"))
    b.append(p(
        "Thực chất, mỗi khi x′ bằng P thì toàn bộ mẫu vân Moiré trải qua một chu kỳ biến thiên trọn vẹn. Nếu hai "
        "cách tử được chỉnh tới gần song song thì các vân “xù” ra (xem Burch [22]) tới bề rộng vô hạn. Trong điều "
        "kiện ấy không quan sát được chuyển động vân, và toàn bộ vùng quan sát chỉ đơn giản chuyển từ sáng sang "
        "tối. Những hiệu ứng này được dự đoán bằng toán học nhờ một tích phân chập:"))
    b.append(eq("f<sub>c</sub>(x′) = ∫<sub>x₁</sub><sup>x₂</sup> f<sub>a</sub>(x)·f<sub>b</sub>(x – x′) dx", "6.106"))
    b.append(p(
        "với x₁ đến x₂ là vùng mà bộ tách sóng quang phủ lên. Nếu g<sub>a</sub>(k) và g<sub>b</sub>(k) là các biến "
        "đổi Fourier mũ của f<sub>a</sub> và f<sub>b</sub>, thì đáp ứng f<sub>c</sub> của bộ tách sóng quang sẽ có "
        "biến đổi Fourier g<sub>c</sub>(k) là"))
    b.append(eq("g<sub>c</sub>(k) = g<sub>a</sub>(k)·g<sub>b</sub>(–k)", "6.107"))
    b.append(p(
        "Hiệu ứng Moiré có thể thu được khi truyền qua hoặc khi phản xạ tại cách tử. Tuy nhiên cần ghi nhớ rằng "
        "khi bước cách tử giảm, hiệu ứng nhiễu xạ trở nên đáng kể; việc thiết kế và chỉnh khe hở giữa cách tử cố "
        "định và cách tử động, cùng cách bố trí chiếu sáng và phát hiện, trở nên quyết định. Vì một số lượng lớn "
        "đường cách tử được dùng để tạo đáp ứng của bộ tách sóng quang, những khuyết tật cục bộ nhỏ của bước cách "
        "tử được lấy trung bình, nhờ vậy độ chính xác đo được cải thiện."))

    b.append(h3("Bộ mã hoá dựa trên nhiễu xạ", "Diffraction-based encoders"))
    b.append(p(
        "Bộ mã hoá dựa trên nhiễu xạ được dùng cho những mức chính xác cao nhất. Chúng khai thác thành công các "
        "hiệu ứng nhiễu xạ và được gọi là bộ mã hoá quang vật lý, để phân biệt với bộ mã hoá quang hình học. Hình "
        "6-78 cho thấy các hiệu ứng nhiễu xạ quan sát được khi ánh sáng kết hợp gặp một dãy khe [20]. Khe rộng "
        "chỉ vài bước sóng, nên quan sát được hiệu ứng nhiễu xạ mạnh. Mỗi khe có thể coi như một nguồn sáng kết "
        "hợp phát ra các mặt sóng tròn. Dọc theo những phương nhất định, các phần của những mặt sóng ấy đồng pha "
        "với nhau. Những phương ấy được cho bởi"))
    b.append(eq("sin θ<sub>m</sub> = mλ / P", "6.108"))
    b.append(p(
        "trong đó m là số nguyên dương hoặc âm và là bậc nhiễu xạ, còn P là bước của cách tử nhiễu xạ. Giả sử bây "
        "giờ các khe dịch đi một đoạn x như trên Hình 6-78. Khi ấy pha của mặt sóng tại một vị trí cố định sẽ tăng "
        "với m dương và giảm với m âm một lượng 2πmx/P. Khi mẫu khe đã dịch đúng một chu kỳ của mẫu, hai mặt sóng "
        "sẽ phát triển một độ lệch pha tương đối 2m chu kỳ. Hai mặt sóng lệch pha ấy có thể được hợp lại để tạo ra "
        "vân giao thoa."))
    b.append(fig(78, F.fig_6_78()))

    b.append(h3("Bộ mã hoá quay", "Rotary encoders"))
    b.append(p(
        "Bộ mã hoá quay laser của Canon dùng một cấu hình quang tạo ra bốn chu kỳ vân giao thoa cho mỗi chu kỳ của "
        "cách tử nhiễu xạ. Điều này đạt được bằng cách tách mặt sóng ban đầu làm hai và đọc cách tử tại hai vị trí "
        "đối tâm. Việc phản xạ cả hai chùm đã nhiễu xạ trở lại qua cách tử làm độ phân giải tăng thêm gấp đôi. "
        "Cuối cùng hai chùm được hợp lại để đếm vân giao thoa. Hơn nữa, như Nishimura và Ishizuka [23] giải thích, "
        "việc dùng những phần đối tâm của đĩa làm suy giảm ảnh hưởng của độ lệch tâm. Một bộ mã hoá có đường kính "
        "ngoài 36 mm tạo ra 81 000 chu kỳ vuông pha tương tự trong một vòng quay. Cách tử có bước xấp xỉ 5 µm và "
        "ánh sáng laser có bước sóng 780 nm."))

    b.append(h3("Bộ mã hoá thẳng", "Linear encoders"))
    b.append(p(
        "Sony tiếp thị một bộ mã hoá thẳng laser dùng cách tử hologram khối có bước 0,55 µm [24]. Hình 6-79 cho "
        "một số hiểu biết về nguyên lý làm việc của loại bộ mã hoá này. Về lý thuyết, để cường độ chùm sáng phản xạ "
        "qua cách tử hologram đạt cực đại, hiệu quang trình từ các gương phẳng liên tiếp phải bằng λ [20]. Bộ mã "
        "hoá Sony Laserscale dùng laser bán dẫn làm nguồn sáng kết hợp. Bộ chia chùm tạo ra hai chùm để đọc cách "
        "tử tại hai vị trí riêng biệt. Hai chùm sau đó bị cách tử hologram nhiễu xạ, tiếp đến phản xạ trên các "
        "gương và đi qua cách tử lần thứ hai. Cuối cùng chúng được hợp lại ở bộ tách sóng quang để tạo vân giao "
        "thoa. Vì hai chùm bị cách tử nhiễu xạ theo hai chiều ngược nhau, và vì chúng đi qua cách tử hai lần, nên "
        "khi cách tử dịch đúng một bước thì thu được bốn chu kỳ tín hiệu."))
    b.append(fig(79, F.fig_6_79()))
    b.append(p(
        "Hãng Heidenhain sản xuất cả bộ mã hoá thẳng lẫn quay có độ phân giải rất cao, cũng dùng các nguyên lý "
        "nhiễu xạ. Cách tiếp cận của họ, khác với những cách đã nêu, dùng một cách tử chỉ mục và một cách tử thang "
        "đo kiểu phản xạ [17, 25]."))
    b.append(p(
        "Hãng Renishaw dùng một cách tử phản xạ mịn có bước 20 µm làm tán xạ ánh sáng từ một diode phát quang hồng "
        "ngoại. Để tránh những vấn đề do hiệu ứng nhiễu xạ gây ra, cách tử chỉ mục của một thiết kế Moiré thông "
        "thường sẽ phải đặt rất sát cách tử chính. Thay vào đó, cách tử chỉ mục được đặt cách xa 2,5 mm. Khi ấy "
        "cách tử chỉ mục có thể nhiễu xạ ánh sáng đã tán xạ từ cách tử chính và tạo ảnh của nó thêm 2,5 mm nữa. "
        "Tại đó hình thành một mẫu vân kiểu Moiré và được phân tích quang điện [26]."))

    # ------------------------------------------------------------ components
    b.append(h2("Linh kiện và công nghệ", "Components and technology"))
    b.append(p("Việc chọn một bộ mã hoá đòi hỏi cân nhắc cẩn thận nhiều yếu tố, chẳng hạn:"))
    b.append(ul([
        "độ phân giải, độ lặp lại và độ chính xác (độ tuyến tính) cần thiết;",
        "tốc độ làm việc cực đại và cực tiểu;",
        "điều kiện môi trường: dải nhiệt độ, độ ẩm tương đối (có ngưng tụ hay không ngưng tụ), các chất nhiễm "
        "như bụi, nước, dầu, v.v.;",
        "mômen ma sát (hoặc lực ma sát) cực tiểu chấp nhận được;",
        "quán tính cực đại chấp nhận được;",
        "không gian sẵn có;",
        "vị trí cần biết ngay sau khi mất nguồn;",
        "dải đo tính bằng độ (hoặc mm);",
        "cách lắp đặt và tải trọng tác dụng lên trục;",
        "giá thành.",
    ]))
    b.append(p(
        "Bộ mã hoá quay đôi khi cũng dùng các băng phản xạ dán lên, hoặc các vạch khắc trực tiếp vào, bề mặt của "
        "một tang trống hay một trục chính để đọc từ bên cạnh. Trong những trường hợp đặc biệt, băng hoặc vạch "
        "khắc loại này có thể được chế tạo cho ôm theo bề mặt của một cam có tiết diện elip hoặc một đường bao "
        "không đều khác. Cách tử sơ cấp dạng trụ dùng đầu đọc truyền qua cũng đã được chế tạo."))
    b.append(p(
        "Cách tử chính (thang đo) có rất nhiều loại vật liệu, cho cả đế lẫn phần vạch. Renishaw cũng cung cấp các "
        "thang đo mềm dùng đế bằng băng kim loại, cho phép đọc liên tục chuyển động thẳng với chiều dài rất lớn "
        "(hàng chục mét). Bảng 6.19 đến 6.21 liệt kê một số bộ mã hoá hiện có trên thị trường. Danh sách này không "
        "đầy đủ về mặt nhà cung cấp và không bao gồm mọi mô hình của các hãng được liệt kê. Bảng 6.22 cho địa chỉ "
        "và số điện thoại của các nhà cung cấp. Bảng 6.23 và 6.24 liệt kê một số nhà cung cấp mạch giải mã vuông "
        "pha."))

    b.append(table(
        ["Hãng", "Mã hiệu", "Kiểu đầu ra", "Số đếm", "Độ phân giải", "Giá"],
        [["BEI", "H25", "Xung vuông", "2 540", "50 800", "340 $"],
         ["Canon", "K1", "Sóng sin", "81 000", "1 296 000", "2 700 $"],
         ["Canon", "X-1M", "Sóng sin", "225 000", "18 000 000", "14 000 $"],
         ["Dynamics", "25", "Sóng sin", "3 000", "60 000", "290 $"],
         ["Dynamics", "35", "Sóng sin", "9 000", "360 000", "1 150 $"],
         ["Gurley", "911", "Xung vuông", "1 800", "144 000", "1 300 $"],
         ["Gurley", "920", "Xung vuông", "4 500", "144 000", "500 $"],
         ["Gurley", "835", "Xung vuông", "11 250", "360 000", "1 500 $"],
         ["Heidenhain", "ROD 426", "Xung vuông", "50 đến 10 000", "200 đến 40 000", "370 $"],
         ["Heidenhain", "ROD 905", "Tương tự", "36 000", "0,035 giây cung", "12 600 $"],
         ["Lucas Ledex", "LD20", "Xung vuông", "100", "—", "180 $"],
         ["Lucas Ledex", "LD20", "Xung vuông", "1 000", "—", "195 $"],
         ["Lucas Ledex", "DG60L", "Xung vuông", "5 000", "—", "245 $"],
         ["Renco", "RM21", "Xung vuông", "2 048", "—", "176 $"],
         ["TR Electronic", "IE58", "Xung vuông", "10 000", "—", "428 $"]],
        "Bảng 6.19 · Bộ mã hoá quang quay kiểu gia số thương mại. Số đếm là số chu kỳ vuông pha trên một vòng khi "
        "chưa chia bốn điện tử hay nội suy. Độ phân giải, trừ khi có ghi khác, là số đếm trên một vòng có nội suy "
        "điện tử (trong hoặc ngoài bộ mã hoá) do hãng cung cấp như một tuỳ chọn. Giá theo đơn hàng một chiếc, "
        "không dùng để so sánh sản phẩm vì còn nhiều đặc tính khác không liệt kê ở đây cũng quyết định giá."))

    b.append(table(
        ["Hãng", "Mã hiệu", "Số bước mỗi vòng", "Số vòng", "Giá"],
        [["BEI", "M25", "65 536", "1", "2 130 $"],
         ["BEI", "MT40", "512", "16", "1 240 $"],
         ["BEI", "MT40", "65 530", "512", "5 000 $"],
         ["Gurley", "25/04S", "131 072", "1", "1 900 $"],
         ["Heidenhain", "ROC 424", "4 096", "4 096", "—"],
         ["Lucas Ledex", "AG60E", "360 hoặc 512", "1", "486 $"],
         ["Lucas Ledex", "AG661", "4 096", "4 096", "1 260 $"],
         ["TR Electronic", "CE65", "8 192", "4 096", "1 408 $"]],
        "Bảng 6.20 · Bộ mã hoá quang quay tuyệt đối thương mại. Giá theo đơn hàng một chiếc; đầu ra của CE65 có "
        "thể lập trình được."))

    b.append(table(
        ["Hãng", "Mã hiệu", "Kiểu đầu ra", "Bước", "Độ phân giải", "Chiều dài (mm)", "Giá"],
        [["Canon", "ML-16+", "Sóng sin", "1,6 µm", "0,4 µm", "đến 300", "1 525 $ (50 mm)"],
         ["Canon", "ML-08+", "Sóng sin", "0,8 µm", "0,2 µm", "đến 150", "3 100 $"],
         ["Gurley", "LE18", "Xung vuông", "20 µm", "0,1 µm", "đến 1 500", "750 $ (1 000 mm)"],
         ["Gurley", "LE25", "Xung vuông", "20 µm", "0,1 µm", "đến 3 000", "800 $ (1 000 mm)"],
         ["Heidenhain", "LS603", "Sóng sin", "20 µm", "5 µm", "đến 3 040", "932 $ (1 020 mm)"],
         ["Heidenhain", "LIP401", "Sóng sin", "2 µm", "0,005 µm", "đến 420", "4 000 $ (100 mm)"],
         ["Renishaw", "RG2", "RS422A", "20 µm", "0,5 µm", "đến 60 000", "640 $ + 360 $/1 000 mm"],
         ["Sony", "BS75A-30NS", "Xung vuông", "0,14 µm", "0,05 µm", "30", "2 628 $"]],
        "Bảng 6.21 · Bộ mã hoá quang thẳng kiểu gia số thương mại. Bước là chu kỳ vuông pha khi chưa chia bốn hay "
        "nội suy điện tử. Độ phân giải tính khi có nội suy điện tử do hãng cung cấp."))

    b.append(table(
        ["Hãng", "Trụ sở"],
        [["BEI Sensors and Motion Systems, Encoder Systems Division", "Sylmar, CA, Hoa Kỳ"],
         ["Canon USA Inc., Components Division", "Lake Success, NY, Hoa Kỳ"],
         ["Dr. Johannes Heidenhain GmbH", "Traunreut, Đức"],
         ["Gurley Precision Instruments Inc.", "Troy, NY, Hoa Kỳ"],
         ["Ledex Products, Lucas Control Systems Products", "Vandalia, OH, Hoa Kỳ"],
         ["Renco Encoders Inc.", "Goleta, CA, Hoa Kỳ"],
         ["Renishaw plc, Transducer Systems Division", "Wotton-under-Edge, Vương quốc Anh"],
         ["TR Electronic GmbH", "Trossingen, Đức"],
         ["Sony Magnescale Inc.", "Shinagawa-ku, Tokyo, Nhật Bản"]],
        "Bảng 6.22 · Các hãng sản xuất bộ mã hoá quang (địa chỉ và số điện thoại theo ấn bản 1999 của sổ tay)."))

    b.append(table(
        ["Hãng", "Mã hiệu", "Đầu ra", "Hệ số giải mã", "Bộ đếm", "Giá"],
        [["Hewlett Packard", "HCTL-2000", "Số đếm", "12 bit", "×4", "12,75 $"],
         ["Hewlett Packard", "HCTL-2016", "Số đếm", "16 bit", "×4", "12,75 $"],
         ["Hewlett Packard", "HCTL-2020", "Số đếm", "16 bit và đầu ra nối tiếp", "×4", "14,55 $"],
         ["U.S. Digital Corp.", "LS7083", "Xung nhịp lên và xuống", "×1 hoặc ×4", "—", "3,05 $"],
         ["U.S. Digital Corp.", "LS7084", "Số đếm và chiều", "×1 hoặc ×4", "—", "3,60 $"]],
        "Bảng 6.23 · Mạch giải mã tín hiệu vuông pha số thương mại"))

    b.append(table(
        ["Hãng", "Trụ sở"],
        [["U.S. Digital Corporation", "Vancouver, WA, Hoa Kỳ"],
         ["Hewlett-Packard Company, Direct Marketing Organization", "Santa Clara, CA, Hoa Kỳ"]],
        "Bảng 6.24 · Các hãng sản xuất bộ giải mã chia bốn"))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "P. E. Stephens and G. G. Davies, New developments in optical shaft-angle encoder design, "
        "<i>Marconi Rev.</i>, 46 (228), 26–42, 1983.",
        "P. Sente and H. Buyse, From smart sensors to smart actuators: application of digital encoders for "
        "position and speed measurements in numerical control systems, <i>Measurement</i>, 15(1), 25–32, 1995.",
        "E. M. Petriu, Absolute-type position transducers using a pseudorandom encoding, <i>IEEE Trans. Instrum. "
        "Meas.</i>, IM-36, 950–955, 1987.",
        "E. M. Petriu, Scanning method for absolute pseudorandom position encoders, <i>Electron. Lett.</i>, 24, "
        "1236–1237, 1988.",
        "G. H. Tomlinson, Absolute-type shaft encoder using shift register sequences, <i>Electron. Lett.</i>, 23, "
        "398–400, 1987.",
        "J. N. Ross and P. A. Taylor, Incremental digital position encoder with error detection and correction, "
        "<i>Electron. Lett.</i>, 25, 1436–1437, 1989.",
        "M. Arsic and D. Denic, New pseudorandom code reading method applied to position encoders, <i>Electron. "
        "Lett.</i>, 29, 893–894, 1993.",
        "B. Arazi, Position recovery using binary sequences, <i>Electron. Lett.</i>, 20, 61–62, 1984.",
        "D. Conner, Long-lived devices offer high resolution, <i>EDN</i>, 35(9), 57–64, 1990.",
        "J. A. Kuzdrall, Build an error-free encoder interface, <i>Electron. Design</i>, September 17, 81–86, 1992.",
        "P. Venugopal, Reflective optical SMT module reduces encoder size, <i>Power Conversion and Intelligent "
        "Motion</i>, 21(5), 60–62, 1995.",
        "S. Holle, Incremental encoder basics, <i>Sensors</i>, 7(4), 22–30, 1990.",
        "T. Wigmore, Optical shaft encoder from Sharp, <i>Elektor Electron.</i>, 15(169), 60–62, 1989.",
        "M. M. Butler, Simplified multiplier improves standard shaft encoder, <i>Electronics</i>, November 20, "
        "128–129, 1980.",
        "B. Marty, Design a robust quadrature encoder, <i>Electron. Design</i>, June 24, 71–72, 74, 76, 1993.",
        "O. Benzaid and B. M. Bird, Interpolation techniques for incremental encoders, <i>Proc. 23rd Int. "
        "Intelligent Motion Conf.</i>, Jun 22–24, 165–172, 1993.",
        "Heidenhain General Catalog, Dr. Johannes Heidenhain GmbH, Traunreut, Germany, November 1993, 8.",
        "N. Hagiwara, Y. Suzuki and H. Murase, A method of improving the resolution and accuracy of rotary "
        "encoders using a code compensation technique, <i>IEEE Trans. Instrum. Meas.</i>, 41(1), 98–101, 1992.",
        "J. R. R. Mayer, High-resolution of rotary encoder analog quadrature signals, <i>IEEE Trans. Instrum. "
        "Meas.</i>, 43(3), 494–498.",
        "K. J. Gasvik, <i>Optical Metrology</i>, New York: John Wiley &amp; Sons, 1987.",
        "R. W. Ditchburn, <i>Light Volume 1</i>, New York: Academic Press, 1976.",
        "J. M. Burch, The metrological applications of diffraction gratings, in E. Wolf (Ed.) <i>Progress in "
        "Optics</i>, Volume II, Amsterdam: North-Holland Publishing, 1963.",
        "T. Nishimura and K. Ishizuka (Canon Inc., Tokyo), Laser rotary encoders, <i>Motion: Official Journal of "
        "the Electronic Motion Control Association</i>, September/October 1986.",
        "Sony Magnescale America Inc., Hologram technology goes to work, <i>Machine Design</i>, January 12, 1995.",
        "Heidenhain, Encoding systems — Vorsprung durch Heidenhain, <i>Engineering Materials and Design</i>, "
        "September 1989, 53–54.",
        "J. Henshaw (Renishaw), Linear encoder offers superior flexibility, <i>Design Engineering</i>, September "
        "1995.",
    ]))
    b.append(nav(8, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "An optical encoder is a deceptively simple device: a grating, a light source, a detector, and a counter. "
        "Almost all of its engineering difficulty sits in the gap between the grating and the detector, and in "
        "what happens at the moment the beam crosses from one line to the next. This companion page follows the "
        "translation section by section and pulls out the points where the physics, the electronics and the "
        "metrology pull against each other."))
    b.append(fig(66, F.fig_6_66(), "en"))

    b.append(h2("Two questions decide everything", "Hai câu hỏi quyết định mọi thứ"))
    b.append(p(
        "Before any specification is written, two questions settle the architecture. First: must the position be "
        "known at power-on? If yes, the encoder is absolute and the scale must carry a code; if no, an "
        "incremental encoder plus a reference mark will do, at a fraction of the cost and with far finer "
        "resolution per unit of scale length. Second: is the motion bidirectional? If yes, quadrature signals are "
        "mandatory, because a single square wave carries no direction information at all."))
    b.append(p(
        "The classification in Figure 6.66 is organised around those two answers, and it is worth noticing what "
        "the tree does not branch on: accuracy. Resolution and accuracy are different quantities, and the "
        "section is careful about it — increasing resolution by interpolation or by ×4 decoding does not improve "
        "trueness. A 20-bit interpolated reading from a scale whose lines are unevenly spaced is a precise "
        "measurement of a wrong position."))

    b.append(h2("Absolute codes: why binary is not enough", "Vì sao mã nhị phân trực tiếp không dùng được"))
    b.append(fig(67, F.fig_6_67(), "en"))
    b.append(p(
        "The direct binary scale is the obvious design and it fails for one reason: at position 7 → 8 all four "
        "bits change at once. If the four read apertures are not perfectly aligned, the intermediate states "
        "0111, 0011, 0001, 0000 will all be read somewhere along the transition, and some of them are valid codes "
        "for other positions. The error is not a small offset; it is a transient jump to a completely different "
        "number."))
    b.append(p(
        "Two cures are given. Vee-scan staggers the read points so that the transition on each track is detected "
        "at a different longitudinal position, and combinational logic reconstructs the word; the tolerance on "
        "each transition relaxes to ±1/8 of that track's cycle. Gray code removes the problem at the source by "
        "making consecutive words differ in exactly one bit, at the cost of a conversion — a chain of "
        "exclusive-ORs, or a ROM."))
    b.append(fig(68, F.fig_6_68(), "en"))
    b.append(fig(69, F.fig_6_69(), "en"))
    b.append(p(
        "The pseudorandom code is the cleverest of the four and the hardest to explain. A maximal-length sequence "
        "of length 2ⁿ − 1 has the property that every window of n consecutive bits is unique, so a single track "
        "carries the whole position — no parallel tracks, no alignment between them. The price is that the word "
        "must be decoded: the reverse-feedback shift register is run until it returns to the initial sequence, "
        "and the number of steps taken is the position. That is a computation, not a lookup, and it takes time. "
        "It is also why the n + 1 heads and the synchronisation track exist: to guarantee that the window is read "
        "at the middle of a record rather than across an edge."))
    b.append(fig(70, F.fig_6_70(), "en"))

    b.append(h2("Quadrature: four edges, one count", "Bốn sườn, một xung đếm"))
    b.append(fig(71, F.fig_6_71(), "en"))
    b.append(p(
        "A quadrature cycle contains four edges, and the simple circuits count only one of them. That is a factor "
        "of four thrown away for nothing. The ×4 decoders in Figure 6.73 recover it by looking at the present and "
        "previous states of A and B together — which is exactly the Gray-code view of the same signals that "
        "Kuzdrall proposes. Once you see the four states as a 2-bit Gray code, the decoding logic writes itself."))
    b.append(fig(72, F.fig_6_72(), "en"))
    b.append(p(
        "The oscillation problem deserves a moment. If the shaft dithers across a single edge, a naive counter "
        "increments and decrements alternately and the count wanders. Kuzdrall's circuit arranges that the up and "
        "down counts happen at the same encoder position, so the dither cancels instead of accumulating. That is "
        "a logic fix to a mechanical problem, and it is the reason his circuit is still copied."))
    b.append(fig(73, F.fig_6_73(), "en"))
    b.append(p(
        "The clock rule f ≥ 8·N·S is not arbitrary. The shift register needs to see each of the four states at "
        "least once, and the demultiplexer needs a settled 4-bit word, so eight clock periods per quadrature "
        "cycle is the practical minimum. Run the clock slower and transitions are simply missed; the count then "
        "loses a step silently, which is the worst failure mode a position sensor has."))

    b.append(h2("Interpolation: buying resolution with analog quality", "Nội suy: đổi chất lượng tương tự lấy độ phân giải"))
    b.append(fig(74, F.fig_6_74(), "en"))
    b.append(p(
        "Benzaid's network is a trigonometric identity turned into resistors. sin(θ + α) = cos α · sin θ + sin α · "
        "cos θ, so a weighted sum of the two encoder signals is a phase-shifted copy of them. Eight such sums, "
        "squared and exclusive-ORed in even and odd groups, give A′ and B′ at eight times the original frequency. "
        "The elegance is that the amplitudes do not matter — only the zero crossings do — which is why the "
        "weights can be rounded to convenient resistor values at the cost of a little duty-cycle error."))
    b.append(p(
        "The limit is not the resistor tolerance but the quality of the incoming sine and cosine. Mark-space "
        "ratio, quadrature separation and jitter all propagate straight through into the interpolated phase. At "
        "high interpolation factors the analog front end, not the digital counter, becomes the specification."))
    b.append(fig(75, F.fig_6_75(), "en"))
    b.append(p(
        "Hagiwara's two-dimensional table replaces the analog network with memory. Digitise A and B to m bits "
        "each, use the pair as an address, and store the phase code for that cell. The table can also store a "
        "correction, which is the real advantage: known periodic errors in the encoder signals — eccentricity, "
        "graduation error, quadrature mismatch — can be compensated cell by cell. Mayer's arctangent processor "
        "does the same thing with arithmetic instead of memory and reaches the highest interpolation factors, but "
        "the caveat in the text is the important part: the ADC sets the theoretical limit, the analog signal "
        "quality sets the practical one."))

    b.append(h2("Three optical principles, three regimes", "Ba nguyên lý quang, ba chế độ"))
    b.append(fig(76, F.fig_6_76(), "en"))
    b.append(p(
        "Geometric masking is ray optics: light goes straight, the two gratings act as a shutter, and the "
        "detector sees the overlap area. It is valid for pitches above roughly 10 µm and it is what every absolute "
        "encoder uses. The index grating in the read head is there for a practical reason — a single slit passes "
        "very little light, so a row of slits is used to raise the flux onto the detector without changing the "
        "period."))
    b.append(fig(77, F.fig_6_77(), "en"))
    b.append(p(
        "Moiré is the regime where the grating period is comparable to the wavelength but the designer chooses to "
        "treat diffraction as a nuisance rather than a tool. Two gratings of equal pitch, slightly rotated, "
        "produce fringes with period P/γ — a magnification of the grating by a factor of 1/γ. A displacement of "
        "half a pitch moves the fringe pattern by half a fringe, so the detector sees a full cycle for a "
        "half-pitch move. That magnification is the whole point: the detector integrates over many lines and "
        "averages out local pitch errors."))
    b.append(p(
        "The radial case is worth remembering because it is the one that bites in practice. Two radial gratings "
        "with displaced centres give circular fringes through both centres; if the centres coincide the fringes "
        "fluff out to infinite width and the whole field goes dark and light together. That is exactly the "
        "eccentricity error of a real encoder disk, and it is why the Canon rotary design reads at two "
        "diametrically opposed points — the eccentricity then shifts one reading up and the other down, and the "
        "average cancels it."))
    b.append(fig(78, F.fig_6_78(), "en"))
    b.append(p(
        "Diffraction is the regime where the wave nature is used deliberately. Each slit radiates circular "
        "wavefronts; along the directions where those wavefronts are in phase, a plane wave leaves at angle "
        "sin θ_m = mλ/P. Move the grating by x and the m = +1 and m = −1 wavefronts shift by +xλ/P and −xλ/P "
        "respectively, so their relative phase changes by 2xλ/P. Interfere the two orders and you have "
        " subdivided the grating pitch optically, with no interpolation electronics at all."))
    b.append(fig(79, F.fig_6_79(), "en"))
    b.append(p(
        "The Sony hologram encoder doubles that again by passing each beam through the grating twice, which is "
        "where the factor of four per pitch comes from. The condition 2P sin ψ = λ is a Bragg condition: the "
        "successive plane mirrors inside the volume hologram must return wavefronts that add in phase. It is a "
        "reminder that in this regime the grating is not a shutter at all — it is a diffractive optical element, "
        "and the encoder is really a small interferometer."))

    b.append(h2("Choosing one", "Chọn một thiết bị"))
    b.append(p(
        "The ten selection criteria in the text are ordered by how often they decide the purchase, and the order "
        "is instructive. Resolution, repeatability and accuracy come first because they are what the datasheet "
        "quotes; speed comes second because it is what the datasheet omits. Environment comes third and is "
        "usually the real constraint — a scale that reads to 0.1 µm in a laboratory reads to nothing at all in a "
        "coolant mist. Friction torque and inertia matter for a small servo axis and not at all for a slow "
        "positioning table."))
    b.append(p(
        "The commercial tables are a snapshot of 1999 and the prices should be read as orders of magnitude, not "
        "quotes. What has not dated is the spread: three orders of magnitude in resolution and two in price "
        "across encoders that all claim to measure position. The difference is almost never the counter — it is "
        "the grating, the optics and the care with which the read head was aligned."))
    b.append(nav(8, "en"))
    return "".join(b)
