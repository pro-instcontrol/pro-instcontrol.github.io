# -*- coding: utf-8 -*-
"""Handbook Chapter 34 — Heat Flux (Thông lượng nhiệt).
Run:  python build/reader_hb_ch34.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch34-heat-flux'
CH_NO = 34
TITLE_EN = 'Heat Flux'
TITLE_VI = 'Thông lượng nhiệt'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Thông lượng nhiệt q″ (W·m⁻²) là mật độ dòng năng lượng nhiệt đi qua một đơn vị diện tích. Cảm biến thông lượng nhiệt biến gradient nhiệt độ qua một lớp cản nhiệt mỏng thành tín hiệu điện, được dùng trong thử nghiệm chống cháy, lò đốt, đo tổn thất nhiệt công trình, khí động học nhiệt độ cao và điều khiển quá trình.'))
    b.append(p('Khác với nhiệt kế chỉ cho nhiệt độ tại một điểm, cảm biến q″ cho trực tiếp dòng năng lượng, nhờ đó suy ra hệ số truyền nhiệt, công suất bức xạ tới hoặc tải nhiệt lên bề mặt.'))
    b.append(h2('34.1 Nguyên lý lớp gradient', 'Gradient-Layer Principle'))
    b.append(p('Cảm biến gồm lớp cản nhiệt có k và chiều dày δ xác định; một thermopile gồm N mối nối mắc nối tiếp đo ΔT giữa hai mặt. Theo Fourier một chiều, q″ tỉ lệ với ΔT, còn điện áp ra U = N·S·ΔT với S là hệ số Seebeck. Hằng số hiệu chuẩn (W·m⁻²·mV⁻¹) được xác định bằng nguồn chuẩn và phụ thuộc nhiệt độ.'))
    b.append(eq('q″ = k·ΔT/δ ,   U = N·S·ΔT   ⇒   q″ = (k/(δ·N·S))·U', '34.1'))
    b.append(h2('34.2 Các kiểu cảm biến', 'Sensor Types'))
    b.append(p('Schmidt–Boelter: thermopile quấn quanh lớp cản nhiệt, tuyến tính, dải tới ~100 kW·m⁻², dùng làm chuẩn trong thử lửa. Gardon (đĩa màng): đĩa constantan mỏng hấp thụ bức xạ, cặp nhiệt điện giữa tâm và vành đồng tản nhiệt, đáp ứng ~0,1 s nhưng phụ thuộc độ hấp thụ bề mặt. Cảm biến màng mỏng (thin-film) dùng nhiệt trở platinum, chịu nhiệt cao và lắp được trên bề mặt cong. Tấm HFS dải thấp 0–2 kW·m⁻² dùng cho bao che công trình.'))
    b.append(table(['Kiểu', 'Dải điển hình', 'Thời gian đáp ứng', 'Ứng dụng'], [['Schmidt–Boelter', '0–100 kW·m⁻²', '≈ 0,3 s', 'Chuẩn thử lửa'], ['Gardon', '0–300 kW·m⁻²', '≈ 0,1 s', 'Bức xạ lò, hồ quang'], ['Màng mỏng', '0–500 kW·m⁻²', '< 0,01 s', 'Cánh tuabin, bề mặt cong'], ['Tấm HFS', '0–2 kW·m⁻²', '≈ 1 s', 'Tường, cách nhiệt']], 'Bảng 34.1 · So sánh cảm biến thông lượng nhiệt.'))
    b.append(h2('34.3 Hiệu chuẩn và lắp đặt', 'Calibration and Mounting'))
    b.append(p('Hiệu chuẩn theo ISO 14934 / ASTM C1130 bằng nguồn đen hoặc tấm nóng có bảo vệ, ở vài mức công suất và nhiệt độ. Sai số lớn nhất thường do chính cảm biến làm thay đổi trường nhiệt: cần phủ bề mặt có độ phát xạ như vật nền, lắp phẳng bằng keo dẫn nhiệt mỏng, che chắn dây dẫn và bù theo nhiệt độ. Với tường công trình, đo đồng thời nhiệt độ không khí hai phía để suy hệ số truyền nhiệt U = q″/(T_in − T_out).'))
    b.append(eq('U = q″/(T_in − T_out) ,   q_rad = ε·σ·(T_s⁴ − T_sur⁴)', '34.2'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Cảm biến thông lượng nhiệt đo ΔT qua lớp cản nhiệt đã biết: q″ = k·ΔT/δ. Chọn Schmidt–Boelter/Gardon cho bức xạ mạnh, màng mỏng cho đáp ứng nhanh, tấm HFS cho công trình. Hiệu chuẩn nguồn chuẩn và lắp đặt đúng độ phát xạ quan trọng hơn bản thân độ nhạy danh định.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 34. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("A heat-flux gauge is a calibrated thermal resistance layer with an embedded thermopile: q'' = k*DeltaT/delta and U = N*S*DeltaT. Schmidt–Boelter gauges are the fire-test reference; Gardon circular-foil gauges respond in about 0.1 s but depend on surface absorptivity; thin-film gauges suit curved hot surfaces; large HFS plates serve building envelopes. Calibration follows ISO 14934 / ASTM C1130. Mounting perturbations (emissivity mismatch, adhesive layer, lead conduction) usually dominate the error, so temperature compensation and matched coating are essential."))
    b.append(eq('q″ = k·ΔT/δ ,   U = N·S·ΔT   ⇒   q″ = (k/(δ·N·S))·U', '34.1'))
    b.append(table(['Type', 'Typical range', 'Response', 'Use'], [['Schmidt–Boelter', '0–100 kW·m⁻²', '≈ 0.3 s', 'Fire-test reference'], ['Gardon', '0–300 kW·m⁻²', '≈ 0.1 s', 'Furnace / arc radiation'], ['Thin film', '0–500 kW·m⁻²', '< 0.01 s', 'Turbine blades, curved surfaces'], ['HFS plate', '0–2 kW·m⁻²', '≈ 1 s', 'Building envelope']], 'Table 34.1 · Heat-flux sensor types.'))
    b.append(eq('U = q″/(T_in − T_out) ,   q_rad = ε·σ·(T_s⁴ − T_sur⁴)', '34.2'))
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
