# -*- coding: utf-8 -*-
"""Handbook Chapter 76 — Blood Flow Measurements (Đo lưu lượng máu).
Run:  python build/reader_hb_ch76.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch76-blood-flow-measurements'
CH_NO = 76
TITLE_EN = 'Blood Flow Measurements'
TITLE_VI = 'Đo lưu lượng máu'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Lưu lượng máu Q (mL·s⁻¹ hoặc L·min⁻¹) quyết định cung lượng tim (CO ≈ 5 L·min⁻¹ ở người nghỉ) và tưới máu mô. Các nguyên lý đo gồm cảm ứng điện từ, siêu âm Doppler, pha loãng chất chỉ thị, nhiệt pha loãng, thể tích kí (plethysmography), laser Doppler và cộng hưởng từ tương phản pha.'))
    b.append(p('Lựa chọn phương pháp là sự thoả hiệp giữa độ xâm lấn, đáp ứng tần số và độ chính xác: trong mổ dùng đầu dò quấn quanh mạch, còn chẩn đoán thường quy ưu tiên siêu âm không xâm lấn.'))
    b.append(h2('76.1 Lưu lượng kế điện từ', 'Electromagnetic Flowmeter'))
    b.append(p('Máu là chất dẫn điện; khi chảy qua từ trường B vuông góc, theo định luật Faraday sinh hiệu điện thế giữa hai electrode đặt hai bên thành mạch. Đầu dò dùng từ trường xoay chiều để triệt điện thế phân cực electrode; cần biết đường kính mạch và hiệu chuẩn zero khi dòng chảy bằng không.'))
    b.append(eq('e = B·l·v ,   Q = (πd²/4)·v = (πd/(4B))·e', '76.1'))
    b.append(h2('76.2 Siêu âm Doppler', 'Ultrasound Doppler'))
    b.append(p('Sóng siêu âm tần số f₀ phản xạ trên hồng cầu chuyển động cho dịch tần số Δf tỉ lệ với vận tốc và cos góc θ giữa chùm tia và trục mạch. Chế độ sóng liên tục (CW) đo vận tốc cao nhưng không phân giải độ sâu; chế độ xung (PW) cho cửa sổ mẫu theo độ sâu nhưng giới hạn bởi tần số lặp xung (aliasing). Góc θ > 60° làm sai số vọt lên rất nhanh, nên chuẩn lâm sàng giữ θ ≤ 60°.'))
    b.append(eq('Δf = (2·f₀·v·cos θ)/c ,   Q = v_mean·A   (c ≈ 1540 m·s⁻¹)', '76.2'))
    b.append(h2('76.3 Pha loãng chỉ thị và nhiệt pha loãng', 'Indicator and Thermodilution'))
    b.append(p('Tiêm bolus chất chỉ thị (thuốc nhuộm indocyanine green, nước muối lạnh hoặc chất phóng xạ) rồi ghi nồng độ C(t) ở hạ lưu. Tích phân đường cong pha loãng theo Stewart–Hamilton cho cung lượng tim; phương pháp Fick dùng chênh lệch oxy động–tĩnh mạch. Thermodilution qua catheter động mạch phổi (Swan–Ganz) là chuẩn lâm sàng, nhưng bị sai lệch khi có hở van ba lá, shunt hoặc tiêm không ổn định.'))
    b.append(eq('CO = (60·I)/∫₀^∞ C(t) dt   ,   CO = VO₂/(C_aO₂ − C_vO₂)   (Fick)', '76.3'))
    b.append(h2('76.4 Vi tuần hoàn và so sánh phương pháp', 'Microcirculation and Comparison'))
    b.append(p('Laser Doppler flowmetry và speckle contrast imaging đo tưới máu mao mạch theo đơn vị tuỳ ý (PU); thể tích kí (venous occlusion plethysmography) đo tăng thể tích chi khi tắc tĩnh mạch tạm thời; phase-contrast MRI cho trường vận tốc 3D không xâm lấn nhưng đắt và chậm.'))
    b.append(table(['Phương pháp', 'Đại lượng', 'Xâm lấn', 'Độ chính xác điển hình'], [['Điện từ', 'Q tức thời mạch hở', 'Rất cao (phẫu thuật)', '± 5 %'], ['Doppler siêu âm', 'v, Q = v·A', 'Không', '± 10–20 %'], ['Thermodilution', 'Cung lượng tim', 'Catheter', '± 10 %'], ['Fick / chỉ thị', 'Cung lượng tim', 'Catheter + máu', '± 5–10 %'], ['Laser Doppler', 'Tưới máu vi mô (PU)', 'Không / tối thiểu', 'Tương đối']], 'Bảng 76.1 · So sánh các phương pháp đo lưu lượng máu.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Q suy từ vận tốc (e = B·l·v cho điện từ, Δf = 2f₀v cos θ/c cho Doppler, θ ≤ 60°) hoặc từ định luật pha loãng (Stewart–Hamilton, Fick). Điện từ chính xác nhưng xâm lấn; Doppler tiện lợi nhưng nhạy góc và diện tích; thermodilution là chuẩn cung lượng tim tại giường bệnh.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 76. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Blood flow is obtained either from velocity (electromagnetic induction e = B*l*v, or Doppler shift df = 2*f0*v*cos(theta)/c with c ≈ 1540 m/s and theta ≤ 60°) times vessel area, or from indicator dilution: CO = 60*I/integral C(t) dt (Stewart–Hamilton) and the Fick relation CO = VO2/(CaO2 − CvO2). Electromagnetic perivascular probes are the most accurate but require surgery; transthoracic/ultrasound Doppler is non-invasive yet angle- and area-sensitive; pulmonary-artery thermodilution remains the bedside reference for cardiac output. Laser Doppler and laser speckle report relative perfusion units.'))
    b.append(eq('e = B·l·v ,   Q = (πd²/4)·v = (πd/(4B))·e', '76.1'))
    b.append(eq('Δf = (2·f₀·v·cos θ)/c ,   Q = v_mean·A   (c ≈ 1540 m·s⁻¹)', '76.2'))
    b.append(eq('CO = (60·I)/∫₀^∞ C(t) dt   ,   CO = VO₂/(C_aO₂ − C_vO₂)   (Fick)', '76.3'))
    b.append(table(['Method', 'Quantity', 'Invasiveness', 'Typical accuracy'], [['Electromagnetic', 'Instantaneous Q, exposed vessel', 'Very high (surgery)', '± 5 %'], ['Doppler ultrasound', 'v, Q = v·A', 'None', '± 10–20 %'], ['Thermodilution', 'Cardiac output', 'Catheter', '± 10 %'], ['Fick / indicator', 'Cardiac output', 'Catheter + blood', '± 5–10 %'], ['Laser Doppler', 'Microvascular perfusion (PU)', 'None / minimal', 'Relative']], 'Table 76.1 · Blood-flow measurement methods.'))
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
