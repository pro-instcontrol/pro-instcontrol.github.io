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
    b.append(p('Bộ lọc chọn lọc tần số: giữ dải mong muốn, loại nhiễu ngoài dải, chống chồng phổ trước ADC và định hình pha/độ trễ của chuỗi đo. Phân loại theo đáp ứng (thông thấp, thông cao, thông dải, triệt dải/notch, thông dải toàn pha) và theo công nghệ (thụ động LC/RC, chủ động op-amp, tụ chuyển mạch, số FIR/IIR).'))
    b.append(p('Lựa chọn họ đáp ứng luôn là thoả hiệp: Butterworth phẳng nhất, Chebyshev góc dốc hơn nhưng gợn sóng, Bessel pha tuyến tính nhất, elliptic dốc nhất nhưng gợn cả hai dải.'))
    b.append(h2('82.1 Hàm truyền và tần số cắt', 'Transfer Function and Cutoff'))
    b.append(p('Bộ RC bậc nhất có hàm truyền H(s) = 1/(1 + sRC); tại f_c biên độ giảm 3 dB và pha lệch 45°. Bậc n cho độ dốc 20n dB/thập phân (6n dB/octave). Với bộ chủ động, hệ số Q và tần số cắt đặt độc lập bằng tỉ lệ điện trở/tụ trong cấu trúc Sallen–Key hoặc multiple-feedback.'))
    b.append(eq('H(s) = 1/(1 + sRC) ,   f_c = 1/(2πRC) ,   |H(jω)| = 1/√(1 + (f/f_c)²ⁿ)', '82.1'))
    b.append(h2('82.2 Các họ xấp xỉ kinh điển', 'Classical Approximations'))
    b.append(p('Butterworth cực đại phẳng trong dải thông; Chebyshev loại I gợn ở dải thông, loại II gợn ở dải triệt; elliptic (Cauer) gợn cả hai nhưng đạt dốc lớn nhất với bậc thấp nhất; Bessel (Thomson) tối ưu độ trễ nhóm phẳng nên giữ dạng xung tốt. Với đo động lực học và tín hiệu xung, Bessel thường quan trọng hơn độ dốc danh định.'))
    b.append(table(['Họ', 'Dải thông', 'Độ dốc', 'Trễ nhóm', 'Dùng khi'], [['Butterworth', 'Phẳng', 'Trung bình', 'Khá', 'Đo biên độ tổng quát'], ['Chebyshev I', 'Gợn 0,5–3 dB', 'Cao', 'Kém', 'Cần dốc, cho phép gợn'], ['Elliptic', 'Gợn', 'Rất cao', 'Kém', 'Ghép kênh, chống chồng phổ'], ['Bessel', 'Phẳng vừa', 'Thấp', 'Rất phẳng', 'Xung, điều khiển'], ['FIR tuyến tính pha', 'Tuỳ thiết kế', 'Cao', 'Phẳng chính xác', 'Xử lý số']], 'Bảng 82.1 · So sánh các họ bộ lọc.'))
    b.append(h2('82.3 Triệt dải, tụ chuyển mạch và lọc số', 'Notch, Switched-Capacitor and Digital Filters'))
    b.append(p('Notch (Twin-T, active) triệt 50/60 Hz với Q cao nhưng cần linh kiện dung sai hẹp. Tụ chuyển mạch đặt f_c theo tần số đồng hồ (f_c ∝ f_clk/C tỉ lệ) nên dễ lập trình, tuy nhiên phát sinh nhiễu đồng hồ cần lọc bậc thấp đi kèm. Lọc số: FIR luôn ổn định và có thể pha tuyến tính chính xác nhưng tốn hệ số; IIR hiệu quả hơn nhưng nhạy lượng tử hoá hệ số và có thể mất ổn định.'))
    b.append(eq('y[n] = Σ b_k·x[n−k] − Σ a_k·y[n−k] ,   f_c,sw ≈ f_clk/(2π·C_ratio)', '82.2'))
    b.append(h2('82.4 Tiêu chí chọn trong chuỗi đo', 'Selection in a Measurement Chain'))
    b.append(p('Bộ lọc chống chồng phổ phải đặt trước ADC với f_c < f_s/2 và suy giảm đủ lớn tại f_s/2; công suất nhiễu tương đương ENBW của bộ lọc quyết định nhiễu đọc được. Dung sai linh kiện, trôi nhiệt và nhiễu op-amp làm lệch f_c thực tế — với bậc cao và Q lớn nên dùng linh kiện 0,1 %/ C0G và mô phỏng Monte Carlo.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Chọn f_c = 1/(2πRC), bậc n cho 20n dB/thập phân; Butterworth phẳng, Chebyshev/elliptic dốc, Bessel pha tuyến tính. Anti-aliasing trước ADC là bắt buộc (f_c < f_s/2). FIR ổn định và pha tuyến tính, IIR tiết kiệm nhưng nhạy lượng tử hoá; ENBW của bộ lọc quyết định nhiễu cuối ra.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 82. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("Filters shape amplitude and phase in a measurement chain. A first-order RC has H(s) = 1/(1+sRC) and f_c = 1/(2πRC); order n gives 20n dB/decade. Butterworth is maximally flat, Chebyshev and elliptic trade ripple for steepness, Bessel preserves group delay and pulse shape. Notch filters remove 50/60 Hz; switched-capacitor filters set f_c from a clock; FIR offers exact linear phase and unconditional stability while IIR is cheaper but coefficient-sensitive. An anti-aliasing filter must precede the ADC with f_c < f_s/2, and the filter's equivalent noise bandwidth sets the output noise."))
    b.append(eq('H(s) = 1/(1 + sRC) ,   f_c = 1/(2πRC) ,   |H(jω)| = 1/√(1 + (f/f_c)²ⁿ)', '82.1'))
    b.append(table(['Family', 'Passband', 'Roll-off', 'Group delay', 'Use when'], [['Butterworth', 'Flat', 'Medium', 'Fair', 'General amplitude measurement'], ['Chebyshev I', 'Ripple 0.5–3 dB', 'High', 'Poor', 'Steepness, ripple tolerated'], ['Elliptic', 'Ripple', 'Very high', 'Poor', 'Anti-alias, channel separation'], ['Bessel', 'Fairly flat', 'Low', 'Very flat', 'Pulses, control loops'], ['Linear-phase FIR', 'Design dependent', 'High', 'Exactly flat', 'Digital processing']], 'Table 82.1 · Filter-family comparison.'))
    b.append(eq('y[n] = Σ b_k·x[n−k] − Σ a_k·y[n−k] ,   f_c,sw ≈ f_clk/(2π·C_ratio)', '82.2'))
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
