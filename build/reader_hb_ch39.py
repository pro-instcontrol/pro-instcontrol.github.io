# -*- coding: utf-8 -*-
"""Handbook Chapter 39 — Power Measurement (Đo công suất điện).
Run:  python build/reader_hb_ch39.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch39-power-measurement"
CH_NO = 39
TITLE_EN = "Power Measurement"
TITLE_VI = "Đo công suất điện"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Công suất (power) là tốc độ truyền năng lượng. Với một phần tử hai cực, công suất tức thời là "
        "tích của điện áp và dòng điện tại mỗi thời điểm: p(t) = v(t)·i(t). Tích phân theo thời gian cho "
        "năng lượng. Trong đo lường, người ta quan tâm đến công suất trung bình (tác dụng) và các thành "
        "phần công suất trong mạch xoay chiều."))
    b.append(p(
        "Ở một chiều (DC), công suất trung bình đơn giản là P = V·I. Ở xoay chiều (AC) hình sine, nếu điện "
        "áp và dòng lệch pha một góc φ:"))
    b.append(eq("P = (1/T) ∫₀ᵀ v(t)·i(t) dt = V_rms · I_rms · cos φ"))
    b.append(p(
        "Trong đó cos φ được gọi là <b>hệ số công suất</b> (power factor). Ngoài công suất tác dụng P, còn "
        "có công suất phản kháng Q = V_rms·I_rms·sin φ và công suất biểu kiến S = V_rms·I_rms, với quan hệ "
        "S² = P² + Q². Đơn vị: P và Q tính bằng watt (W) và var, S bằng volt-ampere (VA)."))

    b.append(h2("39.1 Watt kế điện động", "Electrodynamic Wattmeter"))
    b.append(p(
        "Watt kế (wattmeter) đo P trực tiếp nhờ cấu trúc điện động: một <b>cuộn dòng</b> (current coil) nối "
        "tiếp với tải mang toàn bộ dòng I, và một <b>cuộn áp</b> (potential coil) nối song song mang dòng "
        "tỉ lệ với V. Mômen quay sinh ra tỉ lệ với tích v·i, nên kim chỉ thị giá trị trung bình — chính là "
        "công suất tác dụng. Watt kế kiểu này dùng được cho DC và AC ở tần số công nghiệp."))
    b.append(p(
        "Sai số chủ yếu do <b>sai lệch pha</b> của cuộn áp (voltage-coil phase error) và điện áp gánh "
        "(burden) của cuộn dòng. Ở tần số cao hoặc hệ số công suất thấp, sai lệch pha này gây lỗi lớn nên "
        "phải dùng watt kế hiệu chỉnh hoặc điện tử."))

    b.append(h2("39.2 Đo công suất ba pha", "Three-Phase Power"))
    b.append(p(
        "Trong hệ ba pha ba dây (3 dây), người ta dùng <b>phương pháp hai watt kế</b> (two-wattmeter "
        "method): hai watt kế nối vào hai cặp dây pha bất kỳ, tổng hai chỉ thị bằng tổng công suất ba pha:"))
    b.append(eq("P_tot = W₁ + W₂ ,  W₁ = V_L·I_L·cos(30°+φ) ,  W₂ = V_L·I_L·cos(30°−φ)"))
    b.append(p(
        "Từ tỉ số hai chỉ thị có thể suy ra góc φ và hệ số công suất. Hệ ba pha bốn dây (3 dây + trung "
        "tính) thường dùng ba watt kế (three-wattmeter method) để đo đúng ngay cả khi tải không cân bằng."))

    b.append(h2("39.3 Watt kế điện tử và đo công suất có hài", "Electronic Wattmeters and Harmonic Power"))
    b.append(p(
        "Watt kế điện tử nhân hai tín hiệu tức thời v(t) và i(t) bằng bộ nhân tương tự (analog multiplier) "
        "hoặc qua chuyển đổi tương tự–số, sau đó lọc thông thấp (LPF) lấy giá trị trung bình. Các vi mạch "
        "chuyên dụng (như họ ADE7xxx) tích hợp bộ nhân, ADC và tính toán P, Q, S, năng lượng và hệ số công "
        "suất theo thời gian thực."))
    b.append(p(
        "Khi có sóng hài (harmonics), công suất tổng là tổng theo từng thành phần: "
        "P = Σₙ Vₙ·Iₙ·cos θₙ, với θₙ là độ lệch pha tại họ n. Watt kế điện tử dựa trên nhân tức thời đo "
        "đúng tổng công suất thực, khác với các phương pháp chỉ dùng giá trị cơ bản."))

    b.append(h2("39.4 Thông số và sai số", "Specifications and Errors"))
    b.append(table(
        ["Thông số", "Ý nghĩa", "Điển hình"],
        [["Dải công suất", "Từ mW đến MW", "qua biến dòng / biến áp đo"],
         ["Hệ số công suất", "cos φ đo được", "0,1 – 1,0 (lead/lag)"],
         ["Độ chính xác", "Sai số FS", "0,1% – 0,5% (điện tử)"],
         ["Tần số", "Dải làm việc", "DC – vài kHz (điện động); MHz (IC)"],
         ["Sai số pha", "Lỗi cuộn áp", "< 0,1° (hiệu chỉnh)"],
         ["Hài", "Đo đa tần", "Có (nhân tức thời)"]],
        "Bảng 39.1 · Thông số watt kế."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Công suất trung bình P = V_rms·I_rms·cosφ (AC) hoặc V·I (DC). Watt kế điện động dùng cuộn dòng "
        "tiếp xúc và cuộn áp song song, chỉ thị tích trung bình. Ba pha đo bằng hai hoặc ba watt kế. Watt "
        "kế điện tử nhân tức thời v·i rồi lấy trung bình, đo đúng cả công suất có hài: P = Σ VₙIₙcosθₙ."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 39. Equations and the table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Instantaneous power is p(t)=v(t)·i(t). For DC, P=V·I. For sinusoidal AC with phase angle φ, "
        "P = V_rms·I_rms·cosφ; the reactive power Q = V_rms·I_rms·sinφ and apparent power S = V_rms·I_rms, "
        "with S²=P²+Q². Units: W, var, VA."))
    b.append(p(
        "An electrodynamic wattmeter uses a current coil in series (carrying I) and a potential coil in "
        "parallel (carrying current ∝ V); the torque ∝ v·i, so the pointer reads the average — the real "
        "power. Errors come from the potential-coil phase error and the current-coil burden; at high "
        "frequency or low power factor a phase-compensated or electronic meter is needed."))
    b.append(p(
        "Three-phase power uses the two-wattmeter method (P_tot = W₁+W₂, with W₁=V_L I_L cos(30°+φ), "
        "W₂=V_L I_L cos(30°−φ)); the ratio yields φ and PF. A four-wire (three-phase + neutral) system "
        "uses three wattmeters. Electronic wattmeters multiply v(t)·i(t) in real time (analog multiplier "
        "or ADC) and low-pass filter the average; dedicated ICs (e.g. ADE7xxx) compute P, Q, S, energy and "
        "PF. With harmonics, P = Σ VₙIₙcosθₙ — the instantaneous multiplier reads the true total, unlike "
        "fundamental-only methods."))
    b.append(table(
        ["Parameter", "Meaning", "Typical"],
        [["Power range", "mW to MW", "via CT/VT"],
         ["Power factor", "cos φ measured", "0.1–1.0 lead/lag"],
         ["Accuracy", "Error FS", "0.1%–0.5% (electronic)"],
         ["Frequency", "Operating band", "DC–kHz (dynam); MHz (IC)"],
         ["Phase error", "Potential-coil error", "< 0.1° (compensated)"],
         ["Harmonics", "Multi-frequency", "Yes (instantaneous mult.)"]],
        "Table 39.1 · Wattmeter specifications."))
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
