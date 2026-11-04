# -*- coding: utf-8 -*-
"""Handbook Chapter 33 — Thermal Conductivity Measurement (Đo độ dẫn nhiệt).
Run:  python build/reader_hb_ch33.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch33-thermal-conductivity-measurement'
CH_NO = 33
TITLE_EN = 'Thermal Conductivity Measurement'
TITLE_VI = 'Đo độ dẫn nhiệt'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Độ dẫn nhiệt k (W·m⁻¹·K⁻¹) đặc trưng khả năng dẫn nhiệt của vật liệu và liên hệ với khuếch tán nhiệt α, khối lượng riêng ρ và nhiệt dung riêng c_p qua k = α·ρ·c_p. Phép đo chia làm hai nhóm: trạng thái ổn định (steady-state), cho kết quả tuyệt đối nhưng chậm, và quá độ (transient), nhanh nhưng cần biết thêm tính chất nhiệt của mẫu.'))
    b.append(p('Dải giá trị trải hơn năm bậc: từ ≈ 0,02 W·m⁻¹·K⁻¹ của vật liệu cách nhiệt xốp đến ≈ 400 W·m⁻¹·K⁻¹ của đồng, nên không có một cấu hình đo duy nhất phù hợp cho mọi vật liệu.'))
    b.append(h2('33.1 Định luật Fourier và tấm nóng có bảo vệ', "Fourier's Law and the Guarded Hot Plate"))
    b.append(p('Phương pháp chuẩn ASTM C177 kẹp hai mẫu phẳng giữa tấm nóng chính và hai bản lạnh; vòng bảo vệ (guard ring) giữ cùng nhiệt độ với tấm chính để triệt dòng nhiệt ngang, bảo đảm trường nhiệt một chiều. Với công suất P, diện tích A, chiều dày L và chênh lệch nhiệt độ ΔT giữa hai mặt mẫu, k được suy trực tiếp từ định luật Fourier.'))
    b.append(eq('q = −k ∇T   ⇒   k = (P·L)/(2·A·ΔT)   (hai mẫu đối xứng, mỗi mẫu nhận P/2)', '33.1'))
    b.append(p('Ưu điểm là độ chính xác cao (1–2 %) cho vật liệu cách nhiệt k < 2 W·m⁻¹·K⁻¹; nhược điểm là thời gian đạt cân bằng nhiệt kéo dài hàng giờ, đòi hỏi mẫu phẳng, đủ dày và tiếp xúc nhiệt tốt.'))
    b.append(h2('33.2 Đồng hồ thông lượng nhiệt và phương pháp so sánh', 'Heat Flow Meter and Comparative Methods'))
    b.append(p('ASTM C518 đặt tấm thermopile giữa mẫu và bản lạnh; điện áp ra tỉ lệ với mật độ dòng nhiệt q″. Thiết bị được hiệu chuẩn bằng mẫu chuẩn có k đã biết. Phương pháp thanh so sánh (cut-bar) xếp mẫu nối tiếp với thanh chuẩn và so sánh gradient đo bằng cặp nhiệt điện, thích hợp cho kim loại và chất rắn dẫn nhiệt tốt.'))
    b.append(h2('33.3 Phương pháp quá độ', 'Transient Methods'))
    b.append(p('Dây nóng thoáng qua (transient hot wire) dùng một dây kim loại vừa gia nhiệt vừa làm cảm biến nhiệt độ; độ dốc ΔT theo ln t cho k trực tiếp mà không cần ρ·c_p. Phương pháp chớp laser (laser flash, ASTM E1461) chiếu xung ngắn lên mặt trước đĩa mỏng, ghi đường cong nhiệt độ mặt sau để tính α từ thời gian bán lên nhiệt độ t₁/₂, rồi suy k.'))
    b.append(eq('ΔT = (Q/(4πk))·ln(t₂/t₁) ,   α = 0,1388·L²/t₁/₂ ,   k = α·ρ·c_p', '33.2'))
    b.append(table(['Vật liệu', 'k (W·m⁻¹·K⁻¹)', 'Phương pháp điển hình'], [['Bông thuỷ tinh / xốp', '0,02–0,05', 'Tấm nóng có bảo vệ'], ['Nước (20 °C)', '0,60', 'Dây nóng thoáng qua'], ['Thuỷ tinh', '0,8–1,4', 'C518 / dây nóng'], ['Thép không gỉ', '15', 'Thanh so sánh / chớp laser'], ['Nhôm', '205', 'Chớp laser'], ['Đồng', '400', 'Thanh so sánh']], 'Bảng 33.1 · Giá trị k tham khảo ở nhiệt độ phòng.'))
    b.append(h2('33.4 Nguồn sai số', 'Error Sources'))
    b.append(p('Điện trở tiếp xúc tại mặt mẫu, bức xạ xuyên qua mẫu xốp, đối lưu ở mép, độ ẩm và tính dị hướng là các nguồn sai số chính. Vật liệu dạng sợi phải đo ở mật độ và áp suất xác định; chất lỏng cần lớp mỏng để triệt đối lưu tự nhiên.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('k = (P·L)/(A·ΔT) ở trạng thái ổn định (C177/C518) hoặc k = α·ρ·c_p ở quá độ (dây nóng, chớp laser). Chọn phương pháp theo dải k: tấm có bảo vệ cho cách nhiệt, thanh so sánh và chớp laser cho kim loại. Kiểm soát tiếp xúc nhiệt và đối lưu mép quyết định độ không đảm bảo.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 33. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Thermal conductivity k (W·m⁻¹·K⁻¹) is obtained either from steady-state Fourier conduction (ASTM C177 guarded hot plate, ASTM C518 heat-flow meter) or from transient diffusivity measurements (hot wire, ASTM E1461 laser flash) with k = alpha*rho*cp. Guarded hot plate reaches 1–2 % for insulators but needs hours to equilibrate; laser flash is fast and suits metals. Contact resistance, edge convection, radiation through porous samples, moisture and anisotropy dominate the uncertainty budget.'))
    b.append(eq('q = −k ∇T   ⇒   k = (P·L)/(2·A·ΔT)   (hai mẫu đối xứng, mỗi mẫu nhận P/2)', '33.1'))
    b.append(eq('ΔT = (Q/(4πk))·ln(t₂/t₁) ,   α = 0,1388·L²/t₁/₂ ,   k = α·ρ·c_p', '33.2'))
    b.append(table(['Material', 'k (W·m⁻¹·K⁻¹)', 'Typical method'], [['Glass wool / foam', '0.02–0.05', 'Guarded hot plate'], ['Water (20 °C)', '0.60', 'Transient hot wire'], ['Glass', '0.8–1.4', 'C518 / hot wire'], ['Stainless steel', '15', 'Cut-bar / laser flash'], ['Aluminium', '205', 'Laser flash'], ['Copper', '400', 'Comparative cut-bar']], 'Table 33.1 · Reference k values at room temperature.'))
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
