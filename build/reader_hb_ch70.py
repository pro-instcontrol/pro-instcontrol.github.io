# -*- coding: utf-8 -*-
"""Handbook Chapter 70 — Composition Measurement (Đo thành phần).
Run:  python build/reader_hb_ch70.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch70-composition-measurement"
CH_NO = 70
TITLE_EN = "Composition Measurement"
TITLE_VI = "Đo thành phần"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Đo thành phần</b> (composition measurement) xác định nồng độ/tỉ lệ các chất trong hỗn hợp khí, "
        "lỏng hoặc rắn. Các kỹ thuật chính: hấp thụ quang phổ (IR, UV), sắc ký (GC, LC), khối phổ (MS), điện "
        "hoá, và tính chất vật lý (tỷ trọng, dẫn nhiệt, từ tính)."))

    b.append(h2("70.1 Hấp thụ hồng ngoại (NDIR)", "NDIR Absorption"))
    b.append(p(
        "Nhiều khí (CO₂, CO, CH₄, hydrocarbon) hấp thụ IR ở bước sóng đặc trưng. Máy <b>NDIR</b> (non-dispersive "
        "infrared) chiếu IR qua buồng mẫu và đo suy hao tại dải chọn lọc bằng bộ lọc; theo Beer–Lambert:"))
    b.append(eq("I = I₀·e^(−ε·c·l)"))
    b.append(p(
        "với c là nồng độ, l chiều dài đường quang. NDIR là phương pháp chủ đạo cho CO₂ trong kiểm soát môi "
        "trường, HVAC và y tế (capnography)."))

    b.append(h2("70.2 Sắc ký khí và khối phổ", "Gas Chromatography and Mass Spectrometry"))
    b.append(p(
        "<b>GC</b> tách các thành phần theo thời gian lưu trên cột, rồi đo bằng detector (FID, TCD, ECD) — cho "
        "phân tích đa thành phần chính xác, dùng phòng thí nghiệm và process GC trực tuyến. <b>MS</b> ion hoá "
        "phân tử và phân tích theo tỉ lệ m/z — nhận diện và định lượng cực nhạy (ppb), dùng môi trường, khí hậu, "
        "an ninh."))

    b.append(h2("70.3 Đo khí cụ thể", "Specific Gas Measurements"))
    b.append(p(
        "<b>O₂</b>: cảm biến từ tính (paramagnetic — chuẩn), cell zirconia (khí thải, lò), cell điện hoá (máy "
        "đo cầm tay). <b>CO₂</b>: NDIR. <b>CO, H₂S</b>: cell điện hoá. <b>Độ ẩm khí</b>: xem Ch. 72. "
        "<b>Độ dẫn nhiệt</b> (TCD) đo H₂, He trong hỗn hợp. Cảm biến bán dẫn (metal-oxide) cho khí cháy nổ "
        "rẻ tiền."))

    b.append(h2("70.4 Thông số", "Specifications"))
    b.append(table(
        ["Kỹ thuật", "Chất", "Dải", "Ứng dụng"],
        [["NDIR", "CO₂, CO, CH₄", "ppm–%", "Môi trường, HVAC"],
         ["Paramagnetic O₂", "O₂", "0,1–100%", "Chuẩn, khí thải"],
         ["Zirconia cell", "O₂", "10⁻¹⁸–100%", "Lò, khí thải"],
         ["Cell điện hoá", "CO, H₂S, O₂", "ppb–ppm", "Cầm tay, an toàn"],
         ["Process GC", "Đa thành phần", "ppm–%", "Công nghiệp"],
         ["MS", "Đa thành phần", "ppt–%", "Nghiên cứu, khí hậu"]],
        "Bảng 70.1 · Các kỹ thuật đo thành phần."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Đo thành phần dùng hấp thụ quang (NDIR theo Beer–Lambert cho CO₂/CO/CH₄), O₂ bằng từ tính/zirconia, "
        "khí độc bằng cell điện hoá, phân tích đa thành phần bằng GC/MS. Chọn kỹ thuật theo chất cần đo, dải "
        "nồng độ và môi trường (trực tuyến hay phòng thí nghiệm)."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 70. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Composition measurement determines the concentration of species in gas/liquid/solid mixtures via "
        "spectroscopic absorption (IR, UV), chromatography (GC, LC), mass spectrometry, electrochemistry, or "
        "physical properties. NDIR measures gases with characteristic IR absorption (CO₂, CO, CH₄, "
        "hydrocarbons) through a filter-selected band following Beer–Lambert I = I₀·e^(−ε·c·l) — the dominant "
        "CO₂ method for environmental, HVAC and medical (capnography) use. GC separates components by column "
        "retention time with FID/TCD/ECD detection — accurate multi-component lab and online process analysis. "
        "MS ionizes and analyzes by m/z with ppt sensitivity. Specific gases: O₂ by paramagnetic (reference "
        "method) or zirconia cell (flues, furnaces); CO/H₂S by electrochemical cells; H₂/He by thermal "
        "conductivity (TCD); metal-oxide sensors for low-cost combustible gas."))
    b.append(table(
        ["Technique", "Species", "Range", "Use"],
        [["NDIR", "CO₂, CO, CH₄", "ppm–%", "Env., HVAC"],
         ["Paramagnetic O₂", "O₂", "0.1–100%", "Reference, flue"],
         ["Zirconia cell", "O₂", "10⁻¹⁸–100%", "Furnaces"],
         ["Electrochemical", "CO, H₂S, O₂", "ppb–ppm", "Handheld, safety"],
         ["Process GC", "Multi", "ppm–%", "Industrial"],
         ["MS", "Multi", "ppt–%", "Research, climate"]],
        "Table 70.1 · Composition techniques."))
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
