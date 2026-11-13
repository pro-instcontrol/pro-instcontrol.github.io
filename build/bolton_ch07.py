# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 7, Controllers.

Vietnamese and English prose with all 51 redrawn vector figures (7.1–7.51):
thermostats, electronic switches, PID modes and their responses, controller
block diagrams, Bode forms, tuning, PLC ladder logic and embedded systems.
"""
import boltonfig7 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 26
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Bộ điều khiển ba số tử (PID)</em> — tổ hợp đồng thời tỉ lệ (P), tích phân (I), đạo hàm (D). · "
            "<em>Điều khiển On/Off</em> — chỉ có hai mức bật/tắt; có dải chết (dead band). · "
            "<em>Offset / sai lệch xác lập</em> — sai lệch còn lại với điều khiển chỉ tỉ lệ. · "
            "<em>Dải tỉ lệ (proportional band)</em> — % độ lệch gây đổi đầu ra 100%. · "
            "<em>Hiệu chỉnh (tuning)</em> — chọn Kp, Ki, Kd (Ziegler–Nichols). · "
            "<em>PLC / hệ nhúng</em> — điều khiển số bằng thang (ladder) và vi xử lý.")
    return note(
        "<b>Key terms.</b> <em>Three-term (PID) controller</em> — simultaneous proportional, integral and "
        "derivative action. · <em>On-off control</em> — two-state switching with a dead band. · "
        "<em>Offset / steady-state error</em> — the residual error with proportional-only control. · "
        "<em>Proportional band</em> — the % deviation that produces a 100% change in output. · "
        "<em>Tuning</em> — selecting Kp, Ki, Kd (Ziegler–Nichols). · <em>PLC / embedded</em> — digital "
        "control by ladder logic and microprocessors.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này bàn về bộ điều khiển quá trình và các luật điều khiển, từ điều khiển On/Off đơn giản, "
        "qua bộ điều khiển ba số tử (PID) kinh điển, đến các hệ điều khiển số như PLC và hệ nhúng."))

    # 7.1
    b.append(h2("7.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Các bộ điều khiển quá trình về cơ bản có đầu vào là tín hiệu sai lệch — hiệu giữa tín hiệu giá trị "
        "yêu cầu và tín hiệu phản hồi — và đầu ra là tín hiệu để hiệu chỉnh đầu ra hệ thống. Dạng đơn giản "
        "nhất là thiết bị On/Off bật thiết bị hiệu chỉnh khi có sai lệch và tắt khi hết sai lệch. Tuy nhiên, "
        "phương pháp này có hạn chế, nên thường dùng bộ điều khiển tinh vi hơn. Một dạng điều khiển thỏa mãn "
        "rộng rãi là bộ điều khiển ba số tử hay PID. <b>Chế độ điều khiển (control mode)</b> là kiểu đáp ứng "
        "mà bộ điều khiển đưa ra với sai lệch; ba chế độ cơ bản là tỉ lệ (P), tích phân (I) và đạo hàm (D); "
        "bộ ba số tử là tổ hợp cả ba. Hình 7.1 là bộ cảm biến nhiệt dải kép kim loại (bimetallic) dùng trong "
        "điều khiển On/Off nhiệt độ đơn giản."))
    b.append(fig(1, F.fig_7_1()))
    b.append(h3("7.1.1 Bù và bộ điều khiển", "Compensation and controllers"))
    b.append(p(
        "Thuật ngữ <b>bù (compensation)</b> chỉ việc hiệu chỉnh đặc tính của hệ để đạt đặc tính yêu cầu; bộ "
        "bù là thành phần được thêm vào để sửa đặc tính vòng kín, có thể đặt ở bất kỳ đâu trong hệ. Bộ điều "
        "khiển có đầu vào là sai lệch, đầu ra là tín hiệu hiệu chỉnh, thường đặt tại một điểm cụ thể. Về thiết "
        "kế không có khác biệt thực sự giữa bộ bù và bộ điều khiển — truyền thống bộ điều khiển là linh kiện "
        "độc lập cung cấp các chế độ như tỉ lệ, tích phân, đạo hàm và thường gồm cả phần tử cộng."))

    # 7.2
    b.append(h2("7.2 Điều khiển On/Off", "On-off control"))
    b.append(p(
        "Với điều khiển On/Off, bộ điều khiển về bản chất là một công tắc được kích bởi sai lệch và chỉ đưa ra "
        "tín hiệu hiệu chỉnh bật/tắt. Ví dụ điển hình là bộ điều khiển nhiệt dải kép kim loại (Hình 7.1): khi "
        "nhiệt độ thực trên nhiệt độ yêu cầu thì dải kim loại ở vị trí tắt (heater off); khi dưới thì ở vị trí "
        "bật (heater on). Đầu ra bộ điều khiển chỉ là bật hoặc tắt (Hình 7.2)."))
    b.append(fig(2, F.fig_7_2()))
    b.append(p(
        "Do tác động không liên tục và có độ trễ, biến điều khiển dao động quanh giá trị yêu cầu. Với điều "
        "khiển nhiệt phòng, khi nhiệt độ rơi dưới mức yêu cầu thì mất một thời gian mới có tác dụng, và khi "
        "nhiệt độ đã đạt mức yêu cầu thì hệ vẫn tiếp tục nóng một lúc rồi mới nguội — kết quả là nhiệt độ "
        "dao động qua lại quanh giá trị yêu cầu (Hình 7.3). Một vấn đề khác: khi nhiệt độ lân cận giá trị đặt, "
        "bộ điều khiển có thể liên tục bật/tắt do nhiễu nhỏ. Điều này giảm bớt nếu bật ở nhiệt độ thấp hơn "
        "nhiệt độ tắt (Hình 7.4) — <b>dải chết (dead band)</b> là khoảng giữa hai mức đó. Dải chết lớn gây "
        "dao động lớn; dải chết nhỏ tăng tần số chuyển mạch."))
    b.append(fig(3, F.fig_7_3()))
    b.append(fig(4, F.fig_7_4()))

    # 7.2.1
    b.append(h3("7.2.1 Chuyển mạch điện tử", "Electronic switching"))
    b.append(p(
        "Chuyển mạch cơ học (dải kim loại, rơ-le) có tốc độ chậm; chuyển mạch nhanh hơn đạt được bằng mạch "
        "điện tử như thyristor hay transistor. <b>Thyristor</b> (SCR) có thể xem như diode chỉ dẫn dòng khi "
        "được kích ở một điện áp phân cực thuận nhất định. Hình 7.5 là thyristor mắc nối tiếp điện trở 30 Ω "
        "dưới nguồn 300 V; cổng (gate) điều khiển điện áp đánh thủng. Hình 7.6 minh họa dùng thyristor chóp "
        "điện áp một chiều để điều khiển công suất tới tải; Hình 7.7 là mạch a.c. cho đèn, mô-tơ hay điện "
        "trở nhiệt, trong đó biến trở R2 đặt mức kích và điốt bảo vệ cổng."))
    b.append(fig(5, F.fig_7_5()))
    b.append(fig(6, F.fig_7_6()))
    b.append(fig(7, F.fig_7_7()))
    b.append(p(
        "<b>Transistor</b> cũng dùng làm khóa điện tử (Hình 7.8): không có điện áp vào thì trở giữa collector–"
        "emitter cao, toàn bộ Vcc xuất hiện ở đầu ra; có điện áp vào đủ lớn thì trở thấp, Vout ≈ 0. Cặp "
        "<b>Darlington</b> (Hình 7.9) gồm hai transistor khuếch đại dòng base nhỏ thành dòng lớn, có diode bảo "
        "vệ. Tốc độ mô-tơ một chiều hở vòng có thể điều khiển bằng <b>điều chế độ rộng xung (PWM)</b> "
        "(Hình 7.10): khóa tắt/bật điện áp một chiều, phần trăm chu kỳ bật càng lớn thì trị trung bình càng "
        "gần điện áp vào. Hình 7.11 là mạch transistor thực hiện PWM, điốt cho dòng cảm ứng khi tắt. Mạch "
        "<b>H</b> bốn transistor (Hình 7.12) điều khiển cả hướng và tốc độ mô-tơ; Hình 7.13 là phiên bản dùng "
        "cổng logic cho điều khiển bằng vi xử lý. Hình 7.14 là hệ kín dùng vi xử lý: tachogenerator → ADC → "
        "vi xử lý → PWM → mô-tơ."))
    b.append(fig(8, F.fig_7_8()))
    b.append(fig(9, F.fig_7_9()))
    b.append(fig(10, F.fig_7_10()))
    b.append(fig(11, F.fig_7_11()))
    b.append(fig(12, F.fig_7_12()))
    b.append(fig(13, F.fig_7_13()))
    b.append(fig(14, F.fig_7_14()))

    # 7.3
    b.append(h2("7.3 Điều khiển PID", "PID control"))
    b.append(p(
        "Có ba chế độ điều khiển cơ bản. <b>Tỉ lệ (P):</b> đầu ra tỉ lệ với sai lệch e, tức đầu ra = Kp·e với "
        "Kp là hệ số tỉ lệ (Hình 7.15). <b>Đạo hàm (D):</b> đầu ra tỉ lệ với tốc độ đổi sai lệch de/dt, tức "
        "đầu ra = Kd·de/dt (Hình 7.16) — độ dốc của đồ thị sai lệch–thời gian. <b>Tích phân (I):</b> đầu ra "
        "tỉ lệ với tích phân sai lệch theo thời gian, tức diện tích dưới đồ thị sai lệch–thời gian, nên vẫn "
        "có giá trị ngay cả khi sai lệch đã về 0 (Hình 7.17)."))
    b.append(fig(15, F.fig_7_15()))
    b.append(fig(16, F.fig_7_16()))
    b.append(fig(17, F.fig_7_17()))

    # 7.4
    b.append(h2("7.4 Thuật ngữ", "Terminology"))
    b.append(p(
        "Các thuật ngữ mô tả bộ điều khiển: <b>giá trị đặt (set-point)</b> là tín hiệu đại diện đầu ra yêu "
        "cầu; <b>miền (range)</b> là hai giá trị cực biên hệ hoạt động (vd 0°–30°); <b>biên độ (span)</b> "
        "là hiệu hai giá trị cực biên (vd 30°). Xét bộ điều khiển tỉ lệ trong hệ kín (Hình 7.18): thêm Kp vào "
        "hệ cho hàm truyền vòng kín dạng bậc hai; với đầu vào bậc, nếu under-damped sẽ có quá điều (overshoot) "
        "và thời gian xác lập lớn (Hình 7.19)."))
    b.append(fig(18, F.fig_7_18()))
    b.append(fig(19, F.fig_7_19()))
    b.append(p(
        "Vấn đề thứ hai của chỉ tỉ lệ: xét điều khiển mức nước (Hình 7.20), để giữ lưu lượng ra mới cần tín "
        "hiệu vào van mới, mà bộ tỉ lệ chỉ cho đầu ra khi có sai lệch — nên mức nước không bao giờ đạt chính "
        "xác mức yêu cầu; gọi là <b>offset hay sai lệch xác lập</b> (Hình 7.21). Tăng Kp giảm offset nhưng "
        "tăng tần số dao động và giảm độ giảm chấn (tăng overshoot) — phải thỏa hiệp."))
    b.append(fig(20, F.fig_7_20()))
    b.append(fig(21, F.fig_7_21()))
    b.append(p(
        "<b>PD (tỉ lệ + đạo hàm):</b> đáp ứng với đầu vào dốc (Hình 7.22) — phần đạo hàm lớn nhất khi độ dốc "
        "sai lệch lớn, giúp đầu ra tăng nhanh hơn và giảm overshoot; không bao giờ dùng đạo hàm một mình. "
        "<b>PI (tỉ lệ + tích phân):</b> đáp ứng với đầu vào bậc (Hình 7.23) — phần tích phân loại bỏ offset, "
        "cho giá trị xác lập bằng giá trị đặt, dùng khi nhiễu tải thường xuyên. <b>PID</b> kết hợp: tích phân "
        "khử offset, đạo hàm giúp lên nhanh. Ví dụ (Hình 7.24–7.27): khảo sát đồ thị đầu ra cho tín hiệu sai "
        "lệch cho trước với (a) chỉ P Kp=5, (b) P+D Kp=5 Kd=2,0 s, (c) P+I Kp=5 Ki=2,0 s⁻¹ — đầu ra lần "
        "lượt là 50%+5e, cộng thêm 2,0 lần độ dốc, và cộng thêm 2,0 lần diện tích dưới đồ thị sai lệch."))
    b.append(fig(22, F.fig_7_22()))
    b.append(fig(23, F.fig_7_23()))
    b.append(fig(24, F.fig_7_24()))
    b.append(fig(25, F.fig_7_25()))
    b.append(fig(26, F.fig_7_26()))
    b.append(fig(27, F.fig_7_27()))
    b.append(h3("7.4.1 Dải tỉ lệ", "Proportional band"))
    b.append(p(
        "Với bộ điều khiển quá trình, hệ số tỉ lệ thường biểu diễn bằng <b>dải tỉ lệ (proportional band, "
        "PB)</b> — phần trăm độ lệch gây đổi đầu ra 100% (Hình 7.28): %PB = %độ lệch × 100 / %đổi đầu ra. "
        "PB 50% nghĩa là lệch 50% đổi đầu ra 100%; PB 100% nghĩa là lệch 100% đổi 100%. Ví dụ: bộ điều "
        "khiển nhiệt đầu vào 0°–50°, đầu ra 4–20 mA, PB 60% → Kp = 1/(0,6) × (20−4)/(50−0) = 0,53 mA/°."))
    b.append(fig(28, F.fig_7_28()))

    # 7.5
    b.append(h2("7.5 Bộ điều khiển quá trình", "A process controller"))
    b.append(p(
        "Hình 7.29 là mặt trước điển hình của bộ điều khiển ba số tử: màn hình biến quá trình, giá trị đặt, "
        "thanh đồ thị và các phím. Ở <b>chế độ chỉnh tay (manual)</b> người vận hành trực tiếp tăng/giảm đầu "
        "ra; ở <b>tự động (auto)</b> bộ điều khiển làm việc như ba số tử với giá trị đặt do người vận hành; "
        "<b>tự động từ xa (remote auto)</b> giá trị đặt do tín hiệu ngoài. Chuyển từ tay sang tự động có thể "
        "gây 'bump' (nhảy đầu ra) do phần tử tích phân — các bộ hiện đại tự bù (bumpless transfer). Hình 7.30 "
        "là sơ đồ khối ở chế độ chỉnh tay, tín hiệu chỉnh tay được cộng vào đầu ra trước khi chuyển tự động."))
    b.append(fig(29, F.fig_7_29()))
    b.append(fig(30, F.fig_7_30()))

    # 7.6
    b.append(h2("7.6 Toán học bộ điều khiển", "Controller mathematics"))
    b.append(p(
        "Các dạng cơ bản (Hình 7.31–7.34): <b>P</b> đầu ra = Kp·e; <b>PD</b> đầu ra = Kp·e + Kd·de/dt = "
        "Kd(s + Kp/Kd)E(s), với Td = Kd/Kp là hằng số thời gian đạo hàm; <b>PI</b> đầu ra = Kp·e + Ki∫e dt = "
        "Kp(1 + 1/(Tᵢs))E(s), Tᵢ = Kp/Ki là hằng số thời gian tích phân; <b>PID</b> đầu ra = Kp·e + Ki∫e dt + "
        "Kd·de/dt = Kp(1 + 1/(Tᵢs) + Td·s)E(s). Ví dụ (Hình 7.35): hệ hở có bộ điều khiển PD (Kp+Kd s) và "
        "quá trình G(s) = ωn²/(s²+2ζωn s)."))
    b.append(fig(31, F.fig_7_31()))
    b.append(fig(32, F.fig_7_32()))
    b.append(fig(33, F.fig_7_33()))
    b.append(fig(34, F.fig_7_34()))
    b.append(fig(35, F.fig_7_35()))
    b.append(h3("7.6.1 Biểu đồ Bode", "Bode plots"))
    b.append(p(
        "Hình 7.36 là dạng cơ bản biểu đồ Bode lợi: <b>(a) P</b> làm tăng lợi hệ thống; <b>(b) PI</b> giảm "
        "lợi tần cao (nên giảm ảnh hưởng nhiễu cao tần); <b>(c) PD</b> giảm lợi tần thấp và tăng lợi (tăng "
        "dự trữ pha, nhưng tăng ảnh hưởng nhiễu); <b>(d) PID</b> không có dạng chuẩn vì phụ thuộc tỉ lệ Tᵢ/Td "
        "(thường chọn Tᵢ = 4Td)."))
    b.append(fig(36, F.fig_7_36()))

    # 7.7
    b.append(h2("7.7 Hiệu chỉnh (Tuning)", "Tuning"))
    b.append(p(
        "<b>Hiệu chỉnh (tuning)</b> là chọn các tham số tối ưu của bộ điều khiển (Kp, Ki, Kd). Phương pháp "
        "kinh nghiệm phổ biến nhất là của Ziegler–Nichols, xấp xỉ hàm truyền vòng hở bằng hệ bậc nhất có độ "
        "trễ, gồm hai thủ tục: phương pháp chu kỳ tới hạn (dựa thử nghiệm vòng kín) và phương pháp đặc tuyến "
        "quá trình (dựa thử nghiệm vòng hở). Cả hai nhắm tới đáp ứng quá điều với tỉ lệ suy giảm ~1/4."))
    b.append(p(
        "<b>7.7.1 Phương pháp chu kỳ tới hạn.</b> Tắt các chế độ chỉ để tỉ lệ, tăng dần Kp đến khi đáp ứng "
        "dao động bền (không tăng không giảm); ghi Kpu và chu kỳ Tu. Bảng 7.1 cho thiết lập: P → Kp=0,5Kpu; "
        "PI → Kp=0,45Kpu, Tᵢ=Tu/1,2; PID → Kp=0,6Kpu, Tᵢ=0,5Tu, Td=Tu/8."))
    b.append(table(["Loại bộ điều khiển", "Kp", "Tᵢ", "Td"],
                   [["P", "0,5 Kpu", "—", "—"],
                    ["PI", "0,45 Kpu", "Tu/1,2", "—"],
                    ["PID", "0,6 Kpu", "0,5 Tu", "Tu/8"]],
                   "Bảng 7.1 — Thiết lập từ phương pháp chu kỳ tới hạn."))
    b.append(p(
        "<b>7.7.2 Phương pháp đặc tuyến quá trình.</b> Mở vòng, áp một bước nhỏ vào phần tử hiệu chỉnh và "
        "ghi đáp ứng theo thời gian — <b>đường đặc tuyến quá trình</b> (Hình 7.37). Vẽ tiếp tuyến tại điểm "
        "uốn cho độ dốc cực đại R = M/T; thời gian từ lúc bắt đầu đến giao trục của tiếp tuyến là độ trễ L. "
        "Bảng 7.2 cho thiết lập: P → Kp=P/(RL); PI → Kp=0,9P/(RL), Tᵢ=3,3L; PID → Kp=1,2P/(RL), Tᵢ=2L, "
        "Td=0,5L."))
    b.append(fig(37, F.fig_7_37()))
    b.append(table(["Loại bộ điều khiển", "Kp", "Tᵢ", "Td"],
                   [["P", "P/(RL)", "—", "—"],
                    ["PI", "0,9 P/(RL)", "3,3 L", "—"],
                    ["PID", "1,2 P/(RL)", "2 L", "0,5 L"]],
                   "Bảng 7.2 — Thiết lập từ phương pháp đặc tuyến quá trình."))

    # 7.8
    b.append(h2("7.8 Hệ thống số", "Digital systems"))
    b.append(p(
        "<b>Điều khiển số trực tiếp (DDC)</b> dùng máy tính trong hệ điều khiển để tính tín hiệu điều khiển "
        "tác động lên cơ cấu chấp hành (Hình 7.38). Mỗi chu kỳ lấy mẫu, máy tính qua ADC lấy giá trị đầu ra, "
        "cùng giá trị đầu vào rời rạc xử lý theo luật điều khiển (vd PID) rồi qua DAC đưa ra hiệu chỉnh. Các "
        "chương trình DDC lặp lại mỗi chu kỳ lấy mẫu, tính phần tỉ lệ, đạo hàm (hiệu sai lệch hai mẫu) hay "
        "tích phân (diện tích dưới đồ thị)."))
    b.append(fig(38, F.fig_7_38()))
    b.append(h3("7.8.1 Bộ điều khiển logic khả trình (PLC)", "Programmable logic controllers"))
    b.append(p(
        "PLC là dạng vi xử lý dùng bộ nhớ lập trình, vận hành bởi kỹ sư ít hiểu máy tính, qua ngôn ngữ hình "
        "họa <b>thang (ladder)</b>. Hệ PLC gồm 5 thành phần: vi xử lý, bộ nhớ, nguồn, giao tiếp vào/ra và "
        "thiết bị lập trình (Hình 7.39). Thiết bị lập trình (thường cầm tay, Hình 7.40) nạp chương trình vào "
        "bộ nhớ. Mạch chuyển mô-tơ (Hình 7.41) vẽ lại thành dạng thang (Hình 7.41(b)) với hai thanh nguồn và "
        "các rung ngang. Ký hiệu cơ bản (Hình 7.42): tiếp điểm thường mở, thường đóng (đầu vào) và ký hiệu "
        "thiết bị ra, END kết thúc rung; Hình 7.43 là một rung thang. Ví dụ PLC điều khiển sưởi trung tâm "
        "(Hình 7.44): lò, bơm, radiator, bồn nước nóng với cảm biến và đồng hồ; Hình 7.45 là chương trình "
        "thang với đầu vào X400–X403, đầu ra Y430–Y432."))
    b.append(fig(39, F.fig_7_39()))
    b.append(fig(40, F.fig_7_40()))
    b.append(fig(41, F.fig_7_41()))
    b.append(fig(42, F.fig_7_42()))
    b.append(fig(43, F.fig_7_43()))
    b.append(fig(44, F.fig_7_44()))
    b.append(fig(45, F.fig_7_45()))
    b.append(h3("7.8.2 Hệ nhúng", "Embedded systems"))
    b.append(p(
        "<b>Hệ nhúng</b> là hệ điều khiển có vi xử lý nằm như một phần tử tích hợp trong hệ — quản lý động cơ "
        "xe, lấy nét và phơi sáng máy ảnh, máy giặt hiện đại. Hình 7.46 là hệ lấy nét tự động: cảm biến khoảng "
        "cách → vi xử lý → lái ống kính, vị trí ống kính phản hồi so sánh đến khi hết sai lệch. Hình 7.47 là "
        "hệ nhúng máy giặt: vi xử lý theo chương trình điều khiển van, bơm, gia nhiệt, mô-tơ; các cảm biến "
        "mức/nhiệt/động cơ/cửa phản hồi."))
    b.append(fig(46, F.fig_7_46()))
    b.append(fig(47, F.fig_7_47()))

    # Problems
    b.append(h2("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 14 bài tập. Một số minh họa bằng hình: Bài 5 (Hình 7.48) điều khiển mức nước bằng bộ tỉ lệ "
        "Kp=10; Bài 8 (Hình 7.49) vẽ đồ thị đầu ra theo P/PD/PI từ tín hiệu sai lệch cho trước; Bài 11 "
        "(Hình 7.50) đặc tuyến quá trình để tìm thiết lập PID; Bài 14 (Hình 7.51) điều khiển mức chất lỏng "
        "với bộ điều khiển (s+0,5)/(0,2s+1). Các bài còn lại xoay quanh: range/span, deviation, Kp từ PB, "
        "offset, Ziegler–Nichols (chu kỳ tới hạn và đặc tuyến quá trình), và hàm truyền vòng kín."))
    b.append(fig(48, F.fig_7_48()))
    b.append(fig(49, F.fig_7_49()))
    b.append(fig(50, F.fig_7_50()))
    b.append(fig(51, F.fig_7_51()))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter discusses process controllers and the control laws they use, from simple on-off control, "
        "through the classic three-term (PID) controller, to digital systems such as PLCs and embedded controllers."))

    # 7.1
    b.append(h2("7.1 Introduction", "Introduction"))
    b.append(p(
        "Process controllers are components which basically have an input of the error signal, i.e. the "
        "difference between the required value signal and the feedback signal, and an output of a signal to "
        "modify the system output. The simplest form is an on-off device which switches on a correcting device "
        "when there is an error and switches it off when the error ceases. Such a method has limitations and "
        "more sophisticated controllers are often used. A form of controller which gives satisfactory control "
        "in many situations is the three-term or PID controller. The term <b>control mode</b> is the type of "
        "response a controller gives to an error signal; the three basic modes are proportional (P), integral "
        "(I) and derivative (D), and the three-term controller combines all three. Figure 7.1 is the bimetallic "
        "thermostat used in a simple temperature control system."))
    b.append(fig(1, F.fig_7_1()))
    b.append(h3("7.1.1 Compensation and controllers", "Compensation and controllers"))
    b.append(p(
        "<b>Compensation</b> is the modification of a system's performance characteristics to obtain the "
        "required ones; compensators are added to modify closed-loop performance and can be placed anywhere. "
        "Controllers have an error input and a correction output and are used at a specific point. From the "
        "design point of view there is no real difference between compensators and controllers — the terms "
        "reflect hardware differences. A controller is traditionally a stand-alone component offering control "
        "modes such as proportional gain and integral and derivative action, normally including a summing "
        "element."))

    # 7.2
    b.append(h2("7.2 On-off control", "On-off control"))
    b.append(p(
        "With on-off control, the controller is essentially a switch activated by the error signal and supplies "
        "just an on-off correcting signal. An example is the bimetallic thermostat (Figure 7.1): if the actual "
        "temperature is above the required temperature the strip is in the off position and the heater is off; "
        "if below, it moves to the on position and the heater switches on. The controller output can thus be "
        "just on or off (Figure 7.2)."))
    b.append(fig(2, F.fig_7_2()))
    b.append(p(
        "Because the control action is discontinuous and there are time lags, the controlled variable "
        "oscillates about the required condition. With the bimetallic thermostat, when the room temperature "
        "drops below the required level there is a significant delay before the heater affects the room, so the "
        "temperature has fallen further; when it rises to the required value the system still overshoots "
        "because of reaction delay — the temperature oscillates above and below the required value (Figure "
        "7.3). The system may also chatter near the set value; this is reduced if the heater switches on at a "
        "lower temperature than it switches off (Figure 7.4). The <b>dead band</b> is the range between the on "
        "and off values. A large dead band gives large fluctuations; a small one increases the switching "
        "frequency."))
    b.append(fig(3, F.fig_7_3()))
    b.append(fig(4, F.fig_7_4()))

    # 7.2.1
    b.append(h3("7.2.1 Electronic switching", "Electronic switching"))
    b.append(p(
        "Mechanical switches (bimetallic strips, relays) switch slowly; faster switching uses electronic "
        "circuits such as thyristors or transistors. A <b>thyristor</b> (SCR) can be considered a diode "
        "switched to conduct at a particular forward voltage. Figure 7.5 shows a thyristor in series with a 30 "
        "Ω resistor across 300 V; the gate controls the breakdown voltage. Figure 7.6 shows it chopping a d.c. "
        "voltage to control power to a load; Figure 7.7 is an a.c. circuit for lamps, motors or heaters where "
        "R2 sets the trigger level and a diode protects the gate."))
    b.append(fig(5, F.fig_7_5()))
    b.append(fig(6, F.fig_7_6()))
    b.append(fig(7, F.fig_7_7()))
    b.append(p(
        "The <b>transistor</b> also acts as an electronic switch (Figure 7.8): with no input the collector-"
        "emitter resistance is high and the whole Vcc appears at the output; with sufficient input it drops and "
        "Vout ≈ 0. A <b>Darlington pair</b> (Figure 7.9) amplifies a small base current to switch a larger "
        "load, with a protection diode. D.c. motor speed can be open-loop controlled by <b>pulse-width "
        "modulation (PWM)</b> (Figure 7.10): switching the d.c. voltage on and off, the larger the fraction "
        "on the closer the average to the input. Figure 7.11 is a transistor PWM circuit with a flyback diode. "
        "The four-transistor <b>H-circuit</b> (Figure 7.12) controls both direction and speed; Figure 7.13 "
        "uses logic gates for microprocessor control. Figure 7.14 is a closed-loop microprocessor system: "
        "tachogenerator → ADC → processor → PWM → motor."))
    b.append(fig(8, F.fig_7_8()))
    b.append(fig(9, F.fig_7_9()))
    b.append(fig(10, F.fig_7_10()))
    b.append(fig(11, F.fig_7_11()))
    b.append(fig(12, F.fig_7_12()))
    b.append(fig(13, F.fig_7_13()))
    b.append(fig(14, F.fig_7_14()))

    # 7.3
    b.append(h2("7.3 PID control", "PID control"))
    b.append(p(
        "There are three basic modes. <b>Proportional (P):</b> output proportional to error e, i.e. output = "
        "Kp·e with Kp the proportional gain (Figure 7.15). <b>Derivative (D):</b> output proportional to the "
        "rate of change de/dt, i.e. output = Kd·de/dt (Figure 7.16) — the slope of the error-time graph. "
        "<b>Integral (I):</b> output proportional to the integral of the error with time, i.e. the area under "
        "the error-time graph, and so can be non-zero even when the error has returned to zero (Figure 7.17)."))
    b.append(fig(15, F.fig_7_15()))
    b.append(fig(16, F.fig_7_16()))
    b.append(fig(17, F.fig_7_17()))

    # 7.4
    b.append(h2("7.4 Terminology", "Terminology"))
    b.append(p(
        "Terms used in describing controllers: <b>set-point</b> is the signal representing the required output; "
        "<b>range</b> is the two extreme values between which the system operates (e.g. 0°–30°); <b>span</b> is "
        "the difference between those extremes (e.g. 30°). Consider a proportional controller in a closed-loop "
        "system (Figure 7.18): adding Kp gives a second-order closed-loop transfer function; with a step input, "
        "if underdamped there are oscillations before settling (Figure 7.19)."))
    b.append(fig(18, F.fig_7_18()))
    b.append(fig(19, F.fig_7_19()))
    b.append(p(
        "A second problem with proportional-only control: consider water-level control (Figure 7.20); to hold "
        "a new outflow the valve needs a new signal, but a proportional controller only gives output with an "
        "error — so the level never quite reaches the set value; this is the <b>offset or steady-state "
        "error</b> (Figure 7.21). Increasing Kp reduces the offset but increases the oscillation frequency and "
        "reduces damping (more overshoot) — a compromise is needed."))
    b.append(fig(20, F.fig_7_20()))
    b.append(fig(21, F.fig_7_21()))
    b.append(p(
        "<b>PD (proportional + derivative):</b> the response to a ramp input (Figure 7.22) has the derivative "
        "term largest when the error slope is greatest, so the output rises faster and overshoot is reduced; "
        "derivative is never used alone. <b>PI (proportional + integral):</b> the response to a step input "
        "(Figure 7.23) removes the offset, giving a steady-state value equal to the set value; used where load "
        "disturbances occur frequently. <b>PID</b> combines both. Example (Figures 7.24–7.27): for the given "
        "error signal, sketch the controller output starting at 50% as (a) just proportional Kp=5, (b) P+D with "
        "Kp=5 and Kd=2.0 s, (c) P+I with Kp=5 and Ki=2.0 s⁻¹ — the output is 50%+5e, plus 2.0 times the error "
        "slope, and plus 2.0 times the area under the error-time graph respectively."))
    b.append(fig(22, F.fig_7_22()))
    b.append(fig(23, F.fig_7_23()))
    b.append(fig(24, F.fig_7_24()))
    b.append(fig(25, F.fig_7_25()))
    b.append(fig(26, F.fig_7_26()))
    b.append(fig(27, F.fig_7_27()))
    b.append(h3("7.4.1 Proportional band", "Proportional band"))
    b.append(p(
        "With process controllers the proportional gain is described by its <b>proportional band (PB)</b> — "
        "the percentage deviation that produces a 100% change in controller output (Figure 7.28): %PB = "
        "%deviation × 100 / %change in output. A 50% PB means a 50% deviation gives 100% output change; 100% "
        "PB means 100% deviation gives 100%. Example: a temperature controller with input 0°–50° and output "
        "4–20 mA, PB 60% → Kp = 1/0.6 × (20−4)/(50−0) = 0.53 mA/°."))
    b.append(fig(28, F.fig_7_28()))

    # 7.5
    b.append(h2("7.5 A process controller", "A process controller"))
    b.append(p(
        "Figure 7.29 shows the basic elements on the front face of a typical three-term process controller: "
        "process-variable and set-point displays, a bar graph and the keys. In <b>manual mode</b> the operator "
        "directly raises/lowers the output; in <b>automatic mode</b> it acts as a three-term controller with an "
        "operator-set point; in <b>remote automatic mode</b> the set point comes from an external signal. "
        "Switching manual→automatic can cause a 'bump' in output because of the integral term — modern "
        "controllers give a bumpless transfer. Figure 7.30 is the block diagram in manual mode, with the manual "
        "adjustment added to the controller output before switching to automatic."))
    b.append(fig(29, F.fig_7_29()))
    b.append(fig(30, F.fig_7_30()))

    # 7.6
    b.append(h2("7.6 Controller mathematics", "Controller mathematics"))
    b.append(p(
        "The basic forms (Figures 7.31–7.34): <b>P</b> output = Kp·e; <b>PD</b> output = Kp·e + Kd·de/dt = "
        "Kd(s + Kp/Kd)E(s), with Td = Kd/Kp the derivative time constant; <b>PI</b> output = Kp·e + Ki∫e dt = "
        "Kp(1 + 1/(Tᵢs))E(s), Tᵢ = Kp/Ki the integral time constant; <b>PID</b> output = Kp·e + Ki∫e dt + "
        "Kd·de/dt = Kp(1 + 1/(Tᵢs) + Td·s)E(s). Example (Figure 7.35): the open-loop system uses a PD "
        "controller Kp+Kd s and plant G(s) = ωn²/(s²+2ζωn s)."))
    b.append(fig(31, F.fig_7_31()))
    b.append(fig(32, F.fig_7_32()))
    b.append(fig(33, F.fig_7_33()))
    b.append(fig(34, F.fig_7_34()))
    b.append(fig(35, F.fig_7_35()))
    b.append(h3("7.6.1 Bode plots", "Bode plots"))
    b.append(p(
        "Figure 7.36 shows the basic Bode gain plots: <b>(a) P</b> increases overall system gain; <b>(b) PI</b> "
        "decreases high-frequency gain (thus reducing high-frequency noise effect); <b>(c) PD</b> decreases "
        "low-frequency gain and raises it (increasing phase margin but increasing noise effect); <b>(d) PID</b> "
        "has no standard form since the shape depends on the ratio Tᵢ/Td (commonly Tᵢ = 4Td)."))
    b.append(fig(36, F.fig_7_36()))

    # 7.7
    b.append(h2("7.7 Tuning", "Tuning"))
    b.append(p(
        "<b>Tuning</b> is selecting the optimum controller settings (Kp, Ki, Kd). The most widely used "
        "empirical methods are those of Ziegler and Nichols, approximating the open-loop transfer function by a "
        "first-order system with time delay, giving two procedures: the ultimate-cycle method (closed-loop "
        "test) and the process-reaction method (open-loop test). Both aim for under-damped transients with a "
        "decay ratio of about 1/4."))
    b.append(p(
        "<b>7.7.1 Ultimate cycle method.</b> With only proportional mode, raise Kp until the response shows "
        "sustained oscillations; note Kpu and the oscillation period Tu. Table 7.1 gives the settings: P → "
        "Kp=0.5Kpu; PI → Kp=0.45Kpu, Tᵢ=Tu/1.2; PID → Kp=0.6Kpu, Tᵢ=0.5Tu, Td=Tu/8."))
    b.append(table(["Controller type", "Kp", "Tᵢ", "Td"],
                   [["P", "0.5 Kpu", "—", "—"],
                    ["PI", "0.45 Kpu", "Tu/1.2", "—"],
                    ["PID", "0.6 Kpu", "0.5 Tu", "Tu/8"]],
                   "Table 7.1 — Settings from the ultimate cycle method."))
    b.append(p(
        "<b>7.7.2 Process reaction method.</b> Open the loop, apply a small step to the correction element and "
        "record the response — the <b>process reaction curve</b> (Figure 7.37). A tangent at the inflection "
        "gives the maximum gradient R = M/T; the time from the test start to where the tangent meets the time "
        "axis is the lag L. Table 7.2 gives the settings: P → Kp=P/(RL); PI → Kp=0.9P/(RL), Tᵢ=3.3L; PID → "
        "Kp=1.2P/(RL), Tᵢ=2L, Td=0.5L."))
    b.append(fig(37, F.fig_7_37()))
    b.append(table(["Controller type", "Kp", "Tᵢ", "Td"],
                   [["P", "P/(RL)", "—", "—"],
                    ["PI", "0.9 P/(RL)", "3.3 L", "—"],
                    ["PID", "1.2 P/(RL)", "2 L", "0.5 L"]],
                   "Table 7.2 — Settings from the process reaction curve method."))

    # 7.8
    b.append(h2("7.8 Digital systems", "Digital systems"))
    b.append(p(
        "<b>Direct digital control (DDC)</b> uses a digital computer in the control system to calculate the "
        "control signal applied to the actuators (Figure 7.38). At each sample instant the computer samples the "
        "plant output via an ADC, together with the discrete input, processes them by the required control law "
        "(e.g. PID) and sends the result via a DAC to the plant. The programs repeat every sampling period, "
        "computing the proportional part, the derivative part (difference between successive error samples) or "
        "the integral part (area under the output-time graph)."))
    b.append(fig(38, F.fig_7_38()))
    b.append(h3("7.8.1 Programmable logic controllers", "Programmable logic controllers"))
    b.append(p(
        "A PLC is a special microprocessor-based controller with programmable memory, programmed by engineers "
        "via a simple pictorial <b>ladder</b> language. A PLC system has five basic components: processor, "
        "memory, power supply, I/O interface and programming device (Figure 7.39). The programming device "
        "(often hand-held, Figure 7.40) loads the program into memory. The motor-switching circuit (Figure "
        "7.41) is redrawn as a ladder (Figure 7.41(b)) with two power rails and horizontal rungs. Basic "
        "symbols (Figure 7.42) are normally open / normally closed input contacts and the output symbol, with "
        "END marking the last rung; Figure 7.43 is a ladder rung. Example: a PLC controls central heating "
        "(Figure 7.44) — boiler, pumps, radiators and hot-water tank with sensors and a clock; Figure 7.45 is "
        "the ladder program with inputs X400–X403 and outputs Y430–Y432."))
    b.append(fig(39, F.fig_7_39()))
    b.append(fig(40, F.fig_7_40()))
    b.append(fig(41, F.fig_7_41()))
    b.append(fig(42, F.fig_7_42()))
    b.append(fig(43, F.fig_7_43()))
    b.append(fig(44, F.fig_7_44()))
    b.append(fig(45, F.fig_7_45()))
    b.append(h3("7.8.2 Embedded systems", "Embedded systems"))
    b.append(p(
        "An <b>embedded system</b> is a control system with the microprocessor embedded as an integral element "
        "— engine management, camera exposure/focus, washing machines. Figure 7.46 is automatic focusing: the "
        "range sensor feeds the microprocessor which drives the lens; the lens position is fed back and compared "
        "until there is no error. Figure 7.47 is the embedded washing-machine system: a program-driven "
        "microprocessor controls valves, pump, heater and motor, with sensors for level, temperature, speed and "
        "door feeding back."))
    b.append(fig(46, F.fig_7_46()))
    b.append(fig(47, F.fig_7_47()))

    # Problems
    b.append(h2("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 14 problems. Some are illustrated: Problem 5 (Figure 7.48) water-level control with a "
        "proportional controller Kp=10; Problem 8 (Figure 7.49) sketches the controller output for P/PD/PI from "
        "a given error signal; Problem 11 (Figure 7.50) uses the process reaction curve to find PID settings; "
        "Problem 14 (Figure 7.51) controls liquid level with a controller (s+0.5)/(0.2s+1). The rest cover "
        "range/span, deviation, Kp from PB, offset, Ziegler–Nichols (ultimate cycle and process reaction) and "
        "closed-loop transfer functions."))
    b.append(fig(48, F.fig_7_48()))
    b.append(fig(49, F.fig_7_49()))
    b.append(fig(50, F.fig_7_50()))
    b.append(fig(51, F.fig_7_51()))
    return "".join(b)
