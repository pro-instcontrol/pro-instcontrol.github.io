# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 1, Control systems.

Vietnamese and English prose with all 77 redrawn vector figures.
"""
import boltonfig as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 45
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Hệ thống (system)</em> — tập hợp các phần tử trong một biên giới, nhận đầu vào và cho "
            "đầu ra. · <em>Vòng hở (open-loop)</em> — đầu ra không tác động ngược lại đầu vào. · "
            "<em>Vòng kín (closed-loop)</em> — tín hiệu đầu ra được phản hồi để so sánh với giá trị yêu "
            "cầu. · <em>Phản hồi âm (negative feedback)</em> — tín hiệu phản hồi bị trừ khỏi giá trị đặt. · "
            "<em>Phần tử so sánh (comparison element)</em> — tạo tín hiệu sai lệch. · "
            "<em>Phần tử hiệu chỉnh (correction element)</em> — tác động lên quá trình. · "
            "<em>Cảm biến (sensor)</em> — tạo tín hiệu liên quan đến đại lượng được đo. · "
            "<em>Bộ vi xử lý (microprocessor)</em> — bộ điều khiển số. Tiêu đề mỗi mục giữ nguyên bản "
            "tiếng Anh trong ngoặc để tiện đối chiếu với bản gốc.")
    return note(
        "<b>Key terms.</b> <em>System</em> — parts within a boundary giving outputs from inputs. · "
        "<em>Open-loop</em> — output does not affect the input. · <em>Closed-loop</em> — output is fed "
        "back and compared with the required value. · <em>Negative feedback</em> — feedback subtracted "
        "from the set value. · <em>Comparison element</em> — produces the error signal. · "
        "<em>Correction element</em> — acts on the process. · <em>Sensor</em> — gives a signal related "
        "to the measured variable.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này trình bày một cái nhìn tổng quan phi toán học về hệ thống điều khiển: khái niệm hệ "
        "thống và cách biểu diễn bằng sơ đồ khối, cách sơ đồ khối mô tả hệ điều khiển vòng hở và vòng "
        "kín, các ví dụ về phần tử đo lường, xử lý tín hiệu và hiệu chỉnh, và cuối cùng là sự tổng hợp "
        "thành cấu trúc của nhiều hệ thống điều khiển thực tế."))

    # ---------------------------------------------------------- 1.1
    b.append(h2("1.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Thuật ngữ tự động hóa (automation) dùng để chỉ sự vận hành hoặc điều khiển tự động một quá "
        "trình. Trong sản xuất hiện đại, tự động hóa được dùng ngày càng nhiều — ví dụ máy móc vận hành "
        "tự động, có thể trong một dây chuyền sản xuất với robot, tạo ra các linh kiện hầu như không cần "
        "sự can thiệp của con người. Tự động hóa cũng đang thâm nhập vào các thiết bị gia dụng và văn "
        "phòng. Tự động hóa bao gồm thực hiện các thao tác theo đúng trình tự và duy trì đầu ra ở các "
        "giá trị yêu cầu."))
    b.append(p(
        "Dưới đây là những mốc lịch sử then chốt trong phát triển tự động hóa. Ba mốc đầu liên quan đến "
        "tổ chức sản xuất, tạo điều kiện cho sản xuất tự động:"))
    b.append(ul([
        "Sản xuất hiện đại bắt đầu ở Anh vào thế kỷ 18, khi bánh xe nước và máy hơi nước khiến việc tổ "
        "chức công việc trong các nhà máy hiệu quả hơn so với tại gia đình.",
        "Đầu thế kỷ 20, máy móc có động lực ra đời giúp tăng độ chính xác, các linh kiện được sản xuất "
        "thành các lô đồng nhất thay vì lắp ghép riêng lẻ.",
        "Ý tưởng dây chuyền sản xuất xuất hiện khi Henry Ford phát triển nó năm 1909 cho sản xuất ô tô.",
        "Thập niên 1920: các nguyên lý lý thuyết về hệ thống điều khiển và sử dụng phản hồi để điều "
        "khiển được phát triển (điều khiển tàu thủy, máy bay tự động).",
        "Thập niên 1940 (Thế chiến II): điều khiển quân sự như radar và khóa pháo; bài báo của Bode "
        "năm 1945 về phân tích mạng và thiết kế bộ khuếch đại phản hồi.",
        "Năm 1952: điều khiển số (NC) ra đời, vị trí dụng cụ được định bởi chương trình băng giấy.",
        "Năm 1948: transistor ra đời, dẫn đến mạch tích hợp và những năm 1970 là vi xử lý, giúp điều "
        "khiển trở nên rẻ và phổ biến (máy giặt, máy ảnh tự động lấy nét/lấy sáng).",
    ]))
    b.append(p(
        "Cuốn sách này là lời giới thiệu về các ý tưởng cơ bản để thiết kế hệ thống điều khiển; chương "
        "này giới thiệu khái niệm hệ thống điều khiển và các phần tử cấu thành."))

    # ---------------------------------------------------------- 1.2
    b.append(h2("1.2 Hệ thống", "Systems"))
    b.append(p(
        "Hộp bánh răng ô tô có thể coi là một hệ thống với trục vào và trục ra (Hình 1.1(a)): ta cấp "
        "một chuyển động quay cho trục vào, hệ thống cho chuyển động quay ở trục ra, có liên hệ nào đó "
        "với trục vào. Tương tự, bộ khuếch đại là một hệ thống nhận tín hiệu vào và cho tín hiệu ra liên "
        "quan đến tín hiệu vào (Hình 1.1(b)). Như vậy, một hệ thống giống như một hộp kín: bên trong là "
        "cách thức hoạt động, ta chỉ cần quan tâm đầu vào và đầu ra."))
    b.append(fig(1, F.fig_1_1()))
    b.append(p(
        "Hệ thống được định nghĩa là một sự sắp xếp các phần tử trong một biên giới, cùng làm việc để "
        "tạo ra đầu ra từ đầu vào xác định (Hình 1.1(c)). Biên giới ngăn cách hệ thống với môi trường; "
        "hệ thống tương tác với môi trường qua các tín hiệu đi qua biên giới — đầu vào từ môi trường, đầu "
        "ra ra môi trường. Với kỹ sư, điều quan tâm là đầu vào và đầu ra hơn là chi tiết bên trong."))
    b.append(p(
        "Với hệ thống điều khiển, ta biểu diễn hệ thống vật lý bằng một mô hình gồm các khối có đầu vào, "
        "đầu ra và quan hệ toán học giữa chúng (Hình 1.2, 1.3). Ví dụ: bộ khuếch đại thuật toán được "
        "dùng theo quan hệ vào–ra đã biết mà không cần biết bên trong."))
    b.append(fig(2, F.fig_1_2()))
    b.append(fig(3, F.fig_1_3()))
    b.append(h3("1.2.1 Sơ đồ khối", "Block diagrams"))
    b.append(p(
        "Sơ đồ khối biểu diễn hệ thống: phần tử là hộp có mũi tên vào và ra (Hình 1.4(a)). Nhiều phần "
        "tử nối tiếp thành chuỗi (Hình 1.4(b)). Nút tổng (summing junction) cộng/trừ tín hiệu, đánh dấu "
        "\"+\" hoặc \"−\" (Hình 1.4(c)). Điểm lấy tín hiệu (take-off) tách một tín hiệu ra nhánh khác (Hình "
        "1.4(d)). Hình 1.5 minh họa sơ đồ khối hệ thống sưởi trung tâm dùng phản hồi âm."))
    b.append(fig(4, F.fig_1_4()))
    b.append(fig(5, F.fig_1_5()))

    # ---------------------------------------------------------- 1.3
    b.append(h2("1.3 Mô hình hệ thống điều khiển", "Control systems models"))
    b.append(p(
        "Có hai loại cơ bản (Hình 1.6, 1.7):"))
    b.append(h3("Vòng hở (Open-loop)", "Open-loop"))
    b.append(p(
        "Đầu ra không tác động trở lại tín hiệu vào. Ưu điểm: đơn giản, rẻ, độ tin cậy tốt. Nhược điểm: "
        "không tự hiệu chỉnh khi có nhiễu. Ví dụ sưởi phòng bằng lò điện 1 kW/2 kW: ta chọn và không "
        "điều chỉnh thêm; nếu mở cửa sổ, nhiệt độ không được bù (Hình 1.6). Thường dùng cho các quá "
        "trình tuần tự bật/tắt, như máy giặt."))
    b.append(fig(6, F.fig_1_6()))
    b.append(h3("Vòng kín (Closed-loop)", "Closed-loop"))
    b.append(p(
        "Tín hiệu trạng thái đầu ra được phản hồi về đầu vào, so sánh với giá trị yêu cầu, hiệu chỉnh "
        "đầu ra để duy trì giá trị mong muốn (Hình 1.7). Ưu điểm: chính xác; nhược điểm: phức tạp, đắt "
        "và dễ hỏng do nhiều linh kiện hơn. Ví dụ sưởi phòng có người cầm nhiệt kế hiệu chỉnh (Hình "
        "1.8): phản hồi âm (negative feedback) vì tín hiệu phản hồi bị trừ khỏi giá trị đặt."))
    b.append(fig(7, F.fig_1_7()))
    b.append(fig(8, F.fig_1_8()))
    b.append(h3("1.3.1 Các phần tử cơ bản của hệ vòng hở", "Basic elements of an open-loop control system"))
    b.append(p("Hệ có ba phần tử cơ bản (Hình 1.9): điều khiển (control), hiệu chỉnh (correction) và quá "
               "trình (process). Không có hiệu chỉnh nào bù nhiễu."))
    b.append(fig(9, F.fig_1_9()))
    b.append(h3("1.3.2 Các phần tử cơ bản của hệ vòng kín", "Basic elements of a closed-loop system"))
    b.append(p(
        "Hình 1.10 cho dạng chung của hệ vòng kín. Các phần tử đường truyền thuận (forward path) gồm: "
        "phần tử so sánh, phần tử luật điều khiển, phần tử hiệu chỉnh và quá trình."))
    b.append(fig(10, F.fig_1_10()))
    b.append(p("Các chức năng:"))
    b.append(ul([
        "<b>Phần tử so sánh (comparison element):</b> so sánh giá trị yêu cầu với giá trị đo được, tạo "
        "tín hiệu sai lệch: sai lệch = tín hiệu tham chiếu − tín hiệu đo thực tế.",
        "<b>Phần tử luật điều khiển (control law):</b> quyết định hành động khi có sai lệch — bật/tắt, "
        "tỉ lệ (proportional), tích phân (integral), vi phân (derivative). Bộ khuếch đại vi sai là ví dụ "
        "kết hợp so sánh và luật điều khiển.",
        "<b>Phần tử hiệu chỉnh (correction element):</b> tạo thay đổi trong quá trình; cơ cấu chấp hành "
        "(actuator) cung cấp năng lượng — ví dụ động cơ, xi lanh (Hình 1.11).",
        "<b>Quá trình (process):</b> hệ có đại lượng được điều khiển, ví dụ phòng với nhiệt độ.",
        "<b>Phần tử đo lường (measurement element):</b> tạo tín hiệu liên quan đến trạng thái quá trình, "
        "ví dụ cảm biến nhiệt độ.",
    ]))
    b.append(fig(11, F.fig_1_11()))
    b.append(p(
        "<b>Đường phản hồi (feedback path):</b> tín hiệu liên quan đến trạng thái thực được đưa ngược "
        "lại để hiệu chỉnh đầu vào. Phản hồi âm (trừ đi) là cần thiết để điều khiển; phản hồi dương (cộng "
        "vào) gây mất ổn định. <b>Đường truyền thuận (forward path):</b> từ tín hiệu sai lệch đến đầu ra."))
    b.append(h3("1.3.3 Điều khiển theo sự kiện rời rạc", "Discrete event control"))
    b.append(p(
        "Còn gọi là điều khiển tuần tự: hành động được xác định theo các sự kiện có tính thời gian. Ví "
        "dụ đổ đầy bình nước: cảm biến đáy báo rỗng → bật van; cảm biến đỉnh báo đầy → tắt van. Đây là "
        "dạng vòng kín nhận phản hồi từ hai cảm biến (Hình 1.12)."))
    b.append(fig(12, F.fig_1_12()))

    # ---------------------------------------------------------- 1.4
    b.append(h2("1.4 Các phần tử đo lường", "Measurement elements"))
    b.append(p("Các cảm biến thường gặp trong hệ điều khiển:"))
    b.append(h3("1.4.1 Potentiometer (biến trở)", "Potentiometer"))
    b.append(p(
        "Gồm phần tử điện trở có con trượt. Với điện áp cấp không đổi V, điện áp ra V₀ giữa hai đầu tỉ "
        "lệ với tỉ số điện trở. Nếu dải điện trở đều, V₀ tỉ lệ với vị trí con trượt — đo được chuyển vị "
        "tuyến tính hoặc góc (Hình 1.13)."))
    b.append(fig(13, F.fig_1_13()))
    b.append(h3("1.4.2 Phần tử strain-gauge", "Strain-gauged element"))
    b.append(p(
        "Strain gauge là dải kim loại/màng bán dẫn dán lên bề mặt; khi bị kéo giãn, điện trở R thay đổi. "
        "ΔR/R tỉ lệ với biến dạng ε qua hệ số gauge factor G (kim loại ~2,0). Dán lên thanh công xôn để "
        "tạo cảm biến chuyển vị (Hình 1.14): khi uốn, gauge mặt trên chịu kéo (R tăng), mặt dưới chịu "
        "nén (R giảm)."))
    b.append(fig(14, F.fig_1_14()))
    b.append(h3("1.4.3 Máy biến áp vi phân từ tính tuyến tính (LVDT)", "Linear variable differential transformer"))
    b.append(p(
        "LVDT có một cuộn sơ cấp và hai cuộn thứ cấp mắc đối nhau. Lõi từ di chuyển theo chuyển vị cần "
        "đo. Khi lõi ở giữa, hai cuộn thứ cấp cảm ứng bằng nhau → hiệu số bằng 0. Khi lệch tâm, cuộn này "
        "cảm ứng mạnh hơn → có điện áp ra tỉ lệ với chuyển vị (Hình 1.15). Dải hoạt động khoảng ±2 mm "
        "đến ±400 mm."))
    b.append(fig(15, F.fig_1_15()))
    b.append(h3("1.4.4 Bộ mã hóa quang (optical encoders)", "Optical encoders"))
    b.append(p(
        "Bộ mã hóa cho đầu ra số theo chuyển vị góc hoặc tuyến tính. <b>Tăng dần (incremental):</b> đĩa "
        "có các khe, đếm xung để biết góc so với vị trí gốc (Hình 1.16). <b>Tuyệt đối (absolute):</b> "
        "đĩa có nhiều vành khe, mỗi góc cho một từ nhị phân riêng (Hình 1.17)."))
    b.append(fig(16, F.fig_1_16()))
    b.append(fig(17, F.fig_1_17()))
    b.append(h3("1.4.5 Công tắc", "Switches"))
    b.append(p("Công tắc cơ phát hiện sự có mặt của vật — ví dụ công tắc giới hạn (limit switch) đóng khi "
               "chi tiết chạm tới (Hình 1.18)."))
    b.append(fig(18, F.fig_1_18()))
    b.append(h3("1.4.6 Tachogenerator (máy phát tốc)", "Tachogenerator"))
    b.append(p(
        "Cuộn dây đặt trong từ trường; khi quay, cảm ứng suất điện động xoay chiều tỉ lệ với tốc độ góc "
        "(Hình 1.19). Dùng đo tốc độ trục động cơ."))
    b.append(fig(19, F.fig_1_19()))
    b.append(h3("1.4.7 Cảm biến áp suất", "Pressure sensors"))
    b.append(p(
        "Màng (diaphragm) biến dạng do chênh áp (Hình 1.20). Chuyển vị màng đo bằng strain gauge (Hình "
        "1.21) hoặc tinh thể áp điện (piezo-electric, Hình 1.22) — tinh thể nén sinh điện tích nhưng "
        "bị rò, nên không đo được áp tĩnh."))
    b.append(fig(20, F.fig_1_20()))
    b.append(fig(21, F.fig_1_21()))
    b.append(fig(22, F.fig_1_22()))
    b.append(h3("1.4.8 Lưu lượng chất lỏng", "Fluid flow"))
    b.append(p(
        "Theo phương trình Bernoulli, chênh áp qua vật cản tỉ lệ căn bậc hai của lưu lượng. Ống Venturi "
        "(Hình 1.23) và đĩa lỗ (orifice plate, Hình 1.24) đo chênh áp để suy lưu lượng. Lưu lượng kế "
        "tuabin (Hình 1.25): rotor quay tỉ lệ lưu lượng, nam châm nhỏ sinh xung đếm được."))
    b.append(fig(23, F.fig_1_23()))
    b.append(fig(24, F.fig_1_24()))
    b.append(fig(25, F.fig_1_25()))
    b.append(h3("1.4.9 Mức chất lỏng", "Liquid level"))
    b.append(p(
        "Phao có vị trí tỉ lệ mức chất lỏng; nối với con trượt potentiometer để cho điện áp ra liên quan "
        "đến mức (Hình 1.26)."))
    b.append(fig(26, F.fig_1_26()))
    b.append(h3("1.4.10 Cảm biến nhiệt độ", "Temperature sensors"))
    b.append(p(
        "Nhiều tính chất thay đổi theo nhiệt độ: nở vật liệu, điện trở, suất điện động nhiệt điện, dòng "
        "qua tiếp giáp bán dẫn. Dải kép kim loại (bimetallic, Hình 1.27) uốn cong khi nóng. Thermistor "
        "(Hình 1.28, 1.29) giảm điện trở phi tuyến khi nóng — nhỏ, đáp ứng nhanh nhưng phi tuyến. "
        "Cặp nhiệt điện (thermocouple, Hình 1.30): hai kim loại khác nhau tại hai mối nối lệch nhiệt tạo "
        "suất điện động (Hình 1.31); mạch bù mối nối lạnh (Hình 1.32). IC LM35 cho đầu ra tuyến tính "
        "10 mV/°C (Hình 1.33)."))
    b.append(fig(27, F.fig_1_27()))
    b.append(fig(28, F.fig_1_28()))
    b.append(fig(29, F.fig_1_29()))
    b.append(fig(30, F.fig_1_30()))
    b.append(fig(31, F.fig_1_31()))
    b.append(fig(32, F.fig_1_32()))
    b.append(fig(33, F.fig_1_33()))

    # ---------------------------------------------------------- 1.5
    b.append(h2("1.5 Xử lý tín hiệu", "Signal processing"))
    b.append(p(
        "Tín hiệu từ cảm biến hay bộ điều khiển có thể cần xử lý để phù hợp với khâu tiếp theo: khuếch "
        "đại, đổi tương tự↔số, đổi trở→áp, đổi áp→dòng, v.v. Ví dụ sức điện động cặp nhiệt điện chỉ vài "
        "mV cần khuếch đại và bù mối nối lạnh."))
    b.append(h3("1.5.1 Đổi trở sang áp", "Resistance to voltage converter"))
    b.append(p(
        "Mạch phân áp (Hình 1.34): thermistor mắc nối tiếp điện trở R, điện áp ra trên R tỉ lệ với tỉ "
        "số điện trở. Viết V_out = V·R/(R+R_t). Cầu Wheatstone cũng là bộ đổi trở→áp."))
    b.append(fig(34, F.fig_1_34()))
    b.append(h3("1.5.2 Bảo vệ", "Protection"))
    b.append(p(
        "Điện trở nối tiếp hạn dòng và cầu chì ngắt khi quá dòng (Hình 1.35). Bộ cách ly quang "
        "(optoisolator, Hình 1.36) dùng LED hồng ngoại và phototransistor để cách ly hoàn toàn hai "
        "mạch."))
    b.append(fig(35, F.fig_1_35()))
    b.append(fig(36, F.fig_1_36()))
    b.append(h3("1.5.3 Đổi tương tự sang số (ADC)", "Analogue to digital conversion"))
    b.append(p(
        "Tín hiệu tương tự (Hình 1.37(a)) biến liên tục; tín hiệu số (Hình 1.37(b)) nhảy từng bậc. Vi "
        "xử lý cần đầu vào số, nên phải qua ADC. Quá trình: lấy mẫu (Hình 1.38(a)), xung đồng hồ "
        "(1.38(b)), mẫu rời rạc (1.38(c)), giữ mẫu (1.38(d)), rồi đổi thành từ số (Hình 1.39). Với ADC 3 "
        "bit, 8 từ mã hóa điện áp thành 8 mức (Hình 1.40); độ phân giải = V_FS/2ⁿ."))
    b.append(fig(37, F.fig_1_37()))
    b.append(fig(38, F.fig_1_38()))
    b.append(fig(39, F.fig_1_39()))
    b.append(fig(40, F.fig_1_40()))
    b.append(h3("1.5.4 Đổi số sang tương tự (DAC)", "Digital to analogue conversion"))
    b.append(p(
        "Đầu ra vi xử lý là số, phần lớn phần tử hiệu chỉnh cần tương tự. DAC nhận từ nhị phân, cho giá "
        "trị tương tự tương đương (Hình 1.41); ví dụ 7 V full-scale: 000→0 V, 111→7 V."))
    b.append(fig(41, F.fig_1_41()))
    b.append(h3("1.5.5 Bộ khuếch đại thuật toán", "Amplifiers"))
    b.append(p(
        "Op-amp là nền tảng xử lý tín hiệu, có hai đầu vào (đảo −, không đảo +), hệ số khuếch đại rất "
        "lớn (~100 000). Hình 1.42 là chân 741. Bộ khuếch đại đảo (Hình 1.43): V_out/V_in = −R₂/R₁ "
        "(điểm ảo virtual earth). Bộ khuếch đại vi sai (Hình 1.44) khuếch đại hiệu hai áp vào."))
    b.append(fig(42, F.fig_1_42()))
    b.append(fig(43, F.fig_1_43()))
    b.append(fig(44, F.fig_1_44()))

    # ---------------------------------------------------------- 1.6
    b.append(h2("1.6 Các phần tử hiệu chỉnh", "Correction elements"))
    b.append(h3("1.6.1 Van điều hướng", "Directional control valves"))
    b.append(p(
        "Van đổi hướng hoặc dừng/dẫn dòng chất lỏng khi nhận tín hiệu ngoài. Ký hiệu cơ bản là hình "
        "vuông; mỗi vuông là một vị trí. Hình 1.45(a) hai vị trí, (b) ba vị trí. Đường trong ô chỉ "
        "đường chảy (mũi tên) và đóng (gạch); cổng vẽ ở vị trí nghỉ (Hình 1.46). Van được mô tả bởi số "
        "cổng/số vị trí: 2/2, 3/2, 4/2, 5/3 (Hình 1.47). Cách tác động: nút bấm, cần gạt, đòn bẩy, lò "
        "xo, bàn đạp, con lăn, solenoid, khí nén (Hình 1.48). Hình 1.49: van 3/2 solenoid + lò xo hoàn "
        "vị."))
    b.append(fig(45, F.fig_1_45()))
    b.append(fig(46, F.fig_1_46()))
    b.append(fig(47, F.fig_1_47()))
    b.append(fig(48, F.fig_1_48()))
    b.append(fig(49, F.fig_1_49()))
    b.append(p("Hình 1.50, 1.51 minh họa điều khiển xi lanh tác động đơn và tác động kép bằng van solenoid."))
    b.append(fig(50, F.fig_1_50()))
    b.append(fig(51, F.fig_1_51()))
    b.append(h3("1.6.2 Van điều khiển lưu lượng", "Flow control valves"))
    b.append(p(
        "Van dùng màng tác động bằng khí nén dịch chuyển côn (plug) trong đường chảy để đổi tiết diện "
        "(Hình 1.52, 1.53). Dạng côn quyết định đặc tuyến: tuyến tính, phần trăm đều, mở nhanh (Hình "
        "1.54, 1.55)."))
    b.append(fig(52, F.fig_1_52()))
    b.append(fig(53, F.fig_1_53()))
    b.append(fig(54, F.fig_1_54()))
    b.append(fig(55, F.fig_1_55()))
    b.append(h3("1.6.3 Động cơ DC", "D.c. motors"))
    b.append(p(
        "Động cơ DC dùng nhiều trong điều khiển. Phân loại theo đấu nối: nối tiếp (series, mô-men khởi "
        "động lớn, Hình 1.56(a)), song song (shunt, tốc độ gần không đổi, 1.56(b)), hỗn hợp (compound, "
        "1.56(c)), kích từ riêng (separately excited, 1.56(d)). Đặc tuyến mô-men/tốc độ (Hình 1.57)."))
    b.append(fig(56, F.fig_1_56()))
    b.append(fig(57, F.fig_1_57()))
    b.append(h3("1.6.4 Động cơ bước (stepper)", "Stepper motor"))
    b.append(p(
        "Động cơ bước quay từng góc bằng nhau ứng với mỗi xung số — định vị góc/ vị trí chính xác. Loại "
        "nam châm vĩnh cửu (Hình 1.58, bước 90°) và tựa từ biến thiên (variable reluctance, Hình 1.59). "
        "Mạch điều khiển SAA1027 (Hình 1.60) cấp xung tuần tự cho cuộn stator."))
    b.append(fig(58, F.fig_1_58()))
    b.append(fig(59, F.fig_1_59()))
    b.append(fig(60, F.fig_1_60()))

    # ---------------------------------------------------------- 1.7
    b.append(h2("1.7 Hệ thống điều khiển", "Control systems"))
    b.append(p(
        "Các ví dụ sau minh họa hệ vòng kín — dù hình thức khác nhau, chúng đều có cùng các phần tử cấu "
        "trúc cơ bản."))
    b.append(h3("1.7.1 Điều khiển tốc độ trục động cơ", "Control of the speed of rotation of a motor shaft"))
    b.append(p(
        "Potentiometer đặt giá trị tốc độ yêu cầu; op-amp vi sai so sánh với phản hồi từ tachogenerator, "
        "hiệu chỉnh động cơ qua bánh răng (Hình 1.61, 1.62)."))
    b.append(fig(61, F.fig_1_61()))
    b.append(fig(62, F.fig_1_62()))
    b.append(h3("1.7.2 Điều khiển vị trí dụng cụ", "Control of the position of a tool"))
    b.append(p(
        "Động cơ bước qua dây đai dịch chuyển dụng cụ; potentiometer đo vị trí phản hồi về bộ điều khiển "
        "(vi xử lý + ADC) (Hình 1.63, 1.64)."))
    b.append(fig(63, F.fig_1_63()))
    b.append(fig(64, F.fig_1_64()))
    b.append(h3("1.7.3 Trợ lái", "Power steering"))
    b.append(p(
        "Khi mô-men vượt ngưỡng, hệ tác động để bánh lái theo góc quay vô lăng; phản hồi cơ khí từ vị "
        "trí bánh xe qua van thủy lực (Hình 1.65)."))
    b.append(fig(65, F.fig_1_65()))
    b.append(h3("1.7.4 Điều khiển áp suất nhiên liệu", "Control of fuel pressure"))
    b.append(p(
        "Hệ quản lý động cơ giữ áp suất nhiên liệu không đổi cấp cho vòi phun nhờ van điều áp màng + "
        "bi (Hình 1.66, 1.67). Lò xo đặt giá trị; màng vừa so sánh vừa đo."))
    b.append(fig(66, F.fig_1_66()))
    b.append(fig(67, F.fig_1_67()))
    b.append(h3("1.7.5 Phanh chống bó cứng (ABS)", "Antilock brakes"))
    b.append(p(
        "ABS điều chỉnh áp suất phanh để bánh không bị khóa: cảm biến tốc độ bánh phản hồi, bộ điều "
        "khiển so sánh với dữ liệu nhớ, tác động van modulator (Hình 1.68)."))
    b.append(fig(68, F.fig_1_68()))
    b.append(h3("1.7.6 Điều khiển độ dày", "Thickness control"))
    b.append(p(
        "LVDT đo sai lệch độ dày tấm; tín hiệu lỗi qua bộ đổi AC→DC, khuếch đại, điều khiển động cơ DC "
        "chỉnh vị trí rulo trên (Hình 1.69, 1.70)."))
    b.append(fig(69, F.fig_1_69()))
    b.append(fig(70, F.fig_1_70()))
    b.append(h3("1.7.7 Điều khiển mức chất lỏng", "Control of liquid level"))
    b.append(p(
        "Bộ điều khiển khí nén vận hành bằng phao: mức thay đổi → phao dịch → áp khí đổi → van điều "
        "khiển lưu lượng vào (Hình 1.71, 1.72)."))
    b.append(fig(71, F.fig_1_71()))
    b.append(fig(72, F.fig_1_72()))
    b.append(h3("1.7.8 Cơ cấu kẹp robot", "Robot gripper"))
    b.append(p(
        "Cơ cấu kẹp có các ngón gập để giữ vật (Hình 1.73). Cần phản hồi lực tiếp xúc để giữ vừa đủ — "
        "hệ vòng kín (Hình 1.74) dùng cảm biến piezoelectric hoặc strain gauge."))
    b.append(fig(73, F.fig_1_73()))
    b.append(fig(74, F.fig_1_74()))
    b.append(h3("1.7.9 Điều khiển máy công cụ", "Machine tool control"))
    b.append(p(
        "Điều khiển vị trí dụng cụ/chi tiết và thao tác cắt. Bộ nhớ cung cấp chương trình, vòng kín "
        "giám sát liên tục vị trí bàn máy (Hình 1.75)."))
    b.append(fig(75, F.fig_1_75()))
    b.append(h3("1.7.10 Máy khoan tự động", "An automatic drill"))
    b.append(p(
        "Công tắc cảm biến phát hiện chi tiết trên bàn → bộ điều khiển hạ mũi khoan; khi khoan hết "
        "hành trình, công tắc khác đảo chiều rút mũi (Hình 1.76). Đây là điều khiển theo sự kiện rời "
        "rạc vòng kín."))
    b.append(fig(76, F.fig_1_76()))
    b.append(h3("1.7.11 Hệ điều khiển dùng vi xử lý", "Microprocessor-controlled systems"))
    b.append(p(
        "Nhiều sản phẩm tiêu dùng dùng bộ điều khiển vi xử lý: so sánh đầu vào cảm biến với giá trị yêu "
        "cầu theo luật điều khiển trong bộ nhớ, xuất tín hiệu cho phần tử hiệu chỉnh (Hình 1.77)."))
    b.append(fig(77, F.fig_1_77()))
    b.append(p(
        "<i>Bài tập cuối chương (Problems) gồm các câu 1–12 trên bản gốc: xác định vào/ra của các hệ "
        "thống, so sánh vòng hở/vòng kín, vẽ sơ đồ khối hệ sưởi, nhận diện phần tử chức năng, đề xuất "
        "cảm biến, và giải thích van bi điều khiển mức nước trong bể.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter gives a non-mathematical overview of control systems: the concept of a system "
        "and its block-diagram representation, how block diagrams describe open- and closed-loop "
        "systems, examples of the measurement, signal-processing and correction elements used, and "
        "finally the common structural pattern shared by a wide range of real control systems."))
    b.append(h2("1.1 Introduction", "Giới thiệu"))
    b.append(p(
        "Automation describes the automatic operation or control of a process. Modern manufacturing "
        "uses automation increasingly — robotic production lines producing components with virtually no "
        "human intervention — and it is spreading into domestic and office appliances. Automation "
        "carries out operations in the required sequence and controls outputs to required values."))
    b.append(p("Key historical points in the development of automation:"))
    b.append(ul([
        "Modern manufacturing began in 18th-century England with water wheels and steam engines.",
        "Powered machinery in the early 1900s improved component accuracy, allowing identical batches.",
        "Henry Ford developed the production line in 1909.",
        "1920s: theoretical principles of feedback control; automatic steering of ships and aircraft.",
        "1940s (WWII): radar tracking and gun control; Bode's 1945 paper on network analysis and "
        "feedback-amplifier design.",
        "1952: numerical control (NC) positioned tools from punched-tape instructions (open-loop).",
        "1948: the transistor → integrated circuits → 1970s microprocessors, making control cheap and "
        "widespread (washing machines, auto-focus cameras).",
    ]))
    b.append(p(
        "This book introduces the basic ideas of designing control systems; this chapter introduces the "
        "basic idea of a control system and the elements used."))
    b.append(h2("1.2 Systems", "Hệ thống"))
    b.append(p(
        "A car gear box can be viewed as a system with an input and output shaft (Figure 1.1(a)); an "
        "amplifier is a system with an input signal and a related output signal (Figure 1.1(b)). Thus a "
        "system is like a closed box: we apply inputs and obtain outputs, the output being related to "
        "the input."))
    b.append(fig(1, F.fig_1_1()))
    b.append(p(
        "A system is an arrangement of parts within a boundary that provides an output from specified "
        "inputs (Figure 1.1(c)). The boundary separates the system from the environment; signals cross "
        "it as inputs and outputs. Engineers care more about inputs and outputs than internal detail."))
    b.append(p(
        "In control we model a physical system as blocks with inputs, outputs and a mathematical "
        "relationship (Figures 1.2, 1.3). An operational amplifier is used by its known input–output "
        "relation without knowing its internals."))
    b.append(fig(2, F.fig_1_2()))
    b.append(fig(3, F.fig_1_3()))
    b.append(h3("1.2.1 Block diagrams", "Sơ đồ khối"))
    b.append(p(
        "A block diagram shows a system element as a box with an input arrow and an output arrow "
        "(Figure 1.4(a)). Elements connect in series (1.4(b)). A summing junction adds/subtracts "
        "signals, marked + or − (1.4(c)). A take-off point taps a signal (1.4(d)). Figure 1.5 shows a "
        "central-heating system with negative feedback."))
    b.append(fig(4, F.fig_1_4()))
    b.append(fig(5, F.fig_1_5()))
    b.append(h2("1.3 Control systems models", "Mô hình hệ thống điều khiển"))
    b.append(p("There are two basic types (Figures 1.6, 1.7):"))
    b.append(h3("Open-loop", "Vòng hở"))
    b.append(p(
        "The output has no effect on the input. Advantages: simple, cheap, reliable. Disadvantage: no "
        "correction for disturbances. An electric fire selected at 1 kW or 2 kW holds a temperature "
        "set once and makes no further adjustment (Figure 1.6); opening a window is not compensated. "
        "Used for sequencing operations such as washing machines."))
    b.append(fig(6, F.fig_1_6()))
    b.append(h3("Closed-loop", "Vòng kín"))
    b.append(p(
        "A signal indicating the output state is fed back, compared with the required value, and used to "
        "modify the output to maintain it (Figure 1.7). Advantages: accurate; disadvantages: more "
        "complex, costlier, more failure-prone. A person with a thermometer adjusting the fire is a "
        "closed loop with negative feedback (Figure 1.8): the feedback is subtracted from the set value."))
    b.append(fig(7, F.fig_1_7()))
    b.append(fig(8, F.fig_1_8()))
    b.append(h3("1.3.1 Basic elements of an open-loop control system", "Các phần tử cơ bản của hệ vòng hở"))
    b.append(p("Three basic elements (Figure 1.9): control, correction and process. No correction is made for disturbances."))
    b.append(fig(9, F.fig_1_9()))
    b.append(h3("1.3.2 Basic elements of a closed-loop system", "Các phần tử cơ bản của hệ vòng kín"))
    b.append(p("Figure 1.10 shows the general form. Forward-path elements are comparison, control law, correction and process."))
    b.append(fig(10, F.fig_1_10()))
    b.append(p("Functions:"))
    b.append(ul([
        "<b>Comparison element</b>: compares the required value with the measured value to give the "
        "error signal: error = reference − measured actual value.",
        "<b>Control-law element</b>: decides the action for an error — on/off, proportional, integral, "
        "derivative. A differential amplifier combines comparison and control law.",
        "<b>Correction element</b> (final control element): changes the process; the actuator supplies "
        "the power — e.g. a motor or cylinder (Figure 1.11).",
        "<b>Process</b>: the system whose variable is controlled.",
        "<b>Measurement element</b>: produces a signal related to the controlled variable, e.g. a "
        "temperature sensor.",
    ]))
    b.append(fig(11, F.fig_1_11()))
    b.append(p(
        "<b>Feedback path</b>: a signal related to the actual condition is fed back to modify the input. "
        "Negative feedback (subtracted) is required for control; positive feedback adds to the input. "
        "<b>Forward path</b>: from the error signal to the output."))
    b.append(h3("1.3.3 Discrete event control", "Điều khiển theo sự kiện rời rạc"))
    b.append(p(
        "Sequential control: actions determined by observed time-critical events. Filling a container: "
        "an empty sensor switches the flow on, a full sensor switches it off — a closed loop receiving "
        "feedback from two sensors (Figure 1.12)."))
    b.append(fig(12, F.fig_1_12()))
    b.append(h2("1.4 Measurement elements", "Các phần tử đo lường"))
    b.append(p("Common sensors in control-system measurement:"))
    b.append(h3("1.4.1 Potentiometer", "Potentiometer"))
    b.append(p(
        "A resistance element with a sliding contact. With constant supply voltage V, the output V₀ is "
        "a fraction of the input, depending on the ratio of resistances. If resistance is uniform, V₀ is "
        "proportional to slider displacement — measuring linear or angular position (Figure 1.13)."))
    b.append(fig(13, F.fig_1_13()))
    b.append(h3("1.4.2 Strain-gauged element", "Phần tử strain-gauge"))
    b.append(p(
        "A strain gauge is a wire/foil/semiconductor strip whose resistance R changes when stretched: "
        "ΔR/R = G·ε, where G (gauge factor) is about 2.0 for metal gauges. Mounted on a cantilever it "
        "becomes a displacement sensor (Figure 1.14): bending stretches the upper gauge (R up) and "
        "compresses the lower (R down)."))
    b.append(fig(14, F.fig_1_14()))
    b.append(h3("1.4.3 Linear variable differential transformer (LVDT)", "Máy biến áp vi phân từ tính tuyến tính"))
    b.append(p(
        "An LVDT has a primary and two series-opposed secondary coils. With the magnetic core central, "
        "the induced e.m.f.s cancel (zero output). Displacing the core makes one coil dominate, giving "
        "an output proportional to displacement (Figure 1.15). Ranges about ±2 mm to ±400 mm."))
    b.append(fig(15, F.fig_1_15()))
    b.append(h3("1.4.4 Optical encoders", "Bộ mã hóa quang"))
    b.append(p(
        "Encoders give a digital output from angular/linear displacement. <b>Incremental</b> encoders "
        "count pulses from a slotted disc (Figure 1.16). <b>Absolute</b> encoders output a binary word "
        "for each position (Figure 1.17)."))
    b.append(fig(16, F.fig_1_16()))
    b.append(fig(17, F.fig_1_17()))
    b.append(h3("1.4.5 Switches", "Công tắc"))
    b.append(p("A mechanical switch detects the presence of an object — e.g. a limit switch closed when "
               "a workpiece arrives (Figure 1.18)."))
    b.append(fig(18, F.fig_1_18()))
    b.append(h3("1.4.6 Tachogenerator", "Máy phát tốc"))
    b.append(p("A coil in a magnetic field induces an alternating e.m.f. proportional to angular speed "
               "when rotated (Figure 1.19). Used to measure shaft speed."))
    b.append(fig(19, F.fig_1_19()))
    b.append(h3("1.4.7 Pressure sensors", "Cảm biến áp suất"))
    b.append(p(
        "A diaphragm deflects under a pressure difference (Figure 1.20). Its movement is monitored with "
        "strain gauges (Figure 1.21) or a piezo-electric crystal (Figure 1.22) — the crystal generates "
        "charge on compression but leaks, so it is not for static pressure."))
    b.append(fig(20, F.fig_1_20()))
    b.append(fig(21, F.fig_1_21()))
    b.append(fig(22, F.fig_1_22()))
    b.append(h3("1.4.8 Fluid flow", "Lưu lượng chất lỏng"))
    b.append(p(
        "By Bernoulli's equation, the pressure drop across a restriction is proportional to the square "
        "root of flow rate. The Venturi tube (Figure 1.23) and orifice plate (Figure 1.24) measure the "
        "pressure difference to infer flow. A turbine flowmeter (Figure 1.25) has a rotor whose speed is "
        "roughly proportional to flow; a magnet gives countable pulses."))
    b.append(fig(23, F.fig_1_23()))
    b.append(fig(24, F.fig_1_24()))
    b.append(fig(25, F.fig_1_25()))
    b.append(h3("1.4.9 Liquid level", "Mức chất lỏng"))
    b.append(p("A float's position is directly related to liquid level; linked to a potentiometer slider "
               "it gives a level-related voltage (Figure 1.26)."))
    b.append(fig(26, F.fig_1_26()))
    b.append(h3("1.4.10 Temperature sensors", "Cảm biến nhiệt độ"))
    b.append(p(
        "Many properties change with temperature: expansion, resistance, thermoelectric e.m.f., and "
        "current across semiconductor junctions. The bimetallic strip bends when heated (Figure 1.27). "
        "Thermistors decrease resistance non-linearly when hot (Figures 1.28, 1.29) — small and fast "
        "but non-linear. Thermocouples (Figure 1.30) give an e.m.f. between two junctions at different "
        "temperatures (Figure 1.31); a cold-junction compensation circuit (Figure 1.32) emulates 0 °C. "
        "The LM35 IC gives a linear 10 mV/°C output (Figure 1.33)."))
    b.append(fig(27, F.fig_1_27()))
    b.append(fig(28, F.fig_1_28()))
    b.append(fig(29, F.fig_1_29()))
    b.append(fig(30, F.fig_1_30()))
    b.append(fig(31, F.fig_1_31()))
    b.append(fig(32, F.fig_1_32()))
    b.append(fig(33, F.fig_1_33()))
    b.append(h2("1.5 Signal processing", "Xử lý tín hiệu"))
    b.append(p(
        "The sensor or controller signal may need processing to suit the next element: amplification, "
        "analogue↔digital conversion, resistance→voltage, voltage→current, pressure→current, etc. For "
        "example, a thermocouple output of a few mV needs amplification and cold-junction compensation."))
    b.append(h3("1.5.1 Resistance to voltage converter", "Đổi trở sang áp"))
    b.append(p(
        "A potential divider (Figure 1.34) with a thermistor and series resistor R gives an output "
        "across R: V_out = V·R/(R+R_t). The Wheatstone bridge is another example."))
    b.append(fig(34, F.fig_1_34()))
    b.append(h3("1.5.2 Protection", "Bảo vệ"))
    b.append(p(
        "A series resistor limits current and a fuse breaks the circuit on over-current (Figure 1.35). "
        "An optoisolator (Figure 1.36) uses an LED and phototransistor to fully isolate two circuits."))
    b.append(fig(35, F.fig_1_35()))
    b.append(fig(36, F.fig_1_36()))
    b.append(h3("1.5.3 Analogue to digital conversion (ADC)", "Đổi tương tự sang số"))
    b.append(p(
        "An analogue signal (Figure 1.37(a)) varies continuously; a digital signal (1.37(b)) is in "
        "steps. Microprocessors need digital inputs, so an ADC is used. Stages: sampling (1.38(a)), a "
        "clock (1.38(b)), sampled pulses (1.38(c)), held samples (1.38(d)), then digital words "
        "(1.39). A 3-bit ADC divides the range into 8 levels (Figure 1.40); resolution = V_FS/2ⁿ."))
    b.append(fig(37, F.fig_1_37()))
    b.append(fig(38, F.fig_1_38()))
    b.append(fig(39, F.fig_1_39()))
    b.append(fig(40, F.fig_1_40()))
    b.append(h3("1.5.4 Digital to analogue conversion (DAC)", "Đổi số sang tương tự"))
    b.append(p(
        "Microprocessor output is digital but most elements need analogue. A DAC takes a binary word "
        "and gives the equivalent analogue value (Figure 1.41); e.g. 7 V full-scale: 000→0 V, 111→7 V."))
    b.append(fig(41, F.fig_1_41()))
    b.append(h3("1.5.5 Amplifiers", "Bộ khuếch đại"))
    b.append(p(
        "The op-amp has inverting (−) and non-inverting (+) inputs and very high gain (~100 000). "
        "Figure 1.42 is the 741 pinout. The inverting amplifier (Figure 1.43): V_out/V_in = −R₂/R₁ "
        "(virtual earth). The differential amplifier (Figure 1.44) amplifies the difference of two "
        "inputs."))
    b.append(fig(42, F.fig_1_42()))
    b.append(fig(43, F.fig_1_43()))
    b.append(fig(44, F.fig_1_44()))
    b.append(h2("1.6 Correction elements", "Các phần tử hiệu chỉnh"))
    b.append(h3("1.6.1 Directional control valves", "Van điều hướng"))
    b.append(p(
        "A directional valve changes, stops or starts flow on an external signal. Each square is a "
        "position (Figure 1.45(a) two-position, (b) three-position). Flow paths (arrows) and shut-offs "
        "(terminated lines) are drawn inside; ports are outside at the rest position (Figure 1.46). "
        "Valves are described by ports/positions: 2/2, 3/2, 4/2, 5/3 (Figure 1.47). Actuation methods "
        "include push-button, lever, spring, pedal, roller, solenoid, pneumatic (Figure 1.48). Figure "
        "1.49 shows a 3/2 solenoid valve with return spring."))
    b.append(fig(45, F.fig_1_45()))
    b.append(fig(46, F.fig_1_46()))
    b.append(fig(47, F.fig_1_47()))
    b.append(fig(48, F.fig_1_48()))
    b.append(fig(49, F.fig_1_49()))
    b.append(p("Figures 1.50 and 1.51 show single- and double-acting cylinder control with solenoid valves."))
    b.append(fig(50, F.fig_1_50()))
    b.append(fig(51, F.fig_1_51()))
    b.append(h3("1.6.2 Flow control valves", "Van điều khiển lưu lượng"))
    b.append(p(
        "A pneumatically actuated stem moves a plug in the flow path to change the gap (Figures 1.52, "
        "1.53). Plug shape sets the characteristic: linear, equal-percentage, quick-opening (Figures "
        "1.54, 1.55)."))
    b.append(fig(52, F.fig_1_52()))
    b.append(fig(53, F.fig_1_53()))
    b.append(fig(54, F.fig_1_54()))
    b.append(fig(55, F.fig_1_55()))
    b.append(h3("1.6.3 D.c. motors", "Động cơ DC"))
    b.append(p(
        "DC motors are widely used. Classified by winding connection: series (Figure 1.56(a), high "
        "starting torque), shunt (1.56(b), nearly constant speed), compound (1.56(c)), separately "
        "excited (1.56(d)). Torque–speed characteristics in Figure 1.57."))
    b.append(fig(56, F.fig_1_56()))
    b.append(fig(57, F.fig_1_57()))
    b.append(h3("1.6.4 Stepper motor", "Động cơ bước"))
    b.append(p(
        "A stepper rotates in equal steps per input pulse — accurate positioning. Permanent-magnet "
        "(Figure 1.58, 90° steps) and variable-reluctance (Figure 1.59) types. The SAA1027 driver "
        "(Figure 1.60) sequences the stator coils."))
    b.append(fig(58, F.fig_1_58()))
    b.append(fig(59, F.fig_1_59()))
    b.append(fig(60, F.fig_1_60()))
    b.append(h2("1.7 Control systems", "Hệ thống điều khiển"))
    b.append(p(
        "The following examples illustrate closed-loop systems; despite different forms, they share the "
        "same basic structural elements."))
    b.append(h3("1.7.1 Control of the speed of rotation of a motor shaft", "Điều khiển tốc độ trục động cơ"))
    b.append(p(
        "A potentiometer sets the required speed; a differential amplifier compares it with feedback "
        "from a tachogenerator and adjusts the motor via bevel gears (Figures 1.61, 1.62)."))
    b.append(fig(61, F.fig_1_61()))
    b.append(fig(62, F.fig_1_62()))
    b.append(h3("1.7.2 Control of the position of a tool", "Điều khiển vị trí dụng cụ"))
    b.append(p(
        "A stepper motor drives a belt to position a tool; a potentiometer measures position and feeds "
        "back to the microprocessor controller (ADC) (Figures 1.63, 1.64)."))
    b.append(fig(63, F.fig_1_63()))
    b.append(fig(64, F.fig_1_64()))
    b.append(h3("1.7.3 Power steering", "Trợ lái"))
    b.append(p(
        "When steering resistance exceeds a threshold, the system makes the wheels follow the steering "
        "wheel; feedback is mechanical from wheel position via a hydraulic valve (Figure 1.65)."))
    b.append(fig(65, F.fig_1_65()))
    b.append(h3("1.7.4 Control of fuel pressure", "Điều khiển áp suất nhiên liệu"))
    b.append(p(
        "Engine management holds fuel pressure constant at the injectors via a diaphragm-and-ball "
        "regulator valve (Figures 1.66, 1.67). The spring sets the value; the diaphragm both compares "
        "and measures."))
    b.append(fig(66, F.fig_1_66()))
    b.append(fig(67, F.fig_1_67()))
    b.append(h3("1.7.5 Antilock brakes", "Phanh chống bó cứng"))
    b.append(p(
        "ABS adjusts brake pressure so wheels do not lock: a wheel-speed sensor feeds back, the "
        "controller compares with stored data and operates the modulator valves (Figure 1.68)."))
    b.append(fig(68, F.fig_1_68()))
    b.append(h3("1.7.6 Thickness control", "Điều khiển độ dày"))
    b.append(p(
        "An LVDT measures sheet-thickness error; the AC error is converted to DC, amplified and used "
        "to vary a DC motor's armature current, gearing down to move the upper roll (Figures 1.69, "
        "1.70)."))
    b.append(fig(69, F.fig_1_69()))
    b.append(fig(70, F.fig_1_70()))
    b.append(h3("1.7.7 Control of liquid level", "Điều khiển mức chất lỏng"))
    b.append(p(
        "A float-operated pneumatic controller: level change moves the float, changing air pressure "
        "that adjusts the inflow valve (Figures 1.71, 1.72)."))
    b.append(fig(71, F.fig_1_71()))
    b.append(fig(72, F.fig_1_72()))
    b.append(h3("1.7.8 Robot gripper", "Cơ cấu kẹp robot"))
    b.append(p(
        "A gripper has fingers that pivot to clamp an object (Figure 1.73). Feedback of contact force "
        "is needed to grip with just enough force — a closed-loop system (Figure 1.74) using "
        "piezoelectric or strain-gauge sensors."))
    b.append(fig(73, F.fig_1_73()))
    b.append(fig(74, F.fig_1_74()))
    b.append(h3("1.7.9 Machine tool control", "Điều khiển máy công cụ"))
    b.append(p(
        "Machine-tool systems control tool/workpiece position and operation. Memory supplies a program "
        "of required positions; continuous monitoring closes the loop on the work-table position "
        "(Figure 1.75)."))
    b.append(fig(75, F.fig_1_75()))
    b.append(h3("1.7.10 An automatic drill", "Máy khoan tự động"))
    b.append(p(
        "A switch sensor detects the workpiece, the controller lowers and drives the drill; at full "
        "travel a second sensor reverses the motor (Figure 1.76). This is closed-loop discrete-event "
        "control."))
    b.append(fig(76, F.fig_1_76()))
    b.append(h3("1.7.11 Microprocessor-controlled systems", "Hệ điều khiển dùng vi xử lý"))
    b.append(p(
        "Many consumer products use a microprocessor controller: it compares the sensor input with the "
        "required value using a control law in memory and outputs to a correction element (Figure "
        "1.77)."))
    b.append(fig(77, F.fig_1_77()))
    b.append(p(
        "<i>The end-of-chapter Problems (1–12) ask the reader to identify inputs/outputs of systems, "
        "contrast open- and closed-loop control, draw a central-heating block diagram, identify "
        "functional elements, suggest sensors, and explain a ball-valve cistern level control.</i>"))
    return "".join(b)
