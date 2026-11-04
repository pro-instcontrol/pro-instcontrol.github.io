# -*- coding: utf-8 -*-
"""Handbook Chapter 36 — Calorimetry Measurement (Đo nhiệt lượng).
Run:  python build/reader_hb_ch36.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch36-calorimetry-measurement'
CH_NO = 36
TITLE_EN = 'Calorimetry Measurement'
TITLE_VI = 'Đo nhiệt lượng'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Nhiệt lượng kế đo năng lượng trao đổi dưới dạng nhiệt, từ đó suy nhiệt đốt cháy, nhiệt dung, enthalpy phản ứng và enthalpy chuyển pha. Nguyên lý chung là cân bằng năng lượng: Q = C_eff·ΔT, trong đó C_eff (J·K⁻¹) là dung lượng nhiệt của toàn hệ kể cả bình chứa, xác định bằng hiệu chuẩn.'))
    b.append(p('Hai họ thiết bị chính: nhiệt lượng kế đốt (bom, xác định giá trị năng lượng nhiên liệu và thực phẩm) và nhiệt lượng kế quét vi sai (DSC/DTA/ITC, phân tích tính chất nhiệt của vật liệu và tương tác phân tử).'))
    b.append(h2('36.1 Phân loại theo chế độ nhiệt', 'Classification by Thermal Regime'))
    b.append(p('Đoạn nhiệt (adiabatic): vỏ áo bám theo nhiệt độ cell để triệt trao đổi nhiệt. Đẳng nhiệt môi (isoperibol): vỏ giữ nhiệt độ không đổi và hiệu chỉnh trao đổi nhiệt theo định luật làm nguội Newton. Đẳng nhiệt (isothermal): giữ T không đổi, đo công suất bù. Dòng nhiệt (heat-flow): đo chênh qua cảm biến thông lượng. Mỗi chế độ đổi độ phức tạp cơ khí lấy độ phức tạp của phép hiệu chỉnh.'))
    b.append(eq('Q = C_eff·ΔT ,   dQ/dt = K·(T_cell − T_jacket) ,   C_eff = (V·I·t)/ΔT', '36.1'))
    b.append(h2('36.2 Bom nhiệt lượng', 'Bomb Calorimeter'))
    b.append(p('Mẫu được đốt trong bom thép chứa O₂ ở 25–30 atm, nhúng trong lượng nước cân chính xác có khuấy. Nhiệt đốt cháy thô (gross) suy từ ΔT đã hiệu chỉnh, trừ nhiệt dây đốt và nhiệt tạo acid nitric/sulfuric. Hiệu chuẩn bằng acid benzoic chuẩn (≈ 26,43 MJ·kg⁻¹) theo ASTM D240/D5865. Giá trị ròng (net) trừ thêm nhiệt ẩn hoá hơi nước sinh ra.'))
    b.append(h2('36.3 DSC, DTA và ITC', 'DSC, DTA and ITC'))
    b.append(p('DSC so sánh công suất cần thiết để giữ mẫu và chuẩn đi cùng chương trình nhiệt độ; diện tích peak cho ΔH (nóng chảy, kết tinh, đóng rắn), vị trí peak cho nhiệt độ đặc trưng và bước dịch đường nền cho T_g. DTA ghi ΔT thay vì công suất. ITC tiêm từng liều vào cell đẳng nhiệt và đo công suất bù, cho đồng thời ΔH, hằng số liên kết K_a và tỉ lệ n trong một thí nghiệm.'))
    b.append(table(['Kỹ thuật', 'Đại lượng đo', 'Kết quả', 'Độ nhạy điển hình'], [['Bom đốt', 'ΔT nước', 'Nhiệt đốt cháy (MJ·kg⁻¹)', '≈ 0,1 %'], ['DSC', 'Chênh công suất', 'T_m, T_g, ΔH (J·g⁻¹)', '≈ 1 µW'], ['DTA', 'ΔT mẫu – chuẩn', 'Nhiệt độ chuyển pha', '≈ 0,1 K'], ['ITC', 'Công suất bù', 'ΔH, K_a, n', '≈ 0,1 µW']], 'Bảng 36.1 · Các kỹ thuật nhiệt lượng kế.'))
    b.append(h2('36.4 Hiệu chuẩn và độ không đảm bảo', 'Calibration and Uncertainty'))
    b.append(p('Hiệu chuẩn nhiệt độ bằng điểm nóng chảy chuẩn (indium 156,6 °C, thiếc 231,9 °C) và enthalpy bằng nhiệt nóng chảy indium 28,71 J·g⁻¹. Nguồn sai số gồm tốc độ quét, khối lượng và hình dạng mẫu, tiếp xúc nhiệt với đĩa, bay hơi mẫu và trôi đường nền; độ lặp lại thường 1–3 %.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Mọi nhiệt lượng kế đều giải Q = C_eff·ΔT với C_eff xác định bằng hiệu chuẩn điện hoặc chất chuẩn. Bom đốt cho nhiệt đốt cháy (acid benzoic), DSC/DTA cho chuyển pha và T_g, ITC cho tham số liên kết. Tốc độ quét và tiếp xúc nhiệt là nguồn sai số cần kiểm soát chặt.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 36. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Calorimetry reduces to an energy balance Q = C_eff*DeltaT, with the effective heat capacity of vessel plus contents established by electrical or chemical calibration (benzoic acid, ≈ 26.43 MJ·kg⁻¹). Adiabatic, isoperibol, isothermal and heat-flow designs trade mechanical complexity against correction complexity. Combustion bombs give gross/net heat of combustion (ASTM D240/D5865); DSC gives T_m, T_g and transition enthalpy; ITC yields DeltaH, binding constant K_a and stoichiometry. Indium (156.6 °C, 28.71 J·g⁻¹) is the standard temperature/enthalpy reference.'))
    b.append(eq('Q = C_eff·ΔT ,   dQ/dt = K·(T_cell − T_jacket) ,   C_eff = (V·I·t)/ΔT', '36.1'))
    b.append(table(['Technique', 'Measured', 'Output', 'Typical sensitivity'], [['Combustion bomb', 'Water ΔT', 'Heat of combustion (MJ·kg⁻¹)', '≈ 0.1 %'], ['DSC', 'Power difference', 'T_m, T_g, ΔH (J·g⁻¹)', '≈ 1 µW'], ['DTA', 'Sample–reference ΔT', 'Transition temperature', '≈ 0.1 K'], ['ITC', 'Compensation power', 'ΔH, K_a, n', '≈ 0.1 µW']], 'Table 36.1 · Calorimetric techniques.'))
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
