# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 2, System models.

Vietnamese and English prose with all 49 redrawn vector figures.
"""
import boltonfig2 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 28
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Hệ số khuyếch đại (gain)</em> — tỉ lệ giữa đầu ra và đầu vào. · "
            "<em>Phản hồi (feedback)</em> — một phần đầu ra được đưa ngược lại để so sánh với đầu vào. · "
            "<em>Phản hồi âm/dương (negative/positive feedback)</em> — tín hiệu phản hồi trừ/cộng vào đầu vào. · "
            "<em>Hàm truyền (transfer function)</em> — tỉ lệ Y(s)/X(s) khi điều kiện ban đầu bằng không. · "
            "<em>Biến đổi Laplace</em> — công cụ đưa phương trình vi phân về dạng đại số. · "
            "<em>Hằng số thời gian (time constant)</em> — τ, đặc trưng cho tốc độ đáp ứng hệ bậc nhất. · "
            "<em>Tỷ số giảm chấn (damping ratio) ζ</em> — xác định dạng đáp ứng hệ bậc hai. · "
            "<em>Độ nhạy (sensitivity)</em> — mức độ thay đổi đặc tính do biến thiên tham số hay nhiễu.")
    return note(
        "<b>Key terms.</b> <em>Gain</em> — ratio of output to input. · <em>Feedback</em> — a fraction of "
        "the output returned to be compared with the input. · <em>Negative/positive feedback</em> — the "
        "feedback signal subtracts from / adds to the input. · <em>Transfer function</em> — Y(s)/X(s) with "
        "zero initial conditions. · <em>Laplace transform</em> — turns a differential equation into algebra. · "
        "<em>Time constant τ</em> — characterises first-order response speed. · <em>Damping ratio ζ</em> — "
        "shapes the second-order response. · <em>Sensitivity</em> — how much performance changes when a "
        "parameter or disturbance changes.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này xây dựng các mô hình toán học (phương trình vi phân và hàm truyền) cho những hệ thống "
        "điển hình — cơ, quay, điện, nhiệt và thủy lực — rồi chỉ ra cách ghép chúng thành sơ đồ khối và rút "
        "gọn bằng phương pháp hàm truyền. Đây là nền tảng để phân tích đáp ứng và thiết kế bộ điều khiển ở "
        "các chương sau."))

    # ---------------------------------------------------------- 2.1
    b.append(h2("2.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Để biết đầu ra của một hệ thống điều khiển phản ứng ra sao trước các đầu vào khác nhau, ta cần một "
        "mô hình toán học mô tả quan hệ giữa đầu ra và đầu vào. Với một hệ khuếch đại đơn giản, đầu ra luôn "
        "gấp mười lần đầu vào (Hình 2.1): đây là một mô hình tuyến tính với hệ số khuyếch đại G = 10."))
    b.append(fig(1, F.fig_2_1()))
    b.append(p(
        "Nhưng nhiều hệ thống không cho đầu ra tức thời. Với một cân lò xo, khi đặt một tải không đổi (đầu "
        "vào bậc), kim sẽ dao động một lát rồi mới dừng ở trọng lượng (Hình 2.2). Tương tự, mạch điện trở—tụ "
        "khi đóng điện, hoặc hệ sưởi phòng khi tăng set-point từ 20° đến 22°, đầu ra đều thay đổi theo thời "
        "gian trước khi đạt giá trị xác lập. Mô hình tổng quát thường là một phương trình vi phân."))
    b.append(fig(2, F.fig_2_2()))
    b.append(p(
        "Để giữ quan hệ vào–ra gọn gàng ngay cả khi có yếu tố thời gian, ta dùng <em>biến đổi Laplace</em>: "
        "viết đầu vào, đầu ra dưới dạng hàm của s thay vì của thời gian. Chương này trình bày cách thiết lập "
        "các phương trình đó; phần toán học nền tảng nằm ở Phụ lục A và B."))

    # ---------------------------------------------------------- 2.2
    b.append(h2("2.2 Hệ số khuyếch đại (Gain)", "Gain"))
    b.append(p(
        "Với hệ có đầu ra tỉ lệ trực tiếp với đầu vào, ta viết:"))
    b.append(eq("output = G × input", "2.1"))
    b.append(p(
        "với G là hệ số khuyếch đại. Ví dụ: một động cơ có tốc độ tỉ lệ với điện áp phần ứng; nếu ra 5 vòng/s "
        "khi vào 2 V thì G = 5/2 = 2,5 (vòng/s)/V."))
    b.append(h3("2.2.1 Hệ số khuyếch đại của các hệ mắc nối tiếp", "Gain of systems in series"))
    b.append(p(
        "Xét hai hệ nối tiếp, hệ thứ nhất hệ số G1, hệ thứ hai G2 (Hình 2.3(a)). Đầu ra tổng cộng là tích các "
        "hệ số:"))
    b.append(eq("G = G1 × G2", "2.2"))
    b.append(fig(3, F.fig_2_3()))
    b.append(p(
        "<b>Hệ nối tiếp:</b> hệ số khuyếch đại tổng cộng bằng tích các hệ số của từng hệ thành phần."))
    b.append(h3("2.2.2 Vòng phản hồi", "Feedback loops"))
    b.append(p(
        "Với <em>phản hồi âm</em> (Hình 2.4), đầu ra được đưa ngược qua hệ đo có hệ số H để <em>trừ</em> khỏi "
        "đầu vào của hệ G. Gọi đầu vào tổng là x, tín hiệu lỗi là x − Hy, và:"))
    b.append(eq("y = G(x − Hy)  ⇒  (1 + GH) y = Gx", "2.3"))
    b.append(fig(4, F.fig_2_4()))
    b.append(p(
        "Hệ số khuyếch đại tổng cộng G<sub>overall</sub> = y/x = G/(1+GH). <b>Phản hồi âm:</b> hệ số đường "
        "thẳng chia cho (1 + tích đường thẳng và phản hồi)."))
    b.append(p(
        "Với <em>phản hồi dương</em> (Hình 2.5), tín hiệu phản hồi <em>cộng</em> vào đầu vào, nên:"))
    b.append(eq("y = G(x + Hy)  ⇒  (1 − GH) y = Gx", "2.4"))
    b.append(fig(5, F.fig_2_5()))
    b.append(p(
        "<b>Phản hồi dương:</b> hệ số đường thẳng chia cho (1 − tích đường thẳng và phản hồi)."))
    b.append(h3("2.2.3 Bộ khuếch đại phản hồi", "The feedback amplifier"))
    b.append(p(
        "Hình 2.6 là mạch khuếch đại phản hồi gồm một op-amp với mạng phân áp hai điện trở R1, R2. Vì hệ số "
        "khuếch đại G của op-amp rất lớn, GH ≫ 1 nên hệ số tổng cộng xấp xỉ 1/H. Mạng phân áp cho H = "
        "R1/(R1+R2), do đó:"))
    b.append(eq("hệ số tổng cộng = (R1 + R2)/R1", "2.5"))
    b.append(fig(6, F.fig_2_6()))
    b.append(p(
        "Nhờ phản hồi, hệ số phụ thuộc vào các điện trở (bền) hơn là vào G của op-amp (dễ thay đổi theo nhiệt "
        "độ, tuổi thọ). Với R1 = 1 kΩ, R2 = 49 kΩ và G = 200 000, hệ số tổng cộng vẫn là 50, độc lập với G."))

    # ---------------------------------------------------------- 2.3
    b.append(h2("2.3 Các hệ động (Dynamic systems)", "Dynamic systems"))
    b.append(p(
        "Ta mô hình hóa một hệ phức tạp bằng những phần tử cơ bản. Mỗi lĩnh vực (cơ, quay, điện, nhiệt, thủy "
        "lực) đều có ba khối cấu tạo tương ứng với độ cứng, giảm chấn và quán tính."))
    b.append(h3("2.3.1 Hệ cơ (Mechanical systems)", "Mechanical systems"))
    b.append(p(
        "Hệ cơ gồm ba phần tử: lò xo (độ cứng), giảm chấn (dashpot, damping) và khối lượng (quán tính) — Hình "
        "2.7."))
    b.append(fig(7, F.fig_2_7()))
    b.append(p(
        "Lò xo tuyến tính: F = ky (k là độ cứng). Giảm chấn: F = c·dy/dt (c là hằng số giảm chấn). Khối lượng "
        "m theo Newton: F = m·d²y/dt². Ví dụ hệ ở Hình 2.8(a) có phương trình:"))
    b.append(eq("m·d²y/dt² = F − ky − c·dy/dt   ⇒   m·d²y/dt² + c·dy/dt + ky = F", "2.6"))
    b.append(fig(8, F.fig_2_8()))
    b.append(p(
        "Đây là <em>phương trình vi phân bậc hai</em> (chứa đạo hàm bậc hai)."))
    b.append(h3("2.3.2 Hệ quay (Rotational systems)", "Rotational systems"))
    b.append(p(
        "Các phần tử tương ứng là lò xo xoắn (T = kθ), giảm chấn quay (T = c·dθ/dt) và mô-men quán tính (T = "
        "I·d²θ/dt²) — Hình 2.9. Ví dụ đĩa xoắn bởi trục (Hình 2.10):"))
    b.append(fig(9, F.fig_2_9()))
    b.append(fig(10, F.fig_2_10()))
    b.append(eq("I·d²θ/dt² = T − kθ − c·dθ/dt   ⇒   I·d²θ/dt² + c·dθ/dt + kθ = T", "2.7"))
    b.append(h3("2.3.3 Hệ điện (Electrical systems)", "Electrical systems"))
    b.append(p(
        "Ba phần tử cơ bản: điện trở (v = Ri), cuộn cảm (v = L·di/dt) và tụ (i = C·dv/dt) — Hình 2.11. Dùng "
        "định luật Kirchhoff, mạch RC (Hình 2.12) cho:"))
    b.append(fig(11, F.fig_2_11()))
    b.append(fig(12, F.fig_2_12()))
    b.append(eq("v = RC·dvc/dt + vc", "2.8"))
    b.append(p("đây là phương trình bậc nhất. Mạch RLC (Hình 2.13) cho phương trình bậc hai:"))
    b.append(fig(13, F.fig_2_13()))
    b.append(eq("v = RC·dvc/dt + LC·d²vc/dt² + vc", "2.9"))
    b.append(h3("2.3.4 Hệ nhiệt (Thermal systems)", "Thermal systems"))
    b.append(p(
        "Hai khối cấu tạo: điện trở nhiệt (q = (T1−T2)/R) và điện dung nhiệt (C = mc) — Hình 2.14. Nhiệt kế "
        "(Hình 2.15) và phòng có lò sưởi (Hình 2.16) đều dẫn đến phương trình bậc nhất:"))
    b.append(fig(14, F.fig_2_14()))
    b.append(fig(15, F.fig_2_15()))
    b.append(fig(16, F.fig_2_16()))
    b.append(eq("RC·dT/dt + T = Rq1 + T0", "2.10"))
    b.append(h3("2.3.5 Hệ thủy lực (Hydraulic systems)", "Hydraulic systems"))
    b.append(p(
        "Tương ứng với điện trở, điện dung và cảm kháng là điện trở thủy lực (p1−p2 = Rq), điện dung thủy lực "
        "(q1−q2 = C·dp/dt) và quán tính thủy lực (p1−p2 = I·dq/dt) — Hình 2.17. Hệ bồn–van (Hình 2.18):"))
    b.append(fig(17, F.fig_2_17()))
    b.append(fig(18, F.fig_2_18()))
    b.append(eq("A·dh/dt + (hρg)/R = q1", "2.11"))

    # ---------------------------------------------------------- 2.4
    b.append(h2("2.4 Phương trình vi phân", "Differential equations"))
    b.append(h3("2.4.1 Phương trình bậc nhất", "First-order differential equations"))
    b.append(p(
        "Nhiều hệ được mô tả bởi τ·dy/dt + y = kx, với τ là hằng số thời gian, k là hệ số khuyếch đại xác "
        "lập. Với đầu vào bậc đơn vị, đầu ra tiến tới k, và theo thời gian:"))
    b.append(eq("y = k(1 − e^(−t/τ))", "2.12"))
    b.append(p(
        "Sau 1τ đạt 0,63k; 2τ đạt 0,86k; 3τ đạt 0,95k; 4τ đạt 0,98k (Hình 2.19). Ví dụ: mạch RC, mạch RL, "
        "phòng có sưởi điện."))
    b.append(fig(19, F.fig_2_19()))
    b.append(h3("2.4.2 Phương trình bậc hai", "Second-order differential equations"))
    b.append(p(
        "Nhiều hệ có dạng d²y/dt² + 2ζωn·dy/dt + ωn²y = kωn²x, với ζ là tỷ số giảm chấn, ωn là tần số góc tự "
        "nhiên không giảm chấn. Đáp ứng với đầu vào bậc đơn vị (Hình 2.20) phụ thuộc ζ:"))
    b.append(fig(20, F.fig_2_20()))
    b.append(ul([
        "ζ = 0 (không giảm chấn): dao động biên độ không đổi.",
        "0 &lt; ζ &lt; 1 (giảm chấn nhẹ): dao động tắt dần; ζ càng gần 1 tắt càng nhanh.",
        "ζ = 1 (giảm chấn tới hạn): không dao động, tiến tới giá trị xác lập.",
        "ζ &gt; 1 (quá giảm chấn): chậm hơn giảm chấn tới hạn.",
    ]))
    b.append(p(
        "Ví dụ hệ bậc hai: cơ (lò xo–giảm chấn–khối lượng), điện (R–L–C)."))

    # ---------------------------------------------------------- 2.5
    b.append(h2("2.5 Hàm truyền (Transfer function)", "Transfer function"))
    b.append(p(
        "Biến đổi Laplace đưa phương trình vi phân về dạng đại số: biến hàm thời gian v(t) thành V(s); đạo "
        "hàm bậc nhất thành sV(s) (với điều kiện ban đầu không), bậc hai thành s²V(s). Hàm truyền G(s) là tỉ "
        "lệ giữa đầu ra và đầu vào dưới dạng s, với điều kiện ban đầu bằng không:"))
    b.append(eq("G(s) = Y(s)/X(s)", "2.13"))
    b.append(fig(21, F.fig_2_21()))
    b.append(p(
        "Nó được biểu diễn như một khối: đầu vào X(s) nhân với G(s) để được Y(s). Ví dụ mạch RC cho G(s) = "
        "1/(RCs + 1)."))
    b.append(h3("2.5.2 Hàm truyền của các phần tử thông dụng", "Transfer functions of common elements"))
    b.append(table(
        ["Phần tử", "Hàm truyền G(s)"],
        [["Bộ truyền động (gear train), tỉ số N", "N"],
         ["Bộ khuếch đại, hệ số G", "G"],
         ["Potentiometer, tỉ số K", "K"],
         ["Động cơ một chiều điều khiển phần ứng", "1/(sL + R)"],
         ["Cơ cấu thủy lực điều khiển van", "K1/(s(K2s + K3))"],
         ["Hệ sưởi", "1/(sC + 1/R)"],
         ["Tachogenerator", "K"],
         ["Vị trí từ tốc độ (v = dy/dt)", "1/s"],
         ["Mức chất lỏng trong bồn", "1/(sA + ρg/R)"]],
        caption="Bảng 2.1 — Hàm truyền của các phần tử thường gặp."))
    b.append(h3("2.5.3 Hàm truyền và hệ thống", "Transfer functions and systems"))
    b.append(p(
        "Xét hệ điều khiển tốc độ trục: amplifier K → động cơ 1/(sL+R) → bộ truyền N → đầu ra, phản hồi qua "
        "tachogenerator H (Hình 2.22). Sơ đồ khối:"))
    b.append(fig(22, F.fig_2_22()))

    # ---------------------------------------------------------- 2.6
    b.append(h2("2.6 Hàm truyền hệ thống", "System transfer functions"))
    b.append(h3("2.6.1 Các hệ nối tiếp", "Systems in series"))
    b.append(p(
        "Với hai hệ nối tiếp (Hình 2.23), Y(s) = G2(s)·Y1(s) = G2(s)·G1(s)·X(s), nên:"))
    b.append(eq("G_overall(s) = G1(s)·G2(s)", "2.14"))
    b.append(fig(23, F.fig_2_23()))
    b.append(h3("2.6.2 Các hệ có phản hồi", "Systems with feedback"))
    b.append(p(
        "Phản hồi âm (Hình 2.24): tín hiệu lỗi E(s) = X(s) − H(s)Y(s), và Y(s) = G(s)E(s) ⇒ "))
    b.append(eq("G_overall(s) = G(s) / (1 + G(s)H(s))", "2.15"))
    b.append(fig(24, F.fig_2_24()))
    b.append(p("Phản hồi dương (Hình 2.25):"))
    b.append(eq("G_overall(s) = G(s) / (1 − G(s)H(s))", "2.16"))
    b.append(fig(25, F.fig_2_25()))

    # ---------------------------------------------------------- 2.7
    b.append(h2("2.7 Độ nhạy (Sensitivity)", "Sensitivity"))
    b.append(h3("2.7.1 Nhạy cảm với thay đổi tham số", "Sensitivity to changes in parameters"))
    b.append(p(
        "Với vòng kín phản hồi âm (Hình 2.28), nếu G(s)H(s) lớn thì G_overall ≈ 1/H(s): hệ ít nhạy với biến "
        "thiên đường thẳng nhưng nhạy với biến thiên đường phản hồi. Hệ số nhạy của đường thẳng:"))
    b.append(eq("S = 1 / (1 + G(s)H(s))", "2.17"))
    b.append(fig(28, F.fig_2_28()))
    b.append(p(
        "Ví dụ: hệ phản hồi âm với H = 0,1, G = 50 → G_overall = 8,3; tăng G lên 10% (thành 55) → 8,5, "
        "tức chỉ đổi ~2%. Nếu G = 5 thì đổi ~6%. G lớn càng làm giảm độ nhạy — đó chính là ưu điểm của bộ "
        "khuếch đại phản hồi (Hình 2.26, 2.27)."))
    b.append(fig(26, F.fig_2_26()))
    b.append(fig(27, F.fig_2_27()))
    b.append(h3("2.7.2 Nhạy cảm với nhiễu (Disturbances)", "Sensitivity to disturbances"))
    b.append(p(
        "Nhiễu D(s) tác động giữa hai phần tử. Với hệ vòng hở (Hình 2.29), đầu ra Y = G1G2X + G2D. Với hệ "
        "vòng kín (Hình 2.30), thành phần do nhiễu bị giảm bởi hệ số [1 + G1G2H]:"))
    b.append(fig(29, F.fig_2_29()))
    b.append(fig(30, F.fig_2_30()))

    # ---------------------------------------------------------- 2.8
    b.append(h2("2.8 Thao tác sơ đồ khối", "Block manipulation"))
    b.append(p(
        "Để rút gọn sơ đồ khối mà vẫn giữ nguyên hàm truyền tổng cộng, ta dùng các quy tắc sau (đã lược bỏ "
        "(s))."))
    b.append(h3("2.8.1 Khối nối tiếp", "Blocks in series"))
    b.append(fig(31, F.fig_2_31()))
    b.append(h3("2.8.2 Di chuyển điểm lấy tín hiệu", "Moving take-off points"))
    b.append(fig(32, F.fig_2_32()))
    b.append(fig(33, F.fig_2_33()))
    b.append(h3("2.8.3 Di chuyển điểm cộng", "Moving a summing point"))
    b.append(fig(34, F.fig_2_34()))
    b.append(fig(35, F.fig_2_35()))
    b.append(fig(36, F.fig_2_36()))
    b.append(fig(37, F.fig_2_37()))
    b.append(h3("2.8.4 Đổi đường phản hồi và đường thẳng", "Changing feedback and forward paths"))
    b.append(fig(38, F.fig_2_38()))
    b.append(fig(39, F.fig_2_39()))
    b.append(p(
        "<b>Ví dụ.</b> Rút gọn hệ ở Hình 2.40. Các bước 2.41–2.46 cho kết quả cuối:"))
    b.append(fig(40, F.fig_2_40()))
    b.append(fig(41, F.fig_2_41()))
    b.append(fig(42, F.fig_2_42()))
    b.append(fig(43, F.fig_2_43()))
    b.append(fig(44, F.fig_2_44()))
    b.append(fig(45, F.fig_2_45()))
    b.append(fig(46, F.fig_2_46()))

    # ---------------------------------------------------------- 2.9
    b.append(h2("2.9 Nhiều đầu vào (Multiple inputs)", "Multiple inputs"))
    b.append(p(
        "Khi có nhiều đầu vào, dùng <em>nguyên lý xếp chồng</em>: đặt các đầu vào khác về không, tính đáp "
        "ứng từng đầu vào riêng biệt, rồi cộng lại. Xét hệ ở Hình 2.47 với X(s) và nhiễu D(s):"))
    b.append(fig(47, F.fig_2_47()))
    b.append(p("Đặt D(s) = 0 (Hình 2.48) và X(s) = 0 (Hình 2.49) rồi cộng hai kết quả:"))
    b.append(fig(48, F.fig_2_48()))
    b.append(fig(49, F.fig_2_49()))

    b.append(h3("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 13 bài tập (Hình 2.50–2.55 minh họa một số): tính đầu ra từ hệ số khuyếch đại; hàm truyền "
        "hệ nối tiếp ba phần tử; hàm truyền hệ kín âm với G = 2/(s+1), H = 0,1; rút gọn sơ đồ khối; xác định "
        "đầu ra Y(s) của các hệ nhiều đầu vào (Hình 2.54, 2.55). Các bài này củng cố việc tính hệ số khuyếch "
        "đại, hàm truyền và thao tác sơ đồ khối."))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter builds the mathematical models (differential equations and transfer functions) for "
        "typical systems — mechanical, rotational, electrical, thermal and hydraulic — and shows how to "
        "assemble them into block diagrams and reduce those using transfer-function algebra. It is the "
        "foundation for analysing responses and designing controllers in later chapters."))

    # ---------------------------------------------------------- 2.1
    b.append(h2("2.1 Introduction", "Introduction"))
    b.append(p(
        "To determine how a control system's output reacts to different inputs we need a mathematical model "
        "relating output to input. For a simple amplifier the output is always ten times the input (Figure "
        "2.1): a linear model with gain G = 10."))
    b.append(fig(1, F.fig_2_1()))
    b.append(p(
        "But many systems do not respond instantly. With a spring balance, applying a constant load (a step "
        "input) makes the pointer oscillate before settling on the weight (Figure 2.2). Similarly an RC "
        "circuit when switched on, or a room heater when the set-point is raised from 20° to 22°, all change "
        "with time before reaching the steady value. The general model is a differential equation."))
    b.append(fig(2, F.fig_2_2()))
    b.append(p(
        "To keep input–output relations compact even with time dependence we use the <em>Laplace transform</em>: "
        "write inputs and outputs as functions of s rather than of time. This chapter shows how to obtain "
        "those equations; the underlying mathematics is in Appendices A and B."))

    # ---------------------------------------------------------- 2.2
    b.append(h2("2.2 Gain", "Gain"))
    b.append(p("For a system whose output is directly proportional to the input we write:"))
    b.append(eq("output = G × input", "2.1"))
    b.append(p(
        "where G is the gain. Example: a motor whose speed is proportional to armature voltage; if it gives "
        "5 rev/s at 2 V then G = 5/2 = 2.5 (rev/s)/V."))
    b.append(h3("2.2.1 Gain of systems in series", "Gain of systems in series"))
    b.append(p(
        "For two systems in series, the first with gain G1, the second G2 (Figure 2.3(a)), the overall output "
        "is the product of the gains:"))
    b.append(eq("G = G1 × G2", "2.2"))
    b.append(fig(3, F.fig_2_3()))
    b.append(p(
        "<b>Series systems:</b> the overall gain is the product of the constituent gains."))
    b.append(h3("2.2.2 Feedback loops", "Feedback loops"))
    b.append(p(
        "With <em>negative feedback</em> (Figure 2.4) the output is fed back through a measuring element of "
        "gain H to be <em>subtracted</em> from the input to the G element. Let the input be x; the error is "
        "x − Hy, so:"))
    b.append(eq("y = G(x − Hy)  ⇒  (1 + GH) y = Gx", "2.3"))
    b.append(fig(4, F.fig_2_4()))
    b.append(p(
        "The overall gain G_overall = y/x = G/(1+GH). <b>Negative feedback:</b> the forward gain divided by "
        "(1 + forward × feedback gain)."))
    b.append(p(
        "With <em>positive feedback</em> (Figure 2.5) the fed-back signal <em>adds</em> to the input, so:"))
    b.append(eq("y = G(x + Hy)  ⇒  (1 − GH) y = Gx", "2.4"))
    b.append(fig(5, F.fig_2_5()))
    b.append(p(
        "<b>Positive feedback:</b> the forward gain divided by (1 − forward × feedback gain)."))
    b.append(h3("2.2.3 The feedback amplifier", "The feedback amplifier"))
    b.append(p(
        "Figure 2.6 shows a feedback amplifier: an op-amp with a potential divider of two resistors R1, R2. "
        "Since the op-amp gain G is very large, GH ≫ 1, so the overall gain approximates 1/H. The divider "
        "gives H = R1/(R1+R2), hence:"))
    b.append(eq("overall gain = (R1 + R2)/R1", "2.5"))
    b.append(fig(6, F.fig_2_6()))
    b.append(p(
        "Feedback makes the gain depend on the (stable) resistors rather than on G of the op-amp (which "
        "drifts with temperature and age). With R1 = 1 kΩ, R2 = 49 kΩ and G = 200 000, the overall gain is "
        "still 50, independent of G."))

    # ---------------------------------------------------------- 2.3
    b.append(h2("2.3 Dynamic systems", "Dynamic systems"))
    b.append(p(
        "We model a complex system from a few basic elements. Each domain (mechanical, rotational, "
        "electrical, thermal, hydraulic) has three building blocks corresponding to stiffness, damping and "
        "inertia."))
    b.append(h3("2.3.1 Mechanical systems", "Mechanical systems"))
    b.append(p(
        "Mechanical systems are built from spring (stiffness), dashpot (damping) and mass (inertia) — Figure "
        "2.7."))
    b.append(fig(7, F.fig_2_7()))
    b.append(p(
        "Linear spring: F = ky (k is stiffness). Dashpot: F = c·dy/dt (c is the damping constant). Mass m by "
        "Newton: F = m·d²y/dt². The system of Figure 2.8(a) gives:"))
    b.append(eq("m·d²y/dt² = F − ky − c·dy/dt   ⇒   m·d²y/dt² + c·dy/dt + ky = F", "2.6"))
    b.append(fig(8, F.fig_2_8()))
    b.append(p("This is a <em>second-order differential equation</em> (it contains a second derivative)."))
    b.append(h3("2.3.2 Rotational systems", "Rotational systems"))
    b.append(p(
        "The corresponding elements are torsional spring (T = kθ), rotational dashpot (T = c·dθ/dt) and moment "
        "of inertia (T = I·d²θ/dt²) — Figure 2.9. For the disk twisted by a shaft (Figure 2.10):"))
    b.append(fig(9, F.fig_2_9()))
    b.append(fig(10, F.fig_2_10()))
    b.append(eq("I·d²θ/dt² = T − kθ − c·dθ/dt   ⇒   I·d²θ/dt² + c·dθ/dt + kθ = T", "2.7"))
    b.append(h3("2.3.3 Electrical systems", "Electrical systems"))
    b.append(p(
        "The three basics: resistor (v = Ri), inductor (v = L·di/dt) and capacitor (i = C·dv/dt) — Figure "
        "2.11. Using Kirchhoff's laws, the RC circuit (Figure 2.12) gives:"))
    b.append(fig(11, F.fig_2_11()))
    b.append(fig(12, F.fig_2_12()))
    b.append(eq("v = RC·dvc/dt + vc", "2.8"))
    b.append(p("a first-order equation. The RLC circuit (Figure 2.13) gives a second-order equation:"))
    b.append(fig(13, F.fig_2_13()))
    b.append(eq("v = RC·dvc/dt + LC·d²vc/dt² + vc", "2.9"))
    b.append(h3("2.3.4 Thermal systems", "Thermal systems"))
    b.append(p(
        "Two building blocks: thermal resistance (q = (T1−T2)/R) and thermal capacitance (C = mc) — Figure "
        "2.14. A thermometer (Figure 2.15) and a room with a heater (Figure 2.16) both lead to a first-order "
        "equation:"))
    b.append(fig(14, F.fig_2_14()))
    b.append(fig(15, F.fig_2_15()))
    b.append(fig(16, F.fig_2_16()))
    b.append(eq("RC·dT/dt + T = Rq1 + T0", "2.10"))
    b.append(h3("2.3.5 Hydraulic systems", "Hydraulic systems"))
    b.append(p(
        "Analogous to electrical resistance, capacitance and inductance are hydraulic resistance (p1−p2 = "
        "Rq), hydraulic capacitance (q1−q2 = C·dp/dt) and hydraulic inertance (p1−p2 = I·dq/dt) — Figure "
        "2.17. For the tank–valve system (Figure 2.18):"))
    b.append(fig(17, F.fig_2_17()))
    b.append(fig(18, F.fig_2_18()))
    b.append(eq("A·dh/dt + (hρg)/R = q1", "2.11"))

    # ---------------------------------------------------------- 2.4
    b.append(h2("2.4 Differential equations", "Differential equations"))
    b.append(h3("2.4.1 First-order differential equations", "First-order differential equations"))
    b.append(p(
        "Many systems obey τ·dy/dt + y = kx, where τ is the time constant and k the steady-state gain. For a "
        "unit step input the output approaches k, and with time:"))
    b.append(eq("y = k(1 − e^(−t/τ))", "2.12"))
    b.append(p(
        "After 1τ it reaches 0.63k; 2τ → 0.86k; 3τ → 0.95k; 4τ → 0.98k (Figure 2.19). Examples: RC and RL "
        "circuits, a room with electric heating."))
    b.append(fig(19, F.fig_2_19()))
    b.append(h3("2.4.2 Second-order differential equations", "Second-order differential equations"))
    b.append(p(
        "Many systems take the form d²y/dt² + 2ζωn·dy/dt + ωn²y = kωn²x, where ζ is the damping ratio and ωn "
        "the undamped natural angular frequency. The unit-step response (Figure 2.20) depends on ζ:"))
    b.append(fig(20, F.fig_2_20()))
    b.append(ul([
        "ζ = 0 (undamped): continuous oscillation of constant amplitude.",
        "0 &lt; ζ &lt; 1 (underdamped): decaying oscillation; the closer ζ to 1, the faster it decays.",
        "ζ = 1 (critically damped): no oscillation, rises to the steady value.",
        "ζ &gt; 1 (overdamped): slower than critical damping to reach steady state.",
    ]))
    b.append(p("Second-order examples: a spring–dashpot–mass system, and an RLC circuit."))

    # ---------------------------------------------------------- 2.5
    b.append(h2("2.5 Transfer function", "Transfer function"))
    b.append(p(
        "The Laplace transform turns a differential equation into algebra: a time function v(t) becomes V(s); "
        "a first derivative becomes sV(s) (zero initial conditions), a second becomes s²V(s). The transfer "
        "function G(s) is the ratio of output to input in the s-domain, with zero initial conditions:"))
    b.append(eq("G(s) = Y(s)/X(s)", "2.13"))
    b.append(fig(21, F.fig_2_21()))
    b.append(p(
        "It is drawn as a block: input X(s) multiplied by G(s) to give Y(s). The RC circuit gives G(s) = "
        "1/(RCs + 1)."))
    b.append(h3("2.5.2 Transfer functions of common elements", "Transfer functions of common elements"))
    b.append(table(
        ["Element", "Transfer function G(s)"],
        [["Gear train, ratio N", "N"],
         ["Amplifier, gain G", "G"],
         ["Potentiometer, ratio K", "K"],
         ["Armature-controlled d.c. motor", "1/(sL + R)"],
         ["Valve-controlled hydraulic actuator", "K1/(s(K2s + K3))"],
         ["Heating system", "1/(sC + 1/R)"],
         ["Tachogenerator", "K"],
         ["Displacement from rotation (v = dy/dt)", "1/s"],
         ["Liquid level in a container", "1/(sA + ρg/R)"]],
        caption="Table 2.1 — Transfer functions of commonly encountered elements."))
    b.append(h3("2.5.3 Transfer functions and systems", "Transfer functions and systems"))
    b.append(p(
        "Consider a shaft-speed control system: amplifier K → motor 1/(sL+R) → gears N → output, with "
        "feedback via a tachogenerator H (Figure 2.22). The block diagram:"))
    b.append(fig(22, F.fig_2_22()))

    # ---------------------------------------------------------- 2.6
    b.append(h2("2.6 System transfer functions", "System transfer functions"))
    b.append(h3("2.6.1 Systems in series", "Systems in series"))
    b.append(p(
        "For two subsystems in series (Figure 2.23), Y(s) = G2(s)·Y1(s) = G2(s)·G1(s)·X(s), so:"))
    b.append(eq("G_overall(s) = G1(s)·G2(s)", "2.14"))
    b.append(fig(23, F.fig_2_23()))
    b.append(h3("2.6.2 Systems with feedback", "Systems with feedback"))
    b.append(p(
        "Negative feedback (Figure 2.24): the error E(s) = X(s) − H(s)Y(s), and Y(s) = G(s)E(s) ⇒ "))
    b.append(eq("G_overall(s) = G(s) / (1 + G(s)H(s))", "2.15"))
    b.append(fig(24, F.fig_2_24()))
    b.append(p("Positive feedback (Figure 2.25):"))
    b.append(eq("G_overall(s) = G(s) / (1 − G(s)H(s))", "2.16"))
    b.append(fig(25, F.fig_2_25()))

    # ---------------------------------------------------------- 2.7
    b.append(h2("2.7 Sensitivity", "Sensitivity"))
    b.append(h3("2.7.1 Sensitivity to changes in parameters", "Sensitivity to changes in parameters"))
    b.append(p(
        "For a closed loop with negative feedback (Figure 2.28), if G(s)H(s) is large then G_overall ≈ "
        "1/H(s): the system is relatively insensitive to changes in the forward path but sensitive to "
        "changes in the feedback path. The sensitivity of the forward element is:"))
    b.append(eq("S = 1 / (1 + G(s)H(s))", "2.17"))
    b.append(fig(28, F.fig_2_28()))
    b.append(p(
        "Example: a negative-feedback system with H = 0.1 and G = 50 gives G_overall = 8.3; increasing G by "
        "10% (to 55) gives 8.5, a change of only ~2%. With G = 5 the change is ~6%. A larger forward gain "
        "reduces sensitivity — the advantage of the feedback amplifier (Figures 2.26, 2.27)."))
    b.append(fig(26, F.fig_2_26()))
    b.append(fig(27, F.fig_2_27()))
    b.append(h3("2.7.2 Sensitivity to disturbances", "Sensitivity to disturbances"))
    b.append(p(
        "A disturbance D(s) acts between two elements. For an open-loop system (Figure 2.29), Y = G1G2X + "
        "G2D. For the closed-loop system (Figure 2.30) the disturbance component is reduced by the factor "
        "[1 + G1G2H]:"))
    b.append(fig(29, F.fig_2_29()))
    b.append(fig(30, F.fig_2_30()))

    # ---------------------------------------------------------- 2.8
    b.append(h2("2.8 Block manipulation", "Block manipulation"))
    b.append(p(
        "To simplify a block diagram while keeping the same overall transfer function we use the rules below "
        "(the (s) is omitted)."))
    b.append(h3("2.8.1 Blocks in series", "Blocks in series"))
    b.append(fig(31, F.fig_2_31()))
    b.append(h3("2.8.2 Moving take-off points", "Moving take-off points"))
    b.append(fig(32, F.fig_2_32()))
    b.append(fig(33, F.fig_2_33()))
    b.append(h3("2.8.3 Moving a summing point", "Moving a summing point"))
    b.append(fig(34, F.fig_2_34()))
    b.append(fig(35, F.fig_2_35()))
    b.append(fig(36, F.fig_2_36()))
    b.append(fig(37, F.fig_2_37()))
    b.append(h3("2.8.4 Changing feedback and forward paths", "Changing feedback and forward paths"))
    b.append(fig(38, F.fig_2_38()))
    b.append(fig(39, F.fig_2_39()))
    b.append(p(
        "<b>Example.</b> Simplify the system of Figure 2.40. Stages 2.41–2.46 give the final result:"))
    b.append(fig(40, F.fig_2_40()))
    b.append(fig(41, F.fig_2_41()))
    b.append(fig(42, F.fig_2_42()))
    b.append(fig(43, F.fig_2_43()))
    b.append(fig(44, F.fig_2_44()))
    b.append(fig(45, F.fig_2_45()))
    b.append(fig(46, F.fig_2_46()))

    # ---------------------------------------------------------- 2.9
    b.append(h2("2.9 Multiple inputs", "Multiple inputs"))
    b.append(p(
        "With more than one input we use the <em>superposition principle</em>: set all but one input to zero, "
        "find the output due to that input, and sum the results. Consider the system of Figure 2.47 with "
        "X(s) and disturbance D(s):"))
    b.append(fig(47, F.fig_2_47()))
    b.append(p("Set D(s) = 0 (Figure 2.48) and X(s) = 0 (Figure 2.49), then add the two outputs:"))
    b.append(fig(48, F.fig_2_48()))
    b.append(fig(49, F.fig_2_49()))

    b.append(h3("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 13 problems (Figures 2.50–2.55 illustrate some): finding output from a gain; the "
        "transfer function of a three-element series system; the closed-loop gain for G = 2/(s+1), H = 0.1; "
        "block-diagram reduction; and determining Y(s) for multi-input systems (Figures 2.54, 2.55). They "
        "reinforce gain, transfer-function and block-manipulation calculations."))
    return "".join(b)
