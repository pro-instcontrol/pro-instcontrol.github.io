# -*- coding: utf-8 -*-
"""Handbook Chapter 56 — Photometry and Radiometry (Trắc quang và đo bức xạ).
Run:  python build/reader_hb_ch56.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch56-photometry-and-radiometry"
CH_NO = 56
TITLE_EN = "Photometry and Radiometry"
TITLE_VI = "Trắc quang và đo bức xạ"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Quang trắc</b> (radiometry) đo năng lượng điện từ theo công suất vật lý tuyệt đối, không phụ thuộc "
        "cảm nhận của mắt. <b>Trắc quang</b> (photometry) đo cùng những đại lượng nhưng quy về đáp ứng phổ của "
        "mắt người V(λ), với trọng số lumens/W = 683·V(λ). Cặp đại lượng tương ứng:"))
    b.append(table(
        ["Quang trắc (radiometric)", "Trắc quang (photometric)", "Đơn vị"],
        [["Thông lượng bức xạ Φ", "Thông lượng sáng Φ_v", "W / lm"],
         ["Cường độ bức xạ I", "Cường độ sáng I_v", "W/sr / cd"],
         ["Độ rọi bức xạ E", "Độ rọi sáng E_v", "W/m² / lux"],
         ["Độ sáng bức xạ L", "Độ chói L_v", "W/sr·m² / cd/m²"]],
        "Bảng 56.1 · Tương ứng đại lượng radiometric / photometric."))
    b.append(p(
        "Trắc quang quan trọng trong chiếu sáng, màn hình, máy ảnh; quang trắc trong viễn thám, laser, nhiệt "
        "và khoa học vật liệu."))

    b.append(h2("56.1 Đầu dò và máy đo", "Detectors and Meters"))
    b.append(p(
        "Đầu dò chính: <b>photodiode silicon</b> (200–1100 nm, tuyến tính tốt, dùng làm chuẩn), photodiode "
        "germani/InGaAs (900–1700 nm), <b>thermopile</b> (rộng dải, tuyến tính theo nhiệt), <b>bolometer</b>. "
        "Trắc quang gắn <b>bộ lọc V(λ)</b> hoặc đầu dò silicon hiệu chỉnh đáp ứng để khớp đường cong mắt."))
    b.append(p(
        "<b>Photometer/radiometer</b> cầm tay đọc lux, cd/m² hoặc W/m²; <b>goniophotometer</b> quay đầu dò quanh "
        "nguồn để lấy phân bố không gian (phù hợp IES/LDT); <b>hình cầu hội tụ</b> (integrating sphere) hội tụ "
        "toàn bộ thông lượng của nguồn vào đầu dò để đo tổng lm."))

    b.append(h2("56.2 Hiệu chuẩn và chuẩn", "Calibration"))
    b.append(p(
        "Đầu dò hiệu chuẩn so với chuẩn thế giới (đèn halogen chuẩn, blackbody hoặc detector chuẩn kết nối "
        "NIST/NMI). Photometric chuẩn: <b>là nguồn sáng chuẩn</b> có cường độ sáng đã biết (cd). Sai số chuẩn "
        "điển hình 1%–5% tùy dải phổ và thiết bị."))

    b.append(h2("56.3 Thông số", "Specifications"))
    b.append(table(
        ["Thiết bị", "Dải", "Độ chính xác", "Ứng dụng"],
        [["Photometer (lux)", "0,01–200 000 lx", "2%–5%", "Chiếu sáng, văn phòng"],
         ["Luminance meter", "0,01–200 000 cd/m²", "3%–5%", "Màn hình, đường"],
         ["Radiometer", "200–1700 nm", "1%–3%", "Laser, viễn thám"],
         ["Integrating sphere", "0,1–200 000 lm", "1%–3%", "Tổng thông lượng"],
         ["Goniophotometer", "Phân bố không gian", "2%–5%", "Đèn chuyên dụng"]],
        "Bảng 56.2 · Thiết bị trắc quang/quang trắc."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Quang trắc đo công suất tuyệt đối (W); trắc quang quy về mắt V(λ), lm = 683·V(λ)·W. Cặp đại lượng: "
        "Φ (lm), I (cd), E (lux), L (cd/m²). Đầu dò: photodiode Si/InGaAs, thermopile; gắn bộ lọc V(λ) cho "
        "photometry. Đo tổng thông lượng bằng integrating sphere; phân bố không gian bằng goniophotometer. "
        "Hiệu chuẩn so với đèn/detector chuẩn NMI, sai số 1%–5%."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 56. The tables of the source are reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Radiometry measures optical power absolutely (W); photometry weights by the eye response V(λ) "
        "(lm = 683·V(λ)·W). Corresponding quantities: radiant flux Φ ↔ luminous flux Φ_v (lm), radiant intensity "
        "I ↔ luminous intensity I_v (cd), irradiance E ↔ illuminance E_v (lux), radiance L ↔ luminance L_v "
        "(cd/m²). Detectors: Si photodiodes (200–1100 nm, linear standards), Ge/InGaAs (900–1700 nm), thermopiles "
        "(broadband); photometric units add a V(λ) filter or corrected Si response. Handheld meters read lux, "
        "cd/m² or W/m²; goniophotometers sweep the angular distribution (IES/LDT); integrating spheres collect the "
        "total flux of a source. Calibration against NMI-traceable lamps or detectors, 1%–5% typical uncertainty."))
    b.append(table(
        ["Instrument", "Range", "Accuracy", "Use"],
        [["Photometer (lux)", "0.01–200 000 lx", "2%–5%", "Lighting"],
         ["Luminance meter", "0.01–200 000 cd/m²", "3%–5%", "Displays, roads"],
         ["Radiometer", "200–1700 nm", "1%–3%", "Laser, remote"],
         ["Integrating sphere", "0.1–200 000 lm", "1%–3%", "Total flux"],
         ["Goniophotometer", "Spatial distribution", "2%–5%", "Luminaires"]],
        "Table 56.2 · Photometric/radiometric instruments."))
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
