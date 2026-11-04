# -*- coding: utf-8 -*-
"""Handbook Chapter 67 — Charged Particle Measurement (Đo hạt tích điện).
Run:  python build/reader_hb_ch67.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch67-charged-particle-measurement"
CH_NO = 67
TITLE_EN = "Charged Particle Measurement"
TITLE_VI = "Đo hạt tích điện"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Hạt tích điện (α, β, electron, ion nặng) ion hóa môi trường khi đi qua; tổn hao năng lượng trên "
        "đơn vị đường đi dE/dx tuân theo <b>định luật Bethe–Bloch</b> và phụ thuộc z²/β² (z: điện tích, β: tốc "
        "độ). Điều này cho phép đo cả năng lượng và nhận diện hạt (ΔE–E telescopes)."))
    b.append(p(
        "Hạt α có tầm ngắn (vài cm trong khí, vài chục µm trong rắn) — cần đầu dò mỏng đặt sát nguồn; hạt β "
        "xuyên xa hơn. Đo gồm: đếm (activity), phổ năng lượng (spectrometry), và theo dõi quỹ đạo (tracking)."))

    b.append(h2("67.1 Detector bán dẫn Si", "Silicon Semiconductor Detectors"))
    b.append(p(
        "<b>Si surface barrier</b> hoặc <b>Si PIN</b> là chuẩn cho phổ α: điện tích sinh ∝ năng lượng, phân giải "
        "FWHM ~15–30 keV tại 5,5 MeV (α của Am-241). Đầu dò mỏng (ΔE) ghép đầu dò dày (E) thành <b>telescope</b> "
        "ΔE–E để nhận diện hạt theo z theo quan hệ ΔE ≈ z²·E/dx."))

    b.append(h2("67.2 Buồng khí và dây (proportional, drift, TPC)", "Gas Chambers"))
    b.append(p(
        "Counter tỉ lệ, buồng trôi (drift), và TPC dùng khí ion hóa: electron sinh ra trôi về dây anode, xung "
        "tỉ lệ với năng lượng; đo thời gian trôi cho vị trí. Đây là công nghệ chính của vật lý hạt và experiment "
        "nghiên cứu, đo cả quỹ đạo (tracking) với phân giải tốt."))

    b.append(h2("67.3 Các phép đo", "Measurements"))
    b.append(p(
        "• <b>Đếm</b> (độ hoạt động): GM/counter tỉ lệ, hiệu chuẩn hiệu suất. "
        "• <b>Phổ năng lượng</b>: Si, HPGe, pha xung. "
        "• <b>Nhận diện hạt</b>: ΔE–E, time-of-flight (TOF). "
        "• <b>Quỹ đạo</b>: tracking buồng khí trong từ trường (suy p/z theo độ cong)."))

    b.append(h2("67.4 Thông số", "Specifications"))
    b.append(table(
        ["Detector", "Hạt", "Phân giải", "Ứng dụng"],
        [["Si surface barrier", "α", "15–30 keV @5,5 MeV", "Phổ α"],
         ["Si PIN", "α, β", "Tốt", "Sơn, môi trường"],
         ["Counter tỉ lệ", "α, β", "Thấp", "Đếm, tách α/β"],
         ["Drift / TPC", "Tất cả tích điện", "Vị trí 100 µm", "Vật lý hạt"],
         ["Telescope ΔE–E", "Ion nặng", "Nhận diện z", "Nghiên cứu hạt"]],
        "Bảng 67.1 · Các detector hạt tích điện."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Hạt tích điện ion hóa môi trường; dE/dx theo Bethe–Bloch ∝ z²/β². Si surface barrier/PIN là chuẩn phổ "
        "α (FWHM 15–30 keV); telescope ΔE–E nhận diện hạt; buồng khí (proportional/drift/TPC) đo năng lượng, "
        "vị trí và quỹ đạo trong vật lý hạt."))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 67. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Charged particles (α, β, electrons, heavy ions) ionize matter; the energy loss per path length dE/dx "
        "follows the Bethe–Bloch law, ∝ z²/β² — enabling both energy measurement and particle identification "
        "(ΔE–E telescopes). Alphas have very short range (cm in air, tens of µm in solids), so thin detectors "
        "close to the source are needed; betas penetrate farther. Si surface-barrier or PIN diodes are the alpha-"
        "spectrometry standard (FWHM 15–30 keV at 5.5 MeV, Am-241); a thin ΔE detector in front of a thick E "
        "detector forms a ΔE–E telescope identifying particles by charge. Gas chambers (proportional, drift, TPC) "
        "give proportional pulses and, with drift time, position — the core technology of particle physics "
        "tracking, also used in magnetic fields to reconstruct momentum p/z from curvature."))
    b.append(table(
        ["Detector", "Particles", "Resolution", "Use"],
        [["Si surface barrier", "α", "15–30 keV @5.5 MeV", "Alpha spec."],
         ["Si PIN", "α, β", "Good", "Surfaces, environ."],
         ["Proportional", "α, β", "Low", "Counting, α/β"],
         ["Drift / TPC", "All charged", "100 µm position", "Particle physics"],
         ["ΔE–E telescope", "Heavy ions", "z identification", "Research"]],
        "Table 67.1 · Charged-particle detectors."))
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
