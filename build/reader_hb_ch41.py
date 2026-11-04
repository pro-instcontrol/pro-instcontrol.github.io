# -*- coding: utf-8 -*-
"""Handbook Chapter 41 — Phase Measurement (Đo pha).
Run:  python build/reader_hb_ch41.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch41-phase-measurement"
CH_NO = 41
TITLE_EN = "Phase Measurement"
TITLE_VI = "Đo pha"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Pha</b> (phase) là góc lệch theo thời gian giữa hai tín hiệu cùng tần số, thường ký hiệu φ. Đo "
        "pha là cơ sở để suy ra trở kháng, hệ số công suất, độ tự cảm/điện dung, và là nguyên lý của nhiều "
        "cảm biến (LVDT, cảm biến điện môi đo độ ẩm, radar, siêu âm). Độ chính xác phụ thuộc vào tần số, "
        "méo dạng sóng và nhiễu."))
    b.append(p(
        "Với hai tín hiệu v₁(t)=V₁sin ωt và v₂(t)=V₂sin(ωt−φ), góc φ được xác định qua vị trí tương đối "
        "của các điểm không (zero-crossing) hoặc qua thành phần chéo (cross-correlation)."))

    b.append(h2("41.1 Phương pháp Lissajous", "Lissajous (Oscilloscope) Method"))
    b.append(p(
        "Đưa hai tín hiệu lên trục X và Y của oscilloscope tương tự. Nếu φ = 0 xuất hiện đường chéo thẳng; "
        "φ = 90° cho elip đứng (hoặc tròn nếu biên độ bằng nhau). Với elip, đo độ lệch x₀ tại trục Y = 0 "
        "so với biên độ X_max:"))
    b.append(eq("sin φ = x₀ / X_max   (hoặc  sin φ = y₀ / Y_max)"))
    b.append(p(
        "Phương pháp trực quan, dùng để kiểm tra nhanh, nhưng độ chính xác chỉ khoảng 1°–2° và yêu cầu "
        "biên độ ổn định, tần số bằng nhau."))

    b.append(h2("41.2 Chuyển đổi thời gian – điện áp", "Time-to-Voltage Conversion"))
    b.append(p(
        "Cổng logic (XOR, hoặc flip-flop được kích bởi hai tín hiệu) tạo xung có độ rộng Δt tỉ lệ với φ. "
        "Trung bình xung qua bộ lọc thông thấp (hoặc dùng bộ đếm đo Δt) cho điện áp:"))
    b.append(eq("V_out = K · (Δt / T) = K · φ / 360°   (với φ tính bằng độ)"))
    b.append(p(
        "Đây là nguyên lý của các pha kế điện tử và IC đo pha, cho độ chính xác cao (0,1°–0,5°) trên dải "
        "tần rộng. Nhược điểm: nhạy với méo dạng sóng (sai lệch zero-crossing khi có hài)."))

    b.append(h2("41.3 Phương pháp số và tương quan", "Digital and Correlation Methods"))
    b.append(p(
        "Xử lý số (DSP) lấy mẫu hai tín hiệu, tính thành phần chéo của phổ: φ = arctan(Im{S_xy}/Re{S_xy}), "
        "hoặc dùng cross-correlation cực đại tại độ trễ τ₀ với φ = 2πfτ₀. Cách này miễn nhiễm nhiễu tốt "
        "hơn nhờ lọc và trung bình, và đo được cả khi tín hiệu yếu."))

    b.append(h2("41.4 Ứng dụng", "Applications"))
    b.append(p(
        "Đo pha được dùng để xác định trở kháng Z = V/I và góc pha của nó (từ đó R, L, C); đo hệ số công "
        "suất; cảm biến LVDT (vị trí từ độ lệch pha cuộn sơ/tha cấp); đo độ ẩm bằng cảm biến điện môi "
        "(độ trễ pha thay đổi theo ε); và trong radar/sonar để xác định khoảng cách (φ ≅ 2πd/λ)."))

    b.append(h2("41.5 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Độ chính xác", "Dải tần", "Ghi chú"],
        [["Lissajous", "1°–2°", "DC–băng thông scope", "Trực quan, định tính"],
         ["XOR / chuyển đổi Δt", "0,1°–0,5°", "vài Hz – MHz", "Nhạy méo sóng"],
         ["Số / DSP", "0,01°–0,1°", "rất rộng", "Miễn nhiễm nhiễu tốt"],
         ["Cầu pha", "0,1°–1°", "Âm thanh – RF", "Cân bằng thủ công"]],
        "Bảng 41.1 · Các phương pháp đo pha."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Đo pha xác định góc lệch φ giữa hai tín hiệu cùng tần số. Lissajous cho đánh giá nhanh (sinφ = "
        "x₀/X_max); chuyển đổi thời gian–điện áp (XOR/flip-flop) cho V ∝ φ với độ chính xác 0,1°–0,5°; DSP "
        "qua cross-correlation/phổ cho độ chính xác cao nhất và miễn nhiễm nhiễu. Ứng dụng: trở kháng, hệ "
        "số công suất, cảm biến LVDT, độ ẩm, radar."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 41. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Phase φ is the time displacement between two equal-frequency signals. With v₁=V₁sinωt and "
        "v₂=V₂sin(ωt−φ), φ is found from the relative zero-crossings or from the cross-correlation. The "
        "Lissajous method applies the two signals to the X and Y scope axes: φ=0 gives a diagonal line, "
        "φ=90° an ellipse (circle if amplitudes equal); for an ellipse sinφ = x₀/X_max = y₀/Y_max where "
        "x₀ is the intercept at Y=0. It is qualitative (1°–2°)."))
    b.append(p(
        "Time-to-voltage conversion uses a logic gate (XOR or a flip-flop) to produce a pulse of width Δt "
        "∝ φ; averaging (or counting Δt) yields V_out = K·φ/360°. Electronic phase meters and ICs reach "
        "0.1°–0.5° but are sensitive to waveform distortion (false zero-crossings). Digital methods sample "
        "both signals and compute φ = arctan(Im{S_xy}/Re{S_xy}) or the lag τ₀ of the cross-correlation peak "
        "(φ = 2πfτ₀), giving 0.01°–0.1° with good noise immunity. Applications: impedance Z=V/I and its "
        "phase (hence R, L, C), power factor, LVDT position, dielectric moisture sensing, and radar/sonar "
        "ranging (φ ≈ 2πd/λ)."))
    b.append(table(
        ["Method", "Accuracy", "Freq. range", "Note"],
        [["Lissajous", "1°–2°", "DC–scope BW", "Visual, qualitative"],
         ["XOR / Δt conv.", "0.1°–0.5°", "Hz–MHz", "Distortion-sensitive"],
         ["Digital / DSP", "0.01°–0.1°", "very wide", "Best noise immunity"],
         ["Phase bridge", "0.1°–1°", "audio–RF", "Manual nulling"]],
        "Table 41.1 · Phase-measurement methods."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE, body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
