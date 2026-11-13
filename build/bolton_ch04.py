# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 4, System parameters.

Vietnamese and English prose with all 15 redrawn vector figures, the
damping-ratio/percentage-overshoot table, and the worked examples.
"""
import boltonfig4 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 13
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Đáp ứng quá độ (transient response)</em> — phần đáp ứng trước khi đạt xác lập. · "
            "<em>Thời hằng τ (time constant)</em> — thời gian để đầu ra đạt 0,63 giá trị xác lập. · "
            "<em>Tỷ số giảm chấn ζ (damping ratio)</em> — xác định mức dao động. · "
            "<em>Độ vượt (overshoot)</em> — lượng đầu ra vượt quá giá trị xác lập ở đỉnh đầu. · "
            "<em>Thời gian xác lập (settling time)</em> — thời gian dao động tắt vào vùng ±2% hoặc ±5%. · "
            "<em>Cực (pole)</em> — nghiệm của mẫu hàm truyền; quyết định tính ổn định.")
    return note(
        "<b>Key terms.</b> <em>Transient response</em> — the response before the system reaches steady state. · "
        "<em>Time constant τ</em> — the time for the output to reach 0.63 of the steady-state value. · "
        "<em>Damping ratio ζ</em> — determines the amount of oscillation. · <em>Overshoot</em> — the amount by "
        "which the output exceeds the steady-state value at the first peak. · <em>Settling time</em> — the time "
        "taken for the oscillations to fall and remain within ±2% or ±5% of the steady state. · <em>Pole</em> — a "
        "root of the transfer-function denominator; it governs stability.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này giới thiệu các tham số dùng để chỉ định đáp ứng quá độ của hệ — thời hằng, thời gian trễ, "
        "thời gian trỗi, độ vượt, tỷ số tắt dần và thời gian xác lập — cho cả hệ bậc nhất và bậc hai, rồi xét "
        "điều kiện ổn định qua vị trí các cực trên mặt phẳng s."))

    # 4.1
    b.append(h2("4.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Khi một hệ chịu một đầu vào bậc đơn vị, đầu ra có thể tiến tới một giá trị xác lập. Phần đáp ứng xảy ra "
        "trước khi đạt giá trị xác lập gọi là <b>đáp ứng quá độ (transient response)</b>. Chương này bàn các tham "
        "số dùng để chỉ định đáp ứng quá độ và xem xét liệu các quá độ có dẫn tới hệ không ổn định hay không."))
    b.append(p(
        "Ví dụ, với một hệ lò xo (Hình 4.1), nếu ta bất ngờ tác động một tải, hệ có đáp ứng quá độ: mất một thời "
        "gian để đạt giá trị xác lập và thường bị <b>vượt quá (overshoot)</b> giá trị đó trước khi dừng lại. Ta "
        "muốn biết: thay đổi yếu tố nào của lò xo để hệ đáp ứng nhanh hơn và giảm độ vượt? Tương tự, một hệ điều "
        "khiển vị trí chi tiết gia công cần biết nó phản ứng nhanh đến đâu và có bị vượt vị trí yêu cầu hay không "
        "— vì vượt vị trí là điều không mong muốn."))
    b.append(fig(1, F.fig_4_1()))
    b.append(p(
        "Với hệ lò xo nói trên, sau một số dao động biên độ ngày càng giảm, các quá độ tắt dần và hệ dừng ở giá "
        "trị xác lập — hệ được gọi là <b>ổn định (stable)</b>. Nếu các dao động tiếp tục với biên độ tăng dần thì "
        "không đạt giá trị xác lập nào và hệ <b>không ổn định (unstable)</b>. Chương xem xét ngắn gọn điều kiện "
        "để một hệ ổn định."))

    # 4.2
    b.append(h2("4.2 Hệ bậc nhất", "First order systems"))
    b.append(p("Một hệ bậc nhất có hàm truyền dạng:"))
    b.append(eq("G(s) = k / (τs + 1)", "4.1"))
    b.append(p(
        "với k là hệ số khuyếch đại xác lập và τ là thời hằng. Khi tác động đầu vào bậc đơn vị, đầu ra y là:"))
    b.append(eq("y = k (1 − e^(−t/τ))", "4.2"))
    b.append(p(
        "Tại t = τ thì y = k(1 − e^(−1)) = 0,63k. Vậy thời hằng τ của hệ bậc nhất ứng với đầu vào bậc là thời "
        "gian để đầu ra đạt 0,63 giá trị xác lập."))
    b.append(p("Các tham số chỉ định đặc tính quá độ của hệ bậc nhất:"))
    b.append(h3("Thời gian trễ (Delay time)", "Delay time"))
    b.append(p(
        "Thời gian trễ t<sub>d</sub> là thời gian để đầu ra đạt 50% giá trị xác lập. Vì k là giá trị cuối:"))
    b.append(eq("k/2 = k(1 − e^(−t_d/τ))   →   t_d = τ ln 2", "4.3"))
    b.append(h3("Thời gian trỗi (Rise time)", "Rise time"))
    b.append(p(
        "Thời gian trỗi t<sub>r</sub> là thời gian để đầu ra tăng từ 10% lên 90% giá trị xác lập (đôi khi quy ước "
        "0%–100%). Thời gian đạt 10%:"))
    b.append(eq("0,1k = k(1 − e^(−t_10/τ))   →   t_10 = τ ln 10", "4.4"))
    b.append(p("Thời gian đạt 90%:"))
    b.append(eq("0,9k = k(1 − e^(−t_90/τ))   →   t_90 = τ ln 10 − τ ln 9", "4.5"))
    b.append(p("Vậy thời gian trỗi:"))
    b.append(eq("t_r = t_90 − t_10 = τ ln 9", "4.6"))
    b.append(h3("Ví dụ", "Example"))
    b.append(p(
        "Xác định thời gian trễ và thời gian trỗi của hệ bậc nhất có hàm truyền G(s) = 3/(2s+1). So sánh với dạng "
        "k/(τs+1) cho hệ số khuyếch đại xác lập k = 3 và thời hằng τ = 2 s. Thời gian trễ t_d = 2 ln 10 = 4,6 s; "
        "thời gian trỗi t_r = 2 ln 9 = 4,4 s."))
    b.append(p(
        "Một nhiệt kế thủy ngân–thủy tinh là hệ bậc nhất với đầu vào là nhiệt độ và đầu ra là vị trí cột thủy "
        "ngân. Nhiệt kế ban đầu ở 0°C, thả đột ngột vào nước 100°C, sau 80 s chỉ 98°C. Đầu ra θ = 100(1 − e^(−t/τ)); "
        "từ 98 = 100(1 − e^(−80/τ)) suy ra τ = 49,7 s. (a) Thời hằng 49,7 s; (b) thời gian trễ t_d = 49,7 ln 10 = "
        "114,4 s; (c) thời gian trỗi t_r = 49,7 ln 9 = 109,2 s."))

    # 4.3
    b.append(h2("4.3 Hệ bậc hai", "Second order systems"))
    b.append(p("Một hệ bậc hai có hàm truyền dạng:"))
    b.append(eq("G(s) = ωn² / (s² + 2ζωn s + ωn²)", "4.7"))
    b.append(p(
        "Dạng đầu ra ứng với đầu vào bậc đơn vị phụ thuộc vào tỷ số giảm chấn ζ lớn hơn, bằng hay nhỏ hơn 1 — "
        "tương ứng là giảm chấn kém (underdamped), tới hạn (critically damped) và quá giảm chấn (overdamped) "
        "(xem Mục 3.5). Với dao động giảm chấn kém:"))
    b.append(eq("y = k [ 1 − (e^(−ζωn t)/√(1−ζ²)) · sin(ωd t + φ) ]", "4.8"))
    b.append(p("với tần số góc giảm chấn ωd = ωn√(1−ζ²). Đáp ứng bậc của hệ giảm chấn kém được minh họa ở Hình 4.2."))
    b.append(fig(2, F.fig_4_2()))
    b.append(h3("Thời gian trỗi", "Rise time"))
    b.append(p(
        "Thời gian trỗi t<sub>r</sub> là thời gian để đáp ứng tăng từ 0 đến giá trị xác lập y<sub>ss</sub> — tức "
        "hoàn thành một phần tư chu kỳ dao động, tức ωd·t_r = π/2. Giảm thời gian trỗi bằng cách tăng ωd:"))
    b.append(eq("t_r = π / (2 ωd) = π / (2 ωn √(1−ζ²))", "4.9"))
    b.append(p("Đôi khi thời gian trỗi được định nghĩa từ 10% đến 90% giá trị xác lập."))
    b.append(h3("Thời gian đạt đỉnh (Peak time)", "Peak time"))
    b.append(p(
        "Thời gian đạt đỉnh t<sub>p</sub> là thời gian để đáp ứng tăng từ 0 đến giá trị đỉnh đầu tiên — hoàn "
        "thành nửa chu kỳ, tức ωd·t_p = π:"))
    b.append(eq("t_p = π / ωd = π / (ωn √(1−ζ²))", "4.10"))
    b.append(p("Khi ζ = 1 thì t_p tiến tới vô cực — ở giảm chấn tới hạn giá trị xác lập chỉ được tiếp cận tiệm cận."))
    b.append(h3("Độ vượt (Overshoot)", "Overshoot"))
    b.append(p(
        "Độ vượt là lượng cực đại mà đáp ứng vượt quá giá trị xác lập, thường tính bằng % giá trị xác lập. Tại "
        "ωd·t = π, đầu ra vượt giá trị xác lập một lượng:"))
    b.append(eq("overshoot = y_ss · e^(−ζπ/√(1−ζ²))", "4.11"))
    b.append(p("Dưới dạng % giá trị xác lập:"))
    b.append(eq("%overshoot = e^(−ζπ/√(1−ζ²)) × 100%", "4.12"))
    b.append(p(
        "Độ vượt chỉ phụ thuộc tỷ số giảm chấn ζ, không phụ thuộc tần số tự nhiên. Khi ζ tiến tới 1, % độ vượt "
        "tiến tới 0. Bảng 4.1 cho giá trị % độ vượt ứng với từng tỷ số giảm chấn."))
    b.append(table(
        ["Tỷ số giảm chấn ζ", "% độ vượt"],
        [["0,2", "52,7"], ["0,3", "37,2"], ["0,4", "25,4"], ["0,5", "16,3"],
         ["0,6", "9,5"], ["0,7", "4,6"], ["0,8", "1,5"], ["0,9", "0,2"]],
        caption="Bảng 4.1 — % độ vượt đỉnh ứng với tỷ số giảm chấn."))
    b.append(h3("Tỷ số tắt dần (Subsidence ratio)", "Subsidence ratio"))
    b.append(p(
        "Tỷ số tắt dần (hay độ suy giảm) là biên độ của lần vượt thứ hai chia cho biên độ lần vượt đầu tiên. Tại "
        "ωd·t = π và ωd·t = 3π:"))
    b.append(eq("subsidence ratio = second / first = e^(−2πζ/√(1−ζ²))", "4.13"))
    b.append(h3("Thời gian xác lập (Settling time)", "Settling time"))
    b.append(p(
        "Thời gian xác lập t<sub>s</sub> đo thời gian để dao động tắt và nằm trong (và duy trì trong) một tỷ lệ "
        "nhất định của giá trị xác lập. Với tiêu chuẩn 2%:"))
    b.append(eq("t_s = 4 / (ζ ωn)", "4.14"))
    b.append(p("Với tiêu chuẩn 5%:"))
    b.append(eq("t_s = 3 / (ζ ωn)", "4.15"))
    b.append(h3("Số dao động trong thời gian xác lập", "Number of oscillations to settling time"))
    b.append(p(
        "Chu kỳ dao động là 2π/ωd. Trong thời gian xác lập t<sub>s</sub> (tiêu chuẩn 2%), số dao động:"))
    b.append(eq("number of oscillations = (4/(ζωn)) / (2π/ωd) = 2ζ / √(1−ζ²)", "4.16"))
    b.append(p(
        "Khi thiết kế: để đáp ứng nhanh (thời gian trỗi nhỏ) cần tần số tự nhiên lớn. Hình 4.3 cho đáp ứng với cùng "
        "ζ = 0,2 nhưng ωn khác nhau — ωn = 10 rad/s phản ứng nhanh hơn hẳn ωn = 1 rad/s. Tỷ số giảm chấn thường "
        "từ 0,4 đến 0,8: nhỏ quá gây vượt nhiều, lớn quá làm hệ trì trệ. Hình 4.4 cho hiệu ứng của việc đổi ζ khi "
        "ωn không đổi."))
    b.append(fig(3, F.fig_4_3()))
    b.append(fig(4, F.fig_4_4()))
    b.append(h3("Ví dụ", "Example"))
    b.append(p(
        "Hệ bậc hai có tần số góc tự nhiên ωn = 2,0 rad/s và tần số giảm chấn ωd = 1,8 rad/s. (a) Từ ωd = "
        "ωn√(1−ζ²) → ζ = 0,44. (b) Thời gian trỗi 100%: t_r = π/(2·1,8) = 0,87 s. (c) % độ vượt = exp(−0,44π/"
        "√(1−0,44²))×100% = 21%. (d) Thời gian xác lập 2%: t_s = 4/(0,44·2,0) = 4,5 s. (e) Số dao động = 2·0,44/"
        "√(1−0,44²) = 1,3."))
    b.append(p(
        "Hệ phản hồi ở Hình 4.5 có đường truyền thuận K/[s(s+a)] và đường phản hồi 1. Hàm truyền vòng kín:"))
    b.append(eq("G(s) = K / (s² + a s + K)", "4.17"))
    b.append(p(
        "So với dạng chuẩn bậc hai: ωn = √K, ζ = a/(2√K). Vì ωd·t_r = π/2 nên t_r = π/(2ωn√(1−ζ²)) — thời gian "
        "trỗi giảm khi K tăng (đáp ứng nhanh hơn). % độ vượt = exp(−ζπ/√(1−ζ²)) tăng khi K tăng. Thời gian xác "
        "lập t_s = 4/(ζωn) = 4/a — <b>độc lập với K</b>."))
    b.append(fig(5, F.fig_4_5()))

    # 4.4
    b.append(h2("4.4 Ổn định", "Stability"))
    b.append(p(
        "Một hệ được gọi là <b>ổn định</b> nếu khi có đầu vào hay thay đổi đầu vào, các quá độ tắt dần theo thời "
        "gian và để lại hệ ở trạng thái xác lập. Hệ <b>không ổn định</b> nếu các quá độ không tắt mà tăng dần."))
    b.append(p(
        "Xét hệ bậc hai G(s) = 1/[(s+1)(s+2)]; các giá trị s làm hàm truyền tiến tới vô cực gọi là <b>cực (poles)</b> "
        "— ở đây s = −1 và s = −2. Với đầu vào bậc đơn vị, đầu ra có các số hạng e^(−t) và e^(−2t), đều tắt dần để "
        "lại giá trị xác lập 0,5 — hệ ổn định. Ngược lại G(s) = 1/[(s−1)(s−2)] có cực s = +1, +2, cho các số hạng "
        "e^(+t), e^(+2t) tăng dần — hệ không ổn định. Như vậy: <b>cực âm → quá độ tắt dần (ổn định); cực dương → "
        "quá độ tăng (không ổn định)</b>."))
    b.append(p(
        "Tổng quát, với hệ bậc hai G(s) = ωn²/[(s+p1)(s+p2)], các nghiệm (cực) là:"))
    b.append(eq("p1 = −ζωn + ωn√(ζ²−1) ,   p2 = −ζωn − ωn√(ζ²−1)", "4.18"))
    b.append(p(
        "Với ζ > 1: nghiệm thực, cực thực âm hoặc dương. Với ζ &lt; 1: viết j = √−1, cực phức:"))
    b.append(eq("p1 = −ζωn + j ωn√(1−ζ²) ,   p2 = −ζωn − j ωn√(1−ζ²)", "4.19"))
    b.append(p(
        "Các giá trị cực viết dạng a + jb; phần jb là số ảo. Quy tắc ổn định vẫn giữ: <b>phần thực a âm → ổn định; "
        "a dương → không ổn định</b>."))
    b.append(h3("4.4.1 Mặt phẳng s", "The s plane"))
    b.append(p(
        "Ta vẽ vị trí các cực trên đồ thị với trục hoành là phần thực, trục tung là phần ảo — gọi là <b>mặt phẳng "
        "s (s-plane)</b>. Hình 4.6–4.10 minh họa các trường hợp: cực thực âm (ổn định, quá giảm), cực thực dương "
        "(không ổn định), cực phức nửa trái (ổn định, giảm chấn kém), cực phức nửa phải (không ổn định) và cực kép "
        "(giảm chấn tới hạn). Hình 4.11 tóm tắt: <b>hệ ổn định khi mọi cực nằm ở nửa trái mặt phẳng s</b>. Hình 4.12 "
        "cho thấy phần thực âm càng lớn, quá độ tắt càng nhanh; phần ảo càng lớn, tần số dao động càng cao."))
    b.append(fig(6, F.fig_4_6()))
    b.append(fig(7, F.fig_4_7()))
    b.append(fig(8, F.fig_4_8()))
    b.append(fig(9, F.fig_4_9()))
    b.append(fig(10, F.fig_4_10()))
    b.append(fig(11, F.fig_4_11()))
    b.append(fig(12, F.fig_4_12()))
    b.append(h3("Ví dụ", "Example"))
    b.append(p(
        "Hệ nào ổn định: (a) G(s) = 1/(s²+s+1) → cực −0,5 ± j0,866 (nửa trái) → ổn định; (b) G(s) = 1/(s²−5s+4) → "
        "cực +4, +1 (nửa phải) → không ổn định; (c) G(s) = 1/(s²−2s+3) → cực +1 ± j√2 (nửa phải) → không ổn định."))

    # Problems
    b.append(h2("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 10 bài tập, trong đó các Bài 6, 7, 9 được minh họa bằng sơ đồ khối và mặt phẳng s (Hình 4.13–"
        "4.15). Các bài tập bao gồm: tính thời gian trễ và trỗi cho hệ bậc nhất; xác định ωn, ζ, thời gian trỗi, % "
        "độ vượt và thời gian xác lập 2% cho hệ bậc hai; xác định K để có thời gian trỗi cho trước; xét tính ổn "
        "định từ vị trí cực trên mặt phẳng s và từ phương trình vi phân."))
    b.append(fig(13, F.fig_4_13()))
    b.append(fig(14, F.fig_4_14()))
    b.append(fig(15, F.fig_4_15()))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter introduces the parameters used to specify a system's transient response — time constant, "
        "delay time, rise time, overshoot, subsidence ratio and settling time — for both first- and second-order "
        "systems, then considers the conditions for stability via the location of the poles on the s-plane."))

    # 4.1
    b.append(h2("4.1 Introduction", "Introduction"))
    b.append(p(
        "When a system is subject to, say, a unit step input it may give an output which eventually settles down "
        "to some steady state value. The response that it gives before settling down to this steady state is "
        "called its <b>transient response</b>. This chapter is about the parameters used to specify the transient "
        "response of systems and whether the transients lead to unstable systems."))
    b.append(p(
        "For example, if we have a spring system (Figure 4.1) and suddenly apply a load to it, it has a transient "
        "response which results in it taking some time to reach its steady state value and also it is likely to "
        "<b>overshoot</b> the steady state value before it finally settles down. What factors can we change with "
        "the spring system in order to get it to respond more quickly to an input and also to minimise the "
        "overshooting? As another illustration, consider a control system used with an automatic machine to "
        "position a workpiece: we need to know how fast the system will respond and whether it will overshoot the "
        "required position — overshooting is undesirable in such a situation."))
    b.append(fig(1, F.fig_4_1()))
    b.append(p(
        "With the spring system, after some oscillations with ever-decreasing amplitude, the transients die away "
        "and the system settles down to a steady state value — the system is said to be <b>stable</b>. If, "
        "however, the oscillations continued with ever-increasing amplitude, then no steady state value would be "
        "reached and the system would be <b>unstable</b>. This chapter takes a brief look at the conditions for "
        "stability of systems."))

    # 4.2
    b.append(h2("4.2 First order systems", "First order systems"))
    b.append(p("A first order system has a transfer function of the form:"))
    b.append(eq("G(s) = k / (τs + 1)", "4.1"))
    b.append(p(
        "where k is the steady state gain and τ the time constant. When a unit step input is applied, the output y is:"))
    b.append(eq("y = k (1 − e^(−t/τ))", "4.2"))
    b.append(p(
        "When t = τ then y = k(1 − e^(−1)) = 0.63k. Thus the time constant τ of a first order system subject to a "
        "step input is the time taken for the output to reach 0.63 of the steady state value."))
    b.append(p("The parameters used to specify the transient performance are:"))
    b.append(h3("Delay time", "Delay time"))
    b.append(p(
        "The delay time t<sub>d</sub> is the time required for the output response to reach 50% of its steady "
        "state value. Since k is the final value:"))
    b.append(eq("k/2 = k(1 − e^(−t_d/τ))   →   t_d = τ ln 2", "4.3"))
    b.append(h3("Rise time", "Rise time"))
    b.append(p(
        "The rise time t<sub>r</sub> is the time required for the output to rise from 10% to 90% of its steady "
        "state value (note: sometimes specified 0% to 100%). The time to reach 10% is:"))
    b.append(eq("0.1k = k(1 − e^(−t_10/τ))   →   t_10 = τ ln 10", "4.4"))
    b.append(p("The time to reach 90% is:"))
    b.append(eq("0.9k = k(1 − e^(−t_90/τ))   →   t_90 = τ ln 10 − τ ln 9", "4.5"))
    b.append(p("Hence the rise time is:"))
    b.append(eq("t_r = t_90 − t_10 = τ ln 9", "4.6"))
    b.append(h3("Example", "Example"))
    b.append(p(
        "Determine the delay time and the rise time for a first order system with the transfer function G(s) = "
        "3/(2s+1). Comparison with k/(τs+1) gives a steady state gain of 3 and a time constant of 2 s. Thus the "
        "delay time is t_d = 2 ln 10 = 4.6 s; the rise time is t_r = 2 ln 9 = 4.4 s."))
    b.append(p(
        "A mercury-in-glass thermometer acts as a first order system with temperature as input and mercury "
        "position as output. Initially at 0°C, it is suddenly placed in water at 100°C and reads 98°C after 80 s. "
        "Then θ = 100(1 − e^(−t/τ)); from 98 = 100(1 − e^(−80/τ)) we get τ = 49.7 s. (a) Time constant 49.7 s; "
        "(b) delay time t_d = 49.7 ln 10 = 114.4 s; (c) rise time t_r = 49.7 ln 9 = 109.2 s."))

    # 4.3
    b.append(h2("4.3 Second order systems", "Second order systems"))
    b.append(p("A second order system has a transfer function of the form:"))
    b.append(eq("G(s) = ωn² / (s² + 2ζωn s + ωn²)", "4.7"))
    b.append(p(
        "The output for a unit step input depends on whether the damping factor ζ is less than, equal to or "
        "greater than 1 — the corresponding outcomes being underdamped, critically damped and overdamped (see "
        "Section 3.5). For the underdamped oscillations:"))
    b.append(eq("y = k [ 1 − (e^(−ζωn t)/√(1−ζ²)) · sin(ωd t + φ) ]", "4.8"))
    b.append(p("with the damped natural frequency ωd = ωn√(1−ζ²). Figure 4.2 shows the step response of an under-damped system."))
    b.append(fig(2, F.fig_4_2()))
    b.append(h3("Rise time", "Rise time"))
    b.append(p(
        "The rise time t<sub>r</sub> is the time taken for the response to rise from 0 to the steady-state value "
        "y<sub>ss</sub> — a quarter of a cycle, i.e. ωd·t_r = π/2. We reduce the rise time by increasing ωd:"))
    b.append(eq("t_r = π / (2 ωd) = π / (2 ωn √(1−ζ²))", "4.9"))
    b.append(p("The rise time is sometimes specified as the time to rise from 10% to 90% of the steady state value."))
    b.append(h3("Peak time", "Peak time"))
    b.append(p(
        "The peak time t<sub>p</sub> is the time taken for the response to rise from 0 to the first peak value — "
        "half a cycle, i.e. ωd·t_p = π:"))
    b.append(eq("t_p = π / ωd = π / (ωn √(1−ζ²))", "4.10"))
    b.append(p(
        "When ζ is 1 the peak time becomes infinite; at critical damping the steady state value is never reached "
        "but only approached asymptotically."))
    b.append(h3("Overshoot", "Overshoot"))
    b.append(p(
        "The overshoot is the maximum amount by which the response overshoots the steady state value, often "
        "written as a percentage of the steady state value. At ωd·t = π the output exceeds the steady state by:"))
    b.append(eq("overshoot = y_ss · e^(−ζπ/√(1−ζ²))", "4.11"))
    b.append(p("Expressed as a percentage of y_ss:"))
    b.append(eq("%overshoot = e^(−ζπ/√(1−ζ²)) × 100%", "4.12"))
    b.append(p(
        "The overshoot does not depend on the natural frequency but only on the damping factor. As ζ approaches 1 "
        "the percentage overshoot approaches zero. Table 4.1 gives values of the percentage overshoot for "
        "particular damping ratios."))
    b.append(table(
        ["Damping ratio", "Percentage overshoot"],
        [["0.2", "52.7"], ["0.3", "37.2"], ["0.4", "25.4"], ["0.5", "16.3"],
         ["0.6", "9.5"], ["0.7", "4.6"], ["0.8", "1.5"], ["0.9", "0.2"]],
        caption="Table 4.1 — Percentage peak overshoot for particular damping ratios."))
    b.append(h3("Subsidence ratio", "Subsidence ratio"))
    b.append(p(
        "The subsidence ratio (or decrement) is the amplitude of the second overshoot divided by the amplitude of "
        "the first overshoot. At ωd·t = π and ωd·t = 3π:"))
    b.append(eq("subsidence ratio = second / first = e^(−2πζ/√(1−ζ²))", "4.13"))
    b.append(h3("Settling time", "Settling time"))
    b.append(p(
        "The settling time t<sub>s</sub> is a measure of the time taken for the oscillations to die away — the time "
        "for the response to fall within and remain within some specified percentage of the steady-state value. "
        "For the 2% settling time:"))
    b.append(eq("t_s = 4 / (ζ ωn)", "4.14"))
    b.append(p("For the 5% settling time:"))
    b.append(eq("t_s = 3 / (ζ ωn)", "4.15"))
    b.append(h3("Number of oscillations to settling time", "Number of oscillations to settling time"))
    b.append(p(
        "The periodic time is 2π/ωd. In a settling time t<sub>s</sub> (2% criterion) the number of oscillations is:"))
    b.append(eq("number of oscillations = (4/(ζωn)) / (2π/ωd) = 2ζ / √(1−ζ²)", "4.16"))
    b.append(p(
        "For a rapid response (small rise time) the natural frequency must be large. Figure 4.3 shows the types of "
        "response to a unit step input of systems having the same damping factor of 0.2 but different natural "
        "angular frequencies — the response with ωn = 10 rad/s is much faster than that with ωn = 1 rad/s. The "
        "damping factor is typically in the range 0.4 to 0.8: smaller values give excessive overshoot, larger "
        "values render the system sluggish. Figure 4.4 shows the effect on the response of changing the damping "
        "factor when the natural angular frequency is unchanged."))
    b.append(fig(3, F.fig_4_3()))
    b.append(fig(4, F.fig_4_4()))
    b.append(h3("Example", "Example"))
    b.append(p(
        "A second order system has a natural angular frequency of 2.0 rad/s and a damped frequency of 1.8 rad/s. "
        "(a) Since ωd = ωn√(1−ζ²), ζ = 0.44. (b) The 100% rise time is t_r = π/(2·1.8) = 0.87 s. (c) The "
        "percentage overshoot is exp(−0.44π/√(1−0.44²))×100% = 21%. (d) The 2% settling time is t_s = 4/(0.44·2.0) "
        "= 4.5 s. (e) The number of oscillations within the 2% settling time is 2·0.44/√(1−0.44²) = 1.3."))
    b.append(p(
        "The feedback system shown in Figure 4.5 has a forward path K/[s(s+a)] and a feedback path 1. The closed "
        "loop transfer function is:"))
    b.append(eq("G(s) = K / (s² + a s + K)", "4.17"))
    b.append(p(
        "By comparison with the standard second-order form, ωn = √K and ζ = a/(2√K). Since ωd·t_r = π/2, t_r = "
        "π/(2ωn√(1−ζ²)) — the rise time decreases as K increases (faster response). The percentage overshoot = "
        "exp(−ζπ/√(1−ζ²)) increases as K increases. The 2% settling time t_s = 4/(ζωn) = 4/a — <b>independent of "
        "the gain K</b>."))
    b.append(fig(5, F.fig_4_5()))

    # 4.4
    b.append(h2("4.4 Stability", "Stability"))
    b.append(p(
        "We define a stable system as one which, when given an input or a change in input, has transients which "
        "die away with time and leave the system in a steady state condition. The system is unstable if the "
        "transients do not die away but grow with time."))
    b.append(p(
        "Consider a second order system G(s) = 1/[(s+1)(s+2)]. The values of s which make the transfer function "
        "infinite are termed the <b>poles</b> — here s = −1 and s = −2. A unit step input gives an output with "
        "terms e^(−t) and e^(−2t), both decaying to leave a steady state value of 0.5 — the system is stable. "
        "Now consider G(s) = 1/[(s−1)(s−2)] with poles s = +1 and +2, giving e^(+t) and e^(+2t) which grow — the "
        "system is unstable. Thus: <b>a negative pole gives a transient which dies away (stable); a positive pole "
        "gives a transient which grows (unstable)</b>."))
    b.append(p(
        "In general, for a second order system G(s) = ωn²/[(s+p1)(s+p2)], the roots (poles) are:"))
    b.append(eq("p1 = −ζωn + ωn√(ζ²−1) ,   p2 = −ζωn − ωn√(ζ²−1)", "4.18"))
    b.append(p(
        "With ζ > 1 we have real roots; with ζ &lt; 1 we write j = √−1 and the roots become:"))
    b.append(eq("p1 = −ζωn + j ωn√(1−ζ²) ,   p2 = −ζωn − j ωn√(1−ζ²)", "4.19"))
    b.append(p(
        "We write the roots, and so poles, in the form a + jb; the jb part is an imaginary number. The same rule "
        "applies: if the a term is negative the system is stable, if positive it is unstable."))
    b.append(h3("4.4.1 The s plane", "The s plane"))
    b.append(p(
        "We can plot the positions of the poles on a graph with the real part as the x-axis and the imaginary "
        "part as the y-axis — the <b>s-plane</b>. Figures 4.6–4.10 illustrate: real negative poles (stable, "
        "overdamped), real positive poles (unstable), complex left-half poles (stable, underdamped), complex "
        "right-half poles (unstable) and a double pole (critically damped). Figure 4.11 states that <b>a system "
        "is stable if all its poles lie in the left half of the s-plane</b>. Figure 4.12 shows that the more "
        "negative the real part the more rapidly the transient dies away, and the larger the imaginary part the "
        "higher the frequency of oscillation."))
    b.append(fig(6, F.fig_4_6()))
    b.append(fig(7, F.fig_4_7()))
    b.append(fig(8, F.fig_4_8()))
    b.append(fig(9, F.fig_4_9()))
    b.append(fig(10, F.fig_4_10()))
    b.append(fig(11, F.fig_4_11()))
    b.append(fig(12, F.fig_4_12()))
    b.append(h3("Example", "Example"))
    b.append(p(
        "Which systems are stable: (a) G(s) = 1/(s²+s+1) → poles −0.5 ± j0.866 (left half) → stable; (b) G(s) = "
        "1/(s²−5s+4) → poles +4 and +1 (right half) → unstable; (c) G(s) = 1/(s²−2s+3) → poles +1 ± j√2 (right "
        "half) → unstable."))

    # Problems
    b.append(h2("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 10 problems, of which Problems 6, 7 and 9 are illustrated by block diagrams and s-planes "
        "(Figures 4.13–4.15). They include: delay and rise times for first-order systems; natural angular "
        "frequency, damping factor, rise time, percentage overshoot and 2% settling time for second-order "
        "systems; determining the gain K to give a specified rise time; and assessing stability from pole "
        "locations on the s-plane and from the differential equation."))
    b.append(fig(13, F.fig_4_13()))
    b.append(fig(14, F.fig_4_14()))
    b.append(fig(15, F.fig_4_15()))
    return "".join(b)
