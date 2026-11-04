# -*- coding: utf-8 -*-
"""Handbook Chapter 81 — Modulation (Điều chế).
Run:  python build/reader_hb_ch81.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch81-modulation'
CH_NO = 81
TITLE_EN = 'Modulation'
TITLE_VI = 'Điều chế'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương 81 do David M. Beams (University of Texas at Tyler) biên soạn, tiếp cận điều chế như một phép biến đổi toán học tổng quát của tín hiệu đo thay vì chỉ là kỹ thuật truyền thông. Tác giả thiết lập biểu diễn bức xạ pha vuông góc (in-phase / quadrature), rồi lần lượt khảo sát điều chế biên độ và điều chế góc cùng các mạch và thiết bị đo thực hiện chúng.'))
    b.append(p('Trong đo lường, điều chế phục vụ bốn mục đích: dời phổ tín hiệu khỏi nhiễu 1/f và trôi một chiều, cho phép dùng kênh truyền hẹp, tách nhiều tín hiệu trên cùng một đường dẫn (ghép kênh) và cung cấp tham chiếu pha cho phép dò đồng bộ.'))
    b.append(h2('81.1 Mở đầu', '81.1 Introduction'))
    b.append(p('Điều chế là quá trình làm thay đổi một tham số của sóng mang theo tín hiệu mang tin. Với đo lường, sóng mang không nhất thiết là sóng vô tuyến: nó có thể là nguồn kích thích xoay chiều của một cảm biến điều biến (cầu biến dạng, LVDT, cảm biến điện dung) hoặc là chùm sáng được chopper trong máy đo quang học.'))
    b.append(h2('81.2 Điều chế tổng quát', '81.2 Generalized Modulation'))
    b.append(p('Biểu diễn tổng quát của tín hiệu điều chế là s_c(t) = A_c(t)·cos[ω_c t + φ(t)], trong đó A_c(t) mang thông tin biên độ và φ(t) mang thông tin góc. Khai triển theo công thức cộng cho phép viết lại thành tổng của hai thành phần vuông góc: thành phần đồng pha f_i(t) = A_c(t)cos φ(t) và thành phần cầu phương f_q(t) = A_c(t)sin φ(t).'))
    b.append(eq('s_c(t) = f_i(t)·cos(ω_c t) − f_q(t)·sin(ω_c t)', '81.1'))
    b.append(eq('f_i(t) = A_c(t)·cos[φ(t)] ,   f_q(t) = A_c(t)·sin[φ(t)]', '81.2'))
    b.append(p('Cặp (f_i, f_q) tạo thành <b>bao hình phức</b> (complex envelope) của tín hiệu; phổ của s_c chính là phổ của bao hình được dời lên ±ω_c. Biểu diễn này thống nhất mọi dạng điều chế: nếu f_q ≡ 0 ta có điều chế biên độ thuần, nếu A_c hằng số ta có điều chế góc thuần. Đây cũng là nền tảng của giải điều chế I/Q trong các máy phân tích phổ và thu phát số hiện đại.'))
    b.append(eq('S_c(ω) = ½[F_i(ω−ω_c) + F_i(ω+ω_c)] + (j/2)[F_q(ω−ω_c) − F_q(ω+ω_c)]', '81.3'))
    b.append(h2('81.3 Điều chế biên độ', '81.3 Amplitude Modulation'))
    b.append(p('Với tín hiệu điều chế m(t) và chỉ số điều chế μ, dạng song biên có sóng mang (DSB-LC) là s(t) = A_c[1 + μ·m(t)]cos ω_c t; bỏ sóng mang được DSB-SC, chỉ giữ một dải biên được SSB. Băng thông của DSB bằng 2 lần băng tín hiệu điều chế. DSB-SC không thể dò bằng mạch dò bao mà cần giải điều chế đồng bộ. Điều chế quá mức (μ > 1) làm méo bao hình và mất thông tin.'))
    b.append(eq('s_DSB(t) = A_c[1 + μ·m(t)]·cos(ω_c t) ,   B_DSB = 2·f_m,max', '81.4'))
    b.append(p('<b>Phát tín hiệu AM</b> thực hiện bằng mạch nhân (balanced modulator, Gilbert cell) hoặc bằng phần tử phi tuyến có lọc chọn dải biên. <b>Dò bao</b> dùng diode + RC: hằng số thời gian RC phải đủ lớn để lọc sóng mang nhưng đủ nhỏ để bám theo bao hình, điều kiện 1/ω_c ≪ RC ≪ 1/ω_m. <b>Giải điều chế đồng bộ</b> nhân với sóng mang phục hồi rồi lọc thông thấp; nhạy pha (cos φ) nên cần vòng khoá pha (PLL) hoặc Costas loop để tái tạo tham chiếu.'))
    b.append(eq('s(t)·2cos(ω_c t) → LPF → A_c·μ·m(t)·cos φ', '81.5'))
    b.append(p('Ví dụ đo lường điển hình: cảm biến biến dạng trong cầu Wheatstone được kích thích bằng nguồn xoay chiều, LVDT cho điện áp ra tỉ lệ dịch chuyển theo biên độ sóng mang, và nhiệt kế quang học dùng chopper để đưa tín hiệu DC lên tần số chop. Trong mọi trường hợp, dò đồng bộ cho phép phân biệt dấu của dịch chuyển (phản pha) — điều mà dò bao không làm được.'))
    b.append(h2('81.4 Điều chế góc: tần số và pha', '81.4 Angle (Frequency and Phase) Modulation'))
    b.append(p('Giữ A_c không đổi và cho góc tức thời mang tin: với PM, φ(t) = k_p·m(t); với FM, φ(t) = k_f∫m(τ)dτ. Tần số tức thời là ω_i = ω_c + dφ/dt. Chỉ số điều chế FM β = Δω/ω_m quyết định số cặp dải biên đáng kể theo hàm Bessel J_n(β); băng thông ước lượng bằng quy tắc Carson B ≈ 2(Δf + f_m).'))
    b.append(eq('s_FM(t) = A_c·cos[ω_c t + k_f∫m(τ)dτ] ,   β = Δf/f_m ,   B ≈ 2(Δf + f_m)', '81.6'))
    b.append(p('<b>Phát</b> PM dùng mạch dịch pha điều khiển điện áp; phát FM dùng VCO (dao động LC hoặc RC có varactor). <b>Giải điều chế</b> dùng bộ tách sóng tần số (discriminator, ratio detector), vòng khoá pha hoặc bộ đếm tần số; vì biên độ không mang tin, có thể dùng mạch giới hạn (limiter) phía trước để loại nhiễu biên độ — đây là ưu điểm căn bản của FM so với AM.'))
    b.append(p('Ví dụ: telemetry cảm biến dùng FM băng hẹp (β < 1), VCO biến đổi điện áp cảm biến thành tần số dễ đếm và truyền xa không suy hao biên độ, và phép đo vận tốc Doppler vốn chính là một dịch tần số tỉ lệ vận tốc. Đổi lại, FM cần băng rộng hơn và chịu hiệu ứng ngưỡng khi SNR đầu vào thấp.'))
    b.append(h2('81.5 Thiết bị và linh kiện', '81.5 Instrumentation and Components'))
    b.append(p('Các IC chuyên dụng gồm bộ nhân analog / balanced modulator, mạch dò bao, PLL (CD4046 và họ tương đương), VCO, mạch khoá pha tích hợp và ADC I/Q. Ở cấp độ thiết bị, <b>khuếch đại khoá pha</b> là hiện thân hoàn chỉnh nhất của giải điều chế đồng bộ trong đo lường; máy phân tích phổ và máy phân tích mạng dùng dò I/Q để thu cả biên độ lẫn pha. Khi chọn linh kiện cần chú ý độ rò sóng mang (carrier feedthrough), độ cân bằng của bộ nhân và độ ổn định pha của tham chiếu.'))
    b.append(table(['Dạng', 'Tham số mang tin', 'Giải điều chế', 'Băng thông'], [['DSB-LC (AM)', 'Biên độ A_c(t)', 'Dò bao (diode + RC)', '2f_m'], ['DSB-SC', 'Biên độ, không mang', 'Đồng bộ / Costas', '2f_m'], ['SSB', 'Biên độ, một dải', 'Đồng bộ + tái tạo mang', 'f_m'], ['PM', 'Pha φ(t)', 'Dò pha / PLL', '≈ 2(β+1)f_m'], ['FM', 'Tần số tức thời', 'Discriminator / PLL', '2(Δf+f_m)']], 'Bảng 81.1 · Các dạng điều chế và phương pháp giải điều chế tương ứng.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Biểu diễn I/Q thống nhất mọi phép điều chế: s_c = f_i cos ω_c t − f_q sin ω_c t. AM (DSB-LC/SC/SSB) truyền tin qua A_c(t), dò bao hoặc đồng bộ; FM/PM truyền tin qua góc với β = Δf/f_m và B ≈ 2(Δf+f_m), chịu nhiễu biên độ tốt hơn. Trong đo lường, điều chế kết hợp dò nhạy pha là cách chuẩn để thoát khỏi trôi DC và nhiễu 1/f, đồng thời phân biệt được dấu của đại lượng đo.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 81. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("David M. Beams, Modulation (CRC, 1999). The chapter develops a generalized modulation representation s_c(t) = A_c(t)cos[ω_c t + φ(t)] = f_i(t)cos ω_c t − f_q(t)sin ω_c t, where the in-phase and quadrature components form the complex envelope whose spectrum is shifted to ±ω_c. Amplitude modulation covers DSB-LC, DSB-SC and SSB, generation by balanced modulators, envelope detection (1/ω_c ≪ RC ≪ 1/ω_m) and synchronous demodulation with carrier recovery (PLL/Costas). Angle modulation covers PM and FM, VCO generation, discriminators and PLL demodulation, Bessel sidebands J_n(β), Carson's rule B ≈ 2(Δf + f_m) and the FM threshold effect. Instrumentation includes analog multipliers, PLLs, I/Q demodulators and lock-in amplifiers; metrology examples include AC-excited strain-gauge bridges, LVDTs, chopped optical measurements, sensor telemetry and Doppler shift."))
    b.append(eq('s_c(t) = f_i(t)·cos(ω_c t) − f_q(t)·sin(ω_c t)', '81.1'))
    b.append(eq('f_i(t) = A_c(t)·cos[φ(t)] ,   f_q(t) = A_c(t)·sin[φ(t)]', '81.2'))
    b.append(eq('S_c(ω) = ½[F_i(ω−ω_c) + F_i(ω+ω_c)] + (j/2)[F_q(ω−ω_c) − F_q(ω+ω_c)]', '81.3'))
    b.append(eq('s_DSB(t) = A_c[1 + μ·m(t)]·cos(ω_c t) ,   B_DSB = 2·f_m,max', '81.4'))
    b.append(eq('s(t)·2cos(ω_c t) → LPF → A_c·μ·m(t)·cos φ', '81.5'))
    b.append(eq('s_FM(t) = A_c·cos[ω_c t + k_f∫m(τ)dτ] ,   β = Δf/f_m ,   B ≈ 2(Δf + f_m)', '81.6'))
    b.append(table(['Format', 'Information parameter', 'Demodulation', 'Bandwidth'], [['DSB-LC (AM)', 'Amplitude A_c(t)', 'Envelope (diode + RC)', '2f_m'], ['DSB-SC', 'Amplitude, suppressed carrier', 'Synchronous / Costas', '2f_m'], ['SSB', 'Amplitude, one sideband', 'Synchronous + carrier recovery', 'f_m'], ['PM', 'Phase φ(t)', 'Phase detector / PLL', '≈ 2(β+1)f_m'], ['FM', 'Instantaneous frequency', 'Discriminator / PLL', '2(Δf+f_m)']], 'Table 81.1 · Modulation formats and their demodulators.'))
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
