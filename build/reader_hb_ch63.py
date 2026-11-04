# -*- coding: utf-8 -*-
"""Handbook Chapter 63 — Laser Output Measurement (Đo đầu ra laser).
Run:  python build/reader_hb_ch63.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch63-laser-output-measurement"
CH_NO = 63
TITLE_EN = "Laser Output Measurement"
TITLE_VI = "Đo đầu ra laser"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Đo đầu ra laser gồm: <b>công suất</b> (W) hoặc <b>năng lượng xung</b> (J), bước sóng, độ phân kỳ chùm "
        "(M²), đường kính và phân bố chùm, độ ổn định, và phổ. Mỗi đại lượng dùng thiết bị riêng."))
    b.append(p(
        "Công suất đo bằng <b>thermopile</b> (hấp thụ toàn bộ, dải rộng, cho laser liên tục và xung dài), "
        "<b>photodiode</b> (nhạy, nhanh, cho công suất nhỏ và đo phổ), hoặc <b>calorimeter</b> (chuẩn). Năng "
        "lượng xung đo bằng đầu dò <b>pyroelectric</b> hoặc joulemeter; tốc độ xung cao dùng photodiode tốc độ "
        "nhanh."))

    b.append(h2("63.1 Chất lượng chùm M² và beam profile", "Beam Quality M² and Profile"))
    b.append(p(
        "Độ phân kỳ chùm M² cho biết chùm gần lý tưởng Gaussian như thế nào: M² = 1 là lý tưởng, M² lớn hơn là "
        "chùm tệ hơn. Đo bằng cách hội tụ chùm qua thấu kính, quét beam profile (CCD, camera hoặc lưỡi dao quay) "
        "ở nhiều vị trí dọc trục z, và tính từ bán kính chùm w(z):"))
    b.append(eq("M² = (π·w₀·θ) / λ   (w₀: waist, θ: độ phân kỳ)")
    )
    b.append(p(
        "Phân bố chùm (beam profile) hiển thị bằng camera CCD/CMOS hoặc camera pyroelectric (cho IR), dùng "
        "hiệu chỉnh quang học laser và quan trắc hotspot."))

    b.append(h2("63.2 Bước sóng và phổ", "Wavelength and Spectrum"))
    b.append(p(
        "Bước sóng đo bằng <b>wavemeter</b> ( interferometer Fizeau/Michelson) chính xác 10⁻⁶, hoặc "
        "<b> spectrometer</b> (mạng lưới). Phổ laser (vạch, độ rộng) đo bằng Fabry–Perot hoặc OSA (optical "
        "spectrum analyzer) — cần thiết cho WDM và laser ứng dụng quang phổ."))

    b.append(h2("63.3 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Phương pháp", "Dải", "Độ chính xác"],
        [["Công suất CW", "Thermopile", "µW–kW", "±1%–3%"],
         ["Công suất nhỏ", "Photodiode", "nW–mW", "±1%"],
         ["Năng lượng xung", "Pyroelectric", "µJ–J", "±3%"],
         ["M²", "Lens + CCD quét", "1–50", "±2%–5%"],
         ["Bước sóng", "Wavemeter", "10⁻⁶ chính xác", "±10⁻⁶"],
         ["Phổ", "OSA/Fabry–Perot", "0,01–1 nm", "±0,01 nm"]],
        "Bảng 63.1 · Các phép đo đầu ra laser."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Đo laser: công suất (thermopile/photodiode/calorimeter), năng lượng xung (pyroelectric), chất lượng "
        "chùm M² = πw₀θ/λ qua lens + CCD, bước sóng (wavemeter) và phổ (OSA). Laser liên tục dùng thermopile; "
        "xung dùng pyroelectric/joulemeter."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 63. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Laser output measurement covers power (W) or pulse energy (J), wavelength, beam quality M², beam "
        "diameter/profile, stability and spectrum. Power: a thermopile absorbs everything (broad range, CW and "
        "long pulses), a photodiode is fast and sensitive (small powers, spectral), and a calorimeter is the "
        "primary standard. Pulse energy uses a pyroelectric detector or joulemeter; high-repetition-rate pulses "
        "use fast photodiodes. Beam quality M² = π·w₀·θ/λ (w₀ waist, θ divergence; M² = 1 ideal Gaussian) is "
        "measured by focusing through a lens and profiling the beam (CCD/camera or scanning-knife-edge) at several "
        "axial positions z; beam profiles reveal hotspots and guide optics alignment. Wavelength: a wavemeter "
        "(Fizeau/Michelson interferometer) reaches 10⁻⁶; the spectrum (line width) is measured by a Fabry–Perot "
        "or an optical spectrum analyzer (OSA) — required for WDM and spectroscopic lasers."))
    b.append(table(
        ["Quantity", "Method", "Range", "Accuracy"],
        [["CW power", "Thermopile", "µW–kW", "±1%–3%"],
         ["Small power", "Photodiode", "nW–mW", "±1%"],
         ["Pulse energy", "Pyroelectric", "µJ–J", "±3%"],
         ["M²", "Lens + CCD", "1–50", "±2%–5%"],
         ["Wavelength", "Wavemeter", "10⁻⁶", "±10⁻⁶"],
         ["Spectrum", "OSA / Fabry–Perot", "0.01–1 nm", "±0.01 nm"]],
        "Table 63.1 · Laser-output measurements."))
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
