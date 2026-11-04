# -*- coding: utf-8 -*-
"""Handbook Chapter 35 — Thermal Imaging (Ảnh nhiệt).
Run:  python build/reader_hb_ch35.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch35-thermal-imaging'
CH_NO = 35
TITLE_EN = 'Thermal Imaging'
TITLE_VI = 'Ảnh nhiệt'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Ảnh nhiệt (hồng ngoại nhiệt, thermography) tạo bản đồ nhiệt độ bề mặt không tiếp xúc bằng cách đo bức xạ hồng ngoại tự phát của vật. Camera hiện đại cho ảnh 2D theo thời gian thực, dùng trong bảo trì điện và cơ khí, kiểm tra cách nhiệt công trình, chẩn đoán y tế, giám sát lò công nghiệp và phát hiện rò rỉ khí.'))
    b.append(p('Điểm mấu chốt: camera đo bức xạ thu được, không đo nhiệt độ trực tiếp. Mọi chuyển đổi sang nhiệt độ đều cần mô hình hoá độ phát xạ, nhiệt độ phản xạ và suy giảm khí quyển.'))
    b.append(h2('35.1 Bức xạ nhiệt và cửa sổ khí quyển', 'Thermal Radiation and Atmospheric Windows'))
    b.append(p('Vật có nhiệt độ T > 0 K phát bức xạ theo định luật Planck; công suất toàn phần tỉ lệ T⁴ (Stefan–Boltzmann) và đỉnh phổ dịch theo định luật Wien. Ở 300 K đỉnh nằm gần 9,7 µm, vì vậy camera nhiệt dùng hai cửa sổ khí quyển 3–5 µm và 8–14 µm nơi hơi nước và CO₂ hấp thụ ít.'))
    b.append(eq('M = ε·σ·T⁴ ,   λ_max·T = 2898 µm·K ,   L_λ = (2hc²/λ⁵)·[exp(hc/(λk_BT)) − 1]⁻¹', '35.1'))
    b.append(h2('35.2 Độ phát xạ và nhiệt độ biểu kiến', 'Emissivity and Apparent Temperature'))
    b.append(p('Tín hiệu thu gồm phần tự phát ε·M(T), phần phản xạ (1−ε)·M(T_ref) và phát xạ của khí quyển. Nhập sai ε là nguồn sai số lớn nhất: kim loại đánh bóng ε ≈ 0,05 có thể gây sai hàng chục độ, trong khi da, sơn mờ hay băng keo đen ε ≈ 0,95–0,98 cho kết quả tin cậy. Cần đo nhiệt độ phản xạ biểu kiến (phương pháp gương/Reflectors) và nhập khoảng cách, nhiệt độ và độ ẩm không khí.'))
    b.append(eq('L_meas = τ·[ε·L(T_obj) + (1−ε)·L(T_ref)] + (1−τ)·L(T_atm)', '35.2'))
    b.append(h2('35.3 Đầu dò và thông số chất lượng', 'Detectors and Performance'))
    b.append(p('Đầu dò nhiệt (microbolometer VOx hoặc a-Si, không làm lạnh) chiếm ưu thế ở 8–14 µm; đầu dò photon (InSb 3–5 µm, HgCdTe) phải làm lạnh nhưng nhạy và nhanh hơn. Các thông số quyết định khả năng phát hiện: NETD, IFOV, MRTD, tần số khung hình và dải đo.'))
    b.append(table(['Thông số', 'Ý nghĩa', 'Giá trị điển hình'], [['NETD', 'Nhiễu tương đương nhiệt độ', '30–50 mK'], ['IFOV', 'Góc nhìn tức thời = pitch/f', '0,5–2 mrad'], ['Dải phổ', 'Cửa sổ khí quyển', '7,5–14 µm / 3–5 µm'], ['Độ phân giải', 'Số điểm ảnh', '160×120 … 1280×1024'], ['Khung hình', 'Tốc độ làm tươi', '9 / 30 / 60 Hz'], ['Dải nhiệt độ', 'Thang đo được hiệu chuẩn', '−20 … +1500 °C']], 'Bảng 35.1 · Thông số đặc trưng của camera nhiệt.'))
    b.append(h2('35.4 Hiệu chuẩn và ứng dụng', 'Calibration and Applications'))
    b.append(p('Hiệu chuẩn bức xạ bằng nguồn đen có nhiệt độ chuẩn tại ít nhất hai điểm, kèm hiệu chỉnh tính không đồng nhất (NUC/flat-field) và bù trôi theo nhiệt độ thân máy. Ứng dụng điển hình: phát hiện điểm nóng tiếp xúc điện, cầu nhiệt và rò rỉ khí trong công trình, theo dõi nhiệt độ lò, sàng lọc sốt và chẩn đoán viêm trong y tế.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Camera nhiệt suy nhiệt độ từ bức xạ Planck trong cửa sổ 3–5 µm hoặc 8–14 µm. Độ chính xác phụ thuộc chủ yếu vào ε, T_ref và hiệu chuẩn nguồn đen; chất lượng ảnh đặc trưng bởi NETD, IFOV và MRTD. Luôn xử lý bề mặt (sơn mờ/băng keo) trước khi đo kim loại sáng.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 35. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("Thermal cameras convert band-limited infrared radiance into an apparent temperature. Planck's law, Stefan–Boltzmann T^4 and Wien's displacement law set the physics; the 3–5 µm and 8–14 µm atmospheric windows set the optics. The measured radiance mixes emitted, reflected and atmospheric terms, so emissivity and reflected apparent temperature dominate accuracy. Uncooled VOx/a-Si microbolometers dominate 8–14 µm systems; photon detectors (InSb, MCT) are faster but cryogenic. NETD, IFOV, MRTD and two-point blackbody calibration with NUC define performance."))
    b.append(eq('M = ε·σ·T⁴ ,   λ_max·T = 2898 µm·K ,   L_λ = (2hc²/λ⁵)·[exp(hc/(λk_BT)) − 1]⁻¹', '35.1'))
    b.append(eq('L_meas = τ·[ε·L(T_obj) + (1−ε)·L(T_ref)] + (1−τ)·L(T_atm)', '35.2'))
    b.append(table(['Parameter', 'Meaning', 'Typical value'], [['NETD', 'Noise-equivalent temperature', '30–50 mK'], ['IFOV', 'Instantaneous field of view = pitch/f', '0.5–2 mrad'], ['Spectral band', 'Atmospheric window', '7.5–14 µm / 3–5 µm'], ['Resolution', 'Pixel count', '160×120 … 1280×1024'], ['Frame rate', 'Refresh', '9 / 30 / 60 Hz'], ['Temperature range', 'Calibrated span', '−20 … +1500 °C']], 'Table 35.1 · Thermal-camera specifications.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE,
                                body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
