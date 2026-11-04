# -*- coding: utf-8 -*-
"""Handbook Chapter 83 — Spectrum Analysis and Correlation (Phân tích phổ và tương quan).
Run:  python build/reader_hb_ch83.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch83-spectrum-analysis-and-correlation'
CH_NO = 83
TITLE_EN = 'Spectrum Analysis and Correlation'
TITLE_VI = 'Phân tích phổ và tương quan'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương 83 gồm hai phần độc lập. Phần 83.1 do Ronney B. Panerai (University of Leicester) trình bày phân tích phổ và tương quan bằng FFT; phần 83.2 do A. Ambrosini cùng các cộng sự tại Institute of Radioastronomy (Bologna, Ý) trình bày phân tích phổ RF/vi ba từ góc nhìn thực hành của người vận hành máy phân tích phổ.'))
    b.append(p('Điểm chung của cả hai phần là chuỗi cảnh báo giống nhau: tín hiệu trước khi số hoá phải được lọc thông thấp, nếu không hiện tượng chồng phổ (aliasing) làm sai lệch phổ một cách không thể nhận ra bằng cách nhìn vào kết quả.'))
    b.append(h2('83.1 Phân tích phổ và tương quan bằng FFT', '83.1 FFT Spectrum Analysis and Correlation'))
    b.append(h3('Khái niệm nền tảng', 'Fundamental Concepts'))
    b.append(p('Chuỗi Fourier biểu diễn tín hiệu tuần hoàn bằng tổng các hàm sin/cos ở bội của tần số cơ bản; biến đổi Fourier mở rộng sang tín hiệu không tuần hoàn. Với tín hiệu thực, phổ biên độ đối xứng chẵn và phổ pha đối xứng lẻ quanh tần số không, nên chỉ cần nửa phổ. Định lý Parseval bảo toàn năng lượng giữa hai miền, là cơ sở để chuẩn hoá mật độ công suất phổ (PSD).'))
    b.append(eq('X(f) = ∫₋∞^∞ x(t)·e^(−j2πft)dt ,   ∫|x(t)|²dt = ∫|X(f)|²df', '83.1'))
    b.append(p('Khi lấy mẫu ở f_s với N điểm trong khoảng T = N/f_s, DFT cho các dòng phổ cách nhau Δf = f_s/N = 1/T. Độ phân giải tần số vì thế chỉ cải thiện bằng cách kéo dài thời gian ghi; thêm zero vào cuối bản ghi (zero-padding) chỉ làm mịn đồ thị chứ không tách được hai đỉnh gần nhau. Điều kiện Nyquist f_s > 2f_max phải được bảo đảm bằng bộ lọc analog trước ADC.'))
    b.append(eq('X[k] = Σ_{n=0}^{N−1} x[n]·e^(−j2πkn/N) ,   Δf = f_s/N = 1/T', '83.2'))
    b.append(h3('Biến đổi Fourier nhanh', 'Fast Fourier Transform'))
    b.append(p('FFT là họ thuật toán tính DFT với độ phức tạp O(N log₂N) thay vì O(N²) nhờ phân rã Cooley–Tukey (radix-2, chia đôi chuỗi thành phần chẵn/lẻ). Điều kiện thuận lợi nhất là N = 2^m; các thư viện hiện đại xử lý cả N hợp số bằng các thừa số nguyên tố nhỏ. Với phép đo thời gian thực, giới hạn thường không phải là tốc độ CPU mà là thời gian thu đủ N mẫu và khả năng xử lý khối chồng lấp.'))
    b.append(h3('Phân tích phổ bằng FFT', 'FFT Spectral Analysis'))
    b.append(p('Cắt một đoạn hữu hạn tương đương nhân tín hiệu với cửa sổ chữ nhật, tạo rò rỉ phổ (sidelobe cao, ≈ −13 dB). Các cửa sổ Hann, Hamming, Blackman, Flattop, Kaiser đẩy sidelobe xuống nhưng nới rộng lobe chính; cần hệ số bù biên độ và công suất khi định lượng. Các lỗi kinh điển: đọc sai đỉnh do rò rỉ, quên bù cửa sổ, nhầm dB biên độ với dB công suất, và không phân biệt nhiễu ngẫu nhiên (cần trung bình hoá) với thành phần điều hoà (cần độ phân giải).'))
    b.append(eq('S_xx(f) = |X(f)|²/(T·U) ,   U = (1/N)Σ w²[n]   (hệ số bù cửa sổ)', '83.3'))
    b.append(p('Ước lượng PSD ổn định bằng phương pháp Welch: chia bản ghi thành các đoạn chồng lấp, cửa sổ hoá từng đoạn, tính periodogram rồi trung bình. Trung bình K đoạn làm giảm phương sai ước lượng theo √K nhưng làm độ phân giải kém đi do mỗi đoạn ngắn hơn. Với tín hiệu không dừng (rung động tăng tốc, thoại) phải dùng STFT, spectrogram hoặc biến đổi wavelet thay vì một phổ duy nhất.'))
    b.append(h3('Phân tích tương quan bằng FFT', 'FFT Correlation Analysis'))
    b.append(p('Tự tương quan R_xx(τ) đo mức giống nhau của tín hiệu với bản sao dịch τ, làm nổi bật chu kỳ bị nhiễu che lấp; tương quan chéo R_xy(τ) xác định độ trễ giữa hai kênh. Theo định lý Wiener–Khinchin, PSD chính là biến đổi Fourier của tự tương quan, nên tính tương quan qua FFT (nhân phổ liên hợp rồi IFFT) nhanh hơn nhiều so với tích phân trực tiếp. Cần chú ý tương quan vòng (circular) của DFT: phải zero-padding ít nhất 2N−1 điểm để thu được tương quan tuyến tính.'))
    b.append(eq('R_xy(τ) = ℱ⁻¹{X(f)·Y*(f)} ,   γ²_xy(f) = |S_xy(f)|²/(S_xx·S_yy)', '83.4'))
    b.append(p('Hàm độ kết hợp γ²(f) nằm trong [0,1]: giá trị thấp tại một tần số báo hiệu nhiễu, rò rỉ hoặc hệ phi tuyến, và là tiêu chí chuẩn để chấp nhận hay loại một phép đo hàm đáp ứng tần số (FRF). Từ tương quan chéo còn suy được H(f) = S_xy/S_xx, độ trễ truyền âm và vận tốc dòng chảy trong phép đo hai cảm biến.'))
    b.append(h3('Tham khảo thêm', 'Further Information'))
    b.append(p('Các chủ đề mở rộng gồm cepstrum (biến đổi Fourier của log phổ, dùng tách họ hài và tiếng vang), phân tích bậc thang (order tracking) cho máy quay tốc độ biến đổi, ước lượng phổ tham số (AR/ARMA, Burg) cho bản ghi ngắn, và chuẩn hoá đơn vị PSD (V²/Hz, dB/Hz) để so sánh giữa các thiết bị.'))
    b.append(h2('83.2 Phân tích phổ RF và vi ba', '83.2 RF/Microwave Spectrum Analysis'))
    b.append(h3('Cách tiếp cận thực hành', 'A Practical Approach to Spectrum Analysis'))
    b.append(p('Máy phân tích phổ RF thực chất là một máy thu siêu ngoại sai quét: tín hiệu vào qua bộ suy giảm, trộn với dao động nội quét, qua bộ lọc trung tần có độ rộng phân giải RBW, rồi dò biên độ và hiển thị theo tần số. Ba nút điều khiển quyết định độ tin cậy của phổ đồ: <b>RBW</b> (độ phân giải và mức nhiễu nền: giảm RBW 10 lần hạ nhiễu nền 10 dB), <b>VBW</b> (làm mịn vết quét, không đổi nhiễu nền) và <b>thời gian quét</b> (quét quá nhanh so với RBW làm lệch đỉnh và giảm biên độ).'))
    b.append(eq('DANL ∝ 10·log₁₀(RBW) + NF − 174 dBm/Hz ,   t_sweep ∝ span/RBW²', '83.5'))
    b.append(p('Nhiễu pha của dao động nội quyết định khả năng nhìn tín hiệu nhỏ sát một tín hiệu lớn; méo intermodulation ở tầng trộn tạo các tích giả (spurious) có thể bị nhầm là tín hiệu thật. Quy tắc thực hành: giảm suy hao ngõ vào cho đến khi mức tín hiệu giả bắt đầu đổi, rồi tăng lại vài dB; kiểm tra lại với RBW và span khác nhau để phân biệt tín hiệu thật với spurious.'))
    b.append(h3('Chọn máy phân tích phổ phù hợp', 'Choosing the Right Analyzer'))
    b.append(p('Bộ tiêu chí: dải tần và tần số trung tâm, dải động (DANL đến điểm nén 1 dB / IP3), độ chính xác biên độ, nhiễu pha tại các offset quan trọng, RBW nhỏ nhất, tốc độ quét, và các tuỳ chọn (preamp, tracking generator, phân tích điều chế, ghi phổ thời gian thực). Máy quét siêu ngoại sai truyền thống rẻ và dải động tốt; máy FFT / real-time spectrum analyzer bắt được tín hiệu ngắn và xung hiếm mà máy quét có thể bỏ sót.'))
    b.append(table(['Tiêu chí', 'Ý nghĩa', 'Hệ quả khi chọn sai'], [['RBW', 'Độ rộng lọc trung tần', 'Đỉnh dính nhau hoặc nhiễu nền cao'], ['DANL', 'Mức nhiễu hiển thị trung bình', 'Không thấy tín hiệu yếu'], ['Nhiễu pha', 'Ồn dao động nội', 'Che tín hiệu sát sóng mang lớn'], ['IP3 / nén 1 dB', 'Tuyến tính tầng vào', 'Sinh tín hiệu giả'], ['Thời gian quét', 'Tốc độ quét toàn span', 'Sai biên độ, sót xung'], ['Real-time / FFT', 'Bắt tín hiệu tức thời', 'Bỏ sót phát xạ ngắn']], 'Bảng 83.1 · Tiêu chí chọn máy phân tích phổ.'))
    b.append(h3('Ứng dụng nâng cao', 'Advanced Applications'))
    b.append(p('Trong thiên văn vô tuyến và viễn thám, máy phân tích phổ trở thành bộ lọc ngân hàng (filter bank) / máy đo phổ đa kênh, nơi tích phân dài và hiệu chuẩn nhiệt độ nhiễu bằng nguồn đen nóng–lạnh quyết định độ nhạy. Các ứng dụng khác gồm đo nhiễu pha và jitter, đo độ sâu điều chế và độ chiếm băng kênh, kiểm tra phát xạ ngoại lai (spurious emission) theo chuẩn EMC, và giám sát phổ với ngưỡng cảnh báo theo mặt nạ (mask).'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Phần FFT: Δf = f_s/N = 1/T, cửa sổ chống rò rỉ, Welch giảm phương sai, Wiener–Khinchin nối R_xx với PSD, tương quan chéo cho độ trễ và γ² kiểm định FRF; luôn lọc chống chồng phổ trước ADC. Phần RF: máy thu siêu ngoại sai quét với RBW/VBW/thời gian quét, DANL ∝ 10log(RBW), nhiễu pha và IP3 giới hạn dải động, máy real-time bắt tín hiệu ngắn. Hai phần cùng chung một nguyên tắc: hiểu rõ cửa sổ và băng nhiễu trước khi tin vào đỉnh phổ.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 83. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Ronney B. Panerai (University of Leicester), FFT Spectrum Analysis and Correlation; A. Ambrosini et al. (Institute of Radioastronomy, Bologna), RF/Microwave Spectrum Analysis. Part 1 covers Fourier series/transform and Parseval, the DFT and FFT (Cooley–Tukey, O(N log N)), Δf = f_s/N = 1/T, Nyquist and mandatory low-pass filtering before the ADC, window functions and leakage/correction factors, Welch averaged periodograms, variance–resolution trade-off, autocorrelation and cross-correlation via FFT with zero padding to avoid circular correlation, Wiener–Khinchin, coherence γ² and FRF H = S_xy/S_xx, plus cepstrum, order tracking and parametric AR spectra. Part 2 treats the swept superheterodyne spectrum analyser: RBW, VBW, sweep time, DANL (∝ 10 log RBW), phase noise, IP3/1 dB compression, tracking generators, choosing between swept and real-time FFT analysers, and advanced radioastronomy/EMC/modulation applications.'))
    b.append(eq('X(f) = ∫₋∞^∞ x(t)·e^(−j2πft)dt ,   ∫|x(t)|²dt = ∫|X(f)|²df', '83.1'))
    b.append(eq('X[k] = Σ_{n=0}^{N−1} x[n]·e^(−j2πkn/N) ,   Δf = f_s/N = 1/T', '83.2'))
    b.append(eq('S_xx(f) = |X(f)|²/(T·U) ,   U = (1/N)Σ w²[n]   (hệ số bù cửa sổ)', '83.3'))
    b.append(eq('R_xy(τ) = ℱ⁻¹{X(f)·Y*(f)} ,   γ²_xy(f) = |S_xy(f)|²/(S_xx·S_yy)', '83.4'))
    b.append(eq('DANL ∝ 10·log₁₀(RBW) + NF − 174 dBm/Hz ,   t_sweep ∝ span/RBW²', '83.5'))
    b.append(table(['Criterion', 'Meaning', 'If chosen wrongly'], [['RBW', 'Resolution filter width', 'Merged peaks or high noise floor'], ['DANL', 'Displayed average noise level', 'Weak signals invisible'], ['Phase noise', 'Local-oscillator jitter', 'Masks close-in signals'], ['IP3 / 1 dB compression', 'Input linearity', 'Spurious responses'], ['Sweep time', 'Full-span sweep speed', 'Amplitude error, missed pulses'], ['Real-time / FFT', 'Transient capture', 'Short emissions missed']], 'Table 83.1 · Spectrum-analyser selection criteria.'))
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
