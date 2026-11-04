# -*- coding: utf-8 -*-
"""Handbook Chapter 79 — Medical Imaging (Chẩn đoán hình ảnh).
Run:  python build/reader_hb_ch79.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch79-medical-imaging'
CH_NO = 79
TITLE_EN = 'Medical Imaging'
TITLE_VI = 'Chẩn đoán hình ảnh'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chẩn đoán hình ảnh tạo bản đồ không xâm lấn của cấu trúc và chức năng cơ thể bằng tia X, từ trường, siêu âm hoặc chất phóng xạ đánh dấu. Các hệ chính: X-quang/CT, MRI, siêu âm, PET/SPECT và nội soi quang học.'))
    b.append(p('Mọi hệ thống đều là bài toán đo lường: tín hiệu thu được là một phép chiếu hoặc một đáp ứng vật lý, cần tái dựng ảnh, hiệu chuẩn thang xám và kiểm soát đồng thời độ phân giải, độ nhiễu và liều bức xạ.'))
    b.append(h2('79.1 X-quang và CT', 'X-ray and Computed Tomography'))
    b.append(p('Tia X suy giảm theo Beer–Lambert với hệ số suy giảm µ phụ thuộc năng lượng và số nguyên tử. CT thu hàng nghìn phép chiếu quay quanh bệnh nhân rồi tái dựng bằng lọc chiếu ngược (FBP) hoặc tái dựng lặp. Thang Hounsfield chuẩn hoá µ về nước = 0 HU và không khí = −1000 HU.'))
    b.append(eq('I = I₀·e^(−∫µ(x)dx) ,   HU = 1000·(µ − µ_water)/µ_water', '79.1'))
    b.append(h2('79.2 Cộng hưởng từ', 'Magnetic Resonance Imaging'))
    b.append(p('Proton trong từ trường B₀ cộng hưởng ở tần số Larmor ω₀ = γB₀; gradient tuyến tính mã hoá vị trí vào tần số/pha, tín hiệu thu là biến đổi Fourier của không gian k. Trọng T₁, T₂ hay proton density điều chỉnh bằng TR/TE. Không dùng bức xạ ion hoá nhưng chống chỉ định với cấy ghép sắt từ và cần kiểm soát SAR.'))
    b.append(eq('ω₀ = γ·B₀  (γ/2π = 42,58 MHz·T⁻¹) ,   S(k) = ∫ρ(r)·e^(−i2πk·r) dr', '79.2'))
    b.append(h2('79.3 Siêu âm và y học hạt nhân', 'Ultrasound and Nuclear Medicine'))
    b.append(p('Siêu âm (2–15 MHz) dùng echo thời gian bay z = c·t/2 với c ≈ 1540 m·s⁻¹; độ phân giải dọc tỉ lệ nghịch độ dài xung, độ phân giải ngang quyết định bởi độ rộng chùm. SPECT quay gamma camera quanh bệnh nhân; PET ghi cặp photon 511 keV trùng hợp từ positron annihilation, cho hình ảnh chuyển hoá (FDG) định lượng SUV.'))
    b.append(eq('z = c·t/2 ,   Δz ≈ n·λ/2 ,   SUV = (C_tissue·m_body)/A_inj', '79.3'))
    b.append(h2('79.4 Chất lượng ảnh và liều', 'Image Quality and Dose'))
    b.append(p('Đánh giá bằng SNR, CNR, MTF (độ phân giải tương phản theo tần số không gian), NPS (phổ nhiễu) và DQE của đầu dò. Với CT có sự đánh đổi căn bản: nhiễu ∝ 1/√liều nên giảm một nửa nhiễu cần tăng liều gấp bốn. Hiệu chuẩn định kỳ bằng phantom (Catphan, ACR) và tuân thủ nguyên tắc ALARA.'))
    b.append(table(['Phương thức', 'Độ phân giải', 'Tương phản', 'Liều ion hoá'], [['X-quang', '≈ 0,1 mm', 'Mật độ / Z', 'Thấp (~0,1 mSv)'], ['CT', '≈ 0,5 mm', 'HU, 0,1 %', 'Trung bình (1–10 mSv)'], ['MRI', '≈ 1 mm', 'T₁/T₂ rất cao', 'Không'], ['Siêu âm', '0,2–1 mm', 'Trở kháng âm', 'Không'], ['PET / SPECT', '4–8 mm', 'Chuyển hoá rất cao', 'Có (5–25 mSv)']], 'Bảng 79.1 · So sánh các phương thức chẩn đoán hình ảnh.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('CT: I = I₀e^(−∫µdx) và thang HU; MRI: cộng hưởng Larmor ω₀ = γB₀ và tái dựng  Fourier từ không gian k; siêu âm: z = ct/2; PET: trùng hợp 511 keV. Chất lượng ảnh đặc trưng bởi SNR/CNR/MTF/DQE, và với CT nhiễu ∝ 1/√liều nên phải tối ưu theo ALARA.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 79. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Medical imaging is quantitative measurement: radiography/CT follow exponential attenuation and the Hounsfield scale HU = 1000(µ − µ_water)/µ_water; MRI encodes position via gradients at the Larmor frequency (42.58 MHz/T) and reconstructs by Fourier inversion of k-space; ultrasound ranges echoes with z = c*t/2, c ≈ 1540 m/s; PET detects coincident 511 keV annihilation photons. Image quality is specified by SNR, CNR, MTF, NPS and DQE, with the CT noise ∝ 1/sqrt(dose) trade-off and ALARA dose optimisation, verified by Catphan/ACR phantoms.'))
    b.append(eq('I = I₀·e^(−∫µ(x)dx) ,   HU = 1000·(µ − µ_water)/µ_water', '79.1'))
    b.append(eq('ω₀ = γ·B₀  (γ/2π = 42,58 MHz·T⁻¹) ,   S(k) = ∫ρ(r)·e^(−i2πk·r) dr', '79.2'))
    b.append(eq('z = c·t/2 ,   Δz ≈ n·λ/2 ,   SUV = (C_tissue·m_body)/A_inj', '79.3'))
    b.append(table(['Modality', 'Resolution', 'Contrast', 'Ionising dose'], [['Radiography', '≈ 0.1 mm', 'Density / Z', 'Low (~0.1 mSv)'], ['CT', '≈ 0.5 mm', 'HU, 0.1 %', 'Moderate (1–10 mSv)'], ['MRI', '≈ 1 mm', 'Very high T₁/T₂', 'None'], ['Ultrasound', '0.2–1 mm', 'Acoustic impedance', 'None'], ['PET / SPECT', '4–8 mm', 'Very high metabolic', 'Yes (5–25 mSv)']], 'Table 79.1 · Imaging modality comparison.'))
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
