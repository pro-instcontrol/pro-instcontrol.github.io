# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 5, Frequency response.

Vietnamese and English prose with all 39 redrawn vector figures (5.1–5.23 and
5.25–5.40; 5.24 is not used in the source), the Bode-plot element tables and the
worked examples on system identification, stability margins and compensation.
"""
import boltonfig5 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 18
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Đáp ứng tần số (frequency response)</em> — đầu ra xác lập sin cùng tần số với đầu vào, khác biên độ và lệch pha. · "
            "<em>Phasor</em> — vectơ quay biểu diễn tín hiệu sin (miền tần số). · "
            "<em>Hàm đáp ứng tần số G(jω)</em> — thay s bằng jω trong hàm truyền. · "
            "<em>Biểu đồ Bode</em> — lợi (dB) và góc pha theo lôgarit tần số. · "
            "<em>Điểm gãy (break point)</em> — tần số góc ω = 1/τ. · "
            "<em>Dự trữ lợi / dự trữ pha</em> — đo độ ổn định từ Bode.")
    return note(
        "<b>Key terms.</b> <em>Frequency response</em> — the steady-state sinusoidal output, same frequency as the "
        "input but different amplitude and phase. · <em>Phasor</em> — a rotating vector representing a sinusoid "
        "(frequency domain). · <em>Frequency response function G(jω)</em> — the transfer function with s replaced "
        "by jω. · <em>Bode plot</em> — gain (dB) and phase angle versus log frequency. · <em>Break point</em> — "
        "the corner frequency ω = 1/τ. · <em>Gain/phase margin</em> — stability measures read from a Bode plot.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này xét đáp ứng xác lập của hệ khi đầu vào là tín hiệu sin — tức đáp ứng tần số. Từ hàm truyền "
        "ta thu được hàm đáp ứng tần số G(jω), rồi biểu diễn lợi và góc pha bằng biểu đồ Bode. Chương kết thúc "
        "bằng nhận dạng hệ, các tiêu chuẩn ổn định và kỹ thuật bù."))

    # 5.1
    b.append(h2("5.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Các chương trước xét đầu ra ứng với đầu vào bậc, xung, dốc. Chương này xét đáp ứng xác lập khi đầu vào là "
        "tín hiệu sin. Khi tần số đầu vào sin thay đổi, biên độ và góc pha của đầu ra cũng thay đổi — sự biến thiên "
        "này gọi là <b>đáp ứng tần số (frequency response)</b> của hệ, và có thể biểu diễn bằng biểu đồ Bode."))
    b.append(p(
        "Ta có thể suy ra đáp ứng tần số từ hàm truyền đã biết, hoặc ngược lại — dùng thí nghiệm với đầu vào sin để "
        "xác định đáp ứng tần số rồi từ đó suy ra dạng hàm truyền. Chương chỉ ra cách có được thông tin tần số từ "
        "hàm truyền và trình bày bằng Bode, sau đó dùng Bode thực nghiệm để ước lượng hàm truyền, và cuối cùng là "
        "các tham số ổn định cùng kỹ thuật bù."))

    # 5.2
    b.append(h2("5.2 Phasor", "Phasors"))
    b.append(p(
        "Khi nói về tín hiệu sin, một cách tiện lợi là dùng <b>phasor</b>: tưởng tượng tín hiệu y = Y sin ωt được tạo "
        "bởi một đoạn thẳng độ dài Y quay với vận tốc góc ω, và hình chiếu theo phương thẳng đứng của đoạn thẳng tại "
        "mỗi thời điểm chính là giá trị tín hiệu sin (Hình 5.1). Nếu tín hiệu lệch pha, đoạn thẳng bắt đầu tại một "
        "góc so với trục tham chiếu (thường là trục ngang) — góc đó gọi là góc pha. Cách biểu diễn này gọi là trong "
        "miền tần số."))
    b.append(fig(1, F.fig_5_1()))
    b.append(p(
        "Một số phức z = a + jb được biểu diễn trên mặt phẳng Argand (hình chiếu ảo theo trục tung, thực theo trục "
        "hoành) bởi một đoạn thẳng độ dài |z| và góc θ (Hình 5.2). Độ lớn |z| = √(a²+b²), góc θ = tan⁻¹(b/a). Ta "
        "cũng dùng phasor để biểu diễn lượng sin: y = Y sin ωt chỉ có phần thực (Hình 5.3(a)); y = Y sin(ωt+θ) có "
        "cả thực và ảo (Hình 5.3(b)); θ = 90° cho phasor chỉ có phần ảo (Hình 5.3(c)). Phasor quay 90° tương ứng "
        "nhân với j, quay 180° nhân j² = −1, quay 270° nhân j³ = −j (Hình 5.4)."))
    b.append(fig(2, F.fig_5_2()))
    b.append(fig(3, F.fig_5_3()))
    b.append(fig(4, F.fig_5_4()))
    b.append(p(
        "Ví dụ: phasor j3 có độ lớn 3, pha 90° (chỉ có phần ảo); phasor 1 + j2 có độ lớn √(1²+2²) = 2,2, pha "
        "tan⁻¹(2/1) = 63,4°."))

    # 5.3
    b.append(h2("5.3 Đầu vào sin", "Sinusoidal inputs"))
    b.append(p(
        "Với một hệ điện (như mạch trở–tụ nối tiếp, Hình 5.5), đầu vào sin cho đầu ra cũng sin, cùng tần số nhưng "
        "có thể khác biên độ và lệch pha. Quan hệ này áp dụng cho mọi loại hệ: <b>đáp ứng tần số là đáp ứng xác lập "
        "của hệ với đầu vào sin — đầu ra là tín hiệu sin cùng tần số với đầu vào, chỉ khác biên độ và góc pha</b> "
        "(Hình 5.6)."))
    b.append(fig(5, F.fig_5_5()))
    b.append(fig(6, F.fig_5_6()))
    b.append(h3("5.3.1 Hàm đáp ứng tần số", "Frequency response function"))
    b.append(p(
        "Xét hệ y = kx với đầu vào x = sin ωt → y = k sin ωt. Biểu diễn bằng phasor: phasor đầu ra / phasor đầu vào = "
        "k. Với hệ τ·dy/dt + y = kx, thay x = y = sin ωt và dy/dt = ω cos ωt = ω sin(ωt+90°) ta được jωτY + Y = kX, "
        "nên Y/X = k/(1+jωτ). Tổng quát, <b>hàm đáp ứng tần số thu được bằng cách thay s bằng jω trong hàm truyền</b>, "
        "ký hiệu G(jω). Ví dụ G(s) = 5/(2+s) → G(jω) = 5/(2+jω)."))
    b.append(h3("5.3.2 Hệ bậc nhất", "First-order systems"))
    b.append(p(
        "G(s) = 1/(1+τs) → G(jω) = 1/(1+jωτ) = (1−jωτ)/(1+ω²τ²). Viết dạng a+jb: phần thực 1/(1+ω²τ²), phần ảo "
        "−ωτ/(1+ω²τ²). Lợi (gain) |G(jω)| = 1/√(1+ω²τ²); góc pha tan φ = b/a = −ωτ (âm → đầu ra trễ pha so với "
        "đầu vào). Ví dụ G(s)=2/(s+1), đầu vào 2 sin 3t: |G| = 2/√(3²+1) = 0,63, φ = tan⁻¹(−3) = −72° → đầu ra "
        "1,26 sin(3t−72°)."))
    b.append(h3("5.3.3 Hệ bậc hai", "Second-order systems"))
    b.append(p(
        "G(s) = ωn²/(s²+2ζωn s+ωn²) → G(jω) = ωn²/[(ωn²−ω²)+j2ζωnω]. Lợi |G(jω)| và góc pha φ = −tan⁻¹[2ζωnω/(ωn²−ω²)] "
        "(âm → đầu ra trễ pha). Cũng như hệ bậc nhất, đưa G(jω) về dạng a+jb rồi lợi = √(a²+b²), pha = tan⁻¹(b/a)."))

    # 5.4
    b.append(h2("5.4 Biểu đồ Bode", "Bode plots"))
    b.append(p(
        "Đáp ứng tần số được mô tả bởi lợi và góc pha khi tần số đầu vào thay đổi. <b>Biểu đồ Bode</b> là cặp đồ thị: "
        "lôgarit cơ số 10 của lợi theo lôgarit tần số, và góc pha theo lôgarit tần số. Ưu điểm: đồ thị của một hàm "
        "phức được cộng từ đồ thị của từng thành phần (vì tích lợi → tổng lôgarit lợi). Hình 5.7 minh họa các hệ "
        "nối tiếp: lợi tổng = tích các lợi, pha tổng = tổng các pha."))
    b.append(fig(7, F.fig_5_7()))
    b.append(p(
        "Lợi thường biểu diễn bằng đềxiben (dB): <b>lợi dB = 20 lg|G(jω)|</b>. Vậy lợi 3 tương đương 9,5 dB; lợi 10 "
        "tương đương 20 dB. Chỉ cần biết dạng Bode của một số ít thành phần: hằng số K, 1/sⁿ, sᵐ, 1/(1+τs), (1+τs), "
        "ωn²/(s²+2ζωn s+ωn²), và (s²+2ζωn s+ωn²)/ωn²."))
    b.append(h3("5.4.1 Hàm truyền hằng số", "Constant transfer function"))
    b.append(p("G(s)=K → G(jω)=K. Lợi |G|=K (dB: 20 lg K); pha 0° nếu K>0, −180° nếu K<0 (Hình 5.8). Với K=10: lợi không đổi 20 dB, pha 0°."))
    b.append(fig(8, F.fig_5_8()))
    b.append(h3("5.4.2 Hàm truyền 1/sⁿ", "Transfer function 1/sⁿ"))
    b.append(p("G(s)=1/sⁿ → G(jω)=1/(jω)ⁿ. Lợi = −20n lg ω dB (dốc −20n dB/thập kỷ), pha −n·90° (Hình 5.9). Tại ω=1 lợi 0 dB."))
    b.append(fig(9, F.fig_5_9()))
    b.append(h3("5.4.3 Hàm truyền sᵐ", "Transfer function sᵐ"))
    b.append(p("G(s)=sᵐ (zero tại gốc) → lợi = +20m lg ω dB (dốc +20m dB/thập kỷ), pha +m·90° (Hình 5.10)."))
    b.append(fig(10, F.fig_5_10()))
    b.append(h3("5.4.4 Hàm truyền 1/(1+τs)", "Transfer function 1/(1+τs)"))
    b.append(p(
        "G(s)=1/(1+τs) (cực tại s=−1/τ). Lợi dB = −10 lg(1+ω²τ²); pha = −tan⁻¹(ωτ). Ở tần thấp (ω≪1/τ) lợi 0 dB; ở "
        "tần cao (ω≫1/τ) lợi dốc −20 dB/thập kỷ, cắt trục 0 dB tại ω=1/τ — giao điểm gọi là <b>điểm gãy (break "
        "point)</b> hay tần số góc. Hai đường thẳng này là xấp xỉ tiệm cận (asymptote), sai số lớn nhất 3 dB tại điểm "
        "gãy; pha 0°→−90°, bằng −45° tại điểm gãy (Hình 5.11, Bảng 5.1). Ví dụ 100/(s+100)=1/(1+s/100), điểm gãy "
        "100 rad/s (Hình 5.12)."))
    b.append(fig(11, F.fig_5_11()))
    b.append(fig(12, F.fig_5_12()))
    b.append(h3("5.4.5 Hàm truyền (1+τs)", "Transfer function (1+τs)"))
    b.append(p(
        "G(s)=(1+τs) (zero tại s=1/τ). Lợi dB = +10 lg(1+ω²τ²); pha = +tan⁻¹(ωτ). Ở tần thấp lợi 0 dB; tần cao dốc "
        "+20 dB/thập kỷ, giao trục 0 dB tại ω=1/τ; pha 0°→+90°, +45° tại điểm gãy (Hình 5.13)."))
    b.append(fig(13, F.fig_5_13()))
    b.append(h3("5.4.6 Hệ bậc hai (cực phức và zero phức)", "Second-order terms"))
    b.append(p(
        "G(s)=ωn²/(s²+2ζωn s+ωn²) (cặp cực phức). Lợi dB = −10 lg{[1−(ω/ωn)²]²+[2ζ(ω/ωn)]²}; pha = −tan⁻¹[2ζ(ω/ωn)/(1−"
        "(ω/ωn)²)]. Ở ω≪ωn lợi 0 dB; ω≫ωn dốc −40 dB/thập kỷ; điểm gãy tại ω/ωn=1, hình dạng phụ thuộc ζ (Hình 5.14, "
        "Bảng 5.2, 5.3). Ví dụ 100/(s²+4s+100): ωn=10, ζ=0,2, sai số +8 dB tại điểm gãy (Hình 5.15). Với (s²+2ζωn "
        "s+ωn²)/ωn² (cặp zero phức), lợi và pha là ảnh đối xứng qua trục 0 của Hình 5.14."))
    b.append(fig(14, F.fig_5_14()))
    b.append(fig(15, F.fig_5_15()))
    b.append(p(
        "Ví dụ tổng hợp: G(s)=50(s+2)/[s(s+10)] = 10 × (1+s/2) × 1/s × 1/(1+s/10). Vẽ Bode từng thành phần rồi cộng "
        "(Hình 5.16): hằng số 10 (20 dB, pha 0), (1+s/2) (+20 dB/dec, điểm gãy 2 rad/s), 1/s (−20 dB/dec), 1/(1+s/10) "
        "(−20 dB/dec, điểm gãy 10 rad/s)."))

    # 5.5
    b.append(h2("5.5 Nhận dạng hệ", "System identification"))
    b.append(p(
        "Nhận dạng hệ là tìm mô hình toán học từ đáp ứng thực nghiệm. Một cách hữu ích: dùng đầu vào sin trên dải "
        "tần số, vẽ Bode thực nghiệm, rồi tìm các thành phần Bode khớp bằng cách vẽ đường tiệm cận và xét độ dốc:"))
    b.append(ul([
        "Độ dốc ban đầu bằng 0 → không có s hay 1/s; K lấy từ lợi tần thấp (dB = 20 lg K).",
        "Độ dốc ban đầu −20 dB/thập kỷ → có 1/s.",
        "Tại điểm gãy độ dốc giảm thêm −20 dB/thập kỷ → thêm (1+s/ωc) ở mẫu.",
        "Tại điểm gãy độ dốc tăng thêm +20 dB/thập kỷ → thêm (1+s/ωc) ở tử.",
        "Độ dốc giảm/thêm −40/+40 dB/thập kỷ → thêm tử hoặc mẫu bậc hai; ζ lấy từ hành vi đầu vào bậc.",
    ]))
    b.append(p(
        "Ví dụ Hình 5.17: độ dốc ban đầu 0, lợi 20 dB → K=10; gãy −20 dB/dec tại 10 rad/s → G(s)=10/(1+0,1s). Hình "
        "5.18: dốc −20 dB/dec (1/s), K=2 (6 dB tại ω=1), gãy tại 1 và 10 rad/s → 2/[s(1+s)(1+0,1s)]. Hình 5.19: "
        "lợi 10 dB (K≈3,2), gãy −40 dB/dec tại 1 rad/s, đỉnh thực cao ~4 dB → ζ≈0,3 → 3,2/(s²+0,6s+1)."))
    b.append(fig(16, F.fig_5_16()))
    b.append(fig(17, F.fig_5_17()))
    b.append(fig(18, F.fig_5_18()))
    b.append(fig(19, F.fig_5_19()))

    # 5.6
    b.append(h2("5.6 Ổn định", "Stability"))
    b.append(p(
        "Xét một hệ vòng kín (Hình 5.20) khi có một xung ngắn. Nếu tín hiệu phản hồi có biên độ nhỏ hơn xung đầu → "
        "tắt dần (ổn định, Hình 5.22); bằng → dao động biên ổn định (Hình 5.21); lớn hơn → dao động tăng (không ổn "
        "định, Hình 5.23). Điều kiện mất ổn định: lợi vòng hở G(s)H(s) > 1 và tín hiệu phản hồi lệch pha −180°. "
        "<b>Điểm tới hạn phân biệt ổn định và không ổn định là khi dịch pha vòng hở = −180° và lợi vòng hở = 1.</b>"))
    b.append(fig(20, F.fig_5_20()))
    b.append(fig(21, F.fig_5_21()))
    b.append(fig(22, F.fig_5_22()))
    b.append(fig(23, F.fig_5_23()))
    b.append(h3("5.6.1 Các thông số ổn định", "Stability measures"))
    b.append(ul([
        "<b>Tần số cắt pha (phase crossover):</b> tần số đầu tiên mà pha đạt −180°.",
        "<b>Dự trữ lợi (gain margin):</b> hệ số phải nhân lợi tại tần số cắt pha để đạt 1. Hệ tốt thường có dự trữ lợi 2–2,5.",
        "<b>Tần số cắt lợi (gain crossover):</b> tần số đầu tiên lợi vòng hở đạt 1 (0 dB).",
        "<b>Dự trữ pha (phase margin):</b> số độ pha còn nhỏ hơn −180° tại tần số cắt lợi. Hệ tốt thường 45°–65°.",
    ]))
    b.append(p(
        "Trên Bode lợi (dB), lợi 1 chính là 0 dB. Hình 5.25 minh họa các thông số; Hình 5.26(a) ổn định (lợi <0 dB "
        "tại −180°), (b) không ổn định (lợi >0 dB tại −180°). Ví dụ Hình 5.27: hệ ổn định, dự trữ lợi ~12 dB, dự "
        "trữ pha ~30°. Ví dụ dữ liệu thực nghiệm: tại 0,010 Hz lợi 0,45 và pha −180° → dự trữ lợi 1/0,45=2,22; tại "
        "0,005 Hz lợi 1, pha −120° → dự trữ pha 180−120=60°."))
    b.append(fig(25, F.fig_5_25()))
    b.append(fig(26, F.fig_5_26()))
    b.append(fig(27, F.fig_5_27()))

    # 5.7
    b.append(h2("5.7 Bù (Compensation)", "Compensation"))
    b.append(p(
        "Bù là hiệu chỉnh đặc tính hệ bằng cách thêm một thành phần (bộ bù) vào hệ điều khiển. Bộ bù đặt trong đường "
        "truyền thuận gọi là bộ bù nối tiếp (cascade, Hình 5.28)."))
    b.append(fig(28, F.fig_5_28()))
    b.append(h3("5.7.1 Đổi lợi", "Changing the gain"))
    b.append(p(
        "Tăng lợi dịch chuyển đường lợi lên trên một lượng bằng nhau mọi tần số (không ảnh hưởng pha), đẩy điểm cắt 0 "
        "dB sang tần số cao hơn → giảm dự trữ lợi và dự trữ pha (Hình 5.29, 5.30). Muốn tăng ổn định cần giảm lợi. "
        "Ví dụ Hình 5.31: dự trữ pha 35°, muốn 45° thì giảm lợi ~2 dB (ΔK=1,3)."))
    b.append(fig(29, F.fig_5_29()))
    b.append(fig(30, F.fig_5_30()))
    b.append(fig(31, F.fig_5_31()))
    b.append(h3("5.7.2 Bù sớm pha (Phase-lead)", "Phase-lead compensation"))
    b.append(p(
        "Bộ bù sớm pha có dạng G(s)=(1+aτs)/(1+τs), a>1 (mạch Hình 5.32; a=(R1+R2)/R2, τ=R1R2C/(R1+R2)). Bode (Hình "
        "5.33) có pha dương, đỉnh pha tại tần số gãy hình học ωm=1/(τ√a); độ lệch pha cực đại sin φm=(a−1)/(a+1). Dùng "
        "để tăng dự trữ pha. Ví dụ với hệ hở 10/s² (Hình 5.34, pha −180° mọi tần số): cần dự trữ pha 45° → a=5,9, "
        "τ=0,083 → G(s)=(1+0,49s)/(1+0,083s)."))
    b.append(fig(32, F.fig_5_32()))
    b.append(fig(33, F.fig_5_33()))
    b.append(fig(34, F.fig_5_34()))
    b.append(h3("5.7.3 Bù trễ pha (Phase-lag)", "Phase-lag compensation"))
    b.append(p(
        "Bộ bù trễ pha có dạng G(s)=(1+τs)/(1+aτs), a>1 (mạch Hình 5.35; a=(R1+R2)/R2, τ=R2C). Bode (Hình 5.36) có "
        "pha âm và làm giảm lợi, hạ tần số cắt — nhờ đó cải thiện ổn định ở tần số thấp hơn. Ví dụ Hình 5.37: hệ chưa "
        "bù dự trữ pha ~20°, chọn tần số cắt mới 2 rad/s (nơi dự trữ pha 40°+5°), 1/τ=0,2 → τ=5; lợi tại đó 20 dB → "
        "20 lg a=20 → a=10 → (1+5s)/(1+50s)."))
    b.append(fig(35, F.fig_5_35()))
    b.append(fig(36, F.fig_5_36()))
    b.append(fig(37, F.fig_5_37()))

    # Problems
    b.append(h2("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 16 bài tập, trong đó các Bài 6, 9, 12 minh họa bằng biểu đồ Bode (Hình 5.38–5.40). Các bài tập gồm: "
        "độ lớn/pha của phasor; hàm đáp ứng tần số; độ lớn/pha của hệ bậc nhất ứng với các tần số; phác thảo tiệm cận "
        "Bode; xác định hàm truyền từ Bode; dự trữ lợi/pha; và thiết kế bộ bù sớm/trễ pha."))
    b.append(fig(38, F.fig_5_38()))
    b.append(fig(39, F.fig_5_39()))
    b.append(fig(40, F.fig_5_40()))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter considers the steady-state response of systems when the input is a sinusoidal signal — the "
        "frequency response. From the transfer function we obtain the frequency response function G(jω) and present "
        "gain and phase on a Bode diagram. It ends with system identification, stability criteria and compensation."))

    # 5.1
    b.append(h2("5.1 Introduction", "Introduction"))
    b.append(p(
        "Earlier chapters considered the outputs that arise from step, impulse and ramp inputs. This chapter considers "
        "the steady state output responses when the inputs are sinusoidal signals. As the frequency of the input "
        "sinusoidal signal is changed, the way the amplitude and phase of the output vary is termed the <b>frequency "
        "response</b> of the system and can be described by Bode diagrams."))
    b.append(p(
        "We can derive the frequency response from a known transfer function, or conversely determine the transfer "
        "function from experimental frequency-response data. The chapter shows how frequency-response information is "
        "obtained from the transfer function and presented graphically by a Bode diagram, then how experimentally "
        "determined Bode plots are used to estimate transfer functions, and finally the parameters describing "
        "stability and compensation techniques."))

    # 5.2
    b.append(h2("5.2 Phasors", "Phasors"))
    b.append(p(
        "A convenient way to represent a sinusoidal signal y = Y sin ωt is by a phasor — imagine a radial line of "
        "length Y rotating with constant angular velocity ω (Figure 5.1); the vertical projection at any instant is "
        "the value of the sinusoid. A signal with a phase shift starts at an angle to the reference (horizontal) axis "
        "— that angle is the phase angle. This is representation in the frequency domain."))
    b.append(fig(1, F.fig_5_1()))
    b.append(p(
        "A complex number z = a + jb is represented on an Argand diagram (imaginary part against real part) by a line "
        "of length |z| at angle θ (Figure 5.2), with |z| = √(a²+b²) and θ = tan⁻¹(b/a). A sinusoid is represented by a "
        "phasor: y = Y sin ωt has only a real part (Figure 5.3(a)); y = Y sin(ωt+θ) has both real and imaginary parts "
        "(Figure 5.3(b)); θ = 90° gives a purely imaginary phasor (Figure 5.3(c)). Rotating a phasor by 90° "
        "corresponds to multiplying by j, by 180° to j² = −1, by 270° to j³ = −j (Figure 5.4)."))
    b.append(fig(2, F.fig_5_2()))
    b.append(fig(3, F.fig_5_3()))
    b.append(fig(4, F.fig_5_4()))
    b.append(p(
        "Example: the phasor j3 has magnitude 3 and, being purely imaginary, phase 90°; 1 + j2 has magnitude "
        "√(1²+2²) = 2.2 and phase tan⁻¹(2/1) = 63.4°."))

    # 5.3
    b.append(h2("5.3 Sinusoidal inputs", "Sinusoidal inputs"))
    b.append(p(
        "For an electrical system such as a resistor–capacitor series circuit (Figure 5.5), a sinusoidal input gives "
        "a sinusoidal steady-state output of the same frequency but possibly different amplitude and phase. This "
        "applies to all systems: <b>the frequency response is the steady state response to a sinusoidal input — the "
        "output is a sinusoid of the same frequency, differing only in amplitude and phase angle</b> (Figure 5.6)."))
    b.append(fig(5, F.fig_5_5()))
    b.append(fig(6, F.fig_5_6()))
    b.append(h3("5.3.1 Frequency response function", "Frequency response function"))
    b.append(p(
        "For a system y = kx with input x = sin ωt we have y = k sin ωt, so output phasor / input phasor = k. For "
        "τ·dy/dt + y = kx, substituting x = y = sin ωt and dy/dt = ω cos ωt = ω sin(ωt+90°) gives jωτY + Y = kX, hence "
        "Y/X = k/(1+jωτ). In general, <b>the frequency response function is obtained from the transfer function by "
        "replacing s by jω</b>, written G(jω). Example: G(s) = 5/(2+s) → G(jω) = 5/(2+jω)."))
    b.append(h3("5.3.2 First-order systems", "First-order systems"))
    b.append(p(
        "G(s) = 1/(1+τs) → G(jω) = 1/(1+jωτ) = (1−jωτ)/(1+ω²τ²). As a+jb: real part 1/(1+ω²τ²), imaginary part "
        "−ωτ/(1+ω²τ²). Gain |G(jω)| = 1/√(1+ω²τ²); phase tan φ = −ωτ (negative → output lags). Example G(s)=2/(s+1), "
        "input 2 sin 3t: |G| = 2/√(3²+1) = 0.63, φ = tan⁻¹(−3) = −72° → output 1.26 sin(3t−72°)."))
    b.append(h3("5.3.3 Second-order systems", "Second-order systems"))
    b.append(p(
        "G(s) = ωn²/(s²+2ζωn s+ωn²) → G(jω) = ωn²/[(ωn²−ω²)+j2ζωnω]. Gain |G(jω)| and phase φ = −tan⁻¹[2ζωnω/(ωn²−ω²)] "
        "(negative → output lags). As with first-order systems, put G(jω) in the form a+jb, then gain = √(a²+b²) and "
        "phase = tan⁻¹(b/a)."))

    # 5.4
    b.append(h2("5.4 Bode plots", "Bode plots"))
    b.append(p(
        "The frequency response is described by the gain and phase angle as the input frequency is varied. A "
        "<b>Bode plot</b> is the pair of graphs: log₁₀(gain) versus log₁₀(frequency), and phase angle versus "
        "log₁₀(frequency). The advantage is that the plot of a complex function is obtained by adding the plots of "
        "its elements (product of gains → sum of log gains). Figure 5.7 illustrates systems in series: overall gain "
        "is the product of the gains, total phase is the sum of the phases."))
    b.append(fig(7, F.fig_5_7()))
    b.append(p(
        "Gain is usually expressed in decibels (dB): <b>gain in dB = 20 lg|G(jω)|</b>. Thus a gain of 3 is 9.5 dB and "
        "a gain of 10 is 20 dB. Only a few element forms are needed: constant K, 1/sⁿ, sᵐ, 1/(1+τs), (1+τs), "
        "ωn²/(s²+2ζωn s+ωn²), and (s²+2ζωn s+ωn²)/ωn²."))
    b.append(h3("5.4.1 Constant transfer function", "Constant transfer function"))
    b.append(p("G(s)=K → G(jω)=K. Gain |G|=K (dB: 20 lg K); phase 0° if K>0, −180° if K<0 (Figure 5.8). For K=10 the gain is a constant 20 dB and the phase a constant 0°."))
    b.append(fig(8, F.fig_5_8()))
    b.append(h3("5.4.2 Transfer function 1/sⁿ", "Transfer function 1/sⁿ"))
    b.append(p("G(s)=1/sⁿ → G(jω)=1/(jω)ⁿ. Gain = −20n lg ω dB (slope −20n dB/decade), phase −n·90° (Figure 5.9). At ω=1 the gain is 0 dB."))
    b.append(fig(9, F.fig_5_9()))
    b.append(h3("5.4.3 Transfer function sᵐ", "Transfer function sᵐ"))
    b.append(p("G(s)=sᵐ (a zero at the origin) → gain = +20m lg ω dB (slope +20m dB/decade), phase +m·90° (Figure 5.10)."))
    b.append(fig(10, F.fig_5_10()))
    b.append(h3("5.4.4 Transfer function 1/(1+τs)", "Transfer function 1/(1+τs)"))
    b.append(p(
        "G(s)=1/(1+τs) (a pole at s=−1/τ). Gain dB = −10 lg(1+ω²τ²); phase = −tan⁻¹(ωτ). At low frequency (ω≪1/τ) the "
        "gain is 0 dB; at high frequency (ω≫1/τ) the gain has slope −20 dB/decade, intersecting 0 dB at ω=1/τ — the "
        "<b>break point</b> or corner frequency. The two straight lines are the asymptotic approximation, with a "
        "maximum error of 3 dB at the break point; the phase goes 0°→−90°, being −45° at the break (Figure 5.11, "
        "Table 5.1). Example 100/(s+100)=1/(1+s/100) has break at 100 rad/s (Figure 5.12)."))
    b.append(fig(11, F.fig_5_11()))
    b.append(fig(12, F.fig_5_12()))
    b.append(h3("5.4.5 Transfer function (1+τs)", "Transfer function (1+τs)"))
    b.append(p(
        "G(s)=(1+τs) (a zero at s=1/τ). Gain dB = +10 lg(1+ω²τ²); phase = +tan⁻¹(ωτ). At low frequency the gain is 0 "
        "dB; at high frequency the slope is +20 dB/decade, crossing 0 dB at ω=1/τ; the phase goes 0°→+90°, +45° at "
        "the break (Figure 5.13)."))
    b.append(fig(13, F.fig_5_13()))
    b.append(h3("5.4.6 Second-order terms", "Second-order terms"))
    b.append(p(
        "G(s)=ωn²/(s²+2ζωn s+ωn²) (a pair of complex poles). Gain dB = −10 lg{[1−(ω/ωn)²]²+[2ζ(ω/ωn)]²}; phase = "
        "−tan⁻¹[2ζ(ω/ωn)/(1−(ω/ωn)²)]. For ω≪ωn the gain is 0 dB; for ω≫ωn the slope is −40 dB/decade; the break is "
        "at ω/ωn=1 and the shape depends on ζ (Figure 5.14, Tables 5.2, 5.3). Example 100/(s²+4s+100): ωn=10, ζ=0.2, "
        "+8 dB error at the break (Figure 5.15). For (s²+2ζωn s+ωn²)/ωn² (complex zeros) the gain and phase are the "
        "mirror images of Figure 5.14 about the 0 line."))
    b.append(fig(14, F.fig_5_14()))
    b.append(fig(15, F.fig_5_15()))
    b.append(p(
        "Composite example: G(s)=50(s+2)/[s(s+10)] = 10 × (1+s/2) × 1/s × 1/(1+s/10). Plot each element and sum "
        "(Figure 5.16): constant 10 (20 dB, 0°), (1+s/2) (+20 dB/dec, break 2 rad/s), 1/s (−20 dB/dec), 1/(1+s/10) "
        "(−20 dB/dec, break 10 rad/s)."))

    # 5.5
    b.append(h2("5.5 System identification", "System identification"))
    b.append(p(
        "System identification determines a mathematical model from the measured response. A useful method uses a "
        "sinusoidal input over a range of frequencies, plots the experimental Bode diagram, then finds the Bode "
        "elements that fit by drawing asymptotes and examining the gradients:"))
    b.append(ul([
        "Initial gradient zero → no s or 1/s term; K from the low-frequency gain (dB = 20 lg K).",
        "Initial gradient −20 dB/decade → a 1/s term.",
        "Gradient becomes 20 dB/decade more negative at a corner → a (1+s/ωc) term in the denominator.",
        "Gradient becomes 20 dB/decade more positive at a corner → a (1+s/ωc) term in the numerator.",
        "Gradient changes by −40/+40 dB/decade → a second-order denominator/numerator term; ζ from the step response or Bode detail.",
    ]))
    b.append(p(
        "Example Figure 5.17: zero initial slope, gain 20 dB → K=10; −20 dB/decade break at 10 rad/s → G(s)=10/(1+0.1s). "
        "Figure 5.18: −20 dB/decade (1/s), K=2 (6 dB at ω=1), breaks at 1 and 10 rad/s → 2/[s(1+s)(1+0.1s)]. Figure "
        "5.19: gain 10 dB (K≈3.2), −40 dB/decade break at 1 rad/s, true plot peaks ~4 dB → ζ≈0.3 → 3.2/(s²+0.6s+1)."))
    b.append(fig(16, F.fig_5_16()))
    b.append(fig(17, F.fig_5_17()))
    b.append(fig(18, F.fig_5_18()))
    b.append(fig(19, F.fig_5_19()))

    # 5.6
    b.append(h2("5.6 Stability", "Stability"))
    b.append(p(
        "Consider a closed-loop system (Figure 5.20) given a brief pulse input. If the fed-back signal has smaller "
        "amplitude than the initial pulse the oscillation dies away (stable, Figure 5.22); if equal it continues at "
        "constant amplitude (marginally stable, Figure 5.21); if larger it grows (unstable, Figure 5.23). The "
        "condition for instability is that the gain round the G(s)H(s) loop exceeds 1 while the fed-back signal has "
        "suffered a phase change of −180°. <b>The critical point separating stable from unstable systems is when the "
        "open-loop phase shift is −180° and the open-loop gain is 1.</b>"))
    b.append(fig(20, F.fig_5_20()))
    b.append(fig(21, F.fig_5_21()))
    b.append(fig(22, F.fig_5_22()))
    b.append(fig(23, F.fig_5_23()))
    b.append(h3("5.6.1 Stability measures", "Stability measures"))
    b.append(ul([
        "<b>Phase crossover frequency:</b> the frequency at which the phase first reaches −180°.",
        "<b>Gain margin:</b> the factor by which the gain must be multiplied at the phase crossover to reach 1. A good system typically has a gain margin of 2 to 2.5.",
        "<b>Gain crossover:</b> the frequency at which the open-loop gain first reaches 1 (0 dB).",
        "<b>Phase margin:</b> the number of degrees by which the phase is smaller than −180° at the gain crossover. A good system typically has 45° to 65°.",
    ]))
    b.append(p(
        "On a Bode gain plot (dB), a gain of 1 is 0 dB. Figure 5.25 shows the parameters; Figure 5.26(a) is stable "
        "(gain < 0 dB at −180°), (b) unstable (gain > 0 dB at −180°). Example Figure 5.27: stable, gain margin ~12 "
        "dB, phase margin ~30°. From data: at 0.010 Hz gain 0.45 and phase −180° → gain margin 1/0.45 = 2.22; at "
        "0.005 Hz gain 1, phase −120° → phase margin 180−120 = 60°."))
    b.append(fig(25, F.fig_5_25()))
    b.append(fig(26, F.fig_5_26()))
    b.append(fig(27, F.fig_5_27()))

    # 5.7
    b.append(h2("5.7 Compensation", "Compensation"))
    b.append(p(
        "Compensation modifies a system's performance by adding a compensator. A compensator in the forward path is "
        "a cascade or series compensator (Figure 5.28)."))
    b.append(fig(28, F.fig_5_28()))
    b.append(h3("5.7.1 Changing the gain", "Changing the gain"))
    b.append(p(
        "Increasing the gain shifts the gain–frequency Bode plot upward by the same amount at all frequencies (no "
        "effect on the phase plot) and moves the 0 dB crossing to a higher frequency — decreasing the gain and phase "
        "margins (Figures 5.29, 5.30). To increase stability the gain must therefore be reduced. Example Figure 5.31: "
        "phase margin 35°, to reach 45° reduce gain by ~2 dB (ΔK = 1.3)."))
    b.append(fig(29, F.fig_5_29()))
    b.append(fig(30, F.fig_5_30()))
    b.append(fig(31, F.fig_5_31()))
    b.append(h3("5.7.2 Phase-lead compensation", "Phase-lead compensation"))
    b.append(p(
        "A phase-lead compensator has the form G(s)=(1+aτs)/(1+τs), a>1 (circuit Figure 5.32; a=(R1+R2)/R2, "
        "τ=R1R2C/(R1+R2)). Its Bode plot (Figure 5.33) has positive phase, peaking at the geometric-mean break "
        "frequency ωm=1/(τ√a); the maximum phase advance is sin φm=(a−1)/(a+1). It is used to increase the phase "
        "margin. Example with open-loop 10/s² (Figure 5.34, phase −180° throughout): a phase margin of 45° requires "
        "a=5.9, τ=0.083 → G(s)=(1+0.49s)/(1+0.083s)."))
    b.append(fig(32, F.fig_5_32()))
    b.append(fig(33, F.fig_5_33()))
    b.append(fig(34, F.fig_5_34()))
    b.append(h3("5.7.3 Phase-lag compensation", "Phase-lag compensation"))
    b.append(p(
        "A phase-lag compensator has the form G(s)=(1+τs)/(1+aτs), a>1 (circuit Figure 5.35; a=(R1+R2)/R2, τ=R2C). "
        "Its Bode plot (Figure 5.36) has negative phase and reduces the gain, lowering the crossover frequency — "
        "thereby improving stability at the lower frequency. Example Figure 5.37: uncompensated phase margin ~20°; "
        "choose the new crossover at 2 rad/s (where margin would be 40°+5°), 1/τ=0.2 → τ=5; gain there 20 dB → 20 lg "
        "a = 20 → a=10 → (1+5s)/(1+50s)."))
    b.append(fig(35, F.fig_5_35()))
    b.append(fig(36, F.fig_5_36()))
    b.append(fig(37, F.fig_5_37()))

    # Problems
    b.append(h2("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 16 problems, of which Problems 6, 9 and 12 are illustrated by Bode plots (Figures 5.38–"
        "5.40). They cover: magnitudes and phases of phasors; frequency response functions; magnitude and phase of "
        "first-order systems at given frequencies; sketching Bode asymptotes; determining transfer functions from "
        "Bode plots; gain and phase margins; and designing phase-lead and phase-lag compensators."))
    b.append(fig(38, F.fig_5_38()))
    b.append(fig(39, F.fig_5_39()))
    b.append(fig(40, F.fig_5_40()))
    return "".join(b)
