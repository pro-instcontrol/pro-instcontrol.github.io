# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 6, Nyquist diagrams.

Vietnamese and English prose with all 13 redrawn vector figures (6.1–6.13):
the Cartesian/polar comparison, polar plots, the Nyquist stability criterion,
the common open-loop Nyquist forms with their stability conditions, a worked
example, and the gain/phase margin definitions on a Nyquist plot.
"""
import boltonfig6 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 6
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Biểu đồ cực (polar plot)</em> — đường cong đáp ứng tần số vẽ theo bán kính r và góc θ từ gốc. · "
            "<em>Biểu đồ Nyquist</em> — đồ thị cực của hàm truyền vòng hở G(jω)H(jω) khi ω từ 0 đến ∞. · "
            "<em>Tiêu chuẩn ổn định Nyquist</em> — quỹ đạo vòng hở không bao quanh điểm −1 thì ổn định. · "
            "<em>Dự trữ lợi / dự trữ pha</em> — đo độ ổn định tương đối trên biểu đồ Nyquist.")
    return note(
        "<b>Key terms.</b> <em>Polar plot</em> — the frequency-response locus drawn by radius r and angle θ "
        "from the origin. · <em>Nyquist diagram</em> — the polar plot of the open-loop transfer function "
        "G(jω)H(jω) as ω runs from 0 to ∞. · <em>Nyquist stability criterion</em> — a closed-loop system is "
        "stable if the open-loop locus does not encircle the −1 point. · <em>Gain/phase margin</em> — "
        "relative-stability measures read from a Nyquist plot.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này tiếp nối Chương 5 và trình bày một cách khác để xét đáp ứng tần số cùng độ ổn định của hệ: "
        "dùng biểu đồ Nyquist. Lợi và pha của hàm truyền vòng hở được vẽ dưới dạng đồ thị cực, từ đó suy ra tính "
        "ổn định và dự trữ ổn định của hệ kín."))

    # 6.1
    b.append(h2("6.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Chương này tiếp nối Chương 5 và trình bày một phương pháp khác để xét đáp ứng tần số và độ ổn định của "
        "hệ. Phương pháp dùng biểu đồ Nyquist: trong các biểu đồ này, lợi và pha của hàm truyền vòng hở — tức tích "
        "của hàm truyền đường truyền thuận và đường phản hồi — được vẽ dạng đồ thị cực ứng với các giá trị tần số "
        "khác nhau. Với đồ thị Descartes, các điểm được vẽ theo tọa độ x, y tính từ gốc; với đồ thị cực, các điểm "
        "được vẽ từ gốc tọa độ theo khoảng cách bán kính đến nó và góc so với trục tham chiếu (Hình 6.1)."))
    b.append(fig(1, F.fig_6_1()))
    b.append(p(
        "Biểu đồ cực của đáp ứng tần số một hệ là đường thẳng được vẽ bởi các đỉnh phasor khi tần số thay đổi từ 0 "
        "đến vô cực, trong đó độ dài phasor biểu diễn độ lớn (tức lợi biên độ) của hệ và góc vẽ tương ứng với pha "
        "của nó (Hình 6.2)."))
    b.append(fig(2, F.fig_6_2()))

    # 6.2
    b.append(h2("6.2 Biểu đồ cực", "The polar plot"))
    b.append(p(
        "Biểu đồ cực của đáp ứng tần số một hệ là đường được vẽ bởi các đỉnh phasor khi tần số thay đổi từ 0 đến "
        "vô cực, độ dài phasor biểu diễn độ lớn của hệ và góc tương ứng với pha."))
    b.append(h3("Ví dụ", "Example"))
    b.append(p(
        "Vẽ biểu đồ cực cho dữ liệu đáp ứng tần số sau:"))
    b.append(table(["Tần số (rad/s)", "1,4", "2,0", "2,6", "3,2", "3,8"],
                   [["Độ lớn", "1,6", "1,0", "0,6", "0,4", "0,2"],
                    ["Pha (°)", "−150", "−160", "−170", "−180", "−190"]],
                   "Dữ liệu ví dụ: độ lớn giảm, pha âm (trễ pha) khi tần số tăng."))
    b.append(p(
        "Lưu ý các pha trên mang dấu âm, nghĩa là chúng trễ pha so với đường 0° một lượng tương ứng. Hình 6.3 "
        "cho thấy biểu đồ cực thu được."))
    b.append(fig(3, F.fig_6_3()))
    b.append(h3("6.2.1 Biểu đồ Nyquist", "Nyquist diagrams"))
    b.append(p(
        "Thuật ngữ <b>biểu đồ Nyquist (Nyquist diagram)</b> được dùng cho: đường nối dãy các điểm được vẽ trên "
        "đồ thị cực, mỗi điểm biểu diễn độ lớn và pha của đáp ứng tần số vòng hở ứng với một tần số nhất định. "
        "Để vẽ biểu đồ Nyquist từ hàm truyền vòng hở, ta cần xác định độ lớn và pha theo hàm của tần số."))
    b.append(h4("Ví dụ — hệ bậc nhất"))
    b.append(p(
        "Xác định biểu đồ Nyquist cho hệ bậc nhất có hàm truyền vòng hở 1/(1+τs). Đáp ứng tần số là:"))
    b.append(eq(r"G(j\omega)=\frac{1}{1+j\omega\tau}=\frac{1-j\omega\tau}{1+\omega^2\tau^2}"
                r"=-\frac{j\omega\tau}{1+\omega^2\tau^2}+\frac{1}{1+\omega^2\tau^2}", "6.1"))
    b.append(p(
        "Độ lớn là 1/√(1+ω²τ²), pha là −tan⁻¹(ωτ). Tại tần số không, độ lớn bằng 1 và pha 0°; tại tần số vô cực, "
        "độ lớn bằng 0 và pha −90°. Khi ωτ = 1 thì độ lớn là 1/√2 và pha −45°. Thế các giá trị khác dẫn đến đường "
        "cong nửa đường tròn như Hình 6.4."))
    b.append(fig(4, F.fig_6_4()))
    b.append(h4("Ví dụ — 1/s(s+1)"))
    b.append(p(
        "Xác định biểu đồ Nyquist cho hệ có hàm truyền vòng hở 1/[s(s+1)]. Đáp ứng tần số:"))
    b.append(eq(r"G(j\omega)=\frac{1}{j\omega(j\omega+1)}"
                r"=\frac{-j\omega-\omega^2}{\omega^2(\omega^2+1)}"
                r"=-\frac{1}{\omega^2+1}-j\frac{\omega}{\omega^2+1}", "6.2"))
    b.append(p(
        "độ lớn và pha lần lượt là 1/[ω√(ω²+1)] và 180°+tan⁻¹(1/ω). Khi ω = 0 thì độ lớn 0 và pha 0°; khi ω tiến "
        "tới 0 thì độ lớn tiến tới vô cực và pha tiến tới 270° (hay −90°). Hình 6.5 cho thấy biểu đồ cực."))
    b.append(fig(5, F.fig_6_5()))

    # 6.3
    b.append(h2("6.3 Ổn định", "Stability"))
    b.append(p(
        "Như đã chỉ ra ở Mục 5.6, điểm tới hạn phân biệt hệ ổn định và không ổn định là khi dịch pha vòng hở bằng "
        "−180° và độ lớn vòng hở bằng 1. Nếu vẽ một biểu đồ Nyquist của đáp ứng tần số vòng hở thì để hệ ổn định, "
        "không được có phasor nào có độ dài lớn hơn 1 và pha −180°. Nói cách khác, đường được vẽ bởi các đỉnh "
        "phasor — gọi là quỹ đạo (loci) — không được bao quanh điểm −1."))
    b.append(p(
        "<b>Các hệ kín có quỹ đạo đáp ứng tần số vòng hở G(jω)H(jω), khi ω chạy từ 0 đến ∞, không bao quanh điểm "
        "−1 thì ổn định; những hệ bao quanh điểm −1 thì không ổn định; những hệ đi qua điểm −1 thì ở biên ổn "
        "định.</b> Bao quanh điểm có thể hiểu là đi qua bên trái điểm đó. Phát biểu trên gọi là <b>tiêu chuẩn ổn "
        "định Nyquist</b>."))
    b.append(p(
        "Hình 6.6 minh họa bằng các ví dụ hệ ổn định, ở biên ổn định và không ổn định. (Các biểu đồ Nyquist không "
        "theo tỉ lệ, tương ứng với đáp ứng tần số vòng hở G(jω)H(jω) = K/[(1+j0,2ω)(1+jω)(1+j0,1ω)] với K=10 cho "
        "biểu đồ ổn định, K=137 ở biên ổn định, K=500 không ổn định.)"))
    b.append(fig(6, F.fig_6_6()))
    b.append(p(
        "Trục thẳng đứng của biểu đồ Nyquist tương ứng với pha bằng 90°, tức là phần ảo của đáp ứng tần số vòng "
        "hở. Trục nằm ngang tương ứng với pha bằng 0°, tức là phần thực của đáp ứng tần số vòng hở. Các Hình 6.7 "
        "đến 6.10 cho các ví dụ biểu đồ Nyquist của những dạng hàm truyền vòng hở phổ biến cùng điều kiện ổn định "
        "của chúng."))
    b.append(fig(7, F.fig_6_7()))
    b.append(fig(8, F.fig_6_8()))
    b.append(fig(9, F.fig_6_9()))
    b.append(fig(10, F.fig_6_10()))
    b.append(h4("Ví dụ — K/[(s+1)(s+2)(s+3)]"))
    b.append(p(
        "Vẽ biểu đồ Nyquist cho hệ có hàm truyền vòng hở K/[(s+1)(s+2)(s+3)] và xét giá trị K để hệ ổn định. "
        "Đáp ứng tần số vòng hở:"))
    b.append(eq(r"G(j\omega)H(j\omega)=\frac{K}{(j\omega+1)(j\omega+2)(j\omega+3)}", "6.3"))
    b.append(p(
        "độ lớn và pha lần lượt là K/√[(ω²+1)(ω²+4)(ω²+9)] và [tan⁻¹(−ω)+tan⁻¹(−ω/2)+tan⁻¹(−ω/3)]. Khi ω=0 thì "
        "độ lớn K/6, pha 0°; khi ω=∞ thì độ lớn 0, pha 270°. Hoặc xét theo phần thực và phần ảo:"))
    b.append(eq(r"G(j\omega)H(j\omega)=\frac{6K(1-\omega^2)}{(\omega^2+1)(\omega^2+4)(\omega^2+9)}"
                r"+j\frac{\omega K(\omega^2-11)}{(\omega^2+1)(\omega^2+4)(\omega^2+9)}", "6.4"))
    b.append(p(
        "Khi ω=0 thì phần ảo bằng 0, phần thực K/6; khi ω=∞ thì phần ảo 0, phần thực 0. Phần ảo bằng 0 khi "
        "ω=√11, khi đó phần thực (và độ lớn) là −K/60 — chính là điểm cắt trục thực. Vậy để hệ ổn định phải có "
        "−K/60 < −1, tức K < 60. Hình 6.11 cho biểu đồ Nyquist hoàn chỉnh."))
    b.append(fig(11, F.fig_6_11()))

    # 6.4
    b.append(h2("6.4 Ổn định tương đối", "Relative stability"))
    b.append(p(
        "Việc dùng dự trữ lợi và dự trữ pha đã được giới thiệu ở Mục 5.6.1 để bàn về độ ổn định tương đối của hệ "
        "trong miền tần số khi biểu diễn bằng Bode. Với biểu đồ Nyquist:"))
    b.append(h3("Dự trữ lợi", "Gain margin"))
    b.append(p(
        "Tần số cắt pha là tần số đầu tiên mà góc pha đạt −180°, tức là điểm biểu đồ Nyquist cắt trục thực (Hình "
        "6.12). Trên biểu đồ Nyquist, điểm (−1, j0) là điểm phân biệt ổn định và không ổn định. Dự trữ lợi là lượng "
        "phải nhân lợi thực tế lên trước khi mất ổn định. Vậy nếu đường cắt trục thực âm tại −x (Hình 6.12), nó "
        "phải được nhân với 1/x để đạt giá trị −1, và dự trữ lợi (tính bằng dB) là 20 lg(1/x)."))
    b.append(p(
        "Khi đường vòng hở đi qua điểm (−1, j0) thì dự trữ lợi là 0 dB (ở biên ổn định). Khi đi qua bên trái "
        "(−1, j0) thì dự trữ lợi âm (không ổn định). Khi đi qua bên phải thì dự trữ lợi dương (ổn định). Khi "
        "đường vòng hở không giao trục thực âm thì dự trữ lợi là vô cực (dB)."))
    b.append(fig(12, F.fig_6_12()))
    b.append(h3("Dự trữ pha", "Phase margin"))
    b.append(p(
        "Dự trữ pha là góc (độ) mà góc pha nhỏ hơn −180° tại tần số cắt lợi — tần số mà lợi vòng hở đạt 1 lần "
        "đầu tiên. Vậy trên biểu đồ Nyquist, nếu vẽ một đường tròn bán kính 1 tâm tại gốc, điểm nó cắt đường Nyquist "
        "chính là điểm cắt lợi. Dự trữ pha là góc phải quay đường cắt lợi đó quanh gốc tọa độ để chạm trục thực và "
        "đi qua điểm (−1, j0) (Hình 6.13)."))
    b.append(fig(13, F.fig_6_13()))
    b.append(h4("Ví dụ — K/[(s+1)(s+2)(s+3)] với K=20"))
    b.append(p(
        "Xác định dự trữ lợi và dự trữ pha cho hệ có hàm truyền vòng hở K/[(s+1)(s+2)(s+3)] với K=20 (đã xét ở "
        "Hình 6.11). Viết lại dạng thực/ảo, phần ảo bằng 0 khi ω=√11, phần thực khi đó là −K/60 = −20/60 = −1/3. "
        "Lợi có thể tăng hệ số 3 để tới điểm −1, nên dự trữ lợi = 20 lg 3 = 9,5 dB."))
    b.append(p(
        "Độ lớn = K/√[(ω²+1)(ω²+4)(ω²+9)]; với K=20, độ lớn bằng 1 khi ω=1,84 rad/s. Pha tại tần số này là "
        "−135,5°, nên dự trữ pha = 44,5°."))

    # Problems
    b.append(h2("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 6 bài tập: phác họa biểu đồ Nyquist (Bài 1); điều kiện ổn định trên biểu đồ Nyquist (Bài 2); "
        "xác định dự trữ lợi/dự trữ pha từ dữ liệu thực nghiệm (Bài 3, 4); và từ hàm truyền vòng hở cho trước "
        "K=4 (Bài 5) hoặc dạng s(0,2s+1)(0,05s+1) (Bài 6). Các bài không minh họa bằng hình trong bản gốc."))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter follows Chapter 5 and presents another method of considering the frequency response of "
        "systems and their stability: Nyquist diagrams. The gain and phase of the open-loop transfer function are "
        "plotted as a polar graph, from which the stability and relative stability of the closed-loop system follow."))

    # 6.1
    b.append(h2("6.1 Introduction", "Introduction"))
    b.append(p(
        "This chapter follows on from Chapter 5 and presents another method of considering the frequency response "
        "of systems and their stability. The method uses Nyquist diagrams; in these diagrams the gain and the phase "
        "of the open-loop transfer function, i.e. the product of the forward-path and feedback-path transfer "
        "functions, are plotted as polar graphs for various values of frequency. With Cartesian graphs the points "
        "are plotted according to their x and y coordinates from the origin; with a polar graph the points are "
        "plotted from the origin according to their radial distance from it and their angle to the reference axis "
        "(Figure 6.1)."))
    b.append(fig(1, F.fig_6_1()))
    b.append(p(
        "The polar plot of the frequency response of a system is the line traced out as the frequency is changed "
        "from 0 to infinity by the tips of the phasors whose lengths represent the magnitude, i.e. amplitude gain, "
        "of the system and which are drawn at angles corresponding to their phase (Figure 6.2)."))
    b.append(fig(2, F.fig_6_2()))

    # 6.2
    b.append(h2("6.2 The polar plot", "The polar plot"))
    b.append(p(
        "The polar plot of the frequency response of a system is the line traced out as the frequency is changed "
        "from 0 to infinity by the tips of the phasors, the length of a phasor representing the magnitude of the "
        "system and the angle its phase."))
    b.append(h3("Example", "Example"))
    b.append(p(
        "Draw the polar diagram for the following frequency response data."))
    b.append(table(["Frequency (rad/s)", "1.4", "2.0", "2.6", "3.2", "3.8"],
                   [["Magnitude", "1.6", "1.0", "0.6", "0.4", "0.2"],
                    ["Phase (deg.)", "-150", "-160", "-170", "-180", "-190"]],
                   "Example data: magnitude falls and phase is negative (lagging) as frequency rises."))
    b.append(p(
        "Note that the above data gives the phases with negative signs, meaning they lag behind the 0° line by the "
        "amounts given. Figure 6.3 shows the polar plot obtained."))
    b.append(fig(3, F.fig_6_3()))
    b.append(h3("6.2.1 Nyquist diagrams", "Nyquist diagrams"))
    b.append(p(
        "The term <b>Nyquist diagram</b> is used for the line joining the series of points plotted on a polar graph "
        "when each point represents the magnitude and phase of the open-loop frequency response corresponding to a "
        "particular frequency. To plot the Nyquist diagram from the open-loop transfer function of a system we need "
        "to determine the magnitude and the phase as functions of frequency."))
    b.append(h4("Example — first-order system"))
    b.append(p(
        "Determine the Nyquist diagram for a first-order system with an open-loop transfer function of 1/(1+τs). "
        "The frequency response is:"))
    b.append(eq(r"G(j\omega)=\frac{1}{1+j\omega\tau}=\frac{1-j\omega\tau}{1+\omega^2\tau^2}"
                r"=-\frac{j\omega\tau}{1+\omega^2\tau^2}+\frac{1}{1+\omega^2\tau^2}", "6.1"))
    b.append(p(
        "The magnitude is thus 1/√(1+ω²τ²) and the phase is −tan⁻¹(ωτ). At zero frequency the magnitude is 1 and the "
        "phase 0°; at infinite frequency the magnitude is zero and the phase −90°. When ωτ = 1 the magnitude is "
        "1/√2 and the phase is −45°. Substitution of other values leads to the semicircular plot shown in Figure "
        "6.4."))
    b.append(fig(4, F.fig_6_4()))
    b.append(h4("Example — 1/s(s+1)"))
    b.append(p(
        "Determine the Nyquist plot for the system having the open-loop transfer function of 1/[s(s+1)]. The "
        "frequency response is:"))
    b.append(eq(r"G(j\omega)=\frac{1}{j\omega(j\omega+1)}"
                r"=\frac{-j\omega-\omega^2}{\omega^2(\omega^2+1)}"
                r"=-\frac{1}{\omega^2+1}-j\frac{\omega}{\omega^2+1}", "6.2"))
    b.append(p(
        "the magnitude and phase are thus 1/[ω√(ω²+1)] and 180°+tan⁻¹(1/ω). When ω = 0 then the magnitude is 0 and "
        "the phase is 0°; as ω tends to 0 then the magnitude tends to infinity and the phase to 270° (or −90°). "
        "Figure 6.5 shows the polar plot."))
    b.append(fig(5, F.fig_6_5()))

    # 6.3
    b.append(h2("6.3 Stability", "Stability"))
    b.append(p(
        "As indicated in Section 5.6: the critical point which separates stable from unstable systems is when the "
        "open-loop phase shift is −180° and the open-loop magnitude is 1. If a Nyquist diagram of the open-loop "
        "frequency response is plotted then for the system to be stable there must not be any phasor with length "
        "greater than 1 and phase −180°. Thus the line traced by the tips of the phasors, the so-termed loci, must "
        "not enclose the −1 point."))
    b.append(p(
        "<b>Closed-loop systems whose open-loop frequency response G(jω)H(jω) loci, as ω goes from 0 to ∞, do not "
        "encircle the −1 point will be stable, those which encircle the −1 point are unstable and those which pass "
        "through the −1 point are marginally stable.</b> Encircling the point may be taken as passing to the left of "
        "the point. The above statement is known as the Nyquist stability criterion."))
    b.append(p(
        "Figure 6.6 illustrates the above with examples of stable, marginally stable and unstable systems (the "
        "Nyquist plots, not to scale, correspond to the open-loop frequency response "
        "G(jω)H(jω)=K/[(1+j0.2ω)(1+jω)(1+j0.1ω)] with K=10 for the stable plot, K=137 for the marginally stable "
        "plot and K=500 for the unstable plot)."))
    b.append(fig(6, F.fig_6_6()))
    b.append(p(
        "The vertical axis of the Nyquist plot corresponds to the phase equal to 90° and so is the imaginary part "
        "of the open-loop frequency response. The horizontal axis corresponds to the phase equal to 0° and so is "
        "the real part of the open-loop frequency response. Figures 6.7 to 6.10 show examples of Nyquist plots for "
        "common forms of open-loop transfer functions and their conditions for stability."))
    b.append(fig(7, F.fig_6_7()))
    b.append(fig(8, F.fig_6_8()))
    b.append(fig(9, F.fig_6_9()))
    b.append(fig(10, F.fig_6_10()))
    b.append(h4("Example — K/[(s+1)(s+2)(s+3)]"))
    b.append(p(
        "Plot the Nyquist diagram for a system with the open-loop transfer function K/[(s+1)(s+2)(s+3)] and consider "
        "the value of K needed for stability. The open-loop frequency response is:"))
    b.append(eq(r"G(j\omega)H(j\omega)=\frac{K}{(j\omega+1)(j\omega+2)(j\omega+3)}", "6.3"))
    b.append(p(
        "The magnitude and phase are K/√[(ω²+1)(ω²+4)(ω²+9)] and [tan⁻¹(−ω)+tan⁻¹(−ω/2)+tan⁻¹(−ω/3)]. When ω = 0 "
        "then the magnitude is K/6 and the phase 0°; when ω = ∞ then the magnitude is 0 and the phase 270°. We can "
        "write the open-loop frequency function in real and imaginary parts:"))
    b.append(eq(r"G(j\omega)H(j\omega)=\frac{6K(1-\omega^2)}{(\omega^2+1)(\omega^2+4)(\omega^2+9)}"
                r"+j\frac{\omega K(\omega^2-11)}{(\omega^2+1)(\omega^2+4)(\omega^2+9)}", "6.4"))
    b.append(p(
        "When ω = 0 then the imaginary part is zero and the real part is K/6; when ω = ∞ then the imaginary part is "
        "zero and the real part is 0. The imaginary part will be zero when ω = √11; this gives a real part, and "
        "hence magnitude, of −K/60 — the point at which the plot crosses the real axis. Thus for a stable system we "
        "must have −K/60 less than −1, i.e. K must be less than 60. Figure 6.11 shows the complete Nyquist plot."))
    b.append(fig(11, F.fig_6_11()))

    # 6.4
    b.append(h2("6.4 Relative stability", "Relative stability"))
    b.append(p(
        "The use of gain margin and phase margin was introduced in Section 5.6.1 to discuss the relative stability "
        "of a system in the frequency domain when described by a Bode plot. With Nyquist plots:"))
    b.append(h3("Gain margin", "Gain margin"))
    b.append(p(
        "The phase crossover frequency is the frequency at which the phase angle first reaches −180° and thus is "
        "the point where the Nyquist plot crosses the real axis (Figure 6.12). On a Nyquist plot the (−1, j0) point "
        "is the point separating stability from instability. The gain margin is the amount by which the actual gain "
        "must be multiplied before the onset of instability. Thus if the plot cuts the negative real axis at −x "
        "(Figure 6.12), it has to be multiplied by 1/x to give the value −1 and so the gain margin, which is "
        "expressed in dB, is 20 lg(1/x)."))
    b.append(p(
        "When the open-loop plot goes through the (−1, j0) point the gain margin is 0 dB, the system being on the "
        "margin of instability. When the open-loop plot goes to the left of the (−1, j0) point the gain margin is "
        "negative in dB, the system being unstable. When the open-loop plot goes to the right of the (−1, j0) point "
        "the gain margin is positive in dB, the system being stable. When the open-loop plot does not intersect the "
        "negative real axis the gain margin is infinite in dB."))
    b.append(fig(12, F.fig_6_12()))
    b.append(h3("Phase margin", "Phase margin"))
    b.append(p(
        "The phase margin is defined as the angle in degrees by which the phase angle is smaller than −180° at the "
        "gain crossover, the gain crossover being the frequency at which the open-loop gain first reaches 1. Thus, "
        "with a Nyquist plot, if we draw a circle of radius 1 centred on the origin, then the point at which it "
        "intersects the Nyquist line gives the gain crossover. The phase margin is the angle through which this "
        "gain-crossover line must be rotated about the origin to reach the real axis and pass through the (−1, j0) "
        "point (Figure 6.13)."))
    b.append(fig(13, F.fig_6_13()))
    b.append(h4("Example — K/[(s+1)(s+2)(s+3)] with K = 20"))
    b.append(p(
        "Determine the gain margin and the phase margin for a system with the open-loop transfer function "
        "K/[(s+1)(s+2)(s+3)] with K = 20 (discussed earlier, see Figure 6.11 for the Nyquist plot). Written in "
        "real/imaginary form, the imaginary part is zero when ω = √11 and the real part is then −K/60 = −20/60 = "
        "−1/3. The gain can thus be increased by a factor of 3 to reach the −1 point, so the gain margin is "
        "20 lg 3 = 9.5 dB."))
    b.append(p(
        "The magnitude is K/√[(ω²+1)(ω²+4)(ω²+9)]; for K = 20 the magnitude is 1 when ω = 1.84 rad/s. The phase at "
        "that frequency is −135.5°, so the phase margin is 44.5°."))

    # Problems
    b.append(h2("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 6 problems: sketching the Nyquist diagram (Problem 1); stating the stability condition on "
        "a Nyquist plot (Problem 2); determining gain and phase margins from experimental data (Problems 3, 4); and "
        "from given open-loop transfer functions with K=4 (Problem 5) or of the form s(0.2s+1)(0.05s+1) (Problem 6). "
        "None of the problems is illustrated by a figure in the original."))
    return "".join(b)
