# -*- coding: utf-8 -*-
"""Handbook Chapter 77 — Ventilation Measurement (Đo thông khí).
Run:  python build/reader_hb_ch77.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch77-ventilation-measurement'
CH_NO = 77
TITLE_EN = 'Ventilation Measurement'
TITLE_VI = 'Đo thông khí'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Đo thông khí định lượng thể tích và lưu lượng khí hô hấp, trao đổi khí và cơ học phổi. Các chỉ số lâm sàng chính: tần số thở f, thể tích khí lưu thông V_T, thông khí phút V̇_E = f·V_T, dung tích sống FVC, thể tích thở ra gắng sức trong 1 giây FEV₁ và tỉ lệ FEV₁/FVC.'))
    b.append(p('Hai nhóm thiết bị bổ trợ nhau: đo lưu lượng/ thể tích (spirometer, pneumotachograph, body plethysmograph) và đo thành phần khí (capnograph, máy phân tích O₂/CO₂, oxymeter).'))
    b.append(h2('77.1 Phế dung kế và lưu lượng kế khí', 'Spirometers and Pneumotachographs'))
    b.append(p('Spirometer thể tích dịch chuyển (chuông nước, bellows) tích phân trực tiếp thể tích; pneumotachograph đo chênh áp Δp qua một điện trở khí (lưới hoặc ống mao dẫn) rồi lấy tích phân Q̇ theo thời gian. Với lưới laminar Δp ∝ Q̇, với ống Fleisch hoặc lưới Lilly cần tuyến tính hoá. Điều kiện BTPS (37 °C, áp suất môi trường, bão hoà hơi nước) bắt buộc để so sánh kết quả.'))
    b.append(eq('Q̇ = Δp/R_flow ,   V = ∫ Q̇ dt ,   V̇_E = f·V_T', '77.1'))
    b.append(h2('77.2 Thể tích phổi tĩnh và buồng thể tích kí cơ thể', 'Static Lung Volumes and Body Plethysmography'))
    b.append(p('Spirometry không đo được thể tích khí cặn (RV), dung tích cặn chức năng (FRC) và tổng dung tích phổi (TLC). Các thể tích này đo bằng pha loãng khí trơ (helum), rửa trôi nitơ hoặc body plethysmography dựa trên định luật Boyle: ngồi trong buồng kín, bệnh nhân thở gắng sức ngăn miệng thở, biến thiên áp suất miệng và buồng cho phép tính thể tích khí trong ngực.'))
    b.append(eq('P₁V₁ = P₂V₂   ⇒   FRC = (ΔV/ΔP_mouth)·(P_bar − P_H₂O)', '77.2'))
    b.append(h2('77.3 Capnography và trao đổi khí', 'Capnography and Gas Exchange'))
    b.append(p('Capnograph hồng ngoại (hấp thụ CO₂ tại 4,26 µm) cho đường cong CO₂ theo thì thở: pha I khí chết, pha II trộn, pha III cao nguyên phế nang, giá trị cuối thì thở EtCO₂ ≈ 35–45 mmHg. Kết hợp phân tích O₂ (paramagnetic, zirconia hoặc điện hoá) và spirometry cho VO₂, VCO₂ và tỉ lệ trao đổi hô hấp RER = VCO₂/VO₂. Phương trình khí phế nang liên hệ PaCO₂ với thông khí phế nang.'))
    b.append(eq('PAO₂ = FiO₂·(P_atm − 47) − PaCO₂/R ,   SpO₂ = HbO₂/(HbO₂ + Hb)·100 %', '77.3'))
    b.append(table(['Chỉ số', 'Ký hiệu', 'Người lớn khoẻ mạnh', 'Ý nghĩa'], [['Thể tích khí lưu thông', 'V_T', '≈ 500 mL', 'Mỗi nhịp thở'], ['Thông khí phút', 'V̇_E', '≈ 6 L·min⁻¹', 'f·V_T'], ['Dung tích sống gắng sức', 'FVC', '4–5 L', 'Giới hạn tắc nghẽn'], ['FEV₁/FVC', '—', '> 0,70 (Tiffeneau)', 'Phân biệt tắc/hạn chế'], ['FRC', '—', '≈ 2,4 L', 'Thể tích cuối thì thở ra'], ['EtCO₂', '—', '35–45 mmHg', 'Thông khí phế nang']], 'Bảng 77.1 · Các thông số thông khí tham khảo.'))
    b.append(h2('77.4 Hiệu chuẩn', 'Calibration'))
    b.append(p('Hiệu chuẩn thể tích bằng bơm tiêm chuẩn 3 L (ATS/ERS cho phép ± 3 %), kiểm tra độ kín và tuyến tính ở ba mức lưu lượng, hiệu chuẩn khí bằng bình chuẩn CO₂/O₂ và khí zero. Sai lệch BTPS/ATPS là nguồn sai số hệ thống thường gặp nhất.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Spirometry cho V_T, FVC, FEV₁; pneumotachograph cho Q̇(t) và vòng lưu lượng–thể tích. FRC/RV/TLC cần pha loãng He, rửa N₂ hoặc buồng thể tích kí theo Boyle. Capnography (EtCO₂) và phân tích O₂ hoàn thiện đánh giá trao đổi khí. Hiệu chuẩn 3 L và quy về BTPS là bắt buộc.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 77. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("Ventilation measurement combines volume/flow (volume-displacement spirometers, Fleisch/Lilly pneumotachographs with Q = DeltaP/R and V = integral Q dt) with gas analysis (infrared capnography at 4.26 µm, paramagnetic/zirconia O₂). Minute ventilation is f*V_T ≈ 6 L/min; FEV₁/FVC > 0.70 distinguishes obstructive from restrictive disease. Residual volume and FRC cannot be measured by spirometry and require helium dilution, nitrogen washout or body plethysmography (Boyle's law). ATS/ERS requires 3 L syringe calibration within ± 3 % and BTPS correction."))
    b.append(eq('Q̇ = Δp/R_flow ,   V = ∫ Q̇ dt ,   V̇_E = f·V_T', '77.1'))
    b.append(eq('P₁V₁ = P₂V₂   ⇒   FRC = (ΔV/ΔP_mouth)·(P_bar − P_H₂O)', '77.2'))
    b.append(eq('PAO₂ = FiO₂·(P_atm − 47) − PaCO₂/R ,   SpO₂ = HbO₂/(HbO₂ + Hb)·100 %', '77.3'))
    b.append(table(['Index', 'Symbol', 'Healthy adult', 'Meaning'], [['Tidal volume', 'V_T', '≈ 500 mL', 'Per breath'], ['Minute ventilation', 'V̇_E', '≈ 6 L·min⁻¹', 'f·V_T'], ['Forced vital capacity', 'FVC', '4–5 L', 'Obstructive limit'], ['FEV₁/FVC', '—', '> 0.70 (Tiffeneau)', 'Obstructive vs restrictive'], ['FRC', '—', '≈ 2.4 L', 'End-expiratory volume'], ['EtCO₂', '—', '35–45 mmHg', 'Alveolar ventilation']], 'Table 77.1 · Reference ventilation parameters.'))
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
