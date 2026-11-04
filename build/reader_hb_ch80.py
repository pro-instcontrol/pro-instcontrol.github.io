# -*- coding: utf-8 -*-
"""Handbook Chapter 80 — Amplifiers and Signal Conditioners (Bộ khuếch đại và điều hoà tín hiệu).
Run:  python build/reader_hb_ch80.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch80-amplifiers-and-signal-conditioners'
CH_NO = 80
TITLE_EN = 'Amplifiers and Signal Conditioners'
TITLE_VI = 'Bộ khuếch đại và điều hoà tín hiệu'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương này trình bày các mạch nằm giữa cảm biến và thiết bị thu (thường là bộ chuyển đổi tương tự–số). Tác giả Ramón Pallás-Areny (Universitat Politècnica de Catalunya) đi từ phân loại tín hiệu, dải động và tham số khuếch đại đến từng họ mạch điều hoà: khuếch đại dụng cụ, khuếch đại sóng mang, khuếch đại khoá pha, khuếch đại cách ly, xử lý phi tuyến và tuyến tính hoá tương tự.'))
    b.append(p('Luận điểm xuyên suốt: tín hiệu từ cảm biến hiếm khi có biên độ, công suất, mức một chiều, trở kháng hay băng thông phù hợp để hiển thị, ghi, truyền hoặc xử lý tiếp. Bộ điều hoà phải được thiết kế từ đặc tính của cả tín hiệu lẫn thiết bị thu, chứ không chỉ là chọn một hệ số khuếch đại.'))
    b.append(h2('80.1 Mở đầu', '80.1 Introduction'))
    b.append(p('Cảm biến cung cấp tín hiệu tương tự hoặc số. Tín hiệu số từ encoder vị trí, công tắc hoặc cảm biến dao động đưa vào bộ đếm tần số cần mức điện áp tương thích logic và sườn đủ dốc để không gây kích sai; điện áp lớn được suy giảm bằng phân áp, sườn chậm được làm dốc bằng trigger Schmitt. Thiết bị thu điển hình yêu cầu một điện áp một đầu, tần số thấp (DC), trở ra thấp và biên độ gần sát điện áp nguồn — đó chính là ngõ vào của một ADC.'))
    b.append(p('Cảm biến tương tự chia thành loại tự phát (self-generating: cặp nhiệt điện, áp điện, pin quang) và loại điều biến (modulating: điện trở, điện dung, điện cảm), loại sau bắt buộc phải có nguồn kích thích. Cách phân loại này quyết định ngay cấu trúc tầng vào: tải, nguồn kích thích và mạch cầu.'))
    b.append(h2('80.2 Dải động', '80.2 Dynamic Range'))
    b.append(p('Dải động là tỉ số giữa tín hiệu lớn nhất còn xử lý được không bị méo (bão hoà) và tín hiệu nhỏ nhất còn phân biệt được khỏi nhiễu nền, thường biểu diễn theo decibel. Vế dưới do nhiễu nhiệt, nhiễu 1/f và offset quyết định; vế trên do nguồn nuôi và độ lệch tối đa của op-amp quyết định.'))
    b.append(eq('DR_dB = 20·log₁₀(V_max/V_min) ,   SNR = 20·log₁₀(V_signal/V_noise)', '80.1'))
    b.append(p('Chọn độ lợi sao cho tín hiệu cực đại vừa chiếm toàn thang của ADC mà tín hiệu cực tiểu vẫn nằm trên nhiễu quy về ngõ vào. Khi dải động vượt khả năng của một độ lợi cố định, dùng khuếch đại có độ lợi lập trình (PGA) hoặc tự động chuyển thang; khi đó phải quản lý thời gian ổn định sau mỗi lần đổi thang và ghi nhận thang kèm mẫu dữ liệu.'))
    b.append(h2('80.3 Phân loại tín hiệu', '80.3 Signal Classification'))
    b.append(p('Ba cặp phân loại chi phối thiết kế. <b>Một đầu / vi phân</b>: tín hiệu vi phân cho phép loại nhiễu mode chung và triệt điện áp nối đất, nhưng cần mạch có CMRR cao. <b>Dải hẹp / dải rộng</b>: tín hiệu dải hẹp cho phép lọc chọn lọc và giải điều chế đồng bộ, cải thiện SNR; tín hiệu dải rộng đòi hỏi đáp ứng phẳng và pha tuyến tính. <b>Trở ra thấp / cao</b>: nguồn trở kháng cao (điện cực pH, cảm biến áp điện) cần tầng đệm có trở vào cực lớn và dòng phân cực cực nhỏ, nếu không xảy ra suy giảm biên độ và sai số tải.'))
    b.append(h2('80.4 Các tham số chung của bộ khuếch đại', '80.4 General Amplifier Parameters'))
    b.append(p('Ngoài độ lợi, cần xét: băng thông và tích lợi–băng, trở vào/trở ra, CMRR, PSRR, điện áp offset và trôi theo nhiệt độ, dòng phân cực, mật độ nhiễu điện áp/dòng, tốc độ biến thiên (slew rate), thời gian ổn định, độ phi tuyến và tổng méo hài. Với tín hiệu một chiều, offset và trôi thường quan trọng hơn băng thông; với tín hiệu xung, slew rate và thời gian ổn định lại quyết định.'))
    b.append(eq('CMRR_dB = 20·log₁₀(A_d/A_cm) ,   V_o = A_d(V₂−V₁) + A_cm·V_cm + V_os·G', '80.2'))
    b.append(h2('80.5 Khuếch đại dụng cụ', '80.5 Instrumentation Amplifiers'))
    b.append(p('Cấu trúc ba op-amp (hai tầng đệm không đảo có độ lợi, một tầng vi phân) cho trở vào đối xứng rất cao, độ lợi đặt bằng một điện trở R_G duy nhất và khả năng đưa điện áp tham chiếu V_ref để dịch mức ra. CMRR thực tế bị giới hạn bởi độ sai lệch ghép cặp của điện trở: sai 0,1 % có thể kéo CMRR danh định 100 dB xuống dưới 60 dB.'))
    b.append(eq('G = (1 + 2R/R_G)·(R₃/R₂) ,   V_o = G·(V₂ − V₁) + V_ref', '80.3'))
    b.append(p('Hai cách thực hiện: lắp từ linh kiện rời (rẻ, dễ chọn op-amp chuyên dụng nhưng cần điện trở tinh chính xác) và khuếch đại dụng cụ tích hợp / composite (ghép hai tầng để vừa đạt trở vào cao vừa đạt độ lợi lớn với CMRR được nhà sản xuất bảo đảm). Trong đo điện sinh học, điện cực tham chiếu thường được dẫn ngược (driven-right-leg) để giảm điện áp mode chung.'))
    b.append(h2('80.6 Bộ điều hoà tín hiệu một đầu', '80.6 Single-Ended Signal Conditioners'))
    b.append(p('Các cấu hình cơ bản là khuếch đại đảo / không đảo, bộ đệm, mạch cộng để dịch mức, và bộ chuyển đổi dòng–áp (transimpedance) cho cảm biến quang. Cảm biến áp điện và cảm biến điện dung dùng <b>bộ khuếch đại điện tích</b> với tụ hồi tiếp C_f: điện áp ra chỉ phụ thuộc điện tích Q và C_f, không phụ thuộc điện dung dây dẫn — một lợi ích quyết định khi cảm biến đặt xa.'))
    b.append(eq('V_o = −Q/C_f   (khuếch đại điện tích) ,   V_o = −I_in·R_f   (transimpedance)', '80.4'))
    b.append(h2('80.7 Khuếch đại sóng mang', '80.7 Carrier Amplifiers'))
    b.append(p('Dùng nguồn kích thích xoay chiều (thường 1–10 kHz) cho cảm biến điều biến như cầu biến dạng hay LVDT. Tín hiệu ra là một tín hiệu AM quanh sóng mang, được khuếch đại ở dải hẹp rồi giải điều chế đồng bộ. Nhờ đó trôi DC, nhiễu 1/f và điện áp nhiệt điện tại mối nối (vốn nằm ở tần số rất thấp) bị loại bỏ hoàn toàn — đây là lý do chính dùng sóng mang trong đo lường chính xác.'))
    b.append(h2('80.8 Khuếch đại khoá pha', '80.8 Lock-In Amplifiers'))
    b.append(p('Bộ dò nhạy pha nhân tín hiệu đo với một tham chiếu cùng tần số, cùng pha (hoặc pha bù được), rồi lọc thông thấp. Chỉ thành phần có tần số và pha cố định với tham chiếu đi qua; mọi nhiễu ở tần số khác bị trung bình hoá. Hằng số thời gian T của bộ lọc ấn định băng thông nhiễu tương đương Δf ≈ 1/(4T) — tăng T cải thiện SNR nhưng làm đáp ứng chậm đi. Các thông số đặc trưng là độ dự trữ động (dynamic reserve), độ tuyến tính và độ ổn định pha.'))
    b.append(eq('V_PSD ∝ A·cos(φ_m − φ_ref) ,   Δf_ENBW ≈ 1/(4T)', '80.5'))
    b.append(h2('80.9 Khuếch đại cách ly', '80.9 Isolation Amplifiers'))
    b.append(p('Ba công nghệ: biến áp (điều chế sang xoay chiều rồi chỉnh lưu), quang (LED–photodiode hoặc ghép quang tuyến tính) và điện dung. Chúng cắt vòng nối đất, cho phép ngõ vào nổi trước điện áp mode chung hàng kV và bảo vệ người bệnh / thiết bị khỏi quá áp. Tham số cần xét: điện áp cách ly danh định, dòng rò, điện dung giữa hai vùng, CMRR chế độ cách ly và độ phi tuyến của đường truyền.'))
    b.append(h2('80.10 Kỹ thuật xử lý phi tuyến', '80.10 Nonlinear Signal-Processing Techniques'))
    b.append(p('Giới hạn và cắt xén (limiting/clipping) bảo vệ tầng sau và chuẩn hoá biên độ trước bộ đếm; khuếch đại logarit nén nhiều thập phân tín hiệu về một thang điện áp nhỏ (dùng đặc tính V_BE của transistor: V_o ∝ ln(V_in)); mạch nhân/chia analog thực hiện bình phương, căn bậc hai, đo công suất và chuyển đổi RMS–DC thực. Các phép toán này cho phép tính trực tiếp tỉ số giữa hai kênh mà không cần số hoá.'))
    b.append(eq('V_o = V_T·ln(V_in/(I_S·R)) ,   V_RMS = √mean(v²)', '80.6'))
    b.append(h2('80.11 Tuyến tính hoá tương tự', '80.11 Analog Linearization'))
    b.append(p('Nhiều cảm biến có đặc tính phi tuyến mạnh (thermistor NTC theo hàm mũ, RTD bậc cao, cặp nhiệt điện, diode). Các cách xử lý: đưa cảm biến vào mạch hồi tiếp để luật phi tuyến bị triệt tiêu, dùng mạng điện trở–diode xấp xỉ từng đoạn (piecewise-linear), dùng mạch log/antilog, hoặc kích thích theo hàm bù. Tuyến tính hoá tương tự giảm tải cho ADC nhưng làm tăng sai số do dung sai và trôi nhiệt của linh kiện.'))
    b.append(h2('80.12 Bộ điều hoà chuyên dụng', '80.12 Special-Purpose Signal Conditioners'))
    b.append(p('Các ví dụ điển hình: mạch bù nhiệt độ điểm nối lạnh cho cặp nhiệt điện, tầng đệm trở vào cực cao cho điện cực pH và điện cực chọn lọc ion, mạch đo điện dung chống điện dung ký sinh bằng che chắn driven guard, và bộ phát vòng dòng 4–20 mA cho truyền dẫn đường dài (không nhạy sụt áp dây, dễ phát hiện đứt dây vì 0 mA là trạng thái lỗi).'))
    b.append(table(['Họ mạch', 'Vấn đề giải quyết', 'Tham số then chốt'], [['Khuếch đại dụng cụ', 'Tín hiệu vi phân nhỏ', 'CMRR, Z_in, offset'], ['Điện tích / transimpedance', 'Cảm biến áp điện, quang', 'C_f / R_f, dòng phân cực'], ['Sóng mang + khoá pha', 'Trôi DC, nhiễu 1/f', 'Δf_ENBW, dự trữ động'], ['Cách ly', 'Vòng đất, an toàn', 'kV cách ly, dòng rò'], ['Log / RMS–DC', 'Dải động lớn', 'Độ chính xác log, băng'], ['4–20 mA', 'Truyền dẫn xa', 'Tuân thủ vòng, tải']], 'Bảng 80.1 · Các họ mạch điều hoà và vấn đề chúng giải quyết.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Thiết kế tầng điều hoà bắt đầu từ dải động và phân loại tín hiệu (một đầu/vi phân, dải hẹp/rộng, trở ra thấp/cao), rồi chọn tham số khuếch đại phù hợp. Khuếch đại dụng cụ xử lý tín hiệu vi phân; sóng mang và khoá pha đẩy phép đo lên khỏi nhiễu 1/f; cách ly cắt vòng đất; log/RMS và tuyến tính hoá mở rộng dải; 4–20 mA đưa tín hiệu đi xa. Tầng vào quyết định độ chính xác của toàn chuỗi đo.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 80. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Ramón Pallás-Areny, Amplifiers and Signal Conditioners (CRC, 1999). Sensor signals rarely have the amplitude, level, impedance or bandwidth a receiver (typically an ADC) needs. The chapter treats dynamic range and signal classification (single-ended/differential, narrowband/broadband, low/high output impedance), general amplifier parameters, the three-op-amp instrumentation amplifier (G = 1 + 2R/R_G, CMRR limited by resistor matching), single-ended conditioners including charge and transimpedance amplifiers, carrier amplifiers that move the measurement away from DC drift and 1/f noise, lock-in phase-sensitive detection with ENBW ≈ 1/(4T), transformer/optical/capacitive isolation amplifiers, nonlinear processing (limiting, logarithmic amplification, multiplication/division, RMS-to-DC), analog linearization, and special-purpose conditioners such as cold-junction compensation and 4–20 mA transmitters.'))
    b.append(eq('DR_dB = 20·log₁₀(V_max/V_min) ,   SNR = 20·log₁₀(V_signal/V_noise)', '80.1'))
    b.append(eq('CMRR_dB = 20·log₁₀(A_d/A_cm) ,   V_o = A_d(V₂−V₁) + A_cm·V_cm + V_os·G', '80.2'))
    b.append(eq('G = (1 + 2R/R_G)·(R₃/R₂) ,   V_o = G·(V₂ − V₁) + V_ref', '80.3'))
    b.append(eq('V_o = −Q/C_f   (khuếch đại điện tích) ,   V_o = −I_in·R_f   (transimpedance)', '80.4'))
    b.append(eq('V_PSD ∝ A·cos(φ_m − φ_ref) ,   Δf_ENBW ≈ 1/(4T)', '80.5'))
    b.append(eq('V_o = V_T·ln(V_in/(I_S·R)) ,   V_RMS = √mean(v²)', '80.6'))
    b.append(table(['Circuit family', 'Problem solved', 'Key parameter'], [['Instrumentation amp', 'Small differential signals', 'CMRR, Z_in, offset'], ['Charge / transimpedance', 'Piezoelectric, optical sensors', 'C_f / R_f, bias current'], ['Carrier + lock-in', 'DC drift, 1/f noise', 'ENBW, dynamic reserve'], ['Isolation', 'Ground loops, safety', 'Isolation kV, leakage'], ['Log / RMS–DC', 'Wide dynamic range', 'Log conformity, bandwidth'], ['4–20 mA', 'Long-distance transmission', 'Loop compliance, load']], 'Table 80.1 · Conditioner families and the problems they solve.'))
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
