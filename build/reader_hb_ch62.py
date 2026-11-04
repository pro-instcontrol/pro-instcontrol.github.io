# -*- coding: utf-8 -*-
"""Handbook Chapter 62 — Turbidity Measurement (Đo độ đục).
Run:  python build/reader_hb_ch62.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch62-turbidity-measurement"
CH_NO = 62
TITLE_EN = "Turbidity Measurement"
TITLE_VI = "Đo độ đục"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Độ đục</b> (turbidity) là mức giảm độ trong của nước do hạt lơ lửng (bùn, vi tảo, vi khuẩn, keo) "
        "gây tán xạ và hấp thụ ánh sáng. Đơn vị chuẩn: <b>NTU</b> (Nephelometric Turbidity Unit) với dung dịch "
        "chuẩn formazin. Nước uống phải đạt < 1 NTU (chuẩn WHO/EPA), xử lý nước thải theo dõisettling bằng "
        "độ đục."))
    b.append(p(
        "Đo độ đục là chỉ số trực tiếp nhất để đánh giá chất lượng nước và hiệu quả lọc."))

    b.append(h2("62.1 Nephelometer (tán xạ 90°)", "Nephelometer (90° Scattering)"))
    b.append(p(
        "Chiếu chùm sáng chuẩn (LED 860 nm hoặc đèn tungsten) qua mẫu, đo cường độ tán xạ tại góc 90° bằng "
        "photodiode. Vì tán xạ 90° nhạy nhất với hạt cỡ vi-lít và ít ảnh hưởng màu, đây là phương pháp chuẩn "
        "nephelometric. Đầu dò thường thêm một đầu đo truyền qua để bù nhiễu màu."))

    b.append(h2("62.2 Các phương pháp khác", "Other Methods"))
    b.append(p(
        "<b>Truyền qua</b> (transmissometry): đo I/I₀ qua chiều dài đường, nhạy với độ đục cao (nước thải, "
        "bùn). <b>Tán xạ quay</b> (multi-angle): đo tán xạ ở nhiều góc để phân bố kích thước hạt. <b>Cảm biến "
        "độ đục trực tuyến</b> gắn vào đường ống để điều khiển lọc/hoá chất liên tục."))

    b.append(h2("62.3 Thông số", "Specifications"))
    b.append(table(
        ["Loại", "Dải", "Độ chính xác", "Ứng dụng"],
        [["Cầm tay NTU", "0–1000 NTU", "±2%–5%", "Nước uống, trường"],
         ["Trực tuyến (line)", "0,001–4000 NTU", "±1%–3%", "Điều khiển lọc"],
         ["Truyền qua", "40–4000 NTU", "±5%", "Nước thải, bùn"],
         ["Multi-angle", "0,01–1000 NTU", "±2%", "Nghiên cứu hạt"]],
        "Bảng 62.1 · Thiết bị đo độ đục."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Độ đục đo tán xạ ánh sáng của hạt lơ lửng, đơn vị NTU (formazin). Nephelometer đo tán xạ 90° — chuẩn; "
        "truyền qua cho độ đục cao; multi-angle phân bố hạt. Nước uống phải < 1 NTU. Cảm biến trực tuyến điều "
        "khiển lọc/hoá chất."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 62. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Turbidity is the loss of water clarity from suspended particles (silt, algae, bacteria, colloids) that "
        "scatter and absorb light; the standard unit is NTU against formazin standards. Drinking water must be "
        "< 1 NTU (WHO/EPA). The nephelometer measures 90° scattering (LED 860 nm or tungsten source, photodiode "
        "detector) — the standard method, least affected by color; a transmission channel often compensates. "
        "Transmissometry (I/I₀ over path length) suits high turbidity (wastewater, sludge); multi-angle scattering "
        "gives particle-size information; inline sensors control filtration/chemical dosing continuously."))
    b.append(table(
        ["Type", "Range", "Accuracy", "Use"],
        [["Handheld NTU", "0–1000 NTU", "±2%–5%", "Drinking water"],
         ["Inline", "0.001–4000 NTU", "±1%–3%", "Filtration control"],
         ["Transmissometry", "40–4000 NTU", "±5%", "Wastewater, sludge"],
         ["Multi-angle", "0.01–1000 NTU", "±2%", "Particle research"]],
        "Table 62.1 · Turbidity instruments."))
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
