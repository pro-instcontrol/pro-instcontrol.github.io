# -*- coding: utf-8 -*-
"""Handbook Chapter 82 — Filters (Bộ lọc).
Run:  python build/reader_hb_ch82.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch82-filters'
CH_NO = 82
TITLE_EN = 'Filters'
TITLE_VI = 'Bộ lọc'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương 82 do Rahman Jamal (National Instruments Germany) và Robert Steer (Frequency Devices) biên soạn, đi từ phân loại và bài toán xấp xỉ đáp ứng đến thiết kế bộ lọc thụ động, chủ động, rời rạc, số FIR/IIR, sóng số, tụ chuyển mạch và bộ lọc thích ứng. Đây là chương dài nhất trong khối xử lý tín hiệu của sổ tay.'))
    b.append(p("Bộ lọc trong chuỗi đo không chỉ để 'làm sạch' tín hiệu: nó ấn định băng nhiễu tương đương, quyết định méo pha, bảo vệ ADC khỏi chồng phổ và khôi phục tín hiệu liên tục sau DAC. Vì vậy thông số kỹ thuật của bộ lọc phải được viết cùng lúc với thông số của bộ chuyển đổi."))
    b.append(h2('82.1 Mở đầu', '82.1 Introduction'))
    b.append(p('Bộ lọc là hệ tuyến tính bất biến theo thời gian chọn lọc tần số. Với tín hiệu liên tục, đầu ra là tích phân chập y(t) = ∫h(τ)x(t−τ)dτ; với tín hiệu rời rạc lấy mẫu chu kỳ T, x[k] = x(kT) và đầu ra là tổng chập rời rạc. Hàm truyền H(s) hoặc H(z) mô tả hoàn toàn đáp ứng biên độ và pha.'))
    b.append(eq('y(t) = ∫₀^∞ h(τ)·x(t−τ)dτ ,   y[k] = Σ h[n]·x[k−n]', '82.1'))
    b.append(h2('82.2 Phân loại bộ lọc', '82.2 Filter Classification'))
    b.append(p('Theo dải: thông thấp, thông cao, thông dải, triệt dải (notch), thông toàn dải (all-pass dùng để chỉnh pha). Theo công nghệ: thụ động RLC (không cần nguồn, chịu công suất lớn nhưng cồng kềnh ở tần số thấp), chủ động RC–op-amp (không cần cuộn cảm, dễ lập trình nhưng giới hạn bởi tích lợi–băng), tụ chuyển mạch và số. Theo miền thời gian: liên tục (analog) và rời rạc (digital/discrete-time).'))
    b.append(h2('82.3 Bài toán xấp xỉ đáp ứng', '82.3 The Filter Approximation Problem'))
    b.append(p("Đáp ứng lý tưởng 'viên gạch' không thực hiện được; bài toán thiết kế là tìm hàm hữu tỉ H(s) thoả một tập thông số (dải thông, dải triệt, gợn, suy giảm, trễ nhóm) với bậc thấp nhất. Bốn họ kinh điển tương ứng bốn cách đánh đổi:"))
    b.append(table(['Họ', 'Dải thông', 'Dải triệt', 'Trễ nhóm', 'Độ dốc'], [['Butterworth', 'Cực đại phẳng', 'Đơn điệu', 'Trung bình', 'Trung bình'], ['Chebyshev I', 'Gợn cho phép', 'Đơn điệu', 'Kém', 'Cao'], ['Chebyshev II', 'Phẳng', 'Gợn ngược', 'Kém', 'Cao'], ['Elliptic / Cauer', 'Gợn', 'Gợn + điểm không', 'Kém nhất', 'Cao nhất'], ['Bessel / Thomson', 'Phẳng vừa', 'Chậm', 'Phẳng nhất', 'Thấp nhất']], 'Bảng 82.1 · Bốn họ xấp xỉ kinh điển.'))
    b.append(p('Nguyên tắc chọn: đo biên độ tĩnh dùng Butterworth; cần triệt nhanh trong không gian hẹp (chống chồng phổ, ghép kênh) dùng elliptic; đo xung, điều khiển và truyền dữ liệu dùng Bessel vì độ quá xung tỉ lệ với độ không phẳng của trễ nhóm. Biên độ của bộ Butterworth bậc n là |H| = 1/√(1+(ω/ω_c)²ⁿ), cho độ dốc 20n dB/thập phân.'))
    b.append(eq('|H(jω)|² = 1/(1 + (ω/ω_c)²ⁿ) ,   f_c = 1/(2πRC)  (bậc nhất)', '82.2'))
    b.append(h2('82.4 Ví dụ thiết kế thụ động và chủ động', '82.4 Passive and Active Design Examples'))
    b.append(p('Thụ động: mạng LC theo bậc thang (ladder) tổng hợp từ hệ số Butterworth/Chebyshev chuẩn hoá, rồi giải chuẩn hoá theo tần số và trở tải R₀. Chủ động: cấu trúc Sallen–Key (VCVS, đơn giản nhưng nhạy hệ số Q), multiple-feedback (tốt cho thông dải/Q cao), state-variable và biquad (cung cấp đồng thời thông thấp/cao/dải, Q và ω₀ đặt độc lập). Với Q > 10 và bậc > 4 nên xếp tầng các cell bậc hai để giảm độ nhạy linh kiện.'))
    b.append(h2('82.5 Bộ lọc thời gian rời rạc', '82.5 Discrete-Time Filters'))
    b.append(p('Tín hiệu lấy mẫu x[k] = x(kT) được xử lý bằng phương trình sai phân; biến đổi z thay biến đổi Laplace với ánh xạ z = e^{sT}. Vòng tròn đơn vị |z| = 1 tương ứng trục tần số thực; cực nằm trong vòng tròn đơn vị thì hệ ổn định. Phép đo phải bảo đảm f_s > 2f_max, nếu không thành phần ngoài dải gập về (alias) mà bộ lọc số không thể phân biệt.'))
    b.append(eq('H(z) = Y(z)/X(z) = (Σ b_k z⁻ᵏ)/(1 + Σ a_k z⁻ᵏ) ,   z = e^{sT}', '82.3'))
    b.append(h2('82.6 Quy trình thiết kế bộ lọc số', '82.6 Digital Filter Design Process'))
    b.append(p('Sáu bước: (1) viết đặc tả (f_pass, f_stop, gợn, suy giảm, trễ cho phép, f_s); (2) chọn xấp xỉ và tính bậc; (3) chọn cấu trúc hiện thực (direct form, cascade biquad, lattice, transposed); (4) lượng tử hoá hệ số và biến trung gian, kiểm tra ổn định và dao động tràn số; (5) mô phỏng với tín hiệu thực; (6) kiểm chứng trên phần cứng với cùng tần số lấy mẫu. Bước 4 là nơi các thiết kế IIR bậc cao thường thất bại.'))
    b.append(h2('82.7 Thiết kế FIR', '82.7 FIR Filter Design'))
    b.append(p('FIR có hàm truyền chỉ gồm tử thức, luôn ổn định và có thể đạt <b>pha tuyến tính chính xác</b> nếu hệ số đối xứng (h[n] = h[N−1−n]); trễ nhóm hằng (N−1)/2 mẫu. Thiết kế cửa sổ (windowed) cắt đáp ứng xung lý tưởng rồi nhân cửa sổ Hann/Hamming/Kaiser để đổi gợn Gibbs lấy độ rộng chuyển tiếp. Thiết kế tối ưu Parks–McClellan (Remez exchange) phân bố sai số equiripple và cho bậc thấp nhất với cùng đặc tả. Bộ lọc dải hẹp cần bậc rất lớn, nên thường đi kèm giảm tốc độ lấy mẫu (decimation).'))
    b.append(eq('y[n] = Σ_{k=0}^{N−1} h[k]·x[n−k] ,   τ_g = (N−1)·T/2  (đối xứng)', '82.4'))
    b.append(h2('82.8 Thiết kế IIR', '82.8 IIR Filter Design'))
    b.append(p('IIR mượn các họ xấp xỉ analog, chuyển sang miền z bằng biến đổi song tuyến s = (2/T)(1−z⁻¹)/(1+z⁻¹) (không gây alias nhưng làm nén tần số phi tuyến, cần pre-warp tần số cắt) hoặc bất biến xung (giữ dạng đáp ứng xung nhưng có alias). Hiện thực dạng <b>cascade các cell bậc hai (biquad)</b> để hạn chế độ nhạy hệ số và tràn số. Đổi lấy hiệu quả (bậc thấp hơn FIR rất nhiều) là pha phi tuyến, nguy cơ mất ổn định do lượng tử hoá và dao động limit cycle.'))
    b.append(h2('82.9 Bộ lọc sóng số', '82.9 Wave Digital Filters'))
    b.append(p('Bộ lọc sóng số mô phỏng mạng LC thụ động bằng các biến sóng tới/sóng phản xạ (a = v + R·i, b = v − R·i) và các bộ nối (adaptors). Nhờ bảo toàn tính thụ động của mạng gốc, chúng có độ nhạy hệ số rất thấp, ổn định ngay cả khi lượng tử hoá thô và không sinh dao động limit cycle — rất phù hợp cho bộ lọc tích hợp trên FPGA/ASIC với word length ngắn.'))
    b.append(h2('82.10 Bộ lọc chống chồng phổ và làm mượt', '82.10 Antialiasing and Smoothing Filters'))
    b.append(p('Trước ADC bắt buộc có bộ lọc thông thấp analog (anti-aliasing) với f_c < f_s/2 và suy giảm tại f_s/2 lớn hơn dải động của ADC; thường chọn f_s = 2,5–10·f_max để nới dải chuyển tiếp. Sau DAC cần bộ lọc làm mượt (reconstruction/smoothing) loại bỏ các ảnh phổ tại bội của f_s và bù đáp ứng sin(x)/x của mạch giữ mẫu bậc không.'))
    b.append(eq('H_ZOH(f) = sin(πf/f_s)/(πf/f_s) ,   f_c < f_s/2', '82.5'))
    b.append(h2('82.11 Bộ lọc tụ chuyển mạch', '82.11 Switched-Capacitor Filters'))
    b.append(p('Thay điện trở bằng tụ C_R chuyển mạch ở tần số đồng hồ f_clk, cho điện trở tương đương R_eq = 1/(C_R·f_clk). Vì f_c tỉ lệ với tỉ số tụ và f_clk, tần số cắt được lập trình chính xác bằng một xung đồng hồ và ổn định theo nhiệt độ tốt hơn RC rời. Đổi lại: phát sinh nhiễu đồng hồ (clock feedthrough), cần lọc thông thấp đơn giản ở ngõ ra và phải thoả f_clk ≫ 2f_c.'))
    b.append(eq('R_eq = 1/(C_R·f_clk) ,   f_c ∝ f_clk·(C₁/C₂)', '82.6'))
    b.append(h2('82.12 Bộ lọc thích ứng', '82.12 Adaptive Filters'))
    b.append(p('Khi đặc tính nhiễu hoặc kênh truyền thay đổi theo thời gian, hệ số lọc được cập nhật theo thuật toán LMS (w[n+1] = w[n] + µ·e[n]·x[n]) hoặc RLS (hội tụ nhanh hơn, độ phức tạp O(N²)). Ứng dụng kinh điển: triệt nhiễu (ANC) với tham chiếu nhiễu độc lập, khử tiếng vang, cân bằng kênh, nhận dạng hệ thống và dự báo. Tham số µ điều khiển đổi tốc độ hội tụ lấy sai số trạng thái ổn định.'))
    b.append(eq('e[n] = d[n] − wᵀ[n]x[n] ,   w[n+1] = w[n] + 2µ·e[n]·x[n]  (LMS)', '82.7'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Từ bài toán xấp xỉ (Butterworth phẳng, Chebyshev/elliptic dốc, Bessel pha tuyến tính) đến hiện thực: RLC/Sallen–Key cho analog, FIR (ổn định, pha tuyến tính) và IIR (hiệu quả nhưng nhạy lượng tử hoá) cho số, cộng bộ lọc sóng số, tụ chuyển mạch và LMS thích ứng. Anti-aliasing trước ADC (f_c < f_s/2) và smoothing sau DAC là hai bộ lọc bắt buộc của mọi chuỗi đo số.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 82. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Rahman Jamal and Robert Steer, Filters (CRC, 1999). The chapter covers classification (low/high/band/notch/all-pass; passive, active, switched-capacitor, discrete-time), the filter approximation problem and the Butterworth, Chebyshev I/II, elliptic (Cauer) and Bessel families, passive ladder and active Sallen–Key/multiple-feedback/state-variable design examples, discrete-time filters and H(z) with z = e^{sT}, the digital design workflow including coefficient quantisation, windowed and Parks–McClellan (equiripple) FIR design with exact linear phase for symmetric coefficients, IIR design via the bilinear transform with frequency prewarping and cascade biquads, wave digital filters with low coefficient sensitivity, antialiasing and reconstruction (ZOH sin x/x) filters, switched-capacitor filters (R_eq = 1/(C_R f_clk)), and adaptive LMS/RLS filters for noise cancellation, equalisation and system identification.'))
    b.append(eq('y(t) = ∫₀^∞ h(τ)·x(t−τ)dτ ,   y[k] = Σ h[n]·x[k−n]', '82.1'))
    b.append(table(['Family', 'Passband', 'Stopband', 'Group delay', 'Roll-off'], [['Butterworth', 'Maximally flat', 'Monotonic', 'Medium', 'Medium'], ['Chebyshev I', 'Equiripple', 'Monotonic', 'Poor', 'High'], ['Chebyshev II', 'Flat', 'Inverse ripple', 'Poor', 'High'], ['Elliptic / Cauer', 'Equiripple', 'Ripple + nulls', 'Worst', 'Highest'], ['Bessel / Thomson', 'Fairly flat', 'Slow', 'Flattest', 'Lowest']], 'Table 82.1 · Classical approximation families.'))
    b.append(eq('|H(jω)|² = 1/(1 + (ω/ω_c)²ⁿ) ,   f_c = 1/(2πRC)  (bậc nhất)', '82.2'))
    b.append(eq('H(z) = Y(z)/X(z) = (Σ b_k z⁻ᵏ)/(1 + Σ a_k z⁻ᵏ) ,   z = e^{sT}', '82.3'))
    b.append(eq('y[n] = Σ_{k=0}^{N−1} h[k]·x[n−k] ,   τ_g = (N−1)·T/2  (đối xứng)', '82.4'))
    b.append(eq('H_ZOH(f) = sin(πf/f_s)/(πf/f_s) ,   f_c < f_s/2', '82.5'))
    b.append(eq('R_eq = 1/(C_R·f_clk) ,   f_c ∝ f_clk·(C₁/C₂)', '82.6'))
    b.append(eq('e[n] = d[n] − wᵀ[n]x[n] ,   w[n+1] = w[n] + 2µ·e[n]·x[n]  (LMS)', '82.7'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE,
                                body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
