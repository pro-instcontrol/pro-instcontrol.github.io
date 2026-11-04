# -*- coding: utf-8 -*-
"""Handbook Chapter 65 — Radioactivity Measurement (Đo phóng xạ).
Run:  python build/reader_hb_ch65.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch65-radioactivity-measurement"
CH_NO = 65
TITLE_EN = "Radioactivity Measurement"
TITLE_VI = "Đo phóng xạ"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Hoạt độ phóng xạ</b> (activity) là số phân rã trên giây, đơn vị becquerel (Bq = 1 s⁻¹); đơn vị cũ "
        "là curie (1 Ci = 3,7·10¹⁰ Bq). Phân rã tuân theo N(t) = N₀·e^(−λt) với chu kỳ bán rã T½ = ln2/λ. Các "
        "loại bức xạ: <b>alpha</b> (hạt He, đo ngắn), <b>beta</b> (electron, đo vừa), <b>gamma</b> (photon, xuyên "
        "sâu), cùng neutron (Ch. 68)."))
    b.append(p(
        "Đo phóng xạ dùng detector phát hiện ion hóa: buồng ion, counter tỉ lệ, GM (Geiger–Müller), scintillator, "
        "hoặc bán dẫn."))

    b.append(h2("65.1 Counter GM và buồng ion", "GM Counter and Ion Chamber"))
    b.append(p(
        "<b>Counter Geiger–Müller</b> là ống khí với dây trung tâm cao áp; mỗi ion hóa gây một xung lớn — cực "
        "đơn giản, rẻ, đo <b>đếm số</b> (không đo năng lượng), dùng đầu dò và máy đo bức xạ cầm tay. "
        "<b>Buồng ion</b> đo dòng trung bình do ion hóa, tuyến tính theo tốc độ liều — dùng đo liều và môi "
        "trường. <b>Counter tỉ lệ</b> (proportional) hoạt động ở áp thấp hơn, xung tỉ lệ với năng lượng, dùng "
        "tách α/β."))

    b.append(h2("65.2 Detector phát sáng (scintillator)", "Scintillation Detectors"))
    b.append(p(
        "Vật liệu phát sáng (NaI(Tl), CsI, nhựa plastique) chuyển photon/hạt thành ánh sáng, thu bằng "
        "photomultiplier (PMT) hoặc photodiode. Nhiễu thấp, nhạy gamma tốt, dùng cho máy đo phóng xạ và phổ. "
        "NaI(Tl) là chuẩn cổ điển cho phổ gamma giá rẻ; plastique cho counting."))

    b.append(h2("65.3 Detector bán dẫn", "Semiconductor Detectors"))
    b.append(p(
        "Si (đo α, β), HPGe (phổ gamma phân giải cao), CdZnTe. Điện tích sinh ∝ năng lượng, phân giải tốt nhất. "
        "HPGe phải làm lạnh (lỏng/LN2 hoặc cơ khí), dùng phổ gamma định lượng đồng vị chính xác."))

    b.append(h2("65.4 Thông số", "Specifications"))
    b.append(table(
        ["Detector", "Bức xạ", "Phân giải năng lượng", "Ứng dụng"],
        [["GM counter", "α, β, γ", "Không (đếm)", "Cầm tay, môi trường"],
         ["Buồng ion", "γ, X", "Không (dòng)", "Liều, tốc độ liều"],
         ["Counter tỉ lệ", "α, β", "Thấp", "Tách α/β"],
         ["NaI(Tl)", "γ", "6%–8% (662 keV)", "Phổ gamma giá rẻ"],
         ["HPGe", "γ, X", "0,1%–0,2%", "Định lượng đồng vị"],
         ["Si (surface bar.)", "α, β", "Tốt", "Phổ α"]],
        "Bảng 65.1 · Các detector phóng xạ."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Hoạt độ Bq (= s⁻¹), N(t) = N₀e^(−λt). GM counter: đếm, rẻ; buồng ion: dòng ∝ tốc độ liều; counter tỉ "
        "lệ: tách α/β; NaI(Tl): phổ gamma; HPGe: phân giải cao nhất cho định lượng đồng vị; Si cho α/β."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 65. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Activity is the decay rate in becquerel (Bq = s⁻¹); the old unit is the curie (1 Ci = 3.7×10¹⁰ Bq). "
        "Decay follows N(t) = N₀·e^(−λt) with half-life T½ = ln2/λ. Radiation types: alpha (short range), beta "
        "(medium), gamma (penetrating). The Geiger–Müller counter is a high-voltage gas tube producing one large "
        "pulse per ionization — simple and cheap, counts only (no energy), the standard handheld survey meter. "
        "An ion chamber measures the mean ionization current, linear with dose rate — used for dose and "
        "environmental monitoring. A proportional counter operates at lower gain with pulse height ∝ energy, "
        "separating α/β. Scintillators (NaI(Tl), CsI, plastic) convert radiation to light read by a PMT/photodiode: "
        "low noise, good gamma sensitivity, NaI(Tl) the classic budget gamma spectrometer. Semiconductors: Si "
        "(α, β), HPGe (high-resolution gamma spectroscopy, needs cooling), CdZnTe; charge ∝ energy gives the best "
        "resolution (0.1%–0.2% at 662 keV)."))
    b.append(table(
        ["Detector", "Radiation", "Energy res.", "Use"],
        [["GM counter", "α, β, γ", "None (counting)", "Handheld, survey"],
         ["Ion chamber", "γ, X", "None (current)", "Dose, dose rate"],
         ["Proportional", "α, β", "Low", "α/β separation"],
         ["NaI(Tl)", "γ", "6%–8% (662 keV)", "Budget gamma spec."],
         ["HPGe", "γ, X", "0.1%–0.2%", "Isotope quant."],
         ["Si (surface bar.)", "α, β", "Good", "Alpha spec."]],
        "Table 65.1 · Radiation detectors."))
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
