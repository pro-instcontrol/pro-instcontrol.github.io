# -*- coding: utf-8 -*-
"""Handbook Chapter 73 — Environmental Measurement (Đo môi trường).
Run:  python build/reader_hb_ch73.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch73-environmental-measurement"
CH_NO = 73
TITLE_EN = "Environmental Measurement"
TITLE_VI = "Đo môi trường"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Đo môi trường quan trắc chất lượng không khí, nước, đất và tiếng ồn để bảo vệ sức khoẻ và tuân thủ "
        "quy chuẩn. Các chất ô nhiễm không khí tiêu chuẩn: SO₂, NO₂/NOx, O₃, CO, PM10/PM2.5, cùng benzene và "
        "kim loại nặng. Chỉ số chất lượng không khí (AQI) tổng hợp từ các chất này."))
    b.append(p(
        "Trạm quan trắc tự động đo liên tục với thiết bị phân tích chuyên dụng, kèm thu khí hiệu chuẩn và kiểm "
        "soát nhiệt độ."))

    b.append(h2("73.1 Máy phân tích khí tiêu chuẩn", "Standard Gas Analyzers"))
    b.append(p(
        "<b>SO₂</b>: huỳnh quang UV (UV fluorescence) — SO₂ hấp thụ UV (214 nm) phát lại huỳnh quang ∝ nồng độ. "
        "<b>NO/NOx</b>: hoá phát quang (chemiluminescence) — NO + O₃ → NO₂* phát sáng; NOx đo sau khi qua bộ "
        "chuyển đổi NO₂→NO. <b>O₃</b>: hấp thụ UV 254 nm (phương pháp photometric). <b>CO</b>: NDIR (Ch. 70). "
        "Các máy này đạt ppb và là chuẩn quy định (US EPA/EN)."))

    b.append(h2("73.2 Đo bụi lơ lửng PM", "Particulate Matter (PM)"))
    b.append(p(
        "<b>PM10/PM2.5</b> đo bằng: (1) <b>suy hao beta</b> (beta attenuation) — bụi lọc trên băng, đo hấp thụ "
        "β của C-14; (2) <b>TEOM</b> (tapered element oscillating microbalance) — tần số dao động thay đổi theo "
        "khối lượng bụi; (3) <b>tán xạ quang</b> (nephelometer) giá rẻ, dùng cảm biến giá thấp; (4) cân trọng "
        "lượng theo chuẩn (reference method)."))

    b.append(h2("73.3 Nước, đất và tiếng ồn", "Water, Soil and Noise"))
    b.append(p(
        "<b>Nước</b>: pH, DO (oxy hoà tan — điện cực màng hoặc luminescence), độ dẫn, COD/BOD, NO₃⁻, NH₄⁺, kim "
        "loại nặng (ICP-MS), độ đục (Ch. 62). <b>Đất</b>: pH, kim loại nặng, độ ẩm, hữu cơ. <b>Tiếng ồn</b>: "
        "sound level meter đo dB(A) theo chuẩn IEC 61672, quan trắc 24h cho quy hoạch đô thị."))

    b.append(h2("73.4 Thông số", "Specifications"))
    b.append(table(
        ["Chất/thông số", "Phương pháp", "Dải", "Độ chính xác"],
        [["SO₂", "UV fluorescence", "ppb–ppm", "±2%"],
         ["NO/NOx", "Chemiluminescence", "ppb–ppm", "±2%"],
         ["O₃", "UV photometric", "ppb–ppm", "±2%"],
         ["CO", "NDIR", "ppm–%", "±2%"],
         ["PM2.5/PM10", "Beta, TEOM, trọng lượng", "µg/m³", "±5%–10%"],
         ["Tiếng ồn", "dB(A), IEC 61672", "30–140 dB", "±0,5–1 dB"]],
        "Bảng 73.1 · Các phép đo môi trường."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "SO₂ đo bằng UV fluorescence; NOx bằng chemiluminescence; O₃ bằng UV 254 nm; CO bằng NDIR — đạt ppb, "
        "chuẩn EPA/EN. PM đo bằng beta attenuation/TEOM/tán xạ. Nước: pH, DO, độ dẫn, ICP-MS; đất: pH, kim loại; "
        "ồn: dB(A). Trạm quan trắc tự động tổng hợp thành AQI."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 73. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Environmental monitoring covers air, water, soil and noise for health protection and compliance. "
        "Criteria air pollutants: SO₂ (UV fluorescence — absorption at 214 nm and re-emitted fluorescence ∝ "
        "concentration), NO/NOx (chemiluminescence — NO+O₃→NO₂* emits light; NOx after an NO₂→NO converter), "
        "O₃ (UV photometric at 254 nm), CO (NDIR) — ppb-level analyzers meeting US EPA/EN reference methods. "
        "Particulate matter PM10/PM2.5: beta attenuation (C-14 through a filter tape), TEOM "
        "(tapered-element oscillating microbalance), optical scattering (low-cost sensors), and gravimetric "
        "reference. Water: pH, dissolved oxygen (membrane or luminescence), conductivity, COD/BOD, NO₃⁻/NH₄⁺, "
        "heavy metals (ICP-MS), turbidity (Ch. 62). Soil: pH, heavy metals, moisture, organics. Noise: dB(A) "
        "sound level meters per IEC 61672 for 24-h urban monitoring; stations aggregate into AQI."))
    b.append(table(
        ["Parameter", "Method", "Range", "Accuracy"],
        [["SO₂", "UV fluorescence", "ppb–ppm", "±2%"],
         ["NO/NOx", "Chemiluminescence", "ppb–ppm", "±2%"],
         ["O₃", "UV photometric", "ppb–ppm", "±2%"],
         ["CO", "NDIR", "ppm–%", "±2%"],
         ["PM2.5/PM10", "Beta, TEOM, grav.", "µg/m³", "±5%–10%"],
         ["Noise", "dB(A), IEC 61672", "30–140 dB", "±0.5–1 dB"]],
        "Table 73.1 · Environmental measurements."))
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
