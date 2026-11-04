# -*- coding: utf-8 -*-
"""Handbook Chapter 78 — Blood Chemistry Measurement (Đo hoá học máu).
Run:  python build/reader_hb_ch78.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch78-blood-chemistry-measurement'
CH_NO = 78
TITLE_EN = 'Blood Chemistry Measurement'
TITLE_VI = 'Đo hoá học máu'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Đo hoá học máu định lượng chất điện giải, khí máu, glucose, enzym, protein và thuốc trong máu toàn phần, huyết tương hoặc huyết thanh. Đây là nền tảng của chẩn đoán cấp cứu, hồi sức và theo dõi chuyển hoá, đòi hỏi thời gian trả kết quả ngắn và độ đặc hiệu cao.'))
    b.append(p('Ba họ công nghệ chiếm ưu thế: điện cực chọn lọc ion (ISE), cảm biến điện hoá enzyme và phương pháp quang phổ / sắc ký / miễn dịch.'))
    b.append(h2('78.1 Điện cực chọn lọc ion và phương trình Nernst', 'Ion-Selective Electrodes and the Nernst Equation'))
    b.append(p('ISE dùng màng chọn lọc (thuỷ tinh cho Na⁺ và pH, valinomycin cho K⁺, màng polymer trao đổi ion cho Cl⁻ và Ca²⁺) tạo hiệu điện thế màng tỉ lệ log hoạt độ ion. Phép đo là so sánh với điện cực tham chiếu Ag/AgCl ổn định. Cần phân biệt ISE pha loãng (diluted, cho nồng độ tổng) và ISE trực tiếp (undiluted, cho hoạt độ trong nước huyết tương) — hai kết quả lệch nhau khi protein hoặc lipid cao.'))
    b.append(eq('E = E₀ + (2,303·RT/(zF))·log a_i  ≈  E₀ + (59,16/z) mV·log a_i  (37 °C)', '78.1'))
    b.append(h2('78.2 Khí máu: pH, pCO₂, pO₂', 'Blood Gas: pH, pCO₂, pO₂'))
    b.append(p('pH đo bằng điện cực thuỷ tinh; pCO₂ bằng điện cực Severinghaus (điện cực pH đặt sau màng thấm CO₂, CO₂ khuếch tán làm thay đổi pH dung dịch bicarbonate); pO₂ bằng điện cực Clark (cathode platinum khử O₂, dòng khuếch tán tỉ lệ pO₂). Từ ba giá trị đo, máy tính suy HCO₃⁻, BE và bão hoà oxy theo Henderson–Hasselbalch.'))
    b.append(eq('pH = 6,1 + log( [HCO₃⁻]/(α·pCO₂) ) ,   α = 0,0307 mmol·L⁻¹·mmHg⁻¹', '78.2'))
    b.append(h2('78.3 Cảm biến enzyme và phương pháp quang phổ', 'Enzymatic and Optical Methods'))
    b.append(p('Glucose oxidase / glucose dehydrogenase tạo H₂O₂ hoặc NADH đo bằng dòng ampe hoặc hấp thụ 340 nm. Định luật Beer–Lambert A = ε·c·l là nền tảng của mọi máy đo quang hoá sinh; sắc ký lỏng hiệu năng cao (HPLC) và khối phổ cho thuốc và hormone; miễn dịch (ELISA, chemiluminescence) cho dấu ấn sinh học. Co-oximetry đo đồng thời HbO₂, HbCO, MetHb bằng nhiều bước sóng.'))
    b.append(eq('A = −log(I/I₀) = ε·c·l ,   I = I₀·e^(−ε·c·l)', '78.3'))
    b.append(table(['Chất', 'Phương pháp', 'Khoảng tham chiếu', 'Ghi chú'], [['Na⁺', 'ISE thuỷ tinh', '135–145 mmol·L⁻¹', 'Ảnh hưởng protein'], ['K⁺', 'ISE valinomycin', '3,5–5,0 mmol·L⁻¹', 'Tan máu làm tăng giả'], ['pH', 'Điện cực thuỷ tinh', '7,35–7,45', '37 °C, kỵ khí'], ['pCO₂', 'Severinghaus', '35–45 mmHg', 'Màng thấm khí'], ['pO₂', 'Clark', '80–100 mmHg', 'Cathode Pt, −0,6 V'], ['Glucose', 'GOD / GDH ampe', '3,9–5,5 mmol·L⁻¹', 'Chống nhiễu acid ascorbic']], 'Bảng 78.1 · Các phép đo hoá học máu thường quy.'))
    b.append(h2('78.4 Tiền phân tích và kiểm soát chất lượng', 'Pre-analytical Phase and QC'))
    b.append(p('Phần lớn sai số xảy ra trước khi đo: loại ống (heparin cân bằng vs EDTA), thời gian và nhiệt độ bảo quản, tan máu, tiếp xúc không khí làm pH tăng và pCO₂ giảm. Kiểm soát chất lượng dùng 3 mức huyết thanh điều khiển hàng ngày, hiệu chuẩn 2 điểm và theo dõi biểu đồ Levey–Jennings theo Westgard.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('ISE cho điện giải theo Nernst (≈ 59,16/z mV mỗi thập phân ở 37 °C); Clark, Severinghaus và điện cực thuỷ tinh cho khí máu; enzyme + Beer–Lambert cho glucose và chất chuyển hoá. Hiệu chuẩn 2 điểm, QC nội bộ và xử lý mẫu kỵ khí đúng cách quyết định độ tin cậy.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 78. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Blood chemistry relies on ion-selective electrodes (Nernst: E = E0 + 59.16/z mV per decade at 37 °C), the Severinghaus pCO₂ and Clark pO₂ electrodes with the Henderson–Hasselbalch relation, and enzymatic/photometric assays obeying Beer–Lambert A = epsilon*c*l. Glass ISE for Na⁺/pH, valinomycin for K⁺; co-oximetry resolves Hb species at multiple wavelengths. Distinguish direct (undiluted) from diluted ISE. Pre-analytical handling (heparin balance, anaerobiosis, haemolysis, storage) dominates the error budget; two-point calibration plus Levey–Jennings/Westgard QC is standard.'))
    b.append(eq('E = E₀ + (2,303·RT/(zF))·log a_i  ≈  E₀ + (59,16/z) mV·log a_i  (37 °C)', '78.1'))
    b.append(eq('pH = 6,1 + log( [HCO₃⁻]/(α·pCO₂) ) ,   α = 0,0307 mmol·L⁻¹·mmHg⁻¹', '78.2'))
    b.append(eq('A = −log(I/I₀) = ε·c·l ,   I = I₀·e^(−ε·c·l)', '78.3'))
    b.append(table(['Analyte', 'Method', 'Reference range', 'Note'], [['Na⁺', 'Glass ISE', '135–145 mmol·L⁻¹', 'Protein dependent'], ['K⁺', 'Valinomycin ISE', '3.5–5.0 mmol·L⁻¹', 'Haemolysis biases high'], ['pH', 'Glass electrode', '7.35–7.45', '37 °C, anaerobic'], ['pCO₂', 'Severinghaus', '35–45 mmHg', 'Gas-permeable membrane'], ['pO₂', 'Clark', '80–100 mmHg', 'Pt cathode, −0.6 V'], ['Glucose', 'GOD / GDH amperometric', '3.9–5.5 mmol·L⁻¹', 'Ascorbate interference']], 'Table 78.1 · Routine blood-chemistry measurements.'))
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
