# -*- coding: utf-8 -*-
"""Handbook Chapter 55 — Microwave Measurement (Đo vi ba).
Run:  python build/reader_hb_ch55.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch55-microwave-measurement"
CH_NO = 55
TITLE_EN = "Microwave Measurement"
TITLE_VI = "Đo vi ba"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Vùng <b>vi ba</b> (microwave) từ ~1 GHz đến vài chục GHz, nơi bước sóng nhỏ hơn hoặc cỡ kích thước "
        "mạch, nên dòng và áp không còn xác định cục bộ mà phải dùng lý thuyết đường truyền (transmission line): "
        "sóng truyền trên dây dẫn, waveguide, với trở kháng đặc tính Z₀ (thường 50 Ω). Các phép đo vi ba đo các "
        "thông số phân tán (S-parameters) thay vì R, L, C trực tiếp."))

    b.append(h2("55.1 Các tham số S và phản xạ", "S-Parameters and Reflection"))
    b.append(p(
        "Tại cổng i, sóng tới a_i và sóng phản xạ b_i liên hệ qua ma trận S. Hệ số phản xạ Γ = (Z−Z₀)/(Z+Z₀) "
        "cho biết mức không khớp. Tỷ số sóng đứng (VSWR) liên hệ:"))
    b.append(eq("VSWR = (1+|Γ|)/(1−|Γ|) ,   |Γ| = (VSWR−1)/(VSWR+1)"))
    b.append(p(
        "Đo VSWR/Γ bằng <b>cầu định hướng</b> (directional coupler) tách sóng tới và sóng tới/sóng phản xạ, hoặc "
        "bằng <b>vector network analyzer</b> (VNA) đo trực tiếp S₁₁, S₂₁ trên dải tần rộng."))

    b.append(h2("55.2 Đo công suất vi ba", "Power Measurement"))
    b.append(p(
        "Đầu dò công suất: <b>bolometer/thermistor</b> (điện trở thay đổi theo nhiệt do công suất hấp thụ), "
        "<b>diode detector</b> (tốc độ cao, công suất thấp), và <b>calorimeter</b> (đo nhiệt lượng, chuẩn). "
        "Chúng hiệu chuẩn thành đầu đo công suất (power meter) đọc W hoặc dBm."))

    b.append(h2("55.3 Đo tần số và pha", "Frequency and Phase"))
    b.append(p(
        "Tần số đo bằng <b>bộ đếm</b> (frequency counter) hoặc <b>hốc cộng hưởng chuẩn</b> (cavity wavemeter) "
        "từ dịch tần số cộng hưởng. Pha đo bằng VNA so sánh pha giữa hai cổng trên từng tần số — cho cả biên độ "
        "và pha của S₂₁."))

    b.append(h2("55.4 Đo từ thông và điện môi ở vi ba", "E-field, B-field, Dielectric at Microwave"))
    b.append(p(
        "Hằng số điện môi và từ thẩm đo bằng hốc cộng hưởng hoặc phương pháp không gian tự do (xem Ch. 46). Từ "
        "trường và điện trường đo bằng đầu dò nhỏ (dipole, vòng) hiệu chuẩn. Các phép đo này dùng trong radar, "
        "thông tin và vật liệu."))

    b.append(h2("55.5 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Phương pháp", "Dải"],
        [["Γ, VSWR, S₁₁", "Hướng, VNA", "MHz–GHz"],
         ["S₂₁ (truyền)", "VNA", "MHz–GHz"],
         ["Công suất", "Bolometer/diode", "−70 đến +30 dBm"],
         ["Tần số", "Counter, wavemeter", "MHz–GHz"],
         ["ε_r, μ_r", "Hốc, free-space", "GHz"]],
        "Bảng 55.1 · Các phép đo vi ba."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Vi ba dùng lý thuyết đường truyền với Z₀=50 Ω; đo tham số S thay vì R,L,C. Γ = (Z−Z₀)/(Z+Z₀), VSWR = "
        "(1+|Γ|)/(1−|Γ|) đo bằng cầu định hướng hoặc VNA (S₁₁, S₂₁). Công suất đo bằng bolometer/diode/calorimeter; "
        "tần số bằng counter/wavemeter; pha bằng VNA. ε_r, μ_r đo bằng hốc cộng hưởng hoặc không gian tự do."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 55. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "The microwave band (~1 GHz to tens of GHz) has wavelengths comparable to circuit dimensions, so currents "
        "and voltages are no longer locally defined; transmission-line theory with characteristic impedance Z₀ "
        "(usually 50 Ω) applies, and measurements use scattering (S) parameters instead of R, L, C. The reflection "
        "coefficient Γ = (Z−Z₀)/(Z+Z₀) quantifies mismatch; VSWR = (1+|Γ|)/(1−|Γ|), with |Γ| = (VSWR−1)/(VSWR+1). "
        "A directional coupler separates forward/reflected waves to measure Γ/VSWR, while a vector network analyzer "
        "(VNA) measures S₁₁, S₂₁ directly across frequency. Power is sensed by a bolometer/thermistor (resistance "
        "changes with absorbed heat), a diode detector (fast, low power) or a calorimeter (primary standard), "
        "calibrated into a power meter (W or dBm). Frequency uses a counter or cavity wavemeter; phase is measured "
        "by the VNA. Permittivity/permeability at microwaves use resonant cavities or free-space methods (Ch. 46)."))
    b.append(table(
        ["Quantity", "Method", "Range"],
        [["Γ, VSWR, S₁₁", "Coupler, VNA", "MHz–GHz"],
         ["S₂₁ (transm.)", "VNA", "MHz–GHz"],
         ["Power", "Bolometer/diode", "−70 to +30 dBm"],
         ["Frequency", "Counter, wavemeter", "MHz–GHz"],
         ["ε_r, μ_r", "Cavity, free-space", "GHz"]],
        "Table 55.1 · Microwave measurements."))
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
